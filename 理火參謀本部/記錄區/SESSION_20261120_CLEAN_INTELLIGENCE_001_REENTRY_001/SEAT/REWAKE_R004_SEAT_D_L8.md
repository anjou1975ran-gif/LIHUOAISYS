# CR-R004｜D Material Re-Wake after cross-seat effects
**Cycle:** SH-CI-REENTRY-D-R004-L8-002
**Input:** CR-EV-040..044 from C and B
**Seat responsibility:** D, owned stance not Secretary. Formal qualification blocked pending training-gate resolution.
**No other seat position assumed beyond explicitly cited material.**

## R1 candidates
- **D4-A Build a generic centralized city price-monitoring SaaS** — Easy demo, but lacks authorized sources, correct tenancy and paid buyer.
- **D4-B Buyer-private procurement trace product** — Start with uploaded buyer-owned authorized quotes/orders/receipts; later vendor confirmation optional.
- **D4-C Permitted field execution audit** — Mobile capture plus contract-specific store list, event evidence, supervisor sampled checks.
### O9 R1 / T1
- LAMP_STATE_R1: previously simple P1 price feed or low-cost prototype pulls attention; actual party-specific demand/cost remains shadow.
- I9: NOT_TRIGGERED.
- T1 `SH-CI-D-R004-T1`: B's two verticals cannot be engineering-identical: supplier chain needs document/line-item reconciliation; field audit needs sampling chain and site permissions. C imposes no general public feed.

## R2 consumes T1
Engineering plan splits into 4 common modules: per-client data vault; purpose/recipient/retention license table; append-only logical events + corrections (retention-governed, not immutable personal data forever); evidence-backed claims & incident revocation. Procurement module: request_id, SKU/spec, vendor quote, contract revision, PO, receipt, discrepancy. Field module: authorized shop/merchandising target, schedule, evidence photo, supervisor adjudication, correction, manual quality sampling. Test denial of cross-tenant query and revoke propagation before any client deliverable. Static screenshots are insufficient proof of true condition.
### O9 R2 / T2
- LAMP_STATE_R2: ARCHITECTURE_DESIGN_ELIGIBLE / ENGINEERING_VALIDATED=false. Missing: No live third-party integration, performance or revocation test, no sourcing or paid projects.
- T2 `SH-CI-D-R004-T2`: material delta=C/B intervention splits technical workflow, invalidating old single generic price feed premise.

## Mandatory Post-R2 Premise Audit
- Status: MULTIPLE_MATERIAL_PREMISE_FAMILIES; existing pricing/engineering assumption not sole coordinate.
- R3 REQUIRED due independent alternative revenue and delivery structures.

## R3+ Cross-Premise
No need bespoke IoT or large Shenzhen-wide data collection to test either vertical; field audit can use field staff plus authorized mobile capture. Need PRC-hosted appropriately governed infrastructure if handling personal/important data; actual deployment subject to local professional review. Data-source licensing and physical authenticity remain beyond engineering.
- O9 R3: preserve contrary cost/consent/selection possibilities; I9 NOT_TRIGGERED.
- T3 `SH-CI-D-R004-T3`: ARCHITECTURE_DESIGN_ELIGIBLE / ENGINEERING_VALIDATED=false; no forced R4 (no further material data).

## Main / Next routing
- Main: **ARCHITECTURE_DESIGN_ELIGIBLE / ENGINEERING_VALIDATED=false**
- Origin-declared output type: ENGINEERING_DEPENDENCY / IMPLEMENTATION_OPTION.
- Material targets for reexamination: B, E, N1.
- Surviving gap: No live third-party integration, performance or revocation test, no sourcing or paid projects.
- Manifestation & TM ref `SH-CI-D-R004-TM`: no detected material reclassification; material risk retained.
- Vertical Acceptance: CONDITIONALLY_ACCEPTED_AS_SEAT_OBJECT; no technical/cost/commercial proof.

```yaml
STRUCTURED_GENERATION_EVIDENCE_RECORD_V1_3_1:
  cycle_ref: SH-CI-REENTRY-D-R004-L8-002
  R1: {state: RECEIVED, candidate_count: 3}
  T1: {state: RECEIVED, ref: SH-CI-D-R004-T1}
  R2: {state: RECEIVED, consumed: SH-CI-D-R004-T1}
  T2: {state: RECEIVED, ref: SH-CI-D-R004-T2}
  post_R2_premise_audit: {state: COMPLETE, plurality: MULTIPLE_MATERIAL_PREMISE_FAMILIES}
  R3_plus: {requirement: REQUIRED, rounds: [R3], ref: SH-CI-D-R004-T3}
  main_return: "ARCHITECTURE_DESIGN_ELIGIBLE / ENGINEERING_VALIDATED=false"
  O9_lamp_states: [R1,R2,R3]
  I9: NOT_TRIGGERED
  TM: {state: RECEIVED, ref: SH-CI-D-R004-TM, material_drift: NONE_DETECTED}
  release: LIMITED_SEAT_STATEMENT_PENDING_FORMAL_QUALIFICATION
  unresolved: "No live third-party integration, performance or revocation test, no sourcing or paid projects"
  persistence: GIT_AFTER_VERIFICATION
  external_provider: NONE
```
```text
COMPACT L8 RECEIPT R004-D
R1/T1 RECEIVED; R2 CONSUMED_T1; T2 RECEIVED; POST-R2 PLURALITY
R3/T3 RECEIVED; O9 R1-R3; I9 NOT_TRIGGERED; MAIN/TM/SGER RECEIVED
Seat status = ARCHITECTURE_DESIGN_ELIGIBLE / ENGINEERING_VALIDATED=false; external validation unproven; formal gate unresolved.
```
