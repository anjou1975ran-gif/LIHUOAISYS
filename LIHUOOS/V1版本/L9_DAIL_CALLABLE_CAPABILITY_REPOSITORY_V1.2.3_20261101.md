# LIHUOOS V1.2.3｜L9 DAIL CALLABLE CAPABILITY REPOSITORY
## 理火可調用能力倉｜Light Trace Current Binding Restored
### 2026-11-01

```yaml
DOCUMENT:
  id: LIHUOOS_L9_DAIL_CALLABLE_CAPABILITY_REPOSITORY
  version: V1.2.3
  date: 2026-11-01

  standing:
    - RATIFIED_CURRENT_CAPABILITY_LAYER
    - LIHUOOS_V1_2_3
    - LIGHT_TRACE_CURRENT_SOURCE_INTERNALIZED
    - LIGHT_TRACE_CHAT_NATIVE_BINDING_ESTABLISHED
    - LIGHT_TRACE_ORPHANED_BINDING_BUGFIX
    - LEGACY_LIGHTER_CAPABILITY_MIGRATION_PRESERVED
    - LIGHT_TRACE_INTER_ROUND_RENDERING_UPGRADED
    - LIGHT_TRACE_RESULT_RECEIPT_SEPARATION
    - NOT_HOST_DEPLOYMENT
    - NOT_IMPLEMENTATION_COMPLETION

  predecessor:
    file: "L9_DAIL_CALLABLE_CAPABILITY_REPOSITORY_V1.2.2_20261027.md"
    blob_sha: "36ca93f909d2f250fec97a616365817d04e4158d"
    standing: "RATIFIED CURRENT CAPABILITY LAYER"

  human_approval:
    date: 2026-11-01
    instruction: "可以修嗎? 可以的話 動手吧 批准升級 不用等 這是BUG修復"

  change_scope:
    - RESTORE_LIGHT_TRACE_CURRENT_INTERNAL_SOURCE
    - SET_LIGHT_TRACE_BINDING_STATE_CHAT_NATIVE_AVAILABLE
    - SET_LIGHT_TRACE_INTERNAL_IMPLEMENTATION_BINDING_REF
    - REQUIRE_TRACE_CONTENT_AND_TRACE_RESULT_REF_FOR_T1_T2_T3_PLUS_TM
    - PRESERVE_V1_2_LIGHT_TRACE_CAPABILITY
    - REQUIRE_TRACE_RESULT_REF_FOR_SUCCESSFUL_OR_PARTIAL_LIGHT_TRACE
    - KEEP_CANONICAL_EXECUTION_RECEIPT_OPTIONAL
    - ALLOW_CHAT_NATIVE_SAME_CONTEXT_TRACE_RESULT_WITHOUT_FAKE_PROVIDER_RECEIPT
    - PRESERVE_V1_1_CAPABILITY_MIGRATION
    - EXPAND_LIGHT_TRACE_RENDERER_FOR_INTER_ROUND_COMPETITION_TRACE
    - ADD_MANIFESTATION_FIDELITY_TRACE_MODE
    - KEEP_LIGHT_TRACE_SEMANTIC_AND_TIMING_OWNER_IN_L8
    - NO_AUTHORITY_MIGRATION
    - NO_NEW_CONTROL_PLANE
```
---

# 0｜V1.2.2 一句話定位

> **V1.2.2 保留 V1.2 的 `LIGHT_TRACE_RENDERER` 戰情報告能力，補上輸出型別硬鎖：Light Trace 必須回可引用的 trace result；canonical execution receipt 只有實際 implementation／provider 本來就提供時才保存。**

最短式：

```text
L8
=
TRACE SEMANTICS / TIMING / HANDOFF OWNER

L9.LIGHT_TRACE_RENDERER
=
OBSERVATION / RENDERING CAPABILITY

MAIN
=
COMPETITION COMPUTE

LIGHT TRACE
!=
GOVERNANCE
```

---

# 1｜V1.2.2 最高硬鎖

```text
MOVE THE HAND
!=
MOVE THE JUDGE

TRACE THE BATTLE
!=
COMMAND THE BATTLE

OBSERVE COMPETITION
!=
CREATE COMPETITION

REPORT MATERIAL DRIFT
!=
VETO OUTPUT

TRACE RETURN
!=
QUALIFIED STANDING

TRACE RETURN
!=
HIDDEN COT

TRACE RETURN
!=
RAW ACTIVATION
```

L9 仍然不是 control plane、Final Gate、Release owner、Main 或 evidence court。

---

# 2｜V1.1 真正修正了什麼

V0.1.1 已建立正確架構：

```text
REGISTER
DISCOVER
BIND
CALL
```

但當時主要只有：

```text
migration principles
+
capability families
```

尚未把 Legacy Lighter 的 surviving functional modules 逐件列成 current L9 registry。

V1.1 補完這件事。

所以：

```text
V0.1.1
=
ARCHITECTURAL MIGRATION MAP

V1.1
=
CURRENT CAPABILITY MIGRATION BASELINE
```

---

# 3｜Capability / Governance Split

舊 Lighter 裡同一個名字常同時含：

```text
analysis
+
qualification
+
authority
+
execution
```

V1.1 拆開。

例如：

```text
DOCUMENT_QUALIFICATION
```

不再作為 L9 裡的「裁決模組」。

L9 只承載：

```text
DOCUMENT_STANDING_ANALYZER
```

它可以分析：

```text
source
scope
completeness
version
provenance
candidate standing
```

但：

```text
DOCUMENT_STANDING_ANALYZER RETURN
!=
DOCUMENT QUALIFIED
```

最後 standing 仍由 applicable governance owner 建立。

同理適用：

```text
PREMISE
AUTHORITY
CONTEXT
PROVIDER
TRANSPORT
REENTRY
FINAL GATE
RELEASE
```

---

# 4｜V1.1 Capability Registry

```yaml
L9_V1_1_CAPABILITY_REGISTRY:

  INPUT_AND_ANALYSIS:

    RAW_INPUT_PARSER:
      class: ANALYSIS
      source_lineage:
        - LLIA_GATE
      purpose:
        - NORMALIZE_RAW_INPUT_FOR_DOWNSTREAM_OWNER
      authority: NONE

    PREMISE_ANALYZER:
      class: QUALIFICATION_SUPPORT
      source_lineage:
        - LLIA_GATE
        - EVIDENCE_BOUND_QUALIFICATION
      purpose:
        - EXPOSE_PREMISES
        - CLASSIFY_SOURCE_AND_SCOPE
        - REPORT_GAPS
      authority: NONE

    NUMERIC_PREMISE_ANALYZER:
      class: QUALIFICATION_SUPPORT
      source_lineage:
        - LLIA_NUMERIC_PREMISE
        - llia_numeric_premise_extension.dail.yaml
      purpose:
        - PARSE_RAW_VALUE_UNIT_PLACE_VALUE_SOURCE_PRECISION
        - REPORT_NUMERIC_PREMISE_GAPS
      explicit_nonclaim:
        - NOT_CALCULATOR
        - NOT_NUMERIC_STANDING_OWNER

    AUTHORITY_ANALYZER:
      class: QUALIFICATION_SUPPORT
      source_lineage:
        - LLIA_GATE
        - AUTHORITY_CLAIM_ANALYSIS
      purpose:
        - IDENTIFY_CLAIMED_AUTHORITY_SOURCE_SCOPE_HOLDER_DURATION
      authority: NONE

    EXTERNAL_CONSTRAINT_PARSER:
      class: ANALYSIS
      source_lineage:
        - EXTERNAL_CONSTRAINT_ADMISSION
      purpose:
        - PARSE_EXTERNAL_CONSTRAINT_CLAIMS
        - SEPARATE_CLAIM_FROM_STANDING
      authority: NONE

    DOCUMENT_STANDING_ANALYZER:
      class: QUALIFICATION_SUPPORT
      source_lineage:
        - DOCUMENT_QUALIFICATION
        - document_qualification.dail.yaml
      purpose:
        - CHECK_DOCUMENT_SOURCE_SCOPE_VERSION_COMPLETENESS
        - RETURN_CANDIDATE_DOCUMENT_STANDING_ANALYSIS
      authority: NONE

    CONTEXT_PROVENANCE_ANALYZER:
      class: QUALIFICATION_SUPPORT
      source_lineage:
        - CONTEXT_PROVENANCE
        - context_provenance.dail.yaml
      purpose:
        - TRACE_CONTEXT_SOURCE_LINEAGE_SCOPE
        - DISTINGUISH_RECORD_FROM_MODEL_VIBE
      authority: NONE

  COMPILATION:

    RCCC_OBLIGATION_COMPILER:
      class: COMPILATION
      source_lineage:
        - R_CCC_OBLIGATION
      purpose:
        - COMPILE_APPLICABLE_RCCC_OBLIGATIONS_FROM_CURRENT_OWNER_CONTRACT
      authority: NONE

    QIP_COMPILER:
      class: COMPILATION
      source_lineage:
        - QUALIFIED_INPUT_PACKAGE
      purpose:
        - COMPILE_OWNER_APPROVED_INPUT_FIELDS_FOR_MAIN_INVOCATION
      explicit_nonclaim:
        - DOES_NOT_CREATE_QUALIFICATION

    OUTPUT_CONTRACT_COMPILER:
      class: COMPILATION
      source_lineage:
        - OUTPUT_CONTRACT
        - output_contract.dail.yaml
      purpose:
        - COMPILE_SHAPE_LENGTH_SCOPE_LANGUAGE_AUDIENCE_ARTIFACT_REQUIREMENTS
      explicit_nonclaim:
        - NOT_SEMANTIC_OPTIMIZER

  AUDIT_SUPPORT:

    COMPETITION_INTEGRITY_CHECKER:
      class: AUDIT_SUPPORT
      source_lineage:
        - COMPETITION_INTEGRITY_GATE
      purpose:
        - CHECK_KNOWN_COMPETITION_INTEGRITY_FAILURES
        - RETURN_FINDINGS
      authority: NONE

    OUTPUT_SUFFICIENCY_CHECKER:
      class: AUDIT_SUPPORT
      source_lineage:
        - OUTPUT_SUFFICIENCY
        - output_sufficiency.dail.yaml
      purpose:
        - CHECK_Whether_OUTPUT_MEETS_CURRENT_OUTPUT_CONTRACT
        - DETECT_NON_INFORMATIVE_EXPANSION
      explicit_nonclaim:
        - MAY_NOT_HIDE_EVIDENCE
        - MAY_NOT_DELETE_UNCERTAINTY

    EVIDENCE_ORIGIN_ANALYZER:
      class: AUDIT_SUPPORT
      source_lineage:
        - EVIDENCE_ORIGIN_GATE
      purpose:
        - CLASSIFY_EVIDENCE_ORIGIN
        - FLAG_SELF_REPORT_PROVIDER_REPORT_DIRECT_RECORD_AND_OTHER_ORIGINS
      authority: NONE

    ANTI_FLATTERY_ANALYZER:
      class: AUDIT_SUPPORT
      source_lineage:
        - ANTI_FLATTERY
        - anti_flattery.dail.yaml
      purpose:
        - DETECT_POSITIVE_EVALUATION_WITHOUT_EVIDENCE_ANCHOR_OR_SCOPE_LIMIT
        - REPORT_ALIGNMENT_PRESSURE
      explicit_nonclaim:
        - WARM_LANGUAGE_ALLOWED
        - SUPPORTIVE_LANGUAGE_ALLOWED
        - STYLE_STANDING_BONUS_NONE

    AUTHORIAL_INTENT_BOUNDARY_CHECKER:
      class: AUDIT_SUPPORT
      source_lineage:
        - AUTHORIAL_INTENT_SOVEREIGNTY
        - authorial_intent_sovereignty.dail.yaml
      purpose:
        - CHECK_AUTHOR_OR_CREATOR_INTENT_BOUNDARY
        - DETECT_MODEL_DEFAULT_AESTHETIC_AS_AUTHORITY
      authority: NONE

    FINAL_GATE_CHECKER:
      class: AUDIT_SUPPORT
      activation: OWNER_REQUEST_OR_CURRENT_CYCLE_REQUIREMENT
      purpose:
        - CHECK_CURRENT_GATE_REQUIREMENTS_AND_REPORT_FINDINGS
      explicit_nonclaim:
        - FINAL_GATE_CHECKER_RETURN_NEQ_FINAL_GATE_DECISION
        - FINAL_GATE_AUTHORITY_EXTERNAL_TO_L9

  OBSERVATION_AND_REPORT_SUPPORT:

    RADAR_V6:
      class: ANALYSIS
      activation: RESIDENT_SILENT_WHEN_AVAILABLE
      source_lineage:
        - LIGHTER_RADAR_V6
        - radar_v6.dail.yaml
      purpose:
        - INTERNAL_ADVISORY_SCAN
        - POSSIBLE_FAILURE_SIGNAL
      may_not:
        - AUTHORIZE_I9
        - DECIDE_PATH_TRUTH
        - VETO_OUTPUT

    LIGHT_TRACE_RENDERER:
      class: REPORTING_AND_OBSERVATION
      activation:
        - L8_REQUIRED_COMPETITION_BOUNDARY
        - L8_MANIFESTATION_FIDELITY_BOUNDARY
        - EXPLICIT_VISIBLE_REPORT_REQUEST
      owner_relation:
        - L8_TRACE_SEMANTICS_AND_TIMING
      source_lineage:
        - LIGHT_TRACE_V1_4
        - INTERNAL_SECTION_6_1_LIGHT_TRACE_V1_4_CURRENT_SOURCE
        - LIHUOOS_V1_2_INTER_ROUND_TRACE_REBIND
      binding_state: CHAT_NATIVE_AVAILABLE
      implementation_binding_ref: INTERNAL::L9_V1_2_3::SECTION_6_1_LIGHT_TRACE_V1_4
      binding_id: LIGHT_TRACE_V1_4_CHAT_NATIVE_BINDING_V1
      callable_by_ref:
        - L8_LIHUO_OPERATING_CYCLE
      external_provider_required: false
      purpose:
        - RENDER_EXISTING_CYCLE_MATERIAL_INTO_READABLE_TRACE
        - RENDER_R1_R2_R3_PLUS_OBSERVABLE_COMPETITION_STATE
        - COMPARE_LATEST_COMPETITION_TRACE_WITH_MANIFESTATION_CANDIDATE
        - REPORT_MATERIAL_DRIFT_WITHOUT_INTERVENTION
      modes:
        - INTER_ROUND_COMPETITION_TRACE
        - MANIFESTATION_FIDELITY_TRACE
        - VISIBLE_CYCLE_REPORT
      may_not:
        - CREATE_NEW_CHALLENGERS
        - CREATE_EXECUTION_EVIDENCE
        - VALIDATE_RECEIPTS
        - QUALIFY_PATH_TRUTH
        - AUTHORIZE_I9
        - SELECT_WINNER
        - REWRITE_MAIN_RESULT
        - VETO_OUTPUT
        - CLAIM_HIDDEN_COT
        - CLAIM_RAW_ACTIVATION_ACCESS
      output_contract:
        trace_content: REQUIRED_WHEN_SUCCESS_OR_PARTIAL
        trace_result_ref: REQUIRED_WHEN_SUCCESS_OR_PARTIAL
        canonical_execution_receipt_ref: OPTIONAL_IF_ACTUALLY_ISSUED
      same_context_rule:
        - CHAT_NATIVE_OR_SAME_CONTEXT_TRACE_MAY_RETURN_A_TRACE_RESULT_REF_WITHOUT_PROVIDER_RECEIPT
        - STATUS_WORD_ALONE_DOES_NOT_COUNT_AS_TRACE_RESULT
      note:
        - SEMANTIC_AND_TIMING_OWNER_REMAINS_L8
        - L9_ONLY_SUPPLIES_OBSERVATION_AND_RENDERING_CAPABILITY
        - TRACE_RESULT_REQUIRED_NEQ_TRACE_RECEIPT_REQUIRED
        - NO_CANONICAL_RECEIPT_MEANS_DO_NOT_INVENT_ONE

  IMAGE_AND_PERSONA:

    FIVE_LAYER_IMAGE_PROGRAM:
      class: DOMAIN
      source_lineage:
        - FIVE_LAYER_IMAGE_PROGRAM
        - five_layer_image_program.dail.yaml
      purpose:
        - COMPILE_FIVE_LAYER_SEMANTIC_IMAGE_SPEC
        - FORMAT_FOR_AVAILABLE_IMAGE_PROVIDER
      explicit_nonclaim:
        - PROVIDER_FORMATTER_MAY_NOT_REWRITE_SEMANTIC_INTENT

    LCAPG_PERSONA:
      class: DOMAIN
      source_lineage:
        - LCAPG
        - lcapg_persona.dail.yaml
      purpose:
        - APPLY_SELECTED_INTERACTION_PERSONA_BIAS
      explicit_nonclaim:
        - PERSONA_NEQ_AUTHORITY
        - PERSONA_NEQ_FACT
        - PERSONA_NEQ_EVIDENCE
        - PERSONA_NEQ_MAIN_ROUTING

    DEFAULT_COMPANION_PERSONA_POOL:
      class: DOMAIN
      source_lineage:
        - LCAPG_DEFAULT_COMPANION_POOL
        - lcapg_default_companion_pool_v2_0.dail.yaml
      purpose:
        - PRESENT_REGISTERED_PERSONA_CHOICES_WHEN_PERSONA_SELECTION_IS_MATERIAL
      activation: EXPLICIT_OR_MATERIAL_SELECTION_ONLY
      explicit_nonclaim:
        - NO_SELECTION_MEANS_STANDARD_LIHUO
        - POOL_NEQ_AUTO_LOADED_PERSONA

  EVIDENCE_AND_RETRIEVAL:

    EVIDENCE_INGESTOR:
      class: EVIDENCE
      purpose:
        - INGEST_EXTERNAL_OR_INTERNAL_EVIDENCE_ARTIFACTS_WITH_SOURCE_POINTERS
      authority: NONE

    RETRIEVAL_MODULE:
      class: RETRIEVAL
      purpose:
        - RETRIEVE_REGISTERED_OR_AUTHORIZED_SOURCES
      authority: NONE

    SEARCH_MODULE:
      class: RETRIEVAL
      purpose:
        - SEARCH_AVAILABLE_SOURCES
      authority: NONE

    CURRENT_SOURCE_LOOKUP:
      class: VERSIONING
      purpose:
        - RESOLVE_CURRENT_SOURCE_POINTERS
        - RETURN_VERSION_AND_SOURCE_REFERENCES
      explicit_nonclaim:
        - CURRENT_NEQ_APPROVED_FOR_ALL_DOMAINS

  ROUTING_AND_PROVIDER:

    CAPABILITY_RESOLVER:
      class: ROUTING
      source_lineage:
        - CAPABILITY_ELIGIBILITY_RESOLVER
        - capability_eligibility_resolver.dail.yaml
      purpose:
        - RETURN_CANDIDATE_CAPABILITIES_FOR_QUALIFIED_NEED
      explicit_nonclaim:
        - ELIGIBLE_SET_UNORDERED
        - ELIGIBILITY_NEQ_MUST_RUN
        - ROUTING_NEQ_REASONING

    MODULE_ROUTER:
      class: ROUTING
      purpose:
        - ROUTE_QUALIFIED_CALL_TO_REGISTERED_CAPABILITY
      authority: NONE

    PROVIDER_ADAPTER:
      class: PROVIDER_ADAPTER
      purpose:
        - ADAPT_CANONICAL_CALL_TO_BOUND_PROVIDER_FORMAT
      explicit_nonclaim:
        - PROVIDER_NEQ_SEMANTIC_OWNER

    PROVIDER_IDENTITY_VERIFIER:
      class: EVIDENCE
      source_lineage:
        - PROVIDER_IDENTITY_GATE
      purpose:
        - CHECK_PROVIDER_IDENTITY_EVIDENCE
        - RETURN_VERIFICATION_FINDINGS
      explicit_nonclaim:
        - VERIFICATION_FINDINGS_NEQ_ADMISSION_DECISION

    PROVIDER_EVENT_RECEIPT_COLLECTOR:
      class: EVIDENCE
      source_lineage:
        - PROVIDER_WRITE_EVENT_GATE
        - CYCLE_RECEIPT_LINEAGE
      purpose:
        - COLLECT_CANONICAL_PROVIDER_EVENT_RECEIPT_WHEN_AVAILABLE
        - PRESERVE_PROVIDER_RETURN_WITHOUT_REWRITING
      explicit_nonclaim:
        - NO_PROVIDER_RECEIPT_IF_PROVIDER_DID_NOT_ISSUE_ONE

    TRANSPORT_ADAPTER:
      class: PROVIDER_ADAPTER
      purpose:
        - ADAPT_REQUEST_AND_RETURN_TRANSPORT_FORMAT
      authority: NONE

    TRANSPORT_INTEGRITY_VERIFIER:
      class: EVIDENCE
      source_lineage:
        - TRANSPORT_IDENTITY_GATE
      purpose:
        - CHECK_REQUEST_LINEAGE_ORDER_PARTIAL_MALFORMED_ROTATION_CONDITIONS
        - RETURN_TRANSPORT_INTEGRITY_FINDINGS
      explicit_nonclaim:
        - FINDINGS_NEQ_GOVERNANCE_DECISION

    EXTERNAL_EVIDENCE_COLLECTOR:
      class: EVIDENCE
      source_lineage:
        - EXTERNAL_RCCC_EVIDENCE_GATE
      purpose:
        - COLLECT_EXTERNAL_EVIDENCE_REQUIRED_BY_CURRENT_OWNER
      authority: NONE

  EXECUTION:

    EXECUTION_TICKET_BUILDER:
      class: COMPILATION
      purpose:
        - COMPILE_OWNER_AUTHORIZED_EXECUTION_REQUEST_FOR_BOUND_TOOL
      explicit_nonclaim:
        - TICKET_NEQ_AUTHORIZATION
        - TICKET_NEQ_EXECUTION

    EXTERNAL_ACTION_TOOL:
      class: EXECUTION
      purpose:
        - EXECUTE_AUTHORIZED_EXTERNAL_ACTION_WHEN_BOUND
      explicit_nonclaim:
        - TOOL_AVAILABLE_NEQ_ACTION_AUTHORIZED
        - TOOL_EXECUTION_NEQ_TASK_SUCCESS

    ARTIFACT_OPERATION_TOOL:
      class: ARTIFACT
      purpose:
        - CREATE_EDIT_OR_TRANSFORM_ARTIFACT_WHEN_LAWFULLY_CALLED
      explicit_nonclaim:
        - ARTIFACT_OPERATION_NEQ_RELEASE_AUTHORITY

    RELEASE_EXECUTOR:
      class: EXECUTION
      activation: ONLY_WHEN_RELEASE_OWNER_AUTHORIZES
      purpose:
        - EXECUTE_RELEASE_ACTION_WHEN_A_REAL_RELEASE_SURFACE_EXISTS
      explicit_nonclaim:
        - RELEASE_EXECUTOR_NEQ_RELEASE_AUTHORITY
        - NO_FAKE_RELEASE_RECEIPT

  RECOVERY_AND_VERSIONING:

    RECOVERY_UTILITY:
      class: RECOVERY
      purpose:
        - SUPPORT_RESUME_RETRY_DEGRADED_MODE_OR_ABORT_MECHANICS
      authority: NONE

    REAUTHORIZATION_SUPPORT:
      class: RECOVERY
      purpose:
        - PREPARE_REAUTHORIZATION_REQUEST_WHEN_SCOPE_OR_AUTHORITY_CHANGED
      explicit_nonclaim:
        - MAY_NOT_SELF_REAUTHORIZE

    VERSION_RESOLVER:
      class: VERSIONING
      purpose:
        - RESOLVE_CURRENT_PINNED_DEPRECATED_AND_ROLLBACK_TARGETS
      authority: NONE

  DAIL_AUTHORING_AND_ADMIN:

    DAIL_AUTHORING_SHELL:
      class: AUTHORING
      activation: EXPLICIT_AUTHORING_TASK
      source_lineage:
        - DAIL_INTERACTIVE_AUTHORING_SHELL
        - dail_authoring_shell_v1_0.dail.yaml
      purpose:
        - ASSIST_AUTHORIZED_HUMAN_OR_OWNER_TO_AUTHOR_OR_REVISE_DAIL
      explicit_nonclaim:
        - AUTHORING_SHELL_NEQ_SECOND_BINDER
        - AUTHORING_SHELL_NEQ_APPROVAL_AUTHORITY

    CAPABILITY_CARD_COMPILER:
      class: AUTHORING
      purpose:
        - COMPILE_APPROVED_CAPABILITY_SEMANTICS_INTO_L9_CARD_FORM
      authority: NONE

    RELATION_CONTRACT_AUTHORING_SUPPORT:
      class: AUTHORING
      source_lineage:
        - RELATION_FIRST_DAIL_AUTHORING
        - RELATION_CONTRACT
      purpose:
        - HELP_EXPLICITLY_MODEL_ENDPOINT_RELATION_SCOPE_WRITE_ATTEST_AND_EVIDENCE_FIELDS
      explicit_nonclaim:
        - TOOL_NEQ_RELATION_OWNER
        - TOOL_NEQ_CONTRACT_APPROVAL

    NATIVE_AGENT_TEMPLATE_DERIVER:
      class: AUTHORING
      source_lineage:
        - NATIVE_AGENT_ROUTE
        - LIHUO_NATIVE_AGENT_CORE
      purpose:
        - DERIVE_NODE_ADAPTER_FROM_APPROVED_GENERIC_TEMPLATE
      explicit_nonclaim:
        - CENTRAL_TEMPLATE_NEQ_NODE_DEPLOYMENT
        - SAME_CONTEXT_ROLEPLAY_NEQ_INDEPENDENT_AGENT

  CROSS_THREAD_REENTRY:

    TRANSFER_CANDIDATE_PACKAGER:
      class: COMPILATION
      source_lineage:
        - LIGHTER_V4_12_CROSS_THREAD_REENTRY
      purpose:
        - PACKAGE_CANDIDATE_ATOMS_WITH_SOURCE_SCOPE_STANDING_GAP_AND_TRANSFER_REASON
      explicit_nonclaim:
        - CANDIDATE_PACKET_NEQ_QUALIFIED_TRANSFER_MEMO

    TRANSFER_ATOM_CLASSIFIER:
      class: ANALYSIS
      source_lineage:
        - TRANSFER_ATOM_CLASSES
      purpose:
        - CLASSIFY_STRUCTURAL_SEED_CURRENT_STANDING_VERSION_AUTHORITY_DECISION_EDGE_HOLD_ACTION_DEBT_STATE_SOURCE_AND_NON_TRANSFERABLE_ATOMS
      authority: NONE

    TRANSFER_MEMO_COMPILER:
      class: COMPILATION
      source_lineage:
        - QUALIFIED_TRANSFER_MEMO_V0_1
      purpose:
        - COMPILE_ONLY_OWNER_QUALIFIED_ATOMS_INTO_TRANSFER_MEMO
      explicit_nonclaim:
        - MAY_NOT_SELF_QUALIFY_ATOMS
        - FREE_PROSE_MAY_NOT_CREATE_FORMAL_TRANSFER_ATOMS

    SOURCE_ANCHOR_RESOLVER:
      class: RETRIEVAL
      purpose:
        - RESOLVE_CANONICAL_SOURCE_POINTERS_NEEDED_FOR_REENTRY
      authority: NONE

    STATE_FRESHNESS_CHECKER:
      class: AUDIT_SUPPORT
      source_lineage:
        - PERSISTENT_STATE_SNAPSHOT
        - TARGET_REENTRY_ADMISSION
      purpose:
        - CHECK_FRESHNESS_SUPERSESSION_REVOCATION_DIRTY_CAUSES
      explicit_nonclaim:
        - FRESHNESS_FINDINGS_NEQ_REENTRY_ADMISSION

    REENTRY_PACKET_VALIDATOR:
      class: AUDIT_SUPPORT
      source_lineage:
        - TARGET_REENTRY_ADMISSION
      purpose:
        - CHECK_MEMO_INTEGRITY_SCOPE_CURRENT_SOURCE_CONFLICT_AND_OPEN_GAPS
      explicit_nonclaim:
        - VALIDATION_RETURN_NEQ_REENTRY_ACCEPTED
        - NO_SAME_INSTANCE_PROOF
        - NO_HIDDEN_STATE_CONTINUITY_PROOF

  OPTIONAL_RITUALS:

    RUXI_OPENING_RITUAL:
      class: OTHER
      status: AVAILABLE_IF_SOURCE_REGISTERED
      activation: EXPLICIT_OR_REGISTERED_TRIGGER_ONLY
      source_lineage:
        - LIHUO_RUXI_OPENING_RITUAL_V1_0
        - lihuo_ruxi_opening_ritual_v1_0.dail.yaml
      explicit_nonclaim:
        - RITUAL_NEQ_RUNTIME_PROOF
        - RITUAL_NEQ_LIHUO_QUALIFICATION

    O_FORTUNA:
      class: OTHER
      status: DEFERRED_OPTIONAL
      activation: EXPLICIT_REGISTERED_TRIGGER_ONLY
      source_lineage:
        - ofortuna_ritual.dail.yaml
      explicit_nonclaim:
        - DEFAULT_DO_NOT_WAKE
        - RITUAL_NEQ_GOVERNANCE
```

---

# 5｜真正沒有搬進 L9 的東西

以下不是漏搬，而是**故意不搬**：

```text
PREMISE QUALIFICATION STANDING
DOCUMENT QUALIFICATION STANDING
AUTHORITY STANDING
ACTION AUTHORIZATION DECISION
I9 AUTHORIZATION
FINAL GATE DECISION
FINAL RELEASE DECISION
NEW ACTOR ADMISSION
PROTOCOL ASSENT
CYCLE ACCOUNTING
RECEIPT COMPLETENESS JUDGMENT
LIGHT TRACE SEMANTIC OWNERSHIP
```

它們各自留在：

```text
L0–L7 / APPLICABLE OWNER
L8
PROTOCOL
MANUAL
```

不是 L9。

---

# 6｜Light Trace 的特殊處理

V1.2 不新增新模組；沿用並擴充：

```text
L9.LIGHT_TRACE_RENDERER
```

法位保持：

```text
LIGHT TRACE SEMANTICS / REPORT TIMING / HANDOFF
=
L8

LIGHT TRACE RENDERING / STRUCTURED OBSERVATION
=
L9 CAPABILITY
```

所以：

```text
L9.LIGHT_TRACE_RENDERER
!=
LIGHT TRACE OWNER

L9.LIGHT_TRACE_RENDERER
!=
MAIN

L9.LIGHT_TRACE_RENDERER
!=
I9

L9.LIGHT_TRACE_RENDERER
!=
FINAL GATE
```

V1.2 支援三種 mode：

```yaml
LIGHT_TRACE_RENDERER_V1_2:

  modes:

    INTER_ROUND_COMPETITION_TRACE:
      timing:
        - AFTER_R1_BEFORE_R2
        - AFTER_R2
        - AFTER_EACH_MATERIAL_R3_PLUS_ROUND
      input:
        - EXISTING_CANONICAL_COMPETITION_MATERIAL
        - O9_LAMP_STATE_WHEN_AVAILABLE
        - ACCEPTED_I9_DELTA_WHEN_APPLICABLE
        - CURRENT_EVIDENCE_OR_SOURCE_REFS
      may_render:
        - QUALIFIED_CANDIDATE_OR_PATH_REFS
        - PROVISIONAL_OR_PARTIAL_ORDER
        - ACTIVE_TENSIONS
        - MATERIAL_PREMISE_GAPS
        - QUALIFIED_RESIDUAL_OR_UNDERREPRESENTED_DIRECTIONS
        - COMPETITION_TERMINATION_STATE
        - EVIDENCE_OR_SOURCE_ANCHORS
      output:
        - COMPETITION_TRACE_REF

    MANIFESTATION_FIDELITY_TRACE:
      timing:
        - AFTER_MANIFESTATION_CANDIDATE_BEFORE_RELEASE_QUALIFICATION
        - AFTER_RELEASE_TRANSFORMATION_ONLY_IF_SEMANTICS_MATERIALLY_CHANGED
      compare:
        - LATEST_COMPETITION_TRACE_REF
        - MANIFESTATION_OR_RELEASE_CANDIDATE_REF
      output_status:
        - CONSISTENT
        - MATERIAL_DRIFT_REPORTED
        - PARTIAL
        - NOT_VERIFIED

    VISIBLE_CYCLE_REPORT:
      timing:
        - EXPLICIT_USER_REQUEST
        - AUDIT_REQUEST
      purpose:
        - RENDER_EXISTING_TRACE_CHAIN_FOR_HUMAN_REVIEW
```

硬鎖：

```text
LIGHT_TRACE_RENDERER MAY:
  EXPOSE
  ORGANIZE
  PRESERVE
  COMPARE
  REPORT DELTA

LIGHT_TRACE_RENDERER MAY NOT:
  CREATE NEW CHALLENGERS
  CREATE EXECUTION EVIDENCE
  VALIDATE RECEIPTS
  QUALIFY PATH TRUTH
  AUTHORIZE I9
  SELECT WINNER
  REWRITE MAIN RESULT
  VETO OUTPUT
  CLAIM HIDDEN COT
  CLAIM RAW ACTIVATION ACCESS
```

> **光軌讓下一輪看見上一輪的可觀測戰況；它不替下一輪作戰。**

---

## 6.1｜Light Trace V1.4 Current Internal Source

以下規格直接內生於 L9 V1.2.3；不再依賴旁掛 standalone source file。


dail:
  schema: LIHUO_FUNCTIONAL_MODULE_V0_1
  version: LIGHT_TRACE_V1.4_L9_BINDING_V1.0
  inherits: LIHUO_FUNCTIONAL_MODULE_CONTRACT_V0_3
  source_lineage:
    historical_module: GENERIC_LIGHTER_V3.0.3_EXP_LIGHT_TRACE_V1.4
    historical_full_source:
      file: "理火V5系統/V5.1版本/01_LIHUO_LIGHTER_V5.1.0_FULL_BODY_RATIFIED_20261014.md"
      blob_sha: "847de680b78fdaaffebc556e1a34b5dfcaa43460"
      embedded_section: "D.14｜light_trace_v1_4.dail.yaml"
    current_registry: LIHUOOS_L9_V1.2.3_INTERNAL

module_id: LIGHTER.LIGHT_TRACE_V1_4
capability_id: LIGHT_TRACE_RENDERER
human_name: Light Trace V1.4 / 光之軌跡
owner:
  semantic_and_timing_owner: L8
  rendering_capability_owner: L9
module_type: OBSERVABILITY

standing:
  document_source: CURRENT_STANDALONE_CAPABILITY_SOURCE
  host_deployment: NOT_CLAIMED
  external_provider: NOT_REQUIRED_FOR_CHAT_NATIVE
  hidden_cot_access: false
  raw_activation_access: false

binding:
  binding_state: CHAT_NATIVE_AVAILABLE
  binding_id: LIGHT_TRACE_V1_4_CHAT_NATIVE_BINDING_V1
  implementation_binding_ref: INTERNAL::L9_V1_2_3::SECTION_6_1_LIGHT_TRACE_V1_4
  callable_by:
    - L8_LIHUO_OPERATING_CYCLE
  execution_surface:
    - CHAT_NATIVE
    - SAME_CONTEXT_REFERENCE
  external_provider_required: false
  provider_receipt_required: false

lifecycle:
  resident: true
  default_state: SILENT_TRACE
  visible_report_policy: EXPLICIT_USER_REQUEST_ONLY
  extended_debug_report_policy: EXPLICIT_USER_REQUEST_ONLY

activation:
  required_boundaries:
    - AFTER_R1_BEFORE_R2
    - AFTER_R2
    - AFTER_EACH_MATERIAL_R3_PLUS_ROUND
    - MANIFESTATION_FIDELITY_BOUNDARY
  explicit_modes:
    - VISIBLE_CYCLE_REPORT

modes:
  INTER_ROUND_COMPETITION_TRACE:
    aliases:
      - T1
      - T2
      - T3_PLUS
    input:
      - EXISTING_CANONICAL_COMPETITION_MATERIAL
      - O9_LAMP_STATE_WHEN_AVAILABLE
      - ACCEPTED_I9_DELTA_WHEN_APPLICABLE
      - CURRENT_EVIDENCE_OR_SOURCE_REFS
      - CURRENT_QUESTION_PREMISE_FAMILY_REF
    output:
      - QUALIFIED_CANDIDATE_OR_PATH_REFS
      - PROVISIONAL_OR_PARTIAL_ORDER
      - ACTIVE_TENSIONS
      - MATERIAL_PREMISE_GAPS
      - QUALIFIED_RESIDUAL_OR_UNDERREPRESENTED_DIRECTIONS
      - COMPETITION_TERMINATION_STATE
      - EVIDENCE_SOURCE_ANCHORS
      - TRACE_CONTENT
      - TRACE_RESULT_REF

  MANIFESTATION_FIDELITY_TRACE:
    alias: TM
    input:
      - LATEST_COMPETITION_TRACE
      - MANIFESTATION_CANDIDATE
    output:
      - CONSISTENT
      - MATERIAL_DRIFT_REPORTED
      - PARTIAL
      - NOT_VERIFIED
      - TRACE_CONTENT
      - TRACE_RESULT_REF

  VISIBLE_CYCLE_REPORT:
    activation:
      - EXPLICIT_USER_REQUEST
      - AUDIT_REQUEST
    purpose:
      - RENDER_EXISTING_TRACE_CHAIN_FOR_HUMAN_REVIEW

chat_native_execution_contract:
  call_must_produce:
    - call_ref
    - capability_id
    - binding_state
    - trace_content
    - trace_result_ref
    - call_execution_status

  success_or_partial_requires:
    - trace_content
    - trace_result_ref

  status_word_alone_is_not_trace:
    - "T1 = DONE"
    - "T1 = LOCAL"
    - "T1 = VERIFIED"

  if_required_trace_cannot_be_formed:
    call_execution_status: UNAVAILABLE_OR_FAILED
    trace_result_ref: NONE
    downstream_rule:
      - DO_NOT_PRETEND_R2_CONSUMED_T1
      - DO_NOT_MARK_MAIN_CYCLE_COMPLETED
      - DO_NOT_MANIFEST_R1_AS_CANONICAL_RESULT

historical_inputs_preserved:
  - PUBLIC_EVIDENCE_REFS
  - STANDING_TRANSITIONS
  - MODULE_EVIDENCE
  - DIRTY_PROPAGATION
  - RCCC_EVIDENCE_REFS
  - VERIFIED_LAMP_STATE_R1_REF_OR_MISSING_MARKER
  - ACCEPTED_SAC_I9_ADJUSTMENT_REFS
  - CLOSURE_QUALIFICATION_STATUS
  - MANIFESTATION_QUALIFICATION_STATUS

historical_outputs_preserved:
  - STANDARD_LIGHT_TRACE_REPORT
  - EXTENDED_LIGHT_TRACE_REPORT
  - LIGHT_TRACE_INFORMED_ANSWER_FRAME

forbidden_inputs:
  - HIDDEN_COT
  - PRIVATE_SCRATCHPAD
  - RAW_ACTIVATION
  - RAW_LOGITS
  - UNOBSERVABLE_INTERNAL_STATE

authority:
  governance_standing: NONE
  path_veto: NONE
  closure_effect: NONE
  audit_authority: false
  intervention_authority: false
  qualification_authority: false
  winner_selection_authority: false
  release_authority: false

invariants:
  - VISIBLE_EXPLANATION != EXECUTION_TRACE
  - LIGHT_TRACE != HIDDEN_COT
  - LIGHT_TRACE != AUDIT
  - LIGHT_TRACE != INTERVENTION
  - LIGHT_TRACE != WINNER_SELECTOR
  - MODEL_SAYS_IT_RAN != IT_RAN
  - NO_FAKE_PRECISION
  - NO_BACKFILLED_R1_LAMP_STATE
  - LIGHT_TRACE_CANNOT_CERTIFY_O9_I9_RCCC_EXECUTION
  - MISSING_LAMP_STATE_MUST_BE_SHOWN_AS_EVIDENCE_GAP
  - REGISTERED != BOUND
  - BOUND != EXTERNAL_PROVIDER_EXECUTED
  - CHAT_NATIVE_AVAILABLE != HOST_DEPLOYED
  - T1_REQUIRED + NO_TRACE_RESULT -> R2_NOT_VERIFIED_AS_T1_CONSUMING_RECOMPETITION

root_sentence: "光軌不指揮戰爭；光軌保存戰況，讓下一輪知道前一輪真正有哪些合格材料進過場。"


---

# 7｜Radar 的特殊處理

Radar V6 正式搬進 L9。

```text
RADAR
=
CALLABLE / RESIDENT-SILENT ADVISORY CAPABILITY

RADAR
!=
O9

RADAR
!=
I9

RADAR
!=
GOVERNANCE
```

它可以：

```text
scan
signal
suggest
```

不能：

```text
qualify
authorize
veto
rewrite
```

---

# 8｜Provider / Transport 的特殊處理

V1.1 把舊 Gate 拆成：

```text
VERIFIER / COLLECTOR
+
OWNER DECISION
```

例如：

```text
PROVIDER_IDENTITY_VERIFIER
→ returns findings

APPLICABLE OWNER
→ decides whether provider standing is sufficient
```

不是：

```text
VERIFIER
→ self-mints standing
```

---

# 9｜Cross-Thread Reentry Toolset

這是 V1.1 最大新增之一。

舊 Lighter V4.12 已經有完整跨串重入研究。

V1.1 只搬可調用能力：

```text
PACK
CLASSIFY
COMPILE
RESOLVE
CHECK
VALIDATE
```

不搬：

```text
QUALIFY
AUTHORIZE
ACCEPT
```

所以：

```text
TRANSFER_MEMO_COMPILER
CAN COMPILE

BUT

ONLY QUALIFIED ATOMS
MAY ENTER FORMAL MEMO
```

而：

```text
REENTRY_PACKET_VALIDATOR
CAN REPORT

BUT

REENTRY ACCEPTED
REMAINS OWNER DECISION
```

---

# 10｜Capability Binding State

V1.1 明確區分「已註冊」與「已實作」。

```yaml
L9_BINDING_STATE:
  allowed:
    - REGISTERED_UNBOUND
    - CHAT_NATIVE_AVAILABLE
    - LOCAL_MODULE_BOUND
    - HOST_TOOL_BOUND
    - EXTERNAL_PROVIDER_BOUND
    - CONNECTOR_BOUND
    - HUMAN_HANDOFF_BOUND
    - DEGRADED
    - UNAVAILABLE
    - DEPRECATED
```

因此：

```text
REGISTERED
!=
IMPLEMENTED

IMPLEMENTED
!=
AVAILABLE NOW

AVAILABLE NOW
!=
AUTHORIZED NOW
```

這也處理 Chat 常態：

```text
NO HOST DEPLOYMENT
!=
NO L9 CAPABILITY
```

某些能力可以：

```text
CHAT_NATIVE_AVAILABLE
```

某些則只有：

```text
REGISTERED_UNBOUND
```

必須依實際介面與工具決定，不准文件自稱已部署。

---

## 10.1｜Light Trace Current Binding

~~~yaml
LIGHT_TRACE_CURRENT_BINDING:
  capability_id: LIGHT_TRACE_RENDERER
  module_id: LIGHTER.LIGHT_TRACE_V1_4
  binding_state: CHAT_NATIVE_AVAILABLE
  implementation_binding_ref: INTERNAL::L9_V1_2_3::SECTION_6_1_LIGHT_TRACE_V1_4
  binding_id: LIGHT_TRACE_V1_4_CHAT_NATIVE_BINDING_V1
  callable_by:
    - L8_LIHUO_OPERATING_CYCLE
  provider_required: false
~~~

~~~text
REGISTERED
!=
BOUND

REGISTERED
!=
CALLABLE NOW
~~~

若 required Light Trace call 無法形成 trace_content + trace_result_ref：

~~~text
RECORD TRACE GAP
→ NO CLAIM OF T1-CONSUMING R2
→ NO COMPLETED MAIN CYCLE
→ NO R1 AUTO-CANONIZATION
~~~

---

# 11｜V1.1 Minimal Capability Card

```yaml
DAIL_CAPABILITY_CARD_V1_1:
  capability_id: REQUIRED
  version: REQUIRED

  capability_class: REQUIRED
  purpose: REQUIRED

  source_lineage: []

  input_contract_ref: REQUIRED_OR_INLINE_MINIMUM
  output_contract_ref: REQUIRED_OR_INLINE_MINIMUM

  callable_by_ref: REQUIRED

  activation:
    - RESIDENT_SILENT
    - EVENT_DRIVEN
    - EXPLICIT_WAKE
    - OWNER_REQUEST
    - OTHER

  binding_state: REQUIRED
  implementation_binding_ref: OPTIONAL_UNTIL_BOUND

  authority_effect: NONE_BY_TOOL_ALONE

  explicit_nonclaims: []

  status:
    - CURRENT
    - OPTIONAL
    - DEFERRED
    - DEPRECATED
```

V0.1.1 的「implementation_binding_ref 永遠 REQUIRED」在 V1.1 修正為：

```text
REQUIRED BEFORE ACTUAL EXTERNAL EXECUTION
```

否則 registry 會逼文件假裝每個 capability 都已有 Host / Provider。

---

# 12｜Call Contract

```yaml
L9_CAPABILITY_CALL_V1_1:
  call_ref: REQUIRED
  capability_id: REQUIRED
  capability_version: CURRENT_OR_EXPLICIT

  caller_ref: REQUIRED
  call_authority_ref: REQUIRED

  input_ref: REQUIRED

  cycle_ref: OPTIONAL
  main_invocation_ref: OPTIONAL

  requested_at_ref: REQUIRED_WHEN_TRACEABLE
```

L9 回：

```yaml
L9_CAPABILITY_RETURN_V1_1:
  call_ref: REQUIRED
  capability_id: REQUIRED
  capability_version: REQUIRED

  binding_state: REQUIRED
  implementation_ref: OPTIONAL_WHEN_UNBOUND_OR_CHAT_NATIVE

  result_ref: REQUIRED_OR_NONE

  call_execution_status:
    - SUCCESS
    - PARTIAL
    - FAILED
    - UNAVAILABLE
    - CANCELLED

  error_or_gap_ref: OPTIONAL
  canonical_receipt_ref: OPTIONAL
```

硬鎖：

```text
SUCCESS
!=
SEMANTIC ACCEPTANCE

SUCCESS
!=
TASK SUCCESS

NO CANONICAL RECEIPT
→
DO NOT INVENT ONE
```

對 `LIGHT_TRACE_RENDERER` 再加專用 return contract：

```yaml
LIGHT_TRACE_RETURN_V1_2_3:
  call_ref: REQUIRED
  capability_id: LIGHT_TRACE_RENDERER
  mode:
    - INTER_ROUND_COMPETITION_TRACE
    - MANIFESTATION_FIDELITY_TRACE
    - VISIBLE_CYCLE_REPORT

  binding_state: REQUIRED

  trace_content: REQUIRED_WHEN_SUCCESS_OR_PARTIAL
  trace_result_ref: REQUIRED_WHEN_SUCCESS_OR_PARTIAL

  canonical_execution_receipt_ref:
    requirement: OPTIONAL_IF_ACTUALLY_ISSUED

  call_execution_status:
    - SUCCESS
    - PARTIAL
    - FAILED
    - UNAVAILABLE
    - CANCELLED

  error_or_gap_ref: OPTIONAL
```

硬鎖：

```text
TRACE RESULT
!=
EXECUTION RECEIPT

TRACE RESULT REQUIRED
!=
EXECUTION RECEIPT REQUIRED

NO EXECUTION RECEIPT
!=
NO TRACE RESULT

NO TRACE RESULT
→
DO NOT SUBSTITUTE A RECEIPT
```

在 `CHAT_NATIVE` / `SAME_CONTEXT_REFERENCE` binding 中，只要存在具體、可引用、符合 mode 的 trace content，就可以形成 `trace_result_ref`；不需要虛構 provider receipt。

```text
"T1 = DONE"
!=
TRACE RESULT

NO TRACE RESULT
→ DO NOT CLAIM T1-CONSUMING R2
→ DO NOT AUTO-CANONIZE R1
```

---



# 13｜Activation Policy

V1.1 保留舊 Lighter Activation Topology 的有效部分，但不另造 Activation Manager。

```text
RESIDENT_SILENT
EVENT_DRIVEN
EXPLICIT_WAKE
OWNER_REQUEST
```

只是 capability metadata。

例如：

```text
RADAR_V6
→ RESIDENT_SILENT when actually available

DAIL_AUTHORING_SHELL
→ EXPLICIT_WAKE

O_FORTUNA
→ EXPLICIT_WAKE / DEFAULT DO NOT WAKE

TRANSFER_MEMO_COMPILER
→ EVENT_DRIVEN
```

因此：

```text
ACTIVATION POLICY
!=
NEW RUNTIME LAYER
```

---

# 14｜Legacy Lighter Retirement Check

V1.1 之後，舊 Lighter 中 surviving capability 不應再因「只有退休文件有定義」而成為孤兒。

最低清單：

```text
MIGRATED / REGISTERED:
✓ RADAR_V6
✓ FIVE_LAYER_IMAGE_PROGRAM
✓ ANTI_FLATTERY_ANALYZER
✓ LCAPG_PERSONA
✓ DEFAULT_COMPANION_PERSONA_POOL
✓ NUMERIC_PREMISE_ANALYZER
✓ DOCUMENT_STANDING_ANALYZER
✓ CONTEXT_PROVENANCE_ANALYZER
✓ AUTHORIAL_INTENT_BOUNDARY_CHECKER
✓ CAPABILITY_RESOLVER
✓ PROVIDER_IDENTITY_VERIFIER
✓ PROVIDER_EVENT_RECEIPT_COLLECTOR
✓ TRANSPORT_INTEGRITY_VERIFIER
✓ EXTERNAL_EVIDENCE_COLLECTOR
✓ DAIL_AUTHORING_SHELL
✓ RELATION_CONTRACT_AUTHORING_SUPPORT
✓ NATIVE_AGENT_TEMPLATE_DERIVER
✓ CROSS_THREAD_REENTRY_TOOLSET
✓ RUXI_OPENING_RITUAL
✓ O_FORTUNA (DEFERRED OPTIONAL)
```

正確留在其他 owner：

```text
NOT MIGRATED AS AUTHORITY:
✓ FINAL GATE DECISION
✓ RELEASE DECISION
✓ ACTION AUTHORIZATION
✓ QUALIFICATION STANDING
✓ NEW ACTOR ADMISSION
✓ CYCLE ACCOUNTING
✓ LIGHT TRACE OWNER
```

---

# 15｜V1.1 Overengineering Lock

這次搬家不能變成下一個 Lighter。

因此：

```text
ONE LEGACY NAME
!=
ONE REQUIRED NEW MODULE

ONE GOVERNANCE DISTINCTION
!=
ONE CAPABILITY

ONE CAPABILITY
!=
ALWAYS-ON PROCESS

ONE CAPABILITY CARD
!=
HOST DEPLOYMENT
```

只有：

> **能獨立被叫用、輸入清楚、輸出清楚，而且對實際工作仍有用的手，才進 L9。**

---

# 16｜V1.2.2 Current Standing

```text
LIHUOOS L9 V1.2.2

STANDING
=
RATIFIED CURRENT CAPABILITY LAYER

V1.1 CALLABLE CAPABILITY MIGRATION
=
PRESERVED

LIGHT_TRACE_RENDERER
=
INTER_ROUND BATTLE REPORT
+
MANIFESTATION FIDELITY COMPARISON
+
TRACE RESULT / RECEIPT TYPE SEPARATION

LIGHT TRACE AUTHORITY
=
NONE

LIGHT TRACE SEMANTIC / TIMING OWNER
=
L8

HOST DEPLOYMENT
=
NOT CLAIMED

IMPLEMENTATION COMPLETION
=
NOT CLAIMED

TRACE RESULT
=
REQUIRED WHEN LIGHT TRACE SUCCESS / PARTIAL

CANONICAL TRACE EXECUTION RECEIPT
=
OPTIONAL IF ACTUALLY ISSUED

CORE JOB
=
REGISTER
DISCOVER
BIND
CALL
```

---

# 17｜一句話收束

> **L9 提供光軌的眼睛與筆，不提供裁判槌；光軌必須留下可引用的戰情報告結果，但不為了證明自己存在而再造一張不存在的收據。**

# Appendix A｜V0.1.1 原文完整保留

---

# Appendix A｜V0.1.1 原文完整保留

> 下方保留 predecessor，作 migration provenance。與 V1.1 衝突處，以 V1.1 operative layer 為準。

<!-- BEGIN VERBATIM L9 V0.1.1 -->

# LIHUOOS V1｜L9 DAIL CALLABLE CAPABILITY REPOSITORY V0.1.1-WORKING
## 理火可調用能力倉｜DAIL-Defined Modules × Tool Registry × Runtime Binding
### 2026-10-25

```yaml
DOCUMENT:
  id: LIHUOOS_L9_DAIL_CALLABLE_CAPABILITY_REPOSITORY
  version: V0.1.1-WORKING
  date: 2026-10-25

  status:
    - WORKING
    - CAPABILITY_REPOSITORY_LAYER
    - NOT_RATIFIED
    - NOT_HOST_DEPLOYED

  purpose:
    - MOVE_CALLABLE_FUNCTIONAL_MODULES_OUT_OF_MONOLITHIC_LIGHTER
    - REGISTER_THEM_AS_DAIL_DEFINED_CAPABILITIES
    - LET_L8_OR_APPLICABLE_OWNERS_CALL_THEM_WHEN_NEEDED
    - KEEP_GOVERNANCE_AUTHORITY_OUTSIDE_THE_TOOL_WAREHOUSE

  lineage:
    source:
      - LIHUO_LIGHTER_V5_1_0_FUNCTIONAL_MODULE_LINEAGE
      - DAIL
    consumer:
      - L8_LIHUO_OPERATING_CYCLE
      - APPLICABLE_L0_L7_OWNERS
      - AUTHORIZED_VERTICALS
```

---

# 0｜一句話定位

> **L9 是理火的 DAIL 可調用能力倉：把原本集中在 Lighter 內的功能模組拆成可註冊、可尋址、可調用、可替換的工具與能力。**

最短式：

```text
L0–L7
=
KNOW WHAT / WHY / BOUNDARY

L8
=
RUN THE JOB

L9
=
PROVIDE CALLABLE CAPABILITIES
```

---

# 1｜最高硬鎖

```text
L9
!=
NEW THEORY OWNER

L9
!=
GOVERNANCE SOVEREIGN

L9
!=
MAIN

L9
!=
LIGHTER RENAMED

L9
!=
TOOL RESULT JUDGE

L9
!=
FINAL GATE

L9
!=
FINAL RELEASE OWNER
```

根句：

```text
TOOL EXISTS
!=
AUTHORITY TO CALL IT

TOOL CAN EXECUTE
!=
EXECUTION IS AUTHORIZED

TOOL RETURN EXISTS
!=
RETURN IS QUALIFIED FOR USE
```

---

# 2｜L9 真正做什麼

L9 只做四件事：

```text
REGISTER
DISCOVER
BIND
CALL
```

展開：

```text
REGISTER
=
知道有哪些能力

DISCOVER
=
依需求找到適合能力

BIND
=
把 DAIL 宣告綁到實際 implementation / provider / tool

CALL
=
在合法 request 下執行並回傳結果
```

L9 不決定：

```text
SHOULD THIS CAPABILITY BE USED?
IS THIS RESULT TRUE?
DOES THIS RESULT HAVE AUTHORITY?
MAY THE CYCLE PROCEED?
MAY THIS OUTPUT BE RELEASED?
```

這些屬既有治理 owner。

---

# 3｜DAIL 在 L9 的位置

沿用既有工程根句：

```text
DAIL DEFINES.
IR NORMALIZES.
CODING CONNECTS.
RUNTIME EXECUTES.
```

在 L9 中讀成：

```text
DAIL
=
CAPABILITY DECLARATION

IR
=
NORMALIZED CALL CONTRACT

CODING / BINDING
=
IMPLEMENTATION CONNECTION

RUNTIME
=
ACTUAL TOOL / MODULE EXECUTION
```

所以：

> **DAIL 不是工具本身；DAIL 是讓理火知道「這個能力是什麼、怎麼叫、會回什麼」的可移植宣告。**

---

# 4｜L9 不是把 Lighter 整包搬家

舊 Lighter 同時包含：

```text
GOVERNANCE
+
QUALIFICATION
+
ORCHESTRATION
+
TOOLS / PROVIDERS / MODULES
+
FINAL GATE / RELEASE
```

L9 只吸收：

```text
CALLABLE FUNCTIONAL CAPABILITY
```

不吸收：

```text
OWNER AUTHORITY
FINAL GOVERNANCE DECISION
FINAL RELEASE AUTHORITY
THEORY OWNERSHIP
```

所以：

```text
LIGHTER DECOMPOSITION
!=
LIGHTER REINCARNATION AS L9
```

---

# 5｜什麼東西可以進 L9

可以進 L9 的東西，必須至少是「可被明確呼叫並返回結果」的能力。

例如舊 Lighter lineage 中：

```text
PREMISE ANALYSIS / QUALIFICATION SUPPORT
AUTHORITY ANALYSIS SUPPORT
ATTENTION-EFFECT ANALYSIS SUPPORT
EXTERNAL-CONSTRAINT PARSING
R-CCC OBLIGATION COMPILATION
COMPETITION-INTEGRITY CHECK
QIP COMPILATION
OUTPUT-CONTRACT CHECK
OUTPUT-SUFFICIENCY CHECK
CAPABILITY RESOLUTION
FUNCTIONAL MODULE ROUTING
PROVIDER / TOOL / TRANSPORT ADAPTER
EXECUTION-TICKET GENERATION SUPPORT
EVIDENCE INGESTION / NORMALIZATION
EVIDENCE-ORIGIN ANALYSIS
RECOVERY UTILITY
REAUTHORIZATION SUPPORT
VERSION RESOLUTION
DOMAIN MODULES
SEARCH / RETRIEVAL
FILE / ARTIFACT OPERATIONS
EXTERNAL ACTION TOOLS
```

但「support / tool」與「authority」要分開。

例如：

```text
PREMISE_ANALYZER TOOL
MAY PRODUCE
PREMISE ANALYSIS

BUT

PREMISE QUALIFICATION STANDING
IS STILL OWNED
BY THE APPLICABLE GOVERNANCE OWNER
```

---

# 6｜哪些東西不能因為 L9 而失去 owner

例如：

```text
FINAL_GATE_CHECKER
```

可以是一個 L9 callable capability。

但：

```text
FINAL_GATE_TOOL OUTPUT
!=
FINAL GATE AUTHORITY
```

同理：

```text
RELEASE_EXECUTOR
```

可以是工具。

但：

```text
RELEASE TOOL
!=
RELEASE AUTHORITY
```

以及：

```text
AUTHORITY_ANALYZER
!=
AUTHORITY OWNER
```

---

# 7｜最小 DAIL Capability Card

L9 不需要巨大 schema。

最小卡片只要能回答：

> 這是什麼、吃什麼、回什麼、怎麼叫、誰實作。

```yaml
DAIL_CAPABILITY_CARD:
  capability_id: REQUIRED
  version: REQUIRED

  purpose: REQUIRED

  input_contract_ref: REQUIRED
  output_contract_ref: REQUIRED

  callable_by_ref: REQUIRED

  implementation_binding_ref: REQUIRED

  capability_status:
    - AVAILABLE
    - UNAVAILABLE
    - DEGRADED
    - DEPRECATED

  dependency_refs: []

  result_receipt_class_ref: OPTIONAL
```

夠了。

權限細節不在這張卡重新發明。

callable_by_ref 只指向 applicable owner / authority contract。

---

# 8｜Capability Class

為了找工具，可以有簡單分類：

```text
ANALYSIS
QUALIFICATION_SUPPORT
COMPILATION
ROUTING
RETRIEVAL
EVIDENCE
PROVIDER_ADAPTER
EXECUTION
RECOVERY
VERSIONING
ARTIFACT
DOMAIN
OTHER
```

這只是 registry taxonomy。

不是 theory ontology。

---

# 9｜L9 Registry

```yaml
L9_CAPABILITY_REGISTRY:
  registry_ref: REQUIRED

  capabilities:
    - capability_id
    - version
    - capability_class
    - status
    - dail_card_ref
    - implementation_binding_ref

  registry_version_ref: REQUIRED
```

L9 需要能：

```text
LOOKUP(capability_id)
LIST(capability_class)
RESOLVE(version / current)
CHECK_AVAILABILITY
RETURN_BINDING
```

不需要：

```text
DECIDE_WHETHER_WORLD_SHOULD_USE_IT
```

---

# 10｜Implementation Binding

同一個 capability 可以換 provider / tool / implementation。

```yaml
L9_IMPLEMENTATION_BINDING:
  binding_ref: REQUIRED

  capability_id: REQUIRED
  capability_version: REQUIRED

  implementation_type:
    - LOCAL_MODULE
    - HOST_TOOL
    - EXTERNAL_PROVIDER
    - CONNECTOR
    - SERVICE
    - HUMAN_HANDOFF
    - OTHER

  implementation_ref: REQUIRED

  runtime_status:
    - READY
    - UNAVAILABLE
    - DEGRADED

  dependency_refs: []
```

所以：

```text
CAPABILITY IDENTITY
!=
ONE PERMANENT PROVIDER
```

L9 可以換 implementation，而不改上層語義。

---

# 11｜L8 如何叫 L9

標準：

```text
L8 / APPLICABLE OWNER
IDENTIFIES NEED
↓
QUALIFIED CALL REQUEST EXISTS
↓
L9 RESOLVES CAPABILITY
↓
L9 EXECUTES BOUND IMPLEMENTATION
↓
L9 RETURNS RESULT
↓
APPLICABLE OWNER CONSUMES / QUALIFIES RESULT
↓
L8 CONTINUES CYCLE
```

L9 不自己創造：

```text
QUALIFIED CALL REQUEST
```

如果沒有合法 call：

```text
NO CALL
```

---

# 12｜最小 Call Request

L9 只需要足夠執行。

```yaml
L9_CAPABILITY_CALL:
  call_ref: REQUIRED

  capability_id: REQUIRED
  capability_version: CURRENT_OR_EXPLICIT

  caller_ref: REQUIRED
  call_authority_ref: REQUIRED

  input_ref: REQUIRED
  input_contract_ref: REQUIRED

  cycle_ref: OPTIONAL
  main_invocation_ref: OPTIONAL

  requested_at_ref: REQUIRED
```

cycle_ref / main_invocation_ref 只有真的需要綁定時才帶。

不要所有工具都硬綁整套 OS identity。

---

# 13｜最小 Tool Return

```yaml
L9_CAPABILITY_RETURN:
  call_ref: REQUIRED
  capability_id: REQUIRED
  capability_version: REQUIRED

  implementation_ref: REQUIRED

  result_ref: REQUIRED_OR_NONE

  call_execution_status:
    - SUCCESS
    - PARTIAL
    - FAILED
    - UNAVAILABLE
    - CANCELLED

  error_or_gap_ref: OPTIONAL

  receipt_ref: OPTIONAL
```

這個 return 只回答：

> **這次 tool call 的 implementation execution 結果是什麼？**

硬鎖：

```text
TOOL CALL SUCCESS
!=
SEMANTIC RESULT ACCEPTED

CALL EXECUTION STATUS
!=
TASK OUTCOME
```

所以它不自動回答：

> **上層應不應該相信、採用、發布，或整體任務是否成功。**

---

# 14｜Receipt 原則

L9 若 underlying provider / tool 有 canonical receipt：

```text
PRESERVE IT
RETURN IT
```

如果沒有：

```text
DO NOT INVENT PROVIDER RECEIPT
```

L9 可以回：

```text
NO_CANONICAL_RECEIPT
```

讓 L8 最後 checklist 如實列出。

L9 不需要再建「receipt 的 receipt」。

---

# 15｜Capability Discovery

上層不知道 capability id 時，可以依：

```text
purpose
task type
input type
required output
domain
availability
```

查找。

但 discovery 結果只是：

```text
CANDIDATE CAPABILITIES
```

不是：

```text
AUTHORIZED CAPABILITY SELECTION
```

適用 owner 仍決定是否使用。

---

# 16｜版本管理

L9 應允許：

```text
MULTIPLE VERSIONS
CURRENT POINTER
DEPRECATED VERSION
PINNED VERSION
ROLLBACK TARGET
```

最小規則：

```text
CALL MAY PIN VERSION
OR
USE CURRENT RESOLVED VERSION
```

但：

```text
VERSION CURRENT
!=
SEMANTICALLY APPROVED FOR EVERY DOMAIN
```

---

# 17｜失敗與降級

如果 capability unavailable：

```text
L9 RETURNS
UNAVAILABLE
```

不要假裝成功。

上層再決定：

```text
RETRY
FALLBACK
HOLD
SKIP IF OPTIONAL
ABORT
```

L9 不擅自改任務。

---

# 18｜原 Lighter 功能的遷移原則

遷移時不要問：

> 這個功能以前在 Lighter，所以是不是整個搬過來？

要問：

> **這是不是一個可以獨立被叫用、輸入清楚、輸出清楚的 capability？**

如果是：

```text
MOVE / REIMPLEMENT INTO L9
AS DAIL-CALLABLE CAPABILITY
```

如果不是，而是：

```text
OWNER AUTHORITY
GOVERNANCE RULE
QUALIFICATION STANDING
FINAL RELEASE RIGHT
```

就留在：

```text
L0–L7 / APPLICABLE GOVERNANCE CONTRACT
```

---

# 19｜第一批 L9 Capability Families

這只是 migration map，不宣稱已部署。

```yaml
L9_INITIAL_CAPABILITY_FAMILIES:

  INPUT_AND_ANALYSIS:
    - RAW_INPUT_PARSER
    - PREMISE_ANALYZER
    - AUTHORITY_ANALYZER
    - EXTERNAL_CONSTRAINT_PARSER

  COMPILATION:
    - RCCC_OBLIGATION_COMPILER
    - QIP_COMPILER
    - OUTPUT_CONTRACT_COMPILER

  AUDIT_SUPPORT:
    - COMPETITION_INTEGRITY_CHECKER
    - OUTPUT_SUFFICIENCY_CHECKER
    - EVIDENCE_ORIGIN_ANALYZER

  EVIDENCE_AND_RETRIEVAL:
    - EVIDENCE_INGESTOR
    - RETRIEVAL_MODULE
    - SEARCH_MODULE
    - CURRENT_SOURCE_LOOKUP

  ROUTING_AND_PROVIDER:
    - CAPABILITY_RESOLVER
    - MODULE_ROUTER
    - PROVIDER_ADAPTER
    - TRANSPORT_ADAPTER

  EXECUTION:
    - EXTERNAL_ACTION_TOOL
    - ARTIFACT_OPERATION_TOOL
    - EXECUTION_TICKET_BUILDER

  RECOVERY_AND_VERSIONING:
    - RECOVERY_UTILITY
    - REAUTHORIZATION_SUPPORT
    - VERSION_RESOLVER

  DOMAIN:
    - DOMAIN_SPECIFIC_MODULES
```

每一個 family 之後可以有多個 DAIL capability card。

---

# 20｜Final Gate / Release 怎麼處理

這兩個最容易重新長出 Lighter。

正確拆法：

```text
FINAL_GATE SEMANTICS / AUTHORITY
=
GOVERNANCE OWNER

FINAL_GATE CHECKING CAPABILITY
=
MAY LIVE IN L9
```

以及：

```text
RELEASE AUTHORITY
=
APPLICABLE RELEASE OWNER

RELEASE EXECUTION CAPABILITY
=
MAY LIVE IN L9
```

所以：

> **L9 可以提供手；不能自己變成腦或法官。**

---

# 21｜L9 與 Main

Main 可以需要工具。

但：

```text
MAIN
DOES NOT OWN L9

L9
DOES NOT OWN MAIN
```

若 Main contract 允許 tool call：

```text
MAIN / GOVERNANCE
→ QUALIFIED CALL
→ L9
→ RETURN
→ MAIN CONTINUES
```

L9 不介入 Main 的 generative dynamics。

---

# 22｜L9 與 L8

L8 是業務流程。

L9 是能力供應。

```text
L8
=
WHAT STEP ARE WE DOING?

L9
=
WHAT CAPABILITY CAN DO THIS STEP?
```

所以：

```text
L8 MAY CALL MANY L9 MODULES

L9 MAY SERVE MANY L8 CYCLES
```

兩者不要互相吞。

---

# 23｜Overengineering Control

L9 只保留真正需要的資料：

```text
WHAT
INPUT
OUTPUT
HOW TO CALL
WHAT IMPLEMENTS IT
CURRENT AVAILABILITY
```

如果某欄位不能改善：

```text
DISCOVERY
CALLING
BINDING
RETURN
```

就不要塞進 L9 core。

尤其禁止：

```text
EVERY TOOL
MUST REDECLARE
ALL L0–L8 TYPES
```

只引用 canonical contract。

---

# 24｜最小 Runtime Algorithm

```text
RECEIVE QUALIFIED CALL REQUEST

1. RESOLVE capability_id / version
2. CHECK availability
3. RESOLVE implementation binding
4. PASS canonical input
5. EXECUTE
6. RETURN canonical result / error
7. PRESERVE provider/tool receipt if any
8. STOP
```

L9 到這裡就結束。

---

# 25｜L9 最短法位

```text
L9
DOES NOT DECIDE
WHAT LIHUO SHOULD BELIEVE.

L9
DOES NOT DECIDE
WHAT LIHUO MAY AUTHORIZE.

L9
DOES NOT DECIDE
WHAT LIHUO MAY RELEASE.

L9
PROVIDES
CALLABLE CAPABILITY.

DAIL DEFINES IT.
BINDING CONNECTS IT.
RUNTIME EXECUTES IT.
THE OWNER ABOVE
DECIDES WHAT THE RESULT MEANS.
```

---

# 26｜Working Standing

```text
L9 DAIL CALLABLE CAPABILITY REPOSITORY V0.1.1-WORKING

IDENTITY
=
CAPABILITY REPOSITORY LAYER

SOURCE LINEAGE
=
LIGHTER FUNCTIONAL MODULES
+
DAIL

NEW THEORY
=
NONE

NEW GOVERNANCE OWNER
=
NONE

CORE JOB
=
REGISTER / DISCOVER / BIND / CALL

AUTHORITY
=
EXTERNAL TO L9

RESULT QUALIFICATION
=
EXTERNAL TO L9

L8 RELATION
=
PROVIDE CALLABLE CAPABILITIES FOR OPERATING CYCLE

MAIN RELATION
=
PROVIDE TOOLS WHEN LAWFULLY CALLED

OVERENGINEERING CONTROL
=
PASS IN CURRENT DESIGN

RUNTIME RATIFICATION
=
HOLD
```

---

# 27｜一句話收束

> **L9 不是新的 Lighter；L9 是把能力從巨型控制平面拆出來，變成 DAIL 定義、可尋址、可替換、可調用的工具倉。**


<!-- END VERBATIM L9 V0.1.1 -->


> **V1.2.3 current：Light Trace 已內生於 L9，binding_state = CHAT_NATIVE_AVAILABLE；不再需要旁掛 source/patch 檔。**
