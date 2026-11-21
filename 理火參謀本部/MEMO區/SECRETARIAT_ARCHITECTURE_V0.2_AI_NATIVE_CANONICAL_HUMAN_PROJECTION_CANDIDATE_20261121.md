# SECRETARIAT ARCHITECTURE V0.2｜AI-Native Canonical Plane × Human Projection
## Candidate Architecture / Staff-HQ data-plane reform, 2026-11-21

**Standing:** SECRETARIAT_V0.2_ARCHITECTURE_CANDIDATE / WORKING / NOT_RATIFIED / NON_HOST / NOT_ENGINEERING_VALIDATED.
**Origin:** user-supplied MEMO V0.1 (2026-11-21) plus historical 節電 / Artefak Nol — Versi Uji; reviewed against Secretariat Architecture V0.1, Meeting Record & Chat Surface V0.1, Decision Request V0.1 and Staff-HQ V0.3.0 working runtime.
**Adoption scope:** change only the *write and replay representation*, not who holds judgment, the L8 cognitive protocol, human authority or Council outcome.
**Compatibility:** Secretariat V0.1 remains current working baseline until explicit authorized adoption; historical session files are immutable. This is a proposed new architecture, not a claim that a deterministic service exists.

## 0. Thesis

> Human readability is a projection-time capability, not a write-time requirement for every canonical event.

No hidden-state transport, no inaccessible machine language, no black-box Secretariat. **Human auditability is mandatory** while repeated human-form prose is optional. The AI-native format is public, typed, stable, source-bound, and reconstructable.

~~~text
RAW / SOURCE (L0)
→ ORIGIN-DEClARED OBJECTS + QUALIFICATION
→ COMPACT AI-NATIVE CANONICAL EVENTS / GRAPH (L1)
→ DETERMINISTIC STATE + MATERIAL ROUTING (L2)
→ HUMAN PROJECTION ONLY WHEN USEFUL / REQUIRED (L3)
~~~

**Identity guarantee:** One material event has ONE canonical identity and provenance. Raw statement and L8 evidence are preserved by reference. All derivative views are disposable/reconstructable, never competing truths.

## 1. Four named planes (not ambiguous L0–L3)

| Stable name | Short ID | Contents | Authority |
|---|---|---|---|
| SOURCE_RAW | CP0 | human D0; external documents/data; original seat statements; expert/tool evidence; submitted L8 material record | preserves input bytes and origin; never decides standing |
| CANONICAL_TYPED | CP1 | admitted typed Event, Claim, Relation, Premise, SourceRef, Owner, Edge, Standing, MaterialDelta, Unknown, Authority, ReceiptRef, lineage | append-only qualified semantic history |
| REDUCED_OPERATIONAL | CP2 | current proposal/stance, live objections, minority HOLD, routing queue, pending wake, human gate, unresolved premise | deterministic projection; no new material judgment |
| HUMAN_PROJECTION | CP3 | Executive Brief, Decision Request, optional Audit/Chat/Round/Final views | readable projections from CP0/CP1/CP2; **NOT** canonical history |

Legacy naming collision must be recorded:
- Meeting Record V0.1 **L0 EVENT RECORD** maps to CP1 CANONICAL_TYPED (source attachments to CP0).
- Legacy **L1 ROUND RECORD** maps to CP2 reduced state plus, when material, CP1 event references (never independent history).
- Legacy **L2 CHAT SURFACE** maps to CP3.
- Legacy **L3 FINAL REPORT** maps to CP3.
- V0.3.0 **CANONICAL / OPERATIONAL / DERIVED** maps directly CP1 / CP2 / CP3; CP0 explicitly adds source preservation.
Do not silently rename an old event layer by the new number. Persist this correspondence in migration metadata.

## 2. Canonical object ownership and typed shape (candidate, not DAIL ratification)

**Allowed object roles:** EVENT, CLAIM, RELATION, PREMISE, SOURCE, OWNER, EDGE, STANDING, DELTA, UNKNOWN, AUTHORITY, RECEIPT. These are *semantic functions*, not a demand that every sentence create 11 objects. Only make an object when it carries an independently referable/materially distinct relation.

Example JSONL canonical event, illustrative, not a source fact:

~~~json
{
  "schema_version": "CP1-0.2-CANDIDATE",
  "event_id": "EV-041",
  "sequence_no": 41,
  "session_ref": "SESSION-EXAMPLE",
  "origin_actor_ref": "C",
  "origin_role": "CORE_SEAT",
  "semantic_type": "OBJECTION",
  "object_refs": ["OBJ-C-004", "CL-017"],
  "source_refs": ["SRC-009"],
  "premise_refs": ["PREM-004"],
  "relations": [{"type":"CHALLENGES","target_ref":"CL-017"}],
  "materiality": {"claim":"MATERIAL","owner_ref":"C","basis_refs":["PREM-004"]},
  "standing": "ACTIVE",
  "unresolved_refs": [],
  "prior_event_refs": [],
  "L8_evidence_ref": "L8-C-041",
  "original_statement_ref": "RAW-C-041",
  "persistence": "PENDING_WRITE"
}
~~~

Required:
1. stable session/event identity and monotonic sequence;
2. exact origin, role, owner, authority/scope reference where material;
3. typed relation/edge *with target*, not loose adjectives;
4. source provenance and qualified premise standing;
5. scope and materiality claim, owner-specific qualification, possible CONTESTED;
6. explicit UNKNOWN, surviving objection, alternative and minority HOLD where material;
7. prior/current version lineage and supersession (append-only);
8. L8 evidence pointer when material cognition invoked;
9. persistence truth (UNVERIFIED/PENDING/EXTERNAL_DURABLE only on successful Git write/readback);
10. raw original statement pointer where semantic loss would otherwise occur.

~~~text
SCHEMA_VALID != QUALIFIED
SUMMARY != HISTORY
UNKNOWN != FALSE
COMMENTARY_REWRITE != ORIGIN_SEMANTICS
DELIVERED != CONSUMED
CONSUMED != AGREED
VIEW != CANONICAL EVENT
~~~

Adapter may challenge origin type and route for qualified ownership; may not reclassify it silently. Machine compression must not erase source distinction, modality, value vs fact, owner authority or conditional status.

## 3. L8 / SGER / Receipt: compress duplication, not cognition

Original obligation remains:

~~~text
SEAT WAKE → LIHUOOS V1.4.2 L8
→ MAIN RETURN + TM + SGER + COMPACT RECEIPT
→ VERTICAL ACCEPTANCE → CANONICAL EVENT
~~~

**New serialization discipline:**
- A distinct material L8 cycle has one separately referenced full *observable* research record in CP0 (including actual R1/O9/T1/R2/O9/T2, R3+ when needed, meaningful rival candidates, counterforce, qualified Main Return, SGER and Receipt evidence).
- SGER is structured and **linked** to that cycle; do not create 5 prose restatements of the same conclusion.
- CP1 records one typed **material outcome event** with references to actual L8 evidence and supporting objects; an objection or stance change may require distinct semantic events, not forced aggregation.
- CP2 only derives current position; CP3 shows what human needs, generating expansion from reference only on audit request.
- This is a *representation* optimization. Do not claim that hidden chain-of-thought was collected; visible trace ≠ unseen internal computation.
- Non-material actions (validation, append, route, reduce, view render) do not invoke L8.
- Where a Compact SGER does not preserve a material alternative or change basis, preserve its raw statement in CP0 and a typed reference in CP1; **never discard important rationale in the name of token economy**.

## 4. Persistent layout, written once

Suggested new-version session layout (historical sessions unaffected):

~~~text
會議區/SESSION_<ID>/
  SOURCE/                   # optional raw blobs / source manifest
  CANONICAL/
    events_0001.jsonl       # CP1 append-only; rotate segments, no edits
    objects_0001.jsonl      # CP1 when distinct object types warranted
    source_index.json       # source/path/blob/hash, ownership and scope refs
  EVIDENCE/
    L8_<ID>.md              # CP0 observable L8 record only once
  PROJECTIONS/              # CP2/CP3, may be ephemeral or regenerated
    latest_state.json       # CP2 derived, never source of truth
    executive_brief.md      # CP3 produced only when justified
    decision_request.md     # CP3 mandatory at human gate
  README.md                 # short index to canonical refs, never second truth
~~~

**Git rule:** successful write and verified readback → EXTERNAL_DURABLE. Failed write → PERSISTENCE_GAP, never silently treat local view as durable. Historical records are append-only; correcting an event requires a new event/lineage, not a rewritten original. No mass migration of old Session histories.

## 5. Meaningful generation and stopping

**Generate a new canonical object only if it adds or qualifies a relation, source, premise, standing, delta, owner, authority, unknown, decision-relevant temporal/procedural change, or receipt.**

~~~text
NO NEW MATERIAL SEMANTICS
→ REFERENCE EXISTING OBJECT OR QUIET
NOT
→ NEW HUMAN-PROSE COPY
~~~

This is not "always shorter." Complex genuinely new relation may need more raw text or more distinct objects. Do not trim disagreement or suppress C's minority HOLD. Formal session triggers and First-Observation Clock A remain as in Staff-HQ V0.3.0.

## 6. CP2 is a pure projection

Reducer inputs are ORDERED QUALIFIED CP1 EVENT LOG + VERSIONED STATIC CONTRACTS, plus exact referenced CP0 content only for display or explicit validation, NOT final report prose. State includes:
- current Mandate / D1 standing and version, human gate/end policy;
- latest proposal and lineage;
- each CORE seat's current owned stance/version;
- open objections/minority HOLD/unknowns;
- material relations QUEUED / DELIVERED / CONSUMED / RESPONDED;
- pending re-wake, exact latest-version review and blockers;
- human action and termination state;
- F EXPERIMENTAL_SHADOW observed separately as research, not core coverage.

If a reducer can't reconstruct state without a final report, MRC-001 is not proven. If it creates materiality, owner, truth, vote, authority or release, it is invalid. Spec != implemented reducer.

## 7. CP3: projection on need, never automatic authority

Required render triggers:
- human asks to understand, summarize, audit, or see discussion;
- qualified **HUMAN_ACTION_REQUIRED** → immediately render one plain-language Decision Request;
- CHECKPOINT_ENDING / mandate exit → Executive Brief / decision handoff;
- authorized final delivery or explicit terminal report;
- human-facing important warning needing intervention.

Optional:
- small current-state indicator;
- short source index;
- requested Round/Chat Audit view.

Not required:
- prose restatement for every seat's internal L8;
- per-event ceremony;
- multiple round essays with no new material.

Render must show major objection, minority position, standing, key unknown and smallest human action; any nontrivial claim carries CP1 refs. **Human surface cannot disappear because humanization is expensive.** Human request, silence and result acceptance remain separate.

## 8. F Experimental Shadow compatibility

F is EXPERIMENTAL_SHADOW_SEAT, NOT_CORE7, nonvoting. Its original source, hypothesis, cost bearer, transfer, repair window and disconfirmation belong to CP0 research. If formally admitted by authorized source as **research/reference material**, CP1 event's origin and type must reflect that source; never convert F's signal into a CORE_SEAT stance. Affected CORE-6 owners re-wake under actual materiality and own their L8 and stance.

## 9. RLT scope and energy caveat

CP1 lineage provides suitable *input shape* for future RLT. It **does not** make RLT an active L9 feature.

Expected engineering advantages: fewer duplicated serialization steps, smaller re-ingestion surface, cleaner Git diff and lower risk of narrative thesis capture. No measured token savings or energy savings yet. Never assert fixed conversion from token reduction to electricity; hardware, model, caching, batching, provider still matter.

## 10. Testing and adoption

Acceptance tests:
- **CP-01 semantic preservation:** owner, source, premise, scope, authority, standing, objections, unknowns, lineage survive loss of all projections.
- **CP-02 replay:** CP1 + static qualified contracts rebuild same current state; no L3/prose dependence.
- **CP-03 mandatory human gate:** Decision Request is generated before WAITING_HUMAN.
- **CP-04 no Secretary capture:** derived report cannot edit event history/seat stance.
- **CP-05 no materiality compression:** schema validity cannot turn CONTESTED into MATERIAL or suppress minority HOLD.
- **CP-06 F shadow protection:** no F core vote, quorum or exact-version review counted.
- **CP-07 source audit:** preserved raw and L8 artifacts can be fetched; source hash/lineage, including failed Git write, remains truthful.
- **CP-08 economics:** count actual tokens, repeated parse/read/storage and process overhead before cost/energy benefits are claimed.

**Standing until independently verified:** ARCHITECTURE_PROPOSAL_READY, IMPLEMENTATION_PARTIAL_OR_NOT_STARTED, REDUCER_NOT_PROVEN, HOST_NOT_DEPLOYED.

**END｜SECRETARIAT ARCHITECTURE V0.2 CANDIDATE**
