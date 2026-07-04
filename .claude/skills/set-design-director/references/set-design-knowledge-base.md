# Set-Design Knowledge Base — Prompt-Crafting Edition

Professional set-design knowledge re-tooled as English phrase inventory for natural-language image models. Every table maps a design decision to ready-to-embed prompt phrasing.

## Table of Contents

1. [Space as Narrative — dramatic function → set detail](#1-space-as-narrative)
2. [Symbolic Devices — doors, windows, mirrors, stairs, corridors, tables](#2-symbolic-devices)
3. [Era & Culture Authenticity Kits](#3-era--culture-authenticity-kits)
4. [Anachronism Watchlist](#4-anachronism-watchlist)
5. [Camera-Aware Composition Vocabulary](#5-camera-aware-composition-vocabulary)
6. [Light × Material Interplay](#6-light--material-interplay)
7. [Props as Silent Dialogue — character prop kits](#7-props-as-silent-dialogue)
8. [Life-Trace Checklists by Room](#8-life-trace-checklists-by-room)
9. [Theory → Mood Vocabulary](#9-theory--mood-vocabulary)
10. [Final Quality Checklist](#10-final-quality-checklist)
11. [Worked Example](#11-worked-example)

---

## 1. Space as Narrative

Read the request the way a designer reads a script: not for the *location*, but for the *dramatic function of space*. Encode each answer as physical detail.

| Dimension | Question | Prompt-ready translation |
|---|---|---|
| Class & cultural capital | Rich? Cultured? Pretending? | `a genuine full-grain leather chesterfield` vs `a peeling faux-leather sofa`; `floor-to-ceiling custom walnut bookshelves` vs `sagging flat-pack shelving`; `tarnished heirloom silverware` vs `mismatched convenience-store cutlery` |
| Psychology | Controlling? Avoidant? Chaotic? | `a compulsively symmetrical room, every object squared to the furniture edges`; `unopened moving boxes stacked against the wall years after the move`; `curtains permanently drawn against daylight`; `a wall of CCTV monitors watching every room` |
| Relationships | Intimate or estranged? | `a long dining table with two place settings at opposite far corners`; `a living room with no trace of shared activity`; `a double bed divided by a wall of pillows` |
| Power | Who commands the space? | `a high-backed chair at the head of the table`; `a massive desk holding visitors at a distance`; `the boss's office raised half a level above the floor` |
| Dramatic state | Safe, seduction, trap, or judgment? | safe: `a warm lamplit bedroom, soft bedding` · seduction: `a mirrored bar glowing amber` · trap: `a long narrow corridor with doors on one side only` · judgment: `a vast, echoing boardroom arranged like a tribunal` |
| Character arc | Does the space change with the person? | early: `immaculate, plants thriving` → late: `dishes piling, wilted plants, framed photos removed leaving pale rectangles on the wall` |

---

## 2. Symbolic Devices

Classic spatial symbols with embed-ready phrasing:

- **Door = choice**: `a door left ajar, spilling a thin blade of hallway light`; `a locked door with a polished, untouched brass handle`; `a room no one is ever seen entering`.
- **Window = longing**: `a window overlooking neon-lit streets he can see but never reach`; `iron security bars striping the daylight`; `city lights smeared through rain on the glass`.
- **Mirror = divided self**: `a cracked vanity mirror splitting the reflection`; `a three-panel dressing mirror multiplying her into strangers`; `a mirror half-covered by a draped cloth`.
- **Stairs = hierarchy & pressure**: `a grand staircase ascending into warm light`; `basement steps descending into cold blue shadow`.
- **Corridor = transition, surveillance, fate**: `an endless hospital corridor under flickering fluorescent tubes`; `a hallway lined with identical locked doors`.
- **Dining table = family politics**: `an empty chair at a fully set table`; `place settings for four, only one used`; `the father's seat at the head, oversized, facing the door`.

---

## 3. Era & Culture Authenticity Kits

Period feel is not "stuff old things everywhere" — it is *how people of that time lived, bought, mended, and displayed themselves*. Anchor every prompt with a named decade + region + class, then deploy the kit.

**Research checklist (what to specify so the model doesn't default to modern):**

| Item | Specify in prompt |
|---|---|
| Architecture | window/door proportions, wall material, ceiling height, floor type (`narrow wooden sash windows`, `low stippled ceiling`, `worn terrazzo floor`) |
| Furniture | decade, origin, class, wear (`a 1960s teak sideboard, veneer lifting at one corner`) |
| Appliances | era-correct TV, fridge, phone, lighting, audio (`a rounded-corner CRT television`, `a rotary-dial telephone with a tangled cord`) |
| Daily goods | packaging, medicine, stationery, newspapers with era-correct typography and materials |
| Wardrobe-space logic | how clothes were stored/washed then (`a freestanding wardrobe`, `laundry on a bamboo pole outside the window`) |
| Regional culture | religious objects, eating utensils, festival decorations, family photos — keep ONE coherent culture, never a pan-Asian/pan-European blend |
| Social class | object age, mend marks, brands, spatial density — poor homes are NOT spotless; rich homes are NOT showrooms |

**Six ready kits:**

- **1970s family home**: `wood-veneer paneling, heavy floral curtains, a glass ashtray on the coffee table, a coiled telephone cord, warm tungsten bulbs, patterned wallpaper yellowed near the kitchen`
- **1990s office**: `beige CRT monitors, a fax machine mid-print, venetian blinds, stacked plastic document trays, floppy disks, a whiteboard ghosted with half-erased marker`
- **Postwar household**: `visibly mended furniture, nothing matching, food tins reused as containers, water-stained walls, folded newspaper wedged under a table leg`
- **New-money mansion**: `acres of polished marble, a double-height foyer, artworks with auction labels still attached, and no trace of anyone actually living there`
- **Old-money estate**: `furniture old but perfectly proportioned, silver with decades of polish-wear, books with cracked spines and pencil marginalia`
- **Renter's room**: `makeshift wire-rack storage, one cheap clip-on lamp, flattened moving boxes behind the door, damage-free adhesive hooks and their peeled ghost-marks on the wall`

---

## 4. Anachronism Watchlist

Image models default to *modern*. For any period scene, positively describe the era-correct version of each item below — silence invites a modern intruder into frame:

| Risk item | Positive phrasing fix |
|---|---|
| Windows & frames | `period-correct wooden sash windows` (not modern aluminum sliders) |
| Outlets & switches | `a round bakelite light switch`, `cloth-wrapped wiring on porcelain insulators` |
| Screens & lighting | `a small CRT set`, `bare tungsten bulb under an enamel shade` (no LCD panels, no LED strips before ~2010) |
| Packaging & print | `hand-painted shop signage`, `newspapers in period letterpress type` (no barcodes pre-1980s, no QR codes pre-2010s) |
| Phones | `rotary dial`, `wall-mounted payphone`, `a brick-sized early mobile` by decade |
| Vehicles & plates | name the decade's car body shapes if a window view includes streets |
| Surveillance | CCTV cameras only in contemporary/authority settings — and only deliberately |

---

## 5. Camera-Aware Composition Vocabulary

A set is built to be cut, compressed, blocked, and revealed by a lens. Choose the vocabulary per distance:

| Shot need | What the prompt must specify | Example phrasing |
|---|---|---|
| Wide establishing | three depth layers | `in the foreground a doorframe in shadow, midground the dining table under lamplight, background a rain-streaked window over city neon` |
| Long-lens feel | compressed background, controlled pattern | `telephoto compression stacking the corridor doorways`, `a calm, uncluttered backdrop with no stray lines crossing head height` |
| Close-up | precise micro-subjects | `a desktop scarred with cup rings and knife marks, fingerprints on the brass lamp, a lipstick stain on the rim of a cold coffee` |
| Low angle | ceiling must exist | `exposed joists and a bare bulb overhead`, `a coffered ceiling pressing down in perspective` |
| Overhead / top-down | floor as composition | `a worn Persian rug, scattered case files and photographs arranged across the floorboards` |
| Frame-in-frame | oppression / voyeurism | `seen through the kitchen doorway`, `framed between shelving units`, `watched through the gap in a hospital curtain` |
| Foreground occlusion | layered depth | `shot past an out-of-focus potted palm`, `through rain-beaded glass`, `past a beaded curtain` |

**Composition hygiene**: keep horizon, wall, and window lines off the subject's neck and head; the background must support the story, never become an exhibition; leave breathing room where a character would stand and move.

---

## 6. Light × Material Interplay

Materials are exposure decisions. Name at least two materials per prompt and state how the light hits them.

| Material | On-camera behavior | Prompt phrasing |
|---|---|---|
| Polished metal | harsh hotspots | `softly aged brushed steel catching a dull gleam` |
| Glass | transmits AND reflects | `the window doubling the room as a faint reflection over the neon outside` |
| Dark wood | absorbs light, reads rich | `edge light raking across walnut paneling, pulling out the grain` |
| White walls | flat, bounces everywhere | `off-white walls with faint water stains and a warm color cast, never a flat studio white` |
| Fabric | absorbs, softens | `heavy velvet drapes swallowing the lamplight`, `sun-faded cotton curtains breathing at an open window` |
| Plastic | hard cheap sheen | `glossy molded-plastic chairs under flat fluorescent light` — convenience stores, clinics, low-rent rooms |
| Stone / marble | cold, hard, power | `veined marble reflecting cold daylight` — overuse reads "hotel lobby", ration it |
| Concrete | rough, oppressive, modern | `raw concrete with damp patches and hairline cracks`, never a dead flat gray |

**Lighting principles:**

- **Motivated practicals only** — every light exists in the world: `a green-shaded banker's lamp`, `the blue flicker of a television`, `the cold spill of an open refrigerator`, `buzzing neon signage bleeding through the blinds`, `passing headlights sweeping the ceiling`.
- **Windows are the light's narrative**: `first gray light of dawn`, `low amber sunset`, `pulsing red-and-blue police strobe`, `a single lightning flash freezing the room`.
- **Temperature = psychology**: warm tungsten → intimacy, nostalgia, or decay; cold fluorescent/daylight → clinical, isolation, technology, judgment.
- **Age in layers**, never a uniform dirt pass: `dust on the upper shelves, grease shadowing the stove wall, worn varnish on the chair arms, sun-faded curtains, one mended crack in the window`.
- **Genre surfaces**: horror → `wet-sheen surfaces, things that glisten`; comedy → `clean saturated color blocks, even light`; crime → `desaturated palette, rough matte surfaces`.

---

## 7. Props as Silent Dialogue

Props are the character's unspoken lines — a viewer should read the person in one second. Kits by archetype:

| Archetype | Prop kit |
|---|---|
| Controlling mother | `label-maker tags on every jar, plastic slipcovers on the good furniture, a perfectly aligned dinner service, a seven-day pill organizer, a baby monitor still running in an older child's room` |
| Failed writer | `empty bottles by the desk, a drawer of rejection letters, an old typewriter under sticky notes, a forest of unwashed mugs` |
| Mob boss | `a religious icon above the desk, framed family photos facing the visitor, a cigar humidor, thick drawn curtains, a desk heavy enough to stop bullets` |
| Tech nouveau riche | `minimalist furniture, a smart speaker on every surface, wireless chargers, an expensive space with no memory in it` |
| Old professor | `dog-eared pages, handwritten index cards, a decades-old desk lamp, tea stains ringed into the blotter, strata of stacked papers` |
| Elderly living alone | `pharmacy bags on the counter, a calendar years out of date, plastic flowers, furniture mended with tape, a remote control wrapped in rubber bands` |
| Teenager | `band posters, a tower of sneaker boxes, headphones on the bed, homework abandoned mid-page, one drawer that is clearly private` |
| Fugitive | `bundled cash, spread maps, a fan of forged documents, burner phones still in blister packs, blackout curtains taped at the edges` |

---

## 8. Life-Trace Checklists by Room

The audience never inspects each prop, but they *feel* whether a space has been lived in. Pull ≥3 traces per prompt; every object must have a usage logic.

- **Kitchen**: grease shadow behind the stove · fridge magnets pinning old receipts · expired jars at the back · knives worn to the owner's grip · one favorite cup by the sink
- **Bathroom**: limescale at the tap base · the number of toothbrushes (count = story) · medicine behind the mirror · a damp towel over the rail · fog ghosting the mirror's edge
- **Bedroom**: which side of the bed is slept on · a charging cable snaking to the pillow · a half-read book face-down · a chair buried under worn-once clothes · one private object placed with care
- **Desk**: filed vs drifting papers · coffee rings layered like tree rings · pen impressions in the blotter · sticky notes climbing the monitor bezel
- **Entryway**: how the shoes are ordered (or aren't) · a key dish · a dripping umbrella · unopened mail · coats layered by season
- **Car interior**: parking stubs in the door pocket · a child seat with cracker crumbs · stale cigarette smell told through an overfull ashtray · a charm swinging from the mirror · fast-food bags balled on the passenger floor

---

## 9. Theory → Mood Vocabulary

| Theory / aesthetic | Core idea | Prompt application |
|---|---|---|
| Aristotelian structure | space serves plot movement | let the set track act structure: `open and airy` → `tightening` → `disordered` → `emptied out` |
| Stanislavski | given circumstances, psychological truth | the room must convince us someone truly lives here — habits visible everywhere |
| Brecht | alienation, make the audience think | `deliberately exposed stage rigging, painted flat backdrops, visible slogans` — knowingly theatrical |
| Naturalism | social conditions shape people | class, occupation, family system carried entirely by material detail |
| Expressionism | space externalizes the psyche | `walls leaning at uneasy angles, doorways stretched tall and narrow, shadows grown monstrous` |
| Symbolism | objects as metaphor | `withered flowers, a cracked mirror, an empty birdcage, a room upholstered entirely in red, a window that does not open` |
| Semiotics | every object is a readable sign | brand, color, placement, material chosen as a sentence the audience reads unconsciously |
| Mise-en-scène | people, objects, light, lens in relation | `the patriarch framed at the head of the table`, `her chair angled toward the exit`, `a figure boxed in by doorframes` |
| Spatial power theory | space distributes hierarchy | `a raised platform office`, `glass-walled cubicles under an overseer's window`, `a surveillance-camera viewpoint` |
| Film noir | moral murk and shadow | `venetian-blind shadows slicing the desk, wet asphalt mirroring neon, smoke hanging in a low-ceilinged room` |

**Three-sentence test** before finalizing any design: Does the space reveal what the character cannot say aloud? Does it give the director and camera layered depth to stage in? Does it make the audience feel the emotion before they understand the plot?

---

## 10. Final Quality Checklist

Run every trio against all ten. Fix, don't rationalize:

1. Era, region, class, and culture all correct and coherent?
2. Life traces present — lived-in, not an art-department display?
3. Depth layers stated — foreground, midground, background?
4. Works at all three distances — wide, mid, close?
5. Zero anachronisms — windows, outlets, screens, type, packaging, plates, cameras?
6. Every prop has a reason to be there?
7. Materials stay credible under the named light?
8. Space implies relationship, power, and psychology?
9. Light is motivated — every source exists in the world?
10. The audience wouldn't *notice* the set, yet would be *changed* by it?

The essence of set design: make the invisible visible — memory, class, desire, trauma, order, collapse. A mature set is not a backdrop; it is part of the drama.

---

## 11. Worked Example

**Request**: 「1990年代台北，一個失意私家偵探租的公寓，犯罪片氛圍」

**Design Bible (internal)**: 1990s Taipei walk-up · renter class, ex-cop pride decaying · palette: nicotine amber vs neon cyan · light: one banker's lamp + neon through blinds · hero props: case-file wall, overfull ashtray, rotary phone · subtext: a man who stopped believing but can't stop working · crime-genre desaturated rough surfaces.

**提案一（Establishing Wide）**:

```text
A wide establishing shot of a cramped 1990s Taipei walk-up apartment rented by a washed-up private detective, cinematic crime-drama photography. In the foreground, a doorframe in deep shadow; midground, a sagging faux-leather sofa and a cluttered desk under the green glow of a banker's lamp; background, a rain-streaked sash window where cyan neon signage from the street below bleeds through half-broken venetian blinds, striping the room. Nicotine-stained off-white walls with faint water marks, worn terrazzo flooring, a rotary-dial telephone with a hopelessly tangled cord, stacks of manila case files leaning against the wall, and flattened moving boxes never thrown away. The warm tungsten pool of the desk lamp fights the cold neon from outside, raking across the desk's scarred dark wood veneer. Desaturated palette, rough matte surfaces, heavy atmosphere of stalled ambition, period-correct 1990s Taiwan details throughout, photorealistic, 35mm cinematic film still.
```

The mid-shot proposal would move to the desk and sofa relationship (files as silent dialogue, one visitor's chair that never gets used); the close-up would resolve the ashtray, cup rings, and a single photograph pinned among the case files under the lamp's edge light — same palette, same two light sources, same era anchors, repeated verbatim.
