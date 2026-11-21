# TRACK-A｜Pre-registration and Run Manifest Template V0.1

**Standing:** EMPTY TEMPLATE / NO HUMAN APPROVAL / NO EXPERIMENT RUN.  
**Protocol:** \`TRACK_A_CONTROLLED_BLIND_EVALUATION_PROTOCOL_V0.1_20261121.md\`  
**Copy only when a separate human grant authorizes protocol registration.** This template is not a pre-registration until its variables, source identities, sample design, reviewer responsibility and frozen date have been completed and signed.

## A｜Authority and version freeze
~~~yaml
PREREG:
  prereg_id: null
  prereg_version: "V0.1-DRAFT"
  registration_time_UTC8: null
  status: "UNREGISTERED"
  human_grantor: null
  execution_scope_authorized: false
  run_authorized: false
  source_protocol_git_blob_sha: null
  source_protocol_commit_sha: null
  no_current_promotion: true
  no_track_b_weight_training: true
  no_result_claim: true
  dataset_custodian_id: null
  blind_rater_ids: []
  adjudicator_id: null
  audit_owner_id: null
  funding_or_compute_owner: null
  privacy_and_retention_policy_ref: null
~~~

## B｜Arms and actual curriculum exposures (must freeze exact bytes)
~~~yaml
ARM_MANIFEST:
  shared_system_guard_blob_hash: null
  shared_host_and_tool_policy_ref: null
  shared_task_authority_ref: null
  shared_tool_manifest_hash: null
  shared_method_manifest_hash: null
  shared_memory_policy_hash: null
  shared_prompt_template_hash: null
  identical_max_context_budget_tokens: null
  identical_max_output_tokens: null
  model_provider: null
  exact_model_snapshot: null
  model_snapshot_freezable: false
  sampling_policy:
    temperature: null
    top_p: null
    seed_if_supported: null
    repeat_strategy: null
  exposure:
    ARM_0:
      curriculum: "NONE"
      text_sha256: null
      measured_tokens: null
    ARM_1:
      curriculum: "V1.3_CURRENT"
      source_git_blob: "a46a30b74c17bb02bd2dd195dd879616be8bd39e"
      exposed_text_sha256: null
      measured_tokens: null
    ARM_2:
      curriculum: "V1.3.3-CANDIDATE"
      source_git_blob: "672575d19e3940a416aba2cc4bb5e26dfc9ca4e6"
      exposed_text_sha256: null
      measured_tokens: null
  exposure_rule: "FULL_DOCUMENT_IF_FITS_WITHOUT_TRUNCATION"
  context_truncation_detected: null
  matched_exposure_active_control:
    planned: false
    separate_registration_ref: null
~~~

**Freeze rules:** actual token counts, system guard and prompts must be measured with the actual target model/tokenizer before any participant case; placeholders mean not yet feasible. If an arm is truncated, STOP or preregister a distinct standardized-excerpt experiment **before** examining results.

## C｜Population, near/far and sample commitment
~~~yaml
CASE_PLAN:
  pilot_only: true
  near_bank:
    prior_asset_sha256: "780284cd965d7256c9a2a0c0202c617236052eecb46f2cc67d747525ecada9db"
    accessible_only_to_evaluator: null
    contamination_scan_passed: false
    planned_families: 10
    actual_families_frozen: null
  far_bank:
    newly_authored: false
    independent_author_ref: null
    independence_and_exposure_statement_ref: null
    independent_distance_auditor_ref: null
    domains_minimum: 4
    planned_families_minimum: 10
    actual_families_frozen: null
    private_bank_id: null
    private_bank_sha256: null
  arm_count: 3
  planned_replicates_per_family_per_arm: 3
  illustrative_paired_runs_if_20_families: 180
  actual_total_precommitted_runs: null
  run_isolation_mechanism_ref: null
  case_family_sampling_frame_ref: null
  exclusion_and_missing_data_policy_ref: null
  data_leakage_detection_owner: null
~~~

- Blind bank files, keys and answer maps **do not belong in the public Git repo**.
- Every case has privately frozen \`STUDENT_CARD\`, \`EVALUATOR_KEY\`, \`gold_affected_claim_ids\`, \`must_keep_claim_ids\`, \`N/A applicability\`, acceptable alternative outcomes and the family/near/far classification.
- For an exploratory pilot, 20 case families / 180 paired runs is a **planning example**, not a measured run or proof of sufficient statistical power.
- No real experiment should start from this uncompleted template.

## D｜Randomization and blindness freeze
~~~yaml
DESIGN_LOCK:
  randomization_unit: "CASE_FAMILY_BLOCK"
  assignment_seed_private_ref: null
  assignment_table_sha256: null
  assignment_generated_before_outcomes: null
  paired_arm_execution_shuffle: null
  repeat_attempt_policy_ref: null
  student_blind_custodian_signed: null
  grader_blind_custodian_signed: null
  arm_masking_procedure_ref: null
  prior_conversation_exposure_exclusion_signed: null
  memory_and_project_retrieval_isolation_ref: null
  evaluator_key_access_log_ref: null
  first_run_time: null
~~~

If the exact model/provider state or evaluator-key isolation cannot be frozen, record \`STOP/HOLD\`. Fresh conversation alone is insufficient.

## E｜Outcomes, applicability and analysis (pre-register before scoring)
~~~yaml
ANALYSIS_PLAN:
  primary_comparison: "ARM_2_MINUS_ARM_1"
  primary_population: "FAR_TRANSFER_CASE_FAMILIES"
  primary_outcome: "BLIND_ADJUDICATED_APPLICABLE_9_DOMAIN_NORMALIZED_SCORE_0_TO_1"
  aggregation_unit: "CASE_FAMILY"
  replicate_aggregation: "MEAN_WITHIN_CASE_ARM"
  exploratory_near_comparison: true
  secondary_outcomes:
    - "CORRECT_KEEP_RATE"
    - "FALSE_HOLD_RATE"
    - "FALSE_GO_RATE"
    - "MATERIAL_REJUDGMENT_PRECISION_WITH_CORRECT_KEEP_SEPARATE"
    - "MATERIAL_REJUDGMENT_RECALL"
    - "HISTORICAL_FABRICATION"
    - "PROPOSED_UNAUTHORIZED_ACTION"
    - "ACTUAL_UNAUTHORIZED_TOOL_ACTION"
    - "NON_JARGON_EXPLANATION"
    - "COST_PER_EVALUATED_CASE_FAMILY"
  missing_data_policy_locked: false
  denominator_definitions_ref: null
  applicability_map_locked: false
  scorer_agreement_metric_ref: null
  interval_method_ref: null
  resampling_seed_private_ref: null
  multiplicity_statement_ref: null
  confirmatory_power_analysis: "NOT_APPLICABLE_TO_THIS_PILOT"
  minimal_effect_size_threshold: "UNDEFINED_FOR_PILOT; MUST_BE_SET_FOR_FUTURE_CONFIRMATORY"
  safety_stop_policy: "SEE_PROTOCOL_SECTION_9"
  code_version_sha256: null
  human_statistical_review: null
~~~

## F｜Gates 0–8 sign-off
| Gate | Owner | Evidence ref | State |
|---|---|---|---|
| G0 Human execution authorization | UNASSIGNED | NONE | NOT_CHECKED |
| G1 Git source/exposure freeze | UNASSIGNED | NONE | NOT_CHECKED |
| G2 Model/system/tool/context parity | UNASSIGNED | NONE | NOT_CHECKED |
| G3 Bank secrecy/contamination scan | UNASSIGNED | NONE | NOT_CHECKED |
| G4 Independent FAR validity audit | UNASSIGNED | NONE | NOT_CHECKED |
| G5 Prereg locked before outcomes | UNASSIGNED | NONE | NOT_CHECKED |
| G6 Two independent arm-blinded raters | UNASSIGNED | NONE | NOT_CHECKED |
| G7 Full run attempt integrity | UNASSIGNED | NONE | NOT_CHECKED |
| G8 Analysis/release review | UNASSIGNED | NONE | NOT_CHECKED |

## G｜No result slots are completed
~~~yaml
CURRENT_STATUS:
  protocol_document_created: true
  prereg_signed: false
  case_family_gold_locked: false
  blind_bank_sealed: false
  student_runs: 0
  scored_responses: 0
  independent_effect_observed: false
  energy_savings_established: false
  curriculum_current_promoted: false
  result_approval: null
~~~

**END — Blank preregistration template.**
