# Design Knowledge Base

Table of contents:

1. Genre → Color Systems (七大內容類型配色)
2. Readability Engineering (可讀性工程)
3. Magazine Layout Pattern Library (雜誌感版式庫)
4. Photo Art Direction (真實照片攝影指導)
5. Typography for Traditional Chinese Cards (中文字型學)
6. Headline & Copy Formulas (文案公式)
7. AI Image-Prompt Composition Rules (生圖提示詞規則)

---

## 1. Genre → Color Systems

Classify the article into ONE dominant genre. Always output concrete hex codes (主色 / 輔助色 / 文字色). If the article straddles two genres, choose by the emotional goal of the hook, not the topic keywords.

| Genre | Palette (主色 / 輔助色 / 文字色) | Psychology | 調性判定範例 |
|---|---|---|---|
| 科技 / AI / 數據 | 深海軍藍 `#0B1F3A` / 冰藍 `#4FC3F7` / 白 `#FFFFFF` — 或 螢光綠 `#00E676` / 炭黑 `#111418` / 白 | 冷色 = 精確、未來感、可信的機器理性 | 科技冷冽感 |
| 商業 / 財經 / 職涯 | 墨綠 `#1B3A2F` / 香檳金 `#C9A96A` / 米白 `#F5F0E8` — 或 深藍 `#14213D` / 金 `#FCA311` / 白 | 深色+金屬色 = 資產、專業、權威 | 沉穩權威感 |
| 生活 / 人文 / 情感 | 米白 `#F5F0E8` / 大地棕 `#8D6E52` / 深咖 `#3E2F23` — 或 淺橘 `#F4A261` / 奶油 `#FAF3E0` / 深灰 `#333333` | 暖色低飽和 = 溫度、真實、貼近生活 | 溫暖人文感 |
| 警示 / 批判 / 觀點衝突 | 正紅 `#D62828` / 純黑 `#000000` / 白 — 或 警示黃 `#FFD60A` / 純黑 / 黑字於黃底 | 高對比互補 = 危險、急迫、立場鮮明 | 高壓警示感 |
| 健康 / 醫療 / 心理 | 青瓷綠 `#7FB9A6` / 淨白 `#FDFDFD` / 深灰藍 `#37474F` | 低飽和綠+大量白 = 潔淨、專業、安撫 | 潔淨療癒感 |
| 教育 / 知識 / 方法論 | 奶油底 `#FFF8E7` / 靛藍 `#3D5A80` / 活力橘 `#EE6C4D` (點綴) | 亮底+雙撞色 = 清晰、易讀、筆記感 | 知識筆記感 |
| 環境 / 永續 / 自然 | 苔綠 `#606C38` / 米白 `#FEFAE0` / 深橄欖 `#283618` | 大地綠系 = 有機、責任、長期主義 | 自然永續感 |

Rules:

- 主色 dominates ≥60% of the visual (background tint, overlay, or color block); 輔助色 ≤30%; 點綴/文字 ≤10% (60-30-10 rule).
- Saturation discipline for minimalism: at most ONE high-saturation color per card; everything else stays muted.
- User-supplied brand colors override the table — keep the genre's *contrast logic* but substitute the brand hues.

## 2. Readability Engineering

Non-negotiable rules that keep text legible on a phone feed:

- **Scrim / 壓暗**: any text placed over a photo requires a darkening overlay of 40–60% opacity (or a gradient scrim from the text side), OR a solid color block behind the text.
- **Contrast**: text vs. its immediate background must reach roughly WCAG AA (≥4.5:1). White text on mid-gray photos fails — darken more or add a keyline.
- **Safe area**: keep all text inside the central ~90% of the canvas (platforms crop edges; feed previews crop harder).
- **Mobile scale test**: 主標 height ≥ 1/10 of the image height. If the headline can't be read on a 5 cm-wide thumbnail, it fails.
- **Line discipline**: 主標 max 2 lines; 副標 max 1–2 lines; never let text occupy more than ~40% of the canvas — negative space IS the style.

## 3. Magazine Layout Pattern Library

Pick ONE pattern; name it in 排版佈局 and describe placements concretely.

| Pattern | Structure | Best for |
|---|---|---|
| A. 滿版壓暗置中 | Full-bleed photo, 45–60% dark overlay, all text center-aligned, generous letter-spacing | 情感衝擊、金句型、警示型 |
| B. 左右分割 | Photo on one half, solid 主色 block on the other half carrying all text, hard vertical edge | 數據、商業、教育（文字量較多） |
| C. 上下分割 | Photo top 60–65%, solid color band bottom with text left-aligned, magazine caption feel | 新聞感、專欄連載 |
| D. 色塊卡點 | Full-bleed photo, a semi-opaque 主色 rectangle anchored to one corner/third holding the text | 生活人文、輕觀點 |
| E. 大留白負空間 | Photo composed with vast empty sky/wall/table area; text typeset directly into that void, no overlay | 高級極簡、品牌感、療癒系 |
| F. 雜誌封面式 | Small kicker (欄目名) top, oversized 主標 stacked, thin rule lines, page-number-like 點綴 | 深度長文、系列專題、權威人物 |

Composition notes:

- Respect the photo's gaze/motion direction: subject should look or move *toward* the text, not away.
- Align to a 3×3 grid; place the photo's focal point and the headline on different thirds.
- Pattern E requires the image prompt to explicitly request negative space (see §7).

## 4. Photo Art Direction

Describe the photograph like a photographer's brief, always covering: **subject & action / lighting / lens & angle / mood**.

- **Authenticity over gloss**: candid moments, imperfect environments, real skin texture. The card should feel documentary, not stock.
- **Lighting vocabulary**: 自然窗光 (soft window light), 黃金時刻 (golden hour), 陰天柔光 (overcast diffuse), 冷白螢光 (clinical cool fluorescent — for tech/warning), 單側硬光 (hard side light — for critique/drama).
- **Lens & angle vocabulary**: 特寫淺景深 (close-up, shallow DOF — emotion), 中景平視 (waist-up eye-level — trust), 高俯拍 (top-down flat lay — methodology/objects), 低角度仰拍 (low angle — power/warning), 過肩視角 (over-the-shoulder — immersion).
- **Detail beats concept**: 「佈滿皺紋的手操作手機」>「一位老人使用科技產品」. Always direct one concrete, tension-carrying detail.
- **Cliché blacklist** — never propose: 商務握手、燈泡=創意、純白棚拍商務人像比讚、拼圖、西裝人指著上升箭頭、筆電旁咖啡俯拍(除非生活類)、火柴人示意圖。

## 5. Typography for Traditional Chinese Cards

- **Font persona mapping**: 黑體/無襯線 (Noto Sans TC 類) = 現代、科技、中性；明體/襯線 (Noto Serif TC 類) = 人文、深度、editorial；圓體 = 親和、生活、療癒；手寫體 = 情感、私密感 (只用於點綴或短主標)。
- **Max 2 font families** per card. Classic pairs: 明體主標+黑體副標 (雜誌感)；粗黑體主標+細黑體副標 (現代感)。
- **Weight contrast > size chaos**: 主標:副標 size ratio ≈ 2.5:1, and jump at least two weight steps (e.g., Black vs. Light).
- **CJK letter-spacing**: headlines gain magazine feel with +5%~+15% tracking; never negative-track Chinese.
- **Rescue techniques** when photo is busy: 白色細邊框 (white keyline box), 文字底線色條 (highlight underline in 輔助色), 直排文字 (vertical typesetting — strong editorial flavor, use sparingly).

## 6. Headline & Copy Formulas

主標題 (5–10 字), pick the formula matching the genre's emotional goal:

| Formula | Mechanism | Example shape |
|---|---|---|
| 數字量化 | Specificity = credibility | 「3個習慣，毀掉你的存款」 |
| 反差顛覆 | Break an assumption | 「越努力，越貧窮」 |
| 直球提問 | Reader self-inserts | 「你的薪水去哪了？」 |
| 損失規避 | Fear of missing/losing | 「再不懂AI就晚了」 |
| 斷言金句 | Quotable stance | 「自由是設計出來的」 |
| 身分呼喚 | Target audience callout | 「給30歲的你」 |

- 副標題 (≤15 字): supply the *mechanism* or *scope* the headline deliberately omitted — headline opens the loop, subtitle aims it, the article closes it.
- 點綴文字: choose ONE — 關鍵字 hashtag (2–3個)、一句話金句、or 專欄署名/欄目名 — placed to counterbalance the visual weight, never competing with 主標.
- Copy must be in Traditional Chinese (zh-TW) unless the source article is in another language.

## 7. AI Image-Prompt Composition Rules

The plan's final section is ONE English prompt that regenerates the directed photograph. Structure:

```
[shot type & angle] of [subject + concrete action/detail], [environment], [lighting],
[lens/DOF, e.g. 85mm, shallow depth of field], photorealistic documentary photography,
[mood + color-grading matching the 配色方案], [negative space instruction],
no text, no letters, no watermark, no logo --ar 16:9
```

- **Ratio**: match the card spec (default `--ar 16:9`; use the user's platform ratio otherwise). If the target model takes no `--ar` flag, state "16:9 widescreen composition" in prose.
- **Text-free mandate**: always include `no text, no letters, no watermark` — copy is typeset in the layout stage, never baked into the image.
- **Negative space**: explicitly reserve the area where the layout places text, e.g. "large empty negative space on the left third" for pattern B/E.
- **Color grading**: translate the hex palette into photographic language ("cool teal-and-navy grade", "warm earthy tones, muted saturation") so the photo natively matches the design.
- **Authenticity keywords**: "candid, documentary style, natural skin texture, editorial photography" — avoid "beautiful, perfect, stunning" which drift toward stock-photo gloss.
