# 佈景知識庫——提示詞建構版（zh-TW 人類可讀版）

> 本文件為 `references/set-design-knowledge-base.md` 的繁體中文對照翻譯，僅供人類閱讀；AI 執行時不會載入本檔。英文碼段為可直接嵌入提示詞的實戰短語，保留原文並附中文釋義。

## 目錄

1. 空間即敘事——戲劇功能 → 佈景細節
2. 符號裝置——門、窗、鏡、樓梯、走廊、餐桌
3. 時代與文化真實感套件
4. 穿幫物清單
5. 鏡頭意識構圖詞彙
6. 光 × 材質互動
7. 道具即沉默台詞——角色道具套件
8. 各房間生活痕跡清單
9. 理論 → 氛圍詞彙
10. 最終品質檢查表
11. 完整範例

---

## 1. 空間即敘事

像佈景師讀劇本那樣讀需求：找的不是「地點」，而是「空間中的戲劇功能」。把每個答案編碼成物理細節。

| 面向 | 要判斷的問題 | 提示詞轉譯 |
|---|---|---|
| 階級與文化資本 | 有錢嗎？有文化嗎？在裝嗎？ | `a genuine full-grain leather chesterfield`（真皮切斯特菲爾德沙發）vs `a peeling faux-leather sofa`（脫皮仿皮沙發）；`floor-to-ceiling custom walnut bookshelves`（訂製胡桃木頂天書牆）vs `sagging flat-pack shelving`（下垂的組裝層架）；`tarnished heirloom silverware`（氧化的傳家銀器）vs `mismatched convenience-store cutlery`（不成套的便利商店餐具） |
| 心理 | 控制欲？逃避？混亂？ | `a compulsively symmetrical room, every object squared to the furniture edges`（強迫式對稱、物件對齊家具邊緣的房間）；`unopened moving boxes stacked against the wall years after the move`（搬家多年仍未拆的紙箱）；`curtains permanently drawn against daylight`（永遠拉上的窗簾）；`a wall of CCTV monitors watching every room`（監看每個房間的監視器牆） |
| 人際關係 | 親密或疏離？ | `a long dining table with two place settings at opposite far corners`（長餐桌、兩套餐具擺在對角遠端）；`a living room with no trace of shared activity`（沒有共同活動痕跡的客廳）；`a double bed divided by a wall of pillows`（被枕頭牆一分為二的雙人床） |
| 權力 | 誰支配空間？ | `a high-backed chair at the head of the table`（桌首高背椅）；`a massive desk holding visitors at a distance`（用巨大辦公桌隔出的權力距離）；`the boss's office raised half a level above the floor`（比樓面高半層的老闆辦公室） |
| 戲劇狀態 | 安全、誘惑、陷阱或審判？ | 安全：`a warm lamplit bedroom, soft bedding`（暖燈柔軟寢具的臥室）· 誘惑：`a mirrored bar glowing amber`（琥珀光的鏡面酒吧）· 陷阱：`a long narrow corridor with doors on one side only`（只有單側開門的狹長走廊）· 審判：`a vast, echoing boardroom arranged like a tribunal`（法庭式空曠會議室） |
| 角色變化 | 空間跟著人變嗎？ | 前期：`immaculate, plants thriving`（一塵不染、植物茂盛）→ 後期：`dishes piling, wilted plants, framed photos removed leaving pale rectangles on the wall`（碗盤堆積、植物枯萎、照片取下後牆上留白框） |

---

## 2. 符號裝置

經典空間符號與可嵌入短語：

- **門＝選擇**：`a door left ajar, spilling a thin blade of hallway light`（虛掩的門切出一道走廊光刃）；`a locked door with a polished, untouched brass handle`（銅把手擦亮卻從未被碰的鎖門）；`a room no one is ever seen entering`（永遠沒人進去的房間）。
- **窗＝渴望**：`a window overlooking neon-lit streets he can see but never reach`（看得見卻到不了的霓虹街景）；`iron security bars striping the daylight`（鐵欄切割日光）；`city lights smeared through rain on the glass`（雨痕暈開的城市燈火）。
- **鏡＝自我分裂**：`a cracked vanity mirror splitting the reflection`（裂痕劈開倒影的梳妝鏡）；`a three-panel dressing mirror multiplying her into strangers`（把她複製成陌生人的三面鏡）；`a mirror half-covered by a draped cloth`（被布半遮的鏡子）。
- **樓梯＝階級與心理壓力**：`a grand staircase ascending into warm light`（升向暖光的大樓梯）；`basement steps descending into cold blue shadow`（沉入冷藍陰影的地下室階梯）。
- **走廊＝過渡、監控、命運**：`an endless hospital corridor under flickering fluorescent tubes`（日光燈閃爍的無盡醫院走廊）；`a hallway lined with identical locked doors`（兩側全是相同鎖門的走道）。
- **餐桌＝家庭政治**：`an empty chair at a fully set table`（滿桌餐具中的一張空椅）；`place settings for four, only one used`（四人份餐具只動過一份）；`the father's seat at the head, oversized, facing the door`（桌首過大、面向門口的父親座位）。

---

## 3. 時代與文化真實感套件

時代感不是把「古董」塞滿，而是掌握**當時的人如何生活、購買、修補、展示自己**。每段提示詞先錨定「年代＋地域＋階級」，再部署套件。

**考證清單（必須主動指定，否則模型會預設現代）：**

| 項目 | 提示詞中要指定的 |
|---|---|
| 建築 | 門窗比例、牆面材質、天花高度、地板形式（`narrow wooden sash windows` 窄木框上下拉窗、`low stippled ceiling` 低矮灰泥頂、`worn terrazzo floor` 磨損磨石子地板） |
| 家具 | 年代、產地、階級、磨損（`a 1960s teak sideboard, veneer lifting at one corner` 一角貼皮翹起的 60 年代柚木餐櫃） |
| 家電 | 時代正確的電視、冰箱、電話、燈具、音響（`a rounded-corner CRT television` 圓角映像管電視、`a rotary-dial telephone with a tangled cord` 電話線打結的轉盤電話） |
| 生活用品 | 時代正確字體與材質的包裝、藥品、文具、報紙 |
| 衣物空間邏輯 | 當時如何收納與洗衣（`a freestanding wardrobe` 立式衣櫥、`laundry on a bamboo pole outside the window` 窗外竹竿晾衣） |
| 地域文化 | 宗教物、餐具、節慶裝飾、家庭照——維持單一文化的一致性，絕不混成泛亞洲／泛歐洲大雜燴 |
| 社會階級 | 物件新舊、修補痕跡、品牌、空間密度——窮人家不會一塵不染；富人家不該像樣品屋 |

**六組現成套件：**

- **1970年代家庭**：木紋貼皮、厚重花窗簾、玻璃煙灰缸、螺旋電話線、暖色鎢絲燈、廚房邊泛黃的花紋壁紙
- **1990年代辦公室**：米色 CRT 螢幕、吐紙中的傳真機、百葉窗、塑膠文件盤、磁片、擦不乾淨的白板筆痕
- **戰後住宅**：明顯修補的家具、全不成套、食品罐再利用、牆面水漬、摺報紙墊桌腳
- **新貴豪宅**：大片拋光大理石、挑高門廳、拍賣標籤未撕的藝術品、毫無生活痕跡
- **老錢宅邸**：家具老但比例極好、有數十年擦拭痕的銀器、書脊開裂且有鉛筆眉批的書
- **租屋族房間**：鐵網架臨時收納、一盞便宜夾燈、門後壓扁的搬家紙箱、無痕掛鉤與撕下的殘膠印

---

## 4. 穿幫物清單

繪圖模型預設「現代」。任何時代場景，都要**正面描述**下列物件的時代正確版本——沉默就等於邀請現代物入鏡：

| 風險物件 | 正面措辭修法 |
|---|---|
| 窗與框 | `period-correct wooden sash windows`（時代正確的木框窗，避免現代鋁窗） |
| 插座與開關 | `a round bakelite light switch`（圓形電木開關）、`cloth-wrapped wiring on porcelain insulators`（瓷礙子上的布包線） |
| 螢幕與照明 | `a small CRT set`（小映像管電視）、`bare tungsten bulb under an enamel shade`（琺瑯燈罩下的裸鎢絲燈）——2010 前無 LCD、無 LED 燈條 |
| 包裝與印刷 | `hand-painted shop signage`（手繪招牌）、`newspapers in period letterpress type`（活版鉛字報紙）——1980 前無條碼、2010 前無 QR code |
| 電話 | 依年代選：`rotary dial`（轉盤）、`wall-mounted payphone`（壁掛公共電話）、`a brick-sized early mobile`（黑金剛） |
| 車輛與車牌 | 窗景含街道時，指名該年代車體造型 |
| 監視器 | 只在當代／權力場景刻意出現 |

---

## 5. 鏡頭意識構圖詞彙

佈景是給鏡頭切割、壓縮、遮擋與揭露的。依距離選詞：

| 鏡頭需求 | 提示詞必須指定 | 範例短語 |
|---|---|---|
| 廣角定場 | 三層縱深 | `in the foreground a doorframe in shadow, midground the dining table under lamplight, background a rain-streaked window over city neon`（前景陰影門框、中景燈下餐桌、後景雨窗霓虹） |
| 長焦感 | 背景壓縮、圖案控制 | `telephoto compression stacking the corridor doorways`（長焦壓縮堆疊的走廊門洞）、`no stray lines crossing head height`（無雜線穿過頭部高度） |
| 特寫 | 精準微觀主體 | `a desktop scarred with cup rings and knife marks, fingerprints on the brass lamp, a lipstick stain on the rim of a cold coffee`（杯環刀痕的桌面、銅燈上的指紋、冷咖啡杯口的唇印） |
| 低角度 | 天花必須存在 | `exposed joists and a bare bulb overhead`（外露樑與裸燈泡）、`a coffered ceiling pressing down in perspective`（透視下壓的格子天花） |
| 俯拍 | 地板即構圖 | `a worn Persian rug, scattered case files and photographs arranged across the floorboards`（舊波斯地毯、散落地板的案卷與照片） |
| 框中框 | 壓迫／偷窺 | `seen through the kitchen doorway`（穿過廚房門口看）、`framed between shelving units`（被層架夾框）、`watched through the gap in a hospital curtain`（透過病房簾縫窺看） |
| 前景遮擋 | 層次 | `shot past an out-of-focus potted palm`（越過失焦盆栽拍攝）、`through rain-beaded glass`（透過雨珠玻璃）、`past a beaded curtain`（越過珠簾） |

**構圖衛生**：水平線、牆線、窗框線避開人物頸部與頭部；背景支持故事、絕不變成展覽；預留角色走位與呼吸空間。

---

## 6. 光 × 材質互動

材質就是曝光決策。每段提示詞至少指名兩種材質，並說明光如何打在上面。

| 材質 | 鏡頭特性 | 提示詞措辭 |
|---|---|---|
| 亮面金屬 | 高反光熱點 | `softly aged brushed steel catching a dull gleam`（微舊化髮絲紋鋼面泛出鈍光） |
| 玻璃 | 穿透＋反射雙重 | `the window doubling the room as a faint reflection over the neon outside`（窗玻璃在霓虹外景上疊出室內淡影） |
| 深色木頭 | 吃光、質感沉穩 | `edge light raking across walnut paneling, pulling out the grain`（側緣光掠過胡桃木板拉出木紋） |
| 白牆 | 反光強、易扁平 | `off-white walls with faint water stains and a warm color cast, never a flat studio white`（帶水漬與暖色偏的米白牆，絕非攝影棚死白） |
| 布料 | 吸光、柔化 | `heavy velvet drapes swallowing the lamplight`（吞掉燈光的厚絨簾）、`sun-faded cotton curtains breathing at an open window`（開窗邊呼吸的曬褪棉簾） |
| 塑膠 | 廉價硬反光 | `glossy molded-plastic chairs under flat fluorescent light`（平板日光燈下的亮面塑膠椅）——便利店、診所、廉租空間 |
| 石材／大理石 | 冷、硬、權力 | `veined marble reflecting cold daylight`（映冷日光的紋理大理石）——過量會像飯店大廳，節制使用 |
| 水泥 | 粗糙、壓迫、現代 | `raw concrete with damp patches and hairline cracks`（帶濕痕與髮絲裂的清水模）——避免死灰 |

**燈光原則：**

- **只用合理實用燈**——每道光都存在於世界內：`a green-shaded banker's lamp`（綠罩銀行燈）、`the blue flicker of a television`（電視藍閃）、`the cold spill of an open refrigerator`（冰箱開門冷光）、`buzzing neon signage bleeding through the blinds`（滲過百葉的嗡嗡霓虹）、`passing headlights sweeping the ceiling`（掃過天花的過路車燈）。
- **窗戶是光的敘事**：`first gray light of dawn`（黎明灰光）、`low amber sunset`（低角度琥珀夕陽）、`pulsing red-and-blue police strobe`（紅藍警燈脈動）、`a single lightning flash freezing the room`（一道閃電凍結房間）。
- **色溫＝心理**：暖鎢絲光 → 親密、懷舊或腐敗；冷日光燈／天光 → 醫療、孤立、科技、審判。
- **做舊要分層**，不是刷一層髒：`dust on the upper shelves, grease shadowing the stove wall, worn varnish on the chair arms, sun-faded curtains, one mended crack in the window`（高架灰塵、灶牆油影、扶手磨漆、曬褪窗簾、一道修補過的窗裂）。
- **類型表面**：恐怖 → `wet-sheen surfaces`（濕亮表面）；喜劇 → `clean saturated color blocks, even light`（乾淨飽和色塊、均勻光）；犯罪 → `desaturated palette, rough matte surfaces`（低彩度、粗糙霧面）。

---

## 7. 道具即沉默台詞

道具是角色的無聲台詞——觀眾應在一秒內讀懂這個人。原型套件：

| 原型 | 道具套件 |
|---|---|
| 控制型母親 | 每個罐子都有標籤機貼紙、好家具套塑膠套、完美對齊的餐具組、七日藥盒、大孩子房裡仍在運作的嬰兒監視器 |
| 失意作家 | 桌邊空酒瓶、一抽屜退稿信、便利貼下的舊打字機、沒洗的馬克杯森林 |
| 黑幫老大 | 桌上方的宗教像、面向訪客的家庭照、雪茄保濕盒、拉緊的厚窗簾、重得能擋子彈的辦公桌 |
| 科技新貴 | 極簡家具、每個檯面都有智慧音箱、無線充電板、昂貴卻沒有記憶的空間 |
| 老教授 | 折角書頁、手寫卡片、用了數十年的檯燈、吸墨紙上的茶漬圈、層層堆疊的文獻 |
| 獨居老人 | 流理台上的藥袋、停在多年前的月曆、塑膠花、膠帶修補的家具、橡皮筋纏繞的遙控器 |
| 青少年 | 樂團海報、球鞋盒塔、床上的耳機、寫到一半的作業、一格明顯私密的抽屜 |
| 逃亡者 | 成捆現金、攤開的地圖、一疊假證件、還在吊卡裡的拋棄式手機、邊緣用膠帶封死的遮光簾 |

---

## 8. 各房間生活痕跡清單

觀眾不會逐一檢視道具，但會**感覺**空間是否被生活過。每段提示詞取 ≥3 處；每個物件都要有使用邏輯。

- **廚房**：灶後油漬影 · 冰箱磁鐵壓著舊收據 · 櫃子深處過期罐頭 · 磨出主人握痕的刀 · 水槽邊那只常用杯
- **浴室**：水龍頭底座水垢 · 牙刷數量（數量＝故事）· 鏡櫃裡的藥 · 桿上微濕毛巾 · 鏡緣霧痕
- **臥室**：睡哪一側看得出來 · 蜿蜒到枕邊的充電線 · 面朝下的半讀書 · 堆滿穿過一次衣物的椅子 · 一件被慎重擺放的私人物
- **辦公桌**：歸檔與漂流的文件 · 像年輪疊加的咖啡漬圈 · 吸墨紙上的筆壓痕 · 爬滿螢幕邊框的便利貼
- **玄關**：鞋子的排列方式（或沒有排列）· 鑰匙盤 · 滴水的傘 · 未拆信件 · 按季節疊掛的外套
- **車內**：車門置物格的停車票根 · 有餅乾屑的兒童座椅 · 用滿出的煙灰缸交代菸味 · 後照鏡吊飾 · 副駕腳踏墊上揉成團的速食袋

---

## 9. 理論 → 氛圍詞彙

| 理論／美學 | 核心概念 | 提示詞應用 |
|---|---|---|
| 亞里斯多德戲劇結構 | 場景服務情節推進 | 讓佈景跟著幕次走：`open and airy`（開放）→ `tightening`（緊縮）→ `disordered`（崩解）→ `emptied out`（清空） |
| 斯坦尼斯拉夫斯基 | 規定情境、心理真實 | 房間必須讓人相信真的有人住——習慣處處可見 |
| 布萊希特 | 間離效果、讓觀眾思考 | `deliberately exposed stage rigging, painted flat backdrops, visible slogans`（故意外露的燈架、繪景平片、可見標語）——自知的劇場感 |
| 自然主義 | 社會條件決定人物 | 階級、職業、家庭制度全由物質細節承載 |
| 表現主義 | 空間外化心理 | `walls leaning at uneasy angles, doorways stretched tall and narrow, shadows grown monstrous`（不安傾斜的牆、拉高變窄的門洞、長成怪物的陰影） |
| 象徵主義 | 物件承載隱喻 | `withered flowers, a cracked mirror, an empty birdcage, a room upholstered entirely in red, a window that does not open`（枯花、裂鏡、空鳥籠、全紅房間、打不開的窗） |
| 符號學 | 所有物件都是可讀符號 | 品牌、顏色、位置、材質＝觀眾潛意識讀到的句子 |
| 場面調度 | 人、物、光、鏡頭的關係 | `the patriarch framed at the head of the table`（被框在桌首的家長）、`her chair angled toward the exit`（朝向出口的她的椅子）、`a figure boxed in by doorframes`（被門框困住的人） |
| 空間權力理論 | 空間分配階級與支配 | `a raised platform office`（高台辦公室）、`glass-walled cubicles under an overseer's window`（監工窗下的玻璃隔間）、`a surveillance-camera viewpoint`（監視器視角） |
| 電影黑色美學 | 道德混濁與陰影世界 | `venetian-blind shadows slicing the desk, wet asphalt mirroring neon, smoke hanging in a low-ceilinged room`（百葉窗影切割桌面、濕柏油映霓虹、低天花下懸浮的煙） |

**定稿前三句檢查**：這個空間是否揭露角色不能說出口的東西？是否給導演與攝影可調度的層次？是否讓觀眾在理解劇情前先感覺到情緒？

---

## 10. 最終品質檢查表

每組三提案逐條過，不及格就修：

1. 時代、地域、階級、文化正確且一致？
2. 有生活痕跡——被生活過，不是美術陳列？
3. 縱深層次明示——前景、中景、後景？
4. 三種距離都成立——遠景、中景、特寫？
5. 零穿幫——窗、插座、螢幕、字體、包裝、車牌、監視器？
6. 每件道具都有「為什麼在那裡」？
7. 材質在指定光線下仍可信？
8. 空間暗示了關係、權力與心理？
9. 光都有來由——每個光源存在於世界內？
10. 觀眾不會「注意」佈景，卻會被佈景影響？

佈景的本質：把不可見做成可見——記憶、階級、慾望、創傷、秩序、崩壞。成熟的佈景不是背景，而是戲的一部分。

---

## 11. 完整範例

**需求**：「1990年代台北，一個失意私家偵探租的公寓，犯罪片氛圍」

**設計聖經（內部）**：90 年代台北無電梯公寓 · 租屋階級、前警察的自尊在腐蝕 · 色盤：菸垢琥珀 vs 霓虹青 · 光源：一盞銀行燈＋百葉縫霓虹 · 主角道具：案卷牆、滿出的煙灰缸、轉盤電話 · 潛台詞：不再相信卻停不下來的男人 · 犯罪類型的低彩度粗糙表面。

（英文提示詞原文見 `references/set-design-knowledge-base.md` §11；中景提案移到辦公桌與沙發的關係——案卷即沉默台詞、一張從沒人坐的訪客椅；特寫提案在燈的邊光下解析煙灰缸、杯漬圈、與釘在案卷之間的一張照片——同色盤、同兩個光源、同時代錨點，逐字重複。）
