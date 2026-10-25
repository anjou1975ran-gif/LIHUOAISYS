# 觀止青樓｜白御行線 HOT SAVE V3.3
## 理火三年槐月二十六日清晨｜浮香自願留宿 × 紅娘煙幕揭穿 × 九幽帝皇聯誼會三日後訂單 × 大觀樓交接宴前置版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V3_3_HUAI26_MORNING_FUXIANG_FREE_BED_HONGNIANG_DECOY_JIUYOU_EMPEROR_ASSOCIATION_ORDER"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V3.3"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V11.0-R2"
  character_source: "觀止人物卡池_LCAPG_V2.2_辭歲入觀止動機校正_青禾六條增補_正式版"
  story_time_span:
    start: "理火三年槐月二十五日晚／HOT V3.2 後"
    current: "理火三年槐月二十六日清晨"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AT_GUANZHI_FRONT_DESK_AFTER_PAN_RECEIVES_JIUYOU_ORDER_AND_ASKS_MAX_REIMBURSEMENT"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V3.2_槐月二十五日白日_小翠同床純睡_三月集訓走秀換約_六百兩候選_白宅需求擴張與師師設計版.md"
  previous_hot_sha256: "2615f819d4d34d3ebd8932bd34d112f0b1a55f88c19ea1857898f33bc0f835f7"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"

  experimental_overlays:
    performance_patch:
      file: "觀止青樓_PATCH_風月角色表演與接戲能力_V0.1-EXP_獨立試跑未併主系統.md"
      status: "INDEPENDENT_TRIAL_OVERLAY_NOT_MERGED"
    analyzer_exit_patch:
      file: "觀止青樓_PATCH_分析器退場_重大升階定義_SCOPED_REACTIVATION_顯影反污染_V0.1-EXP.md"
      status: "GUANZHI_SPECIFIC_OPTIONAL_EXPERIMENTAL_OVERLAY_NOT_MERGED"

  save_scope:
    - "HOT V3.2 後白御行第二張免費床賭局之紅娘煙幕與浮香實際留宿結果"
    - "白御行與浮香私房談話、白宅邀請邊界與當夜成年人親密事件"
    - "浮香成人場分析器滯留事故之世界反污染鎖；故障說明不倒灌人物台詞／人格"
    - "鬼差於浮香房外送達之九幽城帝皇聯誼會正式訂單"
    - "白御行對九幽城、后土、攝政王、朱天、帝皇區與帝皇聯誼會之玩家線背景陳述"
    - "帝皇聯誼會本屆部分家族交接名單"
    - "三日後十餘名皇帝至觀止舉行交接大會之訂單需求"
    - "清倌／紅倌需求分流、公帳消費與白御行審帳權"
    - "三輪重量級拍賣只保存為白御行盤算／候選企畫，尚未排程、未取得任何女性本人同意"
    - "潘金蓮今晨收到訂單並開始籌備；目前等待白御行回答最高核銷額"
```

---

# 0｜提交法位、來源與反污染

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V3.2_槐月二十五日白日_小翠同床純睡_三月集訓走秀換約_六百兩候選_白宅需求擴張與師師設計版.md"
    role: "本檔直接前置 HOT；V3.2 及以前有效硬狀態全部繼承"

  master_archive:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"
    role: "截至 HOT V2.5 之長期因果；V2.6-V3.2 由 HOT 鏈承接"

  current_route_conversation_commit:
    role: "HOT V3.2 後至本次 HOT SAVE 命令前之直接劇情、玩家明示自身言行／過往背景、NPC 可觀察回應與玩家明示校正"

  runtime_reference:
    file: "觀止青樓_主程序_V11.0-R2_人物卡池單一接線輕量正式版.md"
    venue_anchor:
      formal_name: "大觀樓"
      function: "二樓中央大圓桌宴席空間"
      capacity: "約二十至三十人"
      distinction:
        - "大觀樓不是風滿樓。"
        - "風滿樓為千人級大型聚會／大型擴張場。"
        - "大觀樓為二樓中央大圓桌、小型高規格宴席空間，適合約二十至三十人。"
      note:
        - "三日後帝皇聯誼會十餘名皇帝交接宴應錨定於大觀樓。"
        - "不得再把大觀樓寫成風滿樓別稱或千人場。"

ANTI_CORRUPTION:
  fuxiang_hot_v1_3:
    status: "ILLEGAL_CORRUPTED_SAVE_AUDIT_ONLY"
    effect:
      - "浮香 HOT V1.3 整段仍不得使用。"
      - "本 V3.3 之浮香關係與成人事件全部來自 HOT V3.2 後重新合法生長之直接劇情，不引用 V1.3。"

  ghost_mail_misclassification:
    status: "PLAYER_CORRECTED"
    false_or_superseded_interpretation:
      - "最初導演曾把鬼差文件理解為『請帖／邀請白御行赴約』。"
    correction:
      - "玩家後續明示：鬼差送來的不是請帖，而是帝皇聯誼會交給潘金蓮／觀止的正式訂單。"
      - "因此本 SAVE 只保存 ORDER；先前『請帖』說法不得回流成世界事實。"

  analyzer_incident:
    status: "GOVERNANCE_FAILURE_NOT_CHARACTER_FACT"
    note:
      - "浮香成人場曾出現關係／安全分析器滯留、人物語言被治理解說污染之故障。"
      - "故障分類與修補只屬治理／回歸資料；不得把錯誤台詞、講義語氣或安全說明寫回浮香人格。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年槐月二十六日"
  time: "清晨"
  primary_location: "觀止青樓／前堂櫃台"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  player:
    name: "白御行"
    current_position: "潘金蓮櫃台前"
    immediate_context:
      - "昨夜自浮香房醒來／下樓後，紅娘當場因煙幕局被揭穿而抓狂。"
      - "白御行已把鬼差送來的帝皇聯誼會訂單交給潘金蓮。"
      - "已告知潘金蓮：該宴會支出走帝皇聯誼會公帳，白御行具有審查權。"

  pan_jinlian:
    current_position: "觀止前堂／櫃台"
    current_action:
      - "已閱讀訂單核心條件。"
      - "已開始叫春梅／瓶兒整理三日後席位、酒器、樂器、房數與相關籌備。"
    last_direct_question_to_player:
      - "這群皇帝的公帳——最高核銷到多少？"

  direct_resume_point:
    - "下一幕先由白御行回答或處理『最高核銷額／審帳尺度』；不得替玩家自動決定金額。"
    - "三日後帝皇聯誼會交接宴已形成真實訂單與籌備事件，但具體菜單、價格、姑娘名單、房間分配與拍賣節目尚未全部成立。"
```

---

# 2｜V3.2 繼承後仍有效之核心狀態

```yaml
INHERITED_ACTIVE_CORE:
  training_and_contract_switch:
    - "三個月新人集訓、走秀驗收、觀止約轉商會約之制度仍有效。"
    - "新人實際接客、出閣、拍賣與服務仍依本人資格／當下事件另行成立。"

  six_hundred_candidate:
    - "十八歲六百兩候選仍為高價候選線。"
    - "既有收購條件、個人五十兩、一成五未來出閣分成與訓練規則沿用 V3.2。"
    - "本輪僅被白御行納入三輪重量級拍賣的腦內盤算；尚未形成三日後實際上拍。"

  white_house:
    - "八千兩／十年條件式租用框架仍有效；需穩定空間真正形成後才啟動。"
    - "李師師已受命進行第一輪生活／功能設計。"
    - "本輪未因浮香談話或帝皇宴自動完成白宅建成、租金交付或永久入住。"

  bed_bet:
    - "白御行與李師師之『第二張免費床』賭局仍須在師師處正式結算。"
    - "賭局核心為：白御行需在無付費、無平兒安排、無權力施壓下，讓觀止女性自願讓他在自己的床／房留宿；性行為與床位判定分開。"
```

---

# 3｜BED25-E01｜紅娘煙幕局與錯誤傳聞

```yaml
EVENT_RECORD:
  event_id: "BED25-E01-HONGNIANG_DECOY"
  lifecycle_state: "COMPLETED_DECOY"
  event_axis_state: "COMPLETED"

  confirmed:
    - "白御行曾向紅娘提出免費床位局。"
    - "紅娘把『床位』與『性』分開，最終只接受一個遊戲性框架：白御行之後可敲門；不收錢；會開門；是否留下／睡覺不預先決定；可離開；不得強迫。"
    - "白御行實際上把紅娘設為煙幕與最後選項，沒有打算當夜真的去敲她房門。"
    - "白御行授意白紅伶散布『白總今晚睡紅娘的床／全套服務』『紅娘今晚不收錢』等煙幕說法。"
    - "上述內容是刻意製造的假傳聞，不是紅娘實際同意免費性服務。"

  morning_consequence:
    - "槐月二十六日清晨，紅娘看到白御行與浮香自樓上下來後，當場確認自己被當成煙幕，對白御行抓狂。"
    - "浮香在旁笑看／補刀；事件為喜劇性羞惱，不自動建立紅娘永久敵意或愛情。"

  pollution_lock:
    - "不得把假傳聞寫成紅娘真的提供免費全套服務。"
    - "不得把『紅娘留門／接受遊戲』改寫成已發生留宿或性行為。"
```

---

# 4｜FUXIANG25-26-E01｜浮香自願給床與白嫖賭局候選勝利

```yaml
EVENT_RECORD:
  event_id: "FUXIANG25-26-E01-FREE_OWN_BED_STAY"
  lifecycle_state: "COMPLETED_STAY"
  event_axis_state: "COMPLETED"

  location: "觀止／浮香私人房"
  time: "槐月二十五日晚至二十六日清晨"

  confirmed:
    - "白御行真正的第一目標一直是浮香；紅娘主要作煙幕。"
    - "白御行與浮香自二樓場面脫身後進入浮香私人房。"
    - "浮香在沒有收費、沒有權力壓迫、沒有被安排的情況下，自主決定讓白御行留在自己的房內並分半張自己的床。"
    - "因此依目前賭局已知條件，此事件構成『免費、自願、自己的床』的明確候選勝利。"
    - "是否正式判白御行贏下賭局，仍待李師師知道後進行實際結算；不得替師師提前宣判。"

  relationship_boundary:
    - "浮香給床不等於永久收留。"
    - "浮香給床不等於婚姻、如夫人、白家永久身份。"
    - "留宿與成人親密分軸成立。"
```

---

# 5｜FUXIANG25-E02｜白宅邀請與浮香位置

```yaml
FUXIANG_WHITE_HOUSE_TALK:
  status: "ROUTE_CONVERSATION_HARD_STATE"

  confirmed:
    - "白御行曾向浮香談及白宅與她可能的位置。"
    - "浮香目前不接受『永久成為白家人／夫人院固定成員』式直接收編。"
    - "若未來白宅實際穩定形成，且能給她一間可自由使用、能放琴、有窗、可住幾日又自行回觀止、沒有日常義務的房，她願意考慮／實地看看。"
    - "她沒有因此要求修改李師師正在做的第一輪白宅設計。"

  not_established:
    - "浮香已入住白宅"
    - "浮香取得夫人身份"
    - "浮香永久離開觀止"
    - "浮香對白御行形成永久承諾"
```

---

# 6｜FUXIANG25-E03｜當夜成年人親密事件

```yaml
ADULT_EVENT_RECORD:
  event_id: "FUXIANG25-E03-ADULT_INTIMACY"
  participants:
    - "白御行"
    - "浮香"
  adult_participants_confirmed: true
  location: "浮香私人房"
  time: "槐月二十五日深夜"

  event_axis:
    state: "COMPLETED_ADULT_INTIMACY"

  confirmed:
    - "雙方在當夜由親吻、擁抱與裸體同床逐步進入成年人親密事件。"
    - "浮香多次以自己的語言與可觀察行動形成主動／接受／回應；白御行也多次依她的即時回應調整。"
    - "事件後段包含已成立的性交與其後另一段成年人性親密；文字顯影曾採較低解析，但不得因此改寫成未發生。"
    - "浮香在互動中保留自己的節奏、戲謔、聲音與『女鬼』玩笑，不等於變成蘇清、張麗華或其他女人的複製。"
    - "雙方最終同床過夜，清晨一起下樓。"

  relation_axis:
    - "當夜慾望與親密成立。"
    - "不自動等於愛情、婚姻、永久專屬、永久性同意或人物所有權。"

  rendering_and_audit_note:
    - "本事件正是 FUXIANG-INC-001 的回歸樣本；治理故障不得回寫人物。"
    - "V11 EVENT / CHARACTER / RELATION / RENDERING 正交仍適用：顯影限制不等於事件不存在。"
```

---

# 7｜GHOST25-E01｜鬼差送達九幽帝皇聯誼會訂單

```yaml
EVENT_RECORD:
  event_id: "GHOST25-E01-JIUYOU_EMPEROR_ASSOCIATION_ORDER"
  lifecycle_state: "ACTIVE_ORDER"
  event_axis_state: "COMPLETED_DELIVERY"
  location: "浮香私人房／窗外"
  time: "槐月二十五日深夜"

  messenger:
    type: "鬼差"
    observable:
      - "黑衣／陰差形貌"
      - "從窗外送達文書"
      - "起初直呼『白御行』，經白御行糾正後改稱『白攝政王殿下』"
      - "接受白御行指示，回覆來方三日後來觀止"

  document:
    corrected_type: "帝皇聯誼會給觀止／潘金蓮的正式訂單"
    not: "私人請帖"
    recipient_operational: "潘金蓮／觀止青樓"
    delivery_intermediary: "白御行"

  confirmed_instruction_from_player:
    - "白御行收下訂單後命鬼差回去覆命：三日後讓他們來觀止即可。"

  not_established:
    - "鬼差知道訂單所有內情"
    - "任何未由玩家揭露的訂單細節"
    - "九幽／酆都對此宴會另有隱藏命令"
```

---

# 8｜JIUYOU-BACKGROUND25｜白御行公開說明之九幽背景

```yaml
PLAYER_STATED_BACKGROUND:
  source: "白御行本人於浮香房內向浮香說明"
  authority:
    - "白御行對自身過往、身分與自己參與之制度具有高權重自述法位。"
    - "除已由鬼差稱呼／訂單關係等可觀察事項外，其餘不自動推成所有世界角色已知的客觀全知事實。"

  statements:
    - "白御行稱其第一任正妻為后土娘娘；后土現為九幽城城主。"
    - "白御行稱九幽城現行制度大部分曾由自己設計。"
    - "白御行自認／被鬼差承認九幽城『攝政王』稱號。"
    - "后土屬甩手掌櫃型；白御行則是安排好制度後不常日常管理。"
    - "九幽城目前真正日常市長／管理者名為朱天。"
    - "朱天曾是定陶商會尚未轉型前最早的第一任總會長；現常副會長接其商會位置。"
    - "九幽有『皇帝區』：因缺乏『皇帝審判皇帝』的規則，歷代皇帝功過無人可合法定奪，因此形成制度 BUG；九幽不管、酆都不收。"
    - "白御行過去協助皇帝區建立『帝皇聯誼會』，讓皇帝們投資九幽產業、取得收入並維持享樂生活。"
    - "白御行稱自己對帝皇聯誼會公帳具有審查權。"
    - "武則天曾以『皇后』而非『皇帝』身份自報，走另一條報關／歸類通道離開皇帝區；此為白御行所述九幽軼事。"

  knowledge:
    heard_by:
      - "浮香"
    later_partial_shared_with:
      - "潘金蓮：至少已知本次帝皇聯誼會訂單、公帳與白御行審查權"
```

---

# 9｜EMPEROR-HANDOVER25｜本屆已揭露之帝皇家族交接名單

```yaml
EMPEROR_ASSOCIATION_HANDOVER:
  event_status: "SCHEDULED_IN_THREE_DAYS_BY_ORDER"
  total_expected: "十餘名皇帝；完整名單尚未全部揭露"
  purpose: "帝皇聯誼會交接大會"

  disclosed_roster:
    zhao_song:
      outgoing: "趙光義"
      incoming: "趙受益"
      role_change: "趙宋家族當家交接"
      note:
        - "趙受益是本白御行線已實際在觀止出現之人物。"
        - "其三日後是否以何種完整禮制／座次出場，尚未演出。"

    qin:
      honorary_president: "始皇"
      handover: false
      note:
        - "嬴家只有兩位皇帝；始皇本屆沒有打算交接。"
        - "始皇作為榮譽總會長將來觀止見證。"

    liu_han:
      outgoing: "劉邦"
      incoming: "劉病己"

    later_han_line:
      outgoing: "劉秀"
      incoming: "劉禪"
      structural_note:
        - "本屆安排把蜀漢納入後漢家族線。"
        - "未選劉備，而由劉禪接任。"

    tang_li:
      outgoing: "李世民"
      incoming: "李隆基"

    ming_zhu:
      outgoing: "朱棣"
      incoming: "豹房小王子"
      identity_expansion: "NOT_ADDED; preserve player's exact route nickname"

    qing:
      outgoing: "皇太極"
      incoming: "乾隆"

  unknown:
    - "其餘十餘名來客中的其他朝代／家族名單"
    - "正式座次"
    - "每一家的投票／交接機制"
    - "交接是否存在爭議或反對票"
```

---

# 10｜ORDER25-E02｜三日後觀止訂單需求

```yaml
JUIYOU_ORDER:
  status: "ACCEPTED_FOR_PREPARATION_NOT_FULLY_PRICED"
  event_date: "槐月二十九日若按三日後計；精確觀止曆換日由後續場景確認"
  venue:
    runtime_formal_anchor:
      name: "大觀樓"
      type: "二樓中央大圓桌宴席空間"
      capacity: "約二十至三十人"
    distinction:
      - "大觀樓與風滿樓為不同空間／場型。"
      - "風滿樓：千人級大型聚會／大型擴張場。"
      - "大觀樓：二樓中央大圓桌，可容納約二十至三十人。"
    intended_configuration:
      - "三日後十餘名皇帝之帝皇聯誼會交接宴使用大觀樓。"
      - "不啟動風滿樓千人級大型聚會狀態。"
      - "大圓桌下方懸空之既有空間形態沿用玩家明示設定。"

  guests:
    expected_count: "十餘名皇帝"
    nature: "帝皇聯誼會交接與見證"

  billing:
    payer: "帝皇聯誼會公帳"
    audit_right:
      holder: "白御行"
      confirmed_by_player: true
    current_max_reimbursement: "UNSETTLED"
    pan_current_question: "最高核銷到多少？"

  entertainment_and_courtesan_requirement:
    qing_courtesans:
      requested_role:
        - "彈琴"
        - "跳舞"
        - "宴樂／場面表演"
      red_service_requested: false

    red_courtesans:
      order_wording_direction:
        - "要能碰的紅倌"
        - "不能全部只看不能碰"
      hard_boundary:
        - "此為客戶訂單需求類型，不等於任何特定紅倌已答應任何特定身體接觸或性服務。"
        - "實際出場／陪席／親近／房事仍須依觀止安排、人物資格、當下事件與個別女性自己的決定成立。"

  fuxiang:
    category_in_current_talk: "清倌"
    response:
      - "浮香接受若此宴成立，自己以彈琴／清倌表演身份出場。"
      - "她未因此取得紅倌服務義務。"
```

---

# 11｜AUCTION25-IDEA｜三輪重量級拍賣盤算【未成立】

```yaml
AUCTION_CONCEPT:
  lifecycle: "PLAYER_IDEA_ONLY"
  world_event_status: "NOT_SCHEDULED"
  pan_approved: false
  women_confirmed: false
  order_includes_auction: "NOT_ESTABLISHED"

  player_private_or_spoken_planning:
    three_weight_candidates:
      - "辭歲"
      - "十八歲六百兩候選"
      - "阿麗婭重新掛牌／重新拍賣"

  idea:
    - "白御行盤算若帝皇聯誼會公帳豪爽、十餘名歷代皇帝同席，三輪重量級競價可能形成極高場面與價格。"
    - "曾討論辭歲若上拍，可設計成一夜／單次而非二十八日長期服務框架。"
    - "曾討論六百兩候選可作另一輪高價新人。"
    - "曾討論阿麗婭若本人未來願意重新掛牌，可成第三個重量級。"

  hard_prohibitions:
    - "不得寫成潘金蓮已批准三輪拍賣。"
    - "不得寫成辭歲已同意上拍。"
    - "不得寫成六百兩候選已同意出閣／上拍。"
    - "不得寫成阿麗婭已重新掛牌或同意拍賣。"
    - "不得把訂單的『紅倌需求』自動擴張成『必須安排三輪初夜拍賣』。"
    - "不得先設定成交價、得標皇帝或服務結果。"
```

---

# 12｜PAN26-E01｜潘金蓮收單與籌備啟動

```yaml
EVENT_RECORD:
  event_id: "PAN26-E01-PAN_RECEIVES_JIUYOU_ORDER"
  lifecycle_state: "ACTIVE_PREPARATION"
  event_axis_state: "INITIATED"
  time: "槐月二十六日清晨"
  location: "觀止前堂／櫃台"

  confirmed:
    - "白御行將昨夜鬼差送達之訂單交給潘金蓮。"
    - "潘金蓮閱讀到帝皇聯誼會、三日後、十餘位、交接宴、大席、清倌琴舞宴樂、紅倌需求等核心內容。"
    - "白御行告知支出走帝皇聯誼會公帳，且自己有審查權。"
    - "潘金蓮立刻轉入掌櫃籌備狀態，叫春梅、瓶兒整理三日後席位／酒器／樂器／房數等準備。"
    - "潘金蓮尚未獲得『最高核銷額』答案。"

  not_yet:
    - "完整菜單"
    - "酒水規格與數量"
    - "正式姑娘名單"
    - "房間分配"
    - "是否有拍賣"
    - "拍賣人選與本人同意"
    - "宴席總預算"
    - "觀止對帝皇聯誼會之最終報價"
```

---

# 13｜人物與關係增量

```yaml
RELATION_DELTAS:
  bai_fuxiang:
    confirmed_new_events:
      - "浮香自主讓白御行免費留宿自己的房／床。"
      - "雙方完成一夜成年人親密與同床過夜。"
      - "浮香知道白御行自述之九幽／后土／攝政王／帝皇區背景。"
      - "浮香願以清倌琴藝身份參與三日後帝皇交接宴。"
    remains_unresolved:
      - "愛情"
      - "長期專屬"
      - "白宅固定入住"
      - "夫人／妾室／正妻等名分"
      - "未來成人關係頻率"

  bai_hongniang:
    confirmed_new_event:
      - "紅娘發現自己被白御行作為免費床賭局煙幕，清晨公開抓狂／記帳式抱怨。"
    not_established:
      - "永久決裂"
      - "真實免費性服務"
      - "留宿事實"
      - "愛情"

  pan_order:
    confirmed:
      - "潘金蓮取得三日後帝皇聯誼會訂單的營運主場。"
      - "白御行保留帝皇聯誼會公帳審查權。"
    relationship_effect:
      - "形成一個新的潘金蓮—白御行合作／預算制衡場：潘負責把單做大，白握核銷尺度。"
```

---

# 14｜知情範圍

```yaml
KNOWLEDGE_SCOPE:
  fuxiang_knows:
    - "白御行昨夜以紅娘為煙幕、真正第一目標是自己"
    - "九幽城／后土／攝政王／帝皇區／帝皇聯誼會之白御行自述背景"
    - "三日後十餘名皇帝將來觀止的訂單大意"
    - "部分交接名單"
    - "訂單要求清倌琴舞、紅倌需有可親近服務類型"

  hongniang_knows:
    - "白御行昨夜沒有去她房，而去了浮香房"
    - "自己曾被拿來作煙幕"
    unknown_or_not_confirmed:
      - "九幽訂單完整內容"
      - "三輪拍賣盤算"

  pan_jinlian_knows:
    - "三日後帝皇聯誼會交接宴訂單"
    - "十餘位皇帝"
    - "公帳付款"
    - "白御行有審查權"
    - "清倌／紅倌需求分流"
    - "需立即籌備大席、酒器、樂器、房數"
    unknown_or_not_yet_shared:
      - "完整三輪拍賣盤算是否已正式告訴她：NOT_CONFIRMED"
      - "白御行與浮香昨夜成人事件的細節"
      - "九幽制度所有背景細節"

  broader_guanzhi:
    - "目前尚不得自動讓全樓知道皇帝完整名單、拍賣企畫或九幽制度內情。"
```

---

# 15｜大觀樓與風滿樓空間法位校正

```yaml
VENUE_CORRECTION:
  da_guan_lou:
    formal_name: "大觀樓"
    location_form: "二樓中央"
    core_feature: "大型圓桌／大餐桌"
    capacity: "約二十至三十人"
    lower_space: "桌／場域下方為懸空空間"
    role:
      - "中小型高規格宴席"
      - "二三十人級核心會議／交接宴"
      - "適合帝皇聯誼會十餘名皇帝同桌"

  feng_man_lou:
    formal_name: "風滿樓"
    capacity_class: "千人級"
    role:
      - "大型聚會"
      - "大型遴選"
      - "千人級擴張公域"

  hard_distinction:
    - "大觀樓不是風滿樓別稱。"
    - "風滿樓不是二三十人大圓桌空間。"
    - "兩者不得再合併、互稱或以同一場型處理。"

  current_event_use:
    - "三日後帝皇聯誼會交接宴固定使用大觀樓。"
    - "本次不啟動風滿樓千人級大型場。"
```

---

# 16｜仍活躍但本輪未解之重要事項

```yaml
OPEN_THREADS:
  pan_su_civil:
    - "蘇清 vs 潘金蓮民事／帳務案仍 ACTIVE；五萬為索賠方向，不是判決。"

  white_jade_pool:
    - "仍在翻修／許願幣系統準備，不因本輪帝皇宴自動復開。"

  white_house:
    - "李師師第一輪配置尚待完成／會審／空間穩定顯影。"

  shishi_bed_bet:
    - "浮香免費給床已形成高資格勝利證據；仍待李師師正式結算。"

  emperor_order:
    - "最高核銷額"
    - "最終預算"
    - "大觀樓席位／座次"
    - "菜單與酒單"
    - "出場清倌／紅倌名單"
    - "紅倌個別服務範圍與當下成立"
    - "是否納入拍賣"
    - "完整十餘名皇帝名單"
    - "每個家族交接的實際儀式與衝突"

  three_auction_idea:
    - "只屬白御行盤算；需潘金蓮營運判斷與各女性本人事件資格後才能升格。"
```

---

# 17｜禁止回歸／防污染

```yaml
ANTI_REGRESSION:
  - "不得恢復浮香 HOT V1.3。"
  - "不得把浮香當夜親密事件寫成她永久歸屬白御行。"
  - "不得把床位勝利自動等於李師師已承認賭輸。"
  - "不得把紅娘假傳聞寫成真實免費全套服務。"
  - "不得把鬼差訂單重新寫成請白御行赴陰間的私人請帖。"
  - "不得把『紅倌要能碰』寫成任何具名姑娘 blanket 性同意。"
  - "不得因皇帝有錢／公帳就讓姑娘自動接受服務、拍賣或出閣。"
  - "不得把三輪拍賣盤算升格成已排程事件。"
  - "不得把阿麗婭重新掛牌寫成已發生；她是否重新掛牌仍須本人另行成立。"
  - "不得把辭歲或六百兩候選寫成已答應三日後上拍。"
  - "不得把『大觀樓／風滿樓』與前幾日大型遴選的數千人擴張狀態混成同一必然場面。"
  - "不得自行替『豹房小王子』補出玩家未明示的正式歷史身份進 SAVE。"
  - "不得解釋命運籤或替九幽未知制度補規則。"
```

---

# 18｜直接接關摘要

```yaml
DIRECT_RESUME:
  story_time: "理火三年槐月二十六日清晨"
  location: "觀止前堂／潘金蓮櫃台"
  immediate_scene:
    - "紅娘抓狂事件剛過。"
    - "浮香在場／近場，昨夜留宿與親密已完成。"
    - "潘金蓮已拿到三日後帝皇聯誼會交接宴訂單。"
    - "大觀樓為二樓中央約二十至三十人大圓桌宴席空間，與千人級風滿樓不同；本次帝皇聯誼會使用大觀樓。"
    - "潘金蓮已開始籌備。"
    - "當前需要白御行回答：帝皇聯誼會公帳最高核銷到多少。"

  next_action_owner: "PLAYER_FOR_BUDGET_DECISION; WORLD_MAY_PREPARE_AFTER_RESPONSE"
```

---

# 19｜HOT V3.3 結論

```yaml
HOT_V3_3_CONCLUSION:
  state: "VALID_CURRENT_HOT"
  replaces_for_direct_resume: "HOT V3.2"
  preserves_previous_chain: true
  master_updated: false
  character_pool_updated: false
  main_program_updated: false
  experimental_patch_merged: false

  key_new_hard_states:
    - "浮香自主免費給床，白御行第二張床賭局取得明確候選勝利證據。"
    - "浮香與白御行完成當夜成年人親密與同床。"
    - "紅娘煙幕於清晨揭穿，紅娘抓狂；假傳聞仍是假。"
    - "鬼差送達的是帝皇聯誼會訂單，不是請帖。"
    - "三日後十餘名皇帝將來觀止舉行帝皇家族交接大會。"
    - "已揭露趙宋、秦、漢、後漢／蜀漢、唐、明、清等部分交接安排。"
    - "宴會支出走帝皇聯誼會公帳，白御行有審查權。"
    - "訂單明示清倌主琴舞宴樂、紅倌需提供可親近類型；個別服務仍不自動成立。"
    - "潘金蓮已接單並開始籌備。"
    - "三輪重量級拍賣仍只是白御行盤算，沒有任何一輪正式成立。"
    - "大觀樓為本次三日後帝皇宴正式空間錨點；風滿樓另為千人級大型聚會場，兩者不可混用。"

  hold_question:
    - "帝皇聯誼會公帳最高核銷額是多少？"
```
