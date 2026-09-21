# Blocking Knowledge Base

## Contents
1. Spatial reconstruction (photo → plan)
2. Actor blocking design
3. Camera vocabulary & plan notation
4. Beat timing
5. Special cases

---

## 1. Spatial Reconstruction (photo → plan)

### 1.1 Orientation
- Reference camera → **bottom edge**. The wall or boundary most parallel to the image plane → **top**. Left/right stay as in the photo. Never mirror.
- Two-point (corner) views: keep walls axis-aligned; put C1 near the bottom corner on the camera's side, aimed diagonally at the corner it faces.
- Lens height = the horizon line: objects whose tops touch the horizon are at camera height.
- Lens: estimate from how fast floor lines converge (strong convergence ≈ 18–24 mm, moderate ≈ 35 mm, flat ≈ 50 mm+). The lens goes in the table, not on the image.

### 1.2 Scale cues (estimate W × D to the nearest 0.5 m)
| Cue | Typical size |
|---|---|
| Door leaf | 2.0–2.1 m tall, 0.8–0.9 m wide |
| Ceiling | 2.4–2.8 m modern; 3.0–3.6 m classical / Haussmann / loft |
| Kitchen counter · dining table | 0.9 m high · 0.75 m high, 0.8–1.0 m deep |
| Chair seat · sofa | 0.45 m high · 2.0–2.4 m long |
| Bed · upright piano · grand piano | 2.0 m long · 1.5 m wide · 1.5–2.7 m long |
| Floor tiles | 30 / 45 / 60 cm — count tiles to measure distance |
| Adult · car | 1.6–1.8 m · 4.5 m long |
| Sidewalk · traffic lane | 1.5–3 m · 3–3.5 m wide |

### 1.3 Depth order from one image
- On the floor, a contact point lower in the frame is nearer the camera.
- Along a side wall, objects closer to the image center are farther away.
- Tile joints, rugs, and floorboards give the grid; count units to place objects.

### 1.4 Inventory order (mirrors paragraph C)
Shape, size, orientation → floor/ground material and pattern as seen from above → top edge → left side, bottom to top → right side, bottom to top → free-standing pieces anchored to fixed ones ("between the fireplace and the palm, about a meter into the room") → floor props / narrative hooks → overhead fixtures → unseen zone.

### 1.5 What a 90° plan can and cannot show
- Invisible from straight above: wall-mounted art, mirrors, sconces, curtain faces. Mention them only if the blocking uses them, as a thin line on the wall.
- Overhead items (chandeliers, pendants, fans, beams): thin grey dashed outlines.
- Balconies, window sills, and door swings read well; describe them.
- Exteriors: tree canopies and awnings semi-transparent so paths beneath stay visible.

### 1.6 Narrative hooks
Props that imply action or history: shoes left behind, an open letter, an instrument, a mirror, a window view, an unmade bed, a half-drunk glass, a door left ajar. List 2–4; they become marks.

### 1.7 Unseen zone
The area near the lens outside the frame edges is unknown. Describe it as open, empty floor. Never furnish it unless the user describes it.

### 1.8 Photo artifacts
- Reflections in mirrors, glass backsplashes, windows, or glossy floors show space behind the camera or beyond the wall. Never place reflected objects in the plan; the unseen zone stays empty unless the user confirms what is there.
- Ignore watermarks, logos, captions, and UI overlays on the photo.

---

## 2. Actor Blocking Design

### 2.1 User-specified action
Map each described action to a mark, in order; keep the user's verbs. Fill only the gaps: exact positions, path shape, timing.

### 2.2 Designing from scratch
Default arc: **ENTER → APPROACH a hook → PAUSE at a light or view source → LAND at the strongest hook** (sit, kneel, touch, pick up).
- 3–5 marks. The first mark carries the figure.
- Start off-frame or at the frame edge so the scene image stays the first frame.
- Readable path shape: S-curve, Z, or L; never self-crossing; always through open floor.
- Anchor every mark to a fixed landmark ("beside the red chair", "in front of the central window").
- If the scene shows an actor, their visible spot is Mark 1 or the key mark.

### 2.3 Notation
- Walk: crimson dashed line with arrowheads. Marks: numbered red circles.
- Turn: small curved arrow at the mark. Exit: the arrow runs off the plan through a door or edge.
- Poses (sit, kneel, lie) are described in words at that mark; only the figure's mark shows a pose.

---

## 3. Camera Vocabulary & Plan Notation

| Move | Label | Draw it as |
|---|---|---|
| Static / hold | HOLD | icon only, no outgoing segment |
| Pan | PAN LEFT / PAN RIGHT | icon + small curved rotation arrow + two wedges (start faint, end solid) |
| Tilt | TILT UP / TILT DOWN | label at the icon (vertical move, invisible in plan) |
| Dolly in / push in | DOLLY IN | straight segment along the lens axis toward the subject |
| Pull back | PULL BACK | straight segment backward along the lens axis |
| Truck | TRUCK LEFT / TRUCK RIGHT | straight sideways segment; wedges stay parallel |
| Tracking on rails | TRACKING | segment parallel to the actor path with thin rail ticks |
| Steadicam / gimbal follow | STEADICAM FOLLOW | smooth curve trailing 1.5–3 m behind the actor |
| Handheld | HANDHELD | slightly wavy line |
| Arc / orbit | ARC 90° / ORBIT 360° | circular segment around the subject, angle in the label |
| Crane / jib | CRANE UP / CRANE DOWN | label + small vertical arrow at the icon |
| Zoom | ZOOM IN / ZOOM OUT | no path; nested wide and narrow wedges |
| Dolly zoom | DOLLY ZOOM | straight segment + label |
| Whip pan | WHIP PAN | icon + sharp curved arrow |
| Drone | DRONE | dotted path + label |

Camera rules:
- C1 = reference camera. 3–5 positions; at most 4 labeled moves.
- Escalate: approach (DOLLY IN) → accompany (STEADICAM FOLLOW / TRACKING / TRUCK) → reveal (ARC / PULL BACK / CRANE).
- Keep 1.5–3 m from the actor except for the landing frame. Run beside or behind the actor path, never on it; cross the actor's line only with a deliberate ARC.
- Aim the last wedge so the actor sits against the most interesting background (window, light, hook).

---

## 4. Beat Timing
- Walk ≈ 1 m/s (dramatic 0.6–0.8 m/s); hold 1–3 s; sit / stand / kneel ≈ 1.5 s; pick up or touch ≈ 1 s.
- Default total ≤ 15 s (a Seedance 2.0 clip runs 4–15 s). 4–5 beats (3 if ≤ 8 s). Each beat = one mark + one camera move; timecodes contiguous from 0.
- If the user sets a longer take, keep their length and note in 使用建議 that the video must be split into clips of ≤ 15 s.

---

## 5. Special Cases
- **Two actors**: A = crimson (A1…), B = amber orange (B1…); a figure at each actor's first mark; mannequins get a thin crimson or amber base ring; legend "ACTOR A", "ACTOR B", "CAMERA". Max 2 actors per plan — more means split plans.
- **Second camera**: a teal icon labeled "CAM 2" with its own wedge (static) or its own teal path. Max 2 cameras.
- **Incidental people in the scene**: omit them, or show grey static mannequins if the user wants them kept.
- **Exteriors**: use the site-block swap in `prompt-template.md` §5; vehicles stay static unless blocked.
- **Doorways into other rooms**: show a sliver of the adjoining space only if a path uses it.
