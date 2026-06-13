# アニメ女性キャラ髪型辞典 (Anime Female Hairstyle Dictionary for Anima Prompts)

キャラクターの髪型を正確にプロンプトで再現するためのタグリファレンス。これらは汎用 Danbooru 髪型タグで、Anima でもそのまま通用する。

> **使い方**: 「単体Tag」はそのまま使用。「組合せTag」は `+` で示した複数タグを併記すること。Anima 記法に従い**小文字＋スペース**で書く（底線は使わない）。
> **⚠ 注意**: 瀏海(前髪)の精密なコントロールはプロンプトだけでは限界がある。Anima では再現が弱い前髪・特殊髪型は **加重を重め（例 `(center part bangs:2)`）** に下げて押し出すこと（SD 系のような専用 LoRA は使わない）。

---

## A. 極短髪 (Very Short / Pixie)

| # | 中文名 | English Prompt Tag(s) | タイプ | キャラ属性・備考 |
|---|--------|----------------------|--------|-----------------|
| 1 | 剃鬢精靈短髮 | `pixie with undercut` | 単体 | サイバーパンク、戦闘系、欧米系キャラ向き |
| 2 | 經典精靈短髮 | `classic pixie` | 単体 | 大人っぽい、落ち着いた雰囲気 |
| 3 | 精靈短髮 | `pixie cut` | 単体 | 個性的でボーイッシュ、活発なキャラ |
| 4 | 西瓜皮妹妹頭 | `bowl cut` | 単体 | 通称マッシュルームカット。AI再現は完璧ではなく毛先が残る傾向 |

---

## B. 短髪 (Short Hair)

| # | 中文名 | English Prompt Tag(s) | タイプ | キャラ属性・備考 |
|---|--------|----------------------|--------|-----------------|
| 5 | 童花頭 | `pageboy` | 単体 | 幼い・可愛い系、学齢前の子供キャラ |
| 6 | 鮑伯頭 | `bob cut` | 単体 | 最も定番の短髪。AI再現はやや長めになる傾向 |
| 7 | 平切鮑伯頭 | `blunt bob` | 単体 | ボブの後髪が一刀平切。最も「ボブらしい」仕上がり。鬢髪はやや長め |
| 8 | 中長鮑伯頭 | `long bob` | 単体 | 前髪が鎖骨付近まで。欧米風、金髪+口紅と相性◎ |

---

## C. 中長髪 (Medium Length)

| # | 中文名 | English Prompt Tag(s) | タイプ | キャラ属性・備考 |
|---|--------|----------------------|--------|-----------------|
| 9 | 及肩中長髮 | `medium hair` | 単体 | 中長髪の基本。学生キャラに最適 |
| 10 | 睡醒毛躁 | `medium hair` + `shaggy` | 組合せ | 寝起きの無造作ヘア。だらしない・不精なキャラ |
| 11 | 公主頭(和) | `hime cut` | 単体 | 姫カット。平切り鬢髪+平切り前髪。`blunt bangs` + `blunt sidelocks` でも再現可 |
| 12 | 公主頭(洋) | `long hair` + `half-up` | 組合せ | ハーフアップ。上半分を結び、下半分を垂らす。ドレス・礼装と相性◎ |

---

## D. 前髪 (Bangs) ※精密制御は困難

| # | 中文名 | English Prompt Tag(s) | タイプ | 備考 |
|---|--------|----------------------|--------|------|
| 13 | 齊瀏海 | `blunt bangs` | 単体 | 平切り前髪。比較的安定 |
| 14 | 碎瀏海 | `choppy bangs` | 単体 | 不規則な前髪 |
| 15 | 短瀏海 | `short bangs` | 単体 | 眉上の短い前髪。本来 `baby bangs` だがモデルが認識しにくいため代替 |
| 16 | 中分 | `center part bangs` | 要加重⚠ | プロンプトだけでは不安定。Anima では `(center part bangs:2)` 級の加重で押す |

---

## E. 長髪 / 長尾 (Long Hair / Long Ponytail)

| # | 中文名 | English Prompt Tag(s) | タイプ | キャラ属性・備考 |
|---|--------|----------------------|--------|-----------------|
| 17 | 長髮 | `long hair` | 単体 | 肩を超える長髪の基本形 |
| 18 | 單馬尾 | `long hair` + `ponytail` | 組合せ | 正面長髪の状態でponytailは中央に結ぶのがデフォルト |
| 19 | 雙長馬尾 | `long hair` + `twintails` | 組合せ | 人気キャラの定番。`pigtails` でも同じ効果。現実では違和感あり |
| 20 | 側邊單馬尾 | `long hair` + `side ponytail` | 組合せ | 人妻感・大人の色気を出す結び方 |

---

## F. 短尾 / お団子 (Short Ponytail / Bun)

| # | 中文名 | English Prompt Tag(s) | タイプ | キャラ属性・備考 |
|---|--------|----------------------|--------|-----------------|
| 21 | 側邊單短馬尾 | `short hair` + `side ponytail` | 組合せ | 片側だけの短いポニーテール |
| 22 | 短雙馬尾 | `short hair` + `pigtails` | 組合せ | 妹系キャラ感。髪飾りを足すとさらに◎ |
| 23 | 單包頭 | `bun` | 単体 | 色気のある結び方。浴衣・バスローブと相性抜群 |
| 24 | 雙包頭 | `buns` | 単体 | チャイナドレス・漢服とほぼセット |

---

## G. 三つ編み / 短カール (Braid / Short Curly)

| # | 中文名 | English Prompt Tag(s) | タイプ | キャラ属性・備考 |
|---|--------|----------------------|--------|-----------------|
| 25 | 單辮髮 | `braid` | 単体 | 中世ファンタジー女騎士風 |
| 26 | 雙辮子 | `braids` | 単体 | ⚠ 黒縁メガネとの組合せは避けること（ステレオタイプ化） |
| 27 | 短捲髮 | `short hair` + `wavy hair` | 組合せ | 画面の美感を高める。動きのある仕上がり |
| 28 | 卷鮑伯頭 | `bob cut` + `wavy hair` | 組合せ | 台湾女性に最もよく見られる髪型。美容院帰り感 |

---

## H. その他・特殊 (Other / Special)

| # | 中文名 | English Prompt Tag(s) | タイプ | キャラ属性・備考 |
|---|--------|----------------------|--------|-----------------|
| 29 | 短髮長鬢 | `short hair` + `long sidelocks` | 組合せ | 顔の輪郭をカバー。初心者が描きやすい定番 |
| 30 | 長髮髮箍 | `long hair` + `forehead` + `alice band` | 組合せ | 額を出すには `forehead` と `alice band` の両方が必要 |
| 31 | 長髮微卷 | `long hair` + `curls` | 組合せ | 天然系or腹黒お嬢様の専用髪型 |
| 32 | 不對稱短髮 | `asymmetrical hair` + `short hair` | 組合せ | 左右非対称。パンク・前衛的なキャラ |
| 33 | 狼尾剪 | `wolf cut` | 単体 | レイヤー多めの80年代風。ロック系・反骨精神キャラ |

---

## I. アニメ定番・二次元専用 (Anime-Iconic Styles)

| # | 中文名 | English Prompt Tag(s) | タイプ | キャラ属性・備考 |
|---|--------|----------------------|--------|-----------------|
| 34 | 呆毛 | `ahoge` | 単体 | 頭頂の飛び出た一本毛。天然・ドジっ子の象徴。他の髪型と自由に組合せ可 |
| 35 | 鑽頭捲/公主捲 | `drill hair` | 単体 | 縦ロール。お嬢様・ツンデレの定番 |
| 36 | 雙鑽頭捲 | `twin drills` | 単体 | 両側の縦ロール。高飛車お嬢様のステレオタイプ |
| 37 | 遮眼髮 | `hair over one eye` | 単体 | 片目を隠す。ミステリアス・クール・中二病キャラ |
| 38 | 觸角髮 | `antenna hair` | 単体 | ahogeの変形。2本以上の髪が触角のように立つ |
| 39 | 超長髮 | `very long hair` | 単体 | 腰〜膝以下の超長髪。神秘的・お姫様系。`long hair` より更に長い |
| 40 | 亂髮 | `messy hair` | 単体 | 全体的にボサボサ。戦闘後・寝起き・野生系 |
| 41 | 低馬尾 | `low ponytail` | 単体 | 首の低い位置で結ぶ。落ち着いた大人の雰囲気。メイド・文学少女 |
| 42 | 高馬尾 | `high ponytail` | 単体 | 頭頂近くで結ぶ。活発・スポーティ |
| 43 | 片側結び | `one side up` | 単体 | 片側だけ上に結ぶ。カジュアルで可愛い |
| 44 | 側編辮子 | `side braid` | 単体 | 片側に流した三つ編み。エルフ・森系キャラと相性◎ |
| 45 | 法式編髮 | `french braid` | 単体 | フレンチブレイド。上品。貴族・メイド長 |
| 46 | 魚骨辮 | `fishtail braid` | 単体 | 細かい編み込み。ボヘミアン・自然派キャラ |
| 47 | 盤髮 | `updo` | 単体 | まとめ上げた正装ヘア。パーティ・結婚式 |
| 48 | 編込みカチューシャ | `braided headband` | 単体 | 編み込みをカチューシャ状に。中世ファンタジー・妖精風 |

---

## J. 前髪バリエーション追加 (Advanced Bangs)

| # | 中文名 | English Prompt Tag(s) | タイプ | 備考 |
|---|--------|----------------------|--------|------|
| 49 | 斜瀏海 | `swept bangs` | 単体 | 横に流した前髪。最も自然で汎用的 |
| 50 | 窗簾瀏海 | `curtain bangs` | 単体 | 中央から左右に分かれるカーテン状。韓国風おしゃれ系 |
| 51 | 瀏海夾 | `hair clip on bangs` | 単体 | ヘアピンで前髪を留める。日常系・元気キャラ |
| 52 | M字瀏海 | `m-shaped bangs` | 単体 | 中央が短く両側が長いM字型。特定キャラの再現に |
| 53 | 額出し(オールバック) | `forehead` + `hair slicked back` | 組合せ | 前髪なし。`forehead` 単独では不十分 |

---

## K. 髪質・ボリューム修飾子 (Hair Texture & Volume Modifiers)

> 独立した髪型ではなく、上記の髪型タグに**追加併用**するモディファイア。

| 中文名 | English Prompt Tag(s) | 効果 |
|--------|----------------------|------|
| 直髮 | `straight hair` | ストレートを強調。くせ毛を防ぐ |
| 捲髮 | `curly hair` | 全体カール。`wavy hair` より強いうねり |
| 微捲 | `wavy hair` | ゆるいウェーブ。自然な動きを出す |
| 蓬鬆髮 | `fluffy hair` | ふわふわ軽い質感。可愛い系キャラ |
| 柔順光澤 | `silky hair` | サラサラ艶やか。お嬢様・黒髪ロングと相性◎ |
| 濕髮 | `wet hair` | 濡れた髪。入浴・雨・海のシーン |
| 風になびく | `floating hair` / `wind-swept hair` | 風で髪が揺れる。ダイナミックな演出 |
| 散亂 | `disheveled hair` | `messy hair` より激しい乱れ。戦闘後・感情シーン |
| 層次感 | `layered hair` | レイヤーカット。動きと立体感 |
| 頭髮光環 | `hair intakes` | 髪の間の空気感。二次元特有のV字アクセント |

---

## L. 髪飾り・アクセサリー (Hair Accessories)

> 髪型のニュアンスを大きく左右する追加要素。

| 中文名 | English Prompt Tag(s) | 効果・備考 |
|--------|----------------------|-----------|
| 蝴蝶結髮帶 | `bow hairband` / `hair bow` | 頭上のリボン。可愛い系・ロリータ |
| 髮箍 | `headband` / `alice band` | カチューシャ。`alice band` がアニメ向き |
| 髮夾 | `hairclip` / `hair pin` | ヘアピン。日常系 |
| 髮帶 | `hair ribbon` | リボンで結ぶ。ポニーテール・ツインテと組合せ |
| 花飾 | `flower in hair` | 髪に飾った花。和装・春のシーン |
| 髮簪 | `kanzashi` / `hair ornament` | 簪。和装・着物と相性◎ |
| 頭紗 | `head veil` | ベール。花嫁・修道女・中東風 |
| 貓耳髮箍 | `cat ear headband` | 猫耳カチューシャ。コスプレ用（本物は `cat ears`） |
| 王冠 | `tiara` / `crown` | ティアラ。お姫様・アイドル |
| 螺旋髮圈 | `scrunchie` | シュシュ。カジュアル・90年代風 |

---

## M. 髪色エフェクト (Hair Color Effects)

> 単色タグ（`blonde hair` 等）は `anima-tags.md` 参照。ここでは複雑な色彩表現をカバー。

| 中文名 | English Prompt Tag(s) | 効果・備考 |
|--------|----------------------|-----------|
| 漸層髮色 | `gradient hair` | 根元→毛先のグラデーション |
| 雙色髮 | `multicolored hair` / `split-color hair` | 左右や内外で色が異なる |
| 挑染 | `streaked hair` / `hair highlights` | ハイライトメッシュ |
| 內層染色 | `colored inner hair` | インナーカラー。動かすと見える隠れた色 |
| 髮尾染色 | `dyed tips` | 毛先だけ色が違う |
| 光澤反射 | `hair shine` / `glossy hair` | 天使の輪・光沢表現 |

---

## 実践ノート (Practical Notes)

### 組合せテクニック
- **基本構造 = 髪長 + スタイル + (前髪) + (質感) + (飾り)**: 最大5層の組合せで精密指定可能
  - 例: `long hair, ponytail, blunt bangs, silky hair, hair ribbon` = 齊瀏海のサラサラポニーテール+リボン
- **瀏海は独立指定**: 髪型タグに加えて `blunt bangs`, `choppy bangs`, `short bangs` 等を追加可
- **`pigtails` = `twintails`**: 同義語。AI的に同等の結果
- **髪長の強度階層**: `short hair` < `medium hair` < `long hair` < `very long hair`
- **質感の重ね掛け**: `wavy hair` + `fluffy hair` のように複数指定で効果が合成される

### AI再現の限界と対策（Anima）
> Anima では「効かない要素はまず詞を換えず**加重を上げる**」。SD 系の LoRA に頼らず `(tag:2)` 級で押すのが基本。
- **Bob Cut**: 単独では理想より長くなりがち → `blunt bob` で改善
- **中分 (Center Part)**: プロンプトだけでは不安定 → `(center part bangs:2)` 級に加重
- **額出し (Forehead)**: `forehead` 単独では不十分 → `alice band` や `hair slicked back` を併用
- **Bowl Cut**: 完璧な再現は難しく、毛先が残る傾向 → `(bowl cut:1.5)` 前後で強調
- **Drill Hair**: 単体で1本になりがち → `twin drills` で両側を明示
- **Very Long Hair vs Long Hair**: 差が出にくい → `hair past waist` を追加で強調
- **Wet Hair**: 全体が塗れすぎる → シーン(rain, shower)と組み合わせると自然
- **Asymmetrical Hair**: 無視されやすい → `short on one side` を補強タグ＋加重で追加

