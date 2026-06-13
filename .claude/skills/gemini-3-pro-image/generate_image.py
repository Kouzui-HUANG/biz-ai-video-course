#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GMI Cloud — Gemini 3 Pro Image Preview（Nano Banana Pro）圖像生成 / 編輯
=====================================================================

呼叫 GMI Cloud 的非同步圖像 API（gemini-3-pro-image-preview）：
    1. （選用）--ref-file 本機參考圖會先上傳到臨時圖床 tmpfiles.org 取得公開網址
    2. POST 送出生成 / 編輯請求 → 取得 request_id
    3. 輪詢 GET，直到 success / failed / cancelled
    4. 成功後把 outcome.media_urls 的圖片下載到 outputs/

所有檔案（金鑰、上傳區、下載區）都在本 skill 資料夾內，且皆已 gitignore：
    .gmi_api_key   API 金鑰
    uploads/       本機參考圖暫存區（--ref-file 裸檔名會在此尋找）
    outputs/       生成結果下載區

純 Python 標準函式庫，無需 pip install。Python 3.8+。
完整 API 規格見 references/gmi-api.md。
文件：https://docs.gmicloud.ai/model-quickstarts/image/gemini-3-pro-image-preview

用法（未指定 --count 時，預設一次並行產生 2 張變體）：
    # 文生圖
    python3 generate_image.py --prompt "a cozy cafe interior, warm afternoon light"
    # 只要一張
    python3 generate_image.py --count 1 --prompt "..."
    # 圖生圖（本機參考圖，自動上傳取得網址）
    python3 generate_image.py --ref-file uploads/girl.png --aspect-ratio 1:1 \
        --prompt "change her hairstyle to a short bob, keep everything else identical"
    # 圖生圖（已有公開網址）
    python3 generate_image.py --ref https://example.com/a.png --prompt "..."
"""

import argparse
import json
import mimetypes
import os
import shutil
import sys
import time
import urllib.error
import urllib.request
import uuid
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

# --------------------------------------------------------------------------- #
# API 常數（官方文件，勿改）
# --------------------------------------------------------------------------- #
API_BASE = "https://console.gmicloud.ai/api/v1/ie/requestqueue/apikey/requests"
MODEL = "gemini-3-pro-image-preview"
UPLOAD_API = "https://tmpfiles.org/api/v1/upload"   # 臨時圖床，約 1 小時自動刪除
# 部分圖床 / CDN 會封鎖預設的 Python-urllib UA（回 403），需偽裝成瀏覽器
USER_AGENT = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

# 本 skill 資料夾內的固定路徑
SKILL_DIR = Path(__file__).resolve().parent
KEY_FILE = SKILL_DIR / ".gmi_api_key"
UPLOADS_DIR = SKILL_DIR / "uploads"
OUTPUTS_DIR = SKILL_DIR / "outputs"

# 合法選項
VALID_IMAGE_SIZES = ["1K", "2K", "4K"]
VALID_ASPECT_RATIOS = ["1:1", "4:5", "5:4", "3:4", "4:3", "9:16", "16:9", "21:9"]
VALID_OUTPUT_FORMATS = ["png", "jpeg"]
REF_IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".heic", ".heif"}
MAX_PROMPT_CHARS = 2000
MAX_REF_IMAGES = 14
MAX_REF_BYTES = 7 * 1024 * 1024  # 單張參考圖 7MB 上限
DEFAULT_COUNT = 2                # 未指定 --count 時，預設一次產生 2 張變體
MAX_COUNT = 8                    # 張數上限，防止誤輸入大數字耗盡額度

TERMINAL_OK = "success"
TERMINAL_FAIL = {"failed", "cancelled"}


# --------------------------------------------------------------------------- #
# HTTP 小工具（帶 Bearer 驗證）
# --------------------------------------------------------------------------- #
def _request(method, url, api_key, body=None, timeout=60):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": USER_AGENT,
    }
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"[HTTP {e.code}] {method} {url} 失敗：\n{detail}") from e
    except urllib.error.URLError as e:
        raise SystemExit(f"[網路錯誤] 無法連線 {url}：{e.reason}") from e


# --------------------------------------------------------------------------- #
# 上傳區：本機參考圖 → 臨時公開網址（GMI 只接受公開 URL）
# --------------------------------------------------------------------------- #
def upload_reference(path, timeout=120):
    """把本機圖上傳到 tmpfiles.org，回傳可公開存取的直連網址。"""
    p = Path(path)
    if not p.exists():                       # 裸檔名 → 改在 uploads/ 內尋找
        alt = UPLOADS_DIR / p.name
        if alt.exists():
            p = alt
        else:
            raise SystemExit(f"[錯誤] 找不到參考圖檔：{path}")
    if p.suffix.lower() not in REF_IMAGE_EXTS:
        raise SystemExit(f"[錯誤] 不支援的格式 {p.suffix}（限 {', '.join(sorted(REF_IMAGE_EXTS))}）")
    size = p.stat().st_size
    if size > MAX_REF_BYTES:
        raise SystemExit(f"[錯誤] {p.name} 為 {size/1048576:.1f}MB，超過 7MB 上限，請先縮圖。")

    data = p.read_bytes()
    ctype = mimetypes.guess_type(p.name)[0] or "application/octet-stream"
    boundary = "----gmi" + uuid.uuid4().hex
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{p.name}"\r\n'
        f"Content-Type: {ctype}\r\n\r\n"
    ).encode("utf-8") + data + f"\r\n--{boundary}--\r\n".encode("utf-8")

    req = urllib.request.Request(
        UPLOAD_API, data=body,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}",
                 "User-Agent": USER_AGENT},
        method="POST",
    )
    print(f"⬆️  上傳參考圖 {p.name}（{size/1048576:.1f}MB）到 tmpfiles.org（約 1 小時後自動刪除）…")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            result = json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, json.JSONDecodeError) as e:
        raise SystemExit(f"[錯誤] 上傳失敗：{e}") from e

    url = (result.get("data") or {}).get("url")
    if not url:
        raise SystemExit(f"[錯誤] 上傳回應缺少網址：{json.dumps(result, ensure_ascii=False)}")
    url = url.replace("tmpfiles.org/", "tmpfiles.org/dl/")   # 轉成直連下載網址
    _verify_image_url(url)
    print(f"   ✔ 公開網址：{url}")
    return url


def _verify_image_url(url, timeout=60):
    """確認網址確實回傳圖片，避免送出無效參考圖而浪費額度。"""
    try:
        req = urllib.request.Request(url, method="GET", headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            ctype = resp.headers.get("Content-Type", "")
            resp.read(512)
    except urllib.error.URLError as e:
        raise SystemExit(f"[錯誤] 參考圖網址無法存取：{url}（{e}）") from e
    if not ctype.lower().startswith("image/"):
        raise SystemExit(f"[錯誤] 參考圖網址未回傳圖片（Content-Type={ctype}）：{url}")


# --------------------------------------------------------------------------- #
# 送出 / 輪詢 / 下載
# --------------------------------------------------------------------------- #
def submit_request(api_key, payload, timeout=300):
    # GMI 常在 POST 內同步完成生成才回應，故 POST 可能阻塞數十秒～數分鐘，
    # timeout 須放寬（與 --timeout 一致），不能用預設的 60s。
    resp = _request("POST", API_BASE, api_key, body={"model": MODEL, "payload": payload}, timeout=timeout)
    request_id = resp.get("request_id")
    if not request_id:
        raise SystemExit(f"[錯誤] 回應缺少 request_id：{json.dumps(resp, ensure_ascii=False)}")
    print(f"✅ 已送出 request_id={request_id}（{resp.get('status', '?')}）")
    return request_id


def poll_request(api_key, request_id, interval, timeout):
    url = f"{API_BASE}/{request_id}"
    deadline = time.time() + timeout
    last = None
    while True:
        resp = _request("GET", url, api_key)
        status = resp.get("status", "unknown")
        if status != last:
            print(f"⏳ {status}")
            last = status
        if status == TERMINAL_OK:
            return resp
        if status in TERMINAL_FAIL:
            raise SystemExit(f"[失敗] 狀態 '{status}'：{json.dumps(resp, ensure_ascii=False)}")
        if time.time() > deadline:
            raise SystemExit(f"[逾時] 超過 {timeout}s，最後狀態 '{status}'。")
        time.sleep(interval)


def download_images(resp, out_dir, ext):
    media = (resp.get("outcome") or {}).get("media_urls") or []
    if not media:
        raise SystemExit(f"[錯誤] 成功但無 media_urls：{json.dumps(resp, ensure_ascii=False)}")
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    rid = resp.get("request_id", "output")
    saved = []
    for item in media:
        url = item.get("url")
        if not url:
            continue
        dest = out_dir / f"{rid}_{item.get('id', len(saved))}.{ext}"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as fh:
                shutil.copyfileobj(r, fh)
        except (urllib.error.URLError, OSError) as e:
            print(f"⚠️  下載失敗 {url}：{e}", file=sys.stderr)
            continue
        print(f"🖼️  已存檔：{dest}")
        saved.append(dest)
    return saved


# --------------------------------------------------------------------------- #
# 金鑰 / 參數
# --------------------------------------------------------------------------- #
def read_key_file():
    try:
        return KEY_FILE.read_text(encoding="utf-8").strip() or None
    except FileNotFoundError:
        return None


def resolve_api_key(cli_key):
    """金鑰來源優先序：--api-key 旗標 > 環境變數 GMI_API_KEY > .gmi_api_key 檔。"""
    return cli_key or os.environ.get("GMI_API_KEY") or read_key_file()


def build_parser():
    p = argparse.ArgumentParser(
        description="呼叫 GMI Cloud gemini-3-pro-image-preview（Nano Banana Pro）生成 / 編輯圖片。",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--prompt", required=True, help=f"圖片描述（≤ {MAX_PROMPT_CHARS} 字元）")
    p.add_argument("--ref", dest="refs", action="append", default=[], metavar="URL",
                   help="參考圖『公開網址』，可重複指定")
    p.add_argument("--ref-file", dest="ref_files", action="append", default=[], metavar="PATH",
                   help="參考圖『本機路徑』，自動上傳取得網址，可重複（裸檔名會在 uploads/ 內尋找）")
    p.add_argument("--image-size", default="2K", choices=VALID_IMAGE_SIZES, help="輸出解析度")
    p.add_argument("--aspect-ratio", default="16:9", choices=VALID_ASPECT_RATIOS,
                   help="長寬比；做圖片編輯時建議改成與來源圖一致（如方形用 1:1）")
    p.add_argument("--output-format", default="png", choices=VALID_OUTPUT_FORMATS, help="輸出格式")
    p.add_argument("--count", type=int, default=DEFAULT_COUNT,
                   help=f"生成張數，每張為一次獨立 API 請求並行送出（上限 {MAX_COUNT}）")
    p.add_argument("--out-dir", default=str(OUTPUTS_DIR), help="下載資料夾")
    p.add_argument("--api-key", default=None,
                   help="API 金鑰（預設序：此旗標 → $GMI_API_KEY → .gmi_api_key 檔）")
    p.add_argument("--poll-interval", type=float, default=3.0, help="輪詢間隔秒數")
    p.add_argument("--timeout", type=float, default=300.0, help="最長等待秒數")
    return p


def main():
    args = build_parser().parse_args()

    api_key = resolve_api_key(args.api_key)
    if not api_key:
        raise SystemExit(f"[錯誤] 找不到 API 金鑰。請建立金鑰檔 {KEY_FILE}，或用 --api-key / $GMI_API_KEY。")
    if len(args.prompt) > MAX_PROMPT_CHARS:
        raise SystemExit(f"[錯誤] prompt 超過 {MAX_PROMPT_CHARS} 字元（目前 {len(args.prompt)}）。")
    if not 1 <= args.count <= MAX_COUNT:
        raise SystemExit(f"[錯誤] --count 須在 1～{MAX_COUNT} 之間（目前 {args.count}）。")

    # 參考圖：本機檔先上傳取得網址，再與直接給的公開網址合併
    refs = list(args.refs)
    for f in args.ref_files:
        refs.append(upload_reference(f))
    if len(refs) > MAX_REF_IMAGES:
        raise SystemExit(f"[錯誤] 參考圖最多 {MAX_REF_IMAGES} 張（目前 {len(refs)}）。")

    payload = {
        "prompt": args.prompt,
        "image_size": args.image_size,
        "aspect_ratio": args.aspect_ratio,
        "image_output_format": args.output_format,
    }
    if refs:
        payload["image"] = refs

    print("📤 送出生成請求：")
    print(json.dumps({"model": MODEL, "payload": payload}, ensure_ascii=False, indent=2))

    if args.count > 1:
        print(f"🔁 相同參數並行送出 {args.count} 次請求，產生 {args.count} 張變體…")

    # POST 常阻塞到生成完成才回應，多張時須並行送出，總耗時才不會隨張數線性增加
    with ThreadPoolExecutor(max_workers=args.count) as pool:
        futures = [pool.submit(submit_request, api_key, payload, args.timeout)
                   for _ in range(args.count)]
        request_ids = [f.result() for f in futures]

    ext = "jpg" if args.output_format == "jpeg" else "png"
    saved = []
    for request_id in request_ids:
        final = poll_request(api_key, request_id, args.poll_interval, args.timeout)
        saved += download_images(final, args.out_dir, ext)
    print(f"\n🎉 完成，共產生 {len(saved)} 張圖片於 {Path(args.out_dir).resolve()}")


if __name__ == "__main__":
    main()
