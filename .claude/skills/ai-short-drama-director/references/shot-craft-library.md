# Shot Craft Library（分鏡技巧庫）

Used in Step 5. Contents:
- §1 10-column storyboard spec
- §2 Narrative purpose
- §3 Shot groups & manga-panel logic
- §4 Split screen / image-in-image
- §5 Action–reaction variants
- §6 Technique library with prompt phrases
- §7 Shot size ↔ emotion
- §8 Camera movement ↔ meaning
- §9 Dutch angle & dolly zoom
- §10 Suspense construction
- §11 Image superposition

The **prompt phrase** column is the telegraphic English that goes into `type` / `action_prompt`. Never write the film titles or director names into a prompt.

---

## §1 10-Column Storyboard Spec（十欄分鏡表）

| Column | Content | Example |
|---|---|---|
| 鏡 | Continuous shot number from 1 (global across Clips) | 1, 2, 3 |
| 時長 | Global timecode | 00:00–00:04 |
| 角度 | Vertical angle | 平視／俯拍／仰拍／頂拍／微俯 |
| 景別 | Shot size | 大遠景／遠景／全景／中景／近景／特寫／大特寫 |
| 畫面內容 | Visible action only | 女孩提燈走過荊棘小徑 |
| 場景 | Space / location ID | L1 荊棘林 |
| 聲音 | All sound elements | 環境風聲；蛾翅拍動 |
| 備註 | Camera move, technique, VFX, subtitle cue | 慢推；前景懸疑 |
| 敘事目的 | Purpose tag + one-line reason | 建立｜交代空間與燈的設定 |
| Clip | Backfilled in Step 6 | C1 |

**Writing 畫面內容.**
- Write only what is visible, never psychology.
- Name key props explicitly.
- Use action sentences, not state sentences.
  - ✔ 「她把燈舉高」
  - ✘ 「她很害怕」

---

## §2 Narrative Purpose（敘事目的）

Narrative purpose is *why this shot must exist at this moment*, not "it looks good".
**Loop:** ask what the shot is for. If you cannot answer, cut it or merge it. If you can, ask whether another shot would serve that purpose better.

| Tag | Meaning | Typical use |
|---|---|---|
| 建立 Establish | Space, time or mood | Opening shot, environment intro |
| 推進 Advance | Pushes the plot | Action and reaction shots |
| 揭示 Reveal | Key information surfaces | Evidence found, truth exposed |
| 強調 Emphasize | Weights a moment | Climax expression, key prop |
| 轉場 Transition | Links two scenes | Empty shot, bridge |
| 情緒 Emotion | Carries feeling, not information | Slow motion, freeze, extended hold |
| 內省 Reflect | Externalizes the inner self | Reflection, subjective shot |

---

## §3 Shot Groups & Manga-Panel Logic（鏡頭組）

**Shot group types:**
- **Montage:** multiple images in fast cuts, 1–3 s each. These must be packed into one Clip (see `clip-assembly.md` §3).
- **Progressive:** each shot adds information or intensifies emotion.
- **Causal:** action → reaction.
- **Contrast:** images set against each other.

**Manga-panel logic translated to video:**

| Panel device | Meaning | Video equivalent |
|---|---|---|
| Large panel | Emphasis, pause | Wider or tighter extreme plus a longer hold (3–5 s) |
| Small panel | Speed, urgency | Short shot (1.5–2 s) inside a multi-shot Clip |
| Tilted frame | Imbalance | Dutch angle (§9) |
| Circular frame | Focus, subjectivity | `iris vignette POV`, `seen through keyhole / telescope` |
| Body crossing the panel border | Links two spaces | Match cut on movement, or `body wipe` transition |

---

## §4 Split Screen & Image-in-Image（分割畫面與畫中畫）

Video models render literal split screens poorly, so use in-world equivalents:
- **Simultaneous display** (parallel spaces or views) → `split by architecture: doorframe divides left room and right room`
- **Nested perspective** (a main view containing a secondary one) → `image-in-image via mirror / TV screen / window reflection showing second figure`
- **Audience knows, character doesn't** → keep the threat inside the secondary image: `in mirror behind her, shadow rises; she faces camera unaware`

---

## §5 Action–Reaction Variants（動作–反應 12 變體）

Basic unit: one action (behaviour) shot + one reaction (result) shot.

| # | Variant | Pattern | Use |
|---|---|---|---|
| 1 | Standard | action → reaction | Baseline cause and effect |
| 2 | Reaction first | reaction → action | Creates suspense |
| 3 | Stacked actions | A + B + C → reaction | Accumulated pressure |
| 4 | Omitted reaction | action → (none) | Blank space for the most important moment |
| 5 | Hidden action | (sound of action) → visual reaction | Sound–image split |
| 6 | Delayed reaction | action → daily life → reaction | Realism |
| 7 | Synchronous | action and reaction in one frame | Information density |
| 8 | Reaction chain | action → A → B → C | Shows the radius of impact |
| 9 | Repeated gradient | action → reaction → same action, slightly changed | Passage of time |
| 10 | Counterpoint | image action + contradictory sound | Reveals contradiction |
| 11 | Omitted action | reaction → reaction → reaction | The key event stays beyond the frame |
| 12 | Chain link | reaction A becomes action B | Domino progression |

---

## §6 Technique Library（技巧庫，含 prompt 片語）

★ = mastery priority, from the source rating.

### Composition (12)

| Technique | Reference | ★ | Use | Prompt phrase |
|---|---|---|---|---|
| Lead room / psychological space | *The Godfather* | ★★★★★ | Dialogue, emotion | `off-center subject, wide lead room in gaze direction` |
| Frame within frame | *In the Mood for Love* | ★★★★★ | Division, alienation | `framed through narrow doorway, walls crowd edges` |
| Symmetry and its break | *The Shining*, *2001* | ★★★★★ | Oppression, ritual | `one-point perspective, perfect bilateral symmetry` / `symmetry broken by lone figure off-axis` |
| Negative space | *The Revenant*, *2001* | ★★★★★ | Minimalism, blank emotion | `tiny figure, vast empty negative space` |
| Leading lines | *Citizen Kane* | ★★★★ | Depth, gaze guidance | `converging lines lead to subject` |
| Rule of thirds | *The Queen's Gambit* | ★★★ | Base composition | `subject on right third` |
| Environmental detail + imagery | Descriptive establishing | ★★★★ | Emotional hint, time passing | `macro of melted candle stubs, dust on untouched plate` |
| Dutch angle | *Psycho*, *Batman* | ★★★★ | Imbalance | `dutch angle 20°` (see §9) |
| Eye close-up | Storyboard tutorial | ★★★★ | Emotional focus | `extreme close-up eyes, reflection in iris` |
| Depth of field | *Citizen Kane*, *Barry Lyndon* | ★★★★ | Sharp vs. soft contrast | `deep focus, foreground and background sharp` / `shallow focus, background dissolves` |
| Progressive distance | Storyboard basics | ★★★★ | Emotional build or release | Successive shots tighten: wide → medium → close |
| Manga-style asymmetric panels | Kon / Urasawa lineage | ★★★★ | Externalized emotion, rhythm | See §3 |

### Camera Movement (10)

| Technique | Reference | ★ | Use | Prompt phrase |
|---|---|---|---|---|
| Push-in | *The Shining* | ★★★★★ | Emotional build, focus | `slow dolly push-in` |
| Pull-back | *Goodfellas*, *Once Upon a Time in the West* | ★★★★★ | Space opens, reveal | `slow pull-back reveals surroundings` |
| Tracking | *1917*, *Birdman* | ★★★★★ | Following, presence | `lateral tracking alongside subject` |
| Handheld | *Saving Private Ryan*, *Black Swan* | ★★★★ | Realism, tension | `handheld, subtle shake, breathing camera` |
| Crane / elevation | Storyboard basics | ★★★★ | Power shift, space change | `crane up from ground to high angle` |
| Pan | Storyboard basics | ★★★ | Showing space | `slow pan left across room` |
| Long vs. short take rhythm | *Gravity*, *The Bourne Ultimatum* | ★★★★ | Rhythm change | Long single take, then rapid cuts |
| Fast cutting | *The Bourne Identity*, *Mad Max: Fury Road* | ★★★★ | Tension, impact | `rapid cuts, 1-second shots` (montage only) |
| Slow motion vs. normal speed | *The Matrix*, *The Girl Who Leapt Through Time* | ★★★★ | Amplify emotion, stretch time | `slow motion, drifting particles` |
| Dolly zoom | *Vertigo*, *Jaws* | ★★★★★ | Vertigo, psychological distortion | See §9 |

### Shot Connection (8)

| Technique | Reference | ★ | Use | Prompt phrase |
|---|---|---|---|---|
| Eyeline match | *Psycho*, *Rear Window* | ★★★★★ | Gaze → object | `she looks off-frame left` → next shot `POV of object` |
| Over-the-shoulder (OTS) | *Citizen Kane*, *12 Angry Men* | ★★★★ | Dialogue | `over-the-shoulder from behind S1` |
| Reaction shot | *Jaws*, Kuleshov | ★★★★★ | Amplify emotion | `hold on face, reacting to off-screen event` |
| Insert | *The Godfather*, *Rocky* | ★★★★ | Detail emphasis | `insert close-up of key in palm` |
| Crossing the line (deliberate) | *The Shining*, *Citizen Kane* | ★★★★ | Tension, rule-breaking | `reverse angle across axis, screen direction flips` (mark in 備註) |
| Scene linking | Storyboard basics | ★★★ | Smooth transition | Carry colour, shape or sound over the cut |
| Shot size + length rhythm | Storyboard basics | ★★★★ | Rhythm design | Alternate wide/long with close/short |
| Freeze-frame emphasis | *Thelma & Louise*, *Bonnie and Clyde* | ★★★ | Key moment | `motion halts, near-frozen frame, only dust drifts` |

### Transitions (6)

| Technique | Reference | ★ | Use | Prompt phrase |
|---|---|---|---|---|
| Graphic match | *2001* | ★★★★★ | Visual spectacle | `end on round moon` → next `open on round clock face` |
| Wipe / occlusion | *October*, *Decisive Engagement* | ★★★★ | Space switch | `dark foreground object passes lens, wipes to next scene` |
| Fade | *Braveheart*, *Shawshank* | ★★★ | Emotional transition | `fade to black` / `candle snuffed to black` |
| Match on action | *Crash*, *Forrest Gump* | ★★★★ | Time/space jump | `hand turns key — cut — same hand older, same motion` |
| Sound bridge | *Apocalypse Now*, *The Godfather* | ★★★★★ | Sound carries over | `audio_prompt: [SFX] pre-lap: church bell from next scene` |
| Cross-cutting | *The Godfather*, *Inception* | ★★★★ | Two lines of action | Alternate Clips or shots between two locations |

### Subjective / Objective (4)

| Technique | Reference | Use | Prompt phrase |
|---|---|---|---|
| POV | *Psycho*, *Rear Window* | Audience becomes the character | `first-person POV, hands visible at frame bottom` |
| OTS | *Citizen Kane*, *The Social Network* | Builds relationships | `over-the-shoulder` |
| Reaction shot | *Jaws*, *North by Northwest* | Amplifies emotion | `reaction close-up` |
| Insert | *There Will Be Blood* | Emphasizes a detail | `insert macro` |

### Suspense & Tension (5)

| Technique | Reference | Use | Prompt phrase |
|---|---|---|---|
| Foreground suspense | *The Lady Vanishes*, *Psycho* | Delayed suspense | `threat object sharp in foreground, unaware subject soft behind` |
| Kill-zone fixed shot | *Psycho* | Tense standoff | `camera settles, locked-off static, action enters frame` |
| Axis confusion | *Psycho* (shower scene) | Panic, terror | `disorienting angles, broken screen direction, fragmented cuts` |
| Symmetric oppression | *The Shining*, *2001* | Solemn dread | `dead-center symmetry, long corridor, slow steady track` |
| Jump cut | *Breathless*, *Breaking Bad* | Time compression | `jump cut, same frame, subject shifts position` |

### Special (3)

| Technique | Reference | Use | Prompt phrase |
|---|---|---|---|
| Split screen | *Dragnet*, *Crash* | Multi-line narrative | Use architecture splits (§4) |
| Image-in-image | Kon lineage, *Perfect Blue* | Nested perspective | `mirror / screen shows second scene` |
| Split + image-in-image | Kon lineage | Complex narrative | Doorframe split + mirror inside one half |

---

## §7 Shot Size ↔ Emotion（景別與情緒）

| Size | EN | Distance | Emotional tendency | Use |
|---|---|---|---|---|
| 大遠景 | extreme wide | Alienation, sacredness | Awe, smallness | Opening, sense of fate |
| 遠景 | wide | Observer | Objective, calm | Environment, farewell |
| 全景 | full shot | Character + environment | Narrative balance | Complete action, space |
| 中景 | medium | Social distance | Everyday, conversation | Interaction |
| 近景 | medium close-up | Personal | Intimacy, attention | Emotional detail, props |
| 特寫 | close-up | Intimate | Intense, oppressive or fragile | Expression peak, key item |
| 大特寫 | extreme close-up | Extreme focus | Suffocation, intrusion | Psychological extreme, impact |

---

## §8 Camera Movement ↔ Meaning（運鏡與敘事）

| Move | EN | Meaning | Typical use |
|---|---|---|---|
| 推 | dolly in | Approach, scrutiny, revelation | Resolve, discovering the truth |
| 拉 | dolly out | Withdrawal, escape, revealing the environment | Endings, reveals |
| 橫移／搖 | track / pan | Crossing space, observer's view | Following, scanning |
| 升降 | crane / jib | God's view, revelation, farewell | Openings, fate turns |
| 旋轉 | orbit / roll | Dizziness, loss of control, romance | Drunkenness, romance, panic |
| 主觀 | POV | Audience becomes the character | Immersion, fear, desire |
| 靜止 | locked-off | Calm watching, waiting, suppression | Interrogation, stares, the calm before the storm |

---

## §9 Dutch Angle & Dolly Zoom

**Dutch angle grading:**
- **Slight, 5–10°:** vague unease. Phrase: `slight dutch tilt`
- **Moderate, 15–30°:** clear imbalance. Phrase: `dutch angle 20°`
- **Extreme, 45°+:** breakdown, nightmare. Phrase: `extreme 45° canted frame`

**Dolly zoom (Hitchcock zoom).** Camera movement and focal length change in opposite directions: the subject stays the same size while the background perspective warps. It reads as spatial distortion, psychological vertigo or the world collapsing.
- **Pull out + zoom in:** background expands. Phrase: `dolly out while zooming in, background stretches away, subject fixed center`
- **Push in + zoom out:** background compresses. Phrase: `dolly in while zooming out, background rushes forward, subject fixed center`
- **Style-agnostic template:** `dolly zoom, subject locked center frame, background perspective warps, [style lock], [light lock]`
- **When to use:** the moment of entering the uncanny world, discovering the horrifying truth, or a psychological stability that collapses. Use at most once per film.

---

## §10 Suspense Construction（懸疑構建）

- **Foreground suspense:** put the key prop in the foreground. The audience knows and the character does not, so the composition carries the clue instead of dialogue. `threat in sharp foreground, subject unaware in soft background`
- **Kill-zone fixed shot:** move the camera into the danger zone → lock it off for the key action → move it away. In a multi-shot Clip this becomes three shots: `track into doorway` → `locked-off static` → `slow drift away`.

---

## §11 Image Superposition（意象疊加）

Replace statements with images:
- Table lamp dimming to the size of a coin → the length of the night.
- Steam condensing on eyelashes → a mother's love, never said.
- A fingerprint on a milk glass → a key plot hint.

**Default-style image bank:**
- A moth circling a dead candle → hope running out.
- A stopped clock whose hands twitch → a loop.
- A covered mirror → denied identity.
- A doll with a mended seam → an old wound.
