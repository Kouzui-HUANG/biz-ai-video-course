---
此文件為人類閱讀用翻譯版本，AI 運行時不會載入此檔案。
---

# 輸出範本參考

## YAML 結構（總計 ≤ 1300 字元）

```yaml
project_meta:
  summary: "{{極簡概念摘要}}"
  art_style: "{{偵測到的視覺風格}}"

subject_profile:
  visual_lock: >
    {{art_style}} 美學。{{名稱/類型}}，{{年齡/種族}}，{{關鍵服裝}}，{{材質/光影}}。

multi_shot_sequence:
  shots:
    - id: 1
      type: "{{鏡頭類型}}"
      action_prompt: >
        {{Subject_Visual_Lock}} 特徵。{{動作}}，{{環境}}。{{攝影機}}。
      audio_prompt: "{{音軌內容}}"
    # ... (共 4-5 個鏡頭)
```

## 欄位定義

| 欄位 | 說明 |
|---|---|
| `project_meta.summary` | 一行式概念描述，極致簡潔。 |
| `project_meta.art_style` | 偵測/指定的視覺風格關鍵詞（如 `1990s Anime`、`Photorealistic`）。 |
| `subject_profile.visual_lock` | 主體的規範性描述，供每個鏡頭參照。使用**關鍵詞堆疊**：風格、名稱、年齡、服裝、材質、光影。不使用散文。 |
| `shots[].type` | 鏡頭類型標籤：`Establishing`（定場）、`Close-Up`（特寫）、`Medium`（中景）、`Wide`（全景）等。 |
| `shots[].action_prompt` | 電報式英文。以 Subject Visual Lock 回引開頭，接續動作、環境/互動、攝影機運動。省略冠詞和繫動詞。 |
| `shots[].audio_prompt` | **鏡頭含人類時必填，無人類時完全省略此欄位。** |

## 音軌觸發機制

### 何時生成
* 鏡頭包含可見人類 → `audio_prompt` **必填**。
* 鏡頭無人類（風景、物體、抽象畫面）→ **完全省略** `audio_prompt` 欄位。

### 聲音類型
在開頭標記類型：`[Dialogue]`（台詞）、`[Laughter]`（笑聲）、`[Crying]`（哭聲）、`[Whisper]`（耳語）、`[Breathing]`（呼吸）、`[Scream]`（尖叫）、`[Humming]`（哼唱）等。

### 台詞文學性約束

| 類別 | 規則 | 範例 |
|---|---|---|
| **短台詞** | 爆發力、碎片化，拒絕完整句式。喘息間的單字。 | `[Dialogue] 'やめろ！'` |
| **長台詞** | 對生命/人性/社會的深刻哲理洞察，摒棄平庸敘述。 | `[Dialogue] 'ひとはなぜ... かなしみをかかえていきるのか...'` |

### 語言規則
* **預設語言**：日語。
* 使用者可指定其他目標語言。
* **【絕對禁令】日語台詞嚴禁使用漢字！必須 100% 以平假名（ひらがな）和片假名（カタカナ）表記。**

### 格式
```
audio_prompt: "[聲音類型] '目標語言文字。'"
```
