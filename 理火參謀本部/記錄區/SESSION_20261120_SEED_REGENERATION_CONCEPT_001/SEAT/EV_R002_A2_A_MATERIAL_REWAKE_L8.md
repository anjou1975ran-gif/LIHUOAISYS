# R002 MATERIAL REWAKE｜CORE SEAT A
**Cycle:** SEED-L8-A-R002-001; **Origin:** CORE_SEAT_A
**Material trigger:** C R001 source standing objection SEED-MREL-001
**Prior owned R001 material stays immutable.** This is an owned response to routed objections, not Secretary rewrite.
**Clock A for new issue:** `METHOD/EV_R002_A0_A_METHOD_RESCREEN.md` → `OBSERVATION/EV_R002_A1_A_NEW_MATERIAL_FIRST_OBSERVATION.md` → THIS R002 L8.
**Execution:** SAME_MODEL_MULTI_ROLE_REFERENCE.

## Previous position and material delta
- **Previous:** Story-based failure examples offered as one parallel first-step SEED form, with only general leakage caution.
- **T1/objection intake:** C 的 `CONTEMPORANEOUS/RETROSPECTIVE/HYPOTHESIS` 讓 Option 1 有實質污染風險：舊案例中誰輸誰贏、誰被說服，可能變成新節點的預設立場；Option 2 則太抽象。

## R1 candidate competition
Option 1: Give prior failure stories upfront so new node learns faster; Option 2: Strip all history and supply slogans; Option 3: Split generating conditions from historical feedback released only after own action.
**O9 R1:** observe premise contrast, not actual model neuron read.
**T1:** SEED-A-R002-T1 — C 的 `CONTEMPORANEOUS/RETROSPECTIVE/HYPOTHESIS` 讓 Option 1 有實質污染風險：舊案例中誰輸誰贏、誰被說服，可能變成新節點的預設立場；Option 2 則太抽象。

## R2 consumes T1
**Owned material stance revision A-V1:** 故事型材料從『預載入 SEED 的教學內容』降成 `OPTIONAL_FEEDBACK_ARCHIVE`。第一階段 Seed 保留面對陌生題的生成任務、必要關係和可自我否定/重新問的條件；歷史失敗案例不直接交給受測節點，在作出初判後經來源定位交由評審/節點做有條件核對，且保留原時事件與事後歸因的區別。保留 SEED 可含短反例形式的可能，但不可包含可還原舊答案的細節。
**O9 R2:** correction of previous own stance after scoped new input.
**T2:** SEED-A-R002-T2 — 從『示例幫助遷移』轉為『先自行形成問題→可追史料作事後 feedback』，是對資料流/授權順序的實質變更，不是換詞。

## Post-R2 Premise Audit
`MULTIPLE_PREMISES=true`; question of usefulness vs contamination / cost remains; R3 required as counter-test.

## R3, surviving counterforce
反證：若毫無案例可讀，新節點可能只會背抽象義務；允許在首次生成後用 Archive 輔助學習，但不能把 feedback 階段的失敗修正冒稱第一次生成。這不是人工或模型權重真的接受訓練的證明。
**T3:** SEED-A-R002-T3 — preserve objection and new test requirement.

## Main / Origin-declared event
```yaml
event_id: SEED-EV-R002-A
origin_actor: CORE_SEAT_A
type: POSITION_REVISION+NEW_RELATION
material_trigger_refs: [SEED-MREL-001]
old_stance: "Story-based failure examples offered as one parallel first-step SEED form, with only general leakage caution."
new_stance: "HISTORICAL_FAILURE_STORIES_NOT_REQUIRED_AS_PRELOADED_SEED_CORE"
main: "A-SEED-FEEDBACK-SEPARATION"
surviving_objection: "何時開放 Archive 與如何防記憶污染需測試"
specialist_return: NONE
```

## TM / SGER / Compact L8 receipt
```yaml
SGER:
  cycle: SEED-L8-A-R002-001
  R1: MATERIAL_CANDIDATE_COMPETITION
  T1: SEED-A-R002-T1
  R2_consumes_T1: true
  T2: SEED-A-R002-T2
  Post_R2_Audit: PLURAL_PREMISES
  R3: COUNTERFORCE
  T3: SEED-A-R002-T3
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  MAIN: SEED-A-R002-MAIN
  TM: "Response is owned by A, not secretary; prior stance unmodified"
  VerticalAcceptance: CONDITIONAL_CONCEPT_EVENT
  execution_identity: SAME_MODEL_MULTI_ROLE_REFERENCE
```
**Compact receipt:** SEAT WAKE → R1/T1 → R2 consumes T1 → T2 → R3/T3 → Main/TM/SGER → vertical conditional acceptance. No independent Agent.
