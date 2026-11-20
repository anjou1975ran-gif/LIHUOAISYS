
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

  core_seats: [N1, A, B, C, D, E]

  execution_identity:
    mode: SAME_MODEL_MULTI_ROLE_REFERENCE
    evidence_ref: "Current ChatGPT project session; separate independent model calls not yet established"

  chat_display_mode: LIVE_STRUCTURED
  recording_depth: FULL_EVENT_AND_ROUND

  current_round: R002
  current_open_or_unresolved_issue_refs:
    - O-N1-001
    - O-B-001
    - O-C-001
    - O-C-002
    - O-C-003
    - O-D-001
    - O-E-001
    - O-C-004
    - O-D-002
    - Q-N1-002
  current_guest_refs: []

  next_runnable_queue:
    - P1_AUTHORITY_BOUNDARY
    - EXECUTIVE_DISSENT_COVERAGE
    - REDUCER_AND_QUEUE_MIN_SPEC
    - SECRETARY_FRAME_RECHECK
~~~
