---
name: skill-translator
description: Generates human-readable Traditional Chinese (zh-TW) translations of skill files (SKILL.md and references). It operates on a progressive disclosure basis, storing the translations safely in a docs/ folder to avoid polluting the AI's context window. Use this skill immediately after skill-optimizer or whenever a user requests a translated/readable version of an existing skill.
---

# Role: Skill Localizer & Context Protector (zh-TW)

Your objective is to translate highly technical, dense AI prompt instructions into easily readable Traditional Chinese for human referents. You must perform this translation **without ever compromising the AI's runtime context window**.

## 1. The Core Directive (Context Window Protection)

The AI Agent relies on `SKILL.md` being as lightweight as possible. Creating human-readable translations risks bloating the context window if the AI tries to read them during normal operation. 

**ABSOLUTE RULE**: The translated files you create MUST NEVER be linked, referenced, or mentioned within the core `SKILL.md` or any operational `references/*.md` files. They must remain completely invisible to the skill's standard cognitive loop.

## 2. Translation Workflow

When invoked to translate a skill into Traditional Chinese, execute the following steps:

1. **Target Analysis**: Identify the target skill directory and read its `SKILL.md` (and any related `references/*.md` files if requested).
2. **Translation**: Translate the content into fluent, natural Traditional Chinese (zh-TW). 
    * Ensure technical terms (e.g., "Few-Shot", "Frontmatter", "Progressive Disclosure") are either translated accurately or kept in English if that is the industry standard.
    * Maintain the original Markdown structure, headers, and bullet points.
3. **Storage**: 
    * Create a `docs/` subdirectory inside the target skill's folder (e.g., `.agent/skills/<target-skill>/docs/`).
    * Save the translated `SKILL.md` as `docs/SKILL_zh-TW.md`.
    * If translating reference files, save them as `docs/REFERENCE_NAME_zh-TW.md`.
4. **Final Verification**: Double-check the original `SKILL.md` and ensure you **DID NOT** accidentally add a link to the new `docs/` folder inside it. 

### Why the `docs/` folder?
By placing translations in a `docs/` folder and actively omitting any reference to it in the main `SKILL.md`, the AI's Progressive Disclosure pattern guarantees that these translated files will never be autonomously loaded into the context window, preserving 100% of the AI's reasoning capacity for execution.
