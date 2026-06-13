# GMI Cloud — `gemini-3-pro-image-preview` API 規格

> 供本 skill 的 `generate_image.py` 參照；除錯或擴充時閱讀。
> 文件來源：<https://docs.gmicloud.ai/model-quickstarts/image/gemini-3-pro-image-preview>

## 非同步佇列流程

1. `POST {API_BASE}` 送出 → 回傳 `request_id`、`status: queued`
2. `GET {API_BASE}/{request_id}` 輪詢 → 回傳 `status`，成功時含 `outcome.media_urls`
3. 從 `outcome.media_urls[].url` 下載圖片

```
API_BASE = https://console.gmicloud.ai/api/v1/ie/requestqueue/apikey/requests
```

## 驗證

HTTP header：`Authorization: Bearer <API_KEY>`

## 送出請求 body

```json
{
  "model": "gemini-3-pro-image-preview",
  "payload": { "...見下表..." }
}
```

`payload` 欄位：

| 欄位 | 型別 | 必填 | 預設 | 說明 / 可選值 |
|------|------|------|------|---------------|
| `prompt` | string | ✓ | — | 文字描述，≤ 2000 字元 |
| `image` | string / array | ✗ | — | 參考圖『公開 URL』，最多 14 張；PNG/JPEG/WebP/HEIC/HEIF，單張 ≤ 7MB。**不接受 base64 / 本機檔** |
| `image_size` | string | ✗ | `1K` | `1K` / `2K` / `4K` |
| `aspect_ratio` | string | ✗ | `1:1` | `1:1` / `4:5` / `5:4` / `3:4` / `4:3` / `9:16` / `16:9` / `21:9` |
| `image_output_format` | string | ✗ | `png` | `png` / `jpeg` |
| `contents` | array | ✗ | — | 多輪對話（Gemini 原生格式）；圖片需用 `fileData.fileUri` 指向 GCS/HTTP 網址 |

## 送出成功回應

```json
{ "request_id": "7eaa77fc-…", "model": "gemini-3-pro-image-preview", "status": "queued",
  "created_at": 1761763441, "updated_at": 1761763441, "queued_at": 1761763441 }
```

## 輪詢回應（成功）

```json
{
  "request_id": "7eaa77fc-…",
  "status": "success",
  "payload": { "prompt": "…", "image_size": "2K", "aspect_ratio": "4:5" },
  "outcome": {
    "media_urls": [ { "id": "0", "url": "https://storage.googleapis.com/gmi-generated-assets/…/gemini_output_0.jpg" } ]
  },
  "created_at": 1761763441, "updated_at": 1761763451
}
```

生成圖片以 **URL** 回傳（`outcome.media_urls[].url`），非 base64。

**狀態值：** `queued` → `processing` → `success` / `failed` / `cancelled`

## 限制與注意

- 參考圖**只接受公開 HTTP(S) 網址**——本 skill 以 tmpfiles.org 自動上傳本機圖（約 1 小時後自動刪除）。
- `prompt` ≤ 2000 字元；參考圖 ≤ 14 張、單張 ≤ 7MB。
- ⚠️ 此圖像端點預計於 **2026-07-17** 前棄用，屆時請改用替代端點。
