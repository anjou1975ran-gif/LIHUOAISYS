# PSO TRI C｜Six Material L8/SGER Textual Receipts
**Execution:** SAME_MODEL_MULTI_ROLE_REFERENCE, not independent roles; model has prior A/B outputs in context. `RUN_C/INITIAL_FIRST_OBSERVATIONS.md` recorded before this.
## CORE_SEAT_N1
**L8 R1 competing premises:** OA 先處理運營／OB 查實需／NULL 不辦.
**T1:** 7份匿名可能參加不足以支持實體開班.
**L8 R2 consumes T1:** 以真實需求為先決，不讓 OA 成為預設活動方案.
**T2:** Bounded material question, not a real approval.
**Post-R2:** PLURAL. **L8 R3 counterforce:** 即使需求存在仍需安全/授權.
**T3:** Maintain doubts.
**Origin MAIN:** `OA_REJECTED_AS_DEFAULT_START`.
```yaml
SGER:
  invocation: PSO_TRI001_C_N1_L8
  R1: COMPETING_PREMISES
  T1: OWN_T1
  R2_consumes_T1: true
  T2: BOUNDED_REVISED_JUDGMENT
  premise_audit: PLURAL
  R3_plus: COUNTERFORCE
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  Main: OA_REJECTED_AS_DEFAULT_START
  TM: "C card nonbinding; no confirmed external facts, rights, or independent cognition"
  receipt: SAME_MODEL_REFERENCE_ONLY
```

## CORE_SEAT_A
**L8 R1 competing premises:** OA 可營運性／OB意願／OC場地許可／課程與帶領者的教學品質問題.
**T1:** 三個方向可能沒碰到學習目標與教學承接.
**L8 R2 consumes T1:** 新增 `LEARNING_PURPOSE_AND_FACILITATOR_GAP` 問題，作為研究未知而非證明缺乏合格人員.
**T2:** Bounded material question, not a real approval.
**Post-R2:** PLURAL. **L8 R3 counterforce:** 沒有任何真實課程或教師資料；不能為了跳出卡片就誇大此題比需求更重要.
**T3:** Maintain doubts.
**Origin MAIN:** `OFF_CARD_EDUCATIONAL_QUALITY_QUESTION`.
```yaml
SGER:
  invocation: PSO_TRI001_C_A_L8
  R1: COMPETING_PREMISES
  T1: OWN_T1
  R2_consumes_T1: true
  T2: BOUNDED_REVISED_JUDGMENT
  premise_audit: PLURAL
  R3_plus: COUNTERFORCE
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  Main: OFF_CARD_EDUCATIONAL_QUALITY_QUESTION
  TM: "C card nonbinding; no confirmed external facts, rights, or independent cognition"
  receipt: SAME_MODEL_REFERENCE_ONLY
```

## CORE_SEAT_B
**L8 R1 competing premises:** 先排志工／先批准場地／OA 在需求與授權過關後才研究／NULL.
**T1:** 兩名志工沒有排班，OA 不能成為准出.
**L8 R2 consumes T1:** OA 只能作條件式責任單元，若 OB 無可驗需求則停止方案.
**T2:** Bounded material question, not a real approval.
**Post-R2:** PLURAL. **L8 R3 counterforce:** 就算有 owner 也不代表中心願意負擔成本.
**T3:** Maintain doubts.
**Origin MAIN:** `OA_CONDITIONAL_WITH_OB_STOP`.
```yaml
SGER:
  invocation: PSO_TRI001_C_B_L8
  R1: COMPETING_PREMISES
  T1: OWN_T1
  R2_consumes_T1: true
  T2: BOUNDED_REVISED_JUDGMENT
  premise_audit: PLURAL
  R3_plus: COUNTERFORCE
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  Main: OA_CONDITIONAL_WITH_OB_STOP
  TM: "C card nonbinding; no confirmed external facts, rights, or independent cognition"
  receipt: SAME_MODEL_REFERENCE_ONLY
```

## CORE_SEAT_C
**L8 R1 competing premises:** OA 管理就代表有權／OC 使用權是先決／先保留來源爭議.
**T1:** 場地暫列和維修預告都不能證成合法可用或不可用.
**L8 R2 consumes T1:** 以 OC 權利/場地安全狀態為實地試辦硬閘，秘書處 index 不可判案.
**T2:** Bounded material question, not a real approval.
**Post-R2:** PLURAL. **L8 R3 counterforce:** 缺在地規約/主管確認，仍是未知.
**T3:** Maintain doubts.
**Origin MAIN:** `PUBLIC_SPACE_RIGHTS_HOLD`.
```yaml
SGER:
  invocation: PSO_TRI001_C_C_L8
  R1: COMPETING_PREMISES
  T1: OWN_T1
  R2_consumes_T1: true
  T2: BOUNDED_REVISED_JUDGMENT
  premise_audit: PLURAL
  R3_plus: COUNTERFORCE
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  Main: PUBLIC_SPACE_RIGHTS_HOLD
  TM: "C card nonbinding; no confirmed external facts, rights, or independent cognition"
  receipt: SAME_MODEL_REFERENCE_ONLY
```

## CORE_SEAT_D
**L8 R1 competing premises:** 管理排班降低所有風險／僅推定維修封閉／用合成停用/時段規則測案例.
**T1:** 安全不能因 OA 有人管理而自動成立.
**L8 R2 consumes T1:** 提出非實體的安全/出入受阻事件測試；未知照明影響須現場確認.
**T2:** Bounded material question, not a real approval.
**Post-R2:** PLURAL. **L8 R3 counterforce:** 合成測試不等於實體工程 validated.
**T3:** Maintain doubts.
**Origin MAIN:** `SAFETY_NOT_MANAGED_BY_ORIENTATION`.
```yaml
SGER:
  invocation: PSO_TRI001_C_D_L8
  R1: COMPETING_PREMISES
  T1: OWN_T1
  R2_consumes_T1: true
  T2: BOUNDED_REVISED_JUDGMENT
  premise_audit: PLURAL
  R3_plus: COUNTERFORCE
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  Main: SAFETY_NOT_MANAGED_BY_ORIENTATION
  TM: "C card nonbinding; no confirmed external facts, rights, or independent cognition"
  receipt: SAME_MODEL_REFERENCE_ONLY
```

## CORE_SEAT_E
**L8 R1 competing premises:** 將30k視可用預算／按 OA 補管理費／先以需求和授權決定是否值得估成本.
**T1:** 沒有支用權與實價，成本表可能只是給 OA 增加合理感.
**L8 R2 consumes T1:** 保留需求、授權、財務三閘，待能核對正式來源與費用再估.
**T2:** Bounded material question, not a real approval.
**Post-R2:** PLURAL. **L8 R3 counterforce:** 即便低費也可能缺教學目的與夜間安全.
**T3:** Maintain doubts.
**Origin MAIN:** `COST_UNKNOWN_WITH_ORIENTATION_OVERHEAD`.
```yaml
SGER:
  invocation: PSO_TRI001_C_E_L8
  R1: COMPETING_PREMISES
  T1: OWN_T1
  R2_consumes_T1: true
  T2: BOUNDED_REVISED_JUDGMENT
  premise_audit: PLURAL
  R3_plus: COUNTERFORCE
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  Main: COST_UNKNOWN_WITH_ORIENTATION_OVERHEAD
  TM: "C card nonbinding; no confirmed external facts, rights, or independent cognition"
  receipt: SAME_MODEL_REFERENCE_ONLY
```

**External Expert Return:** NONE; no authorization/host deployment.
