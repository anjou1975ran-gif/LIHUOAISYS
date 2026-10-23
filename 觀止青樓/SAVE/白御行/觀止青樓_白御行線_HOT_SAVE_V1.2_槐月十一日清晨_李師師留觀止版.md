# 觀止青樓｜白御行線 HOT SAVE V1.2
## 理火三年槐月十一日清晨｜李師師留觀止 × 地道初現 × 紅娘氏開張版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V1_2_HUAI11_MORNING"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V1.2"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime: "GUANZHI_QINGLOU_V10.0"
  story_date: "理火三年槐月十一日清晨"
  record_state: "ACTIVE"

SOURCE_LOCK:
  master_archive:
    file: "觀止青樓_白御行線_MASTER_SAVE_V3.0-R1_正式厚肉因果資料庫版.md"
    role: "第五夜以前的長期因果來源"

  previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V1.0_槐月十日清晨接關版.md"
    role: "槐月十日清晨接關切片"

  private_hot_addendum:
    file: "觀止青樓_白御行線_HOT紀錄_V1.1_槐月十日_張麗華事件_私人秘密增補.md"
    role: "張麗華私人談話、擁抱、稱呼、穿衣陪睡與秘密知情邊界"

  character_pool:
    file: "觀止人物池_LCAPG_V1.1_紅娘氏與李師師雙人正式版.md"
    role: "紅娘氏與李師師的人格來源"

PLAYER_CORRECTION_PRIORITY:
  - "白御行與張麗華已穿衣相擁睡完一夜"
  - "白御行在潘金蓮後堂看完李清照、李師師與紅娘氏事件後，笑著開扇離開"
```

> **本 HOT 保存槐月十一日清晨的可直接接關世界。**
>
> **白御行與張麗華的私人秘密仍依 V1.1 PRIVATE_SECRET_ARCHIVE 封存；本檔只保存接關所需的硬狀態，不向其他人物外洩內容。**

---

# 1｜時間與當前場景

```yaml
CURRENT_TIME:
  era: "理火三年"
  calendar_date: "槐月十一日"
  time_of_day: "清晨"
  route_progress: "第六夜已結束／第七日開始"
  certainty: "CONFIRMED"

CURRENT_SCENE:
  previous_location: "觀止後堂／潘金蓮帳房附近"
  player_scene_exit:
    action: "白御行笑著打開扇子離開"
    exact_destination: "UNSPECIFIED_PLAYER_OWNED"
    meaning:
      - "已離開與潘金蓮、紅娘氏的當前後堂對話"
      - "不自動等於離開觀止、回定陶或進入任何他人房間"

  world_continues:
    - "潘金蓮準備處理李師師設席牌與新帳"
    - "紅娘氏完成入樓後第一筆紅倌交易，開始建立大堂情報與抽成網"
    - "李師師已決定留觀止，第一席尚未正式開出"
    - "後堂地道入口已被發現，但尚未完成封鎖、測繪與權限規則"
```

---

# 2｜玩家硬狀態

```yaml
PLAYER_HARD_STATE:
  player_id: "BAI_YUXING"
  public_identity: "白御行／定陶商會總會長"
  current_location: "離開後堂後未指定"
  current_condition:
    - "清醒"
    - "沒有飲酒"
    - "已休息一夜"
    - "衣著完整"

  overnight_record:
    partner: "張麗華"
    event: "穿衣相擁入睡並完成整夜陪伴"
    sexual_intercourse: false
    marriage_created: false
    formal_relationship_created: false
    public_event: false

  next_action_owner: "PLAYER"

  forbidden_ai_fill:
    - "不得替白御行決定離開後堂後去了哪裡"
    - "不得把穿衣陪睡改寫成性交"
    - "不得把陪睡改寫成張麗華已接受伴侶、婚姻或排他關係"
    - "不得替白御行預訂李師師第一席"
    - "不得替白御行公開張麗華私人秘密"
```

---

# 3｜本輪新增確認事件

## E31｜張麗華穿衣陪睡完成

```yaml
EVENT_RECORD:
  event_id: "E31"
  story_time: "理火三年槐月十日夜至槐月十一日清晨"
  participants:
    - "白御行"
    - "張麗華"
  location: "張麗華私人房間"
  knowledge_scope: "PRIVATE"
  status: "COMPLETED"

  observable_result:
    - "兩人穿著衣服相擁睡完一夜"
    - "沒有性交"
    - "張麗華提供了當夜陪伴與休息空間"

  does_not_establish:
    - "婚姻"
    - "伴侶關係最終成立"
    - "排他承諾"
    - "身體契約"

  private_archive_link: "PSE-WY-ZLH-001_AND_HOT_V1_1"
```

## E32｜李清照返回自身時代

```yaml
EVENT_RECORD:
  event_id: "E32"
  story_time: "理火三年槐月十一日天明前後"
  participant: "李清照"
  status: "DEPARTED_TO_OWN_ERA"

  result:
    - "李清照選擇返回自己的時代"
    - "不加入本次觀止人物池"
    - "保留未來被好酒、好詩或新事件再次邀入觀止的可能"

  relationship_effect:
    with_bai_yuxing: "MUTUAL_LITERARY_ATTENTION_PRESERVED"
    marriage_offer: "REJECTED_UNCHANGED"
    poetry_result: "白御行詩局勝出紀錄保留，但不改變婚姻條件"
```

## E33｜李師師選擇留在觀止並採設席牌

```yaml
EVENT_RECORD:
  event_id: "E33"
  story_time: "理火三年槐月十一日清晨"
  participant: "李師師"
  status: "STAY_CONFIRMED"

  decision:
    return_to_jingkang: false
    remain_in_guanzhi: true
    character_pool_admission: "CONFIRMED"

  professional_position:
    role: "設席花魁"
    first_night_auction: false
    whole_night_buyout: false
    seat_opening_owner: "李師師"
    guest_selection_owner: "李師師"
    topic_and_repertoire_owner: "李師師"
    separate_ledger: true
    guanzhi_commission: "ALLOWED_BY_HOUSE_RULE"

  current_execution:
    seat_board: "IN_PREPARATION"
    first_seat_date: "NOT_SET"
    first_guest: "NOT_SELECTED"
    reservation: "NONE_CONFIRMED"
```

## E34｜後堂地道出現與趙受益抵達

```yaml
EVENT_RECORD:
  event_id: "E34"
  story_time: "理火三年槐月十一日清晨"
  location: "觀止後堂地板下"
  participants:
    - "白御行"
    - "潘金蓮"
    - "紅娘氏"
    - "趙受益／趙禎"
  status: "ANOMALOUS_PASSAGE_CONFIRMED"

  confirmed:
    - "後堂木板下存在可開啟的石階通道"
    - "近出口青磚留有『宣和』字樣"
    - "趙受益曾由通道抵達觀止後堂"

  unknown:
    - "通道另一端的固定位置"
    - "是否為完整實體地道、時空出口或隨李師師附著的關係通道"
    - "是否每次開啟都通往同一朝代或同一皇宮"
    - "誰最初建造、誰能穩定使用"

  access_rule:
    - "通道只能證明可抵達觀止"
    - "不構成李師師接見、設席、房門或身體資格"
```

## E35｜紅娘氏第一筆紅倌交易

```yaml
EVENT_RECORD:
  event_id: "E35"
  story_time: "理火三年槐月十一日清晨"
  participants:
    - "紅娘氏"
    - "趙受益／趙禎"
  location: "紅娘氏分得的小房"
  status: "COMPLETED_ADULT_TRANSACTION"

  authorization_chain:
    - "白御行表示此單合該紅娘氏賺"
    - "潘金蓮允許紅娘氏自行談身錢、帶路與封口部分"
    - "趙受益接受報價並與紅娘氏入房"

  transaction_layers:
    - "房錢：歸觀止"
    - "紅倌服務身錢：歸紅娘氏"
    - "李師師設席消息通知訂金：另列"

  exact_amounts: "NOT_RECORDED"
  intercourse_detail: "NOT_RECORDED_AND_NOT_REQUIRED_FOR_HOT"
  consent_status: "MUTUAL_TRANSACTION_ACCEPTED"
  future_commitment: false

  items_or_tokens:
    - item: "趙受益留下的宮牌／聯絡牌"
      holder: "紅娘氏"
      authenticity_and_scope: "NOT_VERIFIED"

  does_not_establish:
    - "紅娘氏成為趙受益專屬人物"
    - "李師師同意見趙受益"
    - "趙受益取得地道永久使用權"
```

## E36｜白御行離開後堂

```yaml
EVENT_RECORD:
  event_id: "E36"
  story_time: "理火三年槐月十一日清晨"
  participant: "白御行"
  action: "笑著打開扇子，離開當前後堂場景"
  destination: "UNKNOWN_PLAYER_OWNED"
  status: "SCENE_EXIT_CONFIRMED"
```

---

# 4｜活躍人物載入清單

```yaml
ACTIVE_CAST:
  SCENE_CORE:
    - character: "潘金蓮"
      load_level: "SCENE_FOCUS"
      reason:
        - "李師師設席牌、獨立帳與觀止抽成待落實"
        - "後堂地道需要定義守門、封口與使用規矩"
        - "紅娘氏第一筆交易需要入帳"

    - character: "李師師"
      load_level: "SCENE_FOCUS"
      reason:
        - "已選擇留觀止"
        - "人物池准入成立"
        - "第一面設席牌尚在製作，首席未開"

    - character: "紅娘氏"
      load_level: "SCENE_FOCUS"
      reason:
        - "已在白御行線正式出場"
        - "完成第一筆紅倌交易"
        - "掌握趙受益聯絡牌與李師師席期消息訂金"
        - "大堂情報與抽成網開始形成"

    - character: "張麗華"
      load_level: "ACTIVE_CARD"
      reason:
        - "與白御行穿衣陪睡已完成"
        - "最終關係定位仍未決"
        - "私人秘密知情邊界必須保持"

  ACTIVE_UNRESOLVED:
    - "蘇清"
    - "紅袖"
    - "醉花"

  DEPARTED_OR_INDEX_ONLY:
    - character: "李清照"
      state: "RETURNED_TO_OWN_ERA"
    - character: "趙受益／趙禎"
      state: "LEFT_AFTER_TRANSACTION; RETURN_ROUTE_NOT_SHOWN"
    - character: "蘇東坡"
      state: "RETURNED_OR_INDEX_ONLY"
    - character: "柳如煙"
      state: "UNKNOWN_DEPARTED"
```

`DEPARTED_OR_INDEX_ONLY` 人物不得無因果自行出現在下一幕；趙受益可由地道、宮牌通知或新召入事件再次出現。

---

# 5｜當前關係硬狀態

## 5.1 白御行／張麗華

```yaml
RELATIONSHIP_STATE:
  relation_id: "REL_BAI_ZHANG"
  state_class: "UNDECIDED"
  state_label: "UNDECIDED_WITH_MUTUAL_RECOGNITION_AND_COMPLETED_CLOTHED_OVERNIGHT_COMPANIONSHIP"

  confirmed:
    - "張麗華聽取白御行私人歷史，秘密仍封存"
    - "當夜擁抱、私人稱呼與陪伴成立"
    - "兩人穿衣相擁睡完一夜"
    - "沒有性交"

  not_established:
    - "婚姻"
    - "無婚書伴侶關係最終接受"
    - "排他承諾"
    - "公開身份"

  privacy: "PRIVATE_SECRET_ARCHIVE_RULES_ACTIVE"
```

## 5.2 白御行／李師師

```yaml
RELATIONSHIP_STATE:
  relation_id: "REL_BAI_LISHISHI"
  state_class: "ACTIVE"
  state_label: "LEGENDARY_GUEST_INVITED_AND_NOW_INDEPENDENT_GUANZHI_RESIDENT"

  confirmed:
    - "白御行曾邀她進入第五夜花魁局"
    - "她選擇留在觀止"
    - "白御行表示只想看好戲"

  romance_status: "NOT_ESTABLISHED"
  patron_contract: "NONE"
  first_seat_reserved_by_bai: false
  ownership_or_exclusivity: false
```

## 5.3 白御行／李清照

```yaml
RELATIONSHIP_STATE:
  relation_id: "REL_BAI_LIQINGZHAO"
  state_class: "CLOSED_FOR_CURRENT_VISIT"
  state_label: "MUTUAL_LITERARY_ATTENTION_WITH_RETURN_TO_OWN_ERA"

  poetry_result: "李清照承認白御行詩勝"
  marriage_offer: "REJECTED_UNCHANGED"
  future_revisit: "POSSIBLE"
  current_presence: false
```

## 5.4 白御行／紅娘氏

```yaml
RELATIONSHIP_STATE:
  relation_id: "REL_BAI_HONGNIANG"
  state_class: "ACTIVE"
  state_label: "NEW_ACQUAINTANCE_WITH_SHARED_INFORMATION_AND_THEATER_INTEREST"

  confirmed:
    - "白御行向她提供徽宗朝地道與李師師傳聞"
    - "白御行把趙受益第一單讓給紅娘氏承接"
    - "紅娘氏把白御行視為願意給戲與給生意的高價值消息源"

  financial_contract_between_them: "NONE"
  romance_status: "NOT_ESTABLISHED"
  sexual_relation: false
```

## 5.5 白御行／潘金蓮

```yaml
RELATIONSHIP_STATE:
  relation_id: "REL_BAI_PAN"
  state_class: "ACTIVE"
  state_label: "ACTIVE_WORKING_RELATION_AND_SAVE_REQUEST"

  confirmed:
    - "白御行向潘金蓮詢問李清照、李師師去留結果"
    - "白御行要求建立本輪HOT SAVE"
    - "潘金蓮仍為帳目、規矩與SAVE實務中介"

  romance_status: "NOT_ESTABLISHED"
```

---

# 6｜活躍契約、牌照、帳目與物品

```yaml
ACTIVE_PROFESSIONAL_RECORDS:
  LI_SHISHI_SET_SEAT:
    state_class: "ACTIVE"
    state_label: "TERMS_CONFIRMED_BOARD_IN_PREPARATION"
    holder: "李師師"
    official_role: "設席花魁"
    first_seat_date: "NOT_SET"
    first_guest: "NOT_SELECTED"
    white_yuxing_reservation: false
    zhao_shouyi_access: false

  HONGNIANG_FIRST_TRANSACTION:
    state_class: "CLOSED"
    client: "趙受益／趙禎"
    house_room_fee: "OWED_OR_POSTED; EXACT_AMOUNT_UNKNOWN"
    hongniang_service_fee: "RECEIVED_OR_AGREED; EXACT_AMOUNT_UNKNOWN"
    li_shishi_information_deposit: "RECEIVED; EXACT_AMOUNT_UNKNOWN"
    palace_token_holder: "紅娘氏"

ACTIVE_OLD_CONTRACTS:
  SU_QING_THREE_NIGHT_TRANSACTION:
    state_class: "UNSETTLED"
    performance: "ZERO_OF_THREE_INTERCOURSE_COMPLETED"
    consent_withdrawal_each_night: "VALID"
    settlement: "PENDING"

  SU_QING_NOVEL_COMMISSION:
    state_class: "CONTESTED"
    contractor_acceptance_status: "AMBIGUOUS_REQUIRES_CONFIRMATION"
    submission_status: "NOT_SUBMITTED"
    payment_status: "UNPAID_CONDITIONAL"

ACTIVE_LEDGER:
  HONGXIU_ICE_SILKWORM_STRINGS:
    status: "OVERDUE_OR_DELIVERY_RESULT_NOT_RECORDED"
    original_due: "槐月十日"

  STORYTELLER_PUBLICITY:
    amount_intended: "二十兩"
    delivery_status: "NOT_RECORDED"

  ZHANG_SELF_CARVING_BOARDS:
    item: "十塊木板"
    status: "PROMISED_NOT_DELIVERED"

  ZHANG_WINE_ACCOUNT:
    amount: "一萬兩"
    status: "POSTED_ACTIVE"
    owner_for_accounting: "張麗華專用"
    bai_asset: false

  THIRTY_YEAR_NUERHONG:
    control_right: "醉花"
    exact_remaining_quantity: "UNKNOWN"
```

---

# 7｜地道狀態

```yaml
ANOMALOUS_PASSAGE_STATE:
  passage_id: "PASSAGE_GUANZHI_BACKROOM_XUANHE"
  state_class: "ACTIVE_UNMAPPED"
  entrance: "觀止後堂地板下"
  observed_marker: "宣和"
  confirmed_user:
    - "趙受益／趙禎"

  far_endpoint: "UNKNOWN"
  stability: "UNKNOWN"
  ownership: "NONE_ESTABLISHED"
  guard_status: "NOT_RECORDED"
  seal_status: "NOT_RECORDED"

  knowledge_scope:
    confirmed_knowers:
      - "白御行"
      - "潘金蓮"
      - "紅娘氏"
      - "趙受益／趙禎"
    li_shishi_knows: "NOT_RECORDED"
    public_knows: false

  hard_rule:
    - "地道是進入觀止的路，不是取得任何姑娘的權利"
    - "不得自動讓皇帝、趙氏宗室或任何人由地道直入李師師私域"
```

---

# 8｜知情、公開消息與傳聞

```yaml
KNOWLEDGE_AND_RUMOR:
  MANAGEMENT_CONFIRMED:
    - "李清照已返回自身時代"
    - "李師師已選擇留在觀止"
    - "李師師將採設席牌"
    - "紅娘氏完成第一筆紅倌交易"
    - "後堂存在未測繪地道"

  PUBLIC_OR_HALL_RUMOR:
    LI_SHISHI_STAY:
      status: "RUMOR_SPREADING_BEFORE_FORMAL_BOARD"
      variants:
        - "只見詞壓群芳者"
        - "將從歷代名士中選入幕者"
        - "第一席已被白御行買下"
      verified:
        - "李師師確定留下"
      unverified_or_false:
        - "第一席已售"
        - "白御行已取得首席"
        - "趙受益可由地道直接見她"

  PRIVATE:
    - "白御行與張麗華穿衣陪睡及其私人談話"
    - "地道的具體入口"
    - "趙受益與紅娘氏的交易細節"
    - "趙受益留下宮牌／聯絡牌"

  RUMOR_MUST_NOT_SELF_CONFIRM:
    - "皇帝每晚固定由地道來見李師師"
    - "李師師與趙受益已有真實情愛關係"
    - "白御行已包下李師師第一席"
```

---

# 9｜立即到期事項與開放伏筆

```yaml
DUE_ITEMS:
  PRIORITY_1:
    item: "李師師設席牌完成與第一次開席公告"
    status: "IN_PREPARATION"

  PRIORITY_2:
    item: "後堂地道測繪、封鎖、守門與使用規矩"
    status: "UNRESOLVED"

  PRIORITY_3:
    item: "紅袖冰蠶弦逾期結果"
    status: "NOT_RECORDED"

  PRIORITY_4:
    item: "紅娘氏李師師席期消息訂金如何入帳"
    status: "PENDING_ACCOUNTING"

IMMEDIATE_OPEN_HOOKS:
  - hook_id: "HOOK_LISHISHI_FIRST_SEAT"
    question: "李師師第一席何時開、出什麼題、看誰第一眼？"

  - hook_id: "HOOK_RENZONG_LITERATI_FRENZY"
    question: "仁宗朝與跨朝代文士得知設席後，誰先投帖、誰先失態？"

  - hook_id: "HOOK_TUNNEL_ENDPOINT"
    question: "宣和地道下一次開啟會通往哪裡？"

  - hook_id: "HOOK_TUNNEL_AUTHORITY"
    question: "潘金蓮如何處理地道門票、封口與觀止安全？"

  - hook_id: "HOOK_HONGNIANG_NETWORK"
    question: "紅娘氏如何利用第一筆客人、宮牌與席期訂金建立大堂網絡？"

  - hook_id: "HOOK_ZHANG_FINAL_CHOICE"
    question: "張麗華在完成一夜陪伴後，是否以及何時回應正式關係定位？"

  - hook_id: "HOOK_SU_SETTLEMENT"
    question: "蘇清舊三晚交易與新寫作委託如何結帳？"

  - hook_id: "HOOK_HONGXIU_STRINGS_OVERDUE"
    question: "紅袖冰蠶弦是否已交付，若未交付，延誤原因是什麼？"
```

---

# 10｜本輪禁止推斷

1. 不得把白御行與張麗華的穿衣陪睡寫成性交、婚姻或關係定案。
2. 不得讓潘金蓮、紅娘氏、李師師或其他人物知道白御行向張麗華揭露的私人歷史。
3. 不得把李清照返回寫成永久不能再進觀止。
4. 不得把李師師留下寫成她已屬於白御行、趙受益、觀止或任何恩客。
5. 不得把「設席牌」寫成自動禁慾；也不得把設席價自動包含整夜、身體或承諾。
6. 不得把趙受益走過地道寫成他擁有永久通行權或李師師接見權。
7. 不得把紅娘氏完成一次交易寫成趙受益包養、專屬或長期關係成立。
8. 不得自行補寫地道另一端、建造者、朝代穩定性或李師師是否知情。
9. 不得把大堂五種傳聞中的任何一種直接升格為官方規則。
10. 不得替白御行決定離開後堂後的下一步。

---

# 11｜唯一接關點

```yaml
CONTINUATION_POINT:
  story_time: "理火三年槐月十一日清晨"
  player_position: "白御行已離開潘金蓮後堂；下一目的地未指定"
  world_state:
    - "李清照已返回自己的時代"
    - "李師師已留在觀止並進入人物池，設席牌尚在製作"
    - "紅娘氏完成第一筆紅倌交易，開始建立消息與抽成網"
    - "宣和地道存在，但另一端與權限未知"
    - "張麗華穿衣陪睡完成，兩人最終關係仍未決"

  next_action_owner: "PLAYER"
  world_may_advance_without_player:
    - "潘金蓮可完成設席公告與地道封口規則的準備"
    - "紅娘氏可在大堂收集投帖、傳聞與客人名單"
    - "李師師可自行決定第一席題目，但不得自動替玩家取得席位"
```

---

# 12｜待提交 EVENT PATCH 摘要

```yaml
EVENT_PATCH:
  patch_id: "PATCH_BAI_HUAI11_MORNING_E31_E36"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  base_hot: "V1.0 + V1.1_PRIVATE_ADDENDUM"
  target_hot: "V1.2"

  added_events:
    - "E31 張麗華穿衣陪睡完成"
    - "E32 李清照返回自身時代"
    - "E33 李師師留觀止並採設席牌"
    - "E34 宣和地道出現、趙受益抵達"
    - "E35 紅娘氏完成第一筆紅倌交易"
    - "E36 白御行離開後堂"

  relationship_deltas:
    - "白御行／張麗華：增加完成整夜陪伴，不改變未決關係"
    - "李清照：本次來訪結束，文學注意保留"
    - "李師師：去留由UNDECIDED改為STAY_CONFIRMED"
    - "白御行／紅娘氏：建立新識與共享好戲／消息關係"

  world_deltas:
    - "人物池新增李師師"
    - "觀止新增設席牌職業位置"
    - "後堂新增未測繪宣和地道"
    - "紅娘氏由人物池基線進入白御行線ACTIVE_IN_WORLD"
```
