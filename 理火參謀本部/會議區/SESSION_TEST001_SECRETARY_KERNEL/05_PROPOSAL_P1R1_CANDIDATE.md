
# PB-R003-01｜P1R1-CANDIDATE
## Secretariat Institution × Deterministic State × Executive Integrity

**Standing:** UNDER_DELIBERATION / NOT CURRENT / NOT APPROVED  
**Derived from:** PB-R002-01 + R003 amendments

---

# 1｜Frame

~~~text
SECRETARIAT
=
INSTITUTION

NOT
SINGLE COGNITIVE AGENT
~~~

---

# 2｜Component permission boundary

## PROCESS KERNEL
Can:
- validate schema
- validate legal state transition
- apply deterministic primary routing
- reject duplicate / stale / illegal transition

Cannot:
- decide truth
- decide stance
- decide persuasion validity
- decide objection validity

## CANONICAL RECORD KEEPER
Can:
- append canonical event
- preserve immutable refs
- index version lineage

Cannot:
- rewrite prior event
- resolve issue
- summarize away dissent

## EXPERT COORDINATION SURFACE
Can:
- validate consultation request schema
- check duplicate / mandate scope / resource state
- issue expert brief
- register return

Cannot:
- decide expert correctness
- close originating issue
- rewrite requester question

## REPORT / VIEW RENDERER
Can:
- render typed state
- paraphrase for audience
- attach provenance

Cannot:
- mutate canonical state
- change standing
- omit mandatory dissent / unknowns
- freely choose semantic priority

---

# 3｜Canonical / operational / derived

~~~text
CANONICAL:
  IMMUTABLE EVENT LEDGER

OPERATIONAL:
  DETERMINISTIC STATE REDUCER
  CURRENT STATE INDEX
  ROUTING QUEUE

DERIVED:
  ROUND VIEW
  CHAT VIEW
  EXECUTIVE VIEW
  AUDIT VIEW
  FINAL REPORT
~~~

---

# 4｜Reducer minimum contract

~~~yaml
EVENT_ENVELOPE:
  event_id: REQUIRED
  event_type: REQUIRED
  origin_actor: REQUIRED
  target_refs: []
  object_refs: []
  proposal_version_ref: REQUIRED_WHEN_APPLICABLE
  created_at_seq: REQUIRED
  dedupe_key: REQUIRED

REDUCER:
  input: [prior_state_ref, event_ref]
  output:
    - next_state_ref
    - transition_status
    - generated_route_refs
    - rejection_reason_if_any

TRANSITION_STATUS:
  - APPLIED
  - DUPLICATE
  - STALE_VERSION
  - ILLEGAL_TRANSITION
  - SCHEMA_INVALID
  - NO_STATE_CHANGE
~~~

---

# 5｜Primary routing

~~~text
PRIMARY ROUTE
=
EVENT TYPE RULE
+
OBJECT TARGET
+
MANDATORY OWNER MAPPING
~~~

Explicit target may add valid routes but may not suppress mandatory routes.

Mandatory owner / route map remains OPEN for R004.

---

# 6｜Expert consultation

Eligibility:

~~~text
OPEN KNOWLEDGE_OR_EVIDENCE_GAP
+
REQUESTER DECLARES QUALIFIED MATERIAL INSUFFICIENT
+
QUESTION / DOMAIN / SCOPE SPECIFIED
→
CONSULTATION_ELIGIBLE
~~~

Resource availability is separate from eligibility.

~~~text
ELIGIBLE + RESOURCE_LIMIT
→ HOLD_RESOURCE / HUMAN_REVIEW_REQUIRED

NOT
NO_EXPERT_NEEDED
~~~

---

# 7｜Seat-attested exit

~~~text
SECRETARY CHECKS STRUCTURAL COMPLETENESS
+
RELEVANT SEATS ATTEST THEIR OWN DOMAIN
+
UNRESOLVED BLOCKERS REMAIN VISIBLE
→
EXIT STANDING MAY BE GENERATED
~~~

Relevant seat owner map remains OPEN.

---

# 8｜Executive View

Minimum Boss Brief:

1. 這件事是什麼？
2. 現在最重要的結論是什麼？
3. 還有哪些可選路？
4. 最大風險 / 最大反對是什麼？
5. 還有什麼不知道？
6. 現在要我做什麼？

Trust Strip:

~~~text
仍有重大反對：YES / NO
仍有關鍵未知：YES / NO
是否需要老闆現在決定：YES / NO
~~~

Integrity:

~~~text
EXECUTIVE CLAIM → PROVENANCE REF
OPEN MATERIAL DISSENT → DISCLOSURE REQUIRED
UNKNOWN → DISCLOSURE REQUIRED
~~~

Disclosure may be folded but not converted to zero.

Priority rule remains OPEN; Renderer may not freely choose priority.

---

# 9｜Cost accounting

Track separately:

~~~text
INFERENCE COST
STORAGE COST
ENGINEERING COST
MAINTENANCE COST
HUMAN REVIEW COST
~~~

No claim yet that P1R1 is cheaper overall.

---

# 10｜Open issues

- O-N1-001 Executive readability only partially resolved
- O-C-002 Exit authority partially resolved
- O-C-003 Translation authority partially resolved
- O-C-004 Renderer omission partially resolved
- O-D-001 Record duplication partially resolved
- O-D-002 Reducer spec needs replay test
- Q-N1-002 Executive trust partially resolved
- O-E-001 Total cost remains unknown
- O-B-002 Target assignment capture OPEN
- O-C-005 Executive priority selection authority OPEN

**END**
