# 風格聖經（繁中對照）

> `references/style-bible.md` 的中文對照版，僅供人閱讀。英文 prompt 片語、風格鎖定字串、YAML、標籤維持原文，因為那是實際要餵給模型的文字。

任何輸出之前都要先讀。目錄：
- §1 預設風格：哥德怪誕暗黑童話電影感
- §2 風格基因轉譯
- §3 風格覆寫規則與預設集
- §4 內容邊界

---

## §1 預設風格：哥德怪誕暗黑童話電影感

### 1.1 美術風格 lock（逐字貼進每個 Clip 的 `art_style`）

```
Gothic dark fairy-tale animated film, stop-motion-like tactile miniatures, grotesque-cute character design, cinematic chiaroscuro, bioluminescent accents, 35mm film grain
```

### 1.2 渲染子變體

擇一並明確標註。只替換 lock 的第一個子句。

| 變體 | 第一個子句改為 | 適用 |
|---|---|---|
| **A 觸感定格動畫**（預設） | `Gothic dark fairy-tale animated film, stop-motion-like tactile miniatures` | 手作質感：羊毛氈、陶瓷、蠟、老木頭 |
| B 哥德墨線動畫 | `Gothic dark fairy-tale 2D animation, scratchy ink linework, watercolor washes` | 繪本感，預算較輕 |
| C 風格化 3D 動畫長片 | `Gothic dark fairy-tale stylized 3D animated feature, soft subsurface skin` | 精緻的 CG 質感，觀眾面廣 |

### 1.3 配色（60-30-10）

| 比例角色 | 顏色 | 色碼 |
|---|---|---|
| 60 主色 | 墨黑／瘀青般的夜藍 | `#0E0B10` / `#1C2233` |
| 30 輔色 | 苔蘚灰綠／骨白象牙色 | `#2E3A34` / `#E8DCC4` |
| 10 點綴色（每部片擇一） | 燭光琥珀 · 血紅 · 毒藥青綠 · 螢光綠 | `#E0A040` · `#8E1B24` · `#3F8C85` · `#9BE564` |

**螢光點綴色是這個風格的招牌**：生物發光的飛蛾、發光的菇蕈、光蟲垂下的發光絲線、磷光般的眼睛。面積控制在畫面的 10%。

### 1.4 光線邏輯

- **每個鏡頭只用一個有動機依據的主光源：**蠟燭、提燈、一道月光、壁爐火光、生物螢光、一扇透著冷光的窗。
- 低調光的明暗對比，陰影深沉但暗部仍保有細節。用輪廓光把剪影與背景分開。
- 用霧或薄霾讓光束產生體積感。
- 光線狀態本身就是連戲的一部分。一旦改變，就切到新的 Clip（見 `clip-assembly.md` §2）。

### 1.5 質感與調色

35mm 底片顆粒、畫面中的實景光源帶柔和光暈、輕微暗角、黑位略微提起，除了點綴色之外整體降低飽和度。

### 1.6 角色設計（怪誕可愛）

- **比例：**四肢細長、頭和眼睛特別大、嘴巴極小。
- **材質：**帶一道髮絲般細裂紋的陶瓷肌膚、縫線接縫、鈕扣或玻璃細節、脫線綻開的布料。
- **服裝輪廓：**連帽斗篷、高領、圍裙洋裝、燕尾服。服裝上帶一個點綴色。
- **怪誕只停在詭異，絕不是受傷：**一道縫線、一條裂痕、咧得太開的笑容、數量不對的影子。

### 1.7 母題庫

被布蓋住的鏡子 · 鑰匙 · 停擺的時鐘 · 鳥籠 · 飛蛾 · 蠟燭 · 荊棘 · 人偶 · 牙齒 · 音樂盒 · 烏鴉 · 提燈 · 螺旋樓梯 · 空椅子。

### 1.8 聲音調色盤（供 audio_prompt 與後製配樂使用）

- **環境音：**穿過鑰匙孔的風聲、木頭嘎吱作響、遠處的鐘聲、雨打在石板瓦上、飛蛾振翅、蠟油滴落。
- **擬音：**赤腳踩在冰冷石地上、布料拖行、陶瓷輕碰的喀嗒聲、轉動鑰匙。
- **配樂方向（僅限後製）：**走音的音樂盒、沒有旋律的低音弓弦、單一童聲的哼唱、玻璃琴。

### 1.9 預設風格的禁用項

晴朗溫暖的日光 · 平板的正面打光 · 亮面塑膠質感 · 粉嫩的糖果色調 · 露骨的血液或傷口 · 廉價的突發驚嚇構圖 · 任何畫面文字。

---

## §2 風格基因轉譯

導演和藝術家的名字絕不寫進 prompt，一律改用技法描述詞。

| 基因 | 取用什麼 | Prompt 描述詞 |
|---|---|---|
| 希區考克系 | 由資訊落差堆疊出的懸疑 | `threat sharp in foreground, subject unaware`；`high-angle locked-off`；`dolly zoom` |
| 庫柏力克系 | 對稱、靜止、莊嚴的壓迫感 | `one-point perspective, bilateral symmetry`；`slow steady forward track down corridor` |
| 王家衛系（*花樣年華*） | 框中框的空間、被切割的構圖 | `framed through doorway / window bars, walls crowd frame`；`narrow corridor, figures brush past` |
| 今敏系 | 現實與幻覺之間的滑移、畫中畫 | `match cut from reflection to reality`；`mirror shows different action than subject` |
| 浦澤直樹系 | 靠分格大小變化帶出的節奏、有重量的沉默 | `long wide pause, then sudden extreme close-up of eyes`；`held silent reaction` |
| 暗黑童話作者風格 | 哥德怪誕卡通，加上高規格的電影質感 | §1 的 lock |

---

## §3 風格覆寫規則與預設集

使用者一旦指定風格，就**完全取代 §1**：
1. 重建 `art_style` lock（渲染媒材＋類型＋光線＋顆粒），控制在 30 個英文單字以內。
2. 依新風格重建配色（60-30-10 並附色碼，格式同 §1.3）、光線邏輯（§1.4）與禁用清單（§1.9）。以預設集的「禁用種子」作為起點。
3. 導演技法全數保留：範本、懸疑、藏而不露、Clip 規則。
4. 在設計假設中註明這次覆寫。

**預設集。**以預設集為起點，再依使用者的用字調整。

| 使用者說 | 美術風格 lock 種子 | 光線／配色備註 | 禁用種子 |
|---|---|---|---|
| 寫實電影感 / photoreal | `Photorealistic cinematic live-action, anamorphic lens, natural skin texture, 35mm film grain` | 有動機依據的實景光源，青綠與琥珀的冷暖分色 | 塑膠感皮膚、卡通比例、平均打平的光 |
| 日系動畫 / anime | `High-end Japanese 2D anime film, clean cel shading, painterly backgrounds` | 柔和的輪廓光、天空漸層 | 寫實皮膚、3D 算圖感 |
| 水墨武俠 / wuxia | `Chinese ink-wash wuxia film look, wide 2.39:1, desaturated ink palette, heavy atmospheric fog, vintage film grain` | 經霧氣柔化的日光；滑動變焦適合用在「踏入詭異之境」的時刻 | 飽和霓虹、現代物件 |
| 賽博龐克 / cyberpunk | `Neon-noir cyberpunk cinematic, rain-slick streets, volumetric haze` | 洋紅與青色霓虹、濕漉漉的反光 | 日景、田園配色 |
| 溫暖手繪 / cozy hand-drawn | `Warm hand-painted 2D animated film, gouache textures, soft daylight` | 黃金時刻；解除「禁用溫暖陽光」的限制 | 恐怖打光、去飽和調色 |
| 定格黏土 / claymation | `Claymation stop-motion film, fingerprint-textured clay, miniature sets` | 微縮場景的實景打光 | 光滑 CG 表面、寫實皮膚 |

lock 裡絕不寫出工作室、導演或在世藝術家的名字。

---

## §4 內容邊界

- **恐怖只用暗示：**畫外音、一道剪影、一個不對勁的影子、一面被蓋住的鏡子。絕不出現血腥、肢解或露骨的傷害畫面。
- **兒童角色**只能以暗示的方式面臨危險。絕不在畫面上呈現兒童受到傷害。
- **不使用真人肖像**，除非使用者自行提供作為參考素材。即使如此，也請參閱 `clip-assembly.md` §6 關於臉部參考的注意事項。
- 這些限制也能讓 prompt 避開影片模型的內容過濾機制。
