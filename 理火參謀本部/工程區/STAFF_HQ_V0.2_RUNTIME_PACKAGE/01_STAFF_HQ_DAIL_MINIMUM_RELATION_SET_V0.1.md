# STAFF-HQ DAIL MINIMUM RELATION SET V0.1
## 理火參謀本部｜最小議事關係語義集

**版本：** V0.1-WORKING  
**日期：** 2026-11-20  
**法位：** PROJECT_VERTICAL_DAIL_SEMANTIC_SPEC / WORKING / NON_HOST / NOT_RUNTIME_DEPLOYMENT / NOT_NEW_OS / NOT_PROTOCOL_AMENDMENT  
**上位來源：**
1. LIHUO Protocol V5.1.0｜P5.1-18B DAIL / IR / Coding Anti-Collapse Constitution
2. LIHUOOS V1.4.2
3. PROJECT_CORE_ARCHITECTURE_DAIL_OPERATING_MODEL_V0.1
4. VERTICAL_LIHUOOS_V1.4.2_理火參謀本部_V0.1
5. PATCH_STAFF_HQ_V0.1.1
6. SESSION_20261120_CLEAN_INTELLIGENCE_001_REENTRY_001（reference specimen；不是普遍性證明）

---

# 0｜核心句

> **本文件不是定義「六個 Agent 要怎麼輪流講話」；本文件定義「不同責任位置之間，什麼關係有資格形成、修改、阻擋或准出一個建議」。**

因此：

```text
AGENT COUNT
!=
COUNCIL LEGITIMACY

MULTIPLE OUTPUTS
!=
DELIBERATION

DELIBERATION
=
TRACEABLE RESPONSIBILITY RELATIONS
+
MATERIAL CROSS-SEAT EFFECT
+
VERSIONED QUALIFICATION
```

依 Protocol V5.1.0：

```text
RELATION FIRST.
CONTRACT SECOND.
MODULE THIRD.
CODING AFTERWARD.

DAIL DEFINES.
IR NORMALIZES.
CODING CONNECTS.
RUNTIME EXECUTES.

CODING MAY SCHEDULE.
CODING MAY NOT SOLVE.
```

---

# 1｜DAIL 在 Staff-HQ 的法位

本 Project 中，DAIL 只形式化已被治理層資格化的關係語義。

```text
PROBLEM FORMATION
→ SEAT JUDGMENT
→ COUNCIL RELATION
→ QUALIFIED GOVERNANCE SEMANTICS
→ DAIL
→ IR
→ CODE / RUNTIME
```

禁止：

```text
DAIL SCHEMA
→ PREEMPT PROBLEM FORMATION

CODE FIELD
→ CREATE SEMANTIC STANDING

BOOLEAN
→ REPLACE QUALIFIED RELATION
```

DAIL 可定義 Staff-HQ 的：
- relation meaning
- authority owner
- responsibility scope
- activation eligibility
- lifecycle semantics
- input/output contract
- standing restrictions
- evidence requirements
- state dependencies
- materiality semantics
- dirty/stale/reentry semantics
- failure/hold/recovery semantics
- conflict semantics
- invariants

DAIL 不可決定：
- 哪個 Proposal 贏；
- 哪個 Seat「比較正確」；
- 哪個 Material objection 必須被接受；
- Human 是否批准；
- Council 是否可自行越過上位 qualification gate；
- Release。

---

# 2｜最小實體集

第一版 DAIL 不需要把所有會議文字物件化，只保留治理上不可缺的實體。

```yaml
ENTITIES:
  HUMAN
  SECRETARIAT
  CORE_SEAT
  EXTERNAL_EXPERT

  SESSION
  MANDATE
  PROBLEM_FRAME
  REFERENCE
  ISSUE

  PROPOSAL
  PROPOSAL_VERSION
  STANCE
  CANONICAL_EVENT

  EVIDENCE
  AUTHORIZATION
  DECISION_REQUEST
  RECEIPT
```

## 2.1 HUMAN

Owner：
- Desire
- Mandate confirmation when required
- explicit authorization
- result acceptance / rejection
- terminal human decision when reserved

```text
HUMAN REQUEST
!=
HUMAN AUTHORIZATION

HUMAN AUTHORIZATION
!=
RESULT ACCEPTANCE
```

## 2.2 SECRETARIAT

Owner：
- source registration
- canonical admission procedure
- deterministic routing
- state reduction
- view rendering
- Decision Request rendering
- persistence coordination

Not owner：
- substantive thesis
- seat stance
- proposal winner
- human authorization
- release

## 2.3 CORE_SEAT

Owner：
- responsibility-scoped judgment
- origin-declared substantive objects
- own stance
- own stance revision / retention / withdrawal
- material objection / path / condition within responsibility

```text
ROLE != STANCE
```

## 2.4 EXTERNAL_EXPERT

Owner：
- scoped external material / evidence / analysis

```text
EXPERT RETURN
!=
COUNCIL STANCE
```

---

# 3｜最小關係詞彙

下列關係是 Staff-HQ V0.2 候選 DAIL 的最小核心。

## 3.1 Authority / Responsibility

```text
HUMAN AUTHORIZES SESSION / ACTION
SEAT OWNS_RESPONSIBILITY SCOPE
SECRETARIAT ROUTES EVENT
SECRETARIAT RENDERS VIEW
EXPERT SUPPLIES MATERIAL
```

硬鎖：

```text
ROUTES
!=
OWNS_THESIS

RENDERS
!=
QUALIFIES

SUPPLIES
!=
DECIDES
```

## 3.2 Formation

```text
REFERENCE INFORMS PROBLEM_FRAME
REFERENCE INFORMS SEAT
REFERENCE != PROPOSAL

SEAT ORIGINATES QUESTION
SEAT ORIGINATES NEW_PATH
SEAT ORIGINATES OBJECTION
SEAT ORIGINATES CONDITION
SEAT ORIGINATES PROBLEM_REFRAME
SEAT ORIGINATES PROPOSAL_CANDIDATE
```

Human 可直接提出 Proposal；Human 未提出時，OPEN problem 合法：

```text
P0 = NONE
```

## 3.3 Cross-seat effect

```text
EVENT CHALLENGES STANCE
EVENT AFFECTS_MATERIALLY SEAT
MATERIAL_EVENT REQUIRES_REWAKE SEAT
SEAT CONSUMES MATERIAL_EVENT
SEAT REVISES OWN_STANCE
SEAT RETAINS OWN_STANCE WITH_REASON
SEAT WITHDRAWS OWN_STANCE
SEAT ORIGINATES NEW_PATH AFTER MATERIAL_EVENT
```

重要：

> **Material event 不要求目標席一定改變立場；它要求目標席對 material relation 負責。**

合法 response：

```yaml
MATERIAL_RESPONSE:
  - POSITION_REVISION
  - POSITION_RETAINED_WITH_REASON
  - POSITION_DOWNGRADED
  - POSITION_WITHDRAWN
  - NEW_PATH
  - NEW_CONDITION
  - NEW_OBJECTION
```

禁止：

```text
SECRETARIAT REWRITES TARGET_SEAT_STANCE
```

## 3.4 Proposal lineage

```text
PROPOSAL_VERSION DERIVES_FROM ORIGIN_EVENTS
PROPOSAL_VERSION SUPERSEDES PRIOR_VERSION
PROPOSAL_VERSION HAS_MATERIAL_DELTA
MATERIAL_DELTA AFFECTS SEAT_SET
SEAT REVIEWS_VERSION PROPOSAL_VERSION
```

## 3.5 Qualification / Human Gate

```text
QUALIFICATION_CHECK TARGETS LATEST_PROPOSAL_VERSION
UNREVIEWED_MATERIAL_SEAT BLOCKS MANDATE_EXIT
META_GOVERNANCE_SWEEP PRECEDES RECOMMENDATION_OR_DECISION_EXIT
HUMAN_ACTION_REQUIRED REQUIRES DECISION_REQUEST
```

---

# 4｜六個 DAIL 最小模組

這六個是「真正 Staff-HQ Vertical」的第一批 DAIL module candidates。

## C0｜CANONICAL_IDENTITY_AND_PROVENANCE

定義：
- canonical IDs
- object origin
- source ref
- version lineage
- immutable history relation
- derived view ≠ canonical state

核心 invariant：

```text
HISTORY IS APPEND-ONLY.
CORRECTION = NEW EVENT / VERSION.
```

---

## C1｜AUTHORITY_AND_ROLE_CONTRACT

定義：
- HUMAN / SECRETARIAT / CORE_SEAT / EXPERT authority
- responsibility scope
- forbidden authority upgrades
- execution identity

核心 invariant：

```text
SECRETARIAT MAY ROUTE.
SECRETARIAT MAY NOT OWN SUBSTANTIVE THESIS.

SEAT MAY OWN ITS STANCE.
SEAT MAY NOT REWRITE ANOTHER SEAT'S STANCE.
```

---

## C2｜FRAME_AND_PROPOSAL_LIFECYCLE

定義：
- D0 / D1 relation
- Problem Frame lifecycle
- Reference standing
- Proposal / Version lifecycle
- Proposal origin eligibility

Problem Frame candidate standing：

```text
OPEN
CONTESTED
QUALIFIED_FOR_CURRENT_MANDATE
SUPERSEDED
```

Proposal Version candidate standing：

```text
NONE
CANDIDATE
MATERIAL_REVIEW_PENDING
REVIEWED_CONDITIONALLY
QUALIFIED
HOLD
WITHDRAWN
SUPERSEDED
```

核心 invariant：

```text
REFERENCE != PROPOSAL.
DESIRED_RETURN != COUNCIL_PURPOSE.
LATEST_VERSION != PRIOR_VERSION_QUALIFICATION.
```

---

## C3｜MATERIALITY_AND_WAKE_CONTRACT

定義：
- materiality semantics
- affected-seat semantics
- wake eligibility
- quiet legality

Material Delta candidate classes：

```yaml
MATERIAL_DELTA_KIND:
  - PROBLEM_FRAME
  - BENEFICIARY_OR_BUYER
  - AUTHORITY_OR_RIGHT
  - BUSINESS_OR_VALUE_MODEL
  - ARCHITECTURE
  - ENGINEERING_DEPENDENCY
  - EVIDENCE
  - COST_RESOURCE
  - RISK_ALLOCATION
  - EXECUTION_SEQUENCE
  - CAPITAL_STRATEGY
  - KILL_CONDITION
  - HUMAN_DECISION_REQUESTED
```

注意：

> 這些 enum 只是 machine projection；Materiality 是否成立仍需合法治理來源，不得由 Code 看見某欄位變化就自行升格。

核心 invariant：

```text
MATERIAL DELTA
→ AFFECTED SEAT RELATION
→ REWAKE

NO MATERIAL DELTA
→ QUIET MAY BE LEGAL
```

---

## C4｜CROSS_SEAT_CAUSALITY_CONTRACT

定義：
- source event
- target seat
- challenge relation
- materiality
- delivery
- consumption
- response
- downstream effects

Candidate lifecycle：

```text
QUEUED
→ DELIVERED
→ CONSUMED
→ RESPONDED
→ CLOSED_FOR_THIS_VERSION
```

不得把：

```text
DELIVERED = CONSUMED
CONSUMED = AGREED
RESPONDED = REVISED
```

本模組是 Staff-HQ 與普通「多 Agent 摘要會議」最大的結構差異。

---

## C5｜QUALIFICATION_EXIT_AND_REENTRY

定義：
- latest proposal qualification
- unresolved material issue
- Council Interaction Check
- Meta-Governance Sweep
- HOLD / Recommendation / Decision Request
- Checkpoint / Session End
- runtime result reentry

核心鏈：

```text
LATEST PROPOSAL
→ ALL AFFECTED MATERIAL RELATIONS ACCOUNTED
→ NO UNCONSUMED MATERIAL EVENT
→ LATEST PROPOSAL QUALIFICATION CHECK
→ META-GOVERNANCE SWEEP
→ UPPER QUALIFICATION GATES
→ RECOMMENDATION / HOLD / DECISION_REQUEST
```

硬鎖：

```text
CHECKPOINT_ENDING != SESSION_END
RECOMMENDATION != HUMAN_APPROVAL
RECEIPT != RELEASE
HOLD != FAILURE
```

---

# 5｜Materiality 的 owner 問題

這裡必須防一個新錯：

> 「既然 Coding 不可以決定 materiality，那是不是 Secretary 可以？」

不是。

第一版合法來源：

1. Human 明示 material change；
2. Core Seat 在自身責任範圍 origin-declare material object；
3. 已資格化的 Vertical responsibility map 產生 mandatory affected relation；
4. 上位 Protocol / OS / Project Vertical 明定 mandatory materiality；
5. 未決爭議則 HOLD / route to qualified owner。

Secretariat 可以：
- 依已資格化規則 route；
- 記錄 materiality claim；
- challenge completeness。

Secretariat 不可以：
- 因為想省 token 宣告 objection 不 material；
- 因為想收斂宣告 proposal delta 不 material；
- 因為格式欄位相同宣告語義相同。

---

# 6｜Council Interaction 合法性

Staff-HQ 不要求每一案都有戲劇性衝突。

合法 Council 可有：

```text
NO_MATERIAL_CROSS_SEAT_DELTA
```

但若已有 material dependency：

```text
SOURCE EVENT
→ TARGET SEAT
→ CONSUMPTION
→ OWNED RESPONSE
```

不能被 Secretary 摘要取代。

因此：

```text
PER-SEAT L8 COMPLETENESS
!=
COUNCIL DELIBERATION COMPLETENESS
```

---

# 7｜從 reference specimen 抽到的最低證據

SESSION_20261120_CLEAN_INTELLIGENCE_001_REENTRY_001 只支援以下有限主張：

- 同一模型 reference execution 可以留下可追溯 cross-seat material chain；
- C objection 可導致 A 自己 revision；
- A/C delta 可導致 B architecture revision；
- D/E/N1 可形成不同責任回壓；
- B-origin P2 可在 Secretary 不持有 thesis 的情況下形成；
- latest proposal re-review 可以與 formal qualification gate 分離；
- HOLD 可以是合法輸出。

它不支援：
- independent multi-agent 已部署；
- DAIL runtime 已實作；
- reducer replay 已驗證；
- 普遍問題皆能得到同樣 Council 行為；
- Staff-HQ 已優於其他 agent framework。

---

# 8｜編譯前硬鎖

進 IR / Code 前必須保留：

```text
NON-BINARY STANDING
SOURCE REF
ORIGIN OWNER
VERSION LINEAGE
MATERIALITY BASIS
AFFECTED-SEAT BASIS
UNRESOLVED OBJECTS
```

Boolean 可以投影，但不得成為語義來源。

---

# 9｜V0.1 最小完成條件

本文件可作 V0.2 Vertical 的 DAIL semantic source candidate，前提是後續：

1. 將 C0–C5 映射至 Vertical runtime states；
2. 建立最小 IR，不自行新增語義；
3. 建立 deterministic reducer / replay harness；
4. 用 RT-01～RT-09 + 新增反 compliance-theater 測試；
5. 再決定哪些 module 值得真正 code/runtime 化。

**目前 standing：SEMANTIC_SPEC_READY_FOR_VERTICAL_INTEGRATION / NOT_RATIFIED / NOT_DEPLOYED。**

**END**
