# INITIAL MATERIAL L8｜D 測試與工程可觀測性
**Cycle:** SEED-L8-D-INITIAL-001 • SAME_MODEL_MULTI_ROLE_REFERENCE
**Preconditions:** `METHOD/EV_A0_D_METHOD_DECISION.md` → `OBSERVATION/EV_A1_D_FIRST_OBSERVATION.md` → THIS initial material L8. Pack receipt as applicable. **No other seat's current stance used as scoped input.**
**Council Round:** R001, not equal to L8 internal R1/R2/R3+.

## R1｜互競的初始 premises
- **D-P1** 把 SEED 交新節點，再讓它重述內容。**對抗：** 只能證明文字記憶或模仿
- **D-P2** 以另一個主題的 D0 作盲化輸入、只提供最小 SEED。**對抗：** 可看是否自然產生獨立問題，但仍需控制組
- **D-P3** 在 SEED 中依序刪除某一生成關係，做 ablation。**對抗：** 可近似測必需性，但單案例可能非代表性
- **D-P4** 把全 Git Archive 與 SEED 一併給新節點。**對抗：** 增加來源資料，也增加 framing / token 影響
**Point-Light / O9 R1:** 以上候選及反例是可見的文本競爭，不聲稱讀到模型隱藏內部狀態。
**T1 SEED-D-T1：** 要測『最小』必須能把某條必要關係移除，並觀察結果在不同新題上是否崩落；不能單靠作者宣稱移除就會失敗。

## R2｜本席消費 T1
提出一個可重播但尚未執行的比較矩陣：N0 無 Seed 的一般回答，S1 完整 Seed，S-1 移除關鍵邊的 Seed，R1 隨機選法位正確的史料包；全部使用陌生題，記錄相同輸入條件、席位是否各自形成判斷、重大反對有沒有被正確消費，並由看不到 Condition Label 的評審核實。
**O9 R2：** 將反對/黑區帶回本席，不代寫他席立場。
**T2 SEED-D-T2：** 概念上的可判別性建立在 `WHY_THIS_EDGE_NEEDED` 和 `WHAT_BREAKS_IF_REMOVED`；工程實作還缺輸入隔離、試題集和盲評工具。

## Post-R2 Premise Audit
- `MULTIPLE_PREMISE_FAMILIES=true`：來源／觀察／資格／反證／成本是否成立不由單一縮短文本假設決定。
- `R3_REQUIRED=true`：仍有未解的最小性/再生/史料/行為對照前提。

## R3｜保留異議並跨前提核查
注意控制偏差：如果評分只獎勵『六席輪流改判』，就會出現治理劇場；必須允許有理由保留立場與無 Material Wake。未取得獨立評審前不能叫 benchmark proven。
**O9 R3：** 反例仍存在，沒有因寫了 Main 就自行升格。
**T3 SEED-D-T3：** 交還可追查的概念物件與尚未證實項目。

## Main + Origin Declared Typed Objects
```yaml
origin_actor: CORE_SEAT_D
origin_event_id: SEED-EV-A2-D
main_ref: SEED-D-MAIN-001
main: "SEED_REGENERATION_ABLATION_PROTOCOL_CANDIDATE"
origin_semantic_type: "TEST_DESIGN+ENGINEERING_GAP"
stance: "REGENERATION_CLAIMS_REQUIRE_HIDDEN_TEST_AND_ABLATION_NOT_REPLAY"
surviving_objection: "工程與獨立盲評未建置；Git 文件本身不構成實驗結果"
source_method_decision: SEED-EV-A0-D
source_first_observation: SEED-EV-A1-D
external_expert_return: NONE
proposal_originated: NONE
```

## SGER / Compact L8 receipt
```yaml
SGER:
  cycle: SEED-L8-D-INITIAL-001
  R1: [D-P1,D-P2,D-P3,D-P4]
  T1: SEED-D-T1
  R2_consumes_T1: true
  T2: SEED-D-T2
  post_R2_premise_audit: MULTIPLE
  R3_plus: [R3]
  T3: SEED-D-T3
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  Main: SEED-D-MAIN-001
  TM: "SEED-D-TM: no historical validation/seat qualification backfill"
  Vertical_Acceptance: CONDITIONAL_CONCEPT_OBJECT
  execution_identity: SAME_MODEL_MULTI_ROLE_REFERENCE
  evidence_status: TEXTUAL_REFERENCE_NOT_INDEPENDENT_MODEL_PROOF
```
**Compact L8 Cycle Receipt:** R1→T1→R2 consumes T1→T2→plurality check→R3/T3→MAIN/TM/SGER; this is an observable scoped judgement, not actual independent model invocation.
