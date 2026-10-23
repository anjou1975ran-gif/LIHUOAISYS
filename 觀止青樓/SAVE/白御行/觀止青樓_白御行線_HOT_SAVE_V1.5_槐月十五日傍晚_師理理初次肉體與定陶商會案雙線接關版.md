# 觀止青樓｜白御行線 HOT SAVE V1.5
## 理火三年槐月十五日傍晚｜師理理初次肉體關係 × 定陶商會失鹽案雙線接關版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V1_5_HUAI15_EVENING"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V1.5"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime: "GUANZHI_QINGLOU_V10_0"
  story_date: "理火三年槐月十五日傍晚，將近入夜"
  record_state: "ACTIVE"
  save_scope:
    - "師理理／李師師與白御行第一次肉體關係"
    - "定陶商會京師失鹽案、銀庫防衛、制度修補與外圍追查"

SOURCE_LINEAGE:
  previous_valid_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V1.4_槐月十一日整夜事件全紀錄純淨版.md"
    role: "本次雙線事件以前的直接有效接關來源"
  forbidden_source:
    file: "HOT_SAVE_V1.3"
    status: "ILLEGAL_CORRUPTED_SAVE"
    use: "AUDIT_ONLY"
  character_source:
    file: "觀止人物池_LCAPG_V1.1_紅娘氏與李師師雙人正式版.md"
    role: "李師師與紅娘氏人格基線"

COMMIT_NOTE:
  - "本檔取代 V1.4 成為白御行線當前 HOT 接關切片。"
  - "V1.4 仍保留歷史與前置事件法位，不得刪除。"
  - "本檔只固化已發生、可觀察或已明示確認事項；未知保持未知。"
```

---

# 1｜當前時間與接關位置

```yaml
CURRENT_TIME:
  era: "理火三年"
  calendar_date: "槐月十五日"
  time_of_day: "傍晚，將近入夜"
  certainty: "CONFIRMED"

CURRENT_SCENE:
  player_location: "定陶商會京師總會"
  player_state:
    - "已連續處理商會事件四日"
    - "主要緊急處置完成"
    - "案件已轉入制度試行、押送與外圍追查"
    - "目前沒有必須由白御行親自坐鎮的立即節點"
  player_intention:
    - "準備前往觀止見李師師"
  departure_state: "尚未正式離開定陶商會、尚未抵達觀止"
  next_action_owner: "PLAYER"

LI_SHISHI_CURRENT_STATE:
  location: "觀止"
  exact_activity: "UNKNOWN"
  availability_for_bai_yuxing: "UNKNOWN_UNTIL_SCENE_CONTACT"
  access_rule:
    - "白御行可以前往觀止求見"
    - "不得預設李師師此刻空閒、獨處或已替白御行留門"
    - "進入私人房間前仍應敲門並取得當下允許"
```

---

# 2｜故事線一：師理理與白御行第一次肉體關係

## RIR-E01｜事件時間、身份與私密範圍

```yaml
EVENT_RECORD:
  event_id: "RIR-E01"
  story_time: "理火三年槐月十一日深夜至槐月十二日清晨"
  location: "李師師在觀止的私人房間"
  participants:
    - "白御行"
    - "李師師／師理理"
  status: "COMPLETED"
  knowledge_scope: "STRICTLY_PRIVATE"

IDENTITY_RULE:
  - "師理理不是新人、第二人格或獨立人物。"
  - "師理理是李師師只在白御行私人關係中顯露的身份表現。"
  - "人前仍以李師師為主；其他人物不得無來源地知道或使用『師理理』稱呼。"
```

## RIR-E02｜同意與界線

```yaml
CONSENT_STATE:
  initial_stay:
    - "白御行提出更親近的邀請。"
    - "李師師理解邀請內容並自行同意留下。"
  intercourse:
    - "雙方皆為清醒成年人。"
    - "完整性交由雙方當下同意成立。"
    - "李師師在過程中主動選擇姿勢、節奏、靠近與索取方式。"
    - "她曾明確要求白御行在她開口以前忍住；其後由她親口表示『現在』。"
  pain_boundary:
    event:
      - "白御行曾在未先詢問的情況下，對她肚臍附近施加令她感到疼痛的刺激。"
      - "李師師立即制止並要求：疼痛玩法須事前詢問，由她當下決定。"
      - "白御行接受此界線並安撫她。"
    current_rule:
      - "疼痛刺激不是永久拒絕，也不是永久同意。"
      - "未來每次都必須事前提出並重新取得明確同意。"
      - "李師師曾表示，若先詢問，她未來可能願意嘗試。"
  future_consent:
    - "本次同意不得自動延伸至下一次。"
    - "留門、收禮、過往性交與私人稱呼皆不構成永久身體資格。"
```

## RIR-E03｜肉體事件硬狀態

```yaml
PHYSICAL_EVENT_STATE:
  intercourse_type: "陰道性交"
  completion_state: "COMPLETED"
  mutual_participation: true
  li_shishi_orgasm_response: "ESTABLISHED_BY_OBSERVABLE_REACTION"
  bai_yuxing_completion:
    timing: "在李師師明確表示忍不住並說『現在』之後"
    ejaculation_location: "體內；由白御行後續對事件的明示描述確認"
  contraception: "NONE_RECORDED"
  pregnancy_state: "UNKNOWN_NOT_ESTABLISHED"
  injury_state:
    serious_injury: false
    persistent_injury: "NONE_RECORDED"
  post_event_hygiene:
    - "李師師事後自行梳洗、整理衣髮。"
```

## RIR-E04｜事後停留與關係結果

```yaml
POST_EVENT:
  observable_actions:
    - "性交結束後，兩人沒有立即分開。"
    - "雙方長時間相擁，感受呼吸、心跳與身體逐漸平復。"
    - "李師師主動要求白御行先不要放開她。"
    - "她在晨間仍有不願立即起身的依戀與停留。"
  emotional_statement:
    speaker: "李師師"
    content:
      - "她記得白御行的話、手，以及自己如何選擇留下、如何抱住他。"
      - "她不以尚未活過的一生作空白保證。"
      - "只要她仍認得自己，這一夜不會被傳聞、後來故事或人前的李師師形象蓋掉。"
    state_type: "CHARACTER_COMMITMENT_TO_MEMORY"
    not_equal_to:
      - "戀愛承諾"
      - "終身伴侶承諾"
      - "排他承諾"
      - "婚姻"
```

## RIR-E05｜「第一個男人」事實邊界

```yaml
FIRST_MAN_FACT:
  confirmed:
    - "白御行是李師師抵達仁宗朝觀止之後，第一個與她發生性交的男人。"
    - "白御行也是『師理理』此一私人身份第一次自行選擇的男人。"
  unknown:
    - "李師師跨時代以前是否曾與其他男人發生性關係，未被正式建立。"
  forbidden_inference:
    - "不得因花魁、名妓、傳聞、年代差或職業身份推定其一生性史。"
    - "不得把『到觀止後第一個』改寫成『一生第一個』。"
```

## RIR-E06｜目前關係硬狀態

```yaml
RELATION_STATE:
  state_class: "ACTIVE"
  state_label: "私人性關係已成立／追求可能持續開放"
  established:
    - "兩人已有一次雙方同意的完整性交。"
    - "雙方已有私密身體記憶、事後擁抱與私人稱呼。"
    - "李師師允許白御行繼續追求與探索後續親密。"
  not_established:
    - "戀愛正式成立"
    - "排他關係"
    - "專屬身體權"
    - "每日親密義務"
    - "婚姻或長期契約"
  private_name_access:
    name: "理理"
    holder: "白御行"
    scope: "私人使用；不自動公開"
  next_encounter_rule:
    - "李師師會在自己想要時表達。"
    - "可能連續數夜，也可能間隔數日；沒有固定頻率。"
    - "白御行需重新敲門、詢問並取得當下允許。"
```

## RIR-E07｜錯過的再會、禮物與現存伏筆

```yaml
FOLLOWUP_EVENTS:
  planned_second_night:
    - "白御行曾與李師師約定，當晚可能再試『新招數』。"
    - "因定陶商會事件爆發，白御行未能赴約。"
    - "該次留門只屬當夜，現已失效，不構成槐月十五日的自動進房權。"
  messenger_and_gift:
    sender: "白御行"
    item: "一盒十二種花香的定陶香皂"
    message: "今晚有事，無法前往"
    recipient: "李師師"
    result:
      - "李師師收下全盒香皂。"
      - "她先選白梅香使用。"
      - "她回箋表示正事既留住白御行，當晚不再留門；新招數仍欠著，不准以忙碌賴掉。"
  knowledge_scope:
    sexual_event_details:
      know:
        - "白御行"
        - "李師師"
      others: "UNKNOWN_AND_NOT_ESTABLISHED"
    soap_gift:
      know:
        - "白御行"
        - "李師師"
        - "送禮小廝知道送禮與白御行不能赴約"
        - "潘金蓮看見香皂盒，但不知道完整私密事件"
```

## RIR-E08｜三人親密話題

```yaml
THREESOME_DISCUSSION:
  status: "DISCUSSION_ONLY"
  li_shishi_preference:
    first_choice: "紅娘氏"
    reason:
      - "紅娘能看懂三人注意力與場面流向。"
      - "她不會只圍著男人轉，也敢爭取自己的位置。"
  bai_yuxing_preference:
    - "希望紅娘只作輔助，主要注意力留給李師師。"
  li_shishi_response:
    - "她可接受主要心力放在自己身上。"
    - "紅娘不是工具；她是否加入、收費、碰誰及接受何種位置，必須由紅娘本人決定。"
  actual_invitation: false
  hongniang_consent: "NOT_REQUESTED"
  event_scheduled: false
```

---

# 3｜故事線二：定陶商會京師失鹽案

## DTC-E01｜案件起點

```yaml
INCIDENT:
  event_id: "DTC-E01"
  start_time: "理火三年槐月十二日清晨前後"
  location: "定陶商會京師東倉"
  stolen_goods:
    product: "三烤鹽"
    carts: 12
    bags: 96
  method:
    - "偽造總會長直批貨票"
    - "使用近似總會長印的仿印"
    - "使用真實舊票紙、商會舊旗牌與正確夜間口令"
    - "以臨時調貨名義連夜提貨"
  immediate_assessment:
    - "不是單人臨時偷竊。"
    - "至少包含情報、刻印、車隊、藏倉、銷贓與外圍接應。"
    - "對方具有組織化、分層與斷點能力。"
```

## DTC-E02｜貨物追回與人員結果

```yaml
RECOVERY_RESULT:
  operation_commander: "程景衡"
  manpower_source:
    - "前日自定陶送貨入京、尚未返程的第七運隊"
    - "抓捕行動不用京師原守備作主力"
  simultaneous_sites:
    - "西舊窯場：五車"
    - "北渡口廢魚行：四車"
    - "東河堤破廟後院：三車"
  recovered:
    carts: 12
    bags_equivalent: 95.5
    note:
      - "其中半包已被拆作樣品。"
      - "八包外皮被刮洗，但內中仍為原貨。"
  arrested: 27
  escaped: 5
  casualties: "NONE_FORMALLY_RECORDED_IN_HOT"
```

## DTC-E03｜第一告密者

```yaml
FIRST_INFORMANT:
  identity: "年輕車夫；正式姓名未記入公開案卷"
  contribution:
    - "交出三處藏貨位置"
    - "交出三十三人分錢名冊"
    - "提供同時收網的時間條件"
  protection:
    - "在動手前自行避開"
    - "由程景衡安排至城南私宅"
    - "更換衣著與對外身份"
    - "本人與家眷受商會保護"
  reward:
    emergency_debt_cleared: "四十三兩"
    cash_reward: "二百兩"
  legal_and_internal_status:
    - "依白御行先前首告承諾保全"
    - "不得因後續重刑政策撤銷承諾"
```

## DTC-E04｜主要涉案人物與未知上線

```yaml
PERSONS_AND_LEADS:
  shi_kui:
    identity: "河東車行牙人"
    marker: "右手虎口燙傷／纏布"
    confirmed_actions:
      - "替吳六母親先付二十兩藥錢"
      - "參與車隊、藏倉、分帳與收買商會員工資訊"
    current_state: "已捕，隨涉案者分批押送定陶總部"
  gray_ledger_mister:
    name: "灰簿先生"
    source: "被捕押車人口供中的稱呼"
    identity: "UNKNOWN"
    existence_as_single_person: "UNVERIFIED"
    known_method:
      - "蒐集商會員工缺錢、遭難、抱怨與可被逼迫的節點"
      - "透過外圍人員逐層接近，不讓底層知道本體"
  external_enemy:
    state: "ORGANIZED_ENEMY_CONFIRMED_AT_NETWORK_LEVEL"
    exact_core_identity: "UNKNOWN"
```

## DTC-E05｜吳六狀態

```yaml
WU_LIU:
  role: "東倉副倉簿"
  family_crisis:
    - "母親重病屬實"
    - "藥錢缺口約七十八兩"
    - "吳六曾典當冬衣並向熟人借款"
    - "曾兩次向商會申請借支，均以『不合舊例』駁回"
  involvement_evidence:
    - "與舊旗牌銷毀紀錄有關"
    - "石魁曾以藥錢接近並開價收買"
  exculpatory_or_uncertain:
    - "石魁供稱吳六最初可能答應，後在取貨前表示不做、不要錢。"
    - "吳六未出現在三處藏貨與分帳現場。"
    - "目前沒有直接證據證明吳六完成洩密或參與偷運。"
  current_location: "UNKNOWN"
  possible_states:
    - "逃避"
    - "被團伙控制或滅口"
    - "知情後躲藏"
  guilt_state: "NOT_ESTABLISHED"
```

## DTC-E06｜鹽務處置

```yaml
SALT_POLICY:
  three_roast_salt:
    capital_status: "京師現有庫存封存"
    sale_status: "京師停止販售"
    dingtao_supply: "停止供應三烤鹽"
    old_goods_recognition: "商會不再對未經新驗封的舊貨公開保認"
  six_roast_salt:
    dispatch: "定陶庫存已開始分批運往京師"
    price: "原三烤鹽牌價的兩倍"
    package_security:
      - "新印"
      - "新繩"
      - "雙色封口"
      - "不得沿用舊旗、舊票"
  official_report:
    - "不主動報官請其查案"
    - "商會自行追查；若證據完整，再決定是否把人與證據交付官面處理"
```

## DTC-E07｜銀庫守備與攻心紙條

```yaml
SILVER_VAULT_DEFENSE:
  guard_rotation:
    - "銀庫原守備調往貨倉"
    - "貨倉原守備調往銀庫"
    - "分輪交接、重新點人、驗牌與換口令"
  discovered_signs:
    - "銀庫西牆外有避開舊巡線的新鞋印"
    - "後門門軸被提前上油"
    - "排水溝藏有銀庫內外三重門位置圖"
    - "夜役范成攜帶調防前的銀庫值夜名單被捕"
  silver_loss: false
  successful_attack: false

ANONYMOUS_NOTE:
  text: "白總換得好。可你換的是守門的人，不是替你數銀子的人。"
  bai_yuxing_judgment: "標準攻心計"
  current_policy:
    - "匿名紙條不作內鬼證據。"
    - "不因紙條臨時撤換帳房或互相猜疑。"
    - "目前不把任何現任員工標記為內鬼。"
  unresolved_document_leak:
    - "敵方確實持有被駁回的員工借支申請抄件。"
    - "來源可能是舊卷處置漏洞、文件遭竊、外包抄寫或其他外洩路徑。"
    - "在查明傳遞方式以前，不升格為現任內鬼。"
```

## DTC-E08｜隨機交叉審計試行

```yaml
CROSS_AUDIT_TRIAL:
  status: "ACTIVE_TRIAL"
  initial_site: "京師銀庫"
  trial_period: "一個月"
  purpose:
    - "增加程序覆核，不以懷疑個人為起點"
    - "避免任何一人單獨成為制度最後一道門"
  design:
    - "帳房、契印、倉務、行路四房建立輪值池"
    - "每次抽出不同房別兩人"
    - "不得固定搭檔，不得連續三次同組"
    - "第一次隨機抽審計人，第二次隨機抽審計批次"
    - "兩人分開記錄，結果交出後由第三名值日師爺比對"
    - "通過案件仍按比例作秘密盲抽重驗"
    - "審計者只有記錄與上報權，沒有自行處罰權"
  early_results:
    - "查出新舊編號簿並行造成封條重號"
    - "查出驗色石磨損造成成色判定偏差"
    - "未因上述差異認定侵吞或內鬼"
  expansion_rule:
    - "若試行一月有效且交割延誤可控，推廣至總帳、高價貨倉與各地分號"
    - "不得只抄章程便宣稱已施行；各處都需自行試跑與評估"
```

## DTC-E09｜員工急難護持案

```yaml
EMPLOYEE_HARDSHIP_PROGRAM:
  name: "定陶商會急難護持案"
  authorization: "白御行已蓋章"
  status: "FORMAL_SIX_MONTH_TRIAL"
  review_due: "試行滿六個月後重新評估"
  purpose:
    - "讓遭遇重大家庭變故的員工有合法求助入口"
    - "避免敵人利用走投無路者撬開商會制度"
  aid_types:
    emergency_aid:
      - "醫藥、喪葬、贖人等不能拖延事項，可先給後查"
    turnover_loan:
      - "無息或低息借支，往後薪錢分期扣還"
      - "不得因借支降職或羞辱"
    family_protection:
      - "員工因公受傷、失蹤或死亡時，商會暫時支應家眷"
  rules:
    - "申報困難不作為污點。"
    - "虛報、冒領仍照規處分。"
    - "商會救的是難，不以救助購買忠誠。"
    - "受助者若仍背叛商會，本人照背叛處置；家眷生路不因而先被切斷。"
```

## DTC-E10｜涉案者押送與處置命令

```yaml
DETAINEE_DISPOSITION:
  transfer:
    destination: "定陶總部"
    method:
      - "分批押送"
      - "不同道路返程"
      - "不在京師完成最終處置"
    current_state: "IN_TRANSIT_OR_AWAITING_DINGTAO_HQ_PROCESSING"
  family_message:
    scope: "涉及商會員工之家屬"
    public_explanation: "奉總部調派，前往定陶辦差"
    hardship_support:
      - "家中若因此斷薪、缺藥或缺糧，急難房先給短期救濟"
  sentencing_directive:
    lighter_offense:
      - "送礦場服役三年"
      - "期滿放回"
      - "商會及所屬聯號永不再錄用"
    serious_offense:
      - "交定陶總部依證據決定重刑"
      - "若確認為戰時敵首且無情報價值，可考慮列入大野澤水域處置候選"
  execution_certainty:
    - "本 HOT 只確認處置命令與押送。"
    - "尚未確認任何個別重犯已死亡、致殘或被送入大野澤。"
```

## DTC-E11｜參與人員補假

```yaml
STAFF_RECOVERY_ORDER:
  authorization: "白御行裁示"
  scope:
    - "參與四日追查、換防、押運、覆核、夜審與收網者"
  benefit:
    - "下個月分批帶薪補假"
    - "不得以人手不足扣假"
    - "不得要求事後無償補班"
    - "受傷療養另計，不從補假扣除"
  status: "ORDERED_FOR_NEXT_MONTH"
```

## DTC-E12｜當前調查策略

```yaml
INVESTIGATION_STRATEGY:
  core_assessment:
    - "對方擅長斷點，底層不一定知道本體。"
    - "現階段不以直接摸到敵方核心為必要成功條件。"
  active_method:
    - "先抓外圍節點"
    - "追車行、空倉、藥鋪、當鋪、文書抄件、小額先付款與臨時債務清償"
    - "每抓住一層便封住一層，使對方重新花錢、重新建信任、重新冒風險"
  operational_owner: "程景衡與師爺房"
  player_reporting_rule:
    - "一般外圍進度自行決斷，不需逐件回報白御行。"
    - "若發現第二次即將發動的攻擊、總會高層涉案、重大人命風險或需要會長法位，才立即上報。"
  current_threat_state: "CONTAINED_BUT_NOT_CLOSED"
```

---

# 4｜當前關係、知情與公開資訊

```yaml
KNOWLEDGE_MATRIX:
  bai_yuxing:
    knows:
      - "師理理第一次肉體事件全部內容"
      - "李師師的疼痛界線與私人稱呼"
      - "商會案目前全部核心會報與裁示"
  li_shishi:
    knows:
      - "與白御行的全部私密事件"
      - "白御行因商會正事錯過原定再會"
    merchant_case_detail: "只知道白御行有正事被留住；是否得知完整案情，未建立"
  pan_jinlian:
    knows:
      - "白御行曾送十二花香皂給李師師"
    sexual_detail: "NOT_CONFIRMED"
  messenger_page:
    knows:
      - "白御行當晚有事不能赴觀止"
      - "送出十二花香皂"
    sexual_detail: "UNKNOWN"
  guild_staff:
    knows:
      - "失鹽案、換防、押送與制度試行依職務分層知情"
    li_shishi_private_relation: "NO_SOURCE"

PUBLIC_STATE:
  guanzhi:
    - "李師師仍是自主設席花魁。"
    - "白御行與師理理的肉體關係不是公開事件。"
  merchant_guild:
    - "京師三烤鹽停止銷售，六烤鹽正在運京。"
    - "銀庫與高價貨務開始交叉審計試行。"
    - "急難護持案已試行。"
    - "敵方核心身份未公開、未查明。"
```

---

# 5｜未決事項

```yaml
OPEN_THREADS:
  riri_line:
    - "槐月十五日晚，白御行是否前往觀止。"
    - "李師師當晚是否在設席、見客、休息或願意私下見白御行，尚待現場回答。"
    - "先前所說的『新招數』尚未發生。"
    - "未來疼痛玩法需重新詢問。"
    - "紅娘氏三人親密話題仍停留在討論，未形成邀請。"
    - "體內射精後是否產生妊娠結果，當前未知，不得提前宣告。"
  guild_line:
    - "吳六下落與實際涉案程度。"
    - "五名逃犯去向。"
    - "『灰簿先生』是否為單一人物、群體稱號或假名。"
    - "員工借支申請抄件的真正外洩路徑。"
    - "一個月後交叉審計是否推廣全商會。"
    - "六個月後急難護持案重新評估。"
    - "押送定陶者的個別罪責與最終處置。"
    - "六烤鹽抵京後的市場與信用反應。"
```

---

# 6｜接關約束

```yaml
CONTINUATION_LOCK:
  next_scene_entry:
    - "白御行仍在定陶商會京師總會，準備離開。"
    - "玩家若說前往觀止，導演推進到觀止當夜現場。"
    - "不得自動讓李師師空房等待、主動解衣或延續前次性交。"
    - "不得替白御行敲門、進房、承諾或接受新的親密。"
  riri_character_lock:
    - "李師師可想念、拒見、設席、見客、休息、逗弄、追問或接受相見，依當晚自身位置決定。"
    - "她記得第一次肉體事件，不得失憶或被抽象成模糊親近。"
    - "她的記憶不等於戀愛、排他或終身歸屬。"
  guild_lock:
    - "商會案沒有結案，只是由白御行親自處置轉為制度化與外圍追查。"
    - "不得因玩家離開商會便讓敵人自動停止活動。"
    - "不得把匿名紙條重新升格為內鬼證據。"
    - "不得把吳六直接定罪。"
    - "不得宣稱大野澤處置、致殘或死亡已執行，除非後續有明確回報。"
```

---

# 7｜有效接關摘要

白御行與李師師／師理理已完成兩人第一次雙方同意的肉體關係。事件包含性交、體內射精、高潮反應、事後長時間擁抱與私人記憶承諾；同時建立疼痛玩法必須事前詢問的明確界線。白御行是她抵達仁宗朝觀止後第一個男人，但她跨時代以前的性史仍未知。兩人已有私人性關係與追求可能，沒有戀愛、排他、婚姻或永久身體資格。

定陶商會十二車三烤鹽案已追回十二車與九十五包半原貨，捕獲二十七人，五人逃走。第一告密者依承諾受保護並領賞。京師三烤鹽已封存停售，六烤鹽正以雙倍價格運京；急難護持案試行六個月，隨機交叉審計先在京師銀庫試行一個月。涉案者分批押回定陶，家屬短期救濟；案件改以抓外圍節點為主。敵方網路仍存在，但目前沒有立即需要白御行坐鎮的節點。

**當前時間：理火三年槐月十五日傍晚。**

**當前位置：定陶商會京師總會。**

**下一步：白御行可自行決定是否前往觀止求見李師師；尚未出發。**

---

## VERSION_STATUS

```yaml
ACTIVE_HOT_SAVE: "V1.5"
PREVIOUS_VALID_HOT: "V1.4"
ILLEGAL_SAVE:
  version: "V1.3"
  use: "AUDIT_ONLY"
```
