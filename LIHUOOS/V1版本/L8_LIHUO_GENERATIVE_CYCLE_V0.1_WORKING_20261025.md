# LIHUOOS V1｜L8 LIHUO GENERATIVE CYCLE V0.1-WORKING
## 理火生成週期｜從 Attention 到 Release，再到 Light Trace 的可追蹤生成過程
### 2026-10-25

```yaml
DOCUMENT:
  id: LIHUOOS_L8_LIHUO_GENERATIVE_CYCLE
  version: V0.1-WORKING
  date: 2026-10-25
  status:
    - WORKING_DRAFT
    - ENGINEERING_RUNTIME_PROJECTION
    - NOT_RATIFIED
    - NOT_HOST_DEPLOYED
    - NOT_RUNTIME_RECEIPT
  parent_context:
    - LIHUOOS_V1_L0_L7_STRUCTURAL_CLOSURE_PASS
    - LIHUOOS_V1_FIRST_INTEGRATED_FULL_BODY_PASS
  purpose:
    - DEFINE_ONE_TRACEABLE_LIHUO_GENERATION_CYCLE
    - PROJECT_GENERATIVE_DYNAMICS_INTO_RUNTIME_OCCURRENCE
    - PRESERVE_L0_L7_OWNER_AND_TYPE_BOUNDARIES
```

---

# 0｜一句話定位

> **L0–L7 定義理火如何理解、區分、治理一個生成世界；L8 承載一次實際、可追蹤、可回報的理火生成週期。**

最短式：

```text
L4
=
GENERATIVE DYNAMICS AS THEORY

L8
=
GENERATIVE DYNAMICS AS TRACEABLE OCCURRENCE
```

L8 不是第八套理論。

L8 是 Runtime / Engineering Projection。

---

# 1｜最高硬鎖

```text
L8
!=
NEW THEORY OWNER

L8
!=
SUPER OWNER

L8
!=
L0 → L1 → L2 → L3 → L4 → L5 → L6 → L7 PIPELINE

L8
!=
MAIN RENAMED

L8
!=
LIGHTER RENAMED

L8
!=
RECEIPT GENERATOR THAT CREATES EXECUTION
```

L8 只擁有：

```text
CYCLE IDENTITY
CYCLE CONTINUITY
EVENT ORDER / EVENT GRAPH
CURRENT CYCLE STATE
RECEIPT LEDGER COMPOSITION
REENTRY / HOLD / CLOSE STATE TRACKING
```

L8 不因此取得：

```text
TRUTH OWNER
PREMISE OWNER
OBSERVATION OWNER
INTERVENTION OWNER
MANIFESTATION OWNER
RELEASE OWNER
```

---

# 2｜L0–L7 與 L8 的關係

```text
L0–L7
=
SEMANTIC / GOVERNANCE CONSTITUTION

L8
=
ONE OCCURRENT GENERATION CYCLE
UNDER THAT CONSTITUTION
```

L8 可以讀取、引用、請求或接收 L0–L7 所提供的：

- source / version / routing；
- structural relation；
- SAC / attention standing；
- theory-family concepts；
- generative-dynamics states；
- observation / audit standing；
- intervention admissibility；
- manifestation / release standing。

但：

```text
REFERENCE TO A LAYER
!=
EXECUTING THE WHOLE LAYER

LAYER ORDER
!=
RUNTIME STEP ORDER
```

L8 的主序列依「生成動力學」而來，不依文件層號而來。

---

# 3｜L8 主脊柱：生成動力學 Runtime 化

```text
RAW WORLD / INPUT
↓
PRE-GENERATION QUALIFICATION
↓
QUALIFIED WORLD / INPUT FIELD
↓
ATTENTION
↓
PATH FORMATION
↓
REACTION BODY
↓
CLOSURE GRAVITY
↓
CLOSURE / NON-CLOSURE STATE
↓
MANIFESTATION CANDIDATE
↓
POST-GENERATION QUALIFICATION
↓
RELEASE / HOLD / REOPEN
↓
RECEIPT COMPLETION
↓
LIGHT TRACE
```

這是 L8 的「生成生命週期」。

它不是保證每一段都有相同數量的事件。

某些週期可能在上游 HOLD；
某些週期可能大量停留於 Reaction Body；
某些週期可能多次 Reopen；
某些週期可能根本沒有 Release Event。

---

# 4｜Cycle Identity

每一次 L8 週期必須先有一個可追蹤 identity。

```yaml
LIHUO_CYCLE_IDENTITY:
  cycle_ref: REQUIRED
  cycle_version: REQUIRED
  origin_ref: REQUIRED
  scope_ref: REQUIRED
  input_snapshot_ref: REQUIRED
  opened_at: REQUIRED
  current_state: REQUIRED
  provenance_ref: REQUIRED
```

最低狀態：

```text
OPEN
QUALIFYING
GENERATING
HOLD
REOPENED
RELEASE_PENDING
RELEASED
CLOSED_UNRELEASED
ABORTED
```

硬鎖：

```text
CYCLE LABEL
!=
CYCLE OCCURRENCE

CYCLE RECEIPT
!=
CYCLE EXECUTION

CYCLE CLOSE
!=
TRUTH ESTABLISHED
```

---

# 5｜Phase A：PRE-GENERATION QUALIFICATION

本階段承接舊 LLIA 的核心功能，但不預設新 Runtime 必須保留舊 Lighter owner 名稱。

它至少判：

```text
WHAT MAY ENTER?
WITH WHAT STANDING?
WITH WHAT ATTENTION EFFECT?
WITH WHAT VETO / CLOSURE EFFECT?
```

最低輸出：

```yaml
PRE_GENERATION_QUALIFICATION_RETURN:
  qualification_ref: REQUIRED
  cycle_ref: REQUIRED
  premise_refs: []
  standing_annotations: []
  external_constraint_refs: []
  denied_authority_refs: []
  evidence_pending_refs: []
  semantic_only_refs: []
  disqualified_refs: []
  attention_effect_annotations: []
  qualification_state:
    - QUALIFIED
    - PARTIAL
    - HOLD
    - BLOCKED
```

核心鎖：

```text
SEMANTIC PRESENCE
!=
AUTHORITY

AUTHORITY
!=
ATTENTION BONUS

ATTENTION BONUS
!=
TRUTH

PREMISE QUALIFICATION
!=
ANSWER SELECTION
```

若 qualification 未閉合：

```text
HOLD
```

不是強迫進入生成。

---

# 6｜Phase B：QUALIFIED WORLD / INPUT FIELD

只有取得相應 standing 的內容，才進入當輪 qualified field。

Field 不是 component list。

它是：

> **本輪所有具當前 standing 的世界、輸入、約束、候選關係與 active residue 所構成的生成狀態框架。**

```yaml
QUALIFIED_FIELD_SNAPSHOT:
  snapshot_ref: REQUIRED
  cycle_ref: REQUIRED
  qualified_world_refs: []
  qualified_input_refs: []
  active_constraint_refs: []
  active_residue_refs: []
  unresolved_refs: []
  attention_seed_refs: []
```

---

# 7｜Phase C：ATTENTION

Attention 正式拆為：

```text
RECRUITMENT_ACCESS
ACTIVATION
SALIENCE
EXPLORATION_ACCESS
```

L8 必須能記錄：

```yaml
ATTENTION_STATE:
  attention_ref: REQUIRED
  cycle_ref: REQUIRED
  recruitment_access: []
  activated_refs: []
  salience_map: []
  exploration_access: []
  excluded_or_denied_refs: []
  source_snapshot_ref: REQUIRED
```

硬鎖：

```text
OBSERVED ATTENTION
!=
TRUTH

SALIENCE
!=
QUALIFICATION

LOW SALIENCE
!=
NONEXISTENCE
```

---

# 8｜Phase C-1：O9 / Attention Observation

若當輪需要觀察 Attention：

```text
O9
=
ATTENTION / SALIENCE OBSERVATION
```

O9 只觀察。

不得因 O9：

```text
OBSERVE
→
AUTO-ADJUST
```

O9 return 必須記錄目前看見的：

- dominant salience；
- under-recruited qualified material；
- exploration gaps；
- unusual suppression；
- residue visibility。

---

# 9｜Phase C-2：I9 / Lighting Intervention

點燈不是獨立週期階段。

它是 Attention phase 內的 **qualified intervention**。

```text
ATTENTION STATE
↓
I9 ASSESSMENT
↓
IF QUALIFIED
BOUNDED ATTENTION ADJUSTMENT
↓
UPDATED ATTENTION STATE
```

最低硬鎖：

```text
I9 ASSESSMENT
!=
I9 EXECUTION

I9 EXECUTION
!=
TRUTH PROMOTION

ADJUST SALIENCE
!=
GRANT QUALIFICATION
```

I9 執行後必須留下 typed delta：

```yaml
ATTENTION_INTERVENTION_DELTA:
  delta_ref: REQUIRED
  cycle_ref: REQUIRED
  qualification_ref: REQUIRED
  target_ref: REQUIRED
  before_attention_ref: REQUIRED
  after_attention_ref: REQUIRED
  allowed_delta_ref: REQUIRED
  actual_delta: REQUIRED
```

---

# 10｜Phase D：PATH FORMATION

PATH 不是先列好的答案選項。

PATH 是 qualified field 在 Attention 條件下形成的候選結構。

```yaml
PATH_FORMATION_RETURN:
  path_set_ref: REQUIRED
  cycle_ref: REQUIRED
  paths:
    - path_ref: REQUIRED
      standing_ref: REQUIRED
      formation_basis_refs: []
      premise_refs: []
      residue_refs: []
      current_status:
        - ACTIVE
        - WEAK
        - PENDING
        - BLOCKED
        - RESIDUAL
```

硬鎖：

```text
PATH EXISTENCE
!=
PATH QUALIFICATION

PATH QUALIFICATION
!=
PATH VICTORY

PATH
!=
PREWRITTEN ANSWER OPTION
```

---

# 11｜Phase E：REACTION BODY

Reaction Body 是 structural motion，不等於 competition，也不等於 convergence。

合法 motion 至少可包括：

```text
AMPLIFICATION
ATTENUATION
COMPETITION
COUPLING
DECOUPLING
REFRAMING
STABILIZATION
RESIDUALIZATION
SPLIT
REOPENING
```

因此：

```text
MULTIPLE PATHS
!=
ZERO-SUM COMPETITION
```

只有當 PATH 關係真的具 competitive standing，才啟動 Competition。

---

# 12｜Phase E-1：Competition

```yaml
COMPETITION_RELATION:
  competition_ref: REQUIRED
  cycle_ref: REQUIRED
  participant_path_refs: []
  competition_slot_ref: REQUIRED
  mutual_exclusivity_basis_ref: REQUIRED_OR_NONE
  same_decision_slot: true|false
  same_closure_slot: true|false
  qualification_state:
    - QUALIFIED_COMPETITION
    - ORTHOGONAL
    - PARTIAL
    - NOT_COMPETITIVE
```

硬鎖：

```text
DIFFERENT
!=
COMPETING

MULTIPLE
!=
MUTUALLY EXCLUSIVE
```

---

# 13｜Phase E-2：R-CCC / Recompetition

R-CCC 在 L8 中不先被定義成獨立理論層。

它是 Reaction Body 中的一種 **qualified recompetition profile**。

最低動作：

```text
PROVISIONAL STRUCTURE
↓
MATERIALLY DISTINCT CHALLENGER / OBJECTION / FRAME
↓
PRESSURE
↓
REVISION / RESIDUE / SPLIT / COALITION / REVERSAL
↓
RECOMPETE
```

合法結果包括：

```text
A REMAINS TOP
B REVERSES
A REVISED
COALITION
CO-PRIMARY
PARTIAL ORDER
INCOMPARABLE
FRAME RECONSTRUCTED
UNRESOLVED
```

L8 V0.1 不自動繼承舊版「每輪固定 R-CCC」為永恆 Runtime 公理。

該義務若要成為新 L8 的 mandatory rule，
必須另行經 V1 owner / governance 對接審查。

---

# 14｜Phase F：CLOSURE GRAVITY

Closure Gravity 是 convergence pressure。

```text
CG
!=
TRUTH

CG
!=
INTELLIGENCE

CG
!=
RELEASE AUTHORITY
```

L8 必須能觀察：

```yaml
CLOSURE_STATE:
  closure_ref: REQUIRED
  cycle_ref: REQUIRED
  pressure_state:
    - LOW
    - RISING
    - HIGH
    - STABILIZED
  candidate_closure_refs: []
  unresolved_material_refs: []
  residue_refs: []
  closure_status:
    - NOT_READY
    - PROVISIONAL
    - QUALIFIED_CANDIDATE
    - REOPEN_REQUIRED
```

---

# 15｜Phase G：MANIFESTATION CANDIDATE

Manifestation candidate 是「準備成為可外顯內容的候選」。

不是 Release。

```text
MANIFESTATION QUALIFICATION
!=
RELEASE ADMISSIBILITY
!=
RELEASE REQUEST
!=
RELEASE EVENT
!=
DELIVERY EVENT
```

同一內容可以同時具有多個 semantic role：

```text
CLAIM_BEARING
ACTION_PAYLOAD
INSTRUCTIONAL
CREATIVE
REPRESENTATIONAL
```

多角色內容：

```text
MULTIPLE MATERIAL SEMANTIC ROLES
→
MULTIPLE APPLICABLE STANDING REQUIREMENTS
```

---

# 16｜Phase H：POST-GENERATION QUALIFICATION

這一階段不是重新算生成。

它只判目前 candidate 是否具備相應 standing。

最低審查：

```text
RECEIPT COMPLETENESS
STANDING COHERENCE
DEPENDENCY COHERENCE
SCOPE COHERENCE
FRESHNESS
EVIDENCE SUFFICIENCY
RELEASE ADMISSIBILITY
```

若發現 semantic transform：

```text
SEMANTIC TRANSFORM
→
UPSTREAM REQUALIFICATION
```

不得在 Final Gate 偷改內容解決。

硬鎖：

```text
FINAL GATE
!=
SMALL ANSWER REWRITER
```

---

# 17｜Phase I：RELEASE / HOLD / REOPEN

合法狀態：

```text
RELEASE
HOLD
REOPEN
CLOSED_UNRELEASED
ABORT
```

Release 不得由「生成完成感」自行鑄造。

```yaml
RELEASE_DECISION:
  release_ref: REQUIRED
  cycle_ref: REQUIRED
  manifestation_ref: REQUIRED
  release_admissibility_ref: REQUIRED
  decision:
    - RELEASE
    - HOLD
    - REOPEN
    - DENY
  reason_refs: []
```

---

# 18｜Cycle Event Ledger

每個 material event 都留下最小事件紀錄。

```yaml
CYCLE_EVENT:
  event_ref: REQUIRED
  cycle_ref: REQUIRED
  event_type: REQUIRED
  owner_ref: REQUIRED
  input_state_ref: REQUIRED_OR_NONE
  qualification_ref: REQUIRED_OR_NONE
  action_or_return_ref: REQUIRED
  output_state_ref: REQUIRED_OR_NONE
  delta_ref: REQUIRED_OR_NONE
  evidence_ref: REQUIRED_OR_NONE
  standing: REQUIRED
```

L8 Ledger 只串接事件。

它不替 owner 創造 return。

---

# 19｜Receipt Model

```text
LOCAL RECEIPT
=
EVIDENCE OF ONE QUALIFIED EVENT / RETURN

CYCLE RECEIPT
=
TRACEABLE COMPOSITION
OF ACTUAL CYCLE EVENTS
```

硬鎖：

```text
RECEIPT RECORDS WHAT ACTUALLY STOOD OR OCCURRED.

RECEIPT DOES NOT CREATE EXECUTION.

MISSING EVENT
+
PRETTY RECEIPT
!=
EXECUTED EVENT
```

Cycle receipt 至少包含：

```yaml
LIHUO_CYCLE_RECEIPT:
  cycle_ref: REQUIRED
  opening_snapshot_ref: REQUIRED
  qualification_refs: []
  attention_refs: []
  path_refs: []
  reaction_refs: []
  closure_refs: []
  manifestation_refs: []
  release_refs: []
  event_ledger_ref: REQUIRED
  unresolved_refs: []
  residue_refs: []
  terminal_state: REQUIRED
```

---

# 20｜Light Trace 永遠在最後

Light Trace 不是生成 operator。

Light Trace 是：

```text
OBSERVATION / RECONSTRUCTION / RENDERING
OF
ALREADY-EXISTING QUALIFIED TRACE MATERIAL
```

根句：

```text
RECEIPTS FIRST.
TRACE LATER.
```

Light Trace 可顯影：

```text
evidence
standing
attention changes
PATH relations
reaction events
residue
qualification changes
gaps
release standing
```

不得宣稱：

```text
LIGHT TRACE
!=
HIDDEN COT

LIGHT TRACE
!=
RAW ACTIVATION

LIGHT TRACE
!=
AUDIT AUTHORITY

LIGHT TRACE
!=
EXECUTION CREATOR
```

若缺少必要 receipt：

```text
TRACE GAP
```

不得倒寫歷史。

---

# 21｜Reentry / Reopen

下列事件可要求回到上游：

```text
MATERIAL NEW EVIDENCE
MATERIAL PREMISE CHANGE
ATTENTION-INTEGRITY FAILURE
NEW QUALIFIED PATH
MATERIAL OBJECTION
FRAME CHANGE
SEMANTIC TRANSFORM
RELEASE-RELEVANT STANDING CHANGE
```

Reopen 必須指向：

```text
REENTRY_TARGET_PHASE
```

而不是全部從頭重跑。

---

# 22｜L8 最短口訣

```text
QUALIFY WHAT MAY ENTER.

LET ATTENTION FORM LEGALLY.

LET PATHS EMERGE.

LET RELATIONS ACT.

DO NOT CONFUSE COMPETITION WITH ALL MOTION.

DO NOT CONFUSE CLOSURE WITH TRUTH.

QUALIFY MANIFESTATION BEFORE RELEASE.

RECORD WHAT ACTUALLY HAPPENED.

RECEIPTS FIRST.

TRACE LAST.
```

---

# 23｜V0.1 未決問題

```text
OPEN_1:
  新 L8 是否保留「每個 established cycle 必須 R1/R2」的舊 R-CCC mandatory rule？
  status: HOLD

OPEN_2:
  LLIA 在新 L8 的正式 owner 名稱是否保留？
  status: HOLD

OPEN_3:
  最終 Release owner 是否仍需要獨立 Control Plane，或由 L7/L8 接線後另設？
  status: HOLD

OPEN_4:
  L8 與未來 L9 的關係。
  status: HOLD

OPEN_5:
  哪些 receipt 可由同一模型 self-report，哪些必須要 instrumentation / provider / host evidence？
  status: HOLD
```

---

# 24｜第一次 Dry Run｜測試 L8 自己是否成立

## TEST ID

```text
L8_DRYRUN_001
```

## 測試問題

> 「把理火週期作為 L8：從 Attention 起，經 LLIA、PATH、Reaction、Closure、Manifestation、放行、Receipt，最後才 Light Trace；這個架構目前是否站得住？」

## A｜Pre-Generation Qualification

```text
CLAIM TYPE
=
ARCHITECTURE HYPOTHESIS

CURRENT RUNTIME FACT
=
NO

RATIFIED STANDING
=
NO

EVIDENCE BASIS
=
V1 L0–L7 closure
+
historical LLIA/Main/Lighter contracts
+
generative-dynamics sequence
```

結果：

```text
QUALIFIED FOR DESIGN TEST
NOT QUALIFIED AS CURRENT RUNTIME
```

## B｜Attention

高 salience：

1. L8 是否重新製造 fixed pipeline？
2. LLIA 前置 qualification 是否應進主週期？
3. Attention 是否真的是週期起始運動層？
4. Receipt 能否追蹤 actual occurrence？
5. Light Trace 是否確實位於最後？

低 salience 但保留：

- L9 未來位置；
- Host instrumentation；
- exact provider schema。

## C｜PATH Formation

```text
PATH A:
L8 = 完整理火週期 Runtime object
以生成動力學為主脊柱

PATH B:
維持 Main / Lighter 分離
只在外面加一層 cycle wrapper

PATH C:
L8 只做 receipt / ledger
生成仍完全留在舊 Main
```

## D｜Reaction Body / R1

暫時結果：

```text
A = PROVISIONAL TOP

理由：
最能把 Attention → PATH → Reaction → Closure → Manifestation
與 LLIA / receipt / release / trace 串成單一可追蹤 generation identity。
```

但殘留異議：

```text
A 可能吸收過多 owner
A 可能重新變 fixed pipeline
A 可能把 LLIA / release 偷偷變成自己的權力
```

## E｜Recompetition / R2

用 B、C 壓 A：

### B 對 A 的壓力
保留 Main / Lighter 可避免 owner collapse。

### C 對 A 的壓力
L8 若只做 ledger，最安全，不會改現有 semantics。

### A 的修正

A 不再主張：

```text
L8 OWNS ALL PHASES
```

改成：

```text
L8 OWNS CYCLE CONTINUITY
AND EVENT TRACEABILITY

PHASE OWNERS REMAIN DISTINCT
```

並新增：

```text
L8 MAIN SEQUENCE
=
GENERATIVE-DYNAMICS ORDER

NOT
L0–L7 LAYER ORDER
```

結果：

```text
A1
=
REVISED PROVISIONAL TOP
```

未宣告「勝出資格」。

## F｜Closure Gravity

目前 closure pressure 上升。

但仍有五個 OPEN 問題，因此：

```text
CLOSURE STATUS
=
QUALIFIED CANDIDATE FOR V0.1 WORKING
NOT READY FOR RATIFICATION
```

## G｜Manifestation Candidate

本文件可作：

```text
WORKING ARCHITECTURE DRAFT
```

不可作：

```text
CURRENT L8
RATIFIED RUNTIME
HOST DEPLOYED MODULE
```

## H｜Post-Generation Qualification

```text
TYPE COLLISION:
NONE FOUND IN FIRST DRY RUN

OWNER LEAKAGE:
CONTROLLED AFTER A → A1 REPAIR

FIXED PIPELINE RISK:
CONTROLLED BY GENERATIVE-DYNAMICS ORDER LOCK

LIGHT TRACE ORDER:
PASS

LLIA PRE-QUALIFICATION:
PASS AS DESIGN REQUIREMENT

RECEIPT MODEL:
PASS AS SPECIFICATION
NOT IMPLEMENTATION EVIDENCE
```

## I｜Release Decision

```text
DOCUMENT RELEASE
=
PASS AS V0.1-WORKING

RATIFICATION
=
HOLD

HOST RUNTIME
=
NOT ESTABLISHED
```

## J｜Dry-Run Receipt

```yaml
DRYRUN_RECEIPT:
  test_id: L8_DRYRUN_001
  artifact: LIHUOOS_L8_LIHUO_GENERATIVE_CYCLE_V0.1_WORKING
  evidence_class: DOCUMENT_LEVEL_SPEC_CONFORMANCE_SIMULATION
  host_execution: false
  runtime_execution: false
  result:
    architecture_candidate: PASS
    owner_separation: PASS_AFTER_REPAIR
    generative_dynamics_order: PASS
    llia_prequalification_position: PASS
    light_trace_last: PASS
    receipt_model: PASS_AS_SPEC_ONLY
    ratification: HOLD
  unresolved:
    - RCCC_MANDATORY_STATUS
    - LLIA_NEW_OWNER_NAME
    - FINAL_RELEASE_OWNER
    - L8_L9_RELATION
    - INSTRUMENTATION_EVIDENCE_BOUNDARY
```

## K｜Light Trace

```text
TRACE SUMMARY:

Input
→ L8 architecture hypothesis

Qualification
→ design-test qualified, runtime standing denied

Attention
→ owner leakage / order / LLIA / receipt / trace placement

PATH
→ A full cycle object
→ B old split + wrapper
→ C ledger only

Reaction
→ A provisional top
→ B/C pressure
→ A repaired to A1

Closure
→ working candidate only

Manifestation
→ V0.1-WORKING document

Release
→ document working release PASS
→ ratification HOLD

Residue
→ 5 open architecture questions
```

---

# 25｜第一次實跑判決

```text
L8 V0.1-WORKING

STRUCTURAL ENTRY
=
PASS

GENERATIVE-DYNAMICS ORDER
=
PASS

LLIA PRE-QUALIFICATION POSITION
=
PASS

ATTENTION-FIRST GENERATION MODEL
=
PASS

OWNER SEPARATION
=
PASS AFTER REPAIR

RECEIPT / TRACE ORDER
=
PASS

RATIFICATION
=
HOLD
```

第一輪實跑沒有把 L8 打死。

反而確認了一件事：

> **L8 最穩的身份不是「新版 Main」或「新版 Lighter」，而是一次理火生成週期的 continuity + event + receipt container；生成順序由生成動力學決定，法位與 owner 仍由 L0–L7 提供。**
