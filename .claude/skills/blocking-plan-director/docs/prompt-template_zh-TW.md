# 提示詞模板：Clean ArchViz 走位平面圖（繁中閱讀版）

> 本檔為 `references/prompt-template.md` 的人類閱讀版，不會被 AI 載入執行。英文提示詞區塊保持原文。

## 目錄
1. 組裝方式
2. 固定段落 (A) (B) (D)
3. (C) 段落的填空文法
4. 人物描述句
5. 變體：畫幅 · 室外 · 標籤語言
6. 完整範例（沙龍，沒有演員圖 → 白模假人）

---

## 一、組裝方式
一個 `text` code block，裡面有四個標記段落：(A) 攝影機、(B) 渲染風格、(C) 空間＋走位、(D) 光線＋背景＋圖例，最後以 `--ar {ratio}` 結尾。(A)(B)(D) 幾乎照抄；(C) 承載場景內容。

(C) 的方向用語：**up**＝往上緣（遠端），**down**＝往下緣（攝影機那側），**left/right** 依平面圖。稱呼演員時用「the figure」或「the actor」，絕不用有性別的代名詞。

---

## 二、固定段落

**(A)**
```text
(A) A perfectly orthographic top-down plan view, shot from directly overhead at exactly 90 degrees — parallel projection, zero perspective convergence, no tilt — with the whole {room} centered in a {16:9 landscape} frame, a clean margin on the {right} for a small legend, and everything tack-sharp edge to edge with no depth-of-field blur.
```

**(B)**：室內用（室外見 §5）
```text
(B) Photorealistic high-end architectural visualization 3D floor plan, Unreal Engine 5 / V-Ray path-traced quality: ceiling removed, walls shown as clean solid cut sections, physically accurate materials, soft ambient occlusion and contact shadows, subtle reflections in {the glossiest surface} — topped with a crisp, flat vector annotation layer in the style of a professional film blocking diagram.
```

**(D)**：光線欄位從照片推導：光源、在平面圖上的方向、光質（柔和陰天／硬光直射帶窗形光斑／夜間實用光源）、色溫，以及實用燈具畫成的暖色光暈。
```text
(D) {Light from the reference photo}; neutral, true-to-life color with {2–3 signature objects} as clear accents; calm, precise, premium real-estate-render clarity. The cutaway {room} floats on a plain light warm-grey background with a soft drop shadow. A small clean legend card in the {right} margin: red dashed line = "ACTOR", blue solid line = "CAMERA". No other text, no ceiling, no extra furniture, {no other figures | no other people}. --ar {ratio}
```
搭配白模假人時寫「no other figures」，搭配真人演員時寫「no other people」。

---

## 三、(C) 段落的填空文法

**佈局**：依 `blocking-knowledge-base.md` §1.4 的盤點順序：
```text
(C) A faithful plan-view reconstruction of the {space} in the reference photo: a {shape} about {W} m wide and {D} m deep, oriented exactly like the photo — {reference-camera side} at the bottom edge, {far side} along the top, {left side} on the left, {right side} on the right. {Floor as seen from above}. {Top edge}. Left wall, bottom to top: {…}. Right wall, bottom to top: {…}. {Free-standing pieces anchored to fixed ones}. {Floor props / hooks}. {Overhead fixtures as thin grey dashed outlines}; the {near zone} is open, empty floor.
```

**演員**
```text
ACTOR: a bold crimson dashed line with arrowheads through {n} numbered red circles. 1 {where}, where {FIGURE} {pose}; the line {curves / bends / cuts} {direction} to 2 {where}; … to {n} {where}, where {final action}.
```

**攝影機**
```text
CAMERA: a solid electric-blue line with arrowheads linking {m} blue camera icons, each with a short translucent blue field-of-view wedge. C1 {at the reference-camera position}, its wedge opening {into the space} (the reference-photo framing); a {straight / smooth / curved} segment labeled "{MOVE}" {verb} to C2 {where}; …; ending at C{m} {where}, its wedge aimed at {target}.
```
只標運鏡（最多 4 個）；站位與 C 編號不需要額外文字。標籤格式見 `blocking-knowledge-base.md` §3。

---

## 四、人物描述句（FIGURE 欄位）

| 演員來源 | 描述句（英文原文） |
|---|---|
| 有演員圖 | a small photoreal figure of the actor from the attached actor reference, seen from directly above ({hair color & style}, {outfit color & silhouette}, {footwear}) |
| 場景圖中已有人物 | a small photoreal figure of the person from the reference photo, seen from directly above ({same three features}) |
| 沒有演員圖 | a small matte white clay mannequin seen from directly above — a {slender female-proportioned / broad male-proportioned / child-sized} artist's figure with no face, hair or clothing detail |

只採用從上方看得出來的特徵：頭髮、肩膀、服裝顏色與輪廓、帽子、包包、鞋子。臉部略過。如果完全看不出體型，就拿掉比例描述。

---

## 五、變體

**畫幅**（平面圖深度 ÷ 寬度）：
| D ÷ W | 畫幅 | 圖例位置 |
|---|---|---|
| 0.5–1.3（多數房間） | 16:9 橫幅 | 右側 |
| 1.3–2.0 | 3:4 直幅 | 下方 |
| > 2.0（走廊） | 9:16 直幅 | 下方 |
| < 0.5（非常寬的空間） | 21:9 橫幅 | 右側 |

**室外**：把 (B) 換成：
```text
(B) Photorealistic high-end architectural visualization 3D site plan, Unreal Engine 5 / V-Ray path-traced quality: the site cut out as a clean rectangular diorama block with neatly sectioned ground edges, building roofs removed and walls shown as cut sections, tree canopies rendered semi-transparent so the paths beneath stay visible, physically accurate materials, soft ambient occlusion and contact shadows — topped with a crisp, flat vector annotation layer in the style of a professional film blocking diagram.
```
(D) 裡的「cutaway room」改成「cutaway site block」，「no extra furniture」改成「no extra buildings or vehicles」。

**標籤語言**：預設為簡短的英文大寫。如果使用者要中文標籤，就在提示詞裡用引號寫中文，每個不超過 4 個字，並在「使用建議」提醒中文標籤比較容易變成亂碼。

---

## 六、完整範例（僅供校準，絕不可重複使用其內容）

輸入：一張從敞開的雙扇門往內拍的巴黎奧斯曼式沙龍照片；沒有演員圖。

**設計假設：** 只有場景圖、沒有演員圖，所以用白模假人（地上的高跟鞋暗示女性，採纖細女性比例）｜動作由我設計：進門、佇窗、落座｜總長 15 秒｜16:9

| 時間 | 演員 | 攝影機 | 動作與運鏡 |
|---|---|---|---|
| 0–3s | Mark1 | C1→C2 | 首幀＝原圖；假人從鏡頭旁進門；DOLLY IN 穿過門口 |
| 3–7s | Mark2 | C2→C3 | 經過紅絲絨椅；STEADICAM FOLLOW 在身後約 2 m 跟拍 |
| 7–10s | Mark3 | C3 | 停在中央落地窗前望向窗外；HOLD，拍逆光背影 |
| 10–15s | Mark4 | C3→C4 | 斜走到鋼琴，撿起高跟鞋坐下；ARC 90° 收在側臉 |

```text
(A) A perfectly orthographic top-down plan view, shot from directly overhead at exactly 90 degrees — parallel projection, zero perspective convergence, no tilt — with the whole room centered in a 16:9 landscape frame, a clean margin on the right for a small legend, and everything tack-sharp edge to edge with no depth-of-field blur.

(B) Photorealistic high-end architectural visualization 3D floor plan, Unreal Engine 5 / V-Ray path-traced quality: ceiling removed, walls shown as clean solid cut sections, physically accurate materials, soft ambient occlusion and contact shadows, subtle reflections in the polished stone — topped with a crisp, flat vector annotation layer in the style of a professional film blocking diagram.

(C) A faithful plan-view reconstruction of the Parisian Haussmann salon in the reference photo: a rectangular room about 6 m wide and 7 m deep, oriented exactly like the photo — open double entrance doors (dark, distressed paint) centered on the bottom edge, the window wall along the top, the fireplace wall on the left, the piano wall on the right. Polished black-and-white marble checkerboard floor laid on the diagonal, reading as a harlequin diamond pattern from above. Top wall: three tall arched black-framed French doors, the middle one wider, each opening onto a shallow wrought-iron Juliet balcony, sheer ivory curtains gathered beside each on one long black iron rod. Left wall, bottom to top: a carved white marble Louis XV fireplace at mid-wall with a black hearth, brass andirons and a vase of deep red roses on the mantel; a white plaster bust on a dark wood pedestal; a tall dark side door; a kentia palm in a blue-and-white porcelain planter in the top-left corner. Between the fireplace and the palm, about a meter into the room: a red velvet tufted slipper chair with a fringed skirt, angled toward the room center, beside a small round dark wood side table. Right wall, bottom to top: a glossy black upright piano with open sheet music and a black tufted leather bench on its room side; a wooden console bar with crystal decanters and dried branches near the top-right corner. On the floor just below the bench, toward the entrance: a pair of black ankle-strap heels, one tipped over. A thin grey dashed circle at the center marks the chandelier overhead; the lower third near the doors is open, empty floor.
ACTOR: a bold crimson dashed line with arrowheads through four numbered red circles. 1 just inside the doorway, where a small matte white clay mannequin seen from directly above — a slender female-proportioned artist's figure with no face, hair or clothing detail — is stepping into the room; the line curves up and to the left to 2 beside the red velvet chair; bends up and to the right to 3 in front of the central French door, where the figure stops to look out; then cuts diagonally down and to the right to 4 at the piano bench, where the figure picks up the heels and sits facing the piano.
CAMERA: a solid electric-blue line with arrowheads linking four blue camera icons, each with a short translucent blue field-of-view wedge. C1 stands in the open doorway between the two door leaves on the room's center axis, its wedge opening up into the room (the reference-photo framing); a straight segment labeled "DOLLY IN" pushes through the doorway to C2 just inside the room; a smooth curve labeled "STEADICAM FOLLOW" trails about two meters behind the figure to C3 at the center of the room, its wedge aimed at the central window; a final curve labeled "ARC 90°" swings right toward the piano and wraps a quarter-circle around the bench, ending at C4 on the bench's entrance side, just beyond the heels, its wedge aimed up at the figure's seated profile.

(D) Soft overcast winter daylight enters through the three French doors, brightest along the window wall and fading gently toward the entrance, with faint warm pools from brass wall sconces near the side walls; neutral, true-to-life color with the red chair, red roses and black piano as clear accents; calm, precise, premium real-estate-render clarity. The cutaway room floats on a plain light warm-grey background with a soft drop shadow. A small clean legend card in the right margin: red dashed line = "ACTOR", blue solid line = "CAMERA". No other text, no ceiling, no extra furniture, no other figures. --ar 16:9
```

搭配演員圖時，只有人物描述句要換（§4），排除句改成「no other people」。
