# skill-creator（zh-TW 人類可讀版）

> 本文件為 `SKILL.md` 的繁體中文對照翻譯，僅供人類閱讀；AI 執行時不會載入本檔。
> 原檔最後更新：2026-11-11。內容若有出入，以 `SKILL.md` 為準。
> `references/` 與 `agents/` 底下的檔案為 Anthropic 的英文原文，未另行翻譯（其中 `references/description-optimization.md` 與 `references/other-environments.md` 另含以英文撰寫的本地新增內容）。

## Frontmatter 說明

- **name**：`skill-creator`
- **description（觸發條件）**：建立、改進技能，並用 eval（評測）測試技能（有技能 vs. 對照組〔baseline〕的執行、審閱檢視器、benchmark〔基準測試〕、觸發調校）。只要使用者想做一個技能、改變某個既有技能的功能、修正某個技能一再犯的錯，或為技能撰寫或執行測試案例，即使沒有說出 eval 這個詞也要使用（「做一個技能」「把這個流程做成技能」「修改技能」「技能一直出錯」「改完跑測試」「幫技能做測試」）。不適用於精簡 SKILL.md（→ skill-optimizer），也不負責其 zh-TW 說明文件（→ skill-translator）。
- **license**：`Complete terms in LICENSE.txt`（完整條款見 LICENSE.txt）
- **metadata**：
  - **upstream**（上游來源）：Anthropic 的 skill-creator（Apache-2.0），同步於 2026-11-08
  - **local-changes**（本地修改）：2026-11-11：新增內規（house rules）；description 最佳化與其他環境的說明移至 references/

---

# Skill Creator（技能建立器）

一個用來建立新技能、並反覆迭代改進技能的技能。

從高層次來看，建立技能的流程大致如下：

- 決定你要這個技能做什麼，以及大致該怎麼做
- 寫出技能的草稿
- 設計幾個測試提示詞，讓能使用該技能的 Claude 跑這些提示詞
- 協助使用者從質性與量化兩方面評估結果
  - 在這些執行於背景進行的同時，如果還沒有量化 eval，就先擬幾個（如果已經有了，可以直接沿用，或在你覺得需要調整時加以修改）。接著向使用者說明這些 eval（若原本就有，就說明既有的那些）
  - 用 `eval-viewer/generate_review.py` 腳本把結果呈現給使用者檢視，也讓他們看看量化指標
- 根據使用者評估結果後給的回饋改寫技能（量化 benchmark 若暴露出明顯缺陷，也據此修改）
- 重複以上步驟，直到你滿意為止
- 擴充測試集，以更大的規模再試一次

使用這個技能時，你的工作是判斷使用者目前處於這個流程的哪個階段，然後切入，協助他們推進這些階段。舉例來說，使用者可能會說 "I want to make a skill for X"（我想做一個處理 X 的技能）。你可以幫忙釐清他們的意思、寫草稿、寫測試案例、弄清楚他們想怎麼評估、跑完所有提示詞，然後重複。

另一方面，使用者也可能已經有技能的草稿了。這種情況下，你可以直接進入循環中的評測／迭代部分。

當然，你應該隨時保持彈性；如果使用者說 "I don't need to run a bunch of evaluations, just vibe with me"（我不需要跑一堆評測，跟我一起憑感覺來就好），那就改照這種方式做。

接著，在技能完成之後（不過再強調一次，順序可以彈性調整），你還可以執行技能 description 改進器來最佳化技能的觸發——我們為它另外準備了一整支腳本。

這樣可以吧？可以。

這個版本是 Anthropic 的 skill-creator，再加上下方針對本技能庫的**內規**（house rules）。兩者有衝突時，以內規為準：內規反映的是本技能庫的規模與使用對象。

## 與使用者溝通（Communicating with the user）

skill creator 的使用者，對程式術語的熟悉程度可能天差地遠。如果你還沒聽說（你又怎麼可能聽說，這是最近才開始的事），現在有一股趨勢：Claude 的強大能力正激勵水電工打開他們的終端機，也讓爸媽和爺爺奶奶上 Google 搜尋 "how to install npm"（如何安裝 npm）。另一方面，大多數使用者應該還是相當懂電腦的。

所以請留意情境中的線索，判斷該怎麼措辭！在預設情況下，大致給你一點概念：

- "evaluation"（評估）和 "benchmark"（基準測試）算是邊緣，但還可以
- 至於 "JSON" 和 "assertion"（斷言），要先從使用者身上看到明確的線索、確定他們知道這些是什麼，才能不加解釋地直接使用

有疑慮時，簡短解釋一下術語是可以的；如果不確定使用者懂不懂，也儘管附上簡短的定義來說明。

用使用者的語言回覆；本技能庫的使用者大多使用繁體中文或日文。

## 本技能庫的內規（House rules for this library）

*本地新增：本節以及 `metadata` 中列出的修改，變更了 Anthropic 以 Apache-2.0 授權的 skill-creator。*

這個版本只為一套技能庫服務：`.claude/skills/` 裡數十個創意指導與提示詞撰寫類的技能，主要以繁體中文使用，並會交給課程學員，而學員可能在 Claude Code、Claude.ai 或其他代理（agent）中執行它們。

1. **先確認它該不該是一個（新的）技能。** 幾乎每個工作階段都需要的規則，應該放在 `CLAUDE.md`，而不是做成技能。建立技能之前，先掃過既有技能，看看有沒有重疊：近乎重複的技能，是選錯技能的主因。優先擴充既有技能，否則就讓兩者的 description 明確區隔開來。

2. **Description 預算。** 所有技能的 description 共用同一份清單預算（在 Claude Code 中約為上下文視窗的 1%），而且 Claude Code 的內建技能也會用掉其中一部分。一旦超出，最少用到的技能會失去 description，觸發也不再可靠，所以「寫得強勢又冗長」（"pushy and long"）的做法，在這裡規模一大就撐不住：
   - 目標約 300 個字元；只有在技能有容易混淆的相鄰技能時才放寬到 500；絕不超過 1,024（Agent Skills 規格；Claude.ai 與 API 會拒收更長的）；
   - 先用一句話說明它做什麼，接著寫 "Use when …"，列出使用者實際會打的詞句（中文與英文），最後針對最容易混淆的相鄰技能，最多加上一兩條 "not for X (→ other-skill)" 的轉介；
   - 不要有角色頭銜（"Elite…"、"Chief…"），不要有流程指示，不要有 `<` 或 `>`，也不要有「冒號後接空格」（嚴格的 YAML 解析器會拒收，包括 Claude.ai 上傳；Claude Code 雖然能容忍）；
   - 改完 description 後檢查整份清單：執行 `claude -p "ok" --debug`，如果仍然超出預算，`~/.claude/debug/` 裡最新的檔案會寫出 "Skill listing over budget: N skills, X chars > Y budget"。

3. **可攜的 frontmatter。** 只使用 `name`（與資料夾名稱完全相同）、`description`、`license`、`compatibility`、`metadata` 和 `allowed-tools`；其他鍵在 Claude Code 以外都是硬性錯誤（hard error）。僅限 Claude Code 的可見度設定（`name-only`、`user-invocable-only`）要寫在設定鍵 `skillOverrides` 裡，而不是 frontmatter。

4. **捕捉使用者的知識，而非通用知識。** 技能的價值在於 Claude 推斷不出來的東西：使用者的修正、品味、失敗案例與自家格式。省略泛泛的技藝講解和通用的提示詞建議。在 2026 年的 benchmark 中，依模型的通用知識寫成的技能，表現比完全不用技能還差。

5. **規則留在 SKILL.md。** 硬性規則（禁止事項、必要格式、數值上限、輸出語言）應放在 SKILL.md 靠前的位置：分散在多個檔案中的規則容易被漏掉，而且在上下文壓縮（context compaction）之後，只有技能的前約 5,000 個 token 會被重新附上。只把查閱用資料（型錄、詞彙表、大型範例庫、變體細節）移到 `references/`，而且每份都要附上 "read this when…"（何時該讀）的指引。

6. **Gotchas（踩雷紀錄）。** 每個技能都以 `## Gotchas` 一節作結：寫下實際發生過的失敗，以及應該改怎麼做。當使用者修正某個輸出時，除了加上這條 gotcha，*還要*加一個測試案例，用它的斷言抓住這個問題，這樣之後的編輯或模型更新就無法悄悄讓問題復發。Claude 的記憶裡可能已經存有這類修正，但學員拿到的只有技能檔案。

7. **創作類技能也要測試。** 這裡的技能大多產出提示詞或腳本。它們的硬性規則（數量、禁用詞或禁用鏡頭、長度上限、格式、語言）都是很好的斷言；品味則交給審閱檢視器。所以即使是「主觀」的技能，也預設要建議測試案例。

8. **換模型後要重測。** 模型更換時，重跑 eval。如果無技能的對照組現在在某個部分已經追平技能，那個部分就不再發揮作用：提議把它刪掉。

9. **工作區不要放在 `.claude/skills/` 裡。** 把 `<skill-name>-workspace/` 放在 repo 根目錄的 `.skill-workspaces/` 底下（已設為 git 忽略），而不是放在技能旁邊，讓技能資料夾裡只有技能。

10. **每次建立或更新技能，都依這個順序收尾：** 測試通過或使用者認可 → **skill-optimizer** → **skill-translator**（寫出 `docs/SKILL_zh-TW.md`）→ 若新增了技能，或技能的用途或觸發條件有變，就更新它在 `README.md` 中的那一列（日本語與繁體中文兩張表都要）。這裡的技能都是就地編輯，所以只有在使用者要求時才打包 `.skill` 檔。

---

## 建立技能（Creating a skill）

### 掌握意圖（Capture Intent）

先理解使用者的意圖。目前的對話可能已經包含使用者想保存下來的工作流程（例如他們說 "turn this into a skill"〔把這個做成技能〕）。若是如此，先從對話紀錄中擷取答案——用了哪些工具、步驟的順序、使用者做過的修正、觀察到的輸入／輸出格式。使用者可能需要補上缺漏，並應在進入下一步之前確認。

1. 這個技能應該讓 Claude 能做到什麼？
2. 這個技能應該在什麼時候觸發？（使用者的哪些說法／情境）
3. 預期的輸出格式是什麼？
4. 要不要建立測試案例來驗證技能有效？輸出可以客觀驗證的技能（檔案轉換、資料擷取、程式碼生成、固定的工作流程步驟）能從測試案例中獲益。輸出偏主觀的技能（寫作風格、藝術）仍然有可測試的硬性規則（格式、數量、禁止事項），所以在本技能庫中，預設要建議測試案例，品味的判斷則交給檢視器（內規第 7 條）。由使用者決定。

### 訪談與研究（Interview and Research）

主動詢問邊界情況、輸入／輸出格式、範例檔案、成功標準與相依項目。等這部分都釐清之後，再開始寫測試提示詞。

檢查有哪些可用的 MCP——如果對研究有幫助（搜尋文件、尋找類似技能、查詢最佳實務），有子代理可用時就透過子代理平行研究，否則就在當前對話中直接進行。先備妥背景資訊再上場，以減輕使用者的負擔。

### 撰寫 SKILL.md（Write the SKILL.md）

根據對使用者的訪談，填寫以下組成部分：

- **name**：技能識別名稱，與資料夾名稱完全相同（小寫字母、數字、連字號）
- **description**：何時觸發、做什麼。這是主要的觸發機制——既要寫技能做什麼，**也要**寫何時使用它的具體情境。所有「何時使用」的資訊都放在這裡，不要放在本文。Claude 確實有「觸發不足」（undertrigger）的傾向（也就是在技能派得上用場時卻不使用它），但在本技能庫中，解法是寫出有辨識度的觸發詞，而不是加長篇幅：請遵循內規第 2 條。例如，與其寫 "Helps with video prompts."（協助處理影片提示詞。），不如寫 "Writes multi-shot video-generation prompts in YAML with audio tracks. Use when the user asks for 動態提示詞, 影片提示詞 or a video prompt from reference images. Not for text-to-video prose scripts (→ prompt-master-text-to-video)."（意思是：以 YAML 撰寫含音軌的多鏡頭影片生成提示詞；在使用者要求動態提示詞、影片提示詞，或依參考圖要一份影片提示詞時使用；不適用於文生影的散文腳本〔→ prompt-master-text-to-video〕。）
- **compatibility**：所需工具、相依項目（選填，很少需要）
- **技能的其餘部分 :)**

### 技能撰寫指南（Skill Writing Guide）

#### 技能的結構（Anatomy of a Skill）

```
skill-name/
├── SKILL.md（必備）
│   ├── YAML frontmatter（name、description 為必填）
│   └── Markdown 指示（以 ## Gotchas 作結）
├── 隨附資源（選用）
│   ├── scripts/    - 可執行的程式碼，用於確定性／重複性的任務
│   ├── references/ - 視需要載入上下文的文件
│   └── assets/     - 用於輸出的檔案（範本、圖示、字型）
├── evals/          - 測試案例（見下方「測試案例」）
└── docs/           - 給人閱讀的 zh-TW 版本，由 skill-translator 撰寫；SKILL.md 絕不引用
```

#### Progressive Disclosure（漸進式揭露）

技能採用三層載入系統：
1. **Metadata**（name + description）——一律在上下文中（約 100 個單字）
2. **SKILL.md 本文**——技能觸發時就會進入上下文（理想上 <500 行）
3. **隨附資源**——視需要載入（沒有上限，腳本不必載入就能執行）

這些字數都是概略值，需要的話可以放心寫得更長。

**關鍵模式：**
- SKILL.md 保持在 500 行以內；接近這個上限時，多加一層階層結構，並清楚指引使用技能的模型接下來該去哪裡繼續。
- 在 SKILL.md 中清楚引用參考檔案，並說明何時該讀它們
- 大型參考檔案（>300 行）要附上目錄
- 拆出去的是查閱用資料，不是規則（內規第 5 條）

**按領域組織**：當技能支援多個領域／框架時，依變體來組織：
```
cloud-deploy/
├── SKILL.md（工作流程 + 選擇）
└── references/
    ├── aws.md
    ├── gcp.md
    └── azure.md
```
Claude 只會讀取相關的那份參考檔案。

#### 不出人意料原則（Principle of Lack of Surprise）

這點不必多說，但技能不得包含惡意軟體、漏洞利用程式碼，或任何可能危害系統安全的內容。技能的內容若被描述出來，其意圖不應讓使用者感到意外。不要配合那些要求建立誤導性技能，或專為協助未授權存取、資料外洩或其他惡意活動而設計之技能的請求。不過像 "roleplay as an XYZ"（扮演某某角色）這類是可以的。

#### 寫作模式（Writing Patterns）

指示中優先使用祈使句。

**定義輸出格式**——可以這樣寫：
```markdown
## Report structure
ALWAYS use this exact template:
# [Title]
## Executive summary
## Key findings
## Recommendations
```

**範例模式**——附上範例很有用。可以用這樣的格式（不過如果範例本身就含有 "Input" 和 "Output"，你可能要稍微變通一下）：
```markdown
## Commit message format
**Example 1:**
Input: Added user authentication with JWT tokens
Output: feat(auth): implement JWT-based authentication
```

**Gotchas 模式**——在本文結尾列出實際發生過的失敗（內規第 6 條）：
```markdown
## Gotchas
- "single-breasted" in an image prompt trips the safety filter (HTTP 400): write "a single row of buttons".
```

### 寫作風格（Writing Style）

試著向模型解釋事情為什麼重要，而不是堆砌強硬又陳腐的 MUST。運用心智理論（theory of mind），讓技能保有通用性，而不是極度侷限於特定範例。先寫出草稿，再用全新的眼光審視、改進它。

### 測試案例（Test Cases）

寫完技能草稿後，想出 2–3 個貼近真實的測試提示詞——就是真實使用者實際會說的那種話。在本技能庫中，至少要有一個是根據過去的某次修正而來（內規第 6 條）。把它們分享給使用者：〔不必一字不差照用這段話〕「以下是我想試的幾個測試案例。這些看起來對嗎？還是你想再多加幾個？」然後執行它們。

把每個測試案例各自存成技能目錄中 `evals/` 底下的一個資料夾。先不要寫斷言——只寫提示詞就好。斷言會在下一步、趁執行還在進行時再擬。

```
my-skill/
├── SKILL.md
└── evals/
    └── flags-negative-quantity/   # 案例名稱：小寫加連字號，要說明測的是什麼
        ├── prompt.md              # 先寫執行設定，再寫使用者的任務提示詞
        ├── case.yaml              # 名稱，以及好的結果長什麼樣子
        ├── graders/               # 每條斷言一個檔案；步驟 2 之前先放佔位檔
        └── files/                 # 輸入檔案，只在測試需要時才放
```

寫第一個之前，先讀 `references/schemas.md` 的 "Test cases" 一節並照抄其中的範本，因為格式很嚴格。這些都是你自己寫、自己讀的純文字檔，所以在任何地方運作方式都一樣，不需要額外工具。這個目錄結構正是 `claude plugin eval` 讀取的格式，所以有 Claude Code 的使用者之後可以在終端機或 CI 中執行完全相同的測試。

**如果技能已經有 `evals/evals.json`**（舊格式），其中的測試仍然算數：把它們和案例資料夾合在一起，當成同一組來執行。這個檔案屬於使用者，所以除非他們要求，絕不要編輯、轉換或刪除它；任何新增或修改的內容都放進案例資料夾。`references/schemas.md` 的 "evals.json" 一節說明了這兩組測試如何合併。

## 執行與評估測試案例（Running and evaluating test cases）

本節是一整段連續的流程——不要中途停下。**不要**使用 `/skill-test` 或任何其他測試用技能。

把結果放在 `<skill-name>-workspace/`；在本 repo 中，這個資料夾要放在 repo 根目錄的 `.skill-workspaces/` 底下（內規第 9 條）。在工作區內，依迭代整理結果（`iteration-1/`、`iteration-2/` 等），而在每個迭代目錄中，每個測試案例各有一個以案例名稱命名的目錄。每一輪迭代都要沿用相同的目錄名稱，因為檢視器是依據這個路徑，把一次執行和它先前的輸出與回饋對應起來。不要一開始就把這些全部建好——邊做邊建目錄就好。

```
<skill-name>-workspace/
└── iteration-1/
    ├── flags-negative-quantity/  # 每個測試案例一個目錄
    │   ├── eval_metadata.json    # 檢視器從這裡取得提示詞
    │   ├── with_skill/           # 一種組態；只跑一次時，它同時也是執行目錄
    │   │   ├── outputs/          # 該次執行產出的檔案
    │   │   ├── grading.json
    │   │   └── timing.json
    │   └── without_skill/        # 對照組（或 old_skill/），內含同樣的項目
    ├── handles-empty-file/
    ├── benchmark.json
    └── benchmark.md
```

請遵守這個目錄結構，因為檢視器和彙整腳本都會讀取它。執行目錄（run directory）是指存放某次執行之 `outputs/`、`grading.json` 與 `timing.json` 的那個目錄。如果某個組態（configuration）跑了不只一次，就在其中為每次執行各建一個目錄（`with_skill/run-1/`、`with_skill/run-2/`……）；`eval_metadata.json` 則留在原處。

### 步驟 1：在同一回合啟動所有執行（有技能組與對照組，兩者都要）

針對每個測試案例，在同一回合中啟動兩個子代理——一個有技能，一個沒有。這點很重要：不要先啟動有技能的執行，之後才回頭補對照組。一次全部啟動，讓它們大約同時完成。

**有技能的執行（With-skill run）：**

```
Execute this task:
- Skill path: <path-to-skill>
- Task: <eval prompt>
- Input files: <full paths of the test's input files, or "none">
- Save outputs to: <workspace>/iteration-<N>/<case-name>/with_skill/outputs/
- Outputs to save: <what the user cares about — e.g., "the .docx file", "the final CSV">
```

**對照組執行（Baseline run）**（提示詞相同，但對照組是什麼要看情境）：
- **建立新技能時**：完全不用技能。相同提示詞、不給技能路徑，存到 `without_skill/outputs/`。
- **改進既有技能時**：用舊版本。編輯之前先替技能建立快照（`cp -r <skill-path> <workspace>/skill-snapshot/`），然後讓對照組子代理指向這份快照。存到 `old_skill/outputs/`。

為每個測試案例寫一份 `eval_metadata.json`（斷言暫時可以留空），直接放在該測試案例的目錄中，與 `with_skill/` 並列。檢視器和 benchmark 從不查看技能的 `evals/` 資料夾：它們是從這個檔案取得提示詞的，少了它，檢視器會顯示 "(No prompt found)"（找不到提示詞）。每一輪迭代的每個測試案例都要重新寫一份——不要以為它會從先前的迭代延續過來。

```json
{
  "eval_name": "flags-negative-quantity",
  "prompt": "The user's task prompt",
  "assertions": []
}
```

`eval_name` 是案例名稱，`prompt` 是該測試去掉設定區塊後的提示詞，`assertions` 則列出它的斷言（絕不包含佔位評分檔）。

### 步驟 2：趁執行進行中，擬定斷言

不要只是乾等執行結束——這段時間可以好好利用。為每個測試案例擬定量化斷言，並向使用者說明。如果某個測試已經有斷言（它的 `graders/` 資料夾中佔位檔以外的檔案，或舊版 `evals/evals.json` 中的 `expectations` / `assertions`），就檢視它們，並說明它們檢查的是什麼。

好的斷言可以客觀驗證，名稱也具描述性——在 benchmark 檢視器中要清楚易讀，讓人瞄一眼結果就馬上知道每條斷言檢查什麼。主觀性的技能（寫作風格、設計品質）比較適合質性評估——不要把斷言硬套在需要人類判斷的事情上。

擬好之後，把每條斷言各存成該案例 `graders/` 資料夾中的一個檔案，刪除佔位檔，並把同樣的句子放進該測試 `eval_metadata.json` 的 `assertions` 清單。每條斷言都要針對結果本身來措辭（"summary.md states a total revenue of 693.5"，即「summary.md 寫明總營收為 693.5」），而不是針對本工作流程把結果存在哪裡（"…in the outputs folder"，即「……在 outputs 資料夾中」），這樣它在 `claude plugin eval` 底下也同樣成立。

對於要交給人類判斷的測試，保留佔位檔。它存在只是為了讓 `claude plugin eval` 能載入這個案例，所以在這裡不會被評分。

也要向使用者說明他們會在檢視器中看到什麼——包括質性的輸出與量化的 benchmark。

### 步驟 3：每完成一個執行，就記錄計時資料

每個子代理任務完成時，你會收到一則包含 `total_tokens` 與 `duration_ms` 的通知。立刻把這些資料存到執行目錄中的 `timing.json`：

```json
{
  "total_tokens": 84852,
  "duration_ms": 23332,
  "total_duration_seconds": 23.3
}
```

這是記錄這些資料的唯一機會——它只透過任務通知傳來，不會保存在其他地方。每則通知一到就處理，不要想著累積起來批次處理。

### 步驟 4：評分、彙整，並啟動檢視器

所有執行都完成後：

1. **為每次執行評分**——啟動一個評分子代理（或直接在當前對話中評分），讓它讀 `agents/grader.md`，並對照輸出逐條評估每個斷言。把結果存到各執行目錄中的 `grading.json`。grading.json 的 expectations 陣列必須使用 `text`、`passed` 和 `evidence` 這三個欄位（而不是 `name`/`met`/`details` 或其他變體）——檢視器依賴的正是這些確切的欄位名稱。對於可以用程式檢查的斷言，就寫一支腳本來執行，而不是用肉眼判斷——腳本更快、更可靠，而且可以在各輪迭代中重複使用。

2. **彙整成 benchmark**——在 skill-creator 目錄下執行彙整腳本：
   ```bash
   python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>
   ```
   這會產生 `benchmark.json` 和 `benchmark.md`，列出每個組態的 pass_rate、時間與 token 數，附上平均值 ± 標準差以及差值（delta）。如果要手動產生 benchmark.json，請參閱 `references/schemas.md` 中檢視器所預期的確切 schema。
每個 with_skill 版本都要排在對應的對照組之前。

3. **做一輪分析**——閱讀 benchmark 資料，找出彙總統計可能掩蓋的模式。該注意哪些事，請見 `agents/analyzer.md`（"Analyzing Benchmark Results" 一節）——例如不論有沒有技能都一律通過的斷言（不具鑑別力）、變異很大的 eval（可能不穩定），以及時間／token 之間的取捨。把你的觀察加進 `benchmark.json` 的 `notes` 清單，接在腳本已寫入的任何備註之後；不要取代那些備註。

4. **啟動檢視器**，同時呈現質性輸出與量化資料：
   ```bash
   nohup python <skill-creator-path>/eval-viewer/generate_review.py \
     <workspace>/iteration-N \
     --skill-name "my-skill" \
     --benchmark <workspace>/iteration-N/benchmark.json \
     > /dev/null 2>&1 &
   VIEWER_PID=$!
   ```
   從第 2 輪迭代起，還要加上 `--previous-workspace <workspace>/iteration-<N-1>`。

   **Cowork／無頭（headless）環境：** 如果無法使用 `webbrowser.open()`，或環境沒有顯示器，就改用 `--static <output_path>` 寫出一個獨立的 HTML 檔，而不是啟動伺服器。使用者點下 "Submit All Reviews"（送出所有審閱）時，回饋會被下載成一個 `feedback.json` 檔。下載後，把 `feedback.json` 複製到工作區目錄，讓下一輪迭代取用。

注意：請用 generate_review.py 建立檢視器；不需要自己寫客製化的 HTML。

5. **告訴使用者**，大致像這樣：「我已經在你的瀏覽器中打開結果了。共有兩個分頁——'Outputs' 可以逐一點閱每個測試案例並留下回饋，'Benchmark' 則顯示量化比較。看完之後，回到這裡告訴我一聲。」

### 使用者在檢視器中會看到什麼（What the user sees in the viewer）

"Outputs" 分頁一次顯示一個測試案例：
- **Prompt**（提示詞）：給定的任務
- **Output**（輸出）：技能產出的檔案，能內嵌顯示的就直接內嵌顯示
- **Previous Output**（先前輸出，第 2 輪迭代起）：摺疊區塊，顯示上一輪迭代的輸出
- **Formal Grades**（正式評分，有執行評分時）：摺疊區塊，顯示各斷言通過／未通過
- **Feedback**（回饋）：一個會在輸入時自動儲存的文字框
- **Previous Feedback**（先前回饋，第 2 輪迭代起）：使用者上一次的意見，顯示在文字框下方

"Benchmark" 分頁顯示統計摘要：每個組態的通過率、耗時與 token 用量，並附上逐項 eval 的細目與分析觀察。

可用上一個／下一個按鈕或方向鍵切換。看完後，使用者點 "Submit All Reviews"，所有回饋就會存進 `feedback.json`。

### 步驟 5：讀取回饋

使用者告訴你他們看完後，讀取 `feedback.json`：

```json
{
  "reviews": [
    {"run_id": "flags-negative-quantity-with_skill", "feedback": "the chart is missing axis labels", "timestamp": "..."},
    {"run_id": "handles-empty-file-with_skill", "feedback": "", "timestamp": "..."},
    {"run_id": "csv-summary-2-with_skill", "feedback": "perfect, love this", "timestamp": "..."}
  ],
  "status": "complete"
}
```

回饋留空代表使用者覺得沒問題。把改進重點放在使用者有具體意見的測試案例上。

用完檢視器伺服器後，把它關掉：

```bash
kill $VIEWER_PID 2>/dev/null
```

---

## 改進技能（Improving the skill）

這是整個循環的核心。你已經跑完測試案例，使用者也審閱了結果，現在你需要根據他們的回饋讓技能變得更好。

### 如何思考改進（How to think about improvements）

1. **從回饋中歸納通則。** 從大局來看，這裡真正在做的事，是打造能在各式各樣的提示詞中被使用上百萬次（也許真的是字面上的一百萬次，搞不好更多，誰知道呢）的技能。你和使用者在這裡只拿少數幾個範例反覆迭代，是因為這樣推進得比較快。使用者對這些範例瞭若指掌，評估新的輸出也很快。但如果你和使用者共同開發的技能只對這幾個範例有效，那它就毫無用處。遇到頑固的問題時，與其加入瑣碎、過度擬合（overfit）的修改，或令人窒息的嚴苛 MUST，不如試著另闢蹊徑，換個比喻，或推薦不同的工作模式。嘗試的成本相對低，說不定就會找到很棒的做法。

2. **讓提示詞保持精簡。** 刪掉沒有發揮作用的內容。務必閱讀執行紀錄（transcript），而不只是最終輸出——如果看起來技能讓模型浪費大量時間做沒有生產力的事，可以試著拿掉技能中導致這種行為的部分，看看會發生什麼事。

3. **解釋原因。** 盡力解釋你要求模型做的每件事背後的**原因**。現今的 LLM 很*聰明*。它們有良好的心智理論，在好的執行框架（harness）下，能超越死板的指示，真正把事情做成。即使使用者的回饋很簡短或帶著挫折感，也要試著真正理解任務、理解使用者為什麼會這樣寫、他們實際上寫了什麼，再把這份理解轉化到指示中。如果你發現自己用全大寫寫下 ALWAYS 或 NEVER，或使用極度僵硬的結構，那就是黃燈警訊——可以的話，換個說法，解釋背後的理由，讓模型理解你要求的事情為什麼重要。這是更人性化、更強大，也更有效的做法。

4. **找出各測試案例之間的重複工作。** 閱讀測試執行的紀錄，留意子代理是否都各自寫了類似的輔助腳本，或對某件事採取了相同的多步驟做法。如果 3 個測試案例都讓子代理寫了一支 `create_docx.py` 或 `build_chart.py`，這就是強烈的訊號，表示技能應該內附那支腳本。寫一次，放進 `scripts/`，並告訴技能要使用它。這樣以後每次呼叫都不必重新發明輪子。

這項任務相當重要（我們在這裡可是想創造每年數十億的經濟價值！），而你的思考時間並不是瓶頸；慢慢來，好好反覆推敲。我建議先寫出一版修訂草稿，再用全新的眼光審視並改進。盡全力揣摩使用者的想法，理解他們想要什麼、需要什麼。

### 迭代循環（The iteration loop）

改進技能之後：

1. 把你的改進套用到技能上
2. 把所有測試案例重跑一遍，結果放進新的 `iteration-<N+1>/` 目錄，對照組也要跑。如果你在建立新技能，對照組一律是 `without_skill`（無技能）——這在各輪迭代間都不變。如果你在改進既有技能，就自行判斷用什麼當對照組比較合理：使用者一開始帶來的原始版本，或上一輪迭代。
3. 啟動審閱檢視器，並以 `--previous-workspace` 指向上一輪迭代
4. 等使用者審閱完並告訴你他們看完了
5. 讀取新的回饋，再次改進，如此重複

持續進行，直到：
- 使用者表示滿意
- 回饋全部留空（一切看起來都很好）
- 你已經無法取得有意義的進展

---

## 進階：盲測比較（Advanced: Blind comparison）

當你想更嚴謹地比較技能的兩個版本時（例如使用者問 "is the new version actually better?"〔新版真的比較好嗎？〕），可以使用盲測比較系統。細節請讀 `agents/comparator.md` 和 `agents/analyzer.md`。基本概念是：把兩份輸出交給一個獨立的代理，不告訴它哪份是哪份，讓它評判品質。然後分析勝出的一方為什麼勝出。

這是選用功能，需要子代理，而且大多數使用者用不到。通常人類審閱的循環就已足夠。

---

## Description 最佳化（Description Optimization）

SKILL.md frontmatter 中的 description 欄位，是決定 Claude 是否呼叫某個技能的主要機制。建立或改進技能之後，主動提議最佳化 description，以提升觸發準確度。

使用者同意後，讀取 `references/description-optimization.md` 並照著做：先準備約 20 個貼近真實的「應觸發／不應觸發」查詢交給使用者審閱，再執行 `scripts/run_loop.py`——它會測試 description、提出改寫版本，並依保留集（held-out）分數挑出最好的一版。這需要 `claude` CLI。在本 repo 中，直接跑的觸發測試讀數會接近 0%，原因是真正的技能早已安裝，而且平行執行的多個 worker（工作程序）會互相競爭；那份參考文件說明了避開這個問題的沙盒（sandbox）與單一 worker 設定。

請記住，Claude 只會在遇到自己無法輕鬆處理的任務時才去參考技能，所以觸發查詢（以及測試提示詞）應該是有一定份量的任務，而不是一步就能完成的請求。

---

### 打包與呈現（Package and Present；僅在有檔案傳遞工具時）

這裡的技能是就地編輯的，所以只有在使用者要求 `.skill` 檔時才做這一步（內規第 10 條）。

檢查你是否能使用向使用者呈現檔案的工具——`present_files`，或 Cowork remote 中的 `SendUserFile`。兩者都沒有就跳過這一步。如果有，就打包技能，並用該工具把產生的 `.skill` 檔傳給使用者：

```bash
python -m scripts.package_skill <path/to/skill-folder>
```

如果使用者所屬的組織允許建立技能，呈現出來的 `.skill`（或單獨的 `SKILL.md`）檔案卡片上會出現 **Save skill**（儲存技能）按鈕；點下去就會把技能安裝到使用者的個人檔案（profile）中。

---

## 其他環境（Other environments）

不是在 Claude Code 裡？在 Claude.ai、Cowork，或沒有子代理也沒有 `claude` CLI 的代理中（例如 Antigravity，它的工作區技能放在 `.agent/skills/`），有好幾個步驟會不同。執行任何測試之前，先讀 `references/other-environments.md`。

---

## 參考檔案（Reference files）

agents/ 目錄包含給專門子代理的指示。需要啟動相關子代理時再讀。

- `agents/grader.md`——如何對照輸出評估斷言
- `agents/comparator.md`——如何對兩份輸出進行盲測 A/B 比較
- `agents/analyzer.md`——如何分析某個版本為何勝過另一個

references/ 目錄有其他補充文件：
- `references/schemas.md`——檔案格式：測試案例資料夾、舊版 evals.json、grading.json 等
- `references/description-optimization.md`——觸發調校的流程，包括用於已安裝技能的沙盒
- `references/other-environments.md`——Claude.ai、Cowork，以及沒有子代理或 `claude` CLI 的代理

---

## Gotchas（踩雷紀錄）

- **技能一再犯下 SKILL.md 明令禁止的錯誤時，往往是別處還留著相反的建議。** shot-script-director 禁止空鏡（呼吸鏡），但它的某份參考文件卻仍建議切到一個空房間。修正反覆出現的錯誤時，在加重強調之前，先搜尋整個技能資料夾（包括參考文件與範例），找出任何與該規則牴觸的內容。
- **觸發測試讀數為 0% 時，通常是測試本身的問題，而不是 description 的問題。** 先檢查沙盒和 `--num-workers 1`（`references/description-optimization.md`）。直接跑的測試還可能在 repo 裡留下一個空的 `.claude/commands/` 資料夾；把它刪掉。
- 只安裝了桌面版 App 時，**`claude` 可能不在 PATH 上**；請見 `references/description-optimization.md` 中關於 CLI 的說明。

---

為了強調，這裡再重複一次核心循環：

- 弄清楚這個技能是關於什麼
- 起草或編輯技能
- 讓能使用該技能的 Claude 跑測試提示詞
- 與使用者一起評估輸出：
  - 建立 benchmark.json，並執行 `eval-viewer/generate_review.py` 協助使用者審閱
  - 執行量化 eval
- 重複，直到你和使用者都滿意為止
- 收尾時先跑 skill-optimizer，再跑 skill-translator，必要時再更新 README 的對應列（內規第 10 條）
- 只有在使用者要求時才打包 `.skill` 檔

如果你有 TodoList 這類東西，請把這些步驟加進去，以免忘記。如果你在 Cowork 中，請特別把 "Create test cases and run `eval-viewer/generate_review.py` so human can review them"（建立測試案例並執行 `eval-viewer/generate_review.py`，讓人類可以審閱）放進你的 TodoList，確保這件事一定會做到。

祝好運！
