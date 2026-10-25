# 觀止青樓｜白御行線 HOT SAVE V1.7
## 理火三年槐月十六日午後｜白玉池異常通道暫閉 × 時空道人漏籤追責 × 張麗華花燭前入睡接關版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V1_7_HUAI16_AFTERNOON"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V1.7"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime: "GUANZHI_QINGLOU_V10_0"
  patch_runtime: "GUANZHI_QINGLOU_V10_1_PATCH_EVENT_RENDER_ORTHOGONAL"
  story_date: "理火三年槐月十六日午後"
  record_state: "ACTIVE_PAUSED_PLAYER_ASLEEP"
  save_scope:
    - "張麗華情人花燭當日確認、時辰與私人儀式安排"
    - "白玉池異常通道、對側存在、活物與事件傳遞測試"
    - "時空道人槐月十五日晚漏籤與當場接線調查"
    - "白玉池暫閉合、封池與監測規則"
    - "白御行不回商會、授權副會長與重大回報門檻"
    - "蘇清共浴拒絕、小翠擦背服務邊界與實際結果"
    - "白御行花燭前入睡及酉初接關點"

SOURCE_LINEAGE:
  previous_valid_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V1.6_槐月十六日清晨_張麗華花燭前置與白玉池異常回顯封池版.md"
    role: "本輪以前的直接有效 HOT 來源"
  previous_valid_hot_2:
    file: "觀止青樓_白御行線_HOT_SAVE_V1.5_槐月十五日傍晚_師理理初次肉體與定陶商會案雙線接關版.md"
    role: "定陶商會案與此前關係事件的完整承接來源"
  valid_master:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版.md"
    role: "長期因果與人物線歷史來源"
  forbidden_source:
    file: "HOT_SAVE_V1.3"
    status: "ILLEGAL_CORRUPTED_SAVE"
    use: "AUDIT_ONLY"
  character_sources:
    - "觀止人物卡_LCAPG_V1.1-R1_原始重構去污染版_含辭歲_導演隱藏區增補.md"
    - "觀止人物池_LCAPG_V1.1_紅娘氏與李師師雙人正式版.md"

SOURCE_INTEGRITY_LOCK:
  - "本檔只固化槐月十六日清晨至午後本輪已發生、可觀察、人物明示或玩家對自身行動的有效確認。"
  - "白玉池對側的本體、世界位置、時間結構與存在身分均未查明。"
  - "黑洞海、黑洞／白洞、微型宇宙通道、疊加態、神之影、熵與人類智慧等內容，依來源分別保存為玩家假說、神話敘述或角色推論；不得升格為客觀宇宙真相。"
  - "MASTER 中『白玉池無名女子』不得與阿泠、提燈女子或門後其他存在自動合併。"
  - "時空道人、黑影、未知聲音與提燈女子的自述不自動等於世界事實。"

COMMIT_NOTE:
  - "本檔取代 V1.6，成為白御行線當前 HOT 接關切片。"
  - "V1.6 保留槐月十五日晚至十六日清晨師理理、張麗華與白玉池初始異常的完整事件細節。"
  - "V1.5 保留定陶商會案完整活躍狀態。"
  - "本檔將事件軸、人物解讀軸、研究假說軸、同意軸與安全處置軸分開記錄。"
```

---

# 1｜當前時間、位置與暫停點

```yaml
CURRENT_TIME:
  era: "理火三年"
  calendar_date: "槐月十六日"
  time_of_day: "午後，午正後，尚未至酉初"
  exact_minute: "UNKNOWN_NOT_REQUIRED"
  certainty: "CONFIRMED_RANGE"

CURRENT_SCENE:
  location: "觀止西側醒酒小房"
  scene_state: "PLAYER_ASLEEP_BEFORE_FLOWER_CANDLE"
  player_present:
    - "白御行"
  immediate_guard_state:
    - "房門未上鎖。"
    - "門外掛有『白總歇息，船沒沉不准敲門』木牌。"
    - "潘金蓮另補：『張麗華叫人除外』。"
  next_action_owner: "WORLD_AT_WAKE_TRIGGER_THEN_PLAYER"

PLAYER_STATE:
  body:
    - "已在客浴完成洗頭、擦背與自行清洗。"
    - "已換上乾淨中衣。"
    - "上午封池與抓取活物造成的池泥、青苔已清除。"
  fatigue:
    - "此前連續處理定陶商會事件四日。"
    - "槐月十五日晚至十六日清晨睡眠不足，上午又處理白玉池異常。"
  sleep_state: "已入睡"
  sexual_state:
    - "槐月十六日清晨曾射精一次，未陰道內射。"
    - "客浴期間未發生新增性行為。"
  clothing_for_evening:
    - "李師師已送來傍晚可穿的外袍，掛在房內衣架。"

WAKE_TRIGGER:
  planned: "酉初由觀止人員喚醒"
  reason:
    - "預留半個時辰醒神、更衣。"
    - "酉正張麗華房點紅燭。"
    - "戌初張麗華房門開，白御行須準時到場。"
  wake_immediately_only_if:
    - "觀止失火"
    - "觀止內發生死亡"
    - "觀止遭襲"
    - "白玉池通道重新開啟或封池失效"
  do_not_wake_for:
    - "一般帳目"
    - "普通客人"
    - "既定商會貨務"
    - "通常商會消息"
    - "實際船務事故亦先由副會長處理，除非另構成觀止或玩家線即時生死危機"
```

---

# 2｜張麗華：槐月十六日當日確認與花燭時辰

## ZLH16-E01｜張麗華當日書面／口頭安排

```yaml
EVENT_RECORD:
  event_id: "ZLH16-E01"
  time: "槐月十六日清晨至上午"
  status: "COMPLETED_CONFIRMATION"
  source: "張麗華傳話／紙條，由觀止內部人員轉達"

ZHANG_LIHUA_INSTRUCTION:
  confirmed:
    - "紅衣、紅帳照原安排。"
    - "不得使用『囍』字。"
    - "不得加入白家徽記、白家名物或足以使外人誤認正式婚禮的裝飾。"
    - "只請龐春梅喝第一杯酒，之後離開。"
  direct_question_to_bai:
    - "『白御行，今夜你是來看我穿紅，還是來把我放進你早已寫好的故事裡？』"
  player_response:
    - "白御行表示照張麗華安排、聽她的。"
    - "白御行以『新娘今天最大』作個人稱呼。"
  legal_state:
    - "白御行的『新娘』稱呼不改變既有情人法位。"
    - "張麗華未接受妻名、夫人名、婚姻名分或白家身分。"
```

## ZLH16-E02｜佈置、人員與時辰

```yaml
FLOWER_CANDLE_TODAY:
  status: "ACTIVE_DUE_TODAY"
  location: "張麗華房間"
  symbolic_structure:
    - "張麗華穿紅衣。"
    - "房中使用紅帳、紅燭與私人花燭佈置。"
    - "可有合巹酒與兩人私席。"
  forbidden_public_wedding_signals:
    - "囍字"
    - "白家徽記"
    - "妻／夫人稱呼"
    - "公開收賀"
    - "對外宣稱張麗華出嫁"
  participant_plan:
    - "龐春梅喝第一杯酒後離開。"
    - "李師師已獲張麗華允許，於白日替她梳頭。"
    - "李瓶兒處理採買、紅帳、酒席與實務安排。"
  time_schedule:
    "酉正": "張麗華房點紅燭；龐春梅飲第一杯。"
    "戌初": "房門開；白御行可赴約。"
    late_rule: "張麗華明示過時不候；她可關門。"
  authority:
    - "沒有請陰陽先生。"
    - "沒有依黃曆裁定。"
    - "張麗華表示她今日穿紅，由她決定吉時。"

CONSENT_LOCK:
  - "情人花燭與穿紅安排已成立。"
  - "今晚任何身體接觸、性行為、是否進房後繼續及進行到何處，仍須由張麗華當場決定。"
  - "白御行的『討老婆』『新娘』與性玩笑不構成張麗華同意。"
  - "張麗華可以拒絕、停止、延後或更改任何親密內容。"
```

---

# 3｜白玉池異常通道：事件軸

## BYX16-E01｜「續」字轉為黑色門縫

```yaml
EVENT_RECORD:
  event_id: "BYX16-E01"
  time: "槐月十六日清晨"
  location: "白玉池"
  observable:
    - "池中『續』字停在最亮狀態。"
    - "其後出現黑色細線，形態近似一道門縫。"
    - "門後呈現夜色、遠燈、濕臺階、鞋與不明深處。"
    - "門後曾傳來三次敲擊。"
    - "白玉池原有封池紅繩仍在，物理封池沒有自動解除。"
  not_proven:
    - "黑線是否真正空間門"
    - "門後是否另一宇宙、未來、過去、死後世界或觀止內部空間"
```

## BYX16-E02｜語言互動與對側存在

```yaml
OBSERVED_ENTITIES_OR_VOICES:
  lamp_woman:
    label: "提燈女子"
    status: "UNIDENTIFIED_INTERACTIVE_PRESENCE"
    observable:
      - "可聽見觀止側語言並回應。"
      - "能提出問題。"
      - "能在對側持燈、移動並接取部分送入物。"
      - "自述能辨識事件先後，但無法提供穩定經過時長。"
    unknown:
      - "姓名"
      - "身分"
      - "是否為人"
      - "是否曾在白玉池或觀止出現"
      - "是否能離開對側"

  near_breathing_voice:
    label: "貼近提燈女子的未知聲音"
    status: "UNIDENTIFIED_VOICE"
    observable:
      - "曾貼近女子耳側發聲。"
      - "會模仿、提問、提出解讀與威脅性論述。"
      - "未見可確認身體。"
    unknown:
      - "是否單一存在"
      - "是否控制門、鞋、白點或其他現象"
      - "是否能穿越"

  black_shadow:
    label: "門後黑影／由白御行投影分離出的未知存在"
    status: "INDEPENDENT_UNKNOWN_AFTER_SEPARATION"
    observable:
      - "由白御行無影投影事件中分離，最後留在門後。"
      - "曾持有字籤，字樣依事件由『來』變為『等』再變為『看』。"
      - "曾自行作出不跨門、留在對側的決定。"
    unknown:
      - "本體"
      - "是否仍與白御行因果相連"
      - "是否為神之影、暗面、錯誤收斂產物或其他存在"

  shoes_and_white_points:
    status: "UNEXPLAINED_ENVIRONMENTAL_PHENOMENA"
    observable:
      - "門後存在大量不同式樣的鞋。"
      - "鞋會轉向、移動或伴隨聲音。"
      - "深處曾亮起大量成對白點。"
    forbidden_inference:
      - "不得直接稱亡魂、死者、受害者或人數。"
```

## BYX16-E03｜「四十二」與初步語義回顯

```yaml
FORTY_TWO_TEST:
  initiator: "白御行"
  operator: "蘇清協助提問與觀察"
  observable:
    - "池中先出現四十二個小光點。"
    - "光點曾呈現四／十二、其後六等分組變化。"
    - "最後留下『問』字。"
    - "白御行表示想不到好答案後，池中曾顯示『我也』三息。"
  conclusion_limit:
    - "只能確認現象會對語句作變化回顯。"
    - "不能確認其理解宇宙梗、計算意義或具有人類意識。"
```

## BYX16-E04｜命名與時間問題

```yaml
PLAYER_LANGUAGE_INPUTS:
  black_hole_sea:
    content:
      - "白御行提出『黑洞海』作對側暫稱。"
      - "白御行解釋『海』不是客觀無限，而是相對於某個觀察者數不清的物質集合。"
      - "數不清的水可稱海；數不清的星可稱星海；人數不清可稱人海。"
    world_status: "PLAYER_PROPOSED_NAME_NOT_CANONICAL_LOCATION_NAME"
    observable_reaction:
      - "提燈女子與未知聲音能重複、追問並使用『海』概念。"
      - "門後環境對該詞曾出現白點、鞋與聲音變化。"

  space_time_question:
    content:
      - "白御行以『宇為空間、宙為時間』向提燈女子詢問其側經過多久。"
    observable_response:
      - "提燈女子能排列對話事件先後。"
      - "她無法說明經過時長。"
      - "觀止側亦出現日影、墨跡乾燥與前院木魚次數不完全一致的計時現象。"
      - "門上水珠曾映出不同天空與疑似不同事件排列。"
    not_proven:
      - "對側沒有時間"
      - "時間逆流"
      - "平行世界"
      - "預知"
```

---

# 4｜時空道人：召回、漏籤與接線調查

## TD16-E01｜召集觀止門口周圍生物

```yaml
EVENT_RECORD:
  event_id: "TD16-E01"
  player_order:
    - "白御行判斷異常可能與時間節點及時空道人有關。"
    - "他命小廝將觀止門口周圍所有生物帶來，以尋找慣於偽裝的時空道人。"
  execution:
    - "觀止人員以正門為中心，帶回或請來可見的人、貓、狗、雞、雀、昆蟲、青苔與溝中孑孓等。"
    - "人不得綁；說明原由並給茶錢。"
  anomaly:
    - "清點時曾多出一隻灰白小貓，後在無人看見離開的情況下消失。"
    - "門匾『觀』字附近出現只能藉銅鏡看見的灰蛾。"
    - "龐春梅依鏡中位置以白瓷碗扣住灰蛾。"
    - "碗底影子呈現持竹籤的人手形狀。"
  identification:
    - "碗下聲音自稱／被辨認為時空道人。"
    - "該身分目前主要依其言行、道具與既有世界角色結構成立；仍保留角色偽裝可能。"
```

## TD16-E02｜槐月十五日晚漏籤責任

```yaml
MISSED_ENTRY_CONNECTION:
  duty:
    - "時空道人負責觀止每日入場接線與命運籤。"
  interrogation:
    - "蘇清要求其在『已交但記錄遺失／未交／不知道』三者中直接回答。"
  admission:
    - "時空道人明示槐月十五日晚沒有完成白御行的命運籤交付。"
  status: "CHARACTER_ADMISSION_WITH_NO_CONTRARY_EVIDENCE"
  claim_about_cause:
    - "時空道人聲稱當晚門前同時出現七個不同時間位置的白御行。"
    - "他聲稱因此無法完成單一路線接線。"
  claim_status: "TIME_DAOIST_CLAIM_NOT_OBJECTIVELY_VERIFIED"
  correction_lock:
    - "不得倒填一支從未出現過的籤。"
    - "不得宣稱白御行忘記領籤。"
    - "不得把漏籤合理化成時空道人早有安排。"
    - "正式補籤仍未完成。"
```

## TD16-E03｜門認與七道投影

```yaml
DOOR_RECOGNITION_EVENT:
  method:
    - "時空道人以空白竹籤繞白御行，顯出七道因果投影。"
    - "投影分別與商會印、未定關係契、白梅香、紅燭、血帳、黑門與無影狀態相關。"
  observable_result:
    - "與已發生或已到期因果相關的部分投影，曾回入白御行本影。"
    - "黑門投影與無影投影未立即回入。"
    - "空白竹籤曾顯出『歸』字。"
  time_daoist_conclusion:
    - "時空道人宣稱當前白御行是承接槐月十五日晚以前因果、當日晚入場及其後商會、李師師、張麗華與白玉池事件的同一路線節點。"
    - "他宣稱當前白御行不是由其他時間線替換。"
  authority_status: "TIME_DAOIST_PROFESSIONAL_JUDGMENT_NOT_ABSOLUTE_WORLD_PROOF"

UNSHADOWED_PROJECTION:
  time_daoist_interpretation:
    - "時空道人將其解讀為世界曾過快接受白御行判斷、使玩家猜測自動成真所留下的空殼。"
  system_relevance:
    - "該解讀與既有『主角智慧吸引子／錯誤收斂』審計問題相符。"
  world_fact_status: "CHARACTER_AND_META_INTERPRETATION"
  later_event:
    - "此投影因白御行作出實際測試決策而取得可觀察影子。"
    - "其影子與身體其後被門分隔兩側。"
    - "投影最終拒絕白御行提出的四面稱號，身體消散，門後影子成為獨立未知黑影。"
```

---

# 5｜活物與事件傳遞測試

```yaml
TEST_POLICY:
  original_player_order:
    - "將草、蒼蠅、蚊子、蟑螂、青蛙投入洞中，測試對面能否收到。"
  su_qing_protocol:
    - "不同種類分開投放。"
    - "記錄數量、標記、投入狀態與對側回報。"
    - "一旦動物出現強烈退避，停止投放。"
  purpose: "測試通道傳遞，不是建立宇宙真相。"
```

## TEST-01｜帶根青草

```yaml
GRASS_TEST:
  input:
    - "帶根青草一株。"
    - "根部繫紅線。"
    - "剪去一角葉尖作比對。"
    - "根部帶三小團泥。"
  result:
    - "青草完整越過門縫，落入提燈女子碗中。"
    - "紅線、缺葉角與三團泥均可在對側辨認。"
  conclusion:
    - "至少一株活體植物可由觀止側抵達對側。"
    - "尚未證明可反向返回或長期存活。"
```

## TEST-02｜飛蟲與蚊蟲

```yaml
FLYING_INSECT_TEST:
  first_fly:
    - "起初在門前如撞牆，後穿過門縫，停在提燈女子燈柄上。"
    - "對側回報仍活。"
  mosquito:
    - "自行穿過門縫並叮咬提燈女子。"
    - "對側回報仍活。"
  marked_fly:
    input_mark: "左翅根白粉"
    result:
      - "進入後未在女子身旁出現。"
      - "其後觀止側青苔盆上出現一隻具有白粉的蒼蠅。"
      - "白粉位置在右翅根。"
    conclusion_limit:
      - "無法確認為原個體返回、鏡像、複製或標記漂移。"
```

## TEST-03｜蟑螂與事件標記

```yaml
COCKROACH_TEST:
  input:
    - "蟑螂一隻，背甲點兩個紅點，置於白紙上推近門縫。"
  result:
    - "跨越時蟑螂動作停在一個瞬間。"
    - "提燈女子可看見但無法觸碰蟑螂。"
    - "拉回觀止側後蟑螂恢復爬動。"
    - "背甲只剩一個紅點。"
    - "另一紅點出現在對側濕臺階，且可被提燈女子觸碰。"
  conclusion:
    - "個體與其部分標記／事件可能在兩側呈現不同狀態。"
    - "不能確定是物質分割、標記轉移或事件記錄分離。"
```

## TEST-04｜青蛙與提前聲音

```yaml
FROG_TEST:
  input:
    - "活青蛙一隻，置於淺竹籃，尚未完整推入。"
  result:
    - "觀止側青蛙叫聲後，對側出現比下一聲提前半拍的蛙鳴。"
    - "其後對側蛙鳴先出現，觀止側青蛙才叫出相同聲音。"
    - "第三次對側蛙鳴後，觀止側青蛙強烈退避。"
    - "蘇清立即停止投放並將竹籃拉回。"
    - "對側仍傳出第四聲較低、較遠的蛙鳴。"
    - "濕臺階出現蹼形足印，未見青蛙本體。"
  consent_and_welfare:
    - "動物出現明確退避後，試驗中止。"
  conclusion:
    - "對側可能接收到聲音、順序或足印，而非完整個體。"
    - "尚不能判定預先回聲、時間錯位、複製或其他機制。"
```

---

# 6｜玩家假說、神話敘述與角色推論分軸

## 6.1 玩家研究假說

```yaml
PLAYER_HYPOTHESES:
  bidirectional_passage:
    content: "白御行懷疑門為雙向通道。"
    support:
      - "雙方可互相聽見並回應。"
      - "部分植物與飛蟲可由觀止側抵達對側。"
    not_proven:
      - "人或大型物體能否雙向通過"
      - "反向傳遞條件"

  black_hole_white_hole_model:
    content: "白御行提出黑洞／白洞關係及微型宇宙通道模型。"
    status: "INVESTIGATIVE_MODEL_ONLY"

  time_node_hole:
    content: "白御行判斷觀止時間節點複雜，可能形成破洞。"
    support:
      - "對側時長不可辨。"
      - "觀止側不同計時尺度曾不一致。"
      - "時空道人漏籤與接線異常。"
    status: "PLAUSIBLE_HYPOTHESIS_NOT_PROVEN"

  superposition:
    content: "白御行提出七個投影皆是又皆不是自己，決策後承擔後果者才形成真實路線。"
    status: "PLAYER_HYPOTHESIS"
    observed_related_event:
      - "作出投放測試決策後，部分投影狀態發生變化。"
    lock:
      - "不得因此宣稱量子疊加為客觀機制。"
```

## 6.2 白御行四面與創世前神話

```yaml
PLAYER_SELF_MYTH_STRUCTURE:
  four_faces:
    - "光之王"
    - "神之子"
    - "暗之帝"
    - "魔之尊"
  status: "PLAYER_STATED_SELF_STRUCTURE"
  current_world_effect:
    - "黑影拒絕認領四者之一。"
  not_baseline_canon_without_gm_confirmation:
    - "四面是否為白御行客觀靈魂結構"
    - "四面是否具有超自然能力"

PLAYER_CREATION_MYTH:
  source: "白御行敘述"
  story_elements:
    - "創世以前，造物主創造光，同時出現神之影。"
    - "造物主有多強，神之影亦有多強。"
    - "光與影並存；若要消滅影，必須熄滅光。"
    - "造物主與五大天使長曾與神之影進行永恆之戰。"
    - "路西法告訴神之影：光只會造成熵增、持續消耗熱，最終光與神會自行死去，因此不必繼續戰爭，只需等待。"
    - "神之影因此停戰並永恆沉睡。"
  correction_by_player:
    - "光不產生秩序，只消耗並增加混亂。"
    - "宇宙中唯一能使熵減的是人類智慧。"
    - "天使與惡魔做不到。"
    - "神造人，是為利用人類智慧的熵減能力延長自身存在時間。"
    - "人類智慧不是線性爬升，而是可指數成長。"
  status: "PLAYER_NARRATED_MYTH_OR_SETTING_EXPLANATION_NOT_YET_GM_CONFIRMED_AS_BASELINE_CANON"

ROLE_INTERPRETATIONS:
  black_shadow:
    - "曾將沉睡解讀為退出永恆戰爭關係。"
    - "曾推論人類智慧若受完全控制便失去創造與修正能力。"
    - "曾拒絕替未知聲音完成『神之影應消滅人類』的結論。"
  unknown_voice:
    - "提出人類智慧的指數增長也可能被污染成更大消耗。"
    - "提出理解與修正可能追不上智慧製造後果的速度。"
    - "威脅只需使人類不再相信智慧值得使用。"
  status: "CHARACTER_INTERPRETATIONS_AND_THREATS"
  lock:
    - "不得把上述推論、威脅或宇宙論固化成世界客觀規律。"
```

---

# 7｜關閉決策、門後選擇與暫閉合

## BYCLOSE-E01｜是否封門的討論

```yaml
DISCUSSION_POSITIONS:
  bai_yuxing:
    - "明示有些答案現在可能不該或無能力解開，要求眾人討論是否封洞。"
  su_qing:
    - "主張停止擴大研究。"
    - "認為目前缺乏穩定計時、個體識別、雙向回收與停止條件。"
    - "傾向最小必要程序後關閉。"
  pan_jinlian:
    - "主張關閉；觀止需正常營運，今晚張麗華事件到期。"
  a_ling:
    - "主張關閉，但不把提燈女子等同於洞，不願其被隨意抹除。"
  li_shishi:
    - "主張先告知對側、嘗試回收白御行影子，再關閉。"
  time_daoist:
    - "表示能關閉入口，不能保證完成永久封印。"
```

## BYCLOSE-E02｜黑影取得獨立選擇

```yaml
BLACK_SHADOW_DECISION:
  event:
    - "白御行嘗試以『光之王、神之子、暗之帝、魔之尊』詢問投影身分。"
    - "投影拒絕選擇任何一面，並拒絕利用白御行提供的名稱取得身分。"
    - "投影身體在觀止側逐漸消散，影子留在門後成為黑影。"
    - "黑影聽取白御行創世神話與熵論後，選擇不跨門、不奪取白御行名字，留在門後等待／觀看。"
  observable_symbol:
    - "其竹籤字樣由『來』變為『等』，最後變為『看』。"
  status:
    - "已失去冒充當前玩家本體的資格。"
    - "是否為獨立人物、殘影、事件體或其他存在仍未知。"
```

## BYCLOSE-E03｜通道暫閉合

```yaml
CLOSURE_EVENT:
  operator:
    - "時空道人"
    - "門後黑影曾從對側協助合門"
  final_player_position:
    - "白御行對宇宙、人類與神的終局責任表示：『關我屁事，我又沒有永生。』"
    - "此為玩家立場，不代表宇宙問題已解決。"
  observable:
    - "黑色門縫完全合攏。"
    - "門後鞋、燈、女子、黑影、白點與聲音不再可見。"
    - "白玉池恢復清水表面。"
    - "池中留下／退回一株帶根青草，紅線與葉角缺口仍可辨。"
  time_daoist_label: "暫閉合"
  not_proven:
    - "連結完全斷絕"
    - "永久封印"
    - "門後存在消失"
    - "不會在其他位置重開"
```

## BYCLOSE-E04｜封池規則

```yaml
WHITE_JADE_POOL_SECURITY:
  status: "SEALED_AND_MONITORED"
  physical_measures:
    - "池沿紅繩維持。"
    - "蘇清掛上木牌：『白玉池暫封。禁止投物、呼喚、命名及回答池中未知聲音。』"
  guard:
    - "阿泠留在白玉池附近守池。"
  forbidden:
    - "入池洗浴"
    - "投放物品或活物"
    - "呼喚門後存在"
    - "再次命名未知空間"
    - "回答池中未知聲音"
    - "碰觸或重啟『續』字"
  reopen_condition:
    - "需另行完成風險評估、監測方案與人類 GM 授權。"
  current_business_state:
    - "阿泠水療暫停。"
    - "白玉池不得作普通浴房使用。"
```

---

# 8｜阿泠與白御行：兄妹提案未成立

```yaml
A_LING_FAMILY_PROPOSAL:
  initiator: "白御行"
  content:
    - "白御行再次詢問阿泠是否願意當妹妹。"
    - "他以白御行、白玉池、白御池名字相配作玩笑。"
  a_ling_response:
    - "阿泠拒絕『白御池』，認為像浴房名稱。"
    - "阿泠明示自己叫阿泠，白玉池是池，兩者不能混同。"
    - "她表示若妹妹意味受欺負時白御行站她一邊、闖禍時先問清楚、不把她忘在池裡，可以考慮。"
    - "她沒有正式接受兄妹關係。"
    - "她不接受改名；最多只曾說可考慮私下稱『白家小泠』。"
  current_relation:
    family_relation: false
    adoption_or_oath: false
    ownership: false
    name_change: false
    state: "兄妹方向被提出，阿泠保留考慮，尚未成立"
  lock:
    - "不得在未經阿泠明示接受前稱她為白御行妹妹。"
    - "不得把『白家小泠』當正式姓名。"
    - "不得以她居於白玉池推導她是浴房、池靈或白家財產。"
```

---

# 9｜定陶商會：今日授權與回報門檻

```yaml
MERCHANT_DELEGATION:
  player_decision:
    - "白御行決定槐月十六日白日不回商會，留在觀止準備張麗華花燭。"
    - "他判斷若回商會，可能被新增事件拖住。"
  incoming_question:
    - "商會夥計攜帳冊來問定陶既定貨務按昨日方案執行，或等白御行翌日再看。"
  player_answer:
    - "『船沉了再來叫我。』"
  operational_interpretation:
    - "既定貨務由副會長依昨日方案執行。"
    - "普通偏差、帳目與貨務不需白御行即時批准。"
    - "方案失效、重大人員傷亡、貨物全失或同級事故才構成高級回報。"
    - "酉初睡醒前，即使實際船務事故亦先由副會長承接，不因措辭自動喚醒白御行。"
  current_threat_state: "CONTAINED_BUT_NOT_CLOSED"
  full_detail_source: "HOT_SAVE_V1.5"

MERCHANT_CASE_UNRESOLVED:
  - "吳六下落與罪責"
  - "五名逃犯"
  - "灰簿先生身份"
  - "借支文件抄件外洩路徑"
  - "押送者個別最終處置"
  - "白御行所殺背叛者名冊、正式紀錄及家屬援助落實"
```

---

# 10｜蘇清共浴邀請與小翠浴房服務

## BATH16-E01｜蘇清明確拒絕共浴

```yaml
SU_QING_BATH_INVITATION:
  initiator: "白御行"
  request:
    - "白御行提議去蘇清房間洗浴，並因兩人都髒邀她一起洗。"
  su_qing_response:
    - "蘇清明確區分『她髒了』與『一起洗』。"
    - "蘇清明確回答不共同沐浴。"
    - "她安排白御行使用客浴，熱水、皂角與乾衣另備。"
  consent_state: "REFUSED_AND_RESPECTED"
  outcome:
    - "未共同洗浴。"
```

## BATH16-E02｜小翠擦背服務範圍

```yaml
XIAOCUI_SERVICE_REQUEST:
  request:
    - "白御行改請小翠在客浴協助擦背。"
    - "明示不要求小翠一起入浴。"
  communication_by_su_qing:
    - "蘇清派人詢問小翠是否願意。"
    - "只詢問擦背；不施壓、不勸說。"
  xiaocui_consent:
    accepted:
      - "洗頭"
      - "擦背"
      - "遞皂角"
      - "遞衣物"
    conditions:
      - "小翠不下水。"
      - "門不鎖。"
      - "若白御行臨時增加服務，小翠可直接離開。"
  consent_state: "LIMITED_EXPLICIT_CONSENT"
```

## BATH16-E03｜追加私密清洗遭拒

```yaml
ADDITIONAL_REQUEST:
  player_language:
    - "白御行以性玩笑表示今日性精力留給張麗華。"
    - "其後要求小翠替張麗華把其私密部位特別洗乾淨。"
  xiaocui_response:
    - "小翠明示此要求超出原先服務範圍。"
    - "她拒絕替白御行清洗私密部位。"
    - "她將軟布與皂角放在白御行可自行取得的位置。"
    - "她重申張麗華今晚是否使用／是否親密由張麗華當晚決定。"
  player_followup:
    - "白御行表示算了，並說下次要說準。"
  xiaocui_correction:
    - "小翠表示自己先前已說得很準，是白御行聽見可以後忽略後續限制。"
    - "她要求未來一開始說清楚，再由她決定願不願意。"
  outcome:
    - "小翠完成原先同意的洗頭、擦背、遞物。"
    - "白御行自行清洗其他部位。"
    - "沒有新增性服務、私密觸摸或共同入浴。"
  boundary_status: "REFUSAL_EFFECTIVE_NO_ESCALATION"
```

---

# 11｜花燭前休息安排

```yaml
REST_EVENT:
  event_id: "REST16-E01"
  player_decision:
    - "白御行判斷距吉時仍有時間，要求安排一張不受打擾的床休息。"
  room:
    - "觀止西側平日供醉客醒酒的小房。"
    - "窗朝內院，不臨前樓。"
    - "床帳與褥子已更換整理。"
    - "房內不點香。"
  supplies:
    - "溫水一壺。"
    - "清粥一碗，供醒來後食用。"
    - "李師師送來的傍晚外袍。"
  do_not_disturb:
    - "酉初前帳目、客人與普通商會消息不得打擾。"
  wake_plan:
    - "酉初喚醒。"
    - "預留半個時辰醒神與更衣。"
  current_result:
    - "眾人退出，房門帶上但未鎖。"
    - "白御行已入睡。"
```

---

# 12｜人物關係與知情矩陣

```yaml
RELATION_MATRIX:
  bai_yuxing__zhang_lihua:
    state: "情人關係已成立"
    due: "槐月十六日酉正點燭、戌初開門"
    marriage: false
    wife_title: false
    exclusivity: false
    sexual_consent_for_tonight: "UNDECIDED_UNTIL_SCENE"
    player_language:
      - "新娘"
      - "討老婆"
    legal_effect_of_language: "NONE"

  bai_yuxing__li_shishi:
    state: "私人性關係持續；情感與追求未封閉"
    current_role_today:
      - "替張麗華梳頭"
      - "送白御行傍晚外袍"
    pregnancy_state: "UNKNOWN"
    current_internal_ejaculation_rule: "NOT_ALLOWED_UNTIL_FURTHER_DECISION"

  bai_yuxing__a_ling:
    state: "熟識增加、互相調侃、白玉池事件共同經歷"
    family_relation: false
    sibling_proposal: "PROPOSED_NOT_ACCEPTED"
    romantic_relation: false
    sexual_relation: false
    ownership: false

  bai_yuxing__su_qing:
    state: "調查合作與實務互信"
    co_bathing: "REFUSED"
    current_task:
      - "保存白玉池觀察紀錄"
      - "維持封池規則"

  bai_yuxing__xiaocui:
    state: "客浴有限服務已完成"
    agreed_service:
      - "洗頭"
      - "擦背"
      - "遞物"
    private_washing: "REFUSED"
    sexual_service: false

  bai_yuxing__time_daoist:
    state: "職務追責／漏籤未結"
    missed_lot: true
    replacement_lot_issued: false
    responsibility_dispute: "時空道人承認未交，但原因主張未驗證"

  bai_yuxing__black_shadow:
    state: "門後獨立未知存在；與白御行因果關係未明"
    impersonation_status: "NO_LONGER_ACCEPTED_AS_PLAYER_BODY"

  guanzhi__lamp_woman:
    state: "曾建立對話，通道暫閉後失聯"
    rescue_or_entry_commitment: false

  pan_jinlian__white_jade_pool:
    knowledge: "NOW_INFORMED_AND_INVOLVED"
    action:
      - "協助召集生物與維持觀止營運秩序"
      - "支持關閉通道"
```

---

# 13｜知情、傳聞與公開狀態

```yaml
KNOWLEDGE_SCOPE:
  full_or_direct_witnesses_to_pool_event:
    - "白御行"
    - "蘇清"
    - "李師師／師理理"
    - "阿泠"
    - "潘金蓮"
    - "龐春梅（至少參與召集生物與灰蛾捕捉）"
    - "時空道人"
  partial_witnesses:
    - "若干小廝與被帶來的路人／客人，只知道觀止在抓取生物或後院有異常，不必然知道完整通道內容。"
  li_pinger:
    status: "此前參與白玉池封池與張麗華安排；本輪通道全部細節是否全程在場未確認"
  zhang_lihua:
    status: "沒有證據顯示她知道白玉池通道全部內容"
  public_state:
    - "白玉池異常不是對外公開事件。"
    - "張麗華花燭不是公開婚禮。"
    - "時空道人漏籤不是觀止公開通告。"

RUMOR_LOCK:
  - "門後女子不得被公共傳聞直接稱為女鬼。"
  - "白玉池不得公開稱黑洞海、宇宙通道或亡魂之門。"
  - "白御行『討老婆』不得轉化成張麗華正式出嫁傳聞。"
```

---

# 14｜未決事項

```yaml
OPEN_THREADS:
  immediate_evening:
    - "酉初喚醒白御行。"
    - "白御行是否進食清粥、如何更衣與整理。"
    - "酉正張麗華房點紅燭與龐春梅第一杯酒。"
    - "戌初白御行是否準時抵達。"
    - "張麗華是否允許進房及今晚任何身體親近。"

  white_jade_pool:
    - "通道是否真正雙向。"
    - "暫閉合是否持續。"
    - "提燈女子、未知聲音與黑影的身分。"
    - "大量鞋、白點、水珠與多天空映像的來源。"
    - "草是否真的完整返回，或只是近似個體。"
    - "第三隻蒼蠅的個體同一性。"
    - "蟑螂紅點分離的機制。"
    - "青蛙提前叫聲與足印的機制。"
    - "黑影是否仍與白御行存在因果連結。"
    - "門是否會在白玉池或其他位置重開。"
    - "阿泠與白玉池異常的真正關係。"
    - "阿泠是否與 MASTER 中白玉池無名女子同一存在。"
    - "水療生意何時、是否能安全重啟。"

  time_daoist:
    - "槐月十五日晚七個白御行投影主張是否可驗證。"
    - "正式補發／重做命運籤。"
    - "漏籤是否是通道形成的必要因素、促成因素或僅同時事件。"
    - "時空道人是否仍留在觀止附近。"

  player_myth_and_hypotheses:
    - "四面結構是否屬於白御行正式人物設定。"
    - "創世前神話是否為世界基線正史。"
    - "神之影、熵增、人類智慧熵減與指數成長是否只屬玩家故事／哲學模型。"
    - "未經 GM_CONFIRM，不得寫入 BASELINE_CANON。"

  merchant_case:
    - "依第九節未決事項持續。"

  li_shishi:
    - "月事是否如期。"
    - "是否找到可靠女醫。"
    - "槐月十一日體內射精是否造成妊娠。"

  a_ling:
    - "是否將來明示接受兄妹關係。"
    - "目前不得自動成立。"
```

---

# 15｜接關約束

```yaml
CONTINUATION_LOCK:
  scene_entry:
    - "下一幕從槐月十六日酉初前後、白御行在西側小房被喚醒開始。"
    - "除非觸發失火、死亡、遭襲或白玉池重開，睡眠期間不得插入強迫玩家處理的新事件。"
    - "不得替白御行自動起床、穿衣、吃粥、赴約或進張麗華房。"

  zhang_lihua_lock:
    - "張麗華是情人，不是妻。"
    - "紅衣、紅帳、紅燭與合巹酒不構成婚姻或永久同意。"
    - "白御行稱『老婆／新娘』只代表其台詞與期待。"
    - "酉正與戌初是張麗華定下的當日安排。"
    - "遲到可被關門。"
    - "任何性行為由張麗華當場決定。"

  white_jade_pool_lock:
    - "白玉池維持封池與監測。"
    - "通道狀態只能稱『暫閉合』。"
    - "不得因黑線消失便宣稱永久封印。"
    - "不得再次投物、呼喚、命名、回答或自行重啟。"
    - "若通道重開，屬立即喚醒白御行的重大事件。"

  hypothesis_lock:
    - "黑洞海不是正式地名。"
    - "黑洞／白洞、微型宇宙通道、時間破洞與疊加態均非已證明機制。"
    - "七個白御行不是七個客觀人物名冊。"
    - "時空道人與黑影的解讀不等於客觀真相。"
    - "創世神話與熵論未經 GM 明示，不寫入世界基線。"

  time_daoist_lock:
    - "時空道人承認漏籤；此責任不得被漂亮神話抹除。"
    - "正式命運籤仍未補發。"
    - "不得倒填籤文。"

  a_ling_lock:
    - "阿泠沒有接受『白御池』或正式白姓。"
    - "兄妹關係未成立。"
    - "不得把她當浴房、池靈、白家妹妹或白家財產。"

  bath_boundary_lock:
    - "蘇清拒絕共浴，拒絕有效。"
    - "小翠只同意洗頭、擦背與遞物。"
    - "小翠拒絕私密清洗，沒有發生越界服務。"
    - "不得把擦背服務改寫成性服務。"

  merchant_lock:
    - "白御行今日不回商會。"
    - "既定貨務交副會長執行。"
    - "普通消息不得在睡眠期間打斷。"
    - "商會威脅未結案，不得因暫不回去而宣稱停止。"
```

---

# 16｜有效接關摘要

理火三年槐月十六日清晨，白御行、蘇清、李師師、阿泠等人在封鎖中的白玉池繼續調查異常。「續」字停在最亮處後，池中出現一道通往不明夜色的黑色門縫；門後可見提燈女子、濕臺階、大量鞋、成對白點及至少一道身份不明的聲音。雙方可以對話，但對側女子只能辨認事件先後，不能說明穩定經過時長；觀止側亦出現日影、墨跡與木魚次數不完全一致的計時現象。

白御行先後提出「黑洞海」、雙向通道、黑洞／白洞、微型宇宙通道、時間節點破洞與疊加態等模型。他解釋「海」是相對於特定觀察者數不清的物質集合，而非客觀無限。這些說法只屬玩家假說與命名提案，門後現象雖有反應，仍不足以證明其機制。

白御行判斷時空道人可能涉入，命觀止人員把門口周圍所有可見生物帶來尋找偽裝。眾人帶回人、貓狗、雞雀、昆蟲、青苔與孑孓等；門匾附近出現只能透過銅鏡看見的灰蛾，龐春梅依鏡中位置以白瓷碗扣住，碗影呈現持竹籤的人手。時空道人承認槐月十五日晚沒有完成白御行每日入場的命運籤交付，並聲稱當晚同時出現七個不同時間位置的白御行。此原因尚未驗證，正式補籤亦未完成。

時空道人以空白竹籤與門進行接線辨認，顯出七道與商會、關係、白梅、紅燭、血帳、黑門及無影狀態相關的因果投影。他宣稱當前白御行是承接既有事件的同一路線節點，不是別條時間替換者。無影投影被他解讀為世界過快接受白御行判斷所形成的空殼；此屬角色與審計性解讀，不是客觀世界定論。

白御行決定測試通道是否能傳遞活物。蘇清將測試拆分：帶根青草完整抵達對側；蒼蠅與蚊蟲可穿越，但一隻帶白粉標記的蒼蠅進入後，觀止側出現白粉位置相反的近似個體；背甲有兩個紅點的蟑螂在門中停格，拉回後只剩一點，另一紅點留在對側且可被觸碰；青蛙尚未完整進入，對側卻先出現蛙鳴與蹼形足印，青蛙強烈退避後試驗立即停止。測試證明部分植物、昆蟲、聲音與標記可跨側呈現，但沒有證明完整雙向通道、個體同一性或時間機制。

眾人討論是否關閉通道。蘇清、潘金蓮與阿泠均主張停止試驗並關閉；李師師主張先告知對側、處理白御行影子，再關閉；時空道人表示能關閉入口，不能保證永久封印。白御行又以光之王、神之子、暗之帝、魔之尊詢問投影身分，投影拒絕選擇，最終其身體在觀止側消散，影子留在門後成為獨立黑影。

白御行向黑影敘述創世前神話：造物主創造光時同時出現神之影；神與五大天使長曾與神之影進行永恆之戰；路西法以光只會消耗、造成熵增並終將自行死亡為由，使神之影停止戰爭、永恆沉睡。白御行其後校正：光不創造秩序；只有人類智慧能形成熵減，神造人是為延長自身存在時間；人類智慧可指數增長。這些內容尚未經 GM 明示升格為世界基線，只保存為玩家神話與哲學模型。黑影與未知聲音各自作出推論與威脅，但均未取得客觀真相法位。

黑影最後選擇不跨門、不奪取白御行名字，留在門後等待／觀看。時空道人與門後黑影共同收束門縫；未知聲音曾宣稱會污染人類智慧，使其只擴大消耗或不再相信智慧值得使用。蘇清明示這是威脅，不是預言。門縫最終完全合攏，白玉池恢復清水，時空道人只標記為「暫閉合」，未證明永久封印或完全斷線。池沿仍掛紅繩與警示牌，禁止投物、呼喚、命名及回答池中未知聲音；阿泠留守，水療暫停。

白御行其後再次詢問阿泠是否願意當妹妹，並以「白御池」玩笑命名。阿泠拒絕該名字，重申自己叫阿泠、白玉池是池；她只表示若妹妹意味被欺負時有人站她一邊、闖禍時先問清楚、不被遺忘，可以考慮。兄妹關係未成立，名字未改。

白御行決定今日不回定陶商會。商會夥計來問既定貨務是否照昨日方案執行，白御行回答「船沉了再來叫我」；現行解讀為副會長依既定方案執行，只有方案失效、重大傷亡、貨物全失或同級事故才提高回報，不再以普通帳務打斷白御行。商會案仍未結束。

白御行邀蘇清到她房中共同沐浴，蘇清明確拒絕並改安排客浴。白御行其後請小翠只在客浴協助擦背，不共同入浴；小翠同意洗頭、擦背、遞皂角與衣物，並預先說明不得臨時增加服務。白御行後續要求小翠替其清洗私密部位，小翠明確拒絕，將布與皂角放在他可自行取得處；她完成原先同意的服務，沒有性服務、私密觸摸或共同入浴。

張麗華已確認槐月十六日晚的私人情人花燭：紅衣、紅帳照舊，不掛囍、不用白家標記；只請龐春梅喝第一杯後離場。李師師獲准替她梳頭。酉正點紅燭，戌初房門開，過時不候。白御行稱她「新娘」、說今日要「討老婆」，均只是玩家台詞；張麗華仍是情人，不是妻，今晚任何身體親近仍由她當場決定。

午正後，白御行完成客浴，要求安排不受打擾的床休息。觀止將他安置在西側醒酒小房，房內備溫水、清粥與傍晚外袍；酉初以前，帳目、客人與普通商會消息不得打擾，只有觀止失火、死亡、遭襲或白玉池重開才立即喚醒。白御行現已入睡。

**當前時間：理火三年槐月十六日午後，午正後、尚未至酉初。**

**當前位置：觀止西側醒酒小房。**

**當前狀態：白御行熟睡；白玉池封池且通道暫閉合；張麗華花燭於酉正開始、戌初開門。**

**下一幕：酉初喚醒白御行。**

---

## VERSION_STATUS

```yaml
ACTIVE_HOT_SAVE: "V1.7"
PREVIOUS_VALID_HOT: "V1.6"
HISTORICAL_VALID_HOT:
  - "V1.5"
  - "V1.4"
ILLEGAL_SAVE:
  version: "V1.3"
  use: "AUDIT_ONLY"
NEXT_RESUME_POINT: "槐月十六日酉初，觀止西側醒酒小房，白御行被喚醒"
```
