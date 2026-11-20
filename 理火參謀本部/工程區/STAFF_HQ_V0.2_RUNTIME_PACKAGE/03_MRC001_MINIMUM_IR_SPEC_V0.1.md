# MRC-001 MINIMUM IR SPEC V0.1
## Minimum Replayable Council｜最小中介表示規格

**版本：** V0.1-WORKING  
**日期：** 2026-11-20  
**法位：** IR_SPEC_CANDIDATE / NORMALIZATION_ONLY / NOT_SEMANTIC_OWNER / NOT_RUNTIME_DEPLOYMENT  
**依賴：** Package 01 DAIL Minimum Relation Set / Package 02 Vertical V0.2

---

# 0｜一句話

> **IR 只把已資格化的議事語義轉成可機器保存與重播的 shape；IR 不創造 authority、materiality、standing 或 qualification。**

```text
DAIL DEFINES.
IR NORMALIZES.
CODE CONNECTS.
RUNTIME EXECUTES.
```

---

# 1｜MRC-001 必須能重建什麼

只靠 Canonical Events，Reducer 必須能重建：

- Session identity / mandate
- current problem frame
- proposal lineage
- latest proposal version
- each seat current stance ref
- open issues
- material cross-seat relations
- queued / delivered / consumed / responded relations
- affected seat set
- latest-version review coverage
- surviving objections
- human gate
- formal qualification blockers
- checkpoint / session-end standing
- persistence standing

若其中任何一項只能靠 Final Report 猜回來，MRC-001 未成立。

---

# 2｜Canonical ID

所有 governance object 都需要 semantic ID，不得以 Git path 當唯一身份。

```yaml
CanonicalID:
  namespace: string
  object_type: string
  local_id: string
  version: optional
```

例：

```text
SESSION:CI-001-REENTRY-001
EVENT:CR-EV-043
PROPOSAL:P2
PROPOSAL_VERSION:P2@v1
STANCE:B@P2v1
RELATION:CR-X-004
ISSUE:O-C-LEGAL_RIGHTS
```

Git path / blob SHA 是 persistence evidence，不是 semantic identity 本身。

---

# 3｜IR Object Set

## 3.1 Actor

```yaml
Actor:
  actor_id:
  actor_type: HUMAN|SECRETARIAT|CORE_SEAT|EXTERNAL_EXPERT|SYSTEM
  role_ref:
  execution_identity_ref:
```

## 3.2 AuthorityBinding

```yaml
AuthorityBinding:
  binding_id:
  actor_ref:
  authority_type:
  scope_ref:
  source_ref:
  standing:
```

禁止由 IR 自動推導新 authority。

## 3.3 ResponsibilityBinding

```yaml
ResponsibilityBinding:
  binding_id:
  seat_ref:
  responsibility_tags: []
  mandatory_route_tags: []
  source_ref:
```

## 3.4 Session

```yaml
Session:
  session_id:
  parent_session_ref:
  execution_identity:
  mandate_ref:
  end_policy:
  formal_gate_refs: []
  persistence_standing:
```

## 3.5 Mandate

```yaml
Mandate:
  mandate_id:
  mandate_type: CONCEPT|RECOMMENDATION|DECISION
  D0_ref:
  D1_ref:
  primary_question:
  desired_return:
  hard_boundaries: []
  excluded_scope: []
  standing:
```

## 3.6 ProblemFrame

```yaml
ProblemFrame:
  frame_id:
  session_ref:
  origin_ref:
  standing: OPEN|HUMAN_GIVEN|CONTESTED|QUALIFIED_FOR_CURRENT_MANDATE|SUPERSEDED
  statement_ref:
  parent_frame_ref:
```

## 3.7 Reference

```yaml
Reference:
  reference_id:
  source_ref:
  reference_type:
  admissibility_standing:
  privileges: []
```

Invariant:

```text
Reference.privileges
MAY NOT
CONTAIN "AUTO_PROPOSAL"
```

## 3.8 Proposal

```yaml
Proposal:
  proposal_id:
  session_ref:
  origin_ref:
  current_version_ref:
```

## 3.9 ProposalVersion

```yaml
ProposalVersion:
  proposal_version_id:
  proposal_ref:
  version:
  origin_event_refs: []
  parent_version_ref:
  content_ref:
  standing: CANDIDATE|MATERIAL_REVIEW_PENDING|REVIEWED_CONDITIONALLY|QUALIFIED|HOLD|WITHDRAWN|SUPERSEDED
  material_delta_refs: []
  affected_seat_refs: []
  review_refs: []
  surviving_objection_refs: []
  unresolved_refs: []
```

## 3.10 Stance

```yaml
Stance:
  stance_id:
  seat_ref:
  target_ref:
  proposal_version_ref:
  prior_stance_ref:
  response_type:
  statement_ref:
  change_basis_refs: []
  unresolved_refs: []
```

response_type：
- INITIAL_POSITION
- POSITION_REVISION
- POSITION_RETAINED_WITH_REASON
- POSITION_DOWNGRADED
- POSITION_WITHDRAWN
- CONDITIONAL_SUPPORT
- OBJECTION
- NEW_PATH
- CONDITION
- QUESTION

## 3.11 CanonicalEvent

```yaml
CanonicalEvent:
  event_id:
  session_ref:
  sequence_no:
  timestamp_ref:
  origin_actor_ref:
  origin_role_ref:
  semantic_type:
  source_refs: []
  target_refs: []
  proposal_ref:
  proposal_version_ref:
  prior_stance_ref:
  materiality_claim_ref:
  affected_seat_claim_refs: []
  object_refs: []
  unresolved_refs: []
  persistence_standing:
```

## 3.12 MaterialityClaim

```yaml
MaterialityClaim:
  claim_id:
  origin_ref:
  standing: MATERIAL|NON_MATERIAL|CONTESTED
  delta_kind_refs: []
  basis_refs: []
  qualification_source_refs: []
```

IR 不得自行把 CONTESTED 轉 MATERIAL。

## 3.13 MaterialRelation

```yaml
MaterialRelation:
  relation_id:
  session_ref:
  source_event_ref:
  target_seat_ref:
  relation_type: CHALLENGES|CONDITIONS|REFRAMES|CHANGES_ARCHITECTURE|CHANGES_COST|CHANGES_EVIDENCE|OTHER
  materiality_claim_ref:
  affected_basis_refs: []
  state: QUEUED|DELIVERED|CONSUMED|RESPONDED|CLOSED_FOR_VERSION
  delivered_ref:
  consumed_ref:
  response_event_refs: []
  proposal_version_scope_ref:
```

Invariant：

```text
DELIVERED != CONSUMED
CONSUMED != AGREED
RESPONDED != REVISED
```

## 3.14 SeatWake

```yaml
SeatWake:
  wake_id:
  seat_ref:
  trigger_relation_refs: []
  target_proposal_version_ref:
  qualified_input_refs: []
  L8_cycle_ref:
  output_event_refs: []
  acceptance_standing:
```

## 3.15 Issue

```yaml
Issue:
  issue_id:
  origin_ref:
  issue_type:
  materiality_standing:
  target_refs: []
  standing: OPEN|CONDITIONED|HOLD|RESOLVED_FOR_VERSION|SUPERSEDED
  resolution_refs: []
```

## 3.16 QualificationCheck

```yaml
QualificationCheck:
  check_id:
  target_proposal_version_ref:
  affected_seats: []
  reviewed_seats: []
  quiet_or_not_affected: []
  unreviewed_material_seats: []
  surviving_objections: []
  unresolved_external_facts: []
  meta_governance_ref:
  upper_gate_refs: []
  result: QUALIFIED|REVIEWED_CONDITIONALLY|HOLD
```

## 3.17 HumanGate

```yaml
HumanGate:
  gate_id:
  required_action:
  decision_request_ref:
  authorization_ref:
  result_acceptance_ref:
  standing: NOT_REQUIRED|REQUIRED|WAITING|SATISFIED
```

## 3.18 Receipt

```yaml
Receipt:
  receipt_id:
  receipt_type:
  target_ref:
  evidence_refs: []
  persistence_ref:
  standing:
```

---

# 4｜Graph Relations

最小 relation graph：

```text
HUMAN --AUTHORIZES--> SESSION/ACTION
REFERENCE --INFORMS--> PROBLEM_FRAME
SEAT --OWNS_RESPONSIBILITY--> SCOPE
SEAT --ORIGINATES--> EVENT/STANCE/PROPOSAL
EVENT --AFFECTS_MATERIALLY--> SEAT
MATERIAL_RELATION --REQUIRES_REWAKE--> SEAT
SEAT --REVIEWS_EXACT_VERSION--> PROPOSAL_VERSION
PROPOSAL_VERSION --DERIVES_FROM--> EVENTS
PROPOSAL_VERSION --SUPERSEDES--> PRIOR_VERSION
QUALIFICATION_CHECK --TARGETS--> LATEST_PROPOSAL_VERSION
```

---

# 5｜IR Validation Classes

IR validator 只做：

- required field presence
- canonical ref resolution
- enum validity
- version identity consistency
- sequence monotonicity
- duplicate ID detection
- forbidden cardinality
- impossible lifecycle transition detection
- missing source ref detection

IR validator 不做：

- fact truth judgment
- legal judgment
- materiality decision
- seat stance decision
- proposal winner selection
- release authorization

---

# 6｜Forbidden Coercions

```text
UNKNOWN → FALSE
PARTIAL → COMPLETE
CONTESTED → MATERIAL
MATERIAL → NON_MATERIAL
REFERENCE → PROPOSAL
TASK CONTINUATION → HUMAN AUTHORIZATION
SCHEMA VALID → QUALIFIED
GIT EXISTS → DEPLOYED
```

全部禁止由 IR/compiler 自動完成。

---

# 7｜MRC-001 Output State Shape

```yaml
CouncilState:
  session_ref:
  mandate_ref:
  current_problem_frame_ref:
  latest_proposal_version_ref:
  proposal_lineage: []
  seat_current_stance_refs: {}
  open_issue_refs: []
  material_relations:
    queued: []
    delivered: []
    consumed: []
    responded: []
  pending_wake_refs: []
  latest_version_review:
    affected_seats: []
    reviewed_seats: []
    unreviewed_seats: []
  surviving_objections: []
  human_gate_ref:
  qualification_blockers: []
  checkpoint_standing:
  session_end_standing:
  persistence_standing:
```

---

# 8｜Acceptance

MRC-001 IR spec PASS 只表示：

```text
MACHINE SHAPE IS DEFINED
```

不表示：
- semantics ratified
- reducer implemented
- runtime deployed
- multi-agent operational

**END**
