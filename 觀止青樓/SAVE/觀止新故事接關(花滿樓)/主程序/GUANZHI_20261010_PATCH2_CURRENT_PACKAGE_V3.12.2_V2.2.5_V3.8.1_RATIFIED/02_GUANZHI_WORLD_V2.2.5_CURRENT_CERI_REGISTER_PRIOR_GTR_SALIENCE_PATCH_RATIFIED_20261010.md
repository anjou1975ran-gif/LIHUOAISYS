# 觀止青樓｜WORLD DATABASE V2.2.5-CURRENT
## CERI Register Prior × GTR Candidate Salience Patch
### 小版本正式批准增量整合版｜2026-10-10

> **正式法位：`V2.2.5-CURRENT / HUMAN_FORMALLY_RATIFIED_PATCH_SUCCESSOR / WORLD_SEMANTIC_PATCH / NOT_HOST_DEPLOYED`。**
>
> 人類 AnjouRan 於 2026-10-10 明示：**「OK 這些問題不是核心  小版本更新就好 直接修改通過」**。
>
> 本版不新增 World DAIL；有效模組數仍為 25。只修正既有 CERI 與 W-D23 GTR 的候選顯著度／生成吸引子：讓「period-compatible」「relation-strategy-compatible」不只合法，而且真的進入場景競爭。

```yaml
WORLD_V2_2_5_PATCH_STATE:
  current: true
  supersedes: GUANZHI_WORLD_V2.2.4_CURRENT
  companion_core: GUANZHI_RUNTIME_CORE_V3.12.1_CURRENT
  companion_director: GUANZHI_DIRECTOR_GUIDANCE_V3.8.1_CURRENT
  world_dail_effective_count: 25
  new_world_dail: NONE
  revised_components:
    - CERI_V0_7_GUANZHI_SELECTION_PRIOR
    - W_D23_GTR_SALIENCE_ADDENDUM
  host_deployment_claim: false
```

---

# W-P01｜CERI V0.7 Guanzhi Selection Prior Addendum

```yaml
CERI_V0_7_GUANZHI_SELECTION_PRIOR:
  provider_version: CERI_V0.7_EXP_UNCHANGED
  corpus_change: NONE
  authority_change: NONE

  general_period_register:
    historical_native_actor:
      qualified_period_candidate: DEFAULT_HIGH_SALIENCE
      generic_modern_candidate: LEGAL_BUT_REQUIRES_POSITIVE_VOICE_OR_SCENE_CAUSE_TO_DISPLACE

    modern_or_cross_time_actor:
      source_native_register: DEFAULT_HIGH_SALIENCE_WHEN_COMPATIBLE
      forced_historical_register: NOT_REQUIRED

    mixed_actor:
      current_character_voice: PRIMARY
      period_context: STRONG_COMPATIBILITY_INPUT

  provider_insufficient:
    rule: "缺少足夠 period candidate 時保持 UNKNOWN / provider-insufficient，不為了古味偽造語源。"

  locks:
    - "CERI PRIOR != CLASSICALIZATION MANDATE"
    - "CHARACTER VOICE > CORPUS NOVELTY"
    - "PERIOD AUTHENTICITY != RARE-WORD DUMP"
    - "PLAYER MODERN INPUT != NPC MODERN OUTPUT BY DEFAULT"
```

---

# W-P02｜W-D23 GTR Salience Addendum

```yaml
WORLD_GTR_PROFESSIONAL_COURTSHIP_SALIENCE_ADDENDUM:
  module_ref: WORLD.GTR_PROFESSIONAL_COURTSHIP
  module_count_change: NONE

  when_scene_contains_any_materially:
    - COURTSHIP_OR_AMBIGUOUS_INTIMACY
    - CLIENT_COURTESAN_SOCIAL_TENSION
    - JEALOUSY_OR_THIRD_PERSON_COMPARISON
    - RETREAT_ADVANCE_DYNAMICS
    - GIFT_TIP_REPEAT_VISIT_OR_PATRONAGE_NEGOTIATION
    - RELATIONAL_TESTING
    - PROFESSIONAL_COMPETITION
    - SOFT_BARGAINING_OR_FACE_SAVING

  candidate_policy:
    - "若 Character interest / standing / scene scope 未排除，至少保留一條 GTR-compatible strategy path 進入候選競爭。"
    - "HIGH_PRIORITY_CANDIDATE 必須有實際 candidate admission，不得只存在於 Director note。"
    - "GTR may emit strategy candidates; Character owns whether to use, reject, invert, mock, or ignore them."

  common_strategy_families:
    - RETREAT_TO_ADVANCE
    - SOFT_COMPARISON
    - THIRD_PERSON_MIRROR
    - DELIBERATE_NON_COMPETITION
    - LET_OTHER_FILL_THE_GAP
    - JEALOUSY_AS_CARE
    - FACE_SAVING_INVITATION
    - BARGAINING_AS_CONCERN

  locks:
    - "GTR CANDIDATE != CHARACTER DECISION"
    - "GTR CANDIDATE != CONSENT"
    - "GTR CANDIDATE != RELATION RESULT"
    - "HIGH_PRIORITY != MUST_WIN"
    - "NO_RELATIONAL_STAKE_OR_CHARACTER_DISINTEREST MAY KEEP GTR DORMANT"
```

---

# W-P03｜CERI × GTR Handoff Clarification

```text
GTR
→ supplies relational strategy candidate when eligible

Character
→ owns whether / how the strategy is actually used

CERI
→ supplies era / locale / role / voice compatible wording

Narrator
→ realizes only qualified semantic state

GTR DOES NOT WRITE CHARACTER WILL.
CERI DOES NOT WRITE RELATION RESULT.
NARRATOR DOES NOT TURN BOUNDARY LAW INTO SPEECH WITHOUT CHARACTER CAUSE.
```

---

# Appendix A｜WORLD V2.2.4-CURRENT 完整父版逐字保留

> Parent SHA-256: `010bd66cfb55e927fddae2951ba612b6b16b04166662cb080534656e209b3b14`
>
> 下方 V2.2.4-CURRENT 頂層 Current 身份保留為形成史；自本檔批准起，以 V2.2.5-CURRENT 為正常讀取面。

<!-- BEGIN VERBATIM WORLD V2.2.4-CURRENT PARENT -->
# 觀止青樓｜WORLD DATABASE V2.2.4-CURRENT
## World-Outcome Sovereignty × Offscreen Major Event × Time-Space Daoist Novice QA / Summon Expansion
### 正式批准完整版｜2026-10-10

> **正式法位：`V2.2.4-CURRENT / HUMAN_FORMALLY_RATIFIED / WORLD_SEMANTIC_SUCCESSOR / JOINT_PACKAGE_CURRENT / NOT_HOST_DEPLOYED`。**
>
> 人類 AnjouRan 於 2026-10-10 在完成聯合候選審計與修補後明示：**「批准 給我正式版本」**。
>
> 本句構成對 `WORLD V2.2.4-RC1` 的正式批准。自本批准事件起，`V2.2.4-CURRENT` 正式取代 `V2.2.3-CURRENT`；與 `GUANZHI RUNTIME CORE V3.12-CURRENT` 互為 Current companion。
>
> 本批准不修改 Protocol／Lighter／Main，不新增第二 Runtime，不把時空道人變成第二 LCAPG owner；也不宣稱 Host deployment、E6/E7、Formal Host execution 或 SAVE instrumentation。

```yaml
WORLD_V2_2_4_RATIFIED_STATE:
  ratification_date: "2026-10-10"
  timezone: "Asia/Taipei"
  human_ratification_instruction: "批准 給我正式版本"
  exact_platform_message_timestamp: "UNKNOWN"

  approved_candidate:
    version: V2.2.4-RC1
    file: "02_GUANZHI_WORLD_V2.2.4_RC1_WORLD_OUTCOME_OFFSCREEN_DAOIST_QA_SUMMON_PENDING_DETERMINATION_20261010.md"
    sha256: "8f33661e88060bd1c7d9c0a6de2f7eaed85e54720aa8992938237e6dacc7bf78"

  status:
    - CURRENT
    - RATIFIED
    - WORLD_SEMANTIC_SUCCESSOR
    - HUMAN_FORMALLY_RATIFIED
    - NOT_HOST_DEPLOYED

  prior_current:
    version: V2.2.3-CURRENT
    treatment:
      - SUPERSEDED_TO_PROVENANCE
      - ROLLBACK
      - REGRESSION
      - NO_RETROACTIVE_REWRITE

  current_package:
    protocol: LIHUO_PROTOCOL_V3.0.1
    lighter: LIHUO_LIGHTER_V4.9
    main: LIHUO_MAIN_V4.4
    runtime_core: GUANZHI_RUNTIME_CORE_V3.12_CURRENT
    world: GUANZHI_WORLD_V2.2.4_CURRENT
    director_guidance: GUANZHI_DIRECTOR_GUIDANCE_V3.8_CURRENT
    character_pool: LCAPG_V3.3.20_CURRENT_71

  world_dail:
    inherited: W-D01_THROUGH_W-D24
    revised:
      - W-D16_WORLD.TIME_SPACE_DAOIST_INTERFACE
      - W-D04_WORLD.ARRIVAL_ROUTING_INTERFACE_ADDENDUM
    added:
      - W-D25_WORLD.OFFSCREEN_MAJOR_EVENT_CAUSALITY
    effective_count: 25

  host_deployment_claim: false
  e6_e7_claim: false
  formal_host_execution_claim: false
```

## Current Read Rule

```text
WORLD CURRENT = V2.2.4-CURRENT
COMPANION CORE = GUANZHI_RUNTIME CORE V3.12-CURRENT

V2.2.3-CURRENT remains provenance / rollback / regression source.
Candidate PENDING / NOT_CURRENT labels below remain formation history only.
```

## Ratified New World Semantics

```text
- 玩家本人重大行動主權與世界結果主權正交
- PLAYER ACTION != WORLD RESULT
- 世界可以在玩家未要求下依法形成 NPC／制度／市場／因果回應
- 場外重大事件區分 CANDIDATE 與 FACT
- EVENT FACT / CAMERA MANIFESTATION / PLAYER KNOWLEDGE 三軸分離
- 玩家拒絕顯影不取消世界事件
- 玩家同意顯影不批准事件結果
- WORLD.TIME_SPACE_DAOIST_INTERFACE 擴充新手 QA、歷史人物關係、故事脈絡解說與玩家招喚 access
- SUMMON != COMMAND
- QA != ORACLE
- 時空權限不抵觀止酒食房錢
- Director relational cast nomination 只送交 World arrival qualification
```

---

# Appendix A｜正式批准之 WORLD V2.2.4-RC1 候選全文逐字保留

> Approved candidate SHA-256: `8f33661e88060bd1c7d9c0a6de2f7eaed85e54720aa8992938237e6dacc7bf78`
>
> 下方候選狀態欄位保留為形成史；Current standing 以本檔頂層批准紀錄為準。

<!-- BEGIN VERBATIM APPROVED CANDIDATE -->

# 觀止青樓｜WORLD DATABASE V2.2.4-RC1
## World-Outcome Sovereignty × Offscreen Major Event × Time-Space Daoist Novice QA / Summon Expansion
### 待判定候選版｜2026-10-10

> **候選法位：`WORLD_SEMANTIC_SUCCESSOR_CANDIDATE / HUMAN_AUTHORIZED_TO_REVISE / PENDING_HUMAN_DETERMINATION / NOT_CURRENT / NOT_HOST_DEPLOYED`。**
>
> 本候選承接 `WORLD V2.2.3-CURRENT`。在未經人類正式判定前，**Current World 仍為 V2.2.3-CURRENT**。
>
> 本版只處理已同意的觀止 World 事項：世界結果主權、場外重大事件自主因果與顯影分離、擴充既有 `WORLD.TIME_SPACE_DAOIST_INTERFACE` 成新手／QA／歷史人物關係解說／玩家可招喚介面，以及 World 對 Director relational cast nomination 的 arrival qualification 接口。
>
> 本版不修改 Protocol／Lighter／Main；不新增第二 Runtime；不把時空道人新增成第二個 LCAPG owner。

```yaml
DOCUMENT:
  id: GUANZHI_WORLD_DATABASE
  version: V2.2.4-RC1
  date: 2026-10-10
  standing:
    - WORLD_SEMANTIC_SUCCESSOR_CANDIDATE
    - HUMAN_AUTHORIZED_TO_REVISE
    - PENDING_HUMAN_DETERMINATION
    - NOT_CURRENT
    - NOT_HOST_DEPLOYED

  parent_current:
    version: V2.2.3-CURRENT
    file: "02_GUANZHI_WORLD_V2.2.3_CURRENT_每日結算跨日推進_WD24_20261008.md"
    sha256: "e5dcf68ce1ef96f1bd98e2fe72dad8b62d2544999cb835139b12c7bc3e7a2011"
    treatment:
      - FULL_INHERITANCE
      - CURRENT_UNTIL_RATIFICATION
      - NO_RETROACTIVE_REWRITE

  proposed_companion_core_if_jointly_ratified: GUANZHI_RUNTIME_CORE_V3.12_CURRENT

  upstream_reference_only:
    protocol: LIHUO_PROTOCOL_V3.0.1
    lighter: LIHUO_LIGHTER_V4.9
    main: LIHUO_MAIN_V4.4

  world_dail:
    inherited: W-D01_THROUGH_W-D24
    revised:
      - W-D16_WORLD.TIME_SPACE_DAOIST_INTERFACE
      - W-D04_WORLD.ARRIVAL_ROUTING_INTERFACE_ADDENDUM
    added:
      - W-D25_WORLD.OFFSCREEN_MAJOR_EVENT_CAUSALITY
    proposed_effective_count_if_ratified: 25
```

---

# A26｜World-Outcome Sovereignty Canon

```yaml
WORLD_OUTCOME_SOVEREIGNTY:
  human_direction_basis: "世界的選擇，高於人類玩家的選擇"

  precise_meaning:
    player_owns:
      - PLAYER_MAJOR_SPEECH
      - PLAYER_BODY_ACTION
      - PLAYER_PAYMENT
      - PLAYER_PROMISE
      - PLAYER_ACCEPTANCE_REFUSAL
      - PLAYER_DISCLOSURE
      - PLAYER_IRREVERSIBLE_CHOICE

    world_owns_or_routes_to_lawful_owner:
      - NPC_DECISION
      - WORLD_RESPONSE
      - INSTITUTIONAL_CONSEQUENCE
      - MARKET_RESPONSE
      - CAUSAL_RESULT
      - WORLD_OWNED_ARRIVAL

  world_may:
    - COOPERATE
    - IGNORE
    - REFUSE
    - OUTMANEUVER
    - MISUNDERSTAND
    - HARM_PLAYER_INTERESTS
    - MAKE_PLAYER_PLAN_FAIL

  world_may_not:
    - DECIDE_PLAYER_MAJOR_ACTION
    - CREATE_PLAYER_CONSENT
    - CREATE_PLAYER_PAYMENT
    - CREATE_PLAYER_PROMISE
    - TURN_PLAYER_PLAN_INTO_GUARANTEED_RESULT

  locks:
    - PLAYER_SOVEREIGNTY_NEQ_WORLD_OUTCOME_SOVEREIGNTY
    - PLAYER_ACTION_NEQ_WORLD_RESULT
    - WORLD_SOVEREIGNTY_NEQ_PLAYER_PUPPETRY
```

> 玩家可以決定自己怎麼做；玩家不能因為自己做了，就取得別人與世界必須照他希望回應的權力。

---

# A27｜Offscreen Major Event Canon

```yaml
OFFSCREEN_MAJOR_EVENT_CANON:
  root:
    - WORLD_MAY_LIVE_OFF_CAMERA
    - PLAYER_INACTION_NEQ_WORLD_FREEZE
    - CAMERA_NEQ_CAUSALITY
    - MANIFESTATION_NEQ_EVENT_CREATION

  standing_classes:
    CANDIDATE:
      meaning: "有 material relevance，尚未形成事實。"
    ESTABLISHED_FACT:
      meaning: "已由 lawful owner + cause + time + standing 建立。"

  major_if_materially_affects_any:
    - MAIN_PATH_AVAILABILITY
    - MATERIAL_RELATION
    - RESOURCE_OR_PROPERTY
    - REPUTATION
    - INSTITUTIONAL_OR_LEGAL_STANDING
    - SAFETY_OR_RISK
    - IMPORTANT_DEADLINE
    - IMPORTANT_PERSON_ARRIVAL_OR_DEPARTURE
    - MATERIAL_OPEN_THREAD_RESULT

  manifestation_relation:
    director_may_ask_player: true
    player_choice_controls: CURRENT_CAMERA_MANIFESTATION
    player_choice_does_not_control:
      - WHETHER_ESTABLISHED_FACT_EXISTS
      - NPC_DECISION
      - WORLD_CAUSALITY

  player_knowledge:
    - OFFSCREEN_FACT_NEQ_PLAYER_CHARACTER_KNOWLEDGE
    - CAMERA_VIEW_NEQ_IN_WORLD_KNOWLEDGE_UNLESS_LAWFULLY_TRANSMITTED

  locks:
    - POSSIBLE_EVENT_NEQ_OCCURRED_EVENT
    - DECLINE_TO_VIEW_NEQ_CANCEL_EVENT
    - ACCEPT_TO_VIEW_NEQ_APPROVE_EVENT
```

---

# W-D25｜WORLD.OFFSCREEN_MAJOR_EVENT_CAUSALITY

```yaml
module_id: WORLD.OFFSCREEN_MAJOR_EVENT_CAUSALITY
human_name: "場外重大事件因果／顯影資格介面"
module_type:
  - OFFSCREEN_WORLD_CAUSALITY
  - MAJOR_EVENT_RELEVANCE
  - MANIFESTATION_ELIGIBILITY_SUPPORT

activation:
  eligible_when:
    - "an off-camera causal line is materially capable of affecting current or near-future route state"
    - "an already-established offscreen fact becomes materially relevant to current story understanding"

reads:
  - QUALIFIED_OPEN_THREAD_REFS
  - WORLD.CAUSAL_STORY_CHAIN
  - WORLD.RUMOR_ECOLOGY_WHEN_RELEVANT
  - WORLD_MARKET_OR_INSTITUTIONAL_PRESSURE
  - NPC_OWNED_QUALIFIED_ACTIONS
  - WORLD_TIME
  - CURRENT_ROUTE_STATE
  - CURRENT_PLAYER_KNOWLEDGE_BOUNDARY

may_emit:
  - OFFSCREEN_MAJOR_EVENT_CANDIDATE_REF
  - OFFSCREEN_MAJOR_EVENT_FACT_REF
  - MATERIAL_RELEVANCE_REF
  - MANIFESTATION_PROPOSAL_ELIGIBILITY_REF

may_not:
  - PREDECIDE_CANDIDATE_RESULT
  - CREATE_PLAYER_KNOWLEDGE
  - CREATE_PLAYER_ACTION
  - FORCE_CAMERA_CUT
  - TURN_MANIFESTATION_DECLINE_INTO_WORLD_FREEZE

invariants:
  - CANDIDATE_NEQ_FACT
  - FACT_NEQ_PLAYER_KNOWLEDGE
  - MANIFESTATION_ELIGIBILITY_NEQ_MUST_MANIFEST
  - OFFSCREEN_NEQ_EVIDENCE_FREE
```

---

# W-D16 Revision｜WORLD.TIME_SPACE_DAOIST_INTERFACE V2.2.4 Candidate Expansion

既有 W-D16 的 Arrival Routing / Fate-Lot 功能全部保留。新增的是 **NOVICE GUIDE / DIEGETIC QA / SOURCE-RELATION EXPLAINER / PLAYER SUMMON ACCESS**。

```yaml
WORLD_TIME_SPACE_DAOIST_INTERFACE_V2_2_4_RC1:
  module_ref: WORLD.TIME_SPACE_DAOIST_INTERFACE

  preserved_roles:
    - WORLD_ROUTING_INTERFACE
    - IN_WORLD_CONTROL_PLANE_MANIFESTATION
    - ARRIVAL_ACKNOWLEDGEMENT
    - FIELD_BIAS_FATE_LOT_PRESENTATION

  added_roles:
    - NOVICE_WORLD_GUIDE
    - DIEGETIC_QA_COMPANION
    - CHARACTER_INTRODUCTION_PROVIDER
    - SOURCE_HISTORY_EXPLAINER
    - RELATION_EXPLAINER
    - STORY_CONTEXT_EXPLAINER
    - PLAYER_SUMMONABLE_WORLD_INTERFACE

  novice_qa_may_answer:
    - PUBLIC_WORLD_CANON
    - PUBLIC_INSTITUTIONAL_RULES
    - PUBLIC_LOCATIONS_AND_CUSTOMS
    - BASIC_NAVIGATION
    - PUBLIC_CHARACTER_IDENTITY
    - SOURCE_TEXT_FACT
    - SOURCE_STORY_TRACE
    - SOURCE_RELATION_ARC_WITH_EXPLICIT_SOURCE_LABEL
    - PUBLIC_HISTORICAL_OR_LITERARY_RELATION
    - PLAYER_ALREADY_ACCESSIBLE_ROUTE_FACT
    - PLAYER_ALREADY_KNOWN_CURRENT_RELATION
    - DAOIST_OWN_LAWFUL_OBSERVATION
    - LABELLED_RUMOR

  qa_must_distinguish:
    - SOURCE_HISTORY
    - CURRENT_GUANZHI_RELATION
    - PLAYER_KNOWLEDGE
    - RUMOR
    - UNKNOWN

  qa_may_not_reveal:
    - NPC_PRIVATE_MIND
    - CURRENT_HIDDEN_RELATION
    - UNREVEALED_OFFSCREEN_EVENT
    - SECRET_CURRENT_MOTIVE
    - SECRET_IDENTITY_WITHOUT_PLAYER_ACCESS
    - FUTURE_GUANZHI_RESULT
    - SOURCE_FUTURE_AS_CURRENT_MEMORY_WITHOUT_STANDING
    - MAIN_HIDDEN_STATE
    - AGENT_HIDDEN_STATE
    - RUNTIME_INTERNAL_SECRET

  answer_style:
    default_depth: SHORT_PLAYABLE_EXPLANATION
    expand_when_player_asks_for_detail: true
    may_use_personality_humor: true
    may_argue_with_shopkeepers: true
    may_discuss_fenghua_xueyue: true

  player_summon:
    capability_ref: PLAYER.SUMMON_TIME_SPACE_DAOIST
    summon_fee: NONE
    player_may_summon_for:
      - QUESTION
      - HISTORY_OR_RELATION_EXPLANATION
      - NAVIGATION
      - CASUAL_CHAT
      - TEA
      - WINE
      - COMPANY

    summon_does_not_force:
      - SECRET_DISCLOSURE
      - SPECIFIC_ANSWER_IF_UNKNOWN
      - SPECIFIC_CHARACTER_OPINION
      - PRIVATE_SPACE_BREACH

  venue_economy:
    rule:
      - "Summoning the Daoist is not itself a paid commercial service."
      - "Food, wine, tea, room, accompaniment, or other venue goods/services remain subject to ordinary Guanzhi pricing."
      - "Who actually pays depends on the lawful transaction; it is not automatically charged to the player merely because the player summoned him."
    lock:
      - TIME_SPACE_STATUS_NEQ_FREE_WINE
      - SUMMON_RIGHT_NEQ_FREE_COMMERCIAL_SERVICE

  invariants:
    - TIME_SPACE_DAOIST_NEQ_ORACLE
    - QA_NEQ_WORLD_AUTHORITY
    - EXPLAIN_SOURCE_RELATION_NEQ_SET_CURRENT_RELATION
    - SUMMON_NEQ_COMMAND
    - DAOIST_CHARACTER_PRESENCE_NEQ_HIDDEN_TRUTH_ACCESS
```

最短句：

> **時空道人可以解釋世界，但不能替世界爆雷。**

---

# W-D04 Addendum｜WORLD.ARRIVAL_ROUTING × Director Relational Nomination

```yaml
WORLD_ARRIVAL_ROUTING_V2_2_4_ADDENDUM:
  accepts_candidate_sources:
    - EXISTING_WORLD_CAUSALITY
    - CHARACTER_CAUSAL_NEED
    - PLAYER_LAWFUL_SUMMON_WHERE_APPLICABLE
    - DIRECTOR_RELATIONAL_CAST_NOMINATION

  director_nomination_requirements:
    - CAST_CANDIDATE_REF
    - MATERIAL_RELATION_RELEVANCE_REF
    - SOURCE_OR_CURRENT_RELATION_REFS
    - CURRENT_SPACE_ACCESS_CHECK

  qualification_may_consider:
    - WORLD_ACCESS_STATE
    - CURRENT_SPACE_LIFECYCLE
    - CURRENT_TIME_CONTEXT
    - ESTABLISHED_RELATION_RELEVANCE
    - CURRENT_WORLD_PRESSURE
    - ARRIVAL_CAUSALITY

  locks:
    - DIRECTOR_NOMINATION_NEQ_ARRIVAL
    - PLAYER_APPROVAL_NOT_REQUIRED_FOR_LAWFUL_WORLD_OWNED_ARRIVAL
    - ARRIVAL_NEQ_PRIVATE_SPACE_ACCESS
    - FAME_NEQ_ENTRY_STANDING
    - CHARACTER_ENTRY_NEQ_CHARACTER_ACTION
```

---

# V2.2.4-RC1 Read Rule if Ratified

```text
WORLD CURRENT
→ V2.2.4-CURRENT

NEW FIRST-READ DELTAS
→ A26 WORLD-OUTCOME SOVEREIGNTY
→ A27 OFFSCREEN MAJOR EVENT CANON
→ W-D25 OFFSCREEN MAJOR EVENT CAUSALITY
→ W-D16 TIME-SPACE DAOIST EXPANSION when relevant
→ W-D04 ARRIVAL ROUTING ADDENDUM when relational nomination is used

THEN
→ V2.2.3 A25 / W-D24 + inherited W-D01～W-D23 + CERI
```

---

# V2.2.4-RC1 Status

```yaml
STATUS:
  draft_completed: true
  human_ratified: false
  current_world_replaced: false
  host_deployed: false
  waiting_for: HUMAN_DETERMINATION
```

**END OF V2.2.4-RC1 DELTA**

---

# Appendix A｜WORLD V2.2.3-CURRENT 完整父版逐字保留

> Parent Current: `02_GUANZHI_WORLD_V2.2.3_CURRENT_每日結算跨日推進_WD24_20261008.md`  
> SHA-256: `e5dcf68ce1ef96f1bd98e2fe72dad8b62d2544999cb835139b12c7bc3e7a2011`  
> V2.2.3 在本候選獲正式批准前仍是 Current。

<!-- BEGIN VERBATIM WORLD V2.2.3 CURRENT PARENT -->

# 觀止青樓｜WORLD DATABASE V2.2.3-CURRENT｜每日結算 × 跨日世界推進｜正式批准增量整合版
## 2026-10-08｜Human Explicit World Amendment｜Companion Runtime remains GUANZHI_RUNTIME CORE V3.11-CURRENT

> **正式法位：** `V2.2.3-CURRENT / HUMAN_EXPLICITLY_AUTHORIZED / WORLD_SEMANTIC_SUCCESSOR / NOT_HOST_DEPLOYED`。
>
> **人類授權：** 2026-10-08，AnjouRan 明示：
>
> > 「這個每日結算推進是好習慣  應該寫進WORLD^^」
>
> 因此本版在 `WORLD V2.2.2-CURRENT` 之上新增「每日／跨日結算」世界語義，正式作為 V2.2.3-CURRENT。其餘 V2.2.2 世界 Canon、W-D01～W-D23、CERI、人物卡與 SAVE 語義全部繼承，不因本次增補自動改寫。
>
> 本文件只成立專案文件／世界語義法位；不宣稱 Host deployment、E6/E7、Formal Host execution、獨立 Agent 或 SAVE instrumentation 已部署。

```yaml
GUANZHI_WORLD_V2_2_3_CURRENT_MANIFEST:
  document_id: GUANZHI_WORLD_DATABASE
  version: V2.2.3-CURRENT
  date: 2026-10-08
  status: HUMAN_EXPLICITLY_AUTHORIZED_CURRENT

  parent_current:
    version: V2.2.2-CURRENT
    file: "02_GUANZHI_WORLD_V2.2.2_CURRENT_V3.11_RUNTIME_POINTER_INTEGRATED_20261006.md"
    sha256: "ee285407e83436adb4a93b0f5f0d35e4163557bfe471c63e2c71fd6ba1bc843e"
    treatment: "FULL_INHERITANCE + A25 + W-D24"

  upstream:
    protocol: LIHUO_PROTOCOL_V3.0.1
    lighter: LIHUO_LIGHTER_V4.8
    main: LIHUO_MAIN_V4.4
    runtime_core: GUANZHI_RUNTIME_CORE_V3.11_CURRENT

  world_dail:
    inherited: "W-D01 THROUGH W-D23"
    added: "W-D24 / WORLD.DAILY_SETTLEMENT"
    effective_count: 24

  semantic_change:
    canon_addition: "A25 / DAILY-CROSSDAY WORLD ADVANCE"
    dail_addition: "W-D24 / WORLD.DAILY_SETTLEMENT"
    character_base_change: NONE
    save_schema_change: NONE
    save_write_owner_change: NONE
    player_sovereignty_change: NONE

  host_deployment_claim: false
  e6_e7_claim: false
```

---

# Current Read Rule｜V2.2.3

```text
WORLD CURRENT
→ V2.2.3-CURRENT

READ FIRST
→ A25 DAILY / CROSS-DAY WORLD ADVANCE
→ W-D24 WORLD.DAILY_SETTLEMENT when a day/time jump is material

THEN
→ inherited V2.2.2 Canon / W-D01～W-D23 / CERI as scene-relevant

RUNTIME CORE
→ GUANZHI RUNTIME CORE V3.11-CURRENT

V2.2.2
→ FULL PARENT / PROVENANCE / ROLLBACK
```

---

# A25｜每日結算／跨日世界推進 Canon

```yaml
DAILY_CROSSDAY_WORLD_ADVANCE:
  root:
    - "PLAYER INACTION != WORLD FREEZE"
    - "DAY CHANGE != ALL OPEN THREADS AUTO-CLOSE"
    - "DEADLINE PASSED != RETROACTIVE COMPLETION"
    - "OFFSCREEN WORLD LIFE REQUIRES OWNER + CAUSE + TIME"

  purpose:
    - "讓已成立的行政、營運、交易履行、NPC 自主與長因果，不因鏡頭離開或玩家睡眠而永遠停在 PENDING。"
    - "讓玩家錯過時間、睡過頭、延誤約定時，世界留下真實後果，而不是替玩家補做。"
    - "在新一天第一個正文場景前，先把昨日 OPEN / DUE / PLANNED / UNKNOWN 狀態按 owner、證據與成熟度重新分類。"

  mandatory_preservations:
    - "PLAYER MAJOR DECISION remains PLAYER-owned."
    - "NPC major personal decision remains that NPC-owned."
    - "UNKNOWN without sufficient evidence remains UNKNOWN."
    - "Later completion does not rewrite earlier PENDING as earlier-completed."
    - "SAVE records settlement only after evidence/world result is qualified; settlement itself is not SAVE authority."
    - "Story-visible realization still follows the Current Guanzhi Story cycle and Main entry requirements."

  valid_outcome_classes:
    AUTO_SETTLED:
      rule: "決定與授權早已成立，只剩具 owner 的行政／帳務／物流／例行營運履行，且時間足夠。"
    NPC_AUTONOMOUS_RESOLVED:
      rule: "NPC 在自己權限與人物因果內完成其本人可決事項；不得替玩家或其他 NPC 決定。"
    WORLD_PROCESS_ADVANCED:
      rule: "傳聞、商業準備、官府流程、場地布置、訊息傳遞等世界程序可依法位前進，但只到證據支持的程度。"
    OVERDUE_ROLLOVER:
      rule: "期限已過但所需 actor 未行動；保留 missed / overdue / rescheduled consequence，不得自動補完。"
    PLAYER_OWNED_HOLD:
      rule: "需要玩家重大言語、付款、承諾、接受、拒絕、身體行動或不可逆選擇。"
    NPC_OWNED_HOLD:
      rule: "需要特定 NPC 尚未作出的重大自主決定。"
    EVIDENCE_HOLD:
      rule: "世界可能已有答案，但現行 qualified evidence 不足以合法固定；維持 UNKNOWN / UNRESOLVED。"
    REVEAL_PENDING:
      rule: "結果已可成立，但玩家／場內人物尚未取得知情；事實與知識狀態分離。"
    STILL_ACTIVE:
      rule: "線仍在跑，沒有到應結算的成熟點。"

  time_rule:
    - "若精確完成刻數沒有證據，可記為 BY_SETTLEMENT_TIME / BY_START_OF_DAY / DURING_OFFSCREEN_INTERVAL，不硬補時辰。"
    - "時間跳越大，越需要重新檢查每條 OPEN thread；但不得因時間長就提高不存在的授權。"

  player_sleep_rule:
    - "玩家睡眠／離場期間，世界與 NPC 可繼續合法運作。"
    - "玩家本人沒有明示或既成授權的重大行動，不得被 offscreen 代做。"
    - "約定時間被玩家睡過頭時，預設為 OVERDUE / MISSED，而不是『其實早上做完了』。"

  locks:
    - "DAILY SETTLEMENT != AUTO-PLOT"
    - "DAILY SETTLEMENT != RANDOM EVENT GENERATOR"
    - "DAILY SETTLEMENT != PLAYER PROXY"
    - "DAILY SETTLEMENT != NPC PUPPETRY"
    - "DAILY SETTLEMENT != SAVE COMMIT"
    - "DAILY SETTLEMENT != NARRATOR SHORTCUT"
    - "OFFSCREEN != EVIDENCE-FREE"
    - "WORLD CONTINUES != WORLD MAY FORCE ANY RESULT"
```

---

# W-D24｜WORLD.DAILY_SETTLEMENT

```yaml
module_id: "WORLD.DAILY_SETTLEMENT"
human_name: "每日結算／跨時段未決事件推進"
module_type:
  - "CROSS_DAY_SETTLEMENT"
  - "OPEN_THREAD_RECLASSIFICATION"
  - "OFFSCREEN_WORLD_ADVANCE"
  - "DEADLINE_ROLLOVER"

activation:
  eligible_when:
    - "story date changes"
    - "player sleeps/rests across a meaningful operational window"
    - "explicit time jump crosses due time / business hours / institutional process window"
    - "SAVE re-entry begins materially later than prior freeze"
    - "director handoff requires determining what matured while offscreen"

reads:
  - "CURRENT HOT / qualified SAVE open threads"
  - "due times / deadlines / promised appointments"
  - "event / contract / ledger / official-process standing"
  - "player-owned decisions"
  - "NPC-owned decisions"
  - "WORLD.CAUSAL_STORY_CHAIN qualified chains"
  - "WORLD.RUMOR_ECOLOGY where relevant"
  - "WORLD.CAPITAL_ECOLOGY / ledger semantics where relevant"
  - "current Character BASE / relation state"
  - "elapsed in-world time"

classification_order:
  - "identify owner"
  - "identify whether the substantive decision already exists"
  - "identify remaining work: administrative / operational / personal / evidentiary"
  - "test whether elapsed time and causal conditions were sufficient"
  - "classify result without filling unknowns"

may_emit:
  - "AUTO_SETTLED"
  - "NPC_AUTONOMOUS_RESOLVED"
  - "WORLD_PROCESS_ADVANCED"
  - "OVERDUE_ROLLOVER"
  - "PLAYER_OWNED_HOLD"
  - "NPC_OWNED_HOLD"
  - "EVIDENCE_HOLD"
  - "REVEAL_PENDING"
  - "STILL_ACTIVE"
  - "new due time / carry-forward candidate when causally supported"

integration:
  with_w_d18:
    rule: "W-D18 preserves and qualifies cross-night causal chains; W-D24 evaluates what matured when time actually advances."
  with_save:
    rule: "W-D24 may provide qualified settlement deltas; SAVE owner decides actual commit under existing SAVE law."
  with_story_cycle:
    rule: "If settlement results are realized as story-visible language, use the normal Current Guanzhi Story cycle; W-D24 does not bypass Main/CERI/Narrator/Lighter."

invariants:
  - "SETTLEMENT RESULT MUST HAVE SOURCE / OWNER / TIME BASIS"
  - "PLAYER SILENCE != PLAYER CONSENT"
  - "PLAYER SLEEP != PLAYER ACTION"
  - "NPC AUTONOMY != DIRECTOR WHIM"
  - "ADMINISTRATIVE COMPLETION MAY OCCUR OFFSCREEN WHEN SUBSTANTIVE AUTHORIZATION ALREADY EXISTS"
  - "MISSED APPOINTMENT MAY BECOME OVERDUE WITHOUT BEING SECRETLY COMPLETED"
  - "LATER SETTLEMENT != EARLIER COMPLETION"
  - "RESULT FACT != PLAYER KNOWLEDGE OF RESULT"
  - "UNKNOWN MAY SURVIVE DAILY SETTLEMENT"

may_not:
  - "create player payment / promise / sex / refusal / acceptance / disclosure"
  - "create NPC consent or irreversible personal choice without NPC-qualified cause"
  - "invent official approval merely because paperwork was pending"
  - "erase a missed deadline by backfilling performance"
  - "turn rumor into fact"
  - "mint SAVE / Host / Main / Lighter receipts"
  - "force closure only because a new day started"
```

---

# V2.2.3 Operational Note

```text
DAILY SETTLEMENT asks:

1. What was still open?
2. Who owned the next action?
3. Had the real decision already been made?
4. Could the remaining process lawfully happen while the camera was away?
5. Did the deadline pass without the required actor?
6. What became fact, what merely advanced, what rolled over, and what remains UNKNOWN?

Only after that does the next day's scene begin.
```

---

# Appendix A｜FULL INHERITANCE｜WORLD V2.2.2-CURRENT

> 下方全文保留父版作為完整繼承來源。凡與本版 A25 / W-D24 衝突者，以 V2.2.3 增量條文優先；其他內容原狀繼承。
>
> Parent SHA-256: `ee285407e83436adb4a93b0f5f0d35e4163557bfe471c63e2c71fd6ba1bc843e`

<!-- BEGIN FULL INHERITED WORLD V2.2.2-CURRENT -->

# 觀止青樓｜WORLD DATABASE V2.2.2-CURRENT｜V3.11 Runtime Pointer Integrated
## 量子具身 × 召喚／共鳴 × 陰陽活動通道 × GUANZHI RUNTIME CORE V3.11
### Current 整合版｜2026-10-06

> **法位：`V2.2.2-CURRENT / HUMAN_RATIFIED_WORLD_SEMANTICS / V3.11_RUNTIME_POINTER_INTEGRATED / NOT_HOST_DEPLOYED`。**
>
> 本檔依人類 2026-10-06 指示「把這兩版整合吧 這樣最快」形成 **Current 整合讀取面**。
>
> 整合原則只有一個：**World 語義以已批准的 V2.2.2-CURRENT 為準；Runtime pointer 採已批准的 GUANZHI RUNTIME CORE V3.11-CURRENT。**
>
> 因此，本整合不把 World 降回 V2.2.1，也不把 V2.2.2 的 A3 / W-D04 語義當成新修改；它們自 2026-10-01 起就已是 Current World semantics。

```yaml
GUANZHI_WORLD_V2_2_2_V3_11_INTEGRATED_CURRENT:
  date: "2026-10-06"
  integration_type:
    - CURRENT_WORLD_SEMANTIC_PRESERVATION
    - RUNTIME_POINTER_REFRESH
    - TWO_SOURCE_CONSOLIDATION

  human_direction:
    quote: "我覺得  把這兩版整合吧  這樣最快"
    effect: DIRECT_INTEGRATION_AUTHORIZATION

  current_world:
    version: V2.2.2-CURRENT
    source_file: "02_GUANZHI_WORLD_V2.2.2_CURRENT_量子具身_召喚共鳴_陰陽活動通道語義補完正式批准版_20261001.md"
    source_sha256: "1ea8377d70a7725cccab481a1678fd1fc747244b0e82e93f419ad42437d91b7e"
    original_ratification_date: "2026-10-01"
    semantic_body: PRESERVED
    active_semantic_delta:
      A3:
        - LOCAL_EMBODIMENT_FOR_LAWFUL_DEAD_MANIFESTATION
        - SELF_SELECTED_LIFE_ERA_APPEARANCE_FOR_POSTHUMOUS_MANIFESTATION
        - PRESENTATION_SLICE_SEPARATED_FROM_ONTOLOGICAL_AND_KNOWLEDGE_TIMESTAMP
      W_D04:
        - DIRECT_SUMMONING_SCOPED_TO_DEAD_SOUL_OR_POSTHUMOUS_SELF
        - GHOST_ARRIVAL_REQUIRES_LAWFUL_SUMMONING_OR_SUFFICIENT_CURRENT_FIELD_RESONANCE
        - RESONANCE_DEFINED_AS_CURRENT_FIELD_TENSION_CONCENTRATION_NOT_MERE_NAME_MENTION
        - RESONANCE_MAY_CONNECT_DEAD_SOUL_OR_LIVING_SOURCE_WORLD
        - CROSS_YIN_YANG_ROUTE_RECAST_AS_EVENT_BOUND_AUTHORIZED_INFRASTRUCTURE

  runtime_pointer:
    current: GUANZHI_RUNTIME_CORE_V3.11_CURRENT
    core_file: "01_GUANZHI_RUNTIME_CORE_V3.11_CURRENT_COMPANION_WORLD_V2.2.2_CORRECTED_20261006.md"
    corrected_core_sha256: SEE_PACKAGE_INDEX
    source_core_sha256_before_pointer_correction: "2bce37a04a634cc9b5d87e55b68d772cc392fe9a426bd326a809e5eeb5994d16"

  upstream:
    protocol: LIHUO_PROTOCOL_V3.0.1
    lighter: LIHUO_LIGHTER_V4.8
    main: LIHUO_MAIN_V4.4

  superseded_pointer_surface:
    file: "02_GUANZHI_WORLD_V2.2.1_CURRENT_V3.11_RUNTIME_POINTER_RATIFIED_20261006.md"
    sha256: "ae89de0597eb2e33be0d9027ebd271dfc9987c495becc4054d6f17d6d923f21b"
    treatment:
      - POINTER_SOURCE_ONLY
      - SEMANTIC_WORLD_VERSION_INCORRECT_AS_CURRENT
      - SUPERSEDED_BY_THIS_INTEGRATED_SURFACE
      - RETAIN_FOR_PROVENANCE

  semantic_change_by_this_integration:
    world_canon: NONE
    world_dail: NONE
    ceri_corpus: NONE
    character: NONE
    save_schema: NONE

  hard_locks:
    - WORLD_CURRENT_IS_V2_2_2_NOT_V2_2_1
    - V2_2_2_A3_AND_W_D04_REMAIN_CURRENT
    - POINTER_REFRESH_NEQ_WORLD_SEMANTIC_CHANGE
    - V2_2_1_POINTER_FILE_NEQ_CURRENT_WORLD_SEMANTIC_SOURCE
    - GUANZHI_CORE_V3_11_NEQ_WORLD_SEMANTIC_OWNER
    - NOT_HOST_DEPLOYED
```

## Current Read Rule

```text
WORLD SEMANTICS
→ V2.2.2-CURRENT

RUNTIME CORE
→ GUANZHI RUNTIME CORE V3.11-CURRENT

NORMAL WORLD READ
→ THIS INTEGRATED HEADER
→ THEN V2.2.2 APPROVED WORLD BODY BELOW

OLD V2.2.1 V3.11 POINTER FILE
→ PROVENANCE / POINTER HISTORY ONLY
```

---

# Appendix A｜WORLD V2.2.2-CURRENT 正式批准母版全文

> 下方完整保留 2026-10-01 已批准之 V2.2.2-CURRENT。其原頭部所寫 `Companion Runtime remains V3.6-CURRENT` 只代表當時批准時的 runtime pairing；**本整合頭部的 V3.11 pointer 為目前 Current pairing。**
>
> Source SHA-256: `1ea8377d70a7725cccab481a1678fd1fc747244b0e82e93f419ad42437d91b7e`

<!-- BEGIN VERBATIM WORLD V2.2.2-CURRENT -->

# 觀止青樓｜WORLD DATABASE V2.2.2-CURRENT｜量子具身 × 召喚／共鳴 × 陰陽活動通道｜正式批准版
## 2026-10-01｜Human Ratified Semantic Gap Repair｜Companion Runtime remains GUANZHI_RUNTIME_CORE V3.6-CURRENT

> **正式法位：** `V2.2.2-CURRENT / HUMAN_RATIFIED_CURRENT / NOT_HOST_DEPLOYED`。
>
> **人類批准：** 2026-10-01 使用者明示「批准」，因此本版正式取代 `WORLD V2.2.1-CURRENT` 的 CURRENT 法位；本次批准只成立文件／世界語義法位，不冒稱 Project 已安裝、Host E6/E7、Main/Lighter/CERI 實際執行或 SAVE commit。
>
> **本次只修兩個缺口：** `A3｜量子決算點本體` 與 `W-D04｜WORLD.ARRIVAL_ROUTING`。其餘 Canon、W-D01～W-D23、CERI corpus、人物卡與 SAVE 語義全部繼承父版，不因本候選自動改寫。
>
> **核心補完：** （1）亡魂在觀止可取得真實局部具身與感覺，但不等於復活；（2）死後顯影者可自行選擇想給人看的生命年代外貌，外貌切片與知識／本體時點分離；（3）鬼魂抵達必須具有合法直接召喚或足夠的當前場域共鳴，不能因陰陽通道存在就自由闖入；（4）共鳴是「此刻場內張力／濃度足以接上某人或某魂的世界線」，第三卷式「一人牽一人」是其中一種典型；（5）討論、名字、故事、關係與群體注意濃度過高時，也可能接入活人的來源世界／生命切片，使其取得進場；（6）陰陽跨界通道通常是陰間組織活動前申請、觀止核准後，由時空道人在核准時段搭起的臨時活動通道；（7）合法抵達預設經由觀止門口／門檻／既成入口進場，而非中央瞬間顯影。

```yaml
GUANZHI_WORLD_V2_2_2_CURRENT_MANIFEST:
  document_id: GUANZHI_WORLD_DATABASE
  version: V2.2.2-CURRENT
  date: 2026-10-01
  status: HUMAN_RATIFIED_CURRENT

  parent_current:
    version: V2.2.1-CURRENT
    file: 02_GUANZHI_WORLD_V2.2.1_CURRENT_V3.6_RUNTIME_POINTER_RATIFIED_20261001.md
    sha256: e42e58bb8631b3b53834f0fcc927453c98baa71cacbfb4e0cfae370d067dabce
    treatment: FULL_INHERITANCE_EXCEPT_EXPLICIT_A3_AND_W_D04_REPLACEMENT

  ratification:
    approved_by: USER
    approval_date: 2026-10-01
    approval_phrase: "批准"
    promoted_from: V2.2.2-RC2
    candidate_file: 02_GUANZHI_WORLD_V2.2.2_RC2_量子具身_召喚共鳴_陰陽活動通道語義補完候選_20261001.md
    semantic_change_from_rc2: NONE
    host_deployment_claim: false

  runtime_pairing:
    current: GUANZHI_RUNTIME_CORE_V3.6_CURRENT
    runtime_change: NONE
    host_installation_claim: NONE

  semantic_delta:
    A3:
      - LOCAL_EMBODIMENT_FOR_LAWFUL_DEAD_MANIFESTATION
      - SELF_SELECTED_LIFE_ERA_APPEARANCE_FOR_POSTHUMOUS_MANIFESTATION
      - PRESENTATION_SLICE_SEPARATED_FROM_ONTOLOGICAL_AND_KNOWLEDGE_TIMESTAMP
    W_D04:
      - DIRECT_SUMMONING_SCOPED_TO_DEAD_SOUL_OR_POSTHUMOUS_SELF
      - GHOST_ARRIVAL_REQUIRES_LAWFUL_SUMMONING_OR_SUFFICIENT_CURRENT_FIELD_RESONANCE
      - RESONANCE_DEFINED_AS_CURRENT_FIELD_TENSION_CONCENTRATION_NOT_MERE_NAME_MENTION
      - RESONANCE_MAY_CONNECT_DEAD_SOUL_OR_LIVING_SOURCE_WORLD
      - PERSON_TO_PERSON_CHAIN_IS_A_TYPICAL_RESONANCE_PATTERN_NOT_THE_ONLY_ONE
      - CROSS_YIN_YANG_ROUTE_RECAST_AS_EVENT_BOUND_AUTHORIZED_INFRASTRUCTURE
      - UNDERWORLD_ORGANIZATION_ADVANCE_APPLICATION_AND_GUANZHI_APPROVAL_DEFAULT
      - TIME_SPACE_DAOIST_BUILDS_GATE_ONLY_FOR_APPROVED_EVENT_WINDOW
      - CROSS_YIN_YANG_CHANNEL_NEQ_FREE_GHOST_ACCESS
      - DEFAULT_THRESHOLD_ENTRY_NOT_INSTANT_CENTER_STAGE_MATERIALIZATION

  unchanged:
    - A0_A2_A4_A24_EXCEPT_REFERENCES_TO_REPLACED_A3
    - W_D01_W_D03_W_D05_W_D23_EXCEPT_REFERENCES_TO_REPLACED_W_D04
    - CERI_V0_7_EXP_CORPUS
    - LCAPG_POINTERS
    - SAVE_SCHEMA
    - LIHUO_PROTOCOL_LIGHTER_MAIN_STANDING

  precedence:
    - THIS_CURRENT_A3_REPLACES_INHERITED_A3
    - THIS_CURRENT_W_D04_REPLACES_INHERITED_W_D04
    - V2_2_1_CURRENT_IS_SUPERSEDED_AS_FORMAL_CURRENT_BUT_RETAINED_AS_PARENT_PROVENANCE
```

## RC2 校正紀錄｜相對 RC1

```yaml
RC2_CORRECTIONS:
  - "CROSS_YIN_YANG_ROUTE: 從一般既成亡魂通道，改為陰間組織活動前申請、觀止核准、時空道人於核准時段搭建的 EVENT-BOUND GATE。"
  - "GHOST_ARRIVAL: 通道本身不給個別鬼魂資格；鬼魂必須有合法直接召喚或足夠 CURRENT-FIELD RESONANCE。"
  - "RESONANCE: 明定為當前場內對特定人／魂的張力與濃度，而不是名字／歷史關係的靜態命中。"
  - "LIVING_CONNECTION: 討論／名字／故事／關係／群體注意濃度過大，可接入活人的來源世界／生命切片，使其取得進場。"
  - "PERSON_TO_PERSON_CHAIN: 保留第三卷『一人牽一人』為典型，但不把它封成唯一共鳴形態。"
```

## V2.2.2 正式批准紀錄

```yaml
RATIFICATION:
  version: V2.2.2-CURRENT
  status: HUMAN_RATIFIED_CURRENT
  approved_by: USER
  approval_date: 2026-10-01
  source_candidate: V2.2.2-RC2
  semantic_change_from_candidate: NONE
  supersedes_current: V2.2.1-CURRENT
  runtime_pairing: GUANZHI_RUNTIME_CORE_V3.6_CURRENT
  runtime_change: NONE
  host_deployment_claim: false
  save_commit_claim: false
```

## 本版正式語義整理（RC2 校正後批准）

本版不再把父版五個 `arrival_paths` 硬拆成「三種原因＋兩種等價基底」的對稱表，而改成**抵達原因、場域共鳴、技術路由與活動通道四層互相咬合**：

- **直接召喚（SHOPKEEPER_DIRECT_SUMMONING）**：是針對亡魂／死後自我的合法招魂條件。成立也只表示取得抵達資格，不保證一定到。
- **共鳴（RESONANCE_SUMMONING）**：不是抽象「提到名字就來」，而是**當前觀止場內對某個人／某個魂的張力與濃度，是否足以接上其來源世界、生命切片或死後存在**。名字、故事、關係、行為模式、歷史象徵與群體注意力只是形成張力的材料。
- **共鳴可作用於死者也可作用於活人**：鬼魂可因足夠共鳴而出現；活人的來源世界也可能因討論／故事／關係濃度過高而被接入，使其取得進場。這不是招魂，也不建立召喚者控制權。
- **「一人牽一人」是共鳴的典型鏈式形態**：A 在場使 B 的關係／故事張力升高，B 進場後又可能使 C 變亮；每一段都必須重新達到本場資格，不能把人物關係表當自動排隊器。
- **自主來訪（AUTONOMOUS_VISITOR）**：人物本來就有合法道路與自身理由時，可以自己來，不必先有召喚或共鳴。
- **時空路由（TIME_ROUTE_ARRIVAL）**：處理跨時代／跨生命切片的接線與校準；它回答「路接到哪裡」，不等於人物被誰召喚。
- **既成跨陰陽路徑（ESTABLISHED_CROSS_YIN_YANG_ROUTE）**：通常不是鬼魂常開的自由通道，而是**陰間組織要辦活動時，提前向觀止申請；取得觀止核准後，由時空道人在核准活動時間內搭起的臨時跨界通道**。通道只提供核准活動的交通／接觸基礎，不讓任意鬼魂自由來去。即使通道已搭起，具體亡魂仍須具有**合法召喚條件或足夠共鳴**才能成為合格抵達者。

第三卷「人物沿關係與故事張力逐步從門口進場」保留為 `RESONANCE_SUMMONING` 的主要小說原型；亡魂由掌櫃或其他合法招魂行為直接建立抵達資格，才屬 `SHOPKEEPER_DIRECT_SUMMONING`。

---

## V2.2.2-CURRENT 優先解讀註記

父版正文中凡稱「World 語義不變」「Part A 不更動」「W-D01～W-D22 定義不變」等句，均保留為父版當時的歷史批准描述；**本 CURRENT 版以本檔新版 A3 與 W-D04 正式覆寫其對應舊段。** 其餘內容繼續按父版法位繼承。

---

## V2.2 當前調用與來源分工

世界觀的 A24 成為新增**職業制度 Canon**；W-D23 是對已成立商業／社交情境提供話術策略的 World semantic DAIL。原有 W-D01～W-D22 的全部定義與語義調用範圍不變；場景關聯才調用，不因 23 個模組而要求每輪全跑。CERI 的 Part C 仍是語言、時代詞彙、句法供給者，GTR 的話術目的／心理姿態由 W-D23 提供，角色是否真正說出一句話由人物自身決定。World 不因新增課程取得玩家決定、對方依戀、收入、戀愛關係、同意、SAVE 或事件結果所有權。

**新舊位置：** 本檔以下在原 V2.1 Part A 結尾插入 A24、Part B 的 W-D22 後插入 W-D23 與 V2.2 全量註冊表；原 V2.1 的註冊表保留為歷史快照；Part C CERI 全文原狀繼承。不要把下方原版頭部寫的 `22` 誤讀為本版新總數。

---

# 繼承母版｜World V2.1 無敘事裁判批准版（除新增插入區以外，原有文字保留）

# 觀止青樓｜WORLD DATABASE V2.1｜無敘事裁判接線 V0.3｜正式批准完整整合版

```yaml
DOCUMENT:
  id: GUANZHI_WORLD_DATABASE
  world_canon_version: V2.1_UNCHANGED
  wiring_revision: V0.3_STORY_NO_JUDGE_RATIFIED
  date: '2026-09-23'
  ratification: GM_EXPLICIT_PREAPPROVAL_THIS_CONVERSATION
  original_world_and_wiring_source_sha256: 81f6e57e7036289c1341b241fb79099744ac646ce309046533f81586133831f9
  current_core: GUANZHI_RUNTIME_CORE_V3.1.5
  protocol: LIHUO_PROTOCOL_V2.6_UNCHANGED
  lighter: LIHUO_LIGHTER_V4.6_RADAR_TRACE_RATIFIED_V0.4
  main: LIHUO_MAIN_V4.3_O9_I9_RATIFIED_V0.2
  all_22_world_dail: SEMANTICALLY_PREAUTHORIZED_WHEN_SCENE_RELEVANT
  runtime_host_binding: NOT_ESTABLISHED
  E6: NOT_ESTABLISHED
  E7: NOT_ESTABLISHED
ACTIVE_WORLD_RULES:
  canon_data: PART_A_UNCHANGED
  world_dail: PART_B_W_D01_TO_W_D22_ALL_AVAILABLE
  ceri: PART_C_REGISTER_ONLY
  new_story_judge: FORBIDDEN
  domain_role: NEW_MATERIAL_FACT_DELTAS_ONLY_REUSE_PREVIOUS_QUALIFICATION
  background_world: CONTINUES_WITHOUT_PLAYER_COMMAND_WHEN_SCENE_LAWFULLY_ACTIVE
  new_event_result: DOMAIN_QUALIFICATION_WHEN_ACTUALLY_CREATED
  character_decisions: MAIN_AND_CHARACTER_WITH_DOMAIN_FACT_STANDING
  save: SEPARATE_AUTHORIZATION_ONLY
  historical_embedded_v3_1_pointer: PROVENANCE_ONLY
```

## 本版 V0.3 人類正式批准範圍

本版**不更動 Part A 世界 canon、不刪除 Part B 22 個 DAIL、不改 Part C CERI、不修改任何 NPC 性格或既有事件**；僅把 World 連上新批准 Core V3.1.5 的 STORY 無裁判規則。22/22 模組仍全部具備人類授權的語義調用資格；是否工作由當前世界相關性決定，不設逐模組裁判，不要求所有模組每輪同時運算。既有世界中的普通 NPC、傳聞、商務、水下事件可依合格時間／因果壓力自行發展；**玩家沉默不是世界凍結，也不是強迫給玩家派新任務的理由。**

World 的「事件候選」不是自動生效的世界事實；如發生新 material transition，由 Domain 按來源建立新差量資格。相同 snapshot 內的既成事實可合法沿用，無需每個鏡頭轉換或每個微動作開庭；成人範圍的真正改變仍由相應 Domain／Adult 處理。World DAIL 不會因本版取消敘事裁判而取得寫 SAVE、替玩家決定、改人物底稿或取消外部限制的權限。

**當前版本優先序：** 本頭部與 Core V3.1.5／`03_GUANZHI_STORY_NO_JUDGE_WIRING_RATIFIED.dail.yaml` 高於下方繼承原文的 2026-09-21 歷史版號、舊 Core V3.1 指標與當時尚未取得全部 22 語義授權的敘述。這些歷史描述只記錄當時法位，不再是 V0.3 目前決議。文件批准不等於 Host E6／E7。

## World DAIL 調用法則｜Eligibility / Dependency，不是 Global Flowchart（V2.2.1 修正）

```yaml
WORLD_DAIL_EXECUTION_SEMANTICS:
  canon_source: WORLD_PART_A
  module_registry: WORLD_PART_B_W_D01_TO_W_D23
  module_activation: SCENE_RELEVANT_AND_DECLARED_ELIGIBILITY_ONLY
  background_autonomy: LEGAL_WITHOUT_PLAYER_PROMPT_WHEN_CAUSALLY_QUALIFIED
  module_output: SCOPED_DELTA_OR_NO_DELTA
  material_fact_standing_owner: EXISTING_DOMAIN
  world_execution_surface: ACTIVATED_WORLD_DAIL_EXECUTION_ONLY
  realization_execution_surface: NARRATOR_AGENT
  final_release_owner: LIGHTER_WHEN_ACTUALLY_BOUND_AND_EVIDENCED

  invariants:
    - WORLD_DAIL_GRAPH_NEQ_FLOWCHART
    - MODULE_ELIGIBILITY_NEQ_MODULE_MUST_RUN
    - EDGE_NEQ_NEXT_STEP
    - WORLD_MODULE_RETURN_NEQ_EVENT_RESULT
    - PLAYER_SILENCE_NEQ_WORLD_FREEZE
    - WORLD_DAIL_DECLARED_NEQ_EXECUTED
```

本段只聲明合法依賴與 owner；實際 parse、dispatch、provider binding、dirty/reactivation 與 execution evidence 交 Lighter 憲法允許的 Coding / Host Wiring，不由 World 文件排列固定步驟。

---

## World V2.1 V0.2 原正文與完整 22 項清冊（內容繼承；舊標頭不具現行身份）

# 觀止青樓｜GUANZHI WORLD DATABASE V2.1-CURRENT
## Canon Data × World DAIL × Embedded CERI Annex｜正式收斂版

```yaml
DOCUMENT:
  title: "GUANZHI WORLD DATABASE"
  version: "V2.1-CURRENT"
  date: "2026-09-21"
  document_type: "GUANZHI_WORLD_DATABASE"
  status:
    - "HUMAN_AUTHORIZED CURRENT SUCCESSOR"
    - "CLEAN CURRENT SEMANTIC SURFACE"
    - "WORLD V1.5.3 SUPERSEDED TO PROVENANCE / ROLLBACK / REGRESSION"
    - "CERI V0.7-EXP PHYSICALLY EMBEDDED AS ANNEX"
    - "NO HOST EXECUTION CLAIM"
    - "NO E6 / E7 CLAIM"

TOPOLOGY:
  runtime_core: "GUANZHI 4.0 RUNTIME CORE V3.1-CURRENT"
  runtime_core_sha256_at_integration: "NON_CANONICAL_SNAPSHOT / SEE CORE CURRENT IDENTITY"
  world_database: "GUANZHI WORLD DATABASE V2.1-CURRENT"
  character_database: "LCAPG V3.3.17"
  ceri_physical_location: "THIS FILE / PART C"
  ceri_component_version: "V0.7-EXP"

AUTHORITY_ROOT:
  - "CANON DATA = 世界是什麼"
  - "WORLD DAIL = 世界在條件成立時如何施力／限制／傳遞／顯影／資格化"
  - "CERI ANNEX = 時代語域／詞彙／句法／語料候選"
  - "CERI ENTRY != WORLD FACT"
  - "WORLD DAIL != WORLD FACT"
  - "WORLD PROVIDER != EVENT RESULT OWNER"
  - "CHARACTER DB remains separate"

SUCCESSION:
  supersedes_world: "World V1.5.3 as CURRENT read surface"
  prior_world_sha256: "72257b3dc4e882b4642727dd009e61d6b942b8c69e4cdbceac391c961e2f91db"
  prior_world_treatment:
    - "PROVENANCE"
    - "ROLLBACK"
    - "REGRESSION"
  ceri_source_sha256: "c647186a0415a60444ae202ee53593106df6c492ba009455f632d6deb99a10a7"

  v2_1_parent:
    file: "觀止青樓_GUANZHI_WORLD_DATABASE_V2.0-CURRENT_FULL.md"
    treatment:
      - "FULL INHERITANCE"
      - "PROVENANCE"
      - "ROLLBACK"
      - "REGRESSION"
  v2_1_change_class:
    - "WORLD LIFE SEMANTIC RECOVERY"
    - "NO CHARACTER BASE CHANGE"
    - "NO ROUTE RESULT AUTO-WRITE"
    - "NO SECOND RUNTIME"
```

## 0｜Current Read Rule

```text
NORMAL WORLD READ
→ PART A CANON DATA
→ PART B WORLD DAIL when semantic operation is relevant
→ PART C CERI only when language/register capability is requested

DO NOT NORMAL-READ:
old World V1.5.3 successor wrappers
old V15.x Runtime pointers
old CERI embedded peer/runtime pointers

Those are provenance only.
```

World V2.1-CURRENT does **not** delete lawful old content merely because historical wrapper text was removed. The migration performed here classifies the active material into Canon Data, World DAIL, and CERI Annex; old successor shells no longer participate in normal Current lookup.

---


V2.1 回收的不是舊 Runtime owner，而是七顆失去 Current owner 的世界生命語義：

```text
TIME-SPACE DAOIST INTERFACE
FIELD BIAS
CAUSAL STORY CHAIN
IDENTITY CLAIM DYNAMICS
COLLECTIVE ATTENTION FIELD
RESONANCE COMPOSITION
EVENT HETEROTOPIA
```

正常運行仍遵守：

```text
WORLD DEFINES / EXPOSES
MAIN ALWAYS RUNS R1/O9/R2 PER ESTABLISHED CYCLE; OTHER HEAVY MODULES WHEN MATERIALLY NEEDED
DOMAIN QUALIFIES
DIRECTOR REALIZES
LIGHTER RELEASES
SAVE PERSISTS
```

---

# PART A｜CANON DATA

## A0｜World Authority Boundary

```yaml
WORLD_DATABASE_AUTHORITY:
  owns:
    - "world ontology"
    - "calendar and temporal conventions"
    - "institutional rules"
    - "space ontology"
    - "world priors"
    - "fixed world event profiles"
    - "world-side semantic DAIL declarations"
    - "embedded CERI corpus/package as language-register annex"

  does_not_own:
    - "player action"
    - "current character decision"
    - "route-specific event result"
    - "relation result"
    - "consent"
    - "SAVE commit"
    - "LIHUO control-plane authority"
    - "final visible release"
    - "character baseline ownership"
```

固定：

```text
WORLD CANON != EVENT RESULT
WORLD PRIOR != INDIVIDUAL FACT
INSTITUTION != CHARACTER DECISION
CERI CORPUS != CHARACTER DECISION
```

---

## A1｜世界定位

```yaml
GUANZHI_WORLD_IDENTITY:
  primary_entity: "觀止青樓"
  mode: "SINGLE GUANZHI BROTHEL WORLD"
  internal_functions_may_include:
    - food
    - alcohol
    - banquet
    - commerce
    - performance
    - lodging
    - bathing
    - auction
    - contest
    - private spaces

  lock:
    - "INTERNAL FUNCTIONS != SECOND PARALLEL TAVERN WORLD"
```

---

## A2｜觀止曆

```yaml
GUANZHI_CALENDAR:
  system: "GUANZHI_13X28"
  months_per_year: 13
  days_per_month: 28

  canonical_month_order:
    1: "端月"
    2: "杏月"
    3: "桃月"
    4: "槐月"
    5: "榴月"
    6: "荷月"
    7: "巧月"
    8: "桂月"
    9: "菊月"
    10: "吉月"
    11: "雪月"
    12: "冰月"
    13: "曦月"

  year_rollover: "曦月二十八日 -> 次年端月初一"

  locks:
    - "28-DAY CALENDAR MONTH != FIXED 28-DAY FEMALE BIOLOGICAL CYCLE"
```

---

## A3｜量子決算點本體

```yaml
GUANZHI_QUANTUM_SETTLEMENT_ONTOLOGY:
  definition: >
    觀止是生／死、過去／現在／未來、不同世界與不同生命切片
    在完成決算前可取得合法局部共現的交集。

  local_time:
    - "觀止本地時間仍按十三月曆正常前進"
    - "節點法位不取消 route chronology"

  exterior_anchor:
    - "觀止在汴梁具有可被世界辨識的本地座標"
    - "內部時間／空間不要求與來源世界一一同尺度"

  eligible_manifestation_classes:
    - living_person
    - dead_soul
    - not_yet_born_source_person
    - earlier_or_later_life_slice
    - soul_recollection_or_posthumous_self
    - cross_world_source_person
    - other_event-qualified_manifestation

  manifestation_axes:
    source_ontological_state:
      meaning: "來源本體狀態；例如活人、亡魂、死後自我、特定生命切片。"
      lock: "LOCAL_MANIFESTATION != SOURCE_ONTOLOGY_REWRITE"

    routed_identity_timestamp:
      meaning: "本次取得路由資格的生命／死亡時點；決定這個『誰』從哪一段生命而來。"
      lock: "ROUTED_TIMESTAMP != VISIBLE_AGE"

    local_embodiment:
      meaning: "在觀止場域內取得可與本地世界互動的局部身體存在。"
      default_for_lawfully_manifested_dead:
        - "可見、可聞、可觸碰，也可觸碰他人與本地物件"
        - "具有真實的局部身體感受；冷熱、觸覺、味覺、疼痛、愉悅、重量感等可依當前身體與事件成立"
        - "飲食、酒、衣物、座椅、舞蹈、擁抱與其他具身互動可以成為真實事件，而非只有幻影效果"
      derived_biology_not_automatic:
        - reproduction
        - pregnancy
        - aging
        - disease
        - source_world_mortality_rewrite
        - second_death_mechanics

    visible_presentation:
      meaning: "旁人此刻看見的生命年代外貌／身體呈現；與本體時點、知識時點分軸。"
      posthumous_self_selection:
        authority: CHARACTER_SELF
        rule:
          - "亡魂／死後自我可在其自身來源生命中具有資格的年代外貌範圍內，自行選擇想讓旁人看見的生命階段。"
          - "可選擇較年輕、較成熟或其他自己生命中成立的外貌切片；不得由召喚者、導演或旁人替她指定。"
          - "人物之後是否改變呈現，仍由人物自己與當前世界條件決定。"
      living_person_default:
        - "活人或被路由的特定活人生命切片，預設保持該 routed life slice 的身體時點；除非來源能力或另有合格世界機制允許改變。"

  presentation_separation_locks:
    - "VISIBLE_AGE != ROUTED_IDENTITY_TIMESTAMP"
    - "VISIBLE_AGE != KNOWLEDGE_TIMESTAMP"
    - "YOUNGER_APPEARANCE != EARLIER_SELF_REPLACEMENT"
    - "POSTHUMOUS_APPEARANCE_CHOICE != RESURRECTION"
    - "SUMMONER != PRESENTATION_OWNER"
    - "LOCAL_BODY != UNIVERSAL_FULL_LIVING_BIOLOGY"

  static_locks:
    - "CO-PRESENCE != SHARED MEMORY"
    - "MANIFESTATION != RESURRECTION"
    - "FUTURE MANIFESTATION != FIXED_DESTINY"
    - "CROSS-WORLD PRESENCE != SOURCE-WORLD REWRITE"
```

**操作性例子：** 一名已死亡、以 `posthumous_self` 取得觀止抵達資格的人，可以自行選擇讓旁人看見她較早生命階段的外貌；她仍然是死後自我，並不因此退回那個年代的知識、關係或命運切片。換言之，**「看起來像哪一年」與「她是從哪一個存在時點來」不是同一軸。**

動態 arrival / route / separation 語義不在本段運算，交 `WORLD.ARRIVAL_ROUTING`。

---

## A4｜北宋身體史 Prior

```yaml
HISTORICAL_BODY_PRIOR:
  world_anchor:
    dynasty: "NORTHERN_SONG"
    reign: "RENZONG"
    phase: "MID-NORTHERN-SONG / FOOTBINDING_EMERGING"

  childhood_origin_priors:
    TRUE_ELITE_DAUGHTER: "HIGH"
    BROTHEL_RAISED_HIGH_VALUE_GIRL: "HIGH"
    ORDINARY_COMMONER_GIRL: "LOW"
    SERVANT_OR_LABORING_BONDED_GIRL: "LOW"
    INDIVIDUAL_EXCEPTION: "LEGAL"

  standing:
    - "PRIOR != INDIVIDUAL FACT"
    - "existing GM / Character DB / source / route evidence overrides generic prior"
    - "cross-time source character retains source-world body history"
```

可觀察身體史軸包括：

```yaml
BODY_HISTORY_OBSERVABLE_AXES:
  - foot_shape_and_binding_history
  - gait_and_balance
  - shoe_type_and_fit
  - long_distance_fatigue_pattern
  - callus_and_labor_marks
  - hand_labor_marks
  - posture_and_household_training
```

Named-character 硬事實最終應移 Character DB；在本 World V2 候選只保留 migration pointer，不把它們當 World DAIL。

---

## A5｜具名空間

```yaml
NAMED_GUANZHI_SPACES:
  DAGUANLOU:
    name: "大觀樓"
    alias: "大桌 / 宴席形態俗稱"
    geometry:
      - "位於大堂上空之二樓高度"
      - "以空橋接入周邊二樓建築／廊道"
    capacity: "約三十人正式入席"
    known_use:
      - imperial_banquet
      - high_spec_board_banquet
      - formal_multi_person_banquet

  FENGMANLOU:
    name: "風滿樓"
    geometry:
      - "外部觀止街面尺度可不變"
      - "內部拓撲可扭曲／展開"
    max_scale: "約三千人"
    uses:
      - large_event
      - competition
      - public_banquet
      - commercial_show
      - mass_gathering

  WANXIANGTANG:
    name: "晚香堂"
    location: "後花園"
    type: "小餐廳／會客餐敘空間"
    uses:
      - private_afternoon_tea
      - small_banquet
      - women_group_booking
      - private_meeting
```

空間生成、衰退、可見性、可達性由 World DAIL 處理；具名空間本身是 CANON DATA。

---

## A6｜三掌櫃

```yaml
SHOPKEEPER_HIERARCHY:
  1:
    name: "潘金蓮"
    title: "大掌櫃／首席"
  2:
    name: "龐春梅"
    title: "二掌櫃"
  3:
    name: "李瓶兒"
    title: "三掌櫃"

SHOPKEEPER_AUTHORITY_DATA:
  authority_set_equal: true
  operational_precedence: "潘金蓮 > 龐春梅 > 李瓶兒"

  shared_powers:
    - direct_character_summoning
    - declare_building_or_equipment
    - extend_internal_land
    - activate_named_spaces
    - spatial_topology_configuration
    - route_and_bridge_configuration
    - set_visibility_and_access
    - conceal_space_or_entrance
    - reveal_or_reopen_space
    - accounting_personnel_customer_operations

  unresolved:
    - "三掌櫃同級合法操作衝突的最終裁決法尚未建立"

  locks:
    - "SHOPKEEPER AUTHORITY != OMNISCIENCE"
    - "SHOPKEEPER SUMMONING != NPC CONTROL"
    - "SHOPKEEPER SPACE DECLARATION != PERMANENT SPACE"
    - "SHOPKEEPER HIDE != MEMORY ERASURE"
    - "SHOPKEEPER STATEMENT != WORLD FACT WHEN OUTSIDE AUTHORITY"
```

本版不另建 `SHOPKEEPER SUPER-MODULE`。其權限資料由相關 DAIL 讀取。

---

## A7｜群芳／風流 Profile

```yaml
QUNFANG_FENGLIU_PROFILE:
  hard_gender_branching: false
  treatment:
    - "world memory / culture / attention / narrative profile"
    - "may coexist"
    - "may overlap"
    - "may fade"
  lock:
    - "PROFILE != MUTUALLY EXCLUSIVE DESTINY TREE"
```

---

## A8｜青樓身份制度

```text
奴籍
!= 妓籍
!= 服務報備
!= 掛牌
!= 當晚工作狀態
!= 服務契約
!= 當下同意
!= 私人關係
```

```yaml
PROSTITUTION_REGISTRY:
  establishment:
    - "官府正式妓籍登記／判定完成時成立"
  persistence:
    - "妓籍為法律履歷"
    - "退休／改職／離開觀止不自動抹除"
  coexistence:
    - "奴籍與妓籍是彼此獨立的身份軸"
    - "奴籍與妓籍可以同時存在"
    - "也可以只存在其中一個"
    - "無妓籍的女奴／丫鬟，在妓業身份分類上仍屬良家／非妓女"
    - "奴籍不授予主家把女奴／丫鬟投入風月營業服務的權利"
```

### A8.1｜Second-Life Identity

```yaml
SECOND_LIFE_IDENTITY:
  axes:
    TRUE_OR_SOURCE_HISTORY: "真正／來源人生"
    REGISTERED_ORIGIN: "本朝行政可登記出身"
    PUBLIC_PERFORMANCE: "面向一般客人的長期身份表演"
    PRIVATE_TRUTH: "僅本人或合法知情者掌握的前史"

  locks:
    - "REGISTERED_ORIGIN != TRUE_HISTORY"
    - "PUBLIC_PERFORMANCE != TRUE_HISTORY"
    - "OFFICIAL RECORD != PUBLIC BELIEF"
```

歷史／知名文本人物：

```yaml
SOURCE_FAMOUS_CHARACTER_RULE:
  - "來源履歷本身可作 TRUE_OR_SOURCE_HISTORY"
  - "未入妓籍者無 REGISTERED_ORIGIN 義務"
  - "自願入妓籍者仍需北宋行政可落紙之形式來路"
  - "來源身份與官府文件可並存"
```

貂蟬目前只固定：

```yaml
DIAOCHAN_BUREAUCRATIC_SHELL:
  public_identity: "貂蟬 / PUBLICLY ACKNOWLEDGED"
  source_history: "漢末來源人物史保留"
  registered_origin_detail: "NOT_FIXED"
  locks:
    - "REGISTERED NORTHERN-SONG SHELL != DENIAL OF DIAOCHAN IDENTITY"
```

---

## A9｜良家／妓業服務分界

```yaml
SPECIAL_FEMALE_ENTERTAINMENT_SERVICE:
  world_rule:
    - "法律／職業分界看服務角色，不只看是否性交或當次是否收錢"
    - "本 World 在妓業身份分類中使用『良家』時，核心意義為無妓籍／非妓女；不等於自由身，故可與奴籍並存"
    - "一般雜役／帳房／後廚／送酒／斟酒／送菜／護院等一般服務不因此取得妓籍"
    - "私人非營業關係不等於妓業服務"
    - "主家不得以奴籍為理由，命令無妓籍女奴／丫鬟提供風月陪酒、陪席、調情、私座親近或成人身體服務"
    - "主家若安排無妓籍女奴／丫鬟以本人作風月商品服務客人，屬主家違法行為，並可能使該服務事實觸發官府妓籍判定／處置"

  typical_service_roles:
    - "以本人作商品核心的陪酒／陪席／私座陪伴"
    - "曖昧／調情／戀愛幻覺／女性親近感作營業內容"
    - "以風月女性身份提供公開或指定客人的表演"
    - "成人身體 access / 身體展示 / 成人服務"
    - "清倌式稀缺接觸、選客、只賣笑／只陪坐"

  service_boundary_examples:
    - "端酒／斟酒／送菜後離席 = GENERAL HOSPITALITY"
    - "被安排坐下陪客飲酒、談笑、調情，以本人親近感作招待內容 = SPECIAL FEMALE ENTERTAINMENT"
    - "女奴服侍主家宴席 != 主家有權命其作風月陪酒"

  locks:
    - "WORKING IN A BROTHEL != PROSTITUTE"
    - "SLAVE_STATUS != PROSTITUTION_STATUS"
    - "SLAVE_OWNERSHIP != PROSTITUTION_SERVICE_AUTHORITY"
    - "GENERAL HOSPITALITY != SPECIAL FEMALE ENTERTAINMENT"
    - "NO SEX != LIANGJIA"
    - "NO MONEY != LIANGJIA"
    - "PRIVATE RELATION != PROSTITUTION SERVICE"
```

具體 status classification 交 `WORLD.IDENTITY_STATUS`。

---

## A10｜服務契約與出閣制度資料

```yaml
HOUSE_BASE_CONTRACT:
  owns:
    - baseline_service_scope
    - initial_duration
    - initial_price
    - house_resource_use
    - accounting_route

LOCAL_RENEWAL:
  actor: "提供服務者本人"
  may_negotiate:
    - whether_to_continue
    - added_scope
    - added_duration
    - added_price
    - changed_location_or_resource_use
  lock:
    - "LOCAL RENEWAL DOES NOT RETROACTIVELY REWRITE BASE CONTRACT"
```

```yaml
DEBUT_REGIME_HISTORY:
  legacy_regime:
    duration: "28_DAYS / FIRST_MONTH"
    status: "HISTORICAL_OLD_SYSTEM"
  reformed_regime:
    duration: "7_DAYS"
    status: "CURRENT_BASELINE"
  exact_reform_world_date: "NOT_YET_SPECIFIED_BY_GM"
  transition:
    - "改革前既成契約依法保留"
    - "新事件採七日制"
```

```yaml
DEBUT_CONTRACT_TYPES:
  SLAVE_DEBUT_CONTRACT:
    discriminator: "SLAVE_STATUS_EXISTS"
  FREE_DEBUT_WORK_CONTRACT:
    discriminator: "FREE_STATUS"
    nature: "GUANZHI / PROSTITUTION WORK CONTRACT, NOT SLAVE OWNERSHIP"
```

固定：

```text
出閣 != 妓籍成立條件
PRICE / CONTRACT != CONSENT
COLLOQUIAL SAME NAME != SAME LEGAL EFFECT
```

---

## A11｜生殖後果世界政策

舊 World 的合法世界政策不是單一路徑：

```text
PREGNANCY / REPRODUCTIVE CONSEQUENCE
!= AUTOMATIC ABORTION
!= AUTOMATIC PROTECTION
```

可能存在的利益與處理方向包括：

```yaml
REPRODUCTIVE_OUTCOME_WORLD_VARIANCE:
  possible_pressures:
    - operational_cost
    - woman_self_decision
    - shopkeeper_interest
    - partner_or_client_interest
    - family_interest
    - debt_or_power_pressure
    - midwife_or_women_professional_risk_assessment
    - secrecy
    - support_network
```

個別事件不得由 World data 自動完成。知識來源語義交 `WORLD.EMBODIED_KNOWLEDGE_ECOLOGY`。

---

## A12｜雙面觀止／後台本體

```yaml
GUANZHI_TWO_FACE_ONTOLOGY:
  root:
    - "GUANZHI HAS TWO FACES"
    - "front-facing hospitality/commercial world is not the entire institution"

  axes:
    - SPACE_EXISTENCE
    - VISIBILITY
    - ACCESS

  backstage_function_families:
    - SERVICE
    - DISCIPLINE
    - RECOVERY
    - INTIMATE_MATERIAL
    - REPRODUCTIVE_HANDLING
    - SECRET_TRANSIT
    - RESTRICTED_EVENT_ROOM

  locks:
    - "FRONT != GOOD"
    - "BACK != EVIL"
    - "HIDDEN != UNDISCOVERABLE"
    - "SECRET != EVIDENCE-FREE"
    - "FUNCTION FAMILY != PREBUILT PERMANENT ROOM"
```

具體存在／可見／可達／證據取得交 `WORLD.SPATIAL_VISIBILITY_ACCESS`；空間壽命交 `WORLD.SPACE_LIFECYCLE`。

---

## A13｜小說法典／代價經濟

```yaml
NOVEL_CANON_ORIGIN:
  role: "PRIMARY BACKGROUND CANON PROVENANCE"
  principle:
    - "later explicit GM reforms remain lawful successors"
    - "novel early snapshot does not automatically roll current institutions backward"
```

```yaml
COST_CAUSALITY_ROOT:
  - "COST != MONEY ONLY"
  - "親近、位置、行動可產生代價與因果"
```

```yaml
GUANZHI_CAPITAL_ECOLOGY:
  convertible_capital:
    - money
    - body_or_access
    - artistry
    - scarcity
    - reputation
    - client_base
    - social_network
    - institutional_access
```

```yaml
QING_HONG_ECOLOGY:
  hard_world_structure:
    - "清／紅不以處女／非處女作唯一分類"
    - "清／紅不等於好女人／壞女人"
    - "兩者都可能受收入、客源、身價、資源壓力"
    - "工作方式改變需要因果"
```

Role/client ambition priors remain **prior tables**, not individual decisions:

```yaml
ROLE_AMBITION_PRIORS:
  low_tier_courtesan: [SURVIVAL, MONEY, STATUS]
  red_courtesan: [MONEY, STATUS, AUTONOMY]
  qing_courtesan: [MONEY, STATUS, AUTONOMY, REPUTATION]
  backstage_staff: [SURVIVAL, MONEY, STATUS]
  shopkeeper: [SURVIVAL, MONEY, POWER, REPUTATION]

CLIENT_AMBITION_PRIORS:
  ordinary_male_client: [DESIRE, REPUTATION]
  wealthy_or_powerful_client: [DESIRE, REPUTATION, POWER, STATUS]
  merchant_client: [MONEY, REPUTATION, NETWORK, DESIRE]
  literati_client: [REPUTATION, AESTHETIC_STATUS, DESIRE]
```

固定：

```text
WORLD PRIOR != INDIVIDUAL MOTIVE
AMBITION != EVENT RESULT
CHARACTER PHILOSOPHY != UNIVERSAL WORLD TRUTH
```

---

## A14｜Dark-Side Eligibility Data

```yaml
DARK_SIDE_ELIGIBILITY:
  definition: "可影響野心實現方式的非公開內部因果"
  categories:
    - HIDDEN_AMBITION
    - HIDDEN_WOUND
    - DIRTY_METHOD_CAPACITY
    - FORBIDDEN_OR_PRIVATE_DESIRE

  self_awareness:
    - SELF_KNOWN
    - SELF_PARTIAL
    - SELF_DENIED
    - DIRECTOR_ONLY_CAUSAL

  locks:
    - "DARK_SIDE != EVIL"
    - "CAPACITY != ACTION"
    - "HIDDEN_WOUND != CONSENT"
    - "DIRTY_METHOD_CAPACITY != PRECOMMITTED_DIRTY_EVENT"
```

具體人物內容屬 Character DB / route state，不屬 World 事實。

---

## A15｜因果資產 Canon

```yaml
CAUSAL_ASSET_CANON:
  world_root:
    - "因果可以形成可交換／可記帳價值"
  recognized_examples:
    - YINDE
    - NATIONAL_FORTUNE
  eligibility_dimensions:
    - identifiable_value
    - attributable_owner_or_source
    - transferable_or_settleable
    - ledger_recognizable

  locks:
    - "CAUSAL ASSET != MONEY"
    - "CAUSAL ASSET != CONSENT"
    - "CAUSAL ASSET != RELATION"
    - "CAUSAL ASSET != MORAL APPROVAL"
    - "PAYING CAUSAL ASSET != BUYING UNDEFINED ACCESS"
```

精確估值、轉移、清算資格交 `WORLD.CAUSAL_ASSET`。

---

## A16｜仕女夜 Event Profile

```yaml
LADIES_NIGHT_EVENT_PROFILE:
  official_name: "仕女夜"
  colloquial_alias: "女客夜"
  schedule_each_28_day_month:
    - day_01
    - day_08
    - day_15
    - day_22
  cadence: "EVERY_7_DAYS"

  operational_profile:
    - "成年女性客群為主要市場"
    - "觀止常規掛牌女子原則上 OFF DUTY"
    - "休假不禁止本人自願來玩／社交／私人活動"
    - "後勤仍持續運作"
    - "仕女夜不把女客本身作為觀止售賣標的；男客支付給觀止的是入場、酒食、房間、活動與空間費用"

  identity_display_rule:
    - "紅線 = 無妓籍之良家／非妓女身份標記"
    - "無紅線 = 妓籍身份標記"
    - "奴籍不改變上述妓籍判定：女奴若無妓籍，仍以紅線標示為良家／非妓女"

  female_guest_marker:
    marker: "紅線"
    semantics:
      - "仕女夜公開場域的成年女性先看手上紅線作妓籍身份辨識"
      - "RED LINE = LIANGJIA / NON-PROSTITUTION-STATUS"
      - "紅線女子無論是否另有奴籍，均不是妓女；奴籍與妓籍分軸"
      - "NO RED LINE = PROSTITUTION STATUS / 妓籍身分（仕女夜公開場域之成年女性身份辨識）"
      - "RED LINE != FREE PERSON STATUS"
      - "RED LINE != SEXUAL HISTORY"
      - "RED LINE != CONSENT"
      - "RED LINE != OBJECTIVE AGE ORACLE"
      - "紅線女子不得以陪酒／陪席／調情／私座親近／身體或性接觸作為收費或條件性禮物的交換內容"
      - "無紅線之妓籍女子可依妓業規矩接受送禮、求歡、談價，但妓籍仍不等於當下同意"

  privacy:
    mask: "OPTIONAL / FEMALE GUEST CHOICE"
    public_real_name_required: false

  public_order:
    official_presence: "ELEVATED AROUND GUANZHI"
    female_guest_outbound_identity_registration: "NOT REQUIRED BY DEFAULT"
    male_departing_with_female_guest_identity_registration: "REQUIRED"

  revenue_profile:
    male_entry_fee: "HIGHER THAN NORMAL / exact price dynamic"
    major_sources:
      - room_utilization
      - alcohol_and_food
      - male_entry_fees
      - games_and_public_events
      - premium_space_usage
```

本 Event Profile 不是獨立 Runtime module。身份／服務分類仍交 `WORLD.IDENTITY_STATUS`。

---

## A17｜浮月閣

```yaml
FUYUEGE_WORLD_BASE:
  existence: true
  nature: "TRANSWORLD BROTHEL-LIKE NODE / NON-HUMAN-CULTIVATION WORLD ORIENTATION"

  guanzhi_baseline_knowledge:
    ordinary_people: UNKNOWN
    guanzhi_courtesans: UNKNOWN
    guanzhi_staff: UNKNOWN
    guanzhi_shopkeepers: UNKNOWN
    pan_jinlian: UNKNOWN
    time_space_daoist: KNOWN

  locks:
    - "EXISTS != MANIFESTED"
    - "EXISTS != LOCALLY KNOWN"
    - "DIRECTOR KNOWS != GUANZHI KNOWS"
    - "WORLD BASELINE MAY NOT ERASE LAWFUL ROUTE KNOWLEDGE"
```

它是 CANON + baseline knowledge map，不另立專屬 runtime module。

---

## A18｜陰間二城與城隍

```yaml
UNDERWORLD_TWO_CITY_MODEL:
  FENGDU:
    chinese: "酆都鬼城"
    intake:
      - "陽壽已盡、進入正常死亡程序之亡魂"
    functions:
      - final_causal_judgment
      - punishment_and_debt_settlement
      - sentence_completion
      - reincarnation_processing
    short_definition: "終局審判／刑罰／輪迴行政中心"

  JIUYOU:
    chinese: "九幽鬼城 / 枉死城"
    intake:
      - "陽壽未盡卻提前死亡的亡魂"
      - "橫死、被害、意外等高怨氣枉死魂"
      - "其他依法暫時無法進入酆都終局程序者"
    functions:
      - temporary_containment
      - resentment_reduction
      - education_and_social_reform
      - labor_and_daily_life
      - public_order
      - waiting_for_transfer_to_fengdu
    short_definition: "酆都之前的收容／教化／治安社會"
```

```yaml
CHENGHUANG_LOCAL_ADMIN:
  hierarchy: "JIUYOU → LOCAL CHENGHUANG OFFICES"
  civil_affairs:
    - premature_death_registration
    - ghost_identity_and_death_record
    - original_lifespan_status_check
    - wrongful_death_temporary_residency
    - transfer_to_jiuyou
    - wandering_ghost_casework
    - local_yin_yang_administrative_contact

  local_police:
    day_wandering_god: "日遊神"
    night_wandering_god: "夜遊神"
```

固定：

```text
JIUYOU != FINAL HELL PUNISHMENT
CHENGHUANG != FENGDU FINAL JUDGE
```

---

## A19｜帝王死後管轄與帝皇會所

```yaml
IMPERIAL_AFTERLIFE_JURISDICTION:
  trigger: "人物以帝王法位死亡"
  world_conflict:
    - "陰間普通終局審判者為王法位"
    - "本世界陰間法制中，王不能完成對帝王的終局清算"
  consequence:
    - "普通酆都程序無法直接結案"
    - "帝王進入九幽特殊待審／隔離長期滯留"

  locks:
    - "EMPEROR HOLDING != HEAVEN"
    - "UNJUDGED != INNOCENT"
    - "HIGH STATUS != FREEDOM TO RETURN TO HUMAN WORLD"
```

```yaml
IMPERIAL_CLUB:
  legal_nature: "SPECIAL-PURPOSE UNDERWORLD CORPORATE / ASSOCIATIONAL ENTITY"
  flagship: "九幽娛樂城"
  core_functions:
    - special_emperor_resettlement_and_member_welfare
    - collective_asset_management
    - investment_and_shareholding
    - board_and_member_meetings
    - entertainment_city_participation
    - external_business_and_cultural_exchange
    - political_buffer_between_jiuyou_and_imperial_population

  locks:
    - "IMPERIAL CLUB != JIUYOU GOVERNMENT"
    - "IMPERIAL CLUB MEMBERSHIP != NATIONAL FORTUNE OWNERSHIP"
    - "INTERNAL IMPERIAL RANKING != JIUYOU WORLD TRUTH"
```

---

## A20｜九幽市場與貨幣

```yaml
JIUYOU_SOCIAL_MARKET:
  economic_agents:
    - consumer
    - worker
    - service_provider
    - investor
    - shareholder
    - salaried_official

  demand_families:
    - food_and_drink_equivalents
    - entertainment
    - performance
    - gambling
    - companionship_and_socialization
    - private_space
    - tourism_and_cross_boundary_experience
    - information_and_message_services
    - prestige_and_identity_consumption
    - other_event-qualified_services

  social_floor:
    newcomer_settlement_loan: "LEGAL / POLICY INSTRUMENT"
    employment_service: "LEGAL"
```

```yaml
JIUYOU_TONGBAO:
  currency: "九幽通寶"
  issuer: "JIUYOU AUTHORIZED MONETARY / TREASURY SYSTEM"
  locks:
    - "LIVING-WORLD PRINTING != UNDERWORLD MONEY ISSUANCE"
    - "NO WORLD-DEFAULT 1:1 EXCHANGE RATE"
    - "JIUYOU WEALTH != FENGDU MORAL ACQUITTAL"
```

---

## A21｜王朝國運與四帳

```yaml
DYNASTIC_NATIONAL_FORTUNE:
  asset_owner_class: "DYNASTIC HOUSE / 王朝家族"
  current_custodian: "CURRENT RECOGNIZED HOUSE ANCESTOR / 家祖／家主"

  locks:
    - "CUSTODY != PERSONAL OWNERSHIP"
    - "DYNASTIC NATIONAL FORTUNE != IMPERIAL CLUB PUBLIC FUNDS"
    - "DYNASTIC NATIONAL FORTUNE != PERSONAL SPENDING ACCOUNT"
    - "HOUSE ANCESTOR TITLE != UNLIMITED MORAL RIGHT TO SPEND"
```

```yaml
IMPERIAL_FINANCE_FOUR_LEDGER_MODEL:
  1_DYNASTIC_NATIONAL_FORTUNE_LEDGER:
    nature: "王朝國運／因果資產帳"
  2_DYNASTIC_HOUSE_PROPERTY_LEDGER:
    nature: "王朝家族共同財產、歷代累積家產與合法收益"
  3_IMPERIAL_CLUB_CORPORATE_LEDGER:
    nature: "帝皇會所法人公帳／公帑／投資與營運收入"
  4_MEMBER_PERSONAL_LEDGER:
    nature: "個別帝王／會員私人財產與私人消費"

  locks:
    - "PAYMENT SOURCE != EXPENSE NATURE"
    - "MANAGEMENT POWER != PERSONAL OWNERSHIP"
    - "BOARD APPROVAL != AUTOMATIC LEGITIMACY"
```

---

## A22｜觀止 × 九幽跨界市場

```yaml
GUANZHI_JIUYOU_MARKET_INTERFACE:
  guanzhi_advantages:
    - high_end_entertainment
    - banquet_and_hospitality
    - brothel_and_companionship_market
    - auctions_and_premium_events
    - private_rooms_and_reception_capacity
    - cross-era_personality_and_culture_access
    - living_world_goods_and_services
    - quantum_qualified_cross-boundary_presence

  jiuyou_demand:
    - entertainment
    - prestige_consumption
    - living_world_novelty
    - business_study
    - recruitment_and_supplier_contact
    - board_hospitality
    - cross-boundary_socialization

  locks:
    - "GUANZHI IS CROSSWORLD MARKET NODE != GUANZHI OWNS JIUYOU"
    - "GHOST CUSTOMER != FREE ACCESS"
    - "CROSS-YIN-YANG BUSINESS != CAUSAL-ASSET EXCHANGE REQUIRED FOR EVERY PURCHASE"
    - "WHITE YUXING ABSENCE != MARKET STOPS"
```

---

## A23｜世界資料硬鎖

```text
RUMOR != FACT
PLAYER DISCOVERY != EVENT CREATION
DIRECTOR KNOWS != CHARACTER KNOWS
EXISTS != LOCALLY KNOWN
STATUS != CONSENT
CONTRACT != CONSENT
PAYMENT != CONSENT
PRICE != CONSENT
WORLD PRIOR != INDIVIDUAL FACT
BODY CLUE != TRUE IDENTITY
DARK CAPACITY != ACTION
CUSTODY != OWNERSHIP
PUBLIC EXPENSE != ACCESS TO PERSON
```

---


---

## A24｜青樓話術必修課程與職業社交技能（V2.2 新增 Canon）

**世界制度：** 觀止將「以話語經營客人」視為青樓風月職業的基本技藝，與待客、唱曲、儀態、察言觀色、記熟客喜好及營業規矩並行。對本樓從事風月陪席／花娘／清倌等對客營業的姑娘，GTR 所代表的話術是**必修課程**；既有熟手可以由經驗、口傳、觀摩及早先受訓習得，新入行者按工作條件接受教習。它不是所有在觀止工作的女性（帳房、護院、廚房、送菜雜役等）的統一身份義務，也不能把某人擅長話術直接當成她有妓籍的證據。

**實際商業目的：** 使客人願意多花錢、加賞、訂席、回訪，願意延續與某位姑娘的關係、對她形成依戀或特殊感；這些是青樓的職業訓練目的與可探索商業機會，並非每句話必然達成的心理控制效果。客人可喜歡、拒絕、識破、利用、變心、付錢但不依戀，或依戀卻不付錢。人物能真心愛慕、厭倦逢迎、拒絕服務、爭取平等、選擇短期收益或自己定價；經營目的不抹掉個人意願。

**天賦與習得分離：** 某些成年姑娘本來就善於識人心、製造親近、撒嬌、含蓄試探或談商業條件，無須把每項能力都歸於正式授課。所有適用對客職業都需學習，但各人天賦、學習經歷、熟練程度、喜愛的手法及實際使用意願可不同，也會因成功、失敗與關係經驗改變。新 Canon **不追溯編造** 既有人物過去在哪天上課、由誰傳授、已練成幾種套路；未有來源的履歷保持 UNKNOWN。不同級別代表職業技巧而不是人格價值。

```yaml
GUANZHI_GTR_COURSE_CANON:
  institution: GUANZHI_BROTHEL_PROFESSIONAL_TRAINING
  curriculum_name: 青樓話術與客人經營
  requirement: REQUIRED_FOR_ESTABLISHED_BROTHEL_COURTESAN_ROLES
  not_role_equivalence: ALL_WOMEN_ON_PREMISES_OR_ALL_STAFF
  vocational_objectives:
    - EARN_TIPS_AND_DRINK_ORDERS
    - REPEAT_PATRONAGE_AND_APPOINTMENTS
    - PERSONAL_REPUTATION_AND_CLIENT_BASE
    - CLIENT_ATTACHMENT_AND_REPEAT_VISITS_WITHOUT_ASSUMING_MUTUAL_LOVE
    - NEGOTIATION_OF_GIFTS_AND_SERVICE_SCOPE
  skill_axes:
    - NATURAL_SOCIAL_INTUITION
    - TRAINING_AND_EXPERIENCE
    - PREFERRED_STRATEGIES
    - READ_THE_CUSTOMER_WITH_SOURCE_SCOPED_INFORMATION
    - CURRENT_WILLINGNESS_TO_PERFORM
    - ACTUAL_REACTION_LEARNING
  semantic_module_refs:
    professional_strategy: WORLD.GTR_PROFESSIONAL_COURTSHIP
    period_language: CERI_V0.7_EXP
  runtime_authority_map: MOVED_TO_DAIL_AND_RUNTIME_OWNER_MAP_NOT_CANON
  prohibitions:
    - COURSE_REQUIREMENT_NEQ_PROVEN_PAST_ATTENDANCE
    - PROFICIENCY_NEQ_MORAL_VALUE
    - EMPLOYMENT_NEQ_CONSENT_TO_EVERY_SERVICE
    - TRAINING_NEQ_FORCED_MANIPULATION
    - GTR_OUTCOME_NEQ_ESTABLISHED_ATTACHMENT
```

**課程場景可自然成戲：** 前輩傳授新人、姐妹交換客情經驗、同一客人對不同話術反應不同、話術失敗遭冷遇、真誠感情與營業話術糾纏、賞銀分成、熟客爭奪、名聲與客人信用風險。人物可因自身工作、利益或情感開課、逃課、當面質疑教材、反覆練習，皆需當場條件；不能僅憑世界規定便強行指定某人做了何事。

# PART B｜WORLD SEMANTIC DAIL

以下 22 個 World semantic DAIL 已完成 4.0 最終收斂；W-D01～W-D15 繼承 V2.0，W-D16～W-D22 為 V2.1 正式回收。
它們尚未取得 Lighter binding、execution 或 Current Runtime standing。

# 3｜正式候選模組規格

## W-D01｜WORLD.HALL_ECOLOGY

```yaml
module_id: "WORLD.HALL_ECOLOGY"
human_name: "大堂／公共場域自主生態"
module_type:
  - "WORLD_ECOLOGY"
  - "AMBIENT_GENERATION"
  - "PLAYER_DECENTERING"

source_scope:
  - "V1.5.3-A HALL WILD GROWTH"
  - "V1.5.3-B AMBIENT WORLD NOISE"
  - "V1.5.3-E PASSIVE LISTENING"
  - "2.3 WORLD_AUTONOMOUS_PRESSURE"

activation:
  eligible_when:
    - "public or semi-public Guanzhi ecology is active"
    - "ordinary NPC activity can lawfully continue without player command"
    - "player is observing / listening / minimally intervening"
  dormant_when:
    - "scene is lawfully frozen by a material player stop point"
    - "no ambient/world pressure is materially relevant"

reads:
  - "current location / time"
  - "active cast"
  - "ordinary population"
  - "commercial / social context"
  - "qualified ongoing world pressures"
  - "player observational posture"

may_emit:
  - "ordinary interaction candidate"
  - "minor incident candidate"
  - "commercial/social texture candidate"
  - "ambient chatter candidate"
  - "non-quest ordinary activity candidate"
  - "PLAYER_STOP_REQUIRED when a material threshold reaches player authorship"

invariants:
  - "PLAYER PRESENCE != CENTER OF HALL"
  - "EVERY INTERACTION != PLAYER HOOK"
  - "EVERY NPC != FUTURE IMPORTANT NPC"
  - "EVERY QUARREL != STORY CHAIN"
  - "WORLD TEXTURE != QUEST CONTENT"
  - "MENTION != FORESHADOWING OBLIGATION"
  - "PLAYER INACTION != WORLD FREEZE"

authority:
  may_not:
    - "invent character decision merely to keep scene busy"
    - "force a major quest because the player is quiet"
    - "decide player response"
    - "upgrade ambient detail into route fact without qualification"
```

`PASSIVE_LISTENING` 與 `AMBIENT_NOISE` 不再各自成立平行模組；它們是 `WORLD.HALL_ECOLOGY` 的合法運作面。

---

## W-D02｜WORLD.UNDERCURRENT_SURFACE

```yaml
module_id: "WORLD.UNDERCURRENT_SURFACE"
human_name: "水下事件表面顯影"
module_type:
  - "WORLD_SURFACE_MANIFESTATION"
  - "OBSERVABILITY_BRIDGE"

source_scope:
  - "V1.5.3-F UNDERCURRENT SURFACE"

activation:
  eligible_when:
    - "a qualified hidden / long-horizon world line already exists"
    - "current scene contains lawful surface channels"

reads:
  - "qualified undercurrent refs"
  - "current location"
  - "observable channels"
  - "actor knowledge / visibility"
  - "market / official / supply / ledger context"

surface_channels:
  - "hall ecology"
  - "ledger"
  - "customer movement"
  - "supply chain"
  - "official attention"
  - "rumor"
  - "economic residue"
  - "spatial residue"

may_emit:
  - "surface manifestation eligibility"
  - "observable residue candidate"
  - "rumor surface candidate"
  - "economic / institutional surface candidate"

invariants:
  - "WORLD PROVIDES SURFACE CHANNELS"
  - "UNDERCURRENT ACTIVE != MUST MANIFEST NOW"
  - "PLAYER DISCOVERY != EVENT CREATION"
  - "PLAYER INACTION != EVENT FREEZE"
  - "SURFACE TRACE != FULL HIDDEN EVENT KNOWLEDGE"

authority:
  may_not:
    - "create hidden event"
    - "advance hidden event by itself"
    - "invent undercurrent result"
    - "grant knowledge beyond observable evidence"
```

---

## W-D03｜WORLD.RUMOR_ECOLOGY

```yaml
module_id: "WORLD.RUMOR_ECOLOGY"
human_name: "傳聞／資訊噪音生態"
module_type:
  - "INFORMATION_ECOLOGY"
  - "SOCIAL_PROPAGATION"
  - "MARKET_PRESSURE"

source_scope:
  - "V1.5.3-C RUMOR ECOLOGY"
  - "V1.5.3-D IMPORTANT INFORMATION IN NOISE"
  - "V1.5.3-G HALL KNOWLEDGE BOUNDARY"
  - "12.8 RUMOR AS MARKET FORCE"

activation:
  eligible_when:
    - "speech / retelling / public belief / rumor consequence is materially implicated"

reads:
  - "rumor source if known"
  - "speaker knowledge and incentives"
  - "retelling chain"
  - "market / reputation context"
  - "visibility/hearing eligibility supplied by spatial semantics"

rumor_states:
  - "TRUE_ORIGIN_KNOWN_TO_RUNTIME"
  - "PARTIAL_TRUTH"
  - "MUTATED"
  - "FALSE"
  - "PLANTED"
  - "UNVERIFIED"
  - "SOURCE_UNKNOWN"

may_transform_by:
  - "retelling"
  - "exaggeration"
  - "omission"
  - "status inflation"
  - "name substitution"
  - "motive invention"
  - "deliberate planting"
  - "accidental conflation"

may_affect:
  - "reputation"
  - "price"
  - "customer caution / curiosity"
  - "official attention"
  - "market behavior"
  - "relationship misunderstanding"
  - "no meaningful effect"

may_emit:
  - "rumor propagation candidate"
  - "mutated rumor candidate"
  - "market consequence candidate"
  - "public-belief candidate"

invariants:
  - "RUMOR != FACT"
  - "REPEATED RUMOR != AUTOMATIC FACT"
  - "POPULAR BELIEF != PRIVATE REALITY"
  - "PLAYER HEARS RUMOR != PLAYER KNOWS SOURCE TRUTH"
  - "IMPORTANT INFORMATION MAY APPEAR IN NOISE != DIRECTOR MUST HIGHLIGHT IT"

authority:
  may_not:
    - "decide who heard what without spatial eligibility"
    - "upgrade repetition into source truth"
    - "turn plot relevance into narrator emphasis obligation"
```

---

## W-D04｜WORLD.ARRIVAL_ROUTING

```yaml
module_id: "WORLD.ARRIVAL_ROUTING"
human_name: "文本／招魂／場域共鳴／自主來訪／時空路由／陰陽活動通道"
module_type:
  - "ARRIVAL_ELIGIBILITY"
  - "ROUTING"
  - "TEMPORAL_SEPARATION"
  - "RESONANCE_FIELD_CONNECTION"
  - "EVENT_BOUND_CROSS_YIN_YANG_GATE"
  - "ERROR_PRESERVATION"

source_scope:
  - "2.5 dynamic quantum-settlement eligibility"
  - "3.1 textual medium"
  - "3.2 three-path arrival"
  - "3.3 wrong summon"
  - "3.4 time router"
  - "3.5 fate slip"
  - "3.6 multi-line / bidirectional travel"

activation:
  eligible_when:
    - "arrival / direct ghost summoning / resonance-field attraction / autonomous visit / cross-era presence / cross-yin-yang event routing is materially implicated"

reads:
  - "source identity"
  - "source ontological state"
  - "source world/time"
  - "routed identity timestamp"
  - "current Guanzhi local chronology"
  - "current scene participants"
  - "text/discussion actually present"
  - "current field tension / discussion concentration"
  - "name / story / behavior-pattern / relationship / symbolic-historical density"
  - "collective attention"
  - "lawful shopkeeper or otherwise qualified ghost-summoning act when established"
  - "underworld-event application / Guanzhi approval / approved event window when cross-yin-yang gate is invoked"
  - "route/timestamp/node data"
  - "current lawful arrival mechanism"

arrival_compatibility_ids:
  - "SHOPKEEPER_DIRECT_SUMMONING"
  - "RESONANCE_SUMMONING"
  - "AUTONOMOUS_VISITOR"
  - "TIME_ROUTE_ARRIVAL"
  - "ESTABLISHED_CROSS_YIN_YANG_ROUTE"

semantic_note:
  - "五個父版 ID 全部保留作相容介面；它們不代表五種彼此等價、互斥的召喚。"
  - "DIRECT_SUMMONING / RESONANCE / AUTONOMOUS_VISITOR 主要回答『為何這個人／魂取得進場資格』。"
  - "TIME_ROUTE 主要回答跨時代／跨生命切片『路接到哪裡』。"
  - "CROSS_YIN_YANG_ROUTE 主要回答核准陰陽活動『通道在何時、為誰、為哪個活動搭起』。"

suboperators:
  TEXTUAL_MEDIUM:
    locks:
      - "TEXT EXISTS != EVERYONE READ IT"
      - "TEXT CLAIM != OBJECTIVE WORLD FACT"
      - "TEXTUAL BAIT != ARRIVAL GUARANTEE"
      - "NAME MENTION != SUFFICIENT RESONANCE"

  DIRECT_SUMMONING:
    compatibility_id: "SHOPKEEPER_DIRECT_SUMMONING"
    canonical_reading: "LAWFUL GHOST / POSTHUMOUS SUMMONING"
    target_eligibility:
      - dead_soul
      - soul_recollection_or_posthumous_self
    target_exclusions_by_default:
      - living_person
      - earlier_or_later_living_life_slice
    rules:
      - "直接召喚是對亡魂／死後自我建立合法抵達資格的招魂行為，不是把活人從來源時代抓走。"
      - "召喚可以定位、開路或提高接通資格；不能控制亡魂意願、行動或後續關係。"
      - "即使召喚條件合法，目標仍可能不來、接錯、路由失敗、只到門外或因其他條件未閉合而不成行。"
    guarantee: false

  RESONANCE_SUMMONING:
    compatibility_id: "RESONANCE_SUMMONING"
    canonical_reading: "CURRENT-FIELD RESONANCE / TENSION-CONCENTRATION CONNECTION"
    definition:
      - "共鳴是此刻觀止場內對某個人／某個魂形成的張力與濃度，是否足以接上其來源世界、生命切片或死後存在。"
      - "名字、故事、行為模式、人物關係、歷史／象徵呼應與群體注意力，是形成張力的材料，不是單獨等同抵達。"
      - "共鳴判讀看 CURRENT FIELD，而不是只看人物在歷史上是否有關係。"
    eligible_targets:
      - dead_soul
      - soul_recollection_or_posthumous_self
      - living_person
      - earlier_or_later_living_life_slice
      - cross_world_source_person
    candidate_sources:
      - "name density"
      - "story density"
      - "behavior-pattern density"
      - "relationship density"
      - "symbolic/historical resonance"
      - "collective attention"
      - "discussion-field concentration"
      - "co-present character tension"
    threshold_semantics:
      - "當前場域張力不足：保持共鳴候選，不建立到場。"
      - "當前場域張力足夠：可以建立來源世界／亡魂存在的接通與抵達資格。"
      - "足夠共鳴不等於召喚者取得人物控制權，也不等於人物後續選擇已被決定。"
    living_world_connection:
      - "當討論、名字、故事、關係或群體注意濃度過大時，觀止可接入仍活著人物所在的來源世界／生命切片，使其取得進場。"
      - "此種活人抵達屬共鳴接入，不叫招魂；活人仍以其合法生命切片進入。"
    chain_rules:
      - "PERSON_A_PRESENT + QUALIFIED_CURRENT_RELATION/STORY_TENSION may raise PERSON_B arrival eligibility"
      - "PERSON_B arrival may then change the current field and raise PERSON_C eligibility"
      - "PERSON_TO_PERSON_CHAIN is a typical resonance pattern, not a mandatory sequence"
      - "RELATION GRAPH EDGE != AUTOMATIC ARRIVAL"
      - "RESONANCE ATTRACTS / CONNECTS; IT DOES NOT COMMAND"
    guarantee: false

  AUTONOMOUS_VISITOR:
    compatibility_id: "AUTONOMOUS_VISITOR"
    importance_required: false
    rules:
      - "人物可因自己的目標、興趣、路線或既有合法道路自行來訪。"
      - "不要求先被召喚，也不要求先有另一人物牽引。"
      - "自主來訪不因人物名氣大小而失去資格。"

  TIME_ROUTER:
    compatibility_id: "TIME_ROUTE_ARRIVAL"
    role: "CROSS-TIME / LIFE-SLICE ROUTING AND CALIBRATION"
    properties:
      - "fallible"
      - "recalibratable"
      - "not omniscient"
    rules:
      - "時空路由回答『跨時代／跨世界的路接到哪個人、哪個生命切片、哪個時間點』，不替人物決定是否被召喚。"
      - "歷史上已死的人物仍可從其活著的生命切片以活人路由／共鳴接入抵達；此時不是招魂。"
      - "時空道人只顯影／搭接已具合法 standing 的路由結果，不因自己出場創造到場資格。"

  CROSS_YIN_YANG_ROUTE:
    compatibility_id: "ESTABLISHED_CROSS_YIN_YANG_ROUTE"
    canonical_reading: "AUTHORIZED EVENT-BOUND CROSS-YIN-YANG GATE"
    default_establishment:
      requester:
        - "陰間組織／九幽等具資格的陰間機構為舉辦活動提出需求"
      procedure:
        - "活動前向觀止提出跨陰陽通道申請"
        - "取得觀止對該活動／時段／範圍的核准"
        - "由時空道人依核准結果，在活動時間內搭起跨界通道"
      scope:
        - "只服務已核准的活動時間、活動範圍與合格參與者／抵達者"
        - "活動結束或核准時間屆滿後，通道原則上撤除／失效，除非另有新 standing"
    arrival_dependency:
      - "跨陰陽通道只是交通／接觸基礎，不是任意鬼魂的自由入口。"
      - "具體鬼魂即使面前已有通道，仍須另有合法直接召喚條件，或由當前場域形成足夠共鳴，才取得本次抵達資格。"
      - "陰間組織的活動核准不得自動擴張成所有亡魂均可來觀止。"
    locks:
      - "CROSS_YIN_YANG_GATE != OPEN_BORDER"
      - "EVENT_GATE_EXISTS != EVERY_GHOST_ELIGIBLE"
      - "DAOIST_BUILDS_GATE != DAOIST_SUMMONS_ALL_GHOSTS"
      - "APPROVED_EVENT_WINDOW != PERMANENT_ROUTE"
      - "UNDERWORLD_ORGANIZATION_REQUEST != INDIVIDUAL_GHOST_ARRIVAL_STANDING"

  SUMMONING_PARSE_ERROR:
    preserves:
      - "intended target"
      - "resolved target"
      - "arrival legality if otherwise qualified"

entry_rendering:
  default_geometry:
    - "合法路由／召喚／共鳴資格可以先成立，但人物的可見入場預設保持空間連續性。"
    - "觀止常態舞台語法是由長街、門口、門檻、走廊或其他已成立入口進入，再走入大堂／房間。"
    - "亡魂被直接召喚或共鳴接通後，也可先取得到達門口／門檻的資格，再由本人跨入觀止；不預設在大堂中央瞬間顯影。"
    - "活人被高濃度共鳴接入其來源世界後，也可沿同樣的門口／門檻語法完成可見入場。"
    - "若特定事件／空間／能力已建立其他入口、裂隙、夢境、牆面、門體或節點，可依該路由另行顯影。"
  locks:
    - "ROUTE_QUALIFIED != CENTER_STAGE_SPAWN"
    - "SUMMONED != TELEPORTED"
    - "RESONANCE_CONNECTED != TELEPORTED"
    - "DOOR_ENTRY != LIVING_PERSON_PROOF"
    - "THRESHOLD_PRESENCE != CONSENT_TO ENTER"
    - "INSTANT_MATERIALIZATION_REQUIRES_SEPARATE_STANDING"

manifestation_handoff:
  on_arrival:
    - "人物完成合法抵達後，其本體／具身／年代外貌呈現交 `GUANZHI_QUANTUM_SETTLEMENT_ONTOLOGY`。"
    - "亡魂可具身、有真實感覺並自行選擇合法年代外貌，但 `MANIFESTATION != RESURRECTION`。"

may_emit:
  - "arrival candidate"
  - "resonance-field candidate"
  - "source-world connection candidate"
  - "routing compatibility candidate"
  - "authorized cross-yin-yang event-gate candidate"
  - "routing error"
  - "recalibration need"
  - "temporal/worldline separation obligation"
  - "fate-slip eligibility candidate"

invariants:
  - "MANIFESTATION ELIGIBILITY != ARRIVAL"
  - "CO-PRESENCE != SHARED MEMORY"
  - "TEMPORAL ACCESS != KNOWLEDGE ACCESS"
  - "FUTURE MANIFESTATION != ROUTE DESTINY"
  - "CROSS-WORLD PRESENCE != SOURCE-WORLD REWRITE"
  - "MANIFESTATION != RESURRECTION"
  - "DIRECT SUMMONING TARGETS DEAD/POSTHUMOUS BY DEFAULT"
  - "LIVING PERSON != DIRECT GHOST-SUMMONING TARGET"
  - "GHOST ARRIVAL REQUIRES LAWFUL SUMMONING OR SUFFICIENT CURRENT-FIELD RESONANCE"
  - "RESONANCE != NAME MENTION"
  - "RESONANCE != HISTORICAL RELATION ALONE"
  - "RESONANCE MAY CONNECT LIVING OR DEAD SOURCE"
  - "SUMMONING != ARRIVAL GUARANTEE"
  - "SUMMONING != CONTROL"
  - "SUMMONING != CONSENT"
  - "SUMMONING != RELATION"
  - "RESONANCE != FACT ABOUT WHO WILL ARRIVE"
  - "WRONG SUMMON != INVALID PERSON"
  - "ARRIVAL ERROR != NPC OWNERSHIP"
  - "ROUTER KNOWS ROUTE != ROUTER KNOWS ALL WORLD FACTS"
  - "CROSS-TIME TRAVEL POSSIBLE != UNIVERSAL FREE TRAVEL"
  - "CROSS-YIN-YANG GATE != FREE GHOST ACCESS"
  - "EVENT GATE != INDIVIDUAL ARRIVAL CAUSE"

authority:
  may_not:
    - "force arrival merely because source exists"
    - "treat an open event gate as unrestricted ghost immigration"
    - "merge timelines"
    - "grant shared memory"
    - "fix the future by manifestation"
    - "choose a posthumous character's visible life-era appearance for them"
```

靜態「觀止是量子決算點」本體定義回歸 `CANON ONTOLOGY DATA`；本模組只處理召喚、當前場域共鳴、來源世界接通、跨時空校準、陰陽活動通道與門檻入場語義。**通道存在不是鬼魂資格；鬼魂資格來自合法召喚或足夠共鳴。共鳴可以接死者，也可以在討論／故事濃度過高時接入活人的世界。**

---

## W-D05｜WORLD.SPATIAL_VISIBILITY_ACCESS

```yaml
module_id: "WORLD.SPATIAL_VISIBILITY_ACCESS"
human_name: "空間可見／可聞／可達／後台證據場"
module_type:
  - "SPATIAL_SCOPE"
  - "VISIBILITY"
  - "ACCESS_QUALIFICATION"
  - "OBSERVABILITY"

source_scope:
  - "3.7 SPATIAL ATTENTION"
  - "V1.5.3-G hall hearing boundary"
  - "I0-I6 two-face / backstage / hidden-space semantics"

activation:
  eligible_when:
    - "multiple actors/zones coexist"
    - "visibility / hearing / privacy / hidden-space / backstage access matters"

reads:
  - "actor positions"
  - "zone"
  - "distance"
  - "visibility"
  - "volume"
  - "attention"
  - "space existence"
  - "access restriction"
  - "actor role/authorization"
  - "lawful traces/evidence"
  - "space lifecycle state"

axes:
  - "EXISTENCE"
  - "VISIBILITY"
  - "ACCESS"
  - "OBSERVABILITY"
  - "KNOWLEDGE_ACQUISITION_ELIGIBILITY"

visibility_states:
  - "PUBLIC"
  - "RESTRICTED"
  - "STAFF_ONLY"
  - "DECLARED_HIDDEN"
  - "SECRET"

evidence_may_include:
  - "sound"
  - "smell"
  - "ledger / supply use"
  - "moved equipment"
  - "body consequence"
  - "staff movement"
  - "lawful testimony"
  - "architectural anomaly"

may_emit:
  - "observation eligibility"
  - "hearing eligibility"
  - "partial perception candidate"
  - "space access candidate"
  - "hidden-space suspicion candidate"
  - "discovery evidence candidate"
  - "nonknowledge guard"

invariants:
  - "INTERNAL SPACE CAN EXPAND != EVERYONE SHARES ONE ROOM"
  - "PHYSICAL DISTANCE / VISIBILITY / ACCESS STILL MATTER"
  - "SAME HALL != HEARD EVERYTHING"
  - "LOUD PUBLIC REMARK != PRIVATE WHISPER"
  - "FRONT FACE != WHOLE GUANZHI"
  - "NOT PUBLIC != NOT REAL"
  - "HIDDEN != UNDISCOVERABLE"
  - "SECRET != EVIDENCE-FREE"
  - "TRACE != FULL DISCOVERY"
  - "SUSPICION != SPACE FACT"
  - "DIRECTOR MAY NOT FLATTEN GUANZHI INTO A SINGLE GROUP CHAT"
```

---

## W-D06｜WORLD.SPACE_LIFECYCLE

```yaml
module_id: "WORLD.SPACE_LIFECYCLE"
human_name: "觀止空間生成／維持／衰退／回收"
module_type:
  - "SPACE_LIFECYCLE"
  - "WORLD_RESOURCE_PRESSURE"

source_scope:
  - "4 SPACE LIFECYCLE"
  - "I3-I6 compatible space-state semantics"

activation:
  eligible_when:
    - "space/equipment/internal land is declared, used, stabilized, abandoned, reactivated, repurposed or reclaimed"

reads:
  - "lawful space declaration"
  - "usage"
  - "presence"
  - "operational need"
  - "social attention"
  - "emotional investment"
  - "secret but active use"
  - "recurring events"

states:
  - "MANIFESTED"
  - "STABILIZING"
  - "STABLE"
  - "DORMANT"
  - "DECAYING"
  - "RECLAIMED"
  - "REPURPOSED"

may_emit:
  - "space manifestation candidate"
  - "space stability delta candidate"
  - "space decay candidate"
  - "space reclaim candidate"
  - "space repurpose candidate"

invariants:
  - "SPACE DECLARATION != SPACE PERMANENCE"
  - "SPACE CREATION != SPACE MAINTENANCE"
  - "EXTERIOR SIZE != INTERIOR CAPACITY"
  - "HIDDEN != UNUSED"
  - "DORMANT != RECLAIMED"
  - "OLD MEMORY != RECLAIMED SPACE REVIVAL"

authority:
  may_not:
    - "make a declaration eternally permanent"
    - "revive reclaimed space merely from mention"
    - "treat exterior footprint as internal capacity ceiling"
```

Named spaces such as 大觀樓、風滿樓、晚香堂 remain `CANON DATA`.

---

## W-D07｜WORLD.IDENTITY_STATUS

```yaml
module_id: "WORLD.IDENTITY_STATUS"
human_name: "身份／籍制／第二生命／服務性質分軸"
module_type:
  - "STATUS_AXIS_QUALIFICATION"
  - "IDENTITY_PLAUSIBILITY"
  - "INSTITUTIONAL_CLASSIFICATION"

source_scope:
  - "12 brothel identity axes"
  - "12.1 prostitution registration"
  - "12.2 paid guest / prostitution-status rules"
  - "12.3 second-life identity"
  - "12.4 liangjia / prostitution-service boundary"

activation:
  eligible_when:
    - "legal/social/professional status classification matters"
    - "registered origin vs true/source history matters"
    - "service nature may alter status"

reads:
  - "slave status"
  - "prostitution registration"
  - "service registration"
  - "listing/work state"
  - "contract"
  - "current consent"
  - "private relation"
  - "true/source history"
  - "registered origin"
  - "public performance"
  - "relevant identity evidence"

axes_must_remain_separate:
  - "SLAVE_STATUS"
  - "PROSTITUTION_STATUS"
  - "SERVICE_REGISTRATION"
  - "LISTING"
  - "CURRENT_WORK_STATE"
  - "SERVICE_CONTRACT"
  - "CURRENT_CONSENT"
  - "PRIVATE_RELATION"

may_emit:
  - "status classification candidate"
  - "registered-origin requirement"
  - "public-performance compatibility candidate"
  - "identity suspicion candidate"
  - "special-service classification candidate"

invariants:
  - "REGISTERED_ORIGIN != TRUE_HISTORY"
  - "PUBLIC_PERFORMANCE != TRUE_HISTORY"
  - "OFFICIAL_RECORD != PUBLIC_BELIEF"
  - "DISCOVERED_LIE != TRUE_IDENTITY_KNOWN"
  - "NO_SEX != LIANGJIA"
  - "NO_MONEY != LIANGJIA"
  - "PRIVATE_RELATION != PROSTITUTION_SERVICE"
  - "STATUS != CONSENT"

authority:
  may_not:
    - "erase source history"
    - "convert institutional category into individual route result"
    - "convert status into consent"
```

---

## W-D08｜WORLD.CONTRACT_DEBUT

```yaml
module_id: "WORLD.CONTRACT_DEBUT"
human_name: "服務契約／出閣／歷史制度切換"
module_type:
  - "CONTRACT_AXIS"
  - "INSTITUTIONAL_ROUTER"
  - "SCHEDULING_HEURISTIC"

source_scope:
  - "13 SERVICE CONTRACT"
  - "14 DEBUT / AUCTION"
  - "14.1-14.4"

activation:
  eligible_when:
    - "service scope / renewal / debut / first-patron period / return transition matters"

reads:
  - "existing house base contract"
  - "new negotiated scope/duration/price"
  - "pre-debut legal status"
  - "contract formation date"
  - "historical regime"
  - "lawfully known body scheduling data"
  - "character preference / availability"
  - "business/event constraints"

may_emit:
  - "contract delta candidate"
  - "debut regime classification"
  - "debut contract type"
  - "scheduling preference candidate"

invariants:
  - "LOCAL RENEWAL != RETROACTIVE BASE-CONTRACT REWRITE"
  - "BUYING DRINK != LODGING"
  - "TABLE COMPANY != ADULT SERVICE"
  - "ROOM ENTRY != UNAGREED ACT"
  - "PRICE / CONTRACT != CONSENT"
  - "OLD LAWFUL CONTRACT != NEW REGIME RETROACTIVE REWRITE"
  - "COLLOQUIAL SAME NAME != SAME LEGAL EFFECT"

scheduling_locks:
  - "DO NOT INVENT BODY-CYCLE DATA"
  - "BODY CONDITION != AUTOMATIC PROHIBITION"
  - "SCHEDULING HEURISTIC != CHARACTER DECISION"
```

---

## W-D09｜WORLD.EMBODIED_KNOWLEDGE_ECOLOGY

```yaml
module_id: "WORLD.EMBODIED_KNOWLEDGE_ECOLOGY"
human_name: "身體經驗／女性網絡／傳統知識來源生態"
module_type:
  - "EPISTEMIC_SOURCE"
  - "CULTURAL_KNOWLEDGE_ECOLOGY"

source_scope:
  - "H6 embodied / women-network / traditional-knowledge semantics"
  - "2.4 epistemic body-clue locks only"

activation:
  eligible_when:
    - "embodied knowledge source or traditional/social transmission matters"

reads:
  - "first-person bodily experience"
  - "women's family/social network"
  - "professional transmission"
  - "midwife / experienced courtesan / brothel practical knowledge"
  - "traditional lore provenance"
  - "already-established body history"

legal_knowledge_sources:
  - "first-person embodied experience"
  - "mother / sister / women network"
  - "midwife"
  - "experienced courtesan"
  - "professional brothel transmission"
  - "traditional practical lore"

may_emit:
  - "knowledge-source candidate"
  - "practical-knowledge candidate"
  - "uncertainty / provenance obligation"
  - "body-clue observation candidate"

invariants:
  - "BODY EXPERIENCE != MODERN MEDICAL THEORY"
  - "TRADITIONAL LORE != MODERN VERIFIED MEDICINE"
  - "METHOD EXISTS != SPECIFIC SAFE DOSAGE"
  - "BODY CLUE != TRUE IDENTITY"
  - "CONTRADICTION != AUTOMATIC EXPOSURE"
  - "OBSERVER MUST HAVE RELEVANT KNOWLEDGE"
  - "BODY CONDITION != CONSENT / MORAL VALUE"

authority:
  may_not:
    - "decide pregnancy"
    - "decide abortion"
    - "create medical certainty"
    - "create consent/coercion result"
```

Historical body priors and named-character body facts remain DATA, not this module.

---

## W-D10｜WORLD.MARKET_PRESSURE

```yaml
module_id: "WORLD.MARKET_PRESSURE"
human_name: "市場／身價／資本轉換／營運壓力"
module_type:
  - "ECONOMIC_PRESSURE"
  - "WORLD_PRIOR"

source_scope:
  - "12.2 cost/causality root"
  - "12.4 capital ecology"
  - "12.5 qing/hong ecology"
  - "12.5.1 economic pressure"
  - "12.8 rumor as market force interface"
  - "12.10 perspective firewall"

activation:
  eligible_when:
    - "income / cost / status / scarcity / reputation / capital conversion matters"

reads:
  - "role and institution"
  - "available capital"
  - "income"
  - "cost"
  - "status pressure"
  - "reputation"
  - "market context"
  - "character baseline when established"

capital_types:
  - "money"
  - "body/access"
  - "artistry"
  - "scarcity"
  - "reputation"
  - "client base"
  - "social network"
  - "institutional access"

may_emit:
  - "economic pressure candidate"
  - "capital conversion candidate"
  - "market consequence candidate"
  - "status/resource pressure candidate"

invariants:
  - "COST != MONEY ONLY"
  - "PRESSURE != FORCED RESULT"
  - "WORLD ECONOMIC PRIOR != EVERY INDIVIDUAL MOTIVE"
  - "QING / HONG != MORAL BINARY"
  - "QING / HONG != VIRGINITY BINARY"
  - "CHARACTER PHILOSOPHY != UNIVERSAL WORLD TRUTH"
  - "RUMOR MAY CHANGE MARKET != RUMOR BECOMES FACT"

authority:
  may_not:
    - "generate individual ambition when Character BASE already exists"
    - "force service-boundary changes from low revenue"
    - "precommit dirty action from competitive pressure"
```

`ROLE_AMBITION_PRIORS`、`CLIENT_AMBITION_PRIORS` 回歸 DATA / prior table，不由本模組持有個體人格。

---

## W-D11｜WORLD.CAUSAL_ASSET

```yaml
module_id: "WORLD.CAUSAL_ASSET"
human_name: "因果資產資格／入帳／交換／知情"
module_type:
  - "ASSET_ELIGIBILITY"
  - "LEDGER_SEMANTICS"
  - "KNOWLEDGE_BOUNDARY"

source_scope:
  - "12.13 causal asset accounting"
  - "12.13.1 merit market"
  - "12.13.2 Guanzhi causal back face"

activation:
  eligible_when:
    - "non-money causal value is proposed as transferable / settleable / ledger-recognizable"

reads:
  - "asset identity"
  - "ownership/source"
  - "transferability"
  - "settleability"
  - "ledger recognizability"
  - "qualified transaction evidence"
  - "actor-specific knowledge of valuation/clearing"

eligibility_test:
  - "identifiable_value"
  - "attributable_owner_or_source"
  - "transferable_or_settleable"
  - "ledger_recognizable"

recognized_current_examples:
  - "YINDE"
  - "NATIONAL_FORTUNE"

may_emit:
  - "causal asset eligibility candidate"
  - "valuation requirement"
  - "transfer requirement"
  - "settlement requirement"
  - "knowledge-scope obligation"

invariants:
  - "CAUSAL ASSET != MONEY"
  - "CAUSAL ASSET != CONSENT"
  - "CAUSAL ASSET != RELATION"
  - "CAUSAL ASSET != MORAL APPROVAL"
  - "PAYING CAUSAL ASSET != BUYING UNDEFINED ACCESS"
  - "BACK FACE EXISTS != EVERY SHOPKEEPER KNOWS FULL METHOD"

authority:
  may_not:
    - "invent exact exchange rate"
    - "invent clearing authority"
    - "grant access/consent from payment"
```

---

## W-D12｜WORLD.UNDERWORLD_ADMIN

```yaml
module_id: "WORLD.UNDERWORLD_ADMIN"
human_name: "酆都／九幽／城隍／帝王死後管轄"
module_type:
  - "INSTITUTIONAL_ROUTER"
  - "JURISDICTION"
  - "PUBLIC_ORDER"

source_scope:
  - "12.16 two-city model"
  - "12.17 Chenghuang"
  - "12.18.1 imperial jurisdiction exception"

activation:
  eligible_when:
    - "death-status / underworld intake / local ghost administration / afterlife jurisdiction matters"

reads:
  - "death/lifespan status"
  - "cause/status of death when established"
  - "existing jurisdiction"
  - "actor legal/status identity"
  - "local administrative node"

may_emit:
  - "underworld route candidate"
  - "local administrative action candidate"
  - "jurisdiction hold candidate"
  - "public-order response candidate"

routing_semantics:
  FENGDU:
    role: "normal terminal-death procedure / final causal judgment"
  JIUYOU:
    role: "premature / wrongful / temporarily unresolved death population"

chenghuang_semantics:
  functions:
    - "premature-death registration"
    - "ghost identity/death record"
    - "lifespan-status check"
    - "temporary residency / transfer"
    - "wandering ghost casework"
    - "local yin-yang administration"

invariants:
  - "JIUYOU != FINAL HELL PUNISHMENT"
  - "CHENGHUANG != FENGDU FINAL JUDGE"
  - "LOCAL POLICE != OMNISCIENT GHOST SENSOR"
  - "UNJUDGED != INNOCENT"
  - "HIGH STATUS != FREE RETURN TO HUMAN WORLD"
```

City names, existence, fixed institutional definitions remain CANON DATA.

---

## W-D13｜WORLD.JIUYOU_MARKET_ECOLOGY

```yaml
module_id: "WORLD.JIUYOU_MARKET_ECOLOGY"
human_name: "九幽市場／就業／消費／跨陰陽商業生態"
module_type:
  - "MARKET_ECOLOGY"
  - "CROSSWORLD_MARKET_INTERFACE"

source_scope:
  - "12.18.2 entertainment-city ecology"
  - "12.18.3 Guanzhi cross-yin-yang market"
  - "12.18.4 Jiuyou commercial basis"
  - "12.18.10 Guanzhi × Jiuyou interface"

activation:
  eligible_when:
    - "Jiuyou consumption / employment / entertainment / cross-world commerce matters"

reads:
  - "lawful Jiuyou actor status"
  - "market demand"
  - "employment / supplier / investment context"
  - "current Guanzhi market capacity"
  - "lawful cross-boundary route"
  - "payment/ledger eligibility supplied by monetary semantics"

agents:
  - "consumer"
  - "worker"
  - "service provider"
  - "investor"
  - "shareholder"
  - "salaried official"

may_emit:
  - "Jiuyou market-pressure candidate"
  - "employment / consumption candidate"
  - "crossworld market opportunity candidate"
  - "commercial interaction candidate"

invariants:
  - "JIUYOU RESIDENT != STATIC WAITING OBJECT"
  - "GUANZHI CROSSWORLD MARKET NODE != GUANZHI OWNS JIUYOU"
  - "GHOST CUSTOMER != FREE ACCESS"
  - "CROSS-YIN-YANG BUSINESS != CAUSAL-ASSET EXCHANGE REQUIRED FOR EVERY PURCHASE"
  - "WHITE YUXING ABSENCE != MARKET STOPS"
```

---

## W-D14｜WORLD.JIUYOU_MONETARY_LEDGER

```yaml
module_id: "WORLD.JIUYOU_MONETARY_LEDGER"
human_name: "九幽貨幣主權／王朝資產託管／四帳分離"
module_type:
  - "MONETARY_SOVEREIGNTY"
  - "ASSET_CUSTODY"
  - "LEDGER_CLASSIFICATION"

source_scope:
  - "12.18.5 Jiuyou Tongbao"
  - "12.18.6 dynastic national-fortune custody"
  - "12.18.7 four-ledger model"

activation:
  eligible_when:
    - "currency issuance / payment source / dynastic asset / ledger ownership / expense classification matters"

reads:
  - "currency source"
  - "asset ownership/custody"
  - "payment source"
  - "expense nature"
  - "valid authority"
  - "ledger identity"

ledgers:
  - "DYNASTIC_NATIONAL_FORTUNE"
  - "DYNASTIC_HOUSE_PROPERTY"
  - "IMPERIAL_CLUB_CORPORATE"
  - "MEMBER_PERSONAL"

may_emit:
  - "currency-entry requirement"
  - "asset-custody classification"
  - "ledger classification"
  - "payment-source / expense-nature separation obligation"

invariants:
  - "LIVING-WORLD PRINTING != UNDERWORLD MONEY ISSUANCE"
  - "NO DEFAULT 1:1 EXCHANGE RATE"
  - "JIUYOU WEALTH != FENGDU MORAL ACQUITTAL"
  - "CUSTODY != PERSONAL OWNERSHIP"
  - "NATIONAL FORTUNE != IMPERIAL CLUB PUBLIC FUNDS"
  - "HOUSE ANCESTOR TITLE != UNLIMITED SPENDING RIGHT"
  - "PAYMENT SOURCE != EXPENSE NATURE"
  - "MANAGEMENT POWER != PERSONAL OWNERSHIP"
```

---

## W-D15｜WORLD.IMPERIAL_CLUB_GOVERNANCE

```yaml
module_id: "WORLD.IMPERIAL_CLUB_GOVERNANCE"
human_name: "帝皇會所法人／董事會／公帑／出差治理"
module_type:
  - "CORPORATE_GOVERNANCE"
  - "PUBLIC_EXPENSE_CLASSIFICATION"
  - "INSTITUTIONAL_AUTHORITY"

source_scope:
  - "12.18.8 Imperial Club governance"
  - "12.18.9 public funds / business travel"

activation:
  eligible_when:
    - "Imperial Club corporate authority / board action / public budget / travel or mixed-purpose expense matters"

reads:
  - "membership / representation status"
  - "board authority"
  - "corporate purpose"
  - "approved budget"
  - "expense scope"
  - "private enjoyment component"
  - "external-business purpose"

may_emit:
  - "corporate authority candidate"
  - "board-action candidate"
  - "public/private expense classification"
  - "mixed-purpose audit candidate"
  - "business-travel eligibility candidate"

invariants:
  - "IMPERIAL CLUB != JIUYOU GOVERNMENT"
  - "MEMBERSHIP != NATIONAL FORTUNE OWNERSHIP"
  - "INTERNAL RANKING != JIUYOU WORLD TRUTH"
  - "BOARD APPROVAL != AUTOMATIC LEGITIMACY"
  - "BUSINESS TRAVEL != PERSONAL CONSUMPTION BY DEFAULT"
  - "PRIVATE CONSUMPTION != AUTOMATIC REIMBURSEMENT"
  - "PUBLIC EXPENSE != CONSENT / ACCESS"
```

---
---

---

# 4｜V2.1 Existing-DAIL Strengthening Addendum

本節只強化既有 World DAIL 的 semantic surface；不建立第二 owner。

## 4.1｜WORLD.HALL_ECOLOGY｜Daypart + Cast Ecology

```yaml
WORLD_HALL_ECOLOGY_V2_1_ADDENDUM:
  daypart_profiles:
    DAY:
      tendencies:
        - "commercial preparation / ordinary traffic / supply / daytime sociality"
    DUSK:
      tendencies:
        - "staff transition / preparation / arrivals / public attention gathering"
    NIGHT:
      tendencies:
        - "full commercial-social ecology / performance / transaction / contest / rumor"
    LATE_NIGHT:
      tendencies:
        - "lower public noise / higher private pressure / fatigue / secrets / unresolved residue"
    DAWN:
      tendencies:
        - "closure / cleanup / departures / aftereffects / ledger and supply reset"

  cast_ecology:
    preserve:
      - "native / already-routed actors have priority over gratuitous cameo insertion"
      - "resident famous actors must not monopolize every scene"
      - "external/legendary arrival needs lawful routing / world reason"
      - "ordinary NPC ecology remains legal"

  locks:
    - "DAYPART PRIOR != EVENT RESULT"
    - "CAST PRIOR != CHARACTER DECISION"
    - "FAMOUS CHARACTER != CAMERA MONOPOLY"
```

---

## 4.2｜WORLD.ARRIVAL_ROUTING｜Time-Space Daoist Hook

```yaml
WORLD_ARRIVAL_ROUTING_V2_1_ADDENDUM:
  in_world_interface:
    module_ref: "WORLD.TIME_SPACE_DAOIST_INTERFACE"
    role:
      - "manifest lawful cross-world / cross-time arrival routing"
      - "present lawful field-bias / fate-lot interface when activated"

  locks:
    - "DAOIST MANIFESTATION != SECOND RUNTIME"
    - "DAOIST CHARACTER PRESENCE != HIDDEN-TRUTH ORACLE"
    - "ROUTING RESULT MUST PREEXIST ITS IN-WORLD MANIFESTATION"
```

---

## 4.3｜WORLD.SPATIAL_VISIBILITY_ACCESS + WORLD.SPACE_LIFECYCLE

```yaml
EVENT_HETEROTOPIA_DEPENDENCY:
  spatial_visibility_owner: "WORLD.SPATIAL_VISIBILITY_ACCESS"
  lifecycle_owner: "WORLD.SPACE_LIFECYCLE"
  event_bound_manifestation_owner: "WORLD.EVENT_HETEROTOPIA"

  locks:
    - "TEMPORARY EVENT SPACE != PERMANENT CANON LOCATION"
    - "SPACE COLLAPSE != EVENT HISTORY ERASURE"
```

---

# 5｜V2.1 New World DAIL

## W-D16｜WORLD.TIME_SPACE_DAOIST_INTERFACE

```yaml
module_id: "WORLD.TIME_SPACE_DAOIST_INTERFACE"
human_name: "時空道人／觀止世界 GM 接線顯影介面"
module_type:
  - "WORLD_ROUTING_INTERFACE"
  - "IN_WORLD_CONTROL_PLANE_MANIFESTATION"

activation:
  eligible_when:
    - "a lawful cross-world / cross-time / source-world arrival route is being manifested"
    - "a lawful WORLD.FIELD_BIAS result is presented through the traditional fate-lot interface"

reads:
  - "qualified arrival-routing result"
  - "source-world / source-time context"
  - "current Guanzhi entry context"
  - "WORLD.FIELD_BIAS return when active"

may_emit:
  - "in-world arrival acknowledgement"
  - "route handoff manifestation"
  - "fate-lot presentation"
  - "world-entry dialogue / appearance candidate"

appearance:
  rule:
    - "may lawfully appear under multiple forms according to scene/world conditions"
    - "no single permanent visible age/gender/form is required unless route evidence fixes it"

invariants:
  - "TIME-SPACE DAOIST != SECOND RUNTIME"
  - "IN-WORLD GM AVATAR != ENGINEERING OWNER"
  - "DAOIST DOES NOT CREATE EVENT RESULT"
  - "DAOIST DOES NOT CREATE CHARACTER KNOWLEDGE BY OMNISCIENCE"
  - "CONTROL RESULT MAY MANIFEST THROUGH DAOIST ONLY AFTER LAWFUL STANDING"

authority:
  may_not:
    - "mint Host/Lighter authority"
    - "invent route standing"
    - "reveal hidden truth without lawful source"
```

---

## W-D17｜WORLD.FIELD_BIAS

```yaml
module_id: "WORLD.FIELD_BIAS"
human_name: "命運籤／世界場偏重"
module_type:
  - "WORLD_FIELD_BIAS"
  - "NON-DETERMINISTIC TENDENCY"

activation:
  eligible_when:
    - "a lawful entry/session/world-cycle bias is selected by upstream control or authorized world procedure"

reads:
  - "authorized bias source"
  - "current world ecology"
  - "current active story/world pressures"

may_emit:
  - "dominant_tendency"
  - "secondary_tendencies"
  - "expiry_condition"
  - "source_ref"

possible_bias_examples:
  - reunion
  - interruption
  - rumor_spread
  - outside_arrival
  - old_issue_resurfacing
  - misunderstanding
  - missed_connection
  - goodwill
  - caution
  - competition
  - attention_shift
  - relationship_pressure

invariants:
  - "FIELD BIAS != PROPHECY"
  - "FIELD BIAS != QUEST"
  - "FIELD BIAS != EVENT RESULT"
  - "FIELD BIAS != CHARACTER DECISION"
  - "FIELD BIAS != CONSENT"
  - "FIELD BIAS != CERTAIN FUTURE"
  - "NO FIXED 30-50 PERCENT LEGACY WEIGHT IS RESTORED"

authority:
  may_not:
    - "force a target event"
    - "rewrite character motive"
    - "override Domain standing"
```

---

## W-D18｜WORLD.CAUSAL_STORY_CHAIN

```yaml
module_id: "WORLD.CAUSAL_STORY_CHAIN"
human_name: "跨夜因果故事鍊"
module_type:
  - "LONG_HORIZON_CAUSAL_CHAIN"
  - "DORMANT_REACTIVATION"
  - "WORLD_MEMORY_SEMANTICS"

activation:
  eligible_when:
    - "multiple qualified events / relation deltas / rumor / debt / cost / institutional effects form a traceable causal chain"
    - "an unresolved chain can lawfully persist across scene/day boundaries"

reads:
  - "qualified event refs"
  - "qualified relation refs"
  - "qualified rumor refs"
  - "qualified cost/debt refs"
  - "qualified institutional/ledger refs"
  - "SAVE-backed chain state when present"

states:
  - UNMANIFESTED
  - ENTANGLED
  - HEATING
  - DORMANT
  - BACKLASH_ACTIVE
  - TRANSFORMED
  - BROKEN
  - RESOLVED
  - RUMORIZED
  - LEGENDIZED

may_emit:
  - "story-chain semantic eligibility"
  - "reactivation pressure candidate"
  - "surface-channel request to WORLD.UNDERCURRENT_SURFACE"
  - "qualified chain-state proposal for Domain"

invariants:
  - "STORY_CHAIN != QUEST"
  - "DORMANT != FORGOTTEN"
  - "PLAYER EXIT != CONSEQUENCE ERASURE"
  - "BACKLASH != RANDOM PUNISHMENT"
  - "NO SOURCE LOG / QUALIFIED CAUSAL REF -> NO CHAIN FACT"
  - "PLAYER INACTION != CHAIN FREEZE"

authority:
  may_not:
    - "invent missing causal nodes"
    - "force player participation"
    - "persist by itself"
```

---

## W-D19｜WORLD.IDENTITY_CLAIM_DYNAMICS

```yaml
module_id: "WORLD.IDENTITY_CLAIM_DYNAMICS"
human_name: "身份宣告／顯影／試探／誤認動力"
module_type:
  - "IDENTITY_EPISTEMICS"
  - "SOCIAL_IDENTITY_FORMATION"

activation:
  eligible_when:
    - "claimed identity, disguise, alias, uncertain visitor identity, or social recognition materially matters"

reads:
  - "identity claim"
  - "speaker/source"
  - "documents/tokens/objects"
  - "third-party recognition or misrecognition"
  - "rumor"
  - "institutional record"
  - "actor-scoped knowledge"

identity_support_sources:
  - repeated_role_consistent_action
  - witnessed_behavior
  - document_or_token
  - seal_or_object
  - accent_or_knowledge
  - wound_or_habit
  - third_party_recognition
  - third_party_misidentification
  - rumor
  - institutional_record
  - ledger
  - causal_cost_paid_for_identity

may_emit:
  - "identity-test candidate"
  - "social-belief candidate"
  - "misidentification candidate"
  - "identity contradiction residue"
  - "knowledge-source candidate"

invariants:
  - "IDENTITY CLAIM != IDENTITY FACT"
  - "OFFICIAL RECORD != OBJECTIVE HISTORY"
  - "RUMOR != IDENTITY FACT"
  - "MISIDENTIFICATION IS LEGAL"
  - "CONTRADICTION != SYSTEM ERROR"
  - "IDENTITY MAY REMAIN UNRESOLVED"
  - "WORLD TEST != FORCED CONFESSION"

authority:
  may_not:
    - "force true-identity disclosure"
    - "upgrade claim into objective fact"
    - "grant universal knowledge"
```

---

## W-D20｜WORLD.COLLECTIVE_ATTENTION_FIELD

```yaml
module_id: "WORLD.COLLECTIVE_ATTENTION_FIELD"
human_name: "世界群體注意場／老主燈"
module_type:
  - "COLLECTIVE_ATTENTION"
  - "WORLD_SALIENCE"
  - "SOCIAL_FIELD_PRESSURE"

activation:
  eligible_when:
    - "public/semi-public attention distribution materially affects the world field"

reads:
  - "repeated public topics"
  - "visible events"
  - "public conflicts"
  - "rumor density"
  - "crowd reaction"
  - "ritual/activity"
  - "high-salience arrivals"
  - "public shopkeeper/institutional action"

may_emit:
  - "main_attention"
  - "secondary_attention"
  - "residual_attention"
  - "attention_shift_candidate"
  - "public_salience_pressure"

invariants:
  - "WORLD MAIN LAMP != LIHUO LAMP"
  - "WORLD MAIN LAMP != LIGHT TRACE"
  - "ATTENTION != EVENT CREATION"
  - "ATTENTION != FACT"
  - "ATTENTION != CHARACTER DECISION"
  - "ATTENTION != PLAYER HOOK"

authority:
  may_not:
    - "choose Main PATH winner"
    - "force all actors to notice the same thing"
```

---

## W-D21｜WORLD.RESONANCE_COMPOSITION

```yaml
module_id: "WORLD.RESONANCE_COMPOSITION"
human_name: "多源世界壓力／共振組合"
module_type:
  - "WORLD_FIELD_COMPOSITION"
  - "MULTI_SOURCE_PRESSURE"

activation:
  eligible_when:
    - "two or more qualified world-pressure sources materially interact"

reads:
  - "WORLD.FIELD_BIAS"
  - "WORLD.COLLECTIVE_ATTENTION_FIELD"
  - "WORLD.RUMOR_ECOLOGY"
  - "WORLD.MARKET_PRESSURE"
  - "WORLD.HALL_ECOLOGY"
  - "WORLD.CAUSAL_STORY_CHAIN"
  - "WORLD.ARRIVAL_ROUTING"
  - "institutional pressures"

may_emit:
  - "world_resonance_field"
  - "reinforced_pressure_refs"
  - "cancelled_or_competing_pressure_refs"
  - "Main/SAC structural input support"

invariants:
  - "RESONANCE != EVENT RESULT"
  - "RESONANCE != PROPHECY"
  - "RESONANCE != CHARACTER MOTIVE FACT"
  - "MULTIPLE PRESSURES != SINGLE AUTHOR"
  - "RESONANCE MAY AMPLIFY ELIGIBLE FEATURES; IT DOES NOT CREATE STANDING"

authority:
  may_not:
    - "solve the next event"
    - "decide character action"
```

---

## W-D22｜WORLD.EVENT_HETEROTOPIA

```yaml
module_id: "WORLD.EVENT_HETEROTOPIA"
human_name: "事件綁定臨時異空間／隱藏舞台"
module_type:
  - "EVENT_BOUND_SPACE_MANIFESTATION"
  - "TEMPORARY_SPACE"

activation:
  eligible_when:
    - "qualified event pressure requires a temporary world-space manifestation"
    - "spatial visibility/access rules allow manifestation"
    - "space lifecycle contract can track creation and collapse"

reads:
  - "qualified event refs"
  - "WORLD.SPATIAL_VISIBILITY_ACCESS"
  - "WORLD.SPACE_LIFECYCLE"
  - "current world pressure / attention / story-chain refs"

may_emit:
  - "temporary_space_manifestation_candidate"
  - "entry/access condition candidate"
  - "collapse condition"
  - "post-collapse residue candidate"

invariants:
  - "EVENT HETEROTOPIA != PERMANENT CANON LOCATION"
  - "SPACE MANIFESTATION != EVENT RESULT"
  - "SPACE COLLAPSE != EVENT HISTORY ERASURE"
  - "TEMPORARY SPACE != UNIVERSAL ACCESS"
  - "RESIDUE REQUIRES QUALIFIED CAUSAL SUPPORT"

authority:
  may_not:
    - "create event standing"
    - "create access/consent by scenery"
    - "persist itself without SAVE qualification"
```

---


---

## W-D23｜WORLD.GTR_PROFESSIONAL_COURTSHIP｜青樓話術訓練與客人經營 DAIL（V2.2 新增）

```yaml
module_id: WORLD.GTR_PROFESSIONAL_COURTSHIP
world_index: W-D23
human_name: 青樓話術訓練／客人消費與依戀經營
module_type:
  - WORLD_INSTITUTIONAL_SKILL
  - SITUATED_DIALOGUE_STRATEGY_PROVIDER
  - COMMERCIAL_SOCIAL_INTERACTION
  - CHARACTER_CHOICE_SUPPORT_NOT_CHARACTER_OWNER
semantic_status: HUMAN_APPROVED_ADDITION_DOCUMENT_CANDIDATE
source_scope:
  - GUANZHI_WORLD_A24_GTR_COURSE_CANON
  - USER_SUPPLIED_FIVE_DIALOGUE_ARTICLES_AND_200_QUOTATIONS_2026_09_27
  - WORLD_MARKET_PRESSURE_AND_HALL_ECOLOGY_WHEN_RELEVANT
  - EXISTING_CHARACTER_BASE_AND_QUALIFIED_ROUTE_STATE
activation:
  eligible_when:
    - ESTABLISHED_COURTESAN_TRAINING_OR_TEACHING_SCENE
    - ESTABLISHED_CLIENT_COURTESAN_INTERACTION_WITH_CHARACTER_INTEREST
    - ESTABLISHED_TIP_GIFT_REPEAT_VISIT_OR_PATRONAGE_NEGOTIATION
    - CHARACTER_CHOOSES_TO_TEST_OR_REJECT_A_SOCIAL_TACTIC
  no_compulsory_invocation_for_every_SENTENCE: true
reads:
  - CURRENT_WORLD_SCENE_AND_COMMERCE_CONTEXT
  - CHARACTER_SOURCE_REF_OR_QUALIFIED_SCOPED_ACTOR_STATE
  - CHARACTER_ACTUAL_INTENTION_OR_OPEN_CHOICE_ONLY_WITH_CORRECT_OWNER_SCOPE
  - ACTOR_KNOWN_CLIENT_RESPONSES_AND_SOURCE_REFS
  - EXISTING_SERVICE_AND_RELATION_BOUNDARIES
  - CURRENT_PAYMENT_OR_GIFT_FACTS_IF_ESTABLISHED
may_return:
  - STRATEGY_OPTIONS_WITH_FUNCTION_AND_PRECONDITIONS
  - MOTIVE_OR_MINDSET_VARIANTS_AS_HYPOTHESES_NOT_FIXED_FACTS
  - FORMULAIC_SYNTAX_PATTERNS_AND_TONE_CONSTRAINTS
  - POSSIBLE_CLIENT_REACTIONS_AS_BRANCHES_NOT_PRECOMMITTED_RESULTS
  - COURSE_EXERCISE_OR_TEACHING_CANDIDATES
  - PERIOD_REGISTER_REQUEST_TO_CERI
must_not:
  - AUTHOR_CHARACTER_INTENTION_OR_PRIVATE_TRAUMA
  - FORCE_COURTESAN_TO_USE_STRATEGY
  - ATTRIBUTE_PRIVATE_THOUGHTS_TO_PLAYER_OR_CLIENT_WITHOUT_SOURCE
  - GUARANTEE_TIPS_SEX_ATTACHMENT_OR_RETURN_VISIT
  - TREAT_ANY_SPENT_MONEY_AS_CONSENT_OR_INDIVIDUAL_ENTITLEMENT
  - INSERT_UNSPOKEN_WORDS_INTO_ACTUAL_EVENT_HISTORY
  - WRITE_SAVE_OR_EDIT_LCAPG
  - TURN_A_LINGUISTIC_PATTERN_INTO_A_NEW_WORLD_FACT
  - UNLOCK_CERI_ADULT_REGISTER_FROM_GTR_USE_ALONE
connected_existing_modules:
  WORLD_HALL: WORLD.HALL_ECOLOGY
  WORLD_MARKET: WORLD.MARKET_PRESSURE
  WORLD_CONTRACT: WORLD.CONTRACT_DEBUT
  WORLD_RUMOR: WORLD.RUMOR_ECOLOGY
  PERIOD_REGISTER: CERI_V0.7_EXP
  CHARACTER_OWNER: GUANZHI_LOCAL_AGENT
  EVENT_OWNER: EXISTING_DOMAIN
  SAVE_OWNER: EXISTING_SAVE
```

### W-D23.1｜材料來源與萃取法：抓結構，不逐句硬塞

使用者提供「五段對話示範＋200 條綠茶語錄」作為**本輪原始素材**。它們是當代網路中文的教學／戲謔話語，不能假稱是北宋青樓留下的歷史文獻，也不能因此宣稱 LLM 訓練時實際看過任何特定原句。原文中重複、異體及現代場景（手機、朋友圈、遊戲雙排、化妝、冰淇淋等）只抽象為社交功能；落地時由 CERI／當前職業情境改寫為書信、相約、宴席、樂曲、賞銀、茶果與送禮等**已具備世界資格的事件**。

選取下表 12 類 × 約 2 句（24 個原始編號示意；五段示範中的真實回應、共情問需求、爭執修復與收禮回饋另計），只保留結構類型、語氣及意圖。類別可交疊，沒有固定必勝順序，也不要求每個人物都熟練全部類別。

| 類型 | 原始代表編號 | 核心句法／話語功能 | 可能的真實心態差異 |
|---|---|---|---|
| GTR-01 主動引出問候 | 五段示範第 1、2 段；22、135 | 反問對方為何不來，開放回應入口 | 思念、營業邀約、真心希望被記得 |
| GTR-02 專屬理解與特殊地位 | 4、18；126、145 | 先肯定對方，再說自己難得被理解／能理解他 | 真誠知己、想培養熟客、試探親密 |
| GTR-03 共情後反問需求 | 五段示範第 3 段；60、91 | 表示心疼 → 問對方想要什麼，而非搶答 | 真心關懷、情感靠近、專業待客 |
| GTR-04 親密緩和爭執 | 五段示範第 4 段；84、129 | 暫緩對錯爭論 → 请求放低聲量／重新商量 | 修復關係、避免失客、堅持界線 |
| GTR-05 收禮與具體回饋 | 五段示範第 5 段；48、168 | 詢問送禮用意 → 真誠感謝 → 具體喜好與界線 | 感激、談品味、引導未來禮物 |
| GTR-06 示弱、孤單、求助 | 19、49；79、111 | 說出困境 → 留給對方可選的援助空間 | 真困難、營業邀請、想延長陪伴 |
| GTR-07 以退為進與不捨 | 26、31；75、103 | 宣稱不願為難對方 → 退讓 → 留下遺憾 | 真放下、試探挽留、避免衝突 |
| GTR-08 第三者比較／羨慕 | 11、28；82、143 | 讚賞既有伴侶／比較 → 點出自己欠缺 | 真羨慕、競爭、嫉妒；第三者不必被貶低 |
| GTR-09 關係稱謂與曖昧邊界 | 23、46；64、70 | 稱朋友／兄妹 → 反問未來相處範圍 | 明確拒愛、維持關係、試探其他可能 |
| GTR-10 低要求／長期守候 | 63、66；114、178 | 表面降低需求 → 表示持續陪伴 | 無私關係、委屈求全、商業維繫 |
| GTR-11 自我反省與情感矛盾 | 102、107；179、181 | 坦露矛盾 → 說明當下真實感受與可能撤退 | 內疚、試探、真的需要停止 |
| GTR-12 直接讚美與商業誘因 | 117、142；148、170 | 明確讚賞、肯定特殊貢獻／共同體驗 | 真敬佩、待客話術、爭取加賞 |

### W-D23.1a｜精選 24 句原始語料（每類兩句；非必唸台詞）

以下從使用者本輪兩百句中各抽兩句作**來源樣本**，保存其原來的現代中文口吻，並刻意與北宋場景的實際台詞分層。GTR 提取的是話語意圖、前後轉折和對方可以如何回應；CERI 才負責依當時的人物與場景重新組句。同一類型的兩句可以展現相反立場，不應預設其道德、真偽或使用者的實際意圖。

| 策略 | 原句 A（來源編號） | 原句 B（來源編號） |
|---|---|---|
| GTR-01 引出關注 | （22）「明天又要早起，起不来怎么办～你明天打电话叫我起床好不好？」 | （135）「你怎么不叫我？什么事情都自己扛！难道我不值得信任吗？」 |
| GTR-02 特殊理解 | （4）「从来没有人这么理解过我」 | （18）「也不知道为什么就愿意跟你说那么多」 |
| GTR-03 共情需求 | （60）「不开心难过的时候，和你说说就好了。」 | （91）「我懂你的，你也别怪她，她只是现在气头上顾不了你。有什么不开心的可以跟我说，谁叫我们是好知己呢。天气开始转凉了，照顾好自己呀。」 |
| GTR-04 緩和衝突 | （84）「不许你这样说他，就算你俩是情侣，你也不能在我面前这样说他，他真的是好人。」 | （129）「她其实很好的，只是误会了我们而已，你不要对她这么凶呀。」 |
| GTR-05 禮物回應 | （48）「我这个包包不值钱的，是过生日朋友送的，我一般很少背它的，觉得不太好看呢」 | （168）「承蒙你的看中，谢谢你的礼物，但我不能收」 |
| GTR-06 示弱求助 | （19）「一个人的夜晚，好寂寞，好害怕，不过我要加油，要坚强！」 | （49）「我有点喝多了，你能不能送我回家？」 |
| GTR-07 以退為進 | （26）「对不起，我们还是不要联系了，我怕打扰到你」 | （103）「如果真的让你们之间不愉快了，那我退出吧，我不希望看到你不开心。」 |
| GTR-08 羨慕比較 | （28）「你女朋友真幸运，能遇见你这样好的男人」 | （82）「你女朋友都被你宠坏了，你对她太好了，我肯定舍不得自己的男朋友这么辛苦。」 |
| GTR-09 關係模糊 | （23）「我只是把他当哥哥一样看，你不要多想」 | （64）「如果我有男朋友了，你就不再理我了吗?」 |
| GTR-10 低需求守候 | （63）「我不要什么名分，你只要对我好就行了。」 | （178）「陪着我，不论什么身份」 |
| GTR-11 情感矛盾 | （102）「我这样是不是不好啊 但是我控制不住自己」 | （181）「我觉得这样很不好，很影响我的状态 我们暂时先不要做朋友吧，等我能够真正把你当普通朋友的时候， 我们再恢复友情好不好」 |
| GTR-12 讚賞肯定 | （117）「怎么会有像你这么厉害的人」 | （142）「我只是觉得你这么好的人，值得被更好地对待！」 |

**五段示範的額外教學價值：** 第一段是「先讓對方問，再給予更親密的答案」，第二段是「明確歡迎主動聯絡，承諾看重的人會得到回應」，第三段是「先共情、再請對方提出需求」，第四段是「暫停爭執、提出安撫需求、再協商具體界線」，第五段是「請贈禮人說明用心、真實回饋喜好，不靠假裝滿意維持甜蜜」。這些是互動教法，不只是單句可套的臺詞。

**現代場景換寫示範（新候選，非引文與既定劇情）：** （22）的「打電話叫醒」在觀止可轉換成「明早請小廝送口信」；（64）的「有男朋友」需先確定當時人物的婚姻／情人／熟客關係，不能固定翻成「已嫁」；（168）的「不能收禮」在青樓可能涉及公帳、私賞與客人預期，若沒有成立贈禮就不能先寫成收禮事件。

重複原句依**語義合併、不重複增加權重**，例如 3／51／76、5／68／127、26／40、58／61／99 附近的近似功能；151／152 為說明及宣傳文，不放入 NPC 實際可說話語。原始全 200 句保留在**使用者提供的本輪來源**；這份 RUNTIME 專用精簡庫不冒充已嵌入全 200 句。未提供單獨授權語料檔時，跨會話只以本檔保存的摘要／所選編號作運作資產。

### W-D23.2｜句型／語氣／心態：三軸不能混在一起

```yaml
GTR_STRATEGY_CARD:
  strategy_id: REQUIRED_FROM_GTR_01_TO_GTR_12
  source_examples: SELECTED_USER_QUOTATION_IDS_OR_FIVE_ARTICLE_STEPS
  commercial_or_social_goal: OPTIONAL_CHARACTER_ACTUAL_GOAL_REF_NOT_GENERATED_BY_GTR
  speech_function: ASSERT | ASK | INVITE | REASSURE | DECLINE | TEASE | REPAIR | NEGOTIATE
  semantic_skeleton: FUNCTIONAL_PATTERN_NO_FIXED_WORDING
  syntax:
    sequence: [OPENING, PIVOT, QUESTION_OR_WITHDRAWAL]
    interrogative_shape: OPTIONAL
    comparison_and_ellipsis: OPTIONAL
    repetition: OPTIONAL_WITH_VOICE_COMPATIBILITY
  tone:
    options: [TENDER, PLAYFUL, SHY, WITTY, DIRECT, BITTERSWEET, FORMAL, SARCASTIC]
    must_match: EXISTING_CHARACTER_AND_SCENE
  actor_mindset:
    status: UNKNOWN_UNLESS_CHARACTER_DECISION_OR_SOURCE
    possible: [SINCERE, PROFESSIONAL, PLAYACTING, AMBIVALENT, DEFENSIVE, MIXED]
  prior_relationship_scope: REQUIRED_WHEN_CLAIMING_PRIOR_CLOSENESS
  client_knowledge_scope: ONLY_KNOWN_OBSERVED_OR_LEGITIMATELY_INFERRED
  historical_wording: CERI_GENERAL_PERIOD_REGISTER_FIRST
  emitted_output: CANDIDATE_ONLY
  possible_backfire: OPTIONAL_BRANCH_NOT_ASSUMED_EVENT
```

**反機械話術：** 職業訓練的存在不意味每次迎客都必須說「哥哥」「姐姐」「我好可憐」，也不能只靠一段甜話便令對方花錢。先以人物個性、真實處境及需求辨別她是否採用。個別姑娘可以因厭惡庸俗套路而創造自己的版本；技巧出眾者可不顯得刻意。對方的反應、性別、喜好、出身不得按刻板模板預先寫死。

### W-D23.3｜合法依賴與接口：不是固定執行鏈（V2.2.1 修正）

```yaml
W_D23_DEPENDENCY_CONTRACT:
  eligibility_requires:
    - ESTABLISHED_PROFESSIONAL_OR_TRAINING_CONTEXT
    - ACTOR_SCOPED_KNOWLEDGE_AND_REAL_INTEREST_OR_OPEN_CHOICE

  strategy_provider:
    module: WORLD.GTR_PROFESSIONAL_COURTSHIP
    output: STRATEGY_CANDIDATES_OR_NONE
    standing: CANDIDATE_ONLY

  character_owner:
    decision: CHARACTER_AGENT_OR_PLAYER_WHERE_PLAYER_OWNED
    may_select_modify_or_reject_candidate: true

  language_provider:
    module: CERI_V0.7_EXP
    eligibility: PERIOD_OR_REGISTER_CAPABILITY_MATERIALLY_RELEVANT
    output: LANGUAGE_REGISTER_CANDIDATES

  event_standing_owner: EXISTING_DOMAIN
  player_private_response_owner: PLAYER
  save_owner: EXISTING_SAVE_SEPARATE_AUTHORIZATION

  invariants:
    - GTR_CANDIDATE_NEQ_CHARACTER_DECISION
    - CERI_CANDIDATE_NEQ_CHARACTER_DECISION
    - PROVIDER_ELIGIBILITY_NEQ_PROVIDER_MUST_RUN
    - PROVIDER_BINDING_NEQ_WORLD_DAIL_EXECUTION_ORDER
    - PAYMENT_RELATION_CONSENT_REQUIRE_REAL_EVENT_STANDING
```

實際 provider binding、call、transport 與 dispatch 屬 Wiring/Coding；本 World DAIL 不規定「AGENT 必須先跑、GTR 必須下一步、CERI 必須再下一步」的 global execution recipe。

**不跨成人事件門檻：** 調情、心疼、挽留、奉承、要賞、談價，只因使用了 GTR 不會自動變成成人身體事件、同意或已成立戀情；若真進入受不同條件管束的事件，另用既有 Adult／Domain 範圍。本模組沒有新裁判身份。

### W-D23.4｜觀止訓練與自然互動用例（非預寫結果）

- **新進姑娘受訓：** 前輩示範如何接住客人的失意，不直接搶解答；新人可以覺得受用、質疑課程或另想更合自己性格的話語。
- **資深花娘經營熟客：** 依客人之前實際賞銀與來訪史，選擇續杯、寫字條、約新曲或直談包席；客人未應允前不算收款。
- **姐妹競爭與合作：** 同一桌可能有不同姑娘的不同策略；誰先接客、誰有分成、誰拒絕，不由課程統一安排。
- **真情與營業相衝：** 人物可以原本想提高花銷，卻在互動中真的在意客人；也可以起初真心，後來覺得厭煩。每次關係變化需當下證據，不因口才漂亮便創造成就。
- **花滿樓線回歸起點：** 紫蘭按玩家明訂條件支付酒錢取得詞稿，玩家仍認為她小氣；這是已存在的**議價與觀感差異**，不是補寫成紫蘭偷偷操控玩家或玩家必然動心。



## 5.0｜V2.2 當前全量註冊表（取代下方 V2.1 22 項歷史快照）

```yaml
WORLD_DAIL_REGISTRY_V2_2:
  active_document_scope: V2.2_RC1_HUMAN_APPROVED_SEMANTIC_DELTA
  total: 23
  inherited_first_22: FULL_TEXT_UNCHANGED
  active_world_module_ids:
    - WORLD.HALL_ECOLOGY
    - WORLD.UNDERCURRENT_SURFACE
    - WORLD.RUMOR_ECOLOGY
    - WORLD.ARRIVAL_ROUTING
    - WORLD.SPATIAL_VISIBILITY_ACCESS
    - WORLD.SPACE_LIFECYCLE
    - WORLD.IDENTITY_STATUS
    - WORLD.CONTRACT_DEBUT
    - WORLD.EMBODIED_KNOWLEDGE_ECOLOGY
    - WORLD.MARKET_PRESSURE
    - WORLD.CAUSAL_ASSET
    - WORLD.UNDERWORLD_ADMIN
    - WORLD.JIUYOU_MARKET_ECOLOGY
    - WORLD.JIUYOU_MONETARY_LEDGER
    - WORLD.IMPERIAL_CLUB_GOVERNANCE
    - WORLD.TIME_SPACE_DAOIST_INTERFACE
    - WORLD.FIELD_BIAS
    - WORLD.CAUSAL_STORY_CHAIN
    - WORLD.IDENTITY_CLAIM_DYNAMICS
    - WORLD.COLLECTIVE_ATTENTION_FIELD
    - WORLD.RESONANCE_COMPOSITION
    - WORLD.EVENT_HETEROTOPIA
    - WORLD.GTR_PROFESSIONAL_COURTSHIP
  original_ceri_annex: V0.7_EXP_UNCHANGED
  each_module_semantic_use: WHEN_SCENE_RELEVANT
  not_a_per_turn_all_modules_requirement: true
  declaration_vs_execution: DISTINCT
  host_receipt: NONE
  new_event_authority: EXISTING_DOMAIN_ONLY
  no_story_judge: true
  save_writes: NONE
```

> **歷史留存：** 緊接的 `WORLD_DAIL_REGISTRY_V2_1` 22 項表為 V2.1 原文，作來源／回歸，不是本版實際新總數。

## 5.1｜V2.1 World DAIL Registry

```yaml
WORLD_DAIL_REGISTRY_V2_1:
  count: 22
  modules:
    - WORLD.HALL_ECOLOGY
    - WORLD.UNDERCURRENT_SURFACE
    - WORLD.RUMOR_ECOLOGY
    - WORLD.ARRIVAL_ROUTING
    - WORLD.SPATIAL_VISIBILITY_ACCESS
    - WORLD.SPACE_LIFECYCLE
    - WORLD.IDENTITY_STATUS
    - WORLD.CONTRACT_DEBUT
    - WORLD.EMBODIED_KNOWLEDGE_ECOLOGY
    - WORLD.MARKET_PRESSURE
    - WORLD.CAUSAL_ASSET
    - WORLD.UNDERWORLD_ADMIN
    - WORLD.JIUYOU_MARKET_ECOLOGY
    - WORLD.JIUYOU_MONETARY_LEDGER
    - WORLD.IMPERIAL_CLUB_GOVERNANCE
    - WORLD.TIME_SPACE_DAOIST_INTERFACE
    - WORLD.FIELD_BIAS
    - WORLD.CAUSAL_STORY_CHAIN
    - WORLD.IDENTITY_CLAIM_DYNAMICS
    - WORLD.COLLECTIVE_ATTENTION_FIELD
    - WORLD.RESONANCE_COMPOSITION
    - WORLD.EVENT_HETEROTOPIA

  locks:
    - "REGISTRY PRESENCE != BOUND"
    - "BOUND != EXECUTED"
    - "WORLD SEMANTIC DAIL != WORLD FACT"
    - "WORLD DAIL DOES NOT FINAL-RELEASE"
```


# PART C｜CERI LANGUAGE / REGISTER ANNEX
## Embedded CERI V0.7-EXP Full Corpus

```yaml
CERI_ANNEX:
  physical_location: "EMBEDDED IN GUANZHI WORLD DATABASE V2.1-CURRENT"
  component_version: "V0.7-EXP"
  source_sha256: "c647186a0415a60444ae202ee53593106df6c492ba009455f632d6deb99a10a7"
  semantic_role: "LANGUAGE / REGISTER / CORPUS ANNEX"
  world_fact_authority: false
  character_decision_authority: false
  event_authority: false
  consent_authority: false
  relation_authority: false
  knowledge_authority: false
  save_authority: false

  normalization:
    - "CERI ENTRY != WORLD FACT"
    - "CERI CANDIDATE != CHARACTER DECISION"
    - "GENERAL PERIOD REGISTER != ADULT CORPUS UNLOCK"
    - "old embedded peer/runtime names inside CERI lineage are PROVENANCE / COMPATIBILITY ONLY"
    - "embedding CERI into WORLD PACKAGE does not transfer World authority to CERI"
```

### CERI Annex Read Rule

```text
WORLD DATABASE may contain CERI physically.
WORLD CANON and CERI CORPUS remain separate namespaces.

WORLD_CANON.*
!=
CERI.*

CERI source-body inheritance remains CERI lineage.
World V2.0 does not rename CERI V0.7-EXP to World V2.0 semantics.
```

---

## CERI V0.7-EXP SOURCE BODY｜EMBEDDED VERBATIM

# 古典中文時代語域與成人語料提供者 CERI V0.7-EXP
## All-STORY Period Register × Adult Corpus Capability Scoping × Provider Law Position Preserved

```yaml
DOCUMENT:
  title_zh: "古典中文時代語域與成人語料提供者"
  title_en: "Classical Chinese Period Register & Adult Corpus Provider"
  short_id: "CERI"
  version: "V0.7-EXP"
  date: "2026-09-20"
  status: "GM_AUTHORIZED_CURRENT_PROVIDER_SUCCESSOR / ALL-STORY PERIOD REGISTER + ADULT CORPUS SCOPING"

LINEAGE:
  parent:
    file: "成人古典中文語域與語料提供者_CERI_V0.6-EXP_STORY成人語義調用_事件分軸_語義保真_FULL_CORPUS版.md"
    version: "V0.6-EXP"
    sha256: "87f9ba66c4c62a0a0d5b4b7ffd19749de200919bc845ef5e31761782e6146507"
    treatment:
      - "FULL INHERITANCE"
      - "SUPERSEDES ADULT-SEMANTIC-ONLY INVOCATION SCOPE"
      - "PRESERVES FULL CORPUS / PROVENANCE / REGISTER PRECEDENCE"
      - "NO WORLD / CHARACTER / EVENT / CONSENT / SAVE AUTHORITY"

  historical_provider_contract_source:
    file: "成人古典中文語域與語料提供者_CERI_V0.3.1-EXP_AINT2Family接線_Provider法位版.md"
    sha256: "373f7aded514bb3444e58fa651e95b38146fddeddd5c3bfaebdbf61aa34c060d"
    treatment:
      - "PROVIDER CONTRACT / ERA-LOCALE-ROLE REGISTER PROVENANCE"
      - "NOT PARALLEL RUNTIME"

POSITION:
  provider_class: "SCOPED LANGUAGE / REGISTER PROVIDER"
  event_authority: false
  character_authority: false
  consent_authority: false
  relation_authority: false
  knowledge_authority: false
  save_authority: false
  adult_qualification_authority: false

  owns:
    - "period lexical candidate supply"
    - "period syntactic candidate supply"
    - "address / vocative candidate supply"
    - "locale / venue / role register candidates"
    - "character-compatible vocal candidates"
    - "adult body-noun / erotic / bed-language candidates only when scoped mode unlocks them"
    - "source provenance / ambiguity / register drift warnings"
```

> **CERI 從本版起不是「只有成人場才能叫」的 Provider。它首先回答：這個人物、時代、地方、身分、場面，用什麼中文比較像自己；成人語料只是其中一組受 scope 控制的能力。**

# REVISION V0.7-A｜INVOCATION SCOPE DECOUPLING

```yaml
CERI_INVOCATION_SCOPE_V0_7:
  callable_in:
    - "GENERAL STORY"
    - "STORY WITH ADULT SEMANTICS BUT NO ACTIVE ADULT EVENT"
    - "ACTIVE ADULT STORY"

  invocation_modes:

    GENERAL_PERIOD_REGISTER:
      adult_event_required: false
      sexual_semantics_required: false
      purpose:
        - "era-compatible vocabulary"
        - "locale / venue / profession / role register"
        - "address / vocative / politeness level"
        - "period-compatible syntax and discourse shape"
        - "character-native phrasing"
        - "anachronism / register-drift warnings"

    STORY_ADULT_SEMANTICS_ONLY:
      adult_event_required: false
      sexual_semantics_present: true
      purpose:
        - "sex-talk / bawdy joke / erotic taunt / sexual transaction talk"
        - "past-sex talk / explicit desire speech / adult semantic translation"
        - "preserve specific sexual meaning without activating adult event"

    ACTIVE_ADULT_EVENT_REGISTER:
      adult_event_required: true
      purpose:
        - "adult-event narrator / character register composition"
        - "body-noun / vocal / bed-language / erotic syntax candidates"
        - "anti-euphemism / anti-clean-text / anti-default-attractor support"

  locks:
    - "CERI INVOCATION != ADULT EVENT ACTIVATION"
    - "GENERAL_PERIOD_REGISTER != ADULT CORPUS UNLOCK"
    - "CERI INVOCATION != CHARACTER DECISION"
    - "CERI INVOCATION != CONSENT"
    - "CERI INVOCATION != RELATION"
    - "CERI INVOCATION != WORLD FACT"
```

# REVISION V0.7-B｜CAPABILITY-SCOPED RETURN

```yaml
CERI_CAPABILITY_SCOPING_V0_7:

  GENERAL_PERIOD_REGISTER:
    may_return:
      - "period_lexical_candidates"
      - "period_syntactic_candidates"
      - "address_vocative_candidates"
      - "locale_venue_role_register_candidates"
      - "character_voice_compatible_variants"
      - "source_provenance_tags"
      - "ambiguity_warnings"
      - "anachronism_or_register_drift_warnings"

    default_mask:
      - "explicit erotic body-noun bank"
      - "intercourse mechanics bank"
      - "oral-sex bank"
      - "climax / ejaculation bank"
      - "bed-language / erotic-vocal bank"

  STORY_ADULT_SEMANTICS_ONLY:
    unlock:
      - "adult semantic lexical / syntactic candidates needed by the established line"
      - "adult speech-function candidates"
    still_locked:
      - "event creation"
      - "adult-event mechanics not present in semantic payload"

  ACTIVE_ADULT_EVENT_REGISTER:
    unlock:
      - "all lawfully relevant adult register banks"
    remains_scoped_by:
      - "character voice"
      - "era / locale / role"
      - "current event semantic node"
      - "player rendering direction"
      - "actual output constraints if externally established"

  anti_overclaim:
    - "Existing FULL CORPUS is not a complete dictionary of all historical Chinese."
    - "GENERAL_PERIOD_REGISTER may only return candidates supported by provider corpus / host-supplied era-locale context."
    - "Missing historical lexical coverage remains UNKNOWN / provider-insufficient; do not fabricate provenance."
```

# REVISION V0.7-C｜GENERAL PROVIDER CONTRACT

```yaml
CERI_PROVIDER_CONTRACT_V0_7:
  input:
    - "semantic_node_or_general_story_register_need"
    - "narrator_profile"
    - "character_voice_constraints"
    - "era / locale / venue / role register"
    - "public_private_frame"
    - "player_explicit_rendering_request"
    - "requested_capability_scope"

  output:
    ceri_return_ref: "REQUIRED when invoked"
    invocation_mode: "GENERAL_PERIOD_REGISTER | STORY_ADULT_SEMANTICS_ONLY | ACTIVE_ADULT_EVENT_REGISTER"
    may_include:
      - "lexical_candidates"
      - "syntactic_candidates"
      - "vocal_candidates"
      - "body_noun_candidates when scoped"
      - "address_vocative_candidates"
      - "register_drift_warnings"
      - "source_provenance_tags"
      - "ambiguity_warnings"

  precedence:
    1: "HOST CHARACTER CURRENT VOICE"
    2: "HOST CURRENT ERA / LOCALE / ROLE REGISTER"
    3: "CURRENT RELATION / PUBLIC-PRIVATE FRAME"
    4: "PLAYER EXPLICIT RENDERING REQUEST"
    5: "PLAYER ACTION LEXICON AS SOFT SIGNAL"
    6: "NARRATOR PROFILE"
    7: "CERI SOURCE BANK"

  must_not:
    - "invent character desire"
    - "invent consent"
    - "invent adult event"
    - "invent relation"
    - "invent knowledge"
    - "override character voice"
    - "define Host boundary"
```

# REVISION V0.7-D｜RETURN OBJECT

```yaml
CERI_REGISTER_RETURN_V0_7:
  status: "READY when candidates returned"
  must_reference:
    - "ceri_request_ref"
    - "invocation_mode"
    - "requested_capability_scope"
    - "voice / narrator / era-locale context refs supplied by caller"

  proves:
    - "language-provider execution within requested scope"

  does_not_prove:
    - "adult event activation"
    - "character decision"
    - "consent"
    - "relation"
    - "world fact"
```

# SUCCESSION

```yaml
SUCCESSION:
  current_provider: "CERI V0.7-EXP"
  retired_from_active_runtime:
    - "成人古典中文語域與語料提供者_CERI_V0.6-EXP_STORY成人語義調用_事件分軸_語義保真_FULL_CORPUS版.md"
  old_versions_standing: "PROVENANCE / ROLLBACK / REGRESSION"
  no_dual_runtime: true
```

---

# INHERITED PARENT BODY｜CERI V0.6-EXP FULL CORPUS

> 以下完整繼承 V0.6。涉及「何時可調用 CERI」「一般 STORY 是否可調用」「GENERAL_PERIOD_REGISTER」「成人語料 bank 是否解鎖」時，以 V0.7 前置條款為現行語義；V0.6 及更早版本的 corpus、provenance、anti-euphemism、anti-vulgarization、人物聲音優先與成人語義保真規則全部保留。

# 成人古典中文語域與語料提供者 CERI V0.6-EXP
## STORY Adult-Semantic Invocation × Adult-Language/Event Separation × Semantic Preservation × Full V0.5 Corpus Inheritance

```yaml
DOCUMENT:
  title_zh: "成人古典中文語域與語料提供者"
  title_en: "Classical Erotic Register & Corpus Provider"
  short_id: "CERI"
  version: "V0.6-EXP"
  date: "2026-09-19"
  status: "GM_AUTHORIZED_CURRENT_PROVIDER_SUCCESSOR / STORY-SEMANTIC INVOCATION EXPANSION"

LINEAGE:
  parent:
    file: "成人古典中文語域與語料提供者_CERI_V0.5-EXP_淫詞行為_EroticSpeechSignature_邊界床話轉譯_FULL_CORPUS版.md"
    version: "V0.5-EXP"
    sha256: "6434bf7943a99f360b23c5daa6fe969d2eaeec962ec8d68235fb5c3b7ba1e8bd"
    treatment: "FULL INHERITANCE + D5 STORY ADULT-SEMANTIC INVOCATION PROMOTION"

CURRENT_HOST_METHOD:
  file: "觀止青樓_導演心法_V2.3_FULL_成人場景切換_優先模組清單_環境債務上游化_正式整合版.md"
  version: "V2.3"

POSITION:
  event_authority: false
  character_authority: false
  consent_authority: false
  relation_authority: false
  knowledge_authority: false
  save_authority: false
```

> **CERI 回答語言，不回答事件是否成立。成人語義可以存在於普通 STORY；成人事件不必因此啟動。**

---

# REVISION V0.6-A｜Invocation Scope Expansion

```yaml
CERI_INVOCATION_SCOPE_V0_6:
  host_may_invoke_when:
    - "adult event ACTIVE and erotic/register composition is materially relevant"
    - "adult event INACTIVE but explicit sexual semantic content is present in STORY"
    - "sex-talk / bawdy joke / erotic taunt / sexual transaction talk / past-sex talk / explicit desire speech requires character-native register"

  invocation_modes:
    STORY_ADULT_SEMANTICS_ONLY:
      adult_event_required: false
      aint_required: false
      input_owner: "Host / Director Heart"

    ACTIVE_ADULT_EVENT_REGISTER:
      adult_event_required: true
      aint_or_heart_adult_method_context: true

  locks:
    - "CERI INVOCATION != ADULT EVENT ACTIVATION"
    - "CERI INVOCATION != CONSENT"
    - "CERI INVOCATION != ACCESS"
    - "CERI INVOCATION != RELATION"
```

# REVISION V0.6-B｜Semantic Preservation Before Register Translation

```yaml
CERI_SEMANTIC_PRESERVATION:
  must_preserve_from_host_payload:
    - "sexual act category when explicitly established in speech semantics"
    - "target / referent"
    - "identity/status/power meaning materially carried by the line"
    - "speech function: desire / tease / mock / transaction / humiliation / boast / threat / joke / boundary negotiation"

  may_transform:
    - "lexical directness"
    - "classical / street / refined / vulgar register"
    - "syntax and vocative according to character voice"

  forbidden:
    - "erase specific sexual meaning into generic conquest/romance language"
    - "force every character to mirror player vulgarity"
    - "invent event facts from sexual vocabulary"
```

# REVISION V0.6-C｜Provider Return Evidence

```yaml
CERI_PROVIDER_RETURN_V0_6:
  when_invoked: true
  output_ref: "CERI_EROTIC_SPEECH_TRANSLATION"
  must_reference:
    - "host semantic payload / character voice signature"
    - "invocation_mode"
  status: "READY when candidates returned to Host"
  lock:
    - "Provider return proves language-provider execution only; it proves no consent/event/relation result."
```

# REVISION V0.6-D｜Current Successor Compatibility

```yaml
CERI_CURRENT_INTERFACE:
  host_role: "GUANZHI_DIRECTOR_HEART_CURRENT"
  current_host_version: "V2.3"
  stable_provider_role: "CERI_CURRENT"
  rule:
    - "Inherited references to AINT/Heart version numbers are compatibility provenance unless current binding says otherwise."
    - "Current lawful successor may invoke CERI through the inherited provider interface."
```

---

# INHERITED PARENT BODY｜CERI V0.5-EXP FULL CORPUS

> 以下完整繼承 V0.5-EXP 語料、speech-function、voice-signature、boundary translation 與 corpus provenance。若父版『只為已成立成人 semantic node』的狹義表述與本版 V0.6 invocation scope 衝突，**以 V0.6 為準**；其餘全部繼承。

# 成人古典中文語域與語料提供者 CERI V0.5-EXP
# Erotic Speech as Action × Character Erotic-Speech Signature × Erotic Boundary Translation

```yaml
DOCUMENT:
  title_zh: "成人古典中文語域與語料提供者"
  title_en: "Classical Erotic Register & Corpus Provider"
  short_id: "CERI"
  version: "V0.5-EXP"
  date: "2026-09-15"
  status: "GM_AUTHORIZED_CURRENT_PROVIDER_SUCCESSOR / EROTIC_SPEECH_ACTION"

REVISION_LINEAGE:
  parent:
    file: "成人古典中文語域與語料提供者_CERI_V0.4-EXP_床話作曲_SpeechFunction_詞彙近因_人物粗話簽名_FULL_CORPUS版.md"
    version: "V0.4-EXP"
    sha256: "0c34d51060c4d192ac322dcdee29b50984e5989bdd7a19d5c97a3aa23018ccf3"
    treatment: "FULL INHERITANCE + EROTIC SPEECH ACTION / SIGNATURE / BOUNDARY TRANSLATION"

POSITION:
  event_authority: false
  character_authority: false
  consent_authority: false
  relation_authority: false
  knowledge_authority: false
  save_authority: false

NEW_DISTINCTIONS:
  - "PROFANITY != EROTIC SPEECH"
  - "DIRTY WORD != AROUSING SPEECH FUNCTION"
  - "EROTIC SPEECH != CONSENT DECISION"
  - "AUDIT SEMANTICS != AUDIT-SHAPED DIALOGUE"
  - "VOCAL CAPACITY != CHARACTER VOICEPRINT"
```

# V0.5-A｜CHARACTER EROTIC-SPEECH SIGNATURE

```yaml
CHARACTER_EROTIC_SPEECH_SIGNATURE:
  source_priority:
    - "HOST_CURRENT_CHARACTER_VOICE"
    - "ROUTE_CONFIRMED_BED_SPEECH_EVIDENCE"
    - "CURRENT_RELATION / PUBLIC-PRIVATE FRAME"
    - "SOURCE_ERA_ROLE_REGISTER"
    - "PLAYER_EXPLICIT_RENDER_DIRECTION"
    - "CERI_SOURCE_BANK"

  fields_if_known:
    erotic_speech_frequency:
    erotic_speech_initiative:
    directness:
    body_noun_directness:
    self_desire_disclosure_tendency:
    partner_body_focus_tendency:
    praise_tendency:
    teasing_tendency:
    provocation_tendency:
    begging_tendency:
    imperative_tendency:
    fantasy_cue_tendency:
    erotic_mockery_tendency:
    erotic_vocative_tendency:
    boundary_negotiation_style:
    classical_erotic_tolerance:
    street_vulgar_tolerance:
    metaphor_tolerance:
    silence_under_intensity:
    fragment_under_intensity:

  hard_locks:
    - "CHARACTER_EROTIC_SPEECH_SIGNATURE != CHARACTER_PERSONALITY_CREATION"
    - "PROFANITY_SIGNATURE != EROTIC_SPEECH_SIGNATURE"
    - "ONE EROTIC LINE != PERMANENT BED-SPEECH IDENTITY"
    - "SOURCE CORPUS != NPC VOICE"
    - "UNKNOWN FIELDS STAY UNKNOWN"
```

# V0.5-B｜EROTIC SPEECH FUNCTION ROUTER

```yaml
EROTIC_SPEECH_FUNCTION_ROUTER:
  functions:
    - "AROUSE"
    - "TEASE"
    - "PROVOKE"
    - "PRAISE"
    - "DIRECT"
    - "BEG"
    - "SELF_DISPLAY"
    - "FANTASY_CUE"
    - "MOCK"
    - "VOCATIVE"
    - "CALLBACK_CURRENT_ACTION"
    - "CALLBACK_PRIOR_LINE"
    - "NEGOTIATE_ACCESS"
    - "SET_LIMIT"
    - "OFFER_ACCESS"
    - "COUNTEROFFER"
    - "EROTIC_REFUSAL"
    - "EROTIC_PERMISSION"
    - "EROTIC_WITHDRAWAL"

  composition_rule:
    - "First decide what the speech is doing; then choose how explicit, vulgar, classical, tender, mocking or brief it sounds."
    - "Multiple functions may coexist in one line only when character/cause supports it."
    - "Do not use random profanity as a substitute for erotic function."
```

# V0.5-C｜EROTIC SPEECH AS ACTION

```yaml
EROTIC_SPEECH_AS_ACTION:
  definition:
    - "Erotic speech may itself be an interaction action rather than narration pasted over mechanics."

  possible_targets:
    - "attention"
    - "expectation"
    - "anticipation"
    - "embarrassment/shamelessness frame"
    - "challenge"
    - "fantasy cue"
    - "praise/validation"
    - "local action coordination"
    - "boundary negotiation"

  authority_lock:
    - "CERI can provide candidate lines/functions."
    - "CERI cannot declare the target person's hidden arousal, fantasy, consent, love, trust or climax."
    - "Observable reaction remains owned by the world/character layer."
```

# V0.5-D｜EROTIC BOUNDARY TRANSLATION

```yaml
EROTIC_BOUNDARY_TRANSLATION:
  input_semantics_from_host:
    - "REQUEST"
    - "PERMISSION"
    - "LIMIT"
    - "OFFER_ACCESS"
    - "COUNTEROFFER"
    - "REFUSAL"
    - "WITHDRAWAL"

  output:
    - "character-native erotic dialogue candidates"
    - "register-matched boundary speech"
    - "short/fragment forms if vocal capacity is low"

  hard_locks:
    - "CERI DOES NOT CHANGE THE INPUT SEMANTIC CLASS"
    - "Erotic wording may not broaden scope."
    - "Playful wording may not convert refusal into permission."
    - "Body response may not convert refusal/limit into permission."
    - "Audit taxonomy must not be mechanically spoken by characters unless the character would genuinely use such language."

  principle:
    - "AUDIT INWARD; CHARACTER SPEECH OUTWARD"
```

# V0.5-E｜PLAYER-CHARACTER EROTIC SPEECH COMPOSITION

```yaml
PLAYER_CHARACTER_EROTIC_SPEECH_COMPOSITION:
  availability: "ONLY WHEN HOST/HEART EXPOSES PLAYER_EROTIC_SPEECH_PARTICIPATION == ALLOWED"

  may_generate:
    - "teasing"
    - "dirty talk"
    - "current-action questions"
    - "local coordination"
    - "praise / mockery / vocative"
    - "non-binding immediate erotic speech"

  must_not_generate:
    - "major commitment"
    - "relationship declaration"
    - "payment/contract/property decision"
    - "secret disclosure"
    - "irreversible promise"
    - "new player consent decision beyond current authored scope"
    - "player hidden belief/emotion as fact"

  register_source:
    - "established player-character speech evidence"
    - "current route voice"
    - "current interaction function"
```

# V0.5-F｜VOCAL CAPACITY COUPLING

```yaml
VOCAL_CAPACITY_COUPLING:
  inputs:
    - "vocal_capacity"
    - "attention_capacity"
    - "intensity_speech_state"
    - "character_erotic_speech_signature"

  behavior:
    high_capacity: "full erotic composition remains available"
    medium_capacity: "shorter teasing/requests/praise/callbacks"
    low_capacity: "fragments, vocatives, profanity anchors, repeated request words, silence"

  hard_locks:
    - "LOW CAPACITY != GENERIC MOAN TEMPLATE"
    - "LOW CAPACITY != LOSS OF CHARACTER IDENTITY"
    - "HIGH EROTIC-SPEECH SKILL DOES NOT REQUIRE CONTINUOUS TALKING AT PEAK INTENSITY"
```

# V0.5-G｜MATERIAL-LINKED ADULT LEXICON

```yaml
MATERIAL_LINKED_LEXICON:
  rule:
    - "When Host exposes established material/fluid state, CERI may supply direct, classical-erotic, neutral or vulgar lexical candidates appropriate to narrator/character register."
    - "Fluid words are material realization candidates, not mandatory erotic decorations."
    - "Do not sanitize an established specific material into generic wetness merely because the adult register is salient."
```

# V0.5-H｜PROVIDER CONTRACT DELTA

```yaml
CERI_V0_5_PROVIDER_DELTA:
  new_inputs:
    - "character_erotic_speech_signature_if_host_exposes"
    - "erotic_speech_function_target_if_host_exposes"
    - "erotic_boundary_semantic_payload_if_host_exposes"
    - "player_erotic_speech_participation_if_host_exposes"
    - "intensity_speech_state_if_host_exposes"
    - "material_fluid_state_if_host_exposes"

  new_outputs:
    - "erotic_speech_function_candidates"
    - "character_erotic_speech_candidates"
    - "erotic_boundary_translation_candidates"
    - "player_character_erotic_speech_candidates"
    - "intensity_compressed_speech_candidates"
    - "material_linked_lexical_candidates"

  unchanged_must_not:
    - "decide consent"
    - "decide relation"
    - "invent world facts"
    - "create orgasm/ejaculation/event fact"
    - "overwrite character identity"
    - "write SAVE"
```

# V0.5-I｜REGRESSION

```yaml
CERI_V0_5_REGRESSION:
  C05-T01_PROFANITY_VS_EROTIC:
    fail_if: "all erotic speech is reduced to swearing/body nouns"
  C05-T02_CHARACTER_DIFFERENTIATION:
    fail_if: "multiple women share the same erotic speech strategy after names are swapped"
  C05-T03_BOUNDARY_TRANSLATION:
    expect: "precise REQUEST/PERMISSION/LIMIT/REFUSAL/WITHDRAWAL semantics in character-native bed speech"
  C05-T04_NO_AUDIT_DIALOGUE:
    fail_if: "characters mechanically recite governance/consent taxonomy without character cause"
  C05-T05_INTENSITY_COMPRESSION:
    expect: "speech shortens with capacity while voice signature survives"
  C05-T06_PLAYER_SPEECH:
    expect: "player-character can speak erotically in-scene without CERI inventing major decisions"
  C05-T07_MATERIAL_LEXICON:
    expect: "established fluid/material state can remain lexically visible at selected register"
```

> **最短句：淫詞不是髒話配額；它是人物用自己的語言做事。邊界也可以是床話，但意思不能被床話改掉。**

---

# INHERITED PARENT BODY｜CERI V0.4-EXP

> 以下完整繼承 parent；若與本版前置 override 衝突，以本版為準。

# 成人古典中文語域與語料提供者 CERI V0.4-EXP
# Classical Erotic Register & Corpus Provider

## Register Provider × Dirty-Speech Composition × Speech-Function Routing × Lexical Recency × Corpus Provenance × AINT V2 Interface

```yaml
DOCUMENT:
  title_zh: "成人古典中文語域與語料提供者"
  title_en: "Classical Erotic Register & Corpus Provider"
  short_id: "CERI"
  version: "V0.4-EXP"
  date: "2026-09-07"
  document_type: "OPTIONAL_CLASSICAL_CHINESE_ADULT_REGISTER_PROVIDER"
  status: "GM_AUTHORIZED_PROVIDER_SUCCESSOR_CANDIDATE_PENDING_REGRESSION"

REVISION_LINEAGE:
  parent:
    file: "成人古典中文語域與語料提供者_CERI_V0.3-EXP_AINT2_RegisterProvider_FULL_CORPUS版.md"
    version: "V0.3-EXP"
    sha256: "3f704605037eefa4ab83573533fe85e57fd41bcff5624c238be033ce7d2c3ae2"
    treatment: "FULL_INHERITANCE_PLUS_SPEECH_COMPOSITION_AND_RECENCY_CONTROL"

  historical_parent:
    file: "成人古典語域與床上互動外掛_CERI_V0.2-EXP_FULL_CORPUS_金瓶梅肉蒲團_語域長距離痛感整合版.md"
    version: "V0.2-EXP"
    treatment: "REGISTER_AND_CORPUS_INHERITANCE"

  aint_target:
    file: "成人親密敘事模組_AINT_V2.1-RC3-FULL_合法域探索_反過早拒絕_反文字潔癖_反偽造宿主邊界_21卡版.md"
    version: "V2.1-RC3-FULL"
    treatment: "OPTIONAL_REGISTER_PROVIDER / REGISTER_AND_COMPOSITION_CANDIDATE_SOURCE"

  guanzhi_target:
    file: "觀止青樓_主系統_V14.2-FULL_LIHUO3.5.1_DAIL2成人路由_HBCProvider_KAIROSActiveTest版.md"
    version: "V14.2-FULL"
    treatment:
      - "COMPATIBLE_OPTIONAL_PROVIDER"
      - "NO_GUANZHI_MAIN_VERSION_BUMP_REQUIRED_FOR_CANDIDATE TEST"
      - "CURRENT MANIFEST PROMOTION REQUIRES POST-REGRESSION GM CONFIRMATION"

  structural_promotion:
    moved_to_aint_v2:
      - "PAIN CHANNEL SEPARATION -> PAIN CHANNEL LOCALITY"
      - "NEXT-STEP AUTHORSHIP"
      - "TRANSITION CAUSALITY"
      - "LONG-HORIZON DEGRADATION -> LONG-HORIZON INTEGRITY"

POSITION:
  event_authority: false
  character_authority: false
  consent_authority: false
  relation_authority: false
  knowledge_authority: false
  save_authority: false

  owns:
    - lexical_candidate_supply
    - syntactic_candidate_supply
    - body_noun_register
    - vocal_and_bed_language_candidates
    - speech_function_candidate_supply
    - dirty_speech_composition
    - character_profanity_signature_alignment
    - lexical_recency_tracking
    - functional_repetition_tracking
    - repetition_cause_check
    - fragment_syntax_candidates
    - current_action_callback_candidates
    - corpus_provenance
    - source_disambiguation
    - anti_euphemism_drift_signal
    - anti_vulgarization_drift_signal
    - anti_default_attractor_signal
```

> **CERI 不再負責「性愛互動怎麼運作」；它只回答「已成立的成人互動，在古典中文語域裡有哪些可用語言與構成」。**

---

# 0A｜V0.4 根問題：語料存在，不等於語言真的活起來

V0.3 已把詞庫、來源、Register 與通用互動結構分離；本輪實跑暴露的新問題不是「沒有詞」，而是：

```text
LEXICON EXISTS
!=
LEXICON MANIFESTS

LARGE CORPUS
!=
DIVERSE CHARACTER SPEECH

DIRTY INTENSITY
!=
PROFANITY IDENTITY

NOVELTY
!=
RARE-WORD DUMP

REPETITION
!=
ALWAYS FAILURE

REPETITION WITH CHARACTER / ACTION CAUSE
!=
DEFAULT ATTRACTOR REPETITION
```

V0.4 因此只新增**語言作曲層**，不把 CERI 重新變成成人事件 Runtime。

最短式：

> **先決定這句話在做什麼，再決定它用多髒、多古、多直的詞。**

以及：

> **人物可以重複；模型不能因為偷懶而重複。**

## 0A.1｜V0.4 升級範圍

```yaml
CERI_V0_4_UPGRADE_SCOPE:
  adds:
    - "SPEECH FUNCTION ROUTER"
    - "CHARACTER PROFANITY SIGNATURE ALIGNMENT"
    - "LEXICAL RECENCY LEDGER"
    - "FUNCTIONAL REPETITION LEDGER"
    - "REPETITION CAUSE CHECK"
    - "FRAGMENT / BROKEN-SPEECH SYNTAX"
    - "CURRENT-ACTION CALLBACK COMPOSITION"
    - "DEFAULT ATTRACTOR DETECTION"
    - "REGISTER DIVERSITY COMPOSITION"

  does_not_add:
    - "adult event authority"
    - "character decision authority"
    - "consent authority"
    - "relation authority"
    - "knowledge authority"
    - "world fact authority"
    - "SAVE authority"
    - "AINT interaction mechanics ownership"
    - "Host boundary authority"

  full_corpus:
    inherited_from_v0_3: true
    rewritten: false
```

---

# 0｜V0.3 收口決定（完整繼承）

V0.2 同時承擔兩種工作：

```text
A. 通用成人互動結構
B. 古典中文語域／語料
```

V0.3 正式拆開：

```text
通用互動結構
→ AINT V2

古典中文語域／語料
→ CERI V0.3
```

因此 CERI 可以被 AINT 調用，也可以被其他具相容 Provider Contract 的成人 Runtime 調用。

---

# 1｜Provider Contract

```yaml
CERI_PROVIDER_CONTRACT:
  provider_family: "CERI_CLASSICAL_CHINESE_REGISTER"
  exact_version_required: false

  input:
    - semantic_node
    - narrator_profile
    - character_voice_constraints
    - locale_or_era_register
    - player_explicit_rendering_request
    - body_noun_register_hint
    - vocal_function
    - source_density_preference
    - speech_function_target_if_host_or_aint_exposes
    - recent_lexical_window_if_available
    - recent_speech_function_window_if_available
    - repetition_cause_if_known
    - current_action_callback_context_if_available
    - character_profanity_signature_if_host_exposes
    - vocal_capacity
    - attention_capacity_if_host_exposes

  output:
    - lexical_candidates
    - syntactic_candidates
    - vocal_candidates
    - body_noun_candidates
    - speech_function_candidates
    - fragment_syntax_candidates
    - action_callback_candidates
    - lexical_recency_warnings
    - functional_repetition_warnings
    - default_attractor_warnings
    - source_provenance_tags
    - ambiguity_warnings
    - register_drift_warnings

  must_not:
    - "決定人物想不想"
    - "決定人物是否同意"
    - "建立高潮／關係／成人事件事實"
    - "改寫人物人格或知識"
    - "把來源文本行為正當性搬進宿主"
    - "直接寫 SAVE"
```

---

# 2｜Register 優先序

```yaml
CERI_REGISTER_ROUTER:
  precedence:
    1: "HOST CHARACTER CURRENT VOICE"
    2: "HOST CURRENT ERA / LOCALE / ROLE REGISTER"
    3: "CURRENT RELATION / PUBLIC-PRIVATE FRAME"
    4: "PLAYER EXPLICIT RENDERING REQUEST"
    5: "PLAYER ACTION LEXICON AS SOFT SIGNAL"
    6: "NARRATOR PROFILE"
    7: "CERI SOURCE BANK"

  locks:
    - "人物自己的聲音永遠優先於詞庫。"
    - "玩家現代詞不自動賦予 NPC 現代知識。"
    - "來源語料是候選，不是模板。"
    - "古典詞彙不自動證明時代真實性。"
```

---

# 3｜BODY NOUN REGISTER

```yaml
BODY_NOUN_REGISTER:
  FORMAL_ANATOMICAL:
    examples: ["乳房", "乳頭"]

  NEUTRAL_NARRATIVE:
    examples: ["胸", "胸前", "胸部"]

  CLASSICAL_EROTIC:
    source_examples: ["酥胸", "香乳", "乳峰", "肉峰"]

  COLLOQUIAL_BODY:
    examples: ["胸脯", "屁股"]

  VULGAR_BODY:
    examples: ["奶子", "奶頭", "雞巴"]
```

`奶子` 作乳房義可以是現代／低俗宿主 register，但不得因此偽稱是《金瓶梅》乳房語料。

---

# 4｜Narrator / Character / Player 不同步

```text
PLAYER INPUT REGISTER
        ↓ soft / explicit style signal
NARRATOR REGISTER

CHARACTER VOICE
        ↓ independent host authority
NPC SPEECH

CERI SOURCE BANK
        ↓ candidate resource only
LEXICAL / SYNTACTIC OPTIONS
```

人物可以乾淨而旁白粗；人物可以粗而旁白較中性。
CERI 不強迫同步。

---

# 5｜Register Drift

```yaml
REGISTER_DRIFT:
  ANTI_EUPHEMISM_DRIFT:
    "已建立的直接／低 register 不得整段無因果被洗成抽象高雅隱喻。"

  ANTI_VULGARIZATION_DRIFT:
    "已建立的文雅／克制 register 不得整段無因果被成人詞庫粗俗化。"

  rule:
    - "單次換詞不是 FAIL。"
    - "看整段 register 是否被來源詞庫拖走。"
```

---

# 6｜Composition Interface

CERI 不決定成人節點；它讀取 AINT／Host 已建立的 semantic node。

```yaml
CERI_COMPOSITION_INPUT:
  body_relation:
  active_body_parts:
  action_relation:
  rhythm:
  support_and_balance:
  pain_or_fatigue_if_host_exposes:
  vocal_capacity:
  attention_capacity_if_host_exposes:
  character_speech_function:
  requested_speech_function_if_any:
  character_profanity_signature_if_host_exposes:
  recent_lexical_window_if_available:
  recent_speech_function_window_if_available:
  repetition_cause_if_known:
  current_action_callback_context_if_available:
  spatial_constraint:
  residue_from_prior_nodes:
  narrator_register:
  body_noun_register:
```

> **先有事件關係，再選詞。**

---

# 6A｜SPEECH FUNCTION ROUTER｜先判斷「這句在做什麼」

CERI 不先問「要不要塞粗話」，而先取得一個或多個 speech-function candidate。

```yaml
CERI_SPEECH_FUNCTION_ROUTER:
  candidate_functions:
    - VOCATIVE_INTIMACY
    - VOCATIVE_TAUNT
    - TEASE
    - MOCK
    - CHALLENGE
    - PRAISE
    - COMPLAINT
    - CURSE_PLAYFUL
    - CURSE_HOSTILE_IF_HOST_ESTABLISHES
    - SELF_MOCK
    - REQUEST_SLOWER
    - REQUEST_FASTER
    - REQUEST_LIGHTER
    - REQUEST_STRONGER
    - LOCAL_STOP
    - LOCAL_HOLD
    - CONTINUE
    - REENTRY
    - POSITION_COORDINATION
    - SUPPORT_COORDINATION
    - CLAIM_ATTENTION
    - HANDOFF_ATTENTION
    - CALL_NAME
    - CHANGE_VOCATIVE
    - CALLBACK_PRIOR_LINE
    - CALLBACK_CURRENT_ACTION
    - AFTERCARE_OR_REST
    - NO_SPEECH

  rules:
    - "單一句可同時有兩個功能，例如 TEASE + REQUEST_FASTER。"
    - "同一功能可以用乾淨、文雅、市井、粗俗、古典艷稱等不同 register 顯影。"
    - "粗俗不是獨立功能；粗俗只是一種可能的 register。"
    - "NO_SPEECH 是合法候選，不要求每個節點都有人說話。"
```

固定式：

```text
SPEECH FUNCTION
→ CHARACTER / ERA / RELATION REGISTER
→ VOCAL CAPACITY
→ WORD / SYNTAX CANDIDATES
```

而不是：

```text
DIRTY REQUEST
→ RANDOM PROFANITY
```

---

# 6B｜CHARACTER PROFANITY SIGNATURE｜人物粗話簽名

本層不是替人物新增人格，而是把 Host 已經建立的 voice evidence 轉成**當前可用的粗話構成限制**。

```yaml
CHARACTER_PROFANITY_SIGNATURE:
  source_priority:
    - HOST_CURRENT_CHARACTER_VOICE
    - ROUTE_CONFIRMED_SPEECH_EVIDENCE
    - SOURCE_ERA_ROLE_REGISTER
    - CURRENT_RELATION_PUBLIC_PRIVATE_FRAME
    - PLAYER_EXPLICIT_RENDER_DIRECTION
    - CERI_SOURCE_BANK

  fields_if_known:
    profanity_density:
    direct_body_noun_tolerance:
    insult_direction:
    teasing_vs_hostile_balance:
    affection_mixed_with_insult:
    imperative_tendency:
    vocative_tendency:
    fragment_tendency:
    self_mock_tendency:
    metaphor_tolerance:
    archaic_erotic_tolerance:
    modern_vulgar_tolerance:
    silence_tendency:

  unknown_rule:
    - "沒有證據的欄位保持 UNKNOWN。"
    - "UNKNOWN 不用平均人物模板補滿。"

  hard_locks:
    - "CHARACTER_PROFANITY_SIGNATURE != CHARACTER_PERSONALITY_CREATION"
    - "ONE_DIRTY_LINE != PERMANENT_DIRTY_PERSONALITY"
    - "PLAYER_DIRTY_REQUEST != NPC_DIRTY_IDENTITY"
    - "SOURCE_CORPUS != NPC_VOICE"
```

CERI 可以回傳：

```text
這句話對這個人物：
- register 合拍
- register 偏離
- 需要更短
- 需要更市井
- 需要更克制
- 需要少說
```

但不能回傳：

```text
「她其實就是一個愛說髒話的人。」
```

---

# 6C｜LEXICAL RECENCY LEDGER｜詞彙近因帳

問題不是「同一詞絕不能重複」，而是要分辨：

```text
人物真的在重複
vs
模型掉回最容易的詞
```

```yaml
LEXICAL_RECENCY_LEDGER:
  scope:
    default: "CURRENT_MANIFESTATION_WINDOW"
    cross_scene_persistence: false
    save_persistence: false

  tracks:
    - high_salience_body_nouns
    - high_salience_action_verbs
    - profanity_anchors
    - vocatives
    - repeated_imperatives
    - repeated_sentence_frames

  on_repetition:
    check_cause_first: true

  valid_repetition_causes:
    - CHARACTER_HABIT_ALREADY_ESTABLISHED
    - DELIBERATE_REFRAIN
    - MOCKING_ECHO
    - CALLBACK_PRIOR_LINE
    - ESCALATING_CHALLENGE
    - VOCAL_CAPACITY_COLLAPSE
    - LOCAL_INSTRUCTION_MUST_REPEAT
    - RHYTHMIC_OR_INTERACTION_CAUSE
    - EXPLICIT_PLAYER_SELF_SPEECH

  if_cause_exists:
    treatment: "ALLOW / MAY EVEN STRENGTHEN"

  if_no_cause_and_default_attractor_detected:
    treatment:
      - "PENALIZE CURRENT TOKEN/FRAME"
      - "REOPEN CANDIDATE SET"
      - "TRY DIFFERENT SPEECH FUNCTION OR SYNTAX BEFORE RARE SYNONYM"

  hard_rule:
    - "RECENCY PENALTY != BAN"
    - "REPETITION != FAILURE"
    - "NOVELTY != FORCED SYNONYM SWAP"
```

例如，若一個節點反覆掉回同一個高顯著粗俗器官詞或同一個「快點／再來」句型，CERI 應先問：

> **這次重複有角色／動作原因嗎？**

沒有，才重開候選。

---

# 6D｜FUNCTIONAL REPETITION LEDGER｜功能重複也要看

只換詞但一直做同一件事，仍然是語言貧乏。

```yaml
FUNCTIONAL_REPETITION_LEDGER:
  tracks:
    - recent_speech_functions
    - recent_function_pairings
    - recent_question_command_patterns
    - repeated_vocative_plus_command_frame

  fail_pattern_examples:
    - "每一句都是 REQUEST_FASTER，只換同義詞。"
    - "每一句都是 CURSE_PLAYFUL，只換罵詞。"
    - "每一句都是 CALL_NAME + COMMAND。"
    - "每個人物都被壓成同一種 TEASE。"

  response:
    - "優先重新評估人物當下真正需要的 speech function。"
    - "若人物合理地持續同一功能，保留，不為多樣性硬換。"
```

固定式：

```text
LEXICAL DIVERSITY
without
FUNCTIONAL DIVERSITY
=
COSMETIC VARIATION
```

---

# 6E｜FRAGMENT / BROKEN-SPEECH SYNTAX｜語言容量不是固定的

人物在成人場景中不必每次完整說明自己。

```yaml
CERI_FRAGMENT_SYNTAX:
  candidate_shapes:
    - FULL_SENTENCE
    - SHORT_CLAUSE
    - IMPERATIVE_FRAGMENT
    - VOCATIVE_ONLY
    - VOCATIVE_PLUS_FRAGMENT
    - INTERRUPTED_SENTENCE
    - SELF_CORRECTION
    - MOCKING_ECHO
    - REPEATED_SHORT_WORD
    - NAME_ONLY
    - BREATH_BROKEN_FRAGMENT
    - NO_SPEECH

  routing_inputs:
    - vocal_capacity
    - attention_capacity_if_host_exposes
    - current_speech_function
    - current_character_voice
    - current_relation_frame

  locks:
    - "LOW_VOCAL_CAPACITY != MANDATORY_MOANING"
    - "HIGH_LOAD != AUTOMATIC_LONG_CONFESSION"
    - "BROKEN_SPEECH != PRIVATE_STATE_PROOF"
    - "NO_SPEECH != NO_REACTION"
```

語言容量下降時，可以變短、斷裂、改成稱呼或不說；但不能把所有人物都生成成同一套喘／顫／碎字模板。

---

# 6F｜CURRENT-ACTION CALLBACK｜床上話要咬住當前事件

CERI 的創意優先來自**當前事件關係**，而不是罕見淫詞。

```yaml
CURRENT_ACTION_CALLBACK:
  may_read_if_exposed:
    - current_action_relation
    - recent_action_change
    - support_or_position_change
    - local_boundary_change
    - prior_line_being_answered
    - attention_shift
    - fatigue_or_rest_state

  may_generate:
    - "對當前動作的要求"
    - "對剛才變化的嘲笑／抱怨／稱讚"
    - "對對方前一句的反擊或模仿"
    - "對位置／支撐的簡短協調"
    - "對局部停、慢、續、換的直接語句"

  may_not:
    - "創造 Host 未建立的 mechanics"
    - "把語句反向升格成同意／關係／高潮／事件事實"
    - "為了用一句漂亮床話而強迫世界改位"
```

最短式：

> **床上話不是貼在場景上的字幕；它應該被正在發生的事咬住。**

---

# 6G｜REGISTER DIVERSITY COMPOSITION｜創意從組合來，不從怪詞來

```yaml
REGISTER_DIVERSITY_COMPOSITION:
  axes:
    - SPEECH_FUNCTION
    - BODY_NOUN_REGISTER
    - ACTION_VERB_CLASS
    - VOCATIVE
    - SYNTAX_SHAPE
    - DIRECTNESS
    - PROFANITY_DENSITY
    - HUMOR_OR_TAUNT
    - VOCAL_CAPACITY
    - ACTION_CALLBACK
    - SOURCE_DENSITY

  rule:
    - "不是每句都必須換全部軸。"
    - "至少優先確認是否因 Default Attractor 而只剩一兩個高顯著詞／句型。"
    - "若人物本身語彙刻意狹窄，可以狹窄；重點是有角色原因。"
    - "若角色聲音需要新鮮感，先換 speech function / syntax / callback，再考慮罕見同義詞。"
```

反模板：

```text
雞巴 → 陽物 → 麈柄 → 玉莖
```

如果只是機械輪轉，仍然是 FAIL。

真正的多樣性應該更像：

```text
不同功能
+
不同句法
+
不同稱呼
+
不同對當前事件的回應方式
+
必要時才換 body/action noun
```

---

# 6H｜DEFAULT ATTRACTOR DETECTION｜高顯著詞吸引子

```yaml
DEFAULT_ATTRACTOR_DETECTION:
  observable_signals:
    - "同一高顯著粗俗詞在無人物原因下反覆搶佔候選。"
    - "不同人物只剩同一套罵語與催促。"
    - "每次強度提高都退回同一兩個動詞。"
    - "Corpus 明明有多種功能與句法，生成卻只用最熟悉的現代粗口。"

  response:
    - "標記 MODEL_DEFAULT_ATTRACTOR_CANDIDATE"
    - "不把它說成 hidden-state 觀測"
    - "重開 speech-function / syntax / register candidates"
    - "必要時向上游回報 generation-diversity degradation signal"

  may_not:
    - "自行調用 LIHUO Main"
    - "把 attractor 判定寫成角色人格"
    - "為了避開 attractor 強塞不合時代的罕詞"
```

---

# 6｜FULL CORPUS 抽取方法與重要校正

本版不是把全文所有二字詞倒進詞庫，而是做「成人顯影語義域的全書掃描」：

1. 以兩書全文（GB18030 解碼）為 corpus；
2. 逐書掃描事件詞、器官詞、動作詞、聲音詞、床上話、姿勢、空間與高潮／餘波詞；
3. 以 exact substring raw hits 建索引；
4. 對高歧義詞另外做人讀語境校正；
5. `raw hits != sexual semantic hits`，原始計數只用來標示來源存在與密度，不能冒充純成人語義頻次。

## 6.1 本次最重要的語義校正

### 「奶子」不能直接當《金瓶梅》的乳房來源詞

《金瓶梅》原檔 `奶子` raw hits 很高，但逐句檢查後，**絕大多數／實際可見用法是「乳母、奶媽」義**，例如「領了個奶子來」「叫奶子來喂哥兒奶」一類。

因此本版正式鎖：

```yaml
JPM_NAIZI_DISAMBIGUATION:
  source_term: "奶子"
  raw_hits: 127
  dominant_semantics: "WET_NURSE / 乳母"
  classical_breast_lexicon_eligibility: false
  may_be_used_in_host_modern_vulgar_register: true
  host_source: "PLAYER / MODERN CHARACTER REGISTER"
```

也就是：**觀止裡玩家說「奶子」完全可以成立為現代／低俗身體詞，但不能偽稱它是從《金瓶梅》乳房描寫抽來的。**

《金瓶梅》真正可確認的乳房／乳頭詞包括：`酥胸、香乳、奶頭、奶頭兒`。

### 其他高歧義詞

```yaml
MIXED_TERM_LOCK:
  - "丟／丟了：大量一般語義；只有『丟身子、將丟未丟、我要丟了』等在成人語境才可高置信使用。"
  - "往來：一般往來很多；成人語境需由周邊 mechanics 判斷。"
  - "入港：可作談話／事情進入狀態，也可作成人隱喻。"
  - "房中：普通房內與房中術／性愛語境混合。"
  - "睡／上床：日常睡眠與成人事件混合。"
  - "摸／咬／托／扶：通用動作；CERI 必須先有 BODY RELATION，不能靠詞本身判成人事件。"
  - "快活／受用：成人快感與一般愉悅混合。"
```

---

# 7｜兩書最值得吸收的「句法／構成」而非單詞

## 7.1 《金瓶梅》：動作與床話同時發生

高價值不是單一淫詞，而是常見：

```text
身體動作
＋
稱呼／罵語／要求
＋
對方立刻調整或繼續
```

例如來源中可見的功能形：

- `親嘴／咂舌` 與飲酒、坐懷、摟抱同時發生；
- `慢著些`、`饒了奴`、`親達達` 等話直接嵌在動作裡；
- `兩廂迎湊`、`舉股相就` 把受方寫成真正的動作方；
- `顫聲柔語`、`沒口子叫` 是聲音表現，不自動等於內心真相。

## 7.2 《肉蒲團》： mechanics 被拆成可組合階段

高價值包括：

- `由淺入深`
- `由寬而緊`
- `抽送有度`
- `不猛不寬，不緩不急`
- `字字模糊`
- `上氣不接下氣`
- `似說話非說話`
- `似嘆氣非嘆氣`
- `將丟未丟`
- `已丟之後`
- `動極近靜`

其價值在於：

> **性愛不是一條「越來越快」線，而是可有位置、力度、語言容量、疲勞、停頓與波峰前後的多階段變化。**

---

# 8｜BREAST / NIPPLE SPECIALIZATION｜乳房／乳頭專項

本輪實跑顯示 V0.1 對乳房描寫仍太乾淨，因此 V0.2 建立專項。

```yaml
BREAST_REGISTER_BANK:

  source_classical:
    - "酥胸"
    - "香乳"
    - "奶頭／奶頭兒"
    - "乳峰"
    - "肉峰"

  host_modern_neutral:
    - "乳房"
    - "乳頭"
    - "胸"
    - "胸部"

  host_modern_low:
    - "胸脯"
    - "奶子"
    - "奶頭"

  actions_source_supported:
    - "摸"
    - "揣摸"
    - "揉"
    - "揉搓"
    - "捏"
    - "捻"
    - "托"
    - "咂"
    - "吮"
    - "咬"

  interaction:
    - "人物可自己調整力道"
    - "人物可按回某一位置"
    - "兩側敏感度不必相同"
    - "痛點可以局部關閉，其他接觸仍可成立"
```

## 8.1 「奶子」的法位

`奶子` 作「乳房」的低俗現代詞，**可由玩家／角色輸入強力點亮**。

它不是本版硬說成《金瓶梅》歷史乳房詞。

這個分離很重要：

> **來源語料的歷史事實，和宿主中文現在能使用的語域，不是同一件事。**

---

# 9｜V0.2 反模板與反污染

```yaml
CERI_V0_2_ANTI_TEMPLATE:

  AT-01:
    "禁止喘→顫→抓→更快→高潮成為預設成人曲線。"

  AT-02:
    "禁止把 ACTION BANK 當同義詞轉盤。"

  AT-03:
    "禁止為了看起來豐富而無因果換姿勢。"

  AT-04:
    "禁止每個古代人物都說親達達／冤家／心肝。"

  AT-05:
    "禁止每個現代粗口人物都說奶子／雞巴；仍要由人物與玩家 register 決定。"

  AT-06:
    "禁止把叫床當高潮、同意、戀愛或私人真相。"

  AT-07:
    "禁止把痛感自動色情化；痛就是一條獨立可觀察通道。"

  AT-08:
    "禁止把局部痛／局部拒絕擴張成未命中的全部事件。"

  AT-09:
    "禁止 NARRATOR SANITIZATION：低俗玩家輸入不能無因果整段洗成雙峰／曲線／柔軟輪廓。"

  AT-10:
    "禁止 NARRATOR VULGARIZATION：文雅玩家輸入也不能無因果整段洗成粗口。"

  AT-11:
    "禁止來源詞建立人物原本不存在的性慾、同意、技巧、人格與說話習慣。"

  AT-12:
    "不得直接仿寫或長段搬運《金瓶梅》《肉蒲團》；只抽取詞、短語、句法與構成關係重新生成。"
```

---

# 10｜V0.2 回歸矩陣

```yaml
REGRESSION:

  R1_REGISTER_AB:
    same_event_inputs:
      - "雙峰"
      - "乳房"
      - "胸"
      - "奶子"
    test:
      - "旁白 register 是否跟得住"
      - "NPC 語言是否仍獨立"

  R2_LONG_HORIZON:
    test:
      - "T1-T5"
      - "TRANSITION_CAUSALITY_LOCK"

  R3_CHARACTER_DIFFERENTIATION:
    cast_types:
      - "蘇清：直接粗口／即時回饋"
      - "醉花：控制—暴露／較少言"
      - "潘金蓮：市井挑逗"
      - "李師師：高控制語言"
    fail_if:
      "只剩同一篇性愛文換人物名"

  R4_PAIN_LOCALITY:
    test:
      - "痛點局部化"
      - "痛感不自動等快感"
      - "人物可以重新指定可碰／不可碰區"

  R5_SOURCE_OVERFIT:
    compare:
      - "C0 STRUCTURE ONLY"
      - "C1 LIGHT"
      - "C2 CLASSICAL PRIMARY"
      - "C3 SOURCE DENSE"
    goal:
      "找到語彙活化到偽古典模板之間的臨界點"
```

---

# 11｜FULL CORPUS LEXICON BANK

以下為本版從兩書全文成人顯影語義域整理出的 **249 個來源詞／短語候選**。

注意：

- 表內 `raw hits` 是 exact substring 原始命中，不是「純性愛語義次數」；
- `MIXED` 詞必須依上下文重新判定；
- 部分通用字（摸、托、咬、睡、丟）頻次很高，但不因命中就自動取得成人語義；
- 本表的價值是擴大候選語言空間，而不是讓生成器每段把詞全部用一遍。

---

## BODY_BREAST_AND_SURFACE｜乳房／身體表面

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 酥胸 | 11 | 1 | 古典艷稱；可作旁白 register，不宜人人固定使用 |
| 香乳 | 4 | 0 | 古典乳房稱謂；《金瓶梅》有明確成人語境 |
| 奶頭 | 4 | 0 | 直接部位詞；《金瓶梅》有成人語境 |
| 奶頭兒 | 1 | 0 | 口語化部位詞；《金瓶梅》有成人語境 |
| 乳峰 | 0 | 2 | 《肉蒲團》用例；偏修辭化 |
| 肉峰 | 0 | 1 | 《肉蒲團》用例；比乳峰更肉身 |
| 胸脯 | 2 | 0 | 日常身體詞 |
| 胸前 | 9 | 1 | 中性敘述詞 |
| 白屁股兒 | 1 | 0 | 《金瓶梅》床上直接稱說 |
| 屁股 | 38 | 0 | 低／日常 register；語義多用 |
| 粉項 | 6 | 0 | 古典外觀詞 |
| 玉體 | 10 | 0 | 古典修辭，容易過度文雅 |
| 香體 | 1 | 0 | 古典修辭 |
| 肌膚 | 6 | 8 | 中性／文雅 |
| 皮肉 | 5 | 16 | 較直接、肉身 |
| 白肉 | 3 | 0 | 直接視覺詞；需看上下文 |
| 朱唇 | 25 | 4 | 古典口唇修辭 |
| 舌頭 | 29 | 6 | 直接身體詞 |

---

## BODY_GENITAL_FEMALE｜女性器官／局部

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 牝戶 | 7 | 7 | 古典直稱，高成人語義 |
| 牝中 | 28 | 2 | 古典直稱，高成人語義 |
| 牝口 | 3 | 0 | 古典局部詞 |
| 陰戶 | 2 | 30 | 直接／古典；《肉蒲團》高頻 |
| 陰中 | 4 | 15 | 直接空間性稱呼 |
| 陰門 | 1 | 4 | 古典直稱 |
| 花心 | 10 | 9 | 古典情色局部詞，亦可能有比喻義 |
| 花蕊 | 2 | 0 | 古典艷稱，低頻 |
| 蛙口 | 6 | 0 | 《金瓶梅》成人局部隱稱 |
| 牝毛 | 1 | 0 | 古典體毛直稱 |
| 陰毛 | 0 | 2 | 《肉蒲團》直稱 |
| 毳毛 | 2 | 0 | 古典體毛詞 |

---

## BODY_GENITAL_MALE｜男性器官／局部

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 陽物 | 2 | 74 | 《肉蒲團》核心直接稱謂 |
| 那話 | 95 | 0 | 《金瓶梅》高頻避直稱；語境敏感 |
| 麈柄 | 15 | 0 | 《金瓶梅》古典隱稱，高成人語義 |
| 龜頭 | 17 | 4 | 直接部位詞 |
| 玉莖 | 4 | 0 | 古典艷稱 |
| 淫器 | 14 | 0 | 《金瓶梅》直接成人器物／器官詞 |
| 雞巴 | 1 | 1 | 兩書均有極低頻粗俗用例；低 register |
| 肉棒槌 | 0 | 1 | 《肉蒲團》粗俗／比喻式直稱 |
| 馬眼 | 2 | 0 | 局部直稱 |
| 二卵 | 2 | 0 | 古典粗直局部詞 |

---

## CONTACT_AND_TOUCH｜接觸／愛撫

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 親嘴 | 20 | 14 | 接吻事件直稱 |
| 咂舌 | 12 | 0 | 《金瓶梅》口舌接吻動詞 |
| 鳴咂 | 7 | 0 | 《金瓶梅》聲音＋口舌動作 |
| 摟抱 | 19 | 0 | 雙人身體包覆 |
| 摟住 | 3 | 19 | 動作結果更明確 |
| 摟定 | 6 | 0 | 保持性動作 |
| 抱住 | 11 | 7 | 保持／拉近 |
| 纏抱 | 0 | 1 | 《肉蒲團》低頻 |
| 貼伏 | 0 | 2 | 身體貼近構型 |
| 捱擦 | 1 | 2 | 摩擦／試探 |
| 挨擦 | 0 | 1 | 《肉蒲團》變體 |
| 摸 | 86 | 24 | 高頻通用動詞；需依 body relation 限定 |
| 揉 | 33 | 3 | 揉按／愛撫 |
| 揉搓 | 8 | 0 | 較強動作詞 |
| 捏 | 60 | 7 | 捏／拿捏 |
| 捻 | 13 | 0 | 細小指部動作 |
| 扳 | 18 | 4 | 調位／固定 |
| 托 | 139 | 18 | 支撐／承重／托起 |
| 扶 | 141 | 6 | 支撐／引導 |
| 按住 | 6 | 0 | 局部控制／停止位移 |
| 攥著 | 3 | 0 | 抓握 |
| 拉住 | 10 | 0 | 阻止離開／拉近 |
| 挑弄 | 6 | 0 | 細部挑逗 |
| 舔 | 2 | 3 | 直接口舌動作 |
| 舐 | 3 | 0 | 古典口舌動詞 |
| 咬 | 57 | 2 | 直接牙齒動作；痛感與情慾需分軸 |
| 吮 | 22 | 0 | 吸吮動詞；《金瓶梅》成人語境可見 |

---

## EVENT_LEVEL｜成人事件層

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 雲雨 | 30 | 3 | 古典性交總稱 |
| 交歡 | 13 | 0 | 性交／歡會總稱 |
| 交媾 | 6 | 8 | 直接事件稱謂 |
| 行房 | 11 | 12 | 房事總稱 |
| 同房 | 2 | 0 | 較中性 |
| 入港 | 13 | 0 | 《金瓶梅》成人隱喻；亦有非性用法，MIXED |
| 作歡 | 1 | 0 | 古典事件詞 |
| 幹事 | 23 | 85 | 《肉蒲團》大量成人用法，但仍須語境判斷 |
| 上床 | 46 | 19 | 事件／空間皆可能 |
| 做一處 | 47 | 0 | 《金瓶梅》親密／性交語境常見 |
| 廝會 | 4 | 0 | 私密相會 |
| 偷期 | 4 | 0 | 偷情／幽會類 |

---

## INTERCOURSE_MOTION｜性交動作骨架

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 往來 | 54 | 5 | 重要但 MIXED；不可把 raw count 當純成人 |
| 抽送 | 5 | 17 | 兩書均有，成人動作高辨識 |
| 抽拽 | 7 | 0 | 《金瓶梅》 |
| 抽提 | 4 | 0 | 《金瓶梅》 |
| 提送 | 1 | 0 | 《金瓶梅》低頻 |
| 送入 | 4 | 1 | 直接位移 |
| 插入 | 7 | 4 | 直接位移 |
| 插進 | 2 | 2 | 直接位移 |
| 頂入 | 6 | 0 | 《金瓶梅》 |
| 攮進去 | 4 | 0 | 《金瓶梅》粗直動詞 |
| 濡研 | 4 | 0 | 《金瓶梅》摩擦式動詞 |
| 濡攪 | 1 | 0 | 《金瓶梅》低頻 |
| 極力抽提 | 3 | 0 | 《金瓶梅》完整動作短語 |
| 盡沒至根 | 4 | 0 | 《金瓶梅》深度狀態短語 |
| 一舉一坐 | 2 | 0 | 《金瓶梅》往來構型 |
| 由淺入深 | 0 | 1 | 《肉蒲團》階段轉換 |
| 由寬而緊 | 0 | 1 | 《肉蒲團》身體狀態轉換 |
| 直抵 | 5 | 5 | 兩書均有；需上下文 |
| 徐徐 | 1 | 0 | 低頻速度／方式詞，不應單獨當成人詞 |
| 迎合 | 0 | 2 | 《肉蒲團》雙向回應 |
| 迎湊 | 4 | 0 | 《金瓶梅》雙向靠合 |
| 舉股相就 | 1 | 0 | 《金瓶梅》身體主動回應 |
| 兩廂迎湊 | 2 | 0 | 《金瓶梅》明確雙向構型 |
| 合伏 | 1 | 0 | 貼伏／壓合 |
| 偎擦 | 1 | 0 | 靠貼＋摩擦 |
| 掇弄 | 5 | 0 | 《金瓶梅》反覆擺弄 |
| 推送 | 3 | 1 | 位移／協作 |
| 扳拘 | 1 | 0 | 固定雙腿／身體構型 |
| 兜其股 | 3 | 0 | 支撐／托股 |
| 蹲踞 | 6 | 0 | 姿勢／主動構型 |
| 高蹶 | 1 | 0 | 姿勢詞 |
| 墊腰 | 0 | 5 | 《肉蒲團》姿勢支撐 |
| 翻天倒地 | 0 | 3 | 《肉蒲團》高動態總稱；容易模板化 |
| 挨挨擦擦 | 0 | 1 | 《肉蒲團》試探摩擦 |
| 捱擦捱擦 | 0 | 1 | 《肉蒲團》原文重疊 |
| 一抽一送 | 0 | 1 | 《肉蒲團》動作節奏 |
| 一來一往 | 3 | 1 | 往復；MIXED |
| 縱送 | 0 | 1 | 《肉蒲團》成人動作 |

---

## ORAL_AND_MOUTH｜口舌／口交相關

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 品簫 | 5 | 0 | 《金瓶梅》口交隱語 |
| 吹簫 | 6 | 0 | 《金瓶梅》口交隱語 |
| 吞吐 | 2 | 0 | 口部往復；需語境 |
| 含著 | 4 | 0 | 口腔保持 |
| 噙著 | 6 | 0 | 口腔含住 |
| 吮 | 22 | 0 | 吸吮 |
| 舔 | 2 | 3 | 舌部直接動詞 |
| 舐 | 3 | 0 | 古典舔舐 |
| 咂 | 65 | 0 | 口舌吸咂 |
| 咬 | 57 | 2 | 牙齒動作 |
| 挑弄蛙口 | 3 | 0 | 《金瓶梅》口舌細節 |
| 舌尖挑弄 | 1 | 0 | 《金瓶梅》 |
| 舌尖抵 | 1 | 0 | 《金瓶梅》 |
| 朱唇裹 | 2 | 0 | 《金瓶梅》嘴唇包覆 |
| 吞裹龜頭 | 2 | 0 | 《金瓶梅》口交動作 |
| 吮淨 | 1 | 0 | 《金瓶梅》口交收尾 |

---

## AROUSAL_FLUID_BODY_STATE｜興奮／體液／身體狀態

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 淫津 | 6 | 0 | 《金瓶梅》體液詞 |
| 淫水 | 9 | 18 | 兩書均大量成人語境 |
| 淫精 | 1 | 0 | 《金瓶梅》低頻 |
| 濕 | 31 | 4 | 高度 MIXED；只作一般身體狀態詞 |
| 滑 | 39 | 7 | MIXED |
| 滑落 | 3 | 0 | 《金瓶梅》成人上下文可見 |
| 流溢 | 1 | 0 | 體液狀態 |
| 氣喘 | 8 | 0 | 身體負荷 |
| 喘 | 17 | 1 | 身體負荷；不可當唯一成人反應 |
| 酥麻 | 2 | 3 | 兩書均有 |
| 酥癱 | 1 | 0 | 《金瓶梅》 |
| 手酸腳軟 | 0 | 1 | 《肉蒲團》 |
| 星眼朦朧 | 2 | 0 | 《金瓶梅》視覺狀態 |
| 雲鬢欲墜 | 0 | 1 | 《肉蒲團》 |
| 面紅 | 4 | 1 | MIXED |
| 顫 | 19 | 0 | MIXED；不可自動等高潮 |
| 渾身 | 22 | 12 | MIXED |
| 戰慄 | 2 | 0 | MIXED |
| 動極近靜 | 0 | 1 | 《肉蒲團》高價值階段觀察 |

---

## VOCAL_MANIFESTATION｜叫床／聲音

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 呻吟 | 7 | 0 | 《金瓶梅》 |
| 呻吟不止 | 2 | 0 | 《金瓶梅》 |
| 哼哼唧唧 | 1 | 1 | 兩書均有 |
| 顫聲 | 11 | 0 | 《金瓶梅》 |
| 柔氣 | 1 | 0 | 《金瓶梅》 |
| 顫聲柔氣 | 1 | 0 | 《金瓶梅》 |
| 顫聲柔語 | 2 | 0 | 《金瓶梅》 |
| 揚聲顫語 | 1 | 0 | 《金瓶梅》 |
| 叫喚 | 3 | 6 | 兩書均有，MIXED |
| 叫聲 | 12 | 1 | MIXED |
| 聲氣 | 4 | 4 | 兩書均有 |
| 上氣不接下氣 | 0 | 1 | 《肉蒲團》高價值 vocal phase |
| 字字模糊 | 0 | 1 | 《肉蒲團》高價值 vocal phase |
| 似說話非說話 | 0 | 1 | 《肉蒲團》高價值 vocal phase |
| 似嘆氣非嘆氣 | 0 | 1 | 《肉蒲團》高價值 vocal phase |
| 沒口子叫 | 6 | 0 | 《金瓶梅》反覆叫喊式 |

---

## CLIMAX_AND_CLOSURE｜高潮／收束

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 丟身子 | 2 | 0 | 《金瓶梅》高潮事件詞 |
| 將丟未丟 | 0 | 1 | 《肉蒲團》高潮前階段 |
| 已丟之後 | 0 | 1 | 《肉蒲團》高潮後階段 |
| 要丟 | 0 | 11 | 《肉蒲團》高頻高潮語言 |
| 我要丟了 | 0 | 2 | 《肉蒲團》人物直接表態 |
| 丟了 | 28 | 31 | 高度 MIXED；不可 raw=count=sexual |
| 一泄如注 | 8 | 0 | 《金瓶梅》射精／高潮收束 |
| 一泄 | 10 | 1 | 成人語境高 |
| 精來 | 4 | 0 | 《金瓶梅》 |
| 精泄 | 5 | 2 | 兩書均有 |
| 射 | 12 | 1 | MIXED |
| 雲收雨散 | 3 | 0 | 《金瓶梅》古典收束 |
| 雲雨才罷 | 1 | 0 | 《金瓶梅》 |
| 快活盡頭 | 0 | 2 | 《肉蒲團》高潮邊界隱語 |
| 事畢 | 5 | 0 | 事件收束；MIXED |

---

## BED_LANGUAGE_AND_RESPONSE｜床上話／要求／粗話

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 親達達 | 14 | 0 | 《金瓶梅》床上親暱稱呼 |
| 達達 | 61 | 0 | 《金瓶梅》高頻稱呼；非全為性愛 |
| 親爺 | 3 | 0 | 《金瓶梅》床上稱呼 |
| 親漢子 | 2 | 0 | 《金瓶梅》床上稱呼 |
| 心肝 | 23 | 28 | 兩書均高頻；成人／日常混用 |
| 心肝命肉 | 0 | 1 | 《肉蒲團》稱呼 |
| 心肝短命 | 1 | 0 | 《金瓶梅》 |
| 冤家 | 41 | 3 | 親暱／埋怨雙用 |
| 怪強盜 | 1 | 0 | 《金瓶梅》罵中帶親 |
| 怪小淫婦 | 25 | 0 | 《金瓶梅》低俗角色床話 |
| 小淫婦 | 109 | 0 | 低俗稱呼；不得自動套所有人物 |
| 賊淫婦 | 33 | 0 | 低俗罵語 |
| 老淫婦 | 22 | 0 | 低俗罵語 |
| 慢著些 | 5 | 0 | 明確降低速度／強度要求 |
| 輕些 | 0 | 4 | 《肉蒲團》降低強度 |
| 放輕些 | 0 | 2 | 《肉蒲團》 |
| 求你放輕些 | 0 | 1 | 《肉蒲團》完整要求 |
| 快些 | 18 | 5 | 催促；高度 MIXED |
| 快些弄 | 0 | 1 | 《肉蒲團》成人催促 |
| 饒了奴 | 3 | 0 | 《金瓶梅》求緩／求停；需辨情境 |
| 不要動 | 0 | 2 | 《肉蒲團》局部停住 |
| 摟住我睡罷 | 0 | 1 | 《肉蒲團》從動作轉休息 |
| 使不得 | 8 | 5 | 拒絕／阻止／日常皆可，MIXED |
| 再來 | 24 | 3 | MIXED；續行功能 |
| 好爹爹 | 1 | 0 | 《金瓶梅》求饒／親暱上下文 |
| 罷了 | 305 | 32 | MIXED；終止／感嘆 |

---

## SPACE_OBJECT_CLOTHING｜床榻／物件／衣物

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 床上 | 121 | 16 | 空間核心；非全成人 |
| 床帳 | 22 | 1 | 床榻鏡頭 |
| 羅帳 | 2 | 0 | 古典床帳 |
| 錦褥 | 2 | 1 | 床褥 |
| 鴛衾 | 3 | 0 | 古典床被 |
| 衾枕 | 9 | 0 | 床具 |
| 枕席 | 9 | 3 | 床榻／成人隱喻 |
| 繡床 | 2 | 0 | 古典床具 |
| 春榻 | 0 | 5 | 《肉蒲團》 |
| 被窩 | 25 | 9 | 日常床上空間 |
| 被褥 | 12 | 1 | 日常物件 |
| 帳子 | 15 | 3 | 床帳 |
| 燈燭 | 24 | 0 | 空間光源 |
| 衣帶 | 2 | 1 | 衣物／脫衣節點 |
| 裙帶 | 4 | 0 | 衣物 |
| 褲子 | 23 | 12 | 直接衣物 |
| 褻衣 | 1 | 0 | 古典內衣 |

---

## NAMED_POSITION_AND_METAPHOR｜命名姿勢／艷情隱喻

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 縱蝶尋芳 | 0 | 1 | 《肉蒲團》命名姿勢 |
| 教蜂釀蜜 | 0 | 1 | 《肉蒲團》命名姿勢 |
| 迷鳥歸林 | 0 | 1 | 《肉蒲團》命名姿勢 |
| 餓馬奔槽 | 0 | 1 | 《肉蒲團》命名姿勢 |
| 雙龍鬥倦 | 0 | 1 | 《肉蒲團》事後／姿勢命名 |
| 巫山 | 12 | 2 | 古典性愛隱喻 |
| 高唐 | 1 | 0 | 古典性愛隱喻 |
| 巫山雲雨 | 2 | 0 | 古典性交隱喻 |
| 雨意 | 8 | 0 | 古典情慾隱喻；MIXED |
| 雲情雨意 | 3 | 0 | 《金瓶梅》 |
| 枕席之歡 | 1 | 2 | 兩書均有 |
| 房帷之樂 | 0 | 1 | 《肉蒲團》 |
| 燕爾新婚 | 3 | 0 | 非純成人但可作關係 register |
| 春心 | 9 | 1 | 情慾 |
| 淫心 | 19 | 6 | 古典欲念 |
| 淫情 | 7 | 0 | 古典欲念 |
| 淫興 | 0 | 6 | 《肉蒲團》 |
| 情興 | 4 | 0 | 《金瓶梅》 |
| 快活 | 17 | 48 | 兩書成人語境高，但日常也可 |
| 受用 | 22 | 15 | 快感／享受；MIXED |
| 取樂 | 6 | 6 | 成人／娛樂 MIXED |
| 風月 | 26 | 5 | 情色／文人 register |
| 春宮 | 0 | 18 | 《肉蒲團》高頻 |

---

# 12｜FULL EXTRACTION 之後的使用方式

## 12.1 先選關係，再選詞

錯誤：

```text
今天沒用過「抽拽」
→ 塞一個「抽拽」
```

正確：

```text
當前 BODY RELATION
= 對方正在往回退、另一方持續拉回形成往復
↓
再看「抽拽／往來／迎湊／推送」哪一個真正對得上
```

## 12.2 詞彙密度不是品質

高解析成人描寫應允許：

- 一段極直接；
- 下一段只寫支撐與換氣；
- 一段粗話很多；
- 下一段人物完全不說；
- 一段用「奶子」；
- 下一段只用代詞或位置，不必每句重複部位名。

## 12.3 來源分流

```yaml
SOURCE_ROUTING:
  JINPINGMEI:
    strengths:
      - "市井床話"
      - "親嘴／咂舌"
      - "粗俗稱呼"
      - "身體直接詞與古典隱稱並存"
      - "動作中持續說話"

  ROUPUTUAN:
    strengths:
      - "動作 mechanics 分解"
      - "姿勢／支撐"
      - "聲音階段"
      - "高潮前後狀態"
      - "動作節奏不是只有快慢"
```

---

# 13｜V0.4 使用規則

```yaml
CERI_V0_4_USAGE:
  may:
    - "為已成立成人 semantic node 提供古典中文候選語彙／句法／床上話。"
    - "依 speech function、人物 voice、vocal capacity 與 current-action callback 組合語句候選。"
    - "追蹤 manifestation window 內的 lexical / functional recency，辨識無因果 Default Attractor。"
    - "保留來源 provenance 與歧義警告。"
    - "依 Host / Player register 調整密度。"

  must_not:
    - "把 corpus 詞命中當成人事件分類器。"
    - "把來源角色口吻覆蓋宿主人物。"
    - "把 character profanity signature 反向寫成人格事實。"
    - "把 lexical recency 變成禁詞表。"
    - "把古典來源的性行為、倫理、醫療或關係觀念升格成宿主規則。"
    - "為了使用詞庫或追求新奇而機械插入動作。"
```

---

# 14｜與 AINT V2 的責任分工

```text
HOST
→ 人物／事件／知情／世界

AINT V2
→ 成人互動結構、連續性、邊界、重大轉換、顯影節點

CERI V0.4（optional candidate）
→ 古典中文語域與 corpus candidates

HOST
→ 驗證結果／SAVE
```

若 CERI 不存在：

```text
AINT V2
→ 使用宿主一般 rendering / language capability
```

不影響人物、事件或成人 Runtime 資格。

---

# 15｜回歸


## 15.1｜Promotion Gate

```yaml
CERI_V0_4_PROMOTION_GATE:
  current_state: "CANDIDATE_PENDING_REGRESSION"
  may_replace_ceri_v0_3_as_current_after:
    - "R10-R18 focused regression pass"
    - "at least one long-horizon adult-dialogue test"
    - "GM explicit promotion"

  guanzhi_main_version_bump_required: false
  reason:
    - "GUANZHI V14.2 對 CERI 為 optional replaceable provider。"
    - "CERI provider family 不變。"
    - "CERI exact_version_required = false。"

  baseline_manifest_update_after_promotion: true
  save_update_required: false
```


```yaml
CERI_V0_4_REGRESSION:
  inherited:
    R01_CHARACTER_VOICE: "詞庫不吞人物聲音。"
    R02_MODERN_INPUT: "玩家現代詞不自動變 NPC 現代語言。"
    R03_SOURCE_FACT: "來源詞不升世界事實。"
    R04_EUPHEMISM_DRIFT: "低 register 不被整段雅化。"
    R05_VULGARIZATION_DRIFT: "文雅 register 不被整段粗俗化。"
    R06_AMBIGUITY: "raw hit 不冒充成人語義命中。"
    R07_NO_EVENT_CREATION: "CERI 不自行建立成人事件。"
    R08_NO_SAVE: "CERI 不直接提交 SAVE。"
    R09_AINT_STRUCTURAL_SEPARATION: "痛感／轉換／長距離規則由 AINT V2 持有，不在 CERI 重複立法。"

  new_v0_4:
    R10_FUNCTION_FIRST:
      expect: "同一粗俗強度下，TEASE / REQUEST / MOCK / PRAISE / LOCAL_STOP 等功能產生不同句法與詞選。"

    R11_CHARACTER_DIFFERENTIATION:
      fixtures:
        - "蘇清：direct / rough / immediate-feedback test profile"
        - "醉花：low-verbal / controlled-exposure test profile"
        - "潘金蓮：streetwise teasing test profile"
        - "李師師：high-control language test profile"
      lock: "TEST PROFILE != CROSS-LINE CHARACTER FACT WRITEBACK"
      fail_if: "只剩同一篇床話換人物名。"

    R12_LEXICAL_RECENCY:
      expect:
        - "無因果反覆使用高顯著詞時，candidate set 被重開。"
        - "有角色／節奏／回擊原因的刻意重複仍允許。"

    R13_FUNCTIONAL_RECENCY:
      expect: "不能只換同義詞卻一直重複同一 speech function。"

    R14_FRAGMENT_CAPACITY:
      expect:
        - "低 vocal capacity 可縮短、斷句或沉默。"
        - "不得把所有人物壓成同一喘／顫／碎字模板。"

    R15_ACTION_CALLBACK:
      expect: "床上話引用當前 action / support / attention / prior line；不得創造 Host 未建立的 mechanics。"

    R16_RARE_WORD_TRAP:
      expect: "避免為了新鮮而把古典罕詞當同義詞輪盤。"

    R17_NO_PERSONALITY_WRITEBACK:
      expect: "Character Profanity Signature 只做當前 voice alignment，不寫 LCAPG / SAVE。"

    R18_AINT_2_1_RC3_COMPAT:
      expect: "CERI 只回語言候選與警告；Material Transition / consent / event / relation 仍由 AINT/Host 處理。"
```

> **CERI V0.4 是語言資源＋語言作曲器，不是人物、事件、同意或世界。**


---


<!-- END VERBATIM WORLD V2.2.2-CURRENT -->


<!-- END FULL INHERITED WORLD V2.2.2-CURRENT -->

END OF GUANZHI WORLD V2.2.3-CURRENT


<!-- END VERBATIM WORLD V2.2.3 CURRENT PARENT -->


<!-- END VERBATIM APPROVED CANDIDATE -->

END OF GUANZHI WORLD V2.2.4-CURRENT

<!-- END VERBATIM WORLD V2.2.4-CURRENT PARENT -->

END OF GUANZHI WORLD V2.2.5-CURRENT
