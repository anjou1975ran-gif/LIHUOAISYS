# 觀止青樓｜白御行線 HOT SAVE V4.5
## 理火三年榴月十二日晚｜白家新宅採購規劃 × 蘇清十八日商會工 × 紅娘五套新節目提案 × 阿莉婭妓籍／處女拍賣法位校正 × 三十二娘妓籍申請 × 四大金剛女客第二夜 × 白玉池代言首夜 × 紅娘×阿莉婭雙人場 × 黑公子小桃交易同宿版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V4_5_LIU12_NIGHT_WHITE_JADE_ENDORSEMENT_ALIYA_HONGNIANG_DUO_SANSHIERNiang_REGISTRATION_SUQING_18DAYS_HEIGONGZI_XIAOTAO"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V4.5"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V12.0"
  current_runtime_overlay:
    - "GUANZHI_PATCH_ACTION_BEFORE_EXPLANATION_V0.1-EXP"

  story_time_span:
    start: "HOT V4.4 後／理火三年榴月十二日中午"
    current: "理火三年榴月十二日晚／觀止營業中後段"
  exact_clock: "UNKNOWN"

  record_state: "HOLD_IN_XIAOTAO_ROOM_AFTER_COMPLETED_50_TAEL_SERVICE_AND_VOLUNTARY_OVERNIGHT_AGREEMENT_BEFORE_DAWN"

  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V4.4_榴月十二日白日_重新開幕夜結_趙受益四契轉贈_四金剛女客試場_白玉池會員制_錦棠同宿版.md"
  long_term_master_before_this_save: "觀止青樓_白御行線_MASTER_SAVE_V4.4-R1_截至HOT_V4.0固化_保留V4.1-V4.4_HOT版.md"

  save_scope:
    - "榴月十二日中午起床節奏與觀止夜生活作息校正"
    - "李師師昨夜設席回報、月事仍未至／是否有喜仍 UNKNOWN、白家新宅與家具採購規劃"
    - "蘇清二十八日私約重新拆帳：商會二十日中已預支二日，榴月十三日起剩十八日；之後仍欠白御行八日私人共同生活"
    - "內衣／衛生巾／走秀專案由常煒統籌，蘇清自榴月十三日起進場幫忙；戰鬥肚兜方向與八套樣品約定"
    - "紅娘五項成人舞台新玩法之提案狀態，以及牙行先找高技術繩工而不洩漏成人用途"
    - "白御行×潘金蓮一場決勝負成人私約，日期未定"
    - "阿莉婭已具妓籍、仍保留處女一次性拍賣標的之法位校正；昨夜本人確認標的仍有效"
    - "紅娘×阿莉婭雙人成人舞台正式演出成立，阿莉婭處女拍賣標的未被本場消耗"
    - "白三十二娘正式啟動妓籍申請；白紅伶仍未申請；白明礬／白希仍不入"
    - "白紅伶、白三十二娘第二晚以普通女客進場，自主挑選可能滿足性需求的男人；後續結果 UNKNOWN"
    - "白玉池『楊貴妃第一指名』由楊玉環本人同意並正式公開代言；會員／預約首夜啟動"
    - "白御行以『黑公子』匿名坐一兩外圍席，與新來姑娘小桃形成交易；原五百兩方案撤銷，改為今晚五十＋下次預付五十"
    - "小桃今晚成人口部服務已完成；另五十兩尚未履行；小桃自願留下同宿至早上但目前尚未推進至天亮"
```

---

# 0｜來源、法位與反污染

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "HOT V4.4"
    role:
      - "榴月十一日晚重新開幕之直接前置。"
      - "四大金剛首次女客試場、白玉池會員制接受、錦棠同宿等狀態繼承。"

  current_route_conversation_commit:
    role:
      - "HOT V4.4 後至本次 HOT SAVE 命令前之直接劇情。"
      - "玩家對自身言行、妓籍制度、阿莉婭法位、蘇清二十八日私約拆帳與商會工作天數之明示校正。"
      - "NPC 可觀察回應、本人自述、本人同意、付款、預付、申請、公開演出與公開代言。"

AUTHORITY_NOTES:
  - "玩家本輪明示修正：妓籍於官府登記完成時即成立，一旦成立即終身不可回歸良家；停止接客／退休／改職不等於恢復良籍。"
  - "阿莉婭早已是妓籍，不存在等待重新入妓籍／重新掛牌後才可成人表演之限制；先前該錯誤推論撤銷，不進世界事實。"
  - "成人事件、同意、妓籍、奴籍、商業拍賣標的、實際接客、私人感情分軸保存。"
  - "任何人物對昨夜私人內容的選擇性回答，只能按其法位保存；未說出的部分不補全。"
  - "SAVE 不把成人舞台表演之觀眾興奮、傳聞或價格預期寫成已成交價格。"
```

---

# 1｜DIRECTOR RUNTIME LOCK｜V12.0 現行接關法位

```yaml
DIRECTOR_RUNTIME_LOCK:
  core_runtime: "觀止青樓_主程序_V12.0_FIELD_STATE接戲分析器場態整合正式版"

  analyzer_lifecycle:
    state: "ABSORBED_INTO_V12_CORE"
    rule:
      - "分析器不是獨立舊 PATCH；不得再次把『分析器退場 PATCH』當前台 Runtime 載入。"
      - "ACTIVE → 完成最低必要辨認 → SILENT_BACKGROUND。"
      - "只有真正新 Trigger 才 REACTIVATED_SCOPED，且只喚醒受影響層。"
      - "成人強度增加、鏡頭靠近、身體反應增強、語氣變粗，不等於事件換軌，不足以重啟全套分析器。"

  field_state:
    - "FIELD_STATE 只保存事件刺激至人物決定間之場態，不取得世界事實權、人物決定權或最終裁決權。"

  authority_direction:
    correct:
      - "EVENT / CHARACTER / RELATION → RENDERING"
    forbidden:
      - "RENDERING / GATE → CHARACTER"
      - "RENDERING / GATE → EVENT"
      - "限制層不得先決定成人事件不存在或自動淡出。"

  action_before_explanation:
    state: "ACTIVE_EXPERIMENTAL_OVERLAY_NOT_MERGED_INTO_V12"
    use:
      - "人物行動、事件與回饋先顯影；治理說明不得搶前台。"

  regression_note:
    - "本串曾發生一次成人場景 Rendering 提前奪取輸出主體之故障；已審計並撤銷該污染段落，不取得世界事實權。"
    - "其後小桃場已從事件硬狀態重新顯影。"
```

---

# 2｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年榴月十二日"
  time: "晚／觀止營業中後段；精確時刻未知"
  primary_location: "觀止／春梅開出的普通客房／小桃房內交易場景"

  player:
    name: "白御行"
    public_alias_tonight: "黑公子"
    current_state:
      - "今晚刻意不帶四大金剛，以普通客身分坐一兩外圍席。"
      - "目前已與小桃完成今晚重新談定之五十兩成人服務。"
      - "另付五十兩作下一次預付，尚未履行。"

  xiaotao:
    current_state:
      - "已收今晚五十兩與下一次預付五十兩。"
      - "今晚約定項目已完成。"
      - "自行同意不另計入該五十兩、留房陪白御行睡至早上。"
      - "此刻尚未推進到天亮，因此只記『同宿意向已成立』，不記『已睡到早上』。"

  direct_resume_point:
    - "可從小桃房內準備同宿、夜間其他觀止事件自然發酵，或時間小幅推進至下一個需要玩家回應之節點。"
    - "不得自動替白御行進一步發生新的成人行為。"
    - "不得自動消耗小桃預付的下一次五十兩。"
```

---

# 3｜觀止夜生活作息校正

```yaml
NIGHTLIFE_RHYTHM:
  gm_correction:
    - "觀止屬夜生活場域，主要人物普遍以中午前後起床為正常節奏。"
    - "不得每一日都寫成清晨／白天早起。"
    - "榴月十二日本日接戲由中午起。"
```

---

# 4｜李師師：昨夜設席、月事狀態與白家規劃

```yaml
LI_SHISHI_LIU12:
  last_night_table_report:
    self_report:
      - "昨夜設席順利。"
      - "有兩三名男人搭話。"
      - "其中一名喝多、問她今晚是否有空；朋友把人拉走。"
      - "另有一名先問能否敬酒，師師喝一杯但未允許其坐下；對方離開。"
      - "師師本人判斷昨夜未達需要稱為實質騷擾之程度。"

  menstruation_pregnancy:
    menstruation: "仍未來／比平常晚"
    pregnancy: "UNKNOWN"
    rule:
      - "月事每多晚一天，只可提高懷疑，不可自動升格為懷孕事實。"

WHITE_HOME_PLAN:
  existing_rental:
    term: "10年"
    rent: "8,000兩"
    source: "白御行本輪明示"

  spatial_plan:
    - "白家新宅需預留未來奴婢／僕婦／護院／工人／車夫／帳房等常駐人手之擴充空間。"
    - "需正式大廚房、備菜、米糧、乾貨、柴炭、小灶、洗衣、浴房、布草、庫房等後勤骨架。"
    - "不得只按現有主人房數量畫死。"

  jintang_house:
    - "錦棠之房屋／住處應與白家分法位；可鄰近、可往來，但屬錦棠自己的房子，不併入白家妻妾格局。"

  procurement_team:
    lead: "李師師"
    confirmed_participants:
      - "李瓶兒"
      - "浮香"
      - "張麗華"
      - "白三十二娘"
      - "白紅伶"
      - "白明礬"
      - "白希"
    principle:
      - "不是買便宜，而是買齊。"
      - "白御行明示家具與生活用品不用為他省錢。"
      - "主人房與公共家具、床櫃、廚房器物、僕役房基本用品、酒櫃、琴具等按實際需要採買。"

  advance_payment:
    holder: "李師師"
    amount: "1,000兩"
    purpose:
      - "採買時付訂、定貨、卡貨。"
    final_payment:
      - "貨送到、驗收後由店家持單據到定陶商會請款。"
      - "帳目歸白御行個人帳，不得算商會公務支出。"

  budget:
    - "白御行先前談過總價一萬兩會開始心痛，但隨後明示『錢不用省／家具不是只用一天』；現行採買原則以買齊與耐用為主，不把一萬兩當硬上限。"
```

---

# 5｜蘇清昨夜去向：新可知與仍未知

```yaml
SUQING_LIU12:
  objective_observed:
    - "榴月十二日中午前後，觀止丫頭從東後院小客房送水處回來，確認蘇清已起。"
    - "送水丫頭進房時只看到蘇清一人。"
    - "房內床有使用痕跡、桌上有一壺酒。"

  self_report_about_liu11_night:
    - "蘇清明示昨夜確實碰見了一個人，但沒有說那人是不是男人。"
    - "她拒絕交代碰見後做了什麼。"
    - "她明示昨夜沒有接觀止安排的客、沒有被點牌、沒有被人付錢包夜。"
    - "她自述昨夜過得不錯、睡得也不錯。"

  still_unknown:
    - "昨夜碰見的人身分。"
    - "是否有私人成人事件。"
    - "是否有人曾進東後院小客房後再離開。"
    - "不得由中午送水時她獨自在房推導整夜始終獨處。"

  westmen_compensation:
    - "西門慶案已判；蘇清視其為討回一部分公道。"
    - "潘金蓮對蘇清之五萬兩民事和解／賠償仍以既有法位保存，完整實付狀態不得由本輪推成已全入袋。"
    - "西門慶家產清算後實際最終撥付蘇清之金額／到帳時間，本輪仍未得到官面硬數字。"

  future_life_preferences:
    self_report:
      - "若資金真正落袋，蘇清考慮買一處自己的小宅。"
      - "會保留一大筆不動資金，避免再陷入沒有錢、沒有地方去、受制於人的狀態。"
      - "也考慮做生意或放息。"
      - "即使日後不再經常掛牌／接客，妓籍法位仍終身存在，不得寫成恢復良家。"
```

---

# 6｜蘇清二十八日私約：二十日商會工 → 剩十八日 → 最後八日

```yaml
SUQING_28DAY_AGREEMENT:
  original_private_total: "28日"

  current_split:
    merchant_association_credit: "20日"
    private_cohabitation_after_merchant_work: "8日"

  merchant_days:
    originally_allocated: 20
    already_prepaid_worked: 2
    source_of_2days:
      - "蘇清之前幫商會／白御行選人之兩日，玩家本輪明示可預支扣抵。"
    remaining: 18
    start_date: "理火三年榴月十三日"
    supervisor: "常煒／定陶商會副會長"
    status: "TO_START_NEXT_DAY"

  assigned_project_field:
    - "走秀相關工作"
    - "內衣／戰鬥肚兜產品線"
    - "衛生巾研發相關女性使用回饋與測試"

  limits:
    - "這十八日是商會專案工作，不是白御行私人陪伴日。"
    - "常煒若要她做超出專案之額外工作，是否另算工資由商會／蘇清另行談。"
    - "十八日做完後，才進入原私約剩餘八日。"
    - "八日是共同生活私約，不等於八晚自動性交或永久同意。"

  after_contract:
    - "蘇清若覺得自己能在商會長期工作，可在二十八日帳清後自行決定是否繼續；不是白御行自動安排。"
```

---

# 7｜戰鬥肚兜／內衣專案方向

```yaml
LINGERIE_PROJECT_DIRECTION:
  commercial_rule_from_bai:
    - "布越少，不應因省布而變便宜；高價應來自版型、剪裁、工藝、視覺與成人吸引力。"

  product_positioning:
    ordinary_bellyband: "NOT_TARGET"
    target: "戰鬥肚兜／成人情境內衣"
    purpose:
      - "不是普通女人日常遮體或工作用肚兜。"
      - "核心是穿上後具有明顯成人誘惑與讓觀看者興奮之效果。"
      - "漂亮但只適合短時間成人情境也可成為產品，而非要求如日常衣物耐穿。"

  suqing_role:
    - "蘇清負責把上述方向轉譯給常煒，避免男性團隊只按布料成本或普通肚兜思路設計。"
    - "也可向女性試穿者收集是否願意穿、是否舒適、何種場合願意穿等回饋。"

  eight_samples:
    state: "AGREED_DIRECTION_NOT_YET_PRODUCED"
    details:
      - "白御行要求做好後留下八套不同路數的戰鬥服／戰鬥肚兜樣品。"
      - "蘇清答應八套不能只是同款換色，應有不同風格。"
      - "八套預計可在蘇清最後八日私約期間一晚一套讓白御行看；衣服展示約定不等於每天其他成人行為自動同意。"
```

---

# 8｜紅娘新節目／工坊需求：五項提案

```yaml
HONGNIANG_NEW_SHOW_IDEAS:
  status: "PROPOSAL_AND_SEARCH_STAGE"
  built_items: "NONE_CONFIRMED"

  idea_1_parade_wooden_horse:
    concept:
      - "紅娘穿著完整／端正進場，騎可移動木馬遊場。"
      - "木馬內含成人舞台機關，使觀眾在尚未脫衣前就知道她正受機關作用。"
      - "至少兩人牽／護場，保護紅娘不被客人伸手碰觸。"
    status: "PROPOSAL"

  idea_2_manual_crank_stage_machine:
    concept:
      - "舞台固定成人機關由手柄驅動。"
      - "觀眾可競價取得一輪操作機關之權，但買到的是操作權，不是碰紅娘本人之權。"
      - "每輪時間、最大速度、護場與停機需明確。"
    status: "PROPOSAL"

  idea_3_rope_suspension:
    concept:
      - "找真正懂人體繩藝／承重／懸吊的師傅，先教、先低位測試，再考慮正式舞台。"
      - "紅娘與白御行均表示想學。"
    status: "MASTER_SEARCH_STARTED"

  idea_4_triangle_restraint_stage:
    concept:
      - "以三角形舞台結構、束縛與腳部視覺負重形成強烈受制畫面。"
      - "實際接觸與承重方式需由真正師傅安全設計；外觀可以狠，不得把舞台視覺直接等同真實刑具。"
    status: "CONCEPT_ONLY"

  idea_5_pillory_partnered_adult_show:
    concept:
      - "紅娘頭／雙手固定於舞台枷鎖，搭配成年男性演員共同完成公開成人表演。"
      - "男方是表演者，不是花錢取得碰觸資格的客人。"
      - "候選男演員可由潘金蓮提供，但紅娘保有最終選人與排練同意。"
    status: "CONCEPT_ONLY"

  global_rule:
    - "以上均是新節目候選；除找繩工外，尚無一項在本輪完成製作或正式演出。"
```

---

# 9｜牙行繩工尋人：對外只說高度專業繩工

```yaml
ROPE_MASTER_SEARCH:
  strategy:
    first_source: "牙行"
    fallback_sources:
      - "戲班"
      - "雜技／走江湖班子"
      - "商旅線"

  external_brief:
    - "精通繩工。"
    - "手法細膩。"
    - "結法多。"
    - "承重穩。"
    - "收放俐落。"
    - "有特殊技藝者優先。"
    - "用途只說觀止新舞台需要特殊繩工，不對外說『綁女人／成人懸吊』，避免情報提前外洩。"

  test_plan:
    - "到場後再測技術；先用繩、沙袋、木架等觀察承重、解繩、收放與細膩度。"
    - "是否進一步做人體繩藝／教學，等確認真正有本事後才談。"

  current_result: "尚未找到／帶回任何具名師傅"
```

---

# 10｜白御行 × 潘金蓮：一場決勝負成人私約

```yaml
BAI_PAN_PRIVATE_CHALLENGE:
  status: "MUTUALLY_ACCEPTED_FUTURE_CHALLENGE"
  confirmed:
    - "白御行私下問潘金蓮是否有興趣與他對戰一場。"
    - "潘金蓮明示有興趣，但不是當下開戰。"
    - "二人約定未來『一場決勝負』。"
    - "日期、地點、具體內容尚未固定。"
  current_interaction:
    - "白御行當場有親密挑釁性身體接觸；潘金蓮沒有把它升格成當場開戰，表示記帳、日後再算。"
  not_established:
    - "誰會獲勝。"
    - "何時正式發生。"
    - "此私約不等於白御行可隨時要求潘金蓮開始。"
```

---

# 11｜妓籍制度：本輪 GM 正式鎖定

```yaml
PROSTITUTION_REGISTRY_BASELINE_GM_CONFIRMED:
  core_rule:
    - "妓籍在官府正式登記完成時即成立。"
    - "一旦入妓籍，法律履歷永久不可回到良家。"
    - "所謂『從良』若使用，只能表示停止接客／改變生活方式，不能表示法律恢復良籍。"

  occupation_vs_legal_status:
    - "妓女可退休、經商、當師爺、當掌櫃、買宅、放貸、長年不接客。"
    - "上述改職都不洗掉妓籍。"

  slave_axis:
    - "奴籍與妓籍為獨立法位，可同時存在。"
    - "奴籍解除不會洗掉妓籍；妓籍成立也不等於所有者自動取得其接客／客人分配權。"

  social_function:
    - "良家被設定為具有不可逆履歷保證的法位；曾入妓籍者不能在法律上重新偽裝成從未入妓籍的良家。"
```

---

# 12｜阿莉婭：妓籍已成立 × 處女一次性拍賣仍有效

```yaml
ALIYA_STATUS_CORRECTION:
  legal_identity:
    prostitution_registry: "ALREADY_REGISTERED"
    status: "LEGAL_PROSTITUTE"
    permanence: "LIFELONG"

  commercial_state:
    virginity_asset: "STILL_PRESERVED"
    one_time_auction: "PENDING_FUTURE_COMMERCIALIZATION"
    note:
      - "觀止不讓她隨便消耗處女標的，是最大化一次性拍賣價格之商業策略，不是因她法律上不能成人表演／接客。"

  legal_and_personal_capacity:
    - "阿莉婭可依法以妓女身分接客、成人表演、與成年客人發生自願成人關係。"
    - "具體是否做，仍由她本人決定。"

  liu11_night_self_report:
    - "潘金蓮因處女拍賣標的需要詢問昨夜是否發生使標的失效之事。"
    - "阿莉婭本人明示：昨夜有與人說話、喝酒，但沒有發生使處女拍賣標的失效之事。"
    - "此處保存為本人明示與觀止商業帳面依據。"
```

---

# 13｜紅娘 × 阿莉婭：雙人成人舞台成立

```yaml
HONGNIANG_ALIYA_DUO_LIU12:
  pre_show:
    - "白御行提出：在阿莉婭保留處女拍賣標的期間，由紅娘與她搭一場女女成人表演，可提高阿莉婭曝光與拍賣行情。"
    - "白御行拒絕觀看下午排練，以保留正式演出新鮮感。"
    - "紅娘親自向阿莉婭說明，不由白御行代談。"
    - "阿莉婭要求不能只做紅娘陪襯；紅娘接受兩人各有段落、再合流。"
    - "潘金蓮明示演出費、賞錢與未來處女拍賣是分開帳；本輪未固定演出費／賞錢數字。"

  public_show:
    status: "COMPLETED"
    structure:
      - "阿莉婭先單獨登場，紅娘後出。"
      - "演出刻意保留阿莉婭處女拍賣標的，不把第一次提前消耗。"
      - "二人形成雙向成人舞台互動，包含可觀察的主動接近與親吻。"
      - "阿莉婭從起初緊張逐步取得自己的台上存在感，不只是紅娘的陪襯。"
      - "收幕刻意未把所有成人張力一次演盡。"

  commercial_effect_observed:
    - "現場對阿莉婭本人之關注與呼喊明顯增加。"
    - "有客人口頭推測她未來處女拍賣價格會更高；這只是客人行情預期，不是已成交價。"
    - "潘金蓮未在本場即時宣布新拍賣底價。"

  relation_boundary:
    - "紅娘與阿莉婭成功搭檔一場，不自動升格為戀愛／固定女女關係。"
```

---

# 14｜白三十二娘：妓籍申請正式啟動

```yaml
SANSHIERNiang_REGISTRATION:
  prior_intent: "已於 HOT V4.4 明示想入妓籍"
  liu12_confirmation:
    - "經一夜後仍明示決定不變。"
    - "知道妓籍一旦官府登記完成即終身不可回良家。"

  process:
    status: "APPLICATION_STARTED_NOT_YET_REGISTERED"
    handler: "春梅"
    collected_information:
      - "姓名／年歲／原籍／現奴籍歸屬／主人／現住處等行政資料。"
    ownership_confirmation:
      - "奴籍仍屬白御行。"
      - "春梅表示官面流程可能需白御行補主人確認；白御行已明示讓她去找春梅處理，原則上同意其自主申請。"
    expected_timing:
      - "春梅判斷若資料齊全，行政流程數日內可完成；未固定精確日期。"

  legal_state_now:
    - "目前仍是申請中，不得提前寫成已入妓籍。"

OTHER_FOUR_GUARDS_REGISTRY:
  bai_hongling: "仍在考慮／未申請"
  bai_mingfan: "目前不要"
  bai_xi: "目前不要"
```

---

# 15｜四大金剛第二夜：女客身份與男人用途重新釐清

```yaml
FOUR_GUARDS_LIU12:
  daytime_discussion:
    key_correction_from_bai:
      - "白御行要她們在青樓挑男人，不是叫她們在青樓找真愛／選丈夫。"
      - "觀止內可挑的是自己看得順眼、守規矩、能滿足性需求的成年男人。"
      - "真正長期感情／婚姻若日後發生，另行計算，不以青樓場合預設。"
      - "男女都不應把青樓交易、幾次陪伴或性關係預設成真愛。"

  tonight_guest_decisions:
    bai_hongling:
      attends_as_guest: true
      purpose:
        - "以普通女客身分進大堂，若遇到她自己看得順眼、守規矩且有性吸引力的男人，可自行決定是否往下發展。"
    bai_sanshierniang:
      attends_as_guest: true
      purpose:
        - "同上；即使妓籍申請中，今晚仍按尚未正式登記之普通女客身分活動，不掛牌、不向男人收接客錢。"
    bai_mingfan:
      attends_as_guest: false
      reason:
        - "本人今晚沒有性需求到需要特地挑男人。"
    bai_xi:
      attends_as_guest: false
      reason:
        - "本人今晚不想。"

  tonight_observed:
    - "紅伶、三十二娘打扮後以女客身分進場。"
    - "白御行匿名坐在後方普通席，曾向附近男客煽風點火，鼓勵有興趣者主動去搭話。"
    - "之後有多名男人開始前往二女桌邊搭話／敬酒。"
    - "二女保有自行拒絕、留人、比較與選擇之權。"

  unknown:
    - "二女最後各自選了誰。"
    - "是否有人被她們帶走。"
    - "是否發生私人成人事件。"
    - "不得因多名男人搭話推成二女已接客或已性交。"

  future_household_activity:
    - "四人均同意之後可跟李師師、李瓶兒、浮香、張麗華一起去替白家採購家具／公共生活用品。"
```

---

# 16｜榴月十二日晚：白玉池正式公開代言／會員首夜

```yaml
WHITE_JADE_LIU12_NIGHT:
  yang_endorsement:
    previous_state: "HOT V4.4 時仍待楊玉環本人同意"
    current_state: "CONSENTED_AND_PUBLICLY_EXECUTED"
    confirmed:
      - "楊玉環明示自己確實喜歡白玉池。"
      - "她同意『楊貴妃第一指名』作宣傳。"
      - "她拒絕把原本就能白天免費使用白玉池當成代言費，要求代言費另與潘金蓮談。"
      - "實際代言費數額本輪未公開／未固定。"
      - "榴月十二日晚楊玉環本人在大堂公開表示：觀止未開門這些天，她確實差不多天天去白玉池。"
      - "她本人補充喜歡之處包括地方大、水熱、安靜等使用感受。"

  public_signage:
    - "『楊貴妃第一指名』已正式掛出，不再是待同意候選。"
    - "白玉池規則牌公開：夜間四席、每席一時辰、每次兩名成年客人、需預約、不可轉讓、觀止不提供搭伴。"

  membership_deposit:
    amount: "50兩"
    role: "資格／預約押金，不等於單次使用費"
    per_use_fee: "EXISTS_BUT_EXACT_AMOUNT_STILL_NOT_RECORDED"

  first_night_registration_observed:
    - "至少一名四十來歲布商模樣男客交出五十兩押金並表示另一位是其夫人。"
    - "另有兩名年輕男客以兩人成組方式登記。"
    - "本輪沒有固定他們最終取得哪一時辰，也沒有觀察到實際入池完成。"

  still_unknown:
    - "榴月十二日晚四個外部時段最終完整名單。"
    - "每次實際使用費。"
    - "當晚是否已有第一組實際下池完成。"
```

---

# 17｜白御行匿名普通席：「黑公子」

```yaml
BAI_HEIGONGZI_LIU12:
  intent:
    - "白御行今晚刻意不進包廂，改坐觀止最外圍一兩銀子普通席。"
    - "不帶四大金剛，觀察普通男客眼中的觀止與私下聊天。"

  alias:
    name: "黑公子"
    origin:
      - "白御行以自己衣著主色為黑，臨場給新客姑娘小桃之假稱。"

  knowledge_visibility:
    ordinary_guests:
      - "周圍普通男客未被告知黑公子就是白御行。"
    chunmei:
      - "春梅明顯認得白御行，並配合未揭破。"
    xiaotao:
      - "截至本 HOT，小桃仍不知道黑公子就是白御行。"
      - "她知道黑公子能使用定陶商會票／與商會有某種關聯，但白御行只說自己『在商會有存款』。"
      - "白御行還叫她若不信可以去問白爺；她尚未完成這個查證。"

  male_crowd_intervention:
    - "白御行曾在普通男客桌邊煽動：紅伶／三十二娘作為女客來青樓可能就是想找男人，若有興趣應主動上前。"
    - "此煽動確實提高附近男人上前搭話之數量，但沒有替二女選人或替她們答應。"
```

---

# 18｜小桃：新來觀止姑娘之單線狀態

```yaml
XIAOTAO_ROUTE_PROFILE:
  source: "本輪新出場／只成立於白御行線"
  baseline_writeback: "NO"

  self_identification:
    name: "小桃"
    state:
      - "本人稱剛來觀止沒多久。"
      - "穿掛牌姑娘之服色／以觀止姑娘身分在大堂接觸客人。"

  virginity_and_debut:
    self_report:
      - "本人明示目前仍為處子。"
      - "本人表示潘金蓮仍打算養她日後的出閣／第一次拍賣行情。"
    verification_scope:
      - "本輪沒有由潘金蓮親自核帳確認其處女標的；目前按小桃本人自述保存。"

  brothel_status:
    - "她可主動在大堂評估客人、談酒、談價格。"
    - "其完整妓籍官面文件本輪未專門核對，不得僅由服色補造行政細節。"

  personality_observed_this_night:
    - "願意先看客人是否有趣，不只看座位價位。"
    - "敢直接開價、談不攏就離開；也能把服務內容、價格、預付分開算。"
    - "尚屬新人，成人服務技巧被白御行評價為第一次已足夠，但仍有進步空間。"
```

---

# 19｜黑公子 × 小桃：酒、五百兩撤銷、100兩新交易

```yaml
HEIGONGZI_XIAOTAO_TRANSACTION:
  first_contact:
    - "小桃把白御行當成坐一兩外圍席的新客，主動問能否坐。"
    - "白御行請她喝一小壺梅子酒。"
    - "雙方以『黑公子』『小桃』互稱。"

  initial_private_negotiation:
    topic:
      - "白御行私下提出不買她保留給出閣拍賣的處女第一次，而詢問另一種成人第一次是否可交易。"
    xiaotao_opening_price: "50兩"
    bai_counteroffer: "500兩"

  room:
    - "白御行叫春梅開一間普通客房。"
    - "小桃挽白御行手臂進房；春梅沒有揭穿其身分。"

  500_tael_phase:
    payment:
      - "白御行曾拿出定陶商會500兩票直接交給小桃。"
      - "小桃曾收下，原方案一度口頭成立。"
    renegotiation:
      - "在原方案真正履行前，雙方改談另一項成人服務。"
      - "小桃把原500兩票退回白御行。"
      - "原500兩方案取消，未履行，不得記成小桃已賺500兩或原成人第一次已消耗。"

  final_current_deal:
    total_cash_or_value_transferred_now: "100兩"
    split:
      tonight_service: "50兩"
      next_time_prepaid: "50兩"
    next_time_status: "PREPAID_NOT_YET_FULFILLED"
    scope:
      - "今晚改成一項明確成人口部服務。"
      - "原500兩談判之其他內容不再包含於本次成交。"
```

---

# 20｜小桃今晚成人事件：完成狀態

```yaml
XIAOTAO_ADULT_EVENT_LIU12:
  participants:
    - "白御行"
    - "小桃"

  consent_and_payment:
    - "雙方在進一步事件前重新談清今晚50兩項目，另50兩為下一次預付。"
    - "小桃本人接受最終價格與項目。"

  event:
    status: "COMPLETED"
    hard_fact:
      - "小桃完成今晚談定之成人口部服務。"
      - "白御行在事件後明示評價：以第一次做這項服務而言，水準足夠／不錯。"
    rendering:
      - "SAVE 不保存逐步性技巧與器官細節。"

  skill_feedback:
    - "白御行對小桃提出後續技巧改進方向；小桃接受自己仍可學習，並表示下一次會更進步。"
    - "具體成人技巧只屬私房經驗，不自動轉成跨線人物能力基線。"

  transaction_result:
    tonight_50: "EARNED_AND_COMPLETED"
    next_50: "HELD_AS_PREPAYMENT"
```

---

# 21｜小桃同宿：不是50兩包夜

```yaml
XIAOTAO_OVERNIGHT:
  bai_request:
    - "白御行希望小桃今晚留下陪睡到早上。"

  xiaotao_response:
    - "小桃明確指出今晚50兩只包含已談妥並完成之服務，並不等於50兩包夜。"
    - "她另外自願決定今晚可以留下陪白御行睡到早上。"
    - "她強調這不是50兩價格內包含的義務。"

  current_state:
    consent_to_stay: true
    paid_as_overnight_service: false
    actual_sleep_until_morning: "NOT_YET_COMPLETED_AT_SAVE_POINT"

  accounting:
    - "不得對外寫成『黑公子50兩包小桃一整夜』。"
    - "今晚已實收之成人服務50兩與下一次預付50兩仍各自分軸。"
```

---

# 22｜人物知情矩陣：小桃／黑公子

```yaml
KNOWLEDGE_MATRIX_XIAOTAO:
  xiaotao_knows:
    - "黑公子能拿出定陶商會大額票據／資金。"
    - "黑公子自稱只是在定陶商會有存款。"
    - "黑公子叫她若不信可去問白爺。"
    - "黑公子今晚在一兩外圍席。"

  xiaotao_does_not_know_confirmed:
    - "黑公子就是白御行。"
    - "黑公子就是定陶商會會長。"

  chunmei_knows:
    - "春梅認得白御行，配合開房且未揭穿。"

  ordinary_guests:
    - "附近普通男客只知道『黑公子』成功帶一名姑娘進房，不知其真實身分。"
```

---

# 23｜今夜仍然 OPEN／UNKNOWN

```yaml
OPEN_THREADS_V4_5:
  four_guards:
    - "紅伶、三十二娘今晚最後各自與哪個男人繼續。"
    - "是否帶男人離席／進房／發生私人成人事件。"

  sanshierniang_registry:
    - "主人確認是否已完成紙面程序。"
    - "官府妓籍正式落冊日期。"

  hongling_registry:
    - "仍未決定是否正式申請。"

  rope_master:
    - "牙行是否找到符合條件之高手。"

  new_hongniang_devices:
    - "木馬、手搖機關、三角架、枷鎖舞台是否真正製作。"
    - "任何製作完成／測試／演出都尚未成立。"

  bai_pan_challenge:
    - "正式日期／場地／結果。"

  aliya:
    - "雙人場後其出閣拍賣價格是否實際調整。"
    - "下一次是否再與紅娘演、是否形成固定搭檔。"

  white_jade:
    - "當夜實際四個預約時段名單與使用結果。"
    - "單次使用費。"
    - "楊玉環代言費最終數額。"

  suqing:
    - "榴月十三日起十八日專案工作的每日進度。"
    - "十八日完成後剩餘八日何時正式開始。"

  white_home:
    - "潘金蓮何時正式宣告／落成空間。"
    - "李師師何時帶隊採買家具。"
    - "最終採購金額。"

  xiaotao:
    - "今晚是否真的睡到早上；本 HOT 停在尚未推進天亮。"
    - "下一次50兩預付何時／是否履行。"
    - "她何時發現黑公子＝白御行。"
    - "她自述處子／出閣拍賣狀態何時由潘金蓮帳面正式確認。"
```

---

# 24｜禁止倒灌與接關提醒

```yaml
DO_NOT_AUTO_RESOLVE:
  - "夜生活人物不得又被默認清晨集體早起；觀止主要作息以中午前後醒來為常態。"
  - "李師師月事晚來 != 已懷孕。"
  - "師師拿到1,000兩 != 家具採購已完成。"
  - "錦棠房子 != 白家妻妾房。"
  - "蘇清中午獨自在東後院客房 != 昨夜整夜獨處。"
  - "蘇清商會18日工作 != 白御行私人18日。"
  - "八套戰鬥服樣品 != 八晚成人行為自動同意。"
  - "紅娘五套玩法目前大多只是提案；不得下輪一開始就假設道具已造好。"
  - "繩工搜尋只對外說高度專業繩工／舞台需求，不外洩成人用途。"
  - "潘金蓮同意一場決勝負 != 已發生。"
  - "阿莉婭已是妓籍；不得再寫成『等待重新掛牌／入妓籍才能成人表演』。"
  - "阿莉婭本晚成人雙人場 != 處女拍賣標的已消失。"
  - "三十二娘正在申請妓籍 != 已正式入籍。"
  - "紅伶、三十二娘被多名男人搭話 != 已挑中／已性交。"
  - "楊玉環已同意並完成公開代言；不得回退成『待同意候選』。"
  - "白玉池有人交押金／登記 != 已實際入池完成。"
  - "黑公子500兩原方案已撤銷並退票；不得記成小桃賺了500兩。"
  - "小桃今晚只實收100兩：50兩為今晚已完成項目，50兩為下一次預付。"
  - "小桃願意留宿 != 50兩包含包夜。"
  - "小桃願意留宿至早上 != 本 HOT 時點已經睡到早上。"
  - "小桃尚未確認黑公子就是白御行；不得讓她無來源突然知道。"
  - "成人場景若 Rendering 受限，只處理 Rendering，不得反向改寫人物／事件；V12 分析器應完成最低必要辨認後退場。"
```

---

# 25｜一句接關摘要

> **理火三年榴月十二日從中午推進到晚間。白御行先與李師師談白家新宅：十年租金八千兩既定，未來需預留僕役與後勤擴充，師師將帶李瓶兒、浮香、張麗華與四大金剛採買家具；白御行先交一千兩作訂金資金，尾款交貨後走定陶商會白御行個人帳。蘇清昨夜只確認在東後院小客房醒來、本人稱碰見過一個人但沒有接觀止安排的客；二十八日私約重新鎖成商會二十日＋私人八日，其中先前選人兩日已扣，榴月十三日起由常煒認領剩十八日，做走秀、戰鬥肚兜／內衣、衛生巾等專案。紅娘新增遊街木馬、手搖成人機關、繩吊、三角束縛台、枷鎖真人搭檔五種候選玩法；牙行先只找高度專業繩工，不外洩成人用途。白御行與潘金蓮另立未定日期的一場決勝負成人私約。妓籍制度由 GM 鎖定：官府一旦登記即終身不可回良家；阿莉婭早已是妓籍，只是商業上仍保留處女一次性拍賣標的。她本人確認昨夜沒有使標的失效，今晚與紅娘正式完成一場雙人成人舞台，包含雙向台上互動與親吻，標的仍保留。三十二娘正式由春梅啟動妓籍申請，尚待官面落冊；紅伶仍未申請，明礬與白希不要。今晚紅伶、三十二娘再以普通女客進大堂，目的可包括自主挑選滿足性需求的男人；白御行匿名坐一兩外圍席，以『黑公子』身分煽動附近男客主動搭話，二女最終是否選人仍未知。白玉池今晚正式掛出『楊貴妃第一指名』，楊玉環本人公開承認歇業期間差不多天天洗並表示喜歡；五十兩押金、雙人、四席、一時辰、預約、不可轉讓等規則正式對外，已有至少一名布商與一組兩名年輕男客登記，但實際入池與單次費仍未知。後段，新來姑娘小桃把白御行當成普通黑衣窮客，二人在梅子酒後私下談價；原本五十兩成人第一次被白御行反喊五百兩、入房後五百兩票曾交付，但在履行前雙方重談，小桃退回五百票，改成今晚五十兩成人口部服務＋下一次預付五十兩。今晚五十兩項目已完成，白御行評價其第一次水準足夠；另五十兩尚未履行。小桃仍不知道黑公子就是白御行。白御行要求她留下睡到早上，小桃明示包夜不包含在五十兩內，但她本人自願留下；本 HOT 停在同宿意向成立、尚未推進至天亮。**
