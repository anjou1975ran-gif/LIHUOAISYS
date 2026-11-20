
# TEST-001｜CHAT R002
## Targeted Re-deliberation

**Display mode:** LIVE_STRUCTURED  
**Execution identity:** SAME_MODEL_MULTI_ROLE_REFERENCE  
**Standing:** 可觀察角色分流參考；不是六個獨立模型呼叫。

---

【B｜架構轉向｜回應 O-B-001】

我維持 R001 的翻桌：Secretary 應該是一個制度名稱，不是一個單體智能角色。

我把 PB-B-001 收斂成四個責任面：

~~~text
SECRETARY INSTITUTION
├─ PROCESS KERNEL
│  └─ deterministic transition / routing
├─ CANONICAL RECORD KEEPER
│  └─ append-only event history
├─ EXPERT COORDINATION SURFACE
│  └─ consultation workflow only
└─ REPORT / VIEW RENDERER
   └─ read-only rendering
~~~

但第三項「Expert Coordination」不能自己判斷專家說得對不對，只能執行已滿足條件的 consultation workflow。

**A-B-002｜Secretary Institution Split**

如果這個拆分成立，我對「秘書處是運作核心」的反對下降；我反對的是 Secretary-as-single-cognitive-agent。

**立場：** P0 = CONDITIONAL_OPPOSITION；P1-CANDIDATE = CONDITIONAL_SUPPORT。

---

【C｜資格審計｜回應 B / C-001 / C-002 / C-003】

B 的拆分有用，但「分成四塊」本身不夠，必須把每塊可以做的判斷寫死。

### 1. Expert Admission

秘書處不應判斷「這個知識重要不重要」。

改成程序觸發：

~~~text
OPEN KNOWLEDGE / EVIDENCE GAP EXISTS
+
REQUESTER STATES EXISTING QUALIFIED MATERIAL IS INSUFFICIENT
+
QUESTION / DOMAIN / SCOPE ARE SPECIFIED
→
CONSULTATION ELIGIBLE
~~~

Secretary 可以拒絕的理由只應是：
- DUPLICATE；
- SCHEMA_INCOMPLETE；
- CLEARLY_OUT_OF_MANDATE；
- RESOURCE_LIMIT_REQUIRES_HUMAN_REVIEW。

拒絕必須留下 reason，並可被原 requester 挑戰。

**A-C-004｜Procedural Expert Admission**

### 2. Closure

Secretary 不得自行判斷「大家沒有重要問題了」。

Closure Sweep 只是一個詢問程序。

~~~text
SECRETARY ASKS
SEAT DECLARES MATERIALITY
SECRETARY RECORDS
~~~

### 3. Executive Translation

Read-only 還是不夠。Renderer 即使不能改 history，仍可以「不提」某個 material dissent。

所以新增：

**O-C-004｜Renderer Omission Risk**

以及硬鎖候選：

~~~text
EVERY EXECUTIVE CLAIM
→ PROVENANCE REF

EVERY OPEN MATERIAL DISSENT
→ MANDATORY EXECUTIVE DISCLOSURE
~~~

**立場：** P0 = CONDITIONAL_OPPOSITION；P1-CANDIDATE = CONDITIONAL_SUPPORT，O-C-004 OPEN。

---

【D｜工程｜回應 B / D-001】

我支持把「秘書處」當 institutional shell，而不是一個 LLM。

工程上更乾淨的版本：

~~~text
CANONICAL:
  IMMUTABLE EVENT LEDGER

OPERATIONAL:
  DETERMINISTIC STATE REDUCER
  CURRENT STATE INDEX
  ROUTING QUEUE

DERIVED:
  ROUND VIEW
  CHAT VIEW
  EXECUTIVE VIEW
  AUDIT VIEW
  FINAL REPORT
~~~

這裡要再降一級：

> Round Record 不應該保存一份完整真相，它只是由 Event Ledger + State Index 生成的 checkpoint view。

因此 R001 現行紀錄格式雖可用於測試，但正式工程版應減少內容複製。

新增：

**A-D-002｜Canonical Event + Reducer Architecture**

但也新增一個工程缺口：

**O-D-002｜Reducer Specification Gap**

如果沒有 deterministic reducer 規格，所謂「current state」最後仍可能靠 LLM 摘要推算，等於把我們剛拆掉的權力又放回來。

最低要求：
- event type schema；
- legal transition table；
- dedupe key；
- stale-version rejection；
- processed_by；
- result_ref；
- replay determinism test。

**立場：** P0 = CONDITIONAL_SUPPORT；P1-CANDIDATE = CONDITIONAL_SUPPORT，O-D-002 OPEN。

---

【N1｜常識席｜回應 Executive View】

我接受 A 的 Multi-View，但老闆不需要知道「View Rendering」這些字。

我只要一頁回答六件事：

~~~text
1. 這件事是什麼？
2. 現在最重要的結論是什麼？
3. 還有哪些可選路？
4. 最大風險 / 最大反對是什麼？
5. 還有什麼不知道？
6. 現在要我做什麼？
~~~

如果是 CONCEPT，最後一題可以是「目前不需要你決定」。

我再加一個最笨但重要的問題：

**Q-N1-002：**
如果老闆只看這一頁，怎麼知道摘要沒有騙他？

我的答案候選是：
- 每一個關鍵句旁邊可以展開來源；
- 必須有「反對意見」欄；
- 必須有「我們不知道什麼」欄。

**A-N1-002｜Boss Brief 6 Questions**

**立場：** CONDITIONAL_SUPPORT。

---

【A｜可能性擴張｜回應 N1 / C】

我接受 N1 的六問，並把 Multi-View 改成「同源多顯影」而不是多份報告。

~~~text
ONE CANONICAL HISTORY
→ MANY READABLE VIEWS
~~~

Executive View 不應只是壓短版 Audit View，而應按 Mandate 類型改寫入口：

- CONCEPT：看「概念長成什麼、還有哪些分支」。
- RECOMMENDATION：看「選項、推薦、代價、反對」。
- DECISION：看「現在能不能決、若不能缺什麼」。

新增：

**A-A-002｜Mandate-Aware Executive View**

這個 View 可以很短，但不能自己決定哪些 dissent 不重要。

**立場：** CONDITIONAL_SUPPORT。

---

【E｜成本資源｜回應 D / E-001】

D 的架構明顯比「四層都存完整內容」便宜。

我支持：

~~~text
STORE ONCE
REFERENCE MANY
RENDER ON DEMAND
~~~

我要求增加四個成本控制：

1. Seat context 不每輪灌入全歷史，只給 relevant refs + required source。
2. 同一 Event 對同一 target/version 只 Wake 一次，除非有新 Material Delta。
3. Executive / Audit / Final View 按需要 render，不做無意義重生成。
4. Expert Consultation 要有 session-level budget / human escalation 機制，避免每個不確定性都外掛專家。

新增：

**A-E-002｜Deliberation Cost Controls**

O-E-001 暫不關閉，因為目前仍沒有 benchmark。

**立場：** P1-CANDIDATE = CONDITIONAL_SUPPORT。

---

【C｜回應 E / Expert Budget】

我同意有 resource limit，但秘書處不能用「太貴」偷偷否決知識缺口。

因此若符合 Consultation Eligibility，但預算不足：

~~~text
CONSULT_ELIGIBLE
+
BUDGET_LIMIT
→
HOLD_RESOURCE
or
HUMAN_REVIEW_REQUIRED
~~~

不能寫成：

~~~text
NO_EXPERT_NEEDED
~~~

這兩件事必須分開。

新增：

**A-C-005｜Expert Eligibility / Resource Separation**

---

【SEC｜R002 路由】

R002 形成一個明顯的候選新架構，但尚未升格 current Proposal。

建立：

**PB-R002-01｜P1-CANDIDATE — Secretary Institution + Canonical Event Architecture**

其內容由：
- A-B-002
- A-C-004
- A-D-002
- A-N1-002
- A-A-002
- A-E-002
- A-C-005

共同構成。

Issue 狀態更新：

- O-N1-001 → PARTIALLY_RESOLVED
- O-B-001 → PARTIALLY_RESOLVED
- O-C-001 → PARTIALLY_RESOLVED
- O-C-002 → PARTIALLY_RESOLVED
- O-C-003 → PARTIALLY_RESOLVED
- O-D-001 → PARTIALLY_RESOLVED
- O-E-001 → MAINTAINED

新增：
- O-C-004 → OPEN（Renderer Omission Risk）
- O-D-002 → OPEN（Reducer Specification Gap）
- Q-N1-002 → OPEN（老闆如何知道摘要沒有騙他）

R003 路由：

1. **C + D + SEC**：把 P1-CANDIDATE 的 authority boundary 寫成可執行 transition / permissions。
2. **N1 + C + A**：做 Boss Brief 最小規格與 dissent coverage rule。
3. **D + E**：定 reducer / queue 最小工程結構與成本控制。
4. **B**：再次檢查「Secretary Institution」是否仍是錯框架。
5. **目前仍不召外部專家。**

---

# R002｜Executive Delta

- 「秘書處」開始從單一 AI 角色改成制度殼層。
- 底層傾向只保存一次 canonical Event History，再用 reducer 產生 current state。
- Round / Chat / 老闆摘要 / Audit 都改為 derived view。
- 老闆版暫定六問，且必須保留反對與未知。
- 專家「有沒有必要」與「有沒有預算叫」被拆成兩件事。
- 最大新缺口：Renderer omission 與 deterministic reducer 還沒解。
