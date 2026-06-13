---
name: gemini-3-pro-image
description: Executable tool skill that ACTUALLY CALLS the GMI Cloud `gemini-3-pro-image-preview` API to generate or edit real images — it runs a bundled Python script (submit → poll → download), it is NOT a prompt writer. Activation is by MODEL NAME ONLY. Trigger EXCLUSIVELY when the user explicitly names the model: "gemini 3 pro image", "gemini-3-pro-image", "gemini 3 pro image preview", "nanobanana pro", "nano banana pro", "奈米香蕉pro", or "奈米香蕉 pro". CRITICAL — DO NOT trigger on generic image-related wording: "圖片生成", "圖片編輯", "image generation", "image editing", "九宮格 / nine-panel", "動漫化 / anime", "character sheet / 三視圖", "product photo / 產品圖", "makeup / 彩妝", "storyboard / 分鏡", "reverse / 逆向", etc. — those describe IMAGE PROMPT tasks handled by the many other prompt-writing skills in this project and are UNRELATED to this skill. Also do NOT trigger on bare "nano banana" / "奈米香蕉" WITHOUT "pro" (that is a different model). Only the explicit model name above activates this skill; if the user merely describes a picture but never names this model, do NOT use this skill.
---

# Gemini 3 Pro Image / Nano Banana Pro — Live Image Generation & Editing

This is an **executable tool skill**, not a prompt generator. It runs a bundled Python program that calls the **real** GMI Cloud `gemini-3-pro-image-preview` API, then downloads the produced image(s). By default each run produces **two variants** (`--count 2`).

## ⚠️ Activation guard — model name ONLY

Use this skill **only** when the user explicitly names the model — `gemini 3 pro image` / `gemini-3-pro-image[-preview]` / `nanobanana pro` / `nano banana pro` / `奈米香蕉pro`.

This project contains MANY skills that *write image prompts*. Generic wording — 圖片生成 / 圖片編輯 / image generation / image editing / 九宮格 / 動漫化 / 三視圖 / 產品圖 / 彩妝 / 分鏡 / 逆向 — does **NOT** belong here; let the relevant prompt-writing skill handle those. If no explicit model name from the list appears, **do not activate**. Bare `nano banana` / `奈米香蕉` without `pro` is a different model — also do not activate.

## Files in this skill folder

| Path | Purpose | Git |
|------|---------|-----|
| `generate_image.py` | The program (stdlib only, Python 3.8+) | tracked |
| `references/gmi-api.md` | Full API spec — read when debugging | tracked |
| `.gmi_api_key` | API key (Bearer) | **gitignored** |
| `uploads/` | Drop local reference images here | **gitignored** |
| `outputs/` | Generated images land here | **gitignored** |

## Workflow

1. **Confirm activation** — a model name from the list is present. If not, stop.
2. **Identify the task:**
   - **Text-to-image** — only a prompt.
   - **Image editing / reference-guided** — a prompt + one or more reference images.
3. **Gather inputs:**
   - `prompt` (required, ≤ 2000 chars). If the user gives a rough idea, you may compose a strong English prompt for them.
   - Reference images (optional):
     - public URL → `--ref <url>` (repeatable)
     - **local file** → `--ref-file <path>` (repeatable). The script auto-uploads it to a temp host (tmpfiles.org, ~1 h auto-delete) and uses the resulting URL. Bare filenames are looked up in `uploads/`. Limits: ≤ 7 MB each, PNG/JPEG/WebP/HEIC/HEIF, ≤ 14 images total. (GMI accepts **public URLs only** — no base64/local upload to the API itself.)
4. **Parameters** — apply defaults; ask the user **only** for a genuinely undecided necessary value:
   - `--count` (default **2**) — unless the user explicitly asks for a specific number, keep the default: every run delivers TWO variants to choose from. Each image is a separate API request submitted in parallel (max 8).
   - `--image-size` `1K`/`2K`/`4K` (default **2K**)
   - `--aspect-ratio` (default **16:9**). For **editing**, match the source image's ratio (square source → `1:1`) to preserve framing.
   - `--output-format` `png`/`jpeg` (default **png**)
5. **Run** from this skill folder (the script resolves key/uploads/outputs relative to its own location):
   ```bash
   cd .claude/skills/gemini-3-pro-image
   # text-to-image
   python3 generate_image.py --prompt "a serene Japanese garden at dawn, soft mist"
   # image editing with a local reference (auto-uploaded)
   python3 generate_image.py --ref-file uploads/portrait.png --aspect-ratio 1:1 \
     --prompt "give her worried eyebrows while keeping the smile, same art style"
   # single image only (when the user explicitly asks for one)
   python3 generate_image.py --count 1 --prompt "..."
   ```
   For long/complex prompts, write the prompt to a temp file and pass `--prompt "$(cat /tmp/p.txt)"` to avoid shell-quoting issues.
6. **Show the results** — the script prints each saved path under `outputs/` (two by default); open each with the Read tool so the user sees the images.

## Notes

- **API key** precedence: `--api-key` > `$GMI_API_KEY` > `.gmi_api_key`. The key file is already present and gitignored.
- **Privacy** — `--ref-file` uploads to a public temp host (~1 h then auto-deleted). For sensitive images, ask the user for a private URL and use `--ref` instead.
- **Endpoint deprecation** — the GMI image endpoint is scheduled to retire before **2026-07-17**; migrate to its replacement before then.
- Full request/response schema, status values, and limits: **`references/gmi-api.md`**.
