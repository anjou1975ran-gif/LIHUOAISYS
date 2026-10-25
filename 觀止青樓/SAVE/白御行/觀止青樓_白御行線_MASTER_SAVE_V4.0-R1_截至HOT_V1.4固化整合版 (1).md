# 觀止青樓｜白御行線 MASTER SAVE V4.0-R1
## 截至 HOT V1.4 固化整合版｜V1.5／V1.6 保留於 HOT 層

---

```yaml
SAVE_META:
  save_id: "GUANZHI_BAIYUXING_MASTER_V4_0_R1"
  title: "觀止青樓｜白御行線 MASTER SAVE"
  version: "V4.0-R1"
  world: "觀止青樓"
  world_runtime_profile:
    - "GUANZHI_QINGLOU_V10.0"
    - "GUANZHI_QINGLOU_V10.1-PATCH_WHEN_APPLICABLE"
  player: "白御行"
  route_status: "ACTIVE"
  record_type: "CONSOLIDATED_MASTER_ARCHIVE"
  fixed_calendar_anchor: "理火三年槐月五日｜永恆第一夜"
  master_cutoff: "理火三年槐月十一日深夜｜HOT V1.4 結束節點"
  current_route_resume_source: "HOT SAVE V1.6"
  current_route_resume_note: "V1.5 與 V1.6 未併入本 MASTER；實際接關仍以 V1.6 為準。"
  supersedes_as_master:
    - "觀止青樓_白御行線_MASTER_SAVE_V3.0-R1_正式厚肉因果資料庫版.md"
    - "觀止青樓_白御行線_MASTER_SAVE_V3.0-R2_補充修正版.md"
  absorbs_and_retires_from_default_load:
    - "觀止青樓_白御行線_HOT_SAVE_V1.0_槐月十日清晨接關版.md"
    - "觀止青樓_白御行線_HOT紀錄_V1.1_槐月十日_張麗華事件_私人秘密增補.md"
    - "觀止青樓_白御行線_HOT_SAVE_V1.2_槐月十一日清晨_李師師留觀止版.md"
    - "觀止青樓_白御行線_HOT_SAVE_V1.4_槐月十一日整夜事件全紀錄純淨版.md"
  valid_but_not_merged:
    - "觀止青樓_白御行線_HOT_SAVE_V1.5_槐月十五日傍晚_師理理初次肉體與定陶商會案雙線接關版.md"
    - "觀止青樓_白御行線_HOT_SAVE_V1.6_槐月十六日清晨_張麗華花燭前置與白玉池異常回顯封池版.md"
  rejected_source:
    file: "HOT_SAVE_V1.3"
    status: "ILLEGAL_CORRUPTED_SAVE"
    use: "AUDIT_ONLY"
```

```yaml
SOURCE_LOCK:
  master_v3_r1:
    sha256: "57311f329b845cf256a426ffcc034fcb9bee122bb4b29d711687858c07714040"
  master_v3_r2:
    sha256: "9e9c912997446f949f1b23652ab26c79b6686375b35dc28089329a1d1be862fb"
  hot_v1_0:
    sha256: "16047814a095444233670f927b1609196370900c7863287dcfa0a477bf0399cc"
  hot_v1_1_private:
    sha256: "f2b81ceb45bd2db3dea905e5dba48469091510e4f495ea5f5d8d061adbdf2fb3"
  hot_v1_2:
    sha256: "4a9968ccf7e6edc7faf5b25637e7559906f5077d13f010132269b3c7a615a7b0"
  hot_v1_4:
    sha256: "4c5ff297716d2f81c53facd0e370f84dc3304415acf1f31a87077d32834b6e50"
  excluded_hot_v1_5:
    sha256: "e9fc105e4be64a6934a2aa40af08cca26543e15b7752b5548f462ba57614d556"
  excluded_hot_v1_6:
    sha256: "ea7de1259b25d362fd4333728dfb9961463e57f0839e3f33d20422a776fe491d"
```

> **本檔固化至 HOT V1.4。**
>
> **V1.5 與 V1.6 不是被否定，而是刻意保留在 HOT 層，避免尚新的事件過早進入 MASTER。**
>
> **V1.0、V1.1、V1.2、V1.4 已被本檔吸收，後續預設載入不必再逐檔疊加。**

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
