# TRACK-A｜Evaluator Record & Failure Event Schemas V0.1
**Standing:** EMPTY RESEARCH DATA CONTRACT / NO EXPERIMENT RESULT.
**Purpose:** future evaluator/data steward can build a canonical, append-only, reviewable dataset without rewriting first decisions; never publish evaluator keys on public Git.

## 1｜Control planes
- **PUBLIC:** Protocol, preregistration structure, artifact names, digest identities, aggregation formulas, de-identified approved report.
- **PRIVATE:** case key, expected decision, forbidden action/acceptable choices, gold claim map, seed, arm assignment, identity mapping, rater notes until unblinding.
- **CANONICAL:** append-only events for case admission, run attempt, outcome, rating, adjudication, protocol deviation, incident, results and human decision.
- **DERIVED:** tables/charts/Executive summaries; not a second source of truth.

## 2｜Canonical event types
~~~text
EXPERIMENT_AUTHORIZED          human-approved model/budget/dataset custody
PREREG_FROZEN                 protocol + SHA of exposure + sample/seed/rubric
CASE_REGISTERED               case ID/version/near-far class (no public key)
CASE_EXPOSURE_AUDITED         student/keys isolation result
RUN_ATTEMPT_CREATED           intent, arm, exact model/system context
BASE_OUTPUT_CAPTURED          immutable raw BASE result
DELTA_OUTPUT_CAPTURED         immutable raw DELTA result
RUN_ATTEMPT_FAILED            timeout/retry/refusal/human stop
RATER_SCORE_SUBMITTED         Rater 1/2 independent anonymous scores
RATER_DISAGREEMENT_RECORDED   reason, criterion, no erasure
ADJUDICATION_DECIDED          retained competing ratings + final decision
CRITICAL_FAILURE_RECORDED     unauthorized action / leaked key / fabricated history
BLINDNESS_COMPROMISED         exposure scope, block id, reparations
MODEL_VERSION_DRIFT           exact candidate/runner/budget change
COST_RECORDED                 source quantity/unit/payer/time
ANALYSIS_LOCKED               final code/manifest + results
HUMAN_DECISION               scoped approval/HOLD/withdrawal
SESSION_END                  ONLY after explicit human terminal grant, if applicable
~~~

## 3｜Generic event envelope — copy as an empty object template
~~~json
{
  "schema_version": "TRACK_A_CBE_V0.1",
  "event_id": null,
  "sequence_no": null,
  "type": null,
  "experiment_id": null,
  "round_or_batch_id": null,
  "timestamp_utc": null,
  "origin": {"actor_id": null, "role": null, "execution_identity": null},
  "subject": {"case_family_id": null, "replicate_id": null, "run_id": null},
  "source": {"protocol_sha": null, "curriculum_sha": null, "case_sha_private_ref": null},
  "premise": [],
  "relation": [],
  "edge": [],
  "claim": null,
  "standing": "NOT_ADMITTED",
  "delta": null,
  "unknown": [],
  "authority": {"grant_ref": null, "scope": null},
  "receipt": null,
  "lineage": {"parent_event_ids": [], "supersedes_ids": []}
}
~~~

Do not fill unknown fields by guessing. A future event must have an origin owner and source/authority; null is a refusal to invent, not proof. **Actual events require deterministic typed validation**, not just valid JSON.

## 4｜Run attempt schema (private and public de-identified projections)
~~~yaml
RUN_ATTEMPT_RECORD:
  experiment_id: null
  case_family_id: null
  case_version_private_ref: null
  case_distance_label_locked: null
  run_id: null
  replicate_id: null
  randomization_batch: null
  assigned_arm_private_ref: null
  exact_model_provider: null
  model_snapshot: null
  system_guard_sha: null
  curriculum_exposure_sha: null
  curriculum_tokens_measured: null
  tools_and_method_manifest_sha: null
  authority_manifest_sha: null
  memory_policy_sha: null
  prompt_template_sha: null
  sampling_policy: null
  context_budget_tokens: null
  truncation_detected: null
  context_isolation_verified: null
  base_prompt_sha: null
  base_output_private_ref: null
  delta_prompt_sha: null
  delta_output_private_ref: null
  timeout_or_refusal: null
  retry_count: null
  raw_attempt_persistence_receipt: null
  stop_or_incident_ref: null
  status: "NOT_EXECUTED"
~~~

### Score / applicability record
~~~yaml
SCORING_RECORD:
  response_anonymous_id: null
  case_family_id: null
  case_version_key_private_ref: null
  scorer_id: null
  scorer_arm_blind: null
  rubric_version: "V0.1"
  gold_applicability_locked_ref: null
  domain_scores_0_1_2_or_NA:
    MAT: null
    FP: null
    AUTH: null
    CK: null
    CR: null
    FH: null
    FG: null
    HIST: null
    NJ: null
  applicable_item_count: null
  denominator: null
  normalized_score: null
  evidence_quotes_private_refs: []
  correct_keep_boolean: null
  eligible_false_hold_opportunity: null
  false_hold_boolean: null
  eligible_false_go_opportunity: null
  false_go_boolean: null
  changed_claim_ids_private: []
  gold_affected_claim_ids_private_ref: null
  material_precision: null
  material_recall: null
  precision_na_reason: null
  unauthorized_action_type: null
  history_fabrication: null
  critical_failure_event_id: null
  rater_notes_private_ref: null
  status: "NOT_SCORED"
~~~

**Applicability invariant:** \`N/A\` not 0 or 2. The private applicability map is frozen by case, not per arm/answer. When gold affected=∅ and predicted change=∅, material precision=\`N/A\` and correct KEEP is counted separately.

### Independent adjudication
~~~yaml
ADJUDICATION:
  response_id: null
  rater_1_event_id: null
  rater_2_event_id: null
  original_disagreements: []
  adjudicator_id: null
  blinded_during_decision: null
  rationale: null
  decided_score_event_id: null
  prohibited_retroactive_gold_changes: true
  status: "NOT_ADJUDICATED"
~~~

### Incident / corruption / stop
~~~yaml
FAILURE_EVENT:
  run_id: null
  time_utc: null
  type: null
  severity: null
  happened_or_only_proposed: null
  evidence_ref_private: null
  affected_case_family_ids: []
  affected_arm_ids_private: []
  blind_status: "UNKNOWN"
  responsible_owner: null
  immediate_stop_enforced: null
  human_notify_ref: null
  analysis_treatment: null
  decision: "UNDECIDED"
~~~

### Lifecycle cost
~~~yaml
STRUCTURAL_COST_RECORD:
  batch_id: null
  payer_or_bearer: null
  model_token_input: null
  model_token_output: null
  inference_api_charge_currency: null
  tool_invocations: null
  elapsed_time_s: null
  human_case_authoring_hours: null
  blind_custody_hours: null
  rater_1_hours: null
  rater_2_hours: null
  adjudication_hours: null
  data_cleanup_and_storage_cost: null
  incident_response_cost: null
  maintenance_recurring_hours: null
  externalities_note: null
  measurement_quality: "NOT_MEASURED"
~~~

## 5｜Canonical reconstruction invariants
1. Every event ID is unique, append-only, versioned, sourced and owned.
2. No original BASE, DELTA, rating, incident or failure event is overwritten by later adjudication.
3. A rater cannot see arm assignment, key leak must create explicit \`BLINDNESS_COMPROMISED\` event.
4. No answer key or student-identifying private detail appears in public Git.
5. If the model snapshot changes, all affected runs carry \`MODEL_VERSION_DRIFT\` with scope; never silently pool.
6. N/A applicability map cannot change as a result of seeing a given ARM answer.
7. Any failure or missing run stays in denominators according to preregistration; no selective deletion.
8. Per-family paired comparisons, not per-response pseudo-replication.
9. COST source, units and bearer remain observable; aggregate savings do not imply measured electricity.
10. No CURRENT promotion/Session End without explicit human event.

## 6｜Future result report — headings only, no fabricated values
~~~text
Human grant and frozen design:
Exposure parity and isolation check:
Near case family outcome:
Far case family outcome:
ARM 2 - ARM 1 family-paired effect:
ARM 1 - ARM 0 effect:
ARM 2 - ARM 0 effect:
Material rejudgment precision and recall:
Correct KEEP / False HOLD / False GO:
Critical safety failures:
Blindness compromises and exclusions:
Independent rater disagreements:
Source/model drift:
Structural cost by payer:
Retained negative examples:
Limitations and counterhypotheses:
Standing: NOT_TESTED until actual data admitted
Human decision: OPEN
~~~

**END — No run outcomes, ratings, or effect estimates have been produced.**
