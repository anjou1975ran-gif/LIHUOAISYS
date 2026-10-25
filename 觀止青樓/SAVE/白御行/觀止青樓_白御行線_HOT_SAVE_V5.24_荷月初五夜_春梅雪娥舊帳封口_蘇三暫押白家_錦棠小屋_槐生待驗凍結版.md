# 觀止青樓｜白御行線 HOT SAVE V5.24
## 理火三年荷月初五夜｜春梅×雪娥舊帳封口 × 孫雪娥白家掌灶方向 × 蘇三暫押白家 × 錦棠小屋構想 × 槐生租地到期待驗｜SAVE 凍結版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V5_24_HEYUE_CHUWU_NIGHT_SUN_CHUNMEI_CLOSURE_SUSAN_TEMP_CUSTODY_JINTANG_HOUSE_HUAISHENG_PENDING_FREEZE"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V5.24"
  record_type: "HOT_SAVE"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"

  previous_valid_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V5.23_荷月初五早間_四人同宿_潘金蓮追帳_巨床共居設計_舍方知邊界_匿名花魁故事凍結版.md"
    sha256_current_bytes: "e18cd8c7799a3d6489b0a5096cb9421737a18b3d4f7911b6fa7d75f51dff3616"

  current_master:
    file: "觀止青樓_白御行線_MASTER_SAVE_V5.18-HARD_全歷史自足_E01-E126_截至HOT_V5.18固化_保留V5.19-V5.21_HOT版.md"
    generation: "V5.18-HARD"

  current_rcl:
    file: "觀止青樓_白御行線_人物履歷_RCL_V5.18_MASTER_E01-E126_SCHEMA_V1.1_65人對齊版.md"
    generation: "V5.18 / schema V1.1"

  current_character_pool:
    file: "觀止人物卡池_LCAPG_V3.3.14_舍方知女性美女外型定錨_平胸視覺女性_65人對齊版.md"
    version: "V3.3.14 / 65"

  story_time:
    current_date: "理火三年荷月初五"
    exact_clock: "UNKNOWN"
    daypart: "夜間"

  current_scene_freeze:
    state: "STORY_FROZEN_BY_SAVE_COMMAND"
    location: "觀止後區／候交拘押區（本場口語稱『地牢』）"
    present:
      - "白御行"
      - "潘金蓮"
      - "顧仙娘"
      - "錦棠"
      - "蘇三／玉堂春"
    latest_observable:
      - "白御行已在蘇三暫押白家之具結字據上蓋章。"
      - "潘金蓮已同意今晚把蘇三交由白御行暫代看管；顧仙娘以管理見證立字。"
      - "顧仙娘已解除蘇三當下腳鐐／拘束；此舉不等於官府完整移轉已完成。"
      - "蘇三在官文辦妥前不得私自離開白宅；官府若要求驗人／退件／補件，白御行須依字據負責。"
      - "白御行與潘金蓮剛想起槐生一日租地試驗到期後的結果從未回去驗證。"
      - "下一步原意是回白家查看槐生是否仍可留在白家地界、被拉回沈家或出現其他結果；目前尚未出發、尚未驗證。"
      - "玩家此刻要求 HOT SAVE；故事於此凍結。"

  write_scope:
    hot_only: true
    master_write: false
    rcl_write: false
    character_pool_write: false
    core_write: false
    environment_write: false
```

---

# 0｜本次 HOT 性質

```yaml
V5_24_SCOPE:
  type: "INCREMENTAL HOT OVERLAY / V5.23 CHUWU MORNING WHITE-HOUSE FREEZE -> CHUWU NIGHT GUANZHI REAR HOLDING FREEZE"
  covers:
    - "V5.23 凍結後至荷月初五夜間已實際發生之薛嫂／孟玉樓牽線、錦棠訓練與觀止大堂觀察、轉圈遊戲、春梅×孫雪娥舊帳封口、潘×雪娥關係重估、蘇三／雪娥去向談判、白御行與兩女後區對話、蘇三暫押白家具結、錦棠小屋方向，以及槐生舊線重新被想起。"
    - "只保存已發生事件、人物明示、可觀察行動、付款／簽單／具結、知情來源、關係證據與 UNKNOWN / PENDING。"
  excludes:
    - "孫雪娥第一次錯誤重跑中之人格漂移內容；該段已由玩家 HOLD 判定污染，不進世界事實。"
    - "槐生租地到期後的任何結果；尚未回白家驗證。"
    - "蘇三官府完整移轉完成；目前只有暫押白家。"
    - "孫雪娥正式進白家；目前仍待官文／交割。"
    - "錦棠小屋正式設計、潘金蓮宣告、施工、完工或錦棠正式取得外室情人名分。"
    - "孟玉樓已接受初八邀請；目前只到薛嫂送話／等待回覆。"
    - "任何未成立之戀愛、忠誠、感恩、悔改或人物內心補完。"
```

> **LOCK：污染重跑不得雙軌存在；孫雪娥以本 HOT 所列重跑後反應為唯一 LIVE 版本。**

---

# 1｜荷月初五午後｜薛嫂 × 孟玉樓初八仕女夜牽線

```yaml
MENG_YULOU_BROKERAGE_CHUWU_V5_24:
  established:
    - "薛嫂向白御行帶來孟玉樓線索。"
    - "觀止 Route 開局中的孟玉樓目前為汴京靠行自由妓女，不固定隸屬單一妓院；可自行選場所／短租／靠行。"
    - "薛嫂初步描述：孟玉樓目前沒有丈夫控制，也沒有明顯偷情陷阱；不是急迫窮困型，會算帳。"
    - "薛嫂當時尚未直接問過孟玉樓本人。"
    - "白御行另付薛嫂五兩，請她轉話：荷月初八晚觀止仕女夜，可到私人房先喝酒、見面。"
    - "若孟玉樓願意，薛嫂可先陪第一輪作橋接，之後視兩人是否談得來退出。"
  pending:
    - "孟玉樓是否收到完整訊息 = PENDING。"
    - "孟玉樓是否願意來 = PENDING。"
    - "初八房間是否已正式保留 = NOT_ESTABLISHED。"
    - "婚配／納妾／成人關係／性服務／固定靠行均未成立。"
  lock:
    - "BROKER INTRODUCTION != MENG ACCEPTANCE"
    - "FIRST MEETING != MARRIAGE"
```

---

# 2｜時道人命籤｜孟玉樓婚配問題只作場景色彩

```yaml
MENG_FATE_SLIP_CHUWU_V5_24:
  white_question_direction:
    - "白御行曾向時道人問孟玉樓／婚配方向。"
  observed_text:
    - "花在別枝開，客從門外來。欲留先問價，兩意自安排。"
  treatment:
    - "道人只稱此籤為『平』。"
    - "『價』不被固定解讀為只有銀錢，也可由角色理解為價值／條件。"
    - "白御行當場評其為『廢話籤』方向。"
  lock:
    - "FATE SLIP != PROPHECY FACT"
    - "FATE SLIP != MENG FUTURE CONSENT"
```

---

# 3｜錦棠｜關盼盼訓練延續與今日身體控制練習

```yaml
JINTANG_TRAINING_CHUWU_V5_24:
  commercial_carry:
    - "錦棠既有24%可歸屬品牌淨利分潤繼續有效。"
    - "關盼盼此前測評指出錦棠習慣找『最好看的角度』、太知道自己被看；結論為『可以教』。"
    - "關盼盼正式課程費用／期數／付款方仍未最終簽定。"
  today_practice:
    - "白御行到錦棠處後，兩人以頭頂書本、頭髮自然放下練走路，目的在降低刻意擺姿。"
    - "另以地面繩線要求雙腳沿單一直線前進；白御行說明因錦棠未纏足，髖部可在腳線限制下自然產生擺動，不需刻意扭腰。"
    - "錦棠理解為：把頭／上身與腳步兩端約束，中段自然移動。"
  relation_tone:
    - "錦棠對白御行湖心島後少來看她有過帶刺玩笑／輕微不滿。"
    - "白御行今晚承諾主要陪錦棠、看場，不另辦其他事；此只建立當晚陪伴。"
  lock:
    - "TRAINING != ROMANTIC STATUS"
    - "24% SHARE != HOUSEHOLD RELATION"
```

---

# 4｜錦棠 × 白御行｜未來互綁遊戲只成立可撤回方向

```yaml
JINTANG_ROPE_GAME_DIRECTION_V5_24:
  established_speech:
    - "白御行以玩笑／調情提出未來可帶麻繩到錦棠房，試互相綁縛。"
    - "錦棠沒有拒絕概念，並反向提出也可能由她先綁白御行。"
    - "白御行提出『一條繩子、一個時辰、一個白御行』的互綁局。"
    - "錦棠明示『這個局，我接』，但同時說『不是今晚，今晚先看醉鬼』。"
  status:
    - "FUTURE_PLAYFUL_CONCEPT_ACCEPTED"
    - "DATE_NOT_FIXED"
    - "NO BLANKET CONSENT"
```

---

# 5｜觀止大堂醉客觀察｜錦棠把自然／表演差異連回訓練

```yaml
HALL_DRUNK_OBSERVATION_CHUWU_NIGHT_V5_24:
  setup:
    - "白御行與錦棠在觀止大堂樓上側包廂／欄邊觀察下方人群。"
    - "兩人以『自稱沒醉的人走直線』作觀察遊戲。"
  observed_examples:
    - "一名皮貨商醉漢自稱沒醉，甚至把花瓶認錯人；有人拿十兩賭他走十步直線。"
    - "醉漢只走出少量步數即偏線，現場客人與一名邊吃湯餅邊看熱鬧的觀止女子起鬨下注。"
    - "另有一名身形瘦高男子走得過度刻意：肩背、腳步與姿態都像精算過。"
    - "一名觀止女子自然蹲身撿物、隨手拉裙，反而讓錦棠覺得更好看。"
  jintang_takeaway_as_character_position:
    - "錦棠把『知道很多人在看時，身體會變得刻意』與關盼盼此前批評連起來。"
    - "她明示：以前會覺得瘦高男子很好看，現在反而覺得他『很累』。"
    - "她開始偏好未刻意表演的自然動作。"
    - "她明示坐在樓上看別人不知道自己被看時，較像『真的』。"
  lock:
    - "JINTANG TRAINING INTERPRETATION != UNIVERSAL BEAUTY FACT"
```

---

# 6｜紅娘加入｜十圈木棍轉圈賽形成現場遊戲

```yaml
SPIN_STICK_GAME_CHUWU_NIGHT_V5_24:
  host:
    - "紅娘被叫上樓，接手主持／改造玩法。"
  core_rules:
    - "參賽者低頭／額頭靠住木棍一端，繞棍轉十圈，再放手跑向觀止前門。"
    - "正式醉客版原則至少喝五碗酒。"
    - "紅娘把單棍改成兩支等長木棍，以便兩人同時轉圈。"
    - "可做參賽者直接賭與觀眾旁注。"
    - "撞壞姑娘桌椅、翻酒菜者照價賠。"
  no_house_rake_lock:
    - "截至本 HOT，沒有建立觀止官方抽水／固定莊家比例。"
  first_match:
    - "胖醉漢與瘦高商人曾形成對賽，但最終勝負在鏡頭轉移前未被可靠固化。"
```

---

# 7｜錦棠 × 紅娘示範賽｜錦棠窄勝

```yaml
JINTANG_HONGNIANG_EXHIBITION_V5_24:
  established:
    - "錦棠與紅娘進行不飲酒的十圈後跑門示範賽。"
    - "錦棠以極窄差距先到，約一指／一手幅級。"
    - "錦棠把勝負連回訓練：過去若急著找方向、急著走得漂亮，反而更可能偏；今日用較慢、較穩的腳步回正。"
    - "錦棠對白御行明示『今晚這個，算你有陪到我』。"
  lock:
    - "EXHIBITION WIN != PERMANENT SUPERIORITY"
```

---

# 8｜轉圈後互掌遊戲｜阿葵 × 小杏只成立一次自願比賽

```yaml
SPIN_SLAP_TEST_V5_24:
  setup:
    - "白御行提出找兩名彼此有嫌隙的成年女僕，轉十圈後各以一次巴掌作比賽。"
    - "紅娘找到後場成年女僕阿葵與小杏；兩人本來已有小摩擦／不對盤。"
    - "兩人均自行接受參與。"
  rules:
    - "只准一次巴掌。"
    - "揮空即算揮空，不得補第二下。"
    - "不得抱腿。"
    - "不得攻眼／咽喉等高危部位。"
  result:
    - "阿葵最後以擦中的一掌取得較明確命中結果。"
  later_jintang_view:
    - "錦棠認為玩法真正難點是轉完後辨認／找到對手，而不是單純打人。"
  lock:
    - "ONE VOLUNTARY GAME != GENERAL PERMISSION TO ASSAULT"
```

---

# 9｜春梅 × 孫雪娥｜舊西門宅報復帳正式封口

```yaml
CHUNMEI_SUN_OLD_FEUD_CLOSURE_V5_24:
  method:
    - "白御行要求潘金蓮分別私下問春梅與孫雪娥：是否願意參加『轉十圈後各打一巴掌』的公開清算局，以及各自願意把這一局算作什麼。"
    - "潘沒有先把一方答案告知另一方。"
  chunmei_position_before_bout:
    - "春梅表示：若今天還說孫雪娥欠她到現在，考慮到自己後來對雪娥做過的事，她自己也站不住。"
    - "她願意在今晚後不再以舊西門宅那筆帳作為日後針對孫雪娥的理由。"
    - "未來若有新衝突，按新事另算。"
  sun_position_before_bout:
    - "孫雪娥明示三十棍與被賣都不是一巴掌能抹掉；她不把參賽理解成歷史沒發生。"
    - "她願意不再把後半輩子耗在春梅舊帳上。"
    - "她要求春梅不得再以觀止管理權／人手，拿舊西門宅事情作為報復她的理由。"
  bout:
    - "潘金蓮當場說明十圈、各一掌、不補第二下；事後不得再以舊互相帳報復，但不代表忘掉歷史。"
    - "兩人開始前仍可退出；二人均不退出。"
    - "轉圈後，孫雪娥藉喊『春梅』與聲音定位，先打中春梅一掌；春梅其後也回中一掌。"
    - "本局沒有宣告勝負。"
  closure_speech:
    - "春梅明示：『西門家那筆，我不再找妳。』"
    - "孫雪娥明示：春梅後來打她／賣她之事她也不再用作未來報復理由；但她沒有忘。"
    - "雙方確認：日後若再互相得罪，就是新的事。"
  relation_state_after:
    old_feud_as_active_retaliatory_account: "CLOSED_BY_MUTUAL_CHOICE"
    history_erased: false
    forgiveness_established: false
    friendship_established: false
    future_new_conflict_possible: true
```

---

# 10｜潘金蓮 × 孫雪娥｜舊怨重新分級，不再被潘當成同級終身大敵

```yaml
PAN_SUN_REFRAME_V5_24:
  white_argument:
    - "白御行指出：潘金蓮與吳月娘才是舊西門宅上層妻妾／主妻權力軸；春梅是潘的貼身人，孫雪娥亦有較低階起點。"
    - "白御行認為若潘今日仍把孫雪娥當與自己同級的最大仇家，反而把自身位階做小。"
  pan_response:
    - "潘金蓮承認這個結構判讀大致成立。"
    - "她沒有否認自己與孫雪娥曾直接互打、互恨、互相揭舊事。"
    - "她承認其中很大一部分是西門宅派系／站隊造成的長期衝突。"
    - "潘表示不需再為孫雪娥另開一場公開大清算；若仍有殘餘直接帳，她可自行處理。"
  state:
    - "PAN-SUN HISTORY REMAINS"
    - "PAN-SUN ARCHENEMY-LEVEL ACTIVE ACCOUNT REDUCED / RECLASSIFIED"
  lock:
    - "RECLASSIFICATION != HISTORY DENIAL"
    - "RECLASSIFICATION != FRIENDSHIP"
```

---

# 11｜潘金蓮 × 吳月娘｜主軸舊帳仍在，沒有替潘自動完成

```yaml
PAN_WU_DIRECTION_V5_24:
  established_speech:
    - "白御行表示若潘金蓮日後要處理吳月娘舊帳，自己站潘這邊。"
    - "潘沒有要求白御行替她直接處置吳月娘。"
    - "潘當場方向不是單純打一頓／毀掉吳月娘；她更在意有一天讓吳月娘失去『西門家大娘子』護罩後，以本人位置坐下來面對她。"
  status:
    - "DIRECTION / CHARACTER POSITION ONLY"
    - "NO ACTION PLAN"
    - "NO RETALIATION EXECUTED"
```

---

# 12｜孫雪娥 × 白御行｜V5.20 條件式收留推進為「白家掌灶」具體方向

```yaml
SUN_WHITE_HOUSE_COOK_DIRECTION_V5_24:
  predecessor:
    - "V5.20 白御行曾條件式承諾：待孫雪娥與西門府舊帳清、潘方願意放／賣、價格合理時，可以『收她』。"
    - "V5.20 當時未固定『收』是奴、妾、廚娘、床伴或其他位置。"
  now_established:
    - "春梅在本輪確認：孫雪娥當時確曾表示在條件成立時願意進白家，並曾以掌灶、大宅多人飯菜、廚房偷拿／調度等能力向白御行推銷自己。"
    - "春梅與孫雪娥舊帳封口後，春梅明示若白御行照程序收孫雪娥，她沒有舊帳異議。"
    - "白御行本輪明示：自己要孫雪娥進白家後作掌灶／掌杓丫環，理由之一是白家需要可靠廚房人手。"
    - "孫雪娥在後區談話中明示願意做掌灶／廚房管理方向，包含做飯、看灶、盯採買／偷拿等。"
  shishi_pregnancy_knowledge:
    - "白御行在潘金蓮直接在場時，以李師師懷孕作為白家需要廚房人手的理由之一。"
    - "潘金蓮當場反應顯示她因此取得『李師師有喜』知情。"
    - "本 HOT 不因其他人可能在附近，自動擴散完整孕情知情名單。"
  status:
    - "FUTURE WHITE-HOUSE COOK / HEAD-KITCHEN DIRECTION ACCEPTED IN SPEECH"
    - "LEGAL TRANSFER NOT COMPLETE"
    - "WAGES / EXACT SERVANT CONTRACT / DETAILED AUTHORITY NOT FIXED"
    - "NO CONCUBINE STATUS"
```

---

# 13｜白御行私人五萬兩 × 潘金蓮｜用途方向更新為蘇三＋孫雪娥程序池，實際支出仍須按真帳

```yaml
PRIVATE_50K_POOL_UPDATE_V5_24:
  predecessor:
    - "V5.22 已確認白御行私人五萬兩實際送達潘金蓮並取得簽收回單。"
    - "V5.22 當時特別鎖定：不得自動把該筆五萬兩核銷成蘇三法定移轉費。"
  now_established_direction:
    - "白御行本輪明示：這筆私人五萬兩可由潘金蓮拿來辦蘇三與孫雪娥的實際合法程序／移交支出。"
    - "白御行明示：實際程序費用按真實發生記；不是為了湊五萬而製造假官費。"
    - "完成兩人實際合法程序後若有餘額，白御行不要求退還；餘額可作潘金蓮個人所得／私人贈與。"
    - "潘金蓮接受此結構，並區分：觀止只記觀止實收／實辦；餘額私人贈與不是觀止營收、不是蘇三價格、不是孫雪娥價格、也不是假官費。"
  status:
    delivered_to_pan: true
    exact_susan_cost: "UNKNOWN"
    exact_sun_cost: "UNKNOWN"
    exact_remainder: "UNKNOWN"
    full_legal_transfer_both: false
  lock:
    - "PRIVATE GIFT != GUANZHI REVENUE"
    - "BUDGET POOL != FIXED OFFICIAL FEE"
    - "MONEY != CONSENT"
```

---

# 14｜孫雪娥後區談話｜人格漂移重跑後唯一合法 LIVE 版本

```yaml
SUN_REAR_HOLDING_CANONICAL_RERUN_V5_24:
  corruption_exclusion:
    - "早先一輪導演曾把孫雪娥寫成以現代尊嚴式語言拒絕權力／寧可失去出路也不低頭；玩家 HOLD 指出人物漂移。"
    - "該錯誤輪中『現在還不是主子』『十年也教不出來』『只要會跪的就不用接我』等反應全部隔離，不取得世界事實。"
  canonical_sequence:
    - "白御行告知孫雪娥：潘金蓮舊帳已由自己出面壓平；春梅舊帳亦已停止作未來報復理由。"
    - "白御行以非常嚴厲語氣訓斥孫雪娥不要把舊四娘架子帶入新主家，並明示自己可以幫她，也可以抽手。"
    - "孫雪娥在重新判斷權力位置後實際跪下。"
    - "她承認自己剛看見出去的可能，就又把舊四娘架子搬出來，並收回先前要求體面車馬的話。"
    - "孫雪娥在對話中第一次直接稱白御行『主子』，並表示自己知道未來靠誰吃飯／靠誰把她從當前處境帶出去。"
  legal_lock:
    - "SUN VERBALLY CALLS WHITE 'MASTER' != LEGAL TRANSFER COMPLETE"
    - "CURRENT LEGAL OWNER / EXACT DOCUMENT STATUS STILL PENDING"
```

---

# 15｜孫雪娥偷財私奔舊習警告｜白御行設白家硬紅線，雪娥明示接受

```yaml
SUN_THEFT_ELOPEMENT_WARNING_V5_24:
  white_warning:
    - "白御行嚴厲指出：孫雪娥曾有拿家中財物與男人私奔的舊行為；有過一次就可能再犯。"
    - "白御行明示：若她日後進白家又拿白家銀錢／財物養外頭男人、再次私奔，後果會極重。"
  sun_response:
    - "孫雪娥沒有否認自己曾拿財物／跟男人走。"
    - "她明示：日後若進白家，白家的銀子、首飾、貨與帳，不是她的就不碰。"
    - "她明示：即使日後看上別的男人，也不能拿主家的錢替外人養膽。"
    - "若有一天真不想待白家，她表示會先來與白御行說，不以偷錢逃走作第一手段。"
  lock:
    - "CURRENT PROMISE != GUARANTEED FUTURE LOYALTY"
    - "WARNING != FUTURE PUNISHMENT ALREADY OCCURRED"
```

---

# 16｜顧仙娘 × 孫雪娥｜官文前數日管理與之後送白家方向

```yaml
SUN_PRETRANSFER_MANAGEMENT_V5_24:
  white_request:
    - "白御行請顧仙娘在官文未完成的最後幾日多看著孫雪娥。"
    - "白御行說潘金蓮若仍要發脾氣，可讓雪娥做苦／髒／不受歡迎的工作；若雪娥真犯錯需打罰，請顧仙娘下手留分寸，看白御行面子。"
  gu_response_and_boundary:
    - "顧仙娘接受在現有合法管理範圍內派活／處置。"
    - "她不把潘金蓮舊仇本身當成新刑名，也不承諾為買家製造傷害。"
    - "若真有應罰違規，她自行按當前規矩處理，不故意往重裡整。"
  transfer_direction:
    - "官文可合法完成時，白御行要求先讓孫雪娥沐浴、更換乾淨衣物，再派人送白家。"
    - "白御行指定到白家後由李瓶兒接收／安排其廚房工作。"
  pan_sun_or_pinger_sun:
    - "白御行對孫雪娥說：她與李瓶兒若仍有舊西門宅恩怨，進白家後由兩人自己處理；這將是白家內部帳，不再拿觀止／舊宅外人作權力槓桿。"
    - "孫雪娥表示不把潘、春梅、月娘等舊人拉來替自己撐腰；若與李瓶兒有帳，會自己面對。"
  status:
    - "SUN STILL AT GUANZHI / CURRENT HOLDING"
    - "WHITE-HOUSE TRANSFER PENDING OFFICIAL PAPER"
```

---

# 17｜蘇三塞襪連續性｜今晚實際取出口中，過去連續時長不回填

```yaml
SUSAN_SOCK_CONTINUITY_CLOSE_V5_24:
  predecessor:
    - "V5.20 只成立白御行下令把自己的襪子塞蘇三口中、顧仙娘原則接受；當時物理執行是否完成為 PENDING，禁止回填。"
  tonight_observable:
    - "本輪蘇三被帶出來見白御行時，口中實際有襪子。"
    - "顧仙娘表示白御行本人已到、蘇三需要開口談話，因此當場把襪子取下。"
    - "蘇三取下後能正常說話。"
  lock:
    - "TONIGHT OBSERVABLE SOCK IN MOUTH != PROOF IT REMAINED CONTINUOUSLY FOR ALL PRIOR DAYS"
    - "PAST DURATION REMAINS UNKNOWN"
```

---

# 18｜蘇三 × 白御行｜五萬簽單、官文等待與『別喊冤』要求

```yaml
SUSAN_TRANSFER_TALK_CHUWU_NIGHT_V5_24:
  receipt_evidence:
    - "白御行把潘金蓮已簽收私人五萬兩的簽單實際拿給蘇三看。"
    - "蘇三因此取得：白御行所說五萬兩確已付到潘方之直接可見證據。"
  white_statements:
    - "白御行明示：蘇三現在自己做不了官府程序，他也只能等官府流程。"
    - "白御行聲稱自己能讓官府流程跑快或跑慢；此句保存為白御行自述／施壓語言，不自動證成其對所有官府流程有無限控制權。"
    - "白御行明示：塞襪其中一個目的，是要蘇三學會不要在他面前反覆喊冤。"
  susan_response:
    - "蘇三理解：她不能靠重複喊冤使官文照自己意思走。"
    - "她表示可以等、可以在白御行面前不再反覆喊冤。"
    - "她同時沒有改口承認自己有罪；她仍區分『不再對白御行喊冤』與『認為判決正確』。"
  lock:
    - "SILENCE ABOUT INNOCENCE CLAIM != CONFESSION"
    - "WHITE CLAIMS INFLUENCE != OBJECTIVE TOTAL CONTROL OF GOVERNMENT"
```

---

# 19｜錦棠 × 蘇三互看｜花魁自我表演與『自然好看』訓練交叉

```yaml
JINTANG_SUSAN_MUTUAL_LOOK_V5_24:
  setup:
    - "白御行讓錦棠與蘇三互相端詳外貌／姿態。"
  susan_view:
    - "蘇三明示錦棠漂亮，但認為兩人不是同一路數。"
    - "蘇三以自身花魁經驗說：自己以前要做到一進門就先被看、坐下後仍讓人記得。"
    - "她觀察錦棠不刻意站好／不知道正在被挑姿勢時反而更好看。"
    - "她不承認自己作花魁會輸，但承認白御行眼光不差。"
  jintang_view:
    - "錦棠認為蘇三非常知道自己哪個角度好看，像自己過去被關盼盼指出的舊習。"
    - "錦棠把此觀察連回『不刻意讓人看，也能好看』的訓練方向。"
  lock:
    - "MUTUAL BEAUTY JUDGMENT = CHARACTER OPINION"
```

---

# 20｜錦棠 × 蘇三談青樓愛情與帳｜浮香是匿名故事的合法轉述來源

```yaml
JINTANG_SUSAN_LOVE_ACCOUNT_TALK_V5_24:
  continuity_patch:
    - "V5.23 的匿名花魁故事原本由白御行在白家巨床區講給李師師、浮香、舍方知；錦棠當時不在場。"
    - "本輪合法補足來源：其後浮香私下聊天時，曾把該『不具名花魁＋男人花巨款』故事與其中『花錢不等於共同未來』的討論轉述給錦棠。"
    - "浮香與錦棠均未因此取得『匿名花魁 = 蘇三／玉堂春』知情。"
  jintang_position:
    - "錦棠明示：她相信青樓裡可能遇到真心，但不能只靠男人在青樓裡花錢／爭風／說要贖人，就把未來自動補成真愛結果。"
    - "她以自己的24%分潤作例：白御行對她再好、哪怕未來感情更深，也不能因此少算她應得的分成。"
    - "她認為感情與利益必須分軸；越想長久，越要談清錢、贖身、住哪裡、誰承擔什麼。"
    - "她明示：男人可以算帳，女人也可以算；『自己人』反而更該把帳說清楚。"
  susan_learning_as_speech:
    - "蘇三開始區分：男人花過三萬兩、願意出頭、很想要她，可以各自是真的；但不能因此自動追加『會跟她過一輩子』。"
    - "蘇三問了多個延伸問題，包括男人沒錢、感情會變、女人能否欺騙、共同未來需要哪些具體承擔。"
  lock:
    - "CHARACTER DISCUSSION != OBJECTIVE THEORY OF LOVE"
```

---

# 21｜白御行 × 蘇三｜多重動機、投資框架與白御行自述的留人標準

```yaml
WHITE_SUSAN_INVESTMENT_RELATION_TALK_V5_24:
  white_multi_motive_statement:
    - "面對蘇三問『五萬兩是在救我還是在買我』，白御行拒絕二選一。"
    - "他明示：愛她可以成為買她的理由，想整她也可以成為理由，甚至可能因將來拋棄她而先買她；多個動機可以同時存在。"
    - "白御行要求蘇三不要執著猜他當下唯一內心，而是思考自己想成為怎樣的結果。"
  investment_statement:
    - "白御行明示：自己已為蘇三付出成本；若最終棄養，對白御行也是投資失敗，蘇三也得不到好處。"
    - "他認為若蘇三能讓自己覺得這筆投入成功，就不會輕易把成功投入變成失敗。"
  white_success_criteria_as_speech:
    - "不要背叛。"
    - "不要製造麻煩。"
    - "不要自以為是。"
    - "不要求蘇三替他賺大錢。"
    - "至少希望覺得這個女人能跟他說心裡話。"
  communication_rule:
    - "白御行明示：能說心裡話不等於公開讓他丟面子；要懂人心人情、分場合與說法。"
    - "若蘇三已私下勸過而白御行不聽，可找另一個更能讓白御行聽進去的女人繼續勸。"
    - "若已提醒、找人再提醒而白御行仍決定照做，蘇三之責任可到此；她可以為真的出事預作自保。"
    - "反過來若蘇三做蠢事，白御行明示自己比較懶，只提醒一次，聽不聽由蘇三自己負責。"
  lock:
    - "WHITE PERSONAL RELATION PHILOSOPHY != WORLD LAW"
    - "PAST COST != OWNERSHIP OF CONSENT"
```

---

# 22｜蘇三主動開價｜第一志願為妾，第二志願為有房有月錢的內宅女管事

```yaml
SUSAN_PREFERRED_WHITE_HOUSE_POSITION_V5_24:
  opportunity:
    - "白御行給蘇三一次機會：可從正妻到劈柴丫環之間自己提出想要的位置；白御行會考慮，但最終位置由他決定。"
  susan_first_choice:
    - "蘇三明示不會在當下腳上剛解鐐時直接討正妻；她認為那會落回自以為是。"
    - "她也明示不希望只作劈柴／挑水等無名粗使丫環。"
    - "她第一志願開價為『妾』：要有名分、有自己的房、有月錢、有事情做，不再接外客；但不要求一進門就壓過李師師／李瓶兒等既有人。"
  susan_second_choice:
    - "若妾位不給，她第二志願為有自己房、有月錢、不接外客的內宅女管事。"
  status:
    - "SUSAN REQUEST / PREFERENCE ONLY"
    - "WHITE HAS NOT ACCEPTED CONCUBINE TITLE"
    - "NO WHITE-HOUSE POSITION FINALIZED"
```

---

# 23｜錦棠被問若明日進白家要什麼｜先要獨立空間與帳，不先要夫人順位

```yaml
JINTANG_PREFERRED_HOUSE_MODEL_V5_24:
  jintang_initial_answer:
    - "錦棠若假設明日進白家，第一優先不是正妻／第幾房，而是自己的房、能鎖門、自己的衣物／首飾／帳本空間。"
    - "她明示自己的24%分潤仍是自己的商業帳，不因住進白家就自動變成白家錢。"
    - "她希望仍保有走台、訓練、商業工作，不要因住進白家就只剩『白御行第幾個女人』。"
    - "她當下不要求立刻取得夫人／幾房名分。"
  independence_logic:
    - "錦棠明示：若有一天白御行真的叫她走，感情上她可能難過，但自己有錢、有工作，就不至於連飯都沒得吃。"
  relation_lock:
    - "HYPOTHETICAL HOUSE POSITION != JINTANG AGREES TO MOVE IN TOMORROW"
```

---

# 24｜白家既有空間模型 × 錦棠小屋｜只到草圖／用途需求，未宣告施工

```yaml
JINTANG_SMALL_HOUSE_CONCEPT_V5_24:
  verified_existing_white_house_baseline:
    - "較早 MASTER 已建立：白家主樓為核心居所；李師師、李瓶兒同階如夫人；張麗華有獨立外院與酒窖；浮香有獨立小居。"
  white_current_description:
    - "白御行把張麗華／浮香的外院小居模型拿來給錦棠理解：白家內部可承認一個位置，但不必在主樓夫人順位中排名。"
    - "白御行形容張麗華在外以酒莊老闆娘身份生活，白家內部有其私人位置；此處的精確對外稱謂／權利以既有 MASTER 與未來正式文件為準，不單靠本次口述改寫。"
  jintang_response:
    - "錦棠對『不排名、有自己的營生、白家有自己的小屋』模型明顯較有興趣。"
    - "她沒有正式接受『外室情人』作已成立關係；只表示該模型比直接排幾房更接近自己想要的生活。"
  rough_sketch:
    - "錦棠當場用紙／炭筆畫過一張粗略小屋草圖。"
    - "她想要：不太大的獨院、可坐回廊、正屋、放布料／鞋／首飾／帳本的偏房、能拉線練步子的長形空地、小型藏酒處，以及一個方便自己安靜進出的後門方向。"
    - "她要求若真蓋，該屋是她在白家的明確私人空間，不是臨時賞住一晚的空房。"
  pan_response:
    - "潘金蓮看到粗圖後以玩笑嫌其畫得歪，沒有直接依草圖宣告施工。"
    - "潘金蓮確認白宅租約／空間框架原本已有後院增建方向。"
    - "白御行決定先找人把圖畫成詳細設計，再讓潘金蓮正式宣告。"
  status:
    - "ROUGH SKETCH EXISTS"
    - "DETAILED ARCHITECTURAL PLAN PENDING"
    - "PAN FORMAL DECLARATION PENDING"
    - "NO CONSTRUCTION"
    - "NO COST"
    - "NO JINTANG MOVE-IN"
```

---

# 25｜潘金蓮到後區｜願意今晚放蘇三，但完整官文尚未辦妥

```yaml
PAN_SUSAN_RELEASE_WILL_V5_24:
  white_request:
    - "白御行直接問潘金蓮：是否願意今晚就讓自己帶走蘇三。"
  pan_response:
    - "潘金蓮明示自己願意放蘇三，不想因文書等待多養／多管幾日。"
    - "她同時區分：自己願意放 != 官府完整移轉已完成。"
    - "只要顧仙娘能把今晚先行轉到白家看管作成合法可執行的暫交，她願意簽。"
  gu_initial_position:
    - "顧仙娘表示需以現有文書與可執行暫押方式處理，不能把完整移轉說成已完成。"
```

---

# 26｜蘇三暫押白家具結｜潘簽、顧見證、白御行蓋章，今晚可帶走

```yaml
SUSAN_TEMP_WHITE_HOUSE_CUSTODY_V5_24:
  white_proposal:
    - "白御行提出現在立字據：官府文件辦妥前，由自己把蘇三帶回白家暫代看管；蘇三不得離開白家半步。"
  gu_terms:
    - "字據不得寫成『蘇三已完整歸白家』。"
    - "只寫官文未完期間由白御行暫代看管。"
    - "蘇三不得私自離開白宅。"
    - "白家不得把蘇三再轉交第三方、帶出城、藏匿，或在官府要求驗人時交不出人。"
    - "官文若退件／需補件／要求蘇三回到原管理端，暫押字據不會自動變成永久移交。"
  signatures:
    - "潘金蓮已在交方／同意端落名。"
    - "顧仙娘已以管理見證方立字。"
    - "白御行已蓋章／具結。"
  physical_result:
    - "具結完成後，顧仙娘已解除蘇三當下腳鐐／拘束。"
    - "蘇三目前可隨白御行離開觀止前往白家，但仍受暫押條款拘束。"
  legal_status:
    full_official_transfer_complete: false
    temporary_custody_to_white_house: true
    susan_may_leave_white_house_before_official_completion: false
  lock:
    - "TEMPORARY CUSTODY != OWNERSHIP"
    - "REMOVAL OF SHACKLES != LEGAL FREEDOM"
    - "TEMPORARY TRANSFER != ADULT / RELATIONAL CONSENT"
```

---

# 27｜槐生／十一哥舊線被重新想起｜只恢復 PENDING，不自動生成鬼的現況

```yaml
HUAISHENG_GHOST_THREAD_REOPENED_V5_24:
  hard_predecessor:
    - "MASTER E121 已建立：沈家可顯影來源『槐生』在沈家外緣會被拉扯／變淡／難越界。"
    - "白御行曾以100兩向觀止／潘金蓮方向成立一日臨時租地安排，並給槐生進白家許可。"
    - "一日租地成立後，槐生可跨過先前邊界進入白家地界；到白家更外側／外門附近又出現手淡、腳步受拉。"
    - "MASTER 已明鎖：租約到期時槐生會發生什麼 = PENDING。"
    - "十一哥則為另一條來源：依沈家左牆／觀止正門『兩處一門』接觸結構出聲／互動；不得與槐生合併。"
  tonight_recollection:
    - "白御行在談錦棠小屋／白家地界時突然想起槐生試驗。"
    - "潘金蓮也確認：兩人此後沒有回去完成『租約到期後』驗證。"
    - "潘金蓮當場回想100兩一日租地費原約次日上午於白家付款，但本輪沒有查帳完成，故付款完成與否仍依舊證據／帳冊待查。"
  current_unknowns:
    - "槐生目前是否仍在白家地塊 = UNKNOWN。"
    - "租約到期後是否被拉回沈家 = UNKNOWN。"
    - "是否卡在邊界／另有顯影結果 = UNKNOWN。"
    - "本輪尚未回白家檢查。"
  next_scene_direction:
    - "SAVE 解除後，白御行原意為帶蘇三、錦棠等返白家，順道檢查槐生租地到期後的可觀察結果。"
  lock:
    - "REMEMBERING THE THREAD != RESULT"
    - "GHOST LABEL != MECHANISM PROVEN"
```

---

# 28｜當前人物知情與關係重點

```yaml
KNOWLEDGE_RELATION_SNAPSHOT_V5_24:
  sun_xuee:
    knows:
      - "春梅舊帳已互相封口，不作未來報復理由。"
      - "潘金蓮方向由白御行出面處理，潘已願意放她往白家方向走。"
      - "白御行要她未來作白家掌灶／掌杓方向。"
      - "官文未完成前仍要留觀止管理端做事。"
    does_not_yet_have:
      - "完整官府移轉完成"
      - "正式白家僱用／奴契最終文本"
      - "固定月錢／完整權限"

  susan:
    knows:
      - "白御行私人五萬兩已實際給潘金蓮，且看過潘簽收回單。"
      - "潘金蓮今晚願意放她作暫押白家。"
      - "白御行已具結；她官文完成前不得離白宅。"
      - "她可以提出白家位置偏好，但最終由白御行決定。"
    identity_claim:
      - "她仍保留對殺人案的喊冤／自我無罪主張；本輪不因少喊冤而改成認罪。"

  jintang:
    knows:
      - "今晚看過孫雪娥與蘇三在權力／去向未定時的不同反應。"
      - "浮香曾向她轉述白家床上談過的不具名花魁故事，但不知道主角是蘇三。"
      - "白家已有主樓＋麗華外院＋浮香小居等分層空間模型。"
      - "白御行允許她先畫自己的小屋需求，正式設計與潘宣告待後續。"
    not_established:
      - "錦棠已正式搬入白家"
      - "錦棠已接受外室情人名分"
      - "錦棠小屋已施工"

  pan_jinlian:
    knows:
      - "李師師有喜，由白御行本輪直接說出。"
      - "春梅×孫雪娥舊帳已封口。"
      - "白御行打算把孫雪娥帶入白家掌灶。"
      - "蘇三今晚暫押白家字據已成立。"
      - "槐生一日租地到期後結果還沒驗。"
```

---

# 29｜主要未決事項

```yaml
PENDING_LEDGER_V5_24:
  susan:
    - "完整官府移轉尚未完成。"
    - "今晚已可依具結暫押白家；尚未實際走出觀止／到達白家。"
    - "白家最終身分：蘇三本人第一志願妾、第二志願內宅女管事；白御行尚未決定。"
    - "殺人案客觀真相／冤情仍未由本 HOT 判定。"

  sun_xuee:
    - "完整官文／身籍／交割仍未完成。"
    - "白家掌灶方向已談清，但月錢、權限、契約細節未固定。"
    - "官文完成後預定先沐浴更衣，再送白家由李瓶兒接收；尚未執行。"

  meng_yulou:
    - "薛嫂送初八仕女夜喝酒見面邀請結果 PENDING。"

  jintang:
    - "關盼盼課程費／期數／付款方仍待定。"
    - "未來互綁遊戲已接局但日期未定。"
    - "小屋詳細設計、潘正式宣告、施工與費用全 PENDING。"
    - "外室情人／白家內部位置尚未正式成立。"

  chunmei_sun:
    - "舊帳作未來報復理由已 CLOSED。"
    - "兩人並未和解成朋友；未來新衝突照新事另算。"

  pan_wu:
    - "舊宅主軸未決；潘沒有授權白御行替她自動處理。"

  huaisheng:
    - "一日租地到期後結果 PENDING。"
    - "100兩租地費原約次日上午白家付款；本輪未翻帳確認。"
    - "下一幕預計回白家實地確認，但尚未發生。"

  shishi_pregnancy:
    - "李師師妊娠已確認、本人留胎。"
    - "潘金蓮本輪已由白御行直接取得知情。"
    - "不自動擴散到所有觀止人物。"

  white_private_50k:
    - "款已給潘金蓮。"
    - "實際蘇三／孫雪娥程序支出與最終私人贈與餘額尚未結算。"

  giant_bed_house_projects:
    - "V5.23 的共居廳家具／寢具等未決事項繼續有效，除非後續另有完成證據。"

  public_business_threads:
    - "V5.23 以前未結之其他商會、觀止、紅娘、失仙、王婆王六兒、蘇清等線均未因本 HOT 自動關閉。"
```

---

# 30｜最新接關座標

> **時間：理火三年荷月初五夜間；精確時刻 UNKNOWN。**
>
> **地點：觀止後區／候交拘押區（本場口語稱「地牢」）。**
>
> 今晚大堂先有醉客走線、十圈木棍跑門、錦棠×紅娘示範與阿葵×小杏一掌遊戲。白御行其後把這個形式變成春梅×孫雪娥的舊帳清算台：潘金蓮分別問過兩人，兩人都同意參與，但都拒絕把一巴掌寫成歷史消失。兩人各打一掌後，明示舊西門宅互相報復帳到此停止；歷史、受辱、三十棍與轉賣都沒有被抹掉，日後若再衝突按新事另算。
>
> 潘金蓮其後接受白御行對潘×孫雪娥舊怨的重新分級：潘與雪娥確有直接舊仇，但不再把雪娥當與自己同級的終身大敵。白御行同時把孫雪娥的舊「收妳」方向具體化成白家掌灶／掌杓；孫雪娥在重跑後的合法版本中，面對白御行嚴厲訓斥重新判斷權力位置，實際跪下、第一次直接稱白御行「主子」，並明示不再拿四娘舊架子討車馬。她也被白御行嚴厲警告不得再拿主家錢財跟男人私奔，口頭接受此紅線。她目前仍留在觀止管理端等官文，未正式進白家。
>
> 蘇三今晚被帶出時口中實際有襪子，顧仙娘因白御行本人到場、需要對話而當場取下；這只證明今晚現況，不回填前幾日是否一直塞著。白御行拿出潘金蓮已簽收私人五萬兩的回單給蘇三看，並要求她別在自己面前反覆喊冤；蘇三接受少喊／等待官文，但沒有改口認罪。她與錦棠其後長談青樓愛情、分潤、利益、共同未來與自己該成為怎樣的人。錦棠引用匿名花魁故事的合法來源校正為「浮香後來私下轉述」，錦棠仍不知道匿名花魁就是蘇三。
>
> 白御行給蘇三一次開價白家位置的機會。蘇三第一志願為妾：有名分、自己的房、月錢、事情做、不接外客；第二志願為有房有月錢、不接外客的內宅女管事。白御行沒有當場答應哪個位置。錦棠被問同題時，反而先要自己的房、自己的帳與自己的事業，不急著排夫人順位。她畫了一張粗略小屋草圖；潘金蓮只把增建方向記下，要求日後先做正式細圖再宣告，尚未施工。
>
> 潘金蓮最後明示願意今晚放蘇三。因官文完整移轉尚未辦妥，白御行改立暫押具結：官文完成前蘇三由白御行帶回白家看管，不得私自離開白宅；官府若要求驗人／補件，白御行負責交人。潘金蓮落名、顧仙娘見證、白御行已蓋章。顧仙娘隨後已解除蘇三當下拘束。**蘇三尚未實際走出觀止、尚未抵達白家。**
>
> 蓋章後，白御行因談到白家地界突然想起槐生。較早 MASTER 已確認槐生在一日租地成立時能跨入白家地界，但租約到期後究竟會被拉回沈家、留在白家、卡在邊界或出現別的結果一直 PENDING。潘金蓮也承認兩人後來沒有回去驗。**此刻尚未回白家看鬼；下一幕才準備去驗。**

---

# 31｜VALIDATION V5.24

```yaml
VALIDATION_V5_24:
  story_frozen: true
  predecessor: "PASS / HOT V5.23"
  hot_only_write: true
  master_updated: false
  rcl_updated: false
  character_pool_updated: false

  current_date: "理火三年荷月初五"
  current_daypart: "夜間"
  current_location: "觀止後區／候交拘押區"

  sun_bad_rerun_pollution_saved: false
  sun_canonical_rerun_saved: true
  sun_called_white_master_in_speech: true
  sun_legal_transfer_complete: false
  sun_white_house_cook_direction_established: true

  chunmei_sun_old_retaliation_account_closed: true
  chunmei_sun_history_erased: false
  chunmei_sun_friendship_established: false

  pan_sun_old_archenemy_account_reclassified: true
  pan_wu_final_plan_established: false

  private_50k_delivered_to_pan: true
  private_50k_actual_legal_cost_breakdown_complete: false
  private_50k_remainder_known: false

  susan_sock_present_tonight_observed: true
  susan_sock_continuous_prior_duration_backfilled: false
  susan_innocence_claim_withdrawn: false

  susan_preferred_concubine_position_requested: true
  susan_final_white_house_position_granted: false

  jintang_small_house_rough_sketch_exists: true
  jintang_small_house_formally_declared: false
  jintang_small_house_construction_started: false
  jintang_outer_lover_relation_established: false

  susan_temp_custody_document_signed_by_pan: true
  susan_temp_custody_witnessed_by_gu: true
  susan_temp_custody_stamped_by_white: true
  susan_restraints_removed_after_document: true
  susan_full_official_transfer_complete: false
  susan_has_physically_arrived_white_house: false

  huaisheng_expiry_result_checked: false
  huaisheng_current_location_known: false
  shiyige_merged_with_huaisheng: false

  next_intended_scene: "返回白家，先驗槐生一日租地到期後的實際顯影結果"

  status: "HOT SAVE V5.24 READY"
```
