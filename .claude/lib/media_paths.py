#!/usr/bin/env python3
"""共用素材資料夾 —— 三個「會真的呼叫 API」的生成 skill 共用同一組上傳區與產出區。

    <專案根>/uploads/       參考素材上傳區（要用的圖 / 影片 / 音檔丟這裡）
    <專案根>/uploads/done/  已成功用過的參考素材（生成成功後自動搬入）
    <專案根>/outputs/       所有生成結果（檔名帶模型前綴，一眼看得出來源）

使用者：gemini-3-pro-image、gpt-image-2、seedance-2-0。
三者都以 _load_shared() 直接載入本檔（不動 sys.path），共用同一份路徑定義。

環境變數可覆寫（測試 / 換位置時用）：
    AI_MEDIA_ROOT    兩個資料夾都改放在此目錄底下
    AI_UPLOADS_DIR   直接指定上傳區路徑
    AI_OUTPUTS_DIR   直接指定產出區路徑
"""

from __future__ import annotations

import os
import shutil
import time
from pathlib import Path

__all__ = [
    "PROJECT_ROOT", "UPLOADS_DIR", "DONE_DIR", "OUTPUTS_DIR",
    "ensure_dirs", "stamp", "short_id", "resolve_upload", "unique_path", "archive_used",
]


def _project_root() -> Path:
    """本檔位於 <專案根>/.claude/lib/，往上找到含 .claude/ 的那層即專案根。"""
    here = Path(__file__).resolve()
    for d in here.parents:
        if (d / ".claude").is_dir():
            return d
    return here.parents[2]


def _dir_from_env(var: str, default: Path) -> Path:
    raw = os.environ.get(var)
    return Path(raw).expanduser().resolve() if raw else default


PROJECT_ROOT = _project_root()
_MEDIA_ROOT = _dir_from_env("AI_MEDIA_ROOT", PROJECT_ROOT)
UPLOADS_DIR = _dir_from_env("AI_UPLOADS_DIR", _MEDIA_ROOT / "uploads")
DONE_DIR = UPLOADS_DIR / "done"
OUTPUTS_DIR = _dir_from_env("AI_OUTPUTS_DIR", _MEDIA_ROOT / "outputs")


def ensure_dirs() -> None:
    """三個資料夾都建好（已存在就略過）。"""
    for d in (UPLOADS_DIR, DONE_DIR, OUTPUTS_DIR):
        d.mkdir(parents=True, exist_ok=True)


def stamp() -> str:
    """產出檔名用的時間戳：20260813_142530。"""
    return time.strftime("%Y%m%d_%H%M%S")


def short_id(value: str, length: int = 8) -> str:
    """request_id 取前 8 碼當追溯用短碼，檔名才不會長到難讀。"""
    return (str(value) or "output").replace("-", "")[:length] or "output"


def resolve_upload(ref) -> Path | None:
    """把使用者給的路徑 / 裸檔名解析成實際檔案。

    搜尋順序：絕對路徑 → 目前工作目錄 → 專案根 → uploads/ → uploads/done/。
    最後一站讓「同一張參考圖再跑一次」在檔案已被歸檔後仍然找得到。
    找不到回傳 None，錯誤訊息交給呼叫端決定。
    """
    p = Path(ref).expanduser()
    if p.is_absolute():
        return p if p.exists() else None
    for base in (Path.cwd(), PROJECT_ROOT, UPLOADS_DIR, DONE_DIR):
        cand = base / p
        if cand.exists():
            return cand
    return None


def unique_path(directory, name: str) -> Path:
    """回傳 directory/name；已存在就加 _1 / _2… 後綴，永不覆蓋既有檔案。"""
    directory = Path(directory)
    dest = directory / name
    if not dest.exists():
        return dest
    stem, suffix = dest.stem, dest.suffix
    for i in range(1, 1000):
        cand = directory / f"{stem}_{i}{suffix}"
        if not cand.exists():
            return cand
    raise RuntimeError(f"無法為 {name} 找到未使用的檔名（{directory}）")


def archive_used(refs, quiet: bool = False) -> list[Path]:
    """把「已成功用過」的參考素材從 uploads/ 移到 uploads/done/。

    只搬真的躺在 uploads/ 第一層的檔案 —— 使用者從別處指過來的檔案一律不動，
    避免動到不屬於上傳區的東西；已在 done/ 內的重跑素材同樣略過。
    回傳實際搬動後的新路徑清單。
    """
    moved: list[Path] = []
    for ref in refs:
        if not ref:
            continue
        p = ref if isinstance(ref, Path) else resolve_upload(ref)
        if p is None or not p.is_file():
            continue
        try:
            if p.resolve().parent != UPLOADS_DIR.resolve():
                continue
        except OSError:
            continue
        DONE_DIR.mkdir(parents=True, exist_ok=True)
        dest = unique_path(DONE_DIR, p.name)
        try:
            p.replace(dest)                    # 同磁碟改名即可
        except OSError:
            shutil.move(str(p), str(dest))     # 跨磁碟才需要真的搬
        moved.append(dest)
        if not quiet:
            print(f"📦 參考素材歸檔：{p.name} → uploads/done/{dest.name}")
    return moved
