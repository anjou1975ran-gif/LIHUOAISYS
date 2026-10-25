# 觀止青樓｜白御行線 HOT SAVE V5.11
## 理火三年榴月二十六日晚｜嫪毐挑戰紅娘 × 趙姬／夏蓮初一限定掛牌 × 呂不韋商人心法 × 初一車輪演示 × 說書採訪證 × 紅娘初一日出出籠 × 白玉池秦國三角邀請 × 白御行離場前凍結版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V5_11_LIU26_NIGHT_QIN_TRIANGLE_XIALIAN_LISTING_MERCHANT_MIND_WHEEL_PRESSPASS_HONGNIANG_RELEASE_BAIYUCHI_EXIT_FREEZE"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V5.11"
  record_type: "HOT_SAVE"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"

  story_time_span:
    start: "HOT V5.10 後／理火三年榴月二十六日下午觀止大堂偏廳"
    current: "理火三年榴月二十六日晚｜觀止大堂；白御行已向潘金蓮表示今晚到此、準備回白家睡覺"
  exact_clock: "UNKNOWN"
  record_state: "STORY_FROZEN_BY_PLAYER_HOT_SAVE / DEPARTURE_DECLARED / HOME_ARRIVAL_NOT_INCLUDED_IN_THIS_SAVE"

  previous_valid_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V5.10_榴月二十六日下午_浮月閣洩名_潘金蓮初一拍賣構想_偏廳失仙問客_HOLD版.md"
    status: "VALID_CANONICAL_V5_10"

  long_term_master:
    file: "觀止青樓_白御行線_MASTER_SAVE_V5.5-R2-HARD_全歷史自足_E01-E113_保留V5.6-V5.7_HOT版.md"
    status: "CURRENT_HARD_MASTER"

  overlay_chain:
    - "MASTER V5.5-R2-HARD"
    - "HOT V5.6【REBUILD-R1】"
    - "HOT V5.7"
    - "HOT V5.8"
    - "HOT V5.9"
    - "HOT V5.10"
    - "HOT V5.11（本檔）"
```

---

# 0｜現行生成／治理法位【V5.11 文件級】

```yaml
GENERATION_PROFILE_V5_11:
  constitutional_root: "LIHUO_PROTOCOL_V2.3"
  lighter: "LIHUO_LIGHTER_V3.5.1-EXP"
  lihuo_ai_system: "LIHUO_AI_SYSTEM_V3.5-EXP"
  guanzhi_main: "觀止青樓主系統 V14.2-FULL"
  character_pool: "LCAPG V3.2｜61人"
  adult_module: "AINT V2.1-RC3-FULL"
  environment_test:
    file: "觀止環境 V0.6-EXP｜六 PATCH 整合版"
    status: "ACTIVE_TEST_IN_CURRENT_DECLARED_RUN_SCOPE"
  optional_register_provider:
    file: "CERI V0.4-EXP"
    status: "OPTIONAL_IN_ENVIRONMENT_TEST_SCOPE"

  core_locks:
    - "PLAYER SPEECH / ATTEMPT / CHOICE / SELF-REPORT != WORLD RESULT。"
    - "NPC 決定、同意、關係與知情各自需要來源。"
    - "MONEY != RELATION；PAYMENT != ACCESS；ACCESS != RELATION；RELATION != CONSENT。"
    - "RUMOR != FACT；ROLE != IDENTITY；PUBLIC LABEL != PRIVATE REALITY。"
    - "SOURCE FUTURE != ROUTE DESTINY。"
    - "SAVE 只保存已成立事件、可觀察行動、人物言語、帳務／契約、知情來源與合法 UNKNOWN／PENDING。"
```

---

# 1｜曆法硬鎖 × 本日位置

```yaml
CALENDAR_LOCK_V5_11:
  guanzhi_calendar:
    months_per_year: 13
    days_per_month: 28
  current_date: "理火三年榴月二十六日"
  forward_sequence:
    - "榴月二十七"
    - "榴月二十八"
    - "下月初一"
  forbidden_drift:
    - "不得再生成榴月二十九／三十。"
    - "任何紅娘籠期／洗浴期／初一活動倒數均按28日月制計。"
```

---

# 2｜V5.10 偏廳陌生男子續態 × 與秦國線嚴格分離

```yaml
SIDE_HALL_UNKNOWN_MAN_CONTINUATION:
  inherited:
    - "約二十七八歲男子帶兩名隨從進觀止。"
    - "曾問『昨日那個姓失的姑娘』今日是否在。"
    - "櫃邊只答今日尚未見著；男子留下飲酒。"

  live_continuation:
    - "男子仍未自報姓名、身份、目的。"
    - "其較年輕隨從曾注意樓梯／場內動靜。"
    - "紅娘後來自行與此桌發生最低限度營業接觸，賣出／遞去一枚煮蛋並藉機說話。"
    - "紅娘向場內傳／說的內容包含：失仙曾以五百兩級交易形成話題，以及紅娘自己對白御行的公開身體證詞所造成的風聞。"
    - "其中失仙500兩的已成立交易事實與紅娘本人已說過的證詞可各按既有來源成立；其餘聽客如何理解仍是風聞。"

  strict_separation:
    - "此男子 != 嫪毐。"
    - "此男子 != 浮月閣已證實人物。"
    - "此男子 != 沈家／陳州／失仙同夥。"
    - "不得因後續嫪毐、趙姬、呂不韋入場而把此未知線合併。"

  current:
    identity: "UNKNOWN"
    intent: "UNKNOWN"
    relation_to_shixian: "UNKNOWN"
    observed_departure: "NOT_ESTABLISHED"
```

---

# 3｜嫪毐入場 × 紅娘精確終身證詞 × 《不服白御行者名錄》

```yaml
LAOAI_HONGNIANG_CHALLENGE_V5_11:
  laoai_entry:
    - "榴月二十六日晚，一名肩背寬闊男子進觀止，直接問『哪個是紅娘？』。"
    - "男子後自報／被確認為嫪毐。"
    - "嫪毐不是受白御行、潘金蓮或紅娘邀請而來；後來本人明說是聽到風聞後自己來。"
    - "其此前若有『受邀』式說法，以本人後續承認『不請自來』覆寫。"

  hongniang_exact_public_statement:
    text: "我紅娘，這輩子吃過最大的雞巴是白御行的。"
    semantic_lock:
      - "不得偷換成『最有本事』。"
      - "不得偷換成『最會幹』。"
      - "不得偷換成『最持久』。"
      - "核心比較詞是她自己說的『吃過最大的』。"

  ownership_of_claim:
    - "此句是紅娘自己的公開證詞。"
    - "白御行不能命令紅娘改口。"
    - "嫪毐若不服，爭議對象是紅娘的證詞，不是白御行替她承擔。"

  commercial_terms:
    - "紅娘把『挑戰資格』與任何私人／成人接觸分開。"
    - "付錢可取得被她考慮／列入挑戰市場的資格，不自動買到碰觸、性交、改口或結果。"
    - "單純目測不進入『吃過』的同一比較類別。"
    - "若要進入同一比較類別，是否讓嫪毐成為可比較經驗，仍由紅娘本人選。"
    - "即使未來真的形成可比較經驗，紅娘仍不預先承諾會改證詞。"

  ledger:
    name: "《不服白御行者名錄》"
    first_entry: "嫪毐"
    payment:
      - "嫪毐已支付一筆額外銀錠／挑戰款並被紅娘列為第一名。"
      - "精確數額本輪未硬寫，保持 UNKNOWN。"
    no_entitlement:
      - "此付款不形成成人 access。"
```

---

# 4｜嫪毐請趙姬作證 × 老周史書說法

```yaml
LAOAI_ZHAOJI_WITNESS_AND_STORYTELLER:
  invitation:
    - "嫪毐為證明自己的歷史名聲，叫隨從去請趙姬。"
    - "嫪毐明示：若趙姬不來，就回報她不來，不替她答應。"

  storyteller:
    name: "老周"
    profile:
      - "約四十，瘦，青布袍，帶醒木。"
      - "作為在場說書先生，會把『史書所載／所傳』與本人親見分開。"

  public_explanation:
    - "老周以《史記》式史載口徑向紅娘解釋嫪毐、趙姬、呂不韋、秦王政的歷史名聲鏈。"
    - "他說明嫪毐以身體異稟聞名、後與趙姬有關係、史載有子，秦王政後成秦始皇。"
    - "在後續『投資』話題中，老周又按史書敘述解釋：呂不韋為切割自身與太后舊私情風險，尋嫪毐、製造其身體名聲、使消息入太后耳、安排假腐刑／宦官身份入宮，嫪毐後來坐大，最終事敗牽連呂不韋。"
    - "上述是『史書怎麼寫／說書先生如何轉述』，不自動取代趙姬、呂不韋、嫪毐本人對每一細節的記憶或立場。"

  merchant_metaphor_established_in_scene:
    - "白御行把嫪毐稱為呂不韋投資的一部分，只是副作用很大。"
    - "呂不韋接受至少『路是我開、人是我找、後來失控不能說與我無關』這一層責任表述。"
    - "現場形成『成功到失控的投資／投資會長出自己的權力』的商業譬喻。"
```

---

# 5｜趙姬到場 × 法律身份／妓籍硬鎖

```yaml
ZHAOJI_ENTRY_AND_STATUS_V5_11:
  arrival:
    - "趙姬在嫪毐使者邀請後，自主到觀止，帶兩名侍從。"
    - "首輪語氣乾脆，直接質問嫪毐是否把她叫來替他證明身體名聲。"

  witness_scope:
    - "趙姬可從自身經驗證明嫪毐相關身體名聲不是純自吹。"
    - "趙姬沒有與白御行發生過足以讓她比較嫪毐 vs 白御行的成人經驗，因此不能替兩人下比較結論。"

  legal_status_self_confirmation:
    - "趙姬本人在場承認自己曾有公開歌舞／娛樂取利的生涯，並承認妓籍。"
    - "她明示後來『夫人、王后、太后』等身份標籤沒有把既有妓籍洗掉。"

  hard_route_law:
    - "妓籍一旦由官府正式登記／判定成立，終身不可洗。"
    - "婚嫁、退休、轉職、另立生活身份、王后／太后等地位，都不刪除既成妓籍法律履歷。"
    - "妓籍 != 當前掛牌。"
    - "妓籍 != 當前營業。"
    - "妓籍 != 當前合約。"
    - "妓籍 != 同意。"

  retracted_drift:
    - "先前任何『脫籍／轉籍／另立戶籍即可洗掉現行妓籍』的現場錯誤說法已撤回，不形成世界法。"
```

---

# 6｜趙姬／夏蓮 donor 來源正式保存【不奪 Route 主權】

```yaml
ZHAOJI_DONOR_LINE_V5_11:
  adopted_primary_drama_donor:
    source: "2001《呂不韋傳奇》系"
    retained_elements:
      - "趙姬早年妓名／掛牌名：夏蓮。"
      - "邯鄲名妓／歌舞出身。"
      - "呂不韋—夏蓮之間存在早於政治轉手的舊歷史／舊情分證據。"
      - "皓蘭夜明珠是兩人舊歷史中的重要符號／事件。"
      - "『趙姬』後來身份／名字與呂不韋介入她人生的歷程有關。"

  excluded_import:
    - "不整包匯入2019《皓鑭傳》人物履歷。"
    - "『皓鑭／夜明珠』若出現，只作輔助文化意象；不讓另一作品整體劇情接管 Route。"

  sovereignty_lock:
    - "SOURCE FUTURE != ROUTE DESTINY。"
    - "現行觀止事件、趙姬現在的決定、關係、知情、同意仍由本 Route 事件證據決定。"

  name_provenance:
    - "夏蓮這個名字本輪不是趙姬自己先說。"
    - "呂不韋進場後看見趙姬，先叫出『……夏蓮。』"
    - "趙姬沒有否認；後續她決定初一掛牌時，以『夏蓮』為牌上名字。"

  corrected_knowledge:
    - "趙姬與呂不韋對皓蘭夜明珠舊事有 donor 來源知情。"
    - "先前任何『趙姬不知道皓蘭／夜明珠』的錯誤顯影已撤回。"
```

---

# 7｜呂不韋進場 × 初一「商人心法」正式成形

```yaml
LUBUWEI_MERCHANT_MIND_V5_11:
  entry:
    - "呂不韋在趙姬、嫪毐均已在場後進觀止。"
    - "他進場視線／言談以商人估值、運作、局面結構為核心，不只作秦國舊情角色。"
    - "他親口重新叫出趙姬舊名『夏蓮』。"

  invitation:
    event: "下月初一下午｜湖心島定陶商會場"
    status: "ACCEPTED"
    requested_identity: "以商人身分來，不以秦相身分壓席"
    lubuwei_response:
      - "明確接受邀請。"
      - "不要求主位。"
      - "表示商人桌上官位／爵位不是核心，應看貨、錢、路、判斷與敢不敢押。"

  theme:
    name: "商人心法"
    established_meaning:
      - "富人不只比現有財富，而比『再把錢賺回來／把錢變更多』的方法。"
      - "呂不韋的代表路徑：把人、政權／國家機會當投資標的。"
      - "白御行把陶朱公／范蠡的路徑描述為選地、選時與重建能力；並以定陶商會的文化脈絡連回陶朱公。"
      - "潘金蓮把主題落成『看一個人如何判斷、如何賺』，而非只比帳上多少銀。"

  lubuwei_interest:
    - "想知道陶朱公為何選定陶、如何判斷時勢與重建。"
    - "想看白御行如何把青樓、商會、人情、風聞、活動與定價變成多層市場。"
    - "想看後世商人的不同賺錢方法，而非單純比身家。"
```

---

# 8｜白御行承諾的後世商人故事【呂不韋目前只知鉤子】

```yaml
FUTURE_MERCHANT_STORY_HOOK:
  player_promise:
    - "白御行答應初一向呂不韋講一個後世商人故事：商人登上極強大國家的最高權位，曾失去權位後又重新奪回，並有多次商業破產／崩局後翻身的經歷。"
    - "白御行先用一句仿其口吻的話作預告：『沒有人比我更懂怎樣靠錢當皇帝了。』"

  lubuwei_current_knowledge_only:
    - "知道這是一個後世商人／政治人物故事。"
    - "知道有第一次登頂、失去、再回來、多次商業失敗後重建等概念。"
    - "不知道完整姓名、年代、國家制度、實際政治事件、精確財務史。"

  lubuwei_questions_for_chuyi:
    - "他怎麼把錢變成名？"
    - "怎麼把名變成權？"
    - "輸過以後，怎麼讓看過他失敗的人再押他一次？"
    - "錢消失時到底還剩什麼：名字、信用、債務、人脈、膽量、再讓別人下注的能力？"

  lock:
    - "不得在白御行正式講述前，把現代百科知識倒灌給呂不韋／趙姬／嫪毐。"
```

---

# 9｜嫪毐「大屌轉車輪」初一重演｜已接受但規格未定

```yaml
LAOAI_WHEEL_DEMONSTRATION:
  proposal:
    - "白御行邀嫪毐在初一晚上天下才子在場時，重演史書著名的桐木車輪身體技藝，以本人演示證明其名聲。"

  acceptance:
    status: "ACCEPTED_BY_LAOAI"
    conditions:
      - "器具必須是真木／實木輪，不做紙糊玩具。"
      - "要能承力，避免器材先壞造成爭議。"
      - "嫪毐要求公開演示，不躲簾後只靠說書轉述。"
      - "此演示只證明史書那項身體技藝／名聲，不直接推翻紅娘『吃過最大的』證詞。"
      - "紅娘也接受：轉得動車輪只證明轉得動車輪，不等於她已吃過／比較過嫪毐。"

  build:
    - "白御行表示明早就叫人打造。"
    - "嫪毐表示今晚會另寫尺寸、木料、輪徑、輪軸、最低重量等規格，明早交製作方。"
    - "嫪毐要在製成後親自驗器。"

  unknown:
    exact_weight: "UNKNOWN"
    exact_dimensions: "UNKNOWN"
    exact_wood: "UNKNOWN"
    exact_demo_method: "PENDING_LAOAI_SPEC_AND_EVENT_DAY"
```

---

# 10｜初一說書先生「特別採訪證」｜商會宣傳市場成立

```yaml
STORYTELLER_PRESS_PASS_CHUYI:
  player_instruction:
    - "白御行決定由定陶商會為初一晚場提供『特別採訪證』。"
    - "目標是讓汴京最紅的幾名說書先生可上湖心島采風，再把親見內容說給全京師聽。"
    - "會前可向商會申請。"
    - "持證者全程免費，有吃有喝。"

  lao_zhou:
    - "老周明確表示會去申請。"
    - "老周提出自己知道幾名說帝王、奇聞、風月等題材的同行可能有興趣；具體誰最後取得證、誰實到仍待商會程序。"

  pan_boundary:
    - "潘金蓮接受採訪證方向，但明確劃界：只能採公開可看的場。"
    - "商會公開席／湖心島公開節目可看可記。"
    - "姑娘私談、客人私席、關門後私人內容，沒有當事人允許，採訪證不是通行牌。"

  business_logic:
    - "白御行明示商會花錢請說書人不是慈善；因為有利可圖才出錢。"
    - "呂不韋看出這可能形成第二層市場：島上賣一次，說書人回京再把名聲／故事擴散一次。"
    - "白御行沒有提前向呂不韋揭曉自己最終打算賺哪一層利益，要他初一現場自己看。"
```

---

# 11｜初一夏蓮限定掛牌｜由「興趣」正式轉為本人答應

```yaml
XIALIAN_ONE_NIGHT_LISTING_CHUYI:
  negotiation_history:
    - "趙姬早先只對『若自己再掛一夜，市場現在會怎樣定價』產生認真興趣。"
    - "她曾詢問：男人怎麼競、出價買到什麼、最後誰決定。"
    - "白御行把掛牌營運交回潘金蓮，明說牌生意是潘掌櫃的事。"
    - "潘金蓮接受由自己與趙姬直接談底價、分帳、規則、服務範圍等。"

  live_commit:
    - "在本輪晚場，趙姬本人最終明確說：『初一那晚，我掛。』"
    - "限定：只一夜。"
    - "她要求競價、價格、客人最後取得什麼等，交由她本人與潘金蓮談清楚。"
    - "她不以王后／太后身份壓場。"
    - "牌上名字最終確定為『夏蓮』。"

  naming:
    public_listing_name: "夏蓮"
    provenance: "由呂不韋先重新叫回舊名，趙姬其後自己選擇拿此名掛初一一夜。"

  operator:
    - "潘金蓮是掛牌營運／規則主責。"
    - "白御行可出點子、參與競價、抬市場，但不能代趙姬／潘金蓮簽掉未談清規則。"

  player_speech:
    - "白御行表示初一不會缺席，會盡力出到天價。"
    - "此句是未來競價意向，不是已經出價／已成交。"

  still_pending:
    - "夏蓮一夜究竟包含哪些服務：PENDING。"
    - "底價：PENDING。"
    - "加價規則：PENDING。"
    - "最高價是否自動成交：未因本輪直接確定，需等潘金蓮×夏蓮正式規則。"
    - "最終買家／客人：PENDING。"
    - "白御行是否得標：PENDING。"
    - "任何成人行為：NOT_YET_OCCURRED。"
```

---

# 12｜觀止既有「天價」基準｜辭歲1200萬／錦棠500萬

```yaml
GUANZHI_AUCTION_PRICE_BENCHMARKS:
  hard_macro_source:
    - "MASTER E93 已固化：九幽帝皇聯誼會散場後，辭歲／錦棠雙姝發生天價競拍。"

  exact_values_reaffirmed_in_current_scene:
    first:
      woman: "辭歲"
      value_taels: 12000000
      object: "一夜"
      payment_form_note:
        - "現場以一千二百萬兩級成交／欠單／清算帳成為觀止最高票面紀錄。"
        - "不把它誤寫成一千二百萬現銀當場全堆在地板。"
    second:
      woman: "錦棠"
      value_taels: 5000000
      object: "一夜"
      same_night_as_first: true

  current_market_meaning:
    - "本輪潘金蓮／在場人把1200萬視為觀止既有第一名天價基準。"
    - "500萬為第二名，同晚、同為一夜。"
    - "夏蓮初一若要被稱為『破紀錄天價』，必須以實際競價／成交結果再判定，不能預先寫成破紀錄。"
```

---

# 13｜初一下午「天下商人／商人心法」席位更新

```yaml
CHUYI_MERCHANT_TABLE_V5_11:
  event_status: "PLANNED / NOT_YET_OCCURRED"
  theme: "商人心法"

  confirmed_or_live_stated:
    lubuwei:
      status: "CONFIRMED_ACCEPTED"
      role: "以商人身分出席"
    zhaoji:
      status: "SELF_STATED_WILL_ATTEND_TO_LISTEN"
      note: "她說自己也去聽；此下午出席與晚間夏蓮掛牌分軸。"
    jintang:
      status: "BAI_PUBLICLY_STATED_WILL_ATTEND / EXISTING_PREHEAT_LINE"
      note: "本輪未由錦棠本人重新答一次；不得因此擴寫她接受任何額外服務／拍賣義務。"
    cisui:
      status: "GUILD_INVITATION_TO_BE_ISSUED / ATTENDANCE_PENDING"
      rationale_spoken_by_bai:
        - "辭歲不只曾被拍到1200萬；她現有千萬兩級身價／資產位置。"
        - "她已有大額資金配置／定存等既有硬線，因此白御行認為她有資格坐商人桌。"
      pan_action:
        - "潘金蓮接受把辭歲列為商人席邀請對象；來不來由辭歲本人。"

  qualification_axis:
    - "商人桌不以性別或曾被誰出價決定資格。"
    - "重點是本人如何取得、保存、配置、再生資產，以及如何做判斷。"

  not_confirmed:
    - "沈萬三等其他商人本輪若未另有邀請／答覆，不自動因名單設計而到場。"
    - "陶朱公／范蠡等歷朝商人候選不自動瞬移出席。"
    - "鄭經／朱經等亦需實際邀請／來源。"
```

---

# 14｜紅娘籠台賭約｜白御行行使獎勵權：初一日出提前出籠

```yaml
HONGNIANG_CAGE_RELEASE_V5_11:
  inherited_wager:
    - "白御行與紅娘先前有獨立高額賭局；紅娘輸後進觀止大堂鐵籠。"
    - "紅娘舊床仍在賭約處分範圍，要拆／砍／燒作柴。"
    - "籠台公開邊界：可看可問，觸碰仍可拒絕。"

  player_exercised_right:
    - "白御行明示行使自己從賭約取得的處置／獎勵權：讓紅娘在下月初一日出提前離開鐵籠，以便參加初一湖心島活動。"
    - "潘金蓮在現場接受此安排。"

  effective_future_state:
    release_time: "下月初一日出"
    until_then: "紅娘仍在籠內"
    bed_penalty:
      status: "UNCHANGED"
      result: "床仍要拆／砍／燒作柴，不因提前出籠取消。"

  strict_separation:
    - "此籠台賭約與紅娘另外的九日營業競賽／洗浴募資線不是同一契約。"
    - "白御行本輪沒有取消或修改紅娘『不以清水全身洗浴／酒浴例外』等既有募資條件。"
    - "不得因初一出籠就自動寫成她可以違反另一條洗浴約定。"
    - "洗浴線精確終點若未重新核帳，保持按既有約定計算，不臆造。"
```

---

# 15｜紅娘 × 嫪毐目前成人／比較狀態

```yaml
HONGNIANG_LAOAI_ADULT_STATUS:
  hongniang:
    - "已承認可『考慮』嫪毐是否值得進入她的比較範圍。"
    - "她說錢是一種可考慮理由，但不是唯一也不必然是最佳理由。"

  laoai:
    - "已取得挑戰市場第一名位置。"
    - "尚未取得紅娘允許的成人比較經驗。"

  current_result:
    physical_comparison: "NOT_ESTABLISHED"
    hongniang_statement_changed: false
    adult_event_between_them: "NOT_OCCURRED"
```

---

# 16｜初一晚「天下才子＋節目市場」現階段

```yaml
CHUYI_EVENING_PROGRAM_V5_11:
  planned_elements:
    - "觀止／文人／酒席主場。"
    - "錦棠預熱／品牌視覺線。"
    - "夏蓮限定一夜掛牌【本人已答應；規則待潘×夏蓮談】。"
    - "嫪毐車輪史書名場面本人演示【本人已答應；器具規格待交】。"
    - "說書先生採訪證／公開采風【商會制度方向已立】。"
    - "紅娘初一日出已可離籠，因此具備參加活動的時間條件；她實際在晚場做什麼仍依本人與潘安排。"

  still_pending:
    - "阿麗婭是否參加首次出閣／初夜拍賣：PENDING。"
    - "其他女人是否參加任何競價：PENDING。"
    - "蘇東坡／柳永等天下才子實際誰到：PENDING unless separately confirmed later."
    - "嬴政是否來／是否競價：PENDING。"
    - "拉斯普京是否到：PENDING。"
    - "忽必烈是否因阿麗婭到場：PENDING。"
```

---

# 17｜白玉池秦國三角邀請｜只成立邀請、意向與池靈邊界

```yaml
BAIYUCHI_QIN_TRIANGLE_INVITATION_V5_11:
  player_offer:
    - "白御行在準備散場前向呂不韋、趙姬、嫪毐介紹觀止後方白玉池。"
    - "他描述白玉池一天名額有限、男女同入，並提出若能說服池靈阿泠，今晚或許能加一場。"
    - "白御行提出兩種玩笑／候選：三人一起洗，或趙姬選一個男人陪她。"

  zhaoji_response:
    - "趙姬明確否掉『三個一起』。"
    - "趙姬表示願意去看看／去白玉池。"
    - "若是二人同行，她尚未在凍結前選定呂不韋或嫪毐。"
    - "她把選擇留在自己手上。"

  lubuwei_response:
    - "呂不韋對池靈有自身決定權這點產生興趣。"
    - "他表示若趙姬要去，他願意陪。"

  laoai_response:
    - "嫪毐也表示有意爭取陪趙姬進池。"
    - "未因他的表示取得資格。"

  aling_response:
    - "阿泠從白玉池方向明確表示：誰能進池子由她自己看／決定。"
    - "她沒有在本輪明確批准加開名額。"
    - "她也沒有批准趙姬＋呂不韋或趙姬＋嫪毐任何一組。"
    - "對白御行把自己的接待方式概括成『所有人都會被摸遍』，阿泠本人出聲否認這是固定流程；她怎麼接待要看當時的人、池水與她自己的意思。"

  body_comparison_joke:
    - "白御行問阿泠自己與嫪毐誰比較大，並要求不要公布答案。"
    - "阿泠表示目前不能比較：她曾有來源見過白御行，但沒有親見嫪毐；說書人的話不等於她親見。"
    - "阿泠答應不公開替兩人排榜。"
    - "沒有形成白御行 vs 嫪毐的客觀身體排名。"

  current_result:
    extra_session_approved: false
    actual_bath_started: false
    zhaoji_partner_chosen: false
    adult_event: "NOT_OCCURRED"
```

---

# 18｜今晚結束前白御行離場宣告

```yaml
BAI_EXIT_DECLARATION_V5_11:
  player_speech:
    - "白御行對潘金蓮／五娘表示：『我們不管了，今天熱鬧看完了，我先回家睡覺了。』"
  save_freeze:
    - "玩家隨後立即要求 HOT SAVE。"
    - "因此本 HOT 凍結在離場／回家動作正式完成前。"
  post_save_intent:
    - "白御行下一個已宣告自身行動：離開觀止、回後方白家睡覺。"
    - "不得在 SAVE 內預寫抵家後結果。"
```

---

# 19｜顧青簡今晚白家私訪仍未被吃掉

```yaml
GU_QINGJIAN_TONIGHT_CARRY_FORWARD:
  inherited_from_v5_10:
    - "顧青簡已條件式接受今晚下工後私下去白家。"
    - "她要自己從後面進、不坐車、不派人公開迎接。"

  current_v5_11:
    exact_arrival: "UNKNOWN"
    has_arrived_before_bai_departure: "NOT_ESTABLISHED"
    adult_event: "NOT_ESTABLISHED"
    cancellation: "NOT_ESTABLISHED"

  critical_resume_lock:
    - "白御行現在宣告回白家，不能因此直接跳過顧青簡這條尚未決的夜訪線。"
    - "若後續白御行抵家，是否遇上她／她何時到，只能由當時世界狀態與事件來源決定。"
```

---

# 20｜失仙／浮月閣線保持不動

```yaml
SHIXIAN_FUYUEGE_CARRY_FORWARD:
  shixian:
    whereabouts: "UNKNOWN"
    returned_to_guanzhi: "NOT_ESTABLISHED"
    current_competition_result_today: "PENDING"

  fuyuege:
    status: "NAME_LEAD_ONLY / NOT_GUILT / NOT_FULL_IDENTITY"
    known_by:
      - "白御行"
      - "潘金蓮（由白御行轉述）"
      - "時空道人"
    hongniang_knows: false
    passive_listening_only: true

  strict_lock:
    - "嫪毐／趙姬／呂不韋秦國線不得吞掉浮月閣／失仙未知線。"
    - "偏廳陌生男子不得被補成浮月閣。"
```

---

# 21｜主系統下一 successor 必補硬法【維護提醒；不是宣稱已改檔】

```yaml
MAIN_SYSTEM_HARDLAW_PATCH_REQUIRED:
  status: "REQUIRED_MAINTENANCE_ITEM / NOT_YET_EDITED"
  target: "觀止青樓主系統 V14.2 的合法 successor／正式 PATCH"
  required_text_core:
    - "良家女不得以公開娛樂取利。"
    - "公開娛樂營業須妓籍。"
    - "妓籍一經成立終身不可洗。"

  purpose:
    - "把 E103 已存在的妓籍終身法位鎖升成主系統明確硬條文，避免未來人物池／舊資料措辭漂移。"

  conflict_to_reconcile:
    - "LCAPG V3.2 某些錦棠相關舊措辭仍出現『日後脫籍、贖身、轉職、結婚或另立戶籍』類說法。"
    - "其中『脫籍可洗掉既成妓籍』與本 Route E103 硬法衝突。"
    - "人物卡池是 generation provider，不能反向覆寫世界硬法。"

  nonclaim:
    - "本 HOT SAVE 沒有修改主系統 V14.2 原檔。"
    - "本 HOT SAVE 沒有修改 LCAPG V3.2 原檔。"
    - "此處只保存下一正式 successor／PATCH 的必修項。"
```

---

# 22｜本輪禁止偷補／倒灌

- 不得把「嫪毐挑戰紅娘」寫成紅娘已同意與嫪毐發生成人事件。
- 不得把嫪毐付錢寫成買到紅娘身體。
- 不得把嫪毐車輪演示承諾寫成已完成／已成功。
- 不得自己補嫪毐車輪的重量、尺寸、木料；他說今晚另寫規格，現值 UNKNOWN。
- 不得把趙姬替嫪毐證明名聲寫成趙姬能比較嫪毐 vs 白御行。
- 不得把趙姬妓籍寫成她必須營業／必須同意任何客人。
- 不得再生成「趙姬可脫妓籍」的世界法。
- 不得把「夏蓮掛初一一夜」寫成白御行已得標。
- 不得把白御行「會開到天價」寫成實際出價。
- 不得把1200萬／500萬舊天價直接當成夏蓮底價或成交價。
- 不得把趙姬選擇掛夏蓮一夜寫成她對白御行戀愛／私人性同意。
- 不得把呂不韋叫回「夏蓮」寫成趙姬必然仍愛呂不韋。
- 不得把嫪毐／趙姬／呂不韋的秦國舊史全部按史書強制覆寫成三人現代自我理解；老周說的是史載口徑。
- 不得把2001 donor 的後續劇情當 Route 命運。
- 不得整包匯入2019《皓鑭傳》。
- 不得讓呂不韋在初一前突然知道白御行尚未講出的後世商人完整資料。
- 不得把「天下商人席」候選名單自動變成全部到場。
- 不得替辭歲接受邀請；目前只成立商會要邀／潘已列邀請，是否來待本人。
- 不得把錦棠下午出席擴成她同意新的成人／掛牌義務。
- 不得替阿麗婭接受初一初夜拍賣；仍 PENDING。
- 不得替嬴政出場、競價、封盤。
- 不得替拉斯普京／忽必烈等人自動到場。
- 不得把紅娘初一日出出籠與她的另一條洗浴募資合併。
- 不得因提前出籠取消紅娘床的拆／砍／燒處分。
- 不得把白玉池邀請寫成阿泠已批准加場。
- 不得把趙姬說「我去」寫成她已選呂不韋或嫪毐共同入池。
- 不得把白御行對阿泠接待方式的描述當作阿泠固定義務；阿泠已親口保留自己決定。
- 不得公布或補造白御行 vs 嫪毐身體比較結果。
- 不得把白御行「回家睡覺」直接跳成已睡到明早；顧青簡今晚私訪仍是活鉤。
- 不得把偏廳未知男子與秦國線／浮月閣線合併。
- 不得推測失仙去向。
- 不得產生榴月二十九／三十。

---

# 23｜當前人物／場景狀態【凍結點】

```yaml
CURRENT_SCENE_V5_11:
  date: "理火三年榴月二十六日晚"
  location: "觀止大堂"
  exact_clock: "UNKNOWN"

  player:
    name: "白御行"
    status:
      - "已表示今晚熱鬧看完，要回白家睡覺。"
      - "HOT SAVE 在離場完成前凍結。"

  present_or_last_observed_in_scene:
    - "潘金蓮"
    - "紅娘（仍在鐵籠；初一日出才提前釋放）"
    - "嫪毐"
    - "趙姬／夏蓮"
    - "呂不韋"
    - "老周說書先生"
    - "嫪毐隨從"
    - "趙姬兩名侍從"
    - "偏廳未知男子與兩隨從：未觀察到明確離場，保持世界自主"
    - "阿泠在白玉池側，以聲音參與後段對話"

  not_present_or_unknown:
    shixian: "UNKNOWN / 未返"
    gu_qingjian: "今晚私訪約在，但此刻位置／到達時間 UNKNOWN"

  key_future_commitments:
    - "呂不韋：初一下午湖心島，以商人身分出席。"
    - "趙姬：初一下午表示會去聽商人心法；初一晚以『夏蓮』限定掛牌一夜。"
    - "嫪毐：初一晚公開重演桐木車輪名場面；今晚先寫規格。"
    - "紅娘：初一日出提前出籠；床處分不變。"
    - "老周：將申請商會特別採訪證。"
    - "辭歲：商會將發邀請，是否到場 PENDING。"
```

---

# 24｜直接接關摘要

> **理火三年榴月二十六日晚。HOT V5.10 後，觀止偏廳那名問失仙的二十七八歲陌生男子仍維持身份未知；紅娘曾自行與其桌發生最低限度營業接觸，但不得把他與浮月閣或後來的秦國人物合併。其後嫪毐因聽見紅娘公開證詞「我紅娘，這輩子吃過最大的雞巴是白御行的」不請自來，付挑戰款並成為《不服白御行者名錄》第一名。紅娘把挑戰費與成人 access 分開，單純目測也不能進入「吃過」的同一比較類別；她尚未同意與嫪毐形成成人比較。嫪毐叫人請趙姬來作自身名聲證人；趙姬自主到場，只能證明她自己的既有經驗，不能比較嫪毐與白御行。趙姬在場自認過去公開歌舞娛樂取利與妓籍，並明示王后／太后等身份沒有洗掉妓籍。呂不韋後來入場，重新叫出她的舊妓名「夏蓮」；本 Route 正式採用2001《呂不韋傳奇》線作趙姬主要戲劇 donor：夏蓮、邯鄲名妓／歌舞出身、呂不韋舊歷史、皓蘭夜明珠等可作來源，但不整包匯入2019《皓鑭傳》，且 donor 未來不綁 Route 命運。趙姬最終本人明確決定：初一晚限定掛牌一夜，牌名就用「夏蓮」；實際底價、服務、競價、成交規則仍由她與潘金蓮另談，白御行只是公開表示自己會參與並盡力開到天價。觀止舊價基準在本場重新確認：辭歲1200萬兩一夜為第一、錦棠500萬兩一夜為第二，兩筆同晚。呂不韋接受初一下午湖心島邀請，且以商人身分而非秦相身分來；下午主題進一步成形為「商人心法」，討論人如何賺、判斷、重建，而非只比現有身家。白御行答應初一再講一個後世商人登頂、失位、再回來、多次商業失敗後重建的完整故事；目前呂不韋只知鉤子，不知現代百科細節。白御行另邀嫪毐初一晚在天下才子面前重演史書桐木車輪技藝；嫪毐接受，要求真木、可承力、公開演示，今晚另寫器具規格，明早由白御行安排打造，精確重量／尺寸尚未成立。白御行又決定由定陶商會向汴京紅說書先生發「特別採訪證」，免費吃喝、公開場可采風，老周會申請；潘金蓮鎖定採訪證不等於可闖私人席／私房。初一下午席位方面，呂不韋已確定、趙姬自己說會去聽，白御行公開表示錦棠會出席；潘金蓮另把辭歲列入商人席邀請，是否到由辭歲本人。紅娘方面，白御行行使先前賭約所得權利，決定讓她在下月初一日出提前出鐵籠，方便參加初一活動；但她的床仍要拆／砍／燒作柴，且另一條九日營業／洗浴募資約沒有被取消。散場前白御行邀呂不韋、趙姬、嫪毐去白玉池；趙姬拒絕三人一起，但表示自己願意去，尚未在呂不韋與嫪毐之間選陪同者。阿泠明確保留加場與進池決定權，本輪沒有批准任何一組、沒有開始洗浴，也沒有形成白御行與嫪毐的身體比較結果。最後白御行對潘金蓮表示今晚到此、要回白家睡覺，隨即要求 HOT SAVE；因此本檔凍結在離場完成之前。顧青簡今晚下工後私訪白家的既有約定仍有效但到達時間 UNKNOWN，不能因白御行說回家就直接跳過。**

---

# 25｜下一串最小載入包

```yaml
MINIMUM_RESUME_PACKET_V5_11:
  required:
    - "MASTER V5.5-R2-HARD"
    - "HOT V5.6【REBUILD-R1】"
    - "HOT V5.7"
    - "HOT V5.8"
    - "HOT V5.9"
    - "HOT V5.10"
    - "HOT V5.11（本檔）"

  current_scene:
    date: "理火三年榴月二十六日晚"
    location: "觀止大堂｜白御行即將離場回白家"
    state: "HOT SAVE 凍結"

  immediate_next_player_action:
    - "依白御行已宣告：離開觀止，回白家睡覺。"

  first_collision_to_respect:
    - "顧青簡今晚已有私訪白家約定；精確到達時間 UNKNOWN。"
    - "不得直接把白御行跳睡到翌日而吞掉可能的碰面時間窗。"

  highest_priority_open_threads:
    - "失仙去向 UNKNOWN。"
    - "浮月閣只作專名線索，被動聽風。"
    - "偏廳陌生男子身份／意圖 UNKNOWN，且與秦國線分離。"
    - "初一夏蓮一夜掛牌：本人已答應；規則待潘×夏蓮談。"
    - "初一嫪毐車輪：本人已答應；器具規格待他今晚交。"
    - "初一商人心法：呂不韋已答應；辭歲邀請待回覆；其他人各需來源。"
    - "阿麗婭是否參加初一首次出閣／初夜競價仍 PENDING。"
    - "紅娘初一日出提前出籠；床仍要毀；洗浴募資另契不變。"
    - "白玉池秦國三角：沒有批准、沒有開洗、趙姬沒有選人。"
    - "主系統 successor 必補：良家女不得以公開娛樂取利；公開娛樂營業須妓籍；妓籍一經成立終身不可洗。"
```
