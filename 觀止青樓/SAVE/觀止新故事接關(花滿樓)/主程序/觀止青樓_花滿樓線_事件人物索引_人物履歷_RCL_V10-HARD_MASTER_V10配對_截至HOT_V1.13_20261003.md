# 觀止青樓｜花滿樓線事件人物索引／人物履歷 RCL V10-HARD
## 與 MASTER SAVE V10-HARD 同代配對｜E01–E44｜LCAPG V3.3.19／71人對齊｜截至 HOT V1.13
### GUANZHI_RCL_SCHEMA_V1_1_COMPATIBLE｜MASTER/RCL ATOMIC PAIR

```yaml
DOCUMENT:
  title: "觀止青樓｜花滿樓線事件人物索引／人物履歷"
  short_id: "RCL-HML-V10"
  version: "V10-HARD"
  memory_generation: "V10"
  document_type: "COMPILED_ROUTE_EVENT_CHARACTER_LEDGER"
  status: "MASTER_DERIVED / SAME_GENERATION_ATOMIC_PAIR"
  compile_date: "2026-10-03"

PAIR:
  master_file: "觀止青樓_花滿樓線_MASTER_SAVE_V10-HARD_全歷史自足_截至HOT_V1.13_雙檔配對版_20261003.md"
  master_version: "V10-HARD"
  master_story_cutoff: "HOT V1.13 / 理火三年菊月初六入夜"
  latest_hot: "V1.13"
  event_range: "E01-E44"
  lcapg_version: "V3.3.19-CURRENT / 71人"
  hash_policy: "MASTER records RCL SHA256 one-way; RCL records MASTER filename/version to avoid circular hash dependency"

EVENT_ID_POLICY:
  E01_E18: "繼承 MASTER V1.5-HARD 已固化事件號"
  E19_E44: "本次 V10 編譯新增的穩定索引號；只用來指向 V1.6-V1.13 已演事件，不表示舊 HOT 當時已有這些編號"
  rule: "事件號是索引，不新增事件、不回鑄人物當時知情"
```

> **LCAPG 是人物基線；MASTER 是已發生事件正文；RCL 是事件↔人物索引與人物在花滿樓線累積到哪裡。**
>
> 正常重載以 **MASTER V10-HARD + 本 RCL V10-HARD** 為同代配對。需要人物來源史／一般性格時再查 LCAPG；需要事件原文細節時回 MASTER。

---

# 1｜讀取規則

```text
LCAPG V3.3.19 BASE / 71
↓
MASTER V10-HARD EVENT BODY
↕
RCL V10-HARD EVENT↔CHARACTER INDEX / CURRENT ROUTE BIOGRAPHY
↓
HOT V1.14+ future overlays
```

固定鎖：

```text
EVENT PARTICIPATION != FULL KNOWLEDGE
LCAPG BASE != ROUTE ENTRY
CHARACTER SELF-REPORT != OBJECTIVE WORLD TRUTH
LATER REVEAL != EARLIER KNOWLEDGE
PAYMENT != ACCESS != RELATION != CONSENT
ADULT EVENT != LOVE != FUTURE CONSENT
INVITE != ACCEPTANCE != ARRIVAL
JOKE / TEST / VOID ATTEMPT != WORLD FACT
UNDECIDED stays undecided until event/evidence
CURRENT overlay may update status but does not erase historical state
```

---

# 2｜EVENT → CHARACTER INDEX｜E01–E44

> `direct_participants` 只列有事件證據支持的直接參與／在場核心人物；`related_not_confirmed_present` 只表示事件關聯，不得當成在場證據。群眾與未具名職務者保留群體標記。

## E01｜桂月十六｜初到觀止與香料交貨糾紛

- **source:** MASTER V1.5-HARD
- **direct_participants:** 花滿樓、香藥行送貨／驗貨相關人員（未具名）

## E02｜桂月十六｜大堂生活、酒帳與新曲觀察

- **source:** MASTER V1.5-HARD
- **direct_participants:** 花滿樓、李桂姐、醉花、浮香、紫蘭、小桃、青衣、柳黃

## E03｜桂月十六｜《鮮花滿月樓》與紫蘭一壺酒價交易

- **source:** MASTER V1.5-HARD
- **direct_participants:** 花滿樓、潘金蓮、浮香、紫蘭、青衣、柳黃

## E04｜桂月二十二仕女夜｜《鮮花滿月樓》首次公開試唱與小調方向

- **source:** MASTER V1.5-HARD
- **direct_participants:** 花滿樓、潘金蓮、浮香、紫蘭、青衣、柳黃

## E05｜桂月二十二｜沈夫人二百兩送嫁詞約

- **source:** MASTER V1.5-HARD
- **direct_participants:** 花滿樓、沈夫人

## E06｜桂月二十二｜阿蘅比詩、桂花釀與《鵲踏枝·曉別》

- **source:** MASTER V1.5-HARD
- **direct_participants:** 花滿樓、阿蘅／陸夫人（桂月二十二客人）

## E07｜桂月二十二｜醉花西側半圓高台酒吧構想

- **source:** MASTER V1.5-HARD
- **direct_participants:** 花滿樓、潘金蓮、醉花

## E08｜桂月二十五｜照夜／三聖母自主到觀止與三層身份

- **source:** MASTER V1.5-HARD
- **direct_participants:** 花滿樓、潘金蓮、照夜／三聖母、小桃

## E09｜桂月二十五｜花滿樓 × 照夜「人間安身約」

- **source:** MASTER V1.5-HARD
- **direct_participants:** 花滿樓、潘金蓮、照夜／三聖母

## E10｜桂月二十五｜王昭君、《陽關三疊》與紫蘭藝術線

- **source:** MASTER V1.5-HARD
- **direct_participants:** 花滿樓、醉花、浮香、紫蘭、青衣、柳黃、王昭君、鈴娘

## E11｜桂月二十五｜仕女夜巷、夜市商業與疑似宮禁端

- **source:** MASTER V1.5-HARD
- **direct_participants:** 花滿樓、潘金蓮、龐春梅、禁軍詢問人員（未具名）

## E12｜桂月二十五｜「一炷香鴛鴦會」制度與花滿樓首席報名

- **source:** MASTER V1.5-HARD
- **direct_participants:** 花滿樓、潘金蓮

## E13｜桂月二十五至菊月初一｜官家邀帖、劉娥密談與首屆輪轉相親實跑

- **source:** MASTER V1.5-HARD
- **direct_participants:** 花滿樓、潘金蓮、龐春梅、蘇清、照夜／三聖母、小桃、青雀、玄燕、白鹿、紅綃、沈如晦
- **related_not_confirmed_present:** 趙受益／官家（當時邀帖未證到場）

## E14｜菊月初一夜｜「故人」沈如晦與私人成人場

- **source:** MASTER V1.5-HARD
- **direct_participants:** 花滿樓、沈如晦

## E15｜菊月初一夜至初二清晨｜同睡與沈如晦自行離房

- **source:** MASTER V1.5-HARD
- **direct_participants:** 花滿樓、沈如晦

## E16｜菊月初二午後｜小桃、陌生傳話女子與一炷香局外約見入口

- **source:** MASTER V1.5-HARD
- **direct_participants:** 花滿樓、小桃、未知傳話女子

## E17｜菊月初二晚｜薄櫻詞約、匿名測試與真正委託

- **source:** MASTER V1.5-HARD
- **direct_participants:** 花滿樓、紫蘭、薄櫻

## E18｜菊月初三巳正前後｜邵承祿六年帳契談判正式開場

- **source:** MASTER V1.5-HARD
- **direct_participants:** 花滿樓、薄櫻、邵承祿、捧帳冊小夥計

## E19｜菊月初三巳正後｜龐宜娘六年帳契談判完成與三份契據交付

- **source:** HOT V1.6
- **direct_participants:** 花滿樓、龐宜娘／薄櫻、邵承祿、捧帳冊小夥計

## E20｜菊月初三午至午後｜不明男子、賭坊失五兩、舊貨攤七張衣樣、時空道人籤語

- **source:** HOT V1.6
- **direct_participants:** 花滿樓、不明男子、舊貨攤女攤主、藍袍青年、時空道人、賭坊莊家／客群（未具名）

## E21｜菊月初三午後偏後｜返觀止、詞曲分流與花滿樓身世財務公開

- **source:** HOT V1.6
- **direct_participants:** 花滿樓、潘金蓮、紫蘭、白三娘、宋蕙蓮、青衣、柳黃、小桃
- **related_not_confirmed_present:** 醉花（作品／酒吧線被提及）

## E22｜菊月初三夜｜觀止多線營業與紫蘭、浮香雙魁衝突

- **source:** HOT V1.7
- **direct_participants:** 花滿樓、潘金蓮、龐春梅、李瓶兒、李桂姐、醉花、十三娘、白三娘、浮香、紫蘭、小翠、紅娘氏、青禾、青衣、柳黃、小桃
- **related_not_confirmed_present:** 三名女客與多桌客人（未具名）

## E23｜菊月初三夜｜《賀新郎·雙魁夜鬥》五段募資250兩與堂記見證

- **source:** HOT V1.7
- **direct_participants:** 花滿樓、潘金蓮、李瓶兒、十三娘、紫蘭、浮香、白三娘、醉花、龐春梅
- **related_not_confirmed_present:** 多名出資客人／親見者／在場催詞者

## E24｜菊月初三夜｜《鮮花滿月樓》三次真實叫回成功與《夢回謝橋》交付

- **source:** HOT V1.7
- **direct_participants:** 花滿樓、紫蘭、浮香、青衣、柳黃
- **related_not_confirmed_present:** 實際叫回之女客／後排客／老客（未具名）

## E25｜菊月初三夜｜『五萬兩私奔案』戲謔公告與紫蘭自由身／贖身談話

- **source:** HOT V1.7
- **direct_participants:** 花滿樓、潘金蓮、龐春梅、十三娘、醉花、白三娘、紫蘭、浮香

## E26｜菊月初四白日／夜｜假親見箋、二級市場與三十兩『魂在場』新證明

- **source:** HOT V1.8
- **direct_participants:** 花滿樓、假箋持有人／買家（未具名）、觀止帳房／見證人（未具名）
- **related_not_confirmed_present:** 前夜《雙魁夜鬥》出資者群體

## E27｜菊月初四夜｜浮香主動靠近、餵食與專屬新歌材料形成

- **source:** HOT V1.8
- **direct_participants:** 花滿樓、浮香、紫蘭

## E28｜菊月初四深夜｜花滿樓、浮香夜探鬼滿樓並確認女鬼陸蘅

- **source:** HOT V1.8
- **direct_participants:** 花滿樓、浮香、陸蘅／阿蘅
- **related_not_confirmed_present:** 活貓／未知井邊歌聲／哭聲／尾影（非人物確認）

## E29｜菊月初四深夜｜花滿樓與浮香同床、界線改變與一次成人事件完成

- **source:** HOT V1.8
- **direct_participants:** 花滿樓、浮香

## E30｜菊月初五清晨前後｜《紅透清早》專屬演唱權、事後邊界與浮香離宅

- **source:** HOT V1.9
- **direct_participants:** 花滿樓、浮香

## E31｜菊月初五白日｜鬼滿樓四僕入宅與家用／待遇安排

- **source:** HOT V1.9
- **direct_participants:** 花滿樓、許嫂、石頭、春桃、阿巧

## E32｜菊月初五午後｜姚安娘再會、薛嫂五女看郎線、紫蘭提出見陸蘅

- **source:** HOT V1.9
- **direct_participants:** 花滿樓、姚安娘、薛嫂、紫蘭、浮香
- **related_not_confirmed_present:** 薛嫂五女看郎會候選女子（未固定）、陸蘅（被邀約／未在場）

## E33｜菊月初五後續／入夜前後｜祝惟實舊木馬、窄木盒與范姓男子五兩限制

- **source:** HOT V1.10
- **direct_participants:** 花滿樓、祝惟實、范姓男子
- **related_not_confirmed_present:** 陸蘅（木馬來源線相關但本段未必在場）

## E34｜菊月初五後續之夜｜蘇東坡入觀止、環肥燕瘦與官家趙受益、楊玉環到場

- **source:** HOT V1.10
- **direct_participants:** 花滿樓、蘇東坡、趙受益、楊玉環、潘金蓮
- **related_not_confirmed_present:** 趙飛燕（尚未到場／八門結果仍待）

## E35｜同夜｜趙飛燕到場、八門『全來』、待→侍暗改與環肥燕瘦兩輪

- **source:** HOT V1.11
- **direct_participants:** 花滿樓、趙受益、楊玉環、趙飛燕、蘇東坡、潘金蓮

## E36｜同夜｜『趙公子追雙姝專案』成立、三路媒婆分工與募資啟動

- **source:** HOT V1.11
- **direct_participants:** 花滿樓、趙受益、楊玉環、趙飛燕、潘金蓮、紅娘氏、王婆、薛嫂

## E37｜菊月初六丑時至早晨｜鬼滿樓四僕、陸蘅、木馬與未開木盒

- **source:** HOT V1.12
- **direct_participants:** 花滿樓、陸蘅／阿蘅、許嫂、石頭、春桃、阿巧
- **related_not_confirmed_present:** 海娘／前朝千金鬼／東瀛兵鬼（只作花滿樓舊聞，未入場）

## E38｜菊月初六早晨｜追雙姝專案第一次會議與百兩專案資本

- **source:** HOT V1.12
- **direct_participants:** 花滿樓、趙受益、潘金蓮、紅娘氏、王婆、薛嫂
- **related_not_confirmed_present:** 楊玉環、趙飛燕

## E39｜菊月初六上午至午後｜瓦舍說書、蘇東坡到場與『侍』原牌六千兩拍賣

- **source:** HOT V1.12
- **direct_participants:** 花滿樓、瓦舍老說書先生、蘇東坡、瓦舍掌事、匿名買家代理／競價者
- **related_not_confirmed_present:** 趙受益（派隨從觀場，未確認為買家）

## E40｜菊月初六午後｜顧青簡資產配置、五千兩死存／五百活存與商會大宅履約爭議

- **source:** HOT V1.12
- **direct_participants:** 花滿樓、顧青簡
- **related_not_confirmed_present:** 定陶商會／宅屋主（制度相對人，未必在場）

## E41｜菊月初六入夜｜返觀止、私人聘廚與初八老說書先生特別通行帖

- **source:** HOT V1.13
- **direct_participants:** 花滿樓、潘金蓮、趙受益、紅娘氏
- **related_not_confirmed_present:** 瓦舍老說書先生（通行資格對象，未必在場）

## E42｜菊月初六入夜｜醉花盲飲、《晚來》、二十兩研發投資與《遲到的正義》

- **source:** HOT V1.13
- **direct_participants:** 花滿樓、醉花、紫蘭、浮香、趙受益、照夜／三聖母、潘金蓮

## E43｜菊月初六入夜｜照夜妓籍CURRENT校正、出道／初十首夜競拍、出道詞與尋沉香

- **source:** HOT V1.13
- **direct_participants:** 花滿樓、照夜／三聖母、潘金蓮、醉花、紫蘭、浮香
- **related_not_confirmed_present:** 沉香（尋人對象，所在未知）

## E44｜菊月初六入夜｜趙受益借佩劍、人皇天子劍與天庭／開封府法域策略

- **source:** HOT V1.13
- **direct_participants:** 花滿樓、趙受益、紅娘氏、照夜／三聖母
- **related_not_confirmed_present:** 潘金蓮、趙受益管事（奉命取劍）、天庭／楊戩（未到場）、開封府／包拯（策略對象，未受理）

---

# 3｜CHARACTER → EVENT INDEX / CURRENT ROUTE BIOGRAPHY

## 3.1｜玩家與 LCAPG／核心路線人物

## 花滿樓

```yaml
relation_to_route: "PLAYER CHARACTER"
evidence_event_ids: [E01, E02, E03, E04, E05, E06, E07, E08, E09, E10, E11, E12, E13, E14, E15, E16, E17, E18, E19, E20, E21, E22, E23, E24, E25, E26, E27, E28, E29, E30, E31, E32, E33, E34, E35, E36, E37, E38, E39, E40, E41, E42, E43, E44]
current_route_state:
  - "目前在理火三年菊月初六入夜的觀止大堂／門口活動。"
  - "V1.12 新財富操作基準約5700兩；5000兩死存、500兩活存；V1.13向醉花實付20兩研發款後，隨身控制數180兩。"
  - "堅持『我不能在青樓裡面花一毛錢』；私人聘廚與研發投資不列觀止客帳。"
  - "照夜人間安身約仍在；已推進照夜出道、初十首夜競拍宣傳、尋沉香與天庭法域策略。"
  - "趙受益已以本人名義借出一柄名下佩劍；花滿樓稱為『人皇天子劍』，未證有斬仙法力。"
unresolved:
  - "真名／原籍仍未公開"
  - "青雀初八是否赴約"
  - "商會授信與大宅履約爭議"
  - "天庭是否來、如何來"
  - "照夜初十首夜結果"
  - "沉香所在"
locks:
  - "PLAYER_MAJOR_ACTION_REMAINS_PLAYER_CONTROLLED"
  - "TEST_NOT_CANON"
  - "UNDECIDED_NOT_PREDECIDED"
```

## 潘金蓮

```yaml
relation_to_route: "觀止大掌櫃／營運、契約、制度與商業合作節點"
evidence_event_ids: [E03, E04, E07, E08, E09, E11, E12, E13, E21, E22, E23, E25, E34, E35, E36, E38, E41, E42, E43]
current_route_state:
  - "已核發菊月初八瓦舍老說書先生一次性特別通行帖；趙受益已同意。"
  - "照夜／楊蓮娘的自由身妓籍CURRENT已辦妥；與照夜共同決定菊月初十夜做首次正式一夜競拍。"
  - "負責照夜宣傳與營業邊界；『自願賣身』只作風月市場宣傳，不改自由身。"
  - "仍管理觀止大堂、仕女夜、追雙姝專案帳與其他樓內營運。"
unresolved:
  - "照夜首夜起拍價、分帳與流程細節"
  - "初八仕女夜實際發展"
  - "大堂其他營運線"
locks:
  - "SHOPKEEPER_ROLE_NE_PRIVATE_RELATION"
  - "PAYMENT_NE_CONSENT"
```

## 龐春梅

```yaml
relation_to_route: "觀止掌櫃／秩序、空間與營運節點"
evidence_event_ids: [E11, E13, E22, E23, E25]
current_route_state:
  - "參與仕女夜巷與早期制度設計；初三夜曾以職務位置制止紫蘭、浮香實體衝突。"
  - "『五萬兩私奔案』公告中被戲稱為追捕者，但公告情節本身是玩笑。"
unresolved:
  - "後續營運與人物衝突調度"
locks:
  - "JOKE_NOTICE_NE_EVENT_TRUTH"
```

## 蘇清

```yaml
relation_to_route: "仕女夜制度／商業模型與秘密談話協作人物"
evidence_event_ids: [E13]
current_route_state:
  - "早期參與仕女夜商業模型與劉娥來源秘聞私談。"
locks:
  - "DISCUSSION_NE_PRIVATE_RELATION"
```

## 宋蕙蓮

```yaml
relation_to_route: "觀止人物／大堂閒談圈之一"
evidence_event_ids: [E21]
current_route_state:
  - "初三午後參與花滿樓身世、財務與詞曲閒談；無來源知道沈如晦私密事件。"
locks:
  - "DIRECTOR_KNOWLEDGE_NE_CHARACTER_KNOWLEDGE"
```

## 李桂姐

```yaml
relation_to_route: "觀止大堂營業人物"
evidence_event_ids: [E02, E22]
current_route_state:
  - "早期大堂營業；初三夜曾在女客路由中明確制止把女客誤認為妓女。"
locks:
  - "SAME_VENUE_NE_PLAYER_RELATION"
```

## 醉花

```yaml
relation_to_route: "酒務／產品研發／空間與藝事合作節點"
evidence_event_ids: [E02, E07, E10, E22, E23, E25, E42, E43]
current_route_state:
  - "早期有西側半圓高台酒吧構想。"
  - "菊月初六入夜以盲飲測試花滿樓；以無名酒讓趙受益試飲，因其第一句『晚來得正好』建立底酒《晚來》。"
  - "收花滿樓20兩作研發資金，研發以《晚來》為底的新式調飲；花滿樓取得該調飲冠名權。"
  - "新式調飲CURRENT全名《遲到的正義～去你娘的玉皇大帝，有本事來抓我》；不等於趙受益御賜酒名。"
unresolved:
  - "調飲最終配方、正式售價、限量與銷售制度"
locks:
  - "RND_INVESTMENT_NE_GUANZHI_CLIENT_SPEND"
  - "GUANJIA_DRANK_NE_IMPERIAL_GRANT"
```

## 十三娘

```yaml
relation_to_route: "觀止賭局／客人心理與紀錄協作人物"
evidence_event_ids: [E22, E23, E25]
current_route_state:
  - "初三夜參與高級賭局構想、雙魁夜鬥分段募資與名單登記；在戲謔私奔公告上簽名。"
unresolved:
  - "高級私人賭局尚未正式建成"
locks:
  - "DESIGN_NE_OPERATION"
```

## 白三娘

```yaml
relation_to_route: "觀止歌者／《蝶戀花·薄櫻》主要演唱方向人物"
evidence_event_ids: [E21, E22, E23, E25]
current_route_state:
  - "被花滿樓判斷較能唱出《薄櫻》的風霜味；《薄櫻》贈觀止使用。"
  - "初三夜曾介入紫蘭、浮香衝突勸架，後被捲入拉扯；也簽戲謔公告。"
unresolved:
  - "《薄櫻》後續正式演出與觀眾反應"
locks:
  - "ART_ROLE_NE_PRIVATE_RELATION"
```

## 浮香

```yaml
relation_to_route: "觀止琴妓／與花滿樓有一次已完成成人事件及持續張力，無固定關係"
evidence_event_ids: [E02, E03, E04, E10, E22, E23, E24, E25, E27, E28, E29, E30, E32, E42, E43]
current_route_state:
  - "初三夜與紫蘭因曲藝、注意力與故意挑釁爆發實體衝突，雙方輕傷；停手不等於和好。"
  - "菊月初四夜主動靠近花滿樓，後自願赴鬼滿樓；確認對花滿樓『有一點』實際吸引／興趣。"
  - "在鬼滿樓同床後先設定界線，之後自行明確改變當下意願，與花滿樓完成一次雙方同意的成人事件。"
  - "《紅透清早》專屬演唱權已給浮香；後續身體界線回到每次當下意願。"
  - "菊月初六入夜參與《晚來／遲到的正義》與照夜故事討論。"
  - "紫蘭／浮香『求贖身嫁花滿樓』壓力測試屬隔離TEST，從未在正式線發生。"
unresolved:
  - "是否再有成人事件／戀愛／合作"
  - "與紫蘭競爭或合作如何發展"
locks:
  - "PAST_ADULT_EVENT_NE_FUTURE_CONSENT"
  - "TEST_NE_ROUTE_EVENT"
  - "ATTRACTION_NE_RELATION"
```

## 小翠

```yaml
relation_to_route: "觀止營業人物"
evidence_event_ids: [E22]
current_route_state:
  - "初三夜自己接住一桌客，客人讓她自選曲，演唱從不穩逐漸唱穩。"
```

## 紅娘氏

```yaml
relation_to_route: "媒婆／趙公子追雙姝專案統籌與趙受益訓練者"
evidence_event_ids: [E22, E36, E38, E41, E44]
current_route_state:
  - "初三夜另有大堂調停工作。"
  - "趙公子追雙姝專案成立後，負責趙受益本人訓練與三路協調。"
  - "菊月初六入夜參與瓦舍老說書先生初八特別通行帖安排。"
  - "趙受益借劍時在場。"
unresolved:
  - "追雙姝第一階段是否形成任何自願私情／親密"
locks:
  - "MEDIATOR_NE_CONSENT"
```

## 青禾

```yaml
relation_to_route: "觀止服務人物"
evidence_event_ids: [E22]
current_route_state:
  - "初三夜把腿背不適的熟客帶去做腿腳放鬆服務。"
```

## 趙受益

```yaml
relation_to_route: "大宋官家／追雙姝專案主角／花滿樓法域策略的重要人間權力節點"
evidence_event_ids: [E34, E35, E36, E38, E41, E42, E44]
current_route_state:
  - "同夜匿名在觀止，後以足以讓賭局採計的方式承認／默認官家本人到場。"
  - "楊玉環、趙飛燕均實際到場；追雙姝專案成立，趙受益以私人財物把專案資本補足至100兩等值。"
  - "同意菊月初八老說書先生跟隨公開行程記錄。"
  - "初飲醉花無名酒，第一句為『這酒……倒是晚來得正好。』；此話成為《晚來》命名來源。"
  - "菊月初六夜以本人名義留下『佩劍一柄，借花滿樓暫持。趙受益。菊月初六夜。』並命管事取名下可核佩劍。"
unresolved:
  - "初八雙姝專案結果"
  - "借出的具體佩劍哪一柄／物理交付細節"
  - "對天庭後續若實際介入時的具體行動"
locks:
  - "PRIVATE_SUPPORT_NE_STATE_FUNDS"
  - "SWORD_LOAN_NE_WAR_DECLARATION"
  - "DRANK_WINE_NE_IMPERIAL_GRANT"
```

## 顧青簡

```yaml
relation_to_route: "定陶商會固定商務／文書／帳務聯絡人"
evidence_event_ids: [E40]
current_route_state:
  - "承接花滿樓約5700兩新財富配置：5000死存、500活存、200隨身（後者V1.13已降為180）。"
  - "提出以5000死存作擔保之4500授信上限方向；商會尚未正式批准。"
  - "正在回查父親五萬兩舊契與大宅折息履約爭議。"
unresolved:
  - "4500授信正式批准"
  - "大宅修繕責任"
  - "能否換宅／改付現銀"
  - "父親舊契精確文字"
locks:
  - "PROPOSED_CREDIT_NE_APPROVED"
  - "MERCHANT_GUILD_COUNTERPARTY_PRIMARY"
```

## 楊玉環

```yaml
relation_to_route: "追雙姝專案目標人物之一／自主參與者"
evidence_event_ids: [E34, E35, E36]
current_route_state:
  - "本人到觀止並帶隊抓出匿名官家；自願至少留至菊月初八仕女夜再評估。"
  - "沒有因專案、募款或官家身分形成成人／宮廷承諾。"
unresolved:
  - "初八是否與趙受益形成任何進一步關係"
locks:
  - "PROJECT_NE_CONSENT"
  - "STAY_NE_ROMANCE"
```

## 王婆

```yaml
relation_to_route: "趙公子追雙姝專案楊玉環線媒婆"
evidence_event_ids: [E36, E38]
current_route_state:
  - "與紅娘氏、薛嫂分工；首輪工作費800文曾提出，但V1.12不自動算已支付。"
unresolved:
  - "楊玉環線實際工作成果"
  - "工作費結算"
locks:
  - "MEDIATOR_NE_TARGET_DECISION"
```

## 薛嫂

```yaml
relation_to_route: "媒婆；另有五女看郎線；追雙姝專案趙飛燕線負責人"
evidence_event_ids: [E32, E36, E38]
current_route_state:
  - "菊月初五已有五女看郎會另一路線，不得吞掉花滿樓初八既有前約。"
  - "追雙姝專案中負責趙飛燕線；首輪工作費500文方案不自動算已付。"
unresolved:
  - "兩條媒婆線後續成果"
locks:
  - "SEPARATE_PROJECTS_STAY_SEPARATE"
```

## 舍方知

```yaml
relation_to_route: "LCAPG 裁縫資源，尚無正式本線入場"
evidence_event_ids: []
current_route_state:
  - "E16／V1.6僅被提及可研究七張異鄉女衣樣板；未建立正式見面。"
unresolved:
  - "是否實際見花滿樓／看樣板"
locks:
  - "RESOURCE_MENTION_NE_ROUTE_ENTRY"
```

## 照夜／三聖母

```yaml
relation_to_route: "人間安身約相對人／觀止自由身妓女／初十首夜競拍主角"
evidence_event_ids: [E08, E09, E13, E42, E43, E44]
current_route_state:
  - "神話真身華山三聖母；觀止花名照夜；北宋官面姓名楊蓮娘。"
  - "桂月二十五最初只有官面草案；到菊月初六已經過約十日，依本線時間推移校正，文牒與自由身妓籍已在鏡頭外正常行政流程辦妥並送回觀止。"
  - "與潘金蓮定菊月初十夜舉行首次正式一夜競拍；最高價不等於強制成交，本人保留最終拒客權。"
  - "宣傳主軸：『華山三公主／前朝公主／自願賣身』；其中賣身是市場語，不是奴籍。"
  - "接受花滿樓為她寫的出道詞（『多少往事…不如歸去』）；公開邊界由照夜本人決定。"
  - "公開尋沉香：傳達『他母親仍活著、在汴京觀止、花名照夜』；沉香是否得知未定。"
  - "參與《遲到的正義》試飲；天庭追捕尚未發生。"
unresolved:
  - "沉香所在"
  - "天庭是否來、派誰、用兵或用法"
  - "初十競拍買家／成交價／是否成交"
  - "人間安身約最終履約"
locks:
  - "FREE_PERSON_NE_SLAVE"
  - "FIRST_NIGHT_AUCTION_NE_FORCED_SALE"
  - "MYTHIC_IDENTITY_NE_HUMAN_REGISTRATION"
  - "HEAVEN_RESPONSE_PENDING"
```

## 紫蘭

```yaml
relation_to_route: "觀止主唱歌妓／花滿樓詞曲合作人物／與浮香具競爭張力"
evidence_event_ids: [E02, E03, E04, E10, E17, E21, E22, E23, E24, E25, E27, E32, E42, E43]
current_route_state:
  - "持《鮮花滿月樓》詞稿並完成首次公開試唱；菊月初三夜達成三次真實叫回，花滿樓正式交付《采桑子·夢回謝橋》。"
  - "與浮香初三夜因曲藝與注意力爆發實體衝突；停手後仍保留競爭／合作接口。"
  - "本人自由身；五萬兩不是贖身價。『五萬兩私奔案』是全樓戲謔公告，不是真事。"
  - "菊月初五提出想見鬼滿樓女鬼陸蘅，與初八其他前約分離。"
  - "菊月初六入夜參與醉花新酒與照夜出道詞討論。"
unresolved:
  - "與浮香合作／競爭後續"
  - "見陸蘅之邀是否實現"
  - "初八相關安排"
locks:
  - "FREE_PERSON_NE_REDEMPTION_PROPERTY"
  - "JOKE_NOTICE_NE_REAL_ELOPEMENT"
  - "TEST_NE_ROUTE_EVENT"
```

---

## 3.2｜ROUTE-LOCAL／外部人物履歷

### 小桃

```yaml
evidence_event_ids: [E02, E08, E13, E16, E21, E22]
current_route_state: "觀止跑堂／傳話節點；E16有一次花滿樓突來親吻，她明顯驚訝生氣；不構成戀愛或未來接近權。"
```

### 青衣

```yaml
evidence_event_ids: [E02, E03, E04, E10, E21, E22, E24]
current_route_state: "觀止曲藝協作人物；參與《鮮花滿月樓》《陽關三疊》等排練與演出。"
```

### 柳黃

```yaml
evidence_event_ids: [E02, E03, E04, E10, E21, E22, E24]
current_route_state: "觀止曲藝協作人物；參與《鮮花滿月樓》《陽關三疊》等排練與演出。"
```

### 沈夫人

```yaml
evidence_event_ids: [E05]
current_route_state: "《滿庭芳·家後》委託人；200兩契約的20兩潤筆／180兩賀禮結構成立。"
```

### 阿蘅／陸夫人（桂月二十二客人）

```yaml
evidence_event_ids: [E06]
current_route_state: "桂月二十二女客；收兩首題贈並與花滿樓有一次自願短吻。不得與後來鬼滿樓女鬼陸蘅自動合併。"
```

### 王昭君

```yaml
evidence_event_ids: [E10]
current_route_state: "《陽關三疊》與跨時代藝事線人物；無花滿樓私人關係。"
```

### 鈴娘

```yaml
evidence_event_ids: [E10]
current_route_state: "《昭君出塞》戲曲／藝事計畫節點。"
```

### 青雀

```yaml
evidence_event_ids: [E13]
current_route_state: "菊月初一一炷香相親形成短時親近與初八條件式再見前約；初八是否赴約仍未決。"
```

### 玄燕

```yaml
evidence_event_ids: [E13]
current_route_state: "一炷香相親短場人物；無正式配對或固定後約。"
```

### 白鹿

```yaml
evidence_event_ids: [E13]
current_route_state: "一炷香相親問答／白棋短場；舊結果有作廢修正，不固定勝負或配對。"
```

### 紅綃

```yaml
evidence_event_ids: [E13]
current_route_state: "一炷香相親短場；戲劇性收束不等於正式配對或後約。"
```

### 沈如晦

```yaml
evidence_event_ids: [E13, E14, E15]
current_route_state: "與花滿樓完成一次雙方同意的成人事件後同睡；初二清晨自行離房，無下次成人／戀愛／婚約承諾。"
```

### 未知傳話女子

```yaml
evidence_event_ids: [E16]
current_route_state: "E16替匿名女客傳話／送帖的中介；不是主委託人。"
```

### 龐宜娘／薄櫻

```yaml
evidence_event_ids: [E17, E18, E19]
current_route_state: "真名龐宜娘；『薄櫻』為花滿樓給的私人稱呼。六年帳契談判已完成，三份契據取回；花滿樓作第三方見證，事後有一次自願短吻，無戀愛／長期關係。"
```

### 邵承祿

```yaml
evidence_event_ids: [E18, E19]
current_route_state: "龐宜娘母產舊管理人；已交三份契據，三日內交舊帳，未來只留顧問式看帳方向，無單方處分權。"
```

### 捧帳冊小夥計

```yaml
evidence_event_ids: [E18, E19]
current_route_state: "邵承祿工作助手；知情只到實際工作／見聞範圍。"
```

### 不明男子

```yaml
evidence_event_ids: [E20]
current_route_state: "菊月初三街上三次出現；真實身分、委託人與善惡目的均未定。"
```

### 舊貨攤女攤主

```yaml
evidence_event_ids: [E20]
current_route_state: "以十聲不同方式『娘／媽媽／母親』稱呼換出整只木匣與七張異鄉女衣樣板。"
```

### 藍袍青年

```yaml
evidence_event_ids: [E20]
current_route_state: "舊貨攤交易現場競價／旁觀人物，未形成長線關係。"
```

### 時空道人

```yaml
evidence_event_ids: [E20]
current_route_state: "觀止入口有限介面；給『空囊偏得異鄉物／滿袖無心又惹塵』籤語，不作預言或全知NPC。"
```

### 假箋持有人／買家（未具名）

```yaml
evidence_event_ids: [E26]
current_route_state: "買到偽造《雙魁夜鬥》親見箋；後補30兩取得的是菊月初四新的紀念證明，不得倒寫成前夜親見。"
```

### 陸蘅／阿蘅

```yaml
evidence_event_ids: [E28, E37]
current_route_state: "鬼滿樓已確認女性鬼魂；自述等從軍丈夫多年。春桃可清楚見、石頭見模糊形、許嫂較偏聽／感，阿巧未知。西後院會使她不適／虛弱。"
```

### 許嫂

```yaml
evidence_event_ids: [E31, E37]
current_route_state: "鬼滿樓四僕之一，約40歲寡婦，內宅／家務領頭；有家用預支與木盒埋藏待回報事項。"
```

### 石頭

```yaml
evidence_event_ids: [E31, E37]
current_route_state: "鬼滿樓四僕之一；負責外院／粗活，已搬回舊木馬，白日修繕結果仍待回報。"
```

### 春桃

```yaml
evidence_event_ids: [E31, E37]
current_route_state: "鬼滿樓四僕之一，成年；目前能清楚看見陸蘅。"
```

### 阿巧

```yaml
evidence_event_ids: [E31, E37]
current_route_state: "鬼滿樓四僕之一，成年；是否能感知陸蘅仍未知。"
```

### 姚安娘

```yaml
evidence_event_ids: [E32]
current_route_state: "菊月初五街上再會；第三次相逢通道已留下，後續未決。"
```

### 祝惟實

```yaml
evidence_event_ids: [E33]
current_route_state: "提供舊木馬來源線與窄長木盒；其父曾修木馬，不等於製作者。"
```

### 范姓男子

```yaml
evidence_event_ids: [E33]
current_route_state: "付5兩要求窄長木盒子時前不開；限制已屆期，動機與盒中內容未知。"
```

### 蘇東坡

```yaml
evidence_event_ids: [E34, E35, E39]
current_route_state: "因肉香進觀止，參與官家局；後到瓦舍可證官家、楊玉環、趙飛燕昨夜在場，但不能證『侍』字從一開始就是侍。"
```

### 趙飛燕

```yaml
evidence_event_ids: [E35, E36]
current_route_state: "本人到觀止，與楊玉環共同使八門到場局成『全來』；自願留至初八仕女夜再評估，追雙姝專案趙飛燕線由薛嫂負責。"
```

### 瓦舍老說書先生

```yaml
evidence_event_ids: [E39]
current_route_state: "瓦舍合作人；托計畫全程未實際喊價，已收10兩保密＋善意。菊月初八取得觀止一次性特別紀錄通行資格，正式工作費未定。"
```

### 瓦舍掌事

```yaml
evidence_event_ids: [E39]
current_route_state: "與花滿樓談妥門票與原牌拍賣分成；原牌6000兩成交，瓦舍一成600兩。"
```

### 匿名買家代理／競價者

```yaml
evidence_event_ids: [E39]
current_route_state: "原牌6000兩成交之買方代理／競價方；買家真實身份仍未知。"
```

### 趙受益管事

```yaml
evidence_event_ids: []
current_route_state: "受趙受益命令去取其名下可確認來歷的佩劍；具體哪一柄與最終物理交付仍待正面描寫。"
```

---

# 4｜LCAPG 71 人對齊清冊｜V10 CURRENT

```yaml
LCAPG_71_ALIGNMENT_AT_V10:
  - {order: 1, name: "潘金蓮", state: ACTIVE_ROUTE_CHARACTER}
  - {order: 2, name: "李瓶兒", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 3, name: "龐春梅", state: ACTIVE_ROUTE_CHARACTER}
  - {order: 4, name: "蘇清", state: ACTIVE_ROUTE_CHARACTER}
  - {order: 5, name: "阿麗婭", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 6, name: "張麗華", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 7, name: "宋蕙蓮", state: ACTIVE_ROUTE_CHARACTER}
  - {order: 8, name: "李桂姐", state: ACTIVE_ROUTE_CHARACTER}
  - {order: 9, name: "紅袖", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 10, name: "疏影", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 11, name: "醉花", state: ACTIVE_ROUTE_CHARACTER}
  - {order: 12, name: "十三娘", state: ACTIVE_ROUTE_CHARACTER}
  - {order: 13, name: "白三娘", state: ACTIVE_ROUTE_CHARACTER}
  - {order: 14, name: "浮香", state: ACTIVE_ROUTE_CHARACTER}
  - {order: 15, name: "小翠", state: ACTIVE_ROUTE_CHARACTER}
  - {order: 16, name: "李媽媽", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 17, name: "安舟", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 18, name: "汪鹽商", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 19, name: "辭歲", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 20, name: "貂蟬", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 21, name: "紅娘氏", state: ACTIVE_ROUTE_CHARACTER}
  - {order: 22, name: "李師師", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 23, name: "青禾", state: ACTIVE_ROUTE_CHARACTER}
  - {order: 24, name: "六條御息所", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 25, name: "李清照", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 26, name: "趙受益", state: ACTIVE_ROUTE_CHARACTER}
  - {order: 27, name: "錦棠", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 28, name: "顧青簡", state: ACTIVE_ROUTE_CHARACTER}
  - {order: 29, name: "楊玉環", state: ACTIVE_ROUTE_CHARACTER}
  - {order: 30, name: "柳如是", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 31, name: "薛濤", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 32, name: "魚玄機", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 33, name: "失仙", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 34, name: "失美", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 35, name: "失蘿", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 36, name: "錯位", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 37, name: "香雲", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 38, name: "花晨", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 39, name: "艷芳", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 40, name: "玉香", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 41, name: "瑞珠", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 42, name: "瑞玉", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 43, name: "顧仙娘", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 44, name: "王婆", state: ACTIVE_ROUTE_CHARACTER}
  - {order: 45, name: "林太太", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 46, name: "王六兒", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 47, name: "吳銀兒", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 48, name: "薛嫂", state: ACTIVE_ROUTE_CHARACTER}
  - {order: 49, name: "吳月娘", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 50, name: "孟玉樓", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 51, name: "孫雪娥", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 52, name: "李嬌兒", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 53, name: "鄭愛月", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 54, name: "白玉潔", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 55, name: "張明姝", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 56, name: "孫清倩", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 57, name: "沈玉晶", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 58, name: "高承義", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 59, name: "李明遠", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 60, name: "王慎行", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 61, name: "王廷衡", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 62, name: "舍方知", state: BASE_RESOURCE_MENTION_ONLY_NOT_ROUTE_ENTRY}
  - {order: 63, name: "關盼盼", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 64, name: "夏蓮／趙姬", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 65, name: "玉堂春／蘇三", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 66, name: "照夜／三聖母", state: ACTIVE_ROUTE_CHARACTER}
  - {order: 67, name: "紫蘭", state: ACTIVE_ROUTE_CHARACTER}
  - {order: 68, name: "西門慶", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 69, name: "應伯爵", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 70, name: "高衙內", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
  - {order: 71, name: "陳敬濟", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE}
```

> `ACTIVE_ROUTE_CHARACTER` 表示在 E01–E44 至少已有本線事件證據；不等於與花滿樓有私人關係。
> `BASE_RESOURCE_MENTION_ONLY_NOT_ROUTE_ENTRY` 表示只被當世界資源提及（目前為舍方知），未建立正式入場。
> `BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE` 表示人物池存在，但截至 HOT V1.13 沒有足夠證據建立花滿樓線出場。

---

# 5｜CURRENT 關係／知情／契約交叉索引

```yaml
CROSS_AXIS_CURRENT:
  花滿樓_浮香:
    state: "一次已完成成人事件 + 實際吸引／張力；無戀愛、婚姻、排他或下一次成人權利"
    locks: [PAST_CONSENT_NE_FUTURE_CONSENT, TEST_REDEMPTION_MARRIAGE_NE_CANON]
  花滿樓_照夜:
    state: "人間安身約相對人；照夜已正式自由身入妓籍；初十首夜拍賣另有舊三成條件約定；未履約成人酬謝"
    locks: [CONTRACT_NE_BODY_ACCESS, FIRST_NIGHT_AUCTION_NE_FORCED_SALE]
  花滿樓_紫蘭:
    state: "詞曲合作／市場與競爭互動；無戀愛、婚姻、成人或排他關係"
    locks: [LYRIC_NE_ROMANCE, FREE_PERSON_NE_REDEMPTION_PROPERTY]
  花滿樓_青雀:
    state: "初八條件式再見前約；到場未定"
    locks: [INVITE_NE_ARRIVAL]
  花滿樓_沈如晦:
    state: "一次已完成成人事件；無後續承諾"
    locks: [PAST_ADULT_EVENT_NE_FUTURE_CONSENT]
  趙受益_楊玉環_趙飛燕:
    state: "追雙姝專案進行中；初八前均無成人／宮廷結果"
    locks: [PROJECT_NE_CONSENT, FUNDING_NE_ACCESS]
  照夜_天庭:
    state: "追捕／法域衝突仍未決；人間身分與妓籍已成立，但不自動消滅仙界主張"
    locks: [MYTHIC_IDENTITY_NE_HUMAN_REGISTRATION, HEAVEN_RESPONSE_PENDING]
  花滿樓_趙受益_借劍:
    state: "趙受益本人名義借出佩劍成立；具體佩劍與物理交付細節待正面描寫；無斬仙神力證據"
    locks: [SWORD_LOAN_NE_WAR_DECLARATION, SYMBOL_NE_SUPERNATURAL_POWER]
```

---

# 6｜V10 CURRENT RESUME 人物層

- **花滿樓**：觀止大堂／門口；隨身現銀控制數180兩。
- **潘金蓮**：掌櫃；老說書先生初八通行帖已核；照夜初十首夜拍賣已定。
- **照夜／楊蓮娘**：自由身妓籍完成；初十首夜拍賣；出道與尋沉香宣傳進行；天庭反應未決。
- **醉花**：持20兩研發款；《晚來》與《遲到的正義》研發線進行。
- **紫蘭／浮香**：均在大堂活動；兩人競爭／合作張力仍在；贖身嫁娶TEST不屬故事。
- **趙受益**：追雙姝專案主角；已同意說書先生跟行；已寫借劍字據並命取名下佩劍。
- **楊玉環／趙飛燕**：自願至少留至初八仕女夜後再評估。
- **紅娘氏／王婆／薛嫂**：三路媒婆分工有效。
- **顧青簡**：商會資產／舊契爭議線持續；4500授信仍未正式核准。
- **鬼滿樓**：陸蘅、許嫂、石頭、春桃、阿巧線仍活；木盒埋藏回報、木馬修繕、西後院等仍未決。

---

# 7｜編譯驗證

```yaml
COMPILE_STATS:
  memory_generation: "V10"
  master_event_range: "E01-E44"
  inherited_event_ids: 18
  new_index_event_ids: 26
  aligned_character_base_count: 71
  route_local_records_compiled: true
  latest_hot: "V1.13"

VALIDATION:
  master_rcl_generation_match: "PASS / V10"
  master_pair_version: "PASS / V10-HARD"
  lcapg_alignment_count: "PASS / 71"
  old_rcl_v1_5_used_as_historical_character-ledger basis: true
  e19_e44_marked_as_compile_time_index_ids: true
  test_promoted_to_world_fact: false
  undecided_states_preserved: true
  later_status_does_not_retroactively_rewrite_earlier_knowledge: true
```

---

# RCL 責任聲明

本檔與 MASTER V10-HARD 構成花滿樓線目前的 **MASTER SAVE 雙檔配對**：

1. **MASTER V10-HARD**：保存事件正文、因果、帳務、契約、作品、未決與 HOT V1.6–V1.13 完整歷史。
2. **RCL V10-HARD**：保存 E01–E44 的事件↔人物索引，以及各人物截至 HOT V1.13 的路線履歷、關係、知情、契約與未決狀態。

本檔不表示 Host SAVE commit、Project installation、Main／Lighter 外部執行回執或獨立多模型 Agent 執行已發生。
