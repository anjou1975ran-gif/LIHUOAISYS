# R005 Material L8｜E consumes newly found procurement outcomes
**Origin:** CORE_SEAT_E / SAME_MODEL_MULTI_ROLE_REFERENCE.
**Clock A:** `METHOD/EV_R005_A0_E_NEW_EVIDENCE_METHOD_SCREEN.md` committed → `OBSERVATION/EV_R005_A1_E_NEW_BUYER_FIRST_LOOK.md` committed → THIS L8.
**New public evidence source:** `SOURCE/R005_ADDITIONAL_PURCHASERS_AND_PUBLIC_AWARD_LISTING.md`, not part of R004 initial knowledge. R004 initial stance preserved.

## R1 Candidate competition
- R1-1: 採購控制價作收入（不能由公告推得）
- R1-2: 拿兩個控制價直接比較不同服務毛利（不同工期、人力、資格）
- R1-3: 把資格/人力/取得客戶成本列作獨立成立條件，沒有真實收支暫 HOLD
**T1:** 水務採購 40.8 萬控制價、180 天交付、過往 20 萬相關項目要求，與金融辦 30 萬最高投標、四人團隊外加負責人等負擔不能同尺比較。
**O9 R1:** Functional textual comparison, no hidden-state claim.
## R2 consumes T1
新增 `PROCUREMENT_ENTRY_COST_GATE`：`eligibility/prior_contracts`, `bid preparation`, `delivery workdays`, `on-site staffing`, `sampling quality`, `data lawful access`, `payment/acceptance`. 設兩個成本表而非一個『政府情報平均毛利』模型。未取可驗的人力/成交/履約資訊時維持成本資格 HOLD。
**T2:** 兩個官方採購需求支持市場『有買家類別』，但也同時支持『新供應商有進場門檻與完整交付成本』反證，決不可用高控制價掩蓋履約成本。
**Post R2 premise audit:** PLURAL, counterexample remains.
## R3 surviving counterforce
如既有高資歷調查商更有競爭優勢、標案不接受聯合體，新公司可能比私企買方更難切入；須實測而非否定一切。
**T3:** No full procurement award source, rights, market approval or profit promotion.

## Origin Object
```yaml
event: CI3-E-R005-A2-E
origin: CORE_SEAT_E
type: MATERIAL_COST_GATES_REFINED
main: "TWO_CONTRACT_TYPE_ENTRY_COST_AND_UNIT_ECONOMICS_GATES"
stance: "GOV_AND_UTILITY_FEASIBILITY_UNPROVEN_DESPITE_PUBLIC_CONTROL_PRICES"
objection: "得標金額/人力費/利潤/實際銷售資格均未知"
formal_qualification: NOT_CLAIMED
external_specialist_return: NONE
```
## SGER + Compact Receipt
```yaml
cycle: CI3-L8-R005-E
R1: CANDIDATE_COMPETITION
T1: CI3-R005-E-T1
R2_consumes_T1: true
T2: CI3-R005-E-T2
Post_R2_Premise_Audit: PLURAL
R3_plus: R3
T3: CI3-R005-E-T3
O9: [R1,R2,R3]
I9: NOT_TRIGGERED
MAIN: CI3-R005-E-MAIN
TM: "Contract result listing not a receipt or profit; legal authorization not inferred"
VerticalAcceptance: REFERENCE_CONDITIONAL
ExecutionIdentity: SAME_MODEL_MULTI_ROLE_REFERENCE
```
