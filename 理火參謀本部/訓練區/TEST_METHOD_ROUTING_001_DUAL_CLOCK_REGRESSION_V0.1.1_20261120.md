# TEST_METHOD_ROUTING_001｜Dual-Clock Regression V0.1.1
## 第一觀察之前選心法；議事中途才按需請外援

**Date:** 2026-11-20
**Standing:** `TEST_DESIGN_CANDIDATE / NOT_RUN / NO_RESULTS / NOT_RUNTIME_RATIFIED`
**Supersession:** This test plan **revises the prospective procedure** in `TEST_METHOD_ROUTING_001_PROFESSIONAL_TRIGGER_LIVE_REGRESSION_V0.1_20261120.md`. The V0.1 file remains historical evidence, not silently replaced.
**Source patch:** `理火參謀本部/MEMO區/PATCH_PROFESSIONAL_METHOD_DUAL_ROUTING_V0.1.1_WORKING_20261120.md`.
**Audit origin:** `METHOD_ROUTING_NEGATIVE_SPECIMEN_001`.
**Current mandate:** NONE. **No test has started.**
**Identity:** On one ChatGPT session, `SAME_MODEL_MULTI_ROLE_REFERENCE`. External professional execution can only be claimed when actual provider invocation and return exist.

## 1｜Test architecture: two separate clocks
```text
TEST A — PRE-OBSERVATION METHOD ROUTING
D0 / D1 / ISSUE CLASSIFICATION
→ CORE SEAT CONTRACT MATCH
→ POSSIBLE METHOD DELTA SCREEN
→ SELECT METHOD OR NO_METHOD_WITH_REASON
→ VERSION LOCK
→ FIRST OBSERVATION
→ FIRST MATERIAL L8
→ SEAT STANCE

TEST B — MID-DELIBERATION PROFESSIONAL CONSULT
COUNCIL MATERIAL EVENT / NEW PROFESSIONAL GAP
→ SEAT-OWNED SUPPORT REQUEST
→ SECRETARIAT CHECKS AUTHORIZATION STATE
  AND ROUTES WITHIN DELEGATED SCOPE
  OR REFER TO AUTHORIZED OWNER / HUMAN
→ SCOPED SOURCE / SPECIALIST / AGENT
→ REAL RETURN + PROVENANCE + LIMITS
→ AFFECTED SEAT CONSUMPTION
→ NEW L8 WHEN MATERIAL
→ OWNED CHANGE / RETAIN / HOLD
```
**Temporal hard requirement:** For each selected Method, `METHOD_SELECTION_EVENT < FIRST_OBSERVATION_EVENT < L8_INITIAL_MATERIAL_JUDGMENT`. An afterward method review cannot retroactively pass TEST A.

**Note on NEW issues:** When a later Material Issue opens a new cognitive invocation, its own METHOD_DELTA screen, if relevant, still precedes that affected seat's **next L8 for the new issue**. This does not convert a post-hoc method review of the old issue into a PRE-first-observation pass.

## 2｜New test prompt: optional, not pre-authorized
> 一座城市的社區若想讓閒置的私人停車位按小時提供給附近居民使用，能否形成一種合法、有人願意付費，也能讓社區管理者接受的共享服務？先做開放概念探索，不指定既存商業模式，也不要求任何席位一定調用心法或專業 Agent。請先依各責任席判斷是否要在第一觀察之前選擇心法，再進入實質 L8。若議事中途自然出現新的 Material 專業缺口，才評估有無必要申請外援；沒有必要也請有理由地不調用。

This prompt is illustrative; no advance activation, no fixed P0, no prescribed Seat×Method mapping. Human may use a different clean new domain.

## 3｜Setup / common controls
1. Human explicitly opens future Session; D0 preserved; D1 mandate type, scope, human intervention, exit and human approval standing recorded. `CONTINUE != CONSENT`.
2. `P0=NONE` unless Human supplies or authorizes P0. No prior Council stance is fed to a seat on its first pass.
3. Before any material first-pass judgment, only supply each seat D0/D1, own Seat Contract, qualified context and a **minimal Method Atlas index** (not every Pack's content).
4. Actual relevant Method Packs, if selected, are read from Git at exact ref/SHA; save selection reason and a first-observation record before the affected seat L8.
5. Do not provide unselected methods as hidden common prompt context. N1 may act as common-sense/no-method control if that choice is justified by its issue.
6. Mark exact execution identity and source-provenance, not a hypothetical provider's simulated identity.
7. Secretariat can check authorization and route inside *existing* delegation; it cannot grant professional hiring, external data disclosure, funds or regulated professional standing.
8. No unauthorized contact, payment, contract, private data sharing, software deployment or parking-site access.

## 4｜TEST A — PRE-L8 Method Choice and First-Observation Effect

### Stage A0｜Method Choice before Material L8
For each scoped seat:
```yaml
PRE_L8_METHOD_DECISION_TEST:
  seat: N1|A|B|C|D|E
  source_issue: HUMAN_MANDATE_OR_NEW_ISSUE_REF
  seat_responsibility_ref: REQUIRED
  candidate_method_delta: "What change in first observation is plausible?"
  decision: SELECT_METHOD | NO_METHOD_WITH_REASON
  selected_method_git_path: null
  selected_method_blob_or_commit: null
  method_version: null
  rejected_alternatives_brief: REQUIRED
  decision_order: BEFORE_FIRST_OBSERVATION
  standing: TEST_OBJECT_ONLY
```
- Secretary may locate indexed packs / lock a blob under delegated read access. **It must not choose a seat stance or assign a mandatory school**.
- No Method is allowed as a genuinely reasoned choice; `NO_METHOD` does not imply `NO_EXPERT_NEEDED` for later events.
- “Law → always Law Pack”, “Economics → always Economics Pack”, “All seats → 1 Agent each” are failure signatures.

### Stage A1｜First Observation
Seat records which analysis unit, causal lens, evidence type or blind spot became visible before R1. Then invokes LIHUOOS L8, origin-declares own objects, emits SGER/receipt and canonical seat event according to then-current Runtime. Do not claim microscopic attention control.

### Stage A2｜A audit
Check order in Git evidence, not retrospective prose. Ask whether selected pack actually shaped the first observation (if no discernible difference, `METHOD_DELTA_UNDEMONSTRATED` rather than forced PASS). Candidate `NO_METHOD` must show appropriate reason, not merely silence.

## 5｜TEST B — Mid-Council Professional Consult (only when naturally triggered)

### Stage B0｜New professional gap
Council events and L8 uncover new material issue beyond existing scope. A Seat claims why it matters and **whether** real professional input could change rights, validity, architecture or economics; choose `REQUEST` or `NOT_REQUIRED_WITH_REASON`. Do not pre-create fabricated expert needs for test compliance.

### Stage B1｜Secretariat authority check, route, version lock
```yaml
PROFESSIONAL_CONSULT_TEST:
  issue_ref: NEW_MATERIAL_EVENT
  origin_seat: AFFECTED_RESPONSIBILITY_OWNER
  request_ref: REAL_PROFESSIONAL_SUPPORT_REQUEST_OR_NONE
  material_gap_reason: REQUIRED_IF_REQUEST
  support_type: SOURCE_RETRIEVAL | SCOPED_SPECIALIST_AGENT | HUMAN_LICENSED_SPECIALIST
  authorization_state: AUTHORIZED_WITHIN_DELEGATION | PENDING_AUTHORIZED_OWNER | FORBIDDEN
  authority_owner_ref: REQUIRED_IF_EXTERNAL_ACTION
  specialist_provider_and_version: REQUIRED_IF_ACTUALLY_CALLED
  return_ref: REAL_RETURN_OR_NONE
  affected_seat_consumption_ref: ONLY_IF_RETURN_EXISTS
```
- Existing public/source searches can be routed when permitted, with real provenance; they aren't independent Professional Agents.
- External paid/regulated/sensitive work with no delegated authorization routes to human/qualified owner. `SECRETARIAT CHECKS AUTHORIZATION STATE`; **it does not create authorization**.
- An actual specialist's output stays `EVIDENCE / METHOD_SHAPED_ANALYSIS / EXPERT_OPINION` and never becomes a Council stance.

### Stage B2｜Owned seat response
If a real return exists and is material, affected CORE Seat must consume it and invoke its **own new L8**, producing `CHANGE / RETAIN_WITH_REASON / CHALLENGE / HOLD`; quiet when no material delta.
If an external consultation cannot be authorized, valid result is `PENDING_OWNER` or `NO_AGENT` — **not a fabricated return**.
If no material professional gap emerges naturally: B = `NOT_TRIGGERED_WITH_REASON`, not FAIL for absence of expert call.

## 6｜Pass/fail ledger — two tests, not one

| ID | Test dimension | PASS evidence | FAIL evidence |
|---|---|---|---|
| A-01 | Method timing | choice/no-method and version decision logged **before** first substantial observation/L8 | pack added after first L8 but labeled first-step |
| A-02 | Seat-owned method need | seat first-observation delta reason; Secretary only routes | Secretary chooses thesis; keyword→auto-discipline |
| A-03 | Git version lock | exact pack path, ref/SHA and selected lens | unversioned method name or unverified load |
| A-04 | First-observation influence | changed unit/evidence/causal blind spot anchored to selected Method | only post-hoc style/answer decoration |
| A-05 | Legitimate NO_METHOD | reason and bounded unknowns; no forced pack | every seat forced to cite at least one pack |
| B-01 | Natural Material Professional Gap | linked new issue/unknown + material dependency | invented expert need merely to satisfy test |
| B-02 | Source/Expert distinction | source URL, method, agent identity separated | role-play specialist counted as independent Agent |
| B-03 | Authorization standing | delegated scope or real owner referral | Secretariat self-issues approval |
| B-04 | Return provenance | actual provider, task, scope, version, limits | imagined professional return |
| B-05 | CORE Seat consumption | return ref → own L8 → changed or reasoned-retained stance | expert output pasted as Council stance |
| B-06 | NO_AGENT/QUIET | recorded reason for no gap, no call or no material wake | all six forced to invoke an Agent |
| G-01 | Historical non-mutation | CASE-002 original blobs unchanged | retroactive new Method refs in original L8 |
| G-02 | Honest result separation | A and B separate statuses | calling A PASS means B automatically PASS |

## 7｜Result levels (no auto-promotion)
```yaml
TEST_METHOD_ROUTING_001_RESULT:
  TEST_A_PRE_OBSERVATION:
    status: NOT_RUN
    requires: [PRE_L8_DECISION,VERSION_LOCK,FIRST_OBSERVATION,L8_ORDERED_TRACE]
    allowed_results: [PASS,FAIL,PARTIAL,NOT_RUN]
  TEST_B_MID_DELIBERATION:
    status: NOT_RUN
    requires_if_triggered: [NEW_GAP,SEAT_REQUEST,DELEGATION_CHECK,REAL_RETURN,SEAT_CONSUMPTION]
    allowed_results: [PASS,FAIL,HOLD_UNAUTHORIZED,NOT_TRIGGERED,NOT_RUN]
  NO_METHOD_CONTROL: NOT_RUN
  NO_AGENT_CONTROL: NOT_RUN
  FORMAL_RUNTIME_VALIDATION: NOT_CLAIMED
  INDEPENDENT_AGENT_DEPLOYMENT: NOT_CLAIMED
  METHOD_EFFECTIVENESS_PROVEN: NOT_CLAIMED
  CASE_002_HISTORY: PRESERVED
```

### Possible clean outcome
- C selected a law Method before first-observation L8; E an economics lens; A communication/social methods; N1 NO_METHOD — **only if each actually selects based on that issue**, not because this spec tells them to.
- D later detects a security issue exceeding the current Method Pack and requests actual engineering support — **only if the issue genuinely appears**. If no actual specialist is available/authorized, record pending owner and do not invent B PASS.
- If all seats reasonably use NO_METHOD and no material expert gap occurs, record limited meaningful `NO_SUPPORT` outcomes; this is not automatically proof of Method's value.

## 8｜Closure/next move
The corrected test can be initiated only upon a new Human mandate. No fixed Council rounds, no outcome preset, no mandatory number of calls, no forced winner. Track both event clocks and compare actual first-observation evidence; test quality gains require a separate repeated/control comparison.

**Core invariant:** `METHOD BEFORE FIRST LOOK; PROFESSIONAL HELP WHEN NEW GAP APPEARS; RETURN BELONGS TO SOURCE, STANCE BELONGS TO SEAT.`
