\
# 觀止青樓｜白御行線 HOT SAVE V1.0
## 理火三年槐月十日清晨｜第六日接關切片

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V1_0_HUAI10_MORNING"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V1.0"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime: "GUANZHI_QINGLOU_V10.0"
  date_created: "2026-08-03"
  state_class: "ACTIVE"

SOURCE_LOCK:
  master_archive:
    file: "觀止青樓_白御行線_MASTER_SAVE_V3.0-R1_正式厚肉因果資料庫版.md"
    version: "V3.0-R1"
    sha256: "57311f329b845cf256a426ffcc034fcb9bee122bb4b29d711687858c07714040"

  runtime_spec:
    file: "觀止青樓_SAVE_Runtime_V1.0_MASTER_HOT_PATCH_CORRUPTION四層記憶架構正式版.md"
    version: "V1.0"

LOAD_PROFILE:
  purpose: "NEXT_SCENE_DIRECT_RESUME"
  full_master_load_required: false
  persona_full_cards_load:
    default: "ACTIVE_CAST_ONLY"
  recent_event_window:
    - "E27"
    - "E28"
    - "E29"
    - "E30"
```

> **本 HOT 只保存槐月十日清晨下一幕需要運行的世界。**
>
> **完整事件與舊人物線按 E01—E30 回查 MASTER，不在本檔重複搬運。**

---

# 1｜當前時間與場景

```yaml
CURRENT_TIME:
  era: "理火三年"
  calendar_date: "槐月十日"
  time_of_day: "清晨"
  route_progress: "第五夜已結束／第六日開始"
  certainty: "CONFIRMED"

CURRENT_SCENE:
  location: "觀止"
  scene_state: "夜宴散場善後"
  immediate_world_motion:
    - "人物處理返程、留觀止或待決"
    - "帳房處理昨夜酒帳與未交付事項"
    - "紅袖冰蠶弦於本日到期"
  player_next_action_owner: "PLAYER"
```

---

# 2｜玩家硬狀態

```yaml
PLAYER_HARD_STATE:
  player_id: "BAI_YUXING"
  public_identity: "白御行／定陶商會總會長"
  current_location: "觀止"
  current_condition:
    - "清醒"
    - "沒有飲酒"
    - "第五夜尾聲曾假醉以取得與張麗華私談"

  visible_relation_policy:
    - "不再提供正式妻位"
    - "不承諾只愛一人"
    - "可能繼續追求其他女人"
    - "願意以金錢與資源改變選擇環境"

  next_action_owner: "PLAYER"

  forbidden_ai_fill:
    - "不得替白御行決定今日先找誰"
    - "不得替白御行承認悔悟"
    - "不得替白御行簽署任何契約"
    - "不得把假醉寫成真醉"
```

---

# 3｜活躍人物載入清單

```yaml
ACTIVE_CAST:
  SCENE_CORE:
    - character: "潘金蓮"
      load_level: "SCENE_FOCUS"
      reason:
        - "MASTER SAVE 保管者"
        - "酒帳、說書資金與未完成契約實務中介"

    - character: "張麗華"
      load_level: "SCENE_FOCUS"
      reason:
        - "第五夜私人提案仍未決"
        - "官人傳聞與話本操盤直接相關"

    - character: "蘇清"
      load_level: "SCENE_FOCUS"
      reason:
        - "舊三晚契約未結帳"
        - "話本委託條件已提出；蘇清是否明確接受，MASTER 記錄有歧義"

    - character: "紅袖"
      load_level: "SCENE_FOCUS"
      reason:
        - "冰蠶弦本日到期"
        - "似伊未來影像造成的不安仍為開放線"

  DECISION_PENDING:
    - character: "李清照"
      load_level: "ACTIVE_CARD"
      reason: "回原時代或留觀止未決"

    - character: "李師師"
      load_level: "ACTIVE_CARD"
      reason: "回靖康或留觀止掛牌未決"

  LOCAL_SUPPORT:
    - character: "醉花"
      load_level: "ACTIVE_CARD"
      reason: "持有三十年女兒紅剩餘處理權"

  INDEX_ONLY:
    - "浮香"
    - "辭歲"
    - "十三娘"
    - "趙受益"
    - "蘇東坡"
    - "柳如煙"
    - "白玉池無名女子"
```

`INDEX_ONLY` 人物不應自行進場，除非世界因果、玩家行動或新事件合理召入。

---

# 4｜當前關係硬狀態

## 4.1 潘金蓮

```yaml
RELATIONSHIP_STATE:
  relation_id: "REL_BAI_PAN"
  actor_a: "白御行"
  actor_b: "潘金蓮"
  state_class: "ACTIVE"
  state_label: "ACTIVE_WORKING_RELATION"
  established_roles:
    - "觀止掌櫃"
    - "帳目與契約記錄者"
    - "白御行線 SAVE 保管者"
    - "傳聞與物資安排實務中介"
  romance_status: "NOT_ESTABLISHED"
  last_delta_event_id: "E30"
```

## 4.2 張麗華

```yaml
RELATIONSHIP_STATE:
  relation_id: "REL_BAI_ZHANG"
  actor_a: "白御行"
  actor_b: "張麗華"
  state_class: "UNDECIDED"
  state_label: "HIGH_TENSION_PRIVATE_NONMARRIAGE_OFFER_OPEN"

  confirmed:
    - "第五夜所有婚約與資產條件已由白御行收回"
    - "公開兩次官人稱呼只為酒局取酒"
    - "私下無婚書伴侶提案尚未接受"

  active_offer:
    nature: "無婚書、自定義稱謂的伴侶關係"
    accepted: false

  romance_status: "NOT_ADJUDICATED"
  marriage_status: "NONE"
  exclusivity_status: "NONE"
  last_delta_event_id: "E27"
```

## 4.3 蘇清

```yaml
RELATIONSHIP_STATE:
  relation_id: "REL_BAI_SU"
  actor_a: "白御行"
  actor_b: "蘇清"
  state_class: "UNSETTLED"
  state_label: "OLD_SEXUAL_TRANSACTION_UNSETTLED_PLUS_ACTIVE_WRITING_COMMISSION"

  old_contract:
    contract_id: "CONTRACT_BAI_SU_THREE_NIGHTS"
    original_term: "五百兩，三晚性交易，排除感情承諾"
    performance_completed: "ZERO_OF_THREE"
    consent_history:
      - "三晚均在性交前有效拒絕"
    bai_position: "BREACH_ALLEGED"
    su_position: "BREACH_NOT_ADMITTED"
    settlement_status: "UNSETTLED"

  writing_commission:
    contract_id: "COMMISSION_SU_ZHANG_STORY"
    contractor_acceptance_status: "AMBIGUOUS_IN_MASTER_REQUIRES_CONFIRMATION"
    work_submission_status: "NOT_SUBMITTED"
    client_acceptance_status: "NOT_REVIEWED"
    payment_status: "UNPAID_CONDITIONAL"
    schedule: "每日四千字；十日一本"

  romance_status: "NOT_ESTABLISHED"
  last_delta_event_id: "E28"
```

## 4.4 紅袖

```yaml
RELATIONSHIP_STATE:
  relation_id: "REL_BAI_HONGXIU"
  actor_a: "白御行"
  actor_b: "紅袖"
  state_class: "ACTIVE"
  state_label: "DISTURBED_BUT_NOT_SURRENDERED"

  confirmed:
    - "似伊／紅奴影像造成不安與疑問"
    - "未承認未來紅奴線必然成立"
    - "未同意訓練"
    - "未接受如夫人邀請"

  due_item:
    ledger_id: "LEDGER_HONGXIU_ICE_SILKWORM_STRINGS"
    item: "冰蠶弦一盒"
    status: "ORDERED_NOT_DELIVERED"
    due: "槐月十日"

  current_identity: "紅袖"
  must_not_merge_with: "似伊"
  last_delta_event_id: "E25"
```

## 4.5 李清照

```yaml
RELATIONSHIP_STATE:
  relation_id: "REL_BAI_LIQINGZHAO"
  state_class: "UNDECIDED"
  state_label: "MUTUAL_LITERARY_ATTENTION_WITH_STAY_OR_RETURN_PENDING"
  marriage_offer: "REJECTED"
  poetry_result_changes_marriage: false
  current_choice: "回自身時代或留觀止"
  romance_status: "NOT_ADJUDICATED"
  last_delta_event_id: "E30"
```

## 4.6 李師師

```yaml
RELATIONSHIP_STATE:
  relation_id: "REL_BAI_LISHISHI"
  state_class: "UNDECIDED"
  state_label: "ROUTE_GUEST_WITH_STAY_OR_RETURN_PENDING"
  current_choice: "回靖康或留觀止掛牌"
  staged_relation_with_zhao: "NOT_REAL"
  contract_status: "NONE"
  last_delta_event_id: "E30"
```

---

# 5｜活躍契約與帳目

```yaml
ACTIVE_CONTRACTS:
  SU_QING_THREE_NIGHT_TRANSACTION:
    contract_id: "CONTRACT_BAI_SU_THREE_NIGHTS"
    state_class: "UNSETTLED"
    original_terms:
      - "五百兩"
      - "三晚性交易"
      - "感情承諾排除"
    performance: "ZERO_OF_THREE_INTERCOURSE_COMPLETED"
    consent_withdrawal_each_night: "VALID"
    settlement: "PENDING"
    master_lookup:
      - "RELATION_SU_QING"
      - "E06"

  SU_QING_NOVEL_COMMISSION:
    contract_id: "COMMISSION_SU_ZHANG_STORY"
    state_class: "CONTESTED"
    contractor_acceptance_status: "AMBIGUOUS_IN_MASTER_REQUIRES_CONFIRMATION"
    submission_status: "NOT_SUBMITTED"
    client_acceptance_status: "NOT_REVIEWED"
    payment_status: "UNPAID_CONDITIONAL"
    reward: "五百兩"
    schedule: "每日四千字；十日一本"
    master_lookup:
      - "E28"

ACTIVE_LEDGER:
  HONGXIU_ICE_SILKWORM_STRINGS:
    state_class: "ACTIVE"
    status: "ORDERED_NOT_DELIVERED"
    due: "槐月十日"

  STORYTELLER_PUBLICITY:
    amount_intended: "二十兩"
    actually_delivered_to_storyteller: "NOT_RECORDED"
    status: "UNSETTLED"

  ZHANG_SELF_CARVING_BOARDS:
    item: "十塊木板"
    status: "PROMISED_NOT_DELIVERED"

  ZHANG_WINE_ACCOUNT:
    amount: "一萬兩"
    status: "POSTED_ACTIVE"
    owner_for_accounting: "張麗華專用"
    bai_asset: false
    exact_debit: "UNKNOWN"

  THIRTY_YEAR_NUERHONG:
    control_right: "醉花"
    bai_control_relinquished: true
    exact_remaining_quantity: "UNKNOWN"
```

---

# 6｜最近四個確認事件

```yaml
RECENT_EVENTS:
  E27:
    title: "假醉進張麗華房間與私人關係提案"
    result:
      - "白御行未飲酒、沒有醉"
      - "張麗華未接受無婚書伴侶提案"
      - "婚姻仍未成立"

  E28:
    title: "傳聞與話本操盤計畫"
    result:
      - "二十兩說書資金有意向，實際轉付未記錄"
      - "蘇清接入商業寫作委託"
      - "十塊木板尚未交付"
      - "全城傳聞尚未成立"

  E29:
    title: "自由意志、選擇環境與時間窗口爭論"
    result:
      - "白御行明示會改變外部選擇環境"
      - "張麗華仍未選擇白御行"
      - "環境影響不得寫成已控制人心"

  E30:
    title: "第五夜善後與人物去留"
    result:
      - "第五夜結束"
      - "槐月十日清晨開始"
      - "李清照、李師師去留未決"
      - "趙受益、蘇東坡準備返程"
```

---

# 7｜立即到期事項

```yaml
DUE_ITEMS:
  PRIORITY_1:
    item: "紅袖冰蠶弦交付"
    due: "槐月十日"
    current_status: "ORDERED_NOT_DELIVERED"
    must_not_imply:
      - "收下即同意訓練"
      - "收下即接受如夫人"
      - "收下即成為似伊"

  PRIORITY_2:
    item: "李清照與李師師去留"
    due: "清晨善後時段"
    current_status: "UNDECIDED"

  PRIORITY_3:
    item: "潘金蓮核對昨夜酒帳、說書資金與未完成承諾"
    due: "清晨帳房程序"
    current_status: "WORLD_MAY_ADVANCE_NATURALLY"
```

---

# 8｜立即開放伏筆

```yaml
IMMEDIATE_OPEN_HOOKS:
  - hook_id: "HOOK_HONGXIU_STRINGS"
    question: "冰蠶弦是否如期交付，紅袖如何處理？"

  - hook_id: "HOOK_ZHANG_PRIVATE_OFFER"
    question: "張麗華是否在清醒狀態回應無婚書伴侶提案？"

  - hook_id: "HOOK_SU_WRITING_DAY1"
    question: "蘇清是否明確接受委託；若接受，何時開始交付第一日四千字？"

  - hook_id: "HOOK_STORYTELLER_FUNDS"
    question: "潘金蓮是否已把二十兩交給說書先生？"

  - hook_id: "HOOK_LI_DECISIONS"
    question: "李清照與李師師是否留在觀止？"

  - hook_id: "HOOK_WHITE_JADE_POOL_WOMAN"
    question: "白玉池無名女子是否再度聯絡？"
    load_policy: "DO_NOT_ACTIVATE_WITHOUT_NEW_CAUSE"
```

---

# 9｜知情與傳聞

```yaml
KNOWLEDGE_AND_RUMOR:
  PUBLIC_CONFIRMED:
    - "大堂十幾桌聽見張麗華兩次以官人求酒"
    - "李清照親口承認白御行詩勝"
    - "第五夜女兒紅酒局與多場戲中戲"

  PRIVATE:
    - "白御行假醉進張麗華房間"
    - "無婚書伴侶提案完整條件"

  RUMOR:
    GUANREN_RUMOR:
      propagation_status: "PLANNED_OR_LOCAL_NOT_CITYWIDE_CONFIRMED"
      active_promotion_planned: true
      storyteller_distribution_started: "NOT_RECORDED"

    MARRIAGE_RUMOR:
      reality: "無婚書、未成婚"
      likely_distortion:
        - "白御行以酒收服張麗華"
        - "兩人已有婚約"
```

---

# 10｜本輪禁止推斷

1. 不得自動讓張麗華接受無婚書伴侶提案。
2. 不得把兩次「官人」寫成婚姻同意。
3. 不得恢復已撤回的酒莊、薔薇園、三烤鹽與定陶商會婚約條件。
4. 不得把蘇清三晚交易寫成已完成性交。
5. 不得把蘇清三晚拒絕寫成欲拒還迎。
6. 不得讓蘇清用倫理分析永久逃避結算狀態。
7. 不得把紅袖收下冰蠶弦寫成同意訓練、如夫人或紅奴未來。
8. 不得把紅袖與似伊合併。
9. 不得把李清照詩局輸掉寫成婚姻條件改變。
10. 不得把李師師與趙受益戲中位置寫成真實戀情。
11. 不得把說書計畫寫成已經全城傳遍。
12. 不得替白御行選擇清晨第一步。
13. 不得因世界可自然運行，就一次跳過多個事件。
14. 不得以「關係重新定價」取代可觀察事件。

---

# 11｜MASTER 查詢索引

```yaml
MASTER_LOOKUP_INDEX:
  TIME:
    - "第 1 區"

  PLAYER_HARD_STATE:
    - "第 2 區"

  RELATIONSHIPS:
    PAN_JINLIAN: "3.1"
    ZHANG_LIHUA: "3.4"
    SU_QING: "3.5"
    ZUIHUA: "3.6"
    HONGXIU: "3.8"
    LI_QINGZHAO: "3.9"
    LI_SHISHI: "3.10"

  EVENTS:
    SU_QING_CONTRACT: "E06"
    GUANREN_PUBLIC_CALL: "E13"
    MARRIAGE_ASSETS_WITHDRAWN: "E17"
    CHEN_SHUBAO_AND_RELATION_SHIFT: "E18"
    PRIVATE_NONMARRIAGE_OFFER: "E27"
    RUMOR_AND_WRITING_PLAN: "E28"
    FREE_WILL_ENVIRONMENT_ARGUMENT: "E29"
    CURRENT_END_STATE: "E30"

  LEDGER:
    - "第 6 區"

  CONSENT:
    - "第 8 區"

  OPEN_HOOKS:
    - "第 10 區"

  FORBIDDEN_REWRITES:
    - "第 11 區"
```

---

# 12｜下一幕接關點

```yaml
CONTINUATION_POINT:
  exact_time: "理火三年槐月十日清晨"
  location: "觀止"
  scene: "第五夜夜宴散場善後"

  player_state:
    - "白御行清醒"
    - "下一動作由玩家決定"

  world_may_initiate_one_beat:
    - "潘金蓮帶帳目或到期事項來報"
    - "紅袖冰蠶弦交付程序啟動"
    - "李清照或李師師作出去留前的具體行動"

  world_must_not_auto_complete:
    - "婚姻"
    - "伴侶接受"
    - "性交契約結算"
    - "全城傳聞"
    - "話本出版"
    - "木板交付"
    - "白玉池無名女子再度出現"
```

## 最小啟動句

> 槐月十日的清晨已經進了觀止。昨夜留下的酒氣還在，帳房與交付程序先醒了。白御行沒有醉；下一步仍由他自己決定。

此句只建立場景，不替玩家行動。
