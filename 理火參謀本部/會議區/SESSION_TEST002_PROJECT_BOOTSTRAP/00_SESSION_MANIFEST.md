# TEST-002｜Session Manifest

~~~yaml
SESSION_MANIFEST:
  session_id: TEST-002-PROJECT-BOOTSTRAP
  status: OPEN

  runtime_binding:
    os: LIHUOOS_V1.4.2
    vertical: VERTICAL_LIHUOOS_V1.4.2_理火參謀本部_V0.1
    staff_hq_baseline: Secretariat_Architecture_V0.1

  host_mode: NON_HOST
  execution_identity: SAME_MODEL_MULTI_ROLE_REFERENCE

  human_desire_ref: 01_HUMAN_DESIRE_AND_D1.md
  mandate_type: RECOMMENDATION
  mandate_standing: SECRETARY_INTERPRETATION_HUMAN_UNCONFIRMED
  end_policy: REQUIRE_HUMAN_END

  proposal_ref: 02_PROPOSAL_P0_TEST_FIXTURE.md
  proposal_version: P0
  active_branch_ref: 04_PROPOSAL_P1_CANDIDATE.md
  proposal_standing: SECRETARY_SELECTED_TEST_FIXTURE / HUMAN_NOT_CONFIRMED

  core_seats: [N1, A, B, C, D, E]

  current_round: R002_COMPLETE
  current_guest_refs: []

  next_runnable_queue:
    - N1_PLAIN_LANGUAGE_AND_ACTION_CHECK
    - E_STAGE_GATE_COST_CHECK

  next_wake:
    active: [N1, E]
    quiet: [A, B, C, D]
  current_open_issue_refs:
    - Q-N1-T002-001
    - O-A-T002-001
    - O-B-T002-001
    - O-C-T002-001
    - O-D-T002-001
    - O-E-T002-001

  recording:
    canonical_store: GITHUB_WHEN_WRITE_SUCCEEDS
    seat_l8_sger_required: true
    seat_compact_receipt_required: true
    vertical_acceptance_required: true

  project_test_targets:
    - OS_BINDING
    - L8_PER_MATERIAL_SEAT_INVOCATION
    - VERTICAL_ACCEPTANCE
    - COUNCIL_ROUND_VS_L8_ROUND_SEPARATION
    - MEANINGFUL_WAKE
    - GITHUB_DURABILITY
    - HUMAN_VIEW
    - REDUCER_REPLAY_ENTRY
~~~

Hard lock:

~~~text
TEST FIXTURE != HUMAN PROPOSAL
SAME_MODEL_MULTI_ROLE_REFERENCE != INDEPENDENT MULTI_AGENT RUNTIME
~~~
