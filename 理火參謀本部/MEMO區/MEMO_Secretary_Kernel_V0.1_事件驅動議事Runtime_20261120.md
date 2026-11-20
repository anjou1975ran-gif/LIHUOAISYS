
# MEMO｜Secretary Kernel V0.1
## 事件驅動議事 Runtime｜理火參謀本部

**版本：** V0.1-WORKING  
**日期：** 2026-11-20  
**狀態：** FIRST KERNEL CANDIDATE / NOT HOST DEPLOYED / FIRST TEST TARGET

---

# 0｜核心定位

> **秘書處不是決定下一步該想什麼；秘書處負責確保每一個值得被回答的新東西，都找到應該回答它的人，而且任何人的回答都不會把舊歷史洗掉。**

~~~text
SECRETARY OWNS PROCESS
SECRETARY DOES NOT OWN TRUTH
SECRETARY DOES NOT OWN STANCE
SECRETARY DOES NOT OWN FINAL DECISION
~~~

秘書處不是第七個參謀席，也不是「最聰明的主持 AI」。

---

# 1｜Round 的重新定義

~~~text
ROUND != AGENDA
ROUND = CHECKPOINT / SNAPSHOT
~~~

Round 只是一次可封存的議事狀態切片。

會議方向由尚未閉合的 Issue、Proposal Branch、Evidence、Amendment、Consultation Return 與 Material Delta 自然推動。

不採：

~~~text
R1 A講
R2 B講
R3 C講
~~~

避免把議事做成劇本。

---

# 2｜Secretary Kernel State Machine

~~~text
S0 HUMAN_DESIRE_INTAKE
↓
S1 MANDATE_FREEZE
↓
S2 COUNCIL_BOOTSTRAP
↓
S3 INDEPENDENT_FIRST_PASS
↓
S4 OPEN_DELIBERATION
   ↕
   EVENT_ROUTING
   ↕
   TARGETED_REDELIBERATION
↓
S5 CLOSURE_SWEEP
↓
S6 MANDATE_EXIT_TEST
↓
S7 RESULT_OR_HOLD
~~~

任何新 Material Event 都可以把流程從 S5/S6 拉回 S4。

---

# 3｜四本核心帳

## 3.1 Mandate Ledger
保存：
- D0 Raw Desire
- D1 Qualified Mandate
- Mandate Version
- Human Intervention Mode
- Human Intervention Events

## 3.2 Proposal / Version Ledger
保存：
- Proposal ID
- Proposal Version
- Amendment
- Branch
- Supersedes / Derived-from
- Current pointer

## 3.3 Issue Ledger
保存：
- Question
- Objection
- Evidence Gap
- Engineering Gap
- Cost Gap
- Explanation Gap
- Consultation Request
- Blocking / Non-blocking standing

## 3.4 Position Ledger
保存：
- Seat
- Proposal Version
- Stance
- Output Version
- Material Delta
- Position Revision
- Prior Position

---

# 4｜事件類型

第一版最小事件：

~~~text
CLAIM
QUESTION
OBJECTION
AMENDMENT
NEW_PATH
PROPOSAL_BRANCH
EVIDENCE_REQUEST
CONSULT_REQUEST
CONSULT_RETURN
ENGINEERING_FINDING
COST_FINDING
METHOD_FINDING
MATERIAL_DELTA_CANDIDATE
STANCE_REVISION
ISSUE_STATE_CHANGE
HUMAN_INTERVENTION
MANDATE_CHANGE
~~~

每個 Event 必須有唯一 ID。

---

# 5｜Wake / Routing

~~~text
ACTIVE MEMBER != MUST SPEAK EVERY ROUND
~~~

Secretary 可以偵測：
- 新 Event 對誰有 target；
- 哪個 Issue 尚未取得 response；
- 哪個 Proposal Version 改變；
- 哪個 Expert Return 需要重新送回原席。

但：

~~~text
SECRETARY DETECTS CHANGE EVENT
!=
SECRETARY DECIDES SEMANTIC EFFECT
~~~

Material Delta 對某席是否足以改變判斷，由該席自己判。

合法回應：

~~~text
MATERIAL_AND_STANCE_CHANGING
MATERIAL_NOT_STANCE_CHANGING
NON_MATERIAL
NEEDS_MORE_EVIDENCE
~~~

---

# 6｜Issue Ownership

提出 Issue 的席位成為 origin owner。

例如：

~~~yaml
ISSUE:
  issue_id: O-17
  origin_owner: C
  target: PROPOSAL_P3
  type: EVIDENCE_GAP
  statement: "市場規模目前缺乏足夠證據"
~~~

新材料進場後：

~~~text
SECRETARY
→ WAKE ORIGIN OWNER
~~~

原 owner 可回：

~~~text
RESOLVED
PARTIALLY_RESOLVED
MAINTAINED
REFORMULATED
~~~

硬鎖：

~~~text
OBJECTION OWNER != VETO OWNER
~~~

其他席可以不同意 origin owner 對 Issue 的判斷，但不得刪除其存在史。

---

# 7｜Issue Status

~~~text
OPEN
IN_RESPONSE
RESOLVED
PARTIALLY_RESOLVED
MAINTAINED
DORMANT_EXTERNAL_DEPENDENCY
OUT_OF_SCOPE
SUPERSEDED
~~~

硬鎖：

~~~text
DORMANT != RESOLVED
SUPERSEDED != NEVER_EXISTED
~~~

---

# 8｜Expert Consultation

任何席可提出 Consult Request。

只有 Secretary 負責：
- 檢查現有來源是否足夠；
- 建 Expert Brief；
- 召入 Guest Expert；
- 固定 scope；
- 保存來源；
- 控制 exit condition；
- 把 Expert Return 送回需要重新判斷的席。

但：

~~~text
EXPERT RETURN != ISSUE CLOSED
EXPERT RETURN != COUNCIL STANCE
EXPERT RETURN != TRUTH
~~~

專家提供材料，不提供主權。

---

# 9｜Proposal Versioning

~~~text
P0
→ AMENDMENT A-03
→ P1
~~~

舊 Stance 永遠仍指向原 Proposal Version。

例如：

~~~text
C @ P0 = OPPOSE
C @ P1 = CONDITIONAL_SUPPORT
~~~

禁止：

~~~text
P1 EXISTS
→
RETROACTIVELY REWRITE C @ P0
~~~

---

# 10｜Closure Sweep

當 Runnable Event Queue 暫時清空時，進入 Closure Sweep。

Secretariat 向 CORE-6 各自發出最後掃描：

- N1：還有未回答的基本問題嗎？
- A：還有 materially different PATH 嗎？
- B：還有需要翻桌的 framing 問題嗎？
- C：還有 material qualification objection 嗎？
- D：還有 material engineering blocker 嗎？
- E：還有 material cost/resource blocker 嗎？

合法回覆：

~~~text
NO_NEW_MATERIAL_ISSUE
~~~

或新增 Issue。

只要有新 Material Issue：

~~~text
RETURN TO S4
~~~

---

# 11｜Mandate Exit Test

Secretary 只檢查「本 Mandate 所需結構是否齊全」，不裁判哪個答案最好。

## CONCEPT
至少：
- 概念結構
- 主要定義
- materially different branches
- 重大缺口
- open questions

## RECOMMENDATION
至少：
- qualified options
- tradeoffs
- recommendation basis
- failure conditions
- unresolved material risks

## DECISION
至少：
- decision-ready options
- material objections
- evidence standing
- engineering standing
- cost standing
- conditions
- recommendation OR HOLD_DECISION

---

# 12｜Human Position

H0 預設：

~~~text
CONTINUE
PAUSE
STOP
~~~

~~~text
CONTINUE
=
ALLOW PROCESS TO CONTINUE

NOT
APPROVE CURRENT DIRECTION
~~~

Human Intervention 必須寫入 Mandate Ledger，不得回鑄前輪。

---

# 13｜Kernel Invariants

~~~text
ROUND != AGENDA
SUMMARY != HISTORY
OTHER SEAT ASSERTION != FACT
EXPERT RETURN != ISSUE CLOSED
OBJECTION OWNER != VETO OWNER
NEW PROPOSAL VERSION != OLD HISTORY REWRITE
STANCE REVISION REQUIRES TRACEABLE BASIS
SECRETARY ROUTING != SECRETARY REASONING
NO RUNNABLE EVENT != NO UNRESOLVED ISSUE
~~~

---

# 14｜第一個壓力測試

本 Secretary Kernel V0.1 本身就是第一個被送入理火參謀本部的 Proposal。

測試目的不是證明它正確，而是看：
- N1 是否找到基本操作問題；
- A 是否長出更好的會議形態；
- B 是否能翻掉「Round」假設；
- C 是否找到秘書處暗藏權力；
- D 是否找到不可實作或狀態爆炸；
- E 是否找到 token / latency / maintenance 成本；
- 是否需要召入外掛專家；
- 秘書處能否在審自己的制度時不偷改異議。

**END**
