# LIHUOOS｜CURRENT SYSTEM

```yaml
CURRENT_SYSTEM:
  name: LIHUOOS
  version: V1.2

  standing:
    - RATIFIED_CURRENT
    - ACTIVE_SYSTEM_BASELINE
    - DOCUMENT_LEVEL_CURRENT

  activation_date: 2026-10-27

  activation_record:
    file: "V1版本/LIHUOOS_V1.2_ACTIVATION_RATIFICATION_20261027.md"
    blob_sha: "940ca10532944dbd5cfe70b9db98c2152b162b04"

  current_system_edition:
    file: "V1版本/正式版/理火OSV1.2版.md"
    blob_sha: "946e0601c241887ef82b166a5097c6ad52936313"

  current_map:
    file: "V1版本/L0_INDEX_SOURCE_VERSION_V1.2.md"
    blob_sha: "28b2617fbe5d44583e4ce137ae37322bc82737c1"

  current_l8:
    file: "V1版本/L8_LIHUO_OPERATING_CYCLE_V1.2_20261027.md"
    blob_sha: "e365258e912e096b2ecf250907ee35f5b7e0f26e"

  current_l9:
    file: "V1版本/L9_DAIL_CALLABLE_CAPABILITY_REPOSITORY_V1.2_20261027.md"
    blob_sha: "b42f3bef94b7b2ffd8817bc95a77b9b2cfa3942b"

  predecessor:
    version: V1.1
    current_edition: "V1版本/正式版/理火OSV1.1版.md"
    activation_record: "V1版本/LIHUOOS_V1.1_ACTIVATION_RATIFICATION_20261026.md"

  v1_2_scope:
    - R1_TO_R2_LIGHT_TRACE_HANDOFF
    - POST_R2_LIGHT_TRACE
    - POST_MATERIAL_R3_PLUS_LIGHT_TRACE
    - MANIFESTATION_FIDELITY_TRACE
    - L9_LIGHT_TRACE_RENDERER_UPGRADE
    - CURRENT_ROUTING_UPDATE

  preserved_from_v1_1:
    - L1
    - L2
    - L3
    - L4
    - L5
    - L6
    - L7
    - MAIN_CORE_COMPUTE_SEMANTICS
    - V1_1_CAPABILITY_MIGRATION
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

L8 V1.2
=
OPERATION
+
LIGHT TRACE TIMING / HANDOFF

L9 V1.2
=
CAPABILITY

MAIN
=
COMPUTE
```

Current competition observability:

```text
R1 → T1 → R2(T1) → T2
→ [R3+(LATEST_TRACE) → T3+]
→ MANIFESTATION CANDIDATE
→ TM FIDELITY TRACE
→ RELEASE QUALIFICATION
```

> **V1.2 is the current system. V1.1 remains predecessor / rollback history.**
>
> **Light Trace reports the battle; it does not command the battle.**
>
> **This pointer does not claim Host deployment, hidden CoT access, raw activation access, or implementation completion.**
