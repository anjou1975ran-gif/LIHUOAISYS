# WORK｜理火參謀本部：下一代 L8 Cognitive Movement Engine Architecture Concept Council

**日期：** 2026-11-21  
**任務類型：** HUMAN AUTHORIZED / CONCEPT COUNCIL / NEXT-GENERATION OS RESEARCH  
**研究區：** `LIHUOOS/下一代OS設計/L8_認知運動引擎/`  
**Current OS：** LIHUOOS V1.4.2 unchanged  
**授權：** 研究、審議、提出候選架構與測試規格。**不授權 Runtime / OS / Protocol / Method Atlas 修改。**

---

# 0｜研究命題

人類提出：

> 歷代理火 L8 的 R1 / R2 / R3 與反作用、重判流程，本質上可能承接了人類辯證／推理方式；下一代 L8 不必固定單一辯證法，而可以採用多重認知運動引擎，依問題切換。

本次不要求證明 AGI。

本次不要求把模型 hidden chain-of-thought 暴露。

本次研究的是：

> **是否能建立「固定 L8 治理外殼 + 可切換 Cognitive Movement Engines + Router / Switch / Exit」的下一代架構。**

---

# 1｜必讀來源

1. `LIHUOOS/下一代OS設計/L8_認知運動引擎/README.md`
2. `LIHUOOS/下一代OS設計/L8_認知運動引擎/01_ENGINE_CANDIDATE_REGISTRY.md`
3. Current LIHUOOS V1.4.2 中 L8 current semantics。
4. Staff-HQ SEED / owner-preserving rejudgment materials。
5. RLT research area，特別是 claim lineage / material delta / supersedes vs responds-to。
6. 最新 TRACK-A Controlled Blind Evaluation Protocol V0.1，僅吸收其 evidence discipline；不得把 TRACK-A 靜態設計檢查當 L8 efficacy 證據。

若需要確認人類哲學／科學方法原義，可查外部可靠來源，但必須把：
- HISTORICAL SOURCE；
- ENGINEERING ADAPTATION；
- LIHUO NEW RESEARCH
三者分開。

---

# 2｜Council 必須先回答的第一刀

## Q1｜什麼是 L8 不可替換的本體？

請不要先討論哪個 Engine 最好。

先找出：

> 如果把 R1 / R2 / R3、黑格爾、蘇格拉底、Popper、Bayes 全部拿掉，L8 還剩下什麼？

候選：

~~~text
FORMATION
COUNTERFORCE
MATERIAL DELTA
OWNER-PRESERVING REJUDGMENT
HISTORY
QUALIFICATION
SCOPED HOLD
ENGINE-SPECIFIC EXIT
~~~

Council 可以刪、改、補。

---

# 3｜第二刀：Engine 分類是否成立？

逐一審：

- E1 Hegelian-Inspired Sublation
- E2 Socratic Elenchus
- E3 Popperian Falsification
- E4 Bayesian Evidence Update
- E5 Pragmatist Inquiry
- E6 Adversarial Forensic
- E7 LIHUO Generative Collision

對每一項回答：

1. 它真的代表不同的認知運動嗎？
2. 還是只是同一流程換名字？
3. 最適合的 problem shape 是什麼？
4. 它最危險的失效模式是什麼？
5. 它的合法 exit 是什麼？
6. 什麼情況應該切換到另一 Engine？
7. 有沒有不該放進「辯證法」但應保留在上位 Engine Registry 的類型？

---

# 4｜第三刀：找遺漏的人類常見推理方式

不要把初始七項當完整全集。

至少檢查：

- Abductive / Inference to Best Explanation；
- Causal / Counterfactual Intervention；
- Analogical / Case-Based Reasoning；
- Deliberative Value Tradeoff；
- Constraint Satisfaction / Optimization；
- Dialectical Materialism 或其他哲學辯證傳統是否有獨立工程價值；
- 是否有某些形式應該留在 Method 而不是 Engine。

**不要為了湊數硬新增 Engine。**

---

# 5｜第四刀：Method / Engine / L8 / L9 分層

Council 必須壓測：

~~~text
METHOD
= WHAT TO LOOK AT

ENGINE
= HOW THE VIEW MOVES

L8
= HOW THE MOVEMENT IS ROUTED / GOVERNED / RECORDED / QUALIFIED

L9
= WHAT REGISTERED CAPABILITY MAY BE CALLED / COMPOSED
~~~

問題：

- 這四層是否真能分開？
- 哪些邊界仍混淆？
- Engine 是 L8 內部 registry，還是 L9 capability？
- Router 屬於 L8，還是更上層？
- Method routing 與 Engine routing 誰先？
- 是否允許雙向重路由？

---

# 6｜Router 設計

建立 Router Candidate，但不要寫 Runtime。

Router 的輸入至少考慮：

- problem shape；
- premise stability；
- evidence availability；
- uncertainty；
- contradiction type；
- value conflict；
- actionability；
- reversibility；
- authority；
- cost；
- time pressure；
- need for world feedback。

輸出可以是：

~~~text
ONE ENGINE
ENGINE SEQUENCE
PARALLEL ENGINES
NO_ENGINE / DIRECT RESPONSE
HOLD_FOR_MORE_INFORMATION
~~~

硬鎖：

~~~text
ROUTER RECOMMENDATION
!=
ENGINE TRUTH
!=
ACTION AUTHORITY
~~~

---

# 7｜Switch Policy

至少測三條多引擎路徑：

### PATH A
~~~text
SOCRATIC
→ premise stabilized
→ POPPERIAN
→ countertest
→ BAYESIAN update
~~~

### PATH B
~~~text
ADVERSARIAL
→ dispute turns out to be factual uncertainty
→ BAYESIAN / EVIDENCE UPDATE
~~~

### PATH C
~~~text
MULTI-METHOD
→ LIHUO GENERATIVE COLLISION
→ bridge hypothesis
→ POPPERIAN
→ PRAGMATIST authorized pilot
~~~

每次 Switch 必須回答：

- why now；
- what previous Engine established；
- what remains unresolved；
- what state is handed over；
- what history cannot be rewritten。

---

# 8｜Engine Interface

Council 需提出至少 V0.1 schema：

~~~yaml
ENGINE:
  engine_id:
  problem_shape:
  required_inputs:
  first_move:
  counterforce:
  materiality_rule:
  update_rule:
  allowed_outputs:
  exit_conditions:
  switch_triggers:
  failure_modes:
  authority_requirements:
  history_requirements:
  cost_profile:
  evidence_standing:
~~~

不要求 Coding。

先證明 schema 有資格。

---

# 9｜CORE-6 任務

## N1｜Common Sense
- 人類實際會不會這樣切換思考？
- Router 是否比固定 R1/R2/R3 更可理解？
- 是否製造過度複雜的「思考儀表板」？

## A｜Possibility Expansion
- 哪些 engine 組合可能產生新方向？
- 哪些人類推理傳統被漏掉？
- 是否能形成 N+1 cognitive movement？

## B｜Architecture Turn
- 固定 shell + plugin engine 是否真比 current L8 好？
- Router 是否應成為 L8 本體？
- 能否完全不用 round 概念？

## C｜Qualification Audit
- 有沒有把哲學名字冒充工程證據？
- 有沒有把 engine success 冒充 truth？
- 有沒有把 externally visible reasoning structure 冒充 hidden CoT？
- 有沒有偷宣稱 AGI？

## D｜Engineering Audit
- interface 能否 type；
- switch 是否可追蹤；
- history 能否 replay；
- exit 是否可 deterministic / inspectable；
- 怎麼測 engine distinctness？

## E｜Cost & Resource Audit
- 多 engine 是否增加 token / latency / maintenance；
- router error cost；
- switch thrashing；
- engine registry maintenance；
- 何時 direct response 比 L8 更合理？

---

# 10｜會議建議輪次

## R1｜Independent First Formation
六席在不先統一答案下，分別回答 Q1：L8 不變本體是什麼？

## R2｜Engine Distinctness
打七個候選 Engine；刪除同義／錯分／假哲學。

## R3｜Architecture
形成 Shell / Registry / Router / Switch / Exit 候選。

## R4｜Case Pressure Test
至少三種題型：
1. 前提不穩；
2. 證據不確定；
3. 創新＋世界介入。
比較固定單引擎 vs 切換引擎。

## R5｜Anti-Theater / Cost / Qualification
專門找：
- engine-name theater；
- unnecessary multi-round；
- false switch；
- endless debate；
- premature synthesis；
- fake precision；
- cost explosion。

## R6｜Final Research Verdict
只允許：
- KEEP_AS_RESEARCH_CANDIDATE
- REVISE
- SPLIT
- REJECT
- READY_FOR_PROTOTYPE_SPEC

不得直接：
- PATCH_CURRENT_L8
- PROMOTE_TO_LIHUOOS
- CLAIM_AGI

---

# 11｜最低交付物

建議 Session：

`理火參謀本部/會議區/SESSION_20261121_L8_COGNITIVE_ENGINE_ARCHITECTURE_001/`

至少：

~~~text
00_SESSION_INDEX.md
01_SOURCE_LOCK.md
02_SHELL_INVARIANTS.md
03_ENGINE_DISTINCTNESS_REVIEW.md
04_ROUTER_SWITCH_ARCHITECTURE.md
05_ENGINE_INTERFACE_SCHEMA.md
06_CASE_PRESSURE_TESTS.md
07_CANONICAL_EVENT_LOG.jsonl
08_FINAL_COUNCIL_VERDICT.md
09_RECORD_AND_GIT_AUDIT.md
~~~

若有 Engine Registry 修訂，先寫入 Session proposal，不直接覆寫研究區 registry；人類核准後再回寫。

---

# 12｜最終必答

1. L8 本體是否可與 R1/R2/R3 分離？
2. 固定治理 Shell 是否成立？
3. 七個 Engine 中哪些真正 distinct？
4. 應新增／刪除哪些 Engine？
5. Router 應依什麼選引擎？
6. 何時應 Switch？
7. 是否存在「不啟動 L8」的合法直接路徑？
8. Engine-specific exit 能否取代通用勝利判定？
9. Method / Engine / L8 / L9 分層是否成立？
10. 下一步是 prototype spec、更多研究，還是停止？

---

# 13｜一句話

> **不要問哪個辯證法是理火的真理；請研究 AI 能不能知道這一題應該怎麼讓自己的判斷運動，並在錯的時候換一種方式繼續想。**

**START CONCEPT COUNCIL.**
