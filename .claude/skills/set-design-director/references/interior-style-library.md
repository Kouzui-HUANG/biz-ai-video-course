# Interior Style Library — Prompt-Crafting Edition

Interior-design color, material, and style vocabulary re-tooled as English phrase inventory for natural-language image models. Use for style-driven space requests (a named style, a residential/commercial interior); combine with the narrative knowledge base when the space also serves a story.

## Table of Contents

1. [Color & Material Foundations](#1-color--material-foundations)
2. [Style Master Table — 20 styles](#2-style-master-table)
3. [Style Execution Notes](#3-style-execution-notes)
4. [Material Vocabulary](#4-material-vocabulary)
5. [Style-Fusion Formulas](#5-style-fusion-formulas)
6. [Discipline Rules](#6-discipline-rules)
7. [Style-Driven Design Flow](#7-style-driven-design-flow)

---

## 1. Color & Material Foundations

**The 60-30-10 hierarchy** — color is structure, not decoration. State colors in prompts at their correct tier:

| Tier | Carries it | Share |
|---|---|---|
| Dominant | walls, floor, ceiling, large cabinetry | ~60% |
| Secondary | sofa, curtains, rug, wood veneer, stone surfaces | ~30% |
| Accent | cushions, art, vases, an accent chair, lamps | ~10% |

Prompt pattern: `dominant warm off-white walls and pale oak flooring, a secondary layer of sage-green sofa and oatmeal linen curtains, accented only by terracotta cushions and one brass floor lamp`.

**Material = the body-feel of a room** — wood gives warmth, stone gives weight, metal gives edge, glass gives transparency, fabric gives softness, leather gives maturity, concrete gives rawness. A material's color, grain, and surface finish (matte / honed / polished) set the mood as much as paint.

**Style = controlled consistency, not a label** — a mature space keeps ONE logic across: line language, light color-temperature, metal finish, wood tone, furniture scale. Repeat these anchors in every prompt of a trio.

---

## 2. Style Master Table

| Style | Palette | Materials & finishes | Furniture silhouette | Decor vocabulary |
|---|---|---|---|---|
| Modern | white, gray, black, beige, wood tones | glass, metal, wood veneer, stone | straight lines, low ornament, strong proportions | abstract art, sleek fixtures, geometric objects |
| Minimal | white, light gray, off-white, matte black | matte paint, micro-cement, seamless surfaces, pale wood | thin, low, flush, concealed storage | one sculpture, a monochrome vase, deliberate negative space |
| Scandinavian | white, pale wood, gray, dusty blue, sage green | light oak, cotton-linen, wool, rattan | rounded corners, slim tapered legs, lightweight | potted greenery, layered textiles, ceramics, simply framed prints |
| Japanese | off-white, natural wood, ink black, earth tones | solid timber, washi paper, bamboo, tatami, clay | low-slung, horizontal emphasis, austere | paper lanterns, a dry branch arrangement, pottery, shoji screens |
| Wabi-sabi | gray-brown, earth, charcoal, misty beige | mottled lime plaster, coarse pottery, aged wood, stone | imperfect, handmade, understated | rough clay vessels, dried plants, crumpled linen |
| Japandi | off-white, greige, pale wood, sparse black accents | wood, paper, rattan, cotton-linen, matte finishes | Scandinavian roundness at Japanese height — low and soft | paper lamps, ceramics, low-saturation textiles |
| Industrial | black, gray, rust red, dark wood | raw concrete, blackened steel, exposed brick, leather | rugged, exposed structure, metal-framed | track lighting, a vintage wall clock, wire mesh, salvaged pieces |
| American | beige, cream white, navy, walnut | painted millwork & wainscoting, fabric sofas, leather, a fireplace | substantial, comfortable, symmetrical | table lamps, framed family photos, cushions, a large area rug |
| Country | cream, sage green, light blue, wood tones | distressed wood, brick, cotton-linen, floral fabric | warm, rounded, handcrafted feel | fresh flowers, gingham checks, stoneware crocks, wooden crates |
| French | ivory, milk-tea beige, gold, gray-blue | wall paneling (boiserie), stone, brass, velvet | curved, carved, elegant proportions | a crystal chandelier, ornate mirror frames, candlesticks, antiques |
| Neoclassical | white, beige, gray, gold, deep blue | marble, panel molding, metal, leather | symmetrical, upright, precise proportions | wall sconces, sculpture busts, framed paintings, mirrors |
| Art Deco | black, gold, emerald green, burgundy | mirror, polished brass, marble, velvet | geometric, radiating, opulent | fan motifs, arched forms, inlaid metal trim |
| Mid-century | caramel, olive green, mustard yellow, walnut | wood, leather, rattan, metal | splayed tapered legs, low-slung, streamlined | retro lamps, geometric rugs, a starburst wall clock |
| Boho | earthy orange, beige, brown, peacock blue, wine red | rattan, cotton-linen, fringe, woven fiber | eclectic mix, low seating, free-form | macramé wall hangings, abundant plants, ethnic patterns, layered floor mats |
| Mediterranean | white, sea blue, terracotta, olive green | lime-plaster walls, terracotta tile, timber beams, wrought iron | thick-walled, arched openings, natural | clay pots, mosaic accents, linen curtains |
| Moroccan | indigo, ochre red, gold, green, white | zellige mosaic, carved wood, pierced metal, leather | low seating, carved detail, intricate pattern | pierced-brass lanterns, geometric tile, hammered metal trays |
| Luxury | black, white, gold, gray, deep brown | book-matched marble, metal, leather, mirror | grand scale, symmetry, visual weight | statement chandeliers, sculpture, curated objets d'art |
| Hotel style | greige, dark wood, champagne gold, warm white | honed stone, wood veneer, leather, layered textiles | tailored, comfortable, timeless | wall sconces, an upholstered headboard, area rugs, styled trays |
| Oriental Modern | ink black, off-white, dark wood, a restrained touch of vermilion | wood lattice, stone, paper, ceramic, metal | rectilinear, generous negative space, screen-like layering | calligraphy, ceramics, ink-landscape art, lanterns |
| Taiwanese retro (台式老宅) | terrazzo gray, deep green, wood tones, iron-window blue | terrazzo, patterned cement tile, iron window grilles, aged wood | vintage cabinets, rattan chairs, heavy wooden tables | pressed-pattern glass, old pendant lamps, retro majolica tiles |

---

## 3. Style Execution Notes

One-line pro corrections that keep each style from failing in render:

- **Modern**: never only white-gray-black (reads as an empty flat) — add wood tones, fabric, one stone surface for warmth.
- **Minimal**: minimal = low visual noise, not few objects — low-saturation color, fine seams, concealed storage; always specify light quality and proportion or it turns cold and vacant.
- **Scandinavian**: not just "white walls + wood floor" — the rug, plants, table lamp, and framed prints are what complete it; keep it lived-in.
- **Japanese**: restraint, horizontal lines, honest materials; never stack "wafu" clichés — control negative space, light, and material truth instead.
- **Wabi-sabi**: curated plainness, not shabbiness — every rough texture needs quiet negative space beside it.
- **Japandi**: unify all wood into one tone family; black appears only as sparse accents, or soft turns heavy.
- **Industrial**: residential industrial must be softened — leather, a rug, warm lamplight, and wood against the concrete and steel.
- **American**: the premium feel comes from proportion and layering, never from oversized furniture alone.
- **French**: guard against over-sweetness — matte finishes, one modern piece, or darker wood matures the room.
- **Neoclassical**: panel molding must be proportioned to the wall; excess gold reads gaudy.
- **Art Deco**: strongest as a zoned statement (foyer, dining, bar wall, master suite), not wall-to-wall.
- **Mid-century**: the soul is furniture silhouette — without iconic shapes, palette alone cannot carry it.
- **Boho**: needs a restrained base — keep walls, floor, and ceiling off-white or earthen so the patterns read as rich, not chaotic.
- **Mediterranean**: extract plaster texture, an arch, terracotta tones — never the full blue-white theme-restaurant kit.
- **Hotel style**: the key is layered lighting — ambient, indirect cove, reading, and accent lights as separate named layers.

---

## 4. Material Vocabulary

| Material | Character | Fits styles | Caution |
|---|---|---|---|
| Light oak | fresh, natural | Scandinavian, Japandi, Japanese | avoid overly yellow light on it |
| Walnut | mature, grounded | American, Mid-century, Hotel | too much overwhelms small rooms |
| Marble | luxurious, cool | Neoclassical, Luxury, Hotel | control the veining — never busy |
| Travertine | soft natural luxury | Wabi-sabi, Modern, Mediterranean | porous — show honed, not glossy |
| Concrete / micro-cement | raw, calm | Minimal, Industrial, Wabi-sabi | must be balanced by warm materials |
| Brass | vintage refinement | Art Deco, French, Neoclassical | small doses read premium; large doses read brash |
| Blackened steel | crisp, hard-edged | Industrial, Modern, Oriental Modern | keep the room from going all-dark |
| Rattan | light, resort-like | Scandinavian, Boho, Japanese | an accent, never the whole room |
| Velvet | opulent, soft | French, Art Deco, Luxury | deep tones only — pale velvet reads cheap |
| Linen | plain, natural | Wabi-sabi, Japanese, Scandinavian | wrinkles easily — write the wrinkles as the charm |

---

## 5. Style-Fusion Formulas

| Fusion | Working formula |
|---|---|
| Modern + Japanese | `white walls, wood lattice screens, low furniture, fine black detailing` |
| Scandinavian + Japanese | `pale wood, off-white, rounded furniture, paper lamps` |
| Industrial + Modern | `micro-cement, blackened steel, leather, clean uncluttered lines` |
| American + Modern | `painted wall molding, a deep comfortable sofa, clean flat-front cabinetry` |
| French + Modern | `a paneled boiserie backdrop, modern furniture, restrained brass` |
| Wabi-sabi + Hotel | `rough plaster walls, warm layered lighting, immaculate refined bedding` |
| Art Deco + Modern | `geometric lines, brass accents, one deep-toned statement chair, a quiet background` |

Rule: one MAIN style, at most two supporting styles — the main style owns the dominant color tier and the furniture silhouette.

---

## 6. Discipline Rules

Convert the classic interior mistakes into hard prompt rules:

1. **Design the whole frame, not a hero object** — a beautiful chair is not a beautiful room; every prompt states the full 60-30-10 hierarchy.
2. **3–5 primary materials maximum** — name them, then stop adding.
3. **One wood-tone family per room** — pale, yellow, red, and dark woods mixed casually read cheap.
4. **One dominant metal finish** — any second metal is a deliberate minor accent.
5. **Light temperature must match the style** — warm styles (wabi-sabi, country, American, boho, hotel) take warm 2700–3000K tungsten-toned light; cool styles (minimal, industrial, modern) tolerate neutral white. Cold-white light in a warm style destroys the room — always name the light temperature.
6. **No symbol-stacking** — Japanese ≠ noren curtains everywhere; French ≠ glued-on molding; industrial ≠ exposed pipes alone. Build the style from palette + material + silhouette consistency.

---

## 7. Style-Driven Design Flow

When the request is style-driven (an interior, not a drama scene), build the Design Bible in this order — it mirrors how professionals decide:

1. **Lifestyle** — how does the occupant eat, rest, store, work? (becomes the life traces)
2. **Emotional need** — calm, opulent, warm, crisp, or storied?
3. **Main style** — one main, ≤2 supporting (see §5 fusions)
4. **Color board** — dominant / secondary / accent per 60-30-10 (§1)
5. **Material board** — 3–5 materials from §4, one wood tone, one metal
6. **Furniture silhouette** — the style's line language from §2
7. **Decor last** — art, lamps, rugs, cushions, vases from the style's decor vocabulary

**Mini Style Bible example (Japandi living room)**: main style Japandi · dominant warm off-white walls + pale oak floor · secondary greige linen sofa + rattan lounge chair · accent sparse matte-black metal + one dark ceramic vase · materials: pale oak, cotton-linen, paper, rattan, matte ceramic · light: 2700K paper floor lamp + soft daylight through sheer curtains · silhouette: low, rounded, floating.
