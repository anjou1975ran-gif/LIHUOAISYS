# 觀止人物池 V6｜外貌與視覺基線共用格式

**狀態：** WORKING / CHARACTER VISUAL MANIFESTATION SCHEMA
**用途：** 人物文字顯影、立繪、生圖、場景插圖與跨圖一致性。
**原則：** 外貌服從人物結構；視覺設計不反向改寫人物歷史、人格、法律身分、同意或 Route 事件。

## 1｜兩層資料法

每張人物視覺卡分成兩層：

```text
SOURCE_ANCHORED_FACTS
=
現有人物池／世界資料已明確支持的身體、年齡、職業、裝束或生活事實

VISUAL_DESIGN
=
依人物結構新增的導演視覺設計
```

VISUAL_DESIGN 是可用於生圖與文字顯影的現行工作基線，但不得偽裝成舊來源已寫死的事實。

## 2｜共用欄位

```yaml
VISUAL_MANIFESTATION_BASE:
  character: ""
  standing: "WORKING / DIRECTOR_VISUAL_DESIGN"

  SOURCE_ANCHORED_FACTS:
    - ""

  VISUAL_DESIGN:
    apparent_age: ""
    silhouette: ""
    frame: ""
    body_shape: ""
    posture_and_movement: ""

    face:
      shape: ""
      eyes: ""
      brows: ""
      nose: ""
      lips: ""
      skin: ""

    hair:
      color_texture: ""
      default_style: ""

    distinguishing_features:
      - ""

    presentation:
      makeup: ""
      clothing: ""
      palette: ""
      ornaments: ""

    first_glance:
      impression: ""
      attraction_or_presence: ""
      structural_tension:
        - ""

  IMAGE_GENERATION_ANCHOR:
    must_keep:
      - ""
    may_vary:
      - ""
    must_not:
      - ""
```

## 3｜固定規則

- 不要求所有女性白、瘦、幼、尖下巴、大眼、同一種胸腰臀比例。
- 不把「漂亮」當作人物辨識度；必須描述她是哪一種人、她如何被看見。
- 年齡、勞動、職業、階級與身體史可以留下痕跡，不自動磨平成二十歲無瑕皮膚。
- 已確認纏足者可保留小腳與步態影響，但不得把纏足自動色情化、病態奇觀化或誇張成恐怖變形。
- UNKNOWN / NOT_FIXED 不因生圖需要而自動變成 canon；必要時只在 VISUAL_DESIGN 層建立可修改的工作選擇。
- 服裝以觀止世界與人物職業位置為核心；可有美術化，但不得自動現代網紅化、影樓化或把所有人都畫成同一套華服。
- 圖像中的身體、衣著與情色表現不建立任何人物同意、性服務、關係或 Route 結果。
- 外貌卡可以更新；更新視覺設計不等於人物人格或世界史被改寫。

## 4｜最小生圖原則

生圖時優先使用：

```text
人物辨識結構
+
年齡／身形
+
臉部辨識點
+
姿態
+
服裝調性
+
must_keep
+
must_not
```

不需要每次把整張人物卡塞進 prompt。
