# 觀止青樓｜白御行線 HOT SAVE V4.2
## 理火三年榴月九日夜｜曹州假印案多日追查止手 × 疑似何先生今夜借名 × 全員放行 × 中央籠台完工試光 × 女子競技／賭盤／護衛人才池 × 榴月十一日重新開幕準備版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V4_2_LIU09_NIGHT_CAOZHOU_STOP_HE_RELEASE_CAGE_LIGHTTEST_WOMEN_COMBAT_REOPEN_PREP"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V4.2"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V12.0"
  character_source: "觀止人物卡池_LCAPG_V2.3_李清照趙受益錦棠顧青簡增補_薛濤魚玄機暫定入場_正式版.md"

  story_time_span:
    start: "HOT V4.1 後／理火三年榴月四日午後"
    current: "理火三年榴月九日夜"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AFTER_WORK_CLOSE; GUANZHI_PREPARING_FOR_LIU11_EVENING_REOPENING"

  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V4.1_榴月四日午後_九人丫鬟遴選_牙行成交_制服剪髮_白希明礬分教_落選吃麵收尾版.md"
  previous_hot_sha256: "832c2ccae0efecc9904e1f3e611340a97672b12eb22852e81391c1b7105d37cb"

  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md"
  long_term_master_sha256: "0149362b4128d62d947d4ffbcc618003913b1cad7052d57fe5b3f84f8f05084f"

  save_scope:
    - "HOT V4.1 後至榴月九日夜之曹州假印案多日追查、江湖懸賞、分線跟蹤、收網、分押、供述拆解與結構顯影"
    - "『何先生』作為人名／位置／借名之多重不確定性；疑似核心男子之拘押、觀止中央籠台私下面談、今夜借名與故事供述"
    - "白御行由『審訊』轉為『對手』待遇，給桌椅、筆墨、美酒、美食並由白希添酒磨墨"
    - "白御行判定此類手法屬可重生、低值得長期纏鬥之江湖結構，命顧青簡釋放全部曹州案現有被拘者，停止親自追查"
    - "觀止中央鐵籠／顯影舞台已完成至可實用，完成全暗＋中央光之私下試光；第三版亮度／光位效果獲紅娘與潘金蓮接受"
    - "女子競技項目之定位、招募資格、牙行與自由參賽者分流、賞金、服裝、比賽規則、賭盤與開幕暖場位置"
    - "女子競技可作女性護衛／保鑣人才第一層顯影；實際護衛能力須另測，不以擂台勝負直接等同護衛資格"
    - "榴月十一日晚觀止重新開幕之時間鎖、入場費與座席層級、女子競技暖場→紅娘壓軸之第一版流程"
```

---

# 0｜提交法位、來源與反污染說明

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V4.1_榴月四日午後_九人丫鬟遴選_牙行成交_制服剪髮_白希明礬分教_落選吃麵收尾版.md"
    role: "本檔直接前置 HOT；V4.1 及以前有效硬狀態全部繼承，除本檔明示更新／校正者"
    sha256: "832c2ccae0efecc9904e1f3e611340a97672b12eb22852e81391c1b7105d37cb"

  master_archive:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md"
    role: "截至 HOT V3.4 之長期固化；V3.5→V3.6-R2→V3.7→V3.8→V3.9→V4.0→V4.1→本 V4.2 依序作較新合法疊加"
    sha256: "0149362b4128d62d947d4ffbcc618003913b1cad7052d57fe5b3f84f8f05084f"

  current_character_source:
    file: "觀止人物卡池_LCAPG_V2.3_李清照趙受益錦棠顧青簡增補_薛濤魚玄機暫定入場_正式版.md"
    role: "跨線人物基線；本輪曹州案人物、女子競技參賽者與開幕安排均只屬白御行線 ROUTE EVENT／營運狀態"
    sha256: "b7ce5f3e8870b170499e70bfe60b3d6b951987badc795434d7dfd9ef06637d59"

  runtime_reference:
    file: "觀止青樓_主程序_V12.0_FIELD_STATE接戲分析器場態整合正式版.md"
    version: "V12.0"
    status: "DOCUMENT_LEVEL_CURRENT_GUANZHI_RUNTIME_SPEC"
    sha256: "2159467f8a1d3eb31a8a0930e7d7b421bd7501a32eff35ceea383288f25a1978"

  current_route_conversation_commit:
    role:
      - "HOT V4.1 後至本次 HOT SAVE 命令前之直接劇情"
      - "玩家對自身言行、追查策略、釋放命令、開幕商業方向與時間軸之明示校正"
      - "NPC 可觀察行動、本人明示、已執行拘押／放行／舞台試光／營運規劃"
      - "多日曹州案中人物供述、顧青簡分析與白御行解讀分軸保存，不把分析升格成客觀真相"

COMMIT_NOTE:
  - "本檔只更新 HOT SAVE；不更新 MASTER、不修改人物卡池、不修改主程序。"
  - "榴月九日為玩家明示鎖定之目前日期；榴月十一日晚為觀止重新開幕之玩家明示鎖定日期。"
  - "HOT V4.1 後曾有導演錯把多日曹州案仍維持在榴月四日之時間污染；該錯誤日期與以此推導出的『籠台仍未完工』回答作廢。"
  - "曹州案內多個中間事件確實跨越多日，但因先前生成的『第二日／第四日』標記互有污染，本 SAVE 不硬填每一事件的精確日序；保留事件順序，鎖定現時榴月九日夜。"
  - "白御行把疑似核心男子稱作『何先生』是玩家命名／判斷；對方曾說『今晚我就當你的何先生』並寫『何先生記／今夜借名』，仍不等於客觀身份確認。"
  - "曹州案供述中的『何先生』『二掌櫃』『帳先生』『回字』『看風』等，有些可能是人名、有些可能是位置／功能／別稱；未被多源證實者不得固化成固定人物。"
  - "玩家對『江湖流傳千年騙術』『這種手法殺不死』『我也能玩』之說法保存為白御行判斷／策略結論，不升格為觀止世界全部歷史之客觀定論。"
  - "多日拘押曾使用隔離、食物限制、強壓審訊等手段；本 SAVE 只記已發生之事件級事實，不保存可操作的傷害流程或生理閾值。"
  - "女子競技全部參賽者均須為成年女性；競技、賞金、賭盤、護衛招募與風月服務必須分軸，不得因在觀止上場即自動取得妓籍、性服務或親密同意。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年榴月九日"
  time: "夜；當日工作已收尾，精確時刻未知"
  primary_location: "觀止青樓"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  player:
    name: "白御行"
    current_position: "觀止內"
    current_state:
      - "已命顧青簡停止自己對曹州假印案的追查投入，全部現有被拘者放行。"
      - "已完成中央鐵籠／顯影舞台首次私下真人試光。"
      - "已與潘金蓮、紅娘等完成女子競技、賭盤、票價、暖場與紅娘壓軸之第一版開幕營運設計。"
      - "已下令收工，眾人進入榴月十一日晚重新開幕前最後準備。"

  guanzhi:
    ordinary_public_business: "CLOSED_UNTIL_LIU11_EVENING_REOPENING"
    reopening_lock: "理火三年榴月十一日晚上"
    current_phase: "FINAL_PREPARATION_WINDOW"
    central_cage_stage: "PHYSICALLY_USABLE_AND_LIGHT_TESTED"
    hongniang_finale_plan: "ACTIVE_OPENING_PLAN"
    women_combat_plan: "ACTIVE_OPENING_PLAN"
    betting_plan: "ACTIVE_OPENING_PLAN"

  direct_resume_point:
    - "下一幕可從榴月十日最後準備、參賽女子送到觀止試場／試燈／排場，或直接推進到榴月十一日重新開幕前開始。"
    - "若沒有重大事件攔截，不得把日期重新跳回榴月四日。"
    - "榴月十一日晚之前，觀止仍未恢復普通公開營業。"
```

---

# 2｜時間軸校正：榴月四日 → 榴月九日

```yaml
TIMELINE_REPAIR:
  event_id: "LIU04-09-TIME-REPAIR"
  status: "GM_CONFIRMED_ROUTE_CORRECTION"

  fixed:
    v4_1_anchor: "榴月四日午後"
    current_anchor: "榴月九日夜"
    reopening_anchor: "榴月十一日晚"

  reconstructed_sequence:
    - "榴月四日午後後：曹州假印案新情報重新進入注意力，江湖懸賞與腳夫反向報信局啟動。"
    - "其後夜間：多線跟蹤、反跟蹤、紙張／舊文書／交通接頭等線索展開。"
    - "翌晨起：同步收網，多人被抓，分押於京師總會等處。"
    - "後續數日：隔離、供述拆解、利益線追問、多人互證／互拆、部分合作人先行釋放，剩餘人物繼續被觀察。"
    - "榴月九日前後：一名約四十歲、履歷過於完整、可能懂帳務且可能與『何先生』描述重合之男子被押至觀止，由白御行親自面談。"
    - "榴月九日夜：白御行停止追查、全員放行；中央籠台試光；女子競技與開幕營運方向完成第一版，收工。"

  precision_rule:
    - "上列為事件順序與最低必要日期框架；榴月五至八各個供述／放人／外部反應的精確日號若未被直接確認，保持 PARTIALLY_UNKNOWN。"
    - "不得用先前導演污染的『仍是榴月四日』覆寫本節。"
```

---

# 3｜曹州假印案：江湖懸賞、反向情報與同步收網

```yaml
CAOZHOU_INTELLIGENCE_ARC:
  event_id: "LIU04-09-E01-CAOZHOU-JIANGHU-INTELLIGENCE"
  status: "COMPLETED_AS_INVESTIGATION_PHASE"

  inherited_case_basis:
    source: "HOT V3.8 及後續有效 HOT"
    confirmed:
      - "曹州假印案原為定陶商會當前 ACTIVE 案之一。"
      - "核心問題為外部有人使用仿冒定陶商會印信／名義，在曹州等處取得貨物或信用，早期損失約百餘兩級。"
    not_rewritten:
      - "本 HOT 不回溯重寫原始立案細節；只記 V4.1 後追加追查。"

  bai_orders:
    - "白御行不走官府主線，改用江湖／商路／牙行／旅店／運輸／典當等渠道收消息。"
    - "一般無用消息亦給一兩跑腿費；有用情報可高額加賞，個案價值由顧青簡判斷。"
    - "一名腳夫曾被對方以五兩收買，要求先把未來消息賣給對方；白御行另給腳夫五兩，命其反向告知對方此事，並向對方開五十兩要價。"
    - "白御行判斷對方可能利用切線／替身／觀察尾巴，要求追線而非只抓第一個接頭人。"

  observable_results:
    - "腳夫向對方接頭者提出五十兩後，接頭者未當場付款，轉而離開尋求後續處理。"
    - "跟蹤線分裂出茶鋪、車馬鋪／馬匹轉手、油坊、舊紙／文書與多個中間傳遞點。"
    - "偵查中發現有人專門觀察『誰在跟蹤』，即反向監看尾巴。"
    - "茶鋪後室取得一份以『可買／不可買／怕事／要避』等分類的名單；定陶商會出現在『要避』。"
    - "『定陶在要避名單』的墨跡早於本次假印事件，顯示至少某一時點曾有人把定陶視為不宜碰觸的對象。"
    - "白御行後命翌晨多點同步收網，要求主要目標活捉。"
    - "茶鋪、車馬相關人員、油坊相關人員等多人被捕；一名反向監視人物在收網前約一個時辰已離開。"
    - "腳夫後續收到匿名訊息：對方不接受五十兩，改以十兩詢問白御行究竟知道多少。"

  unknown:
    - "匿名訊息真正發出者身份未知。"
    - "反向監視離場者的實際身份、去向與是否為高層未知。"
    - "名單製作人、維護人與『要避』狀態何時、由誰被改動，當時仍未知。"
```

---

# 4｜曹州案分押、供述拆解與結構性發現

```yaml
CAOZHOU_INTERROGATION_ARC:
  event_id: "LIU05-09-E02-CAOZHOU-SEPARATION-STRUCTURE"
  status: "COMPLETED_AS_INFORMATION_EXTRACTION_PHASE"

  detention_state:
    - "被捕者被分開拘押，避免互相串供。"
    - "拘押期間曾有高壓、隔離與食物限制；部分願意書寫者後續獲較好飲食、日照、酒食等差別待遇。"
    - "白御行要求審訊者盡量少向被拘者透露既有情報，避免對方從提問反推定陶掌握程度。"
    - "多名書寫者後被集中面對彼此供述矛盾，再次互相拆解；之後又重新分開。"

  information_method_used:
    - "顧青簡逐漸把人名真偽與結構分離，不先相信名字，改看角色、利益、傳遞、授權與斷點。"
    - "白御行提出：假話常可能改寫既有故事，因此可從多人不同版本中抽取共通結構；此為玩家策略假設，不是世界普遍定律。"
    - "白御行又提出：越晚才合作、越能長期撐住的人可能越接近核心；顧青簡僅將其作排序啟發，不視為必然。"

  repeatedly_emerged_structure:
    qualification: "HYPOTHESIS_FROM_MULTIPLE_TESTIMONIES_NOT_FULLY_PROVEN"
    layers:
      - "地方執行層：實際設計／執行某次局或跑具體工作。"
      - "聯絡／傳遞層：紙張、半票、貨物、馬匹等作中介。"
      - "看風／斷點層：確認線路、觀察跟蹤、切斷上下游認知。"
      - "例外授權層：原本不宜碰的對象可被重新打開，某種『回字／回記』代表有人願意背書或允許繼續。"

  return_mark_findings:
    - "多名供述提到：下層把紙送出，原紙或相應紙張返回並帶小記號，才可繼續。"
    - "不同線的記號形狀可能不同，但記號位置可能較固定。"
    - "舊文書中曾被發現同區域出現針點、墨點、折痕或缺口等細小標記；是否全部屬同一授權系統仍未證實。"
    - "一名供述者稱其路線使用兩點；只屬來源自述。"
    - "另有供述指『回字』未必等於上級直接下令，而較像有人願意替這件事背書／開門；實際作法仍由地方層設計。"

  names_and_roles_emerged:
    - "『二掌櫃』：可能是稱呼／位置，是否固定真人未知。"
    - "『何先生』：首次由被拘者口中浮出；可能是人、角色、位置或對外借名。"
    - "『看風』：被描述為各大線可能各有的反監看／確認接頭可信度功能。"
    - "『帳先生』：後由疑似何先生故事中描述為早期把人情、債務、可用人物與切線整理成系統的人；非已確認固定現役人物。"

  evidence_items:
    - "茶鋪『可買／不可買／怕事／要避』分類名單。"
    - "車馬相關人員持有／使用之半票匹配方式；其中一片留存半票曾在其床板下找到。"
    - "多份被拘者書寫供述與互相拆解紀錄。"
    - "關於舊真文書、舊印、簽押／反記購買需求之商路情報。"

  unknown:
    - "曹州假印案具體最終授權者未確認。"
    - "早前所謂『假回記事件』究竟是偽造授權，或真授權後被上層否認，未確認。"
    - "多條線是否屬單一組織、鬆散市場、若干重疊網絡，未獲客觀終局。"
```

---

# 5｜利益線：誰讓參與者覺得值得

```yaml
CAOZHOU_BENEFIT_AXIS:
  event_id: "LIU05-09-E03-BENEFIT-STRUCTURE"
  status: "TESTIMONY_BASED_PARTIAL_MAP"

  confirmed_as_testimony:
    horse_cart_worker:
      - "低階跑腿，報酬以小額現金／短途差事為主，容易替換。"

    tea_shop_man:
      - "利益不是單次佣金；其舊債催收被放慢、供貨／生意路重新恢復，換取偶爾協助紙張轉手。"
      - "供述曾提及約二十餘兩舊債；精確帳實未完成外部核對。"

    oil_shop_man:
      - "供述稱按成功局面分得較高收益，且因曾參與善後而知道較多。"
      - "供述中的具體分成數字不自動視為整個網絡固定薪制。"

    deeper_man:
      - "利益不一定是錢；其過往麻煩曾被人壓下，形成『欠一件事』式不定義人情債。"

  gu_qingjian_working_conclusion:
    qualification: "ANALYTIC"
    text:
      - "與其只追誰下命令，更可追誰有能力真正兌現利益：債務寬限、供應恢復、麻煩壓下、局後分利。"
      - "名字可假、稱呼可換、線可切；利益兌現通常仍需要實際可操作的人／關係。"
```

---

# 6｜先行四人放行：獎勵與外部猜疑

```yaml
EARLY_RELEASE_FOUR:
  event_id: "LIU05-09-E04-FIRST-FOUR-RELEASE"
  status: "COMPLETED"

  bai_order:
    - "對四名已高度合作的被拘者停止繼續扣押。"
    - "清洗、換乾淨衣物。"
    - "每人給一隻燒鵝與二十兩。"
    - "不要求效忠、不簽成定陶內應。"

  observable_external_reactions:
    - "部分原同業見其帶新衣／燒鵝／銀子返回，對『是否說了什麼』產生猜疑。"
    - "有人見茶鋪相關人物後刻意避開。"
    - "油坊相關人物被人追問『把誰寫了』，後續來訪者又離去。"
    - "剩餘被拘者中至少一人因此主動要求紙筆。"

  interpretation_lock:
    - "這些外部猜疑是已觀察到的局部反應，不等於所有網絡成員都已互相崩潰。"
    - "四人獲釋不是秘密招安；其後是否替定陶做事 UNKNOWN。"
```

---

# 7｜疑似核心男子：身份觀察與押抵觀止

```yaml
SUSPECT_CORE_MAN:
  event_id: "LIU09-E05-SUSPECT-TRANSFER-TO-GUANZHI"
  status: "TRANSFER_COMPLETED"

  observable_profile:
    approximate_age: "約四十歲"
    demeanor:
      - "被捕時未劇烈抵抗。"
      - "個人物品與表面身份乾淨，沒有明顯特殊文書／標記。"
      - "對拘押現場其他人數與動靜較少外露反應。"
      - "自稱曾替舊商號做帳／處理帳務。"
      - "履歷時間、地點、人物交代過度完整且一致，引起顧青簡注意，但『完整』本身不是罪證。"
      - "曾在重複身世敘述中一度以較正式年號起句後改口；只屬弱線索。"

  external_description_overlap:
    source: "其他被拘者對『何先生』的描述"
    overlaps:
      - "不常親自跑地方差事。"
      - "不像一般江湖跑腿。"
      - "手乾淨。"
      - "非曹州口音。"
      - "看帳快。"
    ruling: "與該男子有若干重合，只能標記為疑似，不足以確認身份。"

  transfer:
    - "顧青簡依白御行命令把該男子由京師拘押處押至觀止。"
    - "轉移前未提前告知完整目的地。"
    - "該男子在轉移過程聽到『見老闆』後主動猜測是否見白御行；此可由情境推理，不等於其事前掌握觀止內情。"
```

---

# 8｜中央籠台第一次真人試光：疑似何先生作為被拘者

```yaml
CENTRAL_CAGE_FIRST_LIVE_TEST:
  event_id: "LIU09-E06-CAGE-LIGHTTEST"
  status: "COMPLETED"

  hardware_state:
    - "中央鐵籠／顯影舞台於榴月九日已完成至可實際裝人與試光。"
    - "白御行親手推／扳鐵欄測試強度；籠架只出現輕微聲響，未見明顯失穩。"
    - "此前因錯誤日期產生的『仍未完工』回答作廢。"

  use_this_night:
    - "疑似核心男子被置入中央鐵籠，作為私下審談與舞台光測試對象。"
    - "此為一次性非公開使用，不改變紅娘中央籠台原本作為表演／顯影舞台的主要功能。"
    - "籠台不是因此永久改編為定陶刑房。"

  lighting_test:
    setup:
      - "大堂周邊燭火熄滅。"
      - "中央籠台保持集中光源。"
      - "台上人物清楚可見，台下／周邊人物大幅沉入黑暗。"

    adjustments:
      - "第一版光位讓低頭時眉眼過暗、鐵欄影切臉過重。"
      - "紅娘指出上光過直、需補臉與減少鐵欄影破壞。"
      - "第二版調整下補光。"
      - "第三版再降低整體亮度，使籠體不搶人、人物本身成為視覺中心。"

    accepted_effect:
      - "第三版效果獲紅娘與潘金蓮現場肯定。"
      - "可形成『台上被看見、台下看不清』之強顯影效果。"
      - "紅娘要求正式演出時保留第三版亮度／方向作重要基準。"

  hongniang_boundary:
    - "紅娘明示此台正式開幕後是她的壓軸舞台，不接受把它長期當犯人籠。"
    - "本次試光結束後，何先生使用之桌椅、酒食、紙墨等皆被要求撤出／清理。"
```

---

# 9｜白御行 × 疑似何先生：立場、體面待遇與「今夜借名」

```yaml
BAI_HE_CONFRONTATION:
  event_id: "LIU09-E07-OPPONENT-STATUS"
  status: "COMPLETED"

  identity_exchange:
    bai_position:
      - "白御行明示：對自己而言，該男子就是『何先生』；對方否認也不改變白御行的稱呼。"
      - "白御行要求對方在『對手』與『俘虜』兩種談話立場間選擇。"

    suspect_sequence:
      - "起初選『俘虜』，但拒絕把俘虜等同於對一切待遇的同意。"
      - "白御行提出重刑威嚇後，對方改選『對手』。"
      - "對方否認『選對手＝客觀承認自己是何先生』的邏輯必然性。"
      - "其後接受：『今晚我就當你的何先生』。"
      - "他在紙上寫『何先生記』，並補『今夜借名』。"

  identity_ruling:
    objective_identity: "UNKNOWN"
    player_label: "白御行認定／稱呼其為何先生"
    suspect_self_position: "今夜借名；接受談判稱呼，不形成客觀身份自白"
    forbidden_inference:
      - "不得把『今晚當何先生』寫成永久身份確認。"
      - "不得把『對手』身分選擇倒推成真名證據。"

  treatment_after_opponent_choice:
    - "白御行停止把他當一般待審俘虜對待，要求給桌子、靠背椅、筆墨、美酒與美食。"
    - "白希進籠負責少酒即添、磨墨與基本桌邊照料。"
    - "疑似何先生正常進食、飲酒、書寫，並開始以故事方式講其所知結構。"

  violence_boundary_this_scene:
    - "白御行曾下令準備反勾短鞭並以重刑威嚇。"
    - "在鞭刑真正執行前，對方改選『對手』，後續轉入桌談；本次觀止私人面談中未完成該鞭刑。"
```

---

# 10｜「何先生」故事：供述內容與資格

```yaml
HE_STORY_TESTIMONY:
  event_id: "LIU09-E08-HE-STORY"
  status: "TESTIMONY_RECORDED_NOT_OBJECTIVE_CANON"

  written_material:
    - "疑似何先生在觀止中央籠台桌上寫下多頁文字。"
    - "最上方曾寫『何先生記／今夜借名』。"
    - "他離場前沒有帶走這批紙；留在觀止側作本案資料。"

  story_core_as_told:
    - "最早並不存在完整『何先生』『二掌櫃』體制，而是少數做生意走投無路的人以人情、借貸、關係互相救急。"
    - "一開始價值不只在銀兩，而在誰能讓麻煩消失、讓貨重新動、讓債延後、讓某條路重新可走。"
    - "人情債比銀債更難結清，慢慢形成『需要時替我做一件事』的交換。"
    - "其後有人開始主動製造別人的資金、貨路、信用或關係困境，再以合法／表面正常的方式出面解決，從中取得錢與人情。"
    - "再往後，有人不再只想『救局／做局』，而開始『吃局』：讓一個商號失敗後，拆分其貨、路、債、客與位置。"
    - "故事中所稱『帳先生』把可使用人物、使用代價、知情邊界與出事切點整理成更系統的網絡。"
    - "斷點最初可被理解為降低一人出事拖垮整網的風險，後來也使做局更難被一次抓完。"

  dingtao_as_told:
    - "定陶曾被列為『要避』，故事理由包括帳務較乾淨、票據流動快、地方遇到不懂的帳會往上詢問。"
    - "後來有人主張可以試碰定陶，不是要正面吃掉定陶，而是把一筆小局當測試。"
    - "故事稱該決定在有權改『要避』的人之間並非一致，存在上層反對，顯示內部早已有裂縫。"
    - "『何先生』可被當人名、位置、臉或『有人替這件事看過』的外部稱呼；實際制度性質仍未證實。"

  epistemic_status:
    - "以上均是該男子自述／故事，不直接等於客觀歷史。"
    - "他曾明示：會寫真的，也會寫假的。"
    - "顧青簡因此只把內容作結構材料，需與既有證據／多人供述交叉。"
```

---

# 11｜白御行止手：全員放行，曹州案不再佔用本人時間

```yaml
CAOZHOU_STOP_ORDER:
  event_id: "LIU09-E09-RELEASE-ALL-STOP-PURSUIT"
  status: "EXECUTED_AS_ROUTE_DECISION"

  bai_reasoning_as_stated:
    - "白御行判斷目前挖出的核心手法本質上是製造需求／困境、以幫助換錢與人情、再逐步走向直接吃掉失敗者的常見江湖結構。"
    - "白御行認為這類結構不依賴唯一首腦，懂方法的人可反覆重建；與其追求『為民除害』式永久根除，不值得繼續耗費個人生命與會長時間。"
    - "白御行明示自己也理解這套玩法、若要玩亦能玩，但沒有興趣投入。"
    - "其價值排序明示到：寧可把時間花在觀止／紅娘的表演與開幕。"

  order_to_gu_qingjian:
    - "曹州案目前被扣住的人全部放。"
    - "疑似何先生亦放。"
    - "不以認罪、效忠、交換情報作放行附帶條件。"

  execution:
    - "顧青簡下達解除拘押命令。"
    - "觀止內疑似何先生的籠門被打開並准其離開。"
    - "京師總會等處曹州案仍被拘者亦收到同一放行命令；現有這一輪拘押狀態解除。"
    - "疑似何先生離開前把其書寫材料留在觀止。"

  current_case_state:
    bai_personal_pursuit: "STOPPED"
    current_detention_from_this_sweep: "NONE"
    evidence_archive: "RETAINED"
    objective_truth: "UNRESOLVED"
    formal_case_closure_by_association: "NOT_EXPLICITLY_STATED"
    future_reactivation: "POSSIBLE_ONLY_IF_NEW_CAUSE_OR_NEW_ORDER; NOT_CURRENT_PRIORITY"

  important_distinction:
    - "放人不等於認定無罪。"
    - "停止白御行本人追查不等於曹州假印客觀真相已查明。"
    - "顧青簡曾分析放人可能造成外部互疑，但白御行最終理由不是把放人當精密反間局，而是認為繼續投入不值。"
```

---

# 12｜女子競技：項目定位與參賽資格

```yaml
WOMEN_COMBAT_PROGRAM:
  event_id: "LIU09-E10-WOMEN-COMPETITION-DESIGN"
  status: "ACTIVE_OPENING_PLAN"

  category:
    player_definition:
      - "這是『競技／比賽』，不是青樓性服務。"
      - "男人可把觀看女子對打本身當主要娛樂。"
      - "比賽服容易在拉扯中破損是表演／競技視覺設計，不改變參賽者工作性質。"
    route_rule:
      - "參賽不等於妓籍。"
      - "參賽不等於任何性服務、親密或陪客義務。"
      - "良家／自由成年女子亦可參加；不只牙行名下女子。"

  entry_channels:
    yahang_channel:
      - "觀止可向牙行招募其名下成年女性參賽。"
      - "牙行不是唯一渠道。"
      - "即便由牙行提供，實際上場前仍應讓本人聽懂規則並願意上場，以免形成只縮躲／失控傷人的壞表演。"

    free_women_channel:
      - "成年自由女子／良家／寡婦／做工女子等，只要本人願意並符合規則，可自行報名。"
      - "自由參賽者沒有牙行分成，其勝負賞金原則上歸本人。"

  safety_and_match_rules:
    - "參賽者必須成年。"
    - "上場前保持清潔。"
    - "不得留可造成額外抓傷的長指甲；必要時修短。"
    - "不得攜帶硬物。"
    - "比賽服由場方另備，採容易在拉扯中鬆散／破損的設計，不拿日常好衣裳消耗。"
    - "主要允許推、抱、摔、壓制、抓頭髮與拉扯衣物等近身對抗；若實際排練需再由潘金蓮／紅娘依場地控傷。"
    - "勝負基準：一方被壓制在地，連續五秒／現場五聲內無法有效掙脫或反抗，即判負。"
    - "正式裁判人選未完全鎖死；紅娘曾主動表示可數五聲。"

  prize:
    base_prize:
      winner: "十兩"
      loser: "二兩"

    yahang_owned_entrant_split:
      winner:
        yahang: "五兩"
        woman: "五兩"
      loser:
        yahang: "一兩"
        woman: "一兩"

    free_entrant_split:
      winner: "十兩全歸本人"
      loser: "二兩全歸本人"

    anti_withholding:
      - "牙行不得以自身賭輸／表現不滿為由扣掉參賽女子明示屬本人之半份賞金。"
```

---

# 13｜賭盤：潘金蓮營運主權

```yaml
BETTING_PLAN:
  event_id: "LIU09-E11-PAN-BETTING"
  status: "PAN_OPERATIONAL_PLAN_ACCEPTED"

  authority:
    - "白御行明示：這是潘金蓮的生意，不由白御行替她決定每個盤口。"
    - "潘金蓮取得女子競技賭盤之營運裁量。"

  pan_current_plan:
    - "每場參賽者先亮相，讓客人看人／身形／氣勢後再下注。"
    - "開打前封盤。"
    - "第一版只開左右／兩方勝負，不在首夜同時堆疊過多複雜盤口。"
    - "潘金蓮目前傾向由觀止坐莊，而非只做客人互押抽頭。"
    - "第一晚限制風險、先摸清客人偏好與實際強弱差，盤不開太大。"
    - "下注以現銀結算，不收欠單。"
    - "參賽者、提供參賽者的牙行與直接相關觀止工作人員不得碰自己那一場的盤，以減少內部操縱。"

  accounting_separation:
    - "參賽賞金與賭盤盈虧分帳。"
    - "牙行分成與女子個人賞金分帳。"
    - "觀止不得以賭盤輸贏回頭扣參賽女子已取得的個人賞金。"
```

---

# 14｜女子競技作為女性護衛／保鑣人才第一層顯影

```yaml
FEMALE_GUARD_TALENT_PIPELINE:
  event_id: "LIU09-E12-FEMALE-GUARD-SCOUT"
  status: "DESIGN_DIRECTION_CONFIRMED_NOT_YET_RECRUITED"

  idea:
    - "女子競技能讓觀止／定陶實際看到部分成年女子的力量、膽量、受壓反應、摔倒後是否慌亂、近身對抗與收力能力。"
    - "表現出真正實力者可再問本人是否願意接女性護衛／保鑣／押貨／隨車／女眷貼身護送等工作。"
    - "可採雇傭，不要求買下或加入觀止。"

  gu_qingjian_boundary:
    - "擂台打得好不等於會護衛。"
    - "護衛另需測路線判斷、保護雇主撤離、遇到武器／多人／突發狀況時的取捨與紀律。"
    - "因此女子競技只是第一層顯影／招募入口，護衛資格另測。"

  current_state:
    actual_guard_recruits_from_program: "NONE_YET"
    actual_guard_contracts: "NONE_YET"
```

---

# 15｜榴月十一日重新開幕：入場費與座席

```yaml
REOPENING_TICKET_PLAN:
  event_id: "LIU09-E13-REOPEN-TICKETS"
  status: "ACTIVE_FIRST_NIGHT_PLAN"

  reopening_time:
    fixed: "理火三年榴月十一日晚上"

  player_hard_price_floor:
    - "第一晚最低進場費一兩起跳。"
    - "一兩只能在偏角／後排等較差位置。"
    - "二十兩才進入前排層級。"

  pan_extended_tiers:
    one_tael: "偏角／後排／柱邊等；可進場但不保證好視線"
    three_tael: "普通席"
    five_tael: "佳席"
    ten_tael: "中央外圈"
    twenty_tael_and_up: "籠台前席"
    best_front_seats: "二十兩為底，開幕當日可競價"

  interpretation:
    - "進場費只買入場與對應席位資格；酒、菜、賭盤另算。"
    - "第一晚所有入場者原則上都能看到壓軸，但低價席位視線可能受人群影響。"
    - "潘金蓮刻意保留部分一兩票，維持『一兩可進觀止』的外部話題與入口。"

  status_lock:
    - "以上是榴月九日夜收工前已接受的第一版營運方案。"
    - "若榴月十日實際排座發現硬體容量不足，可由潘金蓮作同級調整，但不得把玩家明示的一兩最低／二十兩前排方向靜默改掉。"
```

---

# 16｜第一晚節目節奏：女子競技暖場 → 紅娘壓軸

```yaml
REOPENING_SHOW_FLOW:
  event_id: "LIU09-E14-OPENING-NIGHT-RUNNING-ORDER"
  status: "ACTIVE_FIRST_NIGHT_PLAN"

  first_version:
    - "開門迎客。"
    - "酒食與座席進場。"
    - "女子競技場亮燈，逐場亮相、收盤、封盤、開打、結算。"
    - "潘金蓮曾提出首夜先試三場；此為目前營運計畫，不是不可變更的世界法則。"
    - "女子競技結束後，賭盤與帳務先結清，舞台清場。"
    - "大堂進入短暫全暗／低干擾狀態。"
    - "中央顯影燈重新以紅娘所需版本點亮。"
    - "紅娘正式作當晚壓軸。"

  hongniang_requirements:
    - "紅娘登場後不希望跑堂穿場、持續收賭、算帳或送菜干擾視線。"
    - "競技場的照明應更偏向看清對抗；紅娘壓軸使用全場暗、中央人物顯影的第三版光感。"
    - "女子競技負責把場子燒熱，不與紅娘爭同一種表演法位。"

  business_logic_as_stated:
    - "白御行判斷男人本就想看女人對打，競技能先把每晚場面炒熱。"
    - "潘金蓮／紅娘接受把紅娘放在最後收場，使中央籠台形成每晚高潮。"
```

---

# 17｜榴月九日夜收工後之工作單

```yaml
PRE_REOPEN_WORK_ORDERS:
  event_id: "LIU09-E15-PREP-WORK"
  status: "ORDERED_IN_PROGRESS"

  assigned_or_active:
    - "女子競技參賽者：三十二娘／潘金蓮側對牙行與其他渠道招募合適成年女性；牙行只是第一批來源。"
    - "榴月十日可進行參賽者初看、試籠、試燈、排場與規則說明。"
    - "木工／現場人員再檢查中央鐵籠、固定件、燈架與隔離距離。"
    - "席位重新按價格層級編排。"
    - "廚房按重新開幕備酒菜。"
    - "帳房至少分開入場收入、女子競技賞金、賭盤三類帳。"
    - "護院重走重新開幕當晚人流、舞台與觀眾隔離線。"
    - "紅娘自行熟悉中央籠台正式走位與第三版顯影光。"

  not_yet_completed:
    - "正式第一批女子競技參賽名單尚未固化。"
    - "正式對戰配對尚未固化。"
    - "正式賠率／每場押注上限尚未固化。"
    - "正式護衛招募測試尚未開始。"
    - "榴月十一日晚重新開幕尚未發生。"
```

---

# 18｜人物與關係／知情更新

```yaml
CHARACTER_STATE_UPDATES:
  gu_qingjian:
    observed:
      - "本輪作為曹州案核心師爺，負責情報分類、分押、供述互證、利益結構拆解與放人執行。"
      - "未把白御行的每個人性假設當成定律；多次保留『可能』『只是排序啟發』。"
      - "在白御行命令全放後直接執行，不擅自留人。"
    no_baseline_rewrite:
      - "以上是玩家線事件能力顯影，不自動回寫跨線人物卡永久能力評級。"

  pan_jinlian:
    observed:
      - "接手女子競技作為觀止營運生意，主動設計賭盤、座席、帳務與第一晚節奏。"
      - "白御行明示『這是你的生意，不是我的』，使潘金蓮取得較明確現場營運裁量。"
      - "對參賽女子賞金、牙行分成、比賽／風月服務分軸作出實務規劃。"

  hongniang:
    observed:
      - "中央籠台試光中實際指出光位與亮度問題，第三版光感獲她接受。"
      - "堅持正式表演時中央籠台是她的壓軸舞台，不希望犯人使用變成常態。"
      - "接受女子競技作暖場，自己最後收場；要求自己演出時停止其他場內干擾。"

  bai_xi:
    observed:
      - "依白御行命令進中央鐵籠，給疑似何先生添酒、磨墨。"
      - "面對被拘男子仍維持工作節奏，沒有被安排成審訊者。"

  bai_sanshierniang:
    observed:
      - "參與曹州案部分外勤／放風／後續觀察。"
      - "在開幕準備中承接女子競技招募跑腿方向。"

  suspected_he:
    route_status:
      - "已被釋放。"
      - "對觀止與白御行已有直接面對面經驗。"
      - "接受『今夜何先生』稱呼，但客觀真名／角色仍未知。"
      - "離場後去向、是否回原網絡、是否再與定陶接觸，UNKNOWN。"
```

---

# 19｜V4.1 繼承事項：沒有在本輪被自動補完的舊安排

```yaml
INHERITED_UNRESOLVED_FROM_V4_1:
  principle:
    - "榴月四日後雖已自然推進至榴月九日，但本輪沒有重新演出／確認的例行事項不得因時間經過自動寫成完成。"

  unresolved_or_unobserved:
    - "V4.1 中安排『翌日剪髮』之白御行本人髮型、三名新丫鬟實際剪髮完成結果與售髮款，未在本輪直接演出；狀態為 UNOBSERVED_NOT_RECONFIRMED。"
    - "V4.1 九名新丫鬟的初教、認路、生活磨合可合理已經發生部分日常進程，但本 HOT 未取得具體事件證據，不編造個別成果。"
    - "牙行轉契／身契文書若 V4.1 截止仍有流程性 pending，本輪未特別核卷；不得以本 HOT 靜默宣告全部文書完成。"
    - "趙受益替楊玉環／六條丫鬟付款仍沒有因本輪時間流逝自動形成債務。"
    - "更早紅娘十日門窗換債等既有契約／整修線，除本輪中央籠台完工與開幕準備外，不因本 HOT 自動推定所有細項已結算。"

  future_resolution:
    - "若榴月十日／十一日劇情需要上述狀態，優先用現場可觀察結果補記，而不是假裝榴月五日已被本 HOT 明示演出。"
```

---

# 20｜帳務、契約、案件狀態快速表

```yaml
STATE_TABLE:
  caozhou_case:
    prior_status: "ACTIVE"
    current_bai_priority: "STOPPED"
    current_detainees_from_current_sweep: 0
    evidence: "RETAINED"
    truth: "UNRESOLVED"
    formal_association_close: "NOT_STATED"

  suspected_he:
    detention: "RELEASED"
    objective_identity: "UNKNOWN"
    player_label: "何先生"
    accepted_alias_this_night: true
    written_pages_left_at_guanzhi: true

  central_cage:
    physical_status: "USABLE"
    first_live_light_test: "COMPLETED"
    primary_future_role: "HONGNIANG_CENTRAL_PERFORMANCE_STAGE"
    permanent_jail_conversion: false

  women_competition:
    status: "OPENING_PLAN"
    adult_only: true
    free_women_can_enter: true
    yahang_can_supply: true
    winner_prize: "10 taels"
    loser_prize: "2 taels"
    match_end: "pin for five seconds/counts without effective escape"
    actual_fighters_selected: "NO"

  betting:
    operator: "PAN_JINLIAN / GUANZHI"
    current_model: "HOUSE_BOOK / simple win-loss first"
    actual_opened: false

  reopening:
    date: "LIU11"
    time: "EVENING"
    minimum_entry: "1 tael"
    front_row_floor: "20 taels"
    status: "PREPARING"
```

---

# 21｜本輪反污染與禁止推斷

```yaml
ANTI_CORRUPTION_LOCK:
  time:
    - "目前是榴月九日夜，不是榴月四日。"
    - "重新開幕是榴月十一日晚。"
    - "不得把先前錯誤日期造成的『籠子還沒做好』重新引入。"

  he_identity:
    - "白御行叫他何先生 ≠ 客觀身份確認。"
    - "選擇對手 ≠ 何先生身份證明。"
    - "『今晚我就當你的何先生』『今夜借名』只成立當晚談話定位。"

  testimony:
    - "疑似何先生的故事 ≠ 世界歷史定稿。"
    - "多人供述重疊 ≠ 所有細節均真。"
    - "『帳先生』不得未經證據直接生成一名固定大反派。"

  release:
    - "全部放行 ≠ 全部無罪。"
    - "停止追查 ≠ 曹州案真相已閉合。"
    - "外部互疑是可能／局部已見反應，不得寫成整個網絡自動崩潰。"

  violence:
    - "先前曾有高壓拘押與食物限制，屬路線已發生事件；不得將其生理效果、可承受日數或『一定會說真話』寫成客觀醫學定律。"
    - "觀止對疑似何先生的反勾短鞭威嚇未實際落鞭；不得倒寫成已受十鞭傷勢。"

  women_competition:
    - "競技參賽 ≠ 性服務。"
    - "服裝破損設計 ≠ 永久裸體／親密同意。"
    - "牙行所有權／身契 ≠ 可略過本人上場意願。"
    - "擂台勝利 ≠ 已取得護衛資格。"
    - "尚無首批正式參賽者，不得下一串自動生成冠軍、明星或護衛名單。"

  business:
    - "潘金蓮目前營運計畫可在開幕前按現場容量作實務調整，但不得靜默改掉玩家已明示的一兩最低入場與二十兩前排方向。"
    - "首夜三場是潘金蓮當前計畫，不是不可修改的 GM 永久法則。"
```

---

# 22｜直接接關快速載入

```yaml
DIRECT_RESUME:
  date: "理火三年榴月九日夜 → 下一自然節點榴月十日"
  reopening: "榴月十一日晚"
  location: "觀止青樓"
  world_attention:
    high:
      - "重新開幕最後準備"
      - "女子競技首批參賽者招募／試場"
      - "座席、票價、賭盤與人流"
      - "紅娘中央籠台壓軸排演"
    low_or_paused:
      - "曹州假印案：白御行本人停止追查；證據保留、真相未完"
    inherited_background:
      - "V4.1 九名新丫鬟與五女生活線仍存在"
      - "觀止其他人物與更早契約／關係線均未因曹州案消失"

  current_hard_facts:
    - "曹州本輪所有被拘者已放。"
    - "疑似何先生已放；客觀身份仍未知。"
    - "中央鐵籠可用，第三版舞台光已試成。"
    - "女子競技為成年女子自願競技，可由牙行供人亦可自由報名。"
    - "勝十兩、敗二兩；牙行名下參賽者牙行與本人各半，自由參賽者全歸本人。"
    - "賭盤由潘金蓮作觀止生意操作。"
    - "第一晚最低入場一兩；二十兩起前排。"
    - "女子競技先暖場，紅娘最後壓軸。"
    - "榴月十一日晚重新開幕。"

  next_stop_conditions:
    - "若榴月十日參賽者實際到場，必須讓人物本人顯影，不得只把她們當數值選手。"
    - "若要把競技者轉入護衛線，需另行測試與本人同意。"
    - "若曹州案突然回流，必須有新事件／新代價／新情報，不得因導演捨不得反派而自行把白御行拉回舊追查。"
```

---

# 23｜本 HOT 提交結論

> **V4.2 將白御行線目前時間正式鎖定在「理火三年榴月九日夜」。**
>
> **曹州假印案：白御行本人追查停止；本輪全部拘押者釋放；既有證據保留；真相仍未完成。**
>
> **疑似何先生：只成立「今夜借名」與玩家稱呼，不成立客觀身份確認。**
>
> **中央鐵籠：已可使用並完成第三版顯影光試驗；正式主要功能仍是紅娘中央舞台。**
>
> **女子競技：正式進入開幕營運方案；競技、賭盤、賞金、護衛人才池與性服務分軸。**
>
> **觀止重新開幕：理火三年榴月十一日晚上。**
>
> **下一自然接關：榴月十日最後準備，或經一個自然節點後進入榴月十一日開幕。**
