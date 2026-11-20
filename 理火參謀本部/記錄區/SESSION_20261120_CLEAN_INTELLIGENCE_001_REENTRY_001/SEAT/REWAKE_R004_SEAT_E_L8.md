# CR-R004｜E Material Re-Wake after cross-seat effects
**Cycle:** SH-CI-REENTRY-E-R004-L8-002
**Input:** CR-EV-031/032 + CR-EV-040..044 + human no-capital constraint
**Seat responsibility:** E, owned stance not Secretary. Formal qualification blocked pending training-gate resolution.
**No other seat position assumed beyond explicitly cited material.**

## R1 candidates
- **E4-A Choose the cheapest development route** — No direct link to willingness-to-pay, revenue, or future margin.
- **E4-B Compare buyer-private per-account recurring contribution** — Subscription/setup, document verification labor, cloud security and legal overhead.
- **E4-C Compare field-audit per-visit contribution** — visit fee, route density, sample recheck, field payroll and travel.
- **E4-D Compare P1 SaaS annual subscriptions** — licensing cost, account support, churn and customer acquisition.
### O9 R1 / T1
- LAMP_STATE_R1: previously simple P1 price feed or low-cost prototype pulls attention; actual party-specific demand/cost remains shadow.
- I9: NOT_TRIGGERED.
- T1 `SH-CI-E-R004-T1`: No capital ceiling does not imply unconstrained spending; ranking low initial expenditure ahead of payback repeats first-case error. Track cash collected, contribution, utilization and recovery as separate metrics.

## R2 consumes T1
Formalize R=(monthly cash receipts), VC=(per-customer or per-visit direct cash cost), FC=(monthly fixed overhead), CAC, I=(incremental up-front investment). BE subscribers=ceil(FC/(unit price-unit VC)), BE visits=ceil(FC/(visit fee-visit VC)). CAC payback months=CAC/monthly per-customer contribution if positive. Initial investment recovery=I/positive monthly net operating cash flow, excluding debts/taxes in simplistic illustrative model; use staged reinvestment only on verified positive cohorts.
### O9 R2 / T2
- LAMP_STATE_R2: NO_PRESET_CAPITAL / MULTI_ROUTE_COST_RECOVERY_NOT_PROVEN. Missing: No pricing quotes, delivery time, customer CAC, real wage/route density, retention or cash collection.
- T2 `SH-CI-E-R004-T2`: material delta=E rejects old HKD1.8M/90d thesis as invalid for current mandate, forces buyers/ops to prove positive contribution.

## Mandatory Post-R2 Premise Audit
- Status: MULTIPLE_MATERIAL_PREMISE_FAMILIES; existing pricing/engineering assumption not sole coordinate.
- R3 REQUIRED due independent alternative revenue and delivery structures.

## R3+ Cross-Premise
Illustrative NOT QUOTED: buyer workspace P=RMB12k/client-month, direct cost=4k, FC=90k, CAC=30k; BE=12 clients, CAC payback=3.75 months (excluding setup and cash collection); field P=RMB380/visit, VC=RMB260, FC=80k; break-even=667 visits/month, unrealistic if sales route density/permission poor; P1 feed P=RMB8k, VC=3k, FC=100k → 20 active clients. All figures are arbitrary stress-test inputs, not Shenzhen price evidence. For buyer workspace at P=6k, VC=4k, FC=90k → 45 clients; for field P=380, VC=350, FC=80k → 2667 visits. These flip apparent priority; show why price and delivery cost matter more than prefixed budget.
- O9 R3: preserve contrary cost/consent/selection possibilities; I9 NOT_TRIGGERED.
- T3 `SH-CI-E-R004-T3`: NO_PRESET_CAPITAL / MULTI_ROUTE_COST_RECOVERY_NOT_PROVEN; no forced R4 (no further material data).

## Main / Next routing
- Main: **NO_PRESET_CAPITAL / MULTI_ROUTE_COST_RECOVERY_NOT_PROVEN**
- Origin-declared output type: RESOURCE_OBJECTION / COST_MODEL.
- Material targets for reexamination: A, B, N1.
- Surviving gap: No pricing quotes, delivery time, customer CAC, real wage/route density, retention or cash collection.
- Manifestation & TM ref `SH-CI-E-R004-TM`: no detected material reclassification; material risk retained.
- Vertical Acceptance: CONDITIONALLY_ACCEPTED_AS_SEAT_OBJECT; no technical/cost/commercial proof.

```yaml
STRUCTURED_GENERATION_EVIDENCE_RECORD_V1_3_1:
  cycle_ref: SH-CI-REENTRY-E-R004-L8-002
  R1: {state: RECEIVED, candidate_count: 4}
  T1: {state: RECEIVED, ref: SH-CI-E-R004-T1}
  R2: {state: RECEIVED, consumed: SH-CI-E-R004-T1}
  T2: {state: RECEIVED, ref: SH-CI-E-R004-T2}
  post_R2_premise_audit: {state: COMPLETE, plurality: MULTIPLE_MATERIAL_PREMISE_FAMILIES}
  R3_plus: {requirement: REQUIRED, rounds: [R3], ref: SH-CI-E-R004-T3}
  main_return: "NO_PRESET_CAPITAL / MULTI_ROUTE_COST_RECOVERY_NOT_PROVEN"
  O9_lamp_states: [R1,R2,R3]
  I9: NOT_TRIGGERED
  TM: {state: RECEIVED, ref: SH-CI-E-R004-TM, material_drift: NONE_DETECTED}
  release: LIMITED_SEAT_STATEMENT_PENDING_FORMAL_QUALIFICATION
  unresolved: "No pricing quotes, delivery time, customer CAC, real wage/route density, retention or cash collection"
  persistence: GIT_AFTER_VERIFICATION
  external_provider: NONE
```
```text
COMPACT L8 RECEIPT R004-E
R1/T1 RECEIVED; R2 CONSUMED_T1; T2 RECEIVED; POST-R2 PLURALITY
R3/T3 RECEIVED; O9 R1-R3; I9 NOT_TRIGGERED; MAIN/TM/SGER RECEIVED
Seat status = NO_PRESET_CAPITAL / MULTI_ROUTE_COST_RECOVERY_NOT_PROVEN; external validation unproven; formal gate unresolved.
```
