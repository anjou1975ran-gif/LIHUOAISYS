# GIT REPOSITORY BRIDGE｜理火參謀本部 V0.1

**版本：** V0.1  
**日期：** 2026-11-20  
**用途：** ChatGPT Project 讀取／核對目前理火參謀本部正式基線與測試紀錄的 Git 入口。

---

# 1｜Repository

~~~text
Repository:
https://github.com/anjou1975ran-gif/LIHUOAISYS

Branch:
main

Staff-HQ Root:
理火參謀本部/
~~~

GitHub browser root:

https://github.com/anjou1975ran-gif/LIHUOAISYS/tree/main/理火參謀本部

---

# 2｜Current Staff-HQ Runtime Sources

## Baseline

~~~text
理火參謀本部/MEMO區/
MEMO_Secretariat_Architecture_V0.1_FIRST_BASELINE_20261120.md
~~~

## LIHUOOS Vertical

~~~text
理火參謀本部/工程區/
VERTICAL_LIHUOOS_V1.4.2_理火參謀本部_V0.1_20261120.md
~~~

## GPT Project Runtime Card

~~~text
理火參謀本部/工程區/
GPT_PROJECT_RUNTIME_CARD_理火參謀本部_V0.1_20261120.md
~~~

## Meeting / Record Contract

~~~text
理火參謀本部/記錄區/
MEETING_RECORD_AND_CHAT_SURFACE_V0.1_20261120.md
~~~

## Human Decision Gate

~~~text
理火參謀本部/記錄區/
HUMAN_DECISION_REQUEST_SPEC_V0.1_20261120.md
~~~

---

# 3｜Test Sessions

## TEST-001｜Secretary Kernel Self-Audit

Meeting:

~~~text
理火參謀本部/會議區/SESSION_TEST001_SECRETARY_KERNEL/
~~~

Record:

~~~text
理火參謀本部/記錄區/SESSION_TEST001_SECRETARY_KERNEL/
~~~

Standing:
- COMPLETED
- V0.1 first baseline produced
- same-model multi-role reference
- not production multi-agent proof

## TEST-002｜LIHUOOS V1.4.2 Project Bootstrap

Meeting:

~~~text
理火參謀本部/會議區/SESSION_TEST002_PROJECT_BOOTSTRAP/
~~~

Record:

~~~text
理火參謀本部/記錄區/SESSION_TEST002_PROJECT_BOOTSTRAP/
~~~

Standing:
- ACTIVE TEST
- LIHUOOS V1.4.2 Vertical bound
- per-seat L8 SGER / Compact Receipt enabled
- Meaningful Wake behavior under test

---

# 4｜Git Usage Rule

When GitHub access is available:

~~~text
PROJECT SOURCE
=
CURRENT RUNTIME / BASELINE

GIT
=
LIVE TEST RECORD / HISTORY / AUDIT SOURCE
~~~

Use Git to:
- inspect latest Session state;
- verify a claimed Git persistence write;
- read Round / Event / L8 records;
- compare current candidate vs prior version;
- inspect test history.

Do not infer current standing from an old session or superseded memo when a newer current baseline exists.

---

# 5｜Standing Locks

~~~text
GIT FILE EXISTS
!=
HOST DEPLOYED

TEST RECORD EXISTS
!=
PRODUCTION VALIDATED

SAME_MODEL_MULTI_ROLE_REFERENCE
!=
INDEPENDENT MULTI_AGENT RUNTIME

CURRENT PROJECT BASELINE
!=
FINAL CONSTITUTION
~~~

**END**
---

# 6｜V0.3.0 Working Load Candidate（2026-11-21）

**Single-file main runtime:**

```text
理火參謀本部/工程區/STAFF_HQ_V0.2_RUNTIME_PACKAGE/DEPLOY/
STAFF_HQ_V0.3.0_RUNTIME_FULL_WORKING_20261121.md
```

Standing:
- PROJECT_RUNTIME_WORKING_LOAD_CANDIDATE
- NOT_RATIFIED
- NOT_HOST_DEPLOYED
- CORE-6 unchanged: N1/A/B/C/D/E
- F = EXPERIMENTAL_SHADOW_SEAT / NOT_CORE7

V0.3.0 在 V0.2.1 技術基底上加入 F 的 Structural Cost trajectory、Cost Bearer / Cost Transfer、Maintenance-vs-Transition、Repair Capacity / Repair Window 研究責任。F 不參與正式表決、quorum 或 exact-version review coverage。

正式 Vertical V0.1 仍是 current baseline，直到明確 Ratification / Cutover Event。V0.2.1 與 V0.2 保留為歷史來源。
