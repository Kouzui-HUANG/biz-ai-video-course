---
name: skill-creator
description: Builds, improves and tests skills with evals (with-skill vs. baseline runs, a review viewer, benchmarks, trigger tuning). Use whenever the user wants to make a skill, change what an existing skill does, fix a mistake a skill keeps making, or write or run test cases for a skill, even without saying eval (「做一個技能」「把這個流程做成技能」「修改技能」「技能一直出錯」「改完跑測試」「幫技能做測試」). Not for slimming a SKILL.md (→ skill-optimizer) or its zh-TW docs (→ skill-translator).
license: Complete terms in LICENSE.txt
metadata:
  upstream: "Anthropic skill-creator (Apache-2.0), synced 2026-11-08"
  local-changes: "2026-11-11: house rules added; description optimization and other-environment notes moved to references/"
---

# Skill Creator

A skill for creating new skills and iteratively improving them.

At a high level, the process of creating a skill goes like this:

- Decide what you want the skill to do and roughly how it should do it
- Write a draft of the skill
- Create a few test prompts and run claude-with-access-to-the-skill on them
- Help the user evaluate the results both qualitatively and quantitatively
  - While the runs happen in the background, draft some quantitative evals if there aren't any (if there are some, you can either use as is or modify if you feel something needs to change about them). Then explain them to the user (or if they already existed, explain the ones that already exist)
  - Use the `eval-viewer/generate_review.py` script to show the user the results for them to look at, and also let them look at the quantitative metrics
- Rewrite the skill based on feedback from the user's evaluation of the results (and also if there are any glaring flaws that become apparent from the quantitative benchmarks)
- Repeat until you're satisfied
- Expand the test set and try again at larger scale

Your job when using this skill is to figure out where the user is in this process and then jump in and help them progress through these stages. So for instance, maybe they're like "I want to make a skill for X". You can help narrow down what they mean, write a draft, write the test cases, figure out how they want to evaluate, run all the prompts, and repeat.

On the other hand, maybe they already have a draft of the skill. In this case you can go straight to the eval/iterate part of the loop.

Of course, you should always be flexible and if the user is like "I don't need to run a bunch of evaluations, just vibe with me", you can do that instead.

Then after the skill is done (but again, the order is flexible), you can also run the skill description improver, which we have a whole separate script for, to optimize the triggering of the skill.

Cool? Cool.

This copy is Anthropic's skill-creator plus the **house rules** below for this library. Where the two disagree, follow the house rules: they reflect this library's size and audience.

## Communicating with the user

The skill creator is liable to be used by people across a wide range of familiarity with coding jargon. If you haven't heard (and how could you, it's only very recently that it started), there's a trend now where the power of Claude is inspiring plumbers to open up their terminals, parents and grandparents to google "how to install npm". On the other hand, the bulk of users are probably fairly computer-literate.

So please pay attention to context cues to understand how to phrase your communication! In the default case, just to give you some idea:

- "evaluation" and "benchmark" are borderline, but OK
- for "JSON" and "assertion" you want to see serious cues from the user that they know what those things are before using them without explaining them

It's OK to briefly explain terms if you're in doubt, and feel free to clarify terms with a short definition if you're unsure if the user will get it.

Reply in the user's language; this library's users mostly write Traditional Chinese or Japanese.

## House rules for this library

*Local addition: this section and the edits listed in `metadata` modify Anthropic's Apache-2.0 skill-creator.*

This copy serves one library: dozens of creative-direction and prompt-writing skills in `.claude/skills/`, used mostly in Traditional Chinese and handed to course students who may run them in Claude Code, Claude.ai or other agents.

1. **Check it should be a (new) skill.** Rules needed in nearly every session belong in `CLAUDE.md`, not a skill. Before creating a skill, scan the existing ones for overlap: near-duplicate skills are the main cause of wrong skill selection. Prefer extending the existing skill, or make the two descriptions clearly distinct.

2. **Description budget.** All skill descriptions share one listing budget (about 1% of the context window in Claude Code), and Claude Code's built-in skills use part of it. When it overflows, the least-used skills lose their descriptions and stop triggering reliably, so "pushy and long" doesn't scale here:
   - aim for about 300 characters, up to 500 only when the skill has easily confused neighbours, and never exceed 1,024 (Agent Skills spec; Claude.ai and the API reject longer);
   - one sentence on what it does, then "Use when …" with the phrases users actually type (Chinese and English), then at most one or two "not for X (→ other-skill)" redirects for the most confusable neighbours;
   - no persona titles ("Elite…", "Chief…"), no process instructions, no `<` or `>`, and no colon followed by a space (strict YAML parsers, including Claude.ai upload, reject it even though Claude Code tolerates it);
   - after changing descriptions, check the whole listing: run `claude -p "ok" --debug`, and the newest file in `~/.claude/debug/` says "Skill listing over budget: N skills, X chars > Y budget" if it still overflows.

3. **Portable frontmatter.** Use only `name` (identical to the folder name), `description`, `license`, `compatibility`, `metadata` and `allowed-tools`; other keys are hard errors outside Claude Code. Claude Code-only visibility (`name-only`, `user-invocable-only`) goes in the settings key `skillOverrides`, not in frontmatter.

4. **Capture the user's knowledge, not general knowledge.** A skill's value is what Claude can't infer: the user's corrections, taste, failure cases and house formats. Skip generic craft lectures and generic prompting advice. In 2026 benchmarks, skills written from a model's general knowledge did worse than no skill at all.

5. **Keep rules in SKILL.md.** Hard rules (forbidden items, required format, numeric limits, output language) belong in SKILL.md near the top: rules split across files get missed, and after context compaction only the first ~5,000 tokens of a skill are re-attached. Move only lookup material (catalogs, glossaries, long example banks, variant details) to `references/`, each with a "read this when…" pointer.

6. **Gotchas.** Every skill ends with a `## Gotchas` section: failures actually seen, and what to do instead. When the user corrects an output, add the gotcha *and* a test case whose assertion catches it, so a later edit or model update can't quietly bring the problem back. Claude's memory may already hold such corrections, but students only receive the skill files.

7. **Test creative skills too.** Most skills here produce prompts or scripts. Their hard rules (counts, forbidden words or shots, length limits, format, language) make good assertions; leave taste to the review viewer. So suggest test cases by default, even for "subjective" skills.

8. **Re-test after model changes.** Rerun the evals when the model changes. If the no-skill baseline now matches the skill on some part, that part no longer pulls its weight: propose removing it.

9. **Keep workspaces out of `.claude/skills/`.** Put `<skill-name>-workspace/` under `.skill-workspaces/` at the repo root (git-ignored) instead of next to the skill, so the skills folder holds only skills.

10. **Finish every create or update, in this order:** tests pass or the user signs off → **skill-optimizer** → **skill-translator** (writes `docs/SKILL_zh-TW.md`) → if a skill was added or its purpose or triggers changed, update its row in `README.md` (both the 日本語 and 繁體中文 tables). Skills are edited in place here, so package a `.skill` file only when the user asks for one.

---

## Creating a skill

### Capture Intent

Start by understanding the user's intent. The current conversation might already contain a workflow the user wants to capture (e.g., they say "turn this into a skill"). If so, extract answers from the conversation history first — the tools used, the sequence of steps, corrections the user made, input/output formats observed. The user may need to fill the gaps, and should confirm before proceeding to the next step.

1. What should this skill enable Claude to do?
2. When should this skill trigger? (what user phrases/contexts)
3. What's the expected output format?
4. Should we set up test cases to verify the skill works? Skills with objectively verifiable outputs (file transforms, data extraction, code generation, fixed workflow steps) benefit from test cases. Skills with subjective outputs (writing style, art) still have testable hard rules (format, counts, forbidden items), so in this library suggest test cases by default and leave the taste judgement to the viewer (house rule 7). Let the user decide.

### Interview and Research

Proactively ask questions about edge cases, input/output formats, example files, success criteria, and dependencies. Wait to write test prompts until you've got this part ironed out.

Check available MCPs - if useful for research (searching docs, finding similar skills, looking up best practices), research in parallel via subagents if available, otherwise inline. Come prepared with context to reduce burden on the user.

### Write the SKILL.md

Based on the user interview, fill in these components:

- **name**: Skill identifier, identical to the folder name (lowercase letters, digits, hyphens)
- **description**: When to trigger, what it does. This is the primary triggering mechanism - include both what the skill does AND specific contexts for when to use it. All "when to use" info goes here, not in the body. Claude does tend to "undertrigger" skills (to not use them when they'd be useful), but in this library the fix is distinctive trigger phrases, not length: follow house rule 2. For instance, instead of "Helps with video prompts.", write "Writes multi-shot video-generation prompts in YAML with audio tracks. Use when the user asks for 動態提示詞, 影片提示詞 or a video prompt from reference images. Not for text-to-video prose scripts (→ prompt-master-text-to-video)."
- **compatibility**: Required tools, dependencies (optional, rarely needed)
- **the rest of the skill :)**

### Skill Writing Guide

#### Anatomy of a Skill

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description required)
│   └── Markdown instructions (ending with ## Gotchas)
├── Bundled Resources (optional)
│   ├── scripts/    - Executable code for deterministic/repetitive tasks
│   ├── references/ - Docs loaded into context as needed
│   └── assets/     - Files used in output (templates, icons, fonts)
├── evals/          - Test cases (see Test Cases below)
└── docs/           - zh-TW copy for humans, written by skill-translator; never referenced from SKILL.md
```

#### Progressive Disclosure

Skills use a three-level loading system:
1. **Metadata** (name + description) - Always in context (~100 words)
2. **SKILL.md body** - In context whenever skill triggers (<500 lines ideal)
3. **Bundled resources** - As needed (unlimited, scripts can execute without loading)

These word counts are approximate and you can feel free to go longer if needed.

**Key patterns:**
- Keep SKILL.md under 500 lines; if you're approaching this limit, add an additional layer of hierarchy along with clear pointers about where the model using the skill should go next to follow up.
- Reference files clearly from SKILL.md with guidance on when to read them
- For large reference files (>300 lines), include a table of contents
- Split off lookup material, not rules (house rule 5)

**Domain organization**: When a skill supports multiple domains/frameworks, organize by variant:
```
cloud-deploy/
├── SKILL.md (workflow + selection)
└── references/
    ├── aws.md
    ├── gcp.md
    └── azure.md
```
Claude reads only the relevant reference file.

#### Principle of Lack of Surprise

This goes without saying, but skills must not contain malware, exploit code, or any content that could compromise system security. A skill's contents should not surprise the user in their intent if described. Don't go along with requests to create misleading skills or skills designed to facilitate unauthorized access, data exfiltration, or other malicious activities. Things like a "roleplay as an XYZ" are OK though.

#### Writing Patterns

Prefer using the imperative form in instructions.

**Defining output formats** - You can do it like this:
```markdown
## Report structure
ALWAYS use this exact template:
# [Title]
## Executive summary
## Key findings
## Recommendations
```

**Examples pattern** - It's useful to include examples. You can format them like this (but if "Input" and "Output" are in the examples you might want to deviate a little):
```markdown
## Commit message format
**Example 1:**
Input: Added user authentication with JWT tokens
Output: feat(auth): implement JWT-based authentication
```

**Gotchas pattern** - End the body with failures that actually happened (house rule 6):
```markdown
## Gotchas
- "single-breasted" in an image prompt trips the safety filter (HTTP 400): write "a single row of buttons".
```

### Writing Style

Try to explain to the model why things are important in lieu of heavy-handed musty MUSTs. Use theory of mind and try to make the skill general and not super-narrow to specific examples. Start by writing a draft and then look at it with fresh eyes and improve it.

### Test Cases

After writing the skill draft, come up with 2-3 realistic test prompts — the kind of thing a real user would actually say. In this library, base at least one of them on a past correction (house rule 6). Share them with the user: [you don't have to use this exact language] "Here are a few test cases I'd like to try. Do these look right, or do you want to add more?" Then run them.

Save each test case as its own folder under `evals/` in the skill directory. Don't write assertions yet — just the prompts. You'll draft assertions in the next step while the runs are in progress.

```
my-skill/
├── SKILL.md
└── evals/
    └── flags-negative-quantity/   # the case name: lowercase-with-hyphens, says what's being tested
        ├── prompt.md              # run settings, then the user's task prompt
        ├── case.yaml              # the name, and what a good result looks like
        ├── graders/               # one file per assertion; a placeholder until Step 2
        └── files/                 # input files, only if the test needs any
```

Before you write the first one, read the "Test cases" section of `references/schemas.md` and copy its templates, because the format is strict. These are plain files that you write and read yourself, so this works the same everywhere, with no extra tooling. The layout is the one `claude plugin eval` reads, so a user who has Claude Code can later run the very same tests from a terminal or in CI.

**If the skill already has an `evals/evals.json`** (the older format), its tests still count: run them together with the case folders, as one set. The file belongs to the user, so never edit, convert or delete it unless they ask; anything new or changed goes in a case folder. The "evals.json" section of `references/schemas.md` says how the two sets combine.

## Running and evaluating test cases

This section is one continuous sequence — don't stop partway through. Do NOT use `/skill-test` or any other testing skill.

Put results in `<skill-name>-workspace/`; in this repo that folder goes under `.skill-workspaces/` at the repo root (house rule 9). Within the workspace, organize results by iteration (`iteration-1/`, `iteration-2/`, etc.) and within that, each test case gets a directory with its case name. Keep the same directory names from one iteration to the next, because the viewer matches a run to its previous output and feedback by that path. Don't create all of this upfront — just create directories as you go.

```
<skill-name>-workspace/
└── iteration-1/
    ├── flags-negative-quantity/  # one directory per test case
    │   ├── eval_metadata.json    # the viewer takes the prompt from here
    │   ├── with_skill/           # a configuration; with one run, also the run directory
    │   │   ├── outputs/          # the files the run produced
    │   │   ├── grading.json
    │   │   └── timing.json
    │   └── without_skill/        # the baseline (or old_skill/), with the same contents
    ├── handles-empty-file/
    ├── benchmark.json
    └── benchmark.md
```

Keep to this layout, because the viewer and the aggregation script both read it. A run directory is the one that holds a run's `outputs/`, `grading.json` and `timing.json`. If you run a configuration more than once, give each run its own inside it (`with_skill/run-1/`, `with_skill/run-2/`, ...); `eval_metadata.json` stays where it is.

### Step 1: Spawn all runs (with-skill AND baseline) in the same turn

For each test case, spawn two subagents in the same turn — one with the skill, one without. This is important: don't spawn the with-skill runs first and then come back for baselines later. Launch everything at once so it all finishes around the same time.

**With-skill run:**

```
Execute this task:
- Skill path: <path-to-skill>
- Task: <eval prompt>
- Input files: <full paths of the test's input files, or "none">
- Save outputs to: <workspace>/iteration-<N>/<case-name>/with_skill/outputs/
- Outputs to save: <what the user cares about — e.g., "the .docx file", "the final CSV">
```

**Baseline run** (same prompt, but the baseline depends on context):
- **Creating a new skill**: no skill at all. Same prompt, no skill path, save to `without_skill/outputs/`.
- **Improving an existing skill**: the old version. Before editing, snapshot the skill (`cp -r <skill-path> <workspace>/skill-snapshot/`), then point the baseline subagent at the snapshot. Save to `old_skill/outputs/`.

Write an `eval_metadata.json` for each test case (assertions can be empty for now), directly in the test case's directory, beside `with_skill/`. The viewer and the benchmark never look inside the skill's `evals/` folder: this file is where they get the prompt from, and without it the viewer shows "(No prompt found)". Write it afresh for every test case in every iteration — don't assume it carries over from previous iterations.

```json
{
  "eval_name": "flags-negative-quantity",
  "prompt": "The user's task prompt",
  "assertions": []
}
```

`eval_name` is the case name, `prompt` is the test's prompt without the settings block, and `assertions` lists its assertions (never the placeholder grader).

### Step 2: While runs are in progress, draft assertions

Don't just wait for the runs to finish — you can use this time productively. Draft quantitative assertions for each test case and explain them to the user. If a test already has assertions (files in its `graders/` folder other than the placeholder, or `expectations` / `assertions` in an old `evals/evals.json`), review them and explain what they check.

Good assertions are objectively verifiable and have descriptive names — they should read clearly in the benchmark viewer so someone glancing at the results immediately understands what each one checks. Subjective skills (writing style, design quality) are better evaluated qualitatively — don't force assertions onto things that need human judgment.

Once drafted, save each assertion as its own file in the case's `graders/` folder, delete the placeholder, and put the same sentences in the `assertions` list of that test's `eval_metadata.json`. Word each assertion about the result itself ("summary.md states a total revenue of 693.5"), not about where this workflow saves it ("…in the outputs folder"), so that it also holds under `claude plugin eval`.

For a test you're leaving to human judgment, keep the placeholder. It is only there so that `claude plugin eval` can load the case, so it isn't graded here.

Also explain to the user what they'll see in the viewer — both the qualitative outputs and the quantitative benchmark.

### Step 3: As runs complete, capture timing data

When each subagent task completes, you receive a notification containing `total_tokens` and `duration_ms`. Save this data immediately to `timing.json` in the run directory:

```json
{
  "total_tokens": 84852,
  "duration_ms": 23332,
  "total_duration_seconds": 23.3
}
```

This is the only opportunity to capture this data — it comes through the task notification and isn't persisted elsewhere. Process each notification as it arrives rather than trying to batch them.

### Step 4: Grade, aggregate, and launch the viewer

Once all runs are done:

1. **Grade each run** — spawn a grader subagent (or grade inline) that reads `agents/grader.md` and evaluates each assertion against the outputs. Save results to `grading.json` in each run directory. The grading.json expectations array must use the fields `text`, `passed`, and `evidence` (not `name`/`met`/`details` or other variants) — the viewer depends on these exact field names. For assertions that can be checked programmatically, write and run a script rather than eyeballing it — scripts are faster, more reliable, and can be reused across iterations.

2. **Aggregate into benchmark** — run the aggregation script from the skill-creator directory:
   ```bash
   python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>
   ```
   This produces `benchmark.json` and `benchmark.md` with pass_rate, time, and tokens for each configuration, with mean ± stddev and the delta. If generating benchmark.json manually, see `references/schemas.md` for the exact schema the viewer expects.
Put each with_skill version before its baseline counterpart.

3. **Do an analyst pass** — read the benchmark data and surface patterns the aggregate stats might hide. See `agents/analyzer.md` (the "Analyzing Benchmark Results" section) for what to look for — things like assertions that always pass regardless of skill (non-discriminating), high-variance evals (possibly flaky), and time/token tradeoffs. Add your notes to the `notes` list in `benchmark.json`, after any notes the script already wrote there; don't replace those.

4. **Launch the viewer** with both qualitative outputs and quantitative data:
   ```bash
   nohup python <skill-creator-path>/eval-viewer/generate_review.py \
     <workspace>/iteration-N \
     --skill-name "my-skill" \
     --benchmark <workspace>/iteration-N/benchmark.json \
     > /dev/null 2>&1 &
   VIEWER_PID=$!
   ```
   For iteration 2+, also pass `--previous-workspace <workspace>/iteration-<N-1>`.

   **Cowork / headless environments:** If `webbrowser.open()` is not available or the environment has no display, use `--static <output_path>` to write a standalone HTML file instead of starting a server. Feedback will be downloaded as a `feedback.json` file when the user clicks "Submit All Reviews". After download, copy `feedback.json` into the workspace directory for the next iteration to pick up.

Note: please use generate_review.py to create the viewer; there's no need to write custom HTML.

5. **Tell the user** something like: "I've opened the results in your browser. There are two tabs — 'Outputs' lets you click through each test case and leave feedback, 'Benchmark' shows the quantitative comparison. When you're done, come back here and let me know."

### What the user sees in the viewer

The "Outputs" tab shows one test case at a time:
- **Prompt**: the task that was given
- **Output**: the files the skill produced, rendered inline where possible
- **Previous Output** (iteration 2+): collapsed section showing last iteration's output
- **Formal Grades** (if grading was run): collapsed section showing assertion pass/fail
- **Feedback**: a textbox that auto-saves as they type
- **Previous Feedback** (iteration 2+): their comments from last time, shown below the textbox

The "Benchmark" tab shows the stats summary: pass rates, timing, and token usage for each configuration, with per-eval breakdowns and analyst observations.

Navigation is via prev/next buttons or arrow keys. When done, they click "Submit All Reviews" which saves all feedback to `feedback.json`.

### Step 5: Read the feedback

When the user tells you they're done, read `feedback.json`:

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

Empty feedback means the user thought it was fine. Focus your improvements on the test cases where the user had specific complaints.

Kill the viewer server when you're done with it:

```bash
kill $VIEWER_PID 2>/dev/null
```

---

## Improving the skill

This is the heart of the loop. You've run the test cases, the user has reviewed the results, and now you need to make the skill better based on their feedback.

### How to think about improvements

1. **Generalize from the feedback.** The big picture thing that's happening here is that we're trying to create skills that can be used a million times (maybe literally, maybe even more who knows) across many different prompts. Here you and the user are iterating on only a few examples over and over again because it helps move faster. The user knows these examples in and out and it's quick for them to assess new outputs. But if the skill you and the user are codeveloping works only for those examples, it's useless. Rather than put in fiddly overfitty changes, or oppressively constrictive MUSTs, if there's some stubborn issue, you might try branching out and using different metaphors, or recommending different patterns of working. It's relatively cheap to try and maybe you'll land on something great.

2. **Keep the prompt lean.** Remove things that aren't pulling their weight. Make sure to read the transcripts, not just the final outputs — if it looks like the skill is making the model waste a bunch of time doing things that are unproductive, you can try getting rid of the parts of the skill that are making it do that and seeing what happens.

3. **Explain the why.** Try hard to explain the **why** behind everything you're asking the model to do. Today's LLMs are *smart*. They have good theory of mind and when given a good harness can go beyond rote instructions and really make things happen. Even if the feedback from the user is terse or frustrated, try to actually understand the task and why the user is writing what they wrote, and what they actually wrote, and then transmit this understanding into the instructions. If you find yourself writing ALWAYS or NEVER in all caps, or using super rigid structures, that's a yellow flag — if possible, reframe and explain the reasoning so that the model understands why the thing you're asking for is important. That's a more humane, powerful, and effective approach.

4. **Look for repeated work across test cases.** Read the transcripts from the test runs and notice if the subagents all independently wrote similar helper scripts or took the same multi-step approach to something. If all 3 test cases resulted in the subagent writing a `create_docx.py` or a `build_chart.py`, that's a strong signal the skill should bundle that script. Write it once, put it in `scripts/`, and tell the skill to use it. This saves every future invocation from reinventing the wheel.

This task is pretty important (we are trying to create billions a year in economic value here!) and your thinking time is not the blocker; take your time and really mull things over. I'd suggest writing a draft revision and then looking at it anew and making improvements. Really do your best to get into the head of the user and understand what they want and need.

### The iteration loop

After improving the skill:

1. Apply your improvements to the skill
2. Rerun all test cases into a new `iteration-<N+1>/` directory, including baseline runs. If you're creating a new skill, the baseline is always `without_skill` (no skill) — that stays the same across iterations. If you're improving an existing skill, use your judgment on what makes sense as the baseline: the original version the user came in with, or the previous iteration.
3. Launch the reviewer with `--previous-workspace` pointing at the previous iteration
4. Wait for the user to review and tell you they're done
5. Read the new feedback, improve again, repeat

Keep going until:
- The user says they're happy
- The feedback is all empty (everything looks good)
- You're not making meaningful progress

---

## Advanced: Blind comparison

For situations where you want a more rigorous comparison between two versions of a skill (e.g., the user asks "is the new version actually better?"), there's a blind comparison system. Read `agents/comparator.md` and `agents/analyzer.md` for the details. The basic idea is: give two outputs to an independent agent without telling it which is which, and let it judge quality. Then analyze why the winner won.

This is optional, requires subagents, and most users won't need it. The human review loop is usually sufficient.

---

## Description Optimization

The description field in SKILL.md frontmatter is the primary mechanism that determines whether Claude invokes a skill. After creating or improving a skill, offer to optimize the description for better triggering accuracy.

When the user agrees, read `references/description-optimization.md` and follow it: about 20 realistic should-trigger / should-not-trigger queries that the user reviews, then `scripts/run_loop.py`, which tests the description, proposes rewrites and picks the best one by held-out score. It needs the `claude` CLI. In this repo a naive trigger test reads near 0%, because the real skill is already installed and because parallel workers compete; the reference explains the sandbox and the one-worker setting that avoid this.

Keep in mind that Claude only consults skills for tasks it can't easily handle on its own, so trigger queries (and test prompts) should be substantive, not one-step requests.

---

### Package and Present (only if a file-delivery tool is available)

Skills here are edited in place, so do this only when the user asks for a `.skill` file (house rule 10).

Check whether you have access to a tool that presents files to the user — `present_files`, or `SendUserFile` in Cowork remote. If you have neither, skip this step. If you do, package the skill and send the user the resulting `.skill` file with that tool:

```bash
python -m scripts.package_skill <path/to/skill-folder>
```

The presented `.skill` (or bare `SKILL.md`) file card shows a **Save skill** button when the user's org allows skill creation; clicking it installs the skill into their profile.

---

## Other environments

Not in Claude Code? In Claude.ai, Cowork, or an agent without subagents or the `claude` CLI (for example Antigravity, whose workspace skills live in `.agent/skills/`), several steps change. Read `references/other-environments.md` before running any tests.

---

## Reference files

The agents/ directory contains instructions for specialized subagents. Read them when you need to spawn the relevant subagent.

- `agents/grader.md` — How to evaluate assertions against outputs
- `agents/comparator.md` — How to do blind A/B comparison between two outputs
- `agents/analyzer.md` — How to analyze why one version beat another

The references/ directory has additional documentation:
- `references/schemas.md` — File formats: test case folders, the older evals.json, grading.json, etc.
- `references/description-optimization.md` — The trigger-tuning procedure, including the sandbox for already-installed skills
- `references/other-environments.md` — Claude.ai, Cowork, and agents without subagents or the `claude` CLI

---

## Gotchas

- **A skill that keeps making a mistake its SKILL.md forbids often has the opposite advice somewhere else.** shot-script-director bans empty cutaways (呼吸鏡), yet one of its references still suggested cutting away to an empty room. When fixing a recurring mistake, search the whole skill folder, references and examples included, for anything that contradicts the rule before adding more emphasis.
- **Trigger tests that read 0% are usually a test problem, not a description problem.** Check the sandbox and `--num-workers 1` first (`references/description-optimization.md`). A naive run can also leave an empty `.claude/commands/` folder in the repo; delete it.
- **`claude` may not be on PATH** when only the desktop app is installed; see the CLI note in `references/description-optimization.md`.

---

Repeating one more time the core loop here for emphasis:

- Figure out what the skill is about
- Draft or edit the skill
- Run claude-with-access-to-the-skill on test prompts
- With the user, evaluate the outputs:
  - Create benchmark.json and run `eval-viewer/generate_review.py` to help the user review them
  - Run quantitative evals
- Repeat until you and the user are satisfied
- Finish with skill-optimizer, then skill-translator, then the README row if needed (house rule 10)
- Package a `.skill` file only if the user asks for one

Please add steps to your TodoList, if you have such a thing, to make sure you don't forget. If you're in Cowork, please specifically put "Create test cases and run `eval-viewer/generate_review.py` so human can review them" in your TodoList to make sure it happens.

Good luck!
