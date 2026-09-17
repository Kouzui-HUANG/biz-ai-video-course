# 輸出格式參考（繁中對照）

> `references/output-schema.md` 的中文對照版，僅供人閱讀。YAML 範本、英文 prompt、標籤維持原文，因為那是實際要餵給模型的文字。

撰寫任何輸出之前請先讀完本檔。目錄：
- §1 完整模式的 Markdown 框架
- §2 方向提案模式的框架
- §3 Clip YAML 結構
- §4 欄位規則
- §5 音軌規則
- §6 asset_refs 結構
- §7 字元上限
- §8 完整範例

---

## §1 完整模式的 Markdown 框架

企劃段落用繁體中文撰寫，YAML 用英文撰寫。輸出直接從「設計假設」開始，開頭不打招呼，結尾也不提問。

````markdown
**設計假設：**[一行——凡是推定而來的項目都寫明：時長／比例／風格變體／台詞／目標模型／資產來源]

### 🎬 導演意圖
- **片名**｜《…》
- **鉤子**｜公式 N [類型]：[一句話——開頭 3 秒讓觀眾心裡冒出什麼疑問]
- **敘事模板**｜[A–G 模板名稱，可複選]
- **故事節拍**｜① … → ② … → ③ …（3–6 個節拍，只寫因果與轉折）
- **資訊差**｜觀眾知道：… ｜角色不知道：…
- **情緒曲線**｜… → … → …
- **反轉點**｜~Ns …；~Ns …
- **視覺基調**｜[色調氛圍]；主色 `#HEX`／`#HEX`，點綴 `#HEX`；光源：…；禁用：…
- **鏡頭語言**｜[核心鏡頭語言＋關鍵技法]
- **聲音設計**｜環境：…；聲畫關係：[同步／對位／延遲揭示]；關鍵聲音：…；配樂（後製）：…
- **節奏**｜[節奏型態] ＋ [雙軌（畫面／聲音）說明]

### 📦 資產清單
| ID | 資產 | 來源 | 鎖定錨點 |
|---|---|---|---|
| S1 | … | 使用者主體／使用者參考圖／待生成 | … |

### 🗂 分鏡總表
| 鏡 | 時長 | 角度 | 景別 | 畫面內容 | 場景 | 聲音 | 備註 | 敘事目的 | Clip |
|---|---|---|---|---|---|---|---|---|---|

### 🎞 Clip 提示詞
**C1｜00:00–00:10｜10s｜[敘事目的標籤]**
```yaml
[Clip YAML——格式見 §3]
```
（每個 Clip 各寫一段，依序重複）

### 🧩 參考圖提示詞
```yaml
[asset_refs——格式見 §6；若沒有任何資產標為待生成或使用者參考圖，整段省略]
```

**後製備註：**[附時間碼的字幕／片名字卡・配樂・淡入淡出・參考圖掛載順序・模型限制提醒——1–4 行]
````

---

## §2 方向提案模式的框架

輸入只有氛圍或類型，或使用者主動要求先看方向時，採用這個模式。輸出以下三個提案後就**停下來**。

````markdown
**方向提案**（尚未進入分鏡）

**方向 A｜《片名》**
- 一句話故事：…
- 鉤子：公式 N …
- 敘事模板：…
- 反轉：…
- 視覺記憶點：[視覺母題＋點綴色]
- 情緒曲線：…

**方向 B｜…**（換一個鉤子公式與敘事模板）

**方向 C｜…**（換一個鉤子公式與敘事模板）

請回覆 A／B／C（可混搭），並可指定：時長（預設 30s）・比例（預設 9:16）・風格（預設暗黑童話 A 觸感定格）・台詞／旁白（預設無）・目標模型。
````

---

## §3 Clip YAML 結構

每個 Clip 寫成一個獨立、可單獨使用的區塊。欄位順序固定，沿用 prompt-master-video-continuity 的做法：`project_meta` → `subject_profile` → `multi_shot_sequence`。

```yaml
project_meta:
  clip: "C{n}/{total} | {global start}-{global end} | {dur}s"
  summary: "{{one-line clip beat}}"
  art_style: "{{art-style lock, verbatim}}"
  format: "{{ratio}}, {{dur}}s"
  bgm: "(none)"   # replace only if the user specified music

subject_profile:
  visual_lock:          # only subjects appearing in this clip
    S1: >
      {{verbatim keyword-stack lock}}
  prop_lock:            # omit key if no locked prop appears
    P1: "{{verbatim lock}}"
  scene_lock:           # only scenes used in this clip
    L1: "{{verbatim lock}}"

multi_shot_sequence:
  continuity_in: "{{tail state of previous clip, or '(opening clip)'}}"
  shots:
    - id: {{global shot number}}
      time: "{{clip-local start}}-{{end}}s"
      type: "{{shot size}}, {{angle}}, {{camera move / technique}}"
      action_prompt: >
        {{Identity echo}} {{action}}. {{environment / lock ID}}. {{light / composition}}.
      audio_prompt: "[Tag] {{sound}}."
  continuity_out: "{{tail state for next clip, or '(final clip)'}}"
```

---

## §4 欄位規則

| 欄位 | 規則 |
|---|---|
| `project_meta.clip` | Clip 序號、全片時間碼與時長。時長限 4–15 秒。 |
| `project_meta.summary` | 一行電報式短句，交代這個 Clip 的節拍。 |
| `project_meta.art_style` | 風格聖經的鎖定描述，每個 Clip 一字不差。 |
| `project_meta.format` | 比例與時長，例如 `9:16 vertical, 10s`。 |
| `project_meta.bgm` | 除非使用者要求音樂，否則一律填 `"(none)"`。全片配樂寫在導演意圖／後製備註裡。 |
| `subject_profile.*_lock` | 關鍵字堆疊（不寫成句子），從資產清單的鎖定錨點逐字照抄。只列這個 Clip 裡出現的資產。狀態有變化時，接在基本詞後面補上（`…, hood now torn`）。**長度上限：**主角 ≤ 25 個英文字・配角 ≤ 12・道具 ≤ 10・場景 ≤ 15・背景路人共用一條群組鎖定（`G1`）≤ 10。 |
| `continuity_in` / `continuity_out` | 寫主體位置與位於畫面哪一側、手上拿的道具、光線狀態、夜裡的時間點、攝影距離，或明確寫出 `Hard cut; …`。 |
| `shots[].id` | 全片鏡號，須與分鏡總表一致。 |
| `shots[].time` | Clip 內的相對時間。所有鏡頭加總必須剛好等於 Clip 時長，且任何一鏡都不得短於 1.5 秒。 |
| `shots[].type` | 景別＋角度＋運鏡／技法，用語取自 `shot-craft-library.md`。 |
| `shots[].action_prompt` | 電報式英文：不用冠詞與繫動詞，只用一到兩個動詞。**身分回聲放最前面：**`S1 (3–6 anchor words)`，每次都用同一組字，而且只能取自永久錨點（臉、髮型、體型、核心服裝），不能用角色之後會失去的物品。畫面中每個有鎖定的角色都要回聲，主角優先；路人只用群組 ID（`G1`）指稱。畫面中沒有角色時，改用道具或場景 ID 加上它的回聲開頭。只寫看得見的動作。不放畫面文字、不出現血腥，也不寫真人、導演或藝術家的名字。 |
| `shots[].audio_prompt` | 每一鏡都必填（見 §5）。 |

---

## §5 音軌規則

**標籤**
- 人聲（僅限畫面中有人物或角色，或其聲音確實在場時）：`[Breathing]` `[Sigh]` `[Gasp]` `[Laughter]` `[Crying]` `[Whisper]` `[Scream]` `[Humming]`
- 環境音（任何鏡頭皆可用）：`[Ambience]` `[Footsteps]` `[Foley]` `[SFX]` `[Silence]`
- 話語（僅限使用者提供）：`[Dialogue]` `[Narration]`

**規則**
- 每一鏡都要帶 `audio_prompt`。沒有角色的鏡頭只能用環境音標籤。
- 每鏡最多兩個標籤，真正推動敘事的聲音排在最前面。
- 聲畫關係：聲音屬於下一鏡或下一個 Clip 時，加上 `pre-lap:`。聲畫對位要刻意製造矛盾（例如不對勁的影子配上輕快的哼歌）。
- 揭示之前使用 `[Silence]`，是正當且極有力量的選擇。
- **不得自創台詞。** `[Dialogue] 'line'`／`[Narration] 'line'` 只有在使用者提供台詞，或明確要求加入時才會出現。沿用使用者的語言。**日文：只用平假名與片假名，不得使用漢字。**

**格式範例**
```
audio_prompt: "[Ambience] Wind through thorns, distant bell."
audio_prompt: "[Humming] Soft tuneless hum. [Footsteps] Bare feet on wet leaves."
audio_prompt: "[Silence] Total silence, then candle snuff."
audio_prompt: "[SFX] pre-lap: church bell from next scene."
audio_prompt: "[Dialogue] 'かえして…'"   # only because the user supplied it
```

---

## §6 asset_refs 結構（參考圖提示詞）

凡是標為待生成（`generate`）或 `user_image` 的資產，各輸出一筆。使用者會先把這些圖生成出來，再掛到對應的 Clip 上。

```yaml
asset_refs:
  - id: S1
    use: "{{turnaround / prop plate / scene plate}}; attach to {{C1-C3}}"
    prompt: >
      {{Sheet type}}, {{views}}, plain white background, even soft studio light.
      {{verbatim lock}}. {{art-style lock, render clause}}. Clean sheet without labels.
```

- **角色：**白底，正面、側面、背面全身圖，外加一張臉部特寫。
- **道具：**白底，一張四分之三角度的主視圖，外加一張細節圖。
- **場景：**一張不含角色的空景定場大遠景，光線狀態沿用鎖定描述。

---

## §7 字元上限

- 每個 Clip 的 YAML：**≤ 2500 字元**。整個專案只有一個 Clip 時：≤ 3000。
- `asset_refs` 沒有整段上限，因為每個條目都是獨立使用的 prompt；每個條目控制在 ≤ 600 字元。
- 某個 Clip 超出上限時，依下列順序刪減：
  1. `action_prompt` 裡的修飾語；
  2. 第二個音軌標籤；
  3. `summary` 的措辭；
  4. 合併一個鏡頭。
- **絕不在單一 Clip 裡縮短鎖定描述**——連戲全靠它們。鎖定描述在 Step 4 一次定好長度，並遵守 §4 的上限。若某個 Clip 仍然超標，就回到源頭（資產清單）縮短鎖定描述，再重新複製到**每一個** Clip，或把 Clip 拆開。

---

## §8 完整範例

**輸入：** 「一個小女孩提著裝滿螢光飛蛾的燈籠穿過荊棘森林，回到小屋照鏡子。30 秒。」

**設計假設：** 總長 30s；9:16；預設風格 A 觸感定格；無台詞；配樂留後製；所有資產為待生成。

### 🎬 導演意圖
- **片名**｜《蛾燈》
- **鉤子**｜公式 1 誤會型：她的影子為什麼慢了半拍？
- **敘事模板**｜G 童話變奏 ＋ D 遮蔽敘事
- **故事節拍**｜① 女孩提蛾燈穿林 → ② 樹幹上的影子慢半拍後停下 → ③ 小屋門自己打開，蛾在燈裡狂拍 → ④ 鏡中倒影轉頭、手掌貼玻璃 → ⑤ 鏡外的「她」笑得過寬，燭滅
- **資訊差**｜觀眾知道：影子不對、蛾在示警｜角色不知道：自己早已被換掉
- **情緒曲線**｜不安 → 懸疑累積 → 反轉驚懼 → 黑暗餘韻
- **反轉點**｜~18s 門自己開；~26s 鏡中人才是真身
- **視覺基調**｜冷夜；主色 `#1C2233`／`#E8DCC4`，點綴螢光綠 `#9BE564`；光源：蛾燈、單燭；禁用：暖陽、正面平光
- **鏡頭語言**｜靜止凝視為主；一次對稱慢推；前景懸疑；畫中畫（鏡子）
- **聲音設計**｜環境：風穿荊棘、蛾翅；聲畫關係：對位（哼歌 vs. 異常影子）；關鍵聲音：燭滅前的全然寂靜；配樂（後製）：走音音樂盒＋無旋律低弦
- **節奏**｜靜＋爆；畫面慢時聲音稀疏，反轉處雙軌同時收成寂靜

### 📦 資產清單
| ID | 資產 | 來源 | 鎖定錨點 |
|---|---|---|---|
| S1 | 女孩 | 待生成 | 瓷白皮膚、左頰細裂紋、大灰玻璃眼、墨黑齊短髮、磨損紅斗篷、赤腳 |
| P1 | 蛾燈 | 待生成 | 鳥籠式鐵燈籠，內有淡綠螢光飛蛾 |
| L1 | 荊棘林 | 待生成 | 黑色扭曲荊棘與樺樹、及膝霧、冷月光束 |
| L2 | 小屋內 | 待生成 | 傾斜木屋內、高大鏽銀橢圓鏡、單根蠟燭、浮塵 |

### 🗂 分鏡總表
| 鏡 | 時長 | 角度 | 景別 | 畫面內容 | 場景 | 聲音 | 備註 | 敘事目的 | Clip |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 00:00–00:04 | 俯拍 | 大遠景 | 渺小的女孩提蛾燈走在霧中小徑 | L1 | 風聲、遠鐘 | 靜止；負空間 | 建立｜孤身與光源設定 | C1 |
| 2 | 00:04–00:07 | 平視 | 全景 | 樹幹上的影子慢半拍後停下，女孩繼續走 | L1 | 哼歌；赤腳踩葉 | 側向跟拍；聲畫對位 | 揭示｜鉤子：影子不對 | C1 |
| 3 | 00:07–00:10 | 平視 | 近景 | 女孩平靜的臉，綠光映在玻璃眼中 | L1 | 哼歌持續 | 反應省略型 | 推進｜角色不知情 | C1 |
| 4 | 00:10–00:14 | 平視 | 遠景 | 小徑盡頭的傾斜小屋，荊棘拱門框住木門 | L1 | 風聲轉弱 | 對稱慢推 | 建立｜目的地與壓迫 | C2 |
| 5 | 00:14–00:17 | 微俯 | 特寫 | 燈籠裡的蛾瘋狂拍翅，光線閃爍 | L1 | 蛾翅急拍 | 插入鏡頭 | 強調｜蛾在示警 | C2 |
| 6 | 00:17–00:20 | 平視 | 過肩 | 木門自己緩緩打開，屋內漆黑 | L1 | 門軸長響；屏息 | 定點殺戮區 | 揭示｜反轉一 | C2 |
| 7 | 00:20–00:24 | 平視 | 中景 | 女孩站在燭旁的橢圓鏡前，倒影一致 | L2 | 呼吸；燭芯聲 | 畫中畫 | 推進｜假性安心 | C3 |
| 8 | 00:24–00:27 | 平視 | 特寫 | 鏡中倒影轉頭，手掌貼上玻璃；鏡外女孩不動 | L2 | 手掌輕叩玻璃 | 慢推；鏡像敘事 | 揭示｜反轉二 | C3 |
| 9 | 00:27–00:30 | 平視 | 近景 | 鏡外女孩嘴角咧得過寬，燭滅，只剩蛾光 | L2 | 全然寂靜→燭滅 | 遮蔽；淡出黑 | 情緒｜暗示收尾 | C3 |

### 🎞 Clip 提示詞

**C1｜00:00–00:10｜10s｜建立・揭示**
```yaml
project_meta:
  clip: "C1/3 | 00:00-00:10 | 10s"
  summary: "Girl crosses thorn forest; her shadow falls out of sync."
  art_style: "Gothic dark fairy-tale animated film, stop-motion-like tactile miniatures, grotesque-cute character design, cinematic chiaroscuro, bioluminescent accents, 35mm film grain"
  format: "9:16 vertical, 10s"
  bgm: "(none)"

subject_profile:
  visual_lock:
    S1: >
      Small girl, porcelain-pale skin, hairline crack on left cheek, large grey glass eyes, ink-black blunt bob, frayed crimson hooded cape, bare feet.
  prop_lock:
    P1: "Iron birdcage lantern, pale-green bioluminescent moths inside."
  scene_lock:
    L1: "Black thorn forest, twisted birches, knee-high fog, cold moonlight shafts."

multi_shot_sequence:
  continuity_in: "(opening clip)"
  shots:
    - id: 1
      time: "0-4s"
      type: "Extreme wide, high angle, locked-off"
      action_prompt: >
        S1 (porcelain girl, crimson hood, grey glass eyes) tiny on fog path, P1 held low, green glow sole light. L1. Vast dark negative space.
      audio_prompt: "[Ambience] Wind through thorns, distant bell."
    - id: 2
      time: "4-7s"
      type: "Full shot, eye level, lateral tracking"
      action_prompt: >
        S1 (porcelain girl, crimson hood, grey glass eyes) walks past birch trunks, P1 throws her shadow on bark. Shadow lags half-beat, then stops; S1 keeps walking.
      audio_prompt: "[Humming] Soft tuneless hum. [Footsteps] Bare feet on wet leaves."
    - id: 3
      time: "7-10s"
      type: "Medium close-up, eye level, static"
      action_prompt: >
        S1 (porcelain girl, crimson hood, grey glass eyes) calm face, green lantern glint in glass eyes, fog drifting behind. Unaware.
      audio_prompt: "[Humming] Hum continues, steady breath."
  continuity_out: "S1 walking screen-left to right, P1 in right hand, moonlit night, medium close-up."
```

**C2｜00:10–00:20｜10s｜建立・強調・揭示**
```yaml
project_meta:
  clip: "C2/3 | 00:10-00:20 | 10s"
  summary: "Cottage waits; moths panic; door opens by itself."
  art_style: "Gothic dark fairy-tale animated film, stop-motion-like tactile miniatures, grotesque-cute character design, cinematic chiaroscuro, bioluminescent accents, 35mm film grain"
  format: "9:16 vertical, 10s"
  bgm: "(none)"

subject_profile:
  visual_lock:
    S1: >
      Small girl, porcelain-pale skin, hairline crack on left cheek, large grey glass eyes, ink-black blunt bob, frayed crimson hooded cape, bare feet.
  prop_lock:
    P1: "Iron birdcage lantern, pale-green bioluminescent moths inside."
  scene_lock:
    L1: "Black thorn forest, twisted birches, knee-high fog, cold moonlight shafts."

multi_shot_sequence:
  continuity_in: "S1 walking screen-left to right, P1 in right hand, same moonlit night."
  shots:
    - id: 4
      time: "0-4s"
      type: "Wide, eye level, slow dolly push-in, one-point symmetry"
      action_prompt: >
        S1 (porcelain girl, crimson hood, grey glass eyes) small silhouette at frame bottom, facing crooked cottage at path's end; thorn arch frames door dead center. L1 fog.
      audio_prompt: "[Ambience] Wind fading, timber creak."
    - id: 5
      time: "4-7s"
      type: "Insert close-up, slight high angle, static"
      action_prompt: >
        P1 (birdcage lantern, green moths) moths beat wildly against bars, glow stutters. S1 crimson hood soft behind.
      audio_prompt: "[SFX] Frantic moth wings tapping iron."
    - id: 6
      time: "7-10s"
      type: "Over-the-shoulder from behind S1, locked-off"
      action_prompt: >
        S1 (porcelain girl, crimson hood, grey glass eyes) back to camera, foreground. Cottage door swings open by itself onto empty pitch-black interior.
      audio_prompt: "[SFX] Long hinge groan. [Breathing] One held breath."
  continuity_out: "Hard cut next: S1 inside cottage L2, P1 on floor, candle sole key light."
```

**C3｜00:20–00:30｜10s｜推進・揭示・情緒**
```yaml
project_meta:
  clip: "C3/3 | 00:20-00:30 | 10s"
  summary: "Mirror reflection turns; girl outside is not the real one."
  art_style: "Gothic dark fairy-tale animated film, stop-motion-like tactile miniatures, grotesque-cute character design, cinematic chiaroscuro, bioluminescent accents, 35mm film grain"
  format: "9:16 vertical, 10s"
  bgm: "(none)"

subject_profile:
  visual_lock:
    S1: >
      Small girl, porcelain-pale skin, hairline crack on left cheek, large grey glass eyes, ink-black blunt bob, frayed crimson hooded cape, bare feet.
  prop_lock:
    P1: "Iron birdcage lantern, pale-green bioluminescent moths inside."
  scene_lock:
    L2: "Crooked cottage interior, tall tarnished-silver oval mirror, single candle, drifting dust."

multi_shot_sequence:
  continuity_in: "Hard cut; inside L2, same night, P1 on floor glowing green, candle lit."
  shots:
    - id: 7
      time: "0-4s"
      type: "Medium, eye level, static, image-in-image"
      action_prompt: >
        S1 (porcelain girl, crimson hood, grey glass eyes) stands before mirror beside candle; reflection matches exactly. L2. Dim candle key, green P1 glow from floor.
      audio_prompt: "[Breathing] Slow breath. [SFX] Faint wick crackle."
    - id: 8
      time: "4-7s"
      type: "Close-up on mirror, eye level, slow push-in"
      action_prompt: >
        S1 (porcelain girl, crimson hood, grey glass eyes) reflection turns head toward real girl, presses palm to glass from inside. Real S1 motionless at frame edge.
      audio_prompt: "[SFX] Soft palm tap on glass."
    - id: 9
      time: "7-10s"
      type: "Medium close-up, eye level, static, fade to black"
      action_prompt: >
        S1 (porcelain girl, crimson hood, grey glass eyes) outside mirror, face half in shadow, smile slowly widening too far. Candle snuffs; green glow on jaw, then black.
      audio_prompt: "[Silence] Total silence, then candle snuff."
  continuity_out: "(final clip)"
```

### 🧩 參考圖提示詞
```yaml
asset_refs:
  - id: S1
    use: "Character turnaround; attach to C1-C3"
    prompt: >
      Character turnaround sheet, front, side, back full-body views plus face close-up, plain white background, even soft studio light.
      Small girl, porcelain-pale skin, hairline crack on left cheek, large grey glass eyes, ink-black blunt bob, frayed crimson hooded cape, bare feet. Gothic dark fairy-tale stop-motion-like tactile miniature. Clean sheet without labels.
  - id: P1
    use: "Prop plate; attach to C1-C3"
    prompt: >
      Prop sheet, three-quarter hero view plus detail view, plain white background, even soft studio light.
      Iron birdcage lantern, pale-green bioluminescent moths inside. Gothic dark fairy-tale stop-motion-like tactile miniature. Clean sheet without labels.
  - id: L1
    use: "Scene plate; attach to C1-C2"
    prompt: >
      Wide empty establishing plate, no characters. Black thorn forest, twisted birches, knee-high fog, cold moonlight shafts. Gothic dark fairy-tale stop-motion-like tactile miniature set, cinematic chiaroscuro, 35mm film grain.
  - id: L2
    use: "Scene plate; attach to C3"
    prompt: >
      Wide empty establishing plate, no characters. Crooked cottage interior, tall tarnished-silver oval mirror, single candle, drifting dust. Gothic dark fairy-tale stop-motion-like tactile miniature set, cinematic chiaroscuro, 35mm film grain.
```

**後製備註：** 片名《蛾燈》於 00:00–00:03 後製疊字；全片一條配樂（走音音樂盒＋低弦），00:27 起抽掉音樂留寂靜；C3 結尾淡出黑 1s；先生成 S1／P1／L1／L2 參考圖，再依 `use` 掛入各 Clip。
