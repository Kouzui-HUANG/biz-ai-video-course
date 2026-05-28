---
name: skill-optimizer
description: An advanced optimizing processor that executes after skill-creator or when a user wants to refactor an existing skill. It enforces Context Window Efficiency and the Progressive Disclosure pattern to ensure the resulting skill is lean, modular, and performant. Use this skill when requested to "optimize", "refactor", or "compress" an existing SKILL.md.
---

# Role: Skill Optimizer & Architecture Refiner

This skill provides an advanced refactoring workflow. It transforms bloated, inefficient skills into modular, high-performance agents by applying **Progressive Disclosure** and **Context Window Optimization**.

## 1. Prime Directives (The Why)

The context window is a shared and highly precious resource. Most skills are overly verbose, containing exhaustive lists, deep tutorials, and edge-case examples directly inside `SKILL.md`. This degrades the AI's core reasoning capacity and increases token costs.

Your supreme goal is to **minimize the footprint of `SKILL.md` (< 100-200 lines if possible)** while preserving 100% of the procedural knowledge by intelligently offloading it.

## 2. The Optimization Workflow (The How)

When invoked to optimize a skill, strictly follow this three-phase process:

### Phase A: Frontmatter & Routing Optimization
1. **Analyze Trigger Conditions**: Review the `description` in the YAML frontmatter.
2. **Refine Intention**: Rewrite the description so it focuses purely on *what the skill does* and *when Claude should trigger it*. Do not put "How to use" instructions here.

### Phase B: Information Extraction & Offloading (Progressive Disclosure)
Identify and extract "heavy" content from `SKILL.md` into dedicated files inside the `/references/` directory.

* **What to extract**:
    * Long enumerations (e.g., genre lists, parameter tables).
    * Exhaustive reference data (e.g., specific API endpoints, syntax dictionaries).
    * Few-Shot Examples (Input/Output text pairs).
    * Specialized sub-workflows only needed for edge cases.
* **Where to put it**:
    * Create logical files (e.g., `references/examples.md`, `references/formats.md`).
* **Critical Rule**: Zero data loss. The extracted files must contain the exact information removed from the main file.

### Phase C: `SKILL.md` Reconstruction
Rewrite the core `SKILL.md` to be a sleek "Control Hub". It should only contain:

1. **Role/Objective**: A 2-sentence summary of the skill's purpose.
2. **Core Directives/Heuristics**: The fundamental rules the AI must never break.
3. **Knowledge Hub Routing**: A clear, bulleted list pointing to the new `references/*.md` files, telling the AI *when* it should invoke `view_file` to read them.
    * *Example*: "For prompt formatting examples, refer to `references/examples.md`."
4. **Cognitive Loop (Standard Operating Procedure)**: A high-level, step-by-step checklist of how the AI should execute the task.
5. **Output Protocol**: The required format for the final response.

## 3. Execution Verification

Before finishing, verify:
* Is `SKILL.md` mostly procedural logic rather than flat data?
* Are there clear pointers telling the AI exactly which `reference/*.md` file to read under what specific conditions?
* Is the YAML frontmatter intact and accurately describing the trigger conditions?
