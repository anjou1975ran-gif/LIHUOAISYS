# CR-R005 B Material Re-Wake｜重新形成比較性 P2 候選
**Cycle:** SH-CI-REENTRY-B-R005-L8-003
**Origin:** CORE_SEAT_B / PROPOSAL_CANDIDATE_ORIGIN; not Secretary.
**Input:** CR-EV-050 D (different engineering workflows), CR-EV-053 E (cost/recovery), CR-EV-054/055 N1 (two buyers and no WTP), original B R003.
**Prior B position:** rights-scoped kernel could support different products; no model winner.

## R1 possible directions
- B5-1 Buyer-private supplier evidence wins: less resale pressure, BUT onboarding/integration and buyer contractual authority unknown.
- B5-2 Authorized storefront execution verification wins: concrete per-visit price, BUT route-density/permissions/marginal visit cost may prevent recovery.
- B5-3 Retain legacy P1 retail price/stock alert: earlier design, BUT no confirmed buyer, legal feed or unique value.
- B5-4 Pure generic provenance platform: reusable, BUT likely a tool looking for an accountable payer.

### SAC O9 R1 and T1
- Bright: B5-1 because 'software-first' is familiar; dark: procurement contract and enterprise sales cost.
- I9 NOT_TRIGGERED.
- T1 SH-CI-B-R005-T1: other seats' material findings deny the basis for a one-route conclusion; avoid fake synthesis.

## R2 consumes T1
B originates **P2 / Shenzhen Evidence Business-Model Comparison**, with three substantially different revenue/source relationships:
(1) VC-FIELD permitted store execution audits;
(2) VC-BUYER private quote–promise–receipt evidence;
(3) VC-P1 licensed retail price/stock alerts.
Shared rights-scoped **software components**, not automatically pooled customer data. **No commercial winner chosen**. This is a `PROPOSAL_CANDIDATE / UNQUALIFIED_CANDIDATE`, not Council approval.

### SAC O9 R2 and T2
- Bright: compare actual buyer job, permitted sources, contribution and recovery; dark: none of them has WTP proof.
- T2 SH-CI-B-R005-T2: material business model, customer, source, architecture, execution and capital changes relative to P1.

## Post-R2 premise audit / R3
- MULTIPLE_MATERIAL_PREMISE_FAMILIES; P1 low-CAPEX price-alert story too narrow.
- R3 REQUIRED: Make sure resold retail data, private procurement evidence, and authorized onsite execution are not treated as the same product merely because they use common source passports.
- R3 outcome: three candidates survive, neither winning by default nor mandated to differ from P1. O9 R3 keeps counterarguments.
- T3 SH-CI-B-R005-T3: scoped comparative P2 candidate, no forced R4.

## MAIN / origin-declared semantic object
```yaml
MAIN: SH-CI-B-R005-MAIN
origin: CORE_SEAT_B
semantic_type: PROPOSAL_CANDIDATE
ref: P2_SHENZHEN_EVIDENCE_BUSINESS_MODEL
standing: UNQUALIFIED_CANDIDATE
options: [VC-FIELD,VC-BUYER,VC-P1]
material_deltas: [CITY_SCOPE,BUYER_JOB,SOURCE_RIGHTS,BUSINESS_MODEL,ARCHITECTURE,EXECUTION_SEQUENCE,CAPITAL_RECOVERY,KILL_CONDITIONS]
affected_seats: [N1,A,B,C,D,E]
no_winner_preselected: true
```
Post-Main: ROUTE to all material seats; TM SH-CI-B-R005-TM no observed reclassification drift; Vertical acceptance source-scoped only.
```yaml
STRUCTURED_GENERATION_EVIDENCE_RECORD_V1_3_1:
  cycle_ref: SH-CI-REENTRY-B-R005-L8-003
  R1: {state: RECEIVED, paths: [B5-1,B5-2,B5-3,B5-4]}
  T1: {state: RECEIVED, ref: SH-CI-B-R005-T1}
  R2: {state: RECEIVED, consumes_T1: SH-CI-B-R005-T1}
  T2: {state: RECEIVED, ref: SH-CI-B-R005-T2}
  post_R2_premise_audit: {state: COMPLETE, plurality: MULTIPLE_MATERIAL_PREMISE_FAMILIES}
  R3_plus: {requirement: REQUIRED, rounds: [R3], ref: SH-CI-B-R005-T3}
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  main_return: P2_UNQUALIFIED_CANDIDATE
  manifestation: PROPOSAL_CANDIDATE_BY_B
  TM: {state: RECEIVED, drift: NONE_DETECTED}
  release: ROUTE_ALL_AFFECTED_SEATS_NOT_APPROVAL
  persistence: GIT_FILE_AFTER_VERIFICATION
  provider_receipt: NONE
```
**Compact L8 Receipt:** R1/T1, R2 consumes T1/T2, premise audit/R3/T3, MAIN/TM/SGER documented, no formal proposal approval.