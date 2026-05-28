# Stable Diffusion 用 品質＆属性タグ辞書 (SD Tags Dictionary)

プロンプト生成時に必ず組み込む要素のリストです。

## 1. [Quality]: 品質アップタグ
画像全体の解像度、書き込み量、レンダリングの美しさを底上げするタグです。
- **基本の高品質化**: masterpiece, best quality, high quality, highres, absurdres, 8k resolution, latest
- **書き込み・ディテール強化**: ultra-detailed, highly detailed, intricate details, extremely detailed CG unity 8k wallpaper, finely detailed, stunning illustration
- **光と影・レンダリング**: cinematic lighting, studio lighting, physically-based rendering / pbr, hdr, ray tracing, volumetric lighting, Front-lighting, silhouette
- **芸術的評価・雰囲気**: award winning, trending on artstation, pixiv fanbox, very aesthetic, elegant

## 2. [Subject]: キャラクター特徴（属性・外見）
キャラクターを形作る最も重要な要素です。組み合わせることで個性が生まれます。
- **基本人数・年齢**: 1girl, 1boy, solo, multiple girls, 12yo, no human
- **髪型 (Hair style)**: long hair, very long hair, short hair, medium hair, twintails, ponytail, high ponytail, low ponytail, side ponytail, braid, braids, side braid, french braid, fishtail braid, bob cut, blunt bob, long bob, hime cut, classic pixie, pixie cut, pixie with undercut, bowl cut, pageboy, messy hair, shaggy, disheveled hair, ahoge, antenna hair, drill hair, twin drills, hair over one eye, sidelocks, long sidelocks, short bangs, blunt bangs, choppy bangs, swept bangs, curtain bangs, M-shaped bangs, bun, buns, updo, braided headband, middle part bangs, parted bangs, one side up, half-up, wavy hair, curly hair, straight hair, curls, fluffy hair, silky hair, wet hair, layered hair, hair intakes, pigtails, asymmetrical hair, wolf cut, alice band, forehead, hair slicked back, floating hair
- **髪色 (Hair color)**: blonde hair, blond, silver hair, black hair, pink hair, blue hair, white hair, gradient hair, multicolored hair, streaked hair
- **顔・目 (Face/Eyes)**: blue eyes, red eyes, green eyes, golden eyes, heterochromia, tsurime, tareme, glowing eyes, detailed eyes, sclera, mole under eye
- **表情 (Expression)**: smile, smirk, blush, tears, expressionless, angry, embarrassed, yandere, wink, seductive smile, wavy mouth, closed mouth, curious, sensual
- **体型・肌・特徴 (Body/Skin)**: pale skin, tan, curvy, thighs, cleavage, collarbone, tall, petite, neckline, calves, midriff, breasts, belly button, navel, armpit, puffy legs, butt crack, small breasts, tattoo, prosthetic arm
- **服装 (Clothing)**: school uniform, sailor collar, sailor suit, maid, gothic lolita, kimono, miko, sweater, cardigan, hoodie, Hoodie, swimsuit, bikini, side-tie bikini, wedding dress, cyberpunk outfit, armor, white shirt, pajamas, Babydoll, linen dress, off shoulders, sleeveless, long top, plaid skirt, pleated skirt, short sleeves, dress shirt, leggings, tank top, overalls, halterneck, blouse, crop top, Chemise, clothes, sneakers, loafers, pumps, Baggy pants, open clothes, summer dress
- **服のディテール (Clothing details)**: frilled, Spaghetti strap, oversized, embroidery, striped, pattern, juliet sleeves, slashed sleeves, holographic skirt
- **装飾品・属性 (Accessories/Tropes)**: glasses / megane, animal ears, cat ears, elf ears, horns, choker, hair ribbon, ribbon, thighhighs, pantyhose, zettai ryouiki, halo, bow tie, sash, Sash, bobby pin, hairclip, thigh strap, ornament, neckerchief, beanie, bow hairband, magical girl, cyborg, Mecha, crystal wings, angel-shaped frame, halo-shaped hair accessory

## 3. [Background & Style]: 背景・画風
イラストの世界観や空気感、アートスタイルを決定づけます。
- **画風・スタイル (Art Style)**: anime artwork, watercolor, oil painting, sketch, lineart, cel shading, impasto, manga style, retro artstyle, pop art, Fluid Art, Underwater Photography, Biomechanical Sculpture, etching print, pen Sketch, limited palette, pastel colors, pastel, character sheet, lofi aesthetic
- **アーティスト**: Greg Rutkowski
- **テーマ・世界観 (Theme)**: cyberpunk, steampunk, fantasy, sci-fi, futuristic, science fiction, post-apocalyptic, dark fantasy, Surrealism, urban dystopia, still life
- **時間・天候 (Time/Weather)**: day, night, sunset, sunrise, twilight, starry sky, rain, snow, cloudy, cumulonimbus cloud, sunlight
- **屋内背景 (Indoor)**: classroom, bedroom, library, cafe, ruins, sci-fi laboratory, japanese style room, corridor, hallway
- **屋外背景 (Outdoor)**: cityscape, forest, beach, ocean, mountain, flower field, cyberpunk city, outer space, underwater, skyscrapers, skyline, recreational boat, megastructure
- **エフェクト・演出 (Effects)**: floating hair, flying petals, particles, light particles, depth of field / dof, depths of field, bokeh, chromatic aberration, lens flare, simple_background, blurry_background, blurry_foreground, reflection, glitch, glowing magic circle, speech bubble, blue vfx, stardust effect, backlit outline

## 4. [Camera & Composition]: 撮影・構図
カメラマンの視点となり、イラストのダイナミックさや視線をコントロールします。
- **カメラアングル (Camera Angle)**: from above, from below, from side, from back, dutch angle, Dutch angles, dynamic angle, fisheye, front-facing, from diagonal front, high angle shot, side profile, eye-level Shot, Low-angle Shot, Straight-on Angle, pov, straight on
- **フレーミング・距離 (Framing/Shot size)**: close-up, extreme close-up, portrait, Front-view portrait, cowboy shot, cowboy_shot, upper body, upper_body, bust, semi full body, full body, wide shot, very wide shot, Extreme Wide Shot, panorama, Medium Shot, headshot, multiple views
- **視線 (Gaze)**: looking at viewer, looking away, look away, looking over shoulder, looking back, looking to the side, eye contact, closed eyes, closed_eyes
- **ポーズ・アクション (Pose/Action)**: standing, sitting, indian style, sitting, yokozuwari, lying, lie down, jumping, walking, running, dynamic pose, fighting stance, leaning forward, leaning back, Leaning, stretching, crossed legs, crossed arms, with her hands resting on her cheeks, chin up, Stick cheek to cheek, squat down, hands up, head tilt, v arms, arm up, arms outstretched, descending pose, attacking viewer with sword, reaching towards viewer, selfie, adjusting hair, hair tie in mouth, tying hair, mouth hold, hair tie, head support on hand
