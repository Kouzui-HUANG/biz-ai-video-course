# Prompt Template — Clean ArchViz Blocking Plan

## Contents
1. Assembly
2. Fixed blocks (A) (B) (D)
3. Paragraph (C) slot grammar
4. Figure phrases
5. Variants: aspect ratio · exteriors · label language
6. Worked example (salon, no actor image → mannequin)

---

## 1. Assembly
One `text` code block with four labeled paragraphs — (A) camera, (B) render style, (C) space + blocking, (D) light + background + legend — ending with `--ar {ratio}`. (A)(B)(D) stay near-verbatim; (C) carries the scene.

Direction words in (C): **up** = toward the top edge (far side), **down** = toward the bottom edge (camera side), **left/right** as in the plan. Refer to the actor as "the figure" or "the actor", never by a gendered pronoun.

---

## 2. Fixed Blocks

**(A)**
```text
(A) A perfectly orthographic top-down plan view, shot from directly overhead at exactly 90 degrees — parallel projection, zero perspective convergence, no tilt — with the whole {room} centered in a {16:9 landscape} frame, a clean margin on the {right} for a small legend, and everything tack-sharp edge to edge with no depth-of-field blur.
```

**(B)** — interior (exteriors: §5)
```text
(B) Photorealistic high-end architectural visualization 3D floor plan, Unreal Engine 5 / V-Ray path-traced quality: ceiling removed, walls shown as clean solid cut sections, physically accurate materials, soft ambient occlusion and contact shadows, subtle reflections in {the glossiest surface} — topped with a crisp, flat vector annotation layer in the style of a professional film blocking diagram.
```

**(D)** — fill the light slot from the photo: source, direction in plan terms, quality (soft overcast / hard sun with window-shaped patches / night practicals), temperature, practical lamps as warm pools.
```text
(D) {Light from the reference photo}; neutral, true-to-life color with {2–3 signature objects} as clear accents; calm, precise, premium real-estate-render clarity. The cutaway {room} floats on a plain light warm-grey background with a soft drop shadow. A small clean legend card in the {right} margin: red dashed line = "ACTOR", blue solid line = "CAMERA". No other text, no ceiling, no extra furniture, {no other figures | no other people}. --ar {ratio}
```
Use "no other figures" with a mannequin and "no other people" with a real actor.

---

## 3. Paragraph (C) Slot Grammar

**Layout** — follow the inventory order in `blocking-knowledge-base.md` §1.4:
```text
(C) A faithful plan-view reconstruction of the {space} in the reference photo: a {shape} about {W} m wide and {D} m deep, oriented exactly like the photo — {reference-camera side} at the bottom edge, {far side} along the top, {left side} on the left, {right side} on the right. {Floor as seen from above}. {Top edge}. Left wall, bottom to top: {…}. Right wall, bottom to top: {…}. {Free-standing pieces anchored to fixed ones}. {Floor props / hooks}. {Overhead fixtures as thin grey dashed outlines}; the {near zone} is open, empty floor.
```

**Actor**
```text
ACTOR: a bold crimson dashed line with arrowheads through {n} numbered red circles. 1 {where}, where {FIGURE} {pose}; the line {curves / bends / cuts} {direction} to 2 {where}; … to {n} {where}, where {final action}.
```

**Camera**
```text
CAMERA: a solid electric-blue line with arrowheads linking {m} blue camera icons, each with a short translucent blue field-of-view wedge. C1 {at the reference-camera position}, its wedge opening {into the space} (the reference-photo framing); a {straight / smooth / curved} segment labeled "{MOVE}" {verb} to C2 {where}; …; ending at C{m} {where}, its wedge aimed at {target}.
```
Label only the moves (at most 4); marks and C-numbers need no extra words. Label format per `blocking-knowledge-base.md` §3.

---

## 4. Figure Phrases (the FIGURE slot)

| Actor source | Phrase |
|---|---|
| Actor image supplied | a small photoreal figure of the actor from the attached actor reference, seen from directly above ({hair color & style}, {outfit color & silhouette}, {footwear}) |
| Actor visible in the scene image | a small photoreal figure of the person from the reference photo, seen from directly above ({same three features}) |
| No actor image | a small matte white clay mannequin seen from directly above — a {slender female-proportioned / broad male-proportioned / child-sized} artist's figure with no face, hair or clothing detail |

Only features legible from above count: hair, shoulders, outfit color and silhouette, hats, bags, footwear. Skip faces. With no hint of body type, drop the proportion words.

---

## 5. Variants

**Aspect ratio** (plan depth ÷ width):
| D ÷ W | Ratio | Legend margin |
|---|---|---|
| 0.5–1.3 (most rooms) | 16:9 landscape | right |
| 1.3–2.0 | 3:4 portrait | bottom |
| > 2.0 (corridors) | 9:16 portrait | bottom |
| < 0.5 (very wide spaces) | 21:9 landscape | right |

**Exteriors** — replace (B) with:
```text
(B) Photorealistic high-end architectural visualization 3D site plan, Unreal Engine 5 / V-Ray path-traced quality: the site cut out as a clean rectangular diorama block with neatly sectioned ground edges, building roofs removed and walls shown as cut sections, tree canopies rendered semi-transparent so the paths beneath stay visible, physically accurate materials, soft ambient occlusion and contact shadows — topped with a crisp, flat vector annotation layer in the style of a professional film blocking diagram.
```
In (D), "cutaway room" → "cutaway site block", and "no extra furniture" → "no extra buildings or vehicles".

**Label language** — default short English caps. If the user asks for Chinese labels, quote them in the prompt, keep each ≤ 4 characters, and warn in 使用建議 that CJK labels garble more often.

---

## 6. Worked Example (calibration only — never reuse its content)

Input: one photo of a Parisian Haussmann salon shot from the open double doorway; no actor image.

**設計假設：** 只有場景圖、沒有演員圖，所以用白模假人（地上的高跟鞋暗示女性，採纖細女性比例）｜動作由我設計：進門、佇窗、落座｜總長 15 秒｜16:9

| 時間 | 演員 | 攝影機 | 動作與運鏡 |
|---|---|---|---|
| 0–3s | Mark1 | C1→C2 | 首幀＝原圖；假人從鏡頭旁進門；DOLLY IN 穿過門口 |
| 3–7s | Mark2 | C2→C3 | 經過紅絲絨椅；STEADICAM FOLLOW 在身後約 2 m 跟拍 |
| 7–10s | Mark3 | C3 | 停在中央落地窗前望向窗外；HOLD，拍逆光背影 |
| 10–15s | Mark4 | C3→C4 | 斜走到鋼琴，撿起高跟鞋坐下；ARC 90° 收在側臉 |

```text
(A) A perfectly orthographic top-down plan view, shot from directly overhead at exactly 90 degrees — parallel projection, zero perspective convergence, no tilt — with the whole room centered in a 16:9 landscape frame, a clean margin on the right for a small legend, and everything tack-sharp edge to edge with no depth-of-field blur.

(B) Photorealistic high-end architectural visualization 3D floor plan, Unreal Engine 5 / V-Ray path-traced quality: ceiling removed, walls shown as clean solid cut sections, physically accurate materials, soft ambient occlusion and contact shadows, subtle reflections in the polished stone — topped with a crisp, flat vector annotation layer in the style of a professional film blocking diagram.

(C) A faithful plan-view reconstruction of the Parisian Haussmann salon in the reference photo: a rectangular room about 6 m wide and 7 m deep, oriented exactly like the photo — open double entrance doors (dark, distressed paint) centered on the bottom edge, the window wall along the top, the fireplace wall on the left, the piano wall on the right. Polished black-and-white marble checkerboard floor laid on the diagonal, reading as a harlequin diamond pattern from above. Top wall: three tall arched black-framed French doors, the middle one wider, each opening onto a shallow wrought-iron Juliet balcony, sheer ivory curtains gathered beside each on one long black iron rod. Left wall, bottom to top: a carved white marble Louis XV fireplace at mid-wall with a black hearth, brass andirons and a vase of deep red roses on the mantel; a white plaster bust on a dark wood pedestal; a tall dark side door; a kentia palm in a blue-and-white porcelain planter in the top-left corner. Between the fireplace and the palm, about a meter into the room: a red velvet tufted slipper chair with a fringed skirt, angled toward the room center, beside a small round dark wood side table. Right wall, bottom to top: a glossy black upright piano with open sheet music and a black tufted leather bench on its room side; a wooden console bar with crystal decanters and dried branches near the top-right corner. On the floor just below the bench, toward the entrance: a pair of black ankle-strap heels, one tipped over. A thin grey dashed circle at the center marks the chandelier overhead; the lower third near the doors is open, empty floor.
ACTOR: a bold crimson dashed line with arrowheads through four numbered red circles. 1 just inside the doorway, where a small matte white clay mannequin seen from directly above — a slender female-proportioned artist's figure with no face, hair or clothing detail — is stepping into the room; the line curves up and to the left to 2 beside the red velvet chair; bends up and to the right to 3 in front of the central French door, where the figure stops to look out; then cuts diagonally down and to the right to 4 at the piano bench, where the figure picks up the heels and sits facing the piano.
CAMERA: a solid electric-blue line with arrowheads linking four blue camera icons, each with a short translucent blue field-of-view wedge. C1 stands in the open doorway between the two door leaves on the room's center axis, its wedge opening up into the room (the reference-photo framing); a straight segment labeled "DOLLY IN" pushes through the doorway to C2 just inside the room; a smooth curve labeled "STEADICAM FOLLOW" trails about two meters behind the figure to C3 at the center of the room, its wedge aimed at the central window; a final curve labeled "ARC 90°" swings right toward the piano and wraps a quarter-circle around the bench, ending at C4 on the bench's entrance side, just beyond the heels, its wedge aimed up at the figure's seated profile.

(D) Soft overcast winter daylight enters through the three French doors, brightest along the window wall and fading gently toward the entrance, with faint warm pools from brass wall sconces near the side walls; neutral, true-to-life color with the red chair, red roses and black piano as clear accents; calm, precise, premium real-estate-render clarity. The cutaway room floats on a plain light warm-grey background with a soft drop shadow. A small clean legend card in the right margin: red dashed line = "ACTOR", blue solid line = "CAMERA". No other text, no ceiling, no extra furniture, no other figures. --ar 16:9
```

With an actor image, only the FIGURE phrase changes (§4) and the exclusion becomes "no other people".
