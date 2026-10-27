# 《九尾龜》遊戲 Corpus｜Stage 1 Baseline V1.0

**狀態：BASELINE / SOURCE-DRIVEN / OPEN-ISSUES-PRESERVED / NOT-RUNTIME**  
**本版定位：** STAGE 1 FROZEN SOURCE CORPUS BASELINE × OPEN ISSUES PRESERVED × RUNTIME DESIGN INPUT  
**來源：** `/mnt/data/九尾龜.epub`，全 192 回  
**用途：** 先抽取《九尾龜》世界結構，不先建立完整 Runtime。

## 0｜抽取原則

- 原文事實、人物觀點、敘述者議論、遊戲推論分離。
- `raw hit != semantic frequency`。
- 固定術語必須有正文用例；回目或後世常用詞不得直接冒充正文固定術語。
- 金錢事件、關係資格、公開名聲、私人偏愛、婚嫁、營業狀態不得互相替代。
- 人物有主權，但主權不等於沒有制度、債務、聲價與第三人壓力。

---

# A｜FENGYUE TERMS / QUALIFICATIONS

## A-001｜功架

```yaml
SOURCE_ENTRY:
  term_or_entity: "功架"
  chapters: [9, 13, 35, 46, 63, 68, 149, 150]
  category: "FENGYUE_TERM / SOCIAL_CAPABILITY"
  observed_function:
    - "評價客人在風月場中的行為熟練、場面感、舉止、談吐、分寸與應酬能力。"
    - "亦用於評價倌人的身段／應酬表現。"
    - "可影響被如何接待、是否被視為外行、以及場面上的光彩。"
  not_equal:
    - "money"
    - "beauty"
    - "relationship status"
    - "sexual access"
  uncertainty:
    - "章秋谷對功架的系統解說屬人物／敘述觀點；應以多回實際事件交叉驗證。"
```

**初步判斷：** `功架` 應是角色的社會操作能力／場性能力，不是單一能力值，也不應直接變成成功率。

## A-002｜資格

```yaml
SOURCE_ENTRY:
  term_or_entity: "資格"
  chapters: [9, 16, 68, 91, 183]
  category: "SOCIAL_QUALIFICATION"
  observed_function:
    - "可指客人在嫖界中的閱歷與進場資格。"
    - "可指倌人經年累積的業內資歷／名次正當性。"
    - "與應酬、聲價、名妓評價互相作用。"
  not_equal:
    - "innate beauty"
    - "money spent"
    - "public fame alone"
```

## A-003｜相好

```yaml
SOURCE_ENTRY:
  term_or_entity: "相好"
  chapters_example: [37, 63, 95, 104, 176]
  category: "RELATION_QUALIFICATION"
  observed_function:
    - "表示已成立且具有歷史、熟悉度與社會期待的客妓往來資格。"
    - "可同時存在多名相好。"
    - "相好關係可發生吃醋、跳槽、公開衝突與長期疏離。"
  not_equal:
    - "exclusive partner"
    - "love"
    - "enke"
    - "marriage"
```

## A-004｜恩客

```yaml
SOURCE_ENTRY:
  term_or_entity: "恩客"
  chapters_example: [36, 64, 91]
  category: "RELATION_QUALIFICATION / PUBLIC_LABEL"
  observed_function:
    - "具有比一般往來更強的社會標籤與期待。"
    - "人物可能自稱恩客而被倌人否認。"
    - "旁人也可能依付款／欠帳等表象傳言某客為恩客。"
  required_separation:
    - "ACTUAL_ENKE_STATUS"
    - "CLAIMED_ENKE_STATUS"
    - "RUMORED_ENKE_STATUS"
  not_equal:
    - "frequent caller"
    - "fast service"
    - "high spender"
```

## A-005｜認了我的開銷

```yaml
SOURCE_ENTRY:
  term_or_entity: "認了我的開銷"
  chapter: 3
  category: "RELATION / FINANCIAL_SUPPORT_EVENT"
  lexical_status: "ATTESTED_PHRASE"
  normalized_candidate: "認開銷"
  normalized_fixed_term_status: "NOT_YET_CONFIRMED"
  observed_function:
    - "與同住／長期財務承擔方向相連。"
  caution:
    - "不得把 normalized_candidate 冒充原作固定術語。"
```

---

# B｜TRANSACTIONS / CREDIT / DEBT

## B-001｜局帳

```yaml
SOURCE_ENTRY:
  term_or_entity: "局帳"
  chapters_example: [22, 23, 37, 38, 62, 64, 93, 100, 129, 162]
  category: "RECEIVABLE / CREDIT"
  observed_function:
    - "可延後收取，不必當場現結。"
    - "節前可能集中收帳。"
    - "倌人或房間可能先承擔現金壓力。"
    - "欠局帳可被旁人解讀成特殊關係，進而造成聲名效果。"
```

## B-002｜帶擋

```yaml
SOURCE_ENTRY:
  term_or_entity: "帶擋"
  chapters_example: [10, 37, 38, 64, 66, 72, 77, 162]
  category: "DEBT / INTERMEDIARY_FINANCE"
  observed_function:
    - "娘姨或房間人員可能持有債權。"
    - "債權會轉化為議價能力與營業干預能力。"
    - "清償帶擋可以解除一部分依附與控制。"
  not_equal:
    - "ownership of person"
    - "automatic authority over all decisions"
```

## B-003｜現金流危機

```yaml
EVENT_PATTERN:
  id: "CASHFLOW_CRISIS"
  chapter_anchor: 162
  state:
    receivables: ["局帳", "酒帳"]
    liabilities: ["房飯錢", "菜錢", "店帳", "帶擋利錢"]
    trigger: "歲末集中催收 + 生意衰退"
    failure_condition: "即使應收全收回，仍不足清償到期負債"
  runtime_implication:
    - "有收入紀錄不等於有現金。"
    - "wallet balance 不足以表示角色經濟狀態。"
```

---

# C｜BUSINESS / LABOR STATUS

## C-001｜牌子／營業狀態

```yaml
SOURCE_ENTRY:
  term_or_entity: "牌子"
  chapters_example: [37, 38, 72, 95, 104, 136]
  category: "BUSINESS_STATUS"
  observed_function:
    - "掛牌表示仍在對外營業／有應酬義務。"
    - "除下牌子可作退出營業流程的一個可觀察事件。"
    - "除牌不等於婚嫁已完成。"
  proposed_fields:
    - public牌面_status
    - accepts_calls
    - accepts_table_service
    - accepts_night_service
    - suspension_reason
    - exit_process_status
```

## C-002｜自家身體

```yaml
SOURCE_ENTRY:
  term_or_entity: "自家身體"
  chapters_example: [37, 66, 78, 95]
  category: "LABOR_DEPENDENCY / EXIT_AUTHORITY"
  observed_function:
    - "在部分上海案例中，是否自家身體會影響本家／娘姨對婚嫁或退出的可干預程度。"
  cross_city_contrast:
    - "天津班子另見捆帳、分帳、包帳、討人等安排，不能套上海同一制度。"
```

---

# D｜EVENT PATTERNS

## D-001｜DEBT_CLEARANCE_AND_ROLE_EXIT

```yaml
EVENT_PATTERN:
  id: "DEBT_CLEARANCE_AND_ROLE_EXIT"
  chapter: 38
  participants:
    - "倌人"
    - "娘姨／債權人"
    - "出資客人"
  sequence:
    - "既存帶擋／店帳形成依附"
    - "倌人與娘姨發生營業權衝突"
    - "第三方提供資金"
    - "逐項清償"
    - "雙方確認往來解除"
    - "娘姨退出房間體系"
  effects:
    money: ["debt cleared", "financier outflow"]
    relation: ["dependency reduced", "financier expectation may rise"]
    knowledge: ["financier may infer marriage progress"]
```

## D-002｜PUBLIC_JEALOUSY_CONFLICT

```yaml
EVENT_PATTERN:
  id: "PUBLIC_JEALOUSY_CONFLICT"
  chapter_anchor: 21
  venue_anchor: "張園"
  participants:
    - "倌人 A"
    - "倌人 B"
    - "爭議客人"
    - "朋友／調停者"
    - "可能被預先召集的外部支援者"
  sequence:
    - "客戶轉移／被認為遭奪"
    - "醋意與面子壓力形成"
    - "公共場所堵人"
    - "相罵／可能升級成動手"
    - "第三人介入調停或外部執法風險上升"
  effects:
    - "relation rupture"
    - "public visibility"
    - "rumor potential"
    - "violence / police escalation risk"
```

## D-003｜JUMP_CLIENT / 跳槽

```yaml
EVENT_PATTERN:
  id: "CLIENT_SWITCHING"
  corpus_term: "跳槽"
  chapters_example: [9, 10, 12, 22, 26, 46, 64, 76, 133, 159]
  sequence:
    - "原有往來成立"
    - "怠慢／金錢／吃醋／新吸引等原因"
    - "降低或停止原往來"
    - "轉向另一倌人"
    - "新叫局／碰和／花酒／住夜等事件"
    - "舊關係產生面子、收入或衝突後果"
```

## D-004｜MARRIAGE_NEGOTIATION_WITH_EVIDENCE

```yaml
EVENT_PATTERN:
  id: "MARRIAGE_NEGOTIATION_WITH_EVIDENCE"
  chapters_example: [66, 67, 72, 77, 78]
  required_axes:
    - expressed_intent
    - mediator_present
    - witness_present
    - money_committed
    - receipt_or_marriage_document
    - debt_clearance
    - business_status_change
    - actual_completion
  observed_rule:
    - "口頭說嫁不等於事件完成。"
    - "有媒人／見證／收據時，爭議中的證據位置明顯不同。"
    - "沒有第三人、收據或婚書時，追索與舉證明顯變弱。"
```

---

# E｜KNOWLEDGE / RUMOR / REPUTATION

## E-001｜錯誤傳聞可產生真實市場後果

```yaml
SOURCE_ENTRY:
  chapter_anchor: 64
  category: "RUMOR_MECHANISM"
  chain:
    - "可觀察付款／欠帳狀態"
    - "娘姨／大姐／相幫形成解讀"
    - "傳言某客為恩客"
    - "倌人名氣／場面受到影響"
  principle:
    - "RUMOR != FACT"
    - "RUMOR may still cause WORLD EFFECT"
```

## E-002｜花榜／報館是聲價製造器

```yaml
SOURCE_ENTRY:
  term_or_entity: "花榜"
  chapters: [91, 155, 156, 183]
  category: "REPUTATION_MARKET / MEDIA_INTERMEDIARY"
  observed_function:
    - "可由報館／主筆評定並公開傳播。"
    - "榜單可能形成叫局熱潮與自我強化。"
    - "榜單可以依資格、色藝、品行等建立聲價，也可能被金錢收買。"
    - "同一制度可同時存在 reputation discovery 與 reputation manipulation。"
  required_separation:
    - "ACTUAL_MARKET_REPUTATION"
    - "PUBLISHED_RANKING"
    - "PAID_PROMOTION"
    - "PUBLIC_BELIEF"
    - "BUSINESS_EFFECT"
```

---

# F｜ROLES / INTERMEDIARIES

## F-001｜本家

```yaml
SOURCE_ENTRY:
  term_or_entity: "本家"
  chapters_example: [2, 38, 54, 72, 77, 78, 131, 136, 151, 156, 162, 163]
  category: "VENUE_OPERATOR / ECONOMIC_INTERMEDIARY"
  observed_capabilities:
    - "提供／管理房間與場所"
    - "收房飯、菜帳等款項"
    - "對營業與客人占用空間具有利益"
    - "可參與婚嫁、帳務、房間規則與資訊證明"
    - "在不同城市／班子制度中的權力程度不同"
  caution:
    - "本家不是固定等同現代老闆，也不能與娘姨、老鴇一律合併。"
```

## F-002｜朋友／媒人／見證人

```yaml
SOURCE_ENTRY:
  category: "THIRD_PARTY_INTERMEDIARY"
  observed_functions:
    - "介紹人物"
    - "議定身價／婚嫁條件"
    - "提供見證與社會信用"
    - "調停相罵／吃醋／公開衝突"
    - "遮掩或傳播醜聞"
    - "在爭議中改變證據強弱"
  runtime_implication:
    - "許多重大事件不能只以兩人對話建模。"
```

---

# G｜VENUES / CITY NETWORK

## G-001｜張園

```yaml
SOURCE_ENTRY:
  term_or_entity: "張園"
  raw_hits: 117
  chapters_with_hits: 42
  category: "PUBLIC_SOCIAL_HUB"
  observed_functions:
    - "遊園／茶敘／碰面"
    - "熟人偶遇"
    - "相好公開同行"
    - "吃醋、堵人、相罵等衝突曝光"
    - "流言與社交可見度提高"
  runtime_implication:
    - "公共場館應具有 encounter density 與 visibility pressure，而非只是地圖背景。"
```

## G-002｜捕房／巡捕

```yaml
SOURCE_ENTRY:
  term_or_entity: "捕房／巡捕"
  category: "EXTERNAL_ENFORCEMENT_NODE"
  observed_function:
    - "租界公共衝突、打架、相罵、詐騙／爭議可能外溢至執法系統。"
    - "人物會預判巡捕／捕房風險並調整行動。"
```


## G-003｜城市制度不能只當地圖皮膚

```yaml
SOURCE_ENTRY:
  category: "CITY_RULE_SCOPE"
  corpus_presence:
    上海:
      raw_hits: 603
      chapters_with_hits: 159
    蘇州:
      raw_hits: 212
      chapters_with_hits: 63
    天津:
      raw_hits: 123
      chapters_with_hits: 32
  observed_rule:
    - "上海、蘇州、天津不只價格不同，角色稱呼、班子結構、營業規矩、客人資格與交易組合也不同。"
    - "同一交易名目不可假定跨城市語義、價格與資格完全一致。"
  runtime_implication:
    - "CITY / DISTRICT / VENUE_CLASS 必須能提供規則 overlay。"
    - "城市不是純場景背景；城市制度會改變角色可行動空間。"
```

---

# H｜目前形成的跨模組結論

```text
人物主權
  +
角色的功架／資格／應酬能力
  +
房間與本家的營業利益
  +
現金／信用／帶擋／局帳
  +
相好／恩客／婚嫁等分離資格
  +
朋友／媒人／見證人
  +
張園／戲園／客棧／公館等城市節點
  +
報館／花榜／傳聞
  +
巡捕／捕房／衙門
=
會自行運轉的蘇滬風月社會網
```

## 暫時禁止的 Runtime 簡化

- `好感度 -> 相好/恩客/婚姻`
- `花錢 -> 自動取得住夜/性愛/關係資格`
- `money balance -> 完整經濟狀態`
- `名氣 -> 真實品質`
- `人物說嫁 -> 婚嫁完成`
- `RUMOR -> FACT`
- `職業角色 -> 固定權力`
- `城市名稱 -> 只有美術皮膚差異`

---

# I｜下一步抽取

1. 建立人物 Entity 索引與跨章別名。
2. 將上海、蘇州、天津制度拆成 CITY / VENUE CLASS Provider 候選。
3. 抽出 `花榜 / 名氣 / 聲價 / 紅倌人 / 資格 / 功架` 的 Reputation graph。
4. 抽出 `朋友 / 媒人 / 本家 / 娘姨 / 相幫 / 大姐` 的 intermediary graph。
5. 抽出 `巡捕 / 捕房 / 衙門 / 官司` 的 enforcement escalation patterns。
6. 繼續收集退出營業、嫁人、從良、搬場、復出等生命週期事件。
---

# J｜CHARACTER ENTITY / ALIAS INDEX｜人物實體與稱呼解析

> 本節只處理「這個文字稱呼指向哪一個人物」；不把稱呼本身升格成人格、關係或世界資格。

## J-000｜ENTITY_ID ≠ DISPLAY_NAME

《九尾龜》人物不能用「目前看到的名字字串」直接當唯一 ID。

目前正文已確認至少存在：

- 名／字／號並存；
- 堂子內稱呼；
- 複姓截短；
- 大少／二少／先生等場域稱呼；
- 綽號；
- 同一短名指向多人；
- 同一人物存在字形變體。

```yaml
ENTITY_NAME_FORM:
  entity_id:
  surface_form:
  form_type:
    - "SURNAME_GIVEN"
    - "GIVEN_NAME"
    - "STYLE_NAME"
    - "HAO"
    - "INDUSTRY_ADDRESS"
    - "TRUNCATED_SURNAME_ADDRESS"
    - "ROLE_TITLE"
    - "NICKNAME"
    - "ORTHOGRAPHIC_VARIANT"
  speaker_scope:
  venue_scope:
  relation_scope:
  chapter_source:
  confidence:
```

### J-000A｜堂子稱呼本身會改寫姓名表面

第 91 回作者直接解釋：

- 東方小松本為複姓「東方」；
- 堂子裡倌人嫌複姓叫起來不順口，可以截掉第一字；
- 因此「東方小松」可被叫成「方小松」「方大少」；
- 作者敘事有時也沿用此一場內省稱。

因此：

```text
東方小松
= 方小松
= 小松
= 某些場景中的「方大少」

但：
「方大少」不能反向全域解析為東方小松。
```

**Runtime implication：**

> 別名不是單純 synonym table，而是 `ENTITY × SPEAKER × VENUE × REGISTER` 的稱呼關係。

---

## J-001｜章秋谷

```yaml
CHARACTER_ENTITY:
  entity_id: "JWG_CHAR_ZHANG_QIUGU"
  dominant_label: "章秋谷"
  attested_identity:
    surname: "章"
    given_name: "瑩"
    hao: "秋谷"
  attested_forms:
    - "章秋谷"
    - "秋谷"
    - "章大少"
  first_appearance: 1
  mention_chapter_count_approx: 146
  category:
    - "MAJOR_CHARACTER"
    - "SOCIAL_NETWORK_NODE"
    - "FENGYUE_EXPERIENCED_CLIENT"
  caution:
    - "章秋谷的議論屬人物／敘述視角，不得直接升格為 Runtime 公理。"
    - "章大少屬場域稱呼，並非唯一識別碼。"
```

---

## J-002｜東方小松

```yaml
CHARACTER_ENTITY:
  entity_id: "JWG_CHAR_DONGFANG_XIAOSONG"
  dominant_label: "東方小松"
  attested_identity:
    compound_surname: "東方"
    given_name: "瑤"
    hao: "小松"
  attested_forms:
    - "東方小松"
    - "方小松"
    - "小松"
    - "方大少"
  alias_rule_source: 91
  first_appearance: 1
  mention_chapter_count_approx: 18
  relation_anchor:
    - "章秋谷的重要朋友／社交節點"
  alias_status: "EXPLICITLY_EXPLAINED_BY_NARRATOR"
```

這是目前最強的 alias regression case。

---

## J-003｜方幼惲

```yaml
CHARACTER_ENTITY:
  entity_id: "JWG_CHAR_FANG_YOUYUN"
  dominant_label: "方幼惲"
  attested_identity:
    family_surname: "方"
    given_name: "寶椿"
    style_name: "幼惲"
  attested_forms:
    - "寶椿"
    - "方幼惲"
    - "幼惲"
  first_appearance: 4
  mention_chapter_count_approx: 10
  caution:
    - "正文目前未以固定字串『方寶椿』作主要稱呼；不能因姓氏可推得就冒充原文固定形式。"
```

---

## J-004｜陳文仙

```yaml
CHARACTER_ENTITY:
  entity_id: "JWG_CHAR_CHEN_WENXIAN"
  dominant_label: "陳文仙"
  attested_forms: ["陳文仙", "文仙"]
  first_appearance: 8
  mention_chapter_count_approx: 61
  major_relation_edges:
    - "章秋谷：舊有親密往來；後續出現搬離原營業空間並共同居住之事件。"
  caution:
    - "共同居住、支付開銷、私人親密、婚嫁資格必須分軸保存。"
```

---

## J-005｜四大金剛成員 Entity 組

第 72 回由敘事明確列出四大金剛的當時狀態，可確認成員：

```yaml
ENTITY_GROUP:
  group_id: "JWG_GROUP_FOUR_GREAT_JINGANG"
  corpus_label: "四大金剛"
  members:
    - "陸蘭芬"
    - "金小寶"
    - "林黛玉"
    - "張書玉"
  chapter_snapshot: 72
  group_type:
    - "PUBLIC_REPUTATION_GROUP"
    - "FENGYUE_MARKET_CLASSIFICATION"
  not_equal:
    - "friendship group"
    - "shared household"
    - "single organization"
```

### 第 72 回生命周期快照

```yaml
FOUR_JINGANG_SNAPSHOT_CH72:
  陸蘭芬:
    status: "DEAD"
  金小寶:
    business_status: "TEMPORARILY_CLOSED"
    cohabitation: "與貢春樹住在一處"
  林黛玉:
    business_status: "RESIDENTIAL / LOW_PUBLIC_ACTIVITY"
    client_access: "舊有熟客仍可往來"
  張書玉:
    business_status: "FULLY_ACTIVE"
    market_state: "聲名與生意上升"
```

**重要：**

> 同一聲價群組裡的四個人物，可以同時處於完全不同的生命週期。

所以「名妓」不是 Runtime 狀態機。

---

## J-006｜沈二寶／沉二寶

```yaml
CHARACTER_ENTITY:
  entity_id: "JWG_CHAR_SHEN_ERBAO"
  dominant_label: "沈二寶"
  surface_variants:
    - "沈二寶"
    - "沉二寶"
  first_appearance_main_arc: 161
  mention_chapter_range_main_arc: [161, 168]
  variant_status: "STRONG_SAME_ENTITY_CONTEXT / PRESERVE_SOURCE_FORM"
  normalization_rule:
    - "Corpus 可用單一 entity_id。"
    - "原文 surface form 必須保留。"
    - "不得靜默修改來源文字。"
```

同一場景內即有「沈／沉」交替，因此這是**字形變體解析**問題，而不是兩個人物。

---

## J-007｜短名碰撞鎖

目前正文已出現至少：

```yaml
SHORT_NAME_COLLISION:
  小寶:
    candidates:
      - "金小寶"
      - "王小寶"

  二寶:
    candidates:
      - "王二寶"
      - "花二寶"
      - "沈二寶"

  黛玉:
    candidates:
      - "林黛玉"
      - "金黛玉"
      - "王黛玉"

  阿金:
    candidates:
      - "陸蘭芬房中娘姨阿金"
      - "金小寶梳頭娘姨『強盜阿金』"
    merge_status: "UNRESOLVED / DO_NOT_MERGE_WITHOUT_EVIDENCE"
```

### 解析規則候選

```yaml
ENTITY_RESOLUTION_PRECEDENCE:
  1: "CURRENT_SCENE_EXPLICIT_FULL_NAME"
  2: "CURRENT_VENUE / HOUSEHOLD"
  3: "CURRENT_ROLE_BINDING"
  4: "RECENT_PROVENANCED_REFERENCE"
  5: "RELATION_GRAPH"
  6: "ALIAS_RULE"
  7: "UNKNOWN / AMBIGUOUS"
```

禁止：

```text
看到「二寶」
→ 永遠解析為沈二寶
```

---

# K｜RELATION GRAPH｜第一批跨章人物關係邊

> 本節保存「事件證明到哪裡」；不以敘述方便將往來升格為愛情、婚姻或所有權。

## K-001｜章秋谷 ↔ 陳文仙

```yaml
RELATION_EDGE:
  edge_id: "ZHANG_QIUGU__CHEN_WENXIAN"
  chapter_anchors: [8, 72]
  observed:
    - "第8回已為舊有往來，文仙不強求秋谷吃酒碰和。"
    - "第72回秋谷出資處理開銷，另租新馬路洋房，文仙搬入，秋谷亦搬入共同居住。"
  axes:
    familiarity: "HIGH"
    financial_support: "PRESENT"
    cohabitation: "PRESENT_BY_CH72"
    public_relation_label: "DO_NOT_OVERWRITE"
    marriage_status: "NOT_DERIVED_FROM_COHABITATION"
```

---

## K-002｜貢春樹 ↔ 金小寶

```yaml
RELATION_EDGE:
  edge_id: "GONG_CHUNSHU__JIN_XIAOBAO"
  chapter_anchors: [15, 72, 121]
  observed:
    - "第15回開始形成明顯互相注意。"
    - "第72回金小寶已暫時收場，與貢春樹住在一處。"
    - "第121回小寶已除牌、不做生意，勸春樹搬來同住；仍有少量熟客往來。"
  required_separation:
    - "cohabitation"
    - "business_exit"
    - "remaining_regular_clients"
    - "private_attachment"
    - "marriage"
```

這條線再次證明：

> `除牌 / 同住 / 相愛 / 熟客仍來往` 可以同時存在，不是一條單向攻略進度。

---

## K-003｜方子衡 ↔ 陸蘭芬

```yaml
RELATION_EDGE:
  edge_id: "FANG_ZIHENG__LU_LANFEN"
  chapter_anchors: [35, 37, 38, 41, 48]
  observed:
    - "由叫局、雙台、碰和迅速進入高消費往來。"
    - "第37回明示形成相好並搬入院中。"
    - "娘姨阿金、帶擋、店帳與面子共同進入兩人關係。"
    - "後續出現以婚嫁預期為核心的資金與退出營業操作。"
    - "第48回回顧蘭芬死亡，證明該線並未完成穩定婚嫁結局。"
  rule:
    - "high_spending != marriage"
    - "xianghao != exclusivity"
    - "cohabitation != completed_marriage"
```

---

## K-004｜牛幼康 ↔ 金小寶

```yaml
RELATION_EDGE:
  edge_id: "NIU_YOUKANG__JIN_XIAOBAO"
  chapter_anchors: [103, 104, 105, 106]
  observed:
    - "牛幼康以婚嫁承諾取得高度信任。"
    - "小寶降低對其他客人的應酬，造成熟客流失與房間收入壓力。"
    - "第104回與娘姨『強盜阿金』因拆頭／營業利益爆發衝突。"
    - "小寶除牌並催促央媒擇日。"
    - "牛幼康的婚嫁說法實為欺騙，後續脫身。"
  chain:
    - "PRIVATE CLAIM"
    - "CHARACTER BELIEF"
    - "BUSINESS_BEHAVIOR_CHANGE"
    - "RUMOR SPREAD"
    - "CLIENT LOSS"
    - "INTERMEDIARY CONFLICT"
    - "BUSINESS_EXIT ACTION"
    - "FRAUD DISCOVERY / RELATION FAILURE"
```

這是一條完整證明：

> **私人關係信念可以改變市場，但信念成真與否仍須獨立驗證。**

---

## K-005｜李子霄 ↔ 張書玉

```yaml
RELATION_EDGE:
  edge_id: "LI_ZIXIAO__ZHANG_SHUYU"
  chapter_anchors: [71, 72, 79]
  observed:
    - "高頻碰和、擺酒與金錢投入。"
    - "張書玉可刻意維持親熱表現，同時不給李子霄期待的住夜／近身結果。"
    - "李子霄具有嫖界資格，仍會在特定人物面前形成強烈期待與判斷偏差。"
  rule:
    - "fengyue_experience != immunity_to_manipulation"
    - "professional_intimacy != private_commitment"
    - "money_spent != access"
```

---

## K-006｜沈仲思 ↔ 洪月娥

```yaml
RELATION_EDGE:
  edge_id: "SHEN_ZHONGSI__HONG_YUEE"
  chapter_anchors: [71, 74, 77, 78, 79]
  observed:
    - "洪月娥為沈仲思既有往來倌人。"
    - "關係後續捲入債務、婚嫁／利益與第三人結構。"
    - "第79回由敘事總結為兩人遭遇騙局後的關係收場。"
  caution:
    - "第79回帶有作者強烈勸世評價；事件事實與作者價值判斷必須分離。"
```

---

# L｜ENTITY / RELATION 對未來 Runtime 的最小結論

目前已可確認：

```text
ENTITY
≠ 名字字串

RELATION
≠ 好感度

ALIAS
≠ 全域同義詞

PUBLIC GROUP
≠ 共同行動單位

COHABITATION
≠ 婚姻

BUSINESS EXIT
≠ 關係完成

CHARACTER BELIEF
≠ WORLD FACT
```

未來人物層至少需要：

```yaml
CHARACTER_RUNTIME_MINIMUM:
  entity_id:
  name_forms:
  current_venue:
  current_household:
  public_roles:
  business_status:
  lifecycle_status:

  relations:
    - relation_partner_id:
      familiarity:
      transaction_history:
      public_label:
      private_claims:
      cohabitation:
      marriage_process:
      rumor_state:

  knowledge:
    - proposition:
      provenance:
      status:
```

但目前仍屬 **Corpus-derived schema candidate**，不是正式 Runtime。

---

# M｜下一輪抽取優先

1. 把人物 Entity Index 從第一批核心人物擴至「主要客人／倌人／娘姨／本家／朋友」。
2. 建立 `HOUSEHOLD / ROOM` 歸屬，解決「阿金／阿玉／大姐」等短名碰撞。
3. 建立人物跨城市移動軸：蘇州 ↔ 上海 ↔ 天津。
4. 建立 `FOUR_JINGANG` 聲價群組的時間切片，不把四人固定成同一狀態。
5. 將 `除牌／收場／住家／搬場／復出／嫁人／死亡` 抽成生命周期事件族。
6. 開始建立 `CITY + VENUE + NAME_REGISTER`，讓稱呼規則與場域制度接起來。
---

# N｜HOUSEHOLD / ROOM GRAPH｜房間不是背景，而是局部社會單位

> 本節只把原作已反覆出現的「房間／院中人員／本家／相幫」關係抽成 Corpus 結構；仍不是正式 Runtime。

## N-001｜ROOM = LOCAL ECONOMIC / SERVICE / KNOWLEDGE UNIT

```yaml
SOURCE_ENTRY:
  term_or_entity: "房間／房間裡人"
  chapters_example: [19, 41, 43, 64, 72, 92, 93, 100, 104, 132, 162, 163, 187]
  category: "HOUSEHOLD_UNIT / LOCAL_SOCIAL_NODE"
  observed_function:
    - "房間不只是物理臥室；它包含倌人、娘姨、大姐、相幫接口、本家帳務與客人出入。"
    - "房間內人員的收入與倌人生意直接相關。"
    - "房間人員可協助接客、招呼、傳話、調桌、陪出門、叫車、送禮、催局、處理客人。"
    - "房間人員也是局部知情與流言節點。"
  not_equal:
    - "courtesan private bedroom only"
    - "static map tile"
    - "single owner-controlled inventory object"
```

第104回強盜阿金明說「屋裡向幾幾化化人」靠金小寶一人的生意吃飯，並提到事先講明「生意浪有拆頭」。  
第162回沈二寶生意衰退後，房間裡娘姨、大姐因「一個大錢都摸不著」而直接改變態度。

**初步結論：**

> 房間是一個會因客流、帳務、賞錢、拆頭與債務而改變行為的微型經濟單位。

---

## N-002｜房間人員的利益不等於倌人利益

```yaml
HOUSEHOLD_INTEREST_SEPARATION:
  chapter_anchors: [37, 38, 104, 162, 163]
  observed:
    - "倌人可能想少做客、停牌、嫁人或偏向單一客人。"
    - "娘姨／大姐可能因拆頭、帶擋、賞錢與日常收入而希望維持生意。"
    - "本家可能因房飯、菜帳、房間占用與預期收益而反對停業或離場。"
  principle:
    - "COURTESAN_GOAL != ROOM_STAFF_GOAL"
    - "ROOM_STAFF_GOAL != OWNER_GOAL"
    - "OWNER_GOAL != CLIENT_GOAL"
```

因此「同一房間」不能建成一個共同意志。

---

## N-003｜房間有 ACCESS CONTROL

```yaml
EVENT_PATTERN:
  id: "ROOM_ACCESS_CONTROL"
  chapter_anchors: [19, 132]
  observed_examples:
    - "第19回：寶珠姐因內房已有客，攔住金和甫等人，不讓直接闖入。"
    - "第132回：馬山甫只能透過小大姐／跟局大姐傳話；本人也知道上海堂子不能隨意混闖房間。"
  possible_actions:
    - "迎入"
    - "安排客堂等候"
    - "代傳"
    - "回覆不在／無空"
    - "拒絕進房"
    - "升級為衝突"
```

所以：

> `VENUE_ACCESS`、`ROOM_ACCESS`、`PERSON_ACCESS` 必須分層。

---

## N-004｜房間也有 PRIVACY STATE

```yaml
SOURCE_ENTRY:
  chapter_anchor: 187
  category: "ROOM_PRIVACY / KNOWLEDGE_PROVENANCE"
  observed:
    - "辛修甫與蘇青青咬耳談事時，房間裡人看見情勢後故意退開。"
    - "敘事明說：談了半天，娘姨、大姐仍不知道談話內容。"
  principle:
    - "SAME_HOUSEHOLD != KNOWS_PRIVATE_CONVERSATION"
    - "PHYSICAL_PROXIMITY != CONTENT_ACCESS"
```

這是未來 `KNOWLEDGE_REQUIRES_SOURCE` 的直接 Corpus 證據。

候選：

```yaml
ROOM_PRIVACY_STATE:
  public_room:
  active_cast:
  staff_present:
  staff_withdrawn:
  audible_to:
  visible_to:
  message_relayed_to:
```

---

## N-005｜房間人員可被上位利益方用作監看者

```yaml
SOURCE_ENTRY:
  chapter_anchor: 163
  category: "SURVEILLANCE_BY_HOUSEHOLD"
  observed:
    - "女本家金姐因怕沈二寶欠債逃走，暗中吩咐其娘姨、大姐緊緊跟隨。"
    - "監看目的源於債權與逃逸風險，而非『本家天然全知』。"
  knowledge_effect:
    - "staff observation may be intentionally generated by an owner instruction"
```

這使得：

> `觀察來源` 本身也可能是一個世界事件。

---

# O｜ROLE ASSIGNMENT｜職業稱呼不是人物永久身份

## O-001｜娘姨

```yaml
ROLE_ENTRY:
  role: "娘姨"
  raw_hits: 356
  chapters_with_hits: 99
  observed_capabilities:
    - "房內日常服侍與梳洗"
    - "迎客／招呼"
    - "傳話／請人"
    - "陪同出門或異地短住"
    - "調停或介入客妓衝突"
    - "代為回覆叫局／客人"
    - "持有帶擋或參與拆頭"
    - "依自身經濟利益改變合作態度"
  attested_sub_labels:
    - "梳頭娘姨"
    - "粗做娘姨"
    - "做手娘姨"
  caution:
    - "這些標籤目前只記錄原作用語與 observed function，不先製造完整職級表。"
```

### 重要案例

```yaml
ROLE_CASE:
  character: "強盜阿金"
  host: "金小寶"
  chapter: 104
  label: "梳頭娘姨"
  economic_interest:
    - "拆頭"
    - "房間生意收入"
  event:
    - "因金小寶偏向牛幼康、客流下降而公開衝突並準備離開"
```

```yaml
ROLE_CASE:
  character: "小妹娘"
  host: "沈二寶"
  chapter: 162
  label: "娘姨"
  debt_claim: 500
  effect:
    - "因持有帶擋，沈二寶即使不滿也不敢任意翻臉"
```

---

## O-002｜大姐

```yaml
ROLE_ENTRY:
  role: "大姐"
  raw_hits: 164
  chapters_with_hits: 73
  observed_capabilities:
    - "迎客與房內招呼"
    - "跟隨倌人出局／出門"
    - "傳話與回覆"
    - "陪侍、調桌、送禮、跑腿"
    - "作為現場目擊者與傳聞節點"
    - "依房間生意取得收入／賞錢"
  attested_sub_labels:
    - "跟局大姐"
    - "小大姐"
  caution:
    - "『小大姐』目前不自動解讀為固定年齡／職級；需後續 corpus 交叉。"
```

### 跟局大姐作為人物—外界接口

第132回：

```text
馬山甫
→ 找陸韻仙
→ 小大姐不處理
→ 跟局大姐接受訊息
→ 回房
→ 回覆「先生嘸撥工夫」
```

這不是純裝飾 NPC，而是一個實際 `MESSAGE / ACCESS GATE`。

---

## O-003｜相幫

```yaml
ROLE_ENTRY:
  role: "相幫"
  raw_hits: 128
  chapters_with_hits: 53
  observed_capabilities:
    - "樓下報客人上來"
    - "高聲報叫局／出局地點"
    - "收送局票與請客票"
    - "催轉局"
    - "分頭送請客票"
    - "叫菜／搬菜／端送物品"
    - "僱馬車／轎子"
    - "收檯面等現場款項"
  special_label:
    - "帶房間的相幫"
  knowledge_position:
    - "頻繁跨房間／樓層／客席移動，天然可能成為高流動資訊節點；但每一筆知情仍需實際來源。"
```

**重要：**

> 相幫不是世界廣播器；他只是具有高交通量的資訊節點。

---

## O-004｜本家／女本家／老鴇

```yaml
ROLE_ENTRY:
  role_family:
    - "本家"
    - "女本家"
    - "老鴇"
  observed_capabilities:
    - "提供／管理營業房間"
    - "房飯／菜帳／房錢等帳務"
    - "對倌人停業、離場、占用房間具有直接經濟利益"
    - "在部分制度中可安排房間、要求結帳、監看債務人"
    - "可因未來收益與客源而談判讓步"
  caution:
    - "三個稱呼在不同城市／文本語境不保證完全同義。"
    - "權力來源需拆成 venue authority / debt claim / contract / custom，而不是職稱一鍵全權。"
```

第136回非常重要：

> 陸韻仙暫時離開原處去照料馬山甫，本家起初不同意；直到章秋谷承諾以每日固定局數補足營業利益，才答應。

所以：

```text
本家反對人物離場
不必然 = 人身所有權
也可能 = 預期營業收入受損
```

---

# P｜ROLE MOBILITY｜角色存在職涯流動

## P-001｜阿毛：大姐 → 女本家

```yaml
ROLE_TRANSITION:
  character: "阿毛"
  chapter: 2
  source_state: "大姐出身"
  later_state: "天津南班女本家"
  enabling_factor:
    - "已有積蓄"
  observed:
    - "可自行開設／經營南班堂子"
```

這直接證明：

> `ROLE != CHARACTER_IDENTITY`

---

## P-002｜阿玉：跟局大姐 → 做手娘姨

```yaml
ROLE_TRANSITION:
  character: "阿玉（沈二寶舊日跟局大姐）"
  chapter: 162
  prior_assignment:
    host: "沈二寶"
    role: "跟局大姐"
  later_assignment:
    host: "花婷婷"
    role: "做手娘姨"
  relation_residue:
    - "離開舊房間後仍保留對沈二寶的私人情誼與舊日資訊"
```

**高價值結論：**

> 人員換房間、換角色後，`ROLE_ASSIGNMENT` 會變，但人物記憶與舊關係不會 reset。

候選 schema：

```yaml
ROLE_ASSIGNMENT:
  character_id:
  role_label:
  household_id:
  venue_id:
  start_event:
  end_event:
  compensation_relation:
  debt_relation:
  information_access:
  mobility_status:
```

---

# Q｜NAMED HOUSEHOLD ENTITIES｜第一批房間人員索引

> 同名嚴重；以下只在宿主／房間已可辨識時建立 local binding。

```yaml
HOUSEHOLD_BINDING:
  "許寶琴房間":
    chapter_anchor: 1
    staff:
      - {name: "阿彩", role: "娘姨"}
      - {name: "阿仙", role: "大姐"}

  "張書玉房間":
    chapter_anchor: 10
    staff:
      - {name: "阿寶姐", role: "娘姨"}

  "陳文仙房間":
    chapters: [19, 46, 64, 72]
    staff:
      - {name: "寶珠姐", role: "娘姨", note: "知風識勢；可擋客、調停、招呼"}

  "陸蘭芬房間":
    chapters: [37, 38, 41]
    staff:
      - {name: "阿金", role: "娘姨", note: "帶擋／營業利益重要"}
      - {name: "巧寶", role: "大姐"}

  "范彩霞房間":
    chapters: [92, 93]
    staff:
      - {name: "阿金", role: "娘姨"}
      - {name: "阿玉", role: "大姐"}
    collision_lock:
      - "不得與其他阿金／阿玉自動合併"

  "陸麗娟房間":
    chapters: [100, 113, 132]
    staff:
      - {name: "金寶", role: "娘姨"}
      - {name: "阿金妹", role: "大姐"}

  "金小寶房間":
    chapters: [104, 105]
    staff:
      - {name: "強盜阿金", role: "梳頭娘姨"}
      - {name: "阿囡", role: "大姐"}

  "沈二寶房間":
    chapters: [162, 163]
    staff:
      - {name: "阿招", role: "大姐"}
      - {name: "小妹娘", role: "娘姨", note: "持有五百塊帶擋"}
      - {name: "阿玉", role: "舊日跟局大姐", status: "FORMER_ASSIGNMENT"}
    owner:
      - {name: "金姐", role: "女本家／老鴇"}
```

---

# R｜房間制度具有 CITY SCOPE

## R-001｜上海：局部房間界線很強

```yaml
CITY_ROOM_MODEL:
  city: "上海"
  evidence_chapters: [64, 132, 162, 163, 187]
  observed:
    - "存在明顯『某倌人的房間／房間裡人』概念。"
    - "人員可附著特定房間。"
    - "外客不能任意混闖房間。"
    - "局帳、酒帳、房飯、帶擋、賞錢、拆頭會在房間周邊形成局部經濟。"
```

## R-002｜天津：不能直接套上海 ROOM MODEL

第144回明示：

```yaml
CITY_ROOM_MODEL:
  city: "天津"
  chapter_anchor: 144
  observed:
    - "姑娘可為捆帳伙計、分帳伙計、老鴇討人、包帳伙計。"
    - "合班倌人受老鴇節制。"
    - "文本特別說『沒有什麼包房間做伙計的名目』。"
    - "客人邊界不像上海房間制：你的客人我也可應酬，我的客人你也可陪待。"
```

因此正式鎖：

```text
SHANGHAI_ROOM_MODEL
!=
TIANJIN_BANZI_MODEL
```

`HOUSEHOLD / ROOM` 必須由城市／場館 Provider 解釋，不能做全域硬規則。

---

# S｜本輪形成的新硬結論候選

```text
ROOM
≠ 物理房間

ROOM
= 局部經濟 + 服務 + 出入 + 知情節點

ROLE
≠ 人物永久身份

ROLE_ASSIGNMENT
= 可移動、可終止、可轉職

STAFF_PRESENT
≠ STAFF_KNOWS_PRIVATE_CONTENT

同房間利益共同
≠ 同一意志

本家有利益與權力
≠ 無條件人物所有權

上海房間制
≠ 天津班子制
```

---

# T｜下一輪抽取優先

1. 抽 `除牌／收場／住家／搬場／復出／嫁人／死亡` 的生命周期事件族。
2. 建 `HOUSEHOLD_ID` 與人物移動事件，處理「房間換人但人物記憶不 reset」。
3. 抽 `堂簿／酒帳／局帳／房飯／菜帳／拆頭／帶擋` 的完整 ledger graph。
4. 抽 `PUBLIC / ROOM / PRIVATE` 三層可見度與傳聞傳播。
5. 補蘇州 ROOM / 書寓制度，避免只用上海與天津形成二元偏見。
---

# U｜LIFECYCLE EVENT FAMILY｜人物營業／退出／復出生命週期

> 本節只記錄原作中可觀察的狀態轉換。不得把「想嫁」「除牌」「同住」「從良」「正式婚嫁」「退出風月場」壓成一個 Boolean。

## U-000｜生命周期不是單線狀態機

目前正文已確認至少存在以下彼此可分離的狀態／事件：

```yaml
LIFECYCLE_AXES:
  business_visibility:
    - "掛牌／營業"
    - "暫停"
    - "除牌"
    - "不做生意"
    - "暫時收場"

  residence:
    - "原堂子／房間"
    - "另租寓所"
    - "住家"
    - "與特定客人同住"

  client_access:
    - "公開接客"
    - "只留熟客"
    - "限制性接觸"
    - "不再見客"

  marriage_process:
    - "口頭意向"
    - "媒人介入"
    - "議價／身價／下腳開銷"
    - "清帳"
    - "停止接客"
    - "搬離"
    - "成婚／同住"
    - "婚姻失敗／下堂"
    - "配偶死亡"

  return_to_market:
    - "復出"
    - "重落風塵"

  terminal:
    - "死亡"
```

**硬鎖：**

```text
BUSINESS_EXIT
!= MARRIAGE

MARRIAGE_INTENT
!= MARRIAGE_COMPLETION

COHABITATION
!= MARRIAGE

FROMGLIANG_INTENT
!= FROMGLIANG_COMPLETION

PUBLIC_EXIT
!= NO_PRIVATE_CLIENT_CONTACT

RETURN_TO_MARKET
may follow:
  - marital breakdown
  - widowhood
  - other unresolved causes
```

---

## U-001｜掛牌／除牌

```yaml
LIFECYCLE_EVENT:
  event: "REMOVE_SIGN / 除牌"
  chapters_example: [72, 95, 104, 121, 192]
  observed_function:
    - "公開停止營業的重要可觀察信號。"
    - "可由倌人主動要求相幫執行。"
    - "常與婚嫁意向、停止接客或搬離原房間相連。"
  not_equal:
    - "marriage completed"
    - "relationship exclusive"
    - "all old clients severed"
```

### 第72回｜陳文仙

事件鏈：

```text
表明嫁人
→ 叫相幫除牌
→ 本家清帳
→ 看房
→ 搬場
→ 另租新馬路洋房
→ 與章秋谷同住
```

原作同時明示：

- 文仙不欠娘姨帶擋，因此娘姨雖不願意，也難以攔阻；
- 本家帳、房錢、菜錢要另行處理；
- 原房間人員不是全體一起搬走，只有部分人繼續服侍。

所以：

> `REMOVE_SIGN` 是一個營業事件，不是「婚姻完成」按鈕。

### 第104回｜金小寶

```text
與娘姨阿金爆發衝突
→ 因牛幼康婚嫁承諾而要求除牌
→ 催牛幼康央媒擇日
→ 牛幼康失蹤／轉投祝小春
→ 婚嫁未完成
```

這是最強反例：

> **除牌成功，婚嫁仍可以失敗。**

---

## U-002｜暫時收場

```yaml
LIFECYCLE_EVENT:
  corpus_form: "暫時收場"
  chapter_anchor: 72
  category: "TEMPORARY_BUSINESS_EXIT"
  observed:
    - "金小寶暫時收場、不做生意，但與貢春樹同住。"
    - "後續仍可保留熟客往來與社交活動。"
```

### 詞義鎖

`收場` 在全書有大量一般「事情如何收場／結局」義。

因此：

```yaml
LEXICAL_DISAMBIGUATION:
  term: "收場"
  business_status_use: "CONTEXT_REQUIRED"
  general_outcome_use: "COMMON"
```

不能把所有 `收場` raw hit 都統計成退出營業事件。

---

## U-003｜歇夏

```yaml
LIFECYCLE_EVENT:
  event: "SUMMER_RECESS / 歇夏"
  chapters_example: [38, 66, 159]
  category: "SEASONAL_TEMPORARY_SUSPENSION"
  observed_function:
    - "端陽後可暫停公開營業。"
    - "可回掉原營業房子、另租寓所。"
    - "停業期間仍有生活開銷。"
    - "可能由特定客人提供月度開銷。"
    - "舊熟客仍可能有限度出入。"
```

### 第66回｜金寓

```text
端陽後歇夏
→ 回掉公陽里房子
→ 搬觀盛里
→ 暫時收場
→ 王太史承擔日常開銷
→ 表面上形成高強度單一客人關係期待
→ 私下仍與另一客人往來
```

### 第159回｜范彩霞

```text
觀盛里歇夏
→ 陳海秋每月貼二百
→ 不做生意
→ 一兩個舊熟客仍可偶然走動
→ 一般客人難以進入
```

所以：

> `歇夏` 是「季節性停業 + access 改變 + financing 改變」，不是單純放假。

候選欄位：

```yaml
SEASONAL_SUSPENSION:
  reason:
  start_time:
  expected_end:
  public_business_open:
  residence_changed:
  sponsor_support:
  allowed_regular_clients:
  general_client_access:
```

---

## U-004｜住家

```yaml
LIFECYCLE_EVENT:
  corpus_form: "住家"
  chapter_anchor_high_value: 72
  category: "RESIDENTIAL_MARKET_STATUS"
```

第72回林黛玉：

```text
住在惠秀里
→ 算個住家
→ 舊日相熟客仍可過去坐坐
→ 本人不大出來
```

因此：

```text
住家
!= 完全退出風月市場
!= 婚嫁
!= 全客戶斷絕
```

另第171回存在「住家野雞」的市場分類，因此 `住家` 也有不同 corpus context。

**暫時鎖：**

> `住家` 不能直接做成全域單一定義；需以角色類型、場域與上下文判讀。

---

## U-005｜從良

```yaml
LIFECYCLE_EVENT_FAMILY:
  corpus_form: "從良"
  raw_hits_index: 18
  observed_modes:
    - "人物願望／意向"
    - "旁人勸說"
    - "媒合婚嫁"
    - "作為債務／本家談判的退出威脅"
    - "實際進入停止接客與清帳程序"
```

### 第156–158回｜月芳

目前可確認的事件鏈：

```text
月芳表達從良意願
→ 金觀察作媒
→ 孫英玉允娶
→ 發現月芳有大量虧空
→ 第三人共同籌款
→ 帳目清償
→ 向本家說明
→ 月芳停止見一般客人
→ 外在打扮／應酬方式改變
```

但 Corpus 必須保留：

```text
「想從良」
!=
「已完成正式婚姻／永久退出」
```

正文第158回可直接確認的是：

- 「嫁人的事情」已向本家說明；
- 帳目已付清；
- 月芳不肯再見客人。

因此目前最安全狀態：

```yaml
YUEFANG_CH158:
  fromliang_intent: "CONFIRMED"
  mediator_match: "CONFIRMED"
  debt_clearance: "CONFIRMED"
  general_client_access: "CLOSED"
  public_transition: "IN_PROGRESS / STRONG"
  final_marriage_completion: "DO_NOT_OVERSTATE_BEYOND_SOURCE"
```

### 第165回｜沈二寶

第165回女本家金姐擔心：

```text
沈二寶索性不做生意
→ 綽一個大爛污
→ 往公堂說「自願從良」
→ 金姐債權可能落空
```

這裡 `從良` 同時也是**可影響債權人行為的退出威脅**。

所以：

> 從良不是純感情事件，也是經濟／法律／場內權力事件。

---

## U-006｜嫁人／婚嫁退出

```yaml
LIFECYCLE_EVENT_FAMILY:
  event: "MARRIAGE_EXIT"
  observed_components:
    - "expressed_intent"
    - "counterparty_acceptance"
    - "mediator"
    - "money / 身價 / 下腳開銷"
    - "debt_clearance"
    - "sign_removal"
    - "client_access_change"
    - "residence_change"
    - "cohabitation"
    - "formal_social_recognition"
```

正文反覆證明：

> 婚嫁是事件鏈，不是單一台詞。

第95回薛金蓮尤其清楚：

```text
與鄭小麻子盟誓
→ 除牌不做生意
→ 親生娘原則上不阻
→ 但要求一千銀下腳開銷
→ 金蓮另尋資金來源
```

`自家身體`、身價、院中開銷與家屬態度都會改變退出成本。

---

## U-007｜復出

```yaml
LIFECYCLE_EVENT:
  corpus_form: "復出"
  chapters_example: [22, 26, 29, 150, 173]
  category: "RETURN_TO_FENGYUE_MARKET"
```

目前至少確認兩種來源：

### A｜婚姻破裂／下堂後復出

第22回林黛玉：

```text
嫁邱八
→ 婚姻生活
→ 下堂
→ 回上海
→ 復出／重落風塵
```

敘事直接稱：

> 「林黛玉嫁人復出的情節」

### B｜夫死後復出

第173回賽金花：

```text
婚嫁／離開原風月身份
→ 丈夫死亡
→ 復出
→ 重落風塵
```

正文直接使用「夫死復出」。

所以：

```text
復出
!= 只有「婚姻失敗」
```

候選：

```yaml
RETURN_EVENT:
  prior_exit_type:
  return_trigger:
  prior_relation_status:
  prior_residence:
  new_market_entry:
  retained_reputation:
  retained_contacts:
  debt_on_return:
```

---

## U-008｜死亡不是清零

第48回陸蘭芬病死後：

- 仍有未收／未付局帳；
- 原客人是否處理舊帳成為死後事件；
- 親生娘仍受經濟後果；
- 其他倌人因她死亡產生情緒與價值判斷；
- 她的聲價與前史繼續作為社會記憶。

因此：

```yaml
DEATH_EVENT:
  character_active: false
  unsettled_ledger_may_remain: true
  relation_memory_may_remain: true
  rumor_and_reputation_may_remain: true
  household_effects_may_remain: true
```

硬鎖：

> **死亡 = 人物行動終止；不等於世界對她的所有狀態立刻歸零。**

---

# V｜LIFECYCLE SNAPSHOTS｜高價值時間切片

## V-001｜四大金剛 CH72

```yaml
SNAPSHOT_CH72:
  陸蘭芬:
    lifecycle: "DEAD"

  金小寶:
    lifecycle: "TEMPORARY_BUSINESS_EXIT"
    public_business: "CLOSED"
    cohabitation: "貢春樹"
    residual_clients: "POSSIBLE"

  林黛玉:
    lifecycle: "RESIDENTIAL_LOW_VISIBILITY"
    market_form: "住家"
    old_clients: "LIMITED_ACCESS"
    public_activity: "LOW"

  張書玉:
    lifecycle: "FULL_ACTIVE"
    public_business: "OPEN"
    reputation: "HIGH / RISING"
```

同一聲價群組可同時落在四個完全不同生命周期節點。

---

## V-002｜金小寶 CH104 → CH121

```yaml
TIMELINE:
  CH104:
    trigger: "牛幼康婚嫁承諾 + 房間衝突"
    event: "除牌"
    marriage_result: "FAILED / NOT_COMPLETED"

  CH121:
    public_business: "STILL_CLOSED"
    familiar_clients: "STILL_VISIT"
    cohabitation: "貢春樹"
    social_activity: "CONTINUES"
```

因此：

> `BUSINESS_CLOSED` 可以持續很久，但人物仍活在社交網內。

---

## V-003｜月芳 CH156 → CH158

```yaml
TIMELINE:
  CH156:
    fromliang_intent: true
    mediator_search: true

  CH157:
    partner_match: "孫英玉"
    debt_problem: "BLOCKING"
    third_party_finance: "ACTIVATED"

  CH158:
    owner_notified: true
    accounts_cleared: true
    general_clients_refused: true
    transition_visibility: "HIGH"
```

這是一條最完整的「退出市場前置程序」樣本。

---

# W｜生命周期對未來 Runtime 的最小候選

```yaml
CHARACTER_LIFECYCLE_STATE:
  alive:
  public_business_status:
  sign_status:
  seasonal_suspension:
  residence_status:
  venue_binding:
  general_client_access:
  regular_client_access:
  cohabitation:
  fromliang_intent:
  marriage_process:
  debt_clearance:
  owner_settlement:
  return_status:
  return_trigger:
```

但這些欄位目前仍屬：

`CORPUS_DERIVED_SCHEMA_CANDIDATE`

不是正式 Runtime。

---

# X｜本輪新增禁止簡化

```text
除牌 -> 已嫁
歇夏 -> 永久退出
住家 -> 完全不接客
同住 -> 婚姻
從良意願 -> 從良完成
媒人成功 -> 婚姻完成
清帳 -> 婚姻完成
復出 -> 一定因婚姻失敗
死亡 -> 關係／帳目／名聲全部清零
```

---

# Y｜下一輪抽取優先

1. 建完整 `LEDGER GRAPH`：堂簿／局帳／酒帳／房飯／菜帳／帶擋／拆頭／賞錢。
2. 把生命周期事件與 `HOUSEHOLD_ID` 連接，確認搬場後哪些人員、帳務、關係跟著走。
3. 抽 `PUBLIC / ROOM / PRIVATE` 三層可見度與消息傳播。
4. 補蘇州書寓／堂子制度與上海對照。
5. 建 `REPUTATION → CLIENT FLOW → CASHFLOW` 事件鏈。
---

# Z｜LEDGER GRAPH｜帳簿、債權、現金流與社會資格

> 本節依《九尾龜》正文抽取帳務結構。  
> 核心不是「加一個金錢數值」，而是保存：**哪一個事件形成哪一筆帳、誰欠誰、誰記帳、何時收、實收多少、誰能看見，以及這筆帳如何反過來影響人物與關係。**

## Z-000｜帳不是單一價格，而是事件債權的累積

```yaml
LEDGER_LINE_ITEM_CANDIDATE:
  line_id:
  source_event_id:
  account_type:
  creditor:
  debtor:
  face_amount:
  incurred_at:
  venue:
  household_id:
  document_source:
  collector:
  due_window:
  expected_collection:
  actual_collection:
  settlement_discount:
  settlement_status:
  relation_effect:
  reputation_effect:
  knowledge_provenance:
```

目前正文已經證明：

```text
TRANSACTION EVENT
→ LINE ITEM
→ ACCOUNT / 帳
→ RECEIVABLE or PAYABLE
→ COLLECTION / SETTLEMENT
→ CASH
```

這幾層不能壓成一個 `money -= X`。

---

# ZA｜堂簿／酒局帳／局帳

## ZA-001｜「開堂簿」具有建立往來資格的功能

第12回章秋谷勸初到上海的貢春樹在張書玉處請酒，明說：

> 「無非開個堂簿的意思，以後便可往來。」

目前只有這個高價值明確用例，因此不把它擴張成全上海唯一開戶規則；但至少可以確認：

```yaml
SOURCE_ENTRY:
  corpus_form: "開個堂簿"
  chapter: 12
  category: "ACCOUNT_OPENING / SOCIAL_ENTRY"
  observed_function:
    - "藉一次正式消費／請酒建立後續往來的帳務與社交入口。"
  caution:
    - "單一明確用例；不先推導所有客人都必須經同一程序。"
```

**重要結論：**

> 帳簿不只是會計紀錄；在部分場景中，它本身就是社交往來的制度接口。

---

## ZA-002｜堂簿保存酒局應收

第162回：

```text
堂簿上的局帳和酒帳
```

花婷婷一線又寫：

```text
堂簿上的酒局帳
```

因此至少可安全抽出：

```yaml
HOUSE_LEDGER:
  ledger_type: "堂簿"
  may_record:
    - "局帳"
    - "酒帳／酒局帳"
```

但不先假設堂簿只記這兩種項目。

---

## ZA-003｜酒局帳可以是混合帳，不是單一交易類別

第100回陳海秋收到范彩霞房間抄出的酒局帳，其中同一張帳至少合併：

```text
二十六台菜錢
十九場和錢
一百二十多個局錢
+
先前碰和時向范彩霞借的一百塊本錢
```

合計六百多元。

因此：

```yaml
COMPOSITE_CLIENT_ACCOUNT:
  client:
  room_or_courtesan:
  line_items:
    - table_food
    - penghe
    - calls
    - temporary_cash_advance
  total_face_amount:
```

硬鎖：

> `酒局帳 ≠ 只有酒錢`  
> `ACCOUNT TOTAL ≠ 單一事件`

每個 line item 必須能追回來源。

---

# ZB｜應收帳的「帳面值」與「可收現金」分離

## ZB-001｜折帳

第128回陸麗娟：

```text
帳面約二千多
扣除兩個不在上海的客人約四百多
餘約一千六百
「收著一個八折帳就算好」
```

第162回花婷婷：

```text
酒局帳約八百
最後只打九折
敘事稱已經算極好
```

所以正式建立：

```yaml
RECEIVABLE_STATE:
  face_amount:
  collectible_scope:
  debtor_location:
  expected_recovery_rate:
  actual_recovery_rate:
  actual_cash_received:
```

硬鎖：

```text
FACE_RECEIVABLE
!= EXPECTED_COLLECTION
!= ACTUAL_COLLECTION
```

---

## ZB-002｜客戶不在本地會直接降低可收性

第128回明確把「不在上海」的兩戶先從年末可收帳中剔除。

因此帳務不能只看：

```text
debtor owes 200
```

還要看：

```yaml
COLLECTION_ELIGIBILITY:
  debtor_location:
  reachable:
  collector_available:
  due_window:
  social_leverage:
```

---

# ZC｜節期結算週期

正文反覆顯示：

```text
端午
中秋
年底／年節
```

是收帳與開銷高度集中的壓力窗口。

## ZC-001｜FESTIVAL_COLLECTION_CYCLE

```yaml
EVENT_PATTERN:
  id: "FESTIVAL_COLLECTION_CYCLE"
  chapters_example: [64, 99, 100, 128, 162, 164, 165]
  sequence:
    - "節期逼近"
    - "堂子／房間開始抄帳、收帳"
    - "娘姨／大姐／相關人員外出尋客"
    - "客戶清局帳／酒帳／菜帳等"
    - "倌人再以實收現金支付本家、店家、帶擋、生活開銷"
    - "不足者進入借貸／延期／催逼／關係衝突"
```

第99回尤其明確：

> 端午前娘姨、大姐在四馬路穿梭收帳；漂帳客人則躲避。

所以：

> 世界時間不是裝飾；節期會改變 NPC 行為密度與現金流壓力。

---

# ZD｜負債端：房飯／菜帳／店帳／房租

## ZD-001｜本家相關帳

正文目前明確出現：

```yaml
HOUSE_PAYABLE_TYPES:
  - "房飯錢／房飯帳"
  - "菜錢／菜帳"
  - "房錢／房租"
  - "伙食"
  - "零用"
```

這些不能全併成 `rent`。

第131回馬山甫收到紅紙帳單：

```text
房租
伙食
零用賞錢
```

合計近三百元，而且他自己的局帳已經另外結清。

因此：

```text
CLIENT_FENGYUE_ACCOUNT
!= RESIDENCE / HOUSEHOLD_ACCOUNT
```

---

## ZD-002｜店帳是外部市場債務

第64、90、162–165回可確認：

- 銀樓；
- 綢緞店；
- 洋貨店；
- 家生店；
- 馬車行；
- 戲館；
- 大菜館；
- 其他店舖；

都能形成跨期欠帳。

第164回沈二寶把店舖發票交帳房先生核算，七百多元中以馬車行、戲館、大菜館最多。

因此：

```yaml
EXTERNAL_PAYABLE:
  merchant_id:
  category:
  invoice_or_account_slip:
  amount:
  aging:
  partial_payment:
  collection_pressure:
```

---

# ZE｜帶擋、利錢、拆頭：三種不同權利／成本

## ZE-001｜帶擋 = 債務／融資關係

既有 V0.1–V0.4 結論保留：

- 娘姨可替倌人掮帶擋；
- 帶擋可形成債權；
- 債權會轉成議價與營業壓力；
- 清償帶擋可以解除一部分依附。

---

## ZE-002｜利錢 ≠ 拆頭

第37回陸蘭芬說得很清楚：

```text
娘姨掮三千帶擋
「拆仔利錢勿算，另外還要……拆頭」
```

因此：

```text
INTEREST / 利錢
!=
REVENUE SHARE / 拆頭
```

這是非常重要的帳務分離。

候選：

```yaml
FINANCING_RELATION:
  principal:
  interest_terms:
  intermediary:
  revenue_share_terms:
  repayment_status:
```

---

## ZE-003｜拆頭也可以直接綁「生意」

第104回金小寶的梳頭娘姨阿金明說：

```text
一開始講明「生意上有拆頭」
```

客流下降後，她因分不到收入而爆發衝突。

所以 `拆頭` 至少存在：

```text
BUSINESS_REVENUE_SHARE
```

的 observed use。

但目前不先製造固定比例。

---

# ZF｜下腳與賞錢必須分開

## ZF-001｜下腳

正文顯示上海案例中：

- 住夜後可有下腳；
- 金額依人物／事件不同；
- 房間人員可能有「下腳拆」；
- 第149回天津人物明說當地「沒有下腳」的規矩。

因此：

```yaml
SOURCE_ENTRY:
  term: "下腳"
  category: "CITY_SCOPED_PAYMENT_EVENT"
  observed:
    - "上海住夜後常見付款事件之一。"
    - "房間人員可能具有其中的分配份額。"
    - "天津不能直接套用上海規則。"
```

硬鎖：

> `下腳` 不是全城市通用價目，也不是賞錢同義詞。

---

## ZF-002｜賞錢

第129回章秋谷想把多付的二十餘元給陸麗娟房間裡的人，陸麗娟反駁：

```text
房間裡的人本已有「下腳拆」
```

章秋谷仍說這是另外「格外賞他們幾個錢」。

因此：

```text
STAFF_ENTITLED_SHARE
!=
DISCRETIONARY_TIP
```

候選：

```yaml
STAFF_PAYMENT:
  entitled_share:
  discretionary_tip:
  source_event:
  payer:
  recipient:
  social_signal:
```

---

# ZG｜帳務文件與證據

目前正文可確認：

```yaml
LEDGER_EVIDENCE_TYPES:
  - "堂簿"
  - "酒局帳／局帳單"
  - "紅紙帳單"
  - "發票"
  - "借據"
  - "收票"
```

## ZG-001｜「發票」不可現代化誤讀

第38、90、164回的 `發票` 是交易／欠款憑據或店舖帳票語境。

因此：

> Corpus 必須保留原詞，但未來遊戲不可把它默認成現代統一發票／稅務發票。

---

## ZG-002｜借據具有債權證據作用

第164回沈二寶高成本借貸：

```text
名義借款 1600
打八扣
預扣三個月利錢
另收借據／中保畫押／帳房回用
最後到手遠低於名義本金
```

並實際：

```text
寫借據
畫押
債權人收存
```

所以未來：

```yaml
DEBT_EVIDENCE:
  verbal_only:
  written_note:
  witness_or_guarantor:
  receipt:
  holder:
```

不可一律等價。

---

# ZH｜高成本借貸與未來收入綁定

第163–164回沈二寶危機提供完整樣本。

## ZH-001｜NOMINAL PRINCIPAL ≠ CASH RECEIVED

```yaml
HIGH_COST_LOAN_SAMPLE:
  chapter: 164
  nominal_principal: 1600
  discount: "八扣"
  prepaid_interest:
    period: "3 months"
    amount: 192
  paperwork_and_guarantor_fees: 80
  cash_received_approx: 1008
```

原文人物自己計算：

> 名義借一千六百，實際生生吃虧六百左右。

因此：

```text
NOMINAL_DEBT
!=
NET_CASH_PROCEEDS
```

---

## ZH-002｜債務可以取得未來收入分成

第163回金姐盤算：

```text
利息
+
扣頭
+
未來「二八提」
```

因此：

```yaml
DEBT_RESTRUCTURING:
  current_debt:
  new_financing:
  interest:
  upfront_discount:
  future_revenue_share:
```

這不是一般 wallet 系統能表示的。

目前 `二八提` 只以此高價值案例收錄，不先推成全行業固定制度。

---

# ZI｜帳務具有委託、抄取與代理流程

第90回章秋谷交錢給陳文仙，要求：

```text
店家來發票後由文仙代為算清
堂子帳則可叫車夫去抄局帳，再送去
```

第100回阿小妹直接把抄好的酒局帳交陳海秋。

因此：

```yaml
ACCOUNT_WORKFLOW:
  account_holder:
  book_keeper:
  authorized_collector:
  messenger:
  payer:
  settlement_receiver:
```

這些角色可能不是同一人。

硬鎖：

> `知道帳目` 也必須有來源；不是所有房間 NPC 都天然知道全部帳。

---

# ZJ｜支付本身可以被當成社會武器

## ZJ-001｜延付／扣帳作為關係施壓

第101回陳海秋承認六百多元酒局帳存在，也明說有錢支付，但故意暫扣，要求范彩霞改變對他的待遇。

因此這是一個可觀察的事件模式：

```yaml
EVENT_PATTERN:
  id: "PAYMENT_WITHHOLDING_AS_SOCIAL_PRESSURE"
  chapter: 101
  conditions:
    - "debt acknowledged"
    - "payer has funds"
    - "payer intentionally delays settlement"
    - "delay is linked to demanded relational / service response"
  effects:
    - "courtesan liquidity pressure"
    - "staff mediation"
    - "relationship conflict"
    - "possible coerced accommodation"
```

**重要鎖：**

> 原作存在此行為，不代表 Runtime 要把「欠帳」合法化為取得親密、住夜或關係資格的權利。

也就是：

```text
PAYMENT LEVERAGE EXISTS AS WORLD BEHAVIOR
!=
PAYMENT CREATES RELATION ENTITLEMENT
```

---

# ZK｜帳務會反向改變聲價、客流與人物決策

## ZK-001｜欠帳 → 名聲

第64回：

```text
客人若節邊不清局帳
→ 房間人員可能傳成「倌人把他做了恩客」
→ 倌人名氣受影響
```

因此：

```text
LEDGER STATE
→ RUMOR
→ PUBLIC RELATION LABEL
```

---

## ZK-002｜傳聞 → 債權人收帳

第10–12回張書玉線：

```text
外面傳她從劉厚卿身上用了很多錢
→ 欠帳店家／借債戶頭認為她有錢
→ 集中收帳
→ 現金流危機
→ 張書玉再向劉厚卿追錢
```

因此形成完整 feedback：

```text
RUMOR
→ CREDITOR EXPECTATION
→ COLLECTION PRESSURE
→ LIQUIDITY
→ CHARACTER ACTION
→ NEW EVENT
```

---

# ZL｜帳目不是關係真相

第94回陶觀察：

```text
實際局帳／菜帳約三百多
但主動交六百
另給四百作新年開銷
```

他的目的之一是希望改善與薛金蓮的關係。

這再次證明：

```text
AMOUNT_PAID > AMOUNT_DUE
!=
RELATION_UPGRADE
```

多付的錢必須拆：

```yaml
PAYMENT_ALLOCATION:
  debt_settlement:
  gift:
  holiday_support:
  tip:
  staff_share:
  other:
```

不能把整筆都算成「消費」。

---

# ZM｜第一版 LEDGER GRAPH

```text
                        ┌─ 客戶叫局／吃酒／碰和／住夜
                        │
                        ▼
                   TRANSACTION EVENT
                        │
                        ▼
                   LEDGER LINE ITEM
                        │
              ┌─────────┴──────────┐
              ▼                    ▼
        客戶對房間欠帳          倌人／房間對外欠帳
        局帳／酒帳              房飯／菜帳／店帳
              │                    │
              │                    ├─ 本家
              │                    ├─ 娘姨帶擋
              │                    ├─ 店家
              │                    └─ 外部借貸
              ▼
        堂簿／酒局帳
              │
       節期抄帳／收帳
              │
       ┌──────┼─────────┐
       ▼      ▼         ▼
     全收    折收      漂帳／拖欠
       │      │         │
       └──────┴────┬────┘
                   ▼
                 現金
                   │
          ┌────────┼─────────┐
          ▼        ▼         ▼
        開銷      還債      房間分配
                  │          ├─ 下腳拆
                  │          └─ 賞錢
                  ▼
            利錢／拆頭／
            未來收入分成
```

旁路：

```text
帳務狀態
↔ 面子
↔ 傳聞
↔ 恩客／瘟生等公開標籤
↔ 客流
↔ 債權人信心
↔ 收帳壓力
```

這使 `LEDGER GRAPH` 成為 `FENGYUE MARKET SYSTEM` 的核心候選，而不是 UI 附件。

---

# ZN｜本輪 raw-hit 索引（INDEX ONLY）

以下只表示正文 exact substring 出現量，不等於純語義頻率：

```yaml
RAW_HIT_INDEX:
  堂簿: {hits: 3, chapters: [12, 162]}
  局帳:
    hits: 59
    chapters: [3,22,23,35,37,38,62,64,68,90,93,94,99,100,101,102,128,129,131,162,164]
  酒帳: {hits: 3, chapters: [90,129,162]}
  房飯: {hits: 14, chapters: [2,29,93,162,163,164,167]}
  菜帳: {hits: 6, chapters: [70,94,163,164]}
  帶擋: {hits: 22, chapters: [10,37,38,64,66,72,77,162]}
  拆頭: {hits: 3, chapters: [37,104]}
  賞錢: {hits: 11, chapters: [14,15,22,51,129,131]}
  店帳: {hits: 12, chapters: [10,11,23,38,90,99,162,163,165]}
```

注意：

- `賞錢` 有大量非堂子場景，必須逐例判讀；
- `房飯` 也包含客棧房飯；
- `堂簿` 用例少，但兩個語境都高度有價值；
- raw hit 不取得正式定義權。

---

# ZO｜目前可鎖的帳務硬結論

```text
ACCOUNT
!= CASH

FACE_AMOUNT
!= ACTUAL_COLLECTION

酒局帳
!= 單一交易

利錢
!= 拆頭

下腳拆
!= 額外賞錢

客戶清帳
!= 關係升級

客戶多付
!= 私人偏愛成立

欠帳
!= 取得人物／身體／住夜之權利

帳務文件
!= 所有人天然知情

死亡／搬場／除牌
!= 舊帳自動消失
```

---

# ZP｜下一輪抽取優先

1. 抽 `PUBLIC / ROOM / PRIVATE` 三層可見度，建立消息傳播與帳務知情 provenance。
2. 建 `REPUTATION → CLIENT FLOW → RECEIVABLE → CASHFLOW` 的完整反饋鏈。
3. 補蘇州書寓的帳務／檯面／碰和／請酒制度，避免 LEDGER 過度上海化。
4. 抽「漂帳／追帳／部分清償／延期／折收」的 debtor behavior family。
5. 把 `LEDGER GRAPH` 與 `HOUSEHOLD_ID + LIFECYCLE` 接起來，處理搬場、除牌、死亡後的未結帳。
---

# AA｜KNOWLEDGE / VISIBILITY GRAPH｜知情、可見度與來源

> 本節依《九尾龜》正文抽取「誰知道什麼、怎麼知道、知道到什麼程度」。  
> 核心不是把資訊固定分成 PUBLIC / ROOM / PRIVATE 三格，而是把**命題、可見範圍、傳遞來源、人物相信程度與世界真值**彼此分離。

## AA-000｜PUBLIC / ROOM / PRIVATE 不是命題永久屬性

同一件事可以經歷：

```text
PRIVATE
→ SELECTIVE DISCLOSURE
→ ROOM / LOCAL KNOWLEDGE
→ RUMOR
→ CITY PUBLIC
→ MEDIA / OFFICIAL ATTENTION
```

也可以停在其中任何一步。

因此：

```text
INFORMATION_CONTENT
!= VISIBILITY_SCOPE

VISIBILITY_SCOPE
!= BELIEF

BELIEF
!= WORLD FACT
```

候選最小結構：

```yaml
KNOWLEDGE_ITEM_CANDIDATE:
  proposition_id:
  content:
  world_truth_status:
    - "TRUE"
    - "FALSE"
    - "UNKNOWN"
    - "DISPUTED"

  current_holder:
  acquisition:
    channel:
      - "DIRECT_OBSERVATION"
      - "DIRECT_SPEECH"
      - "RELAY"
      - "DOCUMENT"
      - "ACTIVE_INQUIRY"
      - "RUMOR"
      - "MEDIA"
      - "SURVEILLANCE"
    source_actor:
    source_document:
    source_event:
    transmission_chain: []

  visibility_scope:
    - "PRIVATE"
    - "ROOM_LOCAL"
    - "SELECTED_GROUP"
    - "PUBLIC"

  belief_state:
    - "BELIEVES"
    - "SUSPECTS"
    - "DOUBTS"
    - "REJECTS"
    - "UNRESOLVED"

  secrecy:
    concealment_intent:
    disclosure_permission:
    leak_source_known:

  verification:
    status:
    method:
    evidence:
```

此處仍是 `CORPUS_DERIVED_SCHEMA_CANDIDATE`，不是正式 Runtime。

---

## AA-001｜私人知情可以被明確保密

### 第33回｜章秋谷 ↔ 陸畹香

章秋谷已知道陸畹香的一件私事，並明示：

```text
「我雖然曉得，決不向人傳說，壞你的名頭。」
```

同一段又說：

```text
若被外頭傳說出來
→ 生意受妨礙
→ 名頭受損
```

因此：

```yaml
CONFIDENTIAL_KNOWLEDGE:
  holder: "章秋谷"
  subject: "陸畹香"
  visibility: "PRIVATE"
  concealment_intent: "EXPLICIT"
  public_leak_risk:
    - "business_damage"
    - "reputation_damage"
```

硬鎖：

> **知道秘密，不等於秘密已進入傳聞網。**

---

## AA-002｜房間裡可以再切出「更私密」的局部空間

第64回陳文仙與章秋谷：

```text
附耳私語
→ 再說一回
→ 文仙支開房裡娘姨
→ 才取出首飾匣處理下一步
```

第187回辛修甫與蘇青青則更明確：

```text
兩人低聲／咬耳談事
→ 房間裡娘姨、大姐看出情勢
→ 主動退開
→ 談話結束後仍不知道內容
```

所以：

```text
SAME_ROOM
!= SAME_INFORMATION_ACCESS
```

候選：

```yaml
SCENE_INFORMATION_ACCESS:
  physically_present:
  within_hearing:
  intentionally_excluded:
  intentionally_withdrawn:
  observed_action:
  heard_content:
  inferred_content:
```

**重要：**

> `ROOM_LOCAL` 不是一個共享記憶池。

---

## AA-003｜保密也可以靠物理出入控制

### 第125回｜內簽押房

康中丞收到涉及自己起復的私人書信後：

```text
怕家人闖入看見
→ 怕消息傳出去
→ 關門
→ 限制家人進入
```

因此：

```text
PRIVACY
can be produced by:
  - speech control
  - audience exclusion
  - room access control
  - document visibility control
```

這與 V0.3 已抽出的 `ROOM_ACCESS_CONTROL` 可以接合，但仍保持：

```text
PHYSICAL ACCESS
!= INFORMATION ACCESS
```

---

# AB｜TRANSMISSION EVENT｜消息傳遞本身是一個世界事件

## AB-001｜相幫可作二手消息來源，但不是天然真相節點

### 第47回｜陸蘭芬死亡消息

貢春樹對章秋谷說：

```text
「我今天早上聽小寶家的相幫傳說，方才知道」
```

同時又說：

```text
還聽相幫們自己議論蘭芬虧空
```

這裡至少有兩筆不同資訊：

```yaml
MESSAGE_A:
  content: "陸蘭芬已死"
  source: "小寶家的相幫"
  recipient: "貢春樹"
  recipient_confidence: "HIGH"

MESSAGE_B:
  content: "陸蘭芬虧空約兩萬多"
  source: "相幫們議論"
  recipient: "貢春樹"
  confidence: "LOWER / HEARSAY"
```

章秋谷收到後仍進一步到現場查看。

因此：

> **同一傳話者可以帶來不同證據強度的內容。**

`SOURCE_ACTOR` 不能自動決定 `TRUTH_STATUS`。

---

## AB-002｜「聽來的」可以被人物主動驗證

### 第50回｜郭觀察

事件鏈非常完整：

```text
親戚告知貝府新聞
→ 郭觀察不信
→ 親戚說「蘇州城內到處皆知」
→ 郭觀察自行細細打聽
→ 得到「眾口相同」
→ 仍認為「眼見是實，耳聞是虛」
→ 親自到戲館連看數日
→ 才形成自己的判斷
```

這直接支持：

```yaml
BELIEF_UPDATE_CHAIN:
  received_claim:
  initial_belief: "REJECT / DOUBT"
  social_corrobation:
  active_inquiry:
  direct_observation:
  final_belief:
```

硬鎖：

> **多人都說同一件事，不等於人物必須相信。**

人物可以要求更高的證據門檻。

---

# AC｜RUMOR GRAPH｜傳聞不是低可信度版 FACT

## AC-001｜錯誤或未證實傳聞也能產生真實後果

既有第64回：

```text
不清局帳
→ 房間人員可能傳成「做了恩客」
→ 名聲受影響
```

現在可以把這條正式升成：

```yaml
RUMOR_EFFECT:
  proposition_truth_required_for_effect: false
  world_effect_may_include:
    - "reputation"
    - "business"
    - "creditor_behavior"
    - "relationship_pressure"
```

所以：

> `RUMOR != FACT`，但 `RUMOR_EFFECT` 可以是真實世界事件。

---

## AC-002｜來源未知的錯誤消息仍然會驅動人物

### 第176回｜賽金花案承審消息

先有消息傳出：

```text
壽尚書要把賽金花案發交雲南司
```

司員收到後：

```text
→ 前往賀喜
→ 宴飲
```

但壽尚書之後明確說：

```text
「我並沒有把這賽金花一案發交雲南司的意思」
```

並追問：

```text
「這個消息是那一個傳出去的？」
```

最後：

```text
查不出來源
```

因此正式建立：

```yaml
EVENT_PATTERN:
  id: "UNKNOWN_SOURCE_FALSE_LEAK"

  proposition:
    truth_status: "FALSE / DENIED_BY_AUTHORITY"

  leak:
    source: "UNKNOWN"

  propagation:
    recipients: "刑部司員群體"

  effects:
    - "behavior_change"
    - "public/social action"
    - "institutional reprimand"

  provenance_status:
    - "LEAK_SOURCE_UNRESOLVED"
```

這證明：

> **UNKNOWN SOURCE 是合法世界狀態。**
>
> 不得為了讓故事完整，就自動補一個洩密者。

---

## AC-003｜傳聞可以被人故意製造

### 第190回｜針對章秋谷的會匪謠言

事件鏈：

```text
祁侍郎與門下人密議
→ 明知要「只說他是會匪頭目」
→ 設計讓風聲傳出去
→ 常熟出現謠言
→ 劣紳附和
→ 一傳十、十傳百
→ 除少數親友外，多數人逐步相信
→ 消息傳到商約大臣
→ 高位人物召章秋谷問話
```

這不是自然誤傳，而是：

```yaml
EVENT_PATTERN:
  id: "ENGINEERED_RUMOR_CAMPAIGN"

  origin:
    intentional: true
    motive: "RETALIATION"

  initial_claim:
    truth_status: "FABRICATED / HOSTILE CLAIM"

  amplification:
    - "allied_repeaters"
    - "social repetition"
    - "local elites"

  spread:
    mechanism: "一傳十、十傳百"

  belief_distribution:
    believers: "MAJORITY_GROWS_OVER_TIME"
    rejecters:
      - "部分親戚"
      - "部分朋友"

  institutional_reach:
    - "傳至商約大臣"

  effect:
    - "reputation pressure"
    - "social withdrawal"
    - "official inquiry"
```

**高價值結論：**

> 傳聞網必須允許「惡意注入」；不能假設所有 rumor 都由模糊誤會自然產生。

---

# AD｜BELIEF ≠ INFORMATION RECEIPT

第50回與第190回共同證明：

```text
RECEIVED(message)
does not imply
BELIEVES(message)
```

而且同一則消息在不同人物身上可同時是：

```yaml
BELIEF_DISTRIBUTION:
  person_A: "BELIEVES"
  person_B: "SUSPECTS"
  person_C: "REJECTS"
  person_D: "UNRESOLVED"
```

因此未來不能把：

```text
rumor_seen = true
```

直接當作：

```text
character_believes = true
```

---

# AE｜PUBLIC KNOWLEDGE 也有不同形成方式

目前 Corpus 至少已確認三種：

## AE-001｜口耳型公開

第50回：

```text
茶坊酒肆
→ 三三兩兩談論
→ 蘇州城內廣泛流傳
```

這是：

```yaml
PUBLIC_CHANNEL:
  type: "ORAL_SOCIAL_NETWORK"
```

---

## AE-002｜房間／相幫擴散型

第47、64回：

```text
房間人員／相幫
→ 轉述／議論
→ 熟客／朋友
→ 外部名聲
```

這是：

```yaml
PUBLIC_CHANNEL:
  type: "HOUSEHOLD_TO_SOCIAL_NETWORK"
```

---

## AE-003｜媒體放大型

第91、183回花榜：

```text
報館主筆／花榜
→ 公開刊載
→ 上海多人閱讀
→ 聲價與叫局增加
```

而第19回甚至有人以「托各報館上報」作為公開惡跡的威脅。

因此：

```yaml
PUBLIC_CHANNEL:
  type: "PRINT_MEDIA"
  reach: "HIGH"
  credibility: "NOT_AUTOMATIC"
  manipulable: true
```

硬鎖：

> **公開 ≠ 真實。**
>
> 報紙只是更高擴散力的來源之一，不取得世界事實權。

---

# AF｜REPUTATION 是資訊網與市場網的接口

目前已可形成：

```text
PRIVATE / LOCAL EVENT
↓
被看見／被轉述／被誤解
↓
RUMOR / PUBLIC CLAIM
↓
不同人物形成不同 BELIEF
↓
REPUTATION STATE
↓
CLIENT FLOW / CREDITOR BEHAVIOR / SOCIAL ACCESS
↓
MONEY / RELATION / CONFLICT
↓
新事件
```

因此：

```text
REPUTATION
!= CHARACTER TRAIT

REPUTATION
= information-mediated social state
```

它需要：

```yaml
REPUTATION_CANDIDATE:
  subject:
  proposition_cluster:
  source_channels:
  reach:
  believer_groups:
  doubter_groups:
  refuters:
  media_support:
  direct_evidence:
  business_effect:
  decay_or_persistence:
```

仍為 Corpus 候選，不升正式 Runtime。

---

# AG｜KNOWLEDGE EDGE｜比「人物知情表」更精確的最小單位

目前最適合的 Corpus 形狀不是：

```yaml
character:
  knows:
    - "X"
```

而是：

```yaml
KNOWLEDGE_EDGE:
  receiver:
  proposition:
  acquisition_event:
  source:
  source_type:
  transmission_chain:
  observed_or_heard_at:
  visibility_at_acquisition:
  belief_state:
  confidence:
  verification_state:
  may_relay:
  secrecy_obligation:
```

原因是：

- 第33回：知道但承諾不傳；
- 第47回：由相幫傳入；
- 第50回：聽到後先不信，再查證；
- 第64回：房間人員若得知可能再向外傳；
- 第176回：消息來源根本查不出；
- 第190回：消息源明知是假，接收者卻可能相信。

所以：

> **「誰知道」永遠必須連著「他憑什麼知道」。**

這條已不只是觀止母架構的繼承原則，而是《九尾龜》Corpus 自己提供了大量獨立證據。

---

# AH｜消息傳播第一版事件族

```yaml
INFORMATION_EVENT_FAMILY:

  PRIVATE_DISCLOSURE:
    "A 對 B 私下說明"

  CONFIDENTIAL_HOLD:
    "B 知道，但明示／默示不外傳"

  SELECTIVE_AUDIENCE:
    "主動支開第三人後再說／做"

  DIRECT_OBSERVATION:
    "人物親眼看見事件"

  LOCAL_RELAY:
    "相幫／娘姨／大姐／朋友轉述"

  ACTIVE_INQUIRY:
    "人物主動打聽、察訪、查問"

  RUMOR_SPREAD:
    "未經正式確認的消息沿社交網擴散"

  UNKNOWN_SOURCE_LEAK:
    "消息已流出，但源頭無法確認"

  ENGINEERED_RUMOR:
    "人物故意製造並推動虛假／敵意消息"

  MEDIA_AMPLIFICATION:
    "報館／榜單將消息擴大為公開注意"

  BELIEF_REVISION:
    "人物因新來源／新觀察改變相信程度"
```

---

# AI｜本輪形成的新硬結論候選

```text
PUBLIC
!= TRUE

PRIVATE
!= SAFE_FOREVER

SAME_ROOM
!= SAME_KNOWLEDGE

HEARD
!= BELIEVED

MULTIPLE_SOURCES
!= FACT

SOURCE_UNKNOWN
is a legal state

RUMOR
may be deliberately manufactured

MEDIA_PUBLICATION
!= WORLD_FACT

KNOWLEDGE
requires provenance

REPUTATION
is an information-mediated world state
```

---

# AJ｜raw-hit 索引（INDEX ONLY）

以下只表示正文 exact substring 出現量：

```yaml
RAW_HIT_INDEX:
  傳說: 22
  傳聞: 0
  聽說: 24
  消息: 27
  新聞: 19
  打聽: 58
  風聲: 40
  謠言: 12
  報館: 11
  附耳: 34
  密密: 28
  瞞: 107
```

注意：

- `傳聞` 雖是現代好用的 normalize label，但正文 exact substring 本輪未找到；
- 正文更常出現 `傳說／風聲／消息／新聞／謠言`；
- 因此遊戲內部可使用 `RUMOR` 作 normalized category，但不得冒充原作固定詞「傳聞」。

---

# AK｜下一輪抽取優先

1. 建 `REPUTATION → CLIENT FLOW → RECEIVABLE → CASHFLOW` 的完整回饋鏈。
2. 抽 `聲價／名氣／面子／風頭／花榜／生意` 的相互作用，避免全部壓成 Reputation Score。
3. 補蘇州書寓／堂子制度，尤其 PUBLIC 場域如何形成新聞與社會評價。
4. 建 `DEBTOR BEHAVIOR FAMILY`：漂帳、躲帳、部分清償、折收、延期、拒付。
5. 將 `KNOWLEDGE_EDGE` 與 `HOUSEHOLD_ID / ROLE_ASSIGNMENT / VENUE` 接起來，形成真正可追蹤的城市資訊網。
---

# AL｜REPUTATION / DEMAND GRAPH｜聲價、名氣、面子、風頭與客流

> 本節把前一版 `KNOWLEDGE / RUMOR GRAPH` 與 V0.5 `LEDGER GRAPH` 接起來。  
> 核心問題不是「名氣值多少」，而是：**哪一種社會評價，透過哪一種渠道，影響哪些客人來不來、怎麼來、花什麼錢，最後又有多少真正變成可收現金。**

## AL-000｜REPUTATION 不能壓成單一數值

目前正文至少反覆使用：

```yaml
REPUTATION_RELATED_FORMS:
  聲價:
    observed_scope:
      - "倌人的市場地位／名妓品評"
      - "其他社會人物的社會評價"
    caution:
      - "不能只用於風月市場"

  名氣:
    observed_scope:
      - "倌人"
      - "客人"
      - "一般社會人物"
    function:
      - "被人知道／談論"
      - "可能影響被如何看待與招待"

  名聲:
    observed_scope:
      - "正面或負面社會評價"
      - "可因醜聞／事件而受損"

  風頭:
    observed_scope:
      - "當時場面上的熱門程度／顯眼程度"
      - "不保證長期持久"

  面子:
    observed_scope:
      - "場面上的可見社會位置"
      - "可被維持、逼迫、損害、利用"
      - "同時存在客人與倌人兩端"

  花榜:
    observed_scope:
      - "公開排名／媒體訊號"
      - "可有評鑑功能，也可被操縱"

  生意:
    observed_scope:
      - "實際市場活動量"
      - "不能直接等於聲價或名氣"
```

所以：

```text
聲價
!= 名氣
!= 名聲
!= 風頭
!= 面子
!= 花榜名次
!= 生意量
```

它們會互相影響，但不是同一欄位。

---

# AM｜QUALIFICATION / SERVICE / FAME / BUSINESS 分軸

## AM-001｜第16回的「資格→聲價」「應酬→生意」是兩條不同路

第16回章秋谷的議論明確分成：

```text
資格熬得久
→ 聲價高

應酬圓到隨和
→ 生意好
```

這是**人物觀點／評論性解說**，不能單獨升成世界公理。

但同段金小寶以自己的經歷回應：

```text
剛出來時不懂應酬
→ 生意少

過了幾年
→ 生意慢慢變好
→ 名氣也慢慢出來

本人並沒有「換一張面孔」
```

因此至少可安全抽出：

```yaml
MARKET_OBSERVATION:
  skill_or_service_change:
    may_affect: "BUSINESS_FLOW"

  elapsed_market_presence:
    may_affect:
      - "RECOGNITION"
      - "PUBLIC_FAME"

  physical_appearance_constant:
    does_not_prevent:
      - "business change"
      - "fame change"
```

硬鎖：

> **外貌沒有變，不代表市場狀態不會變。**

---

## AM-002｜名聲／聲價會形成客人的先驗判斷

第16回又有一個反向鏈：

```text
客人看到某倌人聲價高
→ 先推定她是「名妓／才貌雙全」
→ 願意花大筆銀子巴結
```

而沒有名氣者：

```text
即使實際才貌較好
→ 可能根本得不到同樣注意
```

因此：

```yaml
CLIENT_ATTENTION_PRIOR:
  inputs:
    - public_fame
    - market_prestige
    - published_rank
    - peer_talk

  may_affect:
    - initial_interest
    - willingness_to_call
    - willingness_to_spend
```

但：

```text
PUBLIC_FAME
!= ACTUAL_QUALITY
```

---

# AN｜PUBLIC CONSENSUS / SELF-REINFORCEMENT

## AN-001｜第15回：聲價可由「眾口」形成，也可自抬

第15回直接描述：

```text
上海倌人聲價／名妓平章
→ 「出於眾口」
```

並同時指出：

```text
有些人「自抬聲價」
→ 偶然紅起來
→ 又有人把她當成名妓
→ 進一步巴結
```

因此市場至少允許：

```yaml
REPUTATION_FORMATION:
  - "PEER_CONSENSUS"
  - "SELF_PROMOTION"
  - "SOCIAL_MOMENTUM"
  - "MEDIA_SIGNAL"
```

這形成候選正回饋：

```text
被說成紅
→ 更多人注意
→ 更多人實際接觸
→ 更多人再談
→ 更紅
```

硬鎖：

> **紅起來可以是市場結果，不必先有可量化的「真實品質提升」。**

---

# AO｜FLOW CASE 001｜薛金蓮：付費花榜 → 客流 → 二次口碑

第91回提供目前最完整的 `REPUTATION → CLIENT FLOW` 樣本。

## AO-001｜背景：原客群不能支持新的市場位置

薛金蓮由原來的野雞生涯累積一些資金後，進入長三式營業空間。

但：

```text
原有老客
→ 仍來吃酒
→ 場面可熱鬧

可是：
老客經濟能力有限
→ 無法頻繁支撐花酒消費

結果：
新位置的生意清淡
→ 面子上過不去
```

因此：

> **「有人來」與「有足以支撐市場位置的有效客群」不是同一件事。**

候選：

```yaml
CLIENT_FLOW:
  visitor_count:
  paying_capacity:
  repeat_frequency:
  transaction_mix:
  social_class_or_market_fit:
```

---

## AO-002｜購買排名

事件鏈：

```text
生意清淡
→ 找小報主筆
→ 私下給錢
→ 花榜一甲第一名
→ 報紙公開
```

這是：

```yaml
EVENT_PATTERN:
  id: "PAID_REPUTATION_SIGNAL"
  chapter: 91
  payer: "薛金蓮"
  intermediary: "小報主筆"
  output: "花榜狀元"
  truth_authority: "NONE"
  attention_power: "HIGH"
```

---

## AO-003｜公開排名直接製造新客流

發榜後：

```text
上海人看到排名
→ 原本不認識薛金蓮
→ 「你也去叫，他也去叫」
```

這是目前最直接的：

```text
PUBLIC SIGNAL
→ CALL FLOW
```

證據。

---

## AO-004｜第一批客人的體驗又反過來合理化排名

更重要的是後續：

```text
客人來叫
→ 親自接觸
→ 不把不會應酬解讀成缺點
→ 改說成「大家丰範」

不把不能唱曲解讀成缺點
→ 改說成「閨閣嬌羞」

→ 再一傳十、十傳百
→ 社會評價繼續抬升
```

這形成：

```text
PAID MEDIA SIGNAL
→ ATTENTION
→ CLIENT ARRIVAL
→ POST-HOC POSITIVE INTERPRETATION
→ WORD OF MOUTH
→ MORE REPUTATION
```

**重要：**

> 初始訊號即使被操縱，後續也可能產生真正的市場行為與新的相信者。

---

# AP｜FLOW CASE 002｜花榜成為「投資」

第183回敘事直接說明後期花榜腐敗：

```text
倌人付錢買名次
→ 名字登榜
→ 預期名氣更響
→ 預期生意更大
→ 認為前期花出去的錢可以收回
```

因此：

```yaml
REPUTATION_INVESTMENT:
  upfront_cost:
  signal:
  expected_attention_gain:
  expected_business_gain:
  expected_payback:
```

這意味著：

> Reputation 在原作世界裡可以被當作一種**預期具有現金回收能力的投資標的**。

但不能直接把 `expected_payback` 寫成保證。

---

## AP-001｜媒體訊號本身也有 CREDIBILITY 生命周期

第183回同時指出：

```text
早期花榜
→ 雖有偏私，仍有一定評鑑標準
→ 榜首本身仍有聲價

後期花榜
→ 主筆收賄
→ 名次有價碼
→ 頻繁濫開
→ 評鑑標準崩壞
```

因此：

```yaml
MEDIA_SIGNAL_STATE:
  outlet_id:
  ranking_series:
  selection_criteria:
  corruption_level:
  market_credibility:
  audience_reach:
  demand_effect:
```

硬鎖：

```text
MEDIA_REACH
!= MEDIA_CREDIBILITY
```

一個媒體可以仍然很有擴散力，但它的評鑑可信度已下降。

---

# AQ｜FLOW CASE 003｜城市轉換會改寫市場結果

## AQ-001｜陸畹香：上海不振 → 天津大紅 → 再衰

第30回提供重要跨城市樣本：

```text
上海：
生意不好

→ 移動到天津

天津初期：
名聲大震
→ 各堂子老闆以重金招致
→ 天天冠蓋如雲
→ 市場極熱鬧

後期：
花運退／環境變動
→ 生意一節不如一節

→ 再回上海
```

因此：

```text
CHARACTER_QUALITY_CONSTANT
does not imply
MARKET_RESULT_CONSTANT
```

候選：

```yaml
MARKET_CONTEXT:
  city:
  venue_class:
  local_taste:
  local_network:
  market_phase:
  competition:
  political_or_disaster_shock:
```

硬鎖：

> **名氣與生意具有 CITY / TIME SCOPE。**

不能寫：

```text
character.reputation = 88
```

然後在上海、天津、蘇州全部同值生效。

---

# AR｜FLOW CASE 004｜負面資訊也會抽乾客流

## AR-001｜金小寶：私人關係信號 → 熟客撤退

第104回：

```text
小寶原本生意很好
→ 因牛幼康而冷淡其他客人
→ 客人知道後向外傳
→ 一傳十、十傳百
→ 熟客慢慢裹足不前
→ 房間幾乎無客
→ 娘姨拆頭收入消失
→ 房間內部衝突爆發
```

因此：

```text
RELATION / BEHAVIOR INFORMATION
→ CLIENT EXPECTATION
→ CLIENT WITHDRAWAL
→ BUSINESS FLOW
→ STAFF INCOME
→ HOUSEHOLD CONFLICT
```

這不一定是「名聲變壞」四個字能概括。

它可能是：

```yaml
CLIENT_DECISION_SIGNAL:
  perceived_availability:
  perceived_service_quality:
  perceived_priority:
  perceived_relation_obstacle:
```

---

## AR-002｜沈二寶：社會消息 → 絕腳 → 債務危機

第162回：

```text
原本生意發達
→ 客人知道她愛姘戲子
→ 一個個絕腳不去
→ 生意下跌
→ 消費習慣未同步下降
→ 欠債累積
→ 堂簿應收不足覆蓋到期負債
→ 年底現金流危機
```

這直接閉合：

```text
SOCIAL INFORMATION
→ CLIENT ATTRITION
→ TRANSACTION FLOW DOWN
→ RECEIVABLE STOCK DOWN
→ LIQUIDITY GAP
→ DEBT CRISIS
```

這是目前 `REPUTATION / INFORMATION → LEDGER` 最強負向案例。

---

# AS｜MACRO MARKET REGIME｜個人名氣不能覆蓋整體市況

第183回在談上海後期時明示：

```text
市面一年年衰敗
→ 堂子生意一天寥落似一天
```

而且這一段同時仍提到不少「有名人物」。

所以：

```text
INDIVIDUAL_REPUTATION
does not cancel
MARKET_DOWNTURN
```

候選：

```yaml
MARKET_REGIME:
  city:
  period:
  aggregate_demand:
  disposable_spending:
  venue_activity:
  media_activity:
  shock_events:
```

因此未來 `FENGYUE MARKET SYSTEM` 至少要有：

```text
個人市場位置
+
房間狀態
+
城市市場狀態
+
時間狀態
```

四者共同決定客流。

---

# AT｜CLIENT REPUTATION GRAPH｜客人也有市場名聲

《九尾龜》的 reputation graph 不是只有倌人。

## AT-001｜客人「有名富戶」會改變倌人的預期

第9回陸蘭芬線：

```text
方幼惲初到上海
+
本人沒有嫖界名氣
+
但有「有名富戶」身份
→ 被判斷為可能有高支付能力
→ 倌人可能改變對他的策略
```

所以：

```text
FENGYUE_SKILL_REPUTATION
!= WEALTH_REPUTATION
```

---

## AT-002｜「面子上的錢」可以建立闊客形象

第42、44回章秋谷的議論與自我回顧：

```text
公開場面上的花費
→ 容易被旁人看見
→ 可形成豪華／闊客形象與名氣

私下被敲大量竹槓
→ 即使支出很大
→ 不一定產生同樣社會收益
→ 反而可能被視為「瘟生」
```

這仍首先是章秋谷的**人物市場哲學**，不升世界公理。

但它提供非常重要的分類：

```yaml
CLIENT_SPENDING_VISIBILITY:
  PUBLIC_FACE_SPEND:
    social_visibility: "HIGH"

  PRIVATE_EXTRACTION_SPEND:
    social_visibility: "LOW / VARIABLE"

  actual_money_outflow:
    not_equal: "social_return"
```

---

## AT-003｜客人自稱「有名氣」不取得任何資格

第36回金漢良：

```text
自稱在堂子裡頗有名氣
→ 因金小寶叫局來得早
→ 自稱被當作恩客
```

金小寶當場否認：

```text
來得早
!= 恩客
```

因此：

```text
CLAIMED_CLIENT_REPUTATION
!= ACTUAL_RELATION_QUALIFICATION
```

而且：

```text
SERVICE_ORDER
!= ENKE_STATUS
```

這是 `REPUTATION / RELATION` 分軸的重要 regression case。

---

## AT-004｜客人的面子敏感可以成為別人的經濟情報

第35回方子衡：

```text
方子衡愛裝場面
→ 熟人知道其弱點
→ 判斷可用「擠在面子上」迫使其揮霍
```

因此：

```yaml
CLIENT_MARKET_PROFILE:
  wealth_reputation:
  spending_capacity:
  spending_visibility_preference:
  face_sensitivity:
  bargaining_skill:
  fengyue_experience:
  sucker_label_or_risk:
```

但：

> 這是人物對人物的策略知識，不代表系統替任何 NPC 自動開啟讀心術。

---

# AU｜REPUTATION → CLIENT FLOW → LEDGER 第一版閉環

```text
                         ┌─────────────────────┐
                         │ ACTUAL EXPERIENCE   │
                         │ 應酬／色藝／事件    │
                         └─────────┬───────────┘
                                   │
                                   ▼
┌───────────────┐          PUBLIC / SOCIAL CLAIM
│ MEDIA SIGNAL  │─────────► 名氣／聲價／風頭
│ 花榜／報館     │          / 某種負面消息
└───────┬───────┘                   │
        │                           ▼
        │                    CLIENT ATTENTION
        │                           │
        │                  ┌────────┴────────┐
        │                  ▼                 ▼
        │               新客流             熟客撤退
        │                  │                 │
        │                  ▼                 ▼
        │          叫局／吃酒／碰和       TRANSACTION ↓
        │                  │
        │                  ▼
        │             LEDGER LINE ITEM
        │                  │
        │                  ▼
        │              FACE RECEIVABLE
        │                  │
        │            節期／日常收帳
        │                  │
        │        ┌─────────┼─────────┐
        │        ▼         ▼         ▼
        │       全收       折收       漂帳
        │        │         │         │
        │        └─────────┴────┬────┘
        │                       ▼
        │                    CASHFLOW
        │                       │
        │             ┌─────────┼──────────┐
        │             ▼         ▼          ▼
        │           本家       房間人員      店帳／債務
        │
        └── 可由付費購買／操縱
```

同時還有第二條反饋：

```text
CLIENT ARRIVAL
→ 實際體驗
→ 再解讀／再傳播
→ Reputation 更新
```

以及：

```text
CASHFLOW
→ 有能力買花榜／撐場面／維持房間
→ 新的公開訊號
```

這就是目前 Corpus 已能支持的第一版：

> **FENGYUE REPUTATION–DEMAND–LEDGER FEEDBACK LOOP**

---

# AV｜不能簡化成「名氣越高，收入越高」

目前至少有五個反例：

```yaml
ANTI_LINEAR_CASES:

  1:
    case: "陸蘭芬"
    observation:
      - "有名氣、生意鬧忙"
      - "仍承擔高場面壓力與退出困難"
    rule:
      - "high_reputation != good_life_outcome"

  2:
    case: "薛金蓮花榜"
    observation:
      - "排名可被付費操縱"
      - "操縱後仍能產生真實客流"
    rule:
      - "reputation_signal != underlying_quality"

  3:
    case: "陸畹香"
    observation:
      - "同一人物在上海／天津市場結果完全不同"
    rule:
      - "reputation_effect is context scoped"

  4:
    case: "沈二寶"
    observation:
      - "曾經生意發達"
      - "負面社會消息後迅速失去客流"
    rule:
      - "past_success != persistent_demand"

  5:
    case: "上海後期"
    observation:
      - "宏觀市面衰敗時，有名人物也處在整體需求下行"
    rule:
      - "individual_fame != immunity_to_market_regime"
```

---

# AW｜目前候選資料結構

```yaml
FENGYUE_MARKET_POSITION:
  entity_id:
  city_scope:
  venue_scope:
  time_scope:

  public_fame:
  market_prestige:
  current_momentum:
  published_rankings: []

  qualification_history:
  service_reputation:
  art_reputation:
  conduct_reputation:

  client_flow:
    new_clients:
    regular_clients:
    lost_clients:
    call_frequency:
    table_frequency:
    tea_visit_frequency:

  client_mix:
    spending_capacity:
    repeat_capacity:
    social_visibility:

  business:
    transaction_volume:
    receivable_generation:
    actual_cash_realization:

  information_sources:
    rumor_edges: []
    media_edges: []
    direct_experience_edges: []

  macro_context:
    market_regime_id:
```

**仍為 Corpus-derived candidate，不是正式 Runtime。**

---

# AX｜raw-hit 索引（INDEX ONLY）

```yaml
RAW_HIT_INDEX:
  聲價:
    hits: 11
    chapters: [9,15,16,169,183]

  名氣:
    hits: 49
    chapter_count: 38

  名聲:
    hits: 16
    chapters: [21,25,28,29,30,47,49,52,55,56,63,64,76,83]

  面子:
    hits: 64
    chapter_count: 43

  風頭:
    hits: 21
    chapters: [1,2,9,15,16,17,22,25,27,32,71,80,84,91,115]

  花榜:
    hits: 37
    chapters: [29,91,155,156,183]

  紅倌人:
    hits: 34
    chapter_count: 23

  生意:
    hits: 261
    chapter_count: 98

  叫局:
    hits: 42
    chapter_count: 26

  打茶圍:
    hits: 15
    chapters: [14,30,43,60,100,106,113,136,137,142,145,161,162]

  熟客:
    hits: 17
    chapters: [2,7,9,33,34,35,36,38,63,75,104,121,144,159,165,173,174]

  瘟生:
    hits: 78
    chapter_count: 38
```

注意：

- raw hit 不等於語義頻率；
- `生意` 大量包含非風月市場用法，必須逐場域判讀；
- `面子／名氣／名聲` 也大量出現在官場、家庭與一般社會事件；
- 第169回 `聲價` 即明顯不是倌人市場，因此不能全數塞入 FENGYUE reputation。

---

# AY｜本輪形成的新硬結論候選

```text
REPUTATION
!= DEMAND

DEMAND
!= TRANSACTION

TRANSACTION
!= RECEIVABLE

RECEIVABLE
!= CASH

PUBLIC RANK
!= QUALITY

PUBLIC RANK
may still create REAL CLIENT FLOW

FAME
is city/time scoped

CLIENT MIX
matters as much as client count

MACRO MARKET
can dominate individual fame

NEGATIVE INFORMATION
may reduce client flow without changing intrinsic ability

CLIENT REPUTATION
!= RELATION QUALIFICATION

VISIBLE SPENDING
!= TOTAL SPENDING

PAID PROMOTION
may create self-reinforcing market effects
```

---

# AZ｜下一輪抽取優先

1. 建 `DEBTOR BEHAVIOR FAMILY`：漂帳、躲帳、部分清償、折收、延期、拒付、故意扣帳。
2. 抽蘇州書寓／堂子／酒席的場域制度，補現在過度以上海為中心的市場網。
3. 把 `CLIENT FLOW` 細分為打茶圍、叫局、吃酒、碰和、住夜等不同流量，不用一個 visits。
4. 抽 `RED_COURTESAN / 紅倌人` 的形成、維持與衰退事件，確認它與花榜／聲價／生意的關係。
5. 開始做 Stage 1 的 cross-check：找反例攻擊 V0.1–V0.7 已形成的候選規則。
---

# BA｜DEBTOR BEHAVIOR FAMILY｜債務人行為族

> 本節把 V0.5 的 `LEDGER GRAPH` 從靜態帳目推進成行為系統。  
> 核心不是 `paid = true/false`，而是：**債務人如何面對到期帳、債權人是否同意、最後實收多少、收帳成本如何變化，以及這段歷史如何反過來改變下一次信用。**

## BA-000｜「未付款」不是單一狀態

目前正文至少可分出：

```yaml
DEBTOR_BEHAVIOR_FAMILY:

  FULL_SETTLEMENT:
    "照數清償"

  NEGOTIATED_DEFERRAL:
    "先向債權人說明，取得延期同意"

  UNILATERAL_DEFERRAL:
    "債務人自行主張以後再付，債權人未明確同意"

  STRATEGIC_WITHHOLDING:
    "有支付能力，但故意扣住款項，以取得其他條件"

  DEFAULT_OR_FLOATING_ACCOUNT:
    "帳已到應收時點而未實現，並可能伴隨失聯／躲避／難以追索"

  PARTIAL_SETTLEMENT:
    "先付一部分，剩餘另議"

  NEGOTIATED_HAIRCUT:
    "債權人接受低於帳面值的結清"

  COLLECTION_DISCOUNT_REALIZATION:
    "市場上實際收帳通常低於帳面值；以回收率表示"

  PAYMENT_PRIORITY:
    "資金不足時，債務人先清最不能拖的債權"

  CREDITOR_REFUSES_EXTENSION:
    "債務人提出延期／部分清償，但債權人不接受"
```

硬鎖：

```text
UNPAID
!= DEFAULT

DEFAULT
!= NEGOTIATED DEFERRAL

DELAY
!= HAIRCUT

PARTIAL PAYMENT
!= FINAL SETTLEMENT

ABILITY TO PAY
!= WILLINGNESS TO PAY

CREDITOR CONSENT
must be represented separately
```

---

# BB｜漂帳

## BB-001｜「漂帳」是正文可確認的風月信用風險詞

正文 exact substring：

```yaml
RAW_HIT:
  漂帳:
    hits: 8
    chapters: [99, 129]

  related_form:
    "漂了兩筆局帳":
      chapter: 23
```

第23回林黛玉線：

```text
生意雖好
→ 開銷仍大
→ 又被客人漂掉兩筆局帳
→ 店帳周轉不來
→ 名頭面臨受損
→ 生意難以維持
```

因此：

```yaml
DEFAULT_EFFECT:
  receivable_realization: "FAIL / DELAYED"
  liquidity_effect: "NEGATIVE"
  creditor_to_third_party_payment: "PRESSURED"
  reputation_effect: "POSSIBLE"
  business_continuity_effect: "POSSIBLE"
```

這證明：

> **漂帳不是只讓一筆收入少掉；它能穿透到店帳、名頭與營業存續。**

---

## BB-002｜節期時，漂帳客人會主動躲避收帳網

第99回端午前：

```text
娘姨／大姐沿四馬路收帳
→ 漂帳客人躲得無影無蹤
→ 收帳人員花大量時間尋找
```

所以應建立：

```yaml
COLLECTION_AVOIDANCE:
  debtor_reachable:
  known_location:
  actively_hiding:
  collector_search_cost:
  collection_window:
```

硬鎖：

> `debtor_location` 不只是地圖資料；它直接影響應收可實現性。

---

# BC｜協議延期 vs 單方拖延

## BC-001｜NEGOTIATED DEFERRAL：第128–129回

章秋谷向陸麗娟提出：

```text
今年酒局帳約三百
→ 一時周轉不來
→ 請求暫時耽擱
→ 正月再付
→ 陸麗娟明確答應
```

翌回章秋谷其實有錢，最後照付。

但事件本身仍證明：

```yaml
NEGOTIATED_DEFERRAL:
  debtor_disclosure: true
  requested_new_due_date: true
  creditor_acceptance: true
  relation_context: "EXPLICITLY RELEVANT"
  default_status: false
```

因此：

> **延期可以是一筆新的雙方約定，而不是違約。**

---

## BC-002｜UNILATERAL DEFERRAL：第62回宋子英

宋子英被當場追局帳時主張：

```text
現在又不是年節
→ 自稱還會再來
→ 要求回院後再說
```

王黛玉等不接受，認為自身堂子名氣與收帳風險要緊。

這裡：

```yaml
UNILATERAL_DEFERRAL_ATTEMPT:
  debtor_promises_future_presence: true
  creditor_acceptance: false
  immediate_collection_pressure: true
```

所以：

```text
"I will pay later"
!=
EXTENSION AGREEMENT
```

---

# BD｜部分清償與折收

## BD-001｜第62回：第三人介入的部分結清

三位倌人的帳面應收合計接近二百元。

章秋谷介入後：

```text
要求宋子英拿出一百六十
→ 分給三位債權人
→ 差額不再追究
```

這不是正文固定詞「折帳」，但事件功能可安全記為：

```yaml
MEDIATED_PARTIAL_SETTLEMENT:
  face_amount: "~200"
  cash_paid: 160
  mediator: "章秋谷"
  creditor_acceptance: true
  remaining_claim: "WAIVED / NOT PURSUED IN SCENE"
```

硬鎖：

> **部分付款能否結案，取決於債權人是否接受差額不再追究。**

---

## BD-002｜第128回：八折是預期回收率

陸麗娟：

```text
帳面約二千多
→ 先排除兩個不在上海的客人
→ 可追約一千六百
→ 能收成八折已算好
```

這不是單一債務人主動「談八折」，而是：

```yaml
PORTFOLIO_COLLECTION_EXPECTATION:
  face_receivable:
  collectible_receivable:
  expected_recovery_rate:
```

---

## BD-003｜第162回：九折是實際結果

花婷婷：

```text
酒局帳約七八百
→ 到二十三日已收齊
→ 八百只打九折
→ 敘事稱已屬極好
```

因此：

```text
EXPECTED COLLECTION RATE
!=
ACTUAL COLLECTION RATE
```

並且：

> `收齊` 在此語境不必等於帳面原價 100% 收回，而可指本輪協商後應收已全部結束。

這一點未來必須避免機械誤讀。

---

# BE｜支付優先序

## BE-001｜第165回沈二寶：資金不足時不是平均分配

店家集中上門後，沈二寶：

```text
先挑「必不可少」的幾家
→ 全數付清

其他較不緊要的
→ 提議先付一些
→ 剩餘過年後再付
```

因此：

```yaml
PAYMENT_PRIORITY:
  available_cash:
  obligations: []

  prioritization_inputs:
    - "operational_necessity"
    - "creditor_pressure"
    - "relationship"
    - "future_service_dependency"
    - "reputation_risk"

  allocation:
    - full_pay
    - partial_pay
    - defer
```

硬鎖：

> **現金不足時不能自動按比例平均付款。**

人物會選擇。

---

# BF｜債權人是否接受延期，具有歷史依賴

## BF-001｜第164回：金姐接受短期延期

沈二寶欠金姐一百元找頭：

```text
原約停兩天再付
→ 後來仍缺一百多
→ 請金姐暫緩
→ 明年再付
→ 金姐雖不情願，仍答應
```

所以：

```yaml
EXTENSION_DECISION:
  creditor: "金姐"
  amount: 100
  creditor_acceptance: true
  acceptance_attitude: "RELUCTANT"
```

`acceptance = true` 不要求情緒上樂意。

---

## BF-002｜第165回：店家拒絕延期

沈二寶同樣向店家提出：

```text
先付一些
→ 其餘過年再付
```

但店家拒絕。

正文給出的重要前史：

```text
端午帳未清
+
中秋帳未清
+
年底再次要求延期
→ 債權人信心已崩
→ 不肯再通融
```

因此：

```yaml
CREDITOR_CONFIDENCE:
  prior_due_dates_missed:
  prior_extensions:
  current_perceived_wealth:
  current_business_condition:
  repayment_history:
  relationship_strength:
  collateral_or_evidence:
```

這形成：

> **信用不是人物固定屬性，而是債務歷史的累積結果。**

---

# BG｜債權人看的是「你還不還得出來」，不只看「你現在付不付」

第165回敘事有一段很強的市場觀察：

```text
若債務人被認為有錢
→ 即使暫時一文不付
→ 債權人也可能較放心

若被認為已經沒錢
→ 債權人反而更緊逼
```

這是敘事者概括，不先升成普遍世界定律。

但可作候選：

```yaml
CREDITOR_RISK_ASSESSMENT:
  current_cash_payment:
  perceived_net_worth:
  expected_future_income:
  business_momentum:
  reputation_for_payment:
  reachability:
  prior_default_history:
```

所以：

```text
CURRENT PAYMENT
!= CREDITWORTHINESS

CREDITWORTHINESS
!= WEALTH ALONE
```

---

# BH｜STRATEGIC WITHHOLDING｜故意扣帳

## BH-001｜第101回陳海秋

此案與「沒錢」完全不同：

```text
帳：約六百多
債務承認：YES
支付能力：YES
現金可得：YES
立即支付：NO
原因：故意用款項逼范彩霞改變待遇
```

陳海秋甚至明說錢在手上，六百乃至更多都拿得出來，但暫不交付。

因此：

```yaml
STRATEGIC_WITHHOLDING:
  debt_acknowledged: true
  ability_to_pay: true
  liquidity_available: true
  payment_withheld: true
  leverage_goal: "RELATIONAL / SERVICE PRESSURE"
```

這與：

```text
DEFAULT_DUE_TO_INSOLVENCY
```

完全不同。

硬鎖繼續保留：

> **世界中存在這種施壓行為，不代表支付或欠款取得人物、關係、住夜或親密的權利。**

---

# BI｜賒帳與欠帳交情：信用交易本身是市場常態之一

第139回姓焦客人主張：

```text
堂子吃酒不可能人人都現付
→ 自己與房間有欠帳往來
→ 只要房間自己放心即可
```

這是**人物主張**，不能直接升為全上海規則。

但同場其他人並未否認「賒帳／欠帳往來」本身的存在，而是拿他是否有能力撐起當場鬥氣開銷來攻擊。

因此目前最安全結論：

```yaml
CREDIT_TRANSACTION:
  existence_in_market: "CONFIRMED"
  universal_rule: false
  eligibility_basis: "NOT_YET_FULLY_RESOLVED"
  may_depend_on:
    - prior_relation
    - perceived wealth
    - payment history
    - room willingness
```

---

# BJ｜信用能力也存在風月場之外

第130回馬山甫說：

```text
平時透過往來錢莊
→ 五百、五千都「拖欠得動」

但年底
→ 錢莊只收歸帳
→ 不願再放出
```

此處不是堂子局帳，而是城市金融網。

它補強：

```yaml
CITY_CREDIT_CAPACITY:
  institution_relation:
  season:
  existing_exposure:
  market_liquidity:
  reputation:
```

所以：

> **角色的「有錢」與「現在能借到錢」也不是同一件事。**

這對未來晚清城市 Runtime 很重要，但不併入純 FENGYUE relation。

---

# BK｜債務行為會反向改變名聲與未來信用

目前可以閉合：

```text
TRANSACTION
→ RECEIVABLE
→ DUE DATE

→ FULL PAY
   └─ repayment history improves / remains sound

→ NEGOTIATED DEFERRAL
   └─ relation-based accommodation
   └─ may remain non-default

→ PARTIAL PAY
   └─ remaining claim persists unless waived

→ DEFAULT / AVOIDANCE
   └─ collection cost rises
   └─ creditor liquidity falls
   └─ reputation risk
   └─ future credit tightens

→ STRATEGIC WITHHOLDING
   └─ relation conflict
   └─ coercive pressure event
   └─ creditor liquidity shock
```

再接 V0.7：

```text
PAYMENT HISTORY
→ CLIENT / DEBTOR REPUTATION
→ FUTURE CREDIT ELIGIBILITY
→ FUTURE TRANSACTION TERMS
```

這代表 `LEDGER GRAPH` 已經開始變成一個真正的**信用記憶網**。

---

# BL｜第一版 DEBT OBJECT 候選

```yaml
DEBT_POSITION:
  debt_id:
  creditor:
  debtor:
  source_account:
  source_line_items: []

  face_amount:
  due_window:
  amount_paid:
  remaining_claim:

  debtor_state:
    liquidity:
    ability_to_pay:
    willingness_to_pay:
    reachable:
    avoidance_behavior:

  negotiation:
    requested_extension:
    requested_partial_payment:
    proposed_haircut:
    creditor_acceptance:
    agreed_new_due_date:

  collection:
    collectors: []
    attempts: []
    search_cost:
    pressure_level:
    actual_recovery:
    recovery_rate:

  history:
    prior_due_dates_missed:
    prior_partial_payments:
    prior_extensions:
    prior_defaults:

  social_effect:
    face_effect:
    reputation_effect:
    relation_effect:
    future_credit_effect:
```

仍為：

`CORPUS_DERIVED_SCHEMA_CANDIDATE`

不是正式 Runtime。

---

# BM｜本輪形成的新禁止簡化

```text
未付款 -> 漂帳
延期 -> 違約
部分付款 -> 帳已結
收齊 -> 帳面100%收回
有錢 -> 一定會付
沒現金 -> 沒信用
欠帳 -> 關係資格
欠帳交情 -> 恩客
債權人答應延期 -> 債權人心情愉快
曾經能賒帳 -> 永遠有信用
上一節沒收齊 -> 下一節必定不能再做生意
```

---

# BN｜raw-hit 索引（INDEX ONLY）

以下為全 192 回 exact substring 索引，只作檢索入口：

```yaml
RAW_HIT_INDEX:
  漂帳:
    hits: 8
    chapters: [99,129]

  漂了:
    hits: 1
    chapters: [23]

  拖欠:
    hits: 2
    chapters: [90,130]

  通融:
    hits: 13
    chapters: [2,56,58,60,79,83,84,117,130,165,174,175]

  暫緩:
    hits: 1
    chapters: [164]

  欠帳:
    hits: 7
    chapters: [10,12,139,165]

  賒帳:
    hits: 4
    chapters: [139,144]

  收帳:
    hits: 9
    chapters: [10,12,64,101,128,165]

  還帳:
    hits: 4
    chapters: [10,92,129]

  折帳:
    hits: 1
    chapters: [128]

  八折帳:
    hits: 1
    chapters: [128]

  九折:
    hits: 1
    chapters: [162]
```

注意：

- `拖欠／通融／欠帳／賒帳` 有大量非風月帳務語境；
- `漂帳` 是本輪最有辨識度的風月信用風險詞；
- 第129回大量 `漂帳` 出現於「假漂帳」測試，因此 raw hit 絕不能當實際違約事件數。

---

# BO｜下一輪抽取優先

1. 抽蘇州 `書寓／堂子／酒席／請酒／碰和` 的場域制度，補上海中心偏差。
2. 將 `CLIENT FLOW` 拆成打茶圍、叫局、吃酒、碰和、住夜等不同事件流。
3. 抽 `紅倌人` 的形成、維持與衰退，不把「紅」直接等同名氣或收入。
4. 開始 Stage 1 CROSS-CHECK：用反例攻擊 V0.1–V0.8 的候選規則。
5. 建 `CREDIT HISTORY → FUTURE TERMS` 的跨節期時間序列，驗證信用是否足以形成獨立 Market 子層。
---

# CA｜SUZHOU MARKET / VENUE SYSTEM｜蘇州風月市場與場域制度

> 本節專門修正 V0.1–V0.8 逐步形成的「上海中心偏差」。  
> 《九尾龜》正文自己反覆比較上海與蘇州，且同一城市的規矩還會隨時間、營業慣例與市場反應改變。  
> 因此本節不建立「全世界統一價目表」，而建立 **CITY / VENUE / TIME / TRANSACTION SCOPED RULES**。

---

## CA-000｜城市規則必須有作用域

目前 Corpus 已足以支持：

```yaml
MARKET_RULE_SCOPE_CANDIDATE:
  city:
  district:
  venue_class:
  household_or_room:
  transaction_type:
  client_relation_scope:
  time_period:
  source_chapter:
  evidence_type:
  status:
    - "OBSERVED"
    - "PROVISIONAL"
    - "CONTESTED"
    - "UNKNOWN"
```

硬鎖：

```text
SHANGHAI RULE
!= SUZHOU RULE

SUZHOU RULE AT ONE TIME
!= ETERNAL SUZHOU RULE

NARRATOR PRICE QUOTE
!= UNIVERSAL PRICE CONSTANT
```

---

# CB｜URBAN ECOLOGY CHANGE｜蘇州風月空間本身會搬動

## CB-001｜第1回：倉橋濱書寓外移

第1回敘事明示：

```text
日本通商之後
→ 盤門城外開馬路
→ 設紗廠
→ 原在城內倉橋濱的書寓「統通搬到城外」
→ 大菜館／戲館／書場等娛樂設施也集中形成
```

因此：

```yaml
EVENT_PATTERN:
  id: "URBAN_ENTERTAINMENT_RELOCATION"
  chapter: 1
  city: "蘇州"
  observed_changes:
    - "書寓由舊城內節點向城外新馬路移動"
    - "風月、戲曲、飲食、交通節點形成新聚集區"
  cause_as_narrated:
    - "通商後城市開發"
```

這表示未來世界地圖不能只是一組永恆地點：

> **城市經濟與交通改變，可以讓娛樂／風月節點本身遷移。**

---

# CC｜SHUCHANG DISCOVERY PIPELINE｜書場作為認識與導流節點

## CC-001｜第1回：初到蘇州者可以先在書場「看見市場」

章秋谷初到蘇州，沒有熟識，先進餘香閣書場。

事件鏈：

```text
初到城市／無熟識
→ 進書場泡茶
→ 看台上倌人
→ 堂倌介紹人物、名氣與所長
→ 客人用粉牌點戲／小調
→ 「當台招呼」
→ 大姐下場與客人接觸、問姓氏、應酬
→ 倌人唱畢
→ 大姐／倌人邀客之後到其住所
→ 客人結書場帳
→ 由大姐帶路到倌人房間
```

因此書場至少具有：

```yaml
SHUCHANG_FUNCTION:
  - "DISCOVERY"
  - "PUBLIC_DISPLAY"
  - "PERFORMANCE"
  - "INITIAL_CONTACT"
  - "SOCIAL_ROUTING"
  - "HOUSEHOLD_REFERRAL"
```

重要：

> **書場不是堂子房間的同義詞。**

它可以是「看見人、點藝、建立第一筆接觸、再導流到房間」的獨立節點。

---

## CC-002｜堂倌與大姐在這條入口鏈中作用不同

第1回：

```yaml
ROLE_SPLIT:

  堂倌:
    observed:
      - "向陌生客介紹倌人"
      - "取粉牌／筆"
      - "處理點戲"
      - "結書場帳"

  大姐:
    observed:
      - "下場裝煙、問客人姓氏、應酬"
      - "承接倌人與客人的第一輪社交"
      - "可陪客人前往倌人住所"
```

所以：

```text
堂倌
!= 大姐
!= 相幫
```

三者不能在 Runtime 裡合成「服務 NPC」。

---

# CD｜SUZHOU BANQUET COST STACK｜蘇州酒席不是一個價錢

## CD-001｜第1回：丟檯面

第1回的敘事規則：

```text
姑蘇書寓請客
→ 每位客人現出檯面洋二元
→ 稱「丟檯面」
```

實際事件：

```text
7位客人 × 2元 = 14元
+
主人另出下腳4元
+
添菜2元
=
檯面上共20元被相幫收走
```

這一場至少證明：

```yaml
BANQUET_PAYMENT:
  participant_table_fee:
    amount_observed: 2
    payer: "EACH_GUEST"
    timing: "IMMEDIATE"

  host_additional_outlays:
    observed:
      - "下腳"
      - "添菜"
```

但：

> 第1回這組 `下腳4 / 添菜2` 只先保存為**該事件帳目**，不升成所有蘇州酒席固定價。

---

## CD-002｜第54回再次確認檯面洋錢

第54回更詳細：

```text
一台酒正價：12元
+
無論主客，每人檯面洋錢：2元
+
叫來的局，每人坐場洋錢：1元
```

正文舉例：

```text
8個客人
每人叫1個局

→ 檯面洋錢 16
→ 坐場洋錢 8
→ 均在酒的正價12元之外
```

因此：

```text
BANQUET BASE PRICE
!= TOTAL EVENT COST
```

正確形狀應接 V0.5 `LINE ITEM`：

```yaml
SUZHOU_BANQUET_ACCOUNT:
  base_wine_price:
  guest_table_fees: []
  called_courtesan_sitting_fees: []
  food_additions: []
  other_observed_items: []
```

---

# CE｜坐場洋錢｜出局本身形成前置現金曝險

## CE-001｜第54回：坐場洋錢一元

正文：

```text
叫來的局
→ 每人坐場洋錢1元
→ 當場開發
```

後面又補：

```text
客人的局帳
→ 逢節才開銷

但倌人出局的坐場洋錢
→ 先要自家墊出
```

因此：

```yaml
CALL_OUT_CASHFLOW:
  client_receivable:
    settlement: "FESTIVAL / CREDIT"

  courtesan_upfront_exposure:
    item: "坐場洋錢"
    timing: "IMMEDIATE"
```

這形成非常重要的市場結構：

> **接受一次叫局，對倌人一方可能先產生現金曝險，再等之後收客人的帳。**

---

# CF｜CALL ACCEPTANCE IS ALSO CREDIT DECISION｜應局也是信用決策

## CF-001｜第54回：素來相識方肯應酬

第54回直接解釋蘇州：

```text
客人叫局
→ 往往要與倌人素來相識
→ 才肯應酬
```

敘事給出的原因不是「愛不愛」：

```text
客人局帳要到逢節才開銷
+
倌人出局的坐場洋錢先要自己墊
```

因此：

```yaml
CALL_ACCEPTANCE_CANDIDATE:
  inputs:
    - prior_acquaintance
    - debtor_reputation
    - payment_history
    - expected_collectibility
    - current_schedule
    - current_cash_exposure
    - relationship_context

  not_equal:
    - "private_preference"
    - "love"
    - "automatic regular-client status"
```

這是目前 Corpus 最強的：

> **FENGYUE SOCIAL RELATION × CREDIT SYSTEM 接口。**

---

# CG｜INVITATION ACCEPTANCE HAS ECONOMIC FRICTION｜受邀赴酒不是免費社交

## CG-001｜第1回

正文說：

```text
蘇州朋友被請吃花酒
→ 若非素日知己，不肯到場
```

原因：

```text
要賠貼局錢
+
自己還要現丟檯面
```

並特別與上海對比：

```text
上海被請吃花酒
→ 客人到了常被視作「賞光」
```

---

## CG-002｜第54回再確認

第54回再次說：

```text
蘇州堂子擺酒請客
→ 被請者通常須與主人向來要好
→ 因為來客自己要開銷檯面現錢
```

因此：

```yaml
BANQUET_INVITATION_DECISION:
  social_closeness:
  immediate_out_of_pocket_cost:
  expected_face_return:
  time_cost:
  relation_with_host:
```

硬鎖：

> **收到請客票 ≠ NPC 必然赴約。**

玩家或 NPC 在蘇州請一桌客，不能只靠「邀請成功率」；對方是在衡量一筆實際社交成本。

---

# CH｜PENGHE EVOLUTION｜碰和不是從來就有的固定商品

## CH-001｜第54回：蘇州碰和制度有「形成史」

第54回敘事：

```text
蘇州本來：
只有吃酒
沒有正式碰和
```

偶爾客人高興：

```text
自行約朋友碰一場
→ 和錢可4元、6元
→ 沒有一定
```

後來：

```text
有一班人只來碰和、不吃酒
→ 煙茶酒飯照樣大量消耗
→ 本家與倌人吃虧
→ 蘇州開始仿上海「行出碰和名目」
→ 每場正式收8元
```

因此：

```yaml
INSTITUTION_EVOLUTION:
  id: "SUZHOU_PENGHE_FORMALIZATION"
  stage_1:
    state: "NO_FORMAL_PRODUCT"

  stage_2:
    state: "AD_HOC"
    fee: "VARIABLE 4 / 6 OBSERVED"

  stage_3:
    trigger: "CUSTOMER_BEHAVIOR_CAUSES_HOUSE_LOSS"
    response: "FORMALIZE_FEE"

  stage_4:
    fee_observed: 8
```

高價值結論：

> **市場規矩不是背景常數；它也會因參與者鑽制度漏洞而改變。**

---

# CI｜HOUSE PREFERENCE REVERSAL｜上海與蘇州的「好生意」不是同一交易

第54回敘事明確比較：

```text
上海：
吃酒 → 房間人員好處較少，主要是繃外場
碰和 → 房間人員有些好處

所以：
上海堂子偏願碰和、不願吃酒
```

相對：

```text
蘇州：
吃酒
→ 正價
→ 檯面洋錢
→ 坐場洋錢
→ 倌人／房間有額外收益

所以：
蘇州堂子偏巴吃酒、不願碰和
```

因此：

```text
SAME TRANSACTION NAME
may have
DIFFERENT HOUSEHOLD INCENTIVE
by CITY
```

這代表未來 NPC 不應只看：

```text
transaction_value
```

而要看：

```yaml
HOUSEHOLD_TRANSACTION_INCENTIVE:
  gross_fee:
  staff_share:
  upfront_cost:
  delayed_receivable:
  food_and_service_cost:
  public_face_effect:
```

---

# CJ｜PRICE SOURCE CONFLICT｜原作內部價目衝突必須保留

這輪出現 Stage 1 第一個非常乾淨的價目矛盾。

## CJ-001｜第1回

```yaml
PRICE_OBSERVATION:
  chapter: 1
  shanghai_penghe: 20
  suzhou_penghe: 8
```

正文用語近於：

```text
上海碰和一概二十元
蘇州無論長三么二均八元
```

---

## CJ-002｜第54回

```yaml
PRICE_OBSERVATION:
  chapter: 54
  shanghai_wine: 12
  shanghai_penghe: 12
  suzhou_wine_base: 12
  suzhou_penghe: 8
```

因此：

```yaml
PRICE_CONFLICT:
  field: "SHANGHAI_PENGHE"
  chapter_1: 20
  chapter_54: 12
  resolution: "UNRESOLVED"
  possible_explanations:
    - "time change"
    - "different contextual rule"
    - "narrative inconsistency"
    - "other unextracted distinction"
  canon_choice: "NONE"
```

硬鎖：

> **不得為了 Runtime 好寫，就偷偷選 12 或 20 當唯一真價。**

尤其第54回自己還說「初集已說過，只是沒有這般詳細」，所以原作者顯然把兩段當成相容；但目前文本表面數字仍衝突。

Corpus 必須保存衝突，而不是替作者完成沒有寫出的解釋。

---

# CK｜堂唱需要拆語義，不可做單一布林

## CK-001｜第1回的「生客入門堂唱」

第1回敘事：

```text
以前上海：
生客進門
→ 倌人必唱京調／小曲一支
→ 稱「堂唱」
→ 須現錢開銷

敘事當時：
上海此例已除
蘇州仍未改
```

這裡說的是：

> **FIRST-VISIT ENTRY CUSTOM**

---

## CK-002｜但後文上海仍反覆出現「堂唱／出堂唱」

第7、19、92回的上海事件仍使用：

```text
堂唱
出堂唱
堂唱回來
```

因此不能推出：

```text
上海已完全沒有「堂唱」這種活動
```

比較安全的 Corpus 結論：

```yaml
TERM_POLYSEMY_CANDIDATE:
  term: "堂唱"

  subtype_A:
    observed_in: 1
    meaning:
      - "生客進門時的制度性唱曲／開銷習俗"

  subtype_B:
    observed_in: [7,19,92]
    meaning:
      - "倌人外出／進行某種堂唱活動"
      - "具體制度邊界仍需再抽"

  rule:
    - "ABOLITION_OF_SUBTYPE_A != ABOLITION_OF_ALL_DANGCHANG_ACTIVITY"
```

這是 Corpus cross-check 的典型例子：

> **同一詞，不保證全書只有一種制度語義。**

---

# CL｜MOBILE SOCIAL VENUE｜風月場可以離開堂子

## CL-001｜第52回：虎丘遊船可「帶一個局」

第52回：

```text
陸仲文游虎丘
→ 坐小陳家雙開門船
→ 帶一個局王小寶同行
```

因此：

```text
COURTESAN PARTICIPATION
is not limited to
COURTESAN HOUSE / RESTAURANT
```

---

## CL-002｜第60回：船上臨時寫局票

第60回：

```text
準備游虎丘
→ 在船上問「可要帶局」
→ 直接向船家借筆硯
→ 寫多張局票
→ 各人的局陸續到船
→ 人到齊後開船
```

這是完整：

```yaml
EVENT_PATTERN:
  id: "MOBILE_VENUE_CALL_OUT"

  origin:
    venue: "BOAT"

  call_creation:
    document: "局票"
    writing_location: "BOAT"

  destination:
    type: "MOVING_VENUE"

  sequence:
    - "call tickets written"
    - "courtesans arrive"
    - "boat departs"
    - "group travels"
```

所以未來 `CALL_OUT.destination` 必須能接受：

```text
STATIC_ROOM
RESTAURANT
GARDEN
BOAT
OTHER_EVENT_VENUE
```

不能只存 `house_id`。

---

## CL-003｜山塘／吉公祠／船菜形成多節點遊樂鏈

第60回：

```text
船行至山塘
→ 吉公祠上岸吃茶
→ 再上船
→ 船中擺檯面
→ 倌人坐在客人身後
→ 吃小陳家船菜
```

因此一場事件可以跨：

```text
BOAT
→ WATERWAY
→ LAND POI
→ TEA STOP
→ BOAT BANQUET
```

高價值結論：

> **「場景」不是永遠等於一個固定房間。**

這與《九尾龜》世界網絡型設計高度一致。

---

# CM｜SUZHOU EVENT PIPELINES｜第一版蘇州事件鏈

## CM-001｜陌生外客進場

```text
客棧
→ 書場
→ 堂倌介紹
→ 點戲
→ 公開表演
→ 大姐接觸
→ 倌人／大姐邀往住所
→ 倌人房間
→ 可能請客／叫局／吃酒
```

---

## CM-002｜堂子請酒

```text
主人決定擺酒
→ 確認房間
→ 叫菜
→ 發請客票
→ 受邀客衡量是否赴席
→ 發局票
→ 倌人赴局
→ 入席
→ 基礎酒價
   + 檯面洋錢
   + 坐場洋錢
   + 其他事件項
→ 帳務／現金流
```

---

## CM-003｜碰和

```text
朋友湊足
→ 定底碼／規則
→ 碰和
→ 玩家間輸贏
→ 另有「和錢」／堂子收益項
→ 飯菜／煙茶等成本
```

注意：

> 麻將桌上的輸贏，與支付給堂子／房間的碰和費是不同金流。

---

## CM-004｜移動遊樂

```text
決定游虎丘
→ 租／登船
→ 寫局票
→ 等倌人到齊
→ 開船
→ 山塘／景點
→ 上岸吃茶
→ 回船擺酒
→ 後續娛樂／社交事件
```

---

# CN｜CITY RULE MATRIX｜目前可支持的蘇滬差異

```yaml
CITY_RULE_MATRIX:

  SUZHOU:

    banquet_guest_table_fee:
      observed: 2
      timing: "IMMEDIATE"
      chapters: [1,54]

    sitting_fee_per_called_courtesan:
      observed: 1
      timing: "UPFRONT / IMMEDIATE"
      chapter: 54

    formal_penghe_fee:
      observed: 8
      chapters: [1,54]

    banquet_base_price:
      observed: 12
      chapter: 54

    first_visit_dangchang_custom:
      status: "NARRATOR SAYS STILL ACTIVE"
      chapter: 1

    invitation_friction:
      observed: "HIGHER DUE TO GUEST OUT-OF-POCKET COST"
      chapters: [1,54]

    call_credit_exposure:
      observed: true
      chapter: 54

  SHANGHAI:

    banquet_guest_table_fee:
      observed_contrast: "SUZHOU-SPECIFIC FEE ABSENT IN COMPARISON"
      chapters: [1,54]

    penghe_price:
      observations:
        - {chapter: 1, amount: 20}
        - {chapter: 54, amount: 12}
      status: "CONTESTED"

    wine_price:
      observed: 12
      chapter: 54

    first_visit_dangchang_custom:
      status: "NARRATOR SAYS ABOLISHED"
      chapter: 1

    other_dangchang_activity:
      status: "STILL ATTESTED"
      chapters: [7,19,92]
```

此表只表示**目前正文觀察**，不是完整城市法典。

---

# CO｜本輪形成的新市場硬結論候選

```text
CITY
is a first-class rule scope

VENUE
is a first-class rule scope

TIME / INSTITUTION HISTORY
may change transaction rules

BANQUET BASE PRICE
!= TOTAL BANQUET COST

CALL OUT
may create upfront cost for courtesan

CALL ACCEPTANCE
may depend on credit exposure

INVITATION
!= FREE ATTENDANCE

INVITATION RECEIVED
!= ATTENDANCE

PENGHE
has institutional history

SAME TRANSACTION NAME
!= SAME CITY INCENTIVE

SOURCE PRICE CONFLICT
must remain unresolved until evidence resolves it

DANGCHANG
requires semantic subtype separation

CALL DESTINATION
may be mobile

SOCIAL EVENT
may cross multiple physical nodes
```

---

# CP｜raw-hit 索引（INDEX ONLY）

以下仍只作全文檢索入口：

```yaml
RAW_HIT_INDEX:

  坐場:
    hits: 5
    chapters: [54,144]

  檯面洋錢:
    hits: 2
    chapters: [54]

  堂唱:
    hits: 5
    chapters: [1,7,19,92]

  書場:
    hits: 5
    chapters: [1,3]

  書寓:
    hits: 6
    chapters: [1,3,23,91,95]

  山塘:
    hits: 2
    chapters: [60]

  虎丘:
    hits: 9
    chapters: [52,58,59,60,68]

  船菜:
    hits: 2
    chapters: [60,61]

  盤門:
    hits: 5
    chapters: [1,32,48]

  石路:
    hits: 6
    chapters: [5,17,43,54,58,191]

  甘棠橋:
    hits: 5
    chapters: [1,3,57]

  餘香閣:
    hits: 9
    chapters: [1,3,21,57]

  佛照樓:
    hits: 9
    chapters: [1,2,3,21,32]
```

注意：

- `坐場` 第144回屬其他城市語境，不能全算蘇州；
- `書寓` 在後文也可作身份／營業層級用語，不只指蘇州；
- `堂唱` 已確認至少有不同語境，不能單靠 hit 數量定義；
- raw hit 仍沒有制度法位。

---

# CQ｜Stage 1 到此出現的一個更大結構

V0.1–V0.8 主要逐步抽出：

```text
人物
→ 房間／Household
→ 關係資格
→ 生命周期
→ 帳務
→ 知情／傳聞
→ Reputation / Demand
→ Credit Memory
```

V0.9 補上的不是「蘇州 DLC」，而是：

```text
CITY / VENUE / TIME
```

作為整張網的上位環境作用域。

因此目前比較接近：

```text
CITY / TIME / MARKET REGIME
        ↓
VENUE NETWORK
        ↓
HOUSEHOLD / ROOM
        ↓
CHARACTER / ROLE
        ↓
RELATION / KNOWLEDGE / REPUTATION
        ↓
TRANSACTION / CREDIT / CASHFLOW
        ↓
WORLD EVENT
        ↺
```

這比單一「堂子 Runtime」更接近 MEMO 原定目標：

> **整個晚清蘇滬風月社會網。**

---

# CR｜下一輪抽取優先

1. 將 `CLIENT FLOW` 正式拆成：
   - `茶圍`
   - `堂唱`
   - `叫局`
   - `吃酒`
   - `碰和`
   - `住夜`
   等不同事件流，不再用一個 visit count。
2. 抽 `紅倌人` 的形成、維持、衰退與市場後果。
3. 開始 Stage 1 `CROSS-CHECK / COUNTEREXAMPLE PASS`，專門攻擊 V0.1–V0.9 已形成的候選規則。
4. 對 `PRICE / FEE` 做 source-conflict index，不在 Runtime 前偷偷清洗原作矛盾。
5. 補 `CITY TRANSITION`：人物由上海→蘇州→天津時，哪些狀態帶走、哪些市場狀態重算。
---

# CS｜CLIENT FLOW EVENT FAMILY｜客流不是 Visit Count

> 本節承接 V0.7 `REPUTATION → CLIENT FLOW` 與 V0.9 `CITY / VENUE / TIME SCOPE`。  
> 目標是把過去暫稱的「客流」拆成正文實際存在的不同事件流。  
> 初始預計六類：`茶圍／堂唱／叫局／吃酒／碰和／住夜`；抽取後正文另逼出一條不能合併的 `檯面局／場館配置應酬` 候選。

目前最安全的總結：

```text
CLIENT FLOW
!= VISIT COUNT

TEA VISIT
!= CALL-OUT

CALL REQUEST
!= ACTUAL OUTCALL

BANQUET
!= PENGHE

PENGHE
!= OVERNIGHT

OVERNIGHT
!= RELATION QUALIFICATION

HOUSE-ASSIGNED TABLE SERVICE
!= CLIENT-NAMED CALL
```

---

# CT｜TEA_VISIT / 打茶圍｜低門檻到房拜訪流

## CT-001｜基本形狀：客人到房間，而不是把倌人叫出去

第43回：

```text
章秋谷等
→ 到王佩蘭住所
→ 找牌子／問房間
→ 上樓
→ 大姐招呼
→ 王佩蘭應酬
```

這是典型：

```yaml
EVENT_PATTERN:
  id: "TEA_VISIT"
  actor_move:
    client: "TO_COURTESAN_ROOM"
    courtesan: "MAY_ALREADY_BE_PRESENT_OR_RETURN_LATER"

  possible_functions:
    - "SOCIAL_VISIT"
    - "CONVERSATION"
    - "INITIAL_OR_REPEAT_CONTACT"
    - "LOWER-COST MARKET CONTACT"
```

---

## CT-002｜可以連續打多處，不形成排他關係

第8回：

```text
方幼惲、劉厚卿
→ 花寶玉家打一個茶圍
→ 林佩珠家再打一個茶圍
```

第30回：

```text
貢春樹、呂仰正
→ 路上連打兩處茶圍
→ 再去碰和
```

因此：

```text
TEA_VISIT_COUNT
!= EXCLUSIVITY
```

甚至：

```text
MULTIPLE_TEA_VISITS_SAME_DAY
is normal enough to be directly observed
```

---

## CT-003｜茶圍有「次數」與「時段」兩個不同維度

第14回金漢良：

```text
打茶圍沒有時候
→ 常在未到中午就來
→ 坐下後又久久不走
→ 金小寶與房間人員厭煩
```

所以：

```yaml
TEA_VISIT_STATE:
  arrival_time:
  duration:
  frequency:
  courtesan_available:
  room_load:
  client_behavior:
```

硬鎖：

> **來得勤，不等於受歡迎。**

---

## CT-004｜早到本身可以被視為反常

第113回約十一點：

```text
樓下相幫叫「客人上來」
→ 章秋谷心中詫異
→ 認為這個時候竟已有打茶圍客人
```

因此：

```text
TEA_VISIT
has a social-time rhythm
```

但目前尚不足以建立全上海固定營業時段。

---

## CT-005｜倌人可以因當下狀態不出來應酬

第161回沈二寶：

```text
一批打茶圍客人到房
→ 沈二寶不肯出去應酬
→ 娘姨以「先生有病」回覆
→ 客人略坐後離去
```

所以：

```text
CLIENT ARRIVAL
!= COURTESAN APPEARANCE
```

也不應由系統替人物強制履行。

---

## CT-006｜天津茶圍是逐次計價的獨立交易

第142回：

```text
北班茶圍：2
南班茶圍：1
一天去十趟
→ 就要付十次
```

並且生客初次進班：

```text
先看合班姑娘
→ 若一個都不中意
→ 可直接離開，不付錢

選中
→ 到該姑娘房間
→ 才進入茶圍
```

因此：

```text
DISCOVERY / SELECTION
!= TEA_VISIT

TEA_VISIT
is repeatable per-occurrence transaction
in this Tianjin rule set
```

---

# CU｜CALL REQUEST → OUTCALL｜叫局與出局必須拆開

## CU-001｜叫局是請求／派單端

上海與蘇州事件反覆呈現：

```text
客人／席間決定叫某倌人
→ 寫局票／局條
→ 相幫送出
→ 房間收到
```

例如第35回：

```text
碰和前
→ 先寫局票
→ 各客點名不同倌人
→ 相幫發票
```

因此：

```yaml
CALL_REQUEST:
  requester:
  named_courtesan:
  request_document:
    - "局票"
    - "局條"
  destination:
  requested_time:
  intermediary:
```

---

## CU-002｜出局是執行端，不等於叫局已成立

第2回：

```text
相幫拿數張局票
→ 催花雲香去出黨差
```

第73回：

```text
院中接連派相幫催張書玉
→ 說叫局已催兩回
→ 還有房內客人等她
→ 張書玉仍不急著走
```

所以：

```text
CALL_REQUEST_CREATED
!= ACCEPTED
!= DEPARTED
!= ARRIVED
```

候選生命週期：

```yaml
CALL_LIFECYCLE:
  REQUEST_CREATED:
  REQUEST_DELIVERED:
  ACCEPTED:
  DECLINED:
  DEFERRED:
  DEPARTED:
  ARRIVED:
  SERVING:
  TEMPORARILY_LEFT:
  RETURNED:
  COMPLETED:
  MISSED_OR_DROPPED:
```

---

## CU-003｜「轉局」是多局排程，不是瞬間傳送

第5回陸蘭芬：

```text
同一席仍在應酬
→ 相幫送來一二十張局票
→ 催她轉局
→ 她要求回報「轉過來」
→ 目前客人同意她先去
→ 她才離席
```

因此：

```yaml
CALL_QUEUE:
  current_engagement:
  queued_calls: []
  delay:
  promised_return:
  travel_time:
```

這條與 V0.1 起即建立的 NPC autonomy 一致，但現在已有完整 Corpus 支持。

---

## CU-004｜收到局票可以主動不應

第22–23回林黛玉：

```text
一席之中收到二十多張局票
→ 她叫娘姨多回報「王家庫轉過來」
→ 自己繼續留在邱八席上

之後邱八追問：
為什麼有很多局票卻不去？

林黛玉：
明示今天「堂差不出」
```

因此：

> **高 demand 只增加 opportunity，不取消人物／房間的調度選擇。**

---

## CU-005｜上海熟客「通常會來」只是人物規則認知，不是硬保證

第34回章秋谷說：

```text
上海地方熟客叫局「那有不來之理」
```

這是章秋谷對市場慣例的判斷。

但第22–23、73回都已證明：

```text
即使有局
→ 仍可延遲、回報、脫局或不出
```

因此：

```yaml
EVIDENCE_STATUS:
  claim: "熟客叫局必到"
  source_type: "CHARACTER_CLAIM"
  status: "NOT_HARD_RULE"
```

---

# CV｜CITY DIFFERENCE IN CALL THROUGHPUT｜局量由制度共同決定

## CV-001｜第144回：上海與天津的局數巨大差異

敘事比較：

```text
上海紅倌人：
一夜可出五六十個局

天津頭等名角：
一夜至多六七八個局
```

正文給出的制度原因包括：

```text
天津叫局價格高
+
多數現錢
+
賒帳資格較窄
+
出局後不能隨意離席
+
要離開須「告假」
+
坐場成本
```

因此：

```text
CALL_VOLUME
is generated by
PRICE
+ CREDIT
+ SERVICE_DURATION
+ EXIT_RULE
+ VENUE_RULE
+ DEMAND
```

不是人物單一「人氣」欄位。

---

## CV-002｜天津叫局與上海的詞彙也不同

第147回：

```text
京津一帶
→ 不說「叫局」
→ 說「叫條子」
```

所以 normalized internal event 可用：

```text
CALL_REQUEST
```

但 lexical rendering 必須依城市：

```yaml
LOCAL_TERM:
  SHANGHAI_SUZHOU: "叫局 / 局票 / 局條"
  TIANJIN_BEIJING: "叫條子"
```

不得把 normalized 名稱冒充原作各城市共同用詞。

---

# CW｜DANGCHANG / 堂唱｜至少兩種語義，且是排程負載

V0.9 已確認：

```text
第1回：
堂唱 = 生客入門的制度性唱曲／現錢開銷習俗

第7、19、92回：
堂唱／出堂唱 = 倌人離開房間去從事某種堂唱活動
```

本輪新增的 client-flow 意義：

第19回：

```text
陳文仙堂唱回來
→ 才碰上房內衝突事件
```

第92回：

```text
客人已在房間碰完八圈
→ 薛金蓮仍不在
→ 回來短暫應酬
→ 又說「出堂唱去」
→ 再次離開
```

因此：

```yaml
DANGCHANG_FLOW:
  may_remove_courtesan_from_room: true
  may_compete_with:
    - "TEA_VISIT"
    - "PENGHE_ROOM_SERVICE"
    - "ROOM_GUEST_ATTENTION"

  semantic_subtypes:
    - "FIRST_VISIT_ENTRY_SINGING_CUSTOM"
    - "OUTSIDE_DANGCHANG_ASSIGNMENT"
```

尚不能把兩者強制合併成同一 transaction type。

---

# CX｜BANQUET / 吃酒 / 花酒｜群體席面流

## CX-001｜吃酒不是一般「喝一杯」，而常是可結算的席面事件

第14回上海：

```text
金漢良拿現錢要求擺酒
→ 敘事稱現錢擺酒不能推卻
→ 金小寶讓他吃一台
```

目前只安全記為：

```yaml
SHANGHAI_CASH_BANQUET_RULE:
  chapter: 14
  evidence_type: "NARRATOR_RULE"
  observed:
    - "現錢擺酒形成強營業義務"
  scope:
    - "上海堂子／該敘事時段"
```

不直接擴成全城市永恆公法。

---

## CX-002｜花酒可形成請客網

第1、5回均見：

```text
主人決定在倌人處擺酒
→ 寫請客票
→ 邀朋友
→ 再寫局票
→ 叫各人局
→ 入席
```

因此：

```yaml
BANQUET_EVENT:
  host:
  invited_guests: []
  host_courtesan_or_room:
  called_courtesans: []
  venue:
  table:
  line_items: []
  guest_attendance:
```

---

## CX-003｜吃酒可以與叫局綁在同一事件，但兩者仍是不同層

第5回：

```text
厚卿請客
→ 客人到席
→ 發局票
→ 各人的局陸續到
→ 倌人坐到對應客人身後
```

所以：

```text
BANQUET
contains
CALL-OUT PARTICIPANTS
```

但：

```text
BANQUET EVENT
!= EACH CALL REQUEST
```

一桌酒可能包含多條局生命周期。

---

## CX-004｜「花酒」與一般「吃酒」目前不可完全等號

第36回同一段同時使用：

```text
擺一台花酒
+
又吃一台酒
```

因此：

```yaml
LEXICAL_CAUTION:
  花酒:
    status: "BANQUET/FENGYUE-CONTEXT TERM"
  吃酒:
    status: "BROADER EVENT WORDING"

  equality:
    "NOT_PROVEN"
```

先保留 `BANQUET / WINE_EVENT` normalized family，等下一輪 lexical cross-check 再細分。

---

# CY｜PENGHE / 碰和｜賭局流，不是叫局或吃酒的別名

## CY-001｜有自己的玩家席位與遊戲循環

第35回：

```text
碰和腳色已齊
→ 配籌碼
→ 入座扳莊
→ 再發局票叫倌人
```

所以：

```yaml
PENGHE_EVENT:
  mahjong_players: []
  rounds:
  stakes:
  game_result:
  venue:
  called_courtesans: []
  house_fee:
  food_drink_cost:
```

---

## CY-002｜倌人可以被叫來「代碰」

第35回：

```text
陳海秋起身
→ 花筱舫坐下
→ 替他代碰
```

第93回：

```text
范彩霞在別處替客人代碰
→ 房內另一客人持續等待
```

因此：

```text
COURTESAN PRESENCE AT PENGHE
may be:
  - SOCIAL_COMPANION
  - CALLED_GUEST
  - SUBSTITUTE_PLAYER
```

不能只有 `present=true`。

---

## CY-003｜牌桌輸贏與堂子交易是兩套帳

第30回：

```text
碰和後
→ 客人間結算牌局輸贏
```

而 V0.9 第54回：

```text
碰和另有堂子／房間的和錢
```

所以：

```text
MAHJONG_STAKE_SETTLEMENT
!= HOUSE_PENGHE_FEE
```

兩者必須在 Ledger 分開。

---

# CZ｜OVERNIGHT / 住夜｜獨立 Access Event

## CZ-001｜天津直接明示：住夜與碰和／吃酒彼此不互為前置條件

第142回：

```text
住夜的客人
不必定要碰和吃酒

碰和吃酒的客人
也不必定要住夜
```

這是本輪最強硬鎖：

```text
OVERNIGHT
!= BANQUET UPGRADE

OVERNIGHT
!= PENGHE UPGRADE
```

---

## CZ-002｜上海長三案例可有「先做幾次市場往來」的社會期待，但不是保證

第36回花筱舫娘姨對初到上海的陳海秋說：

```text
長三堂子
→ 不同於么二／野雞
→ 通常要先碰幾場和、吃幾台酒
→ 到一定往來程度
→ 才好談住夜
```

陳海秋立即：

```text
擺花酒
→ 碰和
→ 再吃酒
→ 自認應該被留住夜
```

結果：

```text
花筱舫仍不留
```

所以：

```text
PRIOR MARKET HISTORY
may be a social prerequisite / expectation

but

PRIOR MARKET HISTORY
does not compel overnight
```

---

## CZ-003｜長期大量花費仍不能自動取得住夜

第92回范彩霞：

```text
陳海秋
→ 花費很多
→ 報效許多和酒
→ 幾個月
→ 仍沒有被留住夜
```

第101回他自己也明說：

```text
酒很多次
+
和很多場
+
花二三千
→ 仍沒有得到他期待的待遇
```

人物因此憤怒，但這只證明：

```text
SPENDING HISTORY
can create EXPECTATION / CONFLICT
```

不能證明：

```text
SPENDING HISTORY
creates RIGHT
```

---

## CZ-004｜住夜也有排程／房間衝突

第37回陸蘭芬：

```text
同晚出現兩個住夜客
+
方子衡已住在院內
→ 需要分房
→ 需要協調
→ 需要安排不同客人的時間與位置
```

因此：

```yaml
OVERNIGHT_SCHEDULING:
  requested_guests: []
  room_capacity:
  existing_house_guest:
  courtesan_decision:
  conflict_risk:
  room_assignment:
```

---

# DA｜SOURCE-FORCED SEVENTH FLOW｜檯面局／場館配置應酬

> 本輪原預計只拆六類，但第144回天津材料不允許這樣簡化。

## DA-001｜未點名叫局，也可能有「檯面局」

第144回：

```text
金觀察沒有叫局
→ 吃酒時照例仍有一個檯面局
→ 金蘭按叫局規條向他告假
```

之後：

```text
金蘭、雲蘭暫離
→ 本班其他姑娘進房應酬檯面
→ 一批出去
→ 再換一批進來
```

所以至少存在：

```yaml
HOUSE_ASSIGNED_TABLE_SERVICE:
  selected_by_client: false
  generated_by_venue_rule: true
  personnel:
    - "ROTATING_HOUSE_COURTESANS"
  purpose:
    - "TABLE_SERVICE"
    - "HOUSEHOLD_SOCIAL_COVER"
```

這與：

```text
CLIENT_NAMED_CALL_REQUEST
```

不是同一件事。

---

# DB｜CALL CHANNELS｜目前至少四種「倌人如何出現在場」

```yaml
COURTESAN_ARRIVAL_CHANNEL:

  1_CLIENT_NAMED_CALL:
    path:
      - "client names person"
      - "局票／局條"
      - "courtesan travels to venue"

  2_BROUGHT_ALONG:
    corpus_anchor: "第1回帶局"
    path:
      - "courtesan already accompanies client"
      - "no fresh call needed"

  3_HOUSE_TABLE_ASSIGNMENT:
    corpus_anchor: "第144回檯面局"
    path:
      - "venue/house rule assigns personnel"
      - "not client named"

  4_RETURN_FROM_OTHER_ENGAGEMENT:
    path:
      - "courtesan finishes／pauses another call"
      - "returns to room／table"
```

這代表：

> `NPC_PRESENT_AT_EVENT` 不能反推出「玩家叫來的」。

---

# DC｜FLOW CROSS-MATRIX｜一條流不能自動升成下一條

```yaml
CLIENT_FLOW_CROSS_MATRIX:

  TEA_VISIT:
    may_lead_to:
      - "future conversation"
      - "future banquet"
      - "future call"
    does_not_create:
      - "regular_client_status"
      - "enke"
      - "xianghao"
      - "overnight_right"

  CALL_OUT:
    may_lead_to:
      - "banquet participation"
      - "penghe participation"
      - "public familiarity"
    does_not_create:
      - "private_preference"
      - "overnight_right"
      - "exclusive relation"

  BANQUET:
    may_affect:
      - "public_face"
      - "ledger"
      - "reputation"
      - "social_history"
    does_not_create:
      - "overnight"
      - "enke"
      - "xianghao"

  PENGHE:
    may_affect:
      - "ledger"
      - "public_face"
      - "business_support"
      - "shared_event_history"
    does_not_create:
      - "overnight"
      - "love"
      - "exclusive relation"

  OVERNIGHT:
    creates:
      - "OVERNIGHT_EVENT_HISTORY"
    does_not_automatically_create:
      - "xianghao"
      - "enke"
      - "love"
      - "marriage"
      - "future consent"

  HOUSE_TABLE_SERVICE:
    creates:
      - "SERVICE_EVENT"
    does_not_create:
      - "named client-courtesan relation"
```

---

# DD｜CLIENT FLOW STATE｜不能再用一個 visit_count

目前比較安全的 Corpus 候選：

```yaml
CLIENT_FLOW_STATE:
  client_id:
  courtesan_id:
  city_scope:
  time_scope:

  tea_visits:
    events: []

  call_requests:
    events: []

  accepted_outcalls:
    events: []

  missed_or_declined_calls:
    events: []

  banquet_events:
    events: []

  penghe_events:
    events: []

  dangchang_intersections:
    events: []

  overnight_events:
    events: []

  house_assigned_service_events:
    events: []

  money_history:
    ledger_refs: []

  relation_qualification:
    separate_graph_ref:

  belief_and_rumor:
    knowledge_refs: []
```

硬鎖：

```text
sum(all_events)
!= AFFINITY

frequency
!= preference

money
!= access

access
!= relation
```

---

# DE｜BUSINESS HEALTH 也必須看多條流

第162回沈二寶的房間是一個很乾淨的多流量負樣本：

```text
沒有人叫局
+
沒有人碰和
+
沒有人吃酒
+
連打茶圍客人也沒有
```

所以：

```yaml
ROOM_BUSINESS_FLOW:
  tea_visit_flow:
  call_flow:
  banquet_flow:
  penghe_flow:
  overnight_flow:
```

可以各自衰退，也可能只衰退其中幾條。

因此：

> **「生意不好」未必只是一個數值下降；可能是特定交易流先消失。**

---

# DF｜SCHEDULE CONTENTION｜真正的瓶頸是時間與可用性

目前多回共同支持：

```text
房內有茶圍客
+
外面有局
+
另一處有人吃酒／碰和
+
堂唱
+
住夜客
```

可以同時爭奪一個人物的時間。

所以：

```yaml
COURTESAN_TIME_ALLOCATION_CANDIDATE:
  current_location:
  current_event_type:
  current_commitment:
  queued_calls:
  room_guests:
  dangchang_assignment:
  banquet_assignment:
  penghe_assignment:
  overnight_commitments:
  travel_time:
  promised_return:
```

這會比：

```text
availability = true/false
```

更接近 Corpus。

---

# DG｜raw-hit 索引（INDEX ONLY）

```yaml
RAW_HIT_INDEX:

  打茶圍:
    hits: 15
    chapters: [14,30,43,60,100,106,113,136,137,142,145,161,162]

  茶圍:
    hits: 35
    chapter_count: 23

  堂唱:
    hits: 5
    chapters: [1,7,19,92]

  叫局:
    hits: 42
    chapter_count: 26

  出局:
    hits: 28
    chapter_count: 21

  局票:
    hits: 39
    chapter_count: 24

  轉局:
    hits: 11
    chapters: [5,7,12,17,36,40,46,147]

  吃酒:
    hits: 126
    chapter_count: 65

  花酒:
    hits: 28
    chapter_count: 16

  碰和:
    hits: 105
    chapter_count: 36

  住夜:
    hits: 35
    chapter_count: 22
```

注意：

- `吃酒` 是普通語彙，raw hit 不等於全部都是風月交易；
- `茶圍` 在不同城市的價格與制度不同；
- `堂唱` 已證明存在語義分型；
- `叫局／出局／局票／轉局` 必須放在同一事件生命週期看，不能只統計詞頻。

---

# DH｜本輪形成的新硬結論候選

```text
CLIENT FLOW
is multi-channel

TEA VISIT
is not a relationship tier

CALL REQUEST
is not OUTCALL

OUTCALL
has lifecycle and queue

CALL VOLUME
depends on local market structure

DANGCHANG
competes for schedule

BANQUET
contains multiple call relations

PENGHE GAME MONEY
!= HOUSE PENGHE FEE

OVERNIGHT
is an independent access event

MARKET HISTORY
may create expectation
but not entitlement

HOUSE-ASSIGNED SERVICE
!= CLIENT-NAMED CALL

COURTESAN PRESENCE
requires arrival provenance

BUSINESS DECLINE
may be channel-specific

AVAILABILITY
is a time-allocation problem
```

---

# DI｜下一輪抽取優先

1. 抽 `紅倌人`：
   - 怎麼形成；
   - 怎麼維持；
   - 怎麼退紅；
   - 與聲價、花榜、客流、局量是否等價。
2. 對 V0.1–V0.10 開始第一輪 `CROSS-CHECK / COUNTEREXAMPLE PASS`。
3. 建 `PRICE / FEE SOURCE-CONFLICT INDEX`，集中列出同詞不同章回價目衝突。
4. 抽 `CITY TRANSITION`：
   - 人物跨上海／蘇州／天津時，
   - 哪些個人歷史帶走，
   - 哪些市場資格重新計算。
5. 將 CLIENT FLOW 與 `KNOWLEDGE_EDGE` 接起來：
   - 誰看見誰來過；
   - 誰知道誰叫過局；
   - 誰只聽說；
   - 哪些事件會成為公開面子。
---

# DJ｜RED-COURTESAN STATUS FAMILY｜「紅倌人」不是一個 fame 數值

> 本節承接 V0.7 `REPUTATION / DEMAND GRAPH` 與 V0.10 `CLIENT FLOW EVENT FAMILY`。  
> 目標：抽出《九尾龜》中「紅倌人／名妓／聲價／名氣／花榜／生意」的關係，但不先把它們壓成單一 `reputation_score`。

目前最安全的總結：

```text
RED STATUS
!= BEAUTY

RED STATUS
!= TALENT

RED STATUS
!= MEDIA RANK

RED STATUS
!= CLIENT FLOW

RED STATUS
!= INCOME

RED STATUS
!= RELATION QUALIFICATION

RED STATUS
!= PERMANENT IDENTITY
```

比較接近：

```text
PUBLIC RECOGNITION
+ MARKET VISIBILITY
+ REPEATED CLIENT FLOW
+ SOCIAL TALK
+ QUALIFICATION / TENURE
+ SOCIAL PERFORMANCE
+ MEDIA SIGNAL
+ CITY / TIME CONTEXT
→ 形成某段時間、某城市內的「紅」狀態
```

但目前仍只作 Corpus-derived model candidate。

---

# DK｜紅倌人是 PUBLIC MARKET STATUS，不是私人關係

## DK-001｜第15回：紅倌人的轎子本身具有公共象徵性

金漢良借金小寶轎子：

```text
想讓馬路上的人看見
→ 自己坐的是「紅倌人的轎子」
→ 旁人便會推想他與該倌人有交情
→ 用來出風頭
```

因此：

```yaml
PUBLIC_SYMBOL:
  object: "紅倌人轎子"
  effect:
    - "PUBLIC ASSOCIATION"
    - "BORROWED FACE"
    - "STATUS SIGNAL"
```

但：

```text
BORROWED PUBLIC SIGNAL
!= ACTUAL RELATION
```

這是與 V0.6 `KNOWLEDGE / BELIEF` 很好的接口：
路人可以形成推測，但不是知道真實關係。

---

## DK-002｜第15回：人們會專門去「看紅倌人」

貢春樹提出：

```text
到有名的紅倌人處
→ 多打幾個茶圍
→ 「見識見識」
```

因此：

```text
RED STATUS
can generate DISCOVERY TRAFFIC
```

也就是：

```text
PUBLIC FAME
→ CURIOSITY
→ TEA_VISIT / CALL OPPORTUNITY
```

但這只是 demand funnel，不能反過來把每次茶圍算成關係進度。

---

# DL｜「紅」存在程度語言，但目前不是正式等級制

## DL-001｜第35回：「半紅半黑」

陳海秋羞辱花筱舫時稱：

```text
「你這樣半紅半黑的倌人」
```

此句證明語言上可以把「紅」說成程度。

但 source type 是：

```yaml
EVIDENCE:
  type: "CHARACTER_INSULT / CHARACTER_LABEL"
  speaker: "陳海秋"
  context: "公開衝突／羞辱"
```

因此不能直接建立：

```yaml
RED_TIER:
  BLACK: 0
  HALF_RED: 50
  RED: 100
```

最安全結論：

> **市場參與者會用程度性的「紅／不紅」語言做社會評價，但正式分級規則尚未得到 Corpus 證明。**

---

# DM｜RED STATUS 與 STYLE / 時髦氣派也不可等號

## DM-001｜第8回陳文仙

敘事稱陳文仙：

```text
氣息沉靜
像閨閣大家
「並無紅倌人的一種時髦氣派」
```

這裡有一個重要區分：

```text
RED-COURTESAN STEREOTYPE / PUBLIC STYLE
!= INDIVIDUAL CHARACTER EXPRESSION
```

也就是即使市場上存在「紅倌人應有某種時髦氣派」的想像，
人物實際人格、表達與生活方式仍可不同。

這與：

```text
PERFORMANCE_IS_NOT_PRIVATE_REALITY
PRIVATE_STATE_IS_NOT_SPEECH
```

在結構上相容，但本條來源仍是《九尾龜》自己的敘事描述，不借外部 Runtime 反向證成。

---

# DN｜聲價「出於眾口」：紅是網絡產物

## DN-001｜第15回

正文對上海倌人聲價的討論：

```text
「名妓平章，出於眾口」
```

並描述：

```text
相貌好的紅倌人
→ 有目共賞
→ 眾口交稱
→ 聲價上升
```

同一段又提出反例：

```text
相貌平常
+
酬應無可取
→ 仍可能走運
→ 「無緣無故的紅起來」
→ 有人再把她當名妓巴結
```

因此：

```text
OBSERVED QUALITY
may contribute to REPUTATION

but

REPUTATION
can also become SELF-REINFORCING
```

候選鏈：

```text
INITIAL TALK / SIGNAL
→ MORE ATTENTION
→ MORE CONTACT
→ MORE PUBLIC TALK
→ MORE STATUS
```

---

## DN-002｜「自抬聲價」存在，但不能自我宣告即成功

第15回明見：

```text
自抬聲價
```

這表示人物／房間可以主動進行 reputation management。

但正文同時強調「眾口」與他人接受。

因此：

```text
SELF-PROMOTION
!= SUCCESSFUL PUBLIC REPUTATION
```

必須經過外部傳播／接受。

---

# DO｜資格、應酬、色藝：不同 input，不是一個 QUALITY

## DO-001｜第16回章秋谷的模型

章秋谷主張：

```text
第一講資格
第二講應酬
色藝反而未必居首
```

並說：

```text
資格熬煉年深月久
→ 聲價會高

應酬學得圓到隨和
→ 生意會好
```

必須標：

```yaml
EVIDENCE:
  type: "CHARACTER_ARGUMENT / SOCIAL THEORY"
  speaker: "章秋谷"
  status: "IMPORTANT BUT NOT WORLD AXIOM"
```

因為這是人物評論，不可偷升成 Runtime 公式。

---

## DO-002｜金小寶提供了事件歷史上的旁證

第16回金小寶自述：

```text
剛出來時
→ 不懂應酬
→ 生意沒有
→ 節上十分窘迫

過幾年
→ 生意慢慢變好
→ 名氣慢慢出來
→ 大家才知道金小寶這個名字
```

並強調：

```text
人還是同一個人
不是換了一張臉
```

因此：

> **同一人物的市場狀態可以隨時間、閱歷、應酬與網絡累積變化，而非由靜態外貌決定。**

這是 `RED STATUS` 必須有時間軸的強證據。

---

# DP｜「紅」與 CLIENT FLOW 相關，但不能互相定義

## DP-001｜第144回：上海紅倌人可有極高叫局吞吐量

正文比較：

```text
上海紅倌人
→ 一夜可出五六十個局

天津頭等名角
→ 一夜最多六七八個局
```

但第144回同時明說差異來自：

```text
價格
賒帳
局的停留時間
告假／離席制度
當地規矩
```

所以：

```text
HIGH CALL VOLUME
may be a manifestation of red status

but

CALL VOLUME
is structurally constrained by local market rules
```

因此禁止：

```text
red_score = call_count
```

---

## DP-002｜紅也不等於所有 Flow 都旺

第162回沈二寶：

```text
本來是狠有名氣的紅倌人
+
以前生意十分發達
```

後來：

```text
一班客人因其長期姘戲子的市場形象而絕腳
→ 沒人叫局
→ 沒人碰和
→ 沒人吃酒
→ 沒茶圍客
→ 房間現金流崩潰
```

所以：

> **RED HISTORY 可以存在，而 CURRENT CLIENT FLOW 可以全面崩落。**

需要分：

```yaml
REPUTATION_STATE:
  historical_peak:
  current_public_recognition:
  current_client_flow:
  current_business_health:
```

---

# DQ｜RED STATUS 有生命週期

## DQ-001｜第145回陸月卿／月芳

正文：

```text
十年前狠有些名氣
→ 車馬常盈

過了幾年
→ 不知怎麼忽然門前冷落
→ 上海立不住
→ 到天津再做
→ 天津也不很熱鬧
```

因此：

```text
PAST FAME
!= CURRENT DEMAND

CITY MOVE
!= AUTOMATIC RECOVERY
```

---

## DQ-002｜第172回曹夢蘭／賽金花

正文給出一條非常完整的 lifecycle：

```text
上海重做生意
→ 車馬如雲
→ 因「狀元夫人」身分與既有色藝，聲名大燥

過幾年
→ 年紀漸長
→ 生意漸退

轉天津
→ 改名賽金花
→ 香名大噪
→ 又累積資本

再到北京
→ 開堂子
→ 身分轉為本家
```

這一條同時證明：

```text
REPUTATION
is CITY-SCOPED

BUSINESS STATUS
is TIME-SCOPED

PERSONAL HISTORY
can travel with the character

LOCAL MARKET POSITION
must be recalculated
```

---

## DQ-003｜第29回朱桂寶：極端的繁華→衰退

章秋谷敘述一個前代案例：

```text
二十年前花榜狀元
→ 大名鼎鼎
→ 纏頭千萬
→ 車馬如雲
→ 多人爭娶

不多幾年
→ 年紀大
→ 無人過問
→ 極度貧困
```

source type：

```yaml
EVIDENCE:
  type: "CHARACTER-HISTORICAL-ACCOUNT"
  speaker: "章秋谷"
  status: "SECONDARY WITHIN FICTION"
```

不可把他對原因的全部解釋當統計定律，
但「市場高峰不是永久身份」非常清楚。

---

# DR｜CITY RECOMPUTATION｜上海不紅，天津可以突然大紅

## DR-001｜第30回陸畹香

正文：

```text
上海生意不好
→ 到天津

剛到天津
→ 名聲大震
→ 各堂子老闆重金羅致
→ 天天冠蓋如雲
→ 生意與上海大不相同
```

而正文給出的可觀察個人條件包括：

```text
年輕
品貌好
多種唱藝
琵琶
應酬
```

但不能推出：

```text
這些條件在任何城市必然成功
```

真正支持的是：

> **城市市場會重算人物的 market fit。**

候選：

```yaml
LOCAL_MARKET_POSITION:
  character_id:
  city:
  period:
  prior_external_reputation:
  local_network_reception:
  local_client_flow:
  venue_demand:
```

---

# DS｜花榜是 Reputation Signal，不是 Reputation Truth

## DS-001｜第91回薛金蓮：MEDIA SIGNAL → REAL DEMAND

起點：

```text
生意清淡
→ 面子過不去
```

操作：

```text
給報館主筆錢
→ 被取為花榜狀元
```

市場反應：

```text
原本大家不認識
→ 因榜單感到詫異
→ 你也叫、他也叫
→ 新客實際接觸
→ 客人重新詮釋她的缺點
→ 一傳十、十傳百
→ 市場地位被真正抬高
```

因此：

```text
FALSE / PAID INITIAL SIGNAL
can produce
REAL CLIENT FLOW
```

但：

```text
REAL CLIENT FLOW
does not retroactively make
the original ranking independent
```

---

## DS-002｜第183回：榜單本身有信用週期

敘事比較：

早期：

```text
花榜仍考察
色藝
資格
品行
→ 榜首「著實有些聲價」
```

後期：

```text
報館收賄
→ 名次有價
→ 甚至半年多次開榜
→ 榜單氾濫
→ 花榜上的人還有什麼聲價？
```

所以：

```yaml
MEDIA_SIGNAL:
  reach:
  credibility:
  corruption_level:
  frequency:
  audience_attention:
  market_conversion:
```

硬鎖：

```text
MEDIA REACH
!= MEDIA CREDIBILITY

MEDIA RANK
!= MARKET TRUTH
```

---

## DS-003｜第183回同時說明：倌人把花榜當投資

人物／敘事所描寫的市場計算：

```text
花錢取得名次
→ 名氣可能更響
→ 生意可能更大
→ 希望把投入收回
```

因此：

```yaml
REPUTATION_INVESTMENT:
  cash_outlay:
  expected_visibility_gain:
  expected_demand_gain:
  expected_recovery:
  realized_result:
```

這與 V0.7 的 Reputation→Demand→Ledger feedback loop 正式閉合。

---

# DT｜花榜排名、名妓、紅倌人、金剛：不可合成一個 Rank

目前 Corpus 至少同時存在：

```text
紅倌人
名妓
花榜狀元／榜眼／探花
金剛
有名人物
有名的時髦倌人
```

第155–156回又明確存在人物自行品評花榜的場景，
第183回則說歷史上有前四／中四／後四金剛等媒體提倡名目。

因此：

```text
PUBLIC_LABEL_A
!= PUBLIC_LABEL_B
```

目前不能建立：

```text
野雞 < 么二 < 長三 < 紅倌人 < 金剛 < 花榜狀元
```

因為這把：

```text
VENUE / BUSINESS CLASS
PUBLIC FAME
MEDIA RANK
SOCIAL LABEL
```

混成一條梯子。

---

# DU｜紅倌人的「面子成本」

## DU-001｜第9回陸蘭芬

章秋谷說：

```text
沒有什麼名氣的人
→ 不撐場面，反較容易支持

有了名氣的人
→ 要「撐這個外場」
→ 生意即使鬧忙，也有另一種壓力
```

source type：

```yaml
EVIDENCE:
  type: "CHARACTER_ARGUMENT"
  speaker: "章秋谷"
```

但它與多回 `繃場面`、轎子、衣飾、酒局的實際事件互相呼應。

候選概念：

```yaml
PUBLIC_FACE_MAINTENANCE:
  visible_transport:
  dress_and_jewelry:
  banquet_activity:
  penghe_activity:
  public_client_presence:
  media_presence:
  room_liveliness:
```

---

## DU-002｜「繃場面」證明客流本身可被人為支撐

第8、22、91、149回等：

```text
客人主動吃酒／碰和
→ 目的之一是替倌人「繃場面」
```

這表示：

```text
VISIBLE BUSINESS ACTIVITY
may be partially subsidized / staged
```

所以：

```text
BUSY-LOOKING ROOM
!= ORGANIC DEMAND
```

未來如要模擬 `public_face`，必須能標記：

```yaml
CLIENT_FLOW_EVENT:
  organic_demand:
  relationship_support:
  deliberate_face_support:
  media_stimulated:
```

但這仍是候選欄位，等待更多 cross-check。

---

# DV｜「紅」可以反過來影響他人對同一行為的解讀

第91回薛金蓮：

```text
榜單前：
不會應酬／不能唱曲

榜單後的客人：
不說她不會應酬
→ 說有大家風範

不說不能唱
→ 說有閨閣嬌羞
```

所以：

> **Reputation 不只改變「誰來」，還可能改變「來的人怎麼解讀同一表現」。**

候選：

```yaml
PERCEPTION_BIAS:
  prior_reputation_signal:
  observed_behavior:
  observer_interpretation:
  later_rumor:
```

這不能寫成角色被洗腦；
只是不同觀察者在既有先驗下形成不同評價。

---

# DW｜CLIENT REPUTATION 與 COURTESAN RED STATUS 必須平行

V0.7 已抽出：

```text
有名富戶
闊客
有功架客人
有名氣的客人
```

本輪再確認：

```text
紅倌人具有公共市場地位
```

所以最好是兩張平行的 reputation graph：

```yaml
MARKET_REPUTATION_GRAPH:

  client_side:
    - spending_reputation
    - payment_reputation
    - social_skill_reputation
    - wealth_reputation
    - face_reputation

  courtesan_side:
    - public_fame
    - media_labels
    - client_flow_visibility
    - qualification_tenure
    - performance_reputation
    - business_momentum
```

但兩邊都不能直接決定私人關係。

---

# DX｜第一版 RED STATUS STATE 候選

```yaml
RED_STATUS_STATE:
  character_id:

  scope:
    city:
    district:
    venue:
    period:

  public_recognition:
    known_name:
    talk_intensity:
    public_labels: []

  media:
    rankings: []
    label_sources: []
    source_credibility:
    paid_promotion_history: []

  market_visibility:
    tea_visit_flow:
    call_request_flow:
    outcall_flow:
    banquet_flow:
    penghe_flow:
    overnight_flow:

  business:
    receivables:
    realized_cash:
    room_business_health:
    current_momentum:

  social_capital:
    qualification_history:
    client_network:
    peer_network:
    venue_owner_interest:
    public_face:

  performance_reputation:
    social_service:
    arts:
    appearance:
    fashion_style:

  lifecycle:
    prior_peak_periods: []
    decline_periods: []
    revival_periods: []
    city_transitions: []

  epistemic:
    observer_beliefs: []
    rumor_refs: []
    evidence_refs: []
```

注意：

```text
這不是 final Runtime schema。
```

它只是目前 Corpus 強迫我們保留的分軸集合。

---

# DY｜第一版 RED LIFECYCLE

目前可觀察：

```text
UNKNOWN / LOW VISIBILITY

→ DISCOVERED
   ├─ organic discovery
   ├─ venue introduction
   ├─ client talk
   ├─ media signal
   └─ external prior fame

→ GROWING
   ├─ more tea visits
   ├─ more calls
   ├─ more visible banquets/penghe
   ├─ more public talk
   └─ venue-owner interest

→ HIGH PUBLIC STATUS
   ├─ high visibility
   ├─ symbolic status goods
   ├─ high scheduling load
   └─ face-maintenance pressure

→ DECLINE
   ├─ age / lifecycle
   ├─ client withdrawal
   ├─ scandal / reputation damage
   ├─ city market shift
   ├─ macro market decline
   └─ other unresolved causes

→ POSSIBLE:
   ├─ CITY MOVE
   ├─ REBRANDING / NAME CHANGE
   ├─ REVIVAL
   ├─ ROLE TRANSITION
   └─ EXIT
```

但每個箭頭都不能自動發生。

---

# DZ｜MACRO MARKET CAN DRAG EVERYONE DOWN

第183回不是單一人物退紅，而是：

```text
上海時勢變遷
→ 市面一天衰敗似一天
→ 堂子生意一天寥落似一天
→ 老的老、嫁的嫁、死的死
→ 整個舊風月明星系統更替
```

因此：

```text
CHARACTER REPUTATION
cannot be modeled independently from
MARKET REGIME
```

候選：

```yaml
MARKET_REGIME:
  city:
  period:
  overall_client_demand:
  media_ecology:
  venue_health:
  public_spending:
  entertainment_competition:
```

---

# EA｜raw-hit 索引（INDEX ONLY）

```yaml
RAW_HIT_INDEX:

  紅倌人:
    hits: 34
    chapters: [8,13,15,31,33,35,36,38,40,46,66,68,72,92,97,135,143,144,158,159,162,164,165]

  半紅半黑:
    hits: 1
    chapters: [35]

  聲價:
    hits: 11
    chapters: [9,15,16,169,183]

  名妓:
    hits: 49
    chapter_count: 29

  名氣:
    hits: 49
    chapter_count: 38

  花榜狀元:
    hits: 3
    chapters: [91,183]

  自抬聲價:
    hits: 1
    chapters: [15]

  繃場面:
    hits: 5
    chapters: [8,22,68,91,149]

  生意清淡:
    hits: 2
    chapters: [31,91]

  車馬常盈:
    hits: 1
    chapters: [145]

  冠蓋如雲:
    hits: 2
    chapters: [30,174]

  "上海紅倌人一夜五六十個局":
    anchor: 144
```

注意：

- `紅起來` raw substring 有大量「臉紅」誤撞，不可直接作市場詞頻；
- `紅倌人` 本身也可能出現在人物辱罵、比較、回目或敘事標籤中；
- 所有 hit 仍需 evidence type；
- `名妓／名氣／聲價` 也大量出現在非堂子語境，必須逐回判讀。

---

# EB｜本輪形成的新硬結論候選

```text
RED STATUS
is PUBLIC / MARKET-SCOPED

RED STATUS
is TIME-SCOPED

RED STATUS
is CITY-SCOPED

RED STATUS
has a lifecycle

PAST FAME
!= CURRENT DEMAND

MEDIA RANK
!= REPUTATION TRUTH

PAID MEDIA SIGNAL
may create REAL DEMAND

HIGH CALL VOLUME
!= DEFINITION OF RED

BEAUTY
!= RED

TALENT
!= RED

TENURE / QUALIFICATION
may matter
but is not sole cause

SOCIAL PERFORMANCE
may matter
but is not sole cause

PUBLIC FACE
can be deliberately supported

BUSY-LOOKING ROOM
!= ORGANIC DEMAND

REPUTATION
can alter observer interpretation

MACRO MARKET
can overpower individual status
```

---

# EC｜Stage 1 CROSS-CHECK 開始具備條件

到 V0.11 為止，已抽出：

```text
RELATION
HOUSEHOLD / ROOM
LIFECYCLE
LEDGER
KNOWLEDGE
REPUTATION
CREDIT
CITY / VENUE
CLIENT FLOW
RED STATUS
```

現在第一次具備條件做真正的：

```text
CROSS-CHECK / COUNTEREXAMPLE PASS
```

下一輪不再單純增加新模組，而先專門攻擊 V0.1–V0.11：

1. 找「花很多錢但不是恩客／相好」反例；
2. 找「高名氣但生意差」反例；
3. 找「生意好但非紅倌人」反例；
4. 找「熟客但被怠慢／生客反而優先」反例；
5. 找「有局票但不出局」反例；
6. 找「同詞不同城市制度」反例；
7. 找「同一人物跨城重新定價」反例；
8. 找「帳面收入高但現金流危機」反例；
9. 找「公開標籤與本人／對方否認」反例；
10. 建立第一版 `SOURCE_CONFLICT / COUNTEREVIDENCE INDEX`。

若某條候選規則經不起反例，下一版應降級或刪除，而不是替它補故事。
---

# ED｜CROSS-CHECK / COUNTEREXAMPLE PASS 001
# 第一輪反例攻擊：不新增世界，只攻擊既有候選規則

> V0.12 不以「再多抽一個模組」為目標。  
> 本輪專門回頭測試 V0.1–V0.11 已形成的候選結構，尋找：
>
> - 明確反例；
> - 人物主張與事件事實衝突；
> - 同詞跨城市／跨時段規則不一致；
> - 表面指標與底層狀態脫鉤；
> - 只能支持「傾向」，不能支持「必然」的地方。
>
> 若候選規則被打穿，處理方式是：
>
> ```text
> DOWNGRADE
> SPLIT
> CONTEST
> UNKNOWN
> ```
>
> 而不是替它補一段故事把它救回來。

---

# EE｜VERDICT ENUM｜本輪判定用語

```yaml
CROSS_CHECK_VERDICT:

  SURVIVES:
    meaning:
      - "本輪反例沒有打穿，且存在多個獨立事件支持。"
      - "仍不代表已成 final Runtime law。"

  STRENGTHENED_AS_SEPARATION:
    meaning:
      - "原本的 != 分軸，在反例中得到更強支持。"

  FALSIFIED_AS_UNIVERSAL:
    meaning:
      - "若把候選寫成普遍必然規則，已被正文直接反例推翻。"

  PROVISIONAL_COUNTEREXAMPLE:
    meaning:
      - "有很強的反向材料，但證據類型／時間作用域不足以完成硬否定。"

  SOURCE_CONFLICT:
    meaning:
      - "正文不同位置對同一條件給出彼此不相容的資訊。"

  SEMANTIC_SPLIT_REQUIRED:
    meaning:
      - "同一詞至少存在不同使用方式，不能壓成單一制度定義。"

  UNRESOLVED:
    meaning:
      - "目前仍缺足夠證據決定。"
```

---

# EF｜CEX-001｜花很多錢 ≠ 住夜資格

## EF-001｜第36回：短期密集花費仍不留夜

陳海秋：

```text
初到上海
→ 叫三四個局
→ 想住夜
→ 被娘姨告知長三通常要先有碰和／吃酒等往來

於是：
→ 擺花酒
→ 碰和
→ 再吃酒

陳海秋自認：
→ 這樣應該會被留夜

實際：
→ 花筱舫仍不留
→ 應酬也沒有因此變得十分巴結
```

判定：

```yaml
COUNTEREXAMPLE:
  id: "CEX-001"
  target_rule: "SPENDING / BANQUET / PENGHE HISTORY -> OVERNIGHT"
  verdict: "FALSIFIED_AS_UNIVERSAL"
  chapter: 36
```

硬鎖升級：

```text
MARKET HISTORY
may be socially relevant

but

MARKET HISTORY
does not create OVERNIGHT ENTITLEMENT
```

---

## EF-002｜第92回：長期大量花費仍不形成住夜

陳海秋已是范彩霞：

```text
用錢最多的客人
+
報效許多和酒
+
延續數月
```

實際：

```text
范彩霞仍不讓他近身
+
從不主動表示留他住夜
```

這不是單一事件偶然失敗，而是：

```text
LONGER HORIZON
+
HIGHER SPENDING
+
REPEATED MARKET EVENTS
```

仍然不能生成 access。

判定：

```yaml
COUNTEREXAMPLE:
  id: "CEX-002"
  target_rule: "HIGH SPENDING -> OVERNIGHT ACCESS"
  verdict: "FALSIFIED_AS_UNIVERSAL"
  chapter: 92
```

---

# EG｜CEX-003｜花很多錢 ≠ 相好

第101回陳海秋自己列帳：

```text
認識將近一年
+
酒不知吃多少次
+
和不知碰多少場
+
總支出約二三千
```

但他同時抱怨：

```text
范彩霞仍愛理不理
+
連好好應酬都沒有
+
住夜沒有
+
甚至「攀個相好」都未成立
```

最重要的是：

> 這一段是**陳海秋自己的權利感主張**，不是敘事者替他認證。

因此：

```yaml
COUNTEREXAMPLE:
  id: "CEX-003"
  target_rule: "HIGH SPENDING -> XIANGHAO"
  verdict: "FALSIFIED_AS_UNIVERSAL"
  chapter: 101
```

並得到：

```text
SPENDING
may create
EXPECTATION / RESENTMENT / LEVERAGE ATTEMPT

but

SPENDING
does not create
XIANGHAO STATUS
```

---

# EH｜CEX-004｜叫局早到 ≠ 恩客

第36回金漢良：

```text
金小寶常在他的局先到
→ 金漢良自行解讀：
   「把我當恩客」
```

金小寶立即否認：

```text
只是有轉局／無轉局造成早晚不同
→ 早一點來不等於恩客
```

因此：

```yaml
COUNTEREXAMPLE:
  id: "CEX-004"
  target_rule:
    - "FAST ARRIVAL -> ENKE"
    - "FREQUENT CALL -> ENKE"
  verdict: "FALSIFIED_AS_UNIVERSAL"
  chapter: 36
  evidence_structure:
    claim: "CLIENT_SELF_CLAIM"
    rebuttal: "COUNTERPARTY_EXPLICIT_DENIAL"
```

這是目前 Corpus 最乾淨的：

```text
CLAIMED_ENKE_STATUS
!= COUNTERPARTY_ACKNOWLEDGED_ENKE_STATUS
```

---

# EI｜CEX-005｜熟客 ≠ 當下服務優先

第33回花筱舫：

```text
章秋谷：
→ 今日第一轉
→ 生客

辛修甫／陳海秋：
→ 日日來
→ 熟客
```

花筱舫明說：

```text
先應酬生客
→ 再慢慢應酬熟客
```

因此：

```yaml
COUNTEREXAMPLE:
  id: "CEX-005"
  target_rule: "REGULAR / FAMILIAR CLIENT -> SERVICE PRIORITY"
  verdict: "FALSIFIED_AS_UNIVERSAL"
  chapter: 33
```

新硬鎖：

```text
熟客
is a relationship / market-history qualification

熟客
is not a universal queue priority
```

也就是：

```text
RELATION STATUS
!= SCHEDULING PRIORITY
```

---

# EJ｜CEX-006｜「熟客叫局必來」只是人物市場認知

第34回章秋谷說：

```text
「上海地方，熟客叫局那有不來之理？」
```

如果把此句升成世界公理：

```text
REGULAR CLIENT CALL
→ GUARANTEED ARRIVAL
```

就會與正文實際事件衝突。

第22回林黛玉：

```text
一席收到二十餘張局票
→ 多數回報轉局
→ 自己繼續留在目前席面
```

第73回張書玉：

```text
已有局票
+
院中連續派人催
+
另一批客人在房內等
→ 她仍不急著走
```

因此：

```yaml
COUNTEREXAMPLE:
  id: "CEX-006"
  target_rule: "REGULAR CLIENT CALL -> GUARANTEED OUTCALL"
  verdict: "FALSIFIED_AS_UNIVERSAL"
  claim_source:
    chapter: 34
    evidence_type: "CHARACTER_CLAIM"
  counter_events:
    chapters: [22,73]
```

保留的不是「熟客局沒有意義」；而是：

```text
熟客身份
may affect EXPECTED RESPONSE

but

does not cancel
CHARACTER DECISION
SCHEDULE
CURRENT ENGAGEMENT
CALL QUEUE
```

---

# EK｜CEX-007｜局票 ≠ 出局

V0.10 已拆出 `CALL_REQUEST` 與 `OUTCALL`。

本輪 cross-check 後可升級成更強的事件不變量：

```text
局票被寫
!= 局票送達

局票送達
!= 接受

接受
!= 立即離開

離開
!= 到場

到場
!= 完成
```

第22、73回均為正文事件級反例。

判定：

```yaml
COUNTEREXAMPLE:
  id: "CEX-007"
  target_rule: "CALL TICKET -> OUTCALL COMPLETION"
  verdict: "FALSIFIED_AS_UNIVERSAL"
  chapters: [22,73]
```

因此 `CALL_LIFECYCLE` 從候選提升為強結構：

```yaml
CALL_LIFECYCLE:
  REQUEST_CREATED:
  REQUEST_DELIVERED:
  ACCEPTED:
  DECLINED:
  DEFERRED:
  DEPARTED:
  ARRIVED:
  SERVING:
  COMPLETED:
```

欄位名稱仍可再改，但階段分離不能再合回一格。

---

# EL｜CEX-008｜高名氣／紅歷史 ≠ 當前生意

第162回沈二寶：

```text
前兩年：
→ 生意十分發達

人物／敘事背景：
→ 是有名氣的紅倌人

後來：
→ 一班客人知道她長期姘戲子
→ 一個個絕腳

當下：
→ 沒人叫局
→ 沒人碰和
→ 沒人吃酒
→ 沒打茶圍客
```

因此：

```yaml
COUNTEREXAMPLE:
  id: "CEX-008"
  target_rule: "HIGH FAME / RED HISTORY -> CURRENT HIGH DEMAND"
  verdict: "FALSIFIED_AS_UNIVERSAL"
  chapter: 162
```

V0.7 / V0.11 的分離得到強化：

```text
REPUTATION
!= CURRENT DEMAND

PAST RED STATUS
!= CURRENT BUSINESS HEALTH
```

判定：

```text
STRENGTHENED_AS_SEPARATION
```

---

# EM｜CEX-009｜生意表面好 ≠ 紅倌人

這一條證據沒有前幾條乾淨，所以只做 provisional。

第130回陸韻仙自述：

```text
「看看面子浪生意蠻好」
```

但她接著說：

```text
到節上／年底一算
→ 總歸不靈
→ 仍缺大筆開銷
```

第135回章秋谷又對她房間的人說：

```text
陸韻仙「算不得什麼有名的紅倌人」
```

這可以構成：

```text
VISIBLE / APPARENT BUSINESS
without
ACKNOWLEDGED HIGH RED STATUS
```

但注意：

- 第130回是陸韻仙自述；
- 第135回是章秋谷評價；
- 兩者不是完全相同時點；
- 「算不得有名的紅倌人」仍是人物判斷。

因此：

```yaml
COUNTEREXAMPLE:
  id: "CEX-009"
  target_rule: "GOOD-LOOKING BUSINESS FLOW -> RED COURTESAN"
  verdict: "PROVISIONAL_COUNTEREXAMPLE"
  chapters: [130,135]
```

目前只能鎖：

```text
VISIBLE BUSINESS
does not prove
RED STATUS
```

不能反向宣布：

```text
陸韻仙 = 非紅倌人
```

為確定世界事實。

---

# EN｜CEX-010｜跨城後，原市場結果不保證延續

## EN-001｜陸畹香

第30回：

```text
上海：
→ 生意不好

天津：
→ 剛到即名聲大震
→ 各堂子老闆重金羅致
→ 天天冠蓋如雲
```

同一人物、短時間內：

```text
SHANGHAI RESULT
!= TIANJIN RESULT
```

判定：

```yaml
COUNTEREXAMPLE:
  id: "CEX-010A"
  target_rule: "CHARACTER MARKET VALUE IS GLOBAL"
  verdict: "FALSIFIED_AS_UNIVERSAL"
  chapter: 30
```

---

## EN-002｜陸月卿／月芳

第145回：

```text
上海十年前：
→ 有名氣
→ 車馬常盈

之後：
→ 門前冷落
→ 上海立不住

天津：
→ 做了幾年
→ 也不甚熱鬧
```

所以跨城不是：

```text
MOVE_CITY
→ RESET_TO_HIGH_DEMAND
```

判定：

```yaml
COUNTEREXAMPLE:
  id: "CEX-010B"
  target_rule: "CITY MOVE -> AUTOMATIC REPUTATION RECOVERY"
  verdict: "FALSIFIED_AS_UNIVERSAL"
  chapter: 145
```

保留：

```text
PERSONAL HISTORY
travels

LOCAL MARKET POSITION
recomputes
```

---

# EO｜CEX-011｜帳面「生意好」 ≠ 現金足夠

第130回陸韻仙：

```text
表面：
→ 生意蠻好

年底：
→ 算起來仍不靈
→ 還缺約一千洋鈿
→ 需要借款
```

因此：

```yaml
COUNTEREXAMPLE:
  id: "CEX-011"
  target_rule: "VISIBLE BUSINESS / GROSS ACTIVITY -> CASH SUFFICIENCY"
  verdict: "FALSIFIED_AS_UNIVERSAL"
  chapter: 130
```

V0.5 的 Ledger 分離得到強化：

```text
TRANSACTION ACTIVITY
!= REALIZED CASH

RECEIVABLE
!= CASH

BUSINESS APPEARANCE
!= LIQUIDITY
```

---

# EP｜CEX-012｜收入歷史 ≠ 免除現金流危機

第162回沈二寶：

```text
前兩年：
→ 生意十分發達

後來：
→ 客流消失
→ 生活方式與支出未立即下降
→ 欠下三千餘債務
→ 房飯／菜錢／店帳集中催逼
```

因此：

```yaml
COUNTEREXAMPLE:
  id: "CEX-012"
  target_rule: "PRIOR HIGH INCOME -> CURRENT SOLVENCY"
  verdict: "FALSIFIED_AS_UNIVERSAL"
  chapter: 162
```

硬鎖：

```text
PAST INCOME
!= CURRENT CASH

PAST REPUTATION
!= CURRENT CREDIT CAPACITY

HIGH-LIFESTYLE RESIDUE
can outlive
HIGH CLIENT FLOW
```

---

# EQ｜CEX-013｜公開相好標籤 ≠ 已成立相好

第1回章秋谷與許寶琴：

```text
今日第一次接觸
+
第一次到房
```

朋友方小松見兩人神態親熱，就直接拿「相好／老相好」來取笑。

房間人員則明確說：

```text
章秋谷確是今日才「做起」
```

因此：

```yaml
COUNTEREXAMPLE:
  id: "CEX-013"
  target_rule: "PUBLIC / THIRD-PARTY XIANGHAO LABEL -> ACTUAL XIANGHAO STATUS"
  verdict: "FALSIFIED_AS_UNIVERSAL"
  chapter: 1
```

由此正式需要：

```yaml
RELATION_LABEL:
  speaker_claim:
  third_party_attribution:
  counterparty_acknowledgement:
  observed_history:
  public_rumor:
```

`相好` 不能靠自然語言單句直接寫入 canonical relation graph。

---

# ER｜CEX-014｜「恩客」同樣必須有 ACKNOWLEDGEMENT / EVIDENCE

第36回是更強版本：

```text
金漢良：
→ 公開自稱被當恩客

金小寶：
→ 當場否認
```

因此：

```text
SELF-CLAIM
!= RELATION FACT
```

判定：

```yaml
COUNTEREXAMPLE:
  id: "CEX-014"
  target_rule: "SELF-CLAIMED RELATION LABEL -> RELATION FACT"
  verdict: "FALSIFIED_AS_UNIVERSAL"
  chapter: 36
```

這同時強化 V0.6：

```text
BELIEF / CLAIM
!= EVENT / RELATION FACT
```

---

# ES｜SOURCE-CONFLICT-001｜上海碰和價格：20 vs 12

目前最乾淨的原作內部數字衝突：

第1回敘事：

```text
上海碰和一概二十元
蘇州長三／么二均八元
```

第54回敘事：

```text
上海吃酒碰和都是十二元
蘇州正式碰和八元
```

而第54回還自稱：

```text
前面初集已說過
此次只是說得更詳細
```

所以目前不能直接用：

```text
「作者後來改價」
```

把兩者自動和解。

判定：

```yaml
SOURCE_CONFLICT:
  id: "SRC-CONFLICT-001"
  field: "SHANGHAI_PENGHE_PRICE"
  observations:
    - {chapter: 1, amount: 20}
    - {chapter: 54, amount: 12}
  verdict: "SOURCE_CONFLICT"
  resolution: "UNRESOLVED"
```

允許候選解釋：

```text
時間變動
交易細節不同
敘事口徑不同
原作自身不一致
尚有未抽條件
```

但目前沒有任何一條取得 closure。

---

# ET｜SOURCE-CONFLICT-002｜「堂唱已除」≠ 後文完全沒有堂唱

第1回敘事：

```text
以前上海：
→ 生客進門必唱一曲
→ 名為堂唱
→ 現錢開銷

敘事當時：
→ 上海此例已除
→ 蘇州仍未改
```

但第7、19、92回上海事件仍出現：

```text
堂唱
出堂唱
堂唱回來
```

若把第1回讀成：

```text
上海所有堂唱活動已消失
```

就與後文衝突。

目前最安全處理不是 `SOURCE_CONFLICT`，而是：

```yaml
TERM:
  name: "堂唱"
  verdict: "SEMANTIC_SPLIT_REQUIRED"

  subtype_A:
    meaning: "生客進門時的制度性唱曲／付費慣例"
    status_in_shanghai: "NARRATOR SAYS ABOLISHED"

  subtype_B:
    meaning: "後文所稱出堂唱／堂唱差事"
    status_in_shanghai: "ATTESTED"

  exact_relationship_between_subtypes:
    status: "UNRESOLVED"
```

這是第一個明確：

> **用語相同，但不能用一個布林欄位表示。**

---

# EU｜SOURCE-CONFLICT-003｜人物市場口訣 ≠ 世界法則

第34回章秋谷：

```text
「熟客叫局那有不來之理」
```

第22、73回事件：

```text
局票可積壓
可被回報轉局
可被催
人物可繼續留在原席
```

因此：

```yaml
SOURCE_CONFLICT:
  id: "SRC-CONFLICT-003"
  type: "CHARACTER_CLAIM_VS_OBSERVED_EVENT"
  claim_chapter: 34
  event_chapters: [22,73]
  verdict: "CHARACTER_CLAIM_DOWNGRADED"
```

不是說章秋谷「完全錯」：

```text
他的話仍可代表：
→ 上海熟客對出局有較強的正常期待
```

但不能變成：

```text
CALL_ACCEPTANCE = AUTOMATIC
```

---

# EV｜SOURCE-CONFLICT-004｜「生意看起來好」與「年底不靈」

第130回同一人物同一段話中已經自行形成內部拆分：

```text
面子浪生意蠻好
```

同時：

```text
到節上／年底算起來總歸不靈
```

這不是文本錯誤，反而是語義拆分：

```yaml
BUSINESS_SEMANTICS:
  visible_flow:
  gross_activity:
  receivable:
  realized_cash:
  expenses:
  debt_service:
  year_end_liquidity:
```

所以：

```text
「生意好」
cannot be stored as
one boolean
```

---

# EW｜FIRST COUNTEREVIDENCE INDEX

```yaml
COUNTEREVIDENCE_INDEX:

  CEX-001:
    proposition: "花酒／碰和歷史必然導向住夜"
    verdict: "FALSIFIED_AS_UNIVERSAL"
    chapter: 36

  CEX-002:
    proposition: "長期高消費必然導向住夜"
    verdict: "FALSIFIED_AS_UNIVERSAL"
    chapter: 92

  CEX-003:
    proposition: "高消費自然形成相好"
    verdict: "FALSIFIED_AS_UNIVERSAL"
    chapter: 101

  CEX-004:
    proposition: "叫局早到／常叫局形成恩客"
    verdict: "FALSIFIED_AS_UNIVERSAL"
    chapter: 36

  CEX-005:
    proposition: "熟客必然服務優先"
    verdict: "FALSIFIED_AS_UNIVERSAL"
    chapter: 33

  CEX-006:
    proposition: "熟客叫局必然到場"
    verdict: "FALSIFIED_AS_UNIVERSAL"
    chapters: [22,34,73]

  CEX-007:
    proposition: "局票即出局"
    verdict: "FALSIFIED_AS_UNIVERSAL"
    chapters: [22,73]

  CEX-008:
    proposition: "高名氣／紅歷史保證當前高客流"
    verdict: "FALSIFIED_AS_UNIVERSAL"
    chapter: 162

  CEX-009:
    proposition: "表面生意好即可判定紅倌人"
    verdict: "PROVISIONAL_COUNTEREXAMPLE"
    chapters: [130,135]

  CEX-010A:
    proposition: "人物市場價值跨城市保持"
    verdict: "FALSIFIED_AS_UNIVERSAL"
    chapter: 30

  CEX-010B:
    proposition: "跨城可自動恢復舊名氣"
    verdict: "FALSIFIED_AS_UNIVERSAL"
    chapter: 145

  CEX-011:
    proposition: "表面生意好表示現金充足"
    verdict: "FALSIFIED_AS_UNIVERSAL"
    chapter: 130

  CEX-012:
    proposition: "曾經高收入表示現在有償債能力"
    verdict: "FALSIFIED_AS_UNIVERSAL"
    chapter: 162

  CEX-013:
    proposition: "第三人稱相好即可寫成相好事實"
    verdict: "FALSIFIED_AS_UNIVERSAL"
    chapter: 1

  CEX-014:
    proposition: "本人自稱恩客即可寫成恩客事實"
    verdict: "FALSIFIED_AS_UNIVERSAL"
    chapter: 36
```

---

# EX｜PASS 001 後仍站得住的結構

本輪不是把前十一版打掉。

相反，真正經過反例後仍保留的東西更清楚：

```text
MONEY
!= RELATION

PAYMENT
!= ACCESS

ACCESS
!= RELATION

PUBLIC LABEL
!= RELATION FACT

RELATION STATUS
!= SCHEDULING PRIORITY

CALL REQUEST
!= OUTCALL

REPUTATION
!= CURRENT DEMAND

DEMAND
!= CASH

RECEIVABLE
!= CASH

PAST FAME
!= CURRENT MARKET POSITION

CITY
is a first-class market scope

TIME
is a first-class market scope

VISIBLE BUSINESS
!= LIQUIDITY

CHARACTER CLAIM
!= WORLD RULE
```

這些現在不是「設計偏好」而已；
它們已經有正文反例共同支持。

---

# EY｜本輪被降級的舊候選

```yaml
DOWNGRADED_CANDIDATES:

  "熟客通常有較高出局期待":
    old_risk:
      - "容易被寫成 guaranteed arrival"
    new_status:
      - "EXPECTATION ONLY"
      - "NOT SCHEDULING AUTHORITY"

  "市場往來可作住夜前置":
    old_risk:
      - "容易被寫成 progression ladder"
    new_status:
      - "LOCAL SOCIAL EXPECTATION"
      - "NOT ENTITLEMENT"
      - "NOT UNIVERSAL ACROSS CITY"

  "生意好":
    old_risk:
      - "容易做成單值 business_score"
    new_status:
      - "VECTOR / CONTEXTUAL"
      - "VISIBLE FLOW != LIQUIDITY"

  "紅倌人":
    old_risk:
      - "容易做成 fame tier"
    new_status:
      - "PUBLIC MARKET STATUS FAMILY"
      - "CITY/TIME SCOPED"
      - "NOT DEFINED BY ONE FLOW"

  "相好／恩客自然語言標籤":
    old_risk:
      - "對話一出現就直接入 relation graph"
    new_status:
      - "REQUIRES SOURCE TYPE + ACKNOWLEDGEMENT / HISTORY"
```

---

# EZ｜第一版 FACT / CLAIM / LABEL 寫入規則候選

Cross-check 後，relation / market 狀態至少需要先區分：

```yaml
EVIDENCE_WRITE_GATE:

  OBSERVED_EVENT:
    may_update:
      - "event history"
      - "ledger"
      - "call lifecycle"
      - "location / schedule"

  NARRATOR_EXPLICIT_RULE:
    may_support:
      - "scoped market rule"
    must_keep:
      - "chapter"
      - "city/time scope"
      - "possible source conflict"

  CHARACTER_CLAIM:
    may_update:
      - "speaker belief"
      - "public claim"
    must_not_directly_update:
      - "world fact"
      - "relation qualification"

  THIRD_PARTY_LABEL:
    may_update:
      - "rumor / public attribution"
    must_not_directly_update:
      - "counterparty-acknowledged relation"

  COUNTERPARTY_ACKNOWLEDGEMENT:
    may_support:
      - "relation qualification"
    still_requires:
      - "scope"
      - "current validity"
      - "event history when needed"
```

這不是 final SAVE gate；
只是 Corpus 已經證明：

> **同一句「他是我相好／恩客」的證據法位，不會永遠一樣。**

---

# FA｜Stage 1 第一輪反例後的結構圖

```text
CITY / TIME / MARKET REGIME
        ↓
VENUE / HOUSEHOLD / ROOM
        ↓
CHARACTER + ROLE + SCHEDULE
        ↓
CALL / TEA / BANQUET / PENGHE / OVERNIGHT EVENTS
        ↓
LEDGER / RECEIVABLE / CASH
        ↓
PUBLIC VISIBILITY / REPUTATION / CLIENT FLOW
        ↓
CLAIM / RUMOR / LABEL / BELIEF
        ↓
RELATION QUALIFICATION
```

但箭頭不是單向自動升級。

真正應讀成：

```text
每一層都可以互相影響
但沒有一層可以
「憑自己」
直接替另一層建立事實。
```

這是 V0.12 反例攻擊後最穩的一個 Corpus 結論。

---

# FB｜下一輪優先

V0.12 已完成第一輪 cross-check。

下一步建議不是立即 Runtime，而是先做兩個 Corpus 收口工作：

1. **PRICE / FEE SOURCE-CONFLICT INDEX**
   - 上海／蘇州／天津
   - 茶圍／叫局／出局／碰和／吃酒／住夜
   - 價格、付款時點、現金／賒帳、房間分配
   - 專門保留數字矛盾，不替原作清洗。

2. **CITY TRANSITION PASS**
   - 上海 → 蘇州 → 天津
   - 哪些屬 `PERSONAL HISTORY`
   - 哪些屬 `LOCAL MARKET POSITION`
   - 哪些要重算
   - 哪些身份／債務／關係可攜帶
   - 哪些服務語彙／價格／規則必須換城市 provider。

完成這兩輪後，再判斷 Stage 1 是否已有資格封存為 `CORPUS BASELINE V1.0`。
---

# FC｜PRICE / FEE SOURCE-CONFLICT INDEX
# 價目 × 付款時點 × 現金／賒帳 × 城市／班別作用域

> 本節只做 Corpus 價目整理。  
> 不把人物花費反推出「標準價」，不把不同詞強行合成同一交易，也不替原作修正矛盾。

本輪先建立：

```yaml
PRICE_EVIDENCE:
  city:
  district:
  venue_class:
  house_or_courtesan_class:
  source_term:
  normalized_event_candidate:
  amount:
  currency:
  payer:
  payee:
  payment_timing:
  cash_or_credit:
  prepay_or_advance_actor:
  chapter:
  evidence_type:
  lexical_uncertainty:
  conflict_group:
  status:
```

最重要的硬鎖：

```text
AMOUNT
without
CITY + VENUE + SERVICE TERM + PAYMENT MODE
is not a usable market rule
```

---

# FD｜SHANGHAI PRICE / FEE INDEX

## FD-001｜碰和：第1回 20 vs 第54回 12

第1回敘事比較蘇滬：

```text
上海碰和
→ 一概二十元
```

第54回敘事再次比較蘇滬：

```text
上海地方
→ 吃酒、碰和
→ 都是十二塊錢
```

因此：

```yaml
PRICE_CONFLICT:
  id: "PRICE-CONFLICT-SH-PENGHE-001"
  service: "PENGHE"
  city: "上海"

  source_A:
    chapter: 1
    amount: 20
    currency: "元／洋元語境"
    evidence_type: "NARRATOR_EXPLICIT_RULE"

  source_B:
    chapter: 54
    amount: 12
    currency: "塊錢"
    evidence_type: "NARRATOR_EXPLICIT_RULE"

  status: "UNRESOLVED_SOURCE_CONFLICT"
```

目前禁止：

```text
選 20
選 12
取平均 16
解釋成通貨膨脹
自動假定長三／么二差別
```

除非後續正文給出合法作用域。

---

## FD-002｜吃酒：第54回上海 12

第54回：

```text
上海地方
→ 吃酒十二塊
```

同段還說：

```text
吃酒對房間本身未必有直接好處
→ 主要可「繃外場」
```

因此：

```yaml
PRICE_ENTRY:
  id: "SH-EAT-WINE-CH54"
  city: "上海"
  service: "EAT_WINE / BANQUET"
  amount: 12
  evidence_type: "NARRATOR_EXPLICIT_RULE"
  status: "OBSERVED_SCOPED_RULE"
```

注意：

```text
吃酒十二
!= 任意「菜錢」都十二
```

後文 aggregate ledger 不能反向拿來硬算。

---

## FD-003｜上海出局／局錢：第144回一個局一塊，常賒帳

第144回敘事比較天津與上海：

```text
上海：
→ 出一個局
→ 一古腦兒只有一塊錢
→ 還要大家賒帳
```

因此：

```yaml
PRICE_ENTRY:
  id: "SH-OUTCALL-CH144"
  city: "上海"
  source_term: "出一個局"
  amount: 1
  payment_mode: "CREDIT COMMON"
  evidence_type: "NARRATOR_COMPARATIVE_RULE"
```

這與第64回大量 `局錢／局帳` 可到節邊集中開銷的情形相容。

但禁止直接寫：

```text
所有上海局帳 = count * 1
```

因為正文另有 bundle／帳單語義尚未完全拆清。

---

## FD-004｜上海茶圍：第89回「通共一塊」只作低法位候選

第89回衝突場面中，闖房流氓說：

```text
你們通共出了一塊錢來打個茶圍
```

這可能表示當時該房的茶圍交易成本為一塊。

但來源是：

```yaml
EVIDENCE:
  type: "CHARACTER_CLAIM_IN_CONFLICT"
  speaker: "流氓"
```

不是敘事者價目說明。

因此：

```yaml
PRICE_CANDIDATE:
  id: "SH-TEA-CH89"
  city: "上海_CONTEXT_HIGH_CONFIDENCE"
  service: "TEA_VISIT"
  amount: 1
  status: "PROVISIONAL / LOW_AUTHORITY"
```

不能與天津南班茶圍一塊直接視為同制度。

---

# FE｜SHANGHAI OVERNIGHT / 下腳：不是固定 tarifa

## FE-001｜正文可見多個不同下腳數字

上海案例：

```text
第6回 方幼惲／陸蘭芬
→ 住一夜
→ 下腳二十

第25回 章秋谷／張書玉
→ 住一宵
→ 照例下腳二十

第23回 邱八／林黛玉
→ 住一夜
→ 下腳五十
→ 另有體己三百（被退）

第75回 李子霄／張書玉
→ 住一夜
→ 住夜下腳四十
```

所以：

```text
OVERNIGHT_EVENT
does not map to
ONE FIXED SHANGHAI NIGHT PRICE
```

---

## FE-002｜人物明說「名妓下腳至少應加倍」仍只是社會評價

第9回章秋谷評論方幼惲：

```text
陸蘭芬有聲價
+
破格留宿
→ 下腳二十太少
→ 「至少要再加一倍」
```

法位：

```yaml
EVIDENCE:
  type: "CHARACTER_ARGUMENT"
  speaker: "章秋谷"
```

可支持：

```text
下腳具有
FACE / STATUS / GENEROSITY INTERPRETATION
```

不能支持：

```text
名妓固定下腳 = 40
```

---

## FE-003｜天津沒有「下腳」習俗，但仍有住夜費

第149回：

```text
章秋谷住後要多給錢
→ 房間人員明說：
「天津嘸撥下腳」
```

而第142回天津已有：

```text
南班住夜 = 6塊
北班住夜 = 5兩銀子
```

因此正式分離：

```text
OVERNIGHT SERVICE FEE
!= 下腳 / GRATUITY
```

並得到：

```text
SHANGHAI:
  下腳存在，數額有社會彈性

TIANJIN:
  有住夜價
  但「下腳」作為上海式額外習俗不存在
```

這是城市 Provider 必須保存的差異。

---

# FF｜SUZHOU PRICE / FEE INDEX

## FF-001｜碰和：正式八塊；制度形成前四／六不定

第54回：

```text
蘇州原本：
→ 只有吃酒
→ 沒有正式碰和名目

偶然碰和：
→ 和錢四塊或六塊
→ 沒有一定

後來正式設碰和：
→ 每場八塊
```

因此同一城市同一詞必須帶時間：

```yaml
SUZHOU_PENGHE_HISTORY:

  early_informal:
    amount_examples: [4,6]
    fixed_tariff: false

  later_formalized:
    amount: 8
    fixed_tariff: true
```

這不是 source conflict，而是：

```text
RULE EVOLUTION
```

---

## FF-002｜吃酒正價十二

第54回：

```text
蘇州每一台酒
→ 正價十二
```

但這不是客人實際總支出。

---

## FF-003｜檯面洋錢：每位客人 2，現付

第1、54回一致：

```text
吃酒無論主客
→ 每人檯面洋錢二元
→ 現開銷
```

第1回實際事件：

```text
7個客人
→ 14塊檯面
```

因此：

```yaml
SUZHOU_TABLE_FEE:
  unit: "PER_GUEST"
  amount: 2
  payment_timing: "IMMEDIATE"
  cash_required: true
```

---

## FF-004｜坐場洋錢：每個叫來的局 1，當場發

第54回：

```text
叫來的局
→ 坐場洋錢每人一元
→ 當場開發
```

八客各叫一局的例子：

```text
檯面：
8 * 2 = 16

坐場：
8 * 1 = 8

酒正價：
12

至少可見即時／基本支出：
12 + 16 + 8 = 36
```

但仍有：

```text
局帳
→ 可逢節開銷
```

所以：

```text
36
!= FULL ECONOMIC COST OF ALL CLIENT-COURTESAN RELATIONS
```

---

## FF-005｜坐場是倌人先墊的現金曝險

第54回：

```text
客人的局帳
→ 可逢節開銷

但倌人出局的坐場洋錢
→ 先要自己墊出
```

因此：

```yaml
CALL_CREDIT_EXPOSURE:
  receivable_timing: "DEFERRED / FESTIVAL"
  seat_fee_timing: "IMMEDIATE"
  prepay_actor: "COURTESAN"
```

這一條直接證明：

```text
CALL ACCEPTANCE
can depend on CREDIT RISK
```

而不是只看關係偏愛。

---

## FF-006｜第1回「下腳四元＋添菜二元」只屬單次 event line item

第1回實際席面：

```text
秋谷：
→ 下腳4
→ 添菜2
```

這只是：

```yaml
EVENT_SPECIFIC_LINE_ITEM:
  chapter: 1
  values:
    下腳: 4
    添菜: 2
```

正文沒有證明：

```text
蘇州所有宴席下腳 = 4
添菜固定 = 2
```

因此不可升成 tariff。

---

# FG｜TIANJIN BASE PRICE TABLE｜第142回

第142回是目前最完整的一張 narrator tariff table：

```yaml
TIANJIN_PRICE_TABLE_CH142:

  SOUTHERN_CLASS:
    tea_visit:
      amount: 1
      unit: "per visit"

    penghe:
      amount: 16

    eat_wine:
      amount: 16

    overnight:
      amount: 6
      currency: "塊錢"

  NORTHERN_CLASS:
    tea_visit:
      amount: 2
      unit: "per visit"

    penghe:
      amount: 16

    eat_wine:
      amount: 22

    overnight:
      amount: 5
      currency: "兩銀子"

  BOTH_CLASSES:
    named_call:
      amount: 5

    "請倌人出局":
      amount: 3
```

---

## FG-001｜茶圍逐次收費

第142回：

```text
一天去十趟
→ 十次茶圍錢
→ 一次不能少
```

所以：

```text
TEA_VISIT FEE
is PER-OCCURRENCE
```

不是日票或熟客包月。

---

## FG-002｜生客只看不選，可以零支出離開

第142回：

```text
生客進班
→ 合班姑娘出來
→ 客人挑選

若一個都不中意
→ 直接離開
→ 不花一個大錢
```

因此：

```text
DISCOVERY / SELECTION
!= TEA_VISIT TRANSACTION
```

---

## FG-003｜住夜逐夜計費，且與吃酒／碰和互不前置

第142回：

```text
住一夜是一夜的錢
住十夜是十夜的錢
```

並明說：

```text
住夜
!= 必須碰和吃酒

碰和吃酒
!= 必須住夜
```

所以：

```text
OVERNIGHT
is a separate billed event
```

---

# FH｜TIANJIN CALL PAYMENT MODE｜第144回

## FH-001｜叫局 5，大半現錢

第144回：

```text
天津叫一個局
→ 五塊
→ 大半現錢
→ 沒有什麼賒帳
```

若不付現：

```text
通常只有向來要好的熟客
→ 才可能辦到
```

因此：

```yaml
TIANJIN_CALL_CREDIT:
  base_amount: 5
  dominant_payment_mode: "CASH"
  credit_exception:
    requires: "ESTABLISHED_REGULAR_RELATION"
```

這不是：

```text
熟客免費
```

而是：

```text
熟客可能取得 CREDIT ELIGIBILITY
```

---

## FH-002｜陌生客叫局可能因現金曝險被拒

第144回：

```text
陌生客叫局
→ 倌人多半推托不去

若勉強去
→ 也可能當面討錢
```

原因之一：

```text
若客人賒帳
→ 倌人要自己貼掉坐場錢
```

所以：

```text
CREDIT STATUS
affects
CALL ACCEPTANCE
```

正式接到 V0.8 Credit Memory。

---

# FI｜天津「叫局5／出局3／帶局1」暫時不得合併

目前正文同時有：

第142回：

```text
叫局 = 5
請倌人出局 = 3
```

第144回：

```text
天津地方的「帶局」 = 1
```

三個詞目前沒有足夠 Corpus 證明它們完全同義。

因此：

```yaml
LEXICAL_PRICE_SPLIT:
  city: "天津"

  叫局:
    amount: 5
    status: "ATTESTED"

  請倌人出局:
    amount: 3
    status: "ATTESTED"

  帶局:
    amount: 1
    status: "ATTESTED_TERM_WITH_PRICE"

  mutual_equivalence:
    status: "UNRESOLVED"
```

禁止把：

```text
5 / 3 / 1
```

直接標成「原作價目矛盾」。

目前最安全的是：

> **三種 lexical transaction type 尚未完成 semantic merge。**

---

# FJ｜坐場錢 VENUE SCOPE：第144回本身需要 HOLD

第144回同一段先說：

```text
倌人應局
→ 除戲館、自家公館外
→ 一概有一塊坐場錢
```

接著又說：

```text
蘇州：
→ 只有堂子叫局有坐場
→ 酒館、大菜館沒有

天津：
→ 大菜館和酒館「也是這般」
```

因此若逐字讀取，venue scope 存在不清楚處：

```yaml
VENUE_SCOPE_CONFLICT:
  id: "SEAT-FEE-SCOPE-CH144"

  clearly_supported:
    amount: 1

  unclear:
    - "天津酒館／大菜館究竟有無坐場"
    - "『一概』的實際指涉範圍"

  status: "UNRESOLVED_WITHIN_SAME_EXPLANATORY_PASSAGE"
```

這不是要說作者一定自相矛盾。

而是：

> **目前沒有資格把這段壓成乾淨布林規則。**

---

# FK｜NO BACK-SOLVING PRICE FROM AGGREGATE LEDGER

本輪抓到一個很重要的 Corpus 方法問題：

> **不能拿總帳反推單價，再把反推出來的單價當原作規則。**

---

## FK-001｜第35回

陳海秋說：

```text
23個局錢
+
3台菜錢
=
47塊
```

如果拿第144回上海：

```text
局 = 1
```

再拿第54回：

```text
吃酒 = 12
```

硬代：

```text
23 + 3*12 = 59
```

對不上。

但這不代表：

```text
第35回 arithmetic error
```

因為正文只說：

```text
「菜錢」
```

沒有證明 `菜錢 == 標準吃酒正價`。

因此判定：

```yaml
DERIVATION_WARNING:
  id: "NO-BACKSOLVE-CH35"
  result:
    - "DO NOT DERIVE UNIT PRICE"
    - "DO NOT EQUATE 菜錢 WITH 吃酒 tariff WITHOUT SOURCE"
```

---

## FK-002｜第100回

帳單：

```text
26台菜錢
+
19場和錢
+
120多個局錢
+
另借100本錢
≈ 600多塊
```

同樣不能拿既知 tarif 強拆。

它只證明：

```text
LEDGER contains multiple transaction families
```

不能證明每一項的標準單價。

---

# FL｜FEE TYPE SEPARATION

本輪價目抽取後，至少要分：

```yaml
FEE_TYPE:

  SERVICE_BASE_PRICE:
    examples:
      - "吃酒正價"
      - "碰和"
      - "茶圍"
      - "住夜"
      - "叫局"

  PER_PERSON_TABLE_FEE:
    example: "蘇州檯面洋錢"

  COURTESAN_SEAT_FEE:
    example: "坐場洋錢"

  CLIENT_COURTESAN_RECEIVABLE:
    example: "局帳"

  GRATUITY_OR_DOWNFOOT:
    example: "下腳"

  ADD_ON_FOOD:
    example: "添菜"

  GIFT_OR_ROOM_STAFF_PAYMENT:
    examples:
      - "手巾"
      - "司菜"
      - "房間賞錢"

  RELATIONSHIP_SUPPORT:
    example:
      - "每月貼四百，吃酒叫局外算"

  DEBT_OR_LOAN:
    example:
      - "借款"
```

硬鎖：

```text
SERVICE PRICE
!= GRATUITY
!= TABLE FEE
!= SEAT FEE
!= RECEIVABLE
!= GIFT
!= RELATIONSHIP SUPPORT
```

---

# FM｜CONTRACT OVERLAY DOES NOT REPLACE MARKET FEES

第167回潘侯爺與沈二寶：

```text
每月貼四百
+
吃酒叫局外算
```

這是非常乾淨的證據：

```text
RELATIONSHIP / EXCLUSIVITY SUPPORT PAYMENT
does not absorb
ordinary market transactions
```

所以：

```yaml
RELATIONSHIP_SUPPORT_CONTRACT:
  periodic_support: 400
  excluded_from_support:
    - "吃酒"
    - "叫局"
```

這與早期：

```text
認開銷
!= 做恩客
!= 每次交易全免
```

的分軸相容。

---

# FN｜PRICE / PAYMENT-MODE MATRIX V0.1

```yaml
PRICE_MATRIX:

  SHANGHAI:

    tea_visit:
      amount_candidate: 1
      source: "CH89 CHARACTER CLAIM"
      confidence: "LOW"

    penghe:
      observations:
        - {chapter: 1, amount: 20}
        - {chapter: 54, amount: 12}
      status: "SOURCE_CONFLICT"

    eat_wine:
      observations:
        - {chapter: 54, amount: 12}
      status: "OBSERVED"

    outcall:
      observations:
        - {chapter: 144, amount: 1, payment_mode: "CREDIT COMMON"}
      status: "OBSERVED_COMPARATIVE_RULE"

    overnight:
      fixed_base_price:
        status: "NOT ESTABLISHED"

      downfoot_examples:
        - {chapter: 6, amount: 20}
        - {chapter: 23, amount: 50}
        - {chapter: 25, amount: 20}
        - {chapter: 75, amount: 40}

      interpretation:
        - "VARIABLE SOCIAL PAYMENT / GRATUITY-LIKE"

    tangchang:
      payment_mode: "CASH"
      amount: "UNKNOWN"
      chapter: 1

  SUZHOU:

    penghe:
      historical_informal:
        amounts: [4,6]
        fixed: false
      formal:
        amount: 8

    eat_wine:
      base_price: 12

    table_fee:
      amount: 2
      unit: "PER_GUEST"
      payment_mode: "IMMEDIATE CASH"

    seat_fee:
      amount: 1
      unit: "PER CALLED COURTESAN"
      payment_mode: "IMMEDIATE"
      economic_burden:
        - "courtesan may have to advance"

    call_receivable:
      payment_timing:
        - "festival settlement possible"

  TIANJIN:

    SOUTHERN_CLASS:
      tea_visit: 1
      penghe: 16
      eat_wine: 16
      overnight: 6

    NORTHERN_CLASS:
      tea_visit: 2
      penghe: 16
      eat_wine: 22
      overnight: "5 taels silver"

    BOTH:
      named_call:
        amount: 5
        payment_mode: "mostly cash"
        credit:
          condition: "regular/familiar client"

      "請倌人出局":
        amount: 3

      "帶局":
        amount: 1
        semantic_relation_to_outcall: "UNRESOLVED"

    downfoot:
      status: "NO TIANJIN CUSTOM PER CH149"
```

---

# FO｜SOURCE-CONFLICT INDEX UPDATE

```yaml
PRICE_SOURCE_CONFLICT_INDEX:

  PRICE-CONFLICT-001:
    issue: "上海碰和"
    chapter_A: 1
    value_A: 20
    chapter_B: 54
    value_B: 12
    status: "UNRESOLVED"

  PRICE-CONFLICT-002:
    issue: "第144回坐場錢 venue scope"
    amount:
      value: 1
      status: "STABLE"
    venue_scope:
      status: "UNRESOLVED"
    reason:
      - "同段先用近似全稱說法"
      - "後文又對蘇州／天津酒館大菜館作例外描述"

  PRICE-HOLD-003:
    issue: "天津 叫局5 / 出局3 / 帶局1"
    status: "SEMANTIC_SPLIT_REQUIRED"
    not_yet_a_conflict: true

  PRICE-HOLD-004:
    issue: "上海茶圍1"
    chapter: 89
    status: "LOW-AUTHORITY CHARACTER CLAIM"

  PRICE-HOLD-005:
    issue: "上海住夜下腳"
    values: [20,50,20,40]
    status: "VARIABLE_EVENT_PAYMENT"
    not_a_fixed_tariff: true
```

---

# FP｜本輪形成的新硬結論候選

```text
PRICE RULE
requires SCOPE

CITY
is not enough by itself

VENUE CLASS
may change fee application

COURTESAN / HOUSE CLASS
may change price

PAYMENT MODE
changes behavior

CASH
!= CREDIT

SERVICE PRICE
!= GRATUITY

OVERNIGHT PRICE
!= 下腳

CALL FEE
!= 坐場 FEE
!= 局帳

TABLE FEE
can be PER GUEST

SEAT FEE
can be PER CALLED COURTESAN

DEFERRED RECEIVABLE
can coexist with
IMMEDIATE CASH EXPOSURE

SAME TERM
can change over TIME

DIFFERENT TERM
must not be merged merely because numbers look related

AGGREGATE LEDGER
must not be reverse-engineered into unsupported unit prices

SOURCE CONFLICT
is legal Corpus state
```

---

# FQ｜PRICE PROVIDER 仍不能寫成一張 global lookup table

目前若未來做 Runtime，價目至少需要：

```yaml
PRICE_QUERY_CONTEXT:
  city:
  time_period:
  district:
  venue_type:
  house_class:
  courtesan_class:
  transaction_type:
  local_lexical_term:
  client_credit_status:
  payment_timing:
  relationship_contract_overlay:
```

才能詢問：

```text
「這筆錢到底是多少、現在要不要付、誰先墊？」
```

因此禁止：

```yaml
PRICE_TABLE:
  tea_visit: 1
  call: 1
  penghe: 12
  overnight: 20
```

這種 global table 已被 Corpus 直接否決。

---

# FR｜下一輪：CITY TRANSITION PASS

Price/Fee Pass 後，下一輪正式做：

```text
上海
→ 蘇州
→ 天津
```

的跨城狀態攜帶。

優先判斷：

```yaml
CITY_TRANSITION_QUESTION:

  portable_personal_history:
    - "人物身份"
    - "既往關係"
    - "既往債務"
    - "技能／功架"
    - "外地名聲"
    - "既有秘密"

  local_recompute:
    - "當地聲價"
    - "當地客流"
    - "當地信用資格"
    - "服務詞彙"
    - "價目"
    - "場館規矩"
    - "排程成本"
    - "本家／班子權限"

  unresolved:
    - "外地熟客身份到新城是否仍算熟客"
    - "外地紅名能轉換多少"
    - "舊債權可否跨城市執行"
    - "媒體花榜跨城傳播強度"
```

完成後，再判斷 Stage 1 是否有資格封成：

```text
CORPUS BASELINE V1.0
```
---

# FS｜CITY TRANSITION PASS
# 跨城狀態攜帶 × 本地重綁 × 市場重算 × 地方法位

> 本輪處理 `上海 / 蘇州 / 天津` 的跨城問題。  
> 問題不是「人物換地圖後還剩多少數值」，而是：
>
> **哪些事實屬於人物歷史，哪些資格只在原城市成立，哪些狀態必須在新城市重新建立。**

第一版四分類：

```yaml
CITY_TRANSITION_CLASS:

  PORTABLE:
    meaning:
      - "事件已發生，因此人物移動後仍是其歷史的一部分。"
      - "不表示新城市居民自動知道。"

  REBIND:
    meaning:
      - "同一人物進入新城市後，必須重新綁定當地場館／角色／房間／名稱／組織位置。"

  RECOMPUTE:
    meaning:
      - "不能帶原值；必須依新城市、新時段、新市場重新形成。"

  SCOPED_ENFORCEMENT:
    meaning:
      - "法律、債務、契約、禁令或社會規則可以跟著人物成為歷史事實，但其實際效力範圍不能自行全球化。"
```

硬鎖：

```text
PORTABLE HISTORY
!= PORTABLE LOCAL STATUS
```

---

# FT｜CASE 001｜金月蘭：關係與資本可帶走，營業位置必須重建

第2回是目前最完整的跨城開業案例。

金月蘭原有一項明確限制：

```text
已具結
→ 不得在蘇／杭／滬三處再做生意
```

她因此：

```text
上海／蘇杭不敢再做
→ 聽聞天津市場富盛
→ 前往天津
→ 投奔舊姊妹林黛玉
```

到天津後並不是：

```text
OLD BUSINESS STATUS
→ 自動恢復
```

而是重新經過：

```text
舊姊妹接納
→ 女本家預備房間
→ 自己出資鋪設
→ 熟客替她擺雙台
→ 當地客流重新形成
```

而後才：

```text
車馬盈門
和酒紛紛
```

因此：

```yaml
CITY_TRANSITION_CASE:
  id: "CITY-001"
  character: "金月蘭"

  portable:
    - "與林黛玉的既有姊妹關係"
    - "人物身份與既往經歷"
    - "攜帶資產（金條／現銀）"
    - "原有技能／應酬能力"
    - "原地法律／具結歷史"

  rebind:
    - "天津班子"
    - "女本家"
    - "房間"
    - "開張社交支持者"

  recompute:
    - "天津客流"
    - "天津聲價"
    - "天津營業收入"

  scoped_enforcement:
    source_restriction_scope:
      - "蘇"
      - "杭"
      - "滬"
    tianjin_effect:
      status: "NOT SHOWN AS AUTOMATICALLY ENFORCED"
```

最重要的結論：

> **限制可以有地理作用域；跨城不是「清除違規史」，也不是「所有城市自動繼承同一執法效果」。**

---

# FU｜CASE 002｜阿毛：個人履歷可攜帶，ROLE_ASSIGNMENT 必須重綁

同在第2回：

```text
阿毛
→ 上海人
→ 大姐出身
→ 累積資本
→ 到天津開南班堂子
→ 成為女本家
```

因此：

```text
PERSONAL HISTORY
travels

ROLE ASSIGNMENT
changes
```

候選：

```yaml
CITY_TRANSITION_CASE:
  id: "CITY-002"
  character: "阿毛"

  portable:
    - "上海出身"
    - "大姐職業歷史"
    - "累積資本"
    - "可能的行業經驗"

  rebind:
    - from_role: "大姐"
    - to_role: "天津南班女本家"
    - local_venue_authority: "NEW LOCAL ASSIGNMENT"

  forbidden_inference:
    - "大姐天然可以升本家"
    - "跨城必然升職"
```

這再次強化 V0.3：

```text
ROLE
!= permanent identity
```

---

# FV｜CASE 003｜陸畹香：同一人跨城市／戰亂／時段，多次重算市場位置

第30回提供一條非常長的 transition chain：

```text
上海
→ 生意不好

天津（第一次）
→ 剛到即名聲大震
→ 堂子老闆重金羅致
→ 搭東閻樂
→ 冠蓋如雲

戰亂
→ 逃德州
→ 德州做不出生意

北京
→ 戰後景象蕭條
→ 支持不住

天津（再次）
→ 搭寶華班
→ 花運已退
→ 生意一節不如一節

上海（返回）
→ 想做住家
→ 擺碰和檯
→ 暫住舊姊妹龍蟾珠處
```

因此：

```yaml
CITY_TRANSITION_CASE:
  id: "CITY-003"
  character: "陸畹香"

  portable:
    - "人物身份"
    - "技藝"
    - "應酬能力"
    - "與章秋谷的舊識"
    - "與龍蟾珠的舊姊妹關係"
    - "歷次城市營業史"

  rebind:
    - "東閻樂班"
    - "寶華班"
    - "上海回歸後住家／碰和檯配置"

  recompute:
    - "每次進入天津的市場熱度"
    - "德州市場可行性"
    - "北京戰後市場可行性"
    - "上海回歸後的營業形態"

  external_market_pressure:
    - "戰亂"
    - "城市蕭條"
    - "市場時勢"
```

這一例直接否決：

```text
CITY = only geography
```

更接近：

```text
LOCAL MARKET POSITION
= CHARACTER HISTORY
× CITY
× PERIOD
× MARKET REGIME
× VENUE BINDING
× NETWORK RECEPTION
```

但此式只是結構表示，不是數值公式。

---

# FW｜CASE 004｜陸月卿 → 月芳：ENTITY_ID 可保持，DISPLAY_NAME 可換城／換期

第145回：

```text
上海時：
→ 名稱「陸月卿」
→ 十年前有些名氣
→ 車馬常盈

後來：
→ 上海門前冷落
→ 到天津做生意
→ 天津數年也不甚熱鬧
→ 當前稱「月芳」
```

因此：

```yaml
CITY_TRANSITION_CASE:
  id: "CITY-004"
  entity_id: "陸月卿／月芳 SAME ENTITY"

  portable:
    - "人物本體"
    - "上海舊名"
    - "上海聲價歷史"
    - "人物技能／應酬歷史"

  rebind:
    - "current display name = 月芳"
    - "current venue = 天津五鳳班"
    - "current local room"

  recompute:
    - "天津當前客流"
    - "天津當前聲價"

  rule:
    "ALIAS / DISPLAY_NAME may be CITY+PERIOD scoped"
```

正式強化：

```text
ENTITY_ID
!= CURRENT_DISPLAY_NAME
```

---

# FX｜CASE 005｜曹夢蘭 → 賽金花：改名、跨城、角色轉換可以連續發生

第172回：

```text
傅鈺蓮
→ 改名曹夢蘭
→ 上海重做生意
→ 「狀元夫人」既有身份被客人當成市場標籤
→ 聲名大燥

數年後
→ 年紀漸長
→ 生意漸退

再改名賽金花
→ 天津做生意
→ 香名大噪
→ 積累資本

北京
→ 買討人
→ 開堂子
→ 成為本家
```

因此：

```yaml
CITY_TRANSITION_CASE:
  id: "CITY-005"
  character: "傅鈺蓮 / 曹夢蘭 / 賽金花"

  portable:
    - "人物本體"
    - "色藝／技能歷史"
    - "既往社會身份歷史"
    - "既往人際關係"
    - "資本累積"

  rebind:
    - "display name"
    - "current city"
    - "current venue"
    - "current occupational role"

  recompute:
    - "上海當期聲名"
    - "天津當期香名"
    - "北京本家經營狀態"

  role_transition:
    from: "營業人物"
    to: "本家"

  hard_rule:
    "NAME CHANGE != ENTITY REPLACEMENT"
```

---

# FY｜跨城後舊關係不 reset，但必須有 communication / recognition source

## FY-001｜章秋谷 ↔ 陸畹香

第30回：

```text
兩年前天津舊識
→ 上海重逢
→ 彼此辨認
→ 舊交直接影響當下應酬
```

因此：

```text
RELATION HISTORY
can survive CITY CHANGE
```

---

## FY-002｜章秋谷 ↔ 陸麗娟

第159回：

```text
章秋谷人在天津
→ 陸麗娟仍在上海詢問他的消息
→ 辛修甫說常有信
→ 陸麗娟也收到過他的信
```

所以：

```text
DISTANCE
!= RELATION RESET
```

但同時：

```text
KNOWLEDGE ACROSS CITY
still requires a channel
```

候選：

```yaml
CROSS_CITY_COMMUNICATION:
  channel:
    - "letter"
    - "friend relay"
    - "newspaper / public media"
    - "traveler report"
  delay:
    status: "MUST EXIST / NOT YET QUANTIFIED"
```

---

## FY-003｜賽金花多年後仍有跨城認人，但記憶不是完美資料庫

第172回：

```text
章秋谷提起四年前天津碰和
+
近年北京再見

賽金花起初：
→ 覺得面熟
→ 想不起來

經提醒：
→ 才辨認
```

因此：

```text
RELATION EVENT HISTORY
may persist

but

CHARACTER MEMORY
can be PARTIAL
```

不能因 SAVE 有紀錄就讓人物永遠精確記得。

---

# FZ｜人物功架可帶走；LOCAL RULE KNOWLEDGE 不可帶成全知

第142回金觀察對章秋谷說：

```text
你是在上海頑慣的人
→ 也要看看天津風景
```

敘事隨即明說：

```text
天津嫖場規則
與上海大不相同
```

並重新解說：

```text
倌人 / 姑娘
堂子 / 窯子
南班 / 北班
茶圍價
碰和價
吃酒價
住夜價
叫局價
生客進班規則
```

第145回又有實際失手：

```text
章秋谷
→ 自稱上海歌場酒陣混了六年
→ 誤以為天津人物聽不懂蘇州話
→ 當面說壞話
→ 被對方聽懂
→ 自認第一次碰大釘子
```

所以正式分離：

```yaml
SOCIAL_COMPETENCE:

  portable:
    - "一般應酬能力"
    - "觀察／談吐／場面經驗"
    - "既往技能"

  local_relearn_required:
    - "地方制度"
    - "地方稱謂"
    - "地方價目"
    - "地方信用慣例"
    - "地方語言理解假設"
    - "地方場館禮法"
```

硬鎖：

```text
GENERAL FENGYUE EXPERIENCE
!= LOCAL MARKET KNOWLEDGE
```

---

# GA｜CITY PROVIDER 必須接管詞彙，不只是價目

第142回明確：

```text
上海：
妓女 = 倌人
妓院 = 堂子

天津：
妓女 = 姑娘
妓院 = 窯子
另有「班」的組織名目
```

而 V0.9 / V0.13 已抽出蘇州：

```text
檯面
坐場
局帳付款時點
```

所以跨城時需要：

```yaml
CITY_LEXICON_PROVIDER:
  person_role_terms:
  venue_terms:
  transaction_terms:
  fee_terms:
  service_terms:
  status_terms:
```

這不是翻譯裝飾，而是制度入口。

---

# GB｜HOUSEHOLD / VENUE BINDING 不能跨城照搬

上海既有證據：

```text
房間
娘姨
大姐
相幫
本家
→ room-centric local household
```

天津第142–144回：

```text
班
南班 / 北班
本家／老鴇權限
場館配置檯面局
班內姑娘輪流進房應酬
```

因此人物移動：

```text
上海房間
→ 天津
```

不能做：

```text
同一 HOUSEHOLD object 改 city
```

必須：

```yaml
VENUE_REBIND:
  detach_old_local_assignment:
  preserve_history:
  bind_new_city_provider:
  bind_new_venue:
  bind_new_room_or_banzi_position:
  bind_new_staff_relation:
```

歷史關係可保留，但當前組織權限必須重綁。

---

# GC｜小洪寶寶：「上海新到」是來源標籤，不是可攜帶 reputation 數值

第155回：

```text
寶華班
→ 上海新到的小洪寶寶
```

之後：

```text
金部郎快速建立實際往來
+
章秋谷在天津自製「津門南榜」
→ 取小洪寶寶第一
```

第156回又延續本地花榜事件。

因此可以說：

```text
ORIGIN LABEL
may affect local attention
```

但不能說：

```text
SHANGHAI_REPUTATION_SCORE
copied to
TIANJIN_REPUTATION_SCORE
```

尤其「津門南榜」本身是章秋谷個人評榜與報館傳播事件，
不能倒推成小洪寶寶在上海原有一個等值名次。

---

# GD｜跨城市場位置第一版

```yaml
CITY_MARKET_STATE:

  identity:
    entity_id:
    current_display_name:
    alias_history: []

  location:
    city:
    district:
    venue_id:
    room_or_banzi_binding:

  portable_history:
    origin:
    prior_roles: []
    prior_cities: []
    prior_relations: []
    prior_business_events: []
    prior_reputation_events: []
    known_skills: []
    legal_or_contract_history: []

  local_state:
    current_role:
    local_public_labels: []
    local_reputation:
    local_client_flow:
    local_credit_status:
    local_business_health:
    local_schedule:
    local_price_provider:
    local_venue_rules:
    local_staff_relations:

  epistemic:
    who_knows_prior_history: []
    information_channels: []
    rumors: []
```

注意：

```text
portable_history
is not
auto-public-history
```

人物把歷史帶進城市，不表示整座城市立刻知道。

---

# GE｜CITY TRANSITION EVENT 第一版

```yaml
CITY_TRANSITION_EVENT:
  character_id:
  from_city:
  to_city:
  departure_cause:
  arrival_cause:

  carried:
    identity:
    assets:
    relationship_history:
    skill_history:
    legal_contract_history:
    reputation_history:

  lost_or_changed_in_transit:
    assets:
    documents:
    staff:
    venue_binding:
    active_schedule:

  arrival_rebind:
    alias:
    role:
    venue:
    room_or_banzi:
    staff:
    local_network_anchor:

  local_recompute:
    market_reputation:
    client_flow:
    credit_eligibility:
    business_health:
    service_availability:
    price_context:

  knowledge_provenance:
    who_already_knows:
    who_learns_on_arrival:
    channel:

  completion_status:
  evidence_refs:
  uncertainty:
```

---

# GF｜CARRY / REBIND / RECOMPUTE MATRIX V0.1

```yaml
CITY_TRANSITION_MATRIX:

  ENTITY_ID:
    treatment: "PORTABLE"

  BIOGRAPHICAL_HISTORY:
    treatment: "PORTABLE"

  PAST_EVENT_HISTORY:
    treatment: "PORTABLE"

  RELATION_EVENT_HISTORY:
    treatment: "PORTABLE"
    caution: "CURRENT ACTIVE STATUS MAY CHANGE"

  PERSONAL_SKILL_HISTORY:
    treatment: "PORTABLE"

  ASSETS:
    treatment: "PORTABLE_IF_PHYSICALLY_RETAINED"
    caution:
      - "旅途中可損失"
      - "戰亂可清空"
      - "不能憑 SAVE 假定仍在"

  LEGAL / CONTRACT HISTORY:
    treatment: "PORTABLE FACT"
    enforcement: "SCOPED / SOURCE-DEPENDENT"

  CURRENT_DISPLAY_NAME:
    treatment: "REBINDABLE"

  CURRENT_ROLE:
    treatment: "REBIND"

  VENUE / HOUSEHOLD:
    treatment: "REBIND"

  ROOM / BANZI POSITION:
    treatment: "REBIND"

  STAFF RELATIONS:
    treatment: "REBIND UNLESS SAME PERSON TRAVELS"

  LOCAL REPUTATION:
    treatment: "RECOMPUTE"

  LOCAL CLIENT FLOW:
    treatment: "RECOMPUTE"

  LOCAL CREDIT ELIGIBILITY:
    treatment: "RECOMPUTE / RELATION-DEPENDENT"

  LOCAL PRICE:
    treatment: "RECOMPUTE THROUGH CITY PROVIDER"

  LOCAL SERVICE LEXICON:
    treatment: "REBIND THROUGH CITY PROVIDER"

  LOCAL SCHEDULE COST:
    treatment: "RECOMPUTE"

  LOCAL MEDIA RANK:
    treatment: "RECOMPUTE"

  PUBLIC KNOWLEDGE:
    treatment: "NOT PORTABLE BY DEFAULT"
    requires:
      - "source"
      - "传播 channel"
```

---

# GG｜跨城不是 RESET，也不是 COPY

本輪最重要的不變量：

```text
CITY CHANGE
!= WORLD RESET

CITY CHANGE
!= FULL STATE COPY
```

而是：

```text
CITY CHANGE
=
PORTABLE HISTORY
+
TRANSIT EVENTS
+
LOCAL REBIND
+
LOCAL RECOMPUTE
+
KNOWLEDGE RE-PROPAGATION
```

這與前面所有分軸相容：

```text
HISTORY
!= CURRENT STATUS

RELATION HISTORY
!= CURRENT ACCESS

PAST FAME
!= LOCAL CURRENT FAME

SKILL
!= LOCAL RULE KNOWLEDGE

LEGAL HISTORY
!= GLOBAL ENFORCEMENT

ENTITY
!= DISPLAY NAME

PERSON
!= ROLE
```

---

# GH｜Stage 1 Baseline Eligibility Audit

依原始開發 MEMO，Stage 1 的任務是先建立 192 回 Corpus 結構抽取，
至少涵蓋：

```text
CHARACTERS
VENUES
ROLES
FENGYUE_TERMS
TRANSACTIONS
RELATION_QUALIFICATIONS
EVENT_PATTERNS
```

目前 V0.14 已形成：

```yaml
STAGE1_COVERAGE:

  characters:
    status: "PASS"
    includes:
      - "ENTITY_ID / alias / collision lock"
      - "major character local bindings"
      - "cross-city alias history"

  venues:
    status: "PASS"
    includes:
      - "Shanghai room/household"
      - "Suzhou market/venue"
      - "Tianjin banzi"
      - "public hubs / mobile travel nodes"

  roles:
    status: "PASS"
    includes:
      - "娘姨 / 大姐 / 相幫 / 本家"
      - "role assignment"
      - "role mobility"
      - "cross-city rebind"

  fengyue_terms:
    status: "PASS"
    includes:
      - "叫局 / 出局 / 局票"
      - "檯面 / 坐場 / 碰和 / 吃酒 / 住夜"
      - "熟客 / 生客 / 恩客 / 相好"
      - "聲價 / 花榜 / 紅倌人"

  transactions:
    status: "PASS"
    includes:
      - "ledger"
      - "receivable / cash"
      - "debt / credit"
      - "price / fee scope"
      - "source conflict"

  relation_qualifications:
    status: "PASS"
    includes:
      - "actual / claimed / rumored"
      - "acknowledgement"
      - "money != relation"
      - "relation != access"

  event_patterns:
    status: "PASS"
    includes:
      - "call lifecycle"
      - "client switching"
      - "public conflict"
      - "marriage / exit lifecycle"
      - "business lifecycle"
      - "city transition"

  epistemic_discipline:
    status: "PASS"
    includes:
      - "fact / claim / label separation"
      - "knowledge provenance"
      - "counterevidence"
      - "source conflict preservation"
```

---

# GI｜Baseline Blocking Audit

下列問題仍未解：

```yaml
OPEN_ISSUES:

  OI-001:
    issue: "上海碰和 20 vs 12"
    status: "UNRESOLVED_SOURCE_CONFLICT"

  OI-002:
    issue: "天津 叫局5 / 請倌人出局3 / 帶局1 的精確語義關係"
    status: "SEMANTIC_SPLIT_REQUIRED"

  OI-003:
    issue: "第144回坐場錢 venue scope"
    status: "UNRESOLVED"

  OI-004:
    issue: "上海茶圍1是否可升 narrator-level tariff"
    status: "LOW-AUTHORITY"

  OI-005:
    issue: "跨城舊債權如何執行"
    status: "INSUFFICIENT CORPUS"

  OI-006:
    issue: "跨城媒體／花榜傳播速率"
    status: "INSUFFICIENT CORPUS"

  OI-007:
    issue: "外地熟客資格進入新城市後可轉換多少"
    status: "INSUFFICIENT CORPUS"

  OI-008:
    issue: "蘇州 household / staff model 深度仍低於上海"
    status: "PARTIAL"
```

但是：

> **這些 OPEN ISSUE 不阻擋 Source Corpus Baseline，因為 Baseline 本身允許 UNKNOWN / CONFLICT / PARTIAL。**

它們只阻擋：

```text
把 Corpus 冒充
完整 Runtime Specification
```

---

# GJ｜BASELINE VERDICT

```yaml
STAGE1_BASELINE_AUDIT:

  verdict: "PASS_AS_SOURCE_CORPUS_BASELINE"

  may_freeze_as:
    "JIUWEIGUI CORPUS STAGE1 BASELINE V1.0"

  does_not_mean:
    - "192回所有名詞均已窮盡"
    - "所有價格矛盾已解"
    - "所有人物都已有完整人物卡"
    - "Runtime 已完成"
    - "市場公式已完成"
    - "城市 Provider 已實作"
    - "未知項已被填平"

  reason:
    - "原始七類抽取已全部具備"
    - "關係／金錢／知情／市場／角色／城市已完成主要分軸"
    - "已做第一輪 counterexample pass"
    - "已建立 source conflict legal state"
    - "已建立 city transition semantics"
    - "剩餘問題可合法保存為 OPEN / UNKNOWN"
```

最短結論：

> **Stage 1 已有資格封基線；沒有資格自稱完整 Runtime。**

---

# GK｜Stage 1 Baseline Freeze Rule

Baseline V1.0 若生成，建議：

```yaml
BASELINE_FREEZE:

  source:
    parent: "九尾龜_CORPUS_STAGE1_WORKING_V0.14"

  mutable_after_freeze:
    false

  correction_policy:
    - "錯字／誤抽不得靜默改 V1.0"
    - "另開 V1.0.1 / V1.1 或 ERRATA"
    - "保留原 SHA"

  unresolved_policy:
    - "UNKNOWN 保留 UNKNOWN"
    - "SOURCE_CONFLICT 保留 SOURCE_CONFLICT"
    - "PROVISIONAL 不升 HARD"

  downstream_use:
    - "Runtime architecture design source"
    - "character pool extraction source"
    - "FENGYUE market provider source"
    - "regression source"

  forbidden:
    - "直接把候選 schema 當已部署 Runtime"
```
---

# GL｜BASELINE V1.0 FREEZE MANIFEST

```yaml
BASELINE_MANIFEST:
  id: "JIUWEIGUI_CORPUS_STAGE1_BASELINE_V1_0"
  parent_working: "九尾龜_CORPUS_STAGE1_WORKING_V0.14.md"
  status: "FROZEN_SOURCE_BASELINE"

  source_scope:
    primary_source: "九尾龜.epub"
    chapter_scope: "1..192"

  preserves:
    - "SOURCE_CONFLICT"
    - "UNKNOWN"
    - "PROVISIONAL_COUNTEREXAMPLE"
    - "LEXICAL_UNCERTAINTY"
    - "CITY/TIME/VENUE SCOPE"

  authority:
    source_corpus: true
    runtime_specification: false
    world_fact_for_new_game_instance: false
    character_decision_authority: false

  amendment:
    silent_edit: "FORBIDDEN"
    next_change:
      - "ERRATA"
      - "V1.0.1"
      - "V1.1"
```

> **本 Baseline 封存的是「目前已抽出的來源結構與不確定性」；不是把候選規則封聖成遊戲真理。**
