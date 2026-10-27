# LIHUOOS｜CURRENT SYSTEM

```yaml
CURRENT_SYSTEM:
  name: LIHUOOS
  version: V1.2.1

  standing:
    - RATIFIED_CURRENT
    - ACTIVE_SYSTEM_BASELINE
    - DOCUMENT_LEVEL_CURRENT

  activation_date: 2026-10-27

  activation_record:
    file: "V1版本/LIHUOOS_V1.2.1_ACTIVATION_RATIFICATION_20261027.md"
    blob_sha: "2386916b8a2b3810771f24a31299ff91dfacd4ca"

  current_system_edition:
    file: "V1版本/正式版/理火OSV1.2.1版.md"
    blob_sha: "138be59d40f22b78a667ef0881da00dc99150f71"

  current_map:
    file: "V1版本/L0_INDEX_SOURCE_VERSION_V1.2.1.md"
    blob_sha: "0ffa6ad9969ce88787ce2ab9b866e8f2710a48aa"

  current_l8:
    file: "V1版本/L8_LIHUO_OPERATING_CYCLE_V1.2.1_20261027.md"
    blob_sha: "4abff3e1c3d554ca32d2a5d4a1ba5f483ba845eb"

  current_l9:
    file: "V1版本/L9_DAIL_CALLABLE_CAPABILITY_REPOSITORY_V1.2_20261027.md"
    blob_sha: "b42f3bef94b7b2ffd8817bc95a77b9b2cfa3942b"

  predecessor:
    version: V1.2
    current_edition: "V1版本/正式版/理火OSV1.2版.md"
    activation_record: "V1版本/LIHUOOS_V1.2_ACTIVATION_RATIFICATION_20261027.md"

  v1_2_1_scope:
    - DEFAULT_NON_HOST_UNLESS_HUMAN_EXPLICITLY_DECLARES_HOST_OPERATION
    - NO_HOST_DEPLOYMENT_NOT_AUTOMATIC_CYCLE_BLOCKER
    - HOST_DECLARATION_SEPARATED_FROM_HOST_DEPLOYMENT_EVIDENCE
    - L8_HOST_MODE_ENTRY_ROUTING_HARDENED
    - CURRENT_ROUTING_UPDATE

  preserved_from_v1_2:
    - L1
    - L2
    - L3
    - L4
    - L5
    - L6
    - L7
    - L9_V1_2_CAPABILITY_BASELINE
    - MAIN_CORE_COMPUTE_SEMANTICS
    - V1_2_INTER_ROUND_LIGHT_TRACE
    - V1_2_MANIFESTATION_FIDELITY
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

L8 V1.2.1
=
OPERATION
+
LIGHT TRACE TIMING / HANDOFF

L9 V1.2 (preserved)
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
R1 → T1 → R2(T1) → T2
→ [R3+(LATEST_TRACE) → T3+]
→ MANIFESTATION CANDIDATE
→ TM FIDELITY TRACE
→ RELEASE QUALIFICATION
```

> **V1.2.1 is the current system. V1.2 remains predecessor / rollback history.**
>
> **Default routing is NON-HOST unless the human explicitly declares HOST operation. NON-HOST does not disqualify a LIHUO cycle.**
>
> **Light Trace reports the battle; it does not command the battle.**
>
> **This pointer does not claim Host deployment, hidden CoT access, raw activation access, or implementation completion.**
