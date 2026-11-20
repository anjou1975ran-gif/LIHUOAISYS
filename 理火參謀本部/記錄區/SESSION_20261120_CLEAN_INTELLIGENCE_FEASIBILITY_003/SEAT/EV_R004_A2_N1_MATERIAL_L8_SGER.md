# R004 Material L8｜CORE_SEAT_N1
**Invocation:** CI3-L8-R004-N1; **Origin:** CORE_SEAT_N1; **identity:** SAME_MODEL_MULTI_ROLE_REFERENCE.
**Council Round R004 != internal L8 R1/R2/R3+.**
**Actual Clock A:** `METHOD/EV_R004_A0_N1_NEW_ISSUE_METHOD_DECISION.md` committed → selected Pack source receipt → `OBSERVATION/EV_R004_A1_N1_NEW_BUYER_FIRST_OBSERVATION.md` committed → THIS L8.
**Prior seat state R001–R003 unchanged:** Only validate identifiable company/brand paying buyer before product winner; no actual buyer

## L8 R1｜Competing initial premises
- P1: 市府公開採購=地方政府肯定會買我們的情報 (REJECT OVERGENERALIZATION)
- P2: 市府自有民意管道=不需任何第三方 (REJECT OVERGENERALIZATION)
- P3: 一份明確政府採購標的可作政府部門有預算的個案，但本公司供應能力與獲利仍須證明
**R1 O9:** discriminate factual source vs extrapolation, not claim microscopic model state.
**T1:** 採購公告列出人員、現場回應與資格要求，這不是只買少量原始意見；與先前 F1/F3 實際服務差別不小。

## L8 R2｜Consumes T1
維持原本的 BUYER_BUDGET_FIRST 原則，但**新增實質證據等級**：政府官網的採購需求公告為『某機關曾嘗試向外部採購民意工單分析與輔助』，不等於實際承包/付清/本公司可做。政府與企業都要從決策/預算 owner 的未滿足問題開始。
**R2 O9:** acknowledges material objection, not forced agreement.
**T2:** 區分『有採購公告』『採購已成約』『承包有利潤』『同類政府會購買』四個互不能倒推的層次。

## Post-R2 plurality check
`MULTIPLE_MATERIAL_PREMISES`; C's rights, E's costs and N1's buyer constraints not forcibly settled; R3 required.

## L8 R3｜Surviving counterforce
既有政府持續接收意見且可能有統計中心，第三方沒有補充增量時，賣報告甚至不值得採購。人類提方向不等於已證市場。
**T3:** Evidence/authority status remains limited.

## Origin-declared object, not Secretary thesis
```yaml
event_id: CI3-E-R004-A2-N1
origin_actor: CORE_SEAT_N1
semantic_type: POSITION_RETAINED_WITH_NEW_SOURCE_QUALIFICATION
main: "BUYER_EVIDENCE_LADDER_PUBLIC_SECTOR_INSTANCE"
previous_stance: "Only validate identifiable company/brand paying buyer before product winner; no actual buyer"
new_stance: "RETAIN_BUYER_BUDGET_FIRST_WITH_GOV_PURCHASER_AS_DOCUMENTED_INSTANCE_NOT_WINNER"
surviving_objection: "沒有獲標、報價/成本、額外購買意願或履約能力證據"
human_direction_is_not_preselected_answer: true
actual_professional_agent_return: NONE
```
## SGER / Compact L8 Receipt
```yaml
SGER:
  invocation: CI3-L8-R004-N1
  R1: PLURAL_COMPETING_PREMISES
  T1: CI3-R004-N1-T1
  R2_consumes_T1: true
  T2: CI3-R004-N1-T2
  premise_audit: MULTIPLE
  R3_plus: R3
  T3: CI3-R004-N1-T3
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  MAIN: CI3-R004-N1-MAIN
  TM: "Human offers direction not predetermined answer; public evidence does not prove award, qualification, margins"
  VerticalAcceptance: CONDITIONAL_REFERENCE
  ExecutionIdentity: SAME_MODEL_MULTI_ROLE_REFERENCE
  external_expert: NONE
```
**Receipt:** SEAT WAKE → R1/T1 → R2/T2 → premise check → R3/T3 → Main/TM/SGER → Council admission pending.
