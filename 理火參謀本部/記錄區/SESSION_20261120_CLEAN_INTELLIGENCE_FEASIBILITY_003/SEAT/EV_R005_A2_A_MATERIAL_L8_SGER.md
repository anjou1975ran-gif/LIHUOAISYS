# R005 Material L8｜A consumes newly found procurement outcomes
**Origin:** CORE_SEAT_A / SAME_MODEL_MULTI_ROLE_REFERENCE.
**Clock A:** `METHOD/EV_R005_A0_A_NEW_EVIDENCE_METHOD_SCREEN.md` committed → `OBSERVATION/EV_R005_A1_A_NEW_BUYER_FIRST_LOOK.md` committed → THIS L8.
**New public evidence source:** `SOURCE/R005_ADDITIONAL_PURCHASERS_AND_PUBLIC_AWARD_LISTING.md`, not part of R004 initial knowledge. R004 initial stance preserved.

## R1 Candidate competition
- R1-1: 地方政府意見調查是一種天然統一的情報產品（否定：不同買方責任）
- R1-2: 公營水務企業客戶滿意度與民意工單可以共用資料庫（否定：不同主體與目的）
- R1-3: 把行政民生工單支援與公營事業客戶服務滿意度調查當兩個不同的候選購買關係
**T1:** 同一份『意見』受機構責任、調查群體、客戶關係、付費目的而變成不同商品，不能因名稱像就合併。
**O9 R1:** Functional textual comparison, no hidden-state claim.
## R2 consumes T1
保留新客群探索，但將先前廣義 F5 政府公共需求候選分岔成 `F5a_GOV_CIVIC_WORKORDER_ANALYSIS` 與 `F5b_PUBLIC_UTILITY_CUSTOMER_SATISFACTION`，兩者分別有真實官方公開採購材料支撐**需求類別存在**，不代表本公司有差異化或資格。其他企業、協會、物管買家仍列 UNKNOWN，可被新增或淘汰，不把兩個資料池共享。
**T2:** 新素材讓買方分類更精確：『公權力決策支援』與『公用事業服務品質改善』是不同需求，付費權限、驗收與代表性標準不同。
**Post R2 premise audit:** PLURAL, counterexample remains.
## R3 surviving counterforce
即使兩種市場有採購，也可能屬傳統問卷/勞務外包、對新進公司門檻高且無可自動化利基；缺乏代表性、選擇性排除反對意見會破壞公眾信任。
**T3:** No full procurement award source, rights, market approval or profit promotion.

## Origin Object
```yaml
event: CI3-E-R005-A2-A
origin: CORE_SEAT_A
type: OWNED_OPTION_SET_REFINEMENT
main: "F5_SPLIT_GOV_WORKORDER_VS_UTILITY_SURVEY"
stance: "KEEP_TWO_BUYER_SEGMENTS_SEPARATE_AS_QUALIFIED_RESEARCH_CANDIDATES"
objection: "客戶差異化、來源權利、採購資格、服務毛利均未證"
formal_qualification: NOT_CLAIMED
external_specialist_return: NONE
```
## SGER + Compact Receipt
```yaml
cycle: CI3-L8-R005-A
R1: CANDIDATE_COMPETITION
T1: CI3-R005-A-T1
R2_consumes_T1: true
T2: CI3-R005-A-T2
Post_R2_Premise_Audit: PLURAL
R3_plus: R3
T3: CI3-R005-A-T3
O9: [R1,R2,R3]
I9: NOT_TRIGGERED
MAIN: CI3-R005-A-MAIN
TM: "Contract result listing not a receipt or profit; legal authorization not inferred"
VerticalAcceptance: REFERENCE_CONDITIONAL
ExecutionIdentity: SAME_MODEL_MULTI_ROLE_REFERENCE
```
