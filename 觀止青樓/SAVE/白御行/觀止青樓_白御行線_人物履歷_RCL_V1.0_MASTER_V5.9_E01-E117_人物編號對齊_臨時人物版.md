# 觀止青樓｜白御行線人物履歷 RCL V1.0
## 編譯基準：MASTER V5.9-R1-HARD｜E01–E117｜LCAPG V3.3 對齊｜HOT V5.10–V5.12 不吸收

```yaml
DOCUMENT:
  title: "觀止青樓｜白御行線人物履歷"
  short_id: "RCL-BYX"
  version: "V1.0"
  date: "2026-09-10"
  document_type: "COMPILED_ROUTE_CHARACTER_LEDGER"
  status: "GM_AUTHORIZED_MASTER_DERIVED_ROUTE_MEMORY"

ROUTE:
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"

COMPILED_FROM:
  master_file: "觀止青樓_白御行線_MASTER_SAVE_V5.9-R1-HARD_全歷史自足_E01-E117_截至HOT_V5.9固化_保留V5.10-V5.12_HOT版.md"
  master_version: "V5.9-R1-HARD"
  master_sha256: "9f83412526e551ef12f50ecfdfbb36c7cfbd693f4348750d7bb5f53b8bd9f052"
  canonical_event_range: "E01-E117"
  cutoff_event: "E117"
  cutoff_time: "理火三年榴月二十六日上午稍晚"
  lcapg_file: "觀止人物卡池_LCAPG_V3.3_宋蕙蓮李桂姐後台黑暗面_三掌櫃知情_RCL接口_61人正式版.md"
  lcapg_version: "V3.3"
  lcapg_sha256: "16621fd3b587b86fec3a605c207a8c57d51e41ddf069541a83418ae5f127cce8"
  rcl_spec: "RCL V1.0"
  lighter_relation_semantics: "LIHUO LIGHTER V3.5.2-EXP / af42d36a3d29f1c40ed687a088a480caa04ef6d4f499b0b2b52c1c4eff764343"

POST_MASTER_OVERLAY_EXCLUDED_FROM_THIS_COMPILE:
  - "HOT V5.10"
  - "HOT V5.11"
  - "HOT V5.12"

PRECEDENCE:
  - "MASTER event/current hard state > RCL summary"
  - "RCL does not rewrite LCAPG BASE"
  - "HOT after cutoff may change LIVE state but does not alter this V5.9-compiled ledger"
```

> **這不是第二份人物卡。** LCAPG 保存人物 BASE；本檔只保存白御行線截至 MASTER V5.9 的人物履歷索引與當前 Route state。

> **需要知道『為什麼』時，照本檔 E## 回 MASTER。** 本檔不重抄完整故事。

---

# 1｜讀取規則

```text
LCAPG V3.3 BASE
↓
RCL-BYX @ MASTER V5.9
↓
MASTER E## detail when needed
↓
HOT V5.10 → V5.11 → V5.12
↓
CURRENT LIVE STATE
```

固定：

```text
RCL SUMMARY != EVENT BODY
RCL CURRENT STATE != POST-MASTER HOT STATE
EVENT PARTICIPATION != FULL KNOWLEDGE
ADULT EVENT != LOVE
PAYMENT != ACCESS != RELATION != CONSENT
REFERENCE != ARRIVAL
UNKNOWN / PENDING REMAIN LEGAL
```

---

# 2｜LCAPG 61 人對齊履歷

## 01｜CHARACTER_SLOT_1｜潘金蓮

```yaml
BASE_REF:
  unified_order: 1
  lcapg_source_id: "CHARACTER_SLOT_1"
  name: "潘金蓮"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_CONSTRAINING"
  relation_to_player: "觀止大掌櫃／長期營運對手兼合作節點；與白御行已有多次私人成人事件，但未建立戀愛、排他、固定情人或未來永久同意。"
  current_evidence_summary:
    - "E117：榴月二十六日上午自願成人事件成立；潘金蓮拒絕內射，白御行遵守；『今日10/10』只限今日。"
    - "商業／掌櫃／案件線持續具有因果約束。"
  locks:
    - "ADULT_EVENT != LOVE"
    - "TODAY_10_10 != FUTURE_CONSENT"

MASTER_EVENT_INDEX:
  - event_id: "E02"
    title: "第二夜：辭歲包廂拒絕與張麗華初登場"
  - event_id: "E04"
    title: "一萬兩三日懸賞與「無路，無解」"
  - event_id: "E05"
    title: "一萬兩轉為張麗華酒錢"
  - event_id: "E14"
    title: "女兒紅來源與最後一罈競局"
  - event_id: "E26"
    title: "仁宗朝夜談：天章閣、馬吊與歷史會計帳"
  - event_id: "E28"
    title: "傳聞與話本操盤計畫"
  - event_id: "E30"
    title: "第五夜善後與人物去留"
  - event_id: "E34"
    title: "後堂地道出現與趙受益抵達"
  - event_id: "E35"
    title: "紅娘氏第一筆紅倌交易"
  - event_id: "E43"
    title: "紅娘氏與小翠紅綠雙飛組提案"
  - event_id: "E60"
    title: "白玉池封池、蘇清研究與潘金蓮尚未介入之初始狀態"
  - event_id: "E70"
    title: "張麗華酒莊交接與管理入口"
  - event_id: "E82"
    title: "HOT V2.4：風滿樓、西門暗櫃與五千後算"
  - event_id: "E83"
    title: "HOT V2.5：開封法網、阿麗婭重定義與六條來訪"
  - event_id: "E84"
    title: "京師軍械案鏡頭收網、觀止民事戰重啟、許慎言七十二小時按摩券"
  - event_id: "E85"
    title: "潘金蓮返樓、五千原款重分類、五萬索賠、身籍與重新掛牌條件式討論"
  - event_id: "E86"
    title: "潘身籍副冊補證、白玉池許願幣／定存框架、師師道歉修復與如夫人再確認"
  - event_id: "E88"
    title: "女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限"
  - event_id: "E90"
    title: "小翠同床純睡、三月集訓與走秀換約、六百兩候選條款、白宅設計啟動"
  - event_id: "E91"
    title: "浮香自願給床與成人夜、紅娘煙幕揭穿、九幽帝皇聯誼會正式訂單"
  - event_id: "E109"
    title: "HOT V5.1｜榴月十八日晚"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
  - event_id: "E114"
    title: "HOT V5.6【REBUILD-R1】｜榴月二十四日白日"
  - event_id: "E115"
    title: "HOT V5.7｜榴月二十四日夜"
  - event_id: "E116"
    title: "HOT V5.8｜榴月二十五日夜"
  - event_id: "E117"
    title: "HOT V5.9｜榴月二十六日上午"
```

---

## 02｜CHARACTER_SLOT_2｜李瓶兒

```yaml
BASE_REF:
  unified_order: 2
  lcapg_source_id: "CHARACTER_SLOT_2"
  name: "李瓶兒"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_CONSTRAINING"
  relation_to_player: "白家如夫人／女主人位置已於 MASTER cutoff 成立；與白御行有穩定私人成人關係證據，但不等於永久同意。"
  current_evidence_summary:
    - "E105：白家落地後，李師師／李瓶兒平級如夫人空間法位鎖定。"
    - "E110–E111：兩人私人成人夜與翌晨成人事件成立；E111 內射成立，受孕／懷孕 UNKNOWN。"
  locks:
    - "MASTER_V5_9_CUTOFF_STATE_ONLY"
    - "PREGNANCY_UNKNOWN_AT_CUTOFF"

MASTER_EVENT_INDEX:
  - event_id: "E58"
    title: "李瓶兒入池與追求機會未關閉"
  - event_id: "E60"
    title: "白玉池封池、蘇清研究與潘金蓮尚未介入之初始狀態"
  - event_id: "E71"
    title: "觀止餐飲改良但不開平價早餐鋪"
  - event_id: "E72"
    title: "李瓶兒之秘密關係提案未接受"
  - event_id: "E74"
    title: "四人火鍋家宴"
  - event_id: "E75"
    title: "房內兩日「家人」框架"
  - event_id: "E76"
    title: "李瓶兒接受當晚留宿"
  - event_id: "E77"
    title: "寢具用品準備與親密未決"
  - event_id: "E78"
    title: "HOT V2.0：四人夜結與兩日關係分軸"
  - event_id: "E80"
    title: "HOT V2.2：師師如夫人前置、七色肚兜與張麗華獨宿夜"
  - event_id: "E86"
    title: "潘身籍副冊補證、白玉池許願幣／定存框架、師師道歉修復與如夫人再確認"
  - event_id: "E87"
    title: "曹州假印立案、定陶總會架構、京師女性時尚企畫、師師抱睡"
  - event_id: "E95"
    title: "辭歲／錦棠／李瓶兒私人開戶、紅袖五十萬反向價格尺與召喚權、紅娘門窗屏風換債、趙受益六條夜集外出"
  - event_id: "E105"
    title: "HOT V4.7｜榴月十四日晚"
  - event_id: "E110"
    title: "HOT V5.2｜榴月十九日晚"
  - event_id: "E111"
    title: "HOT V5.3｜榴月二十日白日"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
  - event_id: "E115"
    title: "HOT V5.7｜榴月二十四日夜"
```

---

## 03｜CHARACTER_SLOT_3｜龐春梅

```yaml
BASE_REF:
  unified_order: 3
  lcapg_source_id: "CHARACTER_SLOT_3"
  name: "龐春梅"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_CONSTRAINING"
  relation_to_player: "觀止二掌櫃；與白御行主要是營運／管理／事件協作關係，MASTER 未建立私人戀愛或固定成人關係。"
  current_evidence_summary:
    - "掌櫃權限與後台／現場管理持續有效。"
  locks:
    - "SHOPKEEPER_ROLE != PRIVATE_RELATION"

MASTER_EVENT_INDEX:
  - event_id: "E62"
    title: "張麗華花燭當日確認與時辰"
  - event_id: "E64"
    title: "時空道人承認漏籤"
  - event_id: "E111"
    title: "HOT V5.3｜榴月二十日白日"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
```

---

## 04｜FLOWER_QUEEN_CORE_1｜蘇清

```yaml
BASE_REF:
  unified_order: 4
  lcapg_source_id: "FLOWER_QUEEN_CORE_1"
  name: "蘇清"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_CONSTRAINING"
  relation_to_player: "長期複合關係：曾有付費契約與成人事件，後有二十八日私人盟約、商會工作與牛郎店合作方向；未固化為固定情人／婚姻。"
  current_evidence_summary:
    - "E115：與白御行、醉花完成自願三人成人事件；蘇清當次明示接受內射，懷孕 UNKNOWN。"
    - "E116：牛郎店／男性陪侍投資合作方向成立，店址、資本、股權、契約未落地。"
  locks:
    - "CONTRACT != LOVE"
    - "PARTNERSHIP_DIRECTION != FINAL_CONTRACT"

MASTER_EVENT_INDEX:
  - event_id: "E04"
    title: "一萬兩三日懸賞與「無路，無解」"
  - event_id: "E06"
    title: "蘇清五百兩三晚交易：事實修正版"
  - event_id: "E21"
    title: "顧北辰霸總劇：巴掌、白月光與豬隊友"
  - event_id: "E23"
    title: "無名信與白玉池美女事件"
  - event_id: "E28"
    title: "傳聞與話本操盤計畫"
  - event_id: "E59"
    title: "白玉池「歸零」、算式與續字回顯"
  - event_id: "E60"
    title: "白玉池封池、蘇清研究與潘金蓮尚未介入之初始狀態"
  - event_id: "E65"
    title: "活物與事件傳遞測試"
  - event_id: "E68"
    title: "商會授權與蘇清、小翠浴房邊界"
  - event_id: "E74"
    title: "四人火鍋家宴"
  - event_id: "E75"
    title: "房內兩日「家人」框架"
  - event_id: "E76"
    title: "李瓶兒接受當晚留宿"
  - event_id: "E77"
    title: "寢具用品準備與親密未決"
  - event_id: "E78"
    title: "HOT V2.0：四人夜結與兩日關係分軸"
  - event_id: "E79"
    title: "HOT V2.1：定陶商戰、蘇清私約與白玉池補固"
  - event_id: "E80"
    title: "HOT V2.2：師師如夫人前置、七色肚兜與張麗華獨宿夜"
  - event_id: "E81"
    title: "HOT V2.3：定陶—沈萬三合作與多線案件升級"
  - event_id: "E82"
    title: "HOT V2.4：風滿樓、西門暗櫃與五千後算"
  - event_id: "E83"
    title: "HOT V2.5：開封法網、阿麗婭重定義與六條來訪"
  - event_id: "E84"
    title: "京師軍械案鏡頭收網、觀止民事戰重啟、許慎言七十二小時按摩券"
  - event_id: "E85"
    title: "潘金蓮返樓、五千原款重分類、五萬索賠、身籍與重新掛牌條件式討論"
  - event_id: "E88"
    title: "女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限"
  - event_id: "E103"
    title: "榴月十二日晚白家採購規劃、蘇清十八日商會工拆帳、妓籍終身法位鎖、阿莉婭處女拍賣標的與紅娘雙人場、三十二娘妓籍申請、楊玉環白玉池代言首夜、黑公子×小桃百兩交易與同宿意向"
  - event_id: "E104"
    title: "HOT V4.6｜榴月十三日晚"
  - event_id: "E110"
    title: "HOT V5.2｜榴月十九日晚"
  - event_id: "E114"
    title: "HOT V5.6【REBUILD-R1】｜榴月二十四日白日"
  - event_id: "E115"
    title: "HOT V5.7｜榴月二十四日夜"
  - event_id: "E116"
    title: "HOT V5.8｜榴月二十五日夜"
  - event_id: "E117"
    title: "HOT V5.9｜榴月二十六日上午"
```

---

## 05｜FLOWER_QUEEN_CORE_2｜阿麗婭

```yaml
BASE_REF:
  unified_order: 5
  lcapg_source_id: "FLOWER_QUEEN_CORE_2"
  name: "阿麗婭"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_DORMANT"
  relation_to_player: "觀止人物／舊案與掛牌權利相關節點；MASTER 未建立白御行私人戀愛或成人關係。"
  current_evidence_summary:
    - "E83：保留自己決定第一次實際出閣／第一個男人的權利。"
  locks:
    - "MARKET_RIGHT != PLAYER_ACCESS"

MASTER_EVENT_INDEX:
  - event_id: "E82"
    title: "HOT V2.4：風滿樓、西門暗櫃與五千後算"
  - event_id: "E83"
    title: "HOT V2.5：開封法網、阿麗婭重定義與六條來訪"
  - event_id: "E103"
    title: "榴月十二日晚白家採購規劃、蘇清十八日商會工拆帳、妓籍終身法位鎖、阿莉婭處女拍賣標的與紅娘雙人場、三十二娘妓籍申請、楊玉環白玉池代言首夜、黑公子×小桃百兩交易與同宿意向"
```

---

## 06｜CHARACTER_SLOT_4｜張麗華

```yaml
BASE_REF:
  unified_order: 6
  lcapg_source_id: "CHARACTER_SLOT_4"
  name: "張麗華"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_CONSTRAINING"
  relation_to_player: "E55 明示接受白御行情人關係；有互相喜歡與私人成人歷史；至 MASTER V5.9 已有白家外院／私人空間與酒莊商業線。"
  current_evidence_summary:
    - "E55：情人關係成立。"
    - "E80：互相明示喜歡並有私人成人夜。"
    - "E105：白家落地，麗華外院空間法位鎖定。"
    - "E117：酒莊列為初一全日優先供酒採購方向。"
  locks:
    - "NO_MARRIAGE_DEED_AT_E55"
    - "HOT_V5_12_LATER_CORRECTIONS_NOT_BACKFILLED"

MASTER_EVENT_INDEX:
  - event_id: "E02"
    title: "第二夜：辭歲包廂拒絕與張麗華初登場"
  - event_id: "E03"
    title: "張麗華第一次婚約：五千、一萬五千與一萬訂金"
  - event_id: "E04"
    title: "一萬兩三日懸賞與「無路，無解」"
  - event_id: "E05"
    title: "一萬兩轉為張麗華酒錢"
  - event_id: "E07"
    title: "第五夜開場：張麗華、酒與子時條件"
  - event_id: "E13"
    title: "三十年女兒紅、《不得飲》與公開官人稱呼"
  - event_id: "E14"
    title: "女兒紅來源與最後一罈競局"
  - event_id: "E16"
    title: "歪詩局與《玉樹後庭花》補句"
  - event_id: "E17"
    title: "酒莊、薔薇、三烤鹽與定陶商會婚議升級"
  - event_id: "E18"
    title: "陳叔寶、地府與張麗華去留爭論"
  - event_id: "E21"
    title: "顧北辰霸總劇：巴掌、白月光與豬隊友"
  - event_id: "E26"
    title: "仁宗朝夜談：天章閣、馬吊與歷史會計帳"
  - event_id: "E27"
    title: "假醉進張麗華房間與私人關係提案"
  - event_id: "E28"
    title: "傳聞與話本操盤計畫"
  - event_id: "E29"
    title: "自由意志、選擇環境與時間窗口爭論"
  - event_id: "E31"
    title: "張麗華穿衣陪睡完成"
  - event_id: "E55"
    title: "張麗華明示接受情人關係"
  - event_id: "E56"
    title: "李師師嫉妒、私人稱呼與槐月十五日晚共處"
  - event_id: "E62"
    title: "張麗華花燭當日確認與時辰"
  - event_id: "E70"
    title: "張麗華酒莊交接與管理入口"
  - event_id: "E71"
    title: "觀止餐飲改良但不開平價早餐鋪"
  - event_id: "E73"
    title: "張麗華三日陪伴線"
  - event_id: "E74"
    title: "四人火鍋家宴"
  - event_id: "E75"
    title: "房內兩日「家人」框架"
  - event_id: "E76"
    title: "李瓶兒接受當晚留宿"
  - event_id: "E77"
    title: "寢具用品準備與親密未決"
  - event_id: "E78"
    title: "HOT V2.0：四人夜結與兩日關係分軸"
  - event_id: "E79"
    title: "HOT V2.1：定陶商戰、蘇清私約與白玉池補固"
  - event_id: "E80"
    title: "HOT V2.2：師師如夫人前置、七色肚兜與張麗華獨宿夜"
  - event_id: "E88"
    title: "女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限"
  - event_id: "E90"
    title: "小翠同床純睡、三月集訓與走秀換約、六百兩候選條款、白宅設計啟動"
  - event_id: "E105"
    title: "HOT V4.7｜榴月十四日晚"
  - event_id: "E108"
    title: "HOT V5.0｜榴月十六日下午"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
  - event_id: "E117"
    title: "HOT V5.9｜榴月二十六日上午"
```

---

## 07｜CHARACTER_SLOT_5｜宋蕙蓮

```yaml
BASE_REF:
  unified_order: 7
  lcapg_source_id: "CHARACTER_SLOT_5"
  name: "宋蕙蓮"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 08｜CHARACTER_SLOT_6｜李桂姐

```yaml
BASE_REF:
  unified_order: 8
  lcapg_source_id: "CHARACTER_SLOT_6"
  name: "李桂姐"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 09｜CHARACTER_SLOT_7｜紅袖

```yaml
BASE_REF:
  unified_order: 9
  lcapg_source_id: "CHARACTER_SLOT_7"
  name: "紅袖"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_DORMANT"
  relation_to_player: "觀止人物；與白御行有多次互動、曾有成人適應／三日賭約線，但至 E109 已收束；MASTER 未建立固定私人關係。"
  current_evidence_summary:
    - "E109：紅袖／浮香三日賭約在期限前收束。"
    - "E114：對失仙的觀察只屬紅袖自己的私下分析。"
  locks:
    - "RESOLVED_WAGER != RELATIONSHIP"

MASTER_EVENT_INDEX:
  - event_id: "E12"
    title: "似伊影像與紅袖可能未來"
  - event_id: "E24"
    title: "似伊實體入場與退場"
  - event_id: "E25"
    title: "白御行給紅袖的建議與如夫人邀請"
  - event_id: "E95"
    title: "辭歲／錦棠／李瓶兒私人開戶、紅袖五十萬反向價格尺與召喚權、紅娘門窗屏風換債、趙受益六條夜集外出"
  - event_id: "E104"
    title: "HOT V4.6｜榴月十三日晚"
  - event_id: "E109"
    title: "HOT V5.1｜榴月十八日晚"
  - event_id: "E114"
    title: "HOT V5.6【REBUILD-R1】｜榴月二十四日白日"
```

---

## 10｜CHARACTER_SLOT_8｜疏影

```yaml
BASE_REF:
  unified_order: 10
  lcapg_source_id: "CHARACTER_SLOT_8"
  name: "疏影"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_DORMANT"
  relation_to_player: "觀止人物／觀察與評估節點；MASTER 未建立白御行私人關係。"
  current_evidence_summary:
    - "E114：是否正在觀察失仙、看見什麼保持 UNKNOWN。"
  locks:
    - "OBSERVATION_POSSIBILITY != KNOWLEDGE"

MASTER_EVENT_INDEX:
  - event_id: "E88"
    title: "女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限"
  - event_id: "E114"
    title: "HOT V5.6【REBUILD-R1】｜榴月二十四日白日"
```

---

## 11｜CHARACTER_SLOT_9｜醉花

```yaml
BASE_REF:
  unified_order: 11
  lcapg_source_id: "CHARACTER_SLOT_9"
  name: "醉花"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_DORMANT"
  relation_to_player: "與白御行有既往親近與成人事件；E113 明示未來兩人單獨仍『有』可能，但沒有日期、承諾或固定情人名位。"
  current_evidence_summary:
    - "E113：未來單獨成人關係仍有可能。"
    - "E115：與白御行、蘇清完成自願三人成人事件；不建立戀愛／永久同意。"
  locks:
    - "INTEREST != COMMITMENT"
    - "ADULT_EVENT != FIXED_LOVER"

MASTER_EVENT_INDEX:
  - event_id: "E13"
    title: "三十年女兒紅、《不得飲》與公開官人稱呼"
  - event_id: "E16"
    title: "歪詩局與《玉樹後庭花》補句"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
  - event_id: "E115"
    title: "HOT V5.7｜榴月二十四日夜"
  - event_id: "E116"
    title: "HOT V5.8｜榴月二十五日夜"
  - event_id: "E117"
    title: "HOT V5.9｜榴月二十六日上午"
```

---

## 12｜CHARACTER_SLOT_10｜十三娘

```yaml
BASE_REF:
  unified_order: 12
  lcapg_source_id: "CHARACTER_SLOT_10"
  name: "十三娘"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_DORMANT"
  relation_to_player: "賭局／社交節點；白御行曾交付國運／幸運路徑情報，未建立私人戀愛關係。"
  current_evidence_summary:
    - "E92：豹子賭局白御行敗，依約交付國運／估價／首飾儲存等情報。"
  locks:
    - "GAMBLING_RELATION != PRIVATE_RELATION"

MASTER_EVENT_INDEX:
  - event_id: "E07"
    title: "第五夜開場：張麗華、酒與子時條件"
  - event_id: "E10"
    title: "十三娘問心賭局"
  - event_id: "E92"
    title: "帝皇宴前置、十三娘國運賭桌線、兩局免費床結算、紅娘側賭敗、小翠三娘實習與三人抱睡"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
```

---

## 13｜CHARACTER_SLOT_11｜白三娘

```yaml
BASE_REF:
  unified_order: 13
  lcapg_source_id: "CHARACTER_SLOT_11"
  name: "白三娘"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_DORMANT"
  relation_to_player: "觀止資深人物；與白御行有成年人親密歷史，但 MASTER 未建立固定情人／婚姻。"
  current_evidence_summary:
    - "E92：白三娘與白御行成人事件成立；其後三人抱睡收束。"
  locks:
    - "PAST_ADULT_EVENT != CURRENT_CONSENT"

MASTER_EVENT_INDEX:
  - event_id: "E07"
    title: "第五夜開場：張麗華、酒與子時條件"
  - event_id: "E10"
    title: "十三娘問心賭局"
  - event_id: "E42"
    title: "白三娘老帶新方案接受"
  - event_id: "E88"
    title: "女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限"
  - event_id: "E92"
    title: "帝皇宴前置、十三娘國運賭桌線、兩局免費床結算、紅娘側賭敗、小翠三娘實習與三人抱睡"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
```

---

## 14｜CHARACTER_SLOT_12｜浮香

```yaml
BASE_REF:
  unified_order: 14
  lcapg_source_id: "CHARACTER_SLOT_12"
  name: "浮香"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_DORMANT"
  relation_to_player: "與白御行有自願成人夜與持續親近證據；E105 白家外院空間法位已鎖定，但 MASTER V5.9 尚未以後來 HOT 的『情人身份』校正回填。"
  current_evidence_summary:
    - "E91：浮香自主讓白御行留床，其後另有雙方成人事件。"
    - "E105：白家外院空間法位鎖定。"
    - "E109：三日賭約收束。"
  locks:
    - "MASTER_CUTOFF_ONLY"
    - "HOT_V5_12_LOVER_LABEL_EXCLUDED"

MASTER_EVENT_INDEX:
  - event_id: "E01"
    title: "第一夜：無名客入觀止、辭歲與浮香"
  - event_id: "E09"
    title: "浮香第五夜：琴、琴坊與雙向排他"
  - event_id: "E11"
    title: "白御行家眷與三名正式妻子公開"
  - event_id: "E91"
    title: "浮香自願給床與成人夜、紅娘煙幕揭穿、九幽帝皇聯誼會正式訂單"
  - event_id: "E92"
    title: "帝皇宴前置、十三娘國運賭桌線、兩局免費床結算、紅娘側賭敗、小翠三娘實習與三人抱睡"
  - event_id: "E104"
    title: "HOT V4.6｜榴月十三日晚"
  - event_id: "E105"
    title: "HOT V4.7｜榴月十四日晚"
  - event_id: "E109"
    title: "HOT V5.1｜榴月十八日晚"
  - event_id: "E110"
    title: "HOT V5.2｜榴月十九日晚"
  - event_id: "E111"
    title: "HOT V5.3｜榴月二十日白日"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
  - event_id: "E115"
    title: "HOT V5.7｜榴月二十四日夜"
```

> Cutoff 注意：浮香後來在 HOT V5.12 被玩家校正為白家情人身份；本版只保存 MASTER V5.9 已成立的成人歷史與白家外院空間，不提前吃入該 HOT。

---

## 15｜CHARACTER_SLOT_13｜小翠

```yaml
BASE_REF:
  unified_order: 15
  lcapg_source_id: "CHARACTER_SLOT_13"
  name: "小翠"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_DORMANT"
  relation_to_player: "白御行與小翠有多次床位／訓練／有限成人互動歷史；無固定戀愛、所有權或未來 blanket consent。"
  current_evidence_summary:
    - "E90：同床純睡，邊界明確。"
    - "E92：小翠自願進入有限實習／觀察並自行停止。"
  locks:
    - "TRAINING != AVAILABILITY"
    - "PAST_LIMITED_INTIMACY != FUTURE_CONSENT"

MASTER_EVENT_INDEX:
  - event_id: "E37"
    title: "小翠拒絕八百兩安排"
  - event_id: "E41"
    title: "小翠熟客安全計畫提出"
  - event_id: "E42"
    title: "白三娘老帶新方案接受"
  - event_id: "E43"
    title: "紅娘氏與小翠紅綠雙飛組提案"
  - event_id: "E45"
    title: "深夜休息節點"
  - event_id: "E68"
    title: "商會授權與蘇清、小翠浴房邊界"
  - event_id: "E90"
    title: "小翠同床純睡、三月集訓與走秀換約、六百兩候選條款、白宅設計啟動"
  - event_id: "E92"
    title: "帝皇宴前置、十三娘國運賭桌線、兩局免費床結算、紅娘側賭敗、小翠三娘實習與三人抱睡"
  - event_id: "E101"
    title: "榴月十日開幕前夕、辭歲五百萬五年五分定存、師師月事未至孕否未知、商會女人培訓目的鎖、小翠首次完整成人事件、三人同睡收尾"
```

---

## 16｜NATIVE_08｜李媽媽

```yaml
BASE_REF:
  unified_order: 16
  lcapg_source_id: "NATIVE_08"
  name: "李媽媽"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 17｜NATIVE_09｜安舟

```yaml
BASE_REF:
  unified_order: 17
  lcapg_source_id: "NATIVE_09"
  name: "安舟"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 18｜NATIVE_10｜汪鹽商

```yaml
BASE_REF:
  unified_order: 18
  lcapg_source_id: "NATIVE_10"
  name: "汪鹽商"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 19｜CHARACTER_SLOT_14｜辭歲

```yaml
BASE_REF:
  unified_order: 19
  lcapg_source_id: "CHARACTER_SLOT_14"
  name: "辭歲"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_DORMANT"
  relation_to_player: "高價／資產／觀止經營相關重要人物；與白御行有長期注意與交易歷史，但 MASTER 未建立固定私人戀愛。"
  current_evidence_summary:
    - "E93/E95/E101/E102 等形成資產、帳戶、活動與觀止路線。"
  locks:
    - "MONEY != RELATION"

MASTER_EVENT_INDEX:
  - event_id: "E01"
    title: "第一夜：無名客入觀止、辭歲與浮香"
  - event_id: "E02"
    title: "第二夜：辭歲包廂拒絕與張麗華初登場"
  - event_id: "E08"
    title: "辭歲二十八日心理奴化提案被拒"
  - event_id: "E89"
    title: "風滿樓第二日遴選、十一名候選分流、牙行責任、白宅十年條件式協議"
  - event_id: "E93"
    title: "九幽帝皇聯誼會散場、辭歲／錦棠雙姝天價競拍、白玉池帝皇團特殊試營運、帝皇多線自然分流"
  - event_id: "E95"
    title: "辭歲／錦棠／李瓶兒私人開戶、紅袖五十萬反向價格尺與召喚權、紅娘門窗屏風換債、趙受益六條夜集外出"
  - event_id: "E101"
    title: "榴月十日開幕前夕、辭歲五百萬五年五分定存、師師月事未至孕否未知、商會女人培訓目的鎖、小翠首次完整成人事件、三人同睡收尾"
  - event_id: "E102"
    title: "榴月十一日晚重新開幕完成、女子競技與紅娘壓軸、顧三辭歲再會、趙受益二百兩購四契再贈六條／楊玉環、四大金剛＋李清照女客試場、白玉池會員制接受、錦棠同宿"
```

---

## 20｜CHARACTER_SLOT_15｜貂蟬

```yaml
BASE_REF:
  unified_order: 20
  lcapg_source_id: "CHARACTER_SLOT_15"
  name: "貂蟬"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 21｜POOL_CHARACTER_001｜紅娘氏

```yaml
BASE_REF:
  unified_order: 21
  lcapg_source_id: "POOL_CHARACTER_001"
  name: "紅娘氏"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_CONSTRAINING"
  relation_to_player: "長期營業、情報、成人事件與互坑賭約交疊的複合關係；目前鐵籠、九日競賽與洗浴募款等未決狀態仍直接約束後續。"
  current_evidence_summary:
    - "E108：白御行×紅娘成人場成立，並成立六條十日賭約。"
    - "E112：新加碼賭成立，真條件保密。"
    - "E113：紅娘已在大堂鐵籠公開生活／營業；九日營收競賽與不水浴募款持續。"
    - "E116：52兩單句表演與500兩終身固定答詞背書成立。"
  locks:
    - "WAGER != THIRD_PARTY_CONSENT"
    - "PUBLIC_CAGE != TOUCH_ACCESS"
    - "NO_ROMANCE_INFERRED"

MASTER_EVENT_INDEX:
  - event_id: "E34"
    title: "後堂地道出現與趙受益抵達"
  - event_id: "E35"
    title: "紅娘氏第一筆紅倌交易"
  - event_id: "E40"
    title: "白御行向紅娘氏購買情報"
  - event_id: "E43"
    title: "紅娘氏與小翠紅綠雙飛組提案"
  - event_id: "E48"
    title: "錯過再會、十二香皂與新招數欠帳"
  - event_id: "E91"
    title: "浮香自願給床與成人夜、紅娘煙幕揭穿、九幽帝皇聯誼會正式訂單"
  - event_id: "E92"
    title: "帝皇宴前置、十三娘國運賭桌線、兩局免費床結算、紅娘側賭敗、小翠三娘實習與三人抱睡"
  - event_id: "E95"
    title: "辭歲／錦棠／李瓶兒私人開戶、紅袖五十萬反向價格尺與召喚權、紅娘門窗屏風換債、趙受益六條夜集外出"
  - event_id: "E98"
    title: "三十二娘街行與帳戶指令、紅娘中央籠台演出方案、錦棠首次正式約會、私人成人事件、白御行喜歡明示與相擁收幕"
  - event_id: "E102"
    title: "榴月十一日晚重新開幕完成、女子競技與紅娘壓軸、顧三辭歲再會、趙受益二百兩購四契再贈六條／楊玉環、四大金剛＋李清照女客試場、白玉池會員制接受、錦棠同宿"
  - event_id: "E103"
    title: "榴月十二日晚白家採購規劃、蘇清十八日商會工拆帳、妓籍終身法位鎖、阿莉婭處女拍賣標的與紅娘雙人場、三十二娘妓籍申請、楊玉環白玉池代言首夜、黑公子×小桃百兩交易與同宿意向"
  - event_id: "E108"
    title: "HOT V5.0｜榴月十六日下午"
  - event_id: "E111"
    title: "HOT V5.3｜榴月二十日白日"
  - event_id: "E112"
    title: "HOT V5.4｜榴月二十日白日"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
  - event_id: "E114"
    title: "HOT V5.6【REBUILD-R1】｜榴月二十四日白日"
  - event_id: "E116"
    title: "HOT V5.8｜榴月二十五日夜"
  - event_id: "E117"
    title: "HOT V5.9｜榴月二十六日上午"
```

---

## 22｜POOL_CHARACTER_002｜李師師

```yaml
BASE_REF:
  unified_order: 22
  lcapg_source_id: "POOL_CHARACTER_002"
  name: "李師師"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_CONSTRAINING"
  relation_to_player: "白家如夫人位置與長期私人親密關係成立；保留觀止設席、房門與職業自主。MASTER cutoff 孕況為疑似升高但未確診。"
  current_evidence_summary:
    - "E80/E86：如夫人位置意向與再確認逐步形成。"
    - "E105：白家落地後與李瓶兒平級如夫人空間法位鎖定。"
    - "E109：疑似有喜再升高，仍未確診。"
  locks:
    - "SUSPECTED != CONFIRMED"
    - "MASTER_V5_9_DOES_NOT_BACKFILL_HOT_V5_12_FIRST_RU_FUREN_CORRECTION"

MASTER_EVENT_INDEX:
  - event_id: "E20"
    title: "柳如煙概念體、李師師與趙受益花魁局"
  - event_id: "E22"
    title: "顧家豪門宴戲"
  - event_id: "E26"
    title: "仁宗朝夜談：天章閣、馬吊與歷史會計帳"
  - event_id: "E30"
    title: "第五夜善後與人物去留"
  - event_id: "E33"
    title: "李師師選擇留在觀止並採設席牌"
  - event_id: "E34"
    title: "後堂地道出現與趙受益抵達"
  - event_id: "E35"
    title: "紅娘氏第一筆紅倌交易"
  - event_id: "E38"
    title: "李師師與師理理身份規則確認"
  - event_id: "E39"
    title: "師理理開放白御行追求可能"
  - event_id: "E40"
    title: "白御行向紅娘氏購買情報"
  - event_id: "E45"
    title: "深夜休息節點"
  - event_id: "E46"
    title: "李師師／師理理第一次完整性交"
  - event_id: "E47"
    title: "疼痛界線、事後停留與私人記憶"
  - event_id: "E48"
    title: "錯過再會、十二香皂與新招數欠帳"
  - event_id: "E56"
    title: "李師師嫉妒、私人稱呼與槐月十五日晚共處"
  - event_id: "E58"
    title: "李瓶兒入池與追求機會未關閉"
  - event_id: "E61"
    title: "李師師共宿、停止權校正與清晨射精"
  - event_id: "E62"
    title: "張麗華花燭當日確認與時辰"
  - event_id: "E69"
    title: "花燭前休息"
  - event_id: "E73"
    title: "張麗華三日陪伴線"
  - event_id: "E80"
    title: "HOT V2.2：師師如夫人前置、七色肚兜與張麗華獨宿夜"
  - event_id: "E81"
    title: "HOT V2.3：定陶—沈萬三合作與多線案件升級"
  - event_id: "E83"
    title: "HOT V2.5：開封法網、阿麗婭重定義與六條來訪"
  - event_id: "E86"
    title: "潘身籍副冊補證、白玉池許願幣／定存框架、師師道歉修復與如夫人再確認"
  - event_id: "E87"
    title: "曹州假印立案、定陶總會架構、京師女性時尚企畫、師師抱睡"
  - event_id: "E88"
    title: "女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限"
  - event_id: "E90"
    title: "小翠同床純睡、三月集訓與走秀換約、六百兩候選條款、白宅設計啟動"
  - event_id: "E92"
    title: "帝皇宴前置、十三娘國運賭桌線、兩局免費床結算、紅娘側賭敗、小翠三娘實習與三人抱睡"
  - event_id: "E96"
    title: "趙受益六條夜集返樓、楊玉環白玉池與荔枝、李師師晨間補考、定陶票據信用／朱明長債方向／曹州案盤點"
  - event_id: "E101"
    title: "榴月十日開幕前夕、辭歲五百萬五年五分定存、師師月事未至孕否未知、商會女人培訓目的鎖、小翠首次完整成人事件、三人同睡收尾"
  - event_id: "E105"
    title: "HOT V4.7｜榴月十四日晚"
  - event_id: "E109"
    title: "HOT V5.1｜榴月十八日晚"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
  - event_id: "E115"
    title: "HOT V5.7｜榴月二十四日夜"
  - event_id: "E117"
    title: "HOT V5.9｜榴月二十六日上午"
```

> Cutoff 注意：HOT V5.12 後來對李師師「最早進門／首席如夫人」作了更精確的玩家線校正；**本版 RCL 固定在 MASTER V5.9 cutoff，不倒灌該較新 HOT 校正。**

---

## 23｜SUPPLEMENTAL_CHARACTER_003｜青禾

```yaml
BASE_REF:
  unified_order: 23
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_003"
  name: "青禾"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_DORMANT"
  relation_to_player: "按摩／恢復服務節點；MASTER 未建立白御行私人關係。"
  current_evidence_summary:
    - "E84：青禾開始向許慎言提供分次扣時按摩／恢復服務。"
  locks:
    - "SERVICE != PRIVATE_RELATION"

MASTER_EVENT_INDEX:
  - event_id: "E84"
    title: "京師軍械案鏡頭收網、觀止民事戰重啟、許慎言七十二小時按摩券"
```

---

## 24｜SUPPLEMENTAL_CHARACTER_004｜六條御息所

```yaml
BASE_REF:
  unified_order: 24
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_004"
  name: "六條御息所"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_DORMANT"
  relation_to_player: "異時女客與白御行已有自願成人事件；未建立愛、婚姻、所有權、排他或固定情人契約。"
  current_evidence_summary:
    - "E111：首次雙方自願成人性交事件，兩次內射；受孕／懷孕 UNKNOWN。"
    - "E112：未對未來三人成人事件給出可鎖定明確同意。"
  locks:
    - "PAST_ADULT_EVENT != FUTURE_CONSENT"
    - "PREGNANCY_UNKNOWN"

MASTER_EVENT_INDEX:
  - event_id: "E83"
    title: "HOT V2.5：開封法網、阿麗婭重定義與六條來訪"
  - event_id: "E94"
    title: "榴月一日十日整修起點、雙姝款項／身份翻轉、朱明欠單與鄭成功週轉僅預案、六條／趙受益成人結果與污染校正"
  - event_id: "E95"
    title: "辭歲／錦棠／李瓶兒私人開戶、紅袖五十萬反向價格尺與召喚權、紅娘門窗屏風換債、趙受益六條夜集外出"
  - event_id: "E96"
    title: "趙受益六條夜集返樓、楊玉環白玉池與荔枝、李師師晨間補考、定陶票據信用／朱明長債方向／曹州案盤點"
  - event_id: "E97"
    title: "長恨歌文會、柳如是東林夜談、趙受益宣和地道入席、六條／楊玉環雙線追求與三人約會可能性"
  - event_id: "E102"
    title: "榴月十一日晚重新開幕完成、女子競技與紅娘壓軸、顧三辭歲再會、趙受益二百兩購四契再贈六條／楊玉環、四大金剛＋李清照女客試場、白玉池會員制接受、錦棠同宿"
  - event_id: "E108"
    title: "HOT V5.0｜榴月十六日下午"
  - event_id: "E109"
    title: "HOT V5.1｜榴月十八日晚"
  - event_id: "E111"
    title: "HOT V5.3｜榴月二十日白日"
  - event_id: "E112"
    title: "HOT V5.4｜榴月二十日白日"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
  - event_id: "E114"
    title: "HOT V5.6【REBUILD-R1】｜榴月二十四日白日"
```

---

## 25｜SUPPLEMENTAL_CHARACTER_005｜李清照

```yaml
BASE_REF:
  unified_order: 25
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_005"
  name: "李清照"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_DORMANT"
  relation_to_player: "文藝／社交熟人節點；沒有白御行私人戀愛或成人關係。"
  current_evidence_summary:
    - "E113：雙籠事件中到場，對白御行挪用其詞作梗作出反應。"
  locks:
    - "LITERARY_SOCIAL != PRIVATE_RELATION"

MASTER_EVENT_INDEX:
  - event_id: "E11"
    title: "白御行家眷與三名正式妻子公開"
  - event_id: "E13"
    title: "三十年女兒紅、《不得飲》與公開官人稱呼"
  - event_id: "E15"
    title: "李清照《一剪梅》與白御行四言長詩"
  - event_id: "E16"
    title: "歪詩局與《玉樹後庭花》補句"
  - event_id: "E26"
    title: "仁宗朝夜談：天章閣、馬吊與歷史會計帳"
  - event_id: "E30"
    title: "第五夜善後與人物去留"
  - event_id: "E32"
    title: "李清照返回自身時代"
  - event_id: "E102"
    title: "榴月十一日晚重新開幕完成、女子競技與紅娘壓軸、顧三辭歲再會、趙受益二百兩購四契再贈六條／楊玉環、四大金剛＋李清照女客試場、白玉池會員制接受、錦棠同宿"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
```

---

## 26｜SUPPLEMENTAL_CHARACTER_006｜趙受益

```yaml
BASE_REF:
  unified_order: 26
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_006"
  name: "趙受益"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_DORMANT"
  relation_to_player: "皇帝／常客／白玉池與觀止社交節點；有付費與事件往來，但沒有白御行私人戀愛關係。"
  current_evidence_summary:
    - "E114：與六條進白玉池線；柳永與趙受益『奉旨填詞』伏筆持續。"
  locks:
    - "PAYMENT != ACCESS"
    - "IMPERIAL_STATUS != VENUE_SOVEREIGNTY"

MASTER_EVENT_INDEX:
  - event_id: "E19"
    title: "宋仁宗評價、權力限制與觀止理念"
  - event_id: "E20"
    title: "柳如煙概念體、李師師與趙受益花魁局"
  - event_id: "E22"
    title: "顧家豪門宴戲"
  - event_id: "E26"
    title: "仁宗朝夜談：天章閣、馬吊與歷史會計帳"
  - event_id: "E30"
    title: "第五夜善後與人物去留"
  - event_id: "E34"
    title: "後堂地道出現與趙受益抵達"
  - event_id: "E35"
    title: "紅娘氏第一筆紅倌交易"
  - event_id: "E82"
    title: "HOT V2.4：風滿樓、西門暗櫃與五千後算"
  - event_id: "E83"
    title: "HOT V2.5：開封法網、阿麗婭重定義與六條來訪"
  - event_id: "E94"
    title: "榴月一日十日整修起點、雙姝款項／身份翻轉、朱明欠單與鄭成功週轉僅預案、六條／趙受益成人結果與污染校正"
  - event_id: "E95"
    title: "辭歲／錦棠／李瓶兒私人開戶、紅袖五十萬反向價格尺與召喚權、紅娘門窗屏風換債、趙受益六條夜集外出"
  - event_id: "E96"
    title: "趙受益六條夜集返樓、楊玉環白玉池與荔枝、李師師晨間補考、定陶票據信用／朱明長債方向／曹州案盤點"
  - event_id: "E97"
    title: "長恨歌文會、柳如是東林夜談、趙受益宣和地道入席、六條／楊玉環雙線追求與三人約會可能性"
  - event_id: "E102"
    title: "榴月十一日晚重新開幕完成、女子競技與紅娘壓軸、顧三辭歲再會、趙受益二百兩購四契再贈六條／楊玉環、四大金剛＋李清照女客試場、白玉池會員制接受、錦棠同宿"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
  - event_id: "E114"
    title: "HOT V5.6【REBUILD-R1】｜榴月二十四日白日"
```

---

## 27｜SUPPLEMENTAL_CHARACTER_007｜錦棠／周玉娘

```yaml
BASE_REF:
  unified_order: 27
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_007"
  name: "錦棠／周玉娘"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_CONSTRAINING"
  relation_to_player: "與白御行已有正式約會、私人成人事件與喜歡明示；同時是商會明星／主代言方向的重要商業人物，最終經紀約仍 PENDING。"
  current_evidence_summary:
    - "E98：首次正式約會、私人成人事件、白御行喜歡明示與相擁收幕。"
    - "E117：核心主秀／主代言方向；最終演藝經紀約 PENDING。"
  locks:
    - "PRIVATE_RELATION != COMMERCIAL_CONTRACT"
    - "DIRECTION != SIGNED_CONTRACT"

MASTER_EVENT_INDEX:
  - event_id: "E93"
    title: "九幽帝皇聯誼會散場、辭歲／錦棠雙姝天價競拍、白玉池帝皇團特殊試營運、帝皇多線自然分流"
  - event_id: "E95"
    title: "辭歲／錦棠／李瓶兒私人開戶、紅袖五十萬反向價格尺與召喚權、紅娘門窗屏風換債、趙受益六條夜集外出"
  - event_id: "E98"
    title: "三十二娘街行與帳戶指令、紅娘中央籠台演出方案、錦棠首次正式約會、私人成人事件、白御行喜歡明示與相擁收幕"
  - event_id: "E102"
    title: "榴月十一日晚重新開幕完成、女子競技與紅娘壓軸、顧三辭歲再會、趙受益二百兩購四契再贈六條／楊玉環、四大金剛＋李清照女客試場、白玉池會員制接受、錦棠同宿"
  - event_id: "E114"
    title: "HOT V5.6【REBUILD-R1】｜榴月二十四日白日"
  - event_id: "E117"
    title: "HOT V5.9｜榴月二十六日上午"
```

---

## 28｜SUPPLEMENTAL_CHARACTER_008｜顧青簡

```yaml
BASE_REF:
  unified_order: 28
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_008"
  name: "顧青簡"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_CONSTRAINING"
  relation_to_player: "公開為會長／顧師爺工作關係；私下已有『清簡』地下情／成人歷史，兩層不得互相吞併。"
  current_evidence_summary:
    - "E109：榴月十七日晚兩次成人事件成立，公私面向分層。"
    - "E117：1000兩浮額先清公事，剩餘改白御行私人贈與；精確餘額 UNKNOWN。"
  locks:
    - "PUBLIC_ROLE != PRIVATE_RELATION"
    - "GIFT != STATUS_PROMOTION"

MASTER_EVENT_INDEX:
  - event_id: "E87"
    title: "曹州假印立案、定陶總會架構、京師女性時尚企畫、師師抱睡"
  - event_id: "E109"
    title: "HOT V5.1｜榴月十八日晚"
  - event_id: "E110"
    title: "HOT V5.2｜榴月十九日晚"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
  - event_id: "E114"
    title: "HOT V5.6【REBUILD-R1】｜榴月二十四日白日"
  - event_id: "E116"
    title: "HOT V5.8｜榴月二十五日夜"
  - event_id: "E117"
    title: "HOT V5.9｜榴月二十六日上午"
```

---

## 29｜SUPPLEMENTAL_CHARACTER_009｜楊玉環

```yaml
BASE_REF:
  unified_order: 29
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_009"
  name: "楊玉環"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_DORMANT"
  relation_to_player: "白玉池成人歷史已成立；對未來白＋楊＋六條三人方向曾表示目前有興趣，但可撤回，無固定情人名位。"
  current_evidence_summary:
    - "E104：白御行×楊玉環私人成人事件成立。"
    - "E112：仍願意／有興趣考慮三人方向，屬可撤回未來方向。"
  locks:
    - "INTEREST != CONSENT_FOR_FUTURE_EVENT"

MASTER_EVENT_INDEX:
  - event_id: "E96"
    title: "趙受益六條夜集返樓、楊玉環白玉池與荔枝、李師師晨間補考、定陶票據信用／朱明長債方向／曹州案盤點"
  - event_id: "E97"
    title: "長恨歌文會、柳如是東林夜談、趙受益宣和地道入席、六條／楊玉環雙線追求與三人約會可能性"
  - event_id: "E102"
    title: "榴月十一日晚重新開幕完成、女子競技與紅娘壓軸、顧三辭歲再會、趙受益二百兩購四契再贈六條／楊玉環、四大金剛＋李清照女客試場、白玉池會員制接受、錦棠同宿"
  - event_id: "E103"
    title: "榴月十二日晚白家採購規劃、蘇清十八日商會工拆帳、妓籍終身法位鎖、阿莉婭處女拍賣標的與紅娘雙人場、三十二娘妓籍申請、楊玉環白玉池代言首夜、黑公子×小桃百兩交易與同宿意向"
  - event_id: "E104"
    title: "HOT V4.6｜榴月十三日晚"
  - event_id: "E108"
    title: "HOT V5.0｜榴月十六日下午"
  - event_id: "E111"
    title: "HOT V5.3｜榴月二十日白日"
  - event_id: "E112"
    title: "HOT V5.4｜榴月二十日白日"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
  - event_id: "E114"
    title: "HOT V5.6【REBUILD-R1】｜榴月二十四日白日"
```

---

## 30｜SUPPLEMENTAL_CHARACTER_010｜柳如是

```yaml
BASE_REF:
  unified_order: 30
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_010"
  name: "柳如是"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_DORMANT"
  relation_to_player: "文藝／社交人物；MASTER 僅有入線／社交證據，未建立白御行私人關係。"
  current_evidence_summary:
    - "E97：進入相關社交事件。"
  locks:
    - "SOCIAL_PRESENCE != PRIVATE_RELATION"

MASTER_EVENT_INDEX:
  - event_id: "E97"
    title: "長恨歌文會、柳如是東林夜談、趙受益宣和地道入席、六條／楊玉環雙線追求與三人約會可能性"
```

---

## 31｜SUPPLEMENTAL_CHARACTER_011｜薛濤

```yaml
BASE_REF:
  unified_order: 31
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_011"
  name: "薛濤"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_DORMANT"
  relation_to_player: "匿名／身份揭露與女客夜相關節點；MASTER 未建立白御行私人戀愛或成人關係。"
  current_evidence_summary:
    - "E107：匿名薛濤進線，當時白御行未知其真身。"
    - "E113：合法確認狀態仍依父 MASTER，不因後續自動補完。"
  locks:
    - "DIRECTOR_IDENTITY != PLAYER_KNOWLEDGE"

MASTER_EVENT_INDEX:
  - event_id: "E107"
    title: "HOT V4.9｜榴月十五日晚"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
```

---

## 32｜SUPPLEMENTAL_CHARACTER_012｜魚玄機

```yaml
BASE_REF:
  unified_order: 32
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_012"
  name: "魚玄機"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_DORMANT"
  relation_to_player: "成年紅線女客／競技與社交節點；不是觀止妓籍，與白御行未建立私人戀愛關係。"
  current_evidence_summary:
    - "E110：中央籠台『馬』題詩賽勝洛陽馬商；只承諾看灰青難馬。"
    - "E113：雙籠事件中到場。"
  locks:
    - "GUEST != SEX_WORKER"
    - "PROMISE_TO_LOOK != TOUCH_RIDE_TRAIN"

MASTER_EVENT_INDEX:
  - event_id: "E104"
    title: "HOT V4.6｜榴月十三日晚"
  - event_id: "E107"
    title: "HOT V4.9｜榴月十五日晚"
  - event_id: "E110"
    title: "HOT V5.2｜榴月十九日晚"
  - event_id: "E111"
    title: "HOT V5.3｜榴月二十日白日"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
```

---

## 33｜SUPPLEMENTAL_CHARACTER_013｜失仙

```yaml
BASE_REF:
  unified_order: 33
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_013"
  name: "失仙"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "ACTIVE_ROUTE_CHARACTER"
  relation_lifecycle: "ACTIVE_CONSTRAINING"
  relation_to_player: "浮月閣人物／觀止競賽與異常線核心節點；與白御行有一日邀約賭與500兩當日買斷，但無戀愛或成人關係。"
  current_evidence_summary:
    - "E113：入場、與紅娘九日營收競賽、一日邀約賭成立。"
    - "E114：白御行500兩買斷失仙當日餘時；不是性愛購買。"
    - "E117：獨自離開，去向 UNKNOWN；沈家／陳州／身體真相仍 UNKNOWN。"
  locks:
    - "BUYOUT != SEXUAL_ACCESS"
    - "MYSTERY_LINK != ONTOLOGICAL_PROOF"

MASTER_EVENT_INDEX:
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
  - event_id: "E114"
    title: "HOT V5.6【REBUILD-R1】｜榴月二十四日白日"
  - event_id: "E116"
    title: "HOT V5.8｜榴月二十五日夜"
  - event_id: "E117"
    title: "HOT V5.9｜榴月二十六日上午"
```

---

## 34｜SUPPLEMENTAL_CHARACTER_014｜失美

```yaml
BASE_REF:
  unified_order: 34
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_014"
  name: "失美"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "REFERENCE_ONLY"
  relation_lifecycle: "NOT_ENTERED_ROUTE"
  relation_to_player: "僅因浮月閣四大花魁基線於 E113 被提及；MASTER 未建立實際入白御行線。"
  current_evidence_summary:
    - "E113：人物池／浮月閣基線被提及。"
  locks:
    - "REFERENCE != ARRIVAL"

MASTER_EVENT_INDEX:
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
```

> `E113` 在此只建立人物池／浮月閣四大花魁的引用，不建立本人已到白御行線。

---

## 35｜SUPPLEMENTAL_CHARACTER_015｜失蘿

```yaml
BASE_REF:
  unified_order: 35
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_015"
  name: "失蘿"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "REFERENCE_ONLY"
  relation_lifecycle: "NOT_ENTERED_ROUTE"
  relation_to_player: "僅因浮月閣四大花魁基線於 E113 被提及；MASTER 未建立實際入白御行線。"
  current_evidence_summary:
    - "E113：人物池／浮月閣基線被提及。"
  locks:
    - "REFERENCE != ARRIVAL"

MASTER_EVENT_INDEX:
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
```

> `E113` 在此只建立人物池／浮月閣四大花魁的引用，不建立本人已到白御行線。

---

## 36｜SUPPLEMENTAL_CHARACTER_016｜錯位

```yaml
BASE_REF:
  unified_order: 36
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_016"
  name: "錯位"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "REFERENCE_ONLY"
  relation_lifecycle: "NOT_ENTERED_ROUTE"
  relation_to_player: "僅因浮月閣四大花魁基線於 E113 被提及；MASTER 未建立實際入白御行線。"
  current_evidence_summary:
    - "E113：人物池／浮月閣基線被提及。"
  locks:
    - "REFERENCE != ARRIVAL"

MASTER_EVENT_INDEX:
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
```

> `E113` 在此只建立人物池／浮月閣四大花魁的引用，不建立本人已到白御行線。

---

## 37｜SUPPLEMENTAL_CHARACTER_017｜香雲

```yaml
BASE_REF:
  unified_order: 37
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_017"
  name: "香雲"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 38｜SUPPLEMENTAL_CHARACTER_018｜花晨

```yaml
BASE_REF:
  unified_order: 38
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_018"
  name: "花晨"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 39｜SUPPLEMENTAL_CHARACTER_019｜艷芳

```yaml
BASE_REF:
  unified_order: 39
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_019"
  name: "艷芳"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 40｜SUPPLEMENTAL_CHARACTER_020｜玉香

```yaml
BASE_REF:
  unified_order: 40
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_020"
  name: "玉香"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 41｜SUPPLEMENTAL_CHARACTER_021｜瑞珠

```yaml
BASE_REF:
  unified_order: 41
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_021"
  name: "瑞珠"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 42｜SUPPLEMENTAL_CHARACTER_022｜瑞玉

```yaml
BASE_REF:
  unified_order: 42
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_022"
  name: "瑞玉"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 43｜SUPPLEMENTAL_CHARACTER_023｜顧仙娘

```yaml
BASE_REF:
  unified_order: 43
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_023"
  name: "顧仙娘"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 44｜SUPPLEMENTAL_CHARACTER_024｜王婆

```yaml
BASE_REF:
  unified_order: 44
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_024"
  name: "王婆"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 45｜SUPPLEMENTAL_CHARACTER_025｜林太太

```yaml
BASE_REF:
  unified_order: 45
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_025"
  name: "林太太"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 46｜SUPPLEMENTAL_CHARACTER_026｜王六兒

```yaml
BASE_REF:
  unified_order: 46
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_026"
  name: "王六兒"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 47｜SUPPLEMENTAL_CHARACTER_027｜吳銀兒

```yaml
BASE_REF:
  unified_order: 47
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_027"
  name: "吳銀兒"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 48｜SUPPLEMENTAL_CHARACTER_028｜薛嫂

```yaml
BASE_REF:
  unified_order: 48
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_028"
  name: "薛嫂"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 49｜SUPPLEMENTAL_CHARACTER_029｜吳月娘

```yaml
BASE_REF:
  unified_order: 49
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_029"
  name: "吳月娘"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 50｜SUPPLEMENTAL_CHARACTER_030｜孟玉樓

```yaml
BASE_REF:
  unified_order: 50
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_030"
  name: "孟玉樓"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 51｜SUPPLEMENTAL_CHARACTER_031｜孫雪娥

```yaml
BASE_REF:
  unified_order: 51
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_031"
  name: "孫雪娥"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 52｜SUPPLEMENTAL_CHARACTER_032｜李嬌兒

```yaml
BASE_REF:
  unified_order: 52
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_032"
  name: "李嬌兒"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 53｜SUPPLEMENTAL_CHARACTER_033｜鄭愛月

```yaml
BASE_REF:
  unified_order: 53
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_033"
  name: "鄭愛月"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 54｜SUPPLEMENTAL_CHARACTER_034｜白玉潔

```yaml
BASE_REF:
  unified_order: 54
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_034"
  name: "白玉潔"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 55｜SUPPLEMENTAL_CHARACTER_035｜張明姝

```yaml
BASE_REF:
  unified_order: 55
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_035"
  name: "張明姝"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 56｜SUPPLEMENTAL_CHARACTER_036｜孫清倩

```yaml
BASE_REF:
  unified_order: 56
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_036"
  name: "孫清倩"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 57｜SUPPLEMENTAL_CHARACTER_037｜沈玉晶

```yaml
BASE_REF:
  unified_order: 57
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_037"
  name: "沈玉晶"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 58｜SUPPLEMENTAL_CHARACTER_038｜高承義

```yaml
BASE_REF:
  unified_order: 58
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_038"
  name: "高承義"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 59｜SUPPLEMENTAL_CHARACTER_039｜李明遠

```yaml
BASE_REF:
  unified_order: 59
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_039"
  name: "李明遠"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 60｜SUPPLEMENTAL_CHARACTER_040｜王慎行

```yaml
BASE_REF:
  unified_order: 60
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_040"
  name: "王慎行"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

## 61｜SUPPLEMENTAL_CHARACTER_041｜王廷衡

```yaml
BASE_REF:
  unified_order: 61
  lcapg_source_id: "SUPPLEMENTAL_CHARACTER_041"
  name: "王廷衡"
  baseline_owner: "LCAPG V3.3"

ROUTE_STATE_AT_MASTER_V5_9:
  route_presence: "NOT_ESTABLISHED_IN_MASTER_ROUTE"
  relation_lifecycle: "NOT_ESTABLISHED"
  relation_to_player: "截至 MASTER V5.9 cutoff，沒有足以建立白御行線實際相遇／關係的 MASTER 事件證據。"
  current_evidence_summary: []
  locks:
    - "LCAPG_BASE_EXISTS != ROUTE_ENTRY"

MASTER_EVENT_INDEX:
  []
```

---

# 3｜臨時 Route Character Registry｜無 LCAPG BASE

> 以下人物在 MASTER 已具有實際 Route evidence，但沒有 LCAPG 正式 BASE。編號只屬白御行線；不取得跨線法位。

```yaml
TEMP_ID_POLICY:
  named_family: "BYX_TMP_###"
  anonymous_family: "BYX_ANON_###"
  stable_within_route: true
  cross_route_authority: false
  lcapg_admission: false
  promotion_requires: "GM explicit LCAPG successor"
```

## BYX_TMP_001｜似伊

```yaml
route_character_id: "BYX_TMP_001"
name_or_label: "似伊"
base_character_ref: null
route_summary: "跨世界／私人從屬歷史節點；缺乏 LCAPG BASE。"
master_event_index:
  - event_id: "E12"
    title: "似伊影像與紅袖可能未來"
  - event_id: "E24"
    title: "似伊實體入場與退場"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_002｜阿泠

```yaml
route_character_id: "BYX_TMP_002"
name_or_label: "阿泠"
base_character_ref: null
route_summary: "白玉池自主空間人物；自選姓名，拒絕白姓／妹妹／白家人／所有物定位；白玉池是否營業與服務由她決定。"
master_event_index:
  - event_id: "E57"
    title: "阿泠現身與白玉池水療提案"
  - event_id: "E58"
    title: "李瓶兒入池與追求機會未關閉"
  - event_id: "E60"
    title: "白玉池封池、蘇清研究與潘金蓮尚未介入之初始狀態"
  - event_id: "E67"
    title: "阿泠兄妹方向仍未成立"
  - event_id: "E86"
    title: "潘身籍副冊補證、白玉池許願幣／定存框架、師師道歉修復與如夫人再確認"
  - event_id: "E109"
    title: "HOT V5.1｜榴月十八日晚"
  - event_id: "E112"
    title: "HOT V5.4｜榴月二十日白日"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
  - event_id: "E114"
    title: "HOT V5.6【REBUILD-R1】｜榴月二十四日白日"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
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

## BYX_TMP_003｜常煒

```yaml
route_character_id: "BYX_TMP_003"
name_or_label: "常煒"
base_character_ref: null
route_summary: "定陶商會副會長／營運協作者；E117 物流女子360兩年終獎抵扣條件固定。"
master_event_index:
  - event_id: "E79"
    title: "HOT V2.1：定陶商戰、蘇清私約與白玉池補固"
  - event_id: "E117"
    title: "HOT V5.9｜榴月二十六日上午"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
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

## BYX_TMP_004｜沈萬三

```yaml
route_character_id: "BYX_TMP_004"
name_or_label: "沈萬三"
base_character_ref: null
route_summary: "高能力商業節點；與白御行／定陶形成停止代理試探與技術合作原則，未簽盟書、非永久同盟；風滿樓三金主之一。"
master_event_index:
  - event_id: "E79"
    title: "HOT V2.1：定陶商戰、蘇清私約與白玉池補固"
  - event_id: "E81"
    title: "HOT V2.3：定陶—沈萬三合作與多線案件升級"
  - event_id: "E82"
    title: "HOT V2.4：風滿樓、西門暗櫃與五千後算"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
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

## BYX_TMP_005｜許慎言

```yaml
route_character_id: "BYX_TMP_005"
name_or_label: "許慎言"
base_character_ref: null
route_summary: "蘇清 principal lawyer／法律程序節點；受定陶資助按摩恢復券，不因此取得案件結果主權。"
master_event_index:
  - event_id: "E82"
    title: "HOT V2.4：風滿樓、西門暗櫃與五千後算"
  - event_id: "E84"
    title: "京師軍械案鏡頭收網、觀止民事戰重啟、許慎言七十二小時按摩券"
  - event_id: "E85"
    title: "潘金蓮返樓、五千原款重分類、五萬索賠、身籍與重新掛牌條件式討論"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
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

## BYX_TMP_006｜程景衡

```yaml
route_character_id: "BYX_TMP_006"
name_or_label: "程景衡"
base_character_ref: null
route_summary: "定陶商會調查／押運與外圍追查節點。"
master_event_index:
  - event_id: "E49"
    title: "定陶十二車三烤鹽失竊與全數找回"
  - event_id: "E54"
    title: "涉案者押回定陶、補假與調查授權"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_007｜西門慶

```yaml
route_character_id: "BYX_TMP_007"
name_or_label: "西門慶"
base_character_ref: null
route_summary: "五千舊案、廣源與開封府程序核心外部人物；關係具對抗／法律因果，不是玩家私人關係。"
master_event_index:
  - event_id: "E81"
    title: "HOT V2.3：定陶—沈萬三合作與多線案件升級"
  - event_id: "E82"
    title: "HOT V2.4：風滿樓、西門暗櫃與五千後算"
  - event_id: "E83"
    title: "HOT V2.5：開封法網、阿麗婭重定義與六條來訪"
  - event_id: "E84"
    title: "京師軍械案鏡頭收網、觀止民事戰重啟、許慎言七十二小時按摩券"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_008｜白三十二娘／三十二娘

```yaml
route_character_id: "BYX_TMP_008"
name_or_label: "白三十二娘／三十二娘"
base_character_ref: null
route_summary: "白御行私人持契成年工作人員；白家日常調度與多次跑腿／預算線。"
master_event_index:
  - event_id: "E88"
    title: "女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限"
  - event_id: "E98"
    title: "三十二娘街行與帳戶指令、紅娘中央籠台演出方案、錦棠首次正式約會、私人成人事件、白御行喜歡明示與相擁收幕"
  - event_id: "E103"
    title: "榴月十二日晚白家採購規劃、蘇清十八日商會工拆帳、妓籍終身法位鎖、阿莉婭處女拍賣標的與紅娘雙人場、三十二娘妓籍申請、楊玉環白玉池代言首夜、黑公子×小桃百兩交易與同宿意向"
  - event_id: "E109"
    title: "HOT V5.1｜榴月十八日晚"
  - event_id: "E116"
    title: "HOT V5.8｜榴月二十五日夜"
  - event_id: "E117"
    title: "HOT V5.9｜榴月二十六日上午"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_009｜白明礬

```yaml
route_character_id: "BYX_TMP_009"
name_or_label: "白明礬"
base_character_ref: null
route_summary: "白御行私人持契成年工作人員；方掌櫃布莊／染布線，E117 私下學技術意圖不得外洩。"
master_event_index:
  - event_id: "E88"
    title: "女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限"
  - event_id: "E99"
    title: "榴月四日兩牙行二十三名成年候選雙向遴選、九名丫鬟成交分配、制服／自願剪髮方案、白希白明礬初教、十四名落選者吃麵收尾"
  - event_id: "E117"
    title: "HOT V5.9｜榴月二十六日上午"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_010｜白紅伶

```yaml
route_character_id: "BYX_TMP_010"
name_or_label: "白紅伶"
base_character_ref: null
route_summary: "白御行私人持契成年工作人員；曾執行紅娘免費全套假傳聞煙幕。"
master_event_index:
  - event_id: "E88"
    title: "女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限"
  - event_id: "E91"
    title: "浮香自願給床與成人夜、紅娘煙幕揭穿、九幽帝皇聯誼會正式訂單"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_011｜白希

```yaml
route_character_id: "BYX_TMP_011"
name_or_label: "白希"
base_character_ref: null
route_summary: "白御行私人持契成年工作人員。"
master_event_index:
  - event_id: "E88"
    title: "女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限"
  - event_id: "E99"
    title: "榴月四日兩牙行二十三名成年候選雙向遴選、九名丫鬟成交分配、制服／自願剪髮方案、白希白明礬初教、十四名落選者吃麵收尾"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_012｜沈夫人

```yaml
route_character_id: "BYX_TMP_012"
name_or_label: "沈夫人"
base_character_ref: null
route_summary: "一夜型自願成人事件；只限兩人，事後無第二次義務、無戀愛／情婦／婚姻／排他。"
master_event_index:
  - event_id: "E110"
    title: "HOT V5.2｜榴月十九日晚"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_013｜程小姐

```yaml
route_character_id: "BYX_TMP_013"
name_or_label: "程小姐"
base_character_ref: null
route_summary: "白家成年女客；未參與成人事件，對若當時是否會上樓回答 UNKNOWN。"
master_event_index:
  - event_id: "E110"
    title: "HOT V5.2｜榴月十九日晚"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_014｜蘇東坡

```yaml
route_character_id: "BYX_TMP_014"
name_or_label: "蘇東坡"
base_character_ref: null
route_summary: "文士／女客夜與初一晚場主持邀請節點；E117 主持與出席仍 PENDING。"
master_event_index:
  - event_id: "E20"
    title: "柳如煙概念體、李師師與趙受益花魁局"
  - event_id: "E26"
    title: "仁宗朝夜談：天章閣、馬吊與歷史會計帳"
  - event_id: "E30"
    title: "第五夜善後與人物去留"
  - event_id: "E106"
    title: "HOT V4.8｜榴月十五日下午"
  - event_id: "E107"
    title: "HOT V4.9｜榴月十五日晚"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
  - event_id: "E117"
    title: "HOT V5.9｜榴月二十六日上午"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
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

## BYX_TMP_015｜陳季常

```yaml
route_character_id: "BYX_TMP_015"
name_or_label: "陳季常"
base_character_ref: null
route_summary: "文士／女客夜節點；與金面具女客事件及柳月娥後續相關。"
master_event_index:
  - event_id: "E106"
    title: "HOT V4.8｜榴月十五日下午"
  - event_id: "E107"
    title: "HOT V4.9｜榴月十五日晚"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_016｜佛印

```yaml
route_character_id: "BYX_TMP_016"
name_or_label: "佛印"
base_character_ref: null
route_summary: "文士／女客夜社交節點。"
master_event_index:
  - event_id: "E106"
    title: "HOT V4.8｜榴月十五日下午"
  - event_id: "E107"
    title: "HOT V4.9｜榴月十五日晚"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_017｜蘇小妹

```yaml
route_character_id: "BYX_TMP_017"
name_or_label: "蘇小妹"
base_character_ref: null
route_summary: "成年紅線女客識別；拒絕當場登妓籍。"
master_event_index:
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_018｜柳月娥

```yaml
route_character_id: "BYX_TMP_018"
name_or_label: "柳月娥"
base_character_ref: null
route_summary: "陳季常妻；雙籠投蛋事件與金面具身份疑雲節點，客觀身份仍 UNKNOWN。"
master_event_index:
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_019｜柳永

```yaml
route_character_id: "BYX_TMP_019"
name_or_label: "柳永"
base_character_ref: null
route_summary: "本人已入觀止與白玉池；商會自由顧問方向 PROPOSED，是否接受與報酬 PENDING。"
master_event_index:
  - event_id: "E114"
    title: "HOT V5.6【REBUILD-R1】｜榴月二十四日白日"
  - event_id: "E117"
    title: "HOT V5.9｜榴月二十六日上午"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
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

## BYX_TMP_020｜沈秋

```yaml
route_character_id: "BYX_TMP_020"
name_or_label: "沈秋"
base_character_ref: null
route_summary: "沈家空房／後續現場節點。"
master_event_index:
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
  - event_id: "E116"
    title: "HOT V5.8｜榴月二十五日夜"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_021｜程素娘

```yaml
route_character_id: "BYX_TMP_021"
name_or_label: "程素娘"
base_character_ref: null
route_summary: "沈家／失仙晨報資訊節點。"
master_event_index:
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
  - event_id: "E117"
    title: "HOT V5.9｜榴月二十六日上午"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_022｜桃枝

```yaml
route_character_id: "BYX_TMP_022"
name_or_label: "桃枝"
base_character_ref: null
route_summary: "陪席契約爭議與開放續約營運實務節點；原契約／20兩押金最終結算未確認。"
master_event_index:
  - event_id: "E110"
    title: "HOT V5.2｜榴月十九日晚"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_023｜方掌櫃

```yaml
route_character_id: "BYX_TMP_023"
name_or_label: "方掌櫃"
base_character_ref: null
route_summary: "布匹／驗貨／品質監督與染布線商業節點。"
master_event_index:
  - event_id: "E117"
    title: "HOT V5.9｜榴月二十六日上午"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_024｜黑公子

```yaml
route_character_id: "BYX_TMP_024"
name_or_label: "黑公子"
base_character_ref: null
route_summary: "觀止交易／同宿意向事件節點。"
master_event_index:
  - event_id: "E103"
    title: "榴月十二日晚白家採購規劃、蘇清十八日商會工拆帳、妓籍終身法位鎖、阿莉婭處女拍賣標的與紅娘雙人場、三十二娘妓籍申請、楊玉環白玉池代言首夜、黑公子×小桃百兩交易與同宿意向"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_025｜小桃

```yaml
route_character_id: "BYX_TMP_025"
name_or_label: "小桃"
base_character_ref: null
route_summary: "與黑公子百兩交易／同宿意向事件節點。"
master_event_index:
  - event_id: "E103"
    title: "榴月十二日晚白家採購規劃、蘇清十八日商會工拆帳、妓籍終身法位鎖、阿莉婭處女拍賣標的與紅娘雙人場、三十二娘妓籍申請、楊玉環白玉池代言首夜、黑公子×小桃百兩交易與同宿意向"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_026｜石魁

```yaml
route_character_id: "BYX_TMP_026"
name_or_label: "石魁"
base_character_ref: null
route_summary: "河東車行牙人；被捕並與藏貨、分帳、員工資訊收買線相關。"
master_event_index:
  - event_id: "E51"
    title: "石魁、灰簿先生與吳六未決"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_027｜灰簿先生

```yaml
route_character_id: "BYX_TMP_027"
name_or_label: "灰簿先生"
base_character_ref: null
route_summary: "底層口供提及之未知人物／稱呼；本體是否單一人物 UNKNOWN。"
master_event_index:
  - event_id: "E51"
    title: "石魁、灰簿先生與吳六未決"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_028｜吳六

```yaml
route_character_id: "BYX_TMP_028"
name_or_label: "吳六"
base_character_ref: null
route_summary: "東倉副倉簿；是否涉案 NOT_ESTABLISHED。"
master_event_index:
  - event_id: "E51"
    title: "石魁、灰簿先生與吳六未決"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_029｜梅花面具成年紅線女客

```yaml
route_character_id: "BYX_TMP_029"
name_or_label: "梅花面具成年紅線女客"
base_character_ref: null
route_summary: "與白御行完成一次自願露水成人事件；身份未固定。"
master_event_index:
  - event_id: "E107"
    title: "HOT V4.9｜榴月十五日晚"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_ANON_001｜金面具女客

```yaml
route_character_id: "BYX_ANON_001"
name_or_label: "金面具女客"
base_character_ref: null
route_summary: "與陳季常同行／進房；客觀身份 UNKNOWN，柳月娥嫌疑升高但未證成。"
master_event_index:
  - event_id: "E107"
    title: "HOT V4.9｜榴月十五日晚"
  - event_id: "E113"
    title: "HOT V5.5｜榴月二十四日清晨"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_ANON_002｜觀止大堂陌生中年男人

```yaml
route_character_id: "BYX_ANON_002"
name_or_label: "觀止大堂陌生中年男人"
base_character_ref: null
route_summary: "長時間觀察籠台、樓梯、欄杆與出入口；身份／目的 UNKNOWN。"
master_event_index:
  - event_id: "E111"
    title: "HOT V5.3｜榴月二十日白日"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_TMP_030｜洛陽馬商

```yaml
route_character_id: "BYX_TMP_030"
name_or_label: "洛陽馬商"
base_character_ref: null
route_summary: "魚玄機『馬』題詩賽對手；勝負已定，其他私人關係未建立。"
master_event_index:
  - event_id: "E110"
    title: "HOT V5.2｜榴月十九日晚"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

## BYX_ANON_003｜年輕車夫首告者

```yaml
route_character_id: "BYX_ANON_003"
name_or_label: "年輕車夫首告者"
base_character_ref: null
route_summary: "姓名未公開固化；首告後本人與家眷受保護、急債清除並領賞。"
master_event_index:
  - event_id: "E50"
    title: "第一告密者受保護與領賞"
authority: "ROUTE_LOCAL_ONLY"
promotion_state: "NOT_PROMOTED_TO_LCAPG"
```

---

# 4｜編譯統計與驗證

```yaml
VALIDATION:
  lcapg_total_records: 61
  active_route_characters: 27
  reference_only_characters: 3
  no_master_route_event_characters: 31
  temporary_route_records: 33
  master_event_ids_detected: 117
  expected_master_event_range: "E01-E117"
  all_lcapg_event_refs_exist_in_master: true
  all_temp_event_refs_exist_in_master: true
  hot_v5_10_v5_12_absorbed: false
  lcapg_base_rewritten_by_route: false

NO_MASTER_ROUTE_EVENT_BASE_CHARACTERS:
  - "07｜CHARACTER_SLOT_5｜宋蕙蓮"
  - "08｜CHARACTER_SLOT_6｜李桂姐"
  - "16｜NATIVE_08｜李媽媽"
  - "17｜NATIVE_09｜安舟"
  - "18｜NATIVE_10｜汪鹽商"
  - "20｜CHARACTER_SLOT_15｜貂蟬"
  - "37｜SUPPLEMENTAL_CHARACTER_017｜香雲"
  - "38｜SUPPLEMENTAL_CHARACTER_018｜花晨"
  - "39｜SUPPLEMENTAL_CHARACTER_019｜艷芳"
  - "40｜SUPPLEMENTAL_CHARACTER_020｜玉香"
  - "41｜SUPPLEMENTAL_CHARACTER_021｜瑞珠"
  - "42｜SUPPLEMENTAL_CHARACTER_022｜瑞玉"
  - "43｜SUPPLEMENTAL_CHARACTER_023｜顧仙娘"
  - "44｜SUPPLEMENTAL_CHARACTER_024｜王婆"
  - "45｜SUPPLEMENTAL_CHARACTER_025｜林太太"
  - "46｜SUPPLEMENTAL_CHARACTER_026｜王六兒"
  - "47｜SUPPLEMENTAL_CHARACTER_027｜吳銀兒"
  - "48｜SUPPLEMENTAL_CHARACTER_028｜薛嫂"
  - "49｜SUPPLEMENTAL_CHARACTER_029｜吳月娘"
  - "50｜SUPPLEMENTAL_CHARACTER_030｜孟玉樓"
  - "51｜SUPPLEMENTAL_CHARACTER_031｜孫雪娥"
  - "52｜SUPPLEMENTAL_CHARACTER_032｜李嬌兒"
  - "53｜SUPPLEMENTAL_CHARACTER_033｜鄭愛月"
  - "54｜SUPPLEMENTAL_CHARACTER_034｜白玉潔"
  - "55｜SUPPLEMENTAL_CHARACTER_035｜張明姝"
  - "56｜SUPPLEMENTAL_CHARACTER_036｜孫清倩"
  - "57｜SUPPLEMENTAL_CHARACTER_037｜沈玉晶"
  - "58｜SUPPLEMENTAL_CHARACTER_038｜高承義"
  - "59｜SUPPLEMENTAL_CHARACTER_039｜李明遠"
  - "60｜SUPPLEMENTAL_CHARACTER_040｜王慎行"
  - "61｜SUPPLEMENTAL_CHARACTER_041｜王廷衡"

COMPILER_LOCKS:
  - "若後續發現 RCL 摘要與 E## 衝突，修 RCL，不改 MASTER。"
  - "下一次 MASTER promotion 必須重新編譯新 cutoff 的 RCL。"
  - "HOT V5.10-V5.12 只在 LIVE resume 層疊加；除非它們被正式 promotion，否則不寫入本版履歷。"
```

---

# 5｜最短接關句

> **先讀人物卡，再讀這份履歷；需要細節回 E##；最後疊 MASTER 之後的 HOT。**