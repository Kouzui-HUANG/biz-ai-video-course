# biz-ai-video-course — Claude Code Skills スキル集／技能集合

> 🌐 **Bilingual README ｜ バイリンガル説明文件**
> 先に **日本語** を完全収録し、続いて **繁體中文** を記載しています。／日文版完整在前，繁體中文版在後。
> ⬇️ [日本語](#日本語) ｜ [繁體中文](#繁體中文)

---

# 日本語

このプロジェクトには **34 個の専門 Skill** が集約されており、**ビジネスコンテンツ制作**、**AI 映像生成（動態生成＝モーション生成 / テキスト → 動画 / 画像 → 動画）**、**画像プロンプトエンジニアリング**、**脚本・キャラクター創作**、さらに **GMI Cloud API を直接呼び出して画像・動画を出力する実行ツール** までをカバーします。すべての Skill は `.claude/skills/` ディレクトリ配下にあり、Claude Code が対応するトリガーワードを検出すると自動的に読み込んで実行するため、手動設定は不要です。

---

## 📂 スキル分類一覧

### 1️⃣ Skill 管理・構築ツール

skill 自体を作成・最適化・翻訳するためのメタツール（meta-tools）。

| Skill 名 | 用途 |
|---|---|
| [skill-creator](.claude/skills/skill-creator/SKILL.md) | 新しい skill の作成、または既存 skill を修正するための標準作業手順（SOP）ガイド。仕上げに skill-optimizer と skill-translator を自動的に連携・実行します。 |
| [skill-optimizer](.claude/skills/skill-optimizer/SKILL.md) | 既存の SKILL.md をリファクタリング・圧縮し、「漸進的開示（Progressive Disclosure）」原則を適用して SKILL.md を 100〜200 行以内に抑え、context window の汚染を防ぎます。 |
| [skill-translator](.claude/skills/skill-translator/SKILL.md) | SKILL.md を繁体字中国語の人間可読版に翻訳し、`docs/` フォルダに保存します。AI の実行 context には **一切影響しません**。 |

---

### 2️⃣ キャラクター・脚本創作

断片的な手がかりからキャラクターを逆構築し、脚本を深く分析します。

| Skill 名 | 用途 |
|---|---|
| [character-architect](.claude/skills/character-architect/SKILL.md) | ハリウッド脚本家 + キャラクターアーキテクト（アカデミー賞級、社会学／心理学的洞察を兼備）。一行のセリフ、一つの小物、あるいは一枚の写真の構図・光影といった断片的な手がかりからキャラクターを逆構築し、差別化を最大化した内部整合性のある繁体字キャラクター設定書を **3 つ** 生成します（外見／社会的属性、家庭背景とトラウマ、MBTI／星座／血液型の一貫性、言語習慣とマイクロ表情 + 映画級サマリー）。トリガーワード：「角色設定」「人設」「人物塑造」など。 |
| [script-doctor-architect](.claude/skills/script-doctor-architect/SKILL.md) | ハリウッド最高峰のスクリプトドクター。脚本を受け取ると、高度に構造化された「脚本分析レポート」を生成し、物語構造・キャラクター心理・出来事のタイムライン・市場ポジショニングを分解します。 |

---

### 3️⃣ 画像プロンプトエンジニアリング — 人物 / ポートレート

AI 画像生成モデル（Midjourney、Seedream、Nano Banana、SD）向けに設計された人物系プロンプトエンジニア。

| Skill 名 | 用途 |
|---|---|
| [prompt-master-portrait](.claude/skills/prompt-master-portrait/SKILL.md) | 写真級ポートレート／キャラクター設計プロンプトエンジニア。8〜12 項目の深掘り確認プロセスを強制し、バイリンガル（EN/ZH）の精密なプロンプトを 3 つ生成します。いかなる細部も **捏造を禁止** します。 |
| [prompt-master-character-sheet](.claude/skills/prompt-master-character-sheet/SKILL.md) | キャラクター設計三面図（front/side/back）プロンプト専門家。キャラクター画像を受け取ると元の画風を保持し、純白背景の標準的なバストアップ三面図 prompt を生成します。 |
| [prompt-master-general](.claude/skills/prompt-master-general/SKILL.md) | **汎用型** ビジュアルプロンプト主任エンジニア。ABCD 選択式で必ず 3 問を質問した後、3 つのバリエーション（撮影／アートスタイル／被写体／シーン）を生成します。ユーザーが「通用」と述べた場合に優先的にトリガーされます。 |
| [prompt-master-anime](.claude/skills/prompt-master-anime/SKILL.md) | アニメ風ビジュアルアーキテクト。あらゆる入力画像から元のスタイルを剥ぎ取り、2D アニメの画面で再レンダリング（厚塗り、セルシェーディングなど）し、NanoBanana/SeeDream 級の英語 prompt を出力します。 |
| [prompt-master-otaku-sd](.claude/skills/prompt-master-otaku-sd/SKILL.md) | 究極のオタク AI + Stable Diffusion 神絵師。萌え系／二次元キャラクター（ツンデレ、絶対領域、猫耳、メカ娘など）に特化し、異なるシチュエーションの SD 英語 prompt を 3 つ自動生成します。 |
| [prompt-master-otaku-anima](.claude/skills/prompt-master-otaku-anima/SKILL.md) | 究極のオタク AI + Anima モデル専用プロンプト職人。断片的／曖昧な指示から萌え系キャラクターを設計し、Anima（テキストエンコーダ Qwen3）特有の「Danbooru タグ＋自然言語ハイブリッド」記法で複数シーンの高品質な英語 prompt を生成します。衣装を扱う際は costume-design-director を自動連携します。 |
| [prompt-master-hybrid-realism](.claude/skills/prompt-master-hybrid-realism/SKILL.md) | アニメとリアルのハイブリッドレンダリング監督。2D アニメキャラクターと PBR 物理ベースのリアルな質感（衣装、アクセサリー、背景）を融合し、高い実在感のバイリンガル prompt を生成します。 |
| [prompt-master-makeup](.claude/skills/prompt-master-makeup/SKILL.md) | 巨匠級メイクアップビジュアルプロンプトエンジニア。プロのメイク理論を用いて被写体固有の特徴（そばかす、一重まぶた、非対称の骨格）を引き立て、画一的な「完璧」テンプレートを **拒否** します。 |
| [prompt-master-manga-screentone](.claude/skills/prompt-master-manga-screentone/SKILL.md) | AI ビジュアル錬金術師。入力画像を「高コントラスト・線なし水彩 + スクリーントーン（Screentone）」の漫画風 prompt に変換し、元の背景と繁体字中国語の看板／文字を **厳密に保持** します。 |

---

### 4️⃣ 画像プロンプトエンジニアリング — シーン / オブジェクト / 編集

シーン設計、画像編集、九宮格（3x3 グリッド）、商品撮影、トイ撮影、リバースエンジニアリング向けのプロンプトツール。

| Skill 名 | 用途 |
|---|---|
| [prompt-master-scene-architect](.claude/skills/prompt-master-scene-architect/SKILL.md) | アニメシーンアーキテクト。1 枚の 2D シーン画像から完全な 360° 環境を推論し、2x2 の 4 アングルグリッド（正面、左 90°、右 90°、後 180°）の英語 YAML prompt を生成します。 |
| [prompt-master-image-editor](.claude/skills/prompt-master-image-editor/SKILL.md) | 自然言語画像編集アーキテクト v4.0。曖昧な編集指示（例：「車を赤くする」）を、「編集後の最終画像」を完全に記述する高密度な英語 prompt に翻訳します。デフォルトで元の画風を保持します。 |
| [prompt-master-9panel-grid](.claude/skills/prompt-master-9panel-grid/SKILL.md) | 九宮格（3x3）絵コンテ監督。「九宮格 / 3x3 storyboard grid」専用で、入力画像の核心的なビジュアル特徴を抽出した後、9 コマの映画級カメラワークのバリエーションを YAML prompt で設計します。 |
| [prompt-reverse-engineer](.claude/skills/prompt-reverse-engineer/SKILL.md) | ビジュアル言語リバースエンジニア。入力画像をピクセルレベルで意味的に分解（4 つの分析次元）し、再現可能な英語 prompt + 繁体字中国語の分析を生成します。いかなるデフォルトスタイルも **押し付けません**。 |
| [product-visual-architect](.claude/skills/product-visual-architect/SKILL.md) | AI 商品ビジュアルアーキテクト。商品のテキスト説明または画像を、3 組の補完的な商業級撮影プロンプト（メイン画像／ライフスタイル／マクロなど）に変換します。各組は「光線・環境・構図・フォーカスと質感・色彩」の 5 大要領に基づいて構築され、中英対訳付き、Nano Banana / GPT-image2 などの高パラメータモデルに対応。即時生成・質問なし。 |
| [toy-photography-architect](.claude/skills/toy-photography-architect/SKILL.md) | 超リアルなトイ／模型撮影アーキテクト。実物のトイ／フィギュアを、ダイナミックなカメラワーク、環境ストーリーテリング、ガレージキット塗装技法によって、映画級のリアルな映像 prompt へと昇華させます。 |

---

### 5️⃣ 映像・音声プロンプトエンジニアリング

動態生成（モーション生成）、テキスト → 動画（t2v）、画像 → 動画（i2v）、ショート動画、絵コンテ、音楽、歌詞、ボイス設計向けのツール群。

> **🎬 映像生成 3 択**（この 3 つは最も混同しやすいため、ユーザーのキーワードに従ってルーティングしてください）：
>
> | やりたいこと | トリガーキーワード | 対応 Skill | 出力形式 |
> |---|---|---|---|
> | 汎用的な動態生成（**デフォルト**） | 動態 / 動態生成 / 動態提示詞 | `prompt-master-video-continuity` | 単一の YAML ブロック、音声トラック付き、≤ 1300 文字 |
> | テキスト → 動画 | 文生影 / t2v / text-to-video | `prompt-master-text-to-video` | ワンショット ＋ マルチショットの 2 種のバイリンガル映画脚本 |
> | 画像 → 動画 | 圖生影 / i2v / img2video | `prompt-master-image-to-video` | プラン A 繊細 ＋ プラン B ダイナミック、バイリンガル ＋ 構造サマリー |

| Skill 名 | 用途 |
|---|---|
| [prompt-master-video-continuity](.claude/skills/prompt-master-video-continuity/SKILL.md) | AI 映像連続性監督 + ボイスデザイナー（**動態生成のデフォルト**）。**単一の YAML ブロック・音声トラック付き** の camera-ready prompt を生成し、ビジュアルの連続性・キャラクターのロック・電報式スタイルを強制、ハードリミット 1300 文字。広く「動態生成」を指す場合は一律この skill を使用します。 |
| [prompt-master-text-to-video](.claude/skills/prompt-master-text-to-video/SKILL.md) | AI テキスト → 動画プロンプトアーキテクト（**文生影 / t2v**、Sora2、Veo3、Kling、Seedance、海螺に対応）。大まかな構想を自律的に補完し、2 種の映画級脚本——【プラン 1：ワンショット】＋【プラン 2：マルチショットシーケンス 3〜4 カット】——を生成します。各々完全な英語原文 + 繁体字訳と任意のセリフを含み、全工程で質問せず、テキストのみを書きます。明確に「文生影 / t2v」と指定された場合 **のみ** トリガーされます。 |
| [prompt-master-image-to-video](.claude/skills/prompt-master-image-to-video/SKILL.md) | 海螺 AI ビジュアルダイナミクスアーキテクト（**圖生影 / i2v**）。1 枚の画像を実行性の高いモーションプロンプトに翻訳し、「プラン A 繊細・ミクロ ＋ プラン B 壮大・爆発」の 2 つの対比提案を生成します。各々英語段落、中国語訳、構造サマリー（被写体／背景のモーション、カメラワーク）を含みます。テキストのみを書き、画像は生成しません。明確に「圖生影 / i2v」と指定された場合 **のみ** トリガーされます。純粋なテキスト構想は text-to-video を、広く「動態生成」を指す場合は video-continuity を使用してください。 |
| [prompt-master-short-video](.claude/skills/prompt-master-short-video/SKILL.md) | 雰囲気系ショート動画チーフディレクター（Vlog 風）。1 枚の静止画から 15〜25 秒の TikTok/Reels/Shorts 脚本を 3 つ生成し、女性主人公の雰囲気と没入感のあるムードを重視します。 |
| [storyboard-director](.claude/skills/storyboard-director/SKILL.md) | アニメ映画の絵コンテ監督 + AI 撮影エキスパート。キャラクター設定、シーン設計、テキストのストーリーを、一連の映画級の英語 text-to-image prompt 絵コンテに翻訳します。 |
| [ai-music-prompt-generator](.claude/skills/ai-music-prompt-generator/SKILL.md) | Suno / Udio 専用音楽プロンプト専門家。抽象的な感情／ジャンル融合のニーズ（例：「古風 × サイバーパンク」）を、600〜800 文字の「反凡庸プロトコル」を含むプロダクション級 tags に翻訳します。 |
| [prompt-master-lyrics](.claude/skills/prompt-master-lyrics/SKILL.md) | 巨匠級作詞アーキテクト + Suno 構造タグ職人。Berklee の Pat Pattison システムと中華圏の巨匠（林夕、姚謙、李宗盛、方文山）の手法を融合し、必ず 3 問質問した後に 3 つのバリエーション歌詞を生成します。 |
| [voice-design-director](.claude/skills/voice-design-director/SKILL.md) | ハリウッド級ボイス＆聴覚体験ディレクター。抽象的なキャラクター設定や感情のニーズに対し、文学性に富み演技可能な英語のボイスデザインを 3 つ生成します。 |

---

### 6️⃣ スタイリング / デザイン

キャラクターの性格、背景、シーンに基づき、論理的に一貫した物語駆動の衣装スタイリングを生成します。

| Skill 名 | 用途 |
|---|---|
| [costume-design-director](.claude/skills/costume-design-director/SKILL.md) | キャラクター衣装ビジュアルディレクター。「衣装こそ物語（Wardrobe is Narrative）」を理念とし、キャラクターの性格・背景・感情・場面・気候に基づいて論理的に一貫したバイリンガル（EN/ZH）の衣装デザインを生成します。アクセサリーは 3 点以内。 |

---

### 7️⃣ ソーシャルメディアビジュアルレイアウト

コラム記事の内容を、対応するソーシャルメディアのビジュアルレイアウト案に変換します。

| Skill 名 | 用途 |
|---|---|
| [social-media-visual-designer](.claude/skills/social-media-visual-designer/SKILL.md) | シニアソーシャルメディアビジュアルデザイナー。コラム内容を受け取ると、即座に 16:9 のミニマルな雑誌風ビジュアルレイアウト案を生成し、記事の属性に応じてカラーロジックを動的に決定します。 |

---

### 8️⃣ AI 生成実行ツール（API を直接呼び出し）

プロンプト作成系の skill とは異なり、この 3 つは **実際に GMI Cloud API を呼び出して画像／動画を出力する** 実行可能ツールです（Python スクリプト内蔵：送信 → ポーリング → ダウンロード）。さらに **ユーザーが明確にモデル名を述べた場合のみ** トリガーされ、汎用的な「画像生成」「動画生成」といった語は一律プロンプト系 skill が処理します。

| Skill 名 | 用途 |
|---|---|
| [gemini-3-pro-image](.claude/skills/gemini-3-pro-image/SKILL.md) | GMI Cloud `gemini-3-pro-image-preview` API を実際に呼び出して本物の画像を生成／編集する実行ツール（**プロンプト作成器ではありません**）。モデル名（gemini 3 pro image、nano banana pro、奈米香蕉 pro）を明示した場合のみトリガーされます。単に「nano banana／奈米香蕉」（pro なし）と言った場合は別モデルのためトリガーされません。 |
| [gpt-image-2](.claude/skills/gpt-image-2/SKILL.md) | OpenAI の gpt-image-2 を GMI Cloud の非同期リクエストキュー API 経由で呼び出し、実際に画像を生成／編集する実行ツール（**プロンプト作成器ではありません**）。1 本のデュアルモードスクリプトで、入力画像なしなら `gpt-image-2-generate`（テキスト → 画像）、入力画像ありなら `gpt-image-2-edit`（画像ごとに 1 リクエスト）を実行します。モデル名／プロバイダ名（gpt-image-2、gpt image 2、GMI、GMI Cloud）を明示した場合のみトリガーされます。 |
| [seedance-2-0](.claude/skills/seedance-2-0/SKILL.md) | GMI Cloud `seedance-2-0-260128` API を実際に呼び出して本物の動画を生成する実行ツール（**プロンプト作成器ではありません**）。モデル名（seedance 2、seedance 2.0）を明示した場合のみトリガーされます。単に「seedance」（2 なし）または「seedance 2 fast」と言った場合は別モデルのためトリガーされません。 |

---

### 9️⃣ 開発ツール

Git / GitHub 自動化などの開発補助ツール。

| Skill 名 | 用途 |
|---|---|
| [git-github-pusher](.claude/skills/git-github-pusher/SKILL.md) | Git 初期化 + リモート競合の処理 + GitHub へのプッシュという一連の流れを自動化します。ユーザーが「push」「上傳 github」と言った場合にトリガーされます。 |

---

## 🚀 使い方

1. **自動トリガー**：すべての skill は `description` 内にトリガーワードが設定されており、ユーザーの会話内容がキーワードにヒットすると、Claude Code が対応する skill を自動的に読み込みます。例えば「この画像の **圖生影** プロンプトを作って」と入力すると `prompt-master-image-to-video` が読み込まれ、「**文生影** 脚本」なら `prompt-master-text-to-video` が読み込まれます。
2. **手動指定**：メッセージ内に直接 skill 名を書くことができます。例：「`prompt-master-portrait` で人物 prompt を設計して」。
3. **連携チェーン**：一部の skill は他の skill を自動的に連携します（例：`prompt-master-otaku-sd` / `prompt-master-otaku-anima` は衣装を扱う際に `costume-design-director` を自動呼び出し、`skill-creator` は完了後に必ず `skill-optimizer` と `skill-translator` をトリガーします）。

---

## 📁 ディレクトリ構成

```
biz-ai-video-course/
├── .claude/
│   ├── settings.local.json
│   └── skills/                          ← 34 個の skill メインディレクトリ
│       ├── ai-music-prompt-generator/
│       │   ├── SKILL.md                 ← skill メインファイル
│       │   └── references/              ← Progressive Disclosure の詳細リファレンス
│       ├── prompt-master-portrait/
│       └── ... (全 34 個)
└── README.md                            ← 本ファイル
```

各 skill には以下が含まれます：
- **`SKILL.md`**：簡潔な中核指令（< 200 行）。役割、Prime Directives（最優先命令）、実行フローを定義します。
- **`references/`**：Progressive Disclosure パターンで分離された詳細なナレッジベース（スタイル辞典、分析フレームワークなど）。必要なときにのみ skill が能動的に読み込みます。
- **`docs/`**（一部の skill）：`skill-translator` が生成した繁体字中国語の人間可読版。実行時に AI が **一切読み込みません**。

---

## 🎯 設計思想

1. **Progressive Disclosure（漸進的開示）**：SKILL.md を簡潔に保ち、詳細な知識は `references/` に委ね、context window の汚染を防ぎます。
2. **No Hallucination（幻覚の排除）**：多くの prompt 系 skill は細部の捏造を厳格に禁止し、必ず先に確認するか、元の入力特徴を保持します。
3. **Bilingual Output（バイリンガル出力）**：画像／動画 prompt の多くは「英語 prompt + 繁体字説明」のセットを採用し、モデルへの入力と人間の理解を両立させます。
4. **Mandatory Protocols（強制プロトコル）**：高品質な skill は概して強制的な質問や構造化された ABCD 選択肢を採用し、低品質なデフォルト出力を回避します。

---
---

# 繁體中文

這個專案集結了 **34 個專業 Skill**，涵蓋 **商業內容創作**、**AI 影音生成（動態生成 / 文生影 / 圖生影）**、**圖像提示詞工程**、**劇本與角色創作**，以及**直接呼叫 GMI Cloud API 出圖／出片的執行工具**。所有技能皆位於 `.claude/skills/` 目錄下，由 Claude Code 在偵測到對應觸發詞時自動載入並執行，無需手動設定。

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

從碎片線索逆向建構角色、深度分析劇本。

| Skill 名稱 | 用途 |
|---|---|
| [character-architect](.claude/skills/character-architect/SKILL.md) | 好萊塢編劇 + 角色架構師（奧斯卡級，兼具社會學/心理學洞察）。從一句台詞、一件配飾或單張照片的構圖光影等碎片線索逆向建構角色，產出**三份**差異最大化、內部自洽的繁中角色檔案（外型/社會屬性、家庭背景與創傷、MBTI/星座/血型一致性、語言習慣與微表情 + 電影級摘要）。觸發詞：「角色設定」「人設」「人物塑造」等。 |
| [script-doctor-architect](.claude/skills/script-doctor-architect/SKILL.md) | 好萊塢頂級劇本醫生。接收劇本後產出高度結構化的「劇本分析報告」，拆解敘事結構、角色心理、事件時間軸與市場定位。 |

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
| [prompt-master-manga-screentone](.claude/skills/prompt-master-manga-screentone/SKILL.md) | AI 視覺煉金術士。將輸入圖轉為「高對比無線條水彩 + 網點 (Screentone)」漫畫風 prompt，**嚴格保留**原始背景與繁體中文招牌/文字。 |

---

### 4️⃣ 圖像提示詞工程 — 場景 / 物件 / 編輯

針對場景設計、圖像編輯、九宮格、產品攝影、玩具攝影、逆向工程的提示詞工具。

| Skill 名稱 | 用途 |
|---|---|
| [prompt-master-scene-architect](.claude/skills/prompt-master-scene-architect/SKILL.md) | 動畫場景架構師。從單張 2D 場景圖推演完整 360° 環境，產出 2x2 四視角網格（正面、左 90°、右 90°、後 180°）的英文 YAML prompt。 |
| [prompt-master-image-editor](.claude/skills/prompt-master-image-editor/SKILL.md) | 自然語言圖像編輯架構師 v4.0。將模糊的編輯指令（如「把車變紅色」）翻譯為完整描述「最終編輯後圖像」的高密度英文 prompt，預設保留原始畫風。 |
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

### 6️⃣ 造型 / 設計

依角色個性、背景與場景，產出邏輯一致、敘事驅動的服裝造型。

| Skill 名稱 | 用途 |
|---|---|
| [costume-design-director](.claude/skills/costume-design-director/SKILL.md) | 角色服裝視覺總監。理念為「衣著即敘事 (Wardrobe is Narrative)」，依角色個性、背景、情緒、場合、氣候產出邏輯一致的雙語（EN/ZH）服裝設計，配件 ≤ 3 件。 |

---

### 7️⃣ 社群視覺排版

將專欄文章內容轉化為對應的社群視覺排版方案。

| Skill 名稱 | 用途 |
|---|---|
| [social-media-visual-designer](.claude/skills/social-media-visual-designer/SKILL.md) | 資深社群視覺設計師。接收專欄內容後立刻產出 16:9 極簡雜誌風視覺排版方案，依文章屬性動態決定色彩邏輯。 |

---

### 8️⃣ AI 生成執行工具（直接呼叫 API）

與提示詞撰寫類 skill 不同，這三個是**真正呼叫 GMI Cloud API 出圖／出片**的可執行工具（內建 Python 腳本：提交 → 輪詢 → 下載），且**僅在使用者明確說出模型名稱時**才觸發，泛用的「圖片生成」「影片生成」字眼一律交由提示詞類 skill 處理。

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
│   └── skills/                          ← 34 個 skill 主目錄
│       ├── ai-music-prompt-generator/
│       │   ├── SKILL.md                 ← skill 主檔
│       │   └── references/              ← 漸進式揭露的詳細參考
│       ├── prompt-master-portrait/
│       └── ... (共 34 個)
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
