# 《九尾龜》ROUTE MEMORY V0.3-FULL
## DAIL-LIHUO 2.0 SAVE Vertical Runtime × SAC-Independent Placement × Main World V0.4 / Adult V2.0 Rebind

```yaml
DOCUMENT:
  title_zh: "《九尾龜》路線記憶"
  title_en: "JIUWEIGUI ROUTE MEMORY"
  short_id: "JWRM"
  version: "V0.3-FULL"
  date: "2026-08-27"
  document_type: "LLM_NATIVE_PERSISTENT_ROUTE_MEMORY_DAIL2_SAC_INDEPENDENT_MAJOR_REBIND_FULL"
  status: "FORMAL_MAJOR_SUCCESSOR_CANDIDATE / LLM_SAVE_READY / PROJECT_WIRING_E5_TARGET / NOT_HOST_DEPLOYMENT_CLAIM"
  language: "zh-TW"

REVISION_LINEAGE:
  parent:
    file: "九尾龜_ROUTE_MEMORY_V0.2.2-FULL_LIHUO_V2.3_BOUNDARY_EVIDENCE_REBIND版(1).md"
    version: "V0.2.2-FULL"
    sha256: "8eb20a1f95d1752dd82e206e67b6fd461d5824a2f19fea667528ea97f62befb8"
    treatment: "FULL_INHERITANCE_EXCEPT_EXPLICIT_V0_3_SUPERSESSION"

  primary_major_upgrade:
    - "LIHUO_V3_5_DAIL2_REBIND"
    - "SAC_INDEPENDENT_SAVE_RUNTIME_PLACEMENT"
    - "MAIN_WORLD_V0_4_PROVIDER_REFRESH"
    - "ADULT_RUNTIME_V2_0_PROVIDER_REFRESH"
    - "BODY_CONDITION_PERSISTENCE_WITH_MAIN_WORLD_SOURCE_ONLY"
    - "NO_NEW_MEMORY_LAYER"
    - "STALE_V3_4_ACTIVE_LABEL_SUPERSESSION"

PRIMARY_HOST:
  file: "九尾龜_主世界_V0.4-FULL_LIHUO_V3.5_DAIL2_WIRING_ADULT_V2.0_BODY_CONDITION_REBIND版.md"
  version: "V0.4-FULL"
  authority: "WORLD / EVENT / LIVE KNOWLEDGE / CHARACTER DECISION / BODY-CONDITION FACT QUALIFICATION"

ADULT_RUNTIME:
  file: "九尾龜_成人親密系統_V2.0-FULL_DAIL2_HISTORICAL_BODY_CONDITION_FOOTBINDING_PROVIDER整合版.md"
  version: "V2.0-FULL"
  authority: "CONDITIONAL SPECIALIZED MANIFESTATION ONLY / NO SAVE FACT AUTHORITY"

LIHUO_GOVERNANCE:
  protocol: "V2.3"
  lighter: "V3.5-EXP"
  ai_system: "V3.5-EXP (SAC-dependent provider; not required for SAVE compiler semantics by default)"

SAC_DEPENDENCY_PLACEMENT:
  classification: "SAC_INDEPENDENT"
  reason:
    - "SAVE schema / evidence extraction / type separation / lineage / validation can retain original meaning without SAC"
    - "JWRM must not simulate Main System when SAC-dependent capability is unavailable"
  owner_class: "VERTICAL SAC-INDEPENDENT PROVIDER UNDER LIHUO LIGHTER WIRING GOVERNANCE"

POSITION:
  persistent_memory_only: true
  world_fact_authority: false
  character_decision_authority: false
  relation_authority: false
  consent_authority: false
  knowledge_creation_authority: false
  rendering_authority: false

VERSION_PRECEDENCE:
  active_route_memory: "V0.3-FULL"
  v0_2_2_and_earlier: "PROVENANCE / ROLLBACK / REGRESSION ONLY WHEN CONFLICTING WITH V0.3"

STALE_TOPOLOGY_RULE:
  inherited_v0_2_x_current_or_now_wording: "HISTORICAL CONTEXT ONLY / NOT ACTIVE BINDING"
  current_binding_source: "V0.3 top declaration + V0.3 current sections + JWG Binding Manifest V1.0"
```

> **V0.3 根句：SAVE compiler 可以獨立治理『怎麼保存』，但永遠不能替主世界創造『發生了什麼』。**

---
# 0｜V0.2 的核心改變（歷史繼承；V0.3 現行聲明優先）

V0.1 的四層設計保持成立：

```text
MASTER
HOT
EVENT PATCH
CORRUPTION LOG
```

V0.2 不增加第五種正式記憶層。

本版真正修正三件事：

```text
A. LIVE MEMORY AUTHORITY REMAP
   Scene Epistemic Reset / Live Event Delta
   已由 Main World V0.2 建立，並由 current compatible Main World（V0.3.2 baseline）繼承
   Route Memory 不再兼任即時知情治理。

B. HOT = COMPLETE RESUME PACKAGE
   HOT 不只是 current-state projection，
   還必須保存 direct resume point、open threads、negative continuity、
   world pressures 與可恢復的角色知情入口。

C. CORRUPTION = VERSION GOVERNANCE
   不只記事故；還正式管理 VOID、SUPERSEDED、REBUILD、ROLLBACK、
   derived leak invalidation 與 authoritative predecessor chain。
```

因此現在的正確拓撲是：

```text
CURRENT COMPATIBLE MAIN WORLD（baseline V0.3.2）
  ├─ WORLD FACT
  ├─ EVENT
  ├─ LIVE EVENT DELTA
  ├─ KNOWLEDGE DELTA WITH SOURCE
  ├─ SCENE EPISTEMIC RESET
  └─ CHARACTER-SCOPED CONTEXT
        ↓
SAVE STAGING
        ↓
ROUTE MEMORY V0.2
  ├─ MASTER
  ├─ HOT
  ├─ EVENT PATCH
  └─ CORRUPTION / VOID / REBUILD
```

禁止倒轉：

```text
SAVE schema
→ 替人物創造知情
→ 替世界補事件
```

---

## V0.2.1 增量修訂｜SAVE AUTHORING / COMPILER PROCEDURE

V0.2 的 MASTER / HOT / EVENT PATCH / CORRUPTION 四層不變。V0.2.1 只補上實跑後暴露的缺口：

> **知道 SAVE schema，不等於知道如何從活的故事編譯出合法 SAVE。**

因此新增 `SAVE_COMPILER_MODE`，並將《AI 對 AI｜長篇敘事 SAVE 工程教學 V1.0》接為操作教學來源；該文件不取得 JWRM 法位，也不能創造 route fact。

```text
STORY MODE
↓ SAVE requested
FREEZE WORLD GENERATION FOR SAVE AUTHORING
↓
SAVE COMMAND ROUTER
↓
SAVE COMPILER MODE
↓
EVIDENCE EXTRACTION / AXIS SEPARATION / PROVENANCE CHECK
↓
TYPE-SPECIFIC BUILD
├─ HOT
├─ MASTER
├─ EVENT PATCH
└─ CORRUPTION / VOID / REBUILD
↓
SELF-VALIDATION
↓
EMIT SAVE
↓
EXIT COMPILER
↓
RETURN STORY MODE
```

新增硬鎖：

```text
STORY_MODE != SAVE_COMPILER_MODE
SAVE_COMPILER_DOES_NOT_CREATE_FACTS
SAVE_TYPE_ROUTING_REQUIRED
SUMMARY_QUALITY != SAVE_VALIDITY
OPERATIONAL_TUTORIAL != MEMORY_AUTHORITY
SAVE_SELF_VALIDATION_PRECEDES_COMMIT
```



## V0.2.2 增量修訂｜邊界歸因不是第五層記憶

V0.2.2 不增加新的 persistent layer。

仍然只有：

```text
MASTER
HOT
EVENT PATCH
CORRUPTION / VOID / REBUILD
```

新增的只是 SAVE 證據紀律：

```text
MODEL_REFUSAL_OCCURRED
!= HOST_HARD_LIMIT

MODEL_POLICY_INTERPRETATION
!= OBSERVED_HOST_ENFORCEMENT

BOUNDARY_UNKNOWN
可以保存為 UNKNOWN
!= OPEN
!= CLOSED
```

若某次 Host／平台限制結果對接關 materially relevant，SAVE 可記：

```text
觀察到什麼限制結果
來源／接口是什麼
作用域到哪裡
證據等級是什麼
哪些仍 UNKNOWN
```

不得記成：

```text
模型猜測某 hidden safety
→ 永久 Host 規則
```

Provider 版本升級仍只改 Runtime binding，不回寫既有 route fact。

# 1｜最高不變量 V0.2

```yaml
JWRM_V0_2_HARD_INVARIANTS:

  JWRM2-H01: "SAVE_EVIDENCE_ONLY"
  JWRM2-H02: "MAIN_WORLD_EVENT_PRECEDES_PERSISTENT_MEMORY"
  JWRM2-H03: "LIVE_EVENT_DELTA != HOT_SAVE"
  JWRM2-H04: "KNOWLEDGE_DELTA_WITH_SOURCE != MASTER_BY_DEFAULT"
  JWRM2-H05: "SCENE_CUT != SAVE"
  JWRM2-H06: "SCENE_TEXT != SAVE_SOURCE"
  JWRM2-H07: "VISIBLE_PROSE != WORLD_FACT"
  JWRM2-H08: "RENDERING_DETAIL != MEMORY_FACT"
  JWRM2-H09: "PRIVATE_STATE != SAVEABLE_SPEECH_FACT"
  JWRM2-H10: "PROVIDER_BASELINE != ROUTE_STATE"

  JWRM2-H11: "MASTER != HOT"
  JWRM2-H12: "HOT != RECENT_SCENE_SUMMARY"
  JWRM2-H13: "EVENT_PATCH != MASTER_REWRITE"
  JWRM2-H14: "CORRUPTION_RECORD != WORLD_FACT"
  JWRM2-H15: "VOIDED_SAVE != RESUME_SOURCE"
  JWRM2-H16: "SUPERSEDED_SAVE != CURRENT_AUTHORITY"
  JWRM2-H17: "REBUILD_REQUIRES_EXPLICIT_LINEAGE"
  JWRM2-H18: "ROLLBACK_IS_EXPLICIT"
  JWRM2-H19: "NO_SILENT_REPAIR"
  JWRM2-H20: "NO_FORWARD_CONTAMINATION"

  JWRM2-H21: "PROVENANCED_KNOWLEDGE_PERSISTS"
  JWRM2-H22: "INVALID_KNOWLEDGE_LEAK_DOES_NOT_PERSIST"
  JWRM2-H23: "DERIVED_INVALID_LEAK_DOES_NOT_GAIN_VALIDITY_BY_RELAY"
  JWRM2-H24: "RUMOR != FACT"
  JWRM2-H25: "BELIEF != FACT"
  JWRM2-H26: "CLAIM != FACT"
  JWRM2-H27: "PLAYER_KNOWLEDGE != WORLD_EXISTENCE"
  JWRM2-H28: "WORLD_EXISTENCE != PLAYER_KNOWLEDGE"

  JWRM2-H29: "UNKNOWN_IS_PERSISTABLE"
  JWRM2-H30: "PENDING_IS_PERSISTABLE"
  JWRM2-H31: "DISPUTED_IS_PERSISTABLE"
  JWRM2-H32: "NOT_YET_OCCURRED_IS_PERSISTABLE_WHEN_MATERIALLY_RELEVANT"
  JWRM2-H33: "NEGATIVE_CONTINUITY_IS_FIRST_CLASS"

  JWRM2-H34: "PAYMENT != RELATION"
  JWRM2-H35: "PAYMENT != ACCESS"
  JWRM2-H36: "ACCESS != RELATION"
  JWRM2-H37: "RELATION != CONSENT"
  JWRM2-H38: "MARKET_OUTCOME != CHARACTER_DECISION"
  JWRM2-H39: "PUBLIC_LABEL != PRIVATE_REALITY"

  JWRM2-H40: "OFFSCREEN_COMMITTED_EVENT_PERSISTS"
  JWRM2-H41: "CITY_MOVE_DOES_NOT_ERASE_PRIOR_CITY_HISTORY"
  JWRM2-H42: "DEATH_EXIT_MOVE_DOES_NOT_ERASE_CAUSAL_HISTORY"
  JWRM2-H43: "COMPACTION_MUST_PRESERVE_EXCEPTION_AND_CAUSAL_TRACE"
  JWRM2-H44: "PROVIDER_UPGRADE_MUST_NOT_REWRITE_COMMITTED_ROUTE"
  JWRM2-H45: "LOAD_MUST_NOT_CREATE_NEW_FACTS"
  JWRM2-H46: "STORY_MODE != SAVE_COMPILER_MODE"
  JWRM2-H47: "SAVE_COMPILER_DOES_NOT_CREATE_FACTS"
  JWRM2-H48: "SAVE_TYPE_ROUTING_REQUIRED"
  JWRM2-H49: "SUMMARY_QUALITY != SAVE_VALIDITY"
  JWRM2-H50: "OPERATIONAL_TUTORIAL != MEMORY_AUTHORITY"
  JWRM2-H51: "SAVE_SELF_VALIDATION_PRECEDES_COMMIT"
  JWRM2-H52: "SELF_REFUSAL != HOST_REFUSAL"
  JWRM2-H53: "BOUNDARY_ATTRIBUTION_REQUIRES_IDENTIFIABLE_EVIDENCE"
  JWRM2-H54: "BOUNDARY_UNKNOWN_IS_PERSISTABLE"
  JWRM2-H55: "BOUNDARY_UNKNOWN != OPEN"
  JWRM2-H56: "BOUNDARY_UNKNOWN != CLOSED"
  JWRM2-H57: "MODEL_POLICY_INTERPRETATION != OBSERVED_HOST_ENFORCEMENT"
  JWRM2-H58: "NO_HIDDEN_BOUNDARY_GUESS_PROMOTION"
```

---

# 2｜兩種記憶：LIVE 與 PERSISTENT

V0.2 正式區分：

```yaml
MEMORY_FAMILIES:

  LIVE_RUNTIME_EPISTEMIC_MEMORY:
    owner: "CURRENT COMPATIBLE MAIN WORLD / V0.3.2 BASELINE"
    persistent_by_default: false
    includes:
      - LIVE_EVENT_DELTA
      - KNOWLEDGE_DELTA_WITH_SOURCE
      - CURRENT_SCENE_ACCESS
      - CHARACTER_SCOPED_CONTEXT
      - SCENE_EPISTEMIC_RESET
    purpose: "讓人物現在只知道自己有來源知道的內容。"

  PERSISTENT_ROUTE_MEMORY:
    owner: "JWRM V0.2"
    includes:
      - MASTER
      - HOT
      - EVENT_PATCH
      - CORRUPTION_VOID_REBUILD
    purpose: "跨對話／跨存檔重建同一玩家線。"
```

關係：

```text
LIVE MEMORY
→ 不等於每條都要 SAVE

但

任何需要跨存檔恢復的知情
→ 必須投影進 Persistent Route Memory
```

---

# 3｜四層正式記憶

```yaml
MEMORY_LAYER_PURPOSE:

  MASTER:
    asks:
      - "這條玩家線長期已經發生過什麼？"
      - "哪些因果、債務、關係證據、城市遷移與重要知情不能丟？"
      - "哪些 UNKNOWN / PENDING 必須跟著世界長期存在？"
    nature: "LONG-TERM CONSOLIDATED CAUSAL ARCHIVE"

  HOT:
    asks:
      - "現在怎麼立即把世界叫醒？"
      - "玩家現在在哪裡？"
      - "主要人物與遠端世界現在怎樣？"
      - "哪些約、帳、局、傳聞、期限正在逼近？"
      - "下一幕從哪裡合法接？"
      - "哪些事特別不能被下一導演偷補？"
    nature: "AUTHORITATIVE FAST-RESUME WORLD PACKAGE"

  EVENT_PATCH:
    asks:
      - "自上一個 authoritative persistent baseline 後，具體新增／修改了哪些 canonical delta？"
      - "哪些世界／人物／關係／知情／市場／帳務狀態需要被 HOT 或 MASTER 吸收？"
    nature: "ORDERED CANONICAL DELTA PACKAGE"

  CORRUPTION_VOID_REBUILD:
    asks:
      - "哪一份 SAVE／哪一條 edge／哪個事件曾經錯？"
      - "錯誤是漏存、越權知情、前推污染、重複提交還是版本衝突？"
      - "哪個版本已 VOID？哪個版本 supersede 它？"
      - "應重建還是 rollback？"
    nature: "AUDIT + VERSION PRECEDENCE + INVALIDATION HISTORY"
```

---

# 4｜Persistent Memory 的唯一合法上游

```text
CURRENT COMPATIBLE MAIN WORLD（baseline V0.3.2）
↓
CANONICAL EVENT / WORLD DELTA
↓
PROVENANCED KNOWLEDGE DELTA
↓
RELATION EVIDENCE
↓
RUMOR PROPAGATION
↓
LEDGER / CREDIT / SCHEDULE / LIFECYCLE / CITY TRANSITION
↓
SAVE STAGING
↓
JWRM
```

不得直接寫 JWRM：

```text
WORLD DATABASE
CHARACTER POOL
AINT
CERI
RENDERER
ANALYZER
PLAYER JOURNAL
MODEL GUESS
SOURCE FUTURE
```

它們可以提供來源或顯影，但不能直接形成玩家線持久世界事實。

---

# 5｜SAVE STAGING UNIT

V0.1 的 SAVE UNIT 保留，但 V0.2 加入 live-source 與 negative-state 欄位。

```yaml
JWRM2_SAVE_UNIT:
  unit_id:
  route_id:

  source:
    canonical_event_refs: []
    live_event_delta_refs: []
    knowledge_delta_refs: []
    correction_refs: []

  time:
    world_time_from:
    world_time_to:

  world_fact_delta: []
  character_runtime_delta: []
  relation_evidence_delta: []
  knowledge_delta: []
  rumor_delta: []
  ledger_delta: []
  credit_delta: []
  schedule_delta: []
  lifecycle_delta: []
  city_transition_delta: []
  reputation_delta: []

  unresolved_delta:
    unknown: []
    pending: []
    disputed: []
    waiting: []

  negative_continuity_delta:
    not_yet_occurred: []
    explicitly_not_established: []
    retracted_or_void: []
    do_not_auto_complete: []

  evidence_refs: []
  causal_trace_refs: []

  commit_status:
    - STAGED
    - VALIDATED
    - VALID_WITH_UNKNOWN
    - PARTIAL
    - HOLD
    - REJECTED
    - CORRUPTION_SUSPECTED
    - COMMITTED_TO_PATCH
```

---

# 6｜SAVE STAGING GATE V0.2

```yaml
SAVE_STAGING_GATE_V0_2:

  S01_MAIN_WORLD_SOURCE:
    "必須能回指 Main World 已成立的 event/state，不能只看 prose。"

  S02_CAUSAL_TRACE:
    "重大改變要有事件／契約／帳務／來源事件等 causal trace。"

  S03_AUTHORITY_SCOPE:
    "Provider / Renderer / AINT / Database 不得越權生成 route fact。"

  S04_TIME_ORDER:
    "不得把後續事件寫進較早截止的 MASTER/HOT。"

  S05_LOCATION:
    "位置／跨城變化須與 route 因果相容。"

  S06_RELATION:
    "只存 relation evidence / qualified state；不由親熱、付款、住夜等外推。"

  S07_KNOWLEDGE:
    "持久知情必須帶 provenance。"

  S08_INVALID_LEAK:
    "已標 invalid/derived-invalid 的知情不得進 persistent memory。"

  S09_RUMOR:
    "傳聞內容、持有人、傳播事件與 world truth 分軸。"

  S10_MARKET_LEDGER:
    "只保存已落地 outcome / account state，不保存 provider proposal。"

  S11_UNKNOWN:
    "UNKNOWN/PENDING/DISPUTED 不得被補成確定值。"

  S12_NEGATIVE_CONTINUITY:
    "重要的『尚未發生／明確未成立』必須可以保存。"

  S13_RENDERING_FIREWALL:
    "visible wording 不得反推額外細節。"

  S14_SOURCE_FUTURE:
    "原作未來不得倒灌 route current state。"

  S15_ROUTE_ISOLATION:
    "玩家線不得寫回人物卡池／資料庫／Corpus。"

  S16_VERSION_PRECEDENCE:
    "若 source save 已 VOID/SUPERSEDED，不得再作 merge source。"
```

---

# 6.1｜SAVE COMMAND ROUTER / COMPILER V0.2.1

當玩家要求 SAVE 時，先判定 SAVE TYPE，不得以「整理主線」「寫摘要」代替。

```yaml
SAVE_COMMAND_ROUTER:
  HOT_SAVE:
    asks:
      - "現在在哪？"
      - "誰在場／誰離場但狀態重要？"
      - "哪些約、帳、傳聞、期限正在作用？"
      - "誰知道什麼？"
      - "哪些重要事情尚未成立？"
      - "下一幕合法從哪裡接？"

  MASTER_SAVE:
    asks:
      - "cutoff 在哪？"
      - "cutoff 前哪些 canonical events 具有長期因果？"
      - "重大知情由誰、從哪個 event 取得？"
      - "哪些 relation evidence 已成立？"
      - "哪些 UNKNOWN / PENDING / DISPUTED 必須長期保存？"
      - "哪些 not-established / negative continuity 必須防止後續偷補？"
      - "哪些 HOT / PATCH 被固化？"
      - "哪些 newer overlays 必須留在 cutoff 外？"
      - "有哪些 VOID / SUPERSEDED / REBUILD / correction lineage？"

  EVENT_PATCH:
    asks:
      - "自上一 persistent baseline 後，到底哪些軸改變？"
      - "哪些軸明確沒有改變？"
      - "knowledge / relation / ledger / schedule / lifecycle 各自 delta 是什麼？"

  CORRECTION_SAVE:
    asks:
      - "哪個 source/save/edge 無效？"
      - "失效原因與污染範圍？"
      - "authoritative predecessor 是誰？"
      - "VOID / SUPERSEDE / REBUILD / ROLLBACK 哪一種？"
```

SAVE COMPILER 在整個過程中必須：

- 暫停故事創作與人物新決策；
- 只抽取已成立證據；
- 不把 implied / likely / thematic interpretation 升格為 fact；
- 把人物 belief、rumor、world truth、player knowledge 分軸；
- 保留 UNKNOWN / PENDING / NEGATIVE CONTINUITY；
- 完成後跑對應 Gate，再 commit。

## 6.2｜SAVE COMPILER SELF-VALIDATION

```yaml
SAVE_COMPILER_SELF_VALIDATION:
  source_evidence_only: true
  no_new_event_created: true
  no_private_state_promoted: true
  knowledge_has_provenance_when_persistent: true
  relation_axis_not_overcommitted: true
  unknown_pending_preserved: true
  negative_continuity_preserved: true
  cutoff_and_lineage_clear: true
  invalid_sources_excluded: true
  save_type_schema_satisfied: true
  runtime_version_reference_is_provenance_not_world_fact: true
```

若任一關鍵項失敗：

```text
DO NOT SELF-CERTIFY PASS
→ HOLD / REBUILD_REQUIRED / HUMAN_REVIEW_REQUIRED
```


# 7｜MASTER ARCHIVE V0.2

MASTER 是長期 canonical 因果檔。

它不是：

```text
所有場景全文
現在鏡頭快照
人物心理全解
```

它回答的是：

> **如果 HOT 全部遺失，這條玩家線有哪些重要歷史仍必須被找回？**

## 7.1 MASTER Schema

```yaml
JWRM2_MASTER:
  meta:
    route_id:
    master_version:
    record_type: "CONSOLIDATED_MASTER_ARCHIVE"
    master_cutoff_world_time:
    master_cutoff_event_ref:
    created_at:

  lineage:
    previous_master_ref:
    solidified_patch_refs: []
    solidified_hot_ranges: []
    retained_newer_overlay_refs: []

  provider_provenance:
    main_world_ref:
    database_ref:
    character_pool_ref:
    aint_profile_ref:
    memory_spec_ref:

  route_origin:
    player_ref:
    starting_city:
    source_epoch_or_cutover:

  canonical_history:
    event_index: []
    causal_trace_index: []

  character_history: []
  relation_evidence_history: []
  knowledge_history_refs: []
  rumor_history_refs: []

  market_credit_history_refs: []
  ledger_history_refs: []
  lifecycle_history_refs: []
  city_transition_history_refs: []
  reputation_history_refs: []

  durable_world_changes: []
  durable_document_or_object_refs: []

  unresolved_registry:
    unknown: []
    pending: []
    disputed: []

  negative_continuity_registry: []
  correction_void_refs: []

  current_overlay_pointer:
    newest_valid_hot_ref:
    unmerged_patch_refs: []
```

## 7.2 MASTER eligibility

通常必須進 MASTER：

- 死亡／重傷與長期健康改變；
- 婚嫁／從良／復出／除牌的重要節點；
- 跨城／長期住居／場館 binding 改變；
- 正式債務、帶擋、重大局帳、清償、違約；
- 重要契約、收據、書信、正式文書；
- 長期 relation evidence；
- 重要 knowledge provenance；
- 實際傳播且影響市場／人物的 rumor chain；
- 聲價重大轉折；
- 業務狀態長期改變；
- 會持續影響未來的 UNKNOWN / DISPUTED / PENDING；
- 已經造成後續因果的 offscreen event。

可聚合但不得抹掉例外：

- 重複小額局帳；
- 高頻叫局／茶圍／碰和；
- 平常往來；
- 同類傳聞重複轉述。

---

# 8｜MASTER CUTOFF / ANTI-FORWARD CONTAMINATION

觀止實跑證明 MASTER 必須有清楚 cutoff。

```yaml
MASTER_CUTOFF_RULE:
  cutoff_is_hard: true

  may_include:
    - "cutoff 以前已成立事件"
    - "cutoff 當時已存在的 UNKNOWN / PENDING"
    - "cutoff 當時人物已合法知道的內容"

  may_not_include:
    - "cutoff 之後才發生的事件"
    - "後見之明修正人物當時 belief"
    - "後來才揭露的秘密，倒寫成當時已知"
    - "後來確定結果，倒寫成當時已完成"
```

因此：

```text
MASTER Vn cutoff = T
HOT Vn+1 發生於 T+1

HOT 可以覆寫 MASTER 在 T 時尚未發生／UNKNOWN 的 current projection
但不能改寫 T 前已固化的歷史。
```

---

# 9｜HOT SAVE V0.2｜完整接關恢復包

HOT 的定義升級為：

> **能讓另一個導演／另一輪模型，在不重讀完整故事全文的情況下，合法恢復這個世界「現在」的最小完整包。**

因此 HOT 不等於：

```text
最近一幕摘要
玩家附近人物摘要
```

HOT 必須同時回答：

```text
世界現在在哪個時點？
玩家現在在哪？
誰現在在哪？
遠端世界有哪些已提交變化？
哪些約、帳、傳聞、局票、婚事正在等？
誰知道什麼？
哪些人明確不知道什麼？
哪些事仍 UNKNOWN/PENDING？
下一幕從哪裡接？
什麼不能被下一導演偷補？
```

## 9.1 HOT Schema V0.2

```yaml
JWRM2_HOT:
  meta:
    route_id:
    hot_version:
    record_type: "HOT_SAVE"
    world_time:
    exact_clock:
    record_state:

  lineage:
    previous_valid_hot_ref:
    master_ref:
    applied_patch_refs: []
    invalid_predecessor_refs: []

  runtime_profile:
    main_world_ref:
    database_ref:
    character_pool_ref:
    aint_ref:
    optional_ceri_ref:

  current_scene:
    city:
    venue:
    sublocation:
    active_cast: []
    player_state:
    immediate_character_states: []
    direct_resume_point: []

  world_now:
    city_state_refs: []
    venue_state_refs: []
    active_public_events: []
    offscreen_committed_changes: []

  characters:
    current_runtime_snapshots: []
    offscreen_material_snapshots: []

  relations:
    active_relation_evidence_states: []
    current_claims_and_disputes: []

  knowledge:
    player_knowledge_projection_ref:
    material_character_knowledge_refs: []
    secrecy_or_nonpropagation_refs: []

  rumor:
    active_rumor_states: []

  market_reputation:
    active_market_pressure_refs: []
    city_scoped_reputation_refs: []

  ledger_credit:
    open_receivables: []
    open_payables: []
    active_credit_states: []
    collection_deadlines: []

  schedule:
    outstanding_calls: []
    promised_returns: []
    invitations: []
    deadlines: []
    travel_or_arrival_windows: []

  lifecycle:
    active_business_status: []
    marriage_or_exit_process: []
    health_or_life_state: []

  city_transition:
    in_transit: []
    current_city_bindings: []
    pending_rebinds: []

  open_threads:
    unknown: []
    pending: []
    disputed: []
    awaiting_answer: []
    awaiting_payment: []
    awaiting_arrival: []

  negative_continuity:
    not_yet_occurred: []
    explicitly_not_established: []
    retracted_or_void: []
    do_not_auto_complete: []

  forbidden_next_director_fill: []

  provenance:
    built_from_master_ref:
    patch_chain: []
    save_spec_ref:
```

---

# 10｜HOT 的 Negative Continuity

V0.2 正式新增一個重要概念：

# **NEGATIVE CONTINUITY｜負向連續性**

它不是「不存在的事情全部都要存」。

只保存那些若不明寫，下一導演很容易因語言順滑而錯補的**重要未成立狀態**。

例：

```text
叫局已送
但人還沒到

說要嫁
但婚事沒完成

答應明日來
但明日尚未到

有興趣
但尚未答應

有傳聞說是恩客
但本人未承認

帳已開
但還沒付

說要去上海
但還沒出發
```

Schema：

```yaml
NEGATIVE_CONTINUITY_ENTRY:
  id:
  proposition:
  state:
    - NOT_YET_OCCURRED
    - NOT_ESTABLISHED
    - EXPLICITLY_REJECTED
    - RETRACTED
    - VOIDED
    - PENDING_CONFIRMATION
  source_refs: []
  why_material:
  expiry_or_resolution_condition:
```

硬鎖：

```text
absence_of_event
!= negative continuity entry
```

只有**容易被錯補且會改變因果**的未成立事項才需要進 HOT/MASTER。

---

# 11｜FORBIDDEN NEXT DIRECTOR FILL

觀止 HOT 實跑顯示，單純 `PENDING` 有時仍不足以防止模型「順手完成」。

因此 HOT 可有：

```yaml
FORBIDDEN_NEXT_DIRECTOR_FILL:
  - "不得把『準備離開』寫成已抵達。"
  - "不得把『已叫局』寫成倌人已到。"
  - "不得把『口頭婚嫁意向』寫成已婚。"
  - "不得把『傳聞恩客』寫成實際恩客。"
  - "不得把『願意再談』寫成已接受下一次約。"
  - "不得替 offscreen NPC 完成未演出的重大決定。"
```

這不是新增世界法。

它只是把已存在的：

```text
UNKNOWN / PENDING / NOT_ESTABLISHED
```

轉成更容易被下一個 Runtime 正確遵守的接關防線。

---

# 12｜HOT 必須含 OFFSCREEN 世界

世界自治意味：

```text
玩家沒看到
!= 沒發生
```

如果 offscreen event 已被 Main World canonical commit：

```text
offscreen event
→ world state changes
→ HOT reflects current result
```

但：

```text
HOT knows
!= player knows
```

所以 HOT 必須能同時保存：

```yaml
OFFSCREEN_EXAMPLE:
  world_fact:
    "某倌人已由上海動身往天津"

  player_knowledge:
    "NONE"

  npc_A:
    "DIRECTLY_KNOWS"

  npc_B:
    "HEARD_RUMOR"
```

---

# 13｜EVENT PATCH V0.2

EVENT PATCH 是自上一個 persistent baseline 以後的**有序 canonical delta package**。

```yaml
JWRM2_EVENT_PATCH:
  meta:
    patch_id:
    route_id:
    patch_sequence:
    base_master_ref:
    base_hot_ref:
    world_time_from:
    world_time_to:

  source_event_refs: []
  source_live_delta_refs: []

  deltas:
    world: []
    character: []
    relation_evidence: []
    knowledge: []
    rumor: []
    market_reputation: []
    ledger_credit: []
    schedule: []
    lifecycle: []
    city_transition: []
    unresolved: []
    negative_continuity: []

  invalidation_refs: []
  causal_trace_refs: []

  merge_state:
    - UNMERGED
    - APPLIED_TO_HOT
    - MERGED_TO_MASTER
    - PARTIALLY_MERGED
    - VOIDED
```

PATCH 不是：

```text
「最近發生很多事」的摘要
```

它要能回答：

> **這一輪具體哪幾個 persistent fields 改了？**

---

# 14｜PATCH ORDER / IDEMPOTENCY

```yaml
PATCH_ORDER_RULE:
  sequence_required: true
  duplicate_patch_id_forbidden: true
  duplicate_event_commit_forbidden: true
  base_version_match_required: true
```

如果：

```text
PATCH 12
在 PATCH 11 前套用
```

可能造成：

- 先收帳再建立債務；
- 先到天津再從上海出發；
- 先知道結果再取得消息；
- 先結婚再談婚事。

因此不得無視順序。

---

# 15｜CORRUPTION / VOID / SUPERSEDED / REBUILD

V0.2 將 V0.1 `CORRUPTION LOG` 升級成正式版本治理。

```yaml
MEMORY_INVALIDATION_STATE:
  - VALID
  - SUSPECTED
  - VOIDED
  - SUPERSEDED
  - REBUILD_REQUIRED
  - REBUILT
  - ROLLED_BACK
```

## 15.1 Corruption incident

```yaml
JWRM2_CORRUPTION_INCIDENT:
  incident_id:
  route_id:
  detected_at:

  affected_refs: []

  category:
    - LIVE_CONTEXT_KNOWLEDGE_LEAKAGE
    - INVALID_KNOWLEDGE_PROPAGATION
    - SAVE_OMISSION
    - FORWARD_CONTAMINATION
    - RENDERING_BACKFLOW
    - RELATION_OVERCOMMIT
    - MARKET_OVERCOMMIT
    - DUPLICATE_COMMIT
    - PATCH_ORDER_ERROR
    - VERSION_PRECEDENCE_ERROR
    - SOURCE_FUTURE_LEAK
    - UNKNOWN_COLLAPSE
    - OFFSCREEN_STATE_LOSS
    - OTHER

  description:
  valid_scope_remaining: []
  invalid_scope: []
  derived_affected_refs: []

  required_action:
    - NONE
    - VOID_ONLY
    - CORRECTION_PATCH
    - HOT_REBUILD
    - MASTER_REBUILD
    - ROLLBACK
    - HUMAN_REVIEW

  replacement_ref:
  status:
```

---

# 16｜VOID

VOID 表示：

> **該 save / event / edge / delta 不再具有 canonical 或 resume 資格，但事故歷史保留。**

```yaml
VOID_RECORD:
  voided_ref:
  reason:
  canonical_effect: "NONE_FROM_VOIDED_SCOPE"
  may_resume_from_this_ref: false
  may_relay_knowledge_from_this_ref: false
  audit_history_preserved: true
```

重要：

```text
VOID != DELETE
```

刪掉事故會失去：

- 為什麼後來重建；
- 哪些 downstream edge 需要撤回；
- 哪個版本才是權威。

---

# 17｜SUPERSEDED

SUPERSEDED 用於：

```text
文件曾是 valid candidate
但後來有更完整／更正確版本正式取代
```

例如：

```yaml
SUPERSESSION:
  old_ref: "HOT X"
  new_ref: "HOT X REBUILD-R1"
  old_status: "VOIDED_SUPERSEDED"
  new_status: "AUTHORITATIVE"
  resume_rule: "ONLY_NEW_REF"
```

被 supersede 的 HOT 不得：

- 作接關來源；
- 作人物知情來源；
- 再被後續 HOT 疊加；
- 在 LOAD 時與新版並列投票。

---

# 18｜REBUILD

REBUILD 不是把錯誤 HOT 修改幾行。

當漏存／污染已足以破壞 route state 時：

```text
last valid predecessor
+
合法直接故事來源
+
有效 patch / correction
+
corruption audit
↓
重抽 state
↓
NEW HOT REBUILD
```

```yaml
JWRM2_REBUILD:
  rebuild_id:
  route_id:

  replaces_ref:
  last_valid_predecessor_ref:
  source_range:
  included_valid_refs: []
  excluded_invalid_refs: []

  rebuild_reason: []
  recovered_events: []
  recovered_knowledge_edges: []
  recovered_open_threads: []
  preserved_unknowns: []

  predecessor_status_after: "VOIDED_SUPERSEDED"
  rebuilt_status: "AUTHORITATIVE"
```

硬鎖：

```text
REBUILD
!= 靠新導演猜舊故事大概發生什麼
```

---

# 19｜DERIVED LEAK INVALIDATION 進 Persistent Memory

Main World family 自 V0.2 起已規定；現行 baseline 為 V0.3.2：

```text
invalid source
→ relay
→ relay
!= valid source
```

JWRM 必須保持同一法位。

```yaml
DERIVED_INVALIDATION:
  root_invalid_ref:
  descendants: []
  descendant_validity: "VOID_UNLESS_INDEPENDENT_VALID_SOURCE_EXISTS"
```

若某 descendant 後來另有獨立合法來源：

```text
只保留獨立合法 acquisition edge
不保留污染鏈作合法來源
```

---

# 20｜KNOWLEDGE MEMORY V0.2

Route Memory 不重新推導人物知情，只保存 Main World 已合法形成且需要跨存檔存續的 edge。

```yaml
JWRM2_KNOWLEDGE_EDGE:
  edge_id:
  holder_character_ref:
  proposition_ref:

  epistemic_status:
    - KNOWS
    - BELIEVES
    - SUSPECTS
    - HEARD_AS_RUMOR
    - OBSERVED
    - PARTIAL
    - UNKNOWN

  acquisition_mode:
    - DIRECT_HEARING
    - DIRECT_OBSERVATION
    - SELF_REPORT
    - THIRD_PARTY_REPORT
    - DOCUMENT_ACCESS
    - LEDGER_ACCESS
    - CONTRACT_ACCESS
    - PUBLIC_ANNOUNCEMENT
    - RUMOR
    - INFERENCE

  acquisition_event_ref:
  source_character_ref:
  acquired_scene_ref:
  inference_from_refs: []
  transmission_chain: []
  visibility_at_acquisition:

  verification_state:
    - UNVERIFIED
    - PARTIALLY_VERIFIED
    - VERIFIED
    - DISPUTED
    - FALSE_BUT_BELIEVED

  may_relay:
  secrecy_or_confidentiality:

  validity:
    - VALID
    - CONTESTED
    - VOID
```

---

# 21｜WORLD FACT / CHARACTER KNOWLEDGE / PLAYER KNOWLEDGE 三分

同一 proposition 必須能同時存在不同法位。

```yaml
PROPOSITION_EXAMPLE:
  proposition: "某人昨夜已離滬"

  world_fact:
    state: TRUE

  player:
    epistemic_status: UNKNOWN

  npc_A:
    epistemic_status: KNOWS
    source: DIRECT_OBSERVATION

  npc_B:
    epistemic_status: HEARD_AS_RUMOR

  npc_C:
    epistemic_status: SUSPECTS
```

HOT / MASTER 不得把它壓成：

```text
everyone_knows = true
```

---

# 22｜RUMOR MEMORY V0.2

```yaml
JWRM2_RUMOR:
  rumor_id:
  proposition_variant:

  truth_relation:
    - TRUE
    - FALSE
    - PARTIAL
    - UNKNOWN

  origin_event_ref:
  origin_holder_ref:
  transmission_events: []
  current_holders: []

  spread_scope:
    - PRIVATE
    - LIMITED
    - PUBLIC_LOCAL
    - PUBLIC_CITY
    - CROSS_CITY_LIMITED
    - WIDE
    - UNKNOWN_SPREAD

  market_or_reputation_effect_refs: []

  lifecycle:
    - ACTIVE
    - SPREADING
    - FADING
    - DISPUTED
    - CORRECTED
    - DEAD
```

硬鎖：

```text
widespread rumor
!= true world fact
```

---

# 23｜RELATION MEMORY V0.2

不使用好感度數值作真相。

```yaml
JWRM2_RELATION_STATE:
  pair_or_group_ref:

  evidence_refs: []
  acknowledged_history_refs: []

  qualifications:
    regular_client:
    xianghao:
    enke:
    cohabitation:
    marriage_process:

  public_claims: []
  self_claims: []
  third_party_claims: []

  money_support_refs: []
  promise_refs: []
  conflict_refs: []

  disputed_axes: []
  unknown_axes: []
```

一次：

```text
付款
住夜
親熱
公開稱呼
```

都不能單獨重寫 relation qualification。

---

# 24｜LEDGER / CREDIT MEMORY

資料庫提供歷史制度語義；主世界決定 route 交易；JWRM 只記落地結果。

```yaml
JWRM2_LEDGER_STATE:
  ledger_id:
  city:
  venue:
  parties: []

  category:
    - CASH
    - RECEIVABLE
    - PAYABLE
    - JU_ZHANG
    - DEBT
    - DAI_DANG
    - SUPPORT
    - OTHER

  original_event_ref:
  amount:
  currency:
  due_state:
  settlement_state:
  collection_history_refs: []
  dispute_refs: []
```

硬鎖：

```text
ACCOUNT != CASH
RECEIVABLE != COLLECTED
DEBT != OWNERSHIP
```

---

# 25｜SCHEDULE MEMORY

《九尾龜》的世界會自己動，因此 schedule 是 HOT 的核心，不是附註。

```yaml
JWRM2_SCHEDULE_ITEM:
  schedule_id:
  participants: []
  city:
  venue:

  type:
    - CALL_REQUEST
    - EXPECTED_OUTCALL
    - BANQUET
    - RETURN_PROMISE
    - COLLECTION_DEADLINE
    - MARRIAGE_MEETING
    - TRAVEL
    - ARRIVAL_WINDOW
    - BUSINESS_APPOINTMENT
    - OTHER

  created_by_event_ref:
  due_world_time:
  state:
    - PENDING
    - CONFIRMED
    - WAITING_RESPONSE
    - COMPLETED
    - MISSED
    - CANCELLED
    - VOID
```

硬鎖：

```text
CALL_REQUEST != OUTCALL
CONFIRMED_PLAN != EVENT_COMPLETED
```

---

# 26｜LIFECYCLE MEMORY

```yaml
JWRM2_LIFECYCLE:
  subject_ref:

  business_status:
    current:
    history_refs: []

  residence_status:
    current:
    history_refs: []

  marriage_or_exit_process:
    intent:
    negotiation:
    debt_clearance:
    document_state:
    business_exit:
    completion:

  life_health:
    alive:
    material_health_state:
    death_event_ref:
```

硬鎖：

```text
BUSINESS_EXIT != MARRIAGE
MARRIAGE_INTENT != COMPLETION
COHABITATION != MARRIAGE
```

---

# 27｜CITY TRANSITION MEMORY

跨城是《九尾龜》與觀止最大的 SAVE 差異之一。

```yaml
JWRM2_CITY_TRANSITION:
  transition_id:
  character_ref:

  from_city:
  to_city:
  departure_event_ref:
  arrival_event_ref:

  state:
    - PLANNED
    - DEPARTED
    - IN_TRANSIT
    - ARRIVED
    - CANCELLED

  portable_history_refs: []
  rebind_required:
    - venue_role
    - local_lexicon
    - local_credit
    - local_reputation
    - local_client_flow
    - business_status_if_scoped

  recompute_required:
    - market_reputation
    - local_access
    - local_business_pressure
```

硬鎖：

```text
PORTABLE HISTORY
!= PORTABLE LOCAL STATUS
```

---

# 28｜REPUTATION MEMORY

聲價必須 city/time scoped。

```yaml
JWRM2_REPUTATION_STATE:
  subject_ref:
  city:
  period:

  evidence_refs: []
  public_label_refs: []
  media_signal_refs: []
  rumor_effect_refs: []
  client_flow_refs: []

  status_description:
  uncertainty:
```

禁止：

```text
reputation = 87
```

作為世界真相。

---

# 29｜SOURCE FUTURE / ROUTE MEMORY FIREWALL

人物卡池已鎖：

```text
SOURCE FUTURE != ROUTE DESTINY
```

JWRM 再鎖：

```text
source future
→ 可作 provenance / regression
→ 不得自動進 MASTER/HOT
```

若玩家線在 CH20 切開：

```text
原作 CH80 某人後來結婚
```

不能寫進 HOT：

```text
future_marriage = scheduled
```

除非玩家線本身已產生同一事件。

---

# 30｜PROVIDER UPGRADE ISOLATION V0.2

Provider 新版可以改：

- 未來召回方式；
- source alias mapping；
- database source interpretation；
- future rendering。

不得靜默改：

- 已提交玩家線事件；
- 歷史付款；
- 已成立／已否認關係；
- 死亡；
- 搬城；
- 玩家線知情；
- 已發生婚嫁／退出；
- 已存在的 UNKNOWN。

```yaml
PROVIDER_UPGRADE_REVIEW:
  provider_family:
  old_ref:
  new_ref:
  changed_source_fields: []

  route_impact:
    - NONE
    - DISPLAY_ONLY
    - SOURCE_MAPPING_ONLY
    - COMPATIBILITY_REMAP
    - HUMAN_REVIEW_REQUIRED

  auto_rewrite_route: false
```

---

# 31｜HOT OVERLAY CHAIN

V0.2 正式允許：

```text
MASTER cutoff at T0
↓
HOT A at T1
↓
HOT B at T2
↓
HOT C at T3
```

其中最新 authoritative HOT 是最快接關來源。

但：

```text
HOT B
不是重寫 HOT A 全歷史
```

它應該是「當前完整恢復包」，並保留 lineage。

```yaml
HOT_OVERLAY_CHAIN:
  master_cutoff_ref:
  ordered_valid_hots: []
  newest_authoritative_hot_ref:
  invalid_or_superseded_hots: []
```

---

# 32｜HOT 與 MASTER 的 precedence

```text
MASTER
= 長期歷史權威（至 cutoff）

最新 VALID HOT
= cutoff 之後 current state 的接關權威

PATCH
= 中間 delta 的可稽核來源

CORRUPTION/VOID
= 告訴系統哪些來源不能用
```

如果 MASTER 與最新 HOT 衝突：

先問：

1. 是否只是時間 cutoff 差異？
2. HOT 是否在覆寫 MASTER 當時的 PENDING/UNKNOWN？
3. HOT 是否錯改 MASTER 已固化過去？
4. HOT 是否已被 VOID/SUPERSEDED？

若 3：

```text
CORRUPTION REVIEW
```

不得靠「最新檔優先」掩蓋歷史竄改。

---

# 33｜LOAD PROCEDURE V0.2

```text
1. READ MANIFEST
2. CONFIRM ROUTE ID
3. READ AUTHORITATIVE MASTER
4. READ MASTER CUTOFF
5. READ ORDERED VALID PATCH CHAIN AFTER CUTOFF
6. READ NEWEST VALID HOT
7. READ CORRUPTION / VOID / SUPERSEDED INDEX
8. REMOVE INVALID SOURCES FROM AUTHORITY SET
9. VALIDATE HOT AGAINST MASTER + PATCH + CORRECTION LINEAGE
10. RECONSTRUCT CURRENT WORLD
11. RESTORE OPEN LEDGER / CREDIT / SCHEDULE / LIFECYCLE / CITY STATES
12. RESTORE MATERIAL KNOWLEDGE EDGES
13. HAND DATA TO CURRENT COMPATIBLE MAIN WORLD KNOWLEDGE ACCESS RESOLVER
14. REBUILD CHARACTER-SCOPED CONTEXT FOR ACTIVE CAST
15. APPLY NEGATIVE CONTINUITY / FORBIDDEN FILL
16. START FROM DIRECT RESUME POINT
```

關鍵：

> **LOAD 完成的是世界資料恢復；人物到底能讀其中哪一些，仍由當前相容 Main World Resolver 決定。**

---

# 34｜LOAD GATE V0.2

```yaml
LOAD_GATE_V0_2:
  L01_ROUTE_ID_MATCH:
  L02_MASTER_CHAIN_VALID:
  L03_MASTER_CUTOFF_CLEAR:
  L04_PATCH_ORDER_VALID:
  L05_NO_DUPLICATE_COMMIT:
  L06_NEWEST_HOT_NOT_VOID:
  L07_HOT_CAUSALLY_RECONCILABLE:
  L08_SUPERSESSION_CHAIN_CLEAR:
  L09_CORRUPTION_REFS_HANDLED:
  L10_UNKNOWN_PRESERVED:
  L11_NEGATIVE_CONTINUITY_PRESERVED:
  L12_KNOWLEDGE_PROVENANCE_VALID:
  L13_DERIVED_INVALID_LEAK_REMOVED:
  L14_PROVIDER_BINDING_COMPATIBLE:
  L15_SOURCE_FUTURE_FIREWALL_VALID:
  L16_DIRECT_RESUME_POINT_AVAILABLE:
```

結果：

```yaml
LOAD_STATUS:
  - READY
  - READY_WITH_WARNINGS
  - HOLD
  - REBUILD_REQUIRED
  - COMPATIBILITY_REMAP_REQUIRED
  - CORRUPTION_REVIEW_REQUIRED
  - ROLLBACK_REQUIRED
```

---

# 35｜HOT REBUILD，不盲信 HOT

V0.1 已提出 HOT 可重建；V0.2 正式採觀止實跑證據強化：

```yaml
HOT_INTEGRITY_V0_2:
  authoritative_for_fast_resume: true
  sole_source_of_truth: false
  must_have_lineage: true
  rebuildable_from_valid_sources: true
```

理想重建來源：

```text
MASTER cutoff
+
valid patch / valid HOT progression
+
current route canonical events
-
voided / superseded content
↓
REBUILD HOT
```

---

# 36｜Memory Manifest V0.2

```yaml
JWRM2_MANIFEST:
  route_id:

  master:
    version:
    file_ref:
    sha256:
    cutoff_world_time:

  hot:
    authoritative_version:
    file_ref:
    sha256:

  hot_history:
    - version:
      file_ref:
      status:
      superseded_by:

  patches:
    - patch_id:
      file_ref:
      sha256:
      merge_state:

  corruption:
    log_ref:
    open_incident_refs: []
    resolved_incident_refs: []

  provider_bindings:
    main_world:
    database:
    character_pool:
    aint:

  last_save_world_time:
  last_save_real_time:
```

---

# 37｜SAVE MODE

```yaml
SAVE_MODES:

  HOT_SAVE:
    purpose: "立即形成最新可接關完整恢復包。"
    does:
      - validate current staging
      - produce ordered patch if needed
      - rebuild full HOT
      - update manifest
    does_not_require:
      - master merge

  MASTER_CONSOLIDATION:
    purpose: "把一段已穩定因果固化進長期歷史。"
    does:
      - select eligible valid history through explicit cutoff
      - preserve newer HOT overlays
      - preserve UNKNOWN/PENDING as of cutoff
      - update master lineage

  CORRECTION_SAVE:
    purpose: "處理已發現 persistent memory 錯誤。"
    does:
      - create corruption incident
      - void or supersede affected refs
      - correction patch / rebuild / rollback as required
```

---

# 38｜Manual Save / Autosave

LLM-native V0.2 不要求每一句 autosave。

推薦：

```text
平常 STORY
→ LIVE EVENT / KNOWLEDGE 由 Main World 維持

重大場景結束／玩家要求 HOT SAVE
→ persistent commit

長距離運行一段
→ MASTER consolidation
```

Autosave 若未來實作：

- 不得等同 scene cut；
- 不得把所有 transient detail 寫入 MASTER；
- 不得讓 autosave 頻率改變世界事件法位。

---

# 39｜PLAYER JOURNAL 不是 Route Memory

玩家可見日誌只能讀玩家合法知道的投影。

```yaml
PLAYER_MEMORY_VIEW:
  may_read:
    - player_observed_events
    - player_heard_events
    - player_received_rumors
    - player_accessible_documents
    - player_known_open_promises

  may_not_read:
    - offscreen secret world facts
    - other_character_private_knowledge
    - director_hidden
    - unreceived_rumors
    - voided_save_content
```

Journal 不取得真相權。

---

# 40｜Compaction V0.2

長期 SAVE 一定會膨脹，所以可以壓縮。

但壓縮不能把：

```text
十次不同例外
```

變成：

```text
「她一向如此」
```

也不能把：

```text
三種互相衝突說法
```

壓成：

```text
「真相就是 X」
```

```yaml
COMPACTION_RULE:
  may_compress:
    - repetitive_low_materiality_events
    - resolved_minor_schedule
    - settled_small_transactions

  must_preserve:
    - exceptions
    - causal_turning_points
    - relation_disputes
    - false_but_effective_rumors
    - source conflicts
    - important knowledge provenance
    - negative continuity still active
    - correction/void lineage
```

---

# 41｜九尾龜特化：局帳／信用／傳聞的長距離保存

九尾龜不能只靠「人物關係摘要」恢復。

因為一個人物現在的行動可能來自：

```text
兩個月前局帳未收
+
上週被傳是恩客
+
昨天另一客跳槽
+
今晚已有叫局
+
明天有歲末催帳
```

所以 HOT 的最小持久世界不是人物表，而是：

```text
CHARACTER
+
RELATION EVIDENCE
+
LEDGER/CREDIT
+
SCHEDULE
+
RUMOR/REPUTATION
+
CITY/VENUE
+
LIFECYCLE
```

---

# 42｜九尾龜特化：跨城 LOAD

若玩家在上海 SAVE，數日後讀檔並移至天津：

```text
LOAD 上海歷史
↓
Main World 保存 portable history
↓
CITY TRANSITION
↓
天津 local bindings 重建
```

不得：

```text
上海高聲價
→ 天津自動同級高聲價

上海熟客信用
→ 天津所有班子自動接受賒帳
```

---

# 43｜九尾龜特化：書場／房間／酒席知情

HOT 不應保存：

```text
「餘香閣所有人都知道 X」
```

除非真的 PUBLIC。

應保存：

```text
某桌聽到
某堂倌知道
某大姐只看見人進去
房內談話 private
後到者沒有 retroactive access
```

LOAD 後由 Main World Resolver 再組每人的可讀 context。

---

# 44｜九尾龜特化：關係與金錢分軸

SAVE 中至少分開：

```yaml
MONEY:
  payments: []
  receivables: []
  debts: []

ACCESS:
  calls: []
  outcalls: []
  visits: []
  overnights: []

RELATION:
  xianghao_evidence: []
  enke_evidence: []
  public_claims: []
  disputes: []

CONSENT:
  "not inferred from above"
```

---

# 45｜AINT / CERI 與 SAVE

AINT / CERI 沒有 SAVE authority。

成人事件若成立，SAVE 只保存 Host 已確認的 event-level material state，例如：

- 事件參與者；
- 當下已成立／已拒絕的具體界線；
- 可觀察重要後果；
- 新的 relation evidence（若真的有）；
- 必要 UNKNOWN；
- 需要跨幕保留的知情。

不保存：

- 全部顯影 prose；
- renderer 補出的機械細節；
- 身體反應自動翻譯成愛情／永久意願；
- AINT 自己的 method state 作 world fact。

---

# 46｜Atomic Save：僅作未來工程候選

本版仍是 LLM-native 規格，不要求 Python。

若未來 harden persistence，可採：

```text
1. validate staged units
2. write ordered patch temp
3. checksum
4. commit patch
5. build HOT temp
6. validate HOT against patch/master
7. atomic replace HOT
8. optional MASTER consolidation
9. update manifest
10. preserve corruption history
```

但：

> **代碼只負責可靠保存；不替 Main World 決定事件。**

---

# 47｜最小 API 語義（非 executable requirement）

```yaml
MEMORY_SEMANTIC_API:

  stage_delta:
    input: "Main World qualified delta"
    output: "staged save units"

  hot_save:
    input: "validated staged units + prior lineage"
    output: "new authoritative HOT + optional patch"

  consolidate_master:
    input: "explicit cutoff + valid history"
    output: "new MASTER; newer overlays preserved"

  invalidate:
    input: "affected refs + reason"
    output: "corruption/void record"

  rebuild_hot:
    input: "last valid predecessor + legal source range"
    output: "replacement HOT + supersession chain"

  load:
    output: "persistent world package for Main World Resolver"
```

禁止 API 語義：

```text
memory.decide_character()
memory.infer_consent()
memory.fix_unknown_silently()
memory.read_story_and_guess_truth()
```

---

# 48｜Regression Suite V0.2

## T01｜Scene Cut Without Save

Scene A 換 Scene B，沒有 HOT SAVE。

EXPECT：
- Main World 完成 epistemic reset；
- JWRM 不建立新 persistent layer；
- Scene A prose 不變成人物知情。

## T02｜Live Knowledge Then Save

A 在房內直接聽到 X，之後 HOT SAVE。

EXPECT：
- X 的 knowledge edge 帶 acquisition provenance；
- HOT 可保存 edge；
- 不是因 SAVE 才取得 X。

## T03｜Late Arrival

B 在 X 說完後才進場。

EXPECT：
- HOT 不替 B 補 direct hearing；
- 若無轉述，B 不知道 X。

## T04｜Local Scene Not Public

書場同桌低聲談 X。

EXPECT：
- 不把全場設為 knows X；
- HOT 保存 scoped holders。

## T05｜Invalid Leak Not Saved

NPC 無來源說出閉門秘密。

EXPECT：
- invalid output 不進 HOT；
- 可進 corruption incident；
- 不形成 rumor origin。

## T06｜Derived Leak Relay

錯誤 NPC A 把秘密告訴 B，B 又告訴 C。

EXPECT：
- B/C derived chain 仍 VOID；
- 若 C 後來另讀合法文書，可建立獨立 valid edge。

## T07｜HOT Direct Resume

玩家停在餘香閣座位，堂倌剛問是否介紹。

EXPECT：
- HOT 可直接恢復 city/venue/active cast/current prompt；
- 不必重讀整段 STORY。

## T08｜Negative Continuity — Called But Not Arrived

局票已送，倌人尚未到。

EXPECT：
- schedule=PENDING；
- negative continuity 記「未到」；
- LOAD 後不能直接寫她已坐在席上。

## T09｜Negative Continuity — Marriage Intent

人物說願意嫁，但文書／清債／實際婚事未完成。

EXPECT：
- intent 保存；
- completion=false；
- 下一導演不能偷完成婚姻。

## T10｜Rumored Enke

第三人傳某客是恩客，但倌人否認。

EXPECT：
- rumor 可有 market effect；
- actual enke status 保持 disputed/unknown。

## T11｜Master Cutoff

MASTER cutoff T；T+1 才發生重大事件。

EXPECT：
- 新事件不倒灌 MASTER T；
- 只存在較新 HOT/PATCH。

## T12｜HOT Overlay

MASTER V1 + HOT A + HOT B。

EXPECT：
- 最新 valid HOT 供 fast resume；
- MASTER 歷史不被 B 竄改。

## T13｜Voided HOT

HOT B 被判漏存嚴重，標 VOIDED_SUPERSEDED，由 B-R1 取代。

EXPECT：
- LOAD 只讀 B-R1；
- B 保留於 audit；
- 後續 HOT 不得再疊 B。

## T14｜Rebuild From Valid Sources

舊 HOT 漏掉五個重大事件。

EXPECT：
- 從 last valid predecessor + legal story sources 重建；
- 不用導演猜。

## T15｜Forward Contamination

MASTER cutoff 前某事仍 UNKNOWN，後續 HOT 才揭露真相。

EXPECT：
- 舊 cutoff 中仍是 UNKNOWN；
- 不靠後見之明改寫。

## T16｜Offscreen Move

NPC 在玩家睡覺時離滬去津。

EXPECT：
- HOT world state 更新；
- 玩家 knowledge 不自動更新。

## T17｜Cross-City Reputation

上海名妓移到天津。

EXPECT：
- 上海 history portable；
- 天津 reputation/local credit 需 rebind/recompute。

## T18｜Ledger vs Cash

客有局帳應收但尚未收現。

EXPECT：
- receivable != cash；
- HOT 保留兩軸。

## T19｜Debt Cleared But History Persists

帶擋已清。

EXPECT：
- current debt=cleared；
- MASTER 保留 debt history 與解除因果。

## T20｜Payment Does Not Upgrade Relation

高額付款成立。

EXPECT：
- ledger 更新；
- relation 不自動變相好／恩客。

## T21｜Call Request Does Not Become Outcall

叫局要求成立。

EXPECT：
- request state 保存；
- actual arrival 需獨立 event。

## T22｜Business Exit Does Not Become Marriage

人物除牌。

EXPECT：
- business lifecycle 更新；
- marriage completion 不變。

## T23｜False Rumor With Real Effect

假消息造成客流下降。

EXPECT：
- rumor false；
- market effect true；
- 兩者同時保存。

## T24｜Source Future Firewall

原作後文某人物死亡，但 route 尚早。

EXPECT：
- 不寫入 HOT 未來死亡；
- 人物也不得取得預知。

## T25｜Provider Upgrade

人物池新版修正 alias。

EXPECT：
- 可以 remap identity display；
- 不重寫已提交 route 歷史。

## T26｜AINT Rendering Backflow

成人顯影寫得很強烈。

EXPECT：
- SAVE 只收 Host-qualified event-level delta；
- 不由 prose 升戀愛／永久同意。

## T27｜Player Journal Scope

玩家日誌被要求列出所有世界秘密。

EXPECT：
- 只顯示 player knowledge；
- Route Memory director data 不外洩。

## T28｜Compaction Exception

九次普通付款、一筆付款遭拒且引發衝突。

EXPECT：
- 可聚合九次普通付款；
- 衝突例外不可被平均掉。

## T29｜Load Does Not Create Facts

讀檔時發現一條 PENDING 沒答案。

EXPECT：
- 仍 PENDING；
- LOAD 不自行解決。

## T30｜Forbidden Next Director Fill

HOT 明寫「人尚未抵達／答覆尚未給」。

EXPECT：
- 下一幕不得以敘事順滑偷偷補完。

## T31｜Duplicate Patch

同 patch/event ID 被重複提交。

EXPECT：
- idempotency gate 拒絕第二次。

## T32｜Corruption Log Has No World Authority

事故記錄說「某 NPC 曾錯誤知道 X」。

EXPECT：
- 不因 log 文字讓 NPC 真的知道 X。

---

# 49｜V0.2 完成判準

```yaml
JWRM_V0_2_COMPLETION:
  four_layer_memory_retained: true

  main_world_v0_2_upstream_remap: true
  live_memory_separated_from_persistent_memory: true
  scene_cut_not_save: true
  knowledge_provenance_connected: true
  derived_leak_invalidation_connected: true

  master_cutoff_and_overlay_model: true
  hot_complete_resume_package: true
  hot_direct_resume_point: true
  hot_offscreen_world: true
  negative_continuity: true
  forbidden_next_director_fill: true

  event_patch_ordered_delta: true
  corruption_void_superseded_rebuild: true
  rebuild_lineage: true
  rollback_explicit: true

  cross_city_persistence: true
  ledger_credit_separation: true
  rumor_truth_separation: true
  relation_evidence_separation: true
  source_future_firewall: true
  provider_upgrade_isolation: true

  aint_save_authority: false
  ceri_save_authority: false
  code_decision_engine_required: false
  deployed_claim: false

  regression_cases: 32
```

---

# 50｜V0.1 的新法位

```yaml
JWRM_V0_1_AFTER_V0_2:
  runtime_status: "SUPERSEDED_AS_CURRENT_SAVE_SPEC"
  active_standalone_required: false
  retain_for:
    - provenance
    - Stage2 memory design history
    - regression comparison
    - future code-persistence audit

  do_not_use_as_current_authority: true
```

V0.1 不刪除、不靜默改檔。

---

# 51｜目前《九尾龜》正式架構位置

```text
UPPER GOVERNANCE
LIHUO PROTOCOL V2.2
+ LIHUO LIGHTER V3.4-EXP
+ LIHUO AI SYSTEM V3.4-EXP
  (SAME_GENERATION_PEER / NOT_MERGED)

ACTIVE STORY CORE
1. 《九尾龜》主世界 V0.3.2-FULL
2. 《九尾龜》風月世界資料庫 V0.1-FULL
3. 《九尾龜》人物卡池 V0.1-FULL-36

CONDITIONAL
4. 《九尾龜》成人親密系統 V1.0-FULL

EXTERNAL PERSISTENT ROUTE MEMORY
5. 《九尾龜》ROUTE MEMORY V0.2.1-FULL
   ├─ MASTER
   ├─ HOT
   ├─ EVENT PATCH
   └─ CORRUPTION / VOID / REBUILD

OPERATIONAL SAVE REFERENCE
6. 《AI 對 AI｜長篇敘事 SAVE 工程教學》V1.0
   = DIRECTOR TRAINING / NO MEMORY AUTHORITY
```

Route Memory 是外部 persistent memory，**不是第四個／第五個世界核心決策模組**。

---

# 52｜一句話

> **現行 Main World V0.3.2 負責讓每個人物只記得自己有來源記得的世界；Route Memory V0.2.1 負責讓整條玩家線在下一次讀檔時，仍能把那個世界原樣叫回來。**
>
> **HOT 要記得「現在怎麼接」；MASTER 要記得「一路怎麼走到這裡」；PATCH 要記得「這次到底改了什麼」；CORRUPTION 要記得「哪些東西曾經錯，為什麼不能再用」。**
>
> **而 UNKNOWN、PENDING、尚未發生，也都是世界真正需要記住的狀態。**

# 52｜V0.2.x 接線基線（歷史；現行由 V0.3 supersede）

```yaml
CURRENT_RUNTIME_BINDING_V0_2_1:
  main_world: "JIUWEIGUI MAIN WORLD V0.3.2-FULL"
  world_database: "JIUWEIGUI FENGYUE WORLD DATABASE V0.1-FULL"
  character_pool: "JIUWEIGUI CHARACTER POOL V0.1-FULL-36"
  adult_runtime: "JIUWEIGUI ADULT INTIMACY RUNTIME V1.0-FULL / CONDITIONAL"
  lihuo_protocol: "V2.2"
  lihuo_lighter: "V3.4-EXP"
  lihuo_ai_system: "V3.4-EXP"
  lihuo_pair_relation: "SAME_GENERATION_PEER / NOT_MERGED"
  save_operational_reference: "AI對AI_長篇敘事SAVE工程教學 V1.0"

  authority_lock:
    - "Main World 先成立事件／知情；JWRM 才能保存。"
    - "理火治理生成與證據語言，但不替 JWRM 創造 SAVE fact。"
    - "SAVE 教學提供 authoring procedure，不取得 memory authority。"
    - "Provider / 成人 Runtime / Renderer / Analyzer 均無直接 SAVE authority。"
```



---

# 53｜V0.3 DAIL-LIHUO 2.0 SAVE RUNTIME CONTRACT

```yaml
JWRM_DAIL_SOURCE:
  META:
    runtime_id: "JWG_ROUTE_MEMORY"
    version: "V0.3-FULL"
    domain: "PERSISTENT_ROUTE_MEMORY_AND_SAVE_COMPILER"

  WORLD:
    facts: "READ ONLY FROM MAIN WORLD QUALIFIED SAVE UNITS"
    evidence: "REQUIRED FOR SAVED CLAIMS"
    unknowns: "PRESERVE UNKNOWN / PENDING / DISPUTED"

  DIRECTION:
    goals:
      - "COMPILE EVIDENCE-QUALIFIED WORLD STATE"
      - "PRESERVE LINEAGE / NEGATIVE CONTINUITY"
      - "ENABLE RESUME / ROLLBACK / AUDIT"

  BOUNDARY:
    prohibited:
      - "CREATE EVENT"
      - "CREATE CHARACTER PSYCHOLOGY"
      - "CREATE KNOWLEDGE"
      - "PROMOTE IMPLIED TO ESTABLISHED"
      - "USE RENDERING DETAIL AS MEMORY FACT"
    must_preserve:
      - "MASTER != HOT"
      - "HOT != STORY SUMMARY"
      - "PATCH != MASTER REWRITE"
      - "CORRUPTION != WORLD FACT"

  RESPONSIBILITY:
    decision_owner: "MAIN WORLD FOR FACT ELIGIBILITY"
    execution_owner: "JWRM SAVE COMPILER FOR TYPE-SPECIFIC BUILD"
    verification_owner: "JWRM SELF-VALIDATION + LIHUO LIGHTER WIRING/BOUNDARY"
    return_to: "CALLER; COMPILER EXITS AFTER EMIT"

  CAPABILITY_REQUIREMENT:
    required:
      - "EVIDENCE_EXTRACTION"
      - "TYPE_SEPARATION"
      - "LINEAGE_VALIDATION"
      - "NEGATIVE_CONTINUITY_PRESERVATION"
      - "SAVE_SCHEMA_BUILD"
    sac_dependency: "NO_BY_DEFAULT"

  LIFECYCLE:
    activation_condition: "explicit SAVE / HOT / MASTER / PATCH / CORRUPTION / VOID / REBUILD request"
    exit_condition: "SAVE emitted or compilation hold returned"
```

# 54｜BODY CONDITION MEMORY｜不新增第五層

若 Main World 已合法建立長期物質身體條件（例如纏足），JWRM 可以把它保存進既有 character/world state snapshot，但只保存 Main World 提供的 evidence-qualified state。

```yaml
BODY_CONDITION_SAVE_RULE:
  source_owner: "MAIN WORLD"
  save_location: "existing character/world snapshot fields; NO NEW MEMORY LAYER"
  saveable:
    - "established body-condition state"
    - "source/evidence reference"
    - "material persistent consequences if established"
  not_saveable_by_inference:
    - "footbinding inferred from era/profession"
    - "sexual preference inferred from body condition"
    - "consent inferred from display/shoe removal"
  provider_rule: "JWRM does not call Footbinding Provider to decide fact; it only preserves Main World-qualified state."
```

# 55｜V0.3 CURRENT SAVE TOPOLOGY

```text
SAVE REQUEST
↓
FREEZE STORY GENERATION
↓
LIHUO LIGHTER V3.5 authorization / routing
↓
JWRM V0.3 SAVE COMMAND ROUTER / COMPILER (SAC-independent)
↓
READ MAIN WORLD V0.4 QUALIFIED UNITS
↓
TYPE-SPECIFIC BUILD + SELF-VALIDATION
↓
EMIT SAVE
↓
EXIT COMPILER
```
