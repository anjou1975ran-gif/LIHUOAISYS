# STAFF-HQ V0.2 RUNTIME PACKAGE
## 理火參謀本部｜真正議事型 Vertical 整合包

**版本：** V0.2-WORKING PACKAGE  
**日期：** 2026-11-20  
**法位：** PROJECT_VERTICAL_RUNTIME_PACKAGE / WORKING / NOT_RATIFIED / NOT_DEPLOYED  
**Canonical package home：** `理火參謀本部/工程區/STAFF_HQ_V0.2_RUNTIME_PACKAGE/`

---

# 0｜用途

此子夾把「真正議事型 Staff-HQ Vertical」目前需要放進 GPT Project／工程實作線的核心文件集中在一起。

它不是第二套理火 OS，也不是 Host 部署包。

```text
LIHUO PROTOCOL
>
LIHUOOS V1.4.2
>
STAFF-HQ PROJECT CORE
>
THIS V0.2 PACKAGE
>
SESSION
```

核心目標：

> **把「誰有權提出、誰被 material affect、誰必須重新判斷、哪一版被誰審過、何時只能 HOLD」變成可保存、可重播、可測試的 Council governance runtime。**

---

# 1｜包內文件

1. `01_STAFF_HQ_DAIL_MINIMUM_RELATION_SET_V0.1.md`  
   最小 DAIL 關係語義；C0–C5。

2. `02_VERTICAL_LIHUOOS_V1.4.2_StaffHQ_V0.2_WORKING.md`  
   真正議事型 Vertical 候選。

3. `03_MRC001_MINIMUM_IR_SPEC_V0.1.md`  
   Minimum Replayable Council 的最小 IR。

4. `04_MRC001_DETERMINISTIC_REDUCER_SPEC_V0.1.md`  
   Canonical Event → Current State 的 deterministic reducer／replay 規格。

5. `05_MRC001_ROUTER_AND_QUALIFICATION_ENGINE_SPEC_V0.1.md`  
   Rule-bound routing、MaterialRelation accounting、exact-version qualification。

6. `06_REGRESSION_SUITE_V0.2.md`  
   RT-01～RT-13 + property tests。

7. `07_IMPLEMENTATION_BACKLOG_V0.2.md`  
   工程建置次序與 MRC-001 milestone。

8. `08_GPT_PROJECT_INSTALL_CARD_V0.1.md`  
   真正要放進 GPT Project 的最小檔案清單與來源順序。

9. `09_GPT_PROJECT_INSTRUCTIONS_StaffHQ_V0.2_WORKING.md`  
   V0.2 Project Instructions 候選正文；ratification 前不啟用。

10. `10_RATIFICATION_AND_CUTOVER_CHECKLIST_V0.1.md`  
   V0.2 從 Working Candidate 升為 current vertical 的合法門。

---

# 2｜哪些是語義，哪些是工程

```text
01 = DAIL SEMANTICS
02 = VERTICAL GOVERNANCE
03 = IR
04 = REDUCER / REPLAY
05 = ROUTER / QUALIFICATION
06 = TESTS
07 = ENGINEERING ORDER
08 = PROJECT INSTALL / LOAD ORDER
09 = PROJECT INSTRUCTIONS CANDIDATE
10 = RATIFICATION / CUTOVER
```

不得倒置：

```text
CODE
MAY IMPLEMENT
01/02 QUALIFIED SEMANTICS

CODE
MAY NOT
REWRITE 01/02 SEMANTICS
```

---

# 3｜目前 current standing

```yaml
PACKAGE:
  semantic_set: WORKING
  vertical: V0.2_WORKING_CANDIDATE
  IR: SPECIFIED_CANDIDATE
  reducer: SPECIFIED_NOT_IMPLEMENTED
  router: SPECIFIED_NOT_IMPLEMENTED
  qualification_engine: SPECIFIED_NOT_IMPLEMENTED
  regression_suite: DEFINED
  code: NOT_IMPLEMENTED
  replay: NOT_PROVEN
  independent_multi_agent: NOT_PROVEN
  host_deployment: FALSE
```

V0.1 Vertical 仍是 current working baseline，直到 V0.2 完成 ratification／regression，不因本 package 存在而自動 supersede。

---

# 4｜Reference specimen

第一個 replay fixture：

```text
SESSION_20261120_CLEAN_INTELLIGENCE_001_REENTRY_001
= REFERENCE_SPECIMEN_001
```

用途：
- canonical replay
- cross-seat causality
- latest P2 review
- HOLD projection
- anti-secretary-thesis

不代表：
- generalization proof
- multi-agent proof
- production proof

---

# 5｜一句話工程門檻

> **刪掉最後報告，只留下 Canonical Events；若仍能重建誰影響誰、P2 怎麼形成、誰審哪一版、為何 HOLD，MRC-001 才成立。**

**END**
