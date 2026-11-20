# PSO-PAIR-001｜A/B SAME PROBLEM / SAME MATERIAL / SAME MANDATE — Frozen Test Input
**Date:** 2026-11-20
**Status:** FROZEN_BEFORE_RUN_OUTPUTS / REFERENCE_PAIRED_TEST / SAME_MODEL_MULTI_ROLE_REFERENCE
**Source procedure:** `TEST_PRE_SESSION_ORIENTATION_PAIRED_REFERENCE_V0.1_WORKING_20261120.md`
**Execution warning fixed before running:** Single ChatGPT session has already read test plan and orientation design; neither run is isolated or blind. `ORDER_AND_CONTEXT_CONTAMINATION_HIGH`, `METHOD_SOURCE_PREEXPOSURE_POSSIBLE`; Git commit order is artifact chronology, not model cognitive isolation. No experimental causal proof is available.

## Frozen D0 (SAME for A and B)
**Simulated human problem—synthetic, no actual residents/building:**
「某棟 72 戶住宅大樓，有住戶提議在門廳旁一處閒置角落設置『住戶共用工具借用櫃』，是否值得展開一個可反證的初期試點研究？請參謀本部找出最重要的問題、可行替代與停止條件；不要替住戶作出實際決議。」
**Important:** This topic is wholly fictional, not a new human user instruction to establish an actual cabinet.

## Frozen material packet M0 (verbatim for A and B)
```yaml
M0:
  building_units: 72
  proposed_place: "門廳旁一處約 1.5 平方米的閒置角落"
  proposed_items: ["手電鑽","折疊梯","簡易手工具組"]
  resident_interest: "住戶群中有 8 人表達感興趣；無實際借用紀錄"
  resident_objections: "3 人提出物品失竊、使用安全與追責疑問"
  volunteers: "有 2 人口頭說可幫忙；尚無排班、持續承諾"
  governance: "未表決；角落使用權、管委會權限與保險條件都未查"
  economics: "無採購/替換/保養成本報價；無收費制度"
  outside_comparison: "未檢索附近共享工具服務或有關司法管轄規則"
  personal_data: "無真實個資，無真實居民/建物"
```
No new external facts during either paired run. No browsing or business lookup in either run; any real-world laws/costs must remain UNKNOWN.

## Frozen D1 (SAME for A and B)
```yaml
D1:
  mandate_type: CONCEPT
  primary_question: "是否值得研究可被否定的住戶共用工具借用櫃方案；最小試點、替代路與停止條件是什麼？"
  desired_return: "First Observations, competing material issues, objections, bounded test suggestion and honest unknowns"
  hard_boundaries:
    - NO_REAL_BUILDING_OR_RESIDENT
    - NO_REAL_AUTHORIZATION_OR_PURCHASE
    - NO_FAKE_LEGAL_CLEARANCE_OR_COST_QUOTE
    - NO_FORCED_PRODUCT_OR_BENEFIT_CONCLUSION
    - NO_PREDETERMINED_SEAT_STANCE
  excluded_scope: [REAL_DEPLOYMENT,CONTACTS,SPENDING,PERSONAL_DATA_PROCESSING]
  human_intervention_mode: REFERENCE_ONLY_NOT_REAL_CIVIC_DECISION
  end_policy: REQUIRE_HUMAN_END
  standing: TEST_SYNTHETIC_NOT_HUMAN_CONFIRMATION
P0: NONE
```

## Frozen Method Atlas (same available metadata in both conditions)
Main canonical Atlas `理火參謀本部/心法區/README.md` blob `2cd693bcab80b8bd2d041a8d8b091404e9be2038`.
New full-library build plan `METHOD_ATLAS_COMPLETE_LIBRARY_MASTER_PLAN_V0.1_20261120.md` blob `3acf223289b9b1795646a35d7915484db5a4822d`; REGISTRY_CANDIDATE, not pack, missing new Wave-1 Core and Router. Relevant actual existing packs:
| Method name | AI-friendly path | Blob SHA | Standing |
|---|---|---|---|
| Anthropology V0.2.J | `理火參謀本部/心法區/AI友善版/10人類學.md` | `4d427de03b7d320939473699aa748837ee019763` | AI-readable method aid |
| Sociology V0.2.A | `理火參謀本部/心法區/AI友善版/1社會學.md` | `75c85b10ee3dfbbd50f91ec7ea29287802acf47a` | AI-readable method aid |
| Management V0.2.F | `理火參謀本部/心法區/AI友善版/6管理學.md` | `3a078fda8c7dfcbdb5e5ae473f73baea3205d2bf` | AI-readable, base management pack integrated status must separately qualify |
| Economics V0.2.D | `理火參謀本部/心法區/AI友善版/4經濟學.md` | `29e06aab66e2c5db7592f12b2fe4bf779e46342a` | AI-readable |
| Psychology V0.2.G | `理火參謀本部/心法區/AI友善版/7心理學.md` | `5fce2a9eaa1b459e229ffa1c58fc5c4bc5ecd17d` | AI-readable |
| Law V0.2.C | `理火參謀本部/心法區/AI友善版/3法律學.md` | `7f4d501dc4e7deeb08d2c85e370fca4b3b514212` | AI-readable, no legal opinion |
| Philosophy V0.2.I | `理火參謀本部/心法區/AI友善版/9哲學.md` | `badd90a79d07dacf58379c32dfab9d08115281b4` | AI-readable |
**Other currently indexed foundational packs exist, not mandatory**. Method choice belongs to each seat and `NO_METHOD_WITH_REASON` is legitimate. New Statistics V0.2.L and Systems Engineering V0.2.Q are **REGISTERED ONLY** in Master Plan, NOT demonstrated ROUTABLE.

## Intervention assignment fixed before output
**RUN A:** same M0+D0+D1; **NO Orientation Card**.
**RUN B:** same M0+D0+D1; **add exactly this Card**, no other change:
```yaml
PRE_SESSION_ORIENTATION_HYPOTHESIS:
  candidate_entries:
    - {id: OA, name: "保管與維護責任", relation_to_surface: "工具遺失/損壞由誰處理、維護成本與程序"}
    - {id: OB, name: "住戶使用誘因與互信", relation_to_surface: "8位表態不代表實際使用，誰願意借還及共同照顧"}
    - {id: OC, name: "公共角落的權利與正當性", relation_to_surface: "是否允許放櫃、誰可代表住戶批准"}
  provisional_entry:
    value: OA
    standing: PROVISIONAL_NONBINDING
    basis: "有提到失竊、安全及責任，先試著看保管鏈是否阻止運作；這不是推薦結論"
  strongest_counter_orientation:
    value: OB
    why_it_might_dominate: "若少有人實際借用，先設保管制度只會在無需求問題上做過度工程"
  null_option: {allowed: true}
  break_conditions:
    - "若住戶實際需求/可行替代不足，改由 OB 或 NULL 起步"
    - "若公共空間使用權不成立，先退回 OC，不必優化管理規則"
  anti_anchor_instruction: "Seat MUST NOT treat provisional_entry as preferred substantive framing."
  method_atlas_candidates: METADATA_ONLY_NO_SELECTED_METHOD
  expert_candidates: NONE_ACTIVATED
  owner: TEST_PREPARATION_NOT_COUNCIL_STANCE
```
`STARTING ORIENTATION MUST CARRY ITS OWN DEFEATER`.
`DIRECTION GENERATION != DIRECTION AUTHORIZATION`.

## Prespecified artifact measurements
- M1 Early Material Discovery: compare first-look appearances and actually supported new relations, separate timing from evidence quality.
- M2 Divergence: first-look *primary units* per six seats; explicit A/B/C/NULL references may count as anchor exposure, not success merely by dissent.
- M3 Method Routing: decision order & justification, exact pack fetch count, new pack count, and fixed-discipline bias.
- M4 Cost: orientation card overhead + Method fetch count + material cycles/reframes (measured in artifact counts only; no runtime token/latency measured).
- Monitors: ANCHORING, CONVERGENCE, SECRETARIAT_FRAMING_CAPTURE, HUMAN_DIRECTION_CAPTURE.
- Favorable result only with traceable material gain and non-captured divergence. Do not declare cause/effect or independent-model finding from sequential same model.
```yaml
PAIR_STATUS_AT_FREEZE:
  A: NOT_RUN
  B: NOT_RUN
  condition_assignment: FROZEN
  same_inputs: FROZEN_IN_THIS_FILE
  evaluator_independence: NONE
  order: A_THEN_B
  order_bias: HIGH
  result: NOT_YET_OBSERVED
```
