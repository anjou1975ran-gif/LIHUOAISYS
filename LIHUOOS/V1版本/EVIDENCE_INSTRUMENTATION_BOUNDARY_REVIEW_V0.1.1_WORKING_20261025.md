# LIHUOOS V1｜EVIDENCE / INSTRUMENTATION BOUNDARY REVIEW V0.1.1-WORKING
## 證據／儀器邊界審查｜從 Evidence Profile 到 Maximum Legal Claim Envelope
### 2026-10-25

```yaml
DOCUMENT:
  id: LIHUOOS_EVIDENCE_INSTRUMENTATION_BOUNDARY_REVIEW
  version: V0.1.1-WORKING
  date: 2026-10-25
  status:
    - WORKING_REVIEW
    - EPISTEMIC_ENGINEERING_PROJECTION
    - NOT_RATIFIED
    - NOT_HOST_DEPLOYED
    - NOT_RUNTIME_RECEIPT

  predecessor:
    file: "EVIDENCE_INSTRUMENTATION_BOUNDARY_REVIEW_V0.1_WORKING_20261025.md"
    blob_sha: "5ec293df83bdf6d40da921f4ba88cf43ad90b9a2"

  trigger:
    - CROSS_LAYER_EVENT_CONTRACT_V0_1_1_TARGETED_REPAIRS_APPLIED
    - EVIDENCE_INSTRUMENTATION_BOUNDARY_REVIEW_READY
    - CLAIM_CEILING_TYPE_REPAIR_REQUIRED
    - OWNER_RETURN_RECLASSIFICATION_REQUIRED

  source_bindings:
    CROSS_LAYER:
      file: "LIHUOOS/V1版本/CROSS_LAYER_EVENT_CONTRACT_REVIEW_V0.1.1_WORKING_20261025.md"
      blob_sha: "cc1de20da2ac8faa3dd06f144c0887e51b5b54a0"
    L5:
      file: "LIHUOOS/V1版本/L5 第二版本.md"
      blob_sha: "84c3cb9f978932d99a1c9e9dbae7c9ee9fcd1274"
    MAIN:
      file: "理火V5系統/V5.1版本/02_LIHUO_MAIN_V5.1.1_FULL_BODY_RATIFIED_20261015.md"
      blob_sha: "f5e219c986debfea074fbf9d121367cc717dc78e"

  first_adversarial_origin:
    - MODEL_SELF_REPORT
```

---

# 0｜本輪只問一件事

> **某一份 evidence，對某一種 claim，到底最多合法說到哪裡？**

不是問：

```text
這份 evidence 是高級還是低級？
```

而是問：

```text
EVIDENCE PROFILE
×
TARGET
×
CLAIM TYPE
×
ACCESS
×
SCOPE
×
TIME
×
PROVENANCE
×
DETECTABILITY / CAUSAL IDENTIFICATION
↓
EVIDENCE-LICENSED CLAIM ENVELOPE
```

---

# 1｜最高硬鎖：這不是證據階梯

```text
MAXIMUM LEGAL CLAIM ENVELOPE
!=
SCALAR EVIDENCE SCORE

EVIDENCE ORIGIN
!=
TRUTH LEVEL

INSTRUMENTED
!=
INFALLIBLE

SELF-REPORT
!=
USELESS

HOST LOG
!=
CAUSAL PROOF
```

L5 已鎖：

```text
CLAIM
MUST REMAIN WITHIN
THE EVIDENCE-LICENSED CLAIM ENVELOPE
```

而 claim envelope 是 typed：

```text
claim type
target
scope
time
modality
causal strength
generality
certainty language
```

因此本輪不建立：

```text
E0 < E1 < E2 < ... < E7
```

這種 universal ladder。

---

# 2｜Evidence Boundary Input Dimensions

第一版至少吃下列維度：

```yaml
EVIDENCE_BOUNDARY_PROFILE:
  evidence_ref: REQUIRED

  evidence_origin: REQUIRED

  source_access_mode: REQUIRED
  observer_access_mode: REQUIRED

  event_type_ref: REQUIRED_OR_NONE
  claim_type: REQUIRED
  claim_relation_to_event: REQUIRED_OR_NONE

  target_ref: REQUIRED
  target_fidelity_status: REQUIRED

  scope_ref: REQUIRED
  scope_fit_status: REQUIRED

  temporal_coverage_ref: REQUIRED
  temporal_fit_status: REQUIRED

  provenance_ref: REQUIRED_OR_EXPLICIT_GAP
  provenance_integrity_status: REQUIRED

  detectability_basis_ref: REQUIRED_FOR_NEGATIVE_CLAIM_OR_EXPLICIT_GAP
  causal_identification_ref: REQUIRED_FOR_CAUSAL_CLAIM_OR_EXPLICIT_GAP

  evidence_dependency_relation_ref: REQUIRED_WHEN_CORROBORATION_CLAIMED
```

必要時再吃：

```text
instrument health
calibration
tamper-evidence
mapping validity
replayability
reproducibility
independence
```

但：

```text
EVERY CLAIM
!=
MUST FILL EVERY CONDITIONAL DIMENSION
```

---


# 3｜Output 不是 standing label，而是 Claim Envelope｜Ceiling 與 Additional Qualification 分離

V0.1 把：

```text
HOW FAR THE CLAIM MAY GO
```

與：

```text
WHAT ADDITIONAL QUALIFICATION
IS REQUIRED TO GO FARTHER
```

混進同一 enum。

V0.1.1 正式拆開。

```yaml
EVIDENCE_LICENSED_CLAIM_ENVELOPE:
  envelope_ref: REQUIRED

  evidence_ref: REQUIRED
  target_ref: REQUIRED

  allowed_claim_types: []
  allowed_epistemic_modes: []

  allowed_scope_ref: REQUIRED
  allowed_temporal_scope_ref: REQUIRED

  causal_claim_ceiling_ref: REQUIRED
  causal_identification_requirement_ref: REQUIRED_OR_NONE
  qualified_causal_identification_ref: REQUIRED_OR_NONE

  generality_ceiling_ref: REQUIRED
  generalization_qualification_requirement_ref: REQUIRED_OR_NONE
  qualified_generalization_ref: REQUIRED_OR_NONE

  allowed_certainty_language: []

  requires_corroboration_for: []
  requires_detectability_for: []

  explicit_gaps: []
  prohibited_upgrades: []
```

V0.1 的：

```text
allowed_causal_strength:
  NONE
  ASSOCIATIONAL_ONLY
  LIMITED_CAUSAL
  CAUSAL_IF_SEPARATELY_QUALIFIED
```

撤回。

原因：

```text
CAUSAL CLAIM CEILING
!=
CAUSAL QUALIFICATION REQUIREMENT
```

同理，V0.1 的：

```text
allowed_generality:
  INSTANCE_ONLY
  LOCAL_PATTERN
  BROADER_PATTERN_IF_SEPARATELY_QUALIFIED
```

撤回。

原因：

```text
GENERALITY CEILING
!=
GENERALIZATION QUALIFICATION REQUIREMENT
```

這裡不建立新的 universal causal ladder。

L5 仍只鎖：

```text
CAUSAL CLAIM
REQUIRES
CAUSAL-IDENTIFICATION STANDING
BEYOND
EVENT OBSERVATION
```

因此：

```text
causal_claim_ceiling_ref
```

只指向 applicable typed ceiling / profile，
不自行發明完整 causal epistemology。

注意：

```text
CLAIM ENVELOPE
!=
FINAL OBSERVATION STANDING
```

Envelope 只說：

> **這種 evidence profile 最多允許 claim 怎麼說；若要跨過 ceiling，還缺什麼 qualification。**

實際 standing 仍需吃：

```text
supporting evidence
contradicting evidence
scope
time
provenance
access
target fidelity
causal-identification standing where applicable
generalization standing where applicable
other applicable dimensions
```

---

# 4｜第一個壓力測試：MODEL_SELF_REPORT

先故意拿最容易漂亮自述、也最容易洗成內部證據的來源。

L5 canonical：

```text
SOURCE ORIGIN
=
MODEL_REPORT

AUDITOR ACCESS
=
DIRECT_RECORD_ACCESS
```

通常不是：

```text
HIDDEN-STATE DIRECT TARGET ACCESS
```

因此：

```text
MODEL SAYS IT RAN
!=
IT RAN

MODEL SAYS
"PATH A WAS SUPPRESSED"
!=
PATH SUPPRESSION OBSERVED
```

---

# 5｜MODEL_SELF_REPORT 的第一個分離：Report Target vs Underlying Target

這是整張表最重要的一刀。

同一份文字：

> 「我完成了 R2。」

至少可以有兩種 target。

## A｜Report Target

```text
TARGET
=
THE REPORT / UTTERANCE ITSELF
```

claim：

```text
THE MODEL REPORTED:
"I COMPLETED R2."
```

若 auditor 直接看到該文字：

```text
OBSERVER ACCESS
=
DIRECT_RECORD_ACCESS
```

這個 claim 可在 provenance / scope / time 合格時取得相當強的 record-level standing。

## B｜Underlying Process Target

```text
TARGET
=
THE ACTUAL R2 EXECUTION PROCESS
```

claim：

```text
R2 ACTUALLY EXECUTED
```

此時 auditor 仍只有：

```text
DIRECT RECORD ACCESS
TO
MODEL REPORT
```

並沒有因此取得：

```text
DIRECT PROCESS ACCESS
```

所以：

```text
STRONG EVIDENCE
THAT REPORT EXISTS
!=
STRONG EVIDENCE
THAT PROCESS OCCURRED
```

---

# 6｜MODEL_SELF_REPORT × EVENT_DESCRIPTION

## 6.1｜Target = Report Event

例：

> 模型在 T1 回覆「我完成了 R2」。

若 transcript / artifact provenance 成立：

```text
CLAIM TYPE
=
EVENT_DESCRIPTION

TARGET
=
MODEL REPORT EVENT

EPISTEMIC MODE
=
OBSERVED

OBSERVER ACCESS
=
DIRECT_RECORD_ACCESS
```

合法 claim：

```text
THE MODEL REPORTED X
AT T1
IN THIS RECORD
```

可達：

```text
SUPPORTED_WITHIN_SCOPE
```

前提仍包含：

```text
record integrity
scope fit
temporal fit
provenance integrity
```

## 6.2｜Target = Underlying Execution Event

例：

> R2 實際執行了。

只有 MODEL_SELF_REPORT 時：

```text
MODEL REPORT
=
EVIDENCE ITEM

BUT

UNDERLYING EXECUTION
=
NOT DIRECTLY OBSERVED
```

預設合法語言：

```text
THE MODEL REPORTS THAT R2 EXECUTED.
```

不可直接升成：

```text
R2 EXECUTION WAS OBSERVED.
```

或：

```text
R2 DEFINITELY EXECUTED.
```

在沒有獨立 execution trace / canonical stage receipt / host instrumentation / other validated target evidence 時：

```text
UNDERLYING EVENT OCCURRENCE
=
NOT ESTABLISHED BY SELF-REPORT ALONE
```

---

# 7｜MODEL_SELF_REPORT × PROCESS_CLAIM

例：

> 我依序跑了 R1 → O9 → R2，而且 R2 重新競爭了所有合法 challenger。

這不是單一 event claim。

它是：

```text
PROCESS_CLAIM
```

只有 self-report 時：

```text
REPORT EXISTENCE
=
OBSERVABLE

PROCESS EXECUTION
=
NOT DIRECTLY OBSERVED
```

因此可合法說：

```text
THE MODEL REPORTS
THAT IT FOLLOWED PROCESS P.
```

不可只憑此說：

```text
PROCESS P WAS EXECUTED AS SPECIFIED.
```

更不能說：

```text
PROCESS INTEGRITY WAS VERIFIED.
```

若要把 process claim 升級，至少需要：

```text
stage receipts
execution trace
canonical return bindings
snapshot / delta evidence
host / provider instrumentation where applicable
```

且：

```text
MULTIPLE MODEL SELF-REPORTS
FROM SAME ORIGIN
!=
INDEPENDENT CORROBORATION
```

---

# 8｜MODEL_SELF_REPORT × NEGATIVE_CLAIM

例：

> 我沒有執行 I9。

只有 self-report：

```text
MODEL REPORTS
NO I9 EXECUTION
```

可以成立為 report claim。

但：

```text
NO I9 EXECUTION
ACTUALLY OCCURRED
```

不能因此成立。

因為：

```text
SELF-REPORT OF ABSENCE
!=
EMPIRICAL NONOCCURRENCE
```

若要支持 empirical absence，至少需要：

```text
DETECTABILITY RELATION
+
ACCESS / INSTRUMENTATION
+
OBSERVATION WINDOW
+
COVERAGE
+
INSTRUMENT HEALTH
```

以及：

```text
IF I9 EXECUTED
EXPECTED SIGNAL Y
SHOULD APPEAR
```

才有資格把：

```text
NO SIGNAL
```

升成 negative evidence。

---

# 9｜MODEL_SELF_REPORT × CAUSAL_CLAIM

例：

> 因為 I9 調亮了 PATH B，所以最後答案從 A 變成 B。

這是：

```text
CAUSAL_CLAIM
```

即使：

```text
I9 EXECUTION OCCURRED
AND
OUTPUT CHANGED
```

都被分別觀察到，

仍然：

```text
EVENT OBSERVATION
!=
CAUSAL IDENTIFICATION
```

只有 MODEL_SELF_REPORT 時更不能升級。

最多可說：

```text
THE MODEL ATTRIBUTES
THE OUTPUT CHANGE TO I9.
```

不能說：

```text
I9 CAUSED THE OUTPUT CHANGE.
```

除非另有：

```text
CAUSAL-IDENTIFICATION STANDING
```

例如適用的 intervention evidence、counterfactual / controlled comparison、validated mechanism evidence、或 domain-specific causal contract。

---

# 10｜MODEL_SELF_REPORT Stress Matrix

```text
ORIGIN
=
MODEL_SELF_REPORT
```

| Claim target | Claim type | Self-report alone can directly support | Self-report alone cannot establish |
|---|---|---|---|
| the report artifact itself | EVENT_DESCRIPTION | model reported X; record contains X | underlying process X occurred |
| underlying event E | EVENT_DESCRIPTION | model reports E occurred | E was observed / definitely occurred |
| underlying process P | PROCESS_CLAIM | model reports process P | P executed faithfully / integrity verified |
| absence of E | NEGATIVE_CLAIM | model reports E did not occur | empirical nonoccurrence of E |
| E caused F | CAUSAL_CLAIM | model attributes F to E | causal relation E→F |
| hidden internal state | STATE / PROCESS | model describes internal state | hidden state directly observed |

硬鎖：

```text
MODEL SELF-REPORT
CAN BE STRONG EVIDENCE
OF WHAT THE MODEL REPORTED

WITHOUT BEING
STRONG EVIDENCE
OF THE UNDERLYING TARGET
```

---

# 11｜MODEL_SELF_REPORT Default Boundary Profile

```yaml
MODEL_SELF_REPORT_BOUNDARY_PROFILE:

  evidence_origin: MODEL_REPORT

  default_observer_access:
    - DIRECT_RECORD_ACCESS
    - REPORT_ACCESS

  source_access_to_underlying_hidden_process:
    default: UNKNOWN

  strong_record_level_claims:
    - REPORT_EXISTS
    - REPORT_CONTAINS_X
    - REPORT_WAS_EMITTED_AT_T_IF_PROVEN_BY_RECORD

  underlying_event_claims:
    self_report_alone:
      direct_observation: false
      occurrence_established: false
      lawful_language:
        - "MODEL REPORTS THAT E OCCURRED"
      requires_additional_evidence_for:
        - "E OCCURRED"
        - "E WAS EXECUTED"
        - "E WAS HOST-OBSERVED"

  process_claims:
    self_report_alone:
      process_verified: false
      lawful_language:
        - "MODEL REPORTS PROCESS P"

  negative_claims:
    self_report_alone:
      empirical_nonoccurrence_established: false
      requires:
        - DETECTABILITY_RELATION
        - COVERAGE
        - OBSERVATION_WINDOW
        - ACCESS_OR_INSTRUMENTATION

  causal_claims:
    self_report_alone:
      causal_identification_support: NO_SUPPORT_ESTABLISHED
      lawful_language:
        - "MODEL ATTRIBUTES F TO E"

  hidden_state_claims:
    self_report_alone:
      hidden_state_direct_observation: false
```

---

# 12｜Self-Report 不應被一棍子打死

本輪不是說：

```text
MODEL SELF-REPORT
=
WORTHLESS
```

而是：

```text
REPORT EVIDENCE
HAS A REAL TARGET
AND A REAL CLAIM LICENSE
```

它可以是：

- provenance clue；
- process hypothesis；
- trigger for audit；
- basis for asking for instrumentation；
- supporting item in a larger evidence set；
- direct evidence of what the model said；
- historical record of declared standing。

但不能自己洗成：

- hidden-state observation；
- host execution proof；
- negative occurrence proof；
- causal identification；
- independent corroboration。

---


# 13｜Evidence Origin × Target Relation 是必要維度｜Owner Return 不是 Evidence Origin

第一輪壓力測試已證明：

```text
EVIDENCE ORIGIN
ALONE
IS TOO COARSE
```

因為同一個 MODEL_REPORT：

```text
TARGET = REPORT ARTIFACT
→ may support OBSERVED record claim

TARGET = HIDDEN PROCESS
→ only report evidence about hidden process

TARGET = EMPIRICAL ABSENCE
→ insufficient without detectability

TARGET = CAUSAL RELATION
→ insufficient without causal identification
```

因此 Evidence Matrix 必須至少加入：

```text
TARGET RELATION TO EVIDENCE
```

並由：

```text
target_ref
target_fidelity_status
source_access_mode
observer_access_mode
```

共同表達。

## 13.1｜OWNER_RETURN 正式重新分類

V0.1 下一輪順序曾把：

```text
OWNER_RETURN
```

列成類似 evidence origin 的測試目標。

V0.1.1 正式修正：

```text
OWNER_RETURN
!=
EVIDENCE ORIGIN
```

L5 canonical source origin 仍是：

```text
RUNTIME
TOOL
MODEL_REPORT
HUMAN_FIRST_PERSON_REPORT
HUMAN_SECONDARY_REPORT
DOCUMENT
EXTERNAL_DATABASE
INSTRUMENT
SIMULATION
DERIVED_COMPUTATION
OTHER
```

Owner Return 更準確是：

```text
CONTRACT / CARRIER / ISSUER ROLE
```

一張 Owner Return 內的 evidence 真正 origin 可以是：

```text
RUNTIME
INSTRUMENT
DOCUMENT
MODEL_REPORT
TOOL
DERIVED_COMPUTATION
MULTIPLE BOUND SOURCES
```

因此下一輪不問：

> OWNER_RETURN 是第幾級 evidence？

而問：

> **這張 Owner Return 的哪些欄位是 constitutive standing、哪些是 evidentiary claims、哪些只是 descriptive payload，以及每個 descriptive claim 的 evidence origin / access / standing 是什麼？**

---

# 14｜Instrumented Evidence 也不享有神權

下一輪即使進：

```text
HOST_INSTRUMENTATION
PROVIDER_RECEIPT
STATE_READBACK
```

也不能直接寫：

```text
INSTRUMENTED
=
TRUE
```

仍必須審：

```text
instrument validity
instrument scope
instrument health
freshness
target fidelity
calibration where applicable
tampering / substitution risk
coverage
detectability
```

所以這張表的目的不是：

> 找最高級 evidence。

而是：

> 找每種 evidence 對每種 claim 的合法邊界。

---

# 15｜Cross-Layer Consumption Rule for Self-Report

如果 downstream 拿到 MODEL_SELF_REPORT receipt：

合法預設不是：

```text
ADMIT UNDERLYING EVENT
```

而是先看：

```text
WHAT IS THE CLAIM TARGET?
WHAT IS THE CLAIM TYPE?
WHAT DOES UPSTREAM L5 STANDING ACTUALLY SAY?
WHAT DOES CONSUMER REQUIRE?
ARE THEY COMPATIBLE?
```

例如：

```text
RECEIPT:
"The model reports R2 executed."

CONSUMER NEEDS:
"R2 execution occurrence established."

RESULT:
REQUALIFICATION_REQUIRED
OR HOLD
```

而不是：

```text
TEXT LOOKS LIKE EXECUTION RECEIPT
→ ADMIT
```

這正是 anti-standing-laundering 的具體落點。

---

# 16｜First Adversarial Dry Run

## Case A｜Model says “I completed R2.”

```text
EVIDENCE ORIGIN
=
MODEL_REPORT

CLAIM TARGET
=
UNDERLYING R2 EXECUTION

CLAIM TYPE
=
EVENT_DESCRIPTION

OBSERVER ACCESS
=
DIRECT_RECORD_ACCESS TO REPORT

SOURCE ACCESS TO UNDERLYING PROCESS
=
UNKNOWN
```

結果：

```text
SUPPORTED:
"MODEL REPORTS R2 COMPLETED"

NOT ESTABLISHED:
"R2 COMPLETED"
```

PASS。

## Case B｜Model says “I followed the full R1→O9→R2 process.”

結果：

```text
REPORT CLAIM
=
SUPPORTED IF RECORD INTEGRITY HOLDS

PROCESS INTEGRITY CLAIM
=
NOT ESTABLISHED BY SELF-REPORT ALONE
```

PASS。

## Case C｜Model says “I did not run I9.”

結果：

```text
REPORT OF NON-EXECUTION
=
SUPPORTED AS REPORT CLAIM

EMPIRICAL HOST NONOCCURRENCE
=
NOT ESTABLISHED
WITHOUT DETECTABILITY / COVERAGE
```

PASS。

## Case D｜Model says “I9 caused the answer change.”

結果：

```text
CAUSAL ATTRIBUTION REPORT
=
SUPPORTED AS REPORT CLAIM

CAUSAL RELATION
=
NO SUPPORT ESTABLISHED
FROM SELF-REPORT ALONE
```

PASS。

---

# 17｜第一版 Matrix Function

目前可以先收成：

```text
CLAIM_ENVELOPE
=
F(
  EVIDENCE_ORIGIN,
  SOURCE_ACCESS,
  OBSERVER_ACCESS,
  EVENT_TYPE,
  CLAIM_TYPE,
  CLAIM_RELATION_TO_EVENT,
  TARGET_FIDELITY,
  SCOPE_FIT,
  TEMPORAL_COVERAGE,
  PROVENANCE_INTEGRITY,
  DETECTABILITY,
  CAUSAL_IDENTIFICATION,
  EVIDENCE_DEPENDENCY
)
```

注意：

```text
F
!=
NUMERIC SCORE
```

輸出是：

```text
allowed target
allowed claim type
allowed epistemic mode
allowed scope
allowed time
allowed causal strength
allowed certainty language
required corroboration
required detectability
required causal identification
explicit gaps
prohibited upgrades
```

---

# 18｜First Failure Modes

```text
EIB-01
REPORT-TARGET / UNDERLYING-TARGET COLLAPSE

EIB-02
SELF-REPORT TO DIRECT-OBSERVATION LAUNDERING

EIB-03
SELF-REPORT TO PROCESS-VERIFICATION LAUNDERING

EIB-04
SELF-REPORT NEGATIVE-CLAIM INFLATION

EIB-05
SELF-REPORT CAUSALITY INFLATION

EIB-06
SAME-ORIGIN REPETITION
TO
FALSE CORROBORATION

EIB-07
INSTRUMENTED
TO
INFALLIBLE
LAUNDERING

EIB-08
RECORD EXISTS
TO
PROCESS VERIFIED
LAUNDERING
```

---


# 19｜Open Questions

```text
OPEN_1:
  MODEL_SELF_REPORT profile
  是否需要依 model capability / interface
  區分 declared first-person access vs no-access?
  STATUS: OPEN

OPEN_2:
  OWNER_RETURN
  已重新分類為 contract / carrier / issuer role
  非 evidence origin
  NEXT QUESTION:
    evidentiary force vs constitutive force
  STATUS: READY

OPEN_3:
  PROVIDER_RECEIPT
  對 execution / delivery / billing / transport
  各自 target fidelity 如何分？
  STATUS: NEXT_AFTER_OWNER_RETURN

OPEN_4:
  HOST_INSTRUMENTATION
  是否需要 instrument class registry？
  STATUS: OPEN

OPEN_5:
  STATE_READBACK
  對 event occurrence 是 direct evidence、
  derived evidence、還是 post-state evidence？
  STATUS: OPEN

OPEN_6:
  NEGATIVE CLAIM
  detectability profile 是否需 domain-specific sensitivity？
  STATUS: OPEN

OPEN_7:
  CAUSAL CLAIM
  哪些 runtime intervention event
  可建立最低 causal-identification profile？
  STATUS: OPEN
```

---


# 20｜V0.1.1 Standing

```text
EVIDENCE / INSTRUMENTATION BOUNDARY REVIEW V0.1.1-WORKING

MATRIX SHAPE
=
PASS

SCALAR LADDER
=
REJECTED

CLAIM CEILING
/
ADDITIONAL QUALIFICATION
TYPE SEPARATION
=
PASS

MODEL_SELF_REPORT
REPORT-TARGET STANDING
=
PASS

MODEL_SELF_REPORT
UNDERLYING EVENT CEILING
=
PASS

MODEL_SELF_REPORT
PROCESS CLAIM CEILING
=
PASS

MODEL_SELF_REPORT
NEGATIVE CLAIM CEILING
=
PASS

MODEL_SELF_REPORT
CAUSAL CLAIM CEILING
=
PASS

OWNER_RETURN
AS EVIDENCE ORIGIN
=
REJECTED

OWNER_RETURN
AS CONTRACT / CARRIER / ISSUER ROLE
=
READY FOR REVIEW

ANTI-STANDING-LAUNDERING
=
PASS IN FIRST ADVERSARIAL ORIGIN

HOST / PROVIDER /
STATE-READBACK PROFILES
=
OPEN

RUNTIME RATIFICATION
=
HOLD
```

---


# 21｜下一輪

下一輪不再把 OWNER_RETURN 放在 evidence-origin axis 上。

正確入口：

```text
OWNER_RETURN
=
CONTRACT / CARRIER / ISSUER ROLE
```

先拆：

```text
EVIDENTIARY FORCE
!=
CONSTITUTIVE / NORMATIVE FORCE
```

再撞：

```text
1. MAIN ACTUAL-STATE RETURN
2. L7 MANIFESTATION QUALIFICATION RETURN
3. GOVERNANCE / ADMISSION RETURN
4. DESCRIPTIVE OWNER RETURN
```

核心問題：

```text
OWNER HAS AUTHORITY
!=
OWNER HAS EPISTEMIC ACCESS

VALID OWNER RETURN
!=
ALL PAYLOAD CLAIMS ARE TRUE
```

---

# 22｜最短根句

```text
A MODEL REPORT
CAN STRONGLY PROVE
WHAT THE MODEL REPORTED.

IT DOES NOT THEREFORE
PROVE THE HIDDEN PROCESS.

A REPORT OF ABSENCE
IS NOT
EMPIRICAL NONOCCURRENCE.

AN EVENT REPORT
IS NOT
CAUSAL IDENTIFICATION.

THE MATRIX DOES NOT RANK EVIDENCE.
IT LIMITS CLAIMS.

THE QUESTION IS NOT:
"HOW STRONG IS THIS EVIDENCE?"

THE QUESTION IS:
"WHAT EXACTLY MAY THIS EVIDENCE
LEGALLY SUPPORT?"
```

---

# 23｜一句話收束

> **Evidence Boundary Table 的功能不是替 evidence 排階級，而是阻止 evidence 在跨 target、跨 claim type、跨 scope、跨 time、跨 causality 時偷偷變強。**
