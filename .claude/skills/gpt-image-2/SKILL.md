---
name: gpt-image-2
description: >
  Generate or edit images with OpenAI's gpt-image-2 via GMI Cloud's
  async request-queue API (console.gmicloud.ai). One dual-mode script:
  with NO input image it runs `gpt-image-2-generate` (text-to-image);
  with one or more input images it runs `gpt-image-2-edit` (one request
  per image). Submits the job, polls until done, and downloads every
  result image to the skill's `outputs/` folder. Defaults:
  quality=medium, output_format=png, size=1920x1088, n=2. API key is read
  from a `.gmi_api_key` file in the skill folder (also accepts `--api-key`
  or `$GMI_API_KEY`).
  ACTIVATION IS BY EXPLICIT MODEL NAME ONLY. This skill ACTUALLY
  GENERATES / EDITS real images and spends API credits, so TRIGGER ONLY
  when the user explicitly names this model / provider — "gpt-image-2",
  "gpt image 2", "GMI", "GMI Cloud" — e.g. "用 gpt-image-2 生圖",
  "用 gpt-image-2 改圖", "GMI 生圖", "GMI Cloud 生圖", "跑 gpt-image-2",
  "gpt image 2 編輯", "gpt image 2 生成".
  DO NOT TRIGGER on generic image wording that does NOT name gpt-image-2 /
  GMI — e.g. "編輯圖片", "圖片編輯", "載入圖片編輯", "圖片編輯技能", "改圖",
  "修圖", "編輯這張圖", "轉為黑白線稿", "圖片生成", "生圖", "image editing",
  "edit image", "image generation". Those are PROMPT-WRITING requests, NOT
  generation:
    • editing an image / a hypothetical visual change → use
      `prompt-master-image-editor` (writes an English edit prompt only,
      never generates an actual image).
    • other prompt tasks → the relevant `prompt-master-*` skill.
  Also DO NOT TRIGGER for: Stable Diffusion / TensorArt generation
  (use `sd-image-gen`), Gemini / nano banana editing
  (use `nano-banana-pro-edit`), upscaling (use `sd-upscaler`), or image
  selection / judging (use `image-judge`).
---

# gpt-image-2

Run `scripts/gpt_image_2.py` to call GMI Cloud's gpt-image-2 models. The
script is **dual-mode and auto-detecting**:

- **No input image → generate** (`gpt-image-2-generate`, text-to-image).
- **One or more input images → edit** (`gpt-image-2-edit`, one request
  per image).

Every result image is saved to the skill's `outputs/` folder
(`.claude/skills/gpt-image-2/outputs/`).

## Core directives

1. **Never hard-code the API key.** It is resolved in this order:
   `--api-key` flag → `$GMI_API_KEY` (incl. project `.env`) →
   `.gmi_api_key` file in the skill folder (this is where the copied key
   lives). If none is found the script exits with a clear message. The
   same GMI key powers the `gemini-3-pro-image` skill.
2. **Always run from project root** — CWD is
   `/Users/kouzuimac/Documents/反重力/0527課用教材/biz-ai-video-course`.
3. **Ask for the prompt.** No default prompt. If the user doesn't supply
   one, ask before running.
4. **Mode is decided by whether an image is supplied.** Pass image
   path(s)/URL(s) as positional args (or `--image`) → edit. Pass none →
   generate. `--mode generate|edit` forces it.
5. **Long prompts → `@file.txt`.** For prompts longer than a couple of
   lines, save to a file under project root and pass
   `--prompt @prompts/x.txt`. Avoids shell-quoting traps.
6. **Defaults: quality=medium, png, size=1920x1088, n=2.** Override via
   `--quality / --output-format / --size / --n` only when asked.
7. **Size is flexible** (verified live). gpt-image-2 accepts any `WxH`
   with edges multiple of 16, longest edge ≤ 3840, aspect ≤ 3:1, total
   pixels 0.65M–8.3M — so up to 4K (`3840x2160`). Default `1920x1088`
   (native 16:9 HD). **Exact `1920x1080` is rejected** (1080 isn't ÷16) —
   use `1920x1088`. `auto` also works.
8. **Don't chain into posting.** Report saved paths; do not auto-invoke
   `multi-sns-post`.
9. **Default source folder — `uploads/`.** Edit-source images live in the
   skill's drop-zone: `.claude/skills/gpt-image-2/uploads/`. When the user wants
   to edit an image but doesn't give a full path (or just pastes/drops one),
   look there first. The script resolves bare filenames **and** a directory path
   against this folder automatically (also CWD and project root), so you can
   pass just `2026-06-10-23.png`, or point at the whole `uploads/` directory to
   edit every image inside it in one run. Match the output `--size` to the
   source aspect ratio (e.g. a 9:16 portrait → `1088x1920`) so the edit isn't
   stretched or cropped.

## Knowledge hub

Read only the reference file relevant to the task:

- Need CLI flags, modes, exit codes, the GMI API contract (endpoints,
  payload fields, polling, response shape), output naming →
  [references/flags.md](references/flags.md)
- Need concrete invocation examples (generate, edit single/many,
  file-based prompt, URL input, overrides, stdout shape) →
  [references/examples.md](references/examples.md)

## Standard operating procedure

1. Get the prompt from the user (inline or `@file`).
2. Decide mode: did the user provide an image — a path, or one sitting in the
   `uploads/` drop-zone? → edit, else generate. For edits without an explicit
   path, check `uploads/` first.
3. Run the script (see `references/examples.md` for forms):
   ```bash
   # generate (no image)
   python3 .claude/skills/gpt-image-2/scripts/gpt_image_2.py \
     --prompt "<text-or-@file>"

   # edit (one or more images)
   python3 .claude/skills/gpt-image-2/scripts/gpt_image_2.py \
     --prompt "<text-or-@file>" path/to/source.png
   ```
4. Watch stdout: `[mode] ...`, `[submit] ...`, `[poll] status=...`,
   `[✓] ...`, `[done] ...`.
5. Report saved `outputs/` paths to the user.

## Output protocol

- Files land in the skill's `outputs/` folder (auto-created):
  - generate: `gptgen_{YYYYmmdd_HHMMSS}[_k].{png|jpg}`
  - edit: `{source_stem}_gptedit[_k].{png|jpg}` (overwritten on re-run)
  - `_k` index suffix is added only when `n > 1`.
- Stdout prefixes: `[mode] / [submit] / [poll] / [✓] / [batch] / [done]
  / [!]`. Parse `[✓]` lines for paths when chaining into other tooling.
- Exit codes: `0` all good · `1` config/validation error (bad key,
  invalid size/quality/format/n) · `2` job ran but ≥1 image failed.
