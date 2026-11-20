# R004 Material L8｜CORE_SEAT_B
**Invocation:** CI3-L8-R004-B; **Origin:** CORE_SEAT_B; **identity:** SAME_MODEL_MULTI_ROLE_REFERENCE.
**Council Round R004 != internal L8 R1/R2/R3+.**
**Actual Clock A:** `METHOD/EV_R004_A0_B_NEW_ISSUE_METHOD_DECISION.md` committed → selected Pack source receipt → `OBSERVATION/EV_R004_A1_B_NEW_BUYER_FIRST_OBSERVATION.md` committed → THIS L8.
**Prior seat state R001–R003 unchanged:** CI3-P1 B-origin staged research of F3 SRM and F1 store inspection before platform, F2 rights conditional

## L8 R1｜Competing initial premises
- P1: 以產品 F1/F2/F3 作研究目錄→仍忽略誰控制錢與權力
- P2: 政府有採購公告就先轉型政府民調公司→誤把使用者示例當最後方案
- P3: 建立單一『金流→權力→情報』線性箭頭→忽略資訊主體/服務商/決策者彼此不同
- P4: 每個場景建立付款/採購、資訊取得/使用、行動/驗收三條相交但不等同的流程
**R1 O9:** discriminate factual source vs extrapolation, not claim microscopic model state.
**T1:** 政府公告提供首次具體第三方買方：付款預算主體、服務範圍、交付監督與採購資格均明示，與已有政府的市民訴求平台不同。『買一份市民意見』的商品描述太粗，實際採購帶有運作服務責任。

## L8 R2｜Consumes T1
對 B 自身 P1 作版本化修正，起源 `CI3-P2_BUYER_FLOW_FIRST_RESEARCH`：從買方決策任務與資金/授權/資訊圖出發，保留 F1/F2/F3 與新 F5 為**待映射的交付機制**而非產品勝者；先以深圳 GOV 公告作一個有預算/資格的標本，另用品牌/採購企業與物管/協會作未知對照。每張 flow map 至少標注 `BUDGET_OWNER → PROCUREMENT_AUTHORITY → CONTRACTOR_RIGHTS → SOURCE_CONSENT_OR_LEGAL_BASIS → VERIFIER → DECISION_OWNER → ACCEPTANCE/REMEDY → PAYMENT/COST`。政府部門有法定權力不等於能轉讓給受託商。
**R2 O9:** acknowledges material objection, not forced agreement.
**T2:** 原 P1 的『先以 F3/F1 做產品差異反證』並非被刪除，而是現在作為 P2 下游一條測試；新的第一步是先辨識買方及其權力/付費因果，再決定研究哪種核查/分析服務。

## Post-R2 plurality check
`MULTIPLE_MATERIAL_PREMISES`; C's rights, E's costs and N1's buyer constraints not forcibly settled; R3 required.

## L8 R3｜Surviving counterforce
反例：Flow map 可能畫得精美卻仍找不到真正買方；政府預算可能為現場人力外包而非高毛利資料產品；如果市場實際需求仍不存在，新架構同樣得被淘汰。三種 flow 也不能混同政治影響、法律行政決定或私人的資料所有權。
**T3:** Evidence/authority status remains limited.

## Origin-declared object, not Secretary thesis
```yaml
event_id: CI3-E-R004-A2-B
origin_actor: CORE_SEAT_B
semantic_type: VERSIONED_RECOMMENDATION_REVISION_FROM_B_P1
main: "CI3-P2_BUYER_FLOW_FIRST_RESEARCH"
previous_stance: "CI3-P1 B-origin staged research of F3 SRM and F1 store inspection before platform, F2 rights conditional"
new_stance: "PRIORITIZE_CUSTOMER_DECISION_AND_MONEY_AUTHORITY_INFORMATION_FLOWS_BEFORE_PRODUCTS"
surviving_objection: "Flow maps and public bids do not prove unit economics, procurement eligibility or buyer willingness-to-pay"
human_direction_is_not_preselected_answer: true
actual_professional_agent_return: NONE
```
## SGER / Compact L8 Receipt
```yaml
SGER:
  invocation: CI3-L8-R004-B
  R1: PLURAL_COMPETING_PREMISES
  T1: CI3-R004-B-T1
  R2_consumes_T1: true
  T2: CI3-R004-B-T2
  premise_audit: MULTIPLE
  R3_plus: R3
  T3: CI3-R004-B-T3
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  MAIN: CI3-R004-B-MAIN
  TM: "Human offers direction not predetermined answer; public evidence does not prove award, qualification, margins"
  VerticalAcceptance: CONDITIONAL_REFERENCE
  ExecutionIdentity: SAME_MODEL_MULTI_ROLE_REFERENCE
  external_expert: NONE
```
**Receipt:** SEAT WAKE → R1/T1 → R2/T2 → premise check → R3/T3 → Main/TM/SGER → Council admission pending.
