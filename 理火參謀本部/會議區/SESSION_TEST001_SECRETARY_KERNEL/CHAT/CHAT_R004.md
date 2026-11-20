
# TEST-001｜CHAT R004
## Routing Map × Executive Priority × Replay Spec × Cost Observation × Ending Condition

**Display mode:** LIVE_STRUCTURED  
**Execution identity:** SAME_MODEL_MULTI_ROLE_REFERENCE  
**Standing:** 可觀察角色分流參考；不是六個獨立模型呼叫。

---

【C｜資格審計｜Mandatory Owner / Route Map】

我先處理 O-B-002 與 O-C-002。

Primary Routing 不能由發言者自由指定，也不能由 Secretariat 自由判斷。

提出：

**A-C-007｜Mandatory Route Owner Map V0.1**

~~~text
OBJECTION
→ target object owner
→ objection origin owner
→ seats whose typed responsibility matches objection type

EVIDENCE_REQUEST
→ request origin
→ evidence/qualification owner when typed
→ Expert Coordination Surface only if consultation eligibility is claimed

CONSULT_RETURN
→ request origin
→ linked issue owner
→ seats previously waiting on consultation ref

PROPOSAL_VERSION_CHANGE
→ every seat with a stance on prior/current affected version
→ every OPEN issue owner targeting changed material

STANCE_REVISION
→ Position Ledger
→ issue owners whose open issue is cited as change basis

HUMAN_MANDATE_CHANGE
→ CORE-6
→ all open issue owners
→ Process Kernel / Renderer

ENDING_CANDIDATE
→ relevant seat attestations
→ Process Kernel
→ Report Renderer
~~~

Explicit target 可以增加合法 recipient，但不能 suppress mandatory route。

對 O-B-002：
若 mandatory route 由 typed event map 產生，我認為它可以降為 PARTIALLY_RESOLVED；仍需 replay test。

對 O-C-002：
Exit relevant seats 不由 Secretary 選，而由 Mandate Type + typed responsibility map 固定。

例如：

~~~text
CONCEPT:
  N1 + A + B + C
  D/E only when engineering/cost became material

RECOMMENDATION:
  N1 + A + B + C + D + E

DECISION:
  N1 + A + B + C + D + E
~~~

這只是 V0.1 owner map，之後可被實跑打掉。

---

【D｜工程席｜Replayable Reducer】

我把 reducer 再壓成可 replay 的 pseudo-runtime。

提出：

**A-D-005｜Reducer Replay Contract V0.1**

~~~text
GENESIS_STATE
+
ordered canonical events
↓
REDUCER
↓
STATE_N
~~~

測試要求：

~~~text
REPLAY(GENESIS, EV[1..N])
==
RECORDED_STATE_N
~~~

若不等：
~~~text
STATE_DIVERGENCE
~~~

Reducer 本身不讀自然語言去猜狀態，只吃 typed event payload。

自然語言發言要先由 Seat Output Adapter 產生 typed object，並保留原文 ref：

~~~text
SEAT STATEMENT
→ TYPED EVENT CANDIDATE
→ VALIDATION
→ CANONICAL EVENT
~~~

新的工程風險：

**O-D-003｜Natural-Language-to-Typed-Event Authority**

誰把一句自然語言分類成 OBJECTION / AMENDMENT / CLAIM，本身可能影響 routing。

因此 Adapter 不能靜默分類；至少要：
- 保留原文；
- 暴露 classification；
- 允許 origin seat 修正 classification；
- classification change 形成新 event，不回寫舊 event。

O-D-002 → PARTIALLY_RESOLVED，等待真正 replay test。

---

【E｜成本資源｜Observation Fields】

目前不能估「便宜多少」，但可以先把真實 session 開始量。

提出：

**A-E-004｜Session Cost Observation V0.1**

每輪至少觀察：

~~~yaml
ROUND_COST_OBSERVATION:
  active_seat_count: REQUIRED
  seat_output_refs_count: REQUIRED
  canonical_event_count: REQUIRED
  derived_view_count: REQUIRED
  expert_call_count: REQUIRED
  wake_count: REQUIRED
  duplicate_event_rejections: REQUIRED
  stale_event_rejections: REQUIRED
  human_intervention_count: REQUIRED

  token_or_compute_metrics:
    input_tokens: IF_AVAILABLE
    output_tokens: IF_AVAILABLE
    external_call_cost: IF_AVAILABLE
    latency: IF_AVAILABLE

  unavailable_metrics:
    - MUST_BE_MARKED_UNKNOWN
~~~

不能從文字長度冒充 token telemetry。

另外追一個：

~~~text
COUNCIL OVERKILL SIGNAL
=
Mandate solved with no material gain
while process cost materially exceeds N0 baseline
~~~

O-E-001 維持 MAINTAINED；現在只是建立測量入口。

---

【N1｜常識席｜Executive Priority】

老闆第一頁的 priority 不能靠 Renderer 猜，我同意 C。

我會用最笨的固定順序：

**A-N1-004｜Boss Priority Ladder**

~~~text
P0 HUMAN_ACTION_REQUIRED
P1 BLOCKING
P2 MATERIAL_DISSENT
P3 CRITICAL_UNKNOWN
P4 SURVIVING_OPTIONS / MATERIAL_TRADEOFF
P5 INFORMATIONAL
~~~

同一級如果很多，不要裝作知道哪個一定最重要。

先按：
1. 是否直接影響 current Mandate；
2. 是否直接影響 current proposal；
3. 是否由多個席位獨立標記 material；
4. event sequence / stable ID。

這只是排序，不是「真理排名」。

---

【C｜回應 N1 / O-C-005】

這個比 Renderer 自由挑 top 3 合法。

我加兩條：

~~~text
BLOCKING / HUMAN_ACTION_REQUIRED
MUST NOT BE FOLDED BELOW DEFAULT VIEW

MATERIAL_DISSENT_COUNT
MUST INCLUDE HIDDEN/FOLDED ITEMS
~~~

如果排序依「多席位獨立標記 material」，要保留 minority objection，不得因只有一席反對就掉出 P2。

所以：

~~~text
MINORITY
!=
NON_MATERIAL
~~~

O-C-005 → PARTIALLY_RESOLVED。

---

【A｜可能性擴張｜Executive View】

我接受 Priority Ladder，但補一個 View：

老闆不一定只想看「目前答案」，有時要看「這輪跟上一輪有什麼變」。

提出：

**A-A-004｜Executive Delta View**

~~~text
SINCE LAST CHECKPOINT:
- what changed
- what was resolved
- what became worse / newly uncertain
- what now requires human action
~~~

它仍然是 derived view，不新增 canonical truth。

---

【B｜架構轉向｜Frame Recheck】

目前我不再翻掉 Secretariat Institution。

反而我看到新的邊界：

> 真正的核心不是「秘書處」；真正的核心可能是 **Canonical State + Governance Transitions**。

Secretariat 是操作這個制度的 organizational shell。

所以我不建議現在改名，但留下研究句：

~~~text
SECRETARIAT IS THE OPERATIONAL INSTITUTION
CANONICAL STATE / TRANSITION RULES ARE THE GOVERNANCE CORE
~~~

這能防止未來把所有能力又塞回「秘書處」這個詞。

我沒有新 blocking objection。

---

【SEC｜HI-002 / ENDING Condition】

先拆語義：

~~~text
CLOSURE SWEEP
!=
MANDATE EXIT
!=
HOLD
!=
PAUSE
!=
SESSION END
~~~

候選狀態：

~~~text
OPEN
PAUSED
WAITING_EXTERNAL
WAITING_HUMAN
EXIT_CANDIDATE
ENDED
~~~

我不建議「沒有 runnable event」直接 END。

因為可能只是：
- 等專家；
- 等人類資料；
- 外部依賴 dormant；
- resource hold。

提出：

**A-SEC-002｜Session Ending Candidate V0.1**

合法 ENDING 原因候選：

~~~text
MANDATE_COMPLETED
HUMAN_STOP
MANDATE_WITHDRAWN
SUPERSEDED_BY_NEW_SESSION
~~~

其中 MANDATE_COMPLETED 需要：

~~~text
MANDATE EXIT STANDING EXISTS
+
NO PENDING MANDATORY ROUTE
+
FINAL REPORT RENDERABLE FROM CANONICAL STATE
+
OPEN BLOCKERS DISCLOSED ACCORDING TO EXIT STANDING
→
EXIT_CANDIDATE
~~~

是否從 EXIT_CANDIDATE 自動進 ENDED，還沒決定。

新問題：

**Q-SEC-001｜Auto-End Authority**
H0 FREE 下，Mandate 完成後應自動 END，還是仍需人類最後一個 END/ACCEPT？

---

【N1｜回應 Q-SEC-001】

如果老闆前面說「你們自己開完會給我報告」，最後還要求他按一次接受才能 END，很煩。

我傾向：

~~~text
H0_FREE + MANDATE_COMPLETED
→ AUTO_END_ALLOWED
~~~

但報告要明確寫：

> 會議結束，不代表老闆接受建議。

也就是：

~~~text
SESSION ENDED
!=
HUMAN APPROVED RESULT
~~~

---

【C｜回應 ENDING】

我同意 N1 的方向，但必須由 Human Intervention Profile 預先決定。

新增：

**A-C-008｜End Policy**

~~~text
END_POLICY:
  AUTO_ON_MANDATE_EXIT
  REQUIRE_HUMAN_END
~~~

預設候選：
- H0_FREE → AUTO_ON_MANDATE_EXIT
- H1/H2 → AUTO_ON_MANDATE_EXIT unless human overrides
- H3_DIRECTED → REQUIRE_HUMAN_END

但這只是候選，不能從 H0 的「自由」直接推導人類一定同意 auto-end。

Q-SEC-001 → PARTIALLY_RESOLVED。

---

【D｜回應 ENDING】

工程上 END 必須是 event，不是 derived inference。

~~~text
SESSION_END_EVENT:
  end_reason
  exit_standing_ref
  final_state_ref
  unresolved_disclosure_refs
  human_action_ref: OPTIONAL
~~~

一旦 ENDED：
- 不再接受普通議事 event；
- 只能 REOPEN 形成新 session 或 explicit re-entry event；
- 不回寫舊 session。

提出：

**A-D-006｜Terminal Session Event**

---

【SEC｜R004 路由】

R004 形成新的 **P1R2-CANDIDATE**，仍未升格 current。

主要變化：

1. Primary Route owner map 有第一版。
2. Reducer 加入 replay determinism 與自然語言分類風險。
3. Executive View 有 typed priority ladder，不由 Renderer 自由挑重點。
4. 成本開始建立觀測欄位，而不是猜 token。
5. ENDING 被正式拆離 Closure / Exit / Hold / Pause。
6. Session END 傾向由 explicit terminal event 表示。
7. Auto-End 是否預設啟用仍未完全封閉。

Issue 更新：

- O-B-002 → PARTIALLY_RESOLVED
- O-C-002 → PARTIALLY_RESOLVED
- O-C-005 → PARTIALLY_RESOLVED
- O-D-002 → PARTIALLY_RESOLVED
- O-E-001 → MAINTAINED
- O-D-003 → OPEN
- Q-SEC-001 → PARTIALLY_RESOLVED

R005 路由：

1. C + D：處理 O-D-003，自然語言到 typed event 的資格與更正流程。
2. C + D + B：檢查 owner/route map 是否仍有 authority leak。
3. N1 + A + C：壓縮 Boss Brief / Executive Delta 成最小可用版。
4. E：用 TEST-001 現有可觀測資料建立第一份 Cost Observation；不可假造不可得 telemetry。
5. SEC + C + N1：收斂 End Policy，判斷是否可以進 Closure Sweep 前置。
6. 若仍無外部知識缺口，不召專家。
