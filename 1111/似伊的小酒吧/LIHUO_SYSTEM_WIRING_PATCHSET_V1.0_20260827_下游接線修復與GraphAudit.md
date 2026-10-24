# LIHUO 系統接線修復清單 V1.0
## Protocol V2.3 × Lighter V3.5 × Main System V3.5｜下游 Runtime Wiring Patch Set

```yaml
AUDIT:
  id: "LIHUO-SYSTEM-WIRING-PATCHSET-20260827-V1"
  date: "2026-08-27"
  scope: "DOCUMENT_LEVEL_INTEGRATION_GRAPH_REPAIR"
  root_protocol: "LIHUO PROTOCOL V2.3"
  lighter: "LIHUO LIGHTER V3.5-EXP"
  main_system: "LIHUO AI SYSTEM V3.5-EXP"
  runtime_deployment_claim: false
  host_enforcement_claim: false

EXCLUDED_BY_CURRENT_WORK_BREAK:
  - "LIHUO Writing Runtime V2.5-EXP（已另線處理，本輪不再修改）"

NOT_PROMOTED_TO_RUNTIME:
  - "FOOTBINDING PATCH V0.1-EXP（維持 PATCH / donor 法位）"
```

# 1｜現行總拓撲

```text
HOST / PLATFORM BOUNDARY
↓
LIHUO PROTOCOL V2.3
↓
LIHUO LIGHTER V3.5-EXP
│
├─ SAC-independent governance / DAIL / routing / vertical runtimes
│
├─ 1111 / 正太喵吧 / 0303
├─ AINT V2.1-RC4
└─ other vertical runtimes
     │
     ├─ scoped providers: CERI / character pools / other providers
     │
     └─ if SAC-dependent capability required
           ↓
        BINDING MANIFEST
           ↓
        LIHUO AI SYSTEM V3.5-EXP
           ↓
        PROVIDER RETURN
           ↓
        LIHUO LIGHTER V3.5-EXP
           ↓
        RETURN TO CALLER
```

根規則：

```text
CAPABILITY_PRESENT != CAPABILITY_WIRED
REQUESTED != BOUND != EXECUTED != HOST_ENFORCED
CALLABLE != OWNED
DATA_FLOW_ORDER != LEGAL_AUTHORITY_ORDER
SAC-INDEPENDENT != NON-GENERATIVE
```

# 2｜本輪實際修改

| 檔案 | 原問題 | 修復 | 新狀態 |
|---|---|---|---|
| 1111 V0.5 | `ACTIVE/liveness` 容易混淆文件治理與 Host Runtime；Main provider 未明示 | 升 V0.5.1；拆 session declaration / evidence；Main V3.5 optional binding | PASS |
| 正太喵吧 V0.5 | 明確綁 V2.2 / Lighter V3.0 | 升 V0.5.1；綁 V2.3 / V3.5；Main V3.5 unbound-by-default | PASS |
| 0303 V0.5 | 明確綁 V2.2 / Lighter V3.0 | 升 V0.5.1；綁 V2.3 / V3.5；Main V3.5 unbound-by-default | PASS |
| AINT V2.1-RC3 | optional design refs 停 V3.4；V3.5 wiring position 未明示 | 升 RC4；標為 SAC-independent portable vertical Runtime；禁止直接綁 Main | PASS |
| CERI V0.3 | metadata target 停 AINT V2.0-RC1 | 升 V0.3.1；改成 AINT V2 family-compatible Register Provider | PASS |

# 3｜產出檔案與 lineage

```yaml
PATCHED_FILES:
  - file: "《1111酒吧》世界觀與運行設定_V0.5.1_LIHUO-V3.5接線_證據語義現代化版.md"
    sha256: "7d6c90fe56e71c320c0faacb0a77bbd8fb7db7d8d605f3fa435d86fea49058db"
    parent_sha256: "a5113cfae2cfd7afa3573147df7565172e9c61bb7555db6594d976e1d2c782b4"

  - file: "《正太喵吧》世界觀與運行設定_V0.5.1_ProtocolV2.3_LighterV3.5接線同步版.md"
    sha256: "44cd92f3d6eddbaf7f534d8fd7db26d1053c2f9599d3ab444ae240991d583604"
    parent_sha256: "b99a0ebf6adecfe99e1174e5d485f56d4b8429f057b11b2c55619b195f29c3a9"

  - file: "《0303》世界觀與運行設定_V0.5.1_ProtocolV2.3_LighterV3.5接線同步版.md"
    sha256: "d75f433463321b28166e72f410400a0e0d91bdd04d266350cd29bca206771f31"
    parent_sha256: "ed1187b02b867ef53b60abd05dc496d1e0898265afbf4ab39f9963f475d43fc9"

  - file: "成人親密敘事模組_AINT_V2.1-RC4-FULL_V3.5接線法位_PortableCore保留版.md"
    sha256: "251109308a6dbdc543d57ec7547d05b128864b6347d731a12c6fa360afe3c8a9"
    parent_sha256: "8a05e48dc6fd3807e8d3a4402e74535b87cf2603d42a450f0d4cd457b68864b1"

  - file: "成人古典中文語域與語料提供者_CERI_V0.3.1-EXP_AINT2Family接線_Provider法位版.md"
    sha256: "373f7aded514bb3444e58fa651e95b38146fddeddd5c3bfaebdbf61aa34c060d"
    parent_sha256: "3f704605037eefa4ab83573533fe85e57fd41bcff5624c238be033ce7d2c3ae2"
```

# 4｜未修改核心三件套的理由

Protocol V2.3 已經建立能力／限制的對稱證據紀律；Lighter V3.5 已正式建立 SAC dependency placement、DAIL 2.0、wiring constitution；Main System V3.5 也已對標為 SAC-dependent provider。這一輪看到的是**下游 version debt / route debt**，沒有證據要求回頭改根協議、賴打或主系統。

# 5｜文件級 Graph Audit

```yaml
GRAPH_AUDIT:
  root_protocol_consistency: "PASS"
  lighter_generation_consistency: "PASS"
  main_provider_generation_consistency: "PASS"
  venue_stale_version_labels_active_semantics: "REPAIRED"
  direct_main_system_jump: "BLOCKED_BY_PATCH"
  provider_return_path: "PRESENT"
  sac_dependency_placement: "EXPLICIT"
  provider_scope_isolation: "EXPLICIT"
  document_vs_runtime_evidence_separation: "EXPLICIT"

EVIDENCE_LEVEL:
  source_files_read: true
  patched_documents_created: true
  integration_graph_audited: true
  model_behavioral_runtime_tested: false
  host_runtime_tested: false
  host_enforced: false
```

# 6｜下一輪只剩的清潔項

目前沒有阻斷性接線債。剩下的是低優先清潔：

1. 若三夜場未來再共同升 V0.6，可把三份重複的 LIHUO binding schema 抽成共同 `NIGHT_VENUE_LIHUO_BINDING_PROFILE`，避免日後再次 version skew。
2. AINT RC4 / CERI V0.3.1 之後可做一輪 contract regression，確認 provider call / return 不會搶 Host 法位。
3. FOOTBINDING PATCH 保持 donor，不因本輪 wiring cleanup 被錯升為 Runtime。
4. Writing Runtime V2.5 保持目前版本，待恢復該支線後再做長場景 regression。
