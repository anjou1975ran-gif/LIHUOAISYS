# MRC-001 ROUTER AND QUALIFICATION ENGINE SPEC V0.1
## Rule-Bound Routing × Exact-Version Qualification

**版本：** V0.1-WORKING  
**日期：** 2026-11-20  
**法位：** ROUTER_QUALIFICATION_SPEC / RULE_BOUND / NOT_MATERIALITY_OWNER / NOT_IMPLEMENTED

---

# 0｜核心句

> **Router 決定「已成立的關係送去哪裡」；它不決定「那個關係應不應成立」。Qualification Engine 決定「哪些必要條件已被帳務化」，不決定哪個答案最好。**

---

# 1｜Router Input

Router 可消費：

- Canonical Event semantic type
- origin role
- explicit target refs
- qualified responsibility map
- materiality standing
- proposal version scope
- mandatory route rules
- unresolved issue owner map

Router 不可消費「模型覺得大概重要」作為正式 routing authority。

---

# 2｜Responsibility Map｜Current CORE-6

```yaml
N1:
  tags: [BASIC_QUESTION, EXECUTIVE_CLARITY, USER_ACTION, EXPLANATION_GAP, BUYER_REALITY]
A:
  tags: [NEW_PATH, ALTERNATIVE, OPTION_SPACE, POSSIBILITY]
B:
  tags: [FRAME, ARCHITECTURE, COORDINATE_SHIFT, UNOWNED_RESPONSIBILITY]
C:
  tags: [QUALIFICATION, EVIDENCE, CAUSALITY, AUTHORITY, STANDING, RIGHTS]
D:
  tags: [ENGINEERING, IMPLEMENTATION, DEPENDENCY, TEST, RECOVERY]
E:
  tags: [COST, RESOURCE, TIME, MAINTENANCE, OPPORTUNITY_COST, PAYBACK]
```

這是 V0.2 Staff-HQ Vertical current configuration，不是 DAIL 永久固定六席。

---

# 3｜Primary Route Formula

```text
PRIMARY ROUTE
=
SEMANTIC TYPE RULE
+
EXPLICIT TARGET
+
MANDATORY RESPONSIBILITY MAP
+
QUALIFIED MATERIAL RELATION
```

Explicit target：
- 可以增加合法 target；
- 不得 suppress mandatory owner。

---

# 4｜Materiality Boundary

若：

```text
materiality_standing = MATERIAL
```

Router 依 qualified affected-seat basis 建立 MaterialRelation。

若：

```text
NON_MATERIAL
```

不建立 material wake。

若：

```text
CONTESTED
```

不得自行判定；route 至 qualified materiality owner / HOLD path。

---

# 5｜Proposal Material Delta Routing

若 ProposalVersion 有 qualified material delta：

候選 affected map：

- PROBLEM_FRAME → B, C, N1；視內容可能 A
- BENEFICIARY_OR_BUYER → N1, A, E；視內容 B
- AUTHORITY_OR_RIGHT → C；若改產品/架構再 B/D/E
- BUSINESS_OR_VALUE_MODEL → A, B, E, N1
- ARCHITECTURE → B, D；必要時 C/E
- ENGINEERING_DEPENDENCY → D；必要時 B/E
- EVIDENCE → C；必要時 N1/D
- COST_RESOURCE → E；必要時 A/B/D/N1
- RISK_ALLOCATION → C/E/B
- EXECUTION_SEQUENCE → D/B/E
- CAPITAL_STRATEGY → E/D/A
- KILL_CONDITION → C/E/N1 + relevant owner
- HUMAN_DECISION_REQUESTED → N1/C/Secretary procedural human gate

這是 routing candidate map，不是 semantic truth table。Vertical 可版本化修正。

---

# 6｜Seat Wake Package

```yaml
SeatWakeInput:
  session_ref:
  council_round_ref:
  seat_ref:
  seat_contract_ref:
  mandate_ref:
  exact_proposal_version_ref:
  triggering_relation_refs: []
  qualified_input_refs: []
  prior_stance_ref:
  known_unknown_refs: []
  execution_identity:
```

不得混入：
- 不必要的其他席立場；
- Secretary 預設 winner；
- 未資格化 summary 當 source of truth。

---

# 7｜Consumption Receipt

Seat 對 MaterialRelation 的合法消費至少需：

```yaml
MaterialConsumption:
  relation_ref:
  seat_ref:
  consumed_input_refs: []
  L8_cycle_ref:
  response_event_ref:
  response_type:
```

合法 response_type：
- POSITION_REVISION
- POSITION_RETAINED_WITH_REASON
- POSITION_DOWNGRADED
- POSITION_WITHDRAWN
- NEW_PATH
- NEW_CONDITION
- NEW_OBJECTION

沒有「ACK」就自動算 consumed。

---

# 8｜Latest Proposal Qualification Engine

Target 永遠是：

```text
LATEST PROPOSAL VERSION
```

Input：

```yaml
QualificationInput:
  latest_proposal_version_ref:
  affected_seat_refs: []
  exact_version_review_refs: []
  material_relation_refs: []
  open_issue_refs: []
  meta_governance_ref:
  upper_gate_refs: []
  human_gate_ref:
```

Compute：

```text
unreviewed_material_seats
=
affected_seats
-
exact_version_reviewed_seats
```

---

# 9｜Qualification Hard Blocks

任一成立：

```text
UNREVIEWED_MATERIAL_SEATS != []
UNCONSUMED_MATERIAL_RELATION EXISTS
MISSING_META_GOVERNANCE_WHERE_REQUIRED
UPPER_FORMAL_GATE_BLOCKED
HUMAN_ACTION_REQUIRED_BUT_NO_DECISION_REQUEST
INVALID_ORIGIN/ROLE
UNRESOLVED_MANDATORY_AUTHORITY_CONFLICT
```

則：

```text
MANDATE_EXIT = HOLD
```

---

# 10｜Council Interaction Check

Check 不要求一定有 cross-seat change。

合法兩種：

```text
A. MATERIAL CROSS-SEAT CHAIN EXISTS
   → MUST BE ACCOUNTED

B. NO MATERIAL CROSS-SEAT DELTA
   → RECORD EXPLICITLY
```

禁止：
- 為通過 RT-10 強制製造 objection；
- 為了看起來像 Council 強迫每席改判。

---

# 11｜Meta-Governance Engine Input

最低：

```yaml
MetaGovernance:
  reference_to_proposal_collapse:
  secretariat_thesis_capture:
  material_amendment_bypass:
  l8_as_council_substitute:
  deliverable_capture:
  premature_dail_formalization:
  patch_compliance_theater:
  unresolved_meta_issues: []
```

Engine 可以檢查 evidence presence / relation accounting；
對「是否為 compliance theater」若 evidence 不足，結果可：

```text
SUSPECT
```

不得硬 PASS。

---

# 12｜Human Gate Projection

若 mandate exit 需要人類：
- 選 Proposal
- 批資金
- 允許外部行動
- 接受重大風險
- 終止 session

則：

```text
HUMAN_ACTION_REQUIRED
→ DECISION_REQUEST
→ WAITING_HUMAN
```

Decision Request 必須是 human-readable derived view，但其 request scope 要追 canonical refs。

---

# 13｜Qualification Result Vocabulary

```text
QUALIFIED
REVIEWED_CONDITIONALLY
HOLD
```

禁止模糊混成：
- basically approved
- almost done
- effectively passed

若市場／工程／法律外部證據未驗證，可即使 Council internal review complete 仍是：
- REVIEWED_CONDITIONALLY
- HOLD
視 mandate gate 而定。

---

# 14｜Secretariat Rule

Secretariat 可：
- instantiate routing
- maintain queue
- render state
- produce unqualified composite draft

Secretariat 不可：
- change materiality standing
- author target seat stance
- promote its composite to qualified proposal
- mark relation consumed without seat receipt
- call qualification pass because all files exist

---

# 15｜Reference Specimen Expected Projection

REFERENCE_SPECIMEN_001：

```yaml
latest_proposal: P2
affected_seats: [N1,A,B,C,D,E]
reviewed_exact_version: [N1,A,B,C,D,E]
unreviewed_material_seats: []
unconsumed_material_relations: []
internal_review: REVIEWED_CONDITIONALLY
upper_gate:
  LIHUO_PROJECT_QUALIFIED: false
formal_result: HOLD
session_end: NONE
```

---

# 16｜Non-goals

本 spec 不：
- 選商業 winner；
- 寫 agent prompts；
- 建 UI；
- 決定模型 provider；
- 自動生成 DAIL；
- 取代 Protocol / LIHUOOS。

**END**
