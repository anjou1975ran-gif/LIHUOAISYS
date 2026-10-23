# 觀止青樓（新）｜班富蘭線 HOT SAVE V1.10
## RELATION-FIRST｜理火三年・吉月初九｜午後收束／書商宴前｜2026-10-09

> **用途：** 承接 HOT V1.09，保存吉月初九午後至書商宴前已成立之人物、關係、物件、計畫與未決狀態。
>
> **重要：** 本檔只保存已成立事件與明確計畫；不把候選、待邀、待談、玩家尚未揭露之安排倒灌成已完成事實。
>
> **執行邊界：** 本次為當前對話中依玩家明示所做之 document-level HOT SAVE。不得冒稱 Host-instrumented Formal SAVE、E6/E7、Formal Main 或獨立 Agent receipt。

---

# 0｜CURRENT POINTER

```yaml
ROUTE: "GUANZHI_BANFULAN_ROUTE"
PLAYER: "班傑明／字富蘭／號克林居士"
PREVIOUS_HOT: "V1.09"
CURRENT_HOT: "V1.10"
MASTER: "V1.0"
CHARACTER_INDEX: "V1.0"

STORY_DATE: "理火三年・吉月初九"
TIME: "午後收束／傍晚前；晚宴尚未開席"
CURRENT_SCENE_LOCATION: "觀止二樓・張麗華房中"

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

# 1｜本輪最重要的新狀態

```text
班富蘭已從「街頭假詞／私抄」問題，轉向建立正式出版來源與正本識別。

今晚預定在觀止設書商宴：
- 應伯爵負責邀兩家書商。
- 蘇清本人已答應出席。
- 浮香為主要邀請清倌。
- 紫蘭若有空且本人願意，可一併出席。
- 阿麗婭明確不列入本局。
- 疏影明確不列入本局，不要求她再靠此類陪席賺錢。
- 張麗華已接受以班富蘭「女伴」身分私人赴約；不是陪酒、不是掛牌服務、不是商業宣傳物。

晚宴尚未開始。
兩家書商是否到齊、浮香／紫蘭是否接受邀請、出版分工與價格均仍未決。
```

---

# 2｜街頭假詞事件 × 出版正本策略

## 2.1 已成立事件

- 班富蘭於午後街頭遇到以「克林居士」名義販售之假詞《汴河月》。
- 應伯爵亦看見該假詞，並認為不像班富蘭作品。
- 市場已出現利用「克林居士」名號之灰色私抄／冒名現象。

## 2.2 班富蘭明示立場

```yaml
COUNTERFEIT_POLICY:
  investigate_gray_market_source: false
  reason:
    - "灰產源頭追查成本高、容易換殼，浪費時間。"
    - "有人願意冒名至少證明名號已有市場注意力。"
  phrase_logic:
    - "惡名也是名。"

  preferred_strategy:
    - "不以抓假貨為核心。"
    - "建立可辨識的正式授權／正版來源。"
```

## 2.3 出版策略目前尚未完成之處

班富蘭最初想到「授權一家書商成為唯一正式出版來源」，後續又改成今晚先找**兩家書商**共同到場，查看是否可依能力分工。

因此 Current 不得偷定：

```text
唯一出版社 = 尚未成立
兩家均為正式出版社 = 尚未成立
獨家授權 = 尚未成立
刻印／校對／鋪貨／外地發行分工 = 尚未成立
稿酬／版稅／分帳 = 尚未成立
```

真正已成立的是：

> **今晚要談如何建立「正版／正本／正式授權來源」，並讓兩家書商提出自己的能力與分工方案。**

---

# 3｜應伯爵｜今晚書商中介任務

班富蘭已明示交代應伯爵：

- 若有人脈，找兩家書商。
- 今晚到觀止赴席。
- 應伯爵本人作陪。
- 席上談出版與分工。

```yaml
YING_BOJUE_BOOKSELLER_TASK:
  invite_two_booksellers: true
  tonight_guanzhi_dinner: planned
  ying_attends: planned
  exact_bookseller_identity: UNKNOWN
  actual_acceptance: UNKNOWN
  commission: NOT_FIXED
  agency: NOT_EXCLUSIVE
  authority_to_sign_for_ban: false
```

應伯爵仍只是中介／牽線者；不能替班富蘭簽約。

---

# 4｜兩方「富蘭克林」印章

班富蘭午後已到金石鋪實際刻成兩方隨身印。

## 4.1 第一方｜中文小方印

```yaml
SEAL_1:
  text: "富蘭克林"
  form: "小型方印"
  purpose:
    - "中文正名"
    - "詩稿／書稿／正本識別"
    - "日常隨身鈐用"
  status: "COMPLETED / IN BAN POSSESSION"
```

## 4.2 第二方｜Franklin 長形印

班富蘭以毛筆寫下 `Franklin`，要求刻印師將此視為「圖形」照形刻成長形印。

```yaml
SEAL_2:
  text_shape: "Franklin"
  form: "長形印"
  meaning_in_local_scene:
    - "外來文字／圖形標記"
    - "與中文富蘭克林方印形成雙重識別"
  status: "COMPLETED / IN BAN POSSESSION"
```

兩印未被宣稱為不可仿造之防偽技術；其真正價值要與正式出版來源、底本與授權制度一起形成。

班富蘭另有未執行想法：日後再做一方「超大章」。

```yaml
LARGE_SEAL:
  status: "IDEA_ONLY / NOT_ORDERED"
```

---

# 5｜今晚觀止書商宴｜席面架構

## 5.1 席面目的

```yaml
BOOKSELLER_DINNER:
  purpose:
    - "正式出版"
    - "正本識別"
    - "授權方式"
    - "兩家書商可能分工"
    - "故事 × 詞 × 曲 × 唱之新產品模型"

  NOT_PURPOSE:
    - "追捕街頭假詞販子"
    - "查灰產源頭"
    - "普通喝花酒"
```

## 5.2 目前人員法位

### 已答應／已成立

- **班富蘭**：主人。
- **蘇清**：本人已答應出席，並參與故事／出版設計。
- **張麗華**：本人已接受以班富蘭私人女伴身分出席。

### 已受託邀請、但實際到場仍未確認

- **應伯爵**：負責找兩家書商並作陪；是否成功帶兩家到場待晚間確認。
- **兩家書商**：身份與實際接受狀態 UNKNOWN。
- **浮香**：班富蘭指定主要邀請；需本人接受。
- **紫蘭**：若今晚有空且本人願意，可一同出席；需本人接受。

### 明確不列入

- **阿麗婭**：班富蘭認為此局不適合，明確不邀。
- **疏影**：班富蘭認為她不適合這種局，且現在不需要再靠此類出席賺錢，明確不邀。

---

# 6｜蘇清 × 班富蘭｜第一個聯合作品模型

班富蘭將今晚出版局進一步擴成「聯合創作／連載／音樂」產品。

核心不是單賣詩詞，而是讓詩詞背後故事被串成可持續追讀的作品。

## 6.1 第一個作品

```yaml
FIRST_PROJECT:
  source_inspiration: "《天龍八部》蕭峰 × 阿朱故事線"
  scope: "先抽出蕭峰與阿朱主線，不做整部天龍八部全量改寫"

  songs:
    - "萬水千山縱橫"
    - "兩忘煙水裡"

  roles:
    BAN_FULAN:
      - "提供後世作品記憶碎片"
      - "提供歌詞／旋律記憶"
      - "以哼唱方式提供旋律線索"
      - "提出出版與商業結構"

    SU_QING:
      - "負責把蕭峰 × 阿朱故事改寫成汴京讀者可追之連載文本"
      - "不要求完整逐字重現後世小說"

    FUXIANG:
      - "若接受參與，依班富蘭哼唱重新整理／編曲為本地可演奏版本"

    ZILAN:
      - "若接受參與，作為演唱者"

    BOOKSELLERS:
      - "出版／刻印／鋪貨／唱本／發行方式今晚再談"
```

## 6.2 創作方法

雙方目前形成之方法：

```text
後世故事骨架
+ 觀止人物／觀止語境可理解的改編
+ 班富蘭記得的詞／歌／爆點
+ 蘇清的連載能力
+ 浮香的音樂重整
+ 紫蘭的演唱
+ 書商的出版與流通
= 第一個跨媒介聯合作品
```

尚未完成：

- 蘇清尚未真正完成第一篇全文。
- 浮香尚未正式聽曲／編曲。
- 紫蘭尚未正式接受演唱。
- 書商尚未簽約。
- 定價／連載頻率／唱本形式／版稅未定。

---

# 7｜「上蘇下清仙姑」工作稱呼

班富蘭以「上蘇下清仙姑」稱蘇清為故事作者／筆名候選。

蘇清在對話中以玩笑方式接受並寫下「上蘇下清仙姑／暫定」。

```yaml
SU_QING_PEN_NAME:
  candidate: "上蘇下清仙姑"
  status: "WORKING / PLAYFUL / NOT YET FORMAL PUBLICATION PEN NAME"
```

不得倒灌成已正式公開使用之筆名。

---

# 8｜真實當代人物 × 架空改編規則（本作品工作原則）

在討論《天龍八部》改編時，班富蘭指出：

- 耶律洪基與宋仁宗為同時代真實當代政治人物。
- 若小說直接以現實政治人物作高風險虛構，可能引發現實政治／外交風險。

因此目前形成**本作品的改編方向**：

```text
人物情感／衝突骨架可以借。

仍活著、仍有權、仍可能對作品產生真實反應的當代人物，
優先考慮架空化處理。
```

班富蘭提出玩笑式架空：

```text
耶律家 → 耶路家
```

「耶路撒冷」亦在對話中作為笑談出現。

```yaml
FICTIONALIZATION_NOTE:
  world_canon_change: false
  project_story_rule: "WORKING CREATIVE RULE ONLY"
  yelu_to_yelu_route: "JOKE / CANDIDATE"
```

不得將「耶路家」寫成觀止 World Canon 或真實歷史改寫。

---

# 9｜張麗華｜今晚女伴法位

班富蘭回觀止後，進入隔壁張麗華房中飲酒並提出晚宴邀請。

## 9.1 張麗華已接受

```yaml
ZHANG_LIHUA_EVENING_ROLE:
  accepted: true
  role: "BAN_FULAN_PRIVATE_FEMALE_COMPANION"
  not_role:
    - "陪酒姑娘"
    - "掛牌妓女"
    - "觀止配置之商業陪席"
    - "書商宴商品"

  attendance_fee: 0
  banquet_food_and_drink_paid_by: "班富蘭／主人席"
```

班富蘭明確承認她不是陪酒服務，而是以「麗華夫人／貴妃」本人身份作私人女伴赴約。

## 9.2 名號商業使用邊界

張麗華明示：

> 她本人願意以張麗華身份赴宴，不等於班富蘭可將「陳後主張貴妃親自坐席」拿來對外招客或提高席面價值。

```yaml
ZHANG_LIHUA_NAME_COMMERCIAL_USE:
  private_identity_at_dinner: ALLOWED_BY_HER
  promotional_use: REQUIRES_SEPARATE_PERMISSION
  current_permission_for_promotion: false
```

## 9.3 酒醉後照料邊界

班富蘭表示：若張麗華晚上喝醉，酒帳由他負責，並願意抱她回房上床、協助換睡衣。

張麗華回覆之成立邊界：

```yaml
IF_ZHANG_LIHUA_DRUNK:
  ban_may_carry_back_to_room: true
  ban_may_place_her_on_bed: true
  ban_may_remove_shoes: true

  clothing_change:
    if_lihua_awake_and_explicitly_requests_help: "BAN MAY HELP"
    if_too_drunk_to_clearly_request: "CALL HER PEOPLE / FEMALE ATTENDANT"

  intoxication_is_not_consent: true
```

張麗華另以玩笑口吻表示：若她清醒時主動要求班富蘭協助換睡衣，則另當別論。

不得將此預寫成今晚一定發生之親密事件。

---

# 10｜張麗華鄰居關係增量

既有：

- 班富蘭與張麗華為觀止二樓鄰居。
- 兩人已有「酒國張貴妃」歌曲與「貴妃洗澡水」笑談。
- 張麗華不是掛牌接客女子。

本輪新增：

```yaml
BAN_X_LIHUA_RELATION_DELTA:
  - "PRIVATE_NEIGHBOR_FAMILIARITY_DEEPENED"
  - "CASUAL_ROOM_VISIT / SHARED_DRINKING_NORMALIZED"
  - "ZHANG_LIHUA_ACCEPTED_ONE_EVENING_AS_BAN_PRIVATE_FEMALE_COMPANION"
  - "NO ATTENDANCE FEE"
  - "NO COMMERCIAL COMPANIONSHIP CONTRACT"
  - "NO ROMANCE ESTABLISHED"
  - "NO SEXUAL CONSENT ESTABLISHED"
  - "NO PUBLICITY RIGHT GRANTED"
```

班富蘭另開玩笑表示，既然潘金蓮不收張麗華酒錢，以後自己想喝酒可來她房中蹭酒。

此為鄰居熟稔／玩笑，不是免費供酒契約。

---

# 11｜蘇清目前不知道的玩家安排

班富蘭明示：

> 晚上還打算另外邀一個人，但目前先不告訴蘇清。

```yaml
UNDISCLOSED_EVENING_GUEST:
  player_intention_exists: true
  identity: "PLAYER-HELD / NOT DISCLOSED IN CURRENT STORY"
  invitation_executed: false
  su_qing_knows: false
  director_must_not_invent_identity: true
```

此人不得由 Director 自行補全。

---

# 12｜今晚尚未成立／禁止倒灌

以下均保持 OPEN／UNKNOWN：

- 兩家書商實際是誰。
- 應伯爵是否成功邀到兩家。
- 浮香是否答應出席。
- 紫蘭是否有空、是否答應出席。
- 出版合作是否成交。
- 哪一家負責刻印／校對／鋪貨／外地路線。
- 是否採一主一副、共同授權或單一獨家。
- 蘇清連載首稿是否完成。
- 浮香是否接受編曲。
- 紫蘭是否接受演唱。
- 第一部作品正式名稱。
- 定價、稿費、版稅、分帳。
- 張麗華今晚是否喝醉。
- 張麗華今晚任何親密行為。
- 班富蘭尚未公開之額外客人身份。

---

# 13｜NEXT ENTRY｜進晚間的最短接關

```text
理火三年・吉月初九，午後已近尾聲。

班富蘭仍在張麗華房中；張麗華已答應今晚以私人女伴身分赴書商宴。
蘇清已接下蕭峰×阿朱第一個連載企劃，並答應今晚出席。
應伯爵在外尋兩家書商。
浮香是主要邀請的清倌；紫蘭若有空且本人願意，可一同入席；兩人尚未確認。

班富蘭身上已有兩方新印：
「富蘭克林」中文小方印，及「Franklin」長形圖記印。

今晚的目標不是查盜版，而是第一次把：
故事 × 詞 × 曲 × 唱 × 正版出版
真正放到同一張桌上談。

玩家另有一名尚未公開的預定邀請對象，Director 不得猜。

下一輪可在合法時間推進下進入傍晚／晚宴準備；不得把待邀人物自動寫成已到場。
```

---

# 14｜SAVE AUTHORIZATION / EXECUTION BOUNDARY

```yaml
SAVE_COMMIT:
  human_authorization:
    source: "USER EXPLICIT: 'OK 導演 我們可以HOT SAVE 然後準備進晚上了'"
    status: true

  document_level_hot_save:
    status: "COMPLETED"
    version: "V1.10"

  host_instrumented_formal_save_execution: "NOT_ESTABLISHED"
  formal_main_receipt: "NOT_CLAIMED"
  e6_e7: "NOT_ESTABLISHED"

  next_story_phase:
    target: "吉月初九傍晚／晚間"
    actual_evening_event_result: "NOT YET GENERATED"
```

# END OF HOT SAVE V1.10
