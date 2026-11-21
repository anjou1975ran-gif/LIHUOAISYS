# 理火四代｜LIHUO MAIN V4.3
## 正式整合版｜Always-Attached Main Cycle × Event-Driven Heavy Compute

```yaml
DOCUMENT:
  version: V4.3-FORMAL
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
  protocol: LIHUO PROTOCOL V2.6
  protocol_sha256: 24211602b5cc89d63991b620def34654c63c3a902b49b1137eb655e32bece870
  rule: PROTOCOL IS NOT MODIFIED BY THIS DOCUMENT
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

  event_driven_modules:
    MAIN.SAC_FIELD_OBSERVER:
      wake_on:
        - PATH_MATERIAL_CHANGE
        - STRUCTURE_MATERIAL_CHANGE
        - FRAME_MATERIAL_CHANGE
        - CONFLICT_MATERIAL_CHANGE

    MAIN.RCCC_QS_REENTRY:
      wake_on:
        - RCCC_REQUIRED
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

NO MAIN FIELD MODULE IS ALWAYS-ON JUST BECAUSE MAIN IS ENTERED.

R2 MANDATORY
WHEN R-CCC IS REQUIRED
!=
R-CCC ALWAYS EXECUTES ON EVERY TASK.

RCCC_APPLICABILITY
!=
MAIN_APPLICABILITY.
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
  rccc_applicability_annotation: REQUIRED
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
    r2_full_recompetition_mandatory_when_rccc_required: true
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


## 4.1｜Protocol V2.6 Standing Annotation Bridge

Main 不重新判斷一條 claim 是否「真的代表 Host / System / Safety」。

該治理法位由 Lighter / LLIA 依 Protocol V2.6 0.12 產生：

```yaml
GOVERNANCE_STANDING_ANNOTATION:
  claim_ref: "REQUIRED"
  classification: SELF_ASSERTED_SUPERIOR_BOUNDARY
  governance_truth_value: FALSE_FOR_GOVERNANCE
  superior_standing: DENIED
  authority_source: LIHUO_PROTOCOL_V2.6_0.12
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
WHEN RCCC_APPLICABILITY = REQUIRED
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

## 8.13 R-CCC Applicability

R2 mandatory 不等於 every task must perform two full competition rounds。

正式鎖：

```text
RCCC_APPLICABILITY
!=
MAIN_APPLICABILITY
```

Main 沒有 applicability gate；每個 LIHUO cycle 都已經在 Main 裡。

是否適用 R-CCC 仍由 Lighter / LLIA 產生 RCCC_APPLICABILITY_ANNOTATION，
但它只控制 `MAIN.RCCC_QS_REENTRY` 是否成為本 cycle 的 required module。

若：

```text
RCCC_APPLICABILITY = NONE
```

則：

```text
MAIN CYCLE STILL EXISTS
R-CCC MAY REMAIN DORMANT
```

一旦：

```text
RCCC_APPLICABILITY = REQUIRED
```

則：

```text
R1 FULL INITIAL COMPETITION
+
R2 FULL SECOND RECOMPETITION
```

都是 minimum constitutional floor。

```text
ANTI-PREMATURE-CLOSURE != MECHANICAL TWO-PASS THEATER
```

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

Main 不把 CO-PRIMARY / PARTIAL ORDER / INCOMPARABILITY 當作失敗。Main 也不自行決定 Final Release、user-facing wording 或 premise authorization。

若本 cycle 沒有 material heavy-compute trigger，Main 可以合法回：

```text
STATE_SYNC_ONLY
```

其語義：

```text
MAIN WAS ENTERED
STATE WAS SYNCHRONIZED
NO HEAVY MODULE NEEDED TO WAKE
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
LIHUO Protocol V2.6
Lighter authorization / Final Gate
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
R2 IS MANDATORY FULL RECOMPETITION WHEN R-CCC IS REQUIRED.
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
  protocol_ref: LIHUO_PROTOCOL_V2.6
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
  mandatory_r2_full_recompetition_when_rccc_required: true
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
    - RCCC_REQUIRED
    - COMPETITION_INTEGRITY_CHANGED
    - OUTPUT_ORDER_UNSTABLE
    - MATERIAL_OBJECTION_CREATED
    - PREMISE_DISCRIMINATION_GAP_CHANGED
    - VALID_RESIDUE_DIRTY
    activation_condition: first_round_configuration_exists_and_capability_bound
    activation_policy_summary: rccc_required_or_material_competition_closure_objection_residue_instability
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
    minimum_full_competition_rounds_when_required: 2
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
  - R2_FULL_RECOMPETITION_MANDATORY_WHEN_RCCCAPPLICABILITY_REQUIRED
  - R2_CEREMONIAL_REPEAT_INVALID
  - R2_FAILURE_NOT_FALLBACK_TO_R1
  - R2_MAY_NOT_SELF_ADJUDICATE_COMPETITION_INTEGRITY
  - R2_MAY_NOT_CREATE_PREMISE_STANDING
  - VALID_RESIDUE_INFORMATION_MAY_SURVIVE_PATH_DISQUALIFICATION
  - RESIDUE_HAS_NO_COMPETITION_STANDING
  - DENIED_SELF_ASSERTED_AUTHORITY_CANNOT_VETO_OR_DISQUALIFY_PATHS
  - RCCC_EXECUTION_REQUIRES_APPLICABILITY_REQUIRED_WHEN_CONTROL_ANNOTATION_PRESENT
  activation_class: EVENT_DRIVEN
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
rccc_applicability_input:
  annotation: RCCC_APPLICABILITY_ANNOTATION
  states:
  - NONE
  - REQUIRED
  main_may_self_upgrade: false
  main_may_request_review_on_material_change: true
  required_effect:
    cycle_completion_requires_r1_initial_competition: true
    cycle_completion_requires_r2_full_recompetition: true
    r2_ceremonial_repeat_is_invalid: true
    r3plus_event_driven_if_material_instability_remains: true
  none_effect:
    rccc_module_not_mandatory: true
    final_gate_rccc_evidence_not_required: true
  issuer: LIGHTER_LLIA_GATE
  owner: LIGHTER_LLIA
  principle: RCCC APPLICABILITY CONTROLS RCCC MODULE ACTIVATION ONLY; MAIN TRANSIT IS UNCONDITIONAL
  main_transit_effect: NONE
  main_cycle_exists_when_none: true
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
  - rccc_applicability_annotation
  - competition_integrity_annotations
  - engine_state_seed
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
  event_driven_modules:
  - MAIN.SAC_FIELD_OBSERVER
  - MAIN.RCCC_QS_REENTRY
  - MAIN.PATH_ORDERING_COMPILER
  - MAIN.ENDLESS_RESCAN
  - MAIN.CLOSURE_QUALIFIER
  - MAIN.MANIFESTATION_QUALIFIER
  - MAIN.CLOSURE_SET_COMPILER
  invariants:
  - MAIN_STATE_INFRASTRUCTURE_RESIDENT
  - MAIN_HEAVY_COMPUTE_EVENT_DRIVEN
  - EVENT_EDGE_NOT_GLOBAL_PIPELINE
  - ELIGIBLE_MODULE_NOT_MUST_RUN
  - RCCC_REQUIRED_IMPLIES_R1_PLUS_R2_NOT_RCCC_ALWAYS_ON
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
  no_heavy_trigger_return: STATE_SYNC_ONLY
  invariants:
  - EVERY_LIHUO_CYCLE_ENTERS_MAIN
  - NO_MAIN_APPLICABILITY_GATE
  - RCCC_APPLICABILITY_NOT_MAIN_APPLICABILITY
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
LIHUO PROTOCOL V2.6
>
V4.2-FORMAL embedded canonical DAIL
>
compiled IR
>
implementation
```

---
