# STAFF-HQ V0.2 / V0.2.1 / V0.3.0 RUNTIME PACKAGE
## 理火參謀本部｜真正議事型 Vertical 整合包

**最新 Project 工作載入候選：** V0.3.0-WORKING-FULL  
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
STAFF-HQ V0.3.0 WORKING LOAD CANDIDATE
>
SESSION
```

---

# 1｜單檔 Deploy

**GPT Project 的 Staff-HQ 主程式只載入以下一檔：**

```text
DEPLOY/
  STAFF_HQ_V0.3.0_RUNTIME_FULL_WORKING_20261121.md
```

V0.2.1 與 V0.2 主程式保留歷史，不與 V0.3.0 同時作為 Runtime 載入。

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
