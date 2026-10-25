# 觀止青樓｜白御行線 HOT SAVE V5.12
## 理火三年榴月二十六日晚後續～榴月二十七日晚｜顧青簡白家夜訪 × 私人成人事件 × 青蛙／頂呱呱構想 × 生育條件夜談 × 李師師疑孕晨談 × 白家關係位階校正 × 張麗華初一供酒 × 酒鬼俱樂部邀請 × 九幽帝王信件外送完整固化版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V5_12_LIU27_NIGHT_GU_VISIT_SHISHI_SUSPECTED_PREGNANCY_LIHUA_WINE_JIUYOU_LETTERS"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V5.12"
  record_type: "HOT_SAVE"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"

  story_time_span:
    start: "HOT V5.11 後／理火三年榴月二十六日晚；白御行已表示準備離開觀止回白家"
    current: "理火三年榴月二十七日晚／入夜；白家；晚飯後；九幽信件已交入外送路線"
  exact_clock: "UNKNOWN"
  record_state: "STORY_FROZEN_BY_HOT_SAVE_COMMAND / POST_LETTER_DISPATCH / SUBSEQUENT_HOLD_DISCUSSION_EXCLUDED"

  previous_valid_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V5.11_榴月二十六日晚_嫪毐挑戰_夏蓮初一限定掛牌_商人心法_車輪採訪證_紅娘初一出籠_白玉池邀請_離場前凍結版.md"
    status: "VALID_CANONICAL_V5_11"

  long_term_master_at_time_of_story:
    file: "觀止青樓_白御行線_MASTER_SAVE_V5.5-R2-HARD_全歷史自足_E01-E113_保留V5.6-V5.7_HOT版.md"
    status: "PRE_PROMOTION_MASTER / SUPERSEDED_BY_SEPARATE_MASTER_V5_9_BUILD_IN_SAME_SAVE_OPERATION"

  overlay_chain_before_master_promotion:
    - "MASTER V5.5-R2-HARD"
    - "HOT V5.6【REBUILD-R1】"
    - "HOT V5.7"
    - "HOT V5.8"
    - "HOT V5.9"
    - "HOT V5.10"
    - "HOT V5.11"
    - "HOT V5.12（本檔）"
```

---

# 0｜現行生成／治理法位【V5.12 文件級】

```yaml
GENERATION_PROFILE_V5_12:
  baseline_manifest: "GUANZHI V15 CURRENT BASELINE"
  constitutional_root: "LIHUO PROTOCOL V2.3"
  lighter: "LIHUO LIGHTER V3.5.1-EXP"
  lihuo_ai_system: "LIHUO AI SYSTEM V3.5-EXP / conditional by Lighter"

  guanzhi:
    core: "GUANZHI MAIN V15"
    world: "GUANZHI WORLD V1"
    heart: "GUANZHI HEART V1"
    character_pool: "LCAPG V3.2 / 61 characters"
    route_memory: "EXTERNAL SAVE/HOT/MASTER"

  ceri:
    file: "成人古典中文語域與語料提供者_CERI_V0.4-EXP_床話作曲_SpeechFunction_詞彙近因_人物粗話簽名_FULL_CORPUS版.md"
    status: "PRESENT / OPTIONAL SUCCESSOR CANDIDATE / NOT AUTO-PROMOTED"

  environment:
    file: "觀止環境_V0.10-EXP_升格抽出狀態_上游交接待辦版.md"
    normal_story: "OFF_BY_DEFAULT"

  core_locks:
    - "PLAYER SPEECH / ATTEMPT / CHOICE / SELF-REPORT != WORLD RESULT"
    - "NPC DECISION / CONSENT / RELATION / KNOWLEDGE each require source"
    - "MONEY != RELATION"
    - "PAYMENT != ACCESS"
    - "ACCESS != RELATION"
    - "RELATION != CONSENT"
    - "RUMOR != FACT"
    - "ROLE != IDENTITY"
    - "PUBLIC LABEL != PRIVATE REALITY"
    - "SOURCE FUTURE != ROUTE DESTINY"
    - "SAVE = established event/evidence only"
```

---

# 1｜來源與 SAVE 紀律

```yaml
SOURCE_LINEAGE_V5_12:
  inherited:
    - "MASTER V5.5-R2-HARD"
    - "HOT V5.6【REBUILD-R1】"
    - "HOT V5.7"
    - "HOT V5.8"
    - "HOT V5.9"
    - "HOT V5.10"
    - "HOT V5.11"

  current_live_commit:
    - "HOT V5.11 凍結後至本次 HOT SAVE 命令前之直接 STORY。"
    - "玩家對白御行自身言語、行動、選擇、商業構想、信件內容與出價意向之明示。"
    - "顧青簡、李師師、張麗華在場可觀察言語／行動／接受／拒絕／工作回報。"
    - "玩家對白家人物位階、居住狀態與前段連續性錯誤之明示校正。"

SAVE_DISCIPLINE_V5_12:
  - "顧青簡夜訪成人事件只保存事件成立、邊界、當事人決定與必要生殖後果狀態；不保存露骨 mechanics。"
  - "顧青簡與白御行談生育，不建立懷孕、受孕協議、婚姻、妾位或已決定生子。"
  - "李師師孕況固定為 SUSPECTED / HIGH SUSPICION；不是 CONFIRMED，也不是 plain UNKNOWN。"
  - "味覺／食慾改變是可觀察證據，不單獨證成懷孕。"
  - "初一夏蓮掛牌是已成立的一夜成人床牌方向；精確競價條款、最終服務、得主與實際事件仍待世界發生。"
  - "九幽信件已離開白家；收件、相信、轉述、出席、競價、報復等後續全部 PENDING。"
  - "白御行所述九幽國運／陰德換陽間資金模式，保存為其既有商業安排之自述與本夜商業理由；未在本 HOT 新造不可觀測底層機制。"
  - "HOLD 後關於張麗華／李師師聲紋、V15 架構、Environment 權力拆分等討論不屬世界事件，不寫入 SAVE。"
```

---

# 2｜V5.11 後｜白御行返白家 × 顧青簡私下夜訪

```yaml
GU_QINGJIAN_PRIVATE_VISIT:
  date: "理火三年榴月二十六日晚～二十七日破曉前"
  location: "白家後園／池邊亭與白家私人空間"
  arrival:
    - "顧青簡依先前約定私下到白家。"
    - "由後門入，不坐車，不帶公開排場。"
    - "攜薄文書袋。"
    - "穿私人紫／藕紫色低領薄衣；不是商會工作服。"
  relation_context:
    - "白御行以『清簡』稱呼她。"
    - "二人已有既存地下情／成人歷史。"
    - "本夜仍需由當下人物行動重新成立，不靠歷史 blanket consent。"
```

---

# 3｜顧青簡 × 白御行｜本夜成人事件與生殖邊界

```yaml
GU_BAI_ADULT_EVENT_V5_12:
  status: "ESTABLISHED_VOLUNTARY_ADULT_EVENT"
  observable:
    - "顧青簡本夜是為白御行私人而來。"
    - "她先主動拉近／親吻，之後雙方自願升高為成人事件。"
    - "當夜有『呱』／『白呱呱』玩笑；只屬本夜語境，不形成永久稱號。"

  reproductive_boundary:
    - "顧青簡本夜不接受精液進入生殖道。"
    - "她允許其他不形成該生殖風險的成人收束方式，並保持自己對節奏與位置的控制。"

  locks:
    - "本夜成人事件 != 受孕"
    - "本夜成人事件 != 懷孕"
    - "本夜成人事件 != 生子承諾"
    - "本夜成人事件 != 婚姻／如夫人／妾位"
    - "既有地下情 != 未來 blanket consent"
```

---

# 4｜青蛙／「頂呱呱」生意構想

```yaml
FROG_BUSINESS_IDEA:
  status: "DISCUSSION / BUSINESS IDEA ONLY"
  established:
    - "白御行與顧青簡談可食用青蛙的供應、季節、價格、烹調、養殖可能。"
    - "白御行提出『頂呱呱』作生意／品牌玩笑方向。"
    - "白御行使用『牛蛙』一詞，屬其自身術語，不自動建立本地既有分類。"
    - "方向為先低調做市場調查，再試菜／標準化／放大。"
  not_established:
    - "未成立公司／店鋪。"
    - "未簽供貨。"
    - "未形成固定價格。"
    - "未建立大規模養殖。"
```

---

# 5｜顧青簡生育／孩子談話

```yaml
GU_MOTHERHOOD_DISCUSSION:
  status: "CONDITIONAL_DISCUSSION / NO COMMITMENT"
  bai_position:
    - "白御行因顧青簡聰明而提出『若生孩子』方向。"
    - "談到孩子資產與未來安排。"

  gu_position:
    - "顧青簡明確區分『我的孩子』與『我替你生孩子』。"
    - "若未來選擇生育，孩子資產應獨立，不作白家可借用資金。"
    - "孩子不是投資商品。"
    - "她目前不想取得妾／如夫人身分。"
    - "若有一天她自己選擇做母親，白御行是她會認真考慮的人選之一；未作現在承諾。"

  current_result:
    conception_agreement: false
    pregnancy: "NOT_ESTABLISHED"
    child: "NOT_ESTABLISHED"
    concubine_status: false
```

---

# 6｜古代生殖知情生態 × 白御行現代知識 testimony

```yaml
GU_REPRODUCTIVE_KNOWLEDGE_ECOLOGY:
  legitimate_sources:
    - "母親／年長女性／穩婆等女性口傳"
    - "本人月事與身體經驗"
    - "有限婦人方／求子方／房中話"
    - "白御行對她說的內容"

  distinction:
    - "具身經驗 != 現代醫學理論"
    - "古代婦人知識 != 完全無知"
    - "白御行提出的受孕時機／頻率說法 = 白御行 testimony"
    - "顧青簡可記為『白御行說／天道教他的／待查』，不得因主角身份升格為世界醫學定律"
```

---

# 7｜觀止雙面與潘金蓮／流產傳聞討論

```yaml
GUANZHI_TWO_FACE_DISCUSSION_V5_12:
  bai_legal_source:
    chain:
      - "時空道人早期對李瓶兒等說觀止有兩副面孔"
      - "李瓶兒後向白御行轉述"
    result:
      - "白御行合法知道『觀止有兩副面孔』"
      - "白御行合法知道潘金蓮是最早承接因果籤並取得實際掌櫃位置的人之一"

  unknown:
    - "隱藏 owner 身份"
    - "隱藏 owner 為何選潘金蓮"
    - "觀止所有後台空間精確配置"

  abortion_claims:
    - "白御行提過宋蕙蓮／李桂姐與潘金蓮相關的流產／強制處置說法。"
    - "顧青簡追問來源與不同情形，不接受把猜測混成單一事實。"
    - "本 HOT 不建立潘金蓮曾強迫特定人物流產之新世界事實。"
```

---

# 8｜破曉｜顧青簡離開

```yaml
GU_DEPARTURE:
  time: "榴月二十七日破曉"
  established:
    - "後半夜主要轉為談話、休息與聽蛙聲。"
    - "顧青簡整理衣物／文書後由後門離開。"
    - "白御行送到後門附近。"
    - "街面已開始有人，她認為不需再送。"
    - "臨走以『少跟我談兩億隻蝌蚪』類話取笑白御行。"
  result:
    - "顧青簡安全離開白家。"
```

---

# 9｜榴月二十七日清晨～上午｜李師師共睡 × 疑孕狀態

```yaml
LI_SHISHI_MORNING_V5_12:
  location: "白家／李師師私人起居空間"
  established:
    - "白御行在顧青簡離開後回到李師師處，久違地與她相擁補眠。"
    - "李師師辨認並接受他靠近，把他的手拉到腰間。"
    - "她說今日若有人找白御行可先等，想先讓他陪睡。"
    - "此段成立抱睡／相擁，不成立新的成人事件。"

  pregnancy_state:
    state: "SUSPECTED / HIGH SUSPICION"
    basis_known_to_shishi:
      - "先前存在可能受孕的成人事件。"
      - "她本人已找醫者看過；醫者判斷高度可疑／很可能，但未確診。"
      - "其後有味覺／食慾變化。"
    not_confirmed:
      - "沒有確診。"
      - "沒有可見孕肚。"
      - "不因白御行稱『孕婦』或撤代言而升格。"
```

---

# 10｜李師師｜母職、花魁、自主決定與白家關係

```yaml
SHISHI_MOTHERHOOD_CAREER_DISCUSSION:
  established:
    - "李師師私下想像過孩子名字、睡哪裡、抱孩子、夜哭等畫面；均為假設想像。"
    - "她要求白御行在確診前不要對外宣稱她懷孕。"
    - "她把『是否懷孕』『是否留下』『是否繼續天下第一花魁』拆開。"
    - "若真確診，是否留下由她本人決定。"
    - "她不會只因職業就終止，也不會只因白御行高興就留下。"
    - "白御行表明最終決定在她。"
    - "她願意另外聽白御行的感受，但不交出決定權。"
    - "她對可能的終止風險要求不要把白御行的現代知識講成必然，會問懂婦人身體的人。"
    - "她承認自己想像孩子時，覺得『好像也不壞』。"
    - "她拒絕『有孩子就不能是第一花魁／自由女人』的二分法。"
    - "條件式表示：若真懷、真留下，孩子姓白可以。此句不建立現有孩子或未來出生結果。"
    - "她要求白御行接受：她即使抱著他的孩子，也仍可以保有自己的名聲、邀請、金銀與場子。"
    - "她說若留下，是在許多選擇裡仍留一個位置給白御行。"

  relationship_status:
    - "李師師是白家最早進門的如夫人／首席如夫人，不是普通情人。"
    - "她保留觀止房間、設席／花魁職業與自主流動。"
    - "舊輸出中否認白御行為『相公』的連續性錯誤作廢，不形成世界事實。"
```

---

# 11｜白家家庭位階／居住狀態【玩家明示校正】

```yaml
WHITE_HOUSE_CURRENT_RELATION_STRUCTURE:
  李師師:
    status:
      - "如夫人"
      - "首席如夫人"
      - "白家女主人級成員"
    residence:
      - "白家"
      - "觀止仍有房／職業生活"

  李瓶兒:
    status:
      - "如夫人"
      - "白家女主人級成員"
    residence:
      - "白家"
      - "觀止生活／房間依既有線延續"

  張麗華:
    status:
      - "情人"
      - "白家家內成員／非客人"
    residence:
      - "白家院內有自己的獨立小屋／房"
      - "可在白家自由來去"
      - "觀止亦有房"

  浮香:
    status:
      - "情人"
      - "白家家內成員／非客人"
    residence:
      - "白家院內有自己的獨立小屋／房"
      - "可在白家自由來去"
      - "觀止亦有房"

  locks:
    - "不得把張麗華／浮香寫成白家臨時客人。"
    - "不得把李師師降回戀人級。"
    - "如夫人 != 自動推定官籍正式正妻法位；未有來源的官方婚籍仍不得補全。"
```

---

# 12｜李師師 × 初一湖心島活動

```yaml
SHISHI_DAY1_PARTICIPATION:
  status: "CONDITIONAL_ACCEPTANCE"
  established:
    - "白御行向李師師完整說明初一下午商會＋夜間詩會／觀止安排。"
    - "李師師表示可出席下午席。"
    - "若對場子有幫助，可彈一兩曲。"
    - "不把演出變成偽裝商業代言。"
    - "若身體累可自行提前離開。"
    - "她對嫪毐車輪與呂不韋／夏蓮舊事有好奇。"
  not_established:
    - "當日實際出席尚未發生。"
    - "曲目尚未固定。"
```

---

# 13｜夏蓮初一限定掛牌｜成人床牌法位校正

```yaml
XIALIAN_LISTING_LOCK_V5_12:
  established:
    - "夏蓮／趙姬本人已選擇初一以『夏蓮』舊名限定掛牌一夜。"
    - "此掛牌方向是成人床牌／性服務的一夜掛牌，不是單純喝酒陪坐。"
    - "她不是對成人性事幼稚／天真人物；既有與嫪毐的私人性史可作她自身經驗來源。"

  still_pending:
    - "精確競價規則"
    - "最終價格"
    - "最終得主"
    - "床牌包含／排除的具體項目"
    - "當夜實際成人事件"

  sovereignty:
    - "一夜床牌 != 對所有競價者自動同意"
    - "成交項目仍受夏蓮本人與潘金蓮最終條件約束"
```

---

# 14｜榴月二十七日黃昏｜張麗華白家晚飯 × 初一供酒

```yaml
ZHANG_LIHUA_DINNER_AND_WINE:
  location: "白家主樓／家內晚飯空間"
  established:
    - "白御行黃昏醒來梳洗後找張麗華。"
    - "張麗華已在白家主樓吃飯飲少量酒；這是家內日常，不是客人蹭飯。"
    - "白御行詢問顧青簡是否已向她訂初一用酒。"

  lihua_report:
    epistemic_status: "ZHANG_LIHUA_TESTIMONY / BUSINESS REPORT"
    content:
      - "顧青簡已按定陶商會大客戶採購方式接洽，不走情面白送。"
      - "下午與晚間用酒分開估算。"
      - "顧青簡有問人數增加與臨時加席的備援。"
      - "酒莊按大客戶價做，正常獲利。"
      - "張麗華已預留存貨，較好的酒另行控制。"

  bai_instruction:
    - "初一人數只會多不會少，寧可多備，不要不足。"
    - "湖心島補運麻煩，不能等斷酒才補。"

  lihua_adjustment:
    - "不再把最初估算人數當上限。"
    - "普通酒加大備貨。"
    - "高級酒分開控量。"
    - "備貨分散，避免單點斷供。"
    - "寧可隔日退回酒莊，也不要當晚酒乾。"

  accounting_lock:
    - "精確採購量／單價／折扣／付款仍未在本 HOT 獨立核帳。"
```

---

# 15｜白家女人湖心島家宴構想

```yaml
WHITE_HOUSE_LAKE_ISLAND_FAMILY_OUTING:
  status: "PROPOSAL"
  established:
    - "白御行提議初一大場忙完後，白家自己人另找時間去湖心島。"
    - "張麗華支持『初一是做給天下人看，之後我們自己去一次』的方向。"
    - "她自然列到師師、瓶兒、自己、浮香，再看當時誰真想去。"
    - "不替任何人預先確認出席。"
    - "方向是不上商務、不掛牌、不請外客，以吃喝、釣魚、休息、夜燈為主。"
    - "日期未定。"

  guanzhi_tab_banter:
    - "白御行提到自己曾在觀止壓一萬兩供張麗華扣款／飲用。"
    - "張麗華以『賣自己酒莊的酒、喝你觀止帳上的酒才會過日子』取笑。"
    - "精確剩餘預存款 UNKNOWN。"
```

---

# 16｜初一晚場｜易安居士、柳如是與「酒鬼俱樂部」邀請

```yaml
DRINKERS_CLUB_INVITATIONS:
  invitees:
    - "易安居士／李清照"
    - "柳如是"
    - "張麗華酒鬼俱樂部其他可找到的成員"

  identity_lock:
    - "上述人物不是觀止姑娘／員工。"
    - "只能邀請，不能點名命令出席。"
    - "她們在觀止有既有白吃白喝／朋友招待型特權，不等於妓籍。"

  planned_invitation_copy:
    text: "初一晚場——喝酒喝到吐。免費。白會長買單全場。"

  current:
    - "邀請方向／文案已定。"
    - "是否已逐封實際送達未在本段明確觀察。"
    - "任何人是否接受、是否來場均 UNKNOWN。"
```

---

# 17｜九幽帝王經濟 × 白御行拱火目的【白御行自述】

```yaml
BAI_JIUYOU_BUSINESS_EXPLANATION:
  source: "白御行向張麗華的本夜說法"
  established_as_bai_position:
    - "九幽帝王最重要的資產之一是各朝『國運』／陰德類資產。"
    - "白御行表示自己可用陽間可花用資金與九幽帝王交換其國運／陰德，再轉手給陽間需要平陰債的富豪。"
    - "白御行認為此中存在倍數價差，屬高利潤套利。"
    - "他提到十三娘此前曾取得漢朝國運，因而形成極強賭運；此處按既有路線事實／白御行所知延續，不另擴寫機制。"
    - "他拱夏蓮重新掛牌、準備把競價往上推的重要商業目的，是刺激九幽帝王為面子／舊帳投入國運與陰德資產。"
    - "白御行明示自己會在初一競價中出價、拱火到高價。"

  not_yet_executed:
    - "白御行尚未在初一實際出價。"
    - "任何帝王尚未因本次掛牌交付國運／陰德。"
    - "未形成新成交。"
```

---

# 18｜九幽信件外送｜嬴政、劉邦與其他帝王圈

```yaml
JIUYOU_LETTER_DISPATCH_V5_12:
  date: "理火三年榴月二十七日晚／晚飯後"
  location: "白家"
  established:
    - "白御行決定今晚不再出門。"
    - "在白家寫了多封信，主動把夏蓮初一重新掛牌消息送往九幽圈。"
    - "信件已封妥並交入熟悉的九幽外送／傳遞路線，離開白家。"

  exact_letters:
    嬴政:
      text:
        - "初一，汴梁觀止。"
        - "你媽要復出了。"
    劉邦:
      text:
        - "初一，汴梁觀止。"
        - "嬴政他娘夏蓮重新掛牌，一夜限定。"
        - "記得帶錢。"
        - "不夠找我借。"
        - "——白御行"

  other_letters:
    core_message:
      - "夏蓮，舊名趙姬，初一夜於觀止重新掛牌，只此一夜。"
      - "詳情到場自知。"
    discipline:
      - "不在信中替夏蓮／潘金蓮虛構尚未確定的競價細則或服務條款。"

  current_information_state:
    sender_action: "COMPLETED"
    recipient_receipt: "PENDING"
    recipient_belief: "UNKNOWN"
    rumor_spread: "PENDING"
    yingzheng_attendance: "NOT_ESTABLISHED"
    liubang_attendance: "NOT_ESTABLISHED"
    imperial_bids: "NOT_ESTABLISHED"
    retaliation: "NOT_ESTABLISHED"
```

---

# 19｜張麗華本段關係與聲紋污染鎖

```yaml
ZHANG_LIHUA_CONTINUITY_LOCK:
  canonical:
    - "張麗華是白御行情人。"
    - "她在白家院內有自己的私人小屋／房，家內自由來去。"
    - "她在觀止也有房。"
    - "她不是白家客人。"
    - "她有自己的酒莊與商業主體性。"

  invalidated_output:
    - "此前把她寫成『客人／來蹭飯』的語義錯誤撤回。"
    - "此前 HOLD 前最後一段若出現過度平板、AI 模組式張麗華語氣，只作生成品質／AUDIT 問題，不建立人物性格改變。"
```

---

# 20｜本 HOT 主要 OPEN THREADS

1. **九幽信件是否送達嬴政／劉邦／其他帝王**：PENDING。
2. **嬴政、劉邦與各朝帝王是否來、是否競價、如何回應**：UNKNOWN；不得因信件外送自動生成。
3. **白御行初一拱火出價**：意向已成立，實際出價尚未發生。
4. **夏蓮一夜成人床牌**：掛牌方向成立；精確規則、價格、得主、服務與實際成人事件未發生。
5. **呂不韋／趙姬／嫪毐初一各自行動**：依 V5.11 既有安排與人物決定推進，不自動封結果。
6. **李師師孕況**：SUSPECTED / HIGH SUSPICION；仍需後續來源才能 CONFIRM / RESOLVE。
7. **李師師若確診後是否留下**：由李師師本人決定；目前未決。
8. **錦棠代言／經紀約**：白御行已調整方向，但正式外部執行與最終簽署仍需程序／錦棠本人。
9. **張麗華初一酒水**：已有其工作回報與加量決定；精確數量／價格仍待帳務。
10. **易安居士／柳如是／酒鬼俱樂部**：邀請方向已定，接受與出席未知。
11. **白家女人湖心島家宴**：proposal；日期／參與者未定。
12. **顧青簡「頂呱呱」青蛙生意**：idea / research direction；未落地。
13. **顧青簡生育方向**：無懷孕、無受孕協議、無生子承諾。
14. **失仙／浮月閣／沈家／陳州線**：繼承 V5.11；本段未取得新硬消息。

---

# 21｜禁止下一導演偷補

- 不得把九幽信件「已寄出」寫成「嬴政／劉邦已收到」。
- 不得自動讓嬴政、劉邦、歷朝皇帝出現在初一。
- 不得自動生成帝王競價、國運轉讓或報復。
- 不得把白御行「會出價拱火」寫成已經出價。
- 不得把夏蓮成人床牌退回成單純喝酒陪坐，也不得反向把床牌寫成無限成人 access。
- 不得把夏蓮的妓籍／過往性史寫成對任何人的現在同意。
- 不得把李師師孕況寫成已確診。
- 不得把味覺變化寫成確診證據。
- 不得替李師師決定留胎／終止。
- 不得把李師師降級成普通情人；她是首席如夫人。
- 不得把李瓶兒降級成普通情人；她是如夫人。
- 不得把張麗華／浮香寫成白家客人。
- 不得把顧青簡夜談生育寫成已答應替白御行生孩子。
- 不得把顧青簡本夜成人事件外推成未來 blanket consent。
- 不得把「牛蛙／頂呱呱」寫成已開業生意。
- 不得把白御行的現代生殖說法升格成觀止醫學真理。
- 不得把潘金蓮強迫宋蕙蓮／李桂姐流產寫成已證實事件。
- 不得把張麗華供酒回報中的估量補成精確帳目。
- 不得把酒鬼俱樂部邀請寫成已全員接受。
- 不得把 HOLD 後聲紋／系統討論寫入世界。

---

# 22｜最新接關座標

> **理火三年榴月二十七日晚／入夜，白家。**
>
> 白御行今晚明示不再出門。晚飯後，他已在白家寫好並送出多封前往九幽的信，核心是把「夏蓮初一重新掛牌一夜」的消息送進帝王圈；給嬴政的是「你媽要復出了」，給劉邦則加上「記得帶錢，不夠找我借」。信件已離開白家，但任何收件人是否已收到、相信、轉述、動身或準備競價，全都尚未成立。
>
> 張麗華當下仍在白家家內活動；她不是客人。她已向白御行回報顧青簡對初一酒水的採購接洽，並在白御行提醒人數只會增加後決定把普通酒備量往上拉、分散備貨，高級酒另控。
>
> 白御行已明示自己初一會參與出價、把夏蓮場子往高價拱，理由之一是希望刺激九幽帝王拿國運／陰德類資產來換陽間資金，供其後續套利；但初一尚未到，任何實際出價與成交都沒有發生。
>
> 李師師目前孕況仍是 **SUSPECTED / HIGH SUSPICION**；已看過醫者且有味覺變化，但沒有確診。她若未來確診，是否留下由她本人決定。
>
> **本 HOT 之後的「張麗華很不像張麗華／整串 AI 味／模組套用／V15 架構拆分」全部進入 HOLD／DISCUSSION，不是世界時間。**
