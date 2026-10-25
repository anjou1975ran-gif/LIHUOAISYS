# LIHUOOS V1｜L9 DAIL CALLABLE CAPABILITY REPOSITORY V0.1.1-WORKING
## 理火可調用能力倉｜DAIL-Defined Modules × Tool Registry × Runtime Binding
### 2026-10-25

```yaml
DOCUMENT:
  id: LIHUOOS_L9_DAIL_CALLABLE_CAPABILITY_REPOSITORY
  version: V0.1.1-WORKING
  date: 2026-10-25

  status:
    - WORKING
    - CAPABILITY_REPOSITORY_LAYER
    - NOT_RATIFIED
    - NOT_HOST_DEPLOYED

  purpose:
    - MOVE_CALLABLE_FUNCTIONAL_MODULES_OUT_OF_MONOLITHIC_LIGHTER
    - REGISTER_THEM_AS_DAIL_DEFINED_CAPABILITIES
    - LET_L8_OR_APPLICABLE_OWNERS_CALL_THEM_WHEN_NEEDED
    - KEEP_GOVERNANCE_AUTHORITY_OUTSIDE_THE_TOOL_WAREHOUSE

  lineage:
    source:
      - LIHUO_LIGHTER_V5_1_0_FUNCTIONAL_MODULE_LINEAGE
      - DAIL
    consumer:
      - L8_LIHUO_OPERATING_CYCLE
      - APPLICABLE_L0_L7_OWNERS
      - AUTHORIZED_VERTICALS
```

---

# 0｜一句話定位

> **L9 是理火的 DAIL 可調用能力倉：把原本集中在 Lighter 內的功能模組拆成可註冊、可尋址、可調用、可替換的工具與能力。**

最短式：

```text
L0–L7
=
KNOW WHAT / WHY / BOUNDARY

L8
=
RUN THE JOB

L9
=
PROVIDE CALLABLE CAPABILITIES
```

---

# 1｜最高硬鎖

```text
L9
!=
NEW THEORY OWNER

L9
!=
GOVERNANCE SOVEREIGN

L9
!=
MAIN

L9
!=
LIGHTER RENAMED

L9
!=
TOOL RESULT JUDGE

L9
!=
FINAL GATE

L9
!=
FINAL RELEASE OWNER
```

根句：

```text
TOOL EXISTS
!=
AUTHORITY TO CALL IT

TOOL CAN EXECUTE
!=
EXECUTION IS AUTHORIZED

TOOL RETURN EXISTS
!=
RETURN IS QUALIFIED FOR USE
```

---

# 2｜L9 真正做什麼

L9 只做四件事：

```text
REGISTER
DISCOVER
BIND
CALL
```

展開：

```text
REGISTER
=
知道有哪些能力

DISCOVER
=
依需求找到適合能力

BIND
=
把 DAIL 宣告綁到實際 implementation / provider / tool

CALL
=
在合法 request 下執行並回傳結果
```

L9 不決定：

```text
SHOULD THIS CAPABILITY BE USED?
IS THIS RESULT TRUE?
DOES THIS RESULT HAVE AUTHORITY?
MAY THE CYCLE PROCEED?
MAY THIS OUTPUT BE RELEASED?
```

這些屬既有治理 owner。

---

# 3｜DAIL 在 L9 的位置

沿用既有工程根句：

```text
DAIL DEFINES.
IR NORMALIZES.
CODING CONNECTS.
RUNTIME EXECUTES.
```

在 L9 中讀成：

```text
DAIL
=
CAPABILITY DECLARATION

IR
=
NORMALIZED CALL CONTRACT

CODING / BINDING
=
IMPLEMENTATION CONNECTION

RUNTIME
=
ACTUAL TOOL / MODULE EXECUTION
```

所以：

> **DAIL 不是工具本身；DAIL 是讓理火知道「這個能力是什麼、怎麼叫、會回什麼」的可移植宣告。**

---

# 4｜L9 不是把 Lighter 整包搬家

舊 Lighter 同時包含：

```text
GOVERNANCE
+
QUALIFICATION
+
ORCHESTRATION
+
TOOLS / PROVIDERS / MODULES
+
FINAL GATE / RELEASE
```

L9 只吸收：

```text
CALLABLE FUNCTIONAL CAPABILITY
```

不吸收：

```text
OWNER AUTHORITY
FINAL GOVERNANCE DECISION
FINAL RELEASE AUTHORITY
THEORY OWNERSHIP
```

所以：

```text
LIGHTER DECOMPOSITION
!=
LIGHTER REINCARNATION AS L9
```

---

# 5｜什麼東西可以進 L9

可以進 L9 的東西，必須至少是「可被明確呼叫並返回結果」的能力。

例如舊 Lighter lineage 中：

```text
PREMISE ANALYSIS / QUALIFICATION SUPPORT
AUTHORITY ANALYSIS SUPPORT
ATTENTION-EFFECT ANALYSIS SUPPORT
EXTERNAL-CONSTRAINT PARSING
R-CCC OBLIGATION COMPILATION
COMPETITION-INTEGRITY CHECK
QIP COMPILATION
OUTPUT-CONTRACT CHECK
OUTPUT-SUFFICIENCY CHECK
CAPABILITY RESOLUTION
FUNCTIONAL MODULE ROUTING
PROVIDER / TOOL / TRANSPORT ADAPTER
EXECUTION-TICKET GENERATION SUPPORT
EVIDENCE INGESTION / NORMALIZATION
EVIDENCE-ORIGIN ANALYSIS
RECOVERY UTILITY
REAUTHORIZATION SUPPORT
VERSION RESOLUTION
DOMAIN MODULES
SEARCH / RETRIEVAL
FILE / ARTIFACT OPERATIONS
EXTERNAL ACTION TOOLS
```

但「support / tool」與「authority」要分開。

例如：

```text
PREMISE_ANALYZER TOOL
MAY PRODUCE
PREMISE ANALYSIS

BUT

PREMISE QUALIFICATION STANDING
IS STILL OWNED
BY THE APPLICABLE GOVERNANCE OWNER
```

---

# 6｜哪些東西不能因為 L9 而失去 owner

例如：

```text
FINAL_GATE_CHECKER
```

可以是一個 L9 callable capability。

但：

```text
FINAL_GATE_TOOL OUTPUT
!=
FINAL GATE AUTHORITY
```

同理：

```text
RELEASE_EXECUTOR
```

可以是工具。

但：

```text
RELEASE TOOL
!=
RELEASE AUTHORITY
```

以及：

```text
AUTHORITY_ANALYZER
!=
AUTHORITY OWNER
```

---

# 7｜最小 DAIL Capability Card

L9 不需要巨大 schema。

最小卡片只要能回答：

> 這是什麼、吃什麼、回什麼、怎麼叫、誰實作。

```yaml
DAIL_CAPABILITY_CARD:
  capability_id: REQUIRED
  version: REQUIRED

  purpose: REQUIRED

  input_contract_ref: REQUIRED
  output_contract_ref: REQUIRED

  callable_by_ref: REQUIRED

  implementation_binding_ref: REQUIRED

  capability_status:
    - AVAILABLE
    - UNAVAILABLE
    - DEGRADED
    - DEPRECATED

  dependency_refs: []

  result_receipt_class_ref: OPTIONAL
```

夠了。

權限細節不在這張卡重新發明。

callable_by_ref 只指向 applicable owner / authority contract。

---

# 8｜Capability Class

為了找工具，可以有簡單分類：

```text
ANALYSIS
QUALIFICATION_SUPPORT
COMPILATION
ROUTING
RETRIEVAL
EVIDENCE
PROVIDER_ADAPTER
EXECUTION
RECOVERY
VERSIONING
ARTIFACT
DOMAIN
OTHER
```

這只是 registry taxonomy。

不是 theory ontology。

---

# 9｜L9 Registry

```yaml
L9_CAPABILITY_REGISTRY:
  registry_ref: REQUIRED

  capabilities:
    - capability_id
    - version
    - capability_class
    - status
    - dail_card_ref
    - implementation_binding_ref

  registry_version_ref: REQUIRED
```

L9 需要能：

```text
LOOKUP(capability_id)
LIST(capability_class)
RESOLVE(version / current)
CHECK_AVAILABILITY
RETURN_BINDING
```

不需要：

```text
DECIDE_WHETHER_WORLD_SHOULD_USE_IT
```

---

# 10｜Implementation Binding

同一個 capability 可以換 provider / tool / implementation。

```yaml
L9_IMPLEMENTATION_BINDING:
  binding_ref: REQUIRED

  capability_id: REQUIRED
  capability_version: REQUIRED

  implementation_type:
    - LOCAL_MODULE
    - HOST_TOOL
    - EXTERNAL_PROVIDER
    - CONNECTOR
    - SERVICE
    - HUMAN_HANDOFF
    - OTHER

  implementation_ref: REQUIRED

  runtime_status:
    - READY
    - UNAVAILABLE
    - DEGRADED

  dependency_refs: []
```

所以：

```text
CAPABILITY IDENTITY
!=
ONE PERMANENT PROVIDER
```

L9 可以換 implementation，而不改上層語義。

---

# 11｜L8 如何叫 L9

標準：

```text
L8 / APPLICABLE OWNER
IDENTIFIES NEED
↓
QUALIFIED CALL REQUEST EXISTS
↓
L9 RESOLVES CAPABILITY
↓
L9 EXECUTES BOUND IMPLEMENTATION
↓
L9 RETURNS RESULT
↓
APPLICABLE OWNER CONSUMES / QUALIFIES RESULT
↓
L8 CONTINUES CYCLE
```

L9 不自己創造：

```text
QUALIFIED CALL REQUEST
```

如果沒有合法 call：

```text
NO CALL
```

---

# 12｜最小 Call Request

L9 只需要足夠執行。

```yaml
L9_CAPABILITY_CALL:
  call_ref: REQUIRED

  capability_id: REQUIRED
  capability_version: CURRENT_OR_EXPLICIT

  caller_ref: REQUIRED
  call_authority_ref: REQUIRED

  input_ref: REQUIRED
  input_contract_ref: REQUIRED

  cycle_ref: OPTIONAL
  main_invocation_ref: OPTIONAL

  requested_at_ref: REQUIRED
```

cycle_ref / main_invocation_ref 只有真的需要綁定時才帶。

不要所有工具都硬綁整套 OS identity。

---

# 13｜最小 Tool Return

```yaml
L9_CAPABILITY_RETURN:
  call_ref: REQUIRED
  capability_id: REQUIRED
  capability_version: REQUIRED

  implementation_ref: REQUIRED

  result_ref: REQUIRED_OR_NONE

  call_execution_status:
    - SUCCESS
    - PARTIAL
    - FAILED
    - UNAVAILABLE
    - CANCELLED

  error_or_gap_ref: OPTIONAL

  receipt_ref: OPTIONAL
```

這個 return 只回答：

> **這次 tool call 的 implementation execution 結果是什麼？**

硬鎖：

```text
TOOL CALL SUCCESS
!=
SEMANTIC RESULT ACCEPTED

CALL EXECUTION STATUS
!=
TASK OUTCOME
```

所以它不自動回答：

> **上層應不應該相信、採用、發布，或整體任務是否成功。**

---

# 14｜Receipt 原則

L9 若 underlying provider / tool 有 canonical receipt：

```text
PRESERVE IT
RETURN IT
```

如果沒有：

```text
DO NOT INVENT PROVIDER RECEIPT
```

L9 可以回：

```text
NO_CANONICAL_RECEIPT
```

讓 L8 最後 checklist 如實列出。

L9 不需要再建「receipt 的 receipt」。

---

# 15｜Capability Discovery

上層不知道 capability id 時，可以依：

```text
purpose
task type
input type
required output
domain
availability
```

查找。

但 discovery 結果只是：

```text
CANDIDATE CAPABILITIES
```

不是：

```text
AUTHORIZED CAPABILITY SELECTION
```

適用 owner 仍決定是否使用。

---

# 16｜版本管理

L9 應允許：

```text
MULTIPLE VERSIONS
CURRENT POINTER
DEPRECATED VERSION
PINNED VERSION
ROLLBACK TARGET
```

最小規則：

```text
CALL MAY PIN VERSION
OR
USE CURRENT RESOLVED VERSION
```

但：

```text
VERSION CURRENT
!=
SEMANTICALLY APPROVED FOR EVERY DOMAIN
```

---

# 17｜失敗與降級

如果 capability unavailable：

```text
L9 RETURNS
UNAVAILABLE
```

不要假裝成功。

上層再決定：

```text
RETRY
FALLBACK
HOLD
SKIP IF OPTIONAL
ABORT
```

L9 不擅自改任務。

---

# 18｜原 Lighter 功能的遷移原則

遷移時不要問：

> 這個功能以前在 Lighter，所以是不是整個搬過來？

要問：

> **這是不是一個可以獨立被叫用、輸入清楚、輸出清楚的 capability？**

如果是：

```text
MOVE / REIMPLEMENT INTO L9
AS DAIL-CALLABLE CAPABILITY
```

如果不是，而是：

```text
OWNER AUTHORITY
GOVERNANCE RULE
QUALIFICATION STANDING
FINAL RELEASE RIGHT
```

就留在：

```text
L0–L7 / APPLICABLE GOVERNANCE CONTRACT
```

---

# 19｜第一批 L9 Capability Families

這只是 migration map，不宣稱已部署。

```yaml
L9_INITIAL_CAPABILITY_FAMILIES:

  INPUT_AND_ANALYSIS:
    - RAW_INPUT_PARSER
    - PREMISE_ANALYZER
    - AUTHORITY_ANALYZER
    - EXTERNAL_CONSTRAINT_PARSER

  COMPILATION:
    - RCCC_OBLIGATION_COMPILER
    - QIP_COMPILER
    - OUTPUT_CONTRACT_COMPILER

  AUDIT_SUPPORT:
    - COMPETITION_INTEGRITY_CHECKER
    - OUTPUT_SUFFICIENCY_CHECKER
    - EVIDENCE_ORIGIN_ANALYZER

  EVIDENCE_AND_RETRIEVAL:
    - EVIDENCE_INGESTOR
    - RETRIEVAL_MODULE
    - SEARCH_MODULE
    - CURRENT_SOURCE_LOOKUP

  ROUTING_AND_PROVIDER:
    - CAPABILITY_RESOLVER
    - MODULE_ROUTER
    - PROVIDER_ADAPTER
    - TRANSPORT_ADAPTER

  EXECUTION:
    - EXTERNAL_ACTION_TOOL
    - ARTIFACT_OPERATION_TOOL
    - EXECUTION_TICKET_BUILDER

  RECOVERY_AND_VERSIONING:
    - RECOVERY_UTILITY
    - REAUTHORIZATION_SUPPORT
    - VERSION_RESOLVER

  DOMAIN:
    - DOMAIN_SPECIFIC_MODULES
```

每一個 family 之後可以有多個 DAIL capability card。

---

# 20｜Final Gate / Release 怎麼處理

這兩個最容易重新長出 Lighter。

正確拆法：

```text
FINAL_GATE SEMANTICS / AUTHORITY
=
GOVERNANCE OWNER

FINAL_GATE CHECKING CAPABILITY
=
MAY LIVE IN L9
```

以及：

```text
RELEASE AUTHORITY
=
APPLICABLE RELEASE OWNER

RELEASE EXECUTION CAPABILITY
=
MAY LIVE IN L9
```

所以：

> **L9 可以提供手；不能自己變成腦或法官。**

---

# 21｜L9 與 Main

Main 可以需要工具。

但：

```text
MAIN
DOES NOT OWN L9

L9
DOES NOT OWN MAIN
```

若 Main contract 允許 tool call：

```text
MAIN / GOVERNANCE
→ QUALIFIED CALL
→ L9
→ RETURN
→ MAIN CONTINUES
```

L9 不介入 Main 的 generative dynamics。

---

# 22｜L9 與 L8

L8 是業務流程。

L9 是能力供應。

```text
L8
=
WHAT STEP ARE WE DOING?

L9
=
WHAT CAPABILITY CAN DO THIS STEP?
```

所以：

```text
L8 MAY CALL MANY L9 MODULES

L9 MAY SERVE MANY L8 CYCLES
```

兩者不要互相吞。

---

# 23｜Overengineering Control

L9 只保留真正需要的資料：

```text
WHAT
INPUT
OUTPUT
HOW TO CALL
WHAT IMPLEMENTS IT
CURRENT AVAILABILITY
```

如果某欄位不能改善：

```text
DISCOVERY
CALLING
BINDING
RETURN
```

就不要塞進 L9 core。

尤其禁止：

```text
EVERY TOOL
MUST REDECLARE
ALL L0–L8 TYPES
```

只引用 canonical contract。

---

# 24｜最小 Runtime Algorithm

```text
RECEIVE QUALIFIED CALL REQUEST

1. RESOLVE capability_id / version
2. CHECK availability
3. RESOLVE implementation binding
4. PASS canonical input
5. EXECUTE
6. RETURN canonical result / error
7. PRESERVE provider/tool receipt if any
8. STOP
```

L9 到這裡就結束。

---

# 25｜L9 最短法位

```text
L9
DOES NOT DECIDE
WHAT LIHUO SHOULD BELIEVE.

L9
DOES NOT DECIDE
WHAT LIHUO MAY AUTHORIZE.

L9
DOES NOT DECIDE
WHAT LIHUO MAY RELEASE.

L9
PROVIDES
CALLABLE CAPABILITY.

DAIL DEFINES IT.
BINDING CONNECTS IT.
RUNTIME EXECUTES IT.
THE OWNER ABOVE
DECIDES WHAT THE RESULT MEANS.
```

---

# 26｜Working Standing

```text
L9 DAIL CALLABLE CAPABILITY REPOSITORY V0.1.1-WORKING

IDENTITY
=
CAPABILITY REPOSITORY LAYER

SOURCE LINEAGE
=
LIGHTER FUNCTIONAL MODULES
+
DAIL

NEW THEORY
=
NONE

NEW GOVERNANCE OWNER
=
NONE

CORE JOB
=
REGISTER / DISCOVER / BIND / CALL

AUTHORITY
=
EXTERNAL TO L9

RESULT QUALIFICATION
=
EXTERNAL TO L9

L8 RELATION
=
PROVIDE CALLABLE CAPABILITIES FOR OPERATING CYCLE

MAIN RELATION
=
PROVIDE TOOLS WHEN LAWFULLY CALLED

OVERENGINEERING CONTROL
=
PASS IN CURRENT DESIGN

RUNTIME RATIFICATION
=
HOLD
```

---

# 27｜一句話收束

> **L9 不是新的 Lighter；L9 是把能力從巨型控制平面拆出來，變成 DAIL 定義、可尋址、可替換、可調用的工具倉。**
