# STAFF-HQ V0.3.1｜CP Migration / Regression Plan
**Date:** 2026-11-21
**Standing:** ENGINEERING_DESIGN_AND_REFERENCE_TEST / NOT_DEPLOYED / NO_RETROACTIVE_MIGRATION
**Source lock:** V0.3.0 full SHA 095c3eb799d0f1e89bff8cf3a898cd2c87add7a8; Secretariat V0.1 SHA 8838bd91a7c201a2f769da8994b44ad5af021872; Meeting Record V0.1 SHA eb588d7c0fc5cc337088d9f4d749f4a46d0f18ba; Decision Request V0.1 SHA ce5abb7c012470bf210f17d1d3f0b81bd0035776.

## Why not immediately replace historical events?
Old Council histories may include event JSONL, Markdown evidence, human report and typed statements that follow different schemas. A new CP1 schema is **not** a machine instruction to force origin semantic typing. Legacy historical files remain immutable. A sidecar index may record exact object mappings with a qualified owner; ambiguous elements HOLD / raw ref, not guessed.

## Four-layer nomenclature collision resolution
- Legacy Meeting Record **L0 EVENT** → CP1 CANONICAL_TYPED with CP0 source.
- Legacy **L1 ROUND** → CP2 state + canonical event refs.
- Legacy **L2 CHAT** → CP3.
- Legacy **L3 FINAL** → CP3.
- V0.3.0 CANONICAL/OPERATIONAL/DERIVED → CP1/CP2/CP3, SOURCE_RAW CP0 explicit.
- LIHUOOS L8 is a *seat cognition cycle* and independent of CP0–CP3 data-plane names.

## Migration strategy
1. Freeze current baseline by blob SHA and original Session IDs.
2. Start new CP0/CP1 format on a synthetic new **reference fixture**, not original real history.
3. Test owner/source/premise/authority/lineage/standing/unknown preservation.
4. Remove all CP2/CP3 artifacts and replay from CP1 and static contracts.
5. Verify required Human Decision projection and falsification of unauthorized auto-approval.
6. Pilot on copy of a historical session **without rewriting it**, retaining source refs and mapping ambiguity.
7. Only after source validation consider introducing a formal DAIL/IR versioned patch, human Ratification and a new runtime implementation.

## Minimal reference objects for tests
- D0 from human (raw).
- D1 mandate as separate human/secretariat interpretation, NOT confirmed by silence.
- P1 source-bound candidate with exact version and origin.
- N1/B initial positions, C typed objection with premise/source/authority.
- B own response consumes C objection, may RETAIN_WITH_REASON.
- C minority HOLD remains until C origin-owned resolution.
- Human gate requires Decision Request; no Human approval exists.

## Test gates
| ID | Test | PASS | NOT PASS |
|---|---|---|---|
| CP-01 | Preserve meaning | owner/sources/premise/scope/authority/standing/unknown and objection in CP1 | only report prose carries them |
| CP-02 | Replay | same CP1 input+contracts same CP2; CP3 deletion irrelevant | final report is required |
| CP-03 | Human gate | plain-language Request when required | WAITING_HUMAN without Request |
| CP-04 | Secretariat power | derived output cannot change origin-owned stance | view upgrades position |
| CP-05 | Minority preservation | active objection/HOLD survives summary removal | SILENT removal |
| CP-06 | F separation | F shadow cannot qualify CORE review | F counted as core |
| CP-07 | Persistence | Git durable only after actual success, immutable old history | phantom write |
| CP-08 | Real economics | actual comparative token/generation/reading/storage evidence before claims | fixed energy % invented |
| CP-09 | L8 full source | one source record with actual material L8 evidence, SGER and receipt; CP1 refs it | short schema erases counterforce or fakes L8 |
| CP-10 | Non-material | QUIET/one source ref, no duplicate prose | seat and renderer forced to speak |

**Important tension:** a shorter startup Runtime reduces **read load**, but if a task causes many ad-hoc fetches it may raise repeated retrieval overhead. The new core must **not** claim global savings without measured workload. CP3 on-demand audit may be more expensive *at that moment* but cheaper across long sessions.

## Status
- Design source comparison: DONE.
- CP1 candidate fields documented: DONE.
- Test case layout: DEFINED.
- Deterministic reducer and provider-independent validation: NOT_DEPLOYED.
- Corpus-wide byte/token study: NOT_RUN.
- Formal Ratification: NOT_GRANTED.

**END**
