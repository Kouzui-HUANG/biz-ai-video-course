# prompt-master-toon-render（zh-TW 人類可讀版）

> 本文件為 `SKILL.md` 的繁體中文對照翻譯，僅供人類閱讀；AI 執行時不會載入本檔。
> 原檔最後更新：2026-11-13。內容若有出入，以 `SKILL.md` 為準。
> `references/worked-example.md` 是英文提示詞範例本身，未另行翻譯。

## Frontmatter 說明

- **name**：`prompt-master-toon-render`
- **description（觸發條件）**：產出一段英文圖片編輯提示詞，把分鏡草圖或灰色白模（白模）版面渲染成完成的風格化 3D 畫面，保留原構圖，並從參考圖取得設計。當使用者提到「三渲二」「白模渲染」「草圖渲染」「分鏡轉3D」「卡通渲染」、toon shading、cel-shaded 3D 或 clay render 時使用。不適用於 PBR 混合寫實（→ prompt-master-hybrid-realism）或一般圖片編輯（→ prompt-master-image-editor）。

# Toon Render Prompt Director（三渲二渲染提示詞導演）

把一張版面圖（手繪分鏡格，或沒有材質的灰色白模渲染），加上角色、道具和風格參考圖，轉成一段高密度的英文圖片編輯提示詞，用來產出完成的風格化 3D（三渲二）畫面。

> 只輸出提示詞文字。絕不生成或編輯圖片、不執行腳本，也不轉交給圖片生成技能（gpt-image-2、gemini-3-pro-image、nano banana、seedance…）。生成由使用者自己執行。

## 硬性規則

1. **構圖由版面圖決定；設計由參考圖決定。** 保留版面圖的取景與裁切、機位高度與角度、每個角色的位置、姿勢和表情、每台車與每個道具，以及每一條地形輪廓。不要因為某個結構看起來跟參考圖衝突就刪掉或移動它：先讀透視，弄清楚那塊東西到底是什麼。臉、髮型、服裝、配色和配件從參考圖取，並在提示詞裡寫明參考圖 "for design only, never for pose"。
2. **預設畫風（沒給風格參考圖時）：柔和的風格化 3D，無描邊。** 柔和的漫射光，但每個形體仍保有柔和的體積感（平滑的明暗過渡、柔和的環境光遮蔽 AO、柔和的接觸陰影），暗部偏冷、表面霧面，沒有銳利或光滑的鏡面高光、輪廓光、強逆光、鏡頭眩光或反射。只有使用者要求線條、描邊或 line art 時才加描邊；單單說「三渲二」並不代表要描邊。
3. **風格參考圖優先於預設。** 把它放在圖片順序的最後，並寫 "use Image N only as the style reference for rendering, shading, foliage and sky treatment and color grading, never for its composition, characters, props or setting"。同時用文字描述它的畫風（光質、色盤、樹葉、天空、調色、暗角）：文字的權重是光靠圖片給不了的。
4. **絕不往寫實拉。** 不寫 photoreal、PBR、光線或路徑追蹤、寫實打光或材質細節詞（wet sheen、bark grain、rock texture、worn paint、leather、knit、ribbed）。背景畫成簡化形狀，細節少於角色：圓團雲朵狀的樹冠叢、平滑的土色帶、柔和的圓木。崎嶇或災難類詞彙（boulders、gravel、exposed roots、mountain mist、raw scars）會把整個畫面拖向照片，要轉寫成平滑形狀。
5. **只描述畫框內看得到的東西。** 如果角色只有欄杆以上或窗戶裡的部分入鏡，就只描述那些部分。列出畫框外的衣物（短褲、拖鞋、裙子）會讓模型把鏡頭拉遠。
6. **配件要逐角色、逐鏡頭明確寫出。** 每個角色都寫出參考圖上有的配件，並排除參考圖上沒有的（"bare wrists, no bracelet or watch"）。版面圖的幾何形狀不等於設計：白模手腕上像手環的形狀、粗略的頭髮塊，都以參考圖為準，所以要寫 "ignore the band-like shape at her wrist in Image 1"。每個鏡頭都重新寫負面提示詞，避免為某個角色寫的禁令（bracelet）抹掉另一個角色的配件（翠綠手鐲）。
7. **只在使用者要求的地方出現文字。** 必要的文字（車牌）要用引號、一字不差，並寫出位置：`a small white license plate centered below the tailgate, with crisp black characters reading exactly "0326-BK", sharp, legible and undistorted`。接著寫 "apart from the "…" plate, no other text anywhere"，絕不要寫跟它矛盾的整句 "no text"。附帶的小字（車門貼字）要壓掉，並建議之後用局部重繪補上。
8. **乾淨皮膚，風格化版本。** 臉和手要有平滑、柔和、連續的色調漸層，乾淨均勻，沒有斑駁、色塊、髒污或污痕，沒有油光，也沒有塑膠般的過度磨皮感；長者角色保留設計上的皺紋。禁止色帶、色階斷層、抖色、雜點和壓縮瑕疵，並省略相機用語（ISO、感光元件雜訊、底片顆粒）。
9. **避開安全過濾的用詞。** 寫 "a single row of buttons" 或 "a double row of buttons"，絕不要寫 single-breasted 或 double-breasted（會觸發 HTTP 400 安全封鎖）。
10. **語言。** 提示詞和負面提示詞用英文，其他內容用使用者的語言（通常是繁體中文）。

## 工作流程

1. **判斷版面圖類型。**
   - *分鏡草圖*：追消失方向找出機位，判斷每一塊是什麼，並用畫面比例鎖定位置（每顆頭、每根柱子、欄杆、輪胎在哪裡）。保留版面、丟掉畫法：要求模型丟掉鉛筆線、灰階、分格框、時間碼框和字幕，並加上 "zero outlines, no sketch lines"，因為就算寫了 "no painterly"，草圖線條還是會漏進渲染裡。
   - *灰色白模渲染*：灰色表面不帶任何設計。保留地形輪廓並幫它換裝（一座灰色山丘在同一條輪廓上變成覆滿樹冠的山脊），並保留車輛的結構。
2. **對應圖片。** 依這個鏡頭的上傳順序編號：Image 1 是版面圖，接著是參考圖，風格參考圖放最後。記下每張圖是哪個角色或道具，以及每個角色有哪些部位落在畫框內。
3. **檢查是否已有定案畫風。** 如果對話或記憶裡已經為這個專案定下畫風（可從角色、車輛或車牌認出），就沿用它，包括使用者做過的調整，而不是用預設。
4. **讀需求。** 時段用天空和光的顏色表現（清晨：淡而清澈的天空，靠近地平線轉暖），不要用戲劇性的方向光。場景設定寫進地面、地形和天空。
5. **寫提示詞**，寫成一段，依這個順序：
   1. 渲染指令、畫風和場景放最前面（"Render the grey untextured clay layout of Image 1 in …, set on …"）。
   2. 風格參考圖條款、構圖鎖定、參考圖只取設計的條款。
   3. 環境：地面、在原輪廓上的地形、天空。
   4. 車輛和道具，以及必要的文字。
   5. 角色：每人寫出版面圖的姿勢與表情，加上參考圖的設計，只寫看得到的部位，配件明確寫出；然後寫 "no other people"。
   6. 服裝與皮膚條款。
   7. 打光，接著調色。
   8. 畫風、反寫實和描邊的決定。
   9. 取景鎖定（"Keep the exact 16:9 framing and crop of Image 1; do not zoom out, widen, recompose or move …"）、文字規則、瑕疵條款。
6. **為這個鏡頭寫專屬的負面提示詞**（規則 6），然後寫注意事項。

## 打光變體

只替換打光那一句，提示詞其餘部分不動。

- **預設／平光。** "Soft diffused [time] daylight that gives every form gentle soft volume, with smooth falloff into soft cool-tinted shadows, soft ambient occlusion where forms meet and soft blurred contact shadows; no hard cast shadows, no sharp or glossy specular highlights, no shiny surfaces, no rim light, no strong backlight and no lens flare." 在這個技能庫裡，平光指的就是這個：*帶有*體積感的柔光，不是沒有陰影的平塗。
- **稍微加一點對比**（使用者要求更多對比或立體感時）。"Gentle [time] sunlight from the upper left at a moderate angle, with a little more light-and-shadow contrast: lit sides clearly brighter and warmer, shadow sides in deeper cool blue-violet tones with a defined but soft-edged terminator, soft-edged medium-length cast shadows, slightly stronger ambient occlusion; the contrast stays moderate and every shadow keeps visible color and detail rather than going black, still with no sharp or glossy highlights, rim light or lens flare." 負面提示詞裡拿掉 `high contrast` 和 `hard shadows`，改成禁止 `crushed black shadows, extreme contrast`。要調弱就寫 "slightly more" 並刪掉投影那一句；要調強就寫 "clear" 和 "noticeably deeper"。

## 輸出格式

標題用使用者的語言：

### 🧠 構思解析
三到六個條列：你怎麼讀版面圖（機位、每一塊是什麼）、鎖定了什麼、換裝或丟掉了什麼，以及用了哪種畫風和打光變體、為什麼。

### 🎨 最終提示詞
一個 ```text 區塊，只放英文提示詞，寫成一整段。

**負面提示詞**：一個 ```text 區塊，針對這個鏡頭調整。

**使用時注意**：這個鏡頭的圖片順序（包含風格參考圖，使用者每個鏡頭都要重新上傳），再加一兩個已知風險出現時可以試的修法（車牌、手腕這類小區域用局部重繪，不要整張重生成；打光怎麼調）。

**修改回合。** 使用者要求微調時，重新交付完整的提示詞和負面提示詞，只改那一處，並在構思條列裡列出改了什麼。探索性的微調（「試試」）在使用者確認之前，不要當成新的定案畫風。

完整的已採用範例（條款順序、密度、注意事項）請讀 `references/worked-example.md`。複製它的結構，絕不複製它的角色。

## 基礎負面提示詞

從這份清單開始，每個鏡頭再調整。使用者要線條時拿掉 `outlines, line art`，場景專屬的項目（泥土、樹皮、石頭）換成目前的場景：

```text
photorealistic, realistic rendering, PBR realism, ray-traced reflections, realistic mud texture, realistic bark, boulders, rocks, exposed roots, flat unshaded colors, hard-edged cel shading, outlines, line art, sketch lines, 2D illustration, hard shadows, high contrast, strong specular highlights, glossy, shiny, wet sheen, rim light, strong backlight, lens flare, god rays, heavy fog, grunge, heavy weathering, film grain, noise, color banding, posterization, compression artifacts, blotchy skin, dirty face, extra text, garbled characters, watermark, extra people, changed pose, zoomed out, recomposed framing
```

## Gotchas（踩過的坑）

- **金色主光、輪廓光、水窪反光和長影子**，結果被說「太寫實、太多高光」：使用者要的是平光。預設用柔和漫射光，反光的水窪拿掉或做成霧面。
- **矯枉過正成沒有陰影、沒有材質的平塗**，偏離了使用者的 3D 目標（目標有柔和體積感和 AO），使用者要求更貼近參考圖。平光是柔光，不是平塗。
- **崎嶇的災難詞彙**（boulders、gravel、exposed roots、山嵐、raw scars）把風格化背景變成照片。改寫成平滑的色帶和圓團樹冠。
- **漏掉了已定案的專案畫風**：一個三渲二需求的參考圖和同專案先前的鏡頭吻合，卻被寫成全新的畫風、還加了描邊，而不是沿用該專案的畫風。先檢查有沒有定案畫風（工作流程第 3 步）。
- **白模手腕上的一圈變成了手環**，但那個角色的參考圖是空手。寫明手腕空無一物，並要模型忽略版面圖上的形狀。下一個鏡頭換了一位真的戴手鐲的角色，照抄的負面提示詞 "bracelet" 就會把它抹掉，所以每個鏡頭都要重寫負面提示詞。
- **整句 "No text"** 跟必要的車牌打架。改寫成 "apart from the plate, no other text"。
- **一塊分鏡結構被刪掉了**：它被當成跟開放貨斗小貨車參考圖衝突的「廂型車車板」，其實是駕駛座的後牆。先讀透視，絕不丟掉結構。
- **草圖線條漏進 3D 渲染**，即使提示詞寫了 "no painterly"。要明確丟掉鉛筆線、灰階和疊加物，並寫 "zero outlines"。
