# 觀止青樓｜花滿樓線人物履歷 RCL V1.5
## 與 MASTER SAVE V1.5-HARD 同代｜E01–E18｜LCAPG V3.3.18／67人對齊｜HOT V1.6–V1.9 不吸收
### GUANZHI_RCL_SCHEMA_V1_1_COMPATIBLE｜SAME-GENERATION ATOMIC PAIR｜FIRST GENERATION

```yaml
DOCUMENT:
  title: "觀止青樓｜花滿樓線人物履歷"
  short_id: "RCL-HML"
  version: "V1.5"
  memory_generation: "V1.5"
  schema: "GUANZHI_RCL_SCHEMA_V1_1_COMPATIBLE"
  document_type: "COMPILED_ROUTE_CHARACTER_LEDGER"
  status: "MASTER_DERIVED / SAME_GENERATION_ATOMIC_PAIR / FIRST_GENERATION"
  compile_date: "2026-10-01"

ROUTE:
  route_id: "GUANZHI_NEW_INDEPENDENT_PLAYER_ROUTE_HUAMANLOU"
  player: "花滿樓"
  route_status: "ACTIVE"

COMPILED_FROM:
  master_file: "觀止青樓_花滿樓線_MASTER_SAVE_V1.5-HARD_全歷史自足_E01-E18_截至HOT_V1.5固化_保留V1.6-V1.9_HOT版_20261001.md"
  master_sha256: "e91736bc42dddd2669d060964a258a3513697fa05961b6ebb654d2ec7b62eebe"
  master_memory_generation: "V1.5"
  master_record_version: "V1.5-HARD"
  canonical_event_range: "E01-E18"
  cutoff_event: "E18"
  cutoff_time: "理火三年菊月初三巳正前後"
  parent_rcl_file: "NONE_FIRST_GENERATION"
  parent_rcl_version: "NONE"
  lcapg_file: "觀止人物卡池_LCAPG_V3.3.18_照夜三聖母_紫蘭主唱_67人完整整合版.md"
  lcapg_version: "V3.3.18"
  lcapg_sha256: "598d544ce9fb1bcea73aa6f92d93c95434f9ab5d1a52b9662f7c8611461ee266"

POST_MASTER_OVERLAY_EXCLUDED_FROM_THIS_COMPILE:
  - "HOT V1.6"
  - "HOT V1.7"
  - "HOT V1.8"
  - "HOT V1.9"

VERSION_ALIGNMENT:
  memory_generation: "V1.5"
  master_record: "V1.5-HARD"
  rcl_record: "V1.5"
  schema: "GUANZHI_RCL_SCHEMA_V1_1_COMPATIBLE"
  atomic_pair_required: true

EXECUTION_EVIDENCE:
  local_rcl_file_created: true
  host_save_commit: "NOT_ESTABLISHED"
  host_e6: "NOT_ESTABLISHED"
  host_e7: "NOT_ESTABLISHED"
  formal_ceri_provider_execution: "NOT_ESTABLISHED"
  independent_multi_model_agent_execution: "NOT_ESTABLISHED"
```

> **LCAPG 是人物基線；MASTER 是已發生事件；RCL 是人物截至 E18 在花滿樓線站在哪裡。**
>
> 本版是花滿樓線第一次 RCL。只編譯 **MASTER V1.5-HARD／E01–E18** 已有證據；HOT V1.6–V1.9 是較新的正常續玩 overlay，不得倒灌到本代人物狀態。

---

# 1｜讀取規則

```text
LCAPG V3.3.18 BASE / 67
↓
本 RCL V1.5 CURRENT ROUTE RECORDS
↓
MASTER V1.5-HARD E## detail when needed
↓
HOT V1.6 → HOT V1.7 → HOT V1.8 → HOT V1.9
↓
CURRENT LIVE STATE
```

固定鎖：

```text
RCL SUMMARY != MASTER EVENT BODY
LCAPG BASE != PLAYER ROUTE STATE
LCAPG BASE EXISTS != ROUTE ENTRY
EVENT PARTICIPATION != FULL KNOWLEDGE
CHARACTER SELF-REPORT != OBJECTIVE WORLD TRUTH
MASK REMOVAL != PUBLIC IDENTITY
KISS != FUTURE ACCESS
ADULT EVENT != LOVE
ADULT EVENT != FUTURE CONSENT
CONTRACT != RELATION
PAYMENT != ACCESS != RELATION != CONSENT
INVITE != ACCEPTANCE != ARRIVAL
LATER REVEAL != EARLIER KNOWLEDGE
HOT V1.6+ != MASTER V1.5 CUTOFF
```

---

# 2｜PLAYER ROUTE RECORD｜花滿樓

```yaml
PLAYER:
  name_in_route: "花滿樓"
  identity_class: "PLAYER CHARACTER"
  public_name_status: "ESTABLISHED"
  true_name_at_E18: "UNKNOWN"
  origin_family_at_E18: "UNKNOWN"
  residence_at_E18: "UNKNOWN"
  financial_profile_at_E18: "NOT_YET_CONSOLIDATED"
  relation_lifecycle: "ACTIVE_PLAYER_ROUTE"

  evidence_event_ids:
    - E01
    - E02
    - E03
    - E04
    - E05
    - E06
    - E07
    - E08
    - E09
    - E10
    - E11
    - E12
    - E13
    - E14
    - E15
    - E16
    - E17
    - E18

  established_route_state:
    - "以花滿樓之名在觀止活動、寫詞、參與交易與仕女夜制度設計。"
    - "與照夜的人間安身約成立；實際官訟與安身成果尚未完成。"
    - "菊月初一參與首屆一炷香輪轉相親；與青雀留下菊月初八條件式再見前約。"
    - "與沈如晦完成一次雙方同意的成人事件；不因此建立戀愛、婚姻、排他或下一次成人權利。"
    - "接受薄櫻請託，以獨立第三方／旁聽與談判支援身份進入邵承祿六年帳契談判。"

  authored_works_at_cutoff:
    - "《鮮花滿月樓》"
    - "《滿庭芳·家後》"
    - "《七絕·南風惜別》"
    - "《鵲踏枝·曉別》"
    - "《蝶戀花·青雀離》"
    - "《青玉案·薄櫻》"
    - "《蝶戀花·薄櫻》"

  current_cutoff_location:
    - "菊月初三巳正前後，薄櫻母親留下的香料鋪後堂對帳房。"

  current_cutoff_present_with:
    - "薄櫻"
    - "邵承祿"
    - "捧帳冊小夥計"

  player_authority_lock:
    - "下一句重大言語、付款、承諾、接受／拒絕與不可逆選擇仍由玩家本人決定。"
```

---

# 3｜LCAPG CURRENT ROUTE RECORDS｜截至 E18

## 01｜潘金蓮

```yaml
route_presence: "ACTIVE_ROUTE_CHARACTER"
evidence_event_ids: [E03, E04, E07, E08, E09, E11, E12, E13]
relation_to_player: "觀止大掌櫃／營運、契約、制度與商業合作節點；未建立私人戀愛或固定成人關係。"
relation_lifecycle: "ACTIVE_CONSTRAINING"
current_route_state:
  - "見證並處理花滿樓作品、觀止酒帳／營運、醉花酒吧構想等樓內事務。"
  - "承認花滿樓本人今後入場與普通茶水免費；此優惠不等於全樓無限免單。"
  - "採納仕女夜巷與一炷香鴛鴦會方向，並承擔花滿樓首場報名費。"
  - "參與劉娥來源秘聞的隔音私談並受保密約束。"
knowledge_boundaries:
  - "知道劉娥秘聞談話內容，只在當時私席範圍。"
  - "不知道沈如晦私人成人場細節，除非後續取得來源。"
unresolved:
  - "夜巷長期營運、宮禁方向、官家邀帖結果、租戶與帳務。"
locks:
  - "SHOPKEEPER_COOPERATION != PRIVATE_RELATION"
  - "FREE_ENTRY_TEA != ALL_SERVICES_FREE"
```

## 02｜龐春梅

```yaml
route_presence: "ACTIVE_ROUTE_CHARACTER"
evidence_event_ids: [E11, E13]
relation_to_player: "觀止掌櫃／空間、通道、營運與保密協作節點；未建立私人戀愛或成人關係。"
relation_lifecycle: "ACTIVE_CONSTRAINING"
current_route_state:
  - "參與仕女夜巷、十閣輪轉與疑似宮禁端的空間／安全控制。"
  - "參與劉娥來源秘聞私談並受保密約束。"
unresolved:
  - "宮禁端真實連通與外部程序。"
locks:
  - "MANAGEMENT_ROLE != PLAYER_RELATION"
```

## 03｜蘇清

```yaml
route_presence: "ACTIVE_ROUTE_CHARACTER"
evidence_event_ids: [E13]
relation_to_player: "仕女夜商業模型／秘密談話協作人物；未建立花滿樓私人關係。"
relation_lifecycle: "ACTIVE_DORMANT"
current_route_state:
  - "參與仕女夜巷商業模型、准入分區、雅閣換席與女子自由出口設計。"
  - "參與劉娥來源秘聞私談並受保密約束。"
locks:
  - "DISCUSSION_PARTICIPATION != PRIVATE_RELATION"
```

## 04｜李桂姐

```yaml
route_presence: "ACTIVE_ROUTE_CHARACTER"
evidence_event_ids: [E02]
relation_to_player: "觀止大堂營業人物；與花滿樓無固定私人關係。"
relation_lifecycle: "ACTIVE_DORMANT"
current_route_state:
  - "在花滿樓初到觀止的大堂營業生活中具可觀察存在。"
locks:
  - "SAME_VENUE != PLAYER_RELATION"
```

## 05｜醉花

```yaml
route_presence: "ACTIVE_ROUTE_CHARACTER"
evidence_event_ids: [E02, E07, E10]
relation_to_player: "酒務／空間改造與藝事合作節點；未建立私人戀愛或固定成人關係。"
relation_lifecycle: "ACTIVE_DORMANT"
current_route_state:
  - "與花滿樓談出西側半圓高台酒吧方向，潘要求先由師傅量場與估價。"
  - "參與《陽關三疊》等藝事場景。"
unresolved:
  - "酒吧是否施工、成本與營運權。"
locks:
  - "DESIGN_COLLABORATION != PRIVATE_RELATION"
```

## 06｜浮香

```yaml
route_presence: "ACTIVE_ROUTE_CHARACTER"
evidence_event_ids: [E02, E03, E04, E10]
relation_to_player: "截至 E18 為觀止琴曲／藝事互動人物；尚未建立花滿樓成人史、戀愛或專屬關係。"
relation_lifecycle: "ACTIVE_DORMANT"
current_route_state:
  - "曾在大堂合奏／曲藝場景與花滿樓同場。"
  - "截至 MASTER V1.5 cutoff，HOT V1.8 的鬼滿樓留宿與成人事件尚未發生，不得倒灌。"
locks:
  - "HOT_V1_8_ADULT_EVENT != E18_STATE"
  - "MUSIC_INTERACTION != RELATION"
```

## 07｜照夜／三聖母

```yaml
route_presence: "ACTIVE_ROUTE_CHARACTER"
evidence_event_ids: [E08, E09, E13]
relation_to_player: "人間安身約之契約相對人；未建立已履行成人關係。"
relation_lifecycle: "ACTIVE_CONSTRAINING"
identity_axes:
  mythic_identity: "三聖母／照夜"
  public_route_name: "照夜"
  proposed_human_document_name: "楊蓮娘"
  human_document_status_at_E18: "NOT_COMPLETED"
  prostitution_registration_at_E18: "NOT_COMPLETED"
  freedom_status: "FREE_PERSON"
current_route_state:
  - "花滿樓承諾透過人間公堂爭得天庭不得合法依天條在人間拘拿她的實際安身效果。"
  - "她提出履約成功後另擇一夜的私人酬謝；尚未履行。"
  - "另有首次正式一夜成人陪宿競拍時按花滿樓實際所得三成支付的獨立條件性安排；競拍未發生。"
knowledge_boundaries:
  - "參與劉娥來源秘聞私談並受保密約束。"
unresolved:
  - "人間文牒、妓籍／自由從業契約、官訟、沉香與天庭後續。"
locks:
  - "CONTRACT_PROMISE != COMPLETED_RESULT"
  - "FUTURE_REWARD != CURRENT_CONSENT"
  - "MYTHIC_IDENTITY != HUMAN_REGISTRATION"
```

## 08｜紫蘭

```yaml
route_presence: "ACTIVE_ROUTE_CHARACTER"
evidence_event_ids: [E02, E03, E04, E10, E17]
relation_to_player: "主唱歌妓／詞曲合作人物；未建立花滿樓私人戀愛、成人或排他關係。"
relation_lifecycle: "ACTIVE_CONSTRAINING"
current_route_state:
  - "以初訪一小壺酒價取得《鮮花滿月樓》詞稿。"
  - "桂月二十二完成第一次公開試唱；唱紅與最終編曲結果截至 E18 未固化。"
  - "參與《陽關三疊》排演；終極演出要求尚未完成。"
  - "《蝶戀花·薄櫻》截至 E18 只有匿名送她試唱的計畫，尚未確證送達、看過、接受或開唱。"
locks:
  - "LYRIC_HOLDING != ROMANCE"
  - "PLANNED_ANONYMOUS_DELIVERY != DELIVERY"
```

## 09｜舍方知

```yaml
route_presence: "NOT_ENTERED_ROUTE_AT_E18"
base_ref: "LCAPG V3.3.18 / order 62"
current_route_state:
  - "E16 只把她的裁縫能力當成未來可用世界資源提及。"
  - "截至 E18 花滿樓尚未與她正式見面。"
locks:
  - "BASE_RESOURCE_MENTION != ROUTE_ENTRY"
```

---

# 4｜ROUTE-LOCAL／非 LCAPG 主要人物履歷

## 小桃

```yaml
route_presence: "ACTIVE_ROUTE_LOCAL_NPC"
evidence_event_ids: [E02, E08, E13, E16]
relation_to_player: "觀止跑堂／傳話與服務節點；有一次突來親吻事件，無固定私人關係。"
current_route_state:
  - "曾替花滿樓送菜、跑腿、處理房間與熱水。"
  - "E16 花滿樓突然抱住並親她一下；小桃明顯驚訝、生氣並以言語與踩鞋面反應。"
locks:
  - "SURPRISE_KISS_ESTABLISHED"
  - "SURPRISE_KISS != ROMANCE"
  - "SURPRISE_KISS != FUTURE_ACCESS"
```

## 青衣

```yaml
route_presence: "ACTIVE_ROUTE_LOCAL_MUSIC_NPC"
evidence_event_ids: [E02, E03, E04, E10]
relation_to_player: "觀止曲藝協作／排練人物；無私人關係。"
locks: ["MUSIC_COLLABORATION != PRIVATE_RELATION"]
```

## 柳黃

```yaml
route_presence: "ACTIVE_ROUTE_LOCAL_MUSIC_NPC"
evidence_event_ids: [E02, E03, E04, E10]
relation_to_player: "觀止曲藝協作／排練人物；無私人關係。"
locks: ["MUSIC_COLLABORATION != PRIVATE_RELATION"]
```

## 沈夫人

```yaml
route_presence: "ACTIVE_ROUTE_LOCAL_CLIENT"
evidence_event_ids: [E05]
relation_to_player: "《滿庭芳·家後》委託人。"
contract:
  total: "200兩"
  writer_fee: "20兩"
  wedding_gift_in_huamanlou_name: "180兩"
  work_delivered: true
current_cutoff_note:
  - "E18 時精確銀錢實際交付仍依 MASTER 帳務索引保持未完全結清；後續 HOT 可覆寫當前帳態。"
locks:
  - "COMMISSION != PRIVATE_RELATION"
```

## 阿蘅／陸夫人（桂月二十二客人）

```yaml
route_presence: "ACTIVE_ROUTE_LOCAL_GUEST"
evidence_event_ids: [E06]
relation_to_player: "私人題贈與一次自願短吻的舊客互動；無未來承諾。"
current_route_state:
  - "取得《七絕·南風惜別》《鵲踏枝·曉別》題贈。"
  - "與花滿樓有一次自願短吻。"
critical_identity_lock:
  - "本人物不得因後來鬼滿樓出現名為陸蘅／阿蘅的女鬼而自動合併；截至 E18 沒有證據證明兩者同一人。"
locks:
  - "KISS != RELATION"
  - "NAME_SIMILARITY != IDENTITY_MERGE"
```

## 王昭君

```yaml
route_presence: "ACTIVE_ROUTE_LOCAL_CROSS_TIME_CHARACTER"
evidence_event_ids: [E10]
relation_to_player: "《陽關三疊》與跨時代藝事線人物；無私人關係。"
locks: ["ART_PROJECT != PRIVATE_RELATION"]
```

## 鈴娘

```yaml
route_presence: "ACTIVE_ROUTE_LOCAL_ART_NODE"
evidence_event_ids: [E10]
relation_to_player: "戲曲／藝事計畫節點；無私人關係。"
locks: ["ART_PROJECT != PRIVATE_RELATION"]
```

## 青雀

```yaml
route_presence: "ACTIVE_ROUTE_LOCAL_MATCHMAKING_CHARACTER"
evidence_event_ids: [E13]
relation_to_player: "菊月初一一炷香輪轉相親中形成短時親近與條件式再見前約；沒有正式配對或固定關係。"
current_route_state:
  - "以青雀為花名／稱呼。"
  - "與花滿樓在局內採暫時情郎／女人的遊戲框架，互不強問真姓名家世。"
  - "向花滿樓摘過面具；有牽手與接吻。"
  - "收下《蝶戀花·青雀離》。"
  - "沒有作當場正式配對退場。"
  - "菊月初八前約：花滿樓先開好觀止包廂等她；她若仍想見可自行赴約；若來才再談是否繼續。"
knowledge_boundaries:
  - "摘面具只讓花滿樓取得當場可見身份，不建立公共真名／家門公開。"
unresolved:
  - "真名、家門、初八是否赴約、赴約後結果。"
locks:
  - "MASK_REMOVAL != PUBLIC_IDENTITY"
  - "KISS != FUTURE_ACCESS"
  - "CHU8_INVITE != ARRIVAL"
```

## 玄燕

```yaml
route_presence: "ACTIVE_ROUTE_LOCAL_MATCHMAKING_CHARACTER"
evidence_event_ids: [E13]
relation_to_player: "一炷香相親短場；無正式配對或固定後約。"
current_route_state:
  - "談無聊、陪伴與花和尚／青樓不空不成佛等話題；曾摘面具。"
locks: ["ONE_ROUND != RELATION"]
```

## 白鹿

```yaml
route_presence: "ACTIVE_ROUTE_LOCAL_MATCHMAKING_CHARACTER"
evidence_event_ids: [E13]
relation_to_player: "一炷香相親短場；無固定配對結果。"
current_route_state:
  - "有悖論／問答遊戲、摘面具與白棋物件相關舊記錄。"
  - "舊對話曾有結果作廢／不計修正，因此不固定勝負或配對。"
locks:
  - "VOIDED_RESULT_NOT_CANON"
  - "GAME_RESULT != RELATION"
```

## 紅綃

```yaml
route_presence: "ACTIVE_ROUTE_LOCAL_MATCHMAKING_CHARACTER"
evidence_event_ids: [E13]
relation_to_player: "一炷香相親短場；無正式配對、下次約定或成人事件。"
current_route_state:
  - "花滿樓為她當夜最後一輪男人之一；她曾摘面具。"
  - "收下花滿樓贈詞／話語後以『這第四世，我輸得心甘情願』收束。"
locks:
  - "DRAMATIC_LINE != RELATION"
  - "MASK_REMOVAL != PUBLIC_IDENTITY"
```

## 沈如晦

```yaml
route_presence: "ACTIVE_ROUTE_LOCAL_ADULT_CHARACTER"
evidence_event_ids: [E13, E14, E15]
relation_to_player: "共享一次具體完成的成人親密經歷；未建立戀愛、婚姻、排他、固定性伴侶或下一次成人約定。"
current_route_state:
  - "最初以『故人』入口／花名相遇，後自報真名沈如晦。"
  - "菊月初一夜與花滿樓進入觀止私人房。"
  - "完成一次雙方同意的肛交；沒有陰道插入。"
  - "事件後休息、整理並同睡；初二清晨自行離房，沒有叫醒花滿樓。"
privacy_or_knowledge_boundaries:
  - "成人事件直接知情者只有花滿樓與沈如晦；他人不得因同樓自動知道。"
unresolved:
  - "未來是否再見、是否再發生成人行為、關係如何演變。"
locks:
  - "PAST_ADULT_EVENT != LOVE"
  - "PAST_ADULT_EVENT != FUTURE_CONSENT"
  - "SLEEPING_TOGETHER != RELATION_UPGRADE"
```

## 未知傳話女子

```yaml
route_presence: "ACTIVE_ROUTE_LOCAL_INTERMEDIARY"
evidence_event_ids: [E16]
relation_to_player: "替匿名女客傳話／送帖的中介；無私人關係。"
identity: "UNKNOWN"
locks: ["MESSENGER_ROLE != PRINCIPAL_CLIENT"]
```

## 薄櫻

```yaml
route_presence: "ACTIVE_ROUTE_LOCAL_CLIENT"
evidence_event_ids: [E17, E18]
route_name: "薄櫻"
true_name_at_E18: "UNKNOWN"
adult: true
relation_to_player: "寫詞委託＋財產控制談判委託；無戀愛、成人或排他關係。"
current_route_state:
  - "接受花滿樓臨時稱呼『薄櫻』，當時不願透露真名。"
  - "接受《青玉案·薄櫻》；另獲免費《蝶戀花·薄櫻》。"
  - "寫詞同時也是她測試花滿樓的一部分。"
  - "真正主要請託：請花滿樓陪她見邵承祿，作獨立第三方／旁聽與談判支援。"
  - "她希望事情能成，但不接受不惜一切代價。"
  - "茶壺暗號：她親手把壺嘴轉向花滿樓＝不再希望把事情往談成方向推；截至 E18 未觸發。"
knowledge_boundaries:
  - "HOT V1.6 後揭露的真名不得倒灌為 E18 花滿樓已知。"
unresolved:
  - "真名與家門、財產法律狀態、是否改變談判意願、是否使用暗號。"
locks:
  - "ROUTE_NAME != TRUE_NAME"
  - "COMMISSION != ROMANCE"
  - "LATER_TRUE_NAME != EARLIER_KNOWLEDGE"
```

## 邵承祿

```yaml
route_presence: "ACTIVE_ROUTE_LOCAL_COUNTERPARTY"
evidence_event_ids: [E18]
relation_to_player: "薄櫻財產管理爭議之談判相對方；與花滿樓無私人關係。"
current_route_state:
  - "約五十歲形象；曾替薄櫻母親管理財產，受託法律形式未完全固定。"
  - "帶厚木匣到場，另由小夥計捧帳冊；截至 E18 木匣與帳冊尚未驗證。"
  - "先質疑家裡的帳讓外人聽；談判剛開始。"
unresolved:
  - "法律受託權、帳冊真偽完整性、契據狀態、侵占／挪用／善意保管、談判結果。"
locks:
  - "BAOYING_ALLEGATION != OBJECTIVE_GUILT"
  - "BOX_PRESENT != CONTENT_PROVEN"
  - "LEDGER_PRESENT != LEDGER_TRUE"
```

## 捧帳冊小夥計

```yaml
route_presence: "ACTIVE_ROUTE_LOCAL_WITNESS_ASSISTANT"
evidence_event_ids: [E18]
relation_to_player: "邵承祿帶來之工作助手；無私人關係。"
knowledge_boundary:
  - "只可在其實際工作／見聞範圍內知情，不得自動知道邵承祿全部內情。"
```

---

# 5｜LCAPG 67 人對齊清冊｜E18

```yaml
LCAPG_67_ALIGNMENT_AT_E18:
  - {order: 1, name: "潘金蓮", state: ACTIVE_ROUTE_CHARACTER_AT_E18}
  - {order: 2, name: "李瓶兒", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 3, name: "龐春梅", state: ACTIVE_ROUTE_CHARACTER_AT_E18}
  - {order: 4, name: "蘇清", state: ACTIVE_ROUTE_CHARACTER_AT_E18}
  - {order: 5, name: "阿麗婭", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 6, name: "張麗華", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 7, name: "宋蕙蓮", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 8, name: "李桂姐", state: ACTIVE_ROUTE_CHARACTER_AT_E18}
  - {order: 9, name: "紅袖", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 10, name: "疏影", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 11, name: "醉花", state: ACTIVE_ROUTE_CHARACTER_AT_E18}
  - {order: 12, name: "十三娘", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 13, name: "白三娘", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 14, name: "浮香", state: ACTIVE_ROUTE_CHARACTER_AT_E18}
  - {order: 15, name: "小翠", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 16, name: "李媽媽", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 17, name: "安舟", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 18, name: "汪鹽商", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 19, name: "辭歲", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 20, name: "貂蟬", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 21, name: "紅娘氏", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 22, name: "李師師", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 23, name: "青禾", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 24, name: "六條御息所", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 25, name: "李清照", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 26, name: "趙受益／趙禎／宋仁宗", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 27, name: "錦棠／周玉娘", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 28, name: "顧青簡", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 29, name: "楊玉環", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 30, name: "柳如是", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 31, name: "薛濤", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 32, name: "魚玄機", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 33, name: "失仙", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 34, name: "失美", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 35, name: "失蘿", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 36, name: "錯位", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 37, name: "香雲", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 38, name: "花晨", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 39, name: "艷芳", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 40, name: "玉香", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 41, name: "瑞珠", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 42, name: "瑞玉", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 43, name: "顧仙娘", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 44, name: "王婆", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 45, name: "林太太", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 46, name: "王六兒", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 47, name: "吳銀兒", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 48, name: "薛嫂", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 49, name: "吳月娘", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 50, name: "孟玉樓", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 51, name: "孫雪娥", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 52, name: "李嬌兒", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 53, name: "鄭愛月", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 54, name: "白玉潔", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 55, name: "張明姝", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 56, name: "孫清倩", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 57, name: "沈玉晶", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 58, name: "高承義", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 59, name: "李明遠", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 60, name: "王慎行", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 61, name: "王廷衡", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 62, name: "舍方知", state: BASE_EXISTS_RESOURCE_MENTION_ONLY_NOT_ROUTE_ENTRY_AT_E18}
  - {order: 63, name: "關盼盼", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 64, name: "夏蓮／趙姬", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 65, name: "玉堂春／蘇三", state: BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18}
  - {order: 66, name: "照夜／三聖母", state: ACTIVE_ROUTE_CHARACTER_AT_E18}
  - {order: 67, name: "紫蘭", state: ACTIVE_ROUTE_CHARACTER_AT_E18}
```

> `ACTIVE_ROUTE_CHARACTER_AT_E18` 只表示已有花滿樓線可核對事件；不等於與玩家有私人關係。  
> `BASE_ONLY_NO_ROUTE_ENTRY_EVIDENCE_AT_E18` 表示人物在 LCAPG 世界基線存在，但截至 E18 沒有足以建立本玩家線出場／交接／關係的 MASTER 證據。  
> 舍方知只在 E16 被當作裁縫資源提及，故維持 **NOT ROUTE ENTRY**。

---

# 6｜關係／知情／契約交叉鎖

```yaml
CROSS_AXIS_LOCKS:
  relation:
    - "ADULT_EVENT != LOVE"
    - "KISS != RELATION"
    - "MASK_REMOVAL != PUBLIC_IDENTITY"
    - "ONE_ROUND_MATCHMAKING != FORMAL_PAIRING"
  consent:
    - "PAST_CONSENT != FUTURE_CONSENT"
    - "CONTRACT != BODY_ACCESS"
    - "PAYMENT != CONSENT"
  knowledge:
    - "EVENT_PARTICIPATION != FULL_KNOWLEDGE"
    - "LATER_REVEAL != EARLIER_KNOWLEDGE"
    - "SELF_REPORT != OBJECTIVE_PROOF"
  status:
    - "LCAPG_BASE != ROUTE_ENTRY"
    - "MYTHIC_IDENTITY != HUMAN_REGISTRATION"
    - "ROUTE_NAME != TRUE_NAME"
  future:
    - "INVITE != ACCEPTANCE != ARRIVAL"
    - "PLAN != COMPLETION"
    - "PENDING stays PENDING until event/evidence"
```

---

# 7｜E18 Normal Resume 人物層

```text
MASTER V1.5-HARD
+
本 RCL V1.5 / schema V1.1-compatible
↓
HOT V1.6
↓
HOT V1.7
↓
HOT V1.8
↓
HOT V1.9
↓
CURRENT LIVE STATE
```

截止 E18 的直接人物狀態：

- 花滿樓、薄櫻、邵承祿、捧帳冊小夥計在香料鋪後堂。
- 薄櫻壺嘴朝外，暗號未觸發。
- 木匣與帳冊未驗。
- 花滿樓下一個重大言語／行動仍由玩家決定。
- HOT V1.6–V1.9 的鬼宅、浮香成人史、四僕、姚安娘、現金 292 兩等均不屬本代 cutoff。

---

# 8｜編譯驗證

```yaml
COMPILE_STATS:
  memory_generation: "V1.5"
  master_event_range: "E01-E18"
  aligned_character_base_count: 67
  active_lcapg_route_characters_at_cutoff: 8
  route_local_records_compiled: true
  first_rcl_generation: true
  post_master_hot_overlays:
    - "V1.6"
    - "V1.7"
    - "V1.8"
    - "V1.9"

VALIDATION:
  master_rcl_generation_match: "PASS / V1.5"
  master_sha_match_recorded: true
  rcl_schema: "PASS / GUANZHI_RCL_SCHEMA_V1_1_COMPATIBLE"
  lcapg_alignment_count: "PASS / 67"
  event_reference_upper_bound: "PASS / E18"
  no_hot_v1_6_plus_forward_contamination: true
  later_true_name_baoying_not_backfilled: true
  ghost_luheng_not_backfilled: true
  servants_not_backfilled: true
  current_cash_292_not_backfilled: true
  fuxiang_v1_8_adult_event_not_backfilled: true
  route_local_aheng_not_merged_with_later_ghost: true
  relation_auto_promoted_from_adult_event: false
  payment_auto_promoted_to_consent: false
  invite_auto_promoted_to_arrival: false
  master_rcl_atomic_pair: "PASS"
```

---

# RCL 責任聲明

本檔依玩家本輪對第一次 MASTER SAVE 的明示授權，作為 **MASTER V1.5-HARD 的同代人物履歷配對檔**。

它只表示：

- 已把 E01–E18 中有證據的人物位置、關係、知情、契約與未決狀態編譯為 RCL；
- LCAPG 67 人完成路線對齊，但「人物基線存在」不等於「本線已出場」；
- HOT V1.6–V1.9 仍是較新 overlay，不倒灌本代；
- 正常重載以 MASTER V1.5-HARD + 本 RCL V1.5 為基底，再依序疊加 V1.6–V1.9。

它不表示 Host SAVE commit、Project installation、E6/E7、正式 CERI Provider execution、正式 Main／Lighter receipt 或獨立多模型 Agent execution已發生。
