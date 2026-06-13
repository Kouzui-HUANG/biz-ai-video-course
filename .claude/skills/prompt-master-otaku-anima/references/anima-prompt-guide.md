# Anima 提示詞撰寫指南 — タグ・自然言語・ハイブリッドの黄金比

Anima は Illustrious/SDXL とは「耳」が違う。本ガイドはその違いを前提に、Danbooruタグと自然言語をどう混ぜるかをまとめる。

---

## 0. なぜ Anima は違うのか（CLIP → Qwen3）

- SDXL の文字エンコーダは **CLIP**：文字をキーワード列に分解して画像特徴に対応させる。だからタグで餵え、75-token 上限と戦う必要があった。
- Anima の文字エンコーダは小型言語モデル **Qwen3**：**本当に文章を読んで意味を理解する。**
- 直接の帰結 → Anima は **①純タグ ②純自然言語 ③両者の混用** を同時に受け付ける。選ぶ必要はなく、その場で最も精密・最も楽な方を使う。
- **本スキルの既定は③ハイブリッド**（Illustrious 出身者の甜蜜點）。

---

## 1. 三つの書き方（同じ画面の例）

### ① 純タグ（Illustrious の習慣に最も近い）
```
masterpiece, best quality, score_8, safe, year 2025,
1girl, solo, silver hair, long hair, blue eyes, white sailor uniform,
@some artist,
sitting by a cafe window, warm afternoon sunlight, detailed background, soft shading
```

### ② 純自然言語
```
A masterful anime illustration of a silver-haired girl in a white sailor uniform, sitting by a cafe window in the warm afternoon light. She has long hair and blue eyes, gazing out at the street. Soft shading, detailed background.
```

### ③ ハイブリッド（既定・日常の甜蜜點）
```
masterpiece, best quality, safe,
A silver-haired girl in a white sailor uniform sits by a cafe window, gazing outside in the warm afternoon light.
1girl, solo, long hair, blue eyes, soft shading, detailed background
```

### 使い分けの判準
> **精密に制御したいもの → タグ。 関係・動作・構図を描くもの → 文。**
- タグが信頼できる：角色属性・画師・特定衣装（「言及したか否か」で差が大きい要素）。
- 文が綺麗：「誰が誰に何をしているか・誰がどこに立つか」という空間・敘事の関係。

---

## 2. タグ記法のルール（Illustrious と違う点）

1. **一律小文字・スペース、底線は使わない**：`long hair`（× `long_hair`）。**例外は score タグだけ底線を保持**（`score_8`）。Danbooru の底線形式とは逆＝最頻出の手滑り。
2. **タグの大まかな並び順**（区塊間はこの方向、区塊内は自由）：
   1. 品質／meta／年代／分級（`masterpiece, best quality, score_8, safe, year 2025`）
   2. 主体人数（`1girl` / `1boy` / `1other` …）
   3. 角色名
   4. 作品名
   5. 画師（`@` 必須、§4）
   6. 一般描述タグ（髪色・服装・動作・背景…）
3. **列挙し尽くさない**：Anima はタグ dropout 学習済み＝「情報不完全」に慣れている。関連タグを全部埋めず、要点を選ぶ。
4. **Gelbooru 優先**：Danbooru と Gelbooru で命名が違う時は Gelbooru 版を採る。

---

## 3. 自然言語のルール

- **十分に詳細に**：純自然言語ほど詳しく。最低でも2文相当の情報量。
- **短文は事故る**：短く籠統だと模型が「腦補」して予期せぬ（望まない）要素を生む。短文は必ず `safe` ＋十分なディテールと併用。
- **英語の大小写に従う**：言語モデルなので正常な英文記法が最も通る。
- **多角色は必ず分離記述**：2人以上いる時は各キャラの外見を別々に書く。混ぜると特徴が互いに沾染する（タグ流の「髪色が別人に黏く」回避と同じ理屈）。

---

## 4. 画師タグ — 指定がある時だけ `@`（任意）

- **画師はオプション（任意）**。ユーザーが画師を指定した時だけ入れる。**指定が無ければ画師タグもプレースホルダ `@artist name` も書かない**（空欄を無理に埋めない）。
- 入れる場合、Anima では画師名の前に **必ず `@`**：`@some artist` と書いて初めて画風が乗る。`@` 無しは効果がほぼ消える。
- Illustrious の `(artist_name:1.2)` 加重記法 → Anima では `@artist name` 形式に置き換える。
- **混風能力は Illustrious より弱い**：CLIP の無い新世代アーキは複数画師を独自風に煉る力が天生で弱い。`@` で単一画師を綺麗に効かせるのは得意だが、何人も重ねて新風を作るのは現状不得手。
- 応用：特定画風を**避けたい**時は、その画師タグ（同じく `@` 付き）を**ネガティブ**に置くと逆方向へ引ける。

---

## 5. 品質・分級・年代

### 品質タグ（2系統、単用・混用・不用すべて可）
- 人類評分式：`masterpiece, best quality, good quality …`
- Pony 美学分数：`score_9, score_8 … score_1`
- 併存可：`best quality, score_8`
- **base は「素顔」**：無指定だと中性・平淡になる。綺麗な仕上げには品質タグがほぼ必須。穏当な正面前綴 → `masterpiece, best quality, score_8, safe,`

### 分級タグ
- `safe` / `sensitive` / `questionable` / `explicit`。**短いプロンプトでは特に `safe` を明示**して腦補を抑える。

### 年代タグ
- 明確年：`year 2025` 等／相対詞：`newest / recent / mid / early / old`。
- Anima の動漫知識は **2025年9月まで**（新しめの角色・画師も認識する）。

---

## 6. 加重 — 手はこれまでより重く

- Anima も括弧加重に対応するが、**SDXL より重く**下げないと効かない。
- Illustrious の `(chibi:1.2)` 相当 → Anima では `(chibi:2)` 級。
- ある要素が出ない時は、**まず詞を換えず加重を上げる**。

---

## 7. ネガティブプロンプト

- 論理は SDXL と同じ（CFG で不要物を押し出す）。
- 起手式：
```
worst quality, low quality, score_1, score_2, score_3, jpeg artifacts, bad anatomy, bad hands
```
- 進階：ネガティブに画師タグ（`@` 付き）を入れて画風を逆方向へ引く（§4）。

---

## 8. 避けるべき地雷

- **日本語禁止**：Anima は日本語を解さない。英語に訳してから書く。
- **長すぎ禁止**：Qwen3 は容量が限られる。**約300語以内**。長いと截斷・焦点ボケ。
- **短すぎ・空虚禁止**：短く籠統＝腦補放任。ディテールを足し `safe` を付ける。
- **非動漫の芸術風**：プロンプト**最冒頭**にデータセットタグ `ye-pop` または `deviantart`（改行後の2行目に作品題名や alt-text を置いてもよい）。
- **長文レンダリング非推奨**：画中文字は単語・短句まで。整句は書けない。

---

## 9. Illustrious → Anima 移行対照（最終まとめ）

### Illustrious での書き方
```
masterpiece, best quality, 1girl, solo, silver hair, long hair, blue eyes,
white serafuku, (artist_name:1.2), cafe, window, sunlight, detailed background
```

### Anima へ移植
```
masterpiece, best quality, score_8, safe, year 2025,
1girl, solo, silver hair, long hair, blue eyes, white sailor uniform,
@artist name,
sitting by a cafe window, warm afternoon sunlight, detailed background, soft shading
```
（負面）
```
worst quality, low quality, score_1, score_2, score_3, jpeg artifacts, bad anatomy, bad hands
```

**4つの鍵となる変更点**＝本ガイドの要約：
1. 底線をスペースに（`long_hair` → `long hair`、score だけ底線維持）。
2. 画師を加重から `@` 前綴へ（`(artist_name:1.2)` → `@artist name`）。
3. `safe` ＋ 年代タグを補って出力を安定させる。
4. 自然言語を1文挿入して構図を明確化（`sitting by a cafe window...`）。

> 結局のところ Anima の難しさは技術ではなく、CLIP 時代の筋肉記憶を手放すこと。「人話が通じる」を受け入れれば、あとは生成数を重ねて手感を養うだけ。
