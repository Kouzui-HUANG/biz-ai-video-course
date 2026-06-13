# GMI Cloud — `seedance-2-0-260128` API 規格

> 供本 skill 的 `generate_video.py` 參照；除錯或擴充時閱讀。
> 文件來源：<https://docs.gmicloud.ai/model-quickstarts/video/seedance-2-0-260128>
> （console 入口：<https://console.gmicloud.ai/user-console/ie/model-hub/video/seedance-2-0-260128>）

## 非同步佇列流程

1. `POST {API_BASE}` 送出 → 回傳 `request_id`、`status: queued`
2. `GET {API_BASE}/{request_id}` 輪詢 → 回傳 `status`，成功時含 `outcome.video_url`
3. 從 `outcome.video_url` 下載影片、`outcome.thumbnail_image_url` 下載縮圖

```
API_BASE = https://console.gmicloud.ai/api/v1/ie/requestqueue/apikey/requests
```

## 驗證

HTTP header：`Authorization: Bearer <API_KEY>`（與 gemini-3-pro-image 共用同一把 GMI 平台金鑰）

## 送出請求 body

```json
{
  "model": "seedance-2-0-260128",
  "payload": { "...見下表..." }
}
```

`payload` 欄位：

| 欄位 | 型別 | 必填 | 預設 | 說明 / 可選值 |
|------|------|------|------|---------------|
| `prompt` | string | ✓ | — | 影片文字描述（動作、運鏡、氛圍）；官方未明定長度上限 |
| `duration` | integer | ✗ | `5` | 影片秒數，4～15 |
| `resolution` | string | ✗ | `720p` | `480p` / `720p` / `1080p` |
| `ratio` | string | ✗ | `16:9` | `16:9` / `4:3` / `1:1` / `3:4` / `9:16` / `21:9` / `adaptive`（隨參考素材） |
| `seed` | integer | ✗ | 隨機 | 0～4294967295 |
| `watermark` | boolean | ✗ | `false` | 是否加浮水印 |
| `generate_audio` | boolean | ✗ | `true` | 是否同步生成音訊 |
| `web_search` | boolean | ✗ | `false` | 生成時允許聯網搜尋 |
| `first_frame` | string(URL) | ✗ | — | 首幀圖『公開網址』（I2V 錨定，影片從此圖開始） |
| `last_frame` | string(URL) | ✗ | — | 尾幀圖『公開網址』（影片收在此圖） |
| `reference_images` | array(URL) | ✗ | `[]` | 參考圖網址陣列（R2V：主體 / 風格參考） |
| `reference_videos` | array(URL) | ✗ | `[]` | 參考影片網址陣列 |
| `reference_audios` | array(URL) | ✗ | `[]` | 參考音訊網址陣列 |
| `reference_asset_ids` | array(string) | ✗ | `[]` | GMI 平台資產 ID 陣列 |

所有素材欄位**只接受公開 HTTP(S) 網址**——不接受 base64 / 本機檔。

### 生成模式對照

| 模式 | 給的素材 | 用的欄位 |
|------|----------|----------|
| 文生影 T2V | 只有 prompt | `prompt` |
| 參考生影 R2V（**使用者給圖時的預設**） | prompt + 參考圖 | `reference_images`（可混搭 `reference_videos` / `reference_audios`） |
| 首尾幀圖生影 I2V | prompt + 首（尾）幀 | `first_frame` / `last_frame` |

## 官方 curl 範例

```bash
# 文生影
curl -X POST "https://console.gmicloud.ai/api/v1/ie/requestqueue/apikey/requests" \
  -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" \
  -d '{"model":"seedance-2-0-260128","payload":{
        "prompt":"A thunderstorm rolls over a medieval castle at night, lightning illuminating stone towers",
        "duration":12,"resolution":"1080p","ratio":"21:9","generate_audio":true}}'

# 首尾幀圖生影（I2V）
curl -X POST "https://console.gmicloud.ai/api/v1/ie/requestqueue/apikey/requests" \
  -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" \
  -d '{"model":"seedance-2-0-260128","payload":{
        "prompt":"The flower slowly blooms, petals unfurling in morning light",
        "first_frame":"https://example.com/bud.jpg","last_frame":"https://example.com/bloom.jpg",
        "duration":6,"resolution":"720p","ratio":"1:1","generate_audio":false}}'

# 參考素材（R2V）
curl -X POST "https://console.gmicloud.ai/api/v1/ie/requestqueue/apikey/requests" \
  -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" \
  -d '{"model":"seedance-2-0-260128","payload":{
        "prompt":"The character walks through a neon-lit alley",
        "reference_asset_ids":["asset-id-abc123"],
        "reference_images":["https://example.com/style-ref.jpg"],
        "duration":10,"resolution":"720p","ratio":"adaptive"}}'
```

## 送出成功回應

```json
{ "request_id": "c1c5a812-3c44-4c77-b02c-91c934abcd12", "model": "seedance-2-0-260128",
  "status": "queued", "created_at": 1750442925, "updated_at": 1750442925, "queued_at": 1750442925 }
```

## 輪詢回應（成功）

```json
{
  "request_id": "c1c5a812-3c44-4c77-b02c-91c934abcd12",
  "status": "success",
  "payload": { "prompt": "…", "duration": 8, "resolution": "720p", "ratio": "16:9",
               "seed": 42, "watermark": false, "generate_audio": true },
  "outcome": {
    "video_url": "https://storage.googleapis.com/bucket/generated-video.mp4",
    "thumbnail_image_url": "https://storage.googleapis.com/bucket/thumbnail.jpg"
  },
  "created_at": 1750442925, "updated_at": 1750442930
}
```

生成影片以 **URL** 回傳（`outcome.video_url` + `outcome.thumbnail_image_url`），非 base64。

**狀態值：** `queued` → `processing` → `success` / `failed` / `cancelled`

## 限制與注意

- 素材**只接受公開 HTTP(S) 網址**——本 skill 以 tmpfiles.org 自動上傳本機檔（約 1 小時後自動刪除）。
- 官方未明定 prompt 長度、素材張數 / 大小上限；本 skill 腳本側護欄：參考圖 ≤ 9 張、單張 ≤ 10MB，影片 ≤ 50MB，音訊 ≤ 20MB（tmpfiles 單檔上限 100MB）。
- 影片生成耗時數分鐘，輪詢請用較長 timeout（腳本預設 1800s、間隔 10s）。
- 計費依生成秒數；`--count` 預設 2、上限 4，避免誤耗額度。
- 同 payload + 固定 `seed` 會生成相同結果——腳本在多支變體時自動將 seed 依序 +1。
- 姊妹模型 `seedance-2-0-fast-260128`（Fast 版）端點與欄位相同，僅 `model` 字串不同；本 skill 不負責該模型。
