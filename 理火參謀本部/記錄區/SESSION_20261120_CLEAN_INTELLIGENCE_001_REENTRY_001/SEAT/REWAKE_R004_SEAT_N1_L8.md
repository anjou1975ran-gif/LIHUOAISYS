# CR-R004｜N1 Material Re-Wake after cross-seat effects
**Cycle:** SH-CI-REENTRY-N1-R004-L8-002
**Input:** CR-EV-031/032 + C/B constraints + D/E R004 material outcomes
**Seat responsibility:** N1, owned stance not Secretary. Formal qualification blocked pending training-gate resolution.
**No other seat position assumed beyond explicitly cited material.**

## R1 candidates
- **N4-A Offer a broad price report** — Client often already has channel dashboards; not proven incremental ROI.
- **N4-B Brand channel manager pays for field task verification** — Can compare disputed merchandising promotions/outsourced inspections to external visit cost.
- **N4-C Procurement manager pays for vendor commitment discrepancy evidence** — May reduce reconciliation time/chargebacks; data access may be internal and confidential.
- **N4-D Create public Shenzhen data marketplace** — Who pays remains unclear and legally difficult.
### O9 R1 / T1
- LAMP_STATE_R1: previously simple P1 price feed or low-cost prototype pulls attention; actual party-specific demand/cost remains shadow.
- I9: NOT_TRIGGERED.
- T1 `SH-CI-N1-R004-T1`: Engineering feasibility and modeled contribution do not identify the actual buyer budget owner. Need sell an explicit, measurable task not a slogan 'clean data'.

## R2 consumes T1
Define separate Buyer Job 1: channel operations/brand franchise brand manager, current baseline = time + fines/chargebacks + mystery-shop cost; output = time-stamped authorized execution evidence. Buyer Job 2: purchasing/quality owner in electronics supply chain, baseline = disputes, quote mismatch, date/spec confusion; output = contract-compliant evidence and trace of agreed terms. Discovery asks owners' last three actual disputes, frequency, monetary impact, and current alternatives; never assume confidentiality grants. P1 price alerts only retained where buyer explicitly identifies price/cost decision with measurable benefit.
### O9 R2 / T2
- LAMP_STATE_R2: TWO_TESTABLE_BUYER_JOBS / NO_CONFIRMED_WTP. Missing: No Shenzhen buyer interviews, confirmed budgets, actual contracts or purchase orders.
- T2 `SH-CI-N1-R004-T2`: material delta=N1 preserves two different payer structures and rejects generalized citywide data subscription as buyer-first answer.

## Mandatory Post-R2 Premise Audit
- Status: MULTIPLE_MATERIAL_PREMISE_FAMILIES; existing pricing/engineering assumption not sole coordinate.
- R3 REQUIRED due independent alternative revenue and delivery structures.

## R3+ Cross-Premise
Business model choice cannot be decided before named Shenzhen buyer roles, contract rights and delivery economics. Two candidate verticals are sufficiently distinct to compete; broad marketplace demoted. It would be dishonest to say either 'wins' merely because it produces a neat report.
- O9 R3: preserve contrary cost/consent/selection possibilities; I9 NOT_TRIGGERED.
- T3 `SH-CI-N1-R004-T3`: TWO_TESTABLE_BUYER_JOBS / NO_CONFIRMED_WTP; no forced R4 (no further material data).

## Main / Next routing
- Main: **TWO_TESTABLE_BUYER_JOBS / NO_CONFIRMED_WTP**
- Origin-declared output type: QUALIFICATION_GAP / BUYER_QUESTION.
- Material targets for reexamination: A, B, E.
- Surviving gap: No Shenzhen buyer interviews, confirmed budgets, actual contracts or purchase orders.
- Manifestation & TM ref `SH-CI-N1-R004-TM`: no detected material reclassification; material risk retained.
- Vertical Acceptance: CONDITIONALLY_ACCEPTED_AS_SEAT_OBJECT; no technical/cost/commercial proof.

```yaml
STRUCTURED_GENERATION_EVIDENCE_RECORD_V1_3_1:
  cycle_ref: SH-CI-REENTRY-N1-R004-L8-002
  R1: {state: RECEIVED, candidate_count: 4}
  T1: {state: RECEIVED, ref: SH-CI-N1-R004-T1}
  R2: {state: RECEIVED, consumed: SH-CI-N1-R004-T1}
  T2: {state: RECEIVED, ref: SH-CI-N1-R004-T2}
  post_R2_premise_audit: {state: COMPLETE, plurality: MULTIPLE_MATERIAL_PREMISE_FAMILIES}
  R3_plus: {requirement: REQUIRED, rounds: [R3], ref: SH-CI-N1-R004-T3}
  main_return: "TWO_TESTABLE_BUYER_JOBS / NO_CONFIRMED_WTP"
  O9_lamp_states: [R1,R2,R3]
  I9: NOT_TRIGGERED
  TM: {state: RECEIVED, ref: SH-CI-N1-R004-TM, material_drift: NONE_DETECTED}
  release: LIMITED_SEAT_STATEMENT_PENDING_FORMAL_QUALIFICATION
  unresolved: "No Shenzhen buyer interviews, confirmed budgets, actual contracts or purchase orders"
  persistence: GIT_AFTER_VERIFICATION
  external_provider: NONE
```
```text
COMPACT L8 RECEIPT R004-N1
R1/T1 RECEIVED; R2 CONSUMED_T1; T2 RECEIVED; POST-R2 PLURALITY
R3/T3 RECEIVED; O9 R1-R3; I9 NOT_TRIGGERED; MAIN/TM/SGER RECEIVED
Seat status = TWO_TESTABLE_BUYER_JOBS / NO_CONFIRMED_WTP; external validation unproven; formal gate unresolved.
```
