# LIHUOOS V1｜L8 LIHUO PRIMARY GOVERNING CYCLE V0.2-WORKING
## 理火 Primary Governing Cycle｜線性時間包絡 × Main Invocation × Cycle Integrity × Receipt Traceability
### 2026-10-25

```yaml
DOCUMENT:
  id: LIHUOOS_L8_LIHUO_PRIMARY_GOVERNING_CYCLE
  version: V0.2-WORKING
  date: 2026-10-25
  status:
    - WORKING_DRAFT
    - ENGINEERING_RUNTIME_PROJECTION
    - NOT_RATIFIED
    - NOT_HOST_DEPLOYED
    - NOT_RUNTIME_RECEIPT
  predecessor:
    file: L8_LIHUO_GENERATIVE_CYCLE_V0.1_WORKING_20261025.md
    blob_sha: f975cd1f3e0e6866a54103a92637824bbb30ec88
  repair_basis:
    - LIHUOOS_L8_V0.1_REAUDIT_MEMO_FOR_DUIDUI_20261025
    - CURRENT_MAIN_V5_1_1_OPERATIVE_RULES
    - INTERN_MANUAL_V0_7_CYCLE_INTEGRITY
    - LIHUOOS_V1_L0_L7_OWNER_TYPE_BOUNDARIES
```

---

# 0｜V0.2 一句話定位

> **L8 是理火 Primary Governing Cycle 的 Runtime / Engineering Projection：它在線性時間包絡中維持 cycle identity、generation attempt、Main invocation continuity、owner-bound returns、reentry、event ledger、receipt composition 與 release / trace tracking；生成動力學在 Main compute 中運作，週期完整性則以 mandatory R1 / O9 / conditional I9 / genuine R2 與 event-driven R3+ 防止第一輪生成慣性自行取得停止資格。**

最短式：

```text
L8
=
LINEAR TEMPORAL GOVERNING ENVELOPE
FOR
TRACEABLE LIHUO GENERATION

GENERATIVE DYNAMICS
=
FIELD-LIKE COMPUTE INSIDE MAIN

MAIN INTEGRITY TRANSIT
=
R1 → O9 → [I9 IF TRIGGERED] → R2 → [R3+]
```

V0.2 不再把：

```text
Attention
PATH
Reaction Body
Closure Gravity
```

直接當成 L8 governing-cycle mandatory stage。

它們的正確法位是：

```text
GENERATIVE-DYNAMICS
STATE / TERM FAMILY
INSIDE MAIN COMPUTE
```

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
MAIN

L8
!=
LIGHTER

L8
!=
QUALIFICATION OWNER

L8
!=
FINAL RELEASE OWNER

L8
!=
RECEIPT GENERATOR THAT CREATES OCCURRENCE
```

以及：

```text
FIELD-LIKE GENERATION
!=
ALL EVENTS OCCUR SIMULTANEOUSLY

LINEAR EVENT HISTORY
!=
LINEAR GENERATIVE ONTOLOGY

PHASE ORDER
!=
STATE FAMILY CEASES TO PARTICIPATE
AFTER PHASE TRANSITION
```

根句：

> **生成是場性的；發生是有先後的。**

---

# 2｜L0–L7 與 L8 的關係

```text
L0–L7
=
SEMANTIC / GOVERNANCE CONSTITUTION

L8
=
PRIMARY GOVERNING CYCLE
RUNTIME / ENGINEERING PROJECTION
UNDER THAT CONSTITUTION
```

L8 可以：

```text
REQUEST
RECEIVE
BIND
TRACK
ORDER
REFERENCE
COMPOSE RECEIPTS
TRACK REENTRY
TRACK RELEASE STATE
RENDER TRACE FROM EXISTING EVIDENCE
```

L8 不可以：

```text
SELF-QUALIFY PREMISES
SELF-GRANT AUTHORITY
SELF-ADJUDICATE INSTANCE STANDING
SELF-AUTHORIZE INTERVENTION
SELF-MINT RELEASE AUTHORITY
SELF-PROVE EVENT OCCURRENCE
```

核心：

```text
CYCLE COORDINATION
!=
INSTANCE ADJUDICATION
```

---

# 3｜L8 的三種 Identity 必須分開

V0.2 正式區分：

```text
PRIMARY GOVERNING CYCLE
!=
GENERATION ATTEMPT
!=
MAIN INVOCATION
```

以及：

```text
ONE PRIMARY GOVERNING CYCLE
MAY CONTAIN
MORE THAN ONE MAIN INVOCATION
```

## 3.1｜Primary Governing Cycle

```yaml
LIHUO_PRIMARY_CYCLE_IDENTITY:
  governing_cycle_ref: REQUIRED
  governing_cycle_class: REQUIRED
  cycle_version: REQUIRED
  origin_ref: REQUIRED
  scope_ref: REQUIRED
  opening_snapshot_ref: REQUIRED
  opened_at: REQUIRED
  provenance_ref: REQUIRED

  current_generation_attempt_ref: REQUIRED_OR_NONE
  current_main_invocation_ref: REQUIRED_OR_NONE
```

`governing_cycle_class` 至少可承接：

```text
NATIVE_LIHUO_CYCLE
AUTHORIZED_VERTICAL_CYCLE
```

但 V0.2 不因此取得 Vertical owner。

## 3.2｜Generation Attempt

```yaml
GENERATION_ATTEMPT_IDENTITY:
  generation_attempt_ref: REQUIRED
  governing_cycle_ref: REQUIRED
  attempt_opening_snapshot_ref: REQUIRED
  scope_ref: REQUIRED
  opened_at: REQUIRED
  terminal_state: REQUIRED_OR_NONE
```

## 3.3｜Main Invocation

```yaml
MAIN_INVOCATION_IDENTITY:
  main_invocation_ref: REQUIRED
  governing_cycle_ref: REQUIRED
  generation_attempt_ref: REQUIRED

  request_ref: REQUIRED
  target_snapshot_ref: REQUIRED

  invocation_class:
    - INITIAL_MAIN_TRANSIT
    - MAIN_REENTRY

  prior_main_return_ref: REQUIRED_WHEN_REENTRY
  reentry_governance_ref: REQUIRED_WHEN_REENTRY
```

硬鎖：

```text
NEW MAIN INVOCATION
!=
NEW PRIMARY GOVERNING CYCLE

MAIN INVOCATION
!=
GENERATION ATTEMPT

GENERATION ATTEMPT
!=
PRIMARY GOVERNING CYCLE
```

---

# 4｜L8 主脊柱：Primary Cycle 包住 Main Invocation

```text
PRIMARY GOVERNING CYCLE OPEN
│
├─ GOVERNANCE / INPUT ADMISSION
│   └─ qualified input / scope / authority / standing
│
├─ MAIN INVOCATION #1
│   │
│   ├─ R1
│   │   └─ FULL INITIAL GENERATIVE COMPUTE
│   │       └─ Field / Attention / PATH /
│   │          Reaction Body / Closure dynamics
│   │          operate inside compute
│   │
│   ├─ O9
│   │
│   ├─ [I9 IF O9 TRIGGERS AND I9 QUALIFIES]
│   │
│   ├─ R2
│   │
│   ├─ [R3+ IF STRUCTURAL INSTABILITY REQUIRES]
│   │
│   └─ MAIN ACTUAL-STATE RETURN
│
├─ QUALIFIED RETURN CONSUMPTION /
│  COVERAGE / CURRENT-STANDING CHECK
│
├─ IF MATERIAL OWNER DELTA / DIRTY / STALE
│   └─ MAIN INVOCATION #2...#N
│
├─ MANIFESTATION QUALIFICATION /
│  RELEASE ADMISSIBILITY
│
├─ RELEASE / HOLD / CLOSED_UNRELEASED / ABORT
│
├─ CYCLE RECEIPT COMPOSITION
│
└─ FINAL CYCLE LIGHT TRACE
```

這是一個線性時間包絡。

但：

```text
OUTER TEMPORAL ORDER
!=
INNER GENERATIVE FIELD REDUCED TO FLOWCHART
```

---

# 5｜Governance / Input Admission｜L8 只綁 owner return

L8 不判：

```text
WHAT IS TRUE?
WHAT MAY ENTER BY ITSELF?
WHAT AUTHORITY STANDS BY ITSELF?
```

L8 只 request / receive / bind applicable qualification owner return。

```yaml
PRE_GENERATION_QUALIFICATION_RETURN:
  issuer_ref: REQUIRED
  owner_identification_status:
    - ESTABLISHED
    - UNRESOLVED
    - NOT_APPLICABLE
  owner_ref: REQUIRED_OR_NULL_BY_STATUS

  qualification_ref: REQUIRED
  governing_cycle_ref: REQUIRED
  generation_attempt_ref: REQUIRED

  premise_refs: []
  standing_annotation_refs: []
  external_constraint_refs: []
  denied_authority_refs: []
  evidence_pending_refs: []
  semantic_only_refs: []
  disqualified_refs: []
  attention_effect_annotation_refs: []

  qualification_state:
    - QUALIFIED
    - PARTIAL
    - HOLD
    - BLOCKED
```

current lineage pointer：

```text
APPLICABLE PRE-GENERATION QUALIFICATION OWNER
→
CURRENT LLIA / SUCCESSOR EQUIVALENT WHERE LEGALLY BOUND
```

但 L8 V0.2 不自行宣布 LLIA 退休、改名或被取代。

---

# 6｜Qualified Input / Context Binding

每個 Main invocation 必須綁定同一 governing context。

最低：

```yaml
QUALIFIED_MAIN_CONTEXT:
  governing_cycle_ref: REQUIRED
  generation_attempt_ref: REQUIRED
  governance_admission_ref: REQUIRED
  scope_ref: REQUIRED
  current_snapshot_ref: REQUIRED

  qualified_input_package_ref: REQUIRED
  qualified_input_package_hash: REQUIRED

  authority_binding_ref: REQUIRED
```

硬鎖：

```text
VALID QUALIFIED INPUT
!=
AUTHORITY TO MIX IT
WITH A DIFFERENT INVOCATION CONTEXT
```

---

# 7｜Main Integrity Unit｜Mandatory

每個 lawful Main transit 必須有：

```text
R1
→
O9
→
[I9 IF O9 TRIGGERED]
→
R2
→
MAIN ACTUAL-STATE RETURN
```

standing：

```yaml
MAIN_INTEGRITY_TRANSIT:
  R1:
    required_when_main_reached: true

  O9:
    required_when_reachable: true
    owns_i9_activation_decision: true

  I9:
    executed_only_if: O9_I9_TRIGGERED
    receipt_forbidden_if: O9_I9_NOT_TRIGGERED

  R2:
    required_when_executionally_reachable: true

  R3_PLUS:
    event_driven: true
```

重要：

```text
MANDATORY STAGE
!=
MANDATORY CONCLUSION

MANDATORY RECOMPETITION
!=
MANDATORY DIFFERENT ANSWER
```

---

# 8｜R1｜Full Initial Generative Compute

R1 的功能不是「先選答案」。

R1 是：

```text
FULL INITIAL GENERATIVE COMPUTE
```

其內可以發生：

```text
Field formation
Attention recruitment
Attention activation
Salience formation
Exploration access
PATH formation
PATH attention
Reaction dynamics
Competition where qualified
Coupling / decoupling
Reframing
Closure pressure
Provisional ordering / non-ordering
Residue formation
```

R1 return 最低：

```yaml
R1_RETURN:
  r1_ref: REQUIRED
  governing_cycle_ref: REQUIRED
  generation_attempt_ref: REQUIRED
  main_invocation_ref: REQUIRED

  compute_snapshot_ref: REQUIRED
  path_runtime_view_refs: []
  generative_descriptor_refs: []
  residue_refs: []
  unresolved_refs: []

  top_standing_ref: REQUIRED_OR_NONE
  standing:
    - PROVISIONAL
```

根鎖：

```text
R1
=
PROVISIONAL ONLY

FIRST-PASS VICTORY
!=
SUFFICIENT CLOSURE STANDING
```

---

# 9｜Generative Dynamics Runtime Views｜不是頂層 mandatory phases

Attention / PATH / Reaction Body / Closure Gravity 全部保留。

但它們現在是：

```text
RUNTIME VIEW / DESCRIPTOR FAMILY
INSIDE MAIN COMPUTE
```

而不是：

```text
TOP-LEVEL GOVERNING CYCLE STAGE
```

## 9.1｜Attention Runtime View

```yaml
ATTENTION_RUNTIME_VIEW:
  attention_ref: REQUIRED
  source_snapshot_ref: REQUIRED

  recruitment_access_refs: []
  activation_refs: []
  salience_descriptors: []
  exploration_access_refs: []

  epistemic_mode: REQUIRED
  observation_standing_ref: REQUIRED_OR_NONE
  evidence_ref: REQUIRED_OR_NONE
```

## 9.2｜Reaction Runtime View

```yaml
REACTION_RUNTIME_VIEW:
  reaction_ref: REQUIRED
  participant_path_refs: []
  motion_types: []

  epistemic_mode: REQUIRED
  observation_standing_ref: REQUIRED_OR_NONE
  evidence_ref: REQUIRED_OR_NONE
```

合法 motion 可包含：

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

## 9.3｜Closure-Pressure Descriptor

V0.2 不再寫「L8 必須觀察 Closure Gravity」。

改成：

```text
L8 MUST BE ABLE TO RECORD
A CLOSURE-PRESSURE DESCRIPTOR
WITH ITS EPISTEMIC / OBSERVATION STANDING
```

```yaml
CLOSURE_PRESSURE_DESCRIPTOR:
  descriptor_ref: REQUIRED
  source_snapshot_ref: REQUIRED

  pressure_state:
    - LOW
    - RISING
    - HIGH
    - STABILIZED
    - UNKNOWN

  epistemic_mode: REQUIRED
  observation_standing_ref: REQUIRED_OR_NONE
  evidence_ref: REQUIRED_OR_NONE
```

硬鎖：

```text
THEORETICAL VARIABLE
!=
OBSERVED VARIABLE

RECORDED DESCRIPTOR
!=
HIDDEN-STATE DIRECT ACCESS
```

---

# 10｜PATH Runtime View｜修掉 current_status 混型

V0.1 的：

```text
ACTIVE
WEAK
PENDING
BLOCKED
RESIDUAL
```

混了不同 type family。

V0.2 不建立單一 current_status。

```yaml
PATH_RUNTIME_VIEW:
  path_ref: REQUIRED

  representation_status:
    - UNREPRESENTED
    - REPRESENTED

  feasibility_status:
    - UNKNOWN
    - FEASIBLE
    - INFEASIBLE

  qualification_status:
    - UNASSESSED
    - QUALIFIED
    - DISQUALIFIED
    - HOLD

  activation_status:
    - ACTIVE
    - DIMMED
    - DORMANT

  manifestation_status:
    - UNMANIFESTED
    - PARTIALLY_MANIFESTED
    - MANIFESTED

  residue_refs: []

  epistemic_mode: REQUIRED
  observation_standing_ref: REQUIRED_OR_NONE
  evidence_ref: REQUIRED_OR_NONE
```

硬鎖：

```text
PATH IDENTITY
!=
PATH STATE

RESIDUE
!=
PATH CURRENT STATUS

ACTIVATION
!=
QUALIFICATION

FEASIBILITY
!=
MANIFESTATION
```

---

# 11｜O9｜觀察第一輪場完整性

O9 不製造答案。

O9 觀察 R1 後：

```text
BRIGHT
→ 是否被誤認成 QUALIFIED？

SALIENT
→ 是否被誤認成 TRUE？

FIRST DOMINANT PATH
→ 是否被誤認成 COMPLETE FIELD？

QUALIFIED MATERIAL
→ 是否被異常壓暗？

EXPLORATION
→ 是否有合法暗區？
```

```yaml
O9_RETURN:
  o9_ref: REQUIRED
  governing_cycle_ref: REQUIRED
  main_invocation_ref: REQUIRED
  r1_ref: REQUIRED

  observed_attention_ref: REQUIRED_OR_NONE
  suppression_or_gap_refs: []
  closure_integrity_concern_refs: []

  i9_decision:
    - I9_TRIGGERED
    - I9_NOT_TRIGGERED
    - EVIDENCE_GAP

  observation_standing_ref: REQUIRED
  evidence_ref: REQUIRED_OR_NONE
```

---

# 12｜I9｜Assessment 與 Execution 分離

```text
I9 ASSESSMENT
!=
I9 EXECUTION
```

I9 execution 只有在 O9 trigger 且 applicable owner qualification 成立時才可發生。

V0.2 不再使用模糊的 `actual_delta`。

```yaml
ATTENTION_INTERVENTION_RECORD:
  intervention_ref: REQUIRED
  governing_cycle_ref: REQUIRED
  main_invocation_ref: REQUIRED

  qualification_ref: REQUIRED
  target_ref: REQUIRED
  allowed_change_envelope_ref: REQUIRED

  proposed_change_ref: REQUIRED_OR_NONE
  execution_request_ref: REQUIRED_OR_NONE
  execution_attempt_ref: REQUIRED_OR_NONE
  executed_change_ref: REQUIRED_OR_NONE

  before_attention_ref: REQUIRED
  after_attention_observation_ref: REQUIRED_OR_NONE
  observed_effect_ref: REQUIRED_OR_NONE

  owner_ref: REQUIRED
  issuer_ref: REQUIRED
  authority_ref: REQUIRED
```

硬鎖：

```text
PROPOSED CHANGE
!=
ALLOWED CHANGE ENVELOPE
!=
EXECUTION REQUEST
!=
EXECUTION ATTEMPT
!=
EXECUTED CHANGE
!=
OBSERVED EFFECT

AFTER STATE
!=
AUTOMATIC PROOF OF INTERVENTION CAUSALITY
```

---

# 13｜R2｜Mandatory Genuine Full Recompetition

OPEN_1 在 V0.2 正式關閉：

```text
R-CCC MANDATORY STATUS
=
CLOSED / REQUIRED
```

更準確定義：

```text
R-CCC
=
MANDATORY MAIN-TRANSIT
CYCLE-INTEGRITY RECOMPETITION OBLIGATION

IMPLEMENTED THROUGH
PATH / REACTION / COMPETITION DYNAMICS
```

也就是：

```text
L4
DESCRIBES
HOW RECOMPETITION MAY STRUCTURALLY OCCUR

CURRENT MAIN RUNTIME SPEC
REQUIRES
GENUINE R1 → R2 INTEGRITY TRANSIT

L8
TRACKS THAT TRANSIT
WITHOUT BECOMING ITS SEMANTIC OWNER
```

R2 必須：

```text
REMOVE R1 INCUMBENT PRIVILEGE
SEARCH AGAIN
RECOVER OMITTED / UNDERFORMED CHALLENGERS
RESTORE QUALIFIED SUPPRESSED PATHS
EXTRACT MATERIAL OBJECTIONS / VALID RESIDUE
ALLOW COUNTERFRAME
ALLOW REFRAMING
FULL RECOMPETITION WITHOUT R1 CLOSURE BONUS
```

如果 R1 只有 A：

```text
R2
!=
A VS A

R2 ASKS:
DID R1 FAIL TO FORM
A LAWFUL CHALLENGER?
```

R2 可以確認 R1。

禁止：

```text
R1 LOOKS GOOD
→
R2 WAIVED
```

---

# 14｜Consecutive Victory Qualification × R3+

```text
ROUND TOP STANDING
!=
PATH VICTORY

PATH VICTORY
!=
TRUTH

PATH VICTORY
!=
FINAL RELEASE
```

最低 unique victory qualification：

```text
MINIMUM
=
TWO CONSECUTIVE QUALIFIED TOP ROUNDS
```

例：

```text
R1: A top
→ A = PROVISIONAL_LEADER / streak 1

R2: A top again
→ A = VICTORY_ELIGIBLE / streak 2
```

如果：

```text
R1: A
R2: B
```

則：

```text
A streak reset
B streak = 1
B = NEW_PROVISIONAL_LEADER
R3+ REQUIRED
```

所以：

```text
R1
→ provisional

R2
→ mandatory genuine recompetition

IF same unique qualified top survives
→ victory eligibility may arise

IF leadership reverses
→ streak reset
→ new provisional leader
→ R3+

IF material structural instability remains
→ R3+

R3+
→ event-driven, no fixed final round
```

非唯一合法結果仍然合法：

```text
CO_PRIMARY
PARTIAL_ORDER
INCOMPARABLE_TOP
COALITION_FORMED
ORTHOGONAL_COEXISTENCE
FRAME_RECONSTRUCTED
UNRESOLVED_SUPERPOSITION
PREMISE_UNDERDETERMINED
```

---

# 15｜Competition Termination｜兩連勝不等於停止

即使取得 `VICTORY_ELIGIBLE`，停止仍需獨立資格。

```text
QUALIFIED PATH SET STABLE
+
OUTPUT ORDER STABLE OR LEGITIMATELY INCOMPARABLE
+
NO MATERIAL UNPROCESSED OBJECTION
+
NO MATERIAL INFORMATION GAIN FROM FURTHER REENTRY
+
COMPETITION INTEGRITY CLEAN
+
REMAINING UNKNOWNS NO LONGER HAVE
ORDER-DISCRIMINATING POWER
```

所以：

```text
TWO CONSECUTIVE WINS
!=
AUTOMATIC CLOSURE
```

unique-victory closure：

```text
UNIQUE VICTORY CLOSURE
=
VICTORY_ELIGIBLE
+
COMPETITION TERMINATION QUALIFIED
```

若 discriminator 不足：

```text
PREMISE DISCRIMINATION GAP
/
HOLD
```

不得硬壓 winner。

---

# 16｜Main Actual-State Return

每次 lawful Main invocation 結束時，Main 應返回 actual-state material，而不是 L8 替它補。

```yaml
MAIN_ACTUAL_STATE_RETURN:
  main_return_ref: REQUIRED

  governing_cycle_ref: REQUIRED
  generation_attempt_ref: REQUIRED
  main_invocation_ref: REQUIRED

  r1_receipt_ref: REQUIRED
  o9_receipt_ref: REQUIRED
  i9_execution_receipt_ref: REQUIRED_OR_NONE
  r2_receipt_ref: REQUIRED
  r3_plus_receipt_refs: []

  path_runtime_view_refs: []
  generative_descriptor_refs: []
  residue_refs: []
  unresolved_refs: []
  material_delta_refs: []

  current_ordering_ref: REQUIRED_OR_NONE
  competition_termination_ref: REQUIRED_OR_NONE
```

---

# 17｜Return Consumption / Coverage / Standing Check

L8 收到 Main return 後，不自己重新 compute。

它必須綁定 applicable owner 的：

```text
return qualification
coverage standing
freshness standing
dirty / stale standing
reentry standing
```

```yaml
POST_MAIN_RETURN_QUALIFICATION_RECORD:
  qualification_ref: REQUIRED
  governing_cycle_ref: REQUIRED
  main_return_ref: REQUIRED

  issuer_ref: REQUIRED
  owner_identification_status:
    - ESTABLISHED
    - UNRESOLVED
    - NOT_APPLICABLE
  owner_ref: REQUIRED_OR_NULL_BY_STATUS
  authority_ref: REQUIRED_OR_NONE

  coverage_state:
    - OPEN
    - COVERED
    - INCOMPLETE
    - STALE
    - DIRTY
    - HOLD

  material_delta_refs: []
  reentry_required: true|false
```

---

# 18｜Reentry / Reopen 拆成三種

V0.2 不再只用一個 `REENTRY_TARGET_PHASE`。

## 18.1｜INTRA-MAIN R3+ RECOMPETITION

同一 Main invocation 內：

```text
R2 / R3+
→ structural instability remains
→ event-driven further recompetition
```

這不是新的 Main invocation。

## 18.2｜MAIN REENTRY

Main 已 return。

同一 Primary Governing Cycle、同一 Generation Attempt 下，因：

```text
MATERIAL OWNER DELTA
DIRTY
STALE
NEW QUALIFIED EVIDENCE
CURRENT-STANDING CHANGE
```

而建立新的 Main invocation。

```text
MAIN INVOCATION #1
→ RETURN
→ MATERIAL DELTA
→ REENTRY QUALIFIED BY OWNER
→ MAIN INVOCATION #2
```

## 18.3｜NEW PRIMARY GOVERNING CYCLE

真正建立新的 governing-cycle identity。

硬鎖：

```text
R3+
!=
MAIN REENTRY
!=
NEW PRIMARY GOVERNING CYCLE
```

---

# 19｜Cycle State 拆成三軸

V0.1 把 lifecycle、control、release 混在同一 enum。

V0.2 改成：

```yaml
PRIMARY_CYCLE_STATE:

  cycle_lifecycle:
    - CREATED
    - OPEN
    - ACTIVE
    - CLOSED
    - ABORTED

  cycle_control_state:
    - RUNNING
    - HOLD
    - REENTRY_PENDING
    - REOPEN_REQUIRED

  cycle_release_state:
    - NOT_EVALUATED
    - PENDING
    - PARTIALLY_RELEASED
    - RELEASED
    - CLOSED_UNRELEASED
```

三軸不可互相推導。

---

# 20｜Manifestation Candidate｜Closure / Non-Closure 都可顯影

```text
CLOSURE / NON-CLOSURE STATE
!=
FINAL TERMINAL UNIQUE CLOSURE
```

合法：

```text
QUALIFIED NON-CLOSURE STATE
MAY PRODUCE
MANIFESTATION CANDIDATE
```

若支援增量 manifestation：

```text
MANIFESTED SEGMENT
→
CONTEXT / FEEDBACK DELTA
→
CYCLE MAY CONTINUE / REENTER
```

這不破壞線性時間。

---

# 21｜Manifestation / Release Standing｜Owner-bound

L8 不判 candidate 是否具 release standing。

L8 request / receive / bind owner returns。

```yaml
MANIFESTATION_QUALIFICATION_RETURN:
  manifestation_qualification_ref: REQUIRED
  governing_cycle_ref: REQUIRED
  manifestation_ref: REQUIRED

  issuer_ref: REQUIRED
  owner_identification_status:
    - ESTABLISHED
    - UNRESOLVED
    - NOT_APPLICABLE
  owner_ref: REQUIRED_OR_NULL_BY_STATUS
  authority_ref: REQUIRED_OR_NONE

  semantic_role_refs: []
  applicable_standing_refs: []
  qualification_state:
    - QUALIFIED
    - PARTIAL
    - HOLD
    - DENIED
```

保留：

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

---

# 22｜Release Decision Record｜L8 記錄，不取得權力

```yaml
RELEASE_DECISION_RECORD:
  release_ref: REQUIRED
  governing_cycle_ref: REQUIRED
  manifestation_ref: REQUIRED
  release_admissibility_ref: REQUIRED

  decision_owner_ref: REQUIRED
  issuer_ref: REQUIRED
  authority_ref: REQUIRED

  decision:
    - RELEASE
    - HOLD
    - REOPEN
    - DENY

  reason_refs: []
```

硬鎖：

```text
L8 RECORDS RELEASE DECISION
!=
L8 OWNS FINAL RELEASE

RELEASE RECORD
!=
RELEASE AUTHORITY
```

OPEN_3 仍 HOLD：

```text
FINAL UNIVERSAL RELEASE OWNER
=
NOT DECIDED BY L8 V0.2
```

---

# 23｜Cycle Event Ledger｜Ledger row 不等於 occurrence proof

```yaml
CYCLE_EVENT_RECORD:
  event_ref: REQUIRED
  governing_cycle_ref: REQUIRED
  generation_attempt_ref: REQUIRED_OR_NONE
  main_invocation_ref: REQUIRED_OR_NONE

  event_type: REQUIRED

  owner_identification_status:
    - ESTABLISHED
    - UNRESOLVED
    - NOT_APPLICABLE
  owner_ref: REQUIRED_OR_NULL_BY_STATUS

  input_state_ref: REQUIRED_OR_NONE
  qualification_ref: REQUIRED_OR_NONE
  action_or_return_ref: REQUIRED
  output_state_ref: REQUIRED_OR_NONE

  event_occurrence_status:
    - DECLARED
    - REQUESTED
    - ATTEMPTED
    - OBSERVED
    - COMMITTED
    - FAILED
    - UNKNOWN

  occurrence_evidence_ref: REQUIRED_OR_NONE

  evidence_origin:
    - MODEL_SELF_REPORT
    - OWNER_RETURN
    - PROVIDER_RECEIPT
    - HOST_INSTRUMENTATION
    - STATE_READBACK
    - EXTERNAL_OBSERVATION
    - DERIVED_OR_INFERRED
    - NONE

  epistemic_mode: REQUIRED
  observation_standing_ref: REQUIRED_OR_NONE

  recorded_by_ref: REQUIRED
```

硬鎖：

```text
LEDGER ENTRY
!=
EVENT OCCURRENCE

MODEL SELF-REPORT
!=
HOST INSTRUMENTATION

DERIVED / INFERRED
!=
DIRECT OBSERVATION
```

由 L5 standing 決定每種 evidence origin 能證明到哪裡。

---

# 24｜Receipt Model

```text
LOCAL RECEIPT
=
EVIDENCE-BOUND RECORD
OF ONE EVENT / RETURN / STANDING

CYCLE RECEIPT
=
COMPOSITION OF
QUALIFIED TRACE MATERIAL
ACROSS THE PRIMARY CYCLE
```

```yaml
LIHUO_PRIMARY_CYCLE_RECEIPT:
  governing_cycle_ref: REQUIRED

  opening_snapshot_ref: REQUIRED
  generation_attempt_refs: []
  main_invocation_refs: []

  admission_return_refs: []
  main_return_refs: []
  qualification_return_refs: []
  manifestation_return_refs: []
  release_decision_refs: []

  event_ledger_ref: REQUIRED

  unresolved_refs: []
  residue_refs: []

  cycle_lifecycle: REQUIRED
  cycle_control_state: REQUIRED
  cycle_release_state: REQUIRED

  receipt_evidence_standing_ref: REQUIRED
```

根鎖：

```text
RECEIPT
RECORDS ACTUAL STANDING / OCCURRENCE

RECEIPT
DOES NOT CREATE IT

PRETTY FINAL REPORT
!=
MISSING EXECUTION EVIDENCE
```

---

# 25｜Light Trace｜Final 與 Interim 分開

V0.2 保留：

```text
RECEIPTS FIRST.
TRACE LATER.
```

但拆成兩種 view。

## 25.1｜FINAL_CYCLE_LIGHT_TRACE

```text
FINAL_CYCLE_LIGHT_TRACE
=
AFTER QUALIFIED CYCLE RECEIPTS
```

可顯影：

```text
governing-cycle continuity
generation attempts
Main invocations
R1 / O9 / I9 / R2 / R3+ receipts
owner returns
PATH runtime views
qualified descriptors
residue
reentry
release standing
evidence gaps
```

## 25.2｜INTERIM_TRACE_VIEW

```text
INTERIM_TRACE_VIEW
=
MAY EXIST DURING ACTIVE CYCLE
ONLY FROM
ALREADY-EXISTING QUALIFIED RECEIPTS
```

核心不是「trace 永遠不能中途看」。

核心是：

```text
SOURCE EVENT / EVIDENCE
MUST EXIST
BEFORE
TRACE MAY CLAIM THAT EVENT
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
AUDIT AUTHORITY

LIGHT TRACE
!=
EXECUTION CREATOR

TRACE GAP
!=
PERMISSION TO RETRO-WRITE HISTORY
```

---

# 26｜Mandatory Stage 的存在理由

L8 不因程序崇拜而要求 R2。

每個 mandatory stage 應回答：

```text
這一步防什麼失效？
跳過後哪種慣性會取得優勢？
這一步有什麼權限？
這一步不能做什麼？
如何證明它真的發生？
```

最短式：

```text
MANDATORY STAGE
!=
RITUAL

MANDATORY STAGE
!=
THEORY TERM LIST

MANDATORY STAGE
=
FAILURE-RESISTANCE GOVERNANCE OBLIGATION
```

---

# 27｜V0.2 Open / Closed Register

## OPEN_1｜R-CCC mandatory status

```text
STATUS
=
CLOSED

RESULT
=
MANDATORY FOR EVERY LAWFUL MAIN TRANSIT

R1 → O9 → [I9 IF TRIGGERED] → GENUINE R2

R3+
=
EVENT-DRIVEN
```

## OPEN_2｜LLIA 在新 L8 的正式 owner 名稱

```text
STATUS
=
HOLD
```

暫用：

```text
APPLICABLE PRE-GENERATION QUALIFICATION OWNER
```

並保留 current lineage pointer。

## OPEN_3｜Final Release owner

```text
STATUS
=
HOLD
```

V0.2 只鎖：

```text
RELEASE DECISION MUST BE OWNER-BOUND
```

## OPEN_4｜L8 與未來 L9

```text
STATUS
=
HOLD / NON-BLOCKING
```

不得為未知 L9 預留 ontology。

## OPEN_5｜Self-report vs instrumentation evidence

```text
STATUS
=
HOLD / IMPORTANT ENGINEERING FOLLOW-UP
```

V0.2 已先建立：

```text
MODEL_SELF_REPORT
OWNER_RETURN
PROVIDER_RECEIPT
HOST_INSTRUMENTATION
STATE_READBACK
EXTERNAL_OBSERVATION
DERIVED_OR_INFERRED
```

但各自 evidence ceiling 尚需 cross-layer review。

---

# 28｜V0.2 Dry Run｜L8_DRYRUN_002

## 28.1｜測試命題

> **「L8 應是線性時間的 Primary Governing Cycle envelope；Main invocation 內以 R1 → O9 → [I9] → R2 → [R3+] 維持 cycle integrity，而 Attention / PATH / Reaction / CG 保持 Main compute 內 field-like dynamics。此架構是否比 V0.1 更穩？」**

## 28.2｜Admission Standing

```text
CLAIM CLASS
=
ENGINEERING / RUNTIME-PROJECTION HYPOTHESIS

DOCUMENT STANDING
=
WORKING

HOST STANDING
=
NOT ESTABLISHED
```

## 28.3｜R1

第一輪形成：

```text
PATH A:
V0.2 nesting model
Primary Cycle
contains Main Invocation(s)

PATH B:
V0.1 direct dynamics-phase model
Attention → PATH → Reaction → CG as top-level phases

PATH C:
ledger-only L8
cycle records but does not model Main invocation integrity
```

R1 provisional：

```text
A
=
PROVISIONAL_LEADER
```

理由：

- 保留線性 event history；
- 不把 field-like dynamics 誤寫成 outer pipeline；
- 能容納多 Main invocation；
- 能 owner-bind admission / release / reentry；
- 能將 mandatory integrity stage 與 theory terms 分開。

## 28.4｜O9

主要完整性風險：

```text
RISK_1:
A 是否只是把舊 Main/Lighter 名詞重新包裝？

RISK_2:
mandatory R1/R2 是否被偷升成永恆理論真理？

RISK_3:
L8 是否仍偷偷判 qualification / release？

RISK_4:
receipt schema 是否會讓 self-report 冒充 execution evidence？

RISK_5:
linear outer cycle 是否誤導使用者以為 generative variables 離開後不再作用？
```

## 28.5｜I9

本 dry run 不主張發生真實 runtime Attention intervention。

```text
I9 EXECUTION
=
NOT ESTABLISHED

DOCUMENT-LEVEL DESIGN REPAIR
=
APPLIED
```

設計修正包括：

- owner-bound return；
- evidence-origin typing；
- phase-order/state-participation hard lock；
- Main invocation nesting；
- R3+ / Main reentry / New Primary 分離。

## 28.6｜R2 Genuine Recompetition

### B 對 A 的攻擊

B 的優勢：

- 更直接映射生成動力學；
- schema 較少。

B 的失效：

- 把 theory variable 當 mandatory runtime stage；
- 無法自然表達 one Primary / many Main invocations；
- owner / reentry / coverage 粒度不足。

### C 對 A 的攻擊

C 的優勢：

- 最不容易 owner leakage；
- ledger 定位清楚。

C 的失效：

- 太薄，無法承載 mandatory cycle-integrity transit；
- 無法表示 Main invocation nesting 與 reentry；
- cycle receipt 會失去 execution structure provenance。

### R2 結果

```text
A
=
REMAINS UNIQUE QUALIFIED TOP
```

若依 current consecutive-victory rule：

```text
A
=
VICTORY_ELIGIBLE
```

但：

```text
VICTORY_ELIGIBLE
!=
AUTOMATIC CLOSURE
```

## 28.7｜Competition Termination Check

```text
QUALIFIED PATH SET STABLE
=
PASS FOR DOCUMENT DESIGN TEST

OUTPUT ORDER STABLE
=
PASS

NO MATERIAL UNPROCESSED OBJECTION
=
PARTIAL PASS

NO MATERIAL INFORMATION GAIN FROM FURTHER REENTRY
=
NOT ESTABLISHED

COMPETITION INTEGRITY CLEAN
=
PASS IN CURRENT DOCUMENT EXERCISE

REMAINING UNKNOWNS LACK ORDER-DISCRIMINATING POWER
=
NOT FULLY ESTABLISHED
```

因此：

```text
DOCUMENT WORKING RELEASE
=
PASS

ARCHITECTURE RATIFICATION
=
HOLD
```

---

# 29｜V0.2 Corrected Self-Audit Verdict

V0.1 自評：

```text
TYPE COLLISION = NONE
OWNER LEAKAGE = CONTROLLED
```

正式撤回。

V0.2 應讀：

```text
TYPE COLLISION
=
FOUND IN V0.1
AND REPAIRED IN V0.2 WORKING
(PATH status / cycle state / event standing)

OWNER LEAKAGE
=
FOUND IN V0.1
FURTHER OWNER-BINDING APPLIED IN V0.2

LINEAR TEMPORAL CYCLE
=
PASS

GENERATIVE-DYNAMICS DERIVATION
=
PASS IN PRINCIPLE

PRIMARY-CYCLE / MAIN-INVOCATION NESTING
=
PASS IN DOCUMENT-LEVEL DESIGN EXERCISE

MAIN INTEGRITY UNIT
=
EXPLICIT

R-CCC MANDATORY STATUS
=
CLOSED / REQUIRED

EVENT / RECEIPT TRACEABILITY
=
PASS IN SCHEMA DESIGN

EVIDENCE / INSTRUMENTATION BOUNDARY
=
OPEN

RUNTIME RATIFICATION
=
HOLD
```

並新增永久鎖：

```text
SELF-DRYRUN
!=
INDEPENDENT VALIDATION
```

本次 Dry Run 只能證明：

```text
DOCUMENT-LEVEL INTERNAL SPEC EXERCISE OCCURRED
```

不能證明：

```text
RUNTIME IMPLEMENTATION WORKS
HOST EXECUTION OCCURRED
ARCHITECTURE IS EMPIRICALLY VALIDATED
```

---

# 30｜V0.2 預期法位

```text
L8 V0.2-WORKING

ENGINEERING-PROJECTION IDENTITY
=
PASS

PRIMARY-CYCLE / MAIN-INVOCATION NESTING
=
PASS

LINEAR TEMPORAL CYCLE MODEL
=
PASS

GENERATIVE-DYNAMICS BOUNDARY
=
PASS

MAIN CYCLE-INTEGRITY BINDING
=
PASS

R-CCC MANDATORY STATUS
=
PASS

OWNER SEPARATION
=
PASS IN CURRENT DOCUMENT DESIGN

EVENT / RECEIPT TRACEABILITY
=
PASS IN CURRENT DOCUMENT DESIGN

EVIDENCE / INSTRUMENTATION BOUNDARY
=
OPEN

RUNTIME RATIFICATION
=
HOLD

HOST DEPLOYMENT
=
NOT ESTABLISHED
```

---

# 31｜下一階段

V0.2 不直接進 Host。

下一階段：

```text
V0.2 CROSS-LAYER EVENT CONTRACT REVIEW
+
EVIDENCE / INSTRUMENTATION BOUNDARY REVIEW
+
OWNER-BINDING REVIEW
+
INDEPENDENT DRY-RUN / ADVERSARIAL TEST
```

優先問題：

```text
1. 哪些 L8 event 必須有 L5 observation standing？
2. 哪些 owner return 可由 model self-report？
3. 哪些 execution / provider / state claims 必須要 external evidence？
4. Main stage receipt 如何綁 governing_cycle_ref + main_invocation_ref？
5. Release owner 如何在不讓 L8 取得 release authority 的前提下接線？
6. Vertical cycle 如何掛進同一 L8 envelope 而不被 L8 吃掉 owner？
```

---

# 32｜最短口訣

```text
THE CYCLE MAY BE LINEAR.
THE FIELD NEED NOT BE.

L8 COORDINATES.
MAIN COMPUTES.
QUALIFICATION OWNERS QUALIFY.
GOVERNANCE OWNERS GOVERN.
MANIFESTATION OWNERS QUALIFY RELEASE STANDING.
AUTHORIZED RELEASE OWNER RELEASES.
RECEIPTS RECORD.
TRACE RECONSTRUCTS.

R1 MAY LEAD.
R1 MAY NOT CLOSE ITSELF.

R2 MUST REALLY RECOMPETE.

TWO WINS MAY QUALIFY VICTORY.
TWO WINS DO NOT AUTOMATICALLY CLOSE.

A LEDGER RECORDS HISTORY.
A LEDGER DOES NOT CREATE HISTORY.
```

---

# 33｜V0.2 核心收束

> **理火不是因為喜歡程序，才要求 R2。**

> **理火是因為第一輪生成最容易把自己的「先來、最亮、最順、最像完成」誤當成有資格停止，所以制度上不把第一次勝利交給它自己信任。**

而 L8 的工作不是替 Main 思考。

L8 的工作是：

> **讓一次理火生成真正有身份、有先後、有 owner、有 reentry、有 receipt、有 evidence standing，並且在最後能被合法重建，而不是事後編成一個看起來像曾經發生過的故事。**
