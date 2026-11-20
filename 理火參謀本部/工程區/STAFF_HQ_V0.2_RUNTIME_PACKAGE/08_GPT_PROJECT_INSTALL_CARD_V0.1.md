# GPT PROJECT INSTALL CARD｜Staff-HQ V0.2 Runtime Package
## 要存哪些、放哪裡、讀取順序

**版本：** V0.1-WORKING  
**日期：** 2026-11-20  
**用途：** 將參謀本部真正垂直程序放入 GPT Project 時的最小安裝清單。  
**法位：** PROJECT_INSTALL_GUIDE / NOT_HOST_DEPLOYMENT

---

# 0｜最簡單答案

若要把 Staff-HQ V0.2 放入 GPT Project，**不要把整個 Git 倉庫全塞進 Project Sources**。

保留上位來源 + 本 package。

---

# 1｜Project Sources 必放

## A｜上位治理

1. `00_LIHUO_PROTOCOL_V5.1.0_FULL_BODY_RATIFIED_20261014.md`
2. `理火OSV1.4.2(點燈回歸).md`

這兩份不放在本 package 內，因為它們是上位 source of truth，不應被複製成 Project Vertical 私有版本。

## B｜Staff-HQ Project Core

3. `PROJECT_CORE_ARCHITECTURE_DAIL_OPERATING_MODEL_V0.1_20261120.md`

## C｜本子夾整包

將：

```text
理火參謀本部/工程區/STAFF_HQ_V0.2_RUNTIME_PACKAGE/
```

整個子夾作為 Staff-HQ V0.2 工程／Runtime source。

其中 GPT Project runtime 最重要：
- 01 DAIL Minimum Relation Set
- 02 Vertical V0.2
- 03 Minimum IR
- 04 Reducer
- 05 Router/Qualification
- 06 Regression Suite

07/08 是工程與安裝文件，可放但不取得高於 01/02 的語義權限。

---

# 2｜仍建議放入的既有 Staff-HQ 治理文件

若 Project Sources 容量允許：

- `MEMO_Secretariat_Architecture_V0.1_FIRST_BASELINE_20261120.md`
- `MEETING_RECORD_AND_CHAT_SURFACE_V0.1_20261120.md`
- `HUMAN_DECISION_REQUEST_SPEC_V0.1_20261120.md`
- `GIT_REPOSITORY_BRIDGE_理火參謀本部_V0.1_20261120.md`
- `PATCH_STAFF_HQ_V0.1.1_反交付綁架_秘書處中立_重大修正重喚醒_20261120.md`

V0.1 Vertical 可保留作 predecessor / history，但正式 runtime selection 必須明確指定 current version，避免 V0.1/V0.2 同時搶 current standing。

---

# 3｜Reference / Test Sources

只在測試或 replay 時掛：

```text
SESSION_20261120_CLEAN_INTELLIGENCE_001_REENTRY_001
```

它是：
- REFERENCE_SPECIMEN_001
- replay fixture

不是：
- current runtime instruction
- universal theory
- commercial truth

原失敗 Session：
`SESSION_20261120_CLEAN_INTELLIGENCE_001`
保留作 failure specimen，不需每次 runtime 常駐。

---

# 4｜建議 Project Source Load Order

```text
1 HOST / PLATFORM
2 LIHUO Protocol V5.1.0
3 LIHUOOS V1.4.2
4 Staff-HQ Project Core Architecture
5 Package 01 DAIL Minimum Relation Set
6 Package 02 Vertical V0.2
7 Secretariat / Meeting / Decision Request specs
8 Package 03 IR
9 Package 04 Reducer
10 Package 05 Router / Qualification
11 Package 06 Regression
12 Git Bridge / Engineering Backlog
13 Current Session
14 Reference Specimens only when needed
```

---

# 5｜GPT Project Instructions 要改什麼

現行：
`GPT_PROJECT_INSTRUCTIONS_理火參謀本部_V0.1_20261120.md`

未來應出：
`GPT_PROJECT_INSTRUCTIONS_理火參謀本部_V0.2.md`

但在 V0.2 ratification 前，不直接覆寫 V0.1。

V0.2 Project Instructions 至少要引用：

```text
PROJECT CORE
+
PACKAGE 01
+
PACKAGE 02
+
SECRETARIAT SPECS
+
PACKAGE 03/04/05 RUNTIME CONTRACTS
```

並保留：
- Training Gate standing
- execution identity
- no fake deployment
- no hidden CoT
- Git persistence truth

---

# 6｜不需要放進 Project Sources 的東西

除非特定工作需要，不建議常駐：

- 全部理火散記
- 全部商業案例
- 全部歷史會議
- 所有舊版 Staff-HQ test logs
- 所有最終報告
- 所有 seat receipts

理由：

> Runtime source 應治理生成；Corpus / specimen 應在需要時才取用，避免歷史答案污染新的 formation。

---

# 7｜部署前最小檢查

```yaml
INSTALL_CHECK:
  protocol_present: REQUIRED
  lihuoos_present: REQUIRED
  project_core_present: REQUIRED
  package_01_present: REQUIRED
  package_02_present: REQUIRED
  secretariat_spec_present: REQUIRED
  IR_reducer_router_specs_present: REQUIRED_FOR_MRC001
  current_training_status_known: REQUIRED
  current_vertical_version_explicit: REQUIRED
  execution_identity_explicit: REQUIRED
```

若 current vertical version 不明：

```text
RUNTIME START = HOLD_VERSION_CONFLICT
```

---

# 8｜目前建議實際放法

Git 中集中：

```text
理火參謀本部/
  工程區/
    STAFF_HQ_V0.2_RUNTIME_PACKAGE/
      README.md
      01_STAFF_HQ_DAIL_MINIMUM_RELATION_SET_V0.1.md
      02_VERTICAL_LIHUOOS_V1.4.2_StaffHQ_V0.2_WORKING.md
      03_MRC001_MINIMUM_IR_SPEC_V0.1.md
      04_MRC001_DETERMINISTIC_REDUCER_SPEC_V0.1.md
      05_MRC001_ROUTER_AND_QUALIFICATION_ENGINE_SPEC_V0.1.md
      06_REGRESSION_SUITE_V0.2.md
      07_IMPLEMENTATION_BACKLOG_V0.2.md
      08_GPT_PROJECT_INSTALL_CARD_V0.1.md
```

上位 Protocol / OS / Project Core 留在原 canonical home，不複製進子夾，避免 source-of-truth 漂移。

---

# 9｜現在不要做的事

不要現在：
- 宣告 V0.2 ratified
- 覆寫 V0.1 current baseline
- 開始 dynamic seats
- 加 voting/score
- 寫自動 consensus
- 宣稱 independent agents
- 宣稱 DAIL runtime completed

下一合法工程入口：

```text
MRC-001 IMPLEMENTATION
→ CANONICAL STORE
→ REDUCER
→ REPLAY REFERENCE_SPECIMEN_001
```

**END**
