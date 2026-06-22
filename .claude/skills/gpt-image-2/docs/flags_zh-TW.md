# gpt-image-2 — CLI 參數與 API 規格

腳本：`.claude/skills/gpt-image-2/scripts/gpt_image_2.py`

## CLI 參數

| 參數 | 必填 | 預設值 | 說明 |
|------|------|--------|------|
| `-p` / `--prompt <text\|@file>` | 是 | — | 提示詞文字，或用 `@/path/to/file` 從 UTF-8 檔案讀取。`@相對路徑` 以專案根目錄為基準。 |
| 位置參數 `<image>…` | 否 | — | 輸入圖片路徑或 URL。**只要有給就進入編輯模式**（每張圖一個請求）。都沒給就進入生成模式。 |
| `--image <path\|url>` | 否 | — | 編輯模式的額外輸入圖片。可重複；會與位置參數合併。 |
| `-m` / `--mode <auto\|generate\|edit>` | 否 | `auto` | `auto` = 有給圖就編輯，否則生成。`generate` 會忽略圖片；`edit` 需要至少一張圖。 |
| `--mask <path\|url>` | 否 | — | 局部重繪遮罩（尺寸需與圖片相同），僅編輯模式。 |
| `-s` / `--size <WxH>` | 否 | `1920x1088` | 任何 `WxH`：邊長 ×16、最長邊 3840、長寬比 ≤3:1、0.65M–8.3M 像素（最高 4K）。**精確 `1920x1080` 不合法（非 ×16）→ 用 `1920x1088`。** 可用 `auto`。 |
| `-q` / `--quality <level>` | 否 | `medium` | 只接受 `low`、`medium`、`high`、`auto`。 |
| `-f` / `--output-format <fmt>` | 否 | `png` | 只接受 `png`、`jpeg`。 |
| `-n` / `--n <int>` | 否 | `2` | 每個請求的張數，1–10。 |
| `--data-url` | 否 | 關閉 | 把本機編輯圖片改用 `data:` URL 送出，而非原始 base64（編輯被拒絕時的備援）。 |
| `--api-key <key>` | 否 | — | GMI 金鑰覆寫。優先序：此旗標 → `$GMI_API_KEY` → `.gmi_api_key` 檔。 |

## 結束代碼 (Exit codes)

- `0` — 完成；所有要求的圖片都已存檔。
- `1` — 設定／驗證錯誤（缺 `GMI_API_KEY`、`--size`／`--quality`／
  `--output-format`／`--n` 不合法、`--mode edit` 卻沒給圖、提示詞為空、
  輸入檔不存在）。
- `2` — 工作有跑但至少一張失敗；看 stderr 的 `[!]` 行。

## 輸出檔名規則（`outputs/`）

- 生成：`gptgen_{YYYYmmdd_HHMMSS}[_k]{.png|.jpg}`
- 編輯：`{source_stem}_gptedit[_k]{.png|.jpg}`（重跑會覆寫）
- 只有在 `n > 1` 時才加上 `_k`（從 1 起算）。副檔名跟著
  `--output-format`（`png → .png`、`jpeg → .jpg`）。

## GMI Cloud API 規格

非同步 request-queue，OpenAI 風格 payload。

- **尺寸：** 不是 GMI 表格列的那 3 種——已實測，API 接受任何 `WxH`：
  邊長 ×16、最長邊 3840、長寬比 ≤3:1、總像素 0.65M–8.3M（所以
  `1792x1024`、`1920x1088`、`3840x2160` 都行；精確 `1920x1080` 會報錯，
  因為 1080 非 16 倍數）。
- **驗證：** `Authorization: Bearer <key>`。金鑰解析優先序：`--api-key`
  → `$GMI_API_KEY`（含專案 `.env`）→ skill 資料夾內的 `.gmi_api_key` 檔。
  endpoint base 可用 `GMI_ENDPOINT` 覆寫（預設
  `https://console.gmicloud.ai`）。
- **送出：** `POST /api/v1/ie/requestqueue/apikey/requests`
  ```json
  { "model": "gpt-image-2-generate",
    "payload": { "prompt": "...", "size": "1920x1088",
                 "quality": "medium", "output_format": "png", "n": 2 } }
  ```
  編輯改用 `"model": "gpt-image-2-edit"`，並加上 `"image"`（base64
  字串或公開 URL）與選用的 `"mask"`。**每個編輯請求只吃一張圖** —
  腳本會對多張輸入逐一迴圈處理。
- **輪詢：** `GET /api/v1/ie/requestqueue/apikey/requests/{request_id}`
  每 2 秒一次，最多 300 秒。只要 `outcome.media_urls` 非空（或狀態
  為 `success`／`finished`／`completed`）即視為完成；`failed`／`error`／
  `cancelled` 視為失敗。
- **回應：**
  ```json
  { "request_id": "…", "model": "…", "status": "success",
    "outcome": { "media_urls": [ { "id": "0", "url": "https://…" } ],
                 "thumbnail_image_url": "https://…" } }
  ```
  圖片是公開 URL；腳本會逐一 GET 並寫出位元組。

## 模型 / 相依套件

- 模型：`gpt-image-2-generate`、`gpt-image-2-edit`（GMI Cloud）。
- 相依：`requests`、`python-dotenv`（本專案已安裝）。
- 金鑰：`--api-key` → `$GMI_API_KEY` → skill 資料夾內的 `.gmi_api_key` 檔。
