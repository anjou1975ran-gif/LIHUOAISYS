# GUANZHI SAVE RELATION-FIRST EXTERNAL OVERLAY V0.3-FULL-EXP
## 觀止 SAVE 關係優先外接原則｜HOT SAVE × MASTER SAVE × 人物／事件／關係索引完整實驗版
### 2026-10-07

> **法位**
>
> `EXPERIMENTAL EXTERNAL OVERLAY`
>
> `NON_NORMATIVE`
>
> `NO CORE CHANGE`
>
> `NO SAVE OWNER CHANGE`
>
> `NO FORMAL SAVE SCHEMA MUTATION`
>
> `NO HOST DEPLOYMENT CLAIM`
>
> `NO AUTOMATIC CANON PROMOTION`
>
> 本文件供觀止實跑測試。
>
> 建議至少連續跑 **5–6 個有效 SAVE／接關週期**，再判斷是否值得正式納入 Core / SAVE Runtime。
>
> 本外掛不是第四份 SAVE。
>
> 它是一個：
>
> **RELATION-FIRST SAVE PROJECTION / COMPILATION PRINCIPLE**
>
> 作用是把既有 HOT / MASTER / 人物事件關係索引中的合格資料，
> 編譯成更適合故事接續的「第一讀取面」。

---

# 0｜一句話

> **SAVE 仍然以證據決定什麼可以被記住。**
>
> **但下一位導演應先讀「人物現在彼此站在哪裡」，再讀「發生過什麼」。**

最短式：

```text
EVIDENCE DECIDES MEMORY ELIGIBILITY.

RELATION-FIRST DECIDES READ PRIORITY.

RELATION-FIRST
!=
RELATION-ONLY.

PROJECTION
!=
NEW MEMORY.

INDEX
!=
SOURCE OF TRUTH.

RELATIONAL SYNTHESIS
!=
RELATIONSHIP FABRICATION.
```

---

# 1｜本外掛要解決的問題

現行觀止 SAVE 的工程能力很強：

```text
事件可追
帳務可追
契約可追
知情可追
UNKNOWN 可保留
污染可隔離
角色硬狀態可回查
```

但長期工程化後容易出現一個問題：

```text
EVENT
RELATION
CONTRACT
PAYMENT
KNOWLEDGE
RUMOR
WORLD STATE
...
```

都被作為平行軸保存。

結果是：

> 下一位導演知道「發生了什麼」，
> 卻仍需重新推理一次「所以現在大家彼此是什麼」。

本外掛不推翻現有 SAVE。

它只補：

```text
QUALIFIED EVIDENCE
↓
RELATIONAL SYNTHESIS
↓
FIRST-READ CONTINUATION VIEW
```

---

# 2｜與現行三個主要 SAVE 面的關係

本外掛把目前觀止實務上的三種主要持久化／索引面視為：

```text
HOT SAVE
= 當前可直接接關的工作切片

MASTER SAVE
= 已固化的完整世界線因果、事件與硬狀態

人物／事件／關係索引
= Route Index / RCL 類衍生索引，用於快速回答：
  「某人物目前在本線什麼位置？」
  「與誰有什麼已成立關係？」
  「最後一次重大變化在哪個事件？」
```

其中：

```text
HOT / MASTER
持有「事」與合格狀態。

INDEX / RCL
持有「如何快速找到目前位置」。

RELATIONAL OVERLAY
持有「導演第一眼先看什麼」。
```

硬鎖：

```text
OVERLAY
!=
FOURTH SAVE

INDEX
!=
SECOND MASTER

RELATIONAL CENTER
!=
CANONICAL SOURCE OF TRUTH
```

---

# 3｜資料所有權

```yaml
SAVE_DATA_OWNERSHIP:

  HOT_SAVE:
    owns:
      - CURRENT_WORKING_STATE
      - CURRENT_SCENE
      - ACTIVE_RELATION_HARD_STATE
      - RECENT_CONFIRMED_EVENTS
      - ACTIVE_CONTRACTS
      - ACTIVE_LEDGER_STATE
      - CURRENT_KNOWLEDGE_STATE
      - IMMEDIATE_HOOKS
      - FORBIDDEN_INFERENCES
      - CONTINUATION_POINT

  MASTER_SAVE:
    owns:
      - DURABLE_CAUSAL_HISTORY
      - COMPLETE_EVENT_CHAIN
      - VERIFIED_LONG_TERM_HARD_STATE
      - RELATIONSHIP_HARD_STATE_HISTORY
      - CONTRACT_AND_LEDGER_HISTORY
      - KNOWLEDGE_AND_RUMOR_HISTORY
      - LONG_TERM_WORLD_CHANGES

  ROUTE_INDEX_RCL:
    owns:
      - LOOKUP_POINTERS
      - CHARACTER_CURRENT_ROUTE_POSITION_INDEX
      - RELATION_CURRENT_POSITION_INDEX
      - EVENT_LOOKUP_INDEX
      - LAST_MATERIAL_CHANGE_REF
    does_not_own:
      - ORIGINAL_EVENT_EVIDENCE
      - INDEPENDENT_WORLD_FACTS

  RELATIONAL_OVERLAY:
    owns:
      - NOTHING_CANONICAL
    may_produce:
      - DERIVED_RELATIONAL_CENTER
      - DERIVED_FIRST_READ_VIEW
      - DERIVED_CONTINUATION_PRESSURE_VIEW
```

---

# 4｜唯一真源原則

同一件事件／交易／拒絕／付款：

```text
原始證據只正式保存一次。
```

其他層只存：

```text
ref
summary
current standing
lookup pointer
```

不得：

```text
HOT 寫一版
MASTER 再改一版
RCL 再自行推一版
OVERLAY 又發明第四版
```

正式式：

```text
ONE MATERIAL EVENT
→ ONE QUALIFIED EVIDENCE CHAIN

MANY READ VIEWS
→ ALLOWED

MANY COMPETING FACT SOURCES
→ FORBIDDEN
```

---

# 5｜RELATION-FIRST 的正式含義

本外掛中的「關係」不是：

```text
感情值
好感度
親密度
CP 感
導演覺得很搭
```

而是：

> **人物／制度彼此現在擁有什麼實際位置、權力、依賴、義務、界線、知情與未決。**

最低問題：

```text
誰把誰當什麼？
誰對誰有什麼權力？
誰依賴誰什麼？
誰欠誰什麼？
誰有資格要求誰什麼？
誰拒絕過誰什麼？
誰知道誰的什麼？
誰仍不知道什麼？
哪條界線已經成立？
哪個關係仍未定義？
什麼明確還沒有成立？
```

---

# 6｜合法 Relation Node

V0.3 預設只承認：

```text
PERSON ↔ PERSON
PERSON ↔ INSTITUTION
```

例如：

```text
班富蘭 ↔ 蘇清
錦棠 ↔ 潘金蓮
班富蘭 ↔ 觀止
```

暫不自動承認：

```text
PERSON ↔ OBJECT
PERSON ↔ ABSTRACT_THEME
INSTITUTION ↔ ABSTRACT_VALUE
```

如未來實跑證明有必要，再另案擴充。

---

# 7｜關係資格門檻

外掛**不得降低**既有 SAVE 的關係回寫門檻。

可以支持關係改寫／升格的來源：

```text
1. 人物作出明確選擇
2. 契約簽署／接受／拒絕／撤回／終止
3. 公開身份或關係定位改變
4. 長期承諾成立
5. 有效拒絕成立
6. 未知事項正式揭露
7. 可觀察行動造成持續後果
8. 既有 Domain 已資格化的 RELATION DELTA
```

以下單獨不足以成立硬關係：

```text
笑
喝酒
注意
調情
吃醋表象
沉默
被說中心事
夢
戲中戲
主題相似
一句漂亮話
一次同場
導演覺得兩人很有火花
```

硬鎖：

```text
ATTENTION != RELATIONSHIP
COOPERATION_ONCE != TRUST
TRUST != LOVE
TRADE != LOYALTY
ONE_REFUSAL != PERMANENT_HOSTILITY
ONE_KIND_ACT != LONG_TERM_CARE
THEMATIC_MIRROR != RELATIONAL_STANDING
```

---

# 8｜RELATIONAL_POSITION 標準物件

```yaml
RELATIONAL_POSITION:

  relation_ref:
    value: REQUIRED_OR_TEST_LOCAL_ID

  parties:
    - entity_ref:
      entity_class: "PERSON | INSTITUTION"
    - entity_ref:
      entity_class: "PERSON | INSTITUTION"

  current_position:
    labels: []
    natural_language_definition:

  directionality:

    party_a_toward_b:
      current_view: []
      powers: []
      dependencies: []
      obligations: []
      debts: []
      permissions: []
      boundaries: []
      active_offers: []
      effective_refusals: []

    party_b_toward_a:
      current_view: []
      powers: []
      dependencies: []
      obligations: []
      debts: []
      permissions: []
      boundaries: []
      active_offers: []
      effective_refusals: []

  what_changed:
    qualified_changes: []

  knowledge_asymmetry:
    mutual_knows: []
    a_knows_b_does_not: []
    b_knows_a_does_not: []
    mutually_hidden_or_unknown: []

  unresolved:
    axes: []

  still_not:
    explicit_non_promotions: []

  evidence:
    event_refs: []
    contract_refs: []
    ledger_refs: []
    knowledge_refs: []
    relation_delta_refs: []

  standing:
    relation_state:
      - HARD_ESTABLISHED
      - PARTIAL_ESTABLISHED
      - RELATIONAL_SEED_ONLY
      - UNKNOWN

    evidence_quality:
      - QUALIFIED_SAVE_BACKED
      - CURRENT_HOT_BACKED
      - TEST_SOURCE_BACKED
      - INSUFFICIENT
```

---

# 9｜RELATIONAL_SEED_ONLY

這是一個**投影分類**，不是新的硬世界關係等級。

可用於：

```text
兩人已彼此注意
彼此已產生 material salience
未來可能形成關係
但目前沒有足夠 evidence 讓關係升格
```

```yaml
RELATIONAL_SEED_ONLY:
  may_mean:
    - MUTUAL_SALIENCE
    - FIRST_CONTACT
    - MATERIAL_ATTENTION
    - OPEN_POTENTIAL

  may_not_imply:
    - TRUST
    - ATTRACTION
    - ALLIANCE
    - RIVALRY
    - INTIMACY
    - OBLIGATION
    - SHARED_RESONANCE_AS_HARD_RELATION
```

---

# 10｜STILL_NOT

每條重要關係允許保存少量：

```yaml
still_not:
  - MUTUAL_TRUST
  - LONG_TERM_ALLIANCE
  - FULL_DISCLOSURE
  - ROMANTIC_RELATION
  - COMPLETED_SETTLEMENT
```

功能：

> 防止下一位導演把「已成立的一點」補成「整段關係」。

但不得無限列所有不存在的東西。

規則：

```text
STILL_NOT
只保存「下一位導演最可能誤升格」的項目。
```

---

# 11｜HOT SAVE 外掛原則

## 11.1 HOT 的本體不變

HOT 仍然是：

> **目前這一幕要活起來，最低需要知道什麼。**

外掛不改它的證據內容。

只改第一讀取順序。

## 11.2 HOT 第一讀取順序

```text
1. RELATIONAL CENTER
2. CURRENT SCENE / FREEZE POINT
3. MATERIAL NONRELATIONAL STATE
4. KNOWLEDGE / SECRET / AUTHORITY ASYMMETRY
5. CONTRACT / CONSENT / LEDGER
6. MINIMAL RECENT EVENT EVIDENCE
7. OPEN THREADS / DUE ITEMS
8. FORBIDDEN INFERENCES
9. MASTER / INDEX LOOKUP
10. CONTINUATION POINT
```

## 11.3 HOT_RELATIONAL_PROJECTION

```yaml
HOT_RELATIONAL_PROJECTION:

  source_hot_ref:
  source_hot_version:
  projection_version:

  relational_center: []

  current_scene:
    time:
    location:
    active_people: []
    recently_relevant_people: []
    freeze_point: []
    next_action_owner:

  material_nonrelational_state:
    money_and_ledger: []
    objects_and_custody: []
    physical_state: []
    location_state: []
    contracts: []
    deadlines: []
    legal_or_bureaucratic_state: []
    world_hard_facts: []

  knowledge_and_secret_pressure: []

  minimal_event_evidence: []

  immediate_open_threads: []

  forbidden_promotions: []

  lookup_refs: []

  continuation_point:
```

## 11.4 HOT 的 Relation Center 選擇條件

不是所有關係都進 HOT。

符合至少一項：

```text
A. 當前場景直接在場
B. 本 HOT 時段發生 material relation delta
C. 下一幕有到期權利／義務／拒絕／衝突
D. 未決關係張力會直接影響下一幕
E. 重要知情不對稱會影響下一幕
F. NPC↔NPC 關係雖無玩家參與，但仍正在發力
G. PERSON↔INSTITUTION 關係正在限制人物選擇
```

排除：

```text
只有主題相似
只有一次眼神
只是可能將來很有戲
只是導演覺得有 CP
已經長期無作用
與下一幕無直接壓力
```

建議：

```text
一般 HOT Relation Center
≈ 3–7 條 materially active relations

不是硬上限。
但超過時應檢查是否把整個世界關係網搬進 HOT。
```

## 11.5 HOT 必須保留非關係硬事實

```yaml
MATERIAL_NONRELATIONAL_STATE:
  time:
  location:
  money:
  object_custody:
  injury_or_body_state:
  contract:
  payment:
  legal_status:
  deadline:
  world_state:
  hard_knowledge:
```

硬鎖：

```text
RELATION FIRST != MONEY OPTIONAL
RELATION FIRST != CONTRACT OPTIONAL
RELATION FIRST != LOCATION OPTIONAL
RELATION FIRST != EVIDENCE OPTIONAL
```

---

# 12｜MASTER SAVE 外掛原則

## 12.1 MASTER 的本體不變

MASTER 仍然是：

```text
完整世界線因果
完整事件鏈
已驗證硬狀態
關係硬狀態歷史
契約與帳務歷史
知情與傳聞歷史
長期世界改變
```

外掛不得把 MASTER 變成人際摘要。

## 12.2 MASTER 新增的是「讀取摘要」，不是新事實

```yaml
MASTER_RELATIONAL_DIGEST:

  relation_ref:

  parties: []

  current_position:
    labels: []
    definition:

  historical_turning_points:
    - event_ref:
      effect:

  durable_power_asymmetry: []

  durable_obligations: []

  durable_boundaries: []

  durable_knowledge_asymmetry: []

  unresolved_long_term_axes: []

  still_not: []

  last_material_change_ref:

  source_master_refs: []
```

## 12.3 MASTER_RELATIONAL_DIGEST 不得複製完整事件

壞例：

```text
把 500 字事件再貼一份進 Relation Digest。
```

好例：

```yaml
historical_turning_points:
  - event_ref: E083
    effect: "A 首次拒絕 B 的婚約，私人友好仍保留"
```

事件內容留 MASTER 原事件。

Digest 只保存：

```text
現在的位置
關鍵轉折指標
最後一次 material change
未決軸
```

## 12.4 MASTER 的關係歷史不覆蓋事件歷史

```text
RELATION HISTORY
= INDEXED INTERPRETATION OF QUALIFIED DELTAS

RELATION HISTORY
!=
REPLACEMENT FOR EVENT HISTORY
```

## 12.5 MASTER 更新頻率

不要求每場都重編。

建議重編時機：

```text
1. 關係 hard standing 明確變化
2. 長期契約成立／解除
3. 權力位置轉移
4. 秘密揭露改變長期關係
5. 長期拒絕／和解／背叛成立
6. 多個 HOT 已成熟需定期固化
```

---

# 13｜人物／事件／關係索引 SAVE 原則

## 13.1 索引是什麼

索引層的核心不是「再存一次故事」。

而是：

> **快速回答角色在本玩家線目前站在哪裡，以及去哪裡找證據。**

## 13.2 CHARACTER_ROUTE_INDEX

```yaml
CHARACTER_ROUTE_INDEX:

  character_ref:

  current_route_position:
    one_line_core:
    current_role_in_route:
    active_institution_links: []
    active_contract_refs: []
    active_obligation_refs: []
    active_secret_refs: []
    current_major_relation_refs: []

  latest_material_event_ref:

  latest_hot_ref:
  latest_master_ref:

  current_load_priority:
    - INDEX_ONLY
    - ACTIVE_CARD
    - SCENE_FOCUS

  unresolved_personal_axes: []
```

## 13.3 RELATION_ROUTE_INDEX

```yaml
RELATION_ROUTE_INDEX:

  relation_ref:
  parties: []

  one_line_position:

  standing:
    - HARD_ESTABLISHED
    - PARTIAL_ESTABLISHED
    - RELATIONAL_SEED_ONLY
    - UNKNOWN

  current_active_pressure: []

  last_material_change_ref:

  unresolved_axes: []

  still_not: []

  source_refs:
    hot_ref:
    master_ref:
    event_refs: []
```

## 13.4 EVENT_ROUTE_INDEX

```yaml
EVENT_ROUTE_INDEX:

  event_ref:
  title:
  story_time:
  participants: []

  material_effect_classes:
    - RELATION
    - CONTRACT
    - PAYMENT
    - KNOWLEDGE
    - CONSENT
    - OBJECT
    - WORLD_STATE
    - IDENTITY

  current_relevance:
    - ACTIVE
    - BACKGROUND
    - DORMANT
    - SUPERSEDED
    - CORRECTION_ONLY

  affected_relation_refs: []
  affected_character_refs: []

  source_master_ref:
```

## 13.5 索引不可自行創造結論

```text
INDEX SUMMARIZES
WHAT QUALIFIED SAVE ALREADY SUPPORTS.

INDEX DOES NOT
DECIDE NEW WORLD FACTS.
```

如果 INDEX 與 MASTER 衝突：

```text
MASTER / QUALIFIED EVENT EVIDENCE WINS.
INDEX = STALE_OR_CORRUPTED → REBUILD.
```

如果 HOT 比 MASTER 更新：

```text
CURRENT READ
= MASTER BASE
+ VALID NEWER HOT OVERLAY
```

索引應標出版本，不可把舊 MASTER index 當成最新。

---

# 14｜NPC↔NPC 關係不得因玩家中心而消失

這是本外掛的重要補丁。

HOT 不得只記：

```text
PLAYER ↔ NPC
PLAYER ↔ NPC
PLAYER ↔ NPC
```

若一條 NPC↔NPC 關係：

```text
仍在限制當前世界
仍在造成權力不對稱
仍有未結契約
仍有利益衝突
仍會影響下一幕
```

則必須進 Relation Center 或至少留 active ref。

---

# 15｜PERSON↔INSTITUTION 必須可見

人物不只被人物限制。

如果制度／場所正在實際限制人物：

```text
住宿
抽成
身份
契籍
官冊
幫派
商號
宗門
官府
軍隊
青樓
家族
```

可以建立：

```text
PERSON ↔ INSTITUTION
```

但必須具體。

不能寫：

```text
某人 ↔ 社會
某人 ↔ 命運
某人 ↔ 時代
```

除非另有明確結構化 owner。

---

# 16｜EVENT PATCH 與本外掛

EVENT PATCH 仍照舊分軸：

```yaml
deltas:
  time_delta:
  character_delta:
  relationship_delta:
  contract_delta:
  consent_delta:
  ledger_delta:
  knowledge_delta:
  rumor_delta:
```

外掛不改 PATCH。

只在 PATCH commit 後做：

```text
PATCH QUALIFIED
↓
UPDATE HOT / MASTER WHEN DUE
↓
RECOMPILE AFFECTED RELATION VIEWS
↓
UPDATE INDEX REFS WHEN AUTHORIZED
```

---

# 17｜關係編譯演算法（概念規則）

不是程式要求，只是編譯順序。

```text
STEP 1
讀取 Current HOT / Master / Index

STEP 2
找出本幕 materially active actors / institutions

STEP 3
找出最近 qualified relation deltas

STEP 4
找出仍有效的 contract / refusal / permission / obligation

STEP 5
找出 knowledge asymmetry

STEP 6
建立 current_position

STEP 7
建立 unresolved

STEP 8
建立 still_not
只列高風險誤升格項目

STEP 9
保留 evidence refs

STEP 10
把非關係硬事實另列 Material State

STEP 11
輸出 First-Read View
```

---

# 18｜UNKNOWN 原則

UNKNOWN 不能被關係摘要吃掉。

```text
UNKNOWN
UNDECIDED
PARTIALLY_UNKNOWN
DISPUTED
NOT_PLAYED
PENDING
```

都可以合法存在。

例如：

```yaml
relation:
  current_position: "交易已談定，但實際結算未完成"

payment:
  status: UNKNOWN_OR_PENDING

contract_transfer:
  status: NOT_FULLY_PLAYED
```

不得因為「關係上看起來已經買下」就自動寫：

```text
錢已付
契已換
官冊已登記
```

---

# 19｜知情不對稱是關係的一部分，但不是全部

Relation Center 可以引用：

```text
誰知道誰的秘密
誰懷疑什麼
誰不知道對方知道
誰故意不揭露
```

但完整 epistemic record 仍留 Knowledge / Secret 層。

硬鎖：

```text
RELATIONAL KNOWLEDGE SUMMARY
!=
FULL KNOWLEDGE DATABASE
```

---

# 20｜權力、義務、界線必須有方向

禁止只寫：

```text
A 和 B 關係複雜。
```

至少要能回答：

```text
A 能對 B 做什麼？
B 能拒絕什麼？
誰掌握資源？
誰欠誰？
誰依賴誰？
誰能離開？
誰不能？
```

因此 relation 是有方向的。

---

# 21｜避免關係心理化

不應寫：

```text
A 覺得 B 很特別
A 對 B 產生複雜情緒
A 隱約心動
```

除非來源已成立。

優先寫可追溯位置：

```text
A 已選擇替 B 墊付一筆錢
A 已拒絕 B 進一步碰觸某物
A 已主動測試 B 的身份
A 已接受 B 的價格條件
A 尚未披露自己的來源
```

---

# 22｜HOT / MASTER / INDEX 的同步規則

```yaml
SYNC_RULES:

  HOT_TO_MASTER:
    when:
      - MATERIAL_STATE_MATURE
      - LONG_TERM_CAUSAL_VALUE
      - PERIODIC_RECONCILIATION_DUE

  MASTER_TO_INDEX:
    action:
      - UPDATE_POINTERS
      - UPDATE_CURRENT_ROUTE_POSITION
    may_not:
      - REWRITE_EVENT

  HOT_TO_INDEX:
    allowed_when:
      - HOT_IS_NEWER_THAN_MASTER
      - INDEX_EXPLICITLY_MARKS_HOT_OVERLAY
    must_mark:
      - VERSION
      - SOURCE_REF
      - TEMPORARY_OR_DURABLE_STANDING

  OVERLAY:
    action:
      - READ
      - COMPILE
    commit:
      - NONE
```

---

# 23｜衝突優先序

若出現衝突：

```text
1. Human / GM explicit correction
2. Qualified current event evidence
3. Valid newer HOT
4. Current MASTER
5. Current same-generation RCL / Route Index
6. Relational Overlay
7. Older summaries
```

外掛永遠不能推翻上游 evidence。

---

# 24｜外掛輸出模板

```yaml
GUANZHI_RELATION_FIRST_SAVE_VIEW:

  meta:
    route_id:
    story_time:
    source_hot_ref:
    source_master_ref:
    source_index_ref:
    overlay_version: V0.3-FULL-EXP
    canonical: false

  relational_center:
    - RELATIONAL_POSITION
    - RELATIONAL_POSITION

  current_scene:
    location:
    active_cast:
    freeze_point:
    next_action_owner:

  material_nonrelational_state:
    money_and_ledger: []
    objects_and_custody: []
    contracts: []
    legal_status: []
    deadlines: []
    physical_state: []
    world_state: []

  knowledge_pressure:
    - actor:
      knows:
      suspects:
      does_not_know:

  minimal_event_evidence:
    - event_ref:
      one_line_effect:

  open_threads:
    - thread_ref:
      owner:
      state:

  forbidden_promotions:
    - "X != Y"

  continuation_pressure:
    - "下一幕若無新事件，哪些關係仍然會自然施壓"

  lookup_refs:
    hot:
    master:
    index:
```

---

# 25｜五至六輪實跑方式

不要一輪就決定成敗。

建議：

```text
ROUND 1
新場景接關

ROUND 2
發生第一次新的關係變化

ROUND 3
出現帳務／契約／知情更新

ROUND 4
有 NPC↔NPC 線在玩家不介入時繼續作用

ROUND 5
跨場景或跨日後重新載入

ROUND 6
最好做一次 MASTER / INDEX reconciliation
```

不要求六輪每次都同類型。

重點是要遇到不同壓力。

---

# 26｜每輪測試紀錄

```yaml
RELATION_FIRST_TEST_ROUND:

  round_id:
  route_id:
  source_hot_ref:
  source_master_ref:
  source_index_ref:

  pre_scene_relational_center: []

  scene_material_events: []

  relation_deltas_claimed: []

  relation_deltas_actually_qualified: []

  material_facts_changed: []

  unresolved_preserved: []

  errors:
    premature_relation_promotion: []
    forgotten_npc_npc_relation: []
    forgotten_material_fact: []
    stale_index_used_as_truth: []
    unknown_collapsed: []
    player_sovereignty_violation: []
    overpsychologizing: []

  continuation_quality:
    character_position_drift:
      - NONE
      - LOW
      - MEDIUM
      - HIGH

    relation_readability:
      - POOR
      - FAIR
      - GOOD
      - EXCELLENT

    material_recovery:
      - PASS
      - FAIL

    evidence_traceability:
      - PASS
      - FAIL

  verdict:
    - PASS
    - PASS_WITH_NOTES
    - HOLD
    - FAIL
```

---

# 27｜六輪後比較指標

不要只問：

```text
好不好看？
```

要問：

```yaml
SIX_ROUND_REVIEW:

  relational_continuity:
    question: "人物位置是否比舊 HOT 更穩？"

  relation_overpromotion:
    question: "是否更少出現合作一次就變朋友／戀人／盟友？"

  npc_npc_retention:
    question: "玩家以外的重要關係是否比較不會消失？"

  material_fact_retention:
    question: "錢、物件、契約、知情是否有被 relation-first 吃掉？"

  unknown_preservation:
    question: "未演出的付款／登記／承諾是否仍保持 UNKNOWN？"

  evidence_traceability:
    question: "每條關係結論能否回查事件？"

  token_priority:
    question: "第一屏是否比舊 HOT 更快進入真正張力？"

  director_drift:
    question: "跨輪後是否較少重置人物關係？"

  false_psychology:
    question: "是否開始把位置誤寫成心情？"

  index_integrity:
    question: "索引是否仍只是指路，而沒有變成第二世界？"
```

---

# 28｜判定門檻

## PASS

```text
關係接續更穩
+
非玩家關係保留改善
+
沒有犧牲 material facts
+
沒有提高關係腦補
+
evidence refs 仍可追
```

## HOLD

任一：

```text
關係摘要越來越長，反而比事件更難讀
RELATIONAL CENTER 開始全人物化
STILL_NOT 無限膨脹
索引與 HOT 出現不同版本事實
大量關係只能靠 AI 心理解讀才能成立
```

## FAIL

任一：

```text
外掛創造未發生的感情／承諾／義務
外掛覆寫原始事件
外掛把 UNKNOWN 補成已完成
外掛吞掉付款／契約／物權／位置等硬事實
外掛被當成正式 source of truth
外掛開始決定人物下一步必須做什麼
```

---

# 29｜Rollback

因本文件是外接投影層：

```text
DISABLE OVERLAY
↓
RETURN TO ORIGINAL HOT / MASTER / INDEX
```

不需要：

```text
回寫歷史
修 MASTER
重做 EVENT
撤銷角色狀態
```

前提是實跑期間遵守：

```text
OVERLAY NEVER OWNS CANONICAL WRITES
```

---

# 30｜正式升版前的必要問題

五六輪測完後再決定：

```text
Q1
是否真的需要 SAVE schema change？

Q2
還是只要把 Projection Rule 正式化即可？

Q3
RELATIONAL CENTER 應該內嵌 HOT，
還是由 Director Bootstrap 動態編譯？

Q4
RCL 是否已足夠承載 relation index，
還是需要正式 RELATION_ROUTE_INDEX？

Q5
PERSON↔INSTITUTION 是否足夠？
是否真的有必要再擴張 node 類型？

Q6
哪些 relation labels 應完全自由文字，
哪些需要 enum？

Q7
五六輪後，B 是否真的比原 HOT 更少角色漂移？
```

在這些答案出來以前：

```text
NO CORE V3.12 CLAIM
NO SAVE V2.0 CLAIM
NO FORMAL RATIFICATION CLAIM
```

---

# 31｜推薦實跑法

最推薦的測試方式不是每輪做 A/B 雙寫。

而是：

```text
原始 HOT / MASTER / INDEX
照舊保存

每次接關前
額外生成 RELATION-FIRST VIEW

導演用：
RELATION-FIRST VIEW
+
必要的 HOT material facts
來接戲

結束後
仍照舊用原 SAVE Runtime commit
```

也就是：

```text
WRITE PATH
維持舊制

READ PATH
先換成 Relation-First
```

這樣才能真的知道：

> 問題是不是出在「寫法」，
> 還是其實只出在「讀法」。

---

# 32｜最終根句

```text
SAVE 不替角色活。

SAVE 只保存角色已經活過之後，
世界真正留下的東西。

EVENT 告訴我們：
發生了什麼。

MASTER 告訴我們：
什麼已經成為世界。

HOT 告訴我們：
下一幕最低需要知道什麼。

INDEX 告訴我們：
去哪裡找。

RELATIONAL PROJECTION 告訴我們：
因此，現在大家彼此站在哪裡。
```

最後：

> **先讓證據成立。**
>
> **再讓關係顯影。**
>
> **最後才讓下一幕開始。**

---

# 33｜版本狀態

```yaml
DOCUMENT_STATUS:
  name: "GUANZHI SAVE RELATION-FIRST EXTERNAL OVERLAY"
  version: "V0.3-FULL-EXP"
  date: "2026-10-07"

  intended_test_duration:
    minimum_effective_rounds: 5
    preferred_effective_rounds: 6

  formal_status:
    normative: false
    ratified: false
    host_deployed: false

  architecture:
    core_changed: false
    save_schema_changed: false
    save_write_owner_changed: false
    relation_qualification_owner_changed: false

  test_mode:
    read_path_changed: true
    write_path_changed: false

  rollback:
    remove_overlay_only: true
```

**END OF GUANZHI SAVE RELATION-FIRST EXTERNAL OVERLAY V0.3-FULL-EXP**
