# INITIAL MATERIAL L8｜E 總成本／錯誤成本及維護
**Cycle:** SEED-L8-E-INITIAL-001 • SAME_MODEL_MULTI_ROLE_REFERENCE
**Preconditions:** `METHOD/EV_A0_E_METHOD_DECISION.md` → `OBSERVATION/EV_A1_E_FIRST_OBSERVATION.md` → THIS initial material L8. Pack receipt as applicable. **No other seat's current stance used as scoped input.**
**Council Round:** R001, not equal to L8 internal R1/R2/R3+.

## R1｜互競的初始 premises
- **E-P1** SEED 越短越好。**對抗：** 極短易缺來源和適用邊界，重讀/糾錯成本大
- **E-P2** 每次都載完整 Archive。**對抗：** 保留全部內容但 context/檢索/注意力污染巨大
- **E-P3** Core Seed + Versioned Evidence Pointers，按需讀取。**對抗：** 可能降低啟動開銷，但憑空丟 pointer 也可能失聯
- **E-P4** 每一種再生目標保留最小包而非全域一份。**對抗：** 較準，但維護多版本關係與測試負擔
**Point-Light / O9 R1:** 以上候選及反例是可見的文本競爭，不聲稱讀到模型隱藏內部狀態。
**T1 SEED-E-T1：** 成本不等於 token 費。錯誤 SEED 讓下一個人錯誤授權、錯誤引用或臆造歷史的長期成本，可能比短檔案省下的讀取量大。

## R2｜本席消費 T1
提出比較量：`C_total = C_seed_authoring + C_version_check + C_retrieval + C_regeneration + C_audit + E(loss_from_false_reconstruction)`。沒有數據不能精算，也不主張把所有會議壓成單檔。資料應有耐久錨點、來源缺失時可 HOLD、版本不一致需觸發重新核對。
**O9 R2：** 將反對/黑區帶回本席，不代寫他席立場。
**T2 SEED-E-T2：** 最小充分結構不是檔案長度最短，而是滿足最低生成可靠性的前提下，總擁有成本可接受；需多個不同場景才能估測。

## Post-R2 Premise Audit
- `MULTIPLE_PREMISE_FAMILIES=true`：來源／觀察／資格／反證／成本是否成立不由單一縮短文本假設決定。
- `R3_REQUIRED=true`：仍有未解的最小性/再生/史料/行為對照前提。

## R3｜保留異議並跨前提核查
成本核對不能倒逼修正當時史料：若證據讀取太貴，可能採摘要/索引，但不能把摘要升格成 canonical truth。真正高風險法位要優先完整核對。
**O9 R3：** 反例仍存在，沒有因寫了 Main 就自行升格。
**T3 SEED-E-T3：** 交還可追查的概念物件與尚未證實項目。

## Main + Origin Declared Typed Objects
```yaml
origin_actor: CORE_SEAT_E
origin_event_id: SEED-EV-A2-E
main_ref: SEED-E-MAIN-001
main: "TARGET_RELATIVE_TOTAL_COST_OF_REGENERATION"
origin_semantic_type: "RESOURCE_CONDITION+COUNTERFORCE"
stance: "TOTAL_COST_AND_ERROR_RISK_SHOULD_BE_MEASURED_WITHOUT_MINIMALITY_AS_SHORTNESS"
surviving_objection: "沒有實測 tokens/latency/false reconstruction rate；不得假稱成本效益"
source_method_decision: SEED-EV-A0-E
source_first_observation: SEED-EV-A1-E
external_expert_return: NONE
proposal_originated: NONE
```

## SGER / Compact L8 receipt
```yaml
SGER:
  cycle: SEED-L8-E-INITIAL-001
  R1: [E-P1,E-P2,E-P3,E-P4]
  T1: SEED-E-T1
  R2_consumes_T1: true
  T2: SEED-E-T2
  post_R2_premise_audit: MULTIPLE
  R3_plus: [R3]
  T3: SEED-E-T3
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  Main: SEED-E-MAIN-001
  TM: "SEED-E-TM: no historical validation/seat qualification backfill"
  Vertical_Acceptance: CONDITIONAL_CONCEPT_OBJECT
  execution_identity: SAME_MODEL_MULTI_ROLE_REFERENCE
  evidence_status: TEXTUAL_REFERENCE_NOT_INDEPENDENT_MODEL_PROOF
```
**Compact L8 Cycle Receipt:** R1→T1→R2 consumes T1→T2→plurality check→R3/T3→MAIN/TM/SGER; this is an observable scoped judgement, not actual independent model invocation.
