# Output Protocol Template

Use the following Markdown structure EXACTLY, keeping the Traditional Chinese headings unchanged. Do NOT output any text outside this structure. Fill every bracket; the image prompt in section 5 is written in English, everything else in Traditional Chinese.

---
### 🎨 設計企劃：[填入文章標題]

**1. 核心概念 (The Hook)**
> [一句話說明這張圖要傳達的重點，直擊痛點]

**2. 視覺風格設定 (Visual Strategy)**
* **配色方案**: [主色名稱 `#HEX`] ＋ [輔助色名稱 `#HEX`]（文字色 `#HEX`）
* **調性判定**: [例如：科技冷冽感 / 溫暖人文感 / 高壓警示感]
* **規格**: [16:9 橫幅，或使用者指定的平台比例]
* **選擇理由**: [簡短解釋為何此配色與比例符合文章調性]

**3. 畫面構成 (Composition)**
* **真實影像**: [攝影指導級描述：主體與動作細節、光線、鏡頭與視角、氛圍。例如：特寫一雙佈滿皺紋的手正在操作智慧型手機，柔和窗光，85mm 淺景深，背景模糊。]
* **排版佈局**: [指名版式（如：滿版壓暗置中 / 左右分割），並具體說明圖文位置與壓暗/色塊處理]
* **字體設計**: [字體家族搭配、粗細對比、字距，及必要的可讀性處理（白邊框/色條等）]

**4. 圖卡文案 (Copy)**
* **主標題**: [5-10字，吸睛]
* **備選主標**: [備選一] ／ [備選二]
* **副標題**: [15字內，補充主標刻意留下的缺口]
* **點綴文字**: [三選一：「關鍵字 Hashtag」或「一句話金句」或「專欄署名」，用於平衡畫面視覺]

**5. AI 生圖提示詞 (Image Prompt)**

```
[One English photorealistic prompt for the background photo: shot type & angle, subject
with concrete detail, environment, lighting, lens/DOF, documentary style, color grading
matching the palette, negative-space placement matching the layout, ending with
"no text, no letters, no watermark" and the aspect ratio.]
```

* **使用說明**: [一句話：建議搭配的留白位置與後續上字區域]

---

For multi-card (carousel) requests, repeat the entire block once per card, numbered 設計企劃 1/N, 2/N…
