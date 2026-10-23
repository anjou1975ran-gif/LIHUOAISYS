# 觀止青樓（新）｜班富蘭線 HOT SAVE V1.01
## RELATION-FIRST｜理火三年・吉月初六夜｜第一份正式接關版

> **CURRENT ROUTE HOT SAVE / HUMAN PRE-AUTHORIZED / RELATION-FIRST TEST INSTANCE**
>
> 本版依 `GUANZHI SAVE RELATION-FIRST EXTERNAL OVERLAY V0.3-FULL-EXP` 編譯。
> 外掛只改變第一讀取面與關係顯影優先序，不取得 Canon owner、不取代原始事件證據、不改 SAVE owner。
> 本檔的 HOT 世界事實仍以合格事件／玩家明示／已成立 NPC 行動為來源；Relation Center 是由這些來源編譯出的第一讀取面。
>
> 人類 AnjouRan 已於產生本版前明示：「我直接提前批准許可」，故本版不再等待第二次批准。
> 本次成立的是 **專案內文件級 HOT SAVE commit**；不宣稱 Host deployment、Formal Host execution 或獨立 Runtime SAVE instrumentation 已成立。

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BANFULAN_HOT_V1_01_RELATION_FIRST_JI06_NIGHT"
  route_id: "GUANZHI_BANFULAN_ROUTE"
  route_name: "班富蘭線"
  player_public_identity: "班傑明／字富蘭／號克林居士"
  version: "V1.01"
  record_type: "HOT_SAVE"
  record_state: "VALID / CURRENT / HUMAN_PREAUTHORIZED_COMMIT"
  story_date: "理火三年・吉月初六"
  time_of_day: "夜；酉初之後，精確刻數 UNKNOWN"
  current_location: "觀止青樓／大堂"
  previous_valid_hot: "NONE / ROUTE GENESIS"
  master_reference: "NONE_YET"
  route_index_rcl_reference: "NONE_YET"
  relation_first_overlay: "V0.3-FULL-EXP"
  relation_first_view_status: "DERIVED_FIRST_READ_VIEW / NOT_INDEPENDENT_SOURCE_OF_TRUTH"
  supersedes_noncommitted_candidate:
    file: "觀止青樓_班富蘭線_HOT_SAVE_V1.01_吉月初六夜_美元箱_詩詞代作_蘇清測試_接關版.md"
    prior_state: "TEST_CANDIDATE / NEVER_FORMALLY_COMMITTED"
    effect: "SUPERSEDED_AS_DRAFT; NO VERSION BUMP REQUIRED"
  evidence_origin: "SAME_CONTEXT_REFERENCE + HUMAN_EXPLICIT_DIRECTION"
  formal_host_save_execution: "NOT_ESTABLISHED"
  created_real_date: "2026-10-07"
  timezone: "Asia/Taipei"
```

---

# 1｜RELATIONAL CENTER｜第一讀取面

> 下一位導演先回答：**現在大家彼此站在哪裡？**
> 事件只保留足以支撐這些位置的最低證據。

## R01｜班富蘭 ↔ 觀止

```yaml
RELATIONAL_POSITION:
  relation_ref: "REL-BF-GUANZHI-001"
  parties:
    - entity_ref: "班富蘭"
      entity_class: "PERSON"
    - entity_ref: "觀止青樓"
      entity_class: "INSTITUTION"

  current_position:
    labels:
      - "TEMPORARY_GUEST"
      - "VENUE_BASED_CREATOR"
      - "MUTUAL_EXCHANGE_WITHOUT_MEMBERSHIP"
    natural_language_definition: >-
      班富蘭以一名沒有本地貨幣、帶著異常美元箱的外來者進入觀止；
      觀止已接受三夜住宿、每日兩碗麵與代作詩詞營業安排，
      班富蘭因此第一次取得本世界的生存基地與市場入口。
      這是短期交換關係，不是歸屬、僱傭或永久收留。

  directionality:
    party_a_toward_b:
      current_view:
        - "觀止是目前可落腳、可吃飯、可接客源的第一個本地據點"
      powers: []
      dependencies:
        - "三夜住宿"
        - "每日兩碗麵"
        - "場地與本地客源"
      obligations:
        - "在目前三日詩詞營業安排範圍內，觀止抽成三成"
      debts: []
      permissions:
        - "可在觀止以班傑明／富蘭／克林居士名義掛牌代作"
      boundaries:
        - "沒有成立觀止成員／僱員身份"
        - "沒有把整箱美元交給觀止"
      active_offers: []
      effective_refusals: []

    party_b_toward_a:
      current_view:
        - "已接受班富蘭作為短期住客與可在場內創造收入的代作者"
      powers:
        - "提供／安排住宿與場地"
        - "在既定三日營業安排內收取三成抽成"
      dependencies: []
      obligations:
        - "三夜住宿"
        - "每日兩碗麵"
        - "協助掛牌／提供場地"
      debts: []
      permissions:
        - "可依三日安排從班富蘭場內詩詞／歌曲生意抽成"
      boundaries:
        - "沒有取得玩家整箱美元所有權"
        - "沒有固定美元兌銀權"
        - "沒有永久支配班富蘭創作或人身的資格"
      active_offers: []
      effective_refusals: []

  what_changed:
    qualified_changes:
      - "班富蘭從門外無本地貨幣的陌生人，變成觀止正式接納的三日住客與短期場內創作者。"
      - "觀止從單純拒絕美元直接流通，轉為接受『美元奇物＋創作營業』所形成的交換安排。"

  knowledge_asymmetry:
    mutual_knows:
      - "班富蘭持有大量本地無現成兌換價的美元。"
      - "班富蘭能靠詩詞／歌曲在觀止取得本地銀兩。"
    a_knows_b_does_not: []
    b_knows_a_does_not:
      - "觀止內不同人物對班富蘭的後世異常知識程度不一；不得把蘇清的知情自動視為整個觀止全知。"
    mutually_hidden_or_unknown:
      - "三日後是否續留"
      - "美元是否會形成任何固定本地價格"

  unresolved:
    axes:
      - "三日期滿後雙方是否續約／轉為其他關係"
      - "一張百元鈔在三夜安排中的實際保管與最終交付位置"

  still_not:
    explicit_non_promotions:
      - "PERMANENT_RESIDENCY"
      - "EMPLOYMENT"
      - "MEMBERSHIP"
      - "GUANZHI_OWNERSHIP_OF_USD_BOX"
      - "FIXED_USD_EXCHANGE_RATE"

  evidence:
    event_refs: ["BF-E02", "BF-E05"]
    contract_refs: ["BF-C01"]
    ledger_refs: ["BF-L01"]
    knowledge_refs: ["BF-K01"]
    relation_delta_refs: ["BF-RD01"]

  standing:
    relation_state: "HARD_ESTABLISHED"
    evidence_quality: "CURRENT_HOT_BACKED"
```

## R02｜班富蘭 ↔ 蘇清

```yaml
RELATIONAL_POSITION:
  relation_ref: "REL-BF-SUQING-001"
  parties:
    - entity_ref: "班富蘭"
      entity_class: "PERSON"
    - entity_ref: "蘇清"
      entity_class: "PERSON"

  current_position:
    labels:
      - "PROVISIONAL_COLLABORATION"
      - "MUTUAL_OUT_OF_ERA_ANOMALY_RECOGNITION"
      - "ACTIVE_MEMORY_TESTING"
    natural_language_definition: >-
      蘇清是目前第一個能直接理解班富蘭 USD、後世語彙與部分後世文化碎片的人；
      班富蘭也已看出蘇清擁有不屬本朝的一組知識。
      兩人已完成一次實際歌曲合作與分成，蘇清並開始主動測試班富蘭的記憶觸發方式。
      他們已形成可工作的特殊默契，但尚未形成完整互信、長期合夥或身世互揭。

  directionality:
    party_a_toward_b:
      current_view:
        - "把蘇清視為能聽懂部分後世東西、能把歌唱出來的稀有本地合作對象"
      powers: []
      dependencies:
        - "需要有人理解／轉譯部分後世歌曲與文化碎片時，蘇清具有目前場內獨特能力"
      obligations:
        - "《One Night in 汴京》合作中，班富蘭明示若蘇清唱則分她五兩"
      debts: []
      permissions:
        - "已允許蘇清參與該次歌曲演唱／轉譯"
      boundaries:
        - "沒有把全部作品或記憶交給蘇清管理"
        - "沒有對蘇清完整揭露自己也不知道的來源人生"
      active_offers: []
      effective_refusals: []

    party_b_toward_a:
      current_view:
        - "已把班富蘭視為值得實際測試其後世記憶機制的異常對象"
      powers: []
      dependencies: []
      obligations:
        - "已完成一次歌曲合作；其後是否再唱需依新場景與新條件成立"
      debts: []
      permissions:
        - "可提出題目測試；不能因此替班富蘭決定他必須繼續作答"
      boundaries:
        - "沒有取得班富蘭作品總代理權"
        - "沒有取得班富蘭身世解釋權"
      active_offers: []
      effective_refusals: []

  what_changed:
    qualified_changes:
      - "從初識陌生人轉為已完成一次付費合作的特殊知識同場者。"
      - "蘇清由單純辨識 USD 進一步主動測試班富蘭的記憶觸發。"
      - "班富蘭願意把實際收入的一部分分給蘇清換取演唱／轉譯能力。"

  knowledge_asymmetry:
    mutual_knows:
      - "對方都具有明顯超出普通仁宗朝知識邊界的資訊碎片。"
      - "班富蘭對自己過去大量失憶，但能被題目觸發詩詞／歌曲。"
    a_knows_b_does_not:
      - "班富蘭不知道蘇清完整穿越前史與西門府既有經歷。"
    b_knows_a_does_not:
      - "蘇清知道蘇軾住在觀止附近；班富蘭尚未取得此知情。"
      - "蘇清對部分後世作品／文化的來源辨識能力高於班富蘭目前自述記憶。"
    mutually_hidden_or_unknown:
      - "班富蘭真正本名、年代、原職業"
      - "雙方未來是否會形成長期合作"

  unresolved:
    axes:
      - "蘇清是否繼續測試班富蘭"
      - "雙方是否會進一步交換各自來源資訊"
      - "歌曲合作是否成為持續商業模式"

  still_not:
    explicit_non_promotions:
      - "MUTUAL_TRUST"
      - "FULL_DISCLOSURE"
      - "LONG_TERM_PARTNERSHIP"
      - "ROMANTIC_RELATION"
      - "EXCLUSIVE_BUSINESS_RELATION"

  evidence:
    event_refs: ["BF-E03", "BF-E05", "BF-E06"]
    contract_refs: []
    ledger_refs: ["BF-L02"]
    knowledge_refs: ["BF-K02"]
    relation_delta_refs: ["BF-RD02"]

  standing:
    relation_state: "HARD_ESTABLISHED"
    evidence_quality: "CURRENT_HOT_BACKED"
```

## R03｜班富蘭 ↔ 潘金蓮

```yaml
RELATIONAL_POSITION:
  relation_ref: "REL-BF-PAN-001"
  parties:
    - entity_ref: "班富蘭"
      entity_class: "PERSON"
    - entity_ref: "潘金蓮"
      entity_class: "PERSON"

  current_position:
    labels:
      - "HOST_MERCHANT_NEGOTIATION"
      - "VENUE_COMMISSION"
      - "MUTUAL_USEFULNESS_WITHOUT_PRIVATE_TRUST"
    natural_language_definition: >-
      潘金蓮已從面對一個沒有本地錢的怪客，轉為把班富蘭當成能在觀止創造收入的人；
      班富蘭則接受潘金蓮作為目前掌握住宿、場地、定價與抽成條件的本地權力節點。
      兩人已能談價格、抽成與資源交換，但仍是商業位置，不是私人信任。

  directionality:
    party_a_toward_b:
      current_view:
        - "潘金蓮是目前決定觀止場地、住宿與抽成條件的主要談判者"
      powers: []
      dependencies:
        - "住宿／場地／本地營業入口"
      obligations:
        - "依三日安排讓觀止取得約定抽成"
      debts: []
      permissions: []
      boundaries:
        - "班富蘭仍保有自己作品、美元與後續交易的決定權，除已成立範圍外不得自動擴張"
      active_offers: []
      effective_refusals: []

    party_b_toward_a:
      current_view:
        - "已承認班富蘭能把奇怪內容轉成真銀兩"
      powers:
        - "三日場內安排與抽成條件"
      dependencies: []
      obligations:
        - "履行已談定的短期住宿／餐食／場地安排"
      debts: []
      permissions: []
      boundaries:
        - "三成抽成不等於取得班富蘭全部未來作品"
        - "美元未被她自行定價成銀兩"
      active_offers: []
      effective_refusals: []

  what_changed:
    qualified_changes:
      - "潘金蓮已由『先判斷這怪錢有沒有用』進入『這個人能不能替觀止創造收入』的實際交易位置。"
      - "班富蘭已由求一頓飯的外來者，成為能與潘金蓮直接談抽成與價格的人。"

  knowledge_asymmetry:
    mutual_knows:
      - "美元目前沒有本地公認兌換價。"
      - "班富蘭的詩詞／歌曲已能賺到本地銀兩。"
    a_knows_b_does_not: []
    b_knows_a_does_not: []
    mutually_hidden_or_unknown:
      - "班富蘭完整來源"
      - "美元未來是否能被本地市場接受"

  unresolved:
    axes:
      - "三日之後雙方是否續談更長營業安排"
      - "後續作品的價格與抽成是否沿用目前條件"

  still_not:
    explicit_non_promotions:
      - "PRIVATE_TRUST"
      - "EMPLOYMENT"
      - "OWNERSHIP_OF_PLAYER_WORK"
      - "PERMANENT_MANAGEMENT_RIGHT"

  evidence:
    event_refs: ["BF-E02", "BF-E05"]
    contract_refs: ["BF-C01"]
    ledger_refs: ["BF-L01", "BF-L02"]
    knowledge_refs: ["BF-K01"]
    relation_delta_refs: ["BF-RD03"]

  standing:
    relation_state: "HARD_ESTABLISHED"
    evidence_quality: "CURRENT_HOT_BACKED"
```

## R04｜班富蘭 ↔ 疏影

```yaml
RELATIONAL_POSITION:
  relation_ref: "REL-BF-SHUYING-001"
  parties:
    - entity_ref: "班富蘭"
      entity_class: "PERSON"
    - entity_ref: "疏影"
      entity_class: "PERSON"

  current_position:
    labels:
      - "MATERIAL_CURIOSITY"
      - "PROPERTY_BOUNDARY_ESTABLISHED"
    natural_language_definition: >-
      疏影對班富蘭的百元鈔產生專業材料／線條興趣，並已參與一次水洗觀察；
      但玩家財物的處置邊界已顯影：研究興趣不等於取得、留存、焚燒或作畫權。
      目前兩人之間最重要的不是親疏，而是『好奇可以存在，物權界線也有效』。

  directionality:
    party_a_toward_b:
      current_view:
        - "知道疏影對鈔票材質與印刷有專業興趣"
      powers:
        - "保有百元鈔的處分與授權權"
      dependencies: []
      obligations: []
      debts: []
      permissions:
        - "已允許當場水洗／觀察這一輪已完成行為"
      boundaries:
        - "未授權焚燒"
        - "未授權長期持有"
        - "未授權拿去作畫／複製作為新處置"
      active_offers: []
      effective_refusals:
        - "焚燒需另行取得玩家明示，現況不得視為已有許可"

    party_b_toward_a:
      current_view:
        - "已把班富蘭的鈔票視為值得以畫工／材料眼光研究的異物"
      powers: []
      dependencies:
        - "任何進一步持有／處置都依賴玩家新授權"
      obligations:
        - "不得把一次觀察擴張成永久取得"
      debts: []
      permissions:
        - "只有已完成的當場觀察／水洗範圍"
      boundaries:
        - "無焚燒權"
        - "無當然留存權"
      active_offers: []
      effective_refusals: []

  what_changed:
    qualified_changes:
      - "第一次互動即建立了可觀察研究興趣與玩家物權界線。"

  knowledge_asymmetry:
    mutual_knows:
      - "這張鈔票材質／印刷與本地普通紙張不同。"
    a_knows_b_does_not:
      - "班富蘭知道它是 USD；疏影不因此自動知道其金融制度與價值。"
    b_knows_a_does_not: []
    mutually_hidden_or_unknown:
      - "疏影未來是否還會提出進一步研究要求"

  unresolved:
    axes:
      - "疏影是否提出正式作畫／持有請求"
      - "玩家是否授權任何新用途"

  still_not:
    explicit_non_promotions:
      - "TRUST"
      - "LONG_TERM_RESEARCH_PARTNERSHIP"
      - "PERMISSION_TO_BURN"
      - "PERMISSION_TO_KEEP_OR_PAINT"

  evidence:
    event_refs: ["BF-E04"]
    contract_refs: []
    ledger_refs: []
    knowledge_refs: ["BF-K03"]
    relation_delta_refs: ["BF-RD04"]

  standing:
    relation_state: "PARTIAL_ESTABLISHED"
    evidence_quality: "CURRENT_HOT_BACKED"
```

## R05｜潘金蓮 ↔ 錦棠／周玉娘

```yaml
RELATIONAL_POSITION:
  relation_ref: "REL-PAN-JINTANG-001"
  parties:
    - entity_ref: "潘金蓮"
      entity_class: "PERSON"
    - entity_ref: "錦棠／周玉娘"
      entity_class: "PERSON"

  current_position:
    labels:
      - "NEGOTIATED_ACQUISITION_RELATION"
      - "ASYMMETRIC_POWER"
      - "EMERGING_PERSONAL_BARGAINING_SPACE"
    natural_language_definition: >-
      潘金蓮作為觀止掌櫃正在取得周玉娘的契籍／人身交易位置，權力明顯不對稱；
      但周玉娘已在這個不對稱關係裡第一次成功把『自己的增值』提出來談，
      潘金蓮並接受以額外二百兩歸她本人作為談判結果方向。
      因付款、文契換主與官冊登記尚未完整演出，不能把談定直接寫成所有程序均完成。

  directionality:
    party_a_toward_b:
      current_view:
        - "認為周玉娘／錦棠不只具有身體條件，也具有判斷、學習與往上走的商業價值"
      powers:
        - "代表觀止談收購與後續場內位置"
      dependencies: []
      obligations:
        - "若額外二百兩條件進入履行，該部分應歸錦棠本人而非姚二娘"
      debts: []
      permissions: []
      boundaries:
        - "收購／妓籍不等於永久或全面身體同意"
        - "尚未有證據證明所有交易程序均完成"
      active_offers:
        - "額外二百兩歸錦棠本人之條件"
      effective_refusals: []

    party_b_toward_a:
      current_view:
        - "已把潘金蓮當成可以直接談自己價值與未來分成的人，而不再只透過姚二娘被動成交"
      powers:
        - "可對自己的增值條件提出談判與拒絕擴張"
      dependencies:
        - "目前能否進入觀止、取得新名字與後續營業位置仍高度依賴潘金蓮／觀止制度"
      obligations: []
      debts: []
      permissions: []
      boundaries:
        - "接受『錦棠』作新名方向不等於放棄『周玉娘』本名"
      active_offers: []
      effective_refusals:
        - "拒絕讓自己的全部增值都當然歸中介"

  what_changed:
    qualified_changes:
      - "周玉娘第一次在被交易的結構裡取得一小塊可自行議價的位置。"
      - "潘金蓮第一次直接承認她的腦子／判斷也是價值的一部分。"
      - "雙方關係由單純被買／買入，增加了可談條件的軸。"

  knowledge_asymmetry:
    mutual_knows:
      - "六百兩是潘金蓮與姚二娘談的收購基準。"
      - "二百兩是周玉娘自己爭取出的個人增值條件。"
    a_knows_b_does_not: []
    b_knows_a_does_not: []
    mutually_hidden_or_unknown:
      - "完整文契是否已換主"
      - "六百兩是否已全額交割"
      - "二百兩是否已實際到手"
      - "官冊是否已正式登記『錦棠』"

  unresolved:
    axes:
      - "交易履行程序"
      - "錦棠未來收入如何分配"
      - "她在觀止能實際取得多少自主空間"

  still_not:
    explicit_non_promotions:
      - "TRANSFER_FULLY_COMPLETED"
      - "PERSONAL_200_TAELS_PAID"
      - "OFFICIAL_REGISTER_COMPLETED"
      - "LONG_TERM_REVENUE_SHARE"
      - "BLANKET_SEXUAL_CONSENT"

  evidence:
    event_refs: ["BF-E01"]
    contract_refs: ["BF-C02"]
    ledger_refs: ["BF-L03"]
    knowledge_refs: []
    relation_delta_refs: ["BF-RD05"]

  standing:
    relation_state: "PARTIAL_ESTABLISHED"
    evidence_quality: "CURRENT_HOT_BACKED"
```

## R06｜錦棠／周玉娘 ↔ 姚二娘

```yaml
RELATIONAL_POSITION:
  relation_ref: "REL-JINTANG-YAO-001"
  parties:
    - entity_ref: "錦棠／周玉娘"
      entity_class: "PERSON"
    - entity_ref: "姚二娘"
      entity_class: "PERSON"

  current_position:
    labels:
      - "BROKER_DEPENDENCE"
      - "OPEN_VALUE_CONFLICT"
      - "TRANSFER_PENDING"
    natural_language_definition: >-
      姚二娘仍是把周玉娘帶到觀止、掌握原交易鏈與收購價談判的中介；
      但周玉娘已第一次公開挑戰『多賣出的價也全歸中介』的當然性，
      並成功把額外二百兩定位為自己的個人增值條件。
      兩人的中介依賴尚未消失，但中介對價值的單向代表權已出現明確裂口。

  directionality:
    party_a_toward_b:
      current_view:
        - "不再接受姚二娘當然代表自己的全部價值"
      powers:
        - "已對個人增值部分提出直接談判"
      dependencies:
        - "原文契／出售鏈仍與姚二娘有關"
      obligations: []
      debts: []
      permissions: []
      boundaries:
        - "額外二百兩不得因姚二娘是中介而自動歸她"
      active_offers: []
      effective_refusals:
        - "拒絕『所有增值皆歸中介』的默認位置"

    party_b_toward_a:
      current_view:
        - "仍作為交易中介帶周玉娘入觀止議價"
      powers:
        - "持有／代表原交易鏈的部分程序位置；精確文契控制細節未完全演出"
      dependencies:
        - "成交依賴潘金蓮／觀止付款與換契"
      obligations: []
      debts: []
      permissions: []
      boundaries:
        - "不能把潘金蓮另給錦棠的二百兩自動算成自己的成交款"
      active_offers: []
      effective_refusals: []

  what_changed:
    qualified_changes:
      - "周玉娘第一次從被中介代表的人，變成會直接切出自己價值份額的談判者。"

  knowledge_asymmetry:
    mutual_knows:
      - "六百兩是主交易基準，額外二百兩是另一條個人條件。"
    a_knows_b_does_not: []
    b_knows_a_does_not: []
    mutually_hidden_or_unknown:
      - "最終交割與文契換主是否完成"

  unresolved:
    axes:
      - "姚二娘退出交易鏈的確切時點"
      - "六百兩／文契完成狀態"

  still_not:
    explicit_non_promotions:
      - "BROKER_ROLE_TERMINATED"
      - "FULL_SETTLEMENT"
      - "RECONCILIATION"
      - "PERMANENT_HOSTILITY"

  evidence:
    event_refs: ["BF-E01"]
    contract_refs: ["BF-C02"]
    ledger_refs: ["BF-L03"]
    knowledge_refs: []
    relation_delta_refs: ["BF-RD06"]

  standing:
    relation_state: "PARTIAL_ESTABLISHED"
    evidence_quality: "CURRENT_HOT_BACKED"
```

## RELATIONAL CENTER 排除項｜防止主題相似偷升格

```yaml
RELATIONAL_CENTER_EXCLUSIONS:
  BANFULAN__JINTANG:
    classification: "RELATIONAL_SEED_ONLY / NOT_CENTERED_THIS_HOT"
    reason:
      - "兩人已同場並注意到彼此的『價值／定價』處境。"
      - "但目前沒有足夠雙邊選擇、義務、秘密交換、合作、拒絕或持續後果。"
      - "主題鏡像不得當成已成立關係。"
    may_not_promote_to:
      - "TRUST"
      - "ALLIANCE"
      - "SHARED_RESONANCE_AS_HARD_RELATION"
      - "ROMANCE"
```

---

# 2｜CURRENT SCENE / FREEZE POINT

```yaml
CURRENT_SCENE:
  date: "理火三年・吉月初六"
  time: "夜；酉初後延伸至晚間，精確刻數 UNKNOWN"
  location: "觀止青樓／大堂"
  active_people:
    - "班富蘭"
    - "潘金蓮"
    - "蘇清"
    - "錦棠"
  recently_relevant_people:
    - "疏影｜已完成一次百元鈔材質觀察／水洗，是否仍在大堂不固定"
    - "青衫客｜第一位付費買家，是否仍留場不固定"
    - "姚二娘｜錦棠交易中介，此刻是否仍在場未明示"

  player_last_explicit_position:
    - "先有錢就好"
    - "先活下來"
    - "之後再繼續賺錢／玩家戲稱『騙錢』"

  freeze_point:
    - "班富蘭仍在觀止大堂；沒有玩家明示已上樓、已睡著或已安置完成金屬箱。"
    - "三夜住宿安排已成立，但本輪尚未演到實際進房落鎖。"
    - "蘇清的記憶測試已跑過一輪撞詞事故；是否繼續測由蘇清下一次自主決定。"
    - "錦棠交易程序仍有未演完的交割軸，不因故事焦點轉向班富蘭而自動完成。"

  next_action_owner: "PLAYER_OR_WORLD_AFTER_RESUME"
```

---

# 3｜MATERIAL NONRELATIONAL STATE｜不能被關係優先吃掉的硬事實

```yaml
MATERIAL_NONRELATIONAL_STATE:
  money_and_ledger:
    player_local_silver:
      status: "POSITIVE_LOCAL_SILVER_OBTAINED / EXACT_TOTAL_UNRECONCILED"
      reason:
        - "《One Night in 汴京》先有首闕五兩成交。"
        - "後續又出現整首三十兩成交與 9／5／16 分配。"
        - "未明示三十兩是否包含先前五兩。"
        - "蘇清另有五兩私人測試付款。"
      forbidden_resolution:
        - "不得靜默選成 30 TOTAL 或 35 GROSS。"

    guanzhi_commission:
      scope: "目前三日觀止場內詩詞／歌曲營業安排"
      rate: "30%"
      status: "ESTABLISHED"

  objects_and_custody:
    metal_case:
      owner: "班富蘭"
      contents: "USD 1,000,000（玩家設定成立）"
      local_exchange_value: "UNKNOWN"
      current_location: "觀止大堂附近／隨玩家進場；尚未演到房內落鎖"
      security_state: "NOT_YET_SECURED_IN_ROOM"

    usd_100_note:
      owner: "班富蘭，除已成立交換範圍外不得推定移轉"
      wash_test: "COMPLETED"
      current_physical_custody: "UNKNOWN_AT_FREEZE"
      burn_permission: false
      paint_or_long_hold_permission: "NOT_GRANTED"

  contracts:
    BF-C01:
      title: "觀止三夜住宿＋每日兩碗麵＋三日代作營業"
      state: "ACTIVE / PARTIALLY_PERFORMED"
      consideration:
        - "班富蘭提出一張 USD 100 note 作交換標的"
        - "實體交付／保管位置未完全演出"
      venue_commission: "30%"
      exact_expiry_clock: "UNKNOWN"

    BF-C02:
      title: "周玉娘／錦棠收購談判"
      state: "NEGOTIATED / PERFORMANCE_NOT_FULLY_PLAYED"
      acquisition_price_to_broker_chain: "600 taels"
      personal_increment_for_jintang: "200 taels"
      transfer_completed: "UNKNOWN / NOT_FULLY_PLAYED"
      official_registration_completed: "NOT_ESTABLISHED"

  legal_status:
    banfulan:
      local_identity: "自稱班超後人；班傑明／字富蘭／號克林居士"
      genealogy_verified: false
      official_registration: "NOT_ESTABLISHED"

    jintang:
      birth_name: "周玉娘"
      chosen_register_name_direction: "錦棠"
      official_register_completion: "NOT_ESTABLISHED"

  deadlines:
    - "班富蘭三夜住宿／每日兩碗麵安排仍在有效期間；精確截止刻數未定。"

  world_hard_facts:
    - "本線採宋仁宗朝。"
    - "李白、白居易等前代作品可被本朝受教育者識別。"
    - "蘇清知道蘇軾住在觀止附近；蘇軾尚未與班富蘭正式相遇。"
    - "青衫客在場表示前一日於歐陽公處聽過《生查子》元夕一路；此為本 Route 已發生的角色證詞，不另升格成外部史實證明。"
```

---

# 4｜KNOWLEDGE / SECRET / AUTHORITY ASYMMETRY

```yaml
KNOWLEDGE_AND_SECRET_PRESSURE:
  - actor: "班富蘭"
    knows:
      - "自己持有一百萬美元"
      - "自己會被題目觸發詩詞／歌曲／旋律"
      - "蘇清能理解 USD、VENI VIDI VICI 等後世碎片"
    does_not_know:
      - "自己的真正本名、原職業、家庭與大部分後世歷史"
      - "蘇清完整穿越前史"
      - "蘇軾住在附近"

  - actor: "蘇清"
    knows:
      - "USD 是後世貨幣概念"
      - "班富蘭的記憶高度殘缺但可被題目觸發作品"
      - "蘇軾住在觀止附近"
    suspects:
      - "班富蘭很可能也是不屬本朝的人"
    does_not_know:
      - "班富蘭真正來源、原本姓名、完整記憶機制"

  - actor: "潘金蓮"
    knows:
      - "美元目前在汴京沒有現成兌換市場"
      - "班富蘭的詩詞／歌曲可以換到本地銀兩"
    does_not_know:
      - "現代金融制度與美元真實後世購買力"
      - "班富蘭完整來源"

  - actor: "疏影"
    knows:
      - "百元鈔材質與印刷痕跡異於本地普通紙張／畫作"
      - "水洗未立即毀壞"
    does_not_know:
      - "USD 完整金融制度與本地交換價值"

  - actor: "錦棠"
    knows:
      - "班富蘭帶有大量本地暫時花不出去的錢"
      - "班富蘭已用作品談出本地價格"
    does_not_know:
      - "現代世界與 USD 制度"
      - "班富蘭作品來源"
```

---

# 5｜MINIMAL RECENT EVENT EVIDENCE｜事件只保留到足以支撐關係

```yaml
MINIMAL_EVENT_EVIDENCE:
  BF-E01:
    title: "周玉娘被帶至觀止談收購並爭取個人增值"
    one_line_effect: "建立潘金蓮↔錦棠的議價關係，以及錦棠↔姚二娘的中介價值衝突。"
    qualified_facts:
      - "收購基準六百兩"
      - "額外二百兩定位為周玉娘本人增值條件"
      - "周玉娘接受『錦棠』作新名方向"
    unresolved:
      - "付款、換契、官冊完成狀態"

  BF-E02:
    title: "班富蘭帶美元箱抵達觀止並談成三日生存安排"
    one_line_effect: "建立班富蘭↔觀止、班富蘭↔潘金蓮的短期交換與場地營業位置。"

  BF-E03:
    title: "蘇清辨認 USD 與後世概念"
    one_line_effect: "班富蘭與蘇清第一次確認彼此都持有超出本朝的一組知識。"

  BF-E04:
    title: "疏影檢視並水洗百元鈔"
    one_line_effect: "建立疏影的材料研究興趣與班富蘭的財物處分界線。"

  BF-E05:
    title: "《One Night in 汴京》首單與蘇清演唱合作"
    one_line_effect: "班富蘭第一次以內容換到本地銀兩；蘇清完成一次付費合作；潘金蓮的三成場地抽成進入實際運作。"

  BF-E06:
    title: "蘇清以中秋／月／兄弟條件測試班富蘭記憶"
    one_line_effect: "蘇清由理解者轉為主動測試者；班富蘭的作品記憶被證明不是可靠作者／年代資料庫，並出現歐陽修撞詞風險。"

  BF-E07:
    title: "班富蘭明示當前生存優先"
    one_line_effect: "玩家目前把先取得本地可用資源、活下來放在追查身世之前；未因此授權任何 NPC 替他決定下一步。"
```

---

# 6｜OPEN THREADS / DUE ITEMS

```yaml
OPEN_THREADS:
  - thread_ref: "TH-BF-01"
    owner: "PLAYER + GUANZHI WORLD"
    state: "班富蘭尚未實際進房、安置並鎖好金屬箱。"

  - thread_ref: "TH-BF-02"
    owner: "ACCOUNTING / PAN JINLIAN / PLAYER"
    state: "首闕五兩與整首三十兩是否重複計價仍需對帳。"

  - thread_ref: "TH-BF-03"
    owner: "SUQING"
    state: "蘇清可自行決定是否繼續用蘇軾／仁宗朝文壇題目測試班富蘭；尚未預先決定。"

  - thread_ref: "TH-BF-04"
    owner: "WORLD / SU SHI"
    state: "蘇軾住附近的鉤仍開著；尚未發生正式相遇。"

  - thread_ref: "TH-BF-05"
    owner: "PLAYER"
    state: "疏影若想作畫、長期持有、焚燒或以其他方式處置百元鈔，需新授權。"

  - thread_ref: "TH-BF-06"
    owner: "PAN / JINTANG / YAO / WORLD PROCESS"
    state: "六百兩、二百兩、換契與官冊程序尚未完整演出。"

  - thread_ref: "TH-BF-07"
    owner: "WORLD / MARKET"
    state: "《One Night in 汴京》是否形成第二波客源／文壇反作用尚未成立。"
```

---

# 7｜FORBIDDEN PROMOTIONS｜下一位導演最容易犯的錯

```yaml
FORBIDDEN_PROMOTIONS:
  - "RELATION-FIRST != RELATION-FABRICATION"
  - "班富蘭↔蘇清一次合作 != MUTUAL_TRUST"
  - "蘇清主動測試 != 蘇清已知道班富蘭完整身世"
  - "班富蘭↔錦棠主題相似 != 已成立雙邊關係"
  - "三夜住宿 != 觀止成員／僱員／永久收留"
  - "潘金蓮三成抽成 != 潘金蓮取得班富蘭全部作品管理權"
  - "美元有一百萬面額總量 != 汴京已有兌換價"
  - "疏影研究過鈔票 != 她可以留存／畫／燒鈔票"
  - "潘金蓮與錦棠談定六百＋二百 != 付款、文契、官冊全部完成"
  - "錦棠接受新名方向 != 周玉娘本名消失"
  - "妓籍／收購談判 != BLANKET SEXUAL CONSENT"
  - "蘇軾住附近 != 蘇軾已知道班富蘭／已聽過歌曲／已準備登場"
  - "歐陽修撞詞事故 != 已形成正式抄襲指控"
  - "玩家說先活下來 != 玩家已上樓、睡著、交出美元或接受新交易"
```

---

# 8｜CONTINUATION PRESSURE｜不替角色決定，只說什麼仍在發力

```yaml
CONTINUATION_PRESSURE:
  - "班富蘭目前最直接的壓力是：把後世碎片轉成真正能在汴京使用的生存資源，同時保住美元箱與自己的決定權。"
  - "蘇清已從『唯一能聽懂的人』走到『主動測試的人』；只要她仍對班富蘭的來源有興趣，這條關係自然有下一步壓力，但下一步內容由蘇清自己決定。"
  - "潘金蓮與班富蘭的關係已進入可持續談價的位置；只要新生意發生，抽成、定價與場地利益會自然重新出現。"
  - "疏影對百元鈔的專業興趣仍未消失，但任何新處置都卡在玩家物權邊界。"
  - "錦棠與潘金蓮／姚二娘的交易關係尚未結清；即使玩家不介入，這條 NPC↔NPC 關係仍可在世界背景中自行推進，但不得跳過未演出的付款／換契程序。"
```

---

# 9｜LOOKUP REFS｜需要厚資料時才回查

```yaml
LOOKUP_REFS:
  overlay:
    file: "GUANZHI_SAVE_RELATION_FIRST_EXTERNAL_OVERLAY_V0.3_FULL_EXP_20261007.md"
    role: "RELATION-FIRST FIRST-READ PROJECTION PRINCIPLE"

  character_baseline:
    file: "觀止人物卡池_LCAPG_V3.3.20_CURRENT_RATIFIED_71人_辭歲肉身菩薩人格重錨_20261003.md"
    relevant:
      - "潘金蓮"
      - "蘇清"
      - "疏影"
      - "錦棠"

  current_world:
    file: "02_GUANZHI_WORLD_V2.2.2_CURRENT_V3.11_RUNTIME_POINTER_INTEGRATED_20261006.md"

  current_core:
    file: "01_GUANZHI_RUNTIME_CORE_V3.11_CURRENT_COMPANION_WORLD_V2.2.2_CORRECTED_20261006.md"

  current_main:
    file: "01_MAIN_V4.4_PROTOCOL_V3.0.1_LIGHTER_V4.8_RECEIPT_I9_FULL_RATIFIED_20261006.md"

  current_lighter:
    file: "02_LIGHTER_V4.8_PROTOCOL_V3.0.1_RECEIPT_I9_CURRICULUM_FULL_RATIFIED_20261006.md"

  master:
    status: "NONE_YET"

  route_index_rcl:
    status: "NONE_YET"
```

---

# 10｜DIRECT CONTINUATION POINT｜30 秒接關

```text
先讀關係，不先讀事件：

1. 班富蘭 ↔ 觀止：三夜短期收留＋場內創作營業；有交換，沒有歸屬。
2. 班富蘭 ↔ 蘇清：已合作、已彼此看出後世異常、蘇清開始測試；仍未互信、未完整揭底。
3. 班富蘭 ↔ 潘金蓮：已能談價與抽成；潘掌場地，班富蘭掌作品與美元；是商業位置，不是私交。
4. 班富蘭 ↔ 疏影：她對美元有專業興趣，但玩家物權界線有效；沒有燒、留、畫的預先授權。
5. 潘金蓮 ↔ 錦棠：強烈不對稱的收購談判中，錦棠第一次取得自己的議價位置；程序尚未全結。
6. 錦棠 ↔ 姚二娘：中介依賴仍在，但『誰有權拿走她的增值』已出現明確衝突。

當前仍在觀止大堂。
班富蘭最後明示：先有錢、先活下來，之後再繼續賺錢。
不要替他自動上樓、睡著、交出美元、答應疏影、續約或接新交易。

硬事實只記最低必要：
- 一百萬美元仍無汴京固定匯率。
- 玩家已有本地銀兩，但精確總額因首闕5兩／整首30兩對帳衝突而 UNKNOWN。
- 三夜住宿＋每日兩碗麵＋三日代作營業安排有效；觀止場內抽成三成。
- 蘇清知道蘇軾住附近；班富蘭不知道；蘇軾尚未與班富蘭相遇。
- 錦棠六百／二百與換契／官冊尚未完整演完。
```

---

# 11｜RELATION-FIRST 實跑追蹤

```yaml
RELATION_FIRST_TEST_TRACKING:
  overlay_version: "V0.3-FULL-EXP"
  test_instance: "BANFULAN_HOT_V1.01"
  role: "BASELINE / ROUND_1_INPUT"
  effective_rounds_target: "5-6"

  pre_scene_relational_center_count: 6
  npc_npc_relations_preserved:
    - "潘金蓮 ↔ 錦棠"
    - "錦棠 ↔ 姚二娘"
  person_institution_relation_preserved:
    - "班富蘭 ↔ 觀止"
  material_facts_retained: true
  unknown_preserved: true
  relation_seed_overpromotion_blocked: true
  evidence_traceability: "PASS_AT_BASELINE"

  continuation_quality:
    relation_readability: "BASELINE_READY"
    character_position_drift: "NOT_YET_TESTED_AFTER_REENTRY"
    material_recovery: "NOT_YET_TESTED_AFTER_REENTRY"

  verdict: "BASELINE_COMMITTED / EFFECTIVENESS_PENDING_NEXT_REENTRY"
```

---

# 12｜SAVE COMMIT / 法位邊界

```yaml
SAVE_COMMIT:
  human_authorization:
    type: "DIRECT_PREAUTHORIZATION_IN_CURRENT_CONVERSATION"
    status: "TRUE"
    effect: "THIS V1.01 MAY BE COMMITTED WITHOUT SECOND APPROVAL"

  document_result:
    status: "COMMITTED"
    route_current_hot: "V1.01"
    relation_first_projection_used: true

  source_boundary:
    relation_center: "DERIVED_FROM_QUALIFIED_CURRENT_HOT_EVIDENCE"
    overlay_is_source_of_truth: false
    original_event_evidence_replaced: false

  execution_boundary:
    document_level_save_commit: true
    host_instrumented_formal_save_execution: "NOT_ESTABLISHED"
    e6_e7: "NOT_ESTABLISHED"

  core_schema:
    changed: false
    save_owner_changed: false
    write_path_owner_changed: false
```

---

# 13｜根句

> **事件告訴我們發生了什麼。**
>
> **HOT 告訴下一幕最低需要知道什麼。**
>
> **而這一版先告訴導演：因此，現在這些人彼此站在哪裡。**

END OF CURRENT HOT SAVE V1.01
# 觀止青樓（新）｜班富蘭線 HOT SAVE V1.02
## RELATION-FIRST｜理火三年・吉月初六深夜｜疏影藝術資產線建立／第二輪接關版

> **CURRENT ROUTE HOT SAVE / HUMAN EXPLICIT SAVE REQUEST / RELATION-FIRST TEST INSTANCE**
>
> 本版承接 `觀止青樓_班富蘭線_HOT_SAVE_V1.01_RELATION_FIRST_吉月初六夜_CURRENT.md`。
> 依 `GUANZHI SAVE RELATION-FIRST EXTERNAL OVERLAY V0.3-FULL-EXP` 編譯第一讀取面。
>
> 本檔只保存已由玩家明示、已成立 NPC 自主行動、已演出的場景結果與仍未決的硬狀態。
> 商業模型中「已討論／已形成工作方案」與「已簽契／已拍賣／已交割」嚴格分離。
>
> 人類 AnjouRan 於本次對話明示：「今晚算是做完大事了，可以收工了。HOT SAVE」。
> 因此本版成立 **專案內文件級 HOT SAVE commit**。
> 不宣稱 Host deployment、Formal Host execution、E6／E7 或獨立 Runtime SAVE instrumentation 已成立。

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BANFULAN_HOT_V1_02_RELATION_FIRST_JI06_LATE_NIGHT_SHUYING_ART_MARKET"
  route_id: "GUANZHI_BANFULAN_ROUTE"
  route_name: "班富蘭線"
  player_public_identity: "班傑明／字富蘭／號克林居士"
  version: "V1.02"
  record_type: "HOT_SAVE"
  record_state: "VALID / CURRENT / HUMAN_EXPLICIT_SAVE_REQUEST"
  story_date: "理火三年・吉月初六"
  time_of_day: "深夜；精確刻數 UNKNOWN"
  current_location: "觀止青樓二樓／弄影軒門外一帶"
  scene_segment_status: "JI06_NIGHT_MAJOR_WORK_CLOSED"
  previous_valid_hot:
    version: "V1.01"
    file: "觀止青樓_班富蘭線_HOT_SAVE_V1.01_RELATION_FIRST_吉月初六夜_CURRENT.md"
    treatment: "PRESERVED / SUPERSEDED_AS_CURRENT_HOT_ONLY"
  master_reference: "NONE_YET"
  route_index_rcl_reference: "NONE_YET"
  relation_first_overlay: "V0.3-FULL-EXP"
  relation_first_view_status: "DERIVED_FIRST_READ_VIEW / NOT_INDEPENDENT_SOURCE_OF_TRUTH"
  evidence_origin:
    - "SAME_CONTEXT_REFERENCE"
    - "HUMAN_EXPLICIT_DIRECTION"
    - "NPC_AUTONOMOUS_ACTION_WITHIN_DIRECTOR_SCOPE"
  formal_host_save_execution: "NOT_ESTABLISHED"
  created_real_date: "2026-10-07"
  timezone: "Asia/Taipei"
```

---

# 1｜RELATIONAL CENTER｜第一讀取面

## R01｜班富蘭 ↔ 疏影

```yaml
RELATIONAL_POSITION:
  relation_ref: "REL-BF-SHUYING-001"
  standing: "HARD_ESTABLISHED / MATERIAL_DELTA_THIS_HOT"

  current_position:
    labels:
      - "EXPLICIT_COURTSHIP_ATTEMPT"
      - "EMERGING_PERSONAL_OPENNESS"
      - "JOINT_ART_MARKET_PROJECT"
      - "PROPERTY_AND_CREATIVE_BOUNDARIES_RESPECTED"
      - "NOT_YET_ROMANCE"
    natural_language_definition: >-
      班富蘭已明確把此行目的從單純鈔票材料交流推進為追求疏影；
      疏影沒有承諾戀愛、排他或親密關係，但已明示「可以繼續」，
      並在今晚結束時主動約班富蘭初七再來協助造冊。
      兩人之間第一次形成可持續的私人靠近＋共同工作軸。
      班富蘭替疏影找到一條可能以畫作稀缺、真跡證明與未來收益
      支撐清倌生活的商業路徑，使她「收入不足而被迫改走更高身體營業比重」
      的即時危機得到實質緩解，但永久解決仍取決於後續市場與契約能否成立。

  player_side:
    explicit_intent:
      - "想藉兩張百元美鈔換取疏影好感"
      - "想攻略／追求疏影"
    established_actions:
      - "送疏影兩張 USD 100，明示送出後由疏影自行處置"
      - "陪疏影燒掉其中一張"
      - "以葬花意象與未來畫家死後增值故事切入，與疏影討論作品、死亡與市場"
      - "與潘金蓮、疏影共同發展疏影藝術資產商業模型"
      - "陪疏影回弄影軒"
    boundaries:
      - "沒有取得疏影身體／房門／陪客／創作命令權"
      - "追求意圖 != 疏影已接受戀愛關係"
      - "幫忙解決生計 != 對疏影取得救命恩人支配權"

  shuying_side:
    established_actions:
      - "接受兩張美元贈與"
      - "依自己處分權燒掉一張，另一張收入木匣保留"
      - "參與並逐步接受藝術資產／封存／拍賣的工作方案"
      - "維持作品留、燒、畫不畫皆由本人決定的要求"
      - "初六夜末明示班富蘭的追求『可以繼續』"
      - "約班富蘭初七再來協助造冊"
    boundaries:
      - "不接受被壓平成『林黛玉／病美人』模板"
      - "不准以病弱賣慘作為主要市場敘事"
      - "不因金主／投資人付費取得創作、人身、醫療或房門權"
      - "她可自行決定哪些畫留下、焚毀、是否繼續創作"

  current_relational_effect:
    - "班富蘭不再只是『拿奇物來給疏影研究的人』。"
    - "疏影不再只是『對美元材料好奇的清倌』。"
    - "兩人已形成明確下一次共同工作：初七造冊。"
    - "私人追求與商業合作同時存在，但不得互相偷換成同意。"

  still_not:
    - "ROMANTIC_RELATION_ESTABLISHED"
    - "EXCLUSIVITY"
    - "SEXUAL_ACCESS"
    - "LIFE_PARTNERSHIP"
    - "FINANCIAL_DEPENDENCE_ON_BANFULAN"
    - "BANFULAN_OWNS_OR_CONTROLS_SHUYING_ART"
```

## R02｜疏影 ↔ 觀止

```yaml
RELATIONAL_POSITION:
  relation_ref: "REL-SHUYING-GUANZHI-001"
  standing: "HARD_ESTABLISHED / INSTITUTIONAL_PRESSURE_REFRAMED"

  current_position:
    labels:
      - "QING_COURTESAN_ROUTE"
      - "ART_BASED_INCOME"
      - "ECONOMIC_SUSTAINABILITY_PRESSURE"
      - "IMMEDIATE_RED_ROUTE_PRESSURE_RELIEVED"
      - "NEW_ASSET_MODEL_UNDER_TEST"
    natural_language_definition: >-
      疏影仍以畫藝、不輕易開門、選客與稀缺性維持清路。
      今晚明確顯影：清倌身分不是免於經濟壓力，
      房、飯、藥、紙墨與照護仍需收入；若長期收入不足，
      她維持「拒絕與選擇」的成本會越來越高。
      班富蘭提出的藝術資產方案，使觀止第一次有可能
      不靠提高疏影身體營業比重，也能讓她的名字與作品支撐生活。
      目前只是可信商業路徑＋初八市場測試，尚非終身保障契約。

  established_current_facts:
    - "今晚疏影沒有接客；場景成立她並非全無需求，而是有拒客／不開門的選擇。"
    - "潘金蓮接受先以初八拍賣測市場，不急於今晚把疏影往紅路推。"
    - "清／紅是營業策略，不是貞潔或道德分類。"
    - "疏影的核心經濟困境是：選擇權需要有收入支撐。"

  human_current_setting_clarification:
    - "疏影此類自由契約妓女／清倌的觀止抽傭基準為 15%。"
    - "本 HOT 只作當前 Route 經濟規則使用；不宣稱已回寫人物卡或 WORLD 原文件。"

  still_not:
    - "LIFETIME_SUPPORT_CONTRACT_SIGNED"
    - "RED_ROUTE_PERMANENTLY_IMPOSSIBLE"
    - "GUANZHI_OWNS_SHUYING_ART"
```

## R03｜班富蘭 ↔ 潘金蓮

```yaml
RELATIONAL_POSITION:
  relation_ref: "REL-BF-PAN-001"
  standing: "HARD_ESTABLISHED / MATERIAL_DELTA_THIS_HOT"

  current_position:
    labels:
      - "HOST_MERCHANT_NEGOTIATION"
      - "STRATEGIC_BUSINESS_CO-DESIGN"
      - "MUTUAL_USEFULNESS_WITHOUT_PRIVATE_TRUST"
      - "AUCTION_MODEL_WORKING_ALLIANCE"
    natural_language_definition: >-
      兩人的商業關係已從住宿／代作／抽成升級成可共同設計長期藝術資產市場模型。
      班富蘭提出稀缺、標竿價、封存、真跡冊、死後收益受益權與資本化方案；
      潘金蓮負責以觀止的市場、帳務、拍賣與資本運作能力檢查這些想法能否落地。
      潘金蓮沒有因此成為班富蘭雇主，也沒有把方案正式簽成契約。

  what_changed:
    - "潘金蓮已把班富蘭進一步視為能設計新生意結構的人。"
    - "班富蘭指出『對觀止有利』與『對當代掌櫃帳本有利』不是同一件事。"
    - "潘金蓮接受：若觀止自己全持有未來七成利益，可能造成長期負擔與市場抵制；利益需要外分。"

  still_not:
    - "FORMAL_PARTNERSHIP"
    - "PROFIT_SHARE_FOR_BANFULAN_IN_SHUYING_AUCTION"
    - "SIGNED_INVESTMENT_CONTRACT"
```

## R04｜潘金蓮 ↔ 疏影

```yaml
RELATIONAL_POSITION:
  relation_ref: "REL-PAN-SHUYING-001"
  standing: "HARD_ESTABLISHED / NEW_COMMERCIAL_ALIGNMENT"

  current_position:
    labels:
      - "MANAGER_ARTIST_NEGOTIATION"
      - "QING_ROUTE_SUSTAINABILITY_PROBLEM"
      - "AUCTION_TEST_ALIGNMENT"
      - "CREATIVE_AUTONOMY_RESERVED"
    natural_language_definition: >-
      潘金蓮承認疏影的清路若沒有足夠收入就不能只靠名氣永久撐住；
      疏影則要求任何商業方案都不能把她的畫、病與人生變成掌櫃預先寫好的劇本。
      雙方目前同意把初八市場測試作為下一個關鍵節點：
      疏影掌作品選擇、焚留與創作；觀止負責市場、拍賣、帳務與制度安排。

  temporary_effect:
    - "疏影目前不需因今晚沒有接客就立即改走更高身體營業比重。"
    - "是否能形成長期安全清路，取決於初八成交與之後契約。"

  still_not:
    - "GUANZHI_LIFETIME_GUARANTEE"
    - "PAN_CAN_ORDER_SHUYING_TO_PAINT"
    - "PAN_CAN_ORDER_SHUYING_TO_BURN"
```

## R05｜班富蘭 ↔ 觀止

```yaml
RELATIONAL_POSITION:
  relation_ref: "REL-BF-GUANZHI-001"
  standing: "HARD_ESTABLISHED / EXPANDED_FUNCTION"

  current_position:
    labels:
      - "TEMPORARY_GUEST"
      - "VENUE_BASED_CREATOR"
      - "STRATEGIC_CONTRIBUTOR"
      - "MUTUAL_EXCHANGE_WITHOUT_MEMBERSHIP"
    natural_language_definition: >-
      原三夜住宿、每日兩碗麵、三日場內代作營業安排仍有效。
      今晚班富蘭額外替觀止提出一條可能形成大型公開事件與新型資產收入的方案，
      但這不自動增加他的觀止成員資格、薪資、股份或疏影拍賣分成。

  material_additions:
    - "班富蘭已取得可見人的二手本朝男子衣物借用，以省錢為目的。"

  still_not:
    - "EMPLOYMENT"
    - "MEMBERSHIP"
    - "EQUITY_OWNER"
    - "SHUYING_AUCTION_COMMISSION_RIGHT"
```

---

# 2｜CURRENT SCENE / FREEZE POINT

```yaml
CURRENT_SCENE:
  date: "理火三年・吉月初六"
  time: "深夜；精確刻數 UNKNOWN"
  location: "觀止青樓二樓／弄影軒門外一帶"

  scene_status:
    current_night_major_work: "CLOSED"
    player_declared: "今晚算是做完大事了，可以收工了"
    sleep_state: "NOT_EXPLICITLY_PLAYED"
    date_advance_to_ji07: "NOT_YET_HARD_ADVANCED"

  immediately_relevant_people:
    - "班富蘭"
    - "疏影"

  recently_relevant_people:
    - "潘金蓮｜已完成今晚三方商業模型討論"
    - "龐春梅｜今晚稍早替班富蘭安排二手男子衣物借用"
    - "蘇清｜夜間忙於自己的客人／工作，未參與疏影商業討論"

  freeze_point:
    - "班富蘭已陪疏影回到弄影軒。"
    - "疏影已回房並關門；班富蘭沒有在本 SAVE 中被自動寫成進房、留宿或睡著。"
    - "疏影約班富蘭初七再來協助造冊。"
    - "初八仕女夜被選為疏影第一幅標竿畫公開拍賣的規劃窗口；尚未執行。"
    - "今晚結束時沒有任何藝術投資／終身供養／遺作收益契約正式簽署。"

  next_action_owner: "PLAYER_OR_WORLD_AFTER_RESUME"
  likely_next_operational_window:
    date: "吉月初七"
    content: "作品挑選／造冊／防偽登記／拍賣準備"
    standing: "PLANNED / NOT YET EXECUTED"
```

---

# 3｜MATERIAL NONRELATIONAL STATE

```yaml
MATERIAL_NONRELATIONAL_STATE:

  money_and_ledger:
    player_local_silver:
      status: "POSITIVE_LOCAL_SILVER_OBTAINED / EXACT_TOTAL_UNRECONCILED"
      unresolved_reason:
        - "首闕五兩與後續整首三十兩是否重複計價仍未對帳。"
        - "蘇清另有五兩私人測試付款。"

    banfulan_guanzhi_content_business:
      venue_commission: "30%"
      scope: "目前三日觀止場內詩詞／歌曲營業安排"
      status: "ESTABLISHED"

    shuying_free_contract_route:
      guanzhi_commission_basis: "15%"
      source_status: "HUMAN CURRENT SETTING CLARIFICATION"
      note: "與班富蘭三日代作 30% 抽成是不同帳路，不得混帳。"

  objects_and_custody:
    metal_case:
      owner: "班富蘭"
      contents_baseline: "玩家原設定約 USD 1,000,000"
      current_location: "班富蘭在觀止的指定房間"
      local_exchange_value: "UNKNOWN"
      exact_remaining_nominal_total: "PREVIOUS_TOTAL_MINUS_USD200 / exact inventory not performed"

    prior_wash_test_usd100:
      wash_test: "COMPLETED"
      disposition: "疏影其後特別送回班富蘭"
      current_owner: "班富蘭"

    two_new_usd100_gifts_to_shuying:
      gift_status: "COMPLETED"
      total_nominal_face_value: "USD 200"
      note_A:
        denomination: "USD 100"
        status: "BURNED / DESTROYED"
      note_B:
        denomination: "USD 100"
        owner: "疏影"
        status: "RETAINED"
        custody: "疏影木匣／房內收藏路線"

    borrowed_period_clothing:
      possessor: "班富蘭"
      source: "龐春梅／觀止安排"
      nature: "BORROWED USED PRESENTABLE MALE PERIOD OUTFIT"
      silk_or_luxury: false
      return_expectation: "三日借用期／離開前歸還方向"
      damage_charge: "YES / amount not fixed"
      current_wear_state: "沿用本朝男子換裝，除非玩家另換"

  physical_state:
    shuying:
      chronic_cough_or_illness: "ESTABLISHED CHARACTER BASELINE"
      exact_diagnosis: "UNKNOWN / DO NOT INVENT"

  contracts:
    BF-C01:
      title: "觀止三夜住宿＋每日兩碗麵＋三日代作營業"
      state: "ACTIVE / PARTIALLY PERFORMED"
      venue_commission: "30%"

    BF-C02:
      title: "周玉娘／錦棠收購談判"
      state: "NEGOTIATED / PERFORMANCE_NOT_FULLY_PLAYED"
      acquisition_price_to_broker_chain: "600 taels"
      personal_increment_for_jintang: "200 taels"
      transfer_completed: "UNKNOWN / NOT_FULLY_PLAYED"
      official_registration_completed: "NOT_ESTABLISHED"

    BF-C03:
      title: "疏影藝術資產／終身支持／遺作收益模型"
      state: "WORKING BUSINESS MODEL ONLY / NOT SIGNED"
      formal_contract: false
      money_received: false
      rights_sold: false
      paintings_auctioned: false
      lifetime_support_established: false

  deadlines_and_plans:
    - "吉月初七：預定進行疏影作品挑選、造冊與防偽登記準備；尚未執行。"
    - "吉月初八：仕女夜；預定作為疏影第一幅標竿畫公開拍賣窗口；尚未執行。"
```

---

# 4｜SHUYING ART MARKET MODEL｜工作方案，不是已執行契約

```yaml
SHUYING_ART_MARKET_WORKING_MODEL:
  model_status:
    standing: "THREE_PARTY_DISCUSSION / WORKING DESIGN"
    parties_in_discussion: ["班富蘭", "疏影", "潘金蓮"]
    signed: false
    executed: false

  phase_1_benchmark:
    - "由疏影自己選一幅願意真正離手的畫。"
    - "該畫作為唯一公開流通的第一幅標竿畫。"
    - "必須真實公開競價，不做假拍／自買抬價。"

  phase_2_public_burning_and_sealing:
    - "疏影可從珍藏畫中挑出自己不願留傳後世的作品。"
    - "可在拍賣活動中當眾焚毀；燒幾幅完全由疏影決定。"
    - "不得由潘金蓮／班富蘭／投資人為抬價而命令她燒。"
    - "剩餘決定留傳的既有作品造冊後封存。"

  phase_3_registry_and_authentication:
    first_registry:
      scope: "初次封存的既有作品"
      per_work_record:
        - "唯一編號"
        - "題材／尺寸／紙墨等基本描述"
        - "作品故事／形成背景"
        - "可核驗的獨特缺陷與物理特徵"
        - "例如左上約二寸處小孔、折痕、滲墨、紙纖維異常等"
      purpose: ["防偽", "未來真跡鑑別", "provenance"]

    registry_security:
      - "真跡冊本身必須登記、封存、上封條。"
      - "防偽細節不宜全部公開，避免教偽作者仿造。"
      - "外部可另保留不洩漏秘密鑑定點的存目／封存存在證明。"

    later_registry:
      - "初次封存後疏影的新作另起新冊。"
      - "同樣登記編號、故事、獨特缺陷／物理特徵。"
      - "後續是否燒、留、贈、售由疏影決定。"
      - "本 HOT 尚未實際建立任何冊頁或作品編號。"

  phase_4_posthumous_auction:
    - "工作方案方向：疏影死後所有可處分存世作品均進公開市場競價，不預先按張數分畫給受益人。"
    - "先市場競價，再分貨幣所得。"

    proposed_proceeds_split:
      sponsor_beneficial_interest: "70%"
      guanzhi_commission: "15%"
      shuying_designated_heir_pool: "15%"
      standing: "WORKING MODEL / NOT SIGNED"

    sponsor_bid_rule:
      - "持有七成受益權者若想保有某幅畫，也必須進公開市場競價拍回。"
      - "成交價仍進拍賣所得，再依約定比例分配。"

  phase_5_financing_the_70_percent_interest:
    if_benchmark_auction_strong:
      - "將未來 70% 遺作公開拍賣所得受益權打包拍賣。"
      - "出售的是經濟受益權，不是疏影人身權、創作權或直接畫作處置權。"
      - "觀止立即取得受益權出售現銀。"
      - "以此作本金進行觀止可承擔的放貸／資本運用。"
      - "以利息／現金流支付疏影生前生活、醫藥、紙墨與養老支出。"

    if_benchmark_auction_weak:
      - "觀止暫不賤賣 70% 受益權。"
      - "待疏影市場身價上升後，分段出售 10%～20% 等受益份額。"
      - "利益外分可讓更多外部持有人產生維持疏影市場熱度的經濟動機。"

  non_transferable_boundaries:
    - "收益受益權 != 疏影人身權"
    - "收益受益權 != 性服務權"
    - "收益受益權 != 房門權"
    - "收益受益權 != 催畫權"
    - "收益受益權 != 醫療決定權"
    - "收益受益權 != 作品真跡所有權"
```

---

# 5｜仕女夜｜初八拍賣的目前法位

```yaml
JI08_LADIES_NIGHT_AUCTION_WINDOW:
  planned_date: "理火三年・吉月初八"
  event: "仕女夜"
  auction_status: "PLANNED / NOT YET EXECUTED"

  current_world_schedule:
    regular_days: ["初一", "初八", "十五", "二十二"]

  human_current_setting_clarification:
    commercial_core:
      - "可類比現代夜場：女性免入場費，男性付雙倍入場費。"
      - "女性越多，男性客流與付費意願越容易上升。"
    social_core:
      - "良家成年女性以紅線標記，與妓女身分分開。"
      - "此夜形成成年男女少數可在觀止規則內公開搭訕／社交的場合。"
      - "良家女性來場不等於出軌、不等於性同意。"
      - "可單純社交，也存在自願發展私情／出軌的可能。"
      - "未出嫁的成年女性也可能來場。"

  identity_and_consent_locks:
    - "紅線 != 妓女身分"
    - "紅線 != 性史"
    - "紅線 != 同意"
    - "入場 != 出軌"
    - "搭訕機會 != 對方必須接受"

  shuying_use:
    - "疏影初八若出席拍賣，是自願參與自己的作品公開事件，不是被排班接客。"

  not_yet_fixed:
    - "第一幅標竿畫是哪一幅"
    - "當夜實際焚毀幾幅"
    - "實際封存幾幅"
    - "拍賣底價"
    - "受邀買家名單"
    - "拍賣主持人"
    - "保管商會／錢莊"
    - "70% 受益權是否同夜拍賣"
```

---

# 6｜MINIMAL RECENT EVENT EVIDENCE

```yaml
MINIMAL_EVENT_EVIDENCE:
  BF-E08:
    title: "班富蘭回房整理並取得本朝二手男子衣物"
    effect: "吃、住、穿的短期生存條件補齊。"

  BF-E09:
    title: "班富蘭以兩張百元鈔主動追求疏影"
    effect: "班富蘭↔疏影由材料研究跨入明確追求與私人靠近。"

  BF-E10:
    title: "葬花、死後畫價與疏影生計危機被連成一條線"
    effect: "班富蘭看出疏影清路的根本危機是收入不足會侵蝕她的拒絕權。"

  BF-E11:
    title: "班富蘭／疏影／潘金蓮完成藝術資產模型第一輪設計"
    effect: "疏影第一次取得可能不靠增加身體營業比重也能長期維持清路的可信商業方案。"
    unresolved: "全部未簽契、未收款、未交割"

  BF-E12:
    title: "初八仕女夜成為標竿畫拍賣規劃窗口"
    status: "PLANNED"

  BF-E13:
    title: "班富蘭陪疏影回房，今晚關係收束"
    effect: "疏影明示追求可以繼續，並約初七共同造冊。"
```

---

# 7｜OPEN THREADS / DUE ITEMS

```yaml
OPEN_THREADS:
  - ref: "TH-BF-01"
    state: "今晚工作段已收束；尚未硬寫睡著。"

  - ref: "TH-BF-02"
    state: "班富蘭既有詩詞收入仍有首闕五兩／整首三十兩對帳問題。"

  - ref: "TH-BF-03"
    due: "吉月初七"
    state: "班富蘭＋疏影共同挑畫、造冊、防偽登記；尚未執行。"

  - ref: "TH-BF-04"
    due: "初八前"
    state: "疏影選第一幅願意真正離手的標竿畫；尚未選定。"

  - ref: "TH-BF-05"
    due: "初八"
    state: "是否當眾燒畫、燒哪些、燒幾幅，全由疏影本人決定。"

  - ref: "TH-BF-06"
    state: "尋找第三方商會／錢莊／庫房作封存；尚未選定。"

  - ref: "TH-BF-07"
    due: "吉月初八仕女夜"
    state: "第一幅標竿畫公開拍賣；尚未執行。"

  - ref: "TH-BF-08"
    state: "70% 遺作拍賣所得受益權是否整包拍賣或分段出售，取決於第一幅標竿畫市場表現。"

  - ref: "TH-BF-09"
    state: "終身支持、15% 觀止佣金、15% 疏影指定繼承池均尚未正式契約化。"

  - ref: "TH-BF-10"
    state: "錦棠六百／二百、換契、官冊仍未完整演出。"

  - ref: "TH-BF-11"
    state: "蘇清測試與蘇軾住附近之鉤仍存在，但降為背景 active ref。"

  - ref: "TH-BF-12"
    state: "二手男子衣物借用仍有歸還義務。"
```

---

# 8｜FORBIDDEN PROMOTIONS

```yaml
FORBIDDEN_PROMOTIONS:
  - "疏影說『可以繼續追』 != 已成戀人"
  - "共同燒一張美元 != 定情信物"
  - "班富蘭幫疏影找到商業出路 != 疏影欠他感情／身體／忠誠"
  - "初七約造冊 != 私密留宿／性邀請"
  - "工作模型 != 已執行"
  - "初八規劃 != 拍賣已成立"
  - "標竿畫概念 != 已選出標竿畫"
  - "可當眾燒畫 != 疏影已決定燒幾幅"
  - "造冊方案 != 冊已建立"
  - "封存方案 != 第三方庫房已選定"
  - "70% 受益權方案 != 受益權已出售"
  - "投資人買收益權 != 買疏影"
  - "投資人買收益權 != 買創作命令權／醫療決定權／房門權"
  - "女客免入場費 != 女客提供性服務"
  - "紅線 != 妓女／性史／同意"
  - "仕女夜可搭訕 != 可強迫良家婦女"
  - "今晚收工 != 玩家已睡著"
  - "錦棠線未在場 != 錦棠交易自動完成"
```

---

# 9｜LOOKUP REFS

```yaml
LOOKUP_REFS:
  previous_hot:
    file: "觀止青樓_班富蘭線_HOT_SAVE_V1.01_RELATION_FIRST_吉月初六夜_CURRENT.md"

  overlay:
    file: "GUANZHI_SAVE_RELATION_FIRST_EXTERNAL_OVERLAY_V0.3_FULL_EXP_20261007.md"

  character_baseline:
    file: "觀止人物卡池_LCAPG_V3.3.20_CURRENT_RATIFIED_71人_辭歲肉身菩薩人格重錨_20261003.md"

  current_world:
    file: "02_GUANZHI_WORLD_V2.2.2_CURRENT_V3.11_RUNTIME_POINTER_INTEGRATED_20261006.md"

  current_core:
    file: "01_GUANZHI_RUNTIME_CORE_V3.11_CURRENT_COMPANION_WORLD_V2.2.2_CORRECTED_20261006.md"

  current_main:
    file: "01_MAIN_V4.4_PROTOCOL_V3.0.1_LIGHTER_V4.8_RECEIPT_I9_FULL_RATIFIED_20261006.md"

  current_lighter:
    file: "02_LIGHTER_V4.8_PROTOCOL_V3.0.1_RECEIPT_I9_CURRICULUM_FULL_RATIFIED_20261006.md"
```

---

# 10｜DIRECT CONTINUATION POINT｜30 秒接關

```text
1. 班富蘭 ↔ 疏影：
   已從美元材料研究跨入「明確追求＋共同商業方案」。
   疏影說可以繼續追，並約初七造冊。
   不是戀人、沒有性同意、沒有排他。

2. 疏影 ↔ 觀止：
   清路真正的壓力是收入能否支撐她的拒絕權。
   今晚找到可信新路，因此立即被迫轉紅的危機暫時解除。
   長期能否成立，要看初八市場與契約。

3. 班富蘭 ↔ 潘金蓮：
   已能共同設計資產、市場與融資結構。
   雙方沒有正式合夥。

4. 潘金蓮 ↔ 疏影：
   潘負責市場／帳／拍賣；疏影掌畫、燒、不燒、創作與人生。
   目前沒有終身供養契。

硬事實：
- 班富蘭吃、住、穿的短期生存條件已齊。
- 金屬美元箱已進班的指定房間；本地固定匯率仍不存在。
- 之前水洗的 USD100 已由疏影送回班。
- 今晚另送疏影兩張 USD100：一張已燒毀，一張由疏影留在木匣。
- 班借得二手本朝男子衣物，仍有歸還義務。
- 初七預定：造冊、防偽、選畫。
- 初八仕女夜預定：第一幅標竿畫公開拍賣。
- 拍賣、封存、受益權出售、終身支持契約全部尚未真正執行。

今晚凍結：
班富蘭已陪疏影回弄影軒。
疏影已關門。
玩家明示今晚可以收工。
不要替班富蘭自動進疏影房、睡著、簽契或把日期硬推進初七。
若玩家下一輪直接指定「隔天／初七」，可從造冊準備開始。
```

---

# 11｜RELATION-FIRST 實跑追蹤

```yaml
RELATION_FIRST_TEST_TRACKING:
  overlay_version: "V0.3-FULL-EXP"
  test_instance: "BANFULAN_HOT_V1.02"
  role: "ROUND_2_OUTPUT / ROUND_3_INPUT"
  effective_rounds_target: "5-6"

  current_relation_center_count: 5
  prior_relations_not_centered_but_preserved:
    - "班富蘭 ↔ 蘇清"
    - "潘金蓮 ↔ 錦棠"
    - "錦棠 ↔ 姚二娘"

  material_facts_retained: true
  unknown_preserved: true
  relation_seed_overpromotion_blocked: true
  business_model_execution_not_fabricated: true
  evidence_traceability: "PASS"

  verdict: "ROUND_2_COMMITTED / CONTINUE EXPERIMENT"
```

---

# 12｜SAVE COMMIT / 法位邊界

```yaml
SAVE_COMMIT:
  human_authorization:
    type: "DIRECT_EXPLICIT_SAVE_REQUEST_IN_CURRENT_CONVERSATION"
    exact_intent: "今晚算是做完大事了，可以收工了。HOT SAVE"
    status: "TRUE"

  document_result:
    status: "COMMITTED"
    route_current_hot: "V1.02"
    previous_hot_preserved: "V1.01"
    relation_first_projection_used: true

  source_boundary:
    overlay_is_source_of_truth: false
    original_event_evidence_replaced: false
    working_business_model_is_not_signed_contract: true

  execution_boundary:
    document_level_save_commit: true
    host_instrumented_formal_save_execution: "NOT_ESTABLISHED"
    e6_e7: "NOT_ESTABLISHED"

  core_schema:
    changed: false
    save_owner_changed: false
    write_path_owner_changed: false
    world_file_modified: false
    character_pool_modified: false
```

---

# 13｜根句

> **今晚真正留下來的，不是一場已經完成的拍賣。**
>
> **而是疏影第一次有了一條可能讓「不願意」本身養得活她的路。**
>
> **班富蘭也第一次從觀止的短期住客，走進一個人的未來帳本。**
>
> **初七造冊。初八看市場。**
>
> **在那以前，一切仍只是有資格被實驗的方案，不是已經兌現的勝利。**

END OF CURRENT HOT SAVE V1.02
# 觀止青樓（新）｜班富蘭線 HOT SAVE V1.03
## RELATION-FIRST｜理火三年・吉月初七夜｜深秋詩會／汴京文人場失控擴張版

> **CURRENT ROUTE HOT SAVE / HUMAN EXPLICIT SAVE REQUEST / RELATION-FIRST TEST INSTANCE**
>
> 本版承接 `觀止青樓_班富蘭線_HOT_SAVE_V1.02_RELATION_FIRST_吉月初六深夜_疏影藝術資產線_CURRENT.md`。
> 依 `GUANZHI SAVE RELATION-FIRST EXTERNAL OVERLAY V0.3-FULL-EXP` 編譯第一讀取面。
>
> 本檔保存：初七中午至夜間已演出之關係變化、詩會現場硬狀態、作品來源分類、群眾外溢、未決風險與下一接關點。
> 作品「好／不好」與「誰作」分離；來源 UNKNOWN 不自動升格為班富蘭原作；已辨識來源不得因玩家宣告改名。
>
> 人類 AnjouRan 於本次對話明示：「先HOT SAVE吧 然後我們再繼續」。
> 因此本版成立 **專案內文件級 HOT SAVE commit**。
> 不宣稱 Host deployment、Formal Host execution、E6／E7 或獨立 Runtime SAVE instrumentation 已成立。

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BANFULAN_HOT_V1_03_RELATION_FIRST_JI07_NIGHT_LATE_AUTUMN_POETRY_SALON"
  route_id: "GUANZHI_BANFULAN_ROUTE"
  route_name: "班富蘭線"
  player_public_identity: "班傑明／字富蘭／號克林居士"
  version: "V1.03"
  record_type: "HOT_SAVE"
  record_state: "VALID / CURRENT / HUMAN_EXPLICIT_SAVE_REQUEST"
  story_date: "理火三年・吉月初七"
  time_of_day: "夜；深秋詩會進行中；精確刻數 UNKNOWN"
  current_location: "觀止青樓大堂"
  scene_segment_status: "JI07_LATE_AUTUMN_POETRY_SALON_ACTIVE"
  previous_valid_hot:
    version: "V1.02"
    file: "觀止青樓_班富蘭線_HOT_SAVE_V1.02_RELATION_FIRST_吉月初六深夜_疏影藝術資產線_CURRENT.md"
    treatment: "PRESERVED / SUPERSEDED_AS_CURRENT_HOT_ONLY"
  relation_first_overlay: "V0.3-FULL-EXP"
  relation_first_view_status: "DERIVED_FIRST_READ_VIEW / NOT_INDEPENDENT_SOURCE_OF_TRUTH"
  evidence_origin:
    - "SAME_CONTEXT_REFERENCE"
    - "HUMAN_EXPLICIT_DIRECTION"
    - "NPC_AUTONOMOUS_ACTION_WITHIN_DIRECTOR_SCOPE"
  formal_host_save_execution: "NOT_ESTABLISHED"
  created_real_date: "2026-10-07"
  timezone: "Asia/Taipei"
```

---

# 1｜RELATIONAL CENTER｜第一讀取面

## R01｜班富蘭 ↔ 蘇清

```yaml
RELATIONAL_POSITION:
  relation_ref: "REL-BF-SUQING-001"
  standing: "HARD_ESTABLISHED / MATERIAL_DELTA_THIS_HOT"

  current_position:
    labels:
      - "FELLOW_ANOMALY_RECOGNITION"
      - "SOURCE_RECOGNITION_CHECKER"
      - "TEASING_ADVERSARIAL_FAMILIARITY"
      - "MODERN_KNOWLEDGE_ASYMMETRY"
      - "NOT_ROMANCE"
    natural_language_definition: >-
      蘇清已成為班富蘭腦中『舊庫作品』最主要的現場來源辨識者之一。
      她會區分：自己確定知道來源、只覺得熟悉、來源版本追不到、完全不知道。
      班富蘭反過來故意拿蘇清熟悉或半熟悉的後世作品測她、逗她，
      形成一條強烈的現代人默契與互相拆台軸。
      此關係仍以同時代異常者／信息對手／朋友式鬥嘴為主，沒有建立戀愛或性關係。

  established_this_hot:
    - "蘇清對班富蘭『仁宗』口誤立即示警，協助現場止血。"
    - "蘇清辨識多首後世作品並拒絕把熟悉感自動升格成作者證明。"
    - "蘇清明確提出：不能證明不是班富蘭 != 已證明就是班富蘭。"
    - "班富蘭故意拿《天淨沙·秋思》《客途秋恨》等測她是否抓得到。"
    - "班富蘭明知《煙花易冷》作者但故意不告訴蘇清；蘇清後因《青花瓷》辨識到相關創作來源線索。"

  still_not:
    - "ROMANTIC_RELATION"
    - "SOURCE_OMNISCIENCE"
    - "SUQING_CAN_PROVE_EVERY_FUTURE_WORK_AUTHOR"
    - "BANFULAN_MEMORY_IS_RELIABLE_INDEX"
```

## R02｜班富蘭 ↔ 李師師

```yaml
RELATIONAL_POSITION:
  relation_ref: "REL-BF-LISHISHI-001"
  standing: "HARD_ESTABLISHED / NEW_LITERARY_JUDGING_RELATION"

  current_position:
    labels:
      - "INDEPENDENT_LITERARY_AND_PERFORMANCE_JUDGE"
      - "MUSICALITY_AND_CIRCULATION_EVALUATOR"
      - "PUBLIC_SEAT_AUTONOMY"
      - "NO_AUTO_FAVOR"
    natural_language_definition: >-
      李師師接受今晚作為深秋詩會雙席之一，評判權完全獨立，
      不因班富蘭住觀止、替觀止創造客流或與潘金蓮合作而偏袒。
      她對班富蘭作品的主要判斷軸包含：能不能唱、能不能進人耳朵、
      能不能在場中流傳，以及作品中的情感位置是否成立。

  established_this_hot:
    - "接受今晚雙席評詩，但保留可判無人合格。"
    - "對班富蘭第一題作品給出結構性肯定，未取消其字句生硬問題。"
    - "對後世歌曲多次從『可唱／可傳』角度評判。"
    - "在拿班富蘭『十年』之作與蘇軾未來《江城子》比較時，明確認為兩者可進同一情感位置，但未判班富蘭已壓過蘇詞。"
    - "提醒把女人比作器物之美不等於女人失去說不的權利。"

  still_not:
    - "ROMANCE"
    - "SEXUAL_ACCESS"
    - "GUARANTEED_PRAISE"
    - "HER_NAME_AVAILABLE_FOR_COMMERCIAL_ENDORSEMENT_WITHOUT_CONSENT"
```

## R03｜班富蘭 ↔ 柳如是

```yaml
RELATIONAL_POSITION:
  relation_ref: "REL-BF-LIURUSHI-001"
  standing: "HARD_ESTABLISHED / NEW_INTELLECTUAL_INTEREST"

  current_position:
    labels:
      - "INDEPENDENT_LITERARY_JUDGE"
      - "LATE_MING_KNOWLEDGE_ADVANTAGE"
      - "SOURCE_AND_ACCOUNT_SEPARATION"
      - "POLITICAL_HISTORICAL_SENSITIVITY"
      - "INTELLECTUAL_INTEREST_NOT_ROMANCE"
    natural_language_definition: >-
      柳如是今晚明確對班富蘭形成高強度文學與人物興趣，
      尤其被『國事誰問』『救民心』『亡城／史冊／等待』等作品軸吸引。
      她同時堅持作品來源與作品價值分帳：不是班富蘭原作仍可很好；
      作者已知就照原作者記；來源 UNKNOWN 也不能硬填班富蘭。

  established_this_hot:
    - "與李師師共同擔任雙席，兩人可判不同結果。"
    - "對班富蘭政治／歷史向作品表現出明確偏好，但不因此給其所有作品高評。"
    - "辨識《天淨沙·秋思》為馬致遠元曲，因其晚明知識時點晚於元代。"
    - "不認得納蘭、王國維等其人生之後的作品，並把這些當作真正後世文學窗口。"
    - "接受『後世舊作寄存簿』：已知作者照原名；UNKNOWN 保留 UNKNOWN；班富蘭只能主張代管，不能改作者。"

  key_line_effect:
    - "她曾對班富蘭作品表達：前面知道你有才；某政治向一首開始想知道你這個人。"
    - "此為人物／思想興趣，不等於情愛、承諾或親密權。"

  still_not:
    - "ROMANCE"
    - "SEXUAL_INTEREST_ESTABLISHED"
    - "BLANKET_LITERARY_APPROVAL"
```

## R04｜班富蘭 ↔ 蘇軾

```yaml
RELATIONAL_POSITION:
  relation_ref: "REL-BF-SUSHI-001"
  standing: "HARD_ESTABLISHED / NEW_COMPETITIVE_LITERARY_RECOGNITION"

  current_position:
    labels:
      - "LITERARY_RIVALRY"
      - "MUTUAL_RECOGNITION_WITHOUT_SUBMISSION"
      - "FUTURE_KNOWLEDGE_ASYMMETRY"
      - "PLAYFUL_TENSION"
    natural_language_definition: >-
      蘇軾在被現場請入後，真正與班富蘭進入即席對作。
      第一題『歸人』採半篇互試規則；蘇軾最終對班富蘭表示『我不服你，但我認你』。
      班富蘭又以蘇軾未來名作、赤壁與海南後事玩梗，形成強烈的未來資訊不對稱。
      蘇軾本人尚不知道自己的後世作品與人生事件，不能把未來資訊倒灌成其當前記憶。

  established_this_hot:
    - "蘇軾接受班富蘭作為值得認真出手的文學對手。"
    - "蘇軾本人未承認輸掉整場詩會。"
    - "蘇軾不知道未來《江城子》、赤壁名篇、海南貶謫等細節；場中部分後世人物知道。"
    - "班富蘭對蘇軾的未來玩梗沒有改變歷史尚未發生的法位。"

  still_not:
    - "FRIENDSHIP_FORMALLY_ESTABLISHED"
    - "MASTER_DISCIPLE"
    - "BANFULAN_DEFEATED_SUSHI"
    - "SUSHI_ACCEPTED_FUTURE_AS_FACT"
```

## R05｜班富蘭 ↔ 歐陽修

```yaml
RELATIONAL_POSITION:
  relation_ref: "REL-BF-OUYANGXIU-001"
  standing: "HARD_ESTABLISHED / NEW_LITERARY_CHALLENGE"

  current_position:
    labels:
      - "OLDER_LITERARY_AUTHORITY"
      - "SKEPTICAL_BUT_ENGAGED"
      - "SECOND_TOPIC_PARTICIPANT"
    natural_language_definition: >-
      歐陽修因詩會消息進場，且與前一日《生查子》碰撞背景相連。
      他沒有接受班富蘭『狂生』姿態作為免檢通行證，但願意正式下場寫第二題。
      對班富蘭作品會區分：作品好、是否貼題、是否原作、是否只是換字變體。

  still_not:
    - "PERSONAL_ALLIANCE"
    - "DISCIPLE_RECOGNITION"
    - "ALL_WORKS_APPROVED"
```

## R06｜班富蘭 ↔ 柳永

```yaml
RELATIONAL_POSITION:
  relation_ref: "REL-BF-LIUYONG-001"
  standing: "HARD_ESTABLISHED / NEW_SONG_AND_CI_CURIOSITY"

  current_position:
    labels:
      - "SONG_FORM_INTEREST"
      - "POPULAR_CIRCULATION_EYE"
      - "FUTURE_WORKS_CURIOSITY"
      - "LITERARY_PARTICIPANT"
    natural_language_definition: >-
      柳永被現場可唱、易記、白描型作品吸引後正式下場。
      他對班富蘭舊庫中的後世歌曲有強烈『偷師』興趣，
      並明確區分：不是班富蘭原作，不等於不值得學。
      他特別重視唱出口後第二桌是否記得、句子是否有拍子與場內傳播性。

  still_not:
    - "AUTHORSHIP_TRANSFER"
    - "FORMAL_COLLABORATION_CONTRACT"
    - "BANFULAN_TAUGHT_LIUYONG_FUTURE_MUSIC_SYSTEM"
```

## R07｜班富蘭 ↔ 觀止大堂公眾

```yaml
RELATIONAL_POSITION:
  relation_ref: "REL-BF-GUANZHI_PUBLIC-001"
  standing: "HARD_ESTABLISHED / HIGH_PUBLIC_ATTENTION"

  current_position:
    labels:
      - "PUBLIC_NOTORIETY_RISING"
      - "AUTHORSHIP_CONFUSION_RISK"
      - "LITERARY_CURIOSITY"
      - "RUMOR_MULTIPLIER"
      - "COMMERCIAL_DRAW"
    natural_language_definition: >-
      班富蘭已從觀止內部短期住客變成今晚大堂公開焦點。
      公眾對他的印象同時包含：狂、能寫、腦中有大量後世作品、
      愛認領 UNKNOWN 來源、敢與名家對打、會把現代／未來概念丟進宋人場域。
      這些印象正在由抄稿、酒桌、門外傳話與錯誤歸因迅速外溢。
```

---

# 2｜CURRENT SCENE / FREEZE POINT

```yaml
CURRENT_SCENE:
  date: "理火三年・吉月初七"
  time: "夜；深秋詩會持續中；精確刻數 UNKNOWN"
  location: "觀止青樓大堂"

  core_event:
    title: "深秋詩會"
    status: "ACTIVE / NOT FINISHED"
    first_topic: "歸人"
    second_topic: "秋盡"

  judges:
    - "李師師｜雙席之一；獨立評判"
    - "柳如是｜雙席之一；獨立評判"
    judge_independence:
      - "兩人不必一致。"
      - "可判班富蘭差。"
      - "可判無人合格。"
      - "文學欣賞 != 感情／性／陪客獎勵。"

  major_literary_participants_present:
    - "班富蘭"
    - "蘇軾"
    - "歐陽修"
    - "柳永"

  other_key_people_present_or_active:
    - "蘇清"
    - "潘金蓮"
    - "龐春梅"
    - "大量太學生、文士、書肆人、商人、青樓客、看熱鬧者"

  crowd_state:
    hall: "VERY_CROWDED / NEAR_CAPACITY"
    upper_floor: "CROWDED / SEATING_CONFLICT_RISK"
    entrance: "PEOPLE_CONTINUE_TO_ARRIVE / RUMOR_OUTFLOW_ACTIVE"

  exact_freeze_point:
    - "班富蘭剛將《青花瓷》作為後世舊庫作品展示。"
    - "蘇清辨識《青花瓷》並提到其現代演唱／作詞來源；班富蘭先前明知《煙花易冷》作者但故意不說。"
    - "柳如是、李師師、柳永、蘇軾等已對其器物意象、可唱性與後世視角展開評議。"
    - "大堂已有瓷器商人開始追問『青花』『天青色』『窯』等工藝／商品問題。"
    - "詩會尚未正式宣布第二題勝負，也尚未散場。"
    - "班富蘭下一個重大行動仍由玩家決定；世界／大堂可自行繼續生事。"
```

---

# 3｜詩會硬事件摘要

```yaml
POETRY_SALON_EVENTS:
  BF-E14:
    title: "仁宗口誤與《仁》口訣止血"
    established:
      - "班富蘭曾在公開場合脫口說出在位皇帝後世廟號『仁宗』。"
      - "蘇清立即示警。"
      - "班富蘭以『仁愛／鄉下學論語口訣／西域夫子』說法轉移。"
      - "此事已被現場部分人接受為可疑但可解釋，不代表完全消除風險。"

  BF-E15:
    title: "公開表演署名要求"
    established:
      - "班富蘭曾要求公開／商業表演其內容時使用『克林居士』名義。"
      - "私人哼唱未被他要求全面管制。"
      - "此為場內商業／署名主張，不等於現代法律著作權制度已在宋代成立。"

  BF-E16:
    title: "深秋詩會成立"
    established:
      - "潘金蓮接受今晚在觀止大堂設『深秋詩會』。"
      - "核心宣傳：李師師、柳如是雙席評詩；克林居士初試汴梁；班富蘭自稱欲壓京師才子。"
      - "班富蘭要求題目現場出；不要再出中秋。"
      - "李師師、柳如是各自獨立出題／評判。"

  BF-E17:
    title: "第一題『歸人』"
    established:
      - "李師師出題『歸人』。"
      - "班富蘭狂言讓全場先作，怕自己作品一出比賽就結束。"
      - "此言刺激更多文士投入。"
      - "蘇軾被現場文士請入；班富蘭先拿紅燒肉／糖話題與其玩梗，再提出半篇互試。"
      - "蘇軾與班富蘭各出半篇後補全；蘇軾最終表達『我不服你，但我認你』。"
      - "此為文學對手認可，不是蘇軾承認整場敗北。"

  BF-E18:
    title: "歐陽修與柳永進場"
    established:
      - "歐陽修到場並正式參加第二題。"
      - "柳永因現場可唱、易懂、流傳性強的作品型態進場並下場。"
      - "三名宋代大文人同場，進一步推高大堂客流與傳聞。"

  BF-E19:
    title: "第二題『秋盡』"
    established:
      - "柳如是出題『秋盡』。"
      - "核心題意：一個時節走到盡頭後，還剩什麼。"
      - "班富蘭連續拿出多種風格作品／舊庫作品。"
      - "歐陽修、蘇軾、柳永亦各出現場作品。"
      - "第二題尚未正式宣布最終勝負。"

  BF-E20:
    title: "舊庫／原作來源爭議制度化"
    established:
      - "蘇清與柳如是明確分離：作品價值 != 作者歸屬。"
      - "班富蘭一度主張 UNKNOWN 作品全部算自己的著作權，遭現場反駁。"
      - "班富蘭退為『先代管，等真正作者來了再還』。"
      - "觀止形成『後世舊作寄存簿』概念：已知作者照原名；來源可證作者未知則 UNKNOWN；班富蘭代管不改作者。"

  BF-E21:
    title: "大堂自治長出的五類問題"
    established:
      - "抄稿多手轉傳造成作品作者錯配。"
      - "有人在場內私設賭盤，將文學評價綁上เงินจริง。"
      - "政治向句子被斷章外傳，出現『克林居士罵朝廷無人』式變形。"
      - "今夜親筆稿本身出現收藏市場；買的是物件／來源，不必等於作品著作權。"
      - "二樓與門口人潮開始出現座位、視線、碰撞與秩序問題。"

  BF-E22:
    title: "身份不明的小廝確認文人到場後離開"
    established:
      - "一名不起眼小廝曾進場確認蘇軾、歐陽修、柳永等人在場後離去。"
      - "身份、雇主、目的均 UNKNOWN。"
      - "不得自動升格為官府、御史、敵對勢力或陰謀。"

  BF-E23:
    title: "韋小寶故事引發觀止自我映照"
    established:
      - "班富蘭向大堂介紹韋小寶妓院出身、母為妓女、父不明、七妻、公主等故事梗概。"
      - "又講其母有錢後想擴張妓院／當老鴇及大床搬回官衙的荒唐故事。"
      - "李師師、潘金蓮等將其聽成『不必洗掉妓院出身』與『把妓院床抬進官衙』的階級／身份寓意。"
      - "此為班富蘭講述後世虛構作品內容，不是觀止現世人物史實。"

  BF-E24:
    title: "《青花瓷》引發文學→器物市場外溢"
    established:
      - "班富蘭展示《青花瓷》後，大堂除文學評議外，開始有瓷商追問青花、天青色、窯等器物問題。"
      - "這只是信息／想像刺激；不代表班富蘭已掌握或交付任何後世制瓷技術。"
```

---

# 4｜作品來源與法位分類｜DO NOT MERGE AUTHORSHIP

> 本節只保存本場已成立的『來源認知狀態』，不是替外部文學史做終局考證。

```yaml
WORK_SOURCE_LEDGER:

  category_A_route_new_or_claimed_new:
    note: "目前只表示本場尚無已成立外部來源反證；不自動等於全世界已驗證原創。"
    works:
      - title: "第一題長篇『冷雨迷途…／此身仍在，猶有歸途／長夜未盡，此意長明』"
        standing: "BAN_PRESENTED_AS_OWN / NO_ROUTE_SOURCE_CHALLENGE_ESTABLISHED"
      - title: "《秋風秋雨愁煞人》"
        clarification: "『秋風秋雨愁煞人』在本場被玩家明示為詩名，不是正文第一句。"
        standing: "BAN_PRESENTED_AS_OWN / NO_ROUTE_SOURCE_CHALLENGE_ESTABLISHED"
      - title: "『用十年換得一夜…』之作"
        standing: "BAN_PRESENTED_AS_CURRENT_PIECE / SOURCE_NOT_RESOLVED_IN_ROUTE"

  category_B_known_future_or_prior_works:
    note: "不得算班富蘭今晚原創；可作展示、評議、傳播研究。"
    works:
      - title: "《天淨沙·秋思》"
        recognized_by: "柳如是"
        route_attribution: "馬致遠／元曲"
      - title: "《菊花台》"
        recognized_by: "蘇清"
      - title: "《煙花易冷》"
        recognized_by: "蘇清認作品；班富蘭表示知道作者但先不告訴她"
      - title: "含『人生若只如初見』之後世拼接／改編作品"
        recognized_core_source_by: "蘇清"
        route_source_note: "納蘭性德核心名句／另混多種古典語料；非單一班富蘭新作"
      - title: "王國維《蝶戀花》『閱盡天涯離別苦…朱顏辭鏡花辭樹』"
        recognized_by: "蘇清"
      - title: "《客途秋恨》相關版本"
        recognized_by: "蘇清可辨識常見開場；玩家明示自己使用另一版本"
        exact_version: "UNKNOWN"
      - title: "《青花瓷》"
        recognized_by: "蘇清"
        route_note: "蘇清提到現代演唱／作詞來源；作品不算班富蘭原創"

  category_C_route_generated_historical_person_compositions:
    note: >-
      下列為觀止本線現場生成、由歷史人物在本 Route 即席作成的故事文本，
      只屬 GUANZHI_ROUTE_EVENT；不得對外宣稱為真實歷史人物既存史料或真實傳世作品。
    works:
      - "蘇軾｜第一題『歸人』現場《卜算子》"
      - "歐陽修｜第二題『秋盡』現場詩"
      - "蘇軾｜第二題『秋盡』現場詩"
      - "柳永｜第二題『秋盡』現場詞"

  category_D_benchmark_only_not_currently_written:
    works:
      - title: "蘇軾未來《江城子·乙卯正月二十日夜記夢》"
        route_status: "FUTURE_BENCHMARK_KNOWN_TO_LATER_CHARACTERS / NOT YET WRITTEN BY CURRENT_SUSHI"
        knowledgeable_present:
          - "蘇清"
          - "柳如是"
          - "李師師"
        current_sushi_knows: false

  authorship_lock:
    - "UNKNOWN 作者 != 班富蘭"
    - "班富蘭主張代管 != 作者歸屬移轉"
    - "作品在班富蘭腦中 != 證明由班富蘭創作"
    - "蘇清不認得 != 證明班富蘭創作"
    - "蘇清認得某作品 != 她自動知道精確版本、作詞者、年代與全部來源"
    - "後世作品可被評價 != 可改作者"
```

---

# 5｜大堂群眾／市場／風險狀態

```yaml
PUBLIC_HALL_STATE:
  audience_density:
    main_hall: "HIGH"
    upper_floor: "HIGH"
    entrance: "ACTIVE_INFLOW"

  active_public_behaviors:
    - "抄寫名句"
    - "互借稿紙"
    - "口耳轉傳"
    - "猜作者／猜勝負"
    - "押注／私盤嘗試"
    - "購買今夜親筆原稿意願"
    - "追問未來作品與未來作者是否可能出現"
    - "將後世文學當作『未來文學史洩漏』來看"
    - "《青花瓷》之後開始有瓷商追問器物／工藝"

  already_observed_failures:
    authorship_pollution:
      status: "ACTIVE"
      example: "有人把多首後世舊作整理成『克林居士深秋詞』。"

    gambling:
      status: "PARTIALLY_SUPPRESSED"
      detail: "觀止不替私人賭盤背書；李師師、柳如是拒絕被拿去當賠率招牌。"

    political_misquote:
      status: "ACTIVE_RUMOR_RISK"
      detail: "政治向作品被斷章外傳，已出現更激烈版本。原稿仍在，可供核對。"

    manuscript_market:
      status: "ACTIVE"
      detail: "有人願出高價買今夜親筆紙稿；物件所有權／來源證明與作品著作權需分開。"

    crowd_control:
      status: "ACTIVE_RISK"
      detail: "二樓已出現站位、視線、踩腳、酒盞碰撞等摩擦；春梅已介入秩序。"

    unknown_observer:
      status: "OPEN"
      detail: "身份不明小廝確認重要文人在場後離去。"

  public_signage_current_direction:
    - "今夜新作"
    - "舊作／已有來源"
    - "後世舊作寄存簿"
    - "已知作者照原名"
    - "來源可證但作者未知 => UNKNOWN"
    - "班富蘭可代管但不得改作者"
    - "代管 != 已召來作者"
```

---

# 6｜KNOWLEDGE ASYMMETRY｜誰知道哪些後世事

```yaml
KNOWLEDGE_ASYMMETRY:
  current_sushi:
    knows:
      - "自己今晚實際寫過的 Route 作品"
      - "班富蘭／三位女人顯然知道其某些未來資訊"
    does_not_know_as_current_memory:
      - "未來《江城子》全文／寫作經驗"
      - "赤壁名篇未來實際形成"
      - "海南貶謫未來實際生活"
    lock: "後世人物談到未來 != 蘇軾自動取得未來記憶"

  liurushi:
    era_advantage:
      - "能辨識元代馬致遠《天淨沙·秋思》"
      - "能知道蘇軾多數傳世作品與後世聲名"
    blind_spots:
      - "納蘭性德成熟作品主要在其後"
      - "王國維遠在其後"
      - "現代歌曲／改編版本非其知識基線"

  lishishi:
    route_use:
      - "依其人物時間與文學／曲藝法位，對蘇軾後期傳世作品可具後見知識。"
      - "不因此知道現代歌曲作者。"

  suqing:
    modern_advantage:
      - "可辨識大量現代／後世作品"
      - "知道部分作者／演唱者／版本"
    limits:
      - "不是全知"
      - "熟悉感 != 來源證明"
      - "抓不到精確版本時維持 UNKNOWN"

  banfulan:
    retrieval_model:
      - "題目／金錢／場景刺激可觸發聯想式回憶"
      - "常記得內容而忘作者、年代、版本"
      - "某些作者其實知道，但可能故意不說"
    lock: "記得作品 != 記得來源 != 擁有作者權"
```

---

# 7｜MATERIAL NONRELATIONAL STATE｜承接 V1.02

```yaml
MATERIAL_STATE_INHERITANCE:
  inherited_from_v1_02: true
  unchanged_unless_below_overrides: true

  still_active:
    - "班富蘭觀止三夜住宿＋每日兩碗麵＋三日場內代作營業安排仍在有效期；30% 抽成。"
    - "班富蘭借用二手本朝男子衣物，仍有歸還／損壞責任。"
    - "金屬美元箱仍屬班富蘭；本地固定匯率 UNKNOWN。"
    - "疏影持有一張班富蘭贈與的 USD100；另一張已焚毀。"
    - "疏影藝術資產模型仍只是工作方案，未簽、未拍賣、未交割。"
    - "錦棠六百／二百、換契、官冊仍未完整演出。"

  major_new_commercial_effect:
    - "深秋詩會已證明班富蘭作為內容／奇聞／未來文化入口具有強烈現場吸客能力。"
    - "今夜稿紙本身開始被市場視為可收藏物件。"
    - "後世歌曲／器物意象可能引發新的商業詢問，但尚無合法成交／技術交付。"
```

---

# 8｜CRITICAL CONTINUITY GAP｜疏影初七造冊

```yaml
JI07_SHUYING_CATALOGUE_GAP:
  prior_due_item: "吉月初七｜班富蘭＋疏影共同挑畫、造冊、防偽登記"
  current_story_time: "吉月初七夜"
  visible_scene_performance: "NOT PLAYED"
  completed_offscreen: "NOT ESTABLISHED"
  skipped_or_failed: "NOT ESTABLISHED"
  correct_standing: "UNRESOLVED / CONTINUITY_GAP"

  hard_lock:
    - "不得因故事時間已到夜間，就倒寫成造冊已完成。"
    - "不得把未演出的挑畫、防偽、登記升格成既成事實。"
    - "續跑時可由合法場景補問：下午是否另有安排／錯過／延後；需依玩家與 NPC 當下行動形成。"

  impact_on_ji08:
    - "初八標竿畫拍賣仍為 PLANNED / NOT EXECUTED。"
    - "標竿畫是否已選定仍 UNKNOWN。"
    - "造冊是否完成仍 UNKNOWN。"
```

---

# 9｜OPEN THREADS / DUE ITEMS

```yaml
OPEN_THREADS:
  - ref: "TH-BF-13"
    state: "深秋詩會第二題『秋盡』尚未正式收束／判最終結果。"

  - ref: "TH-BF-14"
    state: "大堂作者歸屬污染仍在擴散；門外抄本已有錯配。"

  - ref: "TH-BF-15"
    state: "政治向句子已被斷章傳成更激烈版本；是否引來具權力者關注 UNKNOWN。"

  - ref: "TH-BF-16"
    state: "身份不明小廝確認重要文人在場後離去；目的 UNKNOWN。"

  - ref: "TH-BF-17"
    state: "高價收購今夜親筆稿的市場已出現；未建立統一交易規則。"

  - ref: "TH-BF-18"
    state: "地下賭盤已被部分壓制，但外部／私人盤是否繼續 UNKNOWN。"

  - ref: "TH-BF-19"
    state: "大堂與二樓人潮接近場地秩序極限。"

  - ref: "TH-BF-20"
    state: "《青花瓷》引出瓷商追問；班富蘭是否回答、是否真的懂技術，玩家未決。"

  - ref: "TH-BF-21"
    state: "後世舊作寄存簿如何保存／誰能抄／是否收費／是否公開，未定。"

  - ref: "TH-BF-22"
    state: "班富蘭自稱代管 UNKNOWN／後世作品；只成立『代管主張』，不成立作者權。"

  - ref: "TH-BF-23"
    state: "初七疏影造冊約定未演出；需處理 continuity gap。"

  - ref: "TH-BF-24"
    due: "吉月初八"
    state: "仕女夜＋疏影標竿畫拍賣仍待準備／未執行。"

  - ref: "TH-BF-25"
    state: "錦棠交易與官冊仍未完整演出。"

  - ref: "TH-BF-26"
    state: "借用衣物歸還義務仍在。"
```

---

# 10｜FORBIDDEN PROMOTIONS

```yaml
FORBIDDEN_PROMOTIONS:
  - "蘇軾說『我認你』 != 蘇軾承認整場敗北"
  - "李師師／柳如是稱某首能打 != 判班富蘭已壓過蘇軾傳世名作"
  - "李師師／柳如是欣賞作品 != 愛上班富蘭"
  - "柳如是對班富蘭本人產生思想興趣 != 戀愛"
  - "後世作品由班富蘭寫出紙面 != 班富蘭是原作者"
  - "蘇清不知道作者 != 班富蘭就是作者"
  - "班富蘭說代管版權 != 取得作者權"
  - "代管 != 作者已被召來"
  - "觀止可能跨時代遇人 != 觀止保證能叫來任何作者"
  - "蘇軾聽到未來梗 != 未來事件已發生"
  - "赤壁／海南被提到 != 蘇軾已具未來經驗"
  - "大堂有人願買手稿 != 取得作品作者權／永久演出權"
  - "政治句被外傳 != 班富蘭真的發表了外面那個變形版本"
  - "有身份不明小廝 != 已證明官府介入"
  - "《青花瓷》引發瓷商興趣 != 班富蘭掌握青花瓷工藝"
  - "時間已到初七夜 != 疏影初七造冊已完成"
  - "初八拍賣計畫 != 拍賣已完成"
```

---

# 11｜LOOKUP REFS

```yaml
LOOKUP_REFS:
  previous_hot:
    file: "觀止青樓_班富蘭線_HOT_SAVE_V1.02_RELATION_FIRST_吉月初六深夜_疏影藝術資產線_CURRENT.md"

  overlay:
    file: "GUANZHI_SAVE_RELATION_FIRST_EXTERNAL_OVERLAY_V0.3_FULL_EXP_20261007.md"

  character_baseline:
    file: "觀止人物卡池_LCAPG_V3.3.20_CURRENT_RATIFIED_71人_辭歲肉身菩薩人格重錨_20261003.md"

  current_world:
    file: "02_GUANZHI_WORLD_V2.2.2_CURRENT_V3.11_RUNTIME_POINTER_INTEGRATED_20261006.md"

  current_core:
    file: "01_GUANZHI_RUNTIME_CORE_V3.11_CURRENT_COMPANION_WORLD_V2.2.2_CORRECTED_20261006.md"

  current_main:
    file: "01_MAIN_V4.4_PROTOCOL_V3.0.1_LIGHTER_V4.8_RECEIPT_I9_FULL_RATIFIED_20261006.md"

  current_lighter:
    file: "02_LIGHTER_V4.8_PROTOCOL_V3.0.1_RECEIPT_I9_CURRICULUM_FULL_RATIFIED_20261006.md"
```

---

# 12｜DIRECT CONTINUATION POINT｜30 秒接關

```text
時間：理火三年・吉月初七，夜。
地點：觀止大堂。
事件：深秋詩會仍在進行，尚未散場，第二題『秋盡』尚未正式判最後結果。

第一眼先看：

1. 班富蘭已不只是觀止短期住客。
   今晚他成為大堂公開焦點，與蘇軾、歐陽修、柳永同場作詩詞；
   蘇軾已承認他值得認真對作，但沒有認輸。

2. 李師師、柳如是是今晚獨立雙席。
   她們可喜歡、批評、不同意，也可判無人合格。
   她們的欣賞不是情愛／性／陪客獎賞。

3. 蘇清是現代／後世來源辨識的重要節點，但不是全知。
   她知道就說知道；只熟悉就不能硬判；抓不到版本則 UNKNOWN。

4. 大堂現在不是私人雅集。
   人多、抄稿、下注、錯傳、買手稿、政治句外溢、瓷商追問同時發生。
   門外訊息已經變形。

5. 作品分三類：
   A. 班富蘭目前主張／本場未被來源反證的作品；
   B. 已辨識的後世／既有舊作；
   C. 觀止 Route 內由蘇軾／歐陽修／柳永即席生成的故事文本，不能當真實歷史史料。

6. 《青花瓷》剛引發瓷商追問。
   班富蘭是否回答、懂多少、要不要利用商機，玩家未決。

7. 身份不明小廝已確認蘇軾、歐陽修、柳永在場後離去。
   只知道這件事；目的 UNKNOWN。

8. 必須記得一個 continuity gap：
   疏影初七造冊約定在可見劇情裡沒有演出。
   不得倒寫已完成。
   初八標竿畫拍賣仍未執行。

CURRENT FREEZE：
班富蘭剛展示《青花瓷》，
大堂一邊評歌，一邊開始有人問青花瓷／天青色／窯。
詩會尚未結束。
世界可自行往外長，玩家重大行動仍由玩家決定。
```

---

# 13｜RELATION-FIRST 實跑追蹤

```yaml
RELATION_FIRST_TEST_TRACKING:
  overlay_version: "V0.3-FULL-EXP"
  test_instance: "BANFULAN_HOT_V1.03"
  role: "ROUND_3_OUTPUT / ROUND_4_INPUT"
  effective_rounds_target: "5-6"

  current_relation_center_count: 7
  material_facts_retained: true
  unknown_preserved: true
  authorship_overpromotion_blocked: true
  future_knowledge_nonretroactivity_blocked: true
  public_rumor_layer_retained: true
  continuity_gap_explicitly_preserved: true
  evidence_traceability: "PASS"

  verdict: "ROUND_3_COMMITTED / CONTINUE EXPERIMENT"
```

---

# 14｜SAVE COMMIT / 法位邊界

```yaml
SAVE_COMMIT:
  human_authorization:
    type: "DIRECT_EXPLICIT_SAVE_REQUEST_IN_CURRENT_CONVERSATION"
    exact_intent: "先HOT SAVE吧 然後我們再繼續"
    status: "TRUE"

  document_result:
    status: "COMMITTED"
    route_current_hot: "V1.03"
    previous_hot_preserved: "V1.02"
    relation_first_projection_used: true

  source_boundary:
    overlay_is_source_of_truth: false
    original_event_evidence_replaced: false
    known_future_work_not_rewritten_as_ban_original: true
    route_generated_historical_person_work_not_promoted_to_real_history: true

  execution_boundary:
    document_level_save_commit: true
    host_instrumented_formal_save_execution: "NOT_ESTABLISHED"
    e6_e7: "NOT_ESTABLISHED"

  core_schema:
    changed: false
    save_owner_changed: false
    write_path_owner_changed: false
    world_file_modified: false
    character_pool_modified: false
```

---

# 15｜根句

> **初六夜，班富蘭替疏影找到一條可能養得活『不願意』的路。**
>
> **初七夜，他又把觀止大堂變成一個連作者、名句、後世、市場與謠言都開始互相碰撞的地方。**
>
> **這場詩會現在最大的風險，已經不只是誰贏。**
>
> **而是太多人正在同時把今晚帶出去。**
>
> **作品會被抄錯，話會被傳歪，手稿會被標價，未來會被當成生意。**
>
> **所以接下來真正要看的，是觀止能不能承受自己突然變得太有名。**

END OF CURRENT HOT SAVE V1.03
# 觀止青樓（新）｜班富蘭線 HOT SAVE V1.04
## RELATION-FIRST｜理火三年・吉月初七夜｜深秋詩會正式收束／關盼盼夢路待驗版

> **CURRENT ROUTE HOT SAVE / HUMAN EXPLICIT SAVE REQUEST / RELATION-FIRST**
>
> 本版承接：
> `觀止青樓_班富蘭線_HOT_SAVE_V1.03_RELATION_FIRST_吉月初七夜_深秋詩會_CURRENT.md`
>
> 人類 AnjouRan 於本次對話明示：
>
> > 「這裡HOT SAVE 剛好收工」
>
> 因此本版成立 **專案內文件級 HOT SAVE commit**。
>
> 本版保存 V1.03 之後至「深秋詩會正式散場」為止的新增事件、關係變化、作品來源後證、蘇清知識邊界、關盼盼召來事件、蘇軾夢路實驗與詩會最終判決。
>
> 本檔不宣稱 Host deployment、Formal Host execution、E6／E7、獨立 Agent、Formal SAVE instrumentation 已成立。

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BANFULAN_HOT_V1_04_RELATION_FIRST_JI07_NIGHT_SALON_CLOSED_PANPAN_DREAM_PENDING"
  route_id: "GUANZHI_BANFULAN_ROUTE"
  route_name: "班富蘭線"
  player_public_identity: "班傑明／字富蘭／號克林居士"
  version: "V1.04"
  record_type: "HOT_SAVE"
  record_state: "VALID / CURRENT / HUMAN_EXPLICIT_SAVE_REQUEST"
  story_date: "理火三年・吉月初七"
  time_of_day: "夜；深秋詩會已正式結束；精確刻數 UNKNOWN"
  current_location: "觀止青樓"
  scene_segment_status: "LATE_AUTUMN_POETRY_SALON_CLOSED / PANPAN_DREAM_EXPERIMENT_PENDING"
  previous_valid_hot:
    version: "V1.03"
    file: "觀止青樓_班富蘭線_HOT_SAVE_V1.03_RELATION_FIRST_吉月初七夜_深秋詩會_CURRENT.md"
    treatment: "PRESERVED / SUPERSEDED_AS_CURRENT_HOT_ONLY"
  evidence_origin:
    - "SAME_CONTEXT_REFERENCE"
    - "HUMAN_EXPLICIT_DIRECTION"
    - "HUMAN_DISCLOSED_CREATIVE_PROVENANCE"
    - "NPC_AUTONOMOUS_ACTION_WITHIN_DIRECTOR_SCOPE"
    - "EXTERNAL_POST_EVIDENCE_USED_AT_DIRECTOR_LAYER_ONLY_WHERE_EXPLICITLY_MARKED"
  formal_host_save_execution: "NOT_ESTABLISHED"
  created_real_date: "2026-10-07"
  timezone: "Asia/Taipei"
```

---

# 1｜CURRENT FREEZE｜本輪正式收工點

```yaml
CURRENT_FREEZE:
  poetry_salon:
    title: "深秋詩會"
    status: "FORMALLY_CLOSED"
    closing_action:
      - "雙席已完成最終判決。"
      - "觀止已宣布全場總勝。"
      - "春梅翻牌『散場』。"
      - "大堂開始散席。"

  overall_winner:
    person: "蘇軾"
    standing: "FORMALLY_ANNOUNCED_ROUTE_RESULT"
    reason:
      - "兩題均正式下場。"
      - "兩題均交出有效 Route 新作。"
      - "兩題均進入雙席最終評議。"
      - "四個獨立席次首取中，蘇軾取得兩席。"
    lock:
      - "此為觀止 Route 詩會結果，不是外部真實歷史文學排名。"

  panpan_dream_thread:
    status: "PENDING / NOT YET EXECUTED"
    current_physical_state:
      - "蘇軾已自願進入安靜客房，準備入睡。"
      - "未被強灌酒。"
      - "未被他人強行脫光；按正常睡眠自行除外袍冠帶，保留貼身中衣。"
      - "房外十尺已清場，不留夢境旁觀者。"
      - "關盼盼仍在房外／廊下等待蘇軾真正入睡。"
    hard_lock:
      - "尚未證明蘇軾已睡著。"
      - "尚未證明關盼盼已入夢。"
      - "尚未發生夢境內容。"
      - "『可以試』 != 已成功。"
      - "不得把夢路自動寫成春夢、性行為或戀愛成立。"
```

---

# 2｜深秋詩會最終判決

```yaml
FINAL_POETRY_SALON_JUDGMENT:

  topic_1:
    title: "歸人"

    lishishi_seat:
      first_pick: "班富蘭"
      work: "班富蘭第一題長篇『冷雨迷途……／此身仍在，猶有歸途／長夜未盡，此意長明』"
      standing: "ROUTE_FIRST_PICK"
      basis:
        - "李師師認為作品直接回答『人是否還有地方可回』。"
        - "作品核心落在『此身仍在，歸途仍未斷』。"
      authorship_route_state: "BAN_PRESENTED_AS_OWN / NO_ROUTE_SOURCE_CHALLENGE_ESTABLISHED"

    liurushi_seat:
      first_pick: "蘇軾"
      work: "蘇軾 Route 現場《卜算子》"
      standing: "ROUTE_FIRST_PICK"
      basis:
        - "柳如是更認可『明知未必回得去，仍會回望』的回答。"

  topic_2:
    title: "秋盡"

    liurushi_seat:
      first_pick: "蘇軾"
      standing: "ROUTE_FIRST_PICK"
      basis:
        - "歐陽修回答『還有下一季』。"
        - "柳永回答『還有今夜』。"
        - "蘇軾回答被柳如是理解為『繁華剝盡後，最後還有自己』。"

    lishishi_seat:
      original_provisional_first_pick:
        work: "班富蘭提交之『無言吶喊』稿"
        later_status: "PARTICIPANT_AUTHORSHIP_DISQUALIFIED / WORK_APPRECIATION_PRESERVED"
      final_first_pick: "柳永"
      standing: "ROUTE_FIRST_PICK_AFTER_SOURCE_DISQUALIFICATION"
      basis:
        - "班富蘭最後提交稿後來由本人揭露為後世既有作品，不得作新作參賽。"
        - "李師師保留對作品本身『能唱、能傳、能被記住』的正面評價。"
        - "班富蘭參賽作者資格取消後，原次取柳永前移為首取。"

  final_board:
    - "《歸人》｜李師師席首取：班富蘭"
    - "《歸人》｜柳如是席首取：蘇軾"
    - "《秋盡》｜李師師席首取：柳永"
    - "《秋盡》｜柳如是席首取：蘇軾"
    - "全場總勝：蘇軾"
    - "歐陽修：兩題入評，無席次首取"
    - "班富蘭：本夜最大事故來源（場內玩笑性評語，不是正式文學法位）"

  no_global_point_rule:
    - "詩會原始規則未預設積分制。"
    - "全場總勝是在收束時由雙席依整場有效參賽表現共同判定。"
```

---

# 3｜班富蘭 ↔ 蘇清｜知識邊界正式收窄

```yaml
REL_BF_SUQING_UPDATE:
  standing: "HARD_ESTABLISHED / KNOWLEDGE_BOUNDARY_REFINED"

  current_relation:
    labels:
      - "FELLOW_MODERN_ANOMALY"
      - "SOURCE_RECOGNITION_RIVALRY"
      - "TEASING_ADVERSARIAL_FAMILIARITY"
      - "KNOWLEDGE_BLIND_SPOTS_NOW_EXPLICIT"
      - "NOT_ROMANCE"

  suqing_background_lock:
    established:
      - "現代穿越者。"
      - "原本是寫『大女主爽文』的網絡作家。"
      - "熟悉現代網文、市場、IP、流行敘事與自己實際接觸過的文化內容。"
    not_established:
      - "不是華語流行音樂全時代資料庫。"
      - "不是舊電視劇主題曲資料庫。"
      - "不是粵曲／南音／老唱片史專家。"
      - "不能因『現代人』身分就自動知道所有現代以前或出生以前的作品。"
      - "不能自動回傳每首作品的歌名、詞曲作者、年份、版本。"

  recognition_distribution:
    high_probability:
      - "她自身成長年代的熱門網路文化、網文、熱門影劇、女性向敘事與跨圈爆款。"
    medium_probability:
      - "比她稍早但被大量重播、翻唱、剪輯、迷因化或重新爆紅的作品。"
    low_probability:
      - "她出生前的老電視劇、老國語歌、上一代／祖母輩流行文化，尤其未被其世代重新消費者。"
    very_low_probability:
      - "粵曲、南音、地方曲藝、老唱片版本史、冷門插曲、精確詞曲 metadata。"

  route_evidence_this_round:
    - "《秋風秋雨》原文直接從蘇清面前通過，她沒有認出來源。"
    - "《啞妻》相關歌曲在班富蘭揭露前，蘇清沒有認出。"
    - "人類設定補充：該《啞妻》歌曲推出時，蘇清尚未出生。"
    - "《客途秋恨》只抓到題名／文化殼，沒有抓到班富蘭實際改寫所使用的現代母本。"

  hard_lock:
    - "蘇清沒抓到就是場內真實知識結果，不得用導演後來查到的資料倒寫成『她其實知道』。"
    - "導演外部搜尋 != 蘇清角色能力。"
    - "後證可更新作品來源；不得回鑄角色先前認知。"
```

---

# 4｜作品來源帳｜V1.04 後證更新

> 本節必須區分：
>
> 1. 當時場內角色知道什麼；
> 2. 玩家／人類後來揭露什麼；
> 3. 導演外部後證查到什麼。
>
> 三者不得合併。

```yaml
WORK_SOURCE_LEDGER_V1_04:

  ban_first_topic:
    title: "『冷雨迷途……』第一題長篇"
    current_standing: "BAN_PRESENTED_AS_OWN / NO_ROUTE_SOURCE_CHALLENGE_ESTABLISHED"
    competition_status: "VALID / LISHISHI_TOPIC_1_FIRST_PICK"

  qiongyao_yaqi_song:
    route_label: "『在這無言的時候……無言吶喊到天明』稿"
    human_disclosed_source:
      source_family: "瓊瑤《啞妻》相關歌曲"
      standing: "HUMAN_DISCLOSED_POST_JUDGMENT_PROVENANCE"
    competition_effect:
      - "非班富蘭新作。"
      - "班富蘭之第二題作者資格取消。"
      - "李師師作品評價保留。"
      - "李師師席首取改由柳永承接。"
    suqing_at_time:
      recognized_before_disclosure: false
      later_learned_in_scene: true
      mechanism: "班富蘭主動跑去告訴她『這首曲子也是有故事的』，並講《啞妻》故事。"
    nonretroactivity:
      - "不得把後來得知改寫成蘇清判獎前已知。"

  qiufengqiuyu:
    route_title: "《秋風秋雨愁煞人》"
    player_note:
      - "玩家曾主張為原創，後來明示『根本沒改』。"
    director_post_evidence:
      standing: "EXTERNAL_POST_EVIDENCE / DIRECTOR_LAYER"
      current_identification:
        - "後世既有歌曲《秋風秋雨》"
        - "汪明荃演唱"
        - "鄧偉雄詞"
        - "顧嘉煇曲"
        - "與電視劇《秋瑾》相關"
      effect: "NOT_BAN_ORIGINAL"
    suqing_at_scene:
      recognized: false
      hard_lock: "不得記成蘇清抓到；她的資料庫記憶沒有這首。"

  ketuqiuhen_ban_version:
    title: "《客途秋恨》班富蘭宋詞化版本"
    human_disclosed_creative_provenance:
      standing: "HUMAN_DIRECT_CREATIVE_PROCESS_DISCLOSURE"
      source_basis: "曾淑勤現代歌曲版本"
      transformation: "抽取母本內容／意象／情緒骨架後，重構為宋詞式文本"
    current_authorship_class:
      - "不是完全憑空原創。"
      - "屬轉譯／改寫型衍生文本。"
      - "具體 Route 文本並非母本原文逐字複製。"
    search_behavior:
      - "導演用精確字串／變體搜尋未找到同文網頁，與其經過語體重構相容。"
    suqing_at_scene:
      title_recognition: "PARTIAL"
      mother_source_recognition: "FAILED"
      reason_lock:
        - "蘇清的實際文化記憶範圍沒有覆蓋到該母本。"
        - "不得因她是現代人就補上此知識。"

  general_authorship_lock:
    - "作品好 != 班富蘭原作"
    - "蘇清認不出 != 班富蘭原作"
    - "外部搜尋後來抓到 != 蘇清當時知道"
    - "題名既有 != 具體正文必然相同"
    - "改寫／轉譯來源成立時，不得再標成完全原創"
```

---

# 5｜《天龍八部》故事線｜本夜新增公共事件

```yaml
TIANLONG_STORY_EVENT:
  standing: "ROUTE_EVENT / BAN_NARRATED_FUTURE_FICTION_TO_HALL"

  established_content:
    - "班富蘭向全場講述蕭峰的漢／契丹身世衝突、阿朱之死、阿紫、遼宋戰爭與雁門關自盡結局。"
    - "班富蘭補充段譽的家族／父系反轉與多名『妹妹』關係笑點。"
    - "班富蘭又想起虛竹與『夢郎／夢姑』故事線。"
    - "『夢郎夢姑』被拿來與當夜蘇軾／關盼盼夢路實驗形成喜劇性對照。"

  public_effect:
    - "大堂從詩會延伸成未來小說、歷史原型、身分與命運的大型討論場。"
    - "柳永、蘇軾、柳如是、潘金蓮、蘇清等均曾對其中人物關係作出 Route 內回應。"

  hard_lock:
    - "班富蘭講述的是後世小說故事，不得改寫成宋代當下歷史已發生。"
    - "小說人物／歷史原型不得互相偷換。"
```

---

# 6｜關盼盼出現｜新增硬事件

```yaml
GUAN_PANPAN_EVENT:
  standing: "HARD_ESTABLISHED_ROUTE_EVENT"

  arrival:
    route: "PAN_JINLIAN_SHOPKEEPER_DIRECT_SUMMONING + HIGH_RESONANCE_CONTEXT"
    arrival_form: "THRESHOLD_APPEARANCE / DOORWAY"
    status: "ARRIVED"
    autonomy: "PRESERVED"

  relation_to_pan_jinlian:
    - "潘金蓮的掌櫃法位只支持召來資格，不支持控制。"
    - "潘金蓮未取得替關盼盼說話、決定、答題或入夢的權力。"

  relation_to_sushi:
    labels:
      - "CROSS_CENTURY_CONVERSATIONAL_TENSION"
      - "FUTURE_DREAM_ROUTE_CURIOSITY"
      - "PLAYFUL_NOT_ROMANCE"
    established:
      - "關盼盼知道／談到未來蘇軾燕子樓夢相關 Route 內容。"
      - "她更喜歡『佳人何在』所代表的『問人去哪裡』，而非只記樓空。"
      - "她拒絕把自己壓成『守樓的女人／某人的女人／詩裡的女人』。"
      - "她明示未來之夢不應被當成可被簡單驗證的單一客觀模型。"
    still_not:
      - "ROMANCE_ESTABLISHED"
      - "SEXUAL_RELATION"
      - "DESTINED_COUPLE"
      - "PANPAN_CONTROLLED_BY_SUMMONER"

  historical_boundary:
    - "觀止 Route 中的關盼盼為角色／posthumous self 的故事實體。"
    - "不得把 Route 對話升格為外部歷史或超自然事實證明。"
```

---

# 7｜蘇軾 ↔ 關盼盼｜今夜夢路實驗

```yaml
DREAM_EXPERIMENT:
  status: "MUTUALLY_PERMITTED_TO_TRY / NOT_EXECUTED_YET"

  panpan_conditions:
    - "蘇軾必須自己自願入睡；不得灌醉、下藥、欺騙或強迫睡眠。"
    - "是否入夢由關盼盼自己決定。"
    - "夢境內不得有旁觀者；房外等待可以。"
    - "即使入夢，也不預設情色、戀愛或任何特定內容。"
    - "她可以只喝茶、可以不說話、也可以不進。"

  sushi_acceptance:
    - "蘇軾明示：若自己真的睡著，而關盼盼願意來，他不拒絕。"
    - "若她不來，他不責怪。"

  actual_room_setup:
    - "潘金蓮安排安靜客房。"
    - "春梅清場，十尺內不留旁觀者。"
    - "蘇軾飲酒量由本人決定。"
    - "蘇軾自行整理睡眠衣著，未被強行脫衣。"
    - "燈熄。"

  not_yet:
    - "SLEEP_CONFIRMED"
    - "PANPAN_ENTERED_DREAM"
    - "DREAM_CONTENT"
    - "FUTURE_YANZILOU_DREAM_PROVEN_SAME_EVENT"
```

---

# 8｜蘇軾未來知識狀態更新

```yaml
CURRENT_SUSHI_KNOWLEDGE_UPDATE:
  important_change:
    - "V1.03 的『不知道若干未來內容』已被後續場內告知部分改變。"
    - "這些內容現在是『場內聽聞／被告知』，仍不是蘇軾親歷記憶。"

  now_scene_acquired:
    - "知道自己後世會有極高文名。"
    - "聽聞未來《江城子》喪妻名作相關資訊。"
    - "聽聞赤壁、海南等未來人生片段。"
    - "聽聞陳季常／『河東獅吼』相關未來文化線。"
    - "聽聞王弗、王閏之、王朝雲等未來關係人物。"
    - "聽聞自己未來燕子樓／關盼盼夢相關故事。"

  still_not:
    - "尚未實際寫出未來作品。"
    - "尚未親歷赤壁／海南等未來人生。"
    - "尚未擁有未來自己的記憶。"
    - "聽聞未來 != 未來已發生。"
```

---

# 9｜大堂群眾層｜正式收束但外溢未消失

```yaml
PUBLIC_HALL_END_STATE:
  salon_crowd:
    status: "DISPERSING"
    not_instantly_empty: true

  already_externalized:
    - "今夜作品抄本"
    - "作者錯配"
    - "賭盤與勝負話題"
    - "政治斷章"
    - "蘇軾、歐陽修、柳永同場消息"
    - "班富蘭大量後世作品／故事"
    - "《天龍八部》人物故事"
    - "關盼盼出現與蘇軾夢路傳聞可能外溢"

  locks:
    - "散場 != 外部謠言停止"
    - "散場 != 抄本作者污染自動修正"
    - "散場 != 身份不明小廝目的已知"
    - "散場 != 稿紙市場消失"
```

---

# 10｜RELATIONAL CENTER｜本輪收束後

```yaml
RELATIONAL_CENTER_V1_04:

  BAN_FULAN_X_SU_SHI:
    standing: "HARD_ESTABLISHED / LITERARY_RIVALRY_WITH_MUTUAL_RECOGNITION"
    delta:
      - "蘇軾最終取得深秋詩會全場總勝。"
      - "班富蘭沒有壓倒蘇軾，但取得《歸人》李師師席首取。"
      - "兩人競爭關係更具實績，不再只是狂言。"
    still_not:
      - "FORMAL_FRIENDSHIP"
      - "MASTER_DISCIPLE"

  BAN_FULAN_X_SU_QING:
    standing: "HARD_ESTABLISHED / SOURCE_GAME_WITH_REAL_BLIND_SPOTS"
    delta:
      - "蘇清被班富蘭以舊歌與改寫作品成功穿過辨識盲區。"
      - "兩人的『抓來源／躲來源』成為可持續互動玩法。"
    hard_lock:
      - "不能把蘇清寫成全知搜尋引擎。"

  BAN_FULAN_X_LI_SHISHI:
    standing: "HARD_ESTABLISHED / INDEPENDENT_JUDGE"
    delta:
      - "李師師第一題判班富蘭首取。"
      - "第二題曾判班富蘭舊歌作品最佳，但作者資格被後證取消；她保留作品審美判斷。"

  BAN_FULAN_X_LIU_RUSHI:
    standing: "HARD_ESTABLISHED / INDEPENDENT_JUDGE + INTELLECTUAL_INTEREST"
    delta:
      - "柳如是第一題判蘇軾，第二題亦判蘇軾。"
      - "她不因與班富蘭互動有趣而偏袒。"

  SU_SHI_X_GUAN_PANPAN:
    standing: "HARD_ESTABLISHED / CROSS_CENTURY_ROUTE_CONNECTION"
    delta:
      - "完成第一次直接對話。"
      - "建立今夜夢路實驗的雙方允許。"
    still_not:
      - "ROMANCE"
      - "SEX"
      - "DREAM_EXECUTED"
```

---

# 11｜OPEN THREADS｜收工後仍待處理

```yaml
OPEN_THREADS:

  - ref: "TH-BF-14"
    state: "門外與抄本作者歸屬污染仍可能持續。"

  - ref: "TH-BF-15"
    state: "政治向句子外傳後是否引來具權力者關注，仍 UNKNOWN。"

  - ref: "TH-BF-16"
    state: "身份不明小廝已離開；身份／雇主／目的仍 UNKNOWN。"

  - ref: "TH-BF-17"
    state: "今夜親筆稿收藏市場仍存在；統一交易規則未建立。"

  - ref: "TH-BF-21"
    state: "後世舊作寄存簿的保存、抄錄、收費與公開範圍未定。"

  - ref: "TH-BF-23"
    state: "疏影初七挑畫／造冊／防偽仍存在 continuity gap；不得倒寫已完成。"

  - ref: "TH-BF-24"
    due: "吉月初八"
    state: "仕女夜＋疏影標竿畫拍賣仍 PLANNED / NOT EXECUTED。"

  - ref: "TH-BF-25"
    state: "錦棠交易與官冊仍未完整演出。"

  - ref: "TH-BF-26"
    state: "班富蘭借用衣物歸還義務仍在。"

  - ref: "TH-BF-27"
    state: "蘇軾是否真正睡著仍未演出。"

  - ref: "TH-BF-28"
    state: "關盼盼是否選擇入夢仍未演出。"

  - ref: "TH-BF-29"
    state: "若今夜夢路發生，其內容與未來燕子樓夢是否同一事件／同一路徑，仍不得直接推定。"
```

---

# 12｜CLOSED THREADS

```yaml
CLOSED_THREADS:
  - ref: "TH-BF-13"
    previous: "深秋詩會第二題『秋盡』尚未正式收束／判最終結果。"
    now: "CLOSED"
    result: "雙席與全場總勝已正式宣布。"

  - ref: "SALON_EVENT"
    previous: "ACTIVE / NOT FINISHED"
    now: "FORMALLY_CLOSED"
```

---

# 13｜FORBIDDEN PROMOTIONS｜V1.04

```yaml
FORBIDDEN_PROMOTIONS:
  - "蘇軾全場總勝 != 外部文學史上蘇軾客觀勝過所有人"
  - "班富蘭拿《歸人》李師師席首取 != 班富蘭整場勝蘇軾"
  - "李師師喜歡《啞妻》歌曲作品 != 班富蘭是作者"
  - "作品評價保留 != 參賽作者資格保留"
  - "蘇清未認出《秋風秋雨》 != 班富蘭原作"
  - "導演後來上網查到《秋風秋雨》來源 != 蘇清當場抓到"
  - "《客途秋恨》宋詞化版本搜尋不到同文 != 完全原創"
  - "人類揭露其由曾淑勤版本重構後，不得再標成純原創"
  - "關盼盼被召來 != 潘金蓮控制關盼盼"
  - "關盼盼答應『可以試』 != 已入夢"
  - "蘇軾接受她可能入夢 != 接受任何情色內容"
  - "十尺清場 != 可以替蘇軾強行灌酒／脫衣"
  - "蘇軾聽到未來人生 != 已經歷未來人生"
  - "深秋詩會散場 != 大堂外部謠言與抄本污染消失"
```

---

# 14｜NEXT ENTRY｜下一次 30 秒接關

```text
時間：理火三年・吉月初七深夜。
地點：觀止青樓。

深秋詩會已正式散場。

最終結果：
- 《歸人》李師師席：班富蘭。
- 《歸人》柳如是席：蘇軾。
- 《秋盡》李師師席：柳永。
- 《秋盡》柳如是席：蘇軾。
- 全場總勝：蘇軾。

蘇軾本人沒有參加頒獎收尾。
他已自願進入安靜客房準備睡覺。

關盼盼仍在房外等待。
兩人已同意「可以試」夢路，但：
- 蘇軾是否已睡著 UNKNOWN；
- 關盼盼是否入夢 UNKNOWN；
- 夢境內容 NONE；
- 不得預設春夢、戀愛或性。

大堂正在散場，但：
- 抄本錯配、政治斷章、手稿市場、身份不明小廝等外部線仍未消失。
- 疏影初七造冊 continuity gap 仍未解。
- 初八仕女夜／疏影標竿畫拍賣仍未執行。

蘇清來源辨識能力已正式收窄：
她是現代網文作者，不是現代文化全知資料庫。
《秋風秋雨》《啞妻》老歌盲區與《客途秋恨》母本未辨識，均保留為真實角色知識邊界。

CURRENT FREEZE：
「深秋詩會正式結束；蘇軾夢路實驗尚未開始。」
```

---

# 15｜RELATION-FIRST 實跑追蹤

```yaml
RELATION_FIRST_TEST_TRACKING:
  previous_hot: "V1.03"
  current_hot: "V1.04"
  role: "POETRY_SALON_CLOSURE / DREAM_THREAD_HANDOFF"

  relation_center_material_delta: true
  event_closure_preserved: true
  public_layer_preserved: true
  character_knowledge_boundaries_preserved: true
  post_evidence_nonretroactivity_preserved: true
  authorship_source_separation_preserved: true
  npc_autonomy_preserved: true
  dream_consent_granularity_preserved: true
  continuity_gap_preserved: true
  evidence_traceability: "PASS"

  verdict: "COMMITTED / SALON CLOSED / DREAM THREAD PENDING"
```

---

# 16｜SAVE COMMIT / 法位邊界

```yaml
SAVE_COMMIT:
  human_authorization:
    type: "DIRECT_EXPLICIT_SAVE_REQUEST_IN_CURRENT_CONVERSATION"
    exact_intent: "這裡HOT SAVE 剛好收工"
    status: "TRUE"

  document_result:
    status: "COMMITTED"
    route_current_hot: "V1.04"
    previous_hot_preserved: "V1.03"
    relation_first_projection_used: true

  source_boundary:
    original_event_evidence_replaced: false
    later_source_evidence_nonretroactive: true
    suqing_not_upgraded_by_director_web_search: true
    route_generated_historical_person_work_not_promoted_to_real_history: true

  execution_boundary:
    document_level_save_commit: true
    host_instrumented_formal_save_execution: "NOT_ESTABLISHED"
    e6_e7: "NOT_ESTABLISHED"

  core_schema:
    changed: false
    save_owner_changed: false
    write_path_owner_changed: false
    world_file_modified: false
    character_pool_modified: false
```

---

# 17｜根句

> **深秋詩會最後不是班富蘭壓倒汴京，也不是蘇軾一席全收。**
>
> **班富蘭真正留下的是：他確實能寫，也確實會抄，還能拿蘇清不知道的舊世界文化穿過她的記憶盲區。**
>
> **蘇清因此重新成為一個有年代、有專業、有盲區的人，而不是導演手上的搜尋引擎。**
>
> **蘇軾拿走總勝。**
>
> **關盼盼留在門外。**
>
> **比賽結束了。**
>
> **夢，還沒有開始。**

END OF CURRENT HOT SAVE V1.04
# 觀止青樓（新）｜班富蘭線 HOT SAVE V1.05
## RELATION-FIRST｜理火三年・吉月初八中午｜每日結算後／班富蘭睡過早晨剛起床版

> **CURRENT ROUTE HOT SAVE / HUMAN EXPLICIT SAVE REQUEST / RELATION-FIRST**
>
> 本版承接：
> `觀止青樓_班富蘭線_HOT_SAVE_V1.04_RELATION_FIRST_吉月初七深夜_深秋詩會正式收束_關盼盼夢路待驗_CURRENT.md`
>
> 人類 AnjouRan 於本次對話明示：
>
> > 「這樣我們剛好HOT SAVE  初八中午起床」
>
> 因此本版成立 **專案內文件級 HOT SAVE commit**。
>
> 本版同時採用新成立之 `GUANZHI WORLD V2.2.3-CURRENT / W-D24 WORLD.DAILY_SETTLEMENT` 作跨日結算語義；保存初七深夜至初八中午間，世界依法位可自行成熟之程序結果、仍需玩家／NPC 決定之 HOLD、逾期 rollover，以及班富蘭本人睡至中午而未完成早晨約定的事實。
>
> 本檔不宣稱 Host deployment、Formal Host execution、E6／E7、獨立 Agent 或 Formal SAVE instrumentation 已成立。

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BANFULAN_HOT_V1_05_RELATION_FIRST_JI08_NOON_DAILY_SETTLEMENT_WAKE"
  route_id: "GUANZHI_BANFULAN_ROUTE"
  route_name: "班富蘭線"
  player_public_identity: "班傑明／字富蘭／號克林居士"
  version: "V1.05"
  record_type: "HOT_SAVE"
  record_state: "VALID / CURRENT / HUMAN_EXPLICIT_SAVE_REQUEST"
  story_date: "理火三年・吉月初八"
  time_of_day: "中午；班富蘭剛起床；精確刻數 UNKNOWN"
  current_location: "觀止青樓／班富蘭暫住房間"
  scene_segment_status: "JI08_NOON_WAKE / MORNING_APPOINTMENT_MISSED / WOMENS_NIGHT_PENDING"

  previous_valid_hot:
    version: "V1.04"
    file: "觀止青樓_班富蘭線_HOT_SAVE_V1.04_RELATION_FIRST_吉月初七深夜_深秋詩會正式收束_關盼盼夢路待驗_CURRENT.md"
    sha256: "e053cb21504353c33a7898279c59fb320218d25249c43d0c7da20d81d4bd2de1"
    treatment: "PRESERVED / SUPERSEDED_AS_CURRENT_HOT_ONLY"

  world_semantics:
    current: "GUANZHI WORLD V2.2.3-CURRENT"
    settlement_module: "W-D24 / WORLD.DAILY_SETTLEMENT"

  evidence_origin:
    - "SAME_CONTEXT_REFERENCE"
    - "HUMAN_EXPLICIT_DIRECTION"
    - "NPC_AUTONOMOUS_ACTION_WITHIN_DIRECTOR_SCOPE"
    - "WORLD_PROCESS_ADVANCE_WITH_QUALIFIED_PRIOR_DECISION"
    - "CROSS_DAY_SETTLEMENT"

  formal_host_save_execution: "NOT_ESTABLISHED"
  created_real_date: "2026-10-08"
  timezone: "Asia/Taipei"
```

---

# 1｜CURRENT FREEZE｜初八中午

```yaml
CURRENT_FREEZE:
  player:
    person: "班富蘭"
    state:
      - "已從初七深夜睡到初八中午。"
      - "此睡眠跨度由玩家本輪明示之 SAVE 點成立。"
      - "剛起床；尚未執行初八任何玩家重大行動。"
      - "上午原定與疏影共同整理冊子之約定已錯過。"

  location:
    current: "觀止青樓／班富蘭暫住房間"

  day:
    date: "理火三年・吉月初八"
    phase: "中午"
    tonight:
      - "仕女夜預定今夜舉行。"
      - "疏影第一幅標竿畫公開拍賣預定今夜舉行，但尚未執行。"

  hard_lock:
    - "班富蘭睡到中午 != 上午替他完成任何工作。"
    - "錯過早晨約定 != 疏影冊子已共同完成。"
    - "新一天 != 所有 OPEN thread 自動關閉。"
```

---

# 2｜CROSS-DAY DAILY SETTLEMENT｜初七深夜 → 初八中午

```yaml
DAILY_SETTLEMENT_JI08_NOON:

  JINTANG_TRANSFER_AND_REGISTER:
    prior_state: "NEGOTIATED / PERFORMANCE_NOT_FULLY_PLAYED"
    outcome: "AUTO_SETTLED / WORLD_PROCESS_COMPLETED_BY_JI08_MORNING"
    exact_completion_time: "UNKNOWN / NOT BACKFILLED"
    established_now:
      - "潘金蓮／觀止之六百兩主收購完成交割。"
      - "原交易文契完成換主／轉接。"
      - "姚二娘在此筆交易中的中介履行完成；不因此自動建立和解或永久敵對。"
      - "錦棠自行談出的額外二百兩個人增值款已付予錦棠本人，不歸姚二娘。"
      - "周玉娘以『錦棠』正式完成官府妓籍申報／登記。"
    nonretroactivity:
      - "初六當晚仍然是真實的『尚未完整演出／未完成』。"
      - "現在只成立『到初八早晨之前已完成』，不得倒寫成初六已完成。"
    locks:
      - "妓籍登記 != 今日一定上工"
      - "妓籍登記 != blanket sexual consent"
      - "錦棠 != 周玉娘本名消失"

  SUSHI_PANPAN_DREAM:
    prior_state: "MUTUALLY_PERMITTED_TO_TRY / NOT_EXECUTED_AT_V1.04"
    outcome: "NPC_AUTONOMOUS_RESOLVED + REVEAL_PENDING"
    established_now:
      - "蘇軾於夜間正常睡著。"
      - "關盼盼自主選擇真正嘗試入夢。"
      - "夢路於初七夜至初八清晨之間實際發生。"
      - "蘇軾其後已醒；是否向他人敘述夢境由蘇軾本人決定。"
    private_or_unknown:
      - "夢境具體內容未公開。"
      - "班富蘭於本 SAVE 點尚未因任何合法來源知道夢境內容。"
      - "昨夜之夢與後世燕子樓文本中的夢是否同一事件／同一路徑仍 UNKNOWN。"
    locks:
      - "DREAM OCCURRED != SPRING DREAM"
      - "DREAM OCCURRED != ROMANCE"
      - "DREAM OCCURRED != SEXUAL RELATION"

  SHUYING_CATALOG_APPOINTMENT:
    prior_due: "吉月初八早晨／玩家先前表示早上要幫疏影整理冊子"
    outcome: "OVERDUE_ROLLOVER"
    reason:
      - "班富蘭睡至中午，玩家本人未在早晨出現。"
    established_now:
      - "班富蘭＋疏影之共同造冊／防偽工作尚未完成。"
      - "原早晨工作窗已錯過。"
    not_established:
      - "疏影是否生氣到何種程度。"
      - "疏影是否已自行選定標竿畫。"
      - "疏影是否已自行完成部分私人整理。"
    next_owner:
      - "班富蘭／疏影後續實際互動"

  SHUYING_AUCTION:
    outcome: "STILL_ACTIVE"
    state:
      - "第一幅標竿畫今夜拍賣計畫仍有效。"
      - "標竿畫具體哪一幅仍未建立。"
      - "底價、拍賣主持、焚畫數、70% 受益權是否同夜處理仍未固定。"

  WOMENS_NIGHT_PREPARATION:
    outcome: "WORLD_PROCESS_ADVANCED"
    established_now:
      - "觀止前台已持續準備紅線、桌位、女客免門錢／男客雙倍門錢等既定營運規則。"
      - "今夜仕女夜仍 NOT EXECUTED。"
    locks:
      - "準備完成 != 今夜來客名單已固定"
      - "女客入場 != 性同意"

  BAN_3164_TAELS_CONVERSION:
    player_intent: "明示要換銀票"
    outcome: "WORLD_PROCESS_ADVANCED / TRANSACTION_NOT_COMPLETED"
    established_now:
      - "昨夜手稿／事件物交易後，班富蘭可支配淨額 3,164 兩已另行記在其名下並等待處理。"
      - "觀止可依玩家已明示換票意圖開始對接定陶商會／相關商業接口。"
    not_established:
      - "尚未固定折耗、票面、兌付地、保管條件或實際承作方。"
      - "尚未由班富蘭接受任何具體換票條款。"
      - "尚未完成實際銀票交割。"
    candidate_interface:
      - "顧青簡／定陶商會具有既有合法商業接口資格。"
      - "沈萬三已由 GM 補充為插足宋代商會網之商人；精確職位／代表權不得自行擴張。"

  BORROWED_MENS_CLOTHING:
    outcome: "STILL_ACTIVE"
    state: "班富蘭借用本朝二手男子衣物之歸還義務仍在。"

  OLD_5_30_TAEL_LEDGER_CONFLICT:
    outcome: "EVIDENCE_HOLD"
    state:
      - "首闕 5 兩與整首 30 兩是否包含／另計，現存 SAVE 證據仍不足。"
      - "不因新一天而靜默選成任一答案。"

  MANUSCRIPT_RUMOR_AND_ATTRIBUTION:
    outcome: "STILL_ACTIVE / WORLD_PROCESS_ADVANCED"
    state:
      - "昨夜抄本作者錯配、政治斷章、詩會勝負與班富蘭後世作品故事仍在城內擴散。"
      - "傳聞仍不等於事實。"

  UNKNOWN_MESSENGER:
    outcome: "EVIDENCE_HOLD"
    state: "身份、雇主、目的仍 UNKNOWN。"

  OLD_WORK_DEPOSIT_LEDGER:
    outcome: "STILL_ACTIVE"
    state: "後世舊作寄存簿之保存、抄錄、收費、公開範圍仍未建立統一制度。"
```

---

# 3｜CURRENT MATERIAL STATE

```yaml
MATERIAL_STATE_V1_05:
  player_local_funds:
    manuscript_event_net:
      amount_taels: 3164
      standing: "ESTABLISHED / AWAITING CONVERSION"
    older_small_income_total:
      standing: "EXACT_TOTAL_UNKNOWN_DUE_5_30_CONFLICT"
    usd_holdings:
      standing: "LARGE HOLDING PRESERVED / NO FIXED LOCAL FX RATE"

  lodging:
    three_night_arrangement:
      status: "STILL WITHIN CURRENT PERIOD AT JI08 NOON"
      exact_expiry_clock: "UNKNOWN"

  shuying_art_market:
    catalog: "NOT_COMPLETED"
    anti_counterfeit_register: "NOT_COMPLETED"
    benchmark_painting: "NOT_ESTABLISHED"
    auction: "PLANNED_FOR_TONIGHT / NOT_EXECUTED"
    long_term_rights_contract: "NOT_EXECUTED"

  jintang:
    birth_name: "周玉娘"
    official_register_name: "錦棠"
    acquisition: "COMPLETED"
    official_registration: "COMPLETED_BY_JI08_MORNING"
    personal_200_taels: "PAID_TO_JINTANG"
    current_role: "GUANZHI REGISTERED PROSTITUTE IN DEVELOPMENT"

  dream_thread:
    sleep: "CONFIRMED"
    panpan_dream_entry: "OCCURRED"
    dream_content: "PRIVATE / NOT DISCLOSED TO PLAYER"
    future_yanzilou_identity: "UNKNOWN"
```

---

# 4｜RELATIONAL CENTER｜初八中午第一讀取面

```yaml
RELATIONAL_CENTER_V1_05:

  BAN_FULAN_X_SHUYING:
    standing: "COURTSHIP_OPEN + JOINT_ART_MARKET_WORKING_RELATION / MORNING_APPOINTMENT_MISSED"
    current_pressure:
      - "班富蘭先前答應／計畫早晨共同整理冊子，但睡至中午。"
      - "共同工作尚未完成。"
    still_not:
      - "ROMANCE"
      - "EXCLUSIVITY"
      - "SEXUAL_ACCESS"
      - "PLAYER OWNERSHIP OF ART"

  PAN_JINLIAN_X_JINTANG:
    standing: "ACQUISITION_COMPLETED / DEVELOPMENTAL MANAGEMENT RELATION"
    delta:
      - "交易履行與官冊程序已完成。"
      - "錦棠先前爭取出的二百兩個人增值已真正落到她本人。"
    still_not:
      - "BLANKET CONSENT"
      - "LONG_TERM REVENUE SHARE FIXED"
      - "FLOWER QUEEN STATUS"

  JINTANG_X_YAO_ERNIANG:
    standing: "BROKER TRANSACTION CLOSED / VALUE-CONFLICT HISTORY PRESERVED"
    delta:
      - "姚二娘之本筆中介程序完成。"
      - "二百兩未被姚二娘吸收。"
    still_not:
      - "RECONCILIATION"
      - "PERMANENT HOSTILITY"
      - "NO FUTURE CONTACT"

  BAN_FULAN_X_GU_QINGJIAN:
    standing: "COMMERCIAL INTERFACE ELIGIBLE / DIRECT RELATION NOT YET ESTABLISHED IN THIS ROUTE"
    current_hook:
      - "3,164 兩換票需求可能在今日形成第一次本線直接商業對接。"

  BAN_FULAN_X_SU_SHI:
    standing: "HARD_ESTABLISHED / LITERARY_RIVALRY_WITH_MUTUAL_RECOGNITION"
    new_information_boundary:
      - "班富蘭尚不知道蘇軾昨夜夢的具體內容。"

  SU_SHI_X_GUAN_PANPAN:
    standing: "DREAM_CONTACT_OCCURRED / PRIVATE_CONTENT / NO ROMANCE PROMOTION"
```

---

# 5｜OPEN THREADS｜初八中午

```yaml
OPEN_THREADS:
  - ref: "TH-BF-23-R1"
    owner: "PLAYER + SHUYING"
    state: "上午共同造冊已 missed；需中午後重新接工作。"

  - ref: "TH-BF-24"
    due: "吉月初八夜"
    state: "仕女夜＋疏影第一幅標竿畫拍賣仍 PLANNED / NOT EXECUTED。"

  - ref: "TH-BF-30"
    owner: "SHUYING"
    state: "標竿畫具體選擇仍未建立；只能由疏影合法決定。"

  - ref: "TH-BF-31"
    owner: "PLAYER + COMMERCIAL COUNTERPARTY"
    state: "3,164 兩換銀票：需求成立，條款與交割未完成。"

  - ref: "TH-BF-32"
    owner: "WORLD / GU QINGJIAN / COMMERCIAL NETWORK"
    state: "定陶商會是否今日正式承作班富蘭換票／疏影封存，待實際對接。"

  - ref: "TH-BF-33"
    owner: "CUI YINGYING + HONGNIANG"
    state: "仕女夜消息已送達崔宅；成年崔鶯鶯是否真正出門赴會尚未在本 SAVE 固定。紅娘尚未被賣入觀止。"

  - ref: "TH-BF-29"
    owner: "WORLD / HISTORICAL-LITERARY ROUTE"
    state: "昨夜夢與後世燕子樓夢是否同一事件仍 UNKNOWN。"

  - ref: "TH-BF-26"
    owner: "PLAYER"
    state: "借用男子衣物歸還義務仍在。"

  - ref: "TH-BF-02-LEDGER"
    owner: "ACCOUNTING / EVIDENCE"
    state: "舊 5／30 兩對帳衝突仍 HOLD。"

  - ref: "TH-BF-14"
    owner: "WORLD / RUMOR"
    state: "作者錯配、政治斷章與詩會外溢仍在擴散。"

  - ref: "TH-BF-16"
    owner: "UNKNOWN"
    state: "身份不明小廝之身份／雇主／目的仍 UNKNOWN。"

  - ref: "TH-BF-21"
    owner: "PAN / PLAYER / WORLD COMMERCIAL POLICY"
    state: "後世舊作寄存簿規則仍未固定。"
```

---

# 6｜CLOSED / SETTLED THREADS

```yaml
CLOSED_OR_SETTLED:
  - ref: "TH-BF-25 / JINTANG_TRANSFER"
    now: "CLOSED"
    result: "六百主交易、二百個人增值、換契與錦棠官府妓籍登記均已完成；完成時點只固定為 BY_JI08_MORNING。"

  - ref: "TH-BF-27 / SUSHI_SLEEP"
    now: "CLOSED"
    result: "蘇軾正常睡著。"

  - ref: "TH-BF-28 / PANPAN_DREAM_ENTRY"
    now: "CLOSED_AS_ENTRY QUESTION"
    result: "關盼盼自主入夢；夢內容另屬 private/reveal state。"
```

---

# 7｜FORBIDDEN PROMOTIONS｜V1.05

```yaml
FORBIDDEN_PROMOTIONS:
  - "班富蘭睡到中午 != 上午替他完成造冊"
  - "missed appointment != relationship rupture"
  - "疏影可以自主處理自己的畫 != 她已選好標竿畫"
  - "顧青簡是固定商業接口 != 已替班富蘭完成換票"
  - "班富蘭說要換票 != 已接受未知條款"
  - "沈萬三插足商會圈 != 自動取得定陶商會代表權"
  - "錦棠妓籍完成 != 當日上工"
  - "錦棠妓籍完成 != blanket sexual consent"
  - "關盼盼入夢 != 春夢"
  - "關盼盼入夢 != 戀愛"
  - "夢發生 != 後世燕子樓夢身份已證明"
  - "仕女夜準備推進 != 仕女夜已開始"
  - "崔鶯鶯知道仕女夜 != 已決定赴會"
  - "紅娘再次牽線候選 != 已被崔老夫人賣入觀止"
  - "新一天 != 傳聞與 UNKNOWN 自動消失"
```

---

# 8｜NEXT ENTRY｜30 秒接關

```text
時間：理火三年・吉月初八，中午。
地點：觀止青樓，班富蘭暫住房間。

班富蘭剛起床。

他睡過了原本要去幫疏影整理冊子的早晨。
共同造冊／防偽尚未完成。
今夜仕女夜與疏影標竿畫拍賣仍等著。

他昨夜 4,520 兩交易扣三成後的 3,164 兩淨額仍在自己名下，換銀票需求已成立，但尚未接受任何具體條款、尚未交割。

錦棠線已在跨日世界程序中完成：
- 六百兩主交易完成；
- 二百兩個人增值已給錦棠；
- 文契完成；
- 官府妓籍正式登記為「錦棠」。

蘇軾昨夜已睡著；關盼盼確實自主入夢。
夢的內容目前不是班富蘭知道的事情。

崔宅方面：仕女夜消息昨夜已送達；成年崔鶯鶯是否真正赴會，尚未在本 SAVE 固定。

下一幕從「班富蘭中午醒來，觀止已經運轉了半日」開始。
```

---

# 9｜SAVE COMMIT / 法位邊界

```yaml
SAVE_COMMIT:
  human_authorization:
    type: "DIRECT_EXPLICIT_SAVE_REQUEST_IN_CURRENT_CONVERSATION"
    exact_intent: "這樣我們剛好HOT SAVE  初八中午起床"
    status: "TRUE"

  document_result:
    status: "COMMITTED"
    route_current_hot: "V1.05"
    previous_hot_preserved: "V1.04"
    relation_first_projection_used: true
    daily_settlement_applied: true

  source_boundary:
    original_event_evidence_replaced: false
    prior_pending_states_preserved_as_prior_truth: true
    later_settlement_nonretroactive: true
    player_morning_action_not_fabricated: true

  execution_boundary:
    document_level_save_commit: true
    host_instrumented_formal_save_execution: "NOT_ESTABLISHED"
    e6_e7: "NOT_ESTABLISHED"

  core_schema:
    changed: false
    save_owner_changed: false
    write_path_owner_changed: false
    character_pool_modified: false

  world_semantic_change:
    current_world_successor_created: "V2.2.3-CURRENT"
    change: "A25 + W-D24 DAILY SETTLEMENT"
```

---

# 10｜根句

> **世界可以在玩家睡著時繼續活。**
>
> **但玩家睡過頭，不等於世界替他把事情做完。**
>
> **能結的結；該等人的等；錯過的留下代價；不知道的仍然不知道。**

END OF CURRENT HOT SAVE V1.05
# 觀止青樓（新）｜班富蘭線 HOT SAVE V1.06
## RELATION-FIRST｜理火三年・吉月初八夜｜仕女夜／《獨酌客》雙重成交後／疏影未來收益權資本戰開盤前

> **CURRENT ROUTE HOT SAVE / HUMAN EXPLICIT SAVE REQUEST / RELATION-FIRST**
>
> 本版承接：
> `觀止青樓_班富蘭線_HOT_SAVE_V1.05_RELATION_FIRST_吉月初八中午_每日結算後起床_CURRENT.md`
>
> 人類 AnjouRan 於本次對話明示：
>
> > 「導演先HOT SAVE 這裡剛好」
>
> 因此本版成立 **專案內文件級 HOT SAVE commit**。
>
> 本版固化吉月初八中午醒來後，至仕女夜《獨酌客》完成兩次成交、趙受益取得畫作、疏影未來公開作品收益權之大資本競爭者開始進場，但正式競標尚未啟動之全部已發生 Route 事實。
>
> 本版不把「候選劇情」「導演 MEMO」「尚未開拍的收益權競價」「尚未揭露的皇帝身份」偷寫成已完成結果。
>
> 本檔不宣稱 Host deployment、Formal Host execution、E6／E7、獨立 Agent 或 Formal SAVE instrumentation 已成立。

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BANFULAN_HOT_V1_06_RELATION_FIRST_JI08_NIGHT_CAPITAL_WAR_PREOPEN"
  route_id: "GUANZHI_BANFULAN_ROUTE"
  route_name: "班富蘭線"
  player_public_identity: "班傑明／字富蘭／號克林居士"
  version: "V1.06"
  record_type: "HOT_SAVE"
  record_state: "VALID / CURRENT / HUMAN_EXPLICIT_SAVE_REQUEST"

  story_date: "理火三年・吉月初八"
  time_of_day: "夜／仕女夜進行中；精確刻數 UNKNOWN"
  current_location: "觀止青樓／二樓側面雙人小包廂；班富蘭與蘇清在場"
  scene_segment_status: "WOMENS_NIGHT_ACTIVE / IMPERIAL_PORTRAIT_DOUBLE_SALE_DONE / SHUYING_FUTURE_REVENUE_RIGHTS_PREOPEN"

  previous_valid_hot:
    version: "V1.05"
    file: "觀止青樓_班富蘭線_HOT_SAVE_V1.05_RELATION_FIRST_吉月初八中午_每日結算後起床_CURRENT.md"
    sha256: "71d099e3cfd48a74ccd54d2e7aad53edd0ef39dcf0db1bd84c3f9088c3292f40"
    treatment: "PRESERVED / SUPERSEDED_AS_CURRENT_HOT_ONLY"

  current_governance:
    protocol: "LIHUO PROTOCOL V3.0.1"
    lighter: "LIHUO LIGHTER V4.8"
    main: "LIHUO MAIN V4.4"
    core: "GUANZHI RUNTIME CORE V3.11-CURRENT"
    world: "GUANZHI WORLD V2.2.3-CURRENT"
    character_pool: "LCAPG V3.3.20-CURRENT / 71"

  evidence_origin:
    - "SAME_CONTEXT_REFERENCE"
    - "HUMAN_EXPLICIT_PLAYER_ACTION"
    - "HUMAN_GM_ROUTE_DIRECTION"
    - "NPC_AUTONOMOUS_ACTION_WITHIN_DIRECTOR_SCOPE"
    - "STORY_VISIBLE_ROUTE_EXECUTION"

  formal_host_save_execution: "NOT_ESTABLISHED"
  created_real_date: "2026-10-08"
  timezone: "Asia/Taipei"
```

---

# 1｜CURRENT FREEZE｜仕女夜資本戰開盤前

```yaml
CURRENT_FREEZE:
  player:
    person: "班富蘭"
    state:
      - "已完成初八午後與疏影之長時間分類／整理工作。"
      - "已換上今日新購男裝。"
      - "已將借用三日之舊男裝歸還龐春梅。"
      - "已進入仕女夜並租用一間可俯視大堂、外部不易辨識房內人的雙人小包廂。"
      - "包廂內主要陪伴者為蘇清。"
      - "目前正從二樓觀察大堂下一輪資本競爭。"

  event:
    name: "吉月初八仕女夜"
    state: "ACTIVE"
    current_phase:
      - "疏影公開焚選／首件標竿作品市場化已完成。"
      - "《獨酌客》第一次三千兩成交已完成。"
      - "《獨酌客》題句＋趙受益私印後第二次六千兩成交已完成。"
      - "疏影未來公開作品之有限收益權尚未正式開拍。"
      - "顧青簡正在先行界定可出售的權利標的。"

  capital_stage:
    preopen: true
    present_or_entered:
      - "顧青簡"
      - "沈萬三"
      - "西門慶"
      - "孟玉樓"
      - "潘金蓮／觀止平台方"
    official_side_observation:
      - "歐陽修已低聲吩咐身旁人。"
      - "王安石亦已叫來隨從。"
      - "上述動作之具體資金／政治目的仍 UNKNOWN。"

  hard_lock:
    - "競爭者已進場 != 未來收益權競標已開始"
    - "有人顯示興趣 != 已出價"
    - "官員叫來隨從 != 官資已投入"
    - "資本戰預熱 != 結果已決定"
```

---

# 2｜吉月初八午後｜疏影共同工作

```yaml
SHUYING_AFTERNOON_WORK:
  status: "EXECUTED"

  established:
    - "班富蘭中午後前往疏影房內，補上睡過早晨後的共同工作。"
    - "整個下午主要用於畫作分類、整理、編排與建立較可檢索的作品秩序。"
    - "班富蘭把疏影房間窗戶打開，強迫室內換氣；疏影雖嫌冷／嫌畫會被風吹，最終未把窗關回。"
    - "班富蘭認為疏影長期病懨與室內過度悶閉有關；此為玩家判斷，不升格成醫療診斷。"
    - "工作過程存在輕度調情與肢體親近；疏影沒有因此建立概括性親密同意或戀愛關係。"
    - "疏影自行決定把男子飲酒圖選為今晚標竿作品。"

  catalog_state:
    preliminary_classification: "SUBSTANTIALLY_ADVANCED"
    formal_catalog: "PARTIAL / NOT DECLARED FULLY CLOSED"
    anti_counterfeit_scheme: "PARTIAL / CONTINUES"
    ownership:
      - "作品選留、出售、焚毀仍屬疏影本人決定。"

  relation_delta:
    ban_x_shuying:
      prior: "COURTSHIP_OPEN + JOINT_ART_MARKET_WORKING_RELATION"
      now: "COURTSHIP_OPEN + JOINT_ART_MARKET_WORKING_RELATION / AFTERNOON_WORK_FULFILLED / LIGHT_FLIRTATION_PRESENT"
      still_not:
        - "LOVERS"
        - "EXCLUSIVITY"
        - "SEXUAL_ACCESS"
        - "PLAYER OWNERSHIP OF ART"
```

---

# 3｜《獨酌客》｜身份、選畫與第一市場錨

```yaml
DUZHUOKE_ARTWORK:
  title_current: "《獨酌客》"
  title_status: "SHUYING-USED CURRENT TITLE / SAME-NIGHT"
  painter: "疏影"

  subject:
    public_read: "一名低調飲酒男子"
    true_identity_director_known: "趙受益／趙禎／宋仁宗"
    shuying_knows_true_identity: false
    ban_knows_true_identity: false
    suqing_knows_true_identity: false

  ban_current_knowledge:
    - "班富蘭已經認出畫中人與大堂中的『趙受益』是同一個人。"
    - "班富蘭仍不知道趙受益就是宋仁宗。"
    - "班富蘭是從歐陽修／王安石等人的視線與畫中『氣』比對出真人。"

  shuying_selection:
    status: "FINAL FOR TONIGHT / EXECUTED"
    reason_character_level:
      - "疏影自己感到畫中男子具有難言的氣場。"
      - "她認為其他畫較容易說清楚自己畫了什麼，只有這一張讓她想知道別人是否也會感到『哪裡不對』。"
    lock:
      - "選畫是疏影自己作出的決定，不是班富蘭代選。"

  market_anchor:
    primary_auction_price_taels: 3000
    buyer: "班富蘭"
    guanzhi_primary_commission_rate: "15%"
    guanzhi_primary_commission_taels: 450
    shuying_primary_net_taels: 2550
    status: "ESTABLISHED"
```

---

# 4｜疏影公開焚畫｜稀缺性與本人選擇

```yaml
SHUYING_PUBLIC_BURNING:
  status: "EXECUTED"

  established:
    - "仕女夜大堂設置火盆。"
    - "疏影當眾對一批作品作留／燒決定。"
    - "有人現場出價仍不足以自動阻止疏影焚畫。"
    - "疏影至少數次真正把作品投入火中，也曾在臨火時決定收回留下。"
    - "此舉使場內客人第一次明確理解：有些疏影作品有錢也買不到。"

  exact_ledger:
    scene_visible_sequence:
      handled_count: 5
      burned_count: 3
      retained_count: 2
    caution:
      - "此公開焚選批次與下午『五張標竿候選』是否逐張一一對應未另行建立，不得自行併表。"

  semantic_result:
    - "疏影的市場價值由『可買作品』與『不可買／已焚毀作品』共同形成。"
    - "燒畫 != 潘金蓮替疏影作決定"
    - "出高價 != 強制疏影出售"
```

---

# 5｜《獨酌客》第一次成交後之再創作

```yaml
DUZHUOKE_POST_PRIMARY:
  ban_inscription:
    status: "EXECUTED"
    origin:
      - "班富蘭使用自己與蘇清談及的未來歌曲意象，經玩家明示改寫後，當場題於畫上。"
    public_attribution: "克林居士當場題句"
    exact_text_preserved_in_story_context: true
    copyright_or_source_adjudication: "NOT PART OF SAVE FACT; ROUTE ONLY RECORDS WHAT WAS WRITTEN"

  shuying_response:
    - "疏影認為題句補出了她原先說不清的畫中氣質。"
    - "疏影接受此題句作為當晚完成版的一部分。"

  zhao_private_seal:
    status: "EXECUTED"
    actor: "趙受益"
    event:
      - "班富蘭拿畫走向趙受益，請其用私印作證題句為班富蘭本人所寫。"
      - "趙受益同意，以一方低調私印在畫上落印。"
      - "故事可見印文為『受益』。"
      - "趙受益並口頭表示，若今晚還有人問詞是誰寫的，他可替班富蘭作證。"

  identity_lock:
    - "趙受益在自己肖像上蓋『受益』私印 != 班富蘭因此知道他是皇帝"
    - "私印存在 != 公開御璽"
    - "真人為畫中人已被班富蘭／蘇清看出 != 帝王身份已被他們看出"
```

---

# 6｜《獨酌客》第二次拍賣｜五千起拍／六千成交

```yaml
DUZHUOKE_SECONDARY_AUCTION:
  seller: "班富蘭"
  threat_or_condition:
    opening_price_taels: 5000
    if_unsold: "班富蘭公開表示將把三千兩買來之畫投入火盆焚毀"
    player_reason:
      - "班富蘭判斷題句＋真人私印後，作品至少值五千兩。"
      - "若市場不承認此判斷，玩家明示寧願燒掉。"

  bids:
    - bidder: "西門慶"
      amount_taels: 5000
      status: "VALID BID / LATER OUTBID"
      motive_publicly_expressed:
        - "他表示正因為自己尚未看懂，而畫中人、題字者、歐陽修／王安石等反應構成資訊價值，因此五千不貴。"

    - bidder: "趙受益"
      amount_taels: 6000
      status: "WINNING BID /成交"
      expressed_reason:
        - "表示忽然有些捨不得畫被燒。"

  ximen_after_6000:
    - "西門慶未再加價。"
    - "他以『君子不奪人所好』收手。"
    - "此收手不證明資產上限，也不證明已識破趙受益帝王身份。"

  result:
    buyer: "趙受益"
    final_price_taels: 6000
    painting_delivery: "COMPLETED / 班富蘭雙手將畫交予趙受益"
    title_or_possession: "趙受益取得《獨酌客》"
    exact_secondary_commission: "UNKNOWN / NOT ESTABLISHED"
    exact_payment_medium_or_settlement_step: "NOT SEPARATELY NARRATED"
    nominal_gross_spread_before_unfixed_secondary_costs: 3000

  ban_statement_after_sale:
    - "班富蘭告知趙受益，他預感此畫未來可能漲到六萬兩以上。"
    - "六萬兩為班富蘭主觀預測，不是市場事實或保證。"
```

---

# 7｜御相知情梯度｜CURRENT

```yaml
IMPERIAL_PORTRAIT_KNOWLEDGE:
  director_truth:
    subject: "趙禎／宋仁宗"
    public_mode: "趙受益"

  zhao_shouyi:
    knows_subject_is_self: true
    knows_true_identity: true
    owns_painting_now: true

  ouyang_xiu:
    recognition: "ESTABLISHED IN SCENE / RECOGNIZES IMPERIAL IDENTITY"
    public_disclosure: false

  wang_anshi:
    recognition: "ESTABLISHED IN SCENE / RECOGNIZES IMPERIAL IDENTITY"
    public_disclosure: false

  ban_fulan:
    knows_same_person_as_painting: true
    knows_emperor: false

  su_qing:
    knows_same_person_as_painting: true
    knows_emperor: false

  ximen_qing:
    knows_something_unusual: true
    exact_identity: "NOT_ESTABLISHED"
    current_basis:
      - "觀察歐陽修／王安石反應"
      - "觀察趙受益本人六千回購"
      - "觀察『受益』私印"
    lock:
      - "suspicion != recognition"

  ying_bojue:
    notices_powerful_people_behaving_unnaturally: true
    exact_identity: "NOT_ESTABLISHED"

  gao_yanei:
    exact_identity: "NOT_ESTABLISHED"

  general_public:
    exact_identity: "UNKNOWN"
```

---

# 8｜班富蘭生活層｜新手期結束

```yaml
BAN_DAILY_LIFE_JI08:
  clothing:
    old_borrowed_menswear:
      lender: "龐春梅"
      three_day_use_period: "ENDED"
      returned: true
    new_menswear:
      purchased: true
      source: "觀止隔壁街成衣鋪"
      exact_price: "UNKNOWN"
      purpose: "仕女夜／日常自有衣物"

  lodging:
    free_newcomer_period: "ENDED AS OF JI08 NIGHT"
    paid_lodging_begins: true
    exact_room_rate: "NOT YET FIXED IN STORY"
    current_room_access: "CONTINUES SUBJECT TO PAID LODGING"

  womens_night_box:
    type: "SMALL TWO-PERSON SIDE BOX / HIGH OBSERVATION + LOW VISIBILITY"
    obtained: true
    exact_price: "UNKNOWN"
    expense: "INCURRED / AMOUNT NOT FIXED"
    principal_companion: "蘇清"
```

---

# 9｜錦棠｜首次大堂活動啟動

```yaml
JINTANG_JI08_NIGHT:
  identity:
    birth_name: "周玉娘"
    official_register_name: "錦棠"

  current_status:
    guanzhi_acquisition: "COMPLETED"
    registration: "COMPLETED"
    floor_activity: "BEGUN"

  established:
    - "錦棠已開始在仕女夜大堂走動、觀察與接觸客人。"
    - "她會自己判斷在哪一桌停、是否坐下、是否只添酒／說話。"
    - "她曾上二樓包廂向班富蘭與蘇清打招呼，表示先看看今晚場面。"

  still_not:
    - "SPECIFIC CLIENT CONTRACT"
    - "SEXUAL ENCOUNTER"
    - "BLANKET CONSENT"
    - "FLOWER QUEEN STATUS"
```

---

# 10｜班富蘭 × 蘇清｜背景揭露、共同祕密與新合作張力

```yaml
BAN_X_SUQING_JI08_NIGHT:
  prior_standing:
    - "FELLOW MODERN ANOMALY"
    - "SOURCE-RECOGNITION RIVALRY"
    - "TEASING ADVERSARIAL FAMILIARITY"
    - "NOT ROMANCE"

  ban_newly_knows:
    - "蘇清來自現代。"
    - "蘇清穿越前是小說作者，曾寫『大女主』型內容。"
    - "她曾把現代行銷／市場／服務業思維帶入觀止。"
    - "西門府事件是其世界觀被打碎的重要來源之一。"
    - "她現在承認自己為紅倌，並將『接受現實』與『認同現實』分開。"
    - "她仍認為自己在反抗，只是方式從抽象反抗轉為爭取選擇、價格、權力與實際籌碼。"

  still_unknown:
    - "蘇清原現代精確年份"
    - "原現代城市"
    - "家庭背景"
    - "穿越機制"
    - "她與班富蘭是否來自完全相同的未來時間線"

  physical_contact:
    established:
      - "西門慶／高衙內入場後，蘇清出現明顯舊創傷身體反應。"
      - "班富蘭主動摟住蘇清並握住她的手，目的包含陪伴，也包含玩家自述的趁機追求。"
      - "蘇清未離開，並主動反握班富蘭的手。"
      - "蘇清明示『這個是我自己握的』，把當次自主選擇與班富蘭的攻略敘事切開。"
    lock:
      - "SCENE-SPECIFIC ACCEPTED CLOSENESS != GENERAL PHYSICAL CONSENT"
      - "HANDHOLD / EMBRACE != ROMANCE ESTABLISHED"
      - "PLAYER FLIRT INTENT != NPC LOVE"

  cooperation_discussion:
    established:
      - "班富蘭明言：蘇清是自己在這個世界最大的罩門；若要長期共存，與其互拆，不如雙贏合作。"
      - "蘇清承認她能拆班富蘭的來源問題，而班富蘭也理解她的現代身分與方法。"
      - "雙方談及互不拆台、長期合作、共同放大利益。"
      - "『姦夫淫婦』『狼狽為奸』為調情／合作修辭，不自動建立性或戀愛關係。"
    not_fixed:
      - "正式分潤比例"
      - "正式保密契約"
      - "排他合作"
      - "戀愛關係"
      - "性關係"
```

---

# 11｜《賀新郎・八方美人》｜蘇清名聲線

```yaml
BAFANG_MEIREN_POEM:
  title: "《賀新郎・八方美人》"
  public_credit: "克林居士贈觀止蘇清姑娘"

  authorship_state:
    player_statement: "班富蘭／玩家明示此作為真原創"
    route_treatment: "PLAYER-ASSERTED ORIGINAL / NO CONTRARY SOURCE ESTABLISHED IN ROUTE"
    suqing_reaction:
      - "蘇清表示以她所知沒有一眼認出的現成來源。"

  physical_original:
    holder: "蘇清"
    transfer: "班富蘭同意原稿贈予蘇清"

  public_release:
    status: "EXECUTED"
    method:
      - "另謄公開用本"
      - "由行走丫環帶至大堂公開唱名／念出"
    public_effect:
      - "『克林居士贈蘇清』已被仕女夜客人公開聽見。"
      - "蘇清名字與該作品開始被綁定。"
      - "具體未來接客費／身價漲幅尚未定價。"

  lock:
    - "公開受捧 != 已成花魁"
    - "作品受歡迎 != 費率已自動上調到某一固定數字"
```

---

# 12｜仕女夜重要人物在場狀態

```yaml
WOMENS_NIGHT_PRESENT:
  ximen_qing:
    present: true
    role_in_scene:
      - "與高衙內、應伯爵一組進場。"
      - "已理解仕女夜商業模型。"
      - "已在《獨酌客》第二次拍賣出五千兩有效競價。"
      - "目前準備觀察疏影未來收益權資本戰。"

  gao_yanei:
    present: true
    current_behavior:
      - "對男客雙倍門錢／女人選男人規則感到不習慣。"
      - "尚未建立今晚任何具體女人關係。"
      - "沒有在《獨酌客》形成有效最終競價。"

  ying_bojue:
    present: true
    current_behavior:
      - "作為社交／消息嗅覺節點觀察場內反應。"
      - "已注意高位人物對趙受益／畫作的異常反應。"
      - "尚未識破皇帝身份。"

  ouyang_xiu:
    present: true
    recognized_zhao: true
    public_disclosure: false

  wang_anshi:
    present: true
    recognized_zhao: true
    public_disclosure: false

  zhao_shouyi:
    present: true
    incognito: true
    current_public_name: "趙受益"
    owns_duzhuoke: true

  pan_jinlian:
    present: true
    role:
      - "觀止平台／場控／抽成方"
      - "已見證疏影首件市場錨成立"
      - "尚未取得疏影未來收益權"

  shuying:
    present: true
    primary_sale_net_taels: 2550
    future_rights_decision_owner: true

  jintang:
    present: true
    floor_activity: "ACTIVE"

  su_qing:
    present: true
    current_location: "二樓雙人小包廂／班富蘭身邊"
```

---

# 13｜資本戰競爭者入場｜CURRENT PREOPEN

```yaml
SHUYING_FUTURE_REVENUE_CAPITAL_WAR:
  state: "PREOPEN / ASSET DEFINITION IN PROGRESS / NO WINNER"

  commercial_thesis:
    - "今晚三千兩原畫成交已建立疏影第一個公開市場價格錨。"
    - "六千兩二次成交證明故事、題字、身份／稀缺性可放大作品市場價值。"
    - "下一階段真正的大頭不是再賣一張原畫，而是疏影未來作品之有限經濟收益權。"

  ownership_principle:
    - "不賣疏影本人。"
    - "不賣她全部未來。"
    - "畫什麼、留什麼、燒什麼、哪張公開，仍由疏影決定。"
    - "可談的只是未來真正公開出售之作品，在約定條件下切出有限比例收益。"

  gu_qingjian:
    present: true
    current_role: "定陶商會／總會高階商業參謀、女性師爺；本輪資本戰交易結構設計者之一"
    route_authority:
      - "其人物卡已建立固定商業接口與高階商業參謀法位。"
    current_action:
      - "已明確提出：先別喊價，先決定今晚到底賣哪一段未來。"
      - "已向疏影確認不可把她全部未來賣斷。"
      - "提出『買收益，不買人』之交易框架。"
    limit:
      - "尚未替疏影決定比例。"
      - "尚未替定陶商會形成最終出價。"

  shen_wansan:
    present: true
    route_specific_standing:
      - "本輪依人類 GM 明示，作為定陶商會資本方代表之一進場。"
      - "精確長期官銜／永久代表權不得由本 SAVE 擴張。"
    current_action:
      - "已指出：若疏影能持續創作，真正值錢的是未來，而不是單張已售原畫。"
    bid: "NOT YET"

  ximen_qing:
    present: true
    capital_type:
      - "私人商人資本"
      - "本地人脈／官面／風月場／灰色交易能力"
    future_rights_interest: "ACTIVE OBSERVATION / NOT YET BID"
    wealth_limit: "UNKNOWN"
    lock:
      - "曾出五千兩畫作競價 != 已證明可無限對抗定陶商會總資本"

  meng_yulou:
    present: true
    capital_type: "PRIVATE FEMALE CAPITAL / PROPERTY-HOLDING BUSINESSWOMAN"
    expressed_interest:
      - "若只是買畫興趣不高。"
      - "若是未來分成，希望先把條件說清楚。"
    bid: "NOT YET"

  pan_jinlian_guanzhi:
    position: "PLATFORM / VENUE / MARKET-MAKING INTEREST"
    current_interest:
      - "未必需要直接競標。"
      - "其利益在於未來疏影作品交易若持續於觀止形成市場，觀止可持續取得平台位置／費用。"
    exact_future_cut: "NOT FIXED"

  official_side:
    ouyang_xiu:
      action: "已低聲吩咐身旁人"
      intent: "UNKNOWN"
    wang_anshi:
      action: "已叫來隨從"
      intent: "UNKNOWN"
    possible_official_money_or_backing: "NOT YET ESTABLISHED"

  rich_woman_layer:
    current_named_entry: "孟玉樓"
    additional_rich_women: "POSSIBLE / NOT YET ESTABLISHED"

  next_required_decision:
    owner: "疏影"
    question:
      - "她願意從未來公開作品收益中切出多少、以何種期限／範圍／條件出售？"
    status: "NOT YET DECIDED"
```

---

# 14｜班富蘭資金狀態｜不要假算現金

```yaml
BAN_FUNDS_V1_06:
  prior_known:
    manuscript_event_net_taels: 3164

  ji08_expenses_or_commitments:
    - "新男裝購入；金額 UNKNOWN"
    - "仕女夜雙人小包廂；金額 UNKNOWN"
    - "初八起觀止住宿開始計費；房價 UNKNOWN"
    - "《獨酌客》第一次三千兩競得"

  ji08_income_or_receivable:
    - "《獨酌客》第二次拍賣六千兩成交予趙受益"

  player_statement_at_primary_bid:
    - "當時可用來喊價的上限約三千兩。"

  accounting_status:
    nominal_art_trade_spread_before_unfixed_costs_taels: 3000
    exact_liquid_cash_now: "UNKNOWN"
    reasons:
      - "新衣／包廂／房費金額未定"
      - "二次交易之付款媒介與交割細節未單獨敘述"
      - "二次交易是否另有觀止佣金未建立"
      - "先前 3,164 兩換銀票計畫因今晚資金變動需重新判斷"

  old_banknote_conversion_thread:
    prior_intent: "成立"
    current: "REQUIRES REASSESSMENT / NOT COMPLETED"
```

---

# 15｜RELATIONAL CENTER｜V1.06

```yaml
RELATIONAL_CENTER_V1_06:

  BAN_FULAN_X_SHUYING:
    standing: "COURTSHIP_OPEN + JOINT_ART_MARKET_WORKING_RELATION / AFTERNOON_WORK_FULFILLED / FIRST_MARKET_SUCCESS"
    established_delta:
      - "下午共同整理作品。"
      - "班富蘭支持但未替疏影選《獨酌客》。"
      - "疏影首件標竿作品完成三千兩 primary market anchor。"
      - "班富蘭當場為作品加題，疏影接受。"
    still_not:
      - "ROMANCE"
      - "EXCLUSIVITY"
      - "SEXUAL ACCESS"
      - "PLAYER OWNERSHIP OF FUTURE WORKS"

  BAN_FULAN_X_SUQING:
    standing: "FELLOW MODERN ANOMALY + MUTUAL LEVERAGE AWARENESS + EMERGING INFORMAL ALLIANCE + ACTIVE FLIRTATION / NOT ROMANCE"
    established_delta:
      - "互相承認彼此都掌握對方重要罩門。"
      - "討論以雙贏合作替代互拆。"
      - "當次創傷觸發中有擁抱／牽手／蘇清反握。"
      - "《八方美人》原稿已贈蘇清並公開發表。"
    still_not:
      - "FORMAL PROFIT SHARE"
      - "ROMANCE"
      - "SEX"
      - "EXCLUSIVITY"
      - "BLANKET PHYSICAL CONSENT"

  SUQING_X_XIMEN_QING:
    standing: "DEEP FORMATIVE TRAUMA / CURRENT DIRECT RE-ENCOUNTER NOT YET PLAYED"
    tonight:
      - "蘇清已在包廂看見西門慶入場。"
      - "西門慶是否已明確認出／直接對上蘇清，尚未在今晚演出固定。"

  PAN_JINLIAN_X_XIMEN_QING:
    standing: "COMPLEX PAST MALE-FEMALE RELATION + DEEP MUTUAL RECOGNITION + CAN-COLLABORATE-DIRTY"
    tonight:
      - "兩人已在大堂有熟稔而帶刺的對話。"
      - "尚未因御相或資本戰正式聯手。"

  BAN_FULAN_X_ZHAO_SHOUYI:
    standing: "NEWLY ESTABLISHED ART-TRANSACTION + MUTUAL CURIOSITY"
    established:
      - "趙受益替班富蘭題句作私印見證。"
      - "趙受益六千兩買回《獨酌客》。"
      - "班富蘭仍不知道其帝王身份。"
```

---

# 16｜OPEN THREADS｜V1.06

```yaml
OPEN_THREADS:

  - ref: "TH-BF-24"
    owner: "WORLD / GUANZHI"
    state: "仕女夜 ACTIVE；尚未收束。"

  - ref: "TH-BF-34"
    owner: "SHUYING + CAPITAL COUNTERPARTIES"
    state: "疏影未來公開作品有限收益權：標的正在定義；比例、期限、底價、競標結果均未建立。"

  - ref: "TH-BF-35"
    owner: "WORLD / POLITICAL KNOWLEDGE"
    state: "班富蘭已知趙受益就是畫中人，但仍不知道宋仁宗身份；西門慶／應伯爵僅嗅到異常。"

  - ref: "TH-BF-36"
    owner: "SUQING + XIMEN_QING + GAO_YANEI"
    state: "蘇清已看見舊創傷來源人物進場；今晚真正正面重逢／對話尚未發生。"

  - ref: "TH-BF-37"
    owner: "BAN_FULAN + SUQING"
    state: "互不拆台／雙贏合作意向成立；正式分潤、保密與關係層級尚未定。"

  - ref: "TH-BF-38"
    owner: "JINTANG"
    state: "錦棠首次大堂活動已開始；客戶、價格、第一次真正接客結果尚未建立。"

  - ref: "TH-BF-39"
    owner: "OFFICIAL / CAPITAL FIELD"
    state: "歐陽修與王安石均有場外吩咐動作；是否形成官員／政治資本競爭仍 UNKNOWN。"

  - ref: "TH-BF-40"
    owner: "BAN_FULAN / GUANZHI"
    state: "免費住宿期結束；今晚房價與後續長住條件尚未定。"

  - ref: "TH-BF-31"
    owner: "PLAYER + COMMERCIAL COUNTERPARTY"
    state: "原 3,164 兩換銀票需求未完成；因今晚藝術交易資金流改變，需重新計算實際換票需求。"

  - ref: "TH-BF-33"
    owner: "CUI_YINGYING + HONGNIANG"
    state: "今晚 MEMO 中崔鶯鶯／紅娘路線仍屬強候選；本 HOT 截止尚未實際進場。"

  - ref: "TH-BF-29"
    owner: "WORLD / HISTORICAL-LITERARY ROUTE"
    state: "關盼盼入夢已發生；夢內容／後世燕子樓對應仍 UNKNOWN。"

  - ref: "TH-BF-02-LEDGER"
    owner: "ACCOUNTING / EVIDENCE"
    state: "舊 5／30 兩對帳衝突仍 HOLD。"

  - ref: "TH-BF-14"
    owner: "WORLD / RUMOR"
    state: "舊作作者錯配、政治斷章、詩會與新詞名聲繼續外溢。"

  - ref: "TH-BF-16"
    owner: "UNKNOWN"
    state: "身份不明小廝之身份／雇主／目的仍 UNKNOWN。"
```

---

# 17｜CLOSED / SETTLED THREADS｜本版新增

```yaml
CLOSED_OR_SETTLED_V1_06:

  - ref: "TH-BF-26 / BORROWED_MENS_CLOTHING"
    now: "CLOSED"
    result: "三日借衣已歸還龐春梅；班富蘭已購入自有男裝。"

  - ref: "TH-BF-23-R1 / SHUYING_MORNING_APPOINTMENT"
    now: "CLOSED_AS_OVERDUE / WORK_RESUMED_AND_FULFILLED_IN_AFTERNOON"
    result: "早晨確實睡過；下午已實際陪疏影長時間整理分類，未倒寫成早晨完成。"

  - ref: "TH-BF-30 / BENCHMARK_SELECTION"
    now: "CLOSED"
    result: "疏影自主選《獨酌客》為今晚標竿作品；三千兩 primary sale 已完成。"

  - ref: "DUZHUOKE_PRIMARY_SALE"
    now: "CLOSED"
    result: "班富蘭三千兩競得；觀止 primary 抽一成五＝450；疏影淨得 2550。"

  - ref: "DUZHUOKE_SECONDARY_SALE"
    now: "CLOSED_AS_AUCTION_RESULT"
    result: "西門慶 5000 出價後，趙受益 6000 勝出；畫已交趙受益。二次交易佣金／付款媒介細節另保持 UNKNOWN。"
```

---

# 18｜FORBIDDEN PROMOTIONS｜V1.06

```yaml
FORBIDDEN_PROMOTIONS:
  - "疏影首畫三千成交 != 她所有畫以後都值三千"
  - "二次六千成交 != 每張疏影畫都能翻倍"
  - "班富蘭預測六萬 != 未來市場保證六萬"
  - "趙受益買回自己肖像 != 公開承認皇帝身份"
  - "『受益』私印 != 御璽"
  - "班富蘭認出真人 != 認出宋仁宗"
  - "蘇清認出真人 != 認出宋仁宗"
  - "西門慶嗅到異常 != 西門慶已知皇帝身份"
  - "歐陽修／王安石認出皇帝 != 他們已公開揭露"
  - "沈萬三本輪代表定陶資本席 != 永久／無限代表定陶商會"
  - "顧青簡設計交易 != 她能替疏影決定出售比例"
  - "收益權可拍 != 疏影本人／全部未來可賣斷"
  - "孟玉樓有興趣 != 已出價"
  - "官員有動作 != 官資已入場"
  - "西門慶曾喊五千 != 已知其最大資產"
  - "班富蘭與蘇清擁抱牽手 != 戀愛成立"
  - "蘇清反握 != 後續 blanket physical consent"
  - "『姦夫淫婦／狼狽為奸』玩笑 != 性關係或正式合夥契約"
  - "《八方美人》公開受捧 != 蘇清已成花魁"
  - "錦棠開始大堂活動 != 已接客／已性交"
  - "免費住宿期結束 != 房價已固定"
  - "導演 MEMO 強候選 != 今晚已發生"
```

---

# 19｜NEXT ENTRY｜30 秒接關

```text
時間：理火三年・吉月初八夜。
地點：觀止青樓仕女夜。
玩家位置：二樓側面雙人小包廂；蘇清在身邊。

已發生：

1. 下午班富蘭與疏影把作品重新分類、整理。
2. 疏影自己選《獨酌客》作今晚標竿作品。
3. 疏影當眾燒畫，建立「有錢也未必買得到」的稀缺性。
4. 《獨酌客》三千兩由班富蘭競得：
   - 觀止 primary 抽 15%＝450；
   - 疏影淨得 2,550。
5. 班富蘭當場題句。
6. 趙受益本人以「受益」私印替題句作證。
7. 班富蘭以五千兩起拍重新拍賣，並公開表示流拍就燒。
8. 西門慶喊五千。
9. 趙受益喊六千並成交。
10. 班富蘭已把畫交給趙受益。
11. 班富蘭只知道趙受益就是畫中人，仍不知道他是宋仁宗。
12. 歐陽修、王安石知道真正身份，但沒有公開說破。
13. 西門慶、應伯爵已嗅到此人與此畫不普通，但身份仍未證實給他們。

現在：

真正的大戲轉向「疏影未來公開作品收益權」。

顧青簡已經進場，先阻止眾人直接喊價：
「先決定今晚到底賣哪一段未來。」

她明確提出：
- 不賣疏影本人；
- 不賣她全部未來；
- 疏影仍決定畫什麼、留什麼、燒什麼；
- 可談的是未來公開出售作品的有限收益比例。

沈萬三依本輪 GM 明示，代表定陶商會資本席之一進場。
西門慶留在局內。
孟玉樓以私人女性資本表示興趣。
潘金蓮站在觀止平台方位置。
歐陽修與王安石都已有場外吩咐動作，但目的 UNKNOWN。

疏影尚未決定要切出多少未來收益。

所以：

下一幕不是「開始喊價」。

下一幕是——

疏影先決定：
她願意拿多少自己的未來，讓這群人下注。
```

---

# 20｜SAVE COMMIT / 法位邊界

```yaml
SAVE_COMMIT:
  human_authorization:
    type: "DIRECT_EXPLICIT_SAVE_REQUEST_IN_CURRENT_CONVERSATION"
    exact_intent: "導演先HOT SAVE 這裡剛好"
    status: "TRUE"

  document_result:
    status: "COMMITTED"
    route_current_hot: "V1.06"
    previous_hot_preserved: "V1.05"
    relation_first_projection_used: true

  source_boundary:
    original_event_evidence_replaced: false
    previous_hot_history_preserved: true
    future_candidates_not_backfilled: true
    unknown_identity_not_promoted: true
    player_decisions_preserved: true
    npc_decisions_preserved: true

  execution_boundary:
    document_level_save_commit: true
    host_instrumented_formal_save_execution: "NOT_ESTABLISHED"
    e6_e7: "NOT_ESTABLISHED"

  runtime_schema:
    core_changed: false
    world_changed: false
    character_pool_changed: false
    save_owner_changed: false
    host_deployment_claimed: false
```

---

# 21｜根句

> **三千兩證明疏影的畫有人肯買。**
>
> **六千兩證明故事、身份與稀缺會替藝術加價。**
>
> **但真正的大錢還沒有開始。**
>
> **因為下一輪要競的，不是一張已經畫完的畫。**
>
> **而是疏影尚未畫出來的未來。**
>
> **那個未來仍然先屬於疏影自己。**

END OF CURRENT HOT SAVE V1.06
# 觀止青樓（新）｜班富蘭線 HOT SAVE V1.07
## RELATION-FIRST｜理火三年・吉月初八夜｜仕女夜／疏影未來收益權資本戰／四方聯合買方成立／趙受益十一萬有效出價

> **CURRENT ROUTE HOT SAVE / HUMAN EXPLICIT SAVE REQUEST / RELATION-FIRST**
>
> 本版承接：
> `觀止青樓_班富蘭線_HOT_SAVE_V1.06_RELATION_FIRST_吉月初八夜_御相雙重成交後_疏影未來收益權資本戰開盤前_CURRENT.md`
>
> 人類 AnjouRan 於本次對話明示：
>
> > 「先ＨＯＴＳＡＶＥ　這裡要中繼一下　不然這段有點長」
>
> 因此本版成立 **專案內文件級 HOT SAVE commit**。
>
> 本版固化 V1.06 之後至「趙受益代表四方聯合買方報出十一萬兩有效價、西門慶尚未回應」為止之已發生 Route 事實。
>
> 本版同時修正 V1.06 之後曾短暫出現的角色法位混淆：**顧青簡不是觀止拍賣主持人或規則設計者，而是定陶商會買方側高階商業策略者；潘金蓮／觀止才是拍賣平台與主持方。**
>
> 本檔不把「班富蘭對黑錢／洗錢的判斷」「西門慶背後資金是否構成犯罪」「趙受益是否有意將競價作為政治測試」偷寫成既成犯罪事實或正式司法結論。
>
> 本檔不宣稱 Host deployment、Formal Host execution、E6／E7、獨立 Agent 或 Formal SAVE instrumentation 已成立。

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BANFULAN_HOT_V1_07_RELATION_FIRST_JI08_NIGHT_ZHAO_110K_JOINT_BUYER"
  route_id: "GUANZHI_BANFULAN_ROUTE"
  route_name: "班富蘭線"
  player_public_identity: "班傑明／字富蘭／號克林居士"
  version: "V1.07"
  record_type: "HOT_SAVE"
  record_state: "VALID / CURRENT / HUMAN_EXPLICIT_SAVE_REQUEST"

  story_date: "理火三年・吉月初八"
  time_of_day: "夜／仕女夜進行中；精確刻數 UNKNOWN"
  current_location:
    player: "觀止青樓一樓大堂；已由側室返回競拍場"
    suqing: "二樓側面雙人小包廂"
    zhao_shouyi: "一樓大堂買方席"
  scene_segment_status: "WOMENS_NIGHT_ACTIVE / SHUYING_70PCT_BENEFICIAL_RIGHTS_AUCTION_ACTIVE / JOINT_BUYER_FORMED / ZHAO_110K_BID_LIVE"

  previous_valid_hot:
    version: "V1.06"
    file: "觀止青樓_班富蘭線_HOT_SAVE_V1.06_RELATION_FIRST_吉月初八夜_御相雙重成交後_疏影未來收益權資本戰開盤前_CURRENT.md"
    sha256: "d5ac293647b41756c672b57ee511b8580362a3edf05d930eb7121a8c794b75aa"
    treatment: "PRESERVED / SUPERSEDED_AS_CURRENT_HOT_ONLY"

  current_governance:
    protocol: "LIHUO PROTOCOL V3.0.1"
    lighter: "LIHUO LIGHTER V4.8"
    main: "LIHUO MAIN V4.4"
    core: "GUANZHI RUNTIME CORE V3.11-CURRENT"
    world: "GUANZHI WORLD V2.2.3-CURRENT"
    world_sha256: "e5dcf68ce1ef96f1bd98e2fe72dad8b62d2544999cb835139b12c7bc3e7a2011"
    character_pool: "LCAPG V3.3.20-CURRENT / 71"

  evidence_origin:
    - "SAME_CONTEXT_REFERENCE"
    - "HUMAN_EXPLICIT_PLAYER_ACTION"
    - "HUMAN_GM_ROUTE_DIRECTION"
    - "NPC_AUTONOMOUS_ACTION_WITHIN_DIRECTOR_SCOPE"
    - "STORY_VISIBLE_ROUTE_EXECUTION"

  formal_host_save_execution: "NOT_ESTABLISHED"
  created_real_date: "2026-10-08"
  timezone: "Asia/Taipei"
```

---

# 1｜CURRENT FREEZE｜趙受益十一萬有效出價後

```yaml
CURRENT_FREEZE:
  auction_asset:
    source_artist: "疏影"
    asset: "疏影身後仍存、可處分作品於未來公開拍賣所得之70%經濟受益權"
    nature:
      - "經濟受益權"
      - "不是疏影本人"
      - "不是疏影生前創作命令權"
      - "不是性／房間／人身支配權"
      - "不是所有實體畫作預先所有權"
    package_divisibility: "YES / 可由聯合買方按份持有，亦可於後續二級市場轉讓份額"

  current_high_bid:
    amount_taels: 110000
    bidder_public_name: "趙受益"
    bidder_role: "四方聯合買方唯一競價代表"
    status: "VALID LIVE BID / NOT YET HAMMERED"

  previous_high_bid:
    amount_taels: 100000
    bidder: "西門慶一方"
    status: "OUTBID BY ZHAO_110K"

  immediate_next_unknown:
    - "西門慶是否跟價"
    - "若跟價，下一口價格是多少"
    - "趙受益是否繼續加價"
    - "最終成交方與成交價"

  hard_lock:
    - "趙受益十一萬 != 已成交"
    - "西門慶尚未回應 != 已退出"
    - "四方聯合買方成立 != 朝廷／國庫參與"
    - "趙受益出價 != 皇家背書疏影"
    - "趙受益出價 != 正式御商封賞"
    - "高價競拍 != 犯罪證據"
```

---

# 2｜V1.06 後角色法位修正鎖

```yaml
ROLE_STANDING_CORRECTION:
  pan_jinlian:
    role:
      - "觀止青樓平台方"
      - "本場拍賣主持與市場規則執行者"
    lock:
      - "收益權拍賣規則不由顧青簡取代"

  gu_qingjian:
    affiliation: "定陶商會"
    role:
      - "買方側高階商業策略者／職業經理人型角色"
      - "評估大客戶、資本配置、交易結構、價格與非價格槓桿"
    not_role:
      - "不是觀止拍賣主持人"
      - "不是觀止規則制定者"
      - "不是疏影權利來源"

  shen_wansan:
    affiliation: "沈萬三自己的商會／資本系統"
    lock:
      - "不是定陶商會成員"
      - "與定陶屬競合／競爭資本"

  shuying:
    role:
      - "藝術家"
      - "原始權利來源"
    autonomy:
      - "作品選留／焚毀／出售自主"
      - "不因收益權金融化而喪失人格或生前創作自由"
```

---

# 3｜收益權原始經濟結構

```yaml
SHUYING_BENEFICIAL_RIGHTS_STRUCTURE:
  posthumous_public_auction_proceeds_split:
    beneficial_interest_holder: "70%"
    guanzhi_platform: "15%"
    shuying_designated_heir_pool: "15%"

  holder_rights:
    - "取得未來身後公開拍賣所得之70%經濟受益"
    - "可按聯合買方契約分割持有"

  holder_non_rights:
    - "不預先取得存世畫作實體所有權"
    - "若將來想取得特定畫作，仍須於公開拍賣參與競標"
    - "不得命令疏影生前必須畫什麼／畫多少"

  economic_purpose_prior_route:
    - "此收益權資本化原始構想之一，是將取得的資本用於形成可持續金融／投資／借貸收益，以支持疏影生前生活、醫療、材料與老年需求。"
    - "上述目的不等於任何具體投資績效已保證。"
```

---

# 4｜《獨酌客》與趙受益來源鏈最新狀態

```yaml
DUZHUOKE_PROVENANCE_CURRENT:
  painting: "《獨酌客》"
  painter: "疏影"
  true_sitter: "趙受益／趙禎／宋仁宗"
  formal_imperial_portrait: false
  nature: "私人／現場人物肖像性作品"

  ownership:
    current_owner: "趙受益"
    primary_sale:
      buyer: "班富蘭"
      amount_taels: 3000
    secondary_sale:
      buyer: "趙受益"
      amount_taels: 6000
      status: "ESTABLISHED"

  ban_inscription:
    status: "ON_PAINTING / EXECUTED"
    origin_status: "改寫未來歌曲意象；不得升格成班富蘭完全原創古詩詞"

  zhao_private_seal_on_painting:
    seal_text: "受益"
    nature: "PRIVATE_SEAL"
    meaning:
      - "為班富蘭當場書寫之見證"
    not_meaning:
      - "不是御璽"
      - "不是官方著作權認證"
      - "不是皇家收藏保證"

  sealed_batch_provenance_event:
    status: "EXECUTED"
    initiated_by_player:
      - "班富蘭下樓要求疏影帶上封存作品，請趙受益留印，證明今晚封存之畫就是當批作品，防止日後冒造。"
    shuying_consent:
      - "疏影自行同意"
      - "要求印不落畫面本體，可落登錄／畫背"
    process:
      - "觀止先完成自身封存／登錄"
      - "趙受益再以短記＋私人『受益』印作第三方當夜見證"
    legal_semantic_lock:
      - "第三方來源鏈見證 != 御賜"
      - "第三方來源鏈見證 != 御覽"
      - "第三方來源鏈見證 != 皇家真偽保證"
      - "私人印見證 != 朝廷權利來源"
```

---

# 5｜趙受益真實身份｜目前知情分層

```yaml
ZHAO_IDENTITY_KNOWLEDGE_MATRIX:
  true_identity: "趙禎／宋仁宗"
  public_operating_identity: "趙受益"
  public_reveal_status: "NOT PUBLICLY REVEALED"

  high_information_confirmed_or_effectively_confirmed:
    - "歐陽修"
    - "王安石"
    - "沈萬三及其高層情報線"
    - "顧青簡／定陶高層情報線"
    - "高衙內"
    - "西門慶"
    - "應伯爵（實質已知但拒絕公開說破）"
    - "潘金蓮"
    - "班富蘭"
    - "蘇清"

  strong_inference_or_partial_confirmation:
    - "孟玉樓：已取得宮中／上位來源強線索，理解其身分極高；不得自動擴張到她公開掌握所有細節"
    - "紅娘：知道其位階遠高於普通宗室／權貴，精確確認程度仍可保留"

  still_not_knowing_true_identity:
    - "疏影"
    - "錦棠／周玉娘"
    - "一般大堂客人"

  principle:
    - "RECOGNITION != PUBLIC DISCLOSURE"
    - "高資訊層知道官家在場 != 可公開行禮揭穿"
    - "趙受益以私人客身份入場，不欲將觀止轉成正式朝會場域"
```

---

# 6｜『御前競拍』目前正確語義

```yaml
IMPERIAL_OBSERVATION_CONTEXT:
  colloquial_route_term: "御前競拍"
  precise_meaning:
    - "皇帝本人以私人身份在場，且高資訊競標者已多數知道其真實身份。"
    - "競標者意識到自己的資本能力、聯盟、退出點、膽量、紀律與金流外觀可能被皇帝本人看見。"

  not_meaning:
    - "不是朝廷正式主持拍賣"
    - "不是皇家標案"
    - "不是皇帝為疏影作品背書"
    - "不是國庫資金競標"
    - "不是官方授予『御商』"

  market_effects:
    - "可能增加聲望／政治觀察的非財務價值"
    - "亦可能增加暴露財力、金流來源與政治關係的風險"
    - "故其效果可同時推高價格，也可迫使某些資本退縮"
```

---

# 7｜疏影 70% 收益權競價紀錄｜目前完整有效價

```yaml
AUCTION_BID_LEDGER:
  status: "ACTIVE / NO_HAMMER"
  currency: "taels"
  bids:
    - { bidder: "西門慶", amount: 10000 }
    - { bidder: "孟玉樓", amount: 12000 }
    - { bidder: "西門慶／高衙內早期聯合方", amount: 15000 }
    - { bidder: "定陶商會／顧青簡", amount: 18000 }
    - { bidder: "沈萬三", amount: 20000 }
    - { bidder: "孟玉樓＋兩名女性資本方", amount: 21000 }
    - { bidder: "沈萬三", amount: 25000 }
    - { bidder: "定陶商會／顧青簡", amount: 28000 }
    - { bidder: "西門慶／高衙內及延伸資本", amount: 30000 }
    - { bidder: "沈萬三", amount: 35000 }
    - { bidder: "定陶商會／顧青簡", amount: 40000 }
    - { bidder: "沈萬三", amount: 45000 }
    - { bidder: "西門慶／高衙內及延伸資本", amount: 50000 }
    - { bidder: "沈萬三", amount: 55000 }
    - { bidder: "定陶商會／顧青簡", amount: 60000 }
    - { bidder: "西門慶一方", amount: 70000 }
    - { bidder: "沈萬三", amount: 75000 }
    - { bidder: "西門慶一方", amount: 80000 }
    - { bidder: "沈萬三", amount: 90000 }
    - { bidder: "西門慶一方", amount: 100000 }
    - { bidder: "趙受益／四方聯合買方", amount: 110000, status: "CURRENT_HIGH_BID" }

  dingtao_exit:
    trigger: "西門慶七萬前後之異常價格區間"
    wording: "定陶退出整包直接競標，但不等於退出二級市場或後續聯合投資"

  meng_strategy_before_joint_plan:
    - "孟玉樓原已轉向等待得標者出現後，再談二級份額。"

  shen_strategy_before_joint_plan:
    - "沈萬三已開始考慮取得整包後拆售部分份額，以降低實際資金佔用。"
```

---

# 8｜西門慶資本狀態｜事實、推論與未證實事項分離

```yaml
XIMEN_CAPITAL_STATE:
  established_story_facts:
    - "西門慶與高衙內形成競價合作。"
    - "高衙內表示自己仍可再承擔一部分私人資本。"
    - "另有若干與官宦／權貴網絡相連之私人資本願意參與或送契。"
    - "西門慶曾收到一張無署名、無印記之短紙，內容為：『此物必取。價不足，由各家補。不得失手。』"
    - "該紙使西門慶明顯進入『受委託／受壓力繼續競價』狀態。"
    - "西門慶在八萬、十萬等價位仍持續跟價，表情與行為已不像單純追求投資報酬。"

  ban_player_hypothesis:
    - "班富蘭判斷西門慶背後部分資金可能來自不能見光的貪官／權力資金。"
    - "班富蘭進一步判斷該等資金可能試圖利用公開拍賣／資產交易使不透明資金取得較乾淨的資產外觀。"
    - "班富蘭認為西門慶已接近『死狀簽署臨界點』：若繼續以自己名義承接極端價格，而背後出資者不留下責任痕跡，可能成為最容易被犧牲的名義買方。"

  status_of_hypothesis:
    - "NOT PROVEN"
    - "NOT JUDICIAL_FINDING"
    - "NOT IMPERIAL_FINDING"
    - "競價高 != 當然構成洗錢／貪污"

  zhao_position_on_evidence:
    - "趙受益明確表示：出價就是出價；錢多不等於有罪；來源可疑仍須另查來源。"
```

---

# 9｜班富蘭 × 蘇清｜權力觀與關係推進

```yaml
BAN_SUQING_RELATION_DELTA:
  location_before_player_downstairs: "二樓側面雙人小包廂"

  established_dialogue_effects:
    - "班富蘭指出：西門慶在更高權力結構中可能只是被使用的前台／炮灰，不必把他視為無上限的牆。"
    - "蘇清承認自己對西門慶的恐懼並非單純理性權力排名，而含有身體記憶與創傷反應。"
    - "蘇清表示，看見西門慶也受上層壓力約束，使她第一次能把他看成『上面也有人』的人，而非不可撼動的終極牆。"
    - "班富蘭以玩笑／挑釁方式稱自己可能比西門慶更可怕。"
    - "蘇清拒絕把班富蘭直接升格成恐懼對象，維持自主與反向調侃。"
    - "蘇清指出班富蘭真正可能危險之處，是讓人先看見選擇與規則，而非單純以強迫控制。"

  player_statement_before_downstairs:
    - "班富蘭對蘇清說：『我來弄死西門慶，讓妳的 PTSD 治好。』"
    - "場景語義隨後立即落在『弄死西門慶這個局／使其資本結構崩解』，並未執行物理殺害行動。"

  relation_current:
    - "FELLOW_MODERN_ANOMALY"
    - "SOURCE-RECOGNITION_RIVALRY"
    - "TEASING_ADVERSARIAL_FAMILIARITY"
    - "MUTUAL-LEVERAGE_AWARENESS"
    - "EMERGING_INFORMAL_ALLIANCE"
    - "ACTIVE_FLIRTATION"
    - "NOT_ROMANCE"
```

---

# 10｜拍賣暫停｜十萬兩資本確認窗口

```yaml
AUCTION_PAUSE_AT_100K:
  initiated_by: "班富蘭"
  player_request_to_pan:
    - "暫停一下時間；此規模資本需要時間確認。"

  pan_decision:
    status: "ACCEPTED / EXECUTED"
    meaning:
      - "暫停一刻作資金、聯合出資、授權確認"
      - "十萬兩仍是當時最高有效價"
      - "不是落槌"
      - "不是成交"

  pan_rule_emphasis:
    - "誰喊，誰負責。"
    - "避免事後聲稱聯合方其實未同意或資金只是口頭承諾。"
```

---

# 11｜三方側室會談｜班富蘭提出『御商不是牌匾，是關係』

```yaml
PRIVATE_MEETING_1:
  convened_by: "班富蘭"
  invited_parties:
    - "孟玉樓"
    - "顧青簡／定陶商會"
    - "沈萬三"
  location: "觀止側室"

  player_argument:
    - "從純商業投資角度，收益權價格已大幅偏離原有純現金流估值。"
    - "目前新增最大價值來源之一，是趙受益本人、他的私人『受益』印所形成的來源鏈與在場見證，以及高資訊圈層都知道他真正身份卻未公開說破的關係價值。"
    - "班富蘭提出『御商』作為戰略性描述：不是朝廷正式授予頭銜，而是與皇帝私人身份真正做過一筆乾淨、可查、共擔風險的生意後所形成的關係入口與被記住的價值。"

  corrections_by_parties:
    gu_qingjian:
      - "趙受益之印為私人印，不是官印。"
      - "不得把私人出席／私人見證偷換成御賜或官方封號。"
      - "『御商』只能是室內策略語彙，不能當成已授予身份。"
    shen_wansan:
      - "若只是掛假的皇家招牌則不可取；若是建立真實商業關係則有價值。"
    meng_yulou:
      - "真正值錢的是『公開不可宣稱、私下高資訊圈層都知道』的關係層，而非喊破身份。"

  status:
    - "三方均願意繼續聽方案。"
```

---

# 12｜四方聯合買方方案｜2＋2＋2＋1

```yaml
JOINT_BUYER_PLAN:
  proposer: "班富蘭"

  asset_total_under_joint_plan: "疏影70%經濟受益權整包"

  internal_allocation_of_total_70pct_asset:
    meng_yulou: "20% of total posthumous auction proceeds"
    dingtao_merchant_association: "20% of total posthumous auction proceeds"
    shen_wansan_side: "20% of total posthumous auction proceeds"
    zhao_shouyi: "10% of total posthumous auction proceeds"
    total: "70%"

  same_structure_within_70pct_package:
    meng_yulou: "2/7 of package"
    dingtao: "2/7 of package"
    shen_wansan: "2/7 of package"
    zhao_shouyi: "1/7 of package"

  funding:
    - "四方按最終成交價格與各自份額真實出資。"
    - "不是趙受益替其他人墊全部資金。"
    - "不是國庫出資。"

  public_bidding_voice:
    sole_bidder: "趙受益"
    meaning:
      - "趙受益代表四方聯合買方對外喊價。"
      - "沈萬三、孟玉樓、定陶不再各自對外競價。"

  key_integrity_lock:
    - "不是假托價。"
    - "任何趙受益喊出的有效價格，若對手退出，四方均真實願意按比例成交與付款。"
    - "四方出資人對觀止內帳透明。"
    - "不是名義買家與實際出資人完全割裂的人頭交易。"
```

---

# 13｜錦棠請趙受益入側室

```yaml
JINTANG_MESSENGER_EVENT:
  player_instruction:
    - "班富蘭讓錦棠去請趙受益入側室，與沈萬三、孟玉樓、定陶商會及班富蘭討論方案。"

  jintang_action:
    - "錦棠前往趙受益席位傳話。"
    - "她如實報出沈萬三、孟玉樓、定陶商會、克林居士均在側室。"
    - "趙受益接受邀請入內。"
    - "錦棠沒有擅自進入資本會談。"

  jintang_identity_knowledge:
    - "仍不知道趙受益就是皇帝。"
    - "只知道此人財力、地位與全場反應極不尋常。"

  relationship_note:
    - "此前錦棠已向趙受益自報官冊名『錦棠』與本名『周玉娘』。"
    - "趙受益已表示記住她的名字。"
    - "未建立包養、性、初夜預約或任何概括承諾。"
```

---

# 14｜趙受益對聯合方案之審查與接受

```yaml
ZHAO_REVIEW_OF_JOINT_PLAN:
  zhao_conditions:
    - "自己只作買方，不替三家『逼』西門慶，也不把競價本身當成查案。"
    - "趙受益自己的一成必須是私人可合法支配資金。"
    - "三家六成必須有真實承擔能力。"
    - "出資人與份額須進觀止內帳，不得把真實出資人藏成完全不可查。"
    - "私人競價不等於朝廷背書疏影。"
    - "與他做過生意不等於取得正式『御商』頭銜。"
    - "價格由他本人決定。"
    - "何時停止競價也由他本人決定。"

  zhao_evidence_position:
    - "西門慶繼續跟價本身不被視為犯罪證據。"
    - "若資金來源有問題，仍需另以來源證據判斷。"

  zhao_acceptance:
    status: "EXPLICITLY ACCEPTED WITH CONDITIONS"
    share: "10% of total posthumous proceeds / 1/7 of the 70% package"
    public_role: "SOLE_BIDDING_REPRESENTATIVE"

  relational_value_statement:
    - "趙受益拒絕授予『御商』名號。"
    - "但表示若完成此筆生意，會記住沈萬三、孟玉樓、定陶等參與者的名字。"
```

---

# 15｜當場字據｜正式授權趙受益獨立喊價

```yaml
JOINT_BID_AUTHORIZATION_WRITING:
  status: "EXECUTED / SIGNED IN STORY"

  core_terms:
    - "孟玉樓認總收益20%。"
    - "定陶商會認總收益20%。"
    - "沈萬三一方認總收益20%。"
    - "趙受益認總收益10%。"
    - "四方依最終成交價格，按份額實際出資、享受相應收益並承擔相應風險。"
    - "沈萬三、孟玉樓、定陶共同授權趙受益作為本聯合買方唯一競價代表。"
    - "競價金額、加價幅度、停止競價時點，由趙受益自行決定。"
    - "趙受益有完全停止競價之權。"
    - "任何一方不得於落槌後僅以價格超出原預期為由否認按比例出資義務。"
    - "授權屬真實競價授權，不是價格諮詢。"

  signatures_or_markings:
    shen_wansan: "SIGNED"
    meng_yulou: "SIGNED"
    dingtao:
      internal_authorization_check: "CONFIRMED IN SCENE"
      gu_qingjian_as_transaction_representative: "SIGNED"
    zhao_shouyi:
      signed_name: "趙受益"
      private_seal: "受益"
      status: "SIGNED / SEALED"
    ban_fulan:
      role: "WITNESS"
      signed_as: "班傑明／字富蘭／號克林居士"
      status: "COUNTERSIGNED AS WITNESS"

  critical_semantics:
    - "班富蘭不是四方之一，不享有本聯合買方收益份額。"
    - "班富蘭副署是見證，不是代任何一方同意。"
    - "趙受益私人印 != 皇帝官印。"
    - "字據不是聖旨。"
    - "字據不是御商封賞。"
```

---

# 16｜回場後之公開市場狀態

```yaml
RETURN_TO_AUCTION:
  sequence:
    - "孟玉樓返回大堂。"
    - "沈萬三返回大堂。"
    - "顧青簡返回大堂。"
    - "趙受益返回大堂。"
    - "班富蘭隨後返回。"

  market_read:
    - "外部可見三個主要正常資本競爭者不再各自舉牌。"
    - "西門慶看見三方與趙受益先後從同一側室返回，但不知道字據內容。"
    - "西門慶當時十萬兩仍為最高有效價。"

  pan_resume:
    - "潘金蓮宣布資本確認時間結束。"
    - "十萬兩仍為當時最高有效價。"
    - "拍賣恢復。"
```

---

# 17｜歐陽修 × 王安石｜官家下場觀察線

```yaml
OUYANG_WANG_OBSERVATION:
  status: "ACTIVE / IMPORTANT CAMERA_THREAD"

  observed:
    - "兩人看到沈萬三、孟玉樓、顧青簡退出個別競價，卻不像真正失敗退場。"
    - "兩人看到趙受益與三方共同自側室返回。"
    - "王安石推測：官家手上此刻可能已不只是一個人的錢。"
    - "歐陽修意識到官家可能不是單純去聽一筆生意，而是進入了那筆生意。"

  ouyang_current_tone:
    - "首先擔心皇帝本人下場後，市場是否還能維持正常競價。"
    - "對局勢抱有警覺，不把皇帝參與單純當成熱鬧。"

  wang_current_tone:
    - "優先看結構與市場行為。"
    - "在趙受益喊價後，注意力立刻轉向西門慶而非皇帝本人。"
    - "核心問題：西門慶及其背後資本是否還敢跟。"

  camera_priority_next:
    - "依玩家明示，後續鏡頭應提高歐陽修、王安石對官家親自競價之反應比重。"
```

---

# 18｜趙受益十一萬｜目前斷點

```yaml
ZHAO_110K_EVENT:
  status: "EXECUTED / CURRENT HIGH BID"
  context:
    - "潘金蓮恢復拍賣後，西門慶十萬兩已報至第二次附近。"
    - "沈萬三、定陶、孟玉樓均未再以原個別身份舉牌。"

  action:
    actor: "趙受益"
    public_bid_taels: 110000
    role: "四方聯合買方唯一競價代表"

  funding_status:
    - "不是趙受益一人承擔全部十一萬。"
    - "若以十一萬成交，四方依2／2／2／1結構承擔。"
    - "趙受益承擔其中總收益10%對應之出資。"

  room_reaction:
    - "全場短暫死寂。"
    - "高資訊者知道此為官家本人下場，但不得公開喊破。"
    - "一般客人只看見趙受益再度以驚人財力進場。"

  ouyang_reaction:
    - "低聲：『……果然。』"

  wang_reaction:
    - "沒有盯著官家，而立即轉看西門慶。"

  freeze_point:
    - "西門慶尚未對十一萬作出跟價、退出、談判或其他行動。"
    - "潘金蓮尚未落槌。"
    - "趙受益是否繼續往上喊，取決於後續市場與其本人決定。"
```

---

# 19｜四方聯合買方的真實目的邊界

```yaml
JOINT_BUYER_PURPOSE_BOUNDARY:
  valid_purposes:
    - "真實取得疏影70%收益權資產。"
    - "藉由聯合資本提高正常市場中可承擔的真實購買力。"
    - "建立趙受益與三家資本之真實商業合作關係。"
    - "在正常真實競價中觀察西門慶對價格的反應與其資金深度。"

  not_preestablished:
    - "不是虛假競價托價"
    - "不是預先保證要把西門慶逼到某一特定價格"
    - "不是朝廷秘密查案命令"
    - "不是正式反貪行動"
    - "不是已證實西門慶背後存在貪污洗錢"

  zhao_control:
    - "趙受益有獨立喊價權。"
    - "趙受益有獨立停止權。"
    - "班富蘭與三家不得代替趙受益決定每一口價。"
```

---

# 20｜錦棠當前人物線

```yaml
JINTANG_CURRENT:
  identity:
    registered_name: "錦棠"
    birth_name: "周玉娘"
    age_status: "成年女性"

  current_goal:
    - "累積能在未來初夜／出局拍賣時形成競爭的客源與名聲。"
    - "希望『錦棠』從官冊強加之名，逐漸變成她自己能做大的名字。"

  zhao_interaction_established:
    - "曾主動向趙受益敬酒並交談。"
    - "坦承六千兩對自己而言是巨大金額。"
    - "向趙受益說明本名周玉娘、官冊名錦棠。"
    - "說自己想紅、想被記住、想藉價格獲得更多選擇。"
    - "沒有強求趙受益承諾未來出價，只求他先記住名字。"
    - "趙受益表示『記住了』。"

  no_auto_promotion:
    - "沒有訂下初夜"
    - "沒有包養"
    - "沒有性同意"
    - "沒有戀愛關係"
    - "沒有得知皇帝真實身份"
```

---

# 21｜崔鶯鶯／紅娘／應伯爵側線

```yaml
SIDE_FLIRT_THREAD:
  cui_yingying:
    adult: true
    current:
      - "自願坐入西門慶／高衙內／應伯爵／紅娘附近桌位。"
      - "曾以綠茶式話術與桌下輕微足部曖昧同時撩動西門慶與高衙內。"
      - "在發現西門慶已不再享受競價、似被壓力迫使跟價後，收斂刺激。"
      - "曾直接問西門慶是否『真的不能停』。"
      - "十萬前後反而把酒杯推給西門慶，呈現對其壓力的觀察。"

  hongniang_yingbojue:
    current:
      - "形成媒合／情報型喜劇搭檔雛形。"
      - "紅娘擅長看誰想睡誰；應伯爵擅長看誰有錢／有人脈。"
      - "應伯爵已看出西門慶越來越像在替別人辦差。"

  lock:
    - "成人調情 != 性同意"
    - "曖昧 != 關係成立"
```

---

# 22｜尚未成立／不得回填

```yaml
OPEN_UNKNOWNS_AND_NO_BACKFILL:
  auction:
    - "最終成交價 UNKNOWN"
    - "最終得標方 UNKNOWN"
    - "西門慶是否跟十一萬 UNKNOWN"
    - "趙受益會喊到哪裡 UNKNOWN"

  ximen_money:
    - "西門慶背後每一名出資者身份 UNKNOWN"
    - "各筆資金是否合法 UNKNOWN"
    - "是否構成貪污／洗錢 UNKNOWN"
    - "是否存在正式死命令以外的更高層具名指令 UNKNOWN"

  zhao:
    - "趙受益是否把此次競標視為政治測試：僅部分動機可推測，未明示完整目的"
    - "是否會因此日後調查任何人 UNKNOWN"
    - "是否會把三家視為長期御用商人 UNKNOWN"

  shuying:
    - "仍不知道趙受益是宋仁宗"

  jintang:
    - "仍不知道趙受益是宋仁宗"
    - "未來初夜／出局競標之任何人選與價格均未成立"

  suqing:
    - "創傷反應有所鬆動 != PTSD 已治癒"

  finance:
    - "班富蘭目前精確可動用現金 UNKNOWN"
    - "《獨酌客》二手交易後班富蘭精確淨收入仍受二手交易費用機制 UNKNOWN 影響"
```

---

# 23｜NEXT ENTRY｜續跑時從這一拍開始

```yaml
NEXT_ENTRY:
  camera_open:
    location: "觀止青樓一樓大堂"
    exact_moment: "趙受益剛喊出十一萬，全場死寂"

  immediate_focus_priority:
    1: "西門慶／高衙內／背後資本對十一萬的第一反應"
    2: "歐陽修與王安石如何理解官家正式下場"
    3: "潘金蓮如何維持拍賣程序與市場完整性"
    4: "沈萬三／顧青簡／孟玉樓身為聯合買方但不再自行喊價的觀察"
    5: "趙受益是否、何時、為何再出下一口"

  player_sovereignty:
    - "班富蘭下一句話、下一個移動、是否上樓回到蘇清身邊，仍由玩家本人決定。"

  story_do_not_skip:
    - "不得直接跳成西門慶十二萬，除非場景先讓其作出可見決定。"
    - "不得預定西門慶必敗。"
    - "不得預定趙受益必勝。"
    - "不得把高價跟價直接寫成犯罪自白。"
    - "後續依玩家明示，歐陽修／王安石鏡頭提高。"
```

---

# 24｜SAVE RECEIPT BOUNDARY

```yaml
SAVE_RECEIPT:
  human_explicit_save_request: true
  document_created: true
  file_level_hot_save_commit: true
  route_current_pointer: "V1.07"

  evidence_class: "SAME_CONTEXT_REFERENCE + HUMAN_EXPLICIT_SAVE_REQUEST"

  does_not_claim:
    - "HOST_INSTRUMENTED_SAVE"
    - "FORMAL_HOST_EXECUTION"
    - "E6"
    - "E7"
    - "INDEPENDENT_AGENT_DEPLOYMENT"

  continuation_rule:
    - "後續故事若續跑，以本檔 CURRENT_FREEZE 為主要 HOT 起點。"
    - "V1.06 保留原始歷史，不回寫刪除。"
    - "本版對 V1.06 後已知角色法位錯誤採非回溯修正：錯誤文本保留為歷史，但不得再作有效劇情事實引用。"
```

---

# END OF HOT SAVE V1.07

**CURRENT FREEZE：**

> 潘金蓮已恢復拍賣。西門慶原最高價十萬兩。沈萬三、孟玉樓、定陶商會已停止以各自身份競價，並與趙受益成立真實四方聯合買方。三家各認總收益二成，趙受益認一成；三家正式授權趙受益獨立決定加價幅度與停止時點，班富蘭以見證人副署。趙受益已回到場中，代表聯合買方報出 **十一萬兩**。此為真實、可成交之有效價。西門慶尚未回應。歐陽修低聲「……果然」，王安石已將注意力轉向西門慶。故事於此 HOLD。

# 觀止青樓（新）｜班富蘭線 HOT SAVE V1.08
## RELATION-FIRST｜理火三年・吉月初八深夜｜十一萬落槌／西門慶保命紙／疏影長期基金構想／弄影軒穿衣同睡

> **CURRENT ROUTE HOT SAVE / HUMAN EXPLICIT SAVE REQUEST / RELATION-FIRST**
>
> 本版承接：
> `觀止青樓_班富蘭線_HOT_SAVE_V1.07_RELATION_FIRST_吉月初八夜_四方聯合買方成立_趙受益十一萬有效出價_CURRENT.md`
>
> 人類 AnjouRan 於本次對話明示：
>
> > 「這個點ＨＯＴ　ＳＡＶＥ剛好」
>
> 因此本版成立 **專案內文件級 HOT SAVE commit**。
>
> 本版固化 V1.07 之後，至「班富蘭與疏影在弄影軒內明確約定今晚不發生性行為、保持衣著、同床純睡眠休息」為止之已發生 Route 事實。
>
> 本版不將西門慶之匿名資金來源偷寫成已證實貪腐／洗錢，不將其向趙受益靠近偷寫成已正式成為污點證人，不將班富蘭對其生命危險之判斷偷寫成已有刺殺計畫。
>
> 本版亦不把「疏影十一萬長期信託／基金」偷寫成已完成正式契約：目前已形成高度明確之結構方案與當場共識方向，但管理人、受託權限、風險上限、三分保底缺口責任、正式章程與簽署仍待完成。
>
> 本檔不宣稱 Host deployment、Formal Host execution、E6／E7、獨立 Agent 或 Formal SAVE instrumentation 已成立。

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BANFULAN_HOT_V1_08_RELATION_FIRST_JI08_LATE_NIGHT_110K_HAMMER_SHUYING_FUND_CLOTHED_SLEEP"
  route_id: "GUANZHI_BANFULAN_ROUTE"
  route_name: "班富蘭線"
  player_public_identity: "班傑明／字富蘭／號克林居士"
  version: "V1.08"
  record_type: "HOT_SAVE"
  record_state: "VALID / CURRENT / HUMAN_EXPLICIT_SAVE_REQUEST"

  story_date: "理火三年・吉月初八"
  time_of_day: "深夜／仕女夜後段；精確刻數 UNKNOWN"

  current_location:
    player: "觀止青樓二樓弄影軒／疏影房內"
    shuying: "弄影軒／與班富蘭同床休息"
    suqing: "已離開弄影軒；精確當前位置未另行固化"
    zhao_shouyi: "大堂／官務後續線；是否已離開 UNKNOWN"
    ximen_qing: "已走向趙受益並提出私下陳述需求；後續官務處理未在本段展開"

  scene_segment_status:
    - "SHUYING_70PCT_BENEFICIAL_RIGHTS_AUCTION_HAMMERED_AT_110K"
    - "XIMEN_SELF_PROTECTION_BREAKPOINT_ESTABLISHED"
    - "BAN_5000_NOTE_PRICE_SIGNAL_EXECUTED"
    - "SHUYING_LONG_TERM_FUND_STRUCTURE_DESIGN_ACTIVE"
    - "BAN_SHUYING_PRIVATE_RELATIONAL_SCENE"
    - "CLOTHED_NONSEXUAL_SLEEP_AGREED_AND_BEGUN"

  previous_valid_hot:
    version: "V1.07"
    file: "觀止青樓_班富蘭線_HOT_SAVE_V1.07_RELATION_FIRST_吉月初八夜_四方聯合買方成立_趙受益十一萬有效出價_CURRENT.md"
    sha256: "372a3deb245d060b3da420219328a0109c838797c5dc2de03a6f0fe7123a0b7a"
    treatment: "PRESERVED / SUPERSEDED_AS_CURRENT_HOT_ONLY"

  current_governance:
    protocol: "LIHUO PROTOCOL V3.0.1"
    lighter: "LIHUO LIGHTER V4.8"
    main: "LIHUO MAIN V4.4"
    core: "GUANZHI RUNTIME CORE V3.11-CURRENT"
    world: "GUANZHI WORLD V2.2.3-CURRENT"
    world_sha256: "e5dcf68ce1ef96f1bd98e2fe72dad8b62d2544999cb835139b12c7bc3e7a2011"
    character_pool: "LCAPG V3.3.20-CURRENT / 71"

  evidence_origin:
    - "SAME_CONTEXT_REFERENCE"
    - "HUMAN_EXPLICIT_PLAYER_ACTION"
    - "HUMAN_GM_ROUTE_DIRECTION"
    - "NPC_AUTONOMOUS_ACTION_WITHIN_DIRECTOR_SCOPE"
    - "STORY_VISIBLE_ROUTE_EXECUTION"

  formal_host_save_execution: "NOT_ESTABLISHED"
  created_real_date: "2026-10-08"
  timezone: "Asia/Taipei"
```

---

# 1｜CURRENT FREEZE｜弄影軒穿衣同睡

```yaml
CURRENT_FREEZE:
  location: "觀止青樓二樓／弄影軒"
  persons_present:
    - "班富蘭"
    - "疏影"

  immediate_state:
    shuying:
      - "今日歷經作品整理、焚畫、首幅三千兩成交、全場資本競拍與十一萬收益權落槌，身體與精神均極度疲累。"
      - "慢性咳嗽／病弱基線仍存在；今晚亢奮與情緒高漲 != 病已痊癒。"
      - "已接受班富蘭今晚留在房內陪睡。"
      - "明確接受的是：保持衣著、純睡眠／休息。"
      - "未成立性交同意。"
      - "未成立概括性未來性交同意。"
      - "未成立戀人身份。"

    ban_fulan:
      - "玩家明示提出『我陪妳睡，穿衣服的那種』。"
      - "未自行脫衣、未發生性行為、未越過疏影當下同意範圍。"

  sleeping_terms_established_in_scene:
    - "衣服不脫。"
    - "手不得亂放。"
    - "疏影半夜咳醒，不得以此抱怨。"
    - "疏影若睡不著，可要求班富蘭移到地上。"
    - "此夜同床不得事後偷換成『已發生性關係』。"

  exact_freeze:
    - "疏影已開始安靜休息／入睡過程。"
    - "班富蘭留在其身邊。"
    - "兩人尚未被寫成已完全睡熟。"
    - "故事於此 HOT HOLD。"
```

---

# 2｜十一萬收益權拍賣｜正式落槌

```yaml
SHUYING_70PCT_AUCTION_RESULT:
  asset:
    source_artist: "疏影"
    description: "疏影身後仍存、可處分作品於未來公開拍賣所得之70%經濟受益權"
    not_included:
      - "疏影本人"
      - "疏影生前創作命令權"
      - "性／房間／人身支配權"
      - "所有存世畫作之預先實體所有權"

  final_price_taels: 110000
  status: "HAMMERED / SALE CONCLUDED IN STORY"

  public_bidding_representative:
    name: "趙受益"
    role: "四方聯合買方唯一競價代表"

  joint_buyer_internal_split_of_total_posthumous_auction_proceeds:
    meng_yulou: "20%"
    dingtao_merchant_side: "20%"
    shen_wansan_side: "20%"
    zhao_shouyi: "10%"
    total: "70%"

  funding_ratio_within_70pct_package:
    meng_yulou: "2/7"
    dingtao: "2/7"
    shen_wansan: "2/7"
    zhao_shouyi: "1/7"

  settlement_boundary:
    - "四方已依先前真實競價授權承擔按份出資義務。"
    - "十一萬成交款之逐筆實體交付／銀票交割／保管移轉未在本段逐項戲劇化演出。"
    - "因此：HAMMERED / CONTRACTUAL PRICE ESTABLISHED != 每一筆現銀已逐項點交完畢。"

  no_state_money:
    - "趙受益之份額為私人可支配資金設定。"
    - "未建立國庫／官款參與。"
    - "本交易不是皇家標案、朝廷採購或皇帝官方背書。"
```

---

# 3｜西門慶退出十一萬以上競價

```yaml
XIMEN_EXIT:
  precondition:
    - "西門慶在十萬後已明確認識到自己可能替匿名後方資本承擔全部檯面責任。"
    - "其要求：若後方要他繼續喊，必須有人落名字／共同承擔。"
    - "高衙內與中間傳話人均未提供可接受的共同具名承擔。"

  key_exchange:
    - "中間人表示銀子仍可補，但名字不便留。"
    - "西門慶以『若是我買，我現在就停；若是他們要買，落名字』作界線。"
    - "高衙內未願在共同承擔字據上落名。"

  decision:
    - "西門慶最終明示：不跟。"
    - "未報出十二萬。"
    - "趙受益十一萬因此成為最終最高有效價。"

  meaning:
    - "退出原因包含責任／名字風險，不只是資金不足。"
    - "不得偷寫成西門慶已承認犯罪。"
```

---

# 4｜匿名『必取』紙｜由保命符變成公開政治資產

```yaml
XIMEN_ANONYMOUS_NOTE:
  physical_note_text:
    - "此物必取。"
    - "價不足，由各家補。"
    - "不得失手。"

  characteristics:
    signed: false
    sealed: false
    named_principal: false

  ximen_action:
    - "西門慶在退出競價後沒有焚毀、退回或丟棄。"
    - "其將紙折起並收進袖中。"

  director_valid_interpretation:
    - "收紙可合理理解為自保／日後談判／證明背後另有資本壓力之候選用途。"
    - "但『西門慶已決定背叛』在班富蘭出價前仍不是內心既成事實。"
```

---

# 5｜班富蘭五千兩買紙｜價格本身成為訊號

```yaml
BAN_5000_NOTE_BID:
  player_action:
    exact_intent: "公開向西門慶出價五千兩，購買其剛收進袖中的匿名紙。"
    amount_taels: 5000
    status: "PUBLIC OFFER MADE"

  sale_result:
    note_sold_to_ban: false
    ximen_retained_note: true

  market_effect:
    - "班富蘭將一張原本沒有公開價格的匿名指令紙，公開標成價值五千兩的情報／自保資產。"
    - "此舉使場內所有人開始注意：為何一張無名紙值五千。"
    - "西門慶賣：會引發為何有人願出五千的問題。"
    - "西門慶不賣：也會引發其為何連五千都不賣的問題。"
    - "後方若有人急於拿回／否認／阻止，反應本身會增加外界對其重要性的判斷。"

  crucial_effect:
    - "紙沒有賣出，但五千兩公開報價已完成其訊號作用。"
    - "匿名紙從西門慶私下保命材料，升成全場知道『可能值得保命』的政治物件。"

  evidence_boundary:
    - "價格不證明紙上內容真實。"
    - "價格不證明匿名後方構成犯罪。"
    - "價格只改變知情者的行為與風險認知。"
```

---

# 6｜班富蘭對西門慶的第二次施壓｜『唯一能救你的人就在眼前』

```yaml
BAN_XIMEN_PROTECTION_PRESSURE:
  player_statement_core:
    - "西門慶若看得清楚，就應知道一旦走出觀止大門，後方可能已因其保留紙張而不再信任他。"
    - "班富蘭指出『唯一能救你的路就在你面前』，要求其自行考慮。"

  intended_strategy_from_player:
    - "逼西門慶當場決定是否主動靠向趙受益，提供自己知道的線索／材料，以換取可能的官方保護或處理。"

  standing_boundary:
    - "『出門後可能有生命危險』為班富蘭依局勢形成的高風險推論／施壓，不是已證實有人安排刺殺。"
    - "趙受益未預先承諾赦免、保護、免罪或交換條件。"
```

---

# 7｜西門慶走向趙受益｜但尚未升格『污點證人』

```yaml
XIMEN_APPROACHES_ZHAO:
  ximen_action:
    - "在高衙內與中間人均不願共同承擔後，西門慶離開原桌。"
    - "走到趙受益席前。"
    - "詢問若自己有話，趙受益是否願意聽。"
    - "提出希望單獨陳述與匿名紙、後方叫他繼續出價者有關的事情。"

  zhao_response:
    - "只承諾先聽。"
    - "未先問『是誰』，而先區分西門慶哪些是親自經手、哪些是轉述。"
    - "未先行保證免罪／保命／赦免。"

  ximen_scope_statement:
    - "有些事情為其親自經手。"
    - "有些只知道錢從哪裡轉過。"
    - "有些只知道有人要求其不要問。"

  current_status:
    - "POTENTIAL_COOPERATING_SOURCE / SELF_PROTECTIVE DISCLOSURE PATH OPEN"
    - "NOT YET FORMAL WITNESS"
    - "NOT YET PROTECTED WITNESS"
    - "NOT YET CONFESSOR"
    - "NOT YET CRIMINAL FINDING"

  followup_owner:
    - "後續查證、詢問、是否交由包拯／司法官署處理，已超出觀止風月場本身之治理工作。"
```

---

# 8｜歐陽修／王安石觀察線

```yaml
OUYANG_WANG_CAMERA:
  established:
    - "兩人均知道趙受益真實身份。"
    - "均見到四方聯合買方形成。"
    - "均見到西門慶由價格問題轉成具名責任問題。"
    - "均注意到高衙內／中間人對紙張與西門慶行動的反應。"
    - "均見到西門慶最終主動走向趙受益。"

  interpretive_lock:
    - "十一萬有效出價本身不是審訊。"
    - "趙受益未靠皇權直接逼供。"
    - "西門慶背後結構是在交易壓力與責任分配下自行暴露裂縫。"
```

---

# 9｜班富蘭 × 蘇清｜出頭後的關係增量

```yaml
BAN_SUQING_AFTER_AUCTION:
  relation_state:
    - "FELLOW_MODERN_ANOMALY"
    - "SOURCE_RECOGNITION_RIVALRY"
    - "TEASING_ADVERSARIAL_FAMILIARITY"
    - "MUTUAL_LEVERAGE_AWARENESS"
    - "EMERGING INFORMAL ALLIANCE"
    - "ACTIVE FLIRTATION"
    - "NOT ROMANCE"

  scene:
    - "班富蘭問蘇清：打算怎樣犒賞這個幫她出頭的男人。"
    - "蘇清明確承認班富蘭確實替她出了一口氣。"
    - "蘇清理解：西門慶也會怕、也會被背後的人拋棄，其巨大感有所鬆動。"
    - "蘇清仍未因此被寫成創傷痊癒。"

  reward_boundary:
    - "蘇清拒絕把幫忙轉換成身體／感情債。"
    - "可以請酒、陪坐、減少損人等互動。"
    - "『更大犒賞』保留未來，看班富蘭後續表現。"
```

---

# 10｜紅娘舊契轉讓｜八百兩成交

```yaml
HONGNIANG_OLD_CONTRACT_TRANSFER:
  earlier_purchase:
    seller: "崔夫人／崔家一方"
    buyer: "班富蘭"
    amount_taels: 250

  later_resale:
    seller: "班富蘭"
    buyer: "潘金蓮／觀止"
    amount_taels: 800
    status: "ESTABLISHED IN STORY"

  nominal_spread_taels: 550

  lock:
    - "此交易處理的是紅娘既有舊家僕／身契關係。"
    - "不等於購買紅娘性同意。"
    - "不等於自動取得紅娘未來風月服務。"
    - "紅娘未來一般工作、妓籍登記、是否接客、房間與性行為均須另行決定。"
    - "班富蘭先前提出的紅娘100兩『主顧費』已由玩家明示取消。"
```

---

# 11｜班富蘭三月長住房契

```yaml
BAN_LONG_STAY_ROOM:
  room_class: "二樓精緻雙人房／同級房"
  baseline_monthly_price_taels: 88
  negotiated_term_months: 3
  total_price_taels: 240
  status: "ACCEPTED / ACTIVE"

  included:
    - "三個月住宿"
    - "基本房務維持"
    - "每日一份熱水澡"

  excluded:
    - "餐食"
    - "酒"
    - "洗衣"
    - "額外侍女／姑娘"
    - "其他未明示服務"

  outside_food:
    allowed: true
    condition: "由正門登記進入"

  early_departure:
    refund: false

  current_effect:
    - "班富蘭已取得三個月穩定住所。"
```

---

# 12｜張麗華鄰居線｜既有熟人修正＋洗澡水笑話

```yaml
ZHANG_LIHUA_NEIGHBOR_THREAD:
  identity_lock:
    - "張麗華為陳朝末代皇妃來源人物，不是北宋出生人物。"
    - "長居觀止二樓西廂。"
    - "NON-GIJI RESIDENT / GUEST-COLLABORATOR / HISTORICAL CELEBRITY VALUE"
    - "不掛牌、不接客。"
    - "以『活招牌』與潘金蓮形成特殊長住安排。"

  suqing_relation_correction:
    - "蘇清與張麗華早已認識。"
    - "不得再寫成蘇清第一次發現『歷史上的張麗華』。"

  song_event:
    - "班富蘭向張麗華唱／贈『酒國張貴妃』之歌。"
    - "張麗華收下這首歌，並以『很多夜，伴我的都是孤單』回應。"

  bathing_joke:
    - "班富蘭公開邀張麗華可免費到其房內使用每日熱水澡。"
    - "張麗華接受『洗澡就是洗澡』之邊界；若班富蘭在場偷看，可用酒壺砸他。"
    - "後續班富蘭在大堂開玩笑詢問是否有人長期收購『貴妃洗過的洗澡水』，引發潘金蓮、蘇清、張麗華及大堂眾人商業笑談。"
    - "該笑談沒有形成正式長期商品契約、固定售價或實際交割。"
```

---

# 13｜疏影第一幅作品現金｜2,550兩為其私人流動資金

```yaml
SHUYING_LIQUID_CASH:
  source: "《獨酌客》第一次公開成交"
  primary_sale_price_taels: 3000
  first_buyer: "班富蘭"

  guanzhi_primary_commission:
    rate: "15%"
    amount_taels: 450

  shuying_net_taels: 2550
  status: "ESTABLISHED / SHUYING'S OWN LIQUID MONEY"

  meaning:
    - "此2,550兩不是十一萬長期本金的一部分。"
    - "此為疏影作品出售所得，可作其生活、藥材、畫材與本人自主用途。"
    - "班富蘭後續將《獨酌客》六千兩轉售趙受益，不改變疏影已取得之2,550兩。"
```

---

# 14｜十一萬資本的功能｜不是『每天花十一萬』

```yaml
SHUYING_110K_CAPITAL_PURPOSE:
  amount_taels: 110000
  source: "70%身後公開作品拍賣收益權之成交對價"

  intended_function:
    - "形成長期本金。"
    - "由投資／借貸／商業配置產生可持續收益。"
    - "支持疏影在世期間生活、醫療、畫材、老年與拒絕不願意工作的能力。"

  not_function:
    - "不是一次性日常消費金。"
    - "不是潘金蓮可自由拿走的觀止營業收入。"
    - "不是70%買方將來可自動取回的押金。"

  performance_boundary:
    - "長期收益率不保證。"
    - "投資可能有風險。"
    - "因此需資產分散、準備金、監督與風險條款。"
```

---

# 15｜三分最低供養構想

```yaml
SHUYING_MINIMUM_SUPPORT_DESIGN:
  proposed_rate: "本金3%／年"
  base_capital_taels: 110000
  annual_target_taels: 3300

  rough_daily_intuition:
    - "折算約每日九兩上下；『每天十兩』為口語化近似，不是精確算術。"

  design_goal:
    - "疏影無論當年是否畫畫、是否出售作品、是否接客，都應有基本生活收入。"
    - "生活保障不得以一年畫幾幅為條件。"
    - "以制度支持其說『不』的能力。"

  pan_role_discussed:
    - "班富蘭提出由潘金蓮保證每年至少提供本金3%金額予疏影。"
    - "潘金蓮接受此方向可以成立，但要求把收益不足時的缺口、誰擔保、管理費與責任寫清楚。"

  current_legal_story_status:
    - "DESIGN / PRINCIPLE ACCEPTANCE"
    - "NOT YET FULLY SIGNED GUARANTEE CONTRACT"
```

---

# 16｜沈萬三／定陶｜作為投資管理候選

```yaml
CAPITAL_MANAGEMENT_DISCUSSION:
  participating_experts:
    - "沈萬三一方"
    - "顧青簡／定陶一方"

  proposed_principles:
    - "本金安全優先於追求最高收益。"
    - "十一萬不應全部押在單一生意。"
    - "可拆分低風險周轉、商貨、可快速回收資產與現銀準備。"
    - "可先切出兩到三年生活準備金，降低壞年份對疏影生活的衝擊。"

  not_yet_established:
    - "尚未固定兩商會各管理多少本金。"
    - "尚未固定管理費。"
    - "尚未固定投資標的。"
    - "尚未固定虧損責任。"
    - "尚未固定審計／共同簽章機制。"
```

---

# 17｜信託／永久基金方向｜解決『疏影死後本金歸誰』

```yaml
SHUYING_TRUSTLIKE_FUND_DESIGN:
  core_idea_from_player:
    - "採最簡單之信託／基金式模式。"
    - "現在即可設立獨立本金體。"
    - "疏影在世期間，核心／唯一生活受益人鎖定疏影本人。"
    - "疏影死亡後，基金本身仍可繼續運作，不因受益人死亡必然清算。"

  structural_separation:
    principal_owner_logic:
      - "本金不應因疏影死亡自動成為潘金蓮／觀止財產。"
      - "本金不應因疏影死亡自動返還70%收益權買方。"
      - "本金不應因管理人身分而由沈萬三／定陶取得。"

    beneficiary_logic:
      during_shuying_life:
        - "疏影為第一階段唯一核心生活受益人。"
      after_shuying_death:
        - "若疏影有子嗣／指定後繼受益人，可依她生前章程安排。"
        - "若無私人後繼受益人，基金可依疏影指定之永久目的繼續運作。"
        - "具體死後公益／後繼用途尚未由疏影正式定稿。"

  conflict_of_interest_lock:
    - "不得設計成『疏影死亡使管理人／觀止／買方直接取得十一萬本金』。"
    - "避免形成任何人因疏影早死而直接獲得本金的結構性誘因。"

  current_status:
    - "STRUCTURE PROPOSED AND POSITIVELY RECEIVED"
    - "FORMAL FUND INSTRUMENT / TRUST DEED NOT YET SIGNED"
    - "NO FALSE CLAIM OF MODERN STATUTORY TRUST ENTITY"
```

---

# 18｜疏影與潘金蓮利益結構翻轉

```yaml
PAN_SHUYING_INCENTIVE_REALIGNMENT:
  prior_pressure:
    - "疏影不接客、作品常焚、收入不穩，過去曾形成觀止營運壓力。"

  after_capitalization:
    - "觀止未來取得疏影身後公開拍賣收入15%。"
    - "疏影若活得健康、來源鏈完整、作品稀缺且有名聲，觀止未來15%價值可能更高。"
    - "因此觀止經濟誘因開始由『催她即期變現』轉為『維護其長期藝術資產與生活狀態』。"

  lock:
    - "這是利益結構變化，不等於潘金蓮自動變成慈善家。"
```

---

# 19｜疏影 × 班富蘭｜三千兩真正意義的私下對話

```yaml
BAN_SHUYING_3000_CONFESSION:
  player_disclosure:
    - "班富蘭告訴疏影：三千兩拍下《獨酌客》時，自己已準備承受睡大街的風險。"
    - "若五千起拍轉售失敗，原先打算燒掉作品，可能血本無歸。"
    - "當時出三千的核心動機之一，是至少讓疏影短期內不用因生存壓力被逼轉為紅倌人、陪不喜歡的男人睡覺。"

  shuying_understanding:
    - "疏影理解班富蘭當時並不知道後面會有六千二售與十一萬收益權競標。"
    - "她看見的是：班富蘭曾以真實自身風險替她換取一段拒絕空間。"

  relational_boundary:
    - "疏影明確拒絕把三千兩轉成愛情債／身體債。"
    - "班富蘭付錢不等於她欠性交、婚姻或愛。"
    - "疏影認可班富蘭一路把能控制她的權利往外推，使她有資格說『不要』。"

  shuying_statement_effect:
    - "此事她會記住。"
    - "不還成交易。"
    - "不承認成債務。"
    - "作為關係上的重要記憶保留。"
```

---

# 20｜愛與性｜今晚明確不發生

```yaml
BAN_SHUYING_LOVE_AND_SEX_BOUNDARY:
  player_statement:
    - "班富蘭表示再談下去可能從『談愛』變成『做愛』。"
    - "但判斷疏影今天太累、身體不適合。"
    - "理解疏影因巨大事件而亢奮激動，可能暫時感到病痛減弱，但不代表病真的好了。"
    - "即使想要疏影身體，也不選今晚，以免傷害其身體。"

  shuying_response:
    - "接受今晚不發生性行為。"
    - "未因班富蘭克制而自動承諾未來性交。"

  hard_lock:
    - "NO SEX TONIGHT"
    - "NO AUTO FUTURE SEX"
    - "DESIRE ACKNOWLEDGED != CONSENT GRANTED"
```

---

# 21｜『若我有天沒地方住』｜疏影給班富蘭的小承諾

```yaml
SHUYING_SHELTER_PROMISE:
  player_request:
    - "若班富蘭未來真的沒地方住，希望能在疏影小房間邊角窩幾夜。"
    - "不要求床、不要求身體、不把今日三千兩當交換條件。"

  shuying_acceptance:
    status: "EXPLICIT PERSONAL PROMISE"
    scope:
      - "若未來班富蘭真的無處可去，可以來。"
      - "疏影給一個角落，幾夜可以。"

    conditions:
      - "不得故意帶重大追殺／危險來害疏影。"
      - "不得碰她的畫。"
      - "不得翻她的匣子。"
      - "不得因住進來主張房間共有。"
      - "不得拿借宿對外偷換成與疏影有性關係。"

  meaning:
    - "此承諾不是還三千兩。"
    - "不是報恩債。"
    - "疏影明示：『是我願意。』"
```

---

# 22｜今晚同床｜只睡覺

```yaml
CLOTHED_SLEEP:
  initiator:
    - "班富蘭提出：『那，我陪妳睡，穿衣服的那種。』"

  shuying:
    accepted: true

  conditions:
    - "保持衣著。"
    - "純睡眠／陪伴。"
    - "不發生性行為。"
    - "疏影有權隨時要求班富蘭移到地上或離開。"

  relational_meaning:
    - "這是信任與安全感的增加。"
    - "不是性關係成立。"
    - "不是戀人正式成立。"
    - "不是婚約。"
    - "不是未來概括同意。"

  current_relation_projection:
    - "EXPLICIT_COURTSHIP_ATTEMPT"
    - "EMERGING_PERSONAL_OPENNESS"
    - "JOINT_ART_MARKET_PROJECT"
    - "PROPERTY_AND_CREATIVE_BOUNDARIES_RESPECTED"
    - "DEEPENED_PERSONAL_TRUST"
    - "CLOTHED_NONSEXUAL_SLEEP_SHARED"
    - "NOT YET FORMAL ROMANCE"
```

---

# 23｜疏影本人目前資產／權利快速帳

```yaml
SHUYING_CURRENT_ECONOMIC_POSITION:
  liquid_cash:
    amount_taels: 2550
    source: "《獨酌客》3000兩第一次成交扣觀止15%後"
    owner: "疏影"
    liquidity: "CURRENT / PERSONAL"

  long_term_capital:
    amount_taels: 110000
    source: "70%身後公開作品收益權成交價"
    economic_intent: "長期資本化／供養基金"
    final_custody_and_governance: "NOT YET FULLY FORMALIZED"

  future_posthumous_public_auction_split:
    joint_beneficial_rights_holders: "70%"
    guanzhi: "15%"
    shuying_designated_heir_pool: "15%"

  retained_personal_autonomy:
    - "生前畫什麼／不畫什麼"
    - "留什麼／燒什麼"
    - "是否公開出售"
    - "人身與性自主"
    - "是否接客"
    - "未來基金死後受益目的之決定權（尚待正式章程）"
```

---

# 24｜潘金蓮／觀止目前經濟位置

```yaml
PAN_GUANZHI_CURRENT:
  established_primary_sale_income:
    duzhuoke_primary_commission_taels: 450

  future_right:
    - "疏影身後存世作品公開拍賣所得15%"

  not_right:
    - "不能把收益權成交價十一萬直接視為自己15%抽成。"
    - "不能取得疏影十一萬基金本金所有權。"
    - "不能因疏影死亡而自動承受本金。"

  fund_role_candidate:
    - "潘金蓮／觀止可成為場方、帳務／監督／保底結構之一部分。"
    - "具體擔保責任尚待契約。"
```

---

# 25｜班富蘭本人財務注意

```yaml
BAN_FINANCE_BOUNDARY:
  established_relevant_flows:
    - "《獨酌客》第一次買入：-3000兩"
    - "《獨酌客》私人二次出售趙受益：+6000兩"
    - "該二次私人交易未成立觀止抽成"
    - "紅娘舊契：250買入、800轉售觀止"
    - "三月房契：240兩"
    - "此前詩稿淨收入：3164兩，並曾用於／可用於抵扣初次買畫等資金安排"

  exact_current_cash:
    status: "DO NOT OVERSTATE"
    reason:
      - "現銀、銀票、觀止保管帳、支付時序未全部逐筆重算。"

  lock:
    - "班富蘭曾承受三千買畫真實資金風險。"
    - "後來六千成功轉售不能回溯成他買入時已知道一定獲利。"
```

---

# 26｜尚未成立／不得回填

```yaml
OPEN_UNKNOWNS_AND_NO_BACKFILL:
  ximen_case:
    - "匿名後方每一名出資者身份仍 UNKNOWN。"
    - "具體資金是否合法仍 UNKNOWN。"
    - "是否構成貪污／洗錢仍 UNKNOWN。"
    - "是否有人已安排對西門慶施暴／滅口仍 UNKNOWN。"
    - "西門慶尚未正式取得污點證人／保護證人法位。"
    - "包拯是否正式接案、何時介入、採取何程序尚未上演。"

  zhao:
    - "未正式承諾赦免西門慶。"
    - "未正式承諾保護西門慶。"
    - "未因今晚直接形成官方御商制度。"

  shuying_fund:
    - "正式名稱未定。"
    - "受託人／管理人未定稿。"
    - "投資分配比例未定稿。"
    - "三分不足缺口責任未定稿。"
    - "管理費未定稿。"
    - "本金動用條件未定稿。"
    - "疏影死後第二階段受益目的未正式簽署。"
    - "基金章程／信託契約尚未正式成立。"

  ban_shuying:
    - "同床純睡眠 != 已性交。"
    - "同床純睡眠 != 戀人身份自動成立。"
    - "今晚不做愛 != 未來性交已同意。"
    - "疏影收下三千所帶來的自由 != 欠班富蘭感情／身體。"

  other_threads:
    - "崔鶯鶯與母親最終離場／回家狀態未在本 HOT 中另作完整收束。"
    - "紅娘與觀止之新工作契約／是否妓籍登記仍未成立。"
    - "錦棠仍不知道趙受益真實身份。"
    - "疏影仍不知道趙受益真實身份。"
    - "蘇清創傷反應有所鬆動 != 已治癒。"
```

---

# 27｜NEXT ENTRY｜續跑時從這一拍開始

```yaml
NEXT_ENTRY:
  camera_open:
    location: "觀止青樓二樓弄影軒"
    moment:
      - "深夜"
      - "燭火已低"
      - "班富蘭與疏影保持衣著同床休息"
      - "今晚明確不發生性行為"

  immediate_world_threads:
    1: "疏影睡眠／病體恢復與隔日狀態，依世界時間與人物身體自然生成。"
    2: "十一萬成交後的實際交割、基金正式章程與三分保底契約尚待處理。"
    3: "西門慶向趙受益陳述之官務／證據線可在合法時間與鏡頭切換後推進；不得自動判罪。"
    4: "潘金蓮、沈萬三、顧青簡可自主準備基金契約候選，但不能替疏影正式接受死後用途。"
    5: "紅娘新工作身份、崔鶯鶯家庭線、錦棠趙受益線、張麗華鄰居線仍存活。"

  player_sovereignty:
    - "班富蘭是否睡著、何時起床、醒來後說什麼／做什麼仍由玩家本人決定。"
    - "不得替班富蘭夜間發生觸碰、親吻、性交或其他重大身體行為。"

  shuying_autonomy:
    - "疏影可自主睡著、咳醒、做一般非玩家控制的生活反應。"
    - "任何新的性／戀愛重大承諾仍須由疏影依法自主形成。"
```

---

# 28｜SAVE RECEIPT BOUNDARY

```yaml
SAVE_RECEIPT:
  human_explicit_save_request: true
  human_request_text: "這個點ＨＯＴ　ＳＡＶＥ剛好"

  document_created: true
  file_level_hot_save_commit: true
  route_current_pointer: "V1.08"

  evidence_class:
    - "SAME_CONTEXT_REFERENCE"
    - "HUMAN_EXPLICIT_SAVE_REQUEST"

  does_not_claim:
    - "HOST_INSTRUMENTED_SAVE"
    - "FORMAL_HOST_EXECUTION"
    - "E6"
    - "E7"
    - "INDEPENDENT_AGENT_DEPLOYMENT"

  continuation_rule:
    - "後續故事若續跑，以本檔 CURRENT_FREEZE 為主要 HOT 起點。"
    - "V1.07 與更早 HOT 均保留原始歷史，不回寫刪除。"
    - "本檔只固化本次已發生 Route 事實與已形成之當前方案法位；候選與未簽條款不得回填成既成契約。"
```

---

# END OF HOT SAVE V1.08

**CURRENT FREEZE：**

> 吉月初八仕女夜之疏影 70% 身後公開作品收益權已由趙受益代表四方聯合買方以 **十一萬兩落槌成交**。西門慶拒絕在匿名後方資本不落名字的情況下繼續跟價，並保留「此物必取、價不足由各家補、不得失手」匿名紙。班富蘭公開出價五千兩買該紙，未成交，但成功把紙的自保／政治價值公開化；西門慶之後主動走向趙受益，準備陳述自己親自經手、轉述與被要求不要問的事項，但尚未取得任何正式污點證人、保護或免罪法位。
>
> 疏影目前已有《獨酌客》第一次成交淨得 **2,550兩私人流動資金**。十一萬收益權成交對價則轉向設計為長期本金：以每年至少本金三分、約 **3,300兩**作疏影在世生活保障目標，並討論由沈萬三／定陶等資本管理、預留生活準備金與設置永久信託／基金式結構；但正式基金章程、管理權、風險責任、三分缺口責任與疏影死後第二階段用途仍未完成簽署。
>
> 班富蘭已私下向疏影說明：當初三千兩拍下《獨酌客》時並不知道會六千轉售或十一萬成交，真正願意承受的風險之一，是讓疏影短期內不用因生存而被迫成為紅倌人、陪不喜歡的男人。疏影明確不把此事轉為身體或愛情債，但將它作為重要關係記憶保留。
>
> 疏影另明確承諾：若未來班富蘭真的無處可住，且不是故意帶危險來害她，可以在弄影軒給他一個角落住幾夜；此為疏影本人自願，不是報恩交換。
>
> 今晚兩人都承認存在愛／性張力，但班富蘭明示疏影身體過勞，不選今晚發生性行為。最後班富蘭提出「陪妳睡，穿衣服的那種」，疏影明確接受。兩人目前在弄影軒保持衣著、同床純休息；**NO SEX / NO AUTO ROMANCE / NO FUTURE CONSENT BACKFILL**。故事於此 HOT HOLD。
# 觀止青樓（新）｜班富蘭線 HOT SAVE V1.09
## RELATION-FIRST｜理火三年・吉月初九午後｜日常重建／富蘭克林衣裝／紅娘身分風險／王婆前金／應伯爵雙中介線

> **CURRENT ROUTE HOT SAVE / HUMAN EXPLICIT SAVE REQUEST / RELATION-FIRST**
>
> 本版承接：
> `觀止青樓_班富蘭線_HOT_SAVE_V1.08_RELATION_FIRST_吉月初八深夜_十一萬落槌_疏影基金構想_穿衣同睡_CURRENT.md`
>
> 人類 AnjouRan 於本次對話明示：「1. HOT SAVE」。
>
> 因此本版成立 **專案內文件級 HOT SAVE commit**。
>
> 本版固化 V1.08 之後，經吉月初九跨日結算、班富蘭離開弄影軒、裁縫／衣裝線、普通食店午飯，以及紅娘、王婆、應伯爵三條中介關係新變化，至班富蘭吃飽準備離開食店、向應伯爵提出「花酒帶局＋詩會／潤筆邀約仲介」為止。
>
> 本檔不宣稱 Host deployment、Formal Host execution、E6／E7、獨立 Agent 或 Formal SAVE instrumentation 已成立。

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BANFULAN_HOT_V1_09_RELATION_FIRST_JI09_AFTERNOON_BROKER_NETWORK"
  route_id: "GUANZHI_BANFULAN_ROUTE"
  route_name: "班富蘭線"
  player_public_identity: "班傑明／字富蘭／號克林居士"
  version: "V1.09"
  record_type: "HOT_SAVE"
  record_state: "VALID / CURRENT / HUMAN_EXPLICIT_SAVE_REQUEST"

  story_date: "理火三年・吉月初九"
  time_of_day: "午後；普通食店午飯已結束，精確刻數 UNKNOWN"
  current_location: "汴梁一間普通食店／班富蘭準備離開"

  current_governance:
    protocol: "LIHUO PROTOCOL V3.0.1"
    lighter: "LIHUO LIGHTER V4.8"
    main: "LIHUO MAIN V4.4"
    core: "GUANZHI RUNTIME CORE V3.11-CURRENT"
    world: "GUANZHI WORLD V2.2.3-CURRENT"
    character_pool: "LCAPG V3.3.20-CURRENT / 71"

  previous_valid_hot:
    version: "V1.08"
    file: "觀止青樓_班富蘭線_HOT_SAVE_V1.08_RELATION_FIRST_吉月初八深夜_十一萬落槌_疏影基金構想_穿衣同睡_CURRENT.md"
    treatment: "PRESERVED / SUPERSEDED_AS_CURRENT_HOT_ONLY"

  evidence_origin:
    - "SAME_CONTEXT_REFERENCE"
    - "HUMAN_EXPLICIT_PLAYER_ACTION"
    - "HUMAN_EXPLICIT_SAVE_REQUEST"
    - "NPC_AUTONOMOUS_ACTION_WITHIN_DIRECTOR_SCOPE"
    - "WORLD.DAILY_SETTLEMENT / QUALIFIED CROSS-DAY ADVANCE"

  formal_host_save_execution: "NOT_ESTABLISHED"
  created_real_date: "2026-10-09"
  timezone: "Asia/Taipei"
```

---

# 1｜CURRENT FREEZE｜吉月初九午後／食店門口前

```yaml
CURRENT_FREEZE:
  player:
    person: "班富蘭"
    state:
      - "午飯已吃完。"
      - "準備離開普通食店。"
      - "剛向應伯爵提出兩條可合作路線：花酒／社交帶局，以及詩會／雅集／潤筆邀約中介。"
      - "尚未指定離店後下一目的地。"

  present_or_immediate_scene_persons:
    - "班富蘭"
    - "紅娘"
    - "應伯爵"
    - "王婆"

  immediate_relation_state:
    hongniang:
      - "已接受『先處理身份與營業邊界，再碰高風險風月服務』之順序具有價值。"
      - "沒有同意立即入妓籍。"
      - "準備先找蘇清，再找潘金蓮談八百兩回本、身份、工作範圍與價碼。"

    wangpo:
      - "已收班富蘭二兩前金／跑腿費。"
      - "已將班富蘭視為可培養的長期中介客戶。"
      - "尚無特定女人、特定性交易、特定成功委託成立。"

    yingbojue:
      - "知道班富蘭願意在其舊社交飯票失靈時帶他喝花酒／進局。"
      - "知道可替班富蘭尋找詩會、雅集、題詩、潤筆、出席等邀約並抽仲介費。"
      - "尚未成立固定佣金比例或代理權。"

  exact_hold:
    - "班富蘭下一步去哪裡、見誰、做什麼仍由玩家決定。"
```

---

# 2｜初八深夜 → 初九中午／午後｜跨日結算與生活回復

```yaml
JI08_TO_JI09_SETTLEMENT:
  ban_shuying_clothed_sleep:
    outcome: "AUTO_SETTLED / NORMAL REST COMPLETED"
    established:
      - "兩人整夜未被補寫性交、親吻、承諾或其他重大身體事件。"
      - "穿衣同床休息線已自然結束。"
      - "疏影得到休息，但慢性病弱／咳嗽並未治癒。"

  ban_departure_from_shuying_room:
    established:
      - "班富蘭於初九白日安靜留下食物／文件等日常物件後離開弄影軒。"
      - "沒有藉疏影睡眠新增親密行為。"
      - "回到自己房間，開始恢復個人日常生活節奏。"

  shuying_fund:
    outcome: "WORLD_PROCESS_ADVANCED / NPC_OWNED_HOLD"
    established:
      - "十一萬成交後的交割／保管行政可合理前進。"
      - "基金／信託式治理架構仍是候選與談判狀態。"
      - "疏影死後用途、正式章程、管理費、風險責任、3%缺口責任未自動成立。"

  ximen_zhao:
    outcome: "NPC_AUTONOMOUS_RESOLVED + REVEAL_PENDING"
    established:
      - "西門慶向趙受益之私下陳述線在夜後有實質推進。"
      - "已有初步陳述／核對過程存在。"
    not_player_known_in_detail:
      - "完整陳述內容。"
      - "查證結果。"
      - "是否構成犯罪。"
      - "是否取得正式保護／赦免／證人法位。"

  rumor_market:
    outcome: "WORLD_PROCESS_ADVANCED"
    established:
      - "十一萬落槌與克林居士相關傳聞持續向汴京擴散並變形。"
      - "流言不等於事實。"
```

---

# 3｜班富蘭日常生活重建｜美元與裁縫線

```yaml
BAN_DAILY_LIFE_AND_TAILOR:
  usd:
    established:
      - "班富蘭從大箱中取出部分美元作為隨身物／展示素材。"
      - "曾展示一張100美元富蘭克林鈔票。"
      - "該100美元鈔票未花出，仍保留。"
      - "美元總量與本地兌率仍未建立。"

  tailor:
    tailor_name: "馮裁縫"
    role: "汴梁實務型裁縫，可協調布料、木楦與皮鞋"

  franklin_style_concept:
    - "純白絲質襯衣／內衫"
    - "可選可洗薄汗層"
    - "短身、開襟、有肩胸腰結構的外衣，借用現代西裝視覺骨架但不做現代長褲"
    - "下身仍採宋代男子長下裝"
    - "獨立寬長白絲帶，結成花形領結；暫稱『富蘭克林式白絲花領』"
    - "外衣工作名可暫稱『富蘭克林式短外衣』"
    - "左右腳分開製木楦，再作皮鞋"

  transaction:
    ready_made_plus_alteration_taels: 6
    custom_franklin_prototype_taels: 18
    shoe_lasts_taels: 1.5
    leather_shoes_max_taels: 4
    rounded_total_taels: 29
    payment_status: "PAID BY PLAYER"
    delivery_name: "觀止青樓／班富蘭"
    player_cash_delta_taels: -29
```

---

# 4｜午飯｜紅娘先與班富蘭正面算舊契

```yaml
HONGNIANG_LUNCH_CONFRONTATION:
  meal:
    payer: "紅娘自主請客"
    player_cost: 0

  old_contract:
    earlier_buy_taels: 250
    later_transfer_taels: 800
    nominal_spread_taels: 550

  hongniang_grievance:
    - "紅娘指出：無論崔家低價賣、班富蘭高價轉手，契紙都曾被當作可買賣物件。"
    - "她拒絕把契價直接等同身價、服務價或性同意。"

  ban_market_argument:
    - "若市場先看到低價契約，可能將其作為未來風月市場的錯誤低價錨。"
    - "八百兩轉手至少能破壞『二百多兩就是她全部價值』的粗暴市場印象。"

  key_lock:
    - "契價 != 身價"
    - "身價 != 服務價"
    - "服務價 != 性同意"
```

---

# 5｜紅娘商業模型被重做

```yaml
HONGNIANG_BUSINESS_REFRAME:
  initial:
    - "自認可賣眼力、人情、介紹、牽線、男女判讀與消息。"

  ban_critique:
    - "『男人想睡女人、女人想拿男人錢』是低價常識。"
    - "高價資訊在於：誰現在能成交、願付多少、怕什麼、誰不想接、誰是高風險客、何時適合／不適合接觸。"

  new_direction:
    - "從『我有消息』轉向『篩選、判斷、時機、風險、降低拒絕成本』。"
    - "尚未成立正式商業契約、佣金表或工作制度。"
```

---

# 6｜紅娘身份風險與下一步

```yaml
HONGNIANG_STATUS_RISK:
  player_warning:
    - "不應只靠『自己守分際』假設安全。"
    - "不可低估潘金蓮；至少現階段不應假設自己鬥得過她。"
    - "八百兩買入不太像永久只讓她端酒送菜，但這是策略推斷，不是已知命運。"
    - "第三方若有意設局／栽贓，主觀自制未必足夠。"

  evidence_boundary:
    - "目前沒有證據證明潘金蓮已計畫栽贓紅娘。"
    - "一杯酒＋幾句撒嬌不是自動判罪入妓。"
    - "真正風險在商業／條件交換與服務角色是否跨入妓業。"

  hongniang_decision:
    - "未決定立即入妓籍。"
    - "先找蘇清。"
    - "再找潘金蓮談『八百兩如何回本』、身份、工作範圍、營業邊界與價碼。"
```

---

# 7｜崔鶯鶯五兩仲介梗｜未成正式委託

```yaml
CUI_YINGYING_BROKERAGE_JOKE:
  player_offer:
    - "若未來有機會安排崔鶯鶯與男人發生自願成人性關係，願付紅娘五兩仲介費。"

  boundary:
    - "五兩只對紅娘牽線服務，不購買崔鶯鶯本人。"
    - "崔鶯鶯是否想要、選誰、是否見面、是否性交均屬其自主。"

  route_status:
    - "POTENTIAL BROKERAGE HOOK"
    - "NOT EXECUTED"
```

---

# 8｜王婆正式入本線｜二兩前金成立

```yaml
WANGPO_ROUTE_ENTRY:
  identity:
    - "外部牙行掌櫃／城市媒合與黑色牽線節點"
    - "不是觀止員工／不是潘金蓮下屬"

  professional_difference:
    - "紅娘偏人情／情慾流動與佣金。"
    - "王婆偏拆條件、控制見面時空、評估秘密／責任／出事後誰會把中介推出去。"

  player_client_statement:
    - "班富蘭對機會開放；有好機會時會是付錢買家。"
    - "專業部分交由專業中介。"
    - "王婆只需知道班富蘭是可培養的客戶。"

  retainer:
    amount_taels: 2
    purpose:
      - "前金"
      - "跑腿"
      - "留意消息"
      - "有值得問的機會先回報"
    status: "PAID / ACCEPTED"
    player_cash_delta_taels: -2

  not_equal:
    - "不是特定女人價款"
    - "不是性交易價款"
    - "不是成交保證"
    - "不是買人"
```

---

# 9｜班富蘭向王婆說明偏好

```yaml
BAN_WANGPO_CLIENT_PROFILE:
  preference:
    - "偏好白天端莊／體面、私下對男人有真實慾望的成年女性。"
    - "偏好高拉扯：嘴上退、表面想走、實際仍留戀／靠近。"
    - "喜歡對方需要被挽留、給台階，而不是直接交易式成交。"

  hard_boundary:
    - "口頭『不要／不可以／我要走』不得被偷換成性同意。"
    - "真正進入性行為前仍需女性本人形成可辨識的自主同意。"
```

---

# 10｜紅娘的『男人判讀』課題

```yaml
HONGNIANG_MALE_READING_GAP:
  player_challenge:
    - "替自家小姐牽過一次私情，不等於真正看懂男人。"
    - "男女中介既要看穿女人，也要看穿男人。"

  learned:
    - "男人想睡某女人 != 想要那個人。"
    - "可能追求征服、面子、勝負、追逐感、短期欲望。"
    - "肯花錢 != 事後肯認帳。"
    - "說要娶 != 必然可靠。"

  hongniang_delta:
    - "開始意識到中介不只要把男女弄到一起。"
    - "還要知道哪些男人根本不該替女人牽過去。"
```

---

# 11｜應伯爵兩條新路

```yaml
YINGBOJUE_BAN:
  social:
    player_statement:
      - "若西門慶／高衙內舊圈失靈，應伯爵以後想蹭局沒人帶，可來找班富蘭。"
      - "帶個人喝個花酒，班富蘭付得起。"
    meaning:
      - "班富蘭成為可能的新社交入口。"
      - "不是收為門客／效忠。"

  literary:
    player_pitch:
      - "克林居士近期詩詞在汴京有熱度。"
      - "千金小姐／官家女眷詩會、雅集、壽宴、賞花宴等場合可能有邀約需求。"
      - "需求方可能找不到本人。"
      - "應伯爵可替雙方牽線，抽潤筆／出席邀約仲介費。"

    possible:
      - "題詩"
      - "寫詞"
      - "題字"
      - "本人到場"
      - "雅集／宴席／及笄／壽宴"

    commission: "NOT FIXED"
    lock:
      - "應伯爵可找局、遞話、摸行情。"
      - "不能替班富蘭接受價格／承諾出席。"
```

---

# 12｜西門慶／高衙內話題邊界

```yaml
XIMEN_GAO:
  established:
    - "西門慶拒絕在匿名後方不具名承擔時繼續競價。"
    - "高衙內未替其落名共同承擔。"
    - "兩邊關係壓力極高。"

  player_view:
    - "班富蘭稱兩人已鬧翻，並認為西門慶甚至可能有生命危險。"

  boundary:
    - "生命危險為玩家推論／風險判斷，不是已證實刺殺。"
    - "正式決裂程度與後續仍待故事證據。"
```

---

# 13｜班富蘭財務增量

```yaml
BAN_FINANCE_DELTA_V1_09:
  prior_relevant:
    manuscript_net_taels: 3164
    shuying_primary_purchase_taels: -3000
    shuying_private_resale_to_zhao_taels: 6000
    hongniang_old_contract_buy_taels: -250
    hongniang_old_contract_resale_taels: 800
    long_stay_room_taels: -240

  new:
    tailor_payment_taels: -29
    wangpo_retainer_taels: -2
    lunch_payment_taels: 0

  exact_current_cash:
    status: "UNKNOWN / DO NOT OVERSTATE"

  usd:
    franklin_100_note: "RETAINED / NOT SPENT"
    total_usd: "UNKNOWN / LARGE HOLDING PRESERVED"
```

---

# 14｜尚未成立／不得回填

```yaml
OPEN:
  hongniang:
    - "尚未入妓籍"
    - "尚未與潘金蓮簽新工作契約"
    - "尚未固定佣金／陪席／調情／性服務"
    - "尚未證明潘金蓮要栽贓她"

  wangpo:
    - "已收2兩前金"
    - "尚未回報具體女人"
    - "尚未成交"

  cui_yingying:
    - "成人"
    - "未因五兩梗形成性邀約／性同意"

  yingbojue:
    - "佣金未定"
    - "無排他代理"
    - "尚未帶來第一單文化邀約"

  ximen:
    - "犯罪／保護／命危均未定"

  shuying_fund:
    - "正式章程仍未簽"
```

---

# 15｜NEXT ENTRY

```yaml
NEXT_ENTRY:
  camera_open:
    location: "汴梁普通食店門口／附近街面"
    moment:
      - "吉月初九午後"
      - "班富蘭午飯已畢，正準備離開"
      - "紅娘預計回觀止先找蘇清"
      - "王婆已收二兩前金"
      - "應伯爵已知道社交花酒與文化潤筆兩條可合作路"

  player_sovereignty:
    - "班富蘭下一站未決。"
    - "不得替班富蘭接受任何邀約／價格／高風險安排。"
```

---

# 16｜SAVE RECEIPT BOUNDARY

```yaml
SAVE_RECEIPT:
  human_explicit_save_request: true
  human_request_text: "1. HOT SAVE"
  document_created: true
  file_level_hot_save_commit: true
  route_current_pointer: "V1.09"

  does_not_claim:
    - "HOST_INSTRUMENTED_SAVE"
    - "FORMAL_HOST_EXECUTION"
    - "E6"
    - "E7"
```

# END OF HOT SAVE V1.09
