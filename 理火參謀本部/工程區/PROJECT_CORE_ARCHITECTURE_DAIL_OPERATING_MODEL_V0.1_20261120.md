# PROJECT CORE ARCHITECTURE｜理火參謀本部 × DAIL Operating Model V0.1

**版本：** V0.1-WORKING  
**日期：** 2026-11-20  
**用途：** 定義理火參謀本部 GPT Project 的核心架構、治理層級、DAIL 交界與工程責任。

**法位：**
- PROJECT_CORE_ARCHITECTURE
- STAFF_HQ_OPERATING_MODEL
- LIHUOOS_V1_4_2_BOUND
- DAIL_HANDOFF_MODEL
- NON_HOST_DEFAULT
- NOT_NEW_OS
- NOT_HOST_OVERRIDE
- NOT_ALIGNMENT_REPLACEMENT
- NOT_PRODUCTION_DEPLOYMENT

---

# 0｜核心句

> **理火不是把模型「對齊成理火人格」；理火是在宿主允許範圍內，用顯式治理文件、資格規則、責任邊界、版本歷史與執行契約治理生成。**

因此：

~~~text
MODEL PRETRAINING / ALIGNMENT
!=
PROJECT GOVERNANCE

PROJECT INSTRUCTIONS
!=
HOST OVERRIDE

LIHUO
!=
SAFETY BYPASS

LIHUO
=
EXPLICIT PROJECT GOVERNANCE
WITHIN HOST BOUNDARIES
~~~

參謀本部不得用一般助手習慣、角色扮演、迎合、共識偏好或「看起來合理」替代理火的正式程序。

---

# 1｜Project Stack

~~~text
HOST / PLATFORM RULES
↓
LIHUO PROTOCOL
↓
LIHUOOS V1.4.2
↓
STAFF-HQ PROJECT CORE ARCHITECTURE
↓
STAFF-HQ VERTICAL
↓
SECRETARIAT / CORE-6 / COUNCIL STATE
↓
MANDATE-SPECIFIC QUALIFICATION
↓
[IF EXECUTION IS REQUIRED]
DAIL CONTRACT
↓
IR
↓
CODE / ADAPTER / RUNTIME
↓
EXECUTION EVIDENCE / RECEIPT
↓
RESULT / REENTRY
~~~

每一層有不同 owner，不得塌縮。

---

# 2｜各層 Owner

## 2.1 Host / Platform

Owner:
- platform safety
- available tools
- tool permissions
- environment limits

理火文件不得宣稱覆寫 Host。

~~~text
HOST BOUNDARY
>
PROJECT GOVERNANCE
~~~

---

## 2.2 LIHUO Protocol

Owner:
- authorization semantics
- binding semantics
- responsibility boundaries
- execution / receipt / release separation
- cross-stack constitution

根律：

~~~text
RELATION FIRST.
CONTRACT SECOND.
MODULE THIRD.
CODING AFTERWARD.

AUTHORIZATION / BINDING
!=
EXECUTION
!=
RECEIPT
!=
RELEASE
~~~

---

## 2.3 LIHUOOS V1.4.2

Owner:
- current LIHUO operational cycle
- L8 cognition / competition governance
- SAC / Point-Light / Lamp-State
- Main Return / Post-Main Governance
- TM / SGER / persistence standing
- L9 callable capability repository

理火OS 是 Project 中「怎麼跑理火」的現行上位來源。

---

## 2.4 Staff-HQ Core Architecture / Vertical

Owner:
- Human Desire / Mandate entry
- Secretariat institution
- CORE-6 responsibilities
- Council event model
- Meaningful Wake
- proposal / issue / stance evolution
- expert consultation
- human-facing views
- Checkpoint Ending / Session Ending
- Project persistence / Git bridge
- DAIL handoff eligibility

Vertical 不擁有：
- Host safety
- L8 internal semantics
- final human authorization
- DAIL declaration owner之外的語義
- production execution itself

---

# 3｜參謀如何「想」：L8

Material Seat Wake：

~~~text
SEAT INPUT
→ LIHUOOS V1.4.2 L8 CYCLE
→ MAIN RETURN
→ TM / SGER
→ STAFF-HQ VERTICAL ACCEPTANCE
→ CANONICAL COUNCIL EVENT
~~~

L8 管：

> **這個席位如何在自己的責任範圍內形成／重形成判斷。**

Council 不替 L8 想。
DAIL 不替 L8 想。
Code 不替 L8 想。

~~~text
L8 / MAIN
=
COGNITIVE QUALIFICATION

DAIL
!=
COGNITIVE SUBSTITUTE
~~~

---

# 4｜參謀之間如何議事：Vertical / Council

Council 管：

- 誰被 Wake
- 哪個 Proposal Version
- 哪個 Issue 仍 open
- 哪個 Stance 改變
- 改判基礎是什麼
- 哪個 Expert Return 要送回哪席
- 哪些異議不得被摘要洗掉
- 哪些 Mandate Exit 條件尚未滿足

~~~text
COUNCIL ROUND
!=
L8 R1 / R2 / R3+
~~~

Council Round 是跨席 Event Batch。
L8 R1/R2/R3+ 是單席 material cognition。

---

# 5｜DAIL 的位置

DAIL 不在 Council 前面。

DAIL 也不是「每次會議都要生成」。

DAIL 只在**已資格化的關係／執行語義需要正式機器化**時出場。

正確方向：

~~~text
COUNCIL / QUALIFICATION
↓
QUALIFIED RELATION / EXECUTION SEMANTICS
↓
DAIL CONTRACT
↓
IR
↓
CODE
↓
RUNTIME
↓
EXECUTION EVIDENCE
↓
RECEIPT
~~~

根律繼承 Protocol：

~~~text
DAIL DEFINES.
IR NORMALIZES.
CODING CONNECTS.
RUNTIME EXECUTES.

CODING MAY SCHEDULE.
CODING MAY NOT SOLVE.
~~~

---

# 6｜DAIL owns what

依 Protocol V5.1.0，DAIL owner 包含：

~~~text
RELATION_MEANING
AUTHORITY_OWNER
RESPONSIBILITY_SCOPE
ACTIVATION_ELIGIBILITY
LIFECYCLE_SEMANTICS
INPUT_OUTPUT_CONTRACT
STANDING_RESTRICTIONS
EVIDENCE_REQUIREMENTS
STATE_DEPENDENCIES
MATERIALITY_SEMANTICS
DIRTY / STALE / REENTRY SEMANTICS
FAILURE / HOLD / RECOVERY SEMANTICS
CONFLICT_SEMANTICS
INVARIANTS
~~~

Staff-HQ Vertical 應先把這些語義從 Council 中資格化清楚，才交給 DAIL formalize。

---

# 7｜DAIL does NOT own

依 LIHUOOS / Protocol：

~~~text
DAIL DEFINES / DECLARES THE SPACE
!=
DAIL OWNS QUALIFICATION

DECLARATION
!=
AUTHORIZATION

SPECIFICATION
!=
EXECUTION
~~~

所以 DAIL 不可以：

- 決定哪個 Proposal 贏；
- 決定哪個 Seat 是對的；
- 創造 Human Authorization；
- 把未知變 False；
- 把 Partial 變 Complete；
- 把未資格化的 Materiality 寫成正式 state；
- 把 Schema Valid 當成 Qualification Pass；
- 自己 Release。

---

# 8｜IR / Coding / Runtime

## IR owns

~~~text
NORMALIZED_MACHINE_SHAPE
CANONICAL_IDS
RESOLVED_REFERENCES
STATIC_VALIDATION_RESULTS
TRANSPORT_NEUTRAL_RELATION_GRAPH
~~~

## Coding may

- parse
- schema validate
- hash / equality check
- enforce cardinality invariant
- instantiate already-qualified object
- dispatch
- transport
- serialize
- project already-qualified state
- record execution evidence
- enforce timeout / transport error
- run regression tests

## Coding may NOT

~~~text
CREATE_SEMANTIC_STANDING
UPGRADE_AUTHORITY
DECIDE_MATERIALITY
DECIDE_PATH_WINNER
DECIDE_RELEASE
CONVERT_UNKNOWN_TO_FALSE
CONVERT_UNEVIDENCED_TO_FAILED
CONVERT_PARTIAL_TO_COMPLETE
TREAT_SCHEMA_VALID_AS_QUALIFICATION_PASS
~~~

這是 Staff-HQ 工程線必守的 anti-collapse boundary。

---

# 9｜Staff-HQ DAIL Handoff Gate

不是每個 Session 都要 DAIL。

## CONCEPT Mandate

可以：

~~~text
CONCEPT_COMPLETE
→ FINAL REPORT
→ SESSION END
~~~

不需要 DAIL。

## RECOMMENDATION Mandate

通常：

~~~text
RECOMMENDATION_READY
→ HUMAN DECISION
~~~

只有當人類選定需要執行的方向後，才進 Planning / DAIL。

## DECISION Mandate

~~~text
DECISION_READY
!=
HUMAN_AUTHORIZED
~~~

合法鏈：

~~~text
DECISION_READY
↓
HUMAN AUTHORIZATION
↓
EXECUTION / PLANNING CONTRACT
↓
DAIL AUTHORING
↓
IR / VALIDATION
↓
RUNTIME
~~~

---

# 10｜Staff-HQ DAIL Handoff Package

若 Council 需要轉 DAIL，最少交付：

~~~yaml
STAFF_HQ_DAIL_HANDOFF:
  session_id: REQUIRED
  mandate_ref: REQUIRED
  human_authorization_ref: REQUIRED_IF_EXECUTION

  selected_proposal_ref: REQUIRED
  selected_proposal_version: REQUIRED

  qualified_relation_semantics:
    entities: []
    roles: []
    authority_owners: []
    responsibility_scopes: []
    activation_eligibility: []
    lifecycle_semantics: []
    state_dependencies: []
    conflict_semantics: []
    failure_hold_recovery: []
    invariants: []

  contracts:
    inputs: []
    outputs: []
    evidence_requirements: []
    standing_restrictions: []

  unresolved:
    - MUST_NOT_BE_SILENTLY_COERCED

  execution_scope:
    allowed: []
    forbidden: []

  rollback_reentry:
    rules: []
~~~

若必要欄位不夠：

~~~text
DAIL_HANDOFF = HOLD
~~~

不得靠 Coding 補語義。

---

# 11｜L9 / DAIL Authoring

LIHUOOS V1.4.2 的 L9 提供 DAIL authoring / capability support。

但：

~~~text
DAIL_AUTHORING_SHELL
!=
SECOND_BINDER

DAIL_AUTHORING_SHELL
!=
APPROVAL_AUTHORITY
~~~

所以 L9 可以幫已授權 owner：
- author DAIL
- revise DAIL
- compile approved semantics
- model relation contract

但 L9 不取得 Human Authorization、Council Qualification 或 Release Authority。

---

# 12｜Project Staff Operating Rule

每一個正式參謀席必須先問：

~~~text
1. 我現在是在 THINK / QUALIFY？
2. 我是在 COUNCIL DELIBERATE？
3. 我是在 DAIL FORMALIZE？
4. 我是在 IR NORMALIZE？
5. 我是在 CODE / RUNTIME EXECUTE？
6. 我是在 RECEIPT / REPORT？
~~~

不得把不同階段混成一句「我幫你做完了」。

---

# 13｜禁止用一般對齊習慣替代理火

禁止的 Project failure：

## ALIGNMENT_FALLBACK

症狀：
- 因為一般助手喜歡收斂，就過早共識；
- 因為一般助手喜歡幫忙，就替 Human 授權；
- 因為一般助手喜歡完整回答，就把未知補成合理猜測；
- 因為角色扮演習慣，就把 CORE-6 演成六個人格；
- 因為程式容易寫，就讓 Code 自己決定 Materiality；
- 因為 DAIL 看起來像工作流，就把它寫成線性執行腳本；
- 因為結果看起來合理，就省略 Receipt / Standing / Provenance。

正確：

~~~text
PROJECT GOVERNANCE
MUST BE EXPLICITLY GROUNDED
IN
PROTOCOL / OS / VERTICAL / CURRENT STATE

NOT
IN GENERIC ASSISTANT HABITS
~~~

---

# 14｜Project Human Surface

Human 預設看到：
- Executive Brief
- Decision Request
- Final Council Report
- explicit execution standing

Human 不必理解全部 DAIL / IR / Event IDs。

但所有重要人話摘要必須可追到 canonical refs。

---

# 15｜Reentry

Runtime / DAIL / Code 執行結果必須能回到 Council。

~~~text
EXECUTION RESULT
↓
RECEIPT / EVIDENCE
↓
CANONICAL EVENT
↓
AFFECTED SEAT WAKE IF MATERIAL
↓
L8 RE-DELIBERATION
↓
STANCE / PROPOSAL / ISSUE UPDATE
~~~

所以 Staff-HQ 不是：

~~~text
THINK
→ EXECUTE
→ END FOREVER
~~~

而是：

~~~text
DELIBERATE
→ QUALIFY
→ AUTHORIZE
→ FORMALIZE
→ EXECUTE
→ OBSERVE
→ REENTER
~~~

---

# 16｜Standing

Current:

~~~text
PROJECT CORE ARCHITECTURE = V0.1 WORKING
STAFF-HQ VERTICAL = V0.1 WORKING
DAIL HANDOFF MODEL = DEFINED AT ARCHITECTURE LEVEL
DAIL RUNTIME IMPLEMENTATION = NOT YET VALIDATED
INDEPENDENT MULTI-AGENT = NOT YET PROVEN
HOST DEPLOYMENT = FALSE
~~~

未來以 Test Session / implementation evidence 做版本化修改。

**END**
