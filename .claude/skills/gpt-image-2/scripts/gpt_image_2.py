"""Generate or edit images with GMI Cloud's gpt-image-2 models.

GMI Cloud exposes an async request-queue API:
    POST https://console.gmicloud.ai/api/v1/ie/requestqueue/apikey/requests
    GET  https://console.gmicloud.ai/api/v1/ie/requestqueue/apikey/requests/{request_id}

Submit returns a `request_id`; poll the GET endpoint until the job carries an
`outcome.media_urls`, then download each public image URL.

Mode auto-detection (override with --mode):
    * No input image  -> gpt-image-2-generate  (text-to-image)
    * Input image(s)  -> gpt-image-2-edit       (one request per image)

Prompt sources:
    --prompt "text ..."            inline string
    --prompt @path/to/prompt.txt   read from a UTF-8 file

Defaults: quality=medium, output_format=png, size=1920x1088, n=2.

Note on size: gpt-image-2 accepts any WxH with edges multiple of 16, longest
edge <= 3840, aspect <= 3:1, total pixels 0.65M-8.3M. Exact 1920x1080 is
rejected (1080 isn't divisible by 16) — use 1920x1088.

Edit-source images resolve against the skill's uploads/ drop-zone (UPLOADS_DIR)
in addition to the CWD and project root, so a bare filename or a directory path
both work. A directory ref expands to every supported image directly inside it.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import time
from pathlib import Path

import requests
from dotenv import load_dotenv


MODEL_GENERATE = "gpt-image-2-generate"
MODEL_EDIT = "gpt-image-2-edit"

DEFAULT_SIZE = "1920x1088"  # native 16:9 HD (1080 padded up to nearest x16)
# gpt-image-2 accepts ANY size meeting these constraints (verified live against
# GMI), not a fixed list. Edges must be multiples of 16 — so exact 1920x1080 is
# rejected; use 1920x1088.
SIZE_MAX_EDGE = 3840
SIZE_MIN_PIXELS = 655_360
SIZE_MAX_PIXELS = 8_294_400
SIZE_MAX_ASPECT = 3.0
COMMON_SIZES = "1024x1024, 1536x1024, 1024x1536, 1792x1024, 1920x1088, 2048x1152, auto"
DEFAULT_QUALITY = "medium"
VALID_QUALITY = {"low", "medium", "high", "auto"}
DEFAULT_FORMAT = "png"
VALID_FORMAT = {"png", "jpeg"}
DEFAULT_N = 2

SUBMIT_PATH = "/api/v1/ie/requestqueue/apikey/requests"
POLL_INTERVAL_SEC = 2
POLL_TIMEOUT_SEC = 600
# Edit submits carry a large base64 payload; the queue can take a while to ack.
# Multi-image edits (image array) and full-resolution sources are heavier and
# often complete inline, so the read timeout doubles as the inline-result cap.
# 300s proved too tight for those, so use a (connect, read) tuple with a generous
# read. Override with $GMI_SUBMIT_READ_TIMEOUT to push it higher still.
SUBMIT_CONNECT_TIMEOUT_SEC = 30
SUBMIT_READ_TIMEOUT_SEC = int(os.environ.get("GMI_SUBMIT_READ_TIMEOUT", "600"))

SUPPORTED_EXTS = {".png", ".jpg", ".jpeg", ".webp"}
EXT = {"png": ".png", "jpeg": ".jpg", "webp": ".webp"}
MIME = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp"}

TERMINAL_OK = {"success", "succeeded", "finished", "completed", "done"}
TERMINAL_FAIL = {"failed", "error", "errored", "cancelled", "canceled", "timeout", "expired"}


def find_project_root(start: Path) -> Path:
    for d in (start, *start.parents):
        if (d / ".env").exists():
            return d
    return start


ROOT = find_project_root(Path.cwd())
SKILL_DIR = Path(__file__).resolve().parent.parent  # .claude/skills/gpt-image-2
KEY_FILE = SKILL_DIR / ".gmi_api_key"
UPLOADS_DIR = SKILL_DIR / "uploads"   # default drop-zone for edit-source images
OUTPUT_DIR = SKILL_DIR / "outputs"    # default destination for generated/edited images


# --------------------------------------------------------------------------- #
# Config / input helpers
# --------------------------------------------------------------------------- #

def read_key_file() -> str | None:
    try:
        return KEY_FILE.read_text(encoding="utf-8").strip() or None
    except FileNotFoundError:
        return None


def load_config(cli_key: str | None = None) -> dict:
    """Resolve the GMI key, priority: --api-key > $GMI_API_KEY (incl. .env) > .gmi_api_key file."""
    load_dotenv(ROOT / ".env")
    endpoint = os.getenv("GMI_ENDPOINT", "https://console.gmicloud.ai").rstrip("/")
    api_key = (cli_key or os.getenv("GMI_API_KEY") or read_key_file() or "").strip()
    if not api_key:
        sys.exit(
            "[!] No GMI API key found. Provide one of:\n"
            "      --api-key <key>\n"
            "      GMI_API_KEY=... in project .env\n"
            f"      a key file at {KEY_FILE}\n"
            "    Get a key from https://console.gmicloud.ai (User Console -> API Keys)."
        )
    return {"endpoint": endpoint, "api_key": api_key}


def resolve_prompt(raw: str) -> str:
    """Inline text, or '@path' to read the prompt from a UTF-8 file."""
    if not raw.startswith("@"):
        return raw
    p = Path(raw[1:]).expanduser()
    if not p.is_absolute():
        p = ROOT / p
    return p.read_text(encoding="utf-8").strip()


def is_url(s: str) -> bool:
    return s.startswith("http://") or s.startswith("https://")


def resolve_image_path(ref: str) -> Path:
    """Resolve a local image/dir ref to a path.

    Search order for relative refs: current working directory, project root,
    then the skill's uploads/ drop-zone (UPLOADS_DIR). Absolute paths and the
    first existing candidate win; otherwise fall back to a root-relative path so
    callers surface a clear not-found error.
    """
    p = Path(ref).expanduser()
    if p.is_absolute():
        return p
    for base in (Path.cwd(), ROOT, UPLOADS_DIR):
        cand = base / p
        if cand.exists():
            return cand
    return ROOT / p


def encode_image(ref: str, as_data_url: bool) -> str:
    """Return the value for the payload `image`/`mask` field.

    URLs pass through untouched. Local files are base64-encoded — raw base64 by
    default (matches GMI's "base64-encoded image or url"), or a data URL when
    --data-url is set (fallback if the API rejects raw base64).
    """
    if is_url(ref):
        return ref
    p = resolve_image_path(ref)
    if not p.is_file():
        raise FileNotFoundError(
            f"image not found: {ref} (searched CWD, {ROOT}, {UPLOADS_DIR})"
        )
    b64 = base64.b64encode(p.read_bytes()).decode()
    if as_data_url:
        mime = MIME.get(p.suffix.lower(), "image/png")
        return f"data:{mime};base64,{b64}"
    return b64


def source_stem(ref: str) -> str:
    """A filesystem-safe stem for naming outputs derived from an edit source."""
    base = Path(ref.split("?")[0].rstrip("/")).stem or "image"
    return re.sub(r"[^A-Za-z0-9_-]+", "_", base).strip("_")[:40] or "image"


def expand_image_refs(refs: list[str]) -> list[str]:
    """Expand any directory ref into the supported image files directly inside
    it (sorted by name). URLs and file refs pass through unchanged. Lets callers
    point at the uploads/ drop-zone to edit every image in it at once.
    """
    out: list[str] = []
    for ref in refs:
        if is_url(ref):
            out.append(ref)
            continue
        p = resolve_image_path(ref)
        if p.is_dir():
            imgs = sorted(
                q for q in p.iterdir()
                if q.is_file() and q.suffix.lower() in SUPPORTED_EXTS
            )
            if not imgs:
                print(f"[!] no supported images found in {p}", file=sys.stderr)
            out.extend(str(q) for q in imgs)
        else:
            out.append(ref)
    return out


# --------------------------------------------------------------------------- #
# GMI request-queue API
# --------------------------------------------------------------------------- #

def submit(cfg: dict, model: str, payload: dict) -> dict:
    url = f"{cfg['endpoint']}{SUBMIT_PATH}"
    headers = {
        "Authorization": f"Bearer {cfg['api_key']}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    body = {"model": model, "payload": payload}
    resp = requests.post(
        url, headers=headers, data=json.dumps(body),
        timeout=(SUBMIT_CONNECT_TIMEOUT_SEC, SUBMIT_READ_TIMEOUT_SEC),
    )
    if resp.status_code >= 400:
        raise RuntimeError(f"submit failed HTTP {resp.status_code}: {resp.text[:600]}")
    return resp.json()


def extract_outcome(data: dict) -> dict | None:
    outcome = data.get("outcome") or {}
    if outcome.get("media_urls"):
        return outcome
    return None


def poll(cfg: dict, request_id: str) -> dict:
    url = f"{cfg['endpoint']}{SUBMIT_PATH}/{request_id}"
    headers = {"Authorization": f"Bearer {cfg['api_key']}", "Accept": "application/json"}
    deadline = time.time() + POLL_TIMEOUT_SEC
    last_status = None
    while time.time() < deadline:
        time.sleep(POLL_INTERVAL_SEC)
        resp = requests.get(url, headers=headers, timeout=60)
        if resp.status_code >= 400:
            print(f"[poll] HTTP {resp.status_code}: {resp.text[:300]}")
            continue
        data = resp.json()
        status = str(data.get("status", "")).lower()
        if status != last_status:
            print(f"[poll] status={status or '?'}")
            last_status = status
        outcome = extract_outcome(data)
        if outcome:
            return outcome
        if status in TERMINAL_OK:
            raise RuntimeError(f"job reported {status} but returned no media_urls: {json.dumps(data)[:400]}")
        if status in TERMINAL_FAIL:
            raise RuntimeError(f"job {status}: {data.get('error') or json.dumps(data)[:400]}")
    raise RuntimeError(f"request {request_id} timed out after {POLL_TIMEOUT_SEC}s")


def run_request(cfg: dict, model: str, payload: dict) -> list[str]:
    """Submit one job, wait for it, and return the list of result image URLs."""
    data = submit(cfg, model, payload)
    outcome = extract_outcome(data)
    if outcome is None:
        request_id = (
            data.get("request_id")
            or (data.get("data") or {}).get("request_id")
            or data.get("id")
        )
        if not request_id:
            raise RuntimeError(f"no request_id or outcome in submit response: {json.dumps(data)[:400]}")
        print(f"[submit] request_id={request_id} status={data.get('status', '?')}")
        outcome = poll(cfg, request_id)
    else:
        print(f"[submit] completed inline (no polling needed)")
    return [m["url"] for m in outcome.get("media_urls", []) if m.get("url")]


def download(urls: list[str], stem: str, fmt: str) -> list[Path]:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    suffix = EXT.get(fmt, ".png")
    saved: list[Path] = []
    multi = len(urls) > 1
    for idx, url in enumerate(urls, 1):
        resp = requests.get(url, timeout=120)
        if resp.status_code >= 400:
            print(f"[!] download skipped {url} ({resp.status_code})", file=sys.stderr)
            continue
        name = f"{stem}_{idx}{suffix}" if multi else f"{stem}{suffix}"
        out = OUTPUT_DIR / name
        out.write_bytes(resp.content)
        saved.append(out)
        print(f"[✓] {out} ({len(resp.content)} bytes)")
    return saved


# --------------------------------------------------------------------------- #
# Modes
# --------------------------------------------------------------------------- #

def run_generate(cfg: dict, prompt: str, args: argparse.Namespace) -> list[Path]:
    payload = {
        "prompt": prompt,
        "size": args.size,
        "quality": args.quality,
        "output_format": args.output_format,
        "n": args.n,
    }
    print(f"[mode] generate ({MODEL_GENERATE}) size={args.size} quality={args.quality} n={args.n}")
    urls = run_request(cfg, MODEL_GENERATE, payload)
    stamp = time.strftime("%Y%m%d_%H%M%S")
    return download(urls, f"gptgen_{stamp}", args.output_format)


def run_edit_one(cfg: dict, prompt: str, image_ref: str, args: argparse.Namespace) -> list[Path]:
    payload = {
        "prompt": prompt,
        "image": encode_image(image_ref, args.data_url),
        "size": args.size,
        "quality": args.quality,
        "output_format": args.output_format,
        "n": args.n,
    }
    if args.mask:
        payload["mask"] = encode_image(args.mask, args.data_url)
    label = image_ref if is_url(image_ref) else Path(image_ref).name
    print(f"[mode] edit ({MODEL_EDIT}) src={label} size={args.size} quality={args.quality} n={args.n}")
    urls = run_request(cfg, MODEL_EDIT, payload)
    return download(urls, f"{source_stem(image_ref)}_gptedit", args.output_format)


def run_edit_multi(cfg: dict, prompt: str, image_refs: list[str], args: argparse.Namespace) -> list[Path]:
    """Send ALL inputs as one edit request — the API accepts `image` as an array,
    so the model composites every reference into a single output (e.g. two
    characters into one scene). Contrast with run_edit_one, which loops."""
    payload = {
        "prompt": prompt,
        "image": [encode_image(ref, args.data_url) for ref in image_refs],
        "size": args.size,
        "quality": args.quality,
        "output_format": args.output_format,
        "n": args.n,
    }
    if args.mask:
        payload["mask"] = encode_image(args.mask, args.data_url)
    labels = [ref if is_url(ref) else Path(ref).name for ref in image_refs]
    print(f"[mode] edit-multi ({MODEL_EDIT}) srcs={labels} size={args.size} "
          f"quality={args.quality} n={args.n}")
    urls = run_request(cfg, MODEL_EDIT, payload)
    stem = "_".join(source_stem(r) for r in image_refs)[:60] or "image"
    return download(urls, f"{stem}_gptedit", args.output_format)


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Generate or edit images with GMI Cloud gpt-image-2."
    )
    p.add_argument("images", nargs="*",
                   help="Input image path(s) or URL(s). Any present -> edit mode (one request each).")
    p.add_argument("-p", "--prompt", required=True,
                   help="Prompt text, or @path/to/file.txt to load from a UTF-8 file.")
    p.add_argument("-m", "--mode", choices=("auto", "generate", "edit"), default="auto",
                   help="auto (default): edit if any image given, else generate.")
    p.add_argument("--image", action="append", default=[], dest="image_flags",
                   help="Additional input image path/URL for edit mode (repeatable).")
    p.add_argument("--multi", action="store_true",
                   help="Edit mode: send ALL inputs as one request (image array) so the "
                        "model composites them into a single output, instead of one request per image.")
    p.add_argument("--mask", default=None,
                   help="Optional inpainting mask (path/URL), same size as the image. Edit mode only.")
    p.add_argument("-s", "--size", default=DEFAULT_SIZE,
                   help=f"WxH, edges multiple of 16, max edge {SIZE_MAX_EDGE}, aspect <=3:1 "
                        f"(default: {DEFAULT_SIZE}; exact 1920x1080 is invalid). Common: {COMMON_SIZES}.")
    p.add_argument("-q", "--quality", default=DEFAULT_QUALITY,
                   help=f"One of {sorted(VALID_QUALITY)} (default: {DEFAULT_QUALITY}).")
    p.add_argument("-f", "--output-format", default=DEFAULT_FORMAT, dest="output_format",
                   help=f"One of {sorted(VALID_FORMAT)} (default: {DEFAULT_FORMAT}).")
    p.add_argument("-n", "--n", type=int, default=DEFAULT_N,
                   help=f"Number of images per request, 1-10 (default: {DEFAULT_N}).")
    p.add_argument("--data-url", action="store_true",
                   help="Send local edit images as data: URLs instead of raw base64 (fallback if edit is rejected).")
    p.add_argument("--api-key", default=None,
                   help="GMI API key (priority: this flag > $GMI_API_KEY > .gmi_api_key file).")
    return p.parse_args()


def check_size(size: str) -> str | None:
    """Return an error string if size is invalid, else None. Accepts 'auto'."""
    if size == "auto":
        return None
    mt = re.fullmatch(r"(\d+)x(\d+)", size.strip())
    if not mt:
        return "format must be WxH (e.g. 1920x1088) or 'auto'"
    w, h = int(mt.group(1)), int(mt.group(2))
    problems = []
    if w % 16 or h % 16:
        problems.append(f"edges must be multiples of 16 (nearest valid: {round(w / 16) * 16}x{round(h / 16) * 16})")
    if max(w, h) > SIZE_MAX_EDGE:
        problems.append(f"longest edge must be <= {SIZE_MAX_EDGE}")
    if max(w, h) / min(w, h) > SIZE_MAX_ASPECT:
        problems.append("aspect ratio must be <= 3:1")
    if w * h < SIZE_MIN_PIXELS:
        problems.append(f"total pixels must be >= {SIZE_MIN_PIXELS:,}")
    if w * h > SIZE_MAX_PIXELS:
        problems.append(f"total pixels must be <= {SIZE_MAX_PIXELS:,}")
    return "; ".join(problems) or None


def validate(args: argparse.Namespace) -> None:
    size_err = check_size(args.size)
    if size_err:
        sys.exit(f"[!] --size {args.size} invalid: {size_err}. Common: {COMMON_SIZES}.")
    if args.quality not in VALID_QUALITY:
        sys.exit(f"[!] --quality must be one of {sorted(VALID_QUALITY)}.")
    if args.output_format not in VALID_FORMAT:
        sys.exit(f"[!] --output-format must be one of {sorted(VALID_FORMAT)}.")
    if not 1 <= args.n <= 10:
        sys.exit("[!] --n must be between 1 and 10.")


def main() -> None:
    args = parse_args()
    validate(args)

    prompt = resolve_prompt(args.prompt)
    if not prompt:
        sys.exit("[!] Empty prompt.")

    image_refs = list(args.images) + list(args.image_flags)
    if args.mode == "generate":
        image_refs = []
    else:
        image_refs = expand_image_refs(image_refs)
        if args.mode == "edit" and not image_refs:
            sys.exit("[!] --mode edit requires at least one input image (positional or --image).")

    cfg = load_config(args.api_key)  # API-key gate last, after all input validation

    do_edit = bool(image_refs)
    total = 0
    failures = 0

    if not do_edit:
        try:
            total += len(run_generate(cfg, prompt, args))
        except Exception as e:
            print(f"[!] generate failed: {e}", file=sys.stderr)
            failures += 1
    elif args.multi:
        print(f"[batch] edit-multi: {len(image_refs)} image(s) -> 1 request")
        try:
            total += len(run_edit_multi(cfg, prompt, image_refs, args))
        except Exception as e:
            print(f"[!] edit-multi failed: {e}", file=sys.stderr)
            failures += 1
    else:
        print(f"[batch] edit {len(image_refs)} image(s)")
        for ref in image_refs:
            try:
                total += len(run_edit_one(cfg, prompt, ref, args))
            except Exception as e:
                print(f"[!] {ref}: {e}", file=sys.stderr)
                failures += 1

    print(f"[done] saved {total} image(s) to {OUTPUT_DIR}" + (f"; {failures} failure(s)" if failures else ""))
    sys.exit(2 if failures else 0)


if __name__ == "__main__":
    main()
