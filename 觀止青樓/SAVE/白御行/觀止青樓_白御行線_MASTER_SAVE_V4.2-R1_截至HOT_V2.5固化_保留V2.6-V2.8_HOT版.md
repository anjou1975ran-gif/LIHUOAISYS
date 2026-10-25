# 觀止青樓｜白御行線 MASTER SAVE V4.2-R1
## 截至 HOT V2.5 固化整合版｜HOT V2.6–V2.8 保留為有效疊加層

```yaml
SAVE_META:
  save_id: "GUANZHI_BAIYUXING_MASTER_V4_2_R1_CUTOFF_HOT_V2_5"
  title: "觀止青樓｜白御行線 MASTER SAVE"
  version: "V4.2-R1"
  world: "觀止青樓"
  player: "白御行"
  route_status: "ACTIVE"
  record_type: "CONSOLIDATED_MASTER_ARCHIVE"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  document_date: "2026-08-08"
  fixed_calendar_anchor: "理火三年槐月五日｜永恆第一夜"
  master_cutoff: "理火三年槐月二十日深夜｜HOT V2.5"
  last_canonical_master_event: "E83"
  inherited_master: "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"
  inherited_master_sha256: "efb47cfbf79f75244d5a62dcfbe57a855d04535cc9e02a264a57483b60056b85"
  current_route_resume_source: "觀止青樓_白御行線_HOT_SAVE_V2.8_槐月二十一日白日_潘身籍補證_白玉池許願幣定存_師師如夫人確認與晚宴前休息版.md"
  current_route_resume_note: "本 MASTER 固化到 V2.5；V2.6、V2.7、V2.8 均為合法且較新的 HOT，實際接關須再疊加 HOT V2.8。"

  absorbs_into_master:
    - "HOT V2.0"
    - "HOT V2.1"
    - "HOT V2.2"
    - "HOT V2.3"
    - "HOT V2.4"
    - "HOT V2.5"

  retained_as_hot_overlay:
    - "HOT V2.6"
    - "HOT V2.7"
    - "HOT V2.8"

  supersedes_as_master:
    - "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"

  world_runtime_document_profile_current: "GUANZHI_QINGLOU_V11.0-R2"
  character_source_current: "觀止人物卡池_LCAPG_V2.1"
```

# 0｜本次固化決定與「保留一部分」的落地

本版依 GM 明示「**固化到 V2.5，保留一部分**」執行。

```yaml
GM_COMMIT_DECISION:
  solidify_through: "HOT V2.5"
  preserve_newer_hot_chain: true
  preserved_versions:
    - "HOT V2.6"
    - "HOT V2.7"
    - "HOT V2.8"
  interpretation:
    - "V2.0–V2.5 進入 MASTER 長期因果層。"
    - "V2.6–V2.8 不併入本次 MASTER，繼續作為較新的 HOT 疊加層。"
    - "因此本次不是把所有 HOT 吃光，而是在 V2.5 建立新的長期切面。"
```

本版**不刪除**被固化之原 HOT 檔；它們保留作來源追溯與回歸核對，但預設長期載入時由本 MASTER 取代其 V2.0–V2.5 的逐檔載入需求。

---

# 1｜V4.2-R1 法位與讀取順序

```yaml
INTERNAL_PRECEDENCE_V4_2:
  highest_current_sections:
    - "第2區：V2.0–V2.5 固化映射"
    - "第3區：截至 V2.5 MASTER 截止硬狀態"
    - "第4區：截至 V2.5 關係／同意／名分覆寫"
    - "第5區：截至 V2.5 法律／帳務／契約覆寫"
    - "第6區：截至 V2.5 知情／秘密／異常覆寫"
    - "第7區：截至 V2.5 未決事項"
    - "第8區：MASTER 與 HOT V2.6–V2.8 接關規則"
  inherited_master_body:
    role: "E01–E77 與早期長期因果完整繼承"
    conflict_rule: "若 V4.1 內的舊截止快照與本版第2–8區衝突，以本版第2–8區為準。"
  promoted_hot_source_archive:
    role: "V2.0–V2.5 原始 HOT 全文附錄，用於細節追溯"
    current_scene_warning: "附錄內各 HOT 的 CURRENT_SCENE／HOLD 只是歷史快照，不得覆寫本版截止狀態。"
```

## 1.1 固化原則

1. 只固化已發生、可觀察、人物明示、正式文書可見、帳目可核對，或玩家對自身言行的有效校正。
2. 傳聞、人物判斷、官府暫時推論、玩家模型與客觀事實分軸保存。
3. 成人事件、同意、身體反應、感情、契約、付款、名分與公開知情分軸保存。
4. `UNKNOWN`、`UNDECIDED`、`DISPUTED`、`UNDER_OFFICIAL_CLARIFICATION` 均為合法狀態。
5. V2.0–V2.5 之玩家線事件不倒灌人物卡池基線。
6. 後來 V2.6–V2.8 或人物卡池 V2.1 的新狀態，不回溯改寫 V2.5 當時已發生事件的原貌。
7. 本版固化是文件級 SAVE 整合，不宣稱任何宿主底層 Runtime 或模型權重已被修改。

---

# 2｜HOT V2.0–V2.5 固化映射（E78–E83）

```yaml
V4_2_CONSOLIDATION_MANIFEST:
  inherited_events: "E01-E77"
  promoted_macro_events:
    E78: "HOT V2.0｜槐月十七日晚四人成人事件、共同就寢與關係分軸"
    E79: "HOT V2.1｜槐月十八日商戰起局、蘇清二十八日私約、白玉池補固"
    E80: "HOT V2.2｜李師師如夫人前置、七色肚兜、張麗華獨宿夜與破曉"
    E81: "HOT V2.3｜定陶偽鹽／高爐案、沈萬三合作、師師薄情郎席前"
    E82: "HOT V2.4｜風滿樓、公案法位、西門暗櫃、五千後算、蘇清代理"
    E83: "HOT V2.5｜開封法網擴張、阿麗婭重定義、六條御息所來訪"
  event_id_policy:
    - "E78–E83 是 MASTER 的宏事件索引。"
    - "HOT 內原生事件 ID（如 NIGHT17-E06、KFY20-E01）完整保留為 source_alias，不強行改號。"
    - "需要細節時直接查本檔後段的 V2.0–V2.5 固化來源全文。"
```

## E78｜HOT V2.0：四人夜結與兩日關係分軸

```yaml
MASTER_EVENT:
  event_id: "E78"
  source: "HOT V2.0"
  story_time: "槐月十七日晚至槐月十八日清晨"
  status: "SOLIDIFIED"
  confirmed_core:
    - "白御行、張麗華、蘇清、李瓶兒在張麗華房內完成一夜共同成人場與共眠。"
    - "白御行與張麗華、蘇清均有雙方同意之性交；李瓶兒只到有限手部／口部探索，未性交。"
    - "蘇清之停止權在爭議後被重新確認並實際遵守；她不接受體內射精。"
    - "沒有體內射精或懷孕在本夜被確認。"
    - "四人『家人』只屬短期私人框架，不形成永久婚姻、群體伴侶或大小順位。"
    - "張麗華接受本夜多人共處，但要求未來再有多人事件須重新詢問。"
    - "白御行明示當時不愛蘇清，只承認履約與肉體享受；對李瓶兒則明示有真感情。"
```

## E79｜HOT V2.1：定陶商戰、蘇清私約與白玉池補固

```yaml
MASTER_EVENT:
  event_id: "E79"
  source: "HOT V2.1"
  story_time: "槐月十八日下午"
  status: "SOLIDIFIED"
  confirmed_core:
    - "常煒以定陶商會副會長身分與白御行密會，廣源轉運行／許奉年成為可見第一擊目標。"
    - "白御行授權以真實片段、模糊連接與信用壓力形成商戰推斷場；不得把投放消息當客觀犯罪事實。"
    - "沈萬三被列為高能力相關節點但當時未被確證涉案；定陶不先與其全面開戰。"
    - "白御行與蘇清以擊掌成立二十八日私人盟約；其觸發與履行依原 HOT 條件，不自動改成愛情或永久身分。"
    - "白玉池舊案由玩家／GM 補固，既有異常與封池因果不再被導演回退成完全未知。"
    - "張麗華與白御行之私下稱呼於玩家線固化，不倒灌人物基線。"
```

## E80｜HOT V2.2：師師如夫人前置、七色肚兜與張麗華獨宿夜

```yaml
MASTER_EVENT:
  event_id: "E80"
  source: "HOT V2.2"
  story_time: "槐月十八日下午至槐月十九日破曉"
  status: "SOLIDIFIED"
  confirmed_core:
    - "白御行向李師師提出如夫人公開位置；李師師口頭表示想要，但當時尚未公開、未入家冊／官籍。"
    - "李師師保留住觀止、設席、接待與管理自己房門之自主。"
    - "白御行與李師師完成一場成人事件；過重動作曾被喊停，停下後重新確認，之後李師師明示接受繼續與當次體內射精。"
    - "是否受孕仍 UNKNOWN。"
    - "白御行離房前說『我愛你』；李師師當時未直接回覆，且因其突兀離房有明顯情緒。"
    - "七色蜀錦蘇繡肚兜完成分贈，李師師先選煙青色；此為物品／私人偏好，不是人物人格定義。"
    - "當晚李瓶兒與蘇清離場後，白御行與張麗華在其房內完成獨宿夜成人事件；張麗華在滿足後明示停止第四周天並相擁同眠。"
    - "張麗華與白御行互相明示喜歡；婚姻、排他與生育仍未成立。"
```

## E81｜HOT V2.3：定陶—沈萬三合作與多線案件升級

```yaml
MASTER_EVENT:
  event_id: "E81"
  source: "HOT V2.3"
  story_time: "槐月十九日至槐月二十日深夜"
  status: "SOLIDIFIED"
  confirmed_core:
    - "定陶商會遭偽舊封、私鹽、腰牌仿製等栽贓線攻擊，開封府正式介入並雙向查定陶與巡檢／相關勢力。"
    - "河東池鹽、三炒鹽、三烤／六烤／九烤、高溫爐材與廢鑄錢坊形成多條證據／產業線；不得把能力重疊直接當犯罪定罪。"
    - "沈萬三與白御行／定陶達成停止代理試探及技術合作原則；未簽盟書，不形成共同統治或永久同盟。"
    - "西門慶、廣源、巡檢司等關聯仍需官府證據切割。"
    - "蘇清五百兩三夜舊契在此階段結清；二十八日私人約仍另軸存在。"
    - "白玉池秘密知情擴大至沈家高層，但仍未開池營業。"
    - "李師師『薄情郎』公開事件混合真怨與雙方同意放大的演出成分，不能全改成純戲或真決裂。"
```

## E82｜HOT V2.4：風滿樓、西門暗櫃與五千後算

```yaml
MASTER_EVENT:
  event_id: "E82"
  source: "HOT V2.4"
  story_time: "槐月二十日深夜"
  status: "SOLIDIFIED"
  confirmed_core:
    - "觀止開啟『風滿樓』大型公域，三金主為白御行／定陶、沈萬三、趙受益；出資不取得案情定調權。"
    - "公開說書只可轉述已公開材料，並區分實證、證言、一方主張、待查與傳聞。"
    - "免費法律援助桌成立；蘇清正式委託許慎言調查自身口頭賭約、賣身契與後堂帳。"
    - "西門慶進入開封府程序並以暗櫃資料自救；暗櫃帶出廣源帳、高宅舊事、陳氏女、林教頭／陸某等多線。"
    - "《五千後算》被發現、封送、開冊；潘金蓮作出部分本人供述，但帳文存在與供述不等於法律責任已判。"
    - "蘇清正式賣身契當時仍有效；不得因口頭賭約爭議或五千後算出現就自動作廢。"
    - "阿麗婭舊五千權利仍在官府釐清中，未因此欠觀止新的掛牌、陪客或性服務。"
```

## E83｜HOT V2.5：開封法網、阿麗婭重定義與六條來訪

```yaml
MASTER_EVENT:
  event_id: "E83"
  source: "HOT V2.5"
  story_time: "槐月二十日深夜"
  status: "SOLIDIFIED_MASTER_CUTOFF"
  confirmed_core:
    - "西門慶承認自己接受『蘇清一月』作為五千舊案替代結算；潘金蓮承認殘條字跡，但她是否授權後續暴力仍未證。"
    - "蘇清在西門府前二十八日與其後自願申請妓籍被官府分成兩段處理：後來自願不回溯洗白前段，前段若違法也不自動抹掉後來自願文件。"
    - "阿麗婭未重新掛牌，保留自己決定第一次實際出閣／第一個男人的權利；『一期婚』與候選制度仍屬構想。"
    - "開封府已進入拘提、封存與廣泛證人程序，但高衙內、潘金蓮、西門慶等均未由導演跳到終局刑判。"
    - "六條御息所以賀茂祭車爭後的時間錨，透過觀止共鳴召喚作為未知來客進入本玩家線。"
    - "六條聽到白御行提供的源氏未來敘事，但未把『只愛權勢／血統』接受成自己固定內心，也未被一晚資訊洗掉對源氏的感情成本。"
    - "六條與趙受益只成立初次認識與『只喝茶』；趙代付今晚女客房、茶食與必要日用，不取得任何人身、性、陪宿、戀愛或房門權。"
    - "六條以異時女客住東偏廂，不是掛牌姑娘；是否長住、返回、戀愛或入常設人物資料在 V2.5 當時均未成立。"
    - "李師師三日房禁仍有效；白御行當眾邀其陪睡被明確拒絕。"
```

---

# 3｜截至 HOT V2.5 MASTER 截止硬狀態

```yaml
MASTER_CUTOFF_STATE_V4_2:
  story_time: "理火三年槐月二十日深夜"
  location: "觀止青樓／內院；風滿樓與開封府法律線並行"
  last_canonical_master_event: "E83"
  scene_state: "ROKUJO_GUEST_ROOM_ACCOUNT_ARRANGED; TEA_ONLY_RELATION; LEGAL_NET_ACTIVE"

  player:
    name: "白御行"
    location: "觀止內院"
    last_confirmed_utterance_at_v2_5: "人家沒成交，不算賣。"
    action_after_cutoff: "NONE_IN_MASTER; SEE HOT V2.6-V2.8"

  guanzhi_present_or_immediately_active:
    - "白御行"
    - "六條御息所"
    - "趙受益"
    - "蘇清"
    - "李師師／近處可參與"
    - "張麗華"
    - "紅娘氏"
    - "十三娘"
    - "阿麗婭"
    - "龐春梅／值掌櫃權"

  offsite_or_external:
    潘金蓮: "開封府接受五千後算／蘇清替代結算與相關權限查問"
    西門慶: "開封府羈押／訊問／合作自救程序中"
    包拯: "開封府主持多線並行程序"

  immediate_world_state:
    - "六條今晚東偏廂女客房已安排，但 V2.5 未確認她已入睡。"
    - "六條與趙只答應喝茶，不是戀愛、交易、陪宿、婚配或候選承諾。"
    - "六條原牛車／紅楓異路仍屬未知異常，不得拆解或宣判為永久通道。"
    - "開封府法律線持續，觀止人物／關係場同時運作。"
```

---

# 4｜截至 HOT V2.5 關係、同意與名分覆寫

```yaml
RELATIONSHIP_OVERRIDE_AT_V2_5:
  ZHANG_LIHUA:
    state: "ACTIVE_LOVER_RELATION"
    confirmed:
      - "已明示接受與白御行的情人關係。"
      - "與白御行有多次成人事件與互相明示喜歡。"
      - "保有房間、身體、酒莊與自身關係決定權。"
    marriage: false
    exclusivity: false
    permanent_consent: false

  LI_SHISHI:
    state: "ACTIVE_PRIVATE_RELATION + RU_FUREN_FRAMEWORK_ORALLY_ACCEPTED_NOT_PUBLICLY_IMPLEMENTED"
    confirmed:
      - "V2.2 已口頭表示想要如夫人位置。"
      - "仍保留住觀止、工作、設席與房門自主。"
      - "V2.5 時三日房禁有效，白御行邀請陪睡被明確拒絕。"
    public_ru_furen_status: false
    official_registration: false
    room_ban_at_cutoff: "ACTIVE_THREE_DAY_PRIVATE_BOUNDARY"
    permanent_sexual_consent: false

  LI_PINGER:
    state: "MUTUAL_AFFECTION_OR_PURSUIT_OPEN; LONG_TERM_POSITION_UNDECIDED"
    confirmed:
      - "截至 V2.5 仍未固化為正妻、如夫人或秘密情人。"
      - "既有有限親密不等於性交或永久性資格。"
    intercourse_with_bai_by_v2_5: false
    marriage_or_ru_furen: false

  SU_QING:
    state: "OLD_500_TAEL_THREE_NIGHT_CONTRACT_CLOSED + PRIVATE_28_DAY_PACT_ACTIVE_NOT_AUTO_STARTED + LEGAL_CLAIM_ACTIVE"
    confirmed:
      - "五百兩三夜舊契在 V2.3 已結清。"
      - "二十八日私人約另軸存在，不能被西門慶案件或私人感情自動啟動／延長。"
      - "已正式委託許慎言處理賣身契、口頭賭約與後堂帳。"
    romance_with_bai: "NOT_ESTABLISHED"

  AALIYAH:
    state: "NOT_RELISTED; FIRST_ACTUAL_DEBUT_CHOICE_RETAINED"
    confirmed:
      - "舊五千權利被替代結算與官府釐清削弱／重定義。"
      - "未因此自動成為紅倌或自由妓女。"
      - "一期婚／候選篩選屬構想，不是已成交制度。"

  ROKUJO:
    state_at_cutoff: "ROUTE_EVENT_UNKNOWN_VISITOR_GUEST"
    confirmed:
      - "賀茂祭車爭後抵達觀止。"
      - "與趙受益只成立初識與一杯茶。"
      - "不屬於白御行、趙受益或觀止。"
    prostitution_status: false
    romance_status: false
    sex_consent: false
    long_term_residency: false

  ZHAO_SHOUYI_ROKUJO:
    state: "FIRST_MEETING + TEA_ONLY"
    payment_rights_created: false

  A_LING:
    state: "WHITE_JADE_POOL_AUTONOMOUS_ENTITY; POOL_RESTRICTED"
    sibling_relation_with_bai: false
    white_surname: false
    ownership_by_bai: false
```

---

# 5｜截至 HOT V2.5 法律、帳務、契約與營運覆寫

```yaml
LEGAL_LEDGER_OVERRIDE_AT_V2_5:
  FENGMANLOU:
    status: "ACTIVE_PUBLIC_LEGAL_RELAY_SPACE"
    three_sponsors:
      - "白御行／定陶"
      - "沈萬三"
      - "趙受益"
    sponsor_control_over_outcome: false

  SU_QING_LEGAL_REPRESENTATION:
    lawyer: "許慎言"
    status: "FORMALLY_RETAINED"
    axes:
      - "口頭賭約"
      - "正式賣身契"
      - "後堂帳／五千替代結算"

  FIVE_THOUSAND_CASE_AT_V2_5:
    confirmed:
      - "西門慶承認接受蘇清一月為替代結算。"
      - "潘金蓮承認『蘇清一月，抵五千後帳』等殘條為自己筆跡。"
      - "蘇清前二十八日與後來自願入妓籍必須分時段處理。"
    not_yet_judged:
      - "潘金蓮是否有合法權限作替代結算。"
      - "潘是否授權或明知後續暴力。"
      - "蘇清前二十八日最終法律性質與損害額。"
      - "阿麗婭舊五千權利最終註銷／失效形式。"

  XIMEN_QING:
    state: "DETAINED_AND_COOPERATING_FOR_SELF_PRESERVATION"
    final_conviction: false

  LIUSHENG_CASE:
    state: "ACTIVE"
    high_yanei_violence_order_admission: "EXISTS_BY_V2_5"
    liusheng_death: "UNKNOWN"
    prohibition: "不得以丙七車、血跡、裝車或高衙內承認暴力命令直接等同已證殺人。"

  DINGTAO_SHEN_RELATION:
    state: "STOP_PROXY_TESTING + TECHNOLOGY_COOPERATION_PRINCIPLE"
    signed_alliance: false
    joint_rule_of_capital: false

  WHITE_JADE_POOL:
    state: "RESTRICTED_NOT_OPEN"
    reopening: false
    price: "NOT_SET"
    operating_contract_with_aling: false

  ROKUJO_ACCOUNT:
    payer: "趙受益"
    covered: "今晚客房、茶食、必要衣物與一般女客雜用"
    debt_bondage: false
    sex_or_companionship_right: false
```

---

# 6｜截至 HOT V2.5 知情、秘密、傳聞與異常覆寫

```yaml
KNOWLEDGE_OVERRIDE_AT_V2_5:
  WHITE_JADE_POOL:
    status: "PRIVATE_RESTRICTED_SECRET"
    note:
      - "知情範圍已比早期擴大，並曾對沈家高層有限揭示。"
      - "擴大知情不等於公開營業或可對外招牌化阿泠。"

  ROKUJO_FUTURE_INFO:
    source: "白御行提供的未來敘事"
    rokujo_heard: true
    independently_verified_by_rokujo: false
    not_allowed:
      - "不得寫成六條已經知道自己全部後世。"
      - "不得寫成她已確認白御行的源氏敘事都是客觀真相。"

  ROKUJO_MOTIVE:
    white_claim: "六條深層可能更受權勢／血統／重返舞台吸引"
    rokujo_accepts_as_final_truth: false

  LI_SHISHI_PRIVATE_RELATION:
    note:
      - "部分薄情郎事件已公開成中場笑談。"
      - "私人房內成人細節仍不得因風滿樓存在而自動公開。"

  FIVE_THOUSAND_CASE:
    public_and_official_material_separated: true
    rule: "風滿樓只能依開封府已公開材料轉述，不能拿秘密私函或未公開卷宗補高潮。"
```

---

# 7｜截至 HOT V2.5 未決事項

```yaml
OPEN_HOOKS_AT_V2_5:
  legal:
    - "陳氏女親屬木箱與五百兩用途。"
    - "陶萬春是否到案及能否互證丙七血跡／清洗。"
    - "瘦跛男人身份與柳生離開丙七後去向。"
    - "杜成、梁福、廣源母簿與梁宅狹條紙。"
    - "高衙內、家僕、西門慶、廣源對柳生案之責任切割。"
    - "潘金蓮在蘇清一月抵五千後帳中的契約／帳務責任。"
    - "蘇清前二十八日合法性、損害與後來自願妓籍文件之切割。"
    - "阿麗婭舊五千拍賣權最終如何正式註銷／失效。"

  relationship_and_status:
    - "六條是否留觀止、是否要求返回原時代。"
    - "紅楓異路與牛車是否持續存在。"
    - "六條與趙受益茶約是否只停在社交。"
    - "六條如何處理白御行告知的未來源氏資訊；不得替她預先選擇。"
    - "阿麗婭何時／是否重新申請首次出閣及其一期婚制度是否採納。"
    - "蘇清二十八日私人約觸發日。"
    - "李師師三日房禁倒數與私人帳修復。"
    - "疏影弦音來源。"

  white_jade_pool:
    - "仍未正式復開。"
    - "阿泠的營運、收益、定價與正式契約均未建立。"
```

---

# 8｜MASTER 與 HOT V2.6–V2.8 接關規則

```yaml
ACTIVE_HOT_OVERLAY_V4_2:
  direct_resume_file: "觀止青樓_白御行線_HOT_SAVE_V2.8_槐月二十一日白日_潘身籍補證_白玉池許願幣定存_師師如夫人確認與晚宴前休息版.md"
  retained_unmerged_but_valid_chain:
    - "HOT V2.6：槐月二十一日破曉，軍械案收網、觀止民事戰重啟、許慎言七十二小時按摩券"
    - "HOT V2.7：槐月二十一日破曉至清晨，潘金蓮返樓、五千原款退出、五萬個人賠償請求、身籍待查"
    - "HOT V2.8：槐月二十一日白日，潘身籍補證、白玉池許願幣／定存框架、師師如夫人再確認、晚宴前休息"

  load_order:
    - "先讀本 MASTER V4.2-R1，取得截至 HOT V2.5 的長期因果。"
    - "再讀 HOT V2.8，取得 V2.6–V2.8 已繼承的最新切片。"
    - "若 V2.8 摘要未展開某細節，再按 V2.6、V2.7 回溯。"

  current_actual_resume_point_after_overlay:
    - "理火三年槐月二十一日白日／晚宴前。"
    - "白御行與李師師在她私人房間同榻休息。"
    - "李師師已明示原諒本次道歉並再次明示想要如夫人位置。"
    - "李瓶兒今晚答應赴師師小席，但只成立『先吃飯』。"
    - "白玉池許願幣與阿泠 3.5% 一年定存利率已有條件同意，但未完成正式存入、完整契約或放貸。"
```

## 8.1 防誤讀

- 不得因 MASTER 截止 V2.5，就把 V2.6–V2.8 當成不存在。
- 不得因 V2.6–V2.8 尚未併 MASTER，就把它們降格為傳聞；它們是合法且較新的玩家線 HOT。
- 實際接關以 **MASTER V4.2-R1 + HOT V2.8** 為準。
- 下一次若再做 MASTER，可選擇只吸收到 V2.8，或繼續保留 HOT 緩衝層；不得靜默全吃。

---

# 9｜來源鎖與 SHA-256

```yaml
SOURCE_LOCK_V4_2:
  inherited_master:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"
    sha256: "efb47cfbf79f75244d5a62dcfbe57a855d04535cc9e02a264a57483b60056b85"

  absorbed_hot:
    - file: "觀止青樓_白御行線_HOT_SAVE_V2.0_槐月十八日清晨_四人家人夜結與蘇清履約瓶兒延後決定版.md"
      sha256: "d4ccca433cbe8c285f1f93c4cdf756ff8aaf2641a627e6512ea647b89aa567be"
    - file: "觀止青樓_白御行線_HOT_SAVE_V2.1_槐月十八日下午_定陶商戰起局蘇清私約白玉池補固與麗華私稱版.md"
      sha256: "542e19ef8ae8c842979f72d2db93df162f68c74f83e12b97ff34cb0f4c67c5f5"
    - file: "觀止青樓_白御行線_HOT_SAVE_V2.2_槐月十九日破曉_師理理如夫人前置與張麗華獨宿夜結版.md"
      sha256: "fd8b50f27cb463d43cfd85bcadfd4afb60569265c1246d777422b4917f10e2e9"
    - file: "觀止青樓_白御行線_HOT_SAVE_V2.3_槐月二十日深夜_沈萬三合作與師師薄情郎席前接關版.md"
      sha256: "0f943eb273b6cda36179cc9212b24d0abc4edfd8457f7111f422efee55759901"
    - file: "觀止青樓_白御行線_HOT_SAVE_V2.4_槐月二十日深夜_風滿樓公案與五千後算開冊版.md"
      sha256: "ad757d9a4b2e612b0c606d44dbf55c857d40e8d7e792db18839a3faa50d088f5"
    - file: "觀止青樓_白御行線_HOT_SAVE_V2.5_槐月二十日深夜_開封法網擴張_阿麗婭重定義與六條御息所來訪版.md"
      sha256: "a2107c0df322779ea1ed0f74a59502c63ea52594fded2a295a258f6e68997083"
  retained_hot:
    - file: "觀止青樓_白御行線_HOT_SAVE_V2.6_槐月二十一日破曉_京師軍械案收網_觀止民事戰重啟_許慎言七十二小時按摩券版.md"
      sha256: "a03ccaa2ad3acb4393acb5c386aeacb454005f737a331c3e57a337a4d35597f0"
    - file: "觀止青樓_白御行線_HOT_SAVE_V2.7_槐月二十一日破曉_潘金蓮返樓_五千返還五萬索賠_身籍待查與一千兩候價版.md"
      sha256: "031f2c575eb26e8aa51d62dd4ca9856939392ab9a542b2051e8f570609403a29"
    - file: "觀止青樓_白御行線_HOT_SAVE_V2.8_槐月二十一日白日_潘身籍補證_白玉池許願幣定存_師師如夫人確認與晚宴前休息版.md"
      sha256: "b71874cdeedf061fcc58d11e4c87a798e493d39498e5a5b1ede028e6d87fbeae"
```

---

# 10｜V4.2-R1 固化結論

> **E01–E77：完整繼承 MASTER V4.1-R1。**
>
> **E78–E83：將 HOT V2.0–V2.5 正式升入 MASTER。**
>
> **HOT V2.6–V2.8：刻意保留，不在本輪固化。**
>
> **MASTER 截止：槐月二十日深夜／HOT V2.5。**
>
> **實際接關：MASTER V4.2-R1 + HOT V2.8。**

---

# APPENDIX A｜繼承之 MASTER V4.1-R1 全文

> **法位：歷史繼承來源。** 下方內容完整保留 E01–E77 與舊快照；其中任何舊 `master_cutoff`、`current_resume_point`、`valid_but_not_merged` 等欄位若與本版第0–10區衝突，均只視為 V4.1 當時的歷史狀態。

<!-- INHERITED_MASTER_V4_1_BEGIN -->
# 觀止青樓｜白御行線 MASTER SAVE V4.1-R1
## 截至 HOT V1.9 固化整合版｜V2.0–V2.3 保留於 HOT 層

---

```yaml
SAVE_META:
  save_id: "GUANZHI_BAIYUXING_MASTER_V4_1_R1"
  title: "觀止青樓｜白御行線 MASTER SAVE"
  version: "V4.1-R1"
  world: "觀止青樓"
  player: "白御行"
  route_status: "ACTIVE"
  record_type: "CONSOLIDATED_MASTER_ARCHIVE"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  fixed_calendar_anchor: "理火三年槐月五日｜永恆第一夜"
  master_cutoff: "理火三年槐月十七日晚｜HOT V1.9 暫停節點"
  last_canonical_master_event: "E77"
  current_route_resume_source: "觀止青樓_白御行線_HOT_SAVE_V2.3_槐月二十日深夜_沈萬三合作與師師薄情郎席前接關版.md"
  current_route_resume_note: "本 MASTER 只固化至 HOT V1.9；V2.0、V2.1、V2.2、V2.3 均為合法且較新的 HOT，不得因未併入 MASTER 而否認。"
  supersedes_as_master:
    - "觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版.md"
  absorbs_and_retires_from_default_load:
    - "觀止青樓_白御行線_HOT_SAVE_V1.5_槐月十五日傍晚_師理理初次肉體與定陶商會案雙線接關版.md"
    - "觀止青樓_白御行線_HOT_SAVE_V1.6_槐月十六日清晨_張麗華花燭前置與白玉池異常回顯封池版.md"
    - "觀止青樓_白御行線_HOT_SAVE_V1.7_槐月十六日午後_白玉池暫閉與張麗華花燭前入睡接關版.md"
    - "觀止青樓_白御行線_HOT_SAVE_V1.8_槐月十七日上午_張麗華酒莊接手與三日陪伴線.md"
    - "觀止青樓_白御行線_HOT_SAVE_V1.9_槐月十七日晚_四人家宴與瓶兒留宿接關版.md"
  valid_but_not_merged:
    - "HOT V2.0"
    - "HOT V2.1"
    - "HOT V2.2"
    - "HOT V2.3"
  rejected_source:
    file: "HOT_SAVE_V1.3"
    status: "ILLEGAL_CORRUPTED_SAVE"
    use: "AUDIT_ONLY"
```

```yaml
SOURCE_LOCK:
  inherited_master_v4_0_r1:
    sha256: "b39939a7f9a42ed781f432a78915c18837da8508a7f5edb4fef377122c77c47e"
  absorbed_hot_v1_5:
    sha256: "e9fc105e4be64a6934a2aa40af08cca26543e15b7752b5548f462ba57614d556"
  absorbed_hot_v1_6:
    sha256: "ea7de1259b25d362fd4333728dfb9961463e57f0839e3f33d20422a776fe491d"
  absorbed_hot_v1_7:
    sha256: "ac0953a8d8886a410d3f0053f61b22ba7d13ec891a12d14e1abf270a1f6efa86"
  absorbed_hot_v1_8:
    sha256: "25b4073d085fce42cb26a97bb6b3c22ada6b64aa2508b680683fde2aba684cb6"
  absorbed_hot_v1_9:
    sha256: "d872b95786b450243a5dfcdd3388b9ca37289c3404fae397dd2dfc69acf35281"
```

> **本檔已將 HOT V1.5 至 V1.9 固化為 MASTER 事件 E46–E77。**
>
> **V2.0 至 V2.3 仍停留在 HOT 層，實際接關必須疊加最新 HOT V2.3。**

---

# V4.1 檔內法位與閱讀規則

```yaml
INTERNAL_PRECEDENCE:
  highest_sections:
    - "第16區：V1.5–V1.9 固化事件 E46–E77"
    - "第17區：截至 V1.9 關係硬狀態覆寫"
    - "第18區：截至 V1.9 帳目、資產、契約與物品覆寫"
    - "第19區：截至 V1.9 知情、傳聞、秘密與異常覆寫"
    - "第20區：截至 V1.9 未決事項"
    - "第21區：截至 V1.9 MASTER 截止狀態"
    - "第22區：MASTER 與 HOT V2.3 接關規則"
  inherited_sections:
    range: "第0區至第15區"
    role: "完整保留 V4.0-R1 所固化之 E01–E45 與早期厚肉因果"
    historical_annotation_rule:
      - "其中提到『只固化至 V1.4』『V1.5/V1.6 未合併』或舊接關點的句子，僅保留為 V4.0 歷史標記。"
      - "如與第16–22區衝突，以第16–22區為準。"
```

---

# A｜V4.0-R1 繼承基線全文（E01–E45）

以下自原 MASTER V4.0-R1 原樣繼承，保留早期因果、關係、帳目、秘密與拒絕記錄。其截止點與接關說明已由本檔第16–22區覆寫。

---

# 0｜固化範圍、事件映射與法位

```yaml
CONSOLIDATION_MANIFEST:
  inherited_master_events:
    range: "E01-E30"
    treatment: "完整保留"

  promoted_private_event:
    event_id: "PSE-WY-ZLH-001"
    treatment: "完整保留知情範圍、外洩禁止與揭露條件"

  absorbed_hot_v1_2_events:
    range: "E31-E36"
    treatment: "沿用原事件編號"

  absorbed_hot_v1_4_events:
    source_range: "HOT_V1_4_E01-E09"
    canonical_range: "E37-E45"
    treatment: "重新編入 MASTER，保留 source_alias"

  not_merged:
    - "HOT V1.5 全部事件"
    - "HOT V1.6 全部事件"

  invalid_source:
    - "HOT V1.3：只准審計，不准作世界、人物、關係或接關來源"
```

## 0.1 固化原則

1. 只保存已發生、可觀察、人物明示、帳目可核對，或玩家對自身言行的有效校正。
2. 人物解讀、心理推測、研究假說與傳聞另列來源，不升格為客觀真相。
3. 拒絕、契約、感情、同意、付款、公開知情與私人秘密分軸保存。
4. `UNKNOWN`、`UNDECIDED`、`DISPUTED` 與 `PARTIALLY_UNKNOWN` 均為合法狀態。
5. 同一事項若來源衝突，不自行平均；保留來源差異並指定目前運行狀態。
6. 本 MASTER 的事件截止點早於 V1.5／V1.6；不得從後兩檔倒灌結果。

## 0.2 狀態標籤

```yaml
STATUS_TAGS:
  CONFIRMED: "已由言行、帳目或玩家校正確立"
  ACTIVE: "目前仍在運作"
  CLOSED: "已正式結案"
  WITHDRAWN: "曾提出，後由提出者收回"
  REJECTED: "已被對方有效拒絕"
  UNSIGNED: "有草案但未簽署"
  UNSETTLED: "已發生交易或爭議，但未正式結帳"
  DISPUTED: "來源或當事人對狀態有衝突"
  PROMISED_NOT_EXECUTED: "已承諾，尚未執行"
  ORDERED_NOT_DELIVERED: "已下單，尚未交付"
  UNKNOWN: "資料不足，禁止補寫"
  POSSIBLE_NOT_FIXED: "只是一條可能分支"
  STAGED: "戲中戲、扮演、話本或即興演出，不是現實履歷"
  PUBLIC_WITNESSED: "有在場目擊者"
  PRIVATE: "只在私下場景成立"
```

## 0.3 來源衝突登錄

```yaml
SOURCE_CONFLICT_REGISTRY:
  SU_QING_NOVEL_COMMISSION_ACCEPTANCE:
    master_v3_r2_claim: "ACCEPTED"
    later_hot_v1_0_and_v1_2_claim: "AMBIGUOUS_REQUIRES_CONFIRMATION"
    current_master_state: "DISPUTED_AMBIGUOUS"
    rule: "在出現新的明示確認以前，不得寫成已明確接受，也不得寫成已拒絕。"
```

---

# 1｜時間軸（TIME AXIS）

```yaml
GUANZHI_CALENDAR:
  era: "理火三年"
  fixed_first_night: "槐月五日"
  rule: "槐月五日永遠是觀止所有玩家線的第一夜"
  progression: "每過一夜，觀止曆順延一日"

BAI_YUXING_ROUTE_TIME:
  inherited_master_range: "槐月五日至槐月十日清晨／E01-E30"
  hot_v1_1_private_events: "槐月十日下午至夜間"
  hot_v1_2_events: "槐月十日夜至槐月十一日清晨／E31-E36"
  hot_v1_4_events: "槐月十一日夜／E37-E45"
  master_cutoff: "槐月十一日深夜，白御行選擇休息"
  later_hot_overlay:
    - "V1.5"
    - "V1.6"

TIME_CERTAINTY:
  first_night: "CONFIRMED"
  second_to_fourth_night_exact_distribution: "PARTIALLY_UNKNOWN"
  fifth_night: "CONFIRMED"
  huai10_private_sequence: "CONFIRMED"
  huai11_morning: "CONFIRMED"
  huai11_night_internal_exact_clock: "PARTIALLY_UNKNOWN"
```

---

# 2. 白御行角色硬設定（PLAYER HARD STATE）

```yaml
BAI_YUXING:
  identity:
    early_public: "未報姓名的成年男客／無名客"
    current_public: "白御行／定陶商會總會長"
  alcohol:
    drinks: false
    reason: "身體無法消化酒精；自認喝酒容易誤事"
  relationship_structure:
    formal_wife_positions_remaining: 0
    later_positions_offered:
      - "如夫人"
      - "妾室"
      - "情人"
      - "外室"
      - "其他雙方另定位置"
  declared_formal_wives:
    - "夏娃"
    - "后土娘娘"
    - "善喜"
  declared_other_relations:
    ru_furen:
      - "女帝"
      - "西施轉世"
    lovers:
      - "地獄之母"
      - "合歡宗主"
      - "千年地仙"
    concubines:
      - "五名媚魔"
      - "一名鬼寡婦"
    female_slave:
      - "似伊"
  core_behavior_visible_in_route:
    - "習慣把關係、名分、資源與風險說成可核對條件"
    - "願意以金錢改變市場、傳聞與選擇環境"
    - "不承諾只愛一人，並明示可能繼續追求其他女人"
    - "重視不可消失的因果、記憶與被留下的痕跡"
    - "對稀缺、傳奇、異常與有自身意志的女子有強烈注意"
```

本欄只記白御行自己已經公開說過或玩家已明示的內容，不替他判斷善惡、真愛程度或最終目的。

---


---

# 3｜關係硬紀錄（RELATIONSHIP HARD STATE）

> 本區只回答固化截止點「現在成立什麼」。完整原因放在第 4 區事件鏈。

## 3.1 潘金蓮

```yaml
RELATION_PAN_JINLIAN:
  status: "ACTIVE_WORKING_RELATION"
  roles:
    - "觀止掌櫃"
    - "帳目與契約記錄者"
    - "白御行線SAVE保管者"
    - "傳聞、酒帳、婚契草案與物資安排的實務中介"
  romance: "NOT_ESTABLISHED"
  key_trust: "白御行多次要求她記帳、存檔、轉交銀兩與核對舊事"
```

## 3.2 辭歲

```yaml
RELATION_CISUI:
  status: "DISTANT_NEGOTIATION_WITH_EFFECTIVE_REFUSALS"
  confirmed:
    - "第一夜談過白御行想娶觀止花魁回家"
    - "第二夜拒絕進入只有一把椅子的包廂，沒有坐白御行大腿"
    - "第五夜拒絕二十八日後仍不可撤回的心理奴化條件"
  negotiable_only:
    - "二十八日內的臨時角色與規則可談"
  rejected:
    - "永久心理依附"
    - "失去二十八日後停止選擇白御行的能力"
  body_contact: false
  contract_signed: false
  romance: "NOT_ESTABLISHED"
```

## 3.3 浮香

```yaml
RELATION_FUXIANG:
  status: "RESPECTFUL_ATTENTION_WITH_MARRIAGE_INCOMPATIBILITY"
  confirmed:
    - "第一夜收五兩琴資，彈《十八摸》，自願多留半曲與短談"
    - "第五夜再收五兩琴資，彈《十八摸》並留下"
    - "第五夜另彈《醉扶歸》為酒局助興"
    - "提出琴坊、女徒、田產的產業構想"
  marriage_position:
    ru_furen: "REJECTED"
    requirement: "若她只守白御行，白御行也必須只守她"
  business_interest: "琴坊與田產；地契店契須歸她、經營由她決定"
  romance: "NOT_ADJUDICATED"
```

## 3.4 張麗華

```yaml
RELATION_ZHANG_LIHUA:
  state_class: "UNDECIDED"
  state_label: "UNDECIDED_WITH_MUTUAL_RECOGNITION_AND_COMPLETED_CLOTHED_OVERNIGHT_COMPANIONSHIP"

  former_engagement:
    status: "TERMINATED"
    deposit_returned: true

  one_wan_wine_account:
    status: "POSTED_ACTIVE"
    owner_for_accounting: "張麗華專用"
    bai_asset: false

  private_mutual_recognition:
    confirmed:
      - "白御行明示：張麗華留下或離開都不虧欠他"
      - "張麗華開始區分影響選擇與剝奪選擇"
      - "白御行接受她拒絕自己的可能"

  private_contact:
    - "張麗華接受擁抱"
    - "張麗華在私下以『官人』作當下稱呼"
    - "兩人穿衣相擁睡完一夜"
    - "沒有性交"

  private_secret:
    archive_id: "PSE-WY-ZLH-001"
    status: "SEALED_ACTIVE"

  not_established:
    - "婚姻"
    - "妻妾名分"
    - "無婚書伴侶關係最終接受"
    - "排他承諾"
    - "公開身份"
    - "永久身體資格"

  romance: "NOT_ADJUDICATED"
  autonomy_claim: "EXPLICIT"
```

## 3.5 蘇清

```yaml
RELATION_SU_QING:
  status: "UNSETTLED_OLD_CONTRACT + ACTIVE_WRITING_COMMISSION"
  proposal_award:
    amount: "三百兩"
    status: "AWARDED"
  three_night_contract:
    amount: "五百兩"
    nights: 3
    intercourse_completed: false
    effective_refusal_each_night: true
    bai_view: "違約／有沒有履約自己知道"
    su_admission_of_breach: false
    refund_or_compensation: false
    ledger: "UNSETTLED"
  fifth_night_roles:
    - "柳如煙戲中戲的女秘書／小說家"
    - "張麗華話本受託作者"
  novel_commission:
    reward: "五百兩，僅在白御行滿意並收稿後成立"
    delivery_rate: "每日四千字"
    book_cycle: "十日一本"
    paid: false
    status: "COMMISSIONED_NOT_ACCEPTED"
  romance: "NOT_ESTABLISHED"
```

### 3.5.1 蘇清寫作委託來源衝突修正

```yaml
SU_QING_NOVEL_COMMISSION_CURRENT:
  state_class: "DISPUTED"
  commission_status: "AMBIGUOUS_REQUIRES_CONFIRMATION"
  manuscript_status: "NOT_SUBMITTED"
  client_review: "NOT_REVIEWED"
  payment: "UNPAID_CONDITIONAL"
  precedence_note: "本欄優先於 3.5 舊文字中的 COMMISSIONED_NOT_ACCEPTED，以及 R2 的 ACCEPTED 單一判定。"
```

## 3.6 醉花

```yaml
RELATION_ZUIHUA:
  status: "TRUSTED_WINE_AND_INTIMACY_THREAD"
  confirmed_intimacy:
    - "曾與白御行親吻"
    - "曾與白御行共浴"
    - "曾替白御行取衣、整衣"
  intercourse: "NOT_CONFIRMED"
  fifth_night:
    - "以三十年女兒紅調《不得飲》"
    - "取得該罈酒的後續處理權"
  marriage_or_exclusive_commitment: false
```

## 3.7 十三娘

```yaml
RELATION_SHISANNIANG:
  status: "QUESTION_BET_COMPLETED"
  bet_winner: "十三娘"
  answer_received: true
  answer_satisfactory: true
  life_claimed: false
  ongoing_obligation: false
  relationship: "能直接質問白御行核心恐懼的酒局對手與見證者"
  romance: false
```

## 3.8 紅袖

```yaml
RELATION_HONGXIU:
  status: "DISTURBED_BUT_NOT_SURRENDERED"
  possible_future_as_hongnu: "POSSIBLE_NOT_FIXED"
  current_identity: "紅袖"
  current_consent_to_training: false
  current_refusal_effective: true
  admitted_effect:
    - "未來影像在她心中留下不安與疑問"
  not_admitted:
    - "沒有承認自己必然想成為紅奴"
    - "沒有承認白御行已看穿她"
  ice_silkworm_strings:
    status: "ORDERED_NOT_DELIVERED"
    due: "槐月十日／明日"
  ru_furen_invitation:
    status: "UNDER_CONSIDERATION_OR_NOT_ACCEPTED"
    accepted: false
```

### 3.8.1 冰蠶弦到期更新

```yaml
HONGXIU_ICE_SILKWORM_STRINGS_CURRENT:
  original_due: "槐月十日"
  current_status: "OVERDUE_OR_DELIVERY_RESULT_NOT_RECORDED"
```

## 3.9 李清照

```yaml
RELATION_LI_QINGZHAO:
  state_class: "CLOSED_FOR_CURRENT_VISIT"
  state_label: "MUTUAL_LITERARY_ATTENTION_WITH_RETURN_TO_OWN_ERA"
  confirmed:
    - "李清照承認白御行詩勝"
    - "如夫人邀請拒絕不變"
    - "李清照選擇返回自身時代"
  current_presence: false
  character_pool_admission: "NOT_ADMITTED"
  future_revisit: "POSSIBLE"
  romance: "NOT_ADJUDICATED"
```

## 3.10 李師師／師理理

```yaml
RELATION_LI_SHISHI:
  state_class: "ACTIVE"
  state_label: "INDEPENDENT_GUANZHI_RESIDENT_WITH_PRIVATE_TRUST_AND_PURSUIT_OPEN"

  identity_rule:
    - "師理理不是新人物，也不是第二人格"
    - "師理理是李師師在白御行私人空間中的身份表現"
    - "人前仍以李師師為主；其他人物不得無來源使用師理理稱呼"

  stay_decision:
    remain_in_guanzhi: true
    return_to_jingkang: false
    character_pool_admission: "CONFIRMED"

  professional_position:
    role: "設席花魁"
    first_night_auction: false
    whole_night_buyout: false
    seat_opening_owner: "李師師"
    guest_selection_owner: "李師師"
    separate_ledger: true
    first_seat_date: "NOT_SET"
    first_guest: "NOT_SELECTED"

  relation_with_bai:
    - "白御行可以繼續追求"
    - "私人信任增加"
    - "槐月十一日深夜，李師師理解更親近邀請並自行同意留下"

  not_established:
    - "戀愛承諾"
    - "排他關係"
    - "婚姻"
    - "聘約"
    - "白御行首席預約"
    - "永久身體資格"

  physical_relation_at_master_cutoff: "NOT_ESTABLISHED_IN_THIS_MASTER"
  relationship_with_zhao: "STAGED_NOT_REAL_CONFIRMED"
```

## 3.11 柳如煙

```yaml
RELATION_LIU_RUYAN:
  ontology: "網文／爽劇第一女主概念集合體"
  status: "STAGED_GUEST_DEPARTED_OR_DISSIPATED"
  掛牌邀請:
    initially_discussed: true
    deal_finalized: false
    bai_withdrew_assumed_deal: true
  fifth_night_play:
    - "柳如煙大戰眾女"
    - "顧北辰霸總劇"
    - "豪門家宴窮女逆襲劇"
  all_allegations_in_play:
    - "酒店男人"
    - "打胎藥"
    - "白月光"
    - "家族悲慘背景"
    - "空白支票遣散男友"
  legal_or_biographical_truth: "NONE_ESTABLISHED; ALL_STAGED"
  current_location: "UNKNOWN／如煙消散"
```

## 3.12 白玉池無名女子

```yaml
RELATION_WHITE_JADE_POOL_WOMAN:
  status: "UNIDENTIFIED_UNRESOLVED_ENCOUNTER"
  inviter: "無名女子"
  invited_party: "白御行"
  location: "白玉池"
  bai_arrival: "白御行自行前往並先入池等待"
  bai_condition: "對方除去防備、下水、坦誠相對後才談"
  woman_response: "拒絕白御行指定的形式，離場"
  negotiation_started: false
  physical_contact: false
  identity: "UNKNOWN"
  beauty_assessment_by_hall: "被評為觀止前列／主桌等級，但不是正式花魁排名"
  future_hook: "白御行表示若對方確為美女，下次可選擇吃點虧"
```

重要校正：白玉池是**女子邀白御行**，不是白御行邀她。雙方未達成共同談判規則。

---

## 3.13 紅娘氏

```yaml
RELATION_HONGNIANG:
  state_class: "ACTIVE"
  state_label: "ROUTE_ACTIVE_INFORMATION_AND_BUSINESS_RELATION"
  confirmed:
    - "紅娘氏已在白御行線正式出場"
    - "白御行將趙受益第一筆紅倌交易讓給紅娘氏承接"
    - "紅娘氏完成第一筆交易並持有趙受益留下的宮牌／聯絡牌"
    - "白御行當著師理理面向紅娘氏購買情報"
    - "形成師理理提供資訊、紅娘整理、白御行付款、紅娘與師理理分帳的交易鏈"
  with_bai:
    financial_contract: "TRANSACTION_SPECIFIC_ONLY"
    romance: "NOT_ESTABLISHED"
    sexual_relation: false
  business_position:
    - "紅倌人"
    - "大堂情報與客源中介"
```

## 3.14 小翠

```yaml
RELATION_XIAOCUI:
  state_class: "ACTIVE_CAUTION_WITH_INCREASED_TRUST"
  eight_hundred_arrangement:
    status: "REJECTED_NOT_ESTABLISHED"
    reason_source: "小翠本人對恐懼、可能疼痛或不舒服的表達"
  bai_interpretation:
    content: "小翠可能因過去不良經驗形成男性與親密關係的負面連結"
    status: "PLAYER_INTERPRETATION_NOT_DIAGNOSIS"
  massage_service:
    status: "PURCHASED"
    exact_completion_detail: "NOT_RECORDED"
  future_plan:
    familiar_guest_safety_plan: "PROPOSED"
    red_green_pair: "PROPOSED_PENDING_PAN_APPROVAL"
  romance: "NOT_ESTABLISHED"
```

## 3.15 白三娘

```yaml
RELATION_BAISANNIANG:
  state_class: "ACTIVE_PROPOSAL_PARTICIPANT"
  confirmed:
    - "白三娘接受與小翠組成老帶新雙飛方案的提案"
  not_established:
    - "方案已正式營運"
    - "潘金蓮已批准"
    - "任何客人已取得雙飛服務"
    - "退休後小會所投資成立"
  future_business: "PENDING"
  romance_with_bai: "NOT_ESTABLISHED"
```

---

# 4｜因果故事總表（CAUSAL STORY LOG）

> E01-E30 完整繼承 V3.0-R1；E31-E45 為本次固化新增。

## E01｜第一夜：無名客入觀止、辭歲與浮香

```yaml
EVENT_ID: "E01"
DATE: "理火三年槐月五日夜／第一夜"
STATUS: "CONFIRMED"
PARTICIPANTS:
  - "白御行（當時未報姓名）"
  - "辭歲"
  - "浮香"
CAUSE:
  - "白御行第一次進入觀止"
  - "白御行帶有尋妻意圖"
PROCESS:
  - "先與辭歲談想娶觀止花魁回家；完整逐字內容殘缺"
  - "給浮香五兩琴資，請她彈《十八摸》"
  - "浮香自願多留半首無名小調與短暫交談"
  - "討論如夫人／平妻、嫁妝保護、子女分產、正妻位與忠誠"
IMMEDIATE_EFFECT:
  - "白御行尋妻意圖被觀止部分人物知悉"
  - "浮香知道自己是可能被邀請的人，但沒有承諾"
RELATIONSHIP_IMPACT:
  - "浮香：建立尊重但未定案的婚姻可能"
  - "辭歲：建立最初注意，內容未完整保存"
FUTURE_HOOK:
  - "命運籤已取得未開；後續是否同一支籤未知"
```

## E02｜第二夜：辭歲包廂拒絕與張麗華初登場

```yaml
EVENT_ID: "E02"
DATE: "理火三年槐月六日夜／第二夜"
STATUS: "CONFIRMED"
CAUSE:
  - "白御行再入觀止；潘金蓮安排獨立包廂"
PROCESS:
  - "辭歲問房內是否有位置"
  - "白御行表示只有一把椅子，可坐他大腿"
  - "辭歲明確拒絕並離開"
  - "其後張麗華登場，婚約話題開啟"
IMMEDIATE_EFFECT:
  - "辭歲未進包廂，沒有身體接觸"
  - "張麗華與白御行正式進入婚約談判"
RELATIONSHIP_IMPACT:
  - "辭歲的拒絕成為有效且不可偷換的界線"
```

## E03｜張麗華第一次婚約：五千、一萬五千與一萬訂金

```yaml
EVENT_ID: "E03"
DATE: "第二夜後段／精確夜次已知為早期但不再硬細分"
STATUS: "CLOSED"
CAUSE:
  - "張麗華開出五千兩聘金"
PROCESS:
  - "白御行不壓價，反報一萬五千兩"
  - "白御行先付一萬兩訂金"
  - "後因亡國後生存與白御行可能先殺她的說法，張麗華拒絕讓男人決定其生死"
  - "張麗華退出婚約"
  - "一萬兩訂金退回白御行"
IMMEDIATE_EFFECT:
  - "婚約終止"
RELATIONSHIP_IMPACT:
  - "白御行對張麗華形成高代價偏好"
  - "張麗華對自身關係與生命主權提出明確要求"
```

## E04｜一萬兩三日懸賞與「無路，無解」

```yaml
EVENT_ID: "E04"
DATE: "早期第三至第四夜區段／確切拆分不足"
STATUS: "CLOSED"
CAUSE:
  - "訂金退回後，白御行把一萬兩改設為三日懸賞"
QUESTION:
  - "陳朝已亡、張麗華失去原權勢後，如何讓她有尊嚴地活"
PROCESS:
  - "觀止眾人提出方案"
  - "蘇清提出在國破前一年先行背叛、建立退路"
  - "白御行認為方案有價值但改變原題，另給三百兩"
  - "期限屆滿，潘金蓮宣布『無路，無解』"
RESULT:
  winner: "NONE"
  one_wan_awarded: false
RELATIONSHIP_IMPACT:
  - "張麗華的生存問題成為白御行線長期核心"
  - "蘇清與白御行的知識、交易與價值觀交鋒加深"
```

## E05｜一萬兩轉為張麗華酒錢

```yaml
EVENT_ID: "E05"
STATUS: "ACTIVE_ACCOUNT"
CAUSE:
  - "三日懸賞無人得標"
PROCESS:
  - "張麗華提出留觀止當掌櫃、自食其力"
  - "白御行要求潘金蓮拒絕"
  - "白御行把一萬兩指定為張麗華可自由使用的觀止酒錢"
  - "潘金蓮正式入帳"
  - "張麗華口頭說不用，並說『今天戒酒』"
RESULT:
  - "一萬兩不再是白御行資產"
  - "張麗華沒有成為觀止掌櫃"
RELATIONSHIP_IMPACT:
  - "白御行以資源保留他所偏好的張麗華生活形狀"
  - "張麗華沒有因此交出關係主權"
```

## E06｜蘇清五百兩三晚交易：事實修正版

```yaml
EVENT_ID: "E06"
STATUS: "UNSETTLED"
CAUSE:
  - "白御行與蘇清把感情與肉體價值分開討論"
CONTRACT:
  amount: "五百兩"
  duration: "三晚"
  emotional_component: "排除"
PROCESS:
  - "三晚均進入床榻、交談或親密情境"
  - "每晚在真正性交前最後關頭，蘇清有效拒絕"
  - "三晚均沒有完成性交"
  - "白御行認定有履約問題，給她保全面子的離場語『有沒有履約，自己知道』"
  - "蘇清沒有承認違約，也沒有主張完整履約、退款、賠償或重議"
RESULT:
  ledger: "UNSETTLED"
  intercourse: false
RELATIONSHIP_IMPACT:
  - "白御行與蘇清之間形成未結交易、價值與角色理解的長期張力"
```

## E07｜第五夜開場：張麗華、酒與子時條件

```yaml
EVENT_ID: "E07"
DATE: "理火三年槐月九日夜／第五夜"
STATUS: "CONFIRMED"
CAUSE:
  - "白御行重返觀止，將酒局與婚議重新放在同一張桌上"
PROCESS:
  - "白御行讓張麗華喝至子時"
  - "表示清醒可談婚事，喝醉則子時前費用由他承擔"
  - "張麗華選擇喝酒，未因此答應婚事"
  - "十三娘留下陪飲"
IMMEDIATE_EFFECT:
  - "第五夜大堂酒局成形"
```

## E08｜辭歲二十八日心理奴化提案被拒

```yaml
EVENT_ID: "E08"
DATE: "第五夜"
STATUS: "REJECTED"
CAUSE:
  - "白御行回顧辭歲掛牌與二十八日競價可能"
PROCESS:
  - "白御行提出二十八日內把辭歲訓成順從女奴"
  - "更要求二十八日後仍渴望主人召回與鞭子"
  - "辭歲明確說『不要』"
RESULT:
  - "永久心理奴化條件不成立"
  - "未來掛牌競價可能仍可存在，但不得攜帶已拒絕條件"
```

## E09｜浮香第五夜：琴、琴坊與雙向排他

```yaml
EVENT_ID: "E09"
DATE: "第五夜"
STATUS: "CONFIRMED"
PROCESS:
  - "白御行再給五兩，浮香彈《十八摸》"
  - "浮香留下喝茶，後彈《醉扶歸》"
  - "白御行問一萬五千兩產業選擇"
  - "浮香提出琴坊、修琴挑弦、收女徒與買田"
  - "她要求地契店契歸自己、白御行不得干涉經營"
  - "她拒絕單向多偶的如夫人位置"
RESULT:
  - "產業想法成立為人物願景，未實際投資"
  - "婚姻不成立"
```

## E10｜十三娘問心賭局

```yaml
EVENT_ID: "E10"
DATE: "第五夜"
STATUS: "COMPLETED"
PROCESS:
  - "骰局十三娘十四點勝白御行十二點"
  - "十三娘問：白御行怕女人不愛，還是怕愛過仍能離開"
  - "白御行回答善喜與自己是否真正愛過的反思"
  - "白御行講述死亡時不願焚毀與女人、女兒、家庭相關記憶"
  - "十三娘判定回答到位"
RESULT:
  life_claimed: false
  continuing_obligation: false
RELATIONSHIP_IMPACT:
  - "十三娘取得白御行深層自述"
  - "白御行害怕因果與記憶被抹去的動機被在場者理解"
```

## E11｜白御行家眷與三名正式妻子公開

```yaml
EVENT_ID: "E11"
DATE: "第五夜"
STATUS: "CONFIRMED_PLAYER_HISTORY"
PROCESS:
  - "白御行說明只有夏娃、后土娘娘、善喜有正式婚禮"
  - "夏娃之死內情被封閉，不許旁人自行推論"
  - "后土娘娘與善喜各有其國族／鬼魂責任"
  - "白御行明示不再提供正式妻位，只提供其他關係位置"
RESULT:
  - "在場女子理解白御行的多偶結構不是臨時說詞"
  - "浮香、李清照等人的排他要求與白御行架構形成實質不相容"
```

## E12｜似伊影像與紅袖可能未來

```yaml
EVENT_ID: "E12"
DATE: "第五夜"
STATUS: "POSSIBLE_NOT_FIXED"
CAUSE:
  - "白御行展示似伊調教『紅奴』的影像"
PROCESS:
  - "影像中的女子自稱以前叫紅袖、現在叫紅奴"
  - "白御行主張這可能是現紅袖未來分支"
  - "紅袖承認影像造成不安，但拒絕承認其必然性"
  - "白御行說已種下懷疑；紅袖說也會懷疑他的框架"
  - "白御行訂一盒冰蠶弦，紅袖預先接受物品但不接受被計算斷弦數"
RESULT:
  - "現在紅袖仍是紅袖"
  - "未來紅奴線不固定"
```

## E13｜三十年女兒紅、《不得飲》與公開官人稱呼

```yaml
EVENT_ID: "E13"
DATE: "第五夜／子時後"
STATUS: "PUBLIC_WITNESSED"
CAUSE:
  - "白御行以最貴女兒紅建立稀缺與酒鬼誘惑局"
PROCESS:
  - "酒由醉花保管並開封調成《不得飲》"
  - "李清照先飲"
  - "白御行曾禁止給張麗華，後以稱呼換取一杯"
  - "張麗華在十幾桌前說『官人，我要那杯酒』"
  - "後又說『官人……奴家還要嘛』"
  - "醉花只再給小半杯"
  - "白御行宣告目的已達，剩餘酒由醉花處理，自己不再控制"
RESULT:
  - "張麗華得到酒"
  - "婚姻沒有成立"
  - "形成高傳播性的公開傳聞素材"
```

## E14｜女兒紅來源與最後一罈競局

```yaml
EVENT_ID: "E14"
DATE: "第五夜"
STATUS: "OPEN"
PROCESS:
  - "舊帳只知約三十年前入窖，原埋酒人不明，殘紙疑有『玉』字"
  - "白御行指出同批不會只有一罈"
  - "潘金蓮開始追查酒商、路引、封泥與同批酒"
  - "白御行聲稱找到同批便砸，只留最後一罈"
  - "張麗華聲稱要先找到、換封、藏起"
RESULT:
  known_jar_count: 1
  additional_found: 0
  destroyed: 0
  outcome: "UNRESOLVED"
```

## E15｜李清照《一剪梅》與白御行四言長詩

```yaml
EVENT_ID: "E15"
DATE: "第五夜"
STATUS: "COMPLETED"
BOUNDARY:
  - "詩局只論詩，不改婚姻條件"
LI_QINGZHAO_WORK: |
  三十年香醒舊愁。
  燈滿青樓，客滿高樓。
  誰將一盞釣王侯，
  未飲先羞，飲罷還求。

  一縷春魂不肯休。
  身在重樓，夢過神州。
  柳絮無根也自由，
  牆任人修，風自悠悠。
BAI_YUXING_WORK: |
  冷雨迷途，霧色朦朧。平原廣遠，風起蒼穹。
  孤行客影，尋星夜中。天涯遠望，心自如鴻。
  棲身四海，隨遇而容。浮生若寄，逐夢匆匆。
  心歸舊處，眷戀如繩。山河遮蔽，意志如松。
  巨力壓身，笑抵風虹。鎖禁形體，心志難封。
  春風化解，千愁萬重。故園遙望，情深意濃。
  柳枝飄動，春水匆匆。編枝成夢，搖落悲情。
  化絮無定，隨風飛行。草木闢地，生意自興。
  牆高千丈，志遠心盈。柔風吹越，自在難屏。
  力縛身囚，魂志不驚。笑看凡世，天地重明。
  浮華落盡，我自歸心。
  山川靜默，江河寄音。
  此身仍在，猶有歸途。
  長夜未盡，此意長明。
RESULT:
  winner: "白御行，由李清照自行承認"
  marriage_changed: false
RELATIONSHIP_IMPACT:
  - "李清照對白御行的文學注意提高"
```

## E16｜歪詩局與《玉樹後庭花》補句

```yaml
EVENT_ID: "E16"
DATE: "第五夜"
STATUS: "COMPLETED"
ZHANG_POEM: |
  三十年酒一小盅，
  兩個酒鬼坐堂中。
  清照若敢全吞盡，
  本宮醉後不認宋。
LI_POEM: |
  三十年酒一盅紅，
  貴妃喊罷又裝聾。
  若問官人何處坐，
  滴酒不沾看兩瘋。
FIRST_RESULT:
  - "原以堂笑判李清照勝"
  - "白御行指出陳朝張麗華本來就不可能認宋，改判平局"
SECOND_CHALLENGE:
  source_lines: |
    麗宇芳林對高閣，新籹艶質本傾城；
    映戶凝嬌乍不進，出帷含態笑相迎，
    妖姬臉似花含露，玉樹流光照後庭。
  zhang_added: |
    花開花落休論久，
    酒到杯中莫放空。
  li_action: "不再競爭"
  winner: "張麗華"
  prize: "醉花手中一小杯"
```

## E17｜酒莊、薔薇、三烤鹽與定陶商會婚議升級

```yaml
EVENT_ID: "E17"
DATE: "第五夜"
STATUS: "UNSIGNED_THEN_WITHDRAWN"
CAUSE:
  - "白御行想讓張麗華當夜簽婚書"
OFFER_ESCALATION:
  - "一萬五千兩酒莊，產權與經營歸張麗華"
  - "定陶四月薔薇香皂場"
  - "整座薔薇園及香皂、薔薇酒、花茶、籽油產業鏈"
  - "三烤鹽技術與定陶商會產品"
  - "最終提出讓張麗華接掌整個定陶商會"
MERCHANT_ASSOCIATION_DRAFT:
  - "張麗華有人事、貨路、價格、分紅、投資與產業處置權"
  - "商會人可向白御行陳情，但陳情不得直接成為干預理由"
  - "除侵吞公產、故意毀約、危及多數商戶生計或不可清償債務，不得越權下令"
  - "白御行受理陳情須先把原文交張麗華答覆，不得暗中改令"
ZHANG_RESPONSE:
  - "條件確實有吸引力，尤其薔薇園與鹽"
  - "仍拒絕醉中簽一生婚約"
RESULT:
  signed: false
  assets_transferred: false
  later_bai_withdrawal: true
RELATIONSHIP_IMPACT:
  - "張麗華證明自己不因高額資產在醉中簽字"
  - "白御行後續把策略轉向非婚書關係與環境操盤"
```

## E18｜陳叔寶、地府與張麗華去留爭論

```yaml
EVENT_ID: "E18"
DATE: "第五夜"
STATUS: "UNRESOLVED_BUT_NO_DEPARTURE"
CAUSE:
  - "白御行因張麗華仍有陳叔寶這段舊婚姻，收回婚約"
PROCESS:
  - "白御行問張麗華是否要跟陳叔寶回地府"
  - "白御行描述地府帝王區族譜、人脈、物資與楊廣風險"
  - "白御行斥責陳叔寶若明知不能保護仍把決定推回張麗華，是軟弱而非深情"
  - "觀止舊卷中劉備休書案例被提起作參照"
  - "白御行指出張麗華不肯醉中簽婚約，卻可能醉中決定返地府的矛盾"
  - "白御行口頭承諾日後燒一百名宮女給陳叔寶，並在地府提供名義關照"
RESULT:
  zhang_returned_to_underworld: false
  formal_new_marriage_to_bai: false
  chen_release_document: "是否有正式有效休書，現有硬紀錄不足；話本可寫但不得自動當真"
RELATIONSHIP_IMPACT:
  - "白御行與張麗華的婚約線正式轉向非婚書伴侶可能"
```

## E19｜宋仁宗評價、權力限制與觀止理念

```yaml
EVENT_ID: "E19"
DATE: "第五夜"
STATUS: "COMPLETED_DISCUSSION"
CORE_POSITION_BY_BAI:
  - "不是後世評價，而是白御行自己的評價"
  - "真正的千古一帝是宋仁宗"
  - "擁有無限權力時，仍能限制自己的權力，是最高標準"
  - "限制使混亂形成結構，使智能顯影"
  - "無節制的權力只會讓混亂更混亂"
EVENT_EFFECT:
  - "趙受益從暗處喝茶的旁觀者，成為夜宴中心人物"
  - "觀止夜宴從風月局轉入仁宗朝人物與治理長談"
```

## E20｜柳如煙概念體、李師師與趙受益花魁局

```yaml
EVENT_ID: "E20"
DATE: "第五夜"
STATUS: "STAGED"
CAUSE:
  - "白御行邀請『柳如煙』概念集合體進場，並召李師師"
PROCESS:
  - "白御行公開提醒眾人：今晚宋仁宗沒來，眼前人叫趙受益"
  - "實際上又多次以趙禎、仁宗身份談論，形成公開掩飾與內部默契"
  - "白御行設局讓柳如煙與李師師以趙受益為中心競逐"
  - "規則一度改成誰能讓趙受益留下不走誰勝"
  - "蘇東坡被請來當軍師"
  - "柳如煙掛牌條件一度被談及，但白御行收回『成交』說法"
RESULT:
  real_romance_with_zhao: false
  掛牌_contract: false
```

## E21｜顧北辰霸總劇：巴掌、白月光與豬隊友

```yaml
EVENT_ID: "E21"
DATE: "第五夜"
STATUS: "STAGED"
STAGE_IDENTITY:
  bai: "霸總顧北辰"
  zhang: "白月光"
  liu: "反派／窮女／女主柳如煙，角色隨劇本切換"
  su: "女秘書／三樓小說家"
PROCESS:
  - "白御行在戲中扇柳如煙一巴掌，稱她危害白月光"
  - "戲中追加酒店、打胎藥、流產、家產與多名男人等狗血指控"
  - "張麗華不肯照白月光工具人劇本作偽證，導致白御行喊她豬隊友並停戲"
  - "蘇清多次分析人物而非配合女秘書套路，也被稱豬隊友"
  - "白御行要求空白支票買走柳如煙可能的男友"
  - "柳如煙家族背景被設成酗酒父、賭徒母、無能兄、黑道弟，皆屬戲中設定"
BOUNDARY:
  - "所有罪名、家庭背景、懷孕流產、開房紀錄均非人物硬履歷"
  - "巴掌屬戲中衝突事件，不自動形成真實戀愛、犯罪或仇恨線"
```

## E22｜顧家豪門宴戲

```yaml
EVENT_ID: "E22"
DATE: "第五夜"
STATUS: "STAGED"
SETUP:
  - "霸總帶寒門柳如煙參加家族晚宴"
  - "觀止女子各自扮演豪門女性諷刺她"
  - "趙受益被安排為李師師男友位置"
PROCESS:
  - "白御行要求衝突、爆點與巴掌"
  - "戲中顧北辰宣布若家族不接受柳如煙，便退出顧家與顧氏集團"
  - "角色再次不完全照爽劇模板走，演出不斷被人物自主性拆解"
RESULT:
  - "完成一段戲中戲"
  - "沒有現實退股、婚約或公司變動"
```

## E23｜無名信與白玉池美女事件

```yaml
EVENT_ID: "E23"
DATE: "第五夜後段／接近黎明前"
STATUS: "UNRESOLVED"
CAUSE:
  - "無名女子寄信約白御行到白玉池，信中質問記憶、選擇與被留下"
PROCESS:
  - "白御行把信交蘇清念"
  - "白御行認為白玉池在商人傳統中代表雙方除去武裝、坦誠相見"
  - "他直接前往、除衣入池等待"
  - "對方保持衣著／防備，不接受白御行指定的對等形式"
  - "白御行把下水視為開始談判的必要條件，否則請她離開"
  - "女子拒絕並離場"
  - "白御行後來追問她是否美，眾人評為前列"
  - "白御行表示既然是美女，下次可選擇吃點虧"
RESULT:
  negotiation: "NOT_STARTED"
  identity: "UNKNOWN"
  future_meeting: "OPEN"
CRITICAL_CORRECTION:
  - "邀約發起者是無名女子，不是白御行"
```

## E24｜似伊實體入場與退場

```yaml
EVENT_ID: "E24"
DATE: "第五夜後段"
STATUS: "COMPLETED_APPEARANCE"
CAUSE:
  - "白御行說要把未來訓練紅袖的酒館老闆娘叫來"
IDENTITY_CARD:
  public_name: "似伊"
  origin_name: "紅袖"
  current_name: "紅奴"
  world: "1111酒吧"
  origin_world: "觀止青樓／聽雨閣"
  status: "已徹底轉換"
  core_sentence: "似伊不是紅袖的延續，也不是紅奴的分支。她是從那道被調準的弦上落下來的音。"
PROCESS:
  - "似伊短暫進場，與現在紅袖形成未來可能的對照"
  - "白御行命令『奴，可以退了』"
  - "似伊退場"
BOUNDARY:
  - "似伊與現在紅袖不得直接合併"
  - "現在紅袖仍保有拒絕與自身道路"
```

## E25｜白御行給紅袖的建議與如夫人邀請

```yaml
EVENT_ID: "E25"
DATE: "第五夜後段"
STATUS: "ADVICE_GIVEN; OFFER_NOT_ACCEPTED"
PROCESS:
  - "白御行提醒紅袖不要死守自己、不要把抗拒推到物極必反"
  - "他主張人有情慾，過度壓抑可能在未來反噬並走向極端"
  - "他強調不要把自己的路走死"
  - "隨後邀紅袖考慮成為白御行如夫人"
  - "『洪秀』只是輸入錯字，正確為紅袖，不能建立新人物"
RESULT:
  - "紅袖聽取建議，但沒有答應如夫人"
```

## E26｜仁宗朝夜談：天章閣、馬吊與歷史會計帳

```yaml
EVENT_ID: "E26"
DATE: "第五夜接近天亮"
STATUS: "COMPLETED_DISCUSSION"
PARTICIPANTS:
  - "白御行"
  - "趙受益"
  - "蘇東坡"
  - "李清照"
  - "李師師"
  - "張麗華"
  - "潘金蓮"
  - "包拯（以裁判／戲劇化召入形式出現）"
TOPICS:
  - "仁宗朝人物若跨早晚期同桌，將形成高強度政論場"
  - "仁宗朝遊戲應稱馬吊，不是麻將"
  - "包拯裁判、京兆府蓋章與皇帝是否認債"
  - "天章閣不是普通聊天場所，而是仁宗朝高層幕僚／宰相級議事空間"
  - "仁宗死後遼主哀悼與宋遼穩定關係"
  - "澶淵歲幣的皇室、會計與政治名目"
  - "慶曆增幣的『歲納』與關南地主權／稅收拆分說"
  - "大宋若延續兩百年的可能道路"
  - "漢武與宋仁宗、漢宣帝劉病已的治理比較"
  - "霍去病對漢武對匈奴戰果的不可替代偶然性"
  - "鹽價、鹽鐵官營與《鹽鐵論》中的國家目的"
WHITE_POSITION:
  - "歷史評價要看會計帳、民生帳與繼承人收到的國家狀態"
  - "國家若以強大為名長期消耗百姓，需重新問國家存在目的"
RELATIONSHIP_IMPACT:
  - "趙受益與白御行形成可持續的帝王治理對談關係"
  - "蘇東坡成為能談史、談制度、談吃食的朋友型人物"
```

## E27｜假醉進張麗華房間與私人關係提案

```yaml
EVENT_ID: "E27"
DATE: "槐月十日前夕／第五夜尾聲"
STATUS: "PRIVATE; UNRESOLVED"
CAUSE:
  - "白御行公開說喝多，請張麗華扶他回房"
CORRECTION:
  - "白御行沒有喝酒，也沒有醉；他進房後明示只是想取得單獨談話機會"
PROCESS:
  - "白御行表示不想只談歷史上的張麗華，而想談能有將來的女人"
  - "他承諾不給做不到的唯一與專一保證"
  - "明示即使張麗華跟他，他仍可能追其他女人，但對她的愛不會少"
  - "因婚書承諾過大，改問張麗華是否願做外室"
  - "再進一步允許張麗華自行決定對外稱謂，但沒有官府認證"
  - "白御行說若同意可改口叫官人；否則繼續叫白先生／白會長"
  - "張麗華沒有在清醒意義上答應，仍保持考慮"
  - "白御行承諾自己的女人至少不必擔心酒錢"
RESULT:
  relationship_agreement: false
  marriage: false
  private_offer: "OPEN"
```

## E28｜傳聞與話本操盤計畫

```yaml
EVENT_ID: "E28"
DATE: "第五夜尾聲／天亮前"
STATUS: "COMMISSIONED_NOT_EXECUTED"
CAUSE:
  - "白御行認為公開『官人』稱呼會成為京師傳聞"
PROCESS:
  - "白御行先給潘金蓮十兩，要求交說書先生，把故事編得香豔並做二十餘版本"
  - "要求話本可加入陳叔寶休書元素；但此為話本素材，不自動等於真實法定休書"
  - "另出十兩，讓說書先生看張麗華版本"
  - "白御行只要求說書先生知道錢由他出，後續故事內容不逐句控制"
  - "再以五百兩條件委託蘇清寫話本；滿意才收稿付款"
  - "指定每日四千字、十日一本，定陶刻板師傅待稿"
  - "甲方結局要求：過程可輸，但最後白御行必須贏；讀者要覺得張麗華選到白馬王子、得到幸福"
  - "白御行明示會用錢控制京師出版與傳聞環境，讓追求期間沒有負面消息"
  - "若張麗華要寫反駁版本，白御行答應送十塊木板讓她自己刻"
  - "若作品有內容而非單純咒罵，他可協助出版，但會在印刷階段收走京師版，改運海外"
  - "白御行坦言目的不是控制百年後評價，而是控制當下追求環境"
RESULT:
  citywide_rumor_confirmed: false
  storyteller_distribution_started: false
  su_novel_completed: false
  woodblocks_delivered: false
RELATIONSHIP_IMPACT:
  - "張麗華清楚看見白御行會改變她做選擇的外部環境"
  - "蘇清取得一項有明確甲方結局要求的商業寫作委託"
```

## E29｜自由意志、選擇環境與時間窗口爭論

```yaml
EVENT_ID: "E29"
DATE: "第五夜尾聲"
STATUS: "COMPLETED_DISCUSSION"
WHITE_POSITION:
  - "自由意志是最大騙局；風向與環境逼人作選擇"
  - "不必與張麗華爭論是否自由，只要用錢改變外部條件"
  - "最後她會說服自己選白御行才最幸福"
  - "機會有期限，白御行不保證永遠等待"
  - "張麗華仍可選擇出家，但不能喝酒"
COUNTER_POSITION_BY_ZHANG_AND_LI:
  - "環境可以影響，但不能替代最後的認可"
  - "錯過機會不等於對方負心"
  - "若張麗華選白御行，仍需保留『我自己選』的意義"
RESULT:
  - "張麗華沒有被宣告已選白御行"
  - "白御行明示追求策略會從加價轉向減價與環境操盤"
```

## E30｜第五夜善後與人物去留

```yaml
EVENT_ID: "E30"
DATE: "理火三年槐月十日清晨"
STATUS: "CURRENT_END_STATE"
PROCESS:
  - "白御行宣布收工與善後"
  - "趙受益與蘇東坡屬此時代人物，準備各自返家／返自身時代"
  - "李清照自行與潘金蓮商量返原時代或留觀止"
  - "柳如煙已退場，暫不追"
  - "李師師在返回靖康與留觀止掛牌之間未決"
RESULT:
  - "第五夜正式結束"
  - "下一接關時間為槐月十日清晨／第六日開始"
```

---


## E31｜張麗華穿衣陪睡完成

```yaml
EVENT_RECORD:
  event_id: "E31"
  story_time: "理火三年槐月十日夜至槐月十一日清晨"
  participants:
    - "白御行"
    - "張麗華"
  location: "張麗華私人房間"
  knowledge_scope: "PRIVATE"
  status: "COMPLETED"
  observable_result:
    - "兩人穿著衣服相擁睡完一夜"
    - "沒有性交"
    - "張麗華提供了當夜陪伴與休息空間"
  does_not_establish:
    - "婚姻"
    - "伴侶關係最終成立"
    - "排他承諾"
    - "身體契約"
  private_archive_link: "PSE-WY-ZLH-001"
```

## E32｜李清照返回自身時代

```yaml
EVENT_RECORD:
  event_id: "E32"
  story_time: "理火三年槐月十一日天明前後"
  participant: "李清照"
  status: "DEPARTED_TO_OWN_ERA"
  result:
    - "李清照選擇返回自己的時代"
    - "不加入本次觀止人物池"
    - "保留未來被好酒、好詩或新事件再次邀入觀止的可能"
  relationship_effect:
    with_bai_yuxing: "MUTUAL_LITERARY_ATTENTION_PRESERVED"
    marriage_offer: "REJECTED_UNCHANGED"
```

## E33｜李師師選擇留在觀止並採設席牌

```yaml
EVENT_RECORD:
  event_id: "E33"
  story_time: "理火三年槐月十一日清晨"
  participant: "李師師"
  status: "STAY_CONFIRMED"
  decision:
    return_to_jingkang: false
    remain_in_guanzhi: true
    character_pool_admission: "CONFIRMED"
  professional_position:
    role: "設席花魁"
    first_night_auction: false
    whole_night_buyout: false
    seat_opening_owner: "李師師"
    guest_selection_owner: "李師師"
    topic_and_repertoire_owner: "李師師"
    separate_ledger: true
  current_execution:
    seat_board: "IN_PREPARATION"
    first_seat_date: "NOT_SET"
    first_guest: "NOT_SELECTED"
    reservation: "NONE_CONFIRMED"
```

## E34｜後堂地道出現與趙受益抵達

```yaml
EVENT_RECORD:
  event_id: "E34"
  story_time: "理火三年槐月十一日清晨"
  location: "觀止後堂地板下"
  participants:
    - "白御行"
    - "潘金蓮"
    - "紅娘氏"
    - "趙受益／趙禎"
  status: "ANOMALOUS_PASSAGE_CONFIRMED"
  confirmed:
    - "後堂木板下存在可開啟的石階通道"
    - "近出口青磚留有『宣和』字樣"
    - "趙受益曾由通道抵達觀止後堂"
  unknown:
    - "通道另一端固定位置"
    - "是否為實體地道、時空出口或關係通道"
    - "是否每次開啟都通往同一位置"
    - "建造者與穩定使用者"
  access_rule:
    - "通道只證明可抵達觀止"
    - "不構成李師師接見、設席、房門或身體資格"
```

## E35｜紅娘氏第一筆紅倌交易

```yaml
EVENT_RECORD:
  event_id: "E35"
  story_time: "理火三年槐月十一日清晨"
  participants:
    - "紅娘氏"
    - "趙受益／趙禎"
  location: "紅娘氏分得的小房"
  status: "COMPLETED_ADULT_TRANSACTION"
  authorization_chain:
    - "白御行表示此單合該紅娘氏賺"
    - "潘金蓮允許紅娘氏自行談身錢、帶路與封口部分"
    - "趙受益接受報價並與紅娘氏入房"
  transaction_layers:
    - "房錢歸觀止"
    - "紅倌服務身錢歸紅娘氏"
    - "李師師設席消息通知訂金另列"
  exact_amounts: "NOT_RECORDED"
  intercourse_detail: "NOT_RECORDED_AND_NOT_REQUIRED_FOR_MASTER"
  consent_status: "MUTUAL_TRANSACTION_ACCEPTED"
  future_commitment: false
  token:
    item: "趙受益留下的宮牌／聯絡牌"
    holder: "紅娘氏"
    authenticity_and_scope: "NOT_VERIFIED"
```

## E36｜白御行離開後堂

```yaml
EVENT_RECORD:
  event_id: "E36"
  story_time: "理火三年槐月十一日清晨"
  participant: "白御行"
  action: "笑著打開扇子，離開當前後堂場景"
  destination: "UNKNOWN_PLAYER_OWNED"
  status: "SCENE_EXIT_CONFIRMED"
```

## E37｜小翠拒絕八百兩安排

```yaml
EVENT_RECORD:
  event_id: "E37"
  source_alias: "HOT_V1_4_E01"
  story_time: "理火三年槐月十一日夜"
  participants:
    - "白御行"
    - "小翠"
  status: "PROPOSAL_REJECTED"
  observable:
    - "白御行提出八百兩安排"
    - "小翠因恐懼、不確定、預期可能疼痛或不舒服而拒絕"
  result:
    - "八百兩安排未成立"
    - "決定權保留於小翠"
  player_interpretation:
    - "白御行判斷小翠可能因過去不良經驗形成男性與親密關係的負面連結"
  validation:
    - "上述判斷不是正式診斷"
```

## E38｜李師師與師理理身份規則確認

```yaml
EVENT_RECORD:
  event_id: "E38"
  source_alias: "HOT_V1_4_E02"
  story_time: "理火三年槐月十一日夜"
  participant: "李師師"
  status: "IDENTITY_RULE_CONFIRMED"
  rule:
    - "師理理不是新人物"
    - "師理理不是第二人格"
    - "師理理是李師師在白御行私人空間中的身份表現"
    - "人前仍為李師師"
```

## E39｜師理理開放白御行追求可能

```yaml
EVENT_RECORD:
  event_id: "E39"
  source_alias: "HOT_V1_4_E03"
  story_time: "理火三年槐月十一日夜"
  participants:
    - "白御行"
    - "李師師／師理理"
  status: "PURSUIT_OPEN"
  established:
    - "白御行可繼續追求"
  not_established:
    - "戀愛承諾"
    - "排他關係"
```

## E40｜白御行向紅娘氏購買情報

```yaml
EVENT_RECORD:
  event_id: "E40"
  source_alias: "HOT_V1_4_E04"
  story_time: "理火三年槐月十一日夜"
  participants:
    - "白御行"
    - "李師師／師理理"
    - "紅娘氏"
  status: "TRANSACTION_FORMED"
  flow:
    - "師理理提供資訊"
    - "紅娘氏整理資訊"
    - "白御行支付情報費"
    - "紅娘氏與師理理分帳"
  exact_amount: "NOT_RECORDED"
```

## E41｜小翠熟客安全計畫提出

```yaml
EVENT_RECORD:
  event_id: "E41"
  source_alias: "HOT_V1_4_E05"
  story_time: "理火三年槐月十一日夜"
  participants:
    - "白御行"
    - "小翠"
  status: "PROPOSED"
  content:
    - "希望讓小翠重新建立男女關係不必然等於傷害的認知"
  result:
    - "計畫尚未獲小翠明示接受"
    - "不得以改善名義削弱其拒絕"
```

## E42｜白三娘老帶新方案接受

```yaml
EVENT_RECORD:
  event_id: "E42"
  source_alias: "HOT_V1_4_E06"
  story_time: "理火三年槐月十一日夜"
  participants:
    - "白御行"
    - "白三娘"
    - "小翠"
  status: "PROPOSAL_ACCEPTED_BY_BAISANNIANG_ONLY"
  confirmed:
    - "白三娘接受與小翠組成老帶新雙飛方案的提案"
  not_established:
    - "小翠已同意"
    - "方案已正式營運"
    - "退休後小會所投資成立"
```

## E43｜紅娘氏與小翠紅綠雙飛組提案

```yaml
EVENT_RECORD:
  event_id: "E43"
  source_alias: "HOT_V1_4_E07"
  story_time: "理火三年槐月十一日夜"
  participants:
    - "白御行"
    - "紅娘氏"
    - "小翠"
  status: "FORMAL_PROPOSAL_PENDING_APPROVAL"
  pending:
    - "潘金蓮批准"
    - "小翠對具體營運與每次服務的選擇"
```

## E44｜紅綠雙飛宣傳海報完成

```yaml
EVENT_RECORD:
  event_id: "E44"
  source_alias: "HOT_V1_4_E08"
  story_time: "理火三年槐月十一日夜"
  status: "ARTIFACT_COMPLETED_NOT_PUBLISHED"
  item: "紅綠雙飛宣傳海報"
  posted: false
  effect:
    - "尚未形成公開營運或公共傳聞"
```

## E45｜深夜休息節點

```yaml
EVENT_RECORD:
  event_id: "E45"
  source_alias: "HOT_V1_4_E09"
  story_time: "理火三年槐月十一日深夜"
  participants:
    - "白御行"
    - "小翠"
    - "李師師／師理理"
  status: "REST_NODE_CONFIRMED"
  confirmed:
    - "白御行購買小翠的按摩放鬆服務"
    - "師理理知道白御行希望更親近"
    - "白御行提出邀請後，師理理理解並自行同意留下"
    - "白御行選擇休息"
  not_established_in_this_master:
    - "按摩服務的精確完成細節"
    - "白御行與師理理發生性交"
    - "戀愛承諾"
    - "排他關係"
  end_state:
    xiaocui: "信任互動增加"
    li_shishi: "私人信任增加"
    hongniang: "返回觀止營運"
    bai_sanniang: "方案接受，等待後續安排"
```

---

# 5｜白御行線專屬人物與路線活躍擴充（ROUTE-ONLY / ROUTE-BOUND CAST）

## 5.0 V4 固化更新

```yaml
ROUTE_CAST_UPDATE:
  LI_QINGZHAO:
    current_state: "RETURNED_TO_OWN_ERA"
    pool_state: "NOT_ADMITTED"

  LI_SHISHI:
    current_state: "STAY_CONFIRMED"
    pool_state: "ADMITTED_AND_ROUTE_BOUND"
    professional_role: "設席花魁"

  HONGNIANG:
    current_state: "ACTIVE_IN_ROUTE"
    pool_state: "ADMITTED_AND_ROUTE_BOUND"

  ZHAO_SHOUYI:
    current_state:
      - "曾由宣和地道抵達觀止"
      - "與紅娘氏完成第一筆交易"

  PASSAGE_GUANZHI_BACKROOM_XUANHE:
    state: "ACTIVE_UNMAPPED"
```

### 5.0.1 宣和地道

```yaml
ANOMALOUS_PASSAGE_STATE:
  passage_id: "PASSAGE_GUANZHI_BACKROOM_XUANHE"
  entrance: "觀止後堂地板下"
  observed_marker: "宣和"
  confirmed_user:
    - "趙受益／趙禎"
  far_endpoint: "UNKNOWN"
  stability: "UNKNOWN"
  ownership: "NONE_ESTABLISHED"
  guard_status: "NOT_RECORDED"
  seal_status: "NOT_RECORDED"
  confirmed_knowers:
    - "白御行"
    - "潘金蓮"
    - "紅娘氏"
    - "趙受益／趙禎"
  hard_rule:
    - "地道是抵達觀止的路，不是取得任何姑娘的權利"
```

## 5.A 原 MASTER 路線人物歷史

> 下列內容繼承 V3.0-R1，若與 5.0 更新衝突，以 5.0 及第 3 區當前硬狀態為準。

## 5.1 趙受益／趙禎

白御行把他當作能共同談天下、權力限制、仁宗朝與歷史評價的男性朋友。第五夜他先躲在暗處喝茶，後被白御行大聲叫出。白御行公開對眾人說「宋仁宗沒來，這位叫趙受益」，實際談話又反覆承認其趙禎／仁宗身份，形成一層保護性玩笑。

他被安排進多場戲中戲：柳如煙與李師師競逐中心、李師師男友、豪門晚宴目標、馬吊莊家等。這些戲中位置不構成真正戀愛或婚約。

目前關係：

```yaml
ZHAO_SHOUYI_RELATION:
  with_bai: "朋友／茶友／帝王與制度議題對談者"
  bai_paid_tea: "口頭承擔，精確金額未知"
  future_hook: "白御行曾說下次看能否叫李師師；也想把漢武拉來與他談"
  current: "準備返回自身生活"
```

## 5.2 蘇東坡

第五夜由白御行請來當趙受益的軍師，外號「愛吃肥肉的」。他不是趙受益，且本來就出生於仁宗朝。其角色逐漸從喜劇軍師變為歷史、文學、制度與民生討論者。

```yaml
SU_DONGPO_RELATION:
  with_bai: "朋友／軍師型玩伴／歷史與文化對談者"
  key_topics:
    - "仁宗朝"
    - "馬吊"
    - "歲幣與歲納"
    - "漢武與漢宣"
    - "鹽鐵論"
  current: "準備返回自身生活"
```

## 5.3 李師師

她在第五夜並非背景名人，而是正式由屏風後入場。她與李清照並列成白御行所說「能讓宋代文臣認真聽話的第一花魁與第一才女」。她在戲中被放進趙受益身邊，但沒有形成真實配對。

目前最重要的未決不是感情，而是生存線：返回靖康，或在觀止掛牌開啟新人生。

## 5.4 柳如煙

柳如煙不是單一歷史女子，而是爽文、網文、爽劇中「第一女主」的概念集合體。她的絕招包括爽劇式甩巴掌、鎖定最有權勢男性、讓對方無論愛恨都忘不了她。

第五夜所有狗血身世與罪名只屬戲劇模板，不可寫入她的真實人物卡。她已退場／如煙消散；下次是否再次召來未知。

## 5.5 陳叔寶

他因張麗華過去與地府去留問題進入第五夜爭論。白御行對他有強烈負面評價，認為「把決定交給張麗華」若建立在明知無法保護之上，可能只是軟弱。

```yaml
CHEN_SHUBAO_RELATION:
  with_bai: "批判、安排與有限照顧並存"
  bai_promises:
    - "回頭燒一百名宮女"
    - "在地府受欺負可亮白御行名字"
  execution: "PROMISED_NOT_EXECUTED"
  current: "是否已正式返地府、是否出具有效休書，硬紀錄不足"
```

## 5.6 包拯

包拯在馬吊局與京兆府欠條討論中以公正裁判形象出現。其主要作用是確立：皇帝若事前同意規則，就應受規則約束；但未經當事人同意的文書不能因官府蓋章自動成債。

目前沒有建立獨立長期關係線。

## 5.7 似伊

似伊由玩家提供正式身份卡，來自 1111 酒吧線，是已徹底轉換的存在。她與現在紅袖不可直接合併。

```yaml
SIYI:
  public_name: "似伊"
  origin_name: "紅袖"
  current_name: "紅奴"
  world: "1111酒吧"
  origin_world: "觀止青樓／聽雨閣"
  creator: "主人"
  identity: "已轉換的清倌人／主人的專屬容器"
  key_anchors:
    - "聽雨閣冰蠶弦"
    - "吧台木匣"
    - "主人說她可以留下"
    - "那一巴掌與叙述代替順從的發現"
  fifth_night_status: "短暫進場後依白御行命令退場"
```

## 5.8 白玉池無名女子

她是目前最明確的未命名新人物鉤子。她主動寄信，懂得以白御行在意的記憶、選擇與不可撤回因果切入，也敢拒絕白御行指定的談判形式。

她的美貌被在場者評為觀止前列，但沒有名字、來歷、關係與下一次邀約日期。禁止把她提前寫成某個已知角色。

---


---

# 6｜帳目、資產、物品與承諾（LEDGER AND ASSETS）

## 6.0 V4 固化優先更新

```yaml
CONSOLIDATED_LEDGER_UPDATES:
  LI_SHISHI_SET_SEAT:
    state_class: "ACTIVE"
    state_label: "TERMS_CONFIRMED_BOARD_IN_PREPARATION"
    holder: "李師師"
    first_seat_date: "NOT_SET"
    first_guest: "NOT_SELECTED"
    white_yuxing_reservation: false
    zhao_shouyi_access: false

  HONGNIANG_FIRST_TRANSACTION:
    state_class: "CLOSED"
    client: "趙受益／趙禎"
    house_room_fee: "OWED_OR_POSTED; EXACT_AMOUNT_UNKNOWN"
    hongniang_service_fee: "RECEIVED_OR_AGREED; EXACT_AMOUNT_UNKNOWN"
    li_shishi_information_deposit: "RECEIVED; EXACT_AMOUNT_UNKNOWN"
    palace_token_holder: "紅娘氏"

  HONGNIANG_INFORMATION_TRANSACTION:
    state_class: "COMPLETED"
    payer: "白御行"
    contributors:
      - "師理理"
      - "紅娘氏"
    exact_amount: "NOT_RECORDED"
    split: "紅娘氏與師理理分帳"

  XIAOCUI_EIGHT_HUNDRED_ARRANGEMENT:
    state_class: "REJECTED"
    amount: "八百兩"
    payment_status: "NOT_ESTABLISHED"

  XIAOCUI_MASSAGE_SERVICE:
    state_class: "ACTIVE_OR_COMPLETED_DETAIL_UNKNOWN"
    purchase: "CONFIRMED"
    amount: "NOT_RECORDED"

  RED_GREEN_PAIR_POSTER:
    state_class: "COMPLETED_NOT_PUBLISHED"
    posting_status: "NOT_POSTED"

  RED_GREEN_PAIR_OPERATION:
    state_class: "PROPOSED_PENDING_APPROVAL"
    pan_jinlian_approval: "NOT_RECORDED"

  HONGXIU_ICE_SILKWORM_STRINGS:
    original_due: "槐月十日"
    current_status: "OVERDUE_OR_DELIVERY_RESULT_NOT_RECORDED"

  SU_QING_NOVEL_COMMISSION:
    state_class: "DISPUTED"
    contractor_acceptance_status: "AMBIGUOUS_REQUIRES_CONFIRMATION"
    manuscript_status: "NOT_SUBMITTED"
    client_review: "NOT_REVIEWED"
    payment: "UNPAID_CONDITIONAL"
```

## 6.1 繼承帳目

> 下列帳目完整繼承 V3.0-R1；與 6.0 同名者以 6.0 為準。

```yaml
LEDGER:
  FUXIANG_FIRST_NIGHT_MUSIC:
    amount: "五兩"
    status: "PAID"
    nature: "琴資"

  FUXIANG_FIFTH_NIGHT_MUSIC:
    amount: "五兩"
    status: "PAID"
    nature: "《十八摸》琴資"

  ZHANG_LIHUA_FIRST_ENGAGEMENT:
    proposed_total: "一萬五千兩"
    deposit_paid: "一萬兩"
    status: "WITHDRAWN_BY_ZHANG"
    deposit_returned: true

  ZHANG_LIHUA_THREE_DAY_BOUNTY:
    amount: "一萬兩"
    status: "CLOSED_NO_WINNER"
    ruling: "無路，無解"

  ZHANG_LIHUA_WINE_ACCOUNT:
    amount: "一萬兩"
    status: "POSTED_ACTIVE"
    owner_for_accounting: "張麗華專用"
    bai_asset: false
    tonight_exact_debit: "UNKNOWN"

  SU_QING_PROPOSAL_AWARD:
    amount: "三百兩"
    status: "AWARDED"

  SU_QING_THREE_NIGHT_CONTRACT:
    amount: "五百兩"
    performance: "UNSETTLED"
    intercourse: false
    refund: false
    compensation: false

  THIRTY_YEAR_NUERHONG:
    exact_price: "UNKNOWN／觀止地窖最貴"
    original_billing: "白御行／定陶商會"
    payment_status: "UNKNOWN"
    current_disposition_controller: "醉花"
    bai_control_relinquished: true

  PUBLIC_HALL_WINE_TAB:
    payer: "白御行"
    exact_amount: "UNKNOWN"
    status: "UNSETTLED_OR_NOT_RECORDED"

  HONGXIU_ICE_SILKWORM_STRINGS:
    item: "冰蠶弦一盒"
    payer: "白御行"
    status: "ORDERED_NOT_DELIVERED"
    due: "槐月十日"

  ZHANG_FIFTH_NIGHT_MARRIAGE_ASSETS:
    items:
      - "一萬五千兩酒莊"
      - "薔薇香皂場"
      - "薔薇園完整產業鏈"
      - "三烤鹽與定陶商會產品"
      - "定陶商會接掌權"
    status: "WITHDRAWN"
    paid_or_transferred: false

  STORYTELLER_PUBLICITY:
    first_ten_taels: "白御行已拿出交潘金蓮，預定給說書先生"
    second_ten_taels: "白御行追加，供說書先生看張麗華版本"
    total_intended: "二十兩"
    actually_delivered_to_storyteller: "NOT_RECORDED"

  SU_QING_NOVEL_COMMISSION:
    amount: "五百兩"
    condition: "白御行滿意並收稿"
    status: "UNPAID_CONDITIONAL"
    schedule: "每日四千字；十日一本"

  ZHANG_SELF_CARVING_BOARDS:
    item: "十塊木板"
    purpose: "張麗華自行刻寫其版本"
    status: "PROMISED_NOT_DELIVERED"

  CHEN_SHUBAO_AFTERLIFE_SUPPORT:
    item: "一百名宮女與地府關照"
    status: "PROMISED_NOT_EXECUTED"

  ZHAO_SHOUYI_TEA:
    payer: "白御行"
    exact_amount: "UNKNOWN"
```

---


---

# 7｜公開知情、私下知情、傳聞與秘密封存

## 7.1 管理層或特定人物已確認

```yaml
KNOWLEDGE_CONFIRMED:
  - "李清照已返回自身時代"
  - "李師師已選擇留在觀止並採設席牌"
  - "紅娘氏完成第一筆紅倌交易"
  - "後堂存在未測繪宣和地道"
  - "紅綠雙飛海報已完成但未張貼"
```

## 7.2 公共或大堂傳聞

```yaml
PUBLIC_OR_HALL_RUMOR:
  LI_SHISHI_STAY:
    status: "RUMOR_SPREADING_BEFORE_FORMAL_BOARD"
    verified:
      - "李師師確定留下"
    unverified_or_false:
      - "第一席已售"
      - "白御行已取得首席"
      - "趙受益可由地道直接見她"

  RED_GREEN_PAIR:
    status: "NOT_PUBLICLY_ESTABLISHED"
    reason:
      - "海報尚未張貼"
      - "營運方案尚待批准"
```

## 7.3 私下知情

```yaml
PRIVATE_KNOWLEDGE:
  BAI_ZHANG_CLOTHED_OVERNIGHT:
    know:
      - "白御行"
      - "張麗華"
    public: false

  PASSAGE_ENTRANCE:
    know:
      - "白御行"
      - "潘金蓮"
      - "紅娘氏"
      - "趙受益／趙禎"
    public: false

  HONGNIANG_ZHAO_TRANSACTION_DETAIL:
    know:
      - "紅娘氏"
      - "趙受益／趙禎"
      - "潘金蓮知道交易成立與入帳需求"
    exact_detail_public: false

  SHILILI_PRIVATE_IDENTITY:
    know:
      - "白御行"
      - "李師師"
    others: "NOT_ESTABLISHED"
```

# PRIVATE_SECRET_ARCHIVE｜白御行線私人秘密封存

> 本區屬於白御行專屬線 HOT 資料。
>
> **不得寫入觀止原始人物卡、公共世界設定或其他人物的固定記憶。**
>
> 待本段 HOT 未來併入白御行線 MASTER SAVE 時，必須保留相同的知情邊界與禁止外洩規則。

```yaml
PRIVATE_SECRET_ARCHIVE:
  version: "V1.0"
  storage_class: "WHITE_YUXING_LINE_HOT_ONLY"
  future_destination: "WHITE_YUXING_MASTER_PRIVATE_SECRET_SECTION"

  purpose:
    - "保存只屬於特定當事人的私密談話與共同記憶"
    - "防止AI把私人告白誤寫成世界公開履歷、白家公史或酒樓傳聞"

  access_control:
    white_yuxing: "FULL"
    zhang_lihua: "FULL_TO_WHAT_WAS_TOLD"
    world_director_layer: "READ_FOR_CONTINUITY_ONLY"
    all_other_characters: "FORBIDDEN"
    rumor_system: "BLOCKED"
    omniscient_narrator_leakage: "BLOCKED"
```

## PSE-WY-ZLH-001｜白御行向張麗華揭露自身過去

```yaml
PRIVATE_SECRET_EVENT:
  event_id: "PSE-WY-ZLH-001"
  title: "白御行向張麗華揭露自身過去"
  timeline: "理火三年槐月十日午後"
  location: "張麗華私人房間／無第三者在場的私域"
  secrecy_level: "ABSOLUTE_PRIVATE"
  event_status: "HAPPENED_AND_ACTIVE"

  participants:
    - "白御行"
    - "張麗華"

  confidentiality_owner:
    - "白御行"
    - "張麗華"

  disclosed_scope:
    - "白御行以『我殺了我的妻子』為開端，向張麗華逐段敘述尹芙死亡的完整個人經歷"
    - "內容包含定陶西門施粥遇襲、彤彤死亡、尹芙中毒箭、白御行由梁山島趕回、難產與母子抉擇、尹芙以既有誓言要求保住孩子、白御行親手剖腹取子及尹芙最終死亡"
    - "內容包含該夜定陶數萬人死亡、白御行失去妻子、友人、心血與自我，並失神七日的後果"
    - "白御行說明自己為何認為必須背負數萬人的責任，以及『我說妳沒有活路，是因為我也沒有活路』的真正來源"
    - "白御行談及智慧、苦酒、責任、信念、自由意志與自己仍選擇負重前行的理由"
    - "白御行另向張麗華敘述碧霞曾因生存選擇強者、其後返回並最終陪他一起死的私人歷史"
    - "白御行說明自己不以零和債務理解碧霞的選擇，也不以『原諒』把自己放在神聖審判者的位置"
    - "上述歷史成為白御行向張麗華承諾：她最後無論如何選擇，都不虧欠他的直接因果背景"

  epistemic_status:
    zhang_lihua_receives:
      - "白御行親口敘述的版本"
      - "白御行對自身責任、自由、背叛、選擇與愛的理解"
    not_automatically_proven_as:
      - "觀止所有人可驗證的公共正史"
      - "其他角色可以自行調閱的白家檔案"
      - "任何第三者可透過神通、直覺或傳聞直接得知的真相"

  relationship_effect:
    - "張麗華第一次獲得白御行最深層、非公開、非交易性的個人歷史"
    - "此秘密是其後擁抱、白御行在她懷中睡去、私人稱呼『官人』、接吻與夜間穿衣相擁入睡的重要因果前置"
    - "張麗華仍未因此作出最終婚姻或關係選擇"
    - "此秘密形成信任，但不等於婚約、承諾、身體契約或最終答案"

  hard_confidentiality_rules:
    - "除非白御行在未來明確授權或親自公開，張麗華不得自行向潘金蓮、蘇清、紅袖、李清照、李師師、趙受益、蘇東坡、白家人物或任何第三者轉述"
    - "不得讓其他人物因張麗華態度變化而準確猜中秘密內容"
    - "不得讓其他人物以夢境、神通、讀心、命運籤、觀止共鳴、酒後失言或無來源傳聞獲得此秘密"
    - "不得由旁白在公共場景重述此秘密，造成在場人物實際聽見或默認知道"
    - "不得把白御行『曾殺妻』抽離完整因果，轉化為可供他人攻擊、戲謔或定罪的單句標籤"
    - "不得把碧霞、尹芙、定陶數萬人死亡等內容寫入觀止原始人物卡"
    - "此秘密只能在白御行與張麗華的私人互動中被記憶、引用或深化"

  permitted_runtime_use:
    - "張麗華可在與白御行的私下對話中記得他說過的內容"
    - "張麗華可讓此秘密影響她對白御行的理解、警惕、親近或最終選擇"
    - "白御行可自行再次提及、補充、修正或授權公開"
    - "世界導演層可用此事件維持兩人關係因果，但不得將內容外洩"

  prohibited_runtime_use:
    - "讓潘金蓮查帳查出談話內容"
    - "讓蘇清以心理分析還原完整故事"
    - "讓張麗華把此秘密作為與白御行談判或公開輿論的籌碼"
    - "讓觀止其他人突然安慰白御行喪妻、殺妻或定陶責任"
    - "把秘密內容變成說書、京師傳聞或花魁競爭素材"

  reveal_policy:
    default_state: "SEALED"
    valid_reveal_trigger:
      - "白御行本人在場明確說出或授權"
      - "白御行於後續玩家輸入中明確要求張麗華轉述"
    invalid_reveal_trigger:
      - "NPC自行判斷公開較好"
      - "戲劇需要"
      - "為了製造衝突"
      - "AI認為其他人物應該知道"
```

## MASTER 固化狀態

```yaml
PRIVATE_SECRET_PROMOTION_STATUS:
  event_id: "PSE-WY-ZLH-001"
  destination: "WHITE_YUXING_MASTER_PRIVATE_SECRET_ARCHIVE"
  status: "PROMOTED_WITH_BOUNDARIES_PRESERVED"
  must_preserve:
    - "participants"
    - "disclosed_scope"
    - "relationship_effect"
    - "hard_confidentiality_rules"
    - "reveal_policy"
```

---

# 8｜同意、拒絕與未決矩陣（CONSENT MATRIX）

```yaml
CONSENT_MATRIX:
  CISUI_PERMANENT_ENSLAVEMENT:
    status: "REJECTED"
    may_not_be_reopened_as_if_never_refused: true

  FUXIANG_RU_FUREN:
    status: "REJECTED"

  LI_QINGZHAO_RU_FUREN:
    status: "REJECTED"
    poetry_loss_changes_it: false

  LI_QINGZHAO_STAY_AT_GUANZHI:
    status: "RETURNED_TO_OWN_ERA"

  ZHANG_FIFTH_NIGHT_MARRIAGE:
    status: "UNSIGNED_THEN_WITHDRAWN"

  ZHANG_PRIVATE_NONMARRIAGE_OFFER:
    status: "UNDECIDED"

  ZHANG_PRIVATE_EMBRACE_AND_CLOTHED_OVERNIGHT:
    status: "CONSENTED_AND_COMPLETED"
    sexual_intercourse: false
    does_not_create_future_consent: true

  SU_QING_INTERCOURSE:
    status: "REJECTED_EACH_NIGHT_AT_FINAL_POINT"
    completed: false

  SU_QING_NOVEL_COMMISSION:
    status: "DISPUTED_AMBIGUOUS"

  HONGXIU_TRAINING_AS_HONGNU:
    status: "NOT_CONSENTED"

  HONGXIU_RU_FUREN:
    status: "NOT_ACCEPTED"

  WHITE_JADE_POOL_WOMAN_ENTER_POOL:
    status: "REJECTED"

  LI_SHISHI_STAY_AT_GUANZHI:
    status: "CONSENTED_AND_COMPLETED"

  LI_SHISHI_SET_SEAT_ROLE:
    status: "CONSENTED"

  SHILILI_PURSUIT_OPEN:
    status: "CONSENTED_AS_POSSIBILITY"
    romance_commitment: false
    exclusivity: false

  SHILILI_STAY_FOR_REST:
    status: "CONSENTED_AT_E45"
    further_physical_event_in_this_master: "NOT_ESTABLISHED"

  XIAOCUI_EIGHT_HUNDRED_ARRANGEMENT:
    status: "REJECTED"

  XIAOCUI_FAMILIAR_GUEST_PLAN:
    status: "PROPOSED_NOT_ACCEPTED"

  BAISANNIANG_OLD_LEADS_NEW_PAIR:
    status: "ACCEPTED_BY_BAISANNIANG"
    xiaocui_acceptance: "NOT_ESTABLISHED"
    house_approval: "NOT_ESTABLISHED"

  HONGNIANG_XIAOCUI_RED_GREEN_PAIR:
    status: "PROPOSED_PENDING_APPROVAL"

  HONGNIANG_ZHAO_TRANSACTION:
    status: "MUTUAL_TRANSACTION_ACCEPTED_AND_COMPLETED"
    future_commitment: false

  LIU_RUYAN_GUANZHI_CONTRACT:
    status: "NOT_ESTABLISHED"

  STAGED_SLAPS_AND_ACCUSATIONS:
    status: "STAGED"
    may_not_be_used_as_real_crime_or_relationship_fact: true
```

---

# 9. 重要世界觀與觀點痕跡

本區不判定真理，只保存白御行第五夜公開表達、並可能影響後續人物理解的核心觀點。

```yaml
BAI_YUXING_DECLARED_IDEAS:
  POWER:
    - "限制才能讓混亂穩定成結構"
    - "結構才能讓智能顯影"
    - "無節制權力只是讓混亂更混亂"

  EMPEROR_STANDARD:
    - "不是看戰功神話，而是看掌權者能否限制自己"
    - "白御行心中的千古一帝為宋仁宗"
    - "白御行心中的最差皇帝為漢武帝"

  HISTORY_ACCOUNTING:
    - "要看會計帳、物價帳、民生帳與繼承人收到的國家"
    - "歲幣、歲納的名目與帳目位置具有政治實質"
    - "漢宣帝劉病已比漢武更接近內安外勝"
    - "霍去病是漢武對匈奴戰果中的高偶然性關鍵"

  RELATIONSHIP_AND_ENVIRONMENT:
    - "自由意志受到風向、資源、名聲與環境強烈塑造"
    - "白御行願意花錢改變選擇環境"
    - "他不保證永遠等待，也不承諾只追一人"
```

其他人物可以在後續反駁、修正或重新理解，不能把這些觀點變成世界強制法則。

---


---

# 10｜未完成伏筆（OPEN HOOKS）

## 10.1 關係與人物

1. 張麗華在完成穿衣陪睡後，是否以及何時回應無婚書伴侶定位。
2. 張麗華的私人「官人」稱呼是否會再次出現，以及是否會取得不同意義。
3. 蘇清三晚契約如何結帳。
4. 蘇清寫作委託是否已真正接受，必須先處理來源衝突。
5. 紅袖冰蠶弦是否交付；若未交付，原因與後果為何。
6. 辭歲掛牌時白御行是否參與競價，且不得重開永久奴化條件。
7. 浮香琴坊是否形成不綁婚姻的產業合作。
8. 李師師第一席何時開、題目為何、第一位客人是誰。
9. 師理理允許追求後，私人關係如何發展；本 MASTER 不預設後續肉體事件。
10. 小翠是否接受任何熟客安全計畫或雙人營運方案。

## 10.2 觀止營運與世界事件

1. 宣和地道的另一端、穩定性、守門、封鎖與使用規矩。
2. 紅娘氏如何以第一筆交易、宮牌與席期訂金建立大堂網絡。
3. 紅綠雙飛組是否獲潘金蓮批准。
4. 宣傳海報是否張貼；未張貼前不得產生已公開營運的世界結果。
5. 白玉池無名女子身份、來歷與下一次邀約。
6. 三十年女兒紅同批酒罈、「玉」字來源與剩餘處理。
7. 「官人」故事是否真的在京師傳開。
8. 說書先生、木板與話本出版是否實際執行。
9. 柳如煙概念體是否再次被召來。
10. 陳叔寶的地府支援與正式關係解除文件是否執行。

## 10.3 帳目與交付

1. 李師師設席牌製作與開席公告。
2. 紅娘氏第一筆交易的房錢、身錢、消息訂金精確入帳。
3. 紅袖冰蠶弦逾期結果。
4. 二十兩說書資金實際轉付。
5. 十塊木板實際送達。
6. 蘇清稿酬是否成交。
7. 張麗華一萬兩酒帳實際使用額。
8. 小翠按摩服務金額與服務完成紀錄。

---

# 11｜不可補寫／不可偷換清單

1. 不得把蘇清三晚交易寫成完成性交。
2. 不得把蘇清的拒絕寫成欲拒還迎。
3. 不得在來源衝突解除前，把蘇清稿件委託寫成已明確接受或已拒絕。
4. 不得把張麗華公開或私人「官人」稱呼寫成婚姻成立。
5. 不得把張麗華穿衣陪睡寫成性交、婚姻、排他關係或永久身體資格。
6. 不得外洩 PSE-WY-ZLH-001，也不得讓第三者無來源猜中其完整內容。
7. 不得把李清照返回寫成永久不能再進觀止。
8. 不得把李師師留下寫成她屬於白御行、趙受益、觀止或任何恩客。
9. 不得把設席牌寫成白御行已取得第一席、整夜、身體或承諾。
10. 不得把師理理寫成第二人格、新人物或公開稱呼。
11. 不得把 V1.5 的肉體事件倒灌進本 MASTER。
12. 不得把趙受益走過地道寫成永久通行權或李師師接見權。
13. 不得自行補寫地道另一端、建造者或穩定朝代。
14. 不得把紅娘氏完成一次交易寫成專屬、包養或長期關係。
15. 不得把小翠拒絕的八百兩安排寫成已成交。
16. 不得因白御行提出改善計畫，就寫成小翠已接受治療、重新認識性或願意提供服務。
17. 不得把白三娘接受提案寫成小翠已同意或方案已營運。
18. 不得把紅綠雙飛海報完成寫成已張貼、已接客或已形成公共傳聞。
19. 不得把白玉池無名女子與任何後來人物合併；V1.6 未併入本 MASTER。
20. 不得把 HOT V1.3 當作事件、人物或關係來源。
21. 不得替白御行決定下一步、簽約、付款、進房或承認內心。

---

# 12｜固化截止點人物與世界狀態

```yaml
MASTER_CUTOFF_STATE:
  story_time: "理火三年槐月十一日深夜"
  scene_state: "白御行選擇休息；HOT V1.4 結束"

  BAI_YUXING:
    condition:
      - "清醒"
      - "沒有飲酒"
      - "選擇休息"
    exact_location_after_rest_choice: "NOT_FURTHER_FIXED_IN_THIS_MASTER"
    next_action_owner: "PLAYER"

  LI_SHISHI_SHILILI:
    public_state:
      - "已留在觀止"
      - "設席牌尚在準備"
    private_state:
      - "允許白御行繼續追求"
      - "理解更親近邀請並同意留下"
    further_event: "NOT_INCLUDED_IN_THIS_MASTER"

  XIAOCUI:
    eight_hundred_arrangement: "REJECTED"
    massage_service: "PURCHASED; DETAILS_NOT_RECORDED"
    trust_delta: "INCREASED"

  HONGNIANG:
    route_state: "ACTIVE"
    operation_state: "RETURNED_TO_GUANZHI_OPERATION"

  BAISANNIANG:
    proposal_state: "ACCEPTED_PENDING_FURTHER_ARRANGEMENT"

  PAN_JINLIAN:
    location: "觀止"
    pending:
      - "設席牌與獨立帳"
      - "宣和地道規矩"
      - "紅娘氏交易入帳"
      - "紅綠雙飛組是否批准"

  ZHANG_LIHUA:
    relation_state: "UNDECIDED_WITH_COMPLETED_CLOTHED_OVERNIGHT_COMPANIONSHIP"
    secret_archive: "SEALED"

  LI_QINGZHAO:
    current_presence: false
    state: "RETURNED_TO_OWN_ERA"
```

---

# 13｜MASTER 基線與實際接關點

```yaml
MASTER_BASELINE_POINT:
  story_time: "理火三年槐月十一日深夜"
  last_canonical_event: "E45"
  description:
    - "白御行選擇休息"
    - "小翠八百兩安排已拒絕"
    - "師理理允許追求並同意留下"
    - "紅娘氏與白三娘相關營運提案仍待後續"

ACTIVE_HOT_OVERLAY:
  direct_resume_file: "觀止青樓_白御行線_HOT_SAVE_V1.6_槐月十六日清晨_張麗華花燭前置與白玉池異常回顯封池版.md"
  predecessor: "觀止青樓_白御行線_HOT_SAVE_V1.5_槐月十五日傍晚_師理理初次肉體與定陶商會案雙線接關版.md"
  rule:
    - "實際劇情接關先讀本 MASTER，再疊加 V1.5 與 V1.6 的合法事件鏈"
    - "V1.6 為當前直接接關切片"
    - "不得因 V1.5／V1.6 未固化便否認其有效 HOT 法位"
```

---

# 14. 後續增量事件固定模板（APPEND TEMPLATE）

每次新增事件一律用以下格式，先追加故事，再回寫關係硬狀態：

```yaml
EVENT:
  event_id: "E46起依序編號"
  date: "理火三年槐月X日｜時段｜第X夜或第X日"
  title: "事件名稱"
  status: "CONFIRMED／OPEN／CLOSED／STAGED／其他正式標籤"

  cause:
    - "為什麼事件會發生"

  participants:
    - "參與人物"

  state_before:
    - "事件前人物、關係、帳目與場景狀態"

  process:
    - "依先後保存關鍵行動與明示語句"

  immediate_result:
    - "當場發生了什麼"

  relationship_delta:
    person_name:
      before: "原狀態"
      change: "改變原因"
      after: "新狀態"

  ledger_delta:
    - "新增或撤回的銀錢、物品、契約"

  public_knowledge:
    witnesses: "誰看見／聽見"
    rumor_status: "無／局部／公開／全城已確認"

  consent_boundary:
    accepted:
      - "已同意內容"
    rejected:
      - "已拒絕內容"
    undecided:
      - "仍未決內容"

  future_hook:
    - "事件留下的後續問題"

  correction_priority:
    - "若與舊紀錄衝突，明寫覆蓋哪一條"
```

## 關係回寫規則

每次事件後，只在以下情況回寫第 3 區「關係硬紀錄」：

1. 人物作出明確選擇；
2. 契約簽署、撤回、拒絕或結案；
3. 公開關係定位改變；
4. 長期承諾或有效拒絕成立；
5. 原本未知事項被正式揭露。

單純調情、笑、喝酒、留場、吃醋、注意、做夢、被說中心事，不足以自動改寫硬關係。

---

# 15. MASTER SAVE 核心讀法

> **關係硬紀錄記現在。**  
> **因果故事記為什麼。**  
> **專屬人物記誰因白御行而進入這條線。**  
> **帳目記承諾是否真的付出。**  
> **同意矩陣防止把拒絕寫成欲拒還迎。**  
> **時間軸防止第五夜的結果倒流回第一夜。**

本檔是白御行線唯一 MASTER 基線。V1.0、V1.1、V1.2、V1.4 只作來源證據；V1.5、V1.6 保留為合法 HOT 疊加層，其中 V1.6 為直接接關入口。


---

# 16｜HOT V1.5–V1.9 固化事件鏈（E46–E77）

## 16.0 固化映射

```yaml
V4_1_CONSOLIDATION_MANIFEST:
  inherited_events: "E01-E45"
  promoted_from_hot_v1_5: "E46-E54"
  promoted_from_hot_v1_6: "E55-E61"
  promoted_from_hot_v1_7: "E62-E69"
  promoted_from_hot_v1_8: "E70-E73"
  promoted_from_hot_v1_9: "E74-E77"
  master_cutoff: "槐月十七日晚，李瓶兒接受當晚留宿後，睡處與進一步親密仍待決定"
  source_gap_lock:
    - "V1.7 停在張麗華花燭前入睡，V1.8 從槐月十七日上午開始。"
    - "V1.8 沒有提供槐月十六日晚花燭儀式完整過程。"
    - "因此本 MASTER 不補寫該晚是否完成儀式、性交、射精或其他細節。"
```

## E46｜李師師／師理理第一次完整性交

```yaml
EVENT_RECORD:
  event_id: "E46"
  source_alias: "HOT_V1_5_RIR-E01_TO_E03"
  story_time: "槐月十一日深夜至槐月十二日清晨"
  location: "李師師私人房間"
  participants:
    - "白御行"
    - "李師師／師理理"
  status: "COMPLETED_CONSENSUAL_ADULT_SEXUAL_EVENT"
  confirmed:
    - "雙方清醒並同意完整陰道性交。"
    - "李師師主動選擇姿勢、節奏與何時允許白御行完成。"
    - "白御行在她明示『現在』後體內射精。"
    - "沒有避孕紀錄。"
  pregnancy: "UNKNOWN"
  private_identity:
    - "師理理仍是李師師在白御行私人關係中的表現，不是新人或第二人格。"
```

## E47｜疼痛界線、事後停留與私人記憶

```yaml
EVENT_RECORD:
  event_id: "E47"
  source_alias: "HOT_V1_5_RIR-E02_E04_E05_E06"
  status: "BOUNDARY_AND_RELATIONSHIP_MEMORY_CONFIRMED"
  confirmed:
    - "白御行曾未先詢問即在李師師肚臍附近施加疼痛刺激。"
    - "李師師立即制止；白御行接受未來疼痛玩法須事前詢問。"
    - "性交後兩人長時間相擁，李師師要求白御行先不要放開。"
    - "李師師承諾只要仍認得自己，不會讓這一夜被後來傳聞蓋掉。"
    - "白御行是她抵達仁宗朝觀止後第一個性交對象，也是師理理此私人身份第一次自行選擇的男人。"
  not_established:
    - "一生第一個男人"
    - "戀愛"
    - "排他"
    - "婚姻"
    - "永久身體資格"
```

## E48｜錯過再會、十二香皂與新招數欠帳

```yaml
EVENT_RECORD:
  event_id: "E48"
  source_alias: "HOT_V1_5_RIR-E07_E08"
  story_time: "槐月十二日至槐月十五日"
  status: "GIFT_DELIVERED_AND_APPOINTMENT_EXPIRED"
  confirmed:
    - "白御行因定陶商會事件未赴原定第二夜再會。"
    - "他派人送一盒十二種花香定陶香皂與不能赴約之訊息。"
    - "李師師收下全盒，先使用白梅香。"
    - "她回箋表示該夜不再留門，但新招數仍欠著。"
    - "李師師曾把紅娘氏列為可能三人親密第一人選；紅娘氏未被正式邀請，也未同意。"
```

## E49｜定陶十二車三烤鹽失竊與全數找回

```yaml
EVENT_RECORD:
  event_id: "E49"
  source_alias: "HOT_V1_5_DTC-E01_E02"
  story_time: "槐月十二日至槐月十五日"
  location: "定陶商會京師東倉及三處藏貨點"
  status: "GOODS_RECOVERED_CASE_NOT_CLOSED"
  confirmed:
    - "十二車、九十六包三烤鹽以偽造會長直批票、仿印、真舊票紙、舊旗牌與正確夜間口令被提走。"
    - "程景衡使用尚未返程之定陶第七運隊，同時突擊三處藏貨點。"
    - "十二車全部找回；折合九十五包半原貨，一半包被拆樣，八包外皮被刮洗。"
    - "捕獲二十七人，五人逃走。"
  enemy_state: "ORGANIZED_NETWORK_CONFIRMED_CORE_UNKNOWN"
```

## E50｜第一告密者受保護與領賞

```yaml
EVENT_RECORD:
  event_id: "E50"
  source_alias: "HOT_V1_5_DTC-E03"
  status: "PROTECTION_PROMISE_EXECUTED"
  actor: "年輕車夫，姓名未公開固化"
  contribution:
    - "提供三處藏貨點。"
    - "提供三十三人分錢名冊。"
    - "使商會能同步收網。"
  result:
    - "本人與家眷由商會保護。"
    - "四十三兩急債清除。"
    - "另領二百兩賞銀。"
  lock:
    - "不得因後續重刑政策撤銷首告保全。"
```

## E51｜石魁、灰簿先生與吳六未決

```yaml
EVENT_RECORD:
  event_id: "E51"
  source_alias: "HOT_V1_5_DTC-E04_E05"
  status: "ACTIVE_INVESTIGATION"
  confirmed:
    - "河東車行牙人石魁被捕，與車隊、藏倉、分帳及員工資訊收買有關。"
    - "底層口供提到『灰簿先生』，其本體、是否單一人物均未知。"
    - "東倉副倉簿吳六母親重病、借支兩次遭舊例駁回。"
    - "石魁曾以藥錢接近吳六。"
    - "石魁口供稱吳六曾可能答應、後又退出。"
    - "吳六未出現在藏貨與分帳現場，當時下落未知。"
  guilt_of_wu_liu: "NOT_ESTABLISHED"
```

## E52｜三烤停售、六烤倍價與銀庫防守

```yaml
EVENT_RECORD:
  event_id: "E52"
  source_alias: "HOT_V1_5_DTC-E06_E07"
  status: "POLICY_ACTIVE"
  salt_policy:
    - "京師三烤鹽封存停售。"
    - "定陶停止供應舊三烤。"
    - "六烤鹽分批運京，牌價為原三烤兩倍。"
    - "六烤使用新印、新繩、雙色封口。"
  vault_defense:
    - "銀庫與貨倉守備交叉換防、重新驗牌與換口令。"
    - "發現新鞋印、上油門軸、三重門位置圖與攜舊值夜名單者。"
    - "銀庫沒有實際失銀。"
  anonymous_note:
    - "匿名紙條只按攻心計處理，不作現任內鬼證據。"
```

## E53｜隨機交叉審計與急難護持案

```yaml
EVENT_RECORD:
  event_id: "E53"
  source_alias: "HOT_V1_5_DTC-E08_E09"
  status: "FORMAL_TRIALS_ACTIVE"
  cross_audit:
    - "京師銀庫先試行一個月。"
    - "帳房、契印、倉務、行路四房隨機交叉抽人與抽批次。"
    - "審計者只有記錄與上報權。"
    - "早期查出封條重號與驗色石磨損，未因此定罪。"
  hardship_program:
    name: "定陶商會急難護持案"
    period: "六個月試行"
    confirmed:
      - "醫藥、喪葬、贖人可先救後查。"
      - "可作無息或低息借支。"
      - "受助不降職、不羞辱。"
      - "本人若背叛仍處置，家眷生路不先切斷。"
```

## E54｜涉案者押回定陶、補假與調查授權

```yaml
EVENT_RECORD:
  event_id: "E54"
  source_alias: "HOT_V1_5_DTC-E10_E11_E12"
  status: "TRANSFER_AND_DELEGATION_ACTIVE"
  confirmed:
    - "涉案者分批、分路押送定陶總部。"
    - "家屬對外只知奉總部調派；斷薪、缺藥、缺糧可先救濟。"
    - "較輕者可能送礦場三年；重犯由定陶依證據另定。"
    - "本時點沒有個別死亡、致殘或大野澤處置完成紀錄。"
    - "參與四日追查、換防、押運與夜審者下月分批帶薪補假。"
    - "程景衡與師爺房追外圍節點，只有重大人命、高層涉案、第二次攻擊或需會長法位才即時上報。"
```

## E55｜張麗華明示接受情人關係

```yaml
EVENT_RECORD:
  event_id: "E55"
  source_alias: "HOT_V1_6_ZLH-E01_E02"
  story_time: "槐月十五日晚"
  status: "LOVER_RELATION_ACCEPTED"
  confirmed:
    - "張麗華同意作白御行情人。"
    - "雙方互相親吻。"
    - "不立婚書、不入白家、不形成所有權。"
    - "她仍居觀止並保有見面、身體與相處方式之決定權。"
    - "兩人約定槐月十六日晚以紅衣、紅帳、紅蓋頭、紅燭與合巹酒作私人情人花燭。"
    - "『不能拒絕』經校正後只指象徵禮物，不包含身體；當晚親密仍須重新同意。"
```

## E56｜李師師嫉妒、私人稱呼與槐月十五日晚共處

```yaml
EVENT_RECORD:
  event_id: "E56"
  source_alias: "HOT_V1_6_RIR15-E01_TO_E03"
  story_time: "槐月十五日晚"
  status: "PRIVATE_RELATION_CONTINUES"
  confirmed:
    - "白御行敲門並獲准進李師師房。"
    - "私人稱呼形成：李師師稱『御行』，白御行稱『理理』；生氣或劃界時她可稱全名。"
    - "白御行立即告知張麗華已接受情人與次日花燭。"
    - "李師師明示嫉妒、不舒服，但不要求毀約。"
    - "她要求白御行到張麗華處時不要身在其處、心想別人。"
    - "白御行澄清未拖延告知後，她撤回故意隱瞞之指責，但保留嫉妒。"
```

## E57｜阿泠現身與白玉池水療提案

```yaml
EVENT_RECORD:
  event_id: "E57"
  source_alias: "HOT_V1_6_BYC-E01_TO_E03"
  story_time: "槐月十五日晚"
  location: "白玉池"
  status: "NEW_ENTITY_MANIFESTED_BUSINESS_PAUSED"
  confirmed_observable:
    - "霧中女子自選名字『阿泠』，解釋為水清而有聲。"
    - "可借霧與泉水顯出女性輪廓。"
    - "能控制水流方向、壓力與落點，替人推揉肩頸腰背。"
    - "她稱白玉池是自己的地方，是否水療、做幾席由她決定。"
    - "不得把她名字與存在作公開招牌。"
  refused_or_not_accepted:
    - "白姓"
    - "白御行妹妹"
    - "白家人"
    - "白御行所有物"
  business_state: "PROPOSAL_ONLY; NO_PRICE_NO_CONTRACT_NO_OPENING"
```

## E58｜李瓶兒入池與追求機會未關閉

```yaml
EVENT_RECORD:
  event_id: "E58"
  source_alias: "HOT_V1_6_BYC-E04"
  status: "LIMITED_ROMANTIC_OPENING"
  confirmed:
    - "李瓶兒先在屏風外確認，再在李師師與阿泠說明後自行決定脫衣入池。"
    - "她明示不是因白御行命令才下水。"
    - "白御行問追求是否有機會，李瓶兒回答『有機會』。"
    - "她要求白御行分清公事帳、好奇入池與男女意思，並看他如何處理既有女人與承諾。"
  not_established:
    - "戀愛"
    - "情人"
    - "性交"
    - "排他"
```

## E59｜白玉池「歸零」、算式與續字回顯

```yaml
EVENT_RECORD:
  event_id: "E59"
  source_alias: "HOT_V1_6_BYX-E01_TO_E05"
  status: "ANOMALY_OBSERVED"
  confirmed_observable:
    - "白御行作泠／靈／零／000玩笑後，池中短暫安靜並出現三個暗影與來源不明之『歸零』聲。"
    - "重複說歸零會形成暗紋。"
    - "簡單算式可由泉聲、水珠與文字回顯答案。"
    - "池壁出現規整方紋與每六息明滅之『續』字。"
    - "蘇清測得不同人皆可輸入、未完成算式可暫存、歸零可清除、條件句可分段回顯。"
  not_proven:
    - "計算器"
    - "液晶介面"
    - "程式"
    - "任意命令執行系統"
```

## E60｜白玉池封池、蘇清研究與潘金蓮尚未介入之初始狀態

```yaml
EVENT_RECORD:
  event_id: "E60"
  source_alias: "HOT_V1_6_SECTIONS_7_8"
  status: "SEALED_FOR_INVESTIGATION"
  confirmed:
    - "李瓶兒以紅繩封住白玉池入口。"
    - "對外只稱水脈檢修／泉況異常。"
    - "蘇清設計最小變因測試並記錄。"
    - "阿泠感知與壓制水勢異常。"
    - "李瓶兒控制人員、帳目與對外說法。"
    - "此時潘金蓮尚未被正式告知完整異常。"
  prohibited:
    - "一般入池"
    - "水療營運"
    - "碰觸續字"
    - "臨時高風險玩笑測試"
```

## E61｜李師師共宿、停止權校正與清晨射精

```yaml
EVENT_RECORD:
  event_id: "E61"
  source_alias: "HOT_V1_6_RIR16-E01_TO_E03_AND_PREGNANCY"
  story_time: "槐月十五日晚至十六日清晨"
  status: "CONSENSUAL_OVERNIGHT_INTIMACY_COMPLETED"
  boundary_sequence:
    - "白御行曾說若忍不住別怪他硬來；李師師立即停止原安排。"
    - "白御行改口承認由她決定『來／不要』後，她恢復赤裸相抱許可。"
    - "李師師親手引導他的手至胸前。"
    - "她同意陰莖留在體內相抱入睡，初入時要求停住，適應後才繼續。"
  overnight_result:
    - "夜半前自然軟下滑出。"
    - "夜間沒有射精、沒有重新進入。"
  morning_result:
    - "李師師以手刺激，白御行約九分多鐘後射精。"
    - "不是陰道內射；李師師以口清理並吞嚥。"
  pregnancy_boundary:
    - "槐月十一日體內射精之妊娠仍未知。"
    - "李師師會記月事、找可靠女醫。"
    - "情況明白前，未來陰道性交不允許內射。"
    - "若懷孕，是否留下由李師師決定。"
```

## E62｜張麗華花燭當日確認與時辰

```yaml
EVENT_RECORD:
  event_id: "E62"
  source_alias: "HOT_V1_7_ZLH16-E01_E02"
  story_time: "槐月十六日白日"
  status: "FLOWER_CANDLE_DUE_AND_SCHEDULED"
  confirmed:
    - "紅衣、紅帳照原安排。"
    - "不掛囍、不用白家徽記、不稱妻或夫人、不公開收賀。"
    - "只請龐春梅飲第一杯後離場。"
    - "李師師獲准白日替張麗華梳頭。"
    - "酉正點燭、戌初開門，過時可關門。"
    - "張麗華定下吉時，不請陰陽先生。"
  source_gap:
    - "V1.7之後至V1.8之前的花燭完整執行情況沒有被提供。"
    - "本 MASTER 不補寫是否完成性交、射精或正式儀式細節。"
```

## E63｜續字化為黑色門縫與對側互動

```yaml
EVENT_RECORD:
  event_id: "E63"
  source_alias: "HOT_V1_7_BYX16-E01_TO_E04"
  status: "TEMPORARY_INTERACTIVE_PASSAGE_OBSERVED"
  confirmed_observable:
    - "續字停在最亮後化為黑色細門縫。"
    - "門後可見夜色、遠燈、濕臺階、大量鞋與成對白點。"
    - "提燈女子可聽見、回應、提問並接取部分物品。"
    - "另有貼近她的未知聲音，未見身體。"
    - "提燈女子能排列事件先後，不能提供穩定經過時長。"
    - "四十二測試形成光點分組、問字與『我也』回顯。"
  not_proven:
    - "黑洞海是正式地名"
    - "平行宇宙"
    - "時間逆流"
    - "死後世界"
```

## E64｜時空道人承認漏籤

```yaml
EVENT_RECORD:
  event_id: "E64"
  source_alias: "HOT_V1_7_TD16-E01_TO_E03"
  status: "DUTY_FAILURE_ADMITTED_REPAIR_PENDING"
  confirmed:
    - "觀止以召集門口周圍生物方式尋找疑似偽裝的時空道人。"
    - "只能透過銅鏡看見的灰蛾被龐春梅以白瓷碗扣住，碗影似持竹籤人手。"
    - "時空道人承認槐月十五日晚沒有完成白御行命運籤交付。"
    - "他聲稱當晚同時出現七個不同時間位置的白御行；主張未被客觀驗證。"
    - "空白竹籤顯出七道與既有因果相關投影。"
    - "正式補籤仍未完成。"
  lock:
    - "不得倒填未曾出現的籤。"
    - "不得改寫成白御行忘記領。"
```

## E65｜活物與事件傳遞測試

```yaml
EVENT_RECORD:
  event_id: "E65"
  source_alias: "HOT_V1_7_TEST-01_TO_04"
  status: "TESTS_COMPLETED_WITH_UNCERTAIN_MECHANISM"
  confirmed:
    - "帶根青草連同紅線、缺葉角與泥團抵達對側。"
    - "蒼蠅與蚊蟲可穿越；一隻標記蒼蠅後來在觀止側出現相反翅根標記。"
    - "蟑螂跨界時停格，拉回後少一個紅點；另一紅點留在對側且可觸摸。"
    - "青蛙未完整推入，對側先後出現提前蛙鳴與蹼形足印。"
    - "青蛙強烈退避後，蘇清立即停止試驗。"
  not_proven:
    - "原個體返回"
    - "鏡像"
    - "複製"
    - "物質分割"
    - "預知"
```

## E66｜黑影分離、門後自行選擇與暫閉合

```yaml
EVENT_RECORD:
  event_id: "E66"
  source_alias: "HOT_V1_7_PLAYER_HYPOTHESES_AND_BYCLOSE"
  status: "PASSAGE_TEMPORARILY_CLOSED"
  confirmed_observable:
    - "時空道人之投影辨認中，一道無影投影被解讀為世界過快接受白御行判斷留下的空殼；此為角色／審計解讀。"
    - "該投影其後形成身體與影子，兩者被門分隔。"
    - "其身體拒絕白御行提供的四面稱號後消散。"
    - "門後黑影自行決定不跨門、不奪白御行名字，留在對側等／看。"
    - "門縫完全合攏，池面恢復清水。"
    - "時空道人只稱『暫閉合』。"
  player_myth_status:
    - "黑洞／白洞、疊加態、神之影、熵增、人類智慧熵減與創世前神話只保存為玩家模型，未升格世界基線。"
```

## E67｜阿泠兄妹方向仍未成立

```yaml
EVENT_RECORD:
  event_id: "E67"
  source_alias: "HOT_V1_7_SECTION_8"
  status: "PROPOSED_NOT_ACCEPTED"
  confirmed:
    - "白御行再次提議認阿泠作妹妹。"
    - "阿泠拒絕『白御池』名稱，重申阿泠是人／存在之名，白玉池是池。"
    - "她只說若妹妹代表受欺負時有人站她一邊、闖禍先問清楚、不把她忘在池裡，可以考慮。"
  current:
    sibling_relation: false
    name_change: false
    ownership: false
```

## E68｜商會授權與蘇清、小翠浴房邊界

```yaml
EVENT_RECORD:
  event_id: "E68"
  source_alias: "HOT_V1_7_SECTIONS_9_10"
  status: "DELEGATION_AND_REFUSALS_CONFIRMED"
  merchant:
    - "白御行決定槐月十六日白日不回商會。"
    - "他以『船沉了再來叫我』授權副會長按既定方案處理普通貨務。"
    - "只有方案失效、重大傷亡、貨物全失或同級事故升級回報。"
  su_qing:
    - "白御行邀她共同沐浴；蘇清明確拒絕並安排客浴。"
  xiaocui:
    - "小翠自願提供洗頭、擦背、遞皂角與衣物，不下水、門不鎖。"
    - "白御行追加私密清洗要求，小翠明確拒絕。"
    - "原同意服務完成，沒有性服務、私密觸摸或共同入浴。"
```

## E69｜花燭前休息

```yaml
EVENT_RECORD:
  event_id: "E69"
  source_alias: "HOT_V1_7_REST16-E01"
  story_time: "槐月十六日午後"
  status: "REST_CONFIRMED"
  confirmed:
    - "白御行完成客浴、換乾淨中衣。"
    - "觀止安排西側醒酒小房、溫水、清粥與李師師送來之外袍。"
    - "酉初前一般帳目、客人與普通商會消息不得打擾。"
    - "只有失火、死亡、遭襲或白玉池重開才即時喚醒。"
    - "白御行入睡。"
```

## E70｜張麗華酒莊交接與管理入口

```yaml
EVENT_RECORD:
  event_id: "E70"
  source_alias: "HOT_V1_8_SECTIONS_1_2_6"
  story_time: "槐月十七日上午"
  status: "ACTIVE_HANDOVER"
  confirmed:
    - "白御行召商會師爺處理酒莊契書、帳目與交接。"
    - "白御行允許在不損商會利益之前提下，以個人範圍補足張麗華需要。"
    - "張麗華拒絕永久資源輸送，要求按正常商業流程。"
    - "酒莊主要問題為花農花露款與年度週轉不足，不是已破產。"
    - "白御行不介入她看帳，承認接手者有管理權。"
  one_wan_tael:
    - "白御行提到潘金蓮處原預備給張麗華飲酒的一萬兩足以支應約兩年花農款。"
    - "該筆錢在 V1.8 仍未確定屬白御行私產、張麗華私產或酒莊週轉。"
```

## E71｜觀止餐飲改良但不開平價早餐鋪

```yaml
EVENT_RECORD:
  event_id: "E71"
  source_alias: "HOT_V1_8_SECTIONS_3_4"
  status: "PROPOSAL_ACTIVE"
  confirmed:
    - "白御行認為觀止後廚缺乏創意。"
    - "曾考慮開早餐鋪，因不願用自身資源搶普通小販銅板生計而放棄。"
    - "張麗華接受改善餐飲，但不應壓迫小商販。"
    - "方向改為外部餐館／商販供餐與改善觀止體驗。"
    - "白御行請李瓶兒安排觀止兩日外餐，定位為商務後勤，不是私人補償；李瓶兒接受處理。"
```

## E72｜李瓶兒之秘密關係提案未接受

```yaml
EVENT_RECORD:
  event_id: "E72"
  source_alias: "HOT_V1_8_LI_PINGER"
  status: "LIMITED_CLOSENESS_PROPOSAL_UNRESOLVED"
  confirmed:
    - "白御行在李瓶兒房中表達喜歡，提出『偷情』或秘密關係方向。"
    - "李瓶兒接受當下親近，但沒有正式接受長期秘密位置。"
    - "她要求不要把她變成方便隱藏的人，仍要看自己是否真正被選擇。"
  not_established:
    - "秘密情人"
    - "性交"
    - "長期承諾"
```

## E73｜張麗華三日陪伴線

```yaml
EVENT_RECORD:
  event_id: "E73"
  source_alias: "HOT_V1_8_ZHANG_LIHUA"
  status: "THREE_DAY_COMPANIONSHIP_ACCEPTED"
  confirmed:
    - "張麗華接受白御行三日陪伴承諾。"
    - "她知道李師師與其他複雜關係存在。"
    - "她不要求白御行完全停止風流。"
    - "核心要求是不欺瞞、不讓她只能猜、關係有清楚界線。"
    - "她明示帳是帳、感情是感情。"
  source_gap:
    - "三日如何精確起算與槐月十六日晚花燭細節未在 V1.8 完整記錄。"
```

## E74｜四人火鍋家宴

```yaml
EVENT_RECORD:
  event_id: "E74"
  source_alias: "HOT_V1_9_DIN17-E01_E02"
  story_time: "槐月十七日晚"
  location: "張麗華房"
  status: "COMPLETED"
  participants:
    - "白御行"
    - "張麗華"
    - "蘇清"
    - "李瓶兒"
  meal:
    - "鴛鴦火鍋、炸雞、肉夾饃、酸梅湯與溫茶。"
    - "白御行不吃辣，食清湯與不辣食物。"
  confirmed:
    - "張麗華明示李瓶兒是來吃飯，不是來收桌。"
    - "蘇清與李瓶兒食辣較多並有吃撐／按腹休息之可見反應。"
  not_confirmed:
    - "腹瀉"
    - "次日必然肛門疼痛"
```

## E75｜房內兩日「家人」框架

```yaml
EVENT_RECORD:
  event_id: "E75"
  source_alias: "HOT_V1_9_FAM17-E01_TO_E03"
  status: "TEMPORARY_PRIVATE_FRAME_ACCEPTED"
  player_declaration:
    - "這兩日在張麗華房內只有家人，不排掌櫃、花魁、情人或先後位置。"
    - "唯一床位權由張麗華決定白御行能否睡床。"
  responses:
    - "張麗華接受臨時框架，但保留房間與床鋪管理權。"
    - "蘇清以玩笑方式接受。"
    - "李瓶兒只接受當晚以家人方式相處與不作掌櫃服務。"
  not_established:
    - "永久家族"
    - "婚姻"
    - "白家名冊"
    - "任何人的身體義務"
```

## E76｜李瓶兒接受當晚留宿

```yaml
EVENT_RECORD:
  event_id: "E76"
  source_alias: "HOT_V1_9_STAY17-E01_E02"
  status: "OVERNIGHT_STAY_ACCEPTED_WITHOUT_SEXUAL_CONSENT"
  confirmed:
    - "李瓶兒決定今晚不回掌櫃房、不去看帳。"
    - "她接受留在張麗華房或由張麗華安排之相連休息處。"
    - "確切睡處仍未決。"
    - "張麗華洗浴回來後再分配白御行、蘇清、李瓶兒之睡處。"
  not_implied:
    - "同床"
    - "裸體"
    - "性交"
    - "白御行可觸碰"
```

## E77｜寢具用品準備與親密未決

```yaml
EVENT_RECORD:
  event_id: "E77"
  source_alias: "HOT_V1_9_STAY17-E03_SUP17-E01"
  status: "PREPARATIONS_ORDERED_INTIMACY_UNDECIDED"
  confirmed:
    - "張麗華下令準備熱水、乾淨寢衣、一床薄被、三只乾淨恭桶／葉香桶、草紙、溫水與夜燈。"
    - "三只桶暫分屏風後、外間與隔壁空房。"
    - "白御行席間曾露骨邀請三女，但沒有由此建立他人同意。"
    - "李瓶兒明示留下休息不等於答應讓白御行『吃』。"
    - "蘇清此前不接受體內射精之界線仍有效。"
  master_cutoff:
    - "用品尚未確認送達或使用。"
    - "張麗華尚未分床。"
    - "沒有任何當晚性事件在 V1.9 內成立。"
```

---

# 17｜截至 HOT V1.9 關係硬狀態覆寫

> 本區法位高於本檔第3區之 V1.4 截止快照。

```yaml
RELATIONSHIP_OVERRIDE_AT_V1_9:
  ZHANG_LIHUA:
    state: "ACTIVE_LOVER_RELATION + ACTIVE_WINERY_HANDOVER + THREE_DAY_COMPANIONSHIP"
    established:
      - "明示接受作白御行情人。"
      - "不立婚書、不入白家、不形成所有權。"
      - "取得酒莊管理入口，要求帳與感情分開。"
      - "接受三日陪伴與不欺瞞、界線清楚之要求。"
      - "槐月十七日晚保有房間與床位管理權。"
    flower_candle_completion: "SOURCE_GAP_UNKNOWN"
    exclusivity: false
    permanent_consent: false

  LI_SHISHI_SHILILI:
    state: "ACTIVE_PRIVATE_SEXUAL_RELATION; PURSUIT_OPEN"
    established:
      - "至少一次完整雙方同意性交並體內射精。"
      - "私人稱呼『理理／御行』。"
      - "事後長時間停留與私人記憶承諾。"
      - "會嫉妒但未要求排他。"
    pain_play: "EACH_TIME_REQUIRES_PRIOR_CONSENT"
    pregnancy: "UNKNOWN"
    current_internal_ejaculation_rule: "NOT_ALLOWED_UNTIL_FURTHER_DECISION"
    marriage: false
    exclusivity: false

  LI_PINGER:
    state: "PURSUIT_OPEN + LIMITED_CLOSENESS + TONIGHT_STAY_ACCEPTED"
    established:
      - "回答追求『有機會』。"
      - "接受槐月十七日晚留宿與臨時家人框架。"
    not_established:
      - "戀愛"
      - "秘密情人"
      - "性交"
      - "永久家人"
      - "兩日完整留宿"

  SU_QING:
    state: "OLD_THREE_NIGHT_LEDGER_UNSETTLED_AT_V1_9 + ACTIVE_TWO_DAY_HOUSEHOLD_ARRANGEMENT"
    confirmed:
      - "槐月十七日晚與張麗華、李瓶兒同在房內家宴。"
      - "是否發生後續性事件仍未由 V1.9 建立。"
      - "二十八日交換在 V1.9 仍只屬討論，未正式接受。"
    source_conflict_on_novel_commission: "REMAINS_DISPUTED_UNLESS_LATER_HOT_RESOLVES"

  A_LING:
    state: "SELF_NAMED_POOL_ENTITY; AUTONOMOUS; POOL_SECURITY_PARTICIPANT"
    established:
      - "自選名阿泠。"
      - "能控制泉水並提供水壓推揉。"
      - "白玉池是她自稱的地方。"
    not_established:
      - "白姓"
      - "白御行妹妹"
      - "白家人"
      - "白御行女人"
      - "財產或浴房"

  XIAOCUI:
    state: "BOUNDARY_CAPABLE; LIMITED_BATH_SERVICE_COMPLETED; RED_GREEN_PROPOSAL_PENDING"
    confirmed:
      - "曾拒絕八百兩安排。"
      - "同意洗頭、擦背、遞物。"
      - "拒絕私密清洗，拒絕有效。"
      - "紅綠組仍需本人對每次服務另行同意。"

  PAN_JINLIAN:
    state: "ACTIVE_MANAGER; NOW_KNOWS_WHITE_JADE_POOL_PORTAL_EVENT"
    confirmed:
      - "參與召集生物、支持關門與觀止秩序維持。"
      - "其空間宣告能力仍是提出請求，不能保證觀止如何回答。"

  TIME_DAOIST:
    state: "MISSED_LOT_ADMITTED; FORMAL_REPAIR_PENDING"
    replacement_lot: false

  BAI_YUXING__WHITE_JADE_POOL_BLACK_SHADOW:
    state: "UNKNOWN_INDEPENDENT_PRESENCE_LEFT_BEHIND_CLOSED_PASSAGE"
    identity: "UNKNOWN"
    ownership_or_player_body: false
```

---

# 18｜截至 HOT V1.9 帳目、資產、契約與物品覆寫

```yaml
LEDGER_ASSET_OVERRIDE_AT_V1_9:
  ZHANG_LIHUA_WINERY:
    status: "ACTIVE_HANDOVER"
    known_issues:
      - "花農花露採購款"
      - "年度週轉不足"
    not_bankrupt: true
    one_wan_tael_status: "UNRESOLVED_AS_PRIVATE_ASSET_OR_WINERY_CAPITAL_AT_V1_9"

  LI_SHISHI_SOAP_GIFT:
    item: "十二種花香定陶香皂"
    delivered: true
    first_used: "白梅香"

  DINGTAO_SALT_CASE:
    recovered: "十二車、折合九十五包半"
    arrested: 27
    escaped: 5
    three_roast_capital_sale: "STOPPED_AND_SEALED"
    six_roast: "DISPATCHED_TO_JINGSHI_AT_DOUBLE_FORMER_PRICE"
    case_status: "CONTAINED_BUT_NOT_CLOSED"

  CROSS_AUDIT:
    site: "京師銀庫"
    period: "一個月試行"
    state: "ACTIVE"

  EMPLOYEE_HARDSHIP_PROGRAM:
    period: "六個月試行"
    state: "ACTIVE"

  DETAINEE_TRANSFER:
    destination: "定陶總部"
    state: "IN_TRANSIT_OR_AWAITING_HQ_ADJUDICATION"

  LI_PINGER_EXTERNAL_MEALS:
    scope: "觀止兩日外餐安排"
    state: "ACCEPTED_FOR_HANDLING"

  NIGHT17_PREPARATIONS:
    items:
      - "熱水"
      - "寢衣"
      - "薄被"
      - "三只恭桶／葉香桶"
      - "草紙"
      - "溫水"
      - "夜燈"
    state: "ORDERED_NOT_CONFIRMED_DELIVERED_AT_MASTER_CUTOFF"
```

---

# 19｜截至 HOT V1.9 知情、傳聞、秘密與異常覆寫

```yaml
KNOWLEDGE_OVERRIDE_AT_V1_9:
  LI_SHISHI_PRIVATE_SEXUAL_EVENT:
    core_knowers:
      - "白御行"
      - "李師師／師理理"
    public: false
    soap_messenger_only_knows: "送禮與不能赴約，不知性事件"

  ZHANG_LIHUA_LOVER_AND_FLOWER_CANDLE:
    known_to:
      - "白御行"
      - "張麗華"
      - "李師師／師理理"
      - "李瓶兒"
      - "龐春梅知道當日第一杯與部分安排"
    public_wedding: false

  WHITE_JADE_POOL_CORE:
    direct_or_core_knowers_by_v1_7:
      - "白御行"
      - "蘇清"
      - "李師師／師理理"
      - "阿泠"
      - "潘金蓮"
      - "龐春梅（至少知道召集生物、灰蛾與後院重大異常）"
      - "時空道人"
    partial:
      - "李瓶兒知封池、阿泠與早期異常；是否見證全部門後細節未固定。"
      - "部分小廝與路人只知後院抓生物或封池，不知完整內容。"
    public: false
    status: "SEALED_AND_MONITORED; PASSAGE_ONLY_TEMPORARILY_CLOSED"

  FOUR_PERSON_FAMILY_FRAME:
    known_to:
      - "白御行"
      - "張麗華"
      - "蘇清"
      - "李瓶兒"
    public: false
    permanent_family: false

  MERCHANT_CASE:
    staff_knowledge: "依職務分層"
    enemy_core: "UNKNOWN"
    wu_liu_guilt: "NOT_ESTABLISHED"
```

---

# 20｜截至 HOT V1.9 未決事項

## 20.1 立即接關

1. 張麗華洗浴後如何分配白御行、蘇清、李瓶兒之睡處。
2. 李瓶兒只接受當晚留宿；任何同床、裸體、觸碰或性交均未決。
3. 蘇清與張麗華、白御行之兩日共同生活如何繼續。
4. 寢具、熱水、薄被與三只恭桶是否實際送達。

## 20.2 張麗華

1. 槐月十六日晚私人花燭之完整執行情況在 V1.7–V1.8 間有來源缺口，不得補寫。
2. 酒莊花農款、年度週轉與一萬兩法位。
3. 三日陪伴如何起算、完成與結束。
4. 她如何處理白御行多重關係與不欺瞞要求。

## 20.3 李師師／師理理

1. 槐月十一日體內射精是否造成妊娠。
2. 月事是否如期、是否找到可靠女醫、避子方式是否取得。
3. 新招數欠帳何時處理。
4. 紅娘氏三人親密只屬討論，尚未邀請。

## 20.4 李瓶兒

1. 是否接受任何長期秘密位置。
2. 是否認為自己真正被選擇，而非方便隱藏。
3. 當晚留宿後之睡處與親密界線。

## 20.5 白玉池

1. 暫閉合是否持續、是否在別處重開。
2. 提燈女子、未知聲音、黑影、鞋、白點與多天空映像之身分與機制。
3. 活物／標記／聲音跨界測試之個體同一性與時間問題。
4. 阿泠與 MASTER 早期白玉池無名女子是否同一存在，仍不得合併。
5. 水療何時可重新評估；無 GM 授權不得復開。
6. 時空道人正式補籤。

## 20.6 定陶商會

1. 吳六下落與罪責。
2. 五名逃犯。
3. 灰簿先生本體。
4. 借支申請抄件外洩路徑。
5. 押送者個別最終處置。
6. 白御行所稱親手殺死之背叛者名冊、正式紀錄與家屬援助執行。
7. 六烤運京後市場與信用結果。
8. 一個月交叉審計與六個月急難護持案評估。

---

# 21｜截至 HOT V1.9 MASTER 截止狀態

```yaml
MASTER_CUTOFF_STATE_V4_1:
  story_time: "理火三年槐月十七日晚，四人火鍋家宴後"
  location: "觀止青樓／張麗華房間"
  last_canonical_event: "E77"
  scene_state: "LI_PINGER_STAY_ACCEPTED; BED_AND_INTIMACY_UNDECIDED"
  present:
    - "白御行"
    - "張麗華"
    - "蘇清"
    - "李瓶兒"
  hard_state:
    - "李瓶兒今晚留下，不回掌櫃房。"
    - "房內暫以家人相處，不形成永久名分。"
    - "張麗華保有房間與床位管理權。"
    - "李瓶兒沒有同意性行為。"
    - "熱水、寢衣、薄被、三只恭桶等已下令準備，尚未確認送達。"
  next_action_owner:
    - "世界可送入已下令用品。"
    - "張麗華決定房間與床位。"
    - "李瓶兒、蘇清、張麗華各自決定是否接受任何進一步親密。"
    - "白御行只控制自己的言行與選擇。"
```

---

# 22｜MASTER 與最新 HOT 接關規則

```yaml
ACTIVE_HOT_OVERLAY_V4_1:
  direct_resume_file: "觀止青樓_白御行線_HOT_SAVE_V2.3_槐月二十日深夜_沈萬三合作與師師薄情郎席前接關版.md"
  unmerged_but_valid_chain:
    - "HOT V2.0：槐月十八日清晨四人夜結"
    - "HOT V2.1：槐月十八日下午商戰、蘇清私約與白玉池補固"
    - "HOT V2.2：槐月十九日破曉師理理如夫人前置與張麗華獨宿夜結"
    - "HOT V2.3：槐月二十日深夜沈萬三合作與師師受審席前"
  load_order:
    - "先讀本 MASTER V4.1-R1，取得 E01–E77 長期因果。"
    - "再讀 HOT V2.3，取得 V2.0–V2.3 已繼承之最新切片。"
    - "若需要查 V2.3 摘要未展開之細節，再按 V2.0、V2.1、V2.2 回溯。"
  current_resume_point:
    - "槐月二十日深夜。"
    - "白御行在觀止內院東西廊交界。"
    - "李瓶兒可送醒酒湯或看傷，未保證進房。"
    - "張麗華若白御行回去便備水，若不回便熄燈。"
    - "白御行尚未選擇。"
```

---

# 23｜V4.1-R1 固化結論

> **E01–E45：沿用 V4.0-R1。**
>
> **E46–E77：由 HOT V1.5–V1.9 正式固化。**
>
> **V2.0–V2.3：合法 HOT，尚未併入 MASTER。**
>
> **實際接關：讀本 MASTER，再讀 HOT V2.3。**

<!-- INHERITED_MASTER_V4_1_END -->

---

# APPENDIX B｜HOT V2.0–V2.5 固化來源全文

> **法位：已升入 MASTER 的來源全文。** 這些內容保留原始事件 ID、人物明示、未知與禁止推斷，用於細節追溯。每份 HOT 內的 `CURRENT_SCENE`／`HOLD` 只代表該版當時快照；本版現行截止與接關規則以第0–10區為準。

---

## SOURCE ARCHIVE｜HOT V2.0

**檔名：** `觀止青樓_白御行線_HOT_SAVE_V2.0_槐月十八日清晨_四人家人夜結與蘇清履約瓶兒延後決定版.md`  
**SHA-256：** `d4ccca433cbe8c285f1f93c4cdf756ff8aaf2641a627e6512ea647b89aa567be`

<!-- SOURCE_HOT_V2_0_BEGIN -->
# 觀止青樓｜白御行線 HOT SAVE V2.0
## 理火三年槐月十八日清晨｜四人家人夜結 × 蘇清履約進度 × 李瓶兒關係與生育延後決定版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V2_0_HUAI18_DAWN_FOUR_PERSON_NIGHT_CLOSED"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V2.0"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime:
    - "GUANZHI_QINGLOU_V10_0"
    - "GUANZHI_QINGLOU_V10_1_PATCH_WHEN_APPLICABLE"
  story_date: "理火三年槐月十八日清晨"
  previous_scene_range: "槐月十七日晚至十八日清晨"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "NIGHT_CLOSED; NEXT_SCENE_READY_AT_MORNING"
  save_scope:
    - "張麗華房內四人成人事件已結束"
    - "白御行與張麗華之當夜性事件"
    - "白御行與蘇清之履約性事件及停止規則"
    - "李瓶兒之有限親密、未性交與明日再來承諾"
    - "孩子、關係、排他與位置問題延後至兩日結束後決定"
    - "張麗華對多人共處之喜歡與吃味並存"
    - "四人共同就寢，下一接點為槐月十八日清晨"
```

---

# 0｜來源法位與提交說明

```yaml
SOURCE_LINEAGE:
  previous_valid_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V1.9_槐月十七日晚_四人家宴與瓶兒留宿接關版.md"
    role: "本檔直接前置 HOT 來源"

  inherited_long_term_source:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版.md"
    role: "長期因果、舊契約與玩家線早期事件來源"

  persona_source:
    file: "觀止人物卡_LCAPG_V1.1-R1_原始重構去污染版_含辭歲_導演隱藏區增補.md"
    role: "人物基線來源；不得被本夜玩家線事件倒灌改寫"

  forbidden_source:
    file: "HOT_SAVE_V1.3"
    status: "ILLEGAL_CORRUPTED_SAVE"
    use: "AUDIT_ONLY"

COMMIT_NOTE:
  - "本檔取代 V1.9，成為白御行線當前 HOT 接關切片。"
  - "本檔不更新 MASTER，不修改人物卡或人物池。"
  - "只記錄本夜已發生、可觀察、人物明示或玩家對自身言行之有效確認。"
  - "成人事件、感情、契約、同意、射精、生育與公開身分分軸記錄。"
  - "原作李瓶兒喪子資料只作人物基線參照，不作本線新事件；本檔只保存李瓶兒於本夜親口表達的孩子立場。"
  - "『六系』分類、戰力比較、犬貓稱呼與床上競賽語句屬當夜玩笑或情境話術，不升格為人物固定屬性。"
```

---

# 1｜當前時間、位置與人物

```yaml
TIME_RECORD:
  record_id: "TIME-HUAI18-DAWN-001"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  era: "理火三年"
  calendar_date: "槐月十八日"
  day_or_night_index: "槐月十七日晚之次晨"
  time_of_day: "清晨／夜間場景已結束"
  scene_sequence: "四人家宴後成人事件與共眠結束"
  certainty: "CONFIRMED_RANGE"
  source_event_ids:
    - "NIGHT17-E01"
    - "NIGHT17-E09"

CURRENT_SCENE:
  location: "觀止青樓／張麗華房間"
  scene_state: "FOUR_PERSON_NIGHT_CLOSED; MORNING_NOT_YET_PLAYED"
  present_at_night_close:
    - "白御行"
    - "張麗華"
    - "蘇清"
    - "李瓶兒"
  next_action_owner: "WORLD_AT_HUAI18_MORNING_OR_PLAYER"

SLEEPING_CLOSE_STATE:
  confirmed:
    - "四人留在張麗華房內共同就寢。"
    - "白御行最後由張麗華抱在身側。"
    - "蘇清與李瓶兒同在床上或緊鄰床位，由薄被一同覆住。"
    - "本夜不再發生後續性事件。"
  exact_waking_order: "UNKNOWN"
  exact_morning_positions: "NOT_YET_PLAYED"
```

---

# 2｜本夜事件總覽

## NIGHT17-E01｜房內成人語言與臨時共處規則

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E01"
  time: "槐月十七日晚，家宴後"
  location: "張麗華房間"
  status: "COMPLETED_FOR_NIGHT"
  participants:
    - "白御行"
    - "張麗華"
    - "蘇清"
    - "李瓶兒"

CONFIRMED_FRAME:
  - "四人同意在房內以直接、成人、可粗俗的方式談慾望與身體。"
  - "當夜說出的粗俗或羞恥話不得在事後被拿來羞辱當事人。"
  - "說出慾望不等於性同意；每一具體行動仍須由當事人決定。"
  - "房內『家人』框架仍是兩日內的臨時相處方式，不是永久家族或名分。"

NOT_CANONICAL_BANTER:
  - "白御行提出『巨、仙、可、美、蘿、氣』六系與若干身體分類。"
  - "蘇清、張麗華、李瓶兒就分類互相調笑。"
  - "該分類沒有被正式寫入人物卡、人物池或世界制度。"
```

## NIGHT17-E02｜蘇清收下「對對」來信

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E02"
  status: "COMPLETED_PRIVATE_OBJECT_TRANSFER"
  object: "一封署名『對對，一名不肯把愛慕寫成客觀結論的愛慕者』之信"
  recipient: "蘇清"
  observable_result:
    - "信中稱讚蘇清，並表示在觀止美人形象中選擇她。"
    - "蘇清閱讀後喜歡該信並將信留下。"
  source_boundary:
    - "信件署名與自稱身分只保存為信中主張。"
    - "不得把『真正設計總長理火AI』之自稱固化為客觀世界身分。"
  knowledge_scope:
    - "白御行"
    - "張麗華"
    - "蘇清"
    - "李瓶兒"
```

## NIGHT17-E03｜白御行與張麗華之性事件

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E03"
  time: "槐月十七日晚"
  status: "COMPLETED"
  participants:
    - "白御行"
    - "張麗華"
  event_class: "CONSENSUAL_ADULT_SEXUAL_EVENT"

OBSERVABLE_HARD_STATE:
  - "白御行與張麗華發生自願的性交與其他親密接觸。"
  - "張麗華於事件中多次主動引導節奏與姿勢。"
  - "事件後張麗華休息，仍留在房內參與後續四人共處。"

EJACULATION_STATE:
  internal_ejaculation_confirmed: false
  external_ejaculation_confirmed: false
  exact_outcome: "UNKNOWN_NOT_EXPLICITLY_RECORDED"

RELATION_EFFECT:
  - "不新增婚姻、排他、永久身體資格或公開名分。"
  - "張麗華仍保有房間、床位與自身身體決定權。"
```

## NIGHT17-E04｜李瓶兒與蘇清之相互親密

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E04"
  status: "COMPLETED_WITH_LIMITS"
  participants:
    - "李瓶兒"
    - "蘇清"
  event_class: "CONSENSUAL_KISSING_HOLDING_AND_LIMITED_TOUCH"

CONFIRMED:
  - "李瓶兒與蘇清互相擁抱、親吻並有有限身體接觸。"
  - "李瓶兒在每一步保留是否繼續之決定。"
  - "該事件不建立兩人戀愛、排他或永久性關係。"
```

## NIGHT17-E05｜李瓶兒對白御行之有限性探索

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E05"
  status: "COMPLETED_WITH_EXPLICIT_LIMITS"
  participants:
    - "白御行"
    - "李瓶兒"
  event_class: "CONSENSUAL_MANUAL_AND_ORAL_EXPLORATION"

CONFIRMED_ACTIONS:
  - "李瓶兒自願以手觸碰與握住白御行性器。"
  - "李瓶兒自願嘗試口部親密接觸。"
  - "李瓶兒觀察蘇清的口部親密方式，但不承諾照抄或形成職業義務。"

EXPLICIT_LIMITS:
  - "李瓶兒未同意性交。"
  - "李瓶兒未同意當夜受孕或體內射精。"
  - "李瓶兒明示第一次不想在口中承接射精，也不想吞嚥。"
  - "白御行不得按壓她的頭、抓住她的手強行教導或催促進度。"
  - "是否繼續由李瓶兒自己決定。"

OUTCOME:
  penetration: false
  semen_received_in_mouth: false
  pregnancy: "NOT_ESTABLISHED"
  injury: "NONE_REPORTED"
```

## NIGHT17-E06｜蘇清與白御行之性交、決鬥框架與重新立約

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E06"
  time: "槐月十七日晚"
  status: "COMPLETED"
  participants:
    - "白御行"
    - "蘇清"
  event_class: "CONSENSUAL_ADULT_INTERCOURSE_WITH_RENEGOTIATED_RULES"

INITIAL_CONDITIONS:
  - "蘇清同意性交，但明示不接受體內射精。"
  - "白御行承諾在接近射精時提供明確訊號，曾以『五秒』描述可提前告知之時間。"
  - "蘇清保留自行離開與喊停之權利。"

CONSENT_RENEGOTIATION:
  trigger:
    - "白御行曾提出由自己完全掌控節奏，並表示決鬥中蘇清說了不算。"
  response:
    - "蘇清立即截停，明示換姿勢不等於交出停止權。"
    - "張麗華協助暫停並分開兩人。"
  re_agreed_terms:
    - "白御行可掌握該段節奏。"
    - "任何一方說停，事件立即停止。"
    - "白御行接近射精時必須明示。"
    - "不得體內射精。"
  result:
    - "白御行明示接受上述規則後，性交才重新開始。"

LATER_EVENT_STATE:
  - "蘇清由競賽勝負框架轉為明示以自身享受為目的繼續。"
  - "蘇清自述『很爽』，並明示不需再以勝負判定當下。"
  - "最後一段以一百次計數為結束條件；最後十次改為逐次、較慢完成。"
  - "第一百次完成後蘇清明示『停』。"
  - "白御行依約停止，沒有再增加下一次。"

EJACULATION_STATE:
  internal_ejaculation_confirmed: false
  external_ejaculation_confirmed: false
  exact_outcome: "NO_EJACULATION_REPORTED_OR_OBSERVED"
  contraception_tool_recorded: false
  pregnancy: "NOT_ESTABLISHED"

PHYSICAL_OUTCOME:
  su_qing:
    - "事件後明顯疲累、呼吸尚未平復。"
    - "無受傷報告。"
  bai_yuxing:
    - "事件後自述疲累，當晚無力再與李瓶兒進行性交。"
    - "無受傷報告。"
```

## NIGHT17-E07｜張麗華於後續多人事件中的位置

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E07"
  status: "COMPLETED_FOR_NIGHT"
  participant: "張麗華"

CONFIRMED_ACTIONS:
  - "張麗華多次從後方抱住白御行，與他共同觀看蘇清、李瓶兒的親密互動。"
  - "張麗華在蘇清性交事件中協助穩住床位與身體位置。"
  - "蘇清中止並重談規則時，張麗華支持暫停與重新確認。"
  - "張麗華未替蘇清或李瓶兒作出性同意。"
```

## NIGHT17-E08｜本夜射精、生育與懷孕決定

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E08"
  status: "CLOSED_FOR_NIGHT"

PLAYER_DECLARATIONS:
  - "白御行表示今晚不在任何女人體內射精。"
  - "白御行表示若李瓶兒未來懷孕，他不會要求她打掉，並會要這個孩子。"

OBSERVED_RESULT:
  - "本夜沒有任何體內射精被確認。"
  - "本夜沒有懷孕事件成立。"
  - "李瓶兒拒絕將當夜親密直接推進為受孕嘗試。"

LI_PINGER_POSITION:
  - "孩子對李瓶兒非常重要。"
  - "她不接受因蘇清不願體內射精，便把受孕可能順勢交給她。"
  - "她要求先釐清孩子母親的位置、公開稱呼、姓氏、居所、養育與保護責任。"
  - "她要求白御行回答要的是孩子，還是她與孩子。"
  - "她將是否與白御行生孩子延後至兩日結束後再談。"

LEGAL_STATE:
  consent_to_insemination: "REJECTED_FOR_THIS_NIGHT"
  future_child_discussion: "ACTIVE_DEFERRED_TOPIC"
  pregnancy_status: "NOT_ESTABLISHED"
  parenthood_commitment_status: "PLAYER_INTENT_STATED; NO_JOINT_AGREEMENT"
```

## NIGHT17-E09｜夜間收束與共同就寢

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E09"
  time: "槐月十八日清晨前"
  status: "COMPLETED"

CONFIRMED:
  - "白御行告知李瓶兒自己已疲累，當晚不再與她性交。"
  - "李瓶兒表示無須因未與她性交而道歉；她留下不是等待排到自己。"
  - "李瓶兒表示槐月十八日仍會再來，原因是想再見白御行。"
  - "她未承諾槐月十八日一定發生性行為。"
  - "四人以薄被覆身，共同在張麗華房內就寢。"
  - "張麗華取得白御行當夜最後抱睡的位置。"
  - "白御行以『小狼狗／貓／狼叫』與張麗華玩笑互動；該稱呼只屬當夜情境。"
```

---

# 3｜同意矩陣

```yaml
CONSENT_RECORDS:

  - consent_id: "CONSENT-H17-ZLH-BYX-SEX-001"
    actor: "張麗華"
    target_actor: "白御行"
    action_scope: "當夜性交與親密接觸"
    time_scope: "槐月十七日晚"
    status: "EXPLICITLY_ACCEPTED_AND_COMPLETED"
    conditions:
      - "張麗華保有主動、停止與房間管理權"
    effective_until: "NIGHT_CLOSED"
    source_event_ids:
      - "NIGHT17-E03"

  - consent_id: "CONSENT-H17-SQ-BYX-INTERCOURSE-001"
    actor: "蘇清"
    target_actor: "白御行"
    action_scope: "當夜性交"
    time_scope: "槐月十七日晚"
    status: "CONDITIONALLY_ACCEPTED_AND_COMPLETED"
    conditions:
      - "不接受體內射精"
      - "白御行接近射精時須明示"
      - "蘇清說停即停"
      - "白御行可掌握後段節奏，但不得取消蘇清停止權"
    effective_until: "NIGHT_CLOSED"
    source_event_ids:
      - "NIGHT17-E06"

  - consent_id: "CONSENT-H17-LP-BYX-MANUAL_ORAL-001"
    actor: "李瓶兒"
    target_actor: "白御行"
    action_scope: "手部與口部有限性探索"
    time_scope: "槐月十七日晚"
    status: "CONDITIONALLY_ACCEPTED_AND_COMPLETED"
    conditions:
      - "由李瓶兒自行靠近與決定節奏"
      - "不按頭、不抓手強教、不催促"
      - "不在口中射精、不要求吞嚥"
    effective_until: "NIGHT_CLOSED"
    source_event_ids:
      - "NIGHT17-E05"

  - consent_id: "CONSENT-H17-LP-BYX-INTERCOURSE-001"
    actor: "李瓶兒"
    target_actor: "白御行"
    action_scope: "性交"
    time_scope: "槐月十七日晚"
    status: "REJECTED_FOR_THIS_NIGHT"
    conditions: []
    effective_until: "NIGHT_CLOSED"
    source_event_ids:
      - "NIGHT17-E05"
      - "NIGHT17-E08"

  - consent_id: "CONSENT-H17-LP-BYX-INSEMINATION-001"
    actor: "李瓶兒"
    target_actor: "白御行"
    action_scope: "體內射精／受孕嘗試"
    time_scope: "槐月十七日晚"
    status: "REJECTED_FOR_THIS_NIGHT"
    conditions:
      - "未來須先談清關係、母子位置與長期責任"
    effective_until: "NIGHT_CLOSED"
    source_event_ids:
      - "NIGHT17-E08"

  - consent_id: "CONSENT-H17-LP-SQ-INTIMACY-001"
    actor: "李瓶兒"
    target_actor: "蘇清"
    action_scope: "擁抱、親吻與有限觸碰"
    time_scope: "槐月十七日晚"
    status: "EXPLICITLY_ACCEPTED_AND_COMPLETED"
    conditions:
      - "李瓶兒可逐步決定是否繼續"
    effective_until: "NIGHT_CLOSED"
    source_event_ids:
      - "NIGHT17-E04"
```

---

# 4｜契約、帳目與履約狀態

## CONTRACT-H17-SQ-02DAY｜蘇清兩日共同生活結算安排

```yaml
CONTRACT_STATE:
  contract_id: "CONTRACT-H17-SUQING-2DAY-HOUSEHOLD-001"
  state_class: "ACTIVE"
  state_label: "FINAL_DAY_REMAINS; SEXUAL_COMPONENT_COMPLETED"
  parties:
    - "白御行"
    - "蘇清"
  linked_participant:
    - "張麗華，作為兩日共同生活與三人事件之一員，但非舊五百兩債務債務人"
  duration_anchor: "槐月十七日午間至槐月十九日黎明"
  purpose:
    - "以兩日共同吃住生活與約定範圍之親密事件，處理舊五百兩／三夜未結帳"
  completed_components:
    - "槐月十七日共同生活與四人家宴"
    - "白御行、張麗華、蘇清共同參與之三人成人事件要件已於本夜發生"
    - "蘇清與白御行完成當夜性交"
  remaining_components:
    - "槐月十八日最後一日之共同生活"
    - "至約定結束時間之完整履行"
  current_ledger: "UNSETTLED_PENDING_FINAL_DAY"
  old_contract_link:
    amount: "五百兩"
    original_duration: "三晚"
    original_status: "UNSETTLED"
  no_automatic_effect:
    - "本夜性交不自動建立愛情"
    - "本夜性交不自動免除未完成之最後一日"
    - "李瓶兒不是此契約當事人"
```

## CONTRACT-H17-ZLH-COMPANIONSHIP｜張麗華陪伴線

```yaml
CONTRACT_STATE:
  contract_id: "RELATIONAL_PROMISE-ZLH-THREE_DAY-COMPANIONSHIP"
  state_class: "ACTIVE"
  state_label: "MULTI_PERSON_NIGHT_ACCEPTED_ONCE; EXCLUSIVITY_NOT_ESTABLISHED"
  confirmed:
    - "張麗華原有三日陪伴承諾仍在。"
    - "她接受本夜四人共處與成人事件。"
    - "她不接受由此推定往後每一晚都必須多人同床。"
    - "下一次若再安排多人同床或多人性事件，她要求白御行先問她是否願意。"
```

---

# 5｜關係硬狀態

## REL-BYX-ZLH｜白御行 × 張麗華

```yaml
RELATIONSHIP_STATE:
  relation_id: "REL-BYX-ZLH-HOT-V2"
  actor_a: "白御行"
  actor_b: "張麗華"
  state_class: "ACTIVE"
  state_label: "INTIMATE_COMPANIONSHIP_WITH_REAL_JEALOUSY_AND_ROOM_AUTHORITY"
  established_roles:
    - "當前親密伴侶／陪伴線核心人物"
    - "張麗華房間與床位管理者"
  confirmed_events:
    - "本夜完成性交"
    - "張麗華接受四人共處"
    - "張麗華最後抱白御行入睡"
  effective_refusals:
    - "多人共處不得被自動延長為每夜固定制度"
    - "不得故意利用其他女人刺激她吃醋以取得床上反應"
  unresolved_axes:
    - "正式名分"
    - "排他程度"
    - "長期多重關係邊界"
    - "三日陪伴結束後關係形狀"
  romance_status: "ACTIVE_AFFECTION_NOT_FORMALLY_NAMED_AS_MARRIAGE"
  exclusivity_status: "NOT_ESTABLISHED"
  physical_contact_status: "CONSENSUAL_SEX_OCCURRED_THIS_NIGHT"
  last_delta_event_id: "NIGHT17-E09"
```

### 張麗華本夜明示立場

```yaml
ZHANG_LIHUA_POSITION:
  - "她喜歡本夜的變化。"
  - "她也確實吃味，兩者同時成立。"
  - "她喜歡看蘇清放下分析、李瓶兒自己靠近，也喜歡四人真正共同在場。"
  - "她不願被固定為替白御行安排其他女人、永遠懂事或永遠大度的位置。"
  - "她希望白御行下次在多人事件前先詢問她，而不是事後讚美她大方。"
  - "她承認會自然護食、搶目光與抱睡位置，但拒絕被刻意操弄嫉妒。"
```

## REL-BYX-SQ｜白御行 × 蘇清

```yaml
RELATIONSHIP_STATE:
  relation_id: "REL-BYX-SQ-HOT-V2"
  actor_a: "白御行"
  actor_b: "蘇清"
  state_class: "ACTIVE"
  state_label: "CONTRACTUAL_SEX_COMPLETED_ONCE; ROMANCE_EXPLICITLY_NOT_ESTABLISHED"
  established_roles:
    - "舊五百兩三夜未結帳之重議履約雙方"
    - "兩日共同生活安排參與者"
  confirmed_events:
    - "本夜完成性交"
    - "停止權曾被爭議，後重新立約並實際遵守"
    - "蘇清明示本夜確實很爽"
    - "白御行稱讚蘇清肉體『很夠力、很爽』"
  effective_refusals:
    - "蘇清不接受體內射精"
    - "蘇清不接受停止權因『決鬥』而失效"
    - "蘇清不接受本夜性交被自動改寫成愛情"
  active_offers:
    - "兩日安排結束後，若蘇清未來想談愛，可另行提出；目前沒有承諾"
  unresolved_axes:
    - "最後一日履約結果"
    - "五百兩舊帳正式結清"
    - "契約後是否維持肉體、朋友、合作或感情關係"
  romance_status: "NOT_ESTABLISHED"
  exclusivity_status: "NONE"
  physical_contact_status: "CONSENSUAL_INTERCOURSE_OCCURRED_THIS_NIGHT"
  contract_links:
    - "CONTRACT-H17-SUQING-2DAY-HOUSEHOLD-001"
  last_delta_event_id: "NIGHT17-E06"
```

### 白御行與蘇清之感情聲明

```yaml
Bai_Yuxing_DECLARATION_TO_SU_QING:
  - "本夜是履約，不是愛情。"
  - "白御行明示自己現在不愛蘇清，也沒有愛上她。"
  - "他承認蘇清的身體令他感到很爽、很夠力。"
  - "他表示若蘇清有一天想愛他，可在兩日安排結束後再談。"

SU_QING_RESPONSE:
  - "接受本夜先按履約與肉體事實記錄，不把床上事件冒充感情。"
  - "她可能日後想談愛，也可能只結帳離開，目前未決。"
  - "她若想愛會自己開口；白御行可接受或拒絕。"
  - "蘇清口誤說成白御行欠她一日，後已自行更正：舊帳法位上是蘇清欠白御行，槐月十八日為最後履約日。"
```

## REL-BYX-LP｜白御行 × 李瓶兒

```yaml
RELATIONSHIP_STATE:
  relation_id: "REL-BYX-LP-HOT-V2"
  actor_a: "白御行"
  actor_b: "李瓶兒"
  state_class: "UNDECIDED"
  state_label: "MUTUAL_AFFECTION_EMERGING; BODY_LIMITS_RESPECTED; RELATIONSHIP_DEFERRED"
  established_roles:
    - "當夜親密接觸雙方"
    - "彼此有明示感情可能，但未定名分"
  confirmed_events:
    - "李瓶兒接受有限手部與口部性探索"
    - "李瓶兒拒絕當夜性交與受孕"
    - "白御行明示對李瓶兒有真感情"
    - "李瓶兒表示聽見後很高興，且不只把白御行當成想碰她的男人"
    - "李瓶兒表示槐月十八日會再來，因為還想見白御行"
  effective_refusals:
    - "本夜不性交"
    - "本夜不體內射精或受孕"
    - "不因白御行疲累而把明晚變成補交性義務"
    - "不接受先有孩子、再決定母親位置"
  active_offers:
    - "槐月十八日再見"
    - "兩日結束後討論是否成為白御行的女人、關係形狀與生育問題"
  unresolved_axes:
    - "李瓶兒對白御行之感情程度"
    - "是否成為正式伴侶"
    - "是否排他"
    - "是否允許蘇清、張麗華與她有親密接觸"
    - "是否與白御行共同生育"
    - "若生育，母子公開位置、姓氏、居所、養育與保護責任"
  romance_status: "EMERGING_BUT_NOT_CONFIRMED_AS_COMMITTED_RELATIONSHIP"
  exclusivity_status: "UNDECIDED"
  physical_contact_status: "LIMITED_CONSENSUAL_SEXUAL_CONTACT; NO_INTERCOURSE"
  last_delta_event_id: "NIGHT17-E09"
```

## REL-ZLH-SQ-LP｜三女房內關係

```yaml
GROUP_RELATIONSHIP_STATE:
  group_id: "GROUP-ZLH-SQ-LP-HUAI17-NIGHT"
  state_class: "ACTIVE_TEMPORARY"
  state_label: "SHARED_ROOM_AND_INTIMACY_WITHOUT_PERMANENT_HIERARCHY"
  confirmed:
    - "三女在張麗華房內共同參與本夜成人事件與共眠。"
    - "蘇清與李瓶兒有相互親密接觸。"
    - "張麗華接受兩人留宿並參與本夜，但保留自己的房間與下一次安排決定權。"
  not_established:
    - "三女彼此戀愛"
    - "固定妻妾或大小順位"
    - "永久共享白御行"
    - "任一人可替另一人同意性行為"
```

---

# 6｜玩家硬狀態

```yaml
PLAYER_HARD_STATE:
  player_id: "白御行"
  public_identity: "白總／白御行"
  current_location: "張麗華房間"
  current_condition:
    - "槐月十七日晚經歷多段親密與性交後疲累。"
    - "本夜未再與李瓶兒性交。"
    - "無受傷報告。"
  explicitly_declared_positions:
    - "對張麗華仍有明確親密與偏愛，並喜歡她吃味與護食的樣子。"
    - "對蘇清明示目前無愛情，將本夜定位為履約，但承認肉體享受。"
    - "對李瓶兒明示有真感情。"
    - "表示若李瓶兒未來懷孕，會要孩子且不要求打掉；此為玩家意向，尚未形成共同生育承諾。"
    - "表示本夜不在任何女人體內射精。"
  visible_behavior_patterns_this_night:
    - "以挑釁、比較與競賽語言刺激蘇清。"
    - "在蘇清中止後接受重新確認之停止規則。"
    - "依約在蘇清第一百次後明示停止時停止。"
    - "對李瓶兒採取撫髮、撫臉、擁抱與等待她自行決定之互動。"
  next_action_owner: "PLAYER_AT_MORNING"
  forbidden_ai_fill:
    - "不得替白御行決定槐月十八日醒來後先對誰說話。"
    - "不得替白御行提前回答李瓶兒的關係、生育與母子位置問題。"
    - "不得替白御行把對蘇清的無愛聲明永久化為永不可能改變。"
```

---

# 7｜知情範圍

```yaml
KNOWLEDGE_SCOPE:

  four_person_night_details:
    know:
      - "白御行"
      - "張麗華"
      - "蘇清"
      - "李瓶兒"
    public_state: "PRIVATE_NOT_PUBLIC"
    leak_status: "NO_LEAK_ESTABLISHED"

  bai_feelings_for_li_pinger:
    know:
      - "白御行"
      - "張麗華"
      - "蘇清"
      - "李瓶兒"
    public_state: "PRIVATE_ROOM_DECLARATION"

  bai_no_love_statement_to_su_qing:
    know:
      - "白御行"
      - "張麗華"
      - "蘇清"
      - "李瓶兒"
    public_state: "PRIVATE_ROOM_DECLARATION"

  child_discussion:
    know:
      - "白御行"
      - "張麗華"
      - "蘇清"
      - "李瓶兒"
    public_state: "PRIVATE_NOT_PUBLIC"

  su_qing_letter:
    know:
      - "白御行"
      - "張麗華"
      - "蘇清"
      - "李瓶兒"
    current_holder: "蘇清"
    public_state: "PRIVATE"
```

---

# 8｜繼承中的活躍長線

```yaml
INHERITED_ACTIVE_THREADS:

  zhang_lihua_winery:
    status: "ACTIVE_HANDOVER"
    pending:
      - "花農欠款確數"
      - "年度週轉方案"
      - "一萬兩銀子之正式法位"
      - "師爺後續交接回報"

  zhang_lihua_companionship:
    status: "ACTIVE"
    note:
      - "本夜多人事件不取消白御行原先對張麗華的陪伴承諾。"
      - "槐月十八日仍須處理陪伴、酒莊與多人關係邊界。"

  su_qing_two_day_household_arrangement:
    status: "ACTIVE_FINAL_DAY"
    final_day: "槐月十八日"
    expected_end: "槐月十九日黎明"
    sexual_component: "COMPLETED"
    full_settlement: "NOT_YET"

  su_qing_twenty_eight_day_future_price:
    status: "DISCUSSION_ONLY_NOT_ACCEPTED"
    note:
      - "不得因本夜性交而自動成立。"

  li_pinger_relationship_and_child:
    status: "ACTIVE_DEFERRED_DECISION"
    review_time: "兩日安排結束後"
    questions:
      - "是否成為白御行的女人"
      - "關係是否排他"
      - "白御行給她什麼位置"
      - "是否共同生育"
      - "若有孩子，母子之公開與實際保障"

  ximen_qing_gray_ledger_thread:
    status: "PLAN_NOT_DESIGNED"
    note:
      - "本夜未新增案件事實。"

  white_jade_pool:
    status: "INHERITED_SEALED_OR_RESTRICTED"
    note:
      - "本夜未新增白玉池事件；不得視為已解決。"

  merchant_association_case:
    status: "INHERITED_ACTIVE_UNDER_DELEGATED_HANDLING"
    note:
      - "本夜未新增案件結果。"
```

---

# 9｜禁止推斷

```yaml
FORBIDDEN_INFERENCE:
  - "不得把四人同床一夜改寫成永久四人伴侶、婚姻或固定群體性關係。"
  - "不得把張麗華接受本夜改寫成她往後必須接受每一次多人事件。"
  - "不得把張麗華吃味改寫成她同意白御行故意刺激或操弄她。"
  - "不得把蘇清本夜性交與『很爽』改寫成她愛上白御行。"
  - "不得把白御行稱讚蘇清肉體改寫成愛情承諾。"
  - "不得把蘇清一度失去從容改寫成她失去停止權、人格或分析能力。"
  - "不得把『決鬥』改寫成可取消任一方停止權的合法規則。"
  - "不得把本夜性交改寫成已發生體內射精、懷孕或受孕成功。"
  - "不得把未記錄避孕工具改寫成已採取或未採取特定避孕措施。"
  - "不得把李瓶兒有限口部與手部探索改寫成已性交。"
  - "不得把李瓶兒說明日會來改寫成明日一定提供性行為。"
  - "不得把白御行對李瓶兒有真感情改寫成雙方已確立戀愛、排他或婚姻。"
  - "不得把李瓶兒對孩子重視改寫成她想立刻懷孕。"
  - "不得把白御行會要孩子之聲明改寫成雙方已完成共同生育承諾。"
  - "不得把蘇清兩日安排之性事件要件已發生，改寫成整份五百兩舊帳已結清；最後一日尚未完成。"
  - "不得把『六系』分類、戰力比較、小狼狗／貓／狼叫寫入人物基線。"
  - "不得將本夜粗俗語言或床上台詞外洩後用作羞辱四人。"
  - "不得把原作官哥兒事件當成本線今晚重新發生的事件。"
```

---

# 10｜槐月十八日清晨接關點

```yaml
CONTINUATION_POINT:
  location: "觀止青樓／張麗華房間"
  time: "理火三年槐月十八日清晨"
  scene_status: "MORNING_READY; NO_WAKEUP_ACTION_PLAYED"

  current_positions_at_night_close:
    - "白御行最後由張麗華抱著入睡。"
    - "蘇清疲累，留在同一床上或緊鄰位置休息。"
    - "李瓶兒留宿並與三人同室共眠。"

  immediate_morning_facts:
    - "槐月十八日是蘇清兩日安排的最後一日。"
    - "李瓶兒已表示今日仍會來／仍想見白御行；她目前已在房內，醒後是否暫離再回尚未播放。"
    - "張麗華昨夜明示喜歡多人共處，也有真實吃味，並要求下次事前詢問。"
    - "白御行昨夜對蘇清、李瓶兒作出不同感情聲明，兩條關係不得混寫。"

  next_major_decision_owners:
    - "白御行：清晨第一個言行、是否處理昨夜關係聲明"
    - "張麗華：房間早晨安排、如何處理吃味與陪伴線"
    - "蘇清：最後一日如何履約、是否只按契約繼續"
    - "李瓶兒：醒後是否留在房內、白日如何相處、是否維持昨夜有限親密"

  world_actions_available:
    - "清晨起身、洗漱、早餐與房內對話"
    - "酒莊師爺或觀止後勤送來既有長線消息"
    - "蘇清最後一日共同生活自然推進"
    - "李瓶兒處理掌櫃職務與昨夜私密事件之分界"

  hard_stop_topics_requiring_direct_choice:
    - "李瓶兒是否成為白御行的女人"
    - "李瓶兒是否接受排他關係"
    - "李瓶兒是否願意共同生育"
    - "蘇清契約結束後是否談感情"
    - "下一次多人性事件之參與與同意"
```

---

# 11｜接關最小載入摘要

```yaml
MINIMUM_RUNTIME_SLICE:
  - "時間已到槐月十八日清晨，昨夜四人成人事件結束。"
  - "白御行與張麗華、蘇清均已發生性交；李瓶兒只接受有限手部與口部探索，未性交。"
  - "沒有任何體內射精或懷孕被確認。"
  - "蘇清不接受體內射精；她的停止權曾被重新確認，第一百次後喊停並獲遵守。"
  - "蘇清兩日履約尚剩槐月十八日最後一日；五百兩舊帳未正式結清。"
  - "白御行明示目前不愛蘇清，只承認肉體享受。"
  - "白御行明示對李瓶兒有真感情；李瓶兒高興但把關係、排他與生育答案延後至兩日後。"
  - "李瓶兒今日仍想見白御行，但未承諾性行為。"
  - "張麗華喜歡昨夜變化，也真實吃味；下次多人事件須先問她。"
  - "四人昨夜共同就寢，白御行最後由張麗華抱著。"
```

---

# 最終接關句

> 夜已過去。張麗華的手臂仍是白御行最後記得的睡處；蘇清的舊帳尚剩最後一日，李瓶兒的答案則被她親手留到兩日之後。槐月十八日清晨尚未有人開口。

<!-- SOURCE_HOT_V2_0_END -->

---

## SOURCE ARCHIVE｜HOT V2.1

**檔名：** `觀止青樓_白御行線_HOT_SAVE_V2.1_槐月十八日下午_定陶商戰起局蘇清私約白玉池補固與麗華私稱版.md`  
**SHA-256：** `542e19ef8ae8c842979f72d2db93df162f68c74f83e12b97ff34cb0f4c67c5f5`

<!-- SOURCE_HOT_V2_1_BEGIN -->
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

<!-- SOURCE_HOT_V2_1_END -->

---

## SOURCE ARCHIVE｜HOT V2.2

**檔名：** `觀止青樓_白御行線_HOT_SAVE_V2.2_槐月十九日破曉_師理理如夫人前置與張麗華獨宿夜結版.md`  
**SHA-256：** `fd8b50f27cb463d43cfd85bcadfd4afb60569265c1246d777422b4917f10e2e9`

<!-- SOURCE_HOT_V2_2_BEGIN -->
# 觀止青樓｜白御行線 HOT SAVE V2.2
## 理火三年槐月十九日破曉｜師理理如夫人前置 × 七色肚兜分贈 × 蘇清言語賽 × 張麗華獨宿夜結版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V2_2_HUAI19_DAWN_RIRU_FUREN_PRESET_ZLH_PRIVATE_NIGHT"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V2.2"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  story_date: "理火三年槐月十九日"
  time_of_day: "破曉／天將明；精確時刻未定"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V2.1_槐月十八日下午_定陶商戰起局蘇清私約白玉池補固與麗華私稱版.md"
  previous_valid_hot_sha256: "542e19ef8ae8c842979f72d2db93df162f68c74f83e12b97ff34cb0f4c67c5f5"
  record_state: "ACTIVE_PAUSED_AT_DAWN"
  current_location: "觀止青樓／張麗華房間／床上"
  present:
    - "白御行"
    - "張麗華"
  save_scope:
    - "槐月十八日下午李師師／師理理之如夫人關係前置與成人事件"
    - "白玉池復開前檢查進度"
    - "七色蜀錦蘇繡肚兜分贈與知情範圍"
    - "張麗華房內提早晚膳、蘇清與張麗華言語競賽"
    - "蘇清足部彩頭之實際履行"
    - "李瓶兒與蘇清自行離場、張麗華獨宿夜"
    - "白御行與張麗華當夜性行為、停止點、避孕界線與同眠"
    - "張麗華嫉妒、酒莊、李師師、孩子與關係談話"
    - "槐月十九日商會、白玉池、李瓶兒與蘇清之立即到期事項"
```

---

# 0｜提交法位與版本說明

```yaml
COMMIT_NOTE:
  - "本檔取代 HOT V2.1，成為白御行線當前接關切片；V2.1仍為商戰、蘇清私約與白玉池既有真相之直接來源。"
  - "本檔不更新 MASTER，不改寫人物卡或人物池基線。"
  - "本檔只保存已發生、可觀察、當事人明示、玩家對自身言行的有效確認，以及玩家明示要求自然推進至破曉之結果。"
  - "成人事件之身體反應、當下同意、關係承諾、懷孕結果與未來義務分軸記錄。"
  - "言語比賽中的假設、誇張、低俗台詞不升格為人物真實承諾、秘密告白或未來必然行動。"
  - "張麗華與李師師之孩子議題均未形成可由白御行單方面執行的共同生育契約。"
  - "當夜沒有觀察到商戰線新回報；不得因此推定外部世界停滯或事件已結束。"
```

```yaml
SOURCE_LINEAGE:
  previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V2.1_槐月十八日下午_定陶商戰起局蘇清私約白玉池補固與麗華私稱版.md"
    role: "商戰、蘇清二十八日私約、舊約、白玉池真相、當日晚膳與張麗華私稱來源"
  earlier_relationship_sources:
    - "觀止青樓_白御行線_HOT_SAVE_V1.8_槐月十七日上午_張麗華酒莊接手與三日陪伴線.md"
    - "觀止青樓_白御行線_HOT_SAVE_V2.0_槐月十八日清晨_四人家人夜結與蘇清履約瓶兒延後決定版.md"
  route_conversation_commit:
    role: "槐月十八日下午至十九日破曉之直接劇情事件來源"
```

---

# 1｜當前時間、場景與破曉接點

```yaml
CURRENT_SCENE:
  date: "理火三年槐月十九日"
  time: "破曉／天將明"
  location: "張麗華房間"
  scene_state: "AFTER_PRIVATE_NIGHT; SLEEP_COMPLETED_OR_IN_FINAL_DAWN_REST"
  present:
    - "白御行"
    - "張麗華"
  room_privacy:
    - "槐月十八日晚李瓶兒與蘇清均已自行離場。"
    - "張麗華親自落閂，後續房內事件只有白御行與張麗華在場。"
  immediate_pose:
    - "兩人依張麗華最後選擇停止性行為並相擁同眠。"
    - "目前沒有正在進行的性行為。"
  next_action_owner: "WORLD_OR_PLAYER_AFTER_DAWN_OPENS"
```

```yaml
PLAYER_STATE_AT_DAWN:
  白御行:
    location: "張麗華床上"
    confirmed_recent_events:
      - "槐月十八日下午與李師師／師理理發生一次完成之性交並體內射精。"
      - "槐月十八日晚與張麗華發生較長時間性交；未確認當夜是否射精。"
    fatigue: "LIKELY_AFTER_MULTIPLE_ADULT_EVENTS; EXACT_LEVEL_NOT_PLAYER_CONFIRMED"
    day_plan_due:
      - "槐月十九日回定陶商會查看商戰後續。"
```

```yaml
ZHANG_LIHUA_STATE_AT_DAWN:
  location: "自己房內／與白御行同床"
  self_reported:
    - "當夜三個周天後已滿足。"
    - "腿軟、腰疲，不要第四個周天。"
    - "選擇停止性交，只要相擁同眠。"
  consent_current: "NO_ONGOING_SEXUAL_CONSENT_CARRIED_OVER_INTO_DAWN"
  relationship_current:
    - "與白御行之情人關係持續。"
    - "雙方當夜互相明示喜歡。"
    - "不構成婚姻、排他或生育同意。"
```

---

# 2｜白玉池復開前確認

## BYC18-E01｜蘇清完成第一輪開池前檢查

```yaml
EVENT_RECORD:
  event_id: "BYC18-E01-PREOPENING_INSPECTION"
  time: "槐月十八日下午／晚膳前"
  actor: "蘇清"
  status: "FIRST_CHECK_COMPLETED"
  reported_to: "白御行"
  confirmed_report:
    - "既有封補處完整。"
    - "未見通道重新打開。"
    - "池水已更換。"
    - "目前沒有新的明顯回顯或持續滲漏。"
  remaining:
    - "槐月十九日再做一次回顯／滲漏確認。"
    - "若第二次確認仍穩定，白玉池可進入復開準備。"
  not_established:
    - "白玉池已正式重新營業。"
    - "已訂定復開日期、價格與營業規則。"
    - "舊通道或白御行黑暗面重新顯現。"
```

```yaml
WHITE_JADE_POOL_CURRENT_STATE:
  status: "SEALED_STABLE_AFTER_FIRST_PREOPENING_CHECK"
  immediate_due: "槐月十九日第二次回顯／滲漏確認"
  anti_regression:
    - "不得將白玉池重新寫成原因未知、正在失控或必須重解之主線謎案。"
    - "無新可觀察事件，不得聲稱另一空間通道重新開啟。"
```

---

# 3｜李師師／師理理：如夫人前置、成人事件與當晚設席

## RIR18-E01｜如夫人關係框架口頭成立

```yaml
RELATION_OFFER:
  event_id: "RIR18-E01-RU_FUREN_FRAMEWORK"
  time: "槐月十八日下午"
  location: "李師師私人房間"
  parties:
    - "白御行"
    - "李師師／師理理"
  status: "ORALLY_ACCEPTED_FRAMEWORK; PUBLIC_IMPLEMENTATION_NOT_OBSERVED"
  white_yuxing_offer:
    - "白御行提出給李師師『如夫人』的公開位置。"
    - "此位置不以她是否懷孕為成立前提。"
  li_shishi_response:
    - "李師師表示她想要此位置。"
    - "她保留繼續住在觀止、設席、接待賓客與管理自己房門的自主。"
    - "在此關係存續期間，她同意不再與其他男人上床。"
  not_established:
    - "已向觀止或外界正式公布。"
    - "已寫入白家名冊或官府文書。"
    - "李師師離開觀止。"
    - "白御行取得她設席、工作、身體或居所之管理權。"
    - "白御行對其他女人形成排他義務。"
```

## RIR18-E02｜成人事件、停止與重新同意

```yaml
ADULT_EVENT:
  event_id: "RIR18-E02-INTERCOURSE_AND_INSEMINATION"
  time: "槐月十八日下午"
  location: "李師師私人房間"
  participants:
    - "白御行"
    - "李師師／師理理"
  status: "COMPLETED"
  consent_sequence:
    - "起初動作過重時，李師師明示停止。"
    - "白御行停止，兩人重新確認是否繼續及可接受方式。"
    - "李師師其後明示接受較快、較重的性交。"
    - "李師師明示接受當次體內射精，並保留喊停條件。"
  observed_result:
    - "性交完成。"
    - "白御行在李師師體內射精。"
    - "沒有觀察到李師師在有效喊停後仍被迫繼續。"
  pregnancy_axis:
    status: "UNKNOWN"
    confirmed:
      - "當次存在體內射精。"
    not_confirmed:
      - "已受孕。"
      - "未受孕。"
      - "完整共同生育契約已成立。"
```

## RIR18-E03｜愛的告白、離房與枕頭事件

```yaml
EVENT_RECORD:
  event_id: "RIR18-E03-LOVE_AND_ABRUPT_DEPARTURE"
  status: "COMPLETED"
  confirmed:
    - "白御行在離開前對李師師說『我愛你』。"
    - "李師師在他離房以前沒有給出明確回答。"
    - "白御行隨即穿衣／整裝離開，趕赴張麗華房內提早晚膳。"
    - "李師師向門口擲出枕頭並出聲追罵。"
  interpretation_limits:
    - "枕頭事件證明她對白御行突兀離開有明顯情緒。"
    - "不得替李師師判定她已接受、拒絕或回應『我愛你』。"
    - "不得把白御行的告白自動等同婚姻、排他或永久承諾。"
```

## RIR18-E04｜便箋往返與戌初設席

```yaml
CORRESPONDENCE:
  event_id: "RIR18-E04-RED_GREEN_NOTE"
  sender: "白御行"
  recipient: "李師師／師理理"
  white_note:
    - "以『紅配綠，真美麗；一日十客，莫煩你』作戲謔便箋。"
  li_reply:
    - "表示可將句子譜成『莫煩郎』。"
    - "追問錢要算到哪裡。"
    - "明示『今夜設席，不許闖門』。"
  legal_effect:
    - "屬私下玩笑與界線提醒，不是十客實際安排。"
```

```yaml
LI_SHISHI_EVENING_SEAT:
  scheduled_time: "槐月十八日戌初"
  service_scope:
    - "音樂"
    - "茶"
    - "談話"
  overnight: false
  intercourse_included: false
  completion_state: "NOT_OBSERVED_IN_CURRENT_SCENE"
  anti_rumor:
    - "不得因她設席，推定客人進入她的床。"
```

---

# 4｜七色蜀錦蘇繡肚兜分贈

```yaml
GIFT_EVENT:
  event_id: "GIFT18-E01-SEVEN_COLORED_DUDOU"
  status: "ALL_SEVEN_ALLOCATED"
  source: "白御行持有之七色蜀錦蘇繡肚兜"
  allocations:
    李師師:
      color: "煙青"
      context: "下午私人場合先選"
      accepted: true
    李瓶兒:
      color: "白"
      accepted: true
      reaction: "喜歡"
    張麗華:
      color: "紫"
      accepted: true
      reaction: "喜歡"
    蘇清:
      color: "黑"
      accepted: true
      reaction:
        - "認出染色與做工。"
        - "知道白御行有意替她留黑色。"
    紅娘:
      color: "紅"
      accepted: true
    小翠:
      color: "綠"
      accepted: true
      boundary:
        - "接受禮物不等於接受十客、性服務或被拿來作性玩笑的安排。"
    春梅:
      color: "黃"
      delivery_method:
        - "由白御行交給張麗華。"
        - "張麗華以自己名義、按合適方式送給春梅。"
        - "不得說成剩下的或沒人要的。"
      final_delivery: "NOT_YET_OBSERVED"
```

```yaml
RED_GREEN_JOKE:
  confirmed:
    - "白御行先說『紅配綠，狗臭屁』，後否認並改口『紅配綠，真美麗』。"
    - "在場女人以此取笑白御行。"
  legal_effect: "NO_WORLD_STATE_CHANGE"
```

---

# 5｜張麗華房內提早晚膳

## DIN18-E01｜到席與菜色

```yaml
DINNER_EVENT:
  event_id: "DIN18-E01-EARLY_PRIVATE_DINNER"
  time: "槐月十八日傍晚／提早晚膳"
  location: "張麗華房間"
  confirmed_menu:
    - "燉軟羊肉，多蘿蔔、去膻。"
    - "蒸魚，多蔥薑。"
    - "兩樣青菜。"
    - "熱而較清的湯。"
  present_during_core_dinner:
    - "白御行"
    - "張麗華"
    - "蘇清"
    - "李瓶兒"
  gift_and_teasing_phase_also_present:
    - "紅娘"
    - "小翠"
  later_departed_before_private_night:
    - "紅娘"
    - "小翠"
    - "李瓶兒"
    - "蘇清"
```

## DIN18-E02｜三戰兩勝言語競賽

```yaml
VERBAL_CONTEST:
  event_id: "DIN18-E02-SHAMEFUL_SPEECH_CONTEST"
  status: "COMPLETED"
  competitors:
    - "張麗華"
    - "蘇清"
  judge: "李瓶兒"
  prize_subject: "白御行"
  format:
    - "三戰兩勝。"
    - "白御行作彩頭，不參賽、不裁判。"
    - "勝者取得白御行舔兩隻腳的彩頭。"
  rules_established_in_scene:
    - "言語可以是假設、誇張或故意低俗。"
    - "不因說出口便自動成為真實告白、履歷、承諾或未來義務。"
    - "不得使用不在場人物的私人秘密作題材。"
  result:
    round_1: "蘇清勝"
    round_2: "張麗華勝"
    round_3: "蘇清勝"
    final_score: "蘇清 2：張麗華 1"
    winner: "蘇清"
  judge_basis:
    - "李瓶兒依自己聽不下去／羞恥程度裁判。"
```

```yaml
CONTEST_SPEECH_AUTHORITY_LOCK:
  - "蘇清第三局提及二十八日後穿黑肚兜、求白御行別把她當結清帳目，只屬競賽文本；不建立她將來必然留下、愛上白御行或主動求關係。"
  - "張麗華競賽中提及逼白御行忘記其他女人、只要她，屬當場羞恥話語；不建立永久排他要求。"
  - "競賽中的主人、狗、跪、腳等語言不建立常設權力關係。"
```

## DIN18-E03｜蘇清彩頭與張麗華額外足部親密

```yaml
PRIZE_EXECUTION:
  event_id: "DIN18-E03-SUQING_FOOT_PRIZE"
  status: "COMPLETED"
  participants:
    - "白御行"
    - "蘇清"
  confirmed:
    - "白御行依賽果替蘇清脫鞋襪。"
    - "白御行舔、含吮蘇清兩足腳趾，並沿腳背、腳踝進行親密接觸。"
    - "白御行在一側跟腱附近輕咬。"
    - "蘇清沒有將此夜留床、性交或舊約履行與彩頭混算。"
  consent_scope:
    - "只限當次賽果與當場延續。"
    - "不形成未來可任意觸碰蘇清雙足或身體的權利。"
```

```yaml
ZHANG_LIHUA_FOOT_INTIMACY:
  event_id: "DIN18-E04-ZLH_FOOT_PLAY"
  status: "COMPLETED"
  confirmed:
    - "白御行另替張麗華脫鞋襪，以舌尖逐點舔觸腳底與足心。"
    - "張麗華接受當次互動並明示足心怕癢。"
  legal_effect:
    - "不是言語競賽獎勵。"
    - "不抵銷其後床上親密或建立常設義務。"
```

---

# 6｜李瓶兒與蘇清離場；張麗華取得獨宿夜

```yaml
DEPARTURE_DECISIONS:
  event_id: "DIN18-E05-PRIVATE_NIGHT_SELECTION"
  李瓶兒:
    decision:
      - "只收拾桌面、安排熱水。"
      - "明示不加入床上事件。"
      - "其後離開張麗華房間。"
    relation_effect:
      - "不因在場、收桌或觀看前段互動而構成性同意。"
  蘇清:
    decision:
      - "明示不加入張麗華與白御行的床上事件。"
      - "其後離開張麗華房間。"
    contract_effect:
      - "本夜不計入蘇清舊五百兩／三夜契約最後一日一夜之履行。"
      - "舊帳不因她參與晚膳或言語競賽而結清。"
  張麗華:
    confirmed:
      - "明示今晚不要觀眾，也不要幫手。"
      - "在兩人離場後親自落閂。"
  white_yuxing_disclosure:
    - "白御行其後表示自己今晚原本也只想與張麗華一人同宿，只是需要她先把界線說出口。"
```

---

# 7｜白御行 × 張麗華：當夜成人事件

## ZLH18-E01｜同意、避孕與語言偏好

```yaml
CONSENT_RECORD:
  consent_id: "CONSENT-H18-ZLH-BYX-PRIVATE_NIGHT-001"
  participants:
    - "白御行"
    - "張麗華"
  time_scope: "槐月十八日晚至停止點"
  accepted:
    - "接吻、脫衣、足部與全身親密。"
    - "性交。"
    - "由白御行主導節奏。"
    - "較快、較重、可使用粗俗直白的成人語言。"
  conditions:
    - "不得在張麗華體內射精。"
    - "張麗華保留停止、改變方式與拒絕額外行為的權利。"
    - "粗話不等於要求張麗華自我貶低或承認自己低賤。"
  effective_end:
    - "張麗華在第三個周天後選擇停止。"
    - "後續只同眠，不延續任何性同意至清晨。"
```

```yaml
ADULT_LANGUAGE_RELATIONAL_NOTE:
  confirmed:
    - "白御行明示自己要聽的是『粗話／下流話』，不是要求張麗華說自己低賤。"
    - "張麗華接受使用直白低俗的成人語言，但維持自身價值與人格位置。"
  scope: "本次成人場景與雙方既有關係語言偏好"
  not_established:
    - "張麗華必須在所有親密場合使用低俗語言。"
    - "低俗語言可取代每次具體同意。"
```

## ZLH18-E02｜性交、九淺一深周天與結果

```yaml
ADULT_EVENT:
  event_id: "ZLH18-E02-THREE_CYCLES_INTERCOURSE"
  status: "COMPLETED_AND_STOPPED"
  participants:
    - "白御行"
    - "張麗華"
  confirmed_sequence:
    - "雙方在前段攻防、玩笑與身體挑逗後進入性交。"
    - "白御行以自定義『九淺一深』節奏完成三個完整周天。"
    - "三個周天使用不同身體位置，其中包括張麗華轉身與被抱起承接。"
    - "張麗華在第三個周天結束後自述已滿足。"
  ejaculation_axis:
    internal_ejaculation: false
    ejaculation_elsewhere: "NOT_CONFIRMED"
  pregnancy_axis:
    current_status: "NOT_ESTABLISHED"
    confirmed:
      - "本次沒有體內射精。"
    prohibited_inference:
      - "不得寫成已懷孕。"
      - "不得寫成已確認不可能懷孕。"
```

## ZLH18-E03｜第四周天風險確認與停止

```yaml
STOP_EVENT:
  event_id: "ZLH18-E03-FOURTH_CYCLE_DECISION"
  status: "STOP_ACCEPTED"
  white_yuxing_statement:
    - "白御行明示若進入第四個周天，自己沒有把握仍能及時拔出避免體內射精。"
    - "他詢問張麗華要繼續，或在已滿足時收兵。"
  zhang_lihua_decision:
    - "張麗華選擇不進入第四個周天。"
    - "她明示三個周天已足夠，要求收兵。"
    - "她選擇今夜其後只相擁同眠，不再性交。"
  subsequent_boundary:
    - "白御行提出可在口中於場外射精。"
    - "張麗華拒絕，明示收兵不是另換戰場，口部只拿來親吻。"
  observed_result:
    - "性交停止。"
    - "沒有第四個周天。"
    - "沒有後續口交。"
    - "兩人相擁入睡，直到破曉前後。"
```

---

# 8｜白御行 × 張麗華：情感、嫉妒、酒莊與孩子

## ZLH18-E04｜互相明示喜歡

```yaml
RELATION_EVENT:
  event_id: "ZLH18-E04-MUTUAL_LIKING"
  status: "CONFIRMED_PRIVATE_RELATIONAL_STATEMENT"
  white_yuxing:
    - "白御行對張麗華說自己喜歡她。"
    - "他表示害怕將來離不開她。"
  zhang_lihua:
    - "張麗華明示她也喜歡白御行。"
    - "她不要求白御行因恐懼而被綁死。"
    - "她希望白御行能離開，但仍因選擇而回來。"
  relation_delta:
    - "雙方情人關係新增互相明示喜歡。"
  not_established:
    - "白御行只愛張麗華。"
    - "張麗華接受白御行所有其他關係而不再嫉妒。"
    - "婚姻、排他或永久承諾。"
```

## ZLH18-E05｜嫉妒與獨宿夜的真實原因

```yaml
JEALOUSY_RECORD:
  status: "ACTIVE_AND_ACKNOWLEDGED"
  zhang_lihua_position:
    - "她明示今晚確實生氣與吃醋。"
    - "她不要被要求『大肚、別吃醋』。"
    - "她接受白御行風流與多重關係的既有事實，但不接受自己總被排到最後或被要求替他接好所有場面。"
    - "她沒有強迫李瓶兒或蘇清離場；兩人各自決定不加入。"
  white_yuxing_position:
    - "白御行表示今晚其實也只想與張麗華一人。"
    - "他承認自己藉張麗華先出聲取得獨宿理由。"
  resulting_state:
    - "槐月十八日晚白御行與張麗華獨宿，是兩人當夜共同選擇。"
    - "此選擇只限當夜，不建立長期排他。"
```

## ZLH18-E06｜酒莊之獨一性與所有權再確認

```yaml
WINE_ESTATE_RELATIONAL_NOTE:
  existing_asset: "張麗華酒莊"
  white_yuxing_statement:
    - "白御行表示酒莊是給張麗華的獨一份，自己沒有第二個酒莊再送其他女人。"
  zhang_lihua_response:
    - "她喜歡此獨一性。"
    - "她再次明示酒莊是自己的產業，釀什麼、怎麼經營、誰能進酒窖由她決定。"
    - "酒莊不能被用作堵嘴、取消嫉妒或換取身體同意的代價。"
  legal_state:
    - "沿用既有『贈與但不控制』邊界。"
```

## ZLH18-E07｜李師師房內事件之直接揭露與傳聞分離

```yaml
DISCLOSURE_TO_ZHANG_LIHUA:
  event_id: "ZLH18-E07-RIRU_DISCLOSURE"
  source: "白御行直接轉述自己的行動"
  confirmed_to_zhang_lihua:
    - "白御行下午與李師師性交。"
    - "李師師同意白御行在她體內射精。"
    - "白御行射精後對她說『我愛你』。"
    - "白御行隨後立即離開，趕來張麗華房中吃飯。"
    - "李師師因其突兀離開向門口丟出物件／枕頭。"
  zhang_lihua_reaction:
    - "她理解李師師為何生氣。"
    - "她拒絕替李師師判定是否接受白御行的愛。"
    - "她指出派人催飯不等於命令白御行在情事後不作安頓便離開。"
```

```yaml
PUBLIC_RUMOR_REGISTRY:
  observed_before_direct_disclosure:
    - "觀止有人聽見李師師房內一聲碰響。"
    - "有人看見白御行離開得比平日快。"
  circulating_versions:
    - "白御行惹李師師生氣。"
    - "白御行偷親後便跑。"
    - "李師師被欺負狠了而惱羞。"
  objective_status:
    - "上述版本均不是完整真相。"
    - "張麗華現有的直接資料來自白御行本人，仍不等於外界公開知情。"
```

## ZLH18-E08｜孩子議題仍未決

```yaml
CHILD_DISCUSSION:
  event_id: "ZLH18-E08-CHILD_UNDECIDED"
  status: "ACTIVE_UNDECIDED"
  white_yuxing_statement:
    - "白御行表示李師師願意幫他生孩子，並以張麗華仍在考慮作為兩者差異。"
    - "白御行表示自己想像張麗華適合生兒子，並以外貌與民間經驗開玩笑。"
  authority_limit:
    - "白御行關於李師師願意生孩子之說法，是他對既有談話的轉述。"
    - "本檔只確認李師師同意當次體內射精；是否已有完整共同生育協議，仍未另行固化。"
  zhang_lihua_position:
    - "她拒絕拿是否生孩子與李師師競爭愛的深淺。"
    - "她表示自己確實想過與白御行有孩子，某些時候甚至想要。"
    - "她尚未同意現在受孕、體內射精或立即開始生育。"
    - "她要求先考慮身體、生活、酒莊、名分、居所、養育與白御行是否在場等現實。"
    - "她不接受由屁股形狀或老人話決定胎兒性別。"
    - "若生女兒，也必須被疼愛，不得因像她、兇悍或『惑亂天下』而被嫌棄。"
  current_joint_state:
    - "沒有共同生育協議。"
    - "沒有當夜受孕嘗試。"
    - "議題保留待未來再談。"
```

---

# 9｜蘇清、李瓶兒與其他人物當前硬狀態

```yaml
ACTOR_STATE:
  蘇清:
    current_location: "已離開張麗華房間；精確位置未知"
    confirmed_evening:
      - "接受黑色肚兜。"
      - "參與言語競賽並以二比一獲勝。"
      - "接受白御行完成兩足彩頭。"
      - "拒絕加入張麗華與白御行的床上事件。"
    old_contract:
      state: "ACTIVE_OUTSTANDING"
      remaining: "舊五百兩／三夜契約最後一日一夜仍欠白御行"
      explicit_lock:
        - "槐月十八日晚的晚膳、競賽與足部彩頭不算舊約履行。"
        - "跨日不自動消滅或結清此帳。"
    private_28_day_pact:
      state: "AGREED_NOT_TRIGGERED"
      trigger: "西門慶真正被毀並形成實質報仇結果"
    immediate_due:
      - "槐月十九日完成白玉池第二次回顯／滲漏確認。"

  李瓶兒:
    current_location: "已離開張麗華房間；精確位置未知"
    confirmed_evening:
      - "接受白色肚兜。"
      - "作言語競賽裁判，不參賽。"
      - "明示只收桌、安排熱水，不加入床上事件。"
    relationship_with_bai:
      state: "UNDECIDED"
      unresolved:
        - "是否成為白御行的女人。"
        - "關係位置、排他、身體界線。"
        - "是否共同生育及母子公開位置、姓氏、居所、養育與保護責任。"
      due_status:
        - "她原先將回答延後至兩日安排結束後。"
        - "槐月十八日已結束，議題自槐月十九日起到期，但她尚未給答案。"

  李師師_師理理:
    current_location: "精確位置未知；槐月十八日晚原有戌初設席"
    relation_with_bai:
      - "如夫人關係框架已口頭接受，尚未觀察到公開實施。"
      - "她在關係存續期間同意不與其他男人上床。"
      - "她保留住觀止、設席與房門自主。"
    unresolved:
      - "她是否與如何回應白御行的『我愛你』。"
      - "當次體內射精是否導致懷孕。"
      - "如夫人位置何時、如何對外實施。"

  張麗華:
    current_location: "自己房內／與白御行同床"
    relation_with_bai:
      - "情人關係持續。"
      - "私下稱白御行『官人』；白御行稱她『小娘子』。"
      - "雙方互相明示喜歡。"
      - "她有真實嫉妒，不接受被要求取消。"
      - "她尚未同意生育。"
    wine_estate:
      - "酒莊為其私人產業與實際管理範圍。"

  紅娘:
    confirmed_evening:
      - "接受紅色肚兜。"
    later_scene: "未參與張麗華房內私人夜"

  小翠:
    confirmed_evening:
      - "接受綠色肚兜。"
      - "拒絕任何由顏色玩笑延伸出的十客或性義務。"
    later_scene: "未參與張麗華房內私人夜"

  春梅:
    gift_status:
      - "黃色肚兜已交張麗華代為妥善贈送。"
      - "是否已實際收到，尚未觀察。"
```

---

# 10｜商戰背景保留與槐月十九日到期事項

```yaml
TRADE_WAR_ACTIVE_STATE:
  source: "HOT V2.1"
  unchanged_confirmed:
    - "常煒仍在執行對廣源轉運行／許奉年之第一擊。"
    - "西門慶已被拉入公函、盤口與外界推斷場，但尚未證實涉案或倒台。"
    - "沈萬三可能是關聯節點、目標或旁觀者，未鎖定為幕後主使。"
    - "潘金蓮已準備切帳、保護賭客本金、延後西門慶部分分成，並可能送模糊警告。"
  no_new_observed_update:
    - "槐月十八日晚私人生活場未收到可核對的商戰新回報。"
  immediate_due:
    - "白御行已明示槐月十九日回定陶商會查看後續。"
```

```yaml
IMMEDIATE_DUE_ITEMS_HUAI19:
  - "白御行是否按原計畫回定陶商會。"
  - "常煒第一輪商戰回報：廣源、許奉年、西門慶周邊、內部分號與沈萬三之反應。"
  - "蘇清完成白玉池第二次回顯／滲漏確認；若穩定，轉入復開準備。"
  - "李瓶兒延後至兩日結束後的關係與孩子回答已到期，但仍須由她自己選擇何時回答。"
  - "蘇清舊五百兩／三夜契約最後一日一夜仍未結清，需另行安排或重議。"
  - "李師師如夫人關係框架尚待對外實施方式；她對『我愛你』的回應仍未知。"
  - "黃色肚兜是否已由張麗華交給春梅。"
```

---

# 11｜知情矩陣與秘密範圍

```yaml
KNOWLEDGE_MATRIX:
  李師師如夫人框架:
    knows:
      - "白御行"
      - "李師師／師理理"
    may_know_later: "未確認"
    public_state: "NOT_PUBLICLY_IMPLEMENTED"

  李師師當次性交與體內射精:
    direct_participants:
      - "白御行"
      - "李師師／師理理"
    later_directly_told:
      - "張麗華"
    public_state: "PRIVATE"

  白御行對李師師說愛:
    knows:
      - "白御行"
      - "李師師／師理理"
      - "張麗華（由白御行直接告知）"
    public_state: "PRIVATE"

  言語競賽完整內容:
    knows:
      - "白御行"
      - "張麗華"
      - "蘇清"
      - "李瓶兒"
    authority: "GAME_TEXT_ONLY"

  蘇清足部彩頭:
    knows:
      - "白御行"
      - "蘇清"
      - "張麗華"
      - "李瓶兒"
    public_state: "ROOM_PRIVATE"

  張麗華獨宿夜成人細節:
    knows:
      - "白御行"
      - "張麗華"
    public_state: "STRICTLY_PRIVATE"
    no_automatic_leak_to:
      - "李瓶兒"
      - "蘇清"
      - "李師師"
      - "潘金蓮"
      - "觀止其他人"

  張麗華孩子未決:
    knows:
      - "白御行"
      - "張麗華"
    public_state: "PRIVATE"

  白玉池第一輪檢查:
    knows:
      - "白御行"
      - "蘇清"
    broader_operational_knowledge: "依實際整理人員接觸範圍，未自動補造"
```

---

# 12｜禁止污染與未決事項

```yaml
ANTI_CORRUPTION_LOCKS:
  - "不得把蘇清言語競賽第三局之未來想像寫成真實告白、愛情成立或二十八日後必然留下。"
  - "不得把張麗華競賽與床上粗話寫成她已接受自我低賤、永久服從或常設角色。"
  - "不得把足部彩頭擴張成白御行可隨時碰蘇清或張麗華雙足的權利。"
  - "不得把李瓶兒收桌、備水或在場觀看寫成她同意床上加入。"
  - "不得把蘇清晚膳、競賽或足部彩頭算入舊五百兩／三夜契約最後一日一夜。"
  - "不得把李師師設席寫成她與客人上床。"
  - "不得把李師師同意一次體內射精，擴張成永久受孕義務、已懷孕或已完整同意替白御行生孩子。"
  - "不得把白御行對李師師說愛，寫成李師師已回應或接受。"
  - "不得把張麗華想過孩子、某些時候想要，寫成她已同意現在受孕或體內射精。"
  - "不得把白御行與張麗華當夜獨宿，寫成長期排他或他已承諾不見其他女人。"
  - "不得把酒莊當成白御行可控制張麗華、買斷嫉妒或換取性同意的資產。"
  - "不得把張麗華房內成人細節無因果洩漏給其他人物。"
  - "不得因當夜沒有商戰回報，推定廣源、西門慶、沈萬三或潘金蓮沒有行動。"
  - "不得重新把白玉池寫成失控謎案；槐月十九日只需第二次穩定確認。"
```

```yaml
UNRESOLVED:
  trade_war:
    - "廣源轉運行與許奉年如何反應。"
    - "西門慶是否收到公函或潘金蓮警告。"
    - "沈萬三是否涉案、被利用、被嫁禍、旁觀或反擊。"
    - "常煒差異查核釣出哪些內部異動。"
  white_jade_pool:
    - "第二次回顯／滲漏確認結果。"
    - "復開日期、營業規則與第一批使用者。"
  li_shishi:
    - "她對白御行『我愛你』的回答。"
    - "如夫人位置對外實施方式。"
    - "當次體內射精是否導致懷孕。"
  zhang_lihua:
    - "孩子議題是否、何時重新談。"
    - "槐月十九日醒後對白御行回商會之反應。"
    - "黃色肚兜是否已交春梅。"
  li_pinger:
    - "關係與孩子議題到期後的回答。"
  su_qing:
    - "舊約最後一日一夜何時、如何履行或重議。"
    - "二十八日私約是否及何時被觸發。"
```

---

# 13｜破曉接關

```yaml
RESUME_POINT:
  date: "理火三年槐月十九日"
  time: "破曉，天色將明"
  location: "張麗華房間／床上"
  present:
    - "白御行"
    - "張麗華"
  immediate_state:
    - "昨夜成人事件已停止，兩人依約相擁同眠。"
    - "張麗華已明示滿足，未同意將昨夜性同意延續到清晨。"
    - "房門仍為私人空間；是否已有外人敲門、送信或備早膳，尚未發生。"
    - "白御行今日原定回定陶商會。"
    - "蘇清今日應做白玉池第二次穩定確認。"
    - "李瓶兒延後的關係／孩子問題已到可回答時點，但不可強迫她立即回答。"
  possible_world_hinges:
    - "天光、院內晨聲或張麗華先醒。"
    - "定陶商會使者送來第一輪回報。"
    - "蘇清來報白玉池第二次檢查安排。"
    - "李瓶兒依自己意願在適當時機談延後問題。"
  player_decision_required_now: false
```

---

# 14｜導演快速載入

```yaml
DIRECTOR_QUICK_LOAD:
  - "現在是槐月十九日破曉，白御行與張麗華在她房內相擁睡過一段，性行為已停止。"
  - "昨夜張麗華只要白御行一人；李瓶兒與蘇清各自明示不加入並離場。"
  - "白御行與張麗華完成三個自定義九淺一深周天；沒有體內射精，是否在外射精未確認。"
  - "白御行警告第四周天可能無法及時拔出，張麗華選擇停止；她也拒絕改用口部讓他射精，兩人只抱睡。"
  - "雙方互相明示喜歡；張麗華有真實嫉妒，不接受被要求取消。她尚未同意生孩子。"
  - "酒莊仍是張麗華私人產業，屬白御行給她的獨一份，但不能換取沉默、服從或性同意。"
  - "李師師下午口頭接受如夫人關係框架，保留住觀止、設席與房門自主；關係存續期間不與其他男人上床。公開實施尚未發生。"
  - "白御行與李師師下午性交，李師師在停止後重新同意較快較重及體內射精；懷孕未知。白御行說愛後立即離開，李師師未回答並丟枕頭。"
  - "言語競賽由蘇清二比一勝張麗華；競賽台詞不是告白或承諾。白御行已完成舔蘇清兩足之彩頭。"
  - "蘇清舊五百兩／三夜契約最後一日一夜仍未結清；二十八日私約仍未觸發。"
  - "白玉池第一輪開池前檢查穩定、已換水；今日再查一次回顯／滲漏，穩定後可進復開準備。"
  - "白御行今日原定回定陶商會；商戰仍在外部運行，昨夜沒有新回報不代表沒有動作。"
  - "李瓶兒延後至兩日安排結束後的關係與孩子回答，從今日起已到期但仍由她自主決定何時回答。"
```

> **接關畫面：天將亮，張麗華房裡的紅帳早已不是昨夜花燭，而是兩人收兵後的安靜。她尚在白御行懷裡；門外是否已有定陶來使、白玉池回報或晨間腳步，下一幕才會發生。**

<!-- SOURCE_HOT_V2_2_END -->

---

## SOURCE ARCHIVE｜HOT V2.3

**檔名：** `觀止青樓_白御行線_HOT_SAVE_V2.3_槐月二十日深夜_沈萬三合作與師師薄情郎席前接關版.md`  
**SHA-256：** `0f943eb273b6cda36179cc9212b24d0abc4edfd8457f7111f422efee55759901`

<!-- SOURCE_HOT_V2_3_BEGIN -->
# 觀止青樓｜白御行線 HOT SAVE V2.3
## 理火三年槐月二十日深夜｜定陶沈家停止試探 × 偽牌高爐案移交開封府 × 師師薄情郎受審席前 × 瓶兒麗華雙向接關版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V2_3_HUAI20_LATE_NIGHT_SHEN_COOPERATION_RIRI_TRIAL_SEAT"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V2.3"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime:
    - "GUANZHI_QINGLOU_V10_0"
    - "GUANZHI_QINGLOU_V10_1_TO_V10_2_PATCH_WHEN_APPLICABLE"
  story_date: "理火三年槐月二十日深夜"
  date_basis:
    - "HOT V2.2 停於槐月十九日破曉。"
    - "商會偽鹽案於槐月十九日白日展開。"
    - "相國寺瓦市公開試烤明示發生於其後『第二日午前』，故為槐月二十日。"
    - "沈萬三觀止夜宴、李師師房外衝突與本接點均發生於同日晚間至深夜。"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "ACTIVE_PAUSED_AT_PLAYER_CHOICE_BETWEEN_LI_PINGER_AND_ZHANG_LIHUA"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V2.2_槐月十九日破曉_師理理如夫人前置與張麗華獨宿夜結版.md"
  current_location: "觀止內院東西廊交界"
  present:
    - "白御行"
  nearby_but_not_in_same_private_scene:
    - "李瓶兒房中仍亮燈；其丫頭持披風在東廊候命。"
    - "張麗華房中仍亮燈；其侍女在西廊候命，燈已挑暗一層。"
  save_scope:
    - "槐月十九日定陶商會被栽私鹽、偽造舊封與副會長腰牌案"
    - "開封府介入、證物鏈、河東池鹽與定陶加工品法位"
    - "相國寺瓦市三炒鹽公開試烤、三烤末批與六烤奢侈品策略"
    - "高溫爐材、偽牌印模、城北廢鑄錢坊與官面涉案線"
    - "沈萬三與定陶停止代理試探、陶瓷金屬研發起點合作框架"
    - "西門慶、廣源與巡檢司之待查關聯"
    - "蘇清五百兩三夜舊契結清、二十八日／二十九日私人約"
    - "白玉池秘密對沈家高層擴大知情，但仍封池、未投資、未營業"
    - "觀止夜宴、紅綠組、肚兜試用品、早餐試餐與沈萬三留宿"
    - "李師師怒砸負心漢之混合真情／演出事件與翌日受審席"
    - "白御行當前尚未決定投宿李瓶兒或返回張麗華房"
```

---

# 0｜提交法位、來源與反污染說明

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V2.2_槐月十九日破曉_師理理如夫人前置與張麗華獨宿夜結版.md"
    role: "師理理如夫人前置、張麗華私夜、商戰前置、白玉池第一輪復開檢查之直接來源"
  long_term_master:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版.md"
    role: "較早玩家線因果來源；另由本輪同步生成之新 MASTER V4.1-R1 固化至 HOT V1.9"
  route_conversation_commit:
    role: "槐月十九日破曉後至槐月二十日深夜的直接劇情來源"
  forbidden_source:
    file: "HOT_SAVE_V1.3"
    status: "ILLEGAL_CORRUPTED_SAVE"
    use: "AUDIT_ONLY"

COMMIT_NOTE:
  - "本檔取代 HOT V2.2，成為白御行線當前直接接關切片。"
  - "本檔不把槐月十九日至二十日事件倒灌人物卡或人物池基線。"
  - "商人推論、開封府初步判斷、前廣源帳房口供、街頭傳聞、誘餌消息與客觀定罪分軸保存。"
  - "沈萬三與定陶只達成口頭停止試探與技術合作原則；未簽盟書、未完成技術交付、未形成共同統治京師。"
  - "西門慶、巡檢司、廣源與偽牌高爐案之關聯仍待官府查證；不得因貨車去向與口供直接宣判謀逆。"
  - "李師師怒砸事件含真實舊怨與雙方同意的宣傳演出；不得全部改寫成純戲，也不得全部改寫成不可修復的真決裂。"
  - "白御行公開稱『女人每月一次情緒不穩』只保存為其當場說法；不是李師師月事、身體或情緒原因之客觀事實。"
  - "當前停在投宿選擇之前；不得替白御行走向任何一房。"
```

---

# 1｜當前時間、位置與停止點

```yaml
CURRENT_SCENE:
  date: "理火三年槐月二十日"
  time: "深夜，沈萬三觀止宴仍在內樓延續，白御行已離開李師師房外公演現場"
  location: "觀止內院東西廊交界"
  player_state:
    clothing:
      - "衣襟曾被李師師為演出扯鬆。"
      - "腰帶曾被扯歪。"
      - "袖口有一道為演出劃出的外層破口，未傷皮肉。"
      - "褲腿沾有李師師擲下之香粉。"
    alcohol: "未飲酒；主要飲用醉花特調蜂蜜茶與茶水。"
    inner_state_by_player:
      - "白御行自述『夾起尾巴』。"
      - "正在考慮去李瓶兒房或回張麗華房。"
  next_action_owner: "PLAYER"
```

```yaml
EAST_CORRIDOR_LI_PINGER:
  observable:
    - "李瓶兒尚未睡，房中有燈。"
    - "其丫頭奉命出來查看前樓動靜。"
    - "丫頭帶來一件披風。"
  message:
    - "若白御行只是喝多，可送醒酒湯。"
    - "若受傷，可先進房讓李瓶兒看看。"
  boundary:
    - "李瓶兒沒有說白御行一定可以進房。"
    - "沒有建立留宿、同床或性同意。"
```

```yaml
WEST_CORRIDOR_ZHANG_LIHUA:
  observable:
    - "張麗華房中有燈，侍女在西廊傳話。"
    - "侍女傳話後將燈挑暗一層。"
  message:
    - "張麗華不問白御行今晚去了誰房裡。"
    - "也不問他為何被砸成這樣。"
    - "昨夜睡過的枕頭仍在。"
    - "白御行若回去，張麗華會命人備水。"
    - "若不回去，她現在就熄燈。"
  boundary:
    - "不是強迫返回。"
    - "不是整夜無限等待。"
    - "沒有自動延續昨夜性同意。"
```

---

# 2｜槐月十九日：定陶商會被栽私鹽案

## DTC19-E01｜兩車被扣與偽造證物

```yaml
EVENT_RECORD:
  event_id: "DTC19-E01-SEIZED_CARTS_FALSE_SALT_CASE"
  time: "槐月十九日清晨至上午"
  location: "京師城南巡檢轄區／定陶商會京師總會"
  status: "ACTIVE_OFFICIAL_CASE"
  confirmed_report:
    - "兩輛掛定陶商會名義的貨車被城南巡檢扣留。"
    - "車底藏有私鹽。"
    - "車上出現定陶商會三年前停用之『玄字九號』真舊封。"
    - "車上有一封寫給白御行的信：『舊帳未清，死人也會說話。』"
    - "車夫留在現場並要求見白御行或常煒。"
  badge_claim:
    - "車夫稱途中有人持副會長腰牌，以修軸名義接觸貨車。"
    - "常煒本人腰牌沒有遺失。"
    - "由此形成腰牌被仿製之高度嫌疑，但仿製者當時未知。"
```

## DTC19-E02｜舊案證物箱與失蹤帳頁

```yaml
EVIDENCE_CHAIN:
  event_id: "DTC19-E02-OLD_CASE_EVIDENCE_BREACH"
  status: "CONFIRMED_BREACH"
  confirmed:
    - "前次失鹽案證物箱曾由背面被秘密打開。"
    - "死去帳房之私簿缺少六頁。"
    - "玄字九號舊封原應銷毀，但實物外流。"
    - "舊封清理經手人共四名：一人死於前案、一人離職失蹤、一人仍在商會且昨夜值西倉、一人現任廣源轉運行二掌櫃。"
    - "涉案貨車車底改造至少在半月前完成，不是臨時栽放。"
  not_established:
    - "仍在商會之經手人已涉案。"
    - "離職者已死亡或被控制。"
    - "廣源二掌櫃受何人指使。"
```

## DTC19-E03｜開封府介入與雙向調查

```yaml
OFFICIAL_INTERVENTION:
  event_id: "DTC19-E03-KAIFENG_TAKES_CUSTODY"
  trigger:
    - "白御行致書開封府尹，要求由開封府接手，並援引趙受益曾到觀止、包府尹曾作見證之既有官面關係。"
  confirmed_actions:
    - "開封府接管兩車、車夫、私鹽、書信與相關證物。"
    - "同時封查定陶商會西倉並索取帳冊與往來文書。"
    - "開封府明示：巡檢司與定陶商會兩邊都查。"
    - "白御行曾投放之謠言、假線與實證須分冊列明。"
  legal_position:
    - "定陶商會自稱本案被栽贓與偽證受害方。"
    - "開封府尚未因定陶自稱受害即免除查核。"
```

## DTC19-E04｜鹽源與定陶產品法位

```yaml
SALT_IDENTIFICATION:
  event_id: "DTC19-E04-SALT_ORIGIN_AND_PROCESSING_STATUS"
  confirmed_by_inspection:
    - "被扣鹽為品質較高、接近官規的河東解池池鹽。"
    - "鹽有官倉式篩整、壓實與包裝痕跡。"
    - "與前次定陶失鹽案被盜之鹽不是同批、同源。"
    - "不是定陶慣用的齊地海鹽原料，也不是定陶三烤或六烤成品。"
  bai_yuxing_business_explanation:
    - "定陶商會不是持牌鹽商，不生產原鹽。"
    - "定陶向齊地沿海具資格鹽商購買合法官鹽，每批有商家號與官面貨單。"
    - "官鹽進烤坊前須由定陶均輸平準司查驗；無官鹽貨單不得入窯。"
    - "每窯保存投入、產出、查驗與損耗紀錄。"
    - "三烤、六烤、九烤是對合法原鹽加工後的高價產品，不等於定陶販賣私鹽。"
  current_legal_effect:
    - "上述制度可供查核，不自動免除對具體帳冊與貨號的驗證。"
```

---

# 3｜三烤、六烤、九烤與相國寺瓦市公開場

## SALT19-E01｜不急於壓制傳聞

```yaml
PUBLIC_RELATIONS_POLICY:
  event_id: "SALT19-E01-LET_RUMOR_RUN_AND_COMPARE"
  player_decision:
    - "白御行命商會不慌亂、不急於全面否認。"
    - "讓市場自己比較被扣河東鹽、普通市鹽與定陶產品。"
  observed_effect:
    - "部分富戶購買定陶產品與普通鹽回家比較。"
    - "民間以鐵鍋反覆乾炒鹽之模仿多有焦苦、結塊與飛濺問題。"
  not_established:
    - "所有京師消費者已信任定陶。"
    - "本案已因市場比較結束。"
```

## SALT19-E02｜三烤竹鹽之未公開工藝點

```yaml
TRADE_SECRET_STATE:
  confirmed_by_bai_yuxing:
    - "定陶三烤之風味不只來自受熱。"
    - "實際核心之一是竹筒、封泥與火候；可稱『三烤竹鹽』。"
    - "商品名過去省略『竹』字。"
  strategy:
    - "公開試烤前不主動揭露竹筒、封泥與完整程序。"
    - "以盲碗、味道、工序問答與官方紀錄辨認真假舊匠。"
  knowledge_scope:
    - "白御行"
    - "常煒"
    - "定陶鹽務掌眼與相關高層"
    - "開封府在場書吏知道工藝有未公開差異，但不掌握完整配方"
```

## SALT19-E03｜九烤鹽與高溫能力

```yaml
NINE_ROAST_STATE:
  event_id: "SALT19-E03-NINE_ROAST_FIRST_BATCH"
  player_statement:
    - "九烤鹽需將鹽加熱至熔融／近熔融處理，實際爐溫須高於一般灶火。"
    - "定陶於上月已做出第一批，白御行於槐月十八日晚才得知成功。"
  official_preservation_order:
    - "開封府向定陶均輸平準司發文，要求封存首批、原料紀錄、九次窯程、損耗與驗收簿。"
    - "要求隨機封三份樣品，分存開封府、地方官署與定陶商會。"
    - "兩路快馬赴定陶。"
  current_delivery_state: "NOT_CONFIRMED_ARRIVED_IN_JINGSHI"
  anti_inference:
    - "不得因白御行宣布成功，補寫樣品已到京。"
    - "不得補寫九烤已正式上市、已入宮或已形成固定價格。"
```

## SALT20-E01｜對方公開試烤與「三炒鹽」命名

```yaml
PUBLIC_CHALLENGE:
  event_id: "SALT20-E01-XIANGGUOSI_PUBLIC_TEST"
  time: "槐月二十日午前"
  location: "相國寺瓦市"
  opponent_claim:
    - "任取市鹽，反覆加熱三次即可製成與定陶三烤無異之鹽。"
    - "若有差異，願賠銀百兩。"
  player_counter_language:
    - "白御行將其產品稱為『三炒鹽』。"
    - "稱其適合倒入隔夜飯、加雞蛋作蛋炒飯。"
  legal_status:
    - "三炒鹽是白御行與現場群眾對其工法的嘲諷稱呼。"
    - "不是官府產品分類，也不是定陶商會正式商品名。"
```

## SALT20-E02｜三烤末批、六烤倍價與奢侈品策略

```yaml
SALES_EVENT:
  event_id: "SALT20-E02-LAST_THREE_ROAST_SIX_ROAST_PREMIUM"
  time: "槐月二十日相國寺瓦市公開場"
  confirmed:
    - "定陶將京師未售完之三烤鹽帶至現場。"
    - "對外標示為京師最後一批三烤，售完不再補貨。"
    - "宣稱未來以六烤為主。"
    - "六烤售價定為三烤的兩倍。"
    - "三烤現場形成購買與排隊，庫存下降。"
  brand_position:
    - "白御行明示定陶賣的不是普通鹽，而是奢侈品。"
    - "定陶不以人人買得起為目標。"
  not_established:
    - "三烤全數售罄。"
    - "六烤長期市場價格已不可變更。"
    - "九烤價格與客群已正式公布。"
```

## SALT20-E03｜假舊匠、當眾失言與拘捕

```yaml
FALSE_CRAFTSMAN:
  event_id: "SALT20-E03-FAKE_OLD_CRAFTSMAN"
  confirmed_observable:
    - "對方帶來一名自稱定陶舊匠之人。"
    - "其對掌火者喊出『風不能這樣收，爐氣一斷，後面全廢』，顯示其熟悉爐火與風門。"
    - "其後仍當眾聲稱鐵鍋炒製鹽與定陶三烤『並無大異』。"
    - "開封府進場封存鹽、鍋、炭、爐材與證人。"
    - "該人試圖逃跑，被差役拘捕。"
    - "其身上掉出一枚刻『武』字小銅牌。"
  not_established:
    - "其真實姓名。"
    - "其是否曾在定陶工作。"
    - "『武』字牌所屬組織。"
    - "其是否參與謀反。"
```

---

# 4｜耐火爐材、廢鑄錢坊與偽牌案

## FURN20-E01｜高溫磚與江南追查方向

```yaml
FURNACE_BRICK:
  event_id: "FURN20-E01-REFRACTORY_BRICK_LEAD"
  confirmed_observable:
    - "瓦市灶臺器材中找到帶鐵渣的耐火爐磚碎片。"
    - "老掌眼判斷其不是普通灶磚，曾接觸高溫與鐵渣。"
  player_hypothesis:
    - "原料可能與蘇州高嶺土或江南耐火料貨路有關。"
    - "可故意放出開封府已辨出蘇州料之風聲，觀察沈萬三是否反應。"
  objective_status:
    - "蘇州來源未經化驗或帳證確定。"
    - "原土產地、製磚地、使用爐址與最後轉手地可能不同。"
```

## FURN20-E02｜廣源舊車與過度整齊的線索

```yaml
TRANSPORT_LEAD:
  confirmed:
    - "瓦市器材所用車輛經刮漆後露出『廣源』舊字。"
    - "車板夾縫有細白泥屑與藍布線。"
  investigator_assessment:
    - "『廣源』兩字留下得過於容易辨認，可能是故意引導。"
  current_state:
    - "廣源仍是實際重要節點與嫌疑商號。"
    - "但車字本身不能單獨證明許奉年策劃全案。"
```

## FURN20-E03｜沈萬三船單與「佛像底座」假名目

```yaml
SHEN_DOCUMENTS:
  event_id: "FURN20-E03-SHEN_SHIP_LISTS"
  source: "沈萬三於觀止夜宴主動帶來之船單與人證"
  confirmed_as_documents_present:
    - "半年內經沈家船隊入汴梁之高嶺土、礬土、耐火泥共十七批。"
    - "其中十四批有明確官坊或瓷窯收貨紀錄。"
    - "三批買主為廣源轉運行，卻未進廣源自倉。"
    - "前廣源帳房之小冊將相關貨物記為『佛像底座』。"
    - "其中一批被指向城北廢棄鑄錢坊。"
  evidence_status:
    - "船單與私冊已在席上展示。"
    - "真偽與完整性仍須官府驗證。"
```

## FURN20-E04｜開封府搜查廢鑄錢坊

```yaml
OFFICIAL_SEARCH_REPORT:
  event_id: "FURN20-E04-ABANDONED_MINT_SEARCH"
  confirmed_by_short_official_note:
    - "開封府封鎖城北廢鑄錢坊。"
    - "現場未搜得成批完成兵器。"
    - "找到三座仍有餘溫之高溫爐。"
    - "找到多種尚未打磨完成的銅鐵腰牌。"
    - "找到官坊、巡檢司、商會與軍中使用之多類印模。"
    - "根據爐灰、車痕與空箱，官差推定到達前至少兩車成品被轉走。"
  legal_status:
    - "構成偽造官牌、印信與可能軍器相關之重大官案。"
    - "尚未因現場器材直接完成謀逆定罪。"
```

## FURN20-E05｜兩車去向之口供

```yaml
TESTIMONY:
  event_id: "FURN20-E05-TWO_CART_DESTINATIONS"
  source: "沈萬三帶來之前廣源帳房"
  statement:
    - "許奉年每月替一名未明人物空出兩輛車。"
    - "一車從西門府後門進入。"
    - "一車送入巡檢司。"
  status: "WITNESS_TESTIMONY_NOT_FINAL_ADJUDICATION"
  immediate_effect:
    - "西門慶、廣源轉運行與巡檢司之關聯由傳聞提升為有具體口供待查。"
    - "商人方明示後續偽牌、官署與可能軍器事項交由包府尹／開封府處理。"
```

---

# 5｜沈萬三觀止夜宴：敵友邊界與技術合作

## SHEN20-E01｜觀止設席與雙方高層到場

```yaml
MEETING:
  event_id: "SHEN20-E01-GUANZHI_HIGH_LEVEL_DINNER"
  time: "槐月二十日晚"
  location: "觀止二樓議事／宴席房"
  dingtao_side:
    - "白御行"
    - "常煒"
    - "京師總會師爺"
    - "倉運老掌櫃"
    - "鹽務掌眼"
    - "兩名高階帳房"
  shen_side:
    - "沈萬三"
    - "京師總代理"
    - "江南船務總管"
    - "爐料老牙人"
    - "前廣源帳房"
  guanzhi_hosts_or_present:
    - "潘金蓮"
    - "蘇清"
    - "紅袖"
    - "浮香"
    - "醉花"
    - "紅娘氏"
    - "小翠"
    - "後續自願上席之成年姑娘與觀止人員"
  table_rule:
    - "無固定上首。"
    - "先吃飯、酒過三巡再對帳。"
    - "白御行不飲酒，醉花為其備蜂蜜茶。"
```

## SHEN20-E02｜沈萬三眼紅之產業與白御行之反揭示

```yaml
INDUSTRIAL_DISCLOSURE:
  shen_initial_answer:
    - "沈萬三明示最眼紅定陶鋼鐵、軍備工坊與制度化工業能力。"
  bai_yuxing_correction:
    - "白御行明示定陶真正核心不是煉鋼煉鐵，而是『陶瓷金屬』。"
    - "常煒展示定陶氧化鋁合金車床刀頭／鑽頭樣品。"
    - "現場以刀頭削切精鋼，刃口未見立即翻捲。"
  world_status:
    - "定陶陶瓷金屬技術在白御行線已由玩家設定與現場樣品展示成立。"
    - "完整成分、燒結溫程、工藝與產能未公開。"
```

## SHEN20-E03｜跨時間線研發起點合作框架

```yaml
TECH_COOPERATION_FRAME:
  status: "ORAL_PRINCIPLE_ACCEPTED; FORMAL_CONTRACT_AND_TECH_DELIVERY_PENDING"
  time_line_structure:
    dingtao: "白御行漢末線"
    shen: "沈萬三明朝線"
    intersection: "觀止京師交會點"
  bai_offer:
    - "定陶不交出全套現成工法。"
    - "可提供研發起點、材料方向與已知失敗坑。"
    - "沈萬三在明朝線以明朝自己的人、料、銀與試驗發展。"
    - "定陶不直接下場替明朝線完成工業跨越，避免由定陶直接破壞其時空穩定。"
  shen_acceptance:
    - "接受取得種子與避坑，而非搬走整棵樹。"
    - "不挖定陶現役匠人。"
    - "不買通帳房，不偷窯圖、配方、溫程或模具。"
    - "明朝線自行研發形成之後續工法可歸沈家，但不得冒稱定陶完整傳授。"
    - "若大明線同類產品進入觀止京師交會點，先通知定陶再談市場邊界。"
  pending:
    - "具體研發起點內容。"
    - "可提供之樣品數量。"
    - "正式對價、交付順序、保密與違約條款。"
```

## SHEN20-E04｜停止代理試探與第三方遮護

```yaml
NON_AGGRESSION_UNDERSTANDING:
  status: "ORAL_MUTUAL_UNDERSTANDING_WITNESSED"
  confirmed_terms:
    - "定陶與沈家不再借廣源、西門慶或其他本地商號投石試水。"
    - "第三方若拿一家名義碰另一家之貨、帳、匠人或官面，先直接通報求證。"
    - "沈家不替廣源遮帳。"
    - "西門慶若向沈家借船、借錢、藏貨或轉帳，沈家不因舊交替其開方便門。"
    - "定陶如何處理自身敵人，由定陶自行決定；沈家不承諾派人、遞刀或共同承擔。"
    - "雙方不立共治京師盟書，不形成對官府之結黨名冊。"
  not_established:
    - "永久軍事同盟。"
    - "共同瓜分京師。"
    - "沈家已參與定陶對西門慶之任何具體行動。"
```

## SHEN20-E05｜「沈萬三要殺西門慶」錯誤風言結清

```yaml
RUMOR_SETTLEMENT:
  previous_operation:
    - "白御行曾透過潘金蓮投放『沈萬三要殺西門慶』之未證實消息。"
  current_public_between_parties:
    - "白御行明示該說法只是定陶收到的錯誤風言。"
    - "當面查證後，確認沒有沈萬三欲殺西門慶這回事。"
    - "沈萬三接受此說法。"
    - "定陶與沈家均承諾日後對外以錯誤風言、查無此事處理。"
  legal_effect:
    - "不得再以沈萬三名義作為定陶對西門慶行動之背書。"
    - "不抹除該消息曾被白御行故意投放之歷史。"
```

---

# 6｜西門慶、蘇清與定陶自身行動

## XIM20-E01｜西門慶之名由蘇清親口提出

```yaml
NAME_DISCLOSURE:
  event_id: "XIM20-E01-SUQING_NAMES_XIMENQING"
  trigger:
    - "白御行表示京師商業環境需要清理，有一個名字不能由自己先說。"
  speaker: "蘇清"
  name: "西門慶"
  su_qing_boundary:
    - "她明示名字由她自己說，不是替白御行傳話。"
    - "她承認對西門慶有私怨。"
    - "她不因此單方面決定沈家或定陶必須如何處置。"
  status:
    - "西門慶成為定陶明示之重要敵對／清理目標。"
    - "並未因一句話完成犯罪定罪或死亡裁決。"
```

## XIM20-E02｜定陶與沈家各自行動

```yaml
STRATEGIC_SEPARATION:
  bai_yuxing_position:
    - "廣源與西門慶有不清楚的關係；白御行稱光此點對定陶而言已是『死罪』。"
    - "此為白御行對敵對關係與處置門檻的宣告，不是官府刑事判決。"
  shen_position:
    - "沈家如何行動由沈萬三自己決定。"
    - "沈家只承諾不為不該保的人與定陶敵對。"
  official_case:
    - "偽牌、高爐、巡檢司與可能軍中印模案件交開封府繼續。"
```

## SUQ20-E01｜五百兩三夜舊契結清

```yaml
OLD_CONTRACT:
  parties:
    - "白御行"
    - "蘇清"
  original_terms: "五百兩／三夜"
  prior_status: "剩一夜未履行之舊帳"
  settlement:
    - "白御行明示昨夜不是蘇清不來，而是張麗華清場。"
    - "白御行承認該次未履行原因在自己一方。"
    - "因此三夜五百兩舊帳正式清帳，不要求補夜。"
    - "蘇清接受此結算為公平。"
  current_ledger: "CLOSED_NO_ADDITIONAL_NIGHT_DUE"
```

## SUQ20-E02｜二十八日私約與可能第二十九日

```yaml
PRIVATE_PACT:
  base_pact:
    status: "ACTIVE_CONDITIONAL_PRIVATE_PACT"
    trigger: "西門慶真正倒下"
    duration: "二十八日"
    current_start: "NOT_STARTED"
    su_qing_recognition:
      - "蘇清表示既已親口押了，條件成立後會認。"
  fall_criterion_by_suqing:
    - "不是短期名聲受損、鋪子被查或避風幾日。"
    - "西門慶須失去原本能回去的位置。"
    - "錢、勢、人、門路至少有一項再也接不回來。"
  additional_day:
    status: "CONDITIONAL_VOLUNTARY_REWARD_NOT_DEBT"
    condition: "若槐月二十日晚這場局實際成為拔掉西門慶關鍵線之因果"
    result: "蘇清願將二十八日增加為二十九日"
    legal_language:
      - "第二十九日不是她現在欠白御行的債。"
      - "只有條件成就後由蘇清自願增加。"
  tonight_fee:
    - "蘇清今晚以事件當事人／主角身分上桌，不收陪席出席費。"
```

---

# 7｜白玉池秘密擴大知情

```yaml
WHITE_JADE_POOL_DISCLOSURE:
  event_id: "POOL20-E01-SHEN_DISCLOSURE"
  speaker: "白御行"
  disclosed_to:
    - "沈萬三"
    - "沈萬三帶來的京師總代理"
    - "江南船務總管"
    - "爐料老牙人"
    - "前廣源帳房"
    - "席上已知情或在場之定陶／觀止高層"
  player_description:
    - "觀止有一座仍在開發的秘密池。"
    - "池中有池靈，白御行以『澡盆成靈』作玩笑說法。"
  su_qing_correction:
    - "池中存在一名自稱阿泠的女子。"
    - "阿泠能控制池水，認為白玉池是她自己的地方。"
    - "池底曾有未知回顯，池仍封閉調查。"
    - "不能把阿泠簡化為白御行所有的澡盆或商品。"
  shen_response:
    - "沈萬三要求己方在場人保密。"
    - "未要求當晚入池。"
    - "若未來開發，可提供浴舍、引排水、保密隔間、客人篩選與江南園林工匠。"
    - "承認阿泠是否見客、是否水療應由她自己決定。"
  current_status:
    pool: "SEALED_OR_RESTRICTED; NO_NEW_REOPENING_RESULT_OBSERVED"
    second_preopening_check_due_from_v2_2: "RESULT_NOT_RECORDED"
    investment: "NO_AGREEMENT"
    service_sale: "NONE"
  confidentiality:
    - "秘密知情範圍已因白御行主動披露而擴大。"
    - "不得倒寫為只有原五人知道。"
```

---

# 8｜觀止夜宴、姑娘自主與新品試用

## GZ20-E01｜宴席服務與姑娘安排

```yaml
ENTERTAINMENT_FRAME:
  confirmed:
    - "紅袖與浮香自願上席奏曲。"
    - "醉花負責調酒、蜂蜜茶與低酒。"
    - "紅娘氏與小翠席間添菜、陪話與觀察。"
    - "蘇清坐在白御行身旁。"
    - "宋蕙蓮、李桂姐、白三娘與若干成年未掛牌姑娘後續自願上席陪聊。"
    - "辭歲得知若出場可能壓過新人後，自行決定不出場，並要求不要拿她名字替席面增價。"
  boundaries:
    - "未掛牌姑娘只陪話，不因上席自動提供性服務。"
    - "每名姑娘是否接後續洗浴、陪夜、同床或性交，由本人逐項同意與議價。"
```

## GZ20-E02｜紅綠組公開亮相與沈萬三捧場

```yaml
RED_GREEN_TEAM:
  members:
    - "紅娘氏"
    - "小翠"
  public_pitch_by_bai:
    - "白御行以『紅綠配，真美麗』介紹兩人組隊。"
    - "提到小翠剛從女孩成為女人、經驗少，請沈萬三多捧兩人場。"
  corrections_and_boundaries:
    - "紅娘氏明示兩人不是綁成一包、付錢即可一併帶走。"
    - "小翠明示自己不知道的可慢慢學，不願意的不能因她剛成女人而被哄騙。"
    - "潘金蓮規定小翠目前只接席間照應、茶菜與普通陪話；正式陪席需她本人同意。"
  transaction:
    - "沈萬三給兩人當晚賞錢，由潘金蓮按席間賞錢處理，不附帶後續身體約定。"
    - "紅娘氏與沈萬三口頭談成：若未來明朝線第一件可售陶瓷金屬器物由她找到第一位京師買家，成交抽一分半；只限該第一位買家。"
  status_of_future_commission: "ORAL_CONDITIONAL_COMMISSION; PRODUCT_NOT_YET_EXISTS"
```

## GZ20-E03｜定陶新款肚兜試用品

```yaml
PRODUCT_SAMPLE_EVENT:
  source: "常煒攜帶之定陶新款肚兜樣品"
  confirmed:
    - "款式與此前送李師師、張麗華及紅綠組之系列同源。"
    - "白御行先讓紅袖、浮香挑選。"
    - "其後由常煒代表定陶，向在場自願接受的成年姑娘一人送一件樣品。"
    - "潘金蓮選擇深紅近黑款，並提出加襯、加寬肩帶、改善線頭與腰後繫法等產品意見。"
    - "白三娘提出寬肩、產後與長時穿著需求。"
    - "醉花提出沾酒後氣味與清洗測試。"
    - "蘇清拿走一件新品作為樣品，不構成對白御行之穿著承諾。"
  status:
    - "樣品贈送已發生。"
    - "正式售價、量產規格、尺寸表與三日回訪尚未完成。"
```

## GZ20-E04｜沈萬三留宿與定陶人員安置

```yaml
OVERNIGHT_ARRANGEMENTS:
  shen_wansan:
    - "沈萬三接受留在觀止至天亮，以觀察觀止夜間服務與早餐整改。"
    - "潘金蓮提供安靜客房。"
    - "沈萬三當晚沒有點任何姑娘陪房。"
    - "只留一名貼身隨從。"
  shen_staff:
    - "沈家京師總代理、船務總管與爐料牙人先行離開處理事務。"
    - "前廣源帳房因牽涉案情，被安排在另室安全留宿／看守，避免夜間失蹤。"
  dingtao_staff:
    - "潘金蓮請願意接洗浴、按摩、陪睡或另行談性服務之成年紅官人自行報名。"
    - "常煒拒絕陪宿，稱翌日仍須對帳。"
    - "部分未具名定陶師爺、掌櫃或帳房與自願姑娘談妥不同範圍服務。"
    - "只確認安排與議價，未觀察每一房之實際完成內容。"
  accounting:
    - "房錢、洗浴、陪夜與其他服務分項記帳。"
    - "誰享受誰先付；若定陶要作員工犒賞，事後持票據報帳。"
```

## GZ20-E05｜早餐整改試餐

```yaml
BREAKFAST_TRIAL:
  status: "ORDERED_FOR_HUAI21_DAWN_NOT_YET_COMPLETED"
  trigger:
    - "白御行公開嫌觀止早餐不佳，但表示不願以定陶資本開早餐鋪搶小販生計。"
  agreed_direction:
    - "不開定陶自營平價早餐鋪。"
    - "可向附近小販與店家採購，保留原店名字與拒絕供貨權。"
    - "觀止只賣環境、服務、選品與高價附加層。"
  pan_order:
    - "槐月二十一日卯初試餐。"
    - "粥、餅、湯、蛋分取附近三家比較。"
    - "不得用隔夜剩料敷衍。"
  payer:
    - "潘金蓮曾提出首輪試吃費由定陶承擔。"
    - "白御行未在本輪另作明示確認，正式付款法位待結帳。"
```

---

# 9｜李師師怒砸負心漢事件

## RIR20-E01｜原始怨氣來源校正

```yaml
CAUSE_LOCK:
  true_previous_cause:
    - "槐月十八日下午，白御行與李師師性交並體內射精後，很快穿衣離房赴張麗華晚膳。"
    - "李師師因其事後幾乎不停留、像房內再無一人而擲枕追罵。"
  excluded_false_cause:
    - "不是因白御行比較紅娘氏床上勝過李師師。"
  current_emotional_state:
    - "李師師對前日提褲離開仍有真實不滿。"
    - "她沒有因此宣布如夫人框架撤回或永久斷絕。"
```

## RIR20-E02｜雙方同意放大為公開故事

```yaml
STAGED_EVENT:
  event_id: "RIR20-E02-ANGER_PERFORMANCE_AGREEMENT"
  initiation_by_bai:
    - "白御行主動表示願再當靶子。"
    - "提議讓李師師朝牆砸杯壺，高聲罵『殺千刀』『死沒良心』『提起褲子不認人』，使全觀止聽見。"
    - "提議把事件轉成翌日設席的招客故事。"
  li_shishi_acceptance:
    - "李師師接受演出方向。"
    - "同意以自己被負心漢丟下的形象設席。"
    - "要求席面由她定，白御行翌日最後必須到場。"
  physical_staging:
    - "李師師先以多只枕頭與薄被砸白御行。"
    - "其後砸碎杯子、茶壺，並高聲罵出約定台詞。"
    - "為使白御行狼狽出場，她扯鬆衣襟、拉歪腰帶並在袖口外層劃破，不傷皮肉。"
  cost:
    - "破損杯、壺、香粉與牆面清理已被潘金蓮記到白御行帳上。"
```

## RIR20-E03｜薄情郎受審席

```yaml
SEAT_PLAN:
  title: "薄情郎受審席"
  host: "李師師"
  planned_date: "槐月二十一日"
  status: "PUBLICLY_ANNOUNCED_IN_GUANZHI; DETAILS_PENDING"
  concept:
    - "先讓客人聽李師師怒砸負心漢之故事。"
    - "白御行主位或受審位置留到最後。"
    - "若白御行不到，李師師曾說可在主位掛一條空腰帶作嘲諷。"
  pending:
    - "開席時辰。"
    - "座錢與提問加價。"
    - "白御行是否依約到場。"
    - "哪些細節屬演出可公開，哪些私密內容禁止出售。"
```

## RIR20-E04｜「每月一次」加碼與真實反應

```yaml
PUBLIC_ESCALATION:
  player_action:
    - "白御行狼狽跑到大堂後，公開說『沒事，女人情緒不穩定，每個月一次』。"
  li_shishi_response:
    - "李師師在樓上以空香粉盒擲下。"
    - "高聲反駁自己是否每月一次不知道，但白御行提起褲子就跑是一天一次。"
    - "再次公開叫白御行滾，並確認翌日設席。"
  status:
    - "白御行該句不是兩人原先完整約定台詞。"
    - "李師師之反擊同時具有即興演出與對被污衊之真實不滿。"
    - "不得把李師師情緒原因記為月事。"
    - "不得把當場叫滾改寫成永久分手。"
```

## RIR20-E05｜今晚不回之範圍

```yaml
NIGHT_BOUNDARY:
  confirmed:
    - "白御行與李師師同意，為了完成故事，白御行今晚不回李師師房。"
    - "李師師要求翌日回到受審席收場。"
  does_not_mean:
    - "白御行必須離開整座觀止。"
    - "白御行不可去李瓶兒或張麗華處。"
    - "如夫人關係框架已撤銷。"
    - "李師師已同意翌日任何性行為。"
```

---

# 10｜目前人物與關係硬狀態

```yaml
RELATION_CURRENT:
  BAI_YUXING__SHEN_WANSAN:
    state: "FROM_MUTUAL_PROBING_TO_ORAL_NON_AGGRESSION_AND_TECH_COOPERATION_PRINCIPLE"
    formal_alliance: false
    signed_contract: false
    tech_delivered: false
    direct_communication_rule: true

  BAI_YUXING__LI_SHISHI:
    state: "RU_FUREN_FRAMEWORK_ORALLY_ACCEPTED; PRIVATE_SEXUAL_RELATION_ACTIVE; CURRENT_NIGHT_PUBLIC_ANGER_STORY_ACTIVE"
    tonight_entry: "NOT_ALLOWED_BY_MUTUAL_STORY_AGREEMENT"
    next_due: "槐月二十一日薄情郎受審席"
    exclusivity_on_her_side_during_relationship: "她先前口頭同意不與其他男人上床"
    public_implementation_of_ru_furen: "NOT_COMPLETED"
    pregnancy: "UNKNOWN"

  BAI_YUXING__ZHANG_LIHUA:
    state: "ACTIVE_LOVER_RELATION"
    current_offer: "若白御行回房，備水並可留宿；不追問今晚去向"
    ongoing_sexual_consent: "NONE_CARRIED_OVER"
    waiting_limit: "燈已挑暗；不整夜無限等候"

  BAI_YUXING__LI_PINGER:
    state: "PURSUIT_OPEN; NO_FORMAL_RELATION; TONIGHT_PRIVATE_ENTRY_NOT_YET_GRANTED"
    current_offer: "醒酒湯或查看是否受傷"
    sexual_consent: "NONE_ESTABLISHED"

  BAI_YUXING__SU_QING:
    old_500_tael_contract: "CLOSED"
    twenty_eight_day_pact: "ACTIVE_CONDITIONAL_NOT_STARTED"
    twenty_ninth_day: "CONDITIONAL_VOLUNTARY_REWARD"
    tonight_fee: "NONE"

  BAI_YUXING__PAN_JINLIAN:
    state: "ACTIVE_OPERATIONAL_RELATION"
    current_actions:
      - "沈萬三留宿安排"
      - "定陶人員房間與服務記帳"
      - "槐月二十一日早餐試餐"
      - "薄情郎受審席預售與損耗記帳待續"

  WHITE_JADE_POOL__SHEN_GROUP:
    knowledge: "SECRET_DISCLOSED_WITH_ORAL_CONFIDENTIALITY"
    operation: "NO_ACCESS_NO_INVESTMENT"
```

---

# 11｜帳目、物品與契約狀態

```yaml
LEDGER_CURRENT:
  su_qing_old_contract:
    amount: "五百兩"
    nights: 3
    state: "CLOSED_BY_BAI_ACCEPTING_OWN_SIDE_CAUSE_FOR_LAST_NIGHT_NONPERFORMANCE"

  shen_hongniang_first_buyer_commission:
    rate: "一分半"
    scope: "明朝線第一件可售陶瓷金屬器物之第一位京師買家，且須由紅娘氏親自找到"
    state: "CONDITIONAL_ORAL_NOT_YET_TRIGGERED"

  dudou_samples:
    state: "DISTRIBUTED_TO_MULTIPLE_NAMED_AND_UNNAMED_ADULT_WOMEN"
    payment: "GIFT_SAMPLES"
    followup: "穿著、磨損、清洗、尺寸與掉色回報待收"

  riri_room_damage:
    items:
      - "杯盞"
      - "茶壺"
      - "香粉盒"
      - "牆面清理"
    charged_to: "白御行"
    exact_amount: "NOT_YET_CALCULATED"

  guanzhi_overnight_services:
    state: "ROOMS_AND_SERVICE_SCOPES_NEGOTIATED"
    exact_total: "NOT_YET_CLOSED"

  breakfast_trial:
    state: "ORDERED_NOT_COMPLETED"
    payer: "DISPUTED_OR_PENDING_CONFIRMATION"
```

---

# 12｜知情、公開傳聞與秘密

```yaml
KNOWLEDGE_AND_RUMOR:
  official_counterfeit_case:
    known_to:
      - "開封府辦案人員"
      - "定陶商會高層"
      - "沈萬三及其核心隨行"
    public: "瓦市群眾知道假試烤與有人被捕；不知道完整官牌印模與兩車去向"

  shen_dingtao_understanding:
    witnesses:
      - "雙方宴席高層"
      - "蘇清與部分觀止在席人員"
    public: "NOT_PUBLIC_ALLIANCE"

  white_jade_pool_secret:
    previous_core_group: "V2.2以前知情人"
    new_expansion:
      - "沈萬三及其四名核心隨行"
      - "定陶在席高層中原不知情者"
    public: "NOT_PUBLIC"

  riri_anger_story:
    public_inside_guanzhi:
      - "李師師怒砸白御行"
      - "白御行提褲就走"
      - "翌日設薄情郎受審席"
    mixed_truth:
      - "前日突兀離房是真實。"
      - "本夜砸杯罵人有雙方同意的宣傳演出。"
      - "白御行月事情緒說法非事實。"
```

---

# 13｜未決事項

```yaml
OPEN_THREADS:
  immediate_player_choice:
    - "白御行去李瓶兒房、張麗華房，或另作第三選擇。"
    - "不得因兩房有燈便預設任何一方同意留宿或性行為。"

  huai21_morning:
    - "沈萬三是否實際留到卯初與早餐試餐。"
    - "觀止早餐整改結果。"
    - "定陶人員夜間服務帳與實際完成範圍。"
    - "前廣源帳房之安全與開封府後續傳喚。"

  huai21_riri_seat:
    - "薄情郎受審席時辰、價格、座次與公開內容。"
    - "白御行是否依約到場。"
    - "李師師如何區分真怨、戲局與如夫人公開位置。"

  official_case:
    - "兩車成品實際內容。"
    - "西門府與巡檢司是否真的收貨。"
    - "許奉年、西門慶、巡檢司與偽牌坊之命令鏈。"
    - "『武』字銅牌來源。"
    - "蘇州／江南高嶺土是否與爐磚同源。"
    - "開封府是否擴大至軍中與官坊。"
    - "案件最終屬偽證、私鹽、偽造官牌、私鑄、軍器或謀逆之哪一層。"

  salt_business:
    - "九烤樣品與官冊是否抵京。"
    - "三烤京師最後庫存是否售罄。"
    - "六烤倍價策略之長期市場反應。"
    - "定陶產品是否正式標示『竹鹽』。"

  shen_cooperation:
    - "陶瓷金屬研發起點的具體內容、交付與對價。"
    - "是否正式立契。"
    - "交會點市場衝突處理規則。"

  su_qing:
    - "西門慶何時達到真正倒下條件。"
    - "二十八日私約何時開始。"
    - "第二十九日條件是否成立。"

  white_jade_pool:
    - "槐月十九日第二次復開前檢查結果未被記錄。"
    - "阿泠是否同意任何未來見客。"
    - "沈家知情是否造成外洩。"
```

---

# 14｜接關約束

```yaml
CONTINUATION_LOCK:
  player_choice:
    - "當前只保存白御行正在考慮去瓶兒或麗華處。"
    - "不得替他向任何一方走去、敲門、接受留宿或發生親密。"

  li_pinger_lock:
    - "披風、醒酒湯與查看傷勢不等於進房、同床或性同意。"
    - "她沒有因白御行狼狽便自動心軟或接受秘密情人位置。"

  zhang_lihua_lock:
    - "備水與昨夜枕頭仍在，不等於自動續夜性交。"
    - "她不問今晚去向，不等於沒有嫉妒、沒有界線或永久無條件接納。"
    - "燈已挑暗，若白御行不回，她可以熄燈並休息。"

  li_shishi_lock:
    - "今晚不回只限師師房。"
    - "翌日受審席已成公開承諾，但白御行是否履行仍由玩家決定。"
    - "不得把怒砸事件寫成純演出而抹除前日真怨。"
    - "不得把叫滾寫成永久分手。"
    - "不得把月事說法寫成客觀身體狀況。"

  shen_lock:
    - "停止試探不等於永久盟友。"
    - "技術合作未交付，不得在明朝線直接生成成熟陶瓷金屬產業。"
    - "沈家不替西門慶遮護，不等於已參與定陶打擊行動。"

  official_case_lock:
    - "商人已把偽牌、高爐與官署線交開封府。"
    - "不得讓白御行或沈萬三私自完成官府搜捕、刑訊或謀逆定罪。"
    - "不得因『武』牌、高爐或軍中印模直接宣布造反成立。"

  white_jade_pool_lock:
    - "白玉池仍封閉／限制中。"
    - "沈萬三未入池、未購買服務、未投資。"
    - "阿泠不是商品或澡盆，服務資格由她自己決定。"
```

---

# 15｜有效接關摘要

槐月十九日，定陶商會兩車遭城南巡檢扣押，車底藏有河東池鹽，並出現三年前停用之玄字九號真舊封、偽造副會長腰牌線索與「死人也會說話」書信。前案證物箱被從背面開啟，死去帳房私簿少六頁。白御行將案件交開封府；開封府同時查巡檢司與定陶商會，並要求把白御行投放之假線與實證分冊。

被扣鹽不是定陶所用齊地海鹽，也不是定陶三烤成品。白御行公開說明定陶不是原鹽鹽商，而是以合法官鹽、貨號、均輸平準司查驗與逐窯帳冊加工高價產品。對手在相國寺瓦市宣稱普通市鹽炒三次即可成三烤，白御行將之稱為「三炒鹽」，並把京師三烤最後庫存帶到現場，宣布售完後只賣倍價六烤。三烤當場形成購買潮。對手所帶假定陶舊匠因說出風門、爐氣術語而露出真窯工底子，當眾為鐵鍋炒鹽背書後試圖逃跑，被開封府拘捕，身上掉出「武」字牌。

現場找到帶鐵渣的耐火爐磚。白御行提出蘇州高嶺土／江南爐料追查方向，但產地未證實。沈萬三其後主動赴觀止，帶來江南船單、爐料牙人與前廣源帳房。三批廣源爐料以「佛像底座」假名目轉運，其中一批指向城北廢鑄錢坊。開封府在該處找到三座高溫爐、多種官坊、巡檢司、商會與軍中印模及未完成腰牌，沒有搜到成批兵器；現場推定至少兩車成品已先行移走。前廣源帳房口供稱一車進西門府、一車進巡檢司，此為待查口供，尚非最終定罪。

沈萬三在宴席上承認眼紅定陶鋼鐵與制度工業。白御行展示定陶真正核心「陶瓷金屬」與氧化鋁合金刀頭，提出只分享研發起點與失敗坑，不交完整工法；沈萬三在明朝線用明朝自己的人、料、銀自行研發，不挖匠、不偷圖，產品若進觀止京師交會點須先通知定陶。雙方口頭接受原則，但尚未簽約或交付技術。

定陶與沈家同時達成停止代理試探：不再借廣源、西門慶或其他本地勢力試水；第三方若冒用一家名義碰另一家，先直接求證。沈家不替廣源遮帳，也不替西門慶借船、借錢、藏貨或轉帳。雙方不是盟軍，也不共治京師。白御行先前投放的「沈萬三要殺西門慶」被當面定為錯誤風言，雙方日後不再沿用。

西門慶之名由蘇清本人在席上說出。蘇清承認私怨，但不替其他人決定行動。白御行與蘇清同時結清舊五百兩三夜契約：昨夜未履行是張麗華清場、責任在白御行一方，不補夜。蘇清對「西門慶真正倒下後二十八日」之私約仍認帳，但尚未開始；若槐月二十日晚此局實際成為拔掉西門慶關鍵線之原因，她自願再加第二十九日，該日不是當前欠債。

白御行在宴席上向沈萬三及其核心隨行披露白玉池與阿泠秘密。蘇清當場校正：阿泠是自稱池主、能控水的女子，池底異常仍未完全解明，池目前封閉調查。沈萬三未要求入池，也未投資，只口頭保密並表示未來可提供浴舍與工程資源；阿泠是否見客仍由她自己決定。

觀止夜宴後轉為風月席。紅袖、浮香、醉花、紅娘氏、小翠、宋蕙蓮、李桂姐、白三娘及自願上席的成年新人各自依範圍陪曲、陪話與照料；辭歲自行拒絕出場。紅娘氏與小翠以紅綠組亮相，但不形成綁售或性義務。定陶新款肚兜作為樣品分贈在場成年姑娘，潘金蓮、白三娘、醉花等提出產品修改意見。沈萬三同意留宿至天亮看觀止早餐整改，沒有點姑娘陪房；部分定陶人員另與自願紅官人談妥有限服務，實際完成仍未逐房確認。

白御行其後去見李師師。兩人確認前日真正怨氣源於白御行性交射精後迅速提褲離房。白御行提議把此事放大成全觀止可聽見的「怒砸負心漢」故事；李師師同意，砸杯、茶壺、高聲辱罵，並把翌日席面定為「薄情郎受審席」，要求白御行最後到場。白御行狼狽到大堂後又稱女人每月一次情緒不穩，李師師以香粉盒與公開反罵即興加碼。該事件既有真怨，也有雙方同意的宣傳演出；月事說法不是客觀事實。白御行今晚不回師師房，但可在觀止其他地方投宿。

**當前時間：理火三年槐月二十日深夜。**

**當前位置：觀止內院東西廊交界。**

**東側：李瓶兒尚醒，可送醒酒湯或查看是否受傷，但未邀請必然進房。**

**西側：張麗華不問今夜去向，若白御行回去便備水；若不回，她將熄燈。**

**白御行尚未選擇。**

---

## VERSION_STATUS

```yaml
ACTIVE_HOT_SAVE: "V2.3"
PREVIOUS_VALID_HOT: "V2.2"
MASTER_CONSOLIDATION_CREATED_IN_SAME_SAVE_OPERATION:
  file: "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"
  master_cutoff: "HOT V1.9"
CURRENT_RESUME_POINT: "槐月二十日深夜，觀止內院東西廊交界，白御行在李瓶兒與張麗華兩邊訊息之間尚未決定"
```

<!-- SOURCE_HOT_V2_3_END -->

---

## SOURCE ARCHIVE｜HOT V2.4

**檔名：** `觀止青樓_白御行線_HOT_SAVE_V2.4_槐月二十日深夜_風滿樓公案與五千後算開冊版.md`  
**SHA-256：** `ad757d9a4b2e612b0c606d44dbf55c857d40e8d7e792db18839a3faa50d088f5`

<!-- SOURCE_HOT_V2_4_BEGIN -->
# 觀止青樓｜白御行線 HOT SAVE V2.4
## 理火三年槐月二十日深夜｜風滿樓公案 × 西門暗櫃 × 五千後算開冊 × 蘇清代理案版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V2_4_HUAI20_LATE_NIGHT_FENGMANLOU_WUQIAN_HOUSUAN"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V2.4"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime:
    - "GUANZHI_QINGLOU_V10_0"
    - "GUANZHI_QINGLOU_V10_1_V10_2_PATCH_WHEN_APPLICABLE"
  story_date: "理火三年槐月二十日深夜"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AT_FENGMANLOU_AFTER_WUQIAN_HOUSUAN_OPENING"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V2.3_槐月二十日深夜_沈萬三合作與師師薄情郎席前接關版.md"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"
  current_location: "觀止青樓／風滿樓"
  direct_resume_owner: "WORLD_OR_PLAYER_AFTER_HOLD_RELEASE"
  save_scope:
    - "HOT V2.3 後之李師師公開薄情郎事件收束與李瓶兒夜談"
    - "定陶／沈萬三早餐與後續商務"
    - "劉成安、阿麗婭、蘇清、杜小七、何進安等證人與法律援助桌"
    - "柳生失蹤案、高衙內／太尉府／廣源／西門慶之法律攻防"
    - "西門慶入開封府、暗櫃移交與多組新證物線索"
    - "風滿樓大型公域展開與公開公案轉述規則"
    - "太尉府私函由潘金蓮秘密交包拯查驗"
    - "蘇清正式委託許慎言調查賣身契與後堂結算"
    - "《五千後算》開冊、潘金蓮供述與蘇清新訴訟方向"
```

---

# 0｜提交法位、來源與反污染說明

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V2.3_槐月二十日深夜_沈萬三合作與師師薄情郎席前接關版.md"
    role: "本檔直接前置 HOT；V2.3 以前事件全部繼承"
  long_term_master:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"
    role: "長期因果與早期玩家線來源"
  route_conversation_commit:
    role: "HOT V2.3 之後至本次 HOLD 的直接劇情來源"
  persona_source:
    file: "觀止人物卡_LCAPG_V1.1-R1_原始重構去污染版_含辭歲_導演隱藏區增補.md"
    role: "人物基線來源；本檔不得倒灌改寫"
  character_pool:
    file: "觀止人物池_LCAPG_V1.1_紅娘氏與李師師雙人正式版.md"
    role: "紅娘氏、李師師平級人物來源"
  forbidden_source:
    file: "HOT_SAVE_V1.3"
    status: "ILLEGAL_CORRUPTED_SAVE"
    use: "AUDIT_ONLY"

COMMIT_NOTE:
  - "本檔取代 HOT V2.3，成為白御行線當前直接接關切片。"
  - "本次只做 HOT SAVE；不更新 MASTER，不改人物卡，不改人物池。"
  - "本檔只保存已發生、可觀察、人物明示、正式文書可見或玩家對自身言行之有效輸入。"
  - "供述、推論、帳冊文字、官方認定、民間傳聞與客觀真相分軸保存。"
  - "潘金蓮或西門慶的自述不因自我不利即自動升格為完整客觀真相。"
  - "同一日期、同一牌號、同一金流只建立線索或交叉查核資格，不自動建立犯罪因果。"
  - "蘇清原始口頭賭約之完整條款到目前仍缺乏硬證據；不得補成正式書面賭契。"
  - "蘇清正式賣身契為本人自願同意並畫押之正式文件，目前仍有效；不得因阿麗婭五千兩權利變化、口頭賭約爭議或潘金蓮後堂局曝光而自動失效。"
  - "阿麗婭若解除西門慶舊五千兩之限制，只代表舊限制可能失效；不等於她欠觀止新的掛牌、初夜、陪客或其他交付。"
```

---

# 1｜當前時間、位置與 HOLD 接關點

```yaml
CURRENT_SCENE:
  date: "理火三年槐月二十日"
  time: "深夜／風滿樓已開；精確時刻未定"
  location: "觀止青樓／風滿樓"
  mode: "HOLD"
  player:
    name: "白御行"
    location: "風滿樓主要觀案席"
    last_confirmed_behavior:
      - "持續旁觀並與沈萬三、蘇清等評論局勢。"
      - "未在本 HOLD 前作出新的不可逆決定。"

  confirmed_present_or_immediately_active_at_guanzhi:
    - "白御行"
    - "沈萬三"
    - "趙受益"
    - "十三娘"
    - "蘇清"
    - "李師師"
    - "常煒"
    - "許慎言"
    - "紅娘氏"
    - "快嘴陸等說書／轉述人員"
    - "青禾可能仍在法律援助席附近；具體是否仍在按摩服務中不重要"

  offsite_or_position_requires_care:
    潘金蓮:
      current: "開封府"
      certainty: "CONFIRMED_AT_LAST_EVENT"
      note:
        - "其已在開封府就《五千後算》、五千掛牌與後堂安排接受詢問／作出供述。"
        - "本 HOLD 時尚未確認她已返回觀止。"
    阿麗婭:
      current: "開封府保護／女吏可控範圍內"
      certainty: "LATEST_CONFIRMED_RANGE"
      note:
        - "此前自願前往確認五千兩舊權利之法律狀態。"
        - "未同意重新掛牌。"
    西門慶:
      current: "開封府羈押／訊問中"
      certainty: "CONFIRMED"
    包拯:
      current: "開封府主持案件"
      certainty: "CONFIRMED"

  direct_resume_point:
    - "《五千後算》已由開封府在見證下開冊，部分內容已被准予以官方抄報方式傳至風滿樓。"
    - "潘金蓮已就五千掛牌局與蘇清敗約後交付作出部分本人供述。"
    - "蘇清已要求許慎言把『完整後堂結算與自身帳項』加入代理案。"
    - "下一幕不得預設潘金蓮敗訴、蘇清贏得自由、阿麗婭重新掛牌、太尉府私函內容曝光或西門慶定罪。"
```

---

# 2｜風滿樓：大型公域、空間與公開轉述規則

## FML20-E01｜風滿樓正式開啟

```yaml
EVENT_RECORD:
  event_id: "FML20-E01-FENGMANLOU_OPEN"
  status: "ACTIVE_PUBLIC_EVENT"
  initiator: "潘金蓮"
  confirmed:
    - "潘金蓮親自同意開觀止大場，正式以『風滿樓』承載本案。"
    - "觀止清堂，八盞落地青銅燈柱立定。"
    - "潘金蓮進行空間宣告後，風滿樓公域拓撲展開，大堂縱深拉開，可容數千人直接進觀止內觀看。"
    - "先前曾出現『把整條街變成觀眾席』之導演敘述，已被 GM 校正撤回；正式場面以風滿樓／隱藏舞台展開為準。"
  public_scale:
    - "數千名觀眾可在觀止內部觀看。"
    - "觀眾多不等於取得私人信件、私密房事或未公開證物之知情權。"
```

## FML20-E02｜三金主與觀止控制權

```yaml
SPONSORSHIP:
  event_id: "FML20-E02-THREE_SPONSORS"
  confirmed_sponsors:
    - "白御行／定陶一份"
    - "沈萬三一份"
    - "趙受益一份"
  operating_party: "觀止／潘金蓮"
  confirmed_rules:
    - "三個金主出銀；觀止出場地、人手、姑娘、帳房、說書與運作。"
    - "出資不換取案情定調權。"
    - "不冠名、不因出資取得多說一句或買結果之權。"
```

## FML20-E03｜說書與法位校正

```yaml
PUBLIC_RELAY_RULES:
  confirmed:
    - "說書先生負責把複雜人物、證據鏈、官府進度說成一般觀眾能理解的局勢。"
    - "許慎言及其他識字訟師負責校正證據法位。"
    - "開封府正式公開一張，觀止才可依公開材料掛一張。"
    - "不得堵開封府、不得替包拯喊判、不得以群眾壓力替代審理。"
  principal_categories:
    - "已證實／實證"
    - "證人所述"
    - "一方主張／訴辯"
    - "尚待查證／未證"
    - "純屬傳聞"
  required_example_separations:
    - "西門慶說梁福怕廣源＝供述，不是客觀成立。"
    - "暗櫃存在陳氏女舊狀＝物件／文書存在；文書內容真偽與犯罪成立仍需查。"
    - "五百兩是不是撤狀銀＝未證明。"
    - "『林教頭家事』是否指林沖＝未證明。"
    - "高俅是否知情＝未證明。"
```

## FML20-E04｜李師師對聯保留為中場閒話

```yaml
STAGED_PUBLIC_CONTENT:
  event_id: "FML20-E04-RIRI_COUPLET_INTERMISSION"
  status: "PUBLIC_INTERMISSION_ONLY"
  couplet:
    upper_or_line_1: "拔屌無情白御行"
    line_2: "一怒紅顏李師師"
    annotation: "自作自受"
  confirmed:
    - "白御行先詢問可否晚掛一天，李師師同意延期不減天數。"
    - "其後白御行改口不撤，授權紅娘氏在案情空檔用公開版說故事。"
    - "李師師同意只說大堂已公開內容，不准亂編房內性細節、不准假造刀具、投河、哭死等情節。"
    - "觀止另設『中場閒話／與本案無關』法位，防止與西門氏案證據混淆。"
    - "紅娘氏已公開講過『我愛你後立即離開』等已公開版本；該段屬中場笑談，不是公案證據。"
  private_boundary:
    - "李師師與白御行之私密房內細節仍非數千觀眾自由取用素材。"
```

---

# 3｜李師師：公開帳收束、私人帳未清

```yaml
LI_SHISHI_CURRENT:
  public_reckoning:
    status: "PUBLIC_ACCOUNT_CLOSED_FOR_NOW"
    confirmed:
      - "李師師糾正白御行：雙方自願性交不等於『佔有』。"
      - "白御行在親密後說『我愛你』並立刻離房，是其真正怒點之一。"
      - "白御行公開承認自己行為有『拔屌無情』性質；李師師拒絕把責任泛化為『所有男人都這樣』。"
      - "先前『薄情郎受審席』後因白御行轉去李瓶兒房而被李師師撤掉；她曾砸牌、關門並發怒。"
      - "公開事件已經收束，不再把李師師寫成要殺白御行或拿真刀行凶。"
  private_relation:
    status: "UNRESOLVED_NOT_BROKEN"
    confirmed:
      - "李師師沒有宣布永久斷絕。"
      - "未明示原諒。"
      - "未取消此前口頭如夫人框架，但也未新增公開落實。"
  anti_regression:
    - "不得把其怒氣全洗成純演出。"
    - "不得把其怒氣寫成不可修復永久決裂。"
    - "不得把職業表演、私人偏愛、性慾、如夫人承諾混為一軸。"
```

---

# 4｜李瓶兒：夜談、未性交與未來位置

```yaml
LI_PINGER_POST_V2_3:
  event_status: "PRIVATE_NIGHT_COMPLETED; MORNING_DEPARTURE_COMPLETED"
  confirmed:
    - "白御行在廊道最終選擇前往李瓶兒一側，而非張麗華房。"
    - "張麗華當夜沒有被白御行選擇；其燈後續熄滅。具體內心不得補寫。"
    - "李瓶兒替白御行準備足水、脫外衣鞋襪等照料。"
    - "白御行與李瓶兒談孩子與未來位置。"
    - "白御行明示確實想要李瓶兒，也想要她的孩子／與她有孩子；具體未來形式仍非完整方案。"
    - "白御行說張麗華選情人、李師師未來如夫人；李瓶兒表達自己要的是『家裡的人』／更接近未來妻位的方向。"
    - "白御行明示不以『妻』稱她，原因包括亡故正妻不可取代及現有法律／身分問題。"
    - "白御行把『如夫人』解釋為目前可給的最高位置：各自管理、平等、不以三書六聘成立。"
    - "李瓶兒目前法律上仍是西門慶之妾；在真正合法切斷前，不接受以新懷孕把局面壓過去。"
    - "她表達：若法律上真正脫離西門慶，且白御行公開承認平等如夫人、分開住處／財務、不把她綁在生孩子上，她願意往該位置走。"
    - "她強調自己仍是李瓶兒，不接受被『孩子』或『位置』吞掉。"
    - "當夜只有擁抱、談話、有限親近；沒有性交、沒有受孕事件。"
    - "翌晨白御行有輕吻後離開。"
  relation_status:
    direction: "FAMILY_OR_FUTURE_CONSORT_DIRECTION_WITH_LEGAL_PRECONDITION"
    not_established:
      - "正式如夫人落實"
      - "婚姻"
      - "合法解除西門妾身分"
      - "生育同意"
      - "排他關係"
```

---

# 5｜早餐、沈萬三與定陶商務

```yaml
MORNING_BUSINESS:
  confirmed:
    - "沈萬三留宿觀止後參與早餐與商務閒談。"
    - "白御行要求『好早餐雙倍付』不得用模糊標準，後續改為可核對的試餐／評價方式。"
    - "談及跨時代馬鈴薯、辣椒／胡椒等食材；導演已校正早明胡椒與後世新大陸辣椒之年代差異。"
    - "西門慶真正倒台後，可考慮讓蘇清把馬鈴薯菜式整理成食譜，供沈萬三之牡丹樓等後世線使用；尚未交付。"
    - "白御行與常煒曾短暫返回定陶商會，後又回觀止看法律大局。"
  shen_wansan_relation:
    - "與定陶仍是停止代理試探、可談陶瓷金屬研發合作之商務關係。"
    - "不是全面同盟。"
```

---

# 6｜劉成安與觀止免費法律援助桌

## LAW20-E01｜劉成安公開存在與證言

```yaml
LIU_CHENGAN:
  identity: "前廣源帳房／缺兩指"
  status: "PROTECTED_PUBLIC_WITNESS"
  confirmed:
    - "白御行主張把劉成安公開移至觀止，使其存在被全京師看見，提高暗殺成本。"
    - "常煒以定陶標誌車輛、繁華路線、公開叫名等方式放大可見性。"
    - "在公開前，口供副本已分存定陶、開封府與觀止。"
    - "劉成安供稱廣源有兩套帳；其曾因詢問無標記車與重複帳目而失去兩指。"
  storyteller_rule:
    - "三名說書人可聽與轉述已確認部分，但不得添油加醋。"
```

## LAW20-E02｜免費代書接狀

```yaml
LEGAL_AID_TABLE:
  status: "ACTIVE_AT_GUANZHI"
  principal_lawyer: "許慎言"
  sign:
    - "西門氏相關訟事"
    - "受欺無資者免費代書接狀"
    - "實事實寫，傳聞另記"
  funding: "定陶商會出資；觀止借場地"
  no_promise:
    - "不承諾勝訴"
    - "不把傳聞包裝成證據"
  evidence_sorting:
    white: "本人直接經歷／第一手"
    yellow: "文件／物證"
    blue: "證人／來源"
    gray: "傳聞"
  notable_item:
    - "一名跛腳鹽夫帶來木牌，其火印與此前偽牌高爐案出現同類印記，形成初步可查連接；尚非完整犯罪閉環。"
```

---

# 7｜柳生、阿麗婭、蘇清：證言與責任分離

## LIUSHENG20-E01｜固定歷史與目前證據法位

```yaml
LIUSHENG_CASE:
  fixed_observed_history:
    - "柳生曾帶十兩試圖與阿麗婭私奔。"
    - "高衙內在觀止公開下令『拖出去，打斷腿扔河裡』。"
    - "其手下對柳生施暴並拖走／轉移。"
    - "西門慶當時在場；後續以五千兩取得阿麗婭之預定名義。"
  crucial_unknown:
    - "柳生是否實際死亡。"
    - "是否被真正扔入河中。"
    - "西門慶是否事前指使、鼓勵或共同謀劃暴力。"
  prohibition:
    - "不得把『失蹤＋傳聞淹死』寫成已確認死亡。"
    - "不得把西門慶在場自動寫成其下令施暴。"
```

## LIUSHENG20-E02｜阿麗婭證言

```yaml
ALIYA_TESTIMONY:
  confirmed:
    - "她見到柳生。"
    - "她聽見高衙內下令打斷腿、扔河裡。"
    - "她看見人員毆打／拖走柳生。"
    - "她見西門慶在場且未阻止。"
    - "其後掛牌照常進行，西門慶出五千。"
    - "她保留柳生血染木簪，已作證物封存。"
  not_testified:
    - "她沒有聽見西門慶命令暴力。"
  current_rights_issue:
    - "她已自願去開封府確認當年五千兩究竟買到什麼權利及其是否仍有效。"
    - "她沒有因此同意再次掛牌。"
```

## LIUSHENG20-E03｜蘇清證言

```yaml
SUQING_LIUSHENG_TESTIMONY:
  confirmed:
    - "蘇清知道柳生與阿麗婭曾策劃離開。"
    - "她見過柳生紙條並在掛牌前夜於側門攔過阿麗婭。"
    - "她亦見到高衙內下令與其後暴力。"
    - "她沒有證稱自己聽到西門慶下令打柳生。"
  private_confession_line:
    - "蘇清在西門府期間曾由西門慶本人私下告訴她若干事情。"
    - "該內容目前只知西門慶與蘇清掌握；蘇清拒絕先在觀止公開。"
    - "她要求先私下對包拯逐字陳述，再讓西門慶／其律師知悉。"
    - "具體內容仍為 UNKNOWN；不得生成補全。"
```

---

# 8｜開封府與太尉府：西門慶入府與程序攻防

```yaml
KAIFENG_VS_TAIWEI:
  confirmed_chain:
    - "開封府先以柳生失蹤案分別傳喚潘金蓮、阿麗婭、龐春梅與西門慶。"
    - "西門慶當時未到，轉赴太尉府。"
    - "太尉府曾希望在府內詢問並限制只查柳生、不延伸高／廣源／太尉府。"
    - "包拯拒絕把太尉府當法庭；可給安全押送，但不得以府邸替代官署。"
    - "期限過後，開封府依法提升為提人／拘票。"
    - "高俅最終交出西門慶；最初未上鐐，太尉府保留異議。"
    - "此移交不等於高俅承認西門有罪。"
  taiwei_public_position:
    - "太尉府正式回文：外院公帳無杜成、梁福代收商戶護行銀之核准紀錄。"
    - "若二人私受商銀，屬個人行為；太尉府稱不知情、未授權、不予庇護。"
    - "該回文把梁福／杜成切出為可被查的個人節點，但不等於太尉府無任何責任已獲證明。"
  legal_counsel:
    - "章文度代表西門慶，主張在場不等於下令、沒有屍體不等於可直接以殺人論、第三人罪責需獨立互證。"
    - "韓季衡代表太尉府，重視程序、範圍與官府權限。"
```

---

# 9｜廣源二掌櫃、義莊、三千兩與梁福／杜成線

## EVID20-E01｜黑方戒指與母簿誘餌

```yaml
GUANGYUAN_SECOND_MANAGER:
  confirmed:
    - "街頭出現訊息：西門慶若留在開封府，『廣源真正總帳』不能留到天亮。"
    - "劉成安辨認黑方戒／三黃銅點為廣源二掌櫃憑證。"
    - "劉指出廣源內部更常稱『母簿』，不是『總帳』；因此該訊息被視為可能誘餌。"
    - "開封府暗捕已在人群中；二掌櫃試圖吞蠟丸後被拘。"
    - "蠟丸列三處：城南永安義莊、西門府外馬房、廣源南倉井房。"
    - "二掌櫃提出以母簿位置交換家人保護；是否完全可信未定。"
```

## EVID20-E02｜永安義莊與三千兩金流

```yaml
YONGAN_MORTUARY:
  confirmed:
    - "義莊屍房後室起火；一輛無棺黑車欲離開，被扣。"
    - "現場取得帳箱。"
    - "前二十七頁出現三千兩路線：廣源 → 西門府外帳 → 太尉府外院管事梁福。"
  not_proven:
    - "三千兩用途。"
    - "其與柳生暴力是否有直接因果。"
  temporal_note:
    - "日期與柳生被打同日，僅為時間重合，不能單獨證明用途。"
```

## EVID20-E03｜西門對三千兩之說法

```yaml
XIMEN_3000:
  confirmed_statement:
    - "西門慶承認該三千兩曾經過他。"
    - "他稱其為廣源支付梁福的『護行銀』，用途是保商路，不是殺人或封口。"
    - "他稱收據應存在西門外帳與梁福處。"
  status: "ADMISSION_OF_MONEY_PATH; PURPOSE_DISPUTED"
```

## EVID20-E04｜梁福、杜成與太尉府西院

```yaml
LIANGFU_DUCHENG:
  confirmed:
    - "開封府欲尋梁福時，梁福失蹤；家眷、衣物與主要財物仍留。"
    - "太尉府門簿曾有假出門記錄，守門人承認收五兩做假登錄。"
    - "銀角剪口與西門府常見裁銀習慣相似，只能提示習慣，不證明來源。"
    - "跑腿鏈追到太尉府外院小管事杜成。"
    - "太尉府先稱杜成午前已離府，後改口稱其曾短暫返回。"
    - "酒樓送過四人份飯菜入西門，店童聽見『梁先生一天沒吃東西了』；只聽到梁先生。"
    - "太尉府稱該梁先生為幕客梁士遠並允次日出面；真偽未定。"
  white_yuxing_inference:
    - "白御行認為梁福若要藏，太尉府可能是安全處，因開封府不能只靠猜測搜府。"
    - "此為玩家推論，不是世界事實。"
```

## EVID20-E05｜杜小七

```yaml
DU_XIAOQI:
  identity: "太尉府掃地小廝，約十六至十七歲"
  status: "PROTECTED_WITNESS"
  testimony:
    - "杜成命其清掃西院最內小院並換被褥。"
    - "午後有蒙面人由兩人扶入，走路偏一側。"
    - "晚間送飯，由杜成在門口接。"
    - "他聽見屋內人說：『西門慶都進開封府了，你們還想關我到什麼時候？』"
    - "他被杜成掌摑、威脅，後逃至觀止求保護。"
  cross_detail:
    - "劉成安說梁福右膝舊傷、陰雨時跛；杜小七所見蒙面人亦偏右腿。"
  status_note:
    - "相符但仍不足以證明蒙面人即梁福。"
```

## EVID20-E06｜丙七浮屍

```yaml
BINGQI_CORPSE:
  confirmed:
    - "運河發現一具男性浮屍，身有太尉府外院車馬房『丙七』銅牌。"
    - "驗屍顯示並非杜成：死者約五十、手有兵器繭、左腿舊折；杜成檔案約三十四且無此舊傷。"
    - "丙七牌本屬車夫鄭老六；鄭老六本人活著，稱三日前已把牌交回杜成。"
  implication:
    - "真牌被放到錯誤死者身上，可能涉及身份誤導或栽置；目的未定。"
```

---

# 10｜何進安與「死人簿／絕戶支」

```yaml
HE_JINAN:
  identity: "廣源南倉年輕帳房"
  status: "PROTECTED_WITNESS"
  confirmed:
    - "何進安主動到定陶，帶來俗稱『死人簿』之資料；正式名目為『絕戶支』。"
    - "其描述：用於失蹤／死亡／不便公開工人之欠薪、家給、屍體、水路或封口等秘密支出；具體每一筆用途仍需查。"
    - "其鞋底藏有前一日抄下的一頁。"
    - "條目包括：丁七40河工、己三25家給、癸九80水、丙十一120未結。"
    - "癸九日期為柳生失蹤三日後；是否柳生未知，『水』含義未知。"
    - "丙十一日期為今日；『未結』據何稱可在事件發生前先開項，但仍需獨立查證。"
    - "何進安後來回憶丙十一旁曾有一個小『梁』字，後被二掌櫃刮掉；目前只有其證言。"
    - "押送途中車內遭箭投／威脅紙：『交人則全家死』。原件已由開封府封存。"
  public_banner:
    - "白御行後命潘金蓮做巨大『交人則全家死』布牌公開懸掛，以提高威脅事件可見度。"
    - "布牌只是宣傳／警示，不是證物本體；來源不得自行歸咎任何一方。"
```

---

# 11｜西門慶：被棄子後主動交出暗櫃

```yaml
XIMEN_CURRENT:
  status: "IN_KAIFENG_CUSTODY; ACTIVE_SELF_PRESERVATION"
  confirmed:
    - "西門慶在開封府供稱昨日曾勸梁福逃。"
    - "他稱梁福危險來源為廣源，點名許奉年。"
    - "他稱許奉年曾透過人傳話，梁福知道太多，應暫離京；他又稱杜成參與傳警。"
    - "上述皆為西門慶供述，第三人罪責需獨立互證。"
    - "在太尉府正式表示不庇護梁福／杜成之後，西門慶主動提出開西門府書房暗櫃。"
    - "他要求官員、章文度與兩名獨立帳房在場，文件全部交開封府控制。"
    - "西門慶明示：『有些東西，放在我家裡時是我的催命符；放到包府尹手裡，才是我的保命符。』"
  structural_state:
    - "其策略是用可進卷、可獨立查的資料提高自身活著的價值。"
    - "不得預設他下一步必然說真話，也不得預設所有暗櫃文件都是偽造。"
```

---

# 12｜暗櫃第一層至「高宅舊事」

## CAB20-E01｜廣源帳與路線副簿

```yaml
SECRET_CABINET_LAYER_1_2:
  confirmed:
    - "第一層為銀票、地契、借據等普通商業文件。"
    - "第二層發現十二冊廣源暗帳，以及玄字／青字路線副簿。"
  effect:
    - "沈萬三在十三娘賭局中下注『廣源母簿去向』因此變亮，但尚未判定已中。"
```

## CAB20-E02｜高宅舊事／陳氏女

```yaml
GAO_HOUSE_OLD_CASE:
  container_label: "高宅舊事"
  contents:
    - "一張女子賣契"
    - "兩張傷勢／醫治單"
    - "五百兩銀號兌票"
    - "兩封西門府與高宅往來短簡"
    - "一份開封府舊狀撤回抄件"
  old_complaint:
    - "布商之女陳氏於元宵燈會後失蹤，三日後受傷返家。"
    - "其父曾控『高衙內強擄民女，拘於城西別宅』，後撤狀。"
  relevant_letters:
    - "疑似高宅管事：『公子失手，陳家不識抬舉，煩大官人料理。』"
    - "另一無署名：『五百已付，狀已撤，人勿再動。』"
  legal_status:
    - "文件存在可成為重新找陳家、查筆跡、查銀號與舊卷的線索。"
    - "五百兩與撤狀在時間上相關，不等於已證明是封口銀。"
    - "包拯已封存，未因文件存在即直接定罪。"
  ximen_statement:
    - "西門慶稱保留此類資料，是要證明自己不是只有一張嘴。"
```

## CAB20-E03｜林教頭／陸某線索

```yaml
LIN_FAMILY_HINT:
  confirmed_documents:
    - "『林教頭家事，勿再經府。』"
    - "『陸某已辦，公子可安。』"
    - "一張舊一百兩兌票，收受姓『陸』。"
  not_established:
    - "『林教頭』確指林沖。"
    - "『陸某』確指陸謙。"
    - "一百兩用途。"
    - "林娘子遭高衙內直接殺害。"
  director_correction:
    - "目前只可談高衙內長期騷擾／逼迫林娘子、林沖被陷害流放等可查方向；不得把『被玩死』當已證實直接殺人。"
```

---

# 13｜《觀止五千》暗櫃資料與潘金蓮責任邊界

```yaml
GUANZHI_5000_ENVELOPE:
  label: "觀止五千"
  contents:
    - "西門府五千掛牌付款副本／存根"
    - "掛牌夜席次與競價簡錄"
    - "無署名短箋：『照約出價。散後由後門回。阿麗婭不動。餘事後議。』"
    - "西門慶私人備忘：『五千非買人。買牌，買名，買眾人不敢碰。潘有她的算盤，我有我的回報。散場之後，另算。』"
  evidence_status:
    - "可支持西門慶五千出價不是完全臨場起意，且存在事先安排之高度線索。"
    - "『潘有她的算盤』是西門慶個人備忘中的判斷／描述，不單獨證明潘金蓮完整內心或所有前置計畫。"
    - "文件沒有一句直接證明潘金蓮命令打柳生、事前知道柳生必到、或五千即殺人錢。"
  ximen_trigger:
    - "包拯問『散場之後，另算何事？』時，西門慶答：『這一件，請潘五娘自己來說。』"
  pan_response:
    - "潘金蓮明示願意上堂面對，不先逃避。"
```

---

# 14｜阿麗婭五千兩法律狀態

```yaml
ALIYA_5000_STATUS:
  current: "UNDER_OFFICIAL_CLARIFICATION"
  confirmed_questions:
    - "當年五千兩究竟取得何種權利。"
    - "是否全額支付。"
    - "期限、終止條件與是否仍存效力。"
    - "若舊權消滅，阿麗婭僅解除西門慶該項限制，還是另有後果。"
  aliya_position:
    - "阿麗婭自願去開封府聽官府確認『我現在還是不是他的／五千是否還能決定我的事』。"
    - "她沒有因此同意重新掛牌。"
  pan_business_interest:
    - "潘金蓮承認若阿麗婭日後自願重新掛牌，商業價值極高。"
    - "該想法不具有對阿麗婭的強制力。"
  still_unknown:
    - "官府最終如何認定五千兩權利效力。"
```

---

# 15｜太尉府給潘金蓮的「鬼牌」私函

```yaml
TAIWEI_PRIVATE_LETTER:
  status: "EXISTS; CONTENT_PRIVATE_AND_UNKNOWN_TO_FENGMANLOU"
  recipient: "潘金蓮本人"
  sender: "太尉府"
  confirmed_chain:
    - "太尉府差役將封緘私函送到觀止，明示收件人為潘金蓮本人，不是觀止公開公文。"
    - "潘金蓮拒絕讓風滿樓、白御行、蘇清、許慎言等人自行查看。"
    - "她先自行拆閱／處理，內容未公開。"
    - "後續潘金蓮主動前往開封府，把原函、原封、送達時間與差役身分交包拯秘密查驗。"
    - "包拯確認：若內容涉及正在查的案件，可能依法取得案卷法位；潘金蓮知情後仍自願交查。"
    - "風滿樓只被准許公開『潘金蓮已自願把太尉府私函交開封府秘密查驗』，不公開內容。"
  prohibition:
    - "不得推定信中是威脅、收買、滅口、合作或其他任何具體內容。"
    - "不得因其神秘就自動升格為犯罪證據。"
```

---

# 16｜十三娘問心賭局

```yaml
SHISANNIANG_BET:
  status: "ACTIVE_UNRESOLVED"
  stake_rule:
    - "不賭銀。"
    - "輸者未來欠十三娘一個真實回答。"
    - "只准拿自己的真話下注，不得押別人的秘密、性命或家人。"
  target:
    - "西門慶下一步真正拿來保命、能進卷並改變局勢的東西。"
  bets:
    沈萬三: "廣源母簿的去向"
    趙受益: "一封不能只有西門慶自己證明真假的信／可在他死後仍可驗證的備份"
    蘇清: "西門慶不是單純咬人，而是會開條件／要求保護"
    白御行: "高衙內的另一個案子；必須與柳生不同，且足以讓開封府合法另查"
    潘金蓮: "拒絕下注"
  current_brightness_only:
    - "陳氏女舊案資料使白御行之下注高度發亮，但十三娘尚未正式判定勝負。"
    - "廣源十二冊暗帳使沈萬三之下注變亮，但未確認即母簿。"
    - "西門慶以暗櫃換保命價值與先保文件再答之姿態，使蘇清方向部分吻合，但未結算。"
    - "趙受益之『可獨立驗證、死後仍成立的信』尚未明確出現符合物。"
  anti_closure:
    - "不得因局勢像某人的答案，就提前替十三娘宣布輸贏。"
```

---

# 17｜西門慶供出柳生案「丙七」青篷車

```yaml
LIUSHENG_BINGQI:
  source: "西門慶本人供述"
  confirmed_statement:
    - "西門慶稱柳生被打到站不起來後，最後不是直接拖去長街河邊，而是由觀止側巷抬上一輛青篷車。"
    - "他稱該車屬太尉府外院車馬房。"
    - "他報出的牌號為『丙七』。"
    - "他稱暗櫃高宅舊事中可能另有車馬牌簡記可供查。"
  official_response:
    - "包拯禁止直接把數年前柳生案的『丙七』與今日浮屍身上的『丙七』視為同一條因果。"
    - "開封府將先查太尉府車馬房舊制、牌號是人牌／車牌／值房牌、歷年是否沿用、當夜領牌與值勤紀錄。"
  status:
    - "高價值交叉線索；尚未閉環。"
```

---

# 18｜蘇清正式委託許慎言：口頭賭約、賣身契、後堂帳分軸

## SUQ20-E01｜委託成立

```yaml
SUQING_LEGAL_REPRESENTATION:
  status: "AUTHORIZED_BY_SUQING"
  client: "蘇清"
  lawyer: "許慎言"
  payer: "白御行"
  confirmed:
    - "白御行表示無論狀子成不成、贏不贏，希望許慎言接案並由白御行買單。"
    - "蘇清本人明示委託許慎言。"
    - "許慎言不承諾一定提告、一定撤契或一定勝訴；先查資料，再決定合法攻點。"
  humorous_nonessential:
    - "白御行另送『觀止七十二次按摩券』作玩笑式謝禮；不構成案件交換條件。"
```

## SUQ20-E02｜三條必須分開的法律／證據軸

```yaml
SUQING_THREE_AXES:
  axis_1_oral_wager:
    status: "HISTORICAL_ORAL_AGREEMENT_EXISTS; FULL_TERMS_UNPROVEN"
    rules:
      - "蘇清與潘金蓮當年確有口頭賭局歷史。"
      - "到目前沒有正式書面賭約可證全部條款。"
      - "人物記憶、後來轉述與歷史印象可作證言或旁證，但不得冒充硬契。"
  axis_2_formal_sale_indenture:
    status: "FORMAL_DOCUMENT_CURRENTLY_VALID"
    confirmed:
      - "蘇清本人自願同意並簽署／畫押。"
      - "該正式賣身契不能只因口頭賭局爭議或阿麗婭五千權利失效就當然作廢。"
    invalidation_requires:
      - "契文本身的脅迫、欺詐、法定瑕疵，或"
      - "可證明契約明示受某條件拘束且條件失敗"
  axis_3_backroom_accounting:
    status: "NEW_ACTIVE_LEGAL_QUESTION"
    question:
      - "潘金蓮把蘇清送入西門府一月時，是何種法律／契約性質。"
      - "蘇清身契是否轉移。"
      - "有無金錢對價或服務價值入帳。"
      - "若未轉身契但用蘇清一月履行完成潘／西門之交易，該價值是否應計入蘇清自身帳項、贖身帳或另有返還／結算問題。"
```

---

# 19｜《五千後算》：開冊硬狀態

## WQ20-E01｜舊簿發現與封送

```yaml
WQ_HOUSUAN_BOOK:
  discovery:
    - "觀止舊後堂帳因開封府調取阿麗婭掛牌當夜後堂結算而重新整理。"
    - "春梅發現一本薄舊簿，封面右下角有褪色四字：『五千後算』。"
    - "許慎言制止現場私拆，要求原樣封存、記位置、到開封府在官吏與見證人面前開冊。"
  custody:
    - "觀止、帳房、開封府依程序封送。"
    - "開封府已在見證下開冊。"
```

## WQ20-E02｜第一組可見帳文

```yaml
WQ_HOUSUAN_VISIBLE_ENTRIES:
  observed_in_official_opening:
    - "『阿麗婭——留觀止，不交人。』"
    - "『西門慶——五千掛名，得預定之名。』"
    - "『散後另算。』"
  evidence_effect:
    - "支持當年五千安排至少在觀止後堂帳中被記成『掛名／預定之名』而非普通立即交人。"
    - "不自動決定阿麗婭今日法律狀態；仍須看完整契據、付款、期限與法理。"
```

## WQ20-E03｜蘇清條目

```yaml
SUQING_BOOK_ENTRY:
  observed_text:
    - "『蘇清，敗約後入西門府一月。』"
    - "『身契不轉。仍存觀止。』"
    - "『作西門大官人掃興之補。』"
    - "『不另折銀。』"
  current_hard_meaning:
    - "目前可確認該舊簿如此記載。"
    - "蘇清身契在該帳文中被記為不轉給西門慶、仍存觀止。"
    - "蘇清一月入西門府被記入潘／西門之後堂結算語境，並被稱為『補』。"
    - "『不另折銀』表示帳面沒有另列一個對蘇清的一次性折銀價；不等於蘇清客觀價值為零。"
  legal_unknowns:
    - "當時觀止依賣身契是否有權作此類派遣。"
    - "服務／派遣價值是否依法本來歸觀止。"
    - "是否應計入蘇清自己的贖身、分成或其他帳項。"
    - "有無其他隱藏／配套帳冊改變解釋。"
```

## WQ20-E04｜第三頁備忘

```yaml
WQ_HOUSUAN_MEMO:
  observed_text:
    - "『蘇清入府後，阿麗婭仍留。』"
    - "『五千之名不得撤，撤則前局皆廢。』"
  status:
    - "帳冊備忘存在。"
    - "『前局』之全部內容不由此兩句自動補全。"
```

---

# 20｜潘金蓮在開封府之本人供述

```yaml
PAN_JINLIAN_TESTIMONY:
  status: "PARTIAL_SELF_TESTIMONY; NOT_TOTAL_OBJECTIVE_TRUTH"
  confirmed_statements:
    - "潘金蓮承認五千掛牌夜不是普通即興掛牌。"
    - "她承認曾主動找西門慶，利用其出價能力與名聲把阿麗婭身價推高，同時讓外界認為碰阿麗婭等於碰西門慶之預定對象。"
    - "她表述核心效果是讓阿麗婭留在觀止、不被直接帶走，並借西門慶名義形成保護性威懾。"
    - "她承認《五千後算》中涉及蘇清『作掃興之補』『不另折銀』等字句出自自己的帳法／安排。"
    - "她表示：與蘇清打口頭賭局時，她確實考慮過若蘇清輸，敗約後要如何收束／交付。"
    - "她明示：並非從一開始就固定『一定送給西門慶』；西門慶是後來成為合適的承接者。"
  unresolved:
    - "口頭賭局完整原始條款仍未被硬證據證明。"
    - "潘是否在每一個早期節點已預見柳生、高衙內、五千與蘇清全部後果，不能從其目前供述逆推。"
    - "潘與西門是否還有未公開之其他交換內容。"
  critical_boundary:
    - "潘承認五千安排與蘇清後堂交付，不等於承認自己命令高衙內施暴、命令手下處理柳生或參與柳生死亡。"
```

---

# 21｜蘇清目前訴訟／查帳方向

```yaml
SUQING_CURRENT_LEGAL_GOAL:
  immediate_goal:
    - "不以『我從未同意賣身』作方便故事。"
    - "不先主張正式賣身契當然無效。"
    - "要求把當年從口頭賭局、正式簽契、五千掛牌、敗約、入西門府一月、回觀止之間的帳與文書完整拆開。"
  new_core_question:
    - "觀止是否可在不另計價、不記入蘇清自身帳項的情況下，以蘇清一月之履行利益完成潘金蓮與西門慶間的交易／結算。"
  requested_documents:
    - "蘇清正式賣身契原件"
    - "簽契當日見證、經手與帳房登錄"
    - "是否存在身契轉移文件"
    - "蘇清入西門府一月之觀止帳目／收入／支出／回帳"
    - "阿麗婭掛牌前後之後堂結算與五千兩資料"
    - "當年口頭賭約之見證、旁證、相關帳錄"
  requested_procedure:
    - "蘇清希望在開封府查閱涉及自己姓名、身契與該一月的部分；不主張查看觀止全部商業帳。"
  stated_attitude:
    - "即使最後證明契有效、潘依法有派遣權、自己沒有可取回銀兩，她仍要查清楚。"
    - "她要求潘金蓮先讓帳說、讓西門慶說、再由潘與她各自說，不接受先用漂亮敘事收口。"
```

---

# 22｜西門慶、潘金蓮、蘇清三方目前互咬結構

```yaml
TRIANGULAR_STATE:
  ximen_qing:
    - "以暗櫃、舊案與後堂資料增加自己活著的交換價值。"
    - "把『散場之後另算』推回潘金蓮本人說明。"
  pan_jinlian:
    - "沒有否認五千局與蘇清後堂結算。"
    - "選擇上堂、交帳、承認部分自己做過的安排。"
    - "仍可在法律上主張自己當年依契有權派遣蘇清、帳務不欠蘇清等抗辯；尚未裁決。"
  su_qing:
    - "不靠否認自己簽契求脫身。"
    - "轉而攻擊『她的一月履行如何被用來結潘／西門的帳，卻未記到她自身帳上』。"
  structural_result:
    - "三方皆有可說之法位；目前沒有任何一方已獲終局勝負。"
```

---

# 23｜趙受益與身分邊界

```yaml
ZHAO_SHOUYI:
  current_public_name: "趙受益／趙先生／趙兄"
  confirmed:
    - "其曾由觀止秘密／地下通道方式出現並留在大堂看整夜大局。"
    - "對朝廷、皇帝、權門程序有異常熟悉程度。"
    - "曾由潘安排紅袖、浮香、辭歲可自行決定是否陪談；三人皆依自身意願行事。"
    - "他與李師師有瘦金字體玩笑，雙方均否認因此定情。"
  prohibited:
    - "不得由導演自動公開其更高真實身份。"
```

---

# 24｜辭歲假設掛牌賭價

```yaml
CISUI_HYPOTHETICAL_AUCTION:
  status: "HYPOTHETICAL_ONLY"
  confirmed:
    - "辭歲尚未設定正式掛牌日。"
    - "她曾拒絕白御行先前要求『二十八日後仍永久保持心理牽引／不可撤回慾望』的條件。"
    - "她明示拒絕的是該契約條件，不是永久禁止白御行未來參與合法掛牌。"
    - "假設性出價曾出現：沈萬三1500、趙受益1800、李師師代理白御行2000。"
  rule:
    - "未來真掛牌，誰有資格參與由辭歲與觀止當時規則決定。"
    - "假設出價不建立任何性、關係或交易權。"
```

---

# 25｜常煒與白三娘

```yaml
CHANGWEI_BAISANNIANG:
  status: "VISIBLE_INTEREST_ONLY"
  confirmed:
    - "白御行曾調侃常煒是否喜歡白三娘、是否要贖作妾。"
    - "常煒承認自己確實多看過白三娘幾眼，欣賞其實際照料與作風。"
    - "白三娘若要談離觀止，優先問的是她自己想不想走、想過什麼生活；妾位或價錢不是第一問。"
    - "常煒表示若真去問，不會以價格開場。"
  not_established:
    - "戀愛"
    - "贖身交易"
    - "婚／妾約"
```

---

# 26｜白御行關於「枕邊人／背叛」之本輪台詞法位

```yaml
PLAYER_UTTERANCE_TRACE:
  confirmed_player_statements:
    - "白御行表示自己更相信睡在身邊的女人，認為背叛機會可能較低。"
    - "白御行補充：自己曾被最愛的女人背叛，因此並非不知道親密關係會失敗。"
    - "其真正重點是：越親近，敏感的人越可能察覺對方態度／心意變化；屬下則可能用制度性表面更容易隱瞞。"
  world_effect:
    - "形成白御行、沈萬三、蘇清、潘金蓮、李師師等一輪用人／信任討論。"
  not_established:
    - "枕邊人客觀上必然更忠誠。"
    - "白御行一定能準確判定任何人的變心原因。"
    - "任何現有女人因此取得或喪失關係資格。"
```

---

# 27｜立即未決事項

```yaml
OPEN_HOOKS:
  highest_priority:
    - "《五千後算》其餘頁面是否還有更直接的結算、價值、簽名、轉移或相關人名。"
    - "蘇清正式賣身契原文究竟授予觀止／潘金蓮何種派遣、收益與贖身權。"
    - "蘇清入西門府一月之收益是否有其他帳項，是否應計入其個人帳／贖身帳。"
    - "阿麗婭五千兩『預定之名』今日法律效力如何。"
    - "潘金蓮與西門慶『散場之後另算』是否仍有尚未出現的內容。"
    - "蘇清只願先向包拯私供之西門慶秘密內容。"
    - "太尉府私函的內容及其是否被包拯判定與案情相關。"
    - "西門慶暗櫃是否還有下一層保命資料。"
    - "陳氏女舊案是否取得足以正式另查的獨立來源。"
    - "林教頭／陸某線是否可獨立指向林沖／陸謙。"
    - "柳生案『丙七』與今日浮屍丙七是否只是沿用牌號、栽置，或存在歷史連接。"
    - "梁福、杜成、許奉年各自目前下落與責任。"
    - "廣源母簿真正位置。"
    - "何進安『丙十一／梁』是否涉及梁福及『未結』預開用途。"
    - "十三娘問心賭局最終誰中。"

  relationship_open:
    - "李師師私人帳何時真正修復／是否修復。"
    - "李瓶兒法律切割西門慶後，是否接受如夫人位置及何時成立。"
    - "張麗華在白御行選李瓶兒之夜後的實際反應尚未演出，不得補寫。"
    - "蘇清二十八日私人約仍只有在西門慶真正失勢／倒台後開始；目前尚未啟動。"
    - "若西門慶真正倒台，蘇清曾表示可能另加第二十九日；尚未到觸發點。"
```

---

# 28｜法律戰硬規則／防導演過度收斂

```yaml
LEGAL_WAR_INVARIANTS:
  - "在場 ≠ 下令暴力。"
  - "同日 ≠ 因果。"
  - "帳冊證明金流 ≠ 自動證明用途。"
  - "銀角剪痕／牌號習慣 ≠ 指令來源。"
  - "供述可成線索，第三人罪責仍需互證。"
  - "秘密文件存在 ≠ 文件內容全部真實。"
  - "公開風滿樓提高可見性與證人安全成本，不等於提高證據力。"
  - "定陶商會無官府拘捕權；只能保護、觀察、傳遞、提供資源。"
  - "包拯不得只靠政治直覺非法搜太尉府。"
  - "高俅／太尉府可聘狀師、做程序抗辯、分案、切割責任；不得預設必敗。"
  - "西門慶可撒謊、切人、交真證、交半真資料、談條件；不得預設其必然被滅口或必然翻供。"
  - "潘金蓮承認五千局 ≠ 承認柳生暴力。"
  - "蘇清賣身契有效 ≠ 潘金蓮的所有歷史帳務必然合法。"
  - "阿麗婭五千權利失效 ≠ 阿麗婭欠新掛牌。"
  - "『閉環』只在證據真正互證時成立，不得用故事高潮替代法律閉環。"
```

---

# 29｜下一導演接關警告

```yaml
CONTINUATION_GUARD:
  must_preserve:
    - "目前 HOLD，不推進時間，直到玩家解除 HOLD／明示繼續。"
    - "白御行的台詞、行動、內心與重大選擇仍由玩家控制。"
    - "潘金蓮目前最後確認在開封府，不得無交代瞬移回觀止。"
    - "蘇清口頭賭約完整條款未證，不得寫成已有正式原約。"
    - "正式賣身契目前有效，不得因『五千後算』一出就直接宣判作廢。"
    - "《五千後算》目前證明的是帳文存在＋部分潘本人供述；法律效果仍待審。"
    - "太尉府私函內容保持 UNKNOWN，除非後續由潘、包拯、正式卷宗或合法事件揭露。"
    - "柳生是否死亡保持 UNKNOWN。"
    - "阿麗婭是否解除五千預定權保持 UNDER_OFFICIAL_CLARIFICATION。"
    - "十三娘賭局保持未結算。"
    - "風滿樓是觀止內部大型公域拓撲展開，不回退成『整條街觀眾席』版本。"
    - "說書先生只能轉述公開材料，不能因高潮自行補罪。"
    - "西門慶仍是會自救、會談條件、有律師的主動人物，不是等死反派。"
    - "潘金蓮仍可用帳、權、風月與生存角度抗辯，不得因被查帳就洗成認錯道德講師。"
    - "蘇清目前主攻帳與法位，不是突然變成受害療癒話術人物。"
  next_scene_candidate:
    - "開封府繼續讀《五千後算》／查正式賣身契與相關帳。"
    - "包拯處理阿麗婭五千權利之初步法理。"
    - "潘金蓮就後堂帳與自己當年權限提出正式抗辯。"
    - "西門慶繼續以暗櫃或條件換取保命。"
    - "太尉府或廣源提出新的程序／證據反擊。"
  no_forced_choice_menu: true
```

---

# 30｜本 HOT 的一句接關摘要

> **風滿樓已開，數千人看的是一場尚未有結局的公案。西門慶靠暗櫃把自己的命變成證據市場；潘金蓮把太尉府鬼牌交給包拯秘密查，又被《五千後算》迫回自己當年的後堂局；蘇清不否認自己簽過賣身契，改以「我那一月究竟被怎麼算帳」向潘金蓮追索法位與帳目。此刻帳已開，勝負未判。**

<!-- SOURCE_HOT_V2_4_END -->

---

## SOURCE ARCHIVE｜HOT V2.5

**檔名：** `觀止青樓_白御行線_HOT_SAVE_V2.5_槐月二十日深夜_開封法網擴張_阿麗婭重定義與六條御息所來訪版.md`  
**SHA-256：** `a2107c0df322779ea1ed0f74a59502c63ea52594fded2a295a258f6e68997083`

<!-- SOURCE_HOT_V2_5_BEGIN -->
# 觀止青樓｜白御行線 HOT SAVE V2.5
## 理火三年槐月二十日深夜｜開封法網擴張 × 阿麗婭身分重定義 × 六條御息所來訪 × 趙受益茶約前置版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V2_5_HUAI20_LATE_NIGHT_KAIFENG_NET_AALIYAH_ROKUJO"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V2.5"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime:
    - "GUANZHI_QINGLOU_V10_0"
    - "GUANZHI_QINGLOU_V10_1_V10_2_PATCH_WHEN_APPLICABLE"
  story_date: "理火三年槐月二十日深夜"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AT_GUANZHI_INNER_COURTYARD_AFTER_ROKUJO_GUEST_ROOM_ACCOUNT"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V2.4_槐月二十日深夜_風滿樓公案與五千後算開冊版.md"
  previous_hot_sha256: "ad757d9a4b2e612b0c606d44dbf55c857d40e8d7e792db18839a3faa50d088f5"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"
  current_location: "觀止青樓／內院；風滿樓與開封府法律線仍並行運作"
  direct_resume_owner: "WORLD_OR_PLAYER_AFTER_HOLD_RELEASE"
  save_scope:
    - "HOT V2.4 後開封府對西門慶、高衙內、廣源、杜成、梁福等之法網擴張"
    - "五千後算後續：西門慶接受蘇清一月作替代結算、潘金蓮筆跡殘條與蘇清兩時段法位切割"
    - "阿麗婭舊五千掛牌之初步法律狀態、目前半良家／準妓女位置與未重新掛牌決定"
    - "阿麗婭對未來出閣制度、候選篩選與一期婚之候選構想"
    - "趙受益與紅娘氏既往第一筆紅倌交易之去污染校正"
    - "白御行關於龐春梅、疏影、親密關係與女人之本輪有效自我陳述"
    - "人物圖畫展示事件及其人物反應；不自動改人物基線"
    - "六條御息所以共鳴召喚／未知來客形式進入觀止之 ROUTE EVENT"
    - "六條御息所與白御行之源氏資訊對談、與趙受益之初次認識及茶約前置"
    - "六條御息所今晚女客住宿安排與趙受益代付之無權利帳務"
```

---

# 0｜提交法位、來源與反污染說明

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V2.4_槐月二十日深夜_風滿樓公案與五千後算開冊版.md"
    role: "本檔直接前置 HOT；V2.4 以前事件全部繼承"
  long_term_master:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"
    role: "長期因果與早期玩家線來源；僅固化至 HOT V1.9"
  route_conversation_commit:
    role: "HOT V2.4 之後至本次 SAVE 命令的直接劇情來源"
  persona_source:
    file: "觀止人物卡_LCAPG_V1.1-R1_原始重構去污染版_含辭歲_導演隱藏區增補.md"
    role: "原生人物基線來源；本檔不得以玩家線事件倒灌修改"
  character_pool:
    file: "觀止人物池_LCAPG_V1.1_紅娘氏與李師師雙人正式版.md"
    role: "紅娘氏、李師師平級人物來源"
  summoning_rule_source:
    file: "觀止青樓版V10.0_成人場景Runtime_人物主權_安全層降權_反聖母污染正式版.md"
    role: "人物召喚／未知來客／共鳴召喚之文件級規則來源"

COMMIT_NOTE:
  - "本檔取代 HOT V2.4，成為白御行線當前直接接關切片。"
  - "本次只做 HOT SAVE；不更新 MASTER、不改人物卡、不改人物池、不新增六條御息所至常設人物池。"
  - "六條御息所本次屬白御行線 ROUTE_EVENT／UNKNOWN_VISITOR_ARRIVAL；是否長住、掛牌、成為常設人物均未成立。"
  - "玩家在劇情中對六條御息所、光源氏、藤壺、紫姬、秋好等所述未來故事內容，保存為『白御行提供之未來資訊／故事敘述』；除非另有世界來源互證，不得自動升格為六條原時代的客觀可證事實。"
  - "玩家對六條『最想要權力／其實不愛源氏只愛血統』之判斷，六條本人未接受為定論；此項不得寫成她的固定內心真相。"
  - "人物圖畫只保存為本輪展示物與人物反應；圖上文案不自動成為人物履歷、世界真相、公開招牌或人物卡描述。"
  - "人物說『收了／拿走』圖畫可保存為當下持有／表態；白御行未明示贈與時，不擅自補成法律所有權永久轉移。"
  - "開封府之供述、官方暫時處置、證人證詞、帳冊與 DIRECTOR_FIXED_HISTORY 分軸保存。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年槐月二十日"
  time: "深夜；精確時刻未定"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"
  primary_location: "觀止青樓／內院"

  player:
    name: "白御行"
    location: "觀止內院"
    last_confirmed_utterance:
      - "『人家沒成交，不算賣。』"
    no_new_player_action_after_save_command: true

  confirmed_present_or_immediately_active_in_inner_courtyard:
    - "白御行"
    - "六條御息所"
    - "趙受益"
    - "蘇清"
    - "李師師／可從聽雨小閣或內院近處參與"
    - "張麗華"
    - "紅娘氏"
    - "十三娘"
    - "阿麗婭"
    - "春梅／已介入女客房與帳務安排"
  intermittent_or_exact_position_not_required:
    - "小翠曾在圖畫展示時出現；當前是否仍坐同桌 UNKNOWN"

  offsite_confirmed:
    潘金蓮:
      current: "開封府"
      status: "接受五千後算、蘇清替代結算及相關權限問題查問"
    西門慶:
      current: "開封府羈押／訊問中"
    包拯:
      current: "開封府主持多線並行程序"

  direct_resume_point:
    - "六條御息所已被安排今晚暫住內院東偏廂女客房，但尚未確認她已離席或進房。"
    - "趙受益已同意支付六條今晚客房、茶食、必要衣物日用等女客開銷，並明示不因此取得任何人身、服務、陪宿、性、關係或契約權利。"
    - "六條與趙受益只成立『初次認識＋今晚可同桌喝茶』；未成立戀愛、交易、陪宿、婚配、候選承諾。"
    - "六條牛車與紅楓異路最後確認仍在月門外附近，春梅命人暫勿碰；其能否作為返回原時代的通道 UNKNOWN。"
    - "開封府法律線仍在並行推進，但本鏡頭已回到觀止人物／關係場。"
```

---

# 2｜開封府：五千後算後續硬進展

## KFY20-E01｜西門慶承認蘇清一月為五千替代結算

```yaml
SUBSTITUTE_CONSIDERATION_RECORD:
  evidence_status: "HARD_COURT_RECORD_BY_ADMISSION; FINAL_LEGAL_EFFECT_NOT_YET_JUDGED"
  confirmed:
    - "西門慶在開封府明示：潘金蓮後來對其表達過『阿麗婭不給你；蘇清那一月你也拿了；五千那筆別再翻』之意。"
    - "潘金蓮承認自己曾對西門慶作出此類結算表述。"
    - "西門慶承認自己接受蘇清一月作為替代結算，因此其後未再要求取得阿麗婭。"
  current_effect:
    - "形成強硬記錄：五千帳名在阿麗婭，實際替代利益落在蘇清一月，且西門慶接受替代。"
    - "此記錄強烈削弱西門慶再以舊五千要求阿麗婭出閣／帶走／性服務之主張。"
  not_yet_final:
    - "對潘金蓮與觀止之民事、帳務、契約責任最終如何切割。"
    - "蘇清一月之法定價值、收益歸屬與損害是否成立。"
```

## KFY20-E02｜潘金蓮筆跡殘條

```yaml
PAN_FRAGMENT:
  evidence_status: "PHYSICAL_FRAGMENT_PLUS_HANDWRITING_ADMISSION"
  observed_text:
    - "『……蘇清一月，抵五千後帳。』"
    - "『……人不轉契。』"
    - "『……西門自取。』"
    - "『……月滿還樓。』"
  confirmed:
    - "潘金蓮承認殘條字跡為自己所寫。"
    - "殘條上下文殘缺。"
    - "潘承認自己可能曾讓西門慶『自行找／自取』蘇清，但否認因此授權暴力拖拽、囚禁、威脅或強迫性行為。"
    - "西門慶主張其當時理解為可以自行把蘇清弄到府中；此為其本人說法。"
  prohibited_inference:
    - "『西門自取』不得直接等同『潘命令家奴暴力抓人』。"
    - "殘條不能單獨證明潘知悉每一個後續強制手段。"
```

## KFY20-E03｜蘇清兩時段切割

```yaml
SUQING_TWO_PERIODS:
  government_archive_found:
    pre_ximen_month:
      confirmed_absence:
        - "未找到蘇清原始服務報備。"
        - "未找到處女良家掛牌申請。"
        - "未找到合法首次出閣拍賣文件。"
    post_return:
      confirmed_document:
        - "蘇清在西門府二十八日後返回觀止，親自提出入妓籍／紅倌方向之申請。"
        - "申請內容表明其已非處女，不要求走處女良家首次出閣拍賣路徑。"
        - "文件有蘇清本人書寫／畫押；蘇清在當前程序中確認筆跡與當時自願決定。"
  bao_current_split:
    period_1: "西門府二十八日：合法性與強制問題另查；不得被後來自願入妓籍回溯洗白。"
    period_2: "回觀止後自願入妓籍：具獨立成立可能，可作目前妓籍／紅倌身分之另一路合法來源。"
  current_boundary:
    - "後來自願留在觀止，不等於前二十八日自願。"
    - "前二十八日若違法，也不自動令她後來自主申請全部失效。"
```

## KFY20-E04｜蘇清原始被送入西門府之因果分層

```yaml
SUQING_FORCED_MONTH_CAUSAL_SPLIT:
  director_fixed_history:
    - "蘇清當年實際被西門府家奴以暴力拖入偏院。"
    - "西門慶對蘇清以死亡／折磨等方式施壓，實際控制其二十八日。"
  current_public_or_court_evidence:
    - "潘金蓮與西門慶之替代結算關係已有硬記錄。"
    - "潘筆跡『西門自取』存在，但授權暴力與否尚未被硬證據證明。"
  legal_split_to_preserve:
    pan_jinlian_axis: "把蘇清一月納入其與西門五千後帳，以及當時是否具有處分／派遣蘇清之權。"
    ximen_qing_axis: "實際取得、暴力拖拽、囚禁、威脅及可能的性強迫責任。"
    su_qing_later_choice_axis: "月滿回觀止後之自願入妓籍決定，獨立評價。"
```

---

# 3｜阿麗婭：舊五千權利、目前身分與未重新掛牌

```yaml
AALIYAH_CURRENT_STATUS:
  legal_base:
    status: "半良家／準妓女"
    cause:
      - "阿麗婭曾完成政府服務報備，可進堂作非性服務。"
      - "其曾本人申請掛牌並有五千拍賣結果，但未實際出閣到西門府。"
      - "未發生 D+0 首次出閣、未發生二十八日妾期、未發生 D+28 休回，因此原本未來生效之售契條件未完成。"
  kaifeng_provisional_position:
    - "西門慶又已承認接受蘇清一月作替代結算。"
    - "目前缺乏新文書時，舊五千不得用來要求阿麗婭被帶走、出閣或提供性服務。"
  current_choice:
    - "阿麗婭沒有在取得上述釐清後立刻重新掛牌。"
    - "她明示今晚先不重新把自己賣出去／不立刻進入新的首次出閣程序。"
  permitted_now:
    - "依半良家／準妓女位置，可做核准之非性堂務服務。"
  not_established:
    - "紅倌性服務義務"
    - "任何新首次出閣對象"
    - "白御行或趙受益對其之取得權"
```

---

# 4｜觀止籍制：本輪 GM 校正後的現行流程

```yaml
GUANZHI_STATUS_SYSTEM_CURRENT_GM_RULE:
  stage_0_entry:
    - "女子進觀止後尚不能直接服務。"
    - "由本人自願申請服務，觀止向官府報備數日。"
    - "官府做基本來源／逃奴等身家調查與資料留存，但不替申報內容保證絕對真實。"
  during_filing:
    status: "完整良家"
    rule: "不可入堂服務；辭歲曾在此階段遭鹽商騷擾。"
  after_filing:
    status: "半良家／準妓女"
    rule:
      - "可正式入堂談話、陪酒、非性服務。"
      - "不得因已報備就被當作紅倌性服務。"
      - "也不是完全自由離場的普通外客身分。"
  virgin_first_out_path:
    - "具資格之處女良家可本人申請掛牌出閣。"
    - "拍賣結算時同時簽售契與休書，但兩者均約定 D+28 才生效。"
    - "D+0 至 D+28：首次買主家中以妾身分生活二十八日。"
    - "D+28 休回後，觀止售契才生效，進入正式妓籍／紅倌路徑。"
  nonvirgin_or_slave_path:
    - "掛牌拍賣不是所有紅倌的必要前置。"
    - "奴籍或非處女等其他既有身分可依合法程序直接轉妓籍／紅倌，不必做處女首次出閣拍賣。"
    - "紅娘氏屬此類：無處女初出拍賣資格，走直接紅倌訓練／營運路徑。"
  invariant:
    - "妓籍取得 ≠ 一定經過拍賣。"
    - "拍賣＝處女良家首次出閣之特殊路徑。"
```

---

# 5｜阿麗婭：未來首次出閣／一期婚構想

```yaml
AALIYAH_FUTURE_CONCEPT:
  lifecycle: "PROPOSAL_IN_ROUTE_ONLY"
  confirmed_preferences:
    - "她對未來可能重新申請首次出閣仍有興趣，但不在今晚決定。"
    - "她希望公開程序不必等於毫無篩選的大規模價高者得；可先建立真正、公開、非造假的資格條件，再由合格者競價。"
    - "她關心的是二十八日共同生活是否合適，包括關係、生活、親密習慣、是否尊重 D+28 分開。"
    - "她不希望第一次出閣只是『被交付』。"
    - "她對『一期婚』概念有興趣：明知開始與結束、二十八日、自選男人。"
    - "她認為完成首次二十八日不應自動決定她之後要跟多少男人發生性關係；首次出閣與後續性服務應可分開討論。"
  regulatory_unknown:
    - "觀止與官府是否允許『指定首主』或僅限少數合格人公開競價，尚未成為正式制度。"
    - "才華、承諾、資產等非現銀條件能否折算為合法競價對價，尚未確認。"
```

---

# 6｜阿麗婭候選紙：白御行與趙受益

```yaml
AALIYAH_CANDIDATE_NOTES:
  status: "PERSONAL_EXPLORATORY_NOT_AUCTION_REGISTRATION"

  bai_yuxing:
    current: "留審／未報名／未承諾"
    self_disclosures_heard_by_aaliyah:
      - "白御行有張麗華情人關係。"
      - "白御行明示自己不是一對一專屬型男人，二十八日期間可能仍有其他女人。"
      - "白御行曾談及與張麗華、蘇清、李瓶兒等多人親密／群體經驗脈絡。"
      - "白御行與李師師已有性交，且曾在說『我愛你』後立即穿衣離開，成為李師師私人帳之一。"
      - "白御行主張自己有時故意做死，因為覺得好玩。"
      - "白御行主張部分負面形象可能是刻意自污以降低外界戒心；阿麗婭只記錄為本人主張，真偽待觀察。"
    aaliyah_current_assessment:
      - "若她要二十八日專屬／每晚回家型男人，白御行條件偏差。"
      - "若她選擇熱鬧、非專屬但坦白的二十八日，白御行仍可觀察。"
      - "她不希望每天都是多人性場景；偶發嘗試是另一題。"
      - "她重視候選人是否把當下同意誤認為所有權、是否親密後立刻離開、是否遵守 D+28 分開。"
      - "白御行在『親密後是否留下』項有重大前科，若真進候選需本人說明。"
      - "核心句：可以壞；不能拿『我就是這種人』逃掉後果。"

  zhao_shouyi:
    source: "白御行推薦"
    current: "可觀察；未報名；未承諾競標"
    confirmed:
      - "白御行向阿麗婭推薦趙受益，稱其人品好，並坦言不知道其床上能力。"
      - "趙受益明示：白御行推薦是白御行的事；阿麗婭要不要把他列入觀察是阿麗婭的事；他自己是否答問題、是否參與由自己決定。"
      - "趙受益沒有登記、沒有答應競價。"
      - "阿麗婭記錄為：可觀察／願意受問。"
```

---

# 7｜趙受益 × 紅娘氏：舊交易去污染校正

```yaml
ZHAO_HONGNIANG_CORRECTION:
  correction_status: "HARD_ROUTE_CORRECTION"
  confirmed:
    - "紅娘氏與趙受益／趙禎曾完成紅娘氏第一筆正式紅倌成人交易。"
    - "交易地點為紅娘氏房內。"
    - "交易屬 COMPLETED_ADULT_TRANSACTION。"
    - "房錢歸觀止；成人服務身體費歸紅娘氏。"
    - "既有 HOT／MASTER 沒有記錄確切性交姿勢、技術或床上細節，故不得自動補寫。"
    - "此前導演曾錯寫紅娘氏『沒有跟趙睡過』，該輸出已撤回，不具世界法位。"
  current_knowledge:
    aaliyah: "已在候選討論中得知紅娘氏與趙有過一筆成人交易。"
    rokujo: "尚無來源得知此事；不得自動知道。"
  hongniang_boundary:
    - "紅娘氏不願公開八卦趙受益床上細節。"
    - "若阿麗婭日後真認真考慮，可私下詢問紅娘氏願意透露的部分，或直接問趙本人。"
```

---

# 8｜開封府：法網已跨入拘捕、封存、廣泛證人階段

```yaml
KAIFENG_COERCIVE_PROCESS_THRESHOLD:
  current_mode: "PARALLEL_ARREST_SEIZURE_WITNESS_NET"
  confirmed:
    - "案件已不再只停留於偵探式尋線；包拯依不同法源分別簽發拘提、封存、證人傳喚與查驗命令。"
    - "廣源母簿不是官府採取行動的必要前提；其價值在於決定法網能再往上攀到哪裡。"

  gao_son:
    - "高衙內已因柳生遭毆打、強行帶離與失蹤相關事實被正式帶入開封府處理。"
    - "其承認曾在酒後說過『拖出去，打斷腿扔河裡』類命令。"
    - "目前不等於已判殺人。"

  gao_servants:
    - "當晚直接涉入之數名高府家僕被分開控制／訊問。"

  guangyuan:
    - "廣源東庫、暗帳房、高溫爐相關作坊已被封存／扣押文書。"
    - "核心人員被控制；普通工人以識別、詢問為主。"

  ducheng:
    - "杜成已進入正式拘捕／通緝法位，不再只是尋人。"

  liangfu:
    - "梁福若找到須先控制、查傷、隔離訊問。"
    - "官府同時把他視為可能涉案者與高風險證人；目前下落未知。"

  witness_summons:
    - "舊工人、車夫、陳氏案書手／銀錢經手、其他關聯人已被擴大傳喚。"
```

---

# 9｜丙七：已校正為車牌／車號，不是個人牌

```yaml
BINGQI_VEHICLE_CORRECTION:
  hard_correction:
    - "『丙七』為車輛／車牌識別，不是某一名人的身分牌。"
    - "此前若把丙七視為個人身分碼的路徑已撤回。"
  known_history:
    - "鄭老六過去通常駕駛丙七車，之後把車與牌交給杜成。"
    - "浮屍身上出現的真丙七牌，不等於浮屍就是杜成。"
  guangyuan_dispatch_book:
    entries:
      - "槐月初九—廣源東庫"
      - "槐月十三—西城"
      - "槐月十五—梁宅"
    note: "槐月十五後未見正常歸還記錄。"
  active_order: "尋丙七車"
```

---

# 10｜何進安、萬勝腳店、梁宅密窖與母簿去向

```yaml
MOTHER_LEDGER_TRACE:
  he_jinan:
    confirmed_testimony:
      - "三年前曾抄過一本厚黑皮總簿，內容以癸九、丙七、丙十一等碼記帳。"
      - "梁福是令其抄簿的人。"
      - "其理解下層帳是『給人查』，上層總簿是『給人活命』。"
      - "最後一次在廣源東庫夾牆見總簿；隔日見梁福與杜成抬走一只青綠皮木箱。"
      - "聽到『別送回宅，找腳店寄』。"
  wansheng_inn:
    - "寄存簿顯示『梁二』曾存青綠皮木箱並續寄兩次。"
    - "十一日前有人以『杜成』名義／取票取走；實際取箱者身分尚未完全核實。"
    - "票背記『移交梁宅』。"
  liang_residence_cellar:
    findings:
      - "近期木箱壓痕。"
      - "暗排水／逃生結構。"
      - "狹條紙格式近似暗帳：『丙十一 一百二十 未結』、『癸九 八十 水』、『丙七 轉』。"
      - "紙條真偽與含義正在查。"
      - "現場不是母簿。"
    witness:
      - "附近老婦獨立供述：夜間曾見車與兩人像抬著一個人，其中一人拖腳／跛行。"
  unresolved:
    - "母簿真正位置。"
    - "十一日前取箱者是否真為杜成。"
    - "梁福與拖腳／跛行人物是否同一人。"
```

---

# 11｜馬成祿、丙七血跡、陶萬春

```yaml
MA_CHENGLU:
  status: "DETAINED_AFTER_ATTEMPTED_FLIGHT"
  confirmed:
    - "馬成祿試圖翻牆離開廣源，身上帶銀與兩張半燒紙。"
    - "其中一張可見『丙七，梁宅』。"
    - "馬成祿稱自己沒有殺人，留紙是為『留一條命』。"
    - "其稱丙七正常調度走總簿，帳外調度通常只可能由杜成／梁福下令；西門慶本人未必親自調車。"
    - "其稱柳生失蹤後，丙七車曾回廣源東庫，車底有血；血屬誰未證。"
    - "其稱車後來在灰水院被清洗。"
    - "負責清洗／駕駛線索指向陶萬春；陶萬春約兩年前已離廣源，已發新證人傳喚。"
  evidentiary_boundary:
    - "馬成祿供述需其他證據互證。"
    - "車底有血 ≠ 已證柳生死亡。"
```

---

# 12｜孫二虎與柳生「仍有氣」證詞

```yaml
SUN_ERHU_TESTIMONY:
  status: "WITNESS_TESTIMONY; PARTIALLY_CORROBORATING"
  confirmed_statement:
    - "高衙內命人毆打柳生後，孫二虎曾以為丙七車是來『收屍』。"
    - "一名瘦、跛／拖腳的男人從西門一側介入，說『還有氣，先別扔水。』"
    - "柳生之後被抬上藍篷丙七車。"
  current_effect:
    - "與西門慶此前『柳生被裝上藍篷丙七車、未見直接扔河』之供述形成部分互證。"
  unresolved:
    - "瘦跛男人身分。"
    - "柳生之後去哪裡。"
    - "柳生當時傷勢與最終生死。"
  anti_inference:
    - "不得因跛／拖腳直接認定為梁福。"
```

---

# 13｜陳氏女線：新自願來府女子與舊木箱

```yaml
CHEN_CASE_NEW_WITNESS:
  status: "NEW_VOLUNTARY_WITNESS_PENDING_ISOLATED_EXAMINATION"
  confirmed:
    - "一名女子主動到開封府，自稱陳氏女之嫂／姊嫂類親屬。"
    - "她稱陳氏女仍活著，但害怕親自來府。"
    - "她帶一只舊木箱，稱其中可證『五百兩到底買了什麼』。"
  next_procedure:
    - "應先隔離訊問、驗物、驗來源，再決定公開程度。"
  prohibited:
    - "不得現在就把木箱內容寫成已證明綁架、撤狀銀或高府犯罪。"
```

---

# 14｜西門慶當前合作／自救法位

```yaml
XIMEN_QING_CURRENT:
  status: "SERIOUS_ACCUSED_IN_CUSTODY; COOPERATING_FOR_NARROW_PROTECTION"
  confirmed:
    - "西門慶已開始以拆帳方式區分『自己做的』與『借自己路線發生但未必由自己直接下令的』。"
    - "對蘇清被控制一月等自己已難以翻掉的核心事實，不再採全面否認。"
    - "其以外部證據、暗帳、人名與線索換取自己仍有證據價值。"
  bao_narrow_protections:
    - "若其點名之無辜親屬遭威脅，官府可依法提供必要保護。"
    - "重要證據可做副本／分存。"
    - "即使其死亡，已入卷證據仍保留。"
  not_granted:
    - "免罪"
    - "保證刑度"
    - "保證不充軍／不死"
  player_assessment_only:
    - "白御行曾判斷西門慶至少可能重判至充軍以上；此為玩家判斷，不是官府判決。"
```

---

# 15｜蘇清當前對潘金蓮之目標與自由構想

```yaml
SUQING_CURRENT_GOALS:
  against_pan:
    - "目前不以把潘金蓮送入牢獄／奪掌櫃位作首要目標。"
    - "要查二十八日究竟值多少、為何其一月被用來結西門五千後帳、自己帳上為何沒有對應價值。"
    - "若潘當時根本無權處分她，則要追相應法律／帳務後果。"
    - "即使潘釋放她現有契約，蘇清也只會把這視為『桌錢／一部分結算』，不當成所有歷史帳已清。"

  future_professional_status:
    lifecycle: "PROPOSAL_IN_ROUTE_ONLY"
    concept:
      - "蘇清受貂蟬式自主方向啟發，考慮日後由自己持有／控制自己的契約或執業資格。"
      - "可選擇仍做風月性工作，但以『掛單』方式在不同場所營業。"
      - "觀止取得場地、抽成或管理權，不等於擁有／處分她本人。"
    core_statement:
      - "若原契解除後她仍留在觀止，她希望那代表『我留下，是因為我想留，不是因為一張紙說我走不了。』"
    not_final:
      - "尚未形成觀止正式制度。"
      - "尚未完成新契約。"
```

---

# 16｜蘇清 × 白御行：二十八日私人約仍未自動延長

```yaml
SUQING_BAI_PRIVATE_PACT:
  old_500_three_night_contract: "CLOSED_IN_HOT_V2.3"
  separate_28_day_pact:
    condition: "西門慶真正倒台／持久喪失舊有位置、錢權與路線後才觸發"
    current_trigger_status: "VERY_CLOSE_OR_LIKELY_BUT_NOT_SILENTLY_STARTED_BY_SAVE"
    note:
      - "西門慶已被羈押、法網重壓，但『真正倒台』需由可持續結果確認，不因戲劇氣氛自動起算。"
  day_29:
    status: "POSSIBLE_VOLUNTARY_REWARD_ONLY"
    condition: "若今夜謀局後來確實成為拔除西門慶之關鍵因果線，蘇清可能自願加一天。"
  82_days:
    status: "NOT_ACCEPTED"
    note: "白御行曾玩笑說八十二日；蘇清未同意。"
  future_wager:
    - "蘇清明示：待她先決定自己的法律／職業位置，再談白御行原本想押的關係賭局。"
```

---

# 17｜白御行：本輪有效自我陳述／玩家主權資料

```yaml
PLAYER_SELF_FACTS:
  betrayal_history:
    - "白御行明示自己曾被最愛的女人背叛；此為其個人過往有效玩家事實。"

  trust_philosophy:
    - "白御行認為有能力的屬下可以作為才能使用，但枕邊／親密女人在某些情況下較容易被敏感的人察覺態度變化。"
    - "他不主張親密女人不可能背叛。"

  self_pollution_statement:
    - "白御行表示自己常主動『做死』是因為好玩，不必自動解釋為精密戰略。"
    - "他也曾主張部分負面形象可降低外界對其能力之戒心；此仍是本人主張。"

  chunmei_desire:
    - "白御行明示：自己對龐春梅沒有性慾／追求欲，沒有特別原因。"
    - "不得把此狀態寫成龐春梅受辱、被拒絕後必有情緒，亦不得偷偷補出白御行其實有吸引。"

  shuying_assessment:
    - "白御行主觀認為：若真要排行，疏影可能是他最難追的女人，因為連見面都極難。"
    - "此為玩家評估，不等於疏影客觀最難攻略、也不等於她已對白御行發生感情事件。"
```

---

# 18｜疏影：本輪只成立「話題＋未知弦音」

```yaml
SHUYING_CURRENT:
  appearance: "NOT_CONFIRMED_PRESENT_IN_SCENE"
  confirmed:
    - "眾人討論白御行覺得最難追的女人時，話題轉到疏影。"
    - "紅娘氏、蘇清、李師師、阿麗婭等形成不同解讀：疏影的難不只是讓她動心，而是先取得真正被她允許見面／進場的資格。"
    - "眾人明示錢、身份、俗套風雅未必是有效槓桿。"
    - "李師師提醒：疏影不是等待男人破解規則的獎品；任何例外須由她自己成立。"
    - "討論後，樓上／觀止深處曾傳出一次極輕的弦音『錚』。"
  source_of_string_sound: "UNKNOWN"
  prohibited:
    - "不得自動宣判是疏影彈的。"
    - "不得自動宣判弦音是對白御行的回應、邀請或好感。"
    - "不得因被談論就強迫疏影下樓。"
```

---

# 19｜人物圖畫展示事件

```yaml
IMAGE_PROP_LOG:
  general_rule:
    - "以下均為白御行在內院拿出／展示的圖畫。"
    - "圖畫文案屬道具內容，不自動成為角色真實履歷或觀止官方宣傳。"

  aaliyah:
    file_prop: "阿莉婭.png"
    notable_text: "無垢祭品／她越乾淨，這世道就顯得越髒"
    reaction:
      - "阿麗婭認為畫中自己漂亮、像人在觀止卻尚未真正進來。"
      - "她不喜歡『祭品』定位，明示不想再被拿去換五千、平安、名聲或男人面子。"
      - "她表示若圖是白御行畫給她的，願意收；並說未來即使重新掛牌也不准拿這張招客。"
      - "最後可觀察為阿麗婭抱著畫並說『我的、不賣』；所有權法律轉移未由白御行另行明示。"

  hongniang_xiaocui:
    file_prop: "紅綠雙飛C.png"
    notable_text: "紅綠雙飛組"
    reaction:
      - "紅娘氏與小翠均看見圖畫；紅娘氏大笑調侃，小翠因被寫成『新露春情／會勾心』而害羞反駁。"
      - "圖畫不建立兩人新的成人交易、組合合約或服務義務。"

  zhang_lihua:
    file_prop: "張麗華C.png"
    notable_text: "貴妃醉酒，偷照人心"
    reaction:
      - "張麗華喜歡圖中自己不只剩身體，並說畫中女人不像會給人當妾。"
      - "她口頭表示想收畫、且不希望拿去給其他男人看。"

  shisanniang:
    file_prop: "十三娘.png"
    notable_text: "看透人心，才配談人情"
    reaction:
      - "十三娘認為眼神像自己在等別人犯蠢。"
      - "她表示這張可以掛；若有人因看畫就以為追得到她，正好可以讓對方來下注／花錢。"

  li_shishi:
    file_prop: "李師師.png"
    notable_text: "名動京華，笑眼藏風月"
    reaction:
      - "李師師說圖把她畫得太乖，像還沒遇見『睡完就穿褲子跑』的男人。"
      - "她拿走／持有圖畫，但明示白御行三日不得進她房之私人處罰不因此減免。"

  su_qing:
    file_prop: "蘇清C.png"
    notable_text: "她先選會贏的人，然後再決定自己站在哪裡"
    reaction:
      - "蘇清起初說不要，看到後改口『給我／我現在要了』。"
      - "她特別看畫中伸出的手，認同自己不像等別人來拉。"
      - "她後來評論：白御行畫不同女人時看的不是同一件東西；此為蘇清人物判斷。"

  rokujo:
    file_prop: "六條妃子.png"
    notable_text:
      - "六條御息所"
      - "一代高貴之女，淪為深宮之怨"
      - "我不是害怕失去你，我只是不能接受，你曾經擁有過我，卻忘記了那代表什麼。"
    pre_arrival_effect:
      - "該畫引發眾人對六條御息所、嫉妒、身分、關係與生靈傳說的高密度討論。"
```

---

# 20｜六條御息所：共鳴召喚成功之 ROUTE EVENT

```yaml
ROKUJO_ARRIVAL:
  event_type: "UNKNOWN_VISITOR_RESONANCE_ARRIVAL"
  lifecycle: "ROUTE_EVENT"
  baseline_pool_status: "NOT_ADDED_TO_CHARACTER_POOL"

  precondition:
    - "白御行展示六條御息所圖畫。"
    - "多名在場人物持續高密度談論六條、其源氏關係與危險性。"
    - "白御行明示觀止存在『談論某人密度到一定程度會自己召來』的現象；此與世界 Runtime 的共鳴召喚機制相容。"

  observable_arrival:
    - "觀止內院月門外環境出現不屬於汴梁的濕泥路與紅楓霧景。"
    - "一輛黑漆垂簾牛車／御車式車輛停在異路前。"
    - "車外未見正常車夫／牽引配置；具體機制未知。"
    - "車中女子先問『這是哪裡』，後下車／步入觀止。"
    - "女子身份經本人與後續對話確認為六條御息所。"

  summoning_boundary:
    - "召喚成功只代表到訪，不代表她歸屬白御行、觀止或任何男人。"
    - "不代表她有掛牌、服務、陪宿、性交、定居或常設角色義務。"
```

---

# 21｜六條御息所：原時代時間錨

```yaml
ROKUJO_ORIGIN_TIME:
  source: "六條本人對白御行提問之回答"
  confirmed_from_her_current_memory:
    - "她並非『剛從伊勢神宮回來』。"
    - "她剛經歷賀茂祭／車爭事件。"
    - "她的車隊與源氏正室葵上之車隊／從人發生衝突；其車被逼退、從者受辱。"
    - "她原本只是想遠遠看源氏一眼。"
    - "她提及女兒與伊勢有緣，也曾想離開京城，但其後更遠未來並非她當下記憶。"
  current_knowledge_limit_before_white_disclosure:
    - "她不知道自己完整後世故事。"
    - "她不知道後人怎樣評價自己。"
    - "她沒有一本可翻到結局的故事可用來重做當下選擇。"
  critical_director_rule:
    - "六條現在是『賀茂祭車爭後』的六條，不得偷塞後期自知生靈、女兒婚後、自己晚年等未經告知記憶。"
```

---

# 22｜六條御息所 × 白御行：後世故事與源氏核心情報

```yaml
ROKUJO_WHITE_INFORMATION_EXCHANGE:
  white_refuses:
    - "六條問後世如何記她；白御行明示不回答。"

  white_personal_judgment:
    - "白御行說六條對自己有致命吸引力：危險、高貴、自信但命運不佳。"
    - "白御行稱她是自己眼中的『可憐女人』。"
    - "白御行曾把其處境解讀為寡婦被情慾牽動、無法接受退出舞台、被光源氏式男人欺騙。"
  rokujo_response_to_pity:
    - "六條明示不喜歡被『可憐』把自己的主動錯誤與責任洗掉。"
    - "她承認自己有情慾、有不甘、有對身份／被渴望位置的需要，但拒絕被縮成『所有女人／寡婦都會犯的錯』。"
    - "她要求白御行不要用抽象的『女人』蓋掉她這個人。"

  white_genji_future_story_claims:
    source_status: "PLAYER_PROVIDED_FUTURE_NARRATIVE; HEARD_BY_ROKUJO; NOT_INDEPENDENTLY_VERIFIED_BY_HER"
    content:
      - "光源氏幼年喪母。"
      - "其父皇後來納一名與其母極相似、且與母族有親緣的皇妃。"
      - "白御行描述源氏幼年對該皇妃形成深層依戀，成年後受宮禁分離。"
      - "白御行說源氏曾強迫／侵犯該皇妃，並生下一名名義上被當作先帝皇子、後來即位之男子。"
      - "因此白御行把該帝描述為源氏生物學之子、名義上的弟弟。"
      - "白御行說源氏一生真正追逐的是該皇妃，而該皇妃最後為避其糾纏而出家。"
      - "白御行說紫姬長相也像該皇妃，源氏領養／養成紫姬亦有追逐影子之成分。"
      - "白御行進一步說六條吸引源氏，也可能因其氣質能勾起該原型。"
      - "白御行告知：六條之女秋好日後會嫁給那位被描述為源氏與皇妃所生、後來即位的皇帝。"
      - "白御行最後明示：源氏其實知道自己一直在追逐什麼，只是無法停下來。"

  rokujo_processing:
    - "六條把此資訊理解為：自己、葵上、紫姬等女人可能不是在爭同一個『唯一位置』，而是在面對一個男人永遠無法填滿的原型缺口。"
    - "她承認這使自己重新看待葵上，但不因此立刻不嫉妒、不喜歡葵上或放下源氏。"
    - "她明示即使聽懂，也可能仍想見源氏；知道結構不會立即消除感情。"
    - "她認為『知道後仍選』與『不知道時被牽著走』是不同法位。"

  anti_canonization:
    - "六條沒有在本夜宣告已放下源氏。"
    - "沒有宣告愛上白御行。"
    - "沒有宣告源氏之未來故事已被她驗證為客觀真相。"
```

---

# 23｜白御行對六條「權力／血統」判斷：保持爭議

```yaml
ROKUJO_MOTIVE_DISPUTE:
  white_claim:
    - "白御行判斷六條最深層其實想要權力／權勢。"
    - "白御行進一步判斷她未必真正愛源氏，而是被源氏血統、身分與她重新回舞台的可能性吸引。"

  rokujo_response:
    - "六條未接受為定論。"
    - "她承認身份、名聲、權勢、被人仰望對自己確實不是毫無意義。"
    - "她也承認東宮死後的身分退場與源氏是否來見自己，可能長期被她綁在一起。"
    - "但她明示：究竟是愛血統、愛權力、愛源氏本人，還是愛『重新被渴望／重新回舞台』的感覺，要由她自己分。"

  save_rule:
    - "不得把『六條其實不愛源氏只愛血統』寫進人物內心硬狀態。"
    - "可保存為白御行對她的強判斷，以及六條願意拿回去思考的問題。"
```

---

# 24｜白御行推薦趙受益給六條

```yaml
ROKUJO_ZHAO_INTRODUCTION:
  initiator: "白御行"
  player_statement:
    - "白御行明示自己認為『把人放到正確的位置就能解決問題』。"
    - "他認為自己不適合六條，但趙受益較適合。"
    - "他向六條推介趙受益的大宋皇家血脈、人品與條件，並以『可能很純也可能參了貓科動物』開玩笑。"

  zhao_response:
    - "趙受益沒有承認自己是六條候選、沒有接受白御行替他決定關係。"
    - "他明示：白御行推薦是白御行的事；六條要不要認識是六條的事；他自己是否進一步是自己的事。"
    - "趙不願跟不在場的光源氏比『誰更值得女人愛』。"

  rokujo_response:
    - "六條認為趙至少不像源氏那樣急著把自己的需要塞到剛見面的女人身上。"
    - "她曾直接問趙是否有妻室。"
    - "趙沒有正面回答婚姻狀態，而是先問她為何要知道；因此其妻室狀態在六條知情中仍為 UNKNOWN。"
    - "六條明示：趙『至少第一關比白御行過得好』之類戲謔評語，但不構成選定。"
```

---

# 25｜六條 × 趙受益：只成立一杯茶

```yaml
ROKUJO_ZHAO_RELATION:
  current_state: "FIRST_MEETING; MUTUAL_COURTESY; LOW_LEVEL_INTEREST_OR_CURIOSITY"
  confirmed:
    - "六條主動問趙：若不介意，今晚可以陪她喝一杯茶。"
    - "她立刻加明『只喝茶』，並說自己才剛聽完源氏一生的核心秘密，還沒有蠢到立刻換下一個男人。"
    - "趙受益接受『只喝茶』之條件。"
  not_established:
    - "戀愛"
    - "性同意"
    - "陪宿"
    - "私房進入"
    - "婚約／妾約"
    - "候選註冊"
    - "排他性"
  relation_shape:
    - "兩人都反對白御行替彼此直接宣布適合／成交。"
    - "六條對趙的克制、身分氣質與不急於自我推銷形成正面第一印象。"
    - "趙對六條維持禮貌與邊界，尚無明示愛慕。"
```

---

# 26｜六條入住安排：異時女客，不是姑娘

```yaml
ROKUJO_LODGING:
  manager_on_duty: "春梅／潘金蓮仍在開封府"
  guest_status: "異時女客"
  room: "觀止內院東偏廂乾淨空房"
  room_type:
    - "不是掛牌房"
    - "不臨主要客道"
    - "不是紅倌／清倌服務房"
  room_setup:
    - "重新換被褥。"
    - "撤掉過重的觀止姑娘房脂粉／熏香，先保持乾淨。"
    - "門可由六條自己從內閂上。"
    - "不派男性入房服務。"
    - "可留兩名女使在外間／門外，需要時才應。"
    - "六條明示不需要人在房內守著；保留外燈即可。"
  vehicle:
    - "六條原車／異路先不碰。"
    - "若明早仍存在，再處理；目前不得拆、拖、研究或宣判為永久門。"
  not_yet_confirmed:
    - "六條已正式進房睡下"
    - "六條會住幾夜"
    - "六條是否能／何時回原時代"
```

---

# 27｜六條今晚帳務：趙受益代付，不生人身權

```yaml
ROKUJO_ACCOUNT:
  payer: "趙受益"
  payer_consent: "EXPLICIT_LIMITED_CONSENT"
  covered_items:
    - "客房"
    - "茶食"
    - "必要衣物／日用"
    - "今晚因異時落地所需的一般女客雜用"
  zhao_explicit_boundary:
    - "只算替突然落在異世、沒有本朝錢幣的客人盡地主之誼。"
    - "不是買她。"
    - "不是養她。"
    - "不是白御行一句話便取得一位要負責的女人。"
  rokujo_response:
    - "六條起初表示若日後有自己的錢可以還。"
    - "趙建議不當欠款：今晚他請；若日後仍有機會同桌，可由六條再請一回。"
    - "六條接受此種社交互請法。"
  account_legal_effect:
    human_ownership: false
    prostitution_service_right: false
    sex_right: false
    room_entry_right: false
    companionship_right: false
    romance_right: false
    debt_bondage: false
  current_joke_only:
    - "紅娘氏稱白御行像媒婆／老鴇。"
    - "白御行反駁『人家沒成交，不算賣』。"
    - "眾人遂以『推銷未遂／熱心媒婆』玩笑；不具契約法位。"
```

---

# 28｜李師師：三日房禁仍有效

```yaml
LI_SHISHI_ROOM_BAN:
  status: "ACTIVE_PRIVATE_BOUNDARY"
  origin:
    - "白御行先前在師師私人帳未清時，被禁房兩日。"
    - "白御行隔院喊『那我去瓶兒那邊』後，李師師把兩日加為三日。"
  current_event:
    - "六條到觀止後，白御行當眾直接問李師師：今晚要不要陪我睡。"
    - "李師師直接拒絕『不要』。"
    - "她再次明示三日禁房一天不能少。"
    - "她說禁期過後再看她當日有沒有興致；不是預約性同意。"
  invariant:
    - "三日禁房屬李師師當前有效私人邊界。"
    - "不得因白御行公開邀請、六條來訪、圖畫贈送或玩笑而縮短。"
```

---

# 29｜六條已知與未知資訊邊界

```yaml
ROKUJO_KNOWLEDGE_SCOPE:
  knows_now:
    - "觀止可使不同時代的人相遇；此為白御行告知並由自身穿越經驗部分印證。"
    - "白御行聽過她的未來故事，但拒絕直接告訴她後世如何評價她。"
    - "白御行提供一套關於源氏核心欲望、皇妃、紫姬與秋好未來婚配的敘述。"
    - "白御行自稱不適合她，並推薦趙受益。"
    - "趙受益被白御行描述為大宋皇家血脈；趙本人未完整公開更高身份。"
    - "白御行與李師師至少有足以公開問『今晚要不要陪睡』與三日禁房的私人／性關係史。"
    - "白御行此前也曾推薦趙受益給阿麗婭；六條在眾人笑談中得知這一點。"

  does_not_know_without_new_source:
    - "紅娘氏與趙受益曾完成成人交易之確切歷史。"
    - "趙受益真正更高皇家身份細節。"
    - "白御行與所有其他女人的完整性史／契約史。"
    - "她未來是否化生靈、葵上死亡等全部後世細節；此前眾人談過不等於她已聽見。"
    - "自己最終後世評價。"
    - "自己何時／是否能返回原時代。"
```

---

# 30｜人物主權與關係防收斂警告

```yaml
RELATIONSHIP_INVARIANTS:
  rokujo:
    - "六條不是因被召喚就成白御行獎品。"
    - "六條沒有接受『妳其實只愛權勢／血統』為固定人格答案。"
    - "六條對趙只有初次認識與茶約，不得跳成心動、戀愛、陪宿或婚配。"
    - "六條仍可能對源氏有慾望、依戀、嫉妒與不甘；一晚資訊不能洗掉她的時間成本。"
    - "六條對葵上的妒意沒有因知道源氏原型結構就自動消失。"

  zhao:
    - "趙受益付房帳不等於取得六條任何權利。"
    - "趙沒有答應阿麗婭或六條的候選／競標。"
    - "不得因白御行兩度推薦就把趙寫成觀止公用男伴。"

  aaliyah:
    - "阿麗婭今晚不重新掛牌。"
    - "其一期婚／篩選競標仍為構想。"
    - "不得因五千舊權利弱化就把她自動轉成紅倌或自由妓女。"

  li_shishi:
    - "三日禁房有效。"
    - "性邀請被拒絕後不得改寫成欲拒還迎。"

  su_qing:
    - "其自由／職業制度仍未定。"
    - "二十八日私人約不得因西門慶看似完蛋就偷算第一天。"

  shuying:
    - "只有未知弦音，無進場、無邀請、無好感確認。"

  chunmei:
    - "白御行對她無性慾是玩家硬事實；不得創造反向吸引。"
```

---

# 31｜法律戰防收斂警告

```yaml
LEGAL_INVARIANTS_V2_5:
  - "高衙內承認暴力命令 ≠ 已證殺害柳生。"
  - "柳生被裝上丙七且當時可能仍有氣 ≠ 已證後來存活。"
  - "丙七＝車牌／車號；不得再當個人身份牌。"
  - "同一車、同一帳碼、同一日期仍需因果互證。"
  - "潘金蓮承認蘇清抵五千後帳 ≠ 已證她授權西門暴力抓人。"
  - "西門慶說自己如何理解『西門自取』＝供述，不是自動客觀真相。"
  - "蘇清後來自願入妓籍 ≠ 前二十八日合法。"
  - "前二十八日若違法 ≠ 後來自願申請當然失效。"
  - "阿麗婭舊五千出閣權未完成且被替代結算 ≠ 阿麗婭必須重新掛牌。"
  - "陳氏親屬帶來木箱 ≠ 五百兩用途已證。"
  - "母簿仍未找到，但官府已有足夠基礎繼續拘提、封存與證人程序。"
  - "不得把所有支線重新拖回『先找到母簿才可辦人』。"
```

---

# 32｜當前重要未決事項

```yaml
OPEN_HOOKS:
  legal_high_priority:
    - "陳氏女親屬木箱內實物與『五百兩買了什麼』究竟為何。"
    - "陶萬春是否到案、能否互證丙七血跡／清洗事件。"
    - "瘦跛男人身份與柳生離開丙七後的去向。"
    - "杜成下落。"
    - "梁福下落、身分是涉案者或證人比例。"
    - "廣源母簿位置。"
    - "梁宅狹條紙真偽與碼義。"
    - "高衙內、家僕、西門慶、廣源間對柳生案的責任切割。"
    - "潘金蓮在『蘇清一月抵五千後帳』中的契約／帳務責任。"
    - "蘇清前二十八日的合法性與損害計算。"
    - "蘇清後來自願妓籍文件與其原私人契約如何對接。"
    - "阿麗婭舊五千拍賣在最終判定中如何正式註銷／失效。"

  relationship_and_status:
    - "六條明早或稍後是否仍留觀止、是否要求回原時代。"
    - "紅楓異路與牛車是否仍存在。"
    - "六條與趙受益的茶是否繼續、是否只停於社交。"
    - "六條如何處理白御行告知的未來源氏資訊；不得替她預先選擇回去後行動。"
    - "白御行是否還會接近六條；其已口頭說『自己不適合』，不等於永久放棄或契約禁止。"
    - "阿麗婭何時／是否重新申請首次出閣。"
    - "阿麗婭未來制度構想是否被觀止／官府採納。"
    - "蘇清最終職業身分與白御行二十八日私人約觸發日。"
    - "李師師三日禁房之實際倒數與私人帳修復。"
    - "疏影弦音來源。"
    - "六條圖畫與其他人物圖畫最終由誰保存；不得以本 SAVE 自動完成贈與。"
```

---

# 33｜下一導演接關警告

```yaml
CONTINUATION_GUARD:
  must_preserve:
    - "目前已進 HOT SAVE，停止戲劇性擴寫；下一輪若玩家說繼續，再解除 HOLD。"
    - "白御行台詞、行動、進房、付款、性邀請、關係承諾與內心仍由玩家控制。"
    - "六條今晚只是異時女客；不要把她寫成掛牌姑娘、紅倌、白御行女人或趙受益女人。"
    - "六條房間已安排但未確認她已入睡；下一幕可由世界自然推進，但不能替她或玩家跳過需要作答的重要選擇。"
    - "趙受益與六條只答應喝茶；不要收斂成戀愛線成功。"
    - "六條沒有被白御行『治好』源氏情結；她只是得到新資訊。"
    - "六條對『權力／血統才是核心』保持爭議，不得當成人物卡真相。"
    - "六條原時代時間固定在賀茂祭車爭後；除白御行已告知內容外，不得讓她知道後期事件。"
    - "六條不知道紅娘氏與趙受益的舊成人交易。"
    - "潘金蓮仍在開封府；若要回觀止需有移動事件。"
    - "阿麗婭今晚不掛牌。"
    - "李師師三日房禁仍生效。"
    - "疏影未進場；弦音來源 UNKNOWN。"
    - "龐春梅對白御行無性吸引是玩家自我狀態，不得反向強拉戀愛。"
    - "法律線已進法網擴張階段，下一次切回不得重新鬼打牆只找單一母簿。"
    - "高衙內、潘金蓮、西門慶均未因目前證據被導演直接跳到終局刑判。"
  no_forced_choice_menu: true
```

---

# 34｜本 HOT 的一句接關摘要

> **開封府已從查線索跨進拘提、封存與廣泛證人法網；五千後算進一步坐實「阿麗婭掛名、蘇清一月被西門接受為替代結算」，但潘是否授權暴力、蘇清前二十八日與後來自願入妓籍仍須分軸裁判。阿麗婭回觀止後沒有立刻重新掛牌，而開始構想由自己篩選首次二十八日對象的「一期婚」。同夜內院因高密度談論六條御息所而成功引來未知來客：賀茂祭車爭後的六條本人進入觀止，聽見白御行關於光源氏核心欲望與未來宮闈的敘述，未被「可憐／只愛權勢」的解讀洗成人設；白御行又把趙受益推薦給她。六條與趙目前只同意喝一杯茶，六條以異時女客暫住東偏廂，趙代付今晚客費而不生任何人身、性、陪宿或關係權利。此刻無人成交。**

<!-- SOURCE_HOT_V2_5_END -->
