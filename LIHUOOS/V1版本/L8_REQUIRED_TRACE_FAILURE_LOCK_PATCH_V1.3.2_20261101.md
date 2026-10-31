# LIHUOOS L8｜Required Trace Failure Lock
## V1.3.2｜Mandatory Companion Patch
### 2026-11-01

~~~yaml
DOCUMENT:
  id: LIHUOOS_L8_REQUIRED_TRACE_FAILURE_LOCK_PATCH
  version: V1.3.2
  date: 2026-11-01
  standing:
    - HUMAN_RATIFIED_CURRENT_MANDATORY_PATCH
    - BUGFIX
    - FIRST_ROUND_DISTRUST_PRESERVATION
    - R1_PREMATURE_CANONIZATION_BLOCK

  base:
    file: "L8_LIHUO_OPERATING_CYCLE_V1.3.1_20261031.md"
    blob_sha: "8f68fd0b522bee38eb0eee370365cd55a8a7d0a1"

  dependency:
    l9_patch: "L9_LIGHT_TRACE_BINDING_PATCH_V1.2.3_20261101.md"
    light_trace_source: "L9_CAPABILITIES/light_trace_v1_4.dail.yaml"
~~~

# 1｜Preserved Rule

原規則不變：

~~~text
R1 = PROVISIONAL

FIRST-PASS VICTORY
!=
AUTOMATIC CLOSURE

R1 MAY BE CORRECT
!=
R1 MAY SELF-VALIDATE
~~~

# 2｜T1 Is Required Handoff

~~~text
R1
→
T1 / R1_COMPETITION_TRACE
→
R2 CONSUMES T1
~~~

因此 T1 不是裝飾欄位。

# 3｜Hard Failure Lock

~~~text
T1 REQUIRED
+
NO TRACE RESULT
→
R2_T1_CONSUMPTION = NOT_VERIFIED

R2_T1_CONSUMPTION = NOT_VERIFIED
→
MAIN_RETURN_COMPLETION = NOT_QUALIFIED

MAIN_RETURN_COMPLETION = NOT_QUALIFIED
→
R1 PROVISIONAL RESULT
MAY NOT BECOME
NEW CANONICAL MANIFESTATION FACT
~~~

允許顯示：

~~~text
ESTABLISHED SOURCE FACT
EXISTING WORLD FACT
EXISTING SAVE FACT
USER-ESTABLISHED FACT
~~~

但不允許把本輪 R1 新生成的 provisional winner 偷渡成已成立世界事實。

# 4｜Receipt Requirement

若 T1 失敗：

~~~yaml
T1:
  state: FAILED_OR_UNAVAILABLE
  trace_result_ref: NONE
  gap: REQUIRED_TRACE_RESULT_MISSING

R2:
  state: NOT_VERIFIED_AS_T1_CONSUMING_RECOMPETITION

Main_Return:
  state: NOT_QUALIFIED

Manifestation:
  new_r1_derived_fact_release: BLOCKED

Cycle_Outcome:
  state: INCOMPLETE
~~~

# 5｜Root Sentence

> **第一輪不信不是一句哲學口號；T1 是它進入 R2 的結構橋。橋沒有成立，R1 就不能偷渡成世界事實。**
