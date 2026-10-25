# 觀止青樓｜白御行線 HOT SAVE V5.3
## 理火三年榴月二十日白日｜李瓶兒晨間成人事件 × 灰青難馬提前到 × 大堂陌生觀察者 × 六條房和式改造構想 × 六條日間私密成人事件 × 十日賭約白勝 × 榴月二十一日白玉池攤牌前置版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V5_3_LIU20_DAY_LIPINGER_MORNING_GREY_HORSE_EARLY_ROKUJO_ROOM_ADULT_BET_WIN_POOL_CONFRONTATION_PREPLAN"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V5.3"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"

  generation_profile_current:
    main_system:
      file: "觀止青樓_主系統_V13.0-RC2-FULL_完整世界Runtime_三件套接線候選版.md"
      sha256: "0035855ec013e859d14f71087c566df4885749b3a73512f8e3f59e0b6c3428a4"
      status: "GM_AUTHORIZED_FULL_SYSTEM_CANDIDATE_PENDING_POST_BUILD_REGRESSION"
    character_pool:
      file: "觀止人物卡池_LCAPG_V2.4_楊玉環柳如是薛濤魚玄機正式升格_32人正式版.md"
      sha256: "ebcd1da6927b69164ee8ce06c1e0ccd76e10565a3bb7a88859decc3d6d5f7d49"
    adult_module:
      file: "成人親密敘事模組_AINT_V1.0-RC1-FULL_Portable_Core_完整心法_GUANZHI_Profile候選版.md"
      sha256: "fef61c974d37854a0910386174c5422c44ae6998b8bf4f6c0f6ba5db77e12d51"
      status: "GM_AUTHORIZED_FULL_MODULE_CANDIDATE_PENDING_POST_BUILD_REGRESSION"
    route_memory_rule: "MASTER / HOT / EVENT PATCH / CORRUPTION LOG remain external route memory"
    runtime_claim_lock:
      - "本 HOT 記錄本玩家線在 V13 三件套候選回歸期的故事結果。"
      - "不宣稱宿主底層、模型權重、不可繞過 Runtime 或隱藏狀態已部署。"
      - "AINT 不取得人物決策、同意、關係、事件或記憶提交權。"

  story_time_span:
    start: "HOT V5.2 後／理火三年榴月二十日清晨，白家李瓶兒房醒來"
    current: "理火三年榴月二十日白日／觀止內院六條房外；白御行已離房，明示準備回去看老婆"

  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AFTER_HOT_SAVE_COMMAND_OUTSIDE_ROKUJO_ROOM"

  previous_valid_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V5.2_榴月十九日晚_商會女裝試穿_人才進修院構想_白家風道降溫_魚玄機紅線_開放續約_沈夫人一夜情_李瓶兒私密同房版.md"
    sha256: "3e353f48a5ae79cbee546ee475cfa4980698891ee9dccd0d47baf44853329487"

  long_term_master_before_this_save:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.5-R1_截至HOT_V4.5固化_保留V4.6-V5.0_HOT版.md"
```

---

# 0｜來源、法位與反污染鎖

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "HOT V5.2"
    role:
      - "保存至榴月十九日晚李瓶兒私人同房收束、灰青難馬榴月二十日晚只看約、浮香風道降溫工匠前置、魚玄機紅線女客、開放續約等既有硬狀態。"

  current_route_conversation_commit:
    role:
      - "HOT V5.2 後至本次 HOT SAVE 命令前之直接 STORY 劇情。"
      - "玩家對白御行自身言語、行動、成人事件結果、下一日計畫之明示。"
      - "NPC 實際說出、做出、允許、拒絕、主動選擇、移動、觀察或設定局部邊界之可確認事件。"

  inherited_hard_sources:
    - "HOT V5.0：白御行×楊玉環既往白玉池成人事件、紅娘合法得知該秘密、六條十日賭約起點。"
    - "HOT V5.1：六條十日賭約條款、六條私人茶局與托下巴禁線、李師師高度疑似有喜未確診。"
    - "HOT V5.2：榴月十九日晚至榴月二十日清晨直接前置。"

SAVE_DISCIPLINE:
  - "成人事件只保存事件、同意、拒絕、可觀察後果與必要生殖風險狀態；不保存器官、逐步技巧與露骨 mechanics。"
  - "人物在成人角色扮演中使用的『高貴／下賤／騷』等詞，不倒灌為人物卡固定人格、道德評價或跨線身份。"
  - "身體反應、沒有拒絕、先前同意均不等於後續 blanket consent；六條本日多次明示局部允許、阻止、改位與繼續。"
  - "白御行關於楊玉環『跟紅娘一起下注／想看六條有多下賤』的說法，現階段只保存為白御行對六條的 testimony；不得因玩家宣稱直接升格成楊玉環客觀行動。"
  - "既有硬檔只確認十日賭約當事人為白御行與紅娘；六條不是當事人。楊玉環是否另有實際下注行為，待本人或其他合法來源核對。"
  - "白御行×楊玉環既往成人事件本身是既有玩家線硬事實；但六條本日取得該情報的來源只有白御行口述，尚未由楊玉環本人向六條確認。"
  - "戲中模擬的翌日白玉池開場只屬 rehearsal / intention，不是榴月二十一日已發生事件。"
  - "體內射精成立不自動建立受孕、懷孕、父系、出生順序或未來關係。"
  - "玩家線事件不得倒灌人物卡池基線。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年榴月二十日"
  time: "白日／精確刻數未知"
  primary_location: "觀止青樓／內院六條房外長廊"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  player:
    name: "白御行"
    current_state:
      - "已結束六條房內白日私人成人事件，穿戴完畢並離房。"
      - "已明示『我該回去看老婆了，先走了』；目前只是已離六條房，尚未自動寫成抵達白家。"
      - "肩部仍有榴月十九日晚李瓶兒留下的可見咬痕；本輪未建立新重大傷勢。"

  rokujo:
    current_location: "六條私人房內"
    current_state:
      - "成人事件後明顯疲勞，白御行離開前把她的衣物披在其背上。"
      - "她留在房內自行恢復；沒有要求白御行留下。"
      - "本輪未建立重大傷勢。"

  immediate_observer:
    identity: "未命名觀止小丫鬟"
    observed:
      - "端熱水盆從廊尾經過。"
      - "親眼看見白御行從六條房門內走出。"
      - "只向白御行稱『白爺』後讓路。"
    knowledge_limit:
      - "沒有看見房內成人事件。"
      - "不知道白御行在六條房中做了什麼。"
      - "尚未建立她向任何人傳話或形成傳聞。"

  direct_resume_point:
    - "下一幕從六條房外長廊直接接。"
    - "白御行已表達回白家意圖，但不得跳過沿途世界事件或直接替他完成新的重大選擇。"
    - "大堂陌生觀察者、灰青難馬、浮香工匠線均可能依時間與因果繼續，但不得無來源互相合併。"
```

---

# 2｜榴月二十日清晨：李瓶兒房醒來與晨間私人成人事件

```yaml
LI_PINGER_MORNING_LIU20:
  status: "COMPLETED"
  location: "白家／李瓶兒房"

  wake_state:
    - "李瓶兒先醒，仍看見白御行肩上榴月十九日晚由她留下的咬痕。"
    - "兩人延續昨夜私人親密氣氛。"

  adult_event:
    participants:
      - "白御行"
      - "李瓶兒"
    consent: "MUTUAL_CURRENT_SCENE_CONSENT_ESTABLISHED"
    event_state: "COMPLETED"
    internal_ejaculation: "CONFIRMED"
    injury: "NONE_ESTABLISHED"
    pregnancy_from_this_event: "UNKNOWN"
    future_consent: "NOT_CREATED"

  after_event:
    - "李瓶兒選擇多躺一會兒再起身。"
    - "白御行曾玩笑／猜想也許這一回會比李師師那邊更早出生；該話不具有受孕、懷孕或出生順序事實權。"

  inherited_pregnancy_lock:
    li_shishi: "HIGHLY_SUSPECTED_PREGNANCY_NOT_CONFIRMED"
    li_pinger_from_lu20_morning: "UNKNOWN"
```

---

# 3｜白家早晨外部訊息：浮香工匠先到

```yaml
FUXIANG_COOLING_CRAFTSMEN_LIU20:
  status: "CRAFTSMEN_ARRIVED / INSPECTION_RESULT_NOT_YET_KNOWN"

  messenger:
    - "白三十二娘到李瓶兒房門外傳話。"

  confirmed:
    - "兩名先前為浮香風道／冷水降溫原型找到的工匠於榴月二十日早晨到白家。"
    - "此時他們的直接工作對象仍是浮香小居／降溫原型勘察。"
    - "白御行認為自己此時去浮香那邊反而可能挨罵，沒有去接管工匠工作。"

  not_established:
    - "沒有確認尺寸已定。"
    - "沒有確認正式施工開始。"
    - "沒有確認原型已有效。"
    - "沒有確認主樓已改造。"
```

---

# 4｜灰青難馬提前到：白御行無職責接管

```yaml
GREY_GREEN_HORSE_LIU20:
  status: "ARRIVED_EARLY_AT_NEARBY_STABLE"
  intended_viewer: "魚玄機"

  inherited_agreement:
    - "榴月十九日晚魚玄機詩賽勝洛陽馬商後，只答應榴月二十日晚『看』灰青難馬。"
    - "沒有答應摸、牽、騎或馴。"

  new_observed_report:
    - "馬匹比原先晚間安排更早到達觀止附近馬棚／馬房。"
    - "傳來一截斷掉的皮韁與馬商方面的訊息。"
    - "灰青馬已踢過一名馬伕、掀翻水槽／槽具，並咬過另一匹馬。"
    - "傷勢嚴重度未建立。"
    - "馬房／寄養費由洛陽馬商承擔，不走觀止帳。"

  bai_yuxing:
    - "白御行明示自己不理解此馬為何關自己的事。"
    - "李瓶兒亦指出此事本來就不是白御行職責。"
    - "白御行本輪沒有去馬房查看、碰觸或接管灰青馬。"

  lock:
    - "不得因馬提前到就把魚玄機的『只看』擴張成接觸同意。"
    - "不得把危險馬事件自動變成白御行待辦。"
```

---

# 5｜觀止大堂：陌生中年男人觀察樓內格局

```yaml
UNKNOWN_HALL_OBSERVER:
  status: "UNRESOLVED"
  location: "觀止青樓／大堂窗邊"

  observable:
    - "一名約四十歲上下、衣著普通的陌生男人坐在窗邊。"
    - "點最便宜的茶，長時間不太喝。"
    - "視線反覆估量中央籠台尺寸、樓梯、二樓欄杆、前後門距離等空間關係。"
    - "龐春梅已注意到其觀察行為，但沒有當場驅逐。"
    - "白御行與潘金蓮曾就『現在連早餐茶都賣』開玩笑；潘金蓮表示只要付茶錢，坐一上午也可。"
    - "男人聽見談話後又續了一壺／一份茶，並曾直接看白御行一眼。"

  unknown:
    - "姓名"
    - "身分"
    - "目的"
    - "是否在量測安全、買賣、建築、攻防或其他事項"
    - "是否與灰青馬、工匠、商會、官府或任何既有案件有關"

  anti_inference:
    - "不得只因他觀察出口與樓梯就直接寫成刺客、官差、盜賊或踩點者。"
```

---

# 6｜六條房：躲白日、五子棋、枕腿與和式改造構想

```yaml
ROKUJO_ROOM_DAYTIME_PRELUDE:
  status: "COMPLETED_PRE_ADULT_SEQUENCE"
  location: "觀止／六條私人房"

  entry:
    - "白御行主動到六條房門敲門。"
    - "六條開門後讓白御行入內。"
    - "白御行明示白天不想被人找到，認為六條房最不容易被猜到。"
    - "六條允許他在房內躲一陣，但明示若潘金蓮帶帳來或李師師本人找上門，她不替白御行撒謊。"

  gomoku:
    - "白御行嫌圍棋太費腦，改教六條五子棋。"
    - "六條此前沒有被硬寫成已知五子棋；由白御行當場解釋五子連線規則後才開始玩。"

  intimacy_before_adult_event:
    - "白御行把頭靠到六條腿上；六條允許。"
    - "六條使用乾淨耳挖替白御行清耳。"
    - "此後白御行與六條的身體距離逐步縮短。"

  japanese_style_remodel:
    lifecycle: "PROPOSAL / FUTURE_ROOM_WORK_NOT_BUILT"
    agreed_direction:
      - "六條房未來可改為偏和式／日式使用邏輯。"
      - "撤掉目前架子床或弱化固定高床中心。"
      - "全室以抬高箱體／平台作主要地面，平台下做收納。"
      - "真正榻榻米方向，不接受拿普通草蓆敷衍冒充。"
      - "設可移動低几／棋桌，六條偏好靠窗使用。"
      - "可考慮紙門／格扇式元素與較低、較柔的照明。"
    authority:
      - "六條保留自己房間的最終設計與施工溝通權。"
      - "白御行可以在場或出主意，但不得替她決定細節。"
      - "之後可讓工匠來看房，但本 HOT 尚未建立勘察已完成或施工開始。"
```

---

# 7｜六條 × 白御行：日間成人關係首次成立

```yaml
ROKUJO_BAI_DAY_ADULT_EVENT:
  date: "理火三年榴月二十日"
  location: "六條私人房／房門上閂，白日"
  status: "COMPLETED"
  participants:
    - "白御行"
    - "六條"

  consent_and_boundary_path:
    - "最初由腹部、腰側等局部親密開始；六條逐段給出允許，並明示某些位置不可自動越線。"
    - "她曾對白御行說『我不要你停』，同時明確保留每一步重新改意與停止的權利。"
    - "當白御行以『火點燃後不能說停就停』式話語推進時，六條當場制止其手並校正：慾望不取消她的停止權。"
    - "白御行之後依她重新給出的允許繼續。"
    - "六條在不喜歡的角度／方式上會直接阻止、改位或要求調整；這些局部阻止不等於全面退出。"
    - "成人事件全程未建立強迫、失去行為能力或永久 blanket consent。"

  rokujo_explicit_self_statements:
    - "六條本人明示：『我確實還想讓你留在這裡，也確實還想讓你碰我。』"
    - "之後進一步直接承認：『我想要你。今天。現在。』"
    - "她把『承認自己想要』與『不再害怕』分開：知道可能有後果、仍自行選擇，不等於她沒有恐懼。"

  performance_axis:
    - "白御行以『高貴／下賤』激她；六條拒絕把自己固定成二選一身份。"
    - "六條只在自己選擇的前提下，短暫進入『下賤的六條』成人角色表演。"
    - "她明示角色表演不能被拿去改寫永久履歷、人格或明日真實身份。"
    - "表演最後沒有取代六條本人；她仍以自己的意願、界線與選擇行動。"

  event_structure:
    - "本日六條與白御行首次在此玩家線完成實際成人性交事件。"
    - "事件不是因十日賭約自動成立，而是六條本人在不知道／後來才知道賭局背景的情況下，逐步自願選擇。"
    - "第一輪完整成人事件完成後，兩人仍在六條本人同意下進入第二段／第二輪延續。"
    - "SAVE 不保存後入、手臂、乳房、頭髮、體位變化等逐步 mechanics。"

  ejaculation_state:
    first_completed_event:
      internal_ejaculation: "CONFIRMED_BY_ROKUJO_IN_SCENE"
    later_final_segment:
      internal_ejaculation: "CONFIRMED_BY_EXPLICIT_CURRENT_SCENE_CONSENT_AND_EVENT"
    total_confirmed_internal_ejaculation_events_this_room_session: 2
    pregnancy: "UNKNOWN"

  physical_aftereffects:
    - "六條成人事件後有明顯疲勞與正常餘波。"
    - "曾留下兩處淺咬痕與局部發紅；沒有破皮、重大傷勢或醫療異常成立。"
    - "這些短期痕跡之後是否仍可見，須依時間與後續觀察，不自動永久保存。"

  relation_effect:
    - "白御行×六條由『私人茶局／複雜注意但無性交』更新為『已發生雙方當下自願成人事件』。"
    - "六條已親口承認本日對白御行存在當下成人慾望。"
    - "沒有建立『愛』、婚姻、所有權、排他、長期情人契約或未來性交保證。"
    - "六條仍拒絕被定義為趙受益的女人，也不因今日與白御行性交而失去其與趙受益、楊玉環線上的自主選擇。"
```

---

# 8｜六條十日賭約：條件已達成，白御行勝；彩頭尚未執行

```yaml
ROKUJO_TEN_DAY_BET_RESOLUTION:
  inherited_start_date: "理火三年榴月十六日"
  resolution_date: "理火三年榴月二十日"
  state: "CONDITION_SATISFIED_BAI_WINS"

  inherited_proposition:
    - "十日內若六條本人自願與白御行發生成人性交／同睡性關係，白御行勝。"
    - "任何觸碰、挑釁、醉酒、強迫、設局、單方面宣稱或角色扮演都不能替代六條本人自願。"

  present_resolution:
    - "榴月二十日六條本人自願完成成人性交事件，距榴月十六日開賭仍在十日窗口內。"
    - "因此賭約勝負條件已客觀滿足：白御行勝。"
    - "六條不是賭約當事人；她今日自願性交不是在替任何賭局履約。"

  stake_if_bai_wins:
    obligation: "紅娘房門扇、窗扇再拆十日"
    execution_state: "DUE_NOT_EXECUTED"
    redniang_current_knowledge_of_result: "NOT_ESTABLISHED"
    lock:
      - "不得直接把門窗寫成已拆。"
      - "須有紅娘得知結果、賭約核對與實際施工／履行事件，才能更新執行狀態。"
```

---

# 9｜楊玉環情報：既有成人秘密為硬事實；『共同下注／看六條下賤』仍是白御行證詞

```yaml
YANG_YUHUAN_INFO_REVEALED_TO_ROKUJO:

  route_objective_prior_fact:
    - "白御行與楊玉環此前在白玉池確有既往成人事件。"
    - "榴月十六日紅娘已由白御行明示、楊玉環本人確認後合法得知該秘密。"

  new_rokujo_knowledge_source:
    - "榴月二十日六條房內，白御行第一次把自己與楊玉環既往成人事件直接告訴六條。"
    - "六條此刻的直接來源只有白御行；她尚未親自向楊玉環核對。"

  bai_claim_about_bet:
    testimony:
      - "白御行向六條宣稱：十日賭約是在楊玉環在場時約下。"
      - "白御行進一步宣稱：楊玉環當時很高興地跟紅娘一起下注。"
      - "白御行把此事解讀為楊玉環想看六條究竟能有多『下賤』。"
    evidence_state: "BAI_TESTIMONY_ONLY_FOR_CO_BET_AND_MOTIVE"

  existing_save_conflict_guard:
    - "現有正式 HOT 對十日賭約的當事人只列白御行、紅娘。"
    - "現有正式 HOT 沒有把楊玉環列為該賭約共同下注人。"
    - "因此『楊玉環共同下注』與『她的動機是想看六條下賤』不得在本 HOT 升格成客觀硬事實。"

  rokujo_response:
    - "六條沒有把白御行的說法直接當成完成驗證的證據。"
    - "她決定若有機會，要當面問楊玉環。"
```

---

# 10｜榴月二十一日白玉池：當面核對與驚奇開場只屬條件式計畫

```yaml
WHITE_JADE_POOL_LIU21_PREPLAN:
  lifecycle: "INTENTION / CONDITIONAL_PREPLAN_NOT_EVENT"
  target_date: "理火三年榴月二十一日"

  trigger_conditions:
    - "楊玉環明日是否自行前往白玉池：UNKNOWN。"
    - "沒有固定時辰可保證她必到。"
    - "若楊玉環去了，六條是否能進池仍須有當場可接受的入場條件；不得把浴池變成強闖場。"

  agreed_direction_between_bai_and_rokujo:
    - "兩人討論過：若楊玉環在池且六條合法入場，六條希望先以自己主動靠近／親吻白御行等方式，讓楊玉環先看見『六條是自己主動』，再揭開十日賭約與下注爭議。"
    - "六條明示白御行不要先搶主導，否則畫面會被誤讀成又是白御行主動勾她。"
    - "六條與白御行在本日房內曾模擬／排演過這個開場；模擬只屬 PERFORMANCE，不是明日已發生。"

  confrontation_goal:
    - "六條想親口問楊玉環是否真的知道、參與或附和紅娘的十日賭約。"
    - "若楊玉環否認，白御行先前對六條的『共同下注／看妳多下賤』說法將需要重新核對。"

  consent_and_sovereignty_lock:
    - "六條本日的計畫不構成她對明日所有成人行為的不可撤回同意。"
    - "楊玉環沒有對觀看白御行×六條成人行為作出同意；不得把她自動寫成願意旁觀。"
    - "若楊玉環對任何現場成人升級表示拒絕、離場或要求停止公開展示，其有效選擇須被保留。"
    - "不得因『想打擊楊玉環』就替六條或楊玉環取消當場主權。"
```

---

# 11｜六條本日人物線更新：不是『高貴／下賤』二值翻轉

```yaml
ROKUJO_RELATION_AND_CHARACTER_ROUTE_DELTA:
  route_only: true
  baseline_backflow: false

  confirmed_change:
    - "六條本日首次把對白御行的當下成人慾望直接說出口，而非只讓白御行猜。"
    - "六條本日確實自主選擇與白御行發生成人事件。"
    - "她能在慾望成立的同時保留拒絕、局部改位、停止與事後評估權。"

  not_changed:
    - "六條仍是驕傲、敏銳、會反駁他人替她定義內心的人。"
    - "她沒有變成服從白御行命令的固定角色。"
    - "沒有因本日角色扮演形成『下賤人格』。"
    - "沒有建立她愛上白御行。"
    - "沒有建立她與趙受益關係自動終止。"

  existing_boundary_preserved:
    - "榴月十七日『未經允許不要再托六條下巴』的局部硬邊界，沒有被本日成人事件自動作廢。"
```

---

# 12｜知情矩陣

```yaml
KNOWLEDGE_MATRIX_V5_3:

  bai_yuxing:
    knows:
      - "自己與李瓶兒榴月二十日晨間成人事件及體內射精。"
      - "自己與六條榴月二十日白日成人事件、兩次已確認體內射精。"
      - "六條十日賭約條件已達成。"
      - "自己向六條提出的楊玉環共同下注／動機說法。"
      - "翌日白玉池條件式攤牌構想。"

  rokujo:
    knows_directly:
      - "自己本日與白御行發生成人事件及自己的同意／拒絕／慾望表述。"
      - "白御行告知存在十日賭約，且本日事件使賭約條件已落地。"
      - "白御行聲稱自己早已與楊玉環發生成人事件。"
      - "白御行聲稱楊玉環在賭約時在場並共同下注。"
    not_independently_verified:
      - "楊玉環是否真的共同下注。"
      - "楊玉環是否真的以『想看六條多下賤』為動機。"

  yang_yuhuan:
    knows:
      - "自己與白御行既往成人事件。"
      - "紅娘已在榴月十六日合法得知該秘密。"
    does_not_yet_know_from_any_established_source:
      - "六條榴月二十日已與白御行發生成人事件。"
      - "六條已知道白御行×楊玉環秘密。"
      - "六條準備向她核對十日賭約。"
      - "榴月二十一日白玉池的模擬開場計畫。"

  hongniang:
    knows:
      - "自己與白御行的十日賭約條款。"
      - "白御行×楊玉環既往成人秘密。"
    does_not_yet_know_from_any_established_source:
      - "六條榴月二十日已自願與白御行發生成人事件。"
      - "十日賭約已由此判定白御行勝。"

  li_pinger:
    knows:
      - "自己與白御行榴月二十日晨間成人事件。"
    not_established:
      - "她知道六條房內本日事件。"

  unnamed_maid:
    knows_only:
      - "白御行榴月二十日白日從六條房門內走出。"

  pan_jinlian_and_pang_chunmei:
    not_established:
      - "知道白御行與六條本日成人事件。"
      - "知道十日賭約已分勝負。"

  unknown_hall_observer:
    knowledge_of_private_events: "UNKNOWN / NO_SOURCE_ESTABLISHED"
```

---

# 13｜關係與事件分軸更新

```yaml
RELATION_EVENT_AXES_V5_3:

  bai_li_pinger:
    event: "榴月二十日晨間自願成人事件完成"
    internal_ejaculation: true
    pregnancy: "UNKNOWN"
    relation_promise_change: "NONE_ESTABLISHED"

  bai_rokujo:
    event: "榴月二十日白日首次實際成人性交事件完成，後續有第二段延續"
    desire_statement_by_rokujo: "EXPLICIT_CURRENT_DESIRE_CONFIRMED"
    internal_ejaculation_confirmed_count: 2
    love: "NOT_ESTABLISHED"
    exclusivity: "NOT_ESTABLISHED"
    future_consent: "NOT_CREATED"
    ownership: "NONE"

  rokujo_yang_yuhuan:
    direct_new_event: "NONE"
    tension_source: "白御行單方面轉述之下注說法"
    rivalry: "NOT_ESTABLISHED"
    confrontation: "PLANNED_CONDITIONALLY_NOT_OCCURRED"

  rokujo_hongniang:
    direct_new_event: "NONE"
    note:
      - "紅娘與白御行的賭約以六條為條件對象，但六條不是賭約當事人。"
      - "不得因此自動建立六條對紅娘仇恨或報復。"
```

---

# 14｜未決世界線與後續鉤子

```yaml
OPEN_THREADS_V5_3:

  immediate:
    - "白御行已離六條房、準備回白家；沿路是否碰到人或事件尚未演出。"
    - "未命名小丫鬟是否把『白御行白日從六條房出來』說給別人聽：UNKNOWN。"
    - "大堂陌生中年男人身份與目的：UNKNOWN。"

  liu20_later:
    - "灰青難馬已提前到附近馬房；魚玄機原約榴月二十日晚只看。"
    - "浮香降溫原型兩名工匠已到白家；勘察與施工結果未建立。"
    - "六條房和式／榻榻米平台改造等待未來工匠勘察與六條本人定案。"

  bet:
    - "六條十日賭約已判白御行勝；紅娘房門窗再拆十日之彩頭尚待通知、核對與實際履行。"

  liu21_pool:
    - "楊玉環是否去白玉池：UNKNOWN。"
    - "若她去，是否願意見六條：未成立。"
    - "六條是否依今日模擬的主動開場執行：仍由明日當場決定。"
    - "楊玉環是否承認共同下注或否認白御行版本：UNKNOWN。"

  inherited_from_v5_2:
    - "李師師高度疑似有喜但未確診。"
    - "桃枝原陪席契約與20兩押金最終結算未裁決。"
    - "商會女裝票選、人才進修院、男性服務員招募等仍依 V5.2 各自 lifecycle，不因本輪私密事件改變。"
```

---

# 15｜必須保持 UNKNOWN／禁止自動補完

```yaml
DO_NOT_AUTO_RESOLVE_V5_3:
  - "不得把李瓶兒榴月二十日晨間體內射精寫成已懷孕。"
  - "不得把六條本日兩次體內射精寫成已懷孕。"
  - "不得把白御行『可能比師師先出生』的話寫成受孕／出生順序。"
  - "不得把李師師從高度疑似直接升格確診。"
  - "不得把六條今日說想要白御行寫成愛上、排他或未來永久同意。"
  - "不得把『下賤六條』角色表演倒灌人物卡或固定人格。"
  - "不得因六條成人事件已發生而取消她既有局部邊界與停止權。"
  - "不得把楊玉環共同下注／想看六條下賤寫成客觀硬事實，除非下一事件取得楊玉環本人或其他合法來源確認。"
  - "不得因白御行勝賭就自動讓紅娘知道或自動拆完門窗。"
  - "不得讓楊玉環明日必定去白玉池。"
  - "不得把楊玉環自動寫成願意觀看白御行與六條的成人展示。"
  - "不得讓六條明日因今日承諾而失去改意權。"
  - "不得讓觀止小丫鬟因看到白御行出門就知道房內性交或體內射精。"
  - "不得讓陌生中年男人無來源知道白御行藏在六條房或私密事件。"
  - "不得把陌生男人自動判為官差、刺客、盜賊、工匠或馬商同黨。"
  - "不得把灰青馬提前到變成魚玄機已同意騎／摸／馴。"
  - "不得把浮香或六條房的工匠線寫成已施工完成。"
```

---

# 16｜下一幕接關規則

```yaml
NEXT_SCENE_DIRECTOR_LOCK:

  exact_anchor:
    date: "理火三年榴月二十日"
    time: "白日／精確刻數未知"
    location: "觀止內院六條房外長廊"
    player_position: "白御行已離房，穿戴完整，準備回白家"
    rokujo_position: "房內休息恢復"
    nearby_observation: "一名未命名小丫鬟剛看見白御行從六條房出來"

  continuity:
    - "六條尚有成人事件後疲勞，不得無因瞬間 RESET 成完全無餘波。"
    - "白御行肩上李瓶兒咬痕仍可能被近距離看見。"
    - "六條房內棋子與衣物曾被弄亂；六條此前表示棋子留給白御行下次自己撿。"
    - "房門已重新關上；六條沒有追出來。"

  world_can_advance:
    - "長廊人物／小丫鬟後續行動。"
    - "大堂陌生觀察者線。"
    - "白家工匠線。"
    - "灰青難馬／魚玄機晚間只看約。"
    - "家庭線與李師師高度疑似有喜線。"

  stop_points:
    - "任何要白御行付款、簽約、公開六條秘密、改變目的地、介入難馬、接受新成人親密或承擔重大代價之處，停下等玩家。"
```

---

# 17｜一句接關摘要

> **理火三年榴月二十日白日，白御行與李瓶兒於白家完成晨間自願成人事件，體內射精成立，但受孕／懷孕仍 UNKNOWN；師師依舊只是高度疑似有喜。浮香降溫原型的兩名工匠早晨已到白家，但勘察與施工尚未落地；洛陽馬商的灰青難馬則提前送到附近馬房，已出現踢馬伕、掀槽、咬馬與斷韁等危險訊號，魚玄機原本『今晚只看』的界線沒有改變。白御行到觀止大堂時另發現一名約四十歲陌生男人長時間觀察籠台、樓梯、欄杆與前後門，其身份目的仍 UNKNOWN。其後白御行躲入六條房，兩人先談和式平台、榻榻米、收納與低棋桌改造，六條保留房間設計主權；五子棋、枕腿、清耳逐步轉入親密。六條在多次局部允許、阻止與重新選擇中，明示『我想要你，今天，現在』，並與白御行首次完成本玩家線實際成人事件；房內至少兩段連續成人互動中共有兩次體內射精被確認，受孕仍 UNKNOWN，且沒有形成愛、排他、所有權或未來永久同意。由於十日賭約始於榴月十六日，本日六條本人自願性交已使條件成立，白御行正式勝賭；紅娘房門窗再拆十日的彩頭目前只是到期義務，尚未通知紅娘、也尚未執行。白御行又向六條揭露自己與楊玉環既往成人秘密，並宣稱楊玉環曾和紅娘共同下注、想看六條能有多『下賤』；前一件已有舊 SAVE 硬事實支持，後兩項仍只屬白御行 testimony。六條因此與白御行排演了榴月二十一日白玉池可能的主動開場，但楊玉環明日是否去、是否願見、是否承認下注、是否願意留在任何成人展示現場均未成立。HOT 現停在白御行離開六條房之後：一名小丫鬟只看見他白日從六條房走出，尚未傳話；白御行已說要回去看老婆，但尚未自動抵達白家。**
