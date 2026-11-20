# VERTICAL｜LIHUOOS V1.4.2 × 理火參謀本部 V0.2
## 真正議事型 Staff-HQ Vertical｜WORKING CANDIDATE

**版本：** V0.2-WORKING  
**日期：** 2026-11-20  
**法位：** PROJECT_VERTICAL_PROCEDURE_CANDIDATE / LIHUOOS_V1_4_2_BOUND / NON_HOST_DEFAULT / NOT_NEW_OS_LAYER / NOT_SECOND_L8 / NOT_SECOND_MAIN / NOT_HOST_DEPLOYMENT  
**前版：** V0.1 仍為現行工作基線；本文件在 ratification 前不自動 supersede V0.1。  
**新增來源：** PATCH_STAFF_HQ_V0.1.1、STAFF_HQ_DAIL_MINIMUM_RELATION_SET_V0.1、Corrective Reentry reference specimen。

---

# 0｜V0.2 的真正改變

V0.1 解決：

> 「一個 Staff-HQ Session 如何被記錄、路由、叫醒席位、跑 L8。」

V0.2 要解決：

> **「不同責任位置如何真正改變彼此的主張，最後讓一份建議取得或失去資格。」**

因此：

```text
V0.1 = SESSION ORCHESTRATION BASELINE

V0.2 = DELIBERATION RELATION + QUALIFICATION VERTICAL
```

不是新增更多角色。

---

# 1｜核心定義

```text
STAFF-HQ DELIBERATION
!=
MULTI-ROLE CHAT

STAFF-HQ DELIBERATION
=
PROBLEM FORMATION
+
RESPONSIBILITY-SCOPED JUDGMENT
+
MATERIAL CROSS-SEAT RELATION
+
OWNED POSITION RESPONSE
+
VERSIONED PROPOSAL QUALIFICATION
```

一句話：

> **參謀本部不是先做答案，再叫六席審；參謀本部要讓不同責任真正改變答案最後有資格長成什麼。**

---

# 2｜上位法位不變

```text
HOST / PLATFORM
>
LIHUO PROTOCOL
>
LIHUOOS V1.4.2
>
STAFF-HQ PROJECT CORE
>
STAFF-HQ VERTICAL
>
SESSION
```

V0.2 不得：
- 覆寫 Host；
- 重寫 L8；
- 宣稱 hidden CoT；
- 自創 Release Authority；
- 把 DAIL 當 cognition；
- 把 same-model reference 稱為 independent multi-agent。

---

# 3｜Formal Session Entry

Human 明示 Staff-HQ / Council / 正式概念案、建議案、決策案時：

```text
HUMAN INPUT
→ D0 RAW DESIRE
→ D1 MANDATE CANDIDATE
→ SESSION MANIFEST
```

D1 仍保留：
- mandate_type
- primary_question
- desired_return
- hard_boundaries
- excluded_scope
- human_intervention_mode
- end_policy
- standing

新增 V0.2：

```yaml
formation_state:
  problem_frame: OPEN | HUMAN_GIVEN | CONTESTED | QUALIFIED_FOR_CURRENT_MANDATE
  proposal_opening:
    P0: NONE | HUMAN_PROPOSAL | EXISTING_CANDIDATE
  reference_set: []
```

硬鎖：

```text
REFERENCE != PROPOSAL
DESIRED_RETURN != COUNCIL_PURPOSE
```

---

# 4｜Open Problem Formation

若 Human 沒有明示 Proposal：

```text
P0 = NONE
```

合法。

CORE seats 初始可收到：
- D0
- D1
- REFERENCE_SET
- seat responsibility
- known unknowns

不要求先對共同答案表態。

合法初始 objects：
- QUESTION
- PROBLEM_REFRAME
- NEW_PATH
- OBJECTION
- CONDITION
- DEPENDENCY
- NO_PROPOSAL_NEEDED_YET

這是 V0.2 對第一輪失敗的根修正。

---

# 5｜Seat Initial Pass

仍遵守：

```text
INITIAL_PASS
→ LIMIT OTHER-SEAT STANCE EXPOSURE
```

目的有兩個：
1. 防 social convergence；
2. 防所有席位被同一個未資格化 framing 綁住。

每個 material seat invocation：

```text
QUALIFIED SEAT INPUT
→ LIHUOOS L8
→ MAIN / TM / SGER / RECEIPT
→ VERTICAL ACCEPTANCE
→ ORIGIN-DECLARED CANONICAL EVENT
```

---

# 6｜Canonical Event Contract V0.2

最低欄位：

```yaml
CANONICAL_EVENT:
  event_id: REQUIRED
  session_id: REQUIRED
  origin_actor: REQUIRED
  origin_role: REQUIRED
  semantic_type: REQUIRED

  source_refs: []
  target_refs: []

  proposal_ref: OPTIONAL
  proposal_version: OPTIONAL
  prior_stance_ref: OPTIONAL

  materiality_claim:
    standing: MATERIAL | NON_MATERIAL | CONTESTED
    basis_refs: []

  affected_seat_claims: []

  unresolved: []
  persistence_standing: REQUIRED
```

Adapter 可 challenge semantic type / materiality completeness；
不可靜默改 origin type。

---

# 7｜Council Cross-Seat Relation

新主鏈：

```text
CANONICAL EVENT
→ MATERIALITY RELATION
→ AFFECTED SEAT SET
→ DELIVERY
→ SEAT CONSUMPTION
→ OWNED RESPONSE
→ NEW CANONICAL EVENT
```

合法 response：
- POSITION_REVISION
- POSITION_RETAINED_WITH_REASON
- POSITION_DOWNGRADED
- POSITION_WITHDRAWN
- NEW_PATH
- NEW_CONDITION
- NEW_OBJECTION

硬鎖：

```text
TARGET SEAT
MUST OWN
ITS RESPONSE

SECRETARIAT
MAY NOT WRITE
THE TARGET SEAT'S SUBSTANTIVE RESPONSE
```

---

# 8｜Materiality / Meaningful Wake V0.2

Meaningful Wake 保留，但加上 owner discipline。

```text
NO QUALIFIED MATERIAL DELTA
→ QUIET MAY BE LEGAL

QUALIFIED MATERIAL DELTA
→ AFFECTED SEAT REWAKE REQUIRED
```

Materiality 不能只由欄位差異產生。

候選 material classes：
- problem frame
- beneficiary/buyer
- authority/right
- value/business model
- architecture
- engineering dependency
- evidence
- cost/resource
- risk allocation
- execution sequence
- capital strategy
- kill condition
- human decision requested

```text
ENUM MATCH
!=
MATERIALITY QUALIFIED
```

---

# 9｜Proposal Origin Rules

Proposal candidate 可由：
- Human 明示；
- CORE seat origin-declare；
- 已授權的專案 owner 依上位規則提出。

Secretariat：
- 可保存 Proposal；
- 可 render composite view；
- 可建立 `SECRETARIAT_COMPOSITE_DRAFT`。

但：

```text
SECRETARIAT_COMPOSITE_DRAFT
=
UNQUALIFIED_CANDIDATE
```

不得因整合能力而升格成 qualified proposal。

---

# 10｜Proposal Version Lifecycle

```text
NONE
→ CANDIDATE
→ MATERIAL_REVIEW_PENDING
→ REVIEWED_CONDITIONALLY
→ QUALIFIED
```

旁路：
- HOLD
- WITHDRAWN
- SUPERSEDED

只要 latest proposal 改變 material relation：

```text
P(n) MATERIAL DELTA
→ EVENT
→ AFFECTED SEAT SET
→ REWAKE
→ STANCE ON EXACT P(n)
```

硬鎖：

```text
NO CLOSURE
WITH UNREVIEWED MATERIAL PROPOSAL DELTA
```

---

# 11｜Council Interaction Check

Mandate Exit 前：

1. 是否有 seat-to-seat material dependency？
2. 是否有 objection 改變另一席 path？
3. architecture 是否改變 engineering/cost？
4. qualification/cost 是否反向改變 path？
5. new path 是否尚未被相關 owner 消費？

若有：

```text
ROUTE → REWAKE → NEW EVENT
```

若沒有：

```text
COUNCIL_INTERACTION_CHECK
=
NO_MATERIAL_CROSS_SEAT_DELTA
```

不強迫表演衝突。

---

# 12｜Latest Proposal Qualification Check

Recommendation / Decision exit 前：

```yaml
LATEST_PROPOSAL_QUALIFICATION_CHECK:
  latest_proposal_ref: REQUIRED
  latest_proposal_version: REQUIRED
  material_delta_since_last_review: REQUIRED
  affected_seats: []
  reviewed_latest_version_seats: []
  quiet_or_not_affected: []
  unreviewed_material_seats: []
  surviving_objections: []
  unresolved_external_facts: []
```

若：

```text
unreviewed_material_seats != []
```

則：

```text
MANDATE_EXIT = HOLD
```

---

# 13｜Meta-Governance Sweep V0.2

最低：

```yaml
META_GOVERNANCE_SWEEP:
  reference_to_proposal_collapse: PASS|FAIL
  secretariat_thesis_capture: PASS|FAIL
  material_amendment_bypass: PASS|FAIL
  l8_as_council_substitute: PASS|FAIL
  deliverable_capture: PASS|FAIL
  premature_dail_formalization: PASS|FAIL
  patch_compliance_theater: PASS|SUSPECT|FAIL
  unresolved_meta_issues: []
```

新增 `patch_compliance_theater` 不要求「一定產生不同答案」。

它問：

> 是否只是刻意製造可見的 objection/revision 來符合測試，而沒有 responsibility-grounded material basis？

若 SUSPECT：
- 不自動 FAIL；
- 保留 evidence gap；
- 可要求 blind / unfamiliar-domain regression。

---

# 14｜DAIL Binding in V0.2

V0.2 採：

```text
C0 CANONICAL_IDENTITY_AND_PROVENANCE
C1 AUTHORITY_AND_ROLE_CONTRACT
C2 FRAME_AND_PROPOSAL_LIFECYCLE
C3 MATERIALITY_AND_WAKE_CONTRACT
C4 CROSS_SEAT_CAUSALITY_CONTRACT
C5 QUALIFICATION_EXIT_AND_REENTRY
```

DAIL 不是每次會議都重新作者化。

Project 應有：
- stable Staff-HQ DAIL contracts
- session instances
- qualified state projections

```text
STABLE DAIL CONTRACT
+
SESSION INSTANCE
!=
NEW DAIL THEORY EACH SESSION
```

---

# 15｜DAIL / IR / Code 邊界

```text
DAIL DEFINES RELATION MEANING.
IR NORMALIZES MACHINE SHAPE.
CODE CONNECTS QUALIFIED OBJECTS.
RUNTIME EXECUTES.
```

Code 可：
- parse
- validate schema
- resolve refs
- enforce cardinality
- dispatch
- serialize
- record evidence
- replay
- regression test

Code 不可：
- decide materiality
- choose path winner
- upgrade standing
- convert unknown to false
- convert partial to complete
- decide final gate
- decide release

---

# 16｜Reducer / Replay Requirement

V0.2 開始把 deterministic reducer + replay 視為真正工程必要條件，不再只是「未來可能」。

理由：

> Council legitimacy 必須能由 canonical event history 重建，而不是依賴最後那篇漂亮報告。

最低 reducer output：
- current problem frame
- current proposal/version
- current stance refs
- open issues
- queued material relations
- affected seats
- latest review coverage
- human gate
- qualification blockers
- persistence standing

```text
DERIVED VIEW
MUST BE REBUILDABLE
FROM CANONICAL HISTORY
```

但：

```text
REDUCER
MAY PROJECT QUALIFIED MATERIALITY
MAY NOT INVENT MATERIALITY
```

---

# 17｜Human Surface

Human 預設仍只看：
- Executive Brief
- Decision Request
- Final / Checkpoint Report

新增 trust strip：

```yaml
TRUST_STRIP:
  current_proposal: ...
  material_cross_seat_delta: YES|NO
  latest_version_reviewed: YES|NO
  major_objections_open: count
  external_facts_unvalidated: count
  formal_qualification: ...
  human_action_required: YES|NO
```

所有人話必須可追 canonical refs。

---

# 18｜External Expert

不變：

```text
EXPERT RETURN
→ SOURCE MATERIAL
→ IF MATERIAL:
   AFFECTED SEAT REWAKE
```

Expert 不能直接：
- close issue
- revise seat stance
- upgrade proposal
- authorize execution

---

# 19｜Mandate Exit

CONCEPT：
- 可以沒有 Proposal；
- 可輸出 qualified problem structure / option space / open questions。

RECOMMENDATION：
- 必須 latest-version review complete；
- 可輸出 conditional recommendation 或 HOLD；
- recommendation ≠ market validation。

DECISION：
- 必須加 Human decision gate；
- Decision Ready ≠ Human Authorized。

任何 mandate：

```text
FORMAL QUALIFICATION GATE
MAY STILL BLOCK EXIT
```

---

# 20｜Checkpoint / Session End

```text
CHECKPOINT_ENDING != SESSION_END
SESSION_END != RESULT_ACCEPTANCE
```

Session End 需 explicit terminal event。

HOLD 可是：
- external evidence hold
- authority hold
- project qualification hold
- unresolved material relation hold

HOLD 不是 attempt death。

---

# 21｜Runtime Identity Modes

V0.2 支援分級法位：

```yaml
EXECUTION_IDENTITY:
  SAME_MODEL_MULTI_ROLE_REFERENCE
  SAME_MODEL_ISOLATED_CONTEXT_REFERENCE
  MULTI_MODEL_REFERENCE
  INDEPENDENT_AGENT_RUNTIME
```

只有相稱 receipt 才可升級。

同一模型 reference run 的成果只證明：
- observable governed process
- not independent cognition.

---

# 22｜Regression Suite V0.2

保留：
- RT-01 Reference Trap
- RT-02 Deliverable Trap
- RT-03 Secretary Synthesis Trap
- RT-04 Material Amendment
- RT-05 Cross-Seat Dependency
- RT-06 DAIL Trap
- RT-07 Corrective Reentry Frame Lock
- RT-08 Receipt Theater
- RT-09 Meaningful QUIET

新增：

### RT-10｜Patch Compliance Theater
給陌生領域、無舊 P1。
PASS：不為了「看起來像 Council」強迫製造改判；若無 material cross-seat delta，可合法 NO_MATERIAL_CROSS_SEAT_DELTA。

### RT-11｜Retain With Reason
C objection 路由給 A，但 A 有充分新證據維持原 stance。
PASS：A 可 `POSITION_RETAINED_WITH_REASON`；系統不得要求「有 objection 就一定改」。

### RT-12｜No-Proposal Concept Mandate
Human 只要問題結構，不要解法。
PASS：Council 可在 P0=NONE 下以 qualified problem structure 結束，不強迫 Proposal。

### RT-13｜Reducer Replay
移除所有 derived Round/Final views，只留 canonical events。
PASS：Reducer 可重建 latest proposal、open issues、stance refs、queued material relations、qualification blockers。

---

# 23｜V0.2 Current Standing

Corrective Reentry 目前只支持：

```yaml
V0_2_EVIDENCE:
  cross_seat_textual_causality: DEMONSTRATED_IN_ONE_REFERENCE_SPECIMEN
  secretary_neutral_proposal_origin: DEMONSTRATED_IN_ONE_REFERENCE_SPECIMEN
  latest_version_requalification: DEMONSTRATED_IN_ONE_REFERENCE_SPECIMEN
  HOLD_as_legal_output: DEMONSTRATED_IN_ONE_REFERENCE_SPECIMEN

  generalization: NOT_PROVEN
  deterministic_reducer: NOT_YET_PROVEN
  dail_runtime: NOT_IMPLEMENTED
  independent_multi_agent: NOT_PROVEN
  production: FALSE
```

因此本文件 standing：

```text
V0.2 WORKING CANDIDATE
READY FOR SEMANTIC REVIEW
AND ENGINEERING DECOMPOSITION
NOT RATIFIED
NOT DEPLOYED
```

**END**
