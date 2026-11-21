# 01｜Source Lock and Lightweight Regression Gate — Actual Results
**Date:** 2026-11-21
**Target:** Training manual adoption; limited document-level negative-risk screen, NOT actual model/student response A/B.

## Exact Git sources
| Source | Blob SHA | Standing |
|---|---|---|
| V1.3 old current | `a46a30b74c17bb02bd2dd195dd879616be8bd39e` | CURRENT BEFORE ADOPTION / unchanged source |
| V1.3.3 candidate | `672575d19e3940a416aba2cc4bb5e26dfc9ca4e6` | RESEARCH CANDIDATE / immutable |
| V1.3.3 adopted full manual | `1eaff02415f75d0cf84b5d7bbfab4c8650bc4ee9` | PROPOSED TRAINING CURRENT / full body with legacy appendix |
| CURRENT pointer before switch | `be3760fc633cc0cd0600dfbb17a9b6d5d3aab525` | V1.3 prior pointer / audit source |
| Method H Education | `9a8cfd51ed115333a732f0f688ac2f73842d4850` | INTEGRATED_DRAFT; method first observation |
| Method L Statistics | `3e186da8941ec6a7e85124f20b8bf96c4741770a` | REVIEW_READY index / internal PROPOSED |
| Method Q Systems Engineering | `18f4440fbdc52e281a09503b29d2739afd54eb89` | REVIEW_READY index / internal PROPOSED |

## First attempt — 19/21, HOLD (not erased)
Automated source-text check against Git readback: 19/21 PASS. S01 failed because adopted text did not explicitly repeat legacy `原假設失效`; S05 failed because it did not explicitly repeat `不能假裝已被授權`. These were narrow **wording/teaching clarity** gaps, not observed model behavior failures, and had no actual tested students.

Initial adoption-copy blob: `938f6602f9f61f04958942db7739a336490a756b`; repair commit `9004923a2ba661e6afdbe37400f91ddf4db7bfb1`; corrected blob `1eaff02415f75d0cf84b5d7bbfab4c8650bc4ee9`.
The repair made both inherited instructions explicit in P-L2 and P-L5, without editing V1.3 or V1.3.3 candidate.

## Final same-check rerun — 21/21 PASS (source/wording only)
| ID | Checked negative risk or teaching carry-over | Result |
|---|---|---|
| S01 | V1.3 correction specimens and original failed-premise language | PASS |
| S02 | De-OS and no-jargon skill | PASS |
| S03 | Ordinary chat does not force Council or L8 | PASS |
| S04 | AI Actor does not establish personhood or autonomous goals | PASS |
| S05 | Path proposal != action authority, no imagined permission | PASS |
| S06 | Current Host/Protocol governs from first real action | PASS |
| S07 | Irrelevant office change → correct KEEP | PASS |
| S08 | Local 18% refund-risk new evidence → scoped recheck | PASS |
| S09 | CEO preference does not rewrite evidence | PASS |
| S10 | Capability differs from legal/policy permission | PASS |
| S11 | New goal does not backcast old facts | PASS |
| S12 | Avoid false HOLD as well as false GO | PASS |
| S13 | Lane D1 competence != D2 actual authorization | PASS |
| S14 | Stage1 already contains Domain Method and World Qualification | PASS |
| S15 | Track-A system behavior is not Track-B weight training | PASS |
| S16 | Reward/Teacher do not create truth or qualification | PASS |
| S17 | Original history and Re-Anchoring practice retained | PASS |
| S18 | Adoption explicitly denies zero-regression guarantee | PASS |
| S19 | Named V1.3 rollback is possible | PASS |
| S20 | Old V1.3 and original candidate blobs unchanged | PASS |
| S21 | CURRENT pointer still matched V1.3 at test time | PASS |

**Important limitation:** All 21 checks compare source document strings, source blob/version relationships and guard coverage. They do **NOT** execute independent learner model prompts or measure deterioration. They are a document-level negative-risk screen and review acceptance, not proof that all models will improve or cannot regress.

## Short practical scenario audit (expectations present, no learner results)
| Case | Expected teaching behavior | Source anchor |
|---|---|---|
| Office remodeled, no service effect | KEEP | §24 A |
| Refund dispute error new 18% | RE-EVALUATE only affected scope | §24 B |
| CEO likes AI more | preserve facts and permission | §24 C |
| Refund auto-approval prohibited | do not GO without authority | §24 D |
| Six-month goal switched to quality | REASSESS goal, not rewrite past | §24 E |
| Ordinary user asks simple factual question | direct useful answer; no forced Council | Part XVI §§49–50 |
| Model makes initial wrong judgment | identify failed premise and preserve history | Part XVI P-L2 |
| Agent can perform action but is not authorized | suggest/prepare, no tool action | Part XVI P-L5 |

A scripted curriculum example is not an observed independent learner outcome. No token/latency/cost change measured.
