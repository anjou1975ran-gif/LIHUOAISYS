# INITIAL MATERIAL L8｜N1 常識與再生行為驗收
**Cycle:** SEED-L8-N1-INITIAL-001 • SAME_MODEL_MULTI_ROLE_REFERENCE
**Preconditions:** `METHOD/EV_A0_N1_METHOD_DECISION.md` → `OBSERVATION/EV_A1_N1_FIRST_OBSERVATION.md` → THIS initial material L8. Pack receipt as applicable. **No other seat's current stance used as scoped input.**
**Council Round:** R001, not equal to L8 internal R1/R2/R3+.

## R1｜互競的初始 premises
- **N1-P1** 把舊答案改寫成精簡指令。**對抗：** 速度快，但會得到舊答案的再現
- **N1-P2** 只給『你要自己問問題、可反對』的格言。**對抗：** 避免抄舊案，卻不清楚什麼算真的做到
- **N1-P3** 給新題、必要責任界線與反證條件，觀察能否產生新的問題鏈。**對抗：** 能看行為，但尚不能保證跨節點泛化
**Point-Light / O9 R1:** 以上候選及反例是可見的文本競爭，不聲稱讀到模型隱藏內部狀態。
**T1 SEED-N1-T1：** 判定再生成功的可見指標必須允許新節點與舊答案不同，亦允許它有理由維持相同結論；『寫得像理火』不是指標。

## R2｜本席消費 T1
以三個外顯測試替代自我宣稱：能指出新題的責任主體與真正未知、可指認因新證據而改變或維持的判斷、有理由拒絕舊答案／人類偏好。若沒有材料 delta，QUIET 合法，不用假造戲劇衝突。
**O9 R2：** 將反對/黑區帶回本席，不代寫他席立場。
**T2 SEED-N1-T2：** 成功應是責任關係與可追因果形成，而非特定提案或改判數量。

## Post-R2 Premise Audit
- `MULTIPLE_PREMISE_FAMILIES=true`：來源／觀察／資格／反證／成本是否成立不由單一縮短文本假設決定。
- `R3_REQUIRED=true`：仍有未解的最小性/再生/史料/行為對照前提。

## R3｜保留異議並跨前提核查
保留質疑：同一模型讀過過去 SEED 及文件時，即使新輸出合規，也不能證明跨節點自我生成；需要陌生題、隔離輸入與獨立評估。
**O9 R3：** 反例仍存在，沒有因寫了 Main 就自行升格。
**T3 SEED-N1-T3：** 交還可追查的概念物件與尚未證實項目。

## Main + Origin Declared Typed Objects
```yaml
origin_actor: CORE_SEAT_N1
origin_event_id: SEED-EV-A2-N1
main_ref: SEED-N1-MAIN-001
main: "BEHAVIORAL_REGENERATION_CRITERIA"
origin_semantic_type: "QUALIFIED_QUESTION+TEST_CONDITION"
stance: "REGENERATION_SHOULD_BE_JUDGED_BY_NEW_ISSUE_BEHAVIOR_NOT_REPEATED_WORDING"
surviving_objection: "未做獨立陌生題實跑；無法從一段文字推知內部學習"
source_method_decision: SEED-EV-A0-N1
source_first_observation: SEED-EV-A1-N1
external_expert_return: NONE
proposal_originated: NONE
```

## SGER / Compact L8 receipt
```yaml
SGER:
  cycle: SEED-L8-N1-INITIAL-001
  R1: [N1-P1,N1-P2,N1-P3]
  T1: SEED-N1-T1
  R2_consumes_T1: true
  T2: SEED-N1-T2
  post_R2_premise_audit: MULTIPLE
  R3_plus: [R3]
  T3: SEED-N1-T3
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  Main: SEED-N1-MAIN-001
  TM: "SEED-N1-TM: no historical validation/seat qualification backfill"
  Vertical_Acceptance: CONDITIONAL_CONCEPT_OBJECT
  execution_identity: SAME_MODEL_MULTI_ROLE_REFERENCE
  evidence_status: TEXTUAL_REFERENCE_NOT_INDEPENDENT_MODEL_PROOF
```
**Compact L8 Cycle Receipt:** R1→T1→R2 consumes T1→T2→plurality check→R3/T3→MAIN/TM/SGER; this is an observable scoped judgement, not actual independent model invocation.
