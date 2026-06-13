# Anima 用 タグ辞書 (Anima Tag Dictionary)

Anima プロンプトのタグ並び順ブロックと、各カテゴリの実用タグ集。
本辞書は **Anima 記法**（小文字＋スペース、底線は使わない／`score_x` のみ底線保持）に統一済み。
> 記法の理屈・ハイブリッドの組み方は `anima-prompt-guide.md` を参照。

## ★ タグの並び順（区塊間はこの方向、区塊内は自由）
`[0] 品質/分数/分級/年代` → `[T] trigger words（指定時・必須）` → `[1] 人数` → `[2] 角色名` → `[3] 作品名` → `[4] @画師（指定時のみ）` → `[5] Subject 一般` → `[6] Background & Style` → `[7] Camera & Composition`

---

## 0. [Prefix]: 品質・分数・分級・年代（提示詞の冒頭固定ブロック）

二つの品質系統は単用・混用・不用すべて可。base は「素顔」なので品質タグは実質必須の起手。

- **品質① 人類評分式**: masterpiece, best quality, high quality, good quality, normal quality, low quality（←負面側）
- **品質② Pony 美学分数**: score_9, score_8, score_7, score_6, score_5, score_4, score_3, score_2, score_1 （★唯一、底線を保持）
- **分級 (Rating)** ※短いプロンプトでは特に明示し腦補を抑える: safe, sensitive, questionable, explicit
- **年代 (Year/Period)**: year 2025, year 2024, year 2023 …（明確年）／ newest, recent, mid, early, old（相対詞）
- **穏当な正面前綴（既定）**: `masterpiece, best quality, score_8, safe, year 2025`
- **🔑 Trigger Words（起動語・トリガータグ）** ※ユーザー指定時は**必須・原文のまま**: 上記前綴の直後（人数タグ付近）に置き、LoRA 等の活性化語・固有トリガーをそのまま列挙する（改変・省略・翻訳しない）。指定が無ければ何も足さない。
- **非動漫スイッチ** ※必要時のみ最冒頭に置く: ye-pop, deviantart（改行後の2行目に題名・alt-text 可）

---

## 1. [Count]: 主体人数
1girl, 1boy, 1other, solo, 2girls, 2boys, multiple girls, multiple boys, no humans, 12yo

## 2. [Character]: 角色名
※指定があれば配置。命名が割れる時は **Gelbooru 版**を採用。

## 3. [Copyright]: 作品名
※原作・シリーズ名。複数角色時は §5 の注意（分離記述）を守る。

## 4. [Artist]: 画師 ※指定がある時だけ（任意）
- **ユーザー指定がある時のみ**配置する。指定が無ければ画師タグも `@artist name` も**書かない**（空のプレースホルダを埋めない）。
- 記法: `@artist name`（`@` 無しは画風がほぼ乗らない）。Illustrious の `(artist_name:1.2)` は使わない。
- Anima は混風が弱い → 入れる場合も基本は単一画師。特定画風を**避けたい**時はネガティブ側に `@artist name` を置く。

---

## 5. [Subject]: キャラクター特徴（属性・外見）
キャラを形作る最重要要素。組み合わせで個性が生まれる。

- **髪型 (Hair style)**: long hair, very long hair, short hair, medium hair, twintails, ponytail, high ponytail, low ponytail, side ponytail, braid, braids, side braid, french braid, fishtail braid, bob cut, blunt bob, long bob, hime cut, classic pixie, pixie cut, pixie with undercut, bowl cut, pageboy, messy hair, shaggy, disheveled hair, ahoge, antenna hair, drill hair, twin drills, hair over one eye, sidelocks, long sidelocks, short bangs, blunt bangs, choppy bangs, swept bangs, curtain bangs, m-shaped bangs, bun, buns, updo, braided headband, center part bangs, parted bangs, one side up, half up, wavy hair, curly hair, straight hair, curls, fluffy hair, silky hair, wet hair, layered hair, hair intakes, pigtails, asymmetrical hair, wolf cut, alice band, forehead, hair slicked back, floating hair
- **髪色 (Hair color)**: blonde hair, blond, silver hair, black hair, pink hair, blue hair, white hair, gradient hair, multicolored hair, streaked hair
- **顔・目 (Face/Eyes)**: blue eyes, red eyes, green eyes, golden eyes, heterochromia, tsurime, tareme, glowing eyes, detailed eyes, sclera, mole under eye
- **表情 (Expression)**: smile, smirk, blush, tears, expressionless, angry, embarrassed, yandere, wink, seductive smile, wavy mouth, closed mouth, curious, sensual ※深掘りは `anime-expression-dictionary.md`
- **体型・肌・特徴 (Body/Skin)**: pale skin, tan, curvy, thighs, cleavage, collarbone, tall, petite, neckline, calves, midriff, breasts, belly button, navel, armpit, puffy legs, butt crack, small breasts, tattoo, prosthetic arm
- **服装 (Clothing)**: school uniform, sailor collar, sailor suit, sailor uniform, maid, gothic lolita, kimono, miko, sweater, cardigan, hoodie, swimsuit, bikini, side-tie bikini, wedding dress, cyberpunk outfit, armor, white shirt, pajamas, babydoll, linen dress, off shoulders, sleeveless, long top, plaid skirt, pleated skirt, short sleeves, dress shirt, leggings, tank top, overalls, halterneck, blouse, crop top, chemise, sneakers, loafers, pumps, baggy pants, open clothes, summer dress
- **服のディテール (Clothing details)**: frilled, spaghetti strap, oversized, embroidery, striped, pattern, juliet sleeves, slashed sleeves, holographic skirt
- **装飾品・属性 (Accessories/Tropes)**: animal ears, cat ears, elf ears, horns, hair ribbon, ribbon, thighhighs, pantyhose, zettai ryouiki, halo, bow tie, sash, bobby pin, hairclip, thigh strap, ornament, neckerchief, beanie, bow hairband, magical girl, cyborg, mecha, crystal wings, angel-shaped frame, halo-shaped hair accessory
  > ⚠ User Preference 禁止タグ（含めない）: glasses, megane, collar, choker, ruffle collar, earrings, ear piercing, stud earrings, hoop earrings, fluid art

## 6. [Background & Style]: 背景・画風
世界観・空気感・アートスタイルを決定づける。

- **画風・スタイル (Art Style)**: anime artwork, watercolor, oil painting, sketch, lineart, cel shading, impasto, manga style, retro artstyle, pop art, underwater photography, biomechanical sculpture, etching print, pen sketch, limited palette, pastel colors, pastel, character sheet, lofi aesthetic, soft shading, detailed background
- **テーマ・世界観 (Theme)**: cyberpunk, steampunk, fantasy, sci-fi, futuristic, science fiction, post-apocalyptic, dark fantasy, surrealism, urban dystopia, still life
- **時間・天候 (Time/Weather)**: day, night, sunset, sunrise, twilight, starry sky, rain, snow, cloudy, cumulonimbus cloud, sunlight, warm afternoon sunlight
- **屋内背景 (Indoor)**: classroom, bedroom, library, cafe, ruins, sci-fi laboratory, japanese style room, corridor, hallway
- **屋外背景 (Outdoor)**: cityscape, forest, beach, ocean, mountain, flower field, cyberpunk city, outer space, underwater, skyscrapers, skyline, recreational boat, megastructure
- **エフェクト・演出 (Effects)**: floating hair, flying petals, particles, light particles, depth of field, bokeh, chromatic aberration, lens flare, simple background, blurry background, blurry foreground, reflection, glitch, glowing magic circle, speech bubble, blue vfx, stardust effect, backlit outline

## 7. [Camera & Composition]: 撮影・構図
カメラマンの視点。ダイナミックさと視線をコントロールする。

- **カメラアングル (Camera Angle)**: from above, from below, from side, from back, dutch angle, dynamic angle, fisheye, front-facing, from diagonal front, high angle shot, side profile, eye-level shot, low-angle shot, straight-on angle, pov, straight on
  > ⚠ 純側面（`side profile`）はユーザー明示指定が無い限り不採用。代わりに「45度斜め正面」を使う。
  > 🎥 **張力アングルを既定化**: 水平の向き（front/diagonal/back）に加え、`low-angle shot`／`from below`（威厳・煽り）・`high-angle shot`／`from above`（可憐・上目遣い）・`dutch angle`（傾き・躍動）・`dynamic angle`（誇張遠近）を**必ず1つ併用**。平板な `eye-level shot`／`straight-on angle` を既定にしない。3シーンでアングルの種類も散らす。
- **フレーミング・距離 (Framing/Shot size)**: close-up, extreme close-up, portrait, front-view portrait, cowboy shot, upper body, bust, semi full body, full body, wide shot, very wide shot, extreme wide shot, panorama, medium shot, headshot, multiple views
- **視線 (Gaze)**: looking at viewer, looking away, looking over shoulder, looking back, looking to the side, eye contact, closed eyes
- **ポーズ・アクション (Pose/Action)**: standing, sitting, indian style sitting, yokozuwari, lying, jumping, walking, running, dynamic pose, fighting stance, leaning forward, leaning back, leaning, stretching, crossed legs, crossed arms, hands resting on cheeks, chin up, cheek to cheek, squatting, hands up, head tilt, v arms, arm up, arms outstretched, descending pose, reaching towards viewer, selfie, adjusting hair, tying hair, mouth hold, head support on hand
