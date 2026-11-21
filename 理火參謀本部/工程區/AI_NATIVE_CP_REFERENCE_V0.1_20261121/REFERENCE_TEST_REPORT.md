# AI-native CP1→CP2 Reference Replay — Execution & Limits
**Date:** 2026-11-21
**Standing:** REFERENCE_IMPLEMENTATION_TESTED_ON_SYNTHETIC_FIXTURE / NOT_MRC001_VALIDATED / NOT_PRODUCTION_DEPLOYED
**Execution:** single JS/V8 reference simulation in same tool context; **not** independently validated IR/DAIL authority or multi-agent runtime.
**Input:** 10 synthetic CP1 typed events in fixed order (source ref, C objection, N1 consumption/reasoned retention, C minority HOLD, F reference and Human decision request). Test source and expected rules available under this directory.
**Result:** **14/14 reference assertions PASS** on this one self-authored fixture. This includes negative tests: Secretary cannot write Seat stance; missing L8 ref rejected; duplicate event rejected; F cannot be CORE-7.
**Strongest reason this matters:** deleting human projections does not alter reduced state; C's material objection and minority HOLD survive; the human gate renders a readable request.
**Qualification limit:** Reproducer is purposely small and does not support arbitrary historic event schemas, complex proposal lifecycle, real Git snapshot/CRDT persistence, live external sources, or actual L8 execution. It does not prove cost savings. A real reducer must be implemented and independently replayed before MRC-001 can be called engineering validated.
**Consumption:** Node.js ESM can import reference_replay.mjs and feed fixture.jsonl; no dependency installer required. Test runner source attached.
**Files:**
- reference_replay.mjs
- fixture.jsonl
- reference_test.mjs
- expected_state.json
- expected_human_request.json
**Checks:**
- T01_state_replay_idempotent: PASS
- T02_objection_survives: PASS
- T03_minority_hold_survives: PASS
- T04_relation_responded_only_after_consumption: PASS
- T05_human_gate_renders_request: PASS
- T06_discard_human_view_no_effect: PASS
- T07_F_not_core: PASS
- T08_unknown_survives: PASS
- T09_forged_Secretary_stance_rejected: PASS
- T10_missing_material_L8_rejected: PASS
- T11_duplicate_event_rejected: PASS
- T12_F_core_promotion_rejected: PASS
- T13_objection_cannot_become_auto_qualified: PASS
- T14_human_silence_not_approval: PASS
**Outstanding:** real source migration, independent blind auditor, pre-/post-token+reading cost, failure injection with invalid authority, F actual numeric forecast, round/seat replay at scale.
