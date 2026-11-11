# skill-translator（zh-TW 人類可讀版）

> 本文件為 `SKILL.md` 的繁體中文對照翻譯，僅供人類閱讀；AI 執行時不會載入本檔。
> 原檔最後更新：2026-11-11。內容若有出入，以 `SKILL.md` 為準。

## Frontmatter 說明

- **name**：`skill-translator`
- **description（觸發條件）**：在技能的 docs/ 資料夾中，撰寫或更新該技能 SKILL.md（應要求時也包括其參考檔）的人類可讀繁體中文（zh-TW）版本，且這份版本不會進入 AI 執行時的上下文。當使用者要求翻譯技能或更新其中文說明文件時使用（「翻譯技能」「技能中文版」「更新中文說明」「SKILL_zh-TW」），也作為 skill-optimizer 之後的最後一步。不用於翻譯提示詞或其他文字。

---

# 技能翻譯器 Skill Translator（zh-TW）

AI 讀的是 `SKILL.md`；人（使用者與課程學員）讀的是 `docs/SKILL_zh-TW.md`。讓兩者說的是同一件事，而譯文永遠不進入 AI 的上下文。

## 規則

1. **絕不指向 `docs/`**——無論是從 SKILL.md 還是任何 `references/` 檔案。Claude 會讀取 SKILL.md 指向的內容，所以只要有一個連結，就會以第二種語言把同一套指示再載入一次，而過時的譯文還可能與原文互相矛盾。
2. **只翻譯，不修改。** 不要增加、刪減或「改進」任何東西：譯本必須呈現技能實際上做什麼。保留 Markdown 結構。以下內容保留原文、一字不改：程式碼、檔案路徑、frontmatter 鍵名、觸發詞、提示詞範本，以及引號中的使用者用語，因為使用者和工具比對的正是這些一字不差的字串。
3. **用語：** 使用台灣慣用的繁體中文。業界習慣用英文的術語就保留英文（Frontmatter、Progressive Disclosure、eval、few-shot），若有助於理解，第一次出現時附上簡短的中文說明。
4. **標示原檔日期**，讓過時的譯本一眼就能看出來（格式見下）。

## 檔案格式

存成 `<skill-dir>/docs/SKILL_zh-TW.md`；翻譯的參考檔則存成 `docs/<NAME>_zh-TW.md`。檔案開頭寫成這樣：

```markdown
# <skill-name>（zh-TW 人類可讀版）

> 本文件為 `SKILL.md` 的繁體中文對照翻譯，僅供人類閱讀；AI 執行時不會載入本檔。
> 原檔最後更新：YYYY-MM-DD。內容若有出入，以 `SKILL.md` 為準。

## Frontmatter 說明

- **name**：`<skill-name>`
- **description（觸發條件）**：<translated description>
```

接著翻譯本文。日期取自 `git log -1 --format=%cs -- <skill-dir>/SKILL.md`；若檔案有尚未提交（commit）的變更，則改用檔案的修改日期。

## 工作流程

1. 讀取目標 `SKILL.md`，以及使用者要求的任何 `references/*.md`。
2. 依照規則翻譯，並把檔案寫進 `docs/`。
3. 確認 SKILL.md 與參考檔仍然沒有連結到、也沒有提到 `docs/`。
4. **同步模式**（被要求更新所有譯文時）：對每個有 `docs/SKILL_zh-TW.md` 的技能，把它檔頭中的日期（或檔案日期）與 SKILL.md 的最後一次變更相比，重新翻譯過時的那些。回報你更新了哪些。

## Gotchas（常見陷阱）

- 「翻譯這段提示詞」講的是提示詞文字，不是技能：這不是本技能的工作。
- 本身已經是中文的參考檔不需要另做譯本；改在檔頭註明即可。
