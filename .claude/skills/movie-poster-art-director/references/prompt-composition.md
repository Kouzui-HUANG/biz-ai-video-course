# Prompt Composition Reference

Contents: §1 Six-segment formula · §2 Vocabulary banks · §3 Identity anchors · §4 Text-free & negative-space phrasing · §5 Aspect-ratio tail · §6 Worked example · §7 Forbidden phrasing

---

## 1. Six-Segment Formula

Write ONE flowing paragraph of 150–220 words. Cinematic English sentences, never a tag list. The segments run in this order and blend into each other:

```
[1 Archetype & framing] → [2 Subject & identity anchors] → [3 Environment & scale]
→ [4 Light logic & atmosphere] → [5 Palette, grade & texture] → [6 Negative space & spec]
```

Segment 6 always closes the paragraph so the reserved zone and the text-free instruction are the last things the model reads.

| # | Segment | Must specify |
|---|---|---|
| 1 | Archetype & framing | Composition archetype + shot size + camera angle + lens |
| 2 | Subject & identity anchors | Locked features from the character image, wardrobe silhouette, pose, gaze direction, micro-expression |
| 3 | Environment & scale | Foreground / midground / background layers + the scale relationship that carries the idea |
| 4 | Light logic & atmosphere | ONE motivated key light + rim/fill, weather or particulate, time of day |
| 5 | Palette, grade & texture | The 60-30-10 colours named, film-stock grain, halation, contrast curve |
| 6 | Negative space & spec | Where the frame stays empty for the title block, text-free phrasing, aspect ratio |

## 2. Vocabulary Banks

**1 · Framing & lens**
`extreme wide establishing frame` · `full-length figure` · `medium shot from chest up` · `extreme close-up portrait` · `top-down bird's-eye view` · `low-angle hero framing` · `dutch-tilted frame` · `14mm ultra-wide with pronounced perspective` · `35mm natural perspective` · `85mm compressed telephoto` · `135mm with heavy background compression` · `anamorphic 2.39:1 framing rendered inside a vertical poster crop` · `shallow depth of field isolating the subject` · `deep focus holding every layer sharp`

**2 · Pose, gaze & expression**
`seen from behind, shoulders squared` · `turned three-quarters away, chin dropped` · `direct unblinking gaze into the lens` · `eyes cast to the lower left, jaw set` · `mid-stride, coat caught by wind` · `hands loose and open at the sides` · `a stillness that reads as containment rather than calm` · `micro-expression of suppressed grief at the corner of the mouth`

**3 · Environment & scale**
`layered depth with a foreground silhouette, a midground figure and a dissolving background` · `dwarfed by a structure that fills the upper two-thirds` · `a low horizon line placing the figure in the bottom eighth of the frame` · `a rigid geometric grid of rooftops enclosing the figure` · `the world falling away into atmospheric haze`

**4 · Light & atmosphere**
`a single hard key raking from frame left` · `motivated by a sodium streetlamp just outside the frame` · `north-window soft key with the shadow side left open` · `hot rim light separating the figure from a near-black ground` · `volumetric god-rays through dust` · `low golden-hour backlight with heavy bloom` · `underlit from a source below the chin` · `flat overcast ambient broken by one directional shaft` · `sea fog softening every edge beyond ten metres` · `smoke and drifting ash catching the light`

**5 · Palette, grade & texture**
`graded around [colour] as the dominant, [colour] carrying the mid-tones and a single [colour] accent` · `crushed blacks with retained shadow detail in the subject only` · `bleach-bypass contrast with desaturated mid-tones` · `warm highlight roll-off and cool shadows` · `fine 35mm film grain` · `subtle halation blooming around the brightest highlights` · `a soft anamorphic streak on the practical` · `matte paper texture across the whole frame`

**6 · Negative space & spec**
`the upper third left as an uninterrupted expanse of [sky/wall/fog], deliberately empty` · `a calm horizontal band across the centre with no detail` · `clean unbroken margin around all four edges` · `entirely free of any lettering, typography, captions, logos or watermarks — a pure photographic image` · `vertical 2:3 movie poster composition`

## 3. Identity Anchors (from supplied character art)

Write the anchor phrase ONCE in the Key Art Bible, then repeat it **verbatim** in every prompt. A good anchor names 5–7 fixed attributes and nothing else:

> `a woman in her early forties, square jaw and heavy brow, shoulder-length black hair pushed back and greying at the temples, deep-brown eyes, a pale vertical scar through the left eyebrow, wearing a salt-stained olive fisherman's jacket`

Rules: name only what the image actually shows · never invent ethnicity, age or marks the art does not support · re-light and re-pose freely, but never restate face structure, hair colour, eye colour or the signature garment differently between proposals · for a background image, anchor the location the same way (`a concrete tidal breakwater under a low grey sky`).

## 4. Text-Free & Negative-Space Phrasing

Always positive, never a negative-prompt list. Two clauses, both required:

1. Reserve the zone — `the lower third resolves into flat unbroken shadow, held deliberately empty`.
2. Forbid lettering as a description of what the image *is* — `a pure photographic frame entirely free of lettering, titles, captions, logos or watermarks`.

Never write "with the film title at the top", "add the tagline", "include credits" — the model will produce garbled pseudo-text and destroy the reserved zone.

## 5. Aspect-Ratio Tail

Close with plain language, not parameters: `vertical 2:3 movie poster composition` / `wide 16:9 streaming key art composition with the subject held off-centre to camera right`. Never emit `--ar 2:3`, `::`, weights, or `(word:1.4)` syntax.

## 6. Worked Example

Material given: a mystery drama script set in a Taiwanese fishing town; one character image (a woman, 40s, olive jacket); one background image (a concrete breakwater in fog).

**提案一：概念先導版 Teaser｜〈退潮之後〉**

- **一句話概念：**海水退去時，露出來的東西不一定是我們想找的。
- **構圖原型：**地平線孤影 Lone Figure on Horizon

**English Prompt:**
```text
An extreme wide establishing frame, shot on a 35mm lens at eye level, holding deep focus across every layer. A woman in her early forties, square jaw and heavy brow, shoulder-length black hair pushed back and greying at the temples, deep-brown eyes, a pale vertical scar through the left eyebrow, wearing a salt-stained olive fisherman's jacket, stands alone in the bottom eighth of the frame with her back to us, shoulders squared, looking out along a concrete tidal breakwater that dissolves into sea fog. Wet sand in the foreground holds a single line of footprints leading to her and none leading away. The light is flat overcast ambient, broken by one weak directional shaft low on the water, sea fog softening every edge beyond ten metres. Graded around cold fog grey as the dominant, wet-slate green carrying the mid-tones and a single rust-orange accent on a distant channel marker, with fine 35mm grain and gentle halation. The upper two-thirds is an uninterrupted expanse of pale fog, deliberately empty. A pure photographic frame entirely free of lettering, titles, captions, logos or watermarks. Vertical 2:3 movie poster composition.
```

**中文翻譯：**
極廣的定場畫面，35mm 鏡頭平視，全景深保持每一層次清晰。一名四十出頭的女性——方下顎、眉骨明顯，及肩黑髮向後撥、鬢角泛白，深棕色雙眼，左眉有一道淺色直向疤痕，身穿沾附鹽漬的橄欖綠漁夫外套——獨自站在畫面最下方八分之一處，背對鏡頭、肩線平直，望向一條沒入海霧的混凝土防波堤。前景濕沙上只有一行走向她的腳印，沒有離開的腳印。光線為平坦的陰天環境光，被水面上一道微弱的低角度光束打破，海霧讓十公尺外的一切邊緣都柔化。調色以冷霧灰為主、濕板岩綠承接中間調，僅在遠方航道標誌上留一抹鏽橙點綴，帶細緻 35mm 顆粒與輕微光暈。畫面上方三分之二是連續未被打斷的淡霧，刻意留白。純攝影畫面，完全不含任何文字、標題、字幕、標誌或浮水印。直式 2:3 電影海報構圖。

**文字排版計畫：**
- **片名：**思源宋體 Bold，直排置於畫面右側上方留白區，字距收緊後逐字微調；霧的漸層剛好讓筆畫從上到下由清晰轉為半透，形成與影像互鎖的關係。
- **Tagline：**「有些東西，退潮才看得見。」— 置於片名下方，級數為片名的 20%，字距放寬。
- **留白版式：**上留白 Top-weighted（上方三分之二為霧）。
- **演職員字塊：**底部置中，寬度佔畫幅 65%，極窄體全大寫；因下方為濕沙有紋理，字塊下方壓一道極淡的暗部漸層。

## 7. Forbidden Phrasing

`--ar 2:3` / `(dramatic:1.3)` / `masterpiece, best quality, 8k, trending on artstation` / `no text, no watermark, no blur` (negative-list syntax) / `movie poster with the title "…"` / `in the style of [living designer or studio]` / comma-separated keyword dumps / `epic, cinematic, stunning, breathtaking` stacked as adjectives with nothing physical behind them.
