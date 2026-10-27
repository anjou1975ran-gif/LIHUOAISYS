# LIHUOOS｜CURRENT SYSTEM

```yaml
CURRENT_SYSTEM:
  name: LIHUOOS
  version: V1.2.2

  standing:
    - RATIFIED_CURRENT
    - ACTIVE_SYSTEM_BASELINE
    - DOCUMENT_LEVEL_CURRENT

  activation_date: 2026-10-27

  activation_record:
    file: "V1版本/LIHUOOS_V1.2.2_ACTIVATION_RATIFICATION_20261027.md"
    blob_sha: "331e2bbf7e441c16bbc4dc9c969ed04d27f23a35"

  current_system_edition:
    file: "V1版本/正式版/理火OSV1.2.2版.md"
    blob_sha: "fdd3f0478c229ca014d411c8258d1d961601ed5d"

  current_map:
    file: "V1版本/L0_INDEX_SOURCE_VERSION_V1.2.2.md"
    blob_sha: "24596436ed187eb1a71acfb04fe24b10ede3ce3a"

  current_l8:
    file: "V1版本/L8_LIHUO_OPERATING_CYCLE_V1.2.2_20261027.md"
    blob_sha: "c3bb04de4f0f9c0c2e866310d60c5a1fca17ddd5"

  current_l9:
    file: "V1版本/L9_DAIL_CALLABLE_CAPABILITY_REPOSITORY_V1.2.2_20261027.md"
    blob_sha: "36ca93f909d2f250fec97a616365817d04e4158d"

  predecessor:
    version: V1.2.1
    current_edition: "V1版本/正式版/理火OSV1.2.1版.md"
    activation_record: "V1版本/LIHUOOS_V1.2.1_ACTIVATION_RATIFICATION_20261027.md"

  v1_2_2_scope:
    - TRACE_RESULT_REQUIRED_NEQ_TRACE_RECEIPT_REQUIRED
    - NO_EXECUTION_RECEIPT_NEQ_NO_TRACE_RESULT
    - CHAT_NATIVE_SAME_CONTEXT_TRACE_RESULT_ALLOWED
    - STATUS_WORD_ALONE_NOT_TRACE_RESULT
    - MAIN_CANONICAL_RETURN_SEPARATED_FROM_TRACE_RESULT
    - FINAL_CYCLE_ACCOUNTING_CHECKLIST_HARDENED

  preserved_from_v1_2_1:
    - L1
    - L2
    - L3
    - L4
    - L5
    - L6
    - L7
    - MAIN_CORE_COMPUTE_SEMANTICS
    - V1_2_INTER_ROUND_LIGHT_TRACE
    - V1_2_MANIFESTATION_FIDELITY
    - V1_2_1_HOST_DEFAULT_NON_HOST
    - LEGACY_LIGHTER_RETIREMENT

  scope_lock:
    hidden_cot_access: false
    raw_activation_access: false
    host_deployed: false
    implementation_complete: false
    whole_system_empirically_validated: false
```

---

```text
L0–L7
=
MEANING / THEORY / GOVERNANCE BASIS

L8 V1.2.2
=
OPERATION
+
LIGHT TRACE TIMING / HANDOFF

L9 V1.2.2
=
CAPABILITY

MAIN
=
COMPUTE
```

Current entry + competition observability:

```text
NO HUMAN HOST DECLARATION → NON_HOST_MODE
HUMAN EXPLICIT HOST DECLARATION → HOST_ROUTED_MODE
↓
R1 → T1(trace_result_ref) → R2(T1) → T2(trace_result_ref)
→ [R3+(LATEST_TRACE) → T3+]
→ MANIFESTATION CANDIDATE
→ TM FIDELITY TRACE
→ RELEASE QUALIFICATION
```

> **V1.2.2 is the current system. V1.2.1 remains predecessor / rollback history.**
>
> **Default routing is NON-HOST unless the human explicitly declares HOST operation. NON-HOST does not disqualify a LIHUO cycle.**
>
> **Light Trace requires a trace result when applicable; a separate execution receipt is optional unless one actually exists.**
>
> **Light Trace reports the battle; it does not command the battle.**
>
> **This pointer does not claim Host deployment, hidden CoT access, raw activation access, or implementation completion.**
