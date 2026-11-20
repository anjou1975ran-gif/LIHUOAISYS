
# PB-R004-01｜P1R2-CANDIDATE
## Secretariat Institution × Replayable Governance × Executive Priority × Session Ending

**Standing:** UNDER_DELIBERATION / NOT CURRENT / NOT APPROVED  
**Derived from:** PB-R003-01 + R004 amendments

---

# 1｜Governance center

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

---

# 2｜Mandatory primary routing V0.1

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

Candidate mappings:
- OBJECTION → target owner + origin owner + typed responsibility owner
- CONSULT_RETURN → request origin + linked issue owner + waiting seats
- PROPOSAL_VERSION_CHANGE → seats with affected stance + affected open issue owners
- STANCE_REVISION → Position Ledger + cited issue owners
- HUMAN_MANDATE_CHANGE → CORE-6 + all open issue owners
- ENDING_CANDIDATE → relevant seat attestations + Process Kernel + Renderer

---

# 3｜Replayable reducer

~~~text
REPLAY(GENESIS, ORDERED_CANONICAL_EVENTS)
==
RECORDED_CURRENT_STATE
~~~

Otherwise:
~~~text
STATE_DIVERGENCE
~~~

Natural-language-to-typed-event admission remains OPEN because classification itself can affect routing.

---

# 4｜Executive priority

~~~text
P0 HUMAN_ACTION_REQUIRED
P1 BLOCKING
P2 MATERIAL_DISSENT
P3 CRITICAL_UNKNOWN
P4 SURVIVING_OPTIONS / MATERIAL_TRADEOFF
P5 INFORMATIONAL
~~~

Rules:
- minority != non-material
- blocking / human-action-required cannot be folded below default view
- folded dissent still counts in visible totals
- priority must derive from typed state / mandate rule / seat attestation, not free renderer choice

Executive Delta View may show changes since last checkpoint.

---

# 5｜Cost observation

Track:
- active seats
- output refs
- canonical events
- derived views
- expert calls
- wakes
- duplicate / stale rejection
- human interventions

Token / latency / external costs only when actually available; otherwise UNKNOWN.

---

# 6｜Session lifecycle / ending

Candidate states:

~~~text
OPEN
PAUSED
WAITING_EXTERNAL
WAITING_HUMAN
EXIT_CANDIDATE
ENDED
~~~

~~~text
CLOSURE SWEEP
!=
MANDATE EXIT
!=
HOLD
!=
PAUSE
!=
SESSION END
~~~

Legal END reasons candidate:
- MANDATE_COMPLETED
- HUMAN_STOP
- MANDATE_WITHDRAWN
- SUPERSEDED_BY_NEW_SESSION

MANDATE_COMPLETED candidate:

~~~text
MANDATE EXIT STANDING EXISTS
+
NO PENDING MANDATORY ROUTE
+
FINAL REPORT RENDERABLE
+
OPEN BLOCKERS DISCLOSED
→
EXIT_CANDIDATE
~~~

END must be represented by explicit terminal event.

~~~text
SESSION ENDED
!=
HUMAN APPROVED RESULT
~~~

End policy remains under deliberation:
- AUTO_ON_MANDATE_EXIT
- REQUIRE_HUMAN_END

---

# 7｜Open issues

- O-N1-001
- O-C-002
- O-C-003
- O-C-004
- O-D-001
- O-D-002
- Q-N1-002
- O-E-001
- O-B-002
- O-C-005
- O-D-003
- Q-SEC-001

**END**
