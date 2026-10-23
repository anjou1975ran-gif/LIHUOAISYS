# 觀止青樓｜白御行線 HOT SAVE V1.6
## 理火三年槐月十六日清晨｜張麗華情人花燭前置 × 師理理共宿 × 白玉池異常回顯封池版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V1_6_HUAI16_MORNING"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V1.6"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime: "GUANZHI_QINGLOU_V10_0"
  story_date: "理火三年槐月十六日清晨"
  record_state: "ACTIVE_PAUSED"
  save_scope:
    - "張麗華接受情人關係與今晚花燭前置"
    - "白御行與李師師／師理理槐月十五日晚至十六日清晨事件"
    - "白玉池阿泠、水療提案、異常回顯與封池調查"
    - "定陶商會案必要活躍狀態承接"

SOURCE_LINEAGE:
  previous_valid_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V1.5_槐月十五日傍晚_師理理初次肉體與定陶商會案雙線接關版.md"
    role: "本輪事件以前的直接有效 HOT 來源"
  previous_valid_history:
    file: "觀止青樓_白御行線_HOT_SAVE_V1.4_槐月十一日整夜事件全紀錄純淨版.md"
    role: "前置事件與拒絕核心來源"
  forbidden_source:
    file: "HOT_SAVE_V1.3"
    status: "ILLEGAL_CORRUPTED_SAVE"
    use: "AUDIT_ONLY"
  character_sources:
    - "觀止人物卡_LCAPG_V1.1-R1_原始重構去污染版_含辭歲_導演隱藏區增補.md"
    - "觀止人物池_LCAPG_V1.1_紅娘氏與李師師雙人正式版.md"

SOURCE_INTEGRITY_LOCK:
  - "本檔白玉池事件只依槐月十五日晚至十六日清晨本輪實際演進固化。"
  - "不得用非法 HOT_SAVE_V1.3 補完阿泠、池底異常或任何人物關係。"
  - "MASTER 中既有『白玉池無名女子』不得自動與阿泠合併；兩者是否同一存在目前未知。"

COMMIT_NOTE:
  - "本檔取代 V1.5，成為白御行線當前 HOT 接關切片。"
  - "V1.5 保留完整定陶商會案與此前師理理事件法位。"
  - "本檔只記已發生、可觀察、人物明示或玩家對自身行動的有效確認。"
  - "推測、比喻、研究假說與人物自述均另行標記，不升格為客觀真相。"
```

---

# 1｜當前時間、位置與暫停點

```yaml
CURRENT_TIME:
  era: "理火三年"
  calendar_date: "槐月十六日"
  time_of_day: "清晨，日已亮"
  certainty: "CONFIRMED"

CURRENT_SCENE:
  location: "觀止後院白玉池池邊／月洞門內"
  scene_state: "PAUSED_AFTER_INVESTIGATION_DISCUSSION"
  present_or_immediately_present:
    - "白御行"
    - "李師師／師理理"
    - "李瓶兒"
    - "蘇清"
    - "阿泠"
  not_present:
    - "潘金蓮"
  next_action_owner: "PLAYER"

PLAYER_STATE:
  wake_state: "已起床、已洗漱穿衣"
  fatigue:
    - "此前連續處理定陶商會事件四日"
    - "昨夜白玉池水療使腰背緊硬得到部分舒緩"
  sexual_state:
    - "清晨已射精一次"
    - "目前沒有正在進行的性行為"

IMMEDIATE_DUE_ITEMS:
  - "槐月十六日晚：張麗華情人花燭夜預定到期。"
  - "槐月十六日上午：李瓶兒須先向張麗華確認飯席、賓客與安排是否照舊。"
  - "白玉池維持封池；蘇清與阿泠繼續調查，李瓶兒看管營運與知情範圍。"
```

---

# 2｜槐月十五日晚：返回觀止與前置事件

## GZ15-E01｜抵達觀止

```yaml
EVENT_RECORD:
  event_id: "GZ15-E01"
  time: "槐月十五日晚，戌初前後"
  location: "觀止"
  status: "COMPLETED"
  observable:
    - "白御行結束定陶商會四日緊急處置後抵達觀止。"
    - "潘金蓮在入口與白御行有短暫調笑。"
    - "李師師當晚已結束一席，不再接新客。"
    - "白御行吩咐廚房送麵、糕點與小食到李師師房中。"
  minor_business_thread:
    - "潘金蓮對定陶花香皂有興趣。"
    - "白御行表示她若付錢可給八折。"
    - "個人價或批發價尚未正式議定。"
```

## GZ15-E02｜白御行對商會殺人事件的私人確認

```yaml
MERCHANT_KILLING_DISCLOSURE:
  speaker: "白御行"
  listener: "李師師／師理理"
  fact_authority: "PLAYER_CONFIRMED_OWN_ACTION"
  confirmed:
    - "白御行表示自己在定陶商會事件中親手殺死一批背叛者。"
    - "他認為其中有人可能因家中困境而走上背叛。"
    - "他已決定援助相關家屬。"
  unknown:
    - "被殺者確切人數與姓名"
    - "每人的具體罪證與死亡情境"
    - "援助家屬的名冊、金額與實際執行情況"
    - "此事在商會內的正式紀錄與公開知情範圍"
  li_shishi_response:
    - "她沒有替白御行赦免或把援助說成抵銷死亡。"
    - "她要求白御行記住姓名與原因，不要把死亡壓成『一批人』。"
    - "她仍允許白御行在她面前卸下會長與善人身分，並抱住他。"
```

---

# 3｜張麗華：情人關係與花燭夜

## ZLH-E01｜接受「情人」關係

```yaml
EVENT_RECORD:
  event_id: "ZLH-E01"
  time: "槐月十五日晚，白御行進李師師房前"
  location: "張麗華房間"
  participants:
    - "白御行"
    - "張麗華"
  status: "COMPLETED"

RELATION_STATE:
  state_label: "情人關係已由張麗華明示接受"
  established:
    - "張麗華同意作白御行的情人。"
    - "雙方互相親吻。"
    - "張麗華表示次日晚會穿紅衣。"
  structure:
    - "不立婚書。"
    - "不入白家名冊。"
    - "不形成所有權。"
    - "張麗華仍居觀止。"
    - "她保留何時見白御行、是否親近與如何相處的決定權。"
  not_established:
    - "妻妾名分"
    - "排他關係"
    - "永久性同意"
    - "離開觀止"
    - "白家對張麗華的管理權"
```

## ZLH-E02｜情人花燭夜內容與界線

```yaml
FLOWER_CANDLE_PLAN:
  due_time: "槐月十六日晚"
  location: "張麗華房間"
  status: "SCHEDULED_WITH_SAME_DAY_RECONFIRMATION_REQUIRED"
  agreed_symbolic_items:
    - "紅色妝面或紅妝安排"
    - "紅衣"
    - "紅蓋頭"
    - "紅色床帳與被褥"
    - "紅燭"
    - "合巹酒"
  restrictions:
    - "不得使用白家徽記。"
    - "不得稱張麗華為妻或夫人。"
    - "送貨與佈置人員不得沿途宣稱張麗華出嫁。"
    - "不得把私人情人儀式變成觀止公開收賀或圍觀事件。"

CONSENT_CLARIFICATION:
  initial_problem:
    - "白御行曾說『明晚給妳洞房花燭夜，妳不能拒絕』。"
    - "張麗華拒絕任何不能拒絕的親密安排。"
  player_clarification:
    - "白御行澄清『不能拒絕』只指紅衣、紅帳、蓋頭等禮物與象徵安排。"
  resulting_state:
    - "張麗華接受上述禮物與情人花燭儀式。"
    - "槐月十六日晚是否發生性行為、身體親近與進行到何處，仍由張麗華當時決定。"
    - "張麗華表示白御行必須到場；若遲到，她可以關門。"
```

## ZLH-E03｜飯席與採買委託

```yaml
LI_PINGER_TASKS:
  task_owner: "李瓶兒"
  payer: "白御行私帳"
  due: "槐月十六日上午"
  preparations:
    - "紅衣、紅蓋頭"
    - "紅帳、紅被褥"
    - "喜燭、燈罩、桌布"
    - "香料"
    - "合巹酒與晚間酒菜"
  accounting:
    - "採買價、人工、酒菜分項記錄。"
    - "不得列入觀止一般日常支出。"
    - "事後向白御行請款。"

DINNER_RULE:
  - "李瓶兒先問張麗華是否仍願照原安排進行。"
  - "李瓶兒先問張麗華是否要請人、願意讓誰知道。"
  - "只請張麗華親口點名的人。"
  - "春梅可能被張麗華選入，但目前不得自動視為確定賓客。"
  - "若張麗華不想請人，只備兩人飯菜。"
  - "飯席預計短而私密；人散後房門關閉，後續不對外。"
```

## ZLH-E04｜知情狀態

```yaml
KNOWLEDGE:
  knows_relation_and_plan:
    - "白御行"
    - "張麗華"
    - "李師師／師理理"
    - "李瓶兒"
  hongniang:
    status: "NOT_INFORMED_AS_OF_LAST_CONFIRMATION"
  pan_jinlian:
    status: "NOT_CONFIRMED"
  public_state: "NOT_PUBLIC"
```

---

# 4｜李師師／師理理：槐月十五日晚關係事件

## RIR15-E01｜進房、身份與私人稱呼

```yaml
EVENT_RECORD:
  event_id: "RIR15-E01"
  location: "李師師私人房間"
  entry:
    - "白御行敲門。"
    - "李師師允許他進房。"
  sensory_detail:
    - "李師師使用了白梅香皂。"
  identity_state:
    - "師理理仍不是新人或第二人格。"
    - "她是李師師在白御行私人關係中的表現。"
  private_address:
    li_shishi_to_player: "御行"
    anger_or_boundary_form: "白御行"
    player_to_li_shishi: "理理"
    scope: "PRIVATE_ONLY"
  not_established:
    - "固定使用『親親好老公』"
    - "婚姻或丈夫身分"
```

## RIR15-E02｜張麗華消息與嫉妒

```yaml
DISCLOSURE:
  - "白御行在李師師房中告知：張麗華已答應作其情人，槐月十六日晚預定花燭夜。"
  - "李師師明示嫉妒與不舒服。"
  - "她沒有要求白御行取消與張麗華的承諾。"
  - "她要求白御行到張麗華房中時，不要身在其處、心想別人。"

TIMING_CORRECTION:
  - "李師師起初以為白御行在房中安頓許久後才告知。"
  - "白御行澄清：張麗華是在他進李師師房前才給答案，他隨即前來告知；紅娘尚未知情。"
  - "李師師接受澄清，撤回『故意拖延告知』的指責。"
  - "她仍保留嫉妒，不因白御行未隱瞞便被要求立刻高興。"

ADDITIONAL_FACT:
  - "白御行表示自己沒有留在張麗華房中，而是赴李師師原先的約。"
  - "李師師承認知道此事令她高興。"
  - "此事不構成排他承諾，也不等於張麗華的情緒已被正式查明。"
```

## RIR15-E03｜當晚關係硬狀態

```yaml
RELATION_RESULT:
  established:
    - "李師師與白御行的私人性關係持續有效。"
    - "李師師會嫉妒，但沒有提出排他要求。"
    - "白御行對張麗華的情人承諾沒有自動取消。"
  situational_claim:
    - "李師師所說『今晚是我的』只指槐月十五日晚兩人已約定並共同度過的實際時段。"
  not_established:
    - "戀愛正式成立"
    - "排他關係"
    - "李師師對白御行其他關係的否決權"
    - "白御行對李師師身體的常設使用權"
```

---

# 5｜白玉池：阿泠、水療與異常回顯

## BYC-E01｜進入白玉池

```yaml
EVENT_RECORD:
  event_id: "BYC-E01"
  time: "槐月十五日晚"
  initial_participants:
    - "白御行"
    - "李師師／師理理"
  access_state:
    - "值夜丫鬟先確認池內無人。"
    - "乾巾、厚袍與熱茶送至池邊。"
    - "止客牌掛出。"
    - "李師師不留丫鬟在場伺候。"
  intimacy:
    - "兩人入池後相擁靠坐、看星。"
    - "李師師自願把頭靠在白御行右肩。"
```

## BYC-E02｜阿泠出現

```yaml
ENTITY_RECORD:
  route_label: "阿泠"
  self_chosen_name: "阿泠"
  character: "泠"
  self_explanation: "水清而有聲"
  first_manifestation_time: "槐月十五日晚"
  location: "白玉池"

OBSERVED:
  - "在李師師邀請池中主人自願現身後，霧中傳出女子聲音。"
  - "她可借霧與泉水顯出女性身形。"
  - "她能維持可見、可辨的肉身輪廓，不會因離開水面一瞬便散去。"
  - "她能控制池水方向、壓力、強弱與落點。"
  - "她能以泉流對不同人的肩頸、腰背施加不同水壓。"

SELF_STATEMENTS_NOT_OBJECTIVE_PROOF:
  - "她自稱生於池中。"
  - "她稱白玉池是自己的地方。"
  - "她表示自己平時不穿衣，水與霧是其遮掩。"

NAME_AND_AFFILIATION_LOCK:
  - "她拒絕『白池靈／白癡靈／白冷靈』等稱呼。"
  - "她沒有接受白姓。"
  - "她沒有接受成為白御行妹妹、乾妹妹或白家人。"
  - "白御行只提出過認她作妹妹；阿泠未認白御行作哥哥。"
  - "她不是白御行的女人。"
```

## BYC-E03｜水療試作與營運提案

```yaml
WATER_THERAPY:
  recipients:
    - "白御行"
    - "李師師／師理理"
    - "李瓶兒"
  result:
    - "阿泠能以不同水壓精準推揉肩頸與腰背。"
    - "李瓶兒確認其具有可形成高價服務的實用性。"
  business_status: "PROPOSAL_ONLY_NOT_OPEN"

A_LING_TERMS:
  - "白玉池仍是她的地方。"
  - "她願意替誰水療、做幾席，由她自己決定。"
  - "客人不能指定她必須出手。"
  - "可以提出力道要求，她保留是否照辦的決定。"
  - "她的名字、存在與身份不得作公開招牌。"

LI_PINGER_PROVISIONAL_MODEL:
  - "對外只可稱水脈或泉況特殊，不公開池靈。"
  - "每日是否有水療、做幾席，不保證。"
  - "不得宣稱治病。"
  - "不得讓客人在池中醉酒。"
  - "不得一次塞入多人。"
  - "手腳不乾淨者可永久止客。"
  - "阿泠需要的回報應先問其真正需要，不預設只能收銀。"

CURRENT_RESULT:
  - "沒有簽約。"
  - "沒有牌價。"
  - "沒有正式分成。"
  - "沒有對外營運。"
  - "因池底異常，水療提案全面暫停。"
```

## BYC-E04｜李瓶兒入池與私人追求狀態

```yaml
LI_PINGER_POOL_ENTRY:
  - "白御行要求外頭丫鬟請李瓶兒，不要請潘金蓮。"
  - "李瓶兒先停在屏風外，確認池中情況。"
  - "她在李師師表示值得、阿泠允許自行決定後，選擇脫衣入池。"
  - "她明示自己下水不是因白御行命令她脫衣。"

ROMANTIC_DISCUSSION:
  trigger: "白御行詢問自己追求李瓶兒是否有機會"
  li_pinger_answer: "有機會"
  state:
    - "李瓶兒沒有接受成為白御行的女人。"
    - "沒有成立情人、性關係、約會或排他承諾。"
    - "她要求白御行分清公事帳、好奇入池與男女意思。"
    - "她表示門尚未關，但要先看白御行如何處理既有女人與承諾。"
  forbidden_inference:
    - "不得把『有機會』寫成已追到、已戀愛或已同意性關係。"
```

---

# 6｜白玉池異常：已觀察事件

## BYX-E01｜初次「歸零」異常

```yaml
TRIGGER_SEQUENCE:
  - "白御行以『泠、靈、零、000』作諧音玩笑。"
  - "白玉池泉聲與水波曾短暫異常安靜。"
  - "池底出現三枚圓形暗影。"
  - "有一道來源不明的聲音說出『歸零』。"

A_LING_RESPONSE:
  - "阿泠確認該聲音與暗影不是她主動製造。"
  - "她表示暗影來自自己平常無法觸及的深水層。"
  - "她以水勢將暗影壓回泉眼以下。"

UNKNOWN:
  - "發聲者身份"
  - "是否存在獨立實體"
  - "『歸零』的作用對象"
  - "深水層的空間、年代與機制"
```

## BYX-E02｜重複語音與算式回顯

```yaml
OBSERVED_TESTS:
  repeated_reset_word:
    input: "白御行連續說『歸零』"
    output:
      - "每一聲對應一圈暗紋。"
      - "停止輸入後，暗紋依序淡去。"
    note: "本次沒有再出現來源不明的主動語音。"

  arithmetic_1:
    input: "一加二加三等於"
    output:
      - "泉眼發出六次等距聲響。"
      - "六粒水珠浮於水面。"
      - "水珠排列為一、二、三的數量分組。"
      - "最後顯出中文字『六』。"

  wall_glyph:
    event:
      - "池邊白玉石面出現規整方形紋路。"
      - "紋路內顯示『續』字。"
      - "『續』約每六息亮暗一次。"
    current_state:
      - "尚未有人觸碰。"
      - "尚未執行任何以『續』為目標的空間宣告。"
```

## BYX-E03｜蘇清通宵最小測試

```yaml
RESEARCH_OWNER:
  lead: "蘇清"
  local_domain_holder: "阿泠"
  operations_and_secrecy: "李瓶兒"
  status: "ACTIVE"

CONFIRMED_OVERNIGHT_OBSERVATIONS:
  speaker_scope:
    - "異常不是只認白御行。"
    - "蘇清與阿泠說出簡單算式時，池面亦能給出正確結果。"
  temporary_storage:
    - "蘇清先輸入『十加五』，半個時辰後才補『等於』。"
    - "池面仍顯出十五。"
  reset_behavior:
    - "蘇清先輸入『九加九』但不說等於。"
    - "其後說『歸零』，再補『等於』。"
    - "池面沒有顯出十八，只出現一道黑圈後消失。"
  autonomous_voice:
    - "通宵測試期間沒有再出現主動說『歸零』的聲音。"
  water_structure:
    - "阿泠感到每次回顯時，深水層會短暫排列成大量規整方格。"
    - "異常會借用她的水勢，但完成後水量未見減少。"
```

## BYX-E04｜IF／THEN 條件測試

```yaml
CONDITIONAL_TEST:
  proposed_by: "白御行"
  executed_by: "蘇清"
  input: "IF，一加一等於二，THEN，顯示一。"
  output:
    - "池面先顯出『真』。"
    - "其後升起一粒水珠。"
    - "水珠停留後落回池中。"
  a_ling_observation:
    - "她感到水脈反應分成前後兩段。"
  minimum_conclusion:
    - "池底異常至少可對某種條件句產生分段回顯。"
  not_confirmed:
    - "是否真正理解英文 IF／THEN"
    - "是否理解語意、說話意圖或固定音型"
    - "是否屬於程式、機器、術法或其他時空結構"
```

## BYX-E05｜目前研究假說，不得固化為真相

```yaml
HYPOTHESES_ONLY:
  - "計算器回聲"
  - "液晶螢幕"
  - "液態顯示介面"
  - "人機介面"
  - "儲存區或方格化資訊層"
  - "疊加態世界中的顯影面"
  - "等待規則輸入的結構"

RULE:
  - "以上皆為白御行或蘇清的暫時理解工具。"
  - "不得把現代機器術語升格為白玉池客觀本體。"
  - "下一步仍以可觀察輸入、回顯、時間與水勢變化記錄。"
```

---

# 7｜潘金蓮的空間宣告能力與當前處置

```yaml
PAN_SPATIAL_AUTHORITY:
  source_of_confirmation: "李瓶兒"
  confirmed_scope:
    - "當觀止現有空間承載不了人物、事件或時空交疊時，潘金蓮可作出空間宣告。"
    - "觀止可能因此展開原本不存在的場地、走廊或門後連接。"
  limits:
    - "潘金蓮不能任意創造或控制任何想要的空間結果。"
    - "她提出要求；觀止是否回答、如何回答，由觀止本身決定。"
  relevance_to_glyph:
    - "『續』可能與空間展開有關。"
    - "潘金蓮可能是可使其展開的鑰匙，也可能因接近而承擔風險。"
  current_status:
    - "潘金蓮尚未被正式告知池底異常。"
    - "尚未請她對『續』作空間宣告。"
    - "此時不得把她帶到方紋前直接試驗。"
```

---

# 8｜封池、調查與知情範圍

```yaml
WHITE_JADE_POOL_LOCKDOWN:
  status: "CLOSED"
  public_explanation: "水脈檢修／泉況異常"
  physical_controls:
    - "止客牌維持。"
    - "李瓶兒已用掌櫃識別紅繩封住入口。"
  prohibited:
    - "一般客人入池"
    - "水療營運"
    - "碰觸『續』字"
    - "未經蘇清安排的語音測試"
    - "白御行臨時追加算式、歸零、除以零或其他高風險玩笑"
  research:
    - "蘇清負責設計最小變因測試與記錄。"
    - "阿泠負責感知深水層與即時壓制水勢異常。"
    - "李瓶兒負責封池、帳目、對外說法與人員控制。"
    - "查得出來或卡住，蘇清都要向白御行回報。"

KNOWLEDGE_SCOPE:
  full_or_core_knowledge:
    - "白御行"
    - "李師師／師理理"
    - "李瓶兒"
    - "蘇清"
    - "阿泠"
  partial_knowledge:
    night_maids:
      - "知道白玉池夜間請過李瓶兒與蘇清。"
      - "知道目前封池。"
      - "不知道完整異常內容。"
  pan_jinlian: "NOT_FORMALLY_INFORMED"
  public: "NO_SOURCE"
```

---

# 9｜李師師房中共宿與同意軸

## RIR16-E01｜「硬來」語句與即時修正

```yaml
BOUNDARY_EVENT:
  initial_player_statement:
    - "白御行提出兩人赤裸共睡、由後方抱住李師師。"
    - "他同時說若忍不住，別怪他『硬來』。"
  li_shishi_response:
    - "她把『硬來』理解為預告可能忽視其拒絕。"
    - "她立即停止原先親密安排，表示只可睡外榻。"
  player_correction:
    - "白御行改口：自己可以勃起，李師師可以自行說『來』。"
  resulting_rule:
    - "李師師接受修正。"
    - "她恢復赤裸共睡與由後方相抱的許可。"
    - "她明示：自己可說『來』或『不要』，白御行必須依當下回答行動。"
  lasting_effect:
    - "本事件沒有建立白御行可用『忍不住』越過同意的資格。"
    - "李師師也沒有因一次錯誤語句永久關係斷裂。"
```

## RIR16-E02｜觸摸與入睡性交

```yaml
INTIMACY_SEQUENCE:
  touch:
    - "白御行先被要求只抱腰。"
    - "他拒絕口頭詢問，要求李師師若願意便親自引導。"
    - "李師師在觀察他確實等待後，親手把他的手放到自己胸前。"
    - "其後胸部觸摸在她持續允許與調整力道下進行。"
  penetration_for_sleep:
    request:
      - "白御行提出陰莖留在李師師體內、相抱入睡，不追求射精。"
    consent:
      - "李師師確認其意圖後明示同意。"
      - "由她親手引導進入。"
      - "初入時她要求停住，待身體適應後才說可以。"
    overnight_result:
      - "兩人以側身相抱姿勢入睡。"
      - "白御行在熟睡後自然軟下並於夜半前滑出。"
      - "夜間雖有短暫睡眠勃起，沒有重新進入。"
      - "夜間沒有射精。"
      - "沒有記錄到持續疼痛或受傷。"
  director_settlement:
    - "白御行沒有硬一整夜。"
```

## RIR16-E03｜槐月十六日清晨射精

```yaml
MORNING_SEXUAL_EVENT:
  initiation:
    - "白御行表示由導演裁決自己是否守得住。"
    - "李師師持續以手刺激。"
  result:
    - "白御行在九分多鐘後射精。"
    - "射精不是陰道內射。"
    - "李師師用口清理殘留並吞嚥。"
  pregnancy_effect:
    - "本次清晨事件沒有新增陰道內精液暴露。"
  knowledge_scope:
    - "白御行"
    - "李師師／師理理"
```

---

# 10｜妊娠風險、月事與未來性界線

```yaml
PREGNANCY_STATE:
  current: "UNKNOWN_NOT_ESTABLISHED"
  known_risk_source:
    - "槐月十一日深夜至十二日清晨第一次性交曾無避孕體內射精。"
  no_new_internal_ejaculation:
    - "槐月十五日晚至十六日清晨共宿沒有陰道內射精。"
  timing:
    - "距第一次體內射精僅數日，當前無法依外觀或感覺確認是否懷孕。"

TIME_TRAVEL_CYCLE_CLAIM:
  source: "時空道人先前說法"
  content:
    - "召喚或時空轉移可能干擾月事週期。"
    - "身體不會因此自動重置。"
  status: "CHARACTER_SOURCE_CLAIM_NOT_MEDICAL_CERTAINTY"

LI_SHISHI_DECISION:
  - "她會自行記錄月事。"
  - "若該來未來，會先告知白御行。"
  - "她會私下找可靠女醫詢問身體與避子方法。"
  - "在情況明白以前，未來陰道性交不允許白御行內射。"
  - "若真的懷孕，是否留下最終由李師師決定。"
  - "白御行可以表達想法與陪伴，但不得以血脈、孩子、感情或白家名冊施壓。"

PLAYER_CONCERN:
  - "白御行明示自己害怕的是李師師在不想要的情況下懷孕。"
  - "李師師接受此說法，並表示因此較安心。"
```

## FUTURE_ANAL_DISCUSSION

```yaml
ANAL_SEX_STATUS:
  current_consent: "NO"
  li_shishi_position:
    - "槐月十六日清晨不接受。"
    - "未永久關閉未來可能。"
    - "未來須事前詢問、充分準備、緩慢進行並在她每次要求時立即停止。"
  lubricant_discussion:
    pig_fat: "李師師明確拒絕氣味。"
    rose_oil:
      - "可以先帶來聞。"
      - "先在手腕少量試用。"
      - "若刺激、發熱、發癢或香味過重則不用。"
  lock:
    - "準備玫瑰油不等於取得性行為同意。"
```

---

# 11｜定陶商會案活躍承接

```yaml
MERCHANT_CASE_CARRY_FORWARD:
  full_detail_source: "HOT_SAVE_V1.5"
  current_operational_state:
    - "十二車三烤鹽已追回；二十七人被捕，五人逃走。"
    - "京師三烤鹽停售封存，六烤鹽正運京。"
    - "銀庫交叉審計試行一個月。"
    - "急難護持案試行六個月。"
    - "涉案者分批押回定陶。"
    - "程景衡與師爺房繼續追查外圍節點。"
    - "目前沒有必須白御行立即回商會坐鎮的已知節點。"
  unresolved:
    - "吳六下落與罪責"
    - "五名逃犯"
    - "灰簿先生身份"
    - "借支文件抄件外洩路徑"
    - "押送者個別最終處置"
    - "白御行所殺背叛者名冊、正式紀錄及家屬援助落實"
  threat_state: "CONTAINED_BUT_NOT_CLOSED"
```

---

# 12｜人物關係與知情矩陣

```yaml
RELATION_MATRIX:
  bai_yuxing__zhang_lihua:
    state: "情人關係已成立"
    due: "槐月十六日晚私人花燭儀式"
    exclusivity: false
    marriage: false
    sexual_consent_for_tonight: "UNDECIDED_UNTIL_SCENE"

  bai_yuxing__li_shishi:
    state: "私人性關係持續；情感與追求未封閉"
    private_names:
      - "理理"
      - "御行"
    exclusivity: false
    pregnancy_state: "UNKNOWN"
    current_internal_ejaculation_rule: "NOT_ALLOWED_UNTIL_FURTHER_DECISION"

  bai_yuxing__li_pinger:
    state: "追求機會未關閉"
    established_romance: false
    established_sexual_relation: false
    current_joint_work:
      - "張麗華花燭採買"
      - "白玉池封池與阿泠營運評估"

  bai_yuxing__a_ling:
    state: "新識／互相調侃／研究合作間接成立"
    family_relation: false
    romantic_relation: false
    sexual_relation: false
    ownership: false

  su_qing__a_ling:
    state: "白玉池異常調查合作"
    trust_level: "FUNCTIONAL_NOT_FULLY_ESTABLISHED"

  pan_jinlian__white_jade_pool_anomaly:
    knowledge: "NOT_FORMALLY_INFORMED"
    spatial_relevance: "POTENTIALLY_HIGH_BUT_UNTESTED"
```

---

# 13｜未決事項

```yaml
OPEN_THREADS:
  immediate_today:
    - "李瓶兒向張麗華確認花燭夜是否照舊、是否設小飯、邀請誰。"
    - "完成紅衣、紅帳、紅被、蓋頭、喜燭、香料、酒菜與合巹酒採買。"
    - "白御行今晚是否準時赴張麗華房。"
    - "張麗華今晚是否仍同意象徵儀式與任何進一步身體親近。"

  white_jade_pool:
    - "來源不明的第一次『歸零』聲音是誰或什麼。"
    - "暗圈、數量回顯、文字回顯與條件句回顯的共同結構。"
    - "『續』字的意義、觸發條件與後果。"
    - "深水方格層是否屬於觀止空間、另一時空或其他結構。"
    - "阿泠與池底異常的真正關係。"
    - "阿泠是否與 MASTER 中白玉池無名女子同一存在。"
    - "何時、如何告知潘金蓮。"
    - "是否需要潘金蓮作空間宣告。"
    - "水療生意能否在安全確認後重啟。"

  li_shishi:
    - "月事是否如期。"
    - "是否私下找到可靠女醫。"
    - "避子方法是否取得、是否適用。"
    - "槐月十一日體內射精是否造成妊娠。"
    - "未來肛交只屬可能討論，未有同意或時間。"

  merchant_case:
    - "依第十一節未決事項持續。"

  minor_business:
    - "潘金蓮與白御行是否談定陶花香皂個人價或批發價。"
```

---

# 14｜接關約束

```yaml
CONTINUATION_LOCK:
  scene_entry:
    - "當前停在槐月十六日清晨白玉池池邊。"
    - "玩家已把白玉池問題交給蘇清、阿泠與李瓶兒繼續處理。"
    - "下一幕可由玩家決定離開白玉池、找張麗華、處理採買、休息或轉往其他事務。"
    - "不得替白御行自動去張麗華房、付款、答應潘金蓮或碰『續』。"

  zhang_lihua_lock:
    - "情人關係成立，不等於今晚性同意成立。"
    - "紅衣、蓋頭與花燭象徵不能用來推導妻妾、所有權或白家名分。"
    - "她可以改變飯席、賓客、儀式細節與身體安排。"
    - "她若關門、拒絕或要求改期，拒絕有效。"

  li_shishi_lock:
    - "她記得昨夜邊界事件與白御行的修正。"
    - "她與白御行有私人性關係，但沒有永久身體資格。"
    - "往後陰道性交不得內射，除非她另行明確改變決定。"
    - "懷孕與否保持未知，不得用幾日內的感覺直接判定。"

  a_ling_lock:
    - "阿泠保有名字、池域、是否現身、是否水療與是否接近他人的自主權。"
    - "不得再自行替她加白姓、親屬名分或女性關係。"
    - "不得將她與既有白玉池無名女子自動合併。"

  anomaly_lock:
    - "不得把計算器、液晶螢幕、人機介面或程式直接寫成客觀真相。"
    - "不得觸碰『續』或作空間宣告，除非玩家明示且現場人物完成風險判斷。"
    - "不得因一次 IF／THEN 成功便宣稱池底可以執行任意命令。"
    - "不得讓潘金蓮無來源地已知道封池真相。"

  merchant_lock:
    - "定陶商會威脅未結案。"
    - "不得把吳六直接定罪。"
    - "不得補出灰簿先生身份。"
    - "不得自行補齊被白御行殺死者的名冊與處置。"
```

---

# 15｜有效接關摘要

理火三年槐月十五日晚，白御行返回觀止。他先向張麗華索取答覆；張麗華明示接受成為其情人，但不立婚書、不入白家、不成為所有物，仍留在觀止並保有見面與身體決定權。雙方約定槐月十六日晚舉行私人情人花燭儀式，包含紅衣、紅蓋頭、紅帳、紅被、紅燭與合巹酒；任何性行為仍須當晚重新由張麗華決定。李瓶兒於槐月十六日上午先向張麗華確認安排，再以白御行私帳張羅物品與可能的小飯席，只請張麗華親口點名的人。

白御行其後赴李師師房。兩人確立私人稱呼「御行／理理」。白御行立即告知張麗華情人與花燭夜消息；李師師明示嫉妒，但不要求他毀約。白御行澄清自己剛從張麗華處得知答案，隨即來告知，紅娘尚未知情；李師師撤回隱瞞指責。白御行亦私下確認自己在定陶商會事件中殺死一批背叛者，並決定援助其家屬；確切名冊與執行情況未知。

白御行與李師師前往白玉池看星。池中女子在李師師邀請下現身，自選名字「阿泠」。她能控制泉水並提供精準水療，但拒絕白姓、白家親屬與白御行的所有權。李瓶兒試池後認為水療可形成生意，但尚未簽約、定價或對外營運。

白御行以「泠、靈、零、000」玩笑後，池底出現暗圈與來源不明的「歸零」聲音。後續算式可由池水回顯結果，並在池壁形成每六息明滅一次的「續」字。蘇清通宵測得：不同人皆可輸入；未完成算式可暫存至少半個時辰；「歸零」可清除待算內容；IF／THEN 真條件會先顯「真」再顯指定數量。這些只證明存在輸入、暫存、判斷與回顯現象，不證明其本體是計算器、液晶、程式或機器。白玉池已封池，阿泠不接客，水療停業，「續」未被觸碰。

李瓶兒確認潘金蓮具有向觀止提出空間宣告的權限，但不能任意控制結果。潘金蓮可能與「續」的空間展開有關，也可能因此承擔風險；她目前尚未被正式告知。

槐月十五日晚至十六日清晨，白御行與李師師共宿。白御行曾用「硬來」表述可能越過拒絕，李師師立即停止親密安排；白御行改口承認由她決定「來／不要」後，她重新允許赤裸相抱。兩人在明確同意、由她引導並等待適應後，以陰道相連方式入睡；白御行夜半前自然軟下滑出，夜間沒有射精。清晨李師師以手刺激，白御行射精，沒有陰道內射，李師師用口清理殘留。

槐月十一日第一次性交的體內射精仍構成未知妊娠風險；目前時間太早，沒有懷孕結論。李師師會記月事、找可靠女醫，在情況明白以前不允許未來陰道性交內射；若真的懷孕，是否留下最終由她決定。白御行明示自己害怕的是她在不想要的情況下懷孕。

**當前時間：理火三年槐月十六日清晨。**

**當前位置：觀止後院白玉池池邊。**

**當前狀態：白玉池封池調查中；張麗華花燭夜於今晚到期；故事暫停。**

---

## VERSION_STATUS

```yaml
ACTIVE_HOT_SAVE: "V1.6"
PREVIOUS_VALID_HOT: "V1.5"
HISTORICAL_VALID_HOT: "V1.4"
ILLEGAL_SAVE:
  version: "V1.3"
  use: "AUDIT_ONLY"
```
