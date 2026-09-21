# Single-Take Schema (一鏡到底)

Use this structure instead of `multi_shot_sequence` when Single-Take mode is active. One take = one shot: the camera path lives inside `single_take.camera_flow` as time-coded beats — never as separate shots.

## YAML Structure (≤ 3000 characters total)

```yaml
project_meta:
  summary: "Oner: one unbroken {{N}}s take, zero cuts—{{Ultra-brief concept}}."
  art_style: "{{Detected Visual Style}}"
  bgm: "(none)"   # default; replace with music description ONLY if user specifies BGM

subject_profile:
  visual_lock: >
    {{project_meta.art_style}} aesthetic. {{Name/Type}}, {{Age/Ethnicity}}, {{Key Outfit}}, {{Texture/Lighting}}.

single_take:
  type: "Oner | Continuous {{Rig}} Take | {{N}}s | Zero Cuts"
  action_prompt: >
    {{Subject_Visual_Lock}} features. {{Space layout: landmarks along path, props later beats pay off}}. Camera and subject move as one; continuous time, no cut, no dissolve.
  camera_flow:
    - beat: "0-{{t1}}s | {{Mark 1}} · {{Cam 1}}"
      camera: "{{Opening framing, height, lens}} → {{first move}}"
      action: "{{Subject action at mark}}"
      sfx: "[{{Type}}] {{Synced non-verbal sound}}"
    - beat: "{{t1}}-{{t2}}s | {{Mark 2}} · {{Cam 1→2}}"
      camera: "{{Move continuing from previous end position}}"
      action: "{{Subject action}}"
      sfx: "[{{Type}}] {{Synced non-verbal sound}}"
    # ... 4-5 beats total, contiguous timecodes
    - beat: "{{tn}}-{{N}}s | {{Mark n}} · {{Cam n-1→n}}"
      camera: "{{Final move}} → land {{final framing}}; hold"
      action: "{{Climactic action}}. Final frame: {{composition}}"
      sfx: "[{{Type}}] {{Sound}}, then silence"
  audio_prompt: "[Ambience] {{Continuous bed under whole take}}."
```

## Field Definitions

| Field | Description |
|---|---|
| `project_meta.summary` | Starts `Oner: one unbroken {{N}}s take, zero cuts—` + one-line concept. |
| `single_take.type` | Declares the oner: rig (`Gimbal`, `Steadicam`, `Handheld`, `Drone`, `Crane`), total duration, `Zero Cuts`. |
| `single_take.action_prompt` | Telegraphic. Visual-lock echo → space layout the path crosses (landmarks by side; plant every prop a later beat touches) → continuity clause `continuous time, no cut, no dissolve`. |
| `camera_flow` | The camera path: 4-5 beats (3 if take ≤ 8s). Timecodes contiguous from `0` to total duration (default 15s unless user/model sets another length). |
| `camera_flow[].beat` | Timecode, then `{{actor mark}} · {{camera waypoint}}`, formatted as in the template. With a blocking diagram, copy its labels verbatim (e.g. `Mark2 · C1→C2`); otherwise short place labels (e.g. `Doorway · Entry`). |
| `camera_flow[].camera` | ONE primary move per beat: framing, height, lens, move; chain changes with `→`. Starts where previous beat ended — never reset, never cut. |
| `camera_flow[].action` | Subject action at that mark. Final beat ends with `Final frame: {{composition}}`. |
| `camera_flow[].sfx` | Sound synced to that beat, tagged per `output-schema.md` § Vocalization Types; non-verbal by default. Omit on beats with no visible human. |
| `single_take.audio_prompt` | ONE continuous `[Ambience]` bed under the whole take (room tone, distant world). Omit if no human appears anywhere in the take. |

## Craft Rules
* **One shot only**: never emit `multi_shot_sequence` / `shots`. Shot size changes come from camera distance & height (wide → medium → close), not cuts.
* **Beat = mark + move**: each beat pairs one subject position with one camera waypoint/move.
* **Setup → payoff**: plant in `action_prompt` every prop/landmark a later beat touches.
* **Landing**: last beat lands a composed final frame and holds.
* **Dialogue**: only when user-supplied — put `[Dialogue] '...'` in that beat's `sfx`; apply `output-schema.md` § Literary Protocol & Language Rules.

## Example Beat _(style reference only — never reuse its content)_

```yaml
    - beat: "10-15s | Mark4 · C3→C4"
      camera: "Arc right alongside her, descend to knee height → land low medium close-up, shallow focus; hold on stillness"
      action: "Sits on tufted bench, bends; fingertips touch ankle strap of shoes left beside piano; breath catches, eyes soften. Final frame: shoes foreground, her three-quarter face above, piano keys behind"
      sfx: "[Sigh] Leather bench creak, shaky quiet sigh, then silence"
```
