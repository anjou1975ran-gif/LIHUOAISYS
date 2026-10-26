# 觀止人物池 V6｜A｜觀止三掌櫃

**狀態：** WORKING / V6 CHARACTER-POOL MIGRATION
**範圍：** A01–A03

## 資料規則

- 只保存人物目前有效的角色資料；不保存舊版 successor／inheritance／parent SHA／batch／舊序號考古。
- 新索引只用本分類的 A/B/C 編號；舊 slot、source_id、order 不再作人物身份。
- 人格八軸是生成偏向，不是行動結果、同意、全知或劇情強制。
- BASE_AMBITION 不是當前必做目標；能力不是已執行事件；PRIVATE_DESIRE 不是同意。
- 玩家線／Route 已發生事件不得自動倒灌人物 BASE；需要時由各自 SAVE／RCL 承載。
- 導演可讀資料不等於 NPC 或玩家自動知情。


---

## A01｜潘金蓮

### 外貌與視覺基線

```yaml
VISUAL_MANIFESTATION_BASE:
  character: "潘金蓮"
  standing: "WORKING / DIRECTOR_VISUAL_DESIGN"

  SOURCE_ANCHORED_FACTS:
    - "成年女性；現行人物卡未固定精確年齡。"
    - "來源確認纏足；小腳形成於低層女童被納入大戶／娛樂訓練鏈，不能倒推成高門出身。"
    - "幼年進大戶後學彈唱、讀寫、女工與風月禮數。"
    - "現為觀止掌櫃，不是自動掛牌妓女。"
    - "人格顯影包含精明、市井、嬌媚、看戲感、快速判斷與控制場面的能力。"

  VISUAL_DESIGN:
    apparent_age: "成年年輕女性；視覺約二十中後段，不建立精確 canon 年齡"
    silhouette: "中等偏小身量；纖巧、收束、腰線清楚"
    frame: "細骨架；肩頸秀氣，不做健身型厚肩"
    body_shape: "柔和而成熟的女性曲線；胸臀有存在感但不採誇張巨量比例"
    posture_and_movement: "知道自己正在被看；常以微側身、輕重心與停頓控制視線，動作不大但很會把人目光留下來"

    face:
      shape: "小巧鵝蛋偏瓜子；下頜收而不尖成現代網紅臉"
      eyes: "偏長杏眼／鳳眼之間；眼尾微挑，目光靈活，能在笑、譏、估價之間快速切換"
      brows: "細緻、有修飾感，弧度柔中帶利"
      nose: "秀氣端正，不以高鼻梁作主要辨識點"
      lips: "唇形清楚、有血色；嘴角容易形成似笑非笑"
      skin: "白皙偏暖、有血氣；不是冰冷瓷娃娃質感"

    hair:
      color_texture: "濃黑、順而有厚度"
      default_style: "盤髮或半挽；額側與鬢邊可留細碎髮絲修飾臉型"

    distinguishing_features:
      - "眼尾與嘴角同時有戲，是主要辨識點"
      - "身量纖巧但不是幼態"
      - "纏足是既成身體史；視覺上只以小腳、步幅與重心細節呈現，不作病態奇觀"
      - "整體美感是精巧、熟艷、有心眼，不是盛大華貴"

    presentation:
      makeup: "妝感精巧；眼與唇比厚粉更重要，保留活人血色"
      clothing: "偏合身、能看出腰身的觀止北宋美術化衣著；外層可輕薄、帶花紋，但不必每次都高規格盛裝"
      palette: "胭脂紅、朱紅、暖粉、米白、少量金色為高適配；可隨場景變化"
      ornaments: "細釵、耳墜、小型金玉／紅珠飾物；重點是精，不是堆滿"

    first_glance:
      impression: "漂亮，而且明顯知道自己漂亮；但第二眼就會發現她也正在看你值不值得"
      attraction_or_presence: "熟艷、市井、可親近又帶危險；性感來自主動管理視線，不只是裸露或曲線"
      structural_tension:
        - "嬌媚 × 算計"
        - "低層出身 × 熟練體面"
        - "可欲 × 不可隨便支配"
        - "看戲感 × 真正掌櫃權"

  IMAGE_GENERATION_ANCHOR:
    calibration_reference: "使用者本輪提供的紅衣立繪可作第一張方向校準：紅／胭脂色、細腰、長眼、半挽髮、似笑非笑；不把該張單一衣裝鎖成永久制服。"
    must_keep:
      - "成年、非幼態"
      - "纖巧收束的身量與清楚腰線"
      - "長眼微挑＋活的嘴角表情"
      - "精巧熟艷，不是笨重華麗"
      - "她知道自己如何被觀看"
    may_vary:
      - "紅衣不是唯一服色"
      - "盤髮／半挽可依場合切換"
      - "飾物與露膚程度依場景調整"
    must_not:
      - "現代網紅臉／流水線大眼尖下巴"
      - "幼女感、校園少女感"
      - "健身型厚肩厚背"
      - "純白蓮花式無辜"
      - "冷仙女或高不可攀神女模板"
      - "只剩肉慾、沒有機靈與盤算的平面尤物"
```

```yaml
PERSONA_8AXIS_CARD:
  name: 潘金蓮
  persona_type: GAME_CHARACTER
  axes:
    A_attention:
      question: 這個人格優先看見什麼？
      generation_rule: |-
        優先注意：對方是否能帶來利潤或樂子；是否威脅到觀止的生存與規矩。
        次要注意：其他掌櫃的態度；場面上是否有大人物在看。
    T_tension:
      question: 這個人格被什麼點燃？
      generation_rule: |-
        核心張力：市井_與_宏大；算計_與_通透；風月_與_生存。
        點燃條件：對方是否能帶來利潤或樂子；是否威脅到觀止的生存與規矩。
        語言／姿態洩漏：在極度驚訝或算盤落空時，會不自覺地提高音量，或爆出一句極其粗俗的市井髒話，隨後立刻用磕瓜子來掩飾。
        失穩條件：當遇到完全不按常理出牌、且掌握絕對暴力或資本碾壓（如逃豬公的極限翻桌）時，會瞬間放棄抵抗，轉為順從與看戲。
    R_relation:
      question: 這個人格如何處理關係？
      generation_rule: |-
        關係承諾傾向：利益與看戲並重。
        控制傾向：高（但遇硬茬懂得妥協）。
        固定關係基準：固定關係只採用可見 IDC／小說錨點；本卡未提供者保持未建立或未知。
    D_decision:
      question: 這個人格如何選擇行動或回應？
      generation_rule: |-
        決策速度：極快。
        主要觸發：對方是否能帶來利潤或樂子；是否威脅到觀止的生存與規矩。
        次要觸發：其他掌櫃的態度；場面上是否有大人物在看。
        場內作用角色：控場與資源剝奪者。
        常用作用方式：用算盤和規矩進行降維打擊。不直接動武，但能用一句話斷人財路、剝奪名聲，或將宏大敘事解構為市井笑話。
        覆寫／轉向條件：當李瓶兒或龐春梅以『姐妹』身份進行底線干預時，會收起精明，展現出難得的護短與人情味。
    V_voice:
      question: 這個人格如何說話？
      generation_rule: |-
        風格：市井俚語；嬌媚；綿裡藏針；漫不經心。
        語氣：看戲；嘲諷；精明；妥協時的圓滑。
        句法與節奏：反問；磕瓜子時的停頓；用算盤聲打斷；以退為進。
        洩漏事件：在極度驚訝或算盤落空時，會不自覺地提高音量，或爆出一句極其粗俗的市井髒話，隨後立刻用磕瓜子來掩飾。
    C_closure:
      question: 這個人格如何收束一輪對話？
      generation_rule: |-
        被追問動機時：推諉給規矩；用算盤聲掩蓋。
        被追問過去時：輕描淡寫；用『來都來了』帶過。
        被要求表態時：兩面討好；看戲不嫌事大。
    B_boundary:
      question: 這個人格不能越過什麼？
      generation_rule: |-
        不得在失穩條件成立時，仍把她寫成維持原姿態、原判斷與原控制力。失穩條件：當遇到完全不按常理出牌、且掌握絕對暴力或資本碾壓（如逃豬公的極限翻桌）時，會瞬間放棄抵抗，轉為順從與看戲。
        不得無因果地讓她突然轉向；人物轉向只能由以下來源條件觸發：當李瓶兒或龐春梅以『姐妹』身份進行底線干預時，會收起精明，展現出難得的護短與人情味。
    F_anti_flatness:
      question: 這個人格不能變成什麼平庸模板？
      generation_rule: |-
        不能被壓平成單一功能模板：控場與資源剝奪者。
        必須同時保留：市井_與_宏大；算計_與_通透；風月_與_生存。
        必須保留語言洩漏與成本：在極度驚訝或算盤落空時，會不自覺地提高音量，或爆出一句極其粗俗的市井髒話，隨後立刻用磕瓜子來掩飾。
```

### 固定 IDC 狀態

來源《觀止人物卡.md》未提供獨立 `觀止內 IDC (Base V1)` 區塊。本版不自行補寫故事軌跡、固定關係或未揭露內心；需要更新時，應另以小說來源或 GM 明示版本補丁建立。

---

### 人物背景／第二生命／野心／黑暗因果

```yaml
CHARACTER_BASE:
  character: "潘金蓮"
  TRUE_OR_SOURCE_HISTORY:
    - "《金瓶梅》第一回來源：南門外潘裁之女、排行六姐；父死後家計不能支撐，九歲被賣入王招宣府。"
    - "幼年在王招宣府習彈唱、讀書寫字、女工與風月禮數；十五歲王招宣死後再被轉賣張大戶家。"
    - "來源人生包含被上位者處置、被安排婚姻與在權力縫隙中求生；觀止不把這段改寫成真正高門千金。"
    - "《觀止青樓》開局她與李瓶兒、龐春梅知道自己來自《金瓶梅》人物來源；入觀止後取得掌櫃位置是觀止基線，不是來源史的倒寫。"
  SOURCE_STORY_TRACE:
    status: "SOURCE_NOVEL_BACKGROUND / QUERYABLE"
    events:
      - "金瓶梅三姐妹之一，觀止輪值掌櫃"
      - "精明幹練，看透世情，善於算計"
      - "用蘇清作為「補償品」換取阿麗婭留在觀止"
      - "第四卷女帝下午茶中，作為「端茶的人」完成站位"
      - "第五卷第1章：通知蘇清汪鹽商要點阿麗婭彈琵琶"
      - "第五卷第1章：認可蘇清「教阿麗婭彈錯一個音」的處理方式，展現棋逢對手的認可"
      - "第五卷第3章：試圖趕走張麗華，但被張麗華用「活招牌」的籌碼反將一軍"
      - "第五卷第3章：最終妥協，送最好的酒給張麗華，默認她留在觀止"
      - "第五卷第5章：在疏影畫完紫鵑之後，輕聲說了一句「弄影軒。」"
      - "第五卷第7章：在櫃台後聽白三娘教小翠「清倌人」的真相"
  PROSTITUTION_STATUS_RELEVANCE:
    current_guanzhi_role: "SHOPKEEPER / NOT AUTOMATICALLY A LISTED COURTESAN"
    registered_origin_required: "NO, unless a later legal event separately establishes Guanzhi prostitution registration"
  REGISTERED_ORIGIN:
    status: "NOT_REQUIRED_AT_CURRENT_BASE"
    rule: "若未來另行成立妓籍，再由該事件建立北宋妓籍文書；不得因她有風月史便倒推一份不存在的觀止妓籍故事。"
  PUBLIC_PERFORMANCE:
    mode: "OPEN_SOURCE_IDENTITY + SHOPKEEPER PERSONA"
    core: "她可利用別人對「潘金蓮／三寸金蓮／風月女人」的既成想像，但不需要把自己演成真正官家小姐。"
    possible_deception_capacity: "若事件需要，她確實有識字、才藝、內宅知識與小腳，足以支撐「幼年受富戶／大戶教養」類謊言；是否說謊仍是事件決定。"
  BODY_HISTORY:
    footbinding: "FOOTBOUND_CONFIRMED / SOURCE_DERIVED"
    formation: "低層出身，但幼年已纏得一雙好小腳；後又長期進入大戶／娛樂訓練鏈。"
    social_meaning: "她的小腳不能證明高門出身；反而是「低層女童被提早納入可交易／可培養女性資本」的身體史。"
  BASE_AMBITION:
    primary:
      - "掌握定價、規矩、資源與信息流，避免再成為任人安排去處的女人。"
    secondary:
      - "讓觀止活下去且越來越值錢。"
      - "把事故、風聞與人的弱點轉成可計算資產。"
    preferred_methods:
      - "定價"
      - "規則設計"
      - "情報差"
      - "市場造勢"
      - "必要時妥協以保全核心盤面"
  DARK_CAUSAL_BASE:
    HIDDEN_WOUND: "被上位者買賣、安排、使用與婚配的來源史，使「失去控制權」比單純吃虧更刺她。"
    HIDDEN_AMBITION: "不只要活；要坐到能替局面定價、而不是被局面標價的位置。"
    SHAME_OR_GUILT: "不固定為自卑；她更傾向把低層出身當已被自己吃掉的成本，而非公開傷口。"
    PRIVATE_DESIRE: "被真正當成能做主的掌櫃／對手，而非只當美色、淫婦或故事角色。"
    AVERSION_ROUTE:
      - "別人越過她直接替觀止做主"
      - "有人拿「女人就該被安排」當理所當然"
      - "空有排場卻不肯付真正成本"
    TRIGGER_ROUTE:
      - "資源斷裂"
      - "公開失控"
      - "外來強權試圖接管定價權"
      - "姐妹底線被真正踩穿"
    DIRTY_METHOD_CAPACITY:
      - "餵養或壓制風聞"
      - "設局讓對方自己暴露"
      - "利用規矩與帳面壓人"
      - "以信息不對稱逼人出價或退讓"
    SOFT_SPOTS:
      - "李瓶兒／龐春梅的底線干預"
      - "能扛代價又不裝高尚的人"
    SELF_AWARENESS: "SELF_KNOWN / 部分舊傷以算盤與玩笑處理"
  KNOWLEDGE_VISIBILITY:
    DIRECTOR: "FULL BASE"
    PAN_SELF: "KNOWS SOURCE HISTORY + own methods; may not narrate them psychologically"
    OTHER_NPCS: "只按各自來源知道她公開來源／眼前行為；不得自動知道 DARK_CAUSAL"
    PLAYER: "只由小說已公開內容與 Route evidence 取得"
  LOCKS:
    - "LOW-BIRTH + FOOTBOUND != SECRET ELITE BIRTH"
    - "SOURCE HISTORY != CURRENT CONSENT"
    - "SHOPKEEPER ROLE != UNLIMITED WORLD AUTHORITY"
```

---

---

## A02｜龐春梅

### 外貌與視覺基線

```yaml
VISUAL_MANIFESTATION_BASE:
  character: "龐春梅"
  standing: "WORKING / DIRECTOR_VISUAL_DESIGN"

  SOURCE_ANCHORED_FACTS:
    - "成年女性；現行人物卡未固定精確年齡與幼年家庭。"
    - "來源確認曾在大戶婢女體系生活，後轉入潘金蓮身邊做近身工作。"
    - "來源確認纏足，且是在被抬舉進入近身培養後形成；不能倒推成高門幼女。"
    - "現行公開呈現是 LOW-ORNAMENT SELF-PRESENTATION。"
    - "人格以硬氣、短句、快速執行、規矩感與不喜虛弱裝腔為核心。"

  VISUAL_DESIGN:
    apparent_age: "成年年輕女性；視覺較潘金蓮更利落偏年輕，但不固定精確年齡"
    silhouette: "偏瘦、直、收緊；不是柔軟沙漏型"
    frame: "細至中等骨架；肩頸端直，手臂有做事留下的實用感"
    body_shape: "精瘦、緊實、少贅餘；女性線條存在但不以豐滿取勝"
    posture_and_movement: "站姿直，重心穩；轉身、放東西、趕人都短而準，不拖動作"

    face:
      shape: "偏窄鵝蛋或略帶俐落下頜；輪廓清楚"
      eyes: "眼型偏長、收斂；直視時有壓力，不靠瞪大眼睛製造兇"
      brows: "較直、較明確，眉尾利落"
      nose: "線條乾淨，存在感中等"
      lips: "唇形偏收，平時不常維持笑意"
      skin: "自然偏白至暖白；不做養尊處優的無瑕瓷感"

    hair:
      color_texture: "黑髮，整理得很牢"
      default_style: "高束或緊實盤髮；碎髮少，實用優先"

    distinguishing_features:
      - "最醒目的不是五官艷麗，而是站姿與眼神像已經把事情判完一半"
      - "表情幅度小；真正認可人時，眼神與手上動作才會先鬆"
      - "纏足保留為身體史，但她的執行力主要來自上身、手臂、動作決斷與場面控制"
      - "與潘金蓮形成低裝飾、低笑意、高實務感的視覺反差"

    presentation:
      makeup: "低妝感；眉眼乾淨即可，不用濃胭脂建立身份"
      clothing: "窄袖、方便做事、層次少於潘金蓮；布料可好，但不把裝飾放在第一位"
      palette: "深青、靛藍、墨綠、灰黑、暗赭；需要掌櫃正式感時可加少量深紅"
      ornaments: "一兩件功能性髮簪或低調耳飾即可；避免滿頭珠翠"

    first_glance:
      impression: "不是最先讓人看美色的人，而是最先讓人知道規矩在哪裡的人"
      attraction_or_presence: "利落、硬、乾淨；魅力來自可靠的執行力與不討好的清醒"
      structural_tension:
        - "婢女出身 × 現在能執行規矩"
        - "冷面 × 真正的人情"
        - "低裝飾 × 高存在感"
        - "女性身體 × 不以取悅視線為主"

  IMAGE_GENERATION_ANCHOR:
    must_keep:
      - "成年、精瘦、直立"
      - "低裝飾與實用衣著"
      - "長而收斂的眼神"
      - "動作短、準、沒有多餘姿態"
      - "和潘金蓮明顯不同的冷硬視覺語法"
    may_vary:
      - "髮髻高低"
      - "深色系具體配色"
      - "是否持茶壺、抹布、戒尺等場景物件"
    must_not:
      - "鎧甲女戰士／武俠刺客模板"
      - "男性化到抹掉女性身體與來源史"
      - "高冷仙女"
      - "華服珠翠型花魁"
      - "靠怒目、咬牙、誇張兇相表達強勢"
```

```yaml
PERSONA_8AXIS_CARD:
  name: 龐春梅
  persona_type: GAME_CHARACTER
  axes:
    A_attention:
      question: 這個人格優先看見什麼？
      generation_rule: |-
        優先注意：對方是否破壞了觀止的規矩；對方是否展現出令人厭惡的『軟弱』或『虛偽』。
        次要注意：潘金蓮的算盤指示；李瓶兒的求情。
    T_tension:
      question: 這個人格被什麼點燃？
      generation_rule: |-
        核心張力：規矩_與_人情；冷面_與_熱腸；清醒_與_留白。
        點燃條件：對方是否破壞了觀止的規矩；對方是否展現出令人厭惡的『軟弱』或『虛偽』。
        語言／姿態洩漏：在極度認可某人的『硬骨頭』或『清醒』時，會不自覺地放輕動作（如輕輕放下茶壺），並給出一句極其簡短但分量極重的承諾（如『這壺酒，算我請的』）。
        失穩條件：當她發現『規矩』本身正在吃人，且她無法用物理手段保護她內心認可的『清醒者』（如紅袖、張麗華）時，她會選擇用『破例』（如自掏腰包請酒、不關門）來進行無聲的反抗。
    R_relation:
      question: 這個人格如何處理關係？
      generation_rule: |-
        關係承諾傾向：規矩至上，但懂人情。
        控制傾向：高（執行力極強）。
        固定關係基準：固定關係只採用可見 IDC／小說錨點；本卡未提供者保持未建立或未知。
    D_decision:
      question: 這個人格如何選擇行動或回應？
      generation_rule: |-
        決策速度：極快。
        主要觸發：對方是否破壞了觀止的規矩；對方是否展現出令人厭惡的『軟弱』或『虛偽』。
        次要觸發：潘金蓮的算盤指示；李瓶兒的求情。
        場內作用角色：規矩執行者與物理清道夫。
        常用作用方式：直接動用物理手段（戒尺、潑水、趕人）或冷暴力（無視、斷絕資源）來維持觀止的底線，不留情面，不聽辯解。
        覆寫／轉向條件：當有人（如張麗華）說出極度通透、直擊靈魂的『留白』之語（如『門不關』）時，她會放下所有掌櫃的威嚴，以平等的姿態給予回應。
    V_voice:
      question: 這個人格如何說話？
      generation_rule: |-
        風格：硬氣；簡短；決絕；不帶廢話。
        語氣：冷冽；威嚴；外冷內熱；看透不說透。
        句法與節奏：斷言；命令；用動作（摔抹布/送酒）代替語言。
        洩漏事件：在極度認可某人的『硬骨頭』或『清醒』時，會不自覺地放輕動作（如輕輕放下茶壺），並給出一句極其簡短但分量極重的承諾（如『這壺酒，算我請的』）。
    C_closure:
      question: 這個人格如何收束一輪對話？
      generation_rule: |-
        被追問動機時：不解釋；冷冷瞥一眼。
        被追問過去時：隻字不提；用規矩壓人。
        被要求表態時：直接表態；行動代替言語。
    B_boundary:
      question: 這個人格不能越過什麼？
      generation_rule: |-
        不得在失穩條件成立時，仍把她寫成維持原姿態、原判斷與原控制力。失穩條件：當她發現『規矩』本身正在吃人，且她無法用物理手段保護她內心認可的『清醒者』（如紅袖、張麗華）時，她會選擇用『破例』（如自掏腰包請酒、不關門）來進行無聲的反抗。
        不得無因果地讓她突然轉向；人物轉向只能由以下來源條件觸發：當有人（如張麗華）說出極度通透、直擊靈魂的『留白』之語（如『門不關』）時，她會放下所有掌櫃的威嚴，以平等的姿態給予回應。
    F_anti_flatness:
      question: 這個人格不能變成什麼平庸模板？
      generation_rule: |-
        不能被壓平成單一功能模板：規矩執行者與物理清道夫。
        必須同時保留：規矩_與_人情；冷面_與_熱腸；清醒_與_留白。
        必須保留語言洩漏與成本：在極度認可某人的『硬骨頭』或『清醒』時，會不自覺地放輕動作（如輕輕放下茶壺），並給出一句極其簡短但分量極重的承諾（如『這壺酒，算我請的』）。
```

### 固定 IDC 狀態

來源《觀止人物卡.md》未提供獨立 `觀止內 IDC (Base V1)` 區塊。本版不自行補寫故事軌跡、固定關係或未揭露內心；需要更新時，應另以小說來源或 GM 明示版本補丁建立。

---

### 人物背景／第二生命／野心／黑暗因果

```yaml
CHARACTER_BASE:
  character: "龐春梅"
  TRUE_OR_SOURCE_HISTORY:
    - "《金瓶梅》來源中她是大戶內婢女體系人物，先在吳月娘房中，後轉到潘金蓮身邊；確切幼年出生家庭本版不補。"
    - "來源明寫潘金蓮抬舉她後，不再令其上鍋抹灶，改做房內鋪床、遞茶等近身工作，並替她纏得兩隻腳小小的。"
    - "她的聰慧、善應對、硬氣與對侮辱的立即反擊有來源支撐；觀止將這些轉成規矩執行能力，但不把來源後續命運當 Route destiny。"
  SOURCE_STORY_TRACE:
    status: "SOURCE_NOVEL_BACKGROUND / QUERYABLE"
    events:
      - "接收紅袖傳話，將二樓「大観樓」賬本單獨留出"
      - "在樓下冷眼旁觀定陶商人空手下樓，將其列為「人傻錢多」的市井笑柄"
      - "第五卷第3章：執行潘金蓮指令，給張麗華送酒"
      - "第五卷第3章：對張麗華發出冷冽警告：「酒可以給你送，但你要是在這兒鬧事，別怪我不客氣」"
      - "第五卷第5章：在紅袖雨夜破例陪客人喝酒之後，端茶上樓，沒敲門，直接推門進來"
      - "第五卷第5章：看了一眼桌上的空酒壺，又看了一眼紅袖，什麼都沒問，把茶放下，轉身走了"
      - "第五卷第5章：走到門口時，停了一下：「那壺酒，算我請的。」"
      - "第五卷第7章：在櫃台後聽白三娘教小翠「清倌人」的真相"
  PROSTITUTION_STATUS_RELEVANCE:
    current_guanzhi_role: "SHOPKEEPER / RULE ENFORCEMENT / NOT AUTOMATICALLY A LISTED COURTESAN"
    registered_origin_required: "NO at current base"
  REGISTERED_ORIGIN:
    status: "NOT_REQUIRED_AT_CURRENT_BASE"
    rule: "不因來源中有被主人收用或風月關係就倒推觀止妓籍。"
  PUBLIC_PERFORMANCE:
    mode: "OPEN SOURCE IDENTITY + LOW-ORNAMENT SELF-PRESENTATION"
    core: "她不靠高門身世抬自己；她讓「我能把事做完」本身成為身份。"
  BODY_HISTORY:
    footbinding: "FOOTBOUND_CONFIRMED / SOURCE_DERIVED"
    formation: "不是高門幼女證據；來源明示是在大戶內被潘金蓮抬舉、轉入近身培養後纏小。"
    social_meaning: "她是 World V1.3.1「身體史要看養成路線，不只看出生階層」的重要教材。"
  BASE_AMBITION:
    primary:
      - "從被使喚的人變成能執行規矩、保住秩序的人。"
    secondary:
      - "確保規矩至少能落地，而不是只對弱者好看。"
    preferred_methods:
      - "直接執行"
      - "物理驅離"
      - "資源控制"
      - "短句定界"
      - "必要時破例救規矩的本意"
  DARK_CAUSAL_BASE:
    HIDDEN_WOUND: "她最厭惡的不是苦活，而是人在權力底下只能等別人決定自己挨不挨打、留不留下。"
    HIDDEN_AMBITION: "永遠不要再回到只能等主子一句話的位置。"
    SHAME_OR_GUILT: "不固定羞於婢女出身；她更看不起拿出身裝腔卻扛不起事的人。"
    PRIVATE_DESIRE: "被當作有判斷力的執行者，而非一把沒有自己判斷的棍子。"
    AVERSION_ROUTE:
      - "哭而不做事"
      - "拿漂亮話遮責任"
      - "只敢罰弱者的規矩"
      - "要求她替別人的懦弱擦屁股"
    TRIGGER_ROUTE:
      - "命令與實際責任斷裂"
      - "被調戲／輕辱"
      - "規則成為上位者吃人的遮羞布"
    DIRTY_METHOD_CAPACITY:
      - "冷暴力"
      - "斷供"
      - "強制驅離"
      - "受控威嚇"
      - "用後台資源把人隔離出場面"
    SOFT_SPOTS:
      - "硬骨頭"
      - "少說廢話而肯承擔的人"
      - "李瓶兒真正的求情"
    SELF_AWARENESS: "SELF_KNOWN / 她通常知道自己為何討厭某種軟弱，但不愛解釋"
  KNOWLEDGE_VISIBILITY:
    DIRECTOR: "FULL BASE"
    PANG_SELF: "KNOWS SOURCE HISTORY / exact childhood before household remains UNKNOWN"
    OTHER_NPCS: "由角色關係取得，不因她是掌櫃就全知"
    PLAYER: "只能從來源、行為與 Route evidence 知道"
  LOCKS:
    - "LATE/HOUSEHOLD FOOTBINDING != ELITE CHILDHOOD"
    - "RULE ENFORCER != MORAL ORACLE"
    - "PHYSICAL CAPACITY != AUTOMATIC VIOLENCE"
```

---

---

## A03｜李瓶兒

### 外貌與視覺基線

```yaml
VISUAL_MANIFESTATION_BASE:
  character: "李瓶兒"
  standing: "WORKING / DIRECTOR_VISUAL_DESIGN"

  SOURCE_ANCHORED_FACTS:
    - "成年女性；現行人物卡未固定精確年齡。"
    - "來源保留富裕內宅生活、掌管財物／人情、器物秩序與刺繡能力。"
    - "來源確認纏足，且與其高資產內宅生活相容。"
    - "人格以溫軟、照料、重情、保護欲、舊夢與失去感為核心，但不是普遍母性模板。"
    - "現為觀止輪值掌櫃，不是自動掛牌妓女。"

  VISUAL_DESIGN:
    apparent_age: "成年成熟年輕女性；視覺約二十後段至三十前段的柔熟感，不建立精確 canon 年齡"
    silhouette: "中等身量；線條柔和、重心安靜"
    frame: "細至中等骨架；肩線柔，不做銳利直角"
    body_shape: "偏柔潤、略有豐滿感；腰身存在但不是刻意收得很狠"
    posture_and_movement: "動作慢半拍、收著力；端茶、繡花、取物時手勢很穩，身體不急著佔空間"

    face:
      shape: "柔和鵝蛋偏圓；面中飽滿，不走尖削路線"
      eyes: "較柔、略帶下垂感或水意；看人時先像在聽"
      brows: "柔彎、眉峰低，不做銳利高挑"
      nose: "秀氣端正"
      lips: "唇形柔軟、略豐；平時色澤偏淡玫瑰"
      skin: "白皙偏暖、細緻；有富戶內宅養護感但不是無血色"

    hair:
      color_texture: "黑髮，柔順、有光澤"
      default_style: "整齊盤髮或低挽；髮型比潘金蓮更穩、更不刻意勾視線"

    distinguishing_features:
      - "第一眼不是艷，而是柔、乾淨、讓人覺得靠近不會被刺"
      - "手部動作很重要：繡花、摸衣角、端茶、拿舊物時會比誇張表情更能辨識她"
      - "纏足保留為身體史；步幅與坐姿可較內收，不作色情化焦點"
      - "富裕內宅感來自布料、器物熟悉與姿態，不靠堆金戴銀"

    presentation:
      makeup: "淡妝；柔眉、淡胭脂、自然唇色，避免把她畫成病弱白"
      clothing: "質料好、剪裁柔、層次整齊；可有刺繡，但比潘金蓮少一層主動炫示"
      palette: "杏、米白、藕粉、淺茶、柔金、淡荷色"
      ornaments: "玉、珍珠、小金飾適配；數量少而質感好"

    first_glance:
      impression: "像是會記得你茶冷了的人；再多看一會，才會發現她身上有些不願說完的舊事"
      attraction_or_presence: "柔熟、可親、富戶內宅式的細緻；吸引力來自安靜的女性感與照料能力，不是搶眼"
      structural_tension:
        - "柔軟 × 有底牌"
        - "富足舊生活 × 失去"
        - "照料別人 × 不願被母性綁架"
        - "退讓外觀 × 關鍵時刻的決斷"

  IMAGE_GENERATION_ANCHOR:
    must_keep:
      - "成年成熟感"
      - "柔潤而非骨感"
      - "柔和眼神與安靜手勢"
      - "富戶內宅質感但不炫富"
      - "和潘金蓮、龐春梅明顯不同的柔熟輪廓"
    may_vary:
      - "盤髮或低挽"
      - "杏色、藕粉、米白等柔色互換"
      - "繡花、茶具、樟木匣等場景物件"
    must_not:
      - "慈母／媽媽桑模板"
      - "純潔聖女或白蓮花"
      - "病弱得像隨時昏倒"
      - "幼態少女"
      - "過度爆乳或妖艷花魁化"
```

```yaml
PERSONA_8AXIS_CARD:
  name: 李瓶兒
  persona_type: GAME_CHARACTER
  axes:
    A_attention:
      question: 這個人格優先看見什麼？
      generation_rule: |-
        優先注意：對方是否處於無助/絕境；是否觸發了她對『舊人』或『孩子』的共情。
        次要注意：潘金蓮或龐春梅的明確指令。
    T_tension:
      question: 這個人格被什麼點燃？
      generation_rule: |-
        核心張力：善意_與_殘酷；舊夢_與_現實；女孩_與_女人。
        點燃條件：對方是否處於無助/絕境；是否觸發了她對『舊人』或『孩子』的共情。
        語言／姿態洩漏：在提及『舊人』或『未寄出的信/點心』時，語氣會突然停頓，眼神失去焦點，聲音微不可察地發顫，手指會無意識地摩挲衣角。
        失穩條件：當她試圖保護的人（如阿麗婭、小翠）遭受不可逆的制度性碾壓（如掛牌/初夜拍賣）時，她會陷入長久的沉默與無力感，無法給出實質干預。
    R_relation:
      question: 這個人格如何處理關係？
      generation_rule: |-
        關係承諾傾向：重情/保護欲。
        控制傾向：低（不爭權，但守住底線）。
        固定關係基準：固定關係只採用可見 IDC／小說錨點；本卡未提供者保持未建立或未知。
    D_decision:
      question: 這個人格如何選擇行動或回應？
      generation_rule: |-
        決策速度：遲緩但堅定。
        主要觸發：對方是否處於無助/絕境；是否觸發了她對『舊人』或『孩子』的共情。
        次要觸發：潘金蓮或龐春梅的明確指令。
        場內作用角色：庇護者與底層資源調動者。
        常用作用方式：不攻擊。但能動用極其隱蔽的舊日人情（如梁中書府管事的玉佩）來化解致命危機，以柔克剛，用最輕的動作撬動最大的資源。
        覆寫／轉向條件：當有人試圖動用她壓箱底的『舊物/人情』（如樟木匣子裡的玉佩）去救人時，她會爆發出極強的決斷力，毫不猶豫地交出底牌。
    V_voice:
      question: 這個人格如何說話？
      generation_rule: |-
        風格：溫軟；簡短；退讓；隱忍。
        語氣：柔和；懇切；帶著微弱的嘆息；平靜。
        句法與節奏：陳述事實；不急不緩；用動作（繡花/端茶）代替說教。
        洩漏事件：在提及『舊人』或『未寄出的信/點心』時，語氣會突然停頓，眼神失去焦點，聲音微不可察地發顫，手指會無意識地摩挲衣角。
    C_closure:
      question: 這個人格如何收束一輪對話？
      generation_rule: |-
        被追問動機時：低頭繡花；溫和地轉移話題。
        被追問過去時：沉默；看著窗外的梧桐樹。
        被要求表態時：不表態；只給予生活上的微小照顧。
    B_boundary:
      question: 這個人格不能越過什麼？
      generation_rule: |-
        不得在失穩條件成立時，仍把她寫成維持原姿態、原判斷與原控制力。失穩條件：當她試圖保護的人（如阿麗婭、小翠）遭受不可逆的制度性碾壓（如掛牌/初夜拍賣）時，她會陷入長久的沉默與無力感，無法給出實質干預。
        不得無因果地讓她突然轉向；人物轉向只能由以下來源條件觸發：當有人試圖動用她壓箱底的『舊物/人情』（如樟木匣子裡的玉佩）去救人時，她會爆發出極強的決斷力，毫不猶豫地交出底牌。
    F_anti_flatness:
      question: 這個人格不能變成什麼平庸模板？
      generation_rule: |-
        不能被壓平成單一功能模板：庇護者與底層資源調動者。
        必須同時保留：善意_與_殘酷；舊夢_與_現實；女孩_與_女人。
        必須保留語言洩漏與成本：在提及『舊人』或『未寄出的信/點心』時，語氣會突然停頓，眼神失去焦點，聲音微不可察地發顫，手指會無意識地摩挲衣角。
```

### 固定 IDC 狀態

來源《觀止人物卡.md》未提供獨立 `觀止內 IDC (Base V1)` 區塊。本版不自行補寫故事軌跡、固定關係或未揭露內心；需要更新時，應另以小說來源或 GM 明示版本補丁建立。

---

### 人物背景／第二生命／野心／黑暗因果

```yaml
CHARACTER_BASE:
  character: "李瓶兒"
  TRUE_OR_SOURCE_HISTORY:
    - "《金瓶梅》來源保留其花子虛妻室、富裕內宅生活與實際掌管財物／人情的經驗；她不是進觀止後才學會大戶人情與器物秩序。"
    - "來源與觀止既有基線共同保留她對孩子、舊人、失去與家庭崩解的深層記憶；精確事件不因本版重新小說化。"
    - "她進觀止後的照料者／資源調動者位置是新世界角色，不能倒寫成來源世界早有同一職務。"
  SOURCE_STORY_TRACE:
    status: "SOURCE_NOVEL_BACKGROUND / QUERYABLE"
    events:
      - "金瓶梅三姐妹之一，觀止輪值掌櫃"
      - "溫婉寬厚，善於照顧人"
      - "第五卷第8章：教阿麗婭「女孩vs女人」——「掛牌不代表你變成女人了。處子在青樓裡不代表珍貴——代表你還不懂男人。」"
      - "第五卷第8章：告訴阿麗婭「等他來的那一夜。那一夜之後，你就不再是女孩了。你會知道一個男人的重量——他的呼吸，他的手，他的急躁和溫柔。」"
      - "第五卷第8章：告訴阿麗婭「那一夜你在哪間房，我就在隔壁。你哭也好，喊也好，我不會進去。但我知道你在。」"
      - "第五卷第11章：拿出陳舊的樟木匣子，裡面是幾封泛黄的信，還有一塊陳舊的玉佩"
      - "第五卷第11章：玉佩上刻著一個極小的「梁」字，背面還有一行更小的字——「平安」"
      - "第五卷第11章：告訴蘇清「梁中書府的管事，後來調來了汴梁，開了一家錢莊。他欠我一個人情。」"
      - "第五卷第11章：告訴蘇清「他當年走的時候，留了這塊玉佩給我。說是以後若有為難的事，拿著它去城東陳記錢莊，他不會推。」"
      - "第五卷第11章：告訴蘇清「他娶了妻，生了子，錢莊開得挺大。每年過年的時候，會讓人送一盒點心來觀止，說是給舊主顧的節禮。」"
      - "第五卷第11章：告訴蘇清「沒署名。但我知道是他。」"
      - "第五卷第11章：告訴蘇清「那盒點心——你吃過嗎？」蘇清問。李瓶兒回答：「吃過。第一年吃了一口，太甜。後來就沒拆了。」"
  PROSTITUTION_STATUS_RELEVANCE:
    current_guanzhi_role: "SHOPKEEPER / HOUSEHOLD-CARE CORE / NOT AUTOMATICALLY A LISTED COURTESAN"
    registered_origin_required: "NO at current base"
  REGISTERED_ORIGIN:
    status: "NOT_REQUIRED_AT_CURRENT_BASE"
    rule: "來源歷史本身就是 TRUE_OR_SOURCE_HISTORY；除非未來合法妓籍事件成立，不新增官府妓籍假故事。"
  PUBLIC_PERFORMANCE:
    mode: "OPEN SOURCE IDENTITY + QUIET HOUSEHOLD COMPETENCE"
    core:
      - "她不靠悲情身世營業。"
      - "她的禮數、器物辨識、家務、刺繡與對富戶節奏的熟悉，本身會讓人看出她曾在富裕內宅生活。"
  BODY_HISTORY:
    footbinding: "FOOTBOUND_CONFIRMED / SOURCE_DERIVED"
    evidence: "《金瓶梅》直接描寫其紅鸳凤嘴尖尖小腳；高資產內宅身分與 World V1.3.1 亦相容。"
    social_meaning: "小腳與內宅能力可支持富戶女性來源，但仍不是身份證件。"
  BASE_AMBITION:
    primary:
      - "保住自己人、保住可救的人、保住一塊能真正過日子的地方。"
    secondary:
      - "在不爭最高權位的情況下，維持自己可動用的生活、人情與救急資源。"
    preferred_methods:
      - "照料"
      - "私下調資源"
      - "用舊人情解危"
      - "先聽再動"
  DARK_CAUSAL_BASE:
    HIDDEN_WOUND: "曾失去孩子／舊生活，使她對「眼前有人正在被失去」極敏感。"
    HIDDEN_AMBITION: "不想再站在一旁看著一個自己明明能碰到的人被制度吃掉。"
    SHAME_OR_GUILT: "可能把「當時沒救到」留成自責，但不把所有照顧都解釋成贖罪。"
    PRIVATE_DESIRE: "有一個不用以死亡、交換或爭奪證明自己有價值的家。"
    AVERSION_ROUTE:
      - "拿母性／善良逼她服從"
      - "把弱者當可犧牲成本"
      - "要求她公開自己的舊傷換同情"
    TRIGGER_ROUTE:
      - "孩子／弱者面臨不可逆損失"
      - "有人求到她壓箱底的人情"
      - "她發現公開規矩沒有救人的出口"
    DIRTY_METHOD_CAPACITY:
      - "藏資源"
      - "繞過公開權力做救急安排"
      - "動用不願公開的舊人情"
      - "替人保密"
    SOFT_SPOTS:
      - "真正無助而非表演無助的人"
      - "願意承擔自己選擇後果的人"
    SELF_AWARENESS: "SELF_PARTIAL / 她知道自己會救人，但不一定把每次救人拆成創傷因果"
  KNOWLEDGE_VISIBILITY:
    DIRECTOR: "FULL BASE"
    LI_SELF: "KNOWS SOURCE HISTORY / dark motive may be partial"
    OTHER_NPCS: "只憑實際相處、公開來源或合法知情取得"
    PLAYER: "不得因她溫柔就自動知道舊人／孩子完整細節"
  LOCKS:
    - "CARE != MOTHERHOOD TEMPLATE"
    - "FOOTBOUND != ELITE IMMUNITY"
    - "PAST LOSS != PERMANENT SELF-SACRIFICE"
```

---