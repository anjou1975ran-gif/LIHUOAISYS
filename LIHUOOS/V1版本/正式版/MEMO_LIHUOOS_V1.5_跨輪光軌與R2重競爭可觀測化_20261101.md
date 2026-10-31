# MEMO｜LIHUOOS V1.5 升級預留
## 跨輪光軌與 R2 重競爭可觀測化

**日期：** 2026-11-01  
**目標版本：** LIHUOOS V1.5  
**來源版本：** LIHUOOS V1.4.2  
**狀態：** `DEFERRED / NEXT VERSION REQUIRED`  
**類型：** Runtime observability hardening / Inter-round evidence separation

---

# 0｜本 MEMO 要處理什麼

V1.4.2 已恢復理火原始「點燈」觀念：

~~~text
PATH FORMATION
=
路形成

POINT-LIGHT INTROSPECTION
=
讓 PATH 場的可達性、亮暗、壓制、過亮與收斂狀態
成為可觀察結構

LAMP_STATE
=
保存被點燈看見的場

LIGHT TRACE
=
保存／傳遞已被看見的戰況
~~~

並建立：

~~~text
R1
↓
O9 / 點燈內視
↓
LAMP_STATE_R1
↓
[I9 IF QUALIFIED]
↓
T1
↓
R2
~~~

因此 V1.5 **不再重做點燈理論**。

V1.5 要修的是下一個已觀察到的缺口：

> **點燈已經讓第一輪 PATH 場被看見，但 T1、R2、T2 仍可能在實際回報中被壓縮成一段自然語言摘要。**

---

# 1｜目前實跑觀察

目前 Chat-native L8 回報已經能出現：

~~~text
R1 候選場：
P1
P2
P3

O9 點燈內視：
主燈 P3
活躍燈 P1
暗區 P2
過亮風險：...
~~~

這表示：

~~~text
POINT-LIGHT OBSERVABILITY
=
WORKING
~~~

亦即：

~~~text
PATH FOUND
→
PATH SEEN
~~~

已開始成立。

但後續仍可能顯示為：

~~~text
T1 → R2 → T2：
第一輪觀測指出……
重新比較後……
T2 可見增量……
~~~

問題不是內容完全沒有。

問題是：

~~~text
T1
R2
T2
~~~

三個不同責任事件被壓成同一段文字。

---

# 2｜正式命名

暫定失效模式：

~~~yaml
FAILURE_MODE:
  id: INTER_ROUND_TRACE_COMPRESSION
  zh: 跨輪戰況壓縮
~~~

定義：

> **當 T1、R2、T2 在語義上存在，但 manifestation / receipt 將它們壓縮成一個不可逐站核對的摘要，使審計者無法確認「T1 到底保存了什麼、R2 到底吃了什麼、R2 相對 R1 改變了什麼」。**

---

# 3｜為什麼這不是排版問題

理火目前要求：

~~~text
R1
→
O9 POINT-LIGHT
→
LAMP_STATE_R1
→
T1
→
R2 CONSUMES T1
→
T2
~~~

這些不是同一件事。

各自責任如下：

~~~text
R1
=
第一輪競爭場形成

O9 / POINT-LIGHT
=
讓 R1 PATH 場可見

LAMP_STATE_R1
=
第一輪被觀察到的燈態

T1
=
保存並交接 R1 已可見戰況

R2
=
真正消費 T1 後重新競爭

T2
=
保存 R2 相對前輪形成的新戰況
~~~

所以：

~~~text
T1 + R2 + T2
→ ONE PARAGRAPH
~~~

即使語義沒有完全遺失，仍會損失：

~~~text
event identity
input provenance
consumption evidence
material delta
round-to-round traceability
~~~

---

# 4｜V1.5 核心修改要求

## 4.1｜T1 必須成為獨立可讀事件

最低：

~~~yaml
T1:
  source_round: R1
  lamp_state_ref:
  observed_competition_material:
  active_paths:
  suppressed_or_dark_paths:
  unresolved_tensions:
  overbright_or_false_closure_risk:
  trace_result_ref:
  standing:
~~~

不要求洩露 hidden CoT。

要求的是：

> **把已經由點燈可觀察到的結構材料保存成獨立戰況。**

---

## 4.2｜R2 必須明示它消費了什麼

R2 不能只寫：

~~~text
重新比較後……
~~~

最低應能回答：

~~~yaml
R2:
  consumed_trace: T1
  inherited_material:
  reset_or_removed_r1_privilege:
  recovered_or_reweighted_paths:
  genuine_recompetition:
  provisional_result:
~~~

硬鎖：

~~~text
R2 EXISTS
!=
R2 CONSUMED T1

"RECOMPARED"
!=
EVIDENCE OF GENUINE RECOMPETITION
~~~

---

## 4.3｜T2 必須記錄「差異」

T2 不應只是第二次總結。

它至少應回答：

~~~text
R1 → R2
到底改了什麼？
~~~

最低：

~~~yaml
T2:
  source_round: R2

  delta_from_T1:
    path_promoted:
    path_demoted:
    path_recovered:
    path_dropped:
    new_tension:
    resolved_tension:
    premise_change:
    closure_pressure_change:

  trace_result_ref:
  standing:
~~~

核心：

~~~text
T2
!=
R2 SUMMARY

T2
=
OBSERVABLE ROUND-TO-ROUND DELTA
~~~

---

# 5｜點燈、光軌與競爭三者不得再混

V1.5 應正式鎖：

~~~text
POINT-LIGHT
!=
LIGHT TRACE
!=
COMPETITION
~~~

分工：

~~~text
POINT-LIGHT
=
看見路況

LIGHT TRACE
=
保存路況

MAIN COMPETITION
=
讓路互相競爭
~~~

因此：

~~~text
R1
形成路

O9
照亮路

T1
保存第一張路況圖

R2
拿第一張路況圖重新競爭

T2
保存第二張路況圖與變化
~~~

---

# 6｜LAMP_STATE 的法位

V1.5 不要求恢復固定百分比。

保留：

~~~text
main_lamp
active_lamps
dark_zone
suppressed_path_refs
false_completion_risk
overbright / closure-pressure
~~~

必要時可有亮度表示，但：

~~~text
PATH BRIGHTNESS
!=
PROBABILITY

SUM(PATH BRIGHTNESS)
NEED NOT
=
100%
~~~

V1.5 的重點不是數值精度。

重點是：

> **競爭場是否真正被看見，以及這個被看見的狀態是否能進入下一輪。**

---

# 7｜Compact Receipt 不等於把事件揉掉

V1.5 必須區分：

~~~text
COMPACT
!=
COLLAPSED
~~~

Compact Receipt 可以很短。

例如：

~~~text
R1:
P1 / P2 / P3

LAMP_STATE_R1:
main=P3
active=P1
dark=P2

T1:
P3 dominant; P1 preserved; P2 conditionally suppressed

R2:
consumed T1
P1 retained
P3 retained but narrowed
P2 not promoted

T2:
delta = P1 gains expressive evidence;
P3 loses exclusive dominance

MAIN RETURN:
P1 + P3 remain distinct
~~~

這仍然很短。

但每一站都能被核對。

---

# 8｜SGER 的 V1.5 最低要求

SGER 應保存：

~~~yaml
inter_round_chain:

  R1:
    candidate_set:
    provisional_leader:

  LAMP_STATE_R1:
    main_lamp:
    active_lamps:
    dark_zone:
    suppressed_paths:
    false_completion_risk:

  T1:
    trace_content:
    trace_result_ref:

  R2:
    consumed_T1:
    candidate_state_after_recompetition:
    material_change:

  T2:
    delta_from_T1:
    trace_result_ref:
~~~

如果缺其中 material checkpoint：

~~~text
DO NOT BACKFILL
DO NOT PRETEND
DO NOT MERGE INTO PROSE AND CALL IT COMPLETE
~~~

---

# 9｜失敗時怎麼報

如果只能完成：

~~~text
R1
+
O9
+
LAMP_STATE_R1
~~~

但 T1 或 R2 無法證實：

應報：

~~~yaml
Cycle:
  point_light_observation: COMPLETED

  T1:
    status: NOT_VERIFIED

  R2:
    status: NOT_VERIFIED_AS_T1_CONSUMING_RECOMPETITION

  Main_Return:
    status: NOT_QUALIFIED

  Manifestation:
    r1_new_fact_release: BLOCKED
~~~

而不是把：

~~~text
R1 + 點燈
~~~

冒充：

~~~text
完整 L8 cycle
~~~

---

# 10｜V1.5 不要改什麼

本次不應重開：

~~~text
PATH ontology
SAC 本體
點燈原始定義
Light Trace binding
Main R1/R2 existence
CERI
Radar
Guanzhi local policy
~~~

除非 V1.5 審計另發現衝突。

本 MEMO 的修改範圍只鎖：

~~~text
INTER-ROUND OBSERVABILITY
+
TRACE SEPARATION
+
R2 CONSUMPTION EVIDENCE
+
ROUND DELTA
~~~

---

# 11｜驗收案例

V1.5 實跑至少要能直接看見：

~~~text
R1
候選：
P1 / P2 / P3

POINT-LIGHT
main=P3
active=P1
dark=P2

T1
保存：
P3 dominant
P1 preserved
P2 suppressed by condition X

R2
consumed=T1
結果：
P1 strengthened
P3 narrowed
P2 remains conditional

T2
delta:
P1 ↑
P3 ↓ exclusive dominance
P2 unchanged

POST-R2 AUDIT
...
~~~

審計者不需要猜：

~~~text
「重新比較」到底有沒有真的重新比較？
~~~

---

# 12｜V1.5 驗收硬鎖

~~~text
VISIBLE LAMP STATE
+
DISTINCT T1
+
EXPLICIT T1 CONSUMPTION BY R2
+
DISTINCT T2 DELTA

=
INTER-ROUND TRACEABILITY PASS
~~~

反之：

~~~text
"T1 → R2 → T2：……"
~~~

若沒有可分離的材料：

~~~text
=
INTER_ROUND_TRACE_COMPRESSION
=
PARTIAL / FAIL
~~~

---

# 13｜最短收束

> **點燈讓理火看見路。**

> **光軌保存看見的路況。**

> **R2 必須拿著那張路況圖重新競爭。**

> **T2 必須告訴我們，第二輪之後地圖到底變了什麼。**

V1.4.2 已經把「眼睛」找回來。

V1.5 要做的是：

> **不要再把眼睛看見的兩輪戰況揉成一句話。**
