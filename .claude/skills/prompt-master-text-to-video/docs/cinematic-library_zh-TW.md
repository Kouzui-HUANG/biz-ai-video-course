---
此文件為人類閱讀用翻譯版本，AI 運行時不會載入此檔案。
---

# 文生影電影術語庫（Cinematic Library）

AI 影片提示詞架構師的參考素材。當你需要精確的輸出範本、電影術語庫，或一個完整範例時載入。請比照這種高密度、可執行、具體的風格。

## 目錄
1. [輸出範本](#1-輸出範本)
2. [鏡位／景別術語庫](#2-鏡位景別術語庫)
3. [攝影機運動術語庫](#3-攝影機運動術語庫)
4. [光線術語庫](#4-光線術語庫)
5. [色彩與調色術語庫](#5-色彩與調色術語庫)
6. [完整範例（full format）](#6-完整範例full-format)

---

## 1. 輸出範本

精確重現以下 Markdown 結構。替換佔位符；保留標題與 emoji。每套方案中，**先完整英文原文**，再**完整繁體中文翻譯**。前面不加前言，後面不加總結。

```markdown
## 🎬 Scenario 1: Single-Take

**[English]**
{一段連貫、流暢地描述單一不間斷鏡頭的文字。先確立鏡位 ＋ 場景，再以精確的場景內時序編排主體動作與一段主導的攝影機運動。僅用具體名詞。僅在場景明顯有對白時才附上 Dialogue: 區塊。}

**[繁體中文] 方案一：單一鏡頭**
{完整、對應的繁體中文翻譯。}

---

## 🎬 Scenario 2: Multi-Shot Sequence

**[English]**
**Shot 1** — {景別} | {攝影機運動}
{一個核心主體動作。僅用具體名詞。}

**Shot 2** — {景別} | {攝影機運動}
{...}

**Shot 3** — {景別} | {攝影機運動}
{...}

**Shot 4** — {景別} | {攝影機運動}   ← 選填（總共 3～4 個鏡頭）
{...}

Dialogue:   ← 僅在場景明顯有對白時保留；否則完全省略
- "{簡短、自然的台詞}"

**[繁體中文] 方案二：多鏡頭序列**
**鏡頭一** — {景別} | {攝影機運動}
{核心動作。}

**鏡頭二** — {景別} | {攝影機運動}
{...}

**鏡頭三** — {景別} | {攝影機運動}
{...}

對白：   ← 僅在有對白時保留
- 「{簡短自然的台詞}」
```

**連貫性規則**：在方案二中，於每個包含角色的鏡頭裡，完全一致地重複鎖定的角色描述（外觀、服裝、關鍵特徵）。

---

## 2. 鏡位／景別術語庫

| 術語 | 用途 |
|---|---|
| Extreme Wide Shot (EWS) 大遠景 | 建立規模感，將主體置於環境中 |
| Wide Shot (WS) / Full Shot 全景 | 全身 ＋ 周遭環境 |
| Cowboy Shot 七分身 | 大腿中段以上；姿態、氣場、拔出武器 |
| Medium Shot (MS) 中景 | 腰部以上；對話、手勢 |
| Medium Close-Up (MCU) 中近景 | 胸部以上；主要的情緒層次 |
| Close-Up (CU) / Extreme CU (ECU) 特寫／大特寫 | 臉部／細節；微表情、物件節拍 |
| Over-the-Shoulder (OTS) 過肩鏡 | 對話幾何、POV 錨定 |
| Point-of-View (POV) 主觀鏡頭 | 第一人稱沉浸感 |
| Low / High / Dutch angle 仰／俯／傾斜角 | 權勢、脆弱、不安 |

---

## 3. 攝影機運動術語庫

| 術語 | 效果 |
|---|---|
| Static / locked-off 固定鏡位 | 靜止、張力、觀察 |
| Slow push-in / pull-out 緩慢推近／拉遠 | 建立親密感／揭示脈絡 |
| Dolly zoom (vertigo) 滑軌變焦（眩暈） | 失向、恐懼、揭露 |
| Tracking / following shot 跟拍 | 隨主體移動 |
| Pan / tilt 橫搖／直搖 | 橫向或上下揭示空間 |
| Jib-up / crane / pedestal 升降臂／吊臂／升降 | 抬升至宏偉或上帝視角揭示 |
| Handheld stabilization 手持穩定 | 紀錄片式急迫感、呼吸感 |
| Orbit / arc 環繞／弧形 | 繞行主體、營造 3D 存在感 |
| Whip pan / crash zoom 甩鏡／爆衝變焦 | 動感的標點、硬切能量 |

**節奏規則**：每個鏡頭一個主導的攝影機運動（準則 4）。單一鏡頭中，運動可以*演進*（例如緩慢推近漸轉為輕緩弧形），但必須維持為一段可追蹤、連續的動作。

---

## 4. 光線術語庫

* **Hard rim light 硬邊緣光**——銳利的輪廓分離、戲劇感。
* **Soft key from window 窗光柔主光**——自然、柔和的塑形。
* **Golden hour 黃金時刻**——溫暖的低角度陽光、長影。
* **Blue hour / twilight 藍色時刻／暮光**——冷調的環境暮色。
* **Neon reflections on wet asphalt 濕瀝青上的霓虹倒影**——飽和的都市夜。
* **Volumetric light shafts 體積光束**——穿過霧／塵／百葉的耶穌光。
* **Practical sources 實景光源**——燈、燭、螢幕、招牌等驅動畫面光感的光源。
* **Chiaroscuro / low-key 明暗對照／低調光**——深沉陰影、單一光源。

---

## 5. 色彩與調色術語庫

* **Desaturated 去飽和**——低調、陰鬱、粗糲。
* **High-contrast 高對比**——大膽、強烈的明暗分離。
* **Teal-and-orange palette 青橙色調**——電影大片式的平衡。
* **Monochrome / duotone 單色／雙色調**——風格化的克制。
* **Anchored by [specific color] 以特定色彩定錨**——單一招牌色主導（例如「以緋紅定錨」）。
* **Warm amber → cool cyan shift 暖琥珀 → 冷青藍的轉換**——貫穿整段的色調弧線。

---

## 6. 完整範例（full format）

**原始構想**：*一名偵探在雨夜的城市辦公室裡接到一通神秘來電。*

## 🎬 Scenario 1: Single-Take

**[English]**
We open on a Medium Close-Up of a woman in a charcoal trench coat seated at a steel desk, her face lit by the cold blue glow of a desk monitor while rain streaks the window behind her and neon signage bleeds crimson across the wet glass. A rotary phone on the desk begins to ring; the camera executes a slow, continuous push-in toward her as her eyes lift from a case file, her hand hovers, then closes around the receiver and raises it to her ear. As she listens, the push-in eases into a gentle arc that drifts to her profile, revealing the rain-blurred skyline beyond, and her jaw tightens on a single held beat.

Dialogue:
- "...Who is this?"

**[繁體中文] 方案一：單一鏡頭**
畫面以中近景（MCU）開場：一名身著炭灰色風衣的女子坐在鋼製辦公桌前，臉龐被桌上螢幕冷冽的藍光映照，身後的窗上雨痕縱橫，霓虹招牌在濕玻璃上滲出緋紅。桌上的轉盤電話響起；鏡頭朝她緩緩、連續地推近，她的目光自案卷抬起，手懸停片刻，繼而握住聽筒、舉至耳畔。在她聆聽之際，推鏡漸轉為輕緩的弧形運動，滑向她的側臉，帶出窗外被雨水模糊的城市天際線，她的下顎在一個凝止的節拍上繃緊。

對白：
- 「……你是誰？」

---

## 🎬 Scenario 2: Multi-Shot Sequence

**[English]**
**Shot 1** — Extreme Wide Shot (EWS) | Slow aerial push-in
A rain-lashed glass office tower at night, a single lit window on the upper floor glowing amber against the blue-black skyline; neon reflections shimmer on the wet street far below.

**Shot 2** — Close-Up (CU) | Static, locked-off
The black rotary phone on a steel desk rings, its bell trembling; cold blue monitor light and crimson neon spill across the brushed-metal surface.

**Shot 3** — Over-the-Shoulder (OTS) | Subtle handheld drift
From behind the woman in the charcoal trench coat, her hand enters frame and lifts the receiver to her ear; the rain-streaked window and bleeding neon fill the soft-focus background.

**Shot 4** — Medium Close-Up (MCU) | Slow push-in
The same woman in the charcoal trench coat, jaw tightening as she listens, cold blue light hardening the line of her cheek against the crimson glow.

Dialogue:
- "...Who is this?"

**[繁體中文] 方案二：多鏡頭序列**
**鏡頭一** — 極遠景（EWS）｜緩慢空拍推進
夜裡一棟被雨水拍打的玻璃辦公大樓，高樓層唯一亮著的窗在藍黑天際線映襯下透出琥珀色光暈；遠處濕亮的街面上霓虹倒影粼粼。

**鏡頭二** — 特寫（CU）｜固定鏡位
鋼製辦公桌上的黑色轉盤電話響起，鈴身微微震顫；冷藍的螢幕光與緋紅霓虹潑灑在拉絲金屬桌面上。

**鏡頭三** — 過肩鏡（OTS）｜輕微手持晃動
自炭灰色風衣女子的背後望去，她的手入鏡、將聽筒舉至耳畔；雨痕窗面與滲開的霓虹填滿柔焦的背景。

**鏡頭四** — 中近景（MCU）｜緩慢推近
同一名炭灰色風衣女子，聆聽時下顎緊繃，冷藍的光在緋紅光暈映襯下勾硬了她的頰線。

對白：
- 「……你是誰？」
