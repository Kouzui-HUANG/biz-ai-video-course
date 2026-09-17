# Clip Assembly Reference（Clip 組裝）

Used in Step 6. Contents:
- §1 Shot timing
- §2 Clip merge / break rules
- §3 Montage handling
- §4 Dual-track rhythm
- §5 Continuity chain
- §6 Reference strategy
- §7 Model fit & batching
- §8 Backfill & self-check

A **Clip** is one video-generation call. The storyboard's rhythm (typically ~4 s per shot, with 1–3 s short shots) is a reference for Step 5 only. The deliverable unit is the Clip, and **every Clip is 4–15 s**.

---

## §1 Shot Timing（單鏡時長估算）

| Shot kind | Typical | Notes |
|---|---|---|
| Establishing / extreme wide | 3–4 s | Shorter than 3 s wastes the scale |
| Simple action (walk, reach, turn) | 2–3 s | One verb per shot |
| Compound action | 3–5 s | At most two verbs, linked by "then" |
| Reaction / expression | 1.5–2.5 s | Hold longer for omitted-reaction beats |
| Insert / prop detail | 1.5–2 s | Anything under 1.5 s must be merged |
| Emotional hold / stillness | 3–5 s | Slow motion or locked-off |
| Reveal | 2–4 s | Reveal on a cut, or at a movement's end point |

Round every shot to 0.5 s. Timecodes are global in the table and Clip-local (`0-4s`) in the YAML.

---

## §2 Clip Merge / Break Rules（合併與切段規則）

**Merge into the same Clip when:**
- the space is the same, the light state is the same, and time is continuous;
- the shots form an action → reaction pair or one shot group (see `shot-craft-library.md` §3);
- a shot is under 1.5 s. Absorb it into a neighbour by extending the neighbour, or turn it into a camera move that passes the detail (`track past candle, settle on door`).

**Break to a new Clip when:**
- the location changes, time jumps, or the light state changes (candle lit → out, dusk → night). Exception: a same-framing time-passage sequence stays in one Clip (§3);
- reality and a dream, memory or mirror-world switch (the new Clip opens clean in the new state);
- a major reveal needs a clean first frame (open the next Clip on the reveal) or a hard last frame (end the Clip on it);
- the running length would exceed 15 s, or a 5th non-montage shot would be needed.

**Shape rules:**
- 1–4 shots per Clip (montage or jump-cut states ≤ 5); target 6–12 s per Clip.
- A single-shot Clip is allowed only for a long take, a slow push or an emotional hold of 4 s or more.
- Default Clip count ≈ total ÷ 10 s, rounded up. A 30 s film is usually 3 Clips.
- Put the hook in the first shot of C1. Put the final reversal in the last Clip, no later than its second-to-last shot, so the last shot can breathe.

---

## §3 Montage Handling（蒙太奇處理）

A montage (several 1–3 s images) becomes **one Clip**:
- write it as ≤ 5 shots of 1.5–2 s each, with `type: "Rapid cut"`; or
- fold it into one continuous move that passes the images in sequence (`fast lateral track past five portraits, each face older`).

Never spread a montage across several Clips. Its rhythm would be lost between generations.

**Time passage / jump-cut sequence.** Nights passing, a repeated action that changes a little each time (action–reaction variant 9), or a loop: keep the framing fixed and write it as **one shot entry**:
- `type: "Jump cuts ×3, same framing, locked-off"`
- `time` covers the whole sequence; each state is ≥ 1.5 s, and the states are listed in order inside `action_prompt` (`Night 1: …; Night 2: …; Night 3: …`).
- Each state counts toward the 5-state montage cap.
- The changing detail (an empty seat, a dying plant, a calendar) must be the only thing that changes.

---

## §4 Dual-Track Rhythm System（雙軌節奏系統）

Rhythm runs on two tracks planned together.

| Track | Controls | Fast state | Slow state |
|---|---|---|---|
| **Visual track** | Shot length, change in shot size, camera speed | Short shots, big size jumps, moving camera | Long holds, gradual size change, static camera |
| **Sound track** | Sound density, dynamics, silence | Layered SFX, breath, rising ambience | Single sound, room tone, true silence |

**Rules:**
1. **Counterweight:** when one track runs fast, keep the other sparse. Fast cuts over near-silence feel uncanny; a long static hold over dense sound feels tense.
2. **Convergence:** at the climax both tracks peak together, then **drop to silence** on the next shot. That silence is the aftertaste.
3. **Pre-lap before reveals:** let the sound arrive before its image (`[SFX] pre-lap`).

**Rhythm patterns (choose one in 導演意圖):**

| Pattern | Shape | Suits |
|---|---|---|
| Fast cut 快切 | Short, short, short, hold | Action, panic |
| Slow push 慢推 | One long approach | Dread, revelation |
| Still + burst 靜＋爆 | Long stillness → sudden sharp beat | Horror, dark fairy tale (default) |
| Breathing 呼吸型 | Alternating long and short | Emotion, restrained tragedy |

---

## §5 Continuity Chain（跨 Clip 連戲）

- **Verbatim locks.** Copy `art_style`, `visual_lock`, `prop_lock` and `scene_lock` strings character for character into every Clip that uses them. Never paraphrase.
- **Identity echo.** Every `action_prompt` opens with `S1 (3–6 key anchors)`, the same words each time, with one echo per locked character on screen (lead first). A hidden identity or double is echoed by its neutral appearance lock only (`S6 (man, same charcoal suit, face unseen)`), so the echo never gives away the reveal.
- **`continuity_out`** (last line of each Clip) records the tail state: subject position and screen side, light state, held props, camera distance.
- **`continuity_in`** (first line of the next Clip) restates that state, or declares the cut: `Hard cut; new location L2, same night`.
- **Screen direction.** Keep the 180° axis consistent across Clips. A deliberate axis break must be declared in 備註 and in `type`.
- **State changes.** Wounds, wet clothes, extinguished lights and lost props must persist once introduced. Update the lock with an appended state (`…, hood now torn`) and keep the base words. Items a character will lose (earbuds, a helmet, a bag) belong in the lock but never in the identity echo.
- **Sound bridge across Clips.** End Clip n with the first sound of Clip n+1 when the cut needs smoothing.

---

## §6 Reference Strategy（參考素材策略）

Asset source tags:

| Tag | Meaning | Action |
|---|---|---|
| `user_subject` | User marked it as a reference subject | Lock from the image; tell the user to attach it as the character reference in every Clip that uses it |
| `user_image` | Ordinary uploaded picture, even if it looks like the protagonist | Lock from the image; it still needs a clean single-entity reference, so also emit an `asset_refs` prompt |
| `generate` | Nothing supplied | Invent the lock; emit an `asset_refs` turnaround or scene-plate prompt to generate **before** the Clips |

**Production notes (include in 後製備註 when relevant):**
- Generate reference sheets first, then feed them as image references to each Clip.
- Real-person photos used as face references may be rejected by some video models (Seedance 2.0 has returned generic errors). Recommend an AI-generated character sheet of a fictional person instead: photoreal for realistic styles, stylized for everything else.
- For consistent props, use a close-up reference plate. For consistent spaces, use a wide establishing plate.

---

## §7 Model Fit & Batching（模型適配與分批）

- **Default range:** 4–15 s per Clip, which matches multi-shot video models such as Seedance 2.0.
- **User-named model or length cap:** set the Clip maximum to that cap and re-split. Never exceed what the user states.
- **Batching:** more than 8 Clips → output C1–C8 plus the full 導演意圖, 資產清單 and 分鏡總表 (the table is complete; Clips beyond C8 are marked 待產出). End with 「回覆「繼續」產出 C9 起」. Later batches output only the Clip YAML, with the locks repeated verbatim.

---

## §8 Backfill & Self-Check（回填與自檢）

1. Fill the table's Clip column.
2. Confirm that each Clip's shot times sum to its duration and that global timecodes are continuous with no gaps.
3. Confirm that each Clip is 4–15 s and has 1–4 shots (montage ≤ 5), with no shot under 1.5 s.
4. Confirm that `continuity_out(Cn)` matches `continuity_in(Cn+1)`.
5. Confirm that the hook is in C1 shot 1 and the final reversal is in the last Clip.
