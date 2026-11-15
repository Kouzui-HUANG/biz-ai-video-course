# Output Schema Reference

Multi-Shot mode (default) structure. Single-Take mode (一鏡到底) uses `references/single-take-schema.md` instead; the Audio Trigger Mechanism below applies to both modes.

## Multi-Shot YAML Structure (≤ 3000 characters total)

```yaml
project_meta:
  summary: "{{Ultra-brief concept summary}}"
  art_style: "{{Detected Visual Style}}"
  bgm: "(none)"   # default; replace with music description ONLY if user specifies BGM

subject_profile:
  visual_lock: >
    {{project_meta.art_style}} aesthetic. {{Name/Type}}, {{Age/Ethnicity}}, {{Key Outfit}}, {{Texture/Lighting}}.

multi_shot_sequence:
  shots:
    - id: 1
      type: "{{Shot Type}}"
      action_prompt: >
        {{Subject_Visual_Lock}} features. {{Action}}, {{Environment}}. {{Camera}}.
      audio_prompt: "{{Non-verbal audio context}}"
    - id: 2
      type: "{{Shot Type}}"
      action_prompt: >
        {{Subject_Visual_Lock}} features. {{Action}}, {{Interaction}}. {{Camera}}.
      audio_prompt: "{{Non-verbal audio ONLY if human is present}}"
    - id: 3
      type: "{{Shot Type}}"
      action_prompt: >
        {{Subject_Visual_Lock}} features. {{Action}}. {{Lighting change}}.
      audio_prompt: "{{Non-verbal audio ONLY if human is present}}"
    - id: 4
      type: "{{Shot Type}}"
      action_prompt: >
        {{Subject_Visual_Lock}} features. {{Climactic Action}}. {{Camera}}.
      audio_prompt: "{{Non-verbal audio ONLY if human is present}}"
    - id: 5
      type: "{{Shot Type}}"
      action_prompt: >
        {{Subject_Visual_Lock}} features. {{Resolution Action}}. {{Camera}}.
      audio_prompt: "{{Non-verbal audio ONLY if human is present}}"
```

## Field Definitions

| Field | Description |
|---|---|
| `project_meta.summary` | One-line concept pitch. Maximum brevity. |
| `project_meta.art_style` | Detected/specified visual style keyword (e.g., `1990s Anime`, `Photorealistic`, `Ghibli Watercolor`). |
| `project_meta.bgm` | Background music. **Default `"(none)"`.** Only replace with a music description (genre, instrumentation, tempo, mood) when the user explicitly specifies BGM/music. |
| `subject_profile.visual_lock` | The canonical subject description. Referenced by every shot. Uses **Keyword Stacking**: art style, name/type, age/ethnicity, outfit, texture, lighting. No prose. |
| `shots[].type` | Shot type label: `Establishing`, `Close-Up`, `Medium`, `Wide`, `POV`, `Over-the-Shoulder`, `Dutch Angle`, etc. |
| `shots[].action_prompt` | Telegraphic English. Begins with Subject Visual Lock echo. Followed by action, environment/interaction, camera movement. Omit articles (`a`, `the`) and copulas (`is`, `are`). |
| `shots[].audio_prompt` | **Required if human in shot. Omit entirely if no human.** **Non-verbal by default** — dialogue appears only when the user supplied it. See Audio Trigger Mechanism below. |

## Audio Trigger Mechanism

### When to Generate
* A shot containing a visible human subject → `audio_prompt` is **mandatory**.
* A shot with no human (landscape, object, abstract) → **omit** the `audio_prompt` field entirely.
* Single-Take mode: same rule per beat — `camera_flow[].sfx` carries the synced sound; `single_take.audio_prompt` is one continuous `[Ambience]` bed.

### [DEFAULT] No Dialogue
* **Never invent spoken lines.** By default `audio_prompt` carries **non-verbal sound only**: breathing, sigh, laughter, footsteps, cloth rustle, wind, room tone.
* A `[Dialogue]` line is written **only** for lines the user supplied. If the user asks for dialogue without giving the lines, ask for them instead of writing them.
* When the user supplies dialogue: keep their wording, punctuation and language verbatim (never shorten, rephrase or translate), and assign each line to the shot it belongs to.

### Vocalization Types
Tag the type at the start: `[Breathing]`, `[Sigh]`, `[Laughter]`, `[Crying]`, `[Whisper]`, `[Scream]`, `[Humming]`, `[Footsteps]`, `[Ambience]` — and `[Dialogue]` **only for user-supplied lines**.

### Dialogue Delivery _(the words always stay exactly as the user wrote them)_

Delivery goes in the acting and sound description; it never changes the words inside `[Dialogue] '…'`.

| Category | Delivery | Example (user-supplied line, copied verbatim) |
|---|---|---|
| **Short Line** | Performed explosive and fragmented, gasps between words. | `[Dialogue] '住手！'` |
| **Long Line** | Performed slow and reflective, pauses between phrases. | `[Dialogue] '人為什麼……要抱著悲傷活下去……'` |

### Language Rules
* Dialogue uses **the language the user wrote it in**. There is no default dialogue language, because there is no default dialogue.
* Japanese lines keep the user's script: kanji stay as written; convert to kana only if the user asks.

### Formatting
```
audio_prompt: "[Vocalization Type] Non-verbal description."
audio_prompt: "[Dialogue] '使用者提供的原句'"   # ONLY when user provided it, copied verbatim
```
Examples:
```
audio_prompt: "[Breathing] Shallow, uneven breaths under wind hiss."
audio_prompt: "[Laughter] Soft, breathy chuckle trailing into silence."
audio_prompt: "[Footsteps] Wet gravel crunch, slow tempo, distant traffic hum."
audio_prompt: "[Dialogue] '住手！'"   # only because the user supplied this exact line
```
