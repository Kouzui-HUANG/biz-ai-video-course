# Portrait Lighting Knowledge Base — Design System & English Vocabulary

Reference library for designing portrait light and translating it into precise English prompt terminology. Every term maps to a visible optical effect, not decoration. Read before writing proposals (§1, §6) and before compiling the final prompt (§10).

## Table of Contents
1. [The Three Design Axes (唯美 / 專業 / 氣氛)](#1-the-three-design-axes)
2. [Core Variables (光質 · 光比 · 減光 · 羽化)](#2-core-variables)
3. [Facial Lighting Patterns (臉部布光法)](#3-facial-lighting-patterns)
4. [Modifier Personalities (控光器材性格)](#4-modifier-personalities)
5. [Natural Light Situations (自然光情境)](#5-natural-light-situations)
6. [Style Schools (可直接引用的流派)](#6-style-schools)
7. [Atmosphere Toolkit (氛圍工具)](#7-atmosphere-toolkit)
8. [Color Temperature Logic (色溫敘事)](#8-color-temperature-logic)
9. [Light Angle vs Skin Texture (光角與質感)](#9-light-angle-vs-skin-texture)
10. [English Vocabulary Library (成句詞庫)](#10-english-vocabulary-library)
11. [Failure Modes (避雷清單)](#11-failure-modes)

---

## 1. The Three Design Axes

These are **independent**, not a scale. Most briefs are a blend — decide a ratio (e.g. 70% 唯美 / 30% 氣氛) before designing.

| | 唯美 Ethereal | 專業 Clean/Commercial | 氣氛 Cinematic/Moody |
|---|---|---|---|
| Key direction | back / side-back 逆光·側逆光 | front-side 45° | strongly directional, off-axis |
| Quality | very soft, huge source, feathered | soft but controlled (gridded) | harder, shaped, motivated |
| Lighting ratio | 1:1.5 – 1:2 | 1:3 – 1:4 | 1:8 – 1:16 |
| Blacks | lifted, matte roll-off | true black, clean | crushed, deep |
| Signature | hair halo, bloom, haze, flare | rim separation, clean catchlights | volumetric beams, gobo shadows |
| Color | warm, desaturated pastel | neutral, accurate | teal-orange or single hue wash |
| Risk | mushy, no structure | sterile, no emotion | muddy, face unreadable |

**Antidote per risk**: 唯美 → keep one crisp edge (rim on the jaw or an in-focus eye). 專業 → let one shadow have shape. 氣氛 → guarantee at least one catchlight and a readable eye.

---

## 2. Core Variables

**Light quality = apparent source size.** Softness depends only on how large the source appears from the subject's position. The same softbox: moved **closer** → softer AND faster falloff (background drops dark); moved **farther** → harder AND more even coverage. This single lever produces two completely different looks from one light.

**Inverse-square law as a background control.** To darken a background without touching it, bring the key closer and reduce its power. To lift subject and background together, pull the key back. Prompt this as *"key light placed intimately close, its rapid falloff sinking the background into darkness"*.

**Lighting ratio** (key vs fill, in stops):

| Ratio | Stops | Reads as |
|---|---|---|
| 1:1 – 1:2 | 0–1 | flat, airy, advertising-clean |
| 1:3 – 1:4 | 1.5–2 | classic portrait dimension |
| 1:8+ | 3+ | low-key, dramatic, chiaroscuro |

**Negative fill 減光** — the amateur/professional dividing line. A black flag on the shadow side subtracts ambient bounce and makes the transfer edge appear. Most people only think about *adding* light; professional shaping comes from *subtracting* it. EN: `black negative fill subtracting ambient bounce from the shadow side, carving a crisp transfer edge along the cheek`.

**Feathering 羽化打光** — aim the *edge* of the modifier across the face rather than its hot center. Stretches the falloff gradient → silk-like skin transition. This is the technical source of the 唯美 quality. EN: `the key feathered so only the soft edge of the source grazes the face, producing an extended luminous gradient`.

---

## 3. Facial Lighting Patterns

| Pattern | Setup | Signature | Best for |
|---|---|---|---|
| **Butterfly / Paramount** 蝴蝶光 | high, directly frontal | small butterfly shadow under nose | glamour, beauty, cheekbones |
| **Rembrandt** 林布蘭光 | ~45° up and to the side | lit triangle on the shadow-side cheek — no longer than the nose, no wider than the eye | painterly, weighty, classical |
| **Loop** 環形光 | slightly more frontal than Rembrandt | short nose loop that does NOT touch the cheek shadow | **most universal, flatters nearly every face** |
| **Split** 分割光 | 90° side | half lit / half dark | tension, mystery, noir |
| **Clamshell** 蚌殼光 | key above + reflector/fill below | ultra-even skin, twin stacked catchlights | beauty, the safest "clean pretty" |
| **Short lighting** 短邊光 | lit side faces AWAY from camera | slims, adds emotion | **default choice for flattering portraits** |
| **Broad lighting** 寬光 | lit side faces camera | widens the face | usually avoid unless deliberately open/friendly |

Lamp height rule: slightly **above** eye level = alert and slimming; **at** eye level = intimate and neutral; **below** eye level = uplight, uncanny/sinister.

---

## 4. Modifier Personalities

| Tool | Character | EN term |
|---|---|---|
| Softbox | even, predictable, rectangular catchlight | `large softbox`, `gridded softbox` |
| Beauty dish 雷達罩 | half-soft with a hard "core" in the highlight | `beauty dish` |
| Parabolic 拋物線傘 | focused soft light — high contrast yet gentle | `parabolic reflector`, `focused soft key` |
| Shoot-through umbrella | spills everywhere, forgiving, lifestyle | `shoot-through umbrella` |
| Fresnel 菲涅爾 | hard, crisp-edged shadows, old Hollywood | `fresnel spotlight`, `hard focused beam` |
| Snoot / optical spot | a single small hard pool of light | `snooted light`, `optical spot projection` |
| Ring light | shadowless, ring-shaped catchlight | `ring light` |
| Bounce 跳燈 | enormous indirect source, natural interior | `bounced off a white wall/ceiling` |

Reflector colors: **white** = natural fill · **silver** = sharp specular fill · **gold** = warm skin · **black** = negative fill (subtract).

**Specular roll-off** — a large source makes the highlight a long gradient rather than a white blob. This gradient is what reads as "expensive". EN: `long specular highlight roll-off across the cheekbone`.

---

## 5. Natural Light Situations

- **North-facing window + sheer curtain** — a natural softbox, constant all day. Closer to the glass = softer + faster falloff.
- **Overcast** — a sky-sized softbox; add a reflector or direction (doorway, wall) or it goes flat.
- **Golden hour backlight** — low warm sun behind the subject, hair rim + haze, gold reflector under the chin.
- **Blue hour + one warm practical** — automatic cool/warm separation with zero gels.
- **Open shade** — soft and neutral, but watch for a green cast from foliage bounce.
- **Dappled light 斑駁光** — leaf-filtered sun; romantic but must not fall randomly across the eyes.
- **Backlit haze / sea spray / dust** — makes the light itself visible, the cheapest route to atmosphere.

---

## 6. Style Schools

Quoting an existing visual grammar is faster and more reliable than describing technique from scratch. Use these as proposal names and as prompt anchors.

- **Old Hollywood Glamour** (Hurrell) — hard fresnel + butterfly key + strong hair light + deep black ground; eyes appear lit from within.
- **Film Noir** — split light, window-blind gobo, cigarette haze, 1:16 ratio, large areas of true black.
- **Dutch Golden Age** (Vermeer / Rembrandt) — single left window, dark ground, rapid falloff across the face.
- **Caravaggio Tenebrism** — one steep shaft from above, everything else extinguished; maximum drama.
- **Japanese High Key 日系** — wall-bounced light, slight overexposure, low contrast, backlit spill, transparent and clean.
- **Peter Lindbergh** — pure natural light, monochrome, coarse grain, no beautifying, anti-fashion truthfulness.
- **Paolo Roversi** — long exposure with hand-torch light painting; dreamlike softness over deep shadow.
- **Gregory Crewdson** — a full film crew's lighting applied to a still; uncanny, hyper-lit suburbia.
- **Korean studio / K-beauty** — near-shadowless, high key, ultra-even, minimal ratio.
- **Editorial fashion** — beauty dish or parabolic key, hard-ish, colored background gel, strong separation.

---

## 7. Atmosphere Toolkit

Physical effects beat post-processing every time — say them explicitly.

- **Haze / fog / sea mist** → makes beams visible. `volumetric light rays through atmospheric haze`, `crepuscular god rays`.
- **Practical sources 實用光源** (neon, lamp, candle, screen, street light) → the light has a visible in-frame justification. Motivated light is the core of 氣氛.
- **Gobo / cookie** → shaped shadows: `window-blind gobo shadow`, `foliage shadow patterning`, `window mullion shadow`.
- **Foreground occlusion** → shoot through leaves, fabric, glass: `out-of-focus foreground occlusion`, `shot through a veil of gauze`.
- **Particles in backlight** → `dust motes drifting in the backlight`, `sea spray catching the sun`, `falling petals`, `snow sparkle`.
- **Lens artifacts** → `anamorphic streak flare`, `prism flare`, `swirly Helios bokeh`, `uncoated-lens veiling glare`, `soft halation bloom around highlights`.
- **Wet surfaces** → rain, condensation, wet sand: they multiply every light source into speculars.

---

## 8. Color Temperature Logic

Warm = memory, safety, dusk, intimacy. Cool = distance, dawn, urban solitude.

- **CTO key + CTB ambient** → classic cinematic teal-and-orange separation.
- **Magenta + green** → unease, cyberpunk, clinical dread.
- **Monochromatic wash** → strong authorial signature; one hue floods everything.
- **Gel discipline**: a gelled background light MUST be gridded, or the color contaminates skin and muddies the complexion. EN: `gridded gel confined strictly to the background, leaving skin tone neutral`.

---

## 9. Light Angle vs Skin Texture

Frontal light suppresses pores → beauty, youth, polish. Raking side light magnifies texture → age, hands, fabric, weathered character. Moving the key from 0° to 80° changes the subject's *story* from flawless to lived-in. Choose deliberately, and state the choice in the prompt.

---

## 10. English Vocabulary Library

Paste-ready clauses. Combine 2–4 per prompt; never dump the whole block.

### 唯美 Ethereal
`soft diffused backlight wrapping the subject` · `golden-hour rim light tracing the hair into a luminous halo` · `feathered soft key grazing the face from a large source` · `gentle 1:2 lighting ratio` · `lifted blacks with a low-contrast matte roll-off` · `hazy atmospheric bloom` · `delicate halation around the highlights` · `warm desaturated pastel palette` · `out-of-focus foreground occlusion` · `gold reflector lifting the shadow under the chin`

### 專業 Clean / Commercial
`large gridded softbox key at 45 degrees` · `classic loop lighting on a short-lit face` · `clamshell lighting with a fill reflector below the chin` · `controlled 1:4 lighting ratio` · `black negative fill carving the shadow side` · `subtle hair light and a rim kicker separating subject from background` · `clean twin catchlights at ten o'clock` · `long specular highlight roll-off` · `separately lit seamless backdrop` · `editorial commercial polish`

### 氣氛 Cinematic / Moody
`single motivated practical light source justified inside the frame` · `chiaroscuro modeling at a 1:8 ratio` · `deep crushed blacks swallowing the shadow side` · `volumetric god rays cutting through atmospheric haze` · `window-blind gobo shadow patterning the wall` · `warm CTO key against cool CTB ambient, teal-and-orange separation` · `hard fresnel beam with crisp-edged shadows` · `tenebrist single shaft from high camera-left` · `neon practical spilling across the cheek`

### Pattern & Craft terms
`Rembrandt lighting with a defined cheek triangle` · `butterfly / Paramount key` · `split lighting` · `short lighting` · `key feathered across the face` · `rapid inverse-square falloff sinking the background` · `raking side light revealing texture` · `dragging the shutter to retain ambient glow` · `high-speed sync balancing flash against the sun`

---

## 11. Failure Modes

| Symptom | Cause | Fix in the prompt |
|---|---|---|
| Raccoon eyes, dead sockets | key too high | lower the key toward eye level; demand visible catchlights |
| Two shadows / two catchlight sets | fill too strong or a second key | specify ONE dominant key and a subordinate fill |
| Dirty, half-yellow half-green skin | mixed color temperatures | declare a single dominant color temperature; grid any gel |
| Background brighter than the face | no falloff control | pull the background down explicitly |
| Flat pancake face | no ratio, no negative fill | name a ratio and add negative fill |
| Muddy unreadable shadow side | crushed blacks with no rim | add a rim/kicker to redraw the silhouette edge |
