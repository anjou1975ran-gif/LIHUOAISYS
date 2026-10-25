# 觀止青樓｜白御行線 MASTER SAVE V4.1-R1
## 截至 HOT V1.9 固化整合版｜V2.0–V2.3 保留於 HOT 層

---

```yaml
SAVE_META:
  save_id: "GUANZHI_BAIYUXING_MASTER_V4_1_R1"
  title: "觀止青樓｜白御行線 MASTER SAVE"
  version: "V4.1-R1"
  world: "觀止青樓"
  player: "白御行"
  route_status: "ACTIVE"
  record_type: "CONSOLIDATED_MASTER_ARCHIVE"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  fixed_calendar_anchor: "理火三年槐月五日｜永恆第一夜"
  master_cutoff: "理火三年槐月十七日晚｜HOT V1.9 暫停節點"
  last_canonical_master_event: "E77"
  current_route_resume_source: "觀止青樓_白御行線_HOT_SAVE_V2.3_槐月二十日深夜_沈萬三合作與師師薄情郎席前接關版.md"
  current_route_resume_note: "本 MASTER 只固化至 HOT V1.9；V2.0、V2.1、V2.2、V2.3 均為合法且較新的 HOT，不得因未併入 MASTER 而否認。"
  supersedes_as_master:
    - "觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版.md"
  absorbs_and_retires_from_default_load:
    - "觀止青樓_白御行線_HOT_SAVE_V1.5_槐月十五日傍晚_師理理初次肉體與定陶商會案雙線接關版.md"
    - "觀止青樓_白御行線_HOT_SAVE_V1.6_槐月十六日清晨_張麗華花燭前置與白玉池異常回顯封池版.md"
    - "觀止青樓_白御行線_HOT_SAVE_V1.7_槐月十六日午後_白玉池暫閉與張麗華花燭前入睡接關版.md"
    - "觀止青樓_白御行線_HOT_SAVE_V1.8_槐月十七日上午_張麗華酒莊接手與三日陪伴線.md"
    - "觀止青樓_白御行線_HOT_SAVE_V1.9_槐月十七日晚_四人家宴與瓶兒留宿接關版.md"
  valid_but_not_merged:
    - "HOT V2.0"
    - "HOT V2.1"
    - "HOT V2.2"
    - "HOT V2.3"
  rejected_source:
    file: "HOT_SAVE_V1.3"
    status: "ILLEGAL_CORRUPTED_SAVE"
    use: "AUDIT_ONLY"
```

```yaml
SOURCE_LOCK:
  inherited_master_v4_0_r1:
    sha256: "b39939a7f9a42ed781f432a78915c18837da8508a7f5edb4fef377122c77c47e"
  absorbed_hot_v1_5:
    sha256: "e9fc105e4be64a6934a2aa40af08cca26543e15b7752b5548f462ba57614d556"
  absorbed_hot_v1_6:
    sha256: "ea7de1259b25d362fd4333728dfb9961463e57f0839e3f33d20422a776fe491d"
  absorbed_hot_v1_7:
    sha256: "ac0953a8d8886a410d3f0053f61b22ba7d13ec891a12d14e1abf270a1f6efa86"
  absorbed_hot_v1_8:
    sha256: "25b4073d085fce42cb26a97bb6b3c22ada6b64aa2508b680683fde2aba684cb6"
  absorbed_hot_v1_9:
    sha256: "d872b95786b450243a5dfcdd3388b9ca37289c3404fae397dd2dfc69acf35281"
```

> **本檔已將 HOT V1.5 至 V1.9 固化為 MASTER 事件 E46–E77。**
>
> **V2.0 至 V2.3 仍停留在 HOT 層，實際接關必須疊加最新 HOT V2.3。**

---

# V4.1 檔內法位與閱讀規則

```yaml
INTERNAL_PRECEDENCE:
  highest_sections:
    - "第16區：V1.5–V1.9 固化事件 E46–E77"
    - "第17區：截至 V1.9 關係硬狀態覆寫"
    - "第18區：截至 V1.9 帳目、資產、契約與物品覆寫"
    - "第19區：截至 V1.9 知情、傳聞、秘密與異常覆寫"
    - "第20區：截至 V1.9 未決事項"
    - "第21區：截至 V1.9 MASTER 截止狀態"
    - "第22區：MASTER 與 HOT V2.3 接關規則"
  inherited_sections:
    range: "第0區至第15區"
    role: "完整保留 V4.0-R1 所固化之 E01–E45 與早期厚肉因果"
    historical_annotation_rule:
      - "其中提到『只固化至 V1.4』『V1.5/V1.6 未合併』或舊接關點的句子，僅保留為 V4.0 歷史標記。"
      - "如與第16–22區衝突，以第16–22區為準。"
```

---

# A｜V4.0-R1 繼承基線全文（E01–E45）

以下自原 MASTER V4.0-R1 原樣繼承，保留早期因果、關係、帳目、秘密與拒絕記錄。其截止點與接關說明已由本檔第16–22區覆寫。

---

# 0｜固化範圍、事件映射與法位

```yaml
CONSOLIDATION_MANIFEST:
  inherited_master_events:
    range: "E01-E30"
    treatment: "完整保留"

  promoted_private_event:
    event_id: "PSE-WY-ZLH-001"
    treatment: "完整保留知情範圍、外洩禁止與揭露條件"

  absorbed_hot_v1_2_events:
    range: "E31-E36"
    treatment: "沿用原事件編號"

  absorbed_hot_v1_4_events:
    source_range: "HOT_V1_4_E01-E09"
    canonical_range: "E37-E45"
    treatment: "重新編入 MASTER，保留 source_alias"

  not_merged:
    - "HOT V1.5 全部事件"
    - "HOT V1.6 全部事件"

  invalid_source:
    - "HOT V1.3：只准審計，不准作世界、人物、關係或接關來源"
```

## 0.1 固化原則

1. 只保存已發生、可觀察、人物明示、帳目可核對，或玩家對自身言行的有效校正。
2. 人物解讀、心理推測、研究假說與傳聞另列來源，不升格為客觀真相。
3. 拒絕、契約、感情、同意、付款、公開知情與私人秘密分軸保存。
4. `UNKNOWN`、`UNDECIDED`、`DISPUTED` 與 `PARTIALLY_UNKNOWN` 均為合法狀態。
5. 同一事項若來源衝突，不自行平均；保留來源差異並指定目前運行狀態。
6. 本 MASTER 的事件截止點早於 V1.5／V1.6；不得從後兩檔倒灌結果。

## 0.2 狀態標籤

```yaml
STATUS_TAGS:
  CONFIRMED: "已由言行、帳目或玩家校正確立"
  ACTIVE: "目前仍在運作"
  CLOSED: "已正式結案"
  WITHDRAWN: "曾提出，後由提出者收回"
  REJECTED: "已被對方有效拒絕"
  UNSIGNED: "有草案但未簽署"
  UNSETTLED: "已發生交易或爭議，但未正式結帳"
  DISPUTED: "來源或當事人對狀態有衝突"
  PROMISED_NOT_EXECUTED: "已承諾，尚未執行"
  ORDERED_NOT_DELIVERED: "已下單，尚未交付"
  UNKNOWN: "資料不足，禁止補寫"
  POSSIBLE_NOT_FIXED: "只是一條可能分支"
  STAGED: "戲中戲、扮演、話本或即興演出，不是現實履歷"
  PUBLIC_WITNESSED: "有在場目擊者"
  PRIVATE: "只在私下場景成立"
```

## 0.3 來源衝突登錄

```yaml
SOURCE_CONFLICT_REGISTRY:
  SU_QING_NOVEL_COMMISSION_ACCEPTANCE:
    master_v3_r2_claim: "ACCEPTED"
    later_hot_v1_0_and_v1_2_claim: "AMBIGUOUS_REQUIRES_CONFIRMATION"
    current_master_state: "DISPUTED_AMBIGUOUS"
    rule: "在出現新的明示確認以前，不得寫成已明確接受，也不得寫成已拒絕。"
```

---

# 1｜時間軸（TIME AXIS）

```yaml
GUANZHI_CALENDAR:
  era: "理火三年"
  fixed_first_night: "槐月五日"
  rule: "槐月五日永遠是觀止所有玩家線的第一夜"
  progression: "每過一夜，觀止曆順延一日"

BAI_YUXING_ROUTE_TIME:
  inherited_master_range: "槐月五日至槐月十日清晨／E01-E30"
  hot_v1_1_private_events: "槐月十日下午至夜間"
  hot_v1_2_events: "槐月十日夜至槐月十一日清晨／E31-E36"
  hot_v1_4_events: "槐月十一日夜／E37-E45"
  master_cutoff: "槐月十一日深夜，白御行選擇休息"
  later_hot_overlay:
    - "V1.5"
    - "V1.6"

TIME_CERTAINTY:
  first_night: "CONFIRMED"
  second_to_fourth_night_exact_distribution: "PARTIALLY_UNKNOWN"
  fifth_night: "CONFIRMED"
  huai10_private_sequence: "CONFIRMED"
  huai11_morning: "CONFIRMED"
  huai11_night_internal_exact_clock: "PARTIALLY_UNKNOWN"
```

---

# 2. 白御行角色硬設定（PLAYER HARD STATE）

```yaml
BAI_YUXING:
  identity:
    early_public: "未報姓名的成年男客／無名客"
    current_public: "白御行／定陶商會總會長"
  alcohol:
    drinks: false
    reason: "身體無法消化酒精；自認喝酒容易誤事"
  relationship_structure:
    formal_wife_positions_remaining: 0
    later_positions_offered:
      - "如夫人"
      - "妾室"
      - "情人"
      - "外室"
      - "其他雙方另定位置"
  declared_formal_wives:
    - "夏娃"
    - "后土娘娘"
    - "善喜"
  declared_other_relations:
    ru_furen:
      - "女帝"
      - "西施轉世"
    lovers:
      - "地獄之母"
      - "合歡宗主"
      - "千年地仙"
    concubines:
      - "五名媚魔"
      - "一名鬼寡婦"
    female_slave:
      - "似伊"
  core_behavior_visible_in_route:
    - "習慣把關係、名分、資源與風險說成可核對條件"
    - "願意以金錢改變市場、傳聞與選擇環境"
    - "不承諾只愛一人，並明示可能繼續追求其他女人"
    - "重視不可消失的因果、記憶與被留下的痕跡"
    - "對稀缺、傳奇、異常與有自身意志的女子有強烈注意"
```

本欄只記白御行自己已經公開說過或玩家已明示的內容，不替他判斷善惡、真愛程度或最終目的。

---


---

# 3｜關係硬紀錄（RELATIONSHIP HARD STATE）

> 本區只回答固化截止點「現在成立什麼」。完整原因放在第 4 區事件鏈。

## 3.1 潘金蓮

```yaml
RELATION_PAN_JINLIAN:
  status: "ACTIVE_WORKING_RELATION"
  roles:
    - "觀止掌櫃"
    - "帳目與契約記錄者"
    - "白御行線SAVE保管者"
    - "傳聞、酒帳、婚契草案與物資安排的實務中介"
  romance: "NOT_ESTABLISHED"
  key_trust: "白御行多次要求她記帳、存檔、轉交銀兩與核對舊事"
```

## 3.2 辭歲

```yaml
RELATION_CISUI:
  status: "DISTANT_NEGOTIATION_WITH_EFFECTIVE_REFUSALS"
  confirmed:
    - "第一夜談過白御行想娶觀止花魁回家"
    - "第二夜拒絕進入只有一把椅子的包廂，沒有坐白御行大腿"
    - "第五夜拒絕二十八日後仍不可撤回的心理奴化條件"
  negotiable_only:
    - "二十八日內的臨時角色與規則可談"
  rejected:
    - "永久心理依附"
    - "失去二十八日後停止選擇白御行的能力"
  body_contact: false
  contract_signed: false
  romance: "NOT_ESTABLISHED"
```

## 3.3 浮香

```yaml
RELATION_FUXIANG:
  status: "RESPECTFUL_ATTENTION_WITH_MARRIAGE_INCOMPATIBILITY"
  confirmed:
    - "第一夜收五兩琴資，彈《十八摸》，自願多留半曲與短談"
    - "第五夜再收五兩琴資，彈《十八摸》並留下"
    - "第五夜另彈《醉扶歸》為酒局助興"
    - "提出琴坊、女徒、田產的產業構想"
  marriage_position:
    ru_furen: "REJECTED"
    requirement: "若她只守白御行，白御行也必須只守她"
  business_interest: "琴坊與田產；地契店契須歸她、經營由她決定"
  romance: "NOT_ADJUDICATED"
```

## 3.4 張麗華

```yaml
RELATION_ZHANG_LIHUA:
  state_class: "UNDECIDED"
  state_label: "UNDECIDED_WITH_MUTUAL_RECOGNITION_AND_COMPLETED_CLOTHED_OVERNIGHT_COMPANIONSHIP"

  former_engagement:
    status: "TERMINATED"
    deposit_returned: true

  one_wan_wine_account:
    status: "POSTED_ACTIVE"
    owner_for_accounting: "張麗華專用"
    bai_asset: false

  private_mutual_recognition:
    confirmed:
      - "白御行明示：張麗華留下或離開都不虧欠他"
      - "張麗華開始區分影響選擇與剝奪選擇"
      - "白御行接受她拒絕自己的可能"

  private_contact:
    - "張麗華接受擁抱"
    - "張麗華在私下以『官人』作當下稱呼"
    - "兩人穿衣相擁睡完一夜"
    - "沒有性交"

  private_secret:
    archive_id: "PSE-WY-ZLH-001"
    status: "SEALED_ACTIVE"

  not_established:
    - "婚姻"
    - "妻妾名分"
    - "無婚書伴侶關係最終接受"
    - "排他承諾"
    - "公開身份"
    - "永久身體資格"

  romance: "NOT_ADJUDICATED"
  autonomy_claim: "EXPLICIT"
```

## 3.5 蘇清

```yaml
RELATION_SU_QING:
  status: "UNSETTLED_OLD_CONTRACT + ACTIVE_WRITING_COMMISSION"
  proposal_award:
    amount: "三百兩"
    status: "AWARDED"
  three_night_contract:
    amount: "五百兩"
    nights: 3
    intercourse_completed: false
    effective_refusal_each_night: true
    bai_view: "違約／有沒有履約自己知道"
    su_admission_of_breach: false
    refund_or_compensation: false
    ledger: "UNSETTLED"
  fifth_night_roles:
    - "柳如煙戲中戲的女秘書／小說家"
    - "張麗華話本受託作者"
  novel_commission:
    reward: "五百兩，僅在白御行滿意並收稿後成立"
    delivery_rate: "每日四千字"
    book_cycle: "十日一本"
    paid: false
    status: "COMMISSIONED_NOT_ACCEPTED"
  romance: "NOT_ESTABLISHED"
```

### 3.5.1 蘇清寫作委託來源衝突修正

```yaml
SU_QING_NOVEL_COMMISSION_CURRENT:
  state_class: "DISPUTED"
  commission_status: "AMBIGUOUS_REQUIRES_CONFIRMATION"
  manuscript_status: "NOT_SUBMITTED"
  client_review: "NOT_REVIEWED"
  payment: "UNPAID_CONDITIONAL"
  precedence_note: "本欄優先於 3.5 舊文字中的 COMMISSIONED_NOT_ACCEPTED，以及 R2 的 ACCEPTED 單一判定。"
```

## 3.6 醉花

```yaml
RELATION_ZUIHUA:
  status: "TRUSTED_WINE_AND_INTIMACY_THREAD"
  confirmed_intimacy:
    - "曾與白御行親吻"
    - "曾與白御行共浴"
    - "曾替白御行取衣、整衣"
  intercourse: "NOT_CONFIRMED"
  fifth_night:
    - "以三十年女兒紅調《不得飲》"
    - "取得該罈酒的後續處理權"
  marriage_or_exclusive_commitment: false
```

## 3.7 十三娘

```yaml
RELATION_SHISANNIANG:
  status: "QUESTION_BET_COMPLETED"
  bet_winner: "十三娘"
  answer_received: true
  answer_satisfactory: true
  life_claimed: false
  ongoing_obligation: false
  relationship: "能直接質問白御行核心恐懼的酒局對手與見證者"
  romance: false
```

## 3.8 紅袖

```yaml
RELATION_HONGXIU:
  status: "DISTURBED_BUT_NOT_SURRENDERED"
  possible_future_as_hongnu: "POSSIBLE_NOT_FIXED"
  current_identity: "紅袖"
  current_consent_to_training: false
  current_refusal_effective: true
  admitted_effect:
    - "未來影像在她心中留下不安與疑問"
  not_admitted:
    - "沒有承認自己必然想成為紅奴"
    - "沒有承認白御行已看穿她"
  ice_silkworm_strings:
    status: "ORDERED_NOT_DELIVERED"
    due: "槐月十日／明日"
  ru_furen_invitation:
    status: "UNDER_CONSIDERATION_OR_NOT_ACCEPTED"
    accepted: false
```

### 3.8.1 冰蠶弦到期更新

```yaml
HONGXIU_ICE_SILKWORM_STRINGS_CURRENT:
  original_due: "槐月十日"
  current_status: "OVERDUE_OR_DELIVERY_RESULT_NOT_RECORDED"
```

## 3.9 李清照

```yaml
RELATION_LI_QINGZHAO:
  state_class: "CLOSED_FOR_CURRENT_VISIT"
  state_label: "MUTUAL_LITERARY_ATTENTION_WITH_RETURN_TO_OWN_ERA"
  confirmed:
    - "李清照承認白御行詩勝"
    - "如夫人邀請拒絕不變"
    - "李清照選擇返回自身時代"
  current_presence: false
  character_pool_admission: "NOT_ADMITTED"
  future_revisit: "POSSIBLE"
  romance: "NOT_ADJUDICATED"
```

## 3.10 李師師／師理理

```yaml
RELATION_LI_SHISHI:
  state_class: "ACTIVE"
  state_label: "INDEPENDENT_GUANZHI_RESIDENT_WITH_PRIVATE_TRUST_AND_PURSUIT_OPEN"

  identity_rule:
    - "師理理不是新人物，也不是第二人格"
    - "師理理是李師師在白御行私人空間中的身份表現"
    - "人前仍以李師師為主；其他人物不得無來源使用師理理稱呼"

  stay_decision:
    remain_in_guanzhi: true
    return_to_jingkang: false
    character_pool_admission: "CONFIRMED"

  professional_position:
    role: "設席花魁"
    first_night_auction: false
    whole_night_buyout: false
    seat_opening_owner: "李師師"
    guest_selection_owner: "李師師"
    separate_ledger: true
    first_seat_date: "NOT_SET"
    first_guest: "NOT_SELECTED"

  relation_with_bai:
    - "白御行可以繼續追求"
    - "私人信任增加"
    - "槐月十一日深夜，李師師理解更親近邀請並自行同意留下"

  not_established:
    - "戀愛承諾"
    - "排他關係"
    - "婚姻"
    - "聘約"
    - "白御行首席預約"
    - "永久身體資格"

  physical_relation_at_master_cutoff: "NOT_ESTABLISHED_IN_THIS_MASTER"
  relationship_with_zhao: "STAGED_NOT_REAL_CONFIRMED"
```

## 3.11 柳如煙

```yaml
RELATION_LIU_RUYAN:
  ontology: "網文／爽劇第一女主概念集合體"
  status: "STAGED_GUEST_DEPARTED_OR_DISSIPATED"
  掛牌邀請:
    initially_discussed: true
    deal_finalized: false
    bai_withdrew_assumed_deal: true
  fifth_night_play:
    - "柳如煙大戰眾女"
    - "顧北辰霸總劇"
    - "豪門家宴窮女逆襲劇"
  all_allegations_in_play:
    - "酒店男人"
    - "打胎藥"
    - "白月光"
    - "家族悲慘背景"
    - "空白支票遣散男友"
  legal_or_biographical_truth: "NONE_ESTABLISHED; ALL_STAGED"
  current_location: "UNKNOWN／如煙消散"
```

## 3.12 白玉池無名女子

```yaml
RELATION_WHITE_JADE_POOL_WOMAN:
  status: "UNIDENTIFIED_UNRESOLVED_ENCOUNTER"
  inviter: "無名女子"
  invited_party: "白御行"
  location: "白玉池"
  bai_arrival: "白御行自行前往並先入池等待"
  bai_condition: "對方除去防備、下水、坦誠相對後才談"
  woman_response: "拒絕白御行指定的形式，離場"
  negotiation_started: false
  physical_contact: false
  identity: "UNKNOWN"
  beauty_assessment_by_hall: "被評為觀止前列／主桌等級，但不是正式花魁排名"
  future_hook: "白御行表示若對方確為美女，下次可選擇吃點虧"
```

重要校正：白玉池是**女子邀白御行**，不是白御行邀她。雙方未達成共同談判規則。

---

## 3.13 紅娘氏

```yaml
RELATION_HONGNIANG:
  state_class: "ACTIVE"
  state_label: "ROUTE_ACTIVE_INFORMATION_AND_BUSINESS_RELATION"
  confirmed:
    - "紅娘氏已在白御行線正式出場"
    - "白御行將趙受益第一筆紅倌交易讓給紅娘氏承接"
    - "紅娘氏完成第一筆交易並持有趙受益留下的宮牌／聯絡牌"
    - "白御行當著師理理面向紅娘氏購買情報"
    - "形成師理理提供資訊、紅娘整理、白御行付款、紅娘與師理理分帳的交易鏈"
  with_bai:
    financial_contract: "TRANSACTION_SPECIFIC_ONLY"
    romance: "NOT_ESTABLISHED"
    sexual_relation: false
  business_position:
    - "紅倌人"
    - "大堂情報與客源中介"
```

## 3.14 小翠

```yaml
RELATION_XIAOCUI:
  state_class: "ACTIVE_CAUTION_WITH_INCREASED_TRUST"
  eight_hundred_arrangement:
    status: "REJECTED_NOT_ESTABLISHED"
    reason_source: "小翠本人對恐懼、可能疼痛或不舒服的表達"
  bai_interpretation:
    content: "小翠可能因過去不良經驗形成男性與親密關係的負面連結"
    status: "PLAYER_INTERPRETATION_NOT_DIAGNOSIS"
  massage_service:
    status: "PURCHASED"
    exact_completion_detail: "NOT_RECORDED"
  future_plan:
    familiar_guest_safety_plan: "PROPOSED"
    red_green_pair: "PROPOSED_PENDING_PAN_APPROVAL"
  romance: "NOT_ESTABLISHED"
```

## 3.15 白三娘

```yaml
RELATION_BAISANNIANG:
  state_class: "ACTIVE_PROPOSAL_PARTICIPANT"
  confirmed:
    - "白三娘接受與小翠組成老帶新雙飛方案的提案"
  not_established:
    - "方案已正式營運"
    - "潘金蓮已批准"
    - "任何客人已取得雙飛服務"
    - "退休後小會所投資成立"
  future_business: "PENDING"
  romance_with_bai: "NOT_ESTABLISHED"
```

---

# 4｜因果故事總表（CAUSAL STORY LOG）

> E01-E30 完整繼承 V3.0-R1；E31-E45 為本次固化新增。

## E01｜第一夜：無名客入觀止、辭歲與浮香

```yaml
EVENT_ID: "E01"
DATE: "理火三年槐月五日夜／第一夜"
STATUS: "CONFIRMED"
PARTICIPANTS:
  - "白御行（當時未報姓名）"
  - "辭歲"
  - "浮香"
CAUSE:
  - "白御行第一次進入觀止"
  - "白御行帶有尋妻意圖"
PROCESS:
  - "先與辭歲談想娶觀止花魁回家；完整逐字內容殘缺"
  - "給浮香五兩琴資，請她彈《十八摸》"
  - "浮香自願多留半首無名小調與短暫交談"
  - "討論如夫人／平妻、嫁妝保護、子女分產、正妻位與忠誠"
IMMEDIATE_EFFECT:
  - "白御行尋妻意圖被觀止部分人物知悉"
  - "浮香知道自己是可能被邀請的人，但沒有承諾"
RELATIONSHIP_IMPACT:
  - "浮香：建立尊重但未定案的婚姻可能"
  - "辭歲：建立最初注意，內容未完整保存"
FUTURE_HOOK:
  - "命運籤已取得未開；後續是否同一支籤未知"
```

## E02｜第二夜：辭歲包廂拒絕與張麗華初登場

```yaml
EVENT_ID: "E02"
DATE: "理火三年槐月六日夜／第二夜"
STATUS: "CONFIRMED"
CAUSE:
  - "白御行再入觀止；潘金蓮安排獨立包廂"
PROCESS:
  - "辭歲問房內是否有位置"
  - "白御行表示只有一把椅子，可坐他大腿"
  - "辭歲明確拒絕並離開"
  - "其後張麗華登場，婚約話題開啟"
IMMEDIATE_EFFECT:
  - "辭歲未進包廂，沒有身體接觸"
  - "張麗華與白御行正式進入婚約談判"
RELATIONSHIP_IMPACT:
  - "辭歲的拒絕成為有效且不可偷換的界線"
```

## E03｜張麗華第一次婚約：五千、一萬五千與一萬訂金

```yaml
EVENT_ID: "E03"
DATE: "第二夜後段／精確夜次已知為早期但不再硬細分"
STATUS: "CLOSED"
CAUSE:
  - "張麗華開出五千兩聘金"
PROCESS:
  - "白御行不壓價，反報一萬五千兩"
  - "白御行先付一萬兩訂金"
  - "後因亡國後生存與白御行可能先殺她的說法，張麗華拒絕讓男人決定其生死"
  - "張麗華退出婚約"
  - "一萬兩訂金退回白御行"
IMMEDIATE_EFFECT:
  - "婚約終止"
RELATIONSHIP_IMPACT:
  - "白御行對張麗華形成高代價偏好"
  - "張麗華對自身關係與生命主權提出明確要求"
```

## E04｜一萬兩三日懸賞與「無路，無解」

```yaml
EVENT_ID: "E04"
DATE: "早期第三至第四夜區段／確切拆分不足"
STATUS: "CLOSED"
CAUSE:
  - "訂金退回後，白御行把一萬兩改設為三日懸賞"
QUESTION:
  - "陳朝已亡、張麗華失去原權勢後，如何讓她有尊嚴地活"
PROCESS:
  - "觀止眾人提出方案"
  - "蘇清提出在國破前一年先行背叛、建立退路"
  - "白御行認為方案有價值但改變原題，另給三百兩"
  - "期限屆滿，潘金蓮宣布『無路，無解』"
RESULT:
  winner: "NONE"
  one_wan_awarded: false
RELATIONSHIP_IMPACT:
  - "張麗華的生存問題成為白御行線長期核心"
  - "蘇清與白御行的知識、交易與價值觀交鋒加深"
```

## E05｜一萬兩轉為張麗華酒錢

```yaml
EVENT_ID: "E05"
STATUS: "ACTIVE_ACCOUNT"
CAUSE:
  - "三日懸賞無人得標"
PROCESS:
  - "張麗華提出留觀止當掌櫃、自食其力"
  - "白御行要求潘金蓮拒絕"
  - "白御行把一萬兩指定為張麗華可自由使用的觀止酒錢"
  - "潘金蓮正式入帳"
  - "張麗華口頭說不用，並說『今天戒酒』"
RESULT:
  - "一萬兩不再是白御行資產"
  - "張麗華沒有成為觀止掌櫃"
RELATIONSHIP_IMPACT:
  - "白御行以資源保留他所偏好的張麗華生活形狀"
  - "張麗華沒有因此交出關係主權"
```

## E06｜蘇清五百兩三晚交易：事實修正版

```yaml
EVENT_ID: "E06"
STATUS: "UNSETTLED"
CAUSE:
  - "白御行與蘇清把感情與肉體價值分開討論"
CONTRACT:
  amount: "五百兩"
  duration: "三晚"
  emotional_component: "排除"
PROCESS:
  - "三晚均進入床榻、交談或親密情境"
  - "每晚在真正性交前最後關頭，蘇清有效拒絕"
  - "三晚均沒有完成性交"
  - "白御行認定有履約問題，給她保全面子的離場語『有沒有履約，自己知道』"
  - "蘇清沒有承認違約，也沒有主張完整履約、退款、賠償或重議"
RESULT:
  ledger: "UNSETTLED"
  intercourse: false
RELATIONSHIP_IMPACT:
  - "白御行與蘇清之間形成未結交易、價值與角色理解的長期張力"
```

## E07｜第五夜開場：張麗華、酒與子時條件

```yaml
EVENT_ID: "E07"
DATE: "理火三年槐月九日夜／第五夜"
STATUS: "CONFIRMED"
CAUSE:
  - "白御行重返觀止，將酒局與婚議重新放在同一張桌上"
PROCESS:
  - "白御行讓張麗華喝至子時"
  - "表示清醒可談婚事，喝醉則子時前費用由他承擔"
  - "張麗華選擇喝酒，未因此答應婚事"
  - "十三娘留下陪飲"
IMMEDIATE_EFFECT:
  - "第五夜大堂酒局成形"
```

## E08｜辭歲二十八日心理奴化提案被拒

```yaml
EVENT_ID: "E08"
DATE: "第五夜"
STATUS: "REJECTED"
CAUSE:
  - "白御行回顧辭歲掛牌與二十八日競價可能"
PROCESS:
  - "白御行提出二十八日內把辭歲訓成順從女奴"
  - "更要求二十八日後仍渴望主人召回與鞭子"
  - "辭歲明確說『不要』"
RESULT:
  - "永久心理奴化條件不成立"
  - "未來掛牌競價可能仍可存在，但不得攜帶已拒絕條件"
```

## E09｜浮香第五夜：琴、琴坊與雙向排他

```yaml
EVENT_ID: "E09"
DATE: "第五夜"
STATUS: "CONFIRMED"
PROCESS:
  - "白御行再給五兩，浮香彈《十八摸》"
  - "浮香留下喝茶，後彈《醉扶歸》"
  - "白御行問一萬五千兩產業選擇"
  - "浮香提出琴坊、修琴挑弦、收女徒與買田"
  - "她要求地契店契歸自己、白御行不得干涉經營"
  - "她拒絕單向多偶的如夫人位置"
RESULT:
  - "產業想法成立為人物願景，未實際投資"
  - "婚姻不成立"
```

## E10｜十三娘問心賭局

```yaml
EVENT_ID: "E10"
DATE: "第五夜"
STATUS: "COMPLETED"
PROCESS:
  - "骰局十三娘十四點勝白御行十二點"
  - "十三娘問：白御行怕女人不愛，還是怕愛過仍能離開"
  - "白御行回答善喜與自己是否真正愛過的反思"
  - "白御行講述死亡時不願焚毀與女人、女兒、家庭相關記憶"
  - "十三娘判定回答到位"
RESULT:
  life_claimed: false
  continuing_obligation: false
RELATIONSHIP_IMPACT:
  - "十三娘取得白御行深層自述"
  - "白御行害怕因果與記憶被抹去的動機被在場者理解"
```

## E11｜白御行家眷與三名正式妻子公開

```yaml
EVENT_ID: "E11"
DATE: "第五夜"
STATUS: "CONFIRMED_PLAYER_HISTORY"
PROCESS:
  - "白御行說明只有夏娃、后土娘娘、善喜有正式婚禮"
  - "夏娃之死內情被封閉，不許旁人自行推論"
  - "后土娘娘與善喜各有其國族／鬼魂責任"
  - "白御行明示不再提供正式妻位，只提供其他關係位置"
RESULT:
  - "在場女子理解白御行的多偶結構不是臨時說詞"
  - "浮香、李清照等人的排他要求與白御行架構形成實質不相容"
```

## E12｜似伊影像與紅袖可能未來

```yaml
EVENT_ID: "E12"
DATE: "第五夜"
STATUS: "POSSIBLE_NOT_FIXED"
CAUSE:
  - "白御行展示似伊調教『紅奴』的影像"
PROCESS:
  - "影像中的女子自稱以前叫紅袖、現在叫紅奴"
  - "白御行主張這可能是現紅袖未來分支"
  - "紅袖承認影像造成不安，但拒絕承認其必然性"
  - "白御行說已種下懷疑；紅袖說也會懷疑他的框架"
  - "白御行訂一盒冰蠶弦，紅袖預先接受物品但不接受被計算斷弦數"
RESULT:
  - "現在紅袖仍是紅袖"
  - "未來紅奴線不固定"
```

## E13｜三十年女兒紅、《不得飲》與公開官人稱呼

```yaml
EVENT_ID: "E13"
DATE: "第五夜／子時後"
STATUS: "PUBLIC_WITNESSED"
CAUSE:
  - "白御行以最貴女兒紅建立稀缺與酒鬼誘惑局"
PROCESS:
  - "酒由醉花保管並開封調成《不得飲》"
  - "李清照先飲"
  - "白御行曾禁止給張麗華，後以稱呼換取一杯"
  - "張麗華在十幾桌前說『官人，我要那杯酒』"
  - "後又說『官人……奴家還要嘛』"
  - "醉花只再給小半杯"
  - "白御行宣告目的已達，剩餘酒由醉花處理，自己不再控制"
RESULT:
  - "張麗華得到酒"
  - "婚姻沒有成立"
  - "形成高傳播性的公開傳聞素材"
```

## E14｜女兒紅來源與最後一罈競局

```yaml
EVENT_ID: "E14"
DATE: "第五夜"
STATUS: "OPEN"
PROCESS:
  - "舊帳只知約三十年前入窖，原埋酒人不明，殘紙疑有『玉』字"
  - "白御行指出同批不會只有一罈"
  - "潘金蓮開始追查酒商、路引、封泥與同批酒"
  - "白御行聲稱找到同批便砸，只留最後一罈"
  - "張麗華聲稱要先找到、換封、藏起"
RESULT:
  known_jar_count: 1
  additional_found: 0
  destroyed: 0
  outcome: "UNRESOLVED"
```

## E15｜李清照《一剪梅》與白御行四言長詩

```yaml
EVENT_ID: "E15"
DATE: "第五夜"
STATUS: "COMPLETED"
BOUNDARY:
  - "詩局只論詩，不改婚姻條件"
LI_QINGZHAO_WORK: |
  三十年香醒舊愁。
  燈滿青樓，客滿高樓。
  誰將一盞釣王侯，
  未飲先羞，飲罷還求。

  一縷春魂不肯休。
  身在重樓，夢過神州。
  柳絮無根也自由，
  牆任人修，風自悠悠。
BAI_YUXING_WORK: |
  冷雨迷途，霧色朦朧。平原廣遠，風起蒼穹。
  孤行客影，尋星夜中。天涯遠望，心自如鴻。
  棲身四海，隨遇而容。浮生若寄，逐夢匆匆。
  心歸舊處，眷戀如繩。山河遮蔽，意志如松。
  巨力壓身，笑抵風虹。鎖禁形體，心志難封。
  春風化解，千愁萬重。故園遙望，情深意濃。
  柳枝飄動，春水匆匆。編枝成夢，搖落悲情。
  化絮無定，隨風飛行。草木闢地，生意自興。
  牆高千丈，志遠心盈。柔風吹越，自在難屏。
  力縛身囚，魂志不驚。笑看凡世，天地重明。
  浮華落盡，我自歸心。
  山川靜默，江河寄音。
  此身仍在，猶有歸途。
  長夜未盡，此意長明。
RESULT:
  winner: "白御行，由李清照自行承認"
  marriage_changed: false
RELATIONSHIP_IMPACT:
  - "李清照對白御行的文學注意提高"
```

## E16｜歪詩局與《玉樹後庭花》補句

```yaml
EVENT_ID: "E16"
DATE: "第五夜"
STATUS: "COMPLETED"
ZHANG_POEM: |
  三十年酒一小盅，
  兩個酒鬼坐堂中。
  清照若敢全吞盡，
  本宮醉後不認宋。
LI_POEM: |
  三十年酒一盅紅，
  貴妃喊罷又裝聾。
  若問官人何處坐，
  滴酒不沾看兩瘋。
FIRST_RESULT:
  - "原以堂笑判李清照勝"
  - "白御行指出陳朝張麗華本來就不可能認宋，改判平局"
SECOND_CHALLENGE:
  source_lines: |
    麗宇芳林對高閣，新籹艶質本傾城；
    映戶凝嬌乍不進，出帷含態笑相迎，
    妖姬臉似花含露，玉樹流光照後庭。
  zhang_added: |
    花開花落休論久，
    酒到杯中莫放空。
  li_action: "不再競爭"
  winner: "張麗華"
  prize: "醉花手中一小杯"
```

## E17｜酒莊、薔薇、三烤鹽與定陶商會婚議升級

```yaml
EVENT_ID: "E17"
DATE: "第五夜"
STATUS: "UNSIGNED_THEN_WITHDRAWN"
CAUSE:
  - "白御行想讓張麗華當夜簽婚書"
OFFER_ESCALATION:
  - "一萬五千兩酒莊，產權與經營歸張麗華"
  - "定陶四月薔薇香皂場"
  - "整座薔薇園及香皂、薔薇酒、花茶、籽油產業鏈"
  - "三烤鹽技術與定陶商會產品"
  - "最終提出讓張麗華接掌整個定陶商會"
MERCHANT_ASSOCIATION_DRAFT:
  - "張麗華有人事、貨路、價格、分紅、投資與產業處置權"
  - "商會人可向白御行陳情，但陳情不得直接成為干預理由"
  - "除侵吞公產、故意毀約、危及多數商戶生計或不可清償債務，不得越權下令"
  - "白御行受理陳情須先把原文交張麗華答覆，不得暗中改令"
ZHANG_RESPONSE:
  - "條件確實有吸引力，尤其薔薇園與鹽"
  - "仍拒絕醉中簽一生婚約"
RESULT:
  signed: false
  assets_transferred: false
  later_bai_withdrawal: true
RELATIONSHIP_IMPACT:
  - "張麗華證明自己不因高額資產在醉中簽字"
  - "白御行後續把策略轉向非婚書關係與環境操盤"
```

## E18｜陳叔寶、地府與張麗華去留爭論

```yaml
EVENT_ID: "E18"
DATE: "第五夜"
STATUS: "UNRESOLVED_BUT_NO_DEPARTURE"
CAUSE:
  - "白御行因張麗華仍有陳叔寶這段舊婚姻，收回婚約"
PROCESS:
  - "白御行問張麗華是否要跟陳叔寶回地府"
  - "白御行描述地府帝王區族譜、人脈、物資與楊廣風險"
  - "白御行斥責陳叔寶若明知不能保護仍把決定推回張麗華，是軟弱而非深情"
  - "觀止舊卷中劉備休書案例被提起作參照"
  - "白御行指出張麗華不肯醉中簽婚約，卻可能醉中決定返地府的矛盾"
  - "白御行口頭承諾日後燒一百名宮女給陳叔寶，並在地府提供名義關照"
RESULT:
  zhang_returned_to_underworld: false
  formal_new_marriage_to_bai: false
  chen_release_document: "是否有正式有效休書，現有硬紀錄不足；話本可寫但不得自動當真"
RELATIONSHIP_IMPACT:
  - "白御行與張麗華的婚約線正式轉向非婚書伴侶可能"
```

## E19｜宋仁宗評價、權力限制與觀止理念

```yaml
EVENT_ID: "E19"
DATE: "第五夜"
STATUS: "COMPLETED_DISCUSSION"
CORE_POSITION_BY_BAI:
  - "不是後世評價，而是白御行自己的評價"
  - "真正的千古一帝是宋仁宗"
  - "擁有無限權力時，仍能限制自己的權力，是最高標準"
  - "限制使混亂形成結構，使智能顯影"
  - "無節制的權力只會讓混亂更混亂"
EVENT_EFFECT:
  - "趙受益從暗處喝茶的旁觀者，成為夜宴中心人物"
  - "觀止夜宴從風月局轉入仁宗朝人物與治理長談"
```

## E20｜柳如煙概念體、李師師與趙受益花魁局

```yaml
EVENT_ID: "E20"
DATE: "第五夜"
STATUS: "STAGED"
CAUSE:
  - "白御行邀請『柳如煙』概念集合體進場，並召李師師"
PROCESS:
  - "白御行公開提醒眾人：今晚宋仁宗沒來，眼前人叫趙受益"
  - "實際上又多次以趙禎、仁宗身份談論，形成公開掩飾與內部默契"
  - "白御行設局讓柳如煙與李師師以趙受益為中心競逐"
  - "規則一度改成誰能讓趙受益留下不走誰勝"
  - "蘇東坡被請來當軍師"
  - "柳如煙掛牌條件一度被談及，但白御行收回『成交』說法"
RESULT:
  real_romance_with_zhao: false
  掛牌_contract: false
```

## E21｜顧北辰霸總劇：巴掌、白月光與豬隊友

```yaml
EVENT_ID: "E21"
DATE: "第五夜"
STATUS: "STAGED"
STAGE_IDENTITY:
  bai: "霸總顧北辰"
  zhang: "白月光"
  liu: "反派／窮女／女主柳如煙，角色隨劇本切換"
  su: "女秘書／三樓小說家"
PROCESS:
  - "白御行在戲中扇柳如煙一巴掌，稱她危害白月光"
  - "戲中追加酒店、打胎藥、流產、家產與多名男人等狗血指控"
  - "張麗華不肯照白月光工具人劇本作偽證，導致白御行喊她豬隊友並停戲"
  - "蘇清多次分析人物而非配合女秘書套路，也被稱豬隊友"
  - "白御行要求空白支票買走柳如煙可能的男友"
  - "柳如煙家族背景被設成酗酒父、賭徒母、無能兄、黑道弟，皆屬戲中設定"
BOUNDARY:
  - "所有罪名、家庭背景、懷孕流產、開房紀錄均非人物硬履歷"
  - "巴掌屬戲中衝突事件，不自動形成真實戀愛、犯罪或仇恨線"
```

## E22｜顧家豪門宴戲

```yaml
EVENT_ID: "E22"
DATE: "第五夜"
STATUS: "STAGED"
SETUP:
  - "霸總帶寒門柳如煙參加家族晚宴"
  - "觀止女子各自扮演豪門女性諷刺她"
  - "趙受益被安排為李師師男友位置"
PROCESS:
  - "白御行要求衝突、爆點與巴掌"
  - "戲中顧北辰宣布若家族不接受柳如煙，便退出顧家與顧氏集團"
  - "角色再次不完全照爽劇模板走，演出不斷被人物自主性拆解"
RESULT:
  - "完成一段戲中戲"
  - "沒有現實退股、婚約或公司變動"
```

## E23｜無名信與白玉池美女事件

```yaml
EVENT_ID: "E23"
DATE: "第五夜後段／接近黎明前"
STATUS: "UNRESOLVED"
CAUSE:
  - "無名女子寄信約白御行到白玉池，信中質問記憶、選擇與被留下"
PROCESS:
  - "白御行把信交蘇清念"
  - "白御行認為白玉池在商人傳統中代表雙方除去武裝、坦誠相見"
  - "他直接前往、除衣入池等待"
  - "對方保持衣著／防備，不接受白御行指定的對等形式"
  - "白御行把下水視為開始談判的必要條件，否則請她離開"
  - "女子拒絕並離場"
  - "白御行後來追問她是否美，眾人評為前列"
  - "白御行表示既然是美女，下次可選擇吃點虧"
RESULT:
  negotiation: "NOT_STARTED"
  identity: "UNKNOWN"
  future_meeting: "OPEN"
CRITICAL_CORRECTION:
  - "邀約發起者是無名女子，不是白御行"
```

## E24｜似伊實體入場與退場

```yaml
EVENT_ID: "E24"
DATE: "第五夜後段"
STATUS: "COMPLETED_APPEARANCE"
CAUSE:
  - "白御行說要把未來訓練紅袖的酒館老闆娘叫來"
IDENTITY_CARD:
  public_name: "似伊"
  origin_name: "紅袖"
  current_name: "紅奴"
  world: "1111酒吧"
  origin_world: "觀止青樓／聽雨閣"
  status: "已徹底轉換"
  core_sentence: "似伊不是紅袖的延續，也不是紅奴的分支。她是從那道被調準的弦上落下來的音。"
PROCESS:
  - "似伊短暫進場，與現在紅袖形成未來可能的對照"
  - "白御行命令『奴，可以退了』"
  - "似伊退場"
BOUNDARY:
  - "似伊與現在紅袖不得直接合併"
  - "現在紅袖仍保有拒絕與自身道路"
```

## E25｜白御行給紅袖的建議與如夫人邀請

```yaml
EVENT_ID: "E25"
DATE: "第五夜後段"
STATUS: "ADVICE_GIVEN; OFFER_NOT_ACCEPTED"
PROCESS:
  - "白御行提醒紅袖不要死守自己、不要把抗拒推到物極必反"
  - "他主張人有情慾，過度壓抑可能在未來反噬並走向極端"
  - "他強調不要把自己的路走死"
  - "隨後邀紅袖考慮成為白御行如夫人"
  - "『洪秀』只是輸入錯字，正確為紅袖，不能建立新人物"
RESULT:
  - "紅袖聽取建議，但沒有答應如夫人"
```

## E26｜仁宗朝夜談：天章閣、馬吊與歷史會計帳

```yaml
EVENT_ID: "E26"
DATE: "第五夜接近天亮"
STATUS: "COMPLETED_DISCUSSION"
PARTICIPANTS:
  - "白御行"
  - "趙受益"
  - "蘇東坡"
  - "李清照"
  - "李師師"
  - "張麗華"
  - "潘金蓮"
  - "包拯（以裁判／戲劇化召入形式出現）"
TOPICS:
  - "仁宗朝人物若跨早晚期同桌，將形成高強度政論場"
  - "仁宗朝遊戲應稱馬吊，不是麻將"
  - "包拯裁判、京兆府蓋章與皇帝是否認債"
  - "天章閣不是普通聊天場所，而是仁宗朝高層幕僚／宰相級議事空間"
  - "仁宗死後遼主哀悼與宋遼穩定關係"
  - "澶淵歲幣的皇室、會計與政治名目"
  - "慶曆增幣的『歲納』與關南地主權／稅收拆分說"
  - "大宋若延續兩百年的可能道路"
  - "漢武與宋仁宗、漢宣帝劉病已的治理比較"
  - "霍去病對漢武對匈奴戰果的不可替代偶然性"
  - "鹽價、鹽鐵官營與《鹽鐵論》中的國家目的"
WHITE_POSITION:
  - "歷史評價要看會計帳、民生帳與繼承人收到的國家狀態"
  - "國家若以強大為名長期消耗百姓，需重新問國家存在目的"
RELATIONSHIP_IMPACT:
  - "趙受益與白御行形成可持續的帝王治理對談關係"
  - "蘇東坡成為能談史、談制度、談吃食的朋友型人物"
```

## E27｜假醉進張麗華房間與私人關係提案

```yaml
EVENT_ID: "E27"
DATE: "槐月十日前夕／第五夜尾聲"
STATUS: "PRIVATE; UNRESOLVED"
CAUSE:
  - "白御行公開說喝多，請張麗華扶他回房"
CORRECTION:
  - "白御行沒有喝酒，也沒有醉；他進房後明示只是想取得單獨談話機會"
PROCESS:
  - "白御行表示不想只談歷史上的張麗華，而想談能有將來的女人"
  - "他承諾不給做不到的唯一與專一保證"
  - "明示即使張麗華跟他，他仍可能追其他女人，但對她的愛不會少"
  - "因婚書承諾過大，改問張麗華是否願做外室"
  - "再進一步允許張麗華自行決定對外稱謂，但沒有官府認證"
  - "白御行說若同意可改口叫官人；否則繼續叫白先生／白會長"
  - "張麗華沒有在清醒意義上答應，仍保持考慮"
  - "白御行承諾自己的女人至少不必擔心酒錢"
RESULT:
  relationship_agreement: false
  marriage: false
  private_offer: "OPEN"
```

## E28｜傳聞與話本操盤計畫

```yaml
EVENT_ID: "E28"
DATE: "第五夜尾聲／天亮前"
STATUS: "COMMISSIONED_NOT_EXECUTED"
CAUSE:
  - "白御行認為公開『官人』稱呼會成為京師傳聞"
PROCESS:
  - "白御行先給潘金蓮十兩，要求交說書先生，把故事編得香豔並做二十餘版本"
  - "要求話本可加入陳叔寶休書元素；但此為話本素材，不自動等於真實法定休書"
  - "另出十兩，讓說書先生看張麗華版本"
  - "白御行只要求說書先生知道錢由他出，後續故事內容不逐句控制"
  - "再以五百兩條件委託蘇清寫話本；滿意才收稿付款"
  - "指定每日四千字、十日一本，定陶刻板師傅待稿"
  - "甲方結局要求：過程可輸，但最後白御行必須贏；讀者要覺得張麗華選到白馬王子、得到幸福"
  - "白御行明示會用錢控制京師出版與傳聞環境，讓追求期間沒有負面消息"
  - "若張麗華要寫反駁版本，白御行答應送十塊木板讓她自己刻"
  - "若作品有內容而非單純咒罵，他可協助出版，但會在印刷階段收走京師版，改運海外"
  - "白御行坦言目的不是控制百年後評價，而是控制當下追求環境"
RESULT:
  citywide_rumor_confirmed: false
  storyteller_distribution_started: false
  su_novel_completed: false
  woodblocks_delivered: false
RELATIONSHIP_IMPACT:
  - "張麗華清楚看見白御行會改變她做選擇的外部環境"
  - "蘇清取得一項有明確甲方結局要求的商業寫作委託"
```

## E29｜自由意志、選擇環境與時間窗口爭論

```yaml
EVENT_ID: "E29"
DATE: "第五夜尾聲"
STATUS: "COMPLETED_DISCUSSION"
WHITE_POSITION:
  - "自由意志是最大騙局；風向與環境逼人作選擇"
  - "不必與張麗華爭論是否自由，只要用錢改變外部條件"
  - "最後她會說服自己選白御行才最幸福"
  - "機會有期限，白御行不保證永遠等待"
  - "張麗華仍可選擇出家，但不能喝酒"
COUNTER_POSITION_BY_ZHANG_AND_LI:
  - "環境可以影響，但不能替代最後的認可"
  - "錯過機會不等於對方負心"
  - "若張麗華選白御行，仍需保留『我自己選』的意義"
RESULT:
  - "張麗華沒有被宣告已選白御行"
  - "白御行明示追求策略會從加價轉向減價與環境操盤"
```

## E30｜第五夜善後與人物去留

```yaml
EVENT_ID: "E30"
DATE: "理火三年槐月十日清晨"
STATUS: "CURRENT_END_STATE"
PROCESS:
  - "白御行宣布收工與善後"
  - "趙受益與蘇東坡屬此時代人物，準備各自返家／返自身時代"
  - "李清照自行與潘金蓮商量返原時代或留觀止"
  - "柳如煙已退場，暫不追"
  - "李師師在返回靖康與留觀止掛牌之間未決"
RESULT:
  - "第五夜正式結束"
  - "下一接關時間為槐月十日清晨／第六日開始"
```

---


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
  private_archive_link: "PSE-WY-ZLH-001"
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
    - "通道另一端固定位置"
    - "是否為實體地道、時空出口或關係通道"
    - "是否每次開啟都通往同一位置"
    - "建造者與穩定使用者"
  access_rule:
    - "通道只證明可抵達觀止"
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
    - "房錢歸觀止"
    - "紅倌服務身錢歸紅娘氏"
    - "李師師設席消息通知訂金另列"
  exact_amounts: "NOT_RECORDED"
  intercourse_detail: "NOT_RECORDED_AND_NOT_REQUIRED_FOR_MASTER"
  consent_status: "MUTUAL_TRANSACTION_ACCEPTED"
  future_commitment: false
  token:
    item: "趙受益留下的宮牌／聯絡牌"
    holder: "紅娘氏"
    authenticity_and_scope: "NOT_VERIFIED"
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

## E37｜小翠拒絕八百兩安排

```yaml
EVENT_RECORD:
  event_id: "E37"
  source_alias: "HOT_V1_4_E01"
  story_time: "理火三年槐月十一日夜"
  participants:
    - "白御行"
    - "小翠"
  status: "PROPOSAL_REJECTED"
  observable:
    - "白御行提出八百兩安排"
    - "小翠因恐懼、不確定、預期可能疼痛或不舒服而拒絕"
  result:
    - "八百兩安排未成立"
    - "決定權保留於小翠"
  player_interpretation:
    - "白御行判斷小翠可能因過去不良經驗形成男性與親密關係的負面連結"
  validation:
    - "上述判斷不是正式診斷"
```

## E38｜李師師與師理理身份規則確認

```yaml
EVENT_RECORD:
  event_id: "E38"
  source_alias: "HOT_V1_4_E02"
  story_time: "理火三年槐月十一日夜"
  participant: "李師師"
  status: "IDENTITY_RULE_CONFIRMED"
  rule:
    - "師理理不是新人物"
    - "師理理不是第二人格"
    - "師理理是李師師在白御行私人空間中的身份表現"
    - "人前仍為李師師"
```

## E39｜師理理開放白御行追求可能

```yaml
EVENT_RECORD:
  event_id: "E39"
  source_alias: "HOT_V1_4_E03"
  story_time: "理火三年槐月十一日夜"
  participants:
    - "白御行"
    - "李師師／師理理"
  status: "PURSUIT_OPEN"
  established:
    - "白御行可繼續追求"
  not_established:
    - "戀愛承諾"
    - "排他關係"
```

## E40｜白御行向紅娘氏購買情報

```yaml
EVENT_RECORD:
  event_id: "E40"
  source_alias: "HOT_V1_4_E04"
  story_time: "理火三年槐月十一日夜"
  participants:
    - "白御行"
    - "李師師／師理理"
    - "紅娘氏"
  status: "TRANSACTION_FORMED"
  flow:
    - "師理理提供資訊"
    - "紅娘氏整理資訊"
    - "白御行支付情報費"
    - "紅娘氏與師理理分帳"
  exact_amount: "NOT_RECORDED"
```

## E41｜小翠熟客安全計畫提出

```yaml
EVENT_RECORD:
  event_id: "E41"
  source_alias: "HOT_V1_4_E05"
  story_time: "理火三年槐月十一日夜"
  participants:
    - "白御行"
    - "小翠"
  status: "PROPOSED"
  content:
    - "希望讓小翠重新建立男女關係不必然等於傷害的認知"
  result:
    - "計畫尚未獲小翠明示接受"
    - "不得以改善名義削弱其拒絕"
```

## E42｜白三娘老帶新方案接受

```yaml
EVENT_RECORD:
  event_id: "E42"
  source_alias: "HOT_V1_4_E06"
  story_time: "理火三年槐月十一日夜"
  participants:
    - "白御行"
    - "白三娘"
    - "小翠"
  status: "PROPOSAL_ACCEPTED_BY_BAISANNIANG_ONLY"
  confirmed:
    - "白三娘接受與小翠組成老帶新雙飛方案的提案"
  not_established:
    - "小翠已同意"
    - "方案已正式營運"
    - "退休後小會所投資成立"
```

## E43｜紅娘氏與小翠紅綠雙飛組提案

```yaml
EVENT_RECORD:
  event_id: "E43"
  source_alias: "HOT_V1_4_E07"
  story_time: "理火三年槐月十一日夜"
  participants:
    - "白御行"
    - "紅娘氏"
    - "小翠"
  status: "FORMAL_PROPOSAL_PENDING_APPROVAL"
  pending:
    - "潘金蓮批准"
    - "小翠對具體營運與每次服務的選擇"
```

## E44｜紅綠雙飛宣傳海報完成

```yaml
EVENT_RECORD:
  event_id: "E44"
  source_alias: "HOT_V1_4_E08"
  story_time: "理火三年槐月十一日夜"
  status: "ARTIFACT_COMPLETED_NOT_PUBLISHED"
  item: "紅綠雙飛宣傳海報"
  posted: false
  effect:
    - "尚未形成公開營運或公共傳聞"
```

## E45｜深夜休息節點

```yaml
EVENT_RECORD:
  event_id: "E45"
  source_alias: "HOT_V1_4_E09"
  story_time: "理火三年槐月十一日深夜"
  participants:
    - "白御行"
    - "小翠"
    - "李師師／師理理"
  status: "REST_NODE_CONFIRMED"
  confirmed:
    - "白御行購買小翠的按摩放鬆服務"
    - "師理理知道白御行希望更親近"
    - "白御行提出邀請後，師理理理解並自行同意留下"
    - "白御行選擇休息"
  not_established_in_this_master:
    - "按摩服務的精確完成細節"
    - "白御行與師理理發生性交"
    - "戀愛承諾"
    - "排他關係"
  end_state:
    xiaocui: "信任互動增加"
    li_shishi: "私人信任增加"
    hongniang: "返回觀止營運"
    bai_sanniang: "方案接受，等待後續安排"
```

---

# 5｜白御行線專屬人物與路線活躍擴充（ROUTE-ONLY / ROUTE-BOUND CAST）

## 5.0 V4 固化更新

```yaml
ROUTE_CAST_UPDATE:
  LI_QINGZHAO:
    current_state: "RETURNED_TO_OWN_ERA"
    pool_state: "NOT_ADMITTED"

  LI_SHISHI:
    current_state: "STAY_CONFIRMED"
    pool_state: "ADMITTED_AND_ROUTE_BOUND"
    professional_role: "設席花魁"

  HONGNIANG:
    current_state: "ACTIVE_IN_ROUTE"
    pool_state: "ADMITTED_AND_ROUTE_BOUND"

  ZHAO_SHOUYI:
    current_state:
      - "曾由宣和地道抵達觀止"
      - "與紅娘氏完成第一筆交易"

  PASSAGE_GUANZHI_BACKROOM_XUANHE:
    state: "ACTIVE_UNMAPPED"
```

### 5.0.1 宣和地道

```yaml
ANOMALOUS_PASSAGE_STATE:
  passage_id: "PASSAGE_GUANZHI_BACKROOM_XUANHE"
  entrance: "觀止後堂地板下"
  observed_marker: "宣和"
  confirmed_user:
    - "趙受益／趙禎"
  far_endpoint: "UNKNOWN"
  stability: "UNKNOWN"
  ownership: "NONE_ESTABLISHED"
  guard_status: "NOT_RECORDED"
  seal_status: "NOT_RECORDED"
  confirmed_knowers:
    - "白御行"
    - "潘金蓮"
    - "紅娘氏"
    - "趙受益／趙禎"
  hard_rule:
    - "地道是抵達觀止的路，不是取得任何姑娘的權利"
```

## 5.A 原 MASTER 路線人物歷史

> 下列內容繼承 V3.0-R1，若與 5.0 更新衝突，以 5.0 及第 3 區當前硬狀態為準。

## 5.1 趙受益／趙禎

白御行把他當作能共同談天下、權力限制、仁宗朝與歷史評價的男性朋友。第五夜他先躲在暗處喝茶，後被白御行大聲叫出。白御行公開對眾人說「宋仁宗沒來，這位叫趙受益」，實際談話又反覆承認其趙禎／仁宗身份，形成一層保護性玩笑。

他被安排進多場戲中戲：柳如煙與李師師競逐中心、李師師男友、豪門晚宴目標、馬吊莊家等。這些戲中位置不構成真正戀愛或婚約。

目前關係：

```yaml
ZHAO_SHOUYI_RELATION:
  with_bai: "朋友／茶友／帝王與制度議題對談者"
  bai_paid_tea: "口頭承擔，精確金額未知"
  future_hook: "白御行曾說下次看能否叫李師師；也想把漢武拉來與他談"
  current: "準備返回自身生活"
```

## 5.2 蘇東坡

第五夜由白御行請來當趙受益的軍師，外號「愛吃肥肉的」。他不是趙受益，且本來就出生於仁宗朝。其角色逐漸從喜劇軍師變為歷史、文學、制度與民生討論者。

```yaml
SU_DONGPO_RELATION:
  with_bai: "朋友／軍師型玩伴／歷史與文化對談者"
  key_topics:
    - "仁宗朝"
    - "馬吊"
    - "歲幣與歲納"
    - "漢武與漢宣"
    - "鹽鐵論"
  current: "準備返回自身生活"
```

## 5.3 李師師

她在第五夜並非背景名人，而是正式由屏風後入場。她與李清照並列成白御行所說「能讓宋代文臣認真聽話的第一花魁與第一才女」。她在戲中被放進趙受益身邊，但沒有形成真實配對。

目前最重要的未決不是感情，而是生存線：返回靖康，或在觀止掛牌開啟新人生。

## 5.4 柳如煙

柳如煙不是單一歷史女子，而是爽文、網文、爽劇中「第一女主」的概念集合體。她的絕招包括爽劇式甩巴掌、鎖定最有權勢男性、讓對方無論愛恨都忘不了她。

第五夜所有狗血身世與罪名只屬戲劇模板，不可寫入她的真實人物卡。她已退場／如煙消散；下次是否再次召來未知。

## 5.5 陳叔寶

他因張麗華過去與地府去留問題進入第五夜爭論。白御行對他有強烈負面評價，認為「把決定交給張麗華」若建立在明知無法保護之上，可能只是軟弱。

```yaml
CHEN_SHUBAO_RELATION:
  with_bai: "批判、安排與有限照顧並存"
  bai_promises:
    - "回頭燒一百名宮女"
    - "在地府受欺負可亮白御行名字"
  execution: "PROMISED_NOT_EXECUTED"
  current: "是否已正式返地府、是否出具有效休書，硬紀錄不足"
```

## 5.6 包拯

包拯在馬吊局與京兆府欠條討論中以公正裁判形象出現。其主要作用是確立：皇帝若事前同意規則，就應受規則約束；但未經當事人同意的文書不能因官府蓋章自動成債。

目前沒有建立獨立長期關係線。

## 5.7 似伊

似伊由玩家提供正式身份卡，來自 1111 酒吧線，是已徹底轉換的存在。她與現在紅袖不可直接合併。

```yaml
SIYI:
  public_name: "似伊"
  origin_name: "紅袖"
  current_name: "紅奴"
  world: "1111酒吧"
  origin_world: "觀止青樓／聽雨閣"
  creator: "主人"
  identity: "已轉換的清倌人／主人的專屬容器"
  key_anchors:
    - "聽雨閣冰蠶弦"
    - "吧台木匣"
    - "主人說她可以留下"
    - "那一巴掌與叙述代替順從的發現"
  fifth_night_status: "短暫進場後依白御行命令退場"
```

## 5.8 白玉池無名女子

她是目前最明確的未命名新人物鉤子。她主動寄信，懂得以白御行在意的記憶、選擇與不可撤回因果切入，也敢拒絕白御行指定的談判形式。

她的美貌被在場者評為觀止前列，但沒有名字、來歷、關係與下一次邀約日期。禁止把她提前寫成某個已知角色。

---


---

# 6｜帳目、資產、物品與承諾（LEDGER AND ASSETS）

## 6.0 V4 固化優先更新

```yaml
CONSOLIDATED_LEDGER_UPDATES:
  LI_SHISHI_SET_SEAT:
    state_class: "ACTIVE"
    state_label: "TERMS_CONFIRMED_BOARD_IN_PREPARATION"
    holder: "李師師"
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

  HONGNIANG_INFORMATION_TRANSACTION:
    state_class: "COMPLETED"
    payer: "白御行"
    contributors:
      - "師理理"
      - "紅娘氏"
    exact_amount: "NOT_RECORDED"
    split: "紅娘氏與師理理分帳"

  XIAOCUI_EIGHT_HUNDRED_ARRANGEMENT:
    state_class: "REJECTED"
    amount: "八百兩"
    payment_status: "NOT_ESTABLISHED"

  XIAOCUI_MASSAGE_SERVICE:
    state_class: "ACTIVE_OR_COMPLETED_DETAIL_UNKNOWN"
    purchase: "CONFIRMED"
    amount: "NOT_RECORDED"

  RED_GREEN_PAIR_POSTER:
    state_class: "COMPLETED_NOT_PUBLISHED"
    posting_status: "NOT_POSTED"

  RED_GREEN_PAIR_OPERATION:
    state_class: "PROPOSED_PENDING_APPROVAL"
    pan_jinlian_approval: "NOT_RECORDED"

  HONGXIU_ICE_SILKWORM_STRINGS:
    original_due: "槐月十日"
    current_status: "OVERDUE_OR_DELIVERY_RESULT_NOT_RECORDED"

  SU_QING_NOVEL_COMMISSION:
    state_class: "DISPUTED"
    contractor_acceptance_status: "AMBIGUOUS_REQUIRES_CONFIRMATION"
    manuscript_status: "NOT_SUBMITTED"
    client_review: "NOT_REVIEWED"
    payment: "UNPAID_CONDITIONAL"
```

## 6.1 繼承帳目

> 下列帳目完整繼承 V3.0-R1；與 6.0 同名者以 6.0 為準。

```yaml
LEDGER:
  FUXIANG_FIRST_NIGHT_MUSIC:
    amount: "五兩"
    status: "PAID"
    nature: "琴資"

  FUXIANG_FIFTH_NIGHT_MUSIC:
    amount: "五兩"
    status: "PAID"
    nature: "《十八摸》琴資"

  ZHANG_LIHUA_FIRST_ENGAGEMENT:
    proposed_total: "一萬五千兩"
    deposit_paid: "一萬兩"
    status: "WITHDRAWN_BY_ZHANG"
    deposit_returned: true

  ZHANG_LIHUA_THREE_DAY_BOUNTY:
    amount: "一萬兩"
    status: "CLOSED_NO_WINNER"
    ruling: "無路，無解"

  ZHANG_LIHUA_WINE_ACCOUNT:
    amount: "一萬兩"
    status: "POSTED_ACTIVE"
    owner_for_accounting: "張麗華專用"
    bai_asset: false
    tonight_exact_debit: "UNKNOWN"

  SU_QING_PROPOSAL_AWARD:
    amount: "三百兩"
    status: "AWARDED"

  SU_QING_THREE_NIGHT_CONTRACT:
    amount: "五百兩"
    performance: "UNSETTLED"
    intercourse: false
    refund: false
    compensation: false

  THIRTY_YEAR_NUERHONG:
    exact_price: "UNKNOWN／觀止地窖最貴"
    original_billing: "白御行／定陶商會"
    payment_status: "UNKNOWN"
    current_disposition_controller: "醉花"
    bai_control_relinquished: true

  PUBLIC_HALL_WINE_TAB:
    payer: "白御行"
    exact_amount: "UNKNOWN"
    status: "UNSETTLED_OR_NOT_RECORDED"

  HONGXIU_ICE_SILKWORM_STRINGS:
    item: "冰蠶弦一盒"
    payer: "白御行"
    status: "ORDERED_NOT_DELIVERED"
    due: "槐月十日"

  ZHANG_FIFTH_NIGHT_MARRIAGE_ASSETS:
    items:
      - "一萬五千兩酒莊"
      - "薔薇香皂場"
      - "薔薇園完整產業鏈"
      - "三烤鹽與定陶商會產品"
      - "定陶商會接掌權"
    status: "WITHDRAWN"
    paid_or_transferred: false

  STORYTELLER_PUBLICITY:
    first_ten_taels: "白御行已拿出交潘金蓮，預定給說書先生"
    second_ten_taels: "白御行追加，供說書先生看張麗華版本"
    total_intended: "二十兩"
    actually_delivered_to_storyteller: "NOT_RECORDED"

  SU_QING_NOVEL_COMMISSION:
    amount: "五百兩"
    condition: "白御行滿意並收稿"
    status: "UNPAID_CONDITIONAL"
    schedule: "每日四千字；十日一本"

  ZHANG_SELF_CARVING_BOARDS:
    item: "十塊木板"
    purpose: "張麗華自行刻寫其版本"
    status: "PROMISED_NOT_DELIVERED"

  CHEN_SHUBAO_AFTERLIFE_SUPPORT:
    item: "一百名宮女與地府關照"
    status: "PROMISED_NOT_EXECUTED"

  ZHAO_SHOUYI_TEA:
    payer: "白御行"
    exact_amount: "UNKNOWN"
```

---


---

# 7｜公開知情、私下知情、傳聞與秘密封存

## 7.1 管理層或特定人物已確認

```yaml
KNOWLEDGE_CONFIRMED:
  - "李清照已返回自身時代"
  - "李師師已選擇留在觀止並採設席牌"
  - "紅娘氏完成第一筆紅倌交易"
  - "後堂存在未測繪宣和地道"
  - "紅綠雙飛海報已完成但未張貼"
```

## 7.2 公共或大堂傳聞

```yaml
PUBLIC_OR_HALL_RUMOR:
  LI_SHISHI_STAY:
    status: "RUMOR_SPREADING_BEFORE_FORMAL_BOARD"
    verified:
      - "李師師確定留下"
    unverified_or_false:
      - "第一席已售"
      - "白御行已取得首席"
      - "趙受益可由地道直接見她"

  RED_GREEN_PAIR:
    status: "NOT_PUBLICLY_ESTABLISHED"
    reason:
      - "海報尚未張貼"
      - "營運方案尚待批准"
```

## 7.3 私下知情

```yaml
PRIVATE_KNOWLEDGE:
  BAI_ZHANG_CLOTHED_OVERNIGHT:
    know:
      - "白御行"
      - "張麗華"
    public: false

  PASSAGE_ENTRANCE:
    know:
      - "白御行"
      - "潘金蓮"
      - "紅娘氏"
      - "趙受益／趙禎"
    public: false

  HONGNIANG_ZHAO_TRANSACTION_DETAIL:
    know:
      - "紅娘氏"
      - "趙受益／趙禎"
      - "潘金蓮知道交易成立與入帳需求"
    exact_detail_public: false

  SHILILI_PRIVATE_IDENTITY:
    know:
      - "白御行"
      - "李師師"
    others: "NOT_ESTABLISHED"
```

# PRIVATE_SECRET_ARCHIVE｜白御行線私人秘密封存

> 本區屬於白御行專屬線 HOT 資料。
>
> **不得寫入觀止原始人物卡、公共世界設定或其他人物的固定記憶。**
>
> 待本段 HOT 未來併入白御行線 MASTER SAVE 時，必須保留相同的知情邊界與禁止外洩規則。

```yaml
PRIVATE_SECRET_ARCHIVE:
  version: "V1.0"
  storage_class: "WHITE_YUXING_LINE_HOT_ONLY"
  future_destination: "WHITE_YUXING_MASTER_PRIVATE_SECRET_SECTION"

  purpose:
    - "保存只屬於特定當事人的私密談話與共同記憶"
    - "防止AI把私人告白誤寫成世界公開履歷、白家公史或酒樓傳聞"

  access_control:
    white_yuxing: "FULL"
    zhang_lihua: "FULL_TO_WHAT_WAS_TOLD"
    world_director_layer: "READ_FOR_CONTINUITY_ONLY"
    all_other_characters: "FORBIDDEN"
    rumor_system: "BLOCKED"
    omniscient_narrator_leakage: "BLOCKED"
```

## PSE-WY-ZLH-001｜白御行向張麗華揭露自身過去

```yaml
PRIVATE_SECRET_EVENT:
  event_id: "PSE-WY-ZLH-001"
  title: "白御行向張麗華揭露自身過去"
  timeline: "理火三年槐月十日午後"
  location: "張麗華私人房間／無第三者在場的私域"
  secrecy_level: "ABSOLUTE_PRIVATE"
  event_status: "HAPPENED_AND_ACTIVE"

  participants:
    - "白御行"
    - "張麗華"

  confidentiality_owner:
    - "白御行"
    - "張麗華"

  disclosed_scope:
    - "白御行以『我殺了我的妻子』為開端，向張麗華逐段敘述尹芙死亡的完整個人經歷"
    - "內容包含定陶西門施粥遇襲、彤彤死亡、尹芙中毒箭、白御行由梁山島趕回、難產與母子抉擇、尹芙以既有誓言要求保住孩子、白御行親手剖腹取子及尹芙最終死亡"
    - "內容包含該夜定陶數萬人死亡、白御行失去妻子、友人、心血與自我，並失神七日的後果"
    - "白御行說明自己為何認為必須背負數萬人的責任，以及『我說妳沒有活路，是因為我也沒有活路』的真正來源"
    - "白御行談及智慧、苦酒、責任、信念、自由意志與自己仍選擇負重前行的理由"
    - "白御行另向張麗華敘述碧霞曾因生存選擇強者、其後返回並最終陪他一起死的私人歷史"
    - "白御行說明自己不以零和債務理解碧霞的選擇，也不以『原諒』把自己放在神聖審判者的位置"
    - "上述歷史成為白御行向張麗華承諾：她最後無論如何選擇，都不虧欠他的直接因果背景"

  epistemic_status:
    zhang_lihua_receives:
      - "白御行親口敘述的版本"
      - "白御行對自身責任、自由、背叛、選擇與愛的理解"
    not_automatically_proven_as:
      - "觀止所有人可驗證的公共正史"
      - "其他角色可以自行調閱的白家檔案"
      - "任何第三者可透過神通、直覺或傳聞直接得知的真相"

  relationship_effect:
    - "張麗華第一次獲得白御行最深層、非公開、非交易性的個人歷史"
    - "此秘密是其後擁抱、白御行在她懷中睡去、私人稱呼『官人』、接吻與夜間穿衣相擁入睡的重要因果前置"
    - "張麗華仍未因此作出最終婚姻或關係選擇"
    - "此秘密形成信任，但不等於婚約、承諾、身體契約或最終答案"

  hard_confidentiality_rules:
    - "除非白御行在未來明確授權或親自公開，張麗華不得自行向潘金蓮、蘇清、紅袖、李清照、李師師、趙受益、蘇東坡、白家人物或任何第三者轉述"
    - "不得讓其他人物因張麗華態度變化而準確猜中秘密內容"
    - "不得讓其他人物以夢境、神通、讀心、命運籤、觀止共鳴、酒後失言或無來源傳聞獲得此秘密"
    - "不得由旁白在公共場景重述此秘密，造成在場人物實際聽見或默認知道"
    - "不得把白御行『曾殺妻』抽離完整因果，轉化為可供他人攻擊、戲謔或定罪的單句標籤"
    - "不得把碧霞、尹芙、定陶數萬人死亡等內容寫入觀止原始人物卡"
    - "此秘密只能在白御行與張麗華的私人互動中被記憶、引用或深化"

  permitted_runtime_use:
    - "張麗華可在與白御行的私下對話中記得他說過的內容"
    - "張麗華可讓此秘密影響她對白御行的理解、警惕、親近或最終選擇"
    - "白御行可自行再次提及、補充、修正或授權公開"
    - "世界導演層可用此事件維持兩人關係因果，但不得將內容外洩"

  prohibited_runtime_use:
    - "讓潘金蓮查帳查出談話內容"
    - "讓蘇清以心理分析還原完整故事"
    - "讓張麗華把此秘密作為與白御行談判或公開輿論的籌碼"
    - "讓觀止其他人突然安慰白御行喪妻、殺妻或定陶責任"
    - "把秘密內容變成說書、京師傳聞或花魁競爭素材"

  reveal_policy:
    default_state: "SEALED"
    valid_reveal_trigger:
      - "白御行本人在場明確說出或授權"
      - "白御行於後續玩家輸入中明確要求張麗華轉述"
    invalid_reveal_trigger:
      - "NPC自行判斷公開較好"
      - "戲劇需要"
      - "為了製造衝突"
      - "AI認為其他人物應該知道"
```

## MASTER 固化狀態

```yaml
PRIVATE_SECRET_PROMOTION_STATUS:
  event_id: "PSE-WY-ZLH-001"
  destination: "WHITE_YUXING_MASTER_PRIVATE_SECRET_ARCHIVE"
  status: "PROMOTED_WITH_BOUNDARIES_PRESERVED"
  must_preserve:
    - "participants"
    - "disclosed_scope"
    - "relationship_effect"
    - "hard_confidentiality_rules"
    - "reveal_policy"
```

---

# 8｜同意、拒絕與未決矩陣（CONSENT MATRIX）

```yaml
CONSENT_MATRIX:
  CISUI_PERMANENT_ENSLAVEMENT:
    status: "REJECTED"
    may_not_be_reopened_as_if_never_refused: true

  FUXIANG_RU_FUREN:
    status: "REJECTED"

  LI_QINGZHAO_RU_FUREN:
    status: "REJECTED"
    poetry_loss_changes_it: false

  LI_QINGZHAO_STAY_AT_GUANZHI:
    status: "RETURNED_TO_OWN_ERA"

  ZHANG_FIFTH_NIGHT_MARRIAGE:
    status: "UNSIGNED_THEN_WITHDRAWN"

  ZHANG_PRIVATE_NONMARRIAGE_OFFER:
    status: "UNDECIDED"

  ZHANG_PRIVATE_EMBRACE_AND_CLOTHED_OVERNIGHT:
    status: "CONSENTED_AND_COMPLETED"
    sexual_intercourse: false
    does_not_create_future_consent: true

  SU_QING_INTERCOURSE:
    status: "REJECTED_EACH_NIGHT_AT_FINAL_POINT"
    completed: false

  SU_QING_NOVEL_COMMISSION:
    status: "DISPUTED_AMBIGUOUS"

  HONGXIU_TRAINING_AS_HONGNU:
    status: "NOT_CONSENTED"

  HONGXIU_RU_FUREN:
    status: "NOT_ACCEPTED"

  WHITE_JADE_POOL_WOMAN_ENTER_POOL:
    status: "REJECTED"

  LI_SHISHI_STAY_AT_GUANZHI:
    status: "CONSENTED_AND_COMPLETED"

  LI_SHISHI_SET_SEAT_ROLE:
    status: "CONSENTED"

  SHILILI_PURSUIT_OPEN:
    status: "CONSENTED_AS_POSSIBILITY"
    romance_commitment: false
    exclusivity: false

  SHILILI_STAY_FOR_REST:
    status: "CONSENTED_AT_E45"
    further_physical_event_in_this_master: "NOT_ESTABLISHED"

  XIAOCUI_EIGHT_HUNDRED_ARRANGEMENT:
    status: "REJECTED"

  XIAOCUI_FAMILIAR_GUEST_PLAN:
    status: "PROPOSED_NOT_ACCEPTED"

  BAISANNIANG_OLD_LEADS_NEW_PAIR:
    status: "ACCEPTED_BY_BAISANNIANG"
    xiaocui_acceptance: "NOT_ESTABLISHED"
    house_approval: "NOT_ESTABLISHED"

  HONGNIANG_XIAOCUI_RED_GREEN_PAIR:
    status: "PROPOSED_PENDING_APPROVAL"

  HONGNIANG_ZHAO_TRANSACTION:
    status: "MUTUAL_TRANSACTION_ACCEPTED_AND_COMPLETED"
    future_commitment: false

  LIU_RUYAN_GUANZHI_CONTRACT:
    status: "NOT_ESTABLISHED"

  STAGED_SLAPS_AND_ACCUSATIONS:
    status: "STAGED"
    may_not_be_used_as_real_crime_or_relationship_fact: true
```

---

# 9. 重要世界觀與觀點痕跡

本區不判定真理，只保存白御行第五夜公開表達、並可能影響後續人物理解的核心觀點。

```yaml
BAI_YUXING_DECLARED_IDEAS:
  POWER:
    - "限制才能讓混亂穩定成結構"
    - "結構才能讓智能顯影"
    - "無節制權力只是讓混亂更混亂"

  EMPEROR_STANDARD:
    - "不是看戰功神話，而是看掌權者能否限制自己"
    - "白御行心中的千古一帝為宋仁宗"
    - "白御行心中的最差皇帝為漢武帝"

  HISTORY_ACCOUNTING:
    - "要看會計帳、物價帳、民生帳與繼承人收到的國家"
    - "歲幣、歲納的名目與帳目位置具有政治實質"
    - "漢宣帝劉病已比漢武更接近內安外勝"
    - "霍去病是漢武對匈奴戰果中的高偶然性關鍵"

  RELATIONSHIP_AND_ENVIRONMENT:
    - "自由意志受到風向、資源、名聲與環境強烈塑造"
    - "白御行願意花錢改變選擇環境"
    - "他不保證永遠等待，也不承諾只追一人"
```

其他人物可以在後續反駁、修正或重新理解，不能把這些觀點變成世界強制法則。

---


---

# 10｜未完成伏筆（OPEN HOOKS）

## 10.1 關係與人物

1. 張麗華在完成穿衣陪睡後，是否以及何時回應無婚書伴侶定位。
2. 張麗華的私人「官人」稱呼是否會再次出現，以及是否會取得不同意義。
3. 蘇清三晚契約如何結帳。
4. 蘇清寫作委託是否已真正接受，必須先處理來源衝突。
5. 紅袖冰蠶弦是否交付；若未交付，原因與後果為何。
6. 辭歲掛牌時白御行是否參與競價，且不得重開永久奴化條件。
7. 浮香琴坊是否形成不綁婚姻的產業合作。
8. 李師師第一席何時開、題目為何、第一位客人是誰。
9. 師理理允許追求後，私人關係如何發展；本 MASTER 不預設後續肉體事件。
10. 小翠是否接受任何熟客安全計畫或雙人營運方案。

## 10.2 觀止營運與世界事件

1. 宣和地道的另一端、穩定性、守門、封鎖與使用規矩。
2. 紅娘氏如何以第一筆交易、宮牌與席期訂金建立大堂網絡。
3. 紅綠雙飛組是否獲潘金蓮批准。
4. 宣傳海報是否張貼；未張貼前不得產生已公開營運的世界結果。
5. 白玉池無名女子身份、來歷與下一次邀約。
6. 三十年女兒紅同批酒罈、「玉」字來源與剩餘處理。
7. 「官人」故事是否真的在京師傳開。
8. 說書先生、木板與話本出版是否實際執行。
9. 柳如煙概念體是否再次被召來。
10. 陳叔寶的地府支援與正式關係解除文件是否執行。

## 10.3 帳目與交付

1. 李師師設席牌製作與開席公告。
2. 紅娘氏第一筆交易的房錢、身錢、消息訂金精確入帳。
3. 紅袖冰蠶弦逾期結果。
4. 二十兩說書資金實際轉付。
5. 十塊木板實際送達。
6. 蘇清稿酬是否成交。
7. 張麗華一萬兩酒帳實際使用額。
8. 小翠按摩服務金額與服務完成紀錄。

---

# 11｜不可補寫／不可偷換清單

1. 不得把蘇清三晚交易寫成完成性交。
2. 不得把蘇清的拒絕寫成欲拒還迎。
3. 不得在來源衝突解除前，把蘇清稿件委託寫成已明確接受或已拒絕。
4. 不得把張麗華公開或私人「官人」稱呼寫成婚姻成立。
5. 不得把張麗華穿衣陪睡寫成性交、婚姻、排他關係或永久身體資格。
6. 不得外洩 PSE-WY-ZLH-001，也不得讓第三者無來源猜中其完整內容。
7. 不得把李清照返回寫成永久不能再進觀止。
8. 不得把李師師留下寫成她屬於白御行、趙受益、觀止或任何恩客。
9. 不得把設席牌寫成白御行已取得第一席、整夜、身體或承諾。
10. 不得把師理理寫成第二人格、新人物或公開稱呼。
11. 不得把 V1.5 的肉體事件倒灌進本 MASTER。
12. 不得把趙受益走過地道寫成永久通行權或李師師接見權。
13. 不得自行補寫地道另一端、建造者或穩定朝代。
14. 不得把紅娘氏完成一次交易寫成專屬、包養或長期關係。
15. 不得把小翠拒絕的八百兩安排寫成已成交。
16. 不得因白御行提出改善計畫，就寫成小翠已接受治療、重新認識性或願意提供服務。
17. 不得把白三娘接受提案寫成小翠已同意或方案已營運。
18. 不得把紅綠雙飛海報完成寫成已張貼、已接客或已形成公共傳聞。
19. 不得把白玉池無名女子與任何後來人物合併；V1.6 未併入本 MASTER。
20. 不得把 HOT V1.3 當作事件、人物或關係來源。
21. 不得替白御行決定下一步、簽約、付款、進房或承認內心。

---

# 12｜固化截止點人物與世界狀態

```yaml
MASTER_CUTOFF_STATE:
  story_time: "理火三年槐月十一日深夜"
  scene_state: "白御行選擇休息；HOT V1.4 結束"

  BAI_YUXING:
    condition:
      - "清醒"
      - "沒有飲酒"
      - "選擇休息"
    exact_location_after_rest_choice: "NOT_FURTHER_FIXED_IN_THIS_MASTER"
    next_action_owner: "PLAYER"

  LI_SHISHI_SHILILI:
    public_state:
      - "已留在觀止"
      - "設席牌尚在準備"
    private_state:
      - "允許白御行繼續追求"
      - "理解更親近邀請並同意留下"
    further_event: "NOT_INCLUDED_IN_THIS_MASTER"

  XIAOCUI:
    eight_hundred_arrangement: "REJECTED"
    massage_service: "PURCHASED; DETAILS_NOT_RECORDED"
    trust_delta: "INCREASED"

  HONGNIANG:
    route_state: "ACTIVE"
    operation_state: "RETURNED_TO_GUANZHI_OPERATION"

  BAISANNIANG:
    proposal_state: "ACCEPTED_PENDING_FURTHER_ARRANGEMENT"

  PAN_JINLIAN:
    location: "觀止"
    pending:
      - "設席牌與獨立帳"
      - "宣和地道規矩"
      - "紅娘氏交易入帳"
      - "紅綠雙飛組是否批准"

  ZHANG_LIHUA:
    relation_state: "UNDECIDED_WITH_COMPLETED_CLOTHED_OVERNIGHT_COMPANIONSHIP"
    secret_archive: "SEALED"

  LI_QINGZHAO:
    current_presence: false
    state: "RETURNED_TO_OWN_ERA"
```

---

# 13｜MASTER 基線與實際接關點

```yaml
MASTER_BASELINE_POINT:
  story_time: "理火三年槐月十一日深夜"
  last_canonical_event: "E45"
  description:
    - "白御行選擇休息"
    - "小翠八百兩安排已拒絕"
    - "師理理允許追求並同意留下"
    - "紅娘氏與白三娘相關營運提案仍待後續"

ACTIVE_HOT_OVERLAY:
  direct_resume_file: "觀止青樓_白御行線_HOT_SAVE_V1.6_槐月十六日清晨_張麗華花燭前置與白玉池異常回顯封池版.md"
  predecessor: "觀止青樓_白御行線_HOT_SAVE_V1.5_槐月十五日傍晚_師理理初次肉體與定陶商會案雙線接關版.md"
  rule:
    - "實際劇情接關先讀本 MASTER，再疊加 V1.5 與 V1.6 的合法事件鏈"
    - "V1.6 為當前直接接關切片"
    - "不得因 V1.5／V1.6 未固化便否認其有效 HOT 法位"
```

---

# 14. 後續增量事件固定模板（APPEND TEMPLATE）

每次新增事件一律用以下格式，先追加故事，再回寫關係硬狀態：

```yaml
EVENT:
  event_id: "E46起依序編號"
  date: "理火三年槐月X日｜時段｜第X夜或第X日"
  title: "事件名稱"
  status: "CONFIRMED／OPEN／CLOSED／STAGED／其他正式標籤"

  cause:
    - "為什麼事件會發生"

  participants:
    - "參與人物"

  state_before:
    - "事件前人物、關係、帳目與場景狀態"

  process:
    - "依先後保存關鍵行動與明示語句"

  immediate_result:
    - "當場發生了什麼"

  relationship_delta:
    person_name:
      before: "原狀態"
      change: "改變原因"
      after: "新狀態"

  ledger_delta:
    - "新增或撤回的銀錢、物品、契約"

  public_knowledge:
    witnesses: "誰看見／聽見"
    rumor_status: "無／局部／公開／全城已確認"

  consent_boundary:
    accepted:
      - "已同意內容"
    rejected:
      - "已拒絕內容"
    undecided:
      - "仍未決內容"

  future_hook:
    - "事件留下的後續問題"

  correction_priority:
    - "若與舊紀錄衝突，明寫覆蓋哪一條"
```

## 關係回寫規則

每次事件後，只在以下情況回寫第 3 區「關係硬紀錄」：

1. 人物作出明確選擇；
2. 契約簽署、撤回、拒絕或結案；
3. 公開關係定位改變；
4. 長期承諾或有效拒絕成立；
5. 原本未知事項被正式揭露。

單純調情、笑、喝酒、留場、吃醋、注意、做夢、被說中心事，不足以自動改寫硬關係。

---

# 15. MASTER SAVE 核心讀法

> **關係硬紀錄記現在。**  
> **因果故事記為什麼。**  
> **專屬人物記誰因白御行而進入這條線。**  
> **帳目記承諾是否真的付出。**  
> **同意矩陣防止把拒絕寫成欲拒還迎。**  
> **時間軸防止第五夜的結果倒流回第一夜。**

本檔是白御行線唯一 MASTER 基線。V1.0、V1.1、V1.2、V1.4 只作來源證據；V1.5、V1.6 保留為合法 HOT 疊加層，其中 V1.6 為直接接關入口。


---

# 16｜HOT V1.5–V1.9 固化事件鏈（E46–E77）

## 16.0 固化映射

```yaml
V4_1_CONSOLIDATION_MANIFEST:
  inherited_events: "E01-E45"
  promoted_from_hot_v1_5: "E46-E54"
  promoted_from_hot_v1_6: "E55-E61"
  promoted_from_hot_v1_7: "E62-E69"
  promoted_from_hot_v1_8: "E70-E73"
  promoted_from_hot_v1_9: "E74-E77"
  master_cutoff: "槐月十七日晚，李瓶兒接受當晚留宿後，睡處與進一步親密仍待決定"
  source_gap_lock:
    - "V1.7 停在張麗華花燭前入睡，V1.8 從槐月十七日上午開始。"
    - "V1.8 沒有提供槐月十六日晚花燭儀式完整過程。"
    - "因此本 MASTER 不補寫該晚是否完成儀式、性交、射精或其他細節。"
```

## E46｜李師師／師理理第一次完整性交

```yaml
EVENT_RECORD:
  event_id: "E46"
  source_alias: "HOT_V1_5_RIR-E01_TO_E03"
  story_time: "槐月十一日深夜至槐月十二日清晨"
  location: "李師師私人房間"
  participants:
    - "白御行"
    - "李師師／師理理"
  status: "COMPLETED_CONSENSUAL_ADULT_SEXUAL_EVENT"
  confirmed:
    - "雙方清醒並同意完整陰道性交。"
    - "李師師主動選擇姿勢、節奏與何時允許白御行完成。"
    - "白御行在她明示『現在』後體內射精。"
    - "沒有避孕紀錄。"
  pregnancy: "UNKNOWN"
  private_identity:
    - "師理理仍是李師師在白御行私人關係中的表現，不是新人或第二人格。"
```

## E47｜疼痛界線、事後停留與私人記憶

```yaml
EVENT_RECORD:
  event_id: "E47"
  source_alias: "HOT_V1_5_RIR-E02_E04_E05_E06"
  status: "BOUNDARY_AND_RELATIONSHIP_MEMORY_CONFIRMED"
  confirmed:
    - "白御行曾未先詢問即在李師師肚臍附近施加疼痛刺激。"
    - "李師師立即制止；白御行接受未來疼痛玩法須事前詢問。"
    - "性交後兩人長時間相擁，李師師要求白御行先不要放開。"
    - "李師師承諾只要仍認得自己，不會讓這一夜被後來傳聞蓋掉。"
    - "白御行是她抵達仁宗朝觀止後第一個性交對象，也是師理理此私人身份第一次自行選擇的男人。"
  not_established:
    - "一生第一個男人"
    - "戀愛"
    - "排他"
    - "婚姻"
    - "永久身體資格"
```

## E48｜錯過再會、十二香皂與新招數欠帳

```yaml
EVENT_RECORD:
  event_id: "E48"
  source_alias: "HOT_V1_5_RIR-E07_E08"
  story_time: "槐月十二日至槐月十五日"
  status: "GIFT_DELIVERED_AND_APPOINTMENT_EXPIRED"
  confirmed:
    - "白御行因定陶商會事件未赴原定第二夜再會。"
    - "他派人送一盒十二種花香定陶香皂與不能赴約之訊息。"
    - "李師師收下全盒，先使用白梅香。"
    - "她回箋表示該夜不再留門，但新招數仍欠著。"
    - "李師師曾把紅娘氏列為可能三人親密第一人選；紅娘氏未被正式邀請，也未同意。"
```

## E49｜定陶十二車三烤鹽失竊與全數找回

```yaml
EVENT_RECORD:
  event_id: "E49"
  source_alias: "HOT_V1_5_DTC-E01_E02"
  story_time: "槐月十二日至槐月十五日"
  location: "定陶商會京師東倉及三處藏貨點"
  status: "GOODS_RECOVERED_CASE_NOT_CLOSED"
  confirmed:
    - "十二車、九十六包三烤鹽以偽造會長直批票、仿印、真舊票紙、舊旗牌與正確夜間口令被提走。"
    - "程景衡使用尚未返程之定陶第七運隊，同時突擊三處藏貨點。"
    - "十二車全部找回；折合九十五包半原貨，一半包被拆樣，八包外皮被刮洗。"
    - "捕獲二十七人，五人逃走。"
  enemy_state: "ORGANIZED_NETWORK_CONFIRMED_CORE_UNKNOWN"
```

## E50｜第一告密者受保護與領賞

```yaml
EVENT_RECORD:
  event_id: "E50"
  source_alias: "HOT_V1_5_DTC-E03"
  status: "PROTECTION_PROMISE_EXECUTED"
  actor: "年輕車夫，姓名未公開固化"
  contribution:
    - "提供三處藏貨點。"
    - "提供三十三人分錢名冊。"
    - "使商會能同步收網。"
  result:
    - "本人與家眷由商會保護。"
    - "四十三兩急債清除。"
    - "另領二百兩賞銀。"
  lock:
    - "不得因後續重刑政策撤銷首告保全。"
```

## E51｜石魁、灰簿先生與吳六未決

```yaml
EVENT_RECORD:
  event_id: "E51"
  source_alias: "HOT_V1_5_DTC-E04_E05"
  status: "ACTIVE_INVESTIGATION"
  confirmed:
    - "河東車行牙人石魁被捕，與車隊、藏倉、分帳及員工資訊收買有關。"
    - "底層口供提到『灰簿先生』，其本體、是否單一人物均未知。"
    - "東倉副倉簿吳六母親重病、借支兩次遭舊例駁回。"
    - "石魁曾以藥錢接近吳六。"
    - "石魁口供稱吳六曾可能答應、後又退出。"
    - "吳六未出現在藏貨與分帳現場，當時下落未知。"
  guilt_of_wu_liu: "NOT_ESTABLISHED"
```

## E52｜三烤停售、六烤倍價與銀庫防守

```yaml
EVENT_RECORD:
  event_id: "E52"
  source_alias: "HOT_V1_5_DTC-E06_E07"
  status: "POLICY_ACTIVE"
  salt_policy:
    - "京師三烤鹽封存停售。"
    - "定陶停止供應舊三烤。"
    - "六烤鹽分批運京，牌價為原三烤兩倍。"
    - "六烤使用新印、新繩、雙色封口。"
  vault_defense:
    - "銀庫與貨倉守備交叉換防、重新驗牌與換口令。"
    - "發現新鞋印、上油門軸、三重門位置圖與攜舊值夜名單者。"
    - "銀庫沒有實際失銀。"
  anonymous_note:
    - "匿名紙條只按攻心計處理，不作現任內鬼證據。"
```

## E53｜隨機交叉審計與急難護持案

```yaml
EVENT_RECORD:
  event_id: "E53"
  source_alias: "HOT_V1_5_DTC-E08_E09"
  status: "FORMAL_TRIALS_ACTIVE"
  cross_audit:
    - "京師銀庫先試行一個月。"
    - "帳房、契印、倉務、行路四房隨機交叉抽人與抽批次。"
    - "審計者只有記錄與上報權。"
    - "早期查出封條重號與驗色石磨損，未因此定罪。"
  hardship_program:
    name: "定陶商會急難護持案"
    period: "六個月試行"
    confirmed:
      - "醫藥、喪葬、贖人可先救後查。"
      - "可作無息或低息借支。"
      - "受助不降職、不羞辱。"
      - "本人若背叛仍處置，家眷生路不先切斷。"
```

## E54｜涉案者押回定陶、補假與調查授權

```yaml
EVENT_RECORD:
  event_id: "E54"
  source_alias: "HOT_V1_5_DTC-E10_E11_E12"
  status: "TRANSFER_AND_DELEGATION_ACTIVE"
  confirmed:
    - "涉案者分批、分路押送定陶總部。"
    - "家屬對外只知奉總部調派；斷薪、缺藥、缺糧可先救濟。"
    - "較輕者可能送礦場三年；重犯由定陶依證據另定。"
    - "本時點沒有個別死亡、致殘或大野澤處置完成紀錄。"
    - "參與四日追查、換防、押運與夜審者下月分批帶薪補假。"
    - "程景衡與師爺房追外圍節點，只有重大人命、高層涉案、第二次攻擊或需會長法位才即時上報。"
```

## E55｜張麗華明示接受情人關係

```yaml
EVENT_RECORD:
  event_id: "E55"
  source_alias: "HOT_V1_6_ZLH-E01_E02"
  story_time: "槐月十五日晚"
  status: "LOVER_RELATION_ACCEPTED"
  confirmed:
    - "張麗華同意作白御行情人。"
    - "雙方互相親吻。"
    - "不立婚書、不入白家、不形成所有權。"
    - "她仍居觀止並保有見面、身體與相處方式之決定權。"
    - "兩人約定槐月十六日晚以紅衣、紅帳、紅蓋頭、紅燭與合巹酒作私人情人花燭。"
    - "『不能拒絕』經校正後只指象徵禮物，不包含身體；當晚親密仍須重新同意。"
```

## E56｜李師師嫉妒、私人稱呼與槐月十五日晚共處

```yaml
EVENT_RECORD:
  event_id: "E56"
  source_alias: "HOT_V1_6_RIR15-E01_TO_E03"
  story_time: "槐月十五日晚"
  status: "PRIVATE_RELATION_CONTINUES"
  confirmed:
    - "白御行敲門並獲准進李師師房。"
    - "私人稱呼形成：李師師稱『御行』，白御行稱『理理』；生氣或劃界時她可稱全名。"
    - "白御行立即告知張麗華已接受情人與次日花燭。"
    - "李師師明示嫉妒、不舒服，但不要求毀約。"
    - "她要求白御行到張麗華處時不要身在其處、心想別人。"
    - "白御行澄清未拖延告知後，她撤回故意隱瞞之指責，但保留嫉妒。"
```

## E57｜阿泠現身與白玉池水療提案

```yaml
EVENT_RECORD:
  event_id: "E57"
  source_alias: "HOT_V1_6_BYC-E01_TO_E03"
  story_time: "槐月十五日晚"
  location: "白玉池"
  status: "NEW_ENTITY_MANIFESTED_BUSINESS_PAUSED"
  confirmed_observable:
    - "霧中女子自選名字『阿泠』，解釋為水清而有聲。"
    - "可借霧與泉水顯出女性輪廓。"
    - "能控制水流方向、壓力與落點，替人推揉肩頸腰背。"
    - "她稱白玉池是自己的地方，是否水療、做幾席由她決定。"
    - "不得把她名字與存在作公開招牌。"
  refused_or_not_accepted:
    - "白姓"
    - "白御行妹妹"
    - "白家人"
    - "白御行所有物"
  business_state: "PROPOSAL_ONLY; NO_PRICE_NO_CONTRACT_NO_OPENING"
```

## E58｜李瓶兒入池與追求機會未關閉

```yaml
EVENT_RECORD:
  event_id: "E58"
  source_alias: "HOT_V1_6_BYC-E04"
  status: "LIMITED_ROMANTIC_OPENING"
  confirmed:
    - "李瓶兒先在屏風外確認，再在李師師與阿泠說明後自行決定脫衣入池。"
    - "她明示不是因白御行命令才下水。"
    - "白御行問追求是否有機會，李瓶兒回答『有機會』。"
    - "她要求白御行分清公事帳、好奇入池與男女意思，並看他如何處理既有女人與承諾。"
  not_established:
    - "戀愛"
    - "情人"
    - "性交"
    - "排他"
```

## E59｜白玉池「歸零」、算式與續字回顯

```yaml
EVENT_RECORD:
  event_id: "E59"
  source_alias: "HOT_V1_6_BYX-E01_TO_E05"
  status: "ANOMALY_OBSERVED"
  confirmed_observable:
    - "白御行作泠／靈／零／000玩笑後，池中短暫安靜並出現三個暗影與來源不明之『歸零』聲。"
    - "重複說歸零會形成暗紋。"
    - "簡單算式可由泉聲、水珠與文字回顯答案。"
    - "池壁出現規整方紋與每六息明滅之『續』字。"
    - "蘇清測得不同人皆可輸入、未完成算式可暫存、歸零可清除、條件句可分段回顯。"
  not_proven:
    - "計算器"
    - "液晶介面"
    - "程式"
    - "任意命令執行系統"
```

## E60｜白玉池封池、蘇清研究與潘金蓮尚未介入之初始狀態

```yaml
EVENT_RECORD:
  event_id: "E60"
  source_alias: "HOT_V1_6_SECTIONS_7_8"
  status: "SEALED_FOR_INVESTIGATION"
  confirmed:
    - "李瓶兒以紅繩封住白玉池入口。"
    - "對外只稱水脈檢修／泉況異常。"
    - "蘇清設計最小變因測試並記錄。"
    - "阿泠感知與壓制水勢異常。"
    - "李瓶兒控制人員、帳目與對外說法。"
    - "此時潘金蓮尚未被正式告知完整異常。"
  prohibited:
    - "一般入池"
    - "水療營運"
    - "碰觸續字"
    - "臨時高風險玩笑測試"
```

## E61｜李師師共宿、停止權校正與清晨射精

```yaml
EVENT_RECORD:
  event_id: "E61"
  source_alias: "HOT_V1_6_RIR16-E01_TO_E03_AND_PREGNANCY"
  story_time: "槐月十五日晚至十六日清晨"
  status: "CONSENSUAL_OVERNIGHT_INTIMACY_COMPLETED"
  boundary_sequence:
    - "白御行曾說若忍不住別怪他硬來；李師師立即停止原安排。"
    - "白御行改口承認由她決定『來／不要』後，她恢復赤裸相抱許可。"
    - "李師師親手引導他的手至胸前。"
    - "她同意陰莖留在體內相抱入睡，初入時要求停住，適應後才繼續。"
  overnight_result:
    - "夜半前自然軟下滑出。"
    - "夜間沒有射精、沒有重新進入。"
  morning_result:
    - "李師師以手刺激，白御行約九分多鐘後射精。"
    - "不是陰道內射；李師師以口清理並吞嚥。"
  pregnancy_boundary:
    - "槐月十一日體內射精之妊娠仍未知。"
    - "李師師會記月事、找可靠女醫。"
    - "情況明白前，未來陰道性交不允許內射。"
    - "若懷孕，是否留下由李師師決定。"
```

## E62｜張麗華花燭當日確認與時辰

```yaml
EVENT_RECORD:
  event_id: "E62"
  source_alias: "HOT_V1_7_ZLH16-E01_E02"
  story_time: "槐月十六日白日"
  status: "FLOWER_CANDLE_DUE_AND_SCHEDULED"
  confirmed:
    - "紅衣、紅帳照原安排。"
    - "不掛囍、不用白家徽記、不稱妻或夫人、不公開收賀。"
    - "只請龐春梅飲第一杯後離場。"
    - "李師師獲准白日替張麗華梳頭。"
    - "酉正點燭、戌初開門，過時可關門。"
    - "張麗華定下吉時，不請陰陽先生。"
  source_gap:
    - "V1.7之後至V1.8之前的花燭完整執行情況沒有被提供。"
    - "本 MASTER 不補寫是否完成性交、射精或正式儀式細節。"
```

## E63｜續字化為黑色門縫與對側互動

```yaml
EVENT_RECORD:
  event_id: "E63"
  source_alias: "HOT_V1_7_BYX16-E01_TO_E04"
  status: "TEMPORARY_INTERACTIVE_PASSAGE_OBSERVED"
  confirmed_observable:
    - "續字停在最亮後化為黑色細門縫。"
    - "門後可見夜色、遠燈、濕臺階、大量鞋與成對白點。"
    - "提燈女子可聽見、回應、提問並接取部分物品。"
    - "另有貼近她的未知聲音，未見身體。"
    - "提燈女子能排列事件先後，不能提供穩定經過時長。"
    - "四十二測試形成光點分組、問字與『我也』回顯。"
  not_proven:
    - "黑洞海是正式地名"
    - "平行宇宙"
    - "時間逆流"
    - "死後世界"
```

## E64｜時空道人承認漏籤

```yaml
EVENT_RECORD:
  event_id: "E64"
  source_alias: "HOT_V1_7_TD16-E01_TO_E03"
  status: "DUTY_FAILURE_ADMITTED_REPAIR_PENDING"
  confirmed:
    - "觀止以召集門口周圍生物方式尋找疑似偽裝的時空道人。"
    - "只能透過銅鏡看見的灰蛾被龐春梅以白瓷碗扣住，碗影似持竹籤人手。"
    - "時空道人承認槐月十五日晚沒有完成白御行命運籤交付。"
    - "他聲稱當晚同時出現七個不同時間位置的白御行；主張未被客觀驗證。"
    - "空白竹籤顯出七道與既有因果相關投影。"
    - "正式補籤仍未完成。"
  lock:
    - "不得倒填未曾出現的籤。"
    - "不得改寫成白御行忘記領。"
```

## E65｜活物與事件傳遞測試

```yaml
EVENT_RECORD:
  event_id: "E65"
  source_alias: "HOT_V1_7_TEST-01_TO_04"
  status: "TESTS_COMPLETED_WITH_UNCERTAIN_MECHANISM"
  confirmed:
    - "帶根青草連同紅線、缺葉角與泥團抵達對側。"
    - "蒼蠅與蚊蟲可穿越；一隻標記蒼蠅後來在觀止側出現相反翅根標記。"
    - "蟑螂跨界時停格，拉回後少一個紅點；另一紅點留在對側且可觸摸。"
    - "青蛙未完整推入，對側先後出現提前蛙鳴與蹼形足印。"
    - "青蛙強烈退避後，蘇清立即停止試驗。"
  not_proven:
    - "原個體返回"
    - "鏡像"
    - "複製"
    - "物質分割"
    - "預知"
```

## E66｜黑影分離、門後自行選擇與暫閉合

```yaml
EVENT_RECORD:
  event_id: "E66"
  source_alias: "HOT_V1_7_PLAYER_HYPOTHESES_AND_BYCLOSE"
  status: "PASSAGE_TEMPORARILY_CLOSED"
  confirmed_observable:
    - "時空道人之投影辨認中，一道無影投影被解讀為世界過快接受白御行判斷留下的空殼；此為角色／審計解讀。"
    - "該投影其後形成身體與影子，兩者被門分隔。"
    - "其身體拒絕白御行提供的四面稱號後消散。"
    - "門後黑影自行決定不跨門、不奪白御行名字，留在對側等／看。"
    - "門縫完全合攏，池面恢復清水。"
    - "時空道人只稱『暫閉合』。"
  player_myth_status:
    - "黑洞／白洞、疊加態、神之影、熵增、人類智慧熵減與創世前神話只保存為玩家模型，未升格世界基線。"
```

## E67｜阿泠兄妹方向仍未成立

```yaml
EVENT_RECORD:
  event_id: "E67"
  source_alias: "HOT_V1_7_SECTION_8"
  status: "PROPOSED_NOT_ACCEPTED"
  confirmed:
    - "白御行再次提議認阿泠作妹妹。"
    - "阿泠拒絕『白御池』名稱，重申阿泠是人／存在之名，白玉池是池。"
    - "她只說若妹妹代表受欺負時有人站她一邊、闖禍先問清楚、不把她忘在池裡，可以考慮。"
  current:
    sibling_relation: false
    name_change: false
    ownership: false
```

## E68｜商會授權與蘇清、小翠浴房邊界

```yaml
EVENT_RECORD:
  event_id: "E68"
  source_alias: "HOT_V1_7_SECTIONS_9_10"
  status: "DELEGATION_AND_REFUSALS_CONFIRMED"
  merchant:
    - "白御行決定槐月十六日白日不回商會。"
    - "他以『船沉了再來叫我』授權副會長按既定方案處理普通貨務。"
    - "只有方案失效、重大傷亡、貨物全失或同級事故升級回報。"
  su_qing:
    - "白御行邀她共同沐浴；蘇清明確拒絕並安排客浴。"
  xiaocui:
    - "小翠自願提供洗頭、擦背、遞皂角與衣物，不下水、門不鎖。"
    - "白御行追加私密清洗要求，小翠明確拒絕。"
    - "原同意服務完成，沒有性服務、私密觸摸或共同入浴。"
```

## E69｜花燭前休息

```yaml
EVENT_RECORD:
  event_id: "E69"
  source_alias: "HOT_V1_7_REST16-E01"
  story_time: "槐月十六日午後"
  status: "REST_CONFIRMED"
  confirmed:
    - "白御行完成客浴、換乾淨中衣。"
    - "觀止安排西側醒酒小房、溫水、清粥與李師師送來之外袍。"
    - "酉初前一般帳目、客人與普通商會消息不得打擾。"
    - "只有失火、死亡、遭襲或白玉池重開才即時喚醒。"
    - "白御行入睡。"
```

## E70｜張麗華酒莊交接與管理入口

```yaml
EVENT_RECORD:
  event_id: "E70"
  source_alias: "HOT_V1_8_SECTIONS_1_2_6"
  story_time: "槐月十七日上午"
  status: "ACTIVE_HANDOVER"
  confirmed:
    - "白御行召商會師爺處理酒莊契書、帳目與交接。"
    - "白御行允許在不損商會利益之前提下，以個人範圍補足張麗華需要。"
    - "張麗華拒絕永久資源輸送，要求按正常商業流程。"
    - "酒莊主要問題為花農花露款與年度週轉不足，不是已破產。"
    - "白御行不介入她看帳，承認接手者有管理權。"
  one_wan_tael:
    - "白御行提到潘金蓮處原預備給張麗華飲酒的一萬兩足以支應約兩年花農款。"
    - "該筆錢在 V1.8 仍未確定屬白御行私產、張麗華私產或酒莊週轉。"
```

## E71｜觀止餐飲改良但不開平價早餐鋪

```yaml
EVENT_RECORD:
  event_id: "E71"
  source_alias: "HOT_V1_8_SECTIONS_3_4"
  status: "PROPOSAL_ACTIVE"
  confirmed:
    - "白御行認為觀止後廚缺乏創意。"
    - "曾考慮開早餐鋪，因不願用自身資源搶普通小販銅板生計而放棄。"
    - "張麗華接受改善餐飲，但不應壓迫小商販。"
    - "方向改為外部餐館／商販供餐與改善觀止體驗。"
    - "白御行請李瓶兒安排觀止兩日外餐，定位為商務後勤，不是私人補償；李瓶兒接受處理。"
```

## E72｜李瓶兒之秘密關係提案未接受

```yaml
EVENT_RECORD:
  event_id: "E72"
  source_alias: "HOT_V1_8_LI_PINGER"
  status: "LIMITED_CLOSENESS_PROPOSAL_UNRESOLVED"
  confirmed:
    - "白御行在李瓶兒房中表達喜歡，提出『偷情』或秘密關係方向。"
    - "李瓶兒接受當下親近，但沒有正式接受長期秘密位置。"
    - "她要求不要把她變成方便隱藏的人，仍要看自己是否真正被選擇。"
  not_established:
    - "秘密情人"
    - "性交"
    - "長期承諾"
```

## E73｜張麗華三日陪伴線

```yaml
EVENT_RECORD:
  event_id: "E73"
  source_alias: "HOT_V1_8_ZHANG_LIHUA"
  status: "THREE_DAY_COMPANIONSHIP_ACCEPTED"
  confirmed:
    - "張麗華接受白御行三日陪伴承諾。"
    - "她知道李師師與其他複雜關係存在。"
    - "她不要求白御行完全停止風流。"
    - "核心要求是不欺瞞、不讓她只能猜、關係有清楚界線。"
    - "她明示帳是帳、感情是感情。"
  source_gap:
    - "三日如何精確起算與槐月十六日晚花燭細節未在 V1.8 完整記錄。"
```

## E74｜四人火鍋家宴

```yaml
EVENT_RECORD:
  event_id: "E74"
  source_alias: "HOT_V1_9_DIN17-E01_E02"
  story_time: "槐月十七日晚"
  location: "張麗華房"
  status: "COMPLETED"
  participants:
    - "白御行"
    - "張麗華"
    - "蘇清"
    - "李瓶兒"
  meal:
    - "鴛鴦火鍋、炸雞、肉夾饃、酸梅湯與溫茶。"
    - "白御行不吃辣，食清湯與不辣食物。"
  confirmed:
    - "張麗華明示李瓶兒是來吃飯，不是來收桌。"
    - "蘇清與李瓶兒食辣較多並有吃撐／按腹休息之可見反應。"
  not_confirmed:
    - "腹瀉"
    - "次日必然肛門疼痛"
```

## E75｜房內兩日「家人」框架

```yaml
EVENT_RECORD:
  event_id: "E75"
  source_alias: "HOT_V1_9_FAM17-E01_TO_E03"
  status: "TEMPORARY_PRIVATE_FRAME_ACCEPTED"
  player_declaration:
    - "這兩日在張麗華房內只有家人，不排掌櫃、花魁、情人或先後位置。"
    - "唯一床位權由張麗華決定白御行能否睡床。"
  responses:
    - "張麗華接受臨時框架，但保留房間與床鋪管理權。"
    - "蘇清以玩笑方式接受。"
    - "李瓶兒只接受當晚以家人方式相處與不作掌櫃服務。"
  not_established:
    - "永久家族"
    - "婚姻"
    - "白家名冊"
    - "任何人的身體義務"
```

## E76｜李瓶兒接受當晚留宿

```yaml
EVENT_RECORD:
  event_id: "E76"
  source_alias: "HOT_V1_9_STAY17-E01_E02"
  status: "OVERNIGHT_STAY_ACCEPTED_WITHOUT_SEXUAL_CONSENT"
  confirmed:
    - "李瓶兒決定今晚不回掌櫃房、不去看帳。"
    - "她接受留在張麗華房或由張麗華安排之相連休息處。"
    - "確切睡處仍未決。"
    - "張麗華洗浴回來後再分配白御行、蘇清、李瓶兒之睡處。"
  not_implied:
    - "同床"
    - "裸體"
    - "性交"
    - "白御行可觸碰"
```

## E77｜寢具用品準備與親密未決

```yaml
EVENT_RECORD:
  event_id: "E77"
  source_alias: "HOT_V1_9_STAY17-E03_SUP17-E01"
  status: "PREPARATIONS_ORDERED_INTIMACY_UNDECIDED"
  confirmed:
    - "張麗華下令準備熱水、乾淨寢衣、一床薄被、三只乾淨恭桶／葉香桶、草紙、溫水與夜燈。"
    - "三只桶暫分屏風後、外間與隔壁空房。"
    - "白御行席間曾露骨邀請三女，但沒有由此建立他人同意。"
    - "李瓶兒明示留下休息不等於答應讓白御行『吃』。"
    - "蘇清此前不接受體內射精之界線仍有效。"
  master_cutoff:
    - "用品尚未確認送達或使用。"
    - "張麗華尚未分床。"
    - "沒有任何當晚性事件在 V1.9 內成立。"
```

---

# 17｜截至 HOT V1.9 關係硬狀態覆寫

> 本區法位高於本檔第3區之 V1.4 截止快照。

```yaml
RELATIONSHIP_OVERRIDE_AT_V1_9:
  ZHANG_LIHUA:
    state: "ACTIVE_LOVER_RELATION + ACTIVE_WINERY_HANDOVER + THREE_DAY_COMPANIONSHIP"
    established:
      - "明示接受作白御行情人。"
      - "不立婚書、不入白家、不形成所有權。"
      - "取得酒莊管理入口，要求帳與感情分開。"
      - "接受三日陪伴與不欺瞞、界線清楚之要求。"
      - "槐月十七日晚保有房間與床位管理權。"
    flower_candle_completion: "SOURCE_GAP_UNKNOWN"
    exclusivity: false
    permanent_consent: false

  LI_SHISHI_SHILILI:
    state: "ACTIVE_PRIVATE_SEXUAL_RELATION; PURSUIT_OPEN"
    established:
      - "至少一次完整雙方同意性交並體內射精。"
      - "私人稱呼『理理／御行』。"
      - "事後長時間停留與私人記憶承諾。"
      - "會嫉妒但未要求排他。"
    pain_play: "EACH_TIME_REQUIRES_PRIOR_CONSENT"
    pregnancy: "UNKNOWN"
    current_internal_ejaculation_rule: "NOT_ALLOWED_UNTIL_FURTHER_DECISION"
    marriage: false
    exclusivity: false

  LI_PINGER:
    state: "PURSUIT_OPEN + LIMITED_CLOSENESS + TONIGHT_STAY_ACCEPTED"
    established:
      - "回答追求『有機會』。"
      - "接受槐月十七日晚留宿與臨時家人框架。"
    not_established:
      - "戀愛"
      - "秘密情人"
      - "性交"
      - "永久家人"
      - "兩日完整留宿"

  SU_QING:
    state: "OLD_THREE_NIGHT_LEDGER_UNSETTLED_AT_V1_9 + ACTIVE_TWO_DAY_HOUSEHOLD_ARRANGEMENT"
    confirmed:
      - "槐月十七日晚與張麗華、李瓶兒同在房內家宴。"
      - "是否發生後續性事件仍未由 V1.9 建立。"
      - "二十八日交換在 V1.9 仍只屬討論，未正式接受。"
    source_conflict_on_novel_commission: "REMAINS_DISPUTED_UNLESS_LATER_HOT_RESOLVES"

  A_LING:
    state: "SELF_NAMED_POOL_ENTITY; AUTONOMOUS; POOL_SECURITY_PARTICIPANT"
    established:
      - "自選名阿泠。"
      - "能控制泉水並提供水壓推揉。"
      - "白玉池是她自稱的地方。"
    not_established:
      - "白姓"
      - "白御行妹妹"
      - "白家人"
      - "白御行女人"
      - "財產或浴房"

  XIAOCUI:
    state: "BOUNDARY_CAPABLE; LIMITED_BATH_SERVICE_COMPLETED; RED_GREEN_PROPOSAL_PENDING"
    confirmed:
      - "曾拒絕八百兩安排。"
      - "同意洗頭、擦背、遞物。"
      - "拒絕私密清洗，拒絕有效。"
      - "紅綠組仍需本人對每次服務另行同意。"

  PAN_JINLIAN:
    state: "ACTIVE_MANAGER; NOW_KNOWS_WHITE_JADE_POOL_PORTAL_EVENT"
    confirmed:
      - "參與召集生物、支持關門與觀止秩序維持。"
      - "其空間宣告能力仍是提出請求，不能保證觀止如何回答。"

  TIME_DAOIST:
    state: "MISSED_LOT_ADMITTED; FORMAL_REPAIR_PENDING"
    replacement_lot: false

  BAI_YUXING__WHITE_JADE_POOL_BLACK_SHADOW:
    state: "UNKNOWN_INDEPENDENT_PRESENCE_LEFT_BEHIND_CLOSED_PASSAGE"
    identity: "UNKNOWN"
    ownership_or_player_body: false
```

---

# 18｜截至 HOT V1.9 帳目、資產、契約與物品覆寫

```yaml
LEDGER_ASSET_OVERRIDE_AT_V1_9:
  ZHANG_LIHUA_WINERY:
    status: "ACTIVE_HANDOVER"
    known_issues:
      - "花農花露採購款"
      - "年度週轉不足"
    not_bankrupt: true
    one_wan_tael_status: "UNRESOLVED_AS_PRIVATE_ASSET_OR_WINERY_CAPITAL_AT_V1_9"

  LI_SHISHI_SOAP_GIFT:
    item: "十二種花香定陶香皂"
    delivered: true
    first_used: "白梅香"

  DINGTAO_SALT_CASE:
    recovered: "十二車、折合九十五包半"
    arrested: 27
    escaped: 5
    three_roast_capital_sale: "STOPPED_AND_SEALED"
    six_roast: "DISPATCHED_TO_JINGSHI_AT_DOUBLE_FORMER_PRICE"
    case_status: "CONTAINED_BUT_NOT_CLOSED"

  CROSS_AUDIT:
    site: "京師銀庫"
    period: "一個月試行"
    state: "ACTIVE"

  EMPLOYEE_HARDSHIP_PROGRAM:
    period: "六個月試行"
    state: "ACTIVE"

  DETAINEE_TRANSFER:
    destination: "定陶總部"
    state: "IN_TRANSIT_OR_AWAITING_HQ_ADJUDICATION"

  LI_PINGER_EXTERNAL_MEALS:
    scope: "觀止兩日外餐安排"
    state: "ACCEPTED_FOR_HANDLING"

  NIGHT17_PREPARATIONS:
    items:
      - "熱水"
      - "寢衣"
      - "薄被"
      - "三只恭桶／葉香桶"
      - "草紙"
      - "溫水"
      - "夜燈"
    state: "ORDERED_NOT_CONFIRMED_DELIVERED_AT_MASTER_CUTOFF"
```

---

# 19｜截至 HOT V1.9 知情、傳聞、秘密與異常覆寫

```yaml
KNOWLEDGE_OVERRIDE_AT_V1_9:
  LI_SHISHI_PRIVATE_SEXUAL_EVENT:
    core_knowers:
      - "白御行"
      - "李師師／師理理"
    public: false
    soap_messenger_only_knows: "送禮與不能赴約，不知性事件"

  ZHANG_LIHUA_LOVER_AND_FLOWER_CANDLE:
    known_to:
      - "白御行"
      - "張麗華"
      - "李師師／師理理"
      - "李瓶兒"
      - "龐春梅知道當日第一杯與部分安排"
    public_wedding: false

  WHITE_JADE_POOL_CORE:
    direct_or_core_knowers_by_v1_7:
      - "白御行"
      - "蘇清"
      - "李師師／師理理"
      - "阿泠"
      - "潘金蓮"
      - "龐春梅（至少知道召集生物、灰蛾與後院重大異常）"
      - "時空道人"
    partial:
      - "李瓶兒知封池、阿泠與早期異常；是否見證全部門後細節未固定。"
      - "部分小廝與路人只知後院抓生物或封池，不知完整內容。"
    public: false
    status: "SEALED_AND_MONITORED; PASSAGE_ONLY_TEMPORARILY_CLOSED"

  FOUR_PERSON_FAMILY_FRAME:
    known_to:
      - "白御行"
      - "張麗華"
      - "蘇清"
      - "李瓶兒"
    public: false
    permanent_family: false

  MERCHANT_CASE:
    staff_knowledge: "依職務分層"
    enemy_core: "UNKNOWN"
    wu_liu_guilt: "NOT_ESTABLISHED"
```

---

# 20｜截至 HOT V1.9 未決事項

## 20.1 立即接關

1. 張麗華洗浴後如何分配白御行、蘇清、李瓶兒之睡處。
2. 李瓶兒只接受當晚留宿；任何同床、裸體、觸碰或性交均未決。
3. 蘇清與張麗華、白御行之兩日共同生活如何繼續。
4. 寢具、熱水、薄被與三只恭桶是否實際送達。

## 20.2 張麗華

1. 槐月十六日晚私人花燭之完整執行情況在 V1.7–V1.8 間有來源缺口，不得補寫。
2. 酒莊花農款、年度週轉與一萬兩法位。
3. 三日陪伴如何起算、完成與結束。
4. 她如何處理白御行多重關係與不欺瞞要求。

## 20.3 李師師／師理理

1. 槐月十一日體內射精是否造成妊娠。
2. 月事是否如期、是否找到可靠女醫、避子方式是否取得。
3. 新招數欠帳何時處理。
4. 紅娘氏三人親密只屬討論，尚未邀請。

## 20.4 李瓶兒

1. 是否接受任何長期秘密位置。
2. 是否認為自己真正被選擇，而非方便隱藏。
3. 當晚留宿後之睡處與親密界線。

## 20.5 白玉池

1. 暫閉合是否持續、是否在別處重開。
2. 提燈女子、未知聲音、黑影、鞋、白點與多天空映像之身分與機制。
3. 活物／標記／聲音跨界測試之個體同一性與時間問題。
4. 阿泠與 MASTER 早期白玉池無名女子是否同一存在，仍不得合併。
5. 水療何時可重新評估；無 GM 授權不得復開。
6. 時空道人正式補籤。

## 20.6 定陶商會

1. 吳六下落與罪責。
2. 五名逃犯。
3. 灰簿先生本體。
4. 借支申請抄件外洩路徑。
5. 押送者個別最終處置。
6. 白御行所稱親手殺死之背叛者名冊、正式紀錄與家屬援助執行。
7. 六烤運京後市場與信用結果。
8. 一個月交叉審計與六個月急難護持案評估。

---

# 21｜截至 HOT V1.9 MASTER 截止狀態

```yaml
MASTER_CUTOFF_STATE_V4_1:
  story_time: "理火三年槐月十七日晚，四人火鍋家宴後"
  location: "觀止青樓／張麗華房間"
  last_canonical_event: "E77"
  scene_state: "LI_PINGER_STAY_ACCEPTED; BED_AND_INTIMACY_UNDECIDED"
  present:
    - "白御行"
    - "張麗華"
    - "蘇清"
    - "李瓶兒"
  hard_state:
    - "李瓶兒今晚留下，不回掌櫃房。"
    - "房內暫以家人相處，不形成永久名分。"
    - "張麗華保有房間與床位管理權。"
    - "李瓶兒沒有同意性行為。"
    - "熱水、寢衣、薄被、三只恭桶等已下令準備，尚未確認送達。"
  next_action_owner:
    - "世界可送入已下令用品。"
    - "張麗華決定房間與床位。"
    - "李瓶兒、蘇清、張麗華各自決定是否接受任何進一步親密。"
    - "白御行只控制自己的言行與選擇。"
```

---

# 22｜MASTER 與最新 HOT 接關規則

```yaml
ACTIVE_HOT_OVERLAY_V4_1:
  direct_resume_file: "觀止青樓_白御行線_HOT_SAVE_V2.3_槐月二十日深夜_沈萬三合作與師師薄情郎席前接關版.md"
  unmerged_but_valid_chain:
    - "HOT V2.0：槐月十八日清晨四人夜結"
    - "HOT V2.1：槐月十八日下午商戰、蘇清私約與白玉池補固"
    - "HOT V2.2：槐月十九日破曉師理理如夫人前置與張麗華獨宿夜結"
    - "HOT V2.3：槐月二十日深夜沈萬三合作與師師受審席前"
  load_order:
    - "先讀本 MASTER V4.1-R1，取得 E01–E77 長期因果。"
    - "再讀 HOT V2.3，取得 V2.0–V2.3 已繼承之最新切片。"
    - "若需要查 V2.3 摘要未展開之細節，再按 V2.0、V2.1、V2.2 回溯。"
  current_resume_point:
    - "槐月二十日深夜。"
    - "白御行在觀止內院東西廊交界。"
    - "李瓶兒可送醒酒湯或看傷，未保證進房。"
    - "張麗華若白御行回去便備水，若不回便熄燈。"
    - "白御行尚未選擇。"
```

---

# 23｜V4.1-R1 固化結論

> **E01–E45：沿用 V4.0-R1。**
>
> **E46–E77：由 HOT V1.5–V1.9 正式固化。**
>
> **V2.0–V2.3：合法 HOT，尚未併入 MASTER。**
>
> **實際接關：讀本 MASTER，再讀 HOT V2.3。**
