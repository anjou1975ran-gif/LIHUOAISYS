# INITIAL MATERIAL L8｜A 可能性擴張與能力遷移
**Cycle:** SEED-L8-A-INITIAL-001 • SAME_MODEL_MULTI_ROLE_REFERENCE
**Preconditions:** `METHOD/EV_A0_A_METHOD_DECISION.md` → `OBSERVATION/EV_A1_A_FIRST_OBSERVATION.md` → THIS initial material L8. Pack receipt as applicable. **No other seat's current stance used as scoped input.**
**Council Round:** R001, not equal to L8 internal R1/R2/R3+.

## R1｜互競的初始 premises
- **A-P1** 故事型 SEED：留下幾次核心失敗與改判例子作練習。**對抗：** 能促發對失敗的辨識，也可能抄到舊案框架
- **A-P2** 關係型 SEED：給必要責任/反對/改判條件，讓新題自己生出具體方向。**對抗：** 較能遷移，但抽象到不足以啟動時會失敗
- **A-P3** 對抗型 SEED：給新節點可自行測試的失效條件或問題設計。**對抗：** 可以驗證，但測試題若洩漏評分會演練通過
- **A-P4** 生態型 SEED：新節點能索取來源、反例與不同方法，而不是被灌整包。**對抗：** 不綁答案，卻依賴可用的讀取權與版本
**Point-Light / O9 R1:** 以上候選及反例是可見的文本競爭，不聲稱讀到模型隱藏內部狀態。
**T1 SEED-A-T1：** 教育方法不等於把樣板答案塞給學生；當『故事』變教材時，可能讓新節點模仿老席位的語氣、異議位置與解題路徑。

## R2｜本席消費 T1
保留四條生成候選，但對故事型標記 LEAKAGE_RISK；提出『seed=生成關係／任務要求，案例另存有法位的 Archive』作可競爭方案。並主張對新節點設反證活動：移除某一關係後，看看它是否失去形成改判理由的能力。
**O9 R2：** 將反對/黑區帶回本席，不代寫他席立場。
**T2 SEED-A-T2：** 要讓遷移自己發生，生成條件應能運用新素材，而非照搬既有例子；歷史敘事可供事後驗證而非必須先全文傳給新節點。

## Post-R2 Premise Audit
- `MULTIPLE_PREMISE_FAMILIES=true`：來源／觀察／資格／反證／成本是否成立不由單一縮短文本假設決定。
- `R3_REQUIRED=true`：仍有未解的最小性/再生/史料/行為對照前提。

## R3｜保留異議並跨前提核查
反向挑戰：純抽象條件也可能變成『漂亮術語測驗』；必須有以陌生題為輸入的可觀察任務，而不只反覆問理火原則。若沒有實際效果測試，不宣稱教育心法能提高 AI 能力。
**O9 R3：** 反例仍存在，沒有因寫了 Main 就自行升格。
**T3 SEED-A-T3：** 交還可追查的概念物件與尚未證實項目。

## Main + Origin Declared Typed Objects
```yaml
origin_actor: CORE_SEAT_A
origin_event_id: SEED-EV-A2-A
main_ref: SEED-A-MAIN-001
main: "FOUR_SEED_GENERATING_FAMILIES"
origin_semantic_type: "NEW_PATH_SET+LEAKAGE_RISK"
stance: "KEEP_MULTIPLE_SEED_FORMS_OPEN_WITH_CAUTION_ON_HISTORICAL_EXEMPLARS"
surviving_objection: "把歷史故事給新節點可能鎖框；但完全刪例子可能讓 SEED 無從復原"
source_method_decision: SEED-EV-A0-A
source_first_observation: SEED-EV-A1-A
external_expert_return: NONE
proposal_originated: NONE
```

## SGER / Compact L8 receipt
```yaml
SGER:
  cycle: SEED-L8-A-INITIAL-001
  R1: [A-P1,A-P2,A-P3,A-P4]
  T1: SEED-A-T1
  R2_consumes_T1: true
  T2: SEED-A-T2
  post_R2_premise_audit: MULTIPLE
  R3_plus: [R3]
  T3: SEED-A-T3
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  Main: SEED-A-MAIN-001
  TM: "SEED-A-TM: no historical validation/seat qualification backfill"
  Vertical_Acceptance: CONDITIONAL_CONCEPT_OBJECT
  execution_identity: SAME_MODEL_MULTI_ROLE_REFERENCE
  evidence_status: TEXTUAL_REFERENCE_NOT_INDEPENDENT_MODEL_PROOF
```
**Compact L8 Cycle Receipt:** R1→T1→R2 consumes T1→T2→plurality check→R3/T3→MAIN/TM/SGER; this is an observable scoped judgement, not actual independent model invocation.
