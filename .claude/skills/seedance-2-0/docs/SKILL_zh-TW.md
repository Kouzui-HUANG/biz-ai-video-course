# Seedance 2.0 技能指南

這是一個**會實際呼叫 API 的工具型技能**，不是寫提示詞的技能。它會執行資料夾內的 Python 程式，呼叫 GMI Cloud 的 `seedance-2-0-260128` 真實 API 生成影片，並把影片與縮圖下載下來。沒有特別說明時，每次執行預設產生**兩支變體**（`--count 2`）、解析度 **720p**。

## 什麼時候會啟用？（只認模型名稱）

**只有**當你明確說出模型名稱時才會啟用：

- `seedance 2`、`seedance2`、`seedance 2.0`
- `seedance-2-0`、`seedance-2-0-260128`

**不會**被以下這類「泛泛跟影片有關」的字眼啟用——因為本專案另有「寫影片提示詞」的技能負責它們（prompt-master-text-to-video / prompt-master-image-to-video / prompt-master-video-continuity）：

> 影片生成、文生影、圖生影、動態生成、動態提示詞、video prompt、t2v、i2v…

只要你沒講出上面的模型名稱，這個技能就不會動。另外：

- 只說 `seedance`（沒有 2）→ 視為 Seedance 1.x 或提示詞目標模型，不觸發本技能。
- `seedance 2 fast` / `seedance 2.0 fast` 是另一個模型（`seedance-2-0-fast-260128`），也不會觸發本技能。

## 資料夾內容

| 路徑 | 用途 | Git |
|------|------|-----|
| `generate_video.py` | 主程式（純標準庫，Python 3.8+） | 追蹤 |
| `references/gmi-api.md` | 完整 API 規格 | 追蹤 |
| `.gmi_api_key` | API 金鑰（與 gemini-3-pro-image 同一把 GMI 金鑰） | **已 gitignore** |
| `uploads/` | 放本機參考圖 / 影片 / 音訊的上傳區 | **已 gitignore** |
| `outputs/` | 生成影片與縮圖下載區 | **已 gitignore** |

## 運作流程

1. 確認你有講模型名稱（否則不啟用）。
2. 依素材自動判斷模式：
   - **文生影 T2V**：只有提示詞。
   - **參考生影 R2V**：提示詞＋參考圖。**你有上傳圖、又沒特別指定時的預設模式**——圖會走 `reference_images`（主體 / 風格參考）。
   - **首尾幀圖生影 I2V**：只有你明確要求「首幀 / 尾幀 / 首尾幀」錨定（影片從那張圖開始、收在那張圖）時才用 `--first-frame(-file)` / `--last-frame(-file)`。
   - 也支援參考影片、參考音訊、GMI 資產 ID。
3. 收集輸入：
   - **提示詞**（必填，描述動作、運鏡、氛圍）。粗略想法 AI 可代為撰寫成英文提示詞。
   - **素材**（選用）：公開網址用 `--ref` 等旗標；本機檔用 `--ref-file` 等（程式會自動上傳到 tmpfiles.org 取得網址，約 1 小時自動刪除）。護欄：圖 ≤ 10MB、最多 9 張；影片 ≤ 50MB；音訊 ≤ 20MB。
4. 參數（有預設值，只有真的沒決定才問你）：
   - `--count`：生成支數（預設 **2** —— 沒特別說明就做兩支變體供挑選；每支是一次獨立 API 請求、並行送出，上限 4，影片較貴）
   - `--resolution`：`480p`/`720p`/`1080p`（預設 **720p**）
   - `--duration`：4～15 秒（預設 **5**）
   - `--ratio`：未指定時——有視覺參考素材 → **adaptive**（隨素材長寬比）；純文生影 → **16:9**。
   - 預設會生成音訊，`--no-audio` 可關閉；另有 `--seed`、`--watermark`、`--web-search`。
5. 執行範例（影片要算數分鐘，Bash timeout 請拉長到 10 分鐘以上）：
   ```bash
   cd .claude/skills/seedance-2-0
   # 文生影
   python3 generate_video.py --prompt "夜裡雷雨籠罩中世紀城堡，閃電照亮石塔（請用英文描述）"
   # 參考生影（本機圖自動上傳；上傳圖的預設模式）
   python3 generate_video.py --ref-file uploads/character.png \
     --prompt "The character walks through a neon-lit alley, cinematic tracking shot"
   # 首尾幀圖生影（明確要求時才用）
   python3 generate_video.py --first-frame-file uploads/bud.jpg --last-frame-file uploads/bloom.jpg \
     --prompt "The flower slowly blooms, petals unfurling in morning light"
   # 只要一支時
   python3 generate_video.py --count 1 --prompt "…"
   # 只看會送出什麼、不花額度
   python3 generate_video.py --dry-run --prompt "…"
   ```
6. 程式會印出存到 `outputs/` 的 `.mp4` 路徑與每支影片的 `_thumb.jpg` 縮圖；AI 會打開縮圖給你預覽，影片本體請在 Finder / QuickTime 開啟。

## 注意事項

- **金鑰順序**：`--api-key` > 環境變數 `GMI_API_KEY` > 本資料夾 `.gmi_api_key` > `../gemini-3-pro-image/.gmi_api_key`（整個 GMI 平台共用一把金鑰，金鑰檔已備妥且 gitignore）。
- **隱私**：本機檔旗標會把素材上傳到公開臨時檔案床（約 1 小時後自刪）。敏感素材請改用你自己的私有網址搭配 URL 旗標。
- **費用**：影片依生成秒數計費，`--count` / `--duration` 沒必要就不要加大。
- 完整 API 規格見 `references/gmi-api.md`。
