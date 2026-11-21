# 候選架構 V0.2｜觀察連續性 × 語義未封閉 × 有權切換
**Standing**：SESSION_ONLY / CONCEPT CANDIDATE / NOT_RUNTIME / NO_REGISTRY_WRITE。

## 對 001 的精確增量
001：Source → Method → First Observation → Engine Router → Engine → Shell Qualification；規劃可用，但若 Router 假定 Problem Shape 已全部建模，會錯過 SAC 可觀察但尚未有名的關係，並讓 DAIL Schema 反過來支配問題形成。

002 補上**可反向改變問題描述**的接口，不把流程圖冒充生成本體：
~~~text
Human problem / qualified source / current authority
     ↘
  SAC-informed qualitative observation (owner: Main/SAC when applicable)
     ↔ problem frame + premise plurality / tentative relational candidate
     ↔ Method first-observation screen (may return NO_METHOD)
     ↔ Engine recommendation (including NO_ENGINE; not truth)
           ↓  only when material and lawful
     engine counterforce / update / locally defined exit
     ↔ newly discovered material relation? → qualified reframe / route reconsideration
           ↓
  Shell: owner, trace continuity, provenance, scope, history, open objection,
         current operating obligations and separate release gate
           ↓
  DAIL semantic declaration of qualified relation/goal/constraint/unknown,
         L9 registered AND actually bound capabilities when needed
           ↓
  authorized action or ordinary response; world result re-enters as new source
~~~
This is a *relational research map*, not an implementation order and not a replacement for V1.4.2's mandatory R1/O9/T1/R2/T2/Post-R2/R3+.

## Three non-collapses
1. SAC observation != Engine local victory != governance qualification. SAC helps disclose possible tension/accessible paths but doesn't mint Engine truth; Shell must not appoint itself SAC owner.
2. DAIL declarative semantics != fixed code state machine != unqualified new relationship. Unformed relation remains provisional source-grounded observation; no loss simply because no enum exists.
3. Radar signal != decision. Resident-silent is the supported conceptual mode; no evidence a background Radar V6 daemon is currently running in this ChatGPT host. L9 registered != presently bound != authorized; no fake execution receipt.

## Engine Interface concept patch (v0.2 proposal, not edits to source Registry)
~~~yaml
ENGINE_INVOCATION_CANDIDATE_V0_2:
  invocation_id: REQUIRED
  source_refs: REQUIRED
  owner_and_scope: REQUIRED
  current_protocol_and_os_version: REQUIRED
  problem_frame_ref: REQUIRED_OR_SOURCE_BOUNDED_UNKNOWN
  premise_family_refs: LIST_OR_UNKNOWN
  sac_observation_ref: OPTIONAL_AND_ACTUAL_IF_AVAILABLE
  lamp_and_trace_refs: REQUIRED_WHEN_CURRENT_L8_DEMANDS
  radar_signal_ref: OPTIONAL_ADVISORY_ONLY
  open_relation_candidate_refs: OPTIONAL_SOURCE_CAPTURE_ONLY
  method_screen: METHOD_ID_OR_NO_METHOD_REASON
  selected_engine_or_no_engine: REQUIRED_WITH_REASON
  counterforce_and_material_delta_ref: REQUIRED_IF_MATERIAL
  prior_engine_exit: REF_OR_NONE
  switch_why_now: IF_SWITCH
  unresolved_claims_and_minority: PRESERVE
  owner_rejudgment: ONLY_BY_OWNER
  engine_exit: LOCAL_STATE_ONLY
  shell_qualification: SEPARATE_FROM_ENGINE_EXIT
  action_authorization: SEPARATE_HUMAN_OR_VALID_OWNER
  l9_capability_binding_state: EXPLICIT_IF_TOOL_PROPOSED
  dail_semantic_contract: ONLY_WHEN_RELATION_QUALIFIED
  lineage: SUPERSEDES_SEPARATE_FROM_RESPONDS_TO
  cost_bearer_and_reversibility: WHEN_MATERIAL
  current_operating_status: NOT_CHANGED_BY_THIS_SCHEMA
~~~

## Additional research constraint
If new relation can be discovered only after typed fields assign an existing Engine, this design has **premature formalization failure**. If every free-form relation causes full re-routing, this design has **unbounded cost / false signal failure**. Both must be measured rather than solved by a verbal slogan.
