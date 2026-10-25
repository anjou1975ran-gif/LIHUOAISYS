# 觀止青樓｜玩家線人物履歷 RCL V1.0
## Route Character Ledger｜人物池 BASE × MASTER 編譯履歷 × HOT Overlay × 臨時人物卡

```yaml
DOCUMENT:
  title: "觀止青樓｜玩家線人物履歷"
  short_id: "RCL"
  version: "V1.0"
  date: "2026-09-10"
  document_type: "EXTERNAL_ROUTE_CHARACTER_MEMORY_LEDGER_SPEC"
  status: "GM_AUTHORIZED_ROUTE_MEMORY_COMPILATION_SPEC"

POSITION:
  character_baseline_owner: "LCAPG"
  route_event_evidence_owner: "MASTER SAVE / HOT SAVE"
  ledger_owner: "ROUTE SAVE COMPILER"
  world_fact_authority: false
  character_baseline_authority: false
  event_result_authority: false
  consent_authority: false
  relation_creation_authority: false
  knowledge_creation_authority: false

ALIGNMENT:
  lihuo_lighter:
    version: "V3.5.2-EXP"
    sha256: "af42d36a3d29f1c40ed687a088a480caa04ef6d4f499b0b2b52c1c4eff764343"
    use:
      - "RELATION_LIFECYCLE_CARRY_PROFILE"
      - "ACTIVE_RELATION_PREMATURE_DEACTIVATION_GATE"
  lcapg:
    version: "V3.3"
    sha256: "16621fd3b587b86fec3a605c207a8c57d51e41ddf069541a83418ae5f127cce8"
```

> **人物卡回答：這個人本來是誰。**
>
> **RCL 回答：截至某個 MASTER cutoff，這個人在這條玩家線已經走到哪裡。**
>
> **MASTER EVENT 回答：這個履歷判斷的事件證據到底發生了什麼。**
>
> **HOT 回答：MASTER cutoff 之後、尚未編譯進 RCL 的最新變化。**

---

# 1｜核心資料流

```text
LCAPG BASE
↓
RCL @ CURRENT MASTER CUTOFF
↓
IF DETAIL NEEDED
→ MASTER E## EVENT EVIDENCE
↓
POST-MASTER HOT OVERLAY
↓
CURRENT LIVE CHARACTER STATE
```

固定：

```text
LCAPG BASE
!=
PLAYER ROUTE STATE

RCL SUMMARY
!=
MASTER EVENT BODY

HOT
!=
RCL COMMIT

ROUTE EVENT
!=
LCAPG BASELINE
```

---

# 2｜BASE 不可被玩家線倒灌

```yaml
BASE_FIREWALL:
  source: "LCAPG current legal successor"
  preserves:
    - identity
    - baseline personality
    - fixed pre-route history
    - baseline knowledge boundary
    - fixed body-history facts
    - anti-flattening rules
    - director-hidden baseline where formally established

  route_may_not_write:
    - new baseline personality
    - permanent cross-route relationship
    - route-specific consent history
    - route-specific transaction
    - route-specific secrets
    - route-specific injuries / pregnancy / contracts
    - route-specific player knowledge

  promotion_exception:
    rule: "只有 GM 明示將某 route result 升格為跨線人物 BASE 時，才另做 LCAPG successor。"
```

---

# 3｜RCL 的最小人物單位

每一名已存在 LCAPG 的人物，以穩定 `source_id` 為第一鍵；統一名冊 order 只作第二索引。

```yaml
ROUTE_CHARACTER_RECORD:
  route_id: "REQUIRED"
  base_ref:
    lcapg_source_id: "REQUIRED"
    unified_order: "SECONDARY"
    name: "REQUIRED"

  compiled_from:
    master_file: "REQUIRED"
    master_version: "REQUIRED"
    master_sha256: "REQUIRED"
    cutoff_event: "REQUIRED"
    cutoff_time: "REQUIRED"

  route_presence:
    state:
      - ACTIVE_ROUTE_CHARACTER
      - REFERENCE_ONLY
      - NOT_ESTABLISHED_IN_MASTER_ROUTE

  current_route_state:
    relation_to_player: "EVIDENCE SUMMARY ONLY"
    relation_lifecycle:
      - ACTIVE_CONSTRAINING
      - ACTIVE_DORMANT
      - RESOLVED
      - NOT_ESTABLISHED
      - NOT_ENTERED_ROUTE
    current_constraints: []
    active_contracts_or_debts: []
    privacy_or_knowledge_boundaries: []
    unresolved: []

  master_event_index:
    - event_id: "E##"
      title: "MASTER heading only"
      tags: []

  locks: []
```

`relation_lifecycle` 借用 LIHUO LIGHTER V3.5.2 的 carry 語義：

```text
DESCRIPTION_EXIT != RELATION_EXIT
PERSIST != MANIFEST
ACTIVE != SALIENT
UNRESOLVED != MUST_RESOLVE_NOW
STILL_ACTIVE != MUST_PRODUCE_NEW_EVENT
RETENTION != REPETITION
```

RCL 只能**記錄／編譯**某關係在 MASTER cutoff 的生命週期狀態，不能因此創造新的關係事件。

---

# 4｜MASTER 事件優先權

```yaml
EVIDENCE_PRECEDENCE:
  1: "MASTER EVENT BODY / CURRENT HARD STATE"
  2: "RCL COMPILED SUMMARY"
  3: "older RCL version"

  conflict_rule:
    - "RCL 與 MASTER 衝突時，MASTER 勝。"
    - "修正 RCL；不得用 RCL 反向重寫 E##。"
    - "RCL 只可引用已存在於 MASTER 的 event_id。"
    - "需要逐句、逐項、特定知情來源時，返回 MASTER／其合法 detail fallback。"
```

---

# 5｜HOT Overlay 規則

RCL **不在 HOT SAVE 時更新**。

```text
MASTER @ N
+
RCL @ MASTER N
+
HOT N+1
+
HOT N+2
=
LIVE STATE

WHEN MASTER PROMOTES TO N+2
↓
COMPILE NEW RCL @ MASTER N+2
↓
HOT N+1 / N+2 NO LONGER COUNT AS POST-MASTER OVERLAY
```

```yaml
HOT_POLICY:
  may_change_live_state: true
  may_override_older_master_cutoff_for_live_story: true
  may_write_rcl_directly: false
  may_backfill_old_rcl: false

  reason:
    - "HOT 是工作記憶／新事件疊加。"
    - "RCL 是 MASTER promotion 後的長期人物履歷編譯。"
    - "避免每一個 HOT 都產生人物履歷版本漂移。"
```

---

# 6｜MASTER Promotion 的原子更新

每次使用者要求 MASTER SAVE 推進時：

```text
FREEZE STORY
↓
PROMOTE HOT → MASTER E##
↓
VALIDATE MASTER
↓
COMPILE RCL FROM NEW MASTER CUTOFF
↓
VALIDATE ALL RCL EVENT REFERENCES
↓
COMMIT MASTER + RCL AS ONE MEMORY GENERATION
```

```yaml
MASTER_RCL_ATOMICITY:
  master_promotion_without_rcl_refresh: "INVALID_CURRENT_MEMORY_GENERATION"
  rcl_refresh_without_valid_master: "INVALID"
  rollback:
    - "MASTER rollback 時 RCL 必須回到同一 cutoff 的合法版本。"
  no_silent_mix:
    - "不得用 MASTER V5.9 配 RCL V5.12。"
    - "不得用 RCL V5.9 假裝已吸收 HOT V5.10-V5.12。"
```

---

# 7｜知情與秘密分軸

人物出現在 E##，**不等於知道 E## 的全部內容**。

```yaml
KNOWLEDGE_FIREWALL:
  event_participation: "NOT FULL KNOWLEDGE"
  director_hidden: "NOT CHARACTER KNOWLEDGE"
  player_knowledge: "NOT NPC KNOWLEDGE"
  rumor: "NOT FACT"

  optional_event_tags:
    - PARTICIPANT
    - WITNESS
    - KNOWLEDGE_ACQUIRED
    - PARTIAL_KNOWLEDGE
    - PRIVATE_SECRET
    - RUMOR_HEARD
    - RELATION_DELTA
    - CONTRACT
    - DEBT
    - ADULT_EVENT
    - CONSENT_BOUNDARY
    - BUSINESS
    - LEGAL
    - UNKNOWN_RETAINED

  rule:
    - "若某知情差異會改變下一步，RCL 必須在 privacy_or_knowledge_boundaries 中留下來源或限制。"
    - "RCL 不因摘要方便，把導演完整事件視角交給角色。"
```

---

# 8｜臨時 Route Character

若 MASTER 已有重要人物，但 LCAPG 沒有 BASE：

```yaml
TEMP_ROUTE_CHARACTER:
  id_family:
    named: "BYX_TMP_###"
    anonymous_or_unresolved_identity: "BYX_ANON_###"

  fields:
    route_character_id: "STABLE"
    name_or_label: "REQUIRED"
    base_character_ref: null
    master_event_index: []
    route_local_state: {}
    route_local_axes: "OPTIONAL / EVIDENCE-LIMITED"

  authority:
    current_route: true
    cross_route: false
    lcapg_admission: false

  promotion:
    requires: "GM explicit LCAPG promotion"
    method:
      - "保留原 BYX_TMP_### 作 provenance ID。"
      - "新增 promoted_to_base_character: SUPPLEMENTAL_CHARACTER_###。"
      - "不得重寫舊 MASTER 事件中的歷史 route ID。"
```

臨時八軸只能從已成立 Route evidence 抽取：

```text
TEMP AXIS
= ROUTE-LOCAL WORKING CHARACTERIZATION

TEMP AXIS
!= LCAPG BASE
!= CROSS-ROUTE PERSONALITY FACT
!= SOURCE FUTURE
```

如果資料不足，寧可保留：

```text
BASE_DATA_INSUFFICIENT
VOICE_NOT_FIXED
MOTIVE_UNKNOWN
```

不為了湊卡補全。

---

# 9｜查人物的標準讀取順序

```yaml
CHARACTER_READ_ORDER:
  1_BASE:
    source: "LCAPG current successor"
    question: "這個人是誰？"

  2_ROUTE_LEDGER:
    source: "RCL compiled at current MASTER"
    question: "這條線她／他跟玩家走到哪裡？"

  3_EVENT_DETAIL:
    source: "MASTER E##"
    condition: "需要原因、逐項條款、知情、拒絕、承諾或事件細節時"
    question: "為什麼現在會是這個狀態？"

  4_POST_MASTER:
    source: "valid HOT overlays after MASTER cutoff"
    question: "MASTER 之後又發生了什麼？"
```

---

# 10｜RCL 不保存的內容

```yaml
RCL_FORBIDDEN:
  - "小說式完整摘要"
  - "未有事件證據的內心推測"
  - "把性事件自動升格成戀愛"
  - "把付款自動升格成 access / relation / consent"
  - "把職業表演升格成私人真心"
  - "把一次拒絕寫成永久拒絕"
  - "把一次同意寫成 blanket consent"
  - "把未決事項為了摘要方便強制結案"
  - "把 HOT 內容提前吃進舊 MASTER cutoff"
  - "把玩家線結果寫回 LCAPG BASE"
```

---

# 11｜最短根句

> **LCAPG 是人。MASTER 是事。RCL 是這個人走過這些事後，在這條線目前站在哪裡。HOT 是還沒編進長期履歷的新事。**
