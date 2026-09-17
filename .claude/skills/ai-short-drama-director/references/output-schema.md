# Output Schema Reference（輸出格式）

Read before writing any output. Contents:
- §1 Full-mode Markdown frame
- §2 Direction-mode frame
- §3 Clip YAML schema
- §4 Field rules
- §5 Audio mechanism
- §6 asset_refs schema
- §7 Character budgets
- §8 Worked example

---

## §1 Full-Mode Markdown Frame（完整模式）

The planning sections are written in Traditional Chinese; the YAML is written in English. Output starts at 設計假設. There is no greeting and no closing question.

````markdown
**設計假設：**[one line — duration / ratio / style variant / dialogue / target model / asset sources, for anything inferred]

### 🎬 導演意圖
- **片名**｜《…》
- **鉤子**｜公式 N [type]：[one sentence — what the first 3 s make the audience ask]
- **敘事模板**｜[A–G name(s)]
- **故事節拍**｜① … → ② … → ③ …（3–6 beats, cause and turn only）
- **資訊差**｜觀眾知道：… ｜角色不知道：…
- **情緒曲線**｜… → … → …
- **反轉點**｜~Ns …；~Ns …
- **視覺基調**｜[tone]；主色 `#HEX`／`#HEX`，點綴 `#HEX`；光源：…；禁用：…
- **鏡頭語言**｜[core camera language + key techniques]
- **聲音設計**｜環境：…；聲畫關係：[同步／對位／延遲揭示]；關鍵聲音：…；配樂（後製）：…
- **節奏**｜[pattern] ＋ [dual-track note]

### 📦 資產清單
| ID | 資產 | 來源 | 鎖定錨點 |
|---|---|---|---|
| S1 | … | 使用者主體／使用者參考圖／待生成 | … |

### 🗂 分鏡總表
| 鏡 | 時長 | 角度 | 景別 | 畫面內容 | 場景 | 聲音 | 備註 | 敘事目的 | Clip |
|---|---|---|---|---|---|---|---|---|---|

### 🎞 Clip 提示詞
**C1｜00:00–00:10｜10s｜[purpose tags]**
```yaml
[Clip YAML — §3]
```
(repeat for each Clip)

### 🧩 參考圖提示詞
```yaml
[asset_refs — §6; omit this whole section if no asset is 待生成 or 使用者參考圖]
```

**後製備註：**[subtitles/titles with timecodes · score · fades · reference-attachment order · model caveats — 1–4 lines]
````

---

## §2 Direction-Mode Frame（方向提案模式）

Use this when the input is a mood or genre only, or when the user asks for directions. Output these three proposals, then **stop**.

````markdown
**方向提案**（尚未進入分鏡）

**方向 A｜《片名》**
- 一句話故事：…
- 鉤子：公式 N …
- 敘事模板：…
- 反轉：…
- 視覺記憶點：[motif + accent colour]
- 情緒曲線：…

**方向 B｜…**（different hook formula and template）

**方向 C｜…**（different hook formula and template）

請回覆 A／B／C（可混搭），並可指定：時長（預設 30s）・比例（預設 9:16）・風格（預設暗黑童話 A 觸感定格）・台詞／旁白（預設無）・目標模型。
````

---

## §3 Clip YAML Schema

One self-contained block per Clip. Keys are in fixed order, following prompt-master-video-continuity: `project_meta` → `subject_profile` → `multi_shot_sequence`.

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

## §4 Field Rules（欄位規則）

| Field | Rule |
|---|---|
| `project_meta.clip` | Clip index, global timecode and duration. Duration is 4–15 s. |
| `project_meta.summary` | One telegraphic line: the clip's beat. |
| `project_meta.art_style` | The style-bible lock, identical in every Clip. |
| `project_meta.format` | Ratio and duration, e.g. `9:16 vertical, 10s`. |
| `project_meta.bgm` | `"(none)"` unless the user asked for music. The film's score lives in 導演意圖 / 後製備註. |
| `subject_profile.*_lock` | Keyword stacks (no prose), copied verbatim from 資產清單 anchors. Include only assets that appear in this Clip. Append a state change after the base words (`…, hood now torn`). **Length caps:** lead character ≤ 25 words · supporting character ≤ 12 · prop ≤ 10 · scene ≤ 15 · background extras share one group lock (`G1`) ≤ 10. |
| `continuity_in` / `continuity_out` | Subject position and screen side, held props, light state, time of night, camera distance, or an explicit `Hard cut; …`. |
| `shots[].id` | Global shot number, matching the 分鏡總表. |
| `shots[].time` | Clip-local time. All shots sum exactly to the Clip duration, with no shot shorter than 1.5 s. |
| `shots[].type` | Shot size + angle + move/technique, using phrases from `shot-craft-library.md`. |
| `shots[].action_prompt` | Telegraphic English: no articles or copulas, one or two verbs. **Identity echo first:** `S1 (3–6 anchor words)`, the same words every time, built only from permanent anchors (face, hair, build, core garment), never from items the character later loses. Every locked character on screen gets an echo, lead first; extras are referenced by group ID only (`G1`). If no character is on screen, open with the prop or scene ID and its echo instead. Visible action only. No on-screen text, no gore, no real-person, director or artist names. |
| `shots[].audio_prompt` | Required on every shot (see §5). |

---

## §5 Audio Mechanism（音軌規則）

**Tags**
- Vocal (only when a human or character is visible or audibly present): `[Breathing]` `[Sigh]` `[Gasp]` `[Laughter]` `[Crying]` `[Whisper]` `[Scream]` `[Humming]`
- World (any shot): `[Ambience]` `[Footsteps]` `[Foley]` `[SFX]` `[Silence]`
- Words (user-supplied only): `[Dialogue]` `[Narration]`

**Rules**
- Every shot carries an `audio_prompt`. A shot with no character uses world tags only.
- At most two tags per shot. The sound that tells the story comes first.
- Sound–image relation: add `pre-lap:` when the sound belongs to the next shot or Clip. Use contradiction deliberately for counterpoint (a cheerful hum over a wrong shadow).
- `[Silence]` is a valid, powerful choice before a reveal.
- **No invented words.** `[Dialogue] 'line'` / `[Narration] 'line'` appear only when the user supplied the lines or explicitly asked for them. Keep the user's language. **Japanese: hiragana and katakana only, NO KANJI.**

**Formatting examples**
```
audio_prompt: "[Ambience] Wind through thorns, distant bell."
audio_prompt: "[Humming] Soft tuneless hum. [Footsteps] Bare feet on wet leaves."
audio_prompt: "[Silence] Total silence, then candle snuff."
audio_prompt: "[SFX] pre-lap: church bell from next scene."
audio_prompt: "[Dialogue] 'かえして…'"   # only because the user supplied it
```

---

## §6 asset_refs Schema（參考圖提示詞）

Emit one entry per asset tagged 待生成 (`generate`) or `user_image`. The user generates these images first and attaches them to the Clips.

```yaml
asset_refs:
  - id: S1
    use: "{{turnaround / prop plate / scene plate}}; attach to {{C1-C3}}"
    prompt: >
      {{Sheet type}}, {{views}}, plain white background, even soft studio light.
      {{verbatim lock}}. {{art-style lock, render clause}}. Clean sheet without labels.
```

- **Characters:** front, side and back full-body views plus a face close-up, on a white background.
- **Props:** a three-quarter hero view plus a detail view, on a white background.
- **Scenes:** one wide empty establishing plate with the lock's light state and no characters.

---

## §7 Character Budgets（字元上限）

- Each Clip YAML: **≤ 2500 characters**. A project with a single Clip: ≤ 3000.
- `asset_refs` has no block budget, because each entry is used as its own prompt. Keep each entry ≤ 600 characters.
- If a Clip runs over, cut in this order:
  1. modifiers in `action_prompt`;
  2. the second audio tag;
  3. `summary` wording;
  4. merge a shot.
- **Never shorten a lock inside one Clip** — locks are the continuity. Size locks once, at Step 4, within the §4 caps. If a Clip still runs over, shorten the lock at its source (資產清單) and re-copy it into **every** Clip, or split the Clip.

---

## §8 Worked Example（範例）

**Input:** 「一個小女孩提著裝滿螢光飛蛾的燈籠穿過荊棘森林，回到小屋照鏡子。30 秒。」

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
