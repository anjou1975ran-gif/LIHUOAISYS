# E-A2-C｜Initial Material L8 + SGER + Compact Receipt
**Origin:** CORE_SEAT_C; Execution `SAME_MODEL_MULTI_ROLE_REFERENCE`; not independent.
**Temporal chain:** `METHOD/E_A0_C_PRE_L8_METHOD_DECISION.md` → `SOURCE/METHOD_FETCH_AND_PUBLIC_EVIDENCE_RECEIPT.md` where selected → `OBSERVATION/E_A1_C_FIRST_OBSERVATION.md` → THIS material judgment. Other seats' current stances not deliberately supplied as initial pass.
**Invocation ID:** CI3-L8-C-R001; Council Round R001 != L8 R1/R2/R3+.

## R1｜Competing premise families
- **C-P1:** 公開可見資料→可自由轉售：拒絕
- **C-P2:** 有權企業對第三方委外核查→仍需看 NDA/目的/委外合約
- **C-P3:** 深圳數據交易規範→適用場域與交易標的須逐案確定，不能對所有核查服務一律套數據交易所流程
**R1 O9:** Identify where tempting shortcut loses rights/payments/quality; textual functional observation, not hidden-state proof.
**T1:** 權利不是商品附屬品質標籤；F1 現場拍攝、F2 自願發布與向多買方再用、F3 客戶私有委外各自牽涉不同主體、目的、接收者和保存期限。

## R2｜Consumes T1 and re-competes
提出每個研究案前必填的 `R0-R4` 權利/用途條件：R0 來源; R1 取得合法性; R2 特定委外/加工目的; R3 交付對象; R4 重用/撤回；每項若缺，商業化相關交付 HOLD。但研究公開競品及合成流程無需假裝先拿到實際資料權。
**R2 T1 consumption:** explicit: handles the first round's weakness instead of merely continuing initial candidate.
**R2 O9:** What remains open and what cannot yet be claimed.
**T2:** F3 的委外處理與 F2 的跨客戶 Feed 不同；即使採 B 的共用引擎，也只能共享軟體，不自動共享數據。

## Post-R2 premise audit
`PLURAL_MATERIAL_PREMISES`. One more internal R3 is required for surviving counterforce. This is NOT a second Council Round.

## R3+｜Counterpremise
公開官方規章不構成實際法律意見；目前沒有合約文本與當地專業審查，不能宣稱某方案依法全面可行或無需批准。
**T3:** Preserve surviving material objection and avoid false commercial qualification.

## Origin-declared typed Council objects
```yaml
origin_event: CI3-E-A2-C
origin_actor: CORE_SEAT_C
main_type: "QUALIFICATION_OBJECTION_AND_LEGAL_HOLD"
main: "DATA_RIGHTS_SCOPE_GATES"
owned_stance: "CONCEPT_RESEARCH_ALLOWED_REAL_DATA_REUSE_AND_DEPLOYMENT_HOLD"
pre_method_ref: CI3-E-A0-C
first_observation_ref: CI3-E-A1-C
professional_support_decision: "無真實交易事實，不請律師給假設性個案正式意見"
real_customer_evidence: NONE
material_risk_status: UNVERIFIED
```

## SGER / Compact L8 Receipt
```yaml
SGER:
  cycle_ref: CI3-L8-C-R001
  R1: COMPETING_PREMISES
  O9: [R1,R2,R3]
  T1: CI3-C-T1
  R2_consumes_T1: true
  T2: CI3-C-T2
  post_R2_premise_audit: PLURAL
  R3_plus: [R3]
  T3: CI3-C-T3
  Main: CI3-C-MAIN
  TM: "Seat judgement stays within unvalidated research not real market facts"
  I9: NOT_TRIGGERED
  vertical_acceptance: CONDITIONAL_REFERENCE_MATERIAL_JUDGMENT
  provider: SAME_MODEL_MULTI_ROLE_REFERENCE
  source_rights_verification: NOT_DONE_REAL_TRANSACTION
```
**Compact:** SEAT_WAKE→R1/T1→R2/T2→PremiseAudit→R3/T3→MAIN/TM/SGER→conditional Council Admission. No external specialist, cost quote, or host execution.
