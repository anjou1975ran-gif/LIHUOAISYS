# MEMO｜Pre-Session Proposed Entry｜提議者法位與席位自主路由
**Date:** 2026-11-20
**Status:** EXPERIMENTAL_DESIGN_WORKING / NOT_RUNTIME_PATCH / NOT_RATIFIED / NO_INDEPENDENT_RADAR_AGENT
**Source:** Human new idea on Radar as proposer, existing `理火OSV1.4.2(點燈回歸).md` Radar L5.23 distinction `RADAR SIGNAL != QUALIFICATION`, earlier CASE-003 L9 RADAR advisory reference, PSO-TRI-001 prior result. Existing V0.2.1 remains unchanged.

## 1｜Why this is a different object from full Orientation
```text
SECRETARIAT → SHARED_SOURCE_BOUND_PREPROCESSING_INDEX
RADAR or SECRETARIAT → OPTIONAL CANDIDATE_ENTRY_SIGNAL (origin attributed)
EACH SEAT → ACCEPT_START | MODIFY | REJECT | NO_POSITION
  → SEAT METHOD CLOCK A → FIRST OBSERVATION → L8 / COUNCIL
```
Shared source preprocessing belongs to Secretariat; optional entry **discovery/suggestion** is not default Council direction. Do not insert a fourth PSO-TRI arm retroactively. The existing C intervention can be abstracted conceptually to `PROPOSED_ENTRY`, whose `proposer` might be `SECRETARIAT | LIHUO_RADAR` in a *later* source-effect test.

## 2｜Authority separation
`SENSOR MAY PROPOSE DIRECTION; SENSOR MAY NOT OWN DIRECTION AUTHORITY`.
`RADAR IS A DETECTOR, NOT NAVIGATION AUTHORITY`.
`RADAR DETECTION != MATERIAL IMPORTANCE`.
`RADAR RECOMMENDATION != METHOD SELECTION != COUNCIL DIRECTION`.
`PROPOSED_ENTRY != P0 != D1_CONFIRMATION != SEAT_STANCE`.
`NO_POSITION != APPROVAL`.

Radar can: flag an entry signal, say why it flagged with exact source refs, mark uncertainty and more than one candidate when material. Radar cannot: choose methods for Seats, qualify Problem Frame, own Seat stance, approve D1, claim consensus, contact externals, grant an action right. Secretariat can normalize/route/record but cannot quietly reword a Radar observation into mandatory Council starting thesis.

## 3｜Thin schema — candidate, not ratified runtime
```yaml
PROPOSED_ENTRY_CANDIDATE:
  proposer: SECRETARIAT | LIHUO_RADAR
  proposer_role: PREPARATORY_SUGGESTER | SIGNAL_AND_ENTRY_RECOMMENDER
  signal: "值得起步檢查的可爭議線索，不是已證關鍵答案"
  why_flagged: []
  source_refs: []
  standing: CANDIDATE_ENTRY_ONLY
  confidence:
    meaning: SIGNAL_WORTH_A_LOOK
    value: LOW | MEDIUM | HIGH
    truth_of_interpretation: NOT_ESTABLISHED_BY_THIS_FIELD
  unresolved: []
  possible_defeater: OPTIONAL_WHEN_PRACTICABLE
  null_option: ALLOWED
  seat_actions: [ACCEPT_START, MODIFY, REJECT, NO_POSITION]
  authority_created: NONE
  MethodChoice: SEAT_ONLY_CLOCK_A
```
**Guard:** `confidence` never means the proposition is factually true; do not use radar aura as an evidence-quality score. Avoid "Radar discovered THE core issue"; use "Radar flagged a signal possibly worth examining".

## 4｜How this relates to the source-first screen
- Candidate entry source may be a **Radar advisory registration** but it is not a new Professional Agent and not a verified autonomous process. A true real Radar execution requires actual log, separate execution identity and source trace.
- Each Seat records preliminary routing reaction with rationale. This is not full Material Judgment or forced six-seat debate. Only actual Material First Observation needs Clock A + L8. `NO_MATERIAL_DELTA → QUIET` still applies; a NO_POSITION Seat may have a separate safety/qualification issue that warrants its own L8.
- If a Seat **modifies or rejects** the candidate, it should not be required to use the suggested frame to select its Method. Original source references and alternatives remain accessible.
- Origin of suggestion `RADAR` cannot be used as a criterion for schema acceptance into Council stance or proposals. Any material Council proposal requires legitimate seat/human origin/qualification, not a metadata label.

## 5｜The key experiment is source effect, not three-arm expansion
Separate control after verifying proposed-entry mechanism:
```text
SAME D0 + SAME RAW + SAME GROUND_INDEX + SAME ENTRY_BODY
    P1: proposer SECRETARIAT
    P2: proposer LIHUO_RADAR
COMPARE:
    entry_accept_modify_reject_no_position
    first-observation primary-unit diversity
    method choice / NO_METHOD reason
    source qualification / framing capture
    actual end-to-end preparation cost
```
If the signal body, number of candidates, evidence, amount of language, or seat permissions change alongside proposer, do NOT claim proposer-source effects. Ideally compare in isolated contexts with blinded evaluator. Same-model sequential reference cannot prove a difference in implicit authority or compliance.

## 6｜Previous test and early reference standing
- `PSO-TRI-001` tested A RAW, B Ground Index, C Ground Index + a multi-entry Orientation Card. B/C shared same index, but results were NOT a clean context-isolated experiment; no demonstrated material gain or net cost improvement.
- `PSO-ENTRY-PROPOSER-001` creates **separate** Secretariat/Radar origin variants with identical thin signal body and six pre-Clock-A screens. This may demonstrate mechanical route controls; it is not a fourth arm or a positive performance benchmark.
- The six-seat Entry screen itself has resource cost and can lead to scripted, superficial divergence. Don't mandate all seats to respond just to show refusal is possible; allow Quiet when no material interest. `NO_MATERIAL_DELTA -> NO_REINVOCATION`.

**Promotability:** only after measured net benefit and acceptable First Observation/Method divergence under a cleaner source-effect and proposed-entry study. No automatic update to Staff-HQ V0.2.1.
