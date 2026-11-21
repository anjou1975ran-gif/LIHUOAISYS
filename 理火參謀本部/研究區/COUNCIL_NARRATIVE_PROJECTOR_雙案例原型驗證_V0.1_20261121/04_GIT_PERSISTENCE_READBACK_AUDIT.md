# Git Persistence & Readback Audit｜Council Narrative Projector Dual Case 001
**Date:** 2026-11-21
**Branch:** main
**Readback verified immediately before this receipt:** main head `ddbc7410cd3f976daebe3f6c371363d07603b67e`.
**Successful add/update commits:** source/DAIL lock `7e7c4d7237eb4297565c108f41e369fc9c2acb20`; Case A `80ef49e53a44d6f07d65b902ec31af61b48236d6`; Case B first `757b0a36b50c0c7c4d0de50329e5d2c6880c1200`; B event-ID normalization `a3c21abff5f5149bb77d0907334515a51c72e57a`; evaluation `ddbc7410cd3f976daebe3f6c371363d07603b67e`.

## File readback (all nonempty, exact blobs)
- 00_PROTOCOL_SOURCE_LOCK_DAIL.md — `f38b43dd257f3e8d484202b30ffcb16aebe6eac9` — 4863 characters
- 01_CASE_A_ALL_THREE_ARMS.md — `3af192e914db9ee2634b3fc3abb4d2a369d06f10` — 5076 characters
- 02_CASE_B_ALL_THREE_ARMS.md — `93732b86d111d9fa255b22ffddd0712fbc6a3e02` — 6452 characters
- 03_EVALUATION_AND_SOURCE_CROSSWALK.md — `4fc863c91991ba36e2234a8341d79b433245061d` — 4581 characters

**Structure check:** Case A and Case B each contain LEGACY A–K, ORDINARY_SUMMARY, DAIL EXECUTIVE_BRIEF, DAIL NARRATIVE_FULL_REPORT, DAIL AUDIT_EXPLAIN. Both Projector reports contain WHAT_CHANGED_BECAUSE_OF_THIS_MEETING and OBJECTION_LIFECYCLE. Case B exact event IDs normalized to `EV-###`, 0 remaining `EV###` display variants.

**Original source check:** Case A source lock 10 of 10 file SHA matches; Case B 15 of 15 file SHA matches, including exact P1 candidate. Historical canonical files were NOT edited. 17 Case A events and 40 Case B events read as source; no fabricated additional Event.
**Research standing:** DESK_PROTOTYPE_GENERATED / NO_HUMAN_RATER / NO_CONTROLLED_BLIND_EFFICACY / NO_MODEL_WEIGHT_CHANGE / NO_L9_BINDING / NO_OS_OR_CURRENT_STAFFHQ_CHANGE.
**Recommendation:** REVISE (Chief LIHUO AI still must separately review; no promotion).
**Persistence:** Those four outputs verified EXTERNAL_DURABLE; this receipt file itself must be read back in its own Git write before claim of its own durability.

**Important:** Three-arm output shares case-specific locked source sets but uses different rendering instructions; the authorship environment is the SAME model context, not isolated provider calls. Actual token/latency/read-time are NOT_CAPTURED.
