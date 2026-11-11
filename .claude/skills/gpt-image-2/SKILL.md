---
name: gpt-image-2
description: Actually generates or edits images with OpenAI gpt-image-2 through GMI Cloud, which spends API credits; results go to outputs/. Use only when the user names gpt-image-2 or GMI, e.g. 「用 gpt-image-2 生圖」「GMI 改圖」. Generic wording such as 編輯圖片, 改圖 or 生圖 is a prompt-writing request (→ prompt-master-image-editor or another prompt-master skill).
---

# gpt-image-2

Run `scripts/gpt_image_2.py` to call GMI Cloud's gpt-image-2 models. The
script is **dual-mode and auto-detecting**:

- **No input image → generate** (`gpt-image-2-generate`, text-to-image).
- **One or more input images → edit** (`gpt-image-2-edit`, one request
  per image).

Every result image is saved to the **shared** `outputs/` folder at the project
root, prefixed `gpt_`. The drop-zone for edit sources is the shared `uploads/`
folder next to it. Both are defined once in `.claude/lib/media_paths.py` and
shared with the `gemini-3-pro-image` and `seedance-2-0` skills:

```
<project root>/uploads/        drop edit-source images here
<project root>/uploads/done/   sources move here after a successful run
<project root>/outputs/        every result lands here (gpt_ / gemini_ / seedance_)
```

## Core directives

1. **Never hard-code the API key.** It is resolved in this order:
   `--api-key` flag → `$GMI_API_KEY` (incl. project `.env`) →
   `.gmi_api_key` file in the skill folder (this is where the copied key
   lives). If none is found the script exits with a clear message. The
   same GMI key powers the `gemini-3-pro-image` skill.
2. **Run from project root** — CWD is
   `/Users/kouzuimac/Documents/反重力/0527課用教材/biz-ai-video-course`. (The
   shared folders resolve from the script's own location, so another CWD still
   works; project root just keeps the relative paths below readable.)
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
9. **Default source folder — the shared `uploads/`.** Edit-source images live in
   the project-root drop-zone `uploads/`, shared with the other two generation
   skills. When the user wants to edit an image but doesn't give a full path (or
   just pastes/drops one), look there first. The script resolves bare filenames
   **and** a directory path against this folder automatically (also CWD, project
   root, and `uploads/done/`), so you can pass just `2026-06-10-23.png`, or point
   at the whole `uploads/` directory to edit every image inside it in one run
   (a directory ref lists only its top level, so already-archived images in
   `done/` are not re-edited). Match the output `--size` to the source aspect
   ratio (e.g. a 9:16 portrait → `1088x1920`) so the edit isn't stretched or
   cropped.
10. **Used sources self-archive.** After a successful edit, sources that were
   sitting in `uploads/` are moved to `uploads/done/`, so the drop-zone only
   ever shows what still needs doing. A failed edit leaves its source in place
   for a retry. Pass `--keep-refs` when the user wants several prompts on the
   same image; a re-run still accepts the bare filename either way.

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
   shared `uploads/` drop-zone? → edit, else generate. For edits without an
   explicit path, check `uploads/` first.
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
   `[✓] ...`, `📦 ...` (source archived), `[done] ...`.
5. Report saved `outputs/` paths to the user.

## Output protocol

- Files land in the shared project-root `outputs/` folder (auto-created):
  - generate: `gpt_{YYYYmmdd_HHMMSS}[_k].{png|jpg}`
  - edit: `gpt_{YYYYmmdd_HHMMSS}_{source_stem}[_k].{png|jpg}`
  - `_k` index suffix is added only when `n > 1`.
  - The `gpt_` prefix is what tells these apart from `gemini_` / `seedance_`
    results in the same folder. An existing file is never overwritten — a
    colliding name gets a `_1`, `_2`… suffix.
- Stdout prefixes: `[mode] / [submit] / [poll] / [✓] / [batch] / [done]
  / [!]`. Parse `[✓]` lines for paths when chaining into other tooling.
- Exit codes: `0` all good · `1` config/validation error (bad key,
  invalid size/quality/format/n) · `2` job ran but ≥1 image failed.
