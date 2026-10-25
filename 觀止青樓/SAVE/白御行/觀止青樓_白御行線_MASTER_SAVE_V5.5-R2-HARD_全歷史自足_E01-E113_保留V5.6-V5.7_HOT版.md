# 觀止青樓｜白御行線 MASTER SAVE V5.5-R2-HARD
## 截至 HOT V5.5｜E01–E113 全歷史自足硬化整合版｜保留 HOT V5.6【REBUILD-R1】–V5.7 為較新有效疊加層
### SELF-CONTAINED HARD MASTER｜OLD MASTER CHAIN RETIREMENT CANDIDATE

```yaml
SAVE_META:
  save_id: "GUANZHI_BAIYUXING_MASTER_V5_5_R2_HARD_SELF_CONTAINED_E01_E113"
  title: "觀止青樓｜白御行線 MASTER SAVE"
  version: "V5.5-R2-HARD"
  world: "觀止青樓"
  player: "白御行"
  route_status: "ACTIVE"
  record_type: "SELF_CONTAINED_HARD_CONSOLIDATED_MASTER_ARCHIVE"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  document_date: "2026-08-24"

  fixed_calendar_anchor: "理火三年槐月五日｜永恆第一夜"
  master_cutoff: "理火三年榴月二十四日清晨｜HOT V5.5"
  last_canonical_master_event: "E113"

  reorganization_only: true
  world_time_advanced: false
  new_story_event_created: false

SELF_CONTAINMENT:
  canonical_event_range: "E01-E113"
  parent_master_required_for_normal_story: false
  parent_master_required_for_deep_master_history: false
  old_master_chain_runtime_dependency: false
  raw_hot_files_required_for_normal_resume: false
  raw_hot_files_role: "OPTIONAL_DETAIL_FALLBACK / PROVENANCE / AUDIT"

  hard_rule:
    - "本檔直接保存 E01-E113 的 MASTER 級因果，不再以 V5.5→V5.1→V4.5→... 的父 MASTER 鏈作讀取前提。"
    - "較早 MASTER 可在本檔驗證通過後退出 Active／Deep Archive 必載鏈。"
    - "舊 MASTER 的歷史截止快照不得覆寫本檔較新狀態。"

SOURCE_MASTER_MANIFEST:
  - file: "觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md"
    sha256: "b39939a7f9a42ed781f432a78915c18837da8508a7f5edb4fef377122c77c47e"
    unique_canonical_range: "E01-E45"
  - file: "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"
    sha256: "efb47cfbf79f75244d5a62dcfbe57a855d04535cc9e02a264a57483b60056b85"
    unique_canonical_range: "E46-E77"
  - file: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"
    sha256: "9000d757cd525bf05d9c0b0d9dba454d9c245a2048d780d3b6da3a11a25b2e8b"
    unique_canonical_range: "E78-E83"
  - file: "觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md"
    sha256: "0149362b4128d62d947d4ffbcc618003913b1cad7052d57fe5b3f84f8f05084f"
    unique_canonical_range: "E84-E92"
  - file: "觀止青樓_白御行線_MASTER_SAVE_V4.4-R1_截至HOT_V4.0固化_保留V4.1-V4.4_HOT版.md"
    sha256: "40c570139367348e3c2b5e623b7baa7c27955bc1cc187d44db53eb8877b82203"
    unique_canonical_range: "E93-E98"
  - file: "觀止青樓_白御行線_MASTER_SAVE_V4.5-R1_截至HOT_V4.5固化_保留V4.6-V5.0_HOT版.md"
    sha256: "7bce803cf35fcc5a67906468fdbaa7cf125f11b3e0916097212c5a523293b3ee"
    unique_canonical_range: "E99-E103"
  - file: "觀止青樓_白御行線_MASTER_SAVE_V5.1-R1_截至HOT_V5.1固化_保留V5.2-V5.5_HOT版.md"
    sha256: "0b72e52a9d50d54779f4617a7ec79803ae3a9194f97c0d34bcc139e112137688"
    unique_canonical_range: "E104-E109"
  - file: "觀止青樓_白御行線_MASTER_SAVE_V5.5-R1_截至HOT_V5.5固化_保留V5.6-V5.7_HOT版.md"
    sha256: "2bf6ecb14d4d99a96030d8a41b213f723faf9a9dc0cfa12ec2ee2c2c9a8afd95"
    unique_canonical_range: "E110-E113 + HOT V5.5 current state"

CURRENT_ROUTE_OVERLAY:
  - "HOT V5.6【REBUILD-R1】"
  - "HOT V5.7"

INVALID_OR_SUPERSEDED_SAVE_LOCK:
  - source: "HOT V1.3"
    status: "ILLEGAL_CORRUPTED_SAVE / AUDIT_ONLY"
  - source: "HOT V3.6"
    status: "SUPERSEDED"
    replacement: "HOT V3.6-R2"
  - source: "HOT V3.6-R1"
    status: "SUPERSEDED"
    replacement: "HOT V3.6-R2"
  - source: "舊 HOT V5.6｜失仙官籍暗查／紅娘蛋局品牌化／雙環境接線版"
    status: "VOIDED_SUPERSEDED"
    replacement: "HOT V5.6【REBUILD-R1】"

MASTER_AUTHORITY:
  - "EVENT HISTORY 與 CURRENT STATE 分層。"
  - "歷史事件發生後，後續可以改變狀態，但不能把事件從歷史抹掉。"
  - "當前狀態以本檔『HOT V5.5 CURRENT HARD STATE』為 V5.5 截止最高 Master 切面。"
  - "HOT V5.6【REBUILD-R1】與 V5.7 只作較新 overlay，不倒灌 V5.5 cutoff。"
  - "UNKNOWN / PENDING / DISPUTED / NOT_PLAYED 保持合法，不為了自足而補全。"
```

> **這一版的目的不是再摘要一次，而是斬斷舊 MASTER 的父子依賴鏈。**
>
> **E01–E113 在本檔內直接可讀；正常接關只需本 HARD MASTER，再疊 HOT V5.6【REBUILD-R1】與 HOT V5.7。**

---

# 0｜HARD SAVE 讀法

```yaml
HARD_READ_ORDER:
  normal_resume:
    1: "本 MASTER V5.5-R2-HARD"
    2: "HOT V5.6【REBUILD-R1】"
    3: "HOT V5.7"

  when_current_state_conflicts_with_old_event_snapshot:
    rule:
      - "事件是否發生：讀 EVENT LEDGER。"
      - "截至 HOT V5.5 現在是什麼：讀 CURRENT HARD STATE。"
      - "HOT V5.6-V5.7 後續變化：讀 overlay。"

  when_deep_detail_is_needed:
    preferred:
      - "對應原 HOT"
    not_required:
      - "舊 MASTER 父鏈"

  no_revival:
    - "歷史 OPEN HOOK snapshot 不得因仍被保存而自動復活。"
    - "舊 PENDING 若後續已有結果，以後續結果為準。"
```

---

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

# 5｜HOT V5.5 CURRENT HARD STATE｜最新 MASTER 截止硬狀態

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

# 6｜較新有效 HOT 疊加

## 8｜MASTER V5.5-R1 與 HOT V5.6【REBUILD-R1】–V5.7 疊加規則

```yaml
NEWER_OVERLAY_RULE:

  valid_chain:
    - "MASTER V5.5-R1"
    - "HOT V5.6【REBUILD-R1】"
    - "HOT V5.7"

  v5_6:
    valid_file: "觀止青樓_白御行線_HOT_SAVE_V5.6_REBUILD-R1_榴月二十四日白日_柳永趙受益白家會議_失仙五百兩觀察實驗_完整版.md"
    treatment:
      - "可更新本 MASTER 截止後的榴月二十四日白日事件。"
      - "若與本 MASTER 的 PENDING／UNKNOWN 後續狀態衝突，以 V5.6【REBUILD-R1】較新硬事件為準。"

  v5_7:
    file: "觀止青樓_白御行線_HOT_SAVE_V5.7_榴月二十四日夜_醉花陰三人事件_蘇清體內射精_甜鹽水_白家小屋構想版.md"
    treatment:
      - "為目前最新有效 HOT。"
      - "可更新 V5.6 之後至榴月二十四日夜的事件與關係。"

  invalid_v5_6:
    rule:
      - "舊 V5.6 已 VOIDED／SUPERSEDED。"
      - "不得因舊檔較早生成就參與衝突平均。"
      - "只能留作 CORRUPTION LOG／回歸樣本。"

  anti_backflow:
    - "V5.6／V5.7 不得被描述成在 V5.5 截止時已經發生。"
    - "人物在 V5.5 的知情不得由 V5.6／V5.7 後見之明補全。"
```

---

## 9｜正常接關最小載入包

```yaml
MINIMUM_RESUME_PACKAGE:
  required:
    - "MASTER V5.5-R1（本檔）"
    - "HOT V5.6【REBUILD-R1】"
    - "HOT V5.7"

  optional_deep_history:
    - "MASTER V5.1-R1"
    - "更早 MASTER / HOT"

  optional_source_detail:
    - "HOT V5.2"
    - "HOT V5.3"
    - "HOT V5.4"
    - "HOT V5.5"

  instruction:
    - "正常 STORY 不應為了重建榴月十九日至二十四日清晨而逐份重載 V5.2-V5.5。"
    - "只有遇到本 MASTER 未保存的逐項帳目、原句、局部知情或審計爭議時，才回查對應 HOT。"
```

---

## 6.1 HARD MASTER 後的正常接關包

```text
MASTER V5.5-R2-HARD
+
HOT V5.6【REBUILD-R1】
+
HOT V5.7
```

舊 MASTER V4.0／4.1／4.2／4.3／4.4／4.5／V5.1／舊 V5.5-R1 不再是正常接關或 deep-master-history 的必要依賴。

---

# 7｜LEGACY OPEN HOOK SNAPSHOTS｜遺失鉤子審計附錄

> **本區不是 ACTIVE OPEN THREAD LIST。**
>
> 它只保留舊 MASTER 在各歷史 cutoff 曾標記過的未決事項，避免清掉舊 MASTER 後連「曾經有這個未決」都消失。
>
> 使用規則：
>
> - 若 E01-E113 或 CURRENT HARD STATE 已給出後續結果，舊 PENDING 不得復活。
> - 若後續完全沒有任何結果或覆寫，才可在 AUDIT 模式把它標成 `DORMANT_UNRESOLVED_CANDIDATE`。
> - 不得為了讓舊鉤子有答案而補寫世界事件。

### MASTER V4.0-R1 / HOT V1.4 cutoff

> 法位：`AUDIT_ONLY_HISTORICAL_SNAPSHOT`。若後續事件已解決，不能用本段把舊 PENDING 復活；若後續完全沒有狀態，才可作遺失鉤子審計入口。

#### 10｜未完成伏筆（OPEN HOOKS）

##### 10.1 關係與人物

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

##### 10.2 觀止營運與世界事件

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

##### 10.3 帳目與交付

1. 李師師設席牌製作與開席公告。
2. 紅娘氏第一筆交易的房錢、身錢、消息訂金精確入帳。
3. 紅袖冰蠶弦逾期結果。
4. 二十兩說書資金實際轉付。
5. 十塊木板實際送達。
6. 蘇清稿酬是否成交。
7. 張麗華一萬兩酒帳實際使用額。
8. 小翠按摩服務金額與服務完成紀錄。

---

### MASTER V4.1-R1 / HOT V1.9 cutoff

> 法位：`AUDIT_ONLY_HISTORICAL_SNAPSHOT`。若後續事件已解決，不能用本段把舊 PENDING 復活；若後續完全沒有狀態，才可作遺失鉤子審計入口。

#### 20｜截至 HOT V1.9 未決事項

##### 20.1 立即接關

1. 張麗華洗浴後如何分配白御行、蘇清、李瓶兒之睡處。
2. 李瓶兒只接受當晚留宿；任何同床、裸體、觸碰或性交均未決。
3. 蘇清與張麗華、白御行之兩日共同生活如何繼續。
4. 寢具、熱水、薄被與三只恭桶是否實際送達。

##### 20.2 張麗華

1. 槐月十六日晚私人花燭之完整執行情況在 V1.7–V1.8 間有來源缺口，不得補寫。
2. 酒莊花農款、年度週轉與一萬兩法位。
3. 三日陪伴如何起算、完成與結束。
4. 她如何處理白御行多重關係與不欺瞞要求。

##### 20.3 李師師／師理理

1. 槐月十一日體內射精是否造成妊娠。
2. 月事是否如期、是否找到可靠女醫、避子方式是否取得。
3. 新招數欠帳何時處理。
4. 紅娘氏三人親密只屬討論，尚未邀請。

##### 20.4 李瓶兒

1. 是否接受任何長期秘密位置。
2. 是否認為自己真正被選擇，而非方便隱藏。
3. 當晚留宿後之睡處與親密界線。

##### 20.5 白玉池

1. 暫閉合是否持續、是否在別處重開。
2. 提燈女子、未知聲音、黑影、鞋、白點與多天空映像之身分與機制。
3. 活物／標記／聲音跨界測試之個體同一性與時間問題。
4. 阿泠與 MASTER 早期白玉池無名女子是否同一存在，仍不得合併。
5. 水療何時可重新評估；無 GM 授權不得復開。
6. 時空道人正式補籤。

##### 20.6 定陶商會

1. 吳六下落與罪責。
2. 五名逃犯。
3. 灰簿先生本體。
4. 借支申請抄件外洩路徑。
5. 押送者個別最終處置。
6. 白御行所稱親手殺死之背叛者名冊、正式紀錄與家屬援助執行。
7. 六烤運京後市場與信用結果。
8. 一個月交叉審計與六個月急難護持案評估。

---

### MASTER V4.2-R1 / HOT V2.5 cutoff

> 法位：`AUDIT_ONLY_HISTORICAL_SNAPSHOT`。若後續事件已解決，不能用本段把舊 PENDING 復活；若後續完全沒有狀態，才可作遺失鉤子審計入口。

#### 7｜截至 HOT V2.5 未決事項

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

### MASTER V4.3-R1 / HOT V3.4 cutoff

> 法位：`AUDIT_ONLY_HISTORICAL_SNAPSHOT`。若後續事件已解決，不能用本段把舊 PENDING 復活；若後續完全沒有狀態，才可作遺失鉤子審計入口。

#### 7｜截至 HOT V3.4 未決事項

```yaml
OPEN_HOOKS_AT_V3_4:
  emperor_event:
  - 潘金蓮完整三日籌備方案
  - 六條是否出席
  - 紅娘以何角色參與
  - 阿麗婭／六百兩候選／辭歲是否各自同意任何競價企畫
  - 白玉池是否能合法具備使用條件
  - 大觀樓座次、酒菜、節目、房間、價格、公帳核銷上限
  - 完整帝皇來客名單與交接實際衝突
  shisanniang_national_fortune:
  - 個人／家族／朝代／公帳國運的可持有與轉讓法位
  - 城隍司現場估價與合法轉移程序
  - 首飾存儲機制與上限
  hongniang_side_bet:
  - V3.4 截止為紅娘已輸、一次三人親密賭債尚未執行；更晚如何處置由 HOT 疊加覆寫。
  xiaocui:
  - 向青禾學按摩只是提案
  - 與白三娘雙人服務未成固定工作
  - 有限實習是否會轉成一般客人的能力仍未知
  shen_wanshan_panel:
  - 高端客戶座談尚未真正由潘金蓮立案、沈萬三未被邀請／到場。
  white_house:
  - 李師師第一版設計、李瓶兒／張麗華／潘金蓮會審、空間穩定、施工與真正租約啟動。
  civil_and_status:
  - 蘇清 vs 潘金蓮五萬請求與五千原款處理
  - 潘金蓮進西門家及重新從妓資格
  - 西門慶及相關刑民責任終局。
  white_jade_pool:
  - 正式復開驗收、許願幣材質／匯率／SPA 價格、阿泠實際定存契約。
  fashion_and_business:
  - 曹州假印案結果、京師女性奢侈品店、肚兜發表會、人物專屬款、外邀人物是否接受等均仍依事件推進。
  fate_stick: 槐月二十六日命運籤「一門踏出千燈遠／回首春風不認人」沒有合法解籤；不得補命定答案。
```

---

### MASTER V4.4-R1 / HOT V4.0 cutoff

> 法位：`AUDIT_ONLY_HISTORICAL_SNAPSHOT`。若後續事件已解決，不能用本段把舊 PENDING 復活；若後續完全沒有狀態，才可作遺失鉤子審計入口。

#### 7｜截至 HOT V4.0 的未決事項

```yaml
OPEN_AT_MASTER_CUTOFF_V4_0:
  guanzhi_reopening:
    - "十日整修尚未完成；重開的具體開幕流程仍由較新 HOT V4.1–V4.4 繼續形成。"

  cao_zhou:
    - "V4.0 截止仍 ACTIVE；後續結果必須讀 V4.2。"

  maid_selection:
    - "V4.0 截止尚未發生榴月四日九人丫鬟遴選；不得從 MASTER cutoff 預知 V4.1 結果。"

  jintang:
    - "錦棠與白御行之戀愛承諾仍未對等完成。"

  rokujo_yang_zhao:
    - "三人約會未定日期、未發生。"

  redniang_stage:
    - "中央籠台概念已接入，但實際開幕壓軸表演屬 V4.4 overlay，不能倒寫成 V4.0 已發生。"
```

---

### MASTER V4.5-R1 / HOT V4.5 cutoff

> 法位：`AUDIT_ONLY_HISTORICAL_SNAPSHOT`。若後續事件已解決，不能用本段把舊 PENDING 復活；若後續完全沒有狀態，才可作遺失鉤子審計入口。

#### 7｜截至 HOT V4.5 的未決事項

```yaml
OPEN_THREADS_AT_MASTER_CUTOFF_V4_5:
  li_shishi:
    - "孕否 UNKNOWN；月事延遲只提高懷疑。"

  cao_zhou:
    - "真實網絡、何先生法位、後續江湖動向 UNKNOWN；白御行本人已止手。"

  maid_followups:
    - "V4.1 制服與三名自願剪髮方案是否全部按原計畫完成，若無後續來源不得補寫。"

  suqing:
    - "榴月十一日晚碰見者身分與私人事件 UNKNOWN。"
    - "商會十八日工作尚未在 V4.5 截止開始；榴月十三日起算。"

  four_guards:
    - "紅伶、三十二娘榴月十二日晚最後是否選男人／離場／發生私人成人事件 UNKNOWN。"
    - "三十二娘妓籍申請尚未完成。"

  white_jade:
    - "會員首夜四組最終完整名單、每次使用費、是否已有第一組實際入池完成 UNKNOWN。"

  pan_bai:
    - "一場決勝負日期、內容、結果 UNKNOWN。"

  xiaotao:
    - "是否實際同宿到天亮：HOT V4.5 截止未完成。"
    - "下一次預付50兩何時／是否履行：PENDING。"
    - "小桃何時得知黑公子真身：UNKNOWN。"

  white_home:
    - "正式落地、入住與最終空間結構尚未發生；由較新 HOT 決定。"
```

---

### MASTER V5.1-R1 / HOT V5.1 cutoff

> 法位：`AUDIT_ONLY_HISTORICAL_SNAPSHOT`。若後續事件已解決，不能用本段把舊 PENDING 復活；若後續完全沒有狀態，才可作遺失鉤子審計入口。

#### 7｜截至 HOT V5.1 的主要未決事項

```yaml
OPEN_THREADS_AT_MASTER_CUTOFF_V5_1:
  li_shishi:
    - "是否懷孕仍未確診。"

  rokujo_ten_day_bet:
    - "十日賭約仍有效。"
    - "截至 V5.1 白御行尚未完成後來 V5.3 才成立的指定事件；不得提前宣告勝負。"
    - "六條同意仍只能逐次由本人建立。"

  hongniang_bai:
    - "兩人未來對賭／私約仍可能發展，但 V5.4 新鐵籠床火賭尚未發生。"

  gu_qingjian:
    - "未來私密玩法、商會正式職位、人才培訓角色都尚未被一次性決定。"

  secretary_room_and_training:
    - "仍是構想／設計階段；正式組織、人數、薪資、規章待定。"

  theme_room:
    - "女性市場與抓姦遊戲尚未正式開售。"

  chen_goldmask:
    - "金面具身份、房內內容 UNKNOWN。"

  su_yu:
    - "蘇東坡×魚玄機房內內容 UNKNOWN。"

  xuetao:
    - "匿名身份對白御行仍未正式揭露。"

  pan_bai:
    - "原先『一場決勝負』成人私約仍未被 V5.1 帳房小試完全取代／兌現。"

  aling_water_shell:
    - "只證明一次短暫成功；最大體積、持續時間、複雜控制仍 UNKNOWN。"
```

---



---

# 8｜舊 MASTER 清理法位

```yaml
OLD_MASTER_DISPOSITION_AFTER_HARD_MASTER_ACCEPTANCE:

  may_retire_from_active_and_deep_load:
    - "觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版 (1).md"
    - "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"
    - "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"
    - "觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md"
    - "觀止青樓_白御行線_MASTER_SAVE_V4.4-R1_截至HOT_V4.0固化_保留V4.1-V4.4_HOT版.md"
    - "觀止青樓_白御行線_MASTER_SAVE_V4.5-R1_截至HOT_V4.5固化_保留V4.6-V5.0_HOT版.md"
    - "觀止青樓_白御行線_MASTER_SAVE_V5.1-R1_截至HOT_V5.1固化_保留V5.2-V5.5_HOT版.md"
    - "觀止青樓_白御行線_MASTER_SAVE_V5.5-R1_截至HOT_V5.5固化_保留V5.6-V5.7_HOT版.md"

  recommended_treatment:
    - "先確認本檔 E01-E113 完整性與 HASH。"
    - "若要節省倉庫位置，可刪除舊 MASTER；不影響正常接關。"
    - "若保留，法位降為 SOURCE_PROVENANCE / ROLLBACK_SOURCE，不再平行載入。"

  raw_hot_policy:
    - "本次不宣告 HOT 原檔可全部刪除。"
    - "HOT 仍可保留作逐句細節、原始帳目、局部知情與回歸核對。"
```

---

# 9｜HARD MASTER 回歸檢查

```yaml
HARD_MASTER_REGRESSION:
  H01_EVENT_RANGE:
    expected: "E01-E113 exactly once"

  H02_CUTOFF:
    expected: "HOT V5.5 / 理火三年榴月二十四日清晨"

  H03_OVERLAY:
    expected:
      - "HOT V5.6【REBUILD-R1】"
      - "HOT V5.7"

  H04_INVALID_SOURCES:
    expected:
      - "HOT V1.3 audit only"
      - "HOT V3.6/R1 superseded by R2"
      - "old HOT V5.6 voided"

  H05_PRIVATE_SECRET:
    expected: "PSE-WY-ZLH-001 boundary preserved"

  H06_UNKNOWN:
    expected: "UNKNOWN / PENDING / DISPUTED remain legal"

  H07_NO_PARENT_DEPENDENCY:
    expected: "Normal and deep-master load do not require old MASTER files"

  H08_NO_FORWARD_CONTAMINATION:
    expected: "HOT V5.6-V5.7 not backfilled into V5.5 cutoff"

  H09_LEGACY_HOOKS:
    expected: "historical hook snapshots are audit-only, not auto-reactivated"
```

---

# 10｜一句話

> **這份 HARD MASTER 把白御行線截至 HOT V5.5 的 E01–E113 因果直接收進同一個自足檔；舊 MASTER 從「父鏈」降為「可退役來源」，最新世界仍由 V5.6【REBUILD-R1】與 V5.7 往前疊。**
