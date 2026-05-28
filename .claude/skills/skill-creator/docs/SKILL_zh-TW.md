---
name: skill-creator
description: Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations. You MUST ALWAYS load and trigger skill-optimizer and skill-translator to finalize the skill creation.
license: Complete terms in LICENSE.txt
---

# Skill Creator (技能建立器)

本技能提供建立有效技能的指南。

## 關於技能 (About Skills)

技能是模組化、獨立的套件，透過提供專業知識、工作流程和工具來擴展 Claude 的能力。將它們視為特定領域或任務的「入門指南」— 它們將 Claude 從通用型代理轉換為具備模型無法完全擁有的程序性知識的專業代理。

### 技能提供的內容 (What Skills Provide)

1. 特定的工作流程 (Specialized workflows) - 針對特定領域的多步驟程序
2. 工具整合 (Tool integrations) - 處理特定文件格式或 API 的指示
3. 領域專業知識 (Domain expertise) - 公司特定的知識、架構 (schemas)、業務邏輯
4. 綑綁資源 (Bundled resources) - 用於複雜和重複性任務的腳本、參考資料和素材

## 核心原則 (Core Principles)

### 簡潔是關鍵 (Concise is Key)

上下文視窗是一項公共資源。技能必須與 Claude 所需的所有其他內容共享上下文視窗：系統提示詞、對話歷史、其他技能的元數據，以及實際的使用者請求。

**預設假設：Claude 已經非常聰明。** 僅添加 Claude 尚未擁有的上下文。對每一段資訊提出質疑：「Claude 真的需要這個解釋嗎？」以及「這段文字值得它所消耗的 token 成本嗎？」

偏好提供簡潔的範例，而非冗長的解釋。

### 設定適當的自由度 (Set Appropriate Degrees of Freedom)

根據任務的脆弱性和可變性來搭配合適的具體程度：

**高自由度 (基於文字的指示)**：當多種方法都有效、決策取決於上下文，或者由啟發式方法引導時使用。

**中等自由度 (帶有參數的虛擬程式碼或腳本)**：當存在偏好的模式、可接受一定程度的變化，或者配置會影響行為時使用。

**低自由度 (具體的腳本、少量參數)**：當操作非常脆弱且容易出錯、一致性至關重要，或者必須遵循特定順序時使用。

將 Claude 想像成在探索一條路徑：懸崖旁的狹窄橋樑需要具體的護欄 (低自由度)，而開闊的原野則允許多種路線 (高自由度)。

### 技能的剖析 (Anatomy of a Skill)

每個技能都包含一個必備的 SKILL.md 檔案和可選的綑綁資源：

```
skill-name/
├── SKILL.md (必備)
│   ├── YAML frontmatter 元數據 (必備)
│   │   ├── name: (必備)
│   │   ├── description: (必備)
│   │   └── compatibility: (可選，極少需要)
│   └── Markdown 指示說明 (必備)
└── Bundled Resources 綑綁資源 (可選)
    ├── scripts/          - 可執行的程式碼 (Python/Bash 等)
    ├── references/       - 打算在需要時載入上下文的參考文件
    └── assets/           - 用於輸出的檔案 (模板、圖示、字體等)
```

#### SKILL.md (必備)

每個 SKILL.md 包含：

- **Frontmatter** (YAML)：包含 `name` 和 `description` 欄位 (必備)，以及可選欄位如 `license`、`metadata` 和 `compatibility`。Claude 只會讀取 `name` 和 `description` 來決定何時觸發技能，因此請清晰且全面地說明這個技能是什麼以及何時應該使用它。`compatibility` 欄位用於註明環境需求 (目標產品、系統套件等)，但大多數技能不需要它。
- **Body** (Markdown)：使用該技能的指示和指引。只有在技能觸發後 (如果有的話) 才會載入。

#### 綑綁資源 (Bundled Resources - 可選)

##### 腳本 (`scripts/`)

可執行的程式碼 (Python/Bash 等)，用於需要確定性可靠度或一再被重複編寫的任務。

- **何時包含**：當同一段程式碼被重複編寫或需要確定性可靠度時
- **範例**：用於旋轉 PDF 任務的 `scripts/rotate_pdf.py`
- **好處**：節省 token、具確定性、可以在不載入上下文的情況下執行
- **注意**：腳本可能仍需要被 Claude 讀取，以進行修補或針對特定環境的調整

##### 參考資料 (`references/`)

打算在需要時載入上下文的文件和參考素材，以提供 Claude 過程思考的資訊。

- **何時包含**：當存在 Claude 在工作時應該參考的文件時
- **範例**：用於財務架構的 `references/finance.md`，用於公司保密協議模板的 `references/mnda.md`，用於公司政策的 `references/policies.md`，用於 API 規格的 `references/api_docs.md`
- **使用案例**：資料庫架構 (schemas)、API 文件、領域知識、公司政策、詳細的工作流程指南
- **好處**：保持 SKILL.md 精簡，僅在 Claude 判斷需要時載入
- **最佳實踐**：如果檔案很大 (>10k 字)，請在 SKILL.md 中包含 grep 搜尋模式
- **避免重複**：資訊應該存在於 SKILL.md 或參考檔案中，而不是兩者皆有。對於詳細資訊，優先使用參考檔案，除非它是技能的真正核心——這使 SKILL.md 保持精簡，同時讓資訊可被發現，而不會佔用上下文視窗。在 SKILL.md 中僅保留必要的程序性指示和工作流程指導；將詳細的參考資料、架構和範例移至參考檔案。

##### 素材 (`assets/`)

不打算載入上下文的檔案，而是用於 Claude 產生的最終輸出中。

- **何時包含**：當技能需要將用於最終輸出的檔案時
- **範例**：用於品牌素材的 `assets/logo.png`，用於 PowerPoint 模板的 `assets/slides.pptx`，用於 HTML/React 樣板的 `assets/frontend-template/`，用於字體的 `assets/font.ttf`
- **使用案例**：模板、圖片、圖示、樣板程式碼 (boilerplate code)、字體、被複製或修改的範例文件
- **好處**：將輸出資源與文件分離，使 Claude 能夠使用檔案而無需將其載入上下文

#### 不該包含在技能中的內容 (What to Not Include in a Skill)

技能應該只包含直接支持其功能的必要檔案。不要建立多餘的文件或輔助檔案，包括：

- README.md
- INSTALLATION_GUIDE.md
- QUICK_REFERENCE.md
- CHANGELOG.md
- 等等

技能應該只包含 AI 代理完成當前工作所需的資訊。它不應該包含關於建立該技能的過程、設定和測試程序、面向使用者的文件等輔助上下文。建立額外的文件檔案只會增加混亂和困惑。

### 漸進式揭露設計原則 (Progressive Disclosure Design Principle)

技能使用三層載入系統來有效管理上下文：

1. **Metadata (name + description)** - 永遠在上下文中 (~100 字)
2. **SKILL.md 本文** - 當技能觸發時載入 (<5k 字)
3. **綑綁資源 (Bundled resources)** - 當 Claude 需要時載入 (無限制，因為腳本可以在不讀入上下文視窗的情況下執行)

#### 漸進式揭露模式 (Progressive Disclosure Patterns)

將 SKILL.md 本文保持在必要內容，並限制在 500 行以內，以最小化上下文膨脹。接近此限制時，將內容拆分到獨立檔案中。將內容拆分到其他檔案時，非常重要的是在 SKILL.md 中引用它們，並清楚說明何時閱讀它們，以確保技能閱讀者知道它們的存在以及何時使用。

**關鍵原則：** 當技能支援多種變體、框架或選項時，只將核心工作流程和選擇指南保留在 SKILL.md 中。將特定於變體的細節 (模式、範例、配置) 移至獨立的參考檔案中。

**模式1：帶有參考資料的高階指南 (Pattern 1: High-level guide with references)**

```markdown
# PDF 處理

## 快速開始

使用 pdfplumber 提取文字：
[程式碼範例]

## 進階功能

- **表單填寫**：查看 [FORMS.md](FORMS.md) 獲取完整指南
- **API 參考**：查看 [REFERENCE.md](REFERENCE.md) 獲取所有方法
- **範例**：查看 [EXAMPLES.md](EXAMPLES.md) 獲取常見模式
```

Claude 只有在需要時才會載入 FORMS.md、REFERENCE.md 或 EXAMPLES.md。

**模式2：特定領域的組織 (Pattern 2: Domain-specific organization)**

對於具有多個領域的技能，按領域組織內容以避免載入無關的上下文：

```
bigquery-skill/
├── SKILL.md (概述和導航)
└── reference/
    ├── finance.md (收入、計費指標)
    ├── sales.md (機會、銷售漏斗)
    ├── product.md (API 使用、功能)
    └── marketing.md (行銷活動、歸因)
```

當使用者詢問關於銷售指標時，Claude 只會閱讀 sales.md。

同樣的，對於支援多種框架或變體的技能，按變體組織：

```
cloud-deploy/
├── SKILL.md (工作流程 + 服務商選擇)
└── references/
    ├── aws.md (AWS 部署模式)
    ├── gcp.md (GCP 部署模式)
    └── azure.md (Azure 部署模式)
```

當使用者選擇 AWS 時，Claude 只讀取 aws.md。

**模式3：條件性細節 (Pattern 3: Conditional details)**

顯示基本內容，連結到進階內容：

```markdown
# DOCX 處理

## 建立文件

使用 docx-js 建立新文件。查看 [DOCX-JS.md](DOCX-JS.md)。

## 編輯文件

對於簡單編輯，直接修改 XML。

**對於追蹤修訂**：查看 [REDLINING.md](REDLINING.md)
**對於 OOXML 細節**：查看 [OOXML.md](OOXML.md)
```

Claude 只有在使用者需要這些功能時才會閱讀 REDLINING.md 或 OOXML.md。

**重要指導方針：**

- **避免深層次巢狀引用** - 使參考檔案與 SKILL.md 保持單層級關係。所有參考檔案應直接從 SKILL.md 連結。
- **結構化較長的參考檔案** - 對於超過 100 行的檔案，在頂部包含目錄，以便 Claude 在預覽時能看到完整範圍。

## 技能建立流程 (Skill Creation Process)

建立技能包含以下步驟：

1. 透過具體範例理解技能
2. 規劃可重複使用的技能內容 (腳本、參考資料、素材)
3. 初始化技能 (執行 init_skill.py)
4. 編輯技能 (實作資源並撰寫 SKILL.md)
5. 打包技能 (執行 package_skill.py)
6. 最佳化與翻譯 (強制性後處理)
7. 根據實際使用情況迭代

按照順序執行這些步驟，只有在有明確理由表明不適用時才跳過。

### 步驟1：透過具體範例理解技能 (Step 1: Understanding the Skill with Concrete Examples)

除非技能的使用模式已經非常清楚，否則不要跳過此步驟。即使在修改現有技能時，這一步仍很有價值。

為了建立一個有效的技能，清楚了解將如何使用該技能的具體範例。這種理解可以來自直接的使用者範例，或生成並通過使用者反饋驗證的範例。

例如，在建立 image-editor (圖片編輯器) 技能時，相關問題包括：

- 「image-editor 技能應支援哪些功能？編輯、旋轉、還有其他的嗎？」
- 「你能給一些這個技能如何被使用的範例嗎？」
- 「我可以想像使用者會提出像『移除這張照片的紅眼』或『旋轉這張圖片』的要求。你還能想像這個技能有其他使用方式嗎？」
- 「使用者說什麼應該觸發這個技能？」

為了避免讓使用者感到不知所措，不要在單一訊息中詢問太多問題。從最重要的問題開始，根據需要跟進，以達到最佳效果。

當清楚了解技能應支援的功能時，總結此步驟。

### 步驟2：規劃可重複使用的技能內容 (Step 2: Planning the Reusable Skill Contents)

為了將具體範例轉化為有效技能，透過以下方式分析每個範例：

1. 考慮如何從零開始執行該範例
2. 識別在重複執行這些工作流程時，哪些腳本、參考資料和素材會有所幫助

範例：建立 `pdf-editor` 技能以處理如「幫我旋轉這個 PDF」的要求時，分析顯示：

1. 旋轉 PDF 需要每次重新編寫相同的程式碼
2. 一個 `scripts/rotate_pdf.py` 腳本如果在技能中儲存會很有幫助

範例：設計 `frontend-webapp-builder` 技能以響應如「幫我建一個待辦事項應用」或「建一個儀表板來追蹤我的步數」時，分析顯示：

1. 編寫前端網頁應用需要每次寫相同的樣板 HTML/React
2. 在技能中儲存包含樣板 HTML/React 專案檔案的 `assets/hello-world/` 模板會很有用

範例：建立 `big-query` 技能處理如「今天有多少使用者登入？」的要求時，分析顯示：

1. 查詢 BigQuery 需要每次重新發現資料表層級結構和關聯
2. 一份記錄資料表結構的 `references/schema.md` 檔案如果儲存在技能中會很有幫助

為了確定技能的內容，分析每個具體範例，建立一個要包含的可重複使用資源清單：腳本、參考資料和素材。

### 步驟3：初始化技能 (Step 3: Initializing the Skill)

到了這個階段，是時候真正建立技能了。

只有當正在開發的技能已經存在，並且需要進行迭代或打包時，才跳過此步驟。在此情況下，繼續下一步。

從零開始建立新技能時，必須始終運行 `init_skill.py` 腳本。該腳本能方便地產生一個新的技能目錄範本，並自動包含技能所需的所有內容，使技能建立過程更高效、更可靠。

使用方法：

```bash
scripts/init_skill.py <skill-name> --path <output-directory>
```

該腳本將：

- 在指定路徑建立技能目錄
- 產生帶有適當 frontmatter 和 TODO 佔位符的 SKILL.md 範本
- 建立範例資源目錄：`scripts/`、`references/` 和 `assets/`
- 在每個目錄中加入可自訂或刪除的範例檔案

初始化後，根據需要自訂或刪除產生的 SKILL.md 和範例檔案。

### 步驟4：編輯技能 (Step 4: Edit the Skill)

在編輯（新產生或現有的）技能時，請記住這個技能是為另一個 Claude 實例建立的。請包含對 Claude 而言有益且非顯然的資訊。考慮哪些程序性知識、特定領域細節或可重複使用的素材將幫助另一個 Claude 實例更有效地執行這些任務。

#### 學習經證實的設計模式 (Learn Proven Design Patterns)

根據您的技能需求，參考以下實用指南：

- **多步驟流程 (Multi-step processes)**：請查看 references/workflows.md 以了解順序工作流程和條件邏輯
- **特定輸出格式或品質標準 (Specific output formats or quality standards)**：請查看 references/output-patterns.md 以了解模板和範例模式

這些檔案包含有效技能設計的既定最佳實務。

#### 從可重複使用的技能內容開始 (Start with Reusable Skill Contents)

開始實作時，先處理上述識別的可重複使用資源：`scripts/`、`references/` 和 `assets/` 檔案。注意，此步驟可能需要使用者的輸入。例如，在實作 `brand-guidelines` 技能時，使用者可能需要提供用於儲存在 `assets/` 的品牌素材或範本，或者提供用於 `references/` 的文件。

加入的腳本必須實際運行測試，確保沒有錯誤且輸出符合預期。如果有許多類似的腳本，只需測試其中具代表性的部分，以平衡確保功能正常和完成時間。

應該刪除技能不需要的任何範例檔案和目錄。初始化腳本在 `scripts/`、`references/` 和 `assets/` 中建立範例檔案只是為了展示結構，但大多數技能不需要全部這些檔案。

#### 更新 SKILL.md (Update SKILL.md)

**寫作指引：** 必須使用祈使句/不定式形式。

##### Frontmatter

撰寫包含 `name` 和 `description` 的 YAML frontmatter：

- `name`：技能名稱
- `description`：這是技能的主要觸發機制，並幫助 Claude 理解何時使用該技能。
  - 包含技能的功能以及何時使用它的具體觸發條件/上下文。
  - 將所有「何時使用」的資訊放在這裡 - 不要放在本文中。本文僅在觸發後載入，因此本文中的「何時使用此技能」章節對 Claude 沒有幫助。
  - `docx` 技能的敘述範例："Comprehensive document creation, editing, and analysis with support for tracked changes, comments, formatting preservation, and text extraction. Use when Claude needs to work with professional documents (.docx files) for: (1) Creating new documents, (2) Modifying or editing content, (3) Working with tracked changes, (4) Adding comments, or any other document tasks"

不要在 YAML frontmatter 中加入任何其他欄位。

##### 本文 (Body)

撰寫使用技能及其綑綁資源的指示。

### 步驟5：打包技能 (Step 5: Packaging a Skill)

技能開發完成後，必須將其打包為可分發的 .skill 檔案，以便與使用者分享。打包流程會自動先驗證技能，確保其符合所有要求：

```bash
scripts/package_skill.py <path/to/skill-folder>
```

可選的輸出目錄指定：

```bash
scripts/package_skill.py <path/to/skill-folder> ./dist
```

打包腳本將：

1. **自動驗證** 技能，檢查：

   - YAML frontmatter 格式與必填欄位
   - 技能命名慣例和目錄結構
   - 描述的完整性和品質
   - 檔案組織和資源引用

2. **打包** 如果驗證通過，將建立一個以技能命名的 .skill 檔案（例如 `my-skill.skill`），其中包含所有檔案並保持正確的目錄結構以供分發。 .skill 檔案是帶有 .skill 副檔名的 zip 檔案。

如果驗證失敗，腳本將回報錯誤並退出而不建立套件。請修復任何驗證錯誤，然後再次運行打包命令。

### 步驟6：最佳化與翻譯 (強制性後處理) (Step 6: Optimize and Translate - Mandatory Post-Processing)

建立或更新技能後，請**務必**觸發最佳化和翻譯工作流程，以確保該技能滿足上下文視窗效率並且對人類使用者友善。

1. **觸發 `skill-optimizer`**：對新建立或更新的技能呼叫 `skill-optimizer` 工具，以實施漸進式揭露原則，將厚重內容提取至 `references/` 檔案中，並極小化 `SKILL.md` 的佔用空間。
2. **觸發 `skill-translator`**：當最佳化完成後，呼叫 `skill-translator` 工具來產生繁體中文 (zh-TW) 版本的說明。這將會儲存到一個 `docs/` 資料夾（例如 `docs/SKILL_zh-TW.md`）。

### 步驟7：迭代 (Step 7: Iterate)

測試完技能後，使用者可能要求改進。這通常發生在使用技能之後，因為如何執行該技能有最新的上下文。

**迭代工作流程：**

1. 在實際任務中使用技能
2. 留意操作困難或效率低下的地方
3. 識別應該如何更新 SKILL.md 或綑綁資源
4. 實施改變並再次測試
