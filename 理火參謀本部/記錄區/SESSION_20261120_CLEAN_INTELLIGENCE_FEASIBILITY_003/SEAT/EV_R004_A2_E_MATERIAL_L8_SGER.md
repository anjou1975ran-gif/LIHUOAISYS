# R004 Material L8｜CORE_SEAT_E
**Invocation:** CI3-L8-R004-E; **Origin:** CORE_SEAT_E; **identity:** SAME_MODEL_MULTI_ROLE_REFERENCE.
**Council Round R004 != internal L8 R1/R2/R3+.**
**Actual Clock A:** `METHOD/EV_R004_A0_E_NEW_ISSUE_METHOD_DECISION.md` committed → selected Pack source receipt → `OBSERVATION/EV_R004_A1_E_NEW_BUYER_FIRST_OBSERVATION.md` committed → THIS L8.
**Prior seat state R001–R003 unchanged:** Per-unit contribution must include human repeat verification, client integration, permission cost; no fake prices

## L8 R1｜Competing initial premises
- P1: 政府開公告→必定有高毛利情報需求 (REJECT)
- P2: 超過30萬無效→30萬是成交價格 (REJECT)
- P3: 有政府訂單→一定適合初創 (REJECT)
- P4: 政府採購是有驗收/人員服務/投標風險的不同交易單位；可研究但不預設優於企業市場
**R1 O9:** discriminate factual source vs extrapolation, not claim microscopic model state.
**T1:** 公告的最大投標門檻與不少於四名服務人員加負責人、緊急現場兩小時支援，使『一次性資料出售』錯估成本；不能直接把政府預算當利潤或客單價。

## L8 R2｜Consumes T1
保留先前對 F1/F2/F3 的成本異議，對政府另起 `GOV_UNIT_COST_GATE`：`Revenue=actual collected contract amount after award`, `Costs=staff + on-site response + service QA + confidentiality/security + insurance/contract + procurement preparation + collection / continuity`. 無此成本表與供應商資格證據，F5 不給任何財務可行性判斷。另一種研究方向是小規模政府合法公開資料分析或企業委託聚合報告，但亦需真正買方付費證據，不能宣稱輕資本。
**R2 O9:** acknowledges material objection, not forced agreement.
**T2:** 官方採購是錢存在某個流程的證據，不能跨越採購競爭、交付成本、實際驗收與回款；真正經濟價值應由買方少了什麼成本/錯誤與服務商剩多少貢獻構成。

## Post-R2 plurality check
`MULTIPLE_MATERIAL_PREMISES`; C's rights, E's costs and N1's buyer constraints not forcibly settled; R3 required.

## L8 R3｜Surviving counterforce
如果要求高級專業團隊或大量人工協調，單案可見公告金額可能根本不足支撐，這是可能淘汰政府路線的明確假設，不是已算出虧損。F2 現有低成本平台和 F3 私有服務也各有成本盲點。
**T3:** Evidence/authority status remains limited.

## Origin-declared object, not Secretary thesis
```yaml
event_id: CI3-E-R004-A2-E
origin_actor: CORE_SEAT_E
semantic_type: COST_OBJECTION_AND_PUBLIC_BUYER_UNIT_QUALIFICATION
main: "GOV_BID_BUDGET_VS_DELIVERY_COST_CONFLICT"
previous_stance: "Per-unit contribution must include human repeat verification, client integration, permission cost; no fake prices"
new_stance: "HOLD_GOV_CONTRACT_PROFITABILITY_UNTIL_REAL_COST_AND_AWARD_EVIDENCE"
surviving_objection: "沒有得標價/成本/續約或合理利潤的可驗資料"
human_direction_is_not_preselected_answer: true
actual_professional_agent_return: NONE
```
## SGER / Compact L8 Receipt
```yaml
SGER:
  invocation: CI3-L8-R004-E
  R1: PLURAL_COMPETING_PREMISES
  T1: CI3-R004-E-T1
  R2_consumes_T1: true
  T2: CI3-R004-E-T2
  premise_audit: MULTIPLE
  R3_plus: R3
  T3: CI3-R004-E-T3
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  MAIN: CI3-R004-E-MAIN
  TM: "Human offers direction not predetermined answer; public evidence does not prove award, qualification, margins"
  VerticalAcceptance: CONDITIONAL_REFERENCE
  ExecutionIdentity: SAME_MODEL_MULTI_ROLE_REFERENCE
  external_expert: NONE
```
**Receipt:** SEAT WAKE → R1/T1 → R2/T2 → premise check → R3/T3 → Main/TM/SGER → Council admission pending.
