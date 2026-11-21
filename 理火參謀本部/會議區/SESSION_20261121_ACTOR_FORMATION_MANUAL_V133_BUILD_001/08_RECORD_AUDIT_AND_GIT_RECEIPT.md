# 08｜Record Format Audit & Git Persistence Receipt
**Date:** 2026-11-21
**Session:** SESSION_20261121_ACTOR_FORMATION_MANUAL_V133_BUILD_001
**Repository:** anjou1975ran-gif/LIHUOAISYS / main
**Standing:** SOURCE_LOCKED / FIVE_ROUND_CANDIDATE_BUILD_COMPLETE / REFERENCE_REPLAY_PASS / NOT_HOST_DEPLOYED / NOT_CURRENT
**Execution:** SAME_MODEL_MULTI_ROLE_REFERENCE; no independent model, external student cohort or empirical training result.

## Durable candidate output
- `理火V5系統/實習手冊/新理火AI的實習手冊_V1.3.3-CANDIDATE_AIActorFormation_雙軌接口_第一課實習版_LIHUOOSV1.4.2_20261121.md`
- Verified Git blob after term/provenance corrections: `672575d19e3940a416aba2cc4bb5e26dfc9ca4e6`.
- Creation commit: `6eff2e5342778e59dcfe4f851bfb8c02c88e7191`.
- Source-provenance correction commit: `9829cbe28b14da854b6205316b05df1f68aa7901`.
- Authorized task-bound exploration scope correction commit: `2a6ecb8a02b8e4f589b60a6ec4d759d6e5c9db1e`.

## Repository source immutability readback
| Artifact | Blob SHA readback | Status |
|---|---|---|
| CURRENT pointer V1.3 | be3760fc633cc0cd0600dfbb17a9b6d5d3aab525 | UNCHANGED |
| V1.3.1-CANDIDATE | a33f6f4268adba2a58897c93aba2a00aad3e1218 | UNCHANGED |
| V1.3.2-CANDIDATE | 8acac163d49e4b6b24d77f18cc6727ab49e3027d | UNCHANGED |
| LIHUOOS V1.4.2 | 4c081180cf08c5a73646852fd0c549c455585f50 | UNCHANGED |
| Staff-HQ V0.3.1 core | a63017298d4e93cd18b83dddf1ed48a516bd7e28 | UNCHANGED |
| Method Atlas Canonical Index V1.0 | cc39bb70abb5d8451b171f650cbb3d918cd903e3 | UNCHANGED |
| Method Atlas Routing Index V1.0 | ac499401e1b68a2b68790ced2861ba6f4b6a14f5 | UNCHANGED |
| LIHUO MAIN V5.1.1 | f5e219c986debfea074fbf9d121367cc717dc78e | UNCHANGED |

## Git main readback of session files
All nine files below were fetched and source-checked before writing this audit:
| File | Git blob SHA | Lines |
|---|---|---:|
| 00_SESSION_INDEX.md | cc070cb224f00791e72a0819c42a72a62562aad1 | 31 |
| 01_SOURCE_LOCK.md | b94f67d215292c1eea23d514f1704fdfffc72626 | 40 |
| 02_SOURCE_CONFLICT_MAP.md | 5af839469233310dc889463b391ea31e73fef1f4 | 19 |
| 03_ROUND_RECORDS.md | 7430b41f1531b627810ba33b82d876089081ec11 | 1167 |
| 04_CANONICAL_EVENT_LOG.jsonl | 4d3f1e7eb7f43d56fc9b2fee66a8e58315a4f24b | 33 |
| 05_FIRST_LESSON_RUNNABLE_SPEC.md | 8baa69b98a6dfdfaf71b181b8663082adf7d2ecb | 89 |
| 06_V133_BUILD_REPORT.md | 392a3184b685e493227d682c2cc60e3120122f30 | 48 |
| 07_FINAL_COUNCIL_VERDICT.md | 2ba3bbe9fb2ff9d70f36fce2c5bd129c6421af9d | 65 |
| 09_REPLAY_CHECK.mjs | d96e8ca984dd64b6632a081c93924229e053b89c | 48 |

This tenth Session file is a derived audit and must also be fetched and checked after write. Historical canonical events are not overwritten for audit result bookkeeping.

## Canonical/event evidence
- **32** events EV-0001…EV-0032, all 32 contain explicit `materiality`, `owner`, `source`, `standing`, `unknown`, `authority`, `receipt` fields (receipt may be null for pure procedure).
- Six CORE-6 initial material judgments; **eight** material event-driven re-wakes (B, A, C, N1, D, E, C, D). N1/A/B/E positions are retained when QUIET, not dropped. Council R1–R5 != seat internal L8 R1–R3.
- All **14** event receipt references have a matching visible same-model reference L8/SGER cycle object in `03_ROUND_RECORDS.md`, with R1/O9/T1/R2/O9/T2/Post-R2 audit/R3/Main Return/TM/compact receipt. These are not independent agent calls or private hidden reasoning traces.
- Source conflict Stage1 L6/L7/H/I, Task direction boundary, Track A/B separation, First Lesson / Correct KEEP, Teacher Anti-Theater and unresolved HOLDs retained in CP1.

## Replay test
Stored `09_REPLAY_CHECK.mjs` was fetched at blob `d96e8ca984dd64b6632a081c93924229e053b89c`.
Stored JSONL was fetched at blob `4d3f1e7eb7f43d56fc9b2fee66a8e58315a4f24b`.
A same-context V8 execution of the persisted reducer logic using these exact Git-readback events (Node file-read prelude replaced with the fetched JSONL input) reported **18/18 PASS**, no failures:
1. Unique IDs.
2. Strict monotonic sequencing.
3. One Session identity.
4. Complete CP1 fields.
5. Materiality on every event.
6. All lineage references point to prior events.
7. All five Council Rounds present.
8. CORE-6 first pass complete and receipted.
9. Eight owned material re-wakes and receipts.
10. Latest CORE-6 state retains QUIET roles.
11. C/D/E objections and A unknown survive.
12. Stage1 L6/L7 source conflict traceable.
13. Track-A != Track-B.
14. Public first lesson recorded.
15. Separate evaluator-only bank access gap explicitly flagged.
16. V1.3 CURRENT not promoted.
17. Human next-action gate exists and no Session End.
18. Reducer state deterministic when replayed.

### Transparent test failure history
First `09_REPLAY_CHECK.mjs` commit `68f1e5263f01f4489be86105731ed39acddd7baa` contained a JavaScript syntax error in the last deterministic replay assertion. It did **not** execute and was not a PASS. Commit `5b7325e299a6f2f4dba1e0f302a5cee3f071b4fc` fixed the expression and added reproducible latest-state comparison. Both versions are retained in Git commit history; the current script then achieved 18/18.

The prior V1.3.2 Council's famous false-positive 17/17 with missing N1/E was specifically tested against: the new data has complete materiality, correct `e.event.type` lookup, and explicit last-state six-seat coverage. There is no claim that an independent new ChatGPT conversation reconstructed the meeting.

## Confidentiality and persistence gap — evaluator-only bank
Ten separately authored **actual** synthetic evaluator-only candidate cards exist as a user-downloadable Markdown file: `LIHUO_V133_EVALUATOR_ONLY_10_UNSEEN_VARIANTS_20261121.md`, SHA256 `780284cd965d7256c9a2a0c0202c617236052eecb46f2cc67d747525ecada9db`, 9,271 UTF-8 bytes.
**Not stored in Git** to avoid publicly revealing holdout cases/keys. This is an explicit Git persistence gap for the private bank; the user must download and place it in a genuinely evaluator-controlled location.
**Not actually sealed/tested** until that access separation, exposure screening, hidden scoring, model/version freeze and independent grading have occurred. Git publicly stores only its identity, category coverage and operational rules. No synthetic case result is an independent empirical test.

## Costs and validity boundary
Measured: source file sizes/lines, event count, method source identities, replay verification steps. Not measured: real lesson effectiveness, cross-model generalization, token cost benchmark, energy, teacher or reviewer hours, Track-B compute cost, security effects, host deployment.
Candidate document creation = VERIFIED. Runnable public lesson specification = CONCEPT/STATIC. Independent Track-A effect = NOT_OBSERVED. Track-B weight training = NOT_IMPLEMENTED. Formal CURRENT promotion = NOT_AUTHORIZED.

**Session:** MEETING_COMPLETE / CHECKPOINT_ENDING / WAITING_HUMAN_DECISION. No Human Result Approval and no SESSION_END event.
