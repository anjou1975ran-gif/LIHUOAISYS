# MEMO｜議前觀察起點探索｜PRE-SESSION STARTING LENS EXPLORATION
**版本：** V0.1-WORKING / 2026-11-20
**法位：** PROPOSED_SESSION_PREPARATION_EXPERIMENT / NOT_RUNTIME_PATCH / NOT_RATIFIED / NOT_MANDATORY
**目標：** 下一場正式 Staff-HQ Session 先試行「小設定」，判斷能否提升議事準確性，而不是現階段加入主 Runtime。
**Execution identity：** SAME_MODEL_MULTI_ROLE_REFERENCE unless real tooling shows otherwise.

## 1｜為什麼值得補
既有 Staff-HQ V0.2.1 Full Working 已有：
- Formal Entry: HUMAN INPUT → D0 RAW DESIRE → D1 MANDATE CANDIDATE → SESSION MANIFEST。
- C2 FRAME_AND_PROPOSAL_LIFECYCLE: Problem Frame `OPEN / CONTESTED / QUALIFIED_FOR_CURRENT_MANDATE / SUPERSEDED`；`REFERENCE != PROPOSAL`。
- Open Problem Formation: `P0 = NONE` 合法，席位可產生 QUESTION、PROBLEM_REFRAME、NEW_PATH。
- Clock A: 每一 Material Seat 首次觀察之前選 `METHOD_PACK / NO_METHOD_WITH_REASON / METHOD_UNAVAILABLE`，選中才鎖來源/版本/SHA並實際讀取。

**可能缺口：** D0/D1 釐清「討論什麼、權限為何」，但沒有明示一個 *optional* 議前討論：**這個問題由哪一種觀察入口開始較有生產力、它漏掉什麼、是否允許席位後續轉向？** 不能把人類給的方向誤讀成已被批准的商業結論。

**來源：**
- `理火參謀本部/工程區/STAFF_HQ_V0.2_RUNTIME_PACKAGE/STAFF_HQ_V0.2.1_RUNTIME_FULL_WORKING_20261120.md`，blob `0c47801d9880c1a9ab8bfe14cefaea25fd28eeae`，C2、Part II §§3–5.3。
- `理火參謀本部/MEMO區/PATCH_PROFESSIONAL_METHOD_DUAL_ROUTING_V0.1.1_WORKING_20261120.md`，blob `4df32103e71504e262572c58b377103e822482f6`：Method Delta 選擇發生在 First Observation 之前，且專業 Agent 不等於 Method。
- CASE003 R004 human proposed `money / power / information flow` as direction, not chosen product; `理火參謀本部/記錄區/SESSION_20261120_CLEAN_INTELLIGENCE_FEASIBILITY_003/EVENT/EV_R004_HUMAN_DIRECTION_MONEY_POWER_INFORMATION_FLOWS.md`。

## 2｜最小設計：只做一張 Starting Lens Card
這是**討論起點、不是先定立場**；可以人類提出，也可以秘書處初步列候選、CORE 責任席後續自行反對或改選。開放問題不強迫選唯一入口。

```yaml
STARTING_LENS_CARD_CANDIDATE:
  scope_question: "這次要研究什麼（受 D0/D1 限制）？"
  candidate_lenses: ["角度一", "不同角度二", "反向角度三（可選）"]
  provisional_entry: "暫由何種觀察單位切入；允許 NONE/OPEN"
  why_this_is_useful: "可能揭露哪種被忽略的關係或證據？"
  blind_spot_and_break_condition: "此切入會漏掉什麼？哪項新材料會改變切入？"
  possible_method_and_expert_needs: "只記候選學科目錄/可能專業缺口，NOT SELECTED / NOT ACTIVATED"
  standing: PROVISIONAL_NONBINDING
```

**可短到幾行。** 不必每次產出大份「議前計畫書」；簡單題目可 `NO_SPECIAL_STARTING_LENS_WITH_REASON`。

## 3｜不增加固定制度負擔的議事時序
```text
Human D0 → D1 Candidate / Mandate boundary
  → OPTIONAL PRE-SESSION STARTING-LENS EXPLORATION
     (可列 1–3 種互相競爭的起點、明示盲區與可撤回條件)
  → PROVISIONAL FRAME / 仍可 OPEN 或 CONTESTED
  → Each affected seat sees D0/D1 + qualified references + provisional lens as NONBINDING
  → Each seat independently decides Method Delta (Clock A)
  → If selected, Secretary locks selected Method Path/Version/SHA then fetches exact pack
  → First Observation → LIHUOOS L8 → Seat-owned objects
  → Council can reframe or reject preparatory lens with traceable material basis
```

嚴禁：
- Human suggestion → Mandatory answer；`STARTING_LENS != D1 CONSENT != P0 != STANCE`。
- Secretary picks a single required approach and scripts all six seats；`STARTING_LENS != SEAT_METHOD_DECISION`。
- Mentioning law/finance → compulsory law/economics Pack；method choice remains per-seat and `NO_METHOD_WITH_REASON` remains legal。
- Before Method selection, read every candidate Method Pack full text; preparation reads only a **minimal method index**. Full selected Pack only after own decision and before First Observation.
- Preemptively hiring an Expert because a field is mentioned; can list `EXPERT_GAP_CANDIDATE`, but real mid-Council support request belongs to materially affected Seat, and Secretariat checks **existing** authorization rather than grants it.
- Treat every proposed lens as a new governance gate, or make all six seats comment before there is a material question.
- Treat a starting lens as a guarantee of accuracy; **opening bias is a real failure mode**.

## 4｜Case illustration (not forced answer)
**Commercial brief:** 客戶需要何種情報服務？
- Angle 1 `MONEY_AND_DECISION_AUTHORITY_FLOW`：預算/採購/驗收/資料合法使用權/責任。
- Angle 2 `UNSOLVED_JOB_AND_ALTERNATIVE`：現有服務已做什麼、哪一件有損失的決策仍缺材料。
- Angle 3 `INFORMATION_SUPPLY_AND_RIGHTS`：哪些來源可合法、可持續、可核實，誰願意供給。
- **Provisional entry** could be Angle 1, with Angle 2 as direct falsifier; choosing it does NOT infer government is the winner. If concrete buyer data show no incremental payment, Angle 1 alone is not useful enough.

## 5｜下一場 Session 的最小真實迴歸測試（先議事、再談改版）
- **Before first L8**：記錄 D0/D1、起點候選、盲點、候選 Method/Expert *routing only*；完整 Method 必須等 Seat 決定後才調閱。
- **During initial pass**：記錄哪些 Seat 改從別的入口觀察，不能強迫六席沿同一起點走；有理由 `NO_METHOD` 或 `QUIET` 合法。
- **During Council**：若新材料推翻起點，允許 `RE-FRAME / SUPERSEDE` 並由受影響席位形成 own L8；不得回寫先前起點，製造事先知道的歷史。
- **After checkpoint**：對照沒有該環節的既有 CASE 與新 Session，審查起點有無真的提前發現可用證據、減少無效 Method 引用、改善反例/資格辨識；同時查是否增強 anchoring 與同模劇場收斂。
- **判準**：`IMPROVED` 需可觀察的變化與反例，不能只因流程整齊就判 PASS；`NO_GAIN / BIAS_INCREASED` 同樣有效。若單次無法辨識，回報 `INCONCLUSIVE`，不宣稱因果效益已證實。

## 6｜可能版本態度
```yaml
CURRENT_RUNTIME_V0_2_1: UNCHANGED
PROPOSED_CHANGE_SCOPE: OPTIONAL_PRE_SESSION_ORIENTATION_WITH_EXISTING_C2
FIRST_TEST_STANDING: WORKING_REFERENCE
NO_NEW_PERMANENT_SEAT: true
NO_NEW_HUMAN_MANDATE_APPROVAL_GATE: true
NO_PRELOADED_ALL_METHOD_PACKS: true
PROFESSIONAL_AGENT_PREFLIGHT: CANDIDATE_ONLY_NOT_CALL
RATIFICATION_OR_NEW_RUNTIME_VERSION: DEFER_UNTIL_ACTUAL_TEST_EVIDENCE
```
**Goal:** 小設定先取得觀察入口，仍保留被推翻的空間。若不能提高實質判斷，應丟棄此補丁，不得為了「看起來準備充分」加流程。
