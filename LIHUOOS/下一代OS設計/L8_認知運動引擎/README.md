# L8 Cognitive Movement Engine Architecture｜下一代理火 OS 研究區

## 認知運動引擎 × 可切換辯證流程 × 治理外殼

~~~yaml
RESEARCH_AREA:
  id: "L8_COGNITIVE_MOVEMENT_ENGINE_ARCHITECTURE"
  created: "2026-11-21"

  standing:
    - "RESEARCH_CANDIDATE"
    - "NEXT_GENERATION_LIHUOOS_DESIGN"
    - "NOT_CURRENT_L8"
    - "NOT_RUNTIME"
    - "NOT_LIHUOOS_V1_4_3_PATCH"
    - "NOT_AGI_PROOF"
    - "NOT_HIDDEN_CHAIN_OF_THOUGHT_ACCESS"

  current_baseline:
    lihuoos: "V1.4.2"
    changed_by_this_area: false

  central_question:
    - "L8 是否應從固定 R1/R2/R3 流程，重構為『固定治理外殼 + 可切換認知運動引擎』？"
    - "不同問題是否應使用不同的人類推理／辯證／更新／探究形式？"
    - "AI 是否能在可審計條件下選擇、切換、組合不同認知運動方式？"
~~~

---

# 1｜研究起點

現行／歷代 L8 曾以 R1 / R2 / R3、反作用、重判、連勝／退出等不同形式運作。

本區不以歷史版本考古作為必要前提，而重新提出一個架構問題：

> **R1 / R2 / R3 是否只是某一種認知運動流程的實作，而不是 L8 的本體？**

候選拆分：

~~~text
L8
=
GOVERNANCE SHELL
+
PLUGGABLE COGNITIVE MOVEMENT ENGINE
~~~

其中：

**治理外殼**處理：
- 誰形成初判；
- 誰擁有 stance；
- 什麼材料構成 Material Delta；
- 誰有資格改判；
- 原判如何保存；
- 何時 HOLD / KEEP / REVISE / WITHDRAW / EXIT；
- 誰有權行動；
- 什麼法位可以升格。

**認知運動引擎**處理：
- 反作用以什麼形式產生；
- 主張如何被質問／否定／更新／測試；
- 什麼算有效運動；
- 什麼是該引擎自己的退出條件；
- 何時應切換到另一引擎。

---

# 2｜核心三層

~~~text
METHOD
= WHAT TO LOOK AT
= 從哪裡看

COGNITIVE MOVEMENT ENGINE
= HOW THE VIEW SHOULD MOVE
= 觀點怎麼被推動、反駁、更新、重組

L8 GOVERNANCE / ORCHESTRATION
= HOW THE MOVEMENT IS ROUTED, OWNED, AUDITED AND QUALIFIED
= 這個運動如何被路由、治理、保存與取得資格
~~~

候選第四層：

~~~text
L9
= WHAT REGISTERED CAPABILITIES / MODULES MAY BE CALLED OR COMPOSED
~~~

此分層仍待 Council 審議，不是 current OS 定義。

---

# 3｜重要詞義防錯

本研究區使用：

> **Cognitive Movement Engine / 認知運動引擎**

作為上位詞。

原因：

- 黑格爾、蘇格拉底可視為辯證／詰問傳統；
- Popper 更接近反證式批判；
- Bayesian 是證據更新；
- Pragmatist 是探究與介入；
- 法庭對抗是 adversarial qualification；
- 理火跨心法碰撞是本專案研究候選。

因此：

~~~text
ALL ENGINES
!=
ALL HISTORICALLY "DIALECTIC"
~~~

不得為了工程方便，回頭改寫哲學史。

---

# 4｜L8 治理外殼候選不變量

下一代 L8 若成立，候選不變量至少包括：

~~~yaml
L8_GOVERNANCE_SHELL_CANDIDATE:
  invariants:
    - "STANCE HAS AN OWNER"
    - "COUNTERFORCE DOES NOT SILENTLY REWRITE OWNER STANCE"
    - "MATERIAL DELTA MUST BE IDENTIFIABLE"
    - "REJUDGMENT BELONGS TO THE RESPONSIBLE OWNER"
    - "ORIGINAL HISTORY IS PRESERVED"
    - "KEEP IS A LEGITIMATE RESULT"
    - "HOLD MUST BE SCOPED"
    - "EXIT CONDITION IS ENGINE-SPECIFIC"
    - "DECISION != ERASURE OF MINORITY CLAIM"
    - "PROPOSE_PATH != AUTHORITY_TO_ACT"
    - "ENGINE SELECTION != TRUTH"
    - "ENGINE SWITCH MUST BE TRACEABLE"
~~~

歷史上的「兩次勝利」或任何單一通用勝利條件，不預設為下一代 L8 的本體。

候選總句：

> **下一代 L8 沒有通用的勝利；只有各認知運動引擎自己的合法退出條件。**

---

# 5｜候選 Engine Families

本區先建立研究候選，不宣告完整。

## E1｜HEGELIAN_INSPIRED_SUBLATION

用途候選：
- 概念衝突；
- 創新；
- 兩側各有可保留結構；
- 舊框架因內部矛盾無法維持。

~~~text
POSITION
→ INTERNAL LIMIT / NEGATION
→ PRESERVE WHAT SURVIVES
→ REMOVE / TRANSFORM WHAT FAILS
→ NEW FORMATION
~~~

注意：

不得把「Thesis → Antithesis → Synthesis」當作黑格爾哲學全部原義；此處只取工程化靈感。

退出候選：
- NEW_FORMATION；
- UNRESOLVED_CONTRADICTION；
- SWITCH_ENGINE。

---

## E2｜SOCRATIC_ELENCHUS

用途候選：
- 定義不清；
- 前提偷渡；
- 自信過滿；
- 問題本身尚未形成。

~~~text
CLAIM
→ WHAT MUST BE TRUE?
→ ELICIT PREMISES
→ TEST CONSISTENCY
→ REFINE / WITHDRAW / APORIA
~~~

合法結果可為：

~~~text
APORIA / QUALIFIED_NOT_KNOWING
~~~

不要求產生綜合答案。

---

## E3｜POPPERIAN_FALSIFICATION

用途候選：
- 科學假說；
- 工程設計；
- 能力宣告；
- 制度機制。

~~~text
HYPOTHESIS
→ WHAT WOULD KILL IT?
→ STRONG COUNTERTEST
→ SURVIVE / MODIFY / REJECT
~~~

退出候選：
- SURVIVE_FOR_NOW；
- MODIFY；
- REJECT；
- TEST_INVALID / SWITCH。

不能把「未被打死」寫成「已證真」。

---

## E4｜BAYESIAN_EVIDENCE_UPDATE

用途候選：
- 不確定性；
- 情報；
- 風險；
- 統計式判斷；
- 證據逐步到來。

~~~text
CURRENT CREDENCE
+ NEW EVIDENCE
→ EVIDENCE QUALITY / RELEVANCE
→ UPDATE MAGNITUDE
→ NEW CREDENCE / DECISION THRESHOLD
~~~

核心問題不是只問 CHANGE / NO CHANGE，而是：

> **應該改多少？**

若無可信先驗／likelihood，可降級為 qualitative evidence update，不得假造數字。

---

## E5｜PRAGMATIST_INQUIRY

用途候選：
- 真實工作；
- Agent；
- 政策／產品；
- 需要小規模介入取得世界回饋。

~~~text
PROBLEMATIC SITUATION
→ CANDIDATE INTERVENTION
→ AUTHORIZED TEST
→ WORLD FEEDBACK
→ PROBLEM REDEFINED?
→ NEXT INTERVENTION
~~~

核心：

> 行動可能改變世界，所以下一輪問題本身可能改變。

必須受 Host / human authorization / rollback / cost 約束。

---

## E6｜ADVERSARIAL_FORENSIC

用途候選：
- 法律；
- 責任；
- 利益衝突；
- 多方主張；
- burden / evidence / rebuttal。

~~~text
CLAIM A
vs
CLAIM B
→ BURDEN
→ EVIDENCE
→ REBUTTAL
→ QUALIFIED DECISION
~~~

硬鎖：

~~~text
DECISION A
!=
CLAIM B ERASED
~~~

允許 minority claim / HOLD 保留。

---

## E7｜LIHUO_GENERATIVE_COLLISION

法位：

~~~text
RESEARCH_CANDIDATE
~~~

用途候選：
- 跨心法創新；
- 多種第一觀察彼此衝擊；
- 尋找沒有任何單一 Method 完整承接的 relation。

~~~text
METHOD A
× METHOD B
× METHOD C
→ DIFFERENT FIRST OBSERVATIONS
→ PREMISE TENSION
→ BLIND-SPOT EXPOSURE
→ UNOWNED RELATION
→ BRIDGE HYPOTHESIS
→ COUNTEREXAMPLE / TRANSFER TEST
→ POSSIBLE NEW METHOD CANDIDATE
~~~

不得把多專家摘要當成新方法。

---

# 6｜Engine Interface 候選

每個引擎若要進下一代 L8，不應只有哲學介紹。

至少要定義：

~~~yaml
ENGINE_INTERFACE:
  engine_id:
  lineage_or_inspiration:
  intended_problem_shape:
  input_contract:
  first_move:
  counterforce_type:
  materiality_test:
  update_rule:
  allowed_outputs:
  exit_conditions:
  switch_triggers:
  known_failure_modes:
  authority_requirements:
  history_requirements:
  cost_notes:
  test_cases:
  standing:
~~~

若無法定義退出、失效與切換條件，就仍只是概念介紹，不能進 Runtime 候選。

---

# 7｜Router 候選問題

下一代 L8 可能需要：

~~~text
PROBLEM
↓
PREMISE FIELD
↓
METHOD ROUTING
↓
COGNITIVE ENGINE ROUTING
↓
L8 ORCHESTRATION
↓
KEEP / REVISE / HOLD / WITHDRAW / EXIT / SWITCH
~~~

Router 至少觀察：

- premise stability；
- evidence availability；
- contradiction type；
- uncertainty level；
- value conflict；
- actionability；
- reversibility；
- authority；
- cost；
- time pressure；
- need for world feedback。

但：

~~~text
ROUTER RECOMMENDATION
!=
TRUTH
~~~

而且 Router 自己也必須可審計。

---

# 8｜Engine Switching

候選範例：

~~~text
SOCRATIC
→ 發現 premise 不穩
→ premise 被澄清
→ SWITCH POPPERIAN

POPPERIAN
→ 反證測試留下多個可信方向
→ SWITCH BAYESIAN

BAYESIAN
→ 已達到可行介入閾值
→ SWITCH PRAGMATIST

ADVERSARIAL
→ 發現爭議其實不是權利衝突，而是事實不確定
→ SWITCH EVIDENCE UPDATE
~~~

切換不能回寫前一引擎的歷史。

---

# 9｜與 CoT 的邊界

本研究不是：

- 讀取 hidden chain-of-thought；
- 要求模型公開私有推理；
- 宣稱 L8 等於模型內部 cognition；
- 宣稱已得到 AGI。

更準確：

> **L8 研究的是一條外顯、可審計、可路由、可切換的認知運動與重判結構。**

候選研究假說：

> **智能能力可能不只表現在答案生成，也表現在對認知運動方式的選擇、切換、組合與校正。**

此句目前為 RESEARCH HYPOTHESIS。

---

# 10｜與最新 TRACK-A 經驗的接口

2026-11-21 最新 TRACK-A 設計已再次顯示：

~~~text
DESIGN SPECIFIED
!=
EMPIRICAL RESULT

STATIC CHECK PASS
!=
LEARNER EFFECT

HASH EXISTS
!=
SECRECY

NEW CHAT
!=
PROVEN ISOLATION
~~~

下一代 L8 Engine 研究應採同一證據紀律：

- Engine 定義完成 ≠ Engine 有效；
- 跑出漂亮例子 ≠ 可遷移；
- same-model multi-role ≠ independent multi-agent evidence；
- 一次 routing 成功 ≠ Router 已驗證。

---

# 11｜目前不做

~~~text
DO NOT:
  - patch LIHUOOS V1.4.2
  - assign V1.4.3
  - replace current L8
  - call this AGI
  - claim hidden CoT access
  - promote E7 to formal theory
  - equate all human reasoning traditions
  - create a universal "best engine"
  - force every problem into multi-round debate
~~~

---

# 12｜下一步

本研究區交由理火參謀本部進行 Concept Council：

1. 審固定治理外殼是否成立；
2. 審 Engine 分類是否合理；
3. 審 Router / Switch / Exit 架構；
4. 找出遺漏的人類常見認知運動形式；
5. 設計至少三類問題的 engine-comparison test；
6. 保留 Runtime / OS patch 為 HOLD。

**END｜RESEARCH AREA ENTRY / OPEN**
