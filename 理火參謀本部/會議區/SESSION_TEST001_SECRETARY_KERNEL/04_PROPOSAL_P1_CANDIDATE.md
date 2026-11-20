
# PB-R002-01｜P1-CANDIDATE
## Secretary Institution + Canonical Event Architecture

**Standing:** UNDER_DELIBERATION / NOT CURRENT / NOT APPROVED  
**Derived from:** P0 + R001 objections + R002 amendments

---

## 1. Secretary Institution

~~~text
SECRETARY INSTITUTION
├─ PROCESS KERNEL
│  deterministic state transition / routing
├─ CANONICAL RECORD KEEPER
│  append-only canonical events
├─ EXPERT COORDINATION SURFACE
│  procedural consultation workflow
└─ REPORT / VIEW RENDERER
   read-only derived views
~~~

No component receives truth / stance / final decision authority.

---

## 2. Data model direction

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

Round / Chat / Report do not create new canonical truth merely by rendering.

---

## 3. Expert consultation candidate rule

~~~text
OPEN KNOWLEDGE_OR_EVIDENCE_GAP
+
REQUESTER DECLARES CURRENT QUALIFIED MATERIAL INSUFFICIENT
+
QUESTION_DOMAIN_SCOPE_SPECIFIED
→
CONSULTATION_ELIGIBLE
~~~

Secretary denial reasons limited to:
- DUPLICATE
- SCHEMA_INCOMPLETE
- CLEARLY_OUT_OF_MANDATE
- RESOURCE_LIMIT_REQUIRES_HUMAN_REVIEW

~~~text
EXPERT ELIGIBILITY
!=
RESOURCE AVAILABILITY
~~~

---

## 4. Executive View candidate

Boss Brief minimum questions:

1. 這件事是什麼？
2. 現在最重要的結論是什麼？
3. 還有哪些可選路？
4. 最大風險 / 最大反對是什麼？
5. 還有什麼不知道？
6. 現在要我做什麼？

Candidate integrity rules:

~~~text
EXECUTIVE CLAIM → PROVENANCE REF
OPEN MATERIAL DISSENT → MANDATORY DISCLOSURE
UNKNOWN → MUST NOT BE SILENTLY OMITTED
~~~

---

## 5. Cost controls

- relevant-context delivery instead of full-history reinjection
- deduplicated wake per target/version/material delta
- store once / reference many
- derived view rendering on demand
- expert call resource controls
- benchmark quality gain against token / latency / maintenance cost

---

## 6. Still open

- O-C-004 Renderer Omission Risk
- O-D-002 Reducer Specification Gap
- Q-N1-002 How can executive reader verify the summary?
- O-E-001 Deliberation Cost Explosion remains unproven
- final permissions / transition table not yet defined

**END**
