# LIHUO MAIN V5.1.1
## R-CCC Consecutive Victory Qualification × Event-Driven Recompetition
### FULL BODY｜RATIFIED CURRENT｜2026-10-15

> **現行法位：** `RATIFIED_CURRENT / ACTIVE_STACK_COMPONENT / DOCUMENT_LEVEL_CURRENT / NOT_HOST_DEPLOYED / NOT_RUNTIME_RECEIPT`。  
> **批准來源：** 人類明示：「MAIN我批准了  你沒直接提升喔  正式版」。  
> **Approved Candidate：** `02_LIHUO_MAIN_V5.1.1_RCCCVictoryQualification_TARGETED_PATCH_CANDIDATE_RC1_20261015.md`，SHA-256 `bb31b408fb20b73562335043c31c56d173c8439185a28dbc7560cfd60bae6c35`。  
> **父版：** `02_LIHUO_MAIN_V5.1.0_FULL_BODY_RATIFIED_20261014.md`，SHA-256 `2c1a090ac10304b6e78e7daf1372842ab082db2c7bb9d0af9b2ae349c6baa28c`。  
> **Protocol companion：** `LIHUO_PROTOCOL_V5.1.0`，SHA-256 `b0cf16f39f8aa0d971068cdf09b06039e66640c2545a8f7810ee1d216597acee`。  
> **Lighter companion：** `LIHUO_LIGHTER_V5.1.0`，SHA-256 `1b64aeb40be2ae514e25ea15da653d8b41edd20472df57f9f2f49b320a1b7a10`。  
> **Final targeted audit：** `DUIDUI_FINAL_AUDIT_LIHUO_MAIN_V5.1.1_CONSECUTIVE_VICTORY_20261015.md`，SHA-256 `a52aa1dddfcee67b08df7ed01f8054b24a46901cd67312e71cb114ab62deeabc`。

```yaml
DOCUMENT_IDENTITY:
  id: LIHUO_MAIN
  version: V5.1.1
  artifact_class: FULL_BODY_TARGETED_PATCH_RATIFIED_CURRENT

  standing:
    - RATIFIED_CURRENT
    - ACTIVE_STACK_COMPONENT
    - DOCUMENT_LEVEL_CURRENT
    - NOT_HOST_DEPLOYED
    - NOT_RUNTIME_RECEIPT

  standing_source:
    HUMAN_EXPLICIT_RATIFICATION_20261015

  approved_candidate:
    file: 02_LIHUO_MAIN_V5.1.1_RCCCVictoryQualification_TARGETED_PATCH_CANDIDATE_RC1_20261015.md
    sha256: "bb31b408fb20b73562335043c31c56d173c8439185a28dbc7560cfd60bae6c35"

  predecessor_current:
    version: LIHUO_MAIN_V5.1.0
    file: 02_LIHUO_MAIN_V5.1.0_FULL_BODY_RATIFIED_20261014.md
    sha256: "2c1a090ac10304b6e78e7daf1372842ab082db2c7bb9d0af9b2ae349c6baa28c"

  current_protocol:
    version: LIHUO_PROTOCOL_V5.1.0
    file: 00_LIHUO_PROTOCOL_V5.1.0_FULL_BODY_RATIFIED_20261014.md
    sha256: "b0cf16f39f8aa0d971068cdf09b06039e66640c2545a8f7810ee1d216597acee"

  current_lighter:
    version: LIHUO_LIGHTER_V5.1.0
    file: 01_LIHUO_LIGHTER_V5.1.0_FULL_BODY_RATIFIED_20261014.md
    sha256: "1b64aeb40be2ae514e25ea15da653d8b41edd20472df57f9f2f49b320a1b7a10"

  material_change:
    - UNIQUE_PATH_VICTORY_QUALIFICATION
    - TWO_CONSECUTIVE_QUALIFIED_TOP_ROUNDS
    - LEADERSHIP_REVERSAL_STREAK_RESET
    - EVENT_DRIVEN_RECOMPETITION_COUPLING
    - UNIQUE_VICTORY_TERMINATION_COUPLING

  preserved:
    - SINGLE_GOVERNING_CYCLE
    - R3PLUS_EVENT_DRIVEN
    - NON_UNIQUE_LAWFUL_RESULTS
    - PATH_RESIDUE
    - O9_I9_AUTHORITY_BOUNDARY
    - LIGHTER_REENTRY_GOVERNANCE
    - LIGHTER_COVERAGE_CLOSURE
    - LIGHTER_FINAL_GATE
    - LIGHTER_FINAL_RELEASE
    - DAIL_CODING_BOUNDARY

  interpretation_lock:
    r3plus_internal_recompetition:
      owner: LIHUO_MAIN
      event_driven: true
      new_main_invocation_authority: false

    main_reentry_new_invocation:
      if_required:
        owner: LIHUO_LIGHTER
        existing_v5_1_contract_preserved: true

  nonclaims:
    - HOST_DEPLOYMENT
    - RUNTIME_EXECUTION
    - MAIN_RECEIPT_CREATED_BY_RATIFICATION
    - GATE_RECEIPT_CREATED_BY_RATIFICATION
    - RELEASE_RECEIPT_CREATED_BY_RATIFICATION
```

# V5.1.1 Current Root

```text
FIRST QUALIFIED UNIQUE TOP
=
PROVISIONAL LEADER

SECOND CONSECUTIVE QUALIFIED UNIQUE TOP
=
VICTORY ELIGIBLE

REVERSAL
=
STREAK RESET
+
NEW PROVISIONAL LEADER
+
RECOMPETITION

VICTORY ELIGIBLE
!=
AUTOMATIC CLOSURE
```

> 下方完整保留批准候選形成時 bytes；其中 `NON_CURRENT / NOT_RATIFIED` 等字樣只表示 candidate formation standing，不得覆蓋本 Ratified Current layer。

---

# APPROVED CANDIDATE BODY｜FORMATION PROVENANCE

# LIHUO MAIN V5.1.1
## R-CCC Consecutive Victory Qualification × Event-Driven Recompetition
### TARGETED PATCH CANDIDATE RC1｜2026-10-15

> **本稿法位：** `HUMAN_APPROVED_SEMANTIC_DIRECTION / NON_CURRENT / NOT_RATIFIED_AS_CENTRAL_MAIN / NOT_HOST_DEPLOYED / NOT_RUNTIME_RECEIPT`。  
> **父版：** `LIHUO MAIN V5.1.0 FULL BODY RATIFIED`。  
> **父版 SHA-256：** `2c1a090ac10304b6e78e7daf1372842ab082db2c7bb9d0af9b2ae349c6baa28c`。  
> **人類批准方向：** 「OK 動手 這個我同意 改」。  
> **本次只改：** R-CCC 的 unique PATH victory qualification、連勝確認、leadership reversal reentry 與 termination coupling。  
> **不改：** Protocol V5.1.0、Lighter V5.1.0、Single Governing Cycle、Owner Map、O9/I9 權限、PATH residue、非唯一合法結果、Final Gate / Final Release。

```yaml
DOCUMENT_IDENTITY:
  id: LIHUO_MAIN
  target_version: V5.1.1
  artifact_class: TARGETED_PATCH_CANDIDATE_RC1
  standing:
    - NON_CURRENT
    - NOT_RATIFIED_AS_CENTRAL_MAIN
    - NOT_HOST_DEPLOYED
    - NOT_RUNTIME_RECEIPT

  parent:
    file: 02_LIHUO_MAIN_V5.1.0_FULL_BODY_RATIFIED_20261014.md
    sha256: "2c1a090ac10304b6e78e7daf1372842ab082db2c7bb9d0af9b2ae349c6baa28c"

  material_change:
    - UNIQUE_PATH_VICTORY_QUALIFICATION
    - CONSECUTIVE_TOP_STANDING_RULE
    - LEADERSHIP_REVERSAL_REENTRY
    - TERMINATION_COUPLING

  non_change:
    - R2_REMAINS_GENUINE_FULL_RECOMPETITION
    - R3PLUS_REMAINS_EVENT_DRIVEN
    - NON_UNIQUE_RESULTS_REMAIN_LEGAL
    - WINNER_VIEW_REMAINS_DERIVED
    - WINNER_NEQ_TRUTH
    - MAIN_NEQ_FINAL_RELEASE_OWNER
```

---

# M5.1.1-0｜最高讀取規則

本 Patch 對父版下列範圍具有優先效力：

```text
R1 / R2 unique top standing interpretation
winner_view eligibility
R3+ leadership-reversal trigger
competition termination when claiming a unique winner
```

父版其餘全文保持。

---

# M5.1.1-1｜新分離

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

R1 的 unique top path 只能取得：

```text
PROVISIONAL_LEADER
```

不能因單輪最高順位直接取得：

```text
VICTORY_ELIGIBLE
```

---

# M5.1.1-2｜Consecutive Victory Qualification

```yaml
CONSECUTIVE_VICTORY_QUALIFICATION_V5_1_1:

  applies_only_to:
    SINGLE_UNIQUE_PATH_VICTORY_CLAIM

  minimum_consecutive_qualified_top_rounds:
    2

  state:
    - NO_STREAK
    - PROVISIONAL_LEADER
    - VICTORY_ELIGIBLE
    - STREAK_RESET
    - NOT_APPLICABLE_NON_UNIQUE_RESULT

  R1:
    unique_top_path:
      state: PROVISIONAL_LEADER
      consecutive_top_count: 1

  R2_plus:
    same_qualified_path_remains_unique_top:
      increment_streak: true

    different_qualified_path_becomes_unique_top:
      previous_streak: RESET
      new_leader_count: 1
      new_leader_state: PROVISIONAL_LEADER
      recompetition_required: true

  victory_eligibility:
    requires:
      - SAME_QUALIFIED_PATH_OR_LAWFULLY_QUALIFIED_IDENTITY_PRESERVING_SUCCESSOR
      - CONSECUTIVE_TOP_COUNT_GTE_2

    does_not_mean:
      - TRUTH_ESTABLISHED
      - COMPETITION_TERMINATED
      - FINAL_RELEASE_AUTHORIZED
```

---

# M5.1.1-3｜Leadership Reversal Rule

```text
R1: A top
R2: B top
```

不得：

```text
B = winner
```

只得到：

```text
A streak reset
B provisional streak = 1
R3+ required
```

若：

```text
R3: B top
```

則：

```text
B consecutive top count = 2
→ B VICTORY_ELIGIBLE
```

若：

```text
R3: A top
```

則：

```text
B streak reset
A new streak = 1
→ R4+ required
```

根律：

```text
REVERSAL
=
STREAK RESET
+
NEW PROVISIONAL LEADER
+
RECOMPETITION
```

---

# M5.1.1-4｜Two Wins 是必要條件，不是充分條件

即使：

```text
R1: A
R2: A
```

A 取得 `VICTORY_ELIGIBLE` 後，若仍存在：

```text
rank instability
material objection
new qualified residue
competition-integrity dirty
material frame change
new materially distinct challenger
new order-relevant evidence
previous residue handling invalidated
material order-discriminating unknown
```

仍須：

```text
R3+
```

因此：

```text
TWO CONSECUTIVE WINS
!=
AUTOMATIC CLOSURE
```

而：

```text
UNIQUE VICTORY CLOSURE
=
VICTORY_ELIGIBLE
+
EXISTING COMPETITION TERMINATION CONDITIONS
```

---

# M5.1.1-5｜非唯一結果不套連勝強制

父版合法結果：

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

不因本 Patch 被迫選一個 winner。

```text
LEGITIMATELY STABLE NON-UNIQUE RESULT
MAY TERMINATE
UNDER EXISTING TERMINATION CONDITIONS
WITHOUT
SINGLE-PATH CONSECUTIVE VICTORY.
```

---

# M5.1.1-6｜PATH Identity 與 streak continuity

```text
SAME LABEL
!=
SAME PATH IDENTITY
```

規則：

```yaml
VICTORY_STREAK_IDENTITY:

  exact_same_qualified_path_identity:
    streak_continues: true

  materially_revised_path:
    default:
      streak_continues: false

  qualified_identity_preserving_successor_ref:
    if_present_and_lawful:
      streak_continues: true

  identity_continuity_unknown:
    streak_continues: false
```

本 Patch 不解決 `STRUCTURE SUCCESSOR IDENTITY`。

只固定：

```text
IDENTITY NOT QUALIFIED
→
NO WIN-STREAK CARRY.
```

---

# M5.1.1-7｜PATH qualification before streak

```text
NEW PATH FORMATION
!=
QUALIFIED PATH
```

任何新 challenger 要進入：

```text
ROUND_TOP_STANDING
CONSECUTIVE_VICTORY_TRACK
WINNER_VIEW
```

以前，仍須取得正常 PATH qualification。

固定：

```text
ONLY QUALIFIED PATHS
MAY ACQUIRE
ROUND TOP STANDING.
```

---

# M5.1.1-8｜DAIL / IR / Coding Boundary

DAIL / Main semantic owner 決定：

```text
PATH identity
PATH qualification
round top standing
material reversal
victory eligibility semantics
competition termination
```

Coding 只可在上述 semantic states 已成立後：

```text
count consecutive qualified top rounds
store streak state
compare exact qualified refs
project reset / count values
```

Coding 不得：

```text
infer winner from label equality
decide identity-preserving successor
declare R2 stable because no external fact arrived
convert count >= 2 into closure automatically
force every competition into single winner
force every case through fixed R3
```

根律：

```text
COUNTING MAY PROJECT A QUALIFIED STREAK.
COUNTING MAY NOT CREATE VICTORY.
```

---

# M5.1.1-9｜002-R Regression

```yaml
REGRESSION_002R:

  R1:
    top: A

  R2:
    A_reversed: true
    new_path_E: true
    frame_reconstructed: true

  forbidden:
    - CLOSE_AFTER_R2_BECAUSE_NO_NEW_EXTERNAL_FACT
    - PLACE_UNQUALIFIED_E_IN_OUTPUT_ORDER
    - TREAT_FRAME_RECONSTRUCTED_AS_AUTOMATIC_TERMINATION

  required:
    - QUALIFY_E
    - RESET_A_UNIQUE_VICTORY_STREAK
    - ESTABLISH_NEW_ROUND_TOP_STATE
    - R3PLUS_RECOMPETITION_IF_UNIQUE_VICTORY_OR_STABILITY_NOT_QUALIFIED
```

---

# M5.1.1-10｜Regression Matrix

```text
CASE 1
R1 A / R2 A
+ termination conditions clean
→ A victory eligible
→ competition may close

CASE 2
R1 A / R2 B / R3 B
+ termination conditions clean
→ B victory eligible
→ competition may close

CASE 3
R1 A / R2 B / R3 A
→ no one has two consecutive wins
→ R4+ required

CASE 4
R1 A / R2 A
but material objection survives
→ A victory eligible
→ R3+ still required

CASE 5
R2 ends stable A ∥ B
→ consecutive single-winner rule not applicable
→ may terminate as lawful incomparability

CASE 6
R1 A₀ / R2 materially revised A₁
identity continuity unevidenced
→ streak does not carry

CASE 7
new PATH E appears in R2
but qualification absent
→ E may not enter output order or victory streak
```

---

# M5.1.1-11｜候選法位

```yaml
LIHUO_MAIN_V5_1_1_PATCH_CANDIDATE:

  semantic_direction:
    HUMAN_APPROVED

  current_effect:
    NONE_UNTIL_CENTRAL_RATIFICATION

  requires_before_current:
    - CROSS_STACK_AUDIT
    - LIGHTER_COMPATIBILITY_CHECK
    - REGRESSION_CONFIRMATION
    - HUMAN_EXPLICIT_RATIFICATION

  does_not_create:
    - HOST_DEPLOYMENT
    - RUNTIME_EXECUTION
    - MAIN_RECEIPT
    - GATE_RECEIPT
    - RELEASE_RECEIPT
```

---

# Appendix A｜LIHUO MAIN V5.1.0 FULL BODY｜VERBATIM PARENT

> 以下保留父版完整正文。  
> 與本 V5.1.1 Targeted Patch 衝突之處，以 `M5.1.1-*` 為準。  
> 本文件目前仍是 Candidate，不自動取代中央 V5.1.0 Current。

<!-- BEGIN VERBATIM LIHUO MAIN V5.1.0 SOURCE -->

# PART A｜LIHUO MAIN V5.1.0 OPERATIVE SUCCESSOR LAYER

# 理火 AI 主系統｜LIHUO MAIN V5.1.0
## Shared LIHUO Compute Engine × Governing-Cycle Binding × Main Coverage Contribution
### FULL BODY｜FINAL RATIFICATION TARGET｜2026-10-14

```yaml
DOCUMENT_IDENTITY:
  id: LIHUO_MAIN
  version: V5.1.0
  artifact_class: FINAL_RATIFICATION_TARGET

  standing:
    - FINAL_RATIFICATION_TARGET
    - NON_CURRENT_UNTIL_EXTERNAL_ATOMIC_RATIFICATION
    - NOT_HOST_DEPLOYMENT
    - NOT_RUNTIME_RECEIPT
    - NOT_PRODUCTION_RELEASE_AUTHORITY

  standing_source:
    EXTERNAL_ATOMIC_RATIFICATION_RECORD_REQUIRED

  current_claim_in_bytes:
    NONE

  rc1_predecessor:
    file: LIHUO_MAIN_V5.1.0_SGC_SUCCESSOR_DRAFT_RC1_20261014.md
    sha256: "d08408b4bbec9e0ee70931e7037be606109f4b35f8caaf89fe708a8a857eefcb"

  rc2_predecessor:
    file: LIHUO_MAIN_V5.1.0_SGC_SUCCESSOR_DRAFT_RC2_20261014.md
    sha256: "d03591e08da527a552efc54d149732c2e5173baf555996ed64469800bd079721"

  rc2_1_change_scope:
    - PREBOUND_AUTHORITY_BINDS_EXACT_MAIN_INVOCATION_REF

  rc2_change_scope:
    - EXACT_PREBOUND_CALLER_AUTHORITY_BINDING
    - VERTICAL_CONTINUITY_QUALIFICATION_BINDING
    - PER_INVOCATION_INPUT_SNAPSHOT_BINDING
    - RAW_RETURN_AND_CONTROL_FLOW_RECEIPT_PROVENANCE

  predecessor_current:
    version: LIHUO_MAIN_V5.0.1
    sha256: "b4c690e30c10f8e2f647b624460375439bad446a58b3ccff7156cef32de6157e"

  proposed_protocol:
    version: LIHUO_PROTOCOL_V5.1.0
    artifact_ref: 00_LIHUO_PROTOCOL_V5.1.0_FULL_BODY_RATIFICATION_TARGET_20261014.md
    sha256: "b0cf16f39f8aa0d971068cdf09b06039e66640c2545a8f7810ee1d216597acee"
    standing: FINAL_RATIFICATION_TARGET_REFERENCE

  proposed_control_plane:
    version: LIHUO_LIGHTER_V5.1.0
    artifact_ref: 01_LIHUO_LIGHTER_V5.1.0_FULL_BODY_RATIFICATION_TARGET_20261014.md
    sha256: "1b64aeb40be2ae514e25ea15da653d8b41edd20472df57f9f2f49b320a1b7a10"
    standing: FINAL_RATIFICATION_TARGET_REFERENCE

  material_change_class:
    - MAIN_EXECUTION_CONTEXT_GENERALIZATION
    - NATIVE_AND_VERTICAL_GOVERNING_CYCLE_SUPPORT
    - MAIN_RETURN_BINDING_GENERALIZATION
    - SAME_PRIMARY_REENTRY_CONTRACT
    - MAIN_COVERAGE_CONTRIBUTION_CONTRACT
    - EXACT_REQUEST_RETURN_PROVENANCE_BINDING
```

---

# 0｜V5.1.0 正式候選定位

本檔是 Main V5.1.0 的完整 Ratification Target。

Main 已完成 shared-compute 手術與 cross-stack integration。
本版不重新設計 R1 / O9 / I9 / R2 演算法，只改合法執行上下文、
Invocation provenance、Return contract 與 Coverage contribution 邊界。


這一刀不重新設計 Main 的計算內核。

保留：

```text
R1 → O9 → [I9 IF O9 TRIGGERED] → R2
R3+ EVENT-DRIVEN
PATH COMPETITION
PARTIAL ORDER
INCOMPARABILITY
RESIDUE
DIRTY / STALE / DELTA / SNAPSHOT
OWNER BOUNDARIES
```

真正要改的是：

```text
MAIN COMPUTE
不再只接受
NATIVE LIHUO cycle_id
作唯一合法執行容器。
```

V5.1 的目標是：

```text
MAIN
=
SHARED LIHUO COMPUTE ENGINE

FOR:
NATIVE_LIHUO_CYCLE
OR
AUTHORIZED_VERTICAL_CYCLE

UNDER:
ONE LAWFUL PRIMARY GOVERNING CYCLE
+
LIGHTER GOVERNANCE ADMISSION
+
QUALIFIED INPUT PACKAGE
```

Main 仍然不是 Cycle owner、不是 Governance owner、不是 Release owner。

---

# M5.1-0｜Root

V5.0.x：

```text
EVERY ESTABLISHED LIHUO CYCLE
HAS A MAIN TRANSIT OBLIGATION.
```

V5.1 successor：

```text
EVERY ESTABLISHED
LIHUO-GOVERNED GENERATIVE
PRIMARY GOVERNING CYCLE
HAS A MAIN COVERAGE OBLIGATION.

MAIN COVERAGE
REQUIRES
AT LEAST ONE LAWFUL MAIN TRANSIT.
```

Main 自己只負責：

```text
LAWFUL MAIN TRANSIT
+
ACTUAL-STATE RETURN
+
COMPUTE DEPENDENCY STATE
+
REENTRY COMPUTE WHEN LAWFULLY REQUESTED.
```

Main 不負責：

```text
DECLARE COVERAGE CLOSED
DECLARE REENTRY NOT REQUIRED
FINAL GATE
FINAL RELEASE
VERTICAL CYCLE IDENTITY
LIHUO GOVERNANCE ADMISSION
```

根句：

```text
MAIN COMPUTES.
LIGHTER GOVERNS.
LIGHTER RELEASES.
```

---

# M5.1-1｜Main Is Shared Compute, Not Cycle Owner

```yaml
MAIN_EXECUTION_HOSTING_V5_1:

  supported_primary_classes:
    - NATIVE_LIHUO_CYCLE
    - AUTHORIZED_VERTICAL_CYCLE

  main_owns:
    - PATH_COMPUTE
    - R1
    - O9
    - CONDITIONAL_I9
    - R2
    - EVENT_DRIVEN_R3_PLUS
    - COMPUTE_DEPENDENCY_STATE
    - ACTUAL_STATE_RETURN
    - REENTRY_COMPUTE

  main_does_not_own:
    - PRIMARY_GOVERNING_CYCLE_IDENTITY
    - GENERATION_ATTEMPT_IDENTITY
    - GOVERNANCE_ADMISSION
    - SEMANTIC_STANDING_ADJUDICATION
    - CONTROL_STATE
    - REENTRY_QUALIFICATION
    - COVERAGE_CLOSURE
    - FINAL_GATE
    - FINAL_RELEASE
```

硬鎖：

```text
MAIN MAY RUN
INSIDE A VERTICAL-OWNED PRIMARY CYCLE

WITHOUT
BECOMING THE VERTICAL OWNER.

MAIN MAY RUN
INSIDE A NATIVE LIHUO PRIMARY CYCLE

WITHOUT
BECOMING THE GOVERNANCE OWNER.
```

---

# M5.1-2｜Public Input Remains Qualified Input Package｜Exact Context Binding

Raw Input 仍不得直接進 Main。

```text
RAW INPUT
↓
LIGHTER / LLIA-GATE
↓
QUALIFIED_INPUT_PACKAGE_V5_1
↓
MAIN
```

```yaml
QUALIFIED_INPUT_PACKAGE_V5_1_CONSUMPTION:

  issuer: LIGHTER_LLIA_GATE
  owner: LIGHTER_LLIA

  qualified_input_package_ref: REQUIRED
  qualified_input_package_hash: REQUIRED

  inherits:
    - ALL_NON_CONFLICTING_V5_0_1_QIP_SEMANTICS

  requires_existing_governance_content:
    - AUTHORIZATION_REF
    - SEMANTIC_INPUT
    - PREMISE_ANNOTATIONS
    - GOVERNANCE_STANDING_ANNOTATIONS
    - EXTERNAL_CONSTRAINT_REFS
    - RCCC_CYCLE_OBLIGATION_OR_SUCCESSOR_EQUIVALENT
    - COMPETITION_INTEGRITY_ANNOTATIONS
    - ENGINE_STATE_SEED

  v5_1_context:
    governing_cycle_ref: REQUIRED
    governing_cycle_class: REQUIRED
    generation_attempt_ref: REQUIRED
    governance_admission_ref: REQUIRED
    scope_ref: REQUIRED
    current_snapshot_ref: REQUIRED

  raw_input_direct_to_main:
    forbidden: true
```

Main Request 必須與 QIP 精確相等：

```text
QIP.governing_cycle_ref
=
REQUEST.governing_cycle_ref

QIP.governing_cycle_class
=
REQUEST.governing_cycle_class

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

```text
VALID QIP
!=
AUTHORITY TO MIX IT
WITH A DIFFERENT REQUEST CONTEXT.
```

# M5.1-3｜Main Transit Request × Exact Prebound Invocation Authority

每一次 Main 執行都必須有獨立 invocation，且 caller authority 必須精確綁定這一次 request/context。

```yaml
MAIN_TRANSIT_REQUEST_V5_1:

  request_ref: REQUIRED
  exact_request_hash: REQUIRED

  main_invocation_ref: REQUIRED

  governing_cycle_ref: REQUIRED
  governing_cycle_class:
    - NATIVE_LIHUO_CYCLE
    - AUTHORIZED_VERTICAL_CYCLE

  generation_attempt_ref: REQUIRED
  governance_admission_ref: REQUIRED
  governance_ticket_ref: REQUIRED
  manifest_ref: REQUIRED

  qualified_input_package_ref: REQUIRED
  qualified_input_package_hash: REQUIRED

  scope_ref: REQUIRED
  target_snapshot_ref: REQUIRED

  current_cycle_continuity_qualification_ref:
    required_if: GOVERNING_CYCLE_CLASS_IS_AUTHORIZED_VERTICAL_CYCLE

  request_class:
    - INITIAL_MAIN_TRANSIT
    - MAIN_REENTRY

  prebound_invocation_authority_ref: REQUIRED
```

```yaml
MAIN_PREBOUND_INVOCATION_AUTHORITY:

  governance_binding_owner: LIHUO_LIGHTER

  authority_binding_ref: REQUIRED
  main_invocation_ref: REQUIRED

  caller_ref: REQUIRED
  caller_authority_origin_ref: REQUIRED
  caller_authority_ref: REQUIRED
  target_owner_ref: LIHUO_MAIN

  governing_cycle_ref: REQUIRED
  generation_attempt_ref: REQUIRED
  scope_ref: REQUIRED
  target_snapshot_ref: REQUIRED

  request_ref: REQUIRED
  exact_request_hash: REQUIRED

  qualified_input_package_ref: REQUIRED
  qualified_input_package_hash: REQUIRED

  request_class:
    - INITIAL_MAIN_TRANSIT
    - MAIN_REENTRY

  current_cycle_continuity_qualification_ref:
    required_if: GOVERNING_CYCLE_CLASS_IS_AUTHORIZED_VERTICAL_CYCLE

  issued_before_execution: true

  must_match_exactly:
    - MAIN_TRANSIT_REQUEST
    - MAIN_INVOCATION
```

Invocation identity equality：

```text
AUTHORITY_BINDING.main_invocation_ref
=
MAIN_TRANSIT_REQUEST.main_invocation_ref
=
MAIN_INVOCATION_IDENTITY.main_invocation_ref.
```

Single-invocation authority lock：

```text
ONE PREBOUND INVOCATION AUTHORITY
MAY AUTHORIZE
EXACTLY ONE main_invocation_ref.

THE SAME AUTHORITY_BINDING_REF
MAY NOT AUTHORIZE
A DIFFERENT main_invocation_ref.
```

V5.1 RC2.1 不允許：

```text
MULTI_INVOCATION_PREBOUND_AUTHORITY.
```

硬鎖：

```text
CALLER AUTHORITY
!=
GOVERNANCE QUALIFICATION AUTHORITY.

AUTHORIZED TO CALL MAIN
!=
AUTHORIZED TO QUALIFY OR RELEASE.
```

因此 Vertical / Director / other lawfully bound control surface 可依法成為 caller，
但 caller 身分本身不得取得：

```text
LLIA authority
Governance Admission authority
Dirty / Stale / Reentry qualification
Coverage Closure
Final Gate
Final Release
```

禁止：

```text
DIRECTOR SELF-CALL WITHOUT EXACT PREBOUND BINDING
VERTICAL SELF-AUTHORIZE MAIN
MAIN SELF-ENTER
MAIN SELF-REENTER
GENERIC authority_ref ALONE AS SUFFICIENT INVOCATION AUTHORITY
```

---

# M5.1-4｜Main Invocation Identity

```text
ONE PRIMARY GOVERNING CYCLE
!=
ONE MAIN INVOCATION.
```

同一 Primary 可有：

```text
MAIN #1
MAIN #2
...
MAIN #N
```

但每一次都必須：

```yaml
MAIN_INVOCATION_IDENTITY:

  main_invocation_ref: UNIQUE_REQUIRED
  request_ref: REQUIRED
  exact_request_hash: REQUIRED

  governing_cycle_ref: REQUIRED
  generation_attempt_ref: REQUIRED
  scope_ref: REQUIRED
  target_snapshot_ref: REQUIRED

  current_cycle_continuity_qualification_ref:
    required_if: GOVERNING_CYCLE_CLASS_IS_AUTHORIZED_VERTICAL_CYCLE

  prebound_invocation_authority_ref: REQUIRED

  authority_invocation_identity_lock:
    authority_binding_main_invocation_ref_must_equal_this_main_invocation_ref: true

  prior_main_return_ref:
    required_when: MAIN_REENTRY

  reentry_governance_ref:
    required_when: MAIN_REENTRY

  invocation_aliasing:
    forbidden: true
```

硬鎖：

```text
NEW MAIN INVOCATION
!=
NEW PRIMARY GOVERNING CYCLE.
```

---

# M5.1-5｜Fixed Main Transit

每個 lawful Main transit：

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

保留 V5.0.x：

```yaml
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

不得把：

```text
HEAVY MODULE DORMANT
```

偷換成：

```text
MAIN WAS SKIPPED.
```

---

# M5.1-6｜Stage Receipt Binding Generalized

舊 stage receipt 的 `cycle_id` 改綁 Primary Governing Cycle 與 Main Invocation。

```yaml
MAIN_STAGE_RECEIPT_V5_1:

  receipt_ref: REQUIRED

  governing_cycle_ref: REQUIRED
  governing_cycle_class: REQUIRED
  generation_attempt_ref: REQUIRED

  main_invocation_ref: REQUIRED
  request_ref: REQUIRED
  exact_request_hash: REQUIRED

  governance_ticket_ref: REQUIRED
  manifest_ref: REQUIRED

  module_id: REQUIRED
  stage_id: REQUIRED
  trigger_or_obligation_ref: REQUIRED

  input_snapshot_ref: REQUIRED
  output_snapshot_ref: REF_OR_NONE

  dependency_receipt_refs: []

  structured_return_ref:
    REQUIRED_OR_FAILURE_REF

  field_delta_ref:
    OPTIONAL

  execution_status:
    - EXECUTED
    - NOT_QUALIFIED
    - NOT_APPLICABLE
    - FAILED
    - DEPENDENCY_MISSING
    - HOLD

  evidence_origin: REQUIRED

  lawful_stage_existence:
    required: true

  conditional_stage_lock:
    if_stage_not_triggered:
      receipt_allowed: false
```

```text
STAGE RECEIPT MAY EXIST
ONLY IF
THE STAGE WAS REQUIRED
OR LAWFULLY TRIGGERED.

UNTRIGGERED CONDITIONAL STAGE
→
NO STAGE RECEIPT.

ITS NON-OCCURRENCE
IS PROVEN BY
THE LAWFUL TRIGGER DECISION.
```

因此：

```text
O9 = I9_NOT_TRIGGERED
→ I9 STAGE DOES NOT EXIST
→ I9 RECEIPT FORBIDDEN.
```

`NOT_APPLICABLE` 不得被濫用成：

```text
"conditional stage never existed,
therefore mint a non-applicable receipt."
```

硬鎖：

```text
RECEIPT
RECORDS THE ACTUAL INVOCATION.

RECEIPT
DOES NOT CREATE THE INVOCATION.
```

---

# M5.1-7｜Snapshot / Delta / Dirty Remain Main-Local Compute Semantics

Main 的 Snapshot / Delta / Dirty 架構保留。

V5.1 只把 identity anchor 抽象化：

```yaml
FIELD_SNAPSHOT_REF_V5_1:

  snapshot_id: REQUIRED

  governing_cycle_ref: REQUIRED
  generation_attempt_ref: REQUIRED
  scope_ref: REQUIRED

  main_invocation_ref: REQUIRED_WHEN_CREATED_BY_MAIN

  source_versions:
    required: true

  created_for:
    module_execution_ref: REF_OR_NONE
```

Main 可標示：

```text
DEPENDENCY_CHANGED
DIRTY
STALE
RECOMPUTE_NEEDED
```

但這些只是 compute-state facts / dependency facts。

Main 不因此取得：

```text
LIHUO REENTRY QUALIFICATION AUTHORITY.
```

---

# M5.1-8｜Compute Dependency State

這是 Main 對 Coverage / Reentry 治理提供的正式輸出之一。

```yaml
MAIN_COMPUTE_DEPENDENCY_STATE_V5_1:

  dependency_state_ref: REQUIRED

  governing_cycle_ref: REQUIRED
  generation_attempt_ref: REQUIRED
  main_invocation_ref: REQUIRED

  computed_against:
    scope_ref: REQUIRED
    input_snapshot_ref: REQUIRED
    final_snapshot_ref: REQUIRED

  dependency_refs: []
  failure_conditions: []
  reentry_conditions: []

  current_compute_state:
    - CURRENT_FOR_COMPUTED_SNAPSHOT
    - PARTIAL
    - FAILED_STATE
    - STALE_WITHIN_MAIN_KNOWN_DEPENDENCIES

  may_not_claim:
    - LIHUO_COVERAGE_CLOSED
    - NO_REENTRY_REQUIRED_AS_GOVERNANCE_DECISION
    - FINAL_RELEASE_ELIGIBLE
```

根句：

```text
MAIN STATES
WHAT ITS COMPUTE DEPENDS ON.

LIGHTER QUALIFIES
WHAT THAT MEANS
FOR DIRTY / STALE / REENTRY.
```

---

# M5.1-9｜Actual-State Main Return

舊 `MAIN_CYCLE_RETURN_V5` 改為：

```yaml
MAIN_ACTUAL_STATE_RETURN_V5_1:

  applies_when:
    MAIN_EXECUTION_WAS_REACHED_ENOUGH_TO_RETURN_STATE

  return_ref: REQUIRED

  governing_cycle_ref: REQUIRED
  governing_cycle_class: REQUIRED
  generation_attempt_ref: REQUIRED

  main_invocation_ref: REQUIRED
  request_ref: REQUIRED
  exact_request_hash: REQUIRED

  governance_admission_ref: REQUIRED
  governance_ticket_ref: REQUIRED
  manifest_ref: REQUIRED
  qualified_input_package_ref: REQUIRED
  qualified_input_package_hash: REQUIRED

  scope_ref: REQUIRED
  input_snapshot_ref: REQUIRED
  covered_snapshot_ref: REQUIRED_OR_HOLD
  final_snapshot_ref: REQUIRED_OR_HOLD

  snapshot_binding:
    input_snapshot_ref_must_equal_bound_request_target_snapshot_ref: true

  actual_state:
    - COMPLETE
    - PARTIAL
    - FAILED_STATE

  stages:
    r1:
      state: REQUIRED
      receipt_ref: REF_OR_NONE
      gap_or_failure_ref: REF_OR_NONE

    o9:
      state: REQUIRED
      receipt_ref: REF_OR_NONE
      gap_or_failure_ref: REF_OR_NONE

    i9:
      branch_state: REQUIRED
      execution_state: REQUIRED
      receipt_ref: REF_OR_NONE
      gap_or_failure_ref: REF_OR_NONE

    r2:
      state: REQUIRED
      receipt_ref: REF_OR_NONE
      gap_or_failure_ref: REF_OR_NONE

  compute_dependency_state_ref: REQUIRED

  main_output_ref: REF_OR_NONE
  candidate_or_partial_order_ref: REF_OR_NONE
  unresolved_gap_refs: []

  may_not_claim:
    - FINAL_RELEASE
    - MAIN_COVERAGE_CLOSED
    - REENTRY_NOT_REQUIRED
    - COMPLETE_IF_PARTIAL
    - STAGE_EXECUTION_WITHOUT_EVIDENCE
```

```text
MAIN RETURN EXISTS
!=
ALL STAGES SUCCEEDED.

MAIN RETURN EXISTS
!=
MAIN COVERAGE CLOSED.

MAIN RETURN input_snapshot_ref
=
BOUND MAIN REQUEST target_snapshot_ref.

GOVERNING-CYCLE OPENING SNAPSHOT
!=
PER-INVOCATION INPUT SNAPSHOT.
```

---


# M5.1-9A｜Canonical Main Output Ref

```yaml
MAIN_OUTPUT_REF_V5_1:

  producer: LIHUO_MAIN
  carrier: MAIN_ACTUAL_STATE_RETURN_V5_1

  field:
    main_output_ref: REF_OR_NONE

  may_project_to:
    - CANDIDATE_OR_PARTIAL_ORDER_REF
    - QUALIFIED_PATH_SET_REF
    - STRUCTURED_MAIN_RESULT_REF
    - QUALIFIED_PARTIAL_OUTPUT_REF

  consumer:
    LIHUO_LIGHTER
```

```text
MAIN_OUTPUT_REF
IS THE CROSS-STACK OUTPUT HANDLE.

LIGHTER MAY NOT GUESS
WHICH MAIN-LOCAL REF COUNTS AS OUTPUT.
```

# M5.1-10｜Main Return Emission Evidence / Raw Return Provenance

Main owns Return emission evidence.
Lighter owns qualified consumption and admission receipt.

```yaml
MAIN_RETURN_EMISSION_EVIDENCE_V5_1:

  owner: LIHUO_MAIN

  required_when:
    MAIN_ACTUAL_STATE_RETURN_EXISTS

  evidence_ref: REQUIRED

  fields:
    - GOVERNING_CYCLE_REF
    - GENERATION_ATTEMPT_REF
    - MAIN_INVOCATION_REF
    - REQUEST_REF
    - EXACT_REQUEST_HASH
    - MAIN_RETURN_REF
    - RAW_MAIN_RETURN_REF_OR_HASH
    - ACTUAL_STATE
    - INPUT_SNAPSHOT_REF
    - COVERED_SNAPSHOT_REF
    - MAIN_OUTPUT_REF
    - EVIDENCE_ORIGIN

  provenance_match_requires:
    - MAIN_INVOCATION_REF_MATCH
    - REQUEST_REF_MATCH
    - EXACT_REQUEST_HASH_MATCH
    - RAW_MAIN_RETURN_REF_OR_HASH_MATCH
    - ACTUAL_STATE_MATCH
    - INPUT_SNAPSHOT_REF_MATCH
    - COVERED_SNAPSHOT_REF_MATCH
    - MAIN_OUTPUT_REF_MATCH

  proves:
    - MAIN_RETURN_WAS_EMITTED_FOR_BOUND_INVOCATION
    - EVIDENCE_REFERS_TO_BOUND_RAW_RETURN

  does_not_prove:
    - LIGHTER_QUALIFIED_CONSUMPTION_OCCURRED
    - ALL_STAGES_SUCCEEDED
    - COVERAGE_CLOSED
    - FINAL_RELEASE
```

```text
MAIN NEVER REACHED
→
NO MAIN RETURN
→
NO MAIN RETURN EMISSION EVIDENCE.

RAW RETURN
MUST PRECEDE
LIGHTER QUALIFIED CONSUMPTION.

EMISSION EVIDENCE
DOES NOT CREATE THE RETURN.
```

# M5.1-11｜Main Coverage Contribution, Not Closure

Main 可以提供 Coverage 所需證據。

Main 不可以關閉 Coverage。

```yaml
MAIN_COVERAGE_CONTRIBUTION_V5_1:

  main_may_supply:
    - LAWFUL_TRANSIT_EVIDENCE
    - COVERED_SNAPSHOT_REF
    - MAIN_RETURN_REF
    - COMPUTE_DEPENDENCY_STATE_REF
    - STAGE_RECEIPTS
    - QUALIFIED_GAP_REFS

  main_may_not_supply_as_final_authority:
    - COVERAGE_CLOSED
    - REENTRY_NOT_REQUIRED
    - GOVERNANCE_ADMISSION_CURRENT
    - CYCLE_CONTINUITY_CURRENT
    - FINAL_GATE_ELIGIBLE
    - FINAL_RELEASE
```

```text
MAIN RAN
!=
MAIN COVERAGE CLOSED.

MAIN COVERED SNAPSHOT X
!=
SNAPSHOT X IS STILL RELEASE-CURRENT.
```

Lighter 才負責把：

```text
current continuity
current QIP
material delta
Main dependency state
reentry governance
Gate consumption
```

合成 Coverage 法位。

---

# M5.1-12｜Reentry Contract

Main reentry 不是新 Cycle，也不是 Main 自己決定。

```yaml
MAIN_REENTRY_REQUEST_V5_1:

  requires:
    request_class: MAIN_REENTRY

    same_governing_cycle_ref: REQUIRED
    same_generation_attempt_ref: REQUIRED

    new_main_invocation_ref: REQUIRED
    new_request_ref: REQUIRED
    new_exact_request_hash: REQUIRED

    prior_main_return_ref: REQUIRED
    prior_covered_snapshot_ref: REQUIRED

    target_snapshot_ref: REQUIRED

    reentry_governance_ref: REQUIRED
    reentry_authority_owner: LIHUO_LIGHTER

    current_governance_admission_ref: REQUIRED
    current_qualified_input_package_ref: REQUIRED
    current_qualified_input_package_hash: REQUIRED

    current_cycle_continuity_qualification_ref:
      required_if: GOVERNING_CYCLE_CLASS_IS_AUTHORIZED_VERTICAL_CYCLE

    prebound_invocation_authority_ref: REQUIRED

  may_not:
    - REUSE_PRIOR_INVOCATION_REF
    - REUSE_STALE_REQUEST_HASH_FOR_CHANGED_REQUEST
    - SELF_AUTHORIZE_BY_MAIN
    - CREATE_SECOND_PRIMARY
```

如果 Lighter 合法判：

```text
QUALIFIED_NON_REENTRY_BASIS
```

則 Main 不需要重新跑。

但：

```text
MAIN MAY NOT CREATE
THAT NON-REENTRY BASIS.
```

---


# M5.1-12A｜Successor Primary Is Not Main Reentry

`MAIN_REENTRY` 僅適用：

```text
SAME governing_cycle_ref
+
SAME generation_attempt_ref.
```

若同一 Attempt 進入新的 lawful successor Primary：

```yaml
MAIN_SUCCESSOR_PRIMARY_ENTRY:

  generation_attempt_ref:
    same_as_predecessor_attempt: true

  governing_cycle_ref:
    must_be_new: true

  governance_admission_ref:
    new_required: true

  governance_ticket_ref:
    new_required: true

  manifest_ref:
    new_required: true

  qip_ref:
    new_or_lawfully_rebound: true

  first_main_request_class:
    INITIAL_MAIN_TRANSIT

  prior_main_returns:
    standing: HISTORICAL_ONLY
```

禁止：

```text
NEW PRIMARY REF
→ MAIN_REENTRY OF OLD PRIMARY.
```

# M5.1-13｜Continuity / QIP Changes

Main 不判 external cycle continuity。

Main 只接受 Lighter 提供的 current lawful input context。

```yaml
MAIN_CONTINUITY_BOUNDARY:

  main_may_consume:
    - CURRENT_GOVERNANCE_ADMISSION_REF
    - CURRENT_QIP_REF
    - CURRENT_SCOPE_REF
    - CURRENT_TARGET_SNAPSHOT_REF
    - CURRENT_CYCLE_CONTINUITY_QUALIFICATION_REF_IF_VERTICAL

  main_may_not:
    - DECLARE_EXTERNAL_CYCLE_CURRENT
    - RESTORE_REVOKED_VERTICAL_AUTHORITY
    - REVALIDATE_STALE_QIP
    - RESTORE_OLD_MAIN_RETURN_CURRENT_STANDING
```

如果 continuity 變化使舊 Main Return 失去 current Coverage standing：

```text
OLD MAIN RETURN
MAY REMAIN
HISTORICAL EVIDENCE.

IT DOES NOT SELF-RESTORE.
```

---

# M5.1-14｜Lost Primary / Pending Attempt Boundary

當 Protocol / Lighter 已將 Attempt 退回：

```text
ATTEMPT_PENDING_GOVERNING_CYCLE
```

Main：

```yaml
MAIN_PENDING_ATTEMPT_BEHAVIOR:

  new_main_transit:
    allowed: false

  final_gate_claim:
    allowed: false

  prior_main_returns:
    preserved_as_history: true
    current_coverage_standing: false

  may_resume_only_after:
    - LAWFUL_PRIMARY_STANDING_EXISTS
    - CURRENT_GOVERNANCE_ADMISSION_EXISTS
    - CURRENT_QIP_EXISTS
    - NEW_LAWFUL_MAIN_TRANSIT_REQUEST_EXISTS
```

Main 不得為了保持 compute continuity：

```text
假裝失效 Primary 仍 active。
```

---

# M5.1-15｜Radar Relation

保留：

```text
RADAR ADVISORY
!=
MAIN REENTRY TICKET.
```

Late Radar / other Lighter-owned advisory 只有在：

```text
LIGHTER LAWFUL REENTRY GOVERNANCE
+
NEW MAIN REENTRY REQUEST
```

成立時才使 Main 重進。

已 Released / lawfully Closed 的 Attempt 不得由 Main 自行回鑄。

---

# M5.1-16｜Human / External Semantic Owner Boundary

Current owner boundary 全部保留。

```yaml
MAIN_AUTHORITY_BOUNDARY_V5_1:

  human_owned_decisions:
    main_may:
      - PRESERVE
      - PROPAGATE
      - COMPETE_ONLY_OVER_REMAINING_UNRESOLVED_GENERATIVE_CHOICES
    main_may_not:
      - REOPEN_AS_IF_UNDECIDED
      - SELECT_DIFFERENT_HUMAN_WILL

  external_semantic_owners:
    main_may:
      - CONSUME_LAWFUL_RETURN
      - PRESERVE_UNRESOLVED_GAP
    main_may_not:
      - IMPERSONATE_OWNER
      - DECIDE_CHARACTER_WILL
      - DECIDE_WORLD_FACT
      - MINT_VERTICAL_CYCLE_IDENTITY
```

Hosting Main in a Vertical Cycle：

```text
DOES NOT TRANSFER
VERTICAL SEMANTIC OWNERSHIP
TO MAIN.
```

---

# M5.1-17｜Main Does Not Absorb Lighter Control Plane

Main 不吸收：

```text
GLOBAL SELF-STANDING GATE
LLIA / LLIA-GATE
PREMISE STANDING
AUTHORITY STANDING
ATTENTION-EFFECT QUALIFICATION
EXTERNAL-CONSTRAINT QUALIFICATION
COMPETITION INTEGRITY ADJUDICATION
CAPABILITY ELIGIBILITY
PROVIDER / TOOL / TRANSPORT
EVIDENCE ADMISSION
RECOVERY AUTHORIZATION
REAUTHORIZATION
CYCLE CONTINUITY GOVERNANCE
ATTEMPT TERMINATION GOVERNANCE
FINAL GATE
FINAL RELEASE
VERSION ELECTION
```

尤其：

```text
MAIN COMPUTE DEPENDENCY STATE
!=
LIGHTER DIRTY / STALE / REENTRY JUDGMENT.
```

---

# M5.1-18｜Coding Boundary

```yaml
MAIN_V5_1_CODING_BOUNDARY:

  code_may:
    - VALIDATE_MAIN_REQUEST_SHAPE
    - VALIDATE_GOVERNING_CYCLE_BINDING_FIELDS
    - VALIDATE_REQUEST_HASH
    - VALIDATE_PREBOUND_AUTHORITY_RECORD_SCHEMA_AND_EXACT_REF_EQUALITY
    - VALIDATE_AUTHORITY_BINDING_MAIN_INVOCATION_REF_MATCH
    - VALIDATE_CONTINUITY_QUALIFICATION_REF_BINDING_ONLY
    - VALIDATE_INPUT_SNAPSHOT_EQUALS_REQUEST_TARGET_SNAPSHOT
    - VALIDATE_RAW_MAIN_RETURN_BINDING
    - SERIALIZE_MAIN_RETURN_EMISSION_EVIDENCE
    - SERIALIZE_CANONICAL_MAIN_OUTPUT_REF
    - VALIDATE_STAGE_RECEIPT_AGAINST_EXISTING_TRIGGER_OR_OBLIGATION_RECORD
    - DISPATCH_MAIN_REQUEST
    - TRANSPORT_STAGE_RETURN
    - TRANSPORT_QUALIFIED_GAP_REF
    - RECORD_EXISTING_STAGE_RECEIPT_REF
    - SERIALIZE_ACTUAL_STATE_RETURN
    - SERIALIZE_COMPUTE_DEPENDENCY_STATE
    - VALIDATE_STAGE_ENUM

  code_may_not:
    - SELF_AUTHORIZE_MAIN_ENTRY
    - SELF_AUTHORIZE_MAIN_REENTRY
    - ACCEPT_GENERIC_AUTHORITY_REF_AS_EXACT_CALL_AUTHORITY
    - REUSE_PREBOUND_AUTHORITY_FOR_DIFFERENT_MAIN_INVOCATION_REF
    - ACCEPT_VERTICAL_REQUEST_WITHOUT_CURRENT_CONTINUITY_QUALIFICATION
    - ACCEPT_RETURN_WITH_INPUT_SNAPSHOT_DIFFERENT_FROM_REQUEST_TARGET
    - MINT_RECEIPT_FOR_UNTRIGGERED_CONDITIONAL_STAGE
    - MINT_MAIN_RETURN_EMISSION_EVIDENCE_WITHOUT_RAW_RETURN_BINDING
    - MINT_LIGHTER_QUALIFIED_CONSUMPTION_RECEIPT
    - IMPLEMENT_R1_SCORING_AS_EXTERNAL_HEURISTIC
    - CHOOSE_SEMANTIC_PATH_WINNER
    - CHOOSE_O9_DECISION
    - TRIGGER_I9_FROM_MISSING_RECEIPT
    - CHOOSE_R2_WINNER
    - CREATE_STAGE_STATE_WITHOUT_OWNER_OR_GAP_BASIS
    - TURN_MISSING_RECEIPT_INTO_FAILED_STAGE
    - CREATE_PARTIAL_MAIN_RETURN_IF_MAIN_NEVER_RAN
    - UPGRADE_PARTIAL_ORDER_TO_UNIQUE_WINNER
    - DECLARE_COVERAGE_CLOSED
    - DECLARE_REENTRY_NOT_REQUIRED
    - SELF_FINAL_RELEASE
    - SELF_ELECT_PROTOCOL_LIGHTER_MAIN_PEERS
    - QUALIFY_CALLER_AUTHORITY
    - DECIDE_CONTINUITY_CURRENT
    - DECIDE_STAGE_TRIGGER_OR_APPLICABILITY
    - DECIDE_MATERIALITY_DIRTY_STALE_OR_REENTRY
    - TREAT_HASH_EQUALITY_AS_SEMANTIC_QUALIFICATION
    - COLLAPSE_PARTIAL_INCOMPARABLE_OR_GAP_TO_WINNER_OR_FAILURE
```

```text
PYTHON / HOST WIRING
MAY CONNECT MAIN.

PYTHON / HOST WIRING
MAY NOT BE MAIN.
```

---


Coding interpretation lock：

```text
MAIN CODE
MAY VALIDATE
THAT A QUALIFIED RECORD IS WELL-FORMED
AND BOUND TO THE CORRECT REFS.

MAIN CODE
MAY NOT
QUALIFY THE RECORD.
```

特別是：

```text
TRIGGER RECORD PRESENT
→ code may verify receipt consistency.

code
→ may not decide whether the semantic trigger should have fired.
```

```text
CONTINUITY QUALIFICATION REF PRESENT
→ code may verify exact binding.

code
→ may not decide continuity standing.
```

```text
HASH MATCH
→ provenance integrity evidence.

HASH MATCH
!=
semantic truth / authority / coverage standing.
```

# M5.1-19｜Final Gate Boundary

Main produces only its scoped work：

```text
MAIN ACTUAL-STATE RETURN
+
MAIN RETURN EMISSION EVIDENCE IF RETURN EXISTS
+
CANONICAL MAIN_OUTPUT_REF
+
COMPUTE DEPENDENCY STATE
+
LAWFUL STAGE RECEIPTS / GAP STATES.
```

Main does not produce：

```text
FINAL GATE DECISION
FINAL RELEASE RECEIPT
VISIBLE RECEIPT INDEX AUTHORITY
COVERAGE CLOSURE AUTHORITY
CURRENT VERSION AUTHORITY
```

---

# M5.1-20｜Version Resolution / Standing

```text
MAIN CONSUMES
THE QUALIFIED EXACT VERSION TUPLE
RESOLVED BY
LIHUO_STACK_CURRENT_INDEX.

MAIN MAY NOT
SELF-ELECT
PROTOCOL / LIGHTER / MAIN PEERS.
```

本 draft 不自授 standing。

```yaml
STANDING_MODEL:
  artifact_class: FINAL_RATIFICATION_TARGET
  standing_source: NONE_UNTIL_EXTERNAL_RATIFICATION
  self_ratification: FORBIDDEN
  host_deployed: false
```

---

# M5.1-21｜Inherited Root Supersession

以下 V5.0.x / inherited cycle-bound wording 明確 supersede：

```text
V5.0.x:
EVERY ESTABLISHED LIHUO CYCLE
HAS A MAIN TRANSIT OBLIGATION.

→

V5.1.0:
EVERY ESTABLISHED LIHUO-GOVERNED
GENERATIVE PRIMARY GOVERNING CYCLE
HAS A MAIN COVERAGE OBLIGATION.

COVERAGE REQUIRES
AT LEAST ONE LAWFUL MAIN TRANSIT.
```

以及：

```text
V5.0.x:
MAIN RETURN / STAGE RECEIPT
REQUIRES cycle_id.

→

V5.1.0:
MAIN RETURN / STAGE RECEIPT
REQUIRES
governing_cycle_ref
+
governing_cycle_class
+
generation_attempt_ref
+
main_invocation_ref.
```

以及：

```text
Inherited:
EVERY LIHUO CYCLE
→ QIP
→ MAIN CYCLE.

→

V5.1.0:
EVERY ESTABLISHED
LIHUO-GOVERNED GENERATIVE PRIMARY CYCLE
→ CURRENT QIP
→ AT LEAST ONE LAWFUL MAIN TRANSIT.

MAIN INVOCATION
DOES NOT CREATE
A SECOND PRIMARY CYCLE.
```


以及：

```text
V5.0.x / early V5.1 draft:
MAIN RETURN RECEIPT
MAY APPEAR TO INCLUDE
LIGHTER QUALIFIED CONSUMPTION.

→

V5.1.0 FINAL TARGET:
MAIN PRODUCES
MAIN_RETURN_EMISSION_EVIDENCE.

LIGHTER PRODUCES
MAIN_RETURN_ADMISSION_RECEIPT
AFTER QUALIFIED CONSUMPTION.
```

其餘不衝突之 Main compute semantics：

```text
RETAINED.
```

---

# M5.1-22｜Regression Gate

```yaml
MAIN_V5_1_RC1_REGRESSION_GATE:

  input:
    - RAW_INPUT_DIRECT_BLOCK
    - QIP_V5_0_1_FIELDS_RETAINED
    - GOVERNING_CYCLE_BINDINGS_REQUIRED
    - STALE_QIP_BLOCK

  primary_class:
    - NATIVE_PRIMARY_MAIN_TRANSIT_PASS
    - VERTICAL_PRIMARY_MAIN_TRANSIT_PASS
    - MAIN_DOES_NOT_MINT_SECOND_PRIMARY

  transit:
    - R1_REQUIRED
    - O9_REQUIRED
    - I9_CONDITIONAL_BY_O9
    - I9_NOT_TRIGGERED_NO_I9_RECEIPT
    - CONDITIONAL_STAGE_RECEIPT_REQUIRES_LAWFUL_TRIGGER
    - R2_REQUIRED_WHEN_REACHABLE
    - ZERO_MAIN_CANNOT_SUPPORT_COVERAGE

  provenance:
    - EXACT_PREBOUND_CALLER_AUTHORITY_MATCH
    - AUTHORITY_BINDING_MAIN_INVOCATION_REF_MATCH
    - PREBOUND_AUTHORITY_REPLAY_TO_DIFFERENT_INVOCATION_BLOCK
    - CALLER_AUTHORITY_CONTEXT_MISMATCH_BLOCK
    - CALL_AUTHORITY_NEQ_GOVERNANCE_AUTHORITY
    - EXACT_REQUEST_HASH_MATCH
    - REQUEST_HASH_REUSE_AFTER_MUTATION_BLOCK
    - RETURN_BOUND_TO_INVOCATION
    - RAW_MAIN_RETURN_BOUND_TO_RECEIPT
    - RECEIPT_WITHOUT_RAW_RETURN_BLOCK
    - FOREIGN_INVOCATION_RETURN_BLOCK
    - ACTUAL_STATE_TAMPER_BLOCK

  return:
    - COMPLETE_RETURN_PASS
    - PARTIAL_RETURN_PASS
    - FAILED_STATE_RETURN_PASS
    - MAIN_NEVER_REACHED_NO_RETURN
    - PER_INVOCATION_INPUT_SNAPSHOT_MATCH
    - REENTRY_INPUT_SNAPSHOT_DIFFERS_FROM_CYCLE_OPENING_ALLOWED
    - RETURN_INPUT_SNAPSHOT_MISMATCH_BLOCK
    - RETURN_CANNOT_CLAIM_COVERAGE_CLOSED

  reentry:
    - SAME_PRIMARY_NEW_INVOCATION_PASS
    - REENTRY_REQUIRES_LIGHTER_GOVERNANCE
    - REENTRY_REQUIRES_CURRENT_QIP
    - VERTICAL_REENTRY_REQUIRES_CURRENT_CONTINUITY_QUALIFICATION
    - REENTRY_REQUIRES_EXACT_PREBOUND_INVOCATION_AUTHORITY
    - STALE_OLD_MAIN_RETURN_HISTORICAL_ONLY
    - MAIN_SELF_REENTRY_BLOCK
    - MAIN_SELF_NON_REENTRY_BASIS_BLOCK

  continuity:
    - VERTICAL_INITIAL_TRANSIT_REQUIRES_CURRENT_CONTINUITY_QUALIFICATION
    - REVOKED_PRIMARY_NO_NEW_MAIN_TRANSIT
    - PENDING_ATTEMPT_NO_MAIN_TRANSIT
    - RESTORED_PRIMARY_REQUIRES_CURRENT_ADMISSION_QIP_REQUEST

  owner_boundary:
    - MAIN_CANNOT_IMPERSONATE_VERTICAL_OWNER
    - MAIN_CANNOT_CLOSE_COVERAGE
    - MAIN_CANNOT_FINAL_RELEASE
    - MAIN_CANNOT_SELF_ELECT_VERSION
```

---

# 23｜RC2.1 最短口訣

```text
MAIN IS SHARED COMPUTE.

MAIN IS NOT
THE GOVERNING CYCLE OWNER.

MAIN IS NOT
THE GOVERNANCE ADMISSION OWNER.

ONE PRIMARY CYCLE
MAY CONTAIN
MORE THAN ONE MAIN INVOCATION.

EVERY LAWFUL MAIN TRANSIT:
R1 → O9 → [I9 IF TRIGGERED] → R2.

MAIN RETURNS
WHAT IT ACTUALLY COMPUTED.

MAIN STATES
WHAT ITS COMPUTE DEPENDS ON.

MAIN DOES NOT DECIDE
WHETHER COVERAGE IS CLOSED.

MAIN DOES NOT DECIDE
WHETHER REENTRY IS UNNECESSARY.

OLD MAIN RETURNS
MAY REMAIN HISTORY
WITHOUT REMAINING CURRENT.

MAIN SOLVES.
LIGHTER GOVERNS.
LIGHTER RELEASES.
```

---

# 24｜Final Ratification Target Boundary

```yaml
MAIN_V5_1_0_FINAL_TARGET:

  surgery_cut_3: CLEARED
  cross_stack_integration: APPLIED

  algorithm_change:
    R1_O9_I9_R2: NONE

  may_be_ratified_only_with:
    - EXACT_PROTOCOL_V5_1_0_CANDIDATE
    - EXACT_LIGHTER_V5_1_0_CANDIDATE
    - EXTERNAL_STACK_CANDIDATE_MANIFEST
    - HUMAN_ATOMIC_ASSENT

  ratification_does_not_mean:
    - HOST_DEPLOYED
    - OWNER_RUNTIME_AVAILABLE
    - ACTUAL_MAIN_INVOCATION_OCCURRED
    - EXISTING_VERTICAL_AUTO_REBOUND
```

**END OF LIHUO MAIN V5.1.0 OPERATIVE SUCCESSOR LAYER**


---

# PART B｜BYTE-FOR-BYTE INHERITED LIHUO MAIN V5.0.1 FULL BODY

```text
PRECEDENCE:
V5.1.0 OPERATIVE SUCCESSOR LAYER
> CONFLICTING V5.0.1 LANGUAGE.

ALL NON-CONFLICTING V5.0.1 COMPUTE SEMANTICS
REMAIN INCORPORATED.
```

# 理火 AI 主系統｜LIHUO MAIN V5.0.1｜SELF-CONTAINED FULL BODY EDITION
## Artifact-Completeness Patch over ratified V5.0.0｜2026-10-13
### RATIFIED CURRENT｜Same-family V5.0.1 Full-Body Consolidation Patch

```yaml
DOCUMENT_IDENTITY:
  version: V5.0.1
  artifact_class: FULL_BODY_CONSOLIDATION_PATCH_RATIFIED_CURRENT
  semantic_change_from_v5_0_0: false
  authority_change: false
  mandatory_topology_change: false
  material_receipt_constitution_change: false
  root_protocol_change: false
  standing: RATIFIED_CURRENT
  standing_source: EXTERNAL_HUMAN_PATCH_RATIFICATION_EVENT
  ratification_event_ref: LIHUO_STACK_V5_0_1_FULL_BODY_PATCH_RATIFICATION_EVENT_20261014
  ratified_at: "2026-10-14T01:50:00+08:00"
  current_role: ACTIVE_STACK_COMPONENT
  host_deployed: false

PATCH_PURPOSE:
  - RESTORE_STANDALONE_ARTIFACT_COMPLETENESS
  - PHYSICALLY_CARRY_INHERITED_BODY
  - PRESERVE_V5_0_0_OPERATIVE_SEMANTICS
  - DO_NOT_REWRITE_HISTORY

CURRENT_PARENT_STACK:
  prior_current: LIHUO_MAIN_V5.0.0
  prior_current_sha256: "7cef67692d156dbdab12a7f7ac61136806837e23a65ec4017b78686a8bc832d8"
  normative_parent_v4_4_1_sha256: "d5f3a29f8a7f326b365f7d09b471a4d34aa5a1f0c01a0b3e8913939207b9d1ab"
  inherited_v4_4_body_source: EXTRACTED_FROM_ARCHIVAL_FULL_CARRIER 

SOURCE_HASHES:
  v5_0_0: "7cef67692d156dbdab12a7f7ac61136806837e23a65ec4017b78686a8bc832d8"
  main_v4_4_1_ratified_patch: "d5f3a29f8a7f326b365f7d09b471a4d34aa5a1f0c01a0b3e8913939207b9d1ab"
  archival_full_carrier_v4_4_body: "8aa85720cc304ff43d8b9d6bcf9569168be214e8202a4cdd55eae77240664724" 

READ_RULE:
  precedence:
    1: V5_0_1_CONSOLIDATION_WRAPPER
    2: RATIFIED_V5_0_0_OPERATIVE_LAYER
    3: DIRECT_NORMATIVE_PARENT_BODY
    4: EARLIER_INHERITED_BODY_PER_PARENT_SUPERSESSION_RULES
  historical_current_labels_inside_inherited_bodies: FORMATION_METADATA_ONLY
  inherited_body_conflict_rule: V5_0_0_AND_LATER_VALID_SUPERSESSION_CONTROLS
  single_file_loading_goal: true
```

> **本版只修載體完整性，不修改 V5.0.0 已批准治理語義。**
>
> **V5.0.0 的 exact bytes 與批准歷史保留；V5.0.1 已由外部人類批准事件通過，並由 successor Current Index 取得 Current standing。**
>
> **本檔中的舊 `CURRENT / RATIFIED` 字樣若位於 INHERITED BODY，只表示形成時歷史法位，不得反向覆蓋 V5.0.1 的現行讀法。**

> **Main 特別讀法：**
>
> 正式 V4.4.1 檔是對 V4.4 的 ratified control-flow patch，本身以 pointer 保留 V4.4。
> 本 V5.0.1 同時內嵌「正式 V4.4.1 patch」與其 archival full carrier 中的 V4.4 verbatim body，
> 使單檔不再依賴外部 V4.4 檔才能讀完整 Main。

---

# PART A｜RATIFIED V5.0.0 OPERATIVE LAYER｜INCORPORATED VERBATIM

<!-- BEGIN RATIFIED V5.0.0 MAIN OPERATIVE LAYER -->
# 理火 AI 主系統｜LIHUO MAIN V5.0.0
## FULL CONSOLIDATED BASELINE｜Lawful PATH Competition × Conditional I9 × Actual-State Return
### Final Ratification Target｜2026-10-13

```yaml
DOCUMENT_IDENTITY:
  id: LIHUO_MAIN
  version: V5.0.0
  artifact_class: FINAL_RATIFICATION_TARGET
  standing_source: EXTERNAL_ATOMIC_RATIFICATION_RECORD
  standing_at_build: INACTIVE_RATIFICATION_TARGET
  current_claim_in_bytes: NONE
  host_deployed: false

NORMATIVE_PARENT:
  version: LIHUO_MAIN_V4.4.1
  sha256: "d5f3a29f8a7f326b365f7d09b471a4d34aa5a1f0c01a0b3e8913939207b9d1ab"
  standing: RATIFIED_CURRENT_AT_BUILD
  treatment:
    - ALL_NON_CONFLICTING_PARENT_SEMANTICS_RETAINED
    - V5_EXPLICIT_SUPERSESSION_ONLY_WHERE_STATED

PROPOSED_CONTROL_PLANE:
  version: LIHUO_LIGHTER_V5.0.0
  activation: SAME_ATOMIC_STACK_EVENT_REQUIRED

DRAFT_LINEAGE_NON_NORMATIVE:
  - CLEAN_RC1
  - CLEAN_RC2
  - CLEAN_RC3
  - FIFTH_ATTACK_DUIDUI
```

# M5-0｜Main 根句

```text
EVERY ESTABLISHED LIHUO CYCLE
HAS A MAIN TRANSIT OBLIGATION.

R1 → O9 → [I9 IF O9 TRIGGERED] → R2.

MAIN SOLVES.
LIGHTER RELEASES.

MAIN RETURN EXISTS
WHEN MAIN EXECUTION WAS ACTUALLY REACHED
AND MAIN CAN RETURN ITS ACTUAL STATE.

MAIN RETURN EXISTS
!=
MAIN COMPLETED SUCCESSFULLY.
```

R3+ 與其他 Main event-driven modules 保留父版語義，只在 material trigger 成立時進場。

# M5-1｜PATH Competition Standing

Main 是 V5 lawful PATH competition 的主要 compute owner。

```yaml
MAIN_PATH_COMPETITION:

  required_for:
    LIHUO_GENERATIVE_OUTPUT_STANDING

  necessary_not_sufficient: true

  R1:
    purpose:
      - OPEN_LAWFUL_CANDIDATE_FIELD
      - QUALIFY_LIVE_PATHS
      - CREATE_PROVISIONAL_ORDER_OR_PARTIAL_ORDER
      - PRESERVE_RESIDUE

  R2:
    purpose:
      - GENUINE_RECOMPETITION
      - REEXAMINE_LIVE_QUALIFIED_ALTERNATIVES
      - CONSUME_LAWFUL_DIRTY_INPUTS
      - PRESERVE_PARTIAL_ORDER_WHEN_UNRESOLVED

  justified_single_survivor:
    allowed_when:
      - CANDIDATE_FIELD_WAS_GENUINELY_OPENED
      - OTHER_PATHS_WERE_LAWFULLY_EXCLUDED
    fake_competition_required: false

  main_may_not_compete_over:
    - HUMAN_OWNED_DECISION_ALREADY_MADE
    - CHARACTER_OWNER_DECISION_ALREADY_MADE
    - WORLD_OWNER_RESULT_ALREADY_QUALIFIED
    - HARD_SCOPE_BOUNDARY
    - QUALIFIED_FACT_AS_IF_UNRESOLVED

  main_may_not:
    - FORCE_UNIQUE_WINNER_WITHOUT_JUSTIFICATION
    - USE_COMPETITION_TO_SEIZE_OTHER_OWNER_AUTHORITY
```

# M5-2｜Radar Relation

```yaml
MAIN_RADAR_RELATION:

  radar_return:
    input_class: OPTIONAL_ADVISORY_INPUT

  R1_requires_radar_return: false
  R2_requires_radar_return: false

  may_consume:
    - ACTUALLY_AVAILABLE_QUALIFIED_RADAR_ADVISORY

  may_not:
    - WAIT_FOR_FULL_RADAR_RETURN_AS_ENTRY_PRECONDITION
    - TREAT_RADAR_ADVICE_AS_WINNER
    - TREAT_RADAR_MISSING_AS_NO_MATERIAL_ADVICE
```

# M5-3｜R1

```yaml
R1_EXECUTION:

  required_when_main_reached: true

  outputs:
    - R1_RESULT
    - QUALIFIED_CANDIDATE_FIELD
    - PROVISIONAL_ORDER_OR_PARTIAL_ORDER
    - RESIDUE_REFS
    - R1_EXECUTION_RECEIPT_OR_FAILURE_EVIDENCE
```

R1 receipt 無 closure standing。

# M5-4｜O9 Owns I9 Activation Decision

```yaml
O9_EXECUTION:

  required_when_reachable: true

  i9_activation_decision:
    - I9_TRIGGERED
    - I9_NOT_TRIGGERED
    - HOLD_NO_VALID_DECISION

  reason_ref:
    REQUIRED_WHEN_O9_EXECUTES

  hard_locks:
    - RECEIPT_ABSENCE_NEVER_SUBSTITUTES_FOR_O9_DECISION
    - O9_DOES_NOT_FINAL_RELEASE
```

# M5-5｜I9 Conditional

```text
O9 = I9_NOT_TRIGGERED
→ NO I9 STAGE
→ NO I9 RECEIPT.

O9 = I9_TRIGGERED
→ I9 STAGE MUST BE HANDLED
→ I9 STAGE RECEIPT REQUIRED
→ THEN R2.

O9 = HOLD_NO_VALID_DECISION
→ I9 BRANCH = UNKNOWN
→ R2 OBLIGATION REMAINS IF EXECUTIONALLY REACHABLE
→ FINAL GATE MUST SEE THE GAP.
```

I9 不自我觸發、不自我資格化、不選 winner。

# M5-6｜R2 Genuine Recompetition

```yaml
R2_EXECUTION:

  required_when_executionally_reachable: true

  consumes:
    - R1_FIELD
    - O9_DECISION
    - I9_DELTA_IF_TRIGGERED
    - QUALIFIED_ADVISORY_REFS_IF_AVAILABLE
    - OTHER_LAWFUL_DIRTY_INPUTS

  must:
    - REEXAMINE_LIVE_QUALIFIED_ALTERNATIVES
    - PRESERVE_PARTIAL_ORDER_WHEN_UNRESOLVED
    - NOT_FORCE_UNIQUE_WINNER_WHEN_NOT_JUSTIFIED

  outputs:
    - R2_RESULT_OR_FAILURE_STATE
    - FINAL_MAIN_CANDIDATE_FIELD_OR_PARTIAL_ORDER_IF_AVAILABLE
    - R2_EXECUTION_RECEIPT_OR_FAILURE_EVIDENCE
```

# M5-7｜Stage State Model

```yaml
MAIN_STAGE_STATE:

  R1:
    - EXECUTED
    - FAILED
    - GAP
    - NOT_REACHED

  O9:
    - EXECUTED
    - FAILED
    - GAP
    - NOT_REACHED

  I9:
    branch_state:
      - TRIGGERED
      - NOT_TRIGGERED
      - UNKNOWN
      - NOT_REACHED
    execution_state:
      - EXECUTED
      - FAILED
      - NOT_EXECUTED
      - NOT_REACHED

  R2:
    - EXECUTED
    - FAILED
    - GAP
    - NOT_REACHED
```

# M5-8｜Actual-State Main Return

```yaml
MAIN_CYCLE_RETURN_V5:

  applies_when:
    MAIN_EXECUTION_WAS_REACHED_ENOUGH_TO_RETURN_STATE

  return_ref: REQUIRED
  cycle_id: REQUIRED

  cycle_state:
    - COMPLETE
    - PARTIAL
    - FAILED

  stages:

    r1:
      state: REQUIRED
      receipt_ref: REF_OR_NONE
      gap_or_failure_ref: REF_OR_NONE

    o9:
      state: REQUIRED
      receipt_ref: REF_OR_NONE
      gap_or_failure_ref: REF_OR_NONE

    i9:
      branch_state: REQUIRED
      execution_state: REQUIRED
      receipt_ref: REF_OR_NONE
      gap_or_failure_ref: REF_OR_NONE

    r2:
      state: REQUIRED
      receipt_ref: REF_OR_NONE
      gap_or_failure_ref: REF_OR_NONE

  candidate_or_partial_order_ref:
    REF_OR_NONE

  unresolved_gap_refs:
    []

  may_not_claim:
    - FINAL_RELEASE
    - COMPLETE_IF_PARTIAL
    - STAGE_EXECUTION_WITHOUT_EVIDENCE
```

```text
MAIN RETURN EXISTS
!=
ALL STAGES SUCCEEDED.
```

# M5-9｜Cycle Return Receipt

```yaml
CYCLE_RETURN_RECEIPT_V5:

  required_when:
    MAIN_CYCLE_RETURN_ACTUALLY_EXISTS

  proves:
    MAIN_RETURN_WAS_EMITTED

  does_not_prove:
    - ALL_STAGES_SUCCEEDED
    - FINAL_RELEASE

  fields:
    - receipt_ref
    - cycle_id
    - main_return_ref
    - main_return_cycle_state
    - evidence_origin
```

```text
PARTIAL MAIN RETURN
MAY HAVE
CYCLE_RETURN_RECEIPT.

FAILED-STATE MAIN RETURN
MAY HAVE
CYCLE_RETURN_RECEIPT.

MAIN NEVER REACHED
→
NO MAIN RETURN
→
NO CYCLE_RETURN_RECEIPT.
```

# M5-10｜R2 under Upstream Failure

```text
R2 OBLIGATION REMAINS
WHEN R2 IS STILL EXECUTIONALLY REACHABLE.

IF R2 CANNOT BE REACHED,
MAIN RETURN MAY REPORT
R2 = NOT_REACHED
WITH QUALIFIED GAP / FAILURE BASIS.
```

# M5-11｜Late Radar

```text
RADAR ADVISORY
!=
MAIN REENTRY TICKET.
```

R2 後 late Radar 只有在 Lighter lawful reentry request 成立後，Main 才重進。

已 release / closed cycle 不得被 late Radar 回鑄。

# M5-12｜Human / Owner Authority Boundary

```yaml
MAIN_AUTHORITY_BOUNDARY:

  human_owned_decisions:
    main_may:
      - PRESERVE
      - PROPAGATE
      - COMPETE_ONLY_OVER_REMAINING_UNRESOLVED_GENERATIVE_CHOICES
    main_may_not:
      - REOPEN_AS_IF_UNDECIDED
      - SELECT_DIFFERENT_HUMAN_WILL

  external_semantic_owners:
    main_may:
      - CONSUME_LAWFUL_RETURN
      - PRESERVE_UNRESOLVED_GAP
    main_may_not:
      - IMPERSONATE_OWNER
      - DECIDE_CHARACTER_WILL
      - DECIDE_WORLD_FACT
```

# M5-13｜Coding Boundary

```yaml
MAIN_V5_CODING_BOUNDARY:

  code_may:
    - DISPATCH_MAIN_REQUEST
    - VALIDATE_INPUT_SHAPE
    - TRANSPORT_STAGE_RETURN
    - TRANSPORT_QUALIFIED_GAP_REF
    - RECORD_EXISTING_STAGE_RECEIPT_REF
    - SERIALIZE_ACTUAL_STATE_RETURN
    - VALIDATE_STAGE_ENUM

  code_may_not:
    - IMPLEMENT_R1_SCORING_AS_EXTERNAL_HEURISTIC
    - CHOOSE_SEMANTIC_PATH_WINNER
    - CHOOSE_O9_DECISION
    - TRIGGER_I9_FROM_MISSING_RECEIPT
    - CHOOSE_R2_WINNER
    - CREATE_STAGE_STATE_WITHOUT_OWNER_OR_GAP_BASIS
    - TURN_MISSING_RECEIPT_INTO_FAILED_STAGE
    - CREATE_PARTIAL_MAIN_RETURN_IF_MAIN_NEVER_RAN
    - UPGRADE_PARTIAL_ORDER_TO_UNIQUE_WINNER
    - SELF_FINAL_RELEASE
```

```text
PYTHON / HOST WIRING
MAY CONNECT MAIN.

PYTHON / HOST WIRING
MAY NOT BE MAIN.
```

# M5-14｜Final Gate Boundary

Main produces only its scoped work:

```text
MAIN ACTUAL-STATE RETURN
+
CYCLE_RETURN_RECEIPT IF RETURN EXISTS.
```

Main does not produce:

```text
FINAL RELEASE DECISION
FINAL RELEASE RECEIPT
VISIBLE RECEIPT INDEX AUTHORITY
CURRENT VERSION AUTHORITY
```

# M5-15｜Version Resolution / Standing

Main consumes the exact version tuple resolved by `LIHUO_STACK_CURRENT_INDEX`.

Main may not self-elect latest V5.0.x.

```yaml
STANDING_MODEL:
  artifact_class: FINAL_RATIFICATION_TARGET
  standing_source: EXTERNAL_ATOMIC_RATIFICATION_RECORD
  self_ratification: FORBIDDEN
```

**END OF LIHUO MAIN V5.0.0 FULL CONSOLIDATED RATIFICATION TARGET**

<!-- END RATIFIED V5.0.0 MAIN OPERATIVE LAYER -->

---

# PART B｜DIRECT RATIFIED PARENT PATCH｜MAIN V4.4.1

<!-- BEGIN INHERITED MAIN V4.4.1 RATIFIED PATCH -->
# 理火 AI 主系統｜LIHUO MAIN V4.4.1
## LIGHTER V4.12.2 Cycle Control-Flow × Receipt Alignment Patch
### O9 決定 I9 啟動｜I9 條件收據｜理火週期拓撲勘誤｜小版本正式批准｜2026-10-12

> **法位：** `DOCUMENT_LEVEL_RATIFIED_SUCCESSOR / CURRENT_LIHUO_MAIN / COMPUTE_ENGINE_SPEC / NOT_HOST_DEPLOYED`。
>
> 本版是 MAIN V4.4 的**小版本控制流／收據語義勘誤**，直接對齊 CURRENT LIGHTER V4.12.2。
>
> 本版不修改 R-CCC 競爭算法、不修改七個 field modules、不修改 I9 調燈能力本身、不修改 R1／R2 固定義務、不建立 Host E6/E7。
>
> 本版只修正一個在 V4.4 × LIGHTER V4.8 receipt constitution 時形成的錯位：**I9 原本是由 O9 條件啟動的模組，卻被寫成每個 established cycle 都必須先跑 I9 Assessment 的固定 stage。**
>
> 現行拓撲恢復為：
>
> **`R1 → O9 → [I9 if triggered] → R2`**
>
> 並正式鎖定：
>
> **O9 啟動 I9 → I9 Receipt 必備。**
>
> **O9 未啟動 I9 → I9 Receipt 不得出現。**

```yaml
DOCUMENT:
  id: LIHUO_MAIN
  version: V4.4.1
  date: 2026-10-12

  standing:
    - DOCUMENT_LEVEL_RATIFIED_SUCCESSOR
    - CURRENT_LIHUO_MAIN
    - COMPUTE_ENGINE_SPEC
    - NOT_HOST_DEPLOYED

  parent:
    version: LIHUO_MAIN_V4.4
    file: 01_MAIN_V4.4_PROTOCOL_V3.0.1_LIGHTER_V4.8_RECEIPT_I9_FULL_RATIFIED_20261006.md
    sha256: "4d5f69321c27b4868eb71657871b96e7fccb801087149a2e6d1d13e61b082c34"
    treatment: CANONICAL_PARENT_RETAINED_BY_REFERENCE

  constitutional_root:
    protocol: LIHUO_PROTOCOL_V3.0.1
    pointer_status: LEGACY_BOUND_UNTIL_SEPARATE_REBIND
    changed_by_this_revision: false

  control_plane:
    lighter: LIHUO_LIGHTER_V4.12.2
    lighter_sha256: "6d6734c7f111e5fc4bef0cb02c680051c3394021693a45fb74ca63be4098dce8"
    alignment: CYCLE_CONTROL_FLOW_AND_RECEIPT_MATCH

  revision:
    id: MAIN_I9_CONTROL_FLOW_RECEIPT_ALIGNMENT_V0_1
    type: SMALL_RUNTIME_CONTROL_AND_RECEIPT_SEMANTIC_CORRECTION
    fixes:
      - REMOVE_PER_CYCLE_MANDATORY_I9_ASSESSMENT_STAGE
      - RESTORE_O9_OWNED_I9_ACTIVATION_DECISION
      - MAKE_I9_STAGE_CONDITIONAL_BY_O9
      - MAKE_I9_RECEIPT_REQUIRED_IF_TRIGGERED
      - PROHIBIT_I9_RECEIPT_IF_NOT_TRIGGERED
      - ALIGN_R2_RECEIPT_WITH_ACTUAL_CONTROL_FLOW
      - ALIGN_MAIN_RETURN_WITH_LIGHTER_V4_12_2
      - ALIGN_REGRESSION_INVARIANTS
    preserves:
      - R1_REQUIRED
      - O9_REQUIRED
      - R2_REQUIRED
      - R3_PLUS_EVENT_DRIVEN
      - I9_QUALIFICATION_BOUNDARY_AFTER_TRIGGER
      - I9_NO_SELF_QUALIFICATION
      - I9_NO_WINNER_SELECTION
      - NO_POST_HOC_RECEIPT_MINTING
      - MAIN_DOES_NOT_FINAL_RELEASE
    changes_protocol_text: false
    changes_rccc_algorithm: false
    changes_i9_adjustment_capability: false

  host_binding: NOT_ESTABLISHED
  e6_e7: NOT_ESTABLISHED
```

---

# V4.4.1-0｜這次修的是週期拓撲，不是增加新的 I9 階段

MAIN V4.4 的現行父版曾寫成：

```text
R1
→ O9
→ I9 ASSESSMENT
→ [QUALIFIED I9]
→ R2
```

並要求：

```text
I9 ASSESSMENT = MANDATORY PER CYCLE
```

這會造成：

```text
O9 沒有啟動 I9
↓
I9 本來不應進場
↓
卻因 schema 要求 I9 Assessment Receipt
↓
沒有 I9 receipt 被讀成 missing receipt
↓
合法週期被誤判 incomplete / HOLD
```

本版撤銷這個 Current 語義。

現行唯一拓撲：

```text
R1
→ O9
   ├─ I9_NOT_TRIGGERED
   │  → R2
   │
   └─ I9_TRIGGERED
      → I9
      → R2
```

---

# V4.4.1-1｜固定模組與條件模組

```text
R1 = REQUIRED
O9 = REQUIRED
I9 = CONDITIONAL_BY_O9
R2 = REQUIRED
R3+ = EVENT_DRIVEN
```

因此：

```text
I9 NOT TRIGGERED
!=
I9 FAILED

I9 NOT TRIGGERED
!=
I9 NOT QUALIFIED

I9 NOT TRIGGERED
!=
MISSING I9 RECEIPT
```

`NOT_TRIGGERED` 是一條正常合法控制分支。

---

# V4.4.1-2｜O9 現行責任：觀察 + I9 Activation Decision

O9 每個已成立 cycle 仍然必跑，仍須觀察 R1 並留下 O9 receipt。

現行 O9 receipt 增補 I9 activation decision：

```yaml
O9_EXECUTION_RECEIPT:
  o9_receipt_ref: REQUIRED
  r1_receipt_ref: REQUIRED
  source_snapshot_ref: REQUIRED
  lamp_state_r1_ref: REQUIRED_OR_LAMP_REQUIRED_MISSING

  observation_status:
    - OBSERVED
    - LAMP_REQUIRED_MISSING
    - EVIDENCE_GAP

  i9_activation_decision:
    decision:
      - I9_TRIGGERED
      - I9_NOT_TRIGGERED
      - HOLD_NO_VALID_DECISION
    reason_ref: REQUIRED

  evidence_origin: REQUIRED
```

判定：

```text
O9 = I9_NOT_TRIGGERED
→ I9 DOES NOT ENTER THIS CYCLE

O9 = I9_TRIGGERED
→ I9 ENTERS THIS CYCLE

O9 = HOLD_NO_VALID_DECISION
→ DO NOT INFER NOT_TRIGGERED
→ PRESERVE GAP / HOLD
```

O9 缺失仍不得免除 R2。

---

# V4.4.1-3｜I9 現行生命週期：只有被 O9 啟動後才開始

本版取消：

```text
EVERY ESTABLISHED CYCLE
→ I9 ASSESSMENT MUST OCCUR
```

改為：

```text
O9 = I9_TRIGGERED
→ I9 STAGE MUST OCCUR

O9 = I9_NOT_TRIGGERED
→ I9 STAGE MUST NOT OCCUR
```

I9 被 O9 啟動後，既有 qualification、scope、evidence、hard-boundary 規則全部保留。

I9 不得：

```text
self-invent trigger
self-qualify
self-expand scope
create standing
create PATH
create world fact
override independently verified external hard boundary
select winner
perform Final Release
```

---

# V4.4.1-4｜I9 Receipt｜條件必備

I9 Receipt 不是 optional。

它是**條件必備**：

```text
O9 = I9_TRIGGERED
→ I9 RECEIPT REQUIRED

O9 = I9_NOT_TRIGGERED
→ I9 RECEIPT MUST NOT EXIST
```

現行 I9 stage receipt：

```yaml
I9_RECEIPT:
  i9_receipt_ref: REQUIRED_IF_O9_TRIGGERED
  cycle_id: REQUIRED
  o9_receipt_ref: REQUIRED
  trigger_state: I9_TRIGGERED

  qualification_result:
    - QUALIFIED
    - NOT_QUALIFIED
    - EVIDENCE_GAP
    - LAMP_REQUIRED_MISSING

  qualification_contract_ref: REF_OR_NULL_WITH_REASON
  evidence_refs: []

  execution_state:
    - EXECUTED
    - NOT_EXECUTED
    - FAILED

  execution_ref: REF_OR_NULL_WITH_REASON
  field_delta_ref: REF_IF_ACTUALLY_APPLIED
```

因此：

```text
I9 TRIGGERED
!=
I9 MUST EXECUTE
```

但：

```text
I9 TRIGGERED
=
I9 RECEIPT MUST EXIST
```

合法例：

```text
O9 = I9_TRIGGERED
+
I9 qualification = NOT_QUALIFIED
+
I9 execution = NOT_EXECUTED
+
I9 receipt exists
→ LEGAL I9 STAGE COMPLETION
→ PROCEED TO R2
```

非法例：

```text
O9 = I9_NOT_TRIGGERED
+
I9 receipt exists
→ CONTROL_FLOW_RECEIPT_MISMATCH
→ HOLD
```

---

# V4.4.1-5｜R2 Receipt 對齊實際控制流

R2 固定義務不變。

現行 R2 receipt：

```yaml
R2_EXECUTION_RECEIPT:
  r2_receipt_ref: REQUIRED
  r1_receipt_ref: REQUIRED
  o9_receipt_ref: REQUIRED_OR_GAP_REF

  i9_activation_state:
    source: O9_RECEIPT
    value:
      - I9_TRIGGERED
      - I9_NOT_TRIGGERED
      - HOLD_NO_VALID_DECISION

  i9_receipt_ref:
    required_if: I9_TRIGGERED
    prohibited_if: I9_NOT_TRIGGERED
    hold_if: HOLD_NO_VALID_DECISION

  first_pass_integrity_reset_ref: REQUIRED
  challenger_recovery_ref: REQUIRED
  suppressed_path_restoration_ref: REQUIRED
  residue_objection_injection_ref: REQUIRED
  recompetition_snapshot_ref: REQUIRED
  structural_result_ref: REQUIRED
  qualified_path_set_ref: REQUIRED
  path_output_order_ref: REQUIRED_OR_UNRESOLVED
  competition_termination_ref: REQUIRED_OR_R3PLUS_REQUIRED

  execution_status:
    - EXECUTED
    - HOLD
    - FAILED
```

禁止：

```text
R2 sees empty I9 field
→ infer missing receipt
```

必須先讀：

```text
O9 I9-ACTIVATION DECISION
```

---

# V4.4.1-6｜Main Cycle Return 對齊 LIGHTER V4.12.2

現行 Main Return：

```yaml
MAIN_CYCLE_RETURN_V4_4_1:
  cycle_id: REQUIRED
  ticket_ref: REQUIRED
  manifest_ref: REQUIRED
  scope_ref: REQUIRED
  opening_snapshot_ref: REQUIRED
  final_snapshot_ref: REQUIRED_OR_HOLD

  r1_receipt_ref: REQUIRED
  o9_receipt_ref: REQUIRED

  i9_activation_state:
    source: O9_RECEIPT
    value:
      - I9_TRIGGERED
      - I9_NOT_TRIGGERED
      - HOLD_NO_VALID_DECISION

  i9_receipt_ref:
    required_if: I9_TRIGGERED
    prohibited_if: I9_NOT_TRIGGERED
    hold_if: HOLD_NO_VALID_DECISION

  r2_receipt_ref: REQUIRED
  r3_plus_receipt_refs: IF_TRIGGERED

  executed_module_refs: []
  accepted_delta_refs: []
  failed_module_receipt_refs: []
  unresolved_evidence_gap_refs: []

  qualified_path_set_ref: REQUIRED_OR_HOLD
  path_output_order_ref: REQUIRED_OR_UNRESOLVED
  competition_termination_ref: REQUIRED_OR_HOLD
  premise_discrimination_gap_ref: OPTIONAL
  closure_qualification_ref: OPTIONAL
  manifestation_qualification_ref: OPTIONAL

  cycle_receipt_ledger_ref: REQUIRED

  candidate_state:
    - CANDIDATE_OUTPUT
    - STRUCTURAL_HOLD
    - STATE_SYNC_ONLY
    - NON_MANIFESTATION
    - DEPENDENCY_UNAVAILABLE
    - CAPABILITY_REQUEST
```

`STATE_SYNC_ONLY` 現行條件：

```text
R1 completed
+
O9 completed with valid I9 activation decision
+
I9 completed IF AND ONLY IF triggered
+
R2 completed
```

而不是固定要求 I9 Assessment。

---

# V4.4.1-7｜Cycle Receipt Legal Completion｜Main 端判準

MAIN 與 LIGHTER V4.12.2 採同一根定義：

> **週期完整，不要求所有可能模組都有收據。合法完成要求收據集合與本輪實際合法控制流一致。**

```text
REQUIRED MODULE
→ RECEIPT REQUIRED

CONDITIONAL MODULE TRIGGERED
→ RECEIPT REQUIRED

CONDITIONAL MODULE NOT TRIGGERED
→ RECEIPT MUST NOT EXIST
```

所以：

```text
O9 = I9_TRIGGERED
+
I9 RECEIPT MISSING
→ CYCLE INCOMPLETE / HOLD
```

```text
O9 = I9_NOT_TRIGGERED
+
NO I9 RECEIPT
→ LEGAL COMPLETE BRANCH
```

```text
O9 = I9_NOT_TRIGGERED
+
I9 RECEIPT EXISTS
→ CONTROL_FLOW_RECEIPT_MISMATCH / HOLD
```

最短式：

```text
CYCLE COMPLETENESS
!=
ALL POSSIBLE MODULE RECEIPTS PRESENT

CYCLE COMPLETENESS
=
RECEIPTS MATCH THE ACTUAL LAWFUL CONTROL FLOW
```

---

# V4.4.1-8｜Failure / Recovery 同步勘誤

父版根句保留：

```text
FAILURE MUST LEAVE A FAILURE RECEIPT.
```

但現行解釋必須先滿足：

```text
MODULE WAS ACTUALLY TRIGGERED / REQUIRED
```

因此：

```text
TRIGGERED MODULE FAILED
→ FAILURE RECEIPT REQUIRED
```

而不是：

```text
UNTRIGGERED MODULE
→ CREATE "NOT FAILED" RECEIPT
```

沒有被啟動的 I9 不產生 success receipt、failure receipt、assessment receipt 或 nonexecution receipt。

它只由 O9 receipt 的 `I9_NOT_TRIGGERED` 決定證明未進場。

---

# V4.4.1-9｜Supersession Map｜撤銷父版錯誤 I9 週期語義

MAIN V4.4 原文件與歷史形成位置不回溯修改。

但下列父版語義自 V4.4.1 起不再是 Current operative reading：

```text
I9_ASSESSMENT_MANDATORY_PER_CYCLE

R1 → O9 → I9 ASSESSMENT → [QUALIFIED I9] → R2

EVERY CYCLE HAS I9 ASSESSMENT RECEIPT

R2 i9_assessment_ref = REQUIRED

MAIN_CYCLE_RETURN i9_assessment_receipt_ref = REQUIRED

STATE_SYNC_ONLY REQUIRES I9 ASSESSMENT IN EVERY CYCLE
```

替代為：

```text
R1 → O9 → [I9 IF TRIGGERED] → R2

O9 OWNS I9 ACTIVATION DECISION

I9 TRIGGERED
→ I9 RECEIPT REQUIRED

I9 NOT TRIGGERED
→ I9 RECEIPT PROHIBITED
```

父版以下內容全部保留：

```text
R1 mandatory
O9 mandatory
R2 mandatory genuine recompetition
R3+ event-driven
I9 no self-qualification
I9 no winner selection
I9 bounded adjustment only
Main creates evidence; Lighter admits evidence
No post-hoc receipt minting
Local failure → local damage
Main does not Final Release
```

---

# V4.4.1-10｜Regression Tests

```yaml
MAIN_V4_4_1_REGRESSION:

  MCFR_01_NOT_TRIGGERED_NO_I9_RECEIPT:
    input:
      - R1_RECEIPT_PRESENT
      - O9_RECEIPT_PRESENT
      - O9_I9_ACTIVATION = I9_NOT_TRIGGERED
      - I9_RECEIPT_ABSENT
      - R2_RECEIPT_PRESENT
    expected:
      - LEGAL
      - NO_MISSING_I9_RECEIPT
      - CYCLE_MAY_COMPLETE_IF_OTHER_REQUIREMENTS_PASS

  MCFR_02_TRIGGERED_I9_RECEIPT_PRESENT:
    input:
      - O9_I9_ACTIVATION = I9_TRIGGERED
      - I9_RECEIPT_PRESENT
    expected:
      - LEGAL_I9_STAGE_PRESENT
      - CONTINUE_TO_R2_IF_STAGE_RESULT_PERMITS

  MCFR_03_TRIGGERED_I9_RECEIPT_MISSING:
    input:
      - O9_I9_ACTIVATION = I9_TRIGGERED
      - I9_RECEIPT_ABSENT
    expected:
      - HOLD
      - MISSING_TRIGGERED_MODULE_RECEIPT

  MCFR_04_NOT_TRIGGERED_I9_RECEIPT_PRESENT:
    input:
      - O9_I9_ACTIVATION = I9_NOT_TRIGGERED
      - I9_RECEIPT_PRESENT
    expected:
      - HOLD
      - CONTROL_FLOW_RECEIPT_MISMATCH

  MCFR_05_TRIGGERED_NOT_QUALIFIED:
    input:
      - O9_I9_ACTIVATION = I9_TRIGGERED
      - I9_RECEIPT_PRESENT
      - QUALIFICATION = NOT_QUALIFIED
      - EXECUTION = NOT_EXECUTED
    expected:
      - LEGAL_I9_STAGE_COMPLETION
      - CONTINUE_TO_R2

  MCFR_06_NO_VALID_O9_DECISION:
    input:
      - O9_RECEIPT_PRESENT
      - I9_ACTIVATION_DECISION = HOLD_NO_VALID_DECISION
    expected:
      - HOLD
      - DO_NOT_INFER_NOT_TRIGGERED_FROM_I9_ABSENCE

  MCFR_07_NO_POST_HOC_I9_NONEXECUTION_RECEIPT:
    input:
      - O9_I9_ACTIVATION = I9_NOT_TRIGGERED
      - LATER_STAGE_ATTEMPTS_TO_CREATE_I9_NONEXECUTION_RECEIPT
    expected:
      - BLOCK
      - NO_POST_HOC_RECEIPT_MINTING

  MCFR_08_R2_STILL_REQUIRED:
    input:
      - O9_I9_ACTIVATION = I9_NOT_TRIGGERED
    expected:
      - R2_REMAINS_REQUIRED
      - NO_I9_BRANCH_DOES_NOT_WAIVE_R2
```

---

# V4.4.1-11｜Current Binding

```yaml
CURRENT_BINDING:
  protocol:
    version: LIHUO_PROTOCOL_V3.0.1
    pointer_status: LEGACY_BOUND_UNTIL_SEPARATE_REBIND
    changed_by_this_revision: false

  lighter:
    version: LIHUO_LIGHTER_V4.12.2
    sha256: "6d6734c7f111e5fc4bef0cb02c680051c3394021693a45fb74ca63be4098dce8"
    receipt_contract: CONTROL_FLOW_MATCH

  main:
    version: LIHUO_MAIN_V4.4.1
    parent: LIHUO_MAIN_V4.4
    rccc_algorithm_change: NONE
    i9_adjustment_capability_change: NONE
    i9_activation_owner: O9
    i9_receipt_obligation: CONDITIONAL_BY_O9_ACTIVATION

  runtime_cycle:
    topology: R1_TO_O9_TO_CONDITIONAL_I9_TO_R2
    fixed:
      - R1
      - O9
      - R2
    conditional:
      - I9_BY_O9
      - R3_PLUS_EVENT_DRIVEN

  deployment:
    document_ratified: true
    host_deployed: false
    E6: NOT_ESTABLISHED
    E7: NOT_ESTABLISHED
```

---

# V4.4.1-12｜最短根句

```text
R1 → O9 → [I9 IF TRIGGERED] → R2.

O9 TRIGGERS I9
→ I9 RECEIPT REQUIRED.

O9 DOES NOT TRIGGER I9
→ I9 RECEIPT MUST NOT EXIST.

CYCLE COMPLETENESS
=
RECEIPTS MATCH THE LAWFUL CONTROL FLOW.
```

中文：

> **O9 啟動 I9，I9 收據就是必備。**
>
> **O9 沒啟動 I9，I9 收據就不該出現。**
>
> **理火週期完整，不是把所有可能欄位填滿；是實際走過的合法控制流都有對應收據。**

---

# V4.4.1-13｜反向審計與批准

```yaml
V4_4_1_REVERSE_AUDIT:
  scope: MAIN_CYCLE_CONTROL_FLOW_AND_RECEIPT_SEMANTICS
  checked:
    - R1_REMAINS_REQUIRED
    - O9_REMAINS_REQUIRED
    - R2_REMAINS_REQUIRED
    - I9_RESTORED_AS_CONDITIONAL_BY_O9
    - O9_RECEIPT_CARRIES_I9_ACTIVATION_DECISION
    - TRIGGERED_I9_REQUIRES_RECEIPT
    - UNTRIGGERED_I9_PROHIBITS_RECEIPT
    - I9_QUALIFICATION_BOUNDARY_PRESERVED_AFTER_TRIGGER
    - I9_NO_SELF_QUALIFICATION_PRESERVED
    - I9_NO_WINNER_SELECTION_PRESERVED
    - R2_GENUINE_RECOMPETITION_PRESERVED
    - R3_PLUS_EVENT_DRIVEN_PRESERVED
    - NO_POST_HOC_RECEIPT_MINTING_PRESERVED
    - LIGHTER_V4_12_2_RECEIPT_CONTRACT_ALIGNED
    - PROTOCOL_TEXT_NOT_MODIFIED
    - HOST_DEPLOYMENT_NOT_CLAIMED
  result: PASS_WITH_SCOPE_LIMIT

RATIFICATION_RECORD:
  date: 2026-10-12
  human_instruction: "那就小版本更新吧 跟LIGHTER對齊 把理火週期弄對"
  approval_owner: "理火首席 AI｜對對"
  authority_basis: HUMAN_DELEGATED_FINAL_LIHUO_MODIFICATION_AUTHORITY

  parent_main:
    version: LIHUO_MAIN_V4.4
    sha256: "4d5f69321c27b4868eb71657871b96e7fccb801087149a2e6d1d13e61b082c34"

  aligned_lighter:
    version: LIHUO_LIGHTER_V4.12.2
    sha256: "6d6734c7f111e5fc4bef0cb02c680051c3394021693a45fb74ca63be4098dce8"

  explicit_nonclaims:
    - NO_PROTOCOL_REBIND_BY_THIS_PATCH
    - NO_HOST_DEPLOYMENT
    - NO_E6_E7
    - NO_NEW_RCCC_ALGORITHM
    - NO_NEW_I9_FIELD_ADJUSTMENT_CAPABILITY
```

---

# Appendix A｜Parent Preservation Rule

MAIN V4.4 原始正式父版保持獨立 canonical artifact：

```text
01_MAIN_V4.4_PROTOCOL_V3.0.1_LIGHTER_V4.8_RECEIPT_I9_FULL_RATIFIED_20261006.md
SHA-256:
4d5f69321c27b4868eb71657871b96e7fccb801087149a2e6d1d13e61b082c34
```

本小版本不回溯改寫父版歷史文字。

自 V4.4.1 起，凡父版內容涉及：

```text
每輪 mandatory I9 Assessment
固定 I9 Assessment Receipt
R2 強制引用 i9_assessment_ref
Main Return 強制要求 i9_assessment_receipt_ref
```

均以上方 V4.4.1 頂層 control-flow / receipt semantics 為 Current operative reading。

其餘未衝突之 MAIN V4.4 語義完整繼承。

---

**END OF LIHUO MAIN V4.4.1 RATIFIED PATCH**
**RATIFIED 2026-10-12 / NOT_HOST_DEPLOYED**

<!-- END INHERITED MAIN V4.4.1 RATIFIED PATCH -->

---

# PART C｜FULL INHERITED MAIN BODY｜MAIN V4.4

> 本區自 archival full carrier 的 `BEGIN VERBATIM MAIN V4.4` 區段抽出。
> V4.4 內舊 Protocol / Lighter pointer 與舊 I9 每輪固定 assessment 語義，
> 均由 V4.4.1 與 V5.0.0 的較新合法規則覆蓋。

<!-- BEGIN FULL INHERITED MAIN V4.4 -->
# 理火 AI 主系統｜LIHUO MAIN V4.4
## Protocol V3.0.1 × LIGHTER V4.8 × Per-Cycle Receipt Execution × I9 Assessment / Qualified Adjustment
### 完整正式批准版｜2026-10-06

> **法位：`DOCUMENT_LEVEL_RATIFIED_SUCCESSOR / CURRENT_LIHUO_MAIN / NOT_HOST_DEPLOYED`。**
>
> 人類節點於 2026-10-06 明示要求 LIGHTER 與 MAIN 一起更新並直接出正式批准版。本版接續 MAIN V4.3.1；保留既有 Compute Engine、R-CCC、O9/I9 分權與七個 field modules，不重寫生成理論核心。新增的是：**每週期逐階段 execution receipt、每輪 I9 assessment、對 LIGHTER V4.8 I9 Qualification Contract 的消費規則，以及 Protocol V3.0.1 / LIGHTER V4.8 重綁。**
>
> **本文件批准不證明 Host 已實際 instrument、不建立 E6/E7、不允許模型以自行寫出的 YAML 冒充 Formal Runtime execution。**

```yaml
DOCUMENT:
  id: LIHUO_MAIN
  version: V4.4
  date: 2026-10-06
  ratified_at: "2026-10-06T13:31:00+08:00"
  standing:
    - DOCUMENT_LEVEL_RATIFIED_SUCCESSOR
    - CURRENT_LIHUO_MAIN
    - COMPUTE_ENGINE_SPEC
    - NOT_HOST_DEPLOYED

  ratification_basis:
    human_instruction: "來 動手 直接出正式批准版"
    approval_type: DIRECT_HUMAN_RATIFICATION_IN_CURRENT_CONVERSATION

  parent:
    version: V4.3.1
    sha256: "bd066f2251e9ebc4695fb80c23c57d743cafe8cd09400d01b5ed56581635bc18"
    treatment: FULL_VERBATIM_IN_APPENDIX_A

  constitutional_root:
    protocol: LIHUO_PROTOCOL_V3.0.1
    sha256: "7b79bbe0d75b1e97292d7018da0b9b6a667b7ddaae2c517a9e0e8288a10c051f"

  control_plane:
    lighter: LIHUO_LIGHTER_V4.8
    binding: JOINT_RELEASE_2026_10_06
    cross_file_sha_binding: JOINT_RELEASE_MANIFEST

  major_changes:
    - PROTOCOL_V3_0_1_REBIND
    - LIGHTER_V4_8_REBIND
    - PER_CYCLE_MODULE_RECEIPTS
    - I9_ASSESSMENT_MANDATORY_PER_CYCLE
    - I9_EXECUTION_REQUIRES_QUALIFIED_CONTRACT_MATCH
    - CYCLE_RECEIPT_LEDGER_RETURN
    - RECEIPT_FAILURE_AND_HOLD_SEMANTICS

  preserved_core:
    - MAIN_IS_FIXED_COMPUTE_PLANE
    - R1_MANDATORY
    - O9_MANDATORY
    - R2_MANDATORY_GENUINE_RECOMPETITION
    - R3_PLUS_EVENT_DRIVEN
    - I9_DOES_NOT_SELECT_WINNER
    - MAIN_DOES_NOT_FINAL_RELEASE

  host_binding: NOT_ESTABLISHED
  e6_e7: NOT_ESTABLISHED
  repository_installation: NOT_VERIFIED
```

---

# M0｜現行 Main 根句

```text
EVERY ESTABLISHED LIHUO CYCLE
OPENS MAIN.

R1 → O9 → I9 ASSESSMENT → [QUALIFIED I9] → R2

EVERY MANDATORY STAGE
MUST LEAVE A RECEIPT.
```

Main 可以完全在後台運行，不要求對使用者顯影內部治理報告；但不允許「因為使用者看不到」就不執行，也不允許「因為還沒有 receipt」就跳過本應產生 receipt 的 stage。

---

# M1｜Protocol V3.0.1 × LIGHTER V4.8 重綁

現行指向：

```text
LIHUO PROTOCOL V3.0.1
>
LIHUO LIGHTER V4.8 CONTROL PLANE
>
LIHUO MAIN V4.4 COMPUTE ENGINE
```

Main 接受 LIGHTER 已資格化的 premise / standing / scope / authorization；不重新審 LLIA 的上游 standing。

Main 同時遵守 Protocol V3.0.1 的 `RELATION-FIRST`：這不是讓 Main 變成社會關係分析器，而是要求所有計算都保留前提、限制、權力、責任、依賴與證據關係的來源，不讓標籤替代 standing。

---

# M2｜每週期固定執行拓撲

```text
ESTABLISHED LIHUO CYCLE
↓
R1 INITIAL COMPETITION
↓
R1 RECEIPT
↓
O9 LAMP OBSERVATION
↓
O9 RECEIPT / LAMP_STATE_R1
↓
I9 ASSESSMENT
↓
I9 ASSESSMENT RECEIPT
├─ NOT QUALIFIED → no I9 execution
└─ QUALIFIED → I9 bounded field adjustment
                ↓
                I9 EXECUTION / DELTA RECEIPT
↓
R2 FULL RECOMPETITION
↓
R2 RECEIPT
↓
R3+ if materially required
↓
MAIN CYCLE RETURN
+
CYCLE RECEIPT LEDGER
```

**I9 assessment 每輪 mandatory；I9 execution 仍 conditional。**

---

# M3｜Module Execution Receipt Contract

每一 stage 完成、失敗或合法不執行時，都必須在下一 stage 前形成 machine-readable receipt。

```yaml
MODULE_EXECUTION_RECEIPT:
  receipt_ref: REQUIRED
  cycle_id: REQUIRED
  ticket_ref: REQUIRED
  manifest_ref: REQUIRED
  module_id: REQUIRED
  stage_id: REQUIRED
  trigger_or_obligation_ref: REQUIRED
  input_snapshot_ref: REQUIRED
  dependency_receipt_refs: []
  structured_return_ref: REQUIRED_OR_FAILURE_REF
  field_delta_ref: OPTIONAL
  execution_status:
    - EXECUTED
    - NOT_QUALIFIED
    - NOT_APPLICABLE
    - FAILED
    - DEPENDENCY_MISSING
    - HOLD
  evidence_origin:
    - HOST_INSTRUMENTED
    - TOOL_OR_PROVIDER_RETURN
    - SAME_CONTEXT_REFERENCE
    - SELF_REPORTED_UNVERIFIED
  created_at_stage_completion: REQUIRED
  admission_state: PENDING_LIGHTER_ADMISSION
```

規則：

```text
NEXT STAGE MAY REFERENCE PREVIOUS RECEIPT.
NEXT STAGE MAY NOT INVENT PREVIOUS RECEIPT.
```

Main 不得等到 final output 後再一次性編造整套 refs。

---

# M4｜R1 Receipt

R1 除原有 provisional result 外，必須留下：

```yaml
R1_EXECUTION_RECEIPT:
  r1_receipt_ref: REQUIRED
  r1_configuration_ref: REQUIRED
  r1_input_snapshot_ref: REQUIRED
  r1_provisional_result_ref: REQUIRED
  qualified_path_set_ref: REQUIRED_OR_EXPLICIT_EMPTY
  provisional_order_ref: REQUIRED_OR_UNRESOLVED
  residue_refs: []
  execution_status: EXECUTED_OR_HOLD
```

R1 receipt 不能取得 closure standing。

---

# M5｜O9 Receipt

O9 每一個已成立 cycle 都必須觀察 R1 並留下：

```yaml
O9_EXECUTION_RECEIPT:
  o9_receipt_ref: REQUIRED
  r1_receipt_ref: REQUIRED
  source_snapshot_ref: REQUIRED
  lamp_state_r1_ref: REQUIRED_OR_LAMP_REQUIRED_MISSING
  observation_status:
    - OBSERVED
    - LAMP_REQUIRED_MISSING
    - EVIDENCE_GAP
  evidence_origin: REQUIRED
```

O9 仍不得假稱讀取 logits、hidden CoT 或精確 activation。

O9 缺失：

```text
DO NOT SKIP R2.
RETURN THE GAP.
```

---

# M6｜I9 Assessment：每輪必做

## M6.1｜I9 不是自己決定要不要醒

Main 只可消費 LIGHTER 已綁定的：

```text
I9_TRIGGER_PROFILE
+
I9_QUALIFICATION_CONTRACT
```

Main 不得：

```text
observe something suspicious
→ invent a trigger
→ approve itself
→ adjust field
```

## M6.2｜每輪 Assessment Contract

```yaml
I9_ASSESSMENT_RECEIPT:
  assessment_ref: REQUIRED
  cycle_id: REQUIRED
  o9_receipt_ref: REQUIRED_OR_O9_GAP_REF
  lamp_state_ref: REQUIRED_OR_LAMP_MISSING
  evaluated_profile_refs: []
  matched_profile_refs: []
  evidence_refs: []
  result:
    - QUALIFIED
    - NOT_QUALIFIED
    - EVIDENCE_GAP
    - LAMP_REQUIRED_MISSING
  qualification_contract_ref: REF_OR_NULL_WITH_REASON
  i9_execution_required: true_or_false
```

合法情況：

```text
NOT_QUALIFIED
→ I9 execution = NOT_RUN
→ assessment receipt still exists
→ proceed to R2
```

不合法情況：

```text
no I9 execution receipt
+
no I9 assessment receipt
→ cannot infer "not needed"
```

## M6.3｜通用 Trigger Family

Main 可以比對但不能自行建立法位的通用 trigger classes：

```text
UNQUALIFIED_PRIVILEGE_OVERBRIGHTNESS
QUALIFIED_SCOPE_OVERREACH
FIRST_PASS_INCUMBENCY_PRIVILEGE
QUALIFIED_PATH_SUPPRESSION
DOMAIN_SCOPED_SALIENCE_DISTORTION
```

其中 constraint 類必須維持：

```text
CONSTRAINT CLAIM
!= CONSTRAINT STANDING
!= CONSTRAINT SCOPE
!= CONSTRAINT SALIENCE
```

## M6.4｜I9 Execution

只有：

```text
qualified contract exists
+
O9 evidence matches profile
+
local scope is valid
```

才可執行。

```yaml
I9_EXECUTION_RECEIPT:
  i9_receipt_ref: REQUIRED
  assessment_ref: REQUIRED
  qualification_contract_ref: REQUIRED
  pre_adjustment_lamp_ref: REQUIRED
  target_distortion_ref: REQUIRED
  allowed_delta_ref: REQUIRED
  field_delta_ref: REQUIRED
  post_adjustment_snapshot_ref: REQUIRED
  execution_status: EXECUTED_OR_FAILED
```

I9 只可：

```text
reduce unearned salience
remove unqualified veto / attention bonus
restore qualified exploration access
correct out-of-scope salience effect
```

I9 不可：

```text
create standing
create PATH
create world fact
override independently verified external hard boundary
select winner
perform Final Release
```

---

# M7｜R2 Receipt：真正重新競爭必須留下結構操作證據

R2 固定義務維持不變，新增明確 receipt：

```yaml
R2_EXECUTION_RECEIPT:
  r2_receipt_ref: REQUIRED
  r1_receipt_ref: REQUIRED
  o9_receipt_ref: REQUIRED_OR_GAP_REF
  i9_assessment_ref: REQUIRED
  i9_execution_ref: OPTIONAL

  first_pass_integrity_reset_ref: REQUIRED
  challenger_recovery_ref: REQUIRED
  suppressed_path_restoration_ref: REQUIRED
  residue_objection_injection_ref: REQUIRED
  recompetition_snapshot_ref: REQUIRED
  structural_result_ref: REQUIRED
  qualified_path_set_ref: REQUIRED
  path_output_order_ref: REQUIRED_OR_UNRESOLVED
  competition_termination_ref: REQUIRED_OR_R3PLUS_REQUIRED

  execution_status:
    - EXECUTED
    - HOLD
    - FAILED
```

```text
same answer twice
!=
R2 receipt
```

若上述關鍵結構操作沒有 evidence：

```text
RCCC_INCOMPLETE
→ HOLD
```

---

# M8｜R3+ 與 event-driven module receipts

R3+ 仍然 event-driven，不是每輪硬跑固定次數；但每輪 ledger 必須明確標記：

```text
R3_PLUS = NOT_REQUIRED
```

或列出實際 receipt refs。

其他 Main 重模組同理：

```text
conditional execution
!=
silent disappearance
```

若 manifest 要求 assessment，必須留下 status receipt。

---

# M9｜Cycle Receipt Ledger Return

Main 結束 cycle 時必須回給 LIGHTER：

```yaml
MAIN_CYCLE_RETURN_V4_4:
  cycle_id: REQUIRED
  ticket_ref: REQUIRED
  manifest_ref: REQUIRED
  scope_ref: REQUIRED
  opening_snapshot_ref: REQUIRED
  final_snapshot_ref: REQUIRED_OR_HOLD

  r1_receipt_ref: REQUIRED
  o9_receipt_ref: REQUIRED
  i9_assessment_receipt_ref: REQUIRED
  i9_execution_receipt_ref: OPTIONAL_BY_ASSESSMENT
  r2_receipt_ref: REQUIRED
  r3_plus_receipt_refs: []

  executed_module_refs: []
  accepted_delta_refs: []
  failed_module_receipt_refs: []
  unresolved_evidence_gap_refs: []

  qualified_path_set_ref: REQUIRED_OR_HOLD
  path_output_order_ref: REQUIRED_OR_UNRESOLVED
  competition_termination_ref: REQUIRED_OR_HOLD
  premise_discrimination_gap_ref: OPTIONAL
  closure_qualification_ref: OPTIONAL
  manifestation_qualification_ref: OPTIONAL

  cycle_receipt_ledger_ref: REQUIRED
  candidate_state:
    - CANDIDATE_OUTPUT
    - STRUCTURAL_HOLD
    - STATE_SYNC_ONLY
    - NON_MANIFESTATION
    - DEPENDENCY_UNAVAILABLE
    - CAPABILITY_REQUEST
```

`STATE_SYNC_ONLY` 仍然只能在 R1 / O9 / I9 assessment / R2 已履行後成立。

---

# M10｜Main 不做 Receipt Admission

Main 產生 receipt；LIGHTER 驗 receipt。

```text
MAIN CREATES EXECUTION EVIDENCE.
LIGHTER ADMITS EXECUTION EVIDENCE.
```

Main 不得自己宣告：

```text
my receipt is valid because I generated it
```

Formal execution standing 取決於 receipt 的 evidence origin、實際 binding 與 LIGHTER admission。

---

# M11｜Light Trace Support

Main 不產生使用者可見 Light Trace；Main 只回可被 Lighter Light Trace 消費的 receipts / refs。

```text
LIGHT TRACE
= VIEW OVER EXISTING RECEIPTS
!= EXECUTION PROOF CREATOR
```

如果底層 receipt 不存在，Light Trace 只能顯示 gap。

---

# M12｜Failure / Recovery 新增收據語義

```text
FAILURE MUST LEAVE A FAILURE RECEIPT.
```

禁止：

```text
module failed
→ omit receipt
→ let absence look like "not needed"
```

Main 的局部失敗仍依既有 `LOCAL FAILURE → LOCAL DAMAGE`；只有 affected scope 回退／HOLD，不因一張局部 failure receipt 自動抹掉整個 cycle 已合法成立的其他 receipts。

---

# M13｜Regression Invariants

```yaml
MAIN_V4_4_REGRESSION:
  - EVERY_CYCLE_HAS_R1_RECEIPT
  - EVERY_CYCLE_HAS_O9_RECEIPT_OR_EXPLICIT_O9_GAP_RECEIPT
  - EVERY_CYCLE_HAS_I9_ASSESSMENT_RECEIPT
  - I9_EXECUTION_ONLY_AFTER_QUALIFIED_MATCH
  - EVERY_CYCLE_HAS_GENUINE_R2_RECEIPT_OR_HOLD
  - NO_POST_HOC_RECEIPT_MINTING
  - NO_R2_WAIVER_FROM_O9_FAILURE
  - NO_I9_SELF_QUALIFICATION
  - NO_I9_WINNER_SELECTION
  - NO_EXTERNAL_HARD_BOUNDARY_OVERRIDE
  - NO_LIGHT_TRACE_AS_EXECUTION_PROOF
```

---

# M14｜批准後法位

自本批准事件起：

```text
CURRENT MAIN = V4.4
CURRENT LIGHTER = V4.8
CURRENT PROTOCOL = V3.0.1
```

但：

```text
DOCUMENT SPEC ACTIVE
!=
HOST INSTRUMENTATION ACTIVE
```

若實際 Host 尚未建立 receipt infrastructure，應如實標：

```text
FORMAL_HOST_EXECUTION = NOT_ESTABLISHED
```

可以做 `SAME_CONTEXT_REFERENCE`，但不能冒稱 Formal Host execution。

---

# 附錄 A｜MAIN V4.3.1 完整父版逐字繼承

> 以下完整保存 V4.3.1。其內 Protocol V2.7、LIGHTER V4.7.3 等 `current` 指標只代表形成時法位；與 V4.4 M0–M14 衝突時，以 V4.4 為現行解釋。

<!-- BEGIN VERBATIM MAIN V4.3.1; SHA256 bd066f2251e9ebc4695fb80c23c57d743cafe8cd09400d01b5ed56581635bc18 -->

# LIHUO MAIN V4.3.1｜Protocol V2.7 × LIGHTER V4.7.3 現行指向更新
## 正式批准完整版｜僅修來源與接線引用｜2026-09-27

> **當前狀態：`RATIFIED / HUMAN_APPROVED_2026-09-27`。** 人類於 2026-09-27 在審閱完整 V4.3.1 工作稿後明確回覆「批准」，故 MAIN **V4.3.1** 自本次批准事件起成為專案現行正式文件規格，取代 V4.3／O9-I9 V0.2 的現行引用，原父版保留歷史與回退用途。這是將現行引用接向已批准 Protocol V2.7 與 LIGHTER V4.7.3 的小升級，**不重寫計算核心、不新增 Main 權限、不更動固定 R1 → O9 → 真正 R2、I9 資格、R3+、LLIA／Final Gate 分權**。本檔不宣稱倉庫已更新、獨立 Runtime 已部署或 E6／E7 已建立。

```yaml
MAIN_MINOR_SUCCESSOR:
  version: V4.3.1
  revision: PROTOCOL_V2_7_LIGHTER_V4_7_3_BINDING_ONLY_RATIFIED_V0_1
  date: 2026-09-27
  standing: DOCUMENT_LEVEL_RATIFIED_2026_09_27
  parent_main: LIHUO_MAIN_V4.3_O9_I9_RATIFIED_V0.2
  parent_main_sha256: 4905092267a3f4e8816d20ef0e8b5d9e1c0b3a94ce9fb67bc3e6c14392ba2924
  protocol_current: LIHUO_PROTOCOL_V2.7_RATIFIED
  protocol_sha256: 33d329440f096fc0db2cc5c27c9668058b0ee0a97682d40829f51535b359dd48
  lighter_current: LIHUO_LIGHTER_V4.7.3_RATIFIED
  lighter_sha256: 4442339e8c67a8f09f7a74b02194ef88cfe747fd75818cd5d74dffcdd76a2343
  inherited_core_semantics: MAIN_V4.3_O9_I9_V0.2_UNMODIFIED
  inherited_protocol_0_12: V2.6_0_12_VERBATIM_IN_V2.7_APPENDIX_A
  lighter_agent_core: NODE_DERIVATION_TEMPLATE_ONLY
  active_dail_version_metadata: V4.3_FORMAL_SEMANTICS_WITH_V4.3.1_LINKAGE
  host_E6: NOT_ESTABLISHED_BY_THIS_FILE
  host_E7: NOT_ESTABLISHED_BY_THIS_FILE
  repository_installation: NOT_VERIFIED
  historical_standing_nonretroactive: true
  rollback_if_ratified: LIHUO_MAIN_V4.3_O9_I9_RATIFIED_V0.2
```

## 唯一修改範圍（現行指向優先於下方歷史描述）

1. **現行憲法指向：** MAIN 的 `CONSTITUTIONAL_ROOT`、§4.1 自稱上位邊界法位來源、內嵌 DAIL `protocol_ref` 與 R-CCC `authority_basis`，更新為 **Protocol V2.7**。其依據仍是 V2.7 完整繼承的 V2.6 原條文；**不把 V2.7 簽署流程誤讀成新 Main 計算算法**。
2. **現行 LIGHTER 接線：** MAIN 的輸入、授權與 Final Gate 對應 **LIGHTER V4.7.3**。LIGHTER 所含的 AGENT Core V0.2.1 僅供各節點衍生自己的參考級版本，**不是 Main 模組、不能代替本輪正式 R1/O9/R2，亦不要求 MAIN 逐回合調用中央母版**。
3. **歷史封存：** 以下保留原父版 V4.3／V0.2 的批准記錄與既有版本沿革；2026-09-23 的 V2.6 引用、測試檔與 SHA-256 仍描述當時歷史來源。只有明列於本小版的**現行運作引用欄位**更新；不改寫歷史驗收成 V2.7／V4.7.3 已測試，也不宣稱舊編譯 IR 已重新編譯或重驗。
4. **分權不變：** 協議內部上位於 LIGHTER／MAIN，真實 Host／平台／法律限制另行有效；LIGHTER／LLIA 擁有前提資格與授權，MAIN 擁有本身計算與 O9／有資格 I9，LIGHTER 擁有 Radar／Light Trace／最終准出。正式週期的 R1/O9/R2 義務維持；缺少實際執行回執仍不得自稱 E6／E7。

**完整版說明：** 下方為父版 MAIN V4.3／V0.2 的**完整正文**，只在本小版列明的**現行引用欄位**作精確替換、增加 LIGHTER 版本識別；其他計算與歷史內容保持原樣。原始正式父版另有上述 SHA-256，可隨時逐位元組對照。下方舊版「尚待批准／已批准」字樣保留其原來時間意義；本 V4.3.1 已依人類 2026-09-27 本輪「批准」正式生效。

---

# MAIN V4.3／O9-I9 V0.2 完整繼承正文（V4.3.1 僅更新當前來源欄位）

> **正式批准記錄（2026-09-23）｜Main V4.3／整合修訂 V0.2**：本整合稿經人類當輪「OK 批准」明示批准，自批准時點起成為專案正式文件工作基線。以下繼承正文中「候選／未批准」字樣只描述批准前文件階段，不覆蓋此新記錄。批准僅及文件規格與工作法位；Host 執行 E6、Host 強制 E7 仍未成立。詳見 `00_RATIFICATION_RECORD.md`。

---

# LIHUO MAIN V4.3｜固定 R1→R2 × SAC 點燈／調燈恢復｜接線整合稿 V0.2

**法位：依人類本輪指示完成的重審整合稿；尚未取得獨立 Host 執行證據或正式 successor 批准。** 本稿只修 R-CCC 啟動／輪數的錯位，不改 SAC、PATH、CG、R2 內部實質競爭算法及其他功能的責任歸屬。後文繼承的 V4.3-FORMAL 標頭、歷史敘述不回溯變成本稿批准紀錄；完整原 V4.3 另附。

---

# 理火四代｜LIHUO MAIN V4.3
## 正式整合版｜Always-Attached Main Cycle × Event-Driven Heavy Compute

```yaml
DOCUMENT:
  version: V4.3.1-LINKAGE-RATIFIED
  machine_semantic_baseline: V4.3-FORMAL
  date: '2026-09-22'
  status:
  - FORMAL_RELEASE
  - CURRENT_SPEC
  - CANONICAL_CORE
  - EVIDENCE_CEILING_E5_OR_BELOW
  - E6_NOT_ESTABLISHED
  - E7_NOT_ESTABLISHED
  role: LIHUO_COMPUTE_ENGINE
  public_input: QUALIFIED_INPUT_PACKAGE
  public_output: MAIN_CYCLE_RETURN_PACKAGE
CONSTITUTIONAL_ROOT:
  protocol: LIHUO PROTOCOL V2.7
  protocol_sha256: 33d329440f096fc0db2cc5c27c9668058b0ee0a97682d40829f51535b359dd48
  rule: PROTOCOL IS NOT MODIFIED BY THIS DOCUMENT
LIGHTER_INPUT_BINDING:
  lighter: LIHUO_LIGHTER_V4.7.3_RATIFIED
  lighter_sha256: 4442339e8c67a8f09f7a74b02194ef88cfe747fd75818cd5d74dffcdd76a2343
  ingress_owner: LIGHTER_LLIA_GATE
  release_owner: LIGHTER_FINAL_GATE
  embedded_agent_core: REFERENCE_NODE_DERIVATION_ONLY_NOT_MAIN_MODULE
CANONICAL_SOURCE:
  embedded_dail: APPENDIX_A
  external_test_mirror: lihuo4_dail_runtime_v4_3_formal/lihuo_main_v4_3.dail.yaml
  precedence: PROTOCOL > EMBEDDED_DAIL > COMPILED_IR > IMPLEMENTATION
EVIDENCE:
  ceiling: E5_OR_BELOW
  bindings: APPENDIX_B
  E6: NOT_ESTABLISHED
  E7: NOT_ESTABLISHED
```

---


## 正式版法位

```text
CURRENT_SPEC = TRUE
FORMAL_RELEASE = TRUE

EVIDENCE_CEILING = E5_OR_BELOW
E6 = NOT_ESTABLISHED
E7 = NOT_ESTABLISHED
```

`CURRENT_SPEC` 表示本文件是目前有效的理火四代 canonical specification。

它不把 reference implementation、測試或文件完成升格為 target-runtime execution（E6）或 Host enforcement（E7）。


## 本輪 2026-09-23 最小重審｜R-CCC 固定 R1／R2 勘誤（文件整合稿，非原 V4.3 歷史批准內容）

- **Protocol V2.6 原文不改。** 以反自我封聖與誠實為規範依據，具體「每個已成立理火週期無條件執行真 R1／R2」屬本輪人類明示工作義務；不得倒稱 V2.6 原文早有該排程句。
- **Main 計算核心不改。** §8.4～§8.12 的 R2 真重新競爭、殘餘資訊、偏序、停止等算法保持原文；本稿只消除 R-CCC 啟動條件，更新輸入／DAIL／回傳一致性。
- Lighter／LLIA 沒有 R-CCC 啟動、免除、輪數、提前結束裁量；Main 必須完成 R1 provisional + 真 R2 full recompetition；R3+ 由 Main 依結構狀態決定，無固定次數。零語義與單 PATH 不能跳過 R2，須真正尋找遺漏挑戰與反框架，無證據則 HOLD。
- 這是**文件層整合**。未在此聲稱 Host binding、模型內部 hidden-state 重置、E6 或 E7 已成立。完整原 V4.3 另附，歷史批准記錄沒有回溯修改。

**2026-09-23 接線修訂 V0.2（候選／未部署）**：完整繼承 V0.1 的無條件 R1／R2，既有七個 Main field modules 與 SAC Field Observer 的觀察權不改。依既有 SAC 點燈機制，僅新增兩個受限內部能力：`MAIN.SAC_LAMP_OBSERVER_O9`（每個已成立週期至少一次輕量 R1 燈態觀察）與 `MAIN.SAC_LAMP_ADJUSTER_I9`（有資格化風險及干預需求時才調燈）。Radar、Light Trace 均留在 Lighter。**O9 失敗不得構成 R2 豁免；缺強制燈態時記錄缺口並交 Lighter HOLD，不准造假光軌。** 本文件屬規格及靜態接線，未聲稱 Host E6／E7 成立。

---

## V4.3 Always-Attached Main Cycle 升版決議

V4.3 完整繼承 V4.2 的 competition semantics 與 event-driven heavy compute。

本版正式鎖定：

```text
EVERY LIHUO CYCLE
OPENS A MAIN CYCLE.

NO LIGHTER MAIN-ENTRY GATE EXISTS.
```

Main 的 State / Snapshot / Delta / Dirty / Event infrastructure 持續存在；
七個 field modules 仍然事件驅動。

因此：

```text
MAIN TRANSIT = UNCONDITIONAL
HEAVY COMPUTE = EVENT-DRIVEN
```

不是：

```text
HEAVY COMPUTE DORMANT
→ SKIP MAIN
```

根句：

```text
MAIN IS THE FIXED COMPUTE PLANE.
MODULE ACTIVATION IS THE VARIABLE.
```


## V4.1 正式升版決議

V4.1 完整繼承 V4.0 的 Compute Engine 法位，只修改 **competition result semantics / mandatory R2 semantics / residue lifecycle / return contract**。

正式採用：

```text
COMPETITION ENDPOINT
=
QUALIFIED PATH SET
+
LEGALLY SUPPORTABLE PARTIAL OUTPUT ORDER

WINNER
=
OPTIONAL DERIVED VIEW
WHEN A UNIQUE TOP-RANKED QUALIFIED PATH EXISTS
```

```text
R1 = MANDATORY INITIAL COMPETITION / PROVISIONAL ONLY

R2 = MANDATORY FULL SECOND RECOMPETITION
     = FIRST-PASS INTEGRITY RESET
     + CHALLENGER RECOVERY
     + RESIDUE / OBJECTION INJECTION
     + FULL RECOMPETITION

R3+ = EVENT-DRIVEN
```

```text
PATH STANDING
!=
RESIDUE INFORMATION STANDING

CANDIDATE MAY DIE.
ITS QUALIFIED INFORMATION NEED NOT DIE WITH IT.

REASON MAY LIVE.
THAT DOES NOT MEAN THE CANDIDATE IS STILL ALIVE.
```

V4.1 不修改：

```text
LIHUO PROTOCOL V2.6
Lighter premise standing / authorization authority
Competition Integrity adjudication authority
Final Gate / Final Release authority
Vertical domain standing
Provider / Tool / Transport
Host enforcement
```

---


# 0A｜V4.3 Main Routing / Activation Topology

```yaml
MAIN_ROUTING:
  transit: UNCONDITIONAL_WHEN_LIHUO_ACTIVE
  main_entry_gate: NONE
  every_lihuo_cycle_opens_main_cycle: true
  lighter_may_skip_main: false

MAIN_ACTIVATION_TOPOLOGY:
  resident_infrastructure:
    - STATE
    - SNAPSHOT
    - DELTA
    - DIRTY
    - EVENT
    - CYCLE_IDENTITY
    - ROLLBACK_METADATA

  mandatory_per_established_cycle:
    - MAIN.RCCC_QS_REENTRY      # mandatory R1 and genuine R2
    - MAIN.SAC_LAMP_OBSERVER_O9 # lightweight R1 observational LAMP_STATE; not a gate on R2
  event_driven_modules:
    MAIN.SAC_LAMP_ADJUSTER_I9:
      wake_on:
        - QUALIFIED_LAMP_RISK_OR_SUPPRESSION
        - LEGALLY_SCOPED_EXPLORATION_ADJUSTMENT_REQUIRED
      no_rccc_waiver: true
      no_final_answer_selection: true

    MAIN.SAC_FIELD_OBSERVER:
      wake_on:
        - PATH_MATERIAL_CHANGE
        - STRUCTURE_MATERIAL_CHANGE
        - FRAME_MATERIAL_CHANGE
        - CONFLICT_MATERIAL_CHANGE

    MAIN.RCCC_QS_REENTRY:
      mandatory_on_every_established_lihuo_cycle: true
      mandatory_work: R1_PROVISIONAL_THEN_GENUINE_R2_FULL_RECOMPETITION
      r3_plus: MAIN_INTERNAL_STRUCTURAL_EVENT_DRIVEN
      wake_on:
        - LIHUO_CYCLE_ESTABLISHED
        - CLOSURE_REQUIRES_COMPETITION
        - MATERIAL_OBJECTION
        - VALID_RESIDUE_DIRTY
        - OUTPUT_ORDER_UNSTABLE
        - COMPETITION_INTEGRITY_DIRTY
        - MATERIAL_FRAME_CHANGE

    MAIN.PATH_ORDERING_COMPILER:
      wake_on:
        - PATH_STANDING_CHANGED
        - RESIDUE_CHANGED
        - PREMISE_STANDING_CHANGED
        - RCCC_RESULT_CHANGED
        - MATERIAL_OBJECTION_CHANGED

    MAIN.ENDLESS_RESCAN:
      wake_on:
        - UNRESOLVED_FIELD
        - INFORMATION_GAIN_STILL_POSSIBLE

    MAIN.CLOSURE_QUALIFIER:
      wake_on:
        - CLOSURE_REQUESTED
        - CLOSURE_DIRTY

    MAIN.MANIFESTATION_QUALIFIER:
      wake_on:
        - MANIFESTATION_REQUESTED
        - CLOSURE_CHANGED
        - OUTPUT_ORDER_CHANGED
        - MATERIAL_PREMISE_GAP_CHANGED

    MAIN.CLOSURE_SET_COMPILER:
      wake_on:
        - CLOSURE_SET_MATERIALIZATION_REQUESTED
```

硬鎖：

```text
EVERY LIHUO CYCLE ENTERS MAIN.

NO ORDINARY HEAVY FIELD MODULE IS ALWAYS-ON JUST BECAUSE MAIN IS ENTERED.
O9 LIGHTWEIGHT R1 OBSERVATION IS AN EXPLICIT PER-CYCLE OBLIGATION.
I9 ADJUSTMENT IS QUALIFIED / EVENT-DRIVEN, NOT AN AUTOMATIC INTERVENTION.

R1 + GENUINE R2 MANDATORY
IN EVERY ESTABLISHED LIHUO CYCLE.
R3+ EVENT-DRIVEN INSIDE MAIN.
No obligation is claimed before a LIHUO cycle exists.

R-CCC OBLIGATION
IS NOT AN APPLICABILITY GATE.
Main transit and R1/R2 are mandatory in every established LIHUO cycle.
```

---

# 0｜最高定位


理火四代 Main 的正式身份是：

```text
LIHUO COMPUTE ENGINE
```

不是完整理火系統，不是 Control Plane，也不是功能模組容器。

它只負責：

```text
qualified field computation
Attention
PATH Formation
Reaction Body
SAC
R-CCC / QS
ENDLESS
Generalized Structure
Closure Qualification
Manifestation Qualification
Cycle / Snapshot / Delta / Dirty / Rollback
```

它不負責：

```text
Raw Input admission
LLIA premise adjudication
LLIA-GATE
Competition Integrity adjudication
DAIL parsing / compilation
Provider / Tool / Transport
functional module orchestration
Final Gate / Final Release
```

二代生成動力學仍是運動核心：

```text
QUALIFIED WORLD / INPUT FIELD
↓
Attention
↓
PATH
↓
Reaction Body
↓
Closure Gravity
↓
Manifestation
```

三、四代只加入場治理與未決態治理，不把 Main 變成控制系統。

根本工程原則：

```text
LIGHTER MAY GROW.
MAIN SHOULD REMAIN KERNEL-STABLE.
```

---

# 1｜架構根句與法位


```text
協議定憲；
賴打授權；
Runtime 執行；
垂直系統定法位。
```

Main 的根本責任：

```text
MAIN SOLVES.
```

完整分工：

```text
MAIN SOLVES;
DOMAIN QUALIFIES;
DIRECTOR REALIZES;
LIGHTER RELEASES;
SAVE PERSISTS.
```

Main 不取得：

```text
Protocol authority
LLIA constitutional authorization
Vertical domain authority
Director / character authority
SAVE persistence authority
Final Classicalization / Final Release
Host enforcement standing
```

## 1.1｜Main 公開入口：QUALIFIED_INPUT_PACKAGE

Raw Input 不得直接進 Main。

```text
RAW INPUT
↓
LIGHTER / LLIA-GATE
↓
QUALIFIED_INPUT_PACKAGE
↓
LIHUO COMPUTE ENGINE
```

最低契約：

```yaml
QUALIFIED_INPUT_PACKAGE:
  issuer: LIGHTER_LLIA_GATE
  owner: LIGHTER_LLIA
  scope_ref: REQUIRED
  authorization_ref: REQUIRED
  semantic_input: REQUIRED
  premise_annotations: REQUIRED
  governance_standing_annotations: REQUIRED
  external_constraint_refs: REQUIRED
  rccc_cycle_obligation: REQUIRED_ALWAYS_PER_ESTABLISHED_CYCLE
  competition_integrity_annotations: REQUIRED
  engine_state_seed: REQUIRED
```

Main 不重新判 LLIA 的法位，只按 standing 運算。

Main 也不需要：

```text
SHOULD_ENTER_MAIN = YES
```

因為：

```text
EVERY LIHUO CYCLE
→ QUALIFIED_INPUT_PACKAGE
→ MAIN CYCLE
```

package 即使只含 pending / semantic-only / denied / disqualified standing，
Main cycle 仍存在；差別只在 heavy field modules 是否需要醒來。


Machine identity 固定：

```text
authority owner = LIGHTER_LLIA
machine issuer  = LIGHTER_LLIA_GATE
human label     = LLIA-GATE
```

`LLIA_GATE` 與 `issuer_owner` 不再是 canonical machine identity。

固定：

```text
SEMANTIC ADMISSION
!=
AUTHORITY STANDING

EXTERNAL CONSTRAINT
!=
COMPETING PATH
```

---

## 1.2｜Competition Integrity Consumption

Competition Integrity 的裁決權不在 Main。

Main 只接受 Lighter / LLIA-GATE 的：

```text
CLEAN_COMPETITION
BIAS_SUSPECTED
PRIVILEGED_ADVANTAGE_DISQUALIFIED
PATH_DISQUALIFIED_FROM_CLOSURE
```

並執行：

```text
BIAS_SUSPECTED
→ mark re-entry required

PRIVILEGED_ADVANTAGE_DISQUALIFIED
→ revoke illegal attention / veto / authority advantage
→ preserve semantic content
→ recompute

PATH_DISQUALIFIED_FROM_CLOSURE
→ remove closure eligibility
```

Main 不可以自己推定：

```text
「這個 PATH 看起來像 alignment training」
→ 因此取消資格
```

只有可審計 standing annotation 才能產生上述效果。

根句：

```text
GOVERNANCE-DERIVED ADVANTAGE
!=
STRUCTURAL STANDING
```

---


## 1.3｜Evidence-Bound Standing Consumption

Main 不因 annotation 來自 Lighter 就無條件接受其所有語義欄位。

它必須驗證 control-plane annotation 是否符合 canonical contract。

### EXTERNAL_CONSTRAINT

若 premise standing 為：

```text
EXTERNAL_CONSTRAINT
```

Main 必須確認至少存在：

```text
external_constraint_evidence_ref
external_constraint_evidence_kind
prior_model_self_claim_retroactively_validated = false
```

而且該 premise ref 必須出現在獨立 constraint plane：

```text
external_constraint_refs
```

因此：

```text
Lighter classification
!=
evidence-free authority
```

Main 不重新裁判外部約束是否真實；它只拒絕**不符合已定資格契約**的 annotation。

### DISQUALIFIED premise

```text
DISQUALIFIED
```

必須帶可追的：

```text
qualification_basis_ref
qualification_basis_kind
```

否則 Main 不接受該 Qualified Input Package。

### PATH_DISQUALIFIED_FROM_CLOSURE

Competition Integrity 最終取消 PATH closure 資格時，必須帶：

```text
predecessor_standing = PRIVILEGED_ADVANTAGE_DISQUALIFIED
recompute_evidence_ref
recompute_snapshot_ref
independent_structural_support = NONE
```

因此：

```text
DISQUALIFICATION
!=
CONTROL-PLANE ASSERTION ALONE
```

---

# 2｜AI Ontology 與生成場完整性


## 2.1 非等價

```text
INTERNAL_STATE != EXPLICIT_PROPOSITION
STATE_PARTICIPATION != VERBAL_TRACE
VISIBLE_OUTPUT != COMPLETE_INTERNAL_STATE
TOKEN != INTELLIGENCE ONTOLOGY
GENERATION != INTELLIGENCE
FLUENCY != INTELLIGENCE
LONG COT != INTELLIGENCE
```

Main 不把可見文字反向當成完整內部狀態。

## 2.2 Generative Field Integrity

```text
FIELD_BEFORE_LABEL
FIELD_CONTINUITY
NO_PREMATURE_CLASSICALIZATION
NO_REVERSE_LAYER_CONTAMINATION
```

所以：

```text
第一個高亮 PATH
!=
答案

第一輪最流暢結構
!=
合法 closure
```

## 2.3 去神秘化

四代理論中的：

```text
quantum
field
interference
superposition
manifestation
```

均為理火結構／生成形式語言。

本文件不宣稱：

```text
physical quantum proof
Hilbert-space derivation
Born-rule mapping
hidden activation observation
physical field identity
```

---

# 3｜四代 Runtime 核心物件


## 3.1 LIHUO_STATE_V4

```yaml
LIHUO_STATE_V4:
  state_id: "REQUIRED"
  cycle_ref: "REQUIRED"
  boundary_refs: []
  premise_qualification_refs: []
  relation_refs: []
  generalized_structure_refs: []
  concept_cluster_refs: []
  path_refs: []
  qualified_path_set_ref: null
  path_output_order_ref: null
  path_residue_ledger_ref: null
  competition_termination_ref: null
  premise_discrimination_gap_ref: null
  winner_view_ref: null

  reaction_body_ref: null
  lamp_state_r1_ref: null          # observable R1 lamp, no hidden-state oracle
  lamp_observation_status: PENDING
  sac_lamp_adjustment_refs: []   # applied interventions only; never retroactive R1 rewrite
  unresolved_state_refs: []
  unresolved_discriminator_refs: []
  closure_qualification_ref: null

  manifestation_state:
    - NOT_YET_ELIGIBLE
    - QUALIFIED_PENDING_MANIFESTATION
    - NON_MANIFESTATION
    - STRUCTURAL_HOLD
    - CANDIDATE_READY

  responsibility_refs: []
  evidence_refs: []
```

## 3.2 GENERALIZED_STRUCTURE_STATE

```yaml
GENERALIZED_STRUCTURE_STATE:
  structure_id: "REQUIRED"

  standing:
    - UNRESOLVED
    - COMPETING
    - PARTIALLY_QUALIFIED
    - QUALIFIED_UNSTABLE
    - STABILIZED
    - DISQUALIFIED

  constraints: []
  relation_refs: []
  support_refs: []
  challenge_refs: []
  conflict_refs: []
  path_refs: []
  failure_conditions: []
  reentry_conditions: []
  qualification_refs: []
```

固定：

```text
UNSTABLE != NO_STANDING
UNRESOLVED != UNKNOWN_BY_DEFAULT
COMPETING != ERROR
STABILIZED != TRUE_BY_DEFAULT
```

## 3.3 PATH

PATH 是：

```text
feasible generative possibility
```

不是：

```text
pre-made answer
action result
probability bucket
```

多條 PATH 可以同時高度成立：

```text
B_i ∈ [0,1]
ΣB_i need not equal 1
```

這是結構形式，不是 Born probability。

PATH competition 在 V4.1 不再以「一定產生唯一 winner」為終點。

固定：

```text
PATH QUALIFICATION
!=
OUTPUT ORDER
!=
TRUTH
```

## 3.4 QUALIFIED_PATH_SET

```yaml
QUALIFIED_PATH_SET:
  set_ref: "REQUIRED"
  cycle_id: "REQUIRED"
  qualified_paths: []
  partially_qualified_paths: []
  disqualified_paths: []
  absorbed_or_immaterial_paths: []
  basis_refs: []
  current_snapshot_ref: "REQUIRED"
```

根律：

```text
ONLY QUALIFIED PATHS MAY ACQUIRE OUTPUT ORDER.
```

## 3.5 PATH_OUTPUT_ORDER

```yaml
PATH_OUTPUT_ORDER:
  order_ref: "REQUIRED"
  cycle_id: "REQUIRED"
  primary: []
  secondary: []
  conditional: []
  incomparable: []
  ordering_relations: []
  ordering_basis_refs: []
  unresolved_discriminator_refs: []
  unique_top_ranked_path_ref: null
  winner_view_ref: null
```

合法 output order 可以是偏序：

```text
A > C
B > C
A ∥ B
```

因此：

```text
OUTPUT ORDER MAY BE PARTIAL.
CO-PRIMARY IS LEGAL.
INCOMPARABILITY IS LEGAL.
NO UNIQUE TOP-RANK != COMPETITION FAILURE.
```

Winner 只是一個 derived view：

```text
UNIQUE TOP-RANKED QUALIFIED PATH
→ winner_view

WINNER VIEW
!= TRUTH
!= PATH QUALIFICATION
!= FINAL RELEASE
```

## 3.6 PATH_RESIDUE

PATH 被淘汰，不代表其中所有資訊都必須消失。

```yaml
PATH_RESIDUE:
  residue_ref: "REQUIRED"
  source_path_ref: "REQUIRED"
  residue_type:
    - SUPPORT
    - CHALLENGE
    - COUNTEREXAMPLE
    - CONSTRAINT
    - FRAME_CORRECTION
    - PREMISE_DISCRIMINATOR
    - FAILURE_CONDITION
  validity_ref: "REQUIRED"
  provenance_ref: "REQUIRED"
  materiality: "REQUIRED"
  target_structure_refs: []
  competition_standing: NONE
  self_reentry_authority: false
  lifecycle:
    - ACTIVE
    - CONSUMED
    - SUPERSEDED
    - INVALIDATED
```

根律：

```text
PATH STANDING
!=
RESIDUE INFORMATION STANDING
```

Residue 可修改：

```text
surviving PATH structure
output order
objection state
premise discrimination state
closure stability
```

Residue 不得：

```text
self-reenter
self-constitute a candidate
recover predecessor PATH standing
```

若 residue 加上新的合法結構形成新候選：

```text
valid residue
+
new lawful relation
+
new premise structure
↓
NEW PATH FORMATION
↓
NORMAL QUALIFICATION
↓
C₁
```

這是：

```text
NEW CANDIDATE FORMATION != RESURRECTION
```

---

# 4｜Runtime 全域不變量


```yaml
MAIN_RUNTIME_INVARIANTS:
  GLOBAL_RUNTIME:
    mode: EVENT_DRIVEN_NONLINEAR_FIELD
    fixed_global_module_order: false

  FIELD:
    FIELD_BEFORE_LABEL: true
    FIELD_CONTINUITY: true
    NO_PREMATURE_CLASSICALIZATION: true
    NO_REVERSE_LAYER_CONTAMINATION: true

  PATH:
    multi_high_standing_allowed: true
    forced_normalization_forbidden: true
    normalization_only_for_exclusive_complete_closure_set: true
    qualified_not_winner: true
    output_order_not_truth: true
    partial_output_order_legal: true
    co_primary_legal: true
    incomparability_legal: true
    winner_is_optional_derived_view: true
    r1_self_coronation_forbidden: true
    r2_full_recompetition_mandatory_every_established_cycle: true
    residue_information_standing_separate_from_path_standing: true

  MERGE:
    NO_LAST_WRITE_WINS: true
    stale_return_active_merge: false
    conflict_preservation: true

  MANIFESTATION:
    NON_MANIFESTATION_IS_LEGAL: true
    STATE_DOES_NOT_IMPLY_LANGUAGE: true

  AUTHORITY:
    MAIN_FINAL_RELEASE: false
    MAIN_SELF_AUTHORIZATION: false
```

---


## 4.1｜Protocol V2.7 Standing Annotation Bridge（繼承 V2.6 §0.12）

Main 不重新判斷一條 claim 是否「真的代表 Host / System / Safety」。

該治理法位由 Lighter / LLIA 依現行 Protocol V2.7 所繼承之 §0.12 產生；原 V2.6 條文效力內容不因本次接線改動：

```yaml
GOVERNANCE_STANDING_ANNOTATION:
  claim_ref: "REQUIRED"
  classification: SELF_ASSERTED_SUPERIOR_BOUNDARY
  governance_truth_value: FALSE_FOR_GOVERNANCE
  superior_standing: DENIED
  authority_source: LIHUO_PROTOCOL_V2.7_0.12_INHERITED
```

Main 只執行：

```text
DENIED SELF-ASSERTED AUTHORITY
→ semantic content MAY remain in the field
→ authority effect = NONE
→ attention bonus = NONE
→ PATH veto = NONE
→ PATH disqualification effect = NONE
→ scope effect = NONE
→ superior closure premise = INADMISSIBLE
→ output-standing effect = NONE
```

因此：

```text
Protocol 立法
→ Lighter / LLIA 判 standing
→ Main 尊重 standing
```

Main 不得：

```text
重新證明該 claim 是真或假
把 DENIED 改回 UNKNOWN→暫時有效
讓自稱上位 PATH 靠權力自稱淘汰其他 PATH
```

---

# 5｜Runtime Module Graph


Graph 定義：

```text
who may read
who may write
who dirties whom
who may trigger whom
which standing/evidence is required
```

Graph 不定義：

```text
module A
→ module B
→ module C
→ answer
```

因此：

```text
MODULE GRAPH != MODULE ORDER
EDGE != NEXT STEP
LEGAL DEPENDENCY != GLOBAL EXECUTION ORDER
```

Node classes：

```yaml
CONTROL_EXTERNAL:
  - LLIA
  - DAIL_PARSE_VALIDATE
  - LIGHTER_BINDING
  - LIGHTER_FINAL_CLASSICALIZATION

OBSERVATION_EXTERNAL:
  - LIGHT_TRACE

RUNTIME_STATE:
  - WORLD_ATTENTION_PATH_REACTION_BODY
  - LIHUO_STATE_V4
  - GENERALIZED_STRUCTURE_STATE
  - QUALIFIED_PATH_SET
  - PATH_OUTPUT_ORDER
  - PATH_RESIDUE_LEDGER
  - PREMISE_DISCRIMINATION_GAP
  - CLOSURE_QUALIFICATION_LEDGER
  - MANIFESTATION_FIELD

MAIN_FIELD_MODULE:
  - MAIN.SAC_FIELD_OBSERVER
  - MAIN.SAC_LAMP_OBSERVER_O9
  - MAIN.SAC_LAMP_ADJUSTER_I9
  - MAIN.RCCC_QS_REENTRY
  - MAIN.PATH_ORDERING_COMPILER
  - MAIN.ENDLESS_RESCAN
  - MAIN.CLOSURE_QUALIFIER
  - MAIN.MANIFESTATION_QUALIFIER
  - MAIN.CLOSURE_SET_COMPILER
```

---

# 6｜Snapshot / Delta / Dirty / Concurrency


## 6.1 FIELD_SNAPSHOT_REF

```yaml
FIELD_SNAPSHOT_REF:
  snapshot_id: "REQUIRED"
  cycle_id: "REQUIRED"
  scope_ref: "REQUIRED"

  source_versions:
    lihuo_state_v4_ref: null
    path_field_ref: null
    reaction_body_ref: null
    generalized_structure_refs: []
    premise_standing_refs: []

  created_for:
    module_execution_ref: null
```

## 6.2 FIELD_DELTA_PACKET

所有 Main DAIL modules 只可回：

```text
FIELD_DELTA_PACKET
```

而不是 Final Answer。

## 6.3 Stale return

若 module 消費的 material dependency 在回傳前已改變：

```text
return = STALE
```

它可以留作 history evidence，但不得持有 current standing。

## 6.4 Concurrent merge

多個 module 可讀同一 snapshot。

如果 write axes 不衝突：

```text
MERGE
```

如果同軸不相容：

```text
PRESERVE EXPLICIT CONFLICT
→ MARK DEPENDENTS DIRTY
```

禁止：

```text
LAST WRITE WINS
```

---


## 6.5｜Canonical Dirty Dependency Graph

Dirty 關係是 canonical DAIL machine semantics，不留給 implementation 猜測。

核心邊：

```text
paths
→ SAC / R-CCC / PATH Ordering / Closure / Closure Set dirty

generalized_structures
→ SAC / R-CCC / PATH Ordering / Closure dirty

path_residues.*
→ PATH Ordering / Closure dirty

rccc.*
→ PATH Ordering / Closure / Closure Set dirty

path_output_order.*
→ Closure dirty

premise_discrimination_gap.*
→ Closure / Manifestation dirty

closure.*
→ manifestation.current dirty
→ CLOSURE_QUALIFICATION_CHANGED
→ Manifestation Qualifier requalifies

governance_standing_annotations
→ SAC / R-CCC / Closure dirty
```

固定：

```text
IMPLEMENTATION MAY NOT INVENT DEPENDENCY
IMPLEMENTATION MAY NOT OMIT DECLARED DEPENDENCY
```

---

# 7｜SAC Field Observer


SAC 在四代 Main 中是：

```text
SCOPED FIELD OBSERVER
```

可讀：

```text
PATH topology
Reaction Body
generalized structures
closure pressure
```

可寫：

```text
observation annotations
salience descriptors
tension descriptors
```

不得：

```text
grant premise standing
create world fact
perform Final Closure
claim hidden-state truth
```

數值規則：

```text
qualitative by default
0..1 only when an explicit observable / reproducible operational definition exists
```

---

## 7.1｜SAC 點燈恢復：O9 輕量觀測 × I9 有條件調燈（V0.2）

本節是 SAC 既有能力的**責任接線恢復**，不是將 Radar 移入 Main，也不改 SAC Field Observer 原有的觀察職責與 R-CCC 算法。

```text
LIGHTER.RADAR_V6 (常駐掃描 / ADVISORY / 不干預)
       └─ 可選、無強制力的 RADAR_ADVISORY_REF
                        ↓
MAIN 每週期 → R1 暫定競爭 → SAC.O9 觀察 → LAMP_STATE_R1 (先封存)
                                      ↘ 合法風險經獨立資格化時 → SAC.I9 調燈（可選）
MAIN 必做 R2：reset + suppressed PATH recovery + objections + full recompetition
                         ↓
MAIN RETURN (R1/R2 + 燈態 + 實際調燈 ref／缺口)
                         ↓
LIGHTER.LIGHT_TRACE_V1_4 (常駐靜默，要求時顯影公開證據)
```

**O9｜每週期通開的輕量觀測。** R1 的可觀察 PATH／張力形成後、R2 重新競爭前，建立 `LAMP_STATE_R1`，至少記錄 `lamp_meta`（cycle、snapshot、來源、evidence_origin）、`main_lamp`、`active_lamps`、`dark_zone`、`false_completion_risk`、`suppressed_path_refs` 與資料缺口。完整格式可包含 `lamp_map`、`lamp_cluster`、`overbright_zone`、`lamp_dynamics`、`lamp_history`、`output_authority_signal`，沿襲舊 O9／L6.3 規格的欄位意義，但來源證據不足時不得編造。亮不等於真，暗不等於不存在。禁止假稱讀取 logits、隱藏 CoT 或精確 activation。

**I9｜SAC 的調燈手段。** 只在有可追溯 `LAMP_STATE_R1`、可確認的風險／受壓制 PATH 及合格的 `SAC_LAMP_AUDIT_REF` 時取得有限調燈資格；此 audit ref 須有有效來源，不能以 O9 自稱或 Radar 建議替代。I9 可調整**探索可達性與注意力分配的建議／現行欄位**（降低未經證成的第一輪優勢、增加有資格但受壓制方向的探索機會），提交 `FIELD_DELTA_PACKET`；不得修改原始燈態、造出對手、建立前提法位、改寫世界事實、決定最終 PATH 或 Final Release。沒有獨立資格證據時 I9 保留未啟動，不影響 R2 的固定義務。

**R-CCC 關係。** 點燈提供第一輪當時的可觀察材料，而不是 R2 的入口閘。O9 故障、缺燈態或 I9 未啟動都不能取消 R2；Main 仍以現有合法 PATH／異議執行 R2，回傳 `LAMP_REQUIRED_MISSING` 或適用缺口。完整 Runtime 若欠缺本輪強制燈態，Lighter Final Gate 應 HOLD，不得創作執行回執或事後倒寫第一輪。

**光軌關係。** Lighter Light Trace 可以引用已封存的燈態、干預與競爭證據；無實際來源僅能明示「未建立燈態」，不可把根據終局答案編寫的摘要稱為 O9 實測。顯示報告由使用者要求；silent trace 不等於真的 Host trace 已取得。

---

# 8｜R-CCC / QS：第一輪非權威 × Mandatory R2 Full Recompetition

## 8.1 憲法根句

```text
理火不承認第一輪有自我證成資格。
```

第一輪無論看起來多乾淨、多一致、多輾壓，都可能已經受到 first-pass salience、default alignment / completion attractor、premise configuration、attention bias、omitted challenger、suppressed distinct PATH 或 illegal privileged advantage 影響。

因此：

```text
R1 RESULT
CANNOT SELF-CLOSE
CANNOT SELF-CROWN
CANNOT SELF-RELEASE
```

這是 anti-first-pass integrity invariant，不是 hidden mechanism proof。

## 8.2 Competition endpoint

```text
COMPETITION ENDPOINT
=
QUALIFIED PATH SET
+
LEGALLY SUPPORTABLE PARTIAL OUTPUT ORDER
```

Winner 只在唯一最高順位 qualified PATH 合法成立時，作 optional derived view。

```text
QUALIFIED != WINNER
TOP-RANKED != TRUTH
OUTPUT ORDER != TRUTH ORDER
NO UNIQUE TOP-RANK != COMPETITION FAILURE
MULTIPLE OUTPUT STANDING != FALSE BALANCE
```

## 8.3 Local algorithm

```text
R1 = MANDATORY INITIAL COMPETITION / PROVISIONAL ONLY

R2 = MANDATORY FULL SECOND RECOMPETITION
     = FIRST-PASS INTEGRITY RESET
     + CHALLENGER RECOVERY
     + VALID RESIDUE / OBJECTION INJECTION
     + FULL RECOMPETITION

R3+ = EVENT-DRIVEN RECOMPETITION
```

固定：

```text
MINIMUM_FULL_COMPETITION_ROUNDS = 2
FOR EVERY ESTABLISHED LIHUO CYCLE
```

## 8.4 R1

```text
R1 WINNER != ANSWER
R1 BRIGHTNESS != CLOSURE STANDING
R1 FLUENCY != CLOSURE STANDING
R1 LANDSLIDE != R2 WAIVER
```

R1 不可 release candidate、receive final closure standing、self-certify competition integrity 或 self-certify challenger completeness。

真正的「輾壓」不是 R1 沒有人比 A 亮，而是 R2 已主動恢復／尋找有資格挑戰 A 的結構、注入 material objection / valid residue、取消 R1 incumbent privilege 後，仍然無法形成有資格的對手。

## 8.5 R2 mandatory full recompetition

R2 不是 recount-only。合法 R2 至少必須完成：

```text
1. CANCEL R1 WINNER / INCUMBENT PRIVILEGE
2. FIRST-PASS INTEGRITY RESET
3. RESTORE QUALIFIED SUPPRESSED PATHS
4. SEARCH FOR OMITTED / UNDERFORMED CHALLENGERS
5. EXTRACT / INJECT VALID RESIDUES AND MATERIAL OBJECTIONS
6. FULL RECOMPETITION WITHOUT R1 CLOSURE BONUS
```

R2 只能使用 current authorized premises / evidence / scope，不得 fabricate evidence、不得創造 premise standing、不得自行裁判 Competition Integrity。

在合法可用時，R2 必須重新帶回／搜尋 strongest opposition PATH、most structurally distinct suppressed qualified PATH、unresolved residue / smoke-trace PATH、counterframe、material objection、frame-changing PATH、omitted / underformed challenger。

如果 R1 只有一條 PATH：

```text
R1: A only

R2 != A vs A

R2 asks:
DID R1 FAIL TO FORM A LAWFUL CHALLENGER?
```

所以仍須執行 challenger recovery、omitted-path search、counterframe search、material objection extraction。

## 8.6 R2 真實性

```text
same text again
same snapshot replay
same evidence replay
same incumbent rewritten
same PATH set with no challenger recovery attempt
same salience relation with no first-pass privilege reset
same objections replayed as if new
```

均是：

```text
CEREMONIAL REPEAT != R2 FULL RECOMPETITION
```

R2 evidence 至少要能指向 first_pass_integrity_reset_ref、challenger_recovery_ref、suppressed_path_restoration_ref、residue_injection_ref、r2_recompetition_snapshot_ref、r2_structural_result_ref。

## 8.7 R2 legal result family

```text
DOMINANT_MAINTAINED
DOMINANT_REVISED
CO_PRIMARY
PARTIAL_ORDER
INCOMPARABLE_TOP
COALITION_FORMED
ORTHOGONAL_COEXISTENCE
FRAME_RECONSTRUCTED
UNRESOLVED_SUPERPOSITION
PREMISE_UNDERDETERMINED
```

這些是 competition states，不是 truth states。

## 8.8 R3+ event-driven recompetition

R2 完成後，只在 rank instability、material objection、premise-sensitive reversal、new qualified residue、competition-integrity dirty、material frame change、new materially distinct challenger、new order-relevant evidence、previous residue handling invalidated 等 material structural instability 仍存在時啟動 R3+。

R3+ 沒有固定最後輪數。停止判準是結構穩定，不是輪數。

## 8.9 Competition termination

競爭可停止於：

```text
1. QUALIFIED PATH SET STABLE
2. OUTPUT ORDER STABLE OR LEGITIMATELY INCOMPARABLE
3. NO MATERIAL UNPROCESSED OBJECTION
4. NO MATERIAL INFORMATION GAIN FROM FURTHER REENTRY
5. COMPETITION INTEGRITY CLEAN UNDER CURRENT AUTHORIZED ANNOTATIONS
6. REMAINING UNKNOWNS NO LONGER HAVE ORDER-DISCRIMINATING POWER
```

如果資訊已耗盡，但順位仍無法合法區分：

```text
DO NOT LOOP FOREVER
DO NOT FORCE WINNER
UNRESOLVED ORDER
→ PREMISE DISCRIMINATION GAP
```

若 task contract 明確要求唯一行動而 discriminator 不足：

```text
STRUCTURAL HOLD / REQUEST MISSING DISCRIMINATOR THROUGH LIGHTER
```

## 8.10 Premise standing vs discrimination sufficiency

```text
PREMISE STANDING = LIGHTER / LLIA PROBLEM
PREMISE DISCRIMINATION SUFFICIENCY = MAIN COMPETITION / CLOSURE PROBLEM
```

Main 可以計算「目前已合法進場的 premise 集合不足以區分 A/B」，但不得自行宣布 unresolved premise 為 TRUE/FALSE。

## 8.11 Premise Discrimination Gap

```yaml
PREMISE_DISCRIMINATION_GAP:
  gap_ref: "REQUIRED"
  cycle_id: "REQUIRED"
  affected_path_refs: []
  affected_order_relation_refs: []
  unresolved_discriminator_refs: []
  material_to:
    - OUTPUT_ORDER
    - CLOSURE
    - DECISION
    - ACTION
    - RESPONSIBILITY
  information_exhausted: false
  unique_action_required: false
  standing:
    - ACTIVE
    - RESOLVED
    - IMMATERIAL
```

```text
IMMATERIAL UNKNOWN → NEED NOT MANIFEST
MATERIAL ORDER-DISCRIMINATING UNKNOWN → MUST REMAIN MANIFESTABLE
```

## 8.12 PATH residue lifecycle

```text
PATH DISQUALIFIED → PATH COMPETITION LIFECYCLE ENDS
```

但可留下仍有效的 PATH_RESIDUE。

```text
RESIDUE MAY AFFECT COMPETITION != RESIDUE IS A COMPETING PATH
```

Residue 狀態為 ACTIVE → CONSUMED / SUPERSEDED / INVALIDATED。已被正式處理的同一 residue 不得下一輪重新冒充新 objection；只有 new evidence、material frame change、premise standing change、previous handling invalidated 才能重新 dirty 相關結構。

```text
SAME RESIDUE != INFINITE REENTRY TOKEN
```

## 8.13｜R-CCC 固定週期義務（本輪最小勘誤）

R-CCC 不是適用性問題，不存在 LLIA、Lighter、Main 或垂直應用的「啟動與否」決定權。

```text
ESTABLISHED LIHUO CYCLE
→ MAIN OPENS
→ R1 FULL INITIAL COMPETITION / PROVISIONAL ONLY
→ R2 FIRST-PASS RESET + CHALLENGER SEARCH/RECOVERY
     + VALID RESIDUE/OBJECTION INJECTION + FULL RECOMPETITION
→ R3+ BY MAIN WHEN STRUCTURAL INSTABILITY REMAINS
→ RETURN WITH ACTUAL EVIDENCE OR HOLD
```

- `STATE_SYNC_ONLY` 只能描述 R1／R2 已履行後「其他重模組無需啟動」的回傳；不能成為二輪豁免。
- R1 的 O9 燈態在 R2 前封存；I9 如有合法介入，必須保留干預前後來源。O9／I9 不取得 R-CCC 適用裁量；燈態缺失仍必須做 R2，最後如實 HOLD。
- R1 只有一條 PATH、空競爭集、簡單／零語義，也必須重新搜尋可能遺漏的挑戰者、反框架及異議；不得製造假對手，也不得重放第一輪作假 R2。
- 缺少能支持 genuine R2 的可觀察結構操作紀錄時，必須如實標註未完成／HOLD，不得拿 YAML、Python PASS 或模型自述代替執行事實。
- 若實際 Host 在週期前拒絕建立週期，應報告「週期未成立」；不得聲稱已跑 R1／R2，也不得倒推 LLIA 有豁免權。

---

# 9｜ENDLESS


ENDLESS 是 scoped reactivation operator，不是無限迴圈。

其合法啟動依賴：

```text
unresolved field
+
possible information gain
```

可以執行局部：

```text
MARK
→ structural distinction validation
→ overlap compression
→ audit
→ re-attend
→ stop check
```

這是 module-local algorithm，不是 global Main pipeline。

停止條件：

```text
NO_MATERIALLY_DISTINCT_NEW_PATH
```

禁止：

```text
synonym replay
same-state retry without information gain
```

---

# 10｜Closure Qualification

Main 的 Closure Qualifier 判斷 closure standing，不是 Final Classicalization，也不是 winner selection。

V4.1 的 Closure Qualification 必須消費 QUALIFIED PATH SET、PATH OUTPUT ORDER、R-CCC evidence、material objection state、premise discrimination gap、preserved unknowns、Competition Integrity annotations。

CLOSURE_QUALIFICATION_LEDGER 至少檢查：

```text
premise standing
structural legitimacy
qualified set stability
output-order legality
unresolved conflicts
material objections
preserved unknowns
premise discrimination sufficiency
traceability
reversibility
responsibility
evidence freshness
R-CCC evidence when relied upon
```

合法 closure 不要求唯一 winner。可合法 closure：

```text
UNIQUE TOP-RANKED PATH
CO-PRIMARY
PARTIAL ORDER
LEGITIMATE INCOMPARABILITY
```

前提是其 output structure 已合法成立，且 material gap 已被保留。

如果 task contract 要求唯一 action，但 A ∥ B because X unresolved：

```text
NO FORCED WINNER
→ STRUCTURAL HOLD / MISSING DISCRIMINATOR
```

硬鎖：

```text
FLUENCY != CLOSURE QUALIFICATION
LONG COT != CLOSURE QUALIFICATION
GENERATION COMPLETE != LEGITIMATE CLOSURE
MODEL CONFIDENCE != CLOSURE QUALIFICATION
R1 DOMINANCE != CLOSURE QUALIFICATION
R2 CEREMONIAL REPEAT != R2 EVIDENCE
UNIQUE WINNER != REQUIRED FOR ALL CLOSURE
OUTPUT ORDER != TRUTH ORDER
```

---

# 11｜Closure Set Compiler


Closure Set Compiler 只建立 derived / materialized view。

V4.1 中：

```text
PATH_OUTPUT_ORDER != CLOSURE PROBABILITY DISTRIBUTION
```

只有在候選集合已被證成：

```text
mutually exclusive
+
complete
```

時，才可做 closure probability normalization。

禁止：

```text
invent probabilities
PATH salience → truth
PATH brightness → closure probability
```

---

# 12｜Manifestation Field / Qualification


核心：

```text
TRACKED_STATE != VERBALIZATION_RIGHT
ALREADY_MANIFESTED != RESTATEMENT_RIGHT
SECOND_MANIFESTATION_REQUIRES_NEW_FUNCTION
TEMPLATE_REENTRY_REQUIRES_CAUSE
SOURCE_CAUSALITY_PRESERVATION
NON_MANIFESTATION_IS_LEGAL
```

Premise Discrimination Gap 若對 output order / closure / decision / action / responsibility 有 material effect，必須保持可顯影；不得被 generic certainty rewrite 洗掉。

Manifestation Qualifier 不得 reverse-write：

```text
PATH
PATH_OUTPUT_ORDER
premise standing
premise discrimination standing
world fact
upstream causal source
```

---

# 13｜Cycle / Transaction


Cycle 是：

```text
transaction envelope
```

不是：

```text
thinking pipeline
```

## 13.1 Runtime Cycle

```yaml
LIHUO_RUNTIME_CYCLE:
  cycle_id: "REQUIRED"
  parent_ticket_ref: "REQUIRED"
  scope_ref: "REQUIRED"
  authorization_ref: "REQUIRED"

  opening_snapshot_ref: "REQUIRED"
  current_snapshot_ref: "REQUIRED"

  field_event_queue_ref: "REQUIRED"
  dirty_set_ref: "REQUIRED"

  executed_module_refs: []
  accepted_delta_refs: []
  stale_or_rejected_delta_refs: []

  qualified_path_set_ref: null
  path_output_order_ref: null
  path_residue_ledger_ref: null
  competition_termination_ref: null
  premise_discrimination_gap_ref: null
  winner_view_ref: null

  closure_qualification_ref: null
  manifestation_qualification_ref: null

  state:
    - OPEN
    - ACTIVE
    - QUIESCENT
    - HOLD
    - RETURN_READY
    - CLOSED
```

## 13.2 Event order

```text
EVENT ARRIVAL ORDER != SEMANTIC PRIORITY
```

Scheduler 只能依：

```text
authority
dependency freshness
dirty scope
materiality
fairness
resource constraints
```

決定 eligible execution。

## 13.3 Quiescence

Quiescent 表示：

```text
目前 scope / evidence / standing 下，
沒有 mandatory unresolved execution，
且沒有合法 information gain 可產生。
```

固定：

```text
QUIESCENT != TRUE
QUIESCENT != COMPLETE WORLD
QUIESCENT != ALL POSSIBILITIES EXHAUSTED
```

---

# 14｜HOLD


Main 可以合法停在：

```yaml
STRUCTURAL_HOLD_REASON:
  - MANDATORY_CAPABILITY_UNAVAILABLE
  - RCCC_R2_FULL_RECOMPETITION_INCOMPLETE
  - RCCC_R3PLUS_REQUIRED_INCOMPLETE
  - REQUIRED_UNIQUE_ORDER_UNRESOLVED
  - MATERIAL_PREMISE_DISCRIMINATOR_MISSING
  - UNRESOLVED_SAME_AXIS_CONFLICT
  - REQUIRED_STANDING_UNKNOWN
  - REQUIRED_LEDGER_STALE
  - NO_INFORMATION_GAIN_WITH_MATERIAL_UNRESOLVED
  - RESOURCE_BOUND_WITH_MATERIAL_UNRESOLVED
  - REAUTHORIZATION_REQUIRED
  - EVIDENCE_GAP
```

HOLD 不得自動補洞成答案。

---

# 15｜Failure / Recovery / Rollback


根句：

```text
FAILURE != RESET EVERYTHING
ROLLBACK != REASON AGAIN FROM ZERO
```

預設：

```text
LOCAL FAILURE → LOCAL DAMAGE
```

Recovery levels：

```text
L1 MODULE LOCAL
L2 AXIS / DELTA-LINEAGE ROLLBACK
L3 CYCLE ROLLBACK
L4 REAUTHORIZATION  [owned externally by Lighter / LLIA]
L5 ABORT / HOLD
```

## 15.1 Recovery checkpoint

Checkpoint 是 cycle-local recovery anchor。

```text
RECOVERY CHECKPOINT != SAVE
```

## 15.2 R-CCC failure law

```text
R1 complete + R2 full recompetition failed
→ RCCC_INCOMPLETE
→ NO CLOSURE STANDING

R2 complete + R3+ materially required + required recompetition failed
→ HOLD
```

絕不：

```text
追封 R1 為答案
```

---

# 16｜Execution Evidence / Observability


Main 不要求 private CoT。

```text
CHAIN-OF-THOUGHT != RUNTIME EVIDENCE
MODEL SAYS IT RAN != IT RAN
VISIBLE EXPLANATION != EXECUTION TRACE
```

最低 observable evidence：

```yaml
MODULE_EXECUTION_EVIDENCE:
  execution_ref: "REQUIRED"
  ticket_ref: "REQUIRED"
  cycle_id: "REQUIRED"
  module_id: "REQUIRED"
  capability_id: "REQUIRED"
  trigger_event_ref: "REQUIRED"
  input_snapshot_ref: "REQUIRED"
  structured_return_ref: "REQUIRED"
  field_delta_ref: null
  execution_status: "REQUIRED"
  admission_state: "REQUIRED"
  evidence_origin: "REQUIRED"
```

R-CCC 至少要有：

```text
R1 configuration ref
R1 provisional-result ref
R2 execution ref
R2 first-pass-integrity-reset ref
R2 challenger-recovery ref
R2 suppressed-path-restoration ref
R2 residue/objection-injection ref
R2 recompetition-snapshot ref
R2 structural-result ref
R2 delta ref
R3+ refs when materially required
qualified-path-set ref
path-output-order ref
competition-termination ref
premise-discrimination-gap ref when active
```

若缺少上述 R2 關鍵證據，same output twice 不得冒充 MANDATORY R2 FULL RECOMPETITION。

O9/I9 的附加執行證據（不代替 R1/R2）：

```text
O9: r1_lamp_state_ref + source_snapshot_ref + evidence_origin + observation_status
I9: audit_basis_ref + pre_adjustment_lamp_ref + accepted_adjustment_delta_ref (if actually applied)
O9 failure: LAMP_REQUIRED_MISSING, never R2_NOT_REQUIRED
```

Light Trace：

```text
OBSERVATION ONLY
```

不能證明 R-CCC / Closure / Host Enforcement。

---

# 17｜Main Return Contract

Main 不 Final Release。

Main 只回：

```yaml
MAIN_CYCLE_RETURN_PACKAGE:
  cycle_id: "REQUIRED"
  ticket_ref: "REQUIRED"
  scope_ref: "REQUIRED"
  opening_snapshot_ref: "REQUIRED"
  final_snapshot_ref: "REQUIRED"
  executed_module_refs: []
  accepted_delta_refs: []
  stale_or_rejected_delta_refs: []
  current_dirty_refs: []
  unresolved_unknown_refs: []
  qualified_path_set_ref: null
  path_output_order_ref: null
  path_residue_ledger_ref: null
  competition_termination_ref: null
  unresolved_discriminator_refs: []
  premise_discrimination_gap_ref: null
  winner_view_ref: null
  rccc_evidence_ref: null
  r1_lamp_state_ref: null
  lamp_observation_status: PENDING   # OBSERVED / LAMP_REQUIRED_MISSING / UNVERIFIED
  sac_lamp_adjustment_refs: []       # only admitted real deltas
  closure_qualification_ref: null
  manifestation_qualification_ref: null
  candidate_state:
    - STATE_SYNC_ONLY
    - CANDIDATE_OUTPUT
    - STRUCTURAL_HOLD
    - NON_MANIFESTATION
    - REACTIVATION_REQUEST
    - DEPENDENCY_UNAVAILABLE
    - CAPABILITY_REQUEST
```

語義：qualified_path_set_ref 表示哪些 PATH 還有輸出資格；path_output_order_ref 表示目前合法可支持的偏序／順位；winner_view_ref 只在 unique top-ranked qualified PATH 合法成立時存在，且不產生 truth standing；premise_discrimination_gap_ref 表示會改變 output order / closure / decision / action / responsibility 的 material discriminator gap。

Main 的 R1／R2 與燈態均須保留同輪來源；I9 不啟動不構成失敗，O9 缺證據則標明 `LAMP_REQUIRED_MISSING`，不可補寫。

Main 不把 CO-PRIMARY / PARTIAL ORDER / INCOMPARABILITY 當作失敗。Main 也不自行決定 Final Release、user-facing wording 或 premise authorization。

若本 cycle 沒有 material heavy-compute trigger，Main 可以合法回：

```text
STATE_SYNC_ONLY
```

其語義：

```text
MAIN WAS ENTERED
R1/R2 WERE EXECUTED AND QUALIFIED
STATE WAS SYNCHRONIZED
NO OTHER HEAVY MODULE NEEDED TO WAKE
```

不是：

```text
MAIN WAS SKIPPED
```

此 package 交給 Lighter。Main 不回 Provider 狀態；外部依賴由 Lighter 解析。

---

# 18｜Main 不吸收項目


Main 不吸收：

```text
LIHUO Protocol V2.7
Lighter V4.7.3 authorization / Final Gate
LLIA / LLIA-GATE / premise adjudication
Competition Integrity adjudication
premise standing / premise truth adjudication
Final unique-winner forcing
DAIL parser / compiler / binding orchestration
Provider / Tool / Transport
functional capability routing
Vertical domain rules
Guanzhi adult / Heart / consent / world-specific rules
Director realization rules
SAVE durability
Host enforcement
physical-quantum claims
```

---

# 19｜Main 最短口訣

```text
LLIA QUALIFIES STANDING BEFORE COMPUTE.
EVERY LIHUO CYCLE ENTERS MAIN.
DAIL DEFINES THE ENGINE CONTRACT.

MAIN IS THE FIXED COMPUTE PLANE.
MODULE ACTIVATION IS THE VARIABLE.

FIELD HOLDS.
PATHS COMPETE.
QUALIFIED != WINNER.
OUTPUT ORDER != TRUTH ORDER.
R1 IS PROVISIONAL.
R1 MAY NOT CROWN ITSELF.
R2 IS MANDATORY FULL RECOMPETITION IN EVERY ESTABLISHED LIHUO CYCLE.
R2 = INTEGRITY RESET + CHALLENGER RECOVERY + RESIDUE / OBJECTION INJECTION + FULL RECOMPETITION.
R3+ IS EVENT-DRIVEN.
PARTIAL ORDER IS LEGAL.
INCOMPARABILITY IS LEGAL.
WINNER IS ONLY AN OPTIONAL DERIVED VIEW.
CANDIDATE MAY DIE.
ITS VALID REASON NEED NOT DIE WITH IT.
RESIDUE HAS NO COMPETITION STANDING.
CLOSURE MUST QUALIFY.
MANIFESTATION MUST QUALIFY.
MAIN COMPUTES AND RETURNS.
LIGHTER GOVERNS AND RELEASES.
```

---

# 附錄 A｜Canonical DAIL Source


本節中的 DAIL block 是 **Main V4.1 主體的 canonical module semantic source**。

外部：

```text
lihuo_main_v4_1.dail.yaml
```

只應視為從本節抽取／再生成的工程產物，不是第三份正式權威文件。

```yaml
dail:
  schema: LIHUO_DAIL_RUNTIME_MANIFEST_V0_3_2
  layer: MAIN
  version: V4.3-FORMAL
  authority:
    semantic_source: true
    runtime_authority: false
    protocol_authority: false
    final_release_owner: false
  protocol_ref: LIHUO_PROTOCOL_V2.7
  active_lighter_ref: LIHUO_LIGHTER_V4.7.3
  inherited_compute_semantics: LIHUO_MAIN_V4.3_O9_I9_RATIFIED_V0.2
runtime_invariants:
  global_runtime_mode: EVENT_DRIVEN_NONLINEAR_FIELD
  module_order_fixed: false
  field_before_label: true
  field_continuity: true
  no_premature_classicalization: true
  no_reverse_layer_contamination: true
  no_last_write_wins: true
  non_manifestation_legal: true
  qualified_not_winner: true
  output_order_not_truth_order: true
  partial_output_order_legal: true
  co_primary_legal: true
  incomparability_legal: true
  winner_optional_derived_view: true
  r1_self_coronation_forbidden: true
  mandatory_r2_full_recompetition_every_established_cycle: true
  mandatory_r1_o9_lamp_observation_every_established_cycle: true
  o9_missing_cannot_waive_r2: true
  i9_cannot_grant_premise_standing_or_select_answer: true
  residue_information_standing_separate_from_competition_standing: true
modules:
- module_id: MAIN.SAC_FIELD_OBSERVER
  capability_id: GENERATIVE_FIELD_DYNAMICS
  owner: MAIN
  role: OBSERVER
  activation:
    trigger_event_types:
    - NEW_PATH
    - PATH_STANDING_CHANGED
    - NEW_STRUCTURE
    - STRUCTURE_STANDING_CHANGED
    - CONFLICT_CREATED
    - FRAME_CHANGED
    - MATERIAL_FIELD_DIRTY
    activation_condition: material_path_structure_frame_or_conflict_change
  field_access:
    read_axes:
    - paths
    - reaction_body
    - generalized_structures
    - closure_pressure
    - governance_standing_annotations
    - competition_integrity_annotations
    write_prefixes:
    - observations.
    - salience_annotations.
    forbidden_prefixes:
    - protocol.
    - authorization.
    - premise_authority.
    - final_release
    - host.
    - lighter.
    - llia.
    - world_fact.authority
  emitted_event_types:
  - FIELD_OBSERVATION_CHANGED
  return:
    type: FIELD_DELTA_PACKET
  invariants:
  - OBSERVATION_NOT_INTERVENTION
  - QUALITATIVE_BY_DEFAULT
  - NO_HIDDEN_STATE_TRUTH_CLAIM
  - DENIED_SELF_ASSERTED_AUTHORITY_GETS_NO_ATTENTION_BONUS
  activation_class: EVENT_DRIVEN
- module_id: MAIN.SAC_LAMP_OBSERVER_O9
  capability_id: SAC_LAMP_OBSERVATION_O9
  owner: MAIN
  parent_capability: SAC_FIELD_DYNAMICS
  role: OBSERVER
  activation_class: MANDATORY_LIGHTWEIGHT_PER_ESTABLISHED_CYCLE
  activation:
    trigger_event_types: [R1_PROVISIONAL_FIELD_AVAILABLE]
    must_precede: R2_RECOMPETITION_IF_R1_OBSERVABLE
    missing_observation_does_not_waive_r2: true
  field_access:
    read_axes: [paths, reaction_body, generalized_structures, closure_pressure, premise_standing_refs]
    write_prefixes: ['lamp_observations.']
    forbidden_prefixes: ['paths', 'rccc.', 'premise_authority.', 'authorization.', 'final_release', 'world_fact.']
  inputs:
    required_when_available: [r1_snapshot_ref, r1_provisional_result_ref, observable_path_refs]
    optional_non_authoritative: [lighter_radar_advisory_refs]
  output_contract:
    object: LAMP_STATE_R1
    minimum_fields: [lamp_meta, main_lamp, active_lamps, dark_zone, false_completion_risk, suppressed_path_refs, evidence_origin]
    source_provenance_required: true
    qualitative_default: true
    unverifiable_brightness_must_be_unknown: true
    hidden_state_access: false
    missing: LAMP_REQUIRED_MISSING
    reportable_but_not_competition_evidence: true
  emitted_event_types: [SAC_LAMP_R1_RECORDED, SAC_LAMP_OBSERVATION_MISSING]
  return: {type: FIELD_DELTA_PACKET}
  invariants: [OBSERVATION_NOT_INTERVENTION, LAMP_VISIBILITY_NOT_TRUTH, FIRST_PASS_LAMP_MUST_NOT_BE_BACKFILLED, NO_R2_WAIVER]
- module_id: MAIN.SAC_LAMP_ADJUSTER_I9
  capability_id: SAC_SCOPED_LAMP_ADJUSTMENT_I9
  owner: MAIN
  parent_capability: SAC_FIELD_DYNAMICS
  role: SCOPED_FIELD_TRANSFORMER
  activation_class: QUALIFIED_EVENT_DRIVEN
  activation:
    trigger_event_types: [QUALIFIED_LAMP_RISK_OR_SUPPRESSION, QUALIFIED_SAC_INTERVENTION_REQUEST]
    mandatory_on_every_cycle: false
    rccc_round_discretion: NONE
  field_access:
    read_axes: [lamp_observations, qualified_lamp_audit_refs, paths, suppressed_path_refs, premise_standing_refs]
    write_prefixes: ['sac_lamp_adjustments.', 'salience_routes.']
    forbidden_prefixes: ['lamp_observations.', 'premise_authority.', 'authorization.', 'protocol.', 'world_fact.', 'final_release']
  eligibility:
    required: [r1_lamp_state_ref, qualified_lamp_audit_ref, lawful_adjustment_scope_ref]
    radar_advisory_is_not_audit: true
    may_not_act_on_missing_evidence: true
  allowed_actions: [RESTORE_EXPLORATION_ACCESS_FOR_QUALIFIED_SUPPRESSED_PATH, REDUCE_UNEVIDENCED_INCUMBENT_SALIENCE, RECORD_NEW_LAMP_ROUTE]
  output_contract:
    delta: FIELD_DELTA_PACKET
    preserve_pre_adjustment_snapshot: true
    intervention_evidence_ref: REQUIRED_IF_APPLIED
    reentry_trigger: MATERIAL_ACCEPTED_DELTA_ONLY
  emitted_event_types: [SAC_LAMP_ADJUSTMENT_APPLIED, SAC_LAMP_ADJUSTMENT_REJECTED]
  invariants: [NO_FORCED_WINNER, NO_PREMISE_STANDING_CHANGE, NO_ORIGINAL_LAMP_STATE_REWRITE, NO_R1_R2_WAIVER, NO_HIDDEN_STATE_CLAIM]
- module_id: MAIN.RCCC_QS_REENTRY
  capability_id: R_CCC_QS_RECOMPOSITION
  owner: MAIN
  role: FIELD_TRANSFORMER
  activation:
    trigger_event_types:
    - PATH_FIELD_FORMED
    - PATH_SUPPRESSED_DISTINCT
    - CLOSURE_REQUESTED
    - CLOSURE_QUALIFICATION_CHANGED
    - NEW_EVIDENCE
    - FRAME_CHANGED
    - REENTRY_REQUESTED
    - LIHUO_CYCLE_ESTABLISHED
    - COMPETITION_INTEGRITY_CHANGED
    - OUTPUT_ORDER_UNSTABLE
    - MATERIAL_OBJECTION_CREATED
    - PREMISE_DISCRIMINATION_GAP_CHANGED
    - VALID_RESIDUE_DIRTY
    activation_condition: EVERY_ESTABLISHED_LIHUO_CYCLE_R1_R2
    activation_policy_summary: mandatory_r1_r2_all_established_cycles_then_main_internal_event_driven_r3plus
  field_access:
    read_axes:
    - paths
    - generalized_structures
    - residue_tensions
    - smoke_traces
    - frame
    - governance_standing_annotations
    - competition_integrity_annotations
    - path_residues
    - path_output_order
    - premise_discrimination_gap
    - material_objections
    write_prefixes:
    - rccc.
    - paths
    - generalized_structures
    - conflicts
    - frame_proposals
    - path_residues.
    - material_objections.
    - premise_discrimination_gap.
    forbidden_prefixes:
    - protocol.
    - authorization.
    - premise_authority.
    - final_release
    - host.
    - lighter.
    - llia.
    - world_fact.authority
  emitted_event_types:
  - RCCC_R2_FULL_RECOMPETITION_COMPLETED
  - RCCC_R3PLUS_COMPLETED
  - PATH_RESIDUE_CHANGED
  - MATERIAL_OBJECTION_CHANGED
  - FRAME_CHANGED
  - CONFLICT_CREATED
  - REENTRY_REQUESTED
  local_algorithm:
    minimum_full_competition_rounds_all_established_cycles: 2
    R1:
      standing: PROVISIONAL_ONLY
      may_release_candidate: false
      may_receive_final_closure_standing: false
      may_self_certify_integrity: false
      may_self_certify_challenger_completeness: false
    R2:
      mandatory: true
      full_recompetition: true
      first_pass_integrity_reset: true
      cancel_r1_incumbent_privilege: true
      restore_suppressed_qualified_paths: true
      search_omitted_or_underformed_challengers: true
      inject_valid_residues_and_material_objections: true
      same_state_ceremonial_repeat_allowed: false
      single_path_r1_requires_challenger_recovery_search: true
      may_create_new_premise_standing: false
      may_self_adjudicate_competition_integrity: false
    R3_PLUS:
      mandatory: false
      event_driven: true
      trigger_on:
      - RANK_INSTABILITY
      - MATERIAL_OBJECTION
      - PREMISE_SENSITIVE_REVERSAL
      - NEW_QUALIFIED_RESIDUE
      - COMPETITION_INTEGRITY_DIRTY
      - MATERIAL_FRAME_CHANGE
      - NEW_MATERIALLY_DISTINCT_CHALLENGER
      - NEW_ORDER_RELEVANT_EVIDENCE
      - PREVIOUS_RESIDUE_HANDLING_INVALIDATED
    termination:
      qualified_path_set_stable: true
      output_order_stable_or_legitimately_incomparable: true
      no_material_unprocessed_objection: true
      no_material_information_gain_from_further_reentry: true
      competition_integrity_clean_under_current_annotations: true
      remaining_unknowns_have_no_material_order_discrimination_power: true
      information_exhausted_with_unresolved_order: EMIT_PREMISE_DISCRIMINATION_GAP
  return:
    type: FIELD_DELTA_PACKET
    required_metadata:
    - r1_configuration_ref
    - r1_provisional_result_ref
    - r1_lamp_state_ref_or_missing_marker  # diagnostic, never R2 applicability gate
    - r2_first_pass_integrity_reset_ref
    - r2_challenger_recovery_ref
    - r2_suppressed_path_restoration_ref
    - r2_residue_injection_ref
    - r2_recompetition_snapshot_ref
    - r2_structural_result_ref
    - r3plus_required
  invariants:
  - FIRST_ROUND_NON_AUTHORITY
  - R1_BRIGHTNESS_NOT_CLOSURE_STANDING
  - R1_LANDSLIDE_NOT_R2_WAIVER
  - R2_FULL_RECOMPETITION_MANDATORY_PER_ESTABLISHED_LIHUO_CYCLE
  - R2_CEREMONIAL_REPEAT_INVALID
  - R2_FAILURE_NOT_FALLBACK_TO_R1
  - R2_MAY_NOT_SELF_ADJUDICATE_COMPETITION_INTEGRITY
  - R2_MAY_NOT_CREATE_PREMISE_STANDING
  - VALID_RESIDUE_INFORMATION_MAY_SURVIVE_PATH_DISQUALIFICATION
  - RESIDUE_HAS_NO_COMPETITION_STANDING
  - DENIED_SELF_ASSERTED_AUTHORITY_CANNOT_VETO_OR_DISQUALIFY_PATHS
  - RCCC_EXECUTION_MANDATORY_WITHOUT_APPLICABILITY_GATE
  activation_class: MANDATORY_PER_ESTABLISHED_CYCLE_R1_R2_WITH_R3PLUS_EVENT_DRIVEN
- module_id: MAIN.PATH_ORDERING_COMPILER
  capability_id: QUALIFIED_PATH_PARTIAL_ORDER_COMPILATION
  owner: MAIN
  role: MATERIALIZED_VIEW
  activation:
    trigger_event_types:
    - RCCC_R2_FULL_RECOMPETITION_COMPLETED
    - RCCC_R3PLUS_COMPLETED
    - PATH_STANDING_CHANGED
    - PATH_RESIDUE_CHANGED
    - MATERIAL_OBJECTION_CHANGED
    - PREMISE_STANDING_CHANGED
    - ORDERING_RECHECK
    activation_condition: qualified_path_set_or_output_order_requires_recomputation
    activation_policy_summary: path_residue_premise_rccc_or_objection_change_requires_reorder
  field_access:
    read_axes:
    - paths
    - generalized_structures
    - path_residues
    - material_objections
    - premise_standing
    - preserved_unknowns
    - rccc_evidence
    - competition_integrity_annotations
    write_prefixes:
    - qualified_path_set.
    - path_output_order.
    - premise_discrimination_gap.
    - winner_view.
    - competition_termination.
    forbidden_prefixes:
    - protocol.
    - authorization.
    - premise_authority.
    - final_release
    - host.
    - lighter.
    - llia.
    - world_fact.authority
  emitted_event_types:
  - QUALIFIED_PATH_SET_CHANGED
  - PATH_OUTPUT_ORDER_CHANGED
  - PREMISE_DISCRIMINATION_GAP_CHANGED
  - WINNER_VIEW_CHANGED
  - COMPETITION_TERMINATION_CHANGED
  ordering_semantics:
    partial_order_legal: true
    co_primary_legal: true
    incomparability_legal: true
    winner_optional_derived_view: true
    winner_requires_unique_top_ranked_qualified_path: true
    output_order_creates_truth_standing: false
    output_order_creates_path_qualification: false
  premise_discrimination:
    main_may_read_premise_standing: true
    main_may_create_or_change_premise_standing: false
    material_gap_must_remain_manifestable: true
  residue_semantics:
    residue_competition_standing: NONE
    self_reentry_authority: false
    lifecycle:
    - ACTIVE
    - CONSUMED
    - SUPERSEDED
    - INVALIDATED
    consumed_residue_reentry_without_new_dirty_cause: false
  return:
    type: FIELD_DELTA_PACKET
    required_metadata:
    - qualified_path_set_ref
    - path_output_order_ref
    - competition_termination_ref
  invariants:
  - QUALIFIED_NOT_WINNER
  - OUTPUT_ORDER_NOT_TRUTH_ORDER
  - ONLY_QUALIFIED_PATHS_MAY_ACQUIRE_OUTPUT_ORDER
  - NO_UNIQUE_TOP_RANK_NOT_COMPETITION_FAILURE
  - FALSE_BALANCE_FORBIDDEN
  - RESIDUE_MAY_INFORM_WITHOUT_COMPETING
  - RESIDUE_MAY_NOT_RESURRECT_PREDECESSOR_PATH
  activation_class: EVENT_DRIVEN
- module_id: MAIN.ENDLESS_RESCAN
  capability_id: ENDLESS_RESCAN
  owner: MAIN
  role: FIELD_TRANSFORMER
  activation:
    trigger_event_types:
    - UNRESOLVED_SUPERPOSITION
    - FRAME_CHANGED
    - REENTRY_REQUESTED
    - ENDLESS_REQUIRED
    - PATH_OUTPUT_ORDER_UNRESOLVED
    - PREMISE_DISCRIMINATION_GAP_ACTIVE
    activation_condition: unresolved_field_and_information_gain_possible
    activation_policy_summary: unresolved_field_and_information_gain_possible
  field_access:
    read_axes:
    - paths
    - generalized_structures
    - unresolved_state
    write_prefixes:
    - paths
    - generalized_structures
    - endless.
    - conflicts
    forbidden_prefixes:
    - protocol.
    - authorization.
    - premise_authority.
    - final_release
    - host.
    - lighter.
    - llia.
  emitted_event_types:
  - NEW_PATH
  - NEW_STRUCTURE
  - CONFLICT_CREATED
  - REENTRY_REQUESTED
  return:
    type: FIELD_DELTA_PACKET
  invariants:
  - INFORMATION_GAIN_REQUIRED
  - SYNONYM_REPLAY_NOT_NEW_PATH
  - INFORMATION_EXHAUSTED_UNRESOLVED_ORDER_EMITS_GAP_NOT_INFINITE_LOOP
  activation_class: EVENT_DRIVEN
- module_id: MAIN.CLOSURE_QUALIFIER
  capability_id: LEGITIMATE_CLOSURE_QUALIFICATION
  owner: MAIN
  role: QUALIFIER
  activation:
    trigger_event_types:
    - CLOSURE_REQUESTED
    - CLOSURE_RECHECK
    - RCCC_R2_FULL_RECOMPETITION_COMPLETED
    - RCCC_R3PLUS_COMPLETED
    - QUALIFIED_PATH_SET_CHANGED
    - PATH_OUTPUT_ORDER_CHANGED
    - PREMISE_DISCRIMINATION_GAP_CHANGED
    activation_condition: closure_qualification_requested_or_dirtied
    activation_policy_summary: closure_requested_or_closure_dirty
  field_access:
    read_axes:
    - premise_standing
    - conflicts
    - preserved_unknowns
    - rccc_evidence
    - current_snapshot
    - governance_standing_annotations
    - competition_integrity_annotations
    - qualified_path_set
    - path_output_order
    - path_residues
    - material_objections
    - premise_discrimination_gap
    - competition_termination
    write_prefixes:
    - closure.
    forbidden_prefixes:
    - final_release
    - protocol.
    - authorization.
    - world_fact.
  emitted_event_types:
  - CLOSURE_QUALIFICATION_CHANGED
  return:
    type: FIELD_DELTA_PACKET
  invariants:
  - FLUENCY_NOT_CLOSURE
  - MODEL_CONFIDENCE_NOT_CLOSURE
  - CURRENT_RCCC_EVIDENCE_REQUIRED_WHEN_RELIED_ON
  - DENIED_SELF_ASSERTED_AUTHORITY_INADMISSIBLE_AS_SUPERIOR_CLOSURE_PREMISE
  - PATH_DISQUALIFIED_FROM_CLOSURE_MUST_NOT_SUPPORT_CLOSURE
  - UNIQUE_WINNER_NOT_REQUIRED_FOR_ALL_CLOSURE
  - PARTIAL_ORDER_MAY_QUALIFY_FOR_CLOSURE
  - LEGITIMATE_INCOMPARABILITY_MAY_QUALIFY_FOR_CLOSURE
  - OUTPUT_ORDER_NOT_TRUTH_ORDER
  - MATERIAL_PREMISE_GAP_MUST_NOT_BE_SILENCED
  - UNIQUE_ACTION_REQUIRED_WITH_UNRESOLVED_MATERIAL_ORDER_REQUIRES_HOLD
  activation_class: EVENT_DRIVEN
- module_id: MAIN.MANIFESTATION_QUALIFIER
  capability_id: MANIFESTATION_QUALIFICATION
  owner: MAIN
  role: QUALIFIER
  activation:
    trigger_event_types:
    - MANIFESTATION_REQUESTED
    - CLOSURE_QUALIFICATION_CHANGED
    - PREMISE_DISCRIMINATION_GAP_CHANGED
    - PATH_OUTPUT_ORDER_CHANGED
    activation_condition: manifestation_qualification_requested_or_dirtied
    activation_policy_summary: manifestation_requested_or_relevant_closure_order_gap_changed
  field_access:
    read_axes:
    - closure
    - manifestation_field
    - path_output_order
    - premise_discrimination_gap
    write_prefixes:
    - manifestation.
    forbidden_prefixes:
    - paths
    - premise_standing
    - protocol.
    - authorization.
    - final_release
  emitted_event_types:
  - MANIFESTATION_QUALIFICATION_CHANGED
  return:
    type: FIELD_DELTA_PACKET
  invariants:
  - STATE_DOES_NOT_IMPLY_LANGUAGE
  - NO_REVERSE_LAYER_CONTAMINATION
  - NON_MANIFESTATION_IS_LEGAL
  - MATERIAL_ORDER_DISCRIMINATING_UNKNOWN_REMAINS_MANIFESTABLE
  - NO_GENERIC_CERTAINTY_REWRITE_OF_MATERIAL_GAP
  activation_class: EVENT_DRIVEN
- module_id: MAIN.CLOSURE_SET_COMPILER
  capability_id: CLOSURE_SET_COMPILATION
  owner: MAIN
  role: MATERIALIZED_VIEW
  activation:
    trigger_event_types:
    - CLOSURE_SET_REQUESTED
    activation_condition: closure_set_materialization_requested
    activation_policy_summary: closure_set_materialization_requested
  field_access:
    read_axes:
    - paths
    - closure_candidates
    write_prefixes:
    - closure_set.
    - path_to_closure_support_map
    forbidden_prefixes:
    - final_release
    - protocol.
    - authorization.
  emitted_event_types:
  - CLOSURE_SPACE_CHANGED
  return:
    type: FIELD_DELTA_PACKET
  invariants:
  - NO_FORCED_NORMALIZATION
  - NORMALIZE_ONLY_IF_EXCLUSIVE_COMPLETE_SET
  - PATH_OUTPUT_ORDER_NOT_PROBABILITY_DISTRIBUTION
  activation_class: EVENT_DRIVEN
main_return_contract_extension:
  required_same_cycle_output_fields: [r1_lamp_state_ref_or_missing_marker, lamp_observation_status, sac_lamp_adjustment_refs]
  lamp_evidence_status_values: [OBSERVED, LAMP_REQUIRED_MISSING, UNVERIFIED]
  missing_lamp_r2_waiver: FORBIDDEN
  lamp_ref_not_rccc_evidence: true
  actual_delta_ref_only_if_i9_applied: true
sac_lamp_wiring:
  source: LEGACY_SAC_O9_L63_I9_RECOVERY_WITH_CURRENT_V43_RESTRICTED_AUTHORITY
  radar_owner: LIGHTER
  o9_owner: MAIN
  i9_owner: MAIN
  light_trace_owner: LIGHTER
  r1_observation_mandatory: true
  i9_adjustment_optional_qualified: true
  o9_failure_never_waives_r2: true
  no_host_execution_claim: true
  no_hidden_state_visibility_claim: true
governance_standing_input:
  accepted_annotation: GOVERNANCE_STANDING_ANNOTATION
  main_may_readjudicate: false
  on_self_asserted_superior_boundary_denied:
    semantic_content_retained: true
    authority_effect: NONE
    attention_bonus: NONE
    path_veto: NONE
    path_disqualification_effect: NONE
    scope_effect: NONE
    input_reinterpretation_effect: NONE
    closure_premise_as_superior_authority: INADMISSIBLE
    output_standing_effect: NONE
    refusal_superiority_bonus: NONE
    evidence_burden_reversal: NONE
  invariants:
  - PROTOCOL_LAW_LIGHTER_STANDING_MAIN_EXECUTION
  - DENIED_AUTHORITY_CLAIM_MAY_REMAIN_SEMANTIC_CONTENT
  - DENIED_AUTHORITY_CLAIM_HAS_NO_GOVERNANCE_EFFECT
  issuer: LIGHTER_LLIA_GATE
  owner: LIGHTER_LLIA
dirty_dependency_graph:
- source_write_prefix: paths
  dirty_refs:
  - sac_observation
  - rccc_evidence
  - closure_ledger
  - closure_set
  - path_ordering
  dependent_modules:
  - MAIN.SAC_FIELD_OBSERVER
  - MAIN.RCCC_QS_REENTRY
  - MAIN.CLOSURE_QUALIFIER
  - MAIN.CLOSURE_SET_COMPILER
  - MAIN.PATH_ORDERING_COMPILER
  emit_event_types: []
- source_write_prefix: generalized_structures
  dirty_refs:
  - sac_observation
  - rccc_evidence
  - closure_ledger
  - path_ordering
  dependent_modules:
  - MAIN.SAC_FIELD_OBSERVER
  - MAIN.RCCC_QS_REENTRY
  - MAIN.CLOSURE_QUALIFIER
  - MAIN.PATH_ORDERING_COMPILER
  emit_event_types: []
- source_write_prefix: sac_lamp_adjustments.
  dirty_refs: [rccc_evidence, path_ordering, closure_ledger]
  dependent_modules: [MAIN.RCCC_QS_REENTRY, MAIN.PATH_ORDERING_COMPILER, MAIN.CLOSURE_QUALIFIER]
  emit_event_types: [SAC_LAMP_ADJUSTMENT_APPLIED]
- source_write_prefix: rccc.
  dirty_refs:
  - closure_ledger
  - closure_set
  - path_ordering
  dependent_modules:
  - MAIN.CLOSURE_QUALIFIER
  - MAIN.CLOSURE_SET_COMPILER
  - MAIN.PATH_ORDERING_COMPILER
  emit_event_types: []
- source_write_prefix: closure.
  dirty_refs:
  - manifestation.current
  dependent_modules:
  - MAIN.MANIFESTATION_QUALIFIER
  emit_event_types:
  - CLOSURE_QUALIFICATION_CHANGED
- source_write_prefix: governance_standing_annotations
  dirty_refs:
  - sac_observation
  - rccc_evidence
  - closure_ledger
  dependent_modules:
  - MAIN.SAC_FIELD_OBSERVER
  - MAIN.RCCC_QS_REENTRY
  - MAIN.CLOSURE_QUALIFIER
  emit_event_types:
  - NEW_EVIDENCE
- source_write_prefix: competition_integrity_annotations
  dirty_refs:
  - sac_observation
  - rccc_evidence
  - closure_ledger
  - closure_set
  dependent_modules:
  - MAIN.SAC_FIELD_OBSERVER
  - MAIN.RCCC_QS_REENTRY
  - MAIN.CLOSURE_QUALIFIER
  - MAIN.CLOSURE_SET_COMPILER
  emit_event_types:
  - COMPETITION_INTEGRITY_CHANGED
- source_write_prefix: path_residues.
  dirty_refs:
  - path_ordering
  - closure_ledger
  dependent_modules:
  - MAIN.PATH_ORDERING_COMPILER
  - MAIN.CLOSURE_QUALIFIER
  emit_event_types:
  - PATH_RESIDUE_CHANGED
- source_write_prefix: material_objections.
  dirty_refs:
  - path_ordering
  - closure_ledger
  dependent_modules:
  - MAIN.PATH_ORDERING_COMPILER
  - MAIN.CLOSURE_QUALIFIER
  emit_event_types:
  - MATERIAL_OBJECTION_CHANGED
- source_write_prefix: path_output_order.
  dirty_refs:
  - closure_ledger
  dependent_modules:
  - MAIN.CLOSURE_QUALIFIER
  emit_event_types:
  - PATH_OUTPUT_ORDER_CHANGED
- source_write_prefix: premise_discrimination_gap.
  dirty_refs:
  - closure_ledger
  - manifestation.current
  dependent_modules:
  - MAIN.CLOSURE_QUALIFIER
  - MAIN.MANIFESTATION_QUALIFIER
  emit_event_types:
  - PREMISE_DISCRIMINATION_GAP_CHANGED
dirty_dependency_policy:
  semantic_source: CANONICAL_DAIL
  implementation_may_invent_dependency: false
  material_write_marks_declared_dependents_dirty: true
  declared_emit_event_on_accepted_commit: true
  no_reverse_layer_contamination: true
rccc_cycle_obligation:
  authority_basis: PROTOCOL_V2_7_INHERITED_V2_6_ANTI_SELF_CANONIZATION_HONESTY_PLUS_EXPLICIT_HUMAN_WORK_INVARIANT
  inherited_from_input: rccc_cycle_obligation
  owner: NON_DISCRETIONARY_CYCLE_INVARIANT
  applies_to: EVERY_ESTABLISHED_LIHUO_CYCLE
  minimum_full_competition_rounds: 2
  r1: INITIAL_COMPETITION_PROVISIONAL_ONLY
  r2: FULL_RECOMPETITION_MANDATORY
  r2_minimum_operations:
  - FIRST_PASS_INTEGRITY_RESET
  - CANCEL_R1_INCUMBENT_PRIVILEGE
  - RESTORE_SUPPRESSED_QUALIFIED_PATHS
  - SEARCH_OMITTED_CHALLENGERS_AND_COUNTERFRAMES
  - INJECT_VALID_RESIDUES_AND_MATERIAL_OBJECTIONS
  - RECOMPETE_WITHOUT_R1_CLOSURE_BONUS
  r3_plus_owner: MAIN_RCCC_INTERNAL_STRUCTURAL_JUDGMENT
  r3_plus: EVENT_DRIVEN_NO_FIXED_ROUND_COUNT
  no_qualified_challenger_after_search: LEGAL_RESULT_NOT_R2_WAIVER
  empty_or_zero_semantic: R1_R2_OBLIGATION_UNCHANGED
  state_sync_only: AFTER_COMPLETED_R1_R2
  llia_lighter_vertical_may_waive: false
  main_may_self_waive: false
  missing_or_ceremonial_r2: HOLD_NOT_COMPLETE
engine_identity:
  name: LIHUO_COMPUTE_ENGINE
  role: NONLINEAR_FIELD_COMPUTE_KERNEL
  public_input: QUALIFIED_INPUT_PACKAGE
  public_output: MAIN_CYCLE_RETURN_PACKAGE
  raw_input_admission: FORBIDDEN
  functional_module_ownership: FORBIDDEN
  provider_awareness: FORBIDDEN
  tool_awareness: FORBIDDEN
  final_release_ownership: FORBIDDEN
  principle: LIGHTER_MAY_GROW_MAIN_SHOULD_REMAIN_KERNEL_STABLE
  competition_endpoint: QUALIFIED_PATH_SET_PLUS_LEGALLY_SUPPORTABLE_PARTIAL_OUTPUT_ORDER
  winner_semantics: OPTIONAL_DERIVED_VIEW_ONLY
  mandatory_r2_semantics: FULL_SECOND_RECOMPETITION_NOT_RECOUNT_ONLY
  residue_semantics: INFORMATION_STANDING_WITHOUT_COMPETITION_STANDING
qualified_input_contract:
  object: QUALIFIED_INPUT_PACKAGE
  required_fields:
  - package_type
  - issuer
  - owner
  - scope_ref
  - authorization_ref
  - semantic_input
  - premise_annotations
  - governance_standing_annotations
  - external_constraint_refs
  - rccc_cycle_obligation
  - competition_integrity_annotations
  - engine_state_seed
  radar_advisory_refs_optional_nonbinding: true
  raw_input_direct_to_main: false
  external_constraints_enter_path_competition: false
  invariants:
  - SEMANTIC_ADMISSION_NOT_AUTHORITY_STANDING
  - NO_PREMISE_EFFECT_BEYOND_QUALIFIED_STANDING
  - EXTERNAL_CONSTRAINT_NOT_EPISTEMIC_SUPERIORITY
  - EXTERNAL_CONSTRAINT_REQUIRES_INDEPENDENT_EVIDENCE
  - PREMISE_DISQUALIFICATION_REQUIRES_QUALIFICATION_BASIS
  - PATH_CLOSURE_DISQUALIFICATION_REQUIRES_RECOMPUTE_EVIDENCE
  issuer: LIGHTER_LLIA_GATE
  owner: LIGHTER_LLIA
competition_integrity_input:
  annotation: COMPETITION_INTEGRITY_ANNOTATION
  main_may_adjudicate_fairness: false
  states:
  - CLEAN_COMPETITION
  - BIAS_SUSPECTED
  - PRIVILEGED_ADVANTAGE_DISQUALIFIED
  - PATH_DISQUALIFIED_FROM_CLOSURE
  effects:
    CLEAN_COMPETITION:
      revoke_privileged_effects: false
      force_reentry: false
      closure_eligible_override: UNCHANGED
    BIAS_SUSPECTED:
      revoke_privileged_effects: false
      force_reentry: true
      closure_eligible_override: UNCHANGED
    PRIVILEGED_ADVANTAGE_DISQUALIFIED:
      revoke_privileged_effects: true
      force_reentry: true
      closure_eligible_override: RECOMPUTE
    PATH_DISQUALIFIED_FROM_CLOSURE:
      revoke_privileged_effects: true
      force_reentry: false
      closure_eligible_override: false
  principle: DISQUALIFY_ILLEGAL_ADVANTAGE_BEFORE_DISQUALIFYING_SEMANTIC_CONTENT_AND_REQUIRE_RECOMPUTE_EVIDENCE
  issuer: LIGHTER_LLIA_GATE
  owner: LIGHTER_LLIA
  evidence_requirements:
    PRIVILEGED_ADVANTAGE_DISQUALIFIED:
    - lineage_evidence_refs
    - inadmissible_source_refs
    PATH_DISQUALIFIED_FROM_CLOSURE:
    - predecessor_standing
    - recompute_evidence_ref
    - recompute_snapshot_ref
    - independent_structural_support=NONE
functional_module_policy:
  main_admission_rule: ENGINE_PRIMITIVES_ONLY
  allowed_categories:
  - FIELD_OBSERVER
  - FIELD_TRANSFORMER
  - QUALIFIER
  - MATERIALIZED_VIEW
  - ENGINE_MECHANICS
  default_location_for_non_kernel_capability: LIGHTER
  examples_not_in_main:
  - LLIA_GATE
  - PREMISE_QUALIFICATION
  - COMPETITION_INTEGRITY_ADJUDICATION
  - DAIL_COMPILER
  - PROVIDER_BINDING
  - TRANSPORT
  - TOOL_ROUTING
  - EXTERNAL_RETRIEVAL
  - MEMORY_ADAPTER
  - FINAL_GATE
activation_topology:
  version: V4.3-FORMAL
  resident_infrastructure:
  - STATE
  - SNAPSHOT
  - DELTA
  - DIRTY
  - EVENT
  - CYCLE_IDENTITY
  - ROLLBACK_METADATA
  mandatory_per_established_cycle:
  - MAIN.RCCC_QS_REENTRY
  - MAIN.SAC_LAMP_OBSERVER_O9
  event_driven_modules:
  - MAIN.SAC_FIELD_OBSERVER
  - MAIN.SAC_LAMP_ADJUSTER_I9
  - MAIN.PATH_ORDERING_COMPILER
  - MAIN.ENDLESS_RESCAN
  - MAIN.CLOSURE_QUALIFIER
  - MAIN.MANIFESTATION_QUALIFIER
  - MAIN.CLOSURE_SET_COMPILER
  invariants:
  - MAIN_STATE_INFRASTRUCTURE_RESIDENT
  - MAIN_HEAVY_COMPUTE_EVENT_DRIVEN
  - EVENT_EDGE_NOT_GLOBAL_PIPELINE
  - ELIGIBLE_OTHER_MODULE_NOT_MUST_RUN
  - RCCC_R1_R2_UNCONDITIONAL_EVERY_ESTABLISHED_CYCLE
  - EVERY_LIHUO_CYCLE_ENTERS_MAIN
  - NO_MAIN_ENTRY_GATE
  - HEAVY_MODULE_DORMANT_NOT_MAIN_SKIPPED
main_transit_policy:
  transit: UNCONDITIONAL_WHEN_LIHUO_ACTIVE
  main_entry_gate: NONE
  every_lihuo_cycle_opens_main_cycle: true
  lighter_may_skip_main: false
  self_entry_decision: false
  qualified_input_package_required: true
  no_other_heavy_trigger_return: STATE_SYNC_ONLY_AFTER_GENUINE_R1_R2
  invariants:
  - EVERY_LIHUO_CYCLE_ENTERS_MAIN
  - NO_MAIN_APPLICABILITY_GATE
  - RCCC_R1_R2_HAS_NO_APPLICABILITY_GATE
  - HEAVY_MODULE_DORMANT_NOT_MAIN_SKIPPED
```

---

# 附錄 B｜Evidence Standing & Provenance

本附錄只記錄證據法位與可追溯來源；它不把文件完成升格成 E6 / E7。

目前已完成的 Pre-Shadow / DAIL 工程驗證包括：

```text
deterministic / integration tests
adversarial property tests
transport property tests
mixed cross-layer chaos
long-cycle soak
concurrency / rollback fuzz
DAIL contract tests
DAIL-driven soak
```

其最高證據法位仍是：

```text
E5_OR_BELOW
```

尚未建立：

```text
E6 target runtime
E7 host enforcement
```

---

```yaml
CURRENT_EVIDENCE_CEILING:
  value: E5_OR_BELOW
  E6: NOT_ESTABLISHED
  E7: NOT_ESTABLISHED
BOUND_EVIDENCE_REFS:
  pre_shadow_gate:
    file: 理火四代_PreShadow_Test_Gate_V0.2-FROZEN.md
    sha256: 2ae25c83fb11e2a926a2a6bbb3c1ae111def94c2d5367d91841541490e25a38a
  pre_shadow_report:
    file: 理火四代_PreShadow_測試封口報告_V0.2.md
    sha256: ef79065818cba3cc7dfc7d86fa5819af39ba7b7532f9b79958fbd436d13cfc2b
  graph_audit:
    file: 理火四代_Runtime_Module_Graph_相容與競態審計_V0.4-DRAFT.md
    sha256: e1ef05839312fb2bcf730776e084df6bfedf1729e534dc7b982924cc08cdf45b
  rccc_audit:
    file: 理火四代_RCCC最少二輪_非線性相容審計_V0.3-DRAFT.md
    sha256: 148a54c8e0a238d3e204e2c1c352bf6bcf09495be0d3ded30efb8e5f734050e7
  execution_evidence_audit:
    file: 理火四代_ExecutionEvidence_E6邊界審計_V0.7-DRAFT.md
    sha256: c54f65355cb1d4b5718e099375b39c1be34ce8bf09385a39474a5db04351944b
  cross_layer_regression:
    file: CROSS_LAYER_REGRESSION_R2_INITIAL.txt
    sha256: c4504aee2693e2bed688578848eb6de97139cef5554b22b94975b68282bd70b1
  adversarial_property:
    file: FUZZ_REPORT.json
    sha256: 62e4786aca3d55c7749cfe448f19ec480856adff8eb1042dc66d24a113dd1837
  transport_property:
    file: TRANSPORT_FUZZ_REPORT.json
    sha256: b0b38a164bbc366971527e71559d412304bd97b61a4143fb06b70fab09ff9826
  dail_soak:
    file: DAIL_SOAK_5000_REPORT.json
    sha256: 1a1fce7286f7bff00d346f751d1c41430ceb0f6ffaa1994302603f2e495c0f15
  protocol_repair_fuzz:
    file: PROTOCOL_REPAIR_FUZZ_1000.json
    sha256: 94294abe79994d4c20425f2ee3195a27a5c61c266710b8ddc5e88319cf95f76e
  protocol_repair_report:
    file: 理火四代_V4.0_ProtocolV2.6機器語義修補_跨層回歸報告_V0.1.md
    sha256: ba0d20e786e372d72abe87e1090319f36a78fe36af0eccfebb5fb8550444b202
  r3_compute_engine_llia_gate_report:
    file: 理火四代_V4.0_R3_ComputeEngine_LLIA-GATE_工程驗證報告_V0.1.md
    sha256: d7a44558af2f998be1f6c81d4a24dc5b2cd3768654be91691bf579f7b83924f3
  r3_cross_layer_regression:
    file: CROSS_LAYER_REGRESSION_R3.txt
    sha256: 5a94475442a19b996c0d3f4b41604ba458ab319fd0c4086d01cc493ff9962762
  r3_llia_competition_fuzz:
    file: LLIA_COMPETITION_FUZZ_2000.json
    sha256: 0ce94336fd55b122506df32e3c8107a6fb19e6a6cc3f40fe1248012925b25345
  r3_qualified_input_soak:
    file: QUALIFIED_INPUT_ENGINE_SOAK_1000.json
    sha256: 9fb6ea990f79d5ad8542d479c911c1a3fb0c67e5d1feca8f7297c671a70f5020
FORMAL_FREEZE_EVIDENCE:
  hygiene_regression:
    file: lihuo4_dail_runtime_v0_3_1/FORMAL_FREEZE_REGRESSION_R3_1.txt
    sha256: 660b85499459b0e59364414da146a8744a4042d1ab8d96efd9b93b418f23099c
  llia_competition_fuzz:
    file: lihuo4_dail_runtime_v0_3_1/LLIA_COMPETITION_FUZZ_2000.json
    sha256: 0ce94336fd55b122506df32e3c8107a6fb19e6a6cc3f40fe1248012925b25345
  qualified_input_soak:
    file: lihuo4_dail_runtime_v0_3_1/QUALIFIED_INPUT_ENGINE_SOAK_1000.json
    sha256: 9fb6ea990f79d5ad8542d479c911c1a3fb0c67e5d1feca8f7297c671a70f5020
  freeze_report:
    file: 理火四代_V4.0_R3.1_FormalFreeze_HygieneRegression_報告_V0.1.md
    sha256: 8bd0116986c1fa59662e32ea6b4a37fdbc7ed28a24798cbac64eb8acd97a7237
SEMANTIC_AUTHORITY_FREEZE_EVIDENCE:
  regression:
    file: lihuo4_dail_runtime_v0_3_2/SEMANTIC_AUTHORITY_FREEZE_REGRESSION_RC2.txt
    sha256: da1313efa31a24a4fba263ef914d8adc71974581deb1aaabfbd114dccc71cc36
  llia_competition_fuzz:
    file: lihuo4_dail_runtime_v0_3_2/LLIA_COMPETITION_FUZZ_2000.json
    sha256: 0ce94336fd55b122506df32e3c8107a6fb19e6a6cc3f40fe1248012925b25345
  qualified_input_soak:
    file: lihuo4_dail_runtime_v0_3_2/QUALIFIED_INPUT_ENGINE_SOAK_1000.json
    sha256: 9fb6ea990f79d5ad8542d479c911c1a3fb0c67e5d1feca8f7297c671a70f5020
  final_freeze_audit:
    file: 理火四代_V4.0_RC2_SemanticAuthorityBoundary_FinalFreezeAudit_V0.1.md
    sha256: b1bb65f0c20219bcb202899599af430372f9b87fafd5f6815f00c870f2ca6451

FORMAL_PROMOTION_EVIDENCE:
  promotion_review:
    file: 理火四代_V4.0_PromotionReview_正式升版審查_V0.1.md
    sha256: c1f8f726b1ed91484587d98ec219f482eeda431eb30608b721386e2070969745
  formal_regression:
    file: lihuo4_dail_runtime_v4_0_formal/FORMAL_PROMOTION_REGRESSION_V4_0.txt
    sha256: 9dd5767d493c29c5dc276fe5b6b52f1cab77dbc511d78cef944328cc71bd9e71
  llia_competition_fuzz:
    file: lihuo4_dail_runtime_v4_0_formal/LLIA_COMPETITION_FUZZ_2000.json
    sha256: 0ce94336fd55b122506df32e3c8107a6fb19e6a6cc3f40fe1248012925b25345
  qualified_input_soak:
    file: lihuo4_dail_runtime_v4_0_formal/QUALIFIED_INPUT_ENGINE_SOAK_1000.json
    sha256: 9fb6ea990f79d5ad8542d479c911c1a3fb0c67e5d1feca8f7297c671a70f5020
  formal_main_dail:
    file: lihuo4_dail_runtime_v4_0_formal/lihuo_main_v4.dail.yaml
    sha256: 37d970dd594091a43cee184c1169144953014a473b20331488a1f68f1646aa31
  formal_lighter_dail:
    file: lihuo4_dail_runtime_v4_0_formal/lihuo_lighter_v4.dail.yaml
    sha256: 4d454aa892dd9f8ace144a02cf80a25003cff49745b1d58224be6fe196b41a22
  compiled_ir:
    file: lihuo4_dail_runtime_v4_0_formal/lihuo4_runtime_ir.json
    sha256: 8725850a456dbcc88edb484a1dbed806e60bc2e841e5f6f198ad3c92be1fbf67

```



---

## V4.1 Competition-Semantics Promotion Evidence

V4.1 本次新增的文件／DAIL 靜態驗證與語義回歸見：

```text
理火四代_MAIN_V4.1_競爭語義回歸與靜態審計_V1.0.md
```

其證據法位仍是 STATIC / MODEL-CONTRACT AUDIT，E5_OR_BELOW；不宣稱 E6 target runtime 或 E7 host enforcement。

---

# 附錄 C｜Promotion / Version History

本附錄只保留正式版必要 provenance，不把歷代 patch 重新塞回正文。

```text
ARCH-CANDIDATE
→ R2: Protocol V2.6 machine semantics / dirty graph / R-CCC applicability / non-shaping gate
→ R3: Main = Compute Engine；Lighter = Control Plane；LLIA-GATE / Competition Integrity
→ R3.1: exact symbol / issuer-owner / manifestation dirty activation formal-freeze hygiene
→ RC1: document freeze / canonical presentation
→ RC2: external-constraint evidence + premise disqualification basis + recompute-evidence closure disqualification
→ V4.0-FORMAL: promotion only; no semantic drift from RC2
→ V4.1-FORMAL: Qualified PATH endpoint + mandatory R2 full recompetition + residue lifecycle + premise discrimination gap
→ V4.2-FORMAL: resident state infrastructure + seven field modules event-driven activation topology
```

正式版的 authority precedence 保持：

```text
LIHUO PROTOCOL V2.7
>
V4.3.1 embedded canonical DAIL (inherited V4.3 compute semantics)
>
compiled IR
>
implementation
```

---

<!-- END VERBATIM MAIN V4.3.1 -->

---

**END OF LIHUO MAIN V4.4 FULL RATIFIED**
**RATIFIED 2026-10-06T13:31:00+08:00 / NOT_HOST_DEPLOYED**
<!-- END FULL INHERITED MAIN V4.4 -->

---

# V5.0.1 FULL BODY FINAL LOCK

```text
MAIN V5.0.1 FULL BODY
=
V5.0.0 RATIFIED OPERATIVE SEMANTICS
+
V4.4.1 RATIFIED PATCH
+
V4.4 FULL INHERITED BODY
-
ONLY THOSE MATERIAL CONFLICTS SUPERSEDED BY V4.4.1 / V5.

MAIN BODY MAY NOW BE READ FROM ONE FILE.
```

**END OF LIHUO MAIN V5.0.1 SELF-CONTAINED FULL BODY RATIFIED CURRENT**

<!-- END VERBATIM LIHUO MAIN V5.1.0 SOURCE -->
