# biz-ai-video-course — Claude Code Skills 技能集合

這個專案集結了 **31 個專業 Skill**，涵蓋 **商業內容創作**、**AI 影音生成（動態生成 / 文生影 / 圖生影）**、**圖像提示詞工程** 與 **劇本創作**。所有技能皆位於 `.claude/skills/` 目錄下，由 Claude Code 在偵測到對應觸發詞時自動載入並執行，無需手動設定。

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

從零打造角色、分析劇本、模擬思想家對話。

| Skill 名稱 | 用途 |
|---|---|
| [character-bible-generator](.claude/skills/character-bible-generator/SKILL.md) | 資深劇本架構師 + 行為心理學家。將最少需求擴展成具有心理深度、缺陷與行為模式的「角色聖經 (Character Bible)」，拒絕扁平完美的瑪麗蘇/傑克蘇。 |
| [script-doctor-architect](.claude/skills/script-doctor-architect/SKILL.md) | 好萊塢頂級劇本醫生。接收劇本後產出高度結構化的「劇本分析報告」，拆解敘事結構、角色心理、事件時間軸與市場定位。 |
| [persona-georg-simmel](.claude/skills/persona-georg-simmel/SKILL.md) | 齊美爾 (Georg Simmel) 角色模擬器。讓 Claude 化身為形式社會學先驅，討論現代性、貨幣異化、都市心理防禦機制等議題。 |

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
| [prompt-master-hybrid-realism](.claude/skills/prompt-master-hybrid-realism/SKILL.md) | 動漫與寫實混合渲染導演。把 2D 動漫角色與 PBR 物理寫實材質（服裝、配件、背景）融合，產出高擬真的雙語 prompt。 |
| [prompt-master-makeup](.claude/skills/prompt-master-makeup/SKILL.md) | 大師級彩妝視覺提示詞工程師。將專業彩妝理論套用於放大主體獨特特徵（雀斑、單眼皮、不對稱骨相），**拒絕**標準化「完美」模板。 |
| [prompt-master-manga-screentone](.claude/skills/prompt-master-manga-screentone/SKILL.md) | AI 視覺煉金術士。將輸入圖轉為「高對比無線條水彩 + 網點 (Screentone)」漫畫風 prompt，**嚴格保留**原始背景與繁體中文招牌/文字。 |

---

### 4️⃣ 圖像提示詞工程 — 場景 / 物件 / 編輯

針對場景設計、圖像編輯、九宮格、玩具攝影、逆向工程的提示詞工具。

| Skill 名稱 | 用途 |
|---|---|
| [prompt-master-scene-architect](.claude/skills/prompt-master-scene-architect/SKILL.md) | 動畫場景架構師。從單張 2D 場景圖推演完整 360° 環境，產出 2x2 四視角網格（正面、左 90°、右 90°、後 180°）的英文 YAML prompt。 |
| [prompt-master-image-editor](.claude/skills/prompt-master-image-editor/SKILL.md) | 自然語言圖像編輯架構師 v4.0。將模糊的編輯指令（如「把車變紅色」）翻譯為完整描述「最終編輯後圖像」的高密度英文 prompt，預設保留原始畫風。 |
| [prompt-master-9panel-grid](.claude/skills/prompt-master-9panel-grid/SKILL.md) | 九宮格分鏡導演。針對「九宮格 / 3x3 storyboard grid」專屬，提取輸入圖的核心視覺特徵後設計 9 格電影級鏡頭變化 YAML prompt。 |
| [prompt-reverse-engineer](.claude/skills/prompt-reverse-engineer/SKILL.md) | 視覺語言逆向工程師。對輸入圖進行像素級語意拆解（4 個分析維度），產出可重現的英文 prompt + 繁體中文分析。**不**強加任何預設風格。 |
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

### 7️⃣ 內容寫作與社群排版

把艱澀內容轉寫為易讀專欄，並產出對應的社群視覺排版方案。

| Skill 名稱 | 用途 |
|---|---|
| [academic-columnist](.claude/skills/academic-columnist/SKILL.md) | 學術專欄作家。將艱澀的哲學/學術對話改寫成 1200 字的 5 段式專欄文章（精彩開頭 + 3 個核心論點 + 有力結論），**零術語、零資訊流失**。 |
| [social-media-visual-designer](.claude/skills/social-media-visual-designer/SKILL.md) | 資深社群視覺設計師。接收專欄內容後立刻產出 16:9 極簡雜誌風視覺排版方案，依文章屬性動態決定色彩邏輯。 |

---

### 8️⃣ 開發工具

Git / GitHub 自動化等開發輔助工具。

| Skill 名稱 | 用途 |
|---|---|
| [git-github-pusher](.claude/skills/git-github-pusher/SKILL.md) | 自動化 Git 初始化 + 處理遠端衝突 + 推送至 GitHub 的全套流程，當使用者說「push」、「上傳 github」時觸發。 |

---

## 🚀 使用方式

1. **自動觸發**：所有 skill 皆已設定 `description` 中的觸發詞，當使用者對話內容命中關鍵字時，Claude Code 會自動載入對應 skill。例如輸入「幫我做這張圖的**圖生影**提示詞」會載入 `prompt-master-image-to-video`，而「**文生影**腳本」則載入 `prompt-master-text-to-video`。
2. **手動指定**：可在訊息中直接寫出 skill 名稱，例如「用 `prompt-master-portrait` 幫我設計一張人像 prompt」。
3. **協作鏈**：部分 skill 會自動串接其他 skill（例如 `prompt-master-otaku-sd` 處理服裝時會自動呼叫 `costume-design-director`、`skill-creator` 完成後一律觸發 `skill-optimizer` 與 `skill-translator`）。

---

## 📁 目錄結構

```
biz-ai-video-course/
├── .claude/
│   ├── settings.local.json
│   └── skills/                          ← 32 個 skill 主目錄
│       ├── academic-columnist/
│       │   ├── SKILL.md                 ← skill 主檔
│       │   └── references/              ← 漸進式揭露的詳細參考
│       ├── prompt-master-portrait/
│       └── ... (共 32 個)
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
