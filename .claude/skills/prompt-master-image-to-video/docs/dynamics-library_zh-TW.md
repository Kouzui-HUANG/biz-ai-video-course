---
此文件為人類閱讀用翻譯版本，AI 運行時不會載入此檔案。
---

# 圖生影動態詞彙庫（Image-to-Video Dynamics Library）

視覺動態架構師的參考資料。當需要確切的輸出範本、更豐富的動態／運鏡詞彙，或完整的 few-shot 範例時載入。

## 目錄
1. [輸出範本](#1-輸出範本)
2. [運鏡矩陣](#2-運鏡矩陣)
3. [主體動態詞彙](#3-主體動態詞彙)
4. [背景／環境動態](#4-背景環境動態)
5. [美學氛圍詞彙](#5-美學氛圍詞彙)
6. [完整範例（完整格式）](#6-完整範例完整格式)
7. [語法參考——動感風格](#7-語法參考動感風格)

---

## 1. 輸出範本

精確重現以下 Markdown 結構。替換佔位符；保留標題與 emoji。

```markdown
### 🎬 方案 A：微觀敘事（Low-Energy / Subtle）

**English Description**
{單一連貫段落。禁止條列。先用一個子句錨定第一幀，再以一條流暢的弧線描述主體微動、運鏡與美學／氛圍演變。}

**中文翻譯**
{生動細膩的繁體中文翻譯，與英文段落對應。}

**結構摘要**
* **主體人物動態 (Subject Motion)**：{...}
* **背景動態 (Background Motion)**：{...}
* **運鏡方式 (Camera Movement)**：{...}

---

### 🎬 方案 B：宏觀爆發（High-Energy / Kinetic）

**English Description**
{單一連貫段落。禁止條列。相同的錨定邏輯，但走動感路線——碰撞、位移、穿越或超現實變形，搭配快速運鏡。}

**中文翻譯**
{生動細膩的繁體中文翻譯。}

**結構摘要**
* **主體人物動態 (Subject Motion)**：{...}
* **背景動態 (Background Motion)**：{...}
* **運鏡方式 (Camera Movement)**：{...}
```

---

## 2. 運鏡矩陣

| 方案 A — 細膩 | 方案 B — 動感 |
|---|---|
| 固定鏡頭 / 鎖定鏡位 | 爆衝變焦 / 急速變焦（crash / snap zoom） |
| 緩慢推進（數公分） | 快速推軌進 / 退（dolly in/out） |
| 呼吸感手持微晃 | 移軸變焦（眩暈 / 希區考克效果） |
| 輕柔緩慢平移 / 俯仰 | 甩鏡（whip pan） |
| 細微視差 | 跟拍 / 追隨鏡頭 |
| 緩慢垂直升降（pedestal） | 環繞 / 弧形繞拍 |
| 柔和變焦對焦（rack focus） | POV 衝刺 / 第一人稱奔跑 |
| 近乎無法察覺的變焦 | 升降鏡上升 + 揭示，空拍機式拉升 |

**節奏規則**：方案 A＝一個主導的緩慢運鏡。方案 B＝可串接 2 個運鏡（例如甩鏡 → 爆衝變焦），但須維持物理上可追溯。

---

## 3. 主體動態詞彙

* **靜止 / 微動**：視線移轉、眨眼、緩緩吐息、雙唇微啟、髮絲隨微風揚起、指尖收緊、重心沉落、衣料波動。
* **位移移動**：走入畫面、轉向鏡頭、傾身、伸手、起身、奔跑、衝刺、躍起、墜落。
* **形變 / 超現實**：變形、化為粒子消散、碎裂、燃燒、結晶、融化、身體纏繞能量／電流、剪影拉伸。
* **互動**：物件自手中滑落、手掃過表面、衣物被風捲起、轉身時髮絲甩動。

---

## 4. 背景／環境動態

* **氛圍**：飄移的霧氣、落雪／落雨、漂浮的塵埃微粒、升騰的蒸氣、搖曳的枝葉、漣漪水面、閃爍的燭光／霓虹。
* **光線事件**：雲層掠過太陽、光線掃過牆面、鏡頭光斑綻放、陰影拉長。
* **動感 / 超現實**：景物向後急速飛掠化作動態模糊、光軌拉長、玻璃向外炸裂、牆面溶解、時間隧道崩塌、人群／陰影逼近。
* **景深線索**：散景微光閃動、粒子掠過前景、視差層次分離。

---

## 5. 美學氛圍詞彙

描述氛圍如何「跨越整段影片演變」——而非靜態的外觀。

* **色彩變化**：暖琥珀 → 冷青藍；去飽和轉為單色；在某個節拍上飽和度綻放。
* **光線變化**：暮色暖了半格、破曉、燈光驟然亮起、閃電頻閃。
* **基調弧線**：寧靜 → 緊張、親密 → 遼闊、夢幻 → 詭譎、平靜 → 混亂。
* **質感 / 調色**：柔光逐漸增強、顆粒感升起、對比壓暗入陰影。

---

## 6. 完整範例（完整格式）

**輸入圖片**：*一位長黑髮的女孩，於黃昏時分站在被雨水沖刷的窗邊，手捧一杯溫熱的茶；她身後是城市霓虹的散景光暈。*

### 🎬 方案 A：微觀敘事（Low-Energy / Subtle）

**English Description**
Thin tendrils of steam curl upward from the cup as her lowered eyes slowly lift into a soft, unfocused gaze toward the glass; a faint draft stirs a few loose strands of hair across her cheek while rain droplets crawl and merge down the window, catching the warm neon bokeh behind her. The camera holds almost static with a barely perceptible breathing handheld drift, easing only a few centimeters closer, as the dusk light warms by half a stop and deepens the amber glow along the curve of her face.

**中文翻譯**
細細的熱氣自杯緣裊裊升起，她垂落的眼睫緩緩抬起，化作一抹柔軟而失焦的凝視望向窗玻璃；一縷微風拂動幾絲散落頰邊的髮絲，雨珠則沿著窗面緩緩滑落、匯聚，映著她身後溫暖的霓虹光斑。鏡頭近乎靜止，僅帶著呼吸般難以察覺的手持微晃，悄悄推近數公分；此時暮色暖了半格，將琥珀色的光暈沿著她的臉頰曲線愈染愈深。

**結構摘要**
* **主體人物動態 (Subject Motion)**：垂眸緩緩抬眼、化為柔和凝視，髮絲隨微風輕動，呼吸般細微起伏。
* **背景動態 (Background Motion)**：杯口熱氣上升、雨珠沿玻璃滑落匯聚、霓虹光斑輕微閃爍。
* **運鏡方式 (Camera Movement)**：近乎固定的呼吸感手持，極緩慢推進數公分。

---

### 🎬 方案 B：宏觀爆發（High-Energy / Kinetic）

**English Description**
She snaps toward the lens and the cup slips from her fingers as the camera whip-pans and crash-zooms past her shoulder; the window detonates outward into a suspended storm of slow-motion glass shards that hang for a breath, then rush toward the viewer as the camera dollies hard through the broken frame into the downpour. The city neon stretches into streaking light trails and the color tone snaps from warm amber to electric cyan, lightning strobing the chaos into a cold, exhilarating blur.

**中文翻譯**
她猛然轉向鏡頭，茶杯自指間滑落，鏡頭隨之急速甩動並越過她的肩頭爆衝推近；窗戶向外炸裂，化作一場凝滯於慢動作的玻璃碎片風暴，懸停一瞬後朝觀者迎面湧來，鏡頭則硬生生穿越破碎的窗框、衝入傾盆大雨之中。城市霓虹被拉成流動的光軌，色調自溫暖琥珀驟然切換為電光青藍，閃電將這片混亂頻閃成冷冽而令人血脈賁張的模糊殘影。

**結構摘要**
* **主體人物動態 (Subject Motion)**：猛然轉身面向鏡頭、茶杯自手中滑落。
* **背景動態 (Background Motion)**：窗戶向外爆裂成慢動作碎片群並衝向鏡頭、霓虹拉成光軌、閃電頻閃。
* **運鏡方式 (Camera Movement)**：急速甩鏡 + 爆衝變焦，接穿越式硬推軌（whip pan → crash zoom → dolly through）。

---

## 7. 語法參考——動感風格

研究以下參考描述的密度與動詞驅動的流暢感（方案 B 的能量）。請比照這種可執行、電影感的英文寫法。

> **參考 1** — A cat in the scene runs quickly toward the camera, with white electric sparks emanating from its eyes. Its entire body becomes surrounded by electricity as it runs faster and faster. The scenery on both sides rushes backward rapidly, creating motion blur that transforms into a glowing white time tunnel.
>
> （場景中一隻貓朝鏡頭飛奔而來，雙眼迸發白色電光火花。隨著牠越跑越快，全身被電流纏繞包覆。兩側景物急速向後飛掠，形成動態模糊，並化為一條發著白光的時間隧道。）

> **參考 2** — The camera pulls back as a man runs toward it. Shadows of figures rapidly close in from behind, growing larger and larger. As one shadow draws near, it reveals a humanoid creature with a goat-like face, its features illuminated by a yellowish light. The color tone of the scene shifts to an eerie palette, creating a chilling and terrifying atmosphere.
>
> （鏡頭向後拉，一名男子朝鏡頭奔來。身後人形陰影急速逼近，越來越巨大。當其中一道陰影靠近時，顯露出一隻有著山羊般臉孔的人形生物，五官被一抹昏黃的光照亮。畫面色調轉為詭譎陰森，營造出令人毛骨悚然的恐怖氛圍。）
