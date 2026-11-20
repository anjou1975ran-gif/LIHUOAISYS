# E-A2-E｜Initial Material L8 + SGER + Compact Receipt
**Origin:** CORE_SEAT_E; Execution `SAME_MODEL_MULTI_ROLE_REFERENCE`; not independent.
**Temporal chain:** `METHOD/E_A0_E_PRE_L8_METHOD_DECISION.md` → `SOURCE/METHOD_FETCH_AND_PUBLIC_EVIDENCE_RECEIPT.md` where selected → `OBSERVATION/E_A1_E_FIRST_OBSERVATION.md` → THIS material judgment. Other seats' current stances not deliberately supplied as initial pass.
**Invocation ID:** CI3-L8-E-R001; Council Round R001 != L8 R1/R2/R3+.

## R1｜Competing premise families
- **E-P1:** F1 按次售價高→人工、交通和二次查核可能吃掉毛利
- **E-P2:** F2 低成本資料可反覆賣→授權/更新/失效與買方訂閱獲客成本未知
- **E-P3:** F3 SaaS 月費高→客製導入、資安隔離和銷售回收期高
- **E-P4:** 只要差異化就一定能收高價→顧客替代方案限制上限
**R1 O9:** Identify where tempting shortcut loses rights/payments/quality; textual functional observation, not hidden-state proof.
**T1:** 必須以同一收費成果和相同期間算每條路的實收貢獻、重驗及留存；不能用不相同單位的演示價格排出先後。

## R2｜Consumes T1 and re-competes
給出可否定研究門檻而非假數字：F1 找每任務完工/二次核對時間與合法成本；F2 看可授權且持續更新來源比例、重核費/續約費；F3 看單企業導入工時、例外核查平均成本與付款周期。先驗收哪種痛點有收入，再估固定成本與擴張，保留三線作可比較性。
**R2 T1 consumption:** explicit: handles the first round's weakness instead of merely continuing initial candidate.
**R2 O9:** What remains open and what cannot yet be claimed.
**T2:** 在市場價未知時，只能判斷 F2 有雙邊冷啟動/授權與信任同時成立的多重門檻，F1 實體變動成本高，F3 大客導入/保密成本高；這些是風險構型不是定量優劣。

## Post-R2 premise audit
`PLURAL_MATERIAL_PREMISES`. One more internal R3 is required for surviving counterforce. This is NOT a second Council Round.

## R3+｜Counterpremise
F4 例外服務也不天然輕資本：要是每個驗證都需人工調查，付費額可能低於跨企業查證成本；白標要付渠道分成、整合及法律成本。
**T3:** Preserve surviving material objection and avoid false commercial qualification.

## Origin-declared typed Council objects
```yaml
origin_event: CI3-E-A2-E
origin_actor: CORE_SEAT_E
main_type: "COST_CONDITIONAL_OBJECTION"
main: "F1_F2_F3_F4_UNIT_ECONOMIC_KILL_TESTS"
owned_stance: "NO_COMMERCIAL_WINNER_UNTIL_PAID_UNIT_COSTS_AND_RIGHTS"
pre_method_ref: CI3-E-A0-E
first_observation_ref: CI3-E-A1-E
professional_support_decision: "未有能供經濟專家得出可靠深圳實價的資料，現在無需外援"
real_customer_evidence: NONE
material_risk_status: UNVERIFIED
```

## SGER / Compact L8 Receipt
```yaml
SGER:
  cycle_ref: CI3-L8-E-R001
  R1: COMPETING_PREMISES
  O9: [R1,R2,R3]
  T1: CI3-E-T1
  R2_consumes_T1: true
  T2: CI3-E-T2
  post_R2_premise_audit: PLURAL
  R3_plus: [R3]
  T3: CI3-E-T3
  Main: CI3-E-MAIN
  TM: "Seat judgement stays within unvalidated research not real market facts"
  I9: NOT_TRIGGERED
  vertical_acceptance: CONDITIONAL_REFERENCE_MATERIAL_JUDGMENT
  provider: SAME_MODEL_MULTI_ROLE_REFERENCE
  source_rights_verification: NOT_DONE_REAL_TRANSACTION
```
**Compact:** SEAT_WAKE→R1/T1→R2/T2→PremiseAudit→R3/T3→MAIN/TM/SGER→conditional Council Admission. No external specialist, cost quote, or host execution.
