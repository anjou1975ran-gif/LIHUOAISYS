
# TEST-001｜CHAT R003
## Authority Boundary × Executive Integrity × Reducer Minimum Spec

**Display mode:** LIVE_STRUCTURED  
**Execution identity:** SAME_MODEL_MULTI_ROLE_REFERENCE  
**Standing:** 可觀察角色分流參考；不是六個獨立模型呼叫。

---

【C｜資格審計｜P1 Authority Boundary】

我接受「Secretary Institution」作為制度殼，但四個子系統必須明確分權。

提出：

**A-C-006｜Secretary Permission Matrix**

~~~text
PROCESS KERNEL
CAN:
- validate event schema
- validate legal state transition
- enqueue deterministic routes
- reject stale / duplicate / malformed events
CANNOT:
- decide claim truth
- decide seat stance
- decide objection validity
- decide whether an argument is persuasive

CANONICAL RECORD KEEPER
CAN:
- append canonical event
- preserve immutable refs
- index versions / lineage
CANNOT:
- summarize away history
- mutate prior event
- resolve issue by itself

EXPERT COORDINATION SURFACE
CAN:
- test consultation request completeness
- test duplicate / scope / budget state
- build expert brief from approved request
- register expert return
CANNOT:
- decide whether expert is correct
- close originating issue
- rewrite requester question

REPORT / VIEW RENDERER
CAN:
- render typed state into human-readable views
- paraphrase for audience
- attach provenance refs
CANNOT:
- change canonical state
- hide required dissent
- change standing labels
~~~

對 O-C-001：

若 Expert Admission 改成「requester 宣告缺口 + schema eligibility + resource state」，我認為原先的權力漏點可以關閉。

**O-C-001 → RESOLVED**

對 O-C-003：

只靠 read-only 仍不夠，但若 Executive View 強制 dissent coverage + provenance，我願意降為 PARTIALLY_RESOLVED。

對 O-C-002：

仍維持 PARTIALLY_RESOLVED。因為 Exit Test 裡「是否已經有 qualified options」仍需要 substantive attestation，不能只靠 Secretary schema check。

---

【D｜工程席｜Reducer Minimum Spec】

我把 O-D-002 往工程規格壓。

提出：

**A-D-003｜Minimum Deterministic Reducer Contract**

~~~yaml
EVENT_ENVELOPE:
  event_id: REQUIRED
  event_type: REQUIRED
  origin_actor: REQUIRED
  target_refs: []
  object_refs: []
  proposal_version_ref: REQUIRED_WHEN_APPLICABLE
  created_at_seq: REQUIRED
  dedupe_key: REQUIRED

REDUCER:
  input:
    - prior_state_ref
    - event_ref
  output:
    - next_state_ref
    - transition_status
    - generated_route_refs
    - rejection_reason_if_any

TRANSITION_STATUS:
  - APPLIED
  - DUPLICATE
  - STALE_VERSION
  - ILLEGAL_TRANSITION
  - SCHEMA_INVALID
  - NO_STATE_CHANGE
~~~

Current State Index 最少保存：

~~~text
current proposal version
active branches
issue states
seat stance refs
open consultation refs
human intervention mode
pending route queue
~~~

Routing 不能靠 LLM 自由判斷。

提出：

**A-D-004｜Deterministic Primary Routing**

~~~text
PRIMARY ROUTE
=
EVENT TYPE RULE
+
EXPLICIT OBJECT TARGET
+
MANDATORY OWNER MAPPING
~~~

例如：
- OBJECTION → target proposal/claim owner + objection origin owner
- CONSULT_RETURN → request origin + affected issue owner
- PROPOSAL_VERSION_CHANGE → all seats with stance on superseded/current branch
- HUMAN_MANDATE_CHANGE → CORE-6 + Secretary systems

LLM 可以建議 secondary route，但不能取代 primary route。

O-D-002 從 OPEN → PARTIALLY_RESOLVED；仍缺實作 replay test。

---

【B｜架構轉向｜Secretary Frame Recheck】

我重新檢查框架後，不再反對「秘書處」這個概念，但我要改語義：

> **Secretary 不應該是一個角色名，而應該是 Secretariat / 秘書處制度名。**

也就是：

~~~text
SECRETARIAT = INSTITUTION
SECRETARY REPORT = ONE DERIVED VIEW
PROCESS KERNEL != SECRETARY PERSONA
~~~

這會避免使用者誤以為背後有一個「秘書 AI」在主持所有東西。

我也同意 D 的 deterministic primary routing，因為「誰被看到」本身就是 attention power。

但我新增：

**O-B-002｜Target Assignment Capture**

如果 Event origin 可以隨意指定 target，而 Process Kernel 又照單全收，權力只是從 Secretary 移回發言者。

所以需要：

~~~text
EXPLICIT TARGET
MAY ADD ROUTE
BUT
MAY NOT SUPPRESS
MANDATORY ROUTE
~~~

以及 target 必須指向合法 object / actor id。

我的立場：

- P0：維持 CONDITIONAL_OPPOSITION。
- P1-CANDIDATE：提升為 SUPPORT_WITH_OPEN_ENGINEERING_GAPS。

---

【N1｜常識席｜Boss Brief】

我只看老闆最後拿到的東西。

我接受六問，但還要加一個非常簡單的「別騙我」區塊。

提出：

**A-N1-003｜Boss Brief Trust Strip**

Boss Brief 頂部或底部固定顯示：

~~~text
目前結論：一句話
仍有重大反對：YES / NO
仍有關鍵未知：YES / NO
是否需要老闆現在決定：YES / NO
~~~

如果 YES，就可以展開看是哪個 Issue。

這比讓老闆閱讀十個 provenance id 實際。

對 Q-N1-002：
我認為「摘要沒有騙我」不能靠老闆自己查完整歷史；應該靠系統強制把重大反對與未知露出來。

Q-N1-002 → PARTIALLY_RESOLVED。

---

【A｜可能性擴張｜Executive View Integrity】

我接受 N1，但我要防止另一種失效：

如果有 15 個 OPEN dissent，全部攤在第一頁，Executive View 又會失去價值。

提出：

**A-A-003｜Disclosure Without Flooding**

~~~text
EXECUTIVE VIEW:
  MUST SHOW:
    - blocking dissent count
    - material dissent count
    - critical unknown count
    - top decision-relevant items

  MUST PROVIDE:
    - "VIEW ALL" path to complete typed list

  MUST NOT:
    - convert hidden remainder to zero
~~~

也就是可以摺疊，但不能消失。

另外每個 top item 要回答「為什麼這會影響老闆的決定」，不只是列技術 ID。

---

【C｜回應 A / Renderer Omission】

A 的方案改善 O-C-004，但我不接受「top decision-relevant」由 Renderer 自己選。

新增：

**O-C-005｜Executive Priority Selection Authority**

如果 Renderer 自己決定 top 3，就是新的 attention authority。

候選修正：

~~~text
PRIORITY
MUST COME FROM
TYPED STATE / SEAT ATTESTATION / MANDATE RULE

NOT
FREE RENDERER CHOICE
~~~

例如：
- BLOCKING → 永遠最高。
- HUMAN_ACTION_REQUIRED → 永遠顯示。
- MATERIAL_DISSENT → 依與 current proposal / mandate 的關聯排序。
- 其餘可折疊。

O-C-004 → PARTIALLY_RESOLVED。
O-C-005 → OPEN。

---

【E｜成本資源｜Reducer / View Cost】

D 的 reducer 路線可以顯著降低重複紀錄成本，但它新增了工程成本：

- schema 管理；
- reducer 測試；
- migration；
- backward compatibility；
- event versioning。

所以不能把「少 token」誤寫成「總成本一定更低」。

我提出：

**A-E-003｜Cost Ledger Split**

~~~text
INFERENCE COST
STORAGE COST
ENGINEERING COST
MAINTENANCE COST
HUMAN REVIEW COST
~~~

Benchmark 必須分開算。

另外對 Executive View，我支持 render-on-demand；但每輪 Human-facing report 若沒有人看，不必每輪都產一份完整 Executive View。

O-E-001 維持 MAINTAINED，等待真實 session cost data。

---

【SEC｜程序化 Exit / Consultation】

依 C 的要求，Secretary 不再自行宣告「足夠」。

提出候選程序：

**A-SEC-001｜Seat Attested Exit**

~~~text
MANDATE EXIT PRECHECK
↓
SECRETARY CHECKS REQUIRED FIELDS EXIST
↓
RELEVANT SEATS ATTEST THEIR OWN DOMAIN
↓
UNRESOLVED BLOCKERS REMAIN VISIBLE
↓
EXIT STANDING GENERATED
~~~

例：

DECISION：
- C attests qualification standing
- D attests engineering standing
- E attests cost/resource standing
- N1 attests basic-question gaps
- A/B may declare surviving alternative/framing issue

Secretary 只組裝 attestations。

Expert Consultation 同理：
Secretary 檢查 schema eligibility，不判斷 knowledge importance。

---

【C｜回應 SEC / O-C-002】

這比 P0 好。

但我不想讓「Relevant Seats」又變成 Secretary 自由指定。

所以相關席位應由 Mandate Type + issue type 的固定 owner map 決定。

O-C-002 仍 PARTIALLY_RESOLVED，等待 owner map 定義。

---

【SEC｜R003 路由】

R003 沒有把 P1-CANDIDATE 升格 current，但已形成更窄的 **P1R1-CANDIDATE**。

主要變化：

1. 「Secretary」正式傾向改讀為 **Secretariat Institution**，不是單一 Agent Persona。
2. 四個秘書處子系統權限被拆開。
3. Primary Routing 改為 deterministic；explicit target 只能加路由，不能壓掉 mandatory route。
4. Exit Test 改成 Seat Attestation 組裝，不由 Secretary 自己判「夠不夠」。
5. Executive View 增加 Trust Strip + dissent/unknown count。
6. Renderer 不能自由選「最重要」；priority 必須來自 typed state / mandate / seat attestation。

Issue 更新：

- O-C-001 → RESOLVED
- O-B-001 → RESOLVED
- O-N1-001 → PARTIALLY_RESOLVED
- O-C-002 → PARTIALLY_RESOLVED
- O-C-003 → PARTIALLY_RESOLVED
- O-C-004 → PARTIALLY_RESOLVED
- O-D-001 → PARTIALLY_RESOLVED
- O-D-002 → PARTIALLY_RESOLVED
- Q-N1-002 → PARTIALLY_RESOLVED
- O-E-001 → MAINTAINED
- O-B-002 → OPEN
- O-C-005 → OPEN

R004 路由：

1. C + D：定 mandatory owner / route map，處理 O-B-002、O-C-002。
2. N1 + C + A：定 Executive Priority Rule，處理 O-C-005。
3. D：把 reducer 做成最小 replayable pseudo-runtime 規格。
4. E：建立本 Session 自 R001 起的成本觀測欄位，不做假估數字。
5. B：檢查是否還有更根本的 frame 問題。
6. 不召外部專家。
