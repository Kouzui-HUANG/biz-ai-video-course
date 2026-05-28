# Anime Expression & Facial Features Dictionary (アニメ表情・顔文字プロンプト辞典)

この辞書は、AIイラストにおける単調な「AI顔」を避け、キャラクターにより豊かで深い感情表現を持たせるためのプロンプトタグをまとめたものです。

## A. 視線方向 (Gaze / Looking Direction)
*   **正視**: `looking at viewer` - 何も指定しないと高確率で出現する正視。最も一般的なAI顔になりやすい。
*   **往下看 (Look Down)**: `look down` - 哀愁や物思いにふける感情を付与します。本やスマホを持っている構図と非常に相性が良いです。
*   **往旁看 (Look to the Side)**: `looking to the side` - 少しやましさや、心がここにあらずといった雰囲気を出せます。

## B. 笑顔1 (Smile 1)
*   **微笑**: `smile` - 最もおなじみの笑顔タグ。多用されるためAI顔になりやすい側面があります。
*   **閉眼微笑 (Smile & Closed Eyes)**: `smile, closed eyes` - 音楽を聴いている、自然を感じているなど、何かを楽しんでいる・浸っている表現に最適です。
*   **眯眼微笑 (Smile with Kaomoji)**: `smile, ^ ^` - 絵文字の「^ ^」は強力なプロンプトです。心底嬉しそうな、守りたくなるような笑顔を高い確率で生成します。

## C. 笑顔2 (Smile 2)
*   **邪媚笑 (Smug/Mischievous Smile)**: `smile, ^ ^, open eyes` - 目の開閉タグが衝突することで生まれる、目が半開きの怪しげな、あるいはイタズラっぽい特殊な笑顔です。
*   **燦爛笑 (Bright Smile with Teeth)**: `smile, ^ ^, teeth` - 歯を見せた屈託のない笑顔。
*   **露齒笑 (Grin)**: `grin` - 歯を見せてニヤリと笑う。少し企みを含んだり、ぎこちない笑顔になることもあります。

## D. 怒り1 (Angry 1)
*   **不悅 (Angry)**: `angry` - 基本的な怒った顔。
*   **不滿/嘟嘴 (Pouty)**: `angry, pouty` - 唇を尖らせた、少しすねたような可愛らしい不満顔。
*   **怒罵 (Angry Shouting)**: `angry, open mouth` - 口を開けて文句を言っているような怒り顔。

## E. 怒り2 (Angry 2)
*   **咬牙切齒 (Clenched Teeth)**: `angry, teeth` - 歯を食いしばるほどの怒り。
*   **暴怒 (Furious)**: `angry, clenched teeth, wide-eyed` - 見た瞬間に逃げたくなるような激怒の表情。
*   **怒罵/破口大罵 (Furious Shouting)**: `angry, open mouth, wide-eyed` - 目を見開いて激しく怒鳴りつけている表情。

## F. 哀しみ (Sadness)
*   **哀傷 (Sad)**: `sad` - デフォルトの悲しい表情。
*   **流淚 (Crying)**: `sad, crying` - 悲しみから涙を流している。
*   **哭泣 (Weeping)**: `sad, crying, closed eyes, open mouth` - 声を出して泣き崩れているような、泣きじゃくる表情。

## G. 心配・困惑・叫び (Worried, Confused, Screaming)
*   **擔心 (Worried)**: `worried` - 不安そうな表情。自信を喪失しているような効果があります。
*   **困惑 (Confused)**: `confused` - 困惑している表情。高確率で頭の上にクエスチョンマーク「？」が出現することがあります。
*   **張嘴叫 (Screaming)**: `screaming` - 叫んでいる顔。発声練習をしているように見えることもあります。

## H. 失神・ハイライト消え (Soulless / Empty Eyes)
*   **失神 (Soulless)**: `sad, empty eyes, expressionless` - 目からハイライトが消えた、いわゆる「壊れた」表情。
*   **失神流淚 (Soulless Crying)**: `sad, empty eyes, expressionless, crying` - ハイライトのない目で涙を流す、非常に痛ましい表情。
*   **失神半開眼 (Hypnotized/Trance)**: `sad, empty eyes, expressionless, jitome, half-closed eyes` - ジト目と半目が合わさり、催眠状態やトランス状態に見える表情。

## I. 楽しさ・爆笑 (Laughing)
*   **笑 (Laugh)**: `smile, open mouth, xd` - 絵文字「XD」を組み合わせることで、ぎこちなさのない自然で大きな笑顔になります。
*   **XD笑 (XD Face)**: `smile, open mouth, xd` または `><` - 漫画表現の「><」の目を本当に再現することがあります。「><」だけでも同様の効果が狙えます。
*   **憋笑 (Stifled Laugh)**: `smile, pouty, ^ ^` - ぷくっとさせた口と笑う目を組み合わせることで、笑いを堪えているような表情になります。

## J. 照れ・羞恥 (Embarrassed)
*   **害羞 (Embarrassed)**: `embarrassed` - デフォルトの赤面・照れ顔。少しAI顔になりがちです。
*   **難為情 (Shy / Looking Away)**: `embarrassed, half-closed eyes, looking to the side` - 目線を横に逸らすことで、より後ろめたさや気恥ずかしさが強調され、色気が生まれることもあります。
*   **混亂 (Confused/Dizzy)**: `embarrassed, open mouth, @_@, wavy mouth` - 「@_@」や波打つ口を合わせた、古典的なアニメの混乱表情。手を添えるなどのジェスチャーと好相性。

## K. 特殊な瞳 (Special Pupils)
*   **無眼白 (Black Sclera)**: `angry, black sclera, cat pupils` - 白目が黒くなり、猫目になる非常に邪悪で人外的な瞳。亜人やアンドロイドなどに適しています。
*   **愛心眼 (Heart-shaped Pupils)**: `smile, heart shaped pupils` - 瞳の中にハートマークが浮かぶ、非常に危険（？）な目。
*   **異色瞳 (Heterochromia)**: `heterochromia` - 左右で色が異なるオッドアイ。`heterochromia, blue eyes, red eyes` のように色を直接指定することも可能です。

## L. 異種族のパーツ (Non-human Facial Features)
*   **精靈耳 (Elf Ears)**: `pointy ears, elf ears` - エルフのような長く尖った耳。
*   **角 (Horns)**: `horns` - 悪魔や鬼のツノ。
*   **尖牙 (Fangs)**: `smile, open mouth, fangs` - 吸血鬼や獣人の特徴的な八重歯・牙。

## M. 驚訝・驚愕 (Surprise / Shock)
*   **驚訝 (Surprised)**: `surprised, wide-eyed` - 目を見開いた基本的な驚きの表情。
*   **驚呆 (Speechless/Shocked)**: `shocked, open mouth, blank stare` - 驚きすぎて言葉を失い、ぽかんと口を開けている状態。
*   **蒼白 (Pale with fear/shock)**: `pale, terrified, wide-eyed` - 恐怖やショックで顔面蒼白になっている状態。

## N. 魅惑・挑逗 (Seductive / Teasing)
*   **魅惑笑 (Seductive Smile)**: `seductive smile, half-closed eyes` - 色気のある挑発的な微笑み。
*   **眨眼 (Wink)**: `wink, smile` - 王道の可愛らしいウインク。
*   **上目遣い (Looking Up)**: `looking up, looking at viewer` - 上目遣いで相手を見つめる、甘えやあざとさを感じる視線。
*   **吐舌 (Tongue Out/Teasing)**: `tongue out, one eye closed` - あっかんべー、または茶目っ気のある「てへぺろ」の表情。

## O. 經典動漫符號 (Classic Anime Symbols & Expressions)
*   **流汗 (Sweatdrop)**: `sweatdrop` - 焦りや呆れを表す、おなじみの顔の横の汗マーク。
*   **爆青筋 (Anger Vein)**: `anger vein` - 怒っている時に額などに浮かぶ十字の青筋マーク。
*   **鼓頰 (Puffed Cheeks)**: `puffed cheeks, pouty` - ぷくーっと頬を膨らませた、子どもっぽいすねた表情。
*   **流口水 (Drooling)**: `drooling` - 寝ている時や、美味しいものを前にした時のよだれ。

## P. 惹人憐愛 (Endearing / Vulnerable)
*   **泛淚/淚眼汪汪 (Tearing Up)**: `tearing up, moist eyes` - まだ泣いてはいないが、目に涙が浮かんでいる状態。うるうるした瞳。
*   **楚楚可憐 (Pleading/Puppy Eyes)**: `pleading, looking up, moist eyes` - 捨て犬のように潤んだ瞳で見つめる、庇護欲をそそる表情。
