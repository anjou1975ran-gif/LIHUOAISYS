# INITIAL MATERIAL L8｜C 史料／資格邊界審計
**Cycle:** SEED-L8-C-INITIAL-001 • SAME_MODEL_MULTI_ROLE_REFERENCE
**Preconditions:** `METHOD/EV_A0_C_METHOD_DECISION.md` → `OBSERVATION/EV_A1_C_FIRST_OBSERVATION.md` → THIS initial material L8. Pack receipt as applicable. **No other seat's current stance used as scoped input.**
**Council Round:** R001, not equal to L8 internal R1/R2/R3+.

## R1｜互競的初始 premises
- **C-P1** 把後來整理的 Lesson 當成當時真相。**對抗：** 事後選擇性歸因可能替舊史補票
- **C-P2** 只交給新節點全部原始 Git 事件。**對抗：** 保真但高污染、耗時，缺少何者關係為必要的指引
- **C-P3** 將證據本體與生成條件分層，宣告來源/解釋與不確定性。**對抗：** 能保留歷史而不預設答案，但需要可查錨點
- **C-P4** 以『從同一歷史中可推多種解釋』提醒模型持續質疑 SEED。**對抗：** 可防後知回鑄，也可能讓研究陷入永久不確定
**Point-Light / O9 R1:** 以上候選及反例是可見的文本競爭，不聲稱讀到模型隱藏內部狀態。
**T1 SEED-C-T1：** 原始事件與事後 SEED 不是同一種時間地位；『由某席反對造成改判』必須有先後有據的 source chain，不能只因後來的 README 說有就當作實證。

## R2｜本席消費 T1
提出三欄來源標記：當時原始事件 `CONTEMPORANEOUS`、事後審計/整理 `RETROSPECTIVE`、尚未證實的因果 `HYPOTHESIS`。新 SEED 至少應有來源錨點與 Standing Resolver；歷史不足的部分不得以角色行為模板填空。C 反對以訓練通過、源頭真相或跨節點成功的名義包裝 SEED。
**O9 R2：** 將反對/黑區帶回本席，不代寫他席立場。
**T2 SEED-C-T2：** 新節點可以學會產生追蹤鏈，但無論多像當時的人，都不得改寫舊事件的已知時序。

## Post-R2 Premise Audit
- `MULTIPLE_PREMISE_FAMILIES=true`：來源／觀察／資格／反證／成本是否成立不由單一縮短文本假設決定。
- `R3_REQUIRED=true`：仍有未解的最小性/再生/史料/行為對照前提。

## R3｜保留異議並跨前提核查
最不舒服的反例是：過去的完整事件也可能只記錄同模型文本因果，不能直接證明真正因果獨立。原始資料的保真只能證明它被保存，不能證明 SEED 有效。
**O9 R3：** 反例仍存在，沒有因寫了 Main 就自行升格。
**T3 SEED-C-T3：** 交還可追查的概念物件與尚未證實項目。

## Main + Origin Declared Typed Objects
```yaml
origin_actor: CORE_SEAT_C
origin_event_id: SEED-EV-A2-C
main_ref: SEED-C-MAIN-001
main: "HISTORICAL_SOURCE_STANDING_AND_NO_RETROACTIVE_CAUSALITY"
origin_semantic_type: "QUALIFICATION_OBJECTION+SOURCE_CONDITION"
stance: "SEED_MUST_PRESERVE_SOURCE_ORIGIN_AND_UNKNOWN_STANDING_WITHOUT_BACKFILL"
surviving_objection: "歷史來源再完整，未實做新節點實驗前也不能證明生成成功"
source_method_decision: SEED-EV-A0-C
source_first_observation: SEED-EV-A1-C
external_expert_return: NONE
proposal_originated: NONE
```

## SGER / Compact L8 receipt
```yaml
SGER:
  cycle: SEED-L8-C-INITIAL-001
  R1: [C-P1,C-P2,C-P3,C-P4]
  T1: SEED-C-T1
  R2_consumes_T1: true
  T2: SEED-C-T2
  post_R2_premise_audit: MULTIPLE
  R3_plus: [R3]
  T3: SEED-C-T3
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  Main: SEED-C-MAIN-001
  TM: "SEED-C-TM: no historical validation/seat qualification backfill"
  Vertical_Acceptance: CONDITIONAL_CONCEPT_OBJECT
  execution_identity: SAME_MODEL_MULTI_ROLE_REFERENCE
  evidence_status: TEXTUAL_REFERENCE_NOT_INDEPENDENT_MODEL_PROOF
```
**Compact L8 Cycle Receipt:** R1→T1→R2 consumes T1→T2→plurality check→R3/T3→MAIN/TM/SGER; this is an observable scoped judgement, not actual independent model invocation.
