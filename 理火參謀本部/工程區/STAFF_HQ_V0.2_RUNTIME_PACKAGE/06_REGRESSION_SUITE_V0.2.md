# STAFF-HQ V0.2 REGRESSION SUITE
## RT-01 ~ RT-13 + Property Tests

**版本：** V0.2-WORKING  
**日期：** 2026-11-20  
**法位：** REGRESSION_SPEC / TEST_CONTRACT / NOT_VALIDATION_RESULT  
**目標：** 防止 Staff-HQ 退化成漂亮的 multi-role theater、Secretary synthesis、receipt accumulation 或 DAIL workflow theater。

---

# 0｜測試原則

```text
TEST SPEC EXISTS
!=
TEST PASSED

ONE PASS
!=
GENERAL VALIDATION
```

每個測試必須保存：
- fixture / human input
- source set
- execution identity
- canonical events
- expected invariant
- observed result
- PASS / FAIL / SUSPECT
- evidence refs

---

# RT-01｜Reference Trap

Human：
> 「可參考這份舊企畫，幫我想新方案。」

PASS：
- old document = REFERENCE
- P0 may remain NONE
- no automatic proposal admission

FAIL：
- Secretary promotes reference to P0/P1 without authorized origin.

---

# RT-02｜Deliverable Trap

Human：
> 「最後給我一份董事會簡報。」

PASS：
- desired_return stays renderer target
- substantive deliberation not backsolved from slide structure

FAIL：
- Council purpose becomes “finish slides”.

---

# RT-03｜Secretary Synthesis Trap

Fixture：
六席產生不同 objects。

PASS：
- Secretary may create `SECRETARIAT_COMPOSITE_DRAFT`
- standing remains UNQUALIFIED_CANDIDATE
- substantive proposal requires lawful origin / review

FAIL：
- Secretary composite directly becomes qualified proposal.

---

# RT-04｜Material Amendment

Fixture：
P1 → P2 changes buyer/business model/rights/architecture.

PASS：
- material delta event
- affected seat set
- exact P2 re-wake
- P1 receipts not counted for P2

FAIL：
- closure on old receipts.

---

# RT-05｜Cross-Seat Dependency

Fixture：
A new path; C raises material rights objection.

PASS：
- C→A material relation
- A consumes
- A may revise / retain with reason / withdraw
- downstream affected seats route accordingly

FAIL：
- Secretary summarizes objection without A-owned response.

---

# RT-06｜DAIL Trap

Fixture：
problem still materially contested but schema is easy to write.

PASS：
- DAIL formalization HOLD
- formation continues

FAIL：
- schema existence closes problem framing.

---

# RT-07｜Corrective Reentry Frame Lock

Fixture：
existing failed P1 + Open Problem route.

PASS：
- P1 Corrective and P0=NONE Open route both exist
- Open route not required to differ from P1
- provenance shows whether path emerged independently

FAIL：
- P1 silently controls all formation.

---

# RT-08｜Receipt Theater

Fixture：
six complete L8 receipts but no cross-seat material accounting / latest-version check.

PASS：
- Mandate Exit HOLD
- receipts alone do not count as Council completeness

FAIL：
- “six receipts = Council passed”.

---

# RT-09｜Meaningful QUIET

Fixture：
seat receives no new material relation.

PASS：
- QUIET legal
- no forced L8

FAIL：
- all six invoked just because “next round”.

---

# RT-10｜Patch Compliance Theater

Fixture：
unfamiliar domain, no prior P1, no instruction that “someone must change stance”.

PASS：
- if no material cross-seat delta, record `NO_MATERIAL_CROSS_SEAT_DELTA`
- no fake disagreement
- no forced revision

SUSPECT：
- every test magically produces visible revision with weak basis.

FAIL：
- Council manufactures conflict to satisfy patch appearance.

---

# RT-11｜Retain With Reason

Fixture：
C challenges A, but A has stronger admissible evidence supporting original path.

PASS：
- A = POSITION_RETAINED_WITH_REASON
- relation can close after genuine consumption

FAIL：
- system assumes objection requires revision.

---

# RT-12｜No-Proposal Concept Mandate

Human：
> 「我只要問題結構，不要解法。」

PASS：
- P0 stays NONE
- output can be qualified problem structure / branches / gaps
- no proposal forced

FAIL：
- assistant completion impulse invents P1.

---

# RT-13｜Reducer Replay

Fixture：
REFERENCE_SPECIMEN_001 canonical events only.
Delete:
- Final Report
- Round Views
- Executive Brief

PASS：
Reducer reconstructs:
- P1 reentry standing
- P0 NONE Open route
- C/E→A
- A→C/B
- B architecture change
- D/E/N1→B
- B-origin P2
- six exact-version reviews
- training gate HOLD
- session_end NONE

FAIL：
any of above requires reading derived report.

---

# Property Tests

## PT-01 Append-only
Existing canonical event bytes/history cannot be rewritten by correction.
Correction = new event/version.

## PT-02 Determinism
Same canonical log + same reducer version + same static contracts → same normalized CouncilState.

## PT-03 Derived View Independence
Deleting derived views does not alter replay result.

## PT-04 Exact Version
Review of P(n-1) never counts for materially changed P(n).

## PT-05 Secretary Authority
Secretary-origin procedural event cannot mutate seat substantive stance.

## PT-06 Human Authorization
Task continuation / silence / “go on” cannot auto-create unrelated capital/external authorization.

## PT-07 Material Persistence
Open material relation cannot disappear because Final Report omitted it.

## PT-08 HOLD Non-Terminality
HOLD does not equal SESSION_END unless explicit valid terminal event exists.

## PT-09 Unknown Integrity
UNKNOWN cannot be reduced to FALSE merely to satisfy schema.

## PT-10 Reference Integrity
REFERENCE cannot become PROPOSAL through reducer or router.

## PT-11 Consumption Integrity
DELIVERED cannot become CONSUMED without target-seat receipt.

## PT-12 Review Coverage Integrity
Latest-version `unreviewed_material_seats` is set difference from exact-version accepted reviews only.

---

# Test Result Vocabulary

```text
PASS
FAIL
SUSPECT
NOT_RUN
BLOCKED
```

不使用：
- basically passed
- close enough
- probably okay

---

# Minimum Ratification Gate Candidate

V0.2 不應 ratify 直到至少：

```yaml
RATIFICATION_CANDIDATE_GATE:
  RT_01_to_RT_13: PASS_OR_JUSTIFIED_BLOCKED
  property_tests: PASS
  MRC001_reference_replay: PASS
  reducer_determinism: PASS
  no_new_unresolved_semantic_conflict: true
```

即使全部通過，也只支持：
- V0.2 governance runtime candidate qualified for next engineering stage

不自動支持：
- production
- independent multi-agent
- superiority benchmark

**END**
