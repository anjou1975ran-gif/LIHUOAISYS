
# TEST-001｜Session Manifest

~~~yaml
SESSION_MANIFEST:
  session_id: TEST-001-SECRETARY-KERNEL
  status: WAITING_HUMAN

  human_desire_ref: 01_HUMAN_DESIRE.md
  mandate_ref: 01_HUMAN_DESIRE.md#D1
  mandate_type: CONCEPT
  mandate_standing: SECRETARY_INTERPRETATION / HUMAN_NOT_YET_CONFIRMED

  human_intervention_mode:
    baseline: H0_FREE
    events:
      - HI-001: H2_GUIDED_ONE_SHOT
      - HI-002: H1_NUDGE_ONE_SHOT
    current: H0_FREE

  end_policy:
    current_session: LEGACY_UNSPECIFIED
    auto_end_allowed: false

  proposal_current_ref: 02_PROPOSAL_P0.md
  proposal_current_version: P0

  leading_candidate_branch_ref: 08_PROPOSAL_P1R3_CANDIDATE.md
  leading_candidate_version: P1R3-CANDIDATE

  active_branch_refs:
    - 04_PROPOSAL_P1_CANDIDATE.md
    - 05_PROPOSAL_P1R1_CANDIDATE.md
    - 06_PROPOSAL_P1R2_CANDIDATE.md
    - 08_PROPOSAL_P1R3_CANDIDATE.md

  core_seats: [N1, A, B, C, D, E]

  execution_identity:
    mode: SAME_MODEL_MULTI_ROLE_REFERENCE
    evidence_ref: "Current ChatGPT project session; separate independent model calls not yet established"

  chat_display_mode: LIVE_STRUCTURED
  recording_depth: FULL_EVENT_AND_ROUND

  current_round: R006

  closure:
    content_closure: PASSED
    mandate_exit: BLOCKED
    blocking_ref: O-C-006

  resolved_issue_refs:
    - O-C-001
    - O-B-001
    - O-B-002
    - O-C-002
    - O-C-003
    - O-C-004
    - O-C-005
    - O-D-001
    - O-D-003
    - O-N1-001
    - Q-N1-002
    - Q-SEC-001

  remaining_validation_refs:
    - O-D-002
    - O-E-001
    - O-E-002

  procedural_blocker_refs:
    - O-C-006

  current_guest_refs: []

  next_required_input:
    - HUMAN_CONFIRM_OR_CORRECT_D1

  next_runnable_queue: []
~~~
