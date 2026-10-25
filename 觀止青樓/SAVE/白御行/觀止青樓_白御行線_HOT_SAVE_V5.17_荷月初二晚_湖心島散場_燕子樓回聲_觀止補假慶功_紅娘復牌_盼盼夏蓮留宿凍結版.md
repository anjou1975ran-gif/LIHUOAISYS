# 觀止青樓｜白御行線 HOT SAVE V5.17
## 理火三年荷月初二晚｜湖心島散場 × 燕子樓回聲 × 師師美成斷尾 × 觀止補假慶功 × 十一哥門口場 × 紅娘復牌 × 關盼盼／夏蓮留宿 × 人物池討論前凍結版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V5_17_HEYUE_CHUER_EVENING_GUANZHI_CELEBRATION_FREEZE"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V5.17"
  record_type: "HOT_SAVE"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"

  previous_valid_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V5.16_荷月初一深夜_阿麗婭三千萬_夏蓮五千萬_千古一帝場外賽_白紗帳終場凍結版.md"
    status: "VALID_PREDECESSOR_WITH_SUCCESSOR_CORRECTIONS"
    sha256_current_bytes: "470466db161174ac96edef6bc03edd32044765ad2f1647da23e22c49f8ad8914"

  current_master:
    file: "觀止青樓_白御行線_MASTER_SAVE_V5.13-R1-HARD_全歷史自足_E01-E121_截至HOT_V5.13-R1固化_保留V5.14-V5.16_HOT版.md"
    generation: "V5.13-R1-HARD"
    sha256_current_bytes: "19d9acb7ee15f829104fb2a31a94966fa4998e6d06b9a7364068413b9c1b01d5"
    write_performed: false

  current_rcl:
    file: "觀止青樓_白御行線_人物履歷_RCL_V5.13-R1_MASTER_E01-E121_SCHEMA_V1.1_62人對齊版.md"
    generation: "V5.13-R1"
    schema: "GUANZHI_RCL_SCHEMA_V1_1"
    sha256_current_bytes: "b74c78cbbde9647191008b5314d01ccf1a2ccfca0c4699a197700633db4da8d0"
    write_performed: false

  story_time:
    calendar_system: "觀止曆：一年十三月，每月固定二十八日"
    current_date: "理火三年荷月初二"
    exact_clock: "UNKNOWN"
    daypart: "晚／觀止大堂慶功宴開席前後"

  current_scene_freeze:
    state: "STORY_FROZEN_BY_HOT_SAVE_COMMAND"
    location: "觀止青樓｜正門門口熱鬧剛收、眾人轉入大堂慶功"
    latest_observable:
      - "潘金蓮已在觀止正門宣布失仙因長期未返、競賽中途離場而作棄賽處理；紅娘恢復『觀止首席紅牌』廣告牌。"
      - "紅娘原床已由白御行在觀止門口公開劈解，木料送入廚下作柴。"
      - "十一哥仍留在觀止正門『兩處一門』聲音接觸位置，可與街上／紅娘互動。"
      - "關盼盼已接受潘金蓮提供的觀止後院東廂暫住安排，當前未簽留樓／掛牌／舞台契約。"
      - "夏蓮的一夜自由掛牌期限已過；其四千五百萬兩本人應得款仍有大額結算工作，暫住觀止並以房費掛帳方式處理。"
      - "關盼盼與夏蓮均已受邀並實際到觀止大堂今晚慶功宴。"
      - "玩家要求在此先 HOT SAVE，下一步轉 DISCUSSION 討論『關盼盼／夏蓮是否適合進人物池』。"

  write_scope:
    hot_only: true
    master_write: false
    rcl_write: false
    character_pool_write: false
    core_write: false
```

---

# 0｜現行治理／生成法位

```yaml
GENERATION_PROFILE_V5_17:
  constitutional_root:
    version: "理火協議 V2.4"
  lighter:
    version: "理火賴打 V3.5.2-EXP"
  guanzhi:
    core: "V15.4 CURRENT"
    world: "V1.5.1 CURRENT"
    heart: "V1 CURRENT"
    character_pool: "LCAPG V3.3.9 / 62"

  current_route_memory:
    - "MASTER V5.13-R1-HARD / E01-E121"
    - "paired RCL V5.13-R1 / schema V1.1"
    - "HOT V5.14"
    - "HOT V5.15"
    - "HOT V5.16"
    - "HOT V5.17（本檔）"

  hard_axes:
    - "PLAYER SPEECH / ATTEMPT / CHOICE / SELF-REPORT != WORLD RESULT"
    - "NPC DECISION / CONSENT / RELATION / KNOWLEDGE require source"
    - "MONEY != RELATION"
    - "PAYMENT != ACCESS"
    - "ACCESS != RELATION"
    - "RELATION != CONSENT"
    - "RUMOR != FACT"
    - "ROLE != IDENTITY"
    - "PUBLIC LABEL != PRIVATE REALITY"
    - "SOURCE FUTURE != ROUTE DESTINY"
    - "SAVE only stores established events/evidence and explicit UNKNOWN/PENDING/DISPUTED"
```

---

# 1｜本次 successor 範圍與編譯紀律

```yaml
SOURCE_LINEAGE_V5_17:
  inherited:
    - "MASTER V5.13-R1-HARD"
    - "paired RCL V5.13-R1"
    - "HOT V5.14"
    - "HOT V5.15"
    - "HOT V5.16"

  current_live_commit_scope:
    - "HOT V5.16 白紗帳公開終場後至荷月初二晚、玩家下達本次 HOT SAVE 命令前之已顯影事件。"
    - "湖心島深夜餘波、初二破曉散場、各路離島、燕子樓／白居易／蘇東坡／關盼盼線、周邦彥／李師師斷尾、商會與觀止輪班／補假、初二晚觀止門口與慶功宴開場。"

SAVE_DISCIPLINE_V5_17:
  - "本檔不重寫 MASTER，不 promotion RCL，不修改 LCAPG。"
  - "討論『關盼盼／夏蓮是否進人物池』尚未開始，故不得把二人 promotion 寫成既成。"
  - "未精確顯影的帳務結算工具、分紅比例、房價、獎勵金數字保持 UNKNOWN。"
  - "人物公開稱呼／暫住／受邀吃飯 != 正式入職、掛牌、簽約或加入人物池。"
  - "夏蓮一夜期限結束 != 自動補完白紗帳私密內容。"
  - "失仙棄賽判定只結束紅娘×失仙營收競賽；不證成失仙失蹤原因、身份、浮月閣真相或死亡。"
```

---

# 2｜對 HOT V5.16 的 successor 校正｜阿麗婭 × 忽必烈離島時間

```yaml
ALIYA_KUBLAI_DEPARTURE_CORRECTION_V5_17:
  supersedes_overbroad_v5_16_assumption:
    - "HOT V5.16 曾以『夜渡已停』把阿麗婭／忽必烈也一併鎖在島上。"
    - "後續 Route 校正：阿麗婭與忽必烈在夜渡停止之前、晚場中途即已搭船離開湖心島。"

  current_hard_state:
    - "阿麗婭與忽必烈目前不在湖心島／觀止慶功場。"
    - "七日首主／共同生活方向在線外持續。"
    - "七日不等於所有權或 blanket adult access。"
    - "成人私密事件沒有由本 HOT 自動補全。"

  deposit_business_lock:
    - "阿麗婭本人應得二千七百萬兩之未來存款／資金安排仍屬她本人決定。"
    - "顧青簡只能在七日結束後再與阿麗婭談定存／資金生意；不得提前接觸成交。"
```

---

# 3｜湖心島深夜至破曉｜散場條件與船運

```yaml
ISLAND_DAWN_TRANSITION_V5_17:
  established:
    - "荷月初二破曉後，湖上船運重新開始。"
    - "第一批船靠岸後，各朝人物、商人、文士與說書先生陸續分流離島。"
    - "商會有自有船隻；觀止亦有自己的船。"
    - "白日收場工作由後續乘商會船／觀止船抵達的新班工作人員接手，不再把昨日下午一路熬到天亮的原班人員續用到白天。"

  zheng_jing_ship:
    - "鄭經以大型戰船離場。"
    - "其公開表示可載順路者，明示不載滿洲人。"
    - "朱正德等人對此起鬨；滿洲陣營自行乘其自身船隻／人馬離開。"

  no_auto_jump:
    - "本 HOT 已合法從初一深夜推進至初二晚，因中間破曉、回城、休息與傍晚返回均已在 STORY 中顯影。"
```

---

# 4｜顧青簡 × 商人資金池｜白御行授權她談

```yaml
GU_QINGJIAN_MERCHANT_NEGOTIATION_V5_17:
  pre_dawn_contact:
    - "顧青簡在破曉前已與沈萬三接觸。"
    - "方向為把巨額資金需求拆成短池／長池／聯合池，而非讓定陶、沈、胡等人零和搶單。"
    - "沈萬三表達願意談短池／長池／聯合池；沒有在湖心島簽成正式契約。"
    - "正式商議留待回城後進行。"

  player_delegation:
    - "白御行明示：『談判的事情交給你，反正我少做事情就是幫忙。』"
    - "因此顧青簡取得代表白御行／定陶方向繼續談判的工作授權。"
    - "授權 != 自動同意任何最終利率、池型、擔保或契約。"

  xialian_aliya_capital_direction:
    xialian:
      amount: 45000000
      direction: "可爭取定存／資金池，但本人是否存、存多少、期限／利率均未成立。"
    aliya:
      amount: 27000000
      direction: "七日後才可談；不得提前成交。"
    cisu_reference:
      - "辭歲五百萬／五年／年利率5%只可作比較與開價參考，不自動套用二人。"
```

---

# 5｜楊玉環 × 趙受益 × 六條｜兩女爭寵但未升格

```yaml
ZHAO_YANG_ROKUJO_DAWN_V5_17:
  presence:
    - "六條自夜場起就一直在趙受益身邊；不得寫成後來才到。"
    - "楊玉環在趙受益拒用人民國運競夏蓮／千古一帝後，主動向他靠近。"

  relation_evidence:
    - "楊玉環明示：以前是趙受益追、她允許他追；現在她不想只等他追，想主動靠近。"
    - "她曾靠在趙受益肩上；表示若不喜歡會告訴他。"
    - "她分給趙受益半份糖果／果子，趙受益接受。"
    - "趙受益把接近她的理由放在『妳在這裡』，而非政治／歷史。"

  rivalry:
    - "六條與楊玉環之間已出現對趙受益注意力／親近位置的公開競爭。"
    - "六條是熟悉與既有陪伴；楊玉環是新近主動靠近。"
    - "兩女爭寵 != 趙受益已與楊玉環形成愛情、性交、排他關係。"

  guan_dance_pause:
    - "關盼盼破曉舞時，楊玉環與六條均認真觀看，短暫停止彼此競爭。"
```

---

# 6｜李隆基 × 紅娘｜破曉鬧場

```yaml
LI_LONGJI_HONGNIANG_DAWN_V5_17:
  established:
    - "白御行先前讓紅娘去鬧李隆基。"
    - "紅娘抓住楊玉環去趙受益身側這件事刺李隆基，形成公開笑料。"
    - "關盼盼破曉舞後，李隆基看舞不語。"
    - "紅娘問其是否不服；李隆基答大意為現在知道白居易與蘇東坡為何都要栽。"
    - "紅娘回『這話倒像人話。』"

  lock:
    - "李隆基可被觀察到在意／注視，不自動生成報復、佔有或敵對行動。"
```

---

# 7｜白居易 × 關盼盼 × 蘇東坡｜燕子樓舊債重新顯影

```yaml
GUAN_BAI_SU_CORE_V5_17:
  guan_bai_old_history_route:
    - "觀止 Route 接受：白居易曾在關盼盼年輕時見過其歌舞。"
    - "燕子樓千年傳說／風聞對二人有真實社會與情感後果，即使史料層存在爭議。"
    - "關盼盼當面追問白居易：當年看見的是她本人，還是『張家的舞姬』。"
    - "白居易面對她後承認自己當年不懂。"
    - "沒有因此形成和解、復合或愛情。"

  guan_su_dream:
    - "蘇東坡出生年代晚於關盼盼約兩百年，沒有在其生前歷史年代實際見到她。"
    - "本 Route 中，關盼盼本人明示『那一年，我入你夢裡的時候』；此 Route 以她確曾進入蘇東坡夢中為成立世界事實。"
    - "蘇東坡當年並不知道夢中女子即為真實關盼盼；到觀止才完成辨認。"
    - "關盼盼問：『當年我都已經不在你的年月裡了。你為什麼還要來找我？』"
    - "蘇東坡回答核心：原以為找的是一座樓，後來才知道是在找她。"

  guan_to_bai:
    - "關盼盼以『他與我隔了兩百年，都知道要來看看。你呢？』刺向白居易。"

  no_forced_resolution:
    - "上述線只建立舊債、追問與重新看見，不建立關盼盼對白居易／蘇東坡的戀愛或成人同意。"
```

---

# 8｜蘇東坡新詞《定風波·湖心再逢燕子樓人》

```text
兩百年前一夢遲，
燕樓風月到今時。
明月不知人世換，
重看，
一燈猶照舊羅衣。

當日尋樓渾未省，
誰信，
醒來只道是相思。
今夜佳人親問我：
何故？
原來尋樓便尋卿。
```

```yaml
SU_NEW_CI_V5_17:
  established:
    - "蘇東坡於湖心島寫成上述詞。"
    - "關盼盼明示允許傳播：『傳吧。』"
    - "但她要求說書時必須連前面的故事一起講，不許只拿最後一句哄男人。"
    - "十名說書先生取得抄本／記錄。"
    - "核心句：『原來尋樓便尋卿。』"
    - "破曉時抄本已在場內流轉；後續汴梁傳播可以發生，但不得補每一家茶樓／版本已全面覆蓋。"
```

---

# 9｜關盼盼破曉一舞｜「讓你們看看我自己」

```yaml
GUAN_DAWN_DANCE_V5_17:
  entry:
    - "破曉後，關盼盼主動起身，不用舞台／樂隊，在湖邊完成一折舞。"
    - "她對白居易與蘇東坡明示：『你們兩個，都替我寫過了。今早，讓你們看看我自己。』"

  body_observation:
    - "她以長袖、身體、呼吸與空間完成舞，不再只作燕子樓文本符號。"
    - "舞畢自然出現微汗、呼吸加快、扶欄等身體反應。"

  bai_response:
    - "關盼盼問白居易：『當年，我是不是也這樣跳過？』"
    - "白居易答『是』，並說她年輕時比現在還狠、更不肯放人。"

  su_response:
    - "關盼盼問蘇東坡：今早這一折是否夠他再寫一句活的。"
    - "蘇東坡沒有立刻再寫新詞，而答：『我以為我找了妳兩百年。現在才知道，不對。是妳先讓我找著的。』"

  crowd_reaction:
    - "紅娘／潘金蓮等有可觀察反應。"
    - "楊玉環／六條等旁人一度被舞吸住。"

  lock:
    - "舞 != 留樓簽約。"
    - "舞 != 掛牌。"
    - "舞 != 對白居易／蘇東坡的感情承諾。"
```

---

# 10｜潘金蓮 × 關盼盼｜留人方向已談，但合約未成立

```yaml
PAN_GUAN_RETENTION_V5_17:
  pan_business_assessment:
    - "潘金蓮明示自己早已在評估關盼盼的商業價值。"
    - "她認為關盼盼的價值不必先從床牌開始，可先由舞、詞、燕子樓傳說、白居易舊債、蘇東坡夢／新詞形成舞台價值。"
    - "若未來合作，可討論獨立舞台、演出頻率、票價／收入分成、觀眾 access 等。"
    - "是否掛成人牌是另一門生意，不因舞台合作自動發生。"

  direct_talk:
    - "潘金蓮帶茶直接去找關盼盼談，開場明示『先不談錢』。"
    - "關盼盼以玩笑回她這句從潘金蓮嘴裡說出來很可怕。"
    - " substantive retention deal 尚未在湖心島談成。"

  current_status:
    - "關盼盼沒有答應加入觀止。"
    - "沒有簽舞台約。"
    - "沒有掛牌。"
    - "沒有設定固定價格。"
    - "沒有建立觀止妓籍／僱傭／人物池 promotion。"
```

---

# 11｜周邦彥 × 李師師｜舊情正式斷尾

```yaml
ZHOU_LI_SHISHI_CLOSURE_V5_17:
  old_history_position:
    - "本 Route 承認李師師與周邦彥存在足以支撐『舊情／前男友』語境的過往私人關係。"
    - "傳說中的床底細節仍不必逐條證實；李師師自己不否認『有些東西若真的發生過，就是發生過』。"

  closure_dialogue:
    - "周邦彥在破曉散場前以『師師』叫住她。"
    - "周問若當年的事並不全是附會；師師答：『那也已經是當年了。』"
    - "李師師以舊稱『美成』叫他。"
    - "她明示：『我不否認認得你。』『也不否認，有些東西若真的發生過，就是發生過。』『可人不能因為一闋詞寫得好，就永遠留在那一夜。』"
    - "周邦彥問白御行待她是否好；李師師沒有把白御行美化，而是直接說白御行風流、會惹亂子、讓她想打人等，最後明示：『可是我現在要回去的地方，在他那邊。』"
    - "她告訴周邦彥昨夜題詩只是逗他。"
    - "最後明示：『以後若再見，寫詞就寫詞。』『別再拿舊事等我。』"
    - "周邦彥回答『好』，停止等待／追求。"

  result:
    - "周邦彥殘留的現役浪漫希望在本 Route 至此 CLOSED。"
    - "舊史、詞、傳聞仍可存在，但不得無新因果重新寫成周持續追李師師。"
    - "李師師回到白御行身邊，恢復其當前白家首席如夫人／女主人級生活位置。"
    - "此位置為她當前選擇／關係結果，不是所有權，也不抹去其花魁職業與自治。"
```

---

# 12｜乾隆退場 × 疏影詢問 × 錦棠回白御行身邊

```yaml
QIANLONG_JINTANG_EXIT_V5_17:
  qianlong:
    - "乾隆離島前主動問錦棠『疏影呢？』／近況方向。"
    - "錦棠不替乾隆傳話，表示若真想知道可自己找疏影。"
    - "此詢問只證明乾隆仍記得／掛念疏影方向，不建立疏影回應或關係恢復。"

  jintang:
    - "錦棠完成昨夜被白御行安排到乾隆身邊的場面／品牌任務。"
    - "初二破曉後她自主回到白御行一側。"
    - "昨日本日限定『公開女伴／一天的男人』語境已隨日期結束，不升格永久關係。"
```

---

# 13｜張麗華｜酒水供應者 × 白家情人／小院居民

```yaml
ZHANG_LIHUA_V5_17:
  event_role:
    - "張麗華自初一午後到晚場／深夜，是湖心島全場主要酒類供應者之一；酒莊承擔酒水供應。"
    - "破曉後她處理未開封酒、空壇與酒莊帳務交接。"

  private_household_role:
    - "她不是散場後回普通酒商住處。"
    - "她是白御行既有情人，白家已有自己的小院／生活位置。"
    - "工作交接後她回到白御行／白家隊伍。"

  double_axis:
    - "酒莊生意身份 != 私人情人身份。"
    - "白家情人身份 != 她失去酒莊經營與帳務自主。"
```

---

# 14｜商會女人、白希與四大丫環、蘇清、舍方知｜昨夜勞務結算方向

```yaml
MERCHANT_EVENT_STAFF_REWARD_V5_17:
  merchant_women:
    - "商會女性人員從初一午後一路參與至深夜／破曉；晚場雖不是主角，仍在迎賓、場務、衣物／布料、茶水、人流等位置持續工作。"
    - "白御行破曉時公開嘉勉，明示昨日下午至天亮之工作會記錄。"
    - "昨夜班交接後先休息，不再繼續白天收場。"
    - "加菜／補休／獎勵金方向成立，但精確獎勵金額未在本 HOT 固定。"

  bai_xi:
    - "白希是白家四大丫環之一，亦是這批商會女性的現場監督者之一。"
    - "她從午後到夜間負責站位／安全／服裝與人員調度方向。"
    - "白御行公開點名其監督有功。"

  four_attendants:
    members:
      - "白希"
      - "白三十二娘"
      - "白明礬"
      - "白紅伶"
    state:
      - "四人昨夜雖未長時間站在白御行身側顯眼出場，但均視為人物池內正常活動、在商會／場務需要處協助。"
      - "白御行明示四人也列入加菜／獎勵方向。"

  su_qing:
    - "蘇清是商會這批女性訓練的重要功臣之一。"
    - "她對待客、觀察、商業互動、服裝與注意力生意等訓練有實際貢獻。"
    - "白御行明示她的獎勵要與受訓人員分開另算；精確數字未定。"

  she_fangzhi:
    - "舍方知不是定陶商會員工，也不是白家人。"
    - "她在昨日下午／夜間對商會衣物、裁改、修補實際出力。"
    - "白御行明示按『裁衣工錢』另付，不混作商會員工獎勵。"
    - "舍方知接受此名目。"
```

---

# 15｜觀止昨夜照常營業｜仕女夜放假 × 春梅主持 × 李瓶兒晨間接班

```yaml
GUANZHI_OPERATIONS_CHUYI_TO_CHUER_V5_17:
  chuyi_night:
    - "初一晚觀止本店仍然營業。"
    - "初一本來恰逢仕女夜／姑娘放假日；湖心島昨夜出勤者屬額外加班／自願到場工作方向，不等於全樓原班被拉來熬夜。"
    - "龐春梅昨夜留守觀止並主持本店營運。"

  dawn_relief:
    - "初二早上李瓶兒帶觀止自己的船與新班工作人員到湖心島接手收場。"
    - "商會亦由自有船帶來新的白班工作人員。"
    - "新班接手後，昨夜班停止工作、回去休息。"

  li_pinger_double_identity:
    - "李瓶兒同時是觀止三掌櫃與白家如夫人／女主人級人物。"
    - "清晨先以三掌櫃身份安排觀止人員接班／收場；工作分派完成後再回白家隊伍。"
    - "掌櫃身份與白家身份均有效，不互相抹除。"
```

---

# 16｜觀止兩筆巨額收入｜八百萬平台收益 × 掌櫃分紅方向

```yaml
GUANZHI_8M_REVENUE_V5_17:
  aliya:
    gross: 30000000
    guanzhi_platform_share: 3000000
    aliya_share: 27000000
  xialian:
    gross: 50000000
    guanzhi_platform_share: 5000000
    xialian_share: 45000000

  guanzhi_total_platform_revenue: 8000000

  accounting_lock:
    - "八百萬是兩筆成交對觀止形成的10%平台收益／應收權利總和。"
    - "並不要求在同一時刻以八百萬現銀全部搬入庫房；精確兌付／票據／資產轉換仍可後續清算。"
    - "掌櫃分紅方向因本次巨額收益而非常可觀，但本 HOT 未固定三掌櫃精確分紅比例／實際領取數。"
```

---

# 17｜潘金蓮宣布初二觀止補假一天 × 晚上全樓慶功

```yaml
GUANZHI_HOLIDAY_CELEBRATION_V5_17:
  public_decision:
    - "潘金蓮以大掌櫃身份宣布：荷月初二觀止停止對外營業一天，作為昨夜活動／本店工作的補假。"
    - "必要門房、看火、守庫等最低值守另補假／另算，不把補假吃掉。"

  celebration:
    - "初二晚上觀止大堂舉辦全樓慶功宴。"
    - "今晚大堂不是營業席，不接客；姑娘不用陪客，內部人員以吃飯／慶功為主。"
    - "潘金蓮、龐春梅、李瓶兒三掌櫃出錢，潘金蓮公開表示自己出大頭。"
    - "餐食、酒水等可向外部酒樓／張麗華酒莊正常付費採買。"

  pan_financial_contrast:
    - "席間眾人以舊事取笑潘金蓮：白宅曾形成八千兩／十年租用框架，而她過去又遭蘇清五萬兩民事索賠起始請求等現金壓力逼得極緊。"
    - "此晚潘金蓮可以公開說『掌櫃出錢』並願意闊氣辦宴，形成與舊日窮困的強烈可觀察對比。"
    - "『財富自由』可作人物／玩家評語，不在 SAVE 中把它升格為永遠不會再有現金流風險的世界定律。"
```

---

# 18｜定陶商會今日照常、初三補假 × 中午第二場慶功

```yaml
DINGTAO_HOLIDAY_CELEBRATION_V5_17:
  chuyi_to_chuer:
    - "初二白天定陶商會照常運轉；昨夜班交班後休息，新班接手。"
    - "原因之一：昨日下午剛與天下商人聯誼，初二仍適合承接回城後的商務流。"

  chusan:
    - "白御行宣布荷月初三商會補假一天。"
    - "必要值守另補，不以此剝奪休息。"
    - "初三中午安排定陶商會自己的慶功宴。"
    - "因此初二晚觀止慶功、初三中午商會慶功，形成連續兩場內部慶功。"
```

---

# 19｜初二晚觀止正門｜十一哥 × 紅娘 × 五兩官方蛋

```yaml
SHIYIGE_HONGNIANG_GATE_SHOW_V5_17:
  shiyige:
    - "十一哥仍自主留在觀止正門『兩處一門』的聲音／接觸位置。"
    - "他不是正式門房雇員。"
    - "可與路人、紅娘對話／互罵。"

  egg_business:
    price_per_egg: 5
    - "紅娘與十一哥的公開鬥嘴／相聲式互動繼續。"
    - "觀眾可判每回合誰輸並買官方蛋投輸方。"
    - "投紅娘不得瞄頭臉；投十一哥以其牆／接觸面為目標。"
    - "蛋錢是實際營業收入／帳務，不因慶功日完全消失。"

  gate_atmosphere:
    - "觀止正門當晚掛『今日歇業／晚間慶功，不接客』方向告示，但門口仍形成公開熱鬧。"
```

---

# 20｜紅娘舊床公開劈解／燒柴｜處分正式完成

```yaml
HONGNIANG_BED_DESTRUCTION_V5_17:
  prior_order:
    - "紅娘免除剩餘鐵籠生活後，舊床『拆／砍／燒』處分並未取消。"

  execution:
    - "初二晚，白三十二娘／白紅伶等把紅娘舊床抬到觀止正門。"
    - "白御行本人持斧，在眾人／街上可見範圍公開劈床。"
    - "紅娘口頭抗議、護床，但未改變既定處分。"
    - "床被實際劈成木料。"
    - "木料被搬入觀止廚下作慶功宴柴火使用。"

  result:
    - "紅娘床拆／砍／燒線至此已進入完成狀態；原床不再存在為可正常使用床榻。"
```

---

# 21｜紅娘 × 失仙九日營收局｜潘金蓮作棄賽結算，紅娘復牌

```yaml
HONGNIANG_SHIXIAN_CONTEST_CLOSE_V5_17:
  original_rules:
    start: "理火三年榴月二十三日"
    nominal_format: "九日雙籠營收競賽"
    accounting:
      - "只計真實營業收入。"
      - "純灌票不計。"
      - "二人各有錢箱／帳冊。"
    stakes:
      hongniang_if_loss: "『觀止首席紅牌』廣告牌交給失仙"
      shixian_if_loss: "日後再見紅娘時低頭承認本局輸"

  incomplete_numeric_record:
    - "失仙離場前存在過領先紅娘約168兩的階段。"
    - "全九日完整總營收沒有留下可直接比較的完整帳。"
    - "因此本次結算不是以偽造總額宣布紅娘數字勝。"

  current_event:
    - "失仙已離場／去向 UNKNOWN，並連續多日未返回觀止完成競賽。"
    - "初二晚潘金蓮以觀止大掌櫃身份在正門公開宣布：失仙中途離場、長期未返，本局作棄賽處理。"
    - "因此紅娘取得本局勝利，恢復／拿回『觀止首席紅牌』廣告牌。"
    - "若失仙日後再回來，紅娘有權按原彩頭要求她低頭承認本局輸；是否實際履行要等失仙本人重新出場。"

  strict_lock:
    - "棄賽結算 != 知道失仙為何消失。"
    - "棄賽結算 != 失仙死亡。"
    - "棄賽結算 != 浮月閣身份／妖化人真相公開。"
    - "棄賽結算 != 關閉失仙／沈家／陳州義莊／木牌主線。"
```

---

# 22｜失仙主線仍 OPEN

```yaml
SHIXIAN_OPEN_STATE_V5_17:
  public_route:
    current_location: "UNKNOWN"
    reason_for_absence: "UNKNOWN"
    return_time: "UNKNOWN"

  unresolved:
    - "失仙是否／何時回觀止。"
    - "失仙與浮月閣的公開關係。"
    - "失仙／陳州義莊女屍／木牌／現在身體之真實關係。"
    - "浮月閣『不是人』與失仙是否同類。"

  note:
    - "紅娘競賽結案只關閉營收賭局，不關閉失仙世界線。"
```

---

# 23｜夏蓮｜一夜期限已結束 × 四千五百萬大額清算 × 暫住觀止

```yaml
XIALIAN_CHUER_STATUS_V5_17:
  listing:
    - "初一以『夏蓮』名義的一夜自由成人掛牌已隨該夜結束。"
    - "一夜掛牌期限結束後，她不因昨日成交自動延長為李世民的第二日／永久 access。"

  settlement:
    gross: 50000000
    guanzhi_share: 5000000
    xialian_personal_share: 45000000
    status:
      - "本人四千五百萬兩大額權利／應收仍需後續清算、交割與安置。"
      - "最終支付工具／現銀／票據／國運轉換配比尚未全部固定。"
      - "她沒有因本 HOT 把四千五百萬贈給嬴政／秦國／李世民。"

  private_night:
    - "白紗帳／一夜成人私密內容仍不因日期已過而由 SAVE 倒推補全。"

  lodging:
    - "潘金蓮允許夏蓮在大額款項未完全清算前先住觀止。"
    - "房費採『先掛帳／賒帳』方向，不要求她當場支付。"
    - "精確房價與最終是否從何筆帳抵扣未固定。"
    - "暫住 != 正式長租、入職、再掛牌或加入人物池。"

  celebration:
    - "夏蓮已接受邀請，初二晚實際到觀止大堂慶功宴。"
```

---

# 24｜關盼盼｜潘金蓮提供免費廂房先落腳

```yaml
GUAN_PANPAN_LODGING_V5_17:
  room:
    location: "觀止後院東廂"
    current_price: "暫不收／潘金蓮提供免費落腳"
    - "潘金蓮安排關盼盼先在觀止住下，讓她休息，不要求她當日離樓另找客棧。"
    - "茶飯／日常先由觀止承接方向已顯影。"
    - "關盼盼以『先欠著』的語氣接受鑰匙／落腳。"

  status:
    - "免費廂房 != 正式加入觀止。"
    - "免費廂房 != 妓籍。"
    - "免費廂房 != 舞台契約。"
    - "免費廂房 != 成人掛牌。"
    - "免費廂房 != 潘金蓮取得關盼盼人身控制。"

  celebration:
    - "潘金蓮初二晚再請她到大堂，並重申今晚不談生意。"
    - "關盼盼已實際出席慶功宴。"
```

---

# 25｜初二晚慶功宴｜當前可見主要人員／位置

```yaml
GUANZHI_CELEBRATION_ENTRY_V5_17:
  guanzhi_shopkeepers:
    - "潘金蓮"
    - "龐春梅"
    - "李瓶兒"

  white_household_or_close:
    - "白御行"
    - "李師師"
    - "李瓶兒"
    - "張麗華"
    - "錦棠"
    - "白希／白三十二娘／白明礬／白紅伶等可按休息／到場狀態自然出入"

  guanzhi_people:
    - "紅娘（已復『觀止首席紅牌』廣告牌）"
    - "昨夜／本店相關姑娘與工作人員依補假／休息情況參與"

  invited_current_guests:
    - "關盼盼"
    - "夏蓮"

  gate:
    - "十一哥仍在門牆接觸位置；沒有建立其可正常進大堂就席／進食的身體條件。"

  note:
    - "此清單不是封閉名單；未明示者不因未列就自動離場／不存在。"
```

---

# 26｜關盼盼／夏蓮人物池法位｜討論前鎖定

```yaml
CHARACTER_POOL_PRE_DISCUSSION_LOCK_V5_17:
  current_lcapg:
    version: "V3.3.9"
    count: 62

  guan_panpan:
    lcapg_promotion_performed: false
    current_route_role:
      - "Route 新近高密度人物"
      - "湖心島燕子樓／白居易／蘇東坡線核心"
      - "目前暫住觀止"
    formal_world_status:
      - "未簽觀止留樓契約"
      - "未掛牌"
      - "未建立固定舞台合約"

  xialian:
    lcapg_promotion_performed: false
    current_route_role:
      - "趙姬／夏蓮 donor 線已在 Route 形成大量事件"
      - "初一限定一夜掛牌已完成"
      - "目前有四千五百萬本人應得款待清算"
      - "暫住觀止"
    formal_world_status:
      - "一夜牌已過期"
      - "未因一夜成交成為永久觀止姑娘"
      - "未建立新長期契約"

  discussion:
    status: "NOT_STARTED"
    next_mode: "DISCUSSION"
    rule:
      - "下一步可以討論二人是否值得／需要 promotion 進人物池。"
      - "討論本身不改 LCAPG；只有玩家明示『正式寫入／新增設定／更新人物池』才執行 SETTING／文件修改。"
```

---

# 27｜知情矩陣重要更新

```yaml
KNOWLEDGE_UPDATE_V5_17:
  public_or_widely_observed:
    - "關盼盼與白居易／蘇東坡在湖心島有公開燕子樓舊債對話。"
    - "蘇東坡寫成《定風波·湖心再逢燕子樓人》，關盼盼允許傳。"
    - "關盼盼破曉公開跳一折舞，並以『讓你們看看我自己』定位。"
    - "乾隆離場前問過疏影方向。"
    - "觀止初二歇業補假、晚間內部慶功。"
    - "觀止昨夜兩筆平台收益總額八百萬方向。"
    - "初二晚觀止門口紅娘床被公開劈成柴。"
    - "紅娘與十一哥仍可在正門鬥嘴／官方蛋營業。"
    - "潘金蓮公開宣布失仙棄賽、紅娘恢復『觀止首席紅牌』廣告牌。"

  private_or_limited:
    - "周邦彥／李師師破曉斷尾對話屬較安靜的私人／近距離場景，不自動成為天下公開傳聞。"
    - "顧青簡與沈萬三資金池的具體談判細節只在相關商務圈／知情者範圍，不自動公開。"

  remains_unknown:
    - "失仙目前去向與離場原因。"
    - "失仙／浮月閣／陳州義莊／木牌真相。"
    - "夏蓮與李世民一夜私密內容。"
    - "夏蓮四千五百萬最終資產配置。"
    - "阿麗婭七日內具體私密生活內容。"
    - "關盼盼最終是否留觀止／是否簽舞台約／是否掛牌。"
    - "關盼盼與白居易／蘇東坡未來關係是否繼續發展。"
```

---

# 28｜下一導演禁止偷補／漂移

```yaml
ANTI_BACKFILL_LOCKS_V5_17:
  - "不得再沿 V5.16 過廣夜渡鎖，把阿麗婭／忽必烈寫成初二才離島；二人已在夜渡停航前中途離島。"
  - "不得把顧青簡與沈萬三願意談寫成正式資金池契約已簽。"
  - "不得在七日結束前讓顧青簡完成阿麗婭二千七百萬定存交易。"
  - "不得把楊玉環主動靠近趙受益寫成愛情／性交／排他關係成立。"
  - "不得把六條寫成後來才到趙受益身邊；她整夜都在。"
  - "不得把李隆基的注視／被紅娘取笑寫成已採取報復。"
  - "不得把白居易／關盼盼寫成已和解、復合或相愛。"
  - "不得把蘇東坡『尋樓便尋卿』寫成關盼盼已接受追求。"
  - "不得替關盼盼新增第二首／第三首蘇東坡詞；破曉後蘇沒有再寫。"
  - "不得把潘金蓮給關盼盼免費東廂寫成她已加入觀止。"
  - "不得把關盼盼免費住房寫成欠身契／必須演出／必須掛牌。"
  - "不得重新開啟周邦彥對李師師的殘留浪漫追求，除非未來另有重大新因果。"
  - "不得把李師師回白家位置寫成所有權或失去花魁職業自主。"
  - "不得把乾隆問疏影寫成疏影已回應／已復合。"
  - "不得把八百萬平台收益寫成八百萬現銀已全部清點入庫；結算工具仍可有後續。"
  - "不得自行填三掌櫃分紅精確比例。"
  - "不得讓昨夜班繼續被當成初二白日收場主力；白班已由船帶來換班。"
  - "不得把觀止初二歇業誤寫成昨夜也歇業；昨夜本店照常由春梅主持。"
  - "不得把商會初二也放假；商會初二照常，初三補假。"
  - "不得把舍方知工錢寫成商會員工薪資或加入商會。"
  - "不得把十一哥寫成正式門房；他只是自主留在正門接觸位置。"
  - "不得把紅娘首席復牌寫成九日完整營收數字勝；本次是潘金蓮依失仙長期未返作棄賽結算。"
  - "不得因競賽結案關閉失仙主線。"
  - "不得把夏蓮一夜牌已結束寫成第二晚仍歸李世民。"
  - "不得把夏蓮四千五百萬寫成秦國／嬴政／唐國／李世民資產。"
  - "不得把夏蓮在觀止賒房寫成正式長住／入職／人物池 promotion。"
  - "不得把關盼盼或夏蓮寫成已進 LCAPG；下一步只是 DISCUSSION。"
```

---

# 29｜主要 OPEN THREADS

```yaml
OPEN_THREADS_V5_17:
  guan_panpan:
    - "是否留在觀止。"
    - "是否接受獨立舞台／舞蹈營運合作。"
    - "演出頻率、票價、分成、觀眾 access。"
    - "是否永遠只賣舞／未來是否本人選擇掛牌。"
    - "與白居易舊債後續。"
    - "與蘇東坡夢／新詞後續。"
    - "是否適合 promotion 進 LCAPG（待 DISCUSSION）。"

  xialian:
    - "四千五百萬本人款之實際清算工具／落袋方式。"
    - "是否接受顧青簡／商會的存款或資金池提案。"
    - "初二後在觀止住多久。"
    - "後續是否還掛牌／以何身份活動。"
    - "是否適合 promotion 進 LCAPG（待 DISCUSSION）。"

  aliya:
    - "七日首主期間的實際生活／事件。"
    - "七日後是否與顧青簡談二千七百萬存款。"

  gu_qingjian_merchants:
    - "沈萬三／定陶短池、長池、聯合池正式談判。"
    - "胡雪巖／伍秉鑑等是否加入、如何分工。"

  shixian:
    - "當前去向。"
    - "浮月閣／陳州義莊／木牌真相。"
    - "若再回來是否履行向紅娘低頭認輸彩頭。"

  shiyige:
    - "拓撲／開門精確結算。"
    - "3%帳戶／信託草案本人是否接受。"
    - "疏影是否接受美人牆／罵門畫作。"

  household:
    - "李師師疑孕仍未確診。"

  celebrations:
    - "初二晚觀止慶功宴尚未真正展開主菜／席間事件。"
    - "初三中午定陶商會慶功宴尚未發生。"
```

---

# 30｜最新接關座標

> **時間：理火三年荷月初二晚。精確時辰 UNKNOWN。**
>
> **地點：觀止青樓。**
>
> 初二白日，觀止已依潘金蓮命令整日歇業補假；定陶商會則照常運作，並排定初三補假與中午慶功。昨夜湖心島原班人員已由新班接手，不再續熬。
>
> 初二晚，觀止正門先完成一輪公開鬧場：十一哥在牆中與紅娘互罵／相聲，五兩官方蛋繼續賺錢；白御行把紅娘舊床當眾劈成柴，送進廚下。
>
> 潘金蓮其後在正門正式結算紅娘×失仙九日營收局。由於失仙中途離場且多日未返、完整九日帳無法形成，潘金蓮沒有偽造總營收，而是判失仙棄賽；紅娘恢復「觀止首席紅牌」廣告牌。失仙本人去向與主線仍 OPEN。
>
> 關盼盼目前住觀止後院東廂，潘金蓮暫不收房錢，只提供落腳；她沒有簽留樓、舞台、掛牌或妓籍契約。她已受邀並到場參加今晚慶功。
>
> 夏蓮初一的一夜掛牌期限已結束。五千萬成交中，她本人應得四千五百萬仍有大額清算工作；潘金蓮准她先在觀止賒帳住下。她也已到今晚慶功宴。這不延長李世民的一夜 access，也不建立永久觀止身份。
>
> **當前大堂慶功宴即將／剛開始。玩家在此下令 HOT SAVE，故事必須凍結。下一步不是自動續宴，而是轉入 DISCUSSION，討論「關盼盼與夏蓮是否適合進人物池」。**

---

# 31｜HOT V5.17 完整性聲明

```yaml
VALIDATION_V5_17:
  story_frozen: true
  predecessor_preserved: true
  predecessor_correction_recorded: true

  master_write_performed: false
  rcl_write_performed: false
  character_pool_write_performed: false

  current_date: "理火三年荷月初二"
  current_daypart: "晚"
  current_location: "觀止青樓"

  aliya_kublai_departure_corrected: true
  aliya_seven_day_line_open: true

  guan_bai_su_dawn_line_saved: true
  su_new_ci_saved: true
  guan_dawn_dance_saved: true
  guan_retention_contract_auto_created: false

  zhou_shishi_romantic_closure_saved: true
  zhou_residual_pursuit_left_open_without_cause: false

  guanzhi_chuer_holiday_saved: true
  guanzhi_celebration_saved: true
  dingtao_chusan_holiday_saved: true
  dingtao_celebration_not_yet_occurred: true

  hongniang_bed_destroyed: true
  hongniang_first_red牌_restored: true
  shixian_contest_close_basis: "FORFEIT / ABSENT, NOT NUMERIC TOTAL WIN"
  shixian_worldline_closed: false

  guan_panpan_lodging_saved: true
  guan_panpan_joined_guanzhi: false
  guan_panpan_lcapg_promotion: false

  xialian_one_night_listing_expired: true
  xialian_45m_fully_cash_settled_assumed: false
  xialian_lodging_on_credit_saved: true
  xialian_lcapg_promotion: false

  next_mode: "DISCUSSION"
  next_topic: "關盼盼／夏蓮是否適合進人物池"
  status: "HOT SAVE V5.17 READY"
```
