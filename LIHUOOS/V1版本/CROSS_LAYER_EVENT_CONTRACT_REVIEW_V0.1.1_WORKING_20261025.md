# LIHUOOS V1｜CROSS-LAYER EVENT CONTRACT REVIEW V0.1.1-WORKING
## 跨層事件契約審查｜Event Identity × Owner × Evidence Standing × Receipt Ceiling × Downstream Consumption
### 2026-10-25

```yaml
DOCUMENT:
  id: LIHUOOS_CROSS_LAYER_EVENT_CONTRACT_REVIEW
  version: V0.1.1-WORKING
  date: 2026-10-25
  status:
    - WORKING_REVIEW
    - CROSS_LAYER_INTERFACE_DESIGN
    - NOT_RATIFIED
    - NOT_HOST_DEPLOYED
    - NOT_RUNTIME_RECEIPT

  predecessor:
    file: "CROSS_LAYER_EVENT_CONTRACT_REVIEW_V0.1_WORKING_20261025.md"
    blob_sha: "23f9af8b8f68cdff0ade9c9ee9c36966a3861a95"

  trigger:
    - L8_V0_2_1_CORE_ARCHITECTURE_PASS
    - CROSS_LAYER_EVENT_CONTRACT_REVIEW_READY
    - TARGETED_INTERFACE_REPAIR_REQUIRED

  source_bindings:
    L5:
      file: "LIHUOOS/V1版本/L5 第二版本.md"
      blob_sha: "84c3cb9f978932d99a1c9e9dbae7c9ee9fcd1274"
    L6:
      file: "LIHUOOS/V1版本/L6 第二版本.md"
      blob_sha: "f028e4c35a047e8fe6851c616ba3251a8a740418"
    L7:
      file: "LIHUOOS/V1版本/L7 第二版本.md"
      blob_sha: "a25fc8da5efcb267d6f0aec4e626748cf097e1d8"
    L8:
      file: "LIHUOOS/V1版本/L8_LIHUO_PRIMARY_GOVERNING_CYCLE_V0.2.1_WORKING_20261025.md"
      blob_sha: "49e29ac965fad15a52699fdacf731a76ea7429d6"
    MAIN:
      file: "理火V5系統/V5.1版本/02_LIHUO_MAIN_V5.1.1_FULL_BODY_RATIFIED_20261015.md"
      blob_sha: "f5e219c986debfea074fbf9d121367cc717dc78e"
```

---

# 0｜本輪問題縮到最小

本輪不再問：

> 理火週期長什麼樣？

本輪只問：

```text
EVENT E
EXISTS IN LEDGER
↓
WHO CLAIMS E OCCURRED?
↓
WHAT TYPE OF EVENT IS E?
↓
WHO OWNS THAT EVENT TYPE?
↓
WHICH IDENTITY BINDING APPLIES?
↓
WHAT EVIDENCE EXISTS?
↓
WHAT DOES L5 ALLOW THAT EVIDENCE TO SUPPORT?
↓
WHAT MAY THE RECEIPT LEGALLY SAY?
↓
WHAT MAY THE NEXT OWNER LEGALLY CONSUME?
```

只要其中一格斷掉：

```text
DOWNSTREAM CONSUMPTION
=
NOT AUTOMATICALLY QUALIFIED
```

---

# 1｜第一總判決

```text
CROSS-LAYER EVENT CONTRACT REVIEW V0.1

EVENT IDENTITY
=
MUST BE SEPARATED FROM OCCURRENCE CLAIM

EVENT TYPE
=
MUST BE OWNER-TYPED

OWNER
=
MUST BE SEPARATED FROM RECORDER / OBSERVER / CLAIM ISSUER

IDENTITY BINDING
=
MUST BE TYPE-APPROPRIATE
NOT UNIVERSAL ALL-REFS REQUIRED

EVIDENCE
=
MUST HAVE ORIGIN / ACCESS / SCOPE / TIME / PROVENANCE

L5 STANDING
=
MUST GOVERN CLAIM CEILING

RECEIPT
=
MUST REFERENCE EVIDENCE-BOUND CLAIM
NOT CREATE OCCURRENCE

DOWNSTREAM CONSUMPTION
=
MUST BE EXPLICITLY QUALIFIED

CORE CONTRACT DIRECTION
=
PASS IN PRINCIPLE

RUNTIME IMPLEMENTATION
=
HOLD
```

---

# 2｜最重要的分離：Event != Claim != Evidence != Receipt

```text
EVENT IDENTITY
!=
EVENT OCCURRENCE CLAIM

EVENT OCCURRENCE CLAIM
!=
EVIDENCE

EVIDENCE
!=
OBSERVATION STANDING

OBSERVATION STANDING
!=
RECEIPT

RECEIPT
!=
EVENT OCCURRENCE

EVENT OCCURRENCE
!=
DOWNSTREAM CONSUMPTION RIGHT
```

最短式：

> **一個 event 可以被命名，不代表它被證明發生；一份 evidence 可以存在，不代表它支持那個 claim；一張 receipt 可以存在，不代表下一層有權把它當真。**

---

# 3｜不要建立 Universal Event State；建立 Event Envelope

Cross-layer contract 不應把所有事件壓成單一 lifecycle enum。

因此定義：

```yaml
CROSS_LAYER_EVENT_ENVELOPE:
  event_ref: REQUIRED
  event_type_ref: REQUIRED

  event_type_owner_ref: REQUIRED_OR_UNRESOLVED
  event_type_owner_status:
    - ESTABLISHED
    - UNRESOLVED

  event_payload_ref: REQUIRED

  identity_binding_profile_ref: REQUIRED
  identity_binding_ref: REQUIRED

  event_related_epistemic_claim_refs: []
  evidence_refs: []
  observation_standing_refs: []
  receipt_refs: []

  producer_ref: REQUIRED_OR_NONE
  recorder_ref: REQUIRED
```

這個 envelope 只做 cross-layer routing / binding。

它不定義各 event type 自己的 semantics。

硬鎖：

```text
EVENT ENVELOPE
!=
EVENT TYPE ONTOLOGY

EVENT ENVELOPE
!=
OWNER

EVENT ENVELOPE
!=
OCCURRENCE PROOF
```

---

# 4｜Owner 必須拆四個角色

至少要拆：

```text
EVENT TYPE OWNER
!=
EVENT PRODUCER / ACTOR
!=
CLAIM ISSUER
!=
RECORDING ACTOR
!=
EVIDENCE SOURCE
!=
OBSERVER
```

例如：

Main return emission：

```text
EVENT TYPE OWNER
=
LIHUO_MAIN

PRODUCER
=
LIHUO_MAIN

CLAIM ISSUER
=
may be Main emission-evidence object / later observer

RECORDER
=
L8 ledger / other lawful recorder

OBSERVER
=
may be L5-qualified observer
```

不能因為 L8 記了它，就變成：

```text
L8 OWNS MAIN RETURN EMISSION
```

---

# 5｜Event Type Family 只做路由，不奪 owner

V0.1 working family：

```text
COMPUTE_EVENT
GOVERNANCE_EVENT
OBSERVATION_EVENT
INTERVENTION_EVENT
MANIFESTATION_EVENT
EXTERNAL_ACTION_EVENT
IDENTITY_BINDING_EVENT
RETURN_EMISSION_EVENT
OTHER_TYPED_EVENT
```

但這不是 universal ontology freeze。

每個 event 必須回 canonical owner/type source。

例如：

```yaml
EVENT_TYPE_BINDING:
  event_type_ref: MAIN_RETURN_EMITTED
  family: RETURN_EMISSION_EVENT
  canonical_owner_ref: LIHUO_MAIN
  canonical_contract_ref: MAIN_RETURN_EMISSION_EVIDENCE_V5_1
```

以及：

```yaml
EVENT_TYPE_BINDING:
  event_type_ref: RELEASE_OCCURRED
  family: MANIFESTATION_EVENT
  canonical_semantic_owner_ref: L7
  occurrence_standing_owner_ref: L5
  action_standing_ref: L6_IF_EXTERNAL_STATE_CHANGE
```

這裡已經出現重要事實：

> **同一 event 可以有 semantic owner、action owner、occurrence-standing owner；它們不一定是同一個 owner。**

---

# 6｜Identity Binding 不得要求所有 Event 都帶完整 Tuple

不是所有 event 都必須同時綁：

```text
Primary
Attempt
Invocation
```

應依 event type 需要採 profile。

```yaml
EVENT_IDENTITY_BINDING_PROFILE:
  profile_ref: REQUIRED
  required_identity_axes: []
  optional_identity_axes: []
  prohibited_identity_axes: []
```

最低 profile：

## 6.1｜PRIMARY_SCOPED

```text
requires:
  governing_cycle_ref
```

## 6.2｜ATTEMPT_SCOPED

```text
requires:
  generation_attempt_ref

and:
  applicable generation_attempt_primary_binding_ref
  when event is evaluated inside a particular Primary
```

## 6.3｜MAIN_INVOCATION_SCOPED

```text
requires:
  governing_cycle_ref
  generation_attempt_ref
  main_invocation_ref
```

並應能對 canonical Main request / identity / return 精確核對。

## 6.4｜CROSS_PRIMARY_ATTEMPT_RELATION

例如 successor-primary binding event：

```text
requires:
  generation_attempt_ref
  predecessor_primary_ref
  successor_primary_ref
  binding_ref
```

## 6.5｜EXTERNAL_ACTION_SCOPED

依 action contract 決定。

不能因為事件出現在理火 cycle 裡，就假設外部世界 event identity 等於 Main invocation identity。

硬鎖：

```text
EVENT IN CYCLE
!=
EVENT OWNED BY CYCLE

EVENT OBSERVED DURING INVOCATION
!=
EVENT CREATED BY INVOCATION
```

---


# 7｜Event-Related Epistemic Claim｜不要把 causal claim 塞成 occurrence claim

V0.1 的 `EVENT_OCCURRENCE_CLAIM_BINDING` 名稱過窄且會誤導。

因為：

```text
E OCCURRED
!=
E CAUSED F
```

所以 V0.1.1 改為：

```yaml
EVENT_RELATED_EPISTEMIC_CLAIM_BINDING:
  event_ref: REQUIRED
  epistemic_claim_ref: REQUIRED

  claim_relation_to_event:
    - OCCURRENCE
    - DESCRIPTION
    - PROCESS
    - NEGATIVE_OCCURRENCE
    - CAUSAL
    - META
    - OTHER

  canonical_l5_claim_type:
    - EVENT_DESCRIPTION
    - PROCESS_CLAIM
    - NEGATIVE_CLAIM
    - CAUSAL_CLAIM
    - META_OBSERVATION_CLAIM
    - OTHER_APPLICABLE_L5_TYPE

  claim_scope_ref: REQUIRED
  temporal_scope_ref: REQUIRED

  evidence_refs: []
  observation_standing_ref: REQUIRED
```

硬鎖：

```text
EVENT-RELATED CLAIM
!=
EVENT-OCCURRENCE CLAIM

EVENT DESCRIPTION
!=
CAUSAL CLAIM

OBSERVED EVENT
!=
OBSERVED CAUSALITY
```

這個分離是下一階段 Evidence / Instrumentation Boundary Review 的前提。

因為同一份 host log 可能支持：

```text
EVENT OCCURRED
```

但未必支持：

```text
EVENT CAUSED RESULT F
```

---

# 8｜Evidence Binding｜來源不等於 standing

Evidence item 可以來自：

```text
RUNTIME
TOOL
MODEL_REPORT
HUMAN REPORT
DOCUMENT
EXTERNAL DATABASE
INSTRUMENT
SIMULATION
DERIVED COMPUTATION
OTHER
```

L8 先前工程枚舉：

```text
MODEL_SELF_REPORT
OWNER_RETURN
PROVIDER_RECEIPT
HOST_INSTRUMENTATION
STATE_READBACK
EXTERNAL_OBSERVATION
DERIVED_OR_INFERRED
```

可保留為 engineering origin mapping。

但必須投影回 L5：

```text
SOURCE ORIGIN
+
EPISTEMIC MODE
+
OBSERVER ACCESS MODE
+
SOURCE ACCESS MODE
+
SCOPE
+
TIME
+
PROVENANCE
+
TARGET FIDELITY
↓
OBSERVATION STANDING
```

因此：

```text
EVIDENCE ORIGIN
!=
EVIDENCE STANDING
```

---

# 9｜L5 Claim Ceiling 是跨層信任的真正閘

L5 已鎖：

```text
EVIDENCE ITEM EXISTS
!=
CLAIM SUPPORTED

DIRECT RECORD ACCESS
!=
DIRECT PROCESS ACCESS

SELF-REPORT
!=
HIDDEN-STATE OBSERVATION

CLAIM
MUST REMAIN WITHIN
EVIDENCE-LICENSED CLAIM ENVELOPE
```

因此 Cross-Layer Event Contract 必須要求：

```yaml
EVENT_EPISTEMIC_STANDING_BINDING:
  event_ref: REQUIRED
  event_related_epistemic_claim_ref: REQUIRED
  evidence_refs: []
  l5_observation_standing_ref: REQUIRED

  supported_claim_envelope_ref: REQUIRED
  unsupported_claim_refs: []
  contradiction_refs: []
  gap_refs: []
```

下游不應直接 consume：

```text
RAW RECEIPT SHAPE
```

而應 consume：

```text
CLAIM
+
L5 STANDING
+
SCOPE
+
TIME
+
PROVENANCE
```

---


# 10｜Receipt Contract｜Consumer-Agnostic + Open-World Claim Ceiling

Receipt 是 upstream 已成立之 evidence-bound claim 的紀錄。

因此：

```text
RECEIPT
=
CONSUMER-AGNOSTIC
EVIDENCE-BOUND CLAIM RECORD
```

Receipt 不得綁死特定 downstream consumption profile。

V0.1 的：

```text
downstream_consumption_profile_ref: REQUIRED
```

正式撤回。

V0.1.1 改為：

```yaml
CROSS_LAYER_EVENT_RECEIPT:
  receipt_ref: REQUIRED
  event_ref: REQUIRED

  event_related_epistemic_claim_ref: REQUIRED
  evidence_refs: []

  l5_observation_standing_ref: REQUIRED
  evidence_licensed_claim_envelope_ref: REQUIRED

  receipt_issuer_ref: REQUIRED
  receipt_scope_ref: REQUIRED
  receipt_time_ref: REQUIRED

  supports_claim_refs: []
  does_not_support_claim_refs: []
```

其中：

```text
supports_claim_refs
=
EXPLICIT POSITIVE EXAMPLES / BINDINGS

does_not_support_claim_refs
=
EXPLICIT HIGH-RISK EXCLUSIONS
```

但兩者都不是 closed-world universe。

永久鎖：

```text
CLAIM NOT EXPLICITLY DENIED
!=
CLAIM SUPPORTED

DOES_NOT_SUPPORT LIST
!=
EXHAUSTIVE COMPLEMENT
OF SUPPORTED CLAIM SPACE
```

真正 authoritative ceiling 仍然是：

```text
evidence_licensed_claim_envelope_ref
```

支持規則：

```text
SUPPORTED
ONLY IF

CLAIM IS
EXPLICITLY SUPPORTED

OR

QUALIFIED WITHIN
EVIDENCE-LICENSED CLAIM ENVELOPE
```

否則：

```text
UNLISTED / UNMAPPED CLAIM
→
REQUALIFICATION REQUIRED
```

Main precedent 仍保留：

```text
MAIN_RETURN_EMISSION_EVIDENCE_V5_1

proves:
  MAIN_RETURN_WAS_EMITTED_FOR_BOUND_INVOCATION
  EVIDENCE_REFERS_TO_BOUND_RAW_RETURN

does_not_prove:
  LIGHTER_QUALIFIED_CONSUMPTION_OCCURRED
  ALL_STAGES_SUCCEEDED
  COVERAGE_CLOSED
  FINAL_RELEASE
```

但這些 explicit exclusions 是高風險提醒，不是合法 claim space 的 exhaustive inverse。

---

# 11｜Typed Event Payload｜各 owner 保持自己的 type system

Cross-layer envelope 不統一 event payload。

例如：

## 11.1｜Main Stage Event

直接 consume：

```text
MAIN_STAGE_RECEIPT_V5_1
```

其 identity 已綁：

```text
governing_cycle_ref
generation_attempt_ref
main_invocation_ref
request_ref
exact_request_hash
```

且 conditional stage 已有：

```text
UNTRIGGERED CONDITIONAL STAGE
→
NO STAGE RECEIPT
```

因此 Cross-Layer contract 不應替 I9 造「未執行 receipt」。

## 11.2｜Main Return Emission Event

直接 consume：

```text
MAIN_RETURN_EMISSION_EVIDENCE_V5_1
```

此 evidence 可支持 bound return emission claim，
但不能自動支持 consumption / coverage / release。

## 11.3｜L6 Execution Event

應保留 L6：

```text
EXECUTION REQUESTED
!=
EXECUTION ATTEMPTED
!=
EXECUTED CHANGE
!=
OBSERVED EFFECT
```

不能把 `executed_change_ref` 與 `observed_effect_ref` 合成「成功」。

## 11.4｜L7 Release Event

L7 可定義：

```text
MANIFESTATION QUALIFICATION
RELEASE ADMISSIBILITY
```

但：

```text
L7 DOES NOT
SELF-CERTIFY
RELEASE OCCURRENCE
OR DELIVERY OCCURRENCE
```

所以 release occurrence claim 仍須 L5 standing。

若 release 本身是 external state-changing action：

```text
L7 STANDING
+
L6 ACTION STANDING
+
L5 OCCURRENCE STANDING
```

可能同時存在。

---


# 12｜Downstream Consumption Contract｜Actual Standing、Required Standing、Qualification Owner 分開

V0.1 的 `required_l5_standing_ref` 太容易讓「需求自己變成證明」。

V0.1.1 正式拆：

```text
WHAT UPSTREAM ACTUALLY HAS
!=
WHAT DOWNSTREAM REQUIRES
!=
WHETHER THE TWO ARE COMPATIBLE
```

同時再拆：

```text
CONSUMER
!=
CONSUMPTION QUALIFICATION OWNER
BY DEFAULT
```

因此 schema 改為：

```yaml
DOWNSTREAM_EVENT_CONSUMPTION:
  consumption_ref: REQUIRED

  consumer_owner_ref: REQUIRED
  event_ref: REQUIRED

  required_event_type_ref: REQUIRED
  required_identity_binding_profile_ref: REQUIRED

  event_related_epistemic_claim_ref: REQUIRED

  upstream_l5_observation_standing_ref: REQUIRED
  required_epistemic_standing_profile_ref: REQUIRED
  standing_compatibility_result_ref: REQUIRED

  receipt_ref: REQUIRED_OR_NONE
  evidence_refs: []

  required_scope_ref: REQUIRED
  required_temporal_applicability_ref: REQUIRED

  accepted_claim_envelope_ref: REQUIRED
  rejected_or_unsupported_claim_refs: []

  consumption_qualification_owner_ref: REQUIRED
  consumption_qualification_issuer_ref: REQUIRED
  consumption_authority_ref: REQUIRED_OR_NONE

  consumption_result:
    - ADMITTED_WITHIN_SCOPE
    - PARTIALLY_ADMITTED
    - HOLD
    - REJECTED
    - REQUALIFICATION_REQUIRED

  consumption_basis_ref: REQUIRED
```

這個 object 的意思不是：

> Consumer 想吃，所以自己填 PASS。

而是：

> 適用的 consumption qualification owner，依 upstream actual standing、consumer requirement、scope/time/identity binding 與 applicable authority，判斷這筆 event claim 可以被消費到哪裡。

硬鎖：

```text
CONSUMER WANTS INPUT
!=
CONSUMER MAY SELF-QUALIFY INPUT

UPSTREAM RECEIPT EXISTS
!=
DOWNSTREAM CONSUMPTION ADMISSIBLE

DOWNSTREAM REQUIRED STANDING
!=
UPSTREAM ACTUAL STANDING

REQUIREMENT FIELD
!=
PROOF FIELD
```

Cross-layer contract 只擁有 interface semantics。

```text
CROSS-LAYER CONTRACT
OWNS
INTERFACE SEMANTICS

L8
MAY BIND / TRACK

INSTANCE CONSUMPTION QUALIFICATION
BELONGS TO
APPLICABLE CONSUMER / GOVERNANCE OWNER

NOT L8 BY DEFAULT
```

某 domain 是否允許 consumer self-admission，必須由該 domain contract 明示。

---


# 13｜Anti-Laundering Lock｜禁止 Cross-Layer Standing Laundering

正式定義：

```text
CROSS-LAYER STANDING LAUNDERING
=
UPSTREAM CLAIM LICENSE
IS STRENGTHENED

OR

ITS MATERIAL LIMITS
ARE ERASED

DURING

PACKAGING
ROUTING
RECEIPT COMPOSITION
TRACE RENDERING
OR
DOWNSTREAM CONSUMPTION
```

被洗掉的不只 standing label。

還可能包括：

```text
scope
time
provenance
identity
uncertainty
authority
causal limits
access limits
target fidelity
```

典型失效：

```text
OWNER A
issues weak / scoped evidence

↓ packaging

OWNER B
reads receipt shape

↓ material limits disappear

OWNER B treats it as
stronger occurrence / authority / causality
than upstream evidence licensed
```

硬鎖：

```text
PACKAGING
MUST NOT
UPGRADE CLAIM LICENSE

ROUTING
MUST NOT
UPGRADE AUTHORITY

RECEIPT COMPOSITION
MUST NOT
UPGRADE OCCURRENCE PROOF

DOWNSTREAM CONSUMPTION
MUST NOT
ERASE MATERIAL LIMITS
```

---

# 14｜Anti-Aliasing Lock｜同名 Event 不得偷偷換 Identity

同一語詞：

```text
"R2 completed"
"release happened"
"Main returned"
```

可能被不同 object 使用。

所以必须綁：

```text
EVENT REF
+
EVENT TYPE REF
+
IDENTITY BINDING
+
SOURCE / PROVENANCE
```

禁止：

```text
SAME LABEL
→
ASSUME SAME EVENT
```

以及：

```text
NEW INVOCATION
+
COPIED OLD RECEIPT
→
CURRENT EVENT PROOF
```

Main 現有 exact request hash / invocation binding 是這條的典型實作。

---

# 15｜Historical Evidence != Current Standing

Main 已有：

```text
OLD MAIN RETURN
MAY REMAIN
HISTORICAL EVIDENCE.

IT DOES NOT SELF-RESTORE.
```

因此通用化：

```text
EVENT OCCURRED IN HISTORY
!=
EVENT / RETURN CURRENTLY APPLICABLE

HISTORICAL EVIDENCE
!=
CURRENT CONSUMPTION STANDING
```

Cross-layer consumption 必須帶：

```text
temporal applicability
current scope
current binding
current qualification
```

---


# 16｜Negative Event Claim｜Normative Absence != Empirical Nonoccurrence

對：

```text
event did not occur
no release happened
I9 did not run
```

不能只靠「沒看到 receipt」。

L5 已鎖：

```text
NOT OBSERVED
!=
DOES NOT EXIST
```

Main conditional stage contract 的：

```text
O9 = I9_NOT_TRIGGERED
→
I9 STAGE DOES NOT EXIST
→
I9 RECEIPT FORBIDDEN
```

能支持的是：

```text
NO LAWFUL I9 STAGE
SHOULD EXIST
UNDER THIS CONTROL FLOW
```

不能自動升成：

```text
NO I9-LIKE EXECUTION
ACTUALLY OCCURRED IN HOST
```

因為仍可能存在：

```text
rogue execution
erroneous execution
unauthorized execution
out-of-band execution
instrumentation gap
```

因此永久拆：

```text
LAWFUL STAGE NON-ENTRY
!=
EMPIRICAL ABSENCE
OF ANY CORRESPONDING HOST ACTION
```

若要支持 empirical nonoccurrence，
仍需足以覆蓋該 action 的：

```text
instrumentation
detectability relation
observation window
coverage
instrument health
target fidelity
```

所以：

```text
ABSENCE OF ARTIFACT
!=
NEGATIVE OCCURRENCE PROOF

LAWFUL CONTROL-FLOW NON-ENTRY
!=
EMPIRICAL HOST NONOCCURRENCE
```

新增 failure mode：

```text
CLX-11
NORMATIVE-ABSENCE
TO
EMPIRICAL-NONOCCURRENCE
LAUNDERING
```

定義：

> **把「依規則不應存在合法事件」洗成「實際世界中確定沒有任何相應事件發生」。**

---

# 17｜R3+ Export Gap 在 Cross-Layer Contract 裡的正式位置

L8 已正確標記：

```text
R3+ SEMANTICS
=
VALID

R3+ CURRENT MAIN RETURN EXPORT
=
OPEN GAP
```

本輪重新定位：

```text
GAP CLASS
=
CROSS-LAYER EVENT EXPORT CONTRACT GAP
```

缺的不是 R3+ 理論。

缺的是：

```text
R3+ EVENT
↓
CANONICAL MAIN EVENT / RECEIPT CARRIER
↓
MAIN RETURN EXPORT HANDLE
↓
L8 BINDING
↓
L5 STANDING
↓
DOWNSTREAM CONSUMPTION
```

現行兩個合法方向仍是：

```text
A.
MAIN_ACTUAL_STATE_RETURN_V5_1
adds canonical R3+ event / receipt refs

OR

B.
MAIN exports canonical stage/event-ledger ref
that includes R3+ typed evidence
```

這個 gap 現在可以正式交回 Main owner 修。

---

# 18｜第一版 Event Contract 最短鏈

```text
EVENT TYPE OWNER
creates / governs typed event semantics
↓
EVENT PAYLOAD / RETURN / ACTION RECORD
↓
EVENT IDENTITY BINDING
↓
EVENT-RELATED EPISTEMIC CLAIM ISSUED
↓
EVIDENCE BOUND
↓
L5 QUALIFIES CLAIM STANDING
↓
RECEIPT RECORDS EVIDENCE-BOUND CLAIM
WITH CLAIM CEILING
↓
L8 BINDS / TRACKS
WITHOUT UPGRADING STANDING
↓
DOWNSTREAM OWNER
EXPLICITLY QUALIFIES CONSUMPTION
↓
CONSUMPTION WITHIN SCOPE
OR HOLD / REJECT / REQUALIFY
```

---

# 19｜First Interface Dry Run｜Main Return Emission

## 19.1 Event

```text
E
=
MAIN RETURN EMITTED
```

## 19.2 Type Owner

```text
LIHUO_MAIN
```

## 19.3 Identity Binding

```text
MAIN_INVOCATION_SCOPED

governing_cycle_ref
generation_attempt_ref
main_invocation_ref
request_ref
exact_request_hash
main_return_ref
```

## 19.4 Evidence

```text
MAIN_RETURN_EMISSION_EVIDENCE_V5_1
```

## 19.5 Legal Claim

可支持：

```text
MAIN RETURN WAS EMITTED
FOR THIS BOUND INVOCATION
```

不可支持：

```text
ALL STAGES SUCCEEDED
COVERAGE CLOSED
LIGHTER CONSUMED IT
FINAL RELEASE OCCURRED
```

## 19.6 L5 Standing

若 evidence provenance / exact binding / access 足夠：

```text
EVENT DESCRIPTION
=
SUPPORTED_WITHIN_SCOPE
```

但不是：

```text
FULL PROCESS SUCCESS
```

## 19.7 Receipt

receipt 只能寫：

```text
BOUND MAIN RETURN EMISSION
SUPPORTED WITHIN DECLARED SCOPE
```

不得寫：

```text
LIHUO CYCLE COMPLETE
```

## 19.8 Downstream Consumption

L8 可以 consume：

```text
RETURN EMISSION CLAIM
+
IDENTITY BINDING
+
L5 STANDING
```

然後再等待：

```text
QUALIFIED RETURN CONSUMPTION
COVERAGE
REENTRY
RELEASE
```

各自 owner return。

結果：

```text
DRYRUN_EVENT_001
=
PASS
```

---

# 20｜Second Interface Dry Run｜Release Event

## 20.1 Event

```text
E
=
RELEASE OCCURRED
```

## 20.2 Owners

```text
L7
=
MANIFESTATION / RELEASE-ADMISSIBILITY SEMANTICS

APPLICABLE RELEASE AUTHORITY
=
AUTHORIZATION OWNER

L6
=
ACTION STANDING
WHEN RELEASE IS EXTERNAL STATE-CHANGING ACTION

L5
=
OCCURRENCE CLAIM STANDING
```

## 20.3 Invalid Shortcut

```text
L7 RELEASE ADMISSIBLE
→
RELEASE OCCURRED
```

非法。

同樣：

```text
SEND REQUEST ATTEMPTED
→
DELIVERED
```

非法。

## 20.4 Required Evidence Chain

至少要能區分：

```text
RELEASE REQUEST
EXECUTION ATTEMPT
EXECUTED RELEASE / PUBLISH / SEND
DELIVERY
RECEPTION
OBSERVED EFFECT
```

並由各 type owner / L5 standing 分別處理。

結果：

```text
DRYRUN_EVENT_002
=
PASS IN PRINCIPLE

ENGINEERING EVIDENCE PROFILE
=
OPEN
```

---

# 21｜本輪抓到的第一批 Cross-Layer Failure Modes

```text
CLX-01
CROSS-LAYER STANDING LAUNDERING

CLX-02
RECEIPT-SHAPE OCCURRENCE INFLATION

CLX-03
EVENT IDENTITY ALIASING

CLX-04
OWNER / RECORDER COLLAPSE

CLX-05
HISTORICAL-EVIDENCE SELF-RESTORATION

CLX-06
MISSING-RECEIPT NEGATIVE-CLAIM ERROR

CLX-07
ACTION / OBSERVATION / OUTCOME COLLAPSE

CLX-08
UPSTREAM CONTRACT SHADOWING

CLX-09
DOWNSTREAM AUTO-CONSUMPTION

CLX-10
SEMANTIC OWNER
IMPERSONATED AS
OCCURRENCE EVIDENCE OWNER

CLX-11
NORMATIVE-ABSENCE
TO
EMPIRICAL-NONOCCURRENCE
LAUNDERING
```

這些先作 working names，不宣稱外部既有術語。

---


# 22｜V0.1.1 Open Issues

```text
OPEN_1:
  R3+ canonical export carrier
  OWNER: MAIN
  STATUS: OPEN

OPEN_2:
  Evidence-origin × access × claim-type
  → L5 standing ceiling table
  OWNER: L5 / ENGINEERING PROJECTION
  STATUS: READY

OPEN_3:
  Event type registry source and ownership rules
  STATUS: OPEN

OPEN_4:
  Instance downstream consumption qualification owner
  RESULT:
    cross-layer contract owns interface semantics
    L8 may bind / track
    applicable consumer / governance owner qualifies instance consumption
  DOMAIN-SPECIFIC SELF-ADMISSION:
    still requires explicit contract
  STATUS: PARTIALLY CLOSED

OPEN_5:
  Release / provider / delivery instrumentation profiles
  STATUS: OPEN

OPEN_6:
  Host-level occurrence evidence minimum
  STATUS: OPEN
```

---


# 23｜V0.1.1 Standing

```text
CROSS-LAYER EVENT CONTRACT REVIEW V0.1.1-WORKING

EVENT / CLAIM / EVIDENCE /
STANDING / RECEIPT SEPARATION
=
PASS

EVENT ENVELOPE
=
PASS

OWNER ROLE SEPARATION
=
PASS IN PRINCIPLE

IDENTITY BINDING PROFILES
=
PASS

L5 CLAIM CEILING
=
PASS

ANTI-STANDING-LAUNDERING
=
PASS AFTER DEFINITION EXPANSION

RECEIPT CONSUMER DECOUPLING
=
PASS

RECEIPT OPEN-WORLD CLAIM CEILING
=
PASS

DOWNSTREAM ACTUAL-vs-REQUIRED STANDING
=
PASS

CONSUMPTION QUALIFICATION OWNER
=
PASS IN INTERFACE SEMANTICS

EVENT-RELATED CLAIM TYPE MODEL
=
PASS

NEGATIVE OCCURRENCE
NORMATIVE-vs-EMPIRICAL ABSENCE
=
PASS IN SEMANTIC MODEL

R3+ EXPORT GAP
=
CONFIRMED / MAIN OWNER LOCATED

VERDICT
=
PASS_WITH_TARGETED_INTERFACE_REPAIR_APPLIED

EVIDENCE / INSTRUMENTATION
BOUNDARY REVIEW
=
READY

RUNTIME CONTRACT RATIFICATION
=
HOLD
```

---

# 24｜最短根句

```text
EVENT IDENTITY
DOES NOT PROVE OCCURRENCE.

EVIDENCE EXISTENCE
DOES NOT PROVE THE CLAIM.

L5 LIMITS
WHAT THE CLAIM MAY SAY.

A RECEIPT
MUST NOT SAY MORE
THAN ITS EVIDENCE CAN SUPPORT.

L8 MAY BIND HISTORY.
L8 MAY NOT UPGRADE HISTORY.

THE NEXT OWNER
MUST QUALIFY WHAT IT CONSUMES.

A RECEIPT
IS NOT A PASSPORT
THAT AUTOMATICALLY CROSSES LAYERS.
```

---

# 25｜一句話收束

> **Cross-Layer Event Contract 的本體不是「讓事件可以跨層傳遞」，而是確保事件跨層時，identity、owner、evidence、standing 與 claim ceiling 不會在傳遞途中被洗掉。**
