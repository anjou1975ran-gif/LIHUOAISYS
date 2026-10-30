# 觀止青樓｜安竹君線｜原生人物 ROUTE SAVE V0.1
## 初始登記：賀小滿（NPC_LOCAL_001_HE_XIAOMAN）

**初始建檔日期：** 2026-10-30（現實作業日；非觀止劇中日期）  
**Route ID：** `GUANZHI_ANZHUJUN_ROUTE`  
**存放位置：** `觀止青樓/SAVE/安竹君線/原生人物_SAVE.md`  
**基礎模板：** `觀止青樓/V6觀止青樓/V3.0.0/觀止青樓原生人物 ROUTE SAVE 模板.md`  
**來源：** 已正式保存的安竹君線 HOT V1.1 與承接之 HOT V1.2，不依導演事後猜測補寫。  
**授權：** 玩家於 HOT V1.2 存檔後明示建議「在安竹君的SAVE裡面增加一個原生人物存檔，賀小滿就可以放進去，未來等她故事線豐滿了就能進大池」，本次依此新增檔案。  
**法位：** `HUMAN_AUTHORIZED / ROUTE_LOCAL_CHARACTER_SAVE / NOT_SHARED_POOL / NOT_MASTER / NOT_WORLD_CANON`。本檔只是已實際建立的當線原生人物資料，**沒有將賀小滿寫進共用 73 人物池，也沒有修改任何既存 HOT SAVE**。

> **設計用途：** HOT SAVE 保存事件斷點；此檔按原生人物逐項累積能追溯的身份、行動、聲紋、關係與未知。新人物有資格成為持續角色時可新增本檔條目；未經選角查證，不將所有臨場無名群眾自動升格。將來若提出共用池入池案，須另外明確審核可跨線的「人物基線」與只屬安竹君線的「歷史增量」，並取得人類批准、實際寫入。

---

## 1｜原生人物總表

| route-local ID | 當線姓名／稱呼 | 最初場景 | 最近可確認動向 | 人物池法位 |
|---|---|---|---|---|
| `NPC_LOCAL_001_HE_XIAOMAN` | 賀小滿／小滿 | 理火三年・吉月二十八戌時，觀止大堂 | 第二局勝後攜五十兩及琵琶往側廊後堂，去收琴／更弦；之後未見有可靠新出場 | `ROUTE_ONLY / NOT_IN_SHARED_POOL` |

**尚未編成正式人物條目：** 羊肉宴席曾以「翠裙、藕荷衫、桃紅衫、杏黃衫、月白衫」等衣色稱呼的無名成年女子，現階段是當線出場人物／群眾，尚無正式名稱及可穩定對應的 local ID；不得偷認她們是賀小滿或共用池既有具名角色。日後若重逢並形成可靠身份，應先核對既有池與當線資料，再依合格證據建檔。

---

## 2｜NPC_LOCAL_001_HE_XIAOMAN｜賀小滿

```yaml
ORIGINAL_CHARACTER_ROUTE_SAVE:
  route_id: "GUANZHI_ANZHUJUN_ROUTE"
  local_id: "NPC_LOCAL_001_HE_XIAOMAN"
  name:
    current: "賀小滿"
    aliases: ["小滿"]
    naming_source: "本人於第二局猜客賭約勝後，當面自報『奴家姓賀，名小滿。觀止的人都叫我小滿。』"
    surname_rule_checked: true
    given_name_warning_char_rule_checked: true
    naming_rule_note: "賀不在禁用十姓；小滿不含十六個名字警戒字；既存 HOT V1.1 姓名不得追溯更改"
  first_entry:
    scene: "觀止大堂，安竹君與潘金蓮談話之際"
    time_precision: "理火三年・吉月二十八・戌時；未鎖定更細時刻"
    location: "觀止青樓大堂、櫃台附近"
    evidence: "安竹君線 HOT SAVE V1.1 §3.1"
  person:
    confirmed_adult: true
    appearance_observed: ["成年女子", "藕色衣裙", "抱琵琶"]
    occupation_claimed: "觀止的人稱其小滿；具體職稱未核"
    occupation_verified: "於觀止大堂有公開琵琶演奏；有人在後堂催其收琴與更弦"
    legal_and_social_status: "妓籍／掛牌／是否受雇／家庭契約／具體年齡均 UNKNOWN"
    abilities_demonstrated: ["在堂中演奏琵琶", "當場理解、談判並挑戰猜客賭約條款", "能堅持辨明賭局判定條件"]
    voice_or_gesture_observed: ["言語爽快，好勝而重規則", "不喜刻意讓棋或紅眼亂賭", "既可認真親吻，也可當場將親吻與感情承諾分清"]
    habits_observed: []
    source_history_confirmed: []
    speculation_not_fact:
      - "自稱父親曾沉迷賭博、輸掉家中冬衣等財物；目前僅確認她作此自述，未完成家世外部查證"
      - "她是否有愛而不得之人，未說明"
      - "沒有證據證明她因一吻而愛上安竹君"
    ambitions: []
    private_desires: "UNKNOWN；當場肯參與賭約與爭取五十兩，不推出長期人生目標"
    intimacy_tags:
      status: "LOCAL_EVENT_ONLY"
      tags: ["吉月二十八：當次自願公開親吻安竹君一次；無後續性事／固定伴侶承諾"]
  relations:
    confirmed_links:
      - "安竹君：吉月二十八新相識；兩次賭約，一次公開親吻，第二局取得五十兩"
      - "潘金蓮：同在大堂見證或討論賭局判定；具體私下關係 UNKNOWN"
      - "觀止後堂工作接點：曾有人催她收琴更弦；該人姓名與上下級關係 UNKNOWN"
    unverified_claims: ["父親昔日賭博家史為賀小滿自述，尚未有獨立證據"]
  knowledge:
    this_character_knows:
      - "安竹君曾以五十兩為賭注試探她"
      - "安竹君曾明言希望在女子一生中留下難忘印記"
      - "安竹君談過風月場不必追問彼此往昔情史"
    player_knows:
      - "她自報姓賀、名小滿"
      - "她會彈琵琶、喜歡公平認真的較量，曾提到父親賭博"
      - "她當夜確實獲得並帶走五十兩"
      - "她不願透露自己是否曾有愛而不得之人"
    others_know:
      - "潘金蓮在場知悉至少兩局賭約及賀小滿的當場回應"
    director_confirmed:
      - "首局吻已發生、銀錠未轉移"
      - "第二局金錢交付完成、未發生第二吻或陪宿"
  continuity:
    current_location: "上次可靠目擊為大堂往側廊後堂；至雪月初一天明時確切位置 UNKNOWN"
    last_observed_event: "第二局勝後，她攜一錠五十兩與琵琶離開大堂，後堂有人催收琴／更弦"
    property_or_money_confirmed: ["安竹君於吉月二十八第二局輸給並交付五十兩銀錠；賀小滿當場收妥攜走；日後如何保管或消費未知"]
    unresolved_threads:
      - "她是否會與安竹君再見，未決"
      - "她過往的感情史及父親賭博家史未查證"
      - "在觀止的具體身份、工作條件、人際網絡與人生計畫尚未確立"
    open_questions:
      - "姓名是否有正式契據來源、精確年齡、入樓緣由"
      - "琵琶造詣／經歷、樓內工作與收入安排"
      - "與其他人物的長期關係，以及她自己的計畫"
  state:
    route_only: true
    shared_pool: "NOT_PROPOSED"
    save_write: "GITHUB_FILE_CREATED"
```

### 2A｜按時間的事件 Delta（均為安竹君線）

| Delta | 場景／時段 | class | 已成立的觀察／其界線 | 主要來源 |
|---|---|---|---|---|
| HX-001 | 吉月二十八・戌時，大堂 | ESTABLISHED_ACTION | 琵琶演奏後抱琴經過，主動詢問安竹君會否雙陸等；當時未報姓名 | HOT V1.1 §3.1 |
| HX-002 | 同夜，大堂 | ESTABLISHED_SPEECH | 說父親曾賭輸家中財物、不喜刻意讓棋；**僅保證自述發生** | HOT V1.1 §3.1 |
| HX-003 | 同夜，第一局 | ESTABLISHED_ACTION | 最終談妥「五十兩對公開一吻」；她押下一組入門客人兩人以上，實際只有一名青袍男子，故賭輸並當眾自願親吻；五十兩沒有轉給她 | HOT V1.1 §3.2 |
| HX-004 | 同夜，第二局協商 | ESTABLISHED_ACTION | 首批兩位女客只預約明日席位，雙方因資格歧義同意改以「今夜入場消費」為判定；**不算她已贏過兩筆五十兩** | HOT V1.1 §3.3 |
| HX-005 | 同夜，第二局 | ESTABLISHED_ACTION | 兩位結伴男客入門並點酒菜，符合新條件；賀小滿勝、實收並攜走五十兩；此局**沒有第二吻** | HOT V1.1 §3.3 |
| HX-006 | 同夜，離席前 | ESTABLISHED_SPEECH | 親自報名「賀小滿／小滿」；不回答過去是否有愛而不得之人；親吻與錢分局結清 | HOT V1.1 §3.3 |
| HX-007 | 同夜，大堂至側廊 | ESTABLISHED_ACTION | 因後堂催促，抱琴、帶銀錠往後堂去；此後沒有可靠回場鏡頭 | HOT V1.1 §3.3 |
| HX-008 | 雪月初一・天明（日結） | CONTINUITY_ONLY | HOT V1.2 承接小滿已獲五十兩及此前行動；**沒有替她新創夜間行為、位置或感情變化** | HOT V1.2 §6 |

### 2B｜身份與「可入共用人物池」必須分離

```yaml
POOL_PROMOTION_CANDIDATE:
  original_route_id: "GUANZHI_ANZHUJUN_ROUTE"
  original_local_id: "NPC_LOCAL_001_HE_XIAOMAN"
  portable_shared_baseline: []
  route_specific_events_not_to_import:
    - "安竹君線的第一局公開親吻及第二局五十兩賭金"
    - "安竹君與賀小滿的特定對話、認知、私人關係與期待"
    - "安竹君線之任何後續未成立或未經證實的事"
  name_and_identity_checked: false
  author_decision: "PENDING"
  actual_pool_write: "NOT_DONE"
```

**未來升格建議程序（尚未觸發）：** 她若在本線累積足夠可追溯的人格、職業、能力、社會位置與生活選擇，再向人類提出「可攜基線／本線專屬歷史」的對照候選；**人類批准之後**才實際編入 73 人共用池或其後繼版。候選入池不會抹掉這份 Route SAVE，也不讓其他 Route 自動繼承安竹君線的五十兩、親吻與個別情史。

---

## 3｜後續記錄紀律

- **新增事件**：有來源的當線新互動才增一條 Delta；寫明時間精度、當事人、完成／未決、得知者與 HOT 來源，不為了豐滿背景而編造身世。
- **新增人物**：先按現行 Director 選角規則查 73 人物池與本線已存在人物；若確認為原生人物再配置新 local ID（例如 `NPC_LOCAL_002`），不重用小滿的 ID。
- **不自動改寫**：不以此檔覆蓋 HOT V1.1／V1.2，亦不擅自更新 MASTER、世界規則或人物池。
- **共用池升格**：另需人類明示及實際池檔修改；單純人物戲份增加、玩家喜愛或導演認為成熟，都不等於已經升格。

**END｜ANZHUJUN_ROUTE_LOCAL_ORIGINAL_CHARACTER_SAVE_V0.1｜NPC_LOCAL_001_HE_XIAOMAN**
