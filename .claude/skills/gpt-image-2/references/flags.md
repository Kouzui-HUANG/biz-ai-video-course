# gpt-image-2 — CLI flags & API contract

Script: `.claude/skills/gpt-image-2/scripts/gpt_image_2.py`

## CLI flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `-p` / `--prompt <text\|@file>` | yes | — | Prompt text, or `@/path/to/file` to read from a UTF-8 file. Relative `@paths` resolve from project root. |
| positional `<image>…` | no | — | Input image path(s) or URL(s). **Any present ⇒ edit mode** (one request per image). None ⇒ generate mode. |
| `--image <path\|url>` | no | — | Extra input image for edit mode. Repeatable; merged with positionals. |
| `-m` / `--mode <auto\|generate\|edit>` | no | `auto` | `auto` = edit if any image given, else generate. `generate` ignores images; `edit` requires ≥1 image. |
| `--mask <path\|url>` | no | — | Inpainting mask (same size as image), edit mode only. |
| `-s` / `--size <WxH>` | no | `1920x1088` | Any `WxH`: edges ×16, max edge 3840, aspect ≤3:1, 0.65M–8.3M px (up to 4K). **Exact `1920x1080` invalid (not ×16) → use `1920x1088`.** `auto` ok. |
| `-q` / `--quality <level>` | no | `medium` | One of `low`, `medium`, `high`, `auto`. |
| `-f` / `--output-format <fmt>` | no | `png` | One of `png`, `jpeg`. |
| `-n` / `--n <int>` | no | `2` | Images per request, 1–10. |
| `--data-url` | no | off | Send local edit images as `data:` URLs instead of raw base64 (fallback if edit is rejected). |
| `--api-key <key>` | no | — | GMI key override. Priority: this flag → `$GMI_API_KEY` → `.gmi_api_key` file. |

## Exit codes

- `0` — completed; all requested images saved.
- `1` — config / validation error (missing `GMI_API_KEY`, invalid
  `--size` / `--quality` / `--output-format` / `--n`, `--mode edit`
  with no image, empty prompt, missing input file).
- `2` — job(s) ran but one or more images failed; see `[!]` lines on stderr.

## Output naming (`outputs/`)

- generate: `gptgen_{YYYYmmdd_HHMMSS}[_k]{.png|.jpg}`
- edit: `{source_stem}_gptedit[_k]{.png|.jpg}` (overwritten on re-run)
- `_k` (1-based) is appended only when `n > 1`. Extension follows
  `--output-format` (`png → .png`, `jpeg → .jpg`).

## GMI Cloud API contract

Async request-queue, OpenAI-style payloads.

- **Size:** not the 3 sizes GMI's table lists — verified live, the API
  accepts any `WxH` with edges ×16, max edge 3840, aspect ≤3:1, total
  pixels 0.65M–8.3M (so `1792x1024`, `1920x1088`, `3840x2160` all work;
  exact `1920x1080` errors because 1080 isn't ÷16).
- **Auth:** `Authorization: Bearer <key>`. The key is resolved as
  `--api-key` → `$GMI_API_KEY` (incl. project `.env`) → `.gmi_api_key`
  file in the skill folder. Endpoint base overridable via `GMI_ENDPOINT`
  (default `https://console.gmicloud.ai`).
- **Submit:** `POST /api/v1/ie/requestqueue/apikey/requests`
  ```json
  { "model": "gpt-image-2-generate",
    "payload": { "prompt": "...", "size": "1920x1088",
                 "quality": "medium", "output_format": "png", "n": 2 } }
  ```
  Edit uses `"model": "gpt-image-2-edit"` and adds `"image"` (base64
  string or public URL) plus optional `"mask"`. **One image per edit
  request** — the script loops over multiple inputs.
- **Poll:** `GET /api/v1/ie/requestqueue/apikey/requests/{request_id}`
  every 2 s, up to 300 s. Treats a non-empty `outcome.media_urls` (or
  status `success`/`finished`/`completed`) as done; `failed`/`error`/
  `cancelled` as failure.
- **Response:**
  ```json
  { "request_id": "…", "model": "…", "status": "success",
    "outcome": { "media_urls": [ { "id": "0", "url": "https://…" } ],
                 "thumbnail_image_url": "https://…" } }
  ```
  Images are public URLs; the script GETs each and writes the bytes.

## Model / deps

- Models: `gpt-image-2-generate`, `gpt-image-2-edit` (GMI Cloud).
- Deps: `requests`, `python-dotenv` (already installed in this project).
- Key: `--api-key` → `$GMI_API_KEY` → `.gmi_api_key` file in the skill folder.
