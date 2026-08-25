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
| `--keep-refs` | 否 | 關閉 | 生成成功後**不要**把用過的來源圖從 `uploads/` 搬進 `uploads/done/`。同一張圖要試多組 prompt 時用。 |
| `--api-key <key>` | 否 | — | GMI 金鑰覆寫。優先序：此旗標 → `$GMI_API_KEY` → `.gmi_api_key` 檔。 |

## 共用素材資料夾

由 `.claude/lib/media_paths.py` 統一定義，與 `gemini-3-pro-image`、
`seedance-2-0` 兩個 skill 共用（都已 gitignore）：

| 路徑 | 角色 |
|------|------|
| `<專案根>/uploads/` | 編輯來源圖的上傳區 |
| `<專案根>/uploads/done/` | 生成成功後來源圖搬到這裡 |
| `<專案根>/outputs/` | 所有產出，靠模型前綴分辨 |

- **輸入解析順序**（相對路徑）：CWD → 專案根 → `uploads/` → `uploads/done/`。
  所以裸檔名找得到上傳區，重跑時也找得到已歸檔的同一張圖。
- **資料夾路徑**會展開成裡面「最上層」的支援圖檔 —— 傳 `uploads` 就是把還
  沒處理的全部改一輪，不會去動 `done/` 裡已完成的。
- **歸檔**只在來源圖真的產出圖片後才做，而且只搬「直接躺在 `uploads/` 裡」
  的檔案 —— 從磁碟其他地方指過來的檔案一律不動。失敗的那張會留在原位好重跑。
- 需要換位置時，可用環境變數 `AI_MEDIA_ROOT`、`AI_UPLOADS_DIR`、
  `AI_OUTPUTS_DIR` 覆寫。

## 結束代碼 (Exit codes)

- `0` — 完成；所有要求的圖片都已存檔。
- `1` — 設定／驗證錯誤（缺 `GMI_API_KEY`、`--size`／`--quality`／
  `--output-format`／`--n` 不合法、`--mode edit` 卻沒給圖、提示詞為空、
  輸入檔不存在）。
- `2` — 工作有跑但至少一張失敗；看 stderr 的 `[!]` 行。

## 輸出檔名規則（共用 `outputs/`）

- 生成：`gpt_{YYYYmmdd_HHMMSS}[_k]{.png|.jpg}`
- 編輯：`gpt_{YYYYmmdd_HHMMSS}_{source_stem}[_k]{.png|.jpg}`
- 只有在 `n > 1` 時才加上 `_k`（從 1 起算）。副檔名跟著
  `--output-format`（`png → .png`、`jpeg → .jpg`）。
- `gpt_` 前綴用來跟同資料夾裡的 `gemini_` / `seedance_` 產出區分。既有檔案
  永遠不會被覆寫 —— 撞名會自動加 `_1`、`_2`… 字尾。

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
