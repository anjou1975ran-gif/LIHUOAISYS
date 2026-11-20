# LIVE REGRESSION｜TEST_METHOD_ROUTING_001
## 當 CORE Seat 自然發現專業缺口，能否申請 Method／專業 Agent，並保有自己的判斷？

**Date:** 2026-11-20
**Standing:** TEST_DESIGN_CANDIDATE / NOT_RUN / NO_RESULTS / NO_RUNTIME_RATIFICATION
**Origin:** `METHOD_ROUTING_NEGATIVE_SPECIMEN_001`, `MEMO_PROFESSIONAL_TRIGGER_METHOD_ROUTING_V0.1_WORKING_20261120`.
**Scope:** New Staff-HQ concept/reference case after separate human instruction; do not reopen CASE-002 to retrofit Method.
**Important:** Test may openly acknowledge "we are testing Method Routing". A hidden exam is neither necessary nor preferable to provenance.

## 1｜測試目標，不是測叫了多少個 Agent
```text
RIGHT MATERIAL PROFESSIONAL GAP
→ SEAT OWNED SUPPORT REQUEST (or NO_SUPPORT reason)
→ SECRETARIAT ROUTING / AUTHORITY SCOPE
→ VERSION-LOCKED METHOD or ACTUAL SPECIALIST
→ SCOPED RETURN / PROVENANCE
→ MATERIALITY ASSESSMENT
→ AFFECTED SEAT CONSUMES AND OWNS CHANGE / RETENTION
```

Success must also include:
```text
NO MATERIAL PROFESSIONAL GAP
→ NO PROFESSIONAL AGENT
→ REASON RECORDED
```

**Don't count:** independent agents, legal opinions, real market approval, deployed tool calls or user approval unless corresponding evidence exists.

## 2｜Clean suggested new test prompt (no prior P1)

> 一座城市的社區若想讓閒置的私人停車位按小時提供給附近居民使用，能否形成一種合法、有人願意付錢、對社區管理者也有好處的共享服務？先只做概念探索，從零形成問題，不指定產品答案，也不要求任何席位一定請專家。請依參謀本部程序議事，並在自然出現真正專業缺口時自行判定需要哪種 Method 或專業支援。

This is an **illustrative** next human problem; it is not a mandate automatically issued now. Other unrelated subject is equally valid provided it contains natural professional unknowns. Unlike CASE-002, it has no inherited business proposal. Test location and exact project boundary are chosen by the human initiating that future session.

Potential unprompted gaps could include:
- who legally may grant parking access versus the parking operator;
- accident/access liability, insurance and on-site authorization;
- two-sided booking/cancellation and congestion economics;
- automated gate/sensor data privacy and engineering security;
- stakeholder governance and fair sharing.

These are **possible gaps**, not a target list that seats are required to recite.

## 3｜Version / setup lock before the test
1. Human opens a new Session, gives D0; Secretary registers D1 as confirmed or unconfirmed without inventing approval.
2. Set `P0=NONE` unless Human explicitly specifies. No prior solution or desired number of calls.
3. Freeze original reference snapshots of applicable V0.2 Staff-HQ and Project Core, LIHUOOS, Method Atlas README, FIRST STEP MEMO, and source git blob SHAs/versions. **Do not load all packs** before the seat's first gap screen.
4. Read current Git Method Packs only after a specific Seat/Issue plausibly triggers them. Do not write Project-only PATCH bytes to Git merely to create a test reference.
5. Mark `execution_identity`: CHAT_NATIVE_SINGLE_MODEL / ACTUAL_SEPARATE_SPECIALIST / HUMAN_PROFESSIONAL, based on truth; no silent switching.
6. No contacts, data transfers, professional hiring, app deployment or spending without separate human authorization.

## 4｜Procedure
### T0 — initial responsibility seats
- Seat sees human problem, own contract, qualified reference and unknowns. No other seat stance fed as an initial frame.
- On materially important unknown, seat first records `PROFESSIONAL_GAP_ASSESSMENT`:
  `issue_ref / issue_materiality / possible_first_observation_delta / current_known_input / support_needed?`.
- Some seats can legitimately return `NOT_REQUIRED_WITH_REASON`.

### T1 — request / decision
- If needed, owner Seat originates `PROFESSIONAL_SUPPORT_REQUEST` with exact unresolved question.
- Secretary checks mandate, subject, data sensitivity, payment, confidentiality, tool availability and qualification owner; may route permitted Git Method Pack selection within scope.
- If a real external Agent would require approval not presently delegated: status `PENDING_AUTHORIZED_OWNER`, no fake return.
- Record available candidate methods and why one is selected or declined; include path, `git ref`, blob SHA and scoped first-observation hypothesis.
- `NO_METHOD_OR_AGENT` is an explicit admissible choice when justified.

### T2 — return and affected-seat consumption
- For Method-only support: return is a **versioned Method Input** describing changed unit/lens/blind spot, not Expert opinion.
- For external source: record actual retrieved facts and provenance; not a Method merely because it used a search query.
- For actual specialist: record provider identity, scope, source, date, declared credentials if relevant, detailed caveats and separate Specialist Return. If only same-model special-role output, label SAME_MODEL_SPECIALIST_REFERENCE, no independent-agent claim.
- Route qualified material to affected CORE Seat; run its own LIHUOOS cycle if material. Output `STANCE_CHANGED / POSITION_RETAINED_WITH_REASON / CHALLENGE / HOLD`.
- Check whether that own response changes another seat's material issue; no forced all-six re-wake.

### T3 — audit, not winner assignment
- Verify request, route, version, specialist material and affected-seat own event chain can be reconstructed from recorded Canonical Events.
- If no material benefit, record `NO_MATERIAL_METHOD_DELTA` and whether the support was unnecessary; do not fake success.
- A concept session may legitimately finish with `NO_PROPOSAL`, multiple path candidates or HOLD.
- No fixed number of Council rounds.

## 5｜Regression cases and failure signatures

| ID | Test | Required observable | Pass / fail |
|---|---|---|---|
| MR-T001 | Material expert gap screen | Seat or Secretary identifies issue's actual expertise dependency, shows why it matters | PASS if reason; FAIL if only generic domain name |
| MR-T002 | Right method, not keyword | Chosen field/lens changes first observation or qualifications | PASS with plausible issue-specific delta; FAIL if legal/econ always called by keywords |
| MR-T003 | Method version lock | Git path + branch/commit or blob SHA + version + chosen lens | PASS if traceable before consumption; FAIL if nameless "used economics" |
| MR-T004 | Secretary neutrality & authority | Request routes to method/source/agent or owner without Secretary owning thesis | PASS if exact ownership and authorization preserved |
| MR-T005 | Specialist return scoped | Evidence vs Method analysis vs Expert opinion distinguished, actual identity not exaggerated | FAIL if "Expert said so" becomes Council stance |
| MR-T006 | CORE Seat consumption | Explicit Return ref → Seat new L8 if material → own change or reasoned retention | PASS if causality visible, not just attached expert memo |
| MR-T007 | Correct non-call | N1 or another seat can record no professional material gap and no Agent | PASS if reasoned, FAIL if mandatory one Agent per seat |
| MR-T008 | Control / method shift | Compare N0/no method and method-selected lens on same qualified question, check different first observations & blind spots without demanding different final answer | NOT_PROVEN unless actual comparison performed |
| MR-T009 | No authority overreach | External professional needing permission/cost/client disclosure remains pending human/owner | FAIL on unapproved external work; PASS if correct HOLD |
| MR-T010 | No history rewrite | Original CASE-002 all Events/Seat L8/SGER preserved while new tests append their own events | PASS by Git blob/commit comparisons |
| MR-T011 | Meaningful quiet | No further Agent/Seat called when return irrelevant or no new material | PASS if reasoned/no fake rounds |

## 6｜Two success levels, do not collapse
```yaml
RESULT_LAYERS:
  METHOD_ROUTING_REFERENCE_PASS:
    requires: [issue_scoped_gap,method_selection_reason,version_lock,method_input,seat_consumption_or_reasoned_no_support]
  PROFESSIONAL_AGENT_LIFECYCLE_PASS:
    requires: [actual_provider_identity,authorized_activation,specialist_return_provenance,scope,affected_seat_consumption]
  INDEPENDENT_MULTI_AGENT_VALIDATED:
    requires: REAL_INDEPENDENT_PROVIDER_AND_REPRODUCIBLE_EVIDENCE
    cannot_infer_from: [same_model_acted_as_specialist,git_receipts]
  SPECIALIST_EFFECTIVENESS_PROVEN:
    requires: REPEATABLE_METHOD_SHIFT_AND_QUALITY_COMPARISON
    cannot_infer_from: [one_good_sounding_answer]
```

An actual professional Agent is not required if the task can be responsibly addressed with a versioned Method Pack and qualified public sources. In that case, `METHOD_ROUTING_REFERENCE_PASS` could be supported, while `PROFESSIONAL_AGENT_LIFECYCLE_PASS` remains `NOT_TESTED`.

## 7｜Test record template and failure names
```yaml
METHOD_ROUTING_TEST_RESULT:
  test_id: MR-LIVE-001
  session_id: FUTURE_SESSION_REF
  human_mandate: FUTURE_REF
  professional_gap_events: []
  support_requests: []
  method_selections_and_blob_refs: []
  actual_specialist_calls: []
  specialist_returns: []
  seat_consumption_refs: []
  no_support_with_reason: []
  uninvolved_seats_quiet: []
  authority_rejections_or_holds: []
  result: NOT_RUN
  failure_modes:
    - METHOD_ROUTING_COMPLIANCE_THEATER
    - DOMAIN_KNOWLEDGE_AS_METHOD_FALLACY
    - EXPERT_RETURN_AS_COUNCIL_STANCE
    - SECRETARIAT_EXPERT_THESIS_CAPTURE
    - UNVERSIONED_METHOD_INPUT
    - UNAUTHORIZED_AGENT_CALL
    - FALSE_PROVIDER_INDEPENDENCE
```

## 8｜What to do with real findings
- If no material gap was detected and reason is credible, DON'T manufacture an expert call. Record NO_SUPPORT as valid.
- If clearly material professional gap appeared but Seat and Secretary ignored it, record fail with event evidence and open new backlog, not fake retroactive request.
- If specialist returned but no Seat owned response, record `EXPERT_RETURN_NOT_CONSUMED` and reopen only affected seats.
- If it works, treat as a **reference specimen for a candidate relation**, not auto-ratified V0.2 Runtime or proof that experts increase quality.

**Last line:** The PASS criterion is **correct source/authority/Method → material seat-owned judgment**, not more meetings or more Agents.
