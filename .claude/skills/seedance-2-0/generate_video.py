#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GMI Cloud — Seedance 2.0（seedance-2-0-260128）影片生成
========================================================

呼叫 GMI Cloud 的非同步影片 API（seedance-2-0-260128）：
    1. （選用）--ref-file / --first-frame-file / --last-frame-file 等本機素材
       會先上傳到臨時檔案床 tmpfiles.org 取得公開網址
    2. POST 送出生成請求 → 取得 request_id
    3. 輪詢 GET，直到 success / failed / cancelled
    4. 成功後把 outcome.video_url（與縮圖 thumbnail_image_url）下載到 outputs/

所有檔案（金鑰、上傳區、下載區）都在本 skill 資料夾內，且皆已 gitignore：
    .gmi_api_key   API 金鑰（找不到時退回 ../gemini-3-pro-image/.gmi_api_key，同一把 GMI 金鑰）
    uploads/       本機參考素材暫存區（裸檔名會在此尋找）
    outputs/       生成結果下載區

純 Python 標準函式庫，無需 pip install。Python 3.8+。
完整 API 規格見 references/gmi-api.md。
文件：https://docs.gmicloud.ai/model-quickstarts/video/seedance-2-0-260128

生成模式（依給的素材自動決定，毋須旗標）：
    文生影 T2V   只給 --prompt
    參考生影 R2V  --ref / --ref-file（使用者給圖且未指明首尾幀時的『預設』模式）
    圖生影 I2V   --first-frame(-file) / --last-frame(-file) 首尾幀錨定（需使用者明確要求）

用法（未指定 --count 時，預設一次並行產生 2 支變體；解析度預設 720p）：
    # 文生影
    python3 generate_video.py --prompt "A thunderstorm rolls over a medieval castle at night"
    # 參考生影（本機圖自動上傳；R2V 預設模式）
    python3 generate_video.py --ref-file uploads/girl.png \
        --prompt "The character walks through a neon-lit alley, cinematic"
    # 首尾幀圖生影（I2V）
    python3 generate_video.py --first-frame-file uploads/bud.jpg --last-frame-file uploads/bloom.jpg \
        --prompt "The flower slowly blooms, petals unfurling in morning light"
    # 只要一支
    python3 generate_video.py --count 1 --prompt "..."
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
MODEL = "seedance-2-0-260128"
UPLOAD_API = "https://tmpfiles.org/api/v1/upload"   # 臨時檔案床，約 1 小時自動刪除
# 部分檔案床 / CDN 會封鎖預設的 Python-urllib UA（回 403），需偽裝成瀏覽器
USER_AGENT = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

# 本 skill 資料夾內的固定路徑
SKILL_DIR = Path(__file__).resolve().parent
KEY_FILE = SKILL_DIR / ".gmi_api_key"
# 同平台同一把金鑰：本資料夾沒有金鑰檔時，退回姊妹 skill 的金鑰檔
SIBLING_KEY_FILE = SKILL_DIR.parent / "gemini-3-pro-image" / ".gmi_api_key"
UPLOADS_DIR = SKILL_DIR / "uploads"
OUTPUTS_DIR = SKILL_DIR / "outputs"

# 合法選項（官方文件）
VALID_RESOLUTIONS = ["480p", "720p", "1080p"]
VALID_RATIOS = ["16:9", "4:3", "1:1", "3:4", "9:16", "21:9", "adaptive"]
MIN_DURATION, MAX_DURATION = 4, 15
MAX_SEED = 4294967295

# 本機素材上傳的副檔名白名單與大小護欄（官方未定上限；tmpfiles 上限 100MB）
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".heic", ".heif"}
VIDEO_EXTS = {".mp4", ".mov", ".webm", ".m4v"}
AUDIO_EXTS = {".mp3", ".wav", ".m4a", ".aac", ".ogg", ".flac"}
KIND_RULES = {
    "image": (IMAGE_EXTS, 10 * 1024 * 1024),
    "video": (VIDEO_EXTS, 50 * 1024 * 1024),
    "audio": (AUDIO_EXTS, 20 * 1024 * 1024),
}
MAX_REF_IMAGES = 9               # 官方未明定，腳本側護欄
DEFAULT_COUNT = 2                # 未指定 --count 時，預設一次產生 2 支變體
MAX_COUNT = 4                    # 支數上限——影片昂貴，防止誤輸入大數字耗盡額度

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
# 上傳區：本機素材 → 臨時公開網址（GMI 只接受公開 URL）
# --------------------------------------------------------------------------- #
def upload_asset(path, kind, timeout=300):
    """把本機素材上傳到 tmpfiles.org，回傳可公開存取的直連網址。"""
    exts, max_bytes = KIND_RULES[kind]
    p = Path(path)
    if not p.exists():                       # 裸檔名 → 改在 uploads/ 內尋找
        alt = UPLOADS_DIR / p.name
        if alt.exists():
            p = alt
        else:
            raise SystemExit(f"[錯誤] 找不到素材檔：{path}")
    if p.suffix.lower() not in exts:
        raise SystemExit(f"[錯誤] {p.name} 不是支援的{kind}格式（限 {', '.join(sorted(exts))}）")
    size = p.stat().st_size
    if size > max_bytes:
        raise SystemExit(f"[錯誤] {p.name} 為 {size/1048576:.1f}MB，超過 {max_bytes//1048576}MB 護欄，請先壓縮。")

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
    print(f"⬆️  上傳{kind}素材 {p.name}（{size/1048576:.1f}MB）到 tmpfiles.org（約 1 小時後自動刪除）…")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            result = json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, json.JSONDecodeError) as e:
        raise SystemExit(f"[錯誤] 上傳失敗：{e}") from e

    url = (result.get("data") or {}).get("url")
    if not url:
        raise SystemExit(f"[錯誤] 上傳回應缺少網址：{json.dumps(result, ensure_ascii=False)}")
    url = url.replace("tmpfiles.org/", "tmpfiles.org/dl/")   # 轉成直連下載網址
    _verify_asset_url(url, kind)
    print(f"   ✔ 公開網址：{url}")
    return url


def _verify_asset_url(url, kind, timeout=60):
    """確認網址確實可存取，避免送出無效素材而浪費額度。圖片嚴格驗 Content-Type，影音從寬。"""
    try:
        req = urllib.request.Request(url, method="GET", headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            ctype = resp.headers.get("Content-Type", "")
            resp.read(512)
    except urllib.error.URLError as e:
        raise SystemExit(f"[錯誤] 素材網址無法存取：{url}（{e}）") from e
    ctype = ctype.lower()
    if kind == "image":
        if not ctype.startswith("image/"):
            raise SystemExit(f"[錯誤] 素材網址未回傳圖片（Content-Type={ctype}）：{url}")
    elif not (ctype.startswith(f"{kind}/") or ctype.startswith("application/octet-stream")):
        print(f"⚠️  {kind}素材 Content-Type 為 {ctype}，若生成失敗請改用自有公開網址。", file=sys.stderr)


# --------------------------------------------------------------------------- #
# 送出 / 輪詢 / 下載
# --------------------------------------------------------------------------- #
def submit_request(api_key, payload, timeout=1800):
    # GMI 的 POST 可能阻塞較久才回應，timeout 須放寬（與 --timeout 一致）。
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


def _download(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=600) as r, open(dest, "wb") as fh:
        shutil.copyfileobj(r, fh)


def download_outputs(resp, out_dir):
    """下載 outcome.video_url 為 {rid}.mp4，縮圖為 {rid}_thumb.jpg；回傳已存影片路徑清單。"""
    outcome = resp.get("outcome") or {}
    rid = resp.get("request_id", "output")
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    saved = []

    video_urls = []
    if outcome.get("video_url"):
        video_urls.append(outcome["video_url"])
    # 防禦：部分佇列模型以 media_urls 回傳，留作備援
    for item in outcome.get("media_urls") or []:
        if item.get("url"):
            video_urls.append(item["url"])
    if not video_urls:
        raise SystemExit(f"[錯誤] 成功但無 video_url：{json.dumps(resp, ensure_ascii=False)}")

    for i, url in enumerate(video_urls):
        suffix = "" if i == 0 else f"_{i}"
        dest = out_dir / f"{rid}{suffix}.mp4"
        try:
            _download(url, dest)
        except (urllib.error.URLError, OSError) as e:
            print(f"⚠️  下載失敗 {url}：{e}", file=sys.stderr)
            continue
        print(f"🎬 已存檔：{dest}")
        saved.append(dest)

    thumb = outcome.get("thumbnail_image_url")
    if thumb:
        dest = out_dir / f"{rid}_thumb.jpg"
        try:
            _download(thumb, dest)
            print(f"🖼️  縮圖：{dest}")
        except (urllib.error.URLError, OSError) as e:
            print(f"⚠️  縮圖下載失敗：{e}", file=sys.stderr)
    return saved


# --------------------------------------------------------------------------- #
# 金鑰 / 參數
# --------------------------------------------------------------------------- #
def _read_key(path):
    try:
        return path.read_text(encoding="utf-8").strip() or None
    except FileNotFoundError:
        return None


def resolve_api_key(cli_key):
    """金鑰優先序：--api-key 旗標 > $GMI_API_KEY > 本 skill 的 .gmi_api_key > gemini-3-pro-image 的金鑰檔。"""
    return (cli_key or os.environ.get("GMI_API_KEY")
            or _read_key(KEY_FILE) or _read_key(SIBLING_KEY_FILE))


def build_parser():
    p = argparse.ArgumentParser(
        description="呼叫 GMI Cloud seedance-2-0-260128（Seedance 2.0）生成影片。",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--prompt", required=True, help="影片描述（動作、運鏡、氛圍）")
    # 參考素材（R2V）——使用者給圖且未指明首尾幀時的預設去處
    p.add_argument("--ref", dest="refs", action="append", default=[], metavar="URL",
                   help="參考圖『公開網址』→ reference_images（R2V），可重複指定")
    p.add_argument("--ref-file", dest="ref_files", action="append", default=[], metavar="PATH",
                   help="參考圖『本機路徑』→ 自動上傳後進 reference_images，可重複（裸檔名在 uploads/ 內尋找）")
    p.add_argument("--ref-video", dest="ref_videos", action="append", default=[], metavar="URL",
                   help="參考影片『公開網址』→ reference_videos，可重複")
    p.add_argument("--ref-video-file", dest="ref_video_files", action="append", default=[], metavar="PATH",
                   help="參考影片『本機路徑』，自動上傳，可重複")
    p.add_argument("--ref-audio", dest="ref_audios", action="append", default=[], metavar="URL",
                   help="參考音訊『公開網址』→ reference_audios，可重複")
    p.add_argument("--ref-audio-file", dest="ref_audio_files", action="append", default=[], metavar="PATH",
                   help="參考音訊『本機路徑』，自動上傳，可重複")
    p.add_argument("--ref-asset-id", dest="ref_asset_ids", action="append", default=[], metavar="ID",
                   help="GMI 資產 ID → reference_asset_ids，可重複")
    # 首尾幀（I2V）——僅在使用者明確要求首/尾幀錨定時使用
    p.add_argument("--first-frame", default=None, metavar="URL", help="首幀圖『公開網址』（I2V）")
    p.add_argument("--first-frame-file", default=None, metavar="PATH", help="首幀圖『本機路徑』，自動上傳")
    p.add_argument("--last-frame", default=None, metavar="URL", help="尾幀圖『公開網址』")
    p.add_argument("--last-frame-file", default=None, metavar="PATH", help="尾幀圖『本機路徑』，自動上傳")
    # 生成參數
    p.add_argument("--duration", type=int, default=5, help=f"影片秒數（{MIN_DURATION}～{MAX_DURATION}）")
    p.add_argument("--resolution", default="720p", choices=VALID_RESOLUTIONS, help="輸出解析度")
    p.add_argument("--ratio", default=None, choices=VALID_RATIOS,
                   help="長寬比；未指定時：有視覺參考素材→ adaptive（隨素材），純文生影→ 16:9")
    p.add_argument("--seed", type=int, default=None, help=f"隨機種子 0～{MAX_SEED}；多支時依序 +1 以產生變體")
    p.add_argument("--watermark", action="store_true", help="加浮水印（預設不加）")
    p.add_argument("--no-audio", action="store_true", help="不生成音訊（預設會生成）")
    p.add_argument("--web-search", action="store_true", help="允許模型在生成時聯網搜尋（預設關閉）")
    p.add_argument("--count", type=int, default=DEFAULT_COUNT,
                   help=f"生成支數，每支為一次獨立 API 請求並行送出（上限 {MAX_COUNT}）")
    p.add_argument("--out-dir", default=str(OUTPUTS_DIR), help="下載資料夾")
    p.add_argument("--api-key", default=None,
                   help="API 金鑰（預設序：此旗標 → $GMI_API_KEY → .gmi_api_key 檔 → gemini skill 金鑰檔）")
    p.add_argument("--poll-interval", type=float, default=10.0, help="輪詢間隔秒數")
    p.add_argument("--timeout", type=float, default=1800.0, help="最長等待秒數（影片生成需數分鐘）")
    p.add_argument("--dry-run", action="store_true", help="只列印將送出的 payload，不實際呼叫 API")
    return p


def main():
    args = build_parser().parse_args()

    api_key = resolve_api_key(args.api_key)
    if not api_key and not args.dry_run:
        raise SystemExit(f"[錯誤] 找不到 API 金鑰。請建立金鑰檔 {KEY_FILE}，或用 --api-key / $GMI_API_KEY。")
    if not MIN_DURATION <= args.duration <= MAX_DURATION:
        raise SystemExit(f"[錯誤] --duration 須在 {MIN_DURATION}～{MAX_DURATION} 秒之間（目前 {args.duration}）。")
    if not 1 <= args.count <= MAX_COUNT:
        raise SystemExit(f"[錯誤] --count 須在 1～{MAX_COUNT} 之間（目前 {args.count}）。")
    if args.seed is not None and not 0 <= args.seed <= MAX_SEED:
        raise SystemExit(f"[錯誤] --seed 須在 0～{MAX_SEED} 之間。")
    if args.first_frame and args.first_frame_file:
        raise SystemExit("[錯誤] --first-frame 與 --first-frame-file 只能擇一。")
    if args.last_frame and args.last_frame_file:
        raise SystemExit("[錯誤] --last-frame 與 --last-frame-file 只能擇一。")

    # 本機素材先上傳取得網址，再與直接給的公開網址合併
    ref_images = list(args.refs) + [upload_asset(f, "image") for f in args.ref_files]
    ref_videos = list(args.ref_videos) + [upload_asset(f, "video") for f in args.ref_video_files]
    ref_audios = list(args.ref_audios) + [upload_asset(f, "audio") for f in args.ref_audio_files]
    first_frame = args.first_frame or (upload_asset(args.first_frame_file, "image") if args.first_frame_file else None)
    last_frame = args.last_frame or (upload_asset(args.last_frame_file, "image") if args.last_frame_file else None)
    if len(ref_images) > MAX_REF_IMAGES:
        raise SystemExit(f"[錯誤] 參考圖最多 {MAX_REF_IMAGES} 張（目前 {len(ref_images)}）。")

    # 長寬比：未指定時，有視覺參考素材就 adaptive（隨素材），否則 16:9
    has_visual_ref = bool(ref_images or ref_videos or args.ref_asset_ids or first_frame or last_frame)
    ratio = args.ratio or ("adaptive" if has_visual_ref else "16:9")

    payload = {
        "prompt": args.prompt,
        "duration": args.duration,
        "resolution": args.resolution,
        "ratio": ratio,
        "watermark": args.watermark,
        "generate_audio": not args.no_audio,
    }
    if args.seed is not None:
        payload["seed"] = args.seed
    if args.web_search:
        payload["web_search"] = True
    if first_frame:
        payload["first_frame"] = first_frame
    if last_frame:
        payload["last_frame"] = last_frame
    if ref_images:
        payload["reference_images"] = ref_images
    if ref_videos:
        payload["reference_videos"] = ref_videos
    if ref_audios:
        payload["reference_audios"] = ref_audios
    if args.ref_asset_ids:
        payload["reference_asset_ids"] = args.ref_asset_ids

    print("📤 送出生成請求：")
    print(json.dumps({"model": MODEL, "payload": payload}, ensure_ascii=False, indent=2))
    if args.dry_run:
        print("🧪 dry-run：未呼叫 API。")
        return

    # 多支變體：固定 seed 會讓每支完全相同，故依序 +1；未給 seed 則交給伺服器隨機
    payloads = []
    for i in range(args.count):
        pl = dict(payload)
        if args.seed is not None and args.count > 1:
            pl["seed"] = args.seed + i
        payloads.append(pl)
    if args.count > 1:
        print(f"🔁 並行送出 {args.count} 次請求，產生 {args.count} 支變體…")

    # POST 可能阻塞到生成完成才回應，多支時須並行送出，總耗時才不會隨支數線性增加
    with ThreadPoolExecutor(max_workers=args.count) as pool:
        futures = [pool.submit(submit_request, api_key, pl, args.timeout) for pl in payloads]
        request_ids = [f.result() for f in futures]

    saved = []
    for request_id in request_ids:
        final = poll_request(api_key, request_id, args.poll_interval, args.timeout)
        saved += download_outputs(final, args.out_dir)
    print(f"\n🎉 完成，共產生 {len(saved)} 支影片於 {Path(args.out_dir).resolve()}")


if __name__ == "__main__":
    main()
