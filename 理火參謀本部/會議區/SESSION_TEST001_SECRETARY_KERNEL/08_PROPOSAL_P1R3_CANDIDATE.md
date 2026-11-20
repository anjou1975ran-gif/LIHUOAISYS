
# PB-R005-01｜P1R3-CANDIDATE
## Secretariat Institution V0.1 Consolidated Candidate

**Standing:** UNDER_DELIBERATION / NOT CURRENT / NOT APPROVED  
**Derived from:** PB-R004-01 + R005 amendments

---

# 1｜Institutional frame

~~~text
SECRETARIAT
=
OPERATIONAL INSTITUTION

CANONICAL STATE
+
TRANSITION RULES
=
GOVERNANCE CORE
~~~

Secretariat is not a single cognitive agent.

Components:
- Process Kernel
- Canonical Record Keeper
- Expert Coordination Surface
- Report / View Renderer

Each component has typed permissions and non-authorities.

---

# 2｜Canonical state architecture

~~~text
CANONICAL:
  RAW INPUT EVENTS
  ADMITTED TYPED EVENTS
  IMMUTABLE VERSION / LINEAGE

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

~~~text
STORE ONCE
DERIVE MANY
~~~

Reducer replay test remains required before engineering closure.

---

# 3｜Typed event admission

CORE seat primary path:

~~~text
RAW STATEMENT
↓
ORIGIN-DECLARED OBJECTS
↓
SCHEMA VALIDATION
↓
CANONICAL TYPED EVENT
~~~

Formal seat output carries:

~~~yaml
DECLARED_OBJECTS:
  claims: []
  questions: []
  objections: []
  amendments: []
  new_paths: []
  consult_requests: []
  stance_revision: OPTIONAL
~~~

Audit channel:

~~~text
ADAPTER CLASSIFICATION CANDIDATE
!=
CANONICAL RECLASSIFICATION
~~~

Mismatch:

~~~text
CLASSIFICATION_MISMATCH
→ ORIGIN CONFIRM / CORRECT / DISPUTE
~~~

Correction creates a new event; no history rewrite.

Unstructured Human / Expert / External input is preserved first as RAW INPUT; interpretation remains explicitly qualified.

---

# 4｜CORE-6 responsibility tags

~~~text
N1:
BASIC_QUESTION
EXECUTIVE_CLARITY
USER_ACTION
EXPLANATION_GAP

A:
NEW_PATH
ALTERNATIVE
OPTION_SPACE

B:
FRAME
ARCHITECTURE
COORDINATE_SHIFT
UNOWNED_RESPONSIBILITY

C:
QUALIFICATION
EVIDENCE
CAUSALITY
AUTHORITY
STANDING

D:
ENGINEERING
IMPLEMENTATION
DEPENDENCY
TEST
RECOVERY

E:
COST
RESOURCE
TIME
MAINTENANCE
OPPORTUNITY_COST
~~~

Multiple tags may route to multiple seats.

Unowned:
~~~text
UNOWNED_RESPONSIBILITY
→ B + C + N1
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
MANDATORY OWNER MAP
~~~

Explicit target may add valid route but may not suppress mandatory route.

Required attestation:

~~~text
MANDATE TYPE
+
MATERIAL ISSUE TAGS
→ REQUIRED ATTESTATION SET
~~~

---

# 6｜Expert consultation

Eligibility and resource remain separated.

~~~text
CONSULT_ELIGIBLE
!=
RESOURCE_AVAILABLE
~~~

Secretariat validates workflow; expert does not own truth or issue closure.

---

# 7｜Executive Brief V0.1

~~~text
[TRUST STRIP]
重大反對：YES/NO + count
關鍵未知：YES/NO + count
現在需要你決定：YES/NO

[1] 這件事是什麼？
[2] 現在到哪裡？
[3] 有哪些路？
[4] 最大風險與反對
[5] 還不知道什麼？
[6] 現在要你做什麼？
~~~

Integrity:
- blocking / human action required cannot be folded
- material dissent remains counted even when collapsed
- minority != non-material
- unknown must remain visible
- important claims have expandable provenance
- Renderer does not freely select semantic priority

Optional:
~~~text
EXECUTIVE DELTA
=
WHAT CHANGED SINCE LAST CHECKPOINT
~~~

---

# 8｜Cost observation

Track:
- inference
- storage
- engineering
- maintenance
- human review

Only record actual telemetry when available.

TEST-001 first observation shows R001-R004 recorded 52 unique event IDs in Git ledgers, with six active CORE seats recorded in each of the first four rounds, zero external expert calls, and two human intervention events.

This does not establish production cost.

Open cost / process issues:
- O-E-001 total cost unknown
- O-E-002 Meaningful Wake not yet demonstrated
- O-D-002 reducer replay not yet executed

---

# 9｜Session lifecycle and ending

States:

~~~text
OPEN
PAUSED
WAITING_EXTERNAL
WAITING_HUMAN
EXIT_CANDIDATE
ENDED
~~~

~~~text
CLOSURE_SWEEP
!=
MANDATE_EXIT
!=
HOLD
!=
PAUSE
!=
SESSION_END
~~~

Future D1 must freeze:

~~~yaml
end_policy:
  - AUTO_ON_MANDATE_EXIT
  - REQUIRE_HUMAN_END
~~~

Legal END reasons candidate:
- MANDATE_COMPLETED
- HUMAN_STOP
- MANDATE_WITHDRAWN
- SUPERSEDED_BY_NEW_SESSION

END is an explicit terminal event.

~~~text
SESSION ENDED
!=
HUMAN APPROVED RESULT
~~~

Legacy session with no frozen End Policy must not be retroactively treated as AUTO.

---

# 10｜Remaining open / maintained

~~~text
O-D-002
Reducer replay engineering test not executed

O-E-001
Total deliberation cost unknown

O-E-002
Meaningful Wake not yet demonstrated
~~~

These are now candidates for Closure Sweep classification:
- concept-blocking?
- engineering validation gap?
- benchmark gap?
- post-V0.1 work?

**END**
