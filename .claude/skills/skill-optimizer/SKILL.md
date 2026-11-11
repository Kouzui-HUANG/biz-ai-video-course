---
name: skill-optimizer
description: Slims and restructures an existing skill so it stays lean, portable and within the library's shared description budget, without losing the rules that matter. Use when the user asks to optimize, refactor, compress or restructure a SKILL.md or shorten its description (「優化技能」「精簡 SKILL.md」「重構技能」「縮短描述」「技能太長」), and as the finishing pass after skill-creator. Not for optimizing an image or video prompt.
---

# Skill Optimizer

Make a skill cheaper to carry and easier to follow, without losing anything Claude can't work out for itself. Lean is not the same as split: the goal is fewer tokens per correct result, not the fewest lines in SKILL.md.

## Why these rules

- **Descriptions are a library-wide cost.** Every description sits in the skill listing of every session, and that listing has a shared budget (about 1% of the context window in Claude Code). When it overflows, the least-used skills lose their descriptions and stop triggering reliably.
- **Rules belong where they are always read.** The whole SKILL.md loads when a skill fires, but a reference file is read only if Claude decides to open it, and after context compaction only the first ~5,000 tokens of a skill are re-attached. In a 2026 study, splitting a skill into a short root plus files helped exploratory tasks slightly and hurt constraint-heavy ones: rules spread across files get missed.
- **Moving filler doesn't remove it.** Text moved to `references/` still gets read and paid for. Delete what Claude already knows instead; exhaustive documentation gave almost no gain over compact skills in 2026 benchmarks.
- **Structure isn't proof.** How tidy a skill looks barely predicts whether it helps, so check behaviour, not just layout.

## Workflow

### Phase 0: Snapshot

Copy the skill before touching it (`cp -r <skill> <workspace>/skill-snapshot/`, with the workspace under `.skill-workspaces/` at the repo root), and note the description length and the SKILL.md line count.

### Phase A: Description

Rewrite it to the library rules, then show before and after with character counts:

1. Aim for about 300 characters, up to 500 only when the skill has easily confused neighbours; never exceed 1,024 (Agent Skills spec; Claude.ai and the API reject longer).
2. Order: what it does, in one sentence starting with a verb → "Use when …" plus the phrases users actually type (Chinese and English) → at most one or two "not for X (→ other-skill)" redirects for the most confusable neighbours.
3. Remove persona titles ("Elite…", "Chief…"), process instructions ("MUST ALWAYS…", "generates immediately"), feature lists that don't help routing, and repeated synonyms.
4. Keep every trigger phrase that real requests use. If you can't tell which ones matter, ask the user, or use the skill's trigger evals if it has them.
5. No `<` or `>` (the validator rejects them, and Claude Code shows them as `&lt;` / `&gt;`), and no colon followed by a space, which breaks strict YAML parsers such as Claude.ai upload.

### Phase B: Body — sort everything into three bins

1. **Keep in SKILL.md, near the top:** a one-line purpose, the hard rules (forbidden items, required format, numeric limits, output language), the core workflow, the output template, and the `## Gotchas` section (add one if it's missing).
2. **Move to `references/`** (one level deep; add a table of contents once a file passes 100 lines): catalogs, glossaries, style dictionaries, long example banks, variant-specific details, background needed only sometimes. In SKILL.md, add a pointer saying *when* to read each file ("When the user picks style X, read `references/x.md`").
3. **Delete:** what Claude already knows (generic craft lectures, generic prompting advice), restatements, motivational filler, persona boilerplate.

List every deletion in the change summary so the user can veto it; nothing disappears silently. Rewrite all-caps MUST/NEVER as a plain rule plus its reason, and keep emphasis only where a format or safety constraint truly needs it. There is no line target: make SKILL.md as short as its rules allow, and never longer than 500 lines.

### Phase C: Portability and hygiene

- Frontmatter has only `name` (identical to the folder name), `description`, `license`, `compatibility`, `metadata` and `allowed-tools`. Claude Code-only visibility (`name-only`, `user-invocable-only`) belongs in the settings key `skillOverrides`.
- Use tool-neutral wording ("read `references/x.md`", not "invoke view_file") and skill-relative paths, not `.agent/skills/...` or absolute user paths.
- No README, changelog or install notes inside the skill, and no API keys or tokens.
- Every file in `references/` is pointed to from SKILL.md, and every file SKILL.md points to exists. `docs/` stays unreferenced.
- Run `python3 <skill-creator>/scripts/quick_validate.py <skill>` and fix what it reports.

### Phase D: Check behaviour

- **Only the description changed:** if the skill has trigger evals, rerun them. Otherwise write down three requests that should trigger it and two near-misses that shouldn't, and check each against the new wording. Then check the whole listing size as in skill-creator's house rule 2.
- **Body content moved or deleted:** if the skill has `evals/`, run them on the snapshot and on the new version through skill-creator's loop and compare. If it has none, run two realistic prompts on both versions, compare the outputs for lost rules, and offer to save the prompts as test cases.

Then hand off to **skill-translator** so `docs/SKILL_zh-TW.md` matches the new SKILL.md.

## Output

A change summary in the user's language:
- description: characters before → after, and the new text
- SKILL.md: lines before → after
- moved: what went to which reference file
- deleted: every removed item
- checks: the validator result and the behaviour check result

## Gotchas

- 「優化這段提示詞」 or 「幫我優化圖片 prompt」 is about a prompt, not a skill: leave it to the prompt skills.
- Moving a rule such as 「不要呼吸鏡」 into `references/` hides it from every run that never opens that file. Rules stay in SKILL.md.
