# 觀止青樓｜白御行線 HOT SAVE V2.1
## 理火三年槐月十八日下午｜定陶商戰起局 × 蘇清二十八日私約 × 白玉池舊案補固 × 張麗華私下稱呼固化版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V2_1_HUAI18_AFTERNOON_TRADE_WAR_SUQING_PRIVATE_PACT_WHITE_JADE_POOL_CORRECTION"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V2.1"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  story_date: "理火三年槐月十八日"
  time_of_day: "下午／提早晚膳以前；精確時刻未定"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V2.0_槐月十八日清晨_四人家人夜結與蘇清履約瓶兒延後決定版.md"
  record_state: "STORY_HELD_FOR_HOT_SAVE; CURRENT_SCENE_READY"
  current_location: "觀止青樓／蘇清房間"
  present:
    - "白御行"
    - "蘇清"
  recently_departed:
    - "潘金蓮"
  save_scope:
    - "定陶商會與汴梁商戰之已發生佈局"
    - "常煒之副會長身分與執行權"
    - "沈萬三、西門慶、廣源轉運行之不同法位"
    - "白御行對潘金蓮投放之未證實消息與真實戰略意圖"
    - "白御行與蘇清之二十八天私人盟約"
    - "白玉池既有真相之玩家／GM補固"
    - "張麗華與白御行私下固定稱呼"
    - "當日晚膳與觀止內部生活接點"
```

---

# 0｜提交法位與版本說明

```yaml
COMMIT_NOTE:
  - "本檔取代 HOT V2.0，成為白御行線當前接關切片；V2.0仍為前置歷史來源。"
  - "本檔不更新 MASTER，不改寫原始人物卡或人物池。"
  - "張麗華私下稱呼屬白御行玩家線關係語言固化，不倒灌人物基線。"
  - "白玉池四項補充為玩家明示之既有事件校正；本線以本檔記錄為準。"
  - "蘇清二十八日之約雖不進觀止公開帳冊，仍以私人秘密契約保存，避免長線遺失。"
  - "白御行對潘金蓮所說『沈萬三要殺西門慶』只保存為白御行投放的消息，不升格為客觀事實。"
  - "商戰內所有人物判斷、流言與操作目的分開記錄；能力、嫌疑、敵意與實際涉案不得互相代換。"
```

```yaml
SOURCE_LINEAGE:
  previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V2.0_槐月十八日清晨_四人家人夜結與蘇清履約瓶兒延後決定版.md"
    role: "前置夜間關係、蘇清舊約、李瓶兒延後決定與張麗華陪伴線來源"
  white_jade_pool_previous_record:
    files:
      - "觀止青樓_白御行線_HOT_SAVE_V1.6_槐月十六日清晨_張麗華花燭前置與白玉池異常回顯封池版.md"
      - "觀止青樓_白御行線_HOT_SAVE_V1.7_槐月十六日午後_白玉池暫閉與張麗華花燭前入睡接關版.md"
    role: "白玉池先前可觀察事件來源；其中仍標記未知之處，由本輪玩家既有事件校正補足"
  novel_source:
    file: "觀止青樓第1-8卷 (1).md"
    role: "沈萬三由明朝線接入觀止及盤商合作之既存來源"
```

---

# 1｜當前時間、位置與生活線

```yaml
CURRENT_SCENE:
  date: "理火三年槐月十八日"
  time: "下午／提早晚膳前；精確時刻未知"
  location: "觀止青樓／蘇清房間"
  story_mode: "HOLD_FOR_SAVE"
  present:
    - "白御行"
    - "蘇清"
  current_scene_last_subject: "白玉池開張前確認與整理"
  next_action_owner: "PLAYER_OR_WORLD_AFTER_RESUME"
```

```yaml
DAY_PLAN:
  white_yuxing:
    - "白御行明示槐月十八日不離開觀止。"
    - "白御行明示槐月十九日回定陶商會處理商戰後續。"
  midday:
    - "白御行與張麗華決定中午不吃，晚膳提早。"
  dinner_location: "張麗華房間"
  dinner_plan:
    - "燉軟羊肉，多放蘿蔔並去膻。"
    - "蒸魚，多放蔥薑。"
    - "兩樣青菜。"
    - "熱湯／較清的醒酒湯。"
  preparation:
    responsible_actor: "李瓶兒"
    confirmed:
      - "李瓶兒已令廚下汆羊肉、準備蘿蔔與清湯。"
      - "魚將晚些再殺，以免肉散。"
      - "李瓶兒會提早將晚膳送到張麗華房裡，並遣人尋白御行。"
  white_yuxing_commitment:
    - "白御行向張麗華明示晚餐再回來。"
  unfinished:
    - "晚膳尚未開始。"
    - "蘇清是否同席未由本輪另行確認，但廚下先前已多備碗筷。"
```

---

# 2｜槐月十八日商會密會：常煒與定陶商戰起局

## TRADE18-E01｜常煒到觀止密會

```yaml
EVENT_RECORD:
  event_id: "TRADE18-E01-CHANGWEI_SECRET_MEETING"
  status: "COMPLETED"
  location: "觀止青樓／密會房間"
  participants:
    - "白御行"
    - "常煒"
    - "送信帳房／商會人員（姓名未固化）"
  actor_identity:
    常煒: "定陶商會副會長"
  privacy_action:
    - "白御行命張麗華、蘇清、李瓶兒等女人離開，將此定為商會密會。"
  confirmed_case_state:
    - "三家分號出現以舊帳務方式製造自然結清的異常帳。"
    - "前案已被宣布結案後，仍有人繼續收取舊帳材料、補洞並追查送信人。"
    - "商會認定此為結案後的再次出手，不再只是舊案未清。"
```

## TRADE18-E02｜沈萬三在本案的法位

```yaml
SHEN_WANSAN_POSITION:
  baseline_identity:
    status: "EXISTING_GUANZHI_CHARACTER"
    origin: "明朝線接入觀止"
    roles:
      - "觀止明朝線代理商"
      - "潘金蓮合作盤商"
      - "花魁賽／品花局外盤、跨地域資金與消息網節點"
  current_case_status: "POSSIBLE_TARGET_OR_HIGH_CAPABILITY_RELATED_NODE; NOT_LOCKED"
  confirmed_reason_for_inclusion:
    - "其舊部／代理網路與跨區資金能力符合部分能力模型。"
    - "沈萬三與定陶商會真正重疊的主要競爭場域，是當前時代的汴梁。"
  not_confirmed:
    - "沈萬三本人參與異常調帳。"
    - "沈萬三授意廣源轉運行。"
    - "沈萬三要殺西門慶。"
    - "沈萬三已把定陶商會視為敵人。"
    - "沈萬三背叛觀止或潘金蓮。"
  strategic_constraint:
    - "白御行與常煒均認為直接與沈萬三全面對抗至少可能兩敗俱傷，不作第一擊目標。"
```

## TRADE18-E03｜廣源轉運行與許奉年成為第一擊目標

```yaml
TARGET_STATE:
  target_name: "汴梁廣源轉運行"
  responsible_person: "許奉年"
  target_class: "REAL_ENEMY_SELECTED_FOR_VISIBLE_DEFEAT"
  confirmed_case_links:
    - "三家分號異常帳中至少兩筆經過廣源轉運行，表面為補運費，實際形成舊貨款結清憑據。"
    - "前案結案後第二日，許奉年方面買走死去帳房家中的舊手簿。"
    - "送信帳房離開定陶以前，有人打聽其住處。"
  power_assessment_by_changwei:
    - "廣源在汴梁有貨棧與城外短線，有分量但承受不了定陶商會斷貨、斷帳、斷信用的合擊。"
  strategic_role:
    - "必須是確實再次出手的敵人，不是純替罪羊。"
    - "可被定陶力量壓倒，並讓商會對外宣布已取得勝利。"
    - "其被擊倒後若仍有人再次出手，則另立下一回戰事。"
```

## TRADE18-E04｜白御行對常煒的作戰指令

```yaml
PLAYER_DIRECTIVE:
  actor: "白御行"
  recipient: "常煒"
  confirmed_orders:
    - "讓定陶商會立即動起來。"
    - "以廣源轉運行／許奉年為可被碾過的真敵人。"
    - "把西門慶拉進事件，使火勢自然燒到他身上。"
    - "將人、銀路、貨路、盤口與時間編得密，使外界自然聯想；關聯不必全部真實。"
    - "不必製造一樁容易被查穿的單一假案，而是利用真實片段與模糊連接製造推斷場。"
    - "對商會自己人不公開揭底，以敲打、差異查核與觀察反應為主。"
    - "槐月十九日由白御行回商會查看後續。"
  declared_end_condition:
    - "廣源等真敵人停止再出手，則本回可宣告結束。"
    - "已結案後仍再次出手者，被視為拒絕和解，另開下一回。"
```

## TRADE18-E05｜常煒之執行方案與已發生初步效果

```yaml
CHANGWEI_EXECUTION_PLAN:
  executor: "常煒"
  status: "ACTIVE"
  external_actions:
    - "定陶體系暫緩廣源轉運行票據兌付，名義為帳目重核。"
    - "向廣源發出查帳公函，查問舊帳、手簿與經手人。"
    - "向西門慶發出另一封公函，只查近三月是否替廣源兌過銀票。"
    - "令與西門慶有舊怨的掮客接觸廣源資金流入汴梁娛樂盤口的消息。"
  internal_actions:
    - "三家分號收到不同查核項目，用於觀察誰急於補帳、燒紙或找人。"
    - "內部有異動者先記錄，不立即抓、不立即審、不公開。"
  shen_wansan_policy:
    - "暫不直接接觸或挑釁沈萬三。"
    - "觀察廣源與西門慶起火後，沈萬三是否調人、撤線、詢問或毫無反應。"
  confirmed_initial_effects:
    - "廣源轉運行第一張票據已在定陶商會櫃上被蓋『暫緩兌付』並退回。"
    - "至少兩名平日與西門慶稱兄道弟者已開始私下詢問其近日盤口數字。"
  not_yet_confirmed:
    - "西門慶是否已收到正式公函。"
    - "廣源是否已正式反應。"
    - "沈萬三是否已知情。"
    - "任何目標是否已實際倒台。"
```

---

# 3｜西門慶火線與潘金蓮會談

## PAN18-E01｜白御行召潘金蓮至蘇清房內

```yaml
EVENT_RECORD:
  event_id: "PAN18-E01-PRIVATE_WARNING_OPERATION"
  status: "COMPLETED_MEETING"
  location: "蘇清房間"
  participants:
    - "白御行"
    - "蘇清"
    - "潘金蓮"
  covert_signal:
    - "白御行在桌下輕踢蘇清，示意她先聽、不拆話、不過度推測。"
    - "蘇清收到提示後沒有替白御行補充或反駁。"
```

## PAN18-E02｜投放給潘金蓮的消息與其法位

```yaml
MESSAGE_RECORD:
  speaker: "白御行"
  recipient: "潘金蓮"
  message_claims:
    - "有人要對西門慶開刀，勢力大到白御行也不敢惹。"
    - "要殺西門慶的人是沈萬三。"
    - "原因可能是商場，也可能是女人；白御行聲稱自己不知道。"
  objective_status: "UNVERIFIED_OPERATIONAL_CLAIM"
  not_world_fact:
    - "沒有確認沈萬三要殺西門慶。"
    - "沒有確認白御行真不知道原因。"
    - "沒有確認白御行客觀上不敢惹對方。"
  later_disclosed_player_intent_to_suqing:
    - "白御行本就預期潘金蓮不會完全相信。"
    - "目的在促使潘金蓮切帳、封銀或傳訊，引發西門慶周邊過度反應。"
    - "待西門慶瘋狂自救並咬向沈萬三，迫使沈萬三不得不實際反擊。"
    - "若兩者原本有勾連，則期待其形成窩裡反。"
```

## PAN18-E03｜潘金蓮的可觀察反應與已表態措施

```yaml
PAN_JINLIAN_RESPONSE:
  belief_state: "DID_NOT_FULLY_ACCEPT; EXACT_PRIVATE_JUDGMENT_UNKNOWN"
  confirmed_position:
    - "她不願以替西門慶擋沈萬三為念舊方式。"
    - "她區分西門慶個人資產與觀止盤口、沈萬三外盤資金。"
    - "若火燒入觀止盤口，她會把出手者視為自己的敵人。"
  declared_actions:
    - "先切分盤口帳目。"
    - "賭客本金與應付彩金照帳，不得因西門慶風險而扣留。"
    - "沈萬三經手之外盤銀另封另算。"
    - "西門慶自己的水錢、墊銀、抽頭與未結分成，可延後兩日交割。"
    - "以重核大額分成、防冒領為公開理由。"
    - "不直接向沈萬三詢問，以免暴露消息外洩。"
    - "考慮向西門慶送出不提沈萬三、不提商會、不提白御行來源的模糊警告。"
  warning_status: "DECLARED_INTENT; DELIVERY_NOT_YET_OBSERVED"
  relational_note:
    - "潘金蓮明示替白御行保密不是白送的人情；未形成具體價碼或正式契約。"
```

## 西門慶目前位置

```yaml
XI_MENQING_CURRENT_STATE:
  baseline_roles:
    - "觀止花魁賽／品花局公開賭盤前台收注者之一。"
    - "與潘金蓮、沈萬三之盤口結構存在不同層次合作。"
  case_status:
    - "尚未證明參與定陶異常帳或廣源收尾。"
    - "已被白御行與常煒刻意拉進外界推斷場。"
    - "其狐朋狗友與周邊利益者已開始出現自保性詢問。"
  not_confirmed:
    - "西門慶已知自己被針對。"
    - "西門慶已咬向沈萬三。"
    - "西門慶已失去盤口、財產或人身安全。"
    - "西門慶已被毀。"
```

---

# 4｜蘇清二十八日私人盟約

## PRIVATE-Pact-SQ28｜擊掌為盟

```yaml
PRIVATE_PACT:
  pact_id: "PRIVATE-BYX-SUQING-28DAY-LIFE-PACT-001"
  status: "AGREED_NOT_YET_TRIGGERED"
  parties:
    - "白御行"
    - "蘇清"
  formation_event:
    - "白御行提出：若他毀掉西門慶、替蘇清報仇，蘇清在他身邊生活二十八天。"
    - "蘇清接受談判後，雙方擊掌為盟。"
  institutional_status:
    - "不進觀止公開帳冊。"
    - "不是觀止對外契約。"
    - "本 HOT SAVE 只為世界連續性保存其存在與保密範圍。"
  knowledge_scope:
    - "白御行"
    - "蘇清"
  trigger:
    required_event: "西門慶被白御行之局真正毀掉／失去原有位置，使蘇清之仇得到實質報償。"
    current_state: "NOT_MET"
    exact_threshold: "若未來對是否已達成存在爭議，需由當時可觀察結果與雙方明示確認，不得由導演單方面偷算。"
  duration:
    value: 28
    unit: "DAY"
    start: "觸發條件成立後"
    exact_calendar_method: "NOT_YET_SPECIFIED"
  content:
    core: "蘇清在白御行身邊共同生活二十八天，重點是日常生活，而非單一工作或單一性服務。"
    possible_activities:
      - "跟隨白御行學做生意。"
      - "陪同應酬。"
      - "陪白御行追求或接觸其他女人。"
      - "一起發呆、無事度日。"
      - "在雙方當下同意下發生性行為，時間與形式不預先鎖定。"
  consent_boundary:
    - "二十八天共同生活不等於預先同意所有性行為、行程、工作或命令。"
    - "每一具體親密行動仍由當時雙方決定。"
    - "蘇清不是丫鬟、護衛或無條件服從的軍師。"
    - "蘇清保留批評、拒絕、嘲笑或不配合特定事項的權利。"
  separation_from_old_contract:
    - "本私人盟約與舊五百兩／三夜未結帳完全分開。"
    - "不得用同一日同時抵銷舊約與二十八天私約，除非雙方日後另行明示重議。"
```

## 舊約仍然有效

```yaml
OLD_SUQING_CONTRACT:
  contract_id: "CONTRACT-H17-SUQING-2DAY-HOUSEHOLD-001"
  state: "ACTIVE_FINAL_DAY_IN_PROGRESS"
  current_date: "槐月十八日"
  debtor_creditor_direction:
    debtor: "蘇清"
    creditor: "白御行"
  remaining:
    - "槐月十八日最後一日共同生活至原約定結束時間。"
  not_settled:
    - "本日上午／下午事件尚未宣告舊五百兩帳正式結清。"
  no_merge:
    - "不得將蘇清二十八日私約倒灌成舊約延長。"
```

---

# 5｜白玉池既有事件補固與當前狀態

```yaml
WHITE_JADE_POOL_GM_CORRECTION:
  status: "GM_CONFIRMED_ROUTE_EVENT; SOLIDIFIED_IN_HOT_V2_1"
  correction_reason:
    - "此線早期已跑過完整事件，但舊 SAVE 未完全保存，導演一度誤以為真相仍未知。"
  confirmed_existing_facts:
    - "時空道人已在眾人決議同意後補上白玉池的洞。"
    - "白玉池對面顯現／連接的是白御行的黑暗面。"
    - "對面屬另一個空間。"
    - "通過該處會造成時間線與空間定位混亂。"
    - "此前已做過小規模實驗，確認穿越會引發時空錯亂風險。"
    - "現在白玉池已封池，基本沒有持續性問題。"
  current_required_work:
    - "開張前重新確認補洞處與封池後狀態穩定。"
    - "確認沒有新的回顯、滲漏或時空異常。"
    - "完成清池、換水、浴具、帷帳、燈火等營業整理。"
  current_risk_status: "SEALED_AND_BROADLY_STABLE; PREOPENING_CONFIRMATION_PENDING"
  prohibited_regression:
    - "不得重新把白玉池寫成原因完全未知、仍需破解的主線謎案。"
    - "不得由蘇清單方面取得永久封池或否決開張的最終裁決權。"
    - "不得在沒有新事件的情況下聲稱通道重新打開。"
```

```yaml
WHITE_JADE_POOL_CURRENT_TASK:
  assigned_by: "白御行"
  tasked_actor: "蘇清"
  instruction:
    - "有空時收拾白玉池，因為總要重新開張，不能永久放置。"
  corrected_interpretation:
    - "蘇清負責確認穩定、整理與準備營業，不是重啟舊案。"
  completion_state: "NOT_STARTED_OR_NOT_YET_OBSERVED"
```

---

# 6｜張麗華 × 白御行私下稱呼固化

```yaml
RELATIONAL_LANGUAGE_CANON:
  record_id: "REL-LANG-BYX-ZLH-PRIVATE-APPELLATIONS-001"
  lifecycle: "GM_CONFIRMED_ROUTE_CANON"
  scope: "白御行玩家線／兩人私下場合"
  confirmed_default_terms:
    zhang_lihua_to_bai_yuxing: "官人"
    bai_yuxing_to_zhang_lihua: "小娘子"
  application:
    - "兩人私下、親密、日常房內交流時，以此作為既有且自然的默認稱呼。"
    - "角色可因爭執、戲弄、商務、公開場合或特定情緒暫時改用其他稱呼，但不得因此遺忘本項既有關係語言。"
  boundaries:
    - "此稱呼固化本身不單獨建立法定婚姻、排他或妻妾名分。"
    - "不得倒灌為張麗華對所有玩家線或所有人物的固定稱呼。"
```

---

# 7｜主要人物當前硬狀態

```yaml
ACTOR_STATE:
  白御行:
    location: "蘇清房間"
    day_plan:
      - "今日不離開觀止。"
      - "提早晚膳時回張麗華房間。"
      - "明日回定陶商會。"
    active_actions:
      - "已將定陶商戰執行交給常煒。"
      - "已向潘金蓮投放沈萬三欲殺西門慶之未證實消息。"
      - "已與蘇清成立二十八日私人盟約。"
    unknown:
      - "商戰第一日實際反應。"
      - "潘金蓮是否已送出警告。"
      - "西門慶與沈萬三是否會形成實際衝突。"

  蘇清:
    location: "自己房間"
    knowledge:
      - "知道白御行投放消息的真實戰略意圖。"
      - "知道常煒商戰線的大致方向，但未必知道全部商會內部名單與公函細節。"
      - "知道並參與二十八日私人盟約。"
    obligations:
      - "舊五百兩契約最後一日仍在進行。"
      - "白玉池整理與開張前確認為待辦，不是立即完成。"
    relation_state:
      - "與白御行之二十八日私約已成立但未觸發。"
      - "與白御行之愛情仍未建立；私約不自動改寫感情。"

  張麗華:
    current_location: "觀止內；精確房間未持續追蹤"
    confirmed:
      - "已點提早晚膳，等待白御行晚上回房。"
      - "私下稱白御行『官人』已固化。"
      - "白御行私下稱她『小娘子』已固化。"
    knowledge_limit:
      - "她知道上午有商會密會，未確認知道常煒完整佈局。"
      - "未確認知道白御行對潘金蓮投放的沈萬三消息。"

  李瓶兒:
    current_location: "觀止後廚／觀止內；精確位置未持續追蹤"
    confirmed:
      - "負責提早晚膳準備。"
      - "與白御行的關係、生育與正式位置仍延後決定。"
    knowledge_limit:
      - "未確認知道商戰密會內容。"

  潘金蓮:
    current_location: "已離開蘇清房間；精確位置未持續追蹤"
    knowledge:
      - "聽見白御行聲稱沈萬三要殺西門慶。"
      - "知道西門慶可能受到大勢力針對。"
      - "不知道白御行已向蘇清明說的完整操盤意圖。"
    active_intent:
      - "切分盤口帳、保護賭客本金、延後西門慶部分分成。"
      - "可能向西門慶送模糊警告。"
```

---

# 8｜知情矩陣

```yaml
KNOWLEDGE_MATRIX:
  常煒商戰完整指令:
    knows:
      - "白御行"
      - "常煒"
      - "在場送信商會人員（僅限其實際聽見部分）"
    does_not_automatically_know:
      - "張麗華"
      - "李瓶兒"
      - "潘金蓮"
      - "西門慶"
      - "沈萬三"

  潘金蓮收到的沈萬三消息:
    knows:
      - "白御行"
      - "蘇清"
      - "潘金蓮"
    objective_truth: "UNCONFIRMED"

  白御行真正挑動意圖:
    knows:
      - "白御行"
      - "蘇清"
    may_infer_but_not_confirmed:
      - "潘金蓮"

  蘇清二十八日私約:
    knows:
      - "白御行"
      - "蘇清"
    secrecy: "PRIVATE; NOT_GUANZHI_PUBLIC_LEDGER"

  白玉池補固真相:
    route_fact: "GM_CONFIRMED"
    exact_original_participants: "依早期事件；本 HOT 不補造完整名單"
    current_operational_knowledge:
      - "白御行"
      - "蘇清（至少已被交代整理；早期完整知情範圍依舊事件）"

  張麗華私下稱呼:
    knows:
      - "白御行"
      - "張麗華"
    status: "ROUTE_CANON"
```

---

# 9｜禁止污染與未決事項

```yaml
ANTI_CORRUPTION_LOCKS:
  - "不得把『沈萬三要殺西門慶』當成已確認世界事實。"
  - "不得把沈萬三的盤商與代理商身分直接等同於定陶案幕後主使。"
  - "不得把西門慶被拉入流言場寫成他已經倒台。"
  - "不得把廣源轉運行作為真敵人，改寫成所有證據與敘事聯繫都必然真實。"
  - "不得把白御行的操盤目的改寫成潘金蓮、常煒或沈萬三的內心。"
  - "不得把蘇清二十八日私約當成觀止公開契約、賣身契、無條件性同意或舊約延長。"
  - "不得忘記蘇清舊約最後一日仍未正式結清。"
  - "不得重新把白玉池寫成完全未知或正在失控；除非新事件提供可觀察證據。"
  - "不得把張麗華『官人／小娘子』私稱升格成已婚法位。"
  - "不得讓商戰線吞掉當日晚膳、張麗華陪伴、李瓶兒延後決定與蘇清最後一日生活線。"
```

```yaml
UNRESOLVED:
  trade_war:
    - "廣源與許奉年將如何反應。"
    - "西門慶是否收到公函或潘金蓮警告。"
    - "西門慶周邊是否開始切割、分食或向沈萬三發難。"
    - "沈萬三是否實際涉案、被利用、被嫁禍、旁觀或反擊。"
    - "常煒差異查核會釣出哪些商會內部異動者。"
  relationships:
    - "蘇清舊約何時正式結清。"
    - "蘇清二十八日私約是否與何時被觸發。"
    - "李瓶兒於兩日後對關係與孩子問題的回答。"
    - "張麗華三日陪伴線後續。"
  white_jade_pool:
    - "開張前檢查結果。"
    - "實際重新開張日期與營業規則。"
```

---

# 10｜下一幕接關

```yaml
RESUME_POINT:
  date: "理火三年槐月十八日下午"
  location: "蘇清房間"
  present:
    - "白御行"
    - "蘇清"
  immediate_state:
    - "潘金蓮已離開。"
    - "二十八日私約已擊掌成立但尚未觸發。"
    - "白玉池舊案真相已由玩家補固，當前只待開張前確認與整理。"
    - "常煒已在外執行商戰佈局。"
    - "白御行今日不離開觀止，提早晚膳將在張麗華房間進行。"
  next_world_hinges:
    - "蘇清回應白玉池整理或轉入當日日常。"
    - "廚下／李瓶兒來請提早晚膳。"
    - "潘金蓮切帳後的第一個盤口反應。"
    - "常煒送回第一輪商戰消息，但普通消息不必立刻打斷生活場。"
  player_decision_required_now: false
```

---

# 11｜接關硬提示

```yaml
DIRECTOR_QUICK_LOAD:
  - "目前是槐月十八日下午，白御行與蘇清在蘇清房內。"
  - "常煒是定陶商會副會長，已執行廣源轉運行／許奉年第一擊與西門慶流言牽引。"
  - "沈萬三是明朝線代理商、潘金蓮合作盤商；可能關聯但完全未鎖定。"
  - "白御行告訴潘金蓮『沈萬三要殺西門慶』是操盤消息，不是已證實真相。"
  - "潘金蓮不全信，但準備切帳、保賭客錢、延後西門慶部分分成，可能送出模糊警告。"
  - "白御行與蘇清擊掌成立私密二十八日共同生活盟約；西門慶真正被毀後才觸發，舊約另算。"
  - "白玉池洞已由時空道人在眾人同意下補好；對面是白御行黑暗面與另一空間，穿越會擾亂時空；目前封池穩定，只待開張確認。"
  - "張麗華私下稱白御行『官人』；白御行私下稱張麗華『小娘子』。"
  - "提早晚膳在張麗華房間，李瓶兒已準備羊肉、蒸魚、青菜與熱湯；白御行承諾晚餐回去。"
```

> **當前畫面：潘金蓮已帶著不全信的消息離去；常煒在汴梁把第一張票據退回，蘇清房內則留下兩人擊掌後的私帳。白玉池不再是待破解的舊洞，只待確認與整理。晚膳的羊肉已下鍋，張麗華的小娘子房裡還留著官人的位置。**
