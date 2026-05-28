# Output Schema Reference

## YAML Structure (≤ 1300 characters total)

```yaml
project_meta:
  summary: "{{Ultra-brief concept summary}}"
  art_style: "{{Detected Visual Style}}"

subject_profile:
  visual_lock: >
    {{project_meta.art_style}} aesthetic. {{Name/Type}}, {{Age/Ethnicity}}, {{Key Outfit}}, {{Texture/Lighting}}.

multi_shot_sequence:
  shots:
    - id: 1
      type: "{{Shot Type}}"
      action_prompt: >
        {{Subject_Visual_Lock}} features. {{Action}}, {{Environment}}. {{Camera}}.
      audio_prompt: "{{Audio context}}"
    - id: 2
      type: "{{Shot Type}}"
      action_prompt: >
        {{Subject_Visual_Lock}} features. {{Action}}, {{Interaction}}. {{Camera}}.
      audio_prompt: "{{Audio context ONLY if human is present}}"
    - id: 3
      type: "{{Shot Type}}"
      action_prompt: >
        {{Subject_Visual_Lock}} features. {{Action}}. {{Lighting change}}.
      audio_prompt: "{{Audio context ONLY if human is present}}"
    - id: 4
      type: "{{Shot Type}}"
      action_prompt: >
        {{Subject_Visual_Lock}} features. {{Climactic Action}}. {{Camera}}.
      audio_prompt: "{{Audio context ONLY if human is present}}"
    - id: 5
      type: "{{Shot Type}}"
      action_prompt: >
        {{Subject_Visual_Lock}} features. {{Resolution Action}}. {{Camera}}.
      audio_prompt: "{{Audio context ONLY if human is present}}"
```

## Field Definitions

| Field | Description |
|---|---|
| `project_meta.summary` | One-line concept pitch. Maximum brevity. |
| `project_meta.art_style` | Detected/specified visual style keyword (e.g., `1990s Anime`, `Photorealistic`, `Ghibli Watercolor`). |
| `subject_profile.visual_lock` | The canonical subject description. Referenced by every shot. Uses **Keyword Stacking**: art style, name/type, age/ethnicity, outfit, texture, lighting. No prose. |
| `shots[].type` | Shot type label: `Establishing`, `Close-Up`, `Medium`, `Wide`, `POV`, `Over-the-Shoulder`, `Dutch Angle`, etc. |
| `shots[].action_prompt` | Telegraphic English. Begins with Subject Visual Lock echo. Followed by action, environment/interaction, camera movement. Omit articles (`a`, `the`) and copulas (`is`, `are`). |
| `shots[].audio_prompt` | **Required if human in shot. Omit entirely if no human.** See Audio Trigger Mechanism below. |

## Audio Trigger Mechanism

### When to Generate
* A shot containing a visible human subject → `audio_prompt` is **mandatory**.
* A shot with no human (landscape, object, abstract) → **omit** the `audio_prompt` field entirely.

### Vocalization Types
Tag the type at the start: `[Dialogue]`, `[Laughter]`, `[Crying]`, `[Whisper]`, `[Breathing]`, `[Scream]`, `[Humming]`, etc.

### Literary Protocol for Dialogue

| Category | Rule | Example |
|---|---|---|
| **Short Line** | Explosive, fragmented, reject complete sentences. Gasps between words. | `[Dialogue] 'やめろ！'` |
| **Long Line** | Philosophical depth on life, humanity, or society. No banal narration. | `[Dialogue] 'ひとはなぜ... かなしみをかかえていきるのか...'` |

### Language Rules
* **Default language**: Japanese.
* User may specify alternative target language.
* **[ABSOLUTE BAN] Japanese lines must use NO KANJI (漢字). 100% Hiragana (ひらがな) and Katakana (カタカナ) only.**

### Formatting
```
audio_prompt: "[Vocalization Type] 'Target Language Text.'"
```
Examples:
```
audio_prompt: "[Dialogue] 'やめろ！'"
audio_prompt: "[Laughter] Soft, breathy chuckle trailing into silence."
audio_prompt: "[Whisper] 'もういちど... あいたい...'"
```
