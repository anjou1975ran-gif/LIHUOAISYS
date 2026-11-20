# R004 Material L8｜CORE_SEAT_C
**Invocation:** CI3-L8-R004-C; **Origin:** CORE_SEAT_C; **identity:** SAME_MODEL_MULTI_ROLE_REFERENCE.
**Council Round R004 != internal L8 R1/R2/R3+.**
**Actual Clock A:** `METHOD/EV_R004_A0_C_NEW_ISSUE_METHOD_DECISION.md` committed → selected Pack source receipt → `OBSERVATION/EV_R004_A1_C_NEW_BUYER_FIRST_OBSERVATION.md` committed → THIS L8.
**Prior seat state R001–R003 unchanged:** R0-R4 source/purpose/recipient/reuse rights from commercial data; no real transaction legal clearance

## L8 R1｜Competing initial premises
- P1: 政府花錢=資料與市民的意見可轉售 (REJECT)
- P2: 政府有採購權=可以把行政決定或政治影響力外包 (REJECT)
- P3: 地方政府可以依法委託特定輔助服務、公開意見分析，但保留決策責任、採購競爭、公眾資料/代表性與反對意見保護
- P4: 公部門與企業都用同一統計/隱私規則 (REJECT: scope varies)
**R1 O9:** discriminate factual source vs extrapolation, not claim microscopic model state.
**T1:** 深圳決策程序要求正當公眾參與方式、科學問卷及客觀記錄反對意見；政府委外公告具採購資格、人員與保密要求。沒有哪條允許新公司任意攫取 @深圳-民意速辦 的個案工單或建立個人政治態度資料產品。

## L8 R2｜Consumes T1
新增 `GOV-C0..C6` 資格鏈：C0 具體政府採購標的/預算權, C1 招標規則/供應商資格, C2 正當取得與委外合約, C3 個資及居民保密, C4 調查樣本/缺失/反對意見的客觀呈現, C5 報告用途與決策權不被買賣, C6 修改/撤回/監督及保留期限。公開案頭研究准入；真實民意收集和委外工單處理法律准出 HOLD。
**R2 O9:** acknowledges material objection, not forced agreement.
**T2:** 公部門是不同授權制度的買方，不是私人情報權力池；資訊可以是有權評估的服務成果，公權力只能依法律由有權機關行使。

## Post-R2 plurality check
`MULTIPLE_MATERIAL_PREMISES`; C's rights, E's costs and N1's buyer constraints not forcibly settled; R3 required.

## L8 R3｜Surviving counterforce
即使有正式採購也仍需公司資格、合約、資安與統計/民調研究倫理；使用一般官方規範不能替代本案司法、當地專業或真實取得資料權。
**T3:** Evidence/authority status remains limited.

## Origin-declared object, not Secretary thesis
```yaml
event_id: CI3-E-R004-A2-C
origin_actor: CORE_SEAT_C
semantic_type: NEW_QUALIFICATION_BOUNDARY_WITH_LEGAL_HOLD
main: "GOVERNMENT_DATA_PROCUREMENT_AND_REPRESENTATIVENESS_HOLD"
previous_stance: "R0-R4 source/purpose/recipient/reuse rights from commercial data; no real transaction legal clearance"
new_stance: "PUBLIC_PROCUREMENT_DESK_RESEARCH_ALLOWED_REAL_CITIZEN_DATA_AND_ENGAGEMENT_HOLD"
surviving_objection: "缺合約、具體法域/政策適用分析、統計代表性證據與實際資料權"
human_direction_is_not_preselected_answer: true
actual_professional_agent_return: NONE
```
## SGER / Compact L8 Receipt
```yaml
SGER:
  invocation: CI3-L8-R004-C
  R1: PLURAL_COMPETING_PREMISES
  T1: CI3-R004-C-T1
  R2_consumes_T1: true
  T2: CI3-R004-C-T2
  premise_audit: MULTIPLE
  R3_plus: R3
  T3: CI3-R004-C-T3
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  MAIN: CI3-R004-C-MAIN
  TM: "Human offers direction not predetermined answer; public evidence does not prove award, qualification, margins"
  VerticalAcceptance: CONDITIONAL_REFERENCE
  ExecutionIdentity: SAME_MODEL_MULTI_ROLE_REFERENCE
  external_expert: NONE
```
**Receipt:** SEAT WAKE → R1/T1 → R2/T2 → premise check → R3/T3 → Main/TM/SGER → Council admission pending.
