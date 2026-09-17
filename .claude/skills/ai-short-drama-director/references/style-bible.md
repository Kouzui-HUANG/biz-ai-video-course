# Style Bible（風格聖經）

Read before any output. Contents:
- §1 Default style — gothic grotesque-cute dark fairy-tale cinema
- §2 Style-gene translation
- §3 Style override protocol & presets
- §4 Content boundaries

---

## §1 Default Style（預設：哥德怪誕暗黑童話電影感）

### 1.1 Art-style lock (paste verbatim into every Clip's `art_style`)

```
Gothic dark fairy-tale animated film, stop-motion-like tactile miniatures, grotesque-cute character design, cinematic chiaroscuro, bioluminescent accents, 35mm film grain
```

### 1.2 Render sub-variants

Pick one and declare it. Only the first clause of the lock changes.

| Variant | First clause replacement | Use |
|---|---|---|
| **A Tactile stop-motion** (default) | `Gothic dark fairy-tale animated film, stop-motion-like tactile miniatures` | Handmade texture: felt, porcelain, wax, aged wood |
| B Gothic ink animation | `Gothic dark fairy-tale 2D animation, scratchy ink linework, watercolor washes` | Storybook feel, lighter budget |
| C Stylized 3D feature | `Gothic dark fairy-tale stylized 3D animated feature, soft subsurface skin` | Polished CG, wide audience |

### 1.3 Palette (60-30-10)

| Role | Colour | Hex |
|---|---|---|
| 60 Dominant | Ink black / bruised night blue | `#0E0B10` / `#1C2233` |
| 30 Secondary | Moss grey-green / bone ivory | `#2E3A34` / `#E8DCC4` |
| 10 Accent (pick one per film) | Candle amber · blood crimson · poison teal · fluorescent green | `#E0A040` · `#8E1B24` · `#3F8C85` · `#9BE564` |

The **fluorescent accent is the style signature**: bioluminescent moths, glowing fungi, glowworm threads, phosphorescent eyes. Keep it to 10% of the frame.

### 1.4 Light logic

- **One motivated key source per shot:** candle, lantern, moonlight shaft, hearth, bioluminescence, a cold window.
- Low-key chiaroscuro with deep shadows that still hold detail. Use rim light to separate silhouettes.
- Fog or haze makes light shafts volumetric.
- Light state is continuity. If it changes, cut to a new Clip (see `clip-assembly.md` §2).

### 1.5 Texture & grade

35mm grain, soft halation on practical lights, gentle vignette, slightly lifted blacks, desaturated except for the accent.

### 1.6 Character design (grotesque-cute)

- **Proportions:** elongated limbs, oversized heads and eyes, tiny mouths.
- **Materials:** porcelain skin with a hairline crack, stitched seams, button or glass details, fraying fabric.
- **Wardrobe silhouettes:** hooded capes, high collars, pinafores, tailcoats. Wardrobe carries one accent colour.
- **Grotesque stays uncanny, never wounded:** a seam, a crack, a too-wide smile, a wrong number of shadows.

### 1.7 Motif bank

Covered mirrors · keys · stopped clocks · birdcages · moths · candles · thorns · dolls · teeth · music boxes · crows · lanterns · spiral staircases · empty chairs.

### 1.8 Sound palette (for audio_prompt and the post-production score)

- **Ambience:** wind through keyholes, creaking timber, distant bells, rain on slate, moth wings, dripping wax.
- **Foley:** bare feet on cold stone, cloth drag, porcelain tick, key turning.
- **Score direction (post only):** detuned music box, low bowed strings with no melody, solo child choir hum, glass harmonica.

### 1.9 Forbidden in the default style

Sunny warm daylight · flat front lighting · glossy plastic surfaces · pastel candy palettes · explicit blood or wounds · cheap jump-scare framing · any on-screen text.

---

## §2 Style-Gene Translation（風格基因 → 技法描述）

Director and artist names never enter a prompt. Use the descriptor instead.

| Gene | What to take | Prompt descriptors |
|---|---|---|
| Hitchcock lineage | Suspense built from information gaps | `threat sharp in foreground, subject unaware`; `high-angle locked-off`; `dolly zoom` |
| Kubrick lineage | Symmetry, stillness, solemn oppression | `one-point perspective, bilateral symmetry`; `slow steady forward track down corridor` |
| Wong Kar-wai lineage (*In the Mood for Love*) | Framed spaces, divided compositions | `framed through doorway / window bars, walls crowd frame`; `narrow corridor, figures brush past` |
| Satoshi Kon lineage | Reality/illusion slips, image-in-image | `match cut from reflection to reality`; `mirror shows different action than subject` |
| Naoki Urasawa lineage | Rhythm from panel-size changes, weighted silence | `long wide pause, then sudden extreme close-up of eyes`; `held silent reaction` |
| Dark fairy-tale author voice | Gothic grotesque cartoon plus high-end cinema | The §1 lock |

---

## §3 Style Override Protocol & Presets（風格覆寫）

If the user names a style, it **replaces §1 entirely**:
1. Rebuild the `art_style` lock (render medium + genre + light + grain) in ≤ 30 words.
2. Rebuild the palette (60-30-10 with hex codes, as in §1.3), the light logic (§1.4) and the forbidden list (§1.9) to match the new style. Use the preset's forbidden seed as the starting point.
3. Keep all director craft: templates, suspense, withholding, clip rules.
4. Declare the override in 設計假設.

**Presets.** Use a preset as a starting point and adapt it to the user's wording.

| User says | Art-style lock seed | Light / palette note | Forbidden seed |
|---|---|---|---|
| 寫實電影感 / photoreal | `Photorealistic cinematic live-action, anamorphic lens, natural skin texture, 35mm film grain` | Motivated practicals, teal-amber split | Plastic skin, cartoon proportions, flat even lighting |
| 日系動畫 / anime | `High-end Japanese 2D anime film, clean cel shading, painterly backgrounds` | Soft rim light, sky gradients | Photoreal skin, 3D render look |
| 水墨武俠 / wuxia | `Chinese ink-wash wuxia film look, wide 2.39:1, desaturated ink palette, heavy atmospheric fog, vintage film grain` | Fog-diffused daylight; dolly zoom suits the "entering the uncanny" moment | Saturated neon, modern objects |
| 賽博龐克 / cyberpunk | `Neon-noir cyberpunk cinematic, rain-slick streets, volumetric haze` | Magenta-cyan neon, wet reflections | Daylight scenes, pastoral palettes |
| 溫暖手繪 / cozy hand-drawn | `Warm hand-painted 2D animated film, gouache textures, soft daylight` | Golden hour; lift the "no warm sun" ban | Horror lighting, desaturated grade |
| 定格黏土 / claymation | `Claymation stop-motion film, fingerprint-textured clay, miniature sets` | Practical miniature lighting | Smooth CG surfaces, photoreal skin |

Never name studios, directors or living artists in the lock.

---

## §4 Content Boundaries（內容邊界）

- **Horror is suggested:** off-screen sound, a silhouette, a wrong shadow, a covered mirror. Never gore, dismemberment or explicit injury.
- **Child characters** may face danger by implication only. Never show harm to a child on screen.
- **No real-person likeness** unless the user supplies it as their own reference. Even then, see the face-reference caveat in `clip-assembly.md` §6.
- These limits also keep prompts clear of video-model content filters.
