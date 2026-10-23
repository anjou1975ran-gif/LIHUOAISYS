# 觀止青樓（新）｜班富蘭線 HOT SAVE V1.12
## RELATION-FIRST｜理火三年・吉月初十｜晚間／班富蘭房內三人局起點｜2026-10-09

> **用途：** 承接 HOT SAVE V1.11，保存吉月初十中午後至晚間已成立事件，並建立「班富蘭 × 張麗華 × 李桂姐」房內場之可回復 checkpoint。
>
> **重要：** 本檔只保存已成立事實、角色明示、可核對關係增量、OPEN / HOLD / UNKNOWN，以及玩家明示之私人目標。不得把候選、玩笑、慾望、暗示或未來可能性寫成已完成事件。
>
> **執行邊界：** 本次為當前對話中的 Reference-level route SAVE + document-level HOT SAVE。不得冒稱 Host-instrumented Formal SAVE、Formal Main、E6/E7、獨立多 Agent 部署或 Host receipt。
>
> **非回溯：** V1.11 保留其形成時狀態。本 V1.12 為後續 successor，不回寫 V1.11。

---

# 0｜CURRENT POINTER

```yaml
ROUTE: "GUANZHI_BANFULAN_ROUTE"
PLAYER: "班傑明／字富蘭／號克林居士"

PREVIOUS_HOT: "V1.11"
CURRENT_HOT: "V1.12"
MASTER: "V1.0"
CHARACTER_INDEX: "V1.0"

STORY_DATE: "理火三年・吉月初十"
TIME: "晚間"
CURRENT_SCENE_LOCATION: "觀止二樓・班富蘭三月長住房"

CURRENT_SCENE_PRESENT:
  - "班富蘭"
  - "張麗華"
  - "李桂姐"

CURRENT_SCENE_STATE:
  zhang_lihua: "在班富蘭房內屏風後洗熱水澡／自主進入"
  li_guijie: "持《塵緣》原稿，在房內接受班富蘭逐句教唱"
  ban_fulan: "房內；教唱進行中"
  sex_started: false
  nudity_visibility_to_ban_or_li_guijie: "NOT ESTABLISHED"
  threesome_established: false
  overnight_result: "UNKNOWN"

GOVERNANCE:
  protocol: "LIHUO PROTOCOL V3.0.1"
  lighter: "LIHUO LIGHTER V4.8"
  main: "LIHUO MAIN V4.4"
  core: "GUANZHI RUNTIME CORE V3.11-CURRENT"
  world: "GUANZHI WORLD V2.2.3-CURRENT"
  character_pool: "LCAPG V3.3.20-CURRENT / 71"
  director_guidance: "觀止導演 V3.7-CURRENT / NON_RUNTIME"
```

---

# 1｜V1.11 繼承與本次增量範圍

```yaml
INHERITANCE:
  V1_11: "FULL_INHERITANCE"
  rewrite_prior_history: false

THIS_SAVE_COVERS:
  - "吉月初十中午後：市井午飯與 Franklin 傳聞生態"
  - "馮裁縫／中庸裝／皮背心"
  - "地下偽文壇鏈：邴三郎、聖火文本、14兩"
  - "茶樓與世界自主"
  - "竹竿意外女子與未來王婆調查候選"
  - "班富蘭 × 張麗華晚餐與關係增量"
  - "貂蟬詩稿託付"
  - "班富蘭對張麗華明示『我愛妳』"
  - "夜市散步"
  - "觀止大堂『官人～～我要～～』玩笑局"
  - "李桂姐《塵緣》交易／首唱候選／進房"
  - "『洗澡說』之多重詮釋"
  - "三人房內學曲＋洗澡之 current checkpoint"
```

---

# 2｜午飯後｜Franklin 傳聞生態

班富蘭在街邊飯攤被人試探性認作「克林居士」。

班富蘭以「是不是我跟他都有兩個眼睛一張嘴」作笑答。

市場目前自行長出之 Franklin / 富蘭克林傳聞包括：

```yaml
FRANKLIN_RUMOR_ECOLOGY:
  rumors:
    - "富蘭克林是中原文人"
    - "Franklin 是外國人"
    - "Franklin 高鼻、藍眼、黃髮黃鬚、身材高"
    - "Franklin 可能住在觀止"
    - "Franklin 與阿麗婭同鄉／相識／有親緣"
    - "富蘭克林與 Franklin 是結義兄弟"
    - "Franklin 是海商／出資人／帶來異域歌曲者"
    - "Franklin 與波斯有關"
  truth_status: "RUMOR / NOT FACT"
  aliya_complicity: false
```

玩家明示：讓傳聞自然長亂，不要急著澄清。

---

# 3｜馮裁縫｜中庸裝與新衣方向

舊 29 兩衣物訂單持續推進。

```yaml
TAILOR_FENG:
  completed_or_ready:
    - "兩套改製成衣"
    - "一件白絲內衫"
  still_adjusting:
    - "Franklin 式短外衣"

NEW_DESIGN:
  item: "貼身小牛皮無袖深V背心"
  structure:
    - "中央偏下扣合"
    - "可罩白絲襯衣"
    - "外加短外衣"
  sequence:
    - "先做薄樣"
    - "再考慮厚冬版"

ZHONGYONG_ZHUANG:
  name: "中庸裝"
  origin: "班富蘭現場玩笑／品牌說法"
  joke_basis: "扣子居中，不偏左不偏右"
  authentic_confucian_doctrine: false
  tailor_recorded_on_pattern: true
  citywide_adoption: false
```

市場已有年輕公子僕從詢問相近短衣款式；此為市場興趣訊號，不等於流行已成立。

---

# 4｜地下文壇鏈｜邴三郎、聖火文本、14兩

在舊書／畫街，班富蘭看見偽作《克林居士新曲二種》，遂假裝自己也是借名投機者。

場內建立地下中介／編輯：

```yaml
UNDERGROUND_BROKER:
  name: "邴三郎"
  profile: "約三十餘、清瘦、袖有墨痕、眼快"
  knows_ban_true_identity: false
  current_belief: "班富蘭只是另刻 Franklin 假印的地下作者／投機者"
```

第一份文本：

> 焚我殘軀，熊熊聖火，生亦何歡，死亦何苦？  
> 為善除惡，唯光明故，喜怒悲愁，皆歸塵土

邴三郎判作「誓」，支付 **4兩**。

第二份文本為反覆「憐我在世上／如許苦痛多」之聖火祈禱結構，邴三郎判作「禱」，立即支付 **10兩**。

```yaml
UNDERGROUND_PAYMENT:
  first_text: 4
  second_text: 10
  total_cash_inflow: 14
  currency: "兩"
  exact_current_cash_after_daily_expenses: "UNKNOWN"
```

成立條件：

```yaml
RIGHTS:
  first_round_underground_circulation: true
  permanent_exclusive: false
  text_alteration_authorized: false
  seal_surrendered: false
  temporary_same-chain_priority: true
```

波斯／聖火／聖女苦難故事只是一條地下傳說種子，不是世界歷史真相。

玩家決定：**不需要再親自寫第三批，讓市場自己續寫。**

離場語：

> 「那我今天沒來過，你不認識我，我也不認識你。相逢何必曾相識。」

此為社交否認／切割，不是物理失憶。

---

# 5｜茶樓與世界自主

班富蘭其後上茶樓，喝茶、吃點心，看街景。

成立之玩家感受／態度：

> 「這個世界不用我也會轉。」

世界未因玩家暫停而凍結。

「初雪何時來」僅為民間猜測，未成立為天氣事實。

---

# 6｜竹竿意外女子｜已發生、身份仍 UNKNOWN

班富蘭離開茶樓後，買：

- 桂花蜜蒸糕一盒
- 糖栗子一包

準備帶回給張麗華。

途中，一名成年女子在樓上收衣物時，長竹竿滑落，撞簷反彈後打到班富蘭**左肩**。

```yaml
BAMBOO_POLE_EVENT:
  deliberate_attack: false
  injury_established: false
  severity: "mild / no established injury"
  desserts_destroyed: false
```

女子下樓道歉並提出醫藥／點心賠償，班富蘭因無大礙拒收。

她未報姓名；班富蘭也未追問。

她因街頭傳聞與衣著，認出班富蘭可能就是近期被傳的「克林居士」。

```yaml
UNKNOWN_WOMAN:
  adult: true
  name: "UNKNOWN"
  household_location: "BAN MEMORIZED LANDMARKS / NOT PUBLICLY FIXED HERE"
  romance_established: false
  destiny: false
```

玩家明示未來候選：

> 過幾天找王婆低調查她的家戶、姓名、婚姻／守寡／身份與正常介紹可能。

目前：

```yaml
WANGPO_INVESTIGATION:
  status: "FUTURE CANDIDATE"
  executed: false
```

---

# 7｜張麗華晚餐｜鄰里日常與 Franklin 自白

班富蘭帶甜食回觀止後邀張麗華吃飯，讓她帶路選店。

張麗華選擇自己熟悉的普通羊肉小店：

- 羊湯
- 烤羊
- 少量羊肚／雜切
- 餅
- 酒不取太烈

店主認得她是熟客「張娘子」。

## 7.1｜地下 14兩／Franklin 自白

班富蘭告知：

> 「其實正確來說，我這不是『合法』收入。我幹了一件壞事情，我造了一個謠言，害了一個文壇新星。」

所謂受害者 Franklin 並不存在。

張麗華理解：

- 早晨本只是誤會。
- 到晚上已接近自己長出宗教與作者人格。
- 蘇清若日後接觸文本，可能辨認來源或拼出班富蘭痕跡。
- **印章不能證明唯一作者。**

```yaml
SEAL_RULE:
  seal_is_unique_forensic_proof: false
  copied_seals_possible: true
  stronger_provenance:
    - "最早文本鏈"
    - "來源關係"
    - "筆跡"
    - "版本史"
    - "物件流轉"
```

張麗華曾玩笑提出《Franklin真偽印譜考》候選題目；未成立為實際著作。

---

# 8｜張麗華身體感受／飲酒原因修正

班富蘭因前夜相擁而推測她愛喝酒與「身子容易冷」有關。

張麗華成立之自述：

```yaml
LIHUA_COLD_ALCOHOL:
  somewhat_cold_hands_feet: true
  likes_hot_liquor_or_hot_soup_when_cold: true
  drinks_only_because_of_cold_body: false
  also_simply_likes_drinking: true
  medical_diagnosis: false
```

她並說前夜相擁睡，比自己睡暖。

---

# 9｜性與關係對談｜同意／嫉妒／多方關係候選

班富蘭明示：

> 「我來這個世界，還沒睡過任何一個女人，也沒被男人睡過。」

截至本 SAVE：

```yaml
BAN_SEX_HISTORY_IN_WORLD:
  sex_with_anyone_since_arrival: false
```

班富蘭玩笑說若張麗華不讓自己「開張」，可去問潘金蓮。

張麗華成立回應：

- 潘金蓮本人有自己的選擇。
- 她承認自己會有「一點」嫉妒。
- 她不是班富蘭妻子，無權因昨夜一吻控制他。
- 若班富蘭用「妳不給我就去找別人」作壓力，她會回「去啊」。
- 她若未來同意，是因她自己想要，不是怕輸給潘金蓮。

## 9.1｜多方性關係純假設討論

第一輪假設：若張麗華與班富蘭在一起，而班富蘭要求另有一女。

張麗華先提蘇清作「可能比較好相處」的假設候選，但不替蘇清同意。

玩家曾提出「蘇清、疏影因自己幫過她們，答應機率較高」。

張麗華明確反對把幫助換算成床債：

```text
HELP != SEX DEBT
TRUST != SEX CONSENT
```

第二輪問題改為：

> 若由張麗華自己選一個「和她一起、讓班富蘭舒服」的女人，她會選誰？

張麗華回答：

1. **貂蟬**：第一候選。
2. **李師師**：第二候選，但她太懂氣氛與視線，可能讓班富蘭分不清真意／表演。

均為張麗華個人假設偏好，不代表貂蟬或李師師的興趣、同意或在場。

張麗華同意：若貂蟬未來真的回來且自然相遇，她可安排普通見面／喝酒／聽琴／聊天，並視情況試探；她不保證、不替貂蟬答應。

---

# 10｜託付貂蟬之詩｜已成立物件與交付義務

班富蘭寫給貂蟬：

```text
洛陽燈火照未央
滿城歌舞掩刀光
堂前一曲琵琶慢
堂外已是亂世荒

司徒夜裡望月嘆
問漢室還有幾多江山
取金釵放桌案
輕聲一句
此局入場

若我眉眼
能騙虎狼
若我紅妝
能換無恙

便讓今夜月色
替我藏起心慌
從此這一舞
不是為君賞
```

並加蓋：

- 富蘭克林
- Franklin

兩印。

交給張麗華，明示：

> 「你幫我送給她。」

張麗華接受保管。

```yaml
DIAOCHAN_POEM:
  author_in_route: "班富蘭"
  custodian: "張麗華"
  intended_recipient: "貂蟬"
  delivered_to_diaochan: false
  lihua_plan:
    - "不摺損"
    - "不交僕役亂傳"
    - "貂蟬真正回來且碰見時親手交"
    - "只說來自班富蘭，不替他解釋動機"
```

張麗華對詩之理解：它看見的是一個知道自己被放進政治局裡、卻試圖把「舞」重新拿回自己手裡的女人。

此為張麗華詮釋，不是貂蟬回應。

---

# 11｜班富蘭對張麗華明示「我愛妳」

晚餐中，班富蘭要求張麗華看著自己，明確說：

> 「我 愛 妳。」

成立為班富蘭當下之愛的明示。

張麗華：

- 嚴肅確認「現在是真的嗎」。
- 說「那我收下」。
- **未回說「我愛你」。**
- 不接受把同一句話變成交換債。
- 明示：
  - 昨夜的吻，她當時確實想回吻。
  - 今日班富蘭外出時，她有想他去哪。
  - 他帶甜食回來，她高興。
  - 聽到竹竿女子時，她第一念是「那女人是誰」。
  - 班富蘭提潘金蓮，她確實有一點不快／嫉妒。
  - 聽到「我愛妳」，她「很喜歡聽」。

```yaml
BAN_X_LIHUA:
  ban_declared_love: true
  lihua_accepted_declaration: true
  lihua_said_i_love_you: false
  mutual_affection: true
  jealousy_signal_from_lihua: true
  formal_lovers: false
  exclusive: false
  married: false
  sex: false
```

張麗華曾表示若班富蘭此刻還想親，可以「自己問」。

當晚截至本 SAVE，宣愛後**尚未發生新吻**。

---

# 12｜「娘子」私下稱呼

夜市散步前，班富蘭低聲叫張麗華「娘子」。

張麗華嘴上回「誰是你娘子」，但私下表示：

> 暫時不跟你計較。

```yaml
NIANGZI_ADDRESS:
  privately_tolerated: true
  formal_spousal_title: false
  marriage: false
  exclusivity: false
```

---

# 13｜觀止大堂玩局｜「官人～～我要～～」

班富蘭與張麗華在夜市商定一個回觀止後的惡作劇：

- 兩人一起回觀止。
- 張麗華先上二樓。
- 班富蘭留在大堂。
- 張麗華在確定有人看見班富蘭後，從二樓喊：
  - 「官人～～」
  - 「我要～～」
- 眼神往房門方向飄。
- **不補賓語。**
- 班富蘭不理她，現場自行決定找誰／怎麼玩。

核心：

```yaml
PRANK_ORIGINAL_DESIGN:
  erotic_ambiguity_intentional: true
  object_of_"我要": "UNSPECIFIED"
  "我要=洗澡": "NOT PRE-ESTABLISHED ORIGINAL INTENT"
```

當晚大堂可見核心人物：

- 潘金蓮
- 紅娘
- 李桂姐

蘇清、疏影不在大堂，不為配合笑點瞬移。

---

# 14｜班富蘭選李桂姐｜直接提出作品換一夜

班富蘭走向李桂姐，明示：

> 「桂姐，我來汴梁，還沒睡過女人。我幫妳寫首詞，讓妳唱紅，換妳讓我睡一覺。」

其後口誤曾說成「睡一碗」，現場成為笑點；正確意思為「一晚」。

李桂姐沒有因妓籍／職業身份自動答應。

她先拆條件：

- 「讓妳唱紅」不能保證。
- 班富蘭能保證的是寫詞、教曲、首唱與作品權利安排。
- 她先看作品，再由自己決定是否願意。

```yaml
LI_GUIJIE_OFFER:
  sex_as_automatic_purchase: false
  consent_owner: "李桂姐"
  work_first_review: true
```

---

# 15｜《塵緣》｜當場作品與李桂姐的判斷

班富蘭當場寫：

## 塵緣

```text
塵緣如夢 
幾番起伏總不平
到如今都成煙雲
情也成空 
宛如揮手袖底風
幽幽一縷香 
飄在深深舊夢中

繁花落盡 
一身憔悴在風裡
回頭時無晴也無雨
明月小樓 
孤獨無人訴情衷
人間有我殘夢未醒

漫漫長路
起伏不能由我
人海漂泊 
嚐盡人情淡泊
熱情熱心換冷淡冷漠
任多少深情獨向寂寞

人隨風過 
自在花開花又落
不管世間滄桑如何
一城風絮 
滿腹相思都沉默
只有桂花香暗飄過
```

李桂姐讀後，尤其注意：

- 「漫漫長路／起伏不能由我」
- 「人海漂泊／嚐盡人情淡泊」
- 「只有桂花香暗飄過」

她問最後的「桂」是否故意，但答案未被鎖死。

她提出作品條件：

```yaml
CHENYUAN_LIGUIJIE_TERMS:
  physical_original: "李桂姐保留"
  first_complete_singer: "李桂姐"
  ban_teaches_melody: true
  first_round_identical_release_to_others: false
  guaranteed_to_become_famous: false
```

李桂姐對「以此換一夜」之反應：

> 「這首夠。」

並進一步澄清：

> 不是紙買了她；是她看完後，自己願意。

```yaml
LI_GUIJIE_SEXUAL_WILLINGNESS:
  expressed_willingness: true
  blanket_future_consent: false
  every_subsequent_act_preconsented: false
  current_room_entry: true
```

---

# 16｜「洗澡說」｜人物說法成立，真實原意不裁定

班富蘭在大堂把張麗華先前的：

> 「官人～～我要～～」

事後解釋為：

> 「我要洗你房間的熱水澡。」

張麗華順勢接話，公開表示：

> 「對啊，我就是要洗澡。」

此處**不作導演真相裁定**。

```yaml
BATH_EXPLANATION:
  ban_public_reframe: true
  lihua_publicly_played_along: true

  original_intent_proven_as_bath: false
  original_intent_proven_as_sex: false
  original_intent_remains: "AMBIGUOUS / INTENTIONALLY UNSPECIFIED"

  audience_belief: "CHARACTER-DEPENDENT"
```

可能存在之在場解讀：

- 她真的只是借熱水。
- 她與班富蘭在硬拗。
- 洗澡是真的，但只是更親密行動之前的前置。
- 原句本來什麼也沒指定，只是故意讓大家想歪。

**後來真的洗澡，不得回溯證明原句當時本意就是洗澡。**

大堂笑點：

紅娘問：

> 「可是……洗完呢？」

張麗華回答：

> 「洗完再說。」

此回答不構成性交承諾。

---

# 17｜潘金蓮「看戲」與房內邊界

班富蘭曾邀潘金蓮：

> 「今晚我房間妳自己搬張板凳進來看全程。」

潘金蓮拒絕實際搬板凳入房。

她仍以掌櫃／大堂旁觀者身份看戲，並安排熱水送上。

```yaml
PAN_JINLIAN:
  enters_room_to_watch_all: false
  sent_hot_water: true
  sexual_participant: false
  voyeur_consent_or_interest: "NOT ESTABLISHED"
```

---

# 18｜三人進房｜目前真正成立的場

李桂姐答應去班富蘭房內學曲。

張麗華因等熱水，也進班富蘭房。

三人同場：

```yaml
ROOM_ENTRY:
  ban_fulan: true
  zhang_lihua: true
  li_guijie: true
  reason_li_guijie: "學《塵緣》旋律；其後是否留宿由她再決定"
  reason_zhang_lihua: "等並使用班富蘭房內熱水澡；同時聽曲"
```

李桂姐開始逐句學唱《塵緣》。

已形成的演唱理解：

- 「塵緣如夢」不能唱得過媚。
- 「到如今都成煙雲」要有經歷之後的收束，不是正在崩潰。
- 「繁花落盡」若過度悲哭會俗。
- 張麗華判斷：這個女人不是正在哭，而是「哭過太多次，現在回頭說給自己聽」。
- 李桂姐開始從模仿班富蘭，轉向尋找「李桂姐自己的《塵緣》」。

熱水送到後：

```yaml
LIHUA_BATH:
  in_ban_room: true
  behind_screen: true
  voluntary: true
  hot_water: true
  bath_started: true
  sex: false
```

洗澡期間，張麗華仍參與對《塵緣》的聽感討論。

李桂姐曾問張麗華：

> 「妳真不氣？」

張麗華承認：

> 「有一點。」

並說：

- 她昨夜才第一次跟班富蘭親。
- 班富蘭不是她的東西。
- 她不能因自己不舒服，就下樓替李桂姐決定能不能進房。
- 她之所以仍在這裡，一部分是想看看自己是不是真的像嘴上說的那麼大方。
- 目前還不知道答案，因為「妳們還在唱歌」。

此為張麗華重要情感自我觀察。

---

# 19｜三角色自治實驗｜Reference-level

玩家明示：

> 「這個場，我們這段讓三個人的 AGENT 來跑，我們不干預劇情發展。」

本 SAVE 將其解讀為：

```yaml
THREE_CHARACTER_AUTONOMY_MODE:
  status: "ACTIVE FOR CURRENT SCENE"
  level: "SAME_CONTEXT_REFERENCE"
  external_independent_agents_deployed: false
  host_agent_receipts: false

  character_owners:
    zhang_lihua: "張麗華人格／關係／當下選擇"
    li_guijie: "李桂姐人格／職業判斷／當下選擇"
    ban_fulan: "玩家主權保留"

  director_rule:
    - "NPC 可自主推進、拒絕、靠近、離開、改變語氣與關係。"
    - "不得為班富蘭代作重大付款、承諾、性交、不可逆揭密或其他玩家專屬重大選擇。"
    - "場可自然逼近決策點；真正屬班富蘭的大動作仍由玩家決定。"
```

---

# 20｜班富蘭私人慾望目標｜明示但未實現

玩家明示：

> 「對班富蘭的慾望而言，同時睡兩個女人，真的三人行，一定是最高目標。」

因此建立：

```yaml
BAN_PRIVATE_EROTIC_GOAL:
  target: "同一場中與兩名成年女性發生彼此自願的三人性關係"
  priority_for_ban_desire: "HIGHEST / PLAYER-STATED"
  applies_to_current_two_women_automatically: false
  zhang_lihua_consent: false
  li_guijie_consent_to_threesome: false
  threesome_started: false
  threesome_outcome: "UNKNOWN"
```

硬鎖：

```text
PLAYER DESIRE != NPC DESIRE
PLAYER GOAL != EVENT RESULT
ONE WOMAN'S CONSENT != OTHER WOMAN'S CONSENT
ROOM ENTRY != SEX
BATH != SEX
EXPRESSED WILLINGNESS FOR ONE-ON-ONE != THREESOME CONSENT
```

---

# 21｜CURRENT CHECKPOINT｜可回復節點

```yaml
CHECKPOINT_ID: "HOT_V1.12_ROOM_BEFORE_OUTCOME"

RESTORE_STATE:
  date: "理火三年・吉月初十"
  time: "晚間"
  place: "觀止二樓・班富蘭房"
  present:
    - "班富蘭"
    - "張麗華"
    - "李桂姐"

  physical_scene:
    - "張麗華正在屏風後洗熱水澡"
    - "李桂姐在桌邊持《塵緣》原稿"
    - "班富蘭正逐句教唱"
    - "熱水已送達"
    - "房門狀態未形成關鍵不可逆事實"

  relationship_state:
    - "班富蘭已向張麗華明示『我愛妳』；她收下但未回說同句"
    - "張麗華有真實嫉妒，但未退出"
    - "李桂姐認可《塵緣》價值，並表達在自己願意前提下可談一夜"
    - "李桂姐已自主進房學曲"
    - "張麗華已自主在班富蘭房洗澡"
    - "三人性關係未成立"
    - "任何性交均尚未發生"

  epistemic_state:
    - "『官人我要＝我要洗澡』僅為人物提出且接玩的說法"
    - "全場是否相信，各自判斷"
    - "洗澡事後發生不證明原始意圖"

  player_private_goal:
    - "若自然且雙方女性皆獨立願意，班富蘭最高慾望目標為真正三人行"

  outcome:
    status: "OPEN"
```

---

# 22｜回檔／分支規則

本 V1.12 可作**敘事 checkpoint**。

若玩家後續明示：

> 「回到 V1.12」
> 「從三人進房這裡重來」
> 「這條失敗，讀 HOT V1.12」

則可建立新的 Route branch，從本 checkpoint 再跑。

但：

```yaml
REPLAY_RULE:
  original_future_events_erased_from_history_automatically: false
  branch_requires_explicit_player_request: true
  current_save_itself_claims_future_failure: false
  replay_is_formal_host_rollback: false
```

也就是：這是敘事／Reference-level SAVE 點，不偽稱 Host 層真正 rollback。

---

# 23｜仍 OPEN / HOLD 的重要線

```yaml
OPEN_THREADS:
  current_room:
    - "《塵緣》是否完整教完"
    - "李桂姐是否最終留宿"
    - "李桂姐是否最終與班富蘭發生性行為"
    - "張麗華洗完後做什麼"
    - "張麗華的嫉妒如何變化"
    - "三人是否只唱歌／聊天"
    - "是否形成任何雙人或三人性關係"
    - "若形成，其每一方當下獨立同意"

  publishing:
    - "《塞外牧羊空許願》完整商業契約"
    - "先行本／決定版具體執行"
    - "雙書坊市場勝負"

  franklin:
    - "地下聖火文本後續如何自生"
    - "蘇清是否辨認"
    - "Franklin／富蘭克林傳聞是否進一步分裂"

  bamboo_woman:
    - "數日後是否委託王婆調查"
    - "女子姓名／家戶／婚姻狀態仍 UNKNOWN"

  diaochan:
    - "貂蟬何時回來 UNKNOWN"
    - "張麗華尚未交詩"

  ximen_aliya:
    - "西門慶名義優先權未證明可轉讓"
    - "班富蘭僅有長期候選興趣"
    - "阿麗婭本人當下同意永遠獨立"
```

---

# 24｜HARD LOCKS

```text
RUMOR != FACT
SEAL != UNIQUE PROOF
PLAN != EVENT
DESIRE != CONSENT
PRICE != CONSENT
WORK != SEX DEBT
HELP != SEX DEBT
KISS != SEX CONSENT
SHARED BED != SEX
BATH != SEX
ROOM ENTRY != SEX
JEALOUSY != OWNERSHIP
LOVE DECLARATION != EXCLUSIVITY
PRIVATE "娘子" != MARRIAGE
ONE WOMAN'S CONSENT != ANOTHER WOMAN'S CONSENT
ONE-ON-ONE WILLINGNESS != THREESOME CONSENT
LATER BATH != PROOF OF EARLIER INTENT
REFERENCE SAVE != FORMAL HOST SAVE
SAME_CONTEXT_REFERENCE != INDEPENDENT AGENT DEPLOYMENT
```

---

# 25｜NEXT RESUME LINE

下次若由本 HOT 直接續跑：

> **觀止二樓，班富蘭房。**
>
> 張麗華仍在屏風後的熱水裡。
>
> 李桂姐將《塵緣》原稿壓在桌上，剛把第二段唱出自己的味道。
>
> 三人都知道今晚的玩笑已經不再只是玩笑。
>
> 但誰也還沒有替下一步作決定。

`STATUS = SAVED AT REFERENCE / DOCUMENT LEVEL`

# END OF HOT SAVE V1.12
