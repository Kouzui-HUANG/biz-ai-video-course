# Suno 結構標籤完整規範

> 本文檔在「第二階段：輸出」時由 SKILL.md 載入。歌詞輸出必須遵守此規範。

## 目錄

1. [基礎骨架標籤（Skeleton Tags）](#1-基礎骨架標籤)
2. [動態修飾標籤（Dynamics Tags）](#2-動態修飾標籤)
3. [情緒與風格修飾（Mood & Style Modifiers）](#3-情緒與風格修飾)
4. [結構組裝範本（Structure Templates）](#4-結構組裝範本)
5. [密度與長度建議（Density Guidelines）](#5-密度與長度建議)
6. [常見錯誤（Common Pitfalls）](#6-常見錯誤)

---

## 1. 基礎骨架標籤

每首歌**至少包含** `[intro] / [verse] / [chorus] / [outro]` 四種標籤。其餘為選用。

### [intro] —— 開場

- **功能**：設定基調、確立情緒色調
- **常見修飾**：Atmospheric（氛圍）/ Percussive（節奏感）/ Ambient（環境音）/ Minimal（極簡）/ Cinematic（電影感）
- **歌詞密度**：低（0-2 句，或純氛圍提示無歌詞）
- **建議**：
  - 寫氛圍提示時用斜體標註：*soft piano, distant rain*
  - 若有歌詞，使用 echo / whisper 風格的短句
  - 避免在 intro 就把 Hook 唱出來（破梗）

**範例**：

```
[intro] *Atmospheric, soft piano fade-in*
（無歌詞，純氛圍鋪陳）
```

或：

```
[intro] *Whispered, distant*
寒風吹過 沒有人在
```

### [verse] —— 主歌

- **功能**：敘事核心、推動故事、建立場景
- **常見修飾**：Spoken-word（說話式）/ Soft（輕柔）/ Narrative（敘事）/ Confessional（告白式）/ Detached（抽離）
- **歌詞密度**：中（4-8 句）
- **編號**：[verse 1] / [verse 2] / [verse 3]
- **建議**：
  - 第一人稱具體畫面（依循 [methodology.md §5](../references/methodology.md#5-視角切換推進)）
  - 每段至少 1 個具體物件 + 1 個動作
  - 使用家族韻或母音韻（不完美韻）製造前進感

**範例**：

```
[verse 1] *First-person, soft delivery*
咖啡店的角落 你坐過的位置
桌上的水印 還是當年的形狀
我點了一杯拿鐵 沒加糖
就像那年你忘了說的話
```

### [pre-chorus] —— 預副歌

- **功能**：張力鋪墊、把聽眾推向 chorus 的情緒高點
- **常見修飾**：Rising（漸強）/ Harmonized（和聲堆疊）/ Building（堆疊）/ Tense（緊繃）
- **歌詞密度**：中低（2-4 句）
- **建議**：
  - 音節密度比 verse 高（製造緊湊感）
  - 使用反問或不完美韻（吊住聽眾）
  - 最後一句必須是「跳板」，自然彈進 chorus

**範例**：

```
[pre-chorus] *Rising tension*
是不是 我們都太晚才懂
那些話 為什麼不能早一點說
```

### [chorus] —— 副歌

- **功能**：全曲情緒高潮、Hook 所在、最大記憶點
- **常見修飾**：Anthemic（頌歌式）/ Dynamic（動感）/ Powerful（強烈）/ Soaring（高揚）/ Catchy（朗朗上口）
- **歌詞密度**：中（4-6 句）
- **建議**：
  - **第一句必須是 Hook**（最重要的金句）
  - 使用完美韻或開口韻（產生穩定與爆發感）
  - 全曲至少出現 2-3 次（標準位置：1/3、2/3、結尾）
  - 可在最後一次出現時做變奏（更多裝飾、更高音）

**範例**：

```
[chorus] *Anthemic, soaring*
越過山丘 才發現無人等候
那些以為的永遠 都成了句號
我把名字寫進風裡
讓它替我 替我說再見
```

### [bridge] —— 橋段

- **功能**：打破副歌重複感、製造對比、為最終副歌蓄力
- **常見修飾**：Stripped-down（留白極簡）/ Climactic（頂峰）/ Reflective（反思）/ Sparse（稀疏）
- **歌詞密度**：中（3-5 句）
- **建議**：
  - **必須換韻部**（與 verse / chorus 不同）
  - 視角切換（時空閃回、抽離、夢境）
  - 通常出現一次，位置在第二次 chorus 之後

**範例**：

```
[bridge] *Stripped-down, only piano and vocal*
如果時間能倒回那年夏天
你還會不會 站在傘下等我
（停頓）
還是說 我們從一開始 就只是路過
```

### [outro] —— 收尾

- **功能**：餘韻、收束、留下懸念或總結
- **常見修飾**：Fade-out（淡出）/ Reverb-tail（殘響尾音）/ Echo（迴聲）/ Whispered（耳語）/ Ambient（環境音）
- **歌詞密度**：低（1-3 句或純氛圍）
- **建議**：
  - 呼應 intro（首尾相扣）
  - 可使用 Hook 的變奏或回聲
  - 避免新意象（聽眾此時不會記住新資訊）

**範例**：

```
[outro] *Reverb-tail, fade out*
越過山丘⋯
（fade）
無人等候⋯
（fade out）
```

---

## 2. 動態修飾標籤

用於段落間的銜接與強化，**非必選**，但能大幅提升結構張力。

### [build] —— 能量堆疊

- **功能**：把能量逐層堆高，放在 chorus 前
- **歌詞建議**：使用重複短句、音節密度提升
- **位置**：通常接在 pre-chorus 後、chorus 前

**範例**：

```
[build] *Energy stacking*
快一點 快一點 快一點
時間不夠了
```

### [rise] —— 史詩感張力

- **功能**：類似 build，但更宏大、適合放在最終 chorus 或 climax 前
- **歌詞建議**：開口韻、長母音、放聲喊唱
- **位置**：最終 chorus 或 climax 前

**範例**：

```
[rise] *Epic, soaring*
讓世界 都聽見
這一刻 不再退
```

### [drop] —— 能量釋放

- **功能**：突然降下能量或炸開，常用於電子曲風
- **修飾**：Bass-heavy（重低音）/ Melodic（旋律性）/ Vocal-cut（人聲切斷）
- **位置**：build 或 rise 之後
- **歌詞建議**：可無歌詞（純樂器釋放）或極短句

**範例**：

```
[drop] *Bass-heavy, no vocals*
（樂器爆發、無歌詞）
```

### [break] —— 呼吸空間

- **功能**：短暫停頓、製造節奏切分
- **位置**：兩段密集段落之間
- **歌詞建議**：1 句或無歌詞

**範例**：

```
[break]
（兩拍停頓）
```

### [breakdown] —— 結構簡化

- **功能**：把編曲拆解到最簡（只剩人聲 + 一個樂器），為二次爆發蓄力
- **位置**：通常在 bridge 後、最終 chorus 前
- **歌詞建議**：低密度、白描句、近耳語

**範例**：

```
[breakdown] *Vocal + acoustic guitar only*
你還記得嗎
那年我們說好的
（停頓）
```

### [climax] —— 全曲頂點

- **功能**：最強烈的情緒爆發
- **修飾**：Vocal-driven（人聲主導）/ Instrumental（樂器主導）/ Full-band（全樂團）/ Choir（合唱團）
- **位置**：通常是最後一次 chorus 或其後
- **歌詞建議**：Hook 的變奏 + 最高音

**範例**：

```
[climax] *Full-band, vocal-driven, key change*
越—過——山——丘
（高八度）
無—人——等——候
```

---

## 3. 情緒與風格修飾

在每個結構標籤後可附加修飾詞，用斜體 `*...*` 標註。

### 情緒修飾詞庫

- **Atmospheric**：空靈、氛圍
- **Spoken-word**：說唱、口白
- **Soft**：柔和、輕聲
- **Harmonized**：和聲堆疊
- **Anthemic**：頌歌式、氣勢磅礴
- **Dynamic**：動感、強弱對比
- **Stripped-down**：極簡、剝離
- **Climactic**：高潮
- **Whispered**：耳語
- **Confessional**：告白式、私密
- **Detached**：抽離、冷靜
- **Reflective**：反思
- **Cinematic**：電影感

### 樂器 / 音色提示

可在標籤後附樂器提示，幫助 Suno 理解氛圍：

```
[verse 1] *Soft piano, brush snare*
[bridge] *Strings swell, no drums*
[outro] *Acoustic guitar fingerpicking, reverb*
```

### 演唱方式提示

```
[chorus] *Vocal harmony, layered*
[verse 2] *Falsetto, intimate*
[bridge] *Choir backing, gospel feel*
```

---

## 4. 結構組裝範本

### 範本 A：流行抒情標準結構（5-6 分鐘）

```
[intro]
[verse 1]
[pre-chorus]
[chorus]
[verse 2]
[pre-chorus]
[chorus]
[bridge]
[breakdown]
[chorus] *Climactic final*
[outro]
```

### 範本 B：搖滾／流行精簡結構（3-4 分鐘）

```
[intro]
[verse 1]
[chorus]
[verse 2]
[chorus]
[bridge]
[chorus]
[outro]
```

### 範本 C：電子舞曲結構（3-5 分鐘）

```
[intro] *Synth pad, gradual*
[verse 1]
[pre-chorus]
[build]
[drop] *Bass-heavy*
[chorus]
[break]
[verse 2]
[pre-chorus]
[build]
[drop]
[chorus]
[breakdown]
[rise]
[climax]
[outro]
```

### 範本 D：民謠／獨立極簡結構（2-3 分鐘）

```
[intro] *Acoustic guitar, fingerpicking*
[verse 1]
[verse 2]
[chorus]
[verse 3]
[chorus]
[outro] *Hum, fade*
```

---

## 5. 密度與長度建議

### 整首字數參考（中文歌詞）

- **抒情慢板**：250-350 字
- **流行搖滾**：300-450 字
- **電子舞曲**：200-300 字（重複多）
- **民謠**：350-500 字（敘事密度高）
- **饒舌段落**：每 16 小節約 100-150 字（密度極高）

### 各段建議字數（中文）

| 段落 | 字數範圍 |
|---|---|
| [intro] | 0-30 字 |
| [verse] | 40-80 字/段 |
| [pre-chorus] | 20-40 字 |
| [chorus] | 40-70 字 |
| [bridge] | 30-60 字 |
| [outro] | 0-30 字 |

### 句長建議

- **副歌句長**：每句 7-12 字（最易記憶）
- **主歌句長**：每句 8-15 字（較有彈性）
- **避免**：單句超過 18 字（Suno 容易斷氣）

---

## 6. 常見錯誤

### ❌ 錯誤 1：標籤格式不對

```
verse 1:
（歌詞）
```

✅ 正確：

```
[verse 1]
（歌詞）
```

### ❌ 錯誤 2：把段落名寫在歌詞裡

```
[chorus]
這是副歌
越過山丘
```

✅ 正確：直接寫歌詞，不要加「這是副歌」這種描述

```
[chorus]
越過山丘 才發現無人等候
```

### ❌ 錯誤 3：標籤太多、太雜

一首 3 分鐘的歌不需要 15 個不同段落標籤。**3 分鐘的歌標籤總數控制在 8-10 個以內**。

### ❌ 錯誤 4：修飾詞語法錯誤

```
[chorus Anthemic]
```

✅ 正確：用斜體分隔

```
[chorus] *Anthemic*
```

### ❌ 錯誤 5：在 chorus 寫完全不同的歌詞

每次 chorus 出現時，**至少 80% 歌詞要一致**（這就是「副歌」的意義 —— 重複）。只有在最後一次 chorus 可以做變奏。

### ❌ 錯誤 6：忘記 outro 呼應 intro

首尾呼應能大幅提升完整度。intro 用了「寒風」，outro 也應該回到「寒風」的意象。

---

## 附錄：Suno 風格標籤推薦組合

當輸出歌詞後，使用者若想搭配 Suno 風格標籤，可推薦使用 `ai-music-prompt-generator` 技能。

若使用者需要快速生成風格標籤，可參考以下基礎組合：

| 曲風 | Suno Style Tags 建議 |
|---|---|
| 抒情慢板 | `Mandopop ballad, soft piano, strings, intimate vocal, 70 BPM` |
| 流行搖滾 | `Pop rock, anthemic, electric guitar, driving drums, 110 BPM` |
| 電子舞曲 | `Synth-pop, future bass, vocal chops, side-chain, 128 BPM` |
| 民謠 | `Acoustic folk, fingerpicking, warm vocal, organic, 85 BPM` |
| 古風 | `Chinese guzheng, ethereal, ambient strings, breathy female vocal, 75 BPM` |
| R&B | `Modern R&B, 808 drums, lush keys, melismatic vocal, 90 BPM` |
