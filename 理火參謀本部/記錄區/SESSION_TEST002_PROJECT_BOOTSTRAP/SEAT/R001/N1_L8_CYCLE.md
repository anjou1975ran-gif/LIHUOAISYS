# TEST-002 R001｜N1 Common-Sense Seat｜L8 Cycle Record

**cycle_ref:** T002-R001-N1-C01
**host_mode:** NON_HOST
**execution_identity:** SAME_MODEL_MULTI_ROLE_REFERENCE
**seat:** N1
**proposal:** P0
**vertical:** Staff-HQ Vertical V0.1

## Qualified Input
Question: multi-model first vs reducer/replay first.
N1 responsibility: BASIC_QUESTION / EXECUTIVE_CLARITY / USER_ACTION.

## R1
Candidate paths:
- N1-P1: Multi-model first; learn whether distinct models actually disagree usefully.
- N1-P2: Reducer first; make state/history trustworthy before adding model diversity.
- N1-P3: Thin reducer + small 2-model probe.

Provisional order:
1. N1-P3
2. N1-P2
3. N1-P1

Material counterforce:
- P3 may become a vague compromise that builds two half-systems.

## LAMP_STATE_R1
main_lamp: "What do we need to learn first?"
active_lamps:
- "Can we tell real disagreement from state drift?"
- "Can we test model diversity without full infrastructure?"
dark_zone:
- "Definition of minimum reducer"
false_completion_risk: "Calling hybrid best without specifying minimum"

## T1
R1 favors a staged hybrid, but the minimum boundary is not yet qualified.

## R2｜Genuine Recompetition
Challenge incumbent P3:
- If reducer is too thin, multi-model output becomes noisy and unreplayable.
- If reducer is too large, we delay the very phenomenon we want to observe.

New candidate:
- N1-P4: Build only canonical event schema + replayable state snapshot, then immediately run a 2-model pilot.

R2 order:
1. N1-P4
2. N1-P2
3. N1-P1
4. N1-P3

## LAMP_STATE_R2
main_lamp: "Minimal auditability before diversity"
active_lamps:
- canonical event identity
- replayable snapshot
- immediate empirical multi-model probe
dark_zone:
- production-grade reducer
false_completion_risk: "Overbuilding infrastructure before learning"

## T2
N1-P4 replaces vague hybrid with a staged gate.

## Post-R2 Premise Audit
Current premise family: "What should be built first?"
Alternative material premise: "What sequence gives the fastest trustworthy learning?"
Status: MULTIPLE_MATERIAL_PREMISE_FAMILIES
R3 required.

## R3｜Cross-Premise
Under learning-rate premise:
- A full multi-model-first path gives fast observations but low interpretability.
- A full reducer-first path gives interpretability but delays observations.
- Minimal replay core → 2-model probe preserves both.

## LAMP_STATE_R3
main_lamp: "Trustworthy learning sequence"
active_lamps:
- minimal replay core
- small diversity probe
dark_zone:
- full productionization
false_completion_risk: LOW

## T3
Staged path remains top across both premise families.

## Main Return
stance: CONDITIONAL_SUPPORT for reducer-first only if "reducer" means minimum replayable core, followed quickly by 2-model probe.
declared_objects:
- amendment: A-N1-T002-001 "Minimal replay core → 2-model probe"
- question: Q-N1-T002-001 "What is the smallest replay core that can distinguish state drift from genuine disagreement?"
unresolved:
- exact minimum schema

## TM Fidelity
PASS: manifestation matches Main Return; no stance inflation.

## Staff-HQ Vertical Acceptance
ACCEPTED.
Reason: seat scope valid; typed objects declared; no cross-seat rewrite; L8 evidence present.

## SGER
persistence: EXTERNAL_DURABLE upon successful GitHub write.
R1/R2/R3/T1/T2/T3 material evidence: inline above.
main_return_ref: inline
manifestation_ref: inline
unresolved: exact minimum reducer boundary.

## Compact L8 Cycle Receipt
~~~yaml
cycle_ref: T002-R001-N1-C01
R1: COMPLETED
LAMP_STATE_R1: PRESENT
T1: PRESENT
R2: COMPLETED_AND_CONSUMED_T1
LAMP_STATE_R2: PRESENT
T2: PRESENT
post_R2_premise_audit: MULTIPLE_MATERIAL_PREMISE_FAMILIES
R3: COMPLETED
LAMP_STATE_R3: PRESENT
T3: PRESENT
main_return: RECEIVED_CHAT_NATIVE
post_main_governance: PROCEED
TM: PASS
vertical_acceptance: ACCEPTED
SGER: INLINE_AND_GITHUB_TARGET
cycle_outcome: COMPLETED
~~~
