# 觀止青樓｜白御行線 MASTER SAVE V3.0-R2 補充修正版

目的： 根據首席AI審核意見，補充 V3.0-R1 的資料結構缺口。
本文件不是推翻原SAVE，而是新增規格。

------------------------------------------------------------------------

# 一、新增：契約狀態機（Contract State Machine）

## 蘇清三晚契約

``` yaml
SU_QING_CONTRACT:

  original_agreement:
    consideration:
      - 五百兩

    duration:
      - 三晚

    status:
      - 原始契約存在

  performance_definition:
    separation_required:
      - 原始約定
      - 實際履行
      - 後續爭議

  execution:

    night_1:
      status:
        - 未完成

    night_2:
      status:
        - 未完成

    night_3:
      status:
        - 未完成

  settlement:
    payment:
      status:
        - 未結算

    dispute:
      status:
        - 未關閉
```

規則：

-   未完成不等於不存在。
-   拒絕履行不等於原始契約不存在。
-   契約成立、履行狀態、後續處理必須分開。

------------------------------------------------------------------------

# 二、新增：事實來源權重（Fact Provenance）

所有重大事實新增：

``` yaml
FACT_RECORD:

  event:

  source_type:
    - CHARACTER_SELF
    - PLAYER_RECORD
    - PUBLIC_WITNESS
    - THIRD_PARTY
    - RUMOR

  certainty:
    - CONFIRMED
    - INTERPRETED
    - DISPUTED
    - UNKNOWN

  interpretation_difference:
    exists:
      true/false
```

用途：

同一事件可以存在不同人物理解。

事件本身與人物解讀分離。

------------------------------------------------------------------------

# 三、新增：狀態分類

原本 status 同時負責分類與描述。

改為：

``` yaml
STATE:

  state_class:
    - ACTIVE
    - UNSETTLED
    - CLOSED
    - UNDECIDED
    - REJECTED

  state_label:

  description:
```

用途：

AI可用 state_class 判斷， 人類可讀 state_label。

------------------------------------------------------------------------

# 四、新增：稿件委託狀態拆分

蘇清話本：

``` yaml
COMMISSION:

  commission_status:
    - ACCEPTED

  manuscript_status:
    - NOT_SUBMITTED

  client_review:
    - NOT_REVIEWED

  payment:
    - CONDITIONAL
```

避免：

委託成立與稿件驗收混淆。

------------------------------------------------------------------------

# 五、新增：MASTER / HOT / PATCH 三層制度

## MASTER ARCHIVE

保存：

-   固化歷史
-   已確認關係
-   已提交事件

## HOT SAVE

保存：

-   當日劇情
-   現場人物
-   未決事項

## EVENT PATCH

保存：

-   單次事件變更

格式：

``` yaml
EVENT_PATCH:

  event_id:

  trigger:

  participants:

  immediate_change:

  affected_states:

  future_hook:
```

------------------------------------------------------------------------

# 六、新增：世界污染歷史紀錄

## 蘇清契約循環污染案例

分類：

-   Runtime污染案例
-   人物狀態漂移案例
-   契約語義漂移案例

原則：

-   不回溯刪除。
-   不假設未發生。
-   作為時間線歷史保存。
