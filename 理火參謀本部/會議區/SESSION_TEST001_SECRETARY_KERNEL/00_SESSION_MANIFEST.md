
# TEST-001｜Session Manifest

~~~yaml
SESSION_MANIFEST:
  session_id: TEST-001-SECRETARY-KERNEL
  status: OPEN

  human_desire_ref: 01_HUMAN_DESIRE.md
  mandate_ref: 01_HUMAN_DESIRE.md#D1
  mandate_type: CONCEPT
  mandate_standing: SECRETARY_INTERPRETATION / HUMAN_NOT_YET_CONFIRMED

  human_intervention_mode:
    baseline: H0_FREE
    events:
      - HI-001: H2_GUIDED_ONE_SHOT
    current: H0_FREE

  proposal_current_ref: 02_PROPOSAL_P0.md
  proposal_current_version: P0
  active_branch_refs:
    - 04_PROPOSAL_P1_CANDIDATE.md
    - 05_PROPOSAL_P1R1_CANDIDATE.md

  core_seats: [N1, A, B, C, D, E]

  execution_identity:
    mode: SAME_MODEL_MULTI_ROLE_REFERENCE
    evidence_ref: "Current ChatGPT project session; separate independent model calls not yet established"

  chat_display_mode: LIVE_STRUCTURED
  recording_depth: FULL_EVENT_AND_ROUND

  current_round: R003

  resolved_issue_refs:
    - O-C-001
    - O-B-001

  current_open_or_unresolved_issue_refs:
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

  current_guest_refs: []

  next_runnable_queue:
    - MANDATORY_OWNER_ROUTE_MAP
    - EXECUTIVE_PRIORITY_RULE
    - REDUCER_REPLAY_SPEC
    - COST_OBSERVATION_FIELDS
    - SECRETARIAT_FRAME_RECHECK
~~~
