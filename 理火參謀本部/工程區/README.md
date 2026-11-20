# 工程區

此區負責把理火參謀本部從概念程序推向可測的垂直系統。

目前優先工程題目：

1. Method Routing / 心法選擇與版本鎖定
2. First-Observation Trace / 第一觀察入口紀錄
3. Proposal Schema / Version Graph
4. Seat Identity + Role Persistence
5. Stance State Model
6. Persuasion / Position-Revision Trace
7. Objection Graph
8. Amendment / Condition / New-Path linkage
9. Round Snapshot / Re-entry Anchor
10. Secretary Record Integrity
11. Decision Replay
12. Execution Handoff / Return-to-Council
13. Benchmark：Normal Agent Control vs Generic Multi-Agent vs LIHUO Staff
14. Method-Pack Ablation：同模型同席位，有／無心法時第一觀察入口與結果差異
15. Role Drift / Conformity / Premature Consensus failure tests

## 第一階段工程鏈

```text
PROPOSAL
↓
METHOD ROUTING
↓
METHOD VERSION LOCK
↓
FIRST OBSERVATION TRACE
↓
SEAT ANALYSIS
↓
COUNCIL ROUNDS
↓
STANCE / OBJECTION / PERSUASION TRACE
↓
DECISION PROVENANCE
```

重要邊界：

```text
METHOD ROUTING
!=
HIDDEN ATTENTION-WEIGHT CONTROL

FIRST OBSERVATION TRACE
=
FUNCTIONAL / SEMANTIC OBSERVATION ENTRY
```

重要歷史教訓：CG 二十輪會議曾出現長程高張力下的角色漂移，因此跨輪身份、狀態快照與重入驗證不得被當成 UI 細節。

目前沒有獨立 Runtime / Host deployment claim。
