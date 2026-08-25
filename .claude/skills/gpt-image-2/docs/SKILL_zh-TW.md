---
name: gpt-image-2
description: >
  透過 GMI Cloud 的非同步 request-queue API（console.gmicloud.ai）
  使用 OpenAI 的 gpt-image-2 生成或編輯圖片。單一腳本、雙模式：
  沒有輸入圖片就跑 `gpt-image-2-generate`（文生圖）；有一張以上輸入
  圖片就跑 `gpt-image-2-edit`（每張圖一個請求）。送出工作後輪詢直到
  完成，再把每張結果圖下載到專案根目錄的共用 `outputs/` 資料夾。
  預設：quality=medium、output_format=png、size=1920x1088、n=2。
  API 金鑰從 skill 資料夾內的 `.gmi_api_key` 檔讀取（也接受 `--api-key`
  或 `$GMI_API_KEY`）。
  觸發條件：使用者想用 gpt-image-2／「gpt image 2」／GMI／GMI Cloud
  生成 / 建立 / 編輯 / 重繪圖片，或使用中文片語「gpt-image-2」
  「gpt image 2」「用 gpt-image-2 生圖」「用 gpt-image-2 改圖」
  「GMI 生圖」「GMI Cloud 生圖」「跑 gpt-image-2」「gpt image 2 編輯」
  「gpt image 2 生成」時。
  不要觸發在：Stable Diffusion／TensorArt 生圖（請用 `sd-image-gen`）、
  Gemini／nano banana 編輯（請用 `nano-banana-pro-edit`）、
  放大（請用 `sd-upscaler`）、或圖片挑選／評分（請用 `image-judge`）。
---

# gpt-image-2

執行 `scripts/gpt_image_2.py` 呼叫 GMI Cloud 的 gpt-image-2 模型。
此腳本**雙模式、會自動判斷**：

- **沒有輸入圖片 → 生成**（`gpt-image-2-generate`，文生圖）。
- **有一張以上輸入圖片 → 編輯**（`gpt-image-2-edit`，每張圖一個請求）。

每張結果圖都會存到**專案根目錄的共用 `outputs/`**，檔名前綴 `gpt_`；編輯來源圖則放在旁邊的共用 `uploads/`。這兩個資料夾由 `.claude/lib/media_paths.py` 統一定義，與 `gemini-3-pro-image`、`seedance-2-0` 兩個 skill 共用：

```
<專案根>/uploads/        把要編輯的來源圖丟這裡
<專案根>/uploads/done/   生成成功後來源圖自動搬進來
<專案根>/outputs/        所有結果（gpt_ / gemini_ / seedance_ 前綴分辨）
```

## 核心準則 (Core directives)

1. **絕不硬寫 API 金鑰。** 金鑰解析優先序：`--api-key` 旗標 →
   `$GMI_API_KEY`（含專案 `.env`）→ skill 資料夾內的 `.gmi_api_key` 檔
   （複製過來的金鑰就放這裡）。都找不到會以明確訊息結束。此 GMI 金鑰
   與 `gemini-3-pro-image` skill 共用同一把。
2. **從專案根目錄執行** — CWD 為
   `/Users/kouzuimac/Documents/反重力/0527課用教材/biz-ai-video-course`。
   （共用資料夾是從腳本自身位置推算的，換別的目錄執行也能跑；用專案根
   目錄只是讓下面的相對路徑好讀。）
3. **主動向使用者索取提示詞。** 沒有預設提示詞。若使用者未提供，
   執行前先問。
4. **模式由「有沒有給圖」決定。** 以位置參數（或 `--image`）傳入圖片
   路徑／URL → 編輯；都沒給 → 生成。可用 `--mode generate|edit` 強制。
5. **長提示詞改用 `@file.txt`。** 提示詞超過幾行時，存成專案根目錄底下
   的檔案並用 `--prompt @prompts/x.txt`，避免 shell 引號被踩雷。
6. **預設：quality=medium、png、size=1920x1088、n=2。** 僅在使用者要求
   時才用 `--quality / --output-format / --size / --n` 覆寫。
7. **尺寸很自由**（已實測）。gpt-image-2 接受任何 `WxH`：兩邊都是 16 的
   倍數、最長邊 ≤ 3840、長寬比 ≤ 3:1、總像素 0.65M–8.3M，所以最高可到
   4K（`3840x2160`）。預設 `1920x1088`（原生 16:9 HD）。**精確的
   `1920x1080` 會被拒絕**（1080 不是 16 的倍數）— 請用 `1920x1088`；
   也可用 `auto`。
8. **不要串到發文流程。** 回報存檔路徑即可，不要自動呼叫
   `multi-sns-post`。
9. **預設來源資料夾 — 共用 `uploads/`。** 編輯用的來源圖放在專案根目錄
   的共用上傳區。使用者說要改圖卻沒給完整路徑（或只是把圖丟進來）時，
   先去那裡找。腳本會自動把**裸檔名**與**資料夾路徑**解析到這個資料夾
   （也會找 CWD、專案根、`uploads/done/`），所以可以只傳
   `2026-06-10-23.png`，或直接指向整個 `uploads/` 資料夾一次改完裡面所有
   圖（資料夾只列最上層，已歸檔到 `done/` 的不會被重改）。輸出 `--size`
   請對齊來源圖長寬比（例如 9:16 直式 → `1088x1920`），才不會被拉伸或裁切。
10. **用過的來源圖會自動歸檔。** 編輯成功後，原本躺在 `uploads/` 的來源圖
   會被搬到 `uploads/done/`，上傳區永遠只留「還沒處理的」。失敗的那張會
   留在原位好重跑。使用者想對同一張圖試多組 prompt 時加 `--keep-refs`；
   不論有沒有加，重跑都還是可以用裸檔名指定。

## 知識樞紐 (Knowledge hub)

只讀跟當前任務相關的參考檔：

- 需要 CLI flags、模式、exit codes、GMI API 規格（endpoints、payload
  欄位、輪詢、回應格式）、輸出檔名規則 →
  [references/flags.md](../references/flags.md)
- 需要具體呼叫範例（生成、單／多張編輯、用檔案讀提示詞、URL 輸入、
  覆寫參數、stdout 樣貌） → [references/examples.md](../references/examples.md)

## 標準作業程序 (Standard operating procedure)

1. 向使用者取得提示詞（行內文字或 `@file`）。
2. 判斷模式：使用者有給圖嗎（完整路徑，或已經躺在共用 `uploads/` 裡的
   那張）？→ 編輯，否則 → 生成。沒給路徑的編輯需求，先看 `uploads/`。
3. 執行腳本（多種形式見 `references/examples.md`）：
   ```bash
   # 生成（沒給圖）
   python3 .claude/skills/gpt-image-2/scripts/gpt_image_2.py \
     --prompt "<text-or-@file>"

   # 編輯（一張以上的圖；裸檔名 → 共用 uploads/）
   python3 .claude/skills/gpt-image-2/scripts/gpt_image_2.py \
     --prompt "<text-or-@file>" source.png
   ```
4. 觀察 stdout：`[mode] ...`、`[submit] ...`、`[poll] status=...`、
   `[✓] ...`、`📦 ...`（來源圖已歸檔）、`[done] ...`。
5. 回報存到共用 `outputs/` 的路徑。

## 輸出協定 (Output protocol)

- 檔案存到專案根目錄的共用 `outputs/` 資料夾（自動建立）：
  - 生成：`gpt_{YYYYmmdd_HHMMSS}[_k].{png|jpg}`
  - 編輯：`gpt_{YYYYmmdd_HHMMSS}_{source_stem}[_k].{png|jpg}`
  - 只有在 `n > 1` 時才加上 `_k` 索引字尾。
  - `gpt_` 前綴就是用來跟同一個資料夾裡的 `gemini_` / `seedance_` 產出
    區分。既有檔案永遠不會被覆寫 —— 撞名會自動加 `_1`、`_2`… 字尾。
- Stdout 字首：`[mode] / [submit] / [poll] / [✓] / [batch] / [done]
  / [!]`。後續工具鏈要串接時，解析 `[✓]` 那幾行取路徑。
- 結束代碼：`0` 全部成功 · `1` 設定／驗證錯誤（金鑰錯、size/quality/
  format/n 不合法） · `2` 工作有跑但至少一張失敗。
