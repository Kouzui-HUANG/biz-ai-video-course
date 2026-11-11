---
name: skill-translator
description: Writes or refreshes the human-readable Traditional Chinese (zh-TW) copy of a skill's SKILL.md (and its references on request) in the skill's docs/ folder, kept out of the AI's runtime context. Use when the user asks to translate a skill or update its Chinese docs (「翻譯技能」「技能中文版」「更新中文說明」「SKILL_zh-TW」), and as the last step after skill-optimizer. Not for translating prompts or other text.
---

# Skill Translator (zh-TW)

The AI reads `SKILL.md`; people (the user and course students) read `docs/SKILL_zh-TW.md`. Keep the two saying the same thing, without the translation ever entering the AI's context.

## Rules

1. **Never point to `docs/`** from SKILL.md or any `references/` file. Claude reads what SKILL.md points to, so a single link would load the same instructions twice in a second language, and a stale translation could contradict the original.
2. **Translate, don't edit.** Don't add, drop or "improve" anything: the copy has to show what the skill actually does. Keep the Markdown structure. Keep verbatim: code, file paths, frontmatter keys, trigger phrases, prompt templates and quoted user phrases, because users and tools match on those exact strings.
3. **Wording:** Traditional Chinese as used in Taiwan. Keep industry terms in English where that's normal (Frontmatter, Progressive Disclosure, eval, few-shot), with a short Chinese gloss the first time if it helps.
4. **Show the source date** so a stale copy is easy to spot (format below).

## File format

Save `<skill-dir>/docs/SKILL_zh-TW.md`; a translated reference goes to `docs/<NAME>_zh-TW.md`. Start the file like this:

```markdown
# <skill-name>（zh-TW 人類可讀版）

> 本文件為 `SKILL.md` 的繁體中文對照翻譯，僅供人類閱讀；AI 執行時不會載入本檔。
> 原檔最後更新：YYYY-MM-DD。內容若有出入，以 `SKILL.md` 為準。

## Frontmatter 說明

- **name**：`<skill-name>`
- **description（觸發條件）**：<translated description>
```

Then translate the body. Take the date from `git log -1 --format=%cs -- <skill-dir>/SKILL.md`, or from the file's modification date when it has uncommitted changes.

## Workflow

1. Read the target `SKILL.md`, plus any `references/*.md` the user asked for.
2. Translate following the rules, and write the file(s) in `docs/`.
3. Check that SKILL.md and the references still contain no link to, or mention of, `docs/`.
4. **Sync mode** (when asked to update all translations): for each skill with a `docs/SKILL_zh-TW.md`, compare the date in its header (or the file dates) with SKILL.md's last change, and re-translate the stale ones. Report which ones you updated.

## Gotchas

- 「翻譯這段提示詞」 is about prompt text, not a skill: it isn't this skill's job.
- References that are already in Chinese don't need a copy; note that in the header instead.
