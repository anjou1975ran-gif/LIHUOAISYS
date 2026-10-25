# 觀止青樓｜白御行線 MASTER SAVE V5.18-HARD
## 截至 HOT V5.18｜E01–E126 全歷史自足硬化整合版｜只保留 HOT V5.19–V5.21 為較新有效疊加層
### SELF-CONTAINED HARD MASTER｜V5.14–V5.18 PROMOTED｜PAIRED RCL V5.18 / SCHEMA V1.1

```yaml
SAVE_META:
  save_id: "GUANZHI_BAIYUXING_MASTER_V5_18_HARD_SELF_CONTAINED_E01_E126"
  title: "觀止青樓｜白御行線 MASTER SAVE"
  version: "V5.18-HARD"
  memory_generation: "V5.18"
  world: "觀止青樓"
  player: "白御行"
  route_status: "ACTIVE"
  record_type: "SELF_CONTAINED_HARD_CONSOLIDATED_MASTER"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  document_date: "2026-09-15"
  fixed_calendar_anchor: "理火三年槐月五日｜永恆第一夜"
  master_cutoff: "理火三年荷月初三清晨｜HOT V5.18"
  last_canonical_master_event: "E126"
  parent_master:
    file: "觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md"
    version: "V5.13-R1-HARD"
    sha256: "19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5"
    status: "VALID_PARENT / SUPERSEDED_AS_CURRENT_MASTER"
    treatment: "PROVENANCE / ROLLBACK / REGRESSION"
  parent_rcl:
    file: "觀止青樓_白御行線_人物履歷_RCL_V5.13-R1_MASTER_E01-E121_SCHEMA_V1.1_62人對齊版.md"
    version: "V5.13-R1"
    schema: "GUANZHI_RCL_SCHEMA_V1_1"
    sha256: "b74c78cbbde9647191008b5314d01ccf1a2ccfca0c4699a197700633db4da8d0"
    treatment: "VALID_PARENT / READ-ONLY PROVENANCE"
  promoted_hot_chain:
    - "HOT V5.14 -> E122"
    - "HOT V5.15 -> E123"
    - "HOT V5.16 -> E124"
    - "HOT V5.17 -> E125"
    - "HOT V5.18 -> E126"
  retained_as_newer_hot_overlay:
    - "HOT V5.19"
    - "HOT V5.20"
    - "HOT V5.21"
  paired_rcl:
    file: "觀止青樓_白御行線_人物履歷_RCL_V5.18_MASTER_E01-E126_SCHEMA_V1.1_65人對齊版.md"
    memory_generation: "V5.18"
    schema: "GUANZHI_RCL_SCHEMA_V1_1"
    status: "REQUIRED SAME-GENERATION OUTPUT"
SELF_CONTAINMENT:
  canonical_event_range: "E01-E126"
  old_master_chain_runtime_dependency: false
  raw_hot_v5_14_to_v5_18_required_for_normal_resume: false
  raw_hot_v5_14_to_v5_18_role: "SOURCE_PROVENANCE / DETAIL_FALLBACK / AUDIT"
CURRENT_ROUTE_RESUME_RULE:
  normal_resume:
    1: "本 MASTER V5.18-HARD"
    2: "paired RCL V5.18 / schema V1.1"
    3: "HOT V5.19"
    4: "HOT V5.20"
    5: "HOT V5.21"
  note:
    - "HOT V5.14–V5.18 已被本 MASTER 吸收，不再是 Normal STORY 必載 overlay。"
    - "Normal STORY 只保留三個 post-MASTER HOT：V5.19、V5.20、V5.21。"
    - "需要逐句／原始交易／特定知情矩陣時，可回查被吸收 HOT 作 provenance / detail fallback。"
```

---

# 0｜MASTER V5.18 固化決定

```yaml
GM_COMMIT_DECISION_V5_18:
  explicit_request:
    - "HOT SAVE。"
    - "MASTER SAVE 推進到 V5.18。"
  legal_interpretation:
    - "現行最新 HOT 在本輪編譯為 V5.21；MASTER cutoff 依玩家明示只推進到 HOT V5.18。"
    - "E01–E121 全量繼承自 MASTER V5.13-R1-HARD。"
    - "HOT V5.14、V5.15、V5.16、V5.17、V5.18 分別固化為 E122–E126。"
    - "HOT V5.19、V5.20、V5.21 晚於本 MASTER cutoff，只作三個較新 overlay，不倒灌 V5.18 時點。"
    - "依 Core V15.4，MASTER promotion 同步產生同代 RCL V5.18 / schema V1.1。"
SAVE_DISCIPLINE_V5_18_MASTER:
  - "只固化已發生、可觀察、本人明示、正式帳目／契約可核對，或 GM／玩家的有效校正。"
  - "UNKNOWN / PENDING / DISPUTED / NOT_YET_OCCURRED 保持合法。"
  - "成人事件、關係、同意、生殖後果分軸保存。"
  - "PUBLIC EVENT != EXTERNAL PUBLICATION。"
  - "較新 HOT V5.19–V5.21 不得倒灌到 HOT V5.18 cutoff。"
```

---

# 1｜HARD READ ORDER

```yaml
HARD_READ_ORDER_V5_18:
  event_history: ["本檔 E01–E126"]
  current_state_at_cutoff: ["第 5 區 MASTER V5.18 CURRENT HARD STATE"]
  paired_character_ledger: ["觀止青樓_白御行線_人物履歷_RCL_V5.18_MASTER_E01-E126_SCHEMA_V1.1_65人對齊版.md"]
  later_than_cutoff: ["HOT V5.19", "HOT V5.20", "HOT V5.21"]
  precedence:
    - "E01–E121 讀繼承事件歷史。"
    - "E122–E126 讀本版 promoted events。"
    - "截至 HOT V5.18 的當前狀態讀 CURRENT HARD STATE。"
    - "人物截至 cutoff 的 Route state 讀 paired RCL V5.18；需要原因／細節回 MASTER E##。"
    - "V5.18 之後依序疊 HOT V5.19 → V5.20 → V5.21。"
```

---
# 2｜E01–E113 + V5.5 歷史硬切面【逐字繼承 parent，可自足回查】

> 下列內容取自 MASTER V5.5-R2-HARD。  
> 其中 E01–E113 仍為本 MASTER 的正式事件歷史；原「HOT V5.5 CURRENT HARD STATE」已改標為 **ARCHIVE-5**，只作歷史截止切面，不再具有 current-state 法位。


# 1｜來源衝突與永久資訊邊界

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



---

# 2｜白御行 PLAYER HARD STATE

## 2. 白御行角色硬設定（PLAYER HARD STATE）

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

> 本區沿用早期已固化的玩家自述／硬設定；若未來玩家本人明示校正，以最新明示為準。本區不替玩家新增內心、價值判定或未說過的履歷。

---

# 3｜PRIVATE SECRET ARCHIVE｜私人秘密硬封存

## PRIVATE_SECRET_ARCHIVE｜白御行線私人秘密封存

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

### PSE-WY-ZLH-001｜白御行向張麗華揭露自身過去

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

### MASTER 固化狀態

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

---

# 4｜E01–E113 SELF-CONTAINED CAUSAL EVENT LEDGER

## 4.0 Event Ledger 規則

```yaml
EVENT_LEDGER_RULE:
  unique_event_ids: "E01-E113"
  event_occurrence_is_historical: true
  later_state_may_change: true
  later_state_does_not_erase_occurrence: true
  macro_event_not_equal_to_unwritten_detail: true
  relation_consent_knowledge_not_inferred_from_headline: true
```

## E01｜第一夜：無名客入觀止、辭歲與浮香
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E02｜第二夜：辭歲包廂拒絕與張麗華初登場
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E03｜張麗華第一次婚約：五千、一萬五千與一萬訂金
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E04｜一萬兩三日懸賞與「無路，無解」
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E05｜一萬兩轉為張麗華酒錢
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E06｜蘇清五百兩三晚交易：事實修正版
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E07｜第五夜開場：張麗華、酒與子時條件
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E08｜辭歲二十八日心理奴化提案被拒
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E09｜浮香第五夜：琴、琴坊與雙向排他
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E10｜十三娘問心賭局
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E11｜白御行家眷與三名正式妻子公開
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E12｜似伊影像與紅袖可能未來
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E13｜三十年女兒紅、《不得飲》與公開官人稱呼
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E14｜女兒紅來源與最後一罈競局
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E15｜李清照《一剪梅》與白御行四言長詩
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E16｜歪詩局與《玉樹後庭花》補句
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E17｜酒莊、薔薇、三烤鹽與定陶商會婚議升級
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E18｜陳叔寶、地府與張麗華去留爭論
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E19｜宋仁宗評價、權力限制與觀止理念
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E20｜柳如煙概念體、李師師與趙受益花魁局
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E21｜顧北辰霸總劇：巴掌、白月光與豬隊友
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E22｜顧家豪門宴戲
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E23｜無名信與白玉池美女事件
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E24｜似伊實體入場與退場
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E25｜白御行給紅袖的建議與如夫人邀請
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E26｜仁宗朝夜談：天章閣、馬吊與歷史會計帳
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E27｜假醉進張麗華房間與私人關係提案
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E28｜傳聞與話本操盤計畫
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E29｜自由意志、選擇環境與時間窗口爭論
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E30｜第五夜善後與人物去留
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E31｜張麗華穿衣陪睡完成
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E32｜李清照返回自身時代
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E33｜李師師選擇留在觀止並採設席牌
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E34｜後堂地道出現與趙受益抵達
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E35｜紅娘氏第一筆紅倌交易
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E36｜白御行離開後堂
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

```yaml
EVENT_RECORD:
  event_id: "E36"
  story_time: "理火三年槐月十一日清晨"
  participant: "白御行"
  action: "笑著打開扇子，離開當前後堂場景"
  destination: "UNKNOWN_PLAYER_OWNED"
  status: "SCENE_EXIT_CONFIRMED"
```

---

## E37｜小翠拒絕八百兩安排
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E38｜李師師與師理理身份規則確認
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E39｜師理理開放白御行追求可能
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E40｜白御行向紅娘氏購買情報
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E41｜小翠熟客安全計畫提出
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E42｜白三娘老帶新方案接受
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E43｜紅娘氏與小翠紅綠雙飛組提案
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E44｜紅綠雙飛宣傳海報完成
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E45｜深夜休息節點
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md`

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

---

## E46｜李師師／師理理第一次完整性交
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E47｜疼痛界線、事後停留與私人記憶
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E48｜錯過再會、十二香皂與新招數欠帳
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E49｜定陶十二車三烤鹽失竊與全數找回
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E50｜第一告密者受保護與領賞
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E51｜石魁、灰簿先生與吳六未決
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E52｜三烤停售、六烤倍價與銀庫防守
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E53｜隨機交叉審計與急難護持案
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E54｜涉案者押回定陶、補假與調查授權
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E55｜張麗華明示接受情人關係
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E56｜李師師嫉妒、私人稱呼與槐月十五日晚共處
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E57｜阿泠現身與白玉池水療提案
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E58｜李瓶兒入池與追求機會未關閉
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E59｜白玉池「歸零」、算式與續字回顯
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E60｜白玉池封池、蘇清研究與潘金蓮尚未介入之初始狀態
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E61｜李師師共宿、停止權校正與清晨射精
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E62｜張麗華花燭當日確認與時辰
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E63｜續字化為黑色門縫與對側互動
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E64｜時空道人承認漏籤
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E65｜活物與事件傳遞測試
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E66｜黑影分離、門後自行選擇與暫閉合
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E67｜阿泠兄妹方向仍未成立
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E68｜商會授權與蘇清、小翠浴房邊界
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E69｜花燭前休息
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E70｜張麗華酒莊交接與管理入口
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E71｜觀止餐飲改良但不開平價早餐鋪
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E72｜李瓶兒之秘密關係提案未接受
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E73｜張麗華三日陪伴線
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E74｜四人火鍋家宴
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E75｜房內兩日「家人」框架
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E76｜李瓶兒接受當晚留宿
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E77｜寢具用品準備與親密未決
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md`

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

---

## E78｜HOT V2.0：四人夜結與兩日關係分軸
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md`

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

---

## E79｜HOT V2.1：定陶商戰、蘇清私約與白玉池補固
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md`

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

---

## E80｜HOT V2.2：師師如夫人前置、七色肚兜與張麗華獨宿夜
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md`

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

---

## E81｜HOT V2.3：定陶—沈萬三合作與多線案件升級
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md`

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

---

## E82｜HOT V2.4：風滿樓、西門暗櫃與五千後算
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md`

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

---

## E83｜HOT V2.5：開封法網、阿麗婭重定義與六條來訪
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md`

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

---

## E84｜京師軍械案鏡頭收網、觀止民事戰重啟、許慎言七十二小時按摩券
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md`

```yaml
MASTER_EVENT:
  event_id: E84
  source: HOT V2.6
  status: SOLIDIFIED
  confirmed_core:
  - 京師軍械／御前營造／權臣大案的觀止主鏡頭正式收網：刑名交開封府、政治處置交皇帝；這是鏡頭退出，不等於所有國家案件均終局。
  - 觀止核心重新回到蘇清、潘金蓮、西門慶、廣源、柳生／高衙內等民事與責任線；不得因國家大案吸附而把它們誤寫成 CLOSED。
  - 許慎言恢復蘇清 principal lawyer 法位；定陶出資的七十二小時按摩體驗券贈與許慎言，青禾開始提供分次扣時之按摩／恢復服務。
  - 趙氏三帝到觀止、皇帝照價付費與不因護駕清場等玩家線政治事件有效，但不回寫一般歷史基線。
```

---

## E85｜潘金蓮返樓、五千原款重分類、五萬索賠、身籍與重新掛牌條件式討論
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md`

```yaml
MASTER_EVENT:
  event_id: E85
  source: HOT V2.7
  status: SOLIDIFIED
  confirmed_core:
  - 潘金蓮由開封府查問線實際返回觀止；不是刑事無罪終判，也不是永久免傳。
  - 五千舊款在觀止內部被重新分類為待返還／司法保全款；截至本 HOT 尚未完成實銀交付。
  - 蘇清／許慎言把五萬兩列為對潘金蓮個人民事賠償的起始請求；當時仍是請求，未判、潘未認責。
  - 潘金蓮身籍／身契來源案啟動；白御行一千兩一夜只是其未來合法重新掛牌且本人自願時的條件式意向價，沒有成交、預約或性同意。
  - 高額、長期、涉及人物身體／身分之交易需要更高治理與本人明示；不得只靠單一掌櫃定價把人物當成已同意。
```

---

## E86｜潘身籍副冊補證、白玉池許願幣／定存框架、師師道歉修復與如夫人再確認
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md`

```yaml
MASTER_EVENT:
  event_id: E86
  source: HOT V2.8
  status: SOLIDIFIED
  confirmed_core:
  - 潘金蓮身籍副冊出現較強補證：較早依附標記有「舊附籍銷，從夫戶」痕跡，後續副冊列武大戶內之妻；沒有官冊支持武松繼承潘金蓮身契。其進西門家與現今從妓資格仍待查。
  - 白玉池本日只完成非正式再檢；水面／修補處未見新異常，但仍為 RESTRICTED_NOT_FORMALLY_REOPENED。
  - 阿泠接受許願幣所有權與一年 3.5% 定存利率框架；許願幣材質、匯率、實際存入、正式契約、備付與放貸均尚未完成。
  - 白御行向李師師跪歉；李師師明示原諒但不抹除過去，並再次明示想要如夫人位置。該位置仍未公開／登記／法定實施。
  - 李師師接受未來李瓶兒在身分乾淨後可與她並列如夫人的原則；只是師師的接受，不等於李瓶兒已正式入白家。
```

---

## E87｜曹州假印立案、定陶總會架構、京師女性時尚企畫、師師抱睡
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md`

```yaml
MASTER_EVENT:
  event_id: E87
  source: HOT V2.9
  status: SOLIDIFIED
  confirmed_core:
  - 槐月二十一日晚宴已實際發生；李瓶兒晚宴後未成立留宿或三人成人事件。白御行疲累後由李師師抱睡，當晚明示不挑逗，場景為非性陪睡。
  - 曹州程姓商人假印／冒名採辦案進入定陶總會內部正式流程；顧青簡成為本玩家線程序端師爺／路線 NPC。
  - 定陶總會架構被明示為多商團聯邦式網絡：地方自負盈虧、總會維護跨團通路／信用／技術授權等；京師被白御行定位為時空商路總會樞紐。
  - 李師師肚兜代言擴張成女性主導的服裝／發表會、人物專屬款與京師女性奢侈品旗艦／批發構想；均為提案，未自動簽約、選址或取得外來女性同意。
```

---

## E88｜女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md`

```yaml
MASTER_EVENT:
  event_id: E88
  source: HOT V3.0
  status: SOLIDIFIED
  confirmed_core:
  - 定陶總會直轄的女性注意力事業秘密模型成立於玩家線：每城可有四十八人架構、神七／御三家、跨城總選等；候選入場不代表知道完整商業戰略。
  - 風滿樓大型遴選啟動；白御行不主導選人，讓潘金蓮、李師師、蘇清、疏影、白三娘、白希等從不同面向評估。
  - 白御行私人取得白三十二娘、白明礬、白紅伶、白希四名成年持契人員，四人契價合計一千一百二十五兩；「四大金剛」只是玩笑稱呼。
  - 四人對李師師稱「白夫人」，並接受其白家內部日常調度；對張麗華稱「麗華夫人」，可協助小事但重大契約／財物／對外承諾不由她任意決定。
  - 上述夫人稱謂是白御行線內部權限與禮數，不等於法律婚姻程序已完成。
```

---

## E89｜風滿樓第二日遴選、十一名候選分流、牙行責任、白宅十年條件式協議
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md`

```yaml
MASTER_EVENT:
  event_id: E89
  source: HOT V3.1
  status: SOLIDIFIED
  confirmed_core:
  - 白宅形成八千兩／十年之條件式租用框架；空間穩定性、實際入住與正式租金啟動仍需後續成立。
  - 風滿樓第二日大型遴選進行；十一名成年候選被允許依自身意願分成退出 2、明確往前 4、未決 5；往前不等於同意行房，退出也不自動等於自由身。
  - 退出者各獲十兩補貼；牙行對「處子」等標示之文書／揭露責任被拉上檯面。
  - 十八歲六百兩候選在此 HOT 尚未成交；她本人自述未與男人行房、拒絕以落紅驗貨，並要求若成交至少五十兩直接歸本人。
  - 辭歲人物資料在本 HOT 曾被標記需回查／修正；後續人物池 V2.2 為較新基線來源，不得把待修舊敘述升格成固定人格。
```

---

## E90｜小翠同床純睡、三月集訓與走秀換約、六百兩候選條款、白宅設計啟動
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md`

```yaml
MASTER_EVENT:
  event_id: E90
  source: HOT V3.2
  status: SOLIDIFIED
  confirmed_core:
  - 大型人才遴選退出主舞台，進入潘金蓮等制度化收尾。
  - 小翠在自己房／自己的床自願讓白御行同床純睡，設定可撤回、指定接觸位置與「只是睡」等邊界；當夜沒有性交、口交、手交或已成立生殖器接觸。
  - 六百兩十八歲候選之原則條件進一步固定為牙行五百五十兩＋本人五十兩，未來若本人自願進正式出閣拍賣，白御行另提出成交額 15% 給她；最終交割手續在此 HOT 尚未硬確認。
  - 本批新人採三個月觀止訓練制；三個月後走秀作為第一期驗收與觀止約→商會約的集體換約節點。處子前三個月不辦正式初夜拍賣。
  - 白宅由李師師先做生活／功能第一輪設計，含主屋、師師院、麗華偶居、浴房、更衣、庫房、議事、宴會廳等；尚未建成。
  - 白御行與李師師的免費床賭局在此時進入活躍階段；床位勝負與是否發生成人性行為分開。
```

---

## E91｜浮香自願給床與成人夜、紅娘煙幕揭穿、九幽帝皇聯誼會正式訂單
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md`

```yaml
MASTER_EVENT:
  event_id: E91
  source: HOT V3.3
  status: SOLIDIFIED
  confirmed_core:
  - 浮香在無付款、無安排、無權力施壓下，自主讓白御行留在自己的房與自己的床；其後另有雙方成年人親密事件，床位與成人親密分軸成立。
  - 紅娘被白御行作為免費床賭局煙幕；白紅伶散播「紅娘免費全套」等話是刻意假傳聞。白御行當夜未去紅娘房，不能把傳聞寫成實際免費性服務。
  - 鬼差將九幽帝皇聯誼會給觀止／潘金蓮的正式訂單送達；不是私人請帖。三日後十餘名皇帝預定在大觀樓舉行家族交接／見證大會。
  - 大觀樓是二樓中央大圓桌、約二十至三十人之高規格宴席空間；不可再與千人級風滿樓混同。
  - 潘金蓮收到訂單並開始籌備；公帳由帝皇聯誼會支付、白御行有審帳權，但最高核銷額與完整菜單／姑娘／房間／拍賣均未在此 HOT 全部成立。
  - 三輪重量級拍賣等只屬白御行盤算；沒有自動取得任何女性本人同意。
```

---

## E92｜帝皇宴前置、十三娘國運賭桌線、兩局免費床結算、紅娘側賭敗、小翠三娘實習與三人抱睡
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md`

```yaml
MASTER_EVENT:
  event_id: E92
  source: HOT V3.4
  status: SOLIDIFIED_MASTER_CUTOFF
  confirmed_core:
  - 十三娘豹子賭局由小翠合法擲出 1-6-6，白御行敗；他依約交付國運／城隍司估價／首飾儲存等頂級幸運路徑情報。十三娘沒有輸掉自己的成人賭注。
  - 浮香第一局免費床已由李師師正式認輸；不得再寫成尚待結算。
  - 第二局免費床以白三娘自願借自己的床、小翠自願把白御行當「大件行李」帶上床成立；白三娘知情、不收費、不受命令，李師師亦正式認輸。
  - 紅娘因第二局白御行獲勝而輸掉側賭；在 V3.4 截止時形成一次未來可執行的免費三人親密賭債，但仍不是 blanket 性同意，李師師與紅娘均保留當下界線。
  - 白三娘房內有白三娘與白御行之成年人親密事件；小翠自行選擇進入有限、可隨時停止的小段實習／觀察，不能改寫成完成性交或固定雙人服務。
  - 小翠自行宣告今晚學夠、停止實習；最後白御行抱小翠、白三娘從後抱白御行，三人停止成人互動後安靜入睡。
```

---

---

## E93｜九幽帝皇聯誼會散場、辭歲／錦棠雙姝天價競拍、白玉池帝皇團特殊試營運、帝皇多線自然分流
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.4-R1_截至HOT_V4.0固化_保留V4.1-V4.4_HOT版.md`

```yaml
MASTER_EVENT:
  event_id: "E93"
  source: "HOT V3.5"
  status: "SOLIDIFIED"
  confirmed_core:
    - "九幽帝皇聯誼會散場、辭歲／錦棠雙姝天價競拍、白玉池帝皇團特殊試營運、帝皇多線自然分流"
  detail_policy:
    - "本 HARD MASTER 保存 MASTER 級宏事件；逐句／逐項原始細節如需回查，以對應 HOT 原檔為 detail fallback。"
    - "不得把宏事件標題外推成未記錄的關係、同意、知情或帳務結果。"
```

---

## E94｜榴月一日十日整修起點、雙姝款項／身份翻轉、朱明欠單與鄭成功週轉僅預案、六條／趙受益成人結果與污染校正
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.4-R1_截至HOT_V4.0固化_保留V4.1-V4.4_HOT版.md`

```yaml
MASTER_EVENT:
  event_id: "E94"
  source: "HOT V3.6-R2"
  status: "SOLIDIFIED"
  confirmed_core:
    - "榴月一日十日整修起點、雙姝款項／身份翻轉、朱明欠單與鄭成功週轉僅預案、六條／趙受益成人結果與污染校正"
  detail_policy:
    - "本 HARD MASTER 保存 MASTER 級宏事件；逐句／逐項原始細節如需回查，以對應 HOT 原檔為 detail fallback。"
    - "不得把宏事件標題外推成未記錄的關係、同意、知情或帳務結果。"
```

---

## E95｜辭歲／錦棠／李瓶兒私人開戶、紅袖五十萬反向價格尺與召喚權、紅娘門窗屏風換債、趙受益六條夜集外出
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.4-R1_截至HOT_V4.0固化_保留V4.1-V4.4_HOT版.md`

```yaml
MASTER_EVENT:
  event_id: "E95"
  source: "HOT V3.7"
  status: "SOLIDIFIED"
  confirmed_core:
    - "辭歲／錦棠／李瓶兒私人開戶、紅袖五十萬反向價格尺與召喚權、紅娘門窗屏風換債、趙受益六條夜集外出"
  detail_policy:
    - "本 HARD MASTER 保存 MASTER 級宏事件；逐句／逐項原始細節如需回查，以對應 HOT 原檔為 detail fallback。"
    - "不得把宏事件標題外推成未記錄的關係、同意、知情或帳務結果。"
```

---

## E96｜趙受益六條夜集返樓、楊玉環白玉池與荔枝、李師師晨間補考、定陶票據信用／朱明長債方向／曹州案盤點
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.4-R1_截至HOT_V4.0固化_保留V4.1-V4.4_HOT版.md`

```yaml
MASTER_EVENT:
  event_id: "E96"
  source: "HOT V3.8"
  status: "SOLIDIFIED"
  confirmed_core:
    - "趙受益六條夜集返樓、楊玉環白玉池與荔枝、李師師晨間補考、定陶票據信用／朱明長債方向／曹州案盤點"
  detail_policy:
    - "本 HARD MASTER 保存 MASTER 級宏事件；逐句／逐項原始細節如需回查，以對應 HOT 原檔為 detail fallback。"
    - "不得把宏事件標題外推成未記錄的關係、同意、知情或帳務結果。"
```

---

## E97｜長恨歌文會、柳如是東林夜談、趙受益宣和地道入席、六條／楊玉環雙線追求與三人約會可能性
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.4-R1_截至HOT_V4.0固化_保留V4.1-V4.4_HOT版.md`

```yaml
MASTER_EVENT:
  event_id: "E97"
  source: "HOT V3.9"
  status: "SOLIDIFIED"
  confirmed_core:
    - "長恨歌文會、柳如是東林夜談、趙受益宣和地道入席、六條／楊玉環雙線追求與三人約會可能性"
  detail_policy:
    - "本 HARD MASTER 保存 MASTER 級宏事件；逐句／逐項原始細節如需回查，以對應 HOT 原檔為 detail fallback。"
    - "不得把宏事件標題外推成未記錄的關係、同意、知情或帳務結果。"
```

---

## E98｜三十二娘街行與帳戶指令、紅娘中央籠台演出方案、錦棠首次正式約會、私人成人事件、白御行喜歡明示與相擁收幕
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.4-R1_截至HOT_V4.0固化_保留V4.1-V4.4_HOT版.md`

```yaml
MASTER_EVENT:
  event_id: "E98"
  source: "HOT V4.0"
  status: "SOLIDIFIED"
  confirmed_core:
    - "三十二娘街行與帳戶指令、紅娘中央籠台演出方案、錦棠首次正式約會、私人成人事件、白御行喜歡明示與相擁收幕"
  detail_policy:
    - "本 HARD MASTER 保存 MASTER 級宏事件；逐句／逐項原始細節如需回查，以對應 HOT 原檔為 detail fallback。"
    - "不得把宏事件標題外推成未記錄的關係、同意、知情或帳務結果。"
```

---

## E99｜榴月四日兩牙行二十三名成年候選雙向遴選、九名丫鬟成交分配、制服／自願剪髮方案、白希白明礬初教、十四名落選者吃麵收尾
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.5-R1_截至HOT_V4.5固化_保留V4.6-V5.0_HOT版.md`

```yaml
MASTER_EVENT:
  event_id: "E99"
  source: "HOT V4.1"
  status: "SOLIDIFIED"
  confirmed_core:
    - "榴月四日兩牙行二十三名成年候選雙向遴選、九名丫鬟成交分配、制服／自願剪髮方案、白希白明礬初教、十四名落選者吃麵收尾"
  detail_policy:
    - "本 HARD MASTER 保存 MASTER 級宏事件；逐句／逐項原始細節如需回查，以對應 HOT 原檔為 detail fallback。"
    - "不得把宏事件標題外推成未記錄的關係、同意、知情或帳務結果。"
```

---

## E100｜榴月九日曹州假印案多日追查後止手、疑似何先生今夜借名與材料留存、全員放行、中央籠台試光、女子競技／賭盤／護衛人才入口、榴月十一日開幕流程
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.5-R1_截至HOT_V4.5固化_保留V4.6-V5.0_HOT版.md`

```yaml
MASTER_EVENT:
  event_id: "E100"
  source: "HOT V4.2"
  status: "SOLIDIFIED"
  confirmed_core:
    - "榴月九日曹州假印案多日追查後止手、疑似何先生今夜借名與材料留存、全員放行、中央籠台試光、女子競技／賭盤／護衛人才入口、榴月十一日開幕流程"
  detail_policy:
    - "本 HARD MASTER 保存 MASTER 級宏事件；逐句／逐項原始細節如需回查，以對應 HOT 原檔為 detail fallback。"
    - "不得把宏事件標題外推成未記錄的關係、同意、知情或帳務結果。"
```

---

## E101｜榴月十日開幕前夕、辭歲五百萬五年五分定存、師師月事未至孕否未知、商會女人培訓目的鎖、小翠首次完整成人事件、三人同睡收尾
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.5-R1_截至HOT_V4.5固化_保留V4.6-V5.0_HOT版.md`

```yaml
MASTER_EVENT:
  event_id: "E101"
  source: "HOT V4.3"
  status: "SOLIDIFIED"
  confirmed_core:
    - "榴月十日開幕前夕、辭歲五百萬五年五分定存、師師月事未至孕否未知、商會女人培訓目的鎖、小翠首次完整成人事件、三人同睡收尾"
  detail_policy:
    - "本 HARD MASTER 保存 MASTER 級宏事件；逐句／逐項原始細節如需回查，以對應 HOT 原檔為 detail fallback。"
    - "不得把宏事件標題外推成未記錄的關係、同意、知情或帳務結果。"
```

---

## E102｜榴月十一日晚重新開幕完成、女子競技與紅娘壓軸、顧三辭歲再會、趙受益二百兩購四契再贈六條／楊玉環、四大金剛＋李清照女客試場、白玉池會員制接受、錦棠同宿
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.5-R1_截至HOT_V4.5固化_保留V4.6-V5.0_HOT版.md`

```yaml
MASTER_EVENT:
  event_id: "E102"
  source: "HOT V4.4"
  status: "SOLIDIFIED"
  confirmed_core:
    - "榴月十一日晚重新開幕完成、女子競技與紅娘壓軸、顧三辭歲再會、趙受益二百兩購四契再贈六條／楊玉環、四大金剛＋李清照女客試場、白玉池會員制接受、錦棠同宿"
  detail_policy:
    - "本 HARD MASTER 保存 MASTER 級宏事件；逐句／逐項原始細節如需回查，以對應 HOT 原檔為 detail fallback。"
    - "不得把宏事件標題外推成未記錄的關係、同意、知情或帳務結果。"
```

---

## E103｜榴月十二日晚白家採購規劃、蘇清十八日商會工拆帳、妓籍終身法位鎖、阿莉婭處女拍賣標的與紅娘雙人場、三十二娘妓籍申請、楊玉環白玉池代言首夜、黑公子×小桃百兩交易與同宿意向
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V4.5-R1_截至HOT_V4.5固化_保留V4.6-V5.0_HOT版.md`

```yaml
MASTER_EVENT:
  event_id: "E103"
  source: "HOT V4.5"
  status: "SOLIDIFIED"
  confirmed_core:
    - "榴月十二日晚白家採購規劃、蘇清十八日商會工拆帳、妓籍終身法位鎖、阿莉婭處女拍賣標的與紅娘雙人場、三十二娘妓籍申請、楊玉環白玉池代言首夜、黑公子×小桃百兩交易與同宿意向"
  detail_policy:
    - "本 HARD MASTER 保存 MASTER 級宏事件；逐句／逐項原始細節如需回查，以對應 HOT 原檔為 detail fallback。"
    - "不得把宏事件標題外推成未記錄的關係、同意、知情或帳務結果。"
```

---

## E104｜HOT V4.6｜榴月十三日晚
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V5.1-R1_截至HOT_V5.1固化_保留V5.2-V5.5_HOT版.md`

```yaml
E104:
    source: "HOT V4.6｜榴月十三日晚"
    summary:
      - "蘇清十八日商會工作正式起算。"
      - "白玉池白御行×楊玉環私人成人事件成立。"
      - "魚玄機首次正式進白御行線並自主登中央籠台。"
      - "紅袖／浮香成人適應事件與三日賭約成立。"
      - "白御行當夜在浮香房單純就寢。"
  status: "SOLIDIFIED"
```

---

## E105｜HOT V4.7｜榴月十四日晚
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V5.1-R1_截至HOT_V5.1固化_保留V5.2-V5.5_HOT版.md`

```yaml
E105:
    source: "HOT V4.7｜榴月十四日晚"
    summary:
      - "白家正式顯影落地並開始入住。"
      - "李師師孕疑升高但未確診。"
      - "白家主樓、師師／瓶兒平級如夫人、麗華與浮香外院等空間法位鎖定。"
      - "入住家宴成立；女客夜開始正式籌備。"
  status: "SOLIDIFIED"
```

---

## E106｜HOT V4.8｜榴月十五日下午
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V5.1-R1_截至HOT_V5.1固化_保留V5.2-V5.5_HOT版.md`

```yaml
E106:
    source: "HOT V4.8｜榴月十五日下午"
    summary:
      - "白家第一夜五人共眠完成；不自動生成後續成人關係。"
      - "白家窗簾／巨型暖炕等生活改造方向成立。"
      - "女客夜營運規則正式鎖定。"
      - "蘇東坡、陳季常、佛印提前抵達；最大自由包廂預留。"
  status: "SOLIDIFIED"
```

---

## E107｜HOT V4.9｜榴月十五日晚
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V5.1-R1_截至HOT_V5.1固化_保留V5.2-V5.5_HOT版.md`

```yaml
E107:
    source: "HOT V4.9｜榴月十五日晚"
    summary:
      - "女客夜正式開場並形成自由流動大包廂。"
      - "匿名薛濤進線但白御行未知其真身。"
      - "白御行與梅花面具成年紅線女客完成一次自願露水成人事件。"
      - "陳季常與金面具女客自主進房；身份與房內內容 UNKNOWN。"
      - "蘇東坡×魚玄機互動升溫；佛印女客圍桌；男客自薦施粥台形成。"
  status: "SOLIDIFIED"
```

---

## E108｜HOT V5.0｜榴月十六日下午
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V5.1-R1_截至HOT_V5.1固化_保留V5.2-V5.5_HOT版.md`

```yaml
E108:
    source: "HOT V5.0｜榴月十六日下午"
    summary:
      - "女客夜後段施粥慈善台收束。"
      - "白御行×紅娘施粥影戲成人場成立；後續同宿紅娘房。"
      - "紅娘在白玉池得知白御行×楊玉環既往私人成人秘密。"
      - "楊玉環×紅娘當場成人較勁只成立當下自願，不固化勝負／戀愛。"
      - "白御行與紅娘成立六條十日賭約：以白御行能否在期限內與六條形成指定成人結果為條件；賭局不能取得六條同意權。"
      - "白御行返白家，張麗華對前夜舞台部分結果提供第二來源證詞。"
  status: "SOLIDIFIED"
```

---

## E109｜HOT V5.1｜榴月十八日晚
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V5.1-R1_截至HOT_V5.1固化_保留V5.2-V5.5_HOT版.md`

```yaml
E109:
    source: "HOT V5.1｜榴月十八日晚"
    summary:
      - "紅袖／浮香三日賭約在期限前收束。"
      - "李師師疑似有喜再升高，但仍未達確診。"
      - "六條私茶確認她知道十日賭存在，但她不是賭注，也不受賭局倒逼。"
      - "顧青簡／清簡榴月十七日晚第一次成人事件與同夜第二次成人事件成立；『顧師爺』公開人格與『清簡』私密面向分層。"
      - "商會秘書房、牙行高階人才培訓與女性市場／主題房形成可發展商業構想，尚未全部落地。"
      - "榴月十八日晚白御行約潘金蓮到帳房；兩人成人挑逗／小試與白家抓姦惡作劇、公審成立。"
      - "潘金蓮局部拒絕被保留；三十二娘襪子堵嘴沒有實際執行。"
      - "潘金蓮同意後，白御行與潘金蓮同入大竹籠移至白玉池；阿泠首次以水罩包覆竹籠，短暫成功。"
      - "《白夫人夜捉潘狐狸》作為公開戲碼散場；白御行與白家眾人返家。"
  status: "SOLIDIFIED"
```

---

## E110｜HOT V5.2｜榴月十九日晚
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V5.5-R1_截至HOT_V5.5固化_保留V5.6-V5.7_HOT版.md`

```yaml
E110:
    source: "HOT V5.2｜榴月十九日晚"
    summary:
      - "蘇清商會貼身衣物／月事用品實穿繼續；至少三名成年女性自願實穿月事用品並回報位移、鬆緊與活動穩定。"
      - "定陶商會京師總部啟動一月女性穿著內部票選；性感肚兜／一片裙只限成年女性自願內部試穿。"
      - "秘書分級、既有人員再訓、定陶商會人才進修院仍屬 PROPOSAL；顧青簡承接年輕成年男服務員招募，尚未正式錄取。"
      - "白家浮香小居形成外置熱煙道抽風＋冷水進氣降溫原型；兩名工匠已找到，截止本 HOT 尚未確認勘察／施工完成。"
      - "魚玄機在中央籠台『馬』題詩賽以13桌比10桌勝洛陽馬商；勝者要求次日晚只看灰青難馬，不承諾摸、牽、騎、馴。"
      - "魚玄機身份校正為成年紅線女客；不是觀止妓籍、不是掛牌工作者。"
      - "桃枝陪席契約爭議促成『開放續約』營運實務：新需求須由女人本人重新決定服務、時間與價格；原契約不自動生成成人服務。"
      - "新紅線女客沈夫人／程小姐入場；公開假想選擇沈夫人18、程小姐15，沈夫人實收白御行10兩獎金。"
      - "沈夫人與白御行在白家完成一次雙方自願、一夜型成人事件；只限兩人，事後無第二次義務、無戀愛／情婦／婚姻／排他。"
      - "程小姐留在樓下，沒有參與成人事件；她對自己若當時是否會上樓回答『不知道』。"
      - "沈、程離開後，李瓶兒與白御行完成第一次真正兩人關門的私人成人夜；當下同意成立，不建立未來 blanket consent。"
      - "李瓶兒給白御行的私密影像／照片只限白御行觀看，不得外傳；不倒灌人物卡固定外貌或服裝。"
  status: "SOLIDIFIED"
```

---

## E111｜HOT V5.3｜榴月二十日白日
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V5.5-R1_截至HOT_V5.5固化_保留V5.6-V5.7_HOT版.md`

```yaml
E111:
    source: "HOT V5.3｜榴月二十日白日"
    summary:
      - "李瓶兒與白御行清晨再次完成雙方自願成人事件；體內射精成立，受孕／懷孕 UNKNOWN。"
      - "浮香降溫原型的兩名工匠已到白家；勘察結果、尺寸、施工、效果仍未建立。"
      - "灰青難馬提前抵達附近馬房，已有踢人、掀槽、咬馬等危險行為報告；馬商承擔馬房費，白御行未接管，魚玄機原約仍只限『看』。"
      - "觀止大堂出現一名陌生中年男人長時間觀察籠台、樓梯、欄杆與出入口；龐春梅已注意，身份與目的保持 UNKNOWN。"
      - "白御行進六條私人房躲白日；兩人玩五子棋、枕腿、清耳，並形成六條房和式／榻榻米平台改造 PROPOSAL；六條保留房間最終設計權。"
      - "六條與白御行在六條房完成本玩家線首次雙方自願成人性交事件；六條多次局部允許、阻止、改位與重新允許均有效。"
      - "六條本日明示對白御行有當下成人慾望；角色表演不改寫她永久人格。"
      - "該次房內成人事件有兩次已確認體內射精；受孕／懷孕 UNKNOWN；沒有重大傷勢。"
      - "六條十日賭約條件因六條本人自願事件而客觀成立：白御行勝；六條不是賭約當事人，也不是替賭局履約。"
      - "原賭白勝彩頭為紅娘房門扇／窗扇再拆十日；截止 V5.3 義務 DUE_NOT_EXECUTED，紅娘尚不知白已勝。"
      - "白御行告訴六條自己與楊玉環既往成人秘密，並宣稱楊玉環曾共同下注／想看六條『下賤』；後兩者此時仍只有白御行 testimony。"
      - "未名小丫鬟只看見白御行從六條房走出，沒有看見房內事件，也尚未形成傳聞。"
  status: "SOLIDIFIED"
```

---

## E112｜HOT V5.4｜榴月二十日白日
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V5.5-R1_截至HOT_V5.5固化_保留V5.6-V5.7_HOT版.md`

```yaml
E112:
    source: "HOT V5.4｜榴月二十日白日"
    summary:
      - "白御行轉往白玉池；楊玉環先在，六條後到，阿泠在場，四人就原十日賭與三人成人方向正面核對。"
      - "楊玉環本人確認：原賭形成時她在場、知道賭約、覺得有趣且沒有反對；她沒有承認自己是正式共同下注人，也沒有承認以羞辱六條為核心動機。"
      - "阿泠以現場見證者身分確認：正式押彩頭者是白御行與紅娘；楊玉環在場，但阿泠沒聽見楊玉環另行下注。"
      - "六條形成『有證據的誤解式理解』：高度傾向認為楊玉環至少在鼓勵／看戲上有份；此為 CHARACTER INTERPRETATION，不是 WORLD FACT。"
      - "楊玉環確認原賭時曾把白御行＋楊玉環＋六條三人成人玩法視為可考慮選項；本日她仍表示目前願意／有興趣，但屬可撤回未來方向。"
      - "六條本輪沒有對未來三人成人事件給出可鎖定明確同意；她不因不拆台、不反對看紅娘被坑而取得成人同意狀態。"
      - "原六條十日賭仍是白御行已勝、紅娘未知、門窗義務 DUE_NOT_EXECUTED。"
      - "白御行與紅娘另立新加碼賭：截止榴月二十二日日出以前，白御行＋楊玉環＋六條必須真正完成三人成人事件，且楊玉環×六條彼此也須自願成立實際成人互動；任何人拒絕／撤回都不能由賭約替代。"
      - "新賭若白御行輸：白御行進觀止大堂鐵籠十日，並在十人大床完成後交紅娘劈解焚毀。"
      - "新賭若紅娘輸：紅娘進大堂鐵籠十日，紅娘既有床劈解焚毀。"
      - "新賭與原賭獨立；新賭不能吞掉原門窗義務。"
      - "新賭真實條件雙方保密，尤其不得公開楊玉環、六條；若紅娘輸，對外可用『白御行與紅娘私下床戰／私人賭局』作 cover story。"
      - "紅娘接受新賭時仍不知道白御行×六條事件、原賭已輸、楊玉環本日現況；新賭勝負仍 PENDING。"
  status: "SOLIDIFIED"
```

---

## E113｜HOT V5.5｜榴月二十四日清晨
> HARD SOURCE MASTER: `觀止青樓_白御行線_MASTER_SAVE_V5.5-R1_截至HOT_V5.5固化_保留V5.6-V5.7_HOT版.md`

```yaml
E113:
    source: "HOT V5.5｜榴月二十四日清晨"
    summary:
      - "浮月閣被 GM 建立為與觀止近似法位的另一時空青樓節點；四大花魁為失仙、失美、失蘿、錯位，已升入當時 LCAPG V2.5 基線。"
      - "失仙在本線入場；導演隱藏真相為浮月閣妖化人名妓、來觀止帶有踢館／比較兩樓本事目的；她對外不揭露來源，個別妖種／真身／能力保持 UNKNOWN。"
      - "觀止出現沈家兩進院落與最深處保留空房：十年樓租60,000兩，另100,000兩守空房；已見1,000兩前押與其後30,000兩首付款併入安排，餘款分期。"
      - "沈家半塊舊木牌與『若另一半木牌持有者來便讓其進空房』家訓成立；等待者身份、年代、生死、來源 UNKNOWN。"
      - "沈家保留空房曾無人操作自行開門一次；門自開是硬事件，原因 UNKNOWN。"
      - "紅娘原賭／新賭結果推進後，至榴月二十三日已在觀止大堂鐵籠公開生活與營業；房中床已搬至籠旁，預定最後一日劈解／焚毀，截止 V5.5 尚未燒。"
      - "紅娘籠內公開邊界成立：看／問可以，手不能伸；曾有醉客伸手被紅娘拒絕並由春梅趕走。"
      - "紅娘與失仙自榴月二十三日起進行九日雙籠營收競賽；只計真實營業收入，純灌票不計；兩人各有錢箱與帳冊。"
      - "九日競賽彩頭：紅娘輸則『觀止首席紅牌』廣告牌交失仙；失仙輸則日後見紅娘低頭承認本局輸。"
      - "白御行與失仙另有一日邀約賭：競賽勝者可日後挑一天邀對方去一個地方；不自動取得第三人、成人或親密內容。"
      - "紅娘 Day 1 形成5兩一蛋、禁止瞄頭臉、集體投蛋與流行梗的公共參與營業模型；至少兩批集體投蛋已發生。"
      - "紅娘另立『剩餘九日不全身清水浴、可酒浴』條件式募款；白御行500兩基礎承諾、現場早期約880兩承諾總額只是 PLEDGE，條件完成前不是營收。"
      - "失仙 Day 1 從20兩一刻的一對一談話，調整為5兩團桌＋20兩獨占一刻；已開始形成回頭客／再約。"
      - "榴月二十三日掌燈時中途盤帳紅娘暫時領先；當晚最終 Day 1 總額與九日總勝負均 UNKNOWN。"
      - "十三娘、蘇小妹、蘇東坡、陳季常、李清照、魚玄機等在雙籠事件中到場；蘇小妹只取得紅線女客識別，拒絕當場登妓籍。"
      - "白御行故意挪李清照『知否，知否，應是綠肥紅瘦』作雙籠競賽梗；李清照到場追來源、標示原詞『我的』並把白改用版稱『贓物』，但認為該比喻有喜劇效果。"
      - "蘇東坡、李清照、蘇小妹現場詞作／演唱為紅娘側帶來額外小費與關注。"
      - "魚玄機接受『49蛋砸紅娘討彩頭／砸晦氣』的娛樂合作，但明示不宣稱改命。"
      - "陳季常預付245兩買49蛋給妻子若願意使用；柳月娥到場實投3蛋，剩46蛋保留，之後帶陳季常回家。"
      - "柳月娥對金面具問題沒有正面承認／否認；其回應使『她可能是女客夜金面具女客』的懷疑顯著升高，但客觀身份仍 UNKNOWN。"
      - "『捉姦保證金』成為潘金蓮認為有營運價值的公開制度 PROPOSAL；金額與正式流程未定。"
      - "秘密『捉姦密室／驚喜抓姦遊戲』仍未公開；曾有導演錯誤洩漏段被玩家 HOLD 撤銷，不形成世界知情。"
      - "白御行榴月二十三日晚躲入醉花陰，確認自己與醉花未來單獨成人關係仍『有』可能；只表示當下興趣，沒有日期／永久承諾。"
      - "白御行當夜裸體睡醉花床外側，醉花內側；兩人整夜無身體接觸、無成人事件。"
  status: "SOLIDIFIED"
```

---

# ARCHIVE-5｜HOT V5.5 HARD STATE SNAPSHOT｜歷史截止切面（非現行；僅作本檔自足基底）

> **本區優先於所有較早 MASTER 截止快照。**
>
> 它回答的是「截至 HOT V5.5 現在成立什麼」，不是重新敘述全部歷史。

## 3｜截至 HOT V5.5 的世界／家庭／觀止硬狀態

```yaml
MASTER_CUTOFF_V5_5:
  date: "理火三年榴月二十四日"
  time: "清晨"
  cutoff_location: "觀止／醉花陰"

  cutoff_scene:
    - "白御行與醉花在醉花陰醒來。"
    - "昨夜兩人同床分側，沒有身體接觸與成人事件。"
    - "樓下開始重新搬桌椅／木架；潘金蓮要求不要堵兩個籠子。"
    - "紅娘清晨已喊著要酒。"
    - "今日新競賽具體規則尚未在 V5.5 演出。"

  white_house:
    state: "FORMALLY_MANIFESTED_AND_IN_USE"
    enduring_structure:
      - "主樓為白御行核心居所。"
      - "李師師、李瓶兒同階如夫人，無主從排序。"
      - "張麗華有獨立外院與酒窖。"
      - "浮香有獨立小居。"
      - "四大金剛輪值屬護衛／勤務，不是成人服務。"

  li_shishi:
    pregnancy_state: "HIGHLY_SUSPECTED_NOT_CONFIRMED"
    lock:
      - "截至 V5.5 仍沒有正式確診，不得寫成已孕。"

  guanzhi:
    enduring:
      - "重新開幕後中央籠台、白玉池、女子競技與女客夜後續營運均為有效世界結構。"
      - "中央籠台已實際承載詩賽、籠居、投蛋、營收競賽等非單一武鬥用途。"
      - "阿泠曾短暫完成水罩包覆竹籠；更大尺度／持續能力仍 UNKNOWN。"

  fuyue_ge:
    world_baseline:
      - "浮月閣是與觀止近似法位的時空青樓節點。"
      - "主要連向妖怪／修行／非人世界。"
      - "失仙、失美、失蘿、錯位為四大花魁。"
    route_visibility:
      - "本線目前只有失仙已實際入場。"
      - "浮月閣來源屬失仙未公開資訊。"

  shen_reserved_courtyard:
    state: "ACTIVE"
    hard_state:
      - "沈家兩進院落已存在。"
      - "最深處保留房必須保持空著，等待另一半木牌持有者。"
      - "四名守院人採兩班值守；已知程素娘、沈秋、老杜，第四人姓名 UNKNOWN。"
      - "空房曾自行開門一次；原因 UNKNOWN。"
```

---

## 4｜人物關係、成人同意、拒絕與契約（截至 HOT V5.5）

```yaml
RELATION_CONSENT_CONTRACT_V5_5:

  bai_li_pinger:
    confirmed_events:
      - "榴月十九日晚兩人完成真正兩人關門的私人成人夜。"
      - "榴月二十日清晨再次完成成人事件並確認體內射精。"
    relation:
      - "李瓶兒在白家有穩定如夫人／女主人位置。"
      - "成人事件不額外建立新的法律名分、排他或永久同意。"
    privacy:
      - "李瓶兒給白御行的私密影像不得外傳。"
    pregnancy:
      - "由榴月二十日事件是否受孕 UNKNOWN。"

  bai_shen_furen:
    event:
      - "榴月十九日晚完成一次自願一夜成人事件。"
    terms:
      - "只限白御行與沈夫人兩人。"
      - "不追問丈夫／住址，不向外炫耀。"
      - "次日離開後沒有第二次義務。"
    relation:
      - "不建立戀愛、情婦、婚姻、排他、未來成人同意。"

  cheng_xiaojie:
    - "榴月十九日晚到白家作客，未發生成人事件。"
    - "她對若當時沈夫人沒有排除她、自己是否會上樓回答 UNKNOWN。"

  bai_rokujo:
    event:
      - "榴月二十日六條房完成首次雙方自願成人性交事件；兩次體內射精已確認。"
    consent:
      - "六條本日多次局部允許、拒絕、改位、重新允許均有效。"
      - "她明示當下成人慾望；不等於永久成人身份或未來 blanket consent。"
    relation:
      - "已由『私人茶局／複雜注意但無性交』更新為『本線已有雙方自願成人事件』。"
      - "沒有建立愛、婚姻、所有權、排他或固定情人契約。"
    pregnancy:
      - "UNKNOWN。"

  rokujo_yang_yuhuan:
    - "榴月二十日白玉池已就原十日賭正面核對。"
    - "六條對楊玉環『至少在鼓勵／看戲上有份』之歸責上升；此為人物解讀。"
    - "本場沒有建立兩人成人關係，也沒有建立未來成人同意。"

  bai_yang_yuhuan:
    - "既往白玉池成人事件繼續有效。"
    - "楊玉環榴月二十日表示目前仍願意／有興趣考慮白＋楊＋六條三人玩法；此為可撤回未來方向。"

  bai_hongniang:
    old_bet:
      objective_result: "BAI_WINS"
      hongniang_knowledge_at_v5_4: "NOT_YET_KNOWN"
      stake: "紅娘房門扇／窗扇再拆十日"
      state_at_v5_4: "DUE_NOT_EXECUTED"
    new_wager:
      - "榴月二十日加碼新賭正式成立，真條件保密。"
      - "新賭以楊玉環、六條本人未來當場自主決定為必要條件；賭約沒有她們的同意權。"
    later_execution:
      - "至 V5.5 紅娘已進大堂鐵籠公開生活／營業；紅娘床已搬至籠旁、預定最後一日焚毀。"
      - "V5.5 不重新推演此執行如何由 V5.4 未決過渡；以 HOT V5.5 已確認硬狀態為準。"
    public_boundary:
      - "看／問可；伸手碰觸可被紅娘拒絕。"

  bai_zuihua:
    - "榴月二十三日晚白御行只問兩人單獨未來是否還有可能，醉花回答『有』。"
    - "這是當下仍有興趣，不是補債、日期、永久承諾或未來 blanket consent。"
    - "當夜同床分側無接觸，沒有成人事件。"

  gu_qingjian_bai:
    - "榴月十七日晚兩次成人事件仍為有效既往事件。"
    - "公開『顧師爺』工作人格與私下『清簡』面向分層，不互相吞併。"

  pan_bai:
    - "榴月十八日晚帳房小試與抓姦鬧劇既往事件仍有效。"
    - "潘金蓮的局部拒絕、後續浸籠同意分開保存。"
    - "不得回填為戀愛或全面成人承諾。"
```

---

## 5｜商會、營運、帳務與空間（截至 HOT V5.5）

```yaml
OPERATIONS_AND_ACCOUNTS_V5_5:

  guild_women_project:
    suqing:
      - "十八日商會專案持續。"
      - "貼身衣物、肚兜、月事用品實穿／展示方向為工作軸。"
    outfit_contest:
      state: "ACTIVE_INTERNAL_EVENT"
      duration: "一個月"
      prizes:
        first: "10兩"
        second: "5兩"
        third: "5兩"
      payer: "白御行"
      lock:
        - "票選不產生成人、戀愛、接觸或私下會面資格。"
    sexy_tryon:
      state: "VOLUNTARY_INTERNAL_TRIAL_ACTIVE"
      lock:
        - "只限成年女性員工自願內部試穿。"

  talent_system:
    secretary_levels: "PROPOSAL"
    academy: "定陶商會人才進修院｜PROPOSAL_NOT_LAUNCHED"
    male_attendant_recruitment:
      assigned_to: "顧青簡"
      status: "ASSIGNED / NOT_HIRED"

  cooling_project:
    location: "白家／浮香小居"
    concept: "外置熱煙道抽風＋冷水進氣"
    state_at_v5_5:
      - "兩名工匠已到白家。"
      - "沒有 MASTER 級證據證明施工完成或效果成立。"

  open_continuation:
    state: "OPERATIONAL_PRACTICE_FORMED / NOT_FORMAL_SYSTEM_DOC"
    principles:
      - "原契約只涵蓋原服務。"
      - "新需求需由女人本人重新同意／拒絕並自行決定價格、時間與範圍。"
      - "使用觀止房間／酒水／人手／車馬可另收資源費。"
    unresolved_case:
      - "桃枝原陪席是否履行、20兩押金最終如何結算仍未確認。"

  fish_horse_line:
    yuxuanji_status: "REDLINE_FEMALE_GUEST / NOT_GUANZHI_SEX_WORKER"
    grey_horse:
      - "已提前到附近馬房。"
      - "具危險行為報告。"
      - "魚玄機只承諾看；沒有觸碰／馴騎義務。"

  hongniang_shixian_contest:
    state: "ACTIVE"
    duration: "榴月二十三日起九日"
    metric: "實際營業收入"
    pure_cash_injection: "EXCLUDED"
    day1_midpoint:
      - "掌燈時紅娘暫時領先。"
      - "失仙改制後收入速度提高並出現回頭客。"
    day1_close: "UNKNOWN"
    overall_result: "UNKNOWN"

  hongniang_egg_business:
    price: "5兩／蛋"
    hard_boundary:
      - "不瞄頭／臉。"
      - "不能用臭蛋、石頭、杯子替代。"
    no_water_bath_pledge:
      bai_pledge: "500兩"
      early_crowd_pledge_total: "約880兩"
      status: "CONDITIONAL_PLEDGE_NOT_REVENUE_UNTIL_COMPLETED"

  shen_courtyard_accounts:
    building_lease: "10年／60,000兩"
    reserved_room_guard: "另100,000兩"
    holding_deposit: "1,000兩"
    later_first_payment: "30,000兩，前1,000兩併入；餘款分期"
    lock:
      - "不得把總額、首付款、承諾款混成同一筆實收。"

  catch_adultery_deposit:
    state: "PUBLIC_PROPOSAL_ACCEPTED_FOR_PRICING"
    rule_direction:
      - "查指定男人前先核對關係／姓名並收保證金。"
      - "不得藉捉姦亂翻全樓。"
    amount: "UNKNOWN"
    formal_policy: "NOT_YET"
```

---

## 6｜知情、秘密、傳聞、人物解讀與隱藏層

```yaml
KNOWLEDGE_SECRET_V5_5:

  six_bet_truth:
    world_fact:
      - "白御行已於榴月二十日因六條本人自願成人事件贏原十日賭。"
    yang_yuhuan:
      knows:
        - "原賭存在。"
        - "自己當時在場並覺得有趣。"
      not_established:
        - "她是正式共同下注人。"
        - "她以羞辱六條為核心動機。"
    aling:
      witness:
        - "正式押彩頭者是白御行與紅娘。"
        - "楊玉環在場，但未聽見她正式下注。"
    rokujo:
      interpretation:
        - "把楊玉環視為至少在鼓勵／看戲上有份。"
      status: "CHARACTER_INTERPRETATION_WITH_EVIDENCE / NOT_WORLD_FACT"

  new_wager_secrecy:
    true_content_known_at_creation:
      - "白御行"
      - "紅娘"
    nearby_partial_knowledge:
      - "楊玉環、六條、阿泠知道白御行打算再坑紅娘、想讓紅娘見證未來三人局，但未合法取得白紅離池後完整最終條款。"
    no_source:
      - "潘金蓮知道新賭真實三人條件"
      - "趙受益知道新賭真實三人條件"

  shixian:
    director_hidden_truth:
      - "浮月閣名妓／妖化人。"
      - "來觀止帶有踢館／比較兩樓本事目的。"
    public_or_bai_knowledge:
      - "不得自動知道上述隱藏真相。"
    unknown:
      - "具體妖種"
      - "真身"
      - "特殊能力"

  shen_reserved_room:
    known_hard:
      - "半塊木牌、三代家訓、保留空房、空房自開一次。"
    unknown:
      - "另一半木牌持有人"
      - "年代"
      - "生死"
      - "世界來源"
      - "空房自開原因"
    prohibited_merge:
      - "不得因失仙也屬異世界節點，就自動把沈家空房與浮月閣接成同一線。"

  chen_gold_mask:
    known:
      - "女客夜陳季常與金面具女客同行／進房線成立。"
      - "柳月娥對金面具問題作出高度相關但不直接承認的回應。"
    current_objective_identity: "UNKNOWN"
    inference: "柳月娥可能是金面具女客的懷疑顯著升高"

  su_dongpo_yuxuanji:
    known:
      - "女客夜兩人曾同行／上樓。"
    room_content: "UNKNOWN"
    adult_event: "UNKNOWN"

  xuetao:
    - "早先匿名薛濤真身的白御行合法確認狀態仍依父 MASTER；沒有因 V5.2-V5.5 自動補完。"

  catch_adultery_secret_game:
    status: "DIRECTOR_HIDDEN_PROPOSAL_NOT_PUBLIC"
    corruption_lock:
      - "曾有導演把密室概念錯放進公開大堂對話；該段已被玩家 HOLD 撤銷。"
      - "不得生成任何人物知情、傳聞或後續因果。"

  arrival_mechanism:
    - "觀止過往錯名／寫名／濃密談論後入場案例只能支持相關性與候選假說。"
    - "不得升格為『念名字就一定召來』的世界定律。"
```

---

## 7｜截至 HOT V5.5 的主要未決事項

```yaml
OPEN_THREADS_AT_MASTER_CUTOFF_V5_5:

  li_shishi:
    - "是否懷孕仍未確診。"

  hongniang_shixian:
    - "九日總營收勝負 UNKNOWN。"
    - "榴月二十三日 Day 1 最終關帳 UNKNOWN；只有掌燈時中途盤帳。"
    - "榴月二十四日『今日新競賽』規則尚未演出。"
    - "紅娘九日不水浴募款最終承諾額 UNKNOWN。"
    - "酒浴正式開始／完成、實際酒種與結果未演出。"
    - "紅娘床最後一日劈解／焚毀尚未在 V5.5 截止前完成。"

  shixian_fuyue:
    - "失仙何時／是否公開浮月閣來源 UNKNOWN。"
    - "失美、失蘿、錯位何時／是否進本線 UNKNOWN。"
    - "失仙此輪競賽是否就是完整踢館或僅第一手試探 UNKNOWN。"

  shen_reserved_room:
    - "另一半木牌持有人全部身份資訊 UNKNOWN。"
    - "空房自開原因 UNKNOWN。"

  chen_goldmask:
    - "柳月娥是否就是金面具女客 UNKNOWN。"
    - "陳季常返家後發生什麼 NOT_PLAYED。"

  su_yu:
    - "蘇東坡×魚玄機女客夜房內內容／是否成人事件 UNKNOWN。"

  catch_adultery:
    - "捉姦保證金金額與正式流程未定。"
    - "秘密捉姦密室仍未落地。"

  zuihua_bai:
    - "未來單獨成人關係只有方向與興趣，沒有日期／承諾／執行。"

  grey_horse:
    - "魚玄機是否／如何實際查看提前抵達的灰青馬，截止 V5.5 未由本 MASTER補寫。"

  cooling_project:
    - "浮香小居風道／冷水原型勘察、施工與效果未確認。"

  rokujo_room:
    - "和式／榻榻米平台改造仍屬 proposal／待工匠與六條本人定案。"

  talent_projects:
    - "商會人才進修院未正式開辦。"
    - "顧青簡男性服務員招募尚無正式錄取。"
    - "桃枝原契約與20兩押金最終結算未確認。"
```

---

---


---

# 3｜E114–E117｜V5.6–V5.9 PROMOTED EVENT LEDGER

## E114｜HOT V5.6【REBUILD-R1】｜榴月二十四日白日

```yaml
EVENT:
  source: "HOT V5.6【REBUILD-R1】"
  date: "理火三年榴月二十四日白日"
  status: "PROMOTED_TO_MASTER"
  key_facts:
    - "柳永本人入觀止，『奉旨填詞』與趙受益正面碰撞；柳永帶銀子，詞不能自動抵帳。"
    - "柳永已進白玉池、見阿泠，並參與白家詞／琴／酒／錦棠明星方向會議。"
    - "失仙官籍來源調查由潘金蓮啟動，當時仍 PENDING。"
    - "白御行、蘇清、顧青簡、柳永對失仙進行桌邊觀察；『樂器』『心理暗示』『封印』『幕後指使』均只屬假說。"
    - "白御行以500兩買斷失仙當日餘時；失仙接受當日餘時不接其他客、不回答旁人問題，可自行休息。"
    - "失仙自述自己太會聽人、沒有需求時不知把自己放哪裡，並有記憶版本混淆疑問；自述不等於客觀身世。"
    - "紅娘×失仙九日營收競賽仍持續；失仙前夜約領先168兩。"
    - "顧青簡、蘇清、錦棠的商會明星／量身／經紀談判線持續。"
  hidden_director_continuity:
    - "失仙＝浮月閣四大名妓之一／妖化人之隱藏層沿用；不得倒灌白御行等人物知情。"
```

# 41｜最新接關座標

> **理火三年榴月二十四日白日。**
>
> 失仙今日剩餘時間已被白御行以五百兩買斷；她已接受「今日餘時不回答旁人之問」，不再接客，可自行休息。白御行、蘇清、顧青簡、柳永已從失仙桌離開，曾在觀止樓上蘇清房內完成一輪討論，現在會議已散。
>
> 潘金蓮對失仙妓籍來源的暗查仍 **PENDING**。
>
> 疏影可能按自己的方式觀察失仙，但是否正在看、看到了什麼 **UNKNOWN**。
>
> 紅袖對失仙的「餘音／自調樂器」觀察只屬她自己的合法私下分析。
>
> 趙受益與六條已進白玉池線；楊玉環是否當下加入 **UNKNOWN**。
>
> 柳永與趙受益早已有「奉旨填詞」正面伏筆；柳永已去過白玉池並見過阿泠，也已進過白家參與詞／琴／酒／明星會議。白御行剛以「真奉旨就不能拿普通實習價」「能奉旨嫖娼我就敬你」繼續拿柳永開玩笑；沒有新的正式聖旨成立。
>
> **下一幕不應回到舊 V5.6 的紅娘蛋局接點。**
>
> 世界目前真正懸著的，是：
> - 失仙在剩餘白日不必回應任何客人後會自然做什麼；
> - 疏影是否看見／畫下那一段；
> - 潘金蓮官籍暗查何時產生第一筆合法結果；
> - 趙受益／六條的白玉池場如何發展，以及楊玉環是否真的到場；
> - 明日普通客人再面對失仙時，她是否仍能像此前那樣無阻力地「善解人意」。

## E115｜HOT V5.7｜榴月二十四日夜

```yaml
EVENT:
  source: "HOT V5.7"
  date: "理火三年榴月二十四日夜"
  status: "PROMOTED_TO_MASTER"
  key_facts:
    - "白御行、蘇清、醉花完成一次三人自願成人事件。"
    - "醉花與蘇清各有已保存之可觀察高潮事件；不建立戀愛／永久同意。"
    - "蘇清當下明示接受白御行在其體內完成射精；受孕／懷孕保持 UNKNOWN。"
    - "三人以甜鹽開水恢復，白御行決定留宿醉花陰。"
    - "蘇清、醉花對白家私人小屋有興趣，但只屬 PROPOSAL；未施工、未入住、未建立夫人名位。"
    - "『白家私人空間不帶男人』大方向獲兩人接受；是否連其他女性／成人對象都禁止，當時未決。"
```

# 16｜直接接關摘要

> **理火三年榴月二十四日夜，醉花陰。白御行、蘇清、醉花今晚的三人成人事件已完成：醉花至少兩次明確高潮，白御行與醉花首次明確完成成人性交；蘇清至少一次明確高潮，並在持續互動中以自己的成人語言直接表示當下希望白御行留在體內完成，白御行遂在蘇清體內射精；受孕／懷孕仍 UNKNOWN。三人事後共同喝甜鹽開水恢復，白御行決定今晚不回白家，留在醉花陰一起睡。睡前又談到：蘇清、醉花都對在白家擁有像浮香小居那樣的私人小屋有興趣，但仍只是 PROPOSAL；兩人要保留自身身份、空間與觀止生活，不自動成為夫人／常住。白御行提出白家小屋不可帶其他男人回去，兩人接受『白家私人空間不帶男人』的大方向，但蘇清追問是否連女性或其他性愛對象也禁止，白御行尚未回答。真要擴張，白御行仍需找潘金蓮談，並先向白家兩位女主人李師師、李瓶兒說明；三人目前仍醒著躺在醉花陰，下一幕尚未發生。**

---

## E116｜HOT V5.8｜榴月二十五日夜

```yaml
EVENT:
  source: "HOT V5.8"
  date: "理火三年榴月二十五日"
  status: "PROMOTED_TO_MASTER"
  key_facts:
    - "V5.7 後蘇清牛郎店／男性陪侍投資合作方向成立，但店址、資本、股權、契約未落地。"
    - "失仙官籍追查得到陳州長期紀錄異常；匿名灰信指向『陳州城南／三年前／義莊／無主女屍衣棺錢／仙姑』，只作線索。"
    - "下月初一湖心觀星會／商務活動方向啟動規劃。"
    - "觀止大堂完成男人送命話錄、紅娘52兩單句表演與500兩終身固定答詞背書；背書不證成客觀身體真相。"
    - "白御行交顧青簡1000兩作結算浮額。"
    - "沈家保留空房內可觀察到至少三類不同反應來源：可顯影對話影子、左牆重擊／語音來源『十一哥』、窗下敲擊／灰塵與沙盒寫字來源；SAVE 分類不證成三個獨立本體。"
    - "窗下來源把另一半木牌線索指向陳州義莊／女屍；其陳述未獲外部查證。"
    - "白御行懸賞1000兩讓潘金蓮把失仙引到沈家；失仙接受500兩營業展示交易。"
    - "沙盤對失仙只形成模糊『一』指向，不能證明失仙＝女屍／佔屍者／持牌者／敵人／沈家等待者。"
    - "白御行退出沈家，不取得離場後房內知情。"
    - "白御行另交三十二娘200兩作砸紅娘蛋局預算；實際購蛋／投擲當時未演。"
    - "白御行返白家睡覺。"
```

# 24｜直接接關摘要

> **理火三年榴月二十五日晚，白御行已結束自己在沈家鄰院保留空房的參與，返白家睡覺。V5.7 後，白御行線先經蘇清牛郎店投資方向、醉花成人事件與睡至二十五日中午；白日失仙官籍追查得到陳州長期紀錄異常，匿名灰信又把線索指向『陳州城南、三年前、義莊、無主女屍衣棺錢、仙姑』。同日另啟動下月初一湖心觀星會規劃；晚上觀止大堂完成男人送命話錄、紅娘52兩單句付費表演與500兩終身固定答詞背書，白御行另交顧青簡1000兩作結算浮額。其後白御行到隔壁沈家守空房，房內可區分出至少三種反應來源：可顯影說話的模糊影子、左牆會重擊並能說話且接受『十一哥』稱呼的來源、以及窗下能敲擊並用灰塵／沙盒寫字的來源。窗下來源以『找 牌 南』及一連串節能問答，自稱另一半牌線指向開封以南的陳州義莊／女屍，並對『牌在女屍身上』『佔據女屍身體的東西是其敵人』『女屍來此可感應』給肯定反應；這些都只是其陳述。白御行用密信懸賞1000兩讓潘金蓮把失仙引來，另與失仙談妥500兩營業展示交易；失仙部分褪衣後，沙盤對白御行『若要找的是這個寫一』寫出『一』。因『這個』指涉過寬，只能確定窗下來源把失仙模糊指到同一條線，不能證明失仙就是女屍、佔屍者、持牌者、敵人或沈家等待者。白御行隨即明示『這是找人的故事，不是我的故事』，叫沈秋進房，與三十二娘退出；後續若有人願意告訴他，他才會知道。離開後白御行又私人給三十二娘200兩，讓她趁比賽尚未確定結束前去按5兩一蛋玩紅娘，實際投蛋尚未演。最後白御行回白家睡覺，故事在此收束。**

---

## E117｜HOT V5.9｜榴月二十六日上午

```yaml
EVENT:
  source: "HOT V5.9"
  date: "理火三年榴月二十六日上午稍晚"
  status: "PROMOTED_TO_MASTER"
  key_facts:
    - "程素娘回報：失仙問『現在這具身體？』得到一敲；問是否要去陳州得到一敲；問去了能否弄清則無回應。"
    - "失仙自願攤出隨身物未見另一半木牌，未受身體搜查；她只說會自己查，未答應立刻赴陳州，之後獨自離開，去向 UNKNOWN。"
    - "潘金蓮引失仙到沈家之1000兩賞金已實際支付結案。"
    - "失仙沈家500兩出台／展示費已實際交觀止／潘方並掛入失仙營業帳；非性愛購買。"
    - "白御行與潘金蓮完成一次自願成人事件；潘明確拒絕內射，白御行遵守；潘評今日10/10只限今日，不建立未來 blanket consent。"
    - "曹州假印／冒名採辦案因無新硬證據轉材料留存、待新證據重啟。"
    - "男性服務業重構：先找2至3名男掌櫃候選，由其自行招訓男性服務隊；舊『年輕俊俏＋顧青簡直選』模型退出主路。"
    - "女性代訓、肚兜、一片裙、染布線綁到初一湖心島下午商務＋晚間詩會／觀止雙場作驗收與預熱。"
    - "李師師主代言方向撤回；錦棠轉為核心主秀／主代言方向，但最終演藝經紀約仍 PENDING。"
    - "蘇東坡初一晚場主持、文豪出席／寫錦棠均須本人未來回應。"
    - "張麗華酒莊成為初一全日優先供酒採購方向；按正常大客戶議價，不作情面原價。"
    - "顧青簡1000兩浮額先清公事，剩餘改為白御行私人贈與；精確餘額 UNKNOWN。"
    - "常煒名下物流女子由常煒決定保留；360兩舊墊款以年終獎抵扣方式固定，尚未在今日現金扣除。"
    - "故事凍結於定陶商會京師總部小型核心議事房；白御行、常煒、顧青簡尚未被自動寫成散會。"
```

# 25｜直接接關摘要

> **理火三年榴月二十六日上午，白御行先收到程素娘對沈家昨夜後續的晨報：失仙穿回衣物後曾問房內異常『女屍是我嗎』無回應，改問『你指的是我現在這具身體』得到一敲；她自願攤出隨身物但沒有找到另一半木牌，也未受身體搜查。她問是否要去陳州得到一敲，問去了是否能弄清則無回應。失仙未答應立刻赴陳州，只說會自己查，之後獨自離開，當前去向 UNKNOWN。白御行到觀止後把潘金蓮引失仙到沈家的1000兩賞金實際付清，也把失仙先前500兩出台／展示費實際交觀止／潘方掛入失仙營業帳；潘金蓮沒有失仙今早去向，也不把失仙沒出現等同離開。其後白御行與潘金蓮在樓上發生一次自願成人事件；潘明確拒絕內射，白御行遵守，今日被潘評為10/10但限定『只有今日』，未建立戀愛或未來 blanket consent。白御行離觀止直接去定陶商會，召常煒與顧青簡開核心會議。曹州假印案因無新硬證據轉為材料留存、等新證據再啟。男性服務員招募被重構：不再以年輕俊臉為核心，改先找2至3名能讀女客、會調整服務位置的『男掌櫃／男人版潘金蓮』競爭，由常煒看管人做事能力、顧青簡看制度契約，再讓男掌櫃自行招訓男人。女性代訓、肚兜、一片裙、染布線被綁到下月初一湖心島活動作驗收與預熱：下午是商會封閉商務招待，不帶家眷、不放閒人、代訓女子全體參加並以新服裝作視覺展示但不硬賣貨；晚上換成詩會／觀止實戰，代訓女子仍繼續參加，觀止熟手接主場，下午商家願意可留到晚間。全日公共成本走商會公帳。李師師服裝主代言被撤回，不以孕否作公開理由；錦棠改成核心主秀／主代言方向，初一作明星正式亮相與市場預熱，柳永需加速包裝。初一晚場暫定找蘇東坡主持，並把衣、色、肚兜、一片裙、染布自然引入詩題／談資；可請有名文士、給主持／出場／潤筆費，但他們是否來、是否寫錦棠均由本人決定。正式走秀正場另有一場，精確日期仍待釘死。白明礬接回方掌櫃布莊／染布線，公開是驗貨與品質監督，私下白御行希望她利用染坊出身偷學關鍵技術，此暗線不得曝光且不可破壞真生意。錦棠經紀約加速談，合理條件可讓，但仍需本人簽；紅娘額外外部宣傳因失仙線暫停。顧青簡手上1000兩先照公事支付紅娘500與核實成年問答人頭，之後剩餘款不再退白御行，改成白御行私人送她的錢，精確餘額仍 UNKNOWN。初一下午與晚間酒水優先採張麗華酒莊，照正常大客戶砍價、談折扣／返利，不以原價放水。柳永只先走自由顧問方向，本人是否正式接受與報酬待談。商會一月女性穿著票選仍在，白御行重新提出『女性穿得更養眼是否提高男性效率』的賭題，顧青簡主張要用實際工作數據判斷，並區分效率提高與只是男人更願意待在商會；她只條件式表示自己可穿得更養眼，不接受被強制指定衣服。最後舊帳找回：常煒名下約三十歲、懂商路／貨物／車隊／四種語言的物流女子當年成交360兩、白御行先墊、常煒本人曾同意持契；本輪常煒明確不退人，並同意360兩從年終獎抵回白御行，爭議條件至此固定。白御行表示其餘蘇清開發工作另與蘇清本人談，本輪不再展開。故事在定陶商會核心議事房因 HOT SAVE 命令凍結，白御行、常煒、顧青簡尚未被自動寫成散會離場。**

---

---

---

# 3｜V5.10–V5.13-R1 PROMOTED EVENTS

## E118｜HOT V5.10｜榴月二十六日下午

```yaml
EVENT:
  source: "HOT V5.10"
  source_file: "觀止青樓_白御行線_HOT_SAVE_V5.10_榴月二十六日下午_浮月閣洩名_潘金蓮初一拍賣構想_偏廳失仙問客_HOLD版.md"
  source_sha256: "62786f0a88be66d30adade32f8bfd4f1197bd985c14d0e4f5ee46ad599aefae1"
  date: "理火三年榴月二十六日下午"
  status: "PROMOTED_TO_MASTER"
  key_facts:
    - "HOT V5.9 定陶商會核心會議完成收尾；常煒離場前答應先叫人粗看初一湖心島船案。"
    - "白御行與顧青簡在辦公環境形成雙向親吻；白御行繼續升高接觸時，顧青簡握腕叫停，公私界線有效。"
    - "白御行邀顧青簡下工後私下到白家；顧青簡接受『今晚自己從後面來、不坐車、不公開迎接』的私人拜訪安排。成人結果此時尚未成立。"
    - "白御行返觀止後，久未出現的時空道人再現。道人拒絕直接劇透失仙真相，但失言說出專名『浮月閣』。"
    - "『浮月閣』只成立為新名字線索；不證成失仙所屬、反派、沈家異常來源或完整身份。"
    - "白御行把『浮月閣』告訴潘金蓮；二人決定不主動派專人追查，只在正常客流、掮客、商旅話語中被動聽風。"
    - "紅娘沒有因本事件取得『浮月閣』知情。"
    - "白御行與潘金蓮其後抱睡至下午，沒有新增成人事件。"
    - "醒後二人加速初一湖心島觀止端準備。白御行提出把阿麗婭等人的首次出閣／初夜競價變成『競價只形成候選、最後由女人本人點人』的玩法。"
    - "潘金蓮認為玩法有錢景並接手規則／營運設計，但明確要求先問阿麗婭；此時阿麗婭及其他女人仍未被自動排入。"
    - "詩詞書畫估值、女人本人選人、《湖心花榜》等均只到構想／規則設計，未有文人或女人自動接受。"
    - "觀止開業後，白御行坐到大堂側後半開偏廳觀察。"
    - "一名約二十七八歲、帶兩名隨從的陌生男子進門，問櫃邊昨日『姓失的姑娘』今日是否在；得知尚未見人後留下飲酒。"
    - "該陌生男子身份／意圖 UNKNOWN；不得與浮月閣、沈家、陳州、失仙同夥或後續秦國人物直接合併。"
    - "紅娘注意到該男子；截至本 HOT 凍結點尚未與其形成明確接觸。"
    - "失仙當前去向仍 UNKNOWN，返觀止未成立。"
    - "玩家喊 HOLD 後所討論的嫪毐、趙姬、呂不韋、嬴政、拉斯普丁、忽必烈、歷朝商人等沒有進入 E118 世界事實。"
```

> **E118 固化切面：榴月二十六日下午，白御行位於觀止大堂側後半開偏廳；失仙未返，問失仙的陌生男子仍留場飲酒。顧青簡今晚私人拜訪已約定但尚未發生；『浮月閣』只是一個由時空道人失言取得的新專名；初一競價玩法仍須逐人取得本人同意。**

---

## E119｜HOT V5.11｜榴月二十六日晚

```yaml
EVENT:
  source: "HOT V5.11"
  source_file: "觀止青樓_白御行線_HOT_SAVE_V5.11_榴月二十六日晚_嫪毐挑戰_夏蓮初一限定掛牌_商人心法_車輪採訪證_紅娘初一出籠_白玉池邀請_離場前凍結版.md"
  source_sha256: "f3b72c3aad79de8d7b424a4be4fb586af0653933776d45df8f84f4234338a5c8"
  date: "理火三年榴月二十六日晚"
  status: "PROMOTED_TO_MASTER"
  key_facts:
    - "E118 偏廳問失仙的陌生男子仍維持身份 UNKNOWN；紅娘後續自行與其桌形成最低限度營業接觸，但沒有因此取得其身份。"
    - "嫪毐因聽見紅娘公開固定證詞『我紅娘，這輩子吃過最大的雞巴是白御行的』不請自來，付挑戰款並成為《不服白御行者名錄》第一名。"
    - "紅娘把挑戰費與成人 access 分開；目測不能進入其『吃過』的同一比較類別。她當晚沒有同意與嫪毐形成成人比較。"
    - "嫪毐叫人請趙姬來為自己作名聲證人；趙姬自主到場，只能證明自己的既有經驗，不能替嫪毐與白御行作客觀身體比較。"
    - "趙姬本人承認過去公開歌舞娛樂取利與妓籍；王后／太后等後來身份沒有被她用來抹除這段妓籍歷史。"
    - "呂不韋後來入場，重新叫出趙姬舊妓名『夏蓮』。"
    - "本 Route 以2001《呂不韋傳奇》作趙姬／夏蓮主要戲劇 donor：夏蓮、邯鄲名妓／歌舞出身、呂不韋舊歷史、皓蘭夜明珠等可作 donor 來源；不整包匯入2019《皓鑭傳》，donor 未來也不綁 Route 命運。"
    - "夏蓮本人明確決定：下月初一晚以『夏蓮』限定掛牌一夜。精確底價、服務、競價與成交細則仍待她與潘金蓮另談。"
    - "白御行公開表示自己會參與並盡力把夏蓮價格往高處拱；實際出價尚未發生。"
    - "觀止既有天價基準在現場被重新提起：辭歲1200萬兩一夜、錦棠500萬兩一夜，兩筆同晚。"
    - "呂不韋接受初一下午湖心島邀請，並明示以商人身份而非秦相身份出席。"
    - "初一下午主題成形為『商人心法』：討論人如何賺、判斷、重建，而非只比現有身家。"
    - "白御行答應初一再向呂不韋講一個後世商人登頂、失位、再回來、多次商業失敗後重建的完整故事；呂不韋此時只知鉤子。"
    - "白御行邀嫪毐初一晚在天下才子面前重演史書桐木車輪技藝；嫪毐接受，要求真木、可承力、公開演示。精確重量／尺寸尚未成立。"
    - "白御行決定由定陶商會向汴京紅說書先生發『特別採訪證』：可免費吃喝並記錄公開場；採訪證不等於私人席／私房通行證。老周表示會申請。"
    - "初一下午人物方向：呂不韋已確定；夏蓮本人說會去聽商人心法；白御行公開表示錦棠會出席；潘金蓮把辭歲列入商人席邀請，辭歲本人是否到仍 PENDING。"
    - "白御行行使先前賭約衍生的紅娘籠居處分／獎勵權，指定紅娘在初一日出提前出籠。此時床拆／砍／燒處分與另一條九日營業／洗浴募資約都沒有取消。"
    - "白御行邀呂不韋、夏蓮、嫪毐去白玉池。夏蓮拒絕三人一起，但表示自己願意去，尚未在呂不韋與嫪毐之間選陪同者。"
    - "阿泠保留白玉池加場與進池決定權；本轮沒有批准任何一組、沒有開始洗浴、沒有形成白御行與嫪毐身體比較結果。"
    - "白御行最後向潘金蓮表示今晚到此、要回白家睡覺；HOT 在實際離場完成前凍結。"
    - "E118 顧青簡今晚下工後私訪白家的約定仍有效，精確到達時間 UNKNOWN，不能被『回家睡覺』一句自動吞掉。"
    - "失仙／浮月閣線本輪沒有取得新硬消息，失仙去向仍 UNKNOWN。"
```

> **E119 固化切面：榴月二十六日晚，夏蓮已本人答應初一限定成人一夜掛牌；呂不韋答應初一以商人身份出席；嫪毐答應車輪公開演示；紅娘只得到『初一日出提前出籠』安排，尚未在本事件即時出籠。白御行尚未真正離場，顧青簡私訪約仍可能在今晚碰撞。**

---

## E120｜HOT V5.12｜榴月二十六日晚後續～榴月二十七日晚

```yaml
EVENT:
  source: "HOT V5.12"
  source_file: "觀止青樓_白御行線_HOT_SAVE_V5.12_榴月二十七日晚_顧青簡夜訪_李師師疑孕晨談_張麗華酒水_九幽帝王信件外送_完整固化版.md"
  source_sha256: "be9de0af9a00c573328566da22090d4ebe9fd3b01c1b6ed9f24980a248678629"
  date: "理火三年榴月二十六日晚後續～榴月二十七日晚"
  status: "PROMOTED_TO_MASTER"
  key_facts:
    - "白御行返白家後，顧青簡依 E118 約定私下由後門到白家，不坐車、不帶公開排場，穿私人衣物並攜薄文書袋。"
    - "白御行與顧青簡既有地下情／成人歷史存在，但本夜仍由當下人物行動重新成立。"
    - "顧青簡先主動拉近／親吻，之後雙方自願升高為成人事件。"
    - "顧青簡本夜不接受精液進入生殖道；她允許其他不形成該生殖風險的收束方式並保持自己對節奏與位置的控制。"
    - "本夜成人事件不建立受孕、懷孕、生子承諾、婚姻、如夫人／妾位或未來 blanket consent。"
    - "白御行與顧青簡談可食用青蛙、供應、烹調、養殖與『頂呱呱』品牌玩笑方向；只成立生意 idea／市場調查方向，未開店、未簽供貨、未定價。"
    - "二人談及未來孩子。顧青簡明確區分『我的孩子』與『我替你生孩子』；若未來自己選擇做母親，白御行是她會認真考慮的人選之一，但沒有現在生育承諾、受孕協議或妾位。"
    - "顧青簡若未來有孩子，主張孩子資產獨立，不作白家可借用資金；孩子不是投資商品。"
    - "白御行提出的現代受孕時機／頻率知識只保存為白御行 testimony，不升格觀止醫學定律。"
    - "二人談到觀止『兩副面孔』以及潘金蓮／流產傳聞；白御行合法知情鏈來自時空道人→李瓶兒→白御行。潘金蓮強迫宋蕙蓮／李桂姐流產沒有因談論被證成。"
    - "榴月二十七日破曉，顧青簡整理衣物／文書後由後門離開白家。"
    - "顧青簡離開後，白御行回到李師師處，二人久違相擁補眠。此段成立抱睡／相擁，不成立新的成人事件。"
    - "李師師孕況升為 SUSPECTED / HIGH SUSPICION：先前存在可能受孕成人事件，她本人已找醫者看過，醫者判斷高度可疑／很可能但未確診，之後又有味覺／食慾變化。"
    - "李師師要求確診前不要對外宣稱她懷孕；是否懷孕、若確診是否留下、是否繼續天下第一花魁三件事分開。"
    - "若未來確診，是否留下由李師師本人決定。她不因職業自動終止，也不因白御行高興自動留下。"
    - "李師師表示即使未來抱著白御行的孩子，也要保有自己的名聲、邀請、金銀與場子；『孩子姓白可以』只在假設確診且本人選擇留下的條件下成立。"
    - "白家家庭位階由玩家明示校正：李師師＝首席如夫人／白家女主人級；李瓶兒＝如夫人／白家女主人級；張麗華、浮香＝情人＋白家家內成員，各自在白家有獨立小屋／房，也在觀止有房，不是白家臨時客人。"
    - "李師師對初一下午席條件式接受：可出席、需要時可彈一兩曲，但不偽裝商業代言，身體累可自行提前離開。"
    - "夏蓮初一限定掛牌法位校正為成人床牌／性服務的一夜掛牌；不是單純喝酒陪坐。精確競價規則、價格、得主、包含／排除項目與實際成人事件仍 PENDING。"
    - "榴月二十七日黃昏，張麗華在白家家內晚飯並回報顧青簡已按定陶商會大客戶方式接洽初一用酒。下午與晚間分開估算、普通酒加備、高級酒控量、備貨分散；精確採購量／單價／折扣／付款未獨立核帳。"
    - "白御行提出初一大場後另找時間讓白家自己人去湖心島家宴；只屬 proposal，日期與參與者未定。"
    - "初一晚『酒鬼俱樂部』邀請方向包含李清照、柳如是與其他可找到成員；邀請方向／文案成立，逐封送達、接受與到場 UNKNOWN。"
    - "白御行向張麗華說明自己希望藉夏蓮競價刺激九幽帝王拿國運／陰德類資產換陽間資金，再作套利；此為白御行自述之商業目的，不證成所有帝王會照做。"
    - "白御行明示初一會參與出價拱火；本事件尚未實際出價。"
    - "榴月二十七日晚，白御行在白家寫好並交入九幽外送／傳遞路線多封信，信件已離開白家。"
    - "給嬴政的核心文字為『初一，汴梁觀止。你媽要復出了。』；給劉邦則告知夏蓮重新掛牌一夜限定並叫他帶錢，不夠可找白御行借。"
    - "其他帝王信只告知夏蓮舊名趙姬、初一於觀止重新掛牌、只此一夜；未替夏蓮／潘金蓮虛構尚未確定細則。"
    - "所有九幽信件只成立寄出；收件、相信、轉述、動身、競價與報復均 PENDING / UNKNOWN。"
    - "失仙／浮月閣／沈家／陳州線本段沒有取得新硬消息。"
```

> **E120 固化切面：榴月二十七日晚白家。顧青簡私訪與本夜成人事件已完成並於破曉離開；李師師孕況為高度疑似但未確診；白家四位女性家庭位置獲玩家校正；張麗華已加大初一供酒備援。白御行把夏蓮重新掛牌消息送入九幽傳遞線，但任何帝王收件／到場／競價都尚未成立。**

---

## E121｜HOT V5.13-R1｜榴月二十七日晚

```yaml
EVENT:
  source: "HOT V5.13-R1"
  source_file: "觀止青樓_白御行線_HOT_SAVE_V5.13-R1_榴月二十七日晚_槐生越界_十一哥罵門_紅娘出籠_仙客文豪秦國邀帖_曆法修正版.md"
  source_sha256: "d62aa90d3028a2f68113d46ff6077febca86e6f1fd859e5f82eca16761200584"
  date: "理火三年榴月二十七日晚"
  calendar_lock:
    - "觀止曆每月固定二十八日。"
    - "本日為榴月二十七日；明日榴月二十八日；後日才是下月初一。"
    - "原 HOT V5.13 的日期誤差由 V5.13-R1 合法修復。"
  status: "PROMOTED_TO_MASTER"
  key_facts:
    - "阿麗婭由先前 PENDING 升為本人明示『初一，我掛。』"
    - "白御行提出五千兩作第一價／起始標尺，連結西門慶舊五千兩歷史重量；阿麗婭接受它作起點，不接受把五千兩解讀為白御行已買到她。"
    - "男人可出錢競，文士可用詩、書、畫等形成她願意看的價值；金錢／作品只取得被她考慮的資格。最後第一個男人由阿麗婭本人選；若沒有她想選的人，不因競價存在強迫完成第一次。"
    - "沈家未知反應來源正式操作性分為三條：可顯影對話來源自選當前稱呼『槐生』；左牆語音／重擊來源『十一哥』；窗下敲擊／灰塵／沙盒寫字來源。三者可分開追蹤，不證成三個獨立鬼魂。"
    - "槐生在沈家範圍外緣出現被拉扯／變淡／難以跨越現象。白御行以100兩向觀止／潘金蓮方向成立一日臨時租地安排，並給槐生進白家許可。"
    - "一日租地成立後，槐生可跨過先前邊界進入白家地界；到白家更外側／外門附近又出現手淡、腳步受拉。這只支持與土地／使用邊界高度相關，不證成靈體機制定律。"
    - "100兩一日租地費約定次日上午於白家付款；截至 cutoff 尚未顯影付款。租約到期時槐生會發生什麼仍 PENDING。"
    - "白御行授權潘金蓮把沈家左牆一小段暫時開成門；新門處十一哥出現撞擊／語音反應並說『我跟過來了』方向。"
    - "潘金蓮其後把同一門體做成沈家左牆一端＋觀止正門一個面／聲音出口的『兩處一門』接觸結構；未授權人士不能藉此任意穿越，但聲音可通。"
    - "十一哥可在觀止正門與路人互罵／互動；他自主選擇暫不回沈家舊處，留在觀止入口接觸位置，但明示自己不是被養的鬼，也不正式認領門房雇傭身份。"
    - "十一哥門／拓撲試驗費由十一哥名義記帳、白御行擔保，精確金額尚待潘金蓮結算。"
    - "觀止正門『漂亮女子畫面＋牆中十一哥粗口』的美人牆構想成立；疏影被提作畫師候選，但疏影本人尚未接受，commission 未成立。"
    - "白御行先讓紅娘出籠一小時與十一哥互動，潘金蓮實際開鎖；其後白御行再依既有籠居處分／獎勵權明示紅娘不必回籠。"
    - "紅娘剩餘鐵籠生活即時完全解除；E119 原『初一日出提前出籠』安排被 supersede。紅娘床拆／砍／燒處分與其他獨立營業／洗浴義務沒有自動取消。"
    - "紅娘與十一哥建立五兩官方蛋鬥嘴生意：觀眾判每回合輸贏，官方蛋5兩／顆；投紅娘不得瞄頭臉，投十一哥則投其牆／接觸面。"
    - "第一個可觀察回合由觀眾判十一哥輸，一顆官方蛋實際打到牆面。聯合節目五兩收入計入紅娘營收流水；投十一哥部分同時另記十一哥可歸屬收益／紅娘代收負債。"
    - "十一哥歸屬本金＋紅娘代理補償的定陶商會帳戶／信託方向談到：本金只進不出，十一哥具本人結算條件前不得提領；年息3%暫按單利方向，利息作紅娘代理補償。"
    - "該3%帳戶／信託截至 cutoff 仍未簽、未開戶、未轉入第一筆本金；顧青簡預定榴月二十八日先擬契約並讀給十一哥，本人接受後才成立。"
    - "時空道人本輪再現，對槐生／十一哥只給出觀察性判斷：槐生較像受『界』拘束，十一哥較像依牆／門／空間構件取得接觸；均不是世界機制定論。"
    - "白御行邀時空道人初一協助路由；道人表示若由他處理，原則是『先看人，再看線』，要防同名、同號、不同年齡、不同文本版本等誤接。他不替觀止決定誰必須來，也不保證每條線必通。"
    - "呂洞賓此時只停留在可能邀請構想；未送帖、未建立路由、未接受。"
    - "白御行與潘金蓮取得一條新的條件式推論：時空道人曾把浮月閣來看場的一批存在稱作『不是人』。只有在失仙確屬同一浮月閣群體的前提下，才可提高她非普通人的可能性。"
    - "失仙本人沒有因此被證明屬浮月閣，也沒有被證明『不是人』；人物池／導演隱藏真相不得倒灌白御行／潘金蓮知情。"
    - "潘金蓮啟動多條彼此獨立的初一邀請：蘇東坡走正式主持人工作約；白居易獨立客帖；關盼盼獨立客帖；謝瓊娘獨立客帖並可由本人另選是否掛牌；嬴異人取得夏蓮掛牌與秦國舊線方向客帖；趙受益取得觀止正式客帖。"
    - "上述全部只成立送帖／送帖路線啟動；收件、接受與到場均 PENDING。"
    - "夏蓮本人初一以『夏蓮』掛一夜的決定繼續有效；嬴異人舊關係不預留成交權。"
    - "E120 嬴政／劉邦九幽信件已寄出狀態繼續有效，但本轮沒有逐名收件證據；白御行『帝皇會所基本都知道』只保存為其估計。"
    - "白御行表示今晚要加急寫信給忽必烈，理由之一是阿麗婭已決定初一掛牌；截至 cutoff 尚未實際顯影寫成／送出。"
    - "趙受益的初一觀止邀請已啟動；玩家同時校正：六條御息所、楊玉環在觀止的相關帳由趙受益支付／供養。此帳務不賦予他兩人的行動與同意權。"
    - "白御行最後表示今天先回去並離開觀止。HOT SAVE 凍結時初一仍未開始；誰收到帖、誰答應、誰真正到場、誰競價、誰成交全部未發生。"
```

> **E121 固化切面：理火三年榴月二十七日晚。阿麗婭已本人決定初一掛牌；紅娘已即時完全出籠；槐生的一日租地／白家越界試驗與十一哥的『兩處一門』接觸口均已建立可觀察結果，但本體機制保持 UNKNOWN。初一主持、文豪、仙客、秦國舊人與趙受益等多條邀帖仍只到送帖／待回覆；九幽舊信收件仍未證；忽必烈急信尚未寫成。明日是榴月二十八日，後日才是下月初一。**

---

---

# 3｜V5.14–V5.18 PROMOTED EVENTS

## E122｜HOT V5.14｜荷月初一午後前｜湖心島天下商人席與舍方知 Route Entry

```yaml
EVENT:
  source: "HOT V5.14"
  source_file: "觀止青樓_白御行線_HOT_SAVE_V5.14_下月初一午後前_湖心島天下商人席_舍方知入場_下午聯誼規則_開場前凍結版.md"
  source_sha256: "16981613bffca677581e690311a3ed45c579fc9171d7d1ea87a84838db17ca3a"
  date: "理火三年荷月初一｜午間至午後正式場開場前"
  status: "PROMOTED_TO_MASTER"
  key_facts:
    - "白御行與白家／定陶商會相關人員抵達湖心島；天下商人桌形成，下午正式場尚未開跑。"
    - "白御行向商人桌正式說明定陶母公司／地方子商團、無息擴張與資本調度等商業方向；席間後世商人、國債、軍官委任、海貿、信用與黑帳等知識只保存實際發言來源。"
    - "錦棠的正式商演／代理契約已有效，直接可歸因品牌淨利分成24%；初一下午定位為壓軸品牌人物，晚上位置另算。"
    - "舍方知 #62 由官府送入觀止後，於本日由潘金蓮第一次帶到湖心島公開場，正式進入白御行 Route；她自帶針線箱，以女裝裁縫本事工作。"
    - "舍方知只公開最少資訊『官府送的』；案件內情、身體秘密與舊客網不因入場自動公開。"
    - "蘇清在商人桌維持獨立商人位置，談男性陪侍店與生存論；白御行私人『香花勇氣空氣』故事亦被商人桌知悉。"
    - "下午服裝與人流展示規則成立；穿著暴露／透明不等於成人邀請。"
    - "下午場最終規則鎖定為純聯誼、零現場交易；商務成交留待次日商會再談。"
    - "范蠡／西施、柳如是／鄭氏等歷史傳說只保存至當事人／席間發言層級，DISPUTED 不被補成客觀真相。"
```

> **E122 固化切面：荷月初一午後正式場開場前，天下商人桌與下午規則已就位；舍方知正式進 Route 並以裁縫身份在場工作。**

---

## E123｜HOT V5.15｜荷月初一傍晚｜午後場收束與晚場啟動

```yaml
EVENT:
  source: "HOT V5.15"
  source_file: "觀止青樓_白御行線_HOT_SAVE_V5.15_荷月初一傍晚_午後場收束_錦棠品牌證詞_十說書採訪證_晚場啟動凍結版.md"
  source_sha256: "85aa0b85a7570eb5dd62c3daf2fb9d069797443885cc1e5017cf4f91b8620642"
  date: "理火三年荷月初一傍晚"
  status: "PROMOTED_TO_MASTER"
  key_facts:
    - "曆法 successor 正式把先前『下月初一』解析為荷月初一。"
    - "下午純聯誼規則實際落地並完成收束，沒有現場完成商務交易。"
    - "趙受益加入天下商人席；其與六條御息所、楊玉環的白玉池舊事與成人事實被分軸保存。"
    - "范蠡本人新增承認與西施有過男女之事的證詞，但西施死亡／被殺線仍 DISPUTED。"
    - "錦棠午後壓軸品牌顯影成功，兩句可用品牌證詞文案成立；白御行與錦棠『今天一天的男人／女伴』只限本日公開角色，不升格永久關係。"
    - "大浦慶作 TEMPORARY_SCENE_CHARACTER 入場，未進人物池。"
    - "蘇清對皇太極仍保有遼東商路圖應收；柳如是支援鄭氏相關資金只保存到已知層級。"
    - "十名持紅邊『定陶商會｜湖心島特別採訪證』的說書先生已實際登島，老周在內；可記公開場，不得進私席／私房。"
    - "嫪毐的實木車輪已送到島上並驗看準備，但本 HOT 截止時公開演示尚未完成。"
    - "晚場開始時阿麗婭、夏蓮、紅娘已現身；其他討論人物不得倒寫成已到場。"
```

> **E123 固化切面：荷月初一傍晚，午後聯誼完成，十名說書先生取得公開採訪位置；車輪已到但競技尚未發生，晚場正式啟動。**

---

## E124｜HOT V5.16｜荷月初一深夜｜三千萬、五千萬與公開競技

```yaml
EVENT:
  source: "HOT V5.16"
  source_file: "觀止青樓_白御行線_HOT_SAVE_V5.16_荷月初一深夜_阿麗婭三千萬_夏蓮五千萬_千古一帝場外賽_白紗帳終場凍結版.md"
  source_sha256: "470466db161174ac96edef6bc03edd32044765ad2f1647da23e22c49f8ad8914"
  date: "理火三年荷月初一深夜"
  status: "PROMOTED_TO_MASTER"
  key_facts:
    - "嫪毐×拉斯普丁公開競技完成：實木車輪嫪毐六、拉斯普丁七；磚塊『九九神功』拉斯普丁六、嫪毐七；舍方知本人自願加入後續磚塊競技並完成九塊，取得該項公開勝出。"
    - "上述競技不建立任何成人關係；舍方知的身體秘密未因競技被強制揭露。"
    - "顧青簡進入晚場財務席；錦棠被白御行安排到乾隆側製造品牌／場面，非自行離開白御行。"
    - "阿麗婭掛牌形成三席制度；忽必烈最終出三千萬。觀止固定抽一成，阿麗婭本人取得二千七百萬；本人最後選擇權仍有效。"
    - "夏蓮以成人一夜掛牌，價格由數百萬逐步抬升；漢、秦、唐、清、遼、朱鄭等帝王／資本力量先後加入或退出。"
    - "國運設定校正：國運是人民意志／國家因果總和，不等於皇帝可隨意私用的現金。"
    - "趙受益明確拒絕拿人民國運為私人競標爭名；他與楊玉環的關係證據有前進，但本 HOT 不把『愛』固化成客觀狀態。"
    - "夏蓮最後本人選擇李世民，以五千萬成交；觀止一成五百萬、夏蓮本人四千五百萬。"
    - "李世民與夏蓮一同進白紗帳，形成極強公開觀感；帳內是否性交、方式、次數與完整私人真實全部 UNKNOWN。"
    - "白居易×關盼盼本夜有小幅關係推進但未和解；蘇清×皇太極遼東圖舊債仍未結清。"
    - "島內夜間船運封閉，主要人員至少待至天亮。"
```

> **E124 固化切面：荷月初一深夜，阿麗婭三千萬、夏蓮五千萬兩大掛牌結果成立；島上競技亦完成，但白紗帳內私人真實仍保持 UNKNOWN。**

---

## E125｜HOT V5.17｜荷月初二晚｜湖心島散場與觀止補假慶功

```yaml
EVENT:
  source: "HOT V5.17"
  source_file: "觀止青樓_白御行線_HOT_SAVE_V5.17_荷月初二晚_湖心島散場_燕子樓回聲_觀止補假慶功_紅娘復牌_盼盼夏蓮留宿凍結版.md"
  source_sha256: "4da556d7e316f88365044fd7f3464890f3165808a42bcf6c910e234c42e9b024"
  date: "理火三年荷月初二晚"
  status: "PROMOTED_TO_MASTER"
  key_facts:
    - "湖心島由深夜至破曉正式散場；阿麗婭×忽必烈離島時間依 successor 校正。"
    - "白御行把與沈萬三等人的短池／長池／聯合池談判方向交給顧青簡；尚無最終利率、擔保或契約。"
    - "楊玉環、趙受益、六條御息所之間的競逐／爭寵只保存實際互動，不升格任何新排他關係。"
    - "白居易×關盼盼×蘇東坡的燕子樓舊債重新顯影；蘇東坡作新詞《定風波·湖心再逢燕子樓人》；關盼盼破曉以『讓你們看看我自己』完成一舞。"
    - "潘金蓮與關盼盼談留人方向並提供後續落腳可能，但合約未成立。"
    - "周邦彥×李師師舊情正式斷尾。"
    - "張麗華的酒水供應者與白家情人／小院居民位置持續；乾隆退場後錦棠回到白御行身邊。"
    - "觀止初一夜照常營業，春梅主持、李瓶兒晨間接班；平台由阿麗婭／夏蓮兩筆成交取得合計八百萬一成抽成。"
    - "潘金蓮宣布初二觀止補假一天、晚上全樓慶功；定陶商會初二照常、初三中午另補假慶功。"
    - "初二晚觀止正門十一哥×紅娘五兩官方蛋再運作；紅娘舊床公開劈解／燒柴處分正式完成。"
    - "紅娘×失仙九日營收局由潘金蓮作棄賽結算，紅娘復牌；失仙主線仍 OPEN。"
    - "夏蓮的一夜期限已結束，四千五百萬屬本人待後續大額清算／配置；她暫住觀止，不等於就業／入籍。"
    - "關盼盼獲潘金蓮提供免費廂房先落腳，不等於雇傭或永久居住。"
```

> **E125 固化切面：荷月初二晚，湖心島已散、觀止補假慶功開席；關盼盼與夏蓮均暫時留在觀止，但各自未形成新的固定職業／籍屬。**

---

## E126｜HOT V5.18｜荷月初三清晨｜瓶兒夜後與次日待啟動

```yaml
EVENT:
  source: "HOT V5.18"
  source_file: "觀止青樓_白御行線_HOT_SAVE_V5.18_荷月初三清晨_瓶兒夜後_紅娘舍方知同房未越界_次日行程凍結版.md"
  source_sha256: "2cd01e6f9f158c3d6acdf1605c6e4a1641c58972430cf9a55530b5995da12186"
  date: "理火三年荷月初三清晨"
  status: "PROMOTED_TO_MASTER"
  key_facts:
    - "初二晚觀止慶功宴收束；初三中午另有定陶商會補假慶功。"
    - "白御行希望關盼盼先試教錦棠舞；關盼盼認為可談但尚未正式答應，費用／堂數／期限都未成立。"
    - "浮香小宅『會呼吸的房子』預定初三下午熱工實測；成功與全觀止改造均未發生。"
    - "白家巨床已訂製並預定初三中午附近送抵／組裝；截至 E126 cutoff 尚未到貨。"
    - "舍方知的身份／市場討論再分軸：女性社會／官方身份、男性身體、妓籍法律資格與私人性吸引不得互相替代；精確身體尺寸仍 UNKNOWN。"
    - "紅娘因舊床已毀，獲舍方知本人同意借宿其房／共床睡眠；沒有裸露、觸摸、測量或成人事件。舍方知只叫紅娘轉告白御行：想知道就自己來問。"
    - "白御行初二深夜選擇到李瓶兒房過夜；瓶兒要求當夜只要兩人，兩人完成私人成人事件。"
    - "白御行在射精前告知，李瓶兒明示『別拔／射裡面／今晚我准你』，因此本夜成立一次陰道內射；只屬當夜局部同意，是否受孕 UNKNOWN。"
    - "兩人事後清理、相擁睡下；李瓶兒當夜要求不與其他女人分享，不形成永久排他要求。"
    - "白御行提出等夏蓮／阿麗婭大額帳務理順後帶家裡人與錦棠去湖心島住幾日；李瓶兒表示喜歡並要去，其他人尚未逐一接受，錦棠不因此升格白家正式成員。"
    - "天亮後 Route 進入荷月初三清晨；商會慶功、舞訓、巨床送抵與浮香熱工試驗均仍在未來。"
```

> **E126 固化切面：荷月初三清晨，白御行與李瓶兒相擁睡後天亮；紅娘借宿舍方知未越界。初三白日多條行程仍 PENDING。**


---


# 4｜V5.18 PROMOTION MANIFEST

```yaml
V5_18_CONSOLIDATION_MANIFEST:
  inherited:
    E01_E121:
      source: "MASTER V5.13-R1-HARD"
      treatment: "FULL_INHERITANCE"
  promoted:
    E122: {source: "HOT V5.14", sha256: "16981613bffca677581e690311a3ed45c579fc9171d7d1ea87a84838db17ca3a"}
    E123: {source: "HOT V5.15", sha256: "85aa0b85a7570eb5dd62c3daf2fb9d069797443885cc1e5017cf4f91b8620642"}
    E124: {source: "HOT V5.16", sha256: "470466db161174ac96edef6bc03edd32044765ad2f1647da23e22c49f8ad8914"}
    E125: {source: "HOT V5.17", sha256: "4da556d7e316f88365044fd7f3464890f3165808a42bcf6c910e234c42e9b024"}
    E126: {source: "HOT V5.18", sha256: "2cd01e6f9f158c3d6acdf1605c6e4a1641c58972430cf9a55530b5995da12186"}
  later_overlays_not_absorbed: ["HOT V5.19", "HOT V5.20", "HOT V5.21"]
  post_master_hot_count: 3
  anti_forward_contamination: true
  paired_rcl_generation: "V5.18 / GUANZHI_RCL_SCHEMA_V1_1"
```

---

# 5｜MASTER V5.18 CURRENT HARD STATE｜截至荷月初三清晨

```yaml
CURRENT_HARD_STATE_V5_18:
  composition_rule:
    - "以 MASTER V5.13-R1-HARD 的 E01–E121 與硬狀態為歷史基底。"
    - "依 E122–E126 已成立變化覆寫。"
    - "HOT V5.19–V5.21 晚於 cutoff，不得出現在本節 current state。"
  current_scene:
    date: "理火三年荷月初三"
    time: "清晨／天亮後"
    location: "白家／李瓶兒房中"
    state:
      - "白御行與李瓶兒昨夜私人成人事件後相擁睡下，天已亮。"
      - "初三中午商會慶功、錦棠舞訓試談、巨床送抵與下午浮香熱工試驗均尚未發生。"
  major_finance:
    aliya:
      gross_sale: "3000萬兩"
      guanzhi_platform_fee: "300萬兩 / 10%"
      aliya_net: "2700萬兩"
      ownership: "阿麗婭本人"
    xialian:
      gross_sale: "5000萬兩"
      guanzhi_platform_fee: "500萬兩 / 10%"
      xialian_net: "4500萬兩"
      ownership: "夏蓮本人"
    guanzhi_total_platform_income_from_two_sales: "800萬兩"
    locks:
      - "兩名女子所得不屬白御行或定陶商會。"
      - "白紗帳內成人真實未因五千萬成交自動確證。"
  route_people:
    li_pinger:
      - "白家如夫人／女主人級位置持續。"
      - "初二深夜本次成人事件與一次明示同意的陰道內射成立；受孕 UNKNOWN。"
      - "當夜要求只要兩人，不形成永久排他。"
    li_shishi:
      - "白家首席如夫人／女主人級位置持續；截至 E126 尚未進入 V5.19 的確診妊娠事件。"
    gu_qingjian:
      - "既有地下私人關係與商會法律／帳務位置持續。"
      - "沈萬三資金池談判方向已由白御行交給她，但尚無最終契約。"
    jintang:
      - "正式商演／代理契約有效，直接可歸因品牌淨利分成24%。"
      - "與白御行初一『一天的男人／女伴』公開角色已結束，不升格永久名分。"
      - "關盼盼舞訓只到試談方向。"
    she_fangzhi:
      - "E122 正式進白御行 Route；官府指定觀止收容／強制妓籍背景有效。"
      - "女性社會／官方身份、男性身體、妓籍資格與私人偏好保持分軸。"
      - "E124 公開競技中磚塊九塊勝出；精確身體尺寸仍 UNKNOWN。"
      - "E126 同意紅娘借宿／共床睡眠，不成立成人事件。"
    hongniang:
      - "已復牌；舊床劈解／燒柴處分完成。"
      - "E126 因無舊床而借宿舍方知房，未越界。"
    guan_panpan:
      - "已實際進 Route；湖心島燕子樓舊債與破曉一舞成立。"
      - "潘金蓮提供免費廂房暫住；未形成觀止雇傭／轉籍。"
    xialian:
      - "一夜掛牌期限已結束；五千萬成交與本人四千五百萬所得成立。"
      - "暫住觀止；未形成觀止雇傭／妓籍轉移。"
  pending_day_schedule:
    - "初三中午定陶商會補假慶功宴。"
    - "關盼盼×錦棠舞訓試談／試課。"
    - "白家巨床預定送抵／組裝。"
    - "初三下午浮香小宅『會呼吸的房子』熱工實測。"
  vacation_proposal:
    - "白御行提議等阿麗婭／夏蓮大額帳務理順後帶家裡人與錦棠去湖心島住幾日。"
    - "李瓶兒表示喜歡並要去；其他人尚未逐一接受。"
```

---

# 6｜V5.18 帳務／契約硬狀態

```yaml
LEDGER_CONTRACT_STATE_V5_18:
  established:
    - "錦棠正式商演／代理契約有效；直接可歸因品牌淨利分成24%。"
    - "阿麗婭三千萬／夏蓮五千萬成交公帳與觀止10%平台抽成成立。"
    - "夏蓮／阿麗婭本人所得權不因觀止抽成改變。"
  not_yet_contract:
    - "沈萬三短池／長池／聯合池。"
    - "潘金蓮×關盼盼留人合約。"
    - "關盼盼×錦棠舞訓費用／堂數／期限。"
    - "浮香房熱工成果後的觀止整體改造。"
    - "湖心島家庭度假日期／名單／船房安排。"
```

---

# 7｜V5.18 未決／禁止偷補

```yaml
OPEN_AND_LOCKS_V5_18:
  - "李瓶兒本夜內射 != 懷孕；受孕 UNKNOWN。"
  - "李瓶兒本夜獨佔時間 != 永久排他。"
  - "紅娘×舍方知共床睡眠 != 成人事件。"
  - "舍方知精確尺寸、對男性私人性吸引、是否願接男客均 UNKNOWN。"
  - "夏蓮五千萬白紗帳公開觀感 != 帳內性交客觀證明。"
  - "關盼盼暫住觀止 != 雇傭／妓籍。"
  - "夏蓮暫住觀止 != 雇傭／轉籍。"
  - "巨床預定到貨 != 已組裝完成。"
  - "浮香熱工試驗預定 != 已成功。"
  - "錦棠受邀家庭度假 != 白家正式成員。"
```

---

# 8｜較新有效 HOT 疊加【保留三個，不倒灌 V5.18 cutoff】

```yaml
NEWER_HOT_OVERLAY:
  order: ["HOT V5.19", "HOT V5.20", "HOT V5.21"]
  count: 3
  rule:
    - "Normal resume 以 MASTER V5.18-HARD + paired RCL V5.18 為基底，再依序疊 V5.19 → V5.20 → V5.21。"
    - "HOT V5.19–V5.21 可改變後續 current state，但不得反寫 E01–E126 是否發生。"
    - "HOT V5.14–V5.18 已 promotion，不再作 Normal STORY overlay。"
```

---

# 9｜舊 SAVE 法位清理

```yaml
SAVE_SUPERSESSION:
  current_master: "MASTER V5.18-HARD"
  current_rcl: "RCL V5.18 / schema V1.1"
  retired_current_master:
    MASTER_V5_13_R1_HARD:
      role: "VALID PARENT PROVENANCE / ROLLBACK / REGRESSION"
      normal_resume_required: false
  retired_current_rcl:
    RCL_V5_13_R1:
      role: "VALID PARENT / READ-ONLY / ROLLBACK"
      normal_resume_required: false
  promoted_hot_sources:
    HOT_V5_14: {role: "PROMOTED_TO_E122 / DETAIL_FALLBACK", normal_resume_required: false}
    HOT_V5_15: {role: "PROMOTED_TO_E123 / DETAIL_FALLBACK", normal_resume_required: false}
    HOT_V5_16: {role: "PROMOTED_TO_E124 / DETAIL_FALLBACK", normal_resume_required: false}
    HOT_V5_17: {role: "PROMOTED_TO_E125 / DETAIL_FALLBACK", normal_resume_required: false}
    HOT_V5_18: {role: "PROMOTED_TO_E126 / DETAIL_FALLBACK", normal_resume_required: false}
```

---

# 10｜MASTER V5.18 × RCL 原子更新要求

```yaml
MASTER_RCL_ATOMIC_COMMIT:
  memory_generation: "V5.18"
  master:
    file: "觀止青樓_白御行線_MASTER_SAVE_V5.18-HARD_全歷史自足_E01-E126_截至HOT_V5.18固化_保留V5.19-V5.21_HOT版.md"
    record_version: "V5.18-HARD"
    event_range: "E01-E126"
    cutoff: "理火三年荷月初三清晨"
  rcl:
    file: "觀止青樓_白御行線_人物履歷_RCL_V5.18_MASTER_E01-E126_SCHEMA_V1.1_65人對齊版.md"
    version: "V5.18"
    schema: "GUANZHI_RCL_SCHEMA_V1_1"
  rule:
    - "MASTER 與 RCL 為同一 memory generation。"
    - "不得拿本 MASTER 搭配舊 RCL V5.13-R1 作 current route memory。"
```

---

# 11｜MASTER V5.18 回歸檢查

```yaml
VALIDATION:
  event_range: {expected: "E01-E126", status: "PASS"}
  promotion_chain:
    expected: ["E122 <- HOT V5.14", "E123 <- HOT V5.15", "E124 <- HOT V5.16", "E125 <- HOT V5.17", "E126 <- HOT V5.18"]
    status: "PASS"
  post_master_hots: ["V5.19", "V5.20", "V5.21"]
  forward_contamination_from_v5_19_plus: false
  unresolved_states_preserved: true
  master_rcl_atomic_pair_required: true
  status: "READY"
```


---

<!-- COMPILE_PRE_FOOTER_SHA256: d49d9208713f51348751be7e336f0cd86c97faa7536fc3a8cf6156e644ff86e4 -->
