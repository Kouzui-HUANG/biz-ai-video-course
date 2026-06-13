# Gemini 3 Pro Image（Nano Banana Pro）技能指南

這是一個**會實際呼叫 API 的工具型技能**，不是寫提示詞的技能。它會執行資料夾內的 Python 程式，呼叫 GMI Cloud 的 `gemini-3-pro-image-preview` 真實 API 生成 / 編輯圖片，並把結果下載下來。沒有特別說明時，每次執行預設產生**兩張變體**（`--count 2`）。

## 什麼時候會啟用？（只認模型名稱）

**只有**當你明確說出模型名稱時才會啟用：

- `gemini 3 pro image`、`gemini-3-pro-image`、`gemini 3 pro image preview`
- `nanobanana pro`、`nano banana pro`
- `奈米香蕉pro`、`奈米香蕉 pro`

**不會**被以下這類「泛泛跟圖片有關」的字眼啟用——因為本專案另有很多「寫圖片提示詞」的技能負責它們：

> 圖片生成、圖片編輯、九宮格、動漫化、三視圖、產品圖、彩妝、分鏡、逆向工程…

只要你沒講出上面的模型名稱，這個技能就不會動。另外，沒有 `pro` 的「nano banana / 奈米香蕉」是另一個模型，也不會觸發本技能。

## 資料夾內容

| 路徑 | 用途 | Git |
|------|------|-----|
| `generate_image.py` | 主程式（純標準庫，Python 3.8+） | 追蹤 |
| `references/gmi-api.md` | 完整 API 規格 | 追蹤 |
| `.gmi_api_key` | API 金鑰 | **已 gitignore** |
| `uploads/` | 放本機參考圖的上傳區 | **已 gitignore** |
| `outputs/` | 生成結果下載區 | **已 gitignore** |

## 運作流程

1. 確認你有講模型名稱（否則不啟用）。
2. 判斷是「文生圖」還是「圖生圖／編輯」。
3. 收集輸入：
   - **提示詞**（必填，≤ 2000 字元）。
   - **參考圖**（選用）：公開網址用 `--ref`；本機檔用 `--ref-file`（程式會自動上傳到 tmpfiles.org 取得網址，約 1 小時自動刪除）。單張 ≤ 7MB、最多 14 張。
4. 參數（有預設值，只有真的沒決定才問你）：
   - `--count`：生成張數（預設 **2** —— 沒特別說明就做兩張變體供挑選；每張是一次獨立 API 請求、並行送出，上限 8）
   - `--image-size`：`1K`/`2K`/`4K`（預設 **2K**）
   - `--aspect-ratio`：預設 **16:9**；做**編輯**時建議改成與來源圖一致（方形→ `1:1`）以保留構圖。
   - `--output-format`：`png`/`jpeg`（預設 **png**）
5. 執行範例：
   ```bash
   cd .claude/skills/gemini-3-pro-image
   # 文生圖
   python3 generate_image.py --prompt "黎明時分的日式庭園，薄霧瀰漫"
   # 圖生圖（本機圖自動上傳）
   python3 generate_image.py --ref-file uploads/portrait.png --aspect-ratio 1:1 \
     --prompt "把眉毛改成擔憂眉，保留原本的微笑與畫風"
   # 只要一張時
   python3 generate_image.py --count 1 --prompt "…"
   ```
6. 程式會印出存到 `outputs/` 的路徑（預設兩張），AI 會逐張打開圖片給你看。

## 注意事項

- **金鑰順序**：`--api-key` > 環境變數 `GMI_API_KEY` > `.gmi_api_key` 檔（金鑰檔已備妥且 gitignore）。
- **隱私**：`--ref-file` 會把圖上傳到公開臨時圖床（約 1 小時後自刪）。敏感圖片請改用你自己的私有網址搭配 `--ref`。
- **端點棄用**：GMI 此圖像端點預計於 **2026-07-17** 前退役，屆時需改用替代端點。
