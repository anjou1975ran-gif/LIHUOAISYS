# R005 Material L8｜N1 consumes newly found procurement outcomes
**Origin:** CORE_SEAT_N1 / SAME_MODEL_MULTI_ROLE_REFERENCE.
**Clock A:** `METHOD/EV_R005_A0_N1_NEW_EVIDENCE_METHOD_SCREEN.md` committed → `OBSERVATION/EV_R005_A1_N1_NEW_BUYER_FIRST_LOOK.md` committed → THIS L8.
**New public evidence source:** `SOURCE/R005_ADDITIONAL_PURCHASERS_AND_PUBLIC_AWARD_LISTING.md`, not part of R004 initial knowledge. R004 initial stance preserved.

## R1 Candidate competition
- R1-1: 看到『中標結果公告』就當公司付費成功（後知偷升格）
- R1-2: 看到『控制價 40.8萬』就當已成交價格（不成立）
- R1-3: 將採購公告、結果索引、得標正文、實際付款、利潤分成不同證據階級
**T1:** 官網存在 2026-02-04 的中標公告條目，比『只有招標公告』往前一步；但未讀得標全文，不能聲稱 award details。
**O9 R1:** Functional textual comparison, no hidden-state claim.
## R2 consumes T1
保持買家先行的立場，將政府採購的證據階梯更新：`TENDER_POSTED→AWARD_RESULT_LISTED→WINNER_AND_BID_DETAILS_VERIFIED→CONTRACT_ACCEPTED→CASH_RECEIVED→PROFITABILITY_VERIFIED`。目前僅前兩層可核對。水務集團也確有公開調查採購與結果索引，但入場先前業績條件可能阻止創業公司投標。
**T2:** 新來源支持『真實採購行為存在』的證據強度增加，**不支持**本公司已拿到客戶或現有服務商可被替代。
**Post R2 premise audit:** PLURAL, counterexample remains.
## R3 surviving counterforce
政府和公營事業付費的存在可能令人高估容易得標，尤其既有供應商業績與項目人力門檻；若無實際痛點和入口資格，就不應作投資前提。
**T3:** No full procurement award source, rights, market approval or profit promotion.

## Origin Object
```yaml
event: CI3-E-R005-A2-N1
origin: CORE_SEAT_N1
type: POSITION_RETAINED_WITH_MATERIAL_EVIDENCE_UPDATE
main: "BUYER_CONTRACT_EVIDENCE_LADDER_EXPANDED"
stance: "BUYER_FIRST_MAINTAINED_GOV_AND_UTILITY_PURCHASE_ACTIVITIES_GROUNDED_WITH_LIMITS"
objection: "未見中標正文/真收款/公司投標資格"
formal_qualification: NOT_CLAIMED
external_specialist_return: NONE
```
## SGER + Compact Receipt
```yaml
cycle: CI3-L8-R005-N1
R1: CANDIDATE_COMPETITION
T1: CI3-R005-N1-T1
R2_consumes_T1: true
T2: CI3-R005-N1-T2
Post_R2_Premise_Audit: PLURAL
R3_plus: R3
T3: CI3-R005-N1-T3
O9: [R1,R2,R3]
I9: NOT_TRIGGERED
MAIN: CI3-R005-N1-MAIN
TM: "Contract result listing not a receipt or profit; legal authorization not inferred"
VerticalAcceptance: REFERENCE_CONDITIONAL
ExecutionIdentity: SAME_MODEL_MULTI_ROLE_REFERENCE
```
