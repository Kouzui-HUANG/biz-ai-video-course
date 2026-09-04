# biz-ai-video-course — Claude Code Skills スキル集／技能集合

> 🌐 **Bilingual README ｜ バイリンガル説明文件**
> 先に **日本語** を完全収録し、続いて **繁體中文** を記載しています。／日文版完整在前，繁體中文版在後。
> ⬇️ [日本語](#日本語) ｜ [繁體中文](#繁體中文)

---

# 日本語

このプロジェクトには **42 個の専門 Skill** が集まっており、**ビジネスコンテンツ制作**、**AI 映像生成（動態生成＝モーション生成 / テキスト → 動画 / 画像 → 動画）**、**画像プロンプトエンジニアリング**、**脚本・キャラクター創作**、さらに **GMI Cloud API を直接呼び出して画像・動画を出力する実行ツール** まで幅広くカバーします。すべての Skill は `.claude/skills/` ディレクトリ配下に置かれており、Claude Code が対応するトリガーワードを検出すると自動で読み込んで実行するため、手動での設定は不要です。

---

## 📂 スキル分類一覧

### 1️⃣ Skill 管理・構築ツール

skill そのものを作成・最適化・翻訳するためのメタツール（meta-tools）。

| Skill 名 | 用途 |
|---|---|
| [skill-creator](.claude/skills/skill-creator/SKILL.md) | 新しい skill を作成したり、既存の skill を修正したりするための標準作業手順（SOP）ガイド。仕上げに skill-optimizer と skill-translator を自動で呼び出して連携します。 |
| [skill-optimizer](.claude/skills/skill-optimizer/SKILL.md) | 既存の SKILL.md をリファクタリング・圧縮するツール。「漸進的開示（Progressive Disclosure）」の原則を適用して SKILL.md を 100〜200 行以内に抑え、context window の汚染を防ぎます。 |
| [skill-translator](.claude/skills/skill-translator/SKILL.md) | SKILL.md を人間が読みやすい繁体字中国語版に翻訳して `docs/` フォルダに保存します。AI の実行時の context には **いっさい影響しません**。 |

---

### 2️⃣ キャラクター・脚本創作

断片的な手がかりからキャラクターを逆算して組み立て、その名前に神話的な奥行きを与え、一行のアイデアを脚本の初稿へ書き起こし、既存の脚本を深く読み解いてショットに翻訳します。

| Skill 名 | 用途 |
|---|---|
| [character-architect](.claude/skills/character-architect/SKILL.md) | ハリウッド脚本家 ＋ キャラクターアーキテクト（アカデミー賞級、社会学・心理学的な洞察を兼ね備える）。一行のセリフ、一つの小物、あるいは写真一枚の構図や光と影といった断片的な手がかりからキャラクターを逆算して組み立て、互いの違いを最大化しつつ、それぞれ内部で破綻のない繁体字中国語のキャラクター設定書を **3 つ** 生成します（外見・社会的属性、家庭環境とトラウマ、MBTI・星座・血液型の一貫性、口癖やマイクロ表情 ＋ 映画級のサマリー）。トリガーワード：「角色設定」「人設」「人物塑造」など。 |
| [cultural-naming-director](.claude/skills/cultural-naming-director/SKILL.md) | 文化共鳴ネーミングマスター（文化共鳴命名大師）。キャラクター（あるいは陣営・地名・武器・作品タイトルといった、物語上のあらゆる対象）の心理スペクトル（混沌↔秩序・利己↔利他・能動↔受動）と致命的な欠陥、そして辿るであろう運命を読み取り、12 文化からなる「世界神話マトリクス」（中国・日本・ヒンドゥー・ギリシャローマ・北欧・ケルト・スラヴ・アブラハム神秘主義・エジプト・メソポタミア・南北アメリカ先住民・ペルシャ）から元型の候補を引き出します。あえて安直な選択を避ける対抗テストを通したうえで、語根の再結合や概念の翻訳といった「命名の錬金術」で名前を鍛え、元型の出典・神話的な背景・対応のロジック（表層の結びつき／欠陥と運命への深層の共鳴／文化的な緊張）まで繁体字中国語で解説します。テキストのみ出力。トリガーワード：「命名」「改名」「角色取名」「有寓意的名字」など。※ 設計するのは **名前** であって、人物像そのものの作り込みは character-architect の担当です。 |
| [screenwriter-architect](.claude/skills/screenwriter-architect/SKILL.md) | エリート脚本家 ＋ 物語アーキテクト（編劇架構師／脚本の第一稿）。一行の思いつきや半端なアイデアを、そのまま撮れる繁体字中国語の **脚本第一稿** に仕上げます。フェーズ 1【立項問診】では ABCD 形式の質問ブロックを 1 回だけ提示し、設定（主人公と欲望・時代と場所・ジャンルとトーン・言語）／筋立て（発端の事件・敵対する力・結末の立場・テーマの主張）／尺（尺・プラットフォーム・製作条件）をまとめて確認。すべての設問に ✔推薦 のデフォルトが付いているので「全部照推薦」と答えるだけでも進みます。フェーズ 2【多稿淬煉】では、ユーザーに 1 行も見せないまま 構造審査 → 声（口調）審査 → セリフの淬煉 → 最終チェックリスト という 3 巡以上の書き直しを内部で回すため、受け取る「第一稿」は実質 3〜4 稿目です。形容詞ではなく具体物で語る、答えをずらす、反復と変奏、語彙レジスターの衝突——詩情と含みがありながら気取らないセリフと、シーン単位の 目標–障害–結果 ＋「だから／しかし」の因果設計、外化・客観的相関物、伏線と回収、予算感覚を得意とします。テキストの脚本のみ出力。トリガーワード：「寫劇本」「劇本創作」「短片劇本」「編劇」など。 |
| [script-doctor-architect](.claude/skills/script-doctor-architect/SKILL.md) | ハリウッド最高峰のスクリプトドクター。脚本を受け取ると、緻密に構造化された「脚本分析レポート」を作成し、物語構造・キャラクター心理・出来事の時系列・市場でのポジショニングを細かく分解します。 |
| [shot-script-director](.claude/skills/shot-script-director/SKILL.md) | 映画監督 ＋ 画面転写アーキテクト（分鏡導演）。短い脚本・台詞・散文の断片を、4〜6 個（通常 4〜5 個）の cut からなる構造化された「分鏡腳本（ショット・ブレイクダウン）」に翻訳します。各 cut は 景別・アングル／被写体／シーン／カメラワーク／雰囲気・情緒／セリフ・演技 を明記。「意味は隙間に宿る」という改編理論（外化・客観的相関物、サブテキスト、情報の経済＝サスペンス、時間の再構築、**台詞の転写＝「そもそも言う必要があるか」を問い、口語化・声の個別化・沈黙まで**）に基づき、説明しすぎず観客に推論させます。テキストの脚本のみを出力し、画像・動画は生成しません。トリガーワード：「分鏡腳本」「拍攝劇本轉譯」「劇本轉分鏡」など。※ storyboard-director（AI 描画 prompt を出力）とは別物です。 |

---

### 3️⃣ 画像プロンプトエンジニアリング — 人物 / ポートレート

AI 画像生成モデル（Midjourney、Seedream、Nano Banana、SD）向けに設計された、人物系のプロンプトエンジニア。

| Skill 名 | 用途 |
|---|---|
| [prompt-master-portrait](.claude/skills/prompt-master-portrait/SKILL.md) | 写真品質のポートレート／キャラクター設計プロンプトエンジニア。8〜12 項目の深掘りヒアリングを必ず行い、バイリンガル（EN/ZH）の精密なプロンプトを 3 つ生成します。細部を勝手に推測・**捏造することはいっさいありません**。 |
| [prompt-master-character-sheet](.claude/skills/prompt-master-character-sheet/SKILL.md) | キャラクター設計の三面図（front/side/back）を作るプロンプト専門家。キャラクター画像を受け取ると、元の画風を保ったまま、純白背景の標準的なバストアップ三面図 prompt を生成します。 |
| [prompt-master-general](.claude/skills/prompt-master-general/SKILL.md) | **汎用型** のビジュアルプロンプト主任エンジニア。ABCD の選択式で必ず 3 つの質問をしたうえで、3 つのバリエーション（撮影／アートスタイル／被写体／シーン）を生成します。ユーザーが「通用」と入力した場合に優先的にトリガーされます。 |
| [prompt-master-anime](.claude/skills/prompt-master-anime/SKILL.md) | アニメ風ビジュアルアーキテクト。どんな入力画像でも元のスタイルを取り払い、2D アニメのタッチ（厚塗り、セルシェーディングなど）で描き直して、NanoBanana／SeeDream 級の英語 prompt を出力します。 |
| [prompt-master-otaku-sd](.claude/skills/prompt-master-otaku-sd/SKILL.md) | 究極のオタク AI ＋ Stable Diffusion 神絵師。萌え系・二次元キャラクター（ツンデレ、絶対領域、猫耳、メカ娘など）に特化し、シチュエーション違いの SD 英語 prompt を 3 つ自動生成します。 |
| [prompt-master-otaku-anima](.claude/skills/prompt-master-otaku-anima/SKILL.md) | 究極のオタク AI ＋ Anima モデル専用のプロンプト職人。断片的・曖昧な指示から萌え系キャラクターを設計し、Anima（テキストエンコーダ Qwen3）特有の「Danbooru タグ＋自然言語のハイブリッド」記法で、複数シーン分の高品質な英語 prompt を生成します。衣装を扱う際は costume-design-director を自動で呼び出して連携します。 |
| [prompt-master-hybrid-realism](.claude/skills/prompt-master-hybrid-realism/SKILL.md) | アニメとリアルのハイブリッドレンダリング監督。2D アニメのキャラクターに、PBR ベースの物理的にリアルな質感（衣装・アクセサリー・背景）を融合させ、リアリティの高いバイリンガル prompt を生成します。 |
| [prompt-master-makeup](.claude/skills/prompt-master-makeup/SKILL.md) | 達人級のメイクアップ・ビジュアルプロンプトエンジニア。プロのメイク理論を使って被写体ならではの特徴（そばかす、一重まぶた、左右非対称の骨格）を引き立て、画一的な「完璧」テンプレートは **あえて使いません**。 |
| [prompt-master-gender-swap](.claude/skills/prompt-master-gender-swap/SKILL.md) | 性別転換ポートレートのプロンプトアーキテクト（性別轉換肖像）。2 フェーズ構成です。フェーズ 1 ではまだ prompt を書かず、画像を読み取って変換の向き（男→女／女→男／中性）を宣言したうえで、髪型・服装・年齢（任意で表情・画角・変換の度合い）を ABCD 形式の確認ブロック 1 つで確認します——髪型によって隠れる部位が変わり、描写の重み配分が根本から変わるためです。フェーズ 2 では、性的二形性の優先順位（眉弓 → 顎とアゴ先 → 首と肩のライン → 人中と唇 → 額の傾斜 → 肌と髭）に沿って性別を変換しつつ、同一人物と分かる要素（目の形・二重の折り・両眼の間隔・虹彩の色・鼻筋と鼻先・肌の色・ほくろなどの特徴・顔の角度・画角）を厳格にロックした英語の画像編集 prompt を 1 本出力。バストアップでは顔よりも肩のラインの方が強い性別シグナルになるため、肩幅・僧帽筋の傾き・鎖骨・首と喉仏・三角筋と腕のテーパー・胸郭の輪郭まで作り替え、連鎖する依存関係（年齢 → 髪色としわ、表情 → 頬の持ち上がり、肩幅を狭める → 背景の埋め合わせ、衣装替え → 新たに露出する部位）も解決し、最後に微調整用のスイッチを添えます。テキストのみ出力、画像は生成しません。トリガーワード：「性別轉換」「性轉」「男變女」「女變男」など。 |
| [prompt-master-manga-screentone](.claude/skills/prompt-master-manga-screentone/SKILL.md) | AI ビジュアル錬金術師。入力画像を「高コントラスト・線画なし水彩 ＋ スクリーントーン（Screentone）」の漫画風 prompt に変換し、元の背景や繁体字中国語の看板・文字を **そのまま厳密に保持** します。 |

---

### 4️⃣ 画像プロンプトエンジニアリング — シーン / オブジェクト / 編集

シーン設計、画像編集、九宮格（3x3 グリッド）、商品撮影、トイ撮影、リバースエンジニアリング向けのプロンプトツール。

| Skill 名 | 用途 |
|---|---|
| [prompt-master-scene-architect](.claude/skills/prompt-master-scene-architect/SKILL.md) | アニメシーンアーキテクト。1 枚の 2D シーン画像から 360° の空間全体を割り出し、2×2 の 4 アングルグリッド（正面・左 90°・右 90°・後 180°）の英語 YAML prompt を生成します。 |
| [set-design-director](.claude/skills/set-design-director/SKILL.md) | セット／プロダクションデザイン監督（佈景指導）。物語ドリブンのシーン・セット、あるいは指定の内装スタイル（北欧・和・侘寂・Japandi・インダストリアル・仏・Art Deco…）を、1 つの「デザインバイブル」（時代・様式・階級・60-30-10 配色・素材・光の論理・主役小物）を共有する 3 段（全景定場／中景の生活感／質感クローズアップ）の自然言語英語 prompt に変換し、各段に繁体字訳を付けます。即座に生成・質問なし、テキストのみ出力。 |
| [prompt-master-image-editor](.claude/skills/prompt-master-image-editor/SKILL.md) | 自然言語による画像編集アーキテクト v4.0。曖昧な編集指示（例：「車を赤くする」）を、「編集後の完成画像」を余すところなく描写した高密度な英語 prompt に変換します。デフォルトで元の画風を保ちます。 |
| [prompt-master-texture-repair](.claude/skills/prompt-master-texture-repair/SKILL.md) | 材質逆向・紋理修復プロンプトアーキテクト。劣化画像（背景ノイズ・塗りつぶし／過度な肌の磨き・プラスチック感・圧縮ダメージ）を分析し、物理的にリアルな質感を再生する **繁体字中国語の Img2Img（圖生圖）再描画 prompt** を 1 つ生成します。人物には毛穴と一本一本の髪、製品には金属／プラ／ガラス等の本物の材質を割り当て、背景は完全ノイズゼロを強制、元の光影・透視・構図をロック。人物には「局部重生強制指令」、製品には「產品精修」ブロックを自動付与。テキストのみ出力、画像は生成しません。トリガー：「圖片紋理修復」「肌膚紋理修復」「去髒」「去噪」など。 |
| [prompt-master-9panel-grid](.claude/skills/prompt-master-9panel-grid/SKILL.md) | 九宮格（3×3）絵コンテ監督。「九宮格 / 3x3 storyboard grid」専用で、入力画像から核となるビジュアル特徴を抽出したうえで、9 コマ分の映画級カメラワークのバリエーションを YAML prompt で設計します。 |
| [prompt-reverse-engineer](.claude/skills/prompt-reverse-engineer/SKILL.md) | ビジュアル言語リバースエンジニア。入力画像をピクセル単位で意味的に分解し（4 つの分析軸）、再現可能な英語 prompt と繁体字中国語の解説を生成します。特定のスタイルを **押し付けることはありません**。 |
| [product-visual-architect](.claude/skills/product-visual-architect/SKILL.md) | AI 商品ビジュアルアーキテクト。商品のテキスト説明か画像から、互いに補完し合う 3 組の商用品質の撮影プロンプト（メイン画像／ライフスタイル／マクロなど）を作成します。各組は「ライティング・環境・構図・フォーカスと質感・色彩」の 5 つの要点に基づいて組み立てられ、中英対訳付き。Nano Banana／GPT-image2 などの高パラメータモデルに対応し、質問せず即座に生成します。 |
| [toy-photography-architect](.claude/skills/toy-photography-architect/SKILL.md) | 超リアルなトイ・模型撮影アーキテクト。実物のトイやフィギュアを、ダイナミックなカメラワーク、環境によるストーリーテリング、ガレージキット塗装の技法で、映画級のリアルな映像 prompt へと昇華させます。 |

---

### 5️⃣ 映像・音声プロンプトエンジニアリング

動態生成（モーション生成）、テキスト → 動画（t2v）、画像 → 動画（i2v）、ショート動画、絵コンテ、音楽、歌詞、ボイス設計向けのツール群。

> **🎬 映像生成は 3 つから選択**（この 3 つは特に混同しやすいので、ユーザーのキーワードに応じて振り分けてください）：
>
> | やりたいこと | トリガーキーワード | 対応 Skill | 出力形式 |
> |---|---|---|---|
> | 汎用的な動態生成（**デフォルト**） | 動態 / 動態生成 / 動態提示詞 | `prompt-master-video-continuity` | 単一の YAML ブロック、音声トラック付き、≤ 1300 文字 |
> | テキスト → 動画 | 文生影 / t2v / text-to-video | `prompt-master-text-to-video` | ワンショット ＋ マルチショットの 2 種のバイリンガル映画脚本 |
> | 画像 → 動画 | 圖生影 / i2v / img2video | `prompt-master-image-to-video` | プラン A 繊細 ＋ プラン B ダイナミック、バイリンガル ＋ 構造サマリー |

| Skill 名 | 用途 |
|---|---|
| [prompt-master-video-continuity](.claude/skills/prompt-master-video-continuity/SKILL.md) | AI 映像連続性ディレクター ＋ ボイスデザイナー（**動態生成のデフォルト**）。**単一の YAML ブロック・音声トラック付き** の camera-ready prompt を生成し、ビジュアルの連続性・キャラクターの固定・簡潔な電報式スタイルを徹底します（上限 1300 文字）。漠然と「動態生成」と言われた場合は、すべてこの skill で対応します。 |
| [prompt-master-text-to-video](.claude/skills/prompt-master-text-to-video/SKILL.md) | AI テキスト → 動画プロンプトアーキテクト（**文生影 / t2v**、Sora2・Veo3・Kling・Seedance・海螺に対応）。大まかな構想を自動で補完し、2 種類の映画級スクリプト——【プラン 1：ワンショット】＋【プラン 2：マルチショット 3〜4 カット】——を生成します。どちらも完全な英語原文と繁体字訳、必要に応じてセリフを含み、いっさい質問せず、テキストのみを出力します。明確に「文生影 / t2v」と指定されたときだけトリガーされます。 |
| [prompt-master-image-to-video](.claude/skills/prompt-master-image-to-video/SKILL.md) | 海螺 AI ビジュアルダイナミクスアーキテクト（**圖生影 / i2v**）。1 枚の画像を再現性の高いモーションプロンプトに変換し、「プラン A：繊細・ミクロ ＋ プラン B：壮大・爆発」という対照的な 2 案を生成します。どちらも英語の本文、中国語訳、構造サマリー（被写体・背景の動き、カメラワーク）付き。テキストのみを出力し、画像は生成しません。明確に「圖生影 / i2v」と指定されたときだけトリガーされます。テキストだけの構想は text-to-video、漠然とした「動態生成」は video-continuity を使ってください。 |
| [prompt-master-short-video](.claude/skills/prompt-master-short-video/SKILL.md) | 雰囲気重視のショート動画チーフディレクター（Vlog 風）。1 枚の静止画から 15〜25 秒の TikTok／Reels／Shorts 台本を 3 つ生成し、女性主人公の佇まいと没入感のあるムードを大切にします。 |
| [storyboard-director](.claude/skills/storyboard-director/SKILL.md) | アニメ映画の絵コンテ監督 ＋ AI 撮影エキスパート。キャラクター設定・シーン設計・文章で書かれたストーリーを、一連の映画級な英語 text-to-image prompt（絵コンテ）に変換します。 |
| [ai-music-prompt-generator](.claude/skills/ai-music-prompt-generator/SKILL.md) | Suno／Udio 専用の音楽プロンプト専門家。抽象的な感情やジャンル融合の要望（例：「古風 × サイバーパンク」）を、「凡庸さを排するプロトコル」を盛り込んだ 600〜800 文字のプロ品質 tags に落とし込みます。 |
| [prompt-master-lyrics](.claude/skills/prompt-master-lyrics/SKILL.md) | 達人級の作詞アーキテクト ＋ Suno 構造タグ職人。バークリー音楽大学の Pat Pattison メソッドと中華圏の巨匠（林夕、姚謙、李宗盛、方文山）の手法を融合し、必ず 3 つの質問をしたうえで 3 パターンの歌詞を生成します。 |
| [voice-design-director](.claude/skills/voice-design-director/SKILL.md) | ハリウッド級のボイス＆聴覚体験ディレクター。抽象的なキャラクター設定や感情の要望をもとに、文学的で演じやすい英語のボイスデザインを 3 つ提案します。 |

---

### 6️⃣ スタイリング / キービジュアルデザイン

キャラクターの性格・背景・シーンから筋の通った衣装スタイリングを、脚本とビジュアル素材から映画ポスターのキービジュアルを、それぞれ物語性を持たせて設計します。

| Skill 名 | 用途 |
|---|---|
| [movie-poster-art-director](.claude/skills/movie-poster-art-director/SKILL.md) | 映画ポスターのアートディレクター ＋ キービジュアル設計者（電影海報主視覺總監）。脚本・ログライン・あらすじ、キャラクター画像や設定シート、背景とセットの画像、スチル、ムードの参考——手元の素材をどんな組み合わせでも受け取り、1 つの Key Art Bible（ジャンル・HEX 付きの 60-30-10 配色・光の論理・主役モチーフ・固定するキャラクターの同一性・グレーディング）を共有しつつ、ポスターの型と構図の型をそれぞれ変えた 3 案——（1）概念先行のティザー、（2）本ビジュアル（Theatrical One-Sheet）、（3）キャラクター／雰囲気の派生ポスター——を設計します。各案には **文字をいっさい入れない** キービジュアル用の自然言語英語 prompt（Nano Banana／GPT-image2／Seedream／Midjourney など高パラメータモデル向け、余白をあらかじめ確保）＋繁体字訳＋タイポグラフィと組版の計画（題字の扱い・タグライン・余白ゾーン・スタッフクレジット）が付きます。題字やクレジットは画像の上に組むもので、モデルに描かせるものではないからです。即座に生成・質問なし、テキストのみ出力。トリガーワード：「電影海報」「海報設計」「主視覺」「key art」など。 |
| [costume-design-director](.claude/skills/costume-design-director/SKILL.md) | キャラクター衣装ビジュアルディレクター。「衣装こそ物語（Wardrobe is Narrative）」を理念に、キャラクターの性格・背景・感情・場面・気候を踏まえた、筋の通ったバイリンガル（EN/ZH）の衣装デザインを生成します。アクセサリーは 3 点まで。 |

---

### 7️⃣ ソーシャルメディア運用 — コピー / ビジュアル

マーケティング要件をソーシャル投稿のコピーに、コラム記事の内容をビジュアルレイアウト案に、それぞれ落とし込みます。

| Skill 名 | 用途 |
|---|---|
| [fb-post-architect](.claude/skills/fb-post-architect/SKILL.md) | ソーシャル爆文アーキテクト（社群爆文架構師）。マーケティング要件を、FB の実際のランキングシグナル（シェアの重み・フォロー転換・滞在時間・ネガティブシグナル回避）に合わせて設計した、そのまま投稿できる繁体字中国語の FB 投稿へ変換します。**本命投稿 1 本**（モバイル改行済み・1 コメント目のリンク付き）＋ **別公式のフック代替案 3 つ** ＋ シグナル設計の解説を出力。戦略軸（分享型＝拡散 / 追蹤型＝フォロワー獲得 / 轉單型＝コンバージョン）を 1 つだけ選んで宣言します。爆文に不可欠な具体的素材（実数値・実体験・反直感の発見）が欠けている場合に限り質問し、**数字や事例を捏造することはいっさいありません**。テキストのみ出力。トリガーワード：「FB貼文」「FB文案」「臉書貼文」「爆文」など。 |
| [social-media-visual-designer](.claude/skills/social-media-visual-designer/SKILL.md) | シニア・ソーシャルメディアビジュアル情報デザイナー。記事やテーマを SNS 画像カード（図卡）の設計企画に変換：7 ジャンル別カラーパレット（HEX 指定）、雑誌風ミニマルレイアウト、実写写真のアートディレクション、コピーに加え、背景写真用の英語 AI 画像生成プロンプトまで出力します。「社群圖卡」「圖卡提示詞」で発動。 |

---

### 8️⃣ AI 生成実行ツール（API を直接呼び出し）

プロンプトを書くタイプの skill とは違い、この 3 つは **実際に GMI Cloud API を呼び出して画像／動画を生成する** 実行ツールです（Python スクリプト内蔵：送信 → ポーリング → ダウンロード）。しかも **ユーザーがモデル名をはっきり指定したときだけ** トリガーされ、「画像生成」「動画生成」といった一般的な言い回しは、すべてプロンプト系 skill が処理します。3 つとも `.claude/lib/media_paths.py` を共有しているので、参考素材はプロジェクト直下の `uploads/`（使用済みは `uploads/done/` へ自動で移動）、生成物は `outputs/` にまとまります。どちらも `.gitignore` 対象です。

| Skill 名 | 用途 |
|---|---|
| [gemini-3-pro-image](.claude/skills/gemini-3-pro-image/SKILL.md) | GMI Cloud の `gemini-3-pro-image-preview` API を呼び出して実際に画像を生成・編集する実行ツール（**プロンプトを書くだけの skill ではありません**）。モデル名（gemini 3 pro image、nano banana pro、奈米香蕉 pro）を明示したときだけトリガーされます。単に「nano banana／奈米香蕉」（pro なし）と言った場合は別モデル扱いで、トリガーされません。 |
| [gpt-image-2](.claude/skills/gpt-image-2/SKILL.md) | OpenAI の gpt-image-2 を GMI Cloud の非同期リクエストキュー API 経由で呼び出し、実際に画像を生成・編集する実行ツール（**プロンプトを書くだけの skill ではありません**）。1 本のデュアルモードスクリプトで動作し、入力画像がなければ `gpt-image-2-generate`（テキスト → 画像）、入力画像があれば `gpt-image-2-edit`（画像 1 枚につき 1 リクエスト）を実行します。モデル名・プロバイダ名（gpt-image-2、gpt image 2、GMI、GMI Cloud）を明示したときだけトリガーされます。 |
| [seedance-2-0](.claude/skills/seedance-2-0/SKILL.md) | GMI Cloud の `seedance-2-0-260128` API を呼び出して実際に動画を生成する実行ツール（**プロンプトを書くだけの skill ではありません**）。モデル名（seedance 2、seedance 2.0）を明示したときだけトリガーされます。単に「seedance」（2 なし）や「seedance 2 fast」と言った場合は別モデル扱いで、トリガーされません。 |

---

### 9️⃣ 開発ツール

Git / GitHub の自動化など、開発を補助するツール。

| Skill 名 | 用途 |
|---|---|
| [git-github-pusher](.claude/skills/git-github-pusher/SKILL.md) | Git の初期化、リモートとの競合処理、GitHub へのプッシュという一連の流れを自動化します。ユーザーが「push」「上傳 github」と言った場合にトリガーされます。 |

---

## 🚀 使い方

1. **自動トリガー**：各 skill は `description` にトリガーワードが設定されており、ユーザーの発言がそのキーワードに該当すると、Claude Code が対応する skill を自動で読み込みます。たとえば「この画像の **圖生影** プロンプトを作って」と入力すれば `prompt-master-image-to-video` が、「**文生影** の台本」なら `prompt-master-text-to-video` が読み込まれます。
2. **手動指定**：メッセージに skill 名を直接書いて指定することもできます。例：「`prompt-master-portrait` で人物 prompt を作って」。
3. **連携チェーン**：一部の skill は別の skill を自動で呼び出して連携します（例：`prompt-master-otaku-sd` / `prompt-master-otaku-anima` は衣装を扱う際に `costume-design-director` を自動で呼び出し、`skill-creator` は完了後に必ず `skill-optimizer` と `skill-translator` を起動します）。

---

## 📁 ディレクトリ構成

```
biz-ai-video-course/
├── .claude/
│   ├── settings.local.json
│   ├── lib/
│   │   └── media_paths.py               ← GMI 実行系 3 skill が共有する素材パス定義
│   └── skills/                          ← 42 個の skill のメインディレクトリ
│       ├── ai-music-prompt-generator/
│       │   ├── SKILL.md                 ← skill の本体ファイル
│       │   ├── references/              ← Progressive Disclosure の詳細リファレンス
│       │   └── docs/                    ← 繁体字の人間向け版（実行時は読み込まれません）
│       ├── prompt-master-portrait/
│       └── ... (全 42 個)
├── prompts/                             ← 使い回したい prompt のテキスト置き場
├── uploads/                             ← GMI 実行系 skill の参考素材（.gitignore 対象）
├── outputs/                             ← 生成された画像・動画の出力先（.gitignore 対象）
└── README.md                            ← 本ファイル
```

各 skill には以下が含まれます：
- **`SKILL.md`**：簡潔なコア指示（200 行未満）。役割、Prime Directives（最優先事項）、実行フローを定義します。
- **`references/`**：Progressive Disclosure パターンで切り出した詳細なナレッジベース（スタイル辞典、分析フレームワークなど）。必要なときにだけ skill が自分で読み込みます。
- **`docs/`**（一部の skill）：`skill-translator` が生成した、人間が読みやすい繁体字中国語版。実行時に AI が読み込むことは **いっさいありません**。

---

## 🎯 設計思想

1. **Progressive Disclosure（漸進的開示）**：SKILL.md は簡潔に保ち、詳細な知識は `references/` に分離して、context window の汚染を防ぎます。
2. **No Hallucination（幻覚の排除）**：多くの prompt 系 skill は細部の捏造を固く禁じ、必ず先に確認するか、元の入力の特徴を保持します。
3. **Bilingual Output（バイリンガル出力）**：画像・動画 prompt の多くは「英語 prompt ＋ 繁体字の解説」をセットにし、モデルへの入力と人間の理解を両立させます。
4. **Mandatory Protocols（必須プロトコル）**：質の高い skill の多くは、必須の質問や構造化された ABCD 形式の選択肢を取り入れ、質の低いデフォルト出力を防ぎます。

---
---

# 繁體中文

這個專案集結了 **42 個專業 Skill**，涵蓋 **商業內容創作**、**AI 影音生成（動態生成 / 文生影 / 圖生影）**、**圖像提示詞工程**、**劇本與角色創作**，以及**直接呼叫 GMI Cloud API 出圖／出片的執行工具**。所有技能皆位於 `.claude/skills/` 目錄下，由 Claude Code 在偵測到對應觸發詞時自動載入並執行，無需手動設定。

---

## 📂 技能分類總覽

### 1️⃣ Skill 管理與架構工具

用於建立、優化與翻譯 skill 本身的元工具（meta-tools）。

| Skill 名稱 | 用途 |
|---|---|
| [skill-creator](.claude/skills/skill-creator/SKILL.md) | 建立新 skill 或修改既有 skill 的標準作業流程指南，會自動串接 skill-optimizer 與 skill-translator 完成收尾。 |
| [skill-optimizer](.claude/skills/skill-optimizer/SKILL.md) | 重構與壓縮既有 SKILL.md，套用「漸進式揭露 (Progressive Disclosure)」原則，將 SKILL.md 控制在 100–200 行以內，避免污染 context window。 |
| [skill-translator](.claude/skills/skill-translator/SKILL.md) | 將 SKILL.md 翻譯成繁體中文人類可讀版本，存放於 `docs/` 資料夾，**完全不影響** AI 執行 context。 |

---

### 2️⃣ 角色與劇本創作

從碎片線索逆向建構角色、為角色取一個有典故的名字、把點子寫成劇本初稿，並深度分析既有劇本、轉譯成鏡頭。

| Skill 名稱 | 用途 |
|---|---|
| [character-architect](.claude/skills/character-architect/SKILL.md) | 好萊塢編劇 + 角色架構師（奧斯卡級，兼具社會學/心理學洞察）。從一句台詞、一件配飾或單張照片的構圖光影等碎片線索逆向建構角色，產出**三份**差異最大化、內部自洽的繁中角色檔案（外型/社會屬性、家庭背景與創傷、MBTI/星座/血型一致性、語言習慣與微表情 + 電影級摘要）。觸發詞：「角色設定」「人設」「人物塑造」等。 |
| [cultural-naming-director](.claude/skills/cultural-naming-director/SKILL.md) | 文化共鳴命名大師。讀取角色檔案（或任何敘事實體——陣營、地名、武器、作品標題），定位其心理光譜（混沌↔秩序・自私↔利他・主動↔被動）與致命缺陷、可能結局，從十二文化的「全球神話矩陣」（中國、日本、印度、希臘羅馬、北歐、凱爾特、斯拉夫、亞伯拉罕神祕主義、埃及、美索不達米亞、美洲原住民、波斯）取出候選原型，經對抗性測試避開最顯而易見的選擇，再以命名煉金術（字根重組／概念翻譯）鍛出名字，並附完整的文化共鳴拆解：原型出處、神話背景、對應邏輯（表層連結／與致命缺陷和結局的深層共鳴／文化張力）。只輸出命名與分析文字。觸發詞：「命名」「改名」「角色取名」「有寓意的名字」等。※ 本技能設計的是**名字**，角色的性格與背景請用 character-architect。 |
| [screenwriter-architect](.claude/skills/screenwriter-architect/SKILL.md) | 頂尖編劇 ＋ 敘事架構師（編劇架構師／劇本第一稿）。把一句話或半成形的點子寫成可拍的繁中 **劇本初稿**。階段一【立項問診】只問一次 ABCD 題組，涵蓋設定問題（主角與渴望、時代場景、類型調性、語言）、劇情問題（引爆事件、對抗力量、結局立場、主題論證）與長度問題（片長、平台用途、製作限制），每題都附 ✔推薦 預設值，回一句「全部照推薦」即可開工。階段二【內部多稿淬鍊】在使用者看到任何一行字之前，先自行跑完 結構審查 → 聲口審查 → 台詞淬鍊 → 終檢核表 至少三輪重寫，所以你拿到的「初稿」其實已是第三、四稿。專長是有詩意有寓意卻不咬文嚼字的台詞（用具體物件取代形容詞、答非所問、重複與變奏、語域衝突），以及場景層級的 目標-阻礙-結果 ＋ 因此／但是 因果結構、外化／客觀對應物、鋪陳與回收、預算意識。只輸出劇本文字。觸發詞：「寫劇本」「劇本創作」「短片劇本」「編劇」等。 |
| [script-doctor-architect](.claude/skills/script-doctor-architect/SKILL.md) | 好萊塢頂級劇本醫生。接收劇本後產出高度結構化的「劇本分析報告」，拆解敘事結構、角色心理、事件時間軸與市場定位。 |
| [shot-script-director](.claude/skills/shot-script-director/SKILL.md) | 電影導演 ＋ 畫面轉譯架構師（分鏡導演）。接收一小段劇本／台詞／散文，轉譯成由 4–6 個（典型 4–5 個）cut 組成的結構化「分鏡腳本」，每個 cut 標明 景別・角度／主體／場景／運鏡／氛圍情緒／台詞演技。以「意義活在縫隙裡」的改編心法（外化・客觀對應物、潛台詞、資訊經濟＝懸念、時間重構、**台詞轉譯：先問要不要用說的、口語化、聲口分化、靜默**）為根基，露出最少讓觀眾自行推論。只輸出腳本文字，不生成圖片／影片。觸發詞：「分鏡腳本」「拍攝劇本轉譯」「劇本轉分鏡」等。※ 與 storyboard-director（輸出 AI 繪圖 prompt）不同。 |

---

### 3️⃣ 圖像提示詞工程 — 人物 / 肖像

針對 AI 圖像生成模型（Midjourney、Seedream、Nano Banana、SD）打造的人物類提示詞工程師。

| Skill 名稱 | 用途 |
|---|---|
| [prompt-master-portrait](.claude/skills/prompt-master-portrait/SKILL.md) | 寫真級肖像/角色設計提示詞工程師。強制執行 8–12 點深度釐清流程，產出 3 個雙語（EN/ZH）的精準提示詞，**禁止憑空捏造**任何細節。 |
| [prompt-master-character-sheet](.claude/skills/prompt-master-character-sheet/SKILL.md) | 角色設計三視圖（front/side/back）提示詞專家。接收角色圖後保留原畫風，生成純白背景的標準半身三視圖 prompt。 |
| [prompt-master-general](.claude/skills/prompt-master-general/SKILL.md) | **通用型**視覺提示詞首席工程師。以 ABCD 多選結構強制提問 3 題後，產出 3 個變體（攝影 / 藝術風格 / 主體 / 場景）。當使用者提到「通用」優先觸發。 |
| [prompt-master-anime](.claude/skills/prompt-master-anime/SKILL.md) | 動漫風格視覺架構師。將任何輸入圖剝除原始風格、用 2D 動漫鏡頭重新渲染（厚塗、賽璐璐等），輸出 NanoBanana/SeeDream 級的英文 prompt。 |
| [prompt-master-otaku-sd](.claude/skills/prompt-master-otaku-sd/SKILL.md) | 究極阿宅 AI + Stable Diffusion 神繪師。專攻萌系/二次元角色（傲嬌、絕對領域、貓耳、機娘等），自動產出 3 個不同情境的 SD 英文 prompt。 |
| [prompt-master-otaku-anima](.claude/skills/prompt-master-otaku-anima/SKILL.md) | 究極阿宅 AI + Anima 模型專用提示詞職人。從碎片化/曖昧指示設計萌系角色，以 Anima（文字編碼器 Qwen3）特有的「Danbooru 標籤＋自然語言混合」記法產出多場景高品質英文 prompt；處理服裝時自動串接 costume-design-director。 |
| [prompt-master-hybrid-realism](.claude/skills/prompt-master-hybrid-realism/SKILL.md) | 動漫與寫實混合渲染導演。把 2D 動漫角色與 PBR 物理寫實材質（服裝、配件、背景）融合，產出高擬真的雙語 prompt。 |
| [prompt-master-makeup](.claude/skills/prompt-master-makeup/SKILL.md) | 大師級彩妝視覺提示詞工程師。將專業彩妝理論套用於放大主體獨特特徵（雀斑、單眼皮、不對稱骨相），**拒絕**標準化「完美」模板。 |
| [prompt-master-gender-swap](.claude/skills/prompt-master-gender-swap/SKILL.md) | 性別轉換肖像提示詞架構師。兩階段運作：階段一收到肖像後**先不寫 prompt**，而是判讀並宣告轉換方向（男→女／女→男／中性），再用單一 ABCD 題組確認髮型、服裝與年齡（可選表情、取景與轉換程度）——因為髮型決定哪些五官被遮蔽，也就決定描述權重該怎麼分配。階段二依性別二態性優先權（眉弓 → 下顎與下巴 → 頸肩線 → 人中與唇 → 額頭斜度 → 膚質與鬍鬚）產出一段可直接執行的英文**圖像編輯** prompt，同時硬鎖必須存活的身分錨點（眼型、雙眼皮摺、瞳距、虹膜顏色、鼻樑與鼻頭、膚色、辨識性特徵、頭部角度、取景）。因為半身照裡肩線比臉更強烈地傳遞性別訊號，它連肩寬、斜方肌坡度、鎖骨跨距、頸部與喉結、三角肌與手臂收窄、胸廓輪廓一併改寫；並處理連鎖依賴（年齡→髮色與皺紋、表情→顴肌上提、肩變窄→背景補位、換衣→新露出的解剖結構），最後附微調開關。只輸出提示詞文字，不生成／編輯圖片。觸發詞：「性別轉換」「性轉」「男變女」「女變男」等。 |
| [prompt-master-manga-screentone](.claude/skills/prompt-master-manga-screentone/SKILL.md) | AI 視覺煉金術士。將輸入圖轉為「高對比無線條水彩 + 網點 (Screentone)」漫畫風 prompt，**嚴格保留**原始背景與繁體中文招牌/文字。 |

---

### 4️⃣ 圖像提示詞工程 — 場景 / 物件 / 編輯

針對場景設計、圖像編輯、九宮格、產品攝影、玩具攝影、逆向工程的提示詞工具。

| Skill 名稱 | 用途 |
|---|---|
| [prompt-master-scene-architect](.claude/skills/prompt-master-scene-architect/SKILL.md) | 動畫場景架構師。從單張 2D 場景圖推演完整 360° 環境，產出 2x2 四視角網格（正面、左 90°、右 90°、後 180°）的英文 YAML prompt。 |
| [set-design-director](.claude/skills/set-design-director/SKILL.md) | 佈景／美術指導（Production Designer）。將敘事驅動的場景／佈景，或指名的室內風格（北歐／日式／侘寂／Japandi／工業／法式／Art Deco…）轉譯為共用同一份「設計聖經」（時代・風格・階級・60-30-10 色盤・材質・光源邏輯・主角道具）的三段（全景定場／中景生活痕跡／特寫質感情緒）自然語言英文 prompt，每段附繁中翻譯。立即生成、不提問，只輸出提示詞文字。 |
| [prompt-master-image-editor](.claude/skills/prompt-master-image-editor/SKILL.md) | 自然語言圖像編輯架構師 v4.0。將模糊的編輯指令（如「把車變紅色」）翻譯為完整描述「最終編輯後圖像」的高密度英文 prompt，預設保留原始畫風。 |
| [prompt-master-texture-repair](.claude/skills/prompt-master-texture-repair/SKILL.md) | 材質逆向工程・紋理修復提示詞架構師。分析劣化圖片（背景噪點／主體塗抹或過度磨皮／塑料感／壓縮損傷），產出一組重生真實物理質感的 **繁體中文 Img2Img（圖生圖）重繪 prompt**。人物給毛孔與一根根髮絲、產品給金屬／塑料／玻璃等真實材質、背景強制完全零噪點，並鎖定原圖光影・透視・構圖。人物自動附「局部重生強制指令」、產品附「產品精修」區塊。只輸出提示詞文字，不生成圖片。觸發詞：「圖片紋理修復」「肌膚紋理修復」「去髒」「去噪」等。 |
| [prompt-master-9panel-grid](.claude/skills/prompt-master-9panel-grid/SKILL.md) | 九宮格分鏡導演。針對「九宮格 / 3x3 storyboard grid」專屬，提取輸入圖的核心視覺特徵後設計 9 格電影級鏡頭變化 YAML prompt。 |
| [prompt-reverse-engineer](.claude/skills/prompt-reverse-engineer/SKILL.md) | 視覺語言逆向工程師。對輸入圖進行像素級語意拆解（4 個分析維度），產出可重現的英文 prompt + 繁體中文分析。**不**強加任何預設風格。 |
| [product-visual-architect](.claude/skills/product-visual-architect/SKILL.md) | AI 產品視覺架構師。將產品文字描述或圖片轉為 3 組互補的商業級攝影提示詞（主圖／情境／微距等），每組依「光線・環境・構圖・焦點質感・色彩」五大要領建構，附中英對照，適用 Nano Banana / GPT-image2 等高參數模型。立即生成、不提問。 |
| [toy-photography-architect](.claude/skills/toy-photography-architect/SKILL.md) | 超寫實玩具/模型攝影建築師。將實體玩具/figure 透過動態運鏡、環境敘事、garage-kit 上色技法，提升為電影級寫實影像 prompt。 |

---

### 5️⃣ 影音與聲音提示詞工程

針對動態生成、文生影 (t2v)、圖生影 (i2v)、短影音、分鏡、音樂、歌詞、人聲設計的工具集。

> **🎬 影音生成三選一**（這三個最容易混淆，請依使用者的關鍵字路由）：
>
> | 你想要 | 觸發關鍵字 | 對應 Skill | 產出形式 |
> |---|---|---|---|
> | 泛用動態生成（**預設**） | 動態 / 動態生成 / 動態提示詞 | `prompt-master-video-continuity` | 單一 YAML 區塊、含音軌、≤ 1300 字元 |
> | 文字 → 影片 | 文生影 / t2v / text-to-video | `prompt-master-text-to-video` | 單鏡頭 ＋ 多鏡頭兩套雙語電影腳本 |
> | 圖片 → 影片 | 圖生影 / i2v / img2video | `prompt-master-image-to-video` | 方案 A 微觀 ＋ 方案 B 爆發，雙語 ＋ 結構摘要 |

| Skill 名稱 | 用途 |
|---|---|
| [prompt-master-video-continuity](.claude/skills/prompt-master-video-continuity/SKILL.md) | AI 影片連續性導演 + 人聲設計師（**動態生成預設**）。產出**單一 YAML 區塊、含音軌**的 camera-ready prompt，強制視覺連續、角色鎖定、電報式風格，硬上限 1300 字元。泛指「動態生成」一律走此 skill。 |
| [prompt-master-text-to-video](.claude/skills/prompt-master-text-to-video/SKILL.md) | AI 文生影提示詞架構師（**文生影 / t2v**，對應 Sora2、Veo3、Kling、Seedance、海螺）。將粗略構想自主補完為兩套電影級腳本——【方案一：單一鏡頭】＋【方案二：多鏡頭序列 3–4 cut】，各含完整英文原文 + 繁中翻譯與可選對白；全程不提問、僅寫文字。**僅**在明確「文生影 / t2v」時觸發。 |
| [prompt-master-image-to-video](.claude/skills/prompt-master-image-to-video/SKILL.md) | 海螺 AI 視覺動態架構師（**圖生影 / i2v**）。將單張圖片轉譯為高可執行性的動態提示詞，產出「方案 A 微觀細膩 ＋ 方案 B 宏觀爆發」兩組對比提案，各含英文段落、中文翻譯與結構摘要（主體/背景動態、運鏡）。僅寫文字、不生成影像。**僅**在明確「圖生影 / i2v」時觸發；純文字構想請用 text-to-video、泛指「動態生成」請用 video-continuity。 |
| [prompt-master-short-video](.claude/skills/prompt-master-short-video/SKILL.md) | 氛圍系短影音首席導演（Vlog 風）。從單張靜態圖產出 3 個 15–25 秒 TikTok/Reels/Shorts 腳本，著重女主角的氣質與沉浸式氛圍。 |
| [storyboard-director](.claude/skills/storyboard-director/SKILL.md) | 動畫電影分鏡導演 + AI 攝影專家。將角色設定、場景設計與文字劇情翻譯成一系列電影級的英文 text-to-image prompt 分鏡。 |
| [ai-music-prompt-generator](.claude/skills/ai-music-prompt-generator/SKILL.md) | Suno / Udio 專用音樂提示詞專家。將抽象情緒/曲風融合需求（如「古風 × 賽博龐克」）轉譯成 600–800 字元、含「反平庸協議」的生產級 tags。 |
| [prompt-master-lyrics](.claude/skills/prompt-master-lyrics/SKILL.md) | 大師級作詞架構師 + Suno 結構詞匠。融合 Berklee Pat Pattison 系統與華語大師（林夕、姚謙、李宗盛、方文山）流程，強制 3 題提問後產出 3 個變體歌詞。 |
| [voice-design-director](.claude/skills/voice-design-director/SKILL.md) | 好萊塢級人聲與聽覺體驗總監。針對抽象角色設定或情緒需求，產出 3 個富文學感、可演繹的英文聲線設計。 |

---

### 6️⃣ 造型 / 主視覺設計

依角色個性、背景與場景產出邏輯一致的服裝造型；依劇本與視覺素材產出敘事驅動的電影海報主視覺。

| Skill 名稱 | 用途 |
|---|---|
| [movie-poster-art-director](.claude/skills/movie-poster-art-director/SKILL.md) | 電影海報主視覺總監 ＋ Key Art 架構師。接收任意組合的素材——劇本／一句話簡介／劇情大綱、角色圖或角色設定表、背景與佈景圖、劇照、氛圍參考——設計三款專業海報提案，共用同一份 Key Art Bible（類型、含色碼的 60-30-10 色盤、光線邏輯、主視覺母題、鎖定的角色身分錨點、調色），但採用三種不同的海報原型與三種不同的構圖原型：(1) 概念先導 Teaser、(2) 主視覺 Theatrical One-Sheet、(3) 角色／氛圍延伸海報。每款提案都給一段自然語言英文生圖 prompt（適用 Nano Banana / GPT-image2 / Seedream / Midjourney 等高參數模型），畫面**完全不含文字**並刻意預留負空間，另附繁中翻譯與獨立的字體排版計畫（片名處理、tagline、留白區、演職員字塊）——因為片名與字卡是要疊印在圖上的，不該交給模型畫。立即生成、不提問，只輸出提示詞與設計計畫文字。觸發詞：「電影海報」「海報設計」「主視覺」「key art」等。 |
| [costume-design-director](.claude/skills/costume-design-director/SKILL.md) | 角色服裝視覺總監。理念為「衣著即敘事 (Wardrobe is Narrative)」，依角色個性、背景、情緒、場合、氣候產出邏輯一致的雙語（EN/ZH）服裝設計，配件 ≤ 3 件。 |

---

### 7️⃣ 社群經營 — 文案 / 視覺

將行銷需求轉化為社群貼文文案，將專欄文章內容轉化為對應的社群視覺排版方案。

| Skill 名稱 | 用途 |
|---|---|
| [fb-post-architect](.claude/skills/fb-post-architect/SKILL.md) | 社群爆文架構師。將行銷需求轉譯為可直接發佈的繁中 FB 貼文，針對平台真實的排序訊號（分享權重・追蹤轉換・停留時間・負面訊號迴避）而設計。產出**主推貼文 1 篇**（手機排版、含第一則留言）＋**不同公式的鉤子替代方案 3 個**＋訊號設計說明，並選定且宣告單一戰略軸（分享型＝擴散／追蹤型＝漲粉／轉單型＝轉換）。僅在缺乏爆文所需的具體素材（真實數字、親身經歷、反直覺發現）時才提問，**絕不捏造數字或案例**。只輸出文字。觸發詞：「FB貼文」「FB文案」「臉書貼文」「爆文」等。 |
| [social-media-visual-designer](.claude/skills/social-media-visual-designer/SKILL.md) | 資深社群視覺資訊設計師。將文章或主題轉為社群圖卡設計企劃：七大類型配色（附色碼）、雜誌感極簡版式、真實照片攝影指導、圖卡文案，並附上背景照片的英文 AI 生圖提示詞。以「社群圖卡」「圖卡提示詞」觸發。 |

---

### 8️⃣ AI 生成執行工具（直接呼叫 API）

與提示詞撰寫類 skill 不同，這三個是**真正呼叫 GMI Cloud API 出圖／出片**的可執行工具（內建 Python 腳本：提交 → 輪詢 → 下載），且**僅在使用者明確說出模型名稱時**才觸發，泛用的「圖片生成」「影片生成」字眼一律交由提示詞類 skill 處理。三者共用 `.claude/lib/media_paths.py`，因此參考素材一律放專案根目錄的 `uploads/`（用過的會自動搬進 `uploads/done/`），產出一律落在 `outputs/`，兩者都已列入 `.gitignore`。

| Skill 名稱 | 用途 |
|---|---|
| [gemini-3-pro-image](.claude/skills/gemini-3-pro-image/SKILL.md) | 實際呼叫 GMI Cloud `gemini-3-pro-image-preview` API 生成／編輯真實圖片的執行工具，**非**提示詞撰寫器。僅在明確說出模型名稱（gemini 3 pro image、nano banana pro、奈米香蕉 pro）時觸發；單講「nano banana／奈米香蕉」（無 pro）屬不同模型，不觸發。 |
| [gpt-image-2](.claude/skills/gpt-image-2/SKILL.md) | 透過 GMI Cloud 非同步請求佇列 API 呼叫 OpenAI 的 gpt-image-2、實際生成／編輯真實圖片的執行工具，**非**提示詞撰寫器。單一雙模式腳本：無輸入圖時跑 `gpt-image-2-generate`（文生圖），有輸入圖時跑 `gpt-image-2-edit`（每張圖一個請求）。僅在明確說出模型／供應商名稱（gpt-image-2、gpt image 2、GMI、GMI Cloud）時觸發。 |
| [seedance-2-0](.claude/skills/seedance-2-0/SKILL.md) | 實際呼叫 GMI Cloud `seedance-2-0-260128` API 生成真實影片的執行工具，**非**提示詞撰寫器。僅在明確說出模型名稱（seedance 2、seedance 2.0）時觸發；單講「seedance」（無 2）或「seedance 2 fast」屬不同模型，不觸發。 |

---

### 9️⃣ 開發工具

Git / GitHub 自動化等開發輔助工具。

| Skill 名稱 | 用途 |
|---|---|
| [git-github-pusher](.claude/skills/git-github-pusher/SKILL.md) | 自動化 Git 初始化 + 處理遠端衝突 + 推送至 GitHub 的全套流程，當使用者說「push」、「上傳 github」時觸發。 |

---

## 🚀 使用方式

1. **自動觸發**：所有 skill 皆已設定 `description` 中的觸發詞，當使用者對話內容命中關鍵字時，Claude Code 會自動載入對應 skill。例如輸入「幫我做這張圖的**圖生影**提示詞」會載入 `prompt-master-image-to-video`，而「**文生影**腳本」則載入 `prompt-master-text-to-video`。
2. **手動指定**：可在訊息中直接寫出 skill 名稱，例如「用 `prompt-master-portrait` 幫我設計一張人像 prompt」。
3. **協作鏈**：部分 skill 會自動串接其他 skill（例如 `prompt-master-otaku-sd` / `prompt-master-otaku-anima` 處理服裝時會自動呼叫 `costume-design-director`、`skill-creator` 完成後一律觸發 `skill-optimizer` 與 `skill-translator`）。

---

## 📁 目錄結構

```
biz-ai-video-course/
├── .claude/
│   ├── settings.local.json
│   ├── lib/
│   │   └── media_paths.py               ← 三個 GMI 執行工具共用的素材路徑定義
│   └── skills/                          ← 42 個 skill 主目錄
│       ├── ai-music-prompt-generator/
│       │   ├── SKILL.md                 ← skill 主檔
│       │   ├── references/              ← 漸進式揭露的詳細參考
│       │   └── docs/                    ← 繁中人類可讀版（執行時不會被載入）
│       ├── prompt-master-portrait/
│       └── ... (共 42 個)
├── prompts/                             ← 想留著重複使用的 prompt 文字檔
├── uploads/                             ← GMI 執行工具的參考素材（已列入 .gitignore）
├── outputs/                             ← 生成的圖片／影片產出區（已列入 .gitignore）
└── README.md                            ← 本檔案
```

每個 skill 內含：
- **`SKILL.md`**：精簡的核心指令（< 200 行），定義角色、Prime Directives 與執行流程。
- **`references/`**：用 Progressive Disclosure 模式分離出的詳細知識庫（風格詞典、分析框架等），僅在需要時由 skill 主動載入。
- **`docs/`**（部分 skill）：由 `skill-translator` 產出的繁體中文人類可讀版本，**完全不會**被 AI 在執行時讀取。

---

## 🎯 設計哲學

1. **Progressive Disclosure（漸進式揭露）**：SKILL.md 保持精簡，詳細知識下放到 `references/`，避免 context window 污染。
2. **No Hallucination（拒絕幻覺）**：多數 prompt 類 skill 嚴格禁止憑空捏造細節，必須先釐清或保留原始輸入特徵。
3. **Bilingual Output（雙語輸出）**：圖像/影片 prompt 多採「英文 prompt + 繁中說明」配套，方便餵給模型同時讓人類理解。
4. **Mandatory Protocols（強制協議）**：高品質 skill 普遍採用強制提問或結構化 ABCD 選項，避免低品質默認輸出。
