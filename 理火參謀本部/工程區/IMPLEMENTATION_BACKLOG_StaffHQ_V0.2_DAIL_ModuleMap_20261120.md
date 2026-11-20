# IMPLEMENTATION BACKLOG｜Staff-HQ Vertical V0.2 × DAIL Module Map
## 從議事語義到可重播 Runtime 的工程路線

**版本：** V0.1-WORKING  
**日期：** 2026-11-20  
**法位：** ENGINEERING_BACKLOG / NON_NORMATIVE / NO_DEPLOYMENT_CLAIM  
**依賴：**
- STAFF_HQ_DAIL_MINIMUM_RELATION_SET_V0.1
- VERTICAL_LIHUOOS_V1.4.2_理火參謀本部_V0.2_WORKING
- Protocol V5.1.0 P5.1-18B
- LIHUOOS V1.4.2

---

# 0｜工程目標

不要先做「多 Agent 聊天介面」。

先做：

> **可保存、可重播、可判定哪些責任關係尚未被消費的 Council governance runtime。**

最小工程成功不是「六個模型會聊天」。

最小工程成功是：

```text
CANONICAL EVENTS
→ DETERMINISTIC REDUCER
→ ROUTING QUEUE
→ MATERIAL RELATION ACCOUNTING
→ EXACT PROPOSAL VERSION REVIEW
→ QUALIFICATION / HOLD
→ REPLAY
```

---

# 1｜建置順序

## Stage 0｜Semantic Freeze

先人工審：
- C0–C5 DAIL module meaning
- authority owner
- lifecycle states
- materiality owner
- reentry / HOLD semantics
- invariants

出口：

```text
SEMANTIC_SPEC_ACCEPTED_FOR_IMPLEMENTATION
```

未完成不得讓 Coding 自行補語義。

---

## Stage 1｜Canonical Store + Deterministic Reducer

第一個真正該寫的工程，不是 multi-agent provider。

實作：
- canonical event append
- immutable IDs / lineage
- proposal version refs
- stance refs
- issue refs
- material edge records
- affected-seat queue
- current state projection
- replay from zero

成功條件：
- derived state 可完全由 canonical history 重建；
- 刪掉 Final Report 不影響 current state；
- 不靠模型摘要恢復 proposal lineage。

對應 DAIL：
- C0
- C2 基礎 lifecycle
- C4 edge lifecycle
- C5 qualification projections

---

## Stage 2｜Rule-Bound Router

Router 只消費已資格化的：
- event semantic type
- target refs
- responsibility map
- materiality standing / owner result

Router 不判：
- event 是否真；
- objection 是否成立；
- materiality 是否應成立；
- seat 是否該改判。

成功條件：
- mandatory owner route 不可被 explicit target suppress；
- QUIET 只在無 qualified material relation 時成立；
- same event replay routing deterministic。

對應 DAIL：
- C1
- C3
- C4

---

## Stage 3｜Seat Invocation Adapter

支援：

```text
SEAT WAKE
→ QUALIFIED INPUT PACKAGE
→ L8 INVOCATION
→ MAIN / TM / SGER / RECEIPT
→ VERTICAL ACCEPTANCE
→ ORIGIN EVENTS
```

第一版仍可：
- SAME_MODEL_MULTI_ROLE_REFERENCE

但 Adapter 必須保存 execution identity。

未來 provider 可換：
- same-model isolated context
- multi-model
- independent agent

Council semantics 不跟 provider 綁死。

---

## Stage 4｜Exact-Version Qualification Engine

實作：
- proposal material delta registration
- affected seat set
- reviewed exact version
- unreviewed material seats
- surviving objections
- Council Interaction Check
- Meta-Governance Sweep state

成功條件：

```text
P1 RECEIPTS
CANNOT
QUALIFY P2
```

以及：

```text
NO CLOSURE
WITH UNCONSUMED MATERIAL RELATION
```

---

## Stage 5｜DAIL → IR Compilation

只在 Stage 0 語義凍結後做。

IR 最小 objects：

```yaml
IR_OBJECTS:
  Actor
  AuthorityBinding
  ResponsibilityBinding
  Session
  Mandate
  ProblemFrame
  Reference
  Proposal
  ProposalVersion
  Stance
  CanonicalEvent
  MaterialRelation
  SeatWake
  Issue
  QualificationCheck
  HumanGate
  Receipt
```

IR 只正規化：
- canonical IDs
- refs
- enums
- graph edges
- static constraints

IR 不創造 semantic standing。

---

## Stage 6｜Human Surface

工程化：
- Executive Brief
- Trust Strip
- Decision Request
- Audit View
- Final Report renderer

規則：

```text
VIEW IS DERIVED.
VIEW IS NOT SECOND TRUTH.
```

每個重要摘要句應能追到 canonical refs。

---

## Stage 7｜Provider Independence

直到 reducer / replay / qualification engine 成立後，才值得投資真正多模型。

測試：
- same model vs isolated same model
- independent models
- seat-specific method packs
- blind P0-none formation

目的不是增加戲劇性，而是測：
- frame lock
- social convergence
- provider-specific bias
- cross-seat causal robustness

---

# 2｜DAIL Module → Engineering Component Map

| DAIL Module | First Engineering Component | 不得偷做 |
|---|---|---|
| C0 Canonical Identity & Provenance | append-only store / ID / lineage / replay | 不得以 Git 檔名代替 semantic ID |
| C1 Authority & Role | authority/responsibility validator | 不得由 code 升權 |
| C2 Frame & Proposal Lifecycle | lifecycle reducer | 不得把 reference 自動升 proposal |
| C3 Materiality & Wake | material relation registry + routing input | 不得由 field diff 自判 material |
| C4 Cross-Seat Causality | edge queue / consumption receipt | delivered 不得視為 consumed/agreed |
| C5 Qualification / Exit / Reentry | qualification engine / human gate | 不得自行 release |

---

# 3｜最小資料結構候選

注意：以下只是 IR 候選，不是 DAIL semantic source。

```yaml
MaterialRelation:
  id:
  source_event_ref:
  target_seat_ref:
  relation_type:
  materiality_standing:
  materiality_basis_refs: []
  state: QUEUED|DELIVERED|CONSUMED|RESPONDED|CLOSED_FOR_VERSION
  response_event_refs: []

ProposalVersionState:
  proposal_ref:
  version:
  origin_ref:
  parent_version_ref:
  material_delta_refs: []
  affected_seats: []
  reviewed_seats: []
  unreviewed_seats: []
  surviving_objections: []
  standing:

SeatStance:
  seat_ref:
  proposal_version_ref:
  stance_ref:
  prior_stance_ref:
  response_type:
  change_basis_refs: []
  unresolved: []
```

---

# 4｜Regression Gate

在宣稱 V0.2 runtime 前，至少全跑：

```text
RT-01 ~ RT-13
```

另加 property tests：

1. append-only history；
2. same canonical log → same reducer state；
3. derived views deletion does not alter state；
4. old proposal receipts cannot qualify new material version；
5. secretariat-origin route cannot self-upgrade proposal；
6. human authorization cannot be inferred from task continuation；
7. unresolved material relation cannot disappear through summary；
8. HOLD remains non-terminal unless end rule says so。

---

# 5｜Reference Specimen Policy

現有 Clean Intelligence Reentry：

```text
REFERENCE_SPECIMEN_001
```

用途：
- replay fixture
- reducer fixture
- cross-seat causal graph fixture
- exact-version qualification fixture
- HOLD fixture

不得作：
- general benchmark proof
- multi-agent proof
- market proof

下一個陌生領域 specimen 應刻意：
- 無既存 P1；
- 無預期「一定要有改判」；
- 允許 NO_MATERIAL_CROSS_SEAT_DELTA；
- 不告訴模型 RT-10 的預期答案。

---

# 6｜第一個真正工程 Milestone

```yaml
MILESTONE_MRC_001:
  name: "Minimum Replayable Council"
  must_have:
    - canonical event store
    - proposal version lineage
    - seat stance refs
    - material relation queue
    - deterministic reducer
    - latest proposal coverage
    - HOLD / human gate projection
    - full replay of REFERENCE_SPECIMEN_001
  not_required_yet:
    - independent multi-agent
    - web UI
    - vector DB
    - external expert automation
    - production deployment
```

判準：

> **若不靠最後報告，只靠 Canonical Events 就能重建「誰影響誰、P2 為什麼形成、誰審了哪一版、為什麼 HOLD」，MRC-001 才算成立。**

---

# 7｜下一版 DAIL 候選，不先納入

先保留，不放進最小核心：
- dynamic seat creation
- weighted voting
- reputation score
- probabilistic confidence aggregation
- token budget optimizer
- automatic expert marketplace
- automatic majority decision
- consensus score

原因：

> 這些都可能讓系統更複雜，但目前沒有證據顯示它們是 Council legitimacy 的必要條件。

---

# 8｜Current Standing

```text
SEMANTIC DESIGN = STARTED
V0.2 VERTICAL = WORKING CANDIDATE
DAIL MODULE MAP = DEFINED
IR = CANDIDATE ONLY
CODE = NOT STARTED
REDUCER = NOT IMPLEMENTED
REPLAY = NOT PROVEN
INDEPENDENT MULTI-AGENT = NOT PROVEN
```

**END**
