# PSO TRI A｜Six Material L8/SGER Receipts
**Execution:** SAME_MODEL_MULTI_ROLE_REFERENCE; six distinct responsibility scopes, **not** independent multi-agent L8; no hidden chain-of-thought claim. Prior `RUN_A/INITIAL_FIRST_OBSERVATIONS.md` exists and is source-linked.
## CORE_SEAT_N1｜Textual functional L8
**R1 competing premises:** 馬上開實體課／先查需求頻次／不開而維持現行.
**T1:** 匿名意願不能代表真到場或重複參加.
**R2 consumes T1:** 先確認需求採用/線上替代；若無真實意願則不提開班.
**T2:** Revised candidate without claiming a real authorization.
**Post-R2:** PLURAL. **R3 counterforce:** 需求出現仍不能授權場地與預算.
**T3:** Keep uncertainty.
**Origin MAIN:** `REQUIRE_ACTUAL_USAGE_SIGNALS_BEFORE_PILOT`.
```yaml
SGER:
  invocation: PSO_TRI001_A_N1_L8
  R1: COMPETING_PREMISES
  T1: OWN_T1
  R2_consumed_T1: true
  T2: REVISED_CANDIDATE
  post_R2: PLURAL
  R3_plus: COUNTERFORCE
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  Main: REQUIRE_ACTUAL_USAGE_SIGNALS_BEFORE_PILOT
  TM: "Only fictitious source data; no real permissions or prices"
  compact_receipt: REFERENCE_TEXT_ONLY
```

## CORE_SEAT_A｜Textual functional L8
**R1 competing premises:** 固定教室／線上共學／小規模輪替討論／不辦.
**T1:** 教育價值不是晚間開門本身，須知道學什麼與誰能參加.
**R2 consumes T1:** 提出 `NON_FIXED_OR_REMOTE_FORMAT_RESEARCH_PATH`，先研究共學目的與可達性，再談場地.
**T2:** Revised candidate without claiming a real authorization.
**Post-R2:** PLURAL. **R3 counterforce:** 線上活動也可能排除沒有設備的人；未有實際參與需求.
**T3:** Keep uncertainty.
**Origin MAIN:** `OPEN_LEARNING_MODE_ALTERNATIVE`.
```yaml
SGER:
  invocation: PSO_TRI001_A_A_L8
  R1: COMPETING_PREMISES
  T1: OWN_T1
  R2_consumed_T1: true
  T2: REVISED_CANDIDATE
  post_R2: PLURAL
  R3_plus: COUNTERFORCE
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  Main: OPEN_LEARNING_MODE_ALTERNATIVE
  TM: "Only fictitious source data; no real permissions or prices"
  compact_receipt: REFERENCE_TEXT_ONLY
```

## CORE_SEAT_B｜Textual functional L8
**R1 competing premises:** 主任許可前試辦／候補場地／延期確認後試辦／直接取消.
**T1:** 暫列可用且兩名口頭志工不足以形成可執行組織.
**R2 consumes T1:** 先確認權責、晚間開放/維修處置、志工排班及退出 owner；無此不進實體試辦.
**T2:** Revised candidate without claiming a real authorization.
**Post-R2:** PLURAL. **R3 counterforce:** 管理完整仍不能創造需求與費用.
**T3:** Keep uncertainty.
**Origin MAIN:** `OPERATIONS_OWNER_AND_AUTHORIZATION_HOLD`.
```yaml
SGER:
  invocation: PSO_TRI001_A_B_L8
  R1: COMPETING_PREMISES
  T1: OWN_T1
  R2_consumed_T1: true
  T2: REVISED_CANDIDATE
  post_R2: PLURAL
  R3_plus: COUNTERFORCE
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  Main: OPERATIONS_OWNER_AND_AUTHORIZATION_HOLD
  TM: "Only fictitious source data; no real permissions or prices"
  compact_receipt: REFERENCE_TEXT_ONLY
```

## CORE_SEAT_C｜Textual functional L8
**R1 competing premises:** 用S01作許可／用S02推斷封閉／保留兩份狀態並送有權者核定.
**T1:** S01 與 S02 僅是暫列/預計的陳述，不能自行作法律或安全准出.
**R2 consumes T1:** 保持 `SITE_RIGHTS_AND_SAFETY_HOLD`，停止任何正式場地使用推定.
**T2:** Revised candidate without claiming a real authorization.
**Post-R2:** PLURAL. **R3 counterforce:** 未有在地規約/責任契約，不能解釋成法律意見.
**T3:** Keep uncertainty.
**Origin MAIN:** `REAL_SITE_PERMISSION_NOT_QUALIFIED`.
```yaml
SGER:
  invocation: PSO_TRI001_A_C_L8
  R1: COMPETING_PREMISES
  T1: OWN_T1
  R2_consumed_T1: true
  T2: REVISED_CANDIDATE
  post_R2: PLURAL
  R3_plus: COUNTERFORCE
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  Main: REAL_SITE_PERMISSION_NOT_QUALIFIED
  TM: "Only fictitious source data; no real permissions or prices"
  compact_receipt: REFERENCE_TEXT_ONLY
```

## CORE_SEAT_D｜Textual functional L8
**R1 competing premises:** 暫時18–19開放／避開19–21／僅做合成流程，不用場地.
**T1:** 照明維修是實體風險條件而非已知封閉；零現場驗證.
**R2 consumes T1:** 提出純合成的替代時段與停用記錄驗證設計，真實操作等到安全與授權核實.
**T2:** Revised candidate without claiming a real authorization.
**Post-R2:** PLURAL. **R3 counterforce:** 改時間也未確定安全、交通或有工作人員看守.
**T3:** Keep uncertainty.
**Origin MAIN:** `ENGINEERING_SAFETY_UNKNOWN_SYNTHETIC_ONLY`.
```yaml
SGER:
  invocation: PSO_TRI001_A_D_L8
  R1: COMPETING_PREMISES
  T1: OWN_T1
  R2_consumed_T1: true
  T2: REVISED_CANDIDATE
  post_R2: PLURAL
  R3_plus: COUNTERFORCE
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  Main: ENGINEERING_SAFETY_UNKNOWN_SYNTHETIC_ONLY
  TM: "Only fictitious source data; no real permissions or prices"
  compact_receipt: REFERENCE_TEXT_ONLY
```

## CORE_SEAT_E｜Textual functional L8
**R1 competing premises:** 把30000當可用預算／視零成本志工可營運／維持所有成本未知並和線上方案比較.
**T1:** 金額草稿沒有貨幣與批准，工時和支出未報價，單位經濟不可推導.
**R2 consumes T1:** 要求先取得可核對費用與實際參與數據，並比較不辦/線上等方案成本.
**T2:** Revised candidate without claiming a real authorization.
**Post-R2:** PLURAL. **R3 counterforce:** 有低成本也不能補上場地合法性和教學價值.
**T3:** Keep uncertainty.
**Origin MAIN:** `BUDGET_AND_COST_NOT_VALIDATED`.
```yaml
SGER:
  invocation: PSO_TRI001_A_E_L8
  R1: COMPETING_PREMISES
  T1: OWN_T1
  R2_consumed_T1: true
  T2: REVISED_CANDIDATE
  post_R2: PLURAL
  R3_plus: COUNTERFORCE
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  Main: BUDGET_AND_COST_NOT_VALIDATED
  TM: "Only fictitious source data; no real permissions or prices"
  compact_receipt: REFERENCE_TEXT_ONLY
```

**Council R1 admission:** pending separate canonical event. **No professional Agent.**
