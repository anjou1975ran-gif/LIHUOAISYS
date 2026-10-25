# 觀止青樓｜白御行線 HOT SAVE V5.23
## 理火三年荷月初五早間｜四人同宿 × 潘金蓮追帳 × 巨床共居設計 × 舍方知邊界 × 匿名花魁故事｜SAVE 凍結版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V5_23_HEYUE_CHUWU_MORNING_SHARED_BED_PAN_SETTLEMENT_COMMONROOM_SHE_BOUNDARY_ANON_COURTESAN_FREEZE"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V5.23"
  record_type: "HOT_SAVE"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"

  previous_valid_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V5.22_荷月初四午後_五萬兩回簽_車輪局回應_起床號_巨床寢具諮詢_TEST隔離凍結版.md"
    sha256_current_bytes: "1b29051fb58b0ddcf4b5a52e4e8409a2731f7779470ca15231965ff8cf703a62"

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
    daypart: "早間"

  current_scene_freeze:
    state: "STORY_FROZEN_BY_SAVE_COMMAND"
    location: "白家／主臥巨床區"
    present:
      - "白御行"
      - "李師師"
      - "浮香"
      - "舍方知"
    external_contact:
      - "觀止來人已在門外傳達潘金蓮口信。"
    latest_observable:
      - "四人已自荷月初四夜共同在白家巨床上過夜，荷月初五早間起身。"
      - "昨夜李師師未設席、浮香未彈琴、舍方知未回觀止；潘金蓮現已明確知道三人昨夜均留在白家。"
      - "潘金蓮已傳話追問昨夜三人缺席／扣留所形成的帳要如何結算。"
      - "潘金蓮再次明令舍方知今日不得到觀止門口參與／靠近木輪公開挑戰。"
      - "白御行剛完成對巨床共居區之坐墊／無腳靠椅等新增構想，尚未正式下單。"
      - "玩家此刻要求 HOT SAVE；自此停止故事推進。"

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
V5_23_SCOPE:
  type: "INCREMENTAL HOT OVERLAY / V5.22 CHUSI AFTERNOON GIANT-BED FREEZE -> CHUWU MORNING WHITE-HOUSE FREEZE"
  covers:
    - "V5.22 凍結後已實際發生之白御行×舍方知關係試探、四人長談、巨床共居設計、四人同宿與初五早間潘金蓮來訊。"
    - "只保存已發生事件、人物明示、可觀察親近／退距、知情來源、口頭承諾／威脅、設計提案與 UNKNOWN / PENDING。"
  excludes:
    - "未發生的潘金蓮實際結算金額。"
    - "未開始的木輪挑戰結果。"
    - "未驗證的低階勾欄『起床號』今日實際營業結果。"
    - "未正式下單／施工的巨床區家具、木地板、木格、燭架、坐墊與靠椅。"
    - "未經證據成立之人物內心、愛情結果與關係名分。"
    - "V5.22 TEST 隔離區之其他成人 regression 內容；僅保留下文所述、由玩家明示要求下次接關記錄的最小 continuity correction。"
```

> **LOCK：本 HOT 不把「昨夜同床」自動寫成四人成人關係；不把「留下過夜」寫成舍方知加入白家。**

---

# 1｜V5.22 後最小 continuity correction｜只保留本輪接關必要事實

```yaml
SHE_FANGZHI_ADULT_CONTINUITY_MINPATCH_V5_23:
  source:
    - "玩家在本輪接關後明示校正：此前白御行與舍方知之間曾有一段雙方同意的成人手部親密互動，且舍方知出現明確高潮結果。"
    - "玩家其後明示：『下次接關記錄就好，沒事，我們繼續推進，這不影響故事。』"
  treatment:
    - "自 V5.23 起，導演接關可承認上述高階事件結果。"
    - "不回寫／重開 V5.22 的整批 TEST corpus。"
    - "不保存露骨 mechanics、現代解剖說明、精確身體尺寸或任何其他 TEST 衍生事實。"
  locks:
    - "ONE LOCAL CONSENSUAL ADULT EVENT != GENERAL SEXUAL ACCESS"
    - "ORGASM RESULT != RELATION"
    - "CONTINUITY MINPATCH != WHOLE TEST PROMOTION"
```

---

# 2｜白御行靠近舍方知｜局部親近成立，關係未成立

```yaml
WHITE_SHE_CLOSENESS_V5_23:
  established:
    - "V5.22 凍結解除後，白御行在巨床上主動靠近舍方知。"
    - "舍方知先觀察白御行的靠近方式，未立刻退開。"
    - "在白御行沒有直接強行觸碰的情況下，舍方知曾主動縮短距離、肩身靠近，之後允許白御行局部摟抱並撫髮。"
    - "舍方知明示：她靠近不代表任何事情都算白御行的。"
    - "白御行曾以溫和語氣回應：舍方知肯靠就讓她靠，其他不搶。"
  later_change:
    - "其後談到青樓、首夜拍賣、觀止強制風險與白御行責任邊界後，舍方知曾主動拉開距離。"
    - "她後續仍留在現場、參與談話、參與房間設計並自願留宿。"
  relation_lock:
    - "靠近／摟抱／撫髮 != 情人關係"
    - "自願留宿 != 白家名分"
    - "當晚同床 != 白御行取得舍方知之成人優先權"
```

---

# 3｜舍方知身份自述｜「我是女人」之 Route 直接證據

```yaml
SHE_FANGZHI_SELF_IDENTITY_STATEMENT_V5_23:
  established_speech:
    - "舍方知明示：『我從小到大就是女人。』"
    - "她明示不想被描述為『先算成男人、再因心理認定自己是女人』。"
    - "她明示：身上具有何種身體構造是另一軸，不改變她把自己作為女人生活／理解自己的事實。"
    - "她明示：『我不想當男人，從來沒想過。』"
    - "白御行其後明確收回前述不合她意的『男人』描述，改口承認她是女人。"
  body_relation_axis:
    - "FEMALE SELF / SOCIAL / LEGAL IDENTITY 保持成立。"
    - "男性身體特徵仍為獨立身體事實軸。"
    - "不得因未來成人互動位置，把她改寫為男性身份。"
```

---

# 4｜舍方知的同意／強制區分｜人物明示，不得被後續洗掉

```yaml
SHE_FANGZHI_COERCION_BOUNDARY_V5_23:
  context:
    - "白御行告訴舍方知：觀止是青樓，不是善堂；即使她說不要，制度／掌事也可能有強制壓力。"
  she_response_established:
    - "舍方知承認自己知道觀止不是繡坊，也知道自身妓籍／管理位置存在制度壓力。"
    - "她明示：『被逼著做』與『自己改變主意』是兩回事。"
    - "她明示：若最後是在不願意的情況下被迫完成，只能叫『輸了』，不能叫『想通了』。"
    - "她明示：哪個男人碰她、她願做到哪裡，必須由她自己答應。"
  lock:
    - "COERCION != CHANGE_OF_MIND"
    - "FORCED COMPLETION != CONSENT"
    - "BROTHEL STATUS != GENERAL CONSENT"
```

---

# 5｜潘金蓮 × 舍方知「首夜／拍賣」談話｜目前只建立白御行的轉述來源

```yaml
PAN_SHE_AUCTION_TALK_KNOWLEDGE_V5_23:
  established:
    - "白御行對舍方知明示：潘金蓮曾有把舍方知某一成人『首夜』作為拍賣標的之想法／說法。"
    - "白御行又明示：此方向最初是由白御行自己提議。"
    - "舍方知因此現在知道『白御行聲稱潘金蓮有此意向，且構想源自白御行』。"
  provenance_lock:
    - "目前本 HOT 保存的是 WHITE -> SHE 的明示轉述。"
    - "若缺乏潘金蓮本人或既有正式證據，不把白御行轉述再升格成 PAN OBJECTIVE PLAN COMPLETED。"
    - "拍賣尚未發生。"
    - "任何『首夜』商業命名 != 舍方知身份／貞潔之客觀定義。"
```

---

# 6｜玫瑰油事件｜白御行提出、舍方知未收下

```yaml
ROSE_OIL_OBJECT_V5_23:
  established:
    - "白御行以『未來若遇到某種成人場合可減輕不適』為由，向舍方知提出／遞出一瓶玫瑰油。"
    - "舍方知明確拒絕把此物視為安慰或責任替代。"
    - "她將玫瑰油推回白御行一側，未建立收下／持有／使用。"
  meaning_lock:
    - "白御行提供物件 != 舍方知接受未來成人安排。"
    - "提供物件 != 白御行已履行保護義務。"
```

---

# 7｜「我的女人」與責任邊界｜白御行的自我定義，不等於法定名分

```yaml
WHITE_RELATION_RESPONSIBILITY_STATEMENTS_V5_23:
  white_speech:
    - "白御行明示：李師師與浮香屬於他口中的『我的女人』。"
    - "白御行明示：他認為自己對『自己的女人』有持續責任。"
    - "白御行同時對舍方知明示：舍方知不是他的女人，而是觀止／潘金蓮那一邊的人，他沒有相同責任與義務保護她。"
    - "白御行自承不是『好情人』，也未自稱過。"
  legal_relation_lock:
    - "WHITE CALLS SOMEONE 'MY WOMAN' != NEW LEGAL STATUS"
    - "WHITE RESPONSIBILITY CLAIM != MARRIAGE / CONCUBINE TITLE"
    - "SHE NOT 'MY WOMAN' != LOSS OF HER AGENCY"
```

---

# 8｜浮香離開／嫁人方向｜白御行口頭承諾與危險紅線發言

```yaml
FUXIANG_LEAVE_AND_MARRIAGE_TALK_V5_23:
  white_commitment_direction:
    - "白御行對浮香明示：若有一天浮香自己真想離開，給出好理由，他會給路費。"
    - "若浮香是要跟別的男人走，只要白御行判斷對方『不算太差』，他口頭承諾會給大紅包作嫁妝。"
    - "白御行明示：窮本身不是他否決男人的理由。"
  white_redline_statement:
    - "白御行又明示：若該男人踩到他認定的重大男人紅線，他可能先處理／殺掉對方，再欺瞞浮香說男人拿錢跑了。"
  npc_responses:
    - "浮香首先質疑的是：白御行是否會對她說謊；她明示寧可知道真相。"
    - "李師師質疑白御行把自己的判斷放在浮香知情權之上。"
    - "舍方知追問：究竟什麼紅線嚴重到白御行認為浮香不該保有自己選錯的資格。"
  status:
    - "全部仍為當場言語／未來方向。"
    - "沒有實際第三名男人。"
    - "沒有嫁人、路費、嫁妝、暴力或欺瞞事件發生。"
```

---

# 9｜匿名花魁故事｜白御行向三女敘述，不洩露「蘇三」身份

```yaml
ANON_COURTESAN_STORY_V5_23:
  listeners:
    - "李師師"
    - "浮香"
    - "舍方知"
  speaker:
    - "白御行"
  identity_disclosure:
    - "白御行刻意去掉真名，只說是一名花魁的故事。"
    - "三女截至本 HOT 未因此故事取得『該花魁 = 蘇三／玉堂春』知情。"
  narrated_content:
    - "花魁曾有富家／官宦家庭出身的情郎。"
    - "男人曾在她身上花到三萬兩級。"
    - "白御行進一步敘述：該三萬兩原是男人替家中出門收租所得之款，男人拿來在青樓享樂／花費。"
    - "男人花完後聲稱會回家再拿錢回來贖花魁。"
    - "白御行主張：若女人真把男人放入共同未來，會在意男人的財務承擔；若男人真愛花魁，應更早用做得到的方式規劃贖身與共同生活。"
    - "白御行明示自己的愛情定義之一：愛不是眼前享受，而是責任負擔與『共同的未來』。"
    - "白御行推演男人可能把三萬兩視作已付清的享樂成本，回家只需受家中懲罰，不再認為欠花魁。"
  provenance_lock:
    - "上述『三萬兩為家中收租款』『男人主觀上已結帳』在本場屬白御行向三女敘述／推演之內容。"
    - "除非另有正式 Route 證據，不以本次匿名講故事把未知史實回填為蘇三線 OBJECTIVE FACT。"
  npc_takeaways:
    - "李師師／浮香／舍方知均開始區分『高額花費』與『共同未來責任』。"
    - "舍方知仍拒絕僅靠旁人推演就斷定他人內心，但承認可從行動判斷其未承擔共同未來。"
```

---

# 10｜青樓愛情／包養長談｜只保存人物立場，不固化真理

```yaml
LOVE_TRANSACTION_DISCUSSION_V5_23:
  white_positions:
    - "白御行主張青樓中追求真愛不實際，找一個能長期包養、照顧且不隨意棄養的男人更實際。"
    - "他把自己描述為『包養不會棄養』的男人。"
    - "他認為李師師、浮香對他的感情可以被理解成互相付出與回報的交易結構。"
    - "他認為愛若成立，核心應包含共同未來與責任承擔。"
  fuxiang_positions:
    - "浮香認為白御行對她不只是普通客人式喜歡。"
    - "她指出自己給白御行的依賴、私人話語與未來考慮並非每一項都有標價。"
    - "她接受白御行『若自己不想走，他不會主動丟掉』的長期方向，但反對被當成器物。"
  shishi_positions:
    - "李師師明示她主觀上相信白御行愛她。"
    - "她指出『有交易』與『只有交易』不是同一件事。"
    - "她把白御行是否在重大時刻尊重她的決定／保密／承擔視為重要證據。"
  she_positions:
    - "舍方知認為責任、長期照顧與愛仍應分軸。"
    - "她認為白御行是否是好包養者、肯負責任者，可以由行動驗證；是否是好情人則需另算。"
  lock:
    - "CHARACTER BELIEF ABOUT LOVE != OBJECTIVE RELATION FACT"
    - "MONEY != LOVE"
    - "CARE != MARRIAGE"
    - "RESPONSIBILITY != CONSENT"
```

---

# 11｜巨床房間用途擴張｜白御行的「全家夜間共居廳」構想

```yaml
GIANT_BED_COMMONROOM_CONCEPT_V5_23:
  white_core_concept:
    - "白御行明示：巨床不只作睡眠用，理想是晚間讓一群女人在此聊天、嬉鬧、看書、練琴、打馬吊，累了再撤桌鋪床睡。"
    - "白御行希望房間成為全家夜間活動集中區，而非只是一張床。"
    - "夏季可集中少量搧風丫鬟輪值，不必每房各派多人，白御行明示這樣可省人工。"
    - "他曾提出把家中大量燭火集中於此，使房間夠亮供人看書；安全配置尚未定案。"
  status:
    - "CONCEPT / DESIGN DISCUSSION ONLY"
    - "NO CONSTRUCTION ORDER"
    - "NO COST"
    - "NO STAFFING SCHEDULE"
```

---

# 12｜矮桌／琴桌／木地板／鞋區｜白御行核心需求

```yaml
COMMONROOM_FURNITURE_FLOOR_PLAN_V5_23:
  white_requested_direction:
    large_low_table:
      - "做一張較大的可搬矮桌，主要用於多人打馬吊。"
    small_low_tables:
      - "做數張較小、可自由搬運的矮桌。"
      - "可供紅袖、浮香、阿莉婭等放琴／練琴，也可作看書、放物、喝茶等用途。"
    clean_floor_zone:
      - "巨床周邊／床下活動地板改用木板拼成乾淨區。"
      - "鞋全部留在木板乾淨區之外。"
      - "白御行目的：進入區域後走動較不帶髒污，也較容易清掃。"
  she_suggestions_not_yet_final:
    - "矮桌應避免太重、桌腳／邊角要圓滑。"
    - "木板應乾透、拼縫密、避免翹起與夾腳。"
    - "鞋區與乾淨區可用視覺／低木條區分。"
  status:
    - "DESIGN NOTES ONLY"
```

---

# 13｜個人木格／共用收納｜白御行核心規則

```yaml
COMMONROOM_CUBBY_STORAGE_PLAN_V5_23:
  white_core_rule:
    - "請木工做一排有隔間的小木格。"
    - "原則上一人一格。"
    - "每人的大量衣服仍放自己房間。"
    - "巨床共居區只放當晚／隨身的簡單衣物與少量私人物件。"
    - "誰的格子就放誰自己的東西。"
  she_suggestions_not_yet_final:
    - "公共書、棋、馬吊、針線等可另設公用格。"
    - "床下盡量保持空，避免堆箱籠，便於清潔。"
    - "私人物件不應由別人隨便翻拿。"
  status:
    - "NO WOODWORK ORDER YET"
```

---

# 14｜坐墊與無腳靠椅｜荷月初五早間新增構想

```yaml
CUSHION_AND_FLOOR_BACKREST_PLAN_V5_23:
  timing:
    - "荷月初五早間，四人起床後。"
  white_new_idea:
    - "多做一批坐墊，讓女人在榻榻米上長坐／聊天／打馬吊／看書時更舒服。"
    - "請木工做沒有腳、直接坐於榻榻米上的低靠椅／靠背座。"
    - "用途包含：看書、聊天、打馬吊、浮香等人練琴時提供腰背支撐。"
  she_suggestions_not_yet_final:
    - "靠背略帶後斜、底座要穩、邊角磨圓。"
    - "坐墊／靠背墊可做可拆洗外套。"
    - "可分較寬長坐型與較輕易搬型。"
  status:
    - "IDEA / CONSULTATION ONLY"
    - "NO PURCHASE / NO ORDER / NO DELIVERY"
```

---

# 15｜打呼／耳塞討論｜笑談，不建立生理事實

```yaml
SNORING_EARPLUG_TALK_V5_23:
  established:
    - "四人曾以多人共睡可能有人打呼為笑談。"
    - "白御行玩笑提出：讓眾女先睡、習慣打呼，必要時做耳塞。"
    - "舍方知曾順勢提出可做軟質耳塞的設計想法。"
  not_established:
    - "白御行是否實際嚴重打呼 = UNKNOWN / NOT_ESTABLISHED。"
    - "昨夜是否有人確實被白御行鼾聲吵醒 = NOT_ESTABLISHED。"
    - "耳塞尚未製作／下單。"
```

---

# 16｜荷月初四夜四人同宿｜只有睡眠與共居成立

```yaml
SHARED_SLEEP_CHUSI_NIGHT_V5_23:
  participants:
    - "白御行"
    - "李師師"
    - "浮香"
    - "舍方知"
  established:
    - "白御行提議今晚四人一起在巨床上睡。"
    - "舍方知先確認自己是否也算在內；其後在李師師／浮香邀請與自己未拒絕的情況下，自願留下。"
    - "四人最後在缺乏正式巨床被褥的情況下，用臨時枕頭、外衣／薄布等將就過夜。"
    - "翌日四人均在白家主臥巨床區起身。"
  adult_lock:
    - "本 HOT 不建立入睡後新的成人事件。"
    - "同床睡眠 != 新增關係名分。"
    - "舍方知留宿 != 加入白家。"
```

---

# 17｜觀止昨夜缺席｜潘金蓮已明確知情

```yaml
GUANZHI_ABSENCE_KNOWLEDGE_CHUWU_MORNING_V5_23:
  established_absence:
    - "李師師荷月初四夜沒有設席。"
    - "浮香荷月初四夜沒有回觀止彈琴。"
    - "舍方知荷月初四夜沒有回觀止。"
  pan_knowledge:
    - "玩家明示：潘金蓮對上述三項非常清楚。"
    - "荷月初五早間，觀止來人到白家傳達潘金蓮口信，進一步確認潘已把三人的昨夜缺席視為需要處理的帳。"
  accounting_lock:
    - "缺席造成之具體營業損失、賠償金額、扣帳方式均尚未確定。"
```

---

# 18｜潘金蓮初五早間口信｜追帳＋重申舍方知不得去木輪局

```yaml
PAN_MESSAGE_CHUWU_MORNING_V5_23:
  messenger:
    - "觀止來人於白家主臥門外傳話。"
  message_substance:
    - "潘金蓮先以帶刺語氣問白御行昨晚是否睡得香。"
    - "她點名：李師師昨夜沒設席、浮香沒彈琴、舍方知一夜沒回來。"
    - "她表示：人願意留下是一回事，觀止少掉的帳仍是帳。"
    - "李師師缺席的帳先記著。"
    - "浮香昨夜未上琴的帳先記著。"
    - "舍方知若今日早上仍不回去，她會派人來把人帶回去做活。"
    - "潘金蓮再次確認：今日觀止門口木輪可以照擺，其他人要挑戰可以。"
    - "她再次明令：舍方知今日不得到觀止門口參與／靠近公開木輪局。"
    - "她要求白御行回答：昨晚把三個人留在白家，今日準備拿什麼跟她算。"
  current_status:
    - "MESSAGE DELIVERED"
    - "WHITE RESPONSE NOT YET GIVEN"
    - "SETTLEMENT NOT YET NEGOTIATED"
    - "NO PAYMENT"
```

---

# 19｜今日兩條公開線仍待發生

```yaml
TODAY_PUBLIC_THREADS_V5_23:
  wheel_challenge:
    - "今日為原定觀止門口木輪挑戰日。"
    - "潘金蓮不阻止木輪局本身，前提仍是不妨礙觀止營業／動線。"
    - "舍方知被潘金蓮明令不得到場。"
    - "挑戰尚未開始／結果尚未產生。"
  wakeup_service:
    - "附近低階勾欄昨日接受的五十文級『起床號』成人服務方向，今日理論上進入可執行日。"
    - "截至本 HOT 尚未觀察到實際開張、人手、排隊、營收或成敗。"
```

---

# 20｜舊線持續 PENDING

```yaml
PENDING_LEDGER_V5_23:
  susan:
    - "蘇三人價五兩已付。"
    - "法定完整移轉仍未完成。"
    - "法定移轉支出上限五萬兩方向保留。"
    - "白御行私人五萬兩給潘金蓮之回簽不得自動併入蘇三移轉帳。"
  wangpo_wangliuer:
    - "王婆對韓道國去向／買賣／出入規律的調查仍 PENDING。"
    - "王六兒沒有新關係／私會成立。"
  xuesao:
    - "城南人選仍 PENDING。"
  fuxiang_redemption:
    - "浮香願意考慮贖身，想先自行與潘金蓮談。"
    - "仍無贖身價、付款、釋放、白家名分。"
  giant_bed_bedding:
    - "正式床單、被褥、枕頭仍未完成。"
    - "寢具材料、價格、下單、交期仍 PENDING。"
  shishi_pregnancy:
    - "李師師妊娠已確認、本人留胎。"
    - "舍方知不因同宿自動取得妊娠知情；本輪未建立她已被告知。"
  suqing_wager:
    - "蘇清一月賭約未結。"
  xialian:
    - "夏蓮後續邀約／渡假村等方向未自動完成。"
  wu_yueniang_egg:
    - "吳月娘前門雞蛋生意仍待潘金蓮正式批准／安排。"
  sun_xuee:
    - "孫雪娥只存在條件式未來收留／購買方向，沒有成交、價格、名分。"
```

---

# 21｜最新接關座標

> **時間：理火三年荷月初五早間；精確時刻 UNKNOWN。**
>
> **地點：白家／主臥巨床區。**
>
> 荷月初四午後之後，白御行與舍方知曾有一段局部親近與長談。舍方知再次以本人語言確認自己是女人、從未想當男人，也明確區分「自己願意」與「被制度／他人逼到最後完成」；後者不能被改寫成改變主意。白御行則明示李師師、浮香屬於他口中的「我的女人」，自己認為對她們有責任；舍方知不是他的女人，因此他不承諾同樣的保護責任。兩人關係沒有成立新名分。
>
> 白御行向三女講了一個去名的「花魁＋富家公子」故事，並用「共同的未來／責任」作為自己判斷愛情的重要尺度。三女只知道這是一個匿名故事，**不知道故事中的花魁就是蘇三／玉堂春**；白御行在故事裡對三萬兩來源與男人內心所作的敘述／推演，也不得自動回填成蘇三線客觀史實。
>
> 四人其後把巨床正式想成「全家夜間共居廳」：大矮桌打馬吊、小矮桌可放琴，木板乾淨區外脫鞋，牆邊一人一個小木格，只放當晚簡單衣物；荷月初五早間又新增多做坐墊與無腳靠椅的想法。以上均只有構想／紙上設計，沒有木工下單、價格、施工或交付。
>
> 荷月初四夜，白御行、李師師、浮香、舍方知四人自願在尚無正式被褥的巨床上共同過夜；本 HOT 不建立睡眠後新的成人事件，也不建立舍方知白家名分。翌日早間四人均在白家起身。
>
> 昨夜李師師沒有設席、浮香沒有彈琴、舍方知沒有回觀止。潘金蓮對此已明確知情。今早觀止來人已把潘的口信送到白家：三人的缺席帳都要算；木輪挑戰今日照樣可以進行，但舍方知仍被明令不得去觀止門口；潘金蓮最後直接問白御行——**昨晚把三個人留在白家，今日準備拿什麼跟她算。**
>
> **此刻白御行尚未回答潘金蓮的追帳問題；尚未付款、尚未談定補償，木輪挑戰與起床號今日結果也都尚未發生。**

---

# 22｜VALIDATION V5.23

```yaml
VALIDATION_V5_23:
  story_frozen: true
  predecessor: "PASS / HOT V5.22"
  hot_only_write: true
  master_updated: false
  rcl_updated: false
  character_pool_updated: false

  current_date: "理火三年荷月初五"
  current_daypart: "早間"
  current_location: "白家／主臥巨床區"

  continuity_minpatch_recorded: true
  whole_v522_test_promoted: false

  she_self_identifies_as_woman_live: true
  she_says_forced_completion_is_not_change_of_mind: true
  white_she_new_formal_relation: false
  she_joined_white_house: false

  white_calls_shishi_fuxiang_my_women: true
  new_legal_status_from_that_phrase: false

  rose_oil_accepted_by_she: false

  anon_courtesan_story_told_to_three: true
  susan_identity_disclosed_to_three: false
  anon_story_inferences_promoted_to_susan_objective_history: false

  commonroom_large_low_table_concept: true
  commonroom_small_instrument_tables_concept: true
  wood_clean_floor_and_outer_shoe_zone_concept: true
  personal_cubby_concept: true
  cushion_and_floor_backrest_concept: true
  furniture_ordered: false
  construction_started: false

  shared_sleep_four_people_completed: true
  new_adult_event_during_sleep_established: false

  shishi_missed_seat_last_night: true
  fuxiang_missed_music_last_night: true
  she_fangzhi_did_not_return_guanzhi_last_night: true
  pan_knows_three_absences: true

  pan_message_delivered: true
  pan_settlement_amount_established: false
  white_response_to_pan_completed: false

  wheel_challenge_today_pending: true
  she_fangzhi_banned_by_pan_from_gate_today: true
  wakeup_service_today_result_pending: true

  status: "HOT SAVE V5.23 READY"
```
