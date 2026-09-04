# Typography & Layout Reference

Contents: §1 Visual hierarchy · §2 Genre → title typefaces · §3 The three typesetting rules · §4 Tagline setting · §5 Billing block · §6 Negative-space layouts · §7 Chinese title treatment · §8 Deliverable specs · §9 Typography failures

The model renders the image; the human typesets the words. Everything in this file describes the vector layer placed **over** the generated key art.

---

## 1. Visual Hierarchy — exactly four layers

`主視覺 → 片名 → Tagline → 資訊區塊`

Rough area budget on a one-sheet: image 100% (it is the ground), title block 12–18% of frame height, tagline 3–5%, billing block 8–10% at the very bottom. Anything demanding a fifth layer of attention gets cut.

## 2. Genre → Title Typeface Character

| Genre | Character | Latin examples | 中文字體 |
|---|---|---|---|
| 史詩／歷史 Epic, Period | Humanist inscribed caps, wide tracking | Trajan Pro, Cinzel, Optima | 思源宋體 Noto Serif TC (Bold)、蒙納超明 |
| 驚悚／犯罪 Thriller, Crime | Ultra-condensed grotesque, all-caps | Steelfish, Bebas Neue, Helvetica Neue Condensed | 台北黑體 Bold、思源黑體 Heavy |
| 科幻 Sci-fi | Geometric or squarish sans, tight tracking | Eurostile, Bank Gothic, Gotham | 蒙納超黑、思源黑體 Black（字面壓縮） |
| 恐怖 Horror | Distressed serif or brittle hand | Hand-distressed Didot, textured slab | 華康標題宋（做破損處理） |
| 愛情／文藝 Romance, Drama | High-contrast didone or light serif | Didot, Bodoni, Garamond | 思源宋體 Light、儷宋 |
| 喜劇 Comedy | Rounded or bouncy heavy sans | Futura Bold, rounded grotesques | 圓體 Heavy、超黑圓 |
| 動畫／家庭 Animation, Family | Soft custom-feel display | Rounded display faces | 圓體 Bold、手寫感字體 |
| 獨立／影展 Indie, Festival | Neutral grotesque, small, lowercase | Helvetica, Akzidenz, Univers | 思源黑體 Regular（小級數） |

Never leave a title at a system default with default tracking — that single fact reads as amateur faster than any other.

## 3. The Three Typesetting Rules

1. **Optical tracking** — after scaling the title, kern letter pairs by eye. Large display type always needs tracking tightened, then individual pairs opened.
2. **Occlusion** — the title should pass *behind* the subject (or a foreground element should overlap the title) so the two layers interlock. Type floating cleanly above everything reads as a sticker.
3. **Value contrast** — the title needs 3+ value steps against the pixels directly under it. Solve with reserved negative space or a controlled gradient scrim, never with an outer glow or a stroke outline.

## 4. Tagline Setting

Set at 15–25% of the title's cap height, in the title family's light weight or a neutral grotesque, generously letter-spaced, all-caps for Latin. Place it **above** the title for restraint (teaser) or below for a sales-forward one-sheet. Never two lines of Chinese tagline; never a full sentence with a period.

## 5. Billing Block (演職員字塊)

The single strongest "this is a real film" signal.

- **Typeface** — an ultra-condensed sans in a light weight, all-caps (the industry convention is a Univers 39-style compressed thin). Set at 60–70% of the poster width, centred, bottom.
- **Line order** — distributor presents / production company / a film by / lead cast (billing order) / casting / music / costume / editor / production designer / cinematographer / executive producers / producers / story by / written by / directed by.
- **Size** — cap height around 0.9–1.2% of poster height. It should be legible only up close; that is correct.
- **Below it** — rating badge, release date line, logos row, socials handle, in that order, each with clear separation.

Deliver placeholder text if the user gave no credits — never invent real names, real studios, or real festival laurels.

## 6. Negative-Space Layouts (tell the image prompt which one)

| Layout | Reserved zone | Best with |
|---|---|---|
| **上留白 Top-weighted** | Upper 30% empty sky/wall | Lone figure on a low horizon; title sits high |
| **下留白 Bottom-weighted** | Lower 30% empty ground/shadow | Colossal scale, overhead geometry; title anchors the base |
| **中央橫帶 Centre band** | A horizontal calm strip across the middle third | Split frame, symmetry; title bisects the image |
| **對角 Diagonal** | One upper corner left clear | Action, dynamic subjects; title reads into the movement |
| **邊框留白 Framed** | Even margin on all four sides | Festival, art-house restraint; small title, large air |

Name the chosen layout inside the image prompt's sixth segment so the model actually reserves the space.

## 7. Chinese Title Treatment

- **主副關係** — decide which language leads. Chinese leading: set the English title at 25–35% of its size beneath, letter-spaced. English leading: reverse.
- **字面調整** — Chinese display type needs per-character optical spacing; punctuation and 、。 should be optically trimmed.
- **直排 Vertical setting** — powerful for period, horror and art-house; run it down the right edge and leave the left two-thirds for image. Never mix vertical Chinese with horizontal Chinese in one block.
- **筆畫與影像** — thin-stroke Chinese faces disintegrate over busy imagery; over texture, go heavy or reserve clean space.

## 8. Deliverable Specs

| Use | Ratio | Notes |
|---|---|---|
| One-sheet (master) | 2:3 (27×40 in) | 300 dpi, CMYK, 3 mm bleed, keep type 12 mm inside trim |
| Taiwan print | B1 / A1 | Same 2:3-ish logic; re-check type size at final scale |
| Streaming key art | 16:9 | Subject off-centre; leave one third clear for the platform's own overlay |
| Social feed | 1:1 and 4:5 | Re-composed, not cropped; title may need a second lockup |
| Story / Reels | 9:16 | Title moves up; billing block usually dropped |
| Thumbnail | any | Test at 60 px wide before signing off |

Design the master at 2:3 and **re-compose** for the others. A centre-weighted master destroyed by a 16:9 crop is a planning failure, not a crop failure.

## 9. Typography Failures

Default tracking on a scaled title · outer glow or bevel used instead of value separation · tagline longer than the title's line · billing block set in a normal-width font (instantly wrong) · five competing type sizes · type touching the trim edge · a Chinese title in a thin serif over a busy photograph · laurels larger than the tagline · a release date in a display face competing with the title.
