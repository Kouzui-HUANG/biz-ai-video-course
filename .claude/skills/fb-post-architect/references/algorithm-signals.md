# Facebook Ranking Signals — Copywriter's Edition

How Facebook distribution actually works, translated into things a writer can act on. Read when choosing or explaining the 戰略軸, or when writing 訊號設計說明.

## Table of Contents

1. [Evidence Strength — read first](#1-evidence-strength--read-first)
2. [The Two Traffic Pools](#2-the-two-traffic-pools)
3. [The Signal Ladder](#3-the-signal-ladder)
4. [Shares — Four Tiers, Not One Action](#4-shares--four-tiers-not-one-action)
5. [Follow-Conversion — The Only Forward-Looking Signal](#5-follow-conversion--the-only-forward-looking-signal)
6. [Negative Signals](#6-negative-signals)
7. [分享型 vs 追蹤型 — The Structural Conflict](#7-分享型-vs-追蹤型--the-structural-conflict)
8. [What This Means for the Page](#8-what-this-means-for-the-page)

---

## 1. Evidence Strength — read first

Meta has never published ranking weights. Calibrate claims honestly; do not state folklore as law.

| Claim | Strength |
|---|---|
| Two distribution pools (connected / unconnected recommendations) exist | **Documented** — Meta describes recommendation-driven distribution publicly |
| External links in the body suppress reach | **Strongly observed** — consistent practitioner data, not officially confirmed as a penalty |
| Point values 讚 1 / 心情 5 / 留言・分享 30 | **Historical leak** — from 2021 disclosures of a 2018 MSI framework. Directionally useful, numerically obsolete. Never quote as current fact. |
| 憤怒 reaction downweighted to 0 | **Reported** (~2020, same leak lineage) |
| Follow-conversion is a ranking input | **Inferred, not documented** — reasoned from system behavior: Meta surfaces per-post follower attribution as a headline creator metric, and discovery engines generally model it. Confirmed on YouTube (subscriber conversion), not on FB. |
| Negative signals (hide/unfollow/report) carry heavy negative weight | **Strongly observed** |

**Rule:** when the user asks *why*, say which tier the claim sits in. A confidently-wrong mechanism produces confidently-wrong copy.

## 2. The Two Traffic Pools

Reach arrives from two places, and they behave nothing alike:

- **連結內容 (connected)** — served to existing followers. Now a *minority* of reach.
- **非連結推薦 (unconnected)** — AI-recommended to strangers. The primary growth engine since FB's ~2022 pivot toward a discovery feed.

**Typical flow:** a new post goes first to a small slice of active followers → performance there decides whether it enters the recommendation pool.

Two consequences a writer must internalize:

1. **The first slice is a test, not an audience.** Everything in the post is optimizing to pass that gate.
2. **Follower quality > follower count.** 抽獎粉, 互追粉, and bought followers dilute the test sample and kill posts at the gate. 5,000 people who actually read beats 50,000 who don't — the second number actively harms you.

**Never tell a user their follower count drives reach.** It largely doesn't anymore.

## 3. The Signal Ladder

Roughly ascending in weight and in information value. The pattern that matters: **behavioral cost ↑ → noise ↓ → signal value ↑.**

| Signal | What it actually says |
|---|---|
| 讚 | 「我不討厭這個」 — cheap, dozens per day, near-zero information |
| 心情 (愛心/哈/哇) | Weak emotional confirmation |
| 停留時間 / 點「顯示更多」 | The hook worked. Quiet but real. |
| 留言 | Investment of effort; also spawns a second interaction surface |
| 儲存 | High — implies future utility; drives dwell too |
| 分享 | High — see §4, it is four different signals wearing one name |
| **追蹤轉換** | **Highest — the only forward-looking signal (§5)** |

**Writer's translation:**
- 按讚 ≈「我不討厭這個」
- 分享 ≈「這個能代表我」 ← note: about the *sharer*, not about you
- 追蹤 ≈「我押注你未來還會產出這種東西」

## 4. Shares — Four Tiers, Not One Action

Design for the tier you want; they are not interchangeable.

| Tier | Weight | Why |
|---|---|---|
| 純轉發（無文字） | Lowest | Reads as a reflex; creates no new content or conversation |
| 加註文字轉發 | Higher | Sharer invested creative effort; their text spawns a **second comment thread** in their own circle |
| 分享到社團 | High, and **cross-pool** | Delivers the post into a closed pool you can't otherwise reach; engagement there feeds back to the original |
| **私訊分享 (Messenger / 限時動態)** | **Highest, and invisible** | Sending directly to one named person is the strongest possible endorsement. It's dark traffic — you'll never see it in the dashboard, you'll only notice reach mysteriously improving. |

**The core mechanic:**

> 人不會為了幫你而分享，人只會為了表達自己而分享。分享是社交貨幣。

So the post must make the sharer look smart, tasteful, or compassionate — **to their own audience**.

**The design question, always:** 「他轉發這篇的時候，會在上面加什麼評論？」 If you can't answer in his words, you gave him no position to take, and he won't share.

Triggers, by tier:
- 加註轉發 → give a sharp, quotable **position** worth agreeing or arguing with
- 截圖分享 → plant one **可被截圖的金句**
- 社團分享 → make it **practically useful** to an identifiable community
- 私訊分享 → name the recipient inside the post: 「這篇傳給那個一直說要做但拖了半年的朋友」 — unusually effective, and it buys the highest-weight tier

## 5. Follow-Conversion — The Only Forward-Looking Signal

New followers attributed to a single post. Highest-value signal available, for four separate reasons:

**1. It evaluates a different object.** 讚/留言/分享 evaluate *this post* → affects this post's reach. 追蹤 evaluates *the author* → affects this post **and your account's long-run baseline**. The return is compounding, not one-off.

**2. It is scarce, so it carries information.** Dozens of likes per day vs. maybe dozens of follows per *year*. High behavioral cost = low noise.

**3. It is the only bet on the future.** Every other signal is a retrospective verdict on content already consumed. A follow is the reader's own *prediction* that more good things are coming. For a system deciding whether to keep distributing an account, that is the most direct answer it can get.

**4. In the recommendation pool it has no social noise.** A stranger has zero social obligation to follow you. A friend's like is contaminated by 人情; a stranger's follow is a pure content-value judgment. This is why follow-conversion dominates specifically in the unconnected pool — which is where growth lives.

### It is a RATE, not a count

| Post | Reading |
|---|---|
| 100 follows / 1,000,000 reach | Bad |
| 100 follows / 10,000 reach | Excellent |

**The counter-intuitive consequence — write this into 訊號設計說明 when relevant:**

> 一篇 50 萬觸及、0 追蹤的爆文，對帳號長期是負面的。

It tells the system: *this account attracts clicks but retains no one.* Same logic as YouTube's high-views/low-subscribes trap. The account gets filed as a one-off stimulus source, not a creator worth sustained distribution.

### Follow-conversion is a TWO-STAGE funnel

Most people optimize stage one and then wonder why the viral post grew nothing.

```
貼文 → 點頭像／名字 → 個人檔案 → 追蹤
                        ↑ the real conversion point
```

The stranger lands on the profile to answer one question: **「這人是不是穩定產出這種東西？」**

- Pinned post + last 3 posts effectively *set* the conversion rate — a three-month-old event promo at the top zeroes it out regardless of how good the post was.
- 簡介 must answer 「追蹤你會得到什麼」, not 「你是誰」.
- 主題一致性 is not just for humans — the recommender must classify your topical cluster to know who to show you to. AI today, breakfast tomorrow = restarting from zero every post.

Post-level levers that raise the rate — all of them say the same thing, **證明還有下一篇**:
- 序列標示: 「AI 影片實驗第 7 天」 — he knows day 8 exists, so following has a point
- 具體預告 next post's content — beats any form of 求追蹤, which does nothing
- 展現產能而非靈感 — make it believable this isn't your best-ever post

## 6. Negative Signals

隱藏貼文 / 取消追蹤 / 檢舉 are **negatively weighted and heavy** — one can offset many positives, and the damage carries forward into your next posts' initial reach.

This is precisely why 索取型互動 (「留言『要』我私訊你」) is a trap: excellent short-term engagement metrics, but once readers feel套路'd, you buy unfollows. Net negative on any horizon longer than a week.

Also generating negative signals: 標題黨 that doesn't pay off · selling before delivering value · posting off your established topic · engagement bait phrasing.

## 7. 分享型 vs 追蹤型 — The Structural Conflict

These pull in opposite directions. This is the single most important strategic fact in this file.

| | 分享型 | 追蹤型 |
|---|---|---|
| Content | 迷因、情緒、爭議、時事 | 專業、系列、獨特觀點 |
| Share rate | High | Low–medium |
| Follow-conversion | **Low** | **High** |
| Why | 人分享是為了表達自己 — that act says nothing about you | 讀者認可的是作者，不是這一則 |
| Failure mode | 跑步機：每篇都要重新爆一次，帳號沒有底線 | 天花板低：好內容沒人看見 |

**分享讓這篇活，追蹤讓下一篇更容易活。**

A content plan needs both, on a rhythm — but any *single post* must pick one. Optimizing both in one post produces a post that does neither.

## 8. What This Means for the Page

Two lines worth telling users when relevant:

- **追蹤轉換率是唯一誠實的指標。** 觸及和讚都會騙你 — they can rise while the account weakens. Follow-conversion rate is the only number that tells you whether the account is compounding or just burning attention.
- **買粉和抽獎粉是負資產**, not neutral ones: they poison the initial test slice that decides whether any post reaches the recommendation pool.
