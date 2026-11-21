# Stage 2A｜Git Persistence、來源與輸出審計收據
**Date**：2026-11-21
**Branch**：main
**Standing**：EXTERNAL_GIT_DURABLE_FOR_RESEARCH_PROTOTYPE / SAME_MODEL_REFERENCE_ONLY。
**Research decision**：UPGRADE_AK_ONLY (candidate recommendation), STAGE_2B_WARRANTED (not run / not approved by this receipt).

## 已寫入且回讀的研究檔案
1. `00_SOURCE_LOCK_AND_ABLATION_CONTRACT.md` — `2e457074ac2dfc53522ff5fba62af1f1b2f72e47` — 2,481 characters
2. `01_CASE_A_ENHANCED_AK.md` — `ecc0942c2eb6f90e7ddfcf0dcb1387b1f612220b` — 2,796 characters
3. `02_CASE_B_ENHANCED_AK.md` — `34211b9509b203973467ebb7943b1e0405a685bc` — 3,516 characters
4. `03_STAGE2A_STRUCTURAL_COMPARISON_AND_RECOMMENDATION.md` — `b69635498dead7d83e74ec19293fbc26a8fa01a1` — 7,003 characters
5. `04_DAIL_ENHANCED_AK_CP3_RESEARCH.yaml` — `3ea1427d9f8364c27149c8d7aa553b86425d97db` — 3,391 characters

**Git main head after these files**：`720ed15f8db824aa51a714b7f0c4bf388cf6001d`。
**Output checks**：Case A/B both preserve exactly A–K headings and contain `WHAT_CHANGED_BECAUSE_OF_THIS_MEETING`, `OBJECTION_LIFECYCLE`, `TEMPORAL_ONLY`, `EVIDENCE_GAP`, `QUIET`, and HOLD / UNKNOWN distinctions. Candidate DAIL contains `no_independent_capability_registration: true`.
**Exact Stage 1 comparator unchanged**：Legacy A–K and Projector use Stage 1 report parts at previously recorded blobs A `3af192e914db9ee2634b3fc3abb4d2a369d06f10` / B `93732b86d111d9fa255b22ffddd0712fbc6a3e02`, no baseline rewriting.

## Frozen source boundaries
- Case A R006 17 events; Case B R004 40 events; exact 10+15 frozen source SHA entries in Stage 1 lock.
- During Stage 2A, re-read original A event ledger `36a4a81dd58257e13001c014243bddfd91554dfa` & B R003 `277677a938dde312f435b9af656ff4d4adf1799f`, B R004 `45d4ef12247d920db5f7567a4ca026d14ae8b9e6`, plus original owner visible text and R004 cross-seat summary.
- Positive cause chains verified against owner text: A C→B, E→A; B C→E, E→C, B→D. D→B (A) and N1→C/E (B) are explicit `TEMPORAL_ONLY` negative examples.
- No material past Session events were appended, modified, or deleted by this Stage.

## Current non-modification checked
- `LIHUOOS/V1版本/正式版/理火OSV1.4.2(點燈回歸).md` SHA `4c081180cf08c5a73646852fd0c549c455585f50` (unchanged).
- `理火參謀本部/工程區/VERTICAL_LIHUOOS_V1.4.2_理火參謀本部_V0.1_20261120.md` SHA `1c23fe0feea77f2e546a08254d6a0e8b6d022583` (unchanged).
- `理火參謀本部/MEMO區/MEMO_Secretariat_Architecture_V0.1_FIRST_BASELINE_20261120.md` SHA `8838bd91a7c201a2f769da8994b44ad5af021872` (unchanged).
- `理火參謀本部/記錄區/MEETING_RECORD_AND_CHAT_SURFACE_V0.1_20261120.md` SHA `eb588d7c0fc5cc337088d9f4d749f4a46d0f18ba` (unchanged).
- Nothing in L9 Current Registry or Protocol was authored, nor any current status change claimed. The only new paths are this research folder.

## Known evidence limits
- This is an author-context, same-model, non-blind **structural expressibility comparison**, not human comprehension improvement or new LLM mechanism proof.
- Length = character proxy, not performance cost; no actual per-arm token, latency or human reading time.
- This receipt's own Git persistence requires its separate write and readback; the five items above were already verified.
