# Post Patterns — 主體結構與訊號觸發

Body construction, formatting, and the per-axis trigger design. Read on every post.

## Table of Contents

1. [貼文骨架](#1-貼文骨架)
2. [情緒選擇](#2-情緒選擇)
3. [手機排版](#3-手機排版)
4. [分享觸發設計](#4-分享觸發設計)
5. [追蹤轉換設計](#5-追蹤轉換設計)
6. [留言誘因設計](#6-留言誘因設計)
7. [轉單型的特殊結構](#7-轉單型的特殊結構)
8. [自我檢核表](#8-自我檢核表)
9. [Worked Example](#9-worked-example)

---

## 1. 貼文骨架

```
鉤子（3 行 — 見 hook-library.md）
↓
共鳴／處境      寫「讀者的處境」，不是「你的故事」。
                即使素材是你的經歷，敘述角度也要讓讀者看見自己。
↓
轉折            「我一直以為…直到…」— 認知翻轉的支點。整篇的重心。
↓
乾貨            2–4 點，條列，可操作。這是讀者「儲存」的理由。
↓
金句            一句可被截圖、可被引用的話。分享的燃料。
↓
互動裝置        低門檻留言誘因（§6）
↓
軸線收尾        分享型→立場；追蹤型→下一篇預告；轉單型→CTA（連結在留言）
```

**Not a rigid template.** 共鳴 and 轉折 may merge; 乾貨 may be a story rather than a list. What is non-negotiable: **鉤子 → 轉折 → 金句** — gap, flip, ammunition.

**長度啟發（非定律）:** avoid the 「不上不下」 middle. Either short enough to be read at a glance and screenshotted, or long enough that the dwell time is itself the signal. A post too long to skim but too thin to reward reading is the worst of both.

## 2. 情緒選擇

What gets shared is not 「感人」 — it is **high-arousal** emotion.

| 高喚醒（會分享） | 低喚醒（不會分享） |
|---|---|
| 驚訝、憤慨、敬畏、幽默、焦慮、強烈認同 | 平靜的溫馨、淡淡的憂傷、滿足、療癒 |

Low-arousal content can be pleasant to read and still spread nowhere. That's not a writing failure — it's a physics failure. If the brief wants reach, the emotion must be high-arousal.

**憤慨 caveat:** it spreads hardest and carries the most risk. Point it at a **practice, a myth, or a default** — never at a demographic or a named person. Rage at people buys 檢舉 and 隱藏, which are heavily negative signals (`algorithm-signals.md` §6). Also, the 憤怒 reaction itself was reportedly downweighted to zero — the value is in the *sharing* it triggers, not the reaction.

## 3. 手機排版

- **一句一行，一概念一段。** Blank line between paragraphs.
- **Paragraphs of 1–3 lines.** A phone renders a "short" desktop paragraph as a wall, and walls get scrolled past — which is exactly the signal that tells the ranker the post is bad.
- **Never let the hook break mid-sentence** across the 3-line fold.
- **Lists get real line breaks and numbers**, never a comma-run inside a paragraph.
- **粗體 sparingly** — 1–2 per post, on the 金句 and the single most important 乾貨 line. Bold everywhere is bold nowhere.
- **Emoji:** at most as list bullets or paragraph markers, never mid-sentence decoration. Zero is a valid and often better choice.
- **Hashtags:** max 3, only if meaningful. FB is not IG; stacking reads as an ad.
- **連結一律放第一則留言**, body says 「連結在留言區」.

## 4. 分享觸發設計

Core mechanic (`algorithm-signals.md` §4): **人不會為了幫你而分享，人只會為了表達自己而分享。**

Design question, every time: **「他轉發這篇時，會在上面加什麼評論？」** Can't answer in his words → no 社交貨幣 → no spread. Rewrite.

| Want this share tier | Build this in |
|---|---|
| 加註轉發 | A sharp **position** worth agreeing or arguing with. Vagueness gives the sharer nothing to type. |
| 截圖分享 | One self-contained **金句** that survives with zero context. |
| 社團分享 | Concrete utility for an **identifiable community**. |
| **私訊分享** (highest weight) | **Name the recipient inside the post**: 「這篇傳給那個一直說要做但拖了半年的朋友」 |

**The 金句 spec:** stands alone without the post · one sentence · contains the reversal, not a summary · no jargon. Usually shaped 「不是 A，是 B」 or 「真正 X 的不是 Y，是 Z」.

## 5. 追蹤轉換設計

Follow-conversion is a **two-stage funnel** (`algorithm-signals.md` §5): 貼文 → 點頭像 → 個人檔案 → 追蹤. The post only wins stage one. Everything below is about making stage two survivable.

Post-level levers — all saying **證明還有下一篇**:

- **序列標示** — 「AI 影片實驗第 7 天」. Day 8 must be implied to exist, or following has no purpose.
- **具體預告** — 「明天寫第二篇：那三句話的實際講法」. Beats 求追蹤, which does literally nothing. Vague 預告 (「下次聊更多」) also does nothing — name the content.
- **展現產能而非靈感** — imply a system, an ongoing experiment, an nth iteration. Make it believable this isn't your best-ever post.
- **獨特觀點 > 正確資訊** — correct information is commodity; they can get it anywhere. They follow a *lens* they can't get elsewhere.

**When the brief is 追蹤型, add this to 訊號設計說明** — it's the part users never think about and it caps everything:

> 陌生人點進你的個人檔案，是在確認「這人是不是穩定產出這種東西」。置頂和最近三篇貼文實質決定了追蹤轉換率——如果他點進來看到的是三個月前的活動宣傳，這篇寫得再好，轉換率也是零。

## 6. 留言誘因設計

留言 weighs far more than 讚, but **「你覺得呢？歡迎留言」 gets nothing.** Comments need *friction removed*, not permission granted.

| 裝置 | 範例 | 注意 |
|---|---|---|
| **二選一** | 「A 方案還是 B 方案？」 | Lowest friction. Safest default. |
| **填空／接龍** | 「____ 是我做過最後悔的商業決策。」 | Invites a story; produces long comments |
| **經驗點名** | 「你也遇過這種客戶嗎？會 or 不會就好」 | Give an explicit permission to answer in two words |
| **爭議表態** | 「這句話我知道有人不同意，來吵。」 | High volume; needs a real position and a thick skin |
| **索取型** | 「留言『要』我私訊你」 | ⚠️ Highest engagement, **highest unfollow cost.** Max once a month. Never two posts running. Never propose it by default. |

**Always give a reason to answer.** 「你會不會問？我很好奇這是不是只有我這樣」 outperforms a bare question — it converts answering from a favor into a contribution.

## 7. 轉單型的特殊結構

轉單型 posts structurally under-reach: they carry a CTA, need a link, and give readers no reason to share. **This is the trade, not a copywriting failure.** Say so plainly in 訊號設計說明; never imply a post will both 爆量 and 轉單.

Structural rules:
- **價值先於銷售** — the pitch never opens the post. Reader gets something usable before any ask.
- **CTA 放最後，連結放留言** — body says 「連結在留言區」.
- **精準勝過廣泛** — 身分標籤點名 hook. The right 200 beats the wrong 20,000.
- **具體勝過形容詞** — 「4 週、每週一次、每次 90 分鐘」 beats 「完整紮實的課程」.
- **一個 CTA** — 「報名」 *and* 「分享」 *and* 「追蹤」 = zero CTAs.
- **先養再收** — the conversion post is cashing a check written by the 追蹤型 posts before it. If nothing came before, recommend that rhythm rather than promising this post can carry it alone.

## 8. 自我檢核表

Run all of it before output. Rewrite anything that fails.

**Gate 1 — 截斷測試（不通過就重寫，其餘免談）**
Read *only* the first 3 lines, as a stranger, no context. Tap 「顯示更多」 or scroll? Be honest.

**Gate 2 — 轉發評論測試**
What would a sharer type above this post? Answerable in his words → has 社交貨幣. Not answerable → no spread. Rewrite.

**Then:**
- [ ] **傳給誰測試** — can you name one specific person a reader would send this to?
- [ ] **金句測試** — is there one line that survives being screenshotted alone?
- [ ] **追蹤理由測試** — after reading, is there any sense that a next post exists?
- [ ] **暖場句掃描** — is line 1 a real sentence, or throat-clearing?
- [ ] **第 3 行掃描** — does it hold tension, or leak the answer?
- [ ] **連結位置** — nothing external in the body?
- [ ] **套路感掃描** — anything here that would make a reader hide/unfollow? (索取型、假急迫、標題黨)
- [ ] **素材真實性** — every number and case traceable to what the user actually said? **No invented figures.**
- [ ] **排版掃描** — any paragraph over 3 lines? Any wall?
- [ ] **用語掃描** — 繁體、台灣用語？(視頻/質量/信息/走心/牛逼 → 刪)
- [ ] **軸線純度** — one axis, or is it hedging across all three?
- [ ] **鉤子多樣性** — are the 3 alternates on 3 *different* formulas?

## 9. Worked Example

Format calibration. Brief: 接案設計師的個人品牌經營，長期養粉。Fuel supplied: 一次改稿 20 版的失敗經驗、報價前不敢問簽核人。

---

**戰略判定：**追蹤型｜受眾＝接案 3 年以上、卡在低價與無限改稿的設計師｜燃料＝代價揭露（41 天／時薪 63 元的真實失敗）＋反直覺歸因（問題不在奧客，在報價階段沒問簽核人）｜假設：讀者已有接案經驗，不解釋基礎名詞。

---

## 主推貼文

接了一個 8 萬的案子，我做到第 41 天還在改。

客戶最後一句話是：「你這樣我很難跟老闆交代耶。」

那天晚上我算了一下時薪：63 塊。

我一直以為問題出在客戶。

奧客、需求不明、改稿無上限——同溫層裡大家都這樣講，我也講了三年。

直到我把過去 12 個案子的紀錄全部攤開，才看見一件很難承認的事：

**改稿最多的那 4 個案子，我在報價階段都做了同一件事——我沒問「這個案子誰有權簽核」。**

沒問，是因為我怕顯得計較、怕案子跑掉。

但實際發生的是：我對著窗口改了 20 版，而真正要點頭的那個人，第一次看到稿是在第 35 天。

前面 34 天，全是在猜。

所以現在，報價前我一定問三句：

1. 這個案子最後誰簽核？
2. 他什麼時候會第一次看到稿？
3. 如果他有意見，走修改還是走加價？

第三句最尷尬，但它省下的時間最多。

問完之後，我的平均改稿次數從 9 次掉到 3 次。案子沒有變少。

**接案這行，真正吃掉利潤的不是低價，是你不敢問的那些問題。**

你報價前會問簽核人是誰嗎？會 or 不會就好，我很好奇這是不是只有我這樣。

明天寫第二篇：那三句話的實際講法——怎麼問才不會像在質疑客戶。

---

**第一則留言：**
（本篇無外連結）

---

## 鉤子替代方案

**方案 A｜敵人指認**
真正吃掉你利潤的不是低價。
是你在報價前不敢問的那一句話。
我用 41 天和 8 萬塊的案子，才學會問它。
> 賭的是：歸因轉移——把「我不夠好」換成一個外部敵人，讀者為了表態而轉發。

**方案 B｜身分標籤點名**
如果你是接案設計師，這篇會讓你有點不舒服。
因為我要說的是：那些奧客，有一半是你自己養出來的。
包括我。
> 賭的是：對號入座＋自我指控——先攻擊受眾再把自己也放進去，冒犯感轉成信任感。

**方案 C｜數字×時間框**
41 天、20 版、時薪 63 塊。
這是我人生最貴的一個案子。
而真正該簽核的那個人，第 35 天才第一次看到稿。
> 賭的是：具體性＝可信度——四個奇數把抽象的接案痛苦變成可驗證的帳。

---

**訊號設計說明：**這篇走追蹤型：用「代價揭露」建立信任，再用一個可操作的三句話清單換取「儲存」，結尾的具體預告（明天第二篇）是追蹤轉換的主要引擎——讀者知道第二篇存在，追蹤才有意義。金句刻意寫成「不是 A，是 B」的句型，讓它單獨截圖也成立。最大的風險是這篇的分享率不會高：它的情緒是低喚醒的自省而非高喚醒的憤慨，換來的是追蹤而不是擴散——這是刻意的取捨。另外提醒，追蹤轉換是兩段漏斗，陌生人點進你的個人檔案是在確認「這人是不是穩定產出這種東西」；如果置頂還是三個月前的作品集宣傳，這篇寫得再好，轉換率也會是零。
