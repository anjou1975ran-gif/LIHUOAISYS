
# MEMO｜理火參謀本部 Secretariat Architecture V0.1
## 第一版工作基線

**版本：** V0.1  
**日期：** 2026-11-20  
**法位：** FIRST_VERSION_BASELINE / WORKING  
**來源：** TEST-001-SECRETARY-KERNEL  
**不是：** FINAL CONSTITUTION / ENGINEERING VALIDATED / COST VALIDATED / BENCHMARK PROVEN / HOST DEPLOYED

---

# 0｜第一版一句話

> **理火參謀本部以 Human Desire / Mandate 為入口，以 Secretariat 作為程序制度，以 Canonical State + Transition Rules 作為治理核心，由 CORE-6 自主議事、允許合法說服與外部專家補充，再將可追溯狀態翻譯為人類可理解的 Executive Brief / Decision Request。**

---

# 1｜核心鏈

~~~text
HUMAN DESIRE
→ D0 RAW DESIRE
→ D1 QUALIFIED MANDATE
→ SECRETARIAT FREEZE
→ METHOD / SEAT INITIALIZATION
→ CORE-6 DELIBERATION
→ ISSUE / OBJECTION / AMENDMENT / CONSULTATION
→ CANONICAL EVENT HISTORY
→ STATE REDUCTION / ROUTING
→ MANDATE-SPECIFIC EXIT
→ EXECUTIVE BRIEF / DECISION REQUEST
→ HUMAN
~~~

---

# 2｜Secretariat

~~~text
SECRETARIAT = OPERATIONAL INSTITUTION
NOT SINGLE COGNITIVE AGENT
~~~

Components:
- Process Kernel
- Canonical Record Keeper
- Expert Coordination Surface
- Report / View Renderer

---

# 3｜治理核心

~~~text
CANONICAL STATE
+
TRANSITION RULES
=
GOVERNANCE CORE
~~~

~~~text
SUMMARY != HISTORY
CHAT VIEW != CANONICAL STATE
EXECUTIVE VIEW != SECOND QUALIFICATION
~~~

---

# 4｜CORE-6

~~~text
N1 = BASIC_QUESTION / EXECUTIVE_CLARITY / USER_ACTION / EXPLANATION_GAP
A  = NEW_PATH / ALTERNATIVE / OPTION_SPACE
B  = FRAME / ARCHITECTURE / COORDINATE_SHIFT / UNOWNED_RESPONSIBILITY
C  = QUALIFICATION / EVIDENCE / CAUSALITY / AUTHORITY / STANDING
D  = ENGINEERING / IMPLEMENTATION / DEPENDENCY / TEST / RECOVERY
E  = COST / RESOURCE / TIME / MAINTENANCE / OPPORTUNITY_COST
~~~

~~~text
ROLE != STANCE
STANCE CHANGE REQUIRES TRACEABLE BASIS
~~~

---

# 5｜Typed Event Admission

~~~text
RAW STATEMENT
→ ORIGIN-DECLARED OBJECTS
→ SCHEMA VALIDATION
→ CANONICAL TYPED EVENT
~~~

~~~text
ADAPTER MAY CHALLENGE
ADAPTER MAY NOT RECLASSIFY BY FORCE
~~~

---

# 6｜Routing

~~~text
PRIMARY ROUTE
=
EVENT TYPE RULE
+
OBJECT TARGET
+
MANDATORY OWNER MAP
~~~

Explicit target may add valid route but may not suppress mandatory route.

---

# 7｜Expert Consultation

~~~text
EXPERT ANSWER != COUNCIL STANCE
CONSULT_ELIGIBLE != RESOURCE_AVAILABLE
~~~

Expert supplies material, not sovereignty.

---

# 8｜Human-facing layer

## Executive Brief

~~~text
[TRUST STRIP]
重大反對：YES/NO + count
關鍵未知：YES/NO + count
現在需要你決定：YES/NO

1. 這件事是什麼？
2. 現在到哪裡？
3. 有哪些路？
4. 最大風險與反對
5. 還不知道什麼？
6. 現在要你做什麼？
~~~

## Decision Request

~~~text
HUMAN_ACTION_REQUIRED
→ DECISION_REQUEST_REQUIRED
~~~

~~~text
WAITING_HUMAN WITHOUT DECISION_REQUEST = UX FAILURE
~~~

---

# 9｜Ending

~~~text
CHECKPOINT_ENDING != SESSION_END
~~~

Checkpoint Ending means AI has reached a legal boundary and must hand the next decision to the human.

Future D1 should freeze an End Policy.

~~~text
SESSION ENDED != HUMAN APPROVED RESULT
~~~

---

# 10｜第一版保留缺口

- O-D-002 Reducer replay 尚未工程實測
- O-E-001 總 deliberation cost 未知
- O-E-002 Meaningful Wake 尚未被實跑證明

因此 V0.1 不得宣稱：
- deterministic runtime 已驗證
- 成本更低
- 比普通 Agent 更有效率
- Meaningful Wake 已節省 token
- production ready

---

# 11｜版本態度

> **第一版夠用，不要求一次完美。**

~~~text
NEW FAILURE
→ REENTRY
→ AUDIT
→ VERSIONED REVISION
~~~

V0.1 是後續實跑與修正的基線，不是終極答案。

**END**
