# gpt-image-2 — 使用範例

所有指令都假設 CWD 為專案根目錄：
`/Users/kouzuimac/Documents/反重力/0527課用教材/biz-ai-video-course`。

下面把腳本路徑簡寫成 `$S`：
`.claude/skills/gpt-image-2/scripts/gpt_image_2.py`。

裸檔名會自動解析到共用上傳區 `uploads/`（再找 `uploads/done/`），所以下面的
範例都可以只寫檔名、不用寫資料夾。

## 生成 — 預設（沒給圖 ⇒ 文生圖，1920x1088，n=2）

```bash
python3 $S --prompt "A photograph of a red fox in an autumn forest"
```

跑 `gpt-image-2-generate`，寫出兩張 PNG：
`outputs/gpt_{timestamp}_1.png` 與 `_2.png`。

## 編輯 — 單張來源圖（有給圖 ⇒ 編輯模式）

```bash
python3 $S \
  --prompt "Replace the background with a snowy mountain scene" \
  foo.png
```

跑 `gpt-image-2-edit`；寫出 `outputs/gpt_{timestamp}_foo_1.png` 與 `_2.png`，
然後把 `uploads/foo.png` 搬到 `uploads/done/foo.png`。

## 編輯 — 把上傳區還沒處理的全部改一輪

```bash
python3 $S --prompt "Turn the lighting into warm golden hour" uploads
```

資料夾路徑會展開成裡面最上層的支援圖檔，所以這行會改掉 `uploads/` 裡所有還
在等的圖（已歸檔到 `done/` 的不會被撈進來），每張成功一張就歸檔一張。

## 編輯 — 多張圖（每張一個請求，批次）

```bash
python3 $S \
  --prompt "Turn the lighting into warm golden hour" \
  a.png b.png --image https://example.com/c.jpg
```

URL 會直接原樣傳入；本機檔案會做 base64 編碼。只有本機檔會被歸檔 —— URL 本來
就沒有檔案可搬。

## 編輯 — 用遮罩做局部重繪 (inpainting)

```bash
python3 $S \
  --prompt "Paint a rainbow in the sky" \
  --mask masks/sky_mask.png \
  scene.png
```

## 編輯 — 同一張圖試多組提示詞

```bash
python3 $S --keep-refs --prompt "make it dusk" scene.png
python3 $S --keep-refs --prompt "make it dawn" scene.png
python3 $S --prompt "make it midnight" scene.png   # 最後這次才歸檔
```

## 用檔案讀長提示詞

提示詞超過幾行時，存成檔案並用 `@path`（相對路徑以專案根目錄為基準）：

```bash
python3 $S --prompt @prompts/scene.txt
```

## 覆寫參數 — quality / format / size / 張數

```bash
python3 $S --prompt "..." \
  --quality high --output-format jpeg --size 1024x1536 --n 1
```

尺寸很自由：任何 `WxH`，兩邊都是 16 的倍數、最長邊 ≤ 3840、長寬比 ≤ 3:1、
0.65M–8.3M 像素（例如 `1024x1024`、`1792x1024`、`1920x1088`、`3840x2160`、
`auto`）。精確的 `1920x1080` 不合法（1080 非 16 倍數）— 請用 `1920x1088`。

## 備援 — 編輯被原始 base64 拒絕時

若編輯請求回傳圖片解碼／驗證錯誤，改用 `data:` URL 重試：

```bash
python3 $S --prompt "..." --data-url foo.png
```

## 典型 stdout

```
[mode] generate (gpt-image-2-generate) size=1920x1088 quality=medium n=2
[submit] request_id=cd5b59d5-1b3f-4fd5-9899-15ecea1f28ba status=queued
[poll] status=processing
[poll] status=success
[✓] /…/outputs/gpt_20260614_103012_1.png (1843921 bytes)
[✓] /…/outputs/gpt_20260614_103012_2.png (1799233 bytes)
[done] saved 2 image(s) to /…/outputs
```

編輯模式會在 `[done]` 之前多一行歸檔訊息：

```
📦 參考素材歸檔：foo.png → uploads/done/foo.png
```

後續自動化若需要輸出路徑，解析 `[✓]` 那幾行。
