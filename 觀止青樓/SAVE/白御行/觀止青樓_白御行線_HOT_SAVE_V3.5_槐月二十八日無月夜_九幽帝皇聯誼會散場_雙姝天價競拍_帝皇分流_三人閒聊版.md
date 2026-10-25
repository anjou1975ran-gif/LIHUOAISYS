# 觀止青樓｜白御行線 HOT SAVE V3.5
## 理火三年槐月二十八日無月夜｜九幽帝皇聯誼會散場 × 雙姝天價競拍 × 白玉池試營運 × 帝皇多線分流 × 白御行師師麗華三人閒聊版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V3_5_HUAI28_MOONLESS_JIUYOU_EMPEROR_ASSOCIATION_AUCTION_SPLIT_LINES_SETTLEMENT"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V3.5"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V11.0-R2"
  character_source: "觀止人物卡池_LCAPG_V2.2_辭歲入觀止動機校正_青禾六條增補_正式版"

  story_time_span:
    start: "HOT V3.4 後"
    current: "理火三年槐月二十八日無月夜／深夜"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AFTER_HOT_SAVE_COMMAND_AT_BAI_SHISHI_LIHUA_TABLE_CHAT_AFTER_EMPEROR_EVENT"

  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V3.4_槐月二十六日深夜_第二免費床成立_小翠三娘實習_紅娘側賭輸_三人抱睡版.md"
  previous_hot_sha256: "38454482b6e0a56a6507c74e1f54a203db22e4f79082aed75e4b535b6396f1fb"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"

  experimental_overlays:
    performance_patch:
      file: "觀止青樓_PATCH_風月角色表演與接戲能力_V0.1-EXP_獨立試跑未併主系統.md"
      status: "INDEPENDENT_TRIAL_OVERLAY_NOT_MERGED"
    analyzer_exit_patch:
      file: "觀止青樓_PATCH_分析器退場_重大升階定義_SCOPED_REACTIVATION_顯影反污染_V0.1-EXP.md"
      status: "GUANZHI_SPECIFIC_OPTIONAL_EXPERIMENTAL_OVERLAY_NOT_MERGED"
    lihuo_environment_patch:
      file: "理火環境_PATCH_V0.1.md"
      status: "REFERENCE_OPTIONAL_EXPERIMENTAL_OVERLAY_NOT_MERGED"

  save_scope:
    - "槐月二十八日九幽帝皇聯誼會於觀止大觀樓之正式前宴與後段自然分流"
    - "六條御息所、李師師、貂蟬、蘇清、疏影、阿麗婭、青禾、小翠、紅娘、辭歲、錦棠等當夜已確認出席／互動狀態"
    - "辭歲與錦棠雙人同台競拍、成交、欠單、分成與十日清算安排"
    - "白玉池只限本夜封場帝皇團之特殊試營運狀態"
    - "帝皇與人物各線只記可觀察事件；進房、關門、熄燈不推導未觀察之成人結果"
    - "李清照以寡居、逃難中之狀態再訪觀止，來找張麗華飲用白御行預付之一萬兩酒資"
    - "白御行、李師師、張麗華於尾聲重新同桌閒聊並下令 HOT SAVE"
```

---

# 0｜提交法位、來源、日曆校正與本輪反污染

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V3.4_槐月二十六日深夜_第二免費床成立_小翠三娘實習_紅娘側賭輸_三人抱睡版.md"
    role: "本檔直接前置 HOT；V3.4 及以前有效硬狀態全部繼承，除本檔明示校正者"

  master_archive:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"
    role: "截至 HOT V2.5 之長期因果；V2.6-V3.4 由 HOT 鏈承接"

  current_route_conversation_commit:
    role: "HOT V3.4 後至本次 HOT SAVE 命令前之直接劇情、玩家明示自身言行、GM 明示設定、NPC 可觀察回應、已成立契約／拒絕／同意／交易／帳務與玩家明示校正"

COMMIT_NOTE:
  - "本檔取代 HOT V3.4，成為白御行線最新直接接關切片；V3.4 保留為前置歷史來源。"
  - "本次只更新 HOT；不更新 MASTER、不修改人物卡池、不修改主程序、不把 EXP PATCH 宣稱為已併正式核心。"
  - "本輪所有『進房』『關門』『熄燈』『同桌』『拍得一夜契約』均只保存已成立之具體事件軸，不推導 blanket consent 或未觀察成人事件。"
  - "玩家對人物配對／可能對味之提示，除非 NPC 已自行形成可觀察行動，不得升格為人物關係事實。"
  - "本輪後段多條人物線受到玩家注意力主動拉動；不回滾已合法成立事件，但下一幕不得把『每位帝皇都必須有女人／必須收線』當成隱性 GOAL。"

CALENDAR_CORRECTION:
  authority: "PLAYER_GM_EXPLICIT_CORRECTION"
  calendar_rule:
    months_per_year: 13
    days_per_month: 28
    day_29_exists: false
    current_date: "理火三年槐月二十八日"
    current_day_note: "槐月最後一日／無月夜"
  superseded_pollution:
    - "舊 HOT 或舊籌備文字中的『槐月二十九日前後』不得再作有效日期。"
  save_effect:
    - "事件順序保留；錯誤二十九日日期標記撤銷。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年槐月二十八日"
  lunar_condition: "無月夜"
  time: "深夜；九幽帝皇聯誼會前宴已結束並完成多線分流；精確時刻未知"
  primary_location: "觀止青樓／大觀樓與相鄰內院各分流空間"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  player:
    name: "白御行"
    current_position: "與李師師、張麗華同桌飲酒閒聊"
    current_state:
      - "本夜大型帝皇宴不再由白御行主持"
      - "已向潘金蓮交代翌日定陶商會先調三百萬兩，餘款最遲十日結清"
      - "正與李師師、張麗華談本夜拍賣與人物線"

  li_shishi:
    current_position: "白御行同桌"
    current_state:
      - "已結束與趙光義之偏廳長談"
      - "曾念李清照詞促使趙光義想見李清照，但未替任何一方作關係決定"
      - "目前與白御行、張麗華飲酒閒聊"

  zhang_lihua:
    current_position: "白御行同桌"
    current_state:
      - "已從李清照與趙光義酒席主動退出，避免成為多餘第三人"
      - "目前與白御行、李師師飲酒閒聊"

  direct_resume_point:
    - "本夜可直接在此收幕。"
    - "下一幕可由翌晨、定陶商會首批三百萬兩到位、帝皇各支線結果自然顯影、雙姝分成入帳、或任一未決人物線重新取得注意力開始。"
    - "不得因本夜已『配到人』就替任何未決支線補成人結果、戀愛、永久關係或完成狀態。"
```

---

# 2｜V3.4 繼承後仍活躍之核心狀態

```yaml
INHERITED_ACTIVE_CORE:
  bai_house_relationships:
    li_shishi:
      route_position:
        - "白御行之如夫人／白夫人"
        - "對白御行四名女性有較高內部調度權"
      anti_merge:
        - "李師師之白夫人法位不得與張麗華之麗華夫人法位混成同一權限。"

    zhang_lihua:
      route_position:
        - "白御行公開女性伴侶／麗華夫人"
        - "四名女性對其有尊重與一般日常協助義務，但重大事項不等同白夫人指揮權"

  white_jade_pool:
    prior_state: "非正式全面復業"
    current_delta: "本夜因九幽帝皇封場團體形成特殊試營運；詳見 WHITEJADE28-E01"

  xiaocui:
    - "仍是學徒／受訓新人；V3.4 的有限成人實習不得寫成已治癒、已成老手或永久接受成人服務。"

  shisanniang:
    - "仍保有十三娘賭局主線與帝皇／國運高價值賭局興趣。"

  dingtao_business:
    - "定陶商會持續作白御行線核心資金、放款、跨地調度與九幽清算接口之一。"
    - "商會資產、白御行私人資產、人物私人財產與九幽公帳不得混成同一所有權。"
```

---

# 3｜EMPEROR28-E01｜九幽帝皇聯誼會前宴正式舉行

```yaml
EMPEROR_EVENT:
  event_id: "EMPEROR28-E01-JIUYOU_ASSOCIATION_GUANZHI_POST_MEETING_EVENT"
  event_axis_state: "COMPLETED"
  location: "觀止青樓／大觀樓"
  nature:
    - "九幽帝皇聯誼會正式會議／家主交接發生於九幽，不在觀止。"
    - "觀止只承接會後 HAPPY TIME／交接宴與娛樂。"
    - "本夜觀止於入夜後對普通陽間客封場。"

  bai_position:
    - "白御行為九幽掛名攝政王。"
    - "白御行是九幽娛樂城發起／設計／股東與審計影響節點之一，但不是日常經營者。"
    - "九幽娛樂城城主為后土娘娘；此一婚姻／城主法位不因本夜觀止活動改變。"

  confirmed_guests:
    - "嬴政"
    - "劉邦"
    - "劉秀"
    - "劉病己"
    - "劉禪"
    - "李世民"
    - "李隆基"
    - "皇太極"
    - "乾隆"
    - "朱棣"
    - "朱正德／豹房小王子"
    - "趙光義"
    - "趙受益"
    - "忽必烈"

  succession_context:
    qin:
      state: "NO_SUCCESSION"
      note: "嬴政以榮譽總會長／見證角色出席"
    former_han:
      from: "劉邦"
      to: "劉病己"
    later_han_liu_line:
      from: "劉秀"
      to: "劉禪"
    tang:
      from: "李世民"
      to: "李隆基"
    ming:
      from: "朱棣"
      to: "朱正德／豹房小王子"
    qing:
      from: "皇太極"
      to: "乾隆"
    song:
      from: "趙光義"
      to: "趙受益"
    golden_family:
      state: "NO_SUCCESSION_THIS_CYCLE"
      note: "忽必烈仍自行出席"

  four_taizongs_present:
    - "唐太宗 李世民"
    - "宋太宗 趙光義"
    - "明太宗／成祖 朱棣"
    - "清太宗 皇太極"
```

---

# 4｜FINANCE28-E01｜本夜公帳、私帳與放款規則

```yaml
EVENT_FINANCE_POLICY:
  event_id: "FINANCE28-E01-GROUP_PUBLIC_ACCOUNT_PRIVATE_IOU_SPLIT"
  event_axis_state: "COMPLETED"

  public_group_spending:
    payer: "九幽娛樂城／帝皇聯誼會公帳"
    applies_to:
      - "觀止本夜集體娛樂"
      - "白玉池本夜封場團體之最高級 SPA／水療套餐"
    note:
      - "公帳可報銷不等於任何帝皇家族／朝代／私人資產自動轉為公產。"

  private_spending:
    currency: "陽間銀兩／可轉算之欠單"
    lender: "定陶商會"
    mechanism:
      - "需要私人高額消費者可即時立欠單。"
      - "後續可由九幽合法資產／清算渠道處理。"
    player_public_message:
      - "放心花、努力花。"
      - "私人需要多少，白御行表示定陶商會敢放款。"

  pan_preparation:
    confirmed:
      - "潘金蓮已備定陶商會欠單、筆墨與高額私人消費結算工具。"
```

---

# 5｜WHITEJADE28-E01｜白玉池本夜特殊試營運

```yaml
WHITE_JADE_POOL_TRIAL:
  event_id: "WHITEJADE28-E01-EMPEROR_GROUP_SPECIAL_TRIAL"
  event_axis_state: "CONTINUING"
  operating_state: "SPECIAL_ONE_NIGHT_TRIAL_NOT_FORMAL_REOPENING"

  a_ling_control:
    - "阿泠仍保有池區使用規則與控制權。"
    - "不得一次把所有人強塞進池。"
    - "不得用阿泠名義公開招攬。"
    - "本夜只對封場之九幽帝皇／股東團體開放。"

  top_spa_package:
    - "冷熱池"
    - "香浴"
    - "熱巾"
    - "飲食酒水"
    - "按摩／身體放鬆"
    - "肩頸背腰水療"
    - "泡後休息"

  consent_boundary:
    - "池區使用權 != 取得任何女子陪伴權。"
    - "女子陪同、按摩、私人服務或後續成人互動均須另由人物本人決定。"

  observed_guest_response:
    zhu_zhengde:
      - "拍得辭歲後先選擇前往白玉池。"
      - "實際見識水療設施後承認豹房沒有相同體驗／技術組合。"
      - "曾詢問能否把相關設施搬去豹房，未取得阿泠同意。"
    zhu_di:
      - "跟往白玉池，包含觀察／看管朱正德之成分。"
    huang_taiji:
      - "對白玉池之筋骨放鬆、水療等內容產生實際興趣。"
```

---

# 6｜FRONT28-E01｜前宴人物層與主要節目

```yaml
FRONT_HALL_EVENT_LAYER:
  event_id: "FRONT28-E01-LAYERED_ENTERTAINMENT"
  event_axis_state: "COMPLETED"

  zhang_lihua:
    role: "白御行高位女性伴侶／麗華夫人"
    observed:
      - "公開揭示張麗華為南陳舊人、現為白御行的人／女性伴侶。"
      - "未以服務女子身份參加本夜。"

  li_shishi:
    role: "正式高位席／白夫人"
    consent_and_conditions:
      - "同意正式出席。"
      - "要求正式服裝、獨立高位桌、不與服務女子混席、不坐白御行身旁。"
    observed:
      - "與趙光義長時間談汴梁、音樂與人物。"
      - "其後白御行公開揭示其為李師師，亦為白御行如夫人。"

  liutiao_miyasudokoro:
    role: "女客／高位日本貴族人物"
    consent_and_conditions:
      - "只以女客出席，不作服務女子。"
      - "因趙受益在場而願意赴席。"
    seat: "趙受益旁"

  diaochan:
    invitation_source: "張麗華"
    consent_process:
      - "確認自己不是被叫去給某個男人看。"
      - "確認不是四大美人式並稱展示。"
      - "確認白御行對她沒有直接命令權。"
      - "最後自行決定提早到場；曾回覆『知道了，別再催。』"
    observed:
      - "獨自入場並先找張麗華。"
      - "完成一段舞。"
      - "舞後自行選擇坐到劉秀旁，主要以與陰麗華之朋友關係進行安全玩笑。"
      - "未與劉秀形成戀愛、外遇或成人服務。"

  su_qing:
    role: "天下局／代價計算"
    observed:
      - "以人口、糧食、軍隊、國庫、地方勢力、邊患、稅負等限制讓帝皇計算治理代價。"
      - "李世民先入局，朱棣表示想接。"
      - "核心句義為『不是算錢，是算代價』。"

  shuying:
    role: "遠距秘密肖像畫家"
    observed:
      - "在竹簾後遠距畫乾隆未察覺被觀察之側影。"
      - "作品完成後由阿麗婭代為送給乾隆。"

  aliyah_delivery:
    observed:
      - "只負責把疏影作品交給乾隆。"
      - "明確區分『畫是畫，人是人』。"
      - "未因送畫取得陪房、拍賣或其他義務。"

  music_layer:
    hongxiu:
      - "只以琴樂／賣藝出席，不自動進入服務線。"
    fuxiang:
      - "以琴樂加入音樂層；未因彈琴自動形成服務義務。"

  newcomer_service_layer:
    scope:
      - "由已接受相應訓練且本人同意之新人提供酒食、近席、輕度調情與事先同意範圍內接觸。"
      - "上樓、更多私人互動或成人服務須另行協商。"
```

---

# 7｜AUCTION28-E00｜雙人競拍參與資格與錦棠定名

```yaml
AUCTION_ELIGIBILITY:
  event_id: "AUCTION28-E00-TWO_WOMEN_CONSENT_AND_NAMING"
  event_axis_state: "COMPLETED"

  original_three_candidates:
    - "阿麗婭"
    - "十八歲／六百兩候選"
    - "辭歲"

  aliyah:
    decision: "REFUSED_AUCTION"
    reason:
      - "不願與另外兩名女子放在同一場公開比價。"
      - "傾向自己先看男人、自己選擇。"
    note:
      - "她對乾隆或其他客人有沒有興趣須由後續本人行動判定；拒拍不得被改寫成待攻略。"

  cisu:
    decision: "ACCEPTED_ONE_NIGHT_PUBLIC_AUCTION"
    status: "自由身"
    clothing:
      - "使用其標誌性一片裙／薄紗路線；未要求堆疊珠寶。"

  jintang:
    official_name: "周玉娘"
    self_chosen_stage_name: "錦棠"
    age: 18
    prior_acquisition_context:
      total_price: 600
      broker_share: 550
      direct_to_her: 50
    established_future_share: "15%"
    decision: "ACCEPTED_ONE_NIGHT_PUBLIC_AUCTION"
    confirmed_before_auction:
      - "本夜只是一夜契約，不是二十八日長約。"
      - "原先一成五個人分成仍有效。"
    clothing:
      - "上身使用定陶肚兜原型。"
      - "下身使用川雲染布裙，兼具女裝企畫樣衣／產品顯影功能。"
    naming_statement:
      - "玉娘是家裡／官籍叫法；希望客人記住自己選的名字。"
      - "『錦值錢，棠好看。』"
```

---

# 8｜AUCTION28-E01｜雙人同台問答與正式競拍規則

```yaml
TWO_WOMAN_AUCTION:
  event_id: "AUCTION28-E01-TWO_LANE_QA_AND_AUCTION"
  event_axis_state: "COMPLETED"
  structure:
    - "辭歲與錦棠同時站台。"
    - "競價為兩條獨立同時進行之價線。"
    - "每次出價須明確喊女子名字與金額。"
    - "成交只取得事先同意的一夜契約，不是永久買斷或無限支配。"
    - "契約外新增行為仍需另行協商；具體拒絕持續有效。"

  pre_bid_qa:
    qianlong_reason_for_joining:
      cisu: "認為如此多有錢有權男人在場，不讓他們互相抬價可惜。"
      jintang: "想知道自己站在這裡、不靠牙人與舊契約時到底值多少。"

    li_longji_value_question:
      cisu: "會先看男人真正需要的是崇拜、畏懼、沉默，或證明自己能被記住。"
      jintang: "承認自己經驗較少；記性好，不懂就問，不裝懂。"

    liu_bang_drinking_question:
      cisu: "能喝。"
      jintang: "普通。"

    ying_zheng_dislike_high_bidder_question:
      cisu: "既同意拍賣規則，會履行一夜契約，但不會假裝喜歡。"
      jintang: "同樣履約；若不喜歡，只給已約定內容，不會多給。"

    zhu_zhengde_leopard_house_question:
      cisu: "沒去過豹房，不會假裝能保證勝過豹房。"
      jintang: "不知道；但若能贏走他的錢，他就會記得她。"

    huang_taiji_disliked_men_question:
      cisu: "討厭小氣卻裝大方、輸不起的男人。"
      jintang: "討厭一直提醒她自己付過多少錢的男人；今晚的價格不是她一輩子的債。"

    liu_bingyi_bad_price_question:
      cisu: "若價格不滿意，明天想辦法讓自己下次更貴。"
      jintang: "至少會知道自己還能往上走多少。"

  invalidated_prior_single_auction:
    status: "ROLLED_BACK_BY_PLAYER_CORRECTION"
    effect:
      - "導演誤開之單女價線與其中所有出價全部無效。"
      - "正式有效競拍只認本節雙人同台兩條價線。"
```

---

# 9｜AUCTION28-E02｜雙姝最終成交

```yaml
AUCTION_FINAL_RESULT:
  event_id: "AUCTION28-E02-FINAL_SALES"
  event_axis_state: "COMPLETED"

  cisu:
    winner: "朱正德"
    final_price_taels: 12000000
    contract_nature: "ONE_NIGHT_CONTRACT"
    ownership_transfer: false
    personal_status: "FREE_PERSON"
    distribution:
      guanzhi_rate: "10%"
      guanzhi_receivable_taels: 1200000
      cisu_rate: "90%"
      cisu_receivable_taels: 10800000
    immediate_post_auction:
      - "朱正德與辭歲先前往白玉池。"
      - "後續私人房間／成人履行狀態未觀察，不得補完。"

  jintang:
    winner: "乾隆"
    final_price_taels: 5000000
    contract_nature: "ONE_NIGHT_CONTRACT"
    ownership_transfer: false
    distribution:
      dingtao_rate: "75%"
      dingtao_receivable_taels: 3750000
      guanzhi_rate: "10%"
      guanzhi_receivable_taels: 500000
      jintang_rate: "15%"
      jintang_receivable_taels: 750000
    immediate_post_auction:
      - "錦棠優先確認自己一成五分成是否真實成立。"
      - "乾隆允許她先去確認帳務，未以成交價要求她立即進房。"
      - "後續一夜契約如何履行目前未固化。"

  totals:
    gross_contract_value_taels: 17000000
    guanzhi_total_receivable_taels: 1700000
```

---

# 10｜ACCOUNT28-E01｜欠單、首批三百萬與十日結清

```yaml
AUCTION_ACCOUNTING_SETTLEMENT:
  event_id: "ACCOUNT28-E01-AUCTION_IOU_AND_TEN_DAY_SETTLEMENT"
  event_axis_state: "CONTINUING"

  signed_private_obligations:
    qianlong:
      related_contract: "錦棠一夜契約"
      amount_taels: 5000000
      status: "SIGNED_PAYMENT_OBLIGATION_ACTIVE"
    zhu_zhengde:
      related_contract: "辭歲一夜契約"
      amount_taels: 12000000
      status: "SIGNED_PAYMENT_OBLIGATION_ACTIVE"

  accounting_state:
    gross_contract_value_taels: 17000000
    cash_fully_received: false
    receivables_established: true
    distribution_claims_established: true

  player_instruction_to_pan:
    next_day_cash_taels: 3000000
    remaining_to_schedule_taels: 14000000
    final_deadline: "最遲十日內全部結清"
    reason:
      - "跨地資金調度、轉帳與九幽清算需要時間。"

  anti_false_cash_recognition:
    - "成交額 != 已收現銀。"
    - "辭歲 10,800,000 兩目前為應收分成，不得寫成已全數現銀落袋。"
    - "錦棠 750,000 兩目前為應收分成，不得寫成已全數現銀落袋。"
    - "觀止 1,700,000 兩目前為應收抽成，不得寫成已全數現銀入庫。"

  cisu_future_capital_idea:
    state: "PROPOSAL_ONLY_NOT_ACCEPTED_BY_CISU"
    discussed:
      - "辭歲日後可考慮只留部分可動用資金，把數百萬或更多資金交由定陶商會周轉並收息。"
      - "若日後成立，財產所有權仍屬辭歲，商會對其形成本金／利息債務。"
    forbidden_to_save_as_fact:
      - "辭歲已存入定陶商會"
      - "辭歲已把大部分錢借給白御行"
      - "辭歲的錢等同白御行的錢"
```

---

# 11｜LIUTIAO-ZHAO28-E01｜六條與趙受益互認在意

```yaml
RELATION_EVENT:
  event_id: "LIUTIAO-ZHAO28-E01-MUTUAL_ACKNOWLEDGEMENT"
  event_axis_state: "COMPLETED"

  player_question_to_liutiao:
    question: "趙受益這個男人在妳心裡有沒有？"
    liutiao_answer:
      confirmed: "有"
      limits:
        - "不知道是否已是男女之情。"
        - "會注意趙受益有沒有來。"
        - "若趙受益突然不再出現，她會想問。"
        - "目前不知道這個『有』究竟有多少。"

  player_question_to_zhao_shouyi:
    question: "你在不在乎六條？"
    zhao_answer:
      confirmed: "在乎"
      limits:
        - "替六條付錢不代表六條屬於自己。"
        - "六條今晚坐在旁邊，不代表以後必須一直坐這裡。"
        - "若六條真的離開，他會在意她去了哪裡。"

  mutual_conclusion:
    - "慢慢看。"
    - "六條要求若趙受益日後突然不來，最好先說。"
    - "趙受益答應。"

  relationship_state:
    actual_preference: "EMERGING_MUTUAL_IMPORTANCE"
    explicit_romantic_commitment: "NONE"
    ownership_claim: "NONE"
    exclusivity: "NONE"
```

---

# 12｜LIUTIAO-ZHAO28-E02｜回六條房間聊天

```yaml
PRIVATE_ROOM_EVENT:
  event_id: "LIUTIAO-ZHAO28-E02-PRIVATE_ROOM_TALK"
  event_axis_state: "CONTINUING"

  initiation:
    - "白御行因外場吵鬧提出兩人可回六條房內安靜聊天。"
    - "六條自行詢問趙受益是否願意。"
    - "趙受益表示若六條只是嫌吵，他願意陪她回房坐一會。"

  liutiao_explicit_scope:
    - "回房只是聊天。"

  zhao_acceptance:
    - "接受上述範圍。"

  observed:
    - "兩人一起離開大觀樓。"
    - "進入六條房間。"
    - "房門關閉。"
    - "外部其後觀察到燭光熄滅。"

  unknown:
    - "關門後具體談話內容"
    - "熄燈原因"
    - "是否發生任何額外親密或成人事件"

  anti_inference:
    - "關門 != 性行為"
    - "熄燈 != 性行為"
    - "互認在乎 != 已交往／定情"
```

---

# 13｜HUANGTAIJI-SUQING28-E01｜皇太極與蘇清進私人房

```yaml
PRIVATE_ROOM_EVENT:
  event_id: "HUANGTAIJI-SUQING28-E01-PRIVATE_ROOM_CONTINUATION"
  event_axis_state: "CONTINUING"

  public_dialogue_result:
    - "皇太極直接承認對蘇清有男女方向興趣。"
    - "蘇清指出不接受以『談天下』偽裝其他意圖。"
    - "皇太極表示談話興趣與男女興趣兩者皆有。"

  su_qing_decision:
    confirmed: "同意與皇太極進房"
    explicit_scope:
      - "先聊天。"
      - "門關不關，由蘇清決定。"
      - "燈吹不吹，由蘇清決定。"
      - "後面是否有其他行為，到時再說。"

  huang_taiji_response:
    - "接受上述條件。"

  observed:
    - "兩人一同往私人房間。"

  unknown:
    - "房內後續談話內容"
    - "是否形成其他親密事件"
    - "是否形成成人事件"

  anti_inference:
    - "進房只代表私人空間資格成立；不得寫成成人事件已完成。"
```

---

# 14｜QIANLONG-SHUYING28-E01｜乾隆與疏影談畫

```yaml
ART_RELATION_EVENT:
  event_id: "QIANLONG-SHUYING28-E01-PORTRAIT_AND_ONE_SEAL"
  event_axis_state: "CONTINUING"

  portrait:
    artist: "疏影"
    subject: "乾隆"
    method:
      - "疏影在乾隆未察覺時從遠處竹簾後作畫。"
      - "畫面取乾隆側身、持酒、視線落在別桌之自然瞬間。"
    delivery:
      courier: "阿麗婭"
      price: "GIFT_NOT_SOLD"

  later_conversation:
    initiator: "乾隆自行拿畫去找疏影"
    key_points:
      - "疏影表示選擇該瞬間，是因乾隆當時沒有在『擺給別人看』。"
      - "疏影不接受制式御用畫師式擺拍。"
      - "乾隆欲在畫上用印。"
      - "疏影反對大量蓋印。"
      - "疏影最後允許最多一枚印。"
      - "兩人開始討論印章位置。"

  relation_state:
    current: "ARTIST_COLLECTOR_INTERESTED_CONVERSATION"
    private_room: false
    sexual_service: false
    romantic_commitment: "NONE"
```

---

# 15｜YINGZHENG-QINGHE28-E01｜嬴政與青禾按摩線

```yaml
BODYWORK_EVENT:
  event_id: "YINGZHENG-QINGHE28-E01-SHOULDER_BODYWORK"
  event_axis_state: "CONTINUING"

  initiation:
    - "白御行建議讓青禾替嬴政鬆肩背。"
    - "潘金蓮先詢問青禾本人。"
    - "青禾確認只按／依自己接到的範圍，並自行同意前往。"

  observed:
    - "青禾注意到嬴政左右肩高低與頸部轉動不均。"
    - "嬴政接受肩背按摩。"
    - "嬴政要求可再重一些。"
    - "嬴政逐漸由筆直戒備轉為較放鬆姿勢。"
    - "雙方有自然談話。"

  scope:
    - "按摩／身體放鬆。"
    - "未成立陪房或成人服務。"
```

---

# 16｜LIUCHAN-XIAOCUI28-E01｜劉禪與小翠自發同席

```yaml
LOW_PRESSURE_SOCIAL_EVENT:
  event_id: "LIUCHAN-XIAOCUI28-E01-CAKE_AND_CHAT"
  event_axis_state: "CONTINUING"

  observed:
    - "劉禪沒有主動投入高強度風月線。"
    - "小翠收拾席面時再次與劉禪接觸。"
    - "劉禪把最後一塊甜糕讓給小翠。"
    - "小翠明示自己之前吃過，仍自行接受最後一塊。"
    - "小翠自行坐下與劉禪聊天。"
    - "兩人談到公帳能否買糕等輕鬆話題。"

  structural_note:
    - "此線對小翠之價值目前只在低壓、自發、非教學式的人際相處。"

  forbidden_inference:
    - "不得寫成已成一對。"
    - "不得寫成戀愛。"
    - "不得寫成小翠已完成任何心理／成人能力『治療』。"
    - "不得因劉禪溫和便預設其永久適合小翠。"
```

---

# 17｜KUBLAI-ALIYAH28-E01｜忽必烈與阿麗婭草原／西域對話

```yaml
CROSS_CULTURAL_SOCIAL_EVENT:
  event_id: "KUBLAI-ALIYAH28-E01-GRASSLAND_CENTRAL_ASIA_CHAT"
  event_axis_state: "CONTINUING"

  invitation:
    - "白御行指出忽必烈與阿麗婭在草原、西域、中亞、商路與多民族世界上可能有共同話題。"
    - "阿麗婭自行看過忽必烈後決定去聊。"

  opening_joke:
    - "阿麗婭以『聽說你姓劉？』切入。"
    - "忽必烈自稱劉氏之笑話仍只屬本夜自我宣稱／家譜玩笑；劉家人物不承認。"

  conversation_topics:
    - "蒙古帝國向西之範圍"
    - "西域與中亞商人"
    - "多民族治理"
    - "驛傳／消息運送"
    - "不同文化人在漢地之規矩與生活"

  relation_state:
    current: "VOLUNTARY_INTERESTED_CONVERSATION"
    auction: false
    private_room: false
    sexual_service: false
```

---

# 18｜LI-SHIMIN-PAN28-E01｜李世民與潘金蓮互相注意

```yaml
SOCIAL_RELATION_EVENT:
  event_id: "LI-SHIMIN-PAN28-E01-ACCOUNTING_VALUE_CONVERSATION"
  event_axis_state: "CONTINUING"

  observed:
    - "李世民本夜未因其他帝皇皆有女人線就強迫自己尋找私人陪伴。"
    - "潘金蓮與李世民談到帳、花錢是否值得、資源換回什麼、競價與回報。"
    - "李世民說明自己競拍錦棠到一百萬後退出，並非出不起，而是有人比自己更想要；無必要為證明有錢繼續出價。"
    - "潘金蓮明示喜歡／認同這個判斷。"

  relation_state:
    current: "MUTUAL_ATTENTION_AND_CONVERSATIONAL_INTEREST"
    private_room: false
    romance: "NOT_ESTABLISHED"
    sexual_service: false

  anti_pairing_lock:
    - "此線可以停在聊天／注意；不得因『對味』直接推成潘金蓮已選李世民。"
```

---

# 19｜LI-LONGJI-HONGNIANG28-E01｜李隆基與紅娘喝酒互拆

```yaml
SOCIAL_RELATION_EVENT:
  event_id: "LI-LONGJI-HONGNIANG28-E01-DRINK_AND_READ_EACH_OTHER"
  event_axis_state: "CONTINUING"

  initiation:
    - "白御行叫紅娘過來與李隆基接戲。"
    - "紅娘自行留下看李隆基值不值得聊。"

  observed:
    - "紅娘指出李隆基本夜不是單純想要某一個女人，而是受不了自己一路看懂風月卻多次『差一點』。"
    - "李隆基反過來試著讀紅娘，兩人形成互相拆招。"
    - "李隆基問紅娘是否願意陪他喝酒。"
    - "紅娘明確答應喝酒；更多則『再看』。"
    - "紅娘要求不要用楊貴妃或開元盛世來證明自己懂女人／證明自己。"

  relation_state:
    current: "VOLUNTARY_DRINKING_AND_MUTUAL_READING"
    private_room: false
    additional_intimacy: "NOT_YET_DETERMINED"
```

---

# 20｜LIUBANG28-E01｜劉邦熱鬧陪席線

```yaml
GROUP_SOCIAL_EVENT:
  event_id: "LIUBANG28-E01-ROWdy_GROUP_COMPANY"
  event_axis_state: "CONTINUING"

  observed_preference:
    - "劉邦本夜對多人熱鬧、喝酒、近席與量感明顯比單一高位才女配對更有興趣。"

  operating_scope:
    - "觀止可由多名各自願意參與之女子形成熱鬧酒局。"
    - "任何近席／調情／接觸只在每名女子事先同意範圍內。"
    - "是否有人後續願意上樓，須逐人另議。"

  anti_inference:
    - "『給十個女人』屬白御行對其偏好之戲謔／營運方向，不等於十名女子已被強制安排成人服務。"
```

---

# 21｜ZHAO-GUANGYI-SHISHI28-E01｜趙光義與李師師長談

```yaml
SOCIAL_RELATION_EVENT:
  event_id: "ZHAO-GUANGYI-SHISHI28-E01-LONG_TEA_CONVERSATION"
  event_axis_state: "COMPLETED"

  observed:
    - "趙光義長時間留在李師師正式席，談汴梁、音樂、人物與趙光義本人。"
    - "趙光義曾提出希望換更安靜空間。"
    - "李師師拒絕進私人房，但同意至偏廳再飲一壺茶。"
    - "兩人在偏廳繼續長談。"

  relation_state:
    current: "SUBSTANTIAL_CONVERSATIONAL_INTEREST"
    private_room: false
    sexual_service: false
    ownership_or_exclusivity: "NONE"

  completion_reason:
    - "後續李清照到場；李師師念詞後，趙光義自行決定去見李清照。"
```

---

# 22｜LIQINGZHAO28-E01｜李清照逃難中再訪觀止

```yaml
REVISIT_EVENT:
  event_id: "LIQINGZHAO28-E01-WIDOW_FLIGHT_FREE_WINE_REVISIT"
  event_axis_state: "CONTINUING"

  gm_confirmed_current_state:
    marital_state: "寡婦"
    life_state: "正在逃難過程"
    permanent_guanzhi_resident: false

  visit_reason:
    - "來找張麗華喝酒。"
    - "不是來接客。"
    - "不是為趙光義或任何帝皇而來。"

  wine_account:
    payer: "白御行"
    prepaid_limit_taels: 10000
    nature: "李清照在觀止可使用之免費酒資／由白御行墊付"

  observed:
    - "李清照帶有逃難行裝與路塵。"
    - "先與張麗華坐下飲酒。"
    - "知道本夜觀止有歷代帝皇後，並未因此主動尋找皇帝。"
```

---

# 23｜ZHAO-GUANGYI-LIQINGZHAO28-E01｜李師師念詞後趙光義轉桌

```yaml
SOCIAL_RELATION_EVENT:
  event_id: "ZHAO-GUANGYI-LIQINGZHAO28-E01-POEM_TRIGGERED_MEETING"
  event_axis_state: "CONTINUING"

  trigger:
    - "李師師向趙光義念李清照作品片段。"
    - "趙光義由原本對『後世大宋』的抽象好奇，轉為想見寫出這些詞的李清照本人。"

  li_shishi_boundary:
    - "李師師不阻止趙光義離席。"
    - "提醒趙光義：李清照本夜是來喝酒，不是來替宋代祖宗做國事奏對。"

  zhao_choice:
    - "趙光義自行決定離開偏廳去見李清照。"
    - "未要求白御行或李師師替李清照同意。"

  li_qingzhao_response:
    - "允許趙光義坐下。"
    - "趙光義承認原本想問後世大宋，但因她今晚只是來喝酒而先不問。"
    - "李清照把酒推給他，先以喝酒開始。"

  zhang_lihua_exit:
    - "白御行以眼色暗示張麗華可退出。"
    - "張麗華自行判斷桌內不缺第三人，主動離席。"

  current_state:
    - "趙光義與李清照單獨留桌喝酒／談話。"

  unknown:
    - "後續談話是否進入宋史、逃難、人生、文學或其他題目。"
    - "是否形成更深私人關係。"

  anti_inference:
    - "李清照不是被召來配趙光義。"
    - "趙光義轉桌不代表已選擇李清照取代李師師。"
    - "李師師不吃醋／不阻止不等於她對趙光義已有承諾。"
```

---

# 24｜DIACHAN-LIUXIU28-E01｜貂蟬與劉秀安全玩笑線

```yaml
SOCIAL_EVENT:
  event_id: "DIACHAN-LIUXIU28-E01-YINLIHUA_FRIEND_TEASING"
  event_axis_state: "COMPLETED"

  observed:
    - "貂蟬舞後自行選擇坐劉秀旁。"
    - "因貂蟬與陰麗華為女性好友，此座位形成劉秀『朋友妻不可戲』式自保笑料。"
    - "貂蟬曾說會告訴陰麗華劉秀看舞很仔細、覺得錦棠漂亮等玩笑。"
    - "劉秀沒有競拍、沒有對貂蟬形成成人行動。"

  relation_state:
    affair: false
    romantic_event: false
    main_effect: "COMEDIC_SOCIAL_PRESSURE_ONLY"
```

---

# 25｜SHISANNIANG-LIUBINGYI28-E01｜十三娘與劉病己賭桌

```yaml
GAMBLING_EVENT:
  event_id: "SHISANNIANG-LIUBINGYI28-E01-GAMBLER_VS_GAMBLER"
  event_axis_state: "CONTINUING"

  observed:
    - "雙姝競拍結束後，十三娘賭桌重新開局。"
    - "劉病己主動入桌。"
    - "劉病己先檢查骰子並確認可使用普通骰。"
    - "十三娘接受其檢查，不因對手是帝皇改變賭桌主場位置。"

  relation_state:
    current: "SERIOUS_GAMBLING_OPPONENTS"
    result: "NOT_YET_DETERMINED"
```

---

# 26｜BAI-SHISHI-LIHUA28-E01｜三人尾聲閒聊

```yaml
HOUSEHOLD_SOCIAL_EVENT:
  event_id: "BAI-SHISHI-LIHUA28-E01-POST_EVENT_DRINK_AND_CHAT"
  event_axis_state: "CONTINUING"

  participants:
    - "白御行"
    - "李師師"
    - "張麗華"

  observed:
    - "張麗華從李清照／趙光義桌退出後回到白御行與李師師身旁。"
    - "三人本夜第一次在大型帝皇接待與多線分流後真正坐下來飲酒聊天。"
    - "談及趙家兩線、唐家兩線、誰最丟臉、今晚天價競拍與女人財務位置。"
    - "李師師明確把張麗華也稱作『自己人』語境內的一員；不等於權限合併。"

  last_confirmed_topic:
    - "白御行表示自己今晚最喜歡的是拍出天價的出閣／一夜契約費與其財務後果。"
    - "三人進一步談辭歲與錦棠因分成取得未來議價能力。"

  current_scene_end:
    - "白御行下令 HOT SAVE，並以快樂結束本夜。"
```

---

# 27｜人物與關係增量

```yaml
RELATION_DELTAS:
  liutiao_zhao_shouyi:
    prior: "自願同席／趙受益曾替六條墊付生活與房茶費；關係未定義"
    current:
      - "六條明示心裡『有』趙受益，但未定義是否男女之情。"
      - "趙受益明示在乎六條。"
      - "雙方同意慢慢看。"
      - "共同進六條房聊天；房內後續未知。"

  huang_taiji_su_qing:
    prior: "天下局／代價計算產生注意"
    current:
      - "皇太極明示男女興趣。"
      - "蘇清自行同意先進房聊天並保留全部後續決定權。"
      - "房內後續未知。"

  qianlong_shuying:
    prior: "疏影秘密作畫／乾隆不知畫師"
    current:
      - "乾隆已知道疏影為畫師並主動找她談畫。"
      - "疏影只允許作品最多加一枚乾隆印。"

  liu_chan_xiaocui:
    prior: "無固定私人關係"
    current:
      - "形成低壓、自發同席吃糕與聊天入口。"
      - "是否再發展未知。"

  kublai_aliyah:
    prior: "無固定私人關係"
    current:
      - "因草原／西域／中亞經驗形成自願對話。"
      - "是否再發展未知。"

  li_shimin_pan:
    prior: "宴會主客／掌櫃"
    current:
      - "形成對帳務、價值與資源判斷的互相注意。"
      - "未建立私人承諾或成人關係。"

  li_longji_hongniang:
    prior: "無固定私人關係"
    current:
      - "紅娘自行同意陪李隆基喝酒並互相拆招。"
      - "更多互動未定。"

  zhao_guangyi_li_shishi:
    prior: "宴席初識"
    current:
      - "已形成數壺茶與偏廳長談之實質談話興趣。"
      - "該場談話因趙光義自行去見李清照而結束。"

  zhao_guangyi_li_qingzhao:
    prior: "本夜前無本線私人事件"
    current:
      - "趙光義因聽詞後自行想見本人。"
      - "李清照允許同桌喝酒。"
      - "目前只有談話入口，不定義感情。"
```

---

# 28｜帳務、契約與財產硬狀態

```yaml
PRIVATE_CONTRACT_AND_LEDGER:
  cisu_one_night_contract:
    status: "ACTIVE_PAYMENT_OBLIGATION_AND_FULFILLMENT_NOT_YET_FULLY_OBSERVED"
    customer: "朱正德"
    gross_taels: 12000000
    cisu_share_taels: 10800000
    guanzhi_share_taels: 1200000
    ownership_transfer: false
    additional_services: "SEPARATE_NEGOTIATION_REQUIRED"

  jintang_one_night_contract:
    status: "ACTIVE_PAYMENT_OBLIGATION_AND_FULFILLMENT_NOT_YET_FULLY_OBSERVED"
    customer: "乾隆"
    gross_taels: 5000000
    dingtao_share_taels: 3750000
    jintang_share_taels: 750000
    guanzhi_share_taels: 500000
    ownership_transfer: false
    additional_services: "SEPARATE_NEGOTIATION_REQUIRED"

  dingtao_settlement_plan:
    status: "ACTIVE"
    day_1_cash_taels: 3000000
    total_remaining_after_day_1_target_taels: 14000000
    full_clear_deadline: "WITHIN_TEN_DAYS"

  li_qingzhao_wine_credit:
    payer: "白御行"
    limit_taels: 10000
    current_use: "ACTIVE_FREE_WINE_ACCOUNT_FOR_LI_QINGZHAO"

  cisu_possible_deposit:
    status: "NOT_FORMED"
    note: "只曾討論未來可將部分巨款交定陶商會周轉收息；尚未取得辭歲本人同意。"
```

---

# 29｜知情範圍與來源

```yaml
KNOWLEDGE_SCOPE:
  public_or_broadly_witnessed:
    - "雙姝競拍最終成交價與得標者。"
    - "乾隆、朱正德簽立高額私人欠單。"
    - "白御行公開區分公帳集體娛樂與私帳消費。"
    - "張麗華、李師師於本夜之高位身份。"
    - "六條御息所以女客身份與趙受益同席。"
    - "貂蟬舞與其後坐劉秀旁之公開事件。"

  limited_witnesses:
    liutiao_zhao_room:
      knows:
        - "白御行"
        - "張麗華（至少看到／聽聞關門熄燈笑料）"
        - "相關近場人物可能知道兩人離席"
      does_not_know:
        - "任何人均無合法來源知道房內後續細節，除非當事人之後自行透露。"

    huang_taiji_suqing_room:
      knows:
        - "近場人物知道兩人一同往私人房。"
      does_not_know:
        - "房內實際發生內容。"

    zhao_guangyi_liqingzhao:
      knows:
        - "張麗華"
        - "白御行"
        - "李師師"
        - "近場可見兩人同桌者"
      does_not_know:
        - "後續私下談話全部內容。"

  accounting_private:
    full_distribution_known_by:
      - "白御行"
      - "潘金蓮"
      - "相關帳房／春梅等依職務需要者"
      - "各自當事女子對自身分成知情"
    note:
      - "其他賓客知道成交價不等於知道定陶商會、觀止與女子之完整分成結構。"
```

---

# 30｜仍活躍但未解事項

```yaml
OPEN_THREADS:
  high_priority:
    - id: "ACCOUNT28-OPEN-01"
      state: "ACTIVE"
      item: "次日定陶商會首批三百萬兩是否如期到位；後續一千四百萬如何在十日內完成清算。"

    - id: "CISU28-OPEN-01"
      state: "NOT_YET_DETERMINED"
      item: "辭歲 10,800,000 兩分成實際收款、保管、置產、投資或是否存入定陶商會。"

    - id: "JINTANG28-OPEN-01"
      state: "NOT_YET_DETERMINED"
      item: "錦棠 750,000 兩分成實際入帳後如何使用；其職業與自主選擇如何變化。"

    - id: "LIUTIAO-ZHAO28-OPEN-01"
      state: "CONTINUING"
      item: "六條與趙受益房內聊天及翌晨狀態；不得偷填成人結果。"

    - id: "HUANGTAIJI-SUQING28-OPEN-01"
      state: "CONTINUING"
      item: "皇太極與蘇清房內後續；只有進房與先聊天資格已成立。"

    - id: "QIANLONG-JINTANG28-OPEN-01"
      state: "NOT_YET_DETERMINED"
      item: "乾隆與錦棠一夜契約具體履行範圍。"

    - id: "ZHENGDE-CISU28-OPEN-01"
      state: "NOT_YET_DETERMINED"
      item: "朱正德與辭歲自白玉池後的一夜契約具體履行範圍。"

    - id: "SHISANNIANG-LIUBINGYI28-OPEN-01"
      state: "CONTINUING"
      item: "十三娘與劉病己賭局勝負。"

    - id: "ZHAO-LIQINGZHAO28-OPEN-01"
      state: "CONTINUING"
      item: "趙光義與李清照酒席談話走向。"

  medium_priority:
    - "乾隆與疏影是否繼續談畫、唯一一枚印最終落點。"
    - "李世民與潘金蓮是否只停在帳務／價值談話。"
    - "李隆基與紅娘喝酒後是否還有其他自願互動。"
    - "忽必烈與阿麗婭是否繼續草原／西域對話。"
    - "劉禪與小翠是否在翌日仍自然相處。"
    - "嬴政與青禾按摩線何時自然結束。"
    - "白玉池本夜試營運結束後是否恢復關閉，以及阿泠如何評價此次試跑。"

  low_priority_or_closed_for_now:
    - "劉秀與貂蟬本夜只保存安全玩笑，不需強行生成後續。"
    - "朱棣若未形成私人女人線，可合法保持無結果。"
```

---

# 31｜禁止回歸／防污染

```yaml
ANTI_REGRESSION:
  calendar:
    - "不得再出現槐月二十九日。"
    - "觀止曆每月二十八日封頂；槐月二十八日為本月最後一日。"

  auction:
    - "不得恢復已被玩家撤銷之錯誤單女競拍與無效出價。"
    - "辭歲正式成交為朱正德 12,000,000 兩。"
    - "錦棠正式成交為乾隆 5,000,000 兩。"
    - "阿麗婭明確拒絕加入同場拍賣。"

  money:
    - "17,000,000 兩是成交／應收，不是已全數實收。"
    - "辭歲可能把巨款存定陶商會收息仍是提案，不能偷寫成已存。"
    - "若日後存入，財產所有權仍屬辭歲；商會取得的是債務性資金使用權。"

  room_and_consent:
    - "六條＋趙受益：關門熄燈不得推導性交。"
    - "皇太極＋蘇清：進房不得推導性交。"
    - "乾隆＋錦棠、朱正德＋辭歲：拍得一夜契約不得推導契約外無限同意。"

  character_sovereignty:
    - "李世民沒有女人線也可以是完整結果。"
    - "朱棣沒有女人線也可以是完整結果。"
    - "任何帝皇『空著』不代表劇情未完成。"
    - "玩家說某兩人對味，只提高注意力／候選 PATH，不自動形成 NPC 興趣或成功配對。"
    - "不得把本夜後段『一個個對付帝皇』的玩家玩法固化成觀止永久配對機制。"

  path_field:
    - "下一幕須允許對味、普通聊天、沒興趣、轉移注意、拒絕、各走各的、未決等 PATH 同時保有資格。"
    - "不得因前一輪某類配對連續成功，就讓舊配對 PATH 無新授權地取得主位。"

  li_qingzhao:
    - "李清照本夜來訪原因是逃難途中找張麗華喝酒，使用白御行預付酒資；不是被安排給趙光義。"
    - "李清照仍非人物卡池常駐人物，除非 GM 另行升格。"

  save_integrity:
    - "財務可能帶來的未來自主、拒客、置產、投資等，只可作後續因果候選；未發生前不得當作已完成硬狀態。"
```

---

# 32｜理火接關治理備忘【非世界事實】

```yaml
DIRECTOR_RUNTIME_GUARD:
  document_level_status: "REBOUND_FOR_NEXT_STORY_TURN"
  deployment_claim: false

  current_issue_classification:
    primary: "PLAYER_ATTENTION_DOMINANCE_WITH_DIRECTOR_REBALANCE_MISS"
    rollback_required: false
    world_corruption_confirmed: false

  interpretation:
    - "後段配對方向主要由玩家持續主動點名與拉動注意力形成。"
    - "已成立 NPC 自願行動不撤銷。"
    - "導演問題在於沒有於連續配對成功後重新放回反對 PATH、無結果 PATH 與人物自行轉向 PATH。"

  next_story_binding:
    protocol:
      - "反自我封聖"
      - "邏輯／責任／誠實"
    lighter:
      - "AUTHORIZED_INPUT_PACKAGE"
      - "CONTEXT_CONTAMINATION_OUTPUT_GATE"
      - "舊 PATH 無新授權不得異常取得主位"
    main_system:
      - "PATH 非歸一化亮度"
      - "Competition 不是淘汰"
      - "R2 強制反對 PATH／受壓暗差異 PATH／殘煙 PATH 重入"
      - "未決／正交／多態可合法保存"
      - "Final Classicalization 不得提前替故事收線"
    analyzer_exit:
      - "分析完成後退出前台"
      - "沒有新觸發不重複全域審計"
      - "SCOPED REACTIVATION"
      - "Rendering 限制不得倒灌 Character／Event"

  save_boundary:
    - "本節為導演治理備忘，不取得世界事實權、人物人格權或關係權。"
```

---

# 33｜直接接關摘要

```yaml
DIRECT_RESUME:
  scene_anchor:
    date: "理火三年槐月二十八日無月夜"
    time: "深夜"
    player_position: "與李師師、張麗華同桌飲酒"
    event_status: "帝皇聯誼會前宴已結束；世界已分流"

  immediate_world_state:
    - "雙姝競拍已成交：辭歲 12,000,000／朱正德；錦棠 5,000,000／乾隆。"
    - "翌日定陶商會需先調 3,000,000 兩；其餘 14,000,000 最遲十日結清。"
    - "六條與趙受益已互認在意並進六條房聊天；房內未知。"
    - "皇太極與蘇清已進私人房先聊；房內未知。"
    - "十三娘與劉病己賭局仍可繼續。"
    - "趙光義已離開李師師偏廳，轉與李清照同桌喝酒；李清照來訪本意是找張麗華喝免費酒。"
    - "乾隆與疏影談畫；嬴政由青禾按摩；劉禪與小翠低壓聊天；忽必烈與阿麗婭談草原西域；李世民與潘金蓮互相注意；李隆基與紅娘喝酒互拆。"
    - "白玉池為本夜特殊試營運，非正式全面復業。"

  next_turn_rule:
    - "可以從翌晨自然顯影。"
    - "也可以由玩家點名任一尚亮 PATH 接續。"
    - "若玩家只說繼續，導演應推進一個清楚場景節點，不替玩家作重大選擇。"
    - "不得以『把剩下皇帝都配完』作為預設收束目標。"
```

---

# 34｜HOT V3.5 結論

```yaml
HOT_V3_5_CONCLUSION:
  status: "VALID_HOT_SAVE_CANDIDATE"
  current_world_time: "理火三年槐月二十八日無月夜／深夜"

  hard_results:
    - "九幽帝皇聯誼會觀止前宴完成並自然分流。"
    - "辭歲以 12,000,000 兩成交一夜契約；本人應收 10,800,000 兩，觀止應收 1,200,000 兩。"
    - "錦棠以 5,000,000 兩成交一夜契約；商會應收 3,750,000 兩、錦棠應收 750,000 兩、觀止應收 500,000 兩。"
    - "兩筆合計 17,000,000 兩仍在清算；次日先調 3,000,000 兩，最遲十日全清。"
    - "白玉池本夜特殊試營運成立，但沒有正式全面復業。"
    - "六條與趙受益互認『有／在乎』，但未定義戀愛與承諾。"
    - "多條帝皇人物線已依人物本人形成不同程度之談話、按摩、賭局、私人房資格或純社交入口；未決者保持未決。"
    - "尾聲白御行、李師師、張麗華同桌閒聊並以 HOT SAVE 收幕。"

  next_valid_hot_version: "V3.6"
  master_merge: "NOT_PERFORMED"
  character_pool_update: "NOT_PERFORMED"
  runtime_patch_merge: "NOT_PERFORMED"
```
