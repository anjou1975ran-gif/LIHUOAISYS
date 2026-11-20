# STAFF-HQ V0.2 RATIFICATION & CUTOVER CHECKLIST V0.1
## 從 Working Candidate 升為 Current Vertical 的合法門

**版本：** V0.1-WORKING  
**日期：** 2026-11-20  
**法位：** RATIFICATION_CHECKLIST / NOT_RATIFIED / NO_AUTOMATIC_CUTOVER

---

# 0｜原則

> **文件完成不等於 Runtime 成立；一次成功案例不等於 Vertical 已普遍驗證。**

V0.2 cutover 必須是 explicit event，不得因檔案存在自動發生。

---

# 1｜Semantic Gate

必須確認：

- C0–C5 語義無 unresolved owner conflict
- materiality owner 邊界清楚
- Secretariat authority 無 thesis capture
- Proposal lifecycle 無 reference collapse
- Cross-seat lifecycle 保留 DELIVERED/CONSUMED/RESPONDED 區分
- HOLD / reentry / Human gate 語義明確
- DAIL / IR / Code 邊界與 Protocol V5.1.0 一致

結果：

```text
SEMANTIC_GATE = PASS|HOLD
```

---

# 2｜MRC-001 Engineering Gate

至少：
- canonical event store / normalized fixture exists
- deterministic reducer implementation exists
- same log replay deterministic
- ProposalVersion lineage reconstructed
- MaterialRelation state reconstructed
- exact-version review coverage reconstructed
- Human / qualification gates projected
- derived report deletion does not break replay

```text
MRC001 = PASS
```

否則 V0.2 不 cutover。

---

# 3｜Regression Gate

至少：
- RT-01~RT-13 executed
- PT-01~PT-12 executed
- failures resolved or explicitly HOLD
- RT-10 Patch Compliance Theater not gamed

一個 reference specimen pass 不等於 suite pass。

---

# 4｜Second Specimen Gate

至少再跑一個：

```text
REFERENCE_SPECIMEN_002
```

條件：
- unfamiliar domain
- no inherited P1
- no instruction that visible revision must occur
- allow NO_MATERIAL_CROSS_SEAT_DELTA
- preferably blinded against RT-10 expected result

目的：
- 測 generalization
- 測 patch compliance theater
- 測 formation independence

---

# 5｜Training Gate Reconciliation

現況：

```text
LIHUO_PROJECT_QUALIFIED = FALSE
```

V0.2 ratification 不得偷偷補發 Training Qualification。

必須另行：
- complete / reconcile Q1–Q18
- or Human/authorized owner formally revise training gate with traceable reason

在未解前：

```text
FORMAL_COUNCIL_QUALIFICATION = HOLD
```

即使 V0.2 engineering pass。

---

# 6｜Project Instructions Gate

準備：
- V0.2 Project Instructions candidate
- current source load order
- version conflict rule
- current Training Status pointer
- execution identity rule

Ratification 時才：
- activate V0.2 Instructions
- mark V0.1 predecessor / historical baseline
- do not delete V0.1

---

# 7｜Cutover Event Candidate

只有 Human / authorized owner 可建立：

```yaml
STAFF_HQ_VERTICAL_CUTOVER:
  from: V0.1
  to: V0.2
  semantic_gate: PASS
  MRC001_gate: PASS
  regression_gate: PASS
  specimen_gate: PASS
  training_gate_standing:
  project_instructions_ref:
  effective_time:
  supersedes_operationally:
    - V0.1_CURRENT_RUNTIME
  preserves_history:
    - V0.1_FILES
    - FAILURE_SPECIMENS
    - REENTRY_SPECIMENS
```

若任何 required gate 未通過：

```text
CUTOVER = HOLD
```

---

# 8｜V0.2 Cutover 後仍不能宣稱

即使 ratified，也不自動代表：
- independent multi-agent runtime
- production scaling
- cost advantage
- superior benchmark
- Host deployment
- universal generalization

各自仍需獨立 evidence。

---

# 9｜Current Checklist Standing

```yaml
CURRENT:
  semantic_gate: WORKING
  MRC001_engineering: NOT_IMPLEMENTED
  regression: NOT_RUN_AS_FULL_SUITE
  second_specimen: NOT_RUN
  training_gate: FALSE
  project_instructions_v0_2: CANDIDATE_READY
  cutover: NOT_AUTHORIZED
```

**END**
