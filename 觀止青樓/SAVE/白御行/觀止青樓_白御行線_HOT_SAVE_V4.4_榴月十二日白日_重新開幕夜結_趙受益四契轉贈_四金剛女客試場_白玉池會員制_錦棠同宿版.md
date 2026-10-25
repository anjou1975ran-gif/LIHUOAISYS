# 觀止青樓｜白御行線 HOT SAVE V4.4
## 理火三年榴月十二日白日｜榴月十一日晚重新開幕 × 女子競技與紅娘壓軸 × 顧三辭歲再會 × 趙受益四契轉贈 × 四大金剛／李清照女客試場 × 白玉池會員制 × 錦棠同宿版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V4_4_LIU12_DAY_REOPENING_NIGHT_CONTRACT_GIFTS_GUEST_TRIAL_WHITE_JADE_MEMBERSHIP_JINTANG_OVERNIGHT"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V4.4"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V12.0"
  character_source: "觀止人物卡池_LCAPG_V2.3_李清照趙受益錦棠顧青簡增補_薛濤魚玄機暫定入場_正式版.md"

  story_time_span:
    start: "HOT V4.3 後／理火三年榴月十一日白日"
    current: "理火三年榴月十二日白日／昨夜重新開幕已結束"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AFTER_HOT_SAVE_COMMAND_ON_LIU12_DAY_AFTER_BAI_YUXING_AND_JINTANG_OVERNIGHT"

  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V4.3_榴月十日深夜_開幕前夕_商會女人培訓目的鎖_小翠首次完整行房_三人同睡版.md"
  long_term_master_before_this_save: "觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md"

  save_scope:
    - "榴月十一日觀止重新開幕之營業、女子競技、賭盤、商會女人第一晚實戰與紅娘壓軸"
    - "白御行以客人身分開最大包廂，定陶商會重要客戶宴請框架與多人自然分流"
    - "顧三以商人／商會拜訪者身分到場，與辭歲重逢；一炷香舊事之公開已知與私人未知分離"
    - "楊玉環／六條正在使用之四名白御行側丫鬟，以總價二百兩轉給趙受益；趙受益再將兩張契分別轉贈二女"
    - "四大金剛對妓籍之個別意向，以及四人＋李清照以付費女客身分進大堂被動回應搭訕之試場"
    - "蘇清、小翠當夜可觀察位置與後續 UNKNOWN"
    - "張麗華『酒促姑娘』自組班底構想，只記為有興趣／候選生意，不記成已成立事業"
    - "潘金蓮接受白玉池高級會員預約制方案，預定榴月十二日晚啟用；白天非營業時間供觀止自己人使用"
    - "楊玉環在觀止歇業期間近十日持續使用白玉池；『楊貴妃第一指名』僅為待本人同意之宣傳候選"
    - "榴月十一日晚白御行與錦棠同宿；私人內容不記、不推導"
```

---

# 0｜來源、法位與反污染

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "HOT V4.3"
    role: "榴月十日深夜直接前置；開幕鎖、小翠前夜事件、商會女人培訓目的等全部繼承。"

  current_route_conversation_commit:
    role:
      - "HOT V4.3 後至本次 HOT SAVE 命令前之直接劇情。"
      - "玩家對自身言行、GM 校正、契籍法位、妓籍／奴籍規則與營運方向之明示。"
      - "NPC 可觀察回應、本人明示選擇、已完成付款／轉契／同桌／入場／退場與營運決策。"

COMMIT_NOTE:
  - "本檔取代 HOT V4.3 成為最新直接接關切片；V4.3 保留為前置歷史來源。"
  - "本檔不修改人物卡池，不把單線人物事件倒灌成跨線人格。"
  - "所有笑話、揶揄、猜測、外界可能如何腦補，不自動升格為世界事實。"
  - "『一炷香』、蘇清去向、小翠後續接客、顧三與辭歲離席後發生什麼，沒有來源就維持 UNKNOWN。"
  - "成人舞台事件只固化事件結構，不把觀眾反應推成每個人必然欲望或後續性行為。"
  - "奴籍、妓籍、陪酒、女客、接客、私人性愛、戀愛與契約分軸保存。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年榴月十二日"
  time: "白日／觀止夜間營業前；精確時刻未知"
  primary_location: "觀止／錦棠房及相鄰內部生活區"
  player:
    name: "白御行"
    state:
      - "榴月十一日晚與錦棠同宿。"
      - "私人內容由玩家明示不記錄。"
      - "現已推進至次日。"
  jintang:
    state:
      - "與白御行同宿至次日。"
      - "未因同宿新增婚姻、獨占、所有權或永久排他承諾。"
  guanzhi:
    reopening_status: "榴月十一日晚正式重新開幕已完成第一夜"
    current_phase: "榴月十二日白日／夜間第二晚營業前"
  direct_resume_point:
    - "可從榴月十二日白日的昨夜結算、人物自然後續、白玉池會員制開放前準備，或其他世界自主事件接起。"
    - "不得替白御行自動決定今晚白玉池預約、付款、邀誰入池或其他私人安排。"
```

---

# 2｜榴月十一日白日：開幕日前半段

```yaml
LIU11_DAY:
  nightlife_rhythm_correction:
    - "觀止為夜間營業場所；人物不應被預設清晨集體早起。"
    - "白御行白日以『今晚做客人』為主，不接管潘金蓮之開幕營運。"

  reopening_lock:
    - "正式重新開幕仍為榴月十一日晚。"
```

---

# 3｜榴月十一日晚：觀止重新開幕成立

```yaml
REOPENING_NIGHT:
  status: "COMPLETED_FIRST_NIGHT"
  venue:
    - "大堂正式重新對外營業。"
    - "中央籠台／舞台投入使用。"
  seating_price_observed:
    front_row: "20兩"
    outer_edge: "1兩"
    note:
      - "潘金蓮已有座席分層；富客與普通看客在空間上可被直接辨識。"
      - "不得再寫成今晚尚未分票價。"

  business_layers_observed:
    - "觀止既有姑娘照常攬客／陪酒／接生意。"
    - "宋蕙蓮、桂姐確實在場內做原有風月生意。"
    - "商會培訓女人被放進真實客場學習找客、被拒、換桌、成交與客情經營。"
    - "商會女人前三個月仍屬觀止實戰培訓期；之後全轉定陶商會約之既有目的不因第一晚改變。"
```

---

# 4｜女子競技與賭盤

```yaml
WOMEN_COMBAT_LIU11:
  status: "ACTIVE_AND_OBSERVED"
  participant_rule:
    - "參賽者均為成年女性。"
    - "潘金蓮已安排參賽前簽『生死狀』／競技風險文書；本 HOT 不外推其超出觀止世界設定之法律效力。"
  core_rule:
    - "以壓制對手達五數為基本勝負判定。"
  recruitment:
    - "潘金蓮已動員牙行等來源持續找參賽者；女子競技可每日持續，亦兼作護衛人才第一層顯影。"
    - "競技勝負 != 護衛資格；後者仍需另測。"

  bai_first_bet:
    stake: "100兩"
    side: "較矮／賠率較冷一方"
    result: "下注方獲勝"
    principal:
      - "白御行原100兩本金收回。"
    winnings:
      - "淨贏額未在本輪留下可核對精確數字。"
      - "白御行把贏得的部分交四大金剛作她們自己的後續賭本；不得補造精確四分之一數字。"

  slippery_hand_special:
    state: "ONE_TRIAL_OCCURRED"
    confirmed:
      - "曾安排一場雙手抹食用油的特殊『滑手局』，參賽成年女性接受後上場。"
    not_formalized:
      - "全身抹油、更加易裂服裝、女子雙打／混合雙打等後續只停在候選點子；本晚未固定成常規。"
```

---

# 5｜紅娘開幕壓軸

```yaml
HONGNIANG_FINALE_LIU11:
  status: "COMPLETED"
  structure:
    - "紅娘先以完整衣裝進場，經脫衣舞逐步推高場內注意。"
    - "脫衣舞不是最終段；後段為公開成人自我慰藉表演。"
    - "紅娘本人於舞台上達到高潮後收幕退場。"
  event_rendering_boundary:
    - "SAVE 固化上述事件結構；不逐格保存器官／技巧描寫。"
  observable_business_aftereffect:
    - "紅娘退場後，大堂叫酒、叫姑娘、問留宿等需求明顯再度升高。"
    - "這只保存為當晚可觀察營業反應，不推成所有客人必然後續性交。"
```

---

# 6｜白御行最大包廂與人物分流

```yaml
VIP_BOX:
  host_frame:
    - "白御行以今晚做客人之姿開樓上最大包廂。"
    - "席間形成『定陶商會宴請重要客戶』之公帳招待框架；最終完整報銷數額本 HOT 未核定。"

  actually_observed_in_box:
    - "白御行"
    - "常煒"
    - "顧青簡"
    - "白三十二娘"
    - "白明礬"
    - "白紅伶"
    - "白希"
    - "錦棠"
    - "辭歲"
    - "顧三（後到）"

  other_parallel_rooms:
    zhao_shouyi:
      - "趙受益另開自己包廂。"
      - "六條御息所與楊玉環後來均到其包廂。"
      - "本 HOT 不推導房內成人、戀愛或三人關係新結果。"
    shen_wansan:
      - "沈萬三另開包廂。"
      - "柳如是自主進入與沈萬三辯論；李清照後被柳如是叫入同桌。"
    li_shishi:
      - "李師師本夜自設自己的桌／場，不是被白御行分配陪酒。"
    zhang_lihua:
      - "張麗華在前堂酒水／酒坊線活動。"
```

---

# 7｜顧三 × 辭歲：舊事重逢與未知邊界

```yaml
GUSAN_CISUI_LIU11:
  gusan_entry:
    - "顧三以商人／定陶商會拜訪者身分到觀止，之前已向商會投帖。"
    - "他到白御行包廂，不得寫成專程追辭歲而來。"

  public_old_event:
    - "外界可知：十幾日前顧三付五十兩、與辭歲有一炷香之私人安排、燈熄後再送客。"
    - "顧三本夜明示自己不覺得五十兩花冤。"
    - "上述足以形成外界風月腦補／傳聞，但不是私室內事件證據。"

  private_unknown:
    - "當晚一炷香私室內究竟發生何種身體／成人事件，仍只有當事二人可能知道。"
    - "不得補寫裸身、性交、保護、戀愛或其他未有來源之細節。"

  current_relation:
    - "本夜二人有可觀察的熟悉與玩笑，可一起碰杯。"
    - "不得因此升格為情人、保護關係或戀愛承諾。"

  later_last_observed:
    - "白御行一行離開原包廂後，顧三與辭歲仍留在該處。"
    - "其後夜生活與是否同行，UNKNOWN。"
```

---

# 8｜辭歲重要客戶狀態

```yaml
CISUI_CLIENT:
  inherited:
    fixed_deposit:
      principal: "5,000,000兩"
      term: "5年"
      rate: "五分"
      status: "SIGNED_AND_EFFECTIVE"
    remaining_liquid: "5,800,000兩"

  liu11:
    - "以重要客戶／金主身分受招待。"
    - "她有考慮未來再添丫鬟，至少一名希望具真實護衛能力；女子競技可作第一層觀察來源。"
    - "本夜未完成新的丫鬟購買。"
```

---

# 9｜趙受益購四契並轉贈六條／楊玉環

```yaml
FOUR_MAID_CONTRACT_TRANSFER:
  prior_title:
    source_axis:
      - "HOT V4.1 六名白御行側新丫鬟中：楊玉環2、六條2、李清照1、柳如是1。"
      - "其中楊玉環、六條各自實際挑人與使用；不等於她們原本持契。"

  liu11_transaction:
    seller: "白御行"
    buyer: "趙受益"
    object:
      - "楊玉環正在使用之2名成年丫鬟之身契"
      - "六條御息所正在使用之2名成年丫鬟之身契"
    total_price: "200兩"
    pricing_logic:
      - "白御行明示嫌逐張計算麻煩，直接取整數二百兩。"
      - "不得由此反推四人原始逐張成本或白御行實際盈虧。"
    payment:
      status: "PAID"
      payer: "趙受益"
      receiver: "白御行"
      amount: "200兩"

  zhao_gifts:
    completed:
      - "趙受益確認二女是否願意收後，六條明示要，楊玉環明示要。"
      - "兩張契轉予六條，兩張契轉予楊玉環。"
      - "二女均收下此份心意。"
    relation_boundary:
      - "二女收下禮物 != 已承認趙受益的愛、婚姻、排他戀愛或其他未明示承諾。"
      - "『愛』只停在白御行玩笑／媒合話術；趙受益本人表示由二女自己判斷。"
```

---

# 10｜奴籍／妓籍法位與四大金剛現況

```yaml
PROSTITUTION_STATUS_WORLD_RULE:
  gm_route_correction:
    - "奴籍與妓籍可同時存在。"
    - "奴籍處理主僕／身契位置；妓籍處理風月職業／合法接客位置，兩者不可互相偷換。"
    - "持有女奴身契不等於持有她作妓女接客之職業權。"
    - "未入妓籍之奴籍女子若被主人強迫按妓女方式陪酒／接客，在本世界具有對主人提出救濟／控訴之位置。"
    - "妓籍一旦正式登記，不可撤銷，為終身妓女身分；自由與否是另一軸。"

FOUR_GUARDS_STATUS:
  bai_sanshierniang:
    slave_status: "仍屬白御行奴籍側"
    prostitution_intent: "本人已明確決定要登妓籍"
    registration_complete: false
    note:
      - "她明示未來作妓女時男人由自己挑、錢自己收；白御行不是她的鴇母。"

  bai_hongling:
    slave_status: "仍屬白御行奴籍側"
    prostitution_intent: "更偏向登妓籍／有明顯興趣"
    registration_complete: false
    note:
      - "仍未形成正式『現在就登』的最終完成事件。"

  bai_mingfan:
    slave_status: "仍屬白御行奴籍側"
    prostitution_intent: "目前不登"
    registration_complete: false

  bai_xi:
    slave_status: "仍屬白御行奴籍側"
    prostitution_intent: "目前不登"
    registration_complete: false
```

---

# 11｜四大金剛＋李清照：女客身分試場

```yaml
FEMALE_GUEST_TRIAL_LIU11:
  framework:
    - "白御行放四大金剛當晚休假。"
    - "四人自行付錢以觀止『女客』身分進大堂。"
    - "她們不是掛牌妓女，不主動攬客，不向男人收客錢。"
    - "男人若主動搭訕，她們可自行決定是否回應。"
    - "四人被要求明白告知對方：自己不是妓女。"
    - "李清照本人也接受同一玩法，付費作女客下場。"

  observed:
    bai_sanshierniang:
      - "有年輕男客主動搭話。"
      - "她先說明自己是付錢女客、不掛牌、不接客錢，再與對方聊賭局。"
      - "後續是否發展，UNKNOWN。"

    bai_hongling:
      - "第一名男客開口問價，她明示自己不是妓女，對方道歉離開。"
      - "另一名較年輕男客先問能否同坐；她再說明女客身分，允許對方請酒並坐下聊天。"
      - "後續是否發展，UNKNOWN。"

    bai_mingfan:
      - "有中年男客因賭票搭話。"
      - "她說明自己不是觀止姑娘後，允許對方坐下。"
      - "後續是否發展，UNKNOWN。"

    bai_xi:
      - "有男客邀一起喝酒；她明示自己是女客並直接表示不想，對方離開。"
      - "她沒有因此形成失落或改變妓籍意向。"

    li_qingzhao:
      - "仍不是妓女，未登妓籍。"
      - "有一名約三十多歲、衣著普通但整潔的男客以麗華酒坊新酒話題搭話。"
      - "李清照先明示自己是女客、不是掛牌姑娘、不接客也不收他的錢，之後允許他坐下談酒。"
      - "二人後續聊酒、地方風味等；最後結果與是否另有私人發展，UNKNOWN。"

  anti_inference:
    - "被搭訕／同桌／請酒 != 接客、性、戀愛、承諾。"
```

---

# 12｜李清照妓籍討論：本夜未登

```yaml
LI_QINGZHAO_STATUS_LIU11:
  baseline: "NOT_A_PROSTITUTE"
  discussion:
    - "白御行曾建議她是否登妓籍，以便合法進場挑男人。"
    - "李清照承認觀止混合風月場會使她感覺男人並非全無意思。"
    - "她明示本夜不登妓籍。"
    - "她後來表示自己拒絕的理由不是單純守『良家』招牌，而是目前沒有覺得妓籍值得拿終身身分交換。"
  state:
    prostitution_registration: "NOT_CHANGED"
    future_position: "可自行再想；不是承諾未來會登"
```

---

# 13｜柳如是：本夜未形成新掛牌事件

```yaml
LIU_RUSHI_LIU11:
  observed:
    - "曾對『若自己舊有妓籍仍能使用，今晚可自行挑男人』表達興趣。"
  not_completed:
    - "本 HOT 未觀察到她正式向潘金蓮掛牌、接客或帶男人離場。"
  therefore:
    - "不得把討論升格為當晚已掛牌／已接客。"
```

---

# 14｜張麗華酒促姑娘構想

```yaml
ZHANG_LIHUA_PROMO_TEAM:
  state: "PROPOSAL_WITH_PERSONAL_INTEREST"
  trigger:
    - "白御行提出『酒促姑娘』概念，並提醒不必只借觀止姑娘，可自組班底。"
  zhang_response:
    - "張麗華對自己養一班懂酒、懂客、能推酒的女人產生明確商業興趣。"
    - "她傾向先做小規模第一批，再看哪些人真的能提高酒水銷售。"
  route_rule_discussed:
    - "純酒促與妓女陪酒／接客應分開。"
    - "良家女子可做推酒、介紹、斟酒等酒坊工作；若進入本世界認定的妓業陪酒／接客，需處理相應妓籍法位。"
  not_yet:
    - "未正式成立酒促團隊。"
    - "未招募第一批人。"
    - "定陶商會未承諾投資。"
```

---

# 15｜蘇清：今晚出現但後段 UNKNOWN

```yaml
SUQING_LIU11:
  fixed_identity:
    - "蘇清為可自主接客／不接客、自己選男人的自由妓女；不是白御行可分配之普通姑娘。"

  observed:
    first:
      witness: "張麗華"
      time: "紅娘壓軸前"
      place: "前堂東側一帶"
      state:
        - "看見蘇清一人活動。"
    second:
      witness: "觀止跑堂"
      time: "紅娘散場後一陣"
      place: "由東側往後廊方向"
      state:
        - "看見蘇清一人往後廊走。"

  unknown:
    - "是否接客。"
    - "是否去白玉池。"
    - "是否找人、休息、回房或有其他私人安排。"
    - "不得因『十幾天沒接客』『有錢仍做妓女』推導她本夜一定缺男人。"
```

---

# 16｜小翠：正式重新入場之第一晚

```yaml
XIAOCUI_LIU11:
  observed:
    - "小翠確實下到大堂。"
    - "錦棠／白御行後來從樓上看到她與一名男客同桌說話。"
    - "小翠看來仍較拘謹，但有回話與笑，沒有被觀察到當場逃離。"

  unknown:
    - "該男客是否成為正式客人／付何種錢。"
    - "小翠後續是否接客、進房、性交或留宿。"
    - "不得由前一夜白御行私人正向成人經驗推導她已能接受所有男客。"
```

---

# 17｜白玉池：高級會員預約制已被潘金蓮接受

```yaml
WHITE_JADE_MEMBERSHIP_PLAN:
  state: "PAN_JINLIAN_ACCEPTED_FOR_LIU12_NIGHT_OPENING"
  purpose:
    - "不把白玉池當普通澡堂，而作稀缺、高級、私人雙人時段。"

  membership:
    security_deposit: "50兩"
    function:
      - "取得會員／預約資格。"
      - "不是一次性買女人或買終身使用權。"
    per_use_fee:
      state: "YES_BUT_AMOUNT_UNSET"
      note:
        - "潘金蓮明示每次使用仍另收費；本輪未定具體金額。"

  night_slots:
    groups_per_night: 4
    exclusivity: "每組獨佔一個時辰"
    reset:
      - "每組之間留清洗、換水、布巾／更衣與場地重置時間。"
      - "下一組進場時原則上看不到上一組留下的使用痕跡。"

  entry:
    single_person: "FORBIDDEN"
    party_size: 2
    companion_supply:
      - "觀止不替會員配女人／配伴。"
      - "會員必須自行邀到另一名願意共同入池的成年客人。"
    current_gender_rule:
      - "潘金蓮於現場將原提案的『必須帶女伴』收斂為『兩名成年客人共同入場』；不另管兩人關係／性別。"
    both_must_agree: true

  reservation:
    advance_booking: true
    walk_in_immediate_use: false
    no_queue_jump: true
    transfer_resale: "FORBIDDEN"
    note:
      - "有錢也不能現場拍五十兩要求立刻塞入時段。"

  daytime_internal_use:
    - "白天非營業時間留給觀止自己人使用，不與夜間會員四組名額競爭。"
    - "楊玉環可延續白天使用習慣。"
```

---

# 18｜楊玉環 × 白玉池既有使用與宣傳候選

```yaml
YANG_WHITE_JADE:
  prior_use:
    - "觀止歇業期間，楊玉環已近十日持續使用白玉池；玩家明示未開放期間她天天洗。"
  implication:
    - "她不是白玉池開放後才臨時試用的代言候選。"
  candidate_marketing:
    phrase: "楊貴妃第一指名"
    state: "PROPOSAL_PENDING_YANG_YUHUAN_CONSENT"
    possible_stage_use:
      - "可候選請楊玉環公開談實際使用感受／使用頻率。"
    forbidden:
      - "楊玉環本人尚未同意前，不得對外掛名。"
      - "不得先替她說『天天』作正式廣告台詞。"
```

---

# 19｜錦棠 × 白御行：公開／私人玩笑與同宿

```yaml
JINTANG_BAI_LIU11:
  relationship_dialogue:
    - "白御行表示錦棠若未來想勾其他男人，他不能把她綁住。"
    - "錦棠回答：她若真想看別的男人會自己去；今晚目前更想和白御行待在一起。"
    - "她表示若未來真看上別的男人，可以先告訴白御行；這是告知，不是請示。"
    - "以上不得推成她未來必然找別的男人或白御行已簽署任何永久開放關係契約。"

  future_star_jokes:
    - "二人談及錦棠若成為商會經紀約下的明星，公開戀情可能被外界解讀成會長潛規則旗下女明星。"
    - "『地下情』等語主要是二人當晚玩笑／風險討論，未形成正式公關契約。"

  overnight:
    - "榴月十一日晚，白御行與錦棠同宿。"
    - "玩家明示私人內容不說、不記。"
    - "SAVE 不推導當晚是否性交、具體身體行為、射精、避孕或其他未明示細節。"
```

---

# 20｜白御行、錦棠與潘金蓮之白玉池對話位置

```yaml
WHITE_JADE_RELATION_TO_PLAYER:
  confirmed:
    - "白御行與錦棠曾拿未來會員資格互相開玩笑，錦棠可自己訂時段再叫白御行陪。"
  not_completed:
    - "榴月十二日晚實際第一個預約人、使用人、付款人尚未成立。"
    - "不得因玩笑直接建立白御行／錦棠已訂首場。"
```

---

# 21｜仍然 UNKNOWN／OPEN

```yaml
OPEN_THREADS_V4_4:
  suqing:
    - "榴月十一日晚往後廊後的最終去向與夜生活。"

  xiaocui:
    - "與男客同桌後是否形成正式接客／進房／成人事件。"

  gusan_cisui:
    - "白御行一行離席後二人的後續；不得把外界腦補當真相。"

  li_qingzhao_guest_man:
    - "與談酒男客聊到何時、是否交換姓名／再約／私下同行。"

  four_guards_guest_trial:
    - "三十二娘、紅伶、明礬當晚與搭訕男客最後是否繼續、散席或另有安排。"

  prostitution_registration:
    - "三十二娘已決定要登妓籍，但尚未完成正式登記。"
    - "紅伶仍是偏向；明礬／白希未登。"

  li_qingzhao_registration:
    - "本夜未登妓籍。"

  liu_rushi:
    - "是否之後真的以既有妓籍掛牌／選男人，本 HOT 無觀察。"

  white_jade:
    - "榴月十二日晚會員制第一批四組預約名單。"
    - "每次使用費金額。"
    - "楊玉環是否同意『楊貴妃第一指名』與上台談使用感受。"

  zhang_lihua_promo_team:
    - "是否真的招募、商會是否投資、第一批人數與薪酬。"
```

---

# 22｜禁止倒灌與接關提醒

```yaml
DO_NOT_AUTO_RESOLVE:
  - "蘇清往後廊 != 去白玉池 != 接客 != 找男人。"
  - "小翠與男人同桌 != 已接客／已性交。"
  - "顧三與辭歲共處 != 戀愛／保護／性交。"
  - "六條、楊玉環收下趙受益轉贈身契 != 接受『愛』或承諾戀愛。"
  - "三十二娘想登妓籍 != 已完成登記。"
  - "紅伶偏向登妓籍 != 已完成登記。"
  - "李清照願意以女客看男人 != 已成妓女。"
  - "四大金剛作女客與男人聊天 != 在偷偷接客。"
  - "白玉池會員制被潘金蓮接受 != 榴月十二日晚已經完成第一組使用。"
  - "『楊貴妃第一指名』仍待本人同意，不能提前掛名。"
  - "白御行與錦棠同宿之私人內容由玩家明示不記，不得回填。"
```

---

# 23｜一句接關摘要

> **榴月十一日晚，觀止正式重新開幕：女子競技、賭盤、既有姑娘與商會培訓女人同時進場，紅娘以脫衣舞接公開成人自我慰藉高潮完成壓軸。白御行以客人身分開最大包廂，顧三與辭歲再會但舊日一炷香私事仍保持未知。白御行把楊玉環、六條正在使用的四張白御行側丫鬟身契，以總價二百兩賣給趙受益；趙受益付款後，兩張送六條、兩張送楊玉環，二女收下心意而未承諾『愛』。四大金剛與李清照其後以付費女客身分進大堂，被動回應搭訕且明示自己不是妓女；三十二娘確定想登妓籍，紅伶更偏向，明礬與白希不登，李清照本夜亦不登。蘇清只知前堂出現並在紅娘散場後獨自往後廊；小翠只知與一名男客同桌，後續均未知。潘金蓮接受白玉池五十兩會員押金、夜間四組、雙人預約、一組一時辰、中間清洗重置、禁止單人／插隊／轉售、白天自己人使用之方案，預定榴月十二日晚啟用；楊玉環此前近十日持續使用，但『楊貴妃第一指名』仍待本人同意。白御行與錦棠榴月十一日晚同宿，私人內容不記。現已榴月十二日白日。**
