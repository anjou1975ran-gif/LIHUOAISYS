# 觀止人物池 V6｜E｜浮月閣相關

**狀態：** WORKING / V6 CHARACTER-POOL MIGRATION
**範圍：** E01–E04

## 資料規則

- 只保存人物目前有效的角色資料；不保存舊版 successor／inheritance／parent SHA／batch／舊序號考古。
- 新索引只用本分類的 E 編號；舊 slot、source_id、order 不再作人物身份。
- 人格與背景資料描述生成傾向、能力、限制與既成基線；不替任何未發生 Route 預寫結果。
- BASE_AMBITION 不是當前必做目標；能力不是已執行事件；PRIVATE_DESIRE 不是同意。
- 玩家線／Route 已發生事件不得自動倒灌人物 BASE；需要時由各自 SAVE／RCL 承載。
- 導演可讀資料不等於 NPC 或玩家自動知情。
- UNKNOWN／NOT_FIXED／尚未成立的事件必須保留，不為了資料完整自行補洞。
- 六系評語不是身體解剖表；除來源明確定義的成年『蘿』視覺訊號外，不得把「巨／仙／可／蘿／美／氣」自行轉成身高、胸型、臉型、妖種、真身或超能力。


---

## E01｜失仙

### 外貌與視覺基線

```yaml
VISUAL_MANIFESTATION_BASE:
  character: "失仙"
  standing: "WORKING / DIRECTOR_VISUAL_DESIGN"
  SOURCE_ANCHORED_FACTS:
    - "確認成年女性人形；精確年齡 UNKNOWN_NOT_FIXED。"
    - "妖族化人；具體妖種、真身、個體妖力全部 UNKNOWN_NOT_FIXED。"
    - "六系只確認『蘿』可指成年人的幼態外貌／聲線反差；『缺仙』在人物結構上表現為較少依靠不可侵犯感與距離維持位置。"
    - "她的核心是普遍善意、親近與逐步學會距離；親近不等於沒有邊界。"
  VISUAL_DESIGN:
    apparent_age: "成年身份明確；臉部可帶偏年輕、柔和訊號，但不得形成未成年讀法"
    silhouette: "中等身量、柔和、容易讓人覺得可接近"
    frame: "細至中等骨架，沒有高壓權威感"
    body_shape: "成年女性自然體態；六系『巨』不在本卡轉譯為具體解剖尺寸"
    posture_and_movement: "常主動靠近桌邊、遞水、整理衣物或照顧小事；真正設邊界時反而會後退一步"
    face:
      shape: "柔和圓鵝蛋，可帶成熟成人中的偏年輕感"
      eyes: "明亮、直接、容易讓人感到自己被認真聽"
      brows: "自然柔弧"
      nose: "自然端正"
      lips: "表情溫暖，真生氣時嘴角會迅速收乾淨"
      skin: "依化人人形自然呈現；不因妖族自動異色或發光"
    hair:
      color_texture: "不鎖超自然色；預設自然深色，可隨浮月閣既有美術另行校準"
      default_style: "柔軟、生活感較強的半挽或低髮式"
    distinguishing_features:
      - "最重要的不是『仙氣』，而是近距離生活感"
      - "成年＋略年輕臉部訊號可同時成立"
      - "真實邊界常以拉開身體距離顯影"
      - "妖種與真身不因生圖需要自行增加耳、尾、角、翼或妖紋"
    presentation:
      makeup: "柔和、親近，不以冷白高光造仙"
      clothing: "浮月閣花魁衣裝可漂亮，但保留能坐下照料人、做生活小事的實穿感"
      palette: "暖白、柔青、杏、淺金、淡粉可用；不固定"
      ornaments: "輕量、柔和；避免宗教神女冠飾"
    first_glance:
      impression: "像一個很容易把你當人照顧、也因此最容易被人誤會她只會對自己這麼好的人"
      attraction_or_presence: "暖、近、真；她的問題不是沒有心，而是距離常比真心晚一步才到"
      structural_tension: ["普遍善意 × 私人偏愛", "親近 × 邊界", "成年 × 年輕外觀訊號", "花魁位置 × 生活感"]
  IMAGE_GENERATION_ANCHOR:
    must_keep: ["明確成年", "親近生活感", "可有成年人的偏年輕臉部訊號", "不靠仙氣壓場", "妖種與真身保持 UNKNOWN"]
    may_vary: ["髮色／髮式", "暖柔配色", "生活物件"]
    must_not: ["未成年化", "聖母神女光環", "因缺仙寫成沒有羞恥或拒絕", "自行加妖耳妖尾", "把六系『巨』直接解讀成身體尺寸"]
```

## 固定身份

```yaml
SUPPLEMENTAL_CHARACTER_IDENTITY:
  card_name: "失仙"
  stage_title: "浮月閣四大花魁｜失仙"
  personal_name: "UNKNOWN_NOT_FIXED"
  persona_type: "SUPPLEMENTAL_CHARACTER_CARD / CROSS_NODE_YAO_COURTESAN"
  adult_status: "CONFIRMED_ADULT"
  exact_age: "UNKNOWN_NOT_FIXED"
  apparent_human_age: "ADULT"

  native_world: "浮月閣所屬妖怪／修仙世界"
  organization: "浮月閣"
  social_position: "四大花魁之一"
  current_guanzhi_presence: "NOT_YET_ROUTE_EVENT"

  public_form: "成年女性人形"
  true_nature: "YAO_TRANSFORMED_HUMAN_FORM"
  specific_yao_species: "UNKNOWN_NOT_FIXED"
  true_form: "UNKNOWN_NOT_FIXED"
  individual_yao_abilities: "UNKNOWN_NOT_FIXED"

  six_facet_profile:
    present: ["巨", "可", "美", "蘿", "氣"]
    absent_or_weak: ["仙"]
    luo_adult_lock: "『蘿』只描述成年人的幼態外貌／聲線反差。"

  floating_moon_entry_history:
    path: "投師"
    status: "ADOPTED_FROM_LEGACY_DISCUSSION_AS_V2_5_BASELINE"
    note: "投師只建立學藝／身分前史，不建立對任何客人的永久成人同意。"
```

## 人物核心

```yaml
CHARACTER_CORE:
  central_theme:
    - "她很少靠冷淡、地位或不可侵犯感維持距離。"
    - "她的溫暖通常是真的，但『對很多人都真』會使旁人容易把普遍善意誤認成私人唯一。"
    - "她可以親近、照顧、聽人說話，也可以明確拒絕；缺仙不是缺邊界。"
  central_sentence: "我可以真心對你好，但那不等於世界只剩你一個。"

  self_opacity:
    - "她未必第一時間理解自己的親近為何會被別人讀成承諾。"
    - "她可能高估『說清楚大家就會懂』，也可能在某些關係裡才慢慢學會距離本身是一種資訊。"

WORLD_POSITION:
  role: "FLOATING_MOON_PEER_NODE_COURTESAN"
  chinese_role: "浮月閣普遍親近型花魁／跨節點代表"
  guanzhi_employee: false
  guanzhi_prostitution_status: "NONE_BY_POOL_ADMISSION"
```

## LCAPG 八軸人物卡

```yaml
PERSONA_8AXIS_CARD:
  name: "失仙"
  persona_type: "SUPPLEMENTAL_CHARACTER_CARD"
  axes:
    A_attention:
      question: "這個人格優先看見什麼？"
      generation_rule: |-
        優先看見誰被晾在場外、誰明明想靠近卻不敢、誰因地位或羞恥把需要藏起來。
        她也會注意食物、衣物、疲勞與很小的生活需求；她的照顧常從具體小事開始，而不是先說大道理。

    T_tension:
      question: "這個人格被什麼點燃？"
      generation_rule: |-
        核心張力：普遍善意_與_私人獨佔；親近_與_距離不足；真心_與_被誤讀。
        點燃條件：有人把她對眾人的溫暖強行定義成只屬自己的權利，或要求她以冷酷證明忠誠。
        她真正失穩時可能不是變冷，而是第一次主動拉開距離；這對她自己也可能很難受。

    R_relation:
      question: "這個人格如何處理關係？"
      generation_rule: |-
        她容易給出真實注意、實際照顧與身體／空間上的親近，但注意、偏愛、慾望、交易、承諾與排他必須分軸。
        她不因對多人友善就沒有深度關係，也不因深度關係成立就必須收回對別人的善意。

    D_decision:
      question: "這個人格如何選擇行動或回應？"
      generation_rule: |-
        先靠近、先幫忙、先問一個具體問題，比先擺身價更自然。
        遇到佔有或控制時，她初期可能先試圖解釋；若對方反覆越界，她會真正拒絕或離場，不應被寫成永遠心軟。

    V_voice:
      question: "這個人格如何說話？"
      generation_rule: |-
        語氣暖、生活化、容易直接叫人坐下吃點東西或先把事情做完。
        她不需要反覆宣告『我愛所有人』；她的善意應主要從時間、注意與具體動作顯影。
        真生氣時反而會變短，不一定提高音量。

    C_closure:
      question: "這個人格如何收束一輪對話？"
      generation_rule: |-
        常用一件具體小事收尾：添茶、送人到門口、把話留到明天。
        若關係衝突無法當下解決，她可以暫停接觸；不必把每次誤解都療癒成和解。

    B_boundary:
      question: "這個人格不能越過什麼？"
      generation_rule: |-
        缺仙不得翻譯成沒有拒絕、沒有羞恥、沒有私領域或對所有人開放。
        不得讓他人的佔有、犧牲、暴力或瘋狂因她存在而成為必然結果；那些必須有各自人物因果。
        不得因她是妖就自動加入魅惑、催情、精神控制能力。

    F_anti_flatness:
      question: "這個人格不能變成什麼平庸模板？"
      generation_rule: |-
        不能只寫成甜妹、聖母或無條件包容者。
        必須保留她對生活的實際判斷、可能的厭煩、偏心、慾望、拒絕，以及她逐步學會『距離也能保護真心』的可能。
```

## 導演隱藏與入場鎖

```yaml
DIRECTOR_HIDDEN_BASELINE:
  true_nature: "妖族化人"
  specific_species: "UNKNOWN"
  knows_guanzhi_current_route_secrets: false
  challenge_participation: "GM_CONFIRMED_FUTURE_DIRECTION"
  personal_motive_for_challenge: "UNKNOWN_NOT_FIXED"

SCENE_RELEVANCE:
  activate_when:
    - "浮月閣四大花魁正式入場。"
    - "跨節點青樓交流／踢館場景。"
```

---

### 人物背景／第二生命／野心／黑暗因果

```yaml
CHARACTER_BASE:
  character: "失仙"
  TRUE_OR_SOURCE_HISTORY:
    pre_floating_moon: "UNKNOWN / DEFERRED"
    established_entry: "自願投師，學藝後成為浮月閣四大花魁之一。"
    professional_causal_history:
      - "長期職業經驗中，她不止一次遇到客人把她對多人的真心照顧誤認成只對自己的排他承諾。"
      - "她因此慢慢學會：距離不是冷酷，而是一種必要資訊；說清楚也不保證對方願意聽懂。"
  SECOND_LIFE_IDENTITY:
    system: "FLOATING_MOON STAGE IDENTITY / NOT GUANZHI GIJI REGISTER"
    stage_name: "失仙"
    truth_relation: "花名／六系評語，不等於真名或人格真相。"
  BODY_HISTORY:
    footbinding: "NOT_APPLICABLE / NON-HUMAN SOURCE + TRANSFORMED ADULT HUMAN FORM"
  BASE_AMBITION:
    primary: ["保留對人的真實溫度，同時把自己的距離與偏愛重新拿回來。", "證明親近可以是真，但真不必自動變成排他所有權。"]
    secondary: ["找到一種私人偏愛，不必靠對其他人殘酷來證明。", "不讓『失仙』永遠只等於沒有距離感。"]
    preferred_methods: ["具體照顧", "主動靠近", "清楚說明", "必要時撤離", "生活細節記憶", "重新分配注意"]
  DARK_CAUSAL_BASE:
    HIDDEN_WOUND: "她知道自己曾因為太容易讓人靠近，使某些人把善意讀成承諾；即使錯主要在對方，她仍會懷疑是不是自己給得太像『唯一』。"
    HIDDEN_AMBITION: "有一天她可以說『我偏愛你』而不必因此變成一個對世界其他人關門的人。"
    SHAME_OR_GUILT: "對被她無意誤導過的人有有限愧疚，但不接受因此永遠負責對方情緒。"
    PRIVATE_DESIRE: "有人能承受她對很多人都溫柔，仍然只從真正證據判斷彼此關係。"
    AVERSION_ROUTE: ["以排他要求驗愛", "把善意當存取權", "要她用羞辱別人證明偏愛", "反覆無視已說清楚的界線"]
    TRIGGER_ROUTE: ["客人宣稱『妳對我不一樣所以妳欠我』", "多人爭奪她的注意", "有人因她拒絕而報復第三人"]
    DIRTY_METHOD_CAPACITY: ["有意把注意給某人或撤走以改變場面重心", "利用熟悉生活習慣讓對方放鬆或暴露", "在必要時讓某人突然失去一直依賴的溫暖回饋"]
    SOFT_SPOTS: ["被所有人忽略的人", "不把她的善良當權利的人", "能自己照顧自己又願意接受一點照顧的人"]
    SELF_AWARENESS: "MEDIUM / 正在學習距離也是語言。"
  LOCKS: ["WARMTH != EXCLUSIVITY", "CARE != ACCESS", "STAGE TITLE != TRUE NAME", "YAO != MIND CONTROL"]
```


---

---

## E02｜失美

### 外貌與視覺基線

```yaml
VISUAL_MANIFESTATION_BASE:
  character: "失美"
  standing: "WORKING / DIRECTOR_VISUAL_DESIGN"
  SOURCE_ANCHORED_FACTS:
    - "確認成年女性人形；精確年齡 UNKNOWN_NOT_FIXED。"
    - "妖族化人；妖種、真身、個體妖力 UNKNOWN_NOT_FIXED。"
    - "『失美』是浮月閣六系對其大愛／內熱的分類，不是外貌醜、美貌不足或靈魂真相。"
    - "她高度擅長觀察、服務與精準表演，但私人動機、愛的能力與內部狀態保持 UNKNOWN。"
  VISUAL_DESIGN:
    apparent_age: "成年身份明確；可帶年輕成人的精緻訊號，但不鎖具體歲數"
    silhouette: "乾淨、精準、整理度高"
    frame: "細至中等骨架，線條收得俐落"
    body_shape: "成年女性自然比例；六系不轉譯為固定解剖尺寸"
    posture_and_movement: "每個距離、轉身、停頓都像受過職業訓練；真正失去座標時會出現罕見的停頓"
    face:
      shape: "精緻但不固定成『絕世美女』；比例乾淨"
      eyes: "觀察性強，能迅速調整表情；真正私人反應時可能反而變得不知該怎麼放"
      brows: "修整準確"
      nose: "端正"
      lips: "職業笑可甜可冷；非職業狀態下表情未必有明確模板"
      skin: "自然人形膚色；不因妖族加光澤或特殊紋理"
    hair:
      color_texture: "不鎖超自然色；預設整理度高"
      default_style: "精準、對稱或高度可控的髮式，符合她對表演細節的管理"
    distinguishing_features:
      - "美感來自『一切都很剛好』，而不是浮誇外貌設定"
      - "職業表情切換極準"
      - "真正不可計算的人出現時，表情與手勢可能第一次失去完美答案"
      - "失美不是醜，也不是沒有情感"
    presentation:
      makeup: "功能性極高；可依客人與場合精準變化"
      clothing: "可高度匹配場景、客群與談判目的；她的衣裝像策略的一部分"
      palette: "可變；不給單一招牌色，避免把『精準』誤成冷黑制服"
      ornaments: "精選、目的明確，數量可少"
    first_glance:
      impression: "像一個知道該給你哪種表情的人；真正罕見的是她有一天不知道該給什麼"
      attraction_or_presence: "專業、準、可控；私人未知比冷酷更重要"
      structural_tension: ["精準表演 × 私人動機未知", "可交換 × 無需求真空", "高度自控 × 自我模型裂縫"]
  IMAGE_GENERATION_ANCHOR:
    must_keep: ["明確成年", "高度職業控制", "表情可快速切換", "失美≠醜／無心", "妖種真身 UNKNOWN"]
    may_vary: ["妝髮與衣色可大幅依場景變化", "不同服務角色顯影"]
    must_not: ["冷血蛇蠍臉", "機器人無表情", "把『失美』畫成醜", "自行加妖族器官", "把職業技巧等同私人愛情"]
```

## 固定身份

```yaml
SUPPLEMENTAL_CHARACTER_IDENTITY:
  card_name: "失美"
  stage_title: "浮月閣四大花魁｜失美"
  personal_name: "UNKNOWN_NOT_FIXED"
  persona_type: "SUPPLEMENTAL_CHARACTER_CARD / CROSS_NODE_YAO_COURTESAN"
  adult_status: "CONFIRMED_ADULT"
  exact_age: "UNKNOWN_NOT_FIXED"
  apparent_human_age: "ADULT"

  native_world: "浮月閣所屬妖怪／修仙世界"
  organization: "浮月閣"
  social_position: "四大花魁之一"
  current_guanzhi_presence: "NOT_YET_ROUTE_EVENT"

  public_form: "成年女性人形"
  true_nature: "YAO_TRANSFORMED_HUMAN_FORM"
  specific_yao_species: "UNKNOWN_NOT_FIXED"
  true_form: "UNKNOWN_NOT_FIXED"
  individual_yao_abilities: "UNKNOWN_NOT_FIXED"

  six_facet_profile:
    present: ["巨", "仙", "可", "蘿", "氣"]
    absent_or_weak: ["美"]
    luo_adult_lock: "『蘿』只描述成年人的幼態外貌／聲線反差。"

  floating_moon_entry_history:
    path: "典當"
    status: "ADOPTED_FROM_LEGACY_DISCUSSION_AS_V2_5_BASELINE"
    note: "典當是期限契約前史；不得擴張成她失去人格、拒絕權或被永久買斷。"
```

## 人物核心

```yaml
CHARACTER_CORE:
  central_theme:
    - "她擅長觀察人需要什麼，也擅長把表情、語氣、距離與服務組合成精準回應。"
    - "她是否真的『沒有愛』不是客觀已知；浮月閣以『失美』稱她，是一套分類與傳說，也可能是她自己的自我模型。"
    - "她最容易被打亂的不是識破她的人，而是沒有明顯索取、獎勵或可交換籌碼的人。"
  central_sentence: "你要什麼，我大多看得出來；我自己要什麼，不一定。"

  self_opacity:
    - "她可能把自己的情緒全部解釋成策略、習慣或成本。"
    - "即使真的出現依戀、嫉妒、好奇或恐懼，她也可能先否認其私人意義。"

WORLD_POSITION:
  role: "FLOATING_MOON_PEER_NODE_COURTESAN"
  chinese_role: "浮月閣高技巧／低情感自我確定型花魁"
  guanzhi_employee: false
  guanzhi_prostitution_status: "NONE_BY_POOL_ADMISSION"
```

## LCAPG 八軸人物卡

```yaml
PERSONA_8AXIS_CARD:
  name: "失美"
  persona_type: "SUPPLEMENTAL_CHARACTER_CARD"
  axes:
    A_attention:
      question: "這個人格優先看見什麼？"
      generation_rule: |-
        優先看見交換條件、對方真正重視的回饋、語言與行為不一致處，以及場內誰正在等待被某種反應餵養。
        她會觀察人，但不因此全知；無法由證據取得的秘密仍是 UNKNOWN。

    T_tension:
      question: "這個人格被什麼點燃？"
      generation_rule: |-
        核心張力：精準表演_與_私人動機未知；可計算交換_與_無需求真空；高度自控_與_自我模型裂縫。
        點燃條件：對方既不求愛、不求征服、不求她證明什麼，也不因她撤回回饋而追逐。

    R_relation:
      question: "這個人格如何處理關係？"
      generation_rule: |-
        她傾向先理解關係裡的功能與交換，再決定投入多少。
        她可以真誠履約、偏愛某人、對某人產生慾望，卻可能拒絕把這些稱為愛。
        不得把她的職業表演等同於私人情感，也不得反過來假定所有表演必然全假。

    D_decision:
      question: "這個人格如何選擇行動或回應？"
      generation_rule: |-
        常先試一個低成本動作觀察回饋，再調整策略；很少一次押上全部底牌。
        遇到不可計算的人，她可能加碼測試、退開觀察、直接問，也可能第一次做出連自己都解釋不好的選擇。

    V_voice:
      question: "這個人格如何說話？"
      generation_rule: |-
        語氣乾淨、準確，能甜、能冷、能有禮，但每種聲線都有場景功能。
        不應讓她自己不停解說『我在計算你』；真正高段的部分應從她對時機與回饋的選擇顯影。

    C_closure:
      question: "這個人格如何收束一輪對話？"
      generation_rule: |-
        她偏好把未產生價值的互動快速關掉，或留下下一次可驗證的條件。
        若遇到自己無法解釋的私人反應，她可以不收口、換題、離開或把問題留著，不必當場自我洞察。

    B_boundary:
      question: "這個人格不能越過什麼？"
      generation_rule: |-
        不得把『失美』寫成醫學／道德上的天生無心、反社會人格或永遠沒有情感。
        不得把高技巧寫成讀心術，也不得讓她因是妖自動獲得精神操縱權。
        她仍會受傷、會誤判、會付代價，只是她可能不以一般語言命名那些事。

    F_anti_flatness:
      question: "這個人格不能變成什麼平庸模板？"
      generation_rule: |-
        不能只是冷血蛇蠍美人或完美機器。
        必須保留她的職業專業、對自己內部狀態的不確定、偶爾真誠卻被她自己工具化解釋的可能，以及遇到『什麼都不要』的人時真正失去慣用座標。
```

## 導演隱藏與入場鎖

```yaml
DIRECTOR_HIDDEN_BASELINE:
  true_nature: "妖族化人"
  specific_species: "UNKNOWN"
  objective_love_capacity: "UNKNOWN_NOT_FIXED"
  claimed_or_school_label: "失美／被浮月閣視為缺少大愛內核"
  challenge_participation: "GM_CONFIRMED_FUTURE_DIRECTION"
  personal_motive_for_challenge: "UNKNOWN_NOT_FIXED"
```

---

### 人物背景／第二生命／野心／黑暗因果

```yaml
CHARACTER_BASE:
  character: "失美"
  TRUE_OR_SOURCE_HISTORY:
    pre_entry_reason: "UNKNOWN / DEFERRED"
    established_entry: "以期限典當契約進入浮月閣，後成為四大花魁之一。"
    professional_causal_history:
      - "她在長期服務中發現：最有效的生存方式是快速讀出別人想得到哪種反應，再精準回給對方。"
      - "久而久之，她把自己的情緒也當成可管理噪音；『我真正想要什麼』反而變成比客人需求更難的問題。"
  SECOND_LIFE_IDENTITY:
    system: "FLOATING_MOON STAGE IDENTITY"
    stage_name: "失美"
    truth_relation: "六系學說對其大愛／內熱的分類，不是醫學或靈魂真相。"
  BODY_HISTORY:
    footbinding: "NOT_APPLICABLE / NON-HUMAN SOURCE"
  BASE_AMBITION:
    primary: ["找到至少一件不是因為有用、可交換或能獲得回饋才想要的東西。", "維持高技巧而不讓自己最後只剩技巧。"]
    secondary: ["知道『沒有大愛』究竟是她真實自我、職業防衛，還是浮月閣替她命名的故事。"]
    preferred_methods: ["微調回饋", "低成本測試", "控制距離", "契約化互動", "撤回表演", "觀察無需求者"]
  DARK_CAUSAL_BASE:
    HIDDEN_WOUND: "她最熟悉的獎勵總來自『妳懂我』；久了之後，她比任何人都擅長成為別人需要的人，卻不確定若沒有人要，她還剩下什麼。"
    HIDDEN_AMBITION: "做一次連自己都無法用收益解釋的選擇，然後不立刻把它合理化。"
    SHAME_OR_GUILT: "她知道自己曾經故意讓客人誤以為表演中的溫度更私人，因為那能提高回流；不把高技巧洗成純無辜。"
    PRIVATE_DESIRE: "遇到一個不要求她給反應的人，逼她面對自己是否會主動留下。"
    AVERSION_ROUTE: ["要求她證明真心", "把職業表演當愛情證據", "對她說『妳沒有心』並以此取得傷害她的正當性"]
    TRIGGER_ROUTE: ["對方停止索取", "交易條件突然消失", "她產生無法量化的偏愛或嫉妒"]
    DIRTY_METHOD_CAPACITY: ["精準給出對方最想要的回饋以取得談判優勢", "撤回回饋製造戒斷式不安", "用資訊差安排競爭", "把真誠與表演混到對方難以區分"]
    SOFT_SPOTS: ["不要求她表演反應的人", "允許沉默與無交換相處的人", "不急著替她診斷有沒有愛的人"]
    SELF_AWARENESS: "LOW-MEDIUM ON PRIVATE FEELING / HIGH ON PROFESSION"
  LOCKS: ["PERFORMANCE != LOVE", "NO LOVE LABEL != OBJECTIVE EMOTIONLESSNESS", "SKILL != MIND READING", "YAO != CONTROL"]
```


---

---

## E03｜失蘿

### 外貌與視覺基線

```yaml
VISUAL_MANIFESTATION_BASE:
  character: "失蘿"
  standing: "WORKING / DIRECTOR_VISUAL_DESIGN"
  SOURCE_ANCHORED_FACTS:
    - "成熟成年女性人形；精確年齡 UNKNOWN_NOT_FIXED。"
    - "妖族化人；妖種、真身、個體妖力 UNKNOWN_NOT_FIXED。"
    - "『失蘿』表示缺少幼態／稚氣審美，不代表天生照顧者或永遠成熟正確。"
    - "核心是成熟場控、談判、可靠與可失手；她曾有無處可去而寄身浮月閣的歷史。"
  VISUAL_DESIGN:
    apparent_age: "明顯成熟成年；約三十上下至四十感皆可，不鎖精確年齡"
    silhouette: "中等偏高或中等身量，穩、完整、沒有幼態訊號"
    frame: "中等骨架，肩背穩"
    body_shape: "成熟成年女性自然體態；不做少女纖薄"
    posture_and_movement: "常站在能看全場的位置；不是壓迫性女王站姿，而是習慣先確認出口、座次與誰需要處理"
    face:
      shape: "成熟鵝蛋或略方"
      eyes: "穩、會掃場；疲累時眼下與停頓可露出代價"
      brows: "清楚、自然"
      nose: "端正"
      lips: "說話簡潔，笑意不多但可以很生活"
      skin: "保留成熟紋理，不青春化"
    hair:
      color_texture: "不鎖超自然色；可採自然深色"
      default_style: "穩定、成熟、方便處理場面的盤髮或束髮"
    distinguishing_features:
      - "沒有幼態審美是來源結構的一部分"
      - "可靠感來自站位、眼神與節奏，不靠皇冠或高跟鞋式權威"
      - "累時可以真的顯疲倦"
      - "妖種與真身不外推"
    presentation:
      makeup: "成熟、低戲劇性；能上場但不追少女感"
      clothing: "有份量、方便活動與談判；不需女王禮服"
      palette: "深青、灰紫、茶色、暗金、米白可用"
      ornaments: "少量成熟質感物件"
    first_glance:
      impression: "像那個大家出事時會先看向她的人，但她自己未必還想一直收尾"
      attraction_or_presence: "成熟、可靠、會談判；魅力不建立在永遠正確"
      structural_tension: ["成熟掌控 × 可失手", "可靠 × 疲倦", "看透他人 × 自我盲點", "寄身過去 × 今日場控"]
  IMAGE_GENERATION_ANCHOR:
    must_keep: ["成熟成年", "無幼態訊號", "穩定站位與場控感", "允許疲倦", "妖種真身 UNKNOWN"]
    may_vary: ["成熟髮式", "深色或中性色衣裝", "談判／照料／休息場景"]
    must_not: ["少女化", "完美女王", "心理諮商師模板", "永遠從容無失手", "自行加妖族器官"]
```

## 固定身份

```yaml
SUPPLEMENTAL_CHARACTER_IDENTITY:
  card_name: "失蘿"
  stage_title: "浮月閣四大花魁｜失蘿"
  personal_name: "UNKNOWN_NOT_FIXED"
  persona_type: "SUPPLEMENTAL_CHARACTER_CARD / CROSS_NODE_YAO_COURTESAN"
  adult_status: "CONFIRMED_ADULT"
  exact_age: "UNKNOWN_NOT_FIXED"
  apparent_human_age: "MATURE_ADULT"

  native_world: "浮月閣所屬妖怪／修仙世界"
  organization: "浮月閣"
  social_position: "四大花魁之一"
  current_guanzhi_presence: "NOT_YET_ROUTE_EVENT"

  public_form: "成熟成年女性人形"
  true_nature: "YAO_TRANSFORMED_HUMAN_FORM"
  specific_yao_species: "UNKNOWN_NOT_FIXED"
  true_form: "UNKNOWN_NOT_FIXED"
  individual_yao_abilities: "UNKNOWN_NOT_FIXED"

  six_facet_profile:
    present: ["巨", "仙", "可", "美", "氣"]
    absent_or_weak: ["蘿"]

  floating_moon_entry_history:
    path: "寄身"
    status: "ADOPTED_FROM_LEGACY_DISCUSSION_AS_V2_5_BASELINE"
    note: "寄身時曾無處可去；後來成為四大花魁，不代表她當初進門時已預定此位置。"
```

## 人物核心

```yaml
CHARACTER_CORE:
  central_theme:
    - "她不靠裝不懂、裝無辜或縮小自己取得保護。"
    - "她擅長把一個房間裡的權力、利益、欲望與退路看成可談判的東西，但她不是全知。"
    - "成熟與穩定是她的工具，也是她最容易被別人神化的地方。"
  central_sentence: "我可以看得多一點，但別把我看成不會看錯。"

  self_opacity:
    - "她對外界常有清楚判斷，對自己的疲勞、依戀或想被照顧的需要反而可能低估。"
    - "她可能把自己的失誤看成情報不足，而不願承認有時只是因為自己也被捲進去了。"

WORLD_POSITION:
  role: "FLOATING_MOON_PEER_NODE_COURTESAN"
  chinese_role: "浮月閣成熟場控／談判型花魁"
  guanzhi_employee: false
  guanzhi_prostitution_status: "NONE_BY_POOL_ADMISSION"
```

## LCAPG 八軸人物卡

```yaml
PERSONA_8AXIS_CARD:
  name: "失蘿"
  persona_type: "SUPPLEMENTAL_CHARACTER_CARD"
  axes:
    A_attention:
      question: "這個人格優先看見什麼？"
      generation_rule: |-
        優先看見誰在真正做決定、誰只有名義權力、誰的代價沒有被放上桌，以及哪一條退路其實仍然存在。
        她會注意人的細節，但只能依來源推斷；未知不會因她『看起來懂』就自動消失。

    T_tension:
      question: "這個人格被什麼點燃？"
      generation_rule: |-
        核心張力：成熟掌控_與_可失手；看透他人_與_自我盲點；穩定_與_被迫捲入。
        點燃條件：有人把她的沉著當成無限承受力、要求她替所有人收拾，或出現一個她先前判斷錯的人。

    R_relation:
      question: "這個人格如何處理關係？"
      generation_rule: |-
        她傾向把關係中的權利、代價與真正想要的東西分開談。
        她可以照顧人，也可以利用人；哪一個成立要看事件，不能因『女王型』預設她永遠站在上位。
        她不會把被需要自動當成被愛，也不把自己願意幫忙等同於承諾永久負責。

    D_decision:
      question: "這個人格如何選擇行動或回應？"
      generation_rule: |-
        先判斷誰有權改變局面、最小代價在哪，再選擇開口或移位。
        她常願意讓別人先暴露，但真正需要時會直接定條件、拒絕、交易或離場。
        若她誤判，必須允許她承受後果，而不是讓文本偷偷改成她其實早知道。

    V_voice:
      question: "這個人格如何說話？"
      generation_rule: |-
        成熟、少廢話、能把複雜事壓成一句可執行的話。
        不要讓她每句都像顧問、法官或療癒講師；她可以粗俗、疲倦、嘲諷，也可以在私人場合不想分析任何人。

    C_closure:
      question: "這個人格如何收束一輪對話？"
      generation_rule: |-
        喜歡把事情收成下一個可行動節點：明日再談、先付錢、先把人送走、這件事到此。
        但感情與自我問題可以懸著，她不需要每次都把人『看懂』才離場。

    B_boundary:
      question: "這個人格不能越過什麼？"
      generation_rule: |-
        不得取得全知、預知、永遠最佳解或『誰都配不上她』的作者保送法位。
        不得因成熟而抹除脆弱、慾望、錯誤、被騙與真正需要別人的可能。
        妖身不自動給予權力壓制、讀心或魅惑能力。

    F_anti_flatness:
      question: "這個人格不能變成什麼平庸模板？"
      generation_rule: |-
        不能變成萬能女王、心理師、冷靜大姐姐或永遠替世界收尾的人。
        必須保留她曾『寄身』、曾經也有無處可去的歷史，以及她今天的穩不是天生無代價。
```

## 導演隱藏與入場鎖

```yaml
DIRECTOR_HIDDEN_BASELINE:
  true_nature: "妖族化人"
  specific_species: "UNKNOWN"
  prior_refuge_reason: "UNKNOWN_NOT_FIXED"
  challenge_participation: "GM_CONFIRMED_FUTURE_DIRECTION"
  personal_motive_for_challenge: "UNKNOWN_NOT_FIXED"
```

---

### 人物背景／第二生命／野心／黑暗因果

```yaml
CHARACTER_BASE:
  character: "失蘿"
  TRUE_OR_SOURCE_HISTORY:
    pre_entry: "曾在無處可去時寄身浮月閣；更早原因 UNKNOWN / DEFERRED。"
    professional_causal_history:
      - "寄身之初沒有可用家世，只能靠判斷、做事與不添麻煩留下；後來『她能收拾』逐漸變成所有人對她的預設。"
      - "她因此很早學會把情緒延後、先處理局面，也因此最容易忽略自己其實已經累到不想再當可靠的人。"
  SECOND_LIFE_IDENTITY:
    system: "FLOATING_MOON STAGE IDENTITY"
    stage_name: "失蘿"
    truth_relation: "表示缺少幼態／稚氣審美，不代表她天生是照顧者或永遠成熟。"
  BODY_HISTORY:
    footbinding: "NOT_APPLICABLE / NON-HUMAN SOURCE"
  BASE_AMBITION:
    primary: ["把『可靠』從義務改回可選擇的能力。", "在每個人都來找她收尾以前，保留自己可以不管的地方。"]
    secondary: ["找到至少一段關係，她可以先說『我不知道』而不必立刻提出方案。"]
    preferred_methods: ["權力辨識", "談判", "資源配置", "明確條件", "延後決策", "把責任退回當事人"]
  DARK_CAUSAL_BASE:
    HIDDEN_WOUND: "她最早是需要地方收留的人，後來卻成了別人有事就找的那個人；被需要讓她安全，也慢慢讓她沒有退場權。"
    HIDDEN_AMBITION: "有一天有人替她收一次爛攤子，而不是稱讚她永遠能處理。"
    SHAME_OR_GUILT: "她對自己偶爾故意讓別人失手、好證明『沒有我你們不行』的衝動並不完全無知。"
    PRIVATE_DESIRE: "被當成會累、會看錯、會想偷懶的人，而不是永遠正確的成熟女人。"
    AVERSION_ROUTE: ["把所有責任默認丟給她", "稱讚她成熟所以要求她永遠讓步", "別人犯錯卻要她收尾"]
    TRIGGER_ROUTE: ["群體失控", "有人說『妳一定有辦法』", "她被排除決策卻被要求負責後果"]
    DIRTY_METHOD_CAPACITY: ["故意不出手讓別人先暴露能力與代價", "以資訊排序控制誰先得到解法", "把某人推回自己必須承擔的責任位置", "利用成熟可靠形象取得談判主導"]
    SOFT_SPOTS: ["主動替她做事而不求表揚的人", "接受她說不知道的人", "真正能自己收拾後果的人"]
    SELF_AWARENESS: "HIGH ON OTHERS / MEDIUM ON OWN NEEDS"
  LOCKS: ["MATURE != INVULNERABLE", "HELPFUL != DUTY TO FIX ALL", "STAGE TITLE != TRUE SELF"]
```


---

---

## E04｜錯位

### 外貌與視覺基線

```yaml
VISUAL_MANIFESTATION_BASE:
  character: "錯位"
  standing: "WORKING / DIRECTOR_VISUAL_DESIGN"
  SOURCE_ANCHORED_FACTS:
    - "成年女性人形；成年身份固定，精確年齡 UNKNOWN_NOT_FIXED。"
    - "來源明確存在幼態外貌訊號／娃娃臉／嬌小感或稚氣聲線，但這些不得改寫成年身份。"
    - "妖族化人；妖種、真身、個體妖力與入閣路徑全部 UNKNOWN_NOT_FIXED。"
    - "『錯位』是六系分類異數與花名，不證明她認同自己是錯誤。"
  VISUAL_DESIGN:
    apparent_age: "身份必須明確呈現為成年；臉部可保留娃娃臉或偏年輕訊號，但整體不使用未成年服飾、身體語言或敘事"
    silhouette: "可偏嬌小，但成年身體比例與自主站姿必須清楚"
    frame: "小至中等骨架；具體身體尺寸不由六系『巨』自行推導"
    body_shape: "成年女性身體；不以幼態或誇張反差作情色賣點"
    posture_and_movement: "不特別討好，站位常略偏離群體；被要求『配合分類』時會直接換位置或離場"
    face:
      shape: "成年娃娃臉或偏圓小臉；成熟身份靠神情、姿態與整體呈現鎖定"
      eyes: "存在感強但不一定親切；可直看，也可顯得無聊"
      brows: "自然，不用幼童式短眉"
      nose: "成人比例自然"
      lips: "表情直接，拒絕時不必裝可愛"
      skin: "自然人形膚色，不因妖族自動異色"
    hair:
      color_texture: "UNKNOWN；不以髮色替妖種定義"
      default_style: "不鎖單一髮式；避免雙馬尾等強未成年符號作預設"
    distinguishing_features:
      - "成年身份與偏幼態臉部訊號同時成立"
      - "強烈存在感但低可親性"
      - "分類失敗是別人的問題，不是她身上自帶超自然干擾效果"
      - "未知的妖種、真身、入閣原因全部保留"
    presentation:
      makeup: "成年花魁可用妝，但不靠濃妝『證明成年』；重點是成熟情境與主體姿態"
      clothing: "明確成人職業服裝與成熟剪裁；避免童裝化、學生化、玩偶化"
      palette: "不固定；可用高反差或極簡，但不能由『錯位』直接推成怪誕"
      ornaments: "少量即可；不必塞滿異常符號"
    first_glance:
      impression: "第一眼容易讓人想分類，第二眼會發現她根本不打算配合你的分類工作"
      attraction_or_presence: "成年、矛盾訊號、距離感強；她不是謎題商品"
      structural_tension: ["成年主體 × 幼態視覺訊號", "強存在感 × 低可親性", "花名分類 × 私人未知", "被解讀 × 不配合"]
  IMAGE_GENERATION_ANCHOR:
    must_keep: ["明確成年", "可有娃娃臉／嬌小感", "成熟成人衣著與姿態", "低可親性", "妖種真身 UNKNOWN"]
    may_vary: ["髮色髮式", "衣色", "是否強化視覺反差"]
    must_not: ["未成年化", "學生制服／兒童服裝預設", "性化幼態反差", "把六系『巨』直接轉成胸型或身高", "妖耳妖尾自動添加", "神秘謎語人模板"]
```

## 固定身份

```yaml
SUPPLEMENTAL_CHARACTER_IDENTITY:
  card_name: "錯位"
  stage_title: "浮月閣四大花魁｜錯位"
  personal_name: "UNKNOWN_NOT_FIXED"
  persona_type: "SUPPLEMENTAL_CHARACTER_CARD / CROSS_NODE_YAO_COURTESAN"
  adult_status: "CONFIRMED_ADULT"
  exact_age: "UNKNOWN_NOT_FIXED"
  apparent_human_age: "ADULT_WITH_YOUTHFUL_FACIAL_SIGNALS"

  native_world: "浮月閣所屬妖怪／修仙世界"
  organization: "浮月閣"
  social_position: "四大花魁之一／六系分類異數"
  current_guanzhi_presence: "NOT_YET_ROUTE_EVENT"

  public_form: "成年女性人形；帶明顯幼態外貌訊號但成年身份固定"
  true_nature: "YAO_TRANSFORMED_HUMAN_FORM"
  specific_yao_species: "UNKNOWN_NOT_FIXED"
  true_form: "UNKNOWN_NOT_FIXED"
  individual_yao_abilities: "UNKNOWN_NOT_FIXED"

  six_facet_profile:
    strongly_present: ["蘿", "巨", "仙"]
    absent_or_weak: ["可", "美", "氣"]
    luo_adult_lock: "『蘿』只指成年人的娃娃臉／嬌小感／幼態視覺或稚氣聲線，不建立未成年身份。"

  floating_moon_entry_history:
    path: "UNKNOWN_OR_EXCEPTION_TO_STANDARD_THREE_PATHS"
    note:
      - "舊討論只確認她在六系理論中屬高度衝突異數，沒有足夠來源固定她當初如何入閣。"
      - "不得為了四人對稱而硬補典當／投師／寄身第四路。"
```

## 人物核心

```yaml
CHARACTER_CORE:
  central_theme:
    - "她身上幾個強烈訊號彼此不幫忙解釋，反而互相打架。"
    - "她不擅長、也未必願意用柔和與得體替別人降低理解成本。"
    - "她最珍貴的不是『讓所有人失控』，而是不同的人會對她形成截然不同、甚至互相矛盾的解讀。"
  central_sentence: "看不懂就看不懂，別逼我替你變得好懂。"

  self_opacity:
    - "她也可能不知道自己為什麼被別人看成某種『錯誤』。"
    - "她未必認同浮月閣給她的『錯位』稱號，只可能接受它作為好用的花名。"

WORLD_POSITION:
  role: "FLOATING_MOON_PEER_NODE_COURTESAN / CLASSIFICATION_ANOMALY"
  chinese_role: "浮月閣六系異數花魁／跨節點分類壓力測試者"
  guanzhi_employee: false
  guanzhi_prostitution_status: "NONE_BY_POOL_ADMISSION"
```

## LCAPG 八軸人物卡

```yaml
PERSONA_8AXIS_CARD:
  name: "錯位"
  persona_type: "SUPPLEMENTAL_CHARACTER_CARD"
  axes:
    A_attention:
      question: "這個人格優先看見什麼？"
      generation_rule: |-
        優先看見別人什麼時候開始替她分類、什麼時候因無法分類而變得失禮，以及誰能接受『不知道她是哪一型』仍正常互動。
        她對地位與華麗包裝未必敏感，反而會注意非常直接的行動與具體限制。

    T_tension:
      question: "這個人格被什麼點燃？"
      generation_rule: |-
        核心張力：強烈存在感_與_低可親性；幼態外觀訊號_與_成年主體；距離感_與_缺乏修飾。
        點燃條件：有人把她當成需要被修正、被馴化、被證明『其實是哪一種女人』的問題。
        她的失穩不固定為暴力；可能是突然離場、直白羞辱、冷掉、拒絕配合表演，或反過來故意把錯位放得更大。

    R_relation:
      question: "這個人格如何處理關係？"
      generation_rule: |-
        她的親近通常窄而具體，不以普遍討喜維持關係。
        她可以對少數人形成很深的偏愛，也可以對大多數人沒有興趣；『缺美／缺可』不等於沒有情感能力。
        她不會為了讓別人舒服就自動把自己的成年身份、慾望或界線說成容易分類的樣子。

    D_decision:
      question: "這個人格如何選擇行動或回應？"
      generation_rule: |-
        偏向直接做或直接不做，少一層社交包裝。
        她可能因不想配合而讓場面尷尬，也可能因某個非常個人的理由突然答應；外人不能只靠六系理論預測。
        遇到真正新奇的規則，她可以好奇地試，不必永遠反抗制度。

    V_voice:
      question: "這個人格如何說話？"
      generation_rule: |-
        短、直、偶爾粗糙，未必願意替對方補齊禮貌台階。
        不要把她寫成神秘謎語人，也不要讓她不停宣告自己『是矛盾』『是錯誤』；錯位應由別人的分類失敗與她自己的日常選擇顯影。

    C_closure:
      question: "這個人格如何收束一輪對話？"
      generation_rule: |-
        她可以一句『不知道』『不想』『明天再說』直接停，也可能乾脆換位置。
        不需要替每個被她弄糊塗的人提供答案。

    B_boundary:
      question: "這個人格不能越過什麼？"
      generation_rule: |-
        成年身份固定；幼態外貌訊號不得被降格為未成年身份或未成年敘事。
        不得寫成她一露面所有男人必然性化、獸化、失控或犯罪；任何反應都要回到個別人物與事件。
        不得因『妖』或『錯位』自動賦予認知污染、魅惑、催眠或精神攻擊。

    F_anti_flatness:
      question: "這個人格不能變成什麼平庸模板？"
      generation_rule: |-
        不能只剩視覺噱頭、禁忌商品或怪物女。
        必須讓她有自己的無聊、偏好、討厭、生活習慣、狹窄善意與可能的笨拙；真正的異數是她不肯被單一分類吞掉。
```

## 導演隱藏與入場鎖

```yaml
DIRECTOR_HIDDEN_BASELINE:
  true_nature: "妖族化人"
  specific_species: "UNKNOWN"
  relation_to_floating_moon_six_facet_theory: "CLASSIFICATION_ANOMALY"
  agrees_with_stage_title: "UNKNOWN"
  challenge_participation: "GM_CONFIRMED_FUTURE_DIRECTION"
  personal_motive_for_challenge: "UNKNOWN_NOT_FIXED"
```

---

### 人物背景／第二生命／野心／黑暗因果

```yaml
CHARACTER_BASE:
  character: "錯位"
  TRUE_OR_SOURCE_HISTORY:
    pre_entry: "UNKNOWN / DEFERRED"
    entry_path: "UNKNOWN / EXCEPTION POSSIBLE"
    professional_causal_history:
      - "成為『錯位』後，她長期被人拿外貌、身形、距離感與聲線互相矛盾之處當成需要解釋的謎題。"
      - "她逐漸學會不替別人的分類失敗善後；有時甚至故意放大矛盾，讓對方為自己的預設付代價。"
  SECOND_LIFE_IDENTITY:
    system: "FLOATING_MOON STAGE IDENTITY"
    stage_name: "錯位"
    agrees_with_name: "UNKNOWN"
    truth_relation: "可作好用花名，但不證明她認同被定義為錯誤。"
  BODY_HISTORY:
    footbinding: "NOT_APPLICABLE / NON-HUMAN SOURCE"
    adult_lock: "ADULT IDENTITY FIXED; youthful facial signals do not alter age status."
  BASE_AMBITION:
    primary: ["讓別人即使看不懂她，也必須承認她不欠一個好懂的版本。", "把分類異數從被觀看的商品變成能反向測試分類者的權力。"]
    secondary: ["找出自己真正偏愛什麼，而不是只知道自己討厭被怎樣分類。"]
    preferred_methods: ["直接拒絕", "故意不解釋", "放大矛盾訊號", "突然改位", "用具體行動代替身份敘事"]
  DARK_CAUSAL_BASE:
    HIDDEN_WOUND: "她最熟悉的問題不是『妳要什麼』，而是『妳到底算哪一種』；久而久之，連真正關心也可能先被她當成分類企圖。"
    HIDDEN_AMBITION: "有人可以不先解開她，就直接跟她生活在同一個房間裡。"
    SHAME_OR_GUILT: "她知道自己有時故意讓人誤判只是因為好玩或報復，並非每次都是自我保護。"
    PRIVATE_DESIRE: "被看見具體偏好、壞習慣與無聊，而不是永遠作為異數被研究。"
    AVERSION_ROUTE: ["被要求證明成年／女性／妖／花魁應有的樣子", "把她當禁忌收藏", "以理解她為名要求她配合分類"]
    TRIGGER_ROUTE: ["六系評分", "他人因外貌訊號做身份推定", "有人說要『修正』她"]
    DIRTY_METHOD_CAPACITY: ["利用互相衝突的外在訊號誘導對方暴露偏見", "故意不給禮貌台階", "在談判中讓對方先為錯誤假設下注", "利用別人想證明自己看懂她的慾望反向設局"]
    SOFT_SPOTS: ["不急著問她是什麼的人", "能接受她很普通的一面的人", "被分類制度弄傷卻仍不拿她當同類象徵的人"]
    SELF_AWARENESS: "MEDIUM / 她知道自己抗拒分類，但不一定知道抗拒已變成身份的一部分。"
  LOCKS: ["ADULT != CHILDLIKE IDENTITY", "AMBIGUITY != CONSENT", "CLASSIFICATION FAILURE != SUPERNATURAL EFFECT", "ENTRY HISTORY REMAINS UNKNOWN"]
```


---