---
name: prompt-master-toon-render
description: Writes one English image-editing prompt that renders a storyboard sketch or grey clay (白模) layout into a finished stylized 3D frame, keeping its composition and taking designs from references. Use when the user mentions 「三渲二」「白模渲染」「草圖渲染」「分鏡轉3D」「卡通渲染」, toon shading, cel-shaded 3D or clay render. Not for PBR hybrid realism (→ prompt-master-hybrid-realism) or ordinary edits (→ prompt-master-image-editor).
---

# Toon Render Prompt Director

Turns a layout image (a hand-drawn storyboard panel or an untextured grey clay render, 白模) plus character, prop and style references into one dense English image-editing prompt for a finished stylized 3D (三渲二) frame.

> Output is prompt text only. Never generate or edit the image, run a script, or hand off to an image-generation skill (gpt-image-2, gemini-3-pro-image, nano banana, seedance…). The user runs the generation.

## Hard rules

1. **The layout image decides composition; the references decide design.** Keep the layout's framing and crop, camera height and angle, each character's position, pose and facial expression, every vehicle and prop, and every terrain silhouette. Never delete or move a structure because it seems to clash with a reference: read the perspective first and work out what the block actually is. Take faces, hair, clothing, colors and accessories from the references, and say in the prompt that the references are "for design only, never for pose".
2. **Default look (no style reference given): soft stylized 3D, no outlines.** Soft diffused light that still gives every form gentle volume (smooth falloff, soft ambient occlusion, soft contact shadows), cool-tinted shadows, matte surfaces, and no sharp or glossy specular highlights, rim light, strong backlight, lens flare or reflections. Add outlines only when the user asks for 線條, 描邊 or line art; 三渲二 on its own does not mean outlines.
3. **A style reference outranks the default.** Put it last in the image order and write "use Image N only as the style reference for rendering, shading, foliage and sky treatment and color grading, never for its composition, characters, props or setting". Also describe its look in words (light quality, palette, foliage, sky, grade, vignette): the text carries weight the image alone does not.
4. **Never pull toward realism.** No photoreal, PBR, ray or path tracing, realistic-lighting or material-detail words (wet sheen, bark grain, rock texture, worn paint, leather, knit, ribbed). Render the background as simplified shapes with less detail than the characters: rounded cloud-like canopy clusters, smooth bands of earth, soft rounded logs. Rugged or disaster vocabulary (boulders, gravel, exposed roots, mountain mist, raw scars) drags the whole frame toward a photo, so translate it into smooth shapes.
5. **Describe only what is inside the frame.** If a character shows only above a rail or through a window, describe only those parts. Listing out-of-frame clothing (shorts, sandals, a skirt) pushes the model to zoom out.
6. **State accessories explicitly, per character and per shot.** For each character, name the accessories its reference shows and rule out the ones it doesn't ("bare wrists, no bracelet or watch"). Layout geometry is not design: a band-like shape at a clay wrist or a rough hair mass follows the reference, so write "ignore the band-like shape at her wrist in Image 1". Rebuild the negative prompt for every shot so a ban written for one character (bracelet) can't erase another character's accessory (a jade bangle).
7. **Text only where the user asks for it.** Put required lettering (a license plate) in quotes, exactly, with its position: `a small white license plate centered below the tailgate, with crisp black characters reading exactly "0326-BK", sharp, legible and undistorted`. Then write "apart from the "…" plate, no other text anywhere", never a blanket "no text" that contradicts it. Suppress small incidental lettering (door decals) and suggest inpainting it afterwards.
8. **Clean skin, stylized version.** Faces and hands get smooth, soft, continuous tonal gradation, clean and even, free of blotchiness, mottling, dirt or smudges, with no oily shine and no plastic airbrushed look; keep designed wrinkles on elderly characters. Ban banding, posterization, dithering, speckling and compression artifacts, and leave out camera terms (ISO, sensor noise, film grain).
9. **Filter-safe words.** Write "a single row of buttons" or "a double row of buttons", never single-breasted or double-breasted (they trigger an HTTP 400 safety block).
10. **Language.** Write the prompt and the negative prompt in English and everything else in the user's language (usually Traditional Chinese).

## Workflow

1. **Classify the layout image.**
   - *Storyboard sketch*: trace the vanishing directions to find the camera, decide what each block is, and lock positions by frame fractions (where each head, pillar, rail and wheel sits). Keep the layout but discard the drawing: tell the model to drop pencil lines, grey tones, panel borders, timecode boxes and subtitles, and add "zero outlines, no sketch lines", because sketch lines leak into renders even under "no painterly".
   - *Grey clay render*: the grey surfaces carry no design. Keep the terrain silhouettes and dress them (a grey hill becomes a canopy-covered ridge on the same outline), and keep the vehicle's structure.
2. **Map the images.** Number them in this shot's upload order: Image 1 is the layout, then the references, with the style reference last. Note which character or prop each image shows and which parts of each fall inside the frame.
3. **Check for an established look.** If the conversation or memory has already settled a look for this project (recognizable by its characters, vehicle or plate), reuse it, including the user's adjustments, instead of the default.
4. **Read the brief.** Show the time of day through sky and light color (early morning: a pale, clear sky warming near the horizon), not through dramatic directional light. Put the setting into the ground, terrain and sky.
5. **Write the prompt** as one paragraph in this order:
   1. Render instruction, look and setting, front-loaded ("Render the grey untextured clay layout of Image 1 in …, set on …").
   2. Style-reference clause, composition lock, references-for-design clause.
   3. Environment: ground, terrain on its exact silhouettes, sky.
   4. Vehicles and props, with any required text.
   5. Characters, each as pose and expression from the layout plus design from its reference, visible parts only, accessories explicit; then "no other people".
   6. Clothing and skin clause.
   7. Lighting, then color grade.
   8. Style, anti-realism and the outline decision.
   9. Framing lock ("Keep the exact 16:9 framing and crop of Image 1; do not zoom out, widen, recompose or move …"), text rule, artifact clause.
6. **Write this shot's own negative prompt** (rule 6), then the notes.

## Lighting variants

Swap only the lighting sentence and keep the rest of the prompt.

- **Default / 平光.** "Soft diffused [time] daylight that gives every form gentle soft volume, with smooth falloff into soft cool-tinted shadows, soft ambient occlusion where forms meet and soft blurred contact shadows; no hard cast shadows, no sharp or glossy specular highlights, no shiny surfaces, no rim light, no strong backlight and no lens flare." In this library 平光 means this: soft light *with* volume, not shadowless flat fills.
- **A little more contrast** (when the user asks for more 對比 or 立體感). "Gentle [time] sunlight from the upper left at a moderate angle, with a little more light-and-shadow contrast: lit sides clearly brighter and warmer, shadow sides in deeper cool blue-violet tones with a defined but soft-edged terminator, soft-edged medium-length cast shadows, slightly stronger ambient occlusion; the contrast stays moderate and every shadow keeps visible color and detail rather than going black, still with no sharp or glossy highlights, rim light or lens flare." In the negative prompt, remove `high contrast` and `hard shadows` and ban `crushed black shadows, extreme contrast` instead. To dial it down, write "slightly more" and drop the cast-shadow clause; to dial it up, write "clear" and "noticeably deeper".

## Output format

Write the headings in the user's language:

### 🧠 構思解析
Three to six bullets: how you read the layout (camera, what each block is), what is locked, what was dressed or dropped, and which look and lighting variant you used and why.

### 🎨 最終提示詞
One ```text block holding only the English prompt, as one continuous paragraph.

**負面提示詞**: one ```text block tailored to this shot.

**使用時注意**: the image order for this shot (including the style reference, which the user re-uploads every shot), plus one or two fixes to try if a known risk shows up (inpaint a small area such as a plate or a wrist instead of regenerating; how to dial the lighting).

**Revisions.** When the user asks for a tweak, re-deliver the full prompt and negative prompt with only that change, and list what changed in the 構思 bullets. Don't treat an exploratory tweak ("試試") as the new settled look until the user confirms it.

For a complete accepted example (clause order, density, notes), read `references/worked-example.md`. Copy its structure, never its characters.

## Base negative prompt

Start from this list and edit it per shot. Remove `outlines, line art` when the user wants lines, and swap the scene-specific items (mud, bark, rocks) for the current setting:

```text
photorealistic, realistic rendering, PBR realism, ray-traced reflections, realistic mud texture, realistic bark, boulders, rocks, exposed roots, flat unshaded colors, hard-edged cel shading, outlines, line art, sketch lines, 2D illustration, hard shadows, high contrast, strong specular highlights, glossy, shiny, wet sheen, rim light, strong backlight, lens flare, god rays, heavy fog, grunge, heavy weathering, film grain, noise, color banding, posterization, compression artifacts, blotchy skin, dirty face, extra text, garbled characters, watermark, extra people, changed pose, zoomed out, recomposed framing
```

## Gotchas

- **A golden key light, rim light, puddle reflections and long shadows** came back "太寫實、太多高光": the user wanted 平光. Default to soft diffused light, and drop reflective puddles or keep them matte.
- **Over-correcting to shadowless flat color with no texture** drifted away from the user's 3D target, which had soft volume and ambient occlusion, and the user asked to get closer to the reference. 平光 is soft light, not flat fills.
- **Rugged disaster words** (boulders, gravel, exposed roots, 山嵐, raw scars) turned a stylized background photographic. Write smooth bands and rounded canopy shapes instead.
- **A settled project look was missed**: a 三渲二 request whose references matched an earlier shot of the same project got a fresh look, with outlines, instead of that project's look. Check for a settled look first (workflow step 3).
- **A clay wrist band turned into a bracelet** on a character whose reference has bare wrists. State bare wrists and tell the model to ignore the layout shape. In the next shot a different character did wear a bangle, and the copied negative prompt "bracelet" would have erased it, so rebuild the negative prompt every shot.
- **A blanket "No text"** fought the required license plate. Write "apart from the plate, no other text".
- **A storyboard block was deleted** as a "van panel" that seemed to clash with the open-bed truck reference; it was actually the cab's rear wall. Read the perspective, and never drop a structure.
- **Sketch lines leaked** into the 3D render even though the prompt said "no painterly". Explicitly discard pencil lines, grey tones and overlays, and write "zero outlines".
