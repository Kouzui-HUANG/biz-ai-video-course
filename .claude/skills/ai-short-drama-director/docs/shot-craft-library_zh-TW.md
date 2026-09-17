# 分鏡技巧庫（繁中對照）

> `references/shot-craft-library.md` 的中文對照版，僅供人閱讀。英文 prompt 片語、YAML、標籤維持原文，因為那是實際要餵給模型的文字。

用於第 5 步。目錄：
- §1 十欄分鏡表規格
- §2 敘事目的
- §3 鏡頭組與漫畫分格邏輯
- §4 分割畫面／畫中畫
- §5 動作–反應變體
- §6 技巧庫（含 prompt 片語）
- §7 景別 ↔ 情緒
- §8 運鏡 ↔ 意義
- §9 荷蘭角與 dolly zoom
- §10 懸疑構建
- §11 意象疊加

「**Prompt 片語**」欄是要填進 `type` / `action_prompt` 的電報式英文。片名和導演名字絕對不可以寫進 prompt。

---

## §1 十欄分鏡表規格

| 欄位 | 內容 | 範例 |
|---|---|---|
| 鏡 | 從 1 開始連續編號（跨 Clip 全片統一） | 1, 2, 3 |
| 時長 | 全片時間碼 | 00:00–00:04 |
| 角度 | 垂直角度 | 平視／俯拍／仰拍／頂拍／微俯 |
| 景別 | 景別大小 | 大遠景／遠景／全景／中景／近景／特寫／大特寫 |
| 畫面內容 | 只寫看得見的動作 | 女孩提燈走過荊棘小徑 |
| 場景 | 空間／場景代號 | L1 荊棘林 |
| 聲音 | 所有聲音元素 | 環境風聲；蛾翅拍動 |
| 備註 | 運鏡、技巧、特效（VFX）、字幕提示 | 慢推；前景懸疑 |
| 敘事目的 | 目的標籤＋一句話理由 | 建立｜交代空間與燈的設定 |
| Clip | 於第 6 步回填 | C1 |

**畫面內容的寫法：**
- 只寫看得見的東西，絕不寫心理狀態。
- 關鍵道具要明確點名。
- 用動作句，不用狀態句。
  - ✔ 「她把燈舉高」
  - ✘ 「她很害怕」

---

## §2 敘事目的

敘事目的是*這個鏡頭為什麼非得在此刻出現*，而不是「因為好看」。
**反覆自問：**這個鏡頭是為了什麼？答不出來，就刪掉或併進別的鏡頭；答得出來，再問有沒有別的鏡頭更能達成這個目的。

| 標籤 | 意義 | 典型用法 |
|---|---|---|
| 建立 Establish | 交代空間、時間或氛圍 | 開場鏡頭、環境介紹 |
| 推進 Advance | 推動劇情 | 動作與反應鏡頭 |
| 揭示 Reveal | 關鍵資訊浮上檯面 | 發現證據、真相揭露 |
| 強調 Emphasize | 加重某個瞬間的份量 | 高潮表情、關鍵道具 |
| 轉場 Transition | 銜接兩場戲 | 空鏡、過場橋段 |
| 情緒 Emotion | 承載情感而非資訊 | 慢動作、定格、延長停留 |
| 內省 Reflect | 把內心世界外化 | 倒影、主觀鏡頭 |

---

## §3 鏡頭組與漫畫分格邏輯

**鏡頭組類型：**
- **蒙太奇（Montage）：**多個畫面快速剪接，每個 1–3 秒。這類鏡頭必須打包進同一個 Clip（見 `clip-assembly.md` §3）。
- **遞進式：**每個鏡頭都補上新資訊，或把情緒再推高一層。
- **因果式：**動作 → 反應。
- **對比式：**讓畫面彼此對照。

**漫畫分格邏輯轉譯成影像：**

| 分格手法 | 意義 | 影像對應做法 |
|---|---|---|
| 大格 | 強調、停頓 | 更廣或更緊的極端景別，再加上較長的停留（3–5 秒） |
| 小格 | 速度、急迫 | 多鏡頭 Clip 裡的短鏡頭（1.5–2 秒） |
| 斜格 | 失衡 | 荷蘭角（§9） |
| 圓形格 | 聚焦、主觀 | `iris vignette POV`、`seen through keyhole / telescope` |
| 人物身體越出格線 | 連結兩個空間 | 以動作做匹配剪接，或用 `body wipe` 轉場 |

---

## §4 分割畫面與畫中畫

影片模型不太會直接畫出分割畫面，所以改用畫面世界裡本來就有的等效手法：
- **同時呈現**（平行的空間或視角）→ `split by architecture: doorframe divides left room and right room`
- **巢狀視角**（主畫面裡還包著一個次畫面）→ `image-in-image via mirror / TV screen / window reflection showing second figure`
- **觀眾知道、角色不知道** → 把威脅放在次畫面裡：`in mirror behind her, shadow rises; she faces camera unaware`

---

## §5 動作–反應 12 變體

基本單位：一個動作（行為）鏡頭＋一個反應（結果）鏡頭。

| # | 變體 | 模式 | 用途 |
|---|---|---|---|
| 1 | 標準型 | 動作 → 反應 | 最基本的因果 |
| 2 | 先反應 | 反應 → 動作 | 製造懸念 |
| 3 | 動作堆疊 | A + B + C → 反應 | 累積壓力 |
| 4 | 省略反應 | 動作 →（無） | 為最重要的時刻留白 |
| 5 | 隱藏動作 | （動作的聲音）→ 畫面上的反應 | 聲畫分離 |
| 6 | 延遲反應 | 動作 → 日常 → 反應 | 寫實感 |
| 7 | 同步型 | 動作與反應同框 | 提高資訊密度 |
| 8 | 反應連鎖 | 動作 → A → B → C | 呈現影響所及的範圍 |
| 9 | 重複漸變 | 動作 → 反應 → 同一個動作，但略有變化 | 時間流逝 |
| 10 | 對位 | 畫面動作＋與之矛盾的聲音 | 揭露矛盾 |
| 11 | 省略動作 | 反應 → 反應 → 反應 | 關鍵事件始終留在畫外 |
| 12 | 環環相扣 | A 的反應變成 B 的動作 | 骨牌式推進 |

---

## §6 技巧庫（含 prompt 片語）

★ = 優先精熟程度，沿用原始資料的評分。

### 構圖（12）

| 技巧 | 參考作品 | ★ | 用途 | Prompt 片語 |
|---|---|---|---|---|
| 視線空間／心理空間 | *The Godfather*（教父） | ★★★★★ | 對話、情緒 | `off-center subject, wide lead room in gaze direction` |
| 框中框 | *In the Mood for Love*（花樣年華） | ★★★★★ | 分隔、疏離 | `framed through narrow doorway, walls crowd edges` |
| 對稱與打破對稱 | *The Shining*（鬼店）、*2001*（2001太空漫遊） | ★★★★★ | 壓迫感、儀式感 | `one-point perspective, perfect bilateral symmetry` / `symmetry broken by lone figure off-axis` |
| 留白（負空間） | *The Revenant*（神鬼獵人）、*2001* | ★★★★★ | 極簡、空白的情緒 | `tiny figure, vast empty negative space` |
| 引導線 | *Citizen Kane*（大國民） | ★★★★ | 營造縱深、引導視線 | `converging lines lead to subject` |
| 三分法 | *The Queen's Gambit*（后翼棄兵） | ★★★ | 基礎構圖 | `subject on right third` |
| 環境細節＋意象 | 描述性建立鏡頭 | ★★★★ | 暗示情緒、時間流逝 | `macro of melted candle stubs, dust on untouched plate` |
| 荷蘭角 | *Psycho*（驚魂記）、*Batman*（蝙蝠俠） | ★★★★ | 失衡 | `dutch angle 20°`（見 §9） |
| 眼部特寫 | 分鏡教學 | ★★★★ | 情緒焦點 | `extreme close-up eyes, reflection in iris` |
| 景深 | *Citizen Kane*、*Barry Lyndon*（亂世兒女） | ★★★★ | 清晰與柔焦的對比 | `deep focus, foreground and background sharp` / `shallow focus, background dissolves` |
| 漸進距離 | 分鏡基礎 | ★★★★ | 情緒堆疊或釋放 | 鏡頭逐步收緊：遠景 → 中景 → 特寫 |
| 漫畫式不對稱分格 | 今敏／浦澤直樹一脈 | ★★★★ | 情緒外化、節奏 | 見 §3 |

### 運鏡（10）

| 技巧 | 參考作品 | ★ | 用途 | Prompt 片語 |
|---|---|---|---|---|
| 推軌（推近） | *The Shining* | ★★★★★ | 堆疊情緒、聚焦 | `slow dolly push-in` |
| 拉鏡 | *Goodfellas*（四海好傢伙）、*Once Upon a Time in the West*（狂沙十萬里） | ★★★★★ | 空間展開、揭示 | `slow pull-back reveals surroundings` |
| 跟拍橫移 | *1917*、*Birdman*（鳥人） | ★★★★★ | 跟隨、臨場感 | `lateral tracking alongside subject` |
| 手持 | *Saving Private Ryan*（搶救雷恩大兵）、*Black Swan*（黑天鵝） | ★★★★ | 寫實、緊張 | `handheld, subtle shake, breathing camera` |
| 升降 | 分鏡基礎 | ★★★★ | 權力關係轉移、空間變化 | `crane up from ground to high angle` |
| 搖鏡 | 分鏡基礎 | ★★★ | 展示空間 | `slow pan left across room` |
| 長鏡頭與短鏡頭的節奏 | *Gravity*（地心引力）、*The Bourne Ultimatum*（神鬼認證：最後通牒） | ★★★★ | 節奏變化 | 先來一段一鏡到底的長鏡頭，再接快速剪接 |
| 快速剪接 | *The Bourne Identity*（神鬼認證）、*Mad Max: Fury Road*（瘋狂麥斯：憤怒道） | ★★★★ | 緊張、衝擊 | `rapid cuts, 1-second shots`（僅限蒙太奇） |
| 慢動作與正常速度 | *The Matrix*（駭客任務）、*The Girl Who Leapt Through Time*（跳躍吧！時空少女） | ★★★★ | 放大情緒、拉長時間 | `slow motion, drifting particles` |
| Dolly zoom | *Vertigo*（迷魂記）、*Jaws*（大白鯊） | ★★★★★ | 暈眩、心理扭曲 | 見 §9 |

### 鏡頭銜接（8）

| 技巧 | 參考作品 | ★ | 用途 | Prompt 片語 |
|---|---|---|---|---|
| 視線匹配 | *Psycho*、*Rear Window*（後窗） | ★★★★★ | 視線 → 物件 | `she looks off-frame left` → 下一鏡 `POV of object` |
| 過肩鏡頭（OTS） | *Citizen Kane*、*12 Angry Men*（十二怒漢） | ★★★★ | 對話 | `over-the-shoulder from behind S1` |
| 反應鏡頭 | *Jaws*、庫勒雪夫 | ★★★★★ | 放大情緒 | `hold on face, reacting to off-screen event` |
| 插入鏡頭 | *The Godfather*、*Rocky*（洛基） | ★★★★ | 強調細節 | `insert close-up of key in palm` |
| 越軸（刻意為之） | *The Shining*、*Citizen Kane* | ★★★★ | 製造緊張、打破規則 | `reverse angle across axis, screen direction flips`（在備註中標明） |
| 場景銜接 | 分鏡基礎 | ★★★ | 轉場流暢 | 讓顏色、形狀或聲音延續、跨過剪接點 |
| 景別＋鏡長的節奏 | 分鏡基礎 | ★★★★ | 節奏設計 | 遠景／長鏡與特寫／短鏡交替出現 |
| 定格強調 | *Thelma & Louise*（末路狂花）、*Bonnie and Clyde*（我倆沒有明天） | ★★★ | 關鍵瞬間 | `motion halts, near-frozen frame, only dust drifts` |

### 轉場（6）

| 技巧 | 參考作品 | ★ | 用途 | Prompt 片語 |
|---|---|---|---|---|
| 圖形匹配 | *2001* | ★★★★★ | 視覺奇觀 | `end on round moon` → 下一鏡 `open on round clock face` |
| 劃接／遮擋 | *October*、*Decisive Engagement* | ★★★★ | 切換空間 | `dark foreground object passes lens, wipes to next scene` |
| 淡出淡入 | *Braveheart*（英雄本色）、*Shawshank*（刺激1995） | ★★★ | 情緒過渡 | `fade to black` / `candle snuffed to black` |
| 動作匹配剪接 | *Crash*、*Forrest Gump*（阿甘正傳） | ★★★★ | 時空跳躍 | `hand turns key — cut — same hand older, same motion` |
| 聲音橋接 | *Apocalypse Now*（現代啟示錄）、*The Godfather* | ★★★★★ | 聲音延續到下一場 | `audio_prompt: [SFX] pre-lap: church bell from next scene` |
| 交叉剪接 | *The Godfather*、*Inception*（全面啟動） | ★★★★ | 兩條動作線並行 | 在兩個地點之間交替切換 Clip 或鏡頭 |

### 主觀／客觀（4）

| 技巧 | 參考作品 | 用途 | Prompt 片語 |
|---|---|---|---|
| POV | *Psycho*、*Rear Window* | 讓觀眾化身為角色 | `first-person POV, hands visible at frame bottom` |
| OTS | *Citizen Kane*、*The Social Network*（社群網戰） | 建立人物關係 | `over-the-shoulder` |
| 反應鏡頭 | *Jaws*、*North by Northwest*（北西北） | 放大情緒 | `reaction close-up` |
| 插入鏡頭 | *There Will Be Blood*（黑金企業） | 強調細節 | `insert macro` |

### 懸疑與張力（5）

| 技巧 | 參考作品 | 用途 | Prompt 片語 |
|---|---|---|---|
| 前景懸疑 | *The Lady Vanishes*、*Psycho* | 延遲型懸念 | `threat object sharp in foreground, unaware subject soft behind` |
| 危險區固定鏡頭 | *Psycho* | 緊張對峙 | `camera settles, locked-off static, action enters frame` |
| 軸線混亂 | *Psycho*（浴室那場戲） | 恐慌、驚駭 | `disorienting angles, broken screen direction, fragmented cuts` |
| 對稱壓迫 | *The Shining*、*2001* | 肅穆的恐懼 | `dead-center symmetry, long corridor, slow steady track` |
| 跳接 | *Breathless*（斷了氣）、*Breaking Bad*（絕命毒師） | 壓縮時間 | `jump cut, same frame, subject shifts position` |

### 特殊手法（3）

| 技巧 | 參考作品 | 用途 | Prompt 片語 |
|---|---|---|---|
| 分割畫面 | *Dragnet*、*Crash* | 多線敘事 | 改用建築物來分割畫面（§4） |
| 畫中畫 | 今敏一脈、*Perfect Blue*（藍色恐懼） | 巢狀視角 | `mirror / screen shows second scene` |
| 分割＋畫中畫 | 今敏一脈 | 複雜敘事 | 用門框分割畫面，其中半邊再放一面鏡子 |

---

## §7 景別 ↔ 情緒（景別與情緒）

| 景別 | 英文 | 距離感 | 情緒傾向 | 用途 |
|---|---|---|---|---|
| 大遠景 | extreme wide | 疏離、神聖 | 敬畏、渺小 | 開場、宿命感 |
| 遠景 | wide | 旁觀者 | 客觀、冷靜 | 交代環境、告別 |
| 全景 | full shot | 人物＋環境 | 敘事上的平衡 | 完整動作、空間 |
| 中景 | medium | 社交距離 | 日常、對話 | 互動 |
| 近景 | medium close-up | 個人距離 | 親近、專注 | 情緒細節、道具 |
| 特寫 | close-up | 親密距離 | 強烈、壓迫或脆弱 | 表情高峰、關鍵物件 |
| 大特寫 | extreme close-up | 極度聚焦 | 窒息、侵入感 | 心理極限、衝擊 |

---

## §8 運鏡 ↔ 意義（運鏡與敘事）

| 運鏡 | 英文 | 意義 | 典型用法 |
|---|---|---|---|
| 推 | dolly in | 靠近、審視、揭露 | 下定決心、發現真相 |
| 拉 | dolly out | 抽離、逃避、揭示環境 | 結尾、揭示 |
| 橫移／搖 | track / pan | 穿越空間、旁觀者視角 | 跟隨、掃視 |
| 升降 | crane / jib | 上帝視角、啟示、告別 | 開場、命運轉折 |
| 旋轉 | orbit / roll | 暈眩、失控、浪漫 | 酒醉、浪漫、恐慌 |
| 主觀 | POV | 讓觀眾化身為角色 | 沉浸感、恐懼、慾望 |
| 靜止 | locked-off | 冷靜凝視、等待、壓抑 | 審問、對峙凝視、暴風雨前的寧靜 |

---

## §9 荷蘭角與 dolly zoom

**荷蘭角分級：**
- **輕微，5–10°：**隱約的不安。片語：`slight dutch tilt`
- **中等，15–30°：**明顯的失衡。片語：`dutch angle 20°`
- **極端，45° 以上：**崩潰、夢魘。片語：`extreme 45° canted frame`

**Dolly zoom（希區考克變焦）。**攝影機移動與焦距朝相反方向變化：主體大小維持不變，背景透視卻隨之扭曲。觀眾會感受到空間扭曲、心理暈眩，或整個世界正在崩塌。
- **後拉＋變焦推近：**背景向外擴展。片語：`dolly out while zooming in, background stretches away, subject fixed center`
- **前推＋變焦拉遠：**背景被壓縮。片語：`dolly in while zooming out, background rushes forward, subject fixed center`
- **不限風格的通用模板：**`dolly zoom, subject locked center frame, background perspective warps, [style lock], [light lock]`
- **使用時機：**踏進詭異世界的那一刻、發現駭人真相之時，或原本穩定的心理狀態瓦解的瞬間。每部片最多用一次。

---

## §10 懸疑構建

- **前景懸疑：**把關鍵道具放在前景。觀眾知道、角色不知道，於是由構圖而非台詞來承載線索。`threat in sharp foreground, subject unaware in soft background`
- **危險區固定鏡頭：**攝影機先移進危險區 → 關鍵動作發生時鎖定不動 → 再移開。在多鏡頭 Clip 裡，這會拆成三個鏡頭：`track into doorway` → `locked-off static` → `slow drift away`。

---

## §11 意象疊加

用意象取代直白的陳述：
- 桌燈暗到只剩一枚硬幣大小 → 夜有多長。
- 蒸氣凝結在睫毛上 → 母親從不說出口的愛。
- 牛奶杯上的一枚指紋 → 關鍵的劇情暗示。

**預設風格意象庫：**
- 飛蛾繞著熄滅的蠟燭打轉 → 希望逐漸耗盡。
- 停擺的時鐘，指針卻微微抽動 → 無限循環。
- 被遮起來的鏡子 → 遭到否認的身分。
- 縫線補過的娃娃 → 舊傷。
