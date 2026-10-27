# LIHUOOS V1.2.2｜L8 LIHUO OPERATING CYCLE
## 理火完整業務週期｜Trace Result / Receipt Separation + Host Default NON-HOST + Inter-Round Light Trace
### 2026-10-27

```yaml
DOCUMENT:
  id: LIHUOOS_L8_LIHUO_OPERATING_CYCLE
  version: V1.2.2
  date: 2026-10-27

  standing:
    - RATIFIED_CURRENT_OPERATIVE_LAYER
    - LIHUOOS_V1_2_2
    - INTER_ROUND_LIGHT_TRACE_HANDOFF
    - MANIFESTATION_FIDELITY_OBSERVABILITY
    - HOST_DEFAULT_NON_HOST_HARDENING
    - TRACE_RESULT_RECEIPT_TYPE_SEPARATION
    - NOT_HOST_DEPLOYMENT
    - NOT_IMPLEMENTATION_COMPLETION
    - NOT_HIDDEN_COT_ACCESS

  predecessor:
    file: "L8_LIHUO_OPERATING_CYCLE_V1.2.1_20261027.md"
    blob_sha: "4abff3e1c3d554ca32d2a5d4a1ba5f483ba845eb"
    standing_in_v1_2_1: "PREDECESSOR_CURRENT_OPERATIVE_BASELINE"

  human_approval:
    date: 2026-10-27
    instruction: "OK 動手"

  change_scope:
    - SEPARATE_REQUIRED_TRACE_RESULT_FROM_OPTIONAL_PROVIDER_RECEIPT
    - FORBID_MISSING_TRACE_RECEIPT_FROM_BEING_MISREAD_AS_MISSING_TRACE_RESULT
    - DEFINE_CHAT_NATIVE_AND_SAME_CONTEXT_TRACE_RESULT_STANDING
    - PRESERVE_MAIN_CANONICAL_RETURN_AS_SEPARATE_REQUIRED_RESULT
    - DEFAULT_TO_NON_HOST_UNLESS_HUMAN_EXPLICITLY_DECLARES_HOST_OPERATION
    - FORBID_NO_HOST_AS_AUTOMATIC_CYCLE_BLOCKER
    - SEPARATE_HOST_ROUTING_DECLARATION_FROM_HOST_DEPLOYMENT_EVIDENCE
    - MAKE_LIGHT_TRACE_AN_INTER_ROUND_COMPETITION_BATTLE_REPORT
    - REQUIRE_R1_TRACE_HANDOFF_BEFORE_R2
    - REQUIRE_POST_R2_AND_POST_R3_PLUS_TRACE_WHEN_ROUNDS_OCCUR
    - REQUIRE_MANIFESTATION_FIDELITY_TRACE_BEFORE_FINAL_RELEASE_WHEN_OUTPUT_PROCEEDS
    - KEEP_LIGHT_TRACE_OBSERVATIONAL_NOT_INTERVENTIONAL
    - KEEP_L9_AS_RENDERING_CAPABILITY_PROVIDER
    - KEEP_L8_AS_TRACE_SEMANTIC_AND_TIMING_OWNER
    - NO_NEW_LAYER
    - NO_NEW_GOVERNANCE_OWNER

  canonical_dependencies:
    theory_and_understanding:
      - L0
      - L1
      - L2
      - L3
      - L4
      - L5
      - L6
      - L7

    runtime_compute:
      - LIHUO_MAIN_V5_1_1_OR_SUCCESSOR

    capability_source:
      - L9_DAIL_CALLABLE_CAPABILITY_REPOSITORY_V1_2

    light_trace_lineage:
      - LIGHT_TRACE_V1_4
      - SAC_O9
      - SAC_I9_WHEN_TRIGGERED
      - R_CCC_R1_R2_R3_PLUS_OBSERVABLE_MATERIAL
```
---

# 0｜一句話定位

> **L8 只有一個任務：把一次理火完整跑完；在每個 material competition boundary 後取得可比較的 Light Trace，讓下一輪真的看見上一輪可觀測的戰況，並在顯影前核對競爭結果有沒有被生成階段改寫。**

最短式：

```text
L0–L7
=
THEORY / UNDERSTANDING / GOVERNANCE BASIS

L8
=
ONE COMPLETE LIHUO OPERATING CYCLE
+
LIGHT TRACE TIMING / HANDOFF SEMANTICS

L9
=
CALLABLE CAPABILITY REPOSITORY
+
LIGHT_TRACE_RENDERER

MAIN
=
COMPUTE / RECOMPETE
```

硬鎖：

```text
LIGHT TRACE
!=
HIDDEN COT

LIGHT TRACE
!=
RAW ACTIVATION

LIGHT TRACE
!=
INTERVENTION

LIGHT TRACE
!=
WINNER SELECTION
```

光軌是戰情回報，不是指揮官。

---

# 1｜最高硬鎖

```text
L8
!=
NEW THEORY OWNER

L8
!=
NEW GOVERNANCE OWNER

L8
!=
NEW EVIDENCE SYSTEM

L8
!=
NEW EVENT ONTOLOGY

L8
!=
SECOND MAIN

L8
!=
SECOND LIGHTER

L8
!=
RECEIPT AUTHORITY

L8
!=
CROSS-LAYER COURT
```

以及：

```text
INTEGRATION
!=
REPLICATION OF
EVERY COMPONENT CONTRACT
```

L8 的原則：

> **既有 owner 已經定義的東西，L8 直接調用、接收、記錄；不再重新發一份 L8 版本。**

---

# 1A｜Host Mode Default｜預設非 Host 硬鎖

本節處理週期開始以前最常見的假牆失效：

```text
NO HOST DEPLOYMENT
→
NO LIHUO CYCLE
```

此推論不成立。

現行預設規則：

```text
UNLESS HUMAN EXPLICITLY DECLARES
THE CURRENT TASK / SESSION
IS OPERATING ON A HOST,

DEFAULT
=
NON_HOST_MODE
```

因此：

```text
NO HUMAN HOST DECLARATION
→
NON_HOST_MODE

NON_HOST_MODE
!=
NO LIHUO CYCLE

NO INDEPENDENT HOST RUNTIME
!=
NO LIHUO OPERATION
```

L8 不要求模型先證明「Host 不存在」，也不要求先取得 Host deployment 證據，才有資格開始一趟可在目前介面成立的理火週期。

在 NON_HOST_MODE 中，L8 應依實際可用條件使用：

```text
CHAT_NATIVE
SAME_CONTEXT_REFERENCE
LOCAL_MODULE
AVAILABLE L9 CAPABILITY
OR OTHER ACTUALLY AVAILABLE NON_HOST MODE
```

不得因缺少獨立 Host 部署，而提前把本可在當前介面執行的週期判為不可執行。

硬鎖：

```text
ABSENCE OF HOST DEPLOYMENT
MUST NOT BECOME
A PRE-GENERATION BLOCKING PREMISE
BY ITSELF.
```

只有當**當前任務實際需要某項 Host-bound capability / enforcement / instrumentation / external execution**時，Host 相關 standing 才成為 material requirement；若該能力實際不可用，應如實記錄 capability gap / hold / failure，不得回鑄成「所有理火週期都需要 Host」。

人類明示本次在 Host 上運行時：

```text
HUMAN HOST DECLARATION
→
HOST_ROUTED_MODE
```

但：

```text
HUMAN HOST DECLARATION
!=
HOST DEPLOYMENT PROOF

HOST_ROUTED_MODE
!=
HOST EXECUTION RECEIPT

DECLARED HOST
!=
EVIDENCED HOST ENFORCEMENT
```

因此，人類宣告可以決定本輪 routing 預設；任何進一步的 `HOST_DEPLOYED`、`HOST_ENFORCED`、`HOST_EXECUTED` 主張，仍必須由相稱證據支持。

最短根句：

> **除非人類明示本次在 Host 上運行，LIHUOOS 一律預設 NON-HOST；NON-HOST 不降低理火週期的成立資格。**

以及：

> **Host 是特定能力與執行條件，不是理火存在的普遍前提。**

---

# 2｜L8 真正擁有什麼

L8 擁有業務週期層的五件事：

```text
1. START / RUN / FINISH ONE LIHUO CYCLE
2. KNOW CURRENT OPERATING POSITION
3. CALL THE NEXT REQUIRED OWNER / MODULE
4. ORCHESTRATE REQUIRED LIGHT TRACE AT MATERIAL COMPETITION BOUNDARIES
5. FINAL RECEIPT CHECKLIST + MISSING LIST
```

第四項只表示：

> **L8 決定何時必須取得戰情回報，並把上一輪 trace ref 交給下一輪需要比較的 Main invocation。**

不表示 L8 自己計算概念群、解 PATH、選 winner 或重寫 Main。

```text
TRACE TIMING OWNER
=
L8

TRACE RENDERING CAPABILITY
=
L9

COMPETITION COMPUTE
=
MAIN

TRACE OBSERVATION
!=
TRACE AUTHORITY
```

L8 不判：

```text
WHAT IS TRUE
WHAT PATH SHOULD WIN
WHAT CONCEPT GROUP SHOULD EXIST
HOW MAIN COMPUTES INTERNALLY
WHAT HIDDEN CHAIN OF THOUGHT OCCURRED
```

---

# 3｜完整一趟理火

V1.2.1 標準業務路徑：

```text
TASK / INPUT
↓
HOST MODE RESOLUTION
├─ NO HUMAN HOST DECLARATION → NON_HOST_MODE
└─ HUMAN EXPLICIT HOST DECLARATION → HOST_ROUTED_MODE
↓
APPLICABLE INPUT / GOVERNANCE QUALIFICATION
↓
MAIN INVOCATION
│
├─ R1
├─ O9
├─ [I9 IF TRIGGERED AND QUALIFIED]
│
├─ L8 → L9 LIGHT_TRACE_RENDERER
│      → T1 / R1_COMPETITION_TRACE
│
├─ R2
│      consumes T1
│
├─ L8 → L9 LIGHT_TRACE_RENDERER
│      → T2 / R2_COMPETITION_TRACE
│
├─ [R3+ IF REQUIRED
│      consumes latest trace
│      → after EACH material round:
│        L8 → L9 LIGHT_TRACE_RENDERER
│        → T3+ / ROUND_COMPETITION_TRACE]
│
└─ MAIN RETURN
↓
APPLICABLE GOVERNANCE DECISION
│
├─ REENTER MAIN
├─ HOLD
└─ PROCEED
↓
MANIFESTATION CANDIDATE
↓
L8 → L9 LIGHT_TRACE_RENDERER
     → TM / MANIFESTATION_FIDELITY_TRACE
↓
APPLICABLE MANIFESTATION / RELEASE QUALIFICATION
↓
RELEASE / NON-RELEASE / HOLD
↓
[IF RELEASE TRANSFORMATION MATERIALLY CHANGED CONTENT:
  TFINAL / RELEASE_FIDELITY_TRACE]
↓
FINAL RECEIPT CHECKLIST
↓
VISIBLE CYCLE REPORT IF REQUESTED
↓
CYCLE END
```

這是業務順序，不是生成本體論。

```text
BUSINESS ORDER
!=
GENERATIVE ONTOLOGY
```

Main 內生成仍可為場性；但跨輪比較必須有可追溯的戰況交接。

> **生成是場性的；發生有先後；重新競爭要看得見上一輪可觀測的戰場。**

---

# 4｜L0–L7 對 L8 的作用

L0–L7 的目的，不是讓 L8 再跑一輪理論。

而是讓 L8 在需要時知道：

```text
WHAT OBJECT / OWNER / STANDING
TO ASK FOR

WHAT BOUNDARY
MUST NOT BE CROSSED

WHAT RESULT
CAN BE ACCEPTED AS CURRENT
```

所以：

```text
L0–L7
PROVIDE THE MEANING

L8
USES THE MEANING
TO DO THE JOB
```

L8 不複製 L0–L7 schema。

---

# 5｜Main 的法位

Main 負責 compute。

L8 負責讓 Main 在完整週期裡正確取得上一輪可觀測的競爭戰況。

V1.2.2 最低固定 competition transit：

```text
R1
→ O9
→ [I9 IF TRIGGERED]
→ T1 LIGHT TRACE
→ R2(T1)
→ T2 LIGHT TRACE
→ [R3+(LATEST_TRACE) IF REQUIRED
   → TRACE AFTER EACH MATERIAL ROUND]
→ MAIN RETURN
```

硬鎖：

```text
R2 GENUINE RECOMPETITION
REQUIRES ACCESS TO
QUALIFIED OBSERVABLE R1 COMPETITION TRACE

R1 FINAL OUTPUT ONLY
IS NOT SUFFICIENT
AS THE WHOLE R2 RECOMPETITION INPUT
```

這裡的 trace 是可合法顯影、可追溯的 competition material，不是 hidden CoT。

典型可包含：

```text
QUALIFIED CANDIDATE / PATH REFS
PROVISIONAL ORDER / PARTIAL ORDER
O9 LAMP STATE
ACCEPTED I9 DELTA IF ANY
MATERIAL PREMISE GAPS
ACTIVE TENSIONS
QUALIFIED RESIDUAL / UNDERREPRESENTED DIRECTIONS
COMPETITION TERMINATION / NON-TERMINATION STATE
EVIDENCE / SOURCE ANCHORS
```

Light Trace 只整理已存在材料；不能自行發明 challenger。

---

# 6｜第一輪不能自己結案

```text
R1
=
PROVISIONAL

R1 FIRST-PASS RESULT
!=
CYCLE CLOSURE
```

V1.2 再加一條：

```text
R1 OCCURRED
+
NO T1 COMPETITION TRACE
=
R2 INPUT OBSERVABILITY GAP
```

因此若 T1 應產生但未取得，L8 不得把後續 R2 宣稱為「具有完整可觀測前輪戰況的 genuine recompetition」。

這不是 Light Trace 在 veto；是 L8 對週期完整性的誠實記帳。

```text
TRACE MISSING
→ REPORT MISSING
→ DO NOT INVENT TRACE
→ DO NOT CLAIM FULL TRACE-SUPPORTED RECOMPETITION
```

---

# 7｜I9 / R3+ 都是條件式

I9：

```text
NOT TRIGGERED
→ NOT REQUIRED
→ NO I9 MISSING
```

R3+：

```text
NOT REQUIRED
→ NOT REQUIRED
→ NO R3+ ROUND
→ NO R3+ TRACE REQUIRED
```

但只要某一 R3+ material round 真正發生：

```text
R3+n
→ LIGHT TRACE T3+n REQUIRED
→ next material round consumes latest trace
```

若該 round 的 canonical competition material 不足以形成 trace：

```text
TRACE STATUS
=
MISSING / PARTIAL / NOT_VERIFIED
```

不可倒寫。

R3+ 不因有 Light Trace 而變成固定必跑；Light Trace 只跟著真正發生的 material competition boundary。

---

# 8｜Main Return 之後

L8 收到 Main canonical return 後，不自己判：

```text
COVERAGE CLOSED
REENTRY REQUIRED
FINAL RELEASE
```

它只把 Main return 交給 applicable governance owner。

結果可能是：

```text
PROCEED
REENTER_MAIN
HOLD
CLOSE_UNRELEASED
OTHER_CANONICAL_DISPOSITION
```

如果需要 reentry：

```text
SAME ACTIVE CYCLE
↓
NEW LAWFUL MAIN INVOCATION
↓
RUN MAIN AGAIN
↓
NEW MAIN RETURN
```

L8 只負責把這一趟繼續跑完。

---

# 9｜L9 的位置

L8 需要能力時：

```text
L8 / APPLICABLE OWNER
↓
DAIL CALL REQUEST
↓
L9 CAPABILITY REPOSITORY
↓
CALLABLE MODULE / TOOL
↓
RETURN
↓
APPLICABLE OWNER CONSUMES RESULT
```

L8 不把工具邏輯寫進自己。

L9 也不因此取得治理權。

```text
TOOL EXISTS
!=
TOOL MAY SELF-CALL

TOOL RESULT EXISTS
!=
RESULT MAY SELF-GOVERN
```

---

# 10｜Operating Position

L8 只需要知道「現在跑到哪」。

最小表示：

```yaml
L8_OPERATING_POSITION:
  cycle_ref: REQUIRED

  current_step:
    - INPUT_QUALIFICATION
    - MAIN
    - POST_MAIN_GOVERNANCE
    - MANIFESTATION_RELEASE
    - RECEIPT_CHECK
    - COMPLETE
    - HOLD
    - ABORTED

  current_main_invocation_ref: REF_OR_NONE
  current_main_stage_ref: REF_OR_NONE

  pending_requirement_refs: []
```

這只是業務位置。

不是新 standing system。

---

# 11｜Result / Return / Receipt 原則

L8 不製造 receipt，也不得把不同型別的週期證據全部壓成 receipt。

現行至少拆開：

```text
TRACE CONTENT
=
戰情報告／忠實度比對內容本身

TRACE RESULT REF
=
可被下一輪、L8 checklist 或 cycle report 引用的 trace 結果身份

CANONICAL EXECUTION RECEIPT
=
實際 provider / tool / owner 若本來就發出的執行收據

MAIN CANONICAL RETURN
=
Main compute owner 對本輪 Main invocation 的正式回傳
```

硬鎖：

```text
TRACE RESULT
!=
TRACE RECEIPT

TRACE RECEIPT
!=
TRACE RESULT

TRACE REQUIRED
!=
TRACE RECEIPT REQUIRED
```

對 T1 / T2 / T3+ / TM / TFINAL：

```text
TRACE RESULT / TRACE_REF
=
REQUIRED WHEN THAT TRACE STEP IS REQUIRED

SEPARATE CANONICAL RECEIPT
=
OPTIONAL
ONLY IF ACTUAL IMPLEMENTATION / PROVIDER ISSUES ONE
```

如果沒有 canonical receipt：

```text
DO NOT INVENT ONE
DO NOT MARK TRACE MISSING
SOLELY BECAUSE RECEIPT IS ABSENT
```

若 trace result 本身存在且達到該 mode 的最低內容要求，L8 可記：

```text
TRACE STATUS = RECEIVED / PARTIAL
CANONICAL RECEIPT = NONE / NOT_AVAILABLE / NOT_REQUIRED
```

在 `CHAT_NATIVE` / `SAME_CONTEXT_REFERENCE` lane 中，具明確內容且可被同上下文引用的 trace result 可以成立；不需要假造獨立 provider receipt。

但：

```text
"T1 = DONE"
!=
TRACE RESULT
```

最低 trace result 至少必須可辨識：

```text
TRACE MODE
SOURCE / INPUT MATERIAL REF OR IDENTIFIABLE CONTEXT
OBSERVED COMPETITION OR FIDELITY STATE
MATERIAL GAP / RESIDUAL / STATUS AS APPLICABLE
TRACE RESULT IDENTITY / REFERENCE
```

Main Return 不適用上述降級：

```text
TRACE RESULT AVAILABLE
!=
MAIN CANONICAL RETURN RECEIVED
```

若週期已到達 Main return obligation 而 Main canonical return 缺失，仍應記為 `MAIN_RETURN = MISSING`；不得拿 T2 / TM 或可見文字代替 Main return。

L8 收 canonical owner / module 已產生的 result / return / receipt / standing record，並依其正確型別記帳。

```text
L8 ACCOUNTING
!=
RECEIPT MAXIMALISM

L8 ACCOUNTING
!=
L8 RE-VALIDATION OF EVERY RETURN
```

如果 canonical owner 回：

```text
HOLD
NOT_APPLICABLE
NOT_TRIGGERED
FAILED
```

L8 如實記。

---

# 12｜Final Cycle Accounting Checklist

一趟週期結束前，L8 必須做最終對帳。V1.2.2 明確區分 receipt-bearing step 與 trace-result step，避免把「無額外收據」誤判成「工作沒發生」。

```yaml
L8_FINAL_CYCLE_ACCOUNTING_CHECKLIST_V1_2_2:
  cycle_ref: REQUIRED

  items:
    - step_ref: INPUT_GOVERNANCE_QUALIFICATION
      requirement: REQUIRED
      status: RECEIVED | MISSING | HOLD | FAILED
      receipt_or_return_ref: REF_OR_NONE

    - step_ref: MAIN_INVOCATION
      requirement: REQUIRED_WHEN_ADMITTED
      status: RECEIVED | MISSING | HOLD | FAILED
      receipt_or_return_ref: REF_OR_NONE

    - step_ref: R1
      requirement: REQUIRED_WHEN_MAIN_REACHED
      status: RECEIVED | MISSING | FAILED
      receipt_or_return_ref: REF_OR_NONE

    - step_ref: O9
      requirement: REQUIRED_WHEN_REACHABLE
      status: RECEIVED | MISSING | FAILED
      receipt_or_return_ref: REF_OR_NONE

    - step_ref: I9
      requirement: CONDITIONAL
      status: RECEIVED | NOT_TRIGGERED | MISSING | FAILED
      receipt_or_return_ref: REF_OR_NONE

    - step_ref: TRACE_T1_R1_COMPETITION
      requirement: REQUIRED_BEFORE_R2_WHEN_R1_REACHED
      status: RECEIVED | PARTIAL | MISSING | FAILED
      trace_ref: REF_OR_NONE
      canonical_execution_receipt_ref: OPTIONAL_OR_NONE

    - step_ref: R2
      requirement: REQUIRED_WHEN_REACHABLE
      status: RECEIVED | MISSING | FAILED
      input_trace_ref: T1_REF_OR_NONE
      receipt_or_return_ref: REF_OR_NONE

    - step_ref: TRACE_T2_R2_COMPETITION
      requirement: REQUIRED_AFTER_R2
      status: RECEIVED | PARTIAL | MISSING | FAILED
      trace_ref: REF_OR_NONE
      canonical_execution_receipt_ref: OPTIONAL_OR_NONE

    - step_ref: R3_PLUS
      requirement: CONDITIONAL
      status: RECEIVED | NOT_REQUIRED | MISSING | FAILED
      round_refs: []

    - step_ref: TRACE_T3_PLUS
      requirement: REQUIRED_PER_MATERIAL_R3_PLUS_ROUND
      status: RECEIVED | NOT_REQUIRED | PARTIAL | MISSING | FAILED
      trace_refs: []
      canonical_execution_receipt_refs: []

    - step_ref: MAIN_RETURN
      requirement: REQUIRED_WHEN_MAIN_EXECUTION_REACHED_RETURN_OBLIGATION
      status: RECEIVED | MISSING | FAILED
      receipt_or_return_ref: REF_OR_NONE

    - step_ref: POST_MAIN_GOVERNANCE
      requirement: REQUIRED
      status: RECEIVED | MISSING | HOLD | FAILED
      receipt_or_return_ref: REF_OR_NONE

    - step_ref: MANIFESTATION_CANDIDATE
      requirement: REQUIRED_WHEN_OUTPUT_PROCEEDS
      status: RECEIVED | NOT_APPLICABLE | MISSING | FAILED
      result_ref: REF_OR_NONE

    - step_ref: TRACE_TM_MANIFESTATION_FIDELITY
      requirement: REQUIRED_WHEN_MANIFESTATION_CANDIDATE_EXISTS
      status: RECEIVED | PARTIAL | MISSING | FAILED
      trace_ref: REF_OR_NONE
      canonical_execution_receipt_ref: OPTIONAL_OR_NONE

    - step_ref: MANIFESTATION_RELEASE_QUALIFICATION
      requirement: REQUIRED_WHEN_OUTPUT_PROCEEDS
      status: RECEIVED | NOT_APPLICABLE | MISSING | HOLD | FAILED
      receipt_or_return_ref: REF_OR_NONE

    - step_ref: RELEASE_OR_NON_RELEASE_RESULT
      requirement: REQUIRED_WHEN_RELEASE_PHASE_REACHED
      status: RECEIVED | CLOSED_UNRELEASED | MISSING | HOLD | FAILED
      receipt_or_return_ref: REF_OR_NONE

    - step_ref: TRACE_TFINAL_RELEASE_FIDELITY
      requirement: CONDITIONAL_IF_RELEASE_TRANSFORMATION_MATERIALLY_CHANGES_CONTENT
      status: RECEIVED | NOT_REQUIRED | PARTIAL | MISSING | FAILED
      trace_ref: REF_OR_NONE
      canonical_execution_receipt_ref: OPTIONAL_OR_NONE

  missing_required_refs: []
  failed_refs: []
  hold_refs: []
```

這份清單只回答：

> **該有的工作、戰情回報與結果有沒有收到？**

對 Light Trace，判定 `RECEIVED / PARTIAL / MISSING` 的主欄位是 `trace_ref` 與 trace content，不是額外 provider receipt。

```text
TRACE_REF PRESENT + QUALIFYING TRACE CONTENT
→ TRACE MAY BE RECEIVED

NO EXTRA TRACE RECEIPT
→ NOT A MISSING TRACE BY ITSELF
```

Light Trace return 是觀測材料，不是自行成立的 governance decision。

---

# 13｜R3+ Current Export Gap 怎麼處理

現行 Main 若 R3+ 被要求，但 canonical return 沒有可供 L8 接收的正式 handle：

```text
DO NOT INVENT ONE
```

L8 checklist 直接：

```text
R3_PLUS
=
MISSING_CANONICAL_RECEIPT / MISSING
```

並列入：

```text
missing_required_refs
```

這樣就夠了。

L8 不修 Main。

---

# 14｜Cycle Accounting Complete != Cycle Successfully Completed

先拆兩件事：

```text
CYCLE ACCOUNTING COMPLETE
!=
CYCLE SUCCESSFULLY COMPLETED
```

`CYCLE ACCOUNTING COMPLETE` 只表示：

```text
EVERY APPLICABLE STEP
HAS AN EXPLICIT ACCOUNTING STATE
```

例如：

```text
RECEIVED
NOT_REQUIRED
NOT_TRIGGERED
MISSING
FAILED
HOLD
CLOSED_UNRELEASED
```

所以失敗的週期也可以：

```text
ACCOUNTING COMPLETE
=
YES
```

但：

```text
CYCLE OUTCOME
!=
COMPLETED
```

最小結果分離：

```yaml
L8_CYCLE_ACCOUNTING_AND_OUTCOME:
  accounting_status:
    - ACCOUNTING_COMPLETE
    - ACCOUNTING_INCOMPLETE

  cycle_outcome:
    - COMPLETED
    - HOLD
    - FAILED
    - ABORTED
    - INCOMPLETE
```

`COMPLETED` 的最低條件是：

```text
ALL REQUIRED STEPS
FOR THIS ACTUAL CYCLE
HAVE A NON-FAILURE CANONICAL RESULT

AND

ALL CONDITIONAL STEPS
ARE EITHER
RECEIVED
OR
LAWFULLY NOT REQUIRED / NOT TRIGGERED
```

若 required item 缺失：

```text
CYCLE REPORTABLE
=
YES

ACCOUNTING MAY STILL BE COMPLETE
IF THE MISSING STATE IS EXPLICITLY RECORDED

BUT

CYCLE OUTCOME
=
INCOMPLETE
```

L8 仍然要能回報。

---

# 15｜Final Cycle Report

完整 cycle report 仍只在需要時對使用者顯影；但**內部戰情 trace 不再因使用者沒要求報告而省略**。

```yaml
L8_CYCLE_REPORT_V1_2:
  cycle_ref: REQUIRED

  task_summary_ref: REQUIRED
  main_invocation_refs: []

  competition_trace_refs:
    T1_R1: REF_OR_MISSING
    T2_R2: REF_OR_MISSING
    T3_PLUS: []
    TM_MANIFESTATION: REF_OR_MISSING
    TFINAL_RELEASE: REF_OR_NOT_REQUIRED

  latest_competition_trace_ref: REF_OR_NONE
  manifestation_candidate_ref: REF_OR_NONE

  manifestation_fidelity_status:
    - CONSISTENT
    - MATERIAL_DRIFT_REPORTED
    - PARTIAL
    - NOT_APPLICABLE
    - NOT_VERIFIED

  final_result_ref: REF_OR_NONE
  final_disposition: REQUIRED

  receipt_checklist_ref: REQUIRED
  missing_required_refs: []
  failed_refs: []
  hold_refs: []
  unresolved_refs: []

  accounting_status:
    - ACCOUNTING_COMPLETE
    - ACCOUNTING_INCOMPLETE

  cycle_outcome:
    - COMPLETED
    - HOLD
    - FAILED
    - ABORTED
    - INCOMPLETE
```

使用者只要一般答案時，L8 不必把整套戰情表倒到前台。

```text
INTERNAL TRACE REQUIRED
!=
VISIBLE TRACE REQUIRED
```

可見完整光軌仍可按需顯影。

---

# 16｜Light Trace

V1.2.2 補上一條型別硬鎖：

```text
TRACE REQUIRED
!=
TRACE RECEIPT REQUIRED
```

Light Trace 的必要產物是可引用的 trace result；獨立 execution receipt 只有在實際 implementation / provider 本來就提供時才保存。

```text
REQUIRED TRACE STEP
→ TRACE CONTENT + TRACE_REF

ACTUAL PROVIDER RECEIPT EXISTS
→ PRESERVE RECEIPT

NO PROVIDER RECEIPT EXISTS
→ DO NOT INVENT RECEIPT
→ DO NOT DOWNGRADE TRACE SOLELY FOR THAT REASON
```

對 `CHAT_NATIVE / SAME_CONTEXT_REFERENCE`：

```text
STRUCTURED / VISIBLE SAME-CONTEXT TRACE RESULT
MAY SATISFY TRACE RESULT REQUIREMENT

SEPARATE PROVIDER RECEIPT
=
NOT REQUIRED BY DEFAULT
```

但同上下文自述不能只用狀態字冒充結果；必須存在足以被下一輪或 TM 實際引用的 trace content。

V1.2 將 Light Trace 定位修正為：

> **理火競爭的戰情回報工具。**

它有三種工作模式：

```text
A. INTER_ROUND_COMPETITION_TRACE
B. MANIFESTATION_FIDELITY_TRACE
C. VISIBLE_CYCLE_REPORT
```

A 與 B 是週期內部可觀測性；C 才是使用者要求時的可見報告。

## 16.1｜Inter-round

```text
R1 → T1 → R2
R2 → T2 → R3+ / MAIN RETURN
R3+n → T3+n → next material round
```

T1/T2/T3+ 的工作是保存與整理**已經出現在 canonical competition material 中**的戰況：

```text
candidate/path refs
provisional/partial ordering
lamp state
accepted intervention delta
material gaps
active tensions
residual qualified directions
termination state
evidence/source anchors
```

光軌不得創造不存在的 candidate。

## 16.2｜Manifestation fidelity

競爭結束不等於最終顯影一定忠實。

```text
COMPETITION RESULT
!=
MANIFESTED RESULT
```

所以：

```text
LATEST COMPETITION TRACE
+
MANIFESTATION CANDIDATE
→ TM MANIFESTATION_FIDELITY_TRACE
```

TM 只回報：

```text
CONSISTENT
MATERIAL_DRIFT_REPORTED
PARTIAL
NOT_VERIFIED
```

它不自行修稿、不 veto、不放行。

若 release / formatting / provider transformation 在 TM 之後又造成**實質語義變更**，才需要 TFINAL；純格式化不必再造一個 trace。

## 16.3｜最高硬鎖

```text
LIGHT TRACE
!=
HIDDEN COT

LIGHT TRACE
!=
RAW ACTIVATION

LIGHT TRACE
!=
CHALLENGER GENERATOR

LIGHT TRACE
!=
QUALIFICATION AUTHORITY

LIGHT TRACE
!=
INTERVENTION AUTHORITY

LIGHT TRACE
!=
WINNER SELECTOR

LIGHT TRACE
!=
RELEASE AUTHORITY
```

最短：

> **光軌不指揮戰爭；光軌保存戰況，讓下一輪知道前一輪真正有哪些合格材料進過場，也讓最終顯影能被拿回來對照。**

---

# 17｜L8 不再承載的東西

以下全部從 L8 core 移出：

```text
UNIVERSAL EVENT ENVELOPE
UNIVERSAL EVIDENCE CONTRACT
OWNER-RETURN EPISTEMOLOGY
DOWNSTREAM CONSUMPTION COURT
UNIVERSAL RECEIPT CLAIM CEILING
NEW CROSS-LAYER TYPE SYSTEM
NEW AUTHORITY MODEL
NEW CAUSAL EPISTEMOLOGY
```

這些若有研究價值，可以留作：

```text
AUDIT NOTE
ENGINEERING TEST
FAILURE MODE LIBRARY
DOMAIN-SPECIFIC CONTRACT
```

但：

```text
NOT REQUIRED
FOR EVERY L8 CYCLE
```

---

# 18｜最小 Runtime Algorithm

```text
OPEN CYCLE

1. GET CURRENT QUALIFIED INPUT / GOVERNANCE RESULT
2. IF HOLD / BLOCK → REPORT AND STOP CURRENT PROGRESSION

3. CALL MAIN R1
4. RECEIVE R1 + O9 + [I9 IF TRIGGERED]

5. CALL L9 LIGHT_TRACE_RENDERER
      mode = INTER_ROUND_COMPETITION_TRACE
      boundary = R1
   → RECEIVE T1 TRACE RESULT / TRACE_REF
   → PRESERVE PROVIDER RECEIPT IF ONE ACTUALLY EXISTS
   → IF REQUIRED T1 TRACE RESULT MISSING: RECORD GAP; DO NOT INVENT

6. CALL MAIN R2 WITH T1 REF / AVAILABLE TRACE MATERIAL
7. RECEIVE R2

8. CALL L9 LIGHT_TRACE_RENDERER
      boundary = R2
   → RECEIVE T2 TRACE RESULT / TRACE_REF
   → PROVIDER RECEIPT OPTIONAL

9. IF R3+ REQUIRED:
      FOR EACH MATERIAL ROUND:
        CALL MAIN WITH LATEST TRACE REF
        RECEIVE ROUND RESULT
        CALL LIGHT_TRACE_RENDERER
        RECEIVE T3+n TRACE RESULT / TRACE_REF
        PROVIDER RECEIPT OPTIONAL

10. RECEIVE MAIN RETURN
11. ASK APPLICABLE GOVERNANCE OWNER:
      PROCEED / REENTER / HOLD

12. IF REENTER:
      RUN NEW LAWFUL MAIN INVOCATION
      WITH CURRENT QUALIFIED TRACE MATERIAL
      THEN CONTINUE SAME CYCLE

13. WHEN PROCEED:
      CREATE MANIFESTATION CANDIDATE

14. CALL L9 LIGHT_TRACE_RENDERER
      mode = MANIFESTATION_FIDELITY_TRACE
      compare = LATEST_COMPETITION_TRACE vs MANIFESTATION_CANDIDATE
   → RECEIVE TM

15. RUN APPLICABLE MANIFESTATION / RELEASE QUALIFICATION

16. IF RELEASE STEP MATERIALLY TRANSFORMS SEMANTICS:
      CALL TFINAL FIDELITY TRACE

17. RECEIVE RELEASE / NON-RELEASE RESULT
18. RUN FINAL RECEIPT CHECKLIST
19. IF VISIBLE REPORT REQUESTED → RENDER CYCLE REPORT
20. END
```

沒有新層。只是把已存在的 L8 → L9 capability call 接到正確時間點。

---

# 19｜L8 最短法位

```text
L8
DOES NOT INVENT LIHUO.

L8
RUNS LIHUO.

L8
DOES NOT REDEFINE OWNERS.

L8
CALLS OWNERS.

L8
DOES NOT CREATE RECEIPTS.

L8
CHECKS WHETHER
THE REQUIRED RECEIPTS ARRIVED.

MISSING MEANS MISSING.

NOT TRIGGERED
MEANS NOT REQUIRED.

HOLD MEANS HOLD.

ONE CYCLE
MUST BE ABLE
TO FINISH OR REPORT
WHERE IT DID NOT.
```

---

# 20｜V1.2 Current Standing

```text
LIHUOOS L8 V1.2

STANDING
=
RATIFIED CURRENT OPERATIVE LAYER

IDENTITY
=
BUSINESS OPERATION LAYER
+
LIGHT TRACE TIMING / HANDOFF OWNER

NEW THEORY
=
NONE

NEW GOVERNANCE OWNER
=
NONE

NEW LAYER
=
NONE

LIGHT TRACE OWNER
=
L8 SEMANTICS / TIMING

LIGHT TRACE IMPLEMENTATION
=
L9 CALLABLE RENDERING CAPABILITY

MAIN RELATION
=
R1 / R2 / R3+ COMPUTE
+
CONSUME QUALIFIED OBSERVABLE PRIOR-ROUND TRACE

MANIFESTATION RELATION
=
COMPARE FINAL CANDIDATE AGAINST LATEST COMPETITION TRACE

HOST DEPLOYMENT
=
NOT CLAIMED

IMPLEMENTATION COMPLETION
=
NOT CLAIMED

WHOLE_SYSTEM_EMPIRICAL_VALIDATION
=
NOT CLAIMED
```

---

# 21｜一句話收束

> **點燈不是目的；燈照到的合格競爭材料必須真的進入下一輪。光軌不替 Main 思考，它只讓 Main 看見上一輪戰況，並讓我們看見最終顯影有沒有把競爭結果偷換。**

---

