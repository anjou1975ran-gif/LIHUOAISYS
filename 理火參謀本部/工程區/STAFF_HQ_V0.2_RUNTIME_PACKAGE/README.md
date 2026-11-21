# STAFF-HQ V0.2 / V0.2.1 / V0.3.0 / V0.3.1 RUNTIME PACKAGE
## 理火參謀本部｜真正議事型 Vertical 整合包

**最新 Project 工作載入候選：** V0.3.1-RUNTIME-CORE-AI-NATIVE-WORKING（已整合 CP3 Enhanced A–K 候選）  
**歷史基底：** V0.2.1-WORKING-FULL  
**日期：** 2026-11-21  
**法位：** PROJECT_RUNTIME_WORKING_LOAD_CANDIDATE / NOT_RATIFIED / NOT_DEPLOYED  
**Canonical package home：** `理火參謀本部/工程區/STAFF_HQ_V0.2_RUNTIME_PACKAGE/`

---

# 0｜用途

此子夾保存 Staff-HQ 的單檔工作 Runtime、工程拆分規格、版本歷史與安裝說明。

它不是第二套理火 OS，也不是 Host 部署包。

```text
LIHUO PROTOCOL
>
LIHUOOS V1.4.2
>
STAFF-HQ PROJECT CORE
>
STAFF-HQ V0.3.1 WORKING LOAD CANDIDATE
>
SESSION
```

---

# 1｜單檔 Deploy

**GPT Project 的 Staff-HQ 主程式只載入以下一檔：**

```text
DEPLOY/
  STAFF_HQ_V0.3.1_RUNTIME_CORE_AI_NATIVE_WORKING_20261121.md
```

V0.3.0、V0.2.1 與 V0.2 主程式保留歷史，不與 V0.3.1 同時作為 Project Runtime 載入。**採用仍須明確人類 Cutover，Git 不等於安裝。**

01–10 拆分文件保留為：
- engineering source；
- diff / audit；
- 模組級修訂依據；
- 回歸與實作來源。

它們不是第二份 Project Load Truth。

完整 Project 上位來源依 V0.3.0 Install Card：
- LIHUO Protocol V5.1.0；
- LIHUOOS V1.4.2；
- Staff-HQ Project Core Architecture；
- 正式 current Vertical V0.1（在明確 Cutover 前）；
- Secretariat Architecture；
- Meeting Record / Chat Surface；
- Human Decision Request；
- Git Bridge。

---

# 2｜V0.3.0 增量

V0.3.0 在 V0.2.1 技術基底上新增：

- F Experimental Shadow Seat；
- Structural Cost Profile 的時間演化研究；
- Cost Bearer / Cost Transfer；
- Maintenance vs Repair vs Transition 路徑比較；
- Repair Capacity / Repair Window；
- F 與 CORE-6 / Radar / L8 / Canonical Event 的邊界；
- F 的 QUIET、實驗門與市場研究驗證邊界。

**CORE-6 保持 N1/A/B/C/D/E。F 不屬於 CORE-7，不投票、不計 quorum、不計正式 review coverage。**

---

# 3｜目前 standing

```yaml
PACKAGE:
  V0_3_0: WORKING_LOAD_CANDIDATE
  formal_vertical_current: V0.1
  F: EXPERIMENTAL_SHADOW_SEAT
  F_incremental_value: NOT_PROVEN
  MRC001: SPECIFIED_NOT_IMPLEMENTED
  reducer: SPECIFIED_NOT_IMPLEMENTED
  router: SPECIFIED_NOT_IMPLEMENTED
  qualification_engine: SPECIFIED_NOT_IMPLEMENTED
  regression_suite: DEFINED_NOT_FULLY_EXECUTED
  training_gate: FALSE
  independent_multi_agent: NOT_PROVEN
  host_deployment: FALSE
```

V0.3.0 檔案存在不代表 Project 已載入；Git 寫入成功不代表 Host 部署。

**END**

## 4｜V0.3.0 Persistence Audit

- [V0.3.0 Git Persistence Audit](DEPLOY/STAFF_HQ_V0.3.0_GIT_PERSISTENCE_AUDIT_20261121.md)
- Main Runtime blob SHA: `095c3eb799d0f1e89bff8cf3a898cd2c87add7a8`
- Main Runtime readback verified after commit `93f0dfc7015ee8c2e116d303139fee3cab7f2228`.


## 2026-11-21｜V0.3.1 AI-Native Candidate
- [New one-file working core](DEPLOY/STAFF_HQ_V0.3.1_RUNTIME_CORE_AI_NATIVE_WORKING_20261121.md)
- [GPT Project Install List](DEPLOY/GPT_PROJECT_INSTALL_LIST_V0.3.1_WORKING_20261121.md)
- [Migration/Regression Plan](DEPLOY/STAFF_HQ_V0.3.1_MIGRATION_AND_REGRESSION_20261121.md)
Current V0.3.0 full body preserved as audit and on-demand engineering detail; do not simultaneously load both.


## Stage 2A｜Enhanced A–K Candidate Integration（2026-11-21）
- **[單檔最新候選主程式](DEPLOY/STAFF_HQ_V0.3.1_RUNTIME_CORE_AI_NATIVE_WORKING_20261121.md)**：§10A 寫入 `WHAT_CHANGED_BECAUSE_OF_THIS_MEETING`／`OBJECTION_LIFECYCLE` 的 A–K 報告語義要求。
- **[DAIL CP3 語義契約](DEPLOY/CP3_ENHANCED_AK_DAIL_NEXTGEN_CANDIDATE_20261121.yaml)**：不另造 Current L9 capability，不另載入第二 Runtime。
- **[Secretariat V0.2 候選](../../MEMO區/SECRETARIAT_ARCHITECTURE_V0.2_AI_NATIVE_CANONICAL_HUMAN_PROJECTION_CANDIDATE_20261121.md)**：§7A／CP09–13。原 `MEETING_RECORD_AND_CHAT_SURFACE_V0.1` §11 Current 本體未改。
- **[Stage 2A 與首席驗收承接](../../研究區/COUNCIL_REPORT_STAGE_2A_STRUCTURAL_ABLATION_20261121/06_HUMAN_REPORTED_CHIEF_ACCEPTANCE_AND_NEXTGEN_SCOPE_20261121.md)**：版本鏈中的批准範圍。
- 原 V0.3.1 Core blob `a63017298d4e93cd18b83dddf1ed48a516bd7e28`、原 Secretariat V0.2 blob `2fea4d9af4fa0419610bef361de30fa6d70295fb` 均可按 Git SHA 回查；更動只發生在 Working Candidate（非 Current）。

- **[Stage 2A Enhanced A–K Git 整合／Current 不變審計](DEPLOY/STAFF_HQ_V0.3.1_ENHANCED_AK_STAGE2A_INTEGRATION_AUDIT_20261121.md)**：候選法位、Git 回讀、來源 SHA、Stage 2B 開放缺口。
