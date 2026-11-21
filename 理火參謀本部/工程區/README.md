# 工程區

此區負責把理火參謀本部從概念程序推向可測的垂直系統。

## 最新 Staff-HQ 主程式工作載入候選

**V0.3.1-RUNTIME-CORE-AI-NATIVE-WORKING｜2026-11-21**（Git 已整合 Enhanced A–K CP3，仍 NOT_RATIFIED / NOT_HOST_DEPLOYED）

[現行最新下一代候選](STAFF_HQ_V0.2_RUNTIME_PACKAGE/DEPLOY/STAFF_HQ_V0.3.1_RUNTIME_CORE_AI_NATIVE_WORKING_20261121.md)；其餘下方 V0.3.0 說明為**前一版歷史形成過程**，不是現行最新候選。

### V0.3.0 歷史載入候選（非最新）

**V0.3.0-WORKING-FULL｜2026-11-21**

`STAFF_HQ_V0.2_RUNTIME_PACKAGE/DEPLOY/STAFF_HQ_V0.3.0_RUNTIME_FULL_WORKING_20261121.md`

- 在 V0.2.1 技術基底上整合 F Experimental Shadow Seat。
- CORE-6 保持 N1/A/B/C/D/E，不升格 CORE-7。
- F 專責結構維持負擔的時間演化、成本承擔與轉移、維持／修復／轉換路徑。
- 正式 Vertical V0.1 的 current standing 不因本候選檔存在而改變。
- NOT_RATIFIED / NOT_HOST_DEPLOYED / F predictive value NOT_PROVEN。

V0.2.1 主程式與 V0.2 拆分包均保留為歷史來源，不覆寫。

## 工程研究方向

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
16. F Shadow Seat：Structural Cost Trajectory / Cost Transfer / Repair Window / Maintenance-vs-Transition Replay

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
METHOD ROUTING != HIDDEN ATTENTION-WEIGHT CONTROL
FIRST OBSERVATION TRACE = FUNCTIONAL / SEMANTIC OBSERVATION ENTRY
F SHADOW OBSERVATION != FORMAL COUNCIL STANCE
```

重要歷史教訓：CG 二十輪會議曾出現長程高張力下的角色漂移，因此跨輪身份、狀態快照與重入驗證不得被當成 UI 細節。

目前沒有獨立 Runtime / Host deployment claim。

## V0.3.0 寫入稽核

- [V0.3.0 Git Persistence Audit](STAFF_HQ_V0.2_RUNTIME_PACKAGE/DEPLOY/STAFF_HQ_V0.3.0_GIT_PERSISTENCE_AUDIT_20261121.md)


## 2026-11-21｜AI-Native / V0.3.1 main program candidate
- [V0.3.1 Runtime Core](STAFF_HQ_V0.2_RUNTIME_PACKAGE/DEPLOY/STAFF_HQ_V0.3.1_RUNTIME_CORE_AI_NATIVE_WORKING_20261121.md)
- [Install List (one new MD file)](STAFF_HQ_V0.2_RUNTIME_PACKAGE/DEPLOY/GPT_PROJECT_INSTALL_LIST_V0.3.1_WORKING_20261121.md)
- [CP Reference Replay + 14-check tests](AI_NATIVE_CP_REFERENCE_V0.1_20261121/REFERENCE_TEST_REPORT.md)
- [Source provenance / PDF standing](AI_NATIVE_CP_REFERENCE_V0.1_20261121/SOURCE_PROVENANCE.md)
**Non-overwriting:** V0.3.0 full remains previous working load candidate, formal Vertical V0.1 unchanged.


## Stage 2A 首席驗收承接｜下一代 CP3 Enhanced A–K 候選
- [V0.3.1 主程式 CP3 §10A](STAFF_HQ_V0.2_RUNTIME_PACKAGE/DEPLOY/STAFF_HQ_V0.3.1_RUNTIME_CORE_AI_NATIVE_WORKING_20261121.md)；[DAIL 語義契約](STAFF_HQ_V0.2_RUNTIME_PACKAGE/DEPLOY/CP3_ENHANCED_AK_DAIL_NEXTGEN_CANDIDATE_20261121.yaml)。
- [Secretariat V0.2 §7A](../MEMO區/SECRETARIAT_ARCHITECTURE_V0.2_AI_NATIVE_CANONICAL_HUMAN_PROJECTION_CANDIDATE_20261121.md)、[Stage 2A 結論](../研究區/COUNCIL_REPORT_STAGE_2A_STRUCTURAL_ABLATION_20261121/03_STAGE2A_STRUCTURAL_COMPARISON_AND_RECOMMENDATION.md)、[人類轉交首席驗收來源](../研究區/COUNCIL_REPORT_STAGE_2A_STRUCTURAL_ABLATION_20261121/06_HUMAN_REPORTED_CHIEF_ACCEPTANCE_AND_NEXTGEN_SCOPE_20261121.md)。
- **版本鏈**：V0.3.0 歷史全本 → V0.3.1 AI-native Working Core（Git pre-integration blob `a63017298d4e93cd18b83dddf1ed48a516bd7e28`）→ **同一 V0.3.1 下一代候選內 CP3 Enhanced A–K Stage 2A 增量**。本次不自創 V0.3.2 或 Current Cutover。