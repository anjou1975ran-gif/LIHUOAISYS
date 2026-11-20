# MEMO｜Pre-Session Orientation Hypothesis｜議前觀察方向假說
**版本：** V0.2-WORKING / 2026-11-20
**來源與沿革：** 修正 `MEMO_PRE_SESSION_STARTING_LENS_EXPLORATION_V0.1_WORKING_20261120.md`，原件保留、不回寫。
**原版 Git Blob：** `e75491d81e8108b8342dad6662500a873e248b24`。
**法位：** `PRE_SESSION_ORIENTATION_AUDIT / WORKING_HYPOTHESIS / NOT_RUNTIME_PATCH / NOT_RATIFIED / NOT_MANDATORY`。
**Execution:** `SAME_MODEL_MULTI_ROLE_REFERENCE` for current reference Council environment.

## 0｜審計裁定
```yaml
PRE_SESSION_ORIENTATION_AUDIT:
  genuine_gap: YES
  overlap_with_problem_frame: PARTIAL_BUT_NOT_REDUNDANT
  overlap_with_method_routing: MUST_BE_SEPARATED_BY_NAME_AND_OBJECT
  runtime_patch_ready: NO
  experiment_ready: YES_WITH_CORRECTIONS
  corrections:
    - "Starting Lens → Pre-Session Orientation Hypothesis"
    - "Every provisional entry carries strongest counter-orientation, null option, break conditions"
    - "Replace ACCURACY with EARLY_MATERIAL_DISCOVERY"
    - "Use SAME PROBLEM / SAME MATERIAL / SAME MANDATE paired reference"
  main_risk:
    - COMMON_ANCHOR_CAPTURE
    - SECRETARIAT_FRAMING_CAPTURE
    - HUMAN_DIRECTION_CAPTURE
  best_next_step: PAIRED_REFERENCE_TEST
```
這是對「議前起點可否改善 Staff-HQ 議事」的可反證提案，不是人類批准某個方向，也不是新的一道強制資格閘門。

## 1｜與現行 V0.2.1 的精確法位分層
```text
D0 / D1
= 我們受託研究什麼、授權與退出邊界

ORIENTATION HYPOTHESIS
= 哪一組關係值得先被顯影（暫定、可反對、可撤回）

METHOD ROUTING (Clock A)
= 每個 CORE Seat 依自己責任，選用什麼 Method／有理由不選

FIRST OBSERVATION → LIHUOOS L8 → COUNCIL
= 各 Seat 形成自己的觀察、判斷、反對、轉向與事件
```
`DIRECTION GENERATION != DIRECTION AUTHORIZATION`
`ORIENTATION != METHOD != KNOWLEDGE != STANCE`
`ORIENTATION != PROBLEM_FRAME_QUALIFIED`
`ORIENTATION != P0 != HUMAN_CONSENT`
`METHOD BEFORE FIRST OBSERVATION` 繼續是 V0.2.1 的硬鎖。

上位相容根據：Staff-HQ V0.2.1 `C2 FRAME_AND_PROPOSAL_LIFECYCLE` 與 Part II §§3–5.3；已保護 `P0=NONE`、`INITIAL_PASS → LIMIT OTHER-SEAT STANCE EXPOSURE`、`METHOD_DECISION < FIRST_OBSERVATION < L8`。
本提案不是取代 C2，而是在 D0/D1 與 Seat Method routing 之間，探索一個 **optional / preparatory / nonbinding direction-generation surface**。

## 2｜最小 Orientation Hypothesis Card（候選 Schema，不是現行 Runtime）
```yaml
PRE_SESSION_ORIENTATION_HYPOTHESIS_CANDIDATE:
  issue_or_mandate_ref: REQUIRED
  candidate_entries:
    - id: A
      relation_to_surface: "哪種 actor/relation/unknown 可能因此顯影？"
    - id: B
      relation_to_surface: "真實的替代起點，不是 A 的換句話說"
    - id: C
      relation_to_surface: "可選的第三種起點"
  provisional_entry:
    value: A | B | C | NONE
    standing: PROVISIONAL_NONBINDING
    basis: "暫定理由；不是哪席必須支持它"
  strongest_counter_orientation:
    value: B | A | C | NONE_WITH_REASON
    why_it_might_dominate: "在何種問題條件下，反方向可能比暫定方向更好？"
  null_option:
    allowed: true
    reason_when_used: OPTIONAL
  break_conditions:
    - "哪類新材料或反例會要求退回、移除或換起點？"
  anti_anchor_instruction: "Seat MUST NOT treat provisional_entry as preferred substantive framing."
  possible_method_index:
    status: METADATA_ONLY_NOT_SELECTED
    candidates: []
  possible_expert_gap:
    status: CANDIDATE_ONLY_NOT_ACTIVATED
    candidates: []
  origin_standing: HUMAN_DIRECTION | SECRETARIAT_WORKING_CANDIDATE | QUALIFIED_SEAT_ORIGIN
  authorization: NONE_CREATED_BY_ORIENTATION
  lifecycle: OPTIONAL / PROVISIONAL / SUPERSEDED | RETIRED | NO_ORIENTATION_WITH_REASON
```

**必要硬鎖：** `STARTING ORIENTATION MUST CARRY ITS OWN DEFEATER`。

如果實際上無法找到能挑戰 A 的 B，不是虛構一個 B 來通過格式；應保留 `COUNTER_ORIENTATION_UNRESOLVED`，標記資料缺口或改採 `NULL`。這個卡不要求每次都正好三個候選；零、一或兩個合法，但**宣稱暫定首選時必須真實說明其最強反對或承認未找到**。不得強迫六席模擬反對。

## 3｜Preflight 不得偷選 Method 或 Expert
議前只允許：
- 用心法目錄的 metadata 提示：哪些學科可能改變某種第一觀察單位、存在何種專業未知；
- 由 CORE Seat 在 Clock A 自行完成 `SELECT_METHOD | NO_METHOD_WITH_REASON | METHOD_UNAVAILABLE`；
- 選中後才鎖 Pack path、version、blob SHA，實際調閱，然後 First Observation；
- 專業領域預警 `EXPERT_GAP_CANDIDATE`，不是 `EXPERT_ACTIVATION`，更不是外部證據、專業判斷或公權准出；
- 後續 Clock B 只在真正新 Material Professional Gap 下由受影響席位發起支援決定，秘書處核對既有授權，不能自行授權。

不准因議前寫「財務」就把所有 Seat 固定配經濟學；不准因議前寫「法律」就虛構律師已加入。新的心法庫可提高 metadata 的候選品質，但不推翻此權限分層。

## 4｜Initial Pass 獨立性保護與不可消除的殘餘風險
```text
SAME D0/D1 + QUALIFIED CONTEXT
  ├── PREP ORIENTATION: candidates + counter + NULL + break
  └── SIX SEAT INITIAL ENTRIES:
       own Seat Contract + nonbinding Card where test condition permits
       → seat-owned Method Decision
       → actual selected Pack fetch
       → own First Observation
       → own L8 → origin-declared objects
```
- 同一張暫定卡餵給六席即使標 `NONBINDING`，**仍可能形成 COMMON ANCHOR**；不能聲稱 `ANTI_ANCHOR_INSTRUCTION` 已證明有效。
- 第一輪不投放其他席位 contemporaneous stances；秘書處不得預先摘要成「大家最該看的方向」。
- Seat 可以指出 Orientation 本身無用、改選 B、採 `NULL`、重構問題或合法 QUIET；必須留形成依據，而不是硬要它反對。
- 問題框架在議事中 `RE-FRAME / SUPERSEDE` 只以新事件追加；不可回寫舊起點假裝當初已有新材料。

## 5｜測量的是 DISCOVERY，不是 ground-truth accuracy
```yaml
STARTING_ORIENTATION_TEST:
  M1_material_discovery:
    question: "是否更早顯影真正 Material 的 actor / relation / unknown / objection？"
    evidence: "有原始事件、來源與可被其他席實質消費的記錄，含首次出現位置"
  M2_divergence_preservation:
    question: "各 Seat 是否仍能形成不同第一觀察、保留立場或推翻起始方向？"
    evidence: "六席 first-observation 單位/Method 分歧及有理由的 NO_METHOD、QUIET、重構；不是異議篇數競賽"
  M3_method_routing_quality:
    question: "Method 選擇是否更有問題依據，而非起始方向固定學科？"
    evidence: "每席的 before-first-look 理由、引用來源與真實 fetch／未選理由"
  M4_process_cost:
    question: "是否減少無效 rounds、無效 Method fetch，還是只增加程序？"
    evidence: "可核實的 round/fetch 計數、重複材料重喚醒、必要時實測時延與 token；不填虛構成本"
  monitors:
    - ANCHORING_RISK
    - CONVERGENCE_RISK
    - SECRETARIAT_FRAMING_CAPTURE
    - HUMAN_DIRECTION_CAPTURE
```
不能把「比較快給出整齊答案」當成 `M1 PASS`；也不能把不同 Seat 用不同字眼形容同一預設方向當成 `M2 PASS`。

## 6｜最小 paired reference 是首個可用實驗
```text
FREEZE: SAME PROBLEM + SAME MATERIAL + SAME MANDATE

RUN A: NO PRE-SESSION ORIENTATION
RUN B: WITH ORIENTATION HYPOTHESIS CARD
       (actual provisional + real counter-orientation + NULL + break)

COMPARE:
  First Observations / Method Decisions
  first Material Issues / cross-seat divergence
  material reframes / useful and wasted rounds
  exact Method fetches / anchoring / cost
```
**不能**拿不同問題的舊 CASE 與新 CASE 直接宣稱提升。若雙組無隔離、同模型記得前組結論，標示順序效應與污染風險；可用相反順序再做一對、盲化輸出評估減少偏差，**不可叫獨立多 Agent 或因果證明**。
`PAIRED REFERENCE != CAUSAL EFFECT PROVEN`。
正式 paired test 在 `理火參謀本部/訓練區/TEST_PRE_SESSION_ORIENTATION_PAIRED_REFERENCE_V0.1_WORKING_20261120.md` 設計，尚未執行。

## 7｜准出規則與版本態度
```yaml
CURRENT_STAFF_HQ_V0_2_1: UNCHANGED
V0_1_ORIGINAL: PRESERVED
V0_2_MEMO: WORKING_DESIGN_ONLY
INITIAL_TEST: NOT_RUN
RUNTIME_PATCH_READY: NO
MRC_001_REDUCER_IMPLEMENTED: NOT_CLAIMED
REQUIRED_NEXT_ACTION: PAIRED_REFERENCE_REGRESSION
POSSIBLE_OUTCOMES: [MATERIAL_GAIN, NO_GAIN, ANCHOR_HARM, INCONCLUSIVE]
AUTOMATIC_PROMOTION_TO_RUNTIME: FORBIDDEN
```
只有 evidence 支持、沒有實質錨定損害，且版本資格審查通過，才討論 Runtime 改版；`NO_GAIN / ANCHOR_HARM` 的可能結果同樣應保存。
**研究問題：** 「給參謀本部一個值得先看的方向，是在增加方向生成，還是在偷走方向生成？」
