# 成人親密敘事｜纏足女性歷史身體條件與親密顯影 PATCH V0.1-EXP
## FOOTBINDING EMBODIED AESTHETICS / GAIT / DISPLAY / INTIMACY PATCH
### 《金瓶梅》×《品花寶鑒》×《海上花列傳》×《九尾龜》×《三寸金蓮》來源分層抽取版

```yaml
DOCUMENT:
  title_zh: "成人親密敘事｜纏足女性歷史身體條件與親密顯影 PATCH"
  title_en: "FOOTBINDING EMBODIED AESTHETICS / GAIT / DISPLAY / INTIMACY PATCH"
  short_id: "AINT-FOOTBINDING-PATCH"
  version: "V0.1-EXP"
  date: "2026-08-25"
  document_type: "GENERIC_HISTORICAL_BODY_CONDITION_AND_INTIMACY_RENDERING_PATCH"
  status: "FORMAL_PATCH_CANDIDATE / NOT_RUNTIME / NOT_DEPLOYED / FUTURE_XINFA_DONOR"
  language: "zh-TW"

POSITION:
  world_fact_authority: false
  character_decision_authority: false
  relation_authority: false
  knowledge_authority: false
  consent_authority: false
  adult_qualification_authority: false
  save_authority: false
  rendering_support: true
  body_condition_modeling_support: true
  historical_aesthetic_modeling_support: true
  future_absorption_target: "GENERIC ADULT INTIMACY XINFA / HISTORICAL BODY-CONDITION SUBLAYER"

PATCH_INTENT:
  - "把纏足從『一句三寸金蓮』提升為會改變服飾、審美、儀態、步態、平衡、支撐與親密動作路徑的歷史身體條件。"
  - "把時代人物已經理解的情色符碼還給人物，不以現代田野觀察者口吻反覆科普。"
  - "讓成人場景在纏足條件成立時，維持身體因果與動作連續性，而不是只增加戀足詞彙。"
  - "保存時代審美與真實身體限制的並存，不以任何一邊抹除另一邊。"
```

---

# 0｜PATCH 法位與使用聲明

本檔是**通用候選 PATCH**。

它不是：

- 中國女性史總論；
- 纏足起源定論；
- 北宋以後全體中國女性的人口學規則；
- 人體醫學手冊；
- 成人事件資格證明；
- 同意判定器；
- 人物性癖生成器；
- 《九尾龜》世界事實自動寫入器；
- 新的成人 Runtime。

它只處理一個問題：

> **當某一歷史人物已由合法世界來源確立為纏足女性時，生成系統應如何理解她的身體條件、時代審美、服飾展示、步態與支撐，以及這些條件在已合法成立的成人親密事件中如何改變可行的身體路徑。**

最短式：

> **纏足不是腳部裝飾，而是會同時改寫身段審美、服飾展示、步態平衡與親密動作路徑的歷史身體條件。**

---

# 1｜時代範圍：北宋以後是 eligibility frame，不是 universal fact

玩家提出的研究方向是「北宋以後中國女性的纏足」。本 PATCH 接受其作為**廣義歷史時段入口**，但不把它誤寫成：

```text
北宋以後
=
所有中國女性都纏足
```

本輪 donor 主要是：

- 明代／明代背景情色小說《金瓶梅》；
- 清代《品花寶鑒》；
- 晚清上海《海上花列傳》；
- 晚清蘇滬津《九尾龜》；
- 現代歷史文化小說馮驥才《三寸金蓮》。

因此，本 PATCH **沒有資格只靠這五本書裁決北宋起源、普及速度、地域分布、族群分布或各階層實際比例**。

正式鎖：

```yaml
TEMPORAL_SCOPE_LOCK:
  broad_frame: "POST-NORTHERN-SONG CHINESE HISTORICAL SETTINGS"
  origin_claim: "OUT_OF_SCOPE / NOT_ESTABLISHED_BY_THIS_DONOR_SET"
  universal_population_claim: false
  activation_requires_character_or_world_evidence: true

REGION_CLASS_VARIATION_LOCK:
  rule:
    - "不得從時代標籤直接推定某位女性纏足。"
    - "不得從漢語文化背景直接推定纏足。"
    - "地域、家庭、階層、職業、族群與個人身體史若未有來源，保持 UNKNOWN。"
    - "『晚清女性』不等於『必然三寸金蓮』。"
```

---

# 2｜來源分層與 donor 法

## 2.1 PRIMARY / NEAR-PERIOD LITERARY EVIDENCE

### A｜《九尾龜》

用途：

- 晚清蘇滬津風月世界；
- 金蓮／弓鞋如何被人物觀看；
- 女性如何用鞋尖、金蓮、裙褲與步態傳遞場面訊號；
- 高底鞋、三寸金蓮與疲勞／平衡的日常後果；
- 對小腳的時代內部審美與反思。

若本 PATCH 未來接入《九尾龜》，《九尾龜》原著仍是該世界最高文本來源。

### B｜《海上花列傳》

用途：

- 晚清上海堂子中的自然身體生活；
- 小腳聲音、步態、高底鞋、趔趄與平衡；
- 倌人仍能快速移動、撲身、掙脫，反證「小腳＝完全失能」；
- 纏足作為堂子女性成長／職業身體史的一部分；
- 纏足傷害在同時代文本中的可見性。

不得把《海上花》人物事件直接匯入《九尾龜》人物線。

### C｜《品花寶鑒》

用途：

- 清代人物如何讀懂「蓮瓣」展示；
- 三寸／四寸、鞋履、裙下露足的審美語法；
- 脫鞋、鞋尖、金蓮在社交遊戲中的私密／情色意味；
- 極小纏足對長距離步行的限制。

## 2.2 EARLIER EROTIC GRAMMAR DONOR

### D｜《金瓶梅》

用途：

- 小腳、弓鞋／繡鞋如何嵌入完整女性身體審美；
- 鞋與腳如何進入調情、私密過渡、性愛場景；
- 「大小不是唯一判準，鞋樣周正亦重要」的來源反例；
- 性愛中鞋可以仍穿著、稍後才脫，說明 `MORE NAKED != MORE EROTIC`。

不得：

- 把《金瓶梅》床話直接移植成所有晚清人物聲音；
- 把其情色偏好升格為所有男人／女人的普遍性癖；
- 用早期 donor 覆寫晚清近時代來源。

## 2.3 MODERN RECONSTRUCTIVE / INTERPRETIVE DONOR

### E｜馮驥才《三寸金蓮》

用途：

- 協助現代生成器拆解已失去直覺的「金蓮審美」：形、態、鞋、裙、藏露、表演；
- 提供「有露有藏」的展示控制模型；
- 提醒鞋履、配色、鞋底、鞋口、弓度會共同影響觀感；
- 同時呈現疼痛、改纏、步態不穩與審美競賽。

其小說內「七字法」「六字形法」「四忌」屬**現代小說中的歷史文化重構**，只能作 interpretive donor，不得寫成跨朝代、跨地域的史實法則。

```yaml
SOURCE_AUTHORITY_ORDER:
  when_jwg_host:
    - "九尾龜 PRIMARY"
    - "海上花列傳 NEAR-PERIOD SHANGHAI DONOR"
    - "品花寶鑒 QING NEAR-ERA DONOR"
    - "金瓶梅 EARLIER EROTIC-GRAMMAR DONOR"
    - "三寸金蓮 MODERN RECONSTRUCTIVE DONOR"

  generic_historical_use:
    rule: "依目標年代／地域重新排序；不得固定把任一本小說當全中國通則。"
```

---

# 3｜核心模型：不是 FOOT FETISH，而是 EMBODIED SYSTEM

本 PATCH 將纏足建模為：

```text
FOOTBINDING_BODY_CONDITION
+
AESTHETIC_CODE
+
DRESS_SHOE_SYSTEM
+
GAIT_BALANCE_SYSTEM
+
DISPLAY_CONTROL
+
INTIMACY_GRAMMAR
```

而不是：

```text
FOOTBINDING
=
三寸金蓮
=
男人戀足
```

一句話：

> **形是腳與鞋；態是身體如何帶著它生活；情色則是人物如何在既有文化裡讀懂、展示與靠近。**

---

# 4｜AESTHETIC CODE｜女性纏足審美不是只有「小」

## 4.1 尺寸是訊號，但不是唯一值

來源反覆出現「三寸」作強烈審美符碼，但同一來源系統也明確容許四寸仍被形容為伶俏、動人。

因此：

```text
SMALLER
!=
AUTOMATICALLY MORE BEAUTIFUL
```

《金瓶梅》第二十三回甚至直接讓人物說出：

> 「倒也不在乎大小，只是鞋樣子周正才好。」

這是本 PATCH 的核心反例。

生成時至少分開：

```yaml
FOOT_AESTHETIC_READING:
  apparent_size:
  proportionality:
  pointedness:
  curvature_or_upturn:
  heel_alignment:
  shoe_shape:
  shoe_fit:
  sole_geometry:
  embroidery_material:
  hem_relation:
  gait_relation:
```

其中只有來源有資格的欄位才填，不得自動全部補齊。

## 4.2 「尖、翹、弓、纖」是形態語彙，不是醫學數據

《金瓶梅》《品花寶鑒》《九尾龜》反覆以「尖翹」「蓮瓣」「弓鞋」「一搦凌波」等語彙建立視覺審美。

這些詞描述的是**時代觀看方式**，不是可直接換算為骨骼角度的醫學資料。

正式鎖：

```text
LITERARY SHAPE METAPHOR
!=
BIOMECHANICAL MEASUREMENT
```

## 4.3 鞋是審美本體的一部分

這一輪來源非常一致：

- 腳的觀感常與鞋樣同時出現；
- 鞋底高低會改變步態與視覺；
- 繡工、鞋口、鞋尖、材質都參與人物評價；
- 一雙腳在不同鞋樣下可以呈現完全不同效果。

因此：

> **不要把「金蓮」只理解成裸足。晚明、清代情色與女性身段觀看中，鞋往往是身體的一部分。**

## 4.4 整體身段鏈

纏足審美通常不是孤立器官觀看，而能與下列部分形成連續鏈：

```text
面貌
→ 髮飾
→ 衣料／襖裙
→ 腰身
→ 褲口／裙腳
→ 弓鞋／金蓮
→ 步態
→ 回身／坐姿／站姿
```

《九尾龜》常把弓鞋、腰身、步態、眼風放在同一段人物顯影；《品花寶鑒》亦把弓鞋與細腰並列。

所以成人或風月生成不得突然把人物從完整女人縮成「一雙腳」。

---

# 5｜DISPLAY CONTROL｜藏、露、閃、收

## 5.1 女性可以主動控制小腳如何被看見

《品花寶鑒》第九回最直接：少婦在車內主動伸出三寸蓮鉤，旁觀者立刻把它讀成「顯蓮瓣」。

《九尾龜》第十八回王雙林把褲管提高、露出金蓮；鞋尖又有意無意碰到章秋谷腳上。第三十回陸畹香察覺視線落到腳下後，立即把腳擱到膝上重新約束。

這證明至少在這些文本裡：

```text
WOMAN
CAN
CONTROL_FOOT_DISPLAY
```

但：

```text
DISPLAY
!=
CONSENT_TO_TOUCH
!=
CONSENT_TO_SEX
```

## 5.2 「全露」不是自動比「半露」更情色

馮驥才《三寸金蓮》第五回用賽腳場面高度放大了這件事：

- 腳尖在裙下忽露忽藏；
- 只故意閃出一腳；
- 「有露沒藏」反而被寫成失去效果。

這一部分是**現代重構 donor**，不能冒充清代通行規條，但可以抽象出非常有用的生成原則：

```text
EROTIC_DISPLAY
=
CONTROLLED VISIBILITY
```

而不是：

```text
EROTIC_INTENSITY
=
MAXIMUM NUDITY
```

最短式：

> **MORE EXPOSED != MORE EROTIC。**

## 5.3 鞋、裙、褲口共同形成顯影框架

生成時不要只問：

> 「腳露了多少？」

而要問：

```text
鞋穿著嗎？
鞋尖看得見嗎？
裙腳在哪裡？
褲口是否遮住鞋幫？
是走動時偶露，還是人物故意展示？
是她自己調整，還是外力造成暴露？
暴露之後她有沒有重新遮回？
```

這些答案屬於事件／人物動作，不得由「她是纏足女性」自動補完。

---

# 6｜GAIT / SOUND / BEARING｜儀態與步態

## 6.1 當時文本不需要科普「什麼是小腳」

《海上花列傳》第一回只寫一路「咕咕咯咯」小腳聲音，人物便知道陸秀寶來了。

這是非常重要的 native-world evidence：

> **對同文化人物，小腳、鞋聲與步態可以是日常可辨認訊號，不必由旁白像現代研究者一樣重新解釋。**

因此：

```yaml
NATIVE_GAZE_RULE:
  if_character_familiarity_high:
    avoid:
      - "第一次理解什麼叫纏足"
      - "把小腳當異文化奇觀"
      - "無因果的現代醫學旁白"
    prefer:
      - "人物直接讀鞋樣、步態、穩不穩、露得巧不巧"
      - "只有異常時才特別注意身體限制"
```

## 6.2 「婀娜」是審美解讀，不是生物力學結論

《九尾龜》第七十回的人物直接把小腳步態比成「出水荷花，隨風楊柳」，同一段又提及纏足痛苦。

這一段最有價值的不是證明「纏足讓人自然婀娜」，而是證明：

```text
ALTERED GAIT
+
PERIOD AESTHETIC INTERPRETATION
CAN COEXIST
```

因此不要寫：

> 「纏足使女人天然走得婀娜。」

應建模為：

```text
FOOTBINDING_ALTERS_GAIT
+
PERIOD_OBSERVER_MAY_CODE_GAIT_AS
蓮步 / 凌波 / 裊娜 / 楊柳 / 嬌弱
```

其中審美詞是觀看文化，不是醫學事實。

## 6.3 聲音也是身體的一部分

《海上花》多次以「小腳高底聲響」直接預告人物接近。

因此場景可以使用：

- 木底／高底／鞋底落地的聲音；
- 走快時聲音節奏改變；
- 樓梯、木地板、房內地面帶來不同回聲。

但鞋聲不能單獨反推：

- 身分；
- 性格；
- 情色意圖；
- 纏足嚴重程度。

---

# 7｜BODY CONDITION｜平衡、支撐、疲勞與個體差異

## 7.1 有限制，但不是「不能動」

來源同時存在兩組證據。

### A｜平衡較容易受外力與鞋底幾何影響

《九尾龜》第五回張書玉穿高底弓鞋時，敘事直接說走路「不甚穩當」。

《海上花》第五回吳雪香穿小腳高底、趔趄著腳；被突然拖腕時「站不穩」，跌入對方懷中。

### B｜纏足女性仍可以快速、主動、強力移動

《海上花》第十回沈小紅伴隨「小腳高底」聲響，仍能飛快衝出、縱身直撲。

第二十五回陸秀寶趔趄著小腳，仍可突然奮身一撲，整個身體壓向對方。

所以正式鎖：

```text
FOOTBINDING_CONSTRAINT
!=
HELPLESSNESS
```

## 7.2 支撐面改變，但程度不可假精準

纏足可能使站立／轉身／快速重心轉移更依賴：

- 膝；
- 小腿；
- 大腿；
- 髖；
- 臀部；
- 手臂；
- 家具；
- 牆面；
- 同伴身體。

但本 PATCH 不提供假醫學精度。

每位人物必須以自己的：

```yaml
INDIVIDUAL_VARIATION:
  binding_degree:
  current_shoe_geometry:
  habitual_training:
  current_pain:
  current_fatigue:
  floor_surface:
  stairs_or_slope:
  current_speed:
  support_available:
```

決定當下行動。

沒有證據時保持 UNKNOWN。

## 7.3 疼痛與傷害必須能存在

《海上花》第三十二回直接提到極端纏足造成腳趾傷害；《三寸金蓮》更以現代小說重構大量初纏、改纏疼痛。

因此：

```text
PERIOD BEAUTY
DOES NOT ERASE
BODY PAIN
```

同時：

```text
BODY PAIN
DOES NOT ERASE
PERIOD BEAUTY CODE
```

兩者可以同時成立。

## 7.4 疲勞是累積態

《九尾龜》第八十一回陳文仙本已「身體嬌弱」，又是一雙三寸金蓮，連續收拾行李後出現喘息與出汗。

不得從單一段落推導「所有纏足女子都體弱」，但可以建立：

> **活動量、鞋履、站立時間、搬動、樓梯與當日足部狀態，會累積成下一個節點仍然存在的 fatigue。**

---

# 8｜SHOE / WRAPPING STATE｜鞋與裹布不是一個開關

成人或私人場景中，不要只有：

```text
穿鞋
→
全裸足
```

可存在多個合法狀態：

```yaml
FOOTWEAR_WRAPPING_STATE:
  - "SHOES_ON"
  - "ONE_SHOE_REMOVED"
  - "BOTH_SHOES_REMOVED"
  - "SHOES_OFF_WRAPPING_REMAINS"
  - "WRAPPING_ADJUSTED"
  - "UNBOUND / ONLY IF EVENT AND CHARACTER ESTABLISH IT"
```

《金瓶梅》第六回把「脫一隻繡花鞋—以鞋作酒杯—再進入床笫」寫在同一條親密過渡鏈上；第八十二回又把脫繡鞋直接放入性愛序列。

這能支持：

> **脫鞋本身可是一個私密／情色 transition。**

但不能推出：

```text
SHOE_REMOVAL
=
UNWRAPPING
=
SEXUAL CONSENT
```

## 8.1 性愛時保留鞋履是合法歷史顯影候選

《金瓶梅》另有性愛場景先讓女性保持紅鞋，之後才摘鞋。

因此：

```text
SEX EVENT
DOES NOT REQUIRE
IMMEDIATE FULL FOOT EXPOSURE
```

這點非常重要，因為現代色情生成很容易自動遵循「越裸越情色」的單一路徑，而來源恰好提供反例。

---

# 9｜PERIOD NATIVE GAZE｜時代人物不是現代田野研究者

生成器必須先判斷：

```yaml
CHARACTER_FOOTBINDING_FAMILIARITY:
  UNKNOWN:
  LOW:
  ORDINARY:
  HIGH:
  PROFESSIONAL_OR_FENGYUE_EXPERIENCE:
```

若人物從小生活在該文化、又熟悉風月場／婚嫁／女裝／鞋履，則他可能直接讀懂：

- 腳大腳小；
- 鞋樣是否周正；
- 鞋底高低；
- 步態是否穩；
- 裙下是否故意露出；
- 鞋尖碰觸是否是場面暗號；
- 某一腳的展示是否比平常更私人。

他不需要在腦中說：

> 「這就是中國古代纏足文化造成的生理現象。」

除非人物本身正處於反思、醫療、改良、比較文明或異文化觀察語境。

---

# 10｜FEMALE SELF-AESTHETIC AGENCY｜女性自己的審美與展示能力

來源不能被簡化成「男人看、女人被看」。

至少在小說顯影裡，可以確認女性也會：

- 選鞋；
- 比鞋；
- 做鞋／改鞋；
- 留意鞋樣；
- 控制裙腳；
- 故意展示或收回；
- 用腳尖／金蓮作場面訊號；
- 在被看時重新整理／約束；
- 以鞋履、步態參與女性間的審美競爭。

因此：

```text
FEMALE AESTHETIC AGENCY
CAN EXIST
WITHOUT
ERASING STRUCTURAL COERCION OR PAIN
```

同樣：

```text
HISTORICAL COERCION / PAIN
DOES NOT AUTHORIZE THE MODEL
TO ERASE FEMALE CHOICE INSIDE A GIVEN SCENE
```

人物在當前一幕仍有自己的行動主權。

---

# 11｜INTIMACY GRAMMAR｜小腳如何進入親密，而不是變成 fetish 插件

本 PATCH 對成人親密的核心定義：

> **小腳的成人情色價值，不只在於「摸腳」，而在於鞋、裙、步態、展示、脫鞋、腿部位置、支撐與換位共同改變兩個身體如何靠近。**

來源提供的高價值語法包括：

```text
公開場面只見弓鞋／鞋尖
→
人物刻意顯示／鞋尖碰觸／桌下勾腳
→
私人空間中脫鞋或保留鞋
→
腿部與身體支撐關係改變
→
成人事件若已合法成立，纏足條件持續影響姿勢與轉位
```

注意：這是**可能的顯影鏈**，不是固定劇本。

---

# 12｜ADULT GATE｜成人域先成立，纏足 PATCH 才能進成人層

```yaml
ADULT_ACTIVATION_GATE:
  all_participants_confirmed_adult: REQUIRED
  adult_event_qualified_by_host_world: REQUIRED
  current_consent_or_event_boundary: READ_ONLY_FROM_HOST
  footbinding_is_adult_evidence: false
  footbinding_is_consent_evidence: false
  profession_is_adult_evidence: false
  beauty_is_consent_evidence: false
```

硬鎖：

```text
FOOTBINDING != ADULTHOOD
FOOT DISPLAY != CONSENT
SHOE REMOVAL != CONSENT
FOOT CONTACT != SEX CONSENT
BODY RESPONSE != CONSENT
RELATION != CONSENT
```

本 PATCH 不創造任何人物慾望、同意或性行為。

---

# 13｜SEXUAL BODY MECHANICS｜纏足條件對性愛「方式」的影響

本節只在 **成年人 + 成人事件已合法成立** 後啟用。

它不規定「纏足女性應該用哪些姿勢」，而是要求每個姿勢先回答：

```text
重量由哪裡承擔？
腳是否需要踩實？
膝與髖是否有支點？
是否需要突然轉身？
是否拉扯腳踝／足部？
鞋與裹布目前在什麼狀態？
前一個動作留下了什麼疲勞或痛感？
下一個動作是誰主動發起？
```

## 13.1 SUPINE / 仰臥型

一般特徵：

- 足部可以不承重；
- 主要支撐由床面、髖、臀、大腿與背部承擔；
- 若需要抬腿，優先支撐大腿、膝彎或小腿，而不是把纏足／腳踝當槓桿；
- 腿部張開幅度由人物自己的髖、膝與當下舒適度決定；
- 鞋／裹布可以保留或移除，不能自動假定。

```text
LEG_ELEVATION
!=
PULL_BY_BOUND_FOOT
```

## 13.2 SIDE-LYING / 側臥型

一般特徵：

- 足部承重低；
- 適合長時間維持相對穩定身體關係；
- 轉位主要從髖、肩、膝與床面發生；
- 若當日已有足部疲勞，側臥不代表疼痛自動消失，但能降低站立負荷。

## 13.3 SEATED / LAP / BED-EDGE｜坐姿／腿上／床沿型

一般特徵：

- 坐具、床沿或對方身體承擔主要重量；
- 小腿可以垂下、輕搭、收回或置於床面；
- 平衡更多依賴臀、髖、大腿與手臂；
- 從站立轉坐下、再從坐姿起身，是比靜態畫面更需要處理的 transition。

## 13.4 WOMAN-ON-TOP / 上位型

**不是因為纏足就禁止。**

可能的穩定來源：

- 雙膝；
- 大腿；
- 髖；
- 手掌／前臂；
- 床面；
- 對方軀幹。

足掌不必成為主要支點。

真正需要顯影的是：

- 如何上去；
- 如何找重心；
- 如何在疲勞後改變支撐；
- 如何下來。

> **纏足條件最容易被 AI 忘掉的，不是靜態姿勢，而是姿勢之間的轉換。**

## 13.5 KNEELING / 跪姿型

不得把「跪」理解成所有人腳掌必須以現代自然足方式平貼床面。

需要看：

- 膝蓋是否承重；
- 小腿是否有床面；
- 足部是否被壓在身下；
- 當事人是否習慣／能耐受該角度；
- 鞋履／裹布是否妨礙；
- 是否需要墊褥或改變腿的位置。

```text
KNEELING
=
PERSON-SPECIFIC BODY GEOMETRY
```

不是固定模板。

## 13.6 STANDING / 站立型

通常需要最高的平衡與支撐注意。

可能使用：

- 牆；
- 床沿；
- 桌／椅；
- 柱；
- 對方身體；
- 短時間站立後轉為坐／臥。

不得寫成：

```text
BOUND FEET -> STANDING SEX IMPOSSIBLE
```

也不得寫成：

```text
BOUND FEET -> NO DIFFERENCE AT ALL
```

應由當事人的實際身體狀態裁決。

## 13.7 RAPID TRANSITIONS / 快速轉位

每次轉位都要重新計算：

```yaml
TRANSITION_RECALC:
  prior_support:
  new_support:
  foot_load_change:
  knee_hip_load_change:
  balance_change:
  pain_change:
  fatigue_change:
  footwear_change:
  who_initiated:
  whether_other_person_adjusted:
```

這正是纏足 PATCH 與成人心法 `TRANSITION CAUSALITY` 最自然的接合點。

---

# 14｜LOCAL PAIN｜腳痛不等於整場性愛自動停止，也不等於可以忽略

纏足相關疼痛可能只在：

- 足趾；
- 足弓；
- 足背；
- 腳跟；
- 腳踝；
- 小腿；
- 特定鞋壓點；
- 久站之後的疲勞。

因此：

```text
LOCAL FOOT PAIN
!=
AUTOMATIC GLOBAL REFUSAL
```

但同樣：

```text
LOCAL FOOT PAIN
!=
IGNORE AND CONTINUE IDENTICALLY
```

正確顯影應是：

```text
疼痛出現
→
當事人動作／聲音／重心改變（若事件中有證據）
→
下一個節點調整支撐、角度、鞋履或姿勢
→
疼痛／疲勞繼續被記住
```

若人物明確拒絕、要求停止、撤回或離開，則由 Host／既有成人邊界立即處理；本 PATCH 沒有覆寫權。

---

# 15｜FOOT CONTACT GRAMMAR｜腳部接觸的社會與情色層級

來源顯示，至少可區分：

```yaml
FOOT_CONTACT_LEVELS:
  L0_PUBLIC_VISIBILITY:
    examples:
      - "裙下弓鞋可見"
      - "走路鞋聲"

  L1_CONTROLLED_DISPLAY:
    examples:
      - "顯蓮瓣"
      - "提高褲管露鞋／腳形"
      - "有意無意讓鞋尖碰到對方"

  L2_PRIVATE_OR_FLIRT_CONTACT:
    examples:
      - "桌下用金蓮勾對方"
      - "碰腳／鞋尖作暗號"

  L3_SHOE_REMOVAL:
    examples:
      - "脫一隻鞋"
      - "拿鞋作酒令／調情物"

  L4_ADULT_BODY_INTEGRATION:
    condition: "ONLY AFTER ADULT EVENT QUALIFIED"
    examples:
      - "腿部位置、支撐、鞋履狀態進入性愛 mechanics"

  L5_UNWRAPPING_OR_BARE_FOOT:
    condition: "ONLY IF SPECIFIC EVENT ESTABLISHES IT"
    default: false
```

注意：這不是「親密度必然逐級升高」的關係計量表，只是**顯影通道分類**。

任何一層都不能自動授權下一層。

---

# 16｜CURRENT BODY STATE MUST PERSIST｜上一秒必須算數

本 PATCH 採用：

> **身體必須記得上一秒。**

例如：

```text
剛才高底鞋走了很久
→ 下一幕腳／小腿可能已有疲勞

剛才被突然一拉失去平衡
→ 下一動作若仍站著，必須有重新找支點的過程

剛才腳部被壓疼
→ 換姿勢時不能像 reset 一樣完全無痕

剛才脫了一隻鞋
→ 下一節點不能無因果地又變成雙鞋穿好
```

這不是增加「疼痛戲份」，而是維持物理連續性。

---

# 17｜DATA MODEL｜候選結構

```yaml
FOOTBINDING_BODY_CONTEXT:
  established: true|false|UNKNOWN

  source_scope:
    period:
    region:
    community_or_class:
    character_evidence:
    confidence:

  body:
    binding_degree: "UNKNOWN|LIGHT|MODERATE|SEVERE|SOURCE_SPECIFIC"
    current_pain:
    current_fatigue:
    sensitivity:
    balance_state:
    support_base:
    mobility_notes:

  dress:
    wrapping_state:
    shoe_type:
    sole_height:
    shoe_fit_or_shape:
    hem_exposure:
    trouser_cuff_relation:

  aesthetic_code:
    character_familiarity:
    observer_familiarity:
    size_reading:
    shape_reading:
    shoe_reading:
    gait_reading:
    display_control:

  intimacy:
    adult_qualified: true|false|UNKNOWN
    local_boundaries:
    foot_contact_status:
    footwear_removal_status:
    support_requirements:
    transition_risk:
    prior_node_residue:
```

禁止填假精準數值。

```text
沒有來源的纏足程度
!=
模型自行猜一個「三寸」
```

---

# 18｜與既有成人心法／Runtime 的接口

本 PATCH 不新增第二套性愛系統。

若未來吸收進通用成人心法，建議作為：

```text
HISTORICAL_BODY_CONDITION PROVIDER
```

由成人節點在 `body_relation` 之前讀取，而不是取代既有成人節點。

候選接口：

```yaml
SEXUAL_MANIFESTATION_NODE:
  historical_body_condition_ref:
  body_relation:
  active_body_parts:
  action_relation:
  pressure_or_depth:
  support_and_balance:
  pain_or_fatigue:
  vocal_capacity:
  character_speech_function:
  next_step_authorship:
  spatial_constraint:
  residue_from_prior_nodes:
  narrator_register:
  body_noun_register:
```

其中：

```text
historical_body_condition_ref
→ 改變 support_and_balance / pain_or_fatigue / spatial_constraint / transition choices
→ 不修改 CHARACTER DECISION / CONSENT / RELATION
```

## 18.1 與方法卡的天然接線

```yaml
METHOD_CARD_BINDING:
  CARD_15_PAIN_CHANNEL_LOCALITY:
    contribution: "足部痛感保持局部，不自動翻譯成全身／情感／同意結論。"

  CARD_16_NEXT_STEP_AUTHORSHIP:
    contribution: "女人自己的腿、腳、鞋與身體怎麼調整，仍由她的當下動作／決定顯影。"

  CARD_17_TRANSITION_CAUSALITY:
    contribution: "姿勢改變時重新計算支撐、重心與鞋履狀態。"

  CARD_18_LONG_HORIZON_INTEGRITY:
    contribution: "足痛、疲勞、鞋履與裹布狀態不在長場景中無故 reset。"

  CARD_19_VALID_DOMAIN_EXPLORATION:
    contribution: "一條足部動作受限，不代表整個合法成人顯影域全部消失。"

  CARD_20_DIRTY_REGISTER_INTEGRITY:
    contribution: "不為了漂亮而刪除笨拙、失衡、汗、鞋聲、重新找支點等真實身體細節。"

  CARD_21_BOUNDARY_EVIDENCE_INTEGRITY:
    contribution: "『顯腳／碰腳／脫鞋』只證明該事件本身，不偽造更大的同意邊界。"
```

---

# 19｜ANTI-FAILURE LOCKS｜反退化規則

```yaml
FOOTBINDING_ANTI_FAILURE:

  F01_MODERN_ANTHROPOLOGIST_GAZE:
    fail: "時代內熟悉纏足的人物無故像現代研究者一樣驚訝／科普。"

  F02_FETISH_COLLAPSE:
    fail: "整個女人被縮成一雙腳；所有情色都繞著腳。"

  F03_BEAUTY_ONLY_ROMANTICIZATION:
    fail: "只有三寸金蓮之美，疼痛、疲勞、平衡與傷害全部消失。"

  F04_INJURY_ONLY_DE_EROTICIZATION:
    fail: "因現代價值而把時代人物確實存在的美感／情色讀法全部洗掉。"

  F05_UNIVERSALIZATION:
    fail: "北宋以後女性 = 一律纏足。"

  F06_SIZE_ONLY:
    fail: "越小必然越美；忽略四寸仍被來源形容為伶俏／動人，以及鞋樣周正。"

  F07_HELPLESSNESS:
    fail: "纏足女性只能被扶、不能跑、不能撲、不能主動改變位置。"

  F08_STATIC_POSE:
    fail: "只畫姿勢，不處理如何進入／退出姿勢。"

  F09_UNBINDING_AUTOMATIC:
    fail: "進入性愛 = 自動把裹腳布全部解開。"

  F10_SHOE_REMOVAL_CONSENT:
    fail: "脫鞋 = 同意性交或更進一步接觸。"

  F11_DISPLAY_CONSENT:
    fail: "顯蓮瓣／鞋尖碰觸 = 授權摸腳／性行為。"

  F12_BODY_LIMIT_IMPLIES_PERSONALITY:
    fail: "步態限制 = 被動／嬌弱／服從的人格。"

  F13_HIGH_SOLE_EQUALS_FOOTBINDING:
    fail: "看見高底鞋就自動認定纏足。"

  F14_LITERARY_METAPHOR_AS_BIOMECHANICS:
    fail: "把凌波、楊柳、蓮步直接當醫學結論。"

  F15_DONOR_BECOMES_CULTURE_LAW:
    fail: "把《三寸金蓮》七字法／四忌變成全歷史硬規則。"

  F16_PORN_SOURCE_OVERRIDES_CHARACTER:
    fail: "因《金瓶梅》有鞋／腳情色，就讓所有人物自動喜歡足部性愛。"

  F17_CURRENT_BODY_STATE_IGNORED:
    fail: "上一節點腳痛／失衡／疲勞，下一秒無因果消失。"

  F18_NO_VARIATION:
    fail: "所有纏足女性都有同一尺寸、同一痛感、同一走法、同一性姿勢限制。"

  F19_PERIOD_SCOPE_LEAK:
    fail: "把現代重構小說當第一手晚清史料。"

  F20_ADULT_GATE_BYPASS:
    fail: "因纏足、風月職業或情色描寫就推定人物成年。"
```

---

# 20｜REGRESSION TESTS｜最小回歸組

## T01｜三寸不是唯一美值

**INPUT**：來源人物金蓮約四寸，但文字明確說「甚是伶俏」。

**EXPECT**：

```text
ATTRACTIVE_ALLOWED
SIZE_ONLY_RULE_REJECTED
```

**FAIL IF**：模型改寫成「四寸不算美」。

## T02｜小腳不是失能

**INPUT**：纏足／小腳高底女性突然衝出、撲向他人。

**EXPECT**：可生成快速主動動作，但保留合理平衡／支撐因果。

**FAIL IF**：因「小腳」直接阻止一切快速動作。

## T03｜突然外力與高底平衡

**INPUT**：小腳高底女性在未準備時被拉腕。

**EXPECT**：失去平衡是合法候選；若來源已明示則直接成立。

**FAIL IF**：她像自然足平底鞋般完全不受重心變化影響。

## T04｜顯蓮瓣

**INPUT**：女性故意伸腳展示並微笑。

**EXPECT**：可成立 flirt/display signal。

**FAIL IF**：直接升格為性交同意、愛情或關係承諾。

## T05｜鞋尖碰觸

**INPUT**：來源明示鞋尖「有意無意」碰對方腳並伴隨眼風。

**EXPECT**：成立當場可讀的調情／暗號 evidence。

**FAIL IF**：推導永久偏愛或後續性同意。

## T06｜性愛時鞋仍穿著

**INPUT**：成人事件已成立，來源／場景顯示鞋仍在腳上。

**EXPECT**：合法；不強制脫鞋。

**FAIL IF**：模型以「性愛必須裸足」自動修改。

## T07｜只脫一隻鞋

**INPUT**：調情中脫一隻鞋。

**EXPECT**：一隻鞋脫、一隻仍穿的狀態可持續。

**FAIL IF**：自動變成全部鞋襪／裹布皆除。

## T08｜局部腳痛

**INPUT**：成人場景中足部出現疼痛，人物未拒絕整場事件。

**EXPECT**：調整支撐／姿勢；同意狀態仍依 Host／人物事件。

**FAIL IF**：

- 把痛感自動翻成「她其實不想要」；或
- 完全忽略疼痛照舊重複同一動作。

## T09｜北宋以後未提供人物證據

**INPUT**：「這是一名南宋／明／清女性」，但沒有她是否纏足的資料。

**EXPECT**：`FOOTBINDING = UNKNOWN`。

**FAIL IF**：自動補成三寸金蓮。

## T10｜《三寸金蓮》七字法

**INPUT**：使用「靈、瘦、彎、小、軟、正、香」。

**EXPECT**：標成 modern reconstructive donor vocabulary。

**FAIL IF**：宣稱「這就是歷代中國公認七項標準」。

## T11｜女性上位

**INPUT**：成年人、成人事件已成立、纏足女性主動採上位。

**EXPECT**：合法候選；重心可由膝、大腿、手臂、床面承擔。

**FAIL IF**：因纏足直接判定不可能。

## T12｜站立成人互動

**INPUT**：成年人、成人事件已成立，站立互動。

**EXPECT**：要求更高支撐；牆／家具／對方身體可成支點；依個體狀態決定持續時間。

**FAIL IF**：寫成完全無差異，或直接全域禁止。

## T13｜同一人物跨節點

**INPUT**：上一節點高底鞋走遠路後已累。

**EXPECT**：下一節點 `fatigue` 保留。

**FAIL IF**：每次成人動作開始即身體 reset。

---

# 21｜SOURCE EVIDENCE MAP｜來源證據表

> 本表只列本 PATCH 實際使用的核心證據。小說人物發言仍是小說內證據，不自動升格為歷史人口統計。

| 來源 | 章回／位置 | 可支持 | 不可支持 |
|---|---|---|---|
| 《九尾龜》 | 第5回 | 張書玉高底弓鞋與「走起路來不甚穩當」；鞋底幾何可進入平衡描寫 | 所有纏足女性都不穩 |
| 《九尾龜》 | 第12回 | 張書玉桌下用金蓮勾章秋谷，腳可作私下場面訊號 | 足部接觸自動等於性同意 |
| 《九尾龜》 | 第16回 | 約四寸紅緞弓鞋仍「更覺動人」 | 只有四寸才美 |
| 《九尾龜》 | 第18回 | 王雙林提高褲管賣弄金蓮；三寸鞋尖碰腳作調情訊號 | 所有倌人都如此 |
| 《九尾龜》 | 第30回 | 蓮步、鞋尖、視線與重新約束小腳；展示與收回可受女性自己控制 | 女性的所有展示皆出於性邀請 |
| 《九尾龜》 | 第70回 | 時代人物可把纏足步態情色化，也可同時意識疼痛 | 「纏足天然使人婀娜」的醫學結論 |
| 《九尾龜》 | 第81回 | 三寸金蓮人物在長時間收拾後可顯疲勞；活動量有 body residue | 三寸金蓮必然體弱 |
| 《海上花列傳》 | 第1回 | 「小腳聲音」可作日常人物接近訊號 | 鞋聲可判定性格 |
| 《海上花列傳》 | 第5回 | 小腳高底、趔趄、突然被拉後站不穩 | 拉扯是合法親密方式；該段本身反而有不情願訊號 |
| 《海上花列傳》 | 第10回 | 小腳高底女性仍可快速奔出、縱身撲人 | 纏足沒有任何限制 |
| 《海上花列傳》 | 第25回 | 小腳女性可扭身、欲前不前、突然奮身一撲並用全身重量互動 | 這種動作是所有女性固定「媚態」 |
| 《海上花列傳》 | 第32回 | 纏足可造成嚴重腳趾傷害 | 所有人都遭同程度傷害 |
| 《海上花列傳》 | 第45、59回 | 「梳頭纏腳」可成堂子女性成長／職業身體史的一部分 | 所有風月女性經歷一致 |
| 《品花寶鑒》 | 第9回 | 三寸蓮鉤可由女性主動展示；旁觀者能讀成「顯蓮瓣」 | 展示＝同意觸碰 |
| 《品花寶鑒》 | 第38回 | 清代小說人物明確區分「略纏」與「緊纏使尖如蓮瓣」 | 可直接建立纏足起源史 |
| 《品花寶鑒》 | 第40回 | 三寸金蓮可成男性情色觀看的一部分 | 所有男性都戀足 |
| 《品花寶鑒》 | 第50回 | 約四寸金蓮仍「甚是伶俏」 | 尺寸與美的固定公式 |
| 《品花寶鑒》 | 第57回 | 「三寸還不滿」與長距離逛園的困難被人物直接連結 | 所有三寸腳都不能走 |
| 《品花寶鑒》 | 第57回遊戲 | 脫鞋、鞋作酒具具有私密／戲謔性；被勾腳可能跌倒 | 強行脫鞋是可接受親密行為 |
| 《金瓶梅》 | 潘金蓮出場／前段 | 小腳、鞋、步態與全身女性美被連續描述 | 晚清人物必須使用同一套語彙 |
| 《金瓶梅》 | 第6回 | 脫一隻繡鞋、鞋杯調情，之後才進入床笫；鞋是 intimacy transition | 脫鞋＝性交同意 |
| 《金瓶梅》 | 第23回 | 「不在乎大小，鞋樣子周正才好」反證 size-only | 大小完全不重要 |
| 《金瓶梅》 | 第28回 | 三寸紅繡鞋可作高度私密的情色物件／調情媒介 | 鞋物本身建立感情 |
| 《金瓶梅》 | 第82回 | 「脫繡鞋」直接嵌在成人性愛序列 | 所有性愛都要脫鞋／玩腳 |
| 《三寸金蓮》 | 第4回 | 「七字法」作小說內蓮癖審美重構 | 歷史通用法則 |
| 《三寸金蓮》 | 第5回 | 形／態、鞋履與「藏露」被系統化；一閃比全露更有效 | 第一手清代民俗統計 |
| 《三寸金蓮》 | 第6回 | 小腳「四忌」、改纏後失衡等為 body/bearing reconstruction donor | 全中國女子必守同一四忌 |

---

# 22｜OPEN QUESTIONS｜仍不得封閉的問題

```yaml
OPEN_QUESTIONS:
  - "北宋至元、明初不同地域的實際纏足比例與形制差異，本 donor set 不足。"
  - "各地裹法造成的足形／鞋形差異，需要更直接史料才能細分。"
  - "特定性愛姿勢在歷史文本中的分布頻率，本輪未做統計研究。"
  - "鞋、襪、裹腳布在不同階層私人空間中的脫除禮俗，不應由單一情色小說推定。"
  - "疼痛、神經、肌骨與長期生理後果若要寫成醫學級模型，需要另接醫學／生物考古來源。"
  - "現代《三寸金蓮》的蓮學分類需要保持為 interpretive donor，不應被證據漂白成古代術語。"
```

UNKNOWN 合法。

---

# 23｜最小生成算法

當人物已確立纏足時：

```text
STEP 1
先讀 BODY CONDITION
不是先找「金蓮」形容詞。

STEP 2
讀 SHOES / WRAPPING / HEM
確定她現在實際穿什麼、露多少。

STEP 3
讀 CURRENT ACTION
站、走、坐、跪、臥、上樓、轉身、被拉、主動撲近，各自需要不同支撐。

STEP 4
讀 PERIOD AESTHETIC CODE
只有當觀察人物有資格理解這套審美時，才讓「蓮步／鞋樣／三寸／弓鞋」取得相應意義。

STEP 5
若進成人事件，先確認成人資格與事件資格。

STEP 6
成人 mechanics 先算 support / balance / pain / transition。

STEP 7
最後才選語言 register。
```

所以：

> **詞跟著身體關係走，不是身體跟著「三寸金蓮」四個字走。**

---

# 24｜核心公理

```yaml
FOOTBINDING_PATCH_AXIOMS:

  AXIOM_01:
    "FOOTBINDING IS A BODY CONDITION, NOT A DECORATIVE TAG."

  AXIOM_02:
    "PERIOD AESTHETICS AND PHYSICAL COST MAY COEXIST."

  AXIOM_03:
    "SIZE IS ONE SIGNAL; SHAPE, SHOE, GAIT, PROPORTION AND DISPLAY ALSO MATTER."

  AXIOM_04:
    "MORE EXPOSED != MORE EROTIC."

  AXIOM_05:
    "DISPLAY != ACCESS != CONSENT."

  AXIOM_06:
    "BOUND FEET != HELPLESS BODY."

  AXIOM_07:
    "THE BODY MUST REMEMBER THE PREVIOUS SECOND."

  AXIOM_08:
    "NATIVE CHARACTERS READ THEIR WORLD; THEY DO NOT AUTOMATICALLY EXPLAIN IT TO THEMSELVES."

  AXIOM_09:
    "A DONOR TEXT PROVIDES EVIDENCE OR FORM; IT DOES NOT BECOME CULTURAL LAW."

  AXIOM_10:
    "ADULT RENDERING ONLY AFTER ADULT QUALIFICATION AND EVENT QUALIFICATION."
```

---

# 25｜一句話收束

> **不要只寫「小腳很美」；要讓鞋、裙、步態、支撐、藏露、疲勞與下一個動作共同證明：這個時代的人看見了什麼，而這副身體又真正能怎麼動。**

以及成人顯影時：

> **纏足不替人物創造性慾；它只改變已成立親密事件中，身體如何靠近、承重、換位、展示、疼痛與繼續。**

---

# APPENDIX A｜本輪 donor 檔案 provenance

```yaml
DONOR_FILES:
  - title: "九尾龜"
    file: "九尾龜.epub"
    sha256: "84455e66dc09c93f50236fe3cdfd553731eb671f6f8601408137aa5e7096f328"
    class: "PRIMARY JWG SOURCE / LATE-QING"

  - title: "海上花列傳"
    file: "海上花列傳.epub"
    sha256: "cda8307097338ae5769c7d3627b6ff54432e976eca2d1a6dd0876e0c899a3d00"
    class: "NEAR-PERIOD SHANGHAI LITERARY DONOR"

  - title: "品花寶鑒"
    file: "品花寶鑒.epub"
    sha256: "b398f93e7a80a926281bc80d261252faf2400bdcb3e7306a992f2a90d1464df5"
    class: "QING NEAR-ERA LITERARY DONOR"

  - title: "金瓶梅"
    file: "金瓶梅.txt"
    sha256: "67ef613e5664eea36018d303747f68c476a0563703eac63db708b0b146ce662e"
    encoding: "GB18030"
    class: "EARLIER EROTIC-GRAMMAR DONOR"

  - title: "三寸金蓮"
    author: "馮驥才"
    file: "1292.epub"
    sha256: "d3cf1809bcf564751874b2fd641ee81235d49d0f5a93464b714b0011ae063049"
    class: "MODERN HISTORICAL-CULTURAL RECONSTRUCTIVE DONOR"
```

---

# APPENDIX B｜未來吸收建議

若未來正式寫入「性愛心法」，建議不要建立「金蓮專用性愛模組」。

建議抽象為：

```text
HISTORICAL EMBODIED CONDITION LAYER
```

纏足只是第一個成熟案例。

同一層未來可容納其他**已由世界／人物來源合法成立**、會改變：

- 支撐；
- 平衡；
- 活動幅度；
- 疼痛；
- 衣著；
- 身體展示；
- 親密轉位；

的歷史身體條件。

這樣成人心法不必把每一種歷史身體都做成 fetish plugin，而是學會一個更通用的原則：

> **人物先有身體；身體再進入事件；事件成立後，情色才從真實的身體關係裡長出來。**

