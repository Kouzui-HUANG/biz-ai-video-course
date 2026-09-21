---
此文件為人類閱讀用翻譯版本，AI 運行時不會載入此檔案。
---

# 一鏡到底範本（Single-Take Schema）

啟用一鏡到底模式時，以此結構取代 `multi_shot_sequence`。一鏡 = 一個鏡頭：運鏡路徑以時間碼節拍寫在 `single_take.camera_flow` 裡——絕不拆成獨立鏡頭。

## YAML 結構（總計 ≤ 3000 字元）

> 範本中的英文固定字串（`Oner: one unbroken`、`Zero Cuts`、`no cut`、`land`、`hold`、`Final frame:`、`then silence` 等）是實際輸出時要照寫的英文；`{{ }}` 內為待填內容。

```yaml
project_meta:
  summary: "Oner: one unbroken {{N}}s take, zero cuts—{{極簡概念}}."
  art_style: "{{偵測到的視覺風格}}"
  bgm: "(none)"   # 預設值；唯有使用者指定配樂時才替換為音樂描述

subject_profile:
  visual_lock: >
    {{art_style}} 美學。{{名稱/類型}}，{{年齡/種族}}，{{關鍵服裝}}，{{材質/光影}}。

single_take:
  type: "Oner | Continuous {{運鏡載具}} Take | {{N}}s | Zero Cuts"
  action_prompt: >
    {{Subject_Visual_Lock}} 特徵。{{空間配置：路徑經過的地標、後段節拍會回收的道具}}。Camera and subject move as one; continuous time, no cut, no dissolve.
  camera_flow:
    - beat: "0-{{t1}}s | {{站位 1}} · {{機位 1}}"
      camera: "{{起幅景別、高度、焦段}} → {{第一個運鏡}}"
      action: "{{主體在此站位的動作}}"
      sfx: "[{{類型}}] {{同步的非語言聲響}}"
    - beat: "{{t1}}-{{t2}}s | {{站位 2}} · {{機位 1→2}}"
      camera: "{{從上一節拍結束位置延續的運鏡}}"
      action: "{{主體動作}}"
      sfx: "[{{類型}}] {{同步的非語言聲響}}"
    # ... 共 4-5 個節拍，時間碼首尾相接
    - beat: "{{tn}}-{{N}}s | {{站位 n}} · {{機位 n-1→n}}"
      camera: "{{最後的運鏡}} → land {{最終景別}}; hold"
      action: "{{高潮動作}}. Final frame: {{最終構圖}}"
      sfx: "[{{類型}}] {{聲響}}, then silence"
  audio_prompt: "[Ambience] {{貫穿全程的環境音底}}."
```

## 欄位定義

| 欄位 | 說明 |
|---|---|
| `project_meta.summary` | 以 `Oner: one unbroken {{N}}s take, zero cuts—` 開頭，接一行概念描述。 |
| `single_take.type` | 宣告這是一鏡到底：運鏡載具（`Gimbal` 穩定器、`Steadicam` 斯坦尼康、`Handheld` 手持、`Drone` 空拍機、`Crane` 搖臂）、總長度、`Zero Cuts`。 |
| `single_take.action_prompt` | 電報式。Visual Lock 回引 → 路徑經過的空間配置（依左右側列出地標；後段節拍會碰到的道具都要先埋下）→ 連續性宣告 `continuous time, no cut, no dissolve`。 |
| `camera_flow` | 運鏡路徑：4-5 個節拍（鏡頭總長 ≤ 8 秒時用 3 個）。時間碼從 `0` 首尾相接到總長度（預設 15 秒，除非使用者或模型另有指定）。 |
| `camera_flow[].beat` | 時間碼，接 `{{演員站位}} · {{攝影機機位}}`，格式同範本。有走位圖時，一字不差沿用圖上標籤（如 `Mark2 · C1→C2`）；沒有則用簡短地點標籤（如 `Doorway · Entry`）。 |
| `camera_flow[].camera` | 每個節拍只有一個主要運鏡：景別、高度、焦段、運動；變化用 `→` 串接。從上一節拍結束的位置接續——絕不重置、絕不剪接。 |
| `camera_flow[].action` | 主體在該站位的動作。最後一個節拍以 `Final frame: {{構圖}}` 收尾。 |
| `camera_flow[].sfx` | 與該節拍同步的聲音，依 `output-schema.md` § Vocalization Types 標記類型；預設為非語言聲響。畫面中沒有人的節拍省略此欄。 |
| `single_take.audio_prompt` | 貫穿全程的單一 `[Ambience]` 環境音底（空間底噪、遠方環境聲）。整個鏡頭都沒有人出現時省略。 |

## 創作規則
* **只有一個鏡頭**：絕不輸出 `multi_shot_sequence` / `shots`。景別變化來自攝影機的距離與高度（全景 → 中景 → 近景），而非剪接。
* **節拍 = 站位 + 運鏡**：每個節拍配對一個主體位置與一個攝影機機位／運鏡。
* **埋設 → 回收**：後段節拍會碰觸的道具／地標，都要先在 `action_prompt` 埋下。
* **落幅**：最後一個節拍落定在構圖完整的最終畫面並停留。
* **台詞**：僅在使用者提供時——把 `[Dialogue] '...'` 寫進該節拍的 `sfx`，並套用 `output-schema.md` § Literary Protocol 與 Language Rules。

## 節拍範例 _（僅供風格參考——不可沿用其內容）_

```yaml
    - beat: "10-15s | Mark4 · C3→C4"
      camera: "Arc right alongside her, descend to knee height → land low medium close-up, shallow focus; hold on stillness"
      action: "Sits on tufted bench, bends; fingertips touch ankle strap of shoes left beside piano; breath catches, eyes soften. Final frame: shoes foreground, her three-quarter face above, piano keys behind"
      sfx: "[Sigh] Leather bench creak, shaky quiet sigh, then silence"
```

中譯：10–15 秒｜站位 4・機位 C3→C4。攝影機沿她身側向右弧移、下降到膝蓋高度 → 落定低角度中近景、淺景深，靜止停留。她坐上釦飾琴凳、彎身，指尖碰觸鋼琴旁那雙鞋的踝帶，呼吸一滯、眼神柔和下來。最終畫面：前景是鞋，上方是她的四分之三側臉，後方是琴鍵。音效：皮革琴凳吱嘎聲、微顫的輕嘆，然後歸於寂靜。
