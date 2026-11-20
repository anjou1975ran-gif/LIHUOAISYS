# E-A2-N1｜Initial Material L8 + SGER + Compact Receipt
**Origin:** CORE_SEAT_N1; Execution `SAME_MODEL_MULTI_ROLE_REFERENCE`; not independent.
**Temporal chain:** `METHOD/E_A0_N1_PRE_L8_METHOD_DECISION.md` → `SOURCE/METHOD_FETCH_AND_PUBLIC_EVIDENCE_RECEIPT.md` where selected → `OBSERVATION/E_A1_N1_FIRST_OBSERVATION.md` → THIS material judgment. Other seats' current stances not deliberately supplied as initial pass.
**Invocation ID:** CI3-L8-N1-R001; Council Round R001 != L8 R1/R2/R3+.

## R1｜Competing premise families
- **N1-P1:** 企業已經在付巡檢與 SRM 費→仍可能願意再購核驗
- **N1-P2:** 只要情報品質更好→不代表有人有新增預算
- **N1-P3:** 找一個造成具體損失、又無法由現有服務有效解決的例外→才可討論付費
**R1 O9:** Identify where tempting shortcut loses rights/payments/quality; textual functional observation, not hidden-state proof.
**T1:** 既有系統功能不缺表示『有競爭者』和『未解決痛點』並非同義；新公司的技術優越不等於新增預算。

## R2｜Consumes T1 and re-competes
將研究起點由做三個產品，修正成逐條尋找一個具名 budget owner 會為何種損失/延誤/爭議多付錢。所有現有供應商已解問題都應視作明示反證，不因本計畫是理火就自動有溢價。
**R2 T1 consumption:** explicit: handles the first round's weakness instead of merely continuing initial candidate.
**R2 O9:** What remains open and what cannot yet be claimed.
**T2:** 需要一張『買方目前怎麼辦？出錯的金錢/時間代價？誰有權付款？』的否定式調查清單，而不是抽象市場規模。

## Post-R2 premise audit
`PLURAL_MATERIAL_PREMISES`. One more internal R3 is required for surviving counterforce. This is NOT a second Council Round.

## R3+｜Counterpremise
即便具名企業說有痛點，也可能不願意改流程；沒有正式付款或採購紀錄時，不能宣稱顧客驗證。
**T3:** Preserve surviving material objection and avoid false commercial qualification.

## Origin-declared typed Council objects
```yaml
origin_event: CI3-E-A2-N1
origin_actor: CORE_SEAT_N1
main_type: "BUYER_REALITY_OBJECTION"
main: "BUYER_BUDGET_FIRST_NEGATIVE_TEST"
owned_stance: "HOLD_THREE_COMMERCIAL_WINNERS_UNTIL_PAYING_PROBLEM_IDENTIFIED"
pre_method_ref: CI3-E-A0-N1
first_observation_ref: CI3-E-A1-N1
professional_support_decision: "沒有具名買家實價；未到外部專家可直接解決的階段"
real_customer_evidence: NONE
material_risk_status: UNVERIFIED
```

## SGER / Compact L8 Receipt
```yaml
SGER:
  cycle_ref: CI3-L8-N1-R001
  R1: COMPETING_PREMISES
  O9: [R1,R2,R3]
  T1: CI3-N1-T1
  R2_consumes_T1: true
  T2: CI3-N1-T2
  post_R2_premise_audit: PLURAL
  R3_plus: [R3]
  T3: CI3-N1-T3
  Main: CI3-N1-MAIN
  TM: "Seat judgement stays within unvalidated research not real market facts"
  I9: NOT_TRIGGERED
  vertical_acceptance: CONDITIONAL_REFERENCE_MATERIAL_JUDGMENT
  provider: SAME_MODEL_MULTI_ROLE_REFERENCE
  source_rights_verification: NOT_DONE_REAL_TRANSACTION
```
**Compact:** SEAT_WAKE→R1/T1→R2/T2→PremiseAudit→R3/T3→MAIN/TM/SGER→conditional Council Admission. No external specialist, cost quote, or host execution.
