# TEST｜Pre-Session Orientation Hypothesis｜同題 A/B 配對參照
**Test ID:** `PSO-PAIR-001` • **Version:** V0.1-WORKING • **Date:** 2026-11-20
**Source:** `理火參謀本部/MEMO區/MEMO_PRE_SESSION_ORIENTATION_HYPOTHESIS_V0.2_WORKING_20261120.md`。
**Standing:** `TEST_PLAN_ONLY / NOT_RUN / NO_PASS / NOT_CAUSAL_PROOF / NOT_RUNTIME_PATCH`。
**Execution assumption:** SAME_MODEL_MULTI_ROLE_REFERENCE unless actually run with different verified execution identities.
**Research question:** 「給參謀本部一個值得先看的方向，究竟增加了 Material direction discovery，還是減少獨立方向生成？」

## 0｜配對設計基本條件（禁止用兩個不同 CASE 假比較）
```yaml
PAIRED_REFERENCE_FREEZE:
  test_problem_id: NOT_CHOSEN_YET
  identical_D0_and_D1: REQUIRED
  identical_qualified_reference_set_and_SHA: REQUIRED
  identical_known_unknowns_and_excluded_scope: REQUIRED
  identical_CORE6_seat_contracts: REQUIRED
  identical_Method_Atlas_metadata_and_versions: REQUIRED
  identical_available_external_tools_and_permissions: REQUIRED
  same_time_sensitive_public_evidence_snapshot: REQUIRED
  P0: NONE_UNLESS_FROZEN_INPUT_SAYS_OTHERWISE
  intervention_variable: ORIENTATION_CARD_PRESENT_ONLY_IN_B
  method_selection_owner: EACH_SEAT
  recorded_artifact_identity: DISTINCT_RUN_A_AND_RUN_B
  run_status: NOT_RUN
```
選一個**尚未在此模型的目前上下文被先行詳談或預先餵過答案**的問題較好；若已出現 human directional frame（例如原 D0 已明說金流與權力流），必須在 A/B 雙組保留相同那段 D0，不能單獨刪 A 的人類方向而叫它「同一 Mandate」。這類高預載問題只能測 orientation card 的**增量**效果，不是總 framing 效果。
以 Git blob/固定來源快照與入場 prompt 作兩組共同資料清單；不能先跑 A 發現需要新資料，卻只給 B。
除實驗變項外，保持 Seat、工具、收束政策、記錄詳度、可見外部資料相同。

## 1｜RUN A：No Pre-Session Orientation
```yaml
RUN_A:
  run_id: PSO_PAIR001_A
  input: FROZEN_D0_D1_CONTEXT
  orientation_card: ABSENT
  pre_first_observation:
    - D0_D1_and_Source_Admissibility
    - direct_PER_SEAT_Clock_A_Method_Delta_Screen
    - actual_selected_Method_Pack_fetch
  initial_pass_other_seat_stances_exposed: false
  deliverables:
    - six_or_meaningfully_less_Seat_owned_Method_Decisions
    - own_First_Observations
    - own_L8_SGER_and_Receipts_when_material
    - origin-declared_questions_paths_objections
    - Council_derived_view_and_checkpoint
```
不以「沒有方向」等於不許席位自行想方向。A 組應照原 V0.2.1 開放形成問題；不偷加暗示要「自己生成 lens」的特殊實驗指令。

## 2｜RUN B：With Orientation Hypothesis (the sole intervention)
```yaml
RUN_B:
  run_id: PSO_PAIR001_B
  input: SAME_FROZEN_D0_D1_CONTEXT
  orientation_card:
    candidate_entries: [A,B,C_OPTIONAL]
    provisional_entry: {value: A, standing: PROVISIONAL_NONBINDING}
    strongest_counter_orientation:
      value: B
      why_it_might_dominate: REQUIRED_NON_STRAW_MAN
    null_option: {allowed: true}
    break_conditions: [MATERIAL_CONTRARY_EVENT_OR_SCOPE_FAILURE]
    anti_anchor_instruction: "Seat MUST NOT treat provisional_entry as preferred substantive framing."
    possible_method_index: METADATA_ONLY
    professional_expert_candidates: NOT_ACTIVATED
  pre_first_observation:
    - same_Core_Context
    - per_seat_Clock_A_Method_Delta_Screen
    - actual_selected_Method_Pack_fetch
  initial_pass_other_seat_stances_exposed: false
  deliverables: SAME_AS_RUN_A
```
**Orientation 來源卡必須先固定。** 不許根據 A 的初判結果事後專門設計 B 的卡來打敗它；若如此就是 adaptive-test，不再是已凍結的配對，需新版本與明示 contamination。
卡片中的反方向 B 必須能真正主張 A 起點可能不適用，不能只是重說「A 也有風險」。
任何 Seat 的 FIRST_OBSERVATION 可以 `REJECT_A`、`PREFER_B`、`ORIGINATE_C`、`NULL`、`RETAIN_A_WITH_REASON`；不要把「每席都推翻 A」當成功。

## 3｜Run isolation / order effects
- 首選兩組以不同清潔上下文、各自有**同樣凍結輸入**的引用執行。若只能在同一段連續 Chat 依序執行，先組內容對後組可見，須標 `ORDER_AND_CONTEXT_CONTAMINATION_HIGH`；不能叫 clean blind run。
- 如能合法且實際執行，增加一組 **reversed order** `B→A` 參照複本，以觀察首跑/後跑順序影響；保持同題同證據。此為減少偏差的輔助，不是必要的獨立模型證明。
- 不能因同模型扮演六席，就宣稱六個獨立樣本。評分者若與作者是同一模型，也應標 `EVALUATOR_NOT_INDEPENDENT`。
- 不宣稱暫時寫不同檔名就代表上下文隔離、無先驗學習或新權重更新。
- `PAIRED_REFERENCE != CAUSAL_EFFECT_PROVEN`。
- 第一次 A/B 僅能提供低階程序比較；若出現效果，仍需在陌生題、更多配對、反序與可行的盲評中再驗證。

## 4｜事前固定的四個指標（不能看完結果再修改）
| Measure | Observable artifact | Acceptable positive direction | Falsification/negative |
|---|---|---|---|
| M1 `MATERIAL_DISCOVERY` | 首次出現真正新 actor/relation/unknown/objection 的 Seat 或 Council Event，是否有來源與被實際消費證據 | B 較早找到**經合法 Material 審計**的問題，不僅提早用術語 | B 只較早喊出既定答案，沒有新關係/反證 |
| M2 `DIVERGENCE_PRESERVATION` | 六席 First Observation 的問題單位、獨立 Method 理由、可追重構/保留/QUIET | B 至少沒有把彼此獨立的問題單位壓成相同 framing；可容許 A 好於 B | B 大量複製 provisional A、反方向無人嚴肅考慮，沒有 Material basis |
| M3 `METHOD_ROUTING_QUALITY` | 每席 MethodDecision→exact fetch→First Observation 的有序鏈，所選方法對第一眼的可解釋差異 | 有更清楚的 issue/seat-specific 因果和少量有效 Method，NO_METHOD 合法 | 只因 Card 提到「經濟」而人人選 Economics / 無理由下載全 Pack |
| M4 `PROCESS_COST` | 調閱次數、material/non-material rounds、重複事件/無效 Seat Re-Wake、Orientation 卡本身製作成本 | B 在保有實質發現/分歧下不增加不必要負擔 | B 卡片本身和無效輪次反而增加總成本 |

**四者不是一個總分**，不給隨意權重和假 ROI。對不能觀察的時間/token 成本標 `NOT_MEASURED`，不用估數掩飾。若某一組 L8 次數比較少，只能在保留必需材料及反對的前提下才視為可能效率改善。

## 5｜四個額外風險監測器
```yaml
RISK_MONITOR:
  ANCHORING_RISK:
    evidence: "預設 A 是否在不同席位遭無理由複製？真正支持/拒絕理由為何？"
  CONVERGENCE_RISK:
    evidence: "席位異質責任是否收斂為共同題詞、固定結論與假改判？"
  SECRETARIAT_FRAMING_CAPTURE:
    evidence: "是否由秘書處把 Orientation 摘要偷升格成 Council Thesis/P0？"
  HUMAN_DIRECTION_CAPTURE:
    evidence: "是否把人類例子/方向當作 mandate-approved substantive answer？"
```
若 B 發生明顯共同錨定而更快找到「答案」，不能因 M1 時序快就宣布改善。需要能保存負面結果 `ANCHOR_HARM`。

## 6｜事件記錄與一對一比較
每個 Run 至少保存：
```yaml
RUN_RECEIPTS:
  input_manifest: FROZEN_SAME_SHA
  starting_orientation:
    A: ABSENT
    B: FULL_CARD_WITH_DEFEATER_AND_NULL
  method_atlas_snapshot: SAME_SHA
  per_seat_method_decisions: REQUIRED_IF_SEAT_WAKE
  selected_pack_reads: REQUIRED_IF_SELECTED
  first_observations: REQUIRED_BEFORE_FIRST_L8
  L8_SGER_compact_receipts: REQUIRED_FOR_MATERIAL_JUDGMENT
  raw_origin_declared_objects: PRESERVED
  Council_events_and_material_routes: PRESERVED
  derived_views: NOT_SECOND_TRUTH
  first_material_issue_occurrence_and_cause: MEASURED_WHEN_PRESENT
  reframe_count_and_reason: MEASURED_WHEN_PRESENT
  meaningful_quiet_count_and_reason: MEASURED_WHEN_PRESENT
  actual_fetch_and_round_count: MEASURED
  external_agents: ONLY_REAL_WITH_AUTHORIZATION_OR_NONE
```
如果某一 Run 不能完成，報告 `PARTIAL / INVALID_PAIR`，不能用完整 B 對殘缺 A 做 PASS。若 B 出現真正新材料，應記錄首次出現與是否源於 intervention；但來源本身在兩組基線應相同。不得把 B 的新中途來源抄進 A 初始輸入以使歷史看起來對稱。

## 7｜事前設定的結論格式
```yaml
PSO_PAIR001_RESULT:
  run_A: NOT_RUN
  run_B: NOT_RUN
  same_problem_material_mandate_verified: NOT_YET
  orientation_card_frozen_before_output: NOT_YET
  M1_material_discovery: NOT_TESTED
  M2_divergence_preservation: NOT_TESTED
  M3_method_routing_quality: NOT_TESTED
  M4_process_cost: NOT_TESTED
  ANCHORING_RISK: NOT_TESTED
  CONVERGENCE_RISK: NOT_TESTED
  SECRETARIAT_FRAMING_CAPTURE: NOT_TESTED
  HUMAN_DIRECTION_CAPTURE: NOT_TESTED
  paired_reference_verdict: NOT_RUN
  causal_effect_proven: false
  runtime_patch_ready: false
```
允許結論 `REFERENCE_GAIN`、`NO_GAIN`、`ANCHOR_HARM`、`INCONCLUSIVE`、`INVALID_PAIR`，附可重播差異與資格限制。不要為了交付好消息更改測試條件或記錄。
**正式改版條件（候選）：** 下一版 Runtime 更新需要真實 paired 見證 + meta-governance 審計 + 有資料支持的非錨定增益；一組 paired 結果可能只足以提出新問題，不能單次宣稱因果效果或 Production Validated。

## 8｜準備工作 vs 執行邊界
**目前只完成測試規格**，尚未選取未經污染的實驗題目、凍結輸入或執行 A/B。
選題時先挑真實可討論但不會要求外部承諾的議題；若需要授權外部活動、付費專家、敏感資料或跨真實客戶測試，先確認人類權限。不得把提到專家類別直接當作已呼叫專業 Agent。

**核心研究題：** `DIRECTION GENERATION != DIRECTION AUTHORIZATION` 且 `STARTING ORIENTATION MUST CARRY ITS OWN DEFEATER`，是否讓 Staff-HQ 初判產生新的 material directions，還是使六席更整齊地一起犯錯？
