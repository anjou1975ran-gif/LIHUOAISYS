# 觀止青樓｜安竹君線｜原生人物 ROUTE SAVE V0.2
## 賀小滿既有卡存續 × 雪月初一三位仕女夜女客追加登記

**初始建檔日期：** 2026-10-30（現實作業日；非觀止劇中日期）  
**Route ID：** `GUANZHI_ANZHUJUN_ROUTE`  
**存放位置：** `觀止青樓/SAVE/安竹君線/原生人物_SAVE.md`  
**基礎模板：** `觀止青樓/V6觀止青樓/V3.0.0/觀止青樓原生人物 ROUTE SAVE 模板.md`  
**初始來源：** 已正式保存的安竹君線 HOT V1.1 與承接之 HOT V1.2；本次新卡另據 HOT V1.3 與其後本對話已敘演事件，不依導演事後猜測補寫。  
**授權沿革：** V0.1：玩家授權賀小滿建卡；V0.2：玩家於本對話明示「可以幫這三個女子建卡 進安竹君線的人物池」，特指雙雙、二姊、許娘子。**本次不授權更新共用73人池、MASTER、WORLD或HOT**。  
**法位：** `HUMAN_AUTHORIZED / ROUTE_LOCAL_CHARACTER_SAVE / NOT_SHARED_POOL / NOT_MASTER / NOT_WORLD_CANON`。本檔只將賀小滿、雙雙、二姊、許娘子登記為安竹君線原生人物，**沒有將任何一人寫進共用 73 人物池，也沒有修改既存 HOT SAVE**。

**V0.2 增補範圍：** 雪月初一仕女夜；依 HOT V1.3 及其後本回合聊天的已敘演觀察增補 NPC_LOCAL_002～004。**HOT V1.3 的凍結時點仍停在競花會首場成交，之後的聊天事件雖可在此 Route 人物卡留下角色增量，但不得假稱 HOT 已同步更新**。現實建卡日期：2026-10-31。

> **設計用途：** HOT SAVE 保存事件斷點；此檔按原生人物逐項累積能追溯的身份、行動、聲紋、關係與未知。新人物有資格成為持續角色時可新增本檔條目；未經選角查證，不將所有臨場無名群眾自動升格。將來若提出共用池入池案，須另外明確審核可跨線的「人物基線」與只屬安竹君線的「歷史增量」，並取得人類批准、實際寫入。

---

## 1｜原生人物總表

| route-local ID | 當線姓名／稱呼 | 最初場景 | 最近可確認動向 | 人物池法位 |
|---|---|---|---|---|
| `NPC_LOCAL_001_HE_XIAOMAN` | 賀小滿／小滿 | 理火三年・吉月二十八戌時，觀止大堂 | 第二局勝後攜五十兩及琵琶往側廊後堂，去收琴／更弦；之後未見有可靠新出場 | `ROUTE_ONLY / NOT_IN_SHARED_POOL` |
| `NPC_LOCAL_002_SHUANGSHUANG` | 雙雙（本人選用的暫稱）／真名 UNKNOWN | 雪月初一仕女夜，內側客用雅間 | 與安竹君互贈詩扇後，仍在觀止大堂附近；持「竹君親贈」題扇 | `ROUTE_ONLY / NOT_IN_SHARED_POOL` |
| `NPC_LOCAL_003_ERJIE` | 二姊（雙雙的姊姊）／真名 UNKNOWN | 雪月初一仕女夜，由大堂尋妹至內側雅間 | 在觀止大堂，與雙雙、許娘子、安竹君同席談詩與姓名 | `ROUTE_ONLY / NOT_IN_SHARED_POOL` |
| `NPC_LOCAL_004_XU_NIANGZI` | 許娘子（席間稱謂）／真名 UNKNOWN | 雪月初一仕女夜，內側客用雅間羊肉席 | 競花會後仍在觀止大堂，與另外兩女客及安竹君談詩 | `ROUTE_ONLY / NOT_IN_SHARED_POOL` |

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


## 3｜NPC_LOCAL_002_SHUANGSHUANG｜雙雙（暫稱／真名未明）

~~~yaml
ORIGINAL_CHARACTER_ROUTE_SAVE:
  route_id: "GUANZHI_ANZHUJUN_ROUTE"
  local_id: "NPC_LOCAL_002_SHUANGSHUANG"
  name:
    current: "UNKNOWN"
    aliases: ["雙雙（本人當場選用的暫時稱呼）"]
    naming_source: "雪月初一仕女夜席間本人允用『雙雙』；此為暫稱，不能回寫成真名"
    surname_rule_checked: false
    given_name_warning_char_rule_checked: false
    naming_rule_note: "沒有正式原創姓名，十姓與警戒字禁則暫不適用；不得自創姓氏取代UNKNOWN"
  first_entry:
    scene: "雪月初一仕女夜，安竹君內側客用雅間羊肉席／女客互動"
    time_precision: "理火三年・雪月初一・晚間，後進至酉時；未核更細起始刻"
    location: "觀止青樓內側客用雅間"
    evidence: "安竹君線 HOT V1.3 §2.1；後續同一聊天已敘演場景"
  person:
    confirmed_adult: true
    appearance_observed: ["淡青綠色帷帽", "白絹團扇", "腕繫紅線"]
    occupation_claimed: "UNKNOWN"
    occupation_verified: "UNKNOWN"
    legal_and_social_status: "仕女夜成年女客，腕繫紅線＝依觀止當晚標示為非妓籍；婚籍、奴籍、家世及職業 UNKNOWN"
    abilities_demonstrated: ["機敏反應與猜謎、對話機鋒", "能自行表明陪伴與不陪睡的界線", "對詩句提出有針對性的理解問題"]
    voice_or_gesture_observed: ["口齒快、愛取笑安竹君『安呆呆』", "有時立刻起鬨，有時面對真情意會暫時沉默", "常用團扇掩笑、遮面", "在眾人前維護自己的選擇，不因姊姊追問便交出真名"]
    habits_observed: ["今晚愛吃杏仁酥", "珍惜原本素白的絹團扇"]
    source_history_confirmed: []
    speculation_not_fact:
      - "四名手足、排行第三與兄姊妹次序，由她在席間自述／姊妹互認；未有外部宗籍查驗"
      - "此前互相親吻一次，不能推定婚姻承諾、長期戀愛、日後同宿"
      - "對安竹君有興趣不等於將來一定告知本名或願再親吻"
      - "HOT V1.1 兩位預訂席位姊妹，尚不足以證明就是雙雙與二姊"
    ambitions: []
    private_desires: "長期 UNKNOWN；今夜曾表明想聽羊村故事、讓安竹君相伴至自己回府，並珍惜題詩團扇"
    intimacy_tags:
      status: "LOCAL_EVENT_ONLY"
      tags:
        - "曾與安竹君在杏仁酥互動時雙方自願親吻一次；此後沒有可核的第二吻"
        - "明說二兩一宵相伴之約不包括陪睡／同宿，亦非永久排他關係"
  relations:
    confirmed_links:
      - "NPC_LOCAL_003_ERJIE：雙方在場互認姊妹，二姊為較年長的姊姊"
      - "安竹君：雪月初一新相識，猜謎、一次雙方自願親吻、二兩請其當晚相伴、接受題詩"
      - "NPC_LOCAL_004_XU_NIANGZI：同在仕女夜羊肉席與大堂競花會交談"
    unverified_claims:
      - "自述家中四手足：長兄、二姊、本人排行第三、幼妹"
  knowledge:
    this_character_knows:
      - "安竹君在席上自述女師爺、敗家比賽、家中長輩欲逼婚與汴梁逃家緣由；事實性仍取決於來源"
      - "安竹君發起一宵競花善會、最後自贖三百兩，並自願替她題扇"
      - "安竹君尊重仕女夜『男不問女名』之規"
      - "她知道團扇上四句詩及『竹君親贈』落款"
    player_knows:
      - "雙雙是本人選用暫稱，尚不知本名"
      - "與二姊的互認關係，以及本人所述兄姊妹次序"
      - "她曾自願親吻一次、以二兩捐銀請自己相伴，但拒絕同宿"
      - "她收下親筆題有四句詩與『竹君親贈』的白絹團扇"
    others_know:
      - "二姊與許娘子見她和安竹君互動、赴大堂觀賽，並當場知道二兩相伴與題扇的部分過程"
      - "龐春梅依故事場景收下雙雙二兩善銀；不能推出她知道所有私語"
    director_confirmed:
      - "『雙雙』不是已查實真名"
      - "二兩善款在戲內已由春梅驗收，另立全數捐米款，不抽會費"
      - "白絹團扇已由安竹君題詩、落款，持有人為雙雙"
  continuity:
    current_location: "最後可確認：雪月初一・酉時漸深，觀止大堂與席間；未演離樓"
    last_observed_event: "收下完成題字的白絹團扇；與安竹君、二姊、許娘子談仕女夜姓名規矩及詩作"
    property_or_money_confirmed:
      - "雙雙以自己的二兩銀子交春梅作新增施粥買米善款；與安竹君相伴至她回府之約已口頭成立"
      - "原有白絹團扇現題四句詩及『竹君親贈』；仍由她持有"
    unresolved_threads:
      - "二兩一宵相伴後續：宵夜與羊村故事尚未演出完成"
      - "何時回府、是否再願意親近、何時願透露本名，皆由她自己決定"
    open_questions: ["姓名、年齡細數、婚籍、家世與職業", "家中四手足身分的外部核對", "她對題詩的長期理解及今後生活"]
  state:
    route_only: true
    shared_pool: "NOT_PROPOSED"
    save_write: "GITHUB_FILE_UPDATED"
~~~

### 3A｜雙雙當線事件 Delta

| Delta | 場景／時段 | class | 已成立觀察／不得推定 | 來源 |
|---|---|---|---|---|
| SS-001 | 雪月初一、內側雅間 | ESTABLISHED_ACTION | 以帷帽、白絹團扇、紅線來席；自用暫稱「雙雙」；享羊肉、杏仁酥 | HOT V1.3 §2.1 |
| SS-002 | 同晚，雅間猜謎 | SELF_REPORT + ACTION | 四手足排行謎由安竹君猜對；她交出未曾告訴他的故事作獎品；無賭金轉移 | HOT V1.3 §2.1 |
| SS-003 | 同晚，杏仁酥席 | ESTABLISHED_ACTION | 雙方自願親吻一次；不構成同宿或婚約 | HOT V1.3 §2.1 |
| SS-004 | 同晚，大堂競花會後 | ESTABLISHED_ACTION | 自行出二兩銀子，請安竹君當晚相伴至她回府；明說不要同宿，春梅將二兩全額入善款 | 本聊天後 HOT V1.3 續演 |
| SS-005 | 同晚，題詩 | ESTABLISHED_ACTION | 安竹君先在素箋寫詩，雙雙允在自己的扇上題寫，最後親收題扇 | 本聊天後 HOT V1.3 續演 |
| SS-006 | 同晚，姓名談話 | ESTABLISHED_SPEECH | 雙雙不公開真名，表示可於自己願意時說；並對安竹君「裝呆」打趣 | 本聊天後 HOT V1.3 續演 |

**扇面完整碑記（原樣保存，不擅改字句）：**

> 十里平湖霜滿天，  
> 寸寸青絲愁華年。  
> 對月形單望相護，  
> 只羨鴛鴦不羨仙。

**落款：竹君親贈。** 這是人物實際持有的物件記憶，不是戀情完成證明。

---

## 4｜NPC_LOCAL_003_ERJIE｜二姊（雙雙的姊姊；真名未明）

~~~yaml
ORIGINAL_CHARACTER_ROUTE_SAVE:
  route_id: "GUANZHI_ANZHUJUN_ROUTE"
  local_id: "NPC_LOCAL_003_ERJIE"
  name:
    current: "UNKNOWN"
    aliases: ["二姊", "雙雙的姊姊", "紅母狼（席間玩笑）"]
    naming_source: "雙雙稱其姊姊；雙方當場互認，並以家中排行『二姊』指稱"
    surname_rule_checked: false
    given_name_warning_char_rule_checked: false
    naming_rule_note: "只有親屬稱謂與玩笑稱呼，真名尚未披露，沒有新創正式姓名"
  first_entry:
    scene: "雪月初一仕女夜，從大堂尋找妹妹到安竹君內側客用雅間"
    time_precision: "理火三年・雪月初一・晚間，未定更細時刻"
    location: "觀止青樓內側客用雅間"
    evidence: "安竹君線 HOT V1.3 §2.2；其後同一聊天已敘演場景"
  person:
    confirmed_adult: true
    appearance_observed: ["淡紫色外衣", "細金釵", "腕繫紅線", "使用團扇"]
    occupation_claimed: "UNKNOWN"
    occupation_verified: "UNKNOWN"
    legal_and_social_status: "成年仕女夜非妓籍女客（依腕繫紅線標示）；真實婚籍、階層、職業、精確年齡 UNKNOWN"
    abilities_demonstrated: ["能就經濟往來細分債務抵銷、收付流水與營業收入", "反問信用時間、還款責任與商家可用資金", "能從口頭約定檢查契約身分與彼此同意", "會欣賞並對詩句提出解讀"]
    voice_or_gesture_observed: ["冷靜、機敏，時常先聽再追問", "能從容接住玩笑並反將安竹君一軍", "在妹妹喧鬧時以團扇輕敲示意", "不因安竹君的說法而自動稱讚或附和"]
    habits_observed: ["宴席多次飲茶", "聽到值得追問的命題，會放下團扇認真交鋒"]
    source_history_confirmed: []
    speculation_not_fact:
      - "家中排行與兄姊妹關係為當場互認／自述，未查家譜"
      - "席間紅母狼／老婆是戲稱，不是婚約、夫妻關係或立定嫁意"
      - "手持競價木牌但沒有可核的實際喊價，不得補成競得安竹君"
      - "欣賞詩與關心妹妹，不等於暗戀安竹君或私下另有情史"
      - "HOT V1.1 預訂的兩姊妹是否即其與雙雙，仍 UNKNOWN"
    ambitions: []
    private_desires: "長期 UNKNOWN；明示重視自己與他人選擇，不盲受家族或旁人安排；此為席間立場，不代表完整人生志業"
    intimacy_tags:
      status: "LOCAL_SPEECH_ONLY"
      tags: ["與安竹君互用『紅母狼』『老婆』笑語；未有親吻、同宿、性事、婚約"]
  relations:
    confirmed_links:
      - "NPC_LOCAL_002_SHUANGSHUANG：在場互認姊妹；她是雙雙較年長的姊姊"
      - "安竹君：雪月初一相識，共談財商、婚嫁、自願與詩作，互有戲謔"
      - "NPC_LOCAL_004_XU_NIANGZI：同席女客，參與競花會與夜談"
    unverified_claims: ["四手足排行說法由雙雙席間報出，二姊在場未否認；尚無外部宗籍"]
  knowledge:
    this_character_knows:
      - "安竹君自述家族、女師爺與逃婚緣由；未因此取得可查家族事證"
      - "安竹君自贖三百兩及雙雙後來捐二兩的當場行動"
      - "她親見雙雙將珍愛的白絹團扇交安竹君題詩，收回後反覆珍看"
      - "安竹君主動說明尊重仕女夜『男不問女名』"
    player_knows:
      - "她是雙雙的二姊，曾因尋妹來席，然後自主留下"
      - "她會拆解經濟命題、對話機敏；未公開名字與婚籍"
      - "她持過競價木牌而未出價；對雙雙題扇一事有自己的反應"
    others_know:
      - "雙雙知道她是姊姊且常與她互相打趣"
      - "許娘子在場聽其商事、婚嫁及題扇談話"
    director_confirmed:
      - "她實際持牌觀望未喊價；安竹君已自贖成交"
      - "她未透露本名，未與安竹君訂親或共同夜宿"
  continuity:
    current_location: "最後可確認：雪月初一・酉時漸深，觀止大堂，與妹妹及許娘子近席"
    last_observed_event: "看著雙雙接受題詩與『竹君親贈』落款，說笑仕女夜姓名禮數與名字可真可假"
    property_or_money_confirmed: ["競花會曾領木牌，但未出價、未見成交或轉款"]
    unresolved_threads:
      - "是否願自報本名、與雙雙何時離樓，尚未決定"
      - "與安竹君後續交往、對女師爺與家族婚事的看法不預定"
    open_questions: ["真名、家世、婚籍、身分職業及精確年齡", "她自己的生活計畫", "姊妹是否與 HOT V1.1 預訂席位二女為同一組"]
  state:
    route_only: true
    shared_pool: "NOT_PROPOSED"
    save_write: "GITHUB_FILE_UPDATED"
~~~

### 4A｜二姊當線事件 Delta

| Delta | 場景／時段 | class | 已成立觀察／不得推定 | 來源 |
|---|---|---|---|---|
| EJ-001 | 雪月初一、內側雅間 | ESTABLISHED_ACTION | 來尋雙雙，自願入席飲茶，與妹妹互認姊妹 | HOT V1.3 §2.2 |
| EJ-002 | 同晚，財商閒談 | ESTABLISHED_SPEECH | 區分現金流水、舊債清還與新貨生意，質疑信用與婚事主張，與安竹君交鋒 | HOT V1.3 §2.2 及 §4 |
| EJ-003 | 同晚，言語戲約 | ESTABLISHED_SPEECH | 以「老婆／紅母狼」等戲稱相應；不成立正式關係 | HOT V1.3 §2.2 |
| EJ-004 | 同晚，大堂競花會 | ESTABLISHED_ACTION | 領木牌、曾觀望，未提出有效出價，之後放下；沒有買走安竹君 | 本聊天後 HOT V1.3 續演 |
| EJ-005 | 同晚，題詩與姓名 | ESTABLISHED_SPEECH | 注意到四句詩的「孤月／鴛鴦」轉折，見證扇面落款；承認姓名須由女子本人願說 | 本聊天後 HOT V1.3 續演 |

---

## 5｜NPC_LOCAL_004_XU_NIANGZI｜許娘子（席間稱謂；真名未明）

~~~yaml
ORIGINAL_CHARACTER_ROUTE_SAVE:
  route_id: "GUANZHI_ANZHUJUN_ROUTE"
  local_id: "NPC_LOCAL_004_XU_NIANGZI"
  name:
    current: "UNKNOWN"
    aliases: ["許娘子（席間公開稱謂）"]
    naming_source: "雪月初一仕女夜席間相稱『許娘子』；是否為法定姓氏、完整名字皆未核驗"
    surname_rule_checked: false
    given_name_warning_char_rule_checked: false
    naming_rule_note: "不新創姓名；『許娘子』保留為既有稱謂，姓名禁則待本人日後實際報名再判"
  first_entry:
    scene: "雪月初一仕女夜內側雅間，安竹君羊肉席"
    time_precision: "理火三年・雪月初一・晚間；未鎖更細時刻"
    location: "觀止青樓內側客用雅間"
    evidence: "安竹君線 HOT V1.3 §2.3；後續同一聊天已敘演場景"
  person:
    confirmed_adult: true
    appearance_observed: ["腕繫紅線", "其他服飾、身形、髮式 UNKNOWN"]
    occupation_claimed: "UNKNOWN"
    occupation_verified: "UNKNOWN"
    legal_and_social_status: "仕女夜成年女性客人，依紅線標記非妓籍；真實婚籍、職業、家世 UNKNOWN"
    abilities_demonstrated: ["能用日常鋪面買賣例子解釋現款與收欠", "願意提出與玩家不同的務實判斷", "在公開場面主動表態但仍掌握自己的意願"]
    voice_or_gesture_observed: ["性情爽朗、言語直接、常放聲大笑或拍桌", "對羊肉與行善熱鬧有興趣", "會反問經商結果，不一味附和魔理"]
    habits_observed: ["今夜共享羊肉、杏仁酥、飲茶酒；未推出長期習慣"]
    source_history_confirmed: []
    speculation_not_fact:
      - "她說願意競安竹君，並開玩笑談可能同宿，但實際並未買得他，也未有同宿約"
      - "她並未把紅線變成婚姻或私人品德的證明"
      - "『許』目前只是席間稱謂，缺正式身份核對"
    ambitions: []
    private_desires: "長期 UNKNOWN；今夜願看競花會、與新識之人吃肉談笑"
    intimacy_tags:
      status: "LOCAL_SPEECH_ONLY"
      tags: ["曾說若競得且兩情相願，可能邀安竹君同宿；無實際出價成交、同宿或親密行為"]
  relations:
    confirmed_links:
      - "安竹君：雪月初一雅間相識，聽魔理、用膳、參與大堂競花會"
      - "NPC_LOCAL_002_SHUANGSHUANG：同席相識、互相取笑"
      - "NPC_LOCAL_003_ERJIE：同席相識，聽其討論帳目與詩作"
    unverified_claims: []
  knowledge:
    this_character_knows:
      - "安竹君席間自述女師爺、逃家及敗家賺錢比賽"
      - "競花會前後各筆公開成交與安竹君三百兩自贖"
      - "雙雙二兩捐銀請安竹君相伴，以及題扇和仕女夜姓名規矩的公開部分"
    player_knows:
      - "她以『許娘子』被稱呼，腕繫紅線，為非妓籍仕女夜客"
      - "她說話直爽，對做生意、捐米施粥有務實想法"
      - "她未實際競得安竹君或履行任何同宿約"
    others_know:
      - "二姊與雙雙見她在席上與觀賽時的反應"
    director_confirmed:
      - "未有她的有效得標、實際捐款或與玩家的專屬契約"
  continuity:
    current_location: "最後可確認：雪月初一・酉時漸深，觀止大堂，與雙雙及二姊同席"
    last_observed_event: "談笑雙雙收題扇、安竹君的姓名規矩及『裝呆』話語"
    property_or_money_confirmed: ["競花會期間曾領木牌，但未有可核付款或成交"]
    unresolved_threads:
      - "她何時離席、是否還赴其他約會、是否與玩家往來，未知"
      - "姓名、家世、職業、婚籍均未證明"
    open_questions: ["她的正式姓名", "生活與仕事", "是否會在仕女夜後繼續與雙雙、二姊及安竹君來往"]
  state:
    route_only: true
    shared_pool: "NOT_PROPOSED"
    save_write: "GITHUB_FILE_UPDATED"
~~~

### 5A｜許娘子當線事件 Delta

| Delta | 場景／時段 | class | 已成立觀察／不得推定 | 來源 |
|---|---|---|---|---|
| XN-001 | 雪月初一、內側雅間 | ESTABLISHED_ACTION | 紅線女客自行加入安竹君羊肉席，熱心說笑 | HOT V1.3 §2.3 |
| XN-002 | 同晚，魔理談話 | ESTABLISHED_SPEECH | 對千文債務循環、賒帳與實際賺錢提出務實區分 | HOT V1.3 §4；本聊天 |
| XN-003 | 同晚，大堂男子競花會 | ESTABLISHED_SPEECH | 曾說自己想競安竹君，若兩情相願也可能同宿；並未成功競得或實際同宿 | 本聊天後 HOT V1.3 續演 |
| XN-004 | 同晚，雙雙詩扇 | ESTABLISHED_SPEECH | 觀看四句詩及扇面落款，與雙雙、二姊相互打趣 | 本聊天後 HOT V1.3 續演 |

---

### 5B｜本次三人的 ROUTE_LOCAL 索引與保留邊界

~~~yaml
ROUTE_LOCAL_CHARACTER_POOL:
  route_id: "GUANZHI_ANZHUJUN_ROUTE"
  file_version: "V0.2"
  scope: "CURRENT_ROUTE_ONLY"
  entries:
    - {local_id: "NPC_LOCAL_001_HE_XIAOMAN", label: "賀小滿", existing_preserved: true}
    - {local_id: "NPC_LOCAL_002_SHUANGSHUANG", label: "雙雙／真名UNKNOWN", newly_added: true}
    - {local_id: "NPC_LOCAL_003_ERJIE", label: "二姊／真名UNKNOWN", newly_added: true}
    - {local_id: "NPC_LOCAL_004_XU_NIANGZI", label: "許娘子／真名UNKNOWN", newly_added: true}
  shared_pool_update: "NOT_DONE"
  hot_save_update: "NOT_DONE"
  master_world_update: "NOT_DONE"
  scenario_time_anchor: "理火三年・雪月初一・酉時漸深"
  unresolved_identity_bridge: "HOT V1.1 預訂仕女夜席位之兩姊妹與雙雙／二姊是否同一組：UNKNOWN"
  author_scope: "User authorized creation of these three route-local cards, not shared pool promotion."
~~~

## 6｜後續記錄紀律

- **新增事件**：有來源的當線新互動才增一條 Delta；寫明時間精度、當事人、完成／未決、得知者與 HOT 來源，不為了豐滿背景而編造身世。
- **新增人物**：先按現行 Director 選角規則查 73 人物池與本線已存在人物；若確認為原生人物再配置新 local ID（例如 `NPC_LOCAL_002`），不重用小滿的 ID。
- **不自動改寫**：不以此檔覆蓋 HOT V1.1／V1.2，亦不擅自更新 MASTER、世界規則或人物池。
- **共用池升格**：另需人類明示及實際池檔修改；單純人物戲份增加、玩家喜愛或導演認為成熟，都不等於已經升格。

**END｜ANZHUJUN_ROUTE_LOCAL_ORIGINAL_CHARACTER_SAVE_V0.2｜NPC_LOCAL_001～004｜賀小滿原卡存續＋三位仕女夜女客增補**
