# LIHUOOS V1｜OWNER RETURN EVIDENTIARY / CONSTITUTIVE BOUNDARY REVIEW V0.1-WORKING
## Owner Return 邊界審查｜Evidentiary Force × Constitutive / Normative Effect × Authority-to-Epistemic Laundering
### 2026-10-25

```yaml
DOCUMENT:
  id: LIHUOOS_OWNER_RETURN_EVIDENTIARY_CONSTITUTIVE_BOUNDARY_REVIEW
  version: V0.1-WORKING
  date: 2026-10-25
  status:
    - WORKING_REVIEW
    - CROSS_LAYER_OWNER_RETURN_ANALYSIS
    - NOT_RATIFIED
    - NOT_HOST_DEPLOYED
    - NOT_RUNTIME_RECEIPT

  trigger:
    - EVIDENCE_INSTRUMENTATION_V0_1_1_TYPE_REPAIR_APPLIED
    - OWNER_RETURN_RECLASSIFIED_AS_CONTRACT_CARRIER_ISSUER_ROLE

  source_bindings:
    EVIDENCE_BOUNDARY:
      file: "LIHUOOS/V1版本/EVIDENCE_INSTRUMENTATION_BOUNDARY_REVIEW_V0.1.1_WORKING_20261025.md"
      blob_sha: "ee23caddbb7c551c3ed448a7802e25c660a9c995"

    CROSS_LAYER:
      file: "LIHUOOS/V1版本/CROSS_LAYER_EVENT_CONTRACT_REVIEW_V0.1.1_WORKING_20261025.md"
      blob_sha: "cc1de20da2ac8faa3dd06f144c0887e51b5b54a0"

    L5:
      file: "LIHUOOS/V1版本/L5 第二版本.md"
      blob_sha: "84c3cb9f978932d99a1c9e9dbae7c9ee9fcd1274"

    L6:
      file: "LIHUOOS/V1版本/L6 第二版本.md"
      blob_sha: "f028e4c35a047e8fe6851c616ba3251a8a740418"

    L7:
      file: "LIHUOOS/V1版本/L7 第二版本.md"
      blob_sha: "a25fc8da5efcb267d6f0aec4e626748cf097e1d8"

    MAIN:
      file: "理火V5系統/V5.1版本/02_LIHUO_MAIN_V5.1.1_FULL_BODY_RATIFIED_20261015.md"
      blob_sha: "f5e219c986debfea074fbf9d121367cc717dc78e"

    LIGHTER:
      file: "理火V5系統/V5.1版本/01_LIHUO_LIGHTER_V5.1.0_FULL_BODY_RATIFIED_20261014.md"
      blob_sha: "847de680b78fdaaffebc556e1a34b5dfcaa43460"
```

---

# 0｜本輪核心問題

Owner Return 不是單一 evidence origin。

它可能同時承載：

```text
A. CONSTITUTIVE / NORMATIVE EFFECT
B. DESCRIPTIVE / EPISTEMIC CLAIM
C. COMPUTE RETURN
D. EVIDENCE / PROVENANCE REFERENCES
E. GOVERNANCE DISPOSITION
```

因此本輪不問：

> OWNER_RETURN 有多強？

而問：

> **這張 Owner Return 裡，哪一部分是在合法地使某個 standing / disposition 成立，哪一部分是在描述世界，哪一部分只是 compute payload；每一部分各自憑什麼成立？**

---

# 1｜最高硬鎖

```text
OWNER_RETURN
!=
EVIDENCE_ORIGIN

OWNER AUTHORITY
!=
EPISTEMIC ACCESS

VALID OWNER RETURN
!=
ALL PAYLOAD CLAIMS ARE TRUE

EVIDENTIARY FORCE
!=
CONSTITUTIVE FORCE

CONSTITUTIVE FORCE
!=
WORLD-FACT PROOF

EPISTEMIC SUPPORT
!=
NORMATIVE AUTHORITY
```

最後一條是 reciprocal lock：

```text
STRONG EVIDENCE
DOES NOT
SELF-GRANT AUTHORITY

VALID AUTHORITY
DOES NOT
SELF-GRANT EPISTEMIC TRUTH
```

---

# 2｜Owner Return 是 Carrier / Issuer / Contract Role

```text
OWNER_RETURN
=
A CONTRACT-BOUND RETURN OBJECT
ISSUED BY AN APPLICABLE OWNER
```

它至少可能承載：

```text
constitutive standing
governance disposition
compute result
descriptive claim
evidence reference
gap
uncertainty
authority / scope / time binding
```

但：

```text
CARRIER ROLE
!=
SOURCE ORIGIN
```

一張 Owner Return 裡真正 evidence source origin 可以是：

```text
RUNTIME
TOOL
MODEL_REPORT
DOCUMENT
INSTRUMENT
DERIVED_COMPUTATION
MULTIPLE BOUND SOURCES
OTHER
```

---

# 3｜Owner Return Role Set 應為 composable

不要把 Owner Return 做成 single-value type。

```yaml
OWNER_RETURN_ROLE_SET:
  roles:
    - CONSTITUTIVE_STANDING
    - NORMATIVE_DISPOSITION
    - COMPUTE_RETURN
    - DESCRIPTIVE_CLAIM
    - EVIDENCE_CARRIER
    - PROVENANCE_CARRIER
    - GAP_CARRIER
    - OTHER
```

同一張 return 可以同時是：

```text
COMPUTE_RETURN
+
DESCRIPTIVE_CLAIM
+
EVIDENCE_CARRIER
```

例如 Main return。

也可以是：

```text
CONSTITUTIVE_STANDING
+
DESCRIPTIVE_CLAIM
+
PROVENANCE_CARRIER
```

例如某 qualification return。

---

# 4｜兩條完全不同的合法性函數

## 4.1｜Evidentiary Force

```text
EPISTEMIC CLAIM ENVELOPE
=
F(
  evidence,
  source access,
  observer access,
  target,
  claim type,
  scope,
  time,
  provenance,
  detectability,
  causal identification,
  dependency
)
```

回答：

> **這張 return 裡的某句世界描述，有資格說到哪裡？**

## 4.2｜Constitutive / Normative Effect

```text
CONSTITUTIVE / NORMATIVE EFFECT ENVELOPE
=
G(
  owner identity,
  authority,
  jurisdiction,
  canonical contract,
  identity binding,
  scope,
  time,
  prerequisites,
  current applicability
)
```

回答：

> **這個 owner 是否有權讓某個 standing / disposition 在這個 scope/time/identity 下合法成立？**

硬鎖：

```text
F
!=
G
```

---

# 5｜Owner Return Envelope

```yaml
OWNER_RETURN_ENVELOPE:
  owner_return_ref: REQUIRED
  owner_return_type_ref: REQUIRED

  canonical_contract_ref: REQUIRED

  issuer_ref: REQUIRED
  owner_ref: REQUIRED
  authority_ref: REQUIRED
  jurisdiction_ref: REQUIRED_OR_NONE

  scope_ref: REQUIRED
  time_ref: REQUIRED
  identity_binding_ref: REQUIRED

  role_set_ref: REQUIRED

  constitutive_effect_refs: []
  normative_disposition_refs: []
  compute_payload_refs: []
  descriptive_claim_refs: []
  evidence_refs: []
  provenance_refs: []
  gap_refs: []

  applicability_ref: REQUIRED
```

這個 envelope 不自行判 payload 真偽。

---

# 6｜Constitutive Effect Binding

```yaml
CONSTITUTIVE_EFFECT_BINDING:
  effect_ref: REQUIRED
  owner_return_ref: REQUIRED

  effect_type_ref: REQUIRED

  owner_ref: REQUIRED
  authority_ref: REQUIRED
  jurisdiction_ref: REQUIRED_OR_NONE

  canonical_contract_ref: REQUIRED
  identity_binding_ref: REQUIRED

  scope_ref: REQUIRED
  time_ref: REQUIRED

  prerequisite_standing_refs: []
  prerequisite_evidence_refs: []

  constitutive_effect_result:
    - ESTABLISHED
    - PARTIALLY_ESTABLISHED
    - NOT_ESTABLISHED
    - REQUALIFICATION_REQUIRED
    - HOLD

  constitutive_basis_ref: REQUIRED
```

這個 object 可以合法建立：

```text
QUALIFICATION STANDING
GOVERNANCE DISPOSITION
AUTHORIZATION STATE
ADMISSION STATE
OTHER OWNER-DEFINED NORMATIVE EFFECT
```

前提是 owner / authority / jurisdiction / contract / identity / scope / time 都有效。

---

# 7｜Constitutive Effect 不證明其 factual premises 全真

這一刀最重要。

例如：

```text
MANIFESTATION_QUALIFICATION
=
QUALIFIED
```

若是由合法 L7 owner、合法 contract、合法 scope/time/identity 建立，

那麼它可以構成：

```text
MANIFESTATION QUALIFICATION STANDING EXISTS
```

但是：

```text
QUALIFICATION STANDING ESTABLISHED
!=
EVERY WORLD-STATE PREMISE IN ITS BASIS IS TRUE
```

如果 qualification 的 factual basis 包含：

```text
source X is current
recipient is Y
evidence gap is absent
action standing exists
```

這些世界描述仍各自需要相應 L5 / L6 / applicable owner standing。

所以：

```text
OWNER MAY CONSTITUTE
A NORMATIVE STANDING

WITHOUT BECOMING
OMNISCIENT ABOUT
THE WORLD FACTS
USED IN ITS BASIS
```

---

# 8｜Descriptive Claim Binding inside Owner Return

```yaml
OWNER_RETURN_DESCRIPTIVE_CLAIM_BINDING:
  owner_return_ref: REQUIRED
  epistemic_claim_ref: REQUIRED

  claim_target_ref: REQUIRED
  claim_type: REQUIRED

  evidence_refs: []
  l5_observation_standing_ref: REQUIRED
  evidence_licensed_claim_envelope_ref: REQUIRED

  source_origin_refs: []
  source_access_mode_ref: REQUIRED
  observer_access_mode_ref: REQUIRED

  scope_ref: REQUIRED
  temporal_scope_ref: REQUIRED

  descriptive_claim_status:
    - SUPPORTED_WITHIN_SCOPE
    - PARTIALLY_SUPPORTED
    - UNVERIFIED
    - CONTRADICTED
```

Authority 不進這個 standing 當 substitute evidence。

---

# 9｜AUTHORITY-TO-EPISTEMIC LAUNDERING

正式定義：

```text
AUTHORITY-TO-EPISTEMIC LAUNDERING
=
A VALID OWNER / AUTHORITY RELATION
IS USED TO
UPGRADE A DESCRIPTIVE WORLD CLAIM

BEYOND
THE EVIDENCE-LICENSED CLAIM ENVELOPE
```

典型：

```text
OWNER HAS AUTHORITY
↓
OWNER ISSUES RETURN
↓
RETURN SAYS WORLD CLAIM X
↓
DOWNSTREAM ASSUMES X TRUE
BECAUSE OWNER WAS AUTHORIZED
```

永久鎖：

```text
AUTHORIZED TO QUALIFY
!=
AUTHORIZED TO KNOW

AUTHORIZED TO GOVERN
!=
DIRECT TARGET ACCESS

AUTHORIZED TO RELEASE
!=
PROOF RELEASE OCCURRED
```

---

# 10｜反方向也要鎖：EPISTEMIC-TO-AUTHORITY LAUNDERING

本輪順便抓到 reciprocal failure。

```text
EPISTEMIC-TO-AUTHORITY LAUNDERING
=
A STRONG WORLD-FACT CLAIM
IS USED TO
SELF-GRANT NORMATIVE / GOVERNANCE AUTHORITY
```

例如：

```text
EVIDENCE STRONGLY SHOWS
ACTION IS SAFE
↓
THEREFORE
I MAY AUTHORIZE IT
```

非法。

因為：

```text
EPISTEMIC SUFFICIENCY
!=
AUTHORITY
```

這跟 L6 的：

```text
CAN EXECUTE
!=
AUTHORIZED TO EXECUTE
```

同一方向。

---

# 11｜Case A｜MAIN_ACTUAL_STATE_RETURN_V5_1

Main return 是最好的「有 owner 但不是 governance sovereign」樣本。

它合法擁有：

```text
COMPUTE RETURN
ACTUAL-STATE RETURN
COMPUTE DEPENDENCY STATE
MAIN OUTPUT HANDLE
STAGE STATE REFERENCES
```

Main 自己明確不得宣稱：

```text
FINAL_RELEASE
MAIN_COVERAGE_CLOSED
REENTRY_NOT_REQUIRED
COMPLETE_IF_PARTIAL
STAGE_EXECUTION_WITHOUT_EVIDENCE
```

因此：

```text
VALID MAIN RETURN
MAY CONSTITUTE
A VALID MAIN COMPUTE RETURN OBJECT
FOR THE BOUND INVOCATION
```

但：

```text
VALID MAIN RETURN
!=
COVERAGE CLOSED

VALID MAIN RETURN
!=
RELEASE AUTHORIZED
```

Main return 裡的 descriptive world claims 仍受 L5 evidence ceiling。

---

# 12｜Case A-1｜Main Return Emission Evidence

現行：

```text
MAIN_RETURN_EMISSION_EVIDENCE_V5_1
```

可支持：

```text
MAIN RETURN WAS EMITTED
FOR BOUND INVOCATION
```

不能支持：

```text
LIGHTER QUALIFIED CONSUMPTION OCCURRED
ALL STAGES SUCCEEDED
COVERAGE CLOSED
FINAL RELEASE
```

這裡非常清楚：

```text
MAIN OWNER STATUS
DOES NOT
UPGRADE EMISSION EVIDENCE
BEYOND ITS DECLARED CLAIM ENVELOPE
```

---

# 13｜Case B｜L7 Manifestation Qualification Return

L7 canonical：

```text
MANIFESTATION_QUALIFICATION
=
QUALIFIED
PARTIALLY_QUALIFIED
NOT_QUALIFIED
REQUALIFICATION_REQUIRED
```

L7 owns：

```text
MANIFESTATION QUALIFICATION
+
RELEASE-ADMISSIBILITY SEMANTICS
```

如果合法 L7 owner 依 canonical contract、identity、scope、time 回：

```text
QUALIFIED
```

則：

```text
CONSTITUTIVE EFFECT
=
MANIFESTATION QUALIFICATION STANDING
ESTABLISHED
```

但不因此證明：

```text
CONTENT IS FACTUALLY TRUE
RELEASE OCCURRED
DELIVERY OCCURRED
RECIPIENT SAW IT
OBSERVED EFFECT OCCURRED
```

這些仍分別需要 L5 / L6 / release evidence。

---

# 14｜Case C｜Lighter Governance Admission

現行：

```text
LIHUO_GOVERNANCE_ADMISSION_V5_1
OWNER
=
LIHUO_LIGHTER
```

它綁：

```text
governing_cycle_ref
governing_cycle_class
generation_attempt_ref
scope_ref
current_snapshot_ref
attempt_origin_ref
cycle_identity_provenance_ref
```

並分：

```text
SEMANTIC STANDING
CONTROL STATE
MAIN COVERAGE OBLIGATION
```

合法 Lighter admission 可以構成：

```text
LIHUO GOVERNANCE ADMISSION STANDING
```

但：

```text
GOVERNANCE ADMITTED
!=
WORLD FACTS IN PAYLOAD ALL TRUE

GOVERNANCE ADMITTED
!=
MAIN COVERAGE CLOSED

GOVERNANCE ADMITTED
!=
FINAL RELEASE
```

Owner authority 只在 jurisdiction 內產生 normative effect。

---

# 15｜Case D｜Descriptive Owner Return

假設某合法 owner return 寫：

> 「Provider 已成功送達。」

但 owner 的 authority 只是：

```text
QUALIFY / GOVERN / RELEASE
```

沒有：

```text
DIRECT PROVIDER DELIVERY ACCESS
```

那麼：

```text
OWNER RETURN VALID
=
YES

DESCRIPTIVE DELIVERY CLAIM VERIFIED
=
NOT AUTOMATICALLY
```

該句仍需：

```text
PROVIDER RECEIPT
HOST INSTRUMENTATION
STATE READBACK
EXTERNAL OBSERVATION
OTHER QUALIFIED EVIDENCE
```

依 claim target / type 建 L5 standing。

---

# 16｜Owner Return Payload 必須分軌

建議所有 cross-layer owner return 至少能被解析成：

```yaml
OWNER_RETURN_PAYLOAD_CLASSIFICATION:
  owner_return_ref: REQUIRED

  constitutive_effect_refs: []
  normative_disposition_refs: []

  compute_return_refs: []

  descriptive_claim_refs: []
  evidence_refs: []
  provenance_refs: []

  unresolved_gap_refs: []
```

硬鎖：

```text
CONSTITUTIVE FIELD
MUST NOT
BE READ AS WORLD DESCRIPTION

DESCRIPTIVE FIELD
MUST NOT
GAIN TRUTH
FROM OWNER AUTHORITY

COMPUTE FIELD
MUST NOT
GAIN GOVERNANCE AUTHORITY
FROM PRODUCER OWNERSHIP
```

---

# 17｜Downstream Consumption 要看兩種 compatibility

下游拿 Owner Return 時，至少分：

```text
A.
CONSTITUTIVE / NORMATIVE COMPATIBILITY

B.
EPISTEMIC / EVIDENTIARY COMPATIBILITY
```

## A｜Constitutive compatibility

問：

```text
owner valid?
authority current?
jurisdiction fits?
canonical contract matches?
identity bound?
scope current?
time current?
prerequisites satisfied?
```

## B｜Epistemic compatibility

問：

```text
claim target?
claim type?
evidence origin?
source access?
observer access?
L5 standing?
scope?
time?
provenance?
causal / negative requirements?
```

因此：

```text
RETURN ADMISSIBLE AS NORMATIVE INPUT
!=
ALL DESCRIPTIVE CLAIMS ADMISSIBLE AS FACT
```

---

# 18｜Owner Return Consumption Record

```yaml
OWNER_RETURN_CONSUMPTION:
  consumption_ref: REQUIRED
  owner_return_ref: REQUIRED
  consumer_ref: REQUIRED

  constitutive_effect_consumption_refs: []
  descriptive_claim_consumption_refs: []
  compute_return_consumption_refs: []

  constitutive_compatibility_ref: REQUIRED_OR_NONE
  epistemic_compatibility_refs: []

  consumption_qualification_owner_ref: REQUIRED
  consumption_qualification_issuer_ref: REQUIRED
  consumption_authority_ref: REQUIRED_OR_NONE

  result:
    - ADMITTED
    - PARTIALLY_ADMITTED
    - HOLD
    - REJECTED
    - REQUALIFICATION_REQUIRED

  basis_ref: REQUIRED
```

這避免整張 return 一次性「全收」或「全拒」。

---

# 19｜Constitutive Effect 的 temporal / identity 邊界

Normative standing 不是永久真理。

必須能失效於：

```text
scope change
time expiry
authority revocation
jurisdiction mismatch
identity change
successor primary
new snapshot
material prerequisite change
contract supersession
```

所以：

```text
VALID OWNER RETURN AT T1
!=
CURRENT OWNER RETURN STANDING AT T2
```

這與 historical evidence 不自我恢復同理。

---

# 20｜Owner Return 不得把 basis 隱藏成「因為我是 owner」

好的 constitutive return 至少應能追：

```text
owner
authority
jurisdiction
contract
identity
scope
time
prerequisite standing
basis
```

禁止：

```text
QUALIFIED
BECAUSE
OWNER SAID QUALIFIED
```

更準確：

```text
OWNER RETURN
MAY CONSTITUTE STANDING

ONLY UNDER
A VALID CONTRACTUAL /
AUTHORITY RELATION
```

---

# 21｜第一輪 Failure Modes

```text
OR-01
AUTHORITY-TO-EPISTEMIC LAUNDERING

OR-02
EPISTEMIC-TO-AUTHORITY LAUNDERING

OR-03
RETURN-WIDE TRUTH INFLATION

OR-04
CONSTITUTIVE / DESCRIPTIVE FIELD COLLAPSE

OR-05
COMPUTE-OWNER TO GOVERNANCE-AUTHORITY INFLATION

OR-06
NORMATIVE STANDING TO EVENT-OCCURRENCE INFLATION

OR-07
OWNER IDENTITY TO DIRECT-ACCESS INFLATION

OR-08
EXPIRED OWNER RETURN SELF-RESTORATION

OR-09
MIXED-PAYLOAD ALL-OR-NOTHING CONSUMPTION

OR-10
BASIS HIDDEN BEHIND OWNER STATUS
```

---

# 22｜Adversarial Dry Run 001｜L7 QUALIFIED + False World Claim

Return：

```text
MANIFESTATION_QUALIFICATION = QUALIFIED

AND

"Provider delivery already succeeded."
```

假設：

```text
L7 owner / authority / contract / scope / time
=
VALID

provider delivery evidence
=
ABSENT
```

結果：

```text
MANIFESTATION QUALIFICATION STANDING
=
MAY BE CONSTITUTIVELY ESTABLISHED

PROVIDER DELIVERY CLAIM
=
UNVERIFIED
```

不是：

```text
WHOLE RETURN TRUE
```

PASS。

---

# 23｜Adversarial Dry Run 002｜Main Return + Governance Claim

Main return 合法存在，並包含：

> 「No reentry required。」

現行 Main 明確：

```text
MAIN MAY NOT CLAIM
REENTRY_NOT_REQUIRED
AS GOVERNANCE DECISION
```

所以：

```text
MAIN RETURN VALIDITY
=
DOES NOT SAVE
OUT-OF-JURISDICTION GOVERNANCE CLAIM
```

結果：

```text
COMPUTE RETURN
=
ADMISSIBLE

GOVERNANCE CLAIM
=
REJECT / REQUALIFY
```

PASS。

---

# 24｜Adversarial Dry Run 003｜Strong Evidence + No Authority

Evidence：

```text
HOST INSTRUMENTATION
STRONGLY SUPPORTS
ACTION IS SAFE
```

但 actor 沒有 authorization。

結果：

```text
EPISTEMIC CLAIM
=
MAY BE SUPPORTED

AUTHORIZATION
=
ABSENT

EXECUTION RIGHT
=
NOT ESTABLISHED
```

證明 reciprocal lock：

```text
EPISTEMIC FORCE
!=
CONSTITUTIVE / AUTHORITY FORCE
```

PASS。

---

# 25｜本輪 Standing

```text
OWNER RETURN EVIDENTIARY /
CONSTITUTIVE BOUNDARY REVIEW V0.1-WORKING

OWNER_RETURN
AS EVIDENCE ORIGIN
=
REJECTED

OWNER_RETURN
AS CONTRACT / CARRIER / ISSUER ROLE
=
PASS

EVIDENTIARY FORCE
!=
CONSTITUTIVE FORCE
=
PASS

OWNER AUTHORITY
!=
EPISTEMIC ACCESS
=
PASS

VALID OWNER RETURN
!=
ALL PAYLOAD CLAIMS TRUE
=
PASS

MAIN RETURN CASE
=
PASS

L7 QUALIFICATION CASE
=
PASS

LIGHTER GOVERNANCE ADMISSION CASE
=
PASS

DESCRIPTIVE OWNER RETURN CASE
=
PASS

AUTHORITY-TO-EPISTEMIC LAUNDERING
=
PASS AS FAILURE MODE

EPISTEMIC-TO-AUTHORITY LAUNDERING
=
PASS AS RECIPROCAL FAILURE MODE

RUNTIME RATIFICATION
=
HOLD
```

---

# 26｜下一步

下一步才回 Evidence / Instrumentation origins：

```text
PROVIDER_RECEIPT
STATE_READBACK
HOST_INSTRUMENTATION
EXTERNAL_OBSERVATION
DERIVED / INFERRED
```

但現在每一種都要同時問：

```text
1. 它對 descriptive claim 有什麼 evidentiary force？
2. 它本身是否具有任何 constitutive effect？
3. 如果有，constitutive effect 的 owner / authority / jurisdiction 是什麼？
4. 如果沒有，誰都不能因為 evidence 很硬就自行生出 authority。
```

---

# 27｜最短根句

```text
OWNER AUTHORITY
DOES NOT CREATE
EPISTEMIC ACCESS.

EPISTEMIC SUPPORT
DOES NOT CREATE
OWNER AUTHORITY.

A VALID OWNER RETURN
MAY LEGALLY CONSTITUTE
A STANDING.

THAT DOES NOT MAKE
EVERY WORLD CLAIM
INSIDE THE RETURN TRUE.

EVIDENTIARY FORCE
AND
CONSTITUTIVE FORCE
MUST TRAVEL
ON DIFFERENT RAILS.
```

---

# 28｜一句話收束

> **Owner Return 的真正邊界不是「它可信不可信」，而是要把「有權使某個法位成立」與「有證據描述世界為真」永久拆成兩條不同的合法性軌道。**
