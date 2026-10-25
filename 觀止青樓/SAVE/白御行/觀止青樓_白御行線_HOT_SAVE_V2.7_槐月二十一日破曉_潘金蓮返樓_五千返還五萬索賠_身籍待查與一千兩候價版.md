# 觀止青樓｜白御行線 HOT SAVE V2.7
## 理火三年槐月二十一日破曉｜潘金蓮返樓 × 五千原款退出 × 五萬個人賠償請求 × 潘金蓮身籍待查 × 一千兩條件式候價版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V2_7_HUAI21_DAWN_PAN_RETURN_5000_RETURN_50000_CLAIM_STATUS_CHECK_1000_INDICATIVE_BID"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V2.7"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime:
    - "GUANZHI_QINGLOU_V10_0"
    - "GUANZHI_QINGLOU_V10_1_V10_2_PATCH_WHEN_APPLICABLE"
  story_time_span:
    start: "理火三年槐月二十一日破曉／HOT V2.6 後"
    current: "理火三年槐月二十一日破曉至清晨前段；精確時刻未定"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AFTER_HOT_SAVE_COMMAND_AT_GUANZHI_FRONT_HALL"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V2.6_槐月二十一日破曉_京師軍械案收網_觀止民事戰重啟_許慎言七十二小時按摩券版.md"
  previous_hot_sha256: "a03ccaa2ad3acb4393acb5c386aeacb454005f737a331c3e57a337a4d35597f0"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"
  current_primary_story_domain:
    - "蘇清 vs 潘金蓮民事／帳務責任"
    - "潘金蓮與李瓶兒西門家身分／文書切割"
    - "觀止掌櫃權與高額交易治理修正"
    - "西門慶／柳生／廣源等核心案之後續"
```

---

# 0｜提交法位、來源與版本說明

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V2.6_槐月二十一日破曉_京師軍械案收網_觀止民事戰重啟_許慎言七十二小時按摩券版.md"
    role: "本檔直接前置 HOT；V2.6 以前有效事件全部繼承"

  legal_core_sources:
    - file: "觀止青樓_白御行線_HOT_SAVE_V2.4_槐月二十日深夜_風滿樓公案與五千後算開冊版.md"
      role: "許慎言代理、五千後算、蘇清／潘金蓮民事爭點、柳生／高衙內、廣源硬來源"
    - file: "觀止青樓_白御行線_HOT_SAVE_V2.5_槐月二十日深夜_開封法網擴張_阿麗婭重定義與六條御息所來訪版.md"
      role: "西門慶接受蘇清一月替代結算、阿麗婭身分重定義等直接來源"

  route_conversation_commit:
    role: "HOT V2.6 後至本次 HOT SAVE 命令前，觀止前堂／後堂已實際演出事件與玩家明示主張"

COMMIT_NOTE:
  - "本檔取代 HOT V2.6，成為白御行線當前直接接關切片；V2.6 保留為前置歷史來源。"
  - "本次只更新 HOT；不更新 MASTER，不修改人物卡／人物池基線。"
  - "本檔只把已演出行動、人物明示、帳面操作、玩家對自身意向及明示歷史主張寫入；未經查證的法律效果與歷史身籍不得偷補。"
  - "五千原款、五萬賠償請求、潘金蓮身籍、一千兩候價四軸分開保存。"
  - "蘇清自由妓女身分方向與阿麗婭首次出閣／第一個男人選擇權嚴格分開，不得互相代換。"
  - "梁山女性／性資源結構之討論屬當場假說；宋江口信只證明本玩家線中宋江所作回應，不證明梁山全寨實態。"
```

---

# 1｜當前場景與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年槐月二十一日"
  time: "破曉至清晨前段；精確時刻未知"
  primary_location: "觀止青樓／前堂；後堂按摩間並行"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  player:
    name: "白御行"
    current_position: "觀止前堂"
    last_confirmed_utterance_before_save:
      - "白御行明示：待潘金蓮合法身分處理完成，且潘金蓮本人真決定重新掛牌拍賣肉體時，願以一千兩／一夜作首輪捧場意向價。"
    no_new_player_action_after_save_command: true

  confirmed_present_or_immediately_active:
    front_hall:
      - "白御行"
      - "潘金蓮"
      - "蘇清"
      - "龐春梅"
      - "李瓶兒"
      - "沈萬三"
      - "紅娘氏"
    back_room:
      - "許慎言／仍在青禾第一段一個時辰按摩服務中；期間曾坐起參與法律討論，服務尚未明示完成"
      - "青禾／持續執行按摩"
    exact_position_not_required:
      - "十三娘、趙受益、李師師、張麗華等仍屬觀止活動人物；本段未形成其新硬事件"

  offsite:
    西門慶:
      current: "開封府刑事／合作程序中"
    包拯:
      current: "開封府主持刑名與證據程序"
    宋江:
      current: "不在觀止；本輪只由梁山口信／傳話回覆白御行詢價"

  direct_resume_point:
    - "潘金蓮已由開封府查問線實際返回觀止；目前不是被關押在觀止，也未被宣判刑事責任。"
    - "蘇清對潘金蓮的民事／帳務戰已從抽象討論進入具體本金、賠償與身分治理。"
    - "五千原掛牌款已在觀止內部被重新分類為待返還／司法保全款；尚未演出實銀完成交付開封府。"
    - "蘇清／許慎言準備以五萬兩作潘金蓮個人賠償之起始請求；潘金蓮未認責，官府亦未判。"
    - "潘金蓮現行是否具自由良籍／奴籍／妾室及可公開從妓資格尚未查清；優先查官冊、身契與過往改籍。"
    - "白御行一千兩／一夜只為潘金蓮未來合法重新掛牌後之條件式意向價；目前不成交、不付款、不預約、不形成性同意。"
```

---

# 2｜PAN21-E01｜潘金蓮由開封府返回觀止

```yaml
EVENT_RECORD:
  event_id: "PAN21-E01-PAN_RETURNS_FROM_KAIFENG"
  status: "COMPLETED_RETURN"
  location: "觀止前堂"
  actor: "潘金蓮"

CONFIRMED:
  - "潘金蓮實際自開封府查問線返回觀止前堂。"
  - "其自述不是被『釋放出獄』；開封府先完成本輪需問事項，之後有傳即到。"
  - "潘金蓮回觀止後重新以掌櫃／當事人身分參與蘇清民事帳務戰。"

NOT_ESTABLISHED:
  - "潘金蓮獲刑事無罪判決"
  - "潘金蓮對蘇清民事無責"
  - "潘金蓮永久免受開封府傳喚"
  - "潘金蓮已恢復或取得妓籍"
```

---

# 3｜SU-PAN21-E01｜蘇清對潘金蓮民事案之三大爭點

```yaml
CIVIL_CASE_FRAME:
  status: "ACTIVE"
  plaintiff_side:
    principal: "蘇清"
    representative_lawyer: "許慎言"
  defendant_side:
    principal: "潘金蓮"
    counsel: "NOT_YET_RETAINED"

  current_major_issues:
    - id: "AUTHORITY_TO_SUBSTITUTE"
      question: "潘金蓮當時是否有權把『蘇清一月』作為西門慶五千掛牌交易之替代結算。"
    - id: "BENEFIT_AND_LOSS"
      question: "西門慶實際取得蘇清二十八日控制／利益後，觀止、西門慶、潘金蓮與蘇清各自取得或承受什麼財產利益與損害。"
    - id: "POST_KNOWLEDGE_USE"
      question: "潘金蓮何時知道蘇清在西門府實際遭遇；若其後仍把蘇清二十八日作為有效結算，其知情後責任如何。"

  pan_response:
    - "潘金蓮未認輸，明示自己可另請狀師應訴。"
    - "潘金蓮接受查帳與訴訟攻防，不等於承認暴力、共犯或全部賠償。"
```

---

# 4｜FIVE-THOUSAND21-E01｜五千原款之觀止帳務處理

```yaml
FIVE_THOUSAND_ORIGINAL_PAYMENT:
  amount_taels: 5000
  source_transaction: "阿麗婭五千掛牌／後續以蘇清一月替代結算之舊案"
  receipt_status_in_current_scene:
    - "觀止舊帳被翻出後，前堂以既有帳冊確認五千為曾實際進入觀止帳房之款項。"

  current_guanzhi_internal_position:
    - "白御行主張：阿麗婭未交付、蘇清替代又引發重大責任，觀止無正當理由永久保有原五千。"
    - "許慎言認為五千原款應與蘇清損害賠償分軸；觀止首先處理原款退出。"
    - "春梅／李瓶兒在帳上將此筆重新標為待返還／司法保全款。"

  current_status: "RECLASSIFIED_PENDING_RETURN_OR_JUDICIAL_ESCROW"
  actual_cash_transfer_to_kaifeng_completed: false
  final_recipient: "UNDECIDED_BY_KAIFENG_OR_LAW"

  prohibited_conclusions:
    - "不得寫成五千已直接退到西門慶手中。"
    - "不得寫成五千即蘇清賠償。"
    - "不得寫成觀止已完成全部返還程序。"
```

---

# 5｜TENFOLD21-E01｜『假一賠十』與五萬賠償請求

```yaml
TENFOLD_COMPENSATION_CLAIM:
  status: "PLAINTIFF_CLAIM_DIRECTION_NOT_JUDGMENT"
  base_number_used_in_argument: 5000
  requested_multiplier: 10
  requested_amount_taels: 50000

  origin:
    - "白御行以商家信用『假一賠十』提出十倍賠償構想。"
    - "白御行認為潘金蓮原交易對西門慶形成錯誤／替代交付，而西門慶對蘇清造成的實際傷害由蘇清承受，因此十倍賠償利益有理由回到蘇清。"
    - "蘇清明示自己要主張十倍；其理由之一是若只退五千，潘金蓮／觀止僅恢復原狀，而蘇清二十八日實害沒有被賠。"

  shen_wansan_analysis:
    - "沈萬三認為『假一賠十』原屬交易信用結構；不能把蘇清本人當成假貨。"
    - "可轉化檢查的是錯誤／無權替代交易所生賠償利益與實際受害者間之歸屬。"
    - "若西門慶一邊實際取得蘇清利益，一邊又主張自己只是拿到假貨之單純受害者，需拆解其實際利益與損失。"

  xu_shenyan_position:
    - "許慎言願意把五萬作為訴訟起始請求方向，但必須找到可成立之法律／交易結構，不能只寫『白會長想讓潘金蓮枯死』。"
    - "五萬目前只是請求額；許慎言明示不是已判。"

  pan_jinlian_position:
    - "潘金蓮未承認十倍賠償成立。"
    - "潘金蓮提出抗辯方向：要先證明她當年究竟承諾賣的是阿麗婭本人、初夜、優先預定、掛牌資格或其他權利。"

  final_judgment: "UNDECIDED"
```

---

# 6｜PAN-PERSONAL21-E01｜潘金蓮個人責任與觀止公帳分離

```yaml
PUBLIC_PRIVATE_LIABILITY_SEPARATION:
  trigger:
    - "白御行明示：若十倍等賠償屬潘金蓮本人錯誤行為之責任，不得由觀止公帳替她付款。"

  accepted_operational_principle:
    guanzhi:
      - "五千原款之返還／司法保全屬觀止舊交易帳務軸。"
    pan_jinlian_personal:
      - "若法院／有效程序最後判定潘金蓮個人負損害賠償責任，應由潘金蓮個人財產／個人收入承擔。"
      - "不得把姑娘收入、技師收入、其他掌櫃份額或觀止公帳當成其個人賠償池。"

  pan_acceptance_scope:
    - "潘金蓮接受公私分帳原則。"
    - "潘金蓮沒有因此承認五萬或任何具體賠償數額。"

  xu_case_drafting:
    - "許慎言準備將潘金蓮個人責任與觀止五千原款證明／返還軸分開書寫。"
```

---

# 7｜SU-QING21-E02｜蘇清要的是『自由妓女』身分

```yaml
SU_QING_STATUS_DIRECTION:
  current_desired_status:
    - "保留妓女／風月職業身份。"
    - "解除被觀止、掌櫃或其他人作為可轉讓／可抵帳人身資源之位置。"
    - "由蘇清本人決定接誰、拒誰、價格、是否服務、何時離開。"
    - "仍願在觀止工作，依法／依樓規支付抽成、房錢、堂費與其他合理成本。"

  explicit_non_goal:
    - "不是要求被洗回良家身份。"
    - "不是要求離開觀止。"
    - "不是要求免除所有觀止營業規矩。"

  relation_to_civil_case:
    - "蘇清對潘金蓮之訴，核心之一是禁止掌櫃再以她本人作他人交易之替代交付／抵帳。"
```

---

# 8｜AALIYAH21-LOCK｜阿麗婭與蘇清不得混線

```yaml
AALIYAH_CURRENT_LOCK:
  inherited_hard_state:
    - "阿麗婭舊五千掛牌／出閣程序沒有完成為一個有效的首次性服務交付。"
    - "阿麗婭目前沒有因五千舊案自動重新掛牌。"

  current_story_direction:
    - "阿麗婭要保留自己選擇第一個男人／首次真正出閣對象的機會。"

  separation_from_su_qing:
    - "蘇清：已選擇妓女職業，追求自由身與自主營業。"
    - "阿麗婭：首次出閣尚未完成，重點是第一個男人由她自己選。"
    - "兩者不得以『都是自由』為由合併成同一身分方案。"
```

---

# 9｜GUANZHI-GOV21-E01｜潘金蓮定價權與高額交易治理修正

```yaml
GUANZHI_HIGH_VALUE_TRANSACTION_GOVERNANCE:
  trigger:
    - "白御行指出潘金蓮過去收費與交易權過度集中，客人與姑娘都可能因過度榨價／人身抵帳反彈；目的不是罷免潘金蓮，而是要求其反省並改進。"

  pan_jinlian_position:
    - "潘金蓮接受自己仍可當掌櫃，但承認特殊高額交易需要額外規則。"

  current_operational_rule:
    normal_operations:
      - "正常酒菜、房錢、普通席與一般營業價格，潘金蓮仍保留日常掌櫃定價／經營權。"
    special_high_value_or_personhood_transactions:
      examples:
        - "長期服務"
        - "包月"
        - "首次出閣"
        - "身分／掛牌變更"
        - "轉契／人身相關契約"
        - "其他高額且可能改變姑娘長期位置之安排"
      requirements:
        - "至少另有一名掌櫃複核；目前春梅或李瓶兒可擔任複核。"
        - "涉及姑娘本人長期服務／身體／身分者，姑娘本人必須明示同意／簽認。"
        - "不得由潘金蓮一人把人、價格、交付與帳務一路單獨定到底。"

  governance_effect:
    - "潘金蓮未被解除掌櫃。"
    - "李瓶兒與春梅既有掌櫃職權被再次確認。"
    - "觀止高額人身／長約交易新增第二掌櫃複核與本人確認機制。"
```

---

# 10｜PAN-LISTING21-E01｜潘金蓮重新掛牌之未成立交易

```yaml
PAN_RELISTING_DISCUSSION:
  current_status: "NOT_CURRENTLY_LISTED_FOR_PUBLIC_SEX_WORK_IN_THIS_ROUTE_EVENT"

  sequence:
    - "白御行曾先提出五百兩拍潘金蓮『復出第一個月』之意向，後撤回；沒有成交。"
    - "其後白御行提出一千兩／一夜，想以潘金蓮床上能力作為對其帶領觀止能力的一部分觀察；前堂一度討論成交條款。"
    - "隨後白御行指出潘金蓮目前只是觀止掌櫃，且西門家／妓籍法位尚未處理，不能直接公開掛牌賣淫。"
    - "許慎言同意必須先釐清潘金蓮現行法律身分與從妓資格；先前一千兩不得記正式成交。"

  final_current_offer:
    offered_by: "白御行"
    amount_taels: 1000
    unit: "一夜"
    condition:
      - "潘金蓮先完成合法身分處理。"
      - "潘金蓮本人之後真決定重新掛牌／公開拍賣性服務。"
    nature: "CONDITIONAL_INDICATIVE_BID_ONLY"
    paid: false
    reserved: false
    sexual_consent_created: false
    priority_right_created: false

  pan_response:
    - "潘金蓮接受把一千兩記作未來合法重新掛牌後的首輪意向價／候價。"
    - "潘金蓮明示若真的拍賣，其他人可競價；一千兩不保證白御行得標。"
    - "潘金蓮明示要先查清自己是否真正屬於自己，再決定是否重新掛牌、賣什麼、賣多少。"
```

---

# 11｜LI-PINGER21-E01｜李瓶兒西門家身分與嫁妝軸

```yaml
LI_PINGER_STATUS_LINE:
  inherited_route_hard_state:
    - "李瓶兒現行玩家線仍未完成與西門慶之正式法律切割。"

  player_provided_historical_correction:
    source: "白御行本輪明示保證"
    claim:
      - "李瓶兒當年是改嫁入西門府。"
      - "李瓶兒帶嫁妝進府。"
      - "不是以奴籍被西門慶購買後收為妾。"
    current_save_treatment: "PLAYER_PROVIDED_HIGH_WEIGHT_HISTORICAL_CORRECTION; DOCUMENT_CHECK_STILL_USEFUL"

  legal_direction_discussed:
    - "李瓶兒之核心問題優先視為妾室／改嫁關係如何合法解除，而非潘金蓮式奴籍／身契來源案。"
    - "若其帶嫁妝改嫁之校正成立，後續還應查嫁妝與其個人財產如何退出西門府。"
    - "李瓶兒沒有因本輪討論表示自己要重新掛牌從妓。"

  anti_merge:
    - "不得把李瓶兒與潘金蓮都簡化成『西門慶可以賣的妾』。"
```

---

# 12｜PAN-STATUS21-E01｜潘金蓮身籍／身契來源案啟動

```yaml
PAN_JINLIAN_STATUS_CASE:
  status: "ACTIVE_DOCUMENT_AND_REGISTRY_INQUIRY"
  current_legal_identity: "UNRESOLVED"

  player_provided_historical_claims:
    source: "白御行在故事中提供之歷史資訊／推論"
    claims:
      - "潘金蓮早年曾為奴婢／奴籍。"
      - "其因與原主人發生曖昧／勾引老爺，被主母處置後進入武大郎家。"
      - "武大郎死後只有弟弟武松作近親；白御行因此提出若身契仍存，武松可能涉及承繼。"
    legal_status: "HISTORICAL_CLAIMS_AND_HYPOTHESIS_NOT_YET_PROVEN_BY_CURRENT_GUANZHI_DOCUMENTS"

  key_counter_hypothesis:
    - "白御行亦主動提出：武大郎可能因愛或其他原因，曾替潘金蓮辦理放良／改籍；若曾正式脫籍，後續『身契由武松繼承』整條推論可能失效。"

  xu_shenyan_inquiry_order:
    - "先查潘金蓮現在官冊究竟登記為良、奴、妾或其他法位。"
    - "追查其由原主人家進入武大郎家時，有無放良／改籍／嫁娶／身契轉讓文書。"
    - "查武大郎生前是否另辦脫籍。"
    - "只有在奴籍／身契從未解除前提成立後，才查武大死亡時身契是否進入遺產。"
    - "再查武松是否為唯一合法承繼人、是否實際承受相關權利。"
    - "最後才處理潘金蓮後續自行進西門府是否存在權利來源瑕疵。"

  prohibited_conclusions:
    - "不得現在就寫潘金蓮仍是奴籍。"
    - "不得現在就寫武松是潘金蓮主人。"
    - "不得把潘金蓮本人等同普通物件；法律爭的是身契／身分權利效力。"
    - "不得因潘金蓮自願跟西門慶，就自動證成所有舊身契已合法移轉。"
```

---

# 13｜WANGPO21-E01｜西門慶付款給王婆之線索

```yaml
WANG_PO_PAYMENT_CLUE:
  source: "白御行本輪明示提供"
  current_status: "PLAYER_PROVIDED_HISTORICAL_CLUE_PENDING_DOCUMENT_OR_WITNESS_VERIFICATION"

  confirmed_as_player_claim:
    - "西門慶當年曾把一筆與潘金蓮往來相關的錢付給王婆。"
    - "王婆是西門慶與潘金蓮之間的牽線／皮條中間人。"

  unknown:
    - "王婆收款究竟是媒錢、跑腿錢、封口錢、買契價銀或其他性質。"
    - "王婆是否持有潘金蓮身契或受真正持契人授權。"
    - "王婆是否將部分銀錢轉交潘金蓮。"
    - "即使潘金蓮曾收錢，該錢是否為身價、贈銀、媒介分成或其他性質。"

  shen_xu_analysis:
    - "錢流本身不足以證明買身；真正關鍵是王婆憑什麼收錢、取得／轉交了什麼權利。"
```

---

# 14｜LIANGSHAN21-E01｜梁山性需求／女性身分討論之法位

```yaml
LIANGSHAN_GENDER_AND_SEXUAL_STRUCTURE_DISCUSSION:
  status: "IN_SCENE_HYPOTHESIS_DISCUSSION_ONLY"

  white_yuxing_hypotheses:
    - "梁山作為軍事組織，性需求可能像軍隊一樣被推到核心軍事空間之外。"
    - "賊軍未必像合法官軍有完整軍紀／外圍市場制度，因此部分女性可能缺乏身體自主權。"
    - "『壓寨夫人』可能在部分案例中只是好聽稱號，實際女性位置可能從屬於頭領／寨權。"
    - "梁山可能存在非貨幣化的性／身體服務；沒有青樓不等於沒有性供給。"

  shen_wansan_and_su_qing_distinction:
    - "非貨幣結算不等於沒有交換；可能嵌在食宿、庇護、依附、家眷、戰利品與權力中。"
    - "最黑的結構不是『免費妓院』，而是女性根本沒有被承認為需要本人同意／結帳的獨立交易主體。"

  objective_world_fact: false
  prohibition:
    - "不得在下一輪直接把梁山全寨寫成系統性強迫女性之確定事實。"
    - "不得把『梁山都是 GAY』笑談升格為人物性向設定。"
```

---

# 15｜SONGJIANG21-E01｜五萬兩＋潘金蓮『押寨夫人』詢價口信

```yaml
SONG_JIANG_INQUIRY:
  status: "COMPLETED_ROUTE_MESSAGE_EXCHANGE"
  initiator: "白御行"
  proposal_as_sent:
    - "白御行提出以五萬兩為條件，詢問宋江／梁山是否收潘金蓮去作『押寨夫人』。"
  consent_boundary_in_message:
    - "春梅於觀止一側明記：此為白御行詢價，不代表潘金蓮同意被出售、婚配或上梁山。"

  song_jiang_reply_as_received:
    - "宋江先問五萬兩究竟是白御行給梁山，還是梁山給白御行。"
    - "得知是白御行出五萬後，宋江表示五萬資助梁山自可感激。"
    - "宋江明問潘金蓮本人願不願意。"
    - "宋江另問武松是否知道。"
    - "宋江表示梁山不是人市；若潘金蓮自己願意上山，其作客、家眷或其他位置可以另談；若她不願，五十萬也不能作為把她賣給梁山的理由。"
    - "宋江另以玩笑／回應指出，若潘金蓮真肯上山，不必由白御行替她指定男人，山上未娶好漢很多。"
    - "宋江反問白御行為何願意倒貼五萬只為把潘金蓮送走。"

  authority_boundary:
    - "此為本玩家線收到之宋江口信；證明宋江當場表態，不自動證明梁山所有頭領／歷史所有事件皆依此原則。"
```

---

# 16｜PAN-RETAIN21-E01｜『送走潘金蓮、扶李瓶兒』長期利益討論

```yaml
MANAGEMENT_SUCCESSION_DISCUSSION:
  white_yuxing_view:
    - "白御行一度認為：若倒貼五萬把潘金蓮送去梁山，再扶植李瓶兒當掌櫃，長期可能收穫更多。"

  shen_wansan_counteranalysis:
    - "五萬給梁山不代表潘金蓮附送；最壞結果可能是五萬捐掉、潘金蓮仍留觀止。"
    - "李瓶兒是否擴大掌櫃權應由李瓶兒本人決定。"
    - "潘金蓮的經營能力可以保留，其錯誤責任由本人承擔；沒必要用五萬換掉整個人。"

  li_pinger_position:
    - "李瓶兒明示：不必先把潘金蓮送走，她才有資格多管觀止。"
    - "若未來需要她多承擔掌櫃職責，可以談，但不是因為潘金蓮被賣掉。"
    - "李瓶兒明示若潘金蓮再拿姑娘去抵帳，她會第一個主張收回潘金蓮相關帳權。"

  current_management_result:
    - "潘金蓮留任掌櫃。"
    - "李瓶兒與春梅掌櫃職能持續。"
    - "沒有形成潘金蓮離樓／梁山轉移／李瓶兒唯一接班之決定。"
```

---

# 17｜XU-QINGHE21-E01｜許慎言與青禾按摩服務持續

```yaml
XU_SHENYAN_MASSAGE_CURRENT:
  inherited_credit:
    - "白御行已正式贈許慎言七十二小時分次按摩體驗額度。"
  current_session:
    planned_first_session: "一個時辰"
    current_status: "ONGOING_OR_NOT_EXPLICITLY_COMPLETED"
    provider: "青禾"
    recipient: "許慎言"
    observed:
      - "許慎言在按摩期間持續隔珠簾參與蘇清／潘金蓮法律討論。"
      - "在潘金蓮身籍議題變複雜時，許慎言曾坐起來拆解法律問題；青禾提醒服務尚有時間。"
  relationship_boundary:
    - "不建立感情、性、陪宿、戀愛或私人所有權。"
```

---

# 18｜關係與責任硬狀態

```yaml
RELATION_AND_RESPONSIBILITY_STATE:
  pan_jinlian_vs_su_qing:
    status: "ACTIVE_CIVIL_ADVERSARIES_WITH_SHARED_GUANZHI_WORKPLACE"
    confirmed:
      - "蘇清仍希望留在觀止工作。"
      - "蘇清主張的是潘金蓮個人及相關交易責任，不是要摧毀觀止。"
      - "潘金蓮願意應訴、查帳並保留抗辯。"
      - "兩人仍可互相譏諷、交易式拆招；不得因此寫成和解或仇恨永久化。"

  pan_jinlian_vs_guanzhi:
    - "潘金蓮仍是掌櫃。"
    - "潘金蓮高額人身／長約交易權受到第二掌櫃複核限制。"
    - "潘金蓮若有個人賠償，不得由觀止公帳代償。"

  bai_yuxing_vs_pan_jinlian:
    - "白御行反覆以高價掛牌、梁山、五萬賠償等話題調侃／施壓潘金蓮。"
    - "目前不存在白御行與潘金蓮已成交的一夜性交易。"
    - "目前只有潘金蓮未來合法重新掛牌後的一千兩／夜條件式意向價。"

  li_pinger_vs_pan_jinlian:
    - "李瓶兒支持潘金蓮繼續作掌櫃，但支持拆分其過度集中之高額交易權。"
    - "李瓶兒沒有接受『潘金蓮離開＝自己接班』的自動安排。"
```

---

# 19｜本 HOT 必須保留的 UNKNOWN／UNDECIDED

```yaml
OPEN_QUESTIONS:
  su_pan_civil:
    - "五萬十倍賠償是否有可成立法律基礎。"
    - "潘金蓮當年究竟承諾了什麼交易標的／權利。"
    - "潘金蓮何時知道蘇清實際受暴力控制與二十八日遭遇。"
    - "潘金蓮知情後是否仍利用蘇清二十八日作有效五千結算。"
    - "蘇清可得多少返還、收益、損害或其他救濟。"

  five_thousand:
    - "五千待返還／司法保全款最後交付給誰、如何扣押、是否與西門慶其他財產程序合併。"
    - "實際將五千從觀止移交開封府之事件尚未演出。"

  pan_status:
    - "潘金蓮由原主家進武大家時究竟是放良嫁人、身契轉讓、其他處置。"
    - "武大郎是否曾替潘金蓮辦理放良／改籍。"
    - "如奴籍持續，武大死亡時相關身契是否依法進入遺產。"
    - "武松是否為唯一合法承繼人且實際承受身契權利。"
    - "潘金蓮後來進西門府時的正式納妾／身分文書是什麼。"
    - "西門慶給王婆之錢究竟性質為何。"
    - "王婆是否分錢給潘金蓮。"
    - "潘金蓮目前是否有資格重新登記／掛牌為妓女。"

  li_pinger_status:
    - "李瓶兒與西門慶之妾室／婚姻關係如何合法解除。"
    - "李瓶兒嫁妝清單、現存財產與退出西門府之財產處理。"
    - "李瓶兒沒有提出從妓／掛牌決定。"

  core_cases_inherited:
    - "西門慶蘇清二十八日最終刑名與處置。"
    - "廣源母簿／核心帳與商業刑民責任。"
    - "柳生實際所在與西門慶『還要問話』口供線後續。"
    - "高衙內公開施暴命令之外的其他責任。"
```

---

# 20｜禁止回歸／反污染

```yaml
ANTI_REGRESSION:
  - "不得把五萬寫成已判、已欠、已執行；目前只是蘇清／許慎言方之起始請求額。"
  - "不得把五千待返還／司法保全寫成已直接退給西門慶。"
  - "不得把五千返還與蘇清五萬賠償合併成同一筆錢。"
  - "不得把潘金蓮個人賠償從觀止公帳、姑娘收入、技師收入或其他掌櫃份額支付。"
  - "不得把蘇清寫成要恢復良家；她現在要的是自由妓女身分。"
  - "不得把阿麗婭套用蘇清方案；阿麗婭重點是首次出閣未完成、第一個男人自己選。"
  - "不得把潘金蓮目前寫成已重新掛牌妓女。"
  - "不得把白御行一千兩／一夜寫成已成交、已付款、已預約或已取得性服務資格。"
  - "不得把潘金蓮早年奴婢史直接推成其現在仍為奴籍；必須先查放良／改籍與官冊。"
  - "不得把武松寫成潘金蓮確定主人／持契人；目前只是條件式繼承假說。"
  - "不得把王婆收西門慶銀錢寫成已證實買身價。"
  - "不得把李瓶兒與潘金蓮的西門家身分案混在一起；瓶兒目前以改嫁／嫁妝校正線處理。"
  - "不得把宋江口信寫成梁山全寨制度真相。"
  - "不得把梁山女性缺乏身體自主權之討論寫成已查證歷史。"
  - "不得把潘金蓮因治理修正而寫成被罷免；她仍是觀止掌櫃。"
  - "不得把李瓶兒因『可多管一些』寫成已接受唯一掌櫃／取代潘金蓮。"
  - "不得再把許慎言只寫成按摩笑梗；其仍是蘇清主要代理律師與觀止法律援助核心。"
  - "不得把青禾因按摩許慎言自動寫成戀愛／性關係。"
```

---

# 21｜下一幕自然接關

```yaml
NEXT_SCENE:
  primary_options_for_world:
    - "查潘金蓮官籍／身契：由開封府、戶籍、舊主家／武大家相關文書線先回一筆可驗證資料。"
    - "蘇清／潘金蓮民事：繼續查當年五千掛牌真正承諾標的、潘金蓮知情時間與後堂副冊。"
    - "五千原款：由春梅／瓶兒準備移交司法保全所需帳證，但不得偷寫已完成交款。"
    - "許慎言按摩第一時辰若自然結束，可正式回前堂整理五萬請求與潘金蓮抗辯。"

  secondary:
    - "西門慶／柳生／廣源任何一條可由開封府短報重入，但不得再次讓國家大案吞掉觀止主鏡頭。"

  optional_humor_or_relation:
    - "潘金蓮可繼續就一千兩候價、梁山倒貼五萬、自由妓女與掌櫃治理與白御行／蘇清拆招；不得因此提前完成掛牌。"

  no_forced_choice_menu: true
  next_action_owner: "WORLD_OR_PLAYER_AFTER_HOLD_RELEASE"
```

---

# 22｜本 HOT 一句接關摘要

> **槐月二十一日破曉，潘金蓮已自開封府查問線真正回到觀止，蘇清對她的民事／帳務戰正式開打。觀止舊帳確認五千曾實收入帳，現已在樓內重新列作待返還／司法保全款，但尚未實際移交；蘇清與許慎言則以『假一賠十』延伸出五萬兩潘金蓮個人賠償請求，潘金蓮未認責、官府未判，且公私帳已明確拆開。蘇清要的是留在觀止做自由妓女；阿麗婭要的是保住自己選第一個男人的機會，兩線不得混。白御行曾多次拿潘金蓮復出掛牌開價，最後留下的有效狀態只有：待潘金蓮先查清官籍／身契、合法取得公開從妓資格且本人真決定重新掛牌後，白御行願出一千兩／一夜作首輪意向價；目前不成交。潘金蓮早年奴籍、武大是否放良、武松是否可能承繼、西門慶付王婆之錢究竟買到什麼，全部轉入身籍文書調查，不得偷填。潘金蓮仍是觀止掌櫃，但高額長約／人身交易已新增第二掌櫃複核與本人簽認；李瓶兒、春梅之掌櫃權再次確認。故事下一刀應落在潘金蓮官籍／身契實證，或蘇清五萬請求真正能否站住。**
