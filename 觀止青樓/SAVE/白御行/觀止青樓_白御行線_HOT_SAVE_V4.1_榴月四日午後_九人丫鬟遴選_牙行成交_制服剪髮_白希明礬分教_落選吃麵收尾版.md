# 觀止青樓｜白御行線 HOT SAVE V4.1
## 理火三年榴月四日午後｜錦棠晨起 × 五女丫鬟遴選 × 兩牙行二十三人雙向選擇 × 九人成交 × 制服剪髮 × 白希明礬分教 × 十四名落選者吃麵收尾版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V4_1_LIU04_AFTERNOON_MAID_SELECTION_YAHANG_PURCHASE_UNIFORM_HAIRCUT_TRAINING_NOODLE_CLOSE"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V4.1"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V12.0"
  character_source: "觀止人物卡池_LCAPG_V2.3_李清照趙受益錦棠顧青簡增補_薛濤魚玄機暫定入場_正式版.md"

  story_time_span:
    start: "HOT V4.0 後／理火三年榴月三日深夜"
    current: "理火三年榴月四日午後早段"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AT_GUANZHI_AFTER_MAID_SELECTION_PURCHASE_AND_TRAINING_HANDOFF; BAI_SANSHIERNIANG_TAKES_14_UNSELECTED_CANDIDATES_OUT_FOR_NOODLES"

  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V4.0_榴月三日深夜_錦棠首次正式約會_自主購衣望河樓_私人成人事件_喜歡確認_相擁收幕版.md"
  previous_hot_sha256: "4ae078855001a64e82c170f7977257fab5557128810bba1c0d68c25265d4a3ea"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md"

  save_scope:
    - "HOT V4.0 相擁收幕後至榴月四日午後之直接玩家線事件"
    - "榴月三日深夜後段公開玩笑、跨夜返房與錦棠主動選擇睡眠收尾"
    - "榴月四日晨間錦棠房醒來、換衣、錦棠續睡與白御行下樓"
    - "李清照、柳如是對目前是否繼續留觀止及丫鬟安排之本人表述"
    - "兩家牙行共二十三名成年女性候選之午飯、體能／實務觀察、五女提問、候選自選主人與最後九人遴選"
    - "錦棠三人由錦棠自行負擔；楊玉環二、六條二、李清照一、柳如是一共六人由白御行先付之帳務分離"
    - "六人一百七十八兩、錦棠三人九十四兩之成交價；白御行兩張百兩票與應找二十二兩"
    - "牙行成本／飲食討論、玩家拒絕二次砍價與『給面子不等於可忽悠』之談判結論"
    - "六名白御行側新丫鬟制服、木簪、夏裝與三名自願剪髮之安排"
    - "三名自願剪髮者各得白御行三兩個人獎勵，剪下頭髮售款亦歸本人；白御行明日亦剪"
    - "白希負責錦棠三人初教；白明礬負責六人初教；白紅伶加入協助認路／跑腿"
    - "十四名未入選成年候選由白三十二娘帶到外攤吃麵吃飽，再交回各自牙行／離場"
```

---

# 0｜提交法位、來源與本輪反污染

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V4.0_榴月三日深夜_錦棠首次正式約會_自主購衣望河樓_私人成人事件_喜歡確認_相擁收幕版.md"
    role: "本檔直接前置 HOT；V4.0 及以前有效硬狀態全部繼承，除本檔明示更新／校正者"
    sha256: "4ae078855001a64e82c170f7977257fab5557128810bba1c0d68c25265d4a3ea"

  master_archive:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md"
    role: "截至 HOT V3.4 之長期固化；V3.5→V3.6-R2→V3.7→V3.8→V3.9→V4.0→本 V4.1 依序作較新合法疊加"

  current_character_source:
    file: "觀止人物卡池_LCAPG_V2.3_李清照趙受益錦棠顧青簡增補_薛濤魚玄機暫定入場_正式版.md"
    role: "現行跨線人物基線；本輪新丫鬟全部只屬白御行線 ROUTE EVENT，不自動加入人物卡池"
    sha256: "b7ce5f3e8870b170499e70bfe60b3d6b951987badc795434d7dfd9ef06637d59"

  runtime_reference:
    file: "觀止青樓_主程序_V12.0_FIELD_STATE接戲分析器場態整合正式版.md"
    version: "V12.0"
    status: "DOCUMENT_LEVEL_CURRENT_GUANZHI_RUNTIME_SPEC"
    sha256: "2159467f8a1d3eb31a8a0930e7d7b421bd7501a32eff35ceea383288f25a1978"

  current_route_conversation_commit:
    role:
      - "HOT V4.0 後至本次 HOT SAVE 命令前之直接劇情"
      - "玩家對自身言行、授權、付款、帳務理解與 GM 校正"
      - "NPC 可觀察行動、本人回答、自主選擇、交易結果與現場安排"
      - "上一份錯誤 V4.1 草稿經玩家明示要求重做，該錯誤草稿不取得 SAVE 法位"

COMMIT_NOTE:
  - "本檔取代 HOT V4.0 成為白御行線最新直接接關切片；V4.0 保留為前置歷史來源。"
  - "本次只更新 HOT SAVE；不更新 MASTER、不修改人物卡池、不修改主程序、不把任何 EXP PATCH 升格為已部署核心。"
  - "上一份將『三十二娘』誤讀成『三十二名落選者』之錯誤 HOT 草稿全部作廢；正確為白三十二娘此人帶十四名未入選候選去吃麵。"
  - "本輪所有候選均為成年女性；被買下／持身契／分配侍奉不等於任何成人親密、性行為、戀愛或永久同意。"
  - "候選自選想侍奉的女人只表示工作／相處方向選擇，不等於感情、忠誠或終身承諾。"
  - "牙行報價、本人技能自述、現場測試、成交價格、身契／轉契、日後工作能力必須分軸；一次測試不能升格成完整人格或永久能力判決。"
  - "玩家關於米價、牛馬價、牙行進價與利潤之說法只保存為玩家當場經濟論述／談判判斷，不自動升格為觀止世界唯一客觀價格表。"
  - "九名被選中者對牙行飲食的回答只代表其本人經歷，不得外推成所有牙行必然完全相同。"
  - "趙受益替楊玉環／六條丫鬟付款仍只是白御行未來可能拿去請款／討帳的方向；趙受益尚未形成債務、承諾或付款義務。"
  - "李清照與柳如是丫鬟先掛白御行名下的安排已成立；若二人日後離開，是否回收／重新分配需依當時實際關係處理，不可機械視為物件回收。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年榴月四日"
  time: "午後早段；午間遴選、成交與分工已完成；精確時刻未知"
  primary_location: "觀止青樓／大堂與內部公共區域"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  player:
    name: "白御行"
    current_position: "觀止內；九名新丫鬟成交與初教分工後"
    current_state:
      - "本輪遴選與付款已完成主要決策。"
      - "已將錦棠三人交白希初教。"
      - "已將自己先付的六人交白明礬初教，白紅伶加入協助。"
      - "已要求白三十二娘帶十四名未入選候選到外攤吃麵吃到飽再離場。"
      - "明日另有剪髮師傅與白御行本人剪髮安排。"

  bai_sanshierniang:
    current_state:
      - "已負責本輪牙行殺價與部分收款／轉契收尾。"
      - "此刻受白御行吩咐，帶十四名未入選候選外出吃麵。"

  guanzhi_background:
    ten_day_closure_day: 4
    ordinary_public_business: "CLOSED"
    internal_operations: "ACTIVE"
    renovation: "ACTIVE"

  direct_resume_point:
    - "可直接從榴月四日下午觀止內部、九名新丫鬟第一輪適應／認路、錦棠自己帶三人回生活區，或其他原有故事線重新取得注意力接起。"
    - "明日才執行剪髮；不得把肩長髮型、售髮收入或白御行新髮型寫成已完成。"
    - "不得替趙受益接受楊玉環／六條的丫鬟帳單。"
    - "不得把十四名落選候選寫成加入觀止；她們仍屬各自牙行後續處理。"
```

---

# 2｜HOT V4.0 後跨夜收尾：錦棠選擇睡眠

```yaml
LIU03_TO_LIU04_NIGHT_CLOSE:
  event_id: "LIU03-LATE-E01-JINTANG-DATE-NIGHT-CLOSE"
  event_axis_state: "COMPLETED"

  confirmed:
    - "HOT V4.0 相擁收幕後，白御行與錦棠本夜仍有後續低強度相處與公共區域玩笑。"
    - "二人跨過午夜，日期進入榴月四日。"
    - "二人最後返回錦棠房間。"
    - "錦棠主動選擇今晚不再追加成人互動，改為睡覺。"
    - "錦棠明示：『今天很好。不是最後那半個時辰。是整天。』"
    - "白御行與錦棠最後相依入睡。"

  relation_axis:
    - "本夜整體被錦棠本人評價為好，不等於她回覆了對等戀愛承諾。"
    - "睡在一起不新增永久同床、婚姻、排他或 blanket 成人同意。"
```

---

# 3｜榴月四日晨：錦棠房醒來、換衣與續睡

```yaml
LIU04_MORNING_JINTANG:
  event_id: "LIU04-MORNING-E01-JINTANG-WAKE-CLOTHING"
  event_axis_state: "COMPLETED"

  environment:
    - "觀止整修聲於清晨／早晨已可聽見。"
    - "錦棠仍在房內休息。"

  observed:
    - "錦棠隔門以『祖奶奶還沒睡飽』式玩笑回應樓下整修／來人。"
    - "白御行讓白希約一個時辰後送替換衣物到門外。"
    - "白御行與錦棠又在床上相依休息約一個時辰，沒有新增成人性行為。"
    - "白希按時把衣物送到門外。"
    - "白御行換衣起身，表示自己不是唐明皇，仍得起來工作。"
    - "白御行離開前親吻錦棠，讓她繼續睡、想起來再起來。"
    - "錦棠接受並繼續休息。"

  clothing_continuity:
    - "榴月三日方掌櫃處只帶走／穿上部分成衣；其他量身衣物仍留裁縫處製作。"
    - "本晨白希送來的是白御行可更換之現成衣物，不代表方掌櫃其餘訂製衣全部完成。"
```

---

# 4｜李清照、柳如是目前留觀止與丫鬟法位

```yaml
LI_QINGZHAO_LIU_RUSHI_STAY:
  event_id: "LIU04-MORNING-E02-LI-LIU-STAY-AND-MAID-ARRANGEMENT"
  event_axis_state: "CURRENT_ROUTE_POSITION_ESTABLISHED"

  continuity_lock:
    - "榴月三日只確認李清照、柳如是仍在觀止；不得補造她們當日具體行程、飲酒量、房間、對話或八卦。"

  li_qingzhao:
    本人_position:
      - "不願把自己先說成『長住』。"
      - "本人表述為眼下還想住；哪一天想走，哪一天再說。"
      - "她過去曾離開觀止，後來自行返回，此歷史保持。"
    maid_need:
      - "可用一名識字、懂紙墨與記憶物件位置、不要亂整理、她醉時不能跟著亂的丫鬟。"

  liu_rushi:
    本人_position:
      - "目前沒有打算走。"
      - "是否長期定居仍未決。"
    maid_need:
      - "偏好識字、有膽、知道何事值得管，在外護主、在內敢講真話的人。"

  player_arrangement:
    - "李清照與柳如是各自的丫鬟先掛白御行名下，供二人在觀止期間使用。"
    - "若二人之後不再需要，原則上可回到白御行側重新安排。"
    - "若丫鬟與主人長期相處形成新的實際關係／安排，屆時需重新談，不機械處理。"
```

---

# 5｜兩家牙行共帶二十三名成年候選入觀止

```yaml
MAID_SELECTION_ENTRY:
  event_id: "LIU04-NOON-E01-TWO-YAHANG-23-ADULT-CANDIDATES"
  event_axis_state: "COMPLETED"

  yahang_1_count: 12
  yahang_2_count: 11
  total_candidates: 23
  candidate_qualification:
    - "全部為成年女性。"
    - "此輪用途為內宅／貼身丫鬟遴選，不是觀止掛牌姑娘遴選。"

  selecting_women:
    - "錦棠"
    - "楊玉環"
    - "六條御息所"
    - "李清照"
    - "柳如是"

  player_position:
    - "白御行提供場地、付款與流程授權，但不替五女直接決定最終人選。"
    - "候選本人也取得自選想侍奉哪一位女子並自薦的機會。"
```

---

# 6｜候選午飯與身體狀態觀察

```yaml
CANDIDATE_MEAL_AND_BODY_CHECK:
  event_id: "LIU04-NOON-E02-CANDIDATE-MEAL-PHYSICAL-OBSERVATION"
  event_axis_state: "COMPLETED"

  meal_before_interview:
    player_instruction:
      - "白御行擔心牙行帶來的人可能尚未吃午飯，要求比照上次先準備吃食，邊吃邊等問話。"
    food:
      - "熱餅"
      - "肉湯"
      - "蒸蛋"
      - "蔬菜"
      - "少量甜食"
    logistics:
      - "先到者可先吃。"
      - "安排側桌，不要求她們在五女注視下進食。"
      - "潘金蓮將此餐列觀止招來候選之現場伙食，不把責任倒給牙行。"

  initial_exercise:
    player_order:
      - "二十下蛙跳"
      - "二十下仰臥起坐"
    purpose:
      - "白御行想看最低限度活動能力，理由之一是將來替小姐搬東西時不能明顯拖累。"
    interpretation_rule:
      - "不能把做不完直接判成懶、沒用或牙行餓壞。"
      - "需區分舊傷、天生低力量、臨時飢餓／疲勞與一般體能差異。"

  practical_followup:
    - "休息與吃飯後，以半箱布／實物從大堂搬至後院再回來作較接近日常工作的觀察。"

  notable_cases:
    old_leg_injury:
      - "一名女子右腿有舊傷；蛙跳三下左右即停。"
      - "她本人說過去摔傷；平常走路、站立、針線可做，但不適合此類蹲跳。"
      - "後成為六條所選丫鬟之一。"
    delicate_detail_worker:
      - "一名女子天生力量較弱，但擅長頭髮、衣物、首飾、香與妝等細活。"
      - "後成為楊玉環所選丫鬟之一。"
    sharp_eyed_candidate:
      - "一名眉眼利落女子搬箱時為避免旁邊候選跟不上／跌倒，主動慢半步。"
      - "後成為錦棠所選丫鬟之一。"
```

---

# 7｜五女各自列出的丫鬟核心條件

```yaml
MAID_CRITERIA:
  event_id: "LIU04-NOON-E03-FIVE-WOMEN-MAID-CRITERIA"
  event_axis_state: "COMPLETED"

  jintang:
    criteria:
      - "做事有分寸"
      - "嘴要緊"
      - "能替她看住衣物、銀錢、箱籠、首飾"
      - "不怕跟她說實話"
      - "遇事別先慌"
    本人_emphasis:
      - "她最怕旁邊的人先慌；過去自己已經夠慌。"

  yang_yuhuan:
    criteria:
      - "眼睛要好，會看場合、人、衣著與氣氛"
      - "手要細，能處理頭髮、衣物、首飾、香、妝"
      - "不蠢"
      - "知道何時該說、何時不必說"
      - "不能太怕她"

  rokujo:
    criteria:
      - "冷靜"
      - "有自己的判斷"
      - "不因主人不高興就亂掉"
      - "懂得保守私事"
      - "能長時間待在旁邊而不讓人覺得吵"

  li_qingzhao:
    criteria:
      - "識字而且真懂"
      - "記性好，能記稿、酒、信、人與物件位置"
      - "不會亂整理"
      - "她醉時不能跟著一起亂"
      - "必要時有膽攔她一次，但不要天天攔"

  liu_rushi:
    criteria:
      - "識字"
      - "有膽"
      - "知道什麼值得管、什麼不值得管"
      - "在外護主、在內敢講真話"
      - "不把忠心理解成沒腦子"

  shisanniang_summary:
    - "錦棠要穩。"
    - "楊玉環要靈。"
    - "六條要靜。"
    - "李清照要記得住。"
    - "柳如是要敢。"
```

---

# 8｜五個主問題與候選主動補答

```yaml
INTERVIEW_HARD_EVENTS:
  event_id: "LIU04-NOON-E04-FIVE-QUESTIONS-AND-VOLUNTARY-ALTERNATIVES"
  event_axis_state: "COMPLETED"

  jintang_question:
    target: "眉眼利落、搬箱時慢半步女子"
    question: "為什麼故意慢？"
    answer:
      - "因旁邊的人跟不上；箱子早半刻送到，不值得讓另一個人摔倒再多一堆事。"

  yang_question:
    target: "細活型、體力偏弱女子"
    question: "若楊玉環說髮簪不見，但妳記得是她自己隨手放的，怎麼處理？"
    answer:
      - "先找。"
      - "若只是主人忘記，不必特地讓她難堪。"
      - "若被問是不是自己放錯，則會直接說不是。"

  rokujo_question:
    initial_target: "眉眼利落女子"
    question: "主人吩咐一件妳覺得很蠢的事，怎麼辦？"
    answer:
      - "只是蠢、沒傷害就先做再說。"
      - "若會傷主人，先說。"
      - "主人若因此不高興，就讓她不高興，總比真受害後再哭好。"
    alternative_answer_old_leg_injury:
      - "右腿舊傷女子主動表示：她以前就是因照做不問而受傷，所以覺得不對會先問。"
      - "若主人確認仍要做，且不是送命，她再做。"

  li_qingzhao_question:
    target: "瘦、識字、簡單算數女子"
    question: "易安喝醉說把稿子燒了，燒不燒？"
    answer:
      - "第一晚不燒。"
      - "第二天再問。"
      - "若第三次仍確認，才燒。"
      - "她怕燒錯甚於怕被罵。"
    alternative_answer:
      - "另有候選表示只再確認一次，主人仍說燒就燒；理由是不應自以為比主人更懂主人意思。"

  liu_rushi_question:
    target: "實務型端茶女子"
    question: "若柳如是與人爭論，而妳知道柳錯了，怎麼辦？"
    answer:
      - "先把門關上。"
      - "私下說柳錯了。"
      - "除非必要，不在外人面前拆自己主人的台；但私下也完全不說，就失去丫鬟作用。"
    alternative_answer:
      - "另一穩重女子表示：不是每個小錯都值得管；若影響錢、人或主人後果才主動說，一般口角不一定插嘴。"

  jintang_alternative:
    - "一名年輕女子表示她不會為旁邊較慢者刻意放慢；除非對方真有危險，否則先完成小姐交代的事。"
    - "錦棠最後同時選了『會顧旁邊』與『先完成主務』兩種不同邏輯的人。"
```

---

# 9｜二十三人雙向選主結果

```yaml
BIDIRECTIONAL_SELECTION:
  event_id: "LIU04-NOON-E05-CANDIDATE-SELF-SELECTION"
  event_axis_state: "COMPLETED"

  rule:
    - "白御行要求候選不只被挑，也自行選想跟哪位女子，並說明自己適合的理由。"

  candidate_choice_counts:
    錦棠: 6
    楊玉環: 5
    六條御息所: 3
    李清照: 4
    柳如是: 5

  meaning:
    - "此數字只表示當下自選方向，不等於最終錄用數。"
    - "候選自選不保證五女必須接受。"
```

---

# 10｜最終九名丫鬟遴選結果

```yaml
FINAL_MAID_SELECTION:
  event_id: "LIU04-NOON-E06-FINAL-NINE-MAIDS"
  event_axis_state: "COMPLETED"
  selected_total: 9

  jintang:
    count: 3
    funding_and_management:
      - "錦棠自己出錢。"
      - "錦棠自己養、自己管。"
      - "因此白御行明示她想選幾個由她自己決定，不受白御行『一人一個』預算限制。"
    selections:
      JINTANG_MAID_A:
        descriptor: "眉眼利落、搬箱時為旁人慢半步女子"
        selection_logic:
          - "會注意旁邊人與整體麻煩。"
      JINTANG_MAID_B:
        descriptor: "年輕、先完成主務型女子"
        selection_logic:
          - "除非真有危險，否則不因別人慢就拖延小姐交代的事。"
      JINTANG_MAID_C:
        descriptor: "約二十七至二十八歲、安靜整齊型女子"
        selection_logic:
          - "不搶眼，但會自然把自己的物件、座位、用過的碗整理妥當。"
    jintang_statement:
      - "一個會顧旁邊，一個會把我要的事情先做完；我不覺得只能留一種。"
      - "第三人加入後，錦棠以『我付』確認自己承擔三人。"

  yang_yuhuan:
    count: 2
    selections:
      YANG_MAID_A:
        descriptor: "細活型、天生力量偏弱女子"
        role_direction:
          - "頭髮、衣物、首飾、香、妝等貼身細務。"
      YANG_MAID_B:
        descriptor: "約三十歲、穩定管理箱籠物件女子"
        self_choice_reason:
          - "認為楊娘子東西應該最多，她會管。"
    yang_logic:
      - "一個管我身上，一個管我東西。"
      - "不要一個人什麼都會，最後什麼都做得半吊子。"

  rokujo:
    count: 2
    selections:
      ROKUJO_MAID_A:
        descriptor: "右腿舊傷、因過去盲從受傷而重視先判斷女子"
        role_direction:
          - "遇到疑似有問題的命令先問，再依確認與風險程度執行。"
      ROKUJO_MAID_B:
        descriptor: "約三十歲、安靜穩定型女子"
        detail: "本輪未建立更多長期人格細節。"
    rokujo_logic:
      - "一個敢攔我，一個最好不要天天攔我。"

  li_qingzhao:
    count: 1
    selections:
      LI_MAID_A:
        descriptor: "瘦、識字、會簡單算數女子"
        role_direction:
          - "紙稿、信件、物件位置與酒後收尾。"
        notable_answer:
          - "醉後燒稿先延後、隔日再問、第三次確認才燒。"
        self_selection_detail:
          - "本人表示不喜歡把東西整理得過頭，否則自己也找不到。"

  liu_rushi:
    count: 1
    selections:
      LIU_MAID_A:
        descriptor: "識字、有膽、主張先關門再私下指出主人錯誤女子"
        history_statement:
          - "她曾待過一個沒人敢向主人說話的家，最後事情越積越糟。"
```

---

# 11｜九人付款、使用與所有權／帳務分軸

```yaml
PURCHASE_AND_ALLOCATION:
  event_id: "LIU04-NOON-E07-NINE-MAIDS-PAYMENT-ALLOCATION"
  event_axis_state: "TRANSACTION_PRICE_CONFIRMED_AND_PAYMENT_ROUTED"

  jintang_side:
    persons: 3
    final_price_total: "94兩"
    payer: "錦棠"
    management:
      - "三人由錦棠自己負擔、自己管理。"
    anti_merge:
      - "不計入白御行六人的178兩。"
      - "錦棠個人資產與白御行私人資產分開。"

  bai_side:
    persons: 6
    allocation:
      楊玉環: 2
      六條御息所: 2
      李清照: 1
      柳如是: 1
    original_yahang_total: "227兩"
    negotiated_total: "178兩"
    payer_now: "白御行"
    payment_instruments:
      - "白御行先交白三十二娘一張百兩票。"
      - "發現六人總價為178兩、錦棠94兩是另帳後，白御行再補一張百兩票。"
    total_notes_handed: "200兩票面"
    amount_due: "178兩"
    change_due_to_bai: "22兩"

  li_qingzhao_liu_rushi_title_axis:
    - "李清照與柳如是的一人丫鬟先掛白御行名下，分配給本人使用。"

  yang_rokujo_axis:
    - "白御行目前先付款，二人各自實際挑人與使用。"
    - "本輪未建立趙受益付款或承擔債務。"
    - "若未來白御行拿帳單找趙受益，趙受益可接受、部分接受或拒絕；必須屆時顯影。"

  transfer_paperwork:
    - "兩家牙行已接受最終價格，三十二娘／白希／潘金蓮負責現場結帳與轉契收尾。"
    - "本輪沒有逐張展示官府轉契文書內容，因此不得補造文書編號、日期戳或額外條款。"
```

---

# 12｜牙行殺價、成本拆帳與最終不再砍價

```yaml
YAHANG_NEGOTIATION:
  event_id: "LIU04-NOON-E08-YAHANG-NEGOTIATION-COST-DISCUSSION"
  event_axis_state: "COMPLETED"

  authorization:
    - "白御行明示自己只負責授權談判與最後付錢，其餘交白三十二娘、白希等人處理。"
    - "白三十二娘主攻價格，白希拆技能／教養／自述與報價差異，潘金蓮在必要時維持合理牙行利。"

  negotiation_principle:
    - "不是要求牙行虧本。"
    - "允許合理食宿、照看、訓練與滯銷風險成本。"
    - "主要拆掉誇大技能、模糊教養費與『因白御行有錢就加價』。"

  player_economic_argument:
    status: "PLAYER_STATEMENT_AND_NEGOTIATION_FRAME_NOT_OBJECTIVE_PRICE_CANON"
    statements:
      - "白御行以大白米、牛馬與牙行收人進價作比較，核心想表達『養人本身未必昂貴，尤其牙行日常並不會拿好酒好菜精養所有待售者』。"
      - "白御行推測部分女性進牙行時收價可能很低，牙行在資訊不透明下可有高利。"

  selected_women_food_testimony:
    status: "PERSONAL_EXPERIENCE_TESTIMONY"
    common_patterns_reported:
      - "粟粥／麥糊／粗糧粥"
      - "粗餅／豆渣餅"
      - "醃菜／菜湯"
      - "肉與精米較少見"
    individual_variation:
      - "有人表示有買主來看時會吃飽些。"
      - "有人病時喝過白米粥。"
      - "右腿舊傷女子曾拿過膏藥，並解讀牙行也有維持可售狀態之動機。"
      - "有人直接形容所在牙行『不餓死人，也不養胖』。"
    anti_generalization:
      - "不得把九人回答合併成所有牙行全國統一配給制度。"

  final_player_boundary:
    - "白三十二娘聽完成本後一度認為178兩可能還能再砍。"
    - "白御行明確制止二次砍價：『不用了，我只是要你們知道，我給你們面子，不代表你們能忽悠我。』"
    - "因此178兩與94兩保持原已談定價格，不因後續成本討論再變更。"

  yahang_result:
    - "兩家牙行接受：白御行肯讓其合理獲利，但後續不可用虛價／含糊成本測試他。"
    - "本事件不等於建立觀止對所有牙行永久統一定價規則。"
```

---

# 13｜六名白御行側丫鬟制服方向

```yaml
SIX_MAID_UNIFORM_PLAN:
  event_id: "LIU04-AFTERNOON-E01-SIX-MAID-UNIFORM"
  event_axis_state: "AUTHORIZED_NOT_YET_COMPLETED"

  handler: "白明礬"
  persons:
    - "YANG_MAID_A"
    - "YANG_MAID_B"
    - "ROKUJO_MAID_A"
    - "ROKUJO_MAID_B"
    - "LI_MAID_A"
    - "LIU_MAID_A"

  player_instruction:
    - "之後帶六人去成衣店。"
    - "每人選兩套制服。"
    - "同一花色／顏色／風格家族，但不要求六人完全一模一樣。"
    - "夏天用較薄、乾淨、實用而不破爛的布料。"
    - "以簡單木簪／木簪髮髻作女僕整體視覺方向。"
    - "可用邊條、腰帶等小差異區分工作／主人。"

  status:
    clothing_purchase: "NOT_YET_CONFIRMED_COMPLETED"
    exact_color: "NOT_FIXED"
    exact_shop: "NOT_FIXED"
```

---

# 14｜自願剪髮試驗、三兩獎勵與售髮收入

```yaml
HAIRCUT_PLAN:
  event_id: "LIU04-AFTERNOON-E02-VOLUNTARY-SHOULDER-HAIRCUT"
  event_axis_state: "VOLUNTEERS_CONFIRMED_EXECUTION_TOMORROW"

  player_reason:
    - "白御行認為夏天長髮工作麻煩，整理耗時，也覺得一大把過長頭髮不好看。"

  voluntary_rule:
    - "剪髮完全自願。"
    - "拒絕不影響錄用與侍奉位置。"

  reward:
    amount_each: "3兩"
    ownership: "本人個人財產"
    separation:
      - "三兩為白御行另給的試剪獎勵。"
      - "剪下來頭髮若可出售，售髮款另算，也全歸本人。"

  current_volunteers:
    - "LIU_MAID_A｜柳如是所選丫鬟"
    - "ROKUJO_MAID_A｜六條所選右腿舊傷丫鬟"
    - "LI_MAID_A｜李清照所選識字丫鬟"

  non_volunteer_example:
    - "YANG_MAID_A 明確不想剪；楊玉環支持她不剪，不因同宅工作要求外觀一致。"

  first_cut_spec:
    - "第一輪先剪到肩膀附近。"
    - "髮尾不得低於肩膀。"
    - "白御行認為日後可再試耳下長度，但本輪不直接剪到耳下。"

  tomorrow_execution:
    - "白明礬明日找真正會剪髮且可收購長髮的師傅。"
    - "剪前先報剪下長髮可售價格，再由本人確認。"
    - "剪髮尚未執行；售髮收入尚未發生。"

  player_haircut:
    - "白御行明日也要讓師傅替自己剪髮，理由是夏天想涼爽。"
    - "白御行本人要剪多短尚未在本輪定死。"
```

---

# 15｜白希、白明礬、白紅伶之初教分工

```yaml
MAID_TRAINING_HANDOFF:
  event_id: "LIU04-AFTERNOON-E03-MAID-TRAINING-HANDOFF"
  event_axis_state: "ASSIGNED_AND_STARTED"

  bai_xi:
    assigned:
      - "JINTANG_MAID_A"
      - "JINTANG_MAID_B"
      - "JINTANG_MAID_C"
    role:
      - "先教錦棠三人觀止／白家環境基本規矩與如何配合錦棠做事。"
      - "不把三人教成同一種人格。"
      - "錦棠本人直接交代優先於白希代教內容。"

  bai_mingfan:
    assigned:
      - "YANG_MAID_A"
      - "YANG_MAID_B"
      - "ROKUJO_MAID_A"
      - "ROKUJO_MAID_B"
      - "LI_MAID_A"
      - "LIU_MAID_A"
    common_training:
      - "觀止與白家哪些地方能去、哪些不能亂進。"
      - "常見人物稱呼與基本日常秩序。"
      - "銀錢、物件、私人房間不得亂碰。"
      - "主人私事不得拿出去當閒話。"
    specialist_rule:
      - "四位女主人各自的生活習慣與細節，由楊玉環、六條、李清照、柳如是本人再教。"
      - "李清照的紙稿不懂就別亂整理。"

  bai_hongling:
    status: "ASSISTING_MINGFAN"
    reason:
      - "白御行開玩笑說明礬若怕累可讓活力滿滿的紅伶來幫，只是可能養成災難。"
    observed_assignment:
      - "明礬接受紅伶協助。"
      - "紅伶先偏向帶人認路、跑腿、拿東西與知道事情該找誰。"
    limit:
      - "明礬仍是六人初教主責，不把紅伶的個人習慣直接當正式規矩。"
```

---

# 16｜十四名未入選候選之離場前吃麵

```yaml
UNSELECTED_CANDIDATES_CLOSE:
  event_id: "LIU04-AFTERNOON-E04-FOURTEEN-UNSELECTED-NOODLES"
  event_axis_state: "PLAYER_INSTRUCTION_GIVEN_AND_HANDOFF_STARTED"

  arithmetic:
    total_candidates: 23
    selected: 9
    unselected: 14

  player_instruction:
    - "白御行宣布本輪『打完收工』。"
    - "命白三十二娘帶沒選上的人去外面的攤子吃麵吃到飽。"
    - "玩家原意：別讓人餓著離開／回去。"

  correct_identity:
    - "『三十二娘』是白三十二娘此人，不是『三十二名姑娘』。"

  legal_status:
    - "十四人沒有因此被觀止買下。"
    - "吃麵不建立僱用、身契轉移、感情、報恩或未來錄用承諾。"
    - "吃飽後仍由各自牙行帶回／依牙行原有法位離場。"

  expense:
    payer_direction: "白御行／觀止本輪善後支出"
    exact_amount: "UNKNOWN_NOT_REQUIRED"
```

---

# 17｜新增九人關係／知情／工作法位摘要

```yaml
NEW_MAID_RELATION_MATRIX:
  jintang_three:
    principal: "錦棠"
    relation: "新購入之貼身／內宅丫鬟；仍在磨合期"
    funding: "錦棠"
    trainer: "白希"
    loyalty_or_affection: "NOT_PREASSIGNED"

  yang_two:
    principal: "楊玉環"
    relation: "新分配使用之丫鬟；仍在磨合期"
    payer_now: "白御行"
    trainer: "白明礬"
    zhao_debt: "NONE"

  rokujo_two:
    principal: "六條御息所"
    relation: "新分配使用之丫鬟；仍在磨合期"
    payer_now: "白御行"
    trainer: "白明礬"
    zhao_debt: "NONE"

  li_one:
    principal: "李清照"
    title_holder_direction: "白御行名下，供李清照使用"
    trainer: "白明礬"
    future_if_li_leaves: "RENEGOTIATE_OR_REASSIGN; NOT_AUTOMATIC_OBJECT_RECOVERY"

  liu_one:
    principal: "柳如是"
    title_holder_direction: "白御行名下，供柳如是使用"
    trainer: "白明礬"
    future_if_liu_leaves: "RENEGOTIATE_OR_REASSIGN; NOT_AUTOMATIC_OBJECT_RECOVERY"

  knowledge:
    - "五位女子均知道自己最後選了誰。"
    - "兩家牙行知道九人成交、十四人未成交。"
    - "九名新丫鬟知道自己的當前侍奉對象與初教安排。"
    - "三名剪髮志願者知道三兩獎勵與售髮款歸本人。"
```

---

# 18｜本輪反污染與失效輸出鎖

```yaml
ANTI_CORRUPTION_LOCK:
  revoked_previous_wrong_save:
    errors:
      - "上一版錯誤 HOT V4.1 將『三十二娘』誤認為『三十二名落選者』。"
      - "上一版錯誤 HOT V4.1 把時間寫回榴月三日深夜。"
      - "上一版錯誤 HOT V4.1 只記最後吃麵，遺失榴月四日整段丫鬟遴選與成交。"
    ruling: "全部作廢，不得作接關或事件來源。"

  no_objective_price_canon:
    - "玩家當場舉的大白米、牛馬、牙行進價等數字不自動固化成全世界唯一行情。"
    - "若未來需做歷史價格審計，另開 DISCUSSION／AUDIT 查證，不用本 HOT 玩家台詞替代。"

  no_yahang_monolith:
    - "九名女子的牙行伙食經驗可以不同；不得用單一『牙行都怎樣』抹平。"

  no_skill_overclaim:
    - "現場體能／搬箱／問答只是遴選證據，不是永久人格卡。"

  no_zhao_debt:
    - "白御行打算日後找趙受益買單是玩笑＋未來談判方向，不建立趙受益欠款。"

  no_haircut_completion:
    - "三名志願者尚未剪髮；白御行本人也尚未剪。"
    - "三兩獎勵與售髮款只有規則／承諾，實際支付與賣價待明日。"
```

---

# 19｜仍活躍／待後續顯影事項

```yaml
OPEN_THREADS:
  tomorrow_haircut:
    - "師傅是否找到、報價多少。"
    - "三名志願者是否明日仍維持意願。"
    - "實際髮型完成效果。"
    - "剪下長髮實際售價與入手金額。"
    - "白御行本人最後剪多短。"

  uniforms:
    - "六名白御行側丫鬟成衣店尚未實際選完兩套。"
    - "最終共同色、花色、邊條與腰帶尚未定。"

  maid_adjustment:
    - "九名新人尚在第一日／第一輪磨合。"
    - "各女主人後續可因實際工作適配調整分工，但不得無事件改人格。"

  zhao_reimbursement:
    - "楊玉環／六條四名丫鬟是否拿帳找趙受益、趙受益是否接受、接受多少，全部未發生。"

  li_liu_stay:
    - "李清照仍未承諾長住。"
    - "柳如是目前沒打算走，但長期狀態仍未定。"

  guanzhi_renovation:
    - "十日整修仍在第4日。"
    - "紅娘中央顯影場舞台硬體方向仍在施工／測試路徑。"
    - "紅娘房門窗／屏風十日換債仍持續至重新開業日上午恢復。"

  dingtao_and_external:
    - "曹州案仍為定陶商會當前 ACTIVE 案。"
    - "朱明長債／外部清算、貼身衣物專案等依 V3.8–V4.0 繼承，不因本輪丫鬟事件自動推進。"
```

---

# 20｜直接接關備忘

```yaml
DIRECTOR_RESUME_MEMO:
  current_date: "理火三年榴月四日"
  time: "午後早段"
  location: "觀止內"

  immediate_visible_state:
    - "九名新丫鬟已分流：錦棠3／楊玉環2／六條2／李清照1／柳如是1。"
    - "白希正接錦棠三人的初教；白明礬主責六人，白紅伶加入認路／跑腿協助。"
    - "白三十二娘正帶十四名未選候選到外面攤子吃麵。"
    - "白御行本輪買人與談判主戲已收工。"

  do_not_forget:
    - "錦棠的3人與白御行的6人是兩筆帳。"
    - "錦棠94兩；白御行六人178兩；白御行交兩張百兩票，應找22兩。"
    - "趙受益目前一文未承認，不得寫成欠債。"
    - "剪髮在明日，不是今天已完成。"
    - "只有三名現有志願者；楊玉環的細活丫鬟明確不剪。"
    - "剪下頭髮的錢歸本人；白御行另給3兩是另一筆。"
    - "十四名落選者只是吃飽再離場，不加入觀止。"
    - "李清照、柳如是榴月三日具體行程仍未知，不得倒填。"

  next_scene_permission:
    - "玩家若說『繼續／GO／下一步』，世界可從下午觀止內部自行發生下一個清楚場景節點。"
    - "不要因一個 GO 跳到明日剪髮；除非自然場景先完成或玩家明示推進到翌日。"
```

---

# 21｜本 HOT 一句接關摘要

> **榴月四日午後，白御行與錦棠跨夜後的第一個白日主戲已收束：兩家牙行帶來二十三名成年候選，五女先定自己真正要的丫鬟條件，再經吃飯、體能與實務觀察、提問和候選自選主人完成雙向遴選。最後錦棠自費留三人，楊玉環二、六條二、李清照一、柳如是一共六人由白御行先付；錦棠九十四兩、白御行一百七十八兩，趙受益沒有因此欠帳。六人制服與三名自願肩長剪髮已排到後續／明日，三兩獎勵與售髮款都歸本人；白希教錦棠三人，明礬教六人、紅伶協助。十四名未入選者由白三十二娘帶去外攤吃麵吃飽再離場。**
