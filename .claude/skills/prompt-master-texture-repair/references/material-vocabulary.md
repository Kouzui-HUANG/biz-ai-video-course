# Material & De-noise Vocabulary Bank

Reference library for Step 2 (Material Regeneration Strategy). Pull the entries that match the parsed image category and weave them — in Traditional Chinese — into the `[極致物理肌理]` module. These are palettes, not a checklist: pick what the specific subject actually has; do not dump every term.

## Table of Contents
1. People (人物)
2. Products (產品)
3. Scenes & Environments (場景)
4. Background De-noise Bank (背景去噪詞庫)
5. Photography & Tone Bank (攝影設備與調性)

---

## 1. People (人物)

The single biggest failure mode is plastic / over-retouched skin. Always restore micro-detail and light-through-skin.

- **皮膚 Skin** —【去噪修復公式・人物必用，兩半務必同時出現】(a) **去噪半** 平滑無瑕、細緻、乾淨純粹、完全零噪點的皮膚表面（clean, pure smooth, completely noise-free），徹底去除顆粒、斑塊、塗抹與壓縮噪點；(b) **紋理半** 同時保留自然彈性皮膚、真實細微毛孔、次表面散射（subsurface scattering）的健康透光感、自然膚色微不均與淡淡潮紅、細絨毛、輕微油光與乾濕分區、保留痣與雀斑等真實特徵；**未經修飾的原始攝影質感**，絕無塑料感、蠟感、過度磨皮或磨成死板面具。「平滑乾淨」意指去噪，而非去除紋理 —— 少了 (a) 沒去噪，少了 (b) 變塑料。
- **毛髮 Hair** — 一根根分明的髮絲、自然髮流與少量飛絲、髮絲高光與陰影層次、蓬鬆而非結塊；眉毛與睫毛根根清晰。
- **眼睛 Eyes** — 清澈的虹膜放射狀紋理、濕潤的眼球高光反光、自然的血絲淡化、眼周細紋保留。
- **唇 Lips** — 自然唇紋、真實濕潤感與高光、唇色漸層，不塗抹成一片死板色塊。
- **手・膚質細節 Hands/detail** — 指節褶皺、指甲的半透明月牙與自然光澤、皮膚表面的細微紋理。

## 2. Products (產品)

Identify the true material first, then assign its signature surface behavior.

- **金屬 Metal** — 拉絲金屬（brushed metal）的方向性細紋、陽極氧化（anodized）霧面、鏡面不鏽鋼反射、噴砂磨砂顆粒、電鍍高光與銳利反光邊、金屬邊緣的環境反射。
- **塑料 Plastic** — 細膩啞光塑料（matte plastic）、ABS 微顆粒紋、亮面注塑的均勻高光、半透明塑料的內部漫射。
- **玻璃／透明 Glass** — 晶瑩剔透、銳利的高光折射與焦散、通透的邊緣光、內部反射與透視變形、水晶般的清澈。
- **皮革 Leather** — 真皮荔枝紋／粒面、自然使用褶皺、車縫線與走線、邊緣的磨損與油潤光澤。
- **木材 Wood** — 清晰木紋與年輪、天然節疤、導管孔隙、啞光原木或上蠟／上漆的柔和反光。
- **織物・布料 Fabric** — 織物經緯結構、針織的線圈紋理、絨毛與起絨感、垂墜的自然褶皺。
- **陶瓷・釉面 Ceramic** — 溫潤釉光、細微開片、手工拉坯的微妙起伏、啞光素坯的顆粒。
- **紙・包裝 Paper** — 紙張纖維紋理、壓紋與燙金的立體反光、啞膜／亮膜的差異。

## 3. Scenes & Environments (場景)

- **植物 Plants** — 清晰的葉脈與葉緣鋸齒、葉面絨毛與蠟質反光、花瓣的半透光、自然的枯萎與蟲蝕邊緣。
- **建材 Masonry** — 粗糙真實的混凝土表面與氣孔、磚牆的顆粒與砂漿縫、石材的天然紋路與礦物斑點。
- **水・液體 Water** — 清澈折射、水面波紋與反光、飛濺水珠的高光、玻璃上的凝結水滴。
- **金屬・木質建築 Architecture** — 飛檐與樑柱的木紋、金屬構件的氧化與反光、屋瓦的排列與陰影。
- **軟裝織物 Soft furnishing** — 窗簾與沙發布料的垂墜、地毯的絨毛方向、抱枕的填充體積感。
- **土壤・自然地面 Ground** — 土壤顆粒與濕度、草地的層次、沙粒的高光與陰影。

## 4. Background De-noise Bank (背景去噪詞庫)

The background clause must be emphatic — Img2Img otherwise re-references the dirty original and de-noises incompletely. Combine several of these into `[環境與背景]`:

- 乾淨純粹、平滑無瑕、完全零噪點的背景
- clean, pure smooth background, completely noise-free
- 無任何顆粒、塗抹感、色帶或壓縮痕跡
- 純色柔和背景，均勻過渡，無雜訊
- **強制去噪聲明**：此處務必強力強調，避免生圖模型參考原圖而導致去噪不徹底 —— 背景需徹底重繪為乾淨表面，不得繼承原圖的髒污與噪點。

## 5. Photography & Tone Bank (攝影設備與調性)

For the closing `[攝影設備與調性]` module — choose what matches the source's look:

- **人像 Portrait** — 未經修飾的原始攝影、85mm 鏡頭、f/1.8 大光圈、中畫幅、淺景深、影棚側光或自然窗光、電影級寫實主義、極致清晰。
- **產品 Product** — 100mm 微距鏡頭、柔光箱均勻布光、無雜亂陰影、高光通透、商業產品攝影、極致銳利、乾淨立體。
- **場景 Scene** — 廣角至標準焦段、自然光或黃金時刻光、高動態範圍、真實環境色、電影級調色、景深層次分明。
- **通用調性** — 高解析度、真實物理光影、無 AI 塑料感、質感細膩、photorealistic、fine detail。

---

## 6. Worked Example — Repair-First Order + Skin De-noise Formula (portrait)

Gold-standard shape for a human portrait. Note (1) the **repair-first order** — restoration payload → background de-noise → realism anchors → subject identity → lighting lock → camera — and (2) the **skin clause carrying BOTH** the de-noise words AND the texture anchors:

> Raw unretouched photographic texture, smooth, flawless, fine and delicate skin, clean, pure smooth, completely noise-free skin surface entirely free of grain, blotches, smearing or compression noise, while still keeping natural elastic real skin with clearly visible fine pores, healthy subsurface-scattering translucency, subtle natural tonal variation and a faint flush across the cheekbones, fine vellus hair, a light natural T-zone sheen, preserved real micro skin texture and bone structure, absolutely no plastic or waxy feel and no over-smoothing into a flat mask, [hair / eyes / makeup / lip / fabric texture …], a clean pure perfectly smooth and completely noise-free solid background that must be entirely repainted and must not inherit the original's dirt and noise, true physical light and shadow, photorealistic, fine detail, no AI plastic feel, [SUBJECT identity + pose + styling + makeup look], keeping the original's [lighting] with light direction and perspective kept identical to the source, [85mm f/1.8, medium format, shallow DoF, cinematic realism, extreme clarity].

The bracketed slots are swapped per image; the leading skin+de-noise run and the background clause keep this same structure every time. (Traditional-Chinese is the default output language; render this shape in TC unless the user explicitly asks for English.)
