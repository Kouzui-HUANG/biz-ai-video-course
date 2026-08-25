# Sexual Dimorphism Atlas — Anatomy Reference

> All entries are **statistical tendencies with wide overlap**, not rules. Individual and ethnic variation is large; many men have soft bone structure and many women have angular structure. Use them as directional levers for a prompt, never as claims about a real person.

## 1. Skull & Bone (hardest to fake, highest prompt value)

| Region | Feminine tendency | Masculine tendency |
|---|---|---|
| Forehead | vertical, rounded, frontal bossing visible | slopes backward, flat transition to nasion |
| Supraorbital ridge | flat, smooth transition brow→orbit | pronounced transverse shelf, deep brow shadow |
| Orbits | larger, rounder, thin upper rim | deeper, squarer, more recessed eye |
| Zygomatic | high, anterior, rounded apple | arch flares laterally, wider and flatter |
| Mandibular angle | obtuse (>125°), soft taper | near 90°, masseter attachment flares |
| Chin | narrow, short, round or gently pointed | wide, tall, square; mental crease or cleft |
| Nasal | narrow bridge, deep nasofrontal notch | high/wide bridge, straight or dorsal hump, shallow notch |
| Midface height | shorter; overall oval / heart face | longer; overall square / rectangular face |
| Brow-to-rim | brows sit **above** the orbital rim, arched | brows sit **on or below** the rim, flat |

## 2. Soft Tissue

- **Fat pads** — feminine: thicker superficial malar fat, continuous smooth contour. Masculine: thinner fat, visible masseter and zygomatic relief.
- **Eyelid show** — feminine: more visible upper-lid platform under a high arched brow. Masculine: brow crowds the lid, minimal platform.
- **Philtrum** — feminine: short, more upper-tooth show at rest. Masculine: long.
- **Lip red** — feminine: fuller, defined cupid's bow. Masculine: thinner, flatter vermilion border.
- **Skin** — feminine: thinner, finer pores, more translucency. Masculine: thicker, coarser pores, more sebum, beard-field shadow.
- **Hairline** — feminine: continuous rounded arc. Masculine: M-shaped temporal recession, larger exposed forehead.
- **Expression lines** — masculine: deeper forehead and glabellar creases from larger muscle excursion.

## 3. Neck, Shoulders, Arms, Torso — the bust-shot signals

On any chest-up or wider crop these are read **before** the face. Never skip them when visible.

| Region | Feminine tendency | Masculine tendency |
|---|---|---|
| Neck | longer, slimmer, no laryngeal prominence, soft SCM | thicker, shorter-looking, visible Adam's apple, corded SCM |
| Trapezius | gentle slope from neck to shoulder | steep thick slope, bulk at the neck root |
| Shoulder width | narrower; acromion points soft | broader; acromion squared and bony |
| Clavicle | shorter span, delicate, soft supraclavicular hollow | longer, thicker, more horizontal |
| Deltoid | small, smoothly rounded, no striation | large, squared cap, visible striation |
| Upper arm | slim continuous taper, soft contour | thicker, defined biceps/triceps separation |
| Ribcage | narrower, higher waist read | broader, deeper |
| Chest | modest natural breast contour | flat broad pectoral plane |
| Shoulder-to-head ratio | ≈ 2 head-widths | ≈ 2.5–3 head-widths |

## 4. Occlusion Map — what each styling choice removes from play

Use with SKILL.md §4. If a feature is occluded, its clause is wasted weight **and** risks the model altering the occluder to "show" it.

| Styling | Occluded | Still fully readable |
|---|---|---|
| Blunt fringe at brow level | forehead slope, hairline, frontal bossing | brow ridge shadow, brows, jaw, chin, neck |
| Side-swept fringe | partial hairline | most of the forehead, all lower face |
| Long hair over shoulders | outer shoulder line, trapezius slope | neck, clavicles, jaw |
| Hair fully tied back | nothing | everything |
| Turtleneck / high collar | neck, Adam's apple, clavicles, chest | full face, jaw silhouette |
| Spaghetti-strap / bare-shoulder top | nothing above the chest | shoulders, clavicles, trapezius, deltoids, arms |
| Head-and-shoulders tight crop | arms, chest, ribcage | face, neck, shoulder tops |
| Face-only close crop | all body signals | face only — push ranks 1/2/4/6 hard |
| Kept beard | skin field, chin outline | brow, forehead, cheekbone, neck |
| Glasses | brow-ridge shadow readout | jaw, chin, lips, neck |

## 5. Direction-Specific Traps

**M→F**
- Removing beard shadow alone reads as "shaved man", not woman — rank 1 and 2 must lead.
- Do not narrow the nose unless asked; the nose is a top identity anchor and narrowing it is the fastest way to lose likeness.
- Long hair without a shoulder-line change reads as a man in a wig on any bust crop.
- Adding makeup is a *separate* request — do not add it unprompted (that belongs to `prompt-master-makeup`).

**F→M**
- Adding a beard alone reads as a costume; the brow ridge and jaw must carry the change.
- Squaring the jaw without lowering the brows leaves the face reading feminine.
- Shorter hair usually exposes the hairline — the M-shaped recession becomes newly available weight (the inverse of occlusion).
- Do not automatically age the subject; masculinisation and ageing are independent axes.

**→ Androgynous**
- Do not average every feature — that yields a bland face. Force ranks 1 and 2 to the midpoint and hold the rest neutral.
- Keep the neck slim but not delicate; the neck is the giveaway in either direction.
- Neutral styling (hair, clothing) is the *weakest* lever; state it last, never as the main mechanism.
