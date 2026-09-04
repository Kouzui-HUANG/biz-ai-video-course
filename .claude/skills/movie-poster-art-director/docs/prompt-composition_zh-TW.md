# 提示詞撰寫參考（繁中對照）

> `references/prompt-composition.md` 的中文對照版，僅供人閱讀。英文提示詞與詞彙庫維持原文，因為那是實際要餵給模型的文字。

目錄：§1 六段公式 · §2 詞彙庫 · §3 身份錨點 · §4 無文字與留白寫法 · §5 比例結尾 · §6 完整範例 · §7 禁用寫法

---

## 1. 六段公式

寫成**一段**流暢段落，150–220 字。電影感的完整英文句子，絕不是標籤列表。六段依序銜接、互相融合：

```
[1 構圖原型與取景] → [2 主體與身份錨點] → [3 環境與尺度]
→ [4 光線邏輯與氛圍] → [5 色彩、調色與質感] → [6 留白與規格]
```

第 6 段永遠收尾，讓「預留區」與「無文字」是模型最後讀到的指令。

| # | 段落 | 必須指定 |
|---|---|---|
| 1 | 構圖原型與取景 | 構圖原型 ＋ 景別 ＋ 攝影角度 ＋ 鏡頭 |
| 2 | 主體與身份錨點 | 取自角色圖的鎖定特徵、服裝剪影、姿態、視線方向、微表情 |
| 3 | 環境與尺度 | 前景／中景／背景層次 ＋ 承載概念的那個尺度關係 |
| 4 | 光線邏輯與氛圍 | 一個有來源的主光 ＋ 輪廓光／補光、天氣或懸浮微粒、時段 |
| 5 | 色彩、調色與質感 | 指名 60-30-10 三色、底片顆粒、光暈、對比曲線 |
| 6 | 留白與規格 | 畫面哪一塊為片名保持淨空、無文字語句、畫面比例 |

## 2. 詞彙庫

英文詞彙庫請直接參照 `references/prompt-composition.md` §2，分為六組：**取景與鏡頭**、**姿態視線與表情**、**環境與尺度**、**光線與氛圍**、**色彩調色與質感**、**留白與規格**。

## 3. 身份錨點（取自提供的角色美術）

錨點句在主視覺聖經寫一次，之後在每則提示詞中**逐字**重複。好的錨點只點名 5–7 個固定屬性：

> `a woman in her early forties, square jaw and heavy brow, shoulder-length black hair pushed back and greying at the temples, deep-brown eyes, a pale vertical scar through the left eyebrow, wearing a salt-stained olive fisherman's jacket`

規則：只描述圖片實際呈現的東西 · 絕不杜撰美術沒有支持的族裔、年齡或身體特徵 · 可以自由重新打光與擺姿，但臉部結構、髮色、瞳色與標誌性服裝在三案之間不可有不同說法 · 背景圖也用同樣方式鎖定（`a concrete tidal breakwater under a low grey sky`）。

## 4. 無文字與留白寫法

一律正面表述，絕不使用負面提示詞列表。兩個子句，缺一不可：

1. 預留該區 —— `the lower third resolves into flat unbroken shadow, held deliberately empty`。
2. 把「沒有文字」寫成畫面**本身是什麼** —— `a pure photographic frame entirely free of lettering, titles, captions, logos or watermarks`。

絕不要寫「with the film title at the top」「add the tagline」「include credits」——模型會生出扭曲的假文字，並且毀掉預留區。

## 5. 比例結尾

用白話收尾，不要參數：`vertical 2:3 movie poster composition` ／ `wide 16:9 streaming key art composition with the subject held off-centre to camera right`。絕不輸出 `--ar 2:3`、`::`、權重或 `(word:1.4)` 之類語法。

## 6. 完整範例

完整的示範提案（含英文提示詞、中文翻譯與文字排版計畫）請見 `references/prompt-composition.md` §6。範例情境為：台灣漁村懸疑劇本 ＋ 一張角色圖（四十多歲女性、橄欖綠外套）＋ 一張背景圖（霧中的混凝土防波堤），採用「地平線孤影」原型的 teaser。

## 7. 禁用寫法

`--ar 2:3` ／ `(dramatic:1.3)` ／ `masterpiece, best quality, 8k, trending on artstation` ／ `no text, no watermark, no blur`（負面列表語法）／ `movie poster with the title "…"` ／ `in the style of [在世設計師或工作室]` ／ 逗號分隔的關鍵字堆疊 ／ 把 `epic, cinematic, stunning, breathtaking` 疊在一起卻沒有任何具體物理描述支撐。
