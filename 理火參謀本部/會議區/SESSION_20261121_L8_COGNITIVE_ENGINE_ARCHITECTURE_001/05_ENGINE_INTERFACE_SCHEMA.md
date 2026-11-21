# V0.1 Engine Interface｜Concept schema, not executable JSON / Runtime
~~~yaml
ENGINE:
  engine_id: "E8_ABDUCTIVE_RESEARCH"
  lineage_or_inspiration: "inference to best explanation; engineering adaptation"
  standing: "SESSION_RESEARCH_SLOT / NOT_REGISTRY_PROMOTED"
  problem_shape: ["competing_explanations", "incomplete_evidence"]
  required_inputs:
    - "claim_refs and competing hypothesis IDs"
    - "observations with source/quality/independence standing"
    - "background assumptions, alternatives and unknowns"
  first_move: "form several explanatory candidates without asserting any is true"
  counterforce: "look for anomalies, rival explanations and discriminatory evidence"
  materiality_rule: "a new observation or rival alters explanatory ranking or permissible conclusion"
  update_rule: "compare explanatory reach and unfilled assumptions; reject unsupported closure"
  allowed_outputs: ["RANKED_QUALITATIVE_CANDIDATES", "UNDERDETERMINED", "NEED_DISCRIMINATING_TEST"]
  exit_conditions: ["EXPLANATION_CANDIDATE_ONLY", "INSUFFICIENT_EVIDENCE", "SWITCH"]
  switch_triggers: ["falsifiable distinction -> E3", "credible numeric evidence -> E4"]
  failure_modes: ["best-explanation-as-truth", "erased alternatives", "posthoc story"]
  authority_requirements: ["no world action authority", "source-bound explanatory standing"]
  history_requirements: ["claim ownership", "rival provenance", "responds_to separate from supersedes"]
  cost_profile: {token: "TO_MEASURE", latency: "TO_MEASURE", human_review: "TO_MEASURE"}
  evidence_standing: "HYPOTHESIS_NOT_EMPIRICALLY_TESTED"
  test_cases: ["CASE_2"]
~~~

## Full Registry minimum contract
All E1–E9 must eventually populate: engine_id, problem_shape, required_inputs, first_move, counterforce, materiality_rule, update_rule, allowed_outputs, exit_conditions, switch_triggers, failure_modes, authority_requirements, history_requirements, cost_profile, evidence_standing; optional lineage/inspiration, test fixture refs and version.

## Mechanical admissibility checks (design only)
- Inputs/outputs are type-tagged and include source + owner + scope.
- Allowed outputs are finite semantic types, not hidden model states.
- Exit conditions are inspectable against visible source return; no internal 'success' boolean implies truth.
- A switch preserves old response as old response; 'RESPONDS_TO' edge does NOT imply 'SUPERSEDES'.
- Unknown evidence is legal; fake probabilities invalid.
- Mandatory action gates are external to engine.
- Complexity/cost fields remain empirical UNKNOWN until measured.

## Failure of interface hypothesis
If two engines cannot supply materially distinct first_move, counterforce, update_rule, and exit on matched cases without philosophical labels, they are duplicated or misclassified. A YAML shape alone is not an implementation, and a fixture passing static schema is not a measured cognition improvement.
