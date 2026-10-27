# LIHUOOS V1.2.1｜ACTIVATION / RATIFICATION RECORD
## Host Default NON-HOST Hardening
### 2026-10-27

```yaml
ACTIVATION:
  system: LIHUOOS
  version: V1.2.1

  standing:
    - RATIFIED_CURRENT
    - ACTIVE_SYSTEM_BASELINE
    - DOCUMENT_LEVEL_CURRENT
    - HOST_DEFAULT_NON_HOST_HARDENING

  human_approval:
    instruction: "OK 動手"
    date: 2026-10-27

  predecessor:
    system: LIHUOOS V1.2
    current_edition:
      file: "正式版/理火OSV1.2版.md"
      blob_sha: "946e0601c241887ef82b166a5097c6ad52936313"
    activation_record:
      file: "LIHUOOS_V1.2_ACTIVATION_RATIFICATION_20261027.md"
      blob_sha: "940ca10532944dbd5cfe70b9db98c2152b162b04"

  current:
    current_edition:
      file: "正式版/理火OSV1.2.1版.md"
      blob_sha: "138be59d40f22b78a667ef0881da00dc99150f71"

    current_l0:
      file: "L0_INDEX_SOURCE_VERSION_V1.2.1.md"
      blob_sha: "0ffa6ad9969ce88787ce2ab9b866e8f2710a48aa"

    current_l8:
      file: "L8_LIHUO_OPERATING_CYCLE_V1.2.1_20261027.md"
      blob_sha: "4abff3e1c3d554ca32d2a5d4a1ba5f483ba845eb"

    current_l9:
      file: "L9_DAIL_CALLABLE_CAPABILITY_REPOSITORY_V1.2_20261027.md"
      blob_sha: "b42f3bef94b7b2ffd8817bc95a77b9b2cfa3942b"

  change_scope:
    - DEFAULT_NON_HOST_UNLESS_HUMAN_EXPLICITLY_DECLARES_HOST_OPERATION
    - NO_HOST_DEPLOYMENT_NOT_AUTOMATIC_CYCLE_BLOCKER
    - HOST_DECLARATION_SEPARATED_FROM_HOST_DEPLOYMENT_EVIDENCE
    - L8_HOST_MODE_ENTRY_ROUTING_HARDENED
    - CURRENT_ROUTING_UPDATE

  preserved:
    - L1_THROUGH_L7
    - MAIN_CORE_COMPUTE_SEMANTICS
    - L9_V1_2_CAPABILITY_BASELINE
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

# 1｜Ratified Host Default

```text
UNLESS HUMAN EXPLICITLY DECLARES
THE CURRENT TASK / SESSION
IS OPERATING ON A HOST,

DEFAULT
=
NON_HOST_MODE
```

因此：

```text
NO HUMAN HOST DECLARATION
→
NON_HOST_MODE

NON_HOST_MODE
!=
NO LIHUO CYCLE

NO HOST DEPLOYMENT
!=
NO LIHUO OPERATION
```

這項 ratification 的目的不是否定 Host。

它禁止的是：

> **在沒有人類明示 Host routing、且當前任務並不依賴 Host-bound capability 的情況下，模型自行把「沒有獨立 Host 部署」升格成週期不能開始的理由。**

---

# 2｜Human Declaration != Deployment Proof

人類明示本次在 Host 上運行時：

```text
HUMAN HOST DECLARATION
→
HOST_ROUTED_MODE
```

但：

```text
HUMAN HOST DECLARATION
!=
HOST DEPLOYMENT PROOF

HOST_ROUTED_MODE
!=
HOST EXECUTION RECEIPT
```

任何 `HOST_DEPLOYED`、`HOST_ENFORCED`、`HOST_EXECUTED` 主張，仍須有相稱證據。

---

# 3｜版本法位

V1.2.1 是 V1.2 的 hardening patch，不重新制憲，不新增 layer，不新增 owner，也不改寫 Main / L9 核心。

最短式：

> **Host 是特定能力與執行條件，不是理火存在的普遍前提。**

以及：

> **除非人類明示本次在 Host 上運行，LIHUOOS 一律預設 NON-HOST；NON-HOST 不降低理火週期的成立資格。**
