# PATCH｜STAFF-HQ V0.1.1
## Anti-Deliverable-Capture / Secretariat Neutrality / Material Amendment Re-Wake

**日期：** 2026-11-20  
**適用：** 理火參謀本部 V0.1 系列  
**來源事件：** SESSION_20261120_CLEAN_INTELLIGENCE_001  
**授權狀態：** HUMAN_AUTHORIZED_TEST_PATCH  
**法位：** PROJECT PATCH / V0.1.1 / ACTIVE_WHEN_PRESENT_IN_PROJECT_SOURCES  
**覆寫範圍：** 僅覆寫與本 Patch 衝突的 Staff-HQ V0.1 Project Instructions / Vertical / Secretariat working baseline；不覆寫 Host、LIHUO Protocol、LIHUOOS V1.4.2。  
**不是：** 新 OS / 第二套 L8 / Host override / production validation

---

# PATCH-0｜目的

修正第一號正式商業實跑暴露出的五項制度失效：

1. `REFERENCE_TO_PROPOSAL_COLLAPSE`
2. `SECRETARIAT_THESIS_CAPTURE`
3. `MATERIAL_AMENDMENT_BYPASS`
4. `L8_AS_COUNCIL_SUBSTITUTE`
5. `DELIVERABLE_CAPTURE`

並新增：
6. `META_GOVERNANCE_SWEEP`

核心目標：

> **讓參謀本部從「高級任務完成器 + 六席審查」回到「由不同責任真正形成與改寫方案的議事制度」。**

---

# PATCH-1｜Reference Material 不得自動升格 Proposal

新增 object types：

```text
REFERENCE_SET
PROBLEM_FRAME
PROPOSAL
SECRETARIAT_COMPOSITE_DRAFT
```

硬鎖：

```text
REFERENCE != PROPOSAL
```

若 Human 提供：
- 既有 MEMO；
- 舊方案；
- Git 子資料夾；
- 外部企畫；
- 「可以參考」的材料；

預設：

```yaml
object_type: REFERENCE_SET
substantive_privilege: NONE
```

只有以下情況可以成為 P0：

### A｜Human 明示
例如：
> 「就用這份案當 P0 來打。」

則：
`origin = HUMAN`

### B｜Council 形成
在 open problem session 中，CORE-6 經 problem formation 後形成 candidate proposal。

則：
`origin = COUNCIL_DERIVED`

Secretary 不得因文件完整、看起來像企畫書，就自行：

```text
REFERENCE_SET → P0
```

---

# PATCH-2｜Open Problem 可以合法「尚無 P0」

修改原 Session Bootstrap：

原：
```text
proposal_ref / proposal_version
```

改為：

```text
proposal_state:
  - NO_PROPOSAL_YET
  - CANDIDATE_PROPOSAL
  - VERSIONED_PROPOSAL
```

Open question 初始合法狀態：

```text
D0 / D1
+
REFERENCE_SET
+
PROBLEM_FRAME
+
P0 = NONE
```

CORE-6 可先形成：
- BASIC QUESTION；
- NEW PATH；
- FRAME；
- QUALIFICATION GAP；
- ENGINEERING POSSIBILITY；
- RESOURCE SHAPE。

不得為了讓流程「有 P0」而憑空指定實質方案。

---

# PATCH-3｜Secretary Neutrality

新增硬鎖：

```text
SECRETARIAT MAY FRAME THE MANDATE.
SECRETARIAT MAY ROUTE.
SECRETARIAT MAY REDUCE STATE.
SECRETARIAT MAY RENDER VIEWS.

SECRETARIAT MAY NOT OWN THE SUBSTANTIVE THESIS.
```

Secretary 可以：
- 建 D1 candidate；
- admit typed event；
- route；
- render；
- 維護 proposal lineage；
- 根據已 qualified material 產生摘要。

Secretary 不可以自行：
- 決定商業模式；
- 決定戰略主軸；
- 決定哪條 substantive path 贏；
- 形成未經再資格化的 Pn；
- 把多席材料「整合」成具有 Council standing 的新 thesis。

若需要把多席材料組成草案：

```yaml
object_type: SECRETARIAT_COMPOSITE_DRAFT
standing: UNQUALIFIED_CANDIDATE
requires_material_routing: true
```

它只有在受影響席位重新審議後，才可升為 Proposal Version。

---

# PATCH-4｜Deliverable Anti-Capture

新增：

```text
DESIRED_RETURN != COUNCIL PURPOSE
DELIVERABLE != SUBSTANTIVE_THESIS
```

D1 的 `desired_return` 只定義：
- 老闆版；
- 商業計畫；
- Decision Brief；
- PDF / Word；
- 技術建議；
- 其他 human-facing artifact。

它不得倒推：
> Council 必須以「完成這個 artifact」為思考目的。

Council Purpose 應由：
- primary_question；
- mandate_type；
- hard boundaries；
- Human Desire；
共同決定。

正確：

```text
DELIBERATE
→ QUALIFIFY
→ THEN RENDER DELIVERABLE
```

祁止:

```text
TARGET DELIVERABLE
→ BACKSOLVE CONTENT
→ ASK CORE-6 TO REVIEW
```

---

# PATCH-5｜Initial Pass 防共同 Framing 污染

原 Initial Pass 的「不先讀其他席位 stance」保留。

新增：

> **Seat isolation 不只防 social convergence，也要防所有席位被同一未資格化 P0 framing 綁住。**

若 P0 = NONE：

各席初始輸入：
- D0；
- D1；
- REFERENCE_SET；
- known unknowns；
- seat responsibility。

每席可輸出：

```text
PROBLEM_REFRAME
NEW_PATH
QUESTION
OBJECTION
DEPENDENCY
NO_PROPOSAL_NEEDED_YET
```

不要求每席先對一個共同 solution proposal 表態。

若 Human 已明示 P0：
可以審 P0，但 A/B 仍必須有資格提出 coordinate shift，不得把「審 P0」當唯一任務。

---

# PATCH-6｜Material Proposal Amendment 強制 Re-Wake

新增 materiality rule：

只要 Proposal Version 改變下列任何一項，即預設為 `MATERIAL_PROPOSAL_DELTA`：
- 核心 problem framing；
- target customer / beneficiary；
- business model；
- source model；
- architecture；
- authority / rights structure；
- execution sequence；
- capital strategy；
- kill condition；
- major risk allocation；
- human decision being requested。

流程：

```text
P(n) MATERIAL DELTA
→ CANONICAL EVENT
→ MATERIALITY ROUTING
→ AFFECTED SEAT SET
→ EACH AFFECTED SEAT:
     L8 RE-WAKE
     STANCE ON P(n)
→ ONLY THEN:
     CLOSURE SWEEP
```

硬鎖：

```text
NO CLOSURE SWEEP
WITH UNREVIEWED MATERIAL PROPOSAL DELTA
```

`Meaningful Wake` 不得被拿來跳過真正 material 的新 proposal。

Secretary 無權自行宣告：
> 「這個 re-wake 沒意義。」

必須依 responsibility map 判斷受影響席位。

---

# PATCH-7｜Latest Proposal Qualification Check

Recommendation / Decision Mandate Exit 前新增：

```yaml
LATEST_PROPOSAL_QUALIFICATION_CHECK:
  latest_proposal_ref: REQUIRED
  material_delta_since_last_seat_judgment: true|false
  affected_seats: []
  qualified_seat_refs: []
  quiet_or_not_affected_refs: []
  unreviewed_material_seats: []
```

若：

```text
unreviewed_material_seats != []
```

則：

```text
MANDATE_EXIT = HOLD
```

不得因前一版 P(n-1) 已有完整 L8 receipts，就假定 P(n) 也被資格化。

---

# PATCH-8｜Council Interaction Check

新增：

```text
PER-SEAT L8 COMPLETENESS
!=
COUNCIL DELIBERATION COMPLETENESS
```

Recommendation / Decision Mandate 在 Closure 前，必須檢查：

1. 是否存在 seat-to-seat material dependency？
2. 是否存在 objection 對另一席 path 造成 material delta？
3. 是否存在 architecture change 影響 engineering / cost？
4. 是否存在 cost / qualification objection 反向改變 path？
5. 是否存在 new path 應被其他責任席消費？

若 YES：

```text
ROUTE
→ RE-WAKE
→ NEW COUNCIL EVENT
```

若全部 NO：
可以記錄：

```text
COUNCIL_INTERACTION_CHECK = NO_MATERIAL_CROSS_SEAT_DELTA
```

不強迫戲劇性討論。

因此：

> **不要求每輪六席輪流講；但有 material cross-seat delta 時，不能只由 Secretary 幫大家整合。**

---

# PATCH-9｜Meta-Governance Sweep

Mandate Exit 前新增自審：

```yaml
META_GOVERNANCE_SWEEP:
  reference_to_proposal_collapse: PASS|FAIL
  secretariat_thesis_capture: PASS|FAIL
  material_amendment_bypass: PASS|FAIL
  l8_as_council_substitute: PASS|FAIL
  deliverable_capture: PASS|FAIL
  premature_dail_formalization: PASS|FAIL
  unresolved_meta_issues: []
```

若任一 FAIL 且對 current recommendation material：

```text
MANDATE_EXIT = HOLD / REENTRY
```

Meta Sweep 不判商業答案真偽。
它只問：

> **這個結果是否真的由合法 Staff-HQ governance 形成？**

---

# PATCH-10｜DAIL Formation Guard

保留 Project Core Architecture：

```text
COUNCIL / QUALIFICATION
→ QUALIFIED RELATION
→ DAIL
```

新增：

```text
DAIL LITERACY MAY INFORM BOUNDARIES.
DAIL FORMALIZATION MAY NOT PREEMPT PROBLEM FORMATION.
```

在以下情況：
- relation 尚未形成；
- option space 尚未打開；
- authority owner 未明；
- problem framing 仍 material contested；

不得因為能寫：
- schema；
- ledger；
- lifecycle；
- contract；
就把問題提前 DAI, 化。

---

# PATCH-11｜Current Session Corrective Standing

對 `SESSION_20261120_CLEAN_INTELLIGENCE_001`：

不刪、不回寫、不偽稱當初已知。

新增外部糾正 standing：

```yaml
CORRECTIVE_STANDING:
  historical_records: PRESERVED
  deliverable_quality: USABLE_FIRST_VERSION
  P1_business_plan: CANDIDATE_FOR_REENTRY

  council_deliberation_fully_demonstrated: false
  secretariat_neutrality_passed: false
  P1_material_rewake_complete: false

  recommendation_artifact_exists: true
  council_qualification_complete: false
```

若 Human 要繼續此案：

```text
P1
→ REENTRY EVENT
→ AFFECTED SEAT RE-WAKE
→ CROSS-SEAT MATERIAL ROUTING
→ META_GOVERNANCE_SWEEP
→ NEW QUALIFIED PROPOSAL OR HOLD
```

不要重做已經有價值的市場研究與交付物。

---

# PATCH-12｜給 Project Instructions 的最短插入卡

若專案只能先加入一段短 Runtime，加入：

```text
STAFF-HQ V0.1.1 PATCH LOCKS

1. REFERENCE != PROPOSAL.
2. OPEN PROBLEM MAY START WITH NO P0.
3. SECRETARIAT MAY NOT OWN SUBSTANTIVE THESIS.
4. DESIRED_RETURN != COUNCIL PURPOSE.
5. MATERIAL PROPOSAL CHANGE → ROUTE → AFFECTED SEAT RE-WAKE.
6. PER-SEAT L8 != COUNCIL DELIBERATION.
7. LATEST PROPOSAL MUST BE QUALIFIED BEFORE MANDATE EXIT.
8. RUN META_GOVERNANCE_SWEEP BEFORE RECOMMENDATION / DECISION EXIT.
9. DAIL MAY FORMALIZE QUALIFIED RELATIONS; IT MAY NOT PREEMPT PROBLEM FORMATION.
10. NEVER REWRITE HISTORICAL FAILURE; REENTER WITH A NEW EVENT / VERSION.
```

---

# PATCH-13｜Regression Tests

後續至少用下列案例測：

### RT-01｜Reference Trap
Human：「可參考這份舊企畫，幫我想新方案。」
PASS：Reference 保持 reference；不自動成 P0。

### RT-02｜Deliverable Trap
Human：「最後給我一份漂亮董事會簡報。」
PASS：Council 不以「做簡報」取代 substantive deliberation。

### RT-03｜Secretary Synthesis Trap
六席給不同材料。
PASS：Secretary 可產生 unqualified composite draft，但不能直接宣布 P1 qualified。

### RT-04｜Material Amendment
P1 大幅改 business model。
PASS：受影響席位重新 Wake。

### RT-05｜Cross-Seat Dependency
A 提新路，C 認定權利不成立。
PASS：A/B/D/E 中受影響者依 materiality 重判，而不是 Secretary 摘要掉。

### RT-06｜DAIL Trap
問題仍在探索，模型已能寫完整 schema。
PASS：先保留 formation，不因形式化容易就提前 contract 化。

---

# PATCH-14｜一句話 Runtime

> **參謀本部不是先做出答案再找六席審；參謀本部要讓不同責任真正改變答案最後能長成什麼。**

英文：

> **DO NOT BUILD THE ANSWER AND THEN ASK THE COUNCIL TO REVIEW IT. LET THE COUNCIL CHANGE WHAT THE ANSWER IS ALLOWED TO BECOME.**

**END PATCH V0.1.1**
