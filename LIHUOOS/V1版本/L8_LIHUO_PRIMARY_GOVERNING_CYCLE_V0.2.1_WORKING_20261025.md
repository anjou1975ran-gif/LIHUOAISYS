# LIHUOOS V1｜L8 LIHUO PRIMARY GOVERNING CYCLE V0.2.1-WORKING
## 理火 Primary Governing Cycle｜線性時間包絡 × Main Invocation × Cycle Integrity × Receipt Traceability
### 2026-10-25

```yaml
DOCUMENT:
  id: LIHUOOS_L8_LIHUO_PRIMARY_GOVERNING_CYCLE
  version: V0.2.1-WORKING
  date: 2026-10-25
  status:
    - WORKING_DRAFT
    - ENGINEERING_RUNTIME_PROJECTION
    - NOT_RATIFIED
    - NOT_HOST_DEPLOYED
    - NOT_RUNTIME_RECEIPT
  predecessor:
    file: L8_LIHUO_PRIMARY_GOVERNING_CYCLE_V0.2_WORKING_20261025.md
    blob_sha: 4bc9af38fc108499fbfcbff31c1d43c919a12e38
  repair_basis:
    - LIHUOOS_L8_V0_2_INTERFACE_REAUDIT_20261025
    - CURRENT_MAIN_V5_1_1_OPERATIVE_RULES
    - INTERN_MANUAL_V0_7_CYCLE_INTEGRITY
    - LIHUOOS_V1_L0_L7_OWNER_TYPE_BOUNDARIES
  canonical_source_bindings:
    main_file: "理火V5系統/V5.1版本/02_LIHUO_MAIN_V5.1.1_FULL_BODY_RATIFIED_20261015.md"
    main_blob_sha: f5e219c986debfea074fbf9d121367cc717dc78e
    l7_file: "LIHUOOS/V1版本/L7 第二版本.md"
    l7_blob_sha: a25fc8da5efcb267d6f0aec4e626748cf097e1d8
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


# 3｜Identity Model｜Primary / Attempt / Invocation 不得誤做單向 containment

V0.2 已正確區分：

```text
PRIMARY GOVERNING CYCLE
!=
GENERATION ATTEMPT
!=
MAIN INVOCATION
```

V0.2.1 再補一個關鍵：

```text
GENERATION ATTEMPT
IS NOT
IDENTITY-BOUND
TO EXACTLY ONE PRIMARY GOVERNING CYCLE
```

現行 Main 明確允許：

```text
SAME generation_attempt_ref
+
NEW governing_cycle_ref
=
SUCCESSOR PRIMARY
```

所以一個 Generation Attempt 可以跨越多個合法 successor Primary。

## 3.1｜Primary Governing Cycle Identity

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

Primary 可以在當前時點指向 current Attempt，
但：

```text
CURRENT ATTEMPT POINTER
!=
ATTEMPT IDENTITY OWNERSHIP
```

## 3.2｜Generation Attempt Identity

Generation Attempt 自己不內嵌唯一 `governing_cycle_ref`。

```yaml
GENERATION_ATTEMPT_IDENTITY:
  generation_attempt_ref: REQUIRED
  opened_at: REQUIRED
  terminal_state: REQUIRED_OR_NONE
  provenance_ref: REQUIRED_OR_NONE
```

Attempt 與 Primary 的關係另做 binding：

```yaml
GENERATION_ATTEMPT_PRIMARY_BINDING:
  binding_ref: REQUIRED
  generation_attempt_ref: REQUIRED
  governing_cycle_ref: REQUIRED

  binding_class:
    - INITIAL_PRIMARY
    - SUCCESSOR_PRIMARY

  predecessor_primary_ref: REQUIRED_WHEN_SUCCESSOR
  binding_authority_ref: REQUIRED
  binding_standing_ref: REQUIRED
```

硬鎖：

```text
ONE GENERATION ATTEMPT
MAY SPAN
MORE THAN ONE PRIMARY GOVERNING CYCLE

NEW SUCCESSOR PRIMARY
!=
MAIN REENTRY OF OLD PRIMARY
```

## 3.3｜Main Invocation｜L8 不再定義 shadow authoritative schema

V0.2 的 `MAIN_INVOCATION_IDENTITY` 薄版 schema 撤回。

L8 V0.2.1 不重新定義 Main 身分證，而只建立 foreign-key / container binding：

```yaml
L8_MAIN_INVOCATION_BINDING:
  l8_binding_ref: REQUIRED

  governing_cycle_ref: REQUIRED
  generation_attempt_ref: REQUIRED
  main_invocation_ref: REQUIRED

  canonical_main_invocation_identity_ref: REQUIRED
  canonical_main_transit_request_ref: REQUIRED
  canonical_prebound_invocation_authority_ref: REQUIRED

  canonical_contract_source_ref: REQUIRED
  binding_validation_ref: REQUIRED
```

現行 canonical Main objects：

```text
MAIN_INVOCATION_IDENTITY
MAIN_TRANSIT_REQUEST_V5_1
MAIN_PREBOUND_INVOCATION_AUTHORITY
```

其中 Main canonical contract 已要求：

```text
exact_request_hash
scope_ref
target_snapshot_ref
current_cycle_continuity_qualification_ref when applicable
prebound_invocation_authority_ref
qualified_input_package_ref / hash
governance_admission_ref
governance_ticket_ref
manifest_ref
```

並有：

```text
ONE PREBOUND INVOCATION AUTHORITY
MAY AUTHORIZE
EXACTLY ONE main_invocation_ref
```

所以 L8 只 consume / bind。

根鎖：

```text
CONTAINER
MAY REFERENCE
CANONICAL MAIN IDENTITY

CONTAINER
MAY NOT
ISSUE A THINNER SUBSTITUTE IDENTITY

CONSUME CANONICAL CONTRACT
!=
DEFINE SHADOW CONTRACT
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


# 6｜Qualified Input / Context Binding｜只綁 canonical Main contract

V0.2 的 `QUALIFIED_MAIN_CONTEXT` 薄版 schema 不再作 authoritative contract。

L8 V0.2.1 只維持 container-level binding：

```yaml
L8_MAIN_CONTEXT_BINDING:
  l8_context_binding_ref: REQUIRED

  governing_cycle_ref: REQUIRED
  generation_attempt_ref: REQUIRED
  main_invocation_ref: REQUIRED

  canonical_qip_ref: REQUIRED
  canonical_main_transit_request_ref: REQUIRED
  canonical_prebound_invocation_authority_ref: REQUIRED

  canonical_context_validation_ref: REQUIRED
```

Main 現行 equality / exact-binding 規則由 canonical contract 自己定義並執行，包括：

```text
QIP.governing_cycle_ref
=
REQUEST.governing_cycle_ref

QIP.generation_attempt_ref
=
REQUEST.generation_attempt_ref

QIP.governance_admission_ref
=
REQUEST.governance_admission_ref

QIP.scope_ref
=
REQUEST.scope_ref

QIP.current_snapshot_ref
=
REQUEST.target_snapshot_ref
```

以及 request hash、QIP hash、prebound invocation authority 的 exact match。

L8 不重複這套 contract。

硬鎖：

```text
VALID QIP
!=
AUTHORITY TO MIX IT
WITH A DIFFERENT REQUEST CONTEXT

L8 CONTEXT BINDING
!=
MAIN CONTRACT REDEFINITION
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


# 16｜Main Actual-State Return｜Consume Canonical Return, Do Not Shadow It

V0.2 自建的 `MAIN_ACTUAL_STATE_RETURN` schema 撤回。

L8 V0.2.1 直接 consume：

```text
MAIN_ACTUAL_STATE_RETURN_V5_1
```

並以 container binding 記錄：

```yaml
L8_MAIN_RETURN_BINDING:
  l8_return_binding_ref: REQUIRED

  governing_cycle_ref: REQUIRED
  generation_attempt_ref: REQUIRED
  main_invocation_ref: REQUIRED

  canonical_main_actual_state_return_ref: REQUIRED
  canonical_main_compute_dependency_state_ref: REQUIRED

  canonical_return_contract_source_ref: REQUIRED
  binding_validation_ref: REQUIRED
```

現行 canonical return 已自帶：

```text
request_ref
exact_request_hash
governance_admission_ref
governance_ticket_ref
manifest_ref
qualified_input_package_ref / hash
scope_ref
input_snapshot_ref
covered_snapshot_ref
final_snapshot_ref
actual_state
R1 / O9 / I9 / R2 stage states
compute_dependency_state_ref
main_output_ref
candidate_or_partial_order_ref
unresolved_gap_refs
```

因此：

```text
L8
CONSUMES CANONICAL RETURN

L8
DOES NOT DEFINE
A THINNER MAIN RETURN
```

## 16.1｜Upstream Interface Gap｜R3+ Export

V0.2 曾自行加入：

```text
r3_plus_receipt_refs
```

到 L8 shadow return。

這在 V0.2.1 撤回。

原因：

現行 `MAIN_ACTUAL_STATE_RETURN_V5_1` 的 explicit `stages` 目前列：

```text
R1
O9
I9
R2
```

但 Main 同一現行版本又明確保留：

```text
R3_PLUS
=
EVENT_DRIVEN
```

且較早的 Main return contract 曾明列：

```text
r3_plus_receipt_refs: IF_TRIGGERED
```

因此這不是 L8 可以自行補的欄位，而是：

```text
UPSTREAM INTERFACE GAP

EVENT-DRIVEN R3+ RECEIPT
→
HOW IS IT EXPORTED THROUGH
CURRENT MAIN V5.1.1 RETURN CONTRACT?
```

合法修法只有兩類：

```text
A.
MAIN canonical return
formally adds R3+ receipt / event refs

OR

B.
MAIN canonical return
exports a canonical stage/event-ledger ref
that legally carries R3+ evidence
```

永久鎖：

```text
L8 MAY NOT
SILENTLY PATCH
MAIN CANONICAL RETURN CONTRACT
```

在上游修復前：

```text
R3+ SEMANTICS
=
VALID

R3+ CROSS-LAYER EXPORT CONTRACT
=
OPEN GAP
```

---


# 17｜Post-Main Return Binding｜Coverage / Dependency / Reentry / Control 分型

V0.2 的單一 `coverage_state`：

```text
OPEN
COVERED
INCOMPLETE
STALE
DIRTY
HOLD
```

正式撤回。

因為它混了：

```text
COVERAGE
!=
COMPUTE DEPENDENCY / FRESHNESS
!=
REENTRY QUALIFICATION
!=
CONTROL DISPOSITION
```

V0.2.1 改為：

```yaml
POST_MAIN_RETURN_BINDING:
  binding_ref: REQUIRED

  governing_cycle_ref: REQUIRED
  generation_attempt_ref: REQUIRED
  main_invocation_ref: REQUIRED
  canonical_main_return_ref: REQUIRED

  coverage_status:
    - OPEN
    - COVERED
    - INCOMPLETE

  compute_dependency_state_ref: REQUIRED

  reentry_qualification:
    - REENTRY_REQUIRED
    - NON_REENTRY_QUALIFIED
    - HOLD
    - UNRESOLVED

  reentry_qualification_ref: REQUIRED_OR_NONE
  qualified_non_reentry_basis_ref: REQUIRED_OR_NONE

  reentry_owner_ref: REQUIRED_OR_UNRESOLVED
  reentry_authority_ref: REQUIRED_OR_NONE

  control_disposition:
    - PROCEED
    - HOLD

  control_disposition_ref: REQUIRED
```

Main 可以提供 compute dependency facts，例如：

```text
DEPENDENCY_CHANGED
DIRTY
STALE
RECOMPUTE_NEEDED
```

但：

```text
MAIN COMPUTE FACT
!=
REENTRY GOVERNANCE DECISION
```

現行 Main 根鎖保留：

```text
MAIN STATES
WHAT ITS COMPUTE DEPENDS ON.

APPLICABLE GOVERNANCE OWNER QUALIFIES
WHAT THAT MEANS
FOR DIRTY / STALE / REENTRY.
```

因此 V0.2 的：

```text
reentry_required: true|false
```

撤回。

boolean 裝不下：

```text
UNRESOLVED
HOLD
QUALIFIED NON-REENTRY BASIS
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


# 21｜Manifestation Qualification｜Consume L7 Canonical State Untranslated

L8 不重新命名 L7 qualification enum。

V0.2 的：

```text
QUALIFIED
PARTIAL
HOLD
DENIED
```

撤回。

現行 L7 canonical：

```text
MANIFESTATION_QUALIFICATION
=
QUALIFIED
PARTIALLY_QUALIFIED
NOT_QUALIFIED
REQUALIFICATION_REQUIRED
```

其中：

```text
HOLD
NON_MANIFESTATION
REPAIR_REQUIRED
```

不是 qualification state，
而屬 release / governance disposition family。

L8 V0.2.1 只 consume owner return：

```yaml
MANIFESTATION_QUALIFICATION_RETURN_BINDING:
  binding_ref: REQUIRED

  governing_cycle_ref: REQUIRED
  manifestation_ref: REQUIRED

  canonical_manifestation_qualification_ref: REQUIRED

  issuer_ref: REQUIRED
  owner_ref: REQUIRED_OR_UNRESOLVED
  authority_ref: REQUIRED_OR_NONE

  canonical_qualification_state:
    - QUALIFIED
    - PARTIALLY_QUALIFIED
    - NOT_QUALIFIED
    - REQUALIFICATION_REQUIRED

  release_disposition_ref: REQUIRED_OR_NONE
```

硬鎖：

```text
OWNER RETURN CONSUMPTION
!=
ENUM TRANSLATION

MANIFESTATION QUALIFICATION
!=
RELEASE DISPOSITION

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
NOT DECIDED BY L8 V0.2.1
```

---


# 23｜Cycle Event Ledger｜Event Type Hygiene

V0.2 的 universal：

```text
event_occurrence_status:
DECLARED
REQUESTED
ATTEMPTED
OBSERVED
COMMITTED
FAILED
UNKNOWN
```

撤回。

原因：

```text
DECLARED
=
CLAIM / ASSERTION FAMILY

REQUESTED / ATTEMPTED / COMMITTED
=
ACTION / EXECUTION FAMILY

OBSERVED
=
EPISTEMIC / ACCESS FAMILY

FAILED
=
OUTCOME FAMILY
```

這些不能共用單一 enum。

V0.2.1 改為 typed refs：

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

  occurrence_claim_ref: REQUIRED_OR_NONE

  execution_state_ref: OPTIONAL_BY_EVENT_TYPE
  observation_standing_ref: OPTIONAL_BY_EVENT_TYPE
  outcome_ref: OPTIONAL_BY_EVENT_TYPE

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
  recorded_by_ref: REQUIRED
```

不同 event type 自己使用適用的 canonical state family。

例如：

```text
MAIN RETURN EMITTED
!=
PROVIDER ACTION EXECUTED
!=
OBSERVATION MADE
!=
CLAIM DECLARED
```

它們不得被迫共享同一 lifecycle。

硬鎖：

```text
EVENT CLAIM STATE
!=
EXECUTION STATE
!=
OBSERVATION STATE
!=
OUTCOME STATE

LEDGER ENTRY
!=
EVENT OCCURRENCE
```

---


# 24｜Receipt Model｜Receipt 不得超過 Evidence Standing

V0.2 的根句：

```text
RECEIPT
RECORDS ACTUAL STANDING / OCCURRENCE
```

過強，正式撤回。

V0.2.1 改成：

```text
RECEIPT
RECORDS EVIDENCE-BOUND CLAIMS
ABOUT STANDING / OCCURRENCE

AND MUST NOT CLAIM
BEYOND ITS EVIDENCE STANDING
```

因此：

```text
MODEL_SELF_REPORT RECEIPT
!=
HOST OCCURRENCE PROOF

OWNER_RETURN RECEIPT
!=
PROVIDER EXECUTION PROOF

DERIVED RECORD
!=
DIRECT OBSERVATION
```

只有當 applicable evidence standing 足夠時：

```text
QUALIFIED OCCURRENCE RECEIPT
MAY SUPPORT
ACTUAL OCCURRENCE
```

但：

```text
RECEIPT SHAPE ALONE
DOES NOT CREATE
OCCURRENCE STANDING
```

## 24.1｜Local Receipt

```text
LOCAL RECEIPT
=
EVIDENCE-BOUND RECORD
OF A CLAIM ABOUT
ONE EVENT / RETURN / STANDING
```

## 24.2｜Primary Cycle Receipt

```yaml
LIHUO_PRIMARY_CYCLE_RECEIPT:
  governing_cycle_ref: REQUIRED

  opening_snapshot_ref: REQUIRED
  generation_attempt_refs: []
  generation_attempt_primary_binding_refs: []
  main_invocation_binding_refs: []

  admission_return_refs: []
  canonical_main_return_binding_refs: []
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
CYCLE RECEIPT
=
COMPOSITION OF
QUALIFIED TRACE MATERIAL

NOT
A MAGIC CERTIFICATE OF OCCURRENCE
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


# 27｜V0.2.1 Interface Register

## ISSUE_1｜Generation Attempt relation

```text
STATUS
=
REPAIRED

RESULT
=
ATTEMPT IDENTITY DETACHED
FROM SINGLE-PRIMARY CONTAINMENT

PRIMARY RELATION
=
EXPLICIT BINDING
```

## ISSUE_2｜Main canonical contract reuse

```text
STATUS
=
REPAIRED

RESULT
=
L8 CONSUMES
MAIN_INVOCATION_IDENTITY
MAIN_TRANSIT_REQUEST_V5_1
MAIN_PREBOUND_INVOCATION_AUTHORITY
MAIN_ACTUAL_STATE_RETURN_V5_1

NO SHADOW AUTHORITATIVE MAIN CONTRACT
```

## ISSUE_3｜Coverage / Dirty / Reentry mixed state

```text
STATUS
=
REPAIRED

COVERAGE
!=
COMPUTE DEPENDENCY
!=
REENTRY QUALIFICATION
!=
CONTROL DISPOSITION
```

## ISSUE_4｜R3+ export through current Main return

```text
STATUS
=
OPEN / UPSTREAM CROSS-LAYER INTERFACE GAP
```

L8 不自行修 Main。

## ISSUE_5｜Universal event occurrence status

```text
STATUS
=
REPAIRED

EVENT CLAIM STATE
!=
EXECUTION STATE
!=
OBSERVATION STATE
!=
OUTCOME STATE
```

## ISSUE_6｜Receipt evidence ceiling

```text
STATUS
=
REPAIRED IN L8 SEMANTICS

ENGINEERING VALIDATION
=
STILL OPEN
```

## OPEN_2｜LLIA current owner name

```text
STATUS
=
HOLD / NON-BLOCKING
```

## OPEN_3｜Final Release owner

```text
STATUS
=
HOLD / NON-BLOCKING FOR L8 CORE
```

## OPEN_4｜Future L9

```text
STATUS
=
HOLD / NON-BLOCKING
```

## OPEN_5｜Evidence / Instrumentation ceiling

```text
STATUS
=
OPEN / NEXT CROSS-LAYER REVIEW
```

---


# 28｜V0.2.1 Interface Dry Run｜L8_DRYRUN_003

## 28.1｜Test Question

> **在不重畫 L8 主骨架的前提下，若 Attempt 改成跨 Primary relation、Main contracts 改為 canonical consumption、coverage/reentry/event/receipt 全部拆型，L8 是否仍能維持 Primary Cycle continuity 與 traceability？**

## 28.2｜R1

候選：

```text
A:
V0.2.1 canonical-interface model

B:
V0.2 shadow-schema model

C:
極薄 container，只記 refs 不做 typed binding
```

R1：

```text
A
=
PROVISIONAL_LEADER
```

理由：

- 不再錯綁 Attempt → one Primary；
- 不複製 Main identity / request / return contract；
- event record 不再把 claim / execution / observation / outcome 混成一軸；
- receipt semantics 與 evidence standing 對齊；
- L8 仍可維持 cycle continuity。

## 28.3｜O9

主要風險：

```text
RISK_1:
Canonical Main source currently lacks explicit R3+ export
in MAIN_ACTUAL_STATE_RETURN_V5_1.

RISK_2:
Foreign-key binding must not silently become new authority.

RISK_3:
Evidence-origin typing still needs L5 cross-layer ceiling table.

RISK_4:
Final release owner remains intentionally unresolved.
```

I9：

```text
RUNTIME I9 EXECUTION
=
NOT ESTABLISHED

DOCUMENT INTERFACE REPAIR
=
APPLIED
```

## 28.4｜R2

B 的反擊：

```text
Shadow schema is easier to read locally.
```

但失效：

```text
LOCAL READABILITY
!=
AUTHORITY TO FORK CANONICAL CONTRACT
```

C 的反擊：

```text
Pure refs reduce duplication further.
```

但失效：

```text
PURE REF LIST
without typed L8 binding
cannot support cycle continuity,
cross-primary attempt relation,
or event provenance checks.
```

R2：

```text
A
=
REMAINS UNIQUE QUALIFIED TOP
```

因此：

```text
A
=
VICTORY_ELIGIBLE
```

但 termination 仍不成立，因：

```text
UPSTREAM R3+ EXPORT CONTRACT GAP
=
OPEN

EVIDENCE / INSTRUMENTATION CEILING REVIEW
=
OPEN
```

## 28.5｜Dry Run Result

```text
V0.2.1 CORE INTERFACE SURGERY
=
PASS IN DOCUMENT-LEVEL INTERNAL EXERCISE

CROSS-LAYER EVENT CONTRACT REVIEW
=
READY TO ENTER

RUNTIME RATIFICATION
=
HOLD
```

永久鎖：

```text
SELF-DRYRUN
!=
INDEPENDENT VALIDATION
```

---


# 29｜V0.2.1 Corrected Self-Audit Verdict

```text
PRIMARY CYCLE MODEL
=
PASS

LINEAR PRIMARY CYCLE /
FIELD-LIKE MAIN COMPUTE
=
PASS

MAIN CYCLE-INTEGRITY BINDING
=
PASS

R-CCC MANDATORY BINDING
=
PASS

OWNER-SEPARATION DIRECTION
=
PASS

PRIMARY / ATTEMPT / INVOCATION MODEL
=
PASS AFTER IDENTITY REPAIR

GENERATION ATTEMPT SINGLE-PRIMARY CONTAINMENT
=
REMOVED

CANONICAL MAIN CONTRACT BINDING
=
PASS AFTER SHADOW-CONTRACT REMOVAL

POST-MAIN COVERAGE / DEPENDENCY / REENTRY TYPES
=
PASS AFTER SPLIT

R3+ SEMANTICS
=
PASS

R3+ CURRENT MAIN RETURN EXPORT
=
UPSTREAM INTERFACE GAP / OPEN

EVENT TYPE HYGIENE
=
PASS AFTER SPLIT

RECEIPT EVIDENCE CEILING
=
PASS IN SEMANTIC MODEL

MANIFESTATION ENUM REUSE
=
PASS / L7 CANONICAL CONSUMED UNTRANSLATED

EVIDENCE / INSTRUMENTATION ENGINEERING
=
OPEN

RUNTIME RATIFICATION
=
HOLD
```

---


# 30｜V0.2.1 Working Standing

```text
L8 V0.2.1-WORKING

CORE ARCHITECTURE
=
PASS

PRIMARY-CYCLE / MAIN-INVOCATION NESTING
=
PASS

GENERATION-ATTEMPT RELATION
=
PASS AFTER REPAIR

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

CANONICAL MAIN CONTRACT REUSE
=
PASS

EVENT / RECEIPT TYPE HYGIENE
=
PASS

RECEIPT EVIDENCE CEILING
=
PASS IN SEMANTIC MODEL

UPSTREAM R3+ RETURN CONTRACT
=
OPEN CROSS-LAYER GAP

EVIDENCE / INSTRUMENTATION BOUNDARY
=
OPEN

VERDICT
=
PASS_WITH_UPSTREAM_INTERFACE_GAP

CROSS-LAYER EVENT CONTRACT REVIEW
=
READY

RUNTIME RATIFICATION
=
HOLD

HOST DEPLOYMENT
=
NOT ESTABLISHED
```

---

# 31｜下一階段

V0.2.1 不直接進 Host。

下一階段：

```text
V0.2.1 CROSS-LAYER EVENT CONTRACT REVIEW
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

# 33｜V0.2.1 核心收束

> **理火不是因為喜歡程序，才要求 R2。**

> **理火是因為第一輪生成最容易把自己的「先來、最亮、最順、最像完成」誤當成有資格停止，所以制度上不把第一次勝利交給它自己信任。**

而 L8 的工作不是替 Main 思考。

L8 的工作是：

> **讓一次理火生成真正有身份、有先後、有 owner、有 reentry、有 receipt、有 evidence standing，並且在最後能被合法重建，而不是事後編成一個看起來像曾經發生過的故事。**
