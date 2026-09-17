# Relight Craft — Writing the Image-Edit Prompt

Technical rules specific to **relighting an existing portrait photo** (as opposed to generating one from nothing). Read before compiling in Phase 2.

## Table of Contents
1. [Relight Feasibility Triage](#1-relight-feasibility-triage)
2. [Identity & Likeness Lock](#2-identity--likeness-lock)
3. [Light–Scene Coherence Law](#3-lightscene-coherence-law)
4. [Frame-Distance Discipline](#4-frame-distance-discipline)
5. [Clean-Skin Render Block](#5-clean-skin-render-block)
6. [Banned Vocabulary](#6-banned-vocabulary)
7. [The Golden Deconstruction Sequence](#7-the-golden-deconstruction-sequence)
8. [Worked Example](#8-worked-example)

---

## 1. Relight Feasibility Triage

**Read the source photo's existing light before promising anything.** An image model cannot simply "add a rim light" — it must re-render the entire shading, and wherever the new design contradicts the baked-in shadows, it will either ignore the instruction or melt the face. Triage first; it determines both what to propose in Phase 1 and what override language Phase 2 must carry.

| Source condition | Achievable | Required prompt handling |
|---|---|---|
| **Flat / soft / overcast / ring-lit** | Almost anything | Easiest case. Simply describe the new light in full. |
| **Soft directional (window light)** | Anything in the SAME hemisphere; opposite side is a fight | Keep the new key on the existing side, or explicitly command the reversal (see below). |
| **Hard directional with crisp shadows** | Same-direction intensification; anything else needs demolition | Must open with an explicit removal instruction: *"the original hard shadow across the left cheek is fully dissolved and replaced by…"*. Without this, two conflicting shadow systems appear. |
| **Strong backlight / silhouette** | More backlight, or added frontal fill | Facial detail may be genuinely absent in shadow; warn the user that the face will be partly re-invented. |
| **Mixed / colored light (neon, stage)** | Re-neutralizing is hard | State the new dominant color temperature explicitly and command the old cast be neutralized. |

**Direction reversal** is the single most destructive request. When the brief requires the key to cross to the other side, say so surgically: *"the light direction is reversed — the previously shadowed right side of the face now receives the key, while the previously lit left side falls into soft shadow; all original shadow shapes are removed and re-derived from the new light position."*

**Flag it to the user.** If the triage says the brief is high-risk, say so in Phase 1 in one sentence and offer a lower-risk alternative direction — do not silently produce a prompt that will fail.

---

## 2. Identity & Likeness Lock

Relighting re-renders the face, and re-rendering drifts the likeness. Every compiled prompt MUST embed an identity-lock clause naming the subject's fixed markers, so the model treats them as constraints rather than suggestions.

Name the markers actually visible in the source: **forehead height · eye spacing (interocular distance) · eye shape & lid type · brow shape and height · nose length, width and tip · mouth width & lip proportion · philtrum · cheekbone position · face shape · jaw and chin · hairline and hairstyle · any moles, freckles or scars**.

Reusable template — adapt the specifics to the actual photo:

> the subject's facial identity is preserved with absolute fidelity — the same forehead height, the same interocular eye spacing, the same eye shape and lid type, the same brow arch and height, the same nose length, width and tip, the same mouth width and lip proportion, the same cheekbone position, face shape, jawline and chin, the same hairline, hairstyle and individual markings; only the light falling across these unchanged features is redesigned, and no feature is slimmed, widened, enlarged, shortened, lifted or repositioned

Eye spacing and forehead height are the two markers that drift most often — always name them.

**Pose, gaze, expression and wardrobe are likewise locked** unless the user asked to change them. The default edit is *light only* (plus scene, when briefed).

---

## 3. Light–Scene Coherence Law

When the brief changes the environment (studio portrait → beach, café, night street), the #1 failure is a subject still wearing the old studio light pasted onto a new location. The composite is instantly recognizable as fake.

Every environment change MUST specify all four, and the subject's light must be **derived from the scene's own sources**:

1. **Direction** — where the scene's light comes from, and the matching key position on the face.
2. **Color temperature** — the scene's dominant Kelvin, and the same cast on the skin.
3. **Hardness** — clear noon sun on sand is hard; overcast sea mist is soft. The face must match.
4. **Bounce & ambient** — name what the environment reflects back: sand and water throw warm light up under the chin; a forest bounces green; snow fills from below; a red wall tints the shadow side.

Write it as a single causal statement, e.g.: *"the low sun sits behind her left shoulder, so her hair carries a warm rim while the bright sand reflects a soft golden fill back up into the shadowed side of her face."* Causality is what makes a composite read as one photograph.

Also state that the subject's **scale, perspective and horizon line** agree with the new environment, and that ground contact (feet, shadow on the sand) is physically correct where visible.

---

## 4. Frame-Distance Discipline

Judge the source's shot size first (head-and-shoulders bust, chest-up, waist-up, full-body). **Describe only what falls inside that crop.** Naming a garment, prop, or body part that lies outside the frame pushes the model to zoom out to include it, destroying the composition.

Default closing instruction: *"keep the exact same framing, crop and shot distance; do not zoom out, widen, re-pose, or extend the composition."*

If the brief genuinely requires a wider view (a beach scene barely reads in a tight headshot), do NOT silently widen — raise it in Phase 1 as an explicit choice, and if confirmed, command the reframe outright and name the new shot size.

---

## 5. Clean-Skin Render Block

Mandatory whenever human skin is in frame. Weave both halves into the prose — never emit them as headers or bullet lists inside the prompt.

**Positive half** (fold into the subject description):

> the complexion is rendered immaculately clean and even — smooth continuous tonal gradation across the forehead, cheeks and jaw, a soft natural matte finish, pores suggested only softly and subtly rather than exaggerated, entirely free of blotchiness, mottling, uneven color patches, redness, discoloration, dirt, smudges or shadow grime, retaining a healthy living skin quality without any plastic over-smoothed airbrushed look

**Negative half** (fold into the closing photography clause):

> accurate white balance with no green, grey or magenta cast anywhere in the skin, captured at base ISO with a pristine high signal-to-noise, high-bit-depth render — absolutely no chroma noise, no color noise, no luminance grain, no sensor noise, no speckling or dithering, no color banding, no posterization, no compression artifacts, and no muddy or dirty tonality on the face

**Deliberate-grain exception**: some lighting designs legitimately call for film grain (Lindbergh monochrome, noir, push-processed night). When grain is *part of the brief*, keep the grain, drop the grain-related negatives, and retain the rest — say explicitly `fine even silver-halide grain, never chroma noise or blotchy digital mottling`.

**Deliberate-shadow exception**: in a 1:8 chiaroscuro design the shadow side is *supposed* to go black. "No shadow grime" governs the **lit** side and the transition; it must not be used to flatten the intended darkness.

---

## 6. Banned Vocabulary

Never write these — diffusion models read them as permission to render a dirty face:

`unretouched texture` · `no skin smoothing` · `no retouching` · `raw skin texture` · `every pore visible` · `detailed pores` · `skin imperfections retained` · `natural skin texture fully retained`

Express "not plastic" the safe way instead: softly *suggested* pores plus an explicit ban on over-smoothing.

Also avoid empty lighting words that carry no optical instruction: `beautiful lighting` · `professional lighting` · `good light` · `dramatic lighting` (alone) · `cinematic` (alone). Every lighting claim must name a direction, a quality, a ratio, or a named pattern.

---

## 7. The Golden Deconstruction Sequence

Compile the English prompt as ONE continuous paragraph, no headers, in this weight order — front-loaded items receive the most model attention:

1. **Relight Directive** — the new light design, first and in full: key direction and height, source size and quality, named pattern, ratio, negative fill, rim/hair light, background falloff. Include any explicit removal of the source photo's original shadow system.
2. **Scene & Environment** *(only if the brief changes it)* — the new location, its own light sources, time of day, weather, atmosphere, and the bounce it throws back onto the subject. Must be causally consistent with block 1.
3. **Identity & Preserved Elements** — the identity-lock clause, plus pose, gaze, expression, hair, wardrobe, and any background elements that must survive.
4. **Skin Render** — the positive half of the Clean-Skin Render Block.
5. **Photography, Medium & Frame Lock** — lens and distance language, the instruction to inherit the source image's original medium, color response and grade, the framing lock, and the negative half of the Clean-Skin Render Block.

---

## 8. Worked Example

**Brief**: a chest-up studio portrait shot in flat frontal light → *「唯美的沙灘攝影」*.
**Triage**: flat soft source → low risk, free to place the new key anywhere.
**Design**: 唯美 80% / 氣氛 20% — golden-hour back-key, 1:2 ratio, sand bounce as fill, sea haze.

> A complete redesign of the light: the low late-afternoon sun is positioned behind the subject's left shoulder, just above the horizon, acting as a warm back-key that traces a luminous golden rim along the edge of her hair, the top of her shoulder and the line of her jaw, while the broad expanse of bright sand and water in front of her reflects a soft, wide golden fill back up into her face, holding a gentle 1:2 lighting ratio with luminous open shadows and lifted matte blacks; the original flat frontal studio shadow pattern is completely dissolved and re-derived from this single low sun, the key feathered so the light grazes rather than strikes, producing an extended silky gradient across the cheek and a delicate halation bloom around every highlight. She now stands on an open beach in the last half hour before sunset, a soft veil of sea haze diffusing the sun into a glowing disc, the ocean behind her dissolving into a warm bokeh of backlit spray and glinting water, fine airborne particles and loose strands of her hair catching the backlight as bright filaments, the whole frame carrying a warm, desaturated pastel palette of honey, pale rose and washed cyan. Her facial identity is preserved with absolute fidelity — the same forehead height, the same interocular eye spacing, the same eye shape and lid type, the same brow arch and height, the same nose length, width and tip, the same mouth width and lip proportion, the same cheekbone position, face shape, jawline and chin, the same hairline and individual markings; her pose, head angle, gaze, expression and clothing remain exactly as in the original, and only the light falling across these unchanged features is redesigned, with no feature slimmed, widened, shortened, lifted or repositioned. Her complexion is rendered immaculately clean and even, with smooth continuous tonal gradation across the forehead, cheeks and jaw, a soft natural matte finish, pores suggested only softly and subtly rather than exaggerated, entirely free of blotchiness, mottling, uneven color patches, redness, discoloration or shadow grime, retaining a healthy living skin quality without any plastic over-smoothed airbrushed look. Photographed on an 85mm lens at a shallow aperture with the same chest-up shot distance as the original, inheriting the source image's photographic medium, color response and grade; keep the exact same framing, crop and shot distance, and do not zoom out, widen, re-pose or extend the composition; accurate white balance with no green, grey or magenta cast anywhere in the skin, captured at base ISO with a pristine high signal-to-noise, high-bit-depth render — absolutely no chroma noise, no color noise, no luminance grain, no sensor noise, no speckling or dithering, no color banding, no posterization, no compression artifacts, and no muddy or dirty tonality on the face.

Note what the example does: block 1 names direction, height, quality, ratio, falloff AND kills the old shadow; block 2 supplies the sand bounce that *causes* block 1's fill; block 3 locks identity and pose; blocks 4–5 close with skin and frame discipline.
