# gpt-image-2 — Usage examples

All commands assume CWD is project root:
`/Users/kouzuimac/Documents/反重力/0527課用教材/biz-ai-video-course`.

Script path is abbreviated below as `$S`:
`.claude/skills/gpt-image-2/scripts/gpt_image_2.py`.

Bare filenames resolve against the shared drop-zone `uploads/` (then
`uploads/done/`), so the examples below can name a file without a folder.

## Generate — defaults (no image ⇒ text-to-image, 1920x1088, n=2)

```bash
python3 $S --prompt "A photograph of a red fox in an autumn forest"
```

Runs `gpt-image-2-generate` and writes two PNGs:
`outputs/gpt_{timestamp}_1.png` and `_2.png`.

## Edit — one source image (image present ⇒ edit mode)

```bash
python3 $S \
  --prompt "Replace the background with a snowy mountain scene" \
  foo.png
```

Runs `gpt-image-2-edit`; writes `outputs/gpt_{timestamp}_foo_1.png` and `_2.png`,
then moves `uploads/foo.png` to `uploads/done/foo.png`.

## Edit — everything pending in the drop-zone

```bash
python3 $S --prompt "Turn the lighting into warm golden hour" uploads
```

A directory ref expands to the supported images directly inside it, so this
edits every image still waiting in `uploads/` (archived ones in `done/` are not
picked up) and archives each as it succeeds.

## Edit — many images (one request each, batch)

```bash
python3 $S \
  --prompt "Turn the lighting into warm golden hour" \
  a.png b.png --image https://example.com/c.jpg
```

URLs are passed straight through; local files are base64-encoded. Only the local
ones get archived — a URL has nothing to move.

## Edit — inpainting with a mask

```bash
python3 $S \
  --prompt "Paint a rainbow in the sky" \
  --mask masks/sky_mask.png \
  scene.png
```

## Edit — several prompts on the same image

```bash
python3 $S --keep-refs --prompt "make it dusk" scene.png
python3 $S --keep-refs --prompt "make it dawn" scene.png
python3 $S --prompt "make it midnight" scene.png   # last run archives it
```

## Long prompt from a file

For any prompt longer than a couple of lines, save it and pass `@path`
(relative paths resolve from project root):

```bash
python3 $S --prompt @prompts/scene.txt
```

## Overrides — quality / format / size / count

```bash
python3 $S --prompt "..." \
  --quality high --output-format jpeg --size 1024x1536 --n 1
```

Sizes are flexible: any `WxH` with edges multiple of 16, longest edge
≤ 3840, aspect ≤ 3:1, 0.65M–8.3M pixels (e.g. `1024x1024`, `1792x1024`,
`1920x1088`, `3840x2160`, `auto`). Exact `1920x1080` is invalid (1080 not
÷16) — use `1920x1088`.

## Fallback — edit rejected with raw base64

If an edit request comes back with an image-decode / validation error,
retry sending the image as a `data:` URL:

```bash
python3 $S --prompt "..." --data-url foo.png
```

## Typical stdout

```
[mode] generate (gpt-image-2-generate) size=1920x1088 quality=medium n=2
[submit] request_id=cd5b59d5-1b3f-4fd5-9899-15ecea1f28ba status=queued
[poll] status=processing
[poll] status=success
[✓] /…/outputs/gpt_20260614_103012_1.png (1843921 bytes)
[✓] /…/outputs/gpt_20260614_103012_2.png (1799233 bytes)
[done] saved 2 image(s) to /…/outputs
```

An edit run adds an archive line before `[done]`:

```
📦 參考素材歸檔：foo.png → uploads/done/foo.png
```

Parse `[✓]` lines if downstream automation needs the output paths.
