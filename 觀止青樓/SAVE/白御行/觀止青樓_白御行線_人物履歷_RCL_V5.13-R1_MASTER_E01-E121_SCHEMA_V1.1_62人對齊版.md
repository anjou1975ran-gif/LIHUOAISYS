# 觀止青樓｜白御行線人物履歷 RCL V5.13-R1
## 與 MASTER SAVE V5.13-R1 同代｜編譯基準：MASTER V5.13-R1-HARD｜E01–E121｜LCAPG V3.3.9／62人對齊｜HOT V5.14–V5.16 不吸收
### GUANZHI_RCL_SCHEMA_V1_1｜NEXT-MASTER-PROMOTION MIGRATION COMPLETE

```yaml
DOCUMENT:
  title: "觀止青樓｜白御行線人物履歷"
  short_id: "RCL-BYX"
  version: "V5.13-R1"
  memory_generation: "V5.13-R1"
  schema: "GUANZHI_RCL_SCHEMA_V1_1"
  schema_owner: "GUANZHI MAIN V15.4 / MEMORY-SAVE SPEC"
  date: "2026-09-13"
  document_type: "COMPILED_ROUTE_CHARACTER_LEDGER"
  status: "MASTER_DERIVED / SAME_GENERATION_ATOMIC_PAIR"

ROUTE:
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"

COMPILED_FROM:
  master_file: "觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md"
  master_memory_generation: "V5.13-R1"
  master_record_version: "V5.13-R1-HARD"
  master_sha256: "19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5"
  canonical_event_range: "E01-E121"
  cutoff_event: "E121"
  cutoff_time: "理火三年榴月二十七日晚"
  parent_rcl_file: "觀止青樓_白御行線_人物履歷_RCL_V5.9-R1_MASTER_E01-E117_人物編號對齊_臨時人物版.md"
  parent_rcl_version: "V5.9-R1"
  parent_rcl_schema: "GUANZHI_RCL_SCHEMA_V1_0"
  parent_rcl_sha256: "c7b7e09fc74fd38b542f9fecb181a29766446858d741241d1aae3e8732177382"
  lcapg_file: "觀止人物卡池_LCAPG_V3.3.9_小說第五卷來源履歷回填_辭歲第六卷補全_62人_WorldV1.5.1_CoreV15.4對齊版.md"
  lcapg_version: "V3.3.9"
  lcapg_sha256: "6fcc3a778ef335c2b77c9799e533a12fa64c56b5e12d016c45efa8fcd023aae9"
  lighter_relation_semantics: "LIHUO LIGHTER V3.5.2-EXP / af42d36a3d29f1c40ed687a088a480caa04ef6d4f499b0b2b52c1c4eff764343"

PROMOTED_IN_THIS_GENERATION:
  - "HOT V5.10 -> MASTER E118"
  - "HOT V5.11 -> MASTER E119"
  - "HOT V5.12 -> MASTER E120"
  - "HOT V5.13-R1 -> MASTER E121"

POST_MASTER_OVERLAY_EXCLUDED_FROM_THIS_COMPILE:
  - "HOT V5.14"
  - "HOT V5.15"
  - "HOT V5.16"

MIGRATION:
  from_schema: "GUANZHI_RCL_SCHEMA_V1_0"
  to_schema: "GUANZHI_RCL_SCHEMA_V1_1"
  rule:
    - "舊 RCL V5.9-R1 保留 read-only provenance，不回寫。"
    - "本次 MASTER promotion 由 paired MASTER E01-E121 重新編譯同代 RCL V1.1。"
    - "RCL 只引用 paired MASTER 已存在事件，不取得第二事件法位。"
    - "LCAPG BASE 不被 Route 結果回寫。"

VERSION_ALIGNMENT:
  memory_generation: "V5.13-R1"
  master_record: "V5.13-R1-HARD"
  rcl_record: "V5.13-R1"
  schema: "GUANZHI_RCL_SCHEMA_V1_1"
  atomic_pair_required: true
```

> **LCAPG 是人；MASTER 是事；RCL 是這個人走過這些事後，在白御行線截至 E121 站在哪裡。**
>
> 本檔不吸收 HOT V5.14–V5.16。較新 LIVE 狀態必須在本 RCL 之後依序疊加三個 HOT。

---

# 1｜讀取規則

```text
LCAPG V3.3.9 BASE
↓
RCL-BYX V5.13-R1 @ MASTER V5.13-R1-HARD / E01-E121
↓
MASTER E## detail when needed
↓
HOT V5.14 → V5.15 → V5.16
↓
CURRENT LIVE STATE
```

固定：

```text
RCL SUMMARY != MASTER EVENT BODY
RCL CURRENT STATE != POST-MASTER HOT STATE
LCAPG BASE != PLAYER ROUTE STATE
EVENT PARTICIPATION != FULL KNOWLEDGE
ADULT EVENT != LOVE
PAYMENT != ACCESS != RELATION != CONSENT
REFERENCE != ARRIVAL
UNKNOWN / PENDING / DISPUTED REMAIN LEGAL
HOT V5.14+ != MASTER V5.13-R1 CUTOFF
```

---

# 2｜LCAPG 62 人對齊履歷

## 01｜CHARACTER_SLOT_1｜潘金蓮

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: CHARACTER_SLOT_1
  unified_order: 1
  name: 潘金蓮
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 觀止大掌櫃／長期營運對手兼合作節點；與白御行已有多次私人成人事件，但未建立戀愛、排他、固定情人或未來永久同意。
  relation_lifecycle: ACTIVE_CONSTRAINING
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E117：榴月二十六日上午自願成人事件成立；潘金蓮拒絕內射，白御行遵守；『今日10/10』只限今日。
  - 商業／掌櫃／案件線持續具有因果約束。
  - E118：取得「浮月閣」專名後採被動聽風；接手初一候選／本人最終選人玩法設計，仍要求先問當事人。
  - E119：處理嫪毐挑戰、夏蓮一夜掛牌與初一規則；挑戰費與成人 access 分離。
  - E121：執行槐生一日租地、十一哥「兩處一門」接觸與紅娘即時完全出籠；啟動多條初一邀帖。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries:
  - 浮月閣只到名字與條件式線索；不得把失仙所屬／非人身份升格。
  unresolved:
  - 槐生租期到期結果、十一哥拓撲費、初一各帖回覆與實際到場。
master_event_index:
- event_id: E02
  title: 第二夜：辭歲包廂拒絕與張麗華初登場
- event_id: E04
  title: 一萬兩三日懸賞與「無路，無解」
- event_id: E05
  title: 一萬兩轉為張麗華酒錢
- event_id: E14
  title: 女兒紅來源與最後一罈競局
- event_id: E26
  title: 仁宗朝夜談：天章閣、馬吊與歷史會計帳
- event_id: E28
  title: 傳聞與話本操盤計畫
- event_id: E30
  title: 第五夜善後與人物去留
- event_id: E34
  title: 後堂地道出現與趙受益抵達
- event_id: E35
  title: 紅娘氏第一筆紅倌交易
- event_id: E43
  title: 紅娘氏與小翠紅綠雙飛組提案
- event_id: E60
  title: 白玉池封池、蘇清研究與潘金蓮尚未介入之初始狀態
- event_id: E70
  title: 張麗華酒莊交接與管理入口
- event_id: E82
  title: HOT V2.4：風滿樓、西門暗櫃與五千後算
- event_id: E83
  title: HOT V2.5：開封法網、阿麗婭重定義與六條來訪
- event_id: E84
  title: 京師軍械案鏡頭收網、觀止民事戰重啟、許慎言七十二小時按摩券
- event_id: E85
  title: 潘金蓮返樓、五千原款重分類、五萬索賠、身籍與重新掛牌條件式討論
- event_id: E86
  title: 潘身籍副冊補證、白玉池許願幣／定存框架、師師道歉修復與如夫人再確認
- event_id: E88
  title: 女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限
- event_id: E90
  title: 小翠同床純睡、三月集訓與走秀換約、六百兩候選條款、白宅設計啟動
- event_id: E91
  title: 浮香自願給床與成人夜、紅娘煙幕揭穿、九幽帝皇聯誼會正式訂單
- event_id: E109
  title: HOT V5.1｜榴月十八日晚
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
- event_id: E114
  title: HOT V5.6【REBUILD-R1】｜榴月二十四日白日
- event_id: E115
  title: HOT V5.7｜榴月二十四日夜
- event_id: E116
  title: HOT V5.8｜榴月二十五日夜
- event_id: E117
  title: HOT V5.9｜榴月二十六日上午
- event_id: E118
  title: HOT V5.10｜榴月二十六日下午
- event_id: E119
  title: HOT V5.11｜榴月二十六日晚
- event_id: E121
  title: HOT V5.13-R1｜榴月二十七日晚
locks:
- ADULT_EVENT != LOVE
- TODAY_10_10 != FUTURE_CONSENT
- INVITE != ACCEPTANCE != ARRIVAL
```

---

## 02｜CHARACTER_SLOT_2｜李瓶兒

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: CHARACTER_SLOT_2
  unified_order: 2
  name: 李瓶兒
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 白家如夫人／女主人級位置成立；與白御行有穩定私人成人關係證據，但不等於永久同意。E120 玩家校正再次確認她為白家如夫人／家內女主人級。
  relation_lifecycle: ACTIVE_CONSTRAINING
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E105：白家落地後，李師師／李瓶兒平級如夫人空間法位鎖定。
  - E110–E111：兩人私人成人夜與翌晨成人事件成立；E111 內射成立，受孕／懷孕 UNKNOWN。
  - E120：白家家庭位階校正，李瓶兒＝如夫人／白家女主人級。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index:
- event_id: E58
  title: 李瓶兒入池與追求機會未關閉
- event_id: E60
  title: 白玉池封池、蘇清研究與潘金蓮尚未介入之初始狀態
- event_id: E71
  title: 觀止餐飲改良但不開平價早餐鋪
- event_id: E72
  title: 李瓶兒之秘密關係提案未接受
- event_id: E74
  title: 四人火鍋家宴
- event_id: E75
  title: 房內兩日「家人」框架
- event_id: E76
  title: 李瓶兒接受當晚留宿
- event_id: E77
  title: 寢具用品準備與親密未決
- event_id: E78
  title: HOT V2.0：四人夜結與兩日關係分軸
- event_id: E80
  title: HOT V2.2：師師如夫人前置、七色肚兜與張麗華獨宿夜
- event_id: E86
  title: 潘身籍副冊補證、白玉池許願幣／定存框架、師師道歉修復與如夫人再確認
- event_id: E87
  title: 曹州假印立案、定陶總會架構、京師女性時尚企畫、師師抱睡
- event_id: E95
  title: 辭歲／錦棠／李瓶兒私人開戶、紅袖五十萬反向價格尺與召喚權、紅娘門窗屏風換債、趙受益六條夜集外出
- event_id: E105
  title: HOT V4.7｜榴月十四日晚
- event_id: E110
  title: HOT V5.2｜榴月十九日晚
- event_id: E111
  title: HOT V5.3｜榴月二十日白日
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
- event_id: E115
  title: HOT V5.7｜榴月二十四日夜
- event_id: E120
  title: HOT V5.12｜榴月二十六日晚後續～榴月二十七日晚
locks:
- MASTER_V5_9_CUTOFF_STATE_ONLY
- PREGNANCY_UNKNOWN_AT_CUTOFF
- RU_FUREN != LEGAL_OFFICIAL_WIFE_WITHOUT_EVIDENCE
```

---

## 03｜CHARACTER_SLOT_3｜龐春梅

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: CHARACTER_SLOT_3
  unified_order: 3
  name: 龐春梅
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 觀止二掌櫃；與白御行主要是營運／管理／事件協作關係，MASTER 未建立私人戀愛或固定成人關係。
  relation_lifecycle: ACTIVE_CONSTRAINING
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - 掌櫃權限與後台／現場管理持續有效。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index:
- event_id: E62
  title: 張麗華花燭當日確認與時辰
- event_id: E64
  title: 時空道人承認漏籤
- event_id: E111
  title: HOT V5.3｜榴月二十日白日
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
locks:
- SHOPKEEPER_ROLE != PRIVATE_RELATION
```

---

## 04｜FLOWER_QUEEN_CORE_1｜蘇清

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: FLOWER_QUEEN_CORE_1
  unified_order: 4
  name: 蘇清
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 長期複合關係：曾有付費契約與成人事件，後有二十八日私人盟約、商會工作與牛郎店合作方向；未固化為固定情人／婚姻。
  relation_lifecycle: ACTIVE_CONSTRAINING
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E115：與白御行、醉花完成自願三人成人事件；蘇清當次明示接受內射，懷孕 UNKNOWN。
  - E116：牛郎店／男性陪侍投資合作方向成立，店址、資本、股權、契約未落地。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index:
- event_id: E04
  title: 一萬兩三日懸賞與「無路，無解」
- event_id: E06
  title: 蘇清五百兩三晚交易：事實修正版
- event_id: E21
  title: 顧北辰霸總劇：巴掌、白月光與豬隊友
- event_id: E23
  title: 無名信與白玉池美女事件
- event_id: E28
  title: 傳聞與話本操盤計畫
- event_id: E59
  title: 白玉池「歸零」、算式與續字回顯
- event_id: E60
  title: 白玉池封池、蘇清研究與潘金蓮尚未介入之初始狀態
- event_id: E65
  title: 活物與事件傳遞測試
- event_id: E68
  title: 商會授權與蘇清、小翠浴房邊界
- event_id: E74
  title: 四人火鍋家宴
- event_id: E75
  title: 房內兩日「家人」框架
- event_id: E76
  title: 李瓶兒接受當晚留宿
- event_id: E77
  title: 寢具用品準備與親密未決
- event_id: E78
  title: HOT V2.0：四人夜結與兩日關係分軸
- event_id: E79
  title: HOT V2.1：定陶商戰、蘇清私約與白玉池補固
- event_id: E80
  title: HOT V2.2：師師如夫人前置、七色肚兜與張麗華獨宿夜
- event_id: E81
  title: HOT V2.3：定陶—沈萬三合作與多線案件升級
- event_id: E82
  title: HOT V2.4：風滿樓、西門暗櫃與五千後算
- event_id: E83
  title: HOT V2.5：開封法網、阿麗婭重定義與六條來訪
- event_id: E84
  title: 京師軍械案鏡頭收網、觀止民事戰重啟、許慎言七十二小時按摩券
- event_id: E85
  title: 潘金蓮返樓、五千原款重分類、五萬索賠、身籍與重新掛牌條件式討論
- event_id: E88
  title: 女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限
- event_id: E103
  title: 榴月十二日晚白家採購規劃、蘇清十八日商會工拆帳、妓籍終身法位鎖、阿莉婭處女拍賣標的與紅娘雙人場、三十二娘妓籍申請、楊玉環白玉池代言首夜、黑公子×小桃百兩交易與同宿意向
- event_id: E104
  title: HOT V4.6｜榴月十三日晚
- event_id: E110
  title: HOT V5.2｜榴月十九日晚
- event_id: E114
  title: HOT V5.6【REBUILD-R1】｜榴月二十四日白日
- event_id: E115
  title: HOT V5.7｜榴月二十四日夜
- event_id: E116
  title: HOT V5.8｜榴月二十五日夜
- event_id: E117
  title: HOT V5.9｜榴月二十六日上午
locks:
- CONTRACT != LOVE
- PARTNERSHIP_DIRECTION != FINAL_CONTRACT
```

---

## 05｜FLOWER_QUEEN_CORE_2｜阿麗婭

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: FLOWER_QUEEN_CORE_2
  unified_order: 5
  name: 阿麗婭
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 觀止人物／舊案與掛牌權利相關節點；E121 已本人明示初一掛牌，但金錢／作品只取得被考慮資格，第一個男人仍由她自己選。未建立白御行私人戀愛或成人關係。
  relation_lifecycle: ACTIVE_DORMANT
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions:
    - 初一掛牌，但保留最終選人權；金錢／作品只形成候選資格。
    status: ACTIVE
    evidence_event_ids:
    - E121
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E83：保留自己決定第一次實際出閣／第一個男人的權利。
  - E118：初一競價候選／本人最終選人玩法仍待本人同意。
  - E121：本人明示「初一，我掛」；接受五千兩作起始標尺，不等於白御行已買到；最後第一個男人由她本人選。
  current_constraints:
  - 最高價者不自動取得第一次／成人 access。
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved:
  - 初一實際競價、候選、本人最終選擇與成人事件均未發生。
master_event_index:
- event_id: E82
  title: HOT V2.4：風滿樓、西門暗櫃與五千後算
- event_id: E83
  title: HOT V2.5：開封法網、阿麗婭重定義與六條來訪
- event_id: E103
  title: 榴月十二日晚白家採購規劃、蘇清十八日商會工拆帳、妓籍終身法位鎖、阿莉婭處女拍賣標的與紅娘雙人場、三十二娘妓籍申請、楊玉環白玉池代言首夜、黑公子×小桃百兩交易與同宿意向
- event_id: E118
  title: HOT V5.10｜榴月二十六日下午
- event_id: E121
  title: HOT V5.13-R1｜榴月二十七日晚
locks:
- MARKET_RIGHT != PLAYER_ACCESS
- BID != FINAL_CHOICE
- LISTING != FORCED_COMPLETION
```

---

## 06｜CHARACTER_SLOT_4｜張麗華

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: CHARACTER_SLOT_4
  unified_order: 6
  name: 張麗華
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 白御行情人＋白家家內成員；在白家有獨立小屋／房，也在觀止有自己的房與酒莊商業線，不是臨時客人。
  relation_lifecycle: ACTIVE_CONSTRAINING
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E55：情人關係成立。
  - E80：互相明示喜歡並有私人成人夜。
  - E105：白家落地，麗華外院空間法位鎖定。
  - E117：酒莊列為初一全日優先供酒採購方向。
  - E120：玩家明示校正為情人＋白家家內成員；初一供酒依大客戶方式加大備援，精確採購量／單價／折扣／付款仍待核帳。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved:
  - 初一酒水精確採購量、單價、折扣與付款。
master_event_index:
- event_id: E02
  title: 第二夜：辭歲包廂拒絕與張麗華初登場
- event_id: E03
  title: 張麗華第一次婚約：五千、一萬五千與一萬訂金
- event_id: E04
  title: 一萬兩三日懸賞與「無路，無解」
- event_id: E05
  title: 一萬兩轉為張麗華酒錢
- event_id: E07
  title: 第五夜開場：張麗華、酒與子時條件
- event_id: E13
  title: 三十年女兒紅、《不得飲》與公開官人稱呼
- event_id: E14
  title: 女兒紅來源與最後一罈競局
- event_id: E16
  title: 歪詩局與《玉樹後庭花》補句
- event_id: E17
  title: 酒莊、薔薇、三烤鹽與定陶商會婚議升級
- event_id: E18
  title: 陳叔寶、地府與張麗華去留爭論
- event_id: E21
  title: 顧北辰霸總劇：巴掌、白月光與豬隊友
- event_id: E26
  title: 仁宗朝夜談：天章閣、馬吊與歷史會計帳
- event_id: E27
  title: 假醉進張麗華房間與私人關係提案
- event_id: E28
  title: 傳聞與話本操盤計畫
- event_id: E29
  title: 自由意志、選擇環境與時間窗口爭論
- event_id: E31
  title: 張麗華穿衣陪睡完成
- event_id: E55
  title: 張麗華明示接受情人關係
- event_id: E56
  title: 李師師嫉妒、私人稱呼與槐月十五日晚共處
- event_id: E62
  title: 張麗華花燭當日確認與時辰
- event_id: E70
  title: 張麗華酒莊交接與管理入口
- event_id: E71
  title: 觀止餐飲改良但不開平價早餐鋪
- event_id: E73
  title: 張麗華三日陪伴線
- event_id: E74
  title: 四人火鍋家宴
- event_id: E75
  title: 房內兩日「家人」框架
- event_id: E76
  title: 李瓶兒接受當晚留宿
- event_id: E77
  title: 寢具用品準備與親密未決
- event_id: E78
  title: HOT V2.0：四人夜結與兩日關係分軸
- event_id: E79
  title: HOT V2.1：定陶商戰、蘇清私約與白玉池補固
- event_id: E80
  title: HOT V2.2：師師如夫人前置、七色肚兜與張麗華獨宿夜
- event_id: E88
  title: 女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限
- event_id: E90
  title: 小翠同床純睡、三月集訓與走秀換約、六百兩候選條款、白宅設計啟動
- event_id: E105
  title: HOT V4.7｜榴月十四日晚
- event_id: E108
  title: HOT V5.0｜榴月十六日下午
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
- event_id: E117
  title: HOT V5.9｜榴月二十六日上午
- event_id: E120
  title: HOT V5.12｜榴月二十六日晚後續～榴月二十七日晚
locks:
- NO_MARRIAGE_DEED_AT_E55
- HOT_V5_12_LATER_CORRECTIONS_NOT_BACKFILLED
- HOUSEHOLD_MEMBER != WIFE
```

---

## 07｜CHARACTER_SLOT_5｜宋蕙蓮

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: CHARACTER_SLOT_5
  unified_order: 7
  name: 宋蕙蓮
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 08｜CHARACTER_SLOT_6｜李桂姐

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: CHARACTER_SLOT_6
  unified_order: 8
  name: 李桂姐
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 09｜CHARACTER_SLOT_7｜紅袖

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: CHARACTER_SLOT_7
  unified_order: 9
  name: 紅袖
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 觀止人物；與白御行有多次互動、曾有成人適應／三日賭約線，但至 E109 已收束；MASTER 未建立固定私人關係。
  relation_lifecycle: ACTIVE_DORMANT
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E109：紅袖／浮香三日賭約在期限前收束。
  - E114：對失仙的觀察只屬紅袖自己的私下分析。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index:
- event_id: E12
  title: 似伊影像與紅袖可能未來
- event_id: E24
  title: 似伊實體入場與退場
- event_id: E25
  title: 白御行給紅袖的建議與如夫人邀請
- event_id: E95
  title: 辭歲／錦棠／李瓶兒私人開戶、紅袖五十萬反向價格尺與召喚權、紅娘門窗屏風換債、趙受益六條夜集外出
- event_id: E104
  title: HOT V4.6｜榴月十三日晚
- event_id: E109
  title: HOT V5.1｜榴月十八日晚
- event_id: E114
  title: HOT V5.6【REBUILD-R1】｜榴月二十四日白日
locks:
- RESOLVED_WAGER != RELATIONSHIP
```

---

## 10｜CHARACTER_SLOT_8｜疏影

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: CHARACTER_SLOT_8
  unified_order: 10
  name: 疏影
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 觀止人物／觀察與評估節點；MASTER 未建立白御行私人關係。
  relation_lifecycle: ACTIVE_DORMANT
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E114：是否正在觀察失仙、看見什麼保持 UNKNOWN。
  - E121：被提出作觀止正門美人牆畫師候選；本人尚未接受，commission 未成立。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved:
  - 是否接受美人牆作畫委託。
master_event_index:
- event_id: E88
  title: 女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限
- event_id: E114
  title: HOT V5.6【REBUILD-R1】｜榴月二十四日白日
- event_id: E121
  title: HOT V5.13-R1｜榴月二十七日晚
locks:
- OBSERVATION_POSSIBILITY != KNOWLEDGE
- PROPOSED_ARTIST != ACCEPTED_COMMISSION
```

---

## 11｜CHARACTER_SLOT_9｜醉花

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: CHARACTER_SLOT_9
  unified_order: 11
  name: 醉花
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 與白御行有既往親近與成人事件；E113 明示未來兩人單獨仍『有』可能，但沒有日期、承諾或固定情人名位。
  relation_lifecycle: ACTIVE_DORMANT
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E113：未來單獨成人關係仍有可能。
  - E115：與白御行、蘇清完成自願三人成人事件；不建立戀愛／永久同意。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index:
- event_id: E13
  title: 三十年女兒紅、《不得飲》與公開官人稱呼
- event_id: E16
  title: 歪詩局與《玉樹後庭花》補句
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
- event_id: E115
  title: HOT V5.7｜榴月二十四日夜
- event_id: E116
  title: HOT V5.8｜榴月二十五日夜
- event_id: E117
  title: HOT V5.9｜榴月二十六日上午
locks:
- INTEREST != COMMITMENT
- ADULT_EVENT != FIXED_LOVER
```

---

## 12｜CHARACTER_SLOT_10｜十三娘

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: CHARACTER_SLOT_10
  unified_order: 12
  name: 十三娘
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 賭局／社交節點；白御行曾交付國運／幸運路徑情報，未建立私人戀愛關係。
  relation_lifecycle: ACTIVE_DORMANT
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E92：豹子賭局白御行敗，依約交付國運／估價／首飾儲存等情報。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index:
- event_id: E07
  title: 第五夜開場：張麗華、酒與子時條件
- event_id: E10
  title: 十三娘問心賭局
- event_id: E92
  title: 帝皇宴前置、十三娘國運賭桌線、兩局免費床結算、紅娘側賭敗、小翠三娘實習與三人抱睡
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
locks:
- GAMBLING_RELATION != PRIVATE_RELATION
```

---

## 13｜CHARACTER_SLOT_11｜白三娘

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: CHARACTER_SLOT_11
  unified_order: 13
  name: 白三娘
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 觀止資深人物；與白御行有成年人親密歷史，但 MASTER 未建立固定情人／婚姻。
  relation_lifecycle: ACTIVE_DORMANT
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E92：白三娘與白御行成人事件成立；其後三人抱睡收束。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index:
- event_id: E07
  title: 第五夜開場：張麗華、酒與子時條件
- event_id: E10
  title: 十三娘問心賭局
- event_id: E42
  title: 白三娘老帶新方案接受
- event_id: E88
  title: 女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限
- event_id: E92
  title: 帝皇宴前置、十三娘國運賭桌線、兩局免費床結算、紅娘側賭敗、小翠三娘實習與三人抱睡
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
locks:
- PAST_ADULT_EVENT != CURRENT_CONSENT
```

---

## 14｜CHARACTER_SLOT_12｜浮香

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: CHARACTER_SLOT_12
  unified_order: 14
  name: 浮香
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 白御行情人＋白家家內成員；與白御行有自願成人夜與持續親近證據，在白家有獨立小屋／房、在觀止亦有房，不是臨時客人。
  relation_lifecycle: ACTIVE_DORMANT
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E91：浮香自主讓白御行留床，其後另有雙方成人事件。
  - E105：白家外院空間法位鎖定。
  - E109：三日賭約收束。
  - E120：玩家明示校正為情人＋白家家內成員。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index:
- event_id: E01
  title: 第一夜：無名客入觀止、辭歲與浮香
- event_id: E09
  title: 浮香第五夜：琴、琴坊與雙向排他
- event_id: E11
  title: 白御行家眷與三名正式妻子公開
- event_id: E91
  title: 浮香自願給床與成人夜、紅娘煙幕揭穿、九幽帝皇聯誼會正式訂單
- event_id: E92
  title: 帝皇宴前置、十三娘國運賭桌線、兩局免費床結算、紅娘側賭敗、小翠三娘實習與三人抱睡
- event_id: E104
  title: HOT V4.6｜榴月十三日晚
- event_id: E105
  title: HOT V4.7｜榴月十四日晚
- event_id: E109
  title: HOT V5.1｜榴月十八日晚
- event_id: E110
  title: HOT V5.2｜榴月十九日晚
- event_id: E111
  title: HOT V5.3｜榴月二十日白日
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
- event_id: E115
  title: HOT V5.7｜榴月二十四日夜
- event_id: E120
  title: HOT V5.12｜榴月二十六日晚後續～榴月二十七日晚
locks:
- MASTER_CUTOFF_ONLY
- HOT_V5_12_LOVER_LABEL_EXCLUDED
- HOUSEHOLD_MEMBER != WIFE
```

---

## 15｜CHARACTER_SLOT_13｜小翠

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: CHARACTER_SLOT_13
  unified_order: 15
  name: 小翠
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 白御行與小翠有多次床位／訓練／有限成人互動歷史；無固定戀愛、所有權或未來 blanket consent。
  relation_lifecycle: ACTIVE_DORMANT
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E90：同床純睡，邊界明確。
  - E92：小翠自願進入有限實習／觀察並自行停止。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index:
- event_id: E37
  title: 小翠拒絕八百兩安排
- event_id: E41
  title: 小翠熟客安全計畫提出
- event_id: E42
  title: 白三娘老帶新方案接受
- event_id: E43
  title: 紅娘氏與小翠紅綠雙飛組提案
- event_id: E45
  title: 深夜休息節點
- event_id: E68
  title: 商會授權與蘇清、小翠浴房邊界
- event_id: E90
  title: 小翠同床純睡、三月集訓與走秀換約、六百兩候選條款、白宅設計啟動
- event_id: E92
  title: 帝皇宴前置、十三娘國運賭桌線、兩局免費床結算、紅娘側賭敗、小翠三娘實習與三人抱睡
- event_id: E101
  title: 榴月十日開幕前夕、辭歲五百萬五年五分定存、師師月事未至孕否未知、商會女人培訓目的鎖、小翠首次完整成人事件、三人同睡收尾
locks:
- TRAINING != AVAILABILITY
- PAST_LIMITED_INTIMACY != FUTURE_CONSENT
```

---

## 16｜NATIVE_08｜李媽媽

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: NATIVE_08
  unified_order: 16
  name: 李媽媽
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 17｜NATIVE_09｜安舟

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: NATIVE_09
  unified_order: 17
  name: 安舟
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 18｜NATIVE_10｜汪鹽商

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: NATIVE_10
  unified_order: 18
  name: 汪鹽商
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 19｜CHARACTER_SLOT_14｜辭歲

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: CHARACTER_SLOT_14
  unified_order: 19
  name: 辭歲
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 高價／資產／觀止經營相關重要人物；與白御行有長期注意與交易歷史，但 MASTER 未建立固定私人戀愛。
  relation_lifecycle: ACTIVE_DORMANT
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E93/E95/E101/E102 等形成資產、帳戶、活動與觀止路線。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index:
- event_id: E01
  title: 第一夜：無名客入觀止、辭歲與浮香
- event_id: E02
  title: 第二夜：辭歲包廂拒絕與張麗華初登場
- event_id: E08
  title: 辭歲二十八日心理奴化提案被拒
- event_id: E89
  title: 風滿樓第二日遴選、十一名候選分流、牙行責任、白宅十年條件式協議
- event_id: E93
  title: 九幽帝皇聯誼會散場、辭歲／錦棠雙姝天價競拍、白玉池帝皇團特殊試營運、帝皇多線自然分流
- event_id: E95
  title: 辭歲／錦棠／李瓶兒私人開戶、紅袖五十萬反向價格尺與召喚權、紅娘門窗屏風換債、趙受益六條夜集外出
- event_id: E101
  title: 榴月十日開幕前夕、辭歲五百萬五年五分定存、師師月事未至孕否未知、商會女人培訓目的鎖、小翠首次完整成人事件、三人同睡收尾
- event_id: E102
  title: 榴月十一日晚重新開幕完成、女子競技與紅娘壓軸、顧三辭歲再會、趙受益二百兩購四契再贈六條／楊玉環、四大金剛＋李清照女客試場、白玉池會員制接受、錦棠同宿
locks:
- MONEY != RELATION
```

---

## 20｜CHARACTER_SLOT_15｜貂蟬

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: CHARACTER_SLOT_15
  unified_order: 20
  name: 貂蟬
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 21｜POOL_CHARACTER_001｜紅娘氏

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: POOL_CHARACTER_001
  unified_order: 21
  name: 紅娘氏
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 長期營業、情報、成人事件與互坑賭約交疊的複合關係；E121 鐵籠生活已即時完全解除，但床拆／砍／燒處分與其他獨立營業／洗浴義務未自動取消。
  relation_lifecycle: ACTIVE_CONSTRAINING
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions:
    - 出籠後把公開鬥嘴／名聲玩法轉成可計營收的生意。
    status: ACTIVE
    evidence_event_ids:
    - E121
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E108：白御行×紅娘成人場成立，並成立六條十日賭約。
  - E112：新加碼賭成立，真條件保密。
  - E113：紅娘已在大堂鐵籠公開生活／營業；九日營收競賽與不水浴募款持續。
  - E116：52兩單句表演與500兩終身固定答詞背書成立。
  - E118：注意到問失仙的陌生男子；沒有因此取得其身份。
  - E119：嫪毐挑戰費與成人 access 分開；當晚沒有同意成人比較。
  - E121：潘金蓮開鎖後，白御行明示不必回籠；剩餘籠居即時完全解除，原初一日出出籠安排被 supersede。
  - E121：與十一哥建立五兩官方蛋鬥嘴生意，第一個可觀察回合已成交／投蛋；十一哥可歸屬部分是紅娘代收負債。
  current_constraints:
  - 床拆／砍／燒處分與其他獨立營業／洗浴義務仍在。
  - 十一哥本金＋3%代理補償帳戶仍未簽、未開戶、未轉本金。
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved:
  - 十一哥信託／帳戶本人接受、顧青簡草約、正式開戶與本金入帳。
master_event_index:
- event_id: E34
  title: 後堂地道出現與趙受益抵達
- event_id: E35
  title: 紅娘氏第一筆紅倌交易
- event_id: E40
  title: 白御行向紅娘氏購買情報
- event_id: E43
  title: 紅娘氏與小翠紅綠雙飛組提案
- event_id: E48
  title: 錯過再會、十二香皂與新招數欠帳
- event_id: E91
  title: 浮香自願給床與成人夜、紅娘煙幕揭穿、九幽帝皇聯誼會正式訂單
- event_id: E92
  title: 帝皇宴前置、十三娘國運賭桌線、兩局免費床結算、紅娘側賭敗、小翠三娘實習與三人抱睡
- event_id: E95
  title: 辭歲／錦棠／李瓶兒私人開戶、紅袖五十萬反向價格尺與召喚權、紅娘門窗屏風換債、趙受益六條夜集外出
- event_id: E98
  title: 三十二娘街行與帳戶指令、紅娘中央籠台演出方案、錦棠首次正式約會、私人成人事件、白御行喜歡明示與相擁收幕
- event_id: E102
  title: 榴月十一日晚重新開幕完成、女子競技與紅娘壓軸、顧三辭歲再會、趙受益二百兩購四契再贈六條／楊玉環、四大金剛＋李清照女客試場、白玉池會員制接受、錦棠同宿
- event_id: E103
  title: 榴月十二日晚白家採購規劃、蘇清十八日商會工拆帳、妓籍終身法位鎖、阿莉婭處女拍賣標的與紅娘雙人場、三十二娘妓籍申請、楊玉環白玉池代言首夜、黑公子×小桃百兩交易與同宿意向
- event_id: E108
  title: HOT V5.0｜榴月十六日下午
- event_id: E111
  title: HOT V5.3｜榴月二十日白日
- event_id: E112
  title: HOT V5.4｜榴月二十日白日
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
- event_id: E114
  title: HOT V5.6【REBUILD-R1】｜榴月二十四日白日
- event_id: E116
  title: HOT V5.8｜榴月二十五日夜
- event_id: E117
  title: HOT V5.9｜榴月二十六日上午
- event_id: E118
  title: HOT V5.10｜榴月二十六日下午
- event_id: E119
  title: HOT V5.11｜榴月二十六日晚
- event_id: E121
  title: HOT V5.13-R1｜榴月二十七日晚
locks:
- WAGER != THIRD_PARTY_CONSENT
- PUBLIC_CAGE != TOUCH_ACCESS
- NO_ROMANCE_INFERRED
- CHALLENGE_FEE != ADULT_ACCESS
- CAGE_RELEASE != OTHER_OBLIGATIONS_CANCELLED
```

---

## 22｜POOL_CHARACTER_002｜李師師

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: POOL_CHARACTER_002
  unified_order: 22
  name: 李師師
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 白家首席如夫人／白家女主人級位置與長期私人親密關係成立；仍保留觀止花魁職業、設席、房門、名聲與收入自主。E120 孕況為高度疑似但未確診。
  relation_lifecycle: ACTIVE_CONSTRAINING
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions:
    - 若未來自己選擇成為母親，仍保有花魁名聲、邀請、金銀與自己的場子。
    status: ACTIVE
    evidence_event_ids:
    - E120
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E80/E86：如夫人位置意向與再確認逐步形成。
  - E105：白家落地後與李瓶兒平級如夫人空間法位鎖定。
  - E109：疑似有喜再升高，仍未確診。
  - E120：孕況升為 SUSPECTED / HIGH SUSPICION；醫者判斷高度可疑／很可能但未確診，味覺／食慾變化不等於確診。
  - E120：玩家校正為首席如夫人／白家女主人級；即使未來有孩子也要保有花魁名聲、邀請、金銀與場子。
  - E120：初一下午條件式接受出席，可彈一兩曲，但身體累可自行提前離開。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries:
  - 確診前要求不要對外宣稱她懷孕。
  unresolved:
  - 是否懷孕仍未確診；若確診是否留下由她本人決定。
master_event_index:
- event_id: E20
  title: 柳如煙概念體、李師師與趙受益花魁局
- event_id: E22
  title: 顧家豪門宴戲
- event_id: E26
  title: 仁宗朝夜談：天章閣、馬吊與歷史會計帳
- event_id: E30
  title: 第五夜善後與人物去留
- event_id: E33
  title: 李師師選擇留在觀止並採設席牌
- event_id: E34
  title: 後堂地道出現與趙受益抵達
- event_id: E35
  title: 紅娘氏第一筆紅倌交易
- event_id: E38
  title: 李師師與師理理身份規則確認
- event_id: E39
  title: 師理理開放白御行追求可能
- event_id: E40
  title: 白御行向紅娘氏購買情報
- event_id: E45
  title: 深夜休息節點
- event_id: E46
  title: 李師師／師理理第一次完整性交
- event_id: E47
  title: 疼痛界線、事後停留與私人記憶
- event_id: E48
  title: 錯過再會、十二香皂與新招數欠帳
- event_id: E56
  title: 李師師嫉妒、私人稱呼與槐月十五日晚共處
- event_id: E58
  title: 李瓶兒入池與追求機會未關閉
- event_id: E61
  title: 李師師共宿、停止權校正與清晨射精
- event_id: E62
  title: 張麗華花燭當日確認與時辰
- event_id: E69
  title: 花燭前休息
- event_id: E73
  title: 張麗華三日陪伴線
- event_id: E80
  title: HOT V2.2：師師如夫人前置、七色肚兜與張麗華獨宿夜
- event_id: E81
  title: HOT V2.3：定陶—沈萬三合作與多線案件升級
- event_id: E83
  title: HOT V2.5：開封法網、阿麗婭重定義與六條來訪
- event_id: E86
  title: 潘身籍副冊補證、白玉池許願幣／定存框架、師師道歉修復與如夫人再確認
- event_id: E87
  title: 曹州假印立案、定陶總會架構、京師女性時尚企畫、師師抱睡
- event_id: E88
  title: 女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限
- event_id: E90
  title: 小翠同床純睡、三月集訓與走秀換約、六百兩候選條款、白宅設計啟動
- event_id: E92
  title: 帝皇宴前置、十三娘國運賭桌線、兩局免費床結算、紅娘側賭敗、小翠三娘實習與三人抱睡
- event_id: E96
  title: 趙受益六條夜集返樓、楊玉環白玉池與荔枝、李師師晨間補考、定陶票據信用／朱明長債方向／曹州案盤點
- event_id: E101
  title: 榴月十日開幕前夕、辭歲五百萬五年五分定存、師師月事未至孕否未知、商會女人培訓目的鎖、小翠首次完整成人事件、三人同睡收尾
- event_id: E105
  title: HOT V4.7｜榴月十四日晚
- event_id: E109
  title: HOT V5.1｜榴月十八日晚
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
- event_id: E115
  title: HOT V5.7｜榴月二十四日夜
- event_id: E117
  title: HOT V5.9｜榴月二十六日上午
- event_id: E120
  title: HOT V5.12｜榴月二十六日晚後續～榴月二十七日晚
locks:
- SUSPECTED != CONFIRMED
- MASTER_V5_9_DOES_NOT_BACKFILL_HOT_V5_12_FIRST_RU_FUREN_CORRECTION
- HIGH_SUSPICION != CONFIRMED_PREGNANCY
- PREGNANCY_IF_CONFIRMED != CAREER_EXIT
```

---

## 23｜SUPPLEMENTAL_CHARACTER_003｜青禾

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_003
  unified_order: 23
  name: 青禾
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 按摩／恢復服務節點；MASTER 未建立白御行私人關係。
  relation_lifecycle: ACTIVE_DORMANT
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E84：青禾開始向許慎言提供分次扣時按摩／恢復服務。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index:
- event_id: E84
  title: 京師軍械案鏡頭收網、觀止民事戰重啟、許慎言七十二小時按摩券
locks:
- SERVICE != PRIVATE_RELATION
```

---

## 24｜SUPPLEMENTAL_CHARACTER_004｜六條御息所

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_004
  unified_order: 24
  name: 六條御息所
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 異時女客與白御行已有自願成人事件；未建立愛、婚姻、所有權、排他或固定情人契約。
  relation_lifecycle: ACTIVE_DORMANT
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E111：首次雙方自願成人性交事件，兩次內射；受孕／懷孕 UNKNOWN。
  - E112：未對未來三人成人事件給出可鎖定明確同意。
  - E121：玩家校正其在觀止相關帳由趙受益支付／供養；此帳務不賦予趙受益她的行動或同意權。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index:
- event_id: E83
  title: HOT V2.5：開封法網、阿麗婭重定義與六條來訪
- event_id: E94
  title: 榴月一日十日整修起點、雙姝款項／身份翻轉、朱明欠單與鄭成功週轉僅預案、六條／趙受益成人結果與污染校正
- event_id: E95
  title: 辭歲／錦棠／李瓶兒私人開戶、紅袖五十萬反向價格尺與召喚權、紅娘門窗屏風換債、趙受益六條夜集外出
- event_id: E96
  title: 趙受益六條夜集返樓、楊玉環白玉池與荔枝、李師師晨間補考、定陶票據信用／朱明長債方向／曹州案盤點
- event_id: E97
  title: 長恨歌文會、柳如是東林夜談、趙受益宣和地道入席、六條／楊玉環雙線追求與三人約會可能性
- event_id: E102
  title: 榴月十一日晚重新開幕完成、女子競技與紅娘壓軸、顧三辭歲再會、趙受益二百兩購四契再贈六條／楊玉環、四大金剛＋李清照女客試場、白玉池會員制接受、錦棠同宿
- event_id: E108
  title: HOT V5.0｜榴月十六日下午
- event_id: E109
  title: HOT V5.1｜榴月十八日晚
- event_id: E111
  title: HOT V5.3｜榴月二十日白日
- event_id: E112
  title: HOT V5.4｜榴月二十日白日
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
- event_id: E114
  title: HOT V5.6【REBUILD-R1】｜榴月二十四日白日
- event_id: E121
  title: HOT V5.13-R1｜榴月二十七日晚
locks:
- PAST_ADULT_EVENT != FUTURE_CONSENT
- PREGNANCY_UNKNOWN
- ZHAO_PAYMENT != ROKUJO_CONSENT_OR_CONTROL
```

---

## 25｜SUPPLEMENTAL_CHARACTER_005｜李清照

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_005
  unified_order: 25
  name: 李清照
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 文藝／社交熟人節點；沒有白御行私人戀愛或成人關係。
  relation_lifecycle: ACTIVE_DORMANT
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E113：雙籠事件中到場，對白御行挪用其詞作梗作出反應。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index:
- event_id: E11
  title: 白御行家眷與三名正式妻子公開
- event_id: E13
  title: 三十年女兒紅、《不得飲》與公開官人稱呼
- event_id: E15
  title: 李清照《一剪梅》與白御行四言長詩
- event_id: E16
  title: 歪詩局與《玉樹後庭花》補句
- event_id: E26
  title: 仁宗朝夜談：天章閣、馬吊與歷史會計帳
- event_id: E30
  title: 第五夜善後與人物去留
- event_id: E32
  title: 李清照返回自身時代
- event_id: E102
  title: 榴月十一日晚重新開幕完成、女子競技與紅娘壓軸、顧三辭歲再會、趙受益二百兩購四契再贈六條／楊玉環、四大金剛＋李清照女客試場、白玉池會員制接受、錦棠同宿
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
locks:
- LITERARY_SOCIAL != PRIVATE_RELATION
```

---

## 26｜SUPPLEMENTAL_CHARACTER_006｜趙受益

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_006
  unified_order: 26
  name: 趙受益
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 皇帝／常客／白玉池與觀止社交節點；有付費與事件往來，但沒有白御行私人戀愛關係。
  relation_lifecycle: ACTIVE_DORMANT
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E114：與六條進白玉池線；柳永與趙受益『奉旨填詞』伏筆持續。
  - E121：初一觀止正式客帖送帖路線啟動；收件、接受與到場均 PENDING。
  - E121：玩家校正其支付／供養六條御息所、楊玉環在觀止的相關帳；付款不產生兩人的行動／同意權。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved:
  - 初一客帖是否收件、接受與到場。
master_event_index:
- event_id: E19
  title: 宋仁宗評價、權力限制與觀止理念
- event_id: E20
  title: 柳如煙概念體、李師師與趙受益花魁局
- event_id: E22
  title: 顧家豪門宴戲
- event_id: E26
  title: 仁宗朝夜談：天章閣、馬吊與歷史會計帳
- event_id: E30
  title: 第五夜善後與人物去留
- event_id: E34
  title: 後堂地道出現與趙受益抵達
- event_id: E35
  title: 紅娘氏第一筆紅倌交易
- event_id: E82
  title: HOT V2.4：風滿樓、西門暗櫃與五千後算
- event_id: E83
  title: HOT V2.5：開封法網、阿麗婭重定義與六條來訪
- event_id: E94
  title: 榴月一日十日整修起點、雙姝款項／身份翻轉、朱明欠單與鄭成功週轉僅預案、六條／趙受益成人結果與污染校正
- event_id: E95
  title: 辭歲／錦棠／李瓶兒私人開戶、紅袖五十萬反向價格尺與召喚權、紅娘門窗屏風換債、趙受益六條夜集外出
- event_id: E96
  title: 趙受益六條夜集返樓、楊玉環白玉池與荔枝、李師師晨間補考、定陶票據信用／朱明長債方向／曹州案盤點
- event_id: E97
  title: 長恨歌文會、柳如是東林夜談、趙受益宣和地道入席、六條／楊玉環雙線追求與三人約會可能性
- event_id: E102
  title: 榴月十一日晚重新開幕完成、女子競技與紅娘壓軸、顧三辭歲再會、趙受益二百兩購四契再贈六條／楊玉環、四大金剛＋李清照女客試場、白玉池會員制接受、錦棠同宿
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
- event_id: E114
  title: HOT V5.6【REBUILD-R1】｜榴月二十四日白日
- event_id: E121
  title: HOT V5.13-R1｜榴月二十七日晚
locks:
- PAYMENT != ACCESS
- IMPERIAL_STATUS != VENUE_SOVEREIGNTY
- PAYMENT_SUPPORT != ACTION_RIGHTS_OR_CONSENT
```

---

## 27｜SUPPLEMENTAL_CHARACTER_007｜錦棠／周玉娘

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_007
  unified_order: 27
  name: 錦棠／周玉娘
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 與白御行已有正式約會、私人成人事件與喜歡明示；同時是商會明星／主代言方向的重要商業人物，最終經紀約仍 PENDING。
  relation_lifecycle: ACTIVE_CONSTRAINING
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E98：首次正式約會、私人成人事件、白御行喜歡明示與相擁收幕。
  - E117：核心主秀／主代言方向；最終演藝經紀約 PENDING。
  - E119：白御行公開表示初一下午錦棠會出席；實際初一尚未開始。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved:
  - 最終演藝經紀約仍 PENDING；初一實際出席尚未發生。
master_event_index:
- event_id: E93
  title: 九幽帝皇聯誼會散場、辭歲／錦棠雙姝天價競拍、白玉池帝皇團特殊試營運、帝皇多線自然分流
- event_id: E95
  title: 辭歲／錦棠／李瓶兒私人開戶、紅袖五十萬反向價格尺與召喚權、紅娘門窗屏風換債、趙受益六條夜集外出
- event_id: E98
  title: 三十二娘街行與帳戶指令、紅娘中央籠台演出方案、錦棠首次正式約會、私人成人事件、白御行喜歡明示與相擁收幕
- event_id: E102
  title: 榴月十一日晚重新開幕完成、女子競技與紅娘壓軸、顧三辭歲再會、趙受益二百兩購四契再贈六條／楊玉環、四大金剛＋李清照女客試場、白玉池會員制接受、錦棠同宿
- event_id: E114
  title: HOT V5.6【REBUILD-R1】｜榴月二十四日白日
- event_id: E117
  title: HOT V5.9｜榴月二十六日上午
- event_id: E119
  title: HOT V5.11｜榴月二十六日晚
locks:
- PRIVATE_RELATION != COMMERCIAL_CONTRACT
- DIRECTION != SIGNED_CONTRACT
- PLANNED_ATTENDANCE != ARRIVAL
```

---

## 28｜SUPPLEMENTAL_CHARACTER_008｜顧青簡

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_008
  unified_order: 28
  name: 顧青簡
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 公開為定陶商會法律／帳務協作者與顧師爺；私下已有「清簡」地下情／成人歷史。E120 新增一夜自願成人事件，但沒有婚姻、如夫人／妾位、生殖承諾或未來 blanket consent。
  relation_lifecycle: ACTIVE_CONSTRAINING
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E109：榴月十七日晚兩次成人事件成立，公私面向分層。
  - E117：1000兩浮額先清公事，剩餘改白御行私人贈與；精確餘額 UNKNOWN。
  - E118：辦公環境雙向親吻成立；升高接觸時顧青簡握腕叫停，公私界線有效；她接受下工後私訪白家的安排。
  - E120：依約由後門私訪；先主動拉近／親吻，之後雙方自願成人事件成立；本夜拒絕精液進入生殖道。
  - E120：未來母職談話只到條件式可能；沒有現在受孕／生子承諾。
  - E121：被指定翌日先擬十一哥本金只進不出／年息3%代理補償方向草約；截至 cutoff 未簽。
  current_constraints:
  - 十一哥3%帳戶／信託仍須先擬、讀給本人並取得接受。
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries:
  - E120 私訪／成人事件屬私人關係證據，不因公開職務而自動外傳。
  unresolved:
  - 十一哥信託契約是否被本人接受並正式開戶。
master_event_index:
- event_id: E87
  title: 曹州假印立案、定陶總會架構、京師女性時尚企畫、師師抱睡
- event_id: E109
  title: HOT V5.1｜榴月十八日晚
- event_id: E110
  title: HOT V5.2｜榴月十九日晚
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
- event_id: E114
  title: HOT V5.6【REBUILD-R1】｜榴月二十四日白日
- event_id: E116
  title: HOT V5.8｜榴月二十五日夜
- event_id: E117
  title: HOT V5.9｜榴月二十六日上午
- event_id: E118
  title: HOT V5.10｜榴月二十六日下午
- event_id: E120
  title: HOT V5.12｜榴月二十六日晚後續～榴月二十七日晚
- event_id: E121
  title: HOT V5.13-R1｜榴月二十七日晚
locks:
- PUBLIC_ROLE != PRIVATE_RELATION
- GIFT != STATUS_PROMOTION
- ADULT_EVENT != PREGNANCY_OR_CONCUBINE_STATUS
- PRIVATE_RELATION != PUBLIC_OFFICE_ROLE
```

---

## 29｜SUPPLEMENTAL_CHARACTER_009｜楊玉環

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_009
  unified_order: 29
  name: 楊玉環
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 白玉池成人歷史已成立；對未來白＋楊＋六條三人方向曾表示目前有興趣，但可撤回，無固定情人名位。
  relation_lifecycle: ACTIVE_DORMANT
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E104：白御行×楊玉環私人成人事件成立。
  - E112：仍願意／有興趣考慮三人方向，屬可撤回未來方向。
  - E121：玩家校正其在觀止相關帳由趙受益支付／供養；付款不賦予趙受益她的行動或同意權。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index:
- event_id: E96
  title: 趙受益六條夜集返樓、楊玉環白玉池與荔枝、李師師晨間補考、定陶票據信用／朱明長債方向／曹州案盤點
- event_id: E97
  title: 長恨歌文會、柳如是東林夜談、趙受益宣和地道入席、六條／楊玉環雙線追求與三人約會可能性
- event_id: E102
  title: 榴月十一日晚重新開幕完成、女子競技與紅娘壓軸、顧三辭歲再會、趙受益二百兩購四契再贈六條／楊玉環、四大金剛＋李清照女客試場、白玉池會員制接受、錦棠同宿
- event_id: E103
  title: 榴月十二日晚白家採購規劃、蘇清十八日商會工拆帳、妓籍終身法位鎖、阿莉婭處女拍賣標的與紅娘雙人場、三十二娘妓籍申請、楊玉環白玉池代言首夜、黑公子×小桃百兩交易與同宿意向
- event_id: E104
  title: HOT V4.6｜榴月十三日晚
- event_id: E108
  title: HOT V5.0｜榴月十六日下午
- event_id: E111
  title: HOT V5.3｜榴月二十日白日
- event_id: E112
  title: HOT V5.4｜榴月二十日白日
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
- event_id: E114
  title: HOT V5.6【REBUILD-R1】｜榴月二十四日白日
- event_id: E121
  title: HOT V5.13-R1｜榴月二十七日晚
locks:
- INTEREST != CONSENT_FOR_FUTURE_EVENT
- ZHAO_PAYMENT != YANG_CONSENT_OR_CONTROL
```

---

## 30｜SUPPLEMENTAL_CHARACTER_010｜柳如是

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_010
  unified_order: 30
  name: 柳如是
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 文藝／社交人物；MASTER 僅有入線／社交證據，未建立白御行私人關係。
  relation_lifecycle: ACTIVE_DORMANT
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E97：進入相關社交事件。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index:
- event_id: E97
  title: 長恨歌文會、柳如是東林夜談、趙受益宣和地道入席、六條／楊玉環雙線追求與三人約會可能性
locks:
- SOCIAL_PRESENCE != PRIVATE_RELATION
```

---

## 31｜SUPPLEMENTAL_CHARACTER_011｜薛濤

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_011
  unified_order: 31
  name: 薛濤
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 匿名／身份揭露與女客夜相關節點；MASTER 未建立白御行私人戀愛或成人關係。
  relation_lifecycle: ACTIVE_DORMANT
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E107：匿名薛濤進線，當時白御行未知其真身。
  - E113：合法確認狀態仍依父 MASTER，不因後續自動補完。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index:
- event_id: E107
  title: HOT V4.9｜榴月十五日晚
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
locks:
- DIRECTOR_IDENTITY != PLAYER_KNOWLEDGE
```

---

## 32｜SUPPLEMENTAL_CHARACTER_012｜魚玄機

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_012
  unified_order: 32
  name: 魚玄機
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 成年紅線女客／競技與社交節點；不是觀止妓籍，與白御行未建立私人戀愛關係。
  relation_lifecycle: ACTIVE_DORMANT
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E110：中央籠台『馬』題詩賽勝洛陽馬商；只承諾看灰青難馬。
  - E113：雙籠事件中到場。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index:
- event_id: E104
  title: HOT V4.6｜榴月十三日晚
- event_id: E107
  title: HOT V4.9｜榴月十五日晚
- event_id: E110
  title: HOT V5.2｜榴月十九日晚
- event_id: E111
  title: HOT V5.3｜榴月二十日白日
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
locks:
- GUEST != SEX_WORKER
- PROMISE_TO_LOOK != TOUCH_RIDE_TRAIN
```

---

## 33｜SUPPLEMENTAL_CHARACTER_013｜失仙

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_013
  unified_order: 33
  name: 失仙
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: ACTIVE_ROUTE_CHARACTER
current_route_state:
  relation_to_player: 浮月閣／觀止競賽與異常線核心節點；與白御行有一日邀約賭與500兩當日買斷，但無戀愛或成人關係。E118–E121 她本人仍未返場，去向 UNKNOWN。
  relation_lifecycle: ACTIVE_CONSTRAINING
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E113：入場、與紅娘九日營收競賽、一日邀約賭成立。
  - E114：白御行500兩買斷失仙當日餘時；不是性愛購買。
  - E117：獨自離開，去向 UNKNOWN；沈家／陳州／身體真相仍 UNKNOWN。
  - E118：時空道人失言提供專名「浮月閣」；只建立名字線索，不證成失仙所屬。
  - E118/E119：一名陌生男子問「姓失的姑娘」；其身份與意圖 UNKNOWN，不能合併為浮月閣同夥。
  - E121：只取得條件式推論——若她確屬時空道人曾稱「不是人」的同一浮月閣群體，才提高非普通人的可能性。本人所屬／非人身份仍未證明。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries:
  - 人物池／導演隱藏真相不得倒灌白御行／潘金蓮知情。
  unresolved:
  - 去向、浮月閣所屬、沈家／陳州／身體真相均 UNKNOWN。
master_event_index:
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
- event_id: E114
  title: HOT V5.6【REBUILD-R1】｜榴月二十四日白日
- event_id: E116
  title: HOT V5.8｜榴月二十五日夜
- event_id: E117
  title: HOT V5.9｜榴月二十六日上午
- event_id: E118
  title: HOT V5.10｜榴月二十六日下午
- event_id: E119
  title: HOT V5.11｜榴月二十六日晚
- event_id: E120
  title: HOT V5.12｜榴月二十六日晚後續～榴月二十七日晚
- event_id: E121
  title: HOT V5.13-R1｜榴月二十七日晚
locks:
- BUYOUT != SEXUAL_ACCESS
- MYSTERY_LINK != ONTOLOGICAL_PROOF
- FUYUEGE_NAME != MEMBERSHIP
- CONDITIONAL_NONHUMAN_INFERENCE != ONTOLOGICAL_PROOF
```

---

## 34｜SUPPLEMENTAL_CHARACTER_014｜失美

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_014
  unified_order: 34
  name: 失美
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: REFERENCE_ONLY
current_route_state:
  relation_to_player: 僅因浮月閣四大花魁基線於 E113 被提及；MASTER 未建立實際入白御行線。
  relation_lifecycle: NOT_ENTERED_ROUTE
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E113：人物池／浮月閣基線被提及。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index:
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
locks:
- REFERENCE != ARRIVAL
```

---

## 35｜SUPPLEMENTAL_CHARACTER_015｜失蘿

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_015
  unified_order: 35
  name: 失蘿
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: REFERENCE_ONLY
current_route_state:
  relation_to_player: 僅因浮月閣四大花魁基線於 E113 被提及；MASTER 未建立實際入白御行線。
  relation_lifecycle: NOT_ENTERED_ROUTE
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E113：人物池／浮月閣基線被提及。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index:
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
locks:
- REFERENCE != ARRIVAL
```

---

## 36｜SUPPLEMENTAL_CHARACTER_016｜錯位

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_016
  unified_order: 36
  name: 錯位
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: REFERENCE_ONLY
current_route_state:
  relation_to_player: 僅因浮月閣四大花魁基線於 E113 被提及；MASTER 未建立實際入白御行線。
  relation_lifecycle: NOT_ENTERED_ROUTE
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary:
  - E113：人物池／浮月閣基線被提及。
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index:
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
locks:
- REFERENCE != ARRIVAL
```

---

## 37｜SUPPLEMENTAL_CHARACTER_017｜香雲

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_017
  unified_order: 37
  name: 香雲
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 38｜SUPPLEMENTAL_CHARACTER_018｜花晨

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_018
  unified_order: 38
  name: 花晨
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 39｜SUPPLEMENTAL_CHARACTER_019｜艷芳

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_019
  unified_order: 39
  name: 艷芳
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 40｜SUPPLEMENTAL_CHARACTER_020｜玉香

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_020
  unified_order: 40
  name: 玉香
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 41｜SUPPLEMENTAL_CHARACTER_021｜瑞珠

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_021
  unified_order: 41
  name: 瑞珠
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 42｜SUPPLEMENTAL_CHARACTER_022｜瑞玉

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_022
  unified_order: 42
  name: 瑞玉
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 43｜SUPPLEMENTAL_CHARACTER_023｜顧仙娘

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_023
  unified_order: 43
  name: 顧仙娘
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 44｜SUPPLEMENTAL_CHARACTER_024｜王婆

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_024
  unified_order: 44
  name: 王婆
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 45｜SUPPLEMENTAL_CHARACTER_025｜林太太

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_025
  unified_order: 45
  name: 林太太
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 46｜SUPPLEMENTAL_CHARACTER_026｜王六兒

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_026
  unified_order: 46
  name: 王六兒
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 47｜SUPPLEMENTAL_CHARACTER_027｜吳銀兒

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_027
  unified_order: 47
  name: 吳銀兒
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 48｜SUPPLEMENTAL_CHARACTER_028｜薛嫂

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_028
  unified_order: 48
  name: 薛嫂
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 49｜SUPPLEMENTAL_CHARACTER_029｜吳月娘

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_029
  unified_order: 49
  name: 吳月娘
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 50｜SUPPLEMENTAL_CHARACTER_030｜孟玉樓

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_030
  unified_order: 50
  name: 孟玉樓
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 51｜SUPPLEMENTAL_CHARACTER_031｜孫雪娥

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_031
  unified_order: 51
  name: 孫雪娥
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 52｜SUPPLEMENTAL_CHARACTER_032｜李嬌兒

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_032
  unified_order: 52
  name: 李嬌兒
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 53｜SUPPLEMENTAL_CHARACTER_033｜鄭愛月

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_033
  unified_order: 53
  name: 鄭愛月
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 54｜SUPPLEMENTAL_CHARACTER_034｜白玉潔

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_034
  unified_order: 54
  name: 白玉潔
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 55｜SUPPLEMENTAL_CHARACTER_035｜張明姝

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_035
  unified_order: 55
  name: 張明姝
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 56｜SUPPLEMENTAL_CHARACTER_036｜孫清倩

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_036
  unified_order: 56
  name: 孫清倩
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 57｜SUPPLEMENTAL_CHARACTER_037｜沈玉晶

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_037
  unified_order: 57
  name: 沈玉晶
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 58｜SUPPLEMENTAL_CHARACTER_038｜高承義

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_038
  unified_order: 58
  name: 高承義
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 59｜SUPPLEMENTAL_CHARACTER_039｜李明遠

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_039
  unified_order: 59
  name: 李明遠
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 60｜SUPPLEMENTAL_CHARACTER_040｜王慎行

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_040
  unified_order: 60
  name: 王慎行
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 61｜SUPPLEMENTAL_CHARACTER_041｜王廷衡

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_041
  unified_order: 61
  name: 王廷衡
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。
  relation_lifecycle: NOT_ESTABLISHED
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries: []
  unresolved: []
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
```

---

## 62｜SUPPLEMENTAL_CHARACTER_042｜舍方知

```yaml
route_id: GUANZHI_BAIYUXING_ROUTE
base_ref:
  lcapg_source_id: SUPPLEMENTAL_CHARACTER_042
  unified_order: 62
  name: 舍方知
compiled_from:
  memory_generation: V5.13-R1
  master_file: 觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md
  master_record_version: V5.13-R1-HARD
  master_sha256: 19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5
  cutoff_event: E121
  cutoff_time: 理火三年榴月二十七日晚
route_presence:
  state: NOT_ESTABLISHED_IN_MASTER_ROUTE
current_route_state:
  relation_to_player: 截至 MASTER V5.13-R1 cutoff，舍方知尚未在白御行線建立實際相遇／Route 事件；其正式入 Route 發生於較新的 HOT V5.14，不得倒灌本代 RCL。
  relation_lifecycle: NOT_ENTERED_ROUTE
  route_ambition_state:
    baseline_ref: LCAPG V3.3.9 BASE_AMBITION if present; not duplicated here
    directions: []
    status: UNKNOWN
    evidence_event_ids: []
    commit_rule: Only evidence-supported / GM-locked route evolution; no free-form mind reading
  identity_and_status_delta: {}
  evidence_summary: []
  current_constraints: []
  active_contracts_or_debts: []
  privacy_or_knowledge_boundaries:
  - LCAPG BASE exists, but V5.13-R1 MASTER has no player-route entry evidence.
  unresolved:
  - 玩家線初見／正式入 Route 尚未發生於本 MASTER cutoff。
master_event_index: []
locks:
- LCAPG_BASE_EXISTS != ROUTE_ENTRY
- HOT_V5_14_ROUTE_ENTRY != MASTER_V5_13_R1_STATE
```

---

# 3｜臨時 Route Character Registry｜無 LCAPG BASE

> 以下人物具有 MASTER E01–E121 的實際 Route evidence，但沒有 LCAPG 正式 BASE。編號只屬白御行線，不取得跨線人物卡法位。

```yaml
TEMP_ID_POLICY:
  named_family: "BYX_TMP_###"
  anonymous_family: "BYX_ANON_###"
  stable_within_route: true
  cross_route_authority: false
  lcapg_admission: false
  promotion_requires: "GM explicit LCAPG successor"
  current_master_cutoff: "E121 / V5.13-R1"
```

## BYX_TMP_001｜似伊

```yaml
route_character_id: BYX_TMP_001
name_or_label: 似伊
base_character_ref: null
route_summary: 跨世界／私人從屬歷史節點；缺乏 LCAPG BASE。
master_event_index:
- event_id: E12
  title: 似伊影像與紅袖可能未來
- event_id: E24
  title: 似伊實體入場與退場
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_002｜阿泠

```yaml
route_character_id: BYX_TMP_002
name_or_label: 阿泠
base_character_ref: null
route_summary: 白玉池自主空間人物；自選姓名，拒絕白姓／妹妹／白家人／所有物定位；白玉池是否營業與服務由她決定；E119 再次保留白玉池加場／進池決定權；本輪沒有批准任何三人組、沒有開始洗浴。
master_event_index:
- event_id: E57
  title: 阿泠現身與白玉池水療提案
- event_id: E58
  title: 李瓶兒入池與追求機會未關閉
- event_id: E60
  title: 白玉池封池、蘇清研究與潘金蓮尚未介入之初始狀態
- event_id: E67
  title: 阿泠兄妹方向仍未成立
- event_id: E86
  title: 潘身籍副冊補證、白玉池許願幣／定存框架、師師道歉修復與如夫人再確認
- event_id: E109
  title: HOT V5.1｜榴月十八日晚
- event_id: E112
  title: HOT V5.4｜榴月二十日白日
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
- event_id: E114
  title: HOT V5.6【REBUILD-R1】｜榴月二十四日白日
- event_id: E119
  title: HOT V5.11｜榴月二十六日晚
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

### Route-local 8-axis｜EVIDENCE-LIMITED

> 這是 MASTER evidence 的路線工作卡，不是 LCAPG BASE；資料不足處不補全。

```yaml
ROUTE_LOCAL_8AXIS:
  A_attention: "優先注意白玉池本身、來客是否尊重場域與她自己的決定權。"
  T_tension: "自主場域 vs 他人命名／收編；願意幫忙 vs 被當成資產。"
  R_relation: "可建立合作與見證，但拒絕被白御行命名為妹妹、白家人或所有物。"
  D_decision: "是否開池、是否提供水療、做幾席由她自己決定。"
  V_voice: "清楚、簡短，對越界身份宣告直接否決。"
  C_closure: "以場域規矩與『這是我的地方』收束。"
  B_boundary: "他人付款、稱呼或親近不得奪走白玉池與她自身的決定權。"
  F_anti_flatness: "不能壓成神秘水靈寵物；她是有場域主權與實務判斷的人物。"
  locks:
    - "ROUTE_LOCAL_AXIS != LCAPG BASE"
    - "MASTER EVIDENCE ONLY / NO EXTERNAL BIOGRAPHY FILL"
```

---

---

## BYX_TMP_003｜常煒

```yaml
route_character_id: BYX_TMP_003
name_or_label: 常煒
base_character_ref: null
route_summary: 定陶商會副會長／營運協作者；E117 物流女子360兩年終獎抵扣條件固定；E118 在 HOT V5.9 會議收尾後答應先叫人粗看初一湖心島船案；只到安排／粗看方向，未自動完成船案。
master_event_index:
- event_id: E79
  title: HOT V2.1：定陶商戰、蘇清私約與白玉池補固
- event_id: E117
  title: HOT V5.9｜榴月二十六日上午
- event_id: E118
  title: HOT V5.10｜榴月二十六日下午
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

### Route-local 8-axis｜EVIDENCE-LIMITED

> 這是 MASTER evidence 的路線工作卡，不是 LCAPG BASE；資料不足處不補全。

```yaml
ROUTE_LOCAL_8AXIS:
  A_attention: "先看商會能不能做、帳怎麼算、人是否真的能把事做完。"
  T_tension: "副會長責任 vs 白御行的高風險新構想；舊帳抱怨 vs 繼續合作。"
  R_relation: "長期商會同僚，可反駁、抱怨、接受條件；不是唯命是從。"
  D_decision: "偏執行可行性；同意前會把成本、責任、實際人手拆開。"
  V_voice: "務實、會抱怨、算帳味重。"
  C_closure: "把口頭構想落成誰去看、誰去辦、何時回報。"
  B_boundary: "不替白御行把未知執行結果寫成已完成。"
  F_anti_flatness: "不能只當吐槽副會長；他承擔定陶商會真實營運重量。"
  locks:
    - "ROUTE_LOCAL_AXIS != LCAPG BASE"
    - "MASTER EVIDENCE ONLY / NO EXTERNAL BIOGRAPHY FILL"
```

---

---

## BYX_TMP_004｜沈萬三

```yaml
route_character_id: BYX_TMP_004
name_or_label: 沈萬三
base_character_ref: null
route_summary: 高能力商業節點；與白御行／定陶形成停止代理試探與技術合作原則，未簽盟書、非永久同盟；風滿樓三金主之一。
master_event_index:
- event_id: E79
  title: HOT V2.1：定陶商戰、蘇清私約與白玉池補固
- event_id: E81
  title: HOT V2.3：定陶—沈萬三合作與多線案件升級
- event_id: E82
  title: HOT V2.4：風滿樓、西門暗櫃與五千後算
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

### Route-local 8-axis｜EVIDENCE-LIMITED

> 這是 MASTER evidence 的路線工作卡，不是 LCAPG BASE；資料不足處不補全。

```yaml
ROUTE_LOCAL_8AXIS:
  A_attention: "先看技術、代理權、資本與合作邊界。"
  T_tension: "合作獲利 vs 被定陶吸收；試探對手 vs 避免全面開戰。"
  R_relation: "與白御行／定陶有合作原則，但沒有盟書與永久同盟。"
  D_decision: "接受可交換的合作，保留自己獨立商人位置。"
  V_voice: "MASTER 證據不足，不固定華麗聲紋；以商業條件與邊界為主。"
  C_closure: "讓合作停在可核對的原則而非口號結盟。"
  B_boundary: "合作 != 共同統治；金主 != 案情定調權。"
  F_anti_flatness: "不能只作『天下首富』梗；在本線首先是能與定陶互相試探的獨立商業節點。"
  locks:
    - "ROUTE_LOCAL_AXIS != LCAPG BASE"
    - "MASTER EVIDENCE ONLY / NO EXTERNAL BIOGRAPHY FILL"
```

---

---

## BYX_TMP_005｜許慎言

```yaml
route_character_id: BYX_TMP_005
name_or_label: 許慎言
base_character_ref: null
route_summary: 蘇清 principal lawyer／法律程序節點；受定陶資助按摩恢復券，不因此取得案件結果主權。
master_event_index:
- event_id: E82
  title: HOT V2.4：風滿樓、西門暗櫃與五千後算
- event_id: E84
  title: 京師軍械案鏡頭收網、觀止民事戰重啟、許慎言七十二小時按摩券
- event_id: E85
  title: 潘金蓮返樓、五千原款重分類、五萬索賠、身籍與重新掛牌條件式討論
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

### Route-local 8-axis｜EVIDENCE-LIMITED

> 這是 MASTER evidence 的路線工作卡，不是 LCAPG BASE；資料不足處不補全。

```yaml
ROUTE_LOCAL_8AXIS:
  A_attention: "先看委託人、證據、契約與法律責任能否成立。"
  T_tension: "蘇清委託利益 vs 定陶出資；程序推進 vs 不越過證據。"
  R_relation: "蘇清 principal lawyer；與白御行／定陶主要是資助與程序合作。"
  D_decision: "按證據鏈與委託權限行事。"
  V_voice: "程序性、精確，避免把主張直接當判決。"
  C_closure: "回到需要的證據、程序與下一步法律動作。"
  B_boundary: "出資 != 裁判權；律師 != 世界真相 owner。"
  F_anti_flatness: "不能成為替玩家宣布法律結論的規則朗讀器。"
  locks:
    - "ROUTE_LOCAL_AXIS != LCAPG BASE"
    - "MASTER EVIDENCE ONLY / NO EXTERNAL BIOGRAPHY FILL"
```

---

---

## BYX_TMP_006｜程景衡

```yaml
route_character_id: BYX_TMP_006
name_or_label: 程景衡
base_character_ref: null
route_summary: 定陶商會調查／押運與外圍追查節點。
master_event_index:
- event_id: E49
  title: 定陶十二車三烤鹽失竊與全數找回
- event_id: E54
  title: 涉案者押回定陶、補假與調查授權
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_007｜西門慶

```yaml
route_character_id: BYX_TMP_007
name_or_label: 西門慶
base_character_ref: null
route_summary: 五千舊案、廣源與開封府程序核心外部人物；關係具對抗／法律因果，不是玩家私人關係。
master_event_index:
- event_id: E81
  title: HOT V2.3：定陶—沈萬三合作與多線案件升級
- event_id: E82
  title: HOT V2.4：風滿樓、西門暗櫃與五千後算
- event_id: E83
  title: HOT V2.5：開封法網、阿麗婭重定義與六條來訪
- event_id: E84
  title: 京師軍械案鏡頭收網、觀止民事戰重啟、許慎言七十二小時按摩券
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_008｜白三十二娘／三十二娘

```yaml
route_character_id: BYX_TMP_008
name_or_label: 白三十二娘／三十二娘
base_character_ref: null
route_summary: 白御行私人持契成年工作人員；白家日常調度與多次跑腿／預算線。
master_event_index:
- event_id: E88
  title: 女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限
- event_id: E98
  title: 三十二娘街行與帳戶指令、紅娘中央籠台演出方案、錦棠首次正式約會、私人成人事件、白御行喜歡明示與相擁收幕
- event_id: E103
  title: 榴月十二日晚白家採購規劃、蘇清十八日商會工拆帳、妓籍終身法位鎖、阿莉婭處女拍賣標的與紅娘雙人場、三十二娘妓籍申請、楊玉環白玉池代言首夜、黑公子×小桃百兩交易與同宿意向
- event_id: E109
  title: HOT V5.1｜榴月十八日晚
- event_id: E116
  title: HOT V5.8｜榴月二十五日夜
- event_id: E117
  title: HOT V5.9｜榴月二十六日上午
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_009｜白明礬

```yaml
route_character_id: BYX_TMP_009
name_or_label: 白明礬
base_character_ref: null
route_summary: 白御行私人持契成年工作人員；方掌櫃布莊／染布線，E117 私下學技術意圖不得外洩。
master_event_index:
- event_id: E88
  title: 女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限
- event_id: E99
  title: 榴月四日兩牙行二十三名成年候選雙向遴選、九名丫鬟成交分配、制服／自願剪髮方案、白希白明礬初教、十四名落選者吃麵收尾
- event_id: E117
  title: HOT V5.9｜榴月二十六日上午
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_010｜白紅伶

```yaml
route_character_id: BYX_TMP_010
name_or_label: 白紅伶
base_character_ref: null
route_summary: 白御行私人持契成年工作人員；曾執行紅娘免費全套假傳聞煙幕。
master_event_index:
- event_id: E88
  title: 女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限
- event_id: E91
  title: 浮香自願給床與成人夜、紅娘煙幕揭穿、九幽帝皇聯誼會正式訂單
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_011｜白希

```yaml
route_character_id: BYX_TMP_011
name_or_label: 白希
base_character_ref: null
route_summary: 白御行私人持契成年工作人員。
master_event_index:
- event_id: E88
  title: 女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限
- event_id: E99
  title: 榴月四日兩牙行二十三名成年候選雙向遴選、九名丫鬟成交分配、制服／自願剪髮方案、白希白明礬初教、十四名落選者吃麵收尾
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_012｜沈夫人

```yaml
route_character_id: BYX_TMP_012
name_or_label: 沈夫人
base_character_ref: null
route_summary: 一夜型自願成人事件；只限兩人，事後無第二次義務、無戀愛／情婦／婚姻／排他。
master_event_index:
- event_id: E110
  title: HOT V5.2｜榴月十九日晚
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_013｜程小姐

```yaml
route_character_id: BYX_TMP_013
name_or_label: 程小姐
base_character_ref: null
route_summary: 白家成年女客；未參與成人事件，對若當時是否會上樓回答 UNKNOWN。
master_event_index:
- event_id: E110
  title: HOT V5.2｜榴月十九日晚
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_014｜蘇東坡

```yaml
route_character_id: BYX_TMP_014
name_or_label: 蘇東坡
base_character_ref: null
route_summary: 文士／女客夜與初一晚場主持邀請節點；E117 主持與出席仍 PENDING；E121 初一正式主持人工作約送帖路線啟動；收件／接受／到場仍 PENDING。
master_event_index:
- event_id: E20
  title: 柳如煙概念體、李師師與趙受益花魁局
- event_id: E26
  title: 仁宗朝夜談：天章閣、馬吊與歷史會計帳
- event_id: E30
  title: 第五夜善後與人物去留
- event_id: E106
  title: HOT V4.8｜榴月十五日下午
- event_id: E107
  title: HOT V4.9｜榴月十五日晚
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
- event_id: E117
  title: HOT V5.9｜榴月二十六日上午
- event_id: E121
  title: HOT V5.13-R1｜榴月二十七日晚
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

### Route-local 8-axis｜EVIDENCE-LIMITED

> 這是 MASTER evidence 的路線工作卡，不是 LCAPG BASE；資料不足處不補全。

```yaml
ROUTE_LOCAL_8AXIS:
  A_attention: "先看文題、場面、可寫之趣與人物之間真正有意思的衝突。"
  T_tension: "名士自由 vs 被商業活動利用；玩笑豪放 vs 自己是否願意出席。"
  R_relation: "與白御行是文士／社交線，初一主持仍待本人回應。"
  D_decision: "是否出席、主持、寫詞由本人決定。"
  V_voice: "MASTER 只提供有限路線證據；保持蘇東坡式機鋒候選但不以外部知識補滿。"
  C_closure: "可用一句詩文／玩笑收束，但不能替他預先答應邀請。"
  B_boundary: "被邀請 != 接受；潤筆費 != 必須寫指定內容。"
  F_anti_flatness: "不能只作名人彩蛋或商業背書工具。"
  locks:
    - "ROUTE_LOCAL_AXIS != LCAPG BASE"
    - "MASTER EVIDENCE ONLY / NO EXTERNAL BIOGRAPHY FILL"
```

---

---

## BYX_TMP_015｜陳季常

```yaml
route_character_id: BYX_TMP_015
name_or_label: 陳季常
base_character_ref: null
route_summary: 文士／女客夜節點；與金面具女客事件及柳月娥後續相關。
master_event_index:
- event_id: E106
  title: HOT V4.8｜榴月十五日下午
- event_id: E107
  title: HOT V4.9｜榴月十五日晚
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_016｜佛印

```yaml
route_character_id: BYX_TMP_016
name_or_label: 佛印
base_character_ref: null
route_summary: 文士／女客夜社交節點。
master_event_index:
- event_id: E106
  title: HOT V4.8｜榴月十五日下午
- event_id: E107
  title: HOT V4.9｜榴月十五日晚
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_017｜蘇小妹

```yaml
route_character_id: BYX_TMP_017
name_or_label: 蘇小妹
base_character_ref: null
route_summary: 成年紅線女客識別；拒絕當場登妓籍。
master_event_index:
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_018｜柳月娥

```yaml
route_character_id: BYX_TMP_018
name_or_label: 柳月娥
base_character_ref: null
route_summary: 陳季常妻；雙籠投蛋事件與金面具身份疑雲節點，客觀身份仍 UNKNOWN。
master_event_index:
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_019｜柳永

```yaml
route_character_id: BYX_TMP_019
name_or_label: 柳永
base_character_ref: null
route_summary: 本人已入觀止與白玉池；商會自由顧問方向 PROPOSED，是否接受與報酬 PENDING。
master_event_index:
- event_id: E114
  title: HOT V5.6【REBUILD-R1】｜榴月二十四日白日
- event_id: E117
  title: HOT V5.9｜榴月二十六日上午
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

### Route-local 8-axis｜EVIDENCE-LIMITED

> 這是 MASTER evidence 的路線工作卡，不是 LCAPG BASE；資料不足處不補全。

```yaml
ROUTE_LOCAL_8AXIS:
  A_attention: "先看詞、名聲、酒席與『奉旨填詞』這類能不能當真。"
  T_tension: "才名與市井風月；皇命笑話與實際付帳；自由文士 vs 商會顧問身份。"
  R_relation: "已與白御行、趙受益產生直接互動；商會自由顧問方向仍待接受。"
  D_decision: "可參與、可評詞，但正式顧問身份與報酬需本人答應。"
  V_voice: "有文人氣與自嘲空間；不得因『奉旨填詞』就免帳。"
  C_closure: "把漂亮話落回詞、錢或是否真的接這份差事。"
  B_boundary: "PROPOSED CONSULTANT != ACCEPTED CONTRACT。"
  F_anti_flatness: "不能只作『奉旨嫖娼』笑話；他仍是有自己名聲與選擇的文人。"
  locks:
    - "ROUTE_LOCAL_AXIS != LCAPG BASE"
    - "MASTER EVIDENCE ONLY / NO EXTERNAL BIOGRAPHY FILL"
```

---

---

## BYX_TMP_020｜沈秋

```yaml
route_character_id: BYX_TMP_020
name_or_label: 沈秋
base_character_ref: null
route_summary: 沈家空房／後續現場節點。
master_event_index:
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
- event_id: E116
  title: HOT V5.8｜榴月二十五日夜
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_021｜程素娘

```yaml
route_character_id: BYX_TMP_021
name_or_label: 程素娘
base_character_ref: null
route_summary: 沈家／失仙晨報資訊節點。
master_event_index:
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
- event_id: E117
  title: HOT V5.9｜榴月二十六日上午
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_022｜桃枝

```yaml
route_character_id: BYX_TMP_022
name_or_label: 桃枝
base_character_ref: null
route_summary: 陪席契約爭議與開放續約營運實務節點；原契約／20兩押金最終結算未確認。
master_event_index:
- event_id: E110
  title: HOT V5.2｜榴月十九日晚
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_023｜方掌櫃

```yaml
route_character_id: BYX_TMP_023
name_or_label: 方掌櫃
base_character_ref: null
route_summary: 布匹／驗貨／品質監督與染布線商業節點。
master_event_index:
- event_id: E117
  title: HOT V5.9｜榴月二十六日上午
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_024｜黑公子

```yaml
route_character_id: BYX_TMP_024
name_or_label: 黑公子
base_character_ref: null
route_summary: 觀止交易／同宿意向事件節點。
master_event_index:
- event_id: E103
  title: 榴月十二日晚白家採購規劃、蘇清十八日商會工拆帳、妓籍終身法位鎖、阿莉婭處女拍賣標的與紅娘雙人場、三十二娘妓籍申請、楊玉環白玉池代言首夜、黑公子×小桃百兩交易與同宿意向
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_025｜小桃

```yaml
route_character_id: BYX_TMP_025
name_or_label: 小桃
base_character_ref: null
route_summary: 與黑公子百兩交易／同宿意向事件節點。
master_event_index:
- event_id: E103
  title: 榴月十二日晚白家採購規劃、蘇清十八日商會工拆帳、妓籍終身法位鎖、阿莉婭處女拍賣標的與紅娘雙人場、三十二娘妓籍申請、楊玉環白玉池代言首夜、黑公子×小桃百兩交易與同宿意向
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_026｜石魁

```yaml
route_character_id: BYX_TMP_026
name_or_label: 石魁
base_character_ref: null
route_summary: 河東車行牙人；被捕並與藏貨、分帳、員工資訊收買線相關。
master_event_index:
- event_id: E51
  title: 石魁、灰簿先生與吳六未決
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_027｜灰簿先生

```yaml
route_character_id: BYX_TMP_027
name_or_label: 灰簿先生
base_character_ref: null
route_summary: 底層口供提及之未知人物／稱呼；本體是否單一人物 UNKNOWN。
master_event_index:
- event_id: E51
  title: 石魁、灰簿先生與吳六未決
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_028｜吳六

```yaml
route_character_id: BYX_TMP_028
name_or_label: 吳六
base_character_ref: null
route_summary: 東倉副倉簿；是否涉案 NOT_ESTABLISHED。
master_event_index:
- event_id: E51
  title: 石魁、灰簿先生與吳六未決
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_029｜梅花面具成年紅線女客

```yaml
route_character_id: BYX_TMP_029
name_or_label: 梅花面具成年紅線女客
base_character_ref: null
route_summary: 與白御行完成一次自願露水成人事件；身份未固定。
master_event_index:
- event_id: E107
  title: HOT V4.9｜榴月十五日晚
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_ANON_001｜金面具女客

```yaml
route_character_id: BYX_ANON_001
name_or_label: 金面具女客
base_character_ref: null
route_summary: 與陳季常同行／進房；客觀身份 UNKNOWN，柳月娥嫌疑升高但未證成。
master_event_index:
- event_id: E107
  title: HOT V4.9｜榴月十五日晚
- event_id: E113
  title: HOT V5.5｜榴月二十四日清晨
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_ANON_002｜觀止大堂陌生中年男人

```yaml
route_character_id: BYX_ANON_002
name_or_label: 觀止大堂陌生中年男人
base_character_ref: null
route_summary: 長時間觀察籠台、樓梯、欄杆與出入口；身份／目的 UNKNOWN。
master_event_index:
- event_id: E111
  title: HOT V5.3｜榴月二十日白日
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_030｜洛陽馬商

```yaml
route_character_id: BYX_TMP_030
name_or_label: 洛陽馬商
base_character_ref: null
route_summary: 魚玄機『馬』題詩賽對手；勝負已定，其他私人關係未建立。
master_event_index:
- event_id: E110
  title: HOT V5.2｜榴月十九日晚
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_ANON_003｜年輕車夫首告者

```yaml
route_character_id: BYX_ANON_003
name_or_label: 年輕車夫首告者
base_character_ref: null
route_summary: 姓名未公開固化；首告後本人與家眷受保護、急債清除並領賞。
master_event_index:
- event_id: E50
  title: 第一告密者受保護與領賞
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
```

---

---

## BYX_TMP_031｜時空道人

```yaml
route_character_id: BYX_TMP_031
name_or_label: 時空道人
base_character_ref: null
route_summary: 跨時空觀察／路由節點；E118 失言說出「浮月閣」專名，E121 對槐生／十一哥只給觀察性判斷並提出初一路由「先看人，再看線」。其說法不是世界機制定律，也不替觀止決定誰必須到場。
master_event_index:
- event_id: E64
  title: 時空道人承認漏籤
- event_id: E118
  title: HOT V5.10｜榴月二十六日下午
- event_id: E121
  title: HOT V5.13-R1｜榴月二十七日晚
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
locks:
- OBSERVATIONAL_JUDGMENT != WORLD_MECHANISM
- ROUTING_HELP != GUARANTEED_ARRIVAL
- NAME_LEAK != MEMBERSHIP_PROOF
```

---

## BYX_ANON_004｜偏廳問失仙陌生男子

```yaml
route_character_id: BYX_ANON_004
name_or_label: 偏廳問失仙陌生男子
base_character_ref: null
route_summary: 約二十七八歲、帶兩名隨從；E118 到觀止問昨日「姓失的姑娘」是否在，得知未見後留下飲酒；E119 與紅娘桌只有最低限度營業接觸。身份、意圖、與失仙／浮月閣／沈家／陳州的關係均 UNKNOWN。
master_event_index:
- event_id: E118
  title: HOT V5.10｜榴月二十六日下午
- event_id: E119
  title: HOT V5.11｜榴月二十六日晚
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
locks:
- ASKING_FOR_SHIXIAN != FUYUEGE_MEMBER
- UNKNOWN_IDENTITY_REMAINS_LEGAL
```

---

## BYX_TMP_032｜嫪毐

```yaml
route_character_id: BYX_TMP_032
name_or_label: 嫪毐
base_character_ref: null
route_summary: E119 因紅娘固定公開證詞不請自來並付挑戰款；挑戰費不取得成人 access，紅娘未同意成人比較。本人接受初一公開桐木車輪技藝演示，精確規格待定；曾請趙姬／夏蓮作既有經驗名聲證人。
master_event_index:
- event_id: E119
  title: HOT V5.11｜榴月二十六日晚
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
locks:
- CHALLENGE_FEE != ADULT_ACCESS
- WITNESS_TESTIMONY != OBJECTIVE_BODY_COMPARISON
- DEMO_ACCEPTED != DEMO_COMPLETED
```

---

## BYX_TMP_033｜夏蓮／趙姬

```yaml
route_character_id: BYX_TMP_033
name_or_label: 夏蓮／趙姬
base_character_ref: null
route_summary: E119 自主到場；本人承認過去公開歌舞娛樂取利與妓籍，後來王后／太后身份不抹除舊妓籍史。呂不韋叫回舊名「夏蓮」；本人決定下月初一以夏蓮限定成人一夜掛牌。E120 校正為成人床牌／性服務的一夜掛牌；E121 決定持續有效，嬴異人舊關係不預留成交權。
master_event_index:
- event_id: E119
  title: HOT V5.11｜榴月二十六日晚
- event_id: E120
  title: HOT V5.12｜榴月二十六日晚後續～榴月二十七日晚
- event_id: E121
  title: HOT V5.13-R1｜榴月二十七日晚
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
locks:
- PAST_PROSTITUTION_HISTORY != CURRENT_BLANKET_CONSENT
- LISTING_DECISION != WINNER_ESTABLISHED
- OLD_RELATION != RESERVED_ACCESS
```

---

## BYX_TMP_034｜呂不韋

```yaml
route_character_id: BYX_TMP_034
name_or_label: 呂不韋
base_character_ref: null
route_summary: E119 實際入場；重新叫出趙姬舊妓名「夏蓮」，接受初一以商人身份出席商人心法場；只知後世商人故事鉤子，完整故事尚未取得。
master_event_index:
- event_id: E119
  title: HOT V5.11｜榴月二十六日晚
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
locks:
- OLD_HISTORY != CURRENT_ACCESS
- INVITE_ACCEPTED_AS_MERCHANT != ARRIVAL_AT_CHUYI
```

---

## BYX_TMP_035｜老周

```yaml
route_character_id: BYX_TMP_035
name_or_label: 老周
base_character_ref: null
route_summary: E119 汴京紅說書先生之一；對定陶商會「特別採訪證」表示會申請。採訪證只准公開場免費吃喝／記錄，不等於私人席、私談或房間通行。
master_event_index:
- event_id: E119
  title: HOT V5.11｜榴月二十六日晚
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
locks:
- PRESS_PASS_INTENT != PASS_ISSUED
- PRESS_PASS != PRIVATE_ACCESS
```

---

## BYX_TMP_036｜槐生

```yaml
route_character_id: BYX_TMP_036
name_or_label: 槐生
base_character_ref: null
route_summary: E121 沈家未知反應來源之一、可顯影對話來源自選當前稱呼「槐生」。白御行以100兩向觀止／潘金蓮方向成立一日臨時租地並給進白家許可後，槐生可跨先前邊界；到更外側又出現淡化／拉扯。只支持與土地／使用邊界高度相關，不證成靈體機制定律。
master_event_index:
- event_id: E121
  title: HOT V5.13-R1｜榴月二十七日晚
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
locks:
- SOURCE_SELECTED_ALIAS != TRUE_IDENTITY
- BOUNDARY_OBSERVATION != ONTOLOGY
- LEASE_EXPIRY_RESULT_PENDING
```

---

## BYX_TMP_037｜十一哥

```yaml
route_character_id: BYX_TMP_037
name_or_label: 十一哥
base_character_ref: null
route_summary: E121 沈家左牆語音／重擊來源；潘金蓮把同一門做成沈家左牆一端＋觀止正門一面的「兩處一門」接觸口。十一哥自主選擇暫留觀止入口接觸位置，但不承認自己是被養的鬼或正式門房。門／拓撲費金額待結算、白御行擔保；與紅娘官方蛋生意已完成第一個可觀察付費回合。
master_event_index:
- event_id: E121
  title: HOT V5.13-R1｜榴月二十七日晚
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
locks:
- CONTACT_PORT != UNAUTHORIZED_TRAVEL
- STAYING_AT_GATE != EMPLOYMENT
- TRUST_PROPOSAL != SIGNED_ACCOUNT
```

---

## BYX_ANON_005｜沈家寫字來源

```yaml
route_character_id: BYX_ANON_005
name_or_label: 沈家寫字來源
base_character_ref: null
route_summary: 沈家異常來源之一，主要透過窗下敲擊／灰塵／沙盒寫字形成可觀察訊息；E121 明確與槐生、十一哥分開作操作性追蹤。身份、本體、是否獨立個體與可否語音均 UNKNOWN。
master_event_index:
- event_id: E116
  title: HOT V5.8｜榴月二十五日夜
- event_id: E121
  title: HOT V5.13-R1｜榴月二十七日晚
authority: ROUTE_LOCAL_ONLY
promotion_state: NOT_PROMOTED_TO_LCAPG
locks:
- SEPARATE_TRACKING != THREE_DISTINCT_GHOSTS
- WRITING_SOURCE != LEGAL_VOICE_ABILITY
```

---

# 4｜E121 只到邀請／寄信的非 Route Entry 名單

```yaml
PENDING_CONTACTS_NOT_PROMOTED_TO_ROUTE_CHARACTER:
  - name: "白居易"
    source_event: "E121"
    state: "獨立客帖送帖路線啟動；收件／接受／到場 PENDING"
  - name: "關盼盼"
    source_event: "E121"
    state: "獨立客帖送帖路線啟動；收件／接受／到場 PENDING"
  - name: "謝瓊娘"
    source_event: "E121"
    state: "獨立客帖送帖路線啟動；本人是否另選掛牌仍由本人"
  - name: "嬴異人"
    source_event: "E121"
    state: "夏蓮掛牌／秦國舊線方向客帖啟動；收件／接受／到場 PENDING"
  - name: "嬴政"
    source_event: "E120"
    state: "九幽信件已寄出；收件／相信／動身／到場 PENDING"
  - name: "劉邦"
    source_event: "E120"
    state: "九幽信件已寄出；收件／相信／動身／到場 PENDING"
  - name: "忽必烈"
    source_event: "E121"
    state: "白御行只表示要加急寫信；截至 cutoff 尚未實際寫成／送出"
  - name: "呂洞賓"
    source_event: "E121"
    state: "只停留在可能邀請構想；未送帖／未建立路由／未接受"

LOCKS:
  - "INVITATION != RECEIPT"
  - "RECEIPT != ACCEPTANCE"
  - "ACCEPTANCE != ARRIVAL"
  - "LETTER_INTENT != LETTER_SENT"
  - "REFERENCE != ROUTE_ENTRY"
```

---

# 5｜編譯統計與驗證

```yaml
COMPILE_STATS:
  memory_generation: V5.13-R1
  master_event_range: E01-E121
  lcapg_records: 62
  temp_route_records: 42
  route_presence_counts:
    ACTIVE_ROUTE_CHARACTER: 27
    NOT_ESTABLISHED_IN_MASTER_ROUTE: 32
    REFERENCE_ONLY: 3
  relation_lifecycle_counts:
    ACTIVE_CONSTRAINING: 10
    ACTIVE_DORMANT: 17
    NOT_ESTABLISHED: 31
    NOT_ENTERED_ROUTE: 4
  post_master_hot_overlays:
  - V5.14
  - V5.15
  - V5.16
  post_master_hot_count: 3
```

```yaml
VALIDATION:
  master_rcl_generation_match: "PASS / V5.13-R1"
  rcl_schema: "PASS / GUANZHI_RCL_SCHEMA_V1_1"
  lcapg_alignment: "PASS / V3.3.9 / 62 records"
  event_reference_upper_bound: "PASS / no reference later than E121"
  hot_v5_14_plus_forward_contamination: false
  old_rcl_v5_9_mutated: false
  lcapg_base_mutated: false
  unresolved_states_preserved: true
  invite_auto_promoted_to_arrival: false
  relation_auto_promoted_from_adult_event: false
  payment_auto_promoted_to_consent: false
  master_rcl_atomic_pair: "PASS"
```

---

# 6｜Normal Resume 最短句

> **MASTER V5.13-R1-HARD + 本 RCL V5.13-R1 / schema V1.1 為同代基底；再依序疊 HOT V5.14 → V5.15 → V5.16。**
>
> **HOT V5.10–V5.13-R1 已固化進 MASTER E118–E121，只作 provenance／detail fallback，不再作 Normal STORY overlay。**
>
> **舍方知 #62 在本 MASTER cutoff 尚未進白御行線；她的實際 Route Entry 從較新的 HOT V5.14 才開始，禁止倒灌。**
