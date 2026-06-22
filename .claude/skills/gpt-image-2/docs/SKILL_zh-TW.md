---
name: gpt-image-2
description: >
  透過 GMI Cloud 的非同步 request-queue API（console.gmicloud.ai）
  使用 OpenAI 的 gpt-image-2 生成或編輯圖片。單一腳本、雙模式：
  沒有輸入圖片就跑 `gpt-image-2-generate`（文生圖）；有一張以上輸入
  圖片就跑 `gpt-image-2-edit`（每張圖一個請求）。送出工作後輪詢直到
  完成，再把每張結果圖下載到 skill 的 `outputs/` 資料夾。
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

每張結果圖都會存到 skill 的 `outputs/` 資料夾（`.claude/skills/gpt-image-2/outputs/`）。

## 核心準則 (Core directives)

1. **絕不硬寫 API 金鑰。** 金鑰解析優先序：`--api-key` 旗標 →
   `$GMI_API_KEY`（含專案 `.env`）→ skill 資料夾內的 `.gmi_api_key` 檔
   （複製過來的金鑰就放這裡）。都找不到會以明確訊息結束。此 GMI 金鑰
   與 `gemini-3-pro-image` skill 共用同一把。
2. **永遠從專案根目錄執行** — CWD 為
   `/Users/kouzuimac/Documents/反重力/0527課用教材/biz-ai-video-course`。
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

## 知識樞紐 (Knowledge hub)

只讀跟當前任務相關的參考檔：

- 需要 CLI flags、模式、exit codes、GMI API 規格（endpoints、payload
  欄位、輪詢、回應格式）、輸出檔名規則 →
  [references/flags.md](../references/flags.md)
- 需要具體呼叫範例（生成、單／多張編輯、用檔案讀提示詞、URL 輸入、
  覆寫參數、stdout 樣貌） → [references/examples.md](../references/examples.md)

## 標準作業程序 (Standard operating procedure)

1. 向使用者取得提示詞（行內文字或 `@file`）。
2. 判斷模式：使用者有給圖嗎？→ 編輯，否則 → 生成。
3. 執行腳本（多種形式見 `references/examples.md`）：
   ```bash
   # 生成（沒給圖）
   python3 .claude/skills/gpt-image-2/scripts/gpt_image_2.py \
     --prompt "<text-or-@file>"

   # 編輯（一張以上的圖）
   python3 .claude/skills/gpt-image-2/scripts/gpt_image_2.py \
     --prompt "<text-or-@file>" path/to/source.png
   ```
4. 觀察 stdout：`[mode] ...`、`[submit] ...`、`[poll] status=...`、
   `[✓] ...`、`[done] ...`。
5. 回報存到 `outputs/` 的路徑。

## 輸出協定 (Output protocol)

- 檔案存到 skill 的 `outputs/` 資料夾（自動建立）：
  - 生成：`gptgen_{YYYYmmdd_HHMMSS}[_k].{png|jpg}`
  - 編輯：`{source_stem}_gptedit[_k].{png|jpg}`（重跑會覆寫）
  - 只有在 `n > 1` 時才加上 `_k` 索引字尾。
- Stdout 字首：`[mode] / [submit] / [poll] / [✓] / [batch] / [done]
  / [!]`。後續工具鏈要串接時，解析 `[✓]` 那幾行取路徑。
- 結束代碼：`0` 全部成功 · `1` 設定／驗證錯誤（金鑰錯、size/quality/
  format/n 不合法） · `2` 工作有跑但至少一張失敗。
