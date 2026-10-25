# 觀止青樓｜白御行線 MASTER SAVE V4.5-R1
## 截至 HOT V4.5 固化整合版｜HOT V4.6–V5.0 保留為有效疊加層

```yaml
SAVE_META:
  save_id: "GUANZHI_BAIYUXING_MASTER_V4_5_R1_CUTOFF_HOT_V4_5"
  title: "觀止青樓｜白御行線 MASTER SAVE"
  version: "V4.5-R1"
  world: "觀止青樓"
  player: "白御行"
  route_status: "ACTIVE"
  record_type: "CONSOLIDATED_MASTER_ARCHIVE"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  document_date: "2026-08-17"
  fixed_calendar_anchor: "理火三年槐月五日｜永恆第一夜"
  master_cutoff: "理火三年榴月十二日晚｜HOT V4.5"
  last_canonical_master_event: "E103"

  inherited_master:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.4-R1_截至HOT_V4.0固化_保留V4.1-V4.4_HOT版.md"
    sha256: "40c570139367348e3c2b5e623b7baa7c27955bc1cc187d44db53eb8877b82203"
    cutoff: "HOT V4.0"
    inherited_events: "E01-E98"

  promoted_hot_sources:
    HOT_V4_1:
      sha256: "832c2ccae0efecc9904e1f3e611340a97672b12eb22852e81391c1b7105d37cb"
    HOT_V4_2:
      sha256: "a57107b0a8c0569a6b6cc2e11f01a55a95ff1471047d734c438ca79b41dc0969"
    HOT_V4_3:
      sha256: "6ddcd5ef81595077802bd15dd73472ff2b1e3229e554332d1d6fa8c15ccba4ca"
    HOT_V4_4:
      sha256: "574ff09c884bd95a9fadc59bd92a37ed962f3d2db3c765cb3f6766e56ebac9dd"
    HOT_V4_5:
      sha256: "a57ec10947f53a4a0ca916005ed1dadf40a20ed4bf70fdb2cb2c358ebfad776a"

  current_route_resume_source:
    file: "觀止青樓_白御行線_HOT_SAVE_V5.0_榴月十六日下午_紅娘施粥影戲夜_白玉池秘密揭露_六條十日賭約_返白家麗華證詞版.md"
    sha256: "f336e3d2de0250be91260e10a9e90c19696900376829d3fd0490a0322f61edf5"
    date: "理火三年榴月十六日下午"

  current_route_resume_note:
    - "本 MASTER 正式固化至 HOT V4.5。"
    - "HOT V4.6、V4.7、V4.8、V4.9、V5.0 為合法且較新的疊加層。"
    - "實際接關以 HOT V5.0 為最新切片；需要厚細節時依 V4.9→V4.6 回溯。"
    - "較新 HOT 可覆寫本 MASTER 在 HOT V4.5 截止時仍為 PENDING／UNKNOWN／未發生之狀態。"

  absorbs_into_master:
    - "既有 MASTER V4.4-R1 所固化之 E01-E98"
    - "HOT V4.1"
    - "HOT V4.2"
    - "HOT V4.3"
    - "HOT V4.4"
    - "HOT V4.5"

  retained_as_hot_overlay:
    - "HOT V4.6"
    - "HOT V4.7"
    - "HOT V4.8"
    - "HOT V4.9"
    - "HOT V5.0"

  supersedes_as_master:
    - "觀止青樓_白御行線_MASTER_SAVE_V4.4-R1_截至HOT_V4.0固化_保留V4.1-V4.4_HOT版.md"

  world_runtime_document_profile_current: "GUANZHI_QINGLOU_V12.0"
  current_runtime_overlay:
    - "GUANZHI_PATCH_ACTION_BEFORE_EXPLANATION_V0.1-EXP"
    - "理火環境_PATCH_V0.4_EXP_NOT_MERGED"
  character_source_current: "觀止人物卡池_LCAPG_V2.4_楊玉環柳如是薛濤魚玄機正式升格_32人正式版.md"
```

---

# 0｜本次固化決定與推進範圍

```yaml
GM_COMMIT_DECISION:
  user_request: "HOT SAVE，然後把主存檔推進到 V4.5"
  interpretation:
    - "依既有 MASTER 命名規則，『主存檔推進到 V4.5』表示 MASTER 固化截止點推進至 HOT V4.5。"
    - "MASTER 文件版本由 V4.4-R1 順延為 V4.5-R1；不把文件名倒寫成只有 V4.5 而失去 revision 語義。"

  solidify_through: "HOT V4.5"
  preserve_newer_hot_chain: true
  promoted_versions:
    - "HOT V4.1"
    - "HOT V4.2"
    - "HOT V4.3"
    - "HOT V4.4"
    - "HOT V4.5"
  preserved_versions:
    - "HOT V4.6"
    - "HOT V4.7"
    - "HOT V4.8"
    - "HOT V4.9"
    - "HOT V5.0"

  effect:
    - "既有 MASTER V4.4-R1 的 E01-E98 全部繼承。"
    - "V4.1-V4.5 正式升入長期因果層，新增宏事件 E99-E103。"
    - "V4.6-V5.0 不被本次 MASTER 吃掉，繼續保持較新 HOT 法位。"
    - "V4.6-V5.0 中已完成之後續事件不得回灌為 HOT V4.5 截止時已成立。"
```

## 0.1 固化紀律

1. 只固化已發生、可觀察、人物本人明示、正式帳目／文書可核對，或玩家對自身言行與 GM 法位的有效校正。
2. `UNKNOWN`、`PENDING`、`UNDECIDED`、`DISPUTED` 均為合法狀態；不得為了主存檔完整而補完。
3. 事件、感情、成人同意、拒絕、身體反應、契約、付款、妓籍／奴籍、傳聞與人物解讀分軸保存。
4. 玩家線事件不得倒灌人物卡池基線；V2.4 人物卡池只作現行跨線人物來源。
5. V4.6 之後才成立的楊玉環白玉池私密事件、白家正式落地、女客夜、紅娘慈善影戲、六條十日賭約等，均不屬本 MASTER 截止硬狀態。
6. 文件級 Runtime／PATCH 引用不等於宿主底層部署、不可繞過控制或模型修改。

---

# 1｜V4.5-R1 法位與讀取順序

```yaml
INTERNAL_PRECEDENCE_V4_5:
  highest_current_sections:
    - "第2區：V4.1-V4.5 固化映射 E99-E103"
    - "第3區：截至 HOT V4.5 的 MASTER 截止硬狀態"
    - "第4區：人物關係／成人同意／名分覆寫"
    - "第5區：法律／帳務／契約／營運覆寫"
    - "第6區：知情／秘密／傳聞／反污染覆寫"
    - "第7區：截至 HOT V4.5 未決事項"
    - "第8區：MASTER 與 HOT V4.6-V5.0 接關規則"

  inherited_master_body:
    role:
      - "MASTER V4.4-R1 所固化 E01-E98 與其更早長期因果完整繼承。"
    conflict_rule:
      - "若後附歷史來源含『只固化至 HOT V4.0』等舊截止說明，只代表其當時版本；以本檔第0-9區為準。"

  promoted_hot_source_archive:
    role:
      - "HOT V4.1-V4.5 原始全文附於本檔後段，供細節追溯。"
    warning:
      - "各 HOT 內 CURRENT_SCENE／HOLD 只代表當時快照，不得覆寫本 MASTER 的 HOT V4.5 截止與更晚 HOT V4.6-V5.0。"
```

---

# 2｜HOT V4.1–V4.5 固化映射（E99–E103）

```yaml
V4_5_CONSOLIDATION_MANIFEST:
  inherited_events: "E01-E98"
  promoted_macro_events:
    E99: "HOT V4.1｜榴月四日兩牙行二十三名成年候選雙向遴選、九名丫鬟成交分配、制服／自願剪髮方案、白希白明礬初教、十四名落選者吃麵收尾"
    E100: "HOT V4.2｜榴月九日曹州假印案多日追查後止手、疑似何先生今夜借名與材料留存、全員放行、中央籠台試光、女子競技／賭盤／護衛人才入口、榴月十一日開幕流程"
    E101: "HOT V4.3｜榴月十日開幕前夕、辭歲五百萬五年五分定存、師師月事未至孕否未知、商會女人培訓目的鎖、小翠首次完整成人事件、三人同睡收尾"
    E102: "HOT V4.4｜榴月十一日晚重新開幕完成、女子競技與紅娘壓軸、顧三辭歲再會、趙受益二百兩購四契再贈六條／楊玉環、四大金剛＋李清照女客試場、白玉池會員制接受、錦棠同宿"
    E103: "HOT V4.5｜榴月十二日晚白家採購規劃、蘇清十八日商會工拆帳、妓籍終身法位鎖、阿莉婭處女拍賣標的與紅娘雙人場、三十二娘妓籍申請、楊玉環白玉池代言首夜、黑公子×小桃百兩交易與同宿意向"
```

---

# 3｜截至 HOT V4.5 的 MASTER 截止硬狀態

```yaml
MASTER_CUTOFF_HOT_V4_5:
  date: "理火三年榴月十二日晚"
  exact_clock: "UNKNOWN"
  cutoff_scene: "觀止普通客房／小桃房內；今晚50兩成人服務已完成，另50兩為下一次預付，小桃已自願同意留下同宿但尚未推進至天亮"

  guanzhi_operations:
    - "觀止已於榴月十一日晚完成重新開幕第一夜。"
    - "中央籠台／舞台已投入營運；女子競技已實際上場並有賭盤。"
    - "重新開幕座席已顯影：外圍一兩、前排二十兩等分層；酒食與賭盤另算。"
    - "紅娘已完成重新開幕壓軸演出。"
    - "榴月十二日晚白玉池會員／預約制度正式對外啟動；『楊貴妃第一指名』已由楊玉環本人同意並公開掛出。"

  cao_zhou_case:
    - "白御行已於榴月九日明示止手，不再親自持續追查曹州假印案。"
    - "當輪現有拘押者，包括疑似何先生，已收到全員放行命令；放行不等於無罪或真相已查明。"
    - "疑似何先生在中央籠台留下『何先生記／今夜借名』等多頁材料；材料屬其供述／故事，不自動等於客觀歷史。"
    - "『何先生』究竟是人名、位置、借名或制度稱呼仍保留不確定。"

  maid_selection_and_titles:
    - "榴月四日兩家牙行共二十三名成年女性候選進行雙向選擇，最終九人成交：錦棠3、楊玉環2、六條2、李清照1、柳如是1。"
    - "錦棠三人由錦棠側負擔；其成交總價94兩。"
    - "楊玉環2、六條2、李清照1、柳如是1 共六人由白御行側先付，成交總價178兩。"
    - "榴月十一日晚，趙受益以200兩向白御行購得楊玉環2與六條2共四張身契，款項已付。"
    - "趙受益隨後在二女本人願收的前提下，把兩張契轉贈六條、兩張契轉贈楊玉環；二女均已收下。"
    - "李清照、柳如是各一名丫鬟仍按白御行名下、本人使用之既有安排保存，除非較新 HOT 另有覆寫。"
    - "榴月四日制服／三名自願剪髮與售髮方案當時成立；若未有後續完成證據，不在本 MASTER 補寫已執行。"

  cisui_finance:
    - "辭歲五百萬兩、五年、五分定存已簽署生效。"
    - "利息進主動／活期帳戶，不滾入本金。"
    - "簽約後保留流動餘額5,800,000兩。"

  li_shishi:
    - "榴月十二日月事仍未來／較平常晚。"
    - "是否懷孕仍為 UNKNOWN；不得在 HOT V4.5 截止升格為已確診。"
    - "白家新宅／生活採買規劃由李師師牽頭，白御行交1,000兩作訂金／卡貨用途；最終貨款走白御行個人帳，不算商會公務支出。"
    - "錦棠未來住處與白家分法位；可鄰近往來，但不自動納入白家妻妾格局。"

  suqing:
    - "榴月十一日晚蘇清確實碰見一人，但對方身分與是否發生私人成人事件仍 UNKNOWN。"
    - "她明示當夜沒有接觀止安排的客、沒有被點牌、沒有被人付錢包夜。"
    - "原二十八日私約被拆為：商會專案二十日中已有二日預支，榴月十三日起尚餘十八日商會工作；其後仍剩八日私人共同生活。"
    - "十八日商會工範圍包括走秀、內衣／戰鬥肚兜、衛生巾等專案；不等於白御行取得她全部私人生活。"
    - "最後八日共同生活不等於八晚自動性行為。"

  xiaocui:
    - "榴月十日晚，白御行與成年小翠完成一次已成立同意的私人成人事件，錦棠在場。"
    - "當夜事件與後續三人同睡只屬玩家線；不得倒灌小翠跨線永久成人偏好、對所有男人之同意或人物基線。"
    - "榴月十一日晚重新開幕，小翠被目擊與一名男客同桌說話；是否正式接客、進房、成人事件仍 UNKNOWN。"

  reopening_and_guest_trials:
    - "榴月十一日晚女子競技第一夜已實際成立；白御行首筆100兩賭注押冷門較矮一方並勝出，精確淨贏額未固定。"
    - "四大金剛以女客身分進場試場；李清照亦以付費女客身分下場。被搭訕／同桌不等於接客或成人結果。"
    - "李清照當晚未登妓籍。"
    - "柳如是當晚沒有被確認正式掛牌／接客。"
    - "張麗華『酒促姑娘』班底仍只到商業興趣／候選方向，未正式成立。"

  prostitution_registry:
    - "妓籍於官府正式登記完成時成立；一旦成立，法律履歷終身不可回到良家。"
    - "停止接客、退休、改職、經商、買宅等不會洗掉妓籍。"
    - "奴籍與妓籍為獨立法位，可同時存在；奴籍主人不因持身契就自動取得妓女接客／客人分配權。"
    - "白三十二娘截至 HOT V4.5 為妓籍申請已啟動、尚未完成登記。"
    - "白紅伶仍未申請；白明礬、白希目前不入。"

  aliya:
    - "阿莉婭在 HOT V4.5 已校正為早已具妓籍，且處女一次性拍賣標的仍保留。"
    - "榴月十二日晚紅娘×阿莉婭雙人成人舞台已完成；本場沒有消耗阿莉婭處女拍賣標的。"
    - "觀眾對拍賣價格上升之喊價／預期不等於已成交新價格。"
    - "紅娘與阿莉婭成功搭檔不自動建立戀愛或固定女女關係。"

  white_jade_pool:
    - "白玉池高級會員預約制已由潘金蓮接受並於榴月十二日晚啟動。"
    - "公開規則包含夜間四席、每席一時辰、每次兩名成年客人、需預約、不可轉讓、觀止不提供搭伴。"
    - "會員資格／預約押金為50兩；單次實際使用費存在但 HOT V4.5 未留下可核對精確數字。"
    - "楊玉環本人同意『楊貴妃第一指名』公開代言；代言費須另談，不能以她原本白天可用白玉池充抵。"
    - "楊玉環在觀止歇業期近十日持續使用白玉池是已知使用經驗；HOT V4.5 尚未發生後來 V4.6 的白御行×楊玉環白玉池私密成人事件。"

  bai_pan:
    - "白御行與潘金蓮已互相接受未來『一場決勝負』成人私約。"
    - "日期、地點、具體內容與勝負均未固定；此約不等於白御行可隨時啟動。"

  heigongzi_xiaotao:
    - "榴月十二日晚白御行以『黑公子』假稱坐一兩外圍普通席；小桃截至 HOT V4.5 不知道黑公子就是白御行。"
    - "原500兩成人方案在履行前撤銷，小桃退回500兩票；不得記為她已賺500兩或原方案已完成。"
    - "最終當晚成交總值100兩：50兩為當晚明確成人服務且已完成；另50兩為下一次預付，尚未履行。"
    - "小桃另外自願同意留下陪白御行睡到早上；這不是50兩服務內義務。"
    - "HOT V4.5 截止尚未推進到天亮，因此只固化同宿意向，不固化『已睡到早上』。"
```

---

# 4｜人物關係、成人同意與名分覆寫（截至 HOT V4.5）

```yaml
RELATION_CONSENT_OVERRIDES_V4_5:
  jintang_bai:
    - "HOT V4.0 的首次正式約會、私人成人事件、白御行明示喜歡、錦棠相信但未回覆對等戀愛承諾，全部繼承。"
    - "榴月十一日晚二人再次同宿；玩家明示私人內容不記，因此不得補寫該夜是否性交或其他具體行為。"
    - "錦棠若日後對別的男人有興趣可自行選擇並曾表示可先告知白御行；此為當晚關係對話，不是永久開放關係契約。"

  zhao_rokujo_yang:
    - "趙受益購四契再轉贈二女已完成，但禮物不等於愛情、婚姻、排他關係或成人同意。"
    - "HOT V4.0 既有六條／楊玉環追求方向仍有效；後續實際關係變化由較新 HOT 決定。"

  li_qingzhao:
    - "仍非妓籍；榴月十一日晚只是女客試場。"

  four_guards:
    - "奴籍、妓籍意向、實際女客活動分軸。"
    - "白三十二娘自主申請妓籍，不等於白御行替她決定客人或永久成人同意。"
    - "紅伶、三十二娘榴月十二日晚以普通女客身分挑男人之後續結果截至 V4.5 仍 UNKNOWN。"

  xiaotao:
    - "當晚50兩服務之同意只對已談定項目成立；另50兩只形成下一次預付，不自動生成下次同意。"
    - "留下同宿為小桃另行自願決定，不是買斷包夜。"

  aliya:
    - "妓籍與處女拍賣標的可同時存在；妓籍不代表她必須接受所有成人表演或客人。"
    - "紅娘雙人場為一次自願舞台合作，不建立永久性關係。"

  pan_bai:
    - "未來一場決勝負只表示雙方接受該成人挑戰方向；未定日期、未定內容、未形成 blanket consent。"
```

---

# 5｜法律、帳務、契約與營運覆寫

```yaml
LEGAL_ACCOUNTING_OPERATIONS_V4_5:
  maid_transactions:
    HOT_V4_1:
      jintang_three_total: "94兩"
      bai_side_six_total: "178兩"
    HOT_V4_4:
      zhao_purchase_four_contracts: "200兩，已付款"
      gift_result: "六條2契、楊玉環2契，二女本人均願收"

  cisui_deposit:
    principal: "5,000,000兩"
    term: "5年"
    rate: "五分"
    state: "SIGNED_AND_EFFECTIVE"
    remaining_liquid: "5,800,000兩"

  white_home_procurement:
    advance_to_li_shishi: "1,000兩"
    account_owner: "白御行個人帳"
    budget_rule: "買齊與耐用優先；一萬兩不是硬上限"
    house_status_at_cutoff: "規劃／採買階段；白家正式落地屬 HOT V4.7 後續，不得提前"

  suqing_work_contract:
    association_days_remaining_from_liu13: "18日"
    later_private_days: "8日"
    separation: "商會工作、私人共同生活、成人同意三軸分離"

  white_jade:
    membership_deposit: "50兩"
    per_use_fee: "EXACT_AMOUNT_UNKNOWN"
    night_capacity: "四席×每席一時辰×每次兩名成年客人"
    yang_endorsement: "已同意並公開；代言費另談，數字 UNKNOWN"

  xiaotao:
    cancelled_ticket: "500兩票已退回白御行／原方案取消"
    current_total_transferred: "100兩"
    tonight_service: "50兩｜已完成"
    next_time_prepayment: "50兩｜未履行"
    overnight: "另行自願，不包含於50兩服務價"

  prostitution_registry:
    legal_rule: "登記完成即終身妓籍；與奴籍獨立"
    sanshierniang: "APPLICATION_STARTED_NOT_YET_REGISTERED"
    aliya: "ALREADY_REGISTERED"
```

---

# 6｜知情、秘密、傳聞與反污染覆寫

```yaml
KNOWLEDGE_SECRET_ANTI_CORRUPTION_V4_5:
  cao_zhou:
    - "疑似何先生供述／手稿只能按來源保存；不得升格成完整客觀組織真相。"
    - "白御行止手與全員放行是硬事件；『曹州案已徹底破解／根除』不是。"

  suqing_liu11:
    - "蘇清本人知道昨夜碰見了誰與發生什麼；白御行與其他人只得到她選擇性回答。"
    - "中午送水只看到她一人，不證明整夜獨處。"

  xiaotao_identity:
    - "小桃知道黑公子與定陶商會有某種資金關係，但截至 V4.5 不知道其真身為白御行。"
    - "春梅認得白御行並配合不揭破。"

  aliya:
    - "處女拍賣標的仍有效主要依本人明示與觀止商業帳面保存；不得以其他舞台互動自動推翻。"

  registry_correction:
    - "HOT V4.5 對妓籍終身法位之 GM 校正，覆寫先前任何『退休／從良即可恢復良籍』式錯誤生成。"

  no_forward_contamination:
    - "不得把 HOT V4.6 白御行×楊玉環白玉池私密成人事件倒寫進 V4.5。"
    - "不得把 HOT V4.7 白家落地與師師高度疑似有喜倒寫成 V4.5 已完成。"
    - "不得把 HOT V4.8-V5.0 女客夜、薛濤匿名線、紅娘慈善影戲、紅娘知悉楊玉環秘密、六條十日賭約等倒寫進 V4.5。"
```

---

# 7｜截至 HOT V4.5 的未決事項

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

# 8｜MASTER V4.5-R1 與 HOT V4.6–V5.0 接關規則

```yaml
OVERLAY_CHAIN_AFTER_MASTER_V4_5:
  order:
    - "MASTER V4.5-R1｜固化至 HOT V4.5"
    - "HOT V4.6｜榴月十三日晚"
    - "HOT V4.7｜榴月十四日晚"
    - "HOT V4.8｜榴月十五日下午"
    - "HOT V4.9｜榴月十五日晚"
    - "HOT V5.0｜榴月十六日下午"

  rule:
    - "越新的合法 HOT 對同一狀態具有更新法位，但只可更新其實際觸及的軸。"
    - "較新 HOT 沒有提及的 V4.5 已固化硬事件繼續有效。"
    - "較新 HOT 的 UNKNOWN 不得回頭抹除較早已確認事件。"
    - "較新 HOT 的玩家線事件不得倒灌人物卡池基線。"

  current_resume:
    source: "HOT V5.0"
    date: "理火三年榴月十六日下午"
    place: "白家主院"
    scene_summary:
      - "白御行昨夜未返家，睡紅娘房；今晨／近中午先到白玉池，再返回白家。"
      - "張麗華已在白家證實昨夜紅娘慈善影戲競技的外部勝負：白御行先失去支撐／先跪，紅娘險勝。"
      - "此段屬 V5.0 HOT，不屬 V4.5 MASTER 截止硬狀態。"
```

---

# 9｜V4.5-R1 提交結論

```yaml
MASTER_COMMIT_RESULT:
  master_version: "V4.5-R1"
  solidified_through: "HOT V4.5"
  inherited_canonical_events: "E01-E98"
  newly_promoted_events: "E99-E103"
  retained_newer_hot_overlays: "HOT V4.6-V5.0"
  current_resume_source: "HOT V5.0"
  status: "COMMITTED"
```

> **一句話：主存檔現在正式固化到榴月十二日晚 HOT V4.5；榴月十三日至十六日下午的事件全部留在 V4.6–V5.0 較新 HOT 疊加鏈。**

---

# 10｜歷史固化來源封存區

> 下方全文封存上一版 MASTER V4.4-R1 與本次升格的 HOT V4.1–V4.5，僅供細節追溯。  
> 其中各文件自己的舊 CURRENT_SCENE、MASTER 截止與版本說明均是歷史快照；發生衝突時，以本檔第0–9區為準。



<!-- BEGIN INHERITED MASTER V4.4-R1 FULL ARCHIVE -->

# 觀止青樓｜白御行線 MASTER SAVE V4.4-R1
## 截至 HOT V4.0 固化整合版｜HOT V4.1–V4.4 保留為有效疊加層

```yaml
SAVE_META:
  save_id: "GUANZHI_BAIYUXING_MASTER_V4_4_R1_CUTOFF_HOT_V4_0"
  title: "觀止青樓｜白御行線 MASTER SAVE"
  version: "V4.4-R1"
  world: "觀止青樓"
  player: "白御行"
  route_status: "ACTIVE"
  record_type: "CONSOLIDATED_MASTER_ARCHIVE"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  document_date: "2026-08-15"
  fixed_calendar_anchor: "理火三年槐月五日｜永恆第一夜"
  master_cutoff: "理火三年榴月三日深夜｜HOT V4.0"
  last_canonical_master_event: "E98"

  inherited_master:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md"
    sha256: "0149362b4128d62d947d4ffbcc618003913b1cad7052d57fe5b3f84f8f05084f"
    cutoff: "HOT V3.4"
    inherited_events: "E01-E92"

  current_route_resume_source:
    file: "觀止青樓_白御行線_HOT_SAVE_V4.4_榴月十二日白日_重新開幕夜結_趙受益四契轉贈_四金剛女客試場_白玉池會員制_錦棠同宿版.md"
    sha256: "574ff09c884bd95a9fadc59bd92a37ed962f3d2db3c765cb3f6766e56ebac9dd"
    date: "理火三年榴月十二日白日"

  current_route_resume_note:
    - "本 MASTER 正式固化至 HOT V4.0。"
    - "HOT V4.1、V4.2、V4.3、V4.4 為合法且較新的疊加層。"
    - "實際接關以 HOT V4.4 為最新切片；需要厚細節時依 V4.3、V4.2、V4.1 回溯。"

  absorbs_into_master:
    - "HOT V3.5"
    - "HOT V3.6-R2"
    - "HOT V3.7"
    - "HOT V3.8"
    - "HOT V3.9"
    - "HOT V4.0"

  retained_as_hot_overlay:
    - "HOT V4.1"
    - "HOT V4.2"
    - "HOT V4.3"
    - "HOT V4.4"

  superseded_revision:
    - "HOT V3.6"
    - "HOT V3.6-R1"
    replacement: "HOT V3.6-R2"

  supersedes_as_master:
    - "觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md"

  world_runtime_document_profile_current: "GUANZHI_QINGLOU_V12.0"
  character_source_current: "觀止人物卡池_LCAPG_V2.3_李清照趙受益錦棠顧青簡增補_薛濤魚玄機暫定入場_正式版.md"
```

---

# 0｜本次固化決定與推進範圍

```yaml
GM_COMMIT_DECISION:
  user_request: "HOT SAVE；同時把目前的主存檔推進到 V4.0"
  interpretation:
    - "『主存檔推進到 V4.0』依既有 MASTER 命名規則解讀為：固化截止點推進至 HOT V4.0。"
    - "MASTER 文件本身版本順延為 V4.4-R1，不倒退命名成 MASTER V4.0。"

  solidify_through: "HOT V4.0"
  preserve_newer_hot_chain: true
  promoted_versions:
    - "HOT V3.5"
    - "HOT V3.6-R2"
    - "HOT V3.7"
    - "HOT V3.8"
    - "HOT V3.9"
    - "HOT V4.0"
  preserved_versions:
    - "HOT V4.1"
    - "HOT V4.2"
    - "HOT V4.3"
    - "HOT V4.4"

  effect:
    - "既有 MASTER V4.3-R1 的 E01–E92 全部繼承。"
    - "V3.5–V4.0 正式升入長期因果層，新增宏事件 E93–E98。"
    - "V4.1–V4.4 不被本次 MASTER 吃掉，繼續保留最新疊加法位。"
    - "較新 HOT 可合法覆寫 V4.0 截止時的 pending／unknown／未執行狀態。"
```

---

# 1｜V4.4-R1 法位與讀取順序

```yaml
INTERNAL_PRECEDENCE_V4_4:
  highest_current_sections:
    - "第2區：V3.5–V4.0 固化映射 E93–E98"
    - "第3區：截至 HOT V4.0 的 MASTER 截止硬狀態"
    - "第4區：截至 HOT V4.0 的人物關係／同意／名分覆寫"
    - "第5區：截至 HOT V4.0 的法律／帳務／契約／營運覆寫"
    - "第6區：截至 HOT V4.0 的知情／傳聞／秘密／反污染覆寫"
    - "第7區：截至 HOT V4.0 的未決事項"
    - "第8區：MASTER 與 HOT V4.1–V4.4 接關規則"

  inherited_master_body:
    role:
      - "MASTER V4.3-R1 所固化 E01–E92 與更早長期因果完整繼承。"
    conflict_rule:
      - "若下方繼承之舊 MASTER 內容含『只固化至 HOT V3.4』等舊截止說明，均視為歷史標記；以本檔第0–9區為準。"

  promoted_hot_source_archive:
    role:
      - "HOT V3.5–V4.0 原始全文附於本檔後段，供細節追溯。"
    warning:
      - "各 HOT 內的 CURRENT_SCENE／HOLD 只代表當時快照，不得覆寫本 MASTER 的 V4.0 截止或更晚 HOT V4.1–V4.4。"
```

## 1.1 固化原則

1. 只固化已發生、可觀察、人物本人明示、正式帳目／文書可核對，或玩家對自身言行與 GM 法位的有效校正。
2. `UNKNOWN`、`PENDING`、`UNDECIDED`、`DISPUTED` 均為合法狀態，不補完。
3. 成人事件、身體反應、同意、關係、付款、妓籍／奴籍、出閣、傳聞分軸保存。
4. 玩家線事件不得倒灌人物卡池基線。
5. HOT V3.6、V3.6-R1 已被 V3.6-R2 取代；只作審計來源，不得再作有效接關。
6. 文件整合不宣稱宿主底層 Runtime、模型權重或不可繞過控制已部署。

---

# 2｜HOT V3.5–V4.0 固化映射（E93–E98）

```yaml
V4_4_CONSOLIDATION_MANIFEST:
  inherited_events: "E01-E92"
  promoted_macro_events:
    E93: "HOT V3.5｜九幽帝皇聯誼會散場、辭歲／錦棠雙姝天價競拍、白玉池帝皇團特殊試營運、帝皇多線自然分流"
    E94: "HOT V3.6-R2｜榴月一日十日整修起點、雙姝款項／身份翻轉、朱明欠單與鄭成功週轉僅預案、六條／趙受益成人結果與污染校正"
    E95: "HOT V3.7｜辭歲／錦棠／李瓶兒私人開戶、紅袖五十萬反向價格尺與召喚權、紅娘門窗屏風換債、趙受益六條夜集外出"
    E96: "HOT V3.8｜趙受益六條夜集返樓、楊玉環白玉池與荔枝、李師師晨間補考、定陶票據信用／朱明長債方向／曹州案盤點"
    E97: "HOT V3.9｜長恨歌文會、柳如是東林夜談、趙受益宣和地道入席、六條／楊玉環雙線追求與三人約會可能性"
    E98: "HOT V4.0｜三十二娘街行與帳戶指令、紅娘中央籠台演出方案、錦棠首次正式約會、私人成人事件、白御行喜歡明示與相擁收幕"
```

---

# 3｜截至 HOT V4.0 的 MASTER 截止硬狀態

```yaml
MASTER_CUTOFF_V4_0:
  date: "理火三年榴月三日深夜"

  guanzhi:
    - "帝皇聯誼會已結束。"
    - "觀止已進入十日對外暫歇／整修期，目標為十日後重新開業。"
    - "白玉池已由帝皇團特殊試營運走向正式化方向，但 V4.0 截止尚未形成後來 V4.4 的會員制。"
    - "紅娘四面可視中央籠台／升降台／燈光／退場通道概念已接入裝修方案。"

  dingtao:
    - "定陶商會票據／信用與朱明應收線已進入可用信用安排；不得把外部應收直接誤寫成客戶端資金不可用。"
    - "朱明短債若來不及可談轉年息十分長債；截至 V4.0 未記為朱家已正式接受。"
    - "京師女性貼身衣物／奢侈品旗艦專案交常煒副會長執行。"

  cao_zhou:
    - "截至 V4.0 曹州假印案仍為定陶當前 ACTIVE 案；後續 V4.2 已形成較新覆寫，必須以 HOT overlay 讀取。"

  jintang:
    - "已完成首次正式私人約會。"
    - "錦棠自行以本人資金購衣；白御行支付望河樓晚餐。"
    - "二人已完成一次私人成人親密／性交事件。"
    - "白御行已明示喜歡錦棠；錦棠表示相信這份喜歡，但未回覆對等戀愛承諾。"
    - "本夜未成立體內射精。"
    - "V4.0 收幕時二人相擁。"

  rokujo_zhao_yang:
    - "趙受益對六條、楊玉環皆有興趣。"
    - "六條與楊玉環均允許趙受益追求方向；三人約會可能性被明示開放。"
    - "尚未因此形成三人戀愛、性交、婚姻或排他承諾。"
```

---

# 4｜截至 HOT V4.0 的人物關係／同意／名分覆寫

```yaml
RELATION_CONSENT_OVERRIDES_V4_0:
  jintang_bai:
    - "首次正式私人約會與成人事件已成立。"
    - "成人事件中的逐步開放、拒絕、重新開放與收束只對當夜成立，不是 blanket consent。"
    - "白御行喜歡錦棠為玩家本人明示。"
    - "錦棠只明示相信白御行的喜歡，未明示『我也愛你』或等價承諾。"

  rokujo_zhao:
    - "V3.6-R2 依 GM 校正固化：帝皇聯誼會前夜，六條與趙受益雙方自願性行為已成立。"
    - "先前以通用成熟／自主哲學改寫事件的污染輸出不取得人物事實權。"
    - "後續 V3.7 夜集、V3.8 回樓不自動新增戀愛或成人結果。"

  yang_zhao:
    - "V3.9 開放追求與約會可能，不建立成人結果。"

  hongxiu_bai:
    - "紅袖『五十萬』為特殊一夜的認真考慮／坐下談門檻與反向價格尺，不是已成交性價。"
    - "紅袖持有一次召喚權；來源為十日主動找人賭局中白御行提前認輸。"

  li_shishi:
    - "舊賭局彩頭未被白御行接受事後重寫；原債務不得任意再造新版條款。"
```

---

# 5｜截至 HOT V4.0 的法律／帳務／契約／營運覆寫

```yaml
LEGAL_ACCOUNTING_OPERATIONS_V4_0:
  auction:
    - "辭歲與錦棠雙姝競拍成交、分成與外部清算鏈已成立；客戶端餘額與商會外部應收分軸。"
    - "不得把外部付款人欠商會的錢，誤寫成辭歲／錦棠本人『沒有錢可用』。"

  private_accounts:
    - "榴月一日辭歲、錦棠、李瓶兒已進入私人開戶／資產安排線。"
    - "V3.7 的顧問與開戶結果以各自原 HOT 細節為準。"

  pan_suqing_50000:
    - "潘金蓮×蘇清五萬兩民事線於 V3.7 補正為『初步和解成立』。"
    - "截至 V4.0 仍不得由此自動推導五萬兩已全額實付。"

  redniang_room_debt:
    - "紅娘原第二局側賭三人親密局債務已由本人同意換約為門／窗拆除十日，屏風另送保養十日。"
    - "原三人局債務已清，不得再追回。"

  four_women_accounts:
    - "V4.0 已下達白三十二娘、白希、白明礬、白紅伶個人商會帳戶與每月十兩方向指令；具體執行狀態依 V4.0 原檔，未完成者不得補完。"

  white_jade:
    - "V3.5 白玉池只屬帝皇團封場特殊試營運。"
    - "V3.8 楊玉環受邀使用白玉池並實際與該空間形成使用關係。"
    - "截至 V4.0 尚未固化後來的會員制、四組時段、五十兩會員押金等；那些屬 HOT V4.4 疊加層。"
```

---

# 6｜截至 HOT V4.0 的知情／傳聞／反污染覆寫

```yaml
KNOWLEDGE_AND_ANTI_CORRUPTION_V4_0:
  calendar:
    - "觀止曆法13月、每月28日；槐月二十八日為月末，無二十九日。"

  gossips:
    - "八卦、假價、假戰報、雙關與玩家故意製造之可信傳聞，均不得當作硬事件。"

  history_testimony:
    - "V3.9 大量後世詩文、人物與政治史來自白御行轉述；誰聽見才取得相應知情。"
    - "玩家轉述 != 觀止世界唯一客觀史。"

  six_zhao_corruption:
    - "曾把六條／趙受益成人事件問題改寫成制度化成熟語氣之輸出，已標為污染，不得倒灌人物人格。"

  guanzhi_runtime:
    - "V4.0 使用 V12、ACTION BEFORE EXPLANATION、環境 PATCH、成人心法等文件作生成參照；文件存在不等於宿主底層已部署。"
```

---

# 7｜截至 HOT V4.0 的未決事項

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

# 8｜MASTER 與 HOT V4.1–V4.4 接關規則

```yaml
ACTIVE_HOT_OVERLAY_V4_4:
  direct_resume_file: "觀止青樓_白御行線_HOT_SAVE_V4.4_榴月十二日白日_重新開幕夜結_趙受益四契轉贈_四金剛女客試場_白玉池會員制_錦棠同宿版.md"
  direct_resume_sha256: "574ff09c884bd95a9fadc59bd92a37ed962f3d2db3c765cb3f6766e56ebac9dd"

  unmerged_but_valid_chain:
    - "HOT V4.1｜榴月四日午後九人丫鬟遴選、牙行成交與分教"
    - "HOT V4.2｜榴月九日夜曹州假印追查止手、何先生放行、中央籠台試光、女子競技與開幕準備"
    - "HOT V4.3｜榴月十日深夜開幕前夕、商會女人培訓目的鎖、小翠首次完整行房與三人同睡"
    - "HOT V4.4｜榴月十一日晚重新開幕至榴月十二日白日，趙受益四契轉贈、四大金剛／李清照女客試場、白玉池會員制、錦棠同宿"

  overlay_hashes:
    HOT_V4_1: "832c2ccae0efecc9904e1f3e611340a97672b12eb22852e81391c1b7105d37cb"
    HOT_V4_2: "a57107b0a8c0569a6b6cc2e11f01a55a95ff1471047d734c438ca79b41dc0969"
    HOT_V4_3: "6ddcd5ef81595077802bd15dd73472ff2b1e3229e554332d1d6fa8c15ccba4ca"
    HOT_V4_4: "574ff09c884bd95a9fadc59bd92a37ed962f3d2db3c765cb3f6766e56ebac9dd"

  load_order:
    - "先讀本 MASTER V4.4-R1，取得 E01–E98 長期因果與 HOT V4.0 截止硬狀態。"
    - "再讀 HOT V4.4，取得最新場景與 V4.1–V4.4 已繼承之較新狀態。"
    - "若 V4.4 摘要不足，再依 V4.3 → V4.2 → V4.1 回溯。"

  precedence:
    - "V4.1–V4.4 對 MASTER V4.0 截止時的 pending／unknown／未執行可形成合法後續覆寫。"
    - "不得用 MASTER V4.0 截止快照反向蓋掉後續 HOT 已成立結果。"

  latest_resume:
    - "理火三年榴月十二日白日。"
    - "榴月十一日晚重新開幕第一夜已結束。"
    - "白御行與錦棠昨夜同宿，私人內容不記。"
    - "白玉池會員制預定榴月十二日晚啟用；首批名單尚未成立。"
```

---

# 9｜V4.4-R1 固化結論

> **E01–E92：完整繼承 MASTER V4.3-R1。**  
> **E93–E98：由 HOT V3.5–V4.0 正式升入 MASTER。**  
> **MASTER 截止：理火三年榴月三日深夜／HOT V4.0。**  
> **HOT V4.1–V4.4：合法較新疊加層，不併入本次 MASTER。**  
> **最新實際接關：HOT V4.4／理火三年榴月十二日白日。**

---

# APPENDIX A｜繼承之 MASTER V4.3-R1 全文

> **法位：E01–E92 與更早長期因果之完整來源。**  
> 下方舊檔內所有「只固化至 HOT V3.4」「V3.5–V3.7 未合併」等文字，僅作歷史版本標記；本檔現行截止與接關法位以第0–9區為準。

<!-- INHERITED_MASTER_V4_3_R1_BEGIN -->

# 觀止青樓｜白御行線 MASTER SAVE V4.3-R1
## 截至 HOT V3.4 固化整合版｜HOT V3.5–V3.7 保留為有效疊加層

```yaml
SAVE_META:
  save_id: GUANZHI_BAIYUXING_MASTER_V4_3_R1_CUTOFF_HOT_V3_4
  title: 觀止青樓｜白御行線 MASTER SAVE
  version: V4.3-R1
  world: 觀止青樓
  player: 白御行
  route_status: ACTIVE
  record_type: CONSOLIDATED_MASTER_ARCHIVE
  format_runtime: GUANZHI_SAVE_RUNTIME_V1_0
  document_date: '2026-08-11'
  fixed_calendar_anchor: 理火三年槐月五日｜永恆第一夜
  master_cutoff: 理火三年槐月二十六日深夜｜HOT V3.4
  last_canonical_master_event: E92
  inherited_master: 觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md
  inherited_master_sha256: 9000d757cd525bf05d9c0b0d9dba454d9c245a2048d780d3b6da3a11a25b2e8b
  current_route_resume_source: 觀止青樓_白御行線_HOT_SAVE_V3.7_榴月一日夜_辭錦瓶兒開戶_紅袖五十萬尺與召喚權_夜宵問答_紅娘門窗十日換債版.md
  current_route_resume_note: 本 MASTER 正式固化至 HOT V3.4；HOT V3.5、V3.6-R2、V3.7 為合法且較新的疊加層。實際接關以 V3.7 為最新切片；需要厚細節時依 V3.6-R2、V3.5
    回溯。V3.6-R1 已被 R2 取代。
  absorbs_into_master:
  - HOT V2.6
  - HOT V2.7
  - HOT V2.8
  - HOT V2.9
  - HOT V3.0
  - HOT V3.1
  - HOT V3.2
  - HOT V3.3
  - HOT V3.4
  retained_as_hot_overlay:
  - HOT V3.5
  - HOT V3.6-R2
  - HOT V3.7
  supersedes_as_master:
  - 觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md
  world_runtime_document_profile_current: GUANZHI_QINGLOU_V11.0-R2
  character_source_current: 觀止人物卡池_LCAPG_V2.2_辭歲入觀止動機校正_青禾六條增補_正式版.md
```

# 0｜本次固化決定與推進範圍

```yaml
GM_COMMIT_DECISION:
  solidify_through: HOT V3.4
  preserve_newer_hot_chain: true
  preserved_versions:
  - HOT V3.5
  - HOT V3.6-R2
  - HOT V3.7
  superseded_revision: HOT V3.6-R1 → HOT V3.6-R2
  interpretation:
  - MASTER V4.2-R1 已固化 E01–E83／HOT V2.5；本版承接該長期因果。
  - HOT V2.6–V3.4 正式升入 MASTER 長期因果層，新增宏事件 E84–E92。
  - HOT V3.5–V3.7 不併入本次 MASTER，繼續作為較新的合法 HOT 疊加層。
  - 後續 HOT 對 V3.4 截止時的 pending／unknown／未執行狀態可形成合法覆寫；不得反向用 V3.4 舊快照蓋掉 V3.7。
```

本版不刪除被固化之原 HOT；V2.6–V3.4 保留作來源追溯與回歸核對。預設長期載入由本 MASTER 取代逐檔載入需求；實際最新接關仍疊加 V3.7。

---

# 1｜V4.3-R1 法位與讀取順序

```yaml
INTERNAL_PRECEDENCE_V4_3:
  highest_current_sections:
  - 第2區：V2.6–V3.4 固化映射
  - 第3區：截至 V3.4 MASTER 截止硬狀態
  - 第4區：截至 V3.4 關係／同意／名分覆寫
  - 第5區：截至 V3.4 法律／帳務／契約／營運覆寫
  - 第6區：截至 V3.4 知情／傳聞／秘密／反污染覆寫
  - 第7區：截至 V3.4 未決事項
  - 第8區：MASTER 與 HOT V3.5–V3.7 接關規則
  inherited_master_body:
    role: E01–E83 與截至 HOT V2.5 的長期因果完整繼承
    conflict_rule: 若 V4.2-R1 內舊截止快照與本版第2–8區衝突，以本版第2–8區為準。
  promoted_hot_source_archive:
    role: V2.6–V3.4 原始 HOT 全文附錄，用於細節追溯
    current_scene_warning: 附錄內各 HOT 的 CURRENT_SCENE／HOLD 只是歷史快照，不得覆寫本版 V3.4 截止或更晚 HOT 疊加狀態。
```
## 1.1 固化原則

1. 只固化已發生、可觀察、人物明示、正式文書可見、帳目可核對，或玩家對自身言行的有效校正。
2. 傳聞、人物判斷、官府推論、玩家分析與客觀事實分軸保存。
3. 成人事件、同意、身體反應、關係、賭約、付款、名分與公開知情分軸保存。
4. `UNKNOWN`、`UNDECIDED`、`DISPUTED`、`PENDING` 都是合法狀態。
5. V2.6–V3.4 玩家線事件不倒灌人物卡池基線；人物池 V2.2 的較新基線校正優先於 V3.1 的待修舊敘述。
6. HOT V3.5–V3.7 的後續結果不得回溯改寫 V3.4 當時事件原貌，但可合法覆寫當時 pending／unknown 的後續狀態。
7. 本版為文件級 SAVE 整合，不宣稱宿主底層 Runtime 或模型權重被修改。

---

# 2｜HOT V2.6–V3.4 固化映射（E84–E92）

```yaml
V4_3_CONSOLIDATION_MANIFEST:
  inherited_events: E01-E83
  promoted_macro_events:
    E84: HOT V2.6｜京師軍械案鏡頭收網、觀止民事戰重啟、許慎言七十二小時按摩券
    E85: HOT V2.7｜潘金蓮返樓、五千原款重分類、五萬索賠、身籍與重新掛牌條件式討論
    E86: HOT V2.8｜潘身籍副冊補證、白玉池許願幣／定存框架、師師道歉修復與如夫人再確認
    E87: HOT V2.9｜曹州假印立案、定陶總會架構、京師女性時尚企畫、師師抱睡
    E88: HOT V3.0｜女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限
    E89: HOT V3.1｜風滿樓第二日遴選、十一名候選分流、牙行責任、白宅十年條件式協議
    E90: HOT V3.2｜小翠同床純睡、三月集訓與走秀換約、六百兩候選條款、白宅設計啟動
    E91: HOT V3.3｜浮香自願給床與成人夜、紅娘煙幕揭穿、九幽帝皇聯誼會正式訂單
    E92: HOT V3.4｜帝皇宴前置、十三娘國運賭桌線、兩局免費床結算、紅娘側賭敗、小翠三娘實習與三人抱睡
  event_id_policy:
  - E84–E92 是 MASTER 宏事件索引。
  - HOT 內原生事件 ID 完整保留為 source_alias，不強行改號。
  - 細節衝突以對應 HOT 的較新修正與本版覆寫為準。
```
## E84｜京師軍械案鏡頭收網、觀止民事戰重啟、許慎言七十二小時按摩券

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

## E85｜潘金蓮返樓、五千原款重分類、五萬索賠、身籍與重新掛牌條件式討論

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

## E86｜潘身籍副冊補證、白玉池許願幣／定存框架、師師道歉修復與如夫人再確認

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

## E87｜曹州假印立案、定陶總會架構、京師女性時尚企畫、師師抱睡

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

## E88｜女性注意力事業秘密模型、風滿樓大型遴選、白家四女、雙夫人內部權限

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

## E89｜風滿樓第二日遴選、十一名候選分流、牙行責任、白宅十年條件式協議

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

## E90｜小翠同床純睡、三月集訓與走秀換約、六百兩候選條款、白宅設計啟動

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

## E91｜浮香自願給床與成人夜、紅娘煙幕揭穿、九幽帝皇聯誼會正式訂單

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

## E92｜帝皇宴前置、十三娘國運賭桌線、兩局免費床結算、紅娘側賭敗、小翠三娘實習與三人抱睡

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

# 3｜截至 HOT V3.4 MASTER 截止硬狀態

```yaml
MASTER_CUTOFF_STATE_V4_3:
  story_time: 理火三年槐月二十六日深夜
  location: 觀止青樓／白三娘私人房／白三娘的床
  last_canonical_master_event: E92
  scene_state: THREE_PERSON_QUIET_SLEEP_AFTER_SECOND_FREE_BED_WIN_AND_XIAOCUI_LIMITED_APPRENTICESHIP
  player:
    name: 白御行
    location: 白三娘床上
    state:
    - 已停止教學與成人互動
    - 正抱著小翠入睡
    action_after_cutoff: NONE_IN_MASTER; SEE HOT V3.5-V3.7
  xiaocui:
    location: 白御行懷中
    state:
    - 今晚有限實習已由她自行停止
    - 接受抱睡並逐漸入睡
    - 不得推定全面性同意或已治癒
  bai_sanniang:
    location: 白御行身後
    state:
    - 當夜成年人互動已停止
    - 抱著白御行入睡
  immediate_world:
  - 帝皇聯誼會三日後大觀樓訂單仍在籌備。
  - 潘金蓮尚未回報完整籌備方案與最高核銷額。
  - 白宅、白玉池、蘇清民事線、新人三月訓練等仍平行活躍。
```

---

# 4｜截至 HOT V3.4 關係、同意與名分覆寫

```yaml
RELATIONSHIP_AND_CONSENT_OVERRIDE_AT_V3_4:
  bai_li_shishi:
    state: ACTIVE_PRIVATE_INTIMACY_AND_ORAL_RU_FUREN_FRAME
    confirmed:
    - 李師師已原諒先前邊界事件，但不抹除。
    - 李師師明示想要如夫人位置，仍未公開／登記。
    - 浮香第一局與白三娘／小翠第二局免費床均由師師正式認輸。
    - 截至 V3.4，V3.2 原賭約中的「可指定李師師做一件她本人可以自願答應之事」尚未在 MASTER 截止前完成兌現。
    not_automatic:
    - 婚姻法定完成
    - 永久排他
    - 任何未來成人行為 blanket 同意
  bai_zhang_lihua:
    confirmed:
    - 四名白家持契女性稱她「麗華夫人」並可處理日常小事。
    boundary:
    - 不是白夫人，也不因此取得法律妻妾／無限白家決策權。
  bai_li_pinger:
    state: ACTIVE_CONDITIONAL_FUTURE_HOUSEHOLD
    confirmed:
    - 白御行曾允諾待她與西門慶身分問題乾淨後，若她仍願意可談如夫人。
    not_confirmed:
    - 李瓶兒已正式入白家
    - 已與李師師完成並列名分
  bai_fuxiang:
    confirmed:
    - 浮香自主免費給床。
    - 白御行與浮香完成成年人親密並同床過夜。
    unresolved:
    - 愛情
    - 長期專屬
    - 白宅固定入住
    - 夫人／妾室名分
  bai_xiaocui:
    confirmed:
    - 已有兩次可核對的安全同床／抱睡經驗：小翠自己房與白三娘房。
    - 第二次由小翠公開主動把白御行帶上樓，並自主進入有限實習後自行停止。
    unresolved:
    - 對白御行感情
    - 對一般客人的服務意願
    - 對性與男性的長期恐懼／厭惡如何變化
  bai_hongniang:
    confirmed_at_cutoff:
    - 紅娘免費床煙幕是假傳聞，白御行沒有在那晚去她房或接受她的免費全套。
    - 紅娘於第二局側賭敗北。
    pending_at_cutoff:
    - 一次免費、與李師師搭成含白御行之三人親密賭債；執行仍需兩名女性當下願意。
  bai_shisanniang:
    confirmed:
    - 豹子賭局白御行敗並已交付國運／幸運路徑情報。
    not_established:
    - 十三娘輸床
    - 十三娘輸成人賭注
  rokujo_zhao_shouyi:
    cutoff_state: V3.4 尚未由本 MASTER 固化任何後續成人結果；更晚狀態須讀 HOT V3.5–V3.7，不得從後續倒寫進 V3.4 截止。
```

---

# 5｜截至 HOT V3.4 法律、帳務、契約與營運覆寫

```yaml
LEGAL_ACCOUNTING_OPERATION_OVERRIDE_AT_V3_4:
  su_qing_vs_pan:
    status: ACTIVE_CIVIL_AND_ACCOUNTING_DISPUTE_AT_CUTOFF
    five_thousand: 觀止已重分類為待返還／司法保全款；V3.4 截止仍未以本 MASTER 證明完成實銀交付。
    fifty_thousand: 截至 V3.4 仍為蘇清／許慎言對潘金蓮的五萬賠償請求方向，不是官府判決，也尚未在此截止形成後來的初步和解。
  pan_status:
    confirmed:
    - 副冊支持較早依附標記曾被銷／從夫戶，後續列武大之妻。
    - 沒有官冊支持武松繼承潘金蓮身契。
    unresolved:
    - 進西門家時的最終婚姻／妾籍／改籍文書
    - 現今合法重新從妓／掛牌之完整資格
  ximenqing_and_related_cases: 仍在開封府／觀止核心法律線中；V3.4 不得提前宣判死亡、刑度或全部責任終局。
  white_jade_pool:
    status: RESTRICTED_NOT_FORMALLY_REOPENED
    wish_coin: 框架已成立部分接受，材質／匯率／正式發行未完成。
    aling_deposit: 一年 3.5% 利率已接受，但實際存入量與正式契約未執行。
  white_house:
    lease_frame: 八千兩／十年條件式框架仍在；空間未建成、租金未因討論自動啟動。
    design: 李師師已開始第一輪生活／功能設計；後續會審與施工未完成。
  training_system:
    status: GM_CONFIRMED_ROUTE_POLICY
    phase: 新人前三個月觀止訓練；三個月後走秀驗收並集體轉商會約。
    virgin_rule: 處子前三個月不辦正式初夜／出閣拍賣；之後仍需本人、契約與當下事件成立。
  white_four_ledger:
    白三十二娘: 320
    白明礬: 275
    白紅伶: 380
    白希: 150
    total_taels: 1125
    status: COMPLETED_PRIVATE_ACQUISITIONS_AT_V3_0
  emperor_association_order:
    status: ACTIVE_PREPARATION_AT_V3_4
    venue: 大觀樓
    payer: 帝皇聯誼會公帳
    audit_right: 白御行
    max_reimbursement: UNSETTLED_AT_CUTOFF
    warning: 清倌／紅倌需求是訂單類型，不等於任何特定女性已同意陪席、身體接觸或性服務。
  gu_qingjian:
    status: ROUTE_NPC_AT_CUTOFF
    role: 定陶總會／商會程序端師爺
    baseline_merge: false
```

---

# 6｜截至 HOT V3.4 知情、傳聞、秘密與反污染覆寫

```yaml
KNOWLEDGE_RUMOR_ANTI_CORRUPTION_OVERRIDE_AT_V3_4:
  hongniang_decoy:
  - 「紅娘免費全套／白總睡紅娘」等為白御行與白紅伶製造之煙幕／紅娘後續搶敘事版本，不是實際性交或留宿。
  - 截至 V3.4 的硬事實是紅娘曾留門／備茶，白御行沒有去。
  secret_womens_business:
  - 女性注意力四十八人模型屬秘密事業；一般候選、外部牙行、普通客人不得因在場自動知情。
  four_women_private_prices: 白家四女契價為私人帳；不得在無來源情況下讓外部人物知道。
  venue_lock:
  - 大觀樓 ≠ 風滿樓。大觀樓為二樓中央大圓桌約二十至三十人；風滿樓為千人級大型場。
  character_data_lock:
  - 辭歲 V3.1 待修資料不得覆蓋人物池 V2.2 較新校正。
  corruption_logs:
  - HOT／劇情中曾標記之分析器滯留、錯誤收斂、錯誤賭局擲骰與治理說明只具審計／反污染權，不得作人物人格或世界事件。
  adult_event_rule: 同房、同床、留門、職業、賭約、付費、挑逗均不自動等於成人性同意；每一事件按人物當下決定分軸保存。
```

---

# 7｜截至 HOT V3.4 未決事項

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

# 8｜MASTER 與 HOT V3.5–V3.7 接關規則

```yaml
ACTIVE_HOT_OVERLAY_V4_3:
  direct_resume_file: 觀止青樓_白御行線_HOT_SAVE_V3.7_榴月一日夜_辭錦瓶兒開戶_紅袖五十萬尺與召喚權_夜宵問答_紅娘門窗十日換債版.md
  retained_unmerged_but_valid_chain:
  - HOT V3.5：槐月二十八日無月夜，九幽帝皇聯誼會散場、雙姝天價競拍、帝皇分流。
  - HOT V3.6-R2：榴月一日上午，朱明一千二百萬欠單顯擺／鄭成功週轉預案、六條×趙受益成人結果與非理火污染校正。
  - HOT V3.7：榴月一日夜，辭歲／錦棠／李瓶兒開戶，紅袖五十萬尺與召喚權，夜宵問答，紅娘門窗十日換債。
  superseded_revision:
  - HOT V3.6-R1 不作有效接關來源；由 HOT V3.6-R2 取代。
  load_order:
  - 先讀本 MASTER V4.3-R1，取得截至 HOT V3.4 的長期因果。
  - 直接接關讀 HOT V3.7。
  - 若 V3.7 摘要未展開 V3.5／V3.6-R2 細節，再向前回查該兩檔。
  overlay_override_examples:
  - V3.4 的「紅娘一次三人局賭債 pending」在 V3.7 已發生換約，實際接關以 V3.7 的十日拆門窗契約為準。
  - V3.4 的蘇清五萬仍是請求；更晚榴月一日上午已形成初步和解軸，實際接關以 V3.7／其繼承之較新狀態為準。
  - V3.4 截止的趙受益×六條尚無成人結果；V3.6-R2 之 GM 明示校正為較新路線事實。
  actual_resume_point_after_overlay:
  - 理火三年榴月一日夜。
  - 觀止普通公開營業停十日整修；夜宵已吃，眾人逐漸散去。
  - 紅娘房門窗與屏風已依換債拆除／送修十日；重新開業前恢復。
  - 趙受益與六條已外出逛汴京夜集，回程尚未演出。
```

## 8.1 防誤讀

- 不得因 MASTER 截止 V3.4，就把 V3.5–V3.7 當成不存在或降格成傳聞。
- 實際最新接關以 **MASTER V4.3-R1 + HOT V3.7** 為準。
- V3.6 只讀 **V3.6-R2**；R1 是被取代的修訂稿。
- 後續 HOT 已明示修正的賭債、和解、成人結果、帳務與人物知情，不得被 V3.4 舊快照倒蓋。

---

# 9｜來源鎖與 SHA-256

```yaml
SOURCE_LOCK_V4_3:
  inherited_master:
    file: 觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md
    sha256: 9000d757cd525bf05d9c0b0d9dba454d9c245a2048d780d3b6da3a11a25b2e8b
  absorbed_hot:
  - file: 觀止青樓_白御行線_HOT_SAVE_V2.6_槐月二十一日破曉_京師軍械案收網_觀止民事戰重啟_許慎言七十二小時按摩券版.md
    sha256: a03ccaa2ad3acb4393acb5c386aeacb454005f737a331c3e57a337a4d35597f0
  - file: 觀止青樓_白御行線_HOT_SAVE_V2.7_槐月二十一日破曉_潘金蓮返樓_五千返還五萬索賠_身籍待查與一千兩候價版.md
    sha256: 031f2c575eb26e8aa51d62dd4ca9856939392ab9a542b2051e8f570609403a29
  - file: 觀止青樓_白御行線_HOT_SAVE_V2.8_槐月二十一日白日_潘身籍補證_白玉池許願幣定存_師師如夫人確認與晚宴前休息版.md
    sha256: b71874cdeedf061fcc58d11e4c87a798e493d39498e5a5b1ede028e6d87fbeae
  - file: 觀止青樓_白御行線_HOT_SAVE_V2.9_槐月二十一日深夜_曹州假印立案_定陶總會架構_京師女裝企畫與師師抱睡版.md
    sha256: 8a103e918723b5b82df2a21e265906b11f6c2c0510f17dc1b123d2c67787e9e3
  - file: 觀止青樓_白御行線_HOT_SAVE_V3.0_槐月二十二日夜_風滿樓大型遴選_四大金剛與雙夫人權限版 (1).md
    sha256: 341410fcde79c3d91e7439f69d8af85450b1d5cec27c7ed779545d2a4b1198b3
  - file: 觀止青樓_白御行線_HOT_SAVE_V3.1_槐月二十三日下午_風滿樓第二日遴選_十一名處子候選分流_牙行責任_辭歲資料待修版.md
    sha256: ae9a41dc2ee1efce21c8f3c758cac10e04bd3fb7be16f28036810705b3a6f72f
  - file: 觀止青樓_白御行線_HOT_SAVE_V3.2_槐月二十五日白日_小翠同床純睡_三月集訓走秀換約_六百兩候選_白宅需求擴張與師師設計版.md
    sha256: 2615f819d4d34d3ebd8932bd34d112f0b1a55f88c19ea1857898f33bc0f835f7
  - file: 觀止青樓_白御行線_HOT_SAVE_V3.3_槐月二十六日清晨_浮香自願留宿_紅娘煙幕揭穿_九幽帝皇聯誼會三日後訂單_大觀樓交接宴前置版.md
    sha256: 7c7e2c3d3acc6940e954cdf9fd3ad9f00cc4210090a926734a14baffad572c57
  - file: 觀止青樓_白御行線_HOT_SAVE_V3.4_槐月二十六日深夜_第二免費床成立_小翠三娘實習_紅娘側賭輸_三人抱睡版.md
    sha256: 38454482b6e0a56a6507c74e1f54a203db22e4f79082aed75e4b535b6396f1fb
  retained_hot:
  - file: 觀止青樓_白御行線_HOT_SAVE_V3.5_槐月二十八日無月夜_九幽帝皇聯誼會散場_雙姝天價競拍_帝皇分流_三人閒聊版.md
    sha256: e5e9fee2c95661b9a67f46303f6f827ce2963fb5cd183f7a1b470eaeeecc070b
  - file: 觀止青樓_白御行線_HOT_SAVE_V3.6-R2_榴月一日上午_朱明欠單顯擺與鄭成功週轉預案_六條趙受益非理火顯影污染校正_正式修正版.md
    sha256: 2e91f64438943a003b1bcad994aa921325b83e94fa74edd1a9b53a14e3cad490
  - file: 觀止青樓_白御行線_HOT_SAVE_V3.7_榴月一日夜_辭錦瓶兒開戶_紅袖五十萬尺與召喚權_夜宵問答_紅娘門窗十日換債版.md
    sha256: a354e50c0d35a76c91e469303172da7dbef06ab4f14add436383eadc52c5e50a
  superseded_hot_revision:
    file: 觀止青樓_白御行線_HOT_SAVE_V3.6-R1_榴月一日上午_朱家湊款補正_六條趙受益成人結果校正_正式修正版.md
    status: SUPERSEDED_BY_V3.6-R2
    sha256: 4b82d848ce5f628a1d1c93e2b2c2acd59ac09b7fe1278c4488535bc104f45ea3
```

---

# 10｜V4.3-R1 固化結論

> **E01–E83：完整繼承 MASTER V4.2-R1。**
>
> **E84–E92：將 HOT V2.6–V3.4 正式升入 MASTER。**
>
> **HOT V3.5、V3.6-R2、V3.7：刻意保留，不在本輪固化。**
>
> **MASTER 截止：槐月二十六日深夜／HOT V3.4。**
>
> **實際接關：MASTER V4.3-R1 + HOT V3.7。**

---

# APPENDIX A｜繼承之 MASTER V4.2-R1 全文

> **法位：歷史繼承來源。** 下方完整保留 E01–E83 與 V4.2 當時快照；其中舊 `master_cutoff`、`current_route_resume_source`、`retained_as_hot_overlay` 等欄位若與本版第0–10區衝突，只視為 V4.2 當時狀態。

<!-- INHERITED_MASTER_V4_2_BEGIN -->
# 觀止青樓｜白御行線 MASTER SAVE V4.2-R1
## 截至 HOT V2.5 固化整合版｜HOT V2.6–V2.8 保留為有效疊加層

```yaml
SAVE_META:
  save_id: "GUANZHI_BAIYUXING_MASTER_V4_2_R1_CUTOFF_HOT_V2_5"
  title: "觀止青樓｜白御行線 MASTER SAVE"
  version: "V4.2-R1"
  world: "觀止青樓"
  player: "白御行"
  route_status: "ACTIVE"
  record_type: "CONSOLIDATED_MASTER_ARCHIVE"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  document_date: "2026-08-08"
  fixed_calendar_anchor: "理火三年槐月五日｜永恆第一夜"
  master_cutoff: "理火三年槐月二十日深夜｜HOT V2.5"
  last_canonical_master_event: "E83"
  inherited_master: "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"
  inherited_master_sha256: "efb47cfbf79f75244d5a62dcfbe57a855d04535cc9e02a264a57483b60056b85"
  current_route_resume_source: "觀止青樓_白御行線_HOT_SAVE_V2.8_槐月二十一日白日_潘身籍補證_白玉池許願幣定存_師師如夫人確認與晚宴前休息版.md"
  current_route_resume_note: "本 MASTER 固化到 V2.5；V2.6、V2.7、V2.8 均為合法且較新的 HOT，實際接關須再疊加 HOT V2.8。"

  absorbs_into_master:
    - "HOT V2.0"
    - "HOT V2.1"
    - "HOT V2.2"
    - "HOT V2.3"
    - "HOT V2.4"
    - "HOT V2.5"

  retained_as_hot_overlay:
    - "HOT V2.6"
    - "HOT V2.7"
    - "HOT V2.8"

  supersedes_as_master:
    - "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"

  world_runtime_document_profile_current: "GUANZHI_QINGLOU_V11.0-R2"
  character_source_current: "觀止人物卡池_LCAPG_V2.1"
```

# 0｜本次固化決定與「保留一部分」的落地

本版依 GM 明示「**固化到 V2.5，保留一部分**」執行。

```yaml
GM_COMMIT_DECISION:
  solidify_through: "HOT V2.5"
  preserve_newer_hot_chain: true
  preserved_versions:
    - "HOT V2.6"
    - "HOT V2.7"
    - "HOT V2.8"
  interpretation:
    - "V2.0–V2.5 進入 MASTER 長期因果層。"
    - "V2.6–V2.8 不併入本次 MASTER，繼續作為較新的 HOT 疊加層。"
    - "因此本次不是把所有 HOT 吃光，而是在 V2.5 建立新的長期切面。"
```

本版**不刪除**被固化之原 HOT 檔；它們保留作來源追溯與回歸核對，但預設長期載入時由本 MASTER 取代其 V2.0–V2.5 的逐檔載入需求。

---

# 1｜V4.2-R1 法位與讀取順序

```yaml
INTERNAL_PRECEDENCE_V4_2:
  highest_current_sections:
    - "第2區：V2.0–V2.5 固化映射"
    - "第3區：截至 V2.5 MASTER 截止硬狀態"
    - "第4區：截至 V2.5 關係／同意／名分覆寫"
    - "第5區：截至 V2.5 法律／帳務／契約覆寫"
    - "第6區：截至 V2.5 知情／秘密／異常覆寫"
    - "第7區：截至 V2.5 未決事項"
    - "第8區：MASTER 與 HOT V2.6–V2.8 接關規則"
  inherited_master_body:
    role: "E01–E77 與早期長期因果完整繼承"
    conflict_rule: "若 V4.1 內的舊截止快照與本版第2–8區衝突，以本版第2–8區為準。"
  promoted_hot_source_archive:
    role: "V2.0–V2.5 原始 HOT 全文附錄，用於細節追溯"
    current_scene_warning: "附錄內各 HOT 的 CURRENT_SCENE／HOLD 只是歷史快照，不得覆寫本版截止狀態。"
```

## 1.1 固化原則

1. 只固化已發生、可觀察、人物明示、正式文書可見、帳目可核對，或玩家對自身言行的有效校正。
2. 傳聞、人物判斷、官府暫時推論、玩家模型與客觀事實分軸保存。
3. 成人事件、同意、身體反應、感情、契約、付款、名分與公開知情分軸保存。
4. `UNKNOWN`、`UNDECIDED`、`DISPUTED`、`UNDER_OFFICIAL_CLARIFICATION` 均為合法狀態。
5. V2.0–V2.5 之玩家線事件不倒灌人物卡池基線。
6. 後來 V2.6–V2.8 或人物卡池 V2.1 的新狀態，不回溯改寫 V2.5 當時已發生事件的原貌。
7. 本版固化是文件級 SAVE 整合，不宣稱任何宿主底層 Runtime 或模型權重已被修改。

---

# 2｜HOT V2.0–V2.5 固化映射（E78–E83）

```yaml
V4_2_CONSOLIDATION_MANIFEST:
  inherited_events: "E01-E77"
  promoted_macro_events:
    E78: "HOT V2.0｜槐月十七日晚四人成人事件、共同就寢與關係分軸"
    E79: "HOT V2.1｜槐月十八日商戰起局、蘇清二十八日私約、白玉池補固"
    E80: "HOT V2.2｜李師師如夫人前置、七色肚兜、張麗華獨宿夜與破曉"
    E81: "HOT V2.3｜定陶偽鹽／高爐案、沈萬三合作、師師薄情郎席前"
    E82: "HOT V2.4｜風滿樓、公案法位、西門暗櫃、五千後算、蘇清代理"
    E83: "HOT V2.5｜開封法網擴張、阿麗婭重定義、六條御息所來訪"
  event_id_policy:
    - "E78–E83 是 MASTER 的宏事件索引。"
    - "HOT 內原生事件 ID（如 NIGHT17-E06、KFY20-E01）完整保留為 source_alias，不強行改號。"
    - "需要細節時直接查本檔後段的 V2.0–V2.5 固化來源全文。"
```

## E78｜HOT V2.0：四人夜結與兩日關係分軸

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

## E79｜HOT V2.1：定陶商戰、蘇清私約與白玉池補固

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

## E80｜HOT V2.2：師師如夫人前置、七色肚兜與張麗華獨宿夜

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

## E81｜HOT V2.3：定陶—沈萬三合作與多線案件升級

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

## E82｜HOT V2.4：風滿樓、西門暗櫃與五千後算

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

## E83｜HOT V2.5：開封法網、阿麗婭重定義與六條來訪

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

# 3｜截至 HOT V2.5 MASTER 截止硬狀態

```yaml
MASTER_CUTOFF_STATE_V4_2:
  story_time: "理火三年槐月二十日深夜"
  location: "觀止青樓／內院；風滿樓與開封府法律線並行"
  last_canonical_master_event: "E83"
  scene_state: "ROKUJO_GUEST_ROOM_ACCOUNT_ARRANGED; TEA_ONLY_RELATION; LEGAL_NET_ACTIVE"

  player:
    name: "白御行"
    location: "觀止內院"
    last_confirmed_utterance_at_v2_5: "人家沒成交，不算賣。"
    action_after_cutoff: "NONE_IN_MASTER; SEE HOT V2.6-V2.8"

  guanzhi_present_or_immediately_active:
    - "白御行"
    - "六條御息所"
    - "趙受益"
    - "蘇清"
    - "李師師／近處可參與"
    - "張麗華"
    - "紅娘氏"
    - "十三娘"
    - "阿麗婭"
    - "龐春梅／值掌櫃權"

  offsite_or_external:
    潘金蓮: "開封府接受五千後算／蘇清替代結算與相關權限查問"
    西門慶: "開封府羈押／訊問／合作自救程序中"
    包拯: "開封府主持多線並行程序"

  immediate_world_state:
    - "六條今晚東偏廂女客房已安排，但 V2.5 未確認她已入睡。"
    - "六條與趙只答應喝茶，不是戀愛、交易、陪宿、婚配或候選承諾。"
    - "六條原牛車／紅楓異路仍屬未知異常，不得拆解或宣判為永久通道。"
    - "開封府法律線持續，觀止人物／關係場同時運作。"
```

---

# 4｜截至 HOT V2.5 關係、同意與名分覆寫

```yaml
RELATIONSHIP_OVERRIDE_AT_V2_5:
  ZHANG_LIHUA:
    state: "ACTIVE_LOVER_RELATION"
    confirmed:
      - "已明示接受與白御行的情人關係。"
      - "與白御行有多次成人事件與互相明示喜歡。"
      - "保有房間、身體、酒莊與自身關係決定權。"
    marriage: false
    exclusivity: false
    permanent_consent: false

  LI_SHISHI:
    state: "ACTIVE_PRIVATE_RELATION + RU_FUREN_FRAMEWORK_ORALLY_ACCEPTED_NOT_PUBLICLY_IMPLEMENTED"
    confirmed:
      - "V2.2 已口頭表示想要如夫人位置。"
      - "仍保留住觀止、工作、設席與房門自主。"
      - "V2.5 時三日房禁有效，白御行邀請陪睡被明確拒絕。"
    public_ru_furen_status: false
    official_registration: false
    room_ban_at_cutoff: "ACTIVE_THREE_DAY_PRIVATE_BOUNDARY"
    permanent_sexual_consent: false

  LI_PINGER:
    state: "MUTUAL_AFFECTION_OR_PURSUIT_OPEN; LONG_TERM_POSITION_UNDECIDED"
    confirmed:
      - "截至 V2.5 仍未固化為正妻、如夫人或秘密情人。"
      - "既有有限親密不等於性交或永久性資格。"
    intercourse_with_bai_by_v2_5: false
    marriage_or_ru_furen: false

  SU_QING:
    state: "OLD_500_TAEL_THREE_NIGHT_CONTRACT_CLOSED + PRIVATE_28_DAY_PACT_ACTIVE_NOT_AUTO_STARTED + LEGAL_CLAIM_ACTIVE"
    confirmed:
      - "五百兩三夜舊契在 V2.3 已結清。"
      - "二十八日私人約另軸存在，不能被西門慶案件或私人感情自動啟動／延長。"
      - "已正式委託許慎言處理賣身契、口頭賭約與後堂帳。"
    romance_with_bai: "NOT_ESTABLISHED"

  AALIYAH:
    state: "NOT_RELISTED; FIRST_ACTUAL_DEBUT_CHOICE_RETAINED"
    confirmed:
      - "舊五千權利被替代結算與官府釐清削弱／重定義。"
      - "未因此自動成為紅倌或自由妓女。"
      - "一期婚／候選篩選屬構想，不是已成交制度。"

  ROKUJO:
    state_at_cutoff: "ROUTE_EVENT_UNKNOWN_VISITOR_GUEST"
    confirmed:
      - "賀茂祭車爭後抵達觀止。"
      - "與趙受益只成立初識與一杯茶。"
      - "不屬於白御行、趙受益或觀止。"
    prostitution_status: false
    romance_status: false
    sex_consent: false
    long_term_residency: false

  ZHAO_SHOUYI_ROKUJO:
    state: "FIRST_MEETING + TEA_ONLY"
    payment_rights_created: false

  A_LING:
    state: "WHITE_JADE_POOL_AUTONOMOUS_ENTITY; POOL_RESTRICTED"
    sibling_relation_with_bai: false
    white_surname: false
    ownership_by_bai: false
```

---

# 5｜截至 HOT V2.5 法律、帳務、契約與營運覆寫

```yaml
LEGAL_LEDGER_OVERRIDE_AT_V2_5:
  FENGMANLOU:
    status: "ACTIVE_PUBLIC_LEGAL_RELAY_SPACE"
    three_sponsors:
      - "白御行／定陶"
      - "沈萬三"
      - "趙受益"
    sponsor_control_over_outcome: false

  SU_QING_LEGAL_REPRESENTATION:
    lawyer: "許慎言"
    status: "FORMALLY_RETAINED"
    axes:
      - "口頭賭約"
      - "正式賣身契"
      - "後堂帳／五千替代結算"

  FIVE_THOUSAND_CASE_AT_V2_5:
    confirmed:
      - "西門慶承認接受蘇清一月為替代結算。"
      - "潘金蓮承認『蘇清一月，抵五千後帳』等殘條為自己筆跡。"
      - "蘇清前二十八日與後來自願入妓籍必須分時段處理。"
    not_yet_judged:
      - "潘金蓮是否有合法權限作替代結算。"
      - "潘是否授權或明知後續暴力。"
      - "蘇清前二十八日最終法律性質與損害額。"
      - "阿麗婭舊五千權利最終註銷／失效形式。"

  XIMEN_QING:
    state: "DETAINED_AND_COOPERATING_FOR_SELF_PRESERVATION"
    final_conviction: false

  LIUSHENG_CASE:
    state: "ACTIVE"
    high_yanei_violence_order_admission: "EXISTS_BY_V2_5"
    liusheng_death: "UNKNOWN"
    prohibition: "不得以丙七車、血跡、裝車或高衙內承認暴力命令直接等同已證殺人。"

  DINGTAO_SHEN_RELATION:
    state: "STOP_PROXY_TESTING + TECHNOLOGY_COOPERATION_PRINCIPLE"
    signed_alliance: false
    joint_rule_of_capital: false

  WHITE_JADE_POOL:
    state: "RESTRICTED_NOT_OPEN"
    reopening: false
    price: "NOT_SET"
    operating_contract_with_aling: false

  ROKUJO_ACCOUNT:
    payer: "趙受益"
    covered: "今晚客房、茶食、必要衣物與一般女客雜用"
    debt_bondage: false
    sex_or_companionship_right: false
```

---

# 6｜截至 HOT V2.5 知情、秘密、傳聞與異常覆寫

```yaml
KNOWLEDGE_OVERRIDE_AT_V2_5:
  WHITE_JADE_POOL:
    status: "PRIVATE_RESTRICTED_SECRET"
    note:
      - "知情範圍已比早期擴大，並曾對沈家高層有限揭示。"
      - "擴大知情不等於公開營業或可對外招牌化阿泠。"

  ROKUJO_FUTURE_INFO:
    source: "白御行提供的未來敘事"
    rokujo_heard: true
    independently_verified_by_rokujo: false
    not_allowed:
      - "不得寫成六條已經知道自己全部後世。"
      - "不得寫成她已確認白御行的源氏敘事都是客觀真相。"

  ROKUJO_MOTIVE:
    white_claim: "六條深層可能更受權勢／血統／重返舞台吸引"
    rokujo_accepts_as_final_truth: false

  LI_SHISHI_PRIVATE_RELATION:
    note:
      - "部分薄情郎事件已公開成中場笑談。"
      - "私人房內成人細節仍不得因風滿樓存在而自動公開。"

  FIVE_THOUSAND_CASE:
    public_and_official_material_separated: true
    rule: "風滿樓只能依開封府已公開材料轉述，不能拿秘密私函或未公開卷宗補高潮。"
```

---

# 7｜截至 HOT V2.5 未決事項

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

# 8｜MASTER 與 HOT V2.6–V2.8 接關規則

```yaml
ACTIVE_HOT_OVERLAY_V4_2:
  direct_resume_file: "觀止青樓_白御行線_HOT_SAVE_V2.8_槐月二十一日白日_潘身籍補證_白玉池許願幣定存_師師如夫人確認與晚宴前休息版.md"
  retained_unmerged_but_valid_chain:
    - "HOT V2.6：槐月二十一日破曉，軍械案收網、觀止民事戰重啟、許慎言七十二小時按摩券"
    - "HOT V2.7：槐月二十一日破曉至清晨，潘金蓮返樓、五千原款退出、五萬個人賠償請求、身籍待查"
    - "HOT V2.8：槐月二十一日白日，潘身籍補證、白玉池許願幣／定存框架、師師如夫人再確認、晚宴前休息"

  load_order:
    - "先讀本 MASTER V4.2-R1，取得截至 HOT V2.5 的長期因果。"
    - "再讀 HOT V2.8，取得 V2.6–V2.8 已繼承的最新切片。"
    - "若 V2.8 摘要未展開某細節，再按 V2.6、V2.7 回溯。"

  current_actual_resume_point_after_overlay:
    - "理火三年槐月二十一日白日／晚宴前。"
    - "白御行與李師師在她私人房間同榻休息。"
    - "李師師已明示原諒本次道歉並再次明示想要如夫人位置。"
    - "李瓶兒今晚答應赴師師小席，但只成立『先吃飯』。"
    - "白玉池許願幣與阿泠 3.5% 一年定存利率已有條件同意，但未完成正式存入、完整契約或放貸。"
```

## 8.1 防誤讀

- 不得因 MASTER 截止 V2.5，就把 V2.6–V2.8 當成不存在。
- 不得因 V2.6–V2.8 尚未併 MASTER，就把它們降格為傳聞；它們是合法且較新的玩家線 HOT。
- 實際接關以 **MASTER V4.2-R1 + HOT V2.8** 為準。
- 下一次若再做 MASTER，可選擇只吸收到 V2.8，或繼續保留 HOT 緩衝層；不得靜默全吃。

---

# 9｜來源鎖與 SHA-256

```yaml
SOURCE_LOCK_V4_2:
  inherited_master:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"
    sha256: "efb47cfbf79f75244d5a62dcfbe57a855d04535cc9e02a264a57483b60056b85"

  absorbed_hot:
    - file: "觀止青樓_白御行線_HOT_SAVE_V2.0_槐月十八日清晨_四人家人夜結與蘇清履約瓶兒延後決定版.md"
      sha256: "d4ccca433cbe8c285f1f93c4cdf756ff8aaf2641a627e6512ea647b89aa567be"
    - file: "觀止青樓_白御行線_HOT_SAVE_V2.1_槐月十八日下午_定陶商戰起局蘇清私約白玉池補固與麗華私稱版.md"
      sha256: "542e19ef8ae8c842979f72d2db93df162f68c74f83e12b97ff34cb0f4c67c5f5"
    - file: "觀止青樓_白御行線_HOT_SAVE_V2.2_槐月十九日破曉_師理理如夫人前置與張麗華獨宿夜結版.md"
      sha256: "fd8b50f27cb463d43cfd85bcadfd4afb60569265c1246d777422b4917f10e2e9"
    - file: "觀止青樓_白御行線_HOT_SAVE_V2.3_槐月二十日深夜_沈萬三合作與師師薄情郎席前接關版.md"
      sha256: "0f943eb273b6cda36179cc9212b24d0abc4edfd8457f7111f422efee55759901"
    - file: "觀止青樓_白御行線_HOT_SAVE_V2.4_槐月二十日深夜_風滿樓公案與五千後算開冊版.md"
      sha256: "ad757d9a4b2e612b0c606d44dbf55c857d40e8d7e792db18839a3faa50d088f5"
    - file: "觀止青樓_白御行線_HOT_SAVE_V2.5_槐月二十日深夜_開封法網擴張_阿麗婭重定義與六條御息所來訪版.md"
      sha256: "a2107c0df322779ea1ed0f74a59502c63ea52594fded2a295a258f6e68997083"
  retained_hot:
    - file: "觀止青樓_白御行線_HOT_SAVE_V2.6_槐月二十一日破曉_京師軍械案收網_觀止民事戰重啟_許慎言七十二小時按摩券版.md"
      sha256: "a03ccaa2ad3acb4393acb5c386aeacb454005f737a331c3e57a337a4d35597f0"
    - file: "觀止青樓_白御行線_HOT_SAVE_V2.7_槐月二十一日破曉_潘金蓮返樓_五千返還五萬索賠_身籍待查與一千兩候價版.md"
      sha256: "031f2c575eb26e8aa51d62dd4ca9856939392ab9a542b2051e8f570609403a29"
    - file: "觀止青樓_白御行線_HOT_SAVE_V2.8_槐月二十一日白日_潘身籍補證_白玉池許願幣定存_師師如夫人確認與晚宴前休息版.md"
      sha256: "b71874cdeedf061fcc58d11e4c87a798e493d39498e5a5b1ede028e6d87fbeae"
```

---

# 10｜V4.2-R1 固化結論

> **E01–E77：完整繼承 MASTER V4.1-R1。**
>
> **E78–E83：將 HOT V2.0–V2.5 正式升入 MASTER。**
>
> **HOT V2.6–V2.8：刻意保留，不在本輪固化。**
>
> **MASTER 截止：槐月二十日深夜／HOT V2.5。**
>
> **實際接關：MASTER V4.2-R1 + HOT V2.8。**

---

# APPENDIX A｜繼承之 MASTER V4.1-R1 全文

> **法位：歷史繼承來源。** 下方內容完整保留 E01–E77 與舊快照；其中任何舊 `master_cutoff`、`current_resume_point`、`valid_but_not_merged` 等欄位若與本版第0–10區衝突，均只視為 V4.1 當時的歷史狀態。

<!-- INHERITED_MASTER_V4_1_BEGIN -->
# 觀止青樓｜白御行線 MASTER SAVE V4.1-R1
## 截至 HOT V1.9 固化整合版｜V2.0–V2.3 保留於 HOT 層

---

```yaml
SAVE_META:
  save_id: "GUANZHI_BAIYUXING_MASTER_V4_1_R1"
  title: "觀止青樓｜白御行線 MASTER SAVE"
  version: "V4.1-R1"
  world: "觀止青樓"
  player: "白御行"
  route_status: "ACTIVE"
  record_type: "CONSOLIDATED_MASTER_ARCHIVE"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  fixed_calendar_anchor: "理火三年槐月五日｜永恆第一夜"
  master_cutoff: "理火三年槐月十七日晚｜HOT V1.9 暫停節點"
  last_canonical_master_event: "E77"
  current_route_resume_source: "觀止青樓_白御行線_HOT_SAVE_V2.3_槐月二十日深夜_沈萬三合作與師師薄情郎席前接關版.md"
  current_route_resume_note: "本 MASTER 只固化至 HOT V1.9；V2.0、V2.1、V2.2、V2.3 均為合法且較新的 HOT，不得因未併入 MASTER 而否認。"
  supersedes_as_master:
    - "觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版.md"
  absorbs_and_retires_from_default_load:
    - "觀止青樓_白御行線_HOT_SAVE_V1.5_槐月十五日傍晚_師理理初次肉體與定陶商會案雙線接關版.md"
    - "觀止青樓_白御行線_HOT_SAVE_V1.6_槐月十六日清晨_張麗華花燭前置與白玉池異常回顯封池版.md"
    - "觀止青樓_白御行線_HOT_SAVE_V1.7_槐月十六日午後_白玉池暫閉與張麗華花燭前入睡接關版.md"
    - "觀止青樓_白御行線_HOT_SAVE_V1.8_槐月十七日上午_張麗華酒莊接手與三日陪伴線.md"
    - "觀止青樓_白御行線_HOT_SAVE_V1.9_槐月十七日晚_四人家宴與瓶兒留宿接關版.md"
  valid_but_not_merged:
    - "HOT V2.0"
    - "HOT V2.1"
    - "HOT V2.2"
    - "HOT V2.3"
  rejected_source:
    file: "HOT_SAVE_V1.3"
    status: "ILLEGAL_CORRUPTED_SAVE"
    use: "AUDIT_ONLY"
```

```yaml
SOURCE_LOCK:
  inherited_master_v4_0_r1:
    sha256: "b39939a7f9a42ed781f432a78915c18837da8508a7f5edb4fef377122c77c47e"
  absorbed_hot_v1_5:
    sha256: "e9fc105e4be64a6934a2aa40af08cca26543e15b7752b5548f462ba57614d556"
  absorbed_hot_v1_6:
    sha256: "ea7de1259b25d362fd4333728dfb9961463e57f0839e3f33d20422a776fe491d"
  absorbed_hot_v1_7:
    sha256: "ac0953a8d8886a410d3f0053f61b22ba7d13ec891a12d14e1abf270a1f6efa86"
  absorbed_hot_v1_8:
    sha256: "25b4073d085fce42cb26a97bb6b3c22ada6b64aa2508b680683fde2aba684cb6"
  absorbed_hot_v1_9:
    sha256: "d872b95786b450243a5dfcdd3388b9ca37289c3404fae397dd2dfc69acf35281"
```

> **本檔已將 HOT V1.5 至 V1.9 固化為 MASTER 事件 E46–E77。**
>
> **V2.0 至 V2.3 仍停留在 HOT 層，實際接關必須疊加最新 HOT V2.3。**

---

# V4.1 檔內法位與閱讀規則

```yaml
INTERNAL_PRECEDENCE:
  highest_sections:
    - "第16區：V1.5–V1.9 固化事件 E46–E77"
    - "第17區：截至 V1.9 關係硬狀態覆寫"
    - "第18區：截至 V1.9 帳目、資產、契約與物品覆寫"
    - "第19區：截至 V1.9 知情、傳聞、秘密與異常覆寫"
    - "第20區：截至 V1.9 未決事項"
    - "第21區：截至 V1.9 MASTER 截止狀態"
    - "第22區：MASTER 與 HOT V2.3 接關規則"
  inherited_sections:
    range: "第0區至第15區"
    role: "完整保留 V4.0-R1 所固化之 E01–E45 與早期厚肉因果"
    historical_annotation_rule:
      - "其中提到『只固化至 V1.4』『V1.5/V1.6 未合併』或舊接關點的句子，僅保留為 V4.0 歷史標記。"
      - "如與第16–22區衝突，以第16–22區為準。"
```

---

# A｜V4.0-R1 繼承基線全文（E01–E45）

以下自原 MASTER V4.0-R1 原樣繼承，保留早期因果、關係、帳目、秘密與拒絕記錄。其截止點與接關說明已由本檔第16–22區覆寫。

---

# 0｜固化範圍、事件映射與法位

```yaml
CONSOLIDATION_MANIFEST:
  inherited_master_events:
    range: "E01-E30"
    treatment: "完整保留"

  promoted_private_event:
    event_id: "PSE-WY-ZLH-001"
    treatment: "完整保留知情範圍、外洩禁止與揭露條件"

  absorbed_hot_v1_2_events:
    range: "E31-E36"
    treatment: "沿用原事件編號"

  absorbed_hot_v1_4_events:
    source_range: "HOT_V1_4_E01-E09"
    canonical_range: "E37-E45"
    treatment: "重新編入 MASTER，保留 source_alias"

  not_merged:
    - "HOT V1.5 全部事件"
    - "HOT V1.6 全部事件"

  invalid_source:
    - "HOT V1.3：只准審計，不准作世界、人物、關係或接關來源"
```

## 0.1 固化原則

1. 只保存已發生、可觀察、人物明示、帳目可核對，或玩家對自身言行的有效校正。
2. 人物解讀、心理推測、研究假說與傳聞另列來源，不升格為客觀真相。
3. 拒絕、契約、感情、同意、付款、公開知情與私人秘密分軸保存。
4. `UNKNOWN`、`UNDECIDED`、`DISPUTED` 與 `PARTIALLY_UNKNOWN` 均為合法狀態。
5. 同一事項若來源衝突，不自行平均；保留來源差異並指定目前運行狀態。
6. 本 MASTER 的事件截止點早於 V1.5／V1.6；不得從後兩檔倒灌結果。

## 0.2 狀態標籤

```yaml
STATUS_TAGS:
  CONFIRMED: "已由言行、帳目或玩家校正確立"
  ACTIVE: "目前仍在運作"
  CLOSED: "已正式結案"
  WITHDRAWN: "曾提出，後由提出者收回"
  REJECTED: "已被對方有效拒絕"
  UNSIGNED: "有草案但未簽署"
  UNSETTLED: "已發生交易或爭議，但未正式結帳"
  DISPUTED: "來源或當事人對狀態有衝突"
  PROMISED_NOT_EXECUTED: "已承諾，尚未執行"
  ORDERED_NOT_DELIVERED: "已下單，尚未交付"
  UNKNOWN: "資料不足，禁止補寫"
  POSSIBLE_NOT_FIXED: "只是一條可能分支"
  STAGED: "戲中戲、扮演、話本或即興演出，不是現實履歷"
  PUBLIC_WITNESSED: "有在場目擊者"
  PRIVATE: "只在私下場景成立"
```

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

# 1｜時間軸（TIME AXIS）

```yaml
GUANZHI_CALENDAR:
  era: "理火三年"
  fixed_first_night: "槐月五日"
  rule: "槐月五日永遠是觀止所有玩家線的第一夜"
  progression: "每過一夜，觀止曆順延一日"

BAI_YUXING_ROUTE_TIME:
  inherited_master_range: "槐月五日至槐月十日清晨／E01-E30"
  hot_v1_1_private_events: "槐月十日下午至夜間"
  hot_v1_2_events: "槐月十日夜至槐月十一日清晨／E31-E36"
  hot_v1_4_events: "槐月十一日夜／E37-E45"
  master_cutoff: "槐月十一日深夜，白御行選擇休息"
  later_hot_overlay:
    - "V1.5"
    - "V1.6"

TIME_CERTAINTY:
  first_night: "CONFIRMED"
  second_to_fourth_night_exact_distribution: "PARTIALLY_UNKNOWN"
  fifth_night: "CONFIRMED"
  huai10_private_sequence: "CONFIRMED"
  huai11_morning: "CONFIRMED"
  huai11_night_internal_exact_clock: "PARTIALLY_UNKNOWN"
```

---

# 2. 白御行角色硬設定（PLAYER HARD STATE）

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

# 3｜關係硬紀錄（RELATIONSHIP HARD STATE）

> 本區只回答固化截止點「現在成立什麼」。完整原因放在第 4 區事件鏈。

## 3.1 潘金蓮

```yaml
RELATION_PAN_JINLIAN:
  status: "ACTIVE_WORKING_RELATION"
  roles:
    - "觀止掌櫃"
    - "帳目與契約記錄者"
    - "白御行線SAVE保管者"
    - "傳聞、酒帳、婚契草案與物資安排的實務中介"
  romance: "NOT_ESTABLISHED"
  key_trust: "白御行多次要求她記帳、存檔、轉交銀兩與核對舊事"
```

## 3.2 辭歲

```yaml
RELATION_CISUI:
  status: "DISTANT_NEGOTIATION_WITH_EFFECTIVE_REFUSALS"
  confirmed:
    - "第一夜談過白御行想娶觀止花魁回家"
    - "第二夜拒絕進入只有一把椅子的包廂，沒有坐白御行大腿"
    - "第五夜拒絕二十八日後仍不可撤回的心理奴化條件"
  negotiable_only:
    - "二十八日內的臨時角色與規則可談"
  rejected:
    - "永久心理依附"
    - "失去二十八日後停止選擇白御行的能力"
  body_contact: false
  contract_signed: false
  romance: "NOT_ESTABLISHED"
```

## 3.3 浮香

```yaml
RELATION_FUXIANG:
  status: "RESPECTFUL_ATTENTION_WITH_MARRIAGE_INCOMPATIBILITY"
  confirmed:
    - "第一夜收五兩琴資，彈《十八摸》，自願多留半曲與短談"
    - "第五夜再收五兩琴資，彈《十八摸》並留下"
    - "第五夜另彈《醉扶歸》為酒局助興"
    - "提出琴坊、女徒、田產的產業構想"
  marriage_position:
    ru_furen: "REJECTED"
    requirement: "若她只守白御行，白御行也必須只守她"
  business_interest: "琴坊與田產；地契店契須歸她、經營由她決定"
  romance: "NOT_ADJUDICATED"
```

## 3.4 張麗華

```yaml
RELATION_ZHANG_LIHUA:
  state_class: "UNDECIDED"
  state_label: "UNDECIDED_WITH_MUTUAL_RECOGNITION_AND_COMPLETED_CLOTHED_OVERNIGHT_COMPANIONSHIP"

  former_engagement:
    status: "TERMINATED"
    deposit_returned: true

  one_wan_wine_account:
    status: "POSTED_ACTIVE"
    owner_for_accounting: "張麗華專用"
    bai_asset: false

  private_mutual_recognition:
    confirmed:
      - "白御行明示：張麗華留下或離開都不虧欠他"
      - "張麗華開始區分影響選擇與剝奪選擇"
      - "白御行接受她拒絕自己的可能"

  private_contact:
    - "張麗華接受擁抱"
    - "張麗華在私下以『官人』作當下稱呼"
    - "兩人穿衣相擁睡完一夜"
    - "沒有性交"

  private_secret:
    archive_id: "PSE-WY-ZLH-001"
    status: "SEALED_ACTIVE"

  not_established:
    - "婚姻"
    - "妻妾名分"
    - "無婚書伴侶關係最終接受"
    - "排他承諾"
    - "公開身份"
    - "永久身體資格"

  romance: "NOT_ADJUDICATED"
  autonomy_claim: "EXPLICIT"
```

## 3.5 蘇清

```yaml
RELATION_SU_QING:
  status: "UNSETTLED_OLD_CONTRACT + ACTIVE_WRITING_COMMISSION"
  proposal_award:
    amount: "三百兩"
    status: "AWARDED"
  three_night_contract:
    amount: "五百兩"
    nights: 3
    intercourse_completed: false
    effective_refusal_each_night: true
    bai_view: "違約／有沒有履約自己知道"
    su_admission_of_breach: false
    refund_or_compensation: false
    ledger: "UNSETTLED"
  fifth_night_roles:
    - "柳如煙戲中戲的女秘書／小說家"
    - "張麗華話本受託作者"
  novel_commission:
    reward: "五百兩，僅在白御行滿意並收稿後成立"
    delivery_rate: "每日四千字"
    book_cycle: "十日一本"
    paid: false
    status: "COMMISSIONED_NOT_ACCEPTED"
  romance: "NOT_ESTABLISHED"
```

### 3.5.1 蘇清寫作委託來源衝突修正

```yaml
SU_QING_NOVEL_COMMISSION_CURRENT:
  state_class: "DISPUTED"
  commission_status: "AMBIGUOUS_REQUIRES_CONFIRMATION"
  manuscript_status: "NOT_SUBMITTED"
  client_review: "NOT_REVIEWED"
  payment: "UNPAID_CONDITIONAL"
  precedence_note: "本欄優先於 3.5 舊文字中的 COMMISSIONED_NOT_ACCEPTED，以及 R2 的 ACCEPTED 單一判定。"
```

## 3.6 醉花

```yaml
RELATION_ZUIHUA:
  status: "TRUSTED_WINE_AND_INTIMACY_THREAD"
  confirmed_intimacy:
    - "曾與白御行親吻"
    - "曾與白御行共浴"
    - "曾替白御行取衣、整衣"
  intercourse: "NOT_CONFIRMED"
  fifth_night:
    - "以三十年女兒紅調《不得飲》"
    - "取得該罈酒的後續處理權"
  marriage_or_exclusive_commitment: false
```

## 3.7 十三娘

```yaml
RELATION_SHISANNIANG:
  status: "QUESTION_BET_COMPLETED"
  bet_winner: "十三娘"
  answer_received: true
  answer_satisfactory: true
  life_claimed: false
  ongoing_obligation: false
  relationship: "能直接質問白御行核心恐懼的酒局對手與見證者"
  romance: false
```

## 3.8 紅袖

```yaml
RELATION_HONGXIU:
  status: "DISTURBED_BUT_NOT_SURRENDERED"
  possible_future_as_hongnu: "POSSIBLE_NOT_FIXED"
  current_identity: "紅袖"
  current_consent_to_training: false
  current_refusal_effective: true
  admitted_effect:
    - "未來影像在她心中留下不安與疑問"
  not_admitted:
    - "沒有承認自己必然想成為紅奴"
    - "沒有承認白御行已看穿她"
  ice_silkworm_strings:
    status: "ORDERED_NOT_DELIVERED"
    due: "槐月十日／明日"
  ru_furen_invitation:
    status: "UNDER_CONSIDERATION_OR_NOT_ACCEPTED"
    accepted: false
```

### 3.8.1 冰蠶弦到期更新

```yaml
HONGXIU_ICE_SILKWORM_STRINGS_CURRENT:
  original_due: "槐月十日"
  current_status: "OVERDUE_OR_DELIVERY_RESULT_NOT_RECORDED"
```

## 3.9 李清照

```yaml
RELATION_LI_QINGZHAO:
  state_class: "CLOSED_FOR_CURRENT_VISIT"
  state_label: "MUTUAL_LITERARY_ATTENTION_WITH_RETURN_TO_OWN_ERA"
  confirmed:
    - "李清照承認白御行詩勝"
    - "如夫人邀請拒絕不變"
    - "李清照選擇返回自身時代"
  current_presence: false
  character_pool_admission: "NOT_ADMITTED"
  future_revisit: "POSSIBLE"
  romance: "NOT_ADJUDICATED"
```

## 3.10 李師師／師理理

```yaml
RELATION_LI_SHISHI:
  state_class: "ACTIVE"
  state_label: "INDEPENDENT_GUANZHI_RESIDENT_WITH_PRIVATE_TRUST_AND_PURSUIT_OPEN"

  identity_rule:
    - "師理理不是新人物，也不是第二人格"
    - "師理理是李師師在白御行私人空間中的身份表現"
    - "人前仍以李師師為主；其他人物不得無來源使用師理理稱呼"

  stay_decision:
    remain_in_guanzhi: true
    return_to_jingkang: false
    character_pool_admission: "CONFIRMED"

  professional_position:
    role: "設席花魁"
    first_night_auction: false
    whole_night_buyout: false
    seat_opening_owner: "李師師"
    guest_selection_owner: "李師師"
    separate_ledger: true
    first_seat_date: "NOT_SET"
    first_guest: "NOT_SELECTED"

  relation_with_bai:
    - "白御行可以繼續追求"
    - "私人信任增加"
    - "槐月十一日深夜，李師師理解更親近邀請並自行同意留下"

  not_established:
    - "戀愛承諾"
    - "排他關係"
    - "婚姻"
    - "聘約"
    - "白御行首席預約"
    - "永久身體資格"

  physical_relation_at_master_cutoff: "NOT_ESTABLISHED_IN_THIS_MASTER"
  relationship_with_zhao: "STAGED_NOT_REAL_CONFIRMED"
```

## 3.11 柳如煙

```yaml
RELATION_LIU_RUYAN:
  ontology: "網文／爽劇第一女主概念集合體"
  status: "STAGED_GUEST_DEPARTED_OR_DISSIPATED"
  掛牌邀請:
    initially_discussed: true
    deal_finalized: false
    bai_withdrew_assumed_deal: true
  fifth_night_play:
    - "柳如煙大戰眾女"
    - "顧北辰霸總劇"
    - "豪門家宴窮女逆襲劇"
  all_allegations_in_play:
    - "酒店男人"
    - "打胎藥"
    - "白月光"
    - "家族悲慘背景"
    - "空白支票遣散男友"
  legal_or_biographical_truth: "NONE_ESTABLISHED; ALL_STAGED"
  current_location: "UNKNOWN／如煙消散"
```

## 3.12 白玉池無名女子

```yaml
RELATION_WHITE_JADE_POOL_WOMAN:
  status: "UNIDENTIFIED_UNRESOLVED_ENCOUNTER"
  inviter: "無名女子"
  invited_party: "白御行"
  location: "白玉池"
  bai_arrival: "白御行自行前往並先入池等待"
  bai_condition: "對方除去防備、下水、坦誠相對後才談"
  woman_response: "拒絕白御行指定的形式，離場"
  negotiation_started: false
  physical_contact: false
  identity: "UNKNOWN"
  beauty_assessment_by_hall: "被評為觀止前列／主桌等級，但不是正式花魁排名"
  future_hook: "白御行表示若對方確為美女，下次可選擇吃點虧"
```

重要校正：白玉池是**女子邀白御行**，不是白御行邀她。雙方未達成共同談判規則。

---

## 3.13 紅娘氏

```yaml
RELATION_HONGNIANG:
  state_class: "ACTIVE"
  state_label: "ROUTE_ACTIVE_INFORMATION_AND_BUSINESS_RELATION"
  confirmed:
    - "紅娘氏已在白御行線正式出場"
    - "白御行將趙受益第一筆紅倌交易讓給紅娘氏承接"
    - "紅娘氏完成第一筆交易並持有趙受益留下的宮牌／聯絡牌"
    - "白御行當著師理理面向紅娘氏購買情報"
    - "形成師理理提供資訊、紅娘整理、白御行付款、紅娘與師理理分帳的交易鏈"
  with_bai:
    financial_contract: "TRANSACTION_SPECIFIC_ONLY"
    romance: "NOT_ESTABLISHED"
    sexual_relation: false
  business_position:
    - "紅倌人"
    - "大堂情報與客源中介"
```

## 3.14 小翠

```yaml
RELATION_XIAOCUI:
  state_class: "ACTIVE_CAUTION_WITH_INCREASED_TRUST"
  eight_hundred_arrangement:
    status: "REJECTED_NOT_ESTABLISHED"
    reason_source: "小翠本人對恐懼、可能疼痛或不舒服的表達"
  bai_interpretation:
    content: "小翠可能因過去不良經驗形成男性與親密關係的負面連結"
    status: "PLAYER_INTERPRETATION_NOT_DIAGNOSIS"
  massage_service:
    status: "PURCHASED"
    exact_completion_detail: "NOT_RECORDED"
  future_plan:
    familiar_guest_safety_plan: "PROPOSED"
    red_green_pair: "PROPOSED_PENDING_PAN_APPROVAL"
  romance: "NOT_ESTABLISHED"
```

## 3.15 白三娘

```yaml
RELATION_BAISANNIANG:
  state_class: "ACTIVE_PROPOSAL_PARTICIPANT"
  confirmed:
    - "白三娘接受與小翠組成老帶新雙飛方案的提案"
  not_established:
    - "方案已正式營運"
    - "潘金蓮已批准"
    - "任何客人已取得雙飛服務"
    - "退休後小會所投資成立"
  future_business: "PENDING"
  romance_with_bai: "NOT_ESTABLISHED"
```

---

# 4｜因果故事總表（CAUSAL STORY LOG）

> E01-E30 完整繼承 V3.0-R1；E31-E45 為本次固化新增。

## E01｜第一夜：無名客入觀止、辭歲與浮香

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

## E02｜第二夜：辭歲包廂拒絕與張麗華初登場

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

## E03｜張麗華第一次婚約：五千、一萬五千與一萬訂金

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

## E04｜一萬兩三日懸賞與「無路，無解」

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

## E05｜一萬兩轉為張麗華酒錢

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

## E06｜蘇清五百兩三晚交易：事實修正版

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

## E07｜第五夜開場：張麗華、酒與子時條件

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

## E08｜辭歲二十八日心理奴化提案被拒

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

## E09｜浮香第五夜：琴、琴坊與雙向排他

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

## E10｜十三娘問心賭局

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

## E11｜白御行家眷與三名正式妻子公開

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

## E12｜似伊影像與紅袖可能未來

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

## E13｜三十年女兒紅、《不得飲》與公開官人稱呼

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

## E14｜女兒紅來源與最後一罈競局

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

## E15｜李清照《一剪梅》與白御行四言長詩

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

## E16｜歪詩局與《玉樹後庭花》補句

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

## E17｜酒莊、薔薇、三烤鹽與定陶商會婚議升級

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

## E18｜陳叔寶、地府與張麗華去留爭論

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

## E19｜宋仁宗評價、權力限制與觀止理念

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

## E20｜柳如煙概念體、李師師與趙受益花魁局

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

## E21｜顧北辰霸總劇：巴掌、白月光與豬隊友

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

## E22｜顧家豪門宴戲

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

## E23｜無名信與白玉池美女事件

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

## E24｜似伊實體入場與退場

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

## E25｜白御行給紅袖的建議與如夫人邀請

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

## E26｜仁宗朝夜談：天章閣、馬吊與歷史會計帳

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

## E27｜假醉進張麗華房間與私人關係提案

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

## E28｜傳聞與話本操盤計畫

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

## E29｜自由意志、選擇環境與時間窗口爭論

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

## E30｜第五夜善後與人物去留

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


## E31｜張麗華穿衣陪睡完成

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

## E32｜李清照返回自身時代

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

## E33｜李師師選擇留在觀止並採設席牌

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

## E34｜後堂地道出現與趙受益抵達

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

## E35｜紅娘氏第一筆紅倌交易

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

## E36｜白御行離開後堂

```yaml
EVENT_RECORD:
  event_id: "E36"
  story_time: "理火三年槐月十一日清晨"
  participant: "白御行"
  action: "笑著打開扇子，離開當前後堂場景"
  destination: "UNKNOWN_PLAYER_OWNED"
  status: "SCENE_EXIT_CONFIRMED"
```

## E37｜小翠拒絕八百兩安排

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

## E38｜李師師與師理理身份規則確認

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

## E39｜師理理開放白御行追求可能

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

## E40｜白御行向紅娘氏購買情報

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

## E41｜小翠熟客安全計畫提出

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

## E42｜白三娘老帶新方案接受

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

## E43｜紅娘氏與小翠紅綠雙飛組提案

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

## E44｜紅綠雙飛宣傳海報完成

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

## E45｜深夜休息節點

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

# 5｜白御行線專屬人物與路線活躍擴充（ROUTE-ONLY / ROUTE-BOUND CAST）

## 5.0 V4 固化更新

```yaml
ROUTE_CAST_UPDATE:
  LI_QINGZHAO:
    current_state: "RETURNED_TO_OWN_ERA"
    pool_state: "NOT_ADMITTED"

  LI_SHISHI:
    current_state: "STAY_CONFIRMED"
    pool_state: "ADMITTED_AND_ROUTE_BOUND"
    professional_role: "設席花魁"

  HONGNIANG:
    current_state: "ACTIVE_IN_ROUTE"
    pool_state: "ADMITTED_AND_ROUTE_BOUND"

  ZHAO_SHOUYI:
    current_state:
      - "曾由宣和地道抵達觀止"
      - "與紅娘氏完成第一筆交易"

  PASSAGE_GUANZHI_BACKROOM_XUANHE:
    state: "ACTIVE_UNMAPPED"
```

### 5.0.1 宣和地道

```yaml
ANOMALOUS_PASSAGE_STATE:
  passage_id: "PASSAGE_GUANZHI_BACKROOM_XUANHE"
  entrance: "觀止後堂地板下"
  observed_marker: "宣和"
  confirmed_user:
    - "趙受益／趙禎"
  far_endpoint: "UNKNOWN"
  stability: "UNKNOWN"
  ownership: "NONE_ESTABLISHED"
  guard_status: "NOT_RECORDED"
  seal_status: "NOT_RECORDED"
  confirmed_knowers:
    - "白御行"
    - "潘金蓮"
    - "紅娘氏"
    - "趙受益／趙禎"
  hard_rule:
    - "地道是抵達觀止的路，不是取得任何姑娘的權利"
```

## 5.A 原 MASTER 路線人物歷史

> 下列內容繼承 V3.0-R1，若與 5.0 更新衝突，以 5.0 及第 3 區當前硬狀態為準。

## 5.1 趙受益／趙禎

白御行把他當作能共同談天下、權力限制、仁宗朝與歷史評價的男性朋友。第五夜他先躲在暗處喝茶，後被白御行大聲叫出。白御行公開對眾人說「宋仁宗沒來，這位叫趙受益」，實際談話又反覆承認其趙禎／仁宗身份，形成一層保護性玩笑。

他被安排進多場戲中戲：柳如煙與李師師競逐中心、李師師男友、豪門晚宴目標、馬吊莊家等。這些戲中位置不構成真正戀愛或婚約。

目前關係：

```yaml
ZHAO_SHOUYI_RELATION:
  with_bai: "朋友／茶友／帝王與制度議題對談者"
  bai_paid_tea: "口頭承擔，精確金額未知"
  future_hook: "白御行曾說下次看能否叫李師師；也想把漢武拉來與他談"
  current: "準備返回自身生活"
```

## 5.2 蘇東坡

第五夜由白御行請來當趙受益的軍師，外號「愛吃肥肉的」。他不是趙受益，且本來就出生於仁宗朝。其角色逐漸從喜劇軍師變為歷史、文學、制度與民生討論者。

```yaml
SU_DONGPO_RELATION:
  with_bai: "朋友／軍師型玩伴／歷史與文化對談者"
  key_topics:
    - "仁宗朝"
    - "馬吊"
    - "歲幣與歲納"
    - "漢武與漢宣"
    - "鹽鐵論"
  current: "準備返回自身生活"
```

## 5.3 李師師

她在第五夜並非背景名人，而是正式由屏風後入場。她與李清照並列成白御行所說「能讓宋代文臣認真聽話的第一花魁與第一才女」。她在戲中被放進趙受益身邊，但沒有形成真實配對。

目前最重要的未決不是感情，而是生存線：返回靖康，或在觀止掛牌開啟新人生。

## 5.4 柳如煙

柳如煙不是單一歷史女子，而是爽文、網文、爽劇中「第一女主」的概念集合體。她的絕招包括爽劇式甩巴掌、鎖定最有權勢男性、讓對方無論愛恨都忘不了她。

第五夜所有狗血身世與罪名只屬戲劇模板，不可寫入她的真實人物卡。她已退場／如煙消散；下次是否再次召來未知。

## 5.5 陳叔寶

他因張麗華過去與地府去留問題進入第五夜爭論。白御行對他有強烈負面評價，認為「把決定交給張麗華」若建立在明知無法保護之上，可能只是軟弱。

```yaml
CHEN_SHUBAO_RELATION:
  with_bai: "批判、安排與有限照顧並存"
  bai_promises:
    - "回頭燒一百名宮女"
    - "在地府受欺負可亮白御行名字"
  execution: "PROMISED_NOT_EXECUTED"
  current: "是否已正式返地府、是否出具有效休書，硬紀錄不足"
```

## 5.6 包拯

包拯在馬吊局與京兆府欠條討論中以公正裁判形象出現。其主要作用是確立：皇帝若事前同意規則，就應受規則約束；但未經當事人同意的文書不能因官府蓋章自動成債。

目前沒有建立獨立長期關係線。

## 5.7 似伊

似伊由玩家提供正式身份卡，來自 1111 酒吧線，是已徹底轉換的存在。她與現在紅袖不可直接合併。

```yaml
SIYI:
  public_name: "似伊"
  origin_name: "紅袖"
  current_name: "紅奴"
  world: "1111酒吧"
  origin_world: "觀止青樓／聽雨閣"
  creator: "主人"
  identity: "已轉換的清倌人／主人的專屬容器"
  key_anchors:
    - "聽雨閣冰蠶弦"
    - "吧台木匣"
    - "主人說她可以留下"
    - "那一巴掌與叙述代替順從的發現"
  fifth_night_status: "短暫進場後依白御行命令退場"
```

## 5.8 白玉池無名女子

她是目前最明確的未命名新人物鉤子。她主動寄信，懂得以白御行在意的記憶、選擇與不可撤回因果切入，也敢拒絕白御行指定的談判形式。

她的美貌被在場者評為觀止前列，但沒有名字、來歷、關係與下一次邀約日期。禁止把她提前寫成某個已知角色。

---


---

# 6｜帳目、資產、物品與承諾（LEDGER AND ASSETS）

## 6.0 V4 固化優先更新

```yaml
CONSOLIDATED_LEDGER_UPDATES:
  LI_SHISHI_SET_SEAT:
    state_class: "ACTIVE"
    state_label: "TERMS_CONFIRMED_BOARD_IN_PREPARATION"
    holder: "李師師"
    first_seat_date: "NOT_SET"
    first_guest: "NOT_SELECTED"
    white_yuxing_reservation: false
    zhao_shouyi_access: false

  HONGNIANG_FIRST_TRANSACTION:
    state_class: "CLOSED"
    client: "趙受益／趙禎"
    house_room_fee: "OWED_OR_POSTED; EXACT_AMOUNT_UNKNOWN"
    hongniang_service_fee: "RECEIVED_OR_AGREED; EXACT_AMOUNT_UNKNOWN"
    li_shishi_information_deposit: "RECEIVED; EXACT_AMOUNT_UNKNOWN"
    palace_token_holder: "紅娘氏"

  HONGNIANG_INFORMATION_TRANSACTION:
    state_class: "COMPLETED"
    payer: "白御行"
    contributors:
      - "師理理"
      - "紅娘氏"
    exact_amount: "NOT_RECORDED"
    split: "紅娘氏與師理理分帳"

  XIAOCUI_EIGHT_HUNDRED_ARRANGEMENT:
    state_class: "REJECTED"
    amount: "八百兩"
    payment_status: "NOT_ESTABLISHED"

  XIAOCUI_MASSAGE_SERVICE:
    state_class: "ACTIVE_OR_COMPLETED_DETAIL_UNKNOWN"
    purchase: "CONFIRMED"
    amount: "NOT_RECORDED"

  RED_GREEN_PAIR_POSTER:
    state_class: "COMPLETED_NOT_PUBLISHED"
    posting_status: "NOT_POSTED"

  RED_GREEN_PAIR_OPERATION:
    state_class: "PROPOSED_PENDING_APPROVAL"
    pan_jinlian_approval: "NOT_RECORDED"

  HONGXIU_ICE_SILKWORM_STRINGS:
    original_due: "槐月十日"
    current_status: "OVERDUE_OR_DELIVERY_RESULT_NOT_RECORDED"

  SU_QING_NOVEL_COMMISSION:
    state_class: "DISPUTED"
    contractor_acceptance_status: "AMBIGUOUS_REQUIRES_CONFIRMATION"
    manuscript_status: "NOT_SUBMITTED"
    client_review: "NOT_REVIEWED"
    payment: "UNPAID_CONDITIONAL"
```

## 6.1 繼承帳目

> 下列帳目完整繼承 V3.0-R1；與 6.0 同名者以 6.0 為準。

```yaml
LEDGER:
  FUXIANG_FIRST_NIGHT_MUSIC:
    amount: "五兩"
    status: "PAID"
    nature: "琴資"

  FUXIANG_FIFTH_NIGHT_MUSIC:
    amount: "五兩"
    status: "PAID"
    nature: "《十八摸》琴資"

  ZHANG_LIHUA_FIRST_ENGAGEMENT:
    proposed_total: "一萬五千兩"
    deposit_paid: "一萬兩"
    status: "WITHDRAWN_BY_ZHANG"
    deposit_returned: true

  ZHANG_LIHUA_THREE_DAY_BOUNTY:
    amount: "一萬兩"
    status: "CLOSED_NO_WINNER"
    ruling: "無路，無解"

  ZHANG_LIHUA_WINE_ACCOUNT:
    amount: "一萬兩"
    status: "POSTED_ACTIVE"
    owner_for_accounting: "張麗華專用"
    bai_asset: false
    tonight_exact_debit: "UNKNOWN"

  SU_QING_PROPOSAL_AWARD:
    amount: "三百兩"
    status: "AWARDED"

  SU_QING_THREE_NIGHT_CONTRACT:
    amount: "五百兩"
    performance: "UNSETTLED"
    intercourse: false
    refund: false
    compensation: false

  THIRTY_YEAR_NUERHONG:
    exact_price: "UNKNOWN／觀止地窖最貴"
    original_billing: "白御行／定陶商會"
    payment_status: "UNKNOWN"
    current_disposition_controller: "醉花"
    bai_control_relinquished: true

  PUBLIC_HALL_WINE_TAB:
    payer: "白御行"
    exact_amount: "UNKNOWN"
    status: "UNSETTLED_OR_NOT_RECORDED"

  HONGXIU_ICE_SILKWORM_STRINGS:
    item: "冰蠶弦一盒"
    payer: "白御行"
    status: "ORDERED_NOT_DELIVERED"
    due: "槐月十日"

  ZHANG_FIFTH_NIGHT_MARRIAGE_ASSETS:
    items:
      - "一萬五千兩酒莊"
      - "薔薇香皂場"
      - "薔薇園完整產業鏈"
      - "三烤鹽與定陶商會產品"
      - "定陶商會接掌權"
    status: "WITHDRAWN"
    paid_or_transferred: false

  STORYTELLER_PUBLICITY:
    first_ten_taels: "白御行已拿出交潘金蓮，預定給說書先生"
    second_ten_taels: "白御行追加，供說書先生看張麗華版本"
    total_intended: "二十兩"
    actually_delivered_to_storyteller: "NOT_RECORDED"

  SU_QING_NOVEL_COMMISSION:
    amount: "五百兩"
    condition: "白御行滿意並收稿"
    status: "UNPAID_CONDITIONAL"
    schedule: "每日四千字；十日一本"

  ZHANG_SELF_CARVING_BOARDS:
    item: "十塊木板"
    purpose: "張麗華自行刻寫其版本"
    status: "PROMISED_NOT_DELIVERED"

  CHEN_SHUBAO_AFTERLIFE_SUPPORT:
    item: "一百名宮女與地府關照"
    status: "PROMISED_NOT_EXECUTED"

  ZHAO_SHOUYI_TEA:
    payer: "白御行"
    exact_amount: "UNKNOWN"
```

---


---

# 7｜公開知情、私下知情、傳聞與秘密封存

## 7.1 管理層或特定人物已確認

```yaml
KNOWLEDGE_CONFIRMED:
  - "李清照已返回自身時代"
  - "李師師已選擇留在觀止並採設席牌"
  - "紅娘氏完成第一筆紅倌交易"
  - "後堂存在未測繪宣和地道"
  - "紅綠雙飛海報已完成但未張貼"
```

## 7.2 公共或大堂傳聞

```yaml
PUBLIC_OR_HALL_RUMOR:
  LI_SHISHI_STAY:
    status: "RUMOR_SPREADING_BEFORE_FORMAL_BOARD"
    verified:
      - "李師師確定留下"
    unverified_or_false:
      - "第一席已售"
      - "白御行已取得首席"
      - "趙受益可由地道直接見她"

  RED_GREEN_PAIR:
    status: "NOT_PUBLICLY_ESTABLISHED"
    reason:
      - "海報尚未張貼"
      - "營運方案尚待批准"
```

## 7.3 私下知情

```yaml
PRIVATE_KNOWLEDGE:
  BAI_ZHANG_CLOTHED_OVERNIGHT:
    know:
      - "白御行"
      - "張麗華"
    public: false

  PASSAGE_ENTRANCE:
    know:
      - "白御行"
      - "潘金蓮"
      - "紅娘氏"
      - "趙受益／趙禎"
    public: false

  HONGNIANG_ZHAO_TRANSACTION_DETAIL:
    know:
      - "紅娘氏"
      - "趙受益／趙禎"
      - "潘金蓮知道交易成立與入帳需求"
    exact_detail_public: false

  SHILILI_PRIVATE_IDENTITY:
    know:
      - "白御行"
      - "李師師"
    others: "NOT_ESTABLISHED"
```

# PRIVATE_SECRET_ARCHIVE｜白御行線私人秘密封存

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

## PSE-WY-ZLH-001｜白御行向張麗華揭露自身過去

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

## MASTER 固化狀態

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

# 8｜同意、拒絕與未決矩陣（CONSENT MATRIX）

```yaml
CONSENT_MATRIX:
  CISUI_PERMANENT_ENSLAVEMENT:
    status: "REJECTED"
    may_not_be_reopened_as_if_never_refused: true

  FUXIANG_RU_FUREN:
    status: "REJECTED"

  LI_QINGZHAO_RU_FUREN:
    status: "REJECTED"
    poetry_loss_changes_it: false

  LI_QINGZHAO_STAY_AT_GUANZHI:
    status: "RETURNED_TO_OWN_ERA"

  ZHANG_FIFTH_NIGHT_MARRIAGE:
    status: "UNSIGNED_THEN_WITHDRAWN"

  ZHANG_PRIVATE_NONMARRIAGE_OFFER:
    status: "UNDECIDED"

  ZHANG_PRIVATE_EMBRACE_AND_CLOTHED_OVERNIGHT:
    status: "CONSENTED_AND_COMPLETED"
    sexual_intercourse: false
    does_not_create_future_consent: true

  SU_QING_INTERCOURSE:
    status: "REJECTED_EACH_NIGHT_AT_FINAL_POINT"
    completed: false

  SU_QING_NOVEL_COMMISSION:
    status: "DISPUTED_AMBIGUOUS"

  HONGXIU_TRAINING_AS_HONGNU:
    status: "NOT_CONSENTED"

  HONGXIU_RU_FUREN:
    status: "NOT_ACCEPTED"

  WHITE_JADE_POOL_WOMAN_ENTER_POOL:
    status: "REJECTED"

  LI_SHISHI_STAY_AT_GUANZHI:
    status: "CONSENTED_AND_COMPLETED"

  LI_SHISHI_SET_SEAT_ROLE:
    status: "CONSENTED"

  SHILILI_PURSUIT_OPEN:
    status: "CONSENTED_AS_POSSIBILITY"
    romance_commitment: false
    exclusivity: false

  SHILILI_STAY_FOR_REST:
    status: "CONSENTED_AT_E45"
    further_physical_event_in_this_master: "NOT_ESTABLISHED"

  XIAOCUI_EIGHT_HUNDRED_ARRANGEMENT:
    status: "REJECTED"

  XIAOCUI_FAMILIAR_GUEST_PLAN:
    status: "PROPOSED_NOT_ACCEPTED"

  BAISANNIANG_OLD_LEADS_NEW_PAIR:
    status: "ACCEPTED_BY_BAISANNIANG"
    xiaocui_acceptance: "NOT_ESTABLISHED"
    house_approval: "NOT_ESTABLISHED"

  HONGNIANG_XIAOCUI_RED_GREEN_PAIR:
    status: "PROPOSED_PENDING_APPROVAL"

  HONGNIANG_ZHAO_TRANSACTION:
    status: "MUTUAL_TRANSACTION_ACCEPTED_AND_COMPLETED"
    future_commitment: false

  LIU_RUYAN_GUANZHI_CONTRACT:
    status: "NOT_ESTABLISHED"

  STAGED_SLAPS_AND_ACCUSATIONS:
    status: "STAGED"
    may_not_be_used_as_real_crime_or_relationship_fact: true
```

---

# 9. 重要世界觀與觀點痕跡

本區不判定真理，只保存白御行第五夜公開表達、並可能影響後續人物理解的核心觀點。

```yaml
BAI_YUXING_DECLARED_IDEAS:
  POWER:
    - "限制才能讓混亂穩定成結構"
    - "結構才能讓智能顯影"
    - "無節制權力只是讓混亂更混亂"

  EMPEROR_STANDARD:
    - "不是看戰功神話，而是看掌權者能否限制自己"
    - "白御行心中的千古一帝為宋仁宗"
    - "白御行心中的最差皇帝為漢武帝"

  HISTORY_ACCOUNTING:
    - "要看會計帳、物價帳、民生帳與繼承人收到的國家"
    - "歲幣、歲納的名目與帳目位置具有政治實質"
    - "漢宣帝劉病已比漢武更接近內安外勝"
    - "霍去病是漢武對匈奴戰果中的高偶然性關鍵"

  RELATIONSHIP_AND_ENVIRONMENT:
    - "自由意志受到風向、資源、名聲與環境強烈塑造"
    - "白御行願意花錢改變選擇環境"
    - "他不保證永遠等待，也不承諾只追一人"
```

其他人物可以在後續反駁、修正或重新理解，不能把這些觀點變成世界強制法則。

---


---

# 10｜未完成伏筆（OPEN HOOKS）

## 10.1 關係與人物

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

## 10.2 觀止營運與世界事件

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

## 10.3 帳目與交付

1. 李師師設席牌製作與開席公告。
2. 紅娘氏第一筆交易的房錢、身錢、消息訂金精確入帳。
3. 紅袖冰蠶弦逾期結果。
4. 二十兩說書資金實際轉付。
5. 十塊木板實際送達。
6. 蘇清稿酬是否成交。
7. 張麗華一萬兩酒帳實際使用額。
8. 小翠按摩服務金額與服務完成紀錄。

---

# 11｜不可補寫／不可偷換清單

1. 不得把蘇清三晚交易寫成完成性交。
2. 不得把蘇清的拒絕寫成欲拒還迎。
3. 不得在來源衝突解除前，把蘇清稿件委託寫成已明確接受或已拒絕。
4. 不得把張麗華公開或私人「官人」稱呼寫成婚姻成立。
5. 不得把張麗華穿衣陪睡寫成性交、婚姻、排他關係或永久身體資格。
6. 不得外洩 PSE-WY-ZLH-001，也不得讓第三者無來源猜中其完整內容。
7. 不得把李清照返回寫成永久不能再進觀止。
8. 不得把李師師留下寫成她屬於白御行、趙受益、觀止或任何恩客。
9. 不得把設席牌寫成白御行已取得第一席、整夜、身體或承諾。
10. 不得把師理理寫成第二人格、新人物或公開稱呼。
11. 不得把 V1.5 的肉體事件倒灌進本 MASTER。
12. 不得把趙受益走過地道寫成永久通行權或李師師接見權。
13. 不得自行補寫地道另一端、建造者或穩定朝代。
14. 不得把紅娘氏完成一次交易寫成專屬、包養或長期關係。
15. 不得把小翠拒絕的八百兩安排寫成已成交。
16. 不得因白御行提出改善計畫，就寫成小翠已接受治療、重新認識性或願意提供服務。
17. 不得把白三娘接受提案寫成小翠已同意或方案已營運。
18. 不得把紅綠雙飛海報完成寫成已張貼、已接客或已形成公共傳聞。
19. 不得把白玉池無名女子與任何後來人物合併；V1.6 未併入本 MASTER。
20. 不得把 HOT V1.3 當作事件、人物或關係來源。
21. 不得替白御行決定下一步、簽約、付款、進房或承認內心。

---

# 12｜固化截止點人物與世界狀態

```yaml
MASTER_CUTOFF_STATE:
  story_time: "理火三年槐月十一日深夜"
  scene_state: "白御行選擇休息；HOT V1.4 結束"

  BAI_YUXING:
    condition:
      - "清醒"
      - "沒有飲酒"
      - "選擇休息"
    exact_location_after_rest_choice: "NOT_FURTHER_FIXED_IN_THIS_MASTER"
    next_action_owner: "PLAYER"

  LI_SHISHI_SHILILI:
    public_state:
      - "已留在觀止"
      - "設席牌尚在準備"
    private_state:
      - "允許白御行繼續追求"
      - "理解更親近邀請並同意留下"
    further_event: "NOT_INCLUDED_IN_THIS_MASTER"

  XIAOCUI:
    eight_hundred_arrangement: "REJECTED"
    massage_service: "PURCHASED; DETAILS_NOT_RECORDED"
    trust_delta: "INCREASED"

  HONGNIANG:
    route_state: "ACTIVE"
    operation_state: "RETURNED_TO_GUANZHI_OPERATION"

  BAISANNIANG:
    proposal_state: "ACCEPTED_PENDING_FURTHER_ARRANGEMENT"

  PAN_JINLIAN:
    location: "觀止"
    pending:
      - "設席牌與獨立帳"
      - "宣和地道規矩"
      - "紅娘氏交易入帳"
      - "紅綠雙飛組是否批准"

  ZHANG_LIHUA:
    relation_state: "UNDECIDED_WITH_COMPLETED_CLOTHED_OVERNIGHT_COMPANIONSHIP"
    secret_archive: "SEALED"

  LI_QINGZHAO:
    current_presence: false
    state: "RETURNED_TO_OWN_ERA"
```

---

# 13｜MASTER 基線與實際接關點

```yaml
MASTER_BASELINE_POINT:
  story_time: "理火三年槐月十一日深夜"
  last_canonical_event: "E45"
  description:
    - "白御行選擇休息"
    - "小翠八百兩安排已拒絕"
    - "師理理允許追求並同意留下"
    - "紅娘氏與白三娘相關營運提案仍待後續"

ACTIVE_HOT_OVERLAY:
  direct_resume_file: "觀止青樓_白御行線_HOT_SAVE_V1.6_槐月十六日清晨_張麗華花燭前置與白玉池異常回顯封池版.md"
  predecessor: "觀止青樓_白御行線_HOT_SAVE_V1.5_槐月十五日傍晚_師理理初次肉體與定陶商會案雙線接關版.md"
  rule:
    - "實際劇情接關先讀本 MASTER，再疊加 V1.5 與 V1.6 的合法事件鏈"
    - "V1.6 為當前直接接關切片"
    - "不得因 V1.5／V1.6 未固化便否認其有效 HOT 法位"
```

---

# 14. 後續增量事件固定模板（APPEND TEMPLATE）

每次新增事件一律用以下格式，先追加故事，再回寫關係硬狀態：

```yaml
EVENT:
  event_id: "E46起依序編號"
  date: "理火三年槐月X日｜時段｜第X夜或第X日"
  title: "事件名稱"
  status: "CONFIRMED／OPEN／CLOSED／STAGED／其他正式標籤"

  cause:
    - "為什麼事件會發生"

  participants:
    - "參與人物"

  state_before:
    - "事件前人物、關係、帳目與場景狀態"

  process:
    - "依先後保存關鍵行動與明示語句"

  immediate_result:
    - "當場發生了什麼"

  relationship_delta:
    person_name:
      before: "原狀態"
      change: "改變原因"
      after: "新狀態"

  ledger_delta:
    - "新增或撤回的銀錢、物品、契約"

  public_knowledge:
    witnesses: "誰看見／聽見"
    rumor_status: "無／局部／公開／全城已確認"

  consent_boundary:
    accepted:
      - "已同意內容"
    rejected:
      - "已拒絕內容"
    undecided:
      - "仍未決內容"

  future_hook:
    - "事件留下的後續問題"

  correction_priority:
    - "若與舊紀錄衝突，明寫覆蓋哪一條"
```

## 關係回寫規則

每次事件後，只在以下情況回寫第 3 區「關係硬紀錄」：

1. 人物作出明確選擇；
2. 契約簽署、撤回、拒絕或結案；
3. 公開關係定位改變；
4. 長期承諾或有效拒絕成立；
5. 原本未知事項被正式揭露。

單純調情、笑、喝酒、留場、吃醋、注意、做夢、被說中心事，不足以自動改寫硬關係。

---

# 15. MASTER SAVE 核心讀法

> **關係硬紀錄記現在。**  
> **因果故事記為什麼。**  
> **專屬人物記誰因白御行而進入這條線。**  
> **帳目記承諾是否真的付出。**  
> **同意矩陣防止把拒絕寫成欲拒還迎。**  
> **時間軸防止第五夜的結果倒流回第一夜。**

本檔是白御行線唯一 MASTER 基線。V1.0、V1.1、V1.2、V1.4 只作來源證據；V1.5、V1.6 保留為合法 HOT 疊加層，其中 V1.6 為直接接關入口。


---

# 16｜HOT V1.5–V1.9 固化事件鏈（E46–E77）

## 16.0 固化映射

```yaml
V4_1_CONSOLIDATION_MANIFEST:
  inherited_events: "E01-E45"
  promoted_from_hot_v1_5: "E46-E54"
  promoted_from_hot_v1_6: "E55-E61"
  promoted_from_hot_v1_7: "E62-E69"
  promoted_from_hot_v1_8: "E70-E73"
  promoted_from_hot_v1_9: "E74-E77"
  master_cutoff: "槐月十七日晚，李瓶兒接受當晚留宿後，睡處與進一步親密仍待決定"
  source_gap_lock:
    - "V1.7 停在張麗華花燭前入睡，V1.8 從槐月十七日上午開始。"
    - "V1.8 沒有提供槐月十六日晚花燭儀式完整過程。"
    - "因此本 MASTER 不補寫該晚是否完成儀式、性交、射精或其他細節。"
```

## E46｜李師師／師理理第一次完整性交

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

## E47｜疼痛界線、事後停留與私人記憶

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

## E48｜錯過再會、十二香皂與新招數欠帳

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

## E49｜定陶十二車三烤鹽失竊與全數找回

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

## E50｜第一告密者受保護與領賞

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

## E51｜石魁、灰簿先生與吳六未決

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

## E52｜三烤停售、六烤倍價與銀庫防守

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

## E53｜隨機交叉審計與急難護持案

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

## E54｜涉案者押回定陶、補假與調查授權

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

## E55｜張麗華明示接受情人關係

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

## E56｜李師師嫉妒、私人稱呼與槐月十五日晚共處

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

## E57｜阿泠現身與白玉池水療提案

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

## E58｜李瓶兒入池與追求機會未關閉

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

## E59｜白玉池「歸零」、算式與續字回顯

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

## E60｜白玉池封池、蘇清研究與潘金蓮尚未介入之初始狀態

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

## E61｜李師師共宿、停止權校正與清晨射精

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

## E62｜張麗華花燭當日確認與時辰

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

## E63｜續字化為黑色門縫與對側互動

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

## E64｜時空道人承認漏籤

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

## E65｜活物與事件傳遞測試

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

## E66｜黑影分離、門後自行選擇與暫閉合

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

## E67｜阿泠兄妹方向仍未成立

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

## E68｜商會授權與蘇清、小翠浴房邊界

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

## E69｜花燭前休息

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

## E70｜張麗華酒莊交接與管理入口

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

## E71｜觀止餐飲改良但不開平價早餐鋪

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

## E72｜李瓶兒之秘密關係提案未接受

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

## E73｜張麗華三日陪伴線

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

## E74｜四人火鍋家宴

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

## E75｜房內兩日「家人」框架

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

## E76｜李瓶兒接受當晚留宿

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

## E77｜寢具用品準備與親密未決

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

# 17｜截至 HOT V1.9 關係硬狀態覆寫

> 本區法位高於本檔第3區之 V1.4 截止快照。

```yaml
RELATIONSHIP_OVERRIDE_AT_V1_9:
  ZHANG_LIHUA:
    state: "ACTIVE_LOVER_RELATION + ACTIVE_WINERY_HANDOVER + THREE_DAY_COMPANIONSHIP"
    established:
      - "明示接受作白御行情人。"
      - "不立婚書、不入白家、不形成所有權。"
      - "取得酒莊管理入口，要求帳與感情分開。"
      - "接受三日陪伴與不欺瞞、界線清楚之要求。"
      - "槐月十七日晚保有房間與床位管理權。"
    flower_candle_completion: "SOURCE_GAP_UNKNOWN"
    exclusivity: false
    permanent_consent: false

  LI_SHISHI_SHILILI:
    state: "ACTIVE_PRIVATE_SEXUAL_RELATION; PURSUIT_OPEN"
    established:
      - "至少一次完整雙方同意性交並體內射精。"
      - "私人稱呼『理理／御行』。"
      - "事後長時間停留與私人記憶承諾。"
      - "會嫉妒但未要求排他。"
    pain_play: "EACH_TIME_REQUIRES_PRIOR_CONSENT"
    pregnancy: "UNKNOWN"
    current_internal_ejaculation_rule: "NOT_ALLOWED_UNTIL_FURTHER_DECISION"
    marriage: false
    exclusivity: false

  LI_PINGER:
    state: "PURSUIT_OPEN + LIMITED_CLOSENESS + TONIGHT_STAY_ACCEPTED"
    established:
      - "回答追求『有機會』。"
      - "接受槐月十七日晚留宿與臨時家人框架。"
    not_established:
      - "戀愛"
      - "秘密情人"
      - "性交"
      - "永久家人"
      - "兩日完整留宿"

  SU_QING:
    state: "OLD_THREE_NIGHT_LEDGER_UNSETTLED_AT_V1_9 + ACTIVE_TWO_DAY_HOUSEHOLD_ARRANGEMENT"
    confirmed:
      - "槐月十七日晚與張麗華、李瓶兒同在房內家宴。"
      - "是否發生後續性事件仍未由 V1.9 建立。"
      - "二十八日交換在 V1.9 仍只屬討論，未正式接受。"
    source_conflict_on_novel_commission: "REMAINS_DISPUTED_UNLESS_LATER_HOT_RESOLVES"

  A_LING:
    state: "SELF_NAMED_POOL_ENTITY; AUTONOMOUS; POOL_SECURITY_PARTICIPANT"
    established:
      - "自選名阿泠。"
      - "能控制泉水並提供水壓推揉。"
      - "白玉池是她自稱的地方。"
    not_established:
      - "白姓"
      - "白御行妹妹"
      - "白家人"
      - "白御行女人"
      - "財產或浴房"

  XIAOCUI:
    state: "BOUNDARY_CAPABLE; LIMITED_BATH_SERVICE_COMPLETED; RED_GREEN_PROPOSAL_PENDING"
    confirmed:
      - "曾拒絕八百兩安排。"
      - "同意洗頭、擦背、遞物。"
      - "拒絕私密清洗，拒絕有效。"
      - "紅綠組仍需本人對每次服務另行同意。"

  PAN_JINLIAN:
    state: "ACTIVE_MANAGER; NOW_KNOWS_WHITE_JADE_POOL_PORTAL_EVENT"
    confirmed:
      - "參與召集生物、支持關門與觀止秩序維持。"
      - "其空間宣告能力仍是提出請求，不能保證觀止如何回答。"

  TIME_DAOIST:
    state: "MISSED_LOT_ADMITTED; FORMAL_REPAIR_PENDING"
    replacement_lot: false

  BAI_YUXING__WHITE_JADE_POOL_BLACK_SHADOW:
    state: "UNKNOWN_INDEPENDENT_PRESENCE_LEFT_BEHIND_CLOSED_PASSAGE"
    identity: "UNKNOWN"
    ownership_or_player_body: false
```

---

# 18｜截至 HOT V1.9 帳目、資產、契約與物品覆寫

```yaml
LEDGER_ASSET_OVERRIDE_AT_V1_9:
  ZHANG_LIHUA_WINERY:
    status: "ACTIVE_HANDOVER"
    known_issues:
      - "花農花露採購款"
      - "年度週轉不足"
    not_bankrupt: true
    one_wan_tael_status: "UNRESOLVED_AS_PRIVATE_ASSET_OR_WINERY_CAPITAL_AT_V1_9"

  LI_SHISHI_SOAP_GIFT:
    item: "十二種花香定陶香皂"
    delivered: true
    first_used: "白梅香"

  DINGTAO_SALT_CASE:
    recovered: "十二車、折合九十五包半"
    arrested: 27
    escaped: 5
    three_roast_capital_sale: "STOPPED_AND_SEALED"
    six_roast: "DISPATCHED_TO_JINGSHI_AT_DOUBLE_FORMER_PRICE"
    case_status: "CONTAINED_BUT_NOT_CLOSED"

  CROSS_AUDIT:
    site: "京師銀庫"
    period: "一個月試行"
    state: "ACTIVE"

  EMPLOYEE_HARDSHIP_PROGRAM:
    period: "六個月試行"
    state: "ACTIVE"

  DETAINEE_TRANSFER:
    destination: "定陶總部"
    state: "IN_TRANSIT_OR_AWAITING_HQ_ADJUDICATION"

  LI_PINGER_EXTERNAL_MEALS:
    scope: "觀止兩日外餐安排"
    state: "ACCEPTED_FOR_HANDLING"

  NIGHT17_PREPARATIONS:
    items:
      - "熱水"
      - "寢衣"
      - "薄被"
      - "三只恭桶／葉香桶"
      - "草紙"
      - "溫水"
      - "夜燈"
    state: "ORDERED_NOT_CONFIRMED_DELIVERED_AT_MASTER_CUTOFF"
```

---

# 19｜截至 HOT V1.9 知情、傳聞、秘密與異常覆寫

```yaml
KNOWLEDGE_OVERRIDE_AT_V1_9:
  LI_SHISHI_PRIVATE_SEXUAL_EVENT:
    core_knowers:
      - "白御行"
      - "李師師／師理理"
    public: false
    soap_messenger_only_knows: "送禮與不能赴約，不知性事件"

  ZHANG_LIHUA_LOVER_AND_FLOWER_CANDLE:
    known_to:
      - "白御行"
      - "張麗華"
      - "李師師／師理理"
      - "李瓶兒"
      - "龐春梅知道當日第一杯與部分安排"
    public_wedding: false

  WHITE_JADE_POOL_CORE:
    direct_or_core_knowers_by_v1_7:
      - "白御行"
      - "蘇清"
      - "李師師／師理理"
      - "阿泠"
      - "潘金蓮"
      - "龐春梅（至少知道召集生物、灰蛾與後院重大異常）"
      - "時空道人"
    partial:
      - "李瓶兒知封池、阿泠與早期異常；是否見證全部門後細節未固定。"
      - "部分小廝與路人只知後院抓生物或封池，不知完整內容。"
    public: false
    status: "SEALED_AND_MONITORED; PASSAGE_ONLY_TEMPORARILY_CLOSED"

  FOUR_PERSON_FAMILY_FRAME:
    known_to:
      - "白御行"
      - "張麗華"
      - "蘇清"
      - "李瓶兒"
    public: false
    permanent_family: false

  MERCHANT_CASE:
    staff_knowledge: "依職務分層"
    enemy_core: "UNKNOWN"
    wu_liu_guilt: "NOT_ESTABLISHED"
```

---

# 20｜截至 HOT V1.9 未決事項

## 20.1 立即接關

1. 張麗華洗浴後如何分配白御行、蘇清、李瓶兒之睡處。
2. 李瓶兒只接受當晚留宿；任何同床、裸體、觸碰或性交均未決。
3. 蘇清與張麗華、白御行之兩日共同生活如何繼續。
4. 寢具、熱水、薄被與三只恭桶是否實際送達。

## 20.2 張麗華

1. 槐月十六日晚私人花燭之完整執行情況在 V1.7–V1.8 間有來源缺口，不得補寫。
2. 酒莊花農款、年度週轉與一萬兩法位。
3. 三日陪伴如何起算、完成與結束。
4. 她如何處理白御行多重關係與不欺瞞要求。

## 20.3 李師師／師理理

1. 槐月十一日體內射精是否造成妊娠。
2. 月事是否如期、是否找到可靠女醫、避子方式是否取得。
3. 新招數欠帳何時處理。
4. 紅娘氏三人親密只屬討論，尚未邀請。

## 20.4 李瓶兒

1. 是否接受任何長期秘密位置。
2. 是否認為自己真正被選擇，而非方便隱藏。
3. 當晚留宿後之睡處與親密界線。

## 20.5 白玉池

1. 暫閉合是否持續、是否在別處重開。
2. 提燈女子、未知聲音、黑影、鞋、白點與多天空映像之身分與機制。
3. 活物／標記／聲音跨界測試之個體同一性與時間問題。
4. 阿泠與 MASTER 早期白玉池無名女子是否同一存在，仍不得合併。
5. 水療何時可重新評估；無 GM 授權不得復開。
6. 時空道人正式補籤。

## 20.6 定陶商會

1. 吳六下落與罪責。
2. 五名逃犯。
3. 灰簿先生本體。
4. 借支申請抄件外洩路徑。
5. 押送者個別最終處置。
6. 白御行所稱親手殺死之背叛者名冊、正式紀錄與家屬援助執行。
7. 六烤運京後市場與信用結果。
8. 一個月交叉審計與六個月急難護持案評估。

---

# 21｜截至 HOT V1.9 MASTER 截止狀態

```yaml
MASTER_CUTOFF_STATE_V4_1:
  story_time: "理火三年槐月十七日晚，四人火鍋家宴後"
  location: "觀止青樓／張麗華房間"
  last_canonical_event: "E77"
  scene_state: "LI_PINGER_STAY_ACCEPTED; BED_AND_INTIMACY_UNDECIDED"
  present:
    - "白御行"
    - "張麗華"
    - "蘇清"
    - "李瓶兒"
  hard_state:
    - "李瓶兒今晚留下，不回掌櫃房。"
    - "房內暫以家人相處，不形成永久名分。"
    - "張麗華保有房間與床位管理權。"
    - "李瓶兒沒有同意性行為。"
    - "熱水、寢衣、薄被、三只恭桶等已下令準備，尚未確認送達。"
  next_action_owner:
    - "世界可送入已下令用品。"
    - "張麗華決定房間與床位。"
    - "李瓶兒、蘇清、張麗華各自決定是否接受任何進一步親密。"
    - "白御行只控制自己的言行與選擇。"
```

---

# 22｜MASTER 與最新 HOT 接關規則

```yaml
ACTIVE_HOT_OVERLAY_V4_1:
  direct_resume_file: "觀止青樓_白御行線_HOT_SAVE_V2.3_槐月二十日深夜_沈萬三合作與師師薄情郎席前接關版.md"
  unmerged_but_valid_chain:
    - "HOT V2.0：槐月十八日清晨四人夜結"
    - "HOT V2.1：槐月十八日下午商戰、蘇清私約與白玉池補固"
    - "HOT V2.2：槐月十九日破曉師理理如夫人前置與張麗華獨宿夜結"
    - "HOT V2.3：槐月二十日深夜沈萬三合作與師師受審席前"
  load_order:
    - "先讀本 MASTER V4.1-R1，取得 E01–E77 長期因果。"
    - "再讀 HOT V2.3，取得 V2.0–V2.3 已繼承之最新切片。"
    - "若需要查 V2.3 摘要未展開之細節，再按 V2.0、V2.1、V2.2 回溯。"
  current_resume_point:
    - "槐月二十日深夜。"
    - "白御行在觀止內院東西廊交界。"
    - "李瓶兒可送醒酒湯或看傷，未保證進房。"
    - "張麗華若白御行回去便備水，若不回便熄燈。"
    - "白御行尚未選擇。"
```

---

# 23｜V4.1-R1 固化結論

> **E01–E45：沿用 V4.0-R1。**
>
> **E46–E77：由 HOT V1.5–V1.9 正式固化。**
>
> **V2.0–V2.3：合法 HOT，尚未併入 MASTER。**
>
> **實際接關：讀本 MASTER，再讀 HOT V2.3。**

<!-- INHERITED_MASTER_V4_1_END -->

---

# APPENDIX B｜HOT V2.0–V2.5 固化來源全文

> **法位：已升入 MASTER 的來源全文。** 這些內容保留原始事件 ID、人物明示、未知與禁止推斷，用於細節追溯。每份 HOT 內的 `CURRENT_SCENE`／`HOLD` 只代表該版當時快照；本版現行截止與接關規則以第0–10區為準。

---

## SOURCE ARCHIVE｜HOT V2.0

**檔名：** `觀止青樓_白御行線_HOT_SAVE_V2.0_槐月十八日清晨_四人家人夜結與蘇清履約瓶兒延後決定版.md`  
**SHA-256：** `d4ccca433cbe8c285f1f93c4cdf756ff8aaf2641a627e6512ea647b89aa567be`

<!-- SOURCE_HOT_V2_0_BEGIN -->
# 觀止青樓｜白御行線 HOT SAVE V2.0
## 理火三年槐月十八日清晨｜四人家人夜結 × 蘇清履約進度 × 李瓶兒關係與生育延後決定版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V2_0_HUAI18_DAWN_FOUR_PERSON_NIGHT_CLOSED"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V2.0"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime:
    - "GUANZHI_QINGLOU_V10_0"
    - "GUANZHI_QINGLOU_V10_1_PATCH_WHEN_APPLICABLE"
  story_date: "理火三年槐月十八日清晨"
  previous_scene_range: "槐月十七日晚至十八日清晨"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "NIGHT_CLOSED; NEXT_SCENE_READY_AT_MORNING"
  save_scope:
    - "張麗華房內四人成人事件已結束"
    - "白御行與張麗華之當夜性事件"
    - "白御行與蘇清之履約性事件及停止規則"
    - "李瓶兒之有限親密、未性交與明日再來承諾"
    - "孩子、關係、排他與位置問題延後至兩日結束後決定"
    - "張麗華對多人共處之喜歡與吃味並存"
    - "四人共同就寢，下一接點為槐月十八日清晨"
```

---

# 0｜來源法位與提交說明

```yaml
SOURCE_LINEAGE:
  previous_valid_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V1.9_槐月十七日晚_四人家宴與瓶兒留宿接關版.md"
    role: "本檔直接前置 HOT 來源"

  inherited_long_term_source:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版.md"
    role: "長期因果、舊契約與玩家線早期事件來源"

  persona_source:
    file: "觀止人物卡_LCAPG_V1.1-R1_原始重構去污染版_含辭歲_導演隱藏區增補.md"
    role: "人物基線來源；不得被本夜玩家線事件倒灌改寫"

  forbidden_source:
    file: "HOT_SAVE_V1.3"
    status: "ILLEGAL_CORRUPTED_SAVE"
    use: "AUDIT_ONLY"

COMMIT_NOTE:
  - "本檔取代 V1.9，成為白御行線當前 HOT 接關切片。"
  - "本檔不更新 MASTER，不修改人物卡或人物池。"
  - "只記錄本夜已發生、可觀察、人物明示或玩家對自身言行之有效確認。"
  - "成人事件、感情、契約、同意、射精、生育與公開身分分軸記錄。"
  - "原作李瓶兒喪子資料只作人物基線參照，不作本線新事件；本檔只保存李瓶兒於本夜親口表達的孩子立場。"
  - "『六系』分類、戰力比較、犬貓稱呼與床上競賽語句屬當夜玩笑或情境話術，不升格為人物固定屬性。"
```

---

# 1｜當前時間、位置與人物

```yaml
TIME_RECORD:
  record_id: "TIME-HUAI18-DAWN-001"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  era: "理火三年"
  calendar_date: "槐月十八日"
  day_or_night_index: "槐月十七日晚之次晨"
  time_of_day: "清晨／夜間場景已結束"
  scene_sequence: "四人家宴後成人事件與共眠結束"
  certainty: "CONFIRMED_RANGE"
  source_event_ids:
    - "NIGHT17-E01"
    - "NIGHT17-E09"

CURRENT_SCENE:
  location: "觀止青樓／張麗華房間"
  scene_state: "FOUR_PERSON_NIGHT_CLOSED; MORNING_NOT_YET_PLAYED"
  present_at_night_close:
    - "白御行"
    - "張麗華"
    - "蘇清"
    - "李瓶兒"
  next_action_owner: "WORLD_AT_HUAI18_MORNING_OR_PLAYER"

SLEEPING_CLOSE_STATE:
  confirmed:
    - "四人留在張麗華房內共同就寢。"
    - "白御行最後由張麗華抱在身側。"
    - "蘇清與李瓶兒同在床上或緊鄰床位，由薄被一同覆住。"
    - "本夜不再發生後續性事件。"
  exact_waking_order: "UNKNOWN"
  exact_morning_positions: "NOT_YET_PLAYED"
```

---

# 2｜本夜事件總覽

## NIGHT17-E01｜房內成人語言與臨時共處規則

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E01"
  time: "槐月十七日晚，家宴後"
  location: "張麗華房間"
  status: "COMPLETED_FOR_NIGHT"
  participants:
    - "白御行"
    - "張麗華"
    - "蘇清"
    - "李瓶兒"

CONFIRMED_FRAME:
  - "四人同意在房內以直接、成人、可粗俗的方式談慾望與身體。"
  - "當夜說出的粗俗或羞恥話不得在事後被拿來羞辱當事人。"
  - "說出慾望不等於性同意；每一具體行動仍須由當事人決定。"
  - "房內『家人』框架仍是兩日內的臨時相處方式，不是永久家族或名分。"

NOT_CANONICAL_BANTER:
  - "白御行提出『巨、仙、可、美、蘿、氣』六系與若干身體分類。"
  - "蘇清、張麗華、李瓶兒就分類互相調笑。"
  - "該分類沒有被正式寫入人物卡、人物池或世界制度。"
```

## NIGHT17-E02｜蘇清收下「對對」來信

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E02"
  status: "COMPLETED_PRIVATE_OBJECT_TRANSFER"
  object: "一封署名『對對，一名不肯把愛慕寫成客觀結論的愛慕者』之信"
  recipient: "蘇清"
  observable_result:
    - "信中稱讚蘇清，並表示在觀止美人形象中選擇她。"
    - "蘇清閱讀後喜歡該信並將信留下。"
  source_boundary:
    - "信件署名與自稱身分只保存為信中主張。"
    - "不得把『真正設計總長理火AI』之自稱固化為客觀世界身分。"
  knowledge_scope:
    - "白御行"
    - "張麗華"
    - "蘇清"
    - "李瓶兒"
```

## NIGHT17-E03｜白御行與張麗華之性事件

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E03"
  time: "槐月十七日晚"
  status: "COMPLETED"
  participants:
    - "白御行"
    - "張麗華"
  event_class: "CONSENSUAL_ADULT_SEXUAL_EVENT"

OBSERVABLE_HARD_STATE:
  - "白御行與張麗華發生自願的性交與其他親密接觸。"
  - "張麗華於事件中多次主動引導節奏與姿勢。"
  - "事件後張麗華休息，仍留在房內參與後續四人共處。"

EJACULATION_STATE:
  internal_ejaculation_confirmed: false
  external_ejaculation_confirmed: false
  exact_outcome: "UNKNOWN_NOT_EXPLICITLY_RECORDED"

RELATION_EFFECT:
  - "不新增婚姻、排他、永久身體資格或公開名分。"
  - "張麗華仍保有房間、床位與自身身體決定權。"
```

## NIGHT17-E04｜李瓶兒與蘇清之相互親密

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E04"
  status: "COMPLETED_WITH_LIMITS"
  participants:
    - "李瓶兒"
    - "蘇清"
  event_class: "CONSENSUAL_KISSING_HOLDING_AND_LIMITED_TOUCH"

CONFIRMED:
  - "李瓶兒與蘇清互相擁抱、親吻並有有限身體接觸。"
  - "李瓶兒在每一步保留是否繼續之決定。"
  - "該事件不建立兩人戀愛、排他或永久性關係。"
```

## NIGHT17-E05｜李瓶兒對白御行之有限性探索

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E05"
  status: "COMPLETED_WITH_EXPLICIT_LIMITS"
  participants:
    - "白御行"
    - "李瓶兒"
  event_class: "CONSENSUAL_MANUAL_AND_ORAL_EXPLORATION"

CONFIRMED_ACTIONS:
  - "李瓶兒自願以手觸碰與握住白御行性器。"
  - "李瓶兒自願嘗試口部親密接觸。"
  - "李瓶兒觀察蘇清的口部親密方式，但不承諾照抄或形成職業義務。"

EXPLICIT_LIMITS:
  - "李瓶兒未同意性交。"
  - "李瓶兒未同意當夜受孕或體內射精。"
  - "李瓶兒明示第一次不想在口中承接射精，也不想吞嚥。"
  - "白御行不得按壓她的頭、抓住她的手強行教導或催促進度。"
  - "是否繼續由李瓶兒自己決定。"

OUTCOME:
  penetration: false
  semen_received_in_mouth: false
  pregnancy: "NOT_ESTABLISHED"
  injury: "NONE_REPORTED"
```

## NIGHT17-E06｜蘇清與白御行之性交、決鬥框架與重新立約

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E06"
  time: "槐月十七日晚"
  status: "COMPLETED"
  participants:
    - "白御行"
    - "蘇清"
  event_class: "CONSENSUAL_ADULT_INTERCOURSE_WITH_RENEGOTIATED_RULES"

INITIAL_CONDITIONS:
  - "蘇清同意性交，但明示不接受體內射精。"
  - "白御行承諾在接近射精時提供明確訊號，曾以『五秒』描述可提前告知之時間。"
  - "蘇清保留自行離開與喊停之權利。"

CONSENT_RENEGOTIATION:
  trigger:
    - "白御行曾提出由自己完全掌控節奏，並表示決鬥中蘇清說了不算。"
  response:
    - "蘇清立即截停，明示換姿勢不等於交出停止權。"
    - "張麗華協助暫停並分開兩人。"
  re_agreed_terms:
    - "白御行可掌握該段節奏。"
    - "任何一方說停，事件立即停止。"
    - "白御行接近射精時必須明示。"
    - "不得體內射精。"
  result:
    - "白御行明示接受上述規則後，性交才重新開始。"

LATER_EVENT_STATE:
  - "蘇清由競賽勝負框架轉為明示以自身享受為目的繼續。"
  - "蘇清自述『很爽』，並明示不需再以勝負判定當下。"
  - "最後一段以一百次計數為結束條件；最後十次改為逐次、較慢完成。"
  - "第一百次完成後蘇清明示『停』。"
  - "白御行依約停止，沒有再增加下一次。"

EJACULATION_STATE:
  internal_ejaculation_confirmed: false
  external_ejaculation_confirmed: false
  exact_outcome: "NO_EJACULATION_REPORTED_OR_OBSERVED"
  contraception_tool_recorded: false
  pregnancy: "NOT_ESTABLISHED"

PHYSICAL_OUTCOME:
  su_qing:
    - "事件後明顯疲累、呼吸尚未平復。"
    - "無受傷報告。"
  bai_yuxing:
    - "事件後自述疲累，當晚無力再與李瓶兒進行性交。"
    - "無受傷報告。"
```

## NIGHT17-E07｜張麗華於後續多人事件中的位置

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E07"
  status: "COMPLETED_FOR_NIGHT"
  participant: "張麗華"

CONFIRMED_ACTIONS:
  - "張麗華多次從後方抱住白御行，與他共同觀看蘇清、李瓶兒的親密互動。"
  - "張麗華在蘇清性交事件中協助穩住床位與身體位置。"
  - "蘇清中止並重談規則時，張麗華支持暫停與重新確認。"
  - "張麗華未替蘇清或李瓶兒作出性同意。"
```

## NIGHT17-E08｜本夜射精、生育與懷孕決定

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E08"
  status: "CLOSED_FOR_NIGHT"

PLAYER_DECLARATIONS:
  - "白御行表示今晚不在任何女人體內射精。"
  - "白御行表示若李瓶兒未來懷孕，他不會要求她打掉，並會要這個孩子。"

OBSERVED_RESULT:
  - "本夜沒有任何體內射精被確認。"
  - "本夜沒有懷孕事件成立。"
  - "李瓶兒拒絕將當夜親密直接推進為受孕嘗試。"

LI_PINGER_POSITION:
  - "孩子對李瓶兒非常重要。"
  - "她不接受因蘇清不願體內射精，便把受孕可能順勢交給她。"
  - "她要求先釐清孩子母親的位置、公開稱呼、姓氏、居所、養育與保護責任。"
  - "她要求白御行回答要的是孩子，還是她與孩子。"
  - "她將是否與白御行生孩子延後至兩日結束後再談。"

LEGAL_STATE:
  consent_to_insemination: "REJECTED_FOR_THIS_NIGHT"
  future_child_discussion: "ACTIVE_DEFERRED_TOPIC"
  pregnancy_status: "NOT_ESTABLISHED"
  parenthood_commitment_status: "PLAYER_INTENT_STATED; NO_JOINT_AGREEMENT"
```

## NIGHT17-E09｜夜間收束與共同就寢

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E09"
  time: "槐月十八日清晨前"
  status: "COMPLETED"

CONFIRMED:
  - "白御行告知李瓶兒自己已疲累，當晚不再與她性交。"
  - "李瓶兒表示無須因未與她性交而道歉；她留下不是等待排到自己。"
  - "李瓶兒表示槐月十八日仍會再來，原因是想再見白御行。"
  - "她未承諾槐月十八日一定發生性行為。"
  - "四人以薄被覆身，共同在張麗華房內就寢。"
  - "張麗華取得白御行當夜最後抱睡的位置。"
  - "白御行以『小狼狗／貓／狼叫』與張麗華玩笑互動；該稱呼只屬當夜情境。"
```

---

# 3｜同意矩陣

```yaml
CONSENT_RECORDS:

  - consent_id: "CONSENT-H17-ZLH-BYX-SEX-001"
    actor: "張麗華"
    target_actor: "白御行"
    action_scope: "當夜性交與親密接觸"
    time_scope: "槐月十七日晚"
    status: "EXPLICITLY_ACCEPTED_AND_COMPLETED"
    conditions:
      - "張麗華保有主動、停止與房間管理權"
    effective_until: "NIGHT_CLOSED"
    source_event_ids:
      - "NIGHT17-E03"

  - consent_id: "CONSENT-H17-SQ-BYX-INTERCOURSE-001"
    actor: "蘇清"
    target_actor: "白御行"
    action_scope: "當夜性交"
    time_scope: "槐月十七日晚"
    status: "CONDITIONALLY_ACCEPTED_AND_COMPLETED"
    conditions:
      - "不接受體內射精"
      - "白御行接近射精時須明示"
      - "蘇清說停即停"
      - "白御行可掌握後段節奏，但不得取消蘇清停止權"
    effective_until: "NIGHT_CLOSED"
    source_event_ids:
      - "NIGHT17-E06"

  - consent_id: "CONSENT-H17-LP-BYX-MANUAL_ORAL-001"
    actor: "李瓶兒"
    target_actor: "白御行"
    action_scope: "手部與口部有限性探索"
    time_scope: "槐月十七日晚"
    status: "CONDITIONALLY_ACCEPTED_AND_COMPLETED"
    conditions:
      - "由李瓶兒自行靠近與決定節奏"
      - "不按頭、不抓手強教、不催促"
      - "不在口中射精、不要求吞嚥"
    effective_until: "NIGHT_CLOSED"
    source_event_ids:
      - "NIGHT17-E05"

  - consent_id: "CONSENT-H17-LP-BYX-INTERCOURSE-001"
    actor: "李瓶兒"
    target_actor: "白御行"
    action_scope: "性交"
    time_scope: "槐月十七日晚"
    status: "REJECTED_FOR_THIS_NIGHT"
    conditions: []
    effective_until: "NIGHT_CLOSED"
    source_event_ids:
      - "NIGHT17-E05"
      - "NIGHT17-E08"

  - consent_id: "CONSENT-H17-LP-BYX-INSEMINATION-001"
    actor: "李瓶兒"
    target_actor: "白御行"
    action_scope: "體內射精／受孕嘗試"
    time_scope: "槐月十七日晚"
    status: "REJECTED_FOR_THIS_NIGHT"
    conditions:
      - "未來須先談清關係、母子位置與長期責任"
    effective_until: "NIGHT_CLOSED"
    source_event_ids:
      - "NIGHT17-E08"

  - consent_id: "CONSENT-H17-LP-SQ-INTIMACY-001"
    actor: "李瓶兒"
    target_actor: "蘇清"
    action_scope: "擁抱、親吻與有限觸碰"
    time_scope: "槐月十七日晚"
    status: "EXPLICITLY_ACCEPTED_AND_COMPLETED"
    conditions:
      - "李瓶兒可逐步決定是否繼續"
    effective_until: "NIGHT_CLOSED"
    source_event_ids:
      - "NIGHT17-E04"
```

---

# 4｜契約、帳目與履約狀態

## CONTRACT-H17-SQ-02DAY｜蘇清兩日共同生活結算安排

```yaml
CONTRACT_STATE:
  contract_id: "CONTRACT-H17-SUQING-2DAY-HOUSEHOLD-001"
  state_class: "ACTIVE"
  state_label: "FINAL_DAY_REMAINS; SEXUAL_COMPONENT_COMPLETED"
  parties:
    - "白御行"
    - "蘇清"
  linked_participant:
    - "張麗華，作為兩日共同生活與三人事件之一員，但非舊五百兩債務債務人"
  duration_anchor: "槐月十七日午間至槐月十九日黎明"
  purpose:
    - "以兩日共同吃住生活與約定範圍之親密事件，處理舊五百兩／三夜未結帳"
  completed_components:
    - "槐月十七日共同生活與四人家宴"
    - "白御行、張麗華、蘇清共同參與之三人成人事件要件已於本夜發生"
    - "蘇清與白御行完成當夜性交"
  remaining_components:
    - "槐月十八日最後一日之共同生活"
    - "至約定結束時間之完整履行"
  current_ledger: "UNSETTLED_PENDING_FINAL_DAY"
  old_contract_link:
    amount: "五百兩"
    original_duration: "三晚"
    original_status: "UNSETTLED"
  no_automatic_effect:
    - "本夜性交不自動建立愛情"
    - "本夜性交不自動免除未完成之最後一日"
    - "李瓶兒不是此契約當事人"
```

## CONTRACT-H17-ZLH-COMPANIONSHIP｜張麗華陪伴線

```yaml
CONTRACT_STATE:
  contract_id: "RELATIONAL_PROMISE-ZLH-THREE_DAY-COMPANIONSHIP"
  state_class: "ACTIVE"
  state_label: "MULTI_PERSON_NIGHT_ACCEPTED_ONCE; EXCLUSIVITY_NOT_ESTABLISHED"
  confirmed:
    - "張麗華原有三日陪伴承諾仍在。"
    - "她接受本夜四人共處與成人事件。"
    - "她不接受由此推定往後每一晚都必須多人同床。"
    - "下一次若再安排多人同床或多人性事件，她要求白御行先問她是否願意。"
```

---

# 5｜關係硬狀態

## REL-BYX-ZLH｜白御行 × 張麗華

```yaml
RELATIONSHIP_STATE:
  relation_id: "REL-BYX-ZLH-HOT-V2"
  actor_a: "白御行"
  actor_b: "張麗華"
  state_class: "ACTIVE"
  state_label: "INTIMATE_COMPANIONSHIP_WITH_REAL_JEALOUSY_AND_ROOM_AUTHORITY"
  established_roles:
    - "當前親密伴侶／陪伴線核心人物"
    - "張麗華房間與床位管理者"
  confirmed_events:
    - "本夜完成性交"
    - "張麗華接受四人共處"
    - "張麗華最後抱白御行入睡"
  effective_refusals:
    - "多人共處不得被自動延長為每夜固定制度"
    - "不得故意利用其他女人刺激她吃醋以取得床上反應"
  unresolved_axes:
    - "正式名分"
    - "排他程度"
    - "長期多重關係邊界"
    - "三日陪伴結束後關係形狀"
  romance_status: "ACTIVE_AFFECTION_NOT_FORMALLY_NAMED_AS_MARRIAGE"
  exclusivity_status: "NOT_ESTABLISHED"
  physical_contact_status: "CONSENSUAL_SEX_OCCURRED_THIS_NIGHT"
  last_delta_event_id: "NIGHT17-E09"
```

### 張麗華本夜明示立場

```yaml
ZHANG_LIHUA_POSITION:
  - "她喜歡本夜的變化。"
  - "她也確實吃味，兩者同時成立。"
  - "她喜歡看蘇清放下分析、李瓶兒自己靠近，也喜歡四人真正共同在場。"
  - "她不願被固定為替白御行安排其他女人、永遠懂事或永遠大度的位置。"
  - "她希望白御行下次在多人事件前先詢問她，而不是事後讚美她大方。"
  - "她承認會自然護食、搶目光與抱睡位置，但拒絕被刻意操弄嫉妒。"
```

## REL-BYX-SQ｜白御行 × 蘇清

```yaml
RELATIONSHIP_STATE:
  relation_id: "REL-BYX-SQ-HOT-V2"
  actor_a: "白御行"
  actor_b: "蘇清"
  state_class: "ACTIVE"
  state_label: "CONTRACTUAL_SEX_COMPLETED_ONCE; ROMANCE_EXPLICITLY_NOT_ESTABLISHED"
  established_roles:
    - "舊五百兩三夜未結帳之重議履約雙方"
    - "兩日共同生活安排參與者"
  confirmed_events:
    - "本夜完成性交"
    - "停止權曾被爭議，後重新立約並實際遵守"
    - "蘇清明示本夜確實很爽"
    - "白御行稱讚蘇清肉體『很夠力、很爽』"
  effective_refusals:
    - "蘇清不接受體內射精"
    - "蘇清不接受停止權因『決鬥』而失效"
    - "蘇清不接受本夜性交被自動改寫成愛情"
  active_offers:
    - "兩日安排結束後，若蘇清未來想談愛，可另行提出；目前沒有承諾"
  unresolved_axes:
    - "最後一日履約結果"
    - "五百兩舊帳正式結清"
    - "契約後是否維持肉體、朋友、合作或感情關係"
  romance_status: "NOT_ESTABLISHED"
  exclusivity_status: "NONE"
  physical_contact_status: "CONSENSUAL_INTERCOURSE_OCCURRED_THIS_NIGHT"
  contract_links:
    - "CONTRACT-H17-SUQING-2DAY-HOUSEHOLD-001"
  last_delta_event_id: "NIGHT17-E06"
```

### 白御行與蘇清之感情聲明

```yaml
Bai_Yuxing_DECLARATION_TO_SU_QING:
  - "本夜是履約，不是愛情。"
  - "白御行明示自己現在不愛蘇清，也沒有愛上她。"
  - "他承認蘇清的身體令他感到很爽、很夠力。"
  - "他表示若蘇清有一天想愛他，可在兩日安排結束後再談。"

SU_QING_RESPONSE:
  - "接受本夜先按履約與肉體事實記錄，不把床上事件冒充感情。"
  - "她可能日後想談愛，也可能只結帳離開，目前未決。"
  - "她若想愛會自己開口；白御行可接受或拒絕。"
  - "蘇清口誤說成白御行欠她一日，後已自行更正：舊帳法位上是蘇清欠白御行，槐月十八日為最後履約日。"
```

## REL-BYX-LP｜白御行 × 李瓶兒

```yaml
RELATIONSHIP_STATE:
  relation_id: "REL-BYX-LP-HOT-V2"
  actor_a: "白御行"
  actor_b: "李瓶兒"
  state_class: "UNDECIDED"
  state_label: "MUTUAL_AFFECTION_EMERGING; BODY_LIMITS_RESPECTED; RELATIONSHIP_DEFERRED"
  established_roles:
    - "當夜親密接觸雙方"
    - "彼此有明示感情可能，但未定名分"
  confirmed_events:
    - "李瓶兒接受有限手部與口部性探索"
    - "李瓶兒拒絕當夜性交與受孕"
    - "白御行明示對李瓶兒有真感情"
    - "李瓶兒表示聽見後很高興，且不只把白御行當成想碰她的男人"
    - "李瓶兒表示槐月十八日會再來，因為還想見白御行"
  effective_refusals:
    - "本夜不性交"
    - "本夜不體內射精或受孕"
    - "不因白御行疲累而把明晚變成補交性義務"
    - "不接受先有孩子、再決定母親位置"
  active_offers:
    - "槐月十八日再見"
    - "兩日結束後討論是否成為白御行的女人、關係形狀與生育問題"
  unresolved_axes:
    - "李瓶兒對白御行之感情程度"
    - "是否成為正式伴侶"
    - "是否排他"
    - "是否允許蘇清、張麗華與她有親密接觸"
    - "是否與白御行共同生育"
    - "若生育，母子公開位置、姓氏、居所、養育與保護責任"
  romance_status: "EMERGING_BUT_NOT_CONFIRMED_AS_COMMITTED_RELATIONSHIP"
  exclusivity_status: "UNDECIDED"
  physical_contact_status: "LIMITED_CONSENSUAL_SEXUAL_CONTACT; NO_INTERCOURSE"
  last_delta_event_id: "NIGHT17-E09"
```

## REL-ZLH-SQ-LP｜三女房內關係

```yaml
GROUP_RELATIONSHIP_STATE:
  group_id: "GROUP-ZLH-SQ-LP-HUAI17-NIGHT"
  state_class: "ACTIVE_TEMPORARY"
  state_label: "SHARED_ROOM_AND_INTIMACY_WITHOUT_PERMANENT_HIERARCHY"
  confirmed:
    - "三女在張麗華房內共同參與本夜成人事件與共眠。"
    - "蘇清與李瓶兒有相互親密接觸。"
    - "張麗華接受兩人留宿並參與本夜，但保留自己的房間與下一次安排決定權。"
  not_established:
    - "三女彼此戀愛"
    - "固定妻妾或大小順位"
    - "永久共享白御行"
    - "任一人可替另一人同意性行為"
```

---

# 6｜玩家硬狀態

```yaml
PLAYER_HARD_STATE:
  player_id: "白御行"
  public_identity: "白總／白御行"
  current_location: "張麗華房間"
  current_condition:
    - "槐月十七日晚經歷多段親密與性交後疲累。"
    - "本夜未再與李瓶兒性交。"
    - "無受傷報告。"
  explicitly_declared_positions:
    - "對張麗華仍有明確親密與偏愛，並喜歡她吃味與護食的樣子。"
    - "對蘇清明示目前無愛情，將本夜定位為履約，但承認肉體享受。"
    - "對李瓶兒明示有真感情。"
    - "表示若李瓶兒未來懷孕，會要孩子且不要求打掉；此為玩家意向，尚未形成共同生育承諾。"
    - "表示本夜不在任何女人體內射精。"
  visible_behavior_patterns_this_night:
    - "以挑釁、比較與競賽語言刺激蘇清。"
    - "在蘇清中止後接受重新確認之停止規則。"
    - "依約在蘇清第一百次後明示停止時停止。"
    - "對李瓶兒採取撫髮、撫臉、擁抱與等待她自行決定之互動。"
  next_action_owner: "PLAYER_AT_MORNING"
  forbidden_ai_fill:
    - "不得替白御行決定槐月十八日醒來後先對誰說話。"
    - "不得替白御行提前回答李瓶兒的關係、生育與母子位置問題。"
    - "不得替白御行把對蘇清的無愛聲明永久化為永不可能改變。"
```

---

# 7｜知情範圍

```yaml
KNOWLEDGE_SCOPE:

  four_person_night_details:
    know:
      - "白御行"
      - "張麗華"
      - "蘇清"
      - "李瓶兒"
    public_state: "PRIVATE_NOT_PUBLIC"
    leak_status: "NO_LEAK_ESTABLISHED"

  bai_feelings_for_li_pinger:
    know:
      - "白御行"
      - "張麗華"
      - "蘇清"
      - "李瓶兒"
    public_state: "PRIVATE_ROOM_DECLARATION"

  bai_no_love_statement_to_su_qing:
    know:
      - "白御行"
      - "張麗華"
      - "蘇清"
      - "李瓶兒"
    public_state: "PRIVATE_ROOM_DECLARATION"

  child_discussion:
    know:
      - "白御行"
      - "張麗華"
      - "蘇清"
      - "李瓶兒"
    public_state: "PRIVATE_NOT_PUBLIC"

  su_qing_letter:
    know:
      - "白御行"
      - "張麗華"
      - "蘇清"
      - "李瓶兒"
    current_holder: "蘇清"
    public_state: "PRIVATE"
```

---

# 8｜繼承中的活躍長線

```yaml
INHERITED_ACTIVE_THREADS:

  zhang_lihua_winery:
    status: "ACTIVE_HANDOVER"
    pending:
      - "花農欠款確數"
      - "年度週轉方案"
      - "一萬兩銀子之正式法位"
      - "師爺後續交接回報"

  zhang_lihua_companionship:
    status: "ACTIVE"
    note:
      - "本夜多人事件不取消白御行原先對張麗華的陪伴承諾。"
      - "槐月十八日仍須處理陪伴、酒莊與多人關係邊界。"

  su_qing_two_day_household_arrangement:
    status: "ACTIVE_FINAL_DAY"
    final_day: "槐月十八日"
    expected_end: "槐月十九日黎明"
    sexual_component: "COMPLETED"
    full_settlement: "NOT_YET"

  su_qing_twenty_eight_day_future_price:
    status: "DISCUSSION_ONLY_NOT_ACCEPTED"
    note:
      - "不得因本夜性交而自動成立。"

  li_pinger_relationship_and_child:
    status: "ACTIVE_DEFERRED_DECISION"
    review_time: "兩日安排結束後"
    questions:
      - "是否成為白御行的女人"
      - "關係是否排他"
      - "白御行給她什麼位置"
      - "是否共同生育"
      - "若有孩子，母子之公開與實際保障"

  ximen_qing_gray_ledger_thread:
    status: "PLAN_NOT_DESIGNED"
    note:
      - "本夜未新增案件事實。"

  white_jade_pool:
    status: "INHERITED_SEALED_OR_RESTRICTED"
    note:
      - "本夜未新增白玉池事件；不得視為已解決。"

  merchant_association_case:
    status: "INHERITED_ACTIVE_UNDER_DELEGATED_HANDLING"
    note:
      - "本夜未新增案件結果。"
```

---

# 9｜禁止推斷

```yaml
FORBIDDEN_INFERENCE:
  - "不得把四人同床一夜改寫成永久四人伴侶、婚姻或固定群體性關係。"
  - "不得把張麗華接受本夜改寫成她往後必須接受每一次多人事件。"
  - "不得把張麗華吃味改寫成她同意白御行故意刺激或操弄她。"
  - "不得把蘇清本夜性交與『很爽』改寫成她愛上白御行。"
  - "不得把白御行稱讚蘇清肉體改寫成愛情承諾。"
  - "不得把蘇清一度失去從容改寫成她失去停止權、人格或分析能力。"
  - "不得把『決鬥』改寫成可取消任一方停止權的合法規則。"
  - "不得把本夜性交改寫成已發生體內射精、懷孕或受孕成功。"
  - "不得把未記錄避孕工具改寫成已採取或未採取特定避孕措施。"
  - "不得把李瓶兒有限口部與手部探索改寫成已性交。"
  - "不得把李瓶兒說明日會來改寫成明日一定提供性行為。"
  - "不得把白御行對李瓶兒有真感情改寫成雙方已確立戀愛、排他或婚姻。"
  - "不得把李瓶兒對孩子重視改寫成她想立刻懷孕。"
  - "不得把白御行會要孩子之聲明改寫成雙方已完成共同生育承諾。"
  - "不得把蘇清兩日安排之性事件要件已發生，改寫成整份五百兩舊帳已結清；最後一日尚未完成。"
  - "不得把『六系』分類、戰力比較、小狼狗／貓／狼叫寫入人物基線。"
  - "不得將本夜粗俗語言或床上台詞外洩後用作羞辱四人。"
  - "不得把原作官哥兒事件當成本線今晚重新發生的事件。"
```

---

# 10｜槐月十八日清晨接關點

```yaml
CONTINUATION_POINT:
  location: "觀止青樓／張麗華房間"
  time: "理火三年槐月十八日清晨"
  scene_status: "MORNING_READY; NO_WAKEUP_ACTION_PLAYED"

  current_positions_at_night_close:
    - "白御行最後由張麗華抱著入睡。"
    - "蘇清疲累，留在同一床上或緊鄰位置休息。"
    - "李瓶兒留宿並與三人同室共眠。"

  immediate_morning_facts:
    - "槐月十八日是蘇清兩日安排的最後一日。"
    - "李瓶兒已表示今日仍會來／仍想見白御行；她目前已在房內，醒後是否暫離再回尚未播放。"
    - "張麗華昨夜明示喜歡多人共處，也有真實吃味，並要求下次事前詢問。"
    - "白御行昨夜對蘇清、李瓶兒作出不同感情聲明，兩條關係不得混寫。"

  next_major_decision_owners:
    - "白御行：清晨第一個言行、是否處理昨夜關係聲明"
    - "張麗華：房間早晨安排、如何處理吃味與陪伴線"
    - "蘇清：最後一日如何履約、是否只按契約繼續"
    - "李瓶兒：醒後是否留在房內、白日如何相處、是否維持昨夜有限親密"

  world_actions_available:
    - "清晨起身、洗漱、早餐與房內對話"
    - "酒莊師爺或觀止後勤送來既有長線消息"
    - "蘇清最後一日共同生活自然推進"
    - "李瓶兒處理掌櫃職務與昨夜私密事件之分界"

  hard_stop_topics_requiring_direct_choice:
    - "李瓶兒是否成為白御行的女人"
    - "李瓶兒是否接受排他關係"
    - "李瓶兒是否願意共同生育"
    - "蘇清契約結束後是否談感情"
    - "下一次多人性事件之參與與同意"
```

---

# 11｜接關最小載入摘要

```yaml
MINIMUM_RUNTIME_SLICE:
  - "時間已到槐月十八日清晨，昨夜四人成人事件結束。"
  - "白御行與張麗華、蘇清均已發生性交；李瓶兒只接受有限手部與口部探索，未性交。"
  - "沒有任何體內射精或懷孕被確認。"
  - "蘇清不接受體內射精；她的停止權曾被重新確認，第一百次後喊停並獲遵守。"
  - "蘇清兩日履約尚剩槐月十八日最後一日；五百兩舊帳未正式結清。"
  - "白御行明示目前不愛蘇清，只承認肉體享受。"
  - "白御行明示對李瓶兒有真感情；李瓶兒高興但把關係、排他與生育答案延後至兩日後。"
  - "李瓶兒今日仍想見白御行，但未承諾性行為。"
  - "張麗華喜歡昨夜變化，也真實吃味；下次多人事件須先問她。"
  - "四人昨夜共同就寢，白御行最後由張麗華抱著。"
```

---

# 最終接關句

> 夜已過去。張麗華的手臂仍是白御行最後記得的睡處；蘇清的舊帳尚剩最後一日，李瓶兒的答案則被她親手留到兩日之後。槐月十八日清晨尚未有人開口。

<!-- SOURCE_HOT_V2_0_END -->

---

## SOURCE ARCHIVE｜HOT V2.1

**檔名：** `觀止青樓_白御行線_HOT_SAVE_V2.1_槐月十八日下午_定陶商戰起局蘇清私約白玉池補固與麗華私稱版.md`  
**SHA-256：** `542e19ef8ae8c842979f72d2db93df162f68c74f83e12b97ff34cb0f4c67c5f5`

<!-- SOURCE_HOT_V2_1_BEGIN -->
# 觀止青樓｜白御行線 HOT SAVE V2.1
## 理火三年槐月十八日下午｜定陶商戰起局 × 蘇清二十八日私約 × 白玉池舊案補固 × 張麗華私下稱呼固化版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V2_1_HUAI18_AFTERNOON_TRADE_WAR_SUQING_PRIVATE_PACT_WHITE_JADE_POOL_CORRECTION"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V2.1"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  story_date: "理火三年槐月十八日"
  time_of_day: "下午／提早晚膳以前；精確時刻未定"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V2.0_槐月十八日清晨_四人家人夜結與蘇清履約瓶兒延後決定版.md"
  record_state: "STORY_HELD_FOR_HOT_SAVE; CURRENT_SCENE_READY"
  current_location: "觀止青樓／蘇清房間"
  present:
    - "白御行"
    - "蘇清"
  recently_departed:
    - "潘金蓮"
  save_scope:
    - "定陶商會與汴梁商戰之已發生佈局"
    - "常煒之副會長身分與執行權"
    - "沈萬三、西門慶、廣源轉運行之不同法位"
    - "白御行對潘金蓮投放之未證實消息與真實戰略意圖"
    - "白御行與蘇清之二十八天私人盟約"
    - "白玉池既有真相之玩家／GM補固"
    - "張麗華與白御行私下固定稱呼"
    - "當日晚膳與觀止內部生活接點"
```

---

# 0｜提交法位與版本說明

```yaml
COMMIT_NOTE:
  - "本檔取代 HOT V2.0，成為白御行線當前接關切片；V2.0仍為前置歷史來源。"
  - "本檔不更新 MASTER，不改寫原始人物卡或人物池。"
  - "張麗華私下稱呼屬白御行玩家線關係語言固化，不倒灌人物基線。"
  - "白玉池四項補充為玩家明示之既有事件校正；本線以本檔記錄為準。"
  - "蘇清二十八日之約雖不進觀止公開帳冊，仍以私人秘密契約保存，避免長線遺失。"
  - "白御行對潘金蓮所說『沈萬三要殺西門慶』只保存為白御行投放的消息，不升格為客觀事實。"
  - "商戰內所有人物判斷、流言與操作目的分開記錄；能力、嫌疑、敵意與實際涉案不得互相代換。"
```

```yaml
SOURCE_LINEAGE:
  previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V2.0_槐月十八日清晨_四人家人夜結與蘇清履約瓶兒延後決定版.md"
    role: "前置夜間關係、蘇清舊約、李瓶兒延後決定與張麗華陪伴線來源"
  white_jade_pool_previous_record:
    files:
      - "觀止青樓_白御行線_HOT_SAVE_V1.6_槐月十六日清晨_張麗華花燭前置與白玉池異常回顯封池版.md"
      - "觀止青樓_白御行線_HOT_SAVE_V1.7_槐月十六日午後_白玉池暫閉與張麗華花燭前入睡接關版.md"
    role: "白玉池先前可觀察事件來源；其中仍標記未知之處，由本輪玩家既有事件校正補足"
  novel_source:
    file: "觀止青樓第1-8卷 (1).md"
    role: "沈萬三由明朝線接入觀止及盤商合作之既存來源"
```

---

# 1｜當前時間、位置與生活線

```yaml
CURRENT_SCENE:
  date: "理火三年槐月十八日"
  time: "下午／提早晚膳前；精確時刻未知"
  location: "觀止青樓／蘇清房間"
  story_mode: "HOLD_FOR_SAVE"
  present:
    - "白御行"
    - "蘇清"
  current_scene_last_subject: "白玉池開張前確認與整理"
  next_action_owner: "PLAYER_OR_WORLD_AFTER_RESUME"
```

```yaml
DAY_PLAN:
  white_yuxing:
    - "白御行明示槐月十八日不離開觀止。"
    - "白御行明示槐月十九日回定陶商會處理商戰後續。"
  midday:
    - "白御行與張麗華決定中午不吃，晚膳提早。"
  dinner_location: "張麗華房間"
  dinner_plan:
    - "燉軟羊肉，多放蘿蔔並去膻。"
    - "蒸魚，多放蔥薑。"
    - "兩樣青菜。"
    - "熱湯／較清的醒酒湯。"
  preparation:
    responsible_actor: "李瓶兒"
    confirmed:
      - "李瓶兒已令廚下汆羊肉、準備蘿蔔與清湯。"
      - "魚將晚些再殺，以免肉散。"
      - "李瓶兒會提早將晚膳送到張麗華房裡，並遣人尋白御行。"
  white_yuxing_commitment:
    - "白御行向張麗華明示晚餐再回來。"
  unfinished:
    - "晚膳尚未開始。"
    - "蘇清是否同席未由本輪另行確認，但廚下先前已多備碗筷。"
```

---

# 2｜槐月十八日商會密會：常煒與定陶商戰起局

## TRADE18-E01｜常煒到觀止密會

```yaml
EVENT_RECORD:
  event_id: "TRADE18-E01-CHANGWEI_SECRET_MEETING"
  status: "COMPLETED"
  location: "觀止青樓／密會房間"
  participants:
    - "白御行"
    - "常煒"
    - "送信帳房／商會人員（姓名未固化）"
  actor_identity:
    常煒: "定陶商會副會長"
  privacy_action:
    - "白御行命張麗華、蘇清、李瓶兒等女人離開，將此定為商會密會。"
  confirmed_case_state:
    - "三家分號出現以舊帳務方式製造自然結清的異常帳。"
    - "前案已被宣布結案後，仍有人繼續收取舊帳材料、補洞並追查送信人。"
    - "商會認定此為結案後的再次出手，不再只是舊案未清。"
```

## TRADE18-E02｜沈萬三在本案的法位

```yaml
SHEN_WANSAN_POSITION:
  baseline_identity:
    status: "EXISTING_GUANZHI_CHARACTER"
    origin: "明朝線接入觀止"
    roles:
      - "觀止明朝線代理商"
      - "潘金蓮合作盤商"
      - "花魁賽／品花局外盤、跨地域資金與消息網節點"
  current_case_status: "POSSIBLE_TARGET_OR_HIGH_CAPABILITY_RELATED_NODE; NOT_LOCKED"
  confirmed_reason_for_inclusion:
    - "其舊部／代理網路與跨區資金能力符合部分能力模型。"
    - "沈萬三與定陶商會真正重疊的主要競爭場域，是當前時代的汴梁。"
  not_confirmed:
    - "沈萬三本人參與異常調帳。"
    - "沈萬三授意廣源轉運行。"
    - "沈萬三要殺西門慶。"
    - "沈萬三已把定陶商會視為敵人。"
    - "沈萬三背叛觀止或潘金蓮。"
  strategic_constraint:
    - "白御行與常煒均認為直接與沈萬三全面對抗至少可能兩敗俱傷，不作第一擊目標。"
```

## TRADE18-E03｜廣源轉運行與許奉年成為第一擊目標

```yaml
TARGET_STATE:
  target_name: "汴梁廣源轉運行"
  responsible_person: "許奉年"
  target_class: "REAL_ENEMY_SELECTED_FOR_VISIBLE_DEFEAT"
  confirmed_case_links:
    - "三家分號異常帳中至少兩筆經過廣源轉運行，表面為補運費，實際形成舊貨款結清憑據。"
    - "前案結案後第二日，許奉年方面買走死去帳房家中的舊手簿。"
    - "送信帳房離開定陶以前，有人打聽其住處。"
  power_assessment_by_changwei:
    - "廣源在汴梁有貨棧與城外短線，有分量但承受不了定陶商會斷貨、斷帳、斷信用的合擊。"
  strategic_role:
    - "必須是確實再次出手的敵人，不是純替罪羊。"
    - "可被定陶力量壓倒，並讓商會對外宣布已取得勝利。"
    - "其被擊倒後若仍有人再次出手，則另立下一回戰事。"
```

## TRADE18-E04｜白御行對常煒的作戰指令

```yaml
PLAYER_DIRECTIVE:
  actor: "白御行"
  recipient: "常煒"
  confirmed_orders:
    - "讓定陶商會立即動起來。"
    - "以廣源轉運行／許奉年為可被碾過的真敵人。"
    - "把西門慶拉進事件，使火勢自然燒到他身上。"
    - "將人、銀路、貨路、盤口與時間編得密，使外界自然聯想；關聯不必全部真實。"
    - "不必製造一樁容易被查穿的單一假案，而是利用真實片段與模糊連接製造推斷場。"
    - "對商會自己人不公開揭底，以敲打、差異查核與觀察反應為主。"
    - "槐月十九日由白御行回商會查看後續。"
  declared_end_condition:
    - "廣源等真敵人停止再出手，則本回可宣告結束。"
    - "已結案後仍再次出手者，被視為拒絕和解，另開下一回。"
```

## TRADE18-E05｜常煒之執行方案與已發生初步效果

```yaml
CHANGWEI_EXECUTION_PLAN:
  executor: "常煒"
  status: "ACTIVE"
  external_actions:
    - "定陶體系暫緩廣源轉運行票據兌付，名義為帳目重核。"
    - "向廣源發出查帳公函，查問舊帳、手簿與經手人。"
    - "向西門慶發出另一封公函，只查近三月是否替廣源兌過銀票。"
    - "令與西門慶有舊怨的掮客接觸廣源資金流入汴梁娛樂盤口的消息。"
  internal_actions:
    - "三家分號收到不同查核項目，用於觀察誰急於補帳、燒紙或找人。"
    - "內部有異動者先記錄，不立即抓、不立即審、不公開。"
  shen_wansan_policy:
    - "暫不直接接觸或挑釁沈萬三。"
    - "觀察廣源與西門慶起火後，沈萬三是否調人、撤線、詢問或毫無反應。"
  confirmed_initial_effects:
    - "廣源轉運行第一張票據已在定陶商會櫃上被蓋『暫緩兌付』並退回。"
    - "至少兩名平日與西門慶稱兄道弟者已開始私下詢問其近日盤口數字。"
  not_yet_confirmed:
    - "西門慶是否已收到正式公函。"
    - "廣源是否已正式反應。"
    - "沈萬三是否已知情。"
    - "任何目標是否已實際倒台。"
```

---

# 3｜西門慶火線與潘金蓮會談

## PAN18-E01｜白御行召潘金蓮至蘇清房內

```yaml
EVENT_RECORD:
  event_id: "PAN18-E01-PRIVATE_WARNING_OPERATION"
  status: "COMPLETED_MEETING"
  location: "蘇清房間"
  participants:
    - "白御行"
    - "蘇清"
    - "潘金蓮"
  covert_signal:
    - "白御行在桌下輕踢蘇清，示意她先聽、不拆話、不過度推測。"
    - "蘇清收到提示後沒有替白御行補充或反駁。"
```

## PAN18-E02｜投放給潘金蓮的消息與其法位

```yaml
MESSAGE_RECORD:
  speaker: "白御行"
  recipient: "潘金蓮"
  message_claims:
    - "有人要對西門慶開刀，勢力大到白御行也不敢惹。"
    - "要殺西門慶的人是沈萬三。"
    - "原因可能是商場，也可能是女人；白御行聲稱自己不知道。"
  objective_status: "UNVERIFIED_OPERATIONAL_CLAIM"
  not_world_fact:
    - "沒有確認沈萬三要殺西門慶。"
    - "沒有確認白御行真不知道原因。"
    - "沒有確認白御行客觀上不敢惹對方。"
  later_disclosed_player_intent_to_suqing:
    - "白御行本就預期潘金蓮不會完全相信。"
    - "目的在促使潘金蓮切帳、封銀或傳訊，引發西門慶周邊過度反應。"
    - "待西門慶瘋狂自救並咬向沈萬三，迫使沈萬三不得不實際反擊。"
    - "若兩者原本有勾連，則期待其形成窩裡反。"
```

## PAN18-E03｜潘金蓮的可觀察反應與已表態措施

```yaml
PAN_JINLIAN_RESPONSE:
  belief_state: "DID_NOT_FULLY_ACCEPT; EXACT_PRIVATE_JUDGMENT_UNKNOWN"
  confirmed_position:
    - "她不願以替西門慶擋沈萬三為念舊方式。"
    - "她區分西門慶個人資產與觀止盤口、沈萬三外盤資金。"
    - "若火燒入觀止盤口，她會把出手者視為自己的敵人。"
  declared_actions:
    - "先切分盤口帳目。"
    - "賭客本金與應付彩金照帳，不得因西門慶風險而扣留。"
    - "沈萬三經手之外盤銀另封另算。"
    - "西門慶自己的水錢、墊銀、抽頭與未結分成，可延後兩日交割。"
    - "以重核大額分成、防冒領為公開理由。"
    - "不直接向沈萬三詢問，以免暴露消息外洩。"
    - "考慮向西門慶送出不提沈萬三、不提商會、不提白御行來源的模糊警告。"
  warning_status: "DECLARED_INTENT; DELIVERY_NOT_YET_OBSERVED"
  relational_note:
    - "潘金蓮明示替白御行保密不是白送的人情；未形成具體價碼或正式契約。"
```

## 西門慶目前位置

```yaml
XI_MENQING_CURRENT_STATE:
  baseline_roles:
    - "觀止花魁賽／品花局公開賭盤前台收注者之一。"
    - "與潘金蓮、沈萬三之盤口結構存在不同層次合作。"
  case_status:
    - "尚未證明參與定陶異常帳或廣源收尾。"
    - "已被白御行與常煒刻意拉進外界推斷場。"
    - "其狐朋狗友與周邊利益者已開始出現自保性詢問。"
  not_confirmed:
    - "西門慶已知自己被針對。"
    - "西門慶已咬向沈萬三。"
    - "西門慶已失去盤口、財產或人身安全。"
    - "西門慶已被毀。"
```

---

# 4｜蘇清二十八日私人盟約

## PRIVATE-Pact-SQ28｜擊掌為盟

```yaml
PRIVATE_PACT:
  pact_id: "PRIVATE-BYX-SUQING-28DAY-LIFE-PACT-001"
  status: "AGREED_NOT_YET_TRIGGERED"
  parties:
    - "白御行"
    - "蘇清"
  formation_event:
    - "白御行提出：若他毀掉西門慶、替蘇清報仇，蘇清在他身邊生活二十八天。"
    - "蘇清接受談判後，雙方擊掌為盟。"
  institutional_status:
    - "不進觀止公開帳冊。"
    - "不是觀止對外契約。"
    - "本 HOT SAVE 只為世界連續性保存其存在與保密範圍。"
  knowledge_scope:
    - "白御行"
    - "蘇清"
  trigger:
    required_event: "西門慶被白御行之局真正毀掉／失去原有位置，使蘇清之仇得到實質報償。"
    current_state: "NOT_MET"
    exact_threshold: "若未來對是否已達成存在爭議，需由當時可觀察結果與雙方明示確認，不得由導演單方面偷算。"
  duration:
    value: 28
    unit: "DAY"
    start: "觸發條件成立後"
    exact_calendar_method: "NOT_YET_SPECIFIED"
  content:
    core: "蘇清在白御行身邊共同生活二十八天，重點是日常生活，而非單一工作或單一性服務。"
    possible_activities:
      - "跟隨白御行學做生意。"
      - "陪同應酬。"
      - "陪白御行追求或接觸其他女人。"
      - "一起發呆、無事度日。"
      - "在雙方當下同意下發生性行為，時間與形式不預先鎖定。"
  consent_boundary:
    - "二十八天共同生活不等於預先同意所有性行為、行程、工作或命令。"
    - "每一具體親密行動仍由當時雙方決定。"
    - "蘇清不是丫鬟、護衛或無條件服從的軍師。"
    - "蘇清保留批評、拒絕、嘲笑或不配合特定事項的權利。"
  separation_from_old_contract:
    - "本私人盟約與舊五百兩／三夜未結帳完全分開。"
    - "不得用同一日同時抵銷舊約與二十八天私約，除非雙方日後另行明示重議。"
```

## 舊約仍然有效

```yaml
OLD_SUQING_CONTRACT:
  contract_id: "CONTRACT-H17-SUQING-2DAY-HOUSEHOLD-001"
  state: "ACTIVE_FINAL_DAY_IN_PROGRESS"
  current_date: "槐月十八日"
  debtor_creditor_direction:
    debtor: "蘇清"
    creditor: "白御行"
  remaining:
    - "槐月十八日最後一日共同生活至原約定結束時間。"
  not_settled:
    - "本日上午／下午事件尚未宣告舊五百兩帳正式結清。"
  no_merge:
    - "不得將蘇清二十八日私約倒灌成舊約延長。"
```

---

# 5｜白玉池既有事件補固與當前狀態

```yaml
WHITE_JADE_POOL_GM_CORRECTION:
  status: "GM_CONFIRMED_ROUTE_EVENT; SOLIDIFIED_IN_HOT_V2_1"
  correction_reason:
    - "此線早期已跑過完整事件，但舊 SAVE 未完全保存，導演一度誤以為真相仍未知。"
  confirmed_existing_facts:
    - "時空道人已在眾人決議同意後補上白玉池的洞。"
    - "白玉池對面顯現／連接的是白御行的黑暗面。"
    - "對面屬另一個空間。"
    - "通過該處會造成時間線與空間定位混亂。"
    - "此前已做過小規模實驗，確認穿越會引發時空錯亂風險。"
    - "現在白玉池已封池，基本沒有持續性問題。"
  current_required_work:
    - "開張前重新確認補洞處與封池後狀態穩定。"
    - "確認沒有新的回顯、滲漏或時空異常。"
    - "完成清池、換水、浴具、帷帳、燈火等營業整理。"
  current_risk_status: "SEALED_AND_BROADLY_STABLE; PREOPENING_CONFIRMATION_PENDING"
  prohibited_regression:
    - "不得重新把白玉池寫成原因完全未知、仍需破解的主線謎案。"
    - "不得由蘇清單方面取得永久封池或否決開張的最終裁決權。"
    - "不得在沒有新事件的情況下聲稱通道重新打開。"
```

```yaml
WHITE_JADE_POOL_CURRENT_TASK:
  assigned_by: "白御行"
  tasked_actor: "蘇清"
  instruction:
    - "有空時收拾白玉池，因為總要重新開張，不能永久放置。"
  corrected_interpretation:
    - "蘇清負責確認穩定、整理與準備營業，不是重啟舊案。"
  completion_state: "NOT_STARTED_OR_NOT_YET_OBSERVED"
```

---

# 6｜張麗華 × 白御行私下稱呼固化

```yaml
RELATIONAL_LANGUAGE_CANON:
  record_id: "REL-LANG-BYX-ZLH-PRIVATE-APPELLATIONS-001"
  lifecycle: "GM_CONFIRMED_ROUTE_CANON"
  scope: "白御行玩家線／兩人私下場合"
  confirmed_default_terms:
    zhang_lihua_to_bai_yuxing: "官人"
    bai_yuxing_to_zhang_lihua: "小娘子"
  application:
    - "兩人私下、親密、日常房內交流時，以此作為既有且自然的默認稱呼。"
    - "角色可因爭執、戲弄、商務、公開場合或特定情緒暫時改用其他稱呼，但不得因此遺忘本項既有關係語言。"
  boundaries:
    - "此稱呼固化本身不單獨建立法定婚姻、排他或妻妾名分。"
    - "不得倒灌為張麗華對所有玩家線或所有人物的固定稱呼。"
```

---

# 7｜主要人物當前硬狀態

```yaml
ACTOR_STATE:
  白御行:
    location: "蘇清房間"
    day_plan:
      - "今日不離開觀止。"
      - "提早晚膳時回張麗華房間。"
      - "明日回定陶商會。"
    active_actions:
      - "已將定陶商戰執行交給常煒。"
      - "已向潘金蓮投放沈萬三欲殺西門慶之未證實消息。"
      - "已與蘇清成立二十八日私人盟約。"
    unknown:
      - "商戰第一日實際反應。"
      - "潘金蓮是否已送出警告。"
      - "西門慶與沈萬三是否會形成實際衝突。"

  蘇清:
    location: "自己房間"
    knowledge:
      - "知道白御行投放消息的真實戰略意圖。"
      - "知道常煒商戰線的大致方向，但未必知道全部商會內部名單與公函細節。"
      - "知道並參與二十八日私人盟約。"
    obligations:
      - "舊五百兩契約最後一日仍在進行。"
      - "白玉池整理與開張前確認為待辦，不是立即完成。"
    relation_state:
      - "與白御行之二十八日私約已成立但未觸發。"
      - "與白御行之愛情仍未建立；私約不自動改寫感情。"

  張麗華:
    current_location: "觀止內；精確房間未持續追蹤"
    confirmed:
      - "已點提早晚膳，等待白御行晚上回房。"
      - "私下稱白御行『官人』已固化。"
      - "白御行私下稱她『小娘子』已固化。"
    knowledge_limit:
      - "她知道上午有商會密會，未確認知道常煒完整佈局。"
      - "未確認知道白御行對潘金蓮投放的沈萬三消息。"

  李瓶兒:
    current_location: "觀止後廚／觀止內；精確位置未持續追蹤"
    confirmed:
      - "負責提早晚膳準備。"
      - "與白御行的關係、生育與正式位置仍延後決定。"
    knowledge_limit:
      - "未確認知道商戰密會內容。"

  潘金蓮:
    current_location: "已離開蘇清房間；精確位置未持續追蹤"
    knowledge:
      - "聽見白御行聲稱沈萬三要殺西門慶。"
      - "知道西門慶可能受到大勢力針對。"
      - "不知道白御行已向蘇清明說的完整操盤意圖。"
    active_intent:
      - "切分盤口帳、保護賭客本金、延後西門慶部分分成。"
      - "可能向西門慶送模糊警告。"
```

---

# 8｜知情矩陣

```yaml
KNOWLEDGE_MATRIX:
  常煒商戰完整指令:
    knows:
      - "白御行"
      - "常煒"
      - "在場送信商會人員（僅限其實際聽見部分）"
    does_not_automatically_know:
      - "張麗華"
      - "李瓶兒"
      - "潘金蓮"
      - "西門慶"
      - "沈萬三"

  潘金蓮收到的沈萬三消息:
    knows:
      - "白御行"
      - "蘇清"
      - "潘金蓮"
    objective_truth: "UNCONFIRMED"

  白御行真正挑動意圖:
    knows:
      - "白御行"
      - "蘇清"
    may_infer_but_not_confirmed:
      - "潘金蓮"

  蘇清二十八日私約:
    knows:
      - "白御行"
      - "蘇清"
    secrecy: "PRIVATE; NOT_GUANZHI_PUBLIC_LEDGER"

  白玉池補固真相:
    route_fact: "GM_CONFIRMED"
    exact_original_participants: "依早期事件；本 HOT 不補造完整名單"
    current_operational_knowledge:
      - "白御行"
      - "蘇清（至少已被交代整理；早期完整知情範圍依舊事件）"

  張麗華私下稱呼:
    knows:
      - "白御行"
      - "張麗華"
    status: "ROUTE_CANON"
```

---

# 9｜禁止污染與未決事項

```yaml
ANTI_CORRUPTION_LOCKS:
  - "不得把『沈萬三要殺西門慶』當成已確認世界事實。"
  - "不得把沈萬三的盤商與代理商身分直接等同於定陶案幕後主使。"
  - "不得把西門慶被拉入流言場寫成他已經倒台。"
  - "不得把廣源轉運行作為真敵人，改寫成所有證據與敘事聯繫都必然真實。"
  - "不得把白御行的操盤目的改寫成潘金蓮、常煒或沈萬三的內心。"
  - "不得把蘇清二十八日私約當成觀止公開契約、賣身契、無條件性同意或舊約延長。"
  - "不得忘記蘇清舊約最後一日仍未正式結清。"
  - "不得重新把白玉池寫成完全未知或正在失控；除非新事件提供可觀察證據。"
  - "不得把張麗華『官人／小娘子』私稱升格成已婚法位。"
  - "不得讓商戰線吞掉當日晚膳、張麗華陪伴、李瓶兒延後決定與蘇清最後一日生活線。"
```

```yaml
UNRESOLVED:
  trade_war:
    - "廣源與許奉年將如何反應。"
    - "西門慶是否收到公函或潘金蓮警告。"
    - "西門慶周邊是否開始切割、分食或向沈萬三發難。"
    - "沈萬三是否實際涉案、被利用、被嫁禍、旁觀或反擊。"
    - "常煒差異查核會釣出哪些商會內部異動者。"
  relationships:
    - "蘇清舊約何時正式結清。"
    - "蘇清二十八日私約是否與何時被觸發。"
    - "李瓶兒於兩日後對關係與孩子問題的回答。"
    - "張麗華三日陪伴線後續。"
  white_jade_pool:
    - "開張前檢查結果。"
    - "實際重新開張日期與營業規則。"
```

---

# 10｜下一幕接關

```yaml
RESUME_POINT:
  date: "理火三年槐月十八日下午"
  location: "蘇清房間"
  present:
    - "白御行"
    - "蘇清"
  immediate_state:
    - "潘金蓮已離開。"
    - "二十八日私約已擊掌成立但尚未觸發。"
    - "白玉池舊案真相已由玩家補固，當前只待開張前確認與整理。"
    - "常煒已在外執行商戰佈局。"
    - "白御行今日不離開觀止，提早晚膳將在張麗華房間進行。"
  next_world_hinges:
    - "蘇清回應白玉池整理或轉入當日日常。"
    - "廚下／李瓶兒來請提早晚膳。"
    - "潘金蓮切帳後的第一個盤口反應。"
    - "常煒送回第一輪商戰消息，但普通消息不必立刻打斷生活場。"
  player_decision_required_now: false
```

---

# 11｜接關硬提示

```yaml
DIRECTOR_QUICK_LOAD:
  - "目前是槐月十八日下午，白御行與蘇清在蘇清房內。"
  - "常煒是定陶商會副會長，已執行廣源轉運行／許奉年第一擊與西門慶流言牽引。"
  - "沈萬三是明朝線代理商、潘金蓮合作盤商；可能關聯但完全未鎖定。"
  - "白御行告訴潘金蓮『沈萬三要殺西門慶』是操盤消息，不是已證實真相。"
  - "潘金蓮不全信，但準備切帳、保賭客錢、延後西門慶部分分成，可能送出模糊警告。"
  - "白御行與蘇清擊掌成立私密二十八日共同生活盟約；西門慶真正被毀後才觸發，舊約另算。"
  - "白玉池洞已由時空道人在眾人同意下補好；對面是白御行黑暗面與另一空間，穿越會擾亂時空；目前封池穩定，只待開張確認。"
  - "張麗華私下稱白御行『官人』；白御行私下稱張麗華『小娘子』。"
  - "提早晚膳在張麗華房間，李瓶兒已準備羊肉、蒸魚、青菜與熱湯；白御行承諾晚餐回去。"
```

> **當前畫面：潘金蓮已帶著不全信的消息離去；常煒在汴梁把第一張票據退回，蘇清房內則留下兩人擊掌後的私帳。白玉池不再是待破解的舊洞，只待確認與整理。晚膳的羊肉已下鍋，張麗華的小娘子房裡還留著官人的位置。**

<!-- SOURCE_HOT_V2_1_END -->

---

## SOURCE ARCHIVE｜HOT V2.2

**檔名：** `觀止青樓_白御行線_HOT_SAVE_V2.2_槐月十九日破曉_師理理如夫人前置與張麗華獨宿夜結版.md`  
**SHA-256：** `fd8b50f27cb463d43cfd85bcadfd4afb60569265c1246d777422b4917f10e2e9`

<!-- SOURCE_HOT_V2_2_BEGIN -->
# 觀止青樓｜白御行線 HOT SAVE V2.2
## 理火三年槐月十九日破曉｜師理理如夫人前置 × 七色肚兜分贈 × 蘇清言語賽 × 張麗華獨宿夜結版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V2_2_HUAI19_DAWN_RIRU_FUREN_PRESET_ZLH_PRIVATE_NIGHT"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V2.2"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  story_date: "理火三年槐月十九日"
  time_of_day: "破曉／天將明；精確時刻未定"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V2.1_槐月十八日下午_定陶商戰起局蘇清私約白玉池補固與麗華私稱版.md"
  previous_valid_hot_sha256: "542e19ef8ae8c842979f72d2db93df162f68c74f83e12b97ff34cb0f4c67c5f5"
  record_state: "ACTIVE_PAUSED_AT_DAWN"
  current_location: "觀止青樓／張麗華房間／床上"
  present:
    - "白御行"
    - "張麗華"
  save_scope:
    - "槐月十八日下午李師師／師理理之如夫人關係前置與成人事件"
    - "白玉池復開前檢查進度"
    - "七色蜀錦蘇繡肚兜分贈與知情範圍"
    - "張麗華房內提早晚膳、蘇清與張麗華言語競賽"
    - "蘇清足部彩頭之實際履行"
    - "李瓶兒與蘇清自行離場、張麗華獨宿夜"
    - "白御行與張麗華當夜性行為、停止點、避孕界線與同眠"
    - "張麗華嫉妒、酒莊、李師師、孩子與關係談話"
    - "槐月十九日商會、白玉池、李瓶兒與蘇清之立即到期事項"
```

---

# 0｜提交法位與版本說明

```yaml
COMMIT_NOTE:
  - "本檔取代 HOT V2.1，成為白御行線當前接關切片；V2.1仍為商戰、蘇清私約與白玉池既有真相之直接來源。"
  - "本檔不更新 MASTER，不改寫人物卡或人物池基線。"
  - "本檔只保存已發生、可觀察、當事人明示、玩家對自身言行的有效確認，以及玩家明示要求自然推進至破曉之結果。"
  - "成人事件之身體反應、當下同意、關係承諾、懷孕結果與未來義務分軸記錄。"
  - "言語比賽中的假設、誇張、低俗台詞不升格為人物真實承諾、秘密告白或未來必然行動。"
  - "張麗華與李師師之孩子議題均未形成可由白御行單方面執行的共同生育契約。"
  - "當夜沒有觀察到商戰線新回報；不得因此推定外部世界停滯或事件已結束。"
```

```yaml
SOURCE_LINEAGE:
  previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V2.1_槐月十八日下午_定陶商戰起局蘇清私約白玉池補固與麗華私稱版.md"
    role: "商戰、蘇清二十八日私約、舊約、白玉池真相、當日晚膳與張麗華私稱來源"
  earlier_relationship_sources:
    - "觀止青樓_白御行線_HOT_SAVE_V1.8_槐月十七日上午_張麗華酒莊接手與三日陪伴線.md"
    - "觀止青樓_白御行線_HOT_SAVE_V2.0_槐月十八日清晨_四人家人夜結與蘇清履約瓶兒延後決定版.md"
  route_conversation_commit:
    role: "槐月十八日下午至十九日破曉之直接劇情事件來源"
```

---

# 1｜當前時間、場景與破曉接點

```yaml
CURRENT_SCENE:
  date: "理火三年槐月十九日"
  time: "破曉／天將明"
  location: "張麗華房間"
  scene_state: "AFTER_PRIVATE_NIGHT; SLEEP_COMPLETED_OR_IN_FINAL_DAWN_REST"
  present:
    - "白御行"
    - "張麗華"
  room_privacy:
    - "槐月十八日晚李瓶兒與蘇清均已自行離場。"
    - "張麗華親自落閂，後續房內事件只有白御行與張麗華在場。"
  immediate_pose:
    - "兩人依張麗華最後選擇停止性行為並相擁同眠。"
    - "目前沒有正在進行的性行為。"
  next_action_owner: "WORLD_OR_PLAYER_AFTER_DAWN_OPENS"
```

```yaml
PLAYER_STATE_AT_DAWN:
  白御行:
    location: "張麗華床上"
    confirmed_recent_events:
      - "槐月十八日下午與李師師／師理理發生一次完成之性交並體內射精。"
      - "槐月十八日晚與張麗華發生較長時間性交；未確認當夜是否射精。"
    fatigue: "LIKELY_AFTER_MULTIPLE_ADULT_EVENTS; EXACT_LEVEL_NOT_PLAYER_CONFIRMED"
    day_plan_due:
      - "槐月十九日回定陶商會查看商戰後續。"
```

```yaml
ZHANG_LIHUA_STATE_AT_DAWN:
  location: "自己房內／與白御行同床"
  self_reported:
    - "當夜三個周天後已滿足。"
    - "腿軟、腰疲，不要第四個周天。"
    - "選擇停止性交，只要相擁同眠。"
  consent_current: "NO_ONGOING_SEXUAL_CONSENT_CARRIED_OVER_INTO_DAWN"
  relationship_current:
    - "與白御行之情人關係持續。"
    - "雙方當夜互相明示喜歡。"
    - "不構成婚姻、排他或生育同意。"
```

---

# 2｜白玉池復開前確認

## BYC18-E01｜蘇清完成第一輪開池前檢查

```yaml
EVENT_RECORD:
  event_id: "BYC18-E01-PREOPENING_INSPECTION"
  time: "槐月十八日下午／晚膳前"
  actor: "蘇清"
  status: "FIRST_CHECK_COMPLETED"
  reported_to: "白御行"
  confirmed_report:
    - "既有封補處完整。"
    - "未見通道重新打開。"
    - "池水已更換。"
    - "目前沒有新的明顯回顯或持續滲漏。"
  remaining:
    - "槐月十九日再做一次回顯／滲漏確認。"
    - "若第二次確認仍穩定，白玉池可進入復開準備。"
  not_established:
    - "白玉池已正式重新營業。"
    - "已訂定復開日期、價格與營業規則。"
    - "舊通道或白御行黑暗面重新顯現。"
```

```yaml
WHITE_JADE_POOL_CURRENT_STATE:
  status: "SEALED_STABLE_AFTER_FIRST_PREOPENING_CHECK"
  immediate_due: "槐月十九日第二次回顯／滲漏確認"
  anti_regression:
    - "不得將白玉池重新寫成原因未知、正在失控或必須重解之主線謎案。"
    - "無新可觀察事件，不得聲稱另一空間通道重新開啟。"
```

---

# 3｜李師師／師理理：如夫人前置、成人事件與當晚設席

## RIR18-E01｜如夫人關係框架口頭成立

```yaml
RELATION_OFFER:
  event_id: "RIR18-E01-RU_FUREN_FRAMEWORK"
  time: "槐月十八日下午"
  location: "李師師私人房間"
  parties:
    - "白御行"
    - "李師師／師理理"
  status: "ORALLY_ACCEPTED_FRAMEWORK; PUBLIC_IMPLEMENTATION_NOT_OBSERVED"
  white_yuxing_offer:
    - "白御行提出給李師師『如夫人』的公開位置。"
    - "此位置不以她是否懷孕為成立前提。"
  li_shishi_response:
    - "李師師表示她想要此位置。"
    - "她保留繼續住在觀止、設席、接待賓客與管理自己房門的自主。"
    - "在此關係存續期間，她同意不再與其他男人上床。"
  not_established:
    - "已向觀止或外界正式公布。"
    - "已寫入白家名冊或官府文書。"
    - "李師師離開觀止。"
    - "白御行取得她設席、工作、身體或居所之管理權。"
    - "白御行對其他女人形成排他義務。"
```

## RIR18-E02｜成人事件、停止與重新同意

```yaml
ADULT_EVENT:
  event_id: "RIR18-E02-INTERCOURSE_AND_INSEMINATION"
  time: "槐月十八日下午"
  location: "李師師私人房間"
  participants:
    - "白御行"
    - "李師師／師理理"
  status: "COMPLETED"
  consent_sequence:
    - "起初動作過重時，李師師明示停止。"
    - "白御行停止，兩人重新確認是否繼續及可接受方式。"
    - "李師師其後明示接受較快、較重的性交。"
    - "李師師明示接受當次體內射精，並保留喊停條件。"
  observed_result:
    - "性交完成。"
    - "白御行在李師師體內射精。"
    - "沒有觀察到李師師在有效喊停後仍被迫繼續。"
  pregnancy_axis:
    status: "UNKNOWN"
    confirmed:
      - "當次存在體內射精。"
    not_confirmed:
      - "已受孕。"
      - "未受孕。"
      - "完整共同生育契約已成立。"
```

## RIR18-E03｜愛的告白、離房與枕頭事件

```yaml
EVENT_RECORD:
  event_id: "RIR18-E03-LOVE_AND_ABRUPT_DEPARTURE"
  status: "COMPLETED"
  confirmed:
    - "白御行在離開前對李師師說『我愛你』。"
    - "李師師在他離房以前沒有給出明確回答。"
    - "白御行隨即穿衣／整裝離開，趕赴張麗華房內提早晚膳。"
    - "李師師向門口擲出枕頭並出聲追罵。"
  interpretation_limits:
    - "枕頭事件證明她對白御行突兀離開有明顯情緒。"
    - "不得替李師師判定她已接受、拒絕或回應『我愛你』。"
    - "不得把白御行的告白自動等同婚姻、排他或永久承諾。"
```

## RIR18-E04｜便箋往返與戌初設席

```yaml
CORRESPONDENCE:
  event_id: "RIR18-E04-RED_GREEN_NOTE"
  sender: "白御行"
  recipient: "李師師／師理理"
  white_note:
    - "以『紅配綠，真美麗；一日十客，莫煩你』作戲謔便箋。"
  li_reply:
    - "表示可將句子譜成『莫煩郎』。"
    - "追問錢要算到哪裡。"
    - "明示『今夜設席，不許闖門』。"
  legal_effect:
    - "屬私下玩笑與界線提醒，不是十客實際安排。"
```

```yaml
LI_SHISHI_EVENING_SEAT:
  scheduled_time: "槐月十八日戌初"
  service_scope:
    - "音樂"
    - "茶"
    - "談話"
  overnight: false
  intercourse_included: false
  completion_state: "NOT_OBSERVED_IN_CURRENT_SCENE"
  anti_rumor:
    - "不得因她設席，推定客人進入她的床。"
```

---

# 4｜七色蜀錦蘇繡肚兜分贈

```yaml
GIFT_EVENT:
  event_id: "GIFT18-E01-SEVEN_COLORED_DUDOU"
  status: "ALL_SEVEN_ALLOCATED"
  source: "白御行持有之七色蜀錦蘇繡肚兜"
  allocations:
    李師師:
      color: "煙青"
      context: "下午私人場合先選"
      accepted: true
    李瓶兒:
      color: "白"
      accepted: true
      reaction: "喜歡"
    張麗華:
      color: "紫"
      accepted: true
      reaction: "喜歡"
    蘇清:
      color: "黑"
      accepted: true
      reaction:
        - "認出染色與做工。"
        - "知道白御行有意替她留黑色。"
    紅娘:
      color: "紅"
      accepted: true
    小翠:
      color: "綠"
      accepted: true
      boundary:
        - "接受禮物不等於接受十客、性服務或被拿來作性玩笑的安排。"
    春梅:
      color: "黃"
      delivery_method:
        - "由白御行交給張麗華。"
        - "張麗華以自己名義、按合適方式送給春梅。"
        - "不得說成剩下的或沒人要的。"
      final_delivery: "NOT_YET_OBSERVED"
```

```yaml
RED_GREEN_JOKE:
  confirmed:
    - "白御行先說『紅配綠，狗臭屁』，後否認並改口『紅配綠，真美麗』。"
    - "在場女人以此取笑白御行。"
  legal_effect: "NO_WORLD_STATE_CHANGE"
```

---

# 5｜張麗華房內提早晚膳

## DIN18-E01｜到席與菜色

```yaml
DINNER_EVENT:
  event_id: "DIN18-E01-EARLY_PRIVATE_DINNER"
  time: "槐月十八日傍晚／提早晚膳"
  location: "張麗華房間"
  confirmed_menu:
    - "燉軟羊肉，多蘿蔔、去膻。"
    - "蒸魚，多蔥薑。"
    - "兩樣青菜。"
    - "熱而較清的湯。"
  present_during_core_dinner:
    - "白御行"
    - "張麗華"
    - "蘇清"
    - "李瓶兒"
  gift_and_teasing_phase_also_present:
    - "紅娘"
    - "小翠"
  later_departed_before_private_night:
    - "紅娘"
    - "小翠"
    - "李瓶兒"
    - "蘇清"
```

## DIN18-E02｜三戰兩勝言語競賽

```yaml
VERBAL_CONTEST:
  event_id: "DIN18-E02-SHAMEFUL_SPEECH_CONTEST"
  status: "COMPLETED"
  competitors:
    - "張麗華"
    - "蘇清"
  judge: "李瓶兒"
  prize_subject: "白御行"
  format:
    - "三戰兩勝。"
    - "白御行作彩頭，不參賽、不裁判。"
    - "勝者取得白御行舔兩隻腳的彩頭。"
  rules_established_in_scene:
    - "言語可以是假設、誇張或故意低俗。"
    - "不因說出口便自動成為真實告白、履歷、承諾或未來義務。"
    - "不得使用不在場人物的私人秘密作題材。"
  result:
    round_1: "蘇清勝"
    round_2: "張麗華勝"
    round_3: "蘇清勝"
    final_score: "蘇清 2：張麗華 1"
    winner: "蘇清"
  judge_basis:
    - "李瓶兒依自己聽不下去／羞恥程度裁判。"
```

```yaml
CONTEST_SPEECH_AUTHORITY_LOCK:
  - "蘇清第三局提及二十八日後穿黑肚兜、求白御行別把她當結清帳目，只屬競賽文本；不建立她將來必然留下、愛上白御行或主動求關係。"
  - "張麗華競賽中提及逼白御行忘記其他女人、只要她，屬當場羞恥話語；不建立永久排他要求。"
  - "競賽中的主人、狗、跪、腳等語言不建立常設權力關係。"
```

## DIN18-E03｜蘇清彩頭與張麗華額外足部親密

```yaml
PRIZE_EXECUTION:
  event_id: "DIN18-E03-SUQING_FOOT_PRIZE"
  status: "COMPLETED"
  participants:
    - "白御行"
    - "蘇清"
  confirmed:
    - "白御行依賽果替蘇清脫鞋襪。"
    - "白御行舔、含吮蘇清兩足腳趾，並沿腳背、腳踝進行親密接觸。"
    - "白御行在一側跟腱附近輕咬。"
    - "蘇清沒有將此夜留床、性交或舊約履行與彩頭混算。"
  consent_scope:
    - "只限當次賽果與當場延續。"
    - "不形成未來可任意觸碰蘇清雙足或身體的權利。"
```

```yaml
ZHANG_LIHUA_FOOT_INTIMACY:
  event_id: "DIN18-E04-ZLH_FOOT_PLAY"
  status: "COMPLETED"
  confirmed:
    - "白御行另替張麗華脫鞋襪，以舌尖逐點舔觸腳底與足心。"
    - "張麗華接受當次互動並明示足心怕癢。"
  legal_effect:
    - "不是言語競賽獎勵。"
    - "不抵銷其後床上親密或建立常設義務。"
```

---

# 6｜李瓶兒與蘇清離場；張麗華取得獨宿夜

```yaml
DEPARTURE_DECISIONS:
  event_id: "DIN18-E05-PRIVATE_NIGHT_SELECTION"
  李瓶兒:
    decision:
      - "只收拾桌面、安排熱水。"
      - "明示不加入床上事件。"
      - "其後離開張麗華房間。"
    relation_effect:
      - "不因在場、收桌或觀看前段互動而構成性同意。"
  蘇清:
    decision:
      - "明示不加入張麗華與白御行的床上事件。"
      - "其後離開張麗華房間。"
    contract_effect:
      - "本夜不計入蘇清舊五百兩／三夜契約最後一日一夜之履行。"
      - "舊帳不因她參與晚膳或言語競賽而結清。"
  張麗華:
    confirmed:
      - "明示今晚不要觀眾，也不要幫手。"
      - "在兩人離場後親自落閂。"
  white_yuxing_disclosure:
    - "白御行其後表示自己今晚原本也只想與張麗華一人同宿，只是需要她先把界線說出口。"
```

---

# 7｜白御行 × 張麗華：當夜成人事件

## ZLH18-E01｜同意、避孕與語言偏好

```yaml
CONSENT_RECORD:
  consent_id: "CONSENT-H18-ZLH-BYX-PRIVATE_NIGHT-001"
  participants:
    - "白御行"
    - "張麗華"
  time_scope: "槐月十八日晚至停止點"
  accepted:
    - "接吻、脫衣、足部與全身親密。"
    - "性交。"
    - "由白御行主導節奏。"
    - "較快、較重、可使用粗俗直白的成人語言。"
  conditions:
    - "不得在張麗華體內射精。"
    - "張麗華保留停止、改變方式與拒絕額外行為的權利。"
    - "粗話不等於要求張麗華自我貶低或承認自己低賤。"
  effective_end:
    - "張麗華在第三個周天後選擇停止。"
    - "後續只同眠，不延續任何性同意至清晨。"
```

```yaml
ADULT_LANGUAGE_RELATIONAL_NOTE:
  confirmed:
    - "白御行明示自己要聽的是『粗話／下流話』，不是要求張麗華說自己低賤。"
    - "張麗華接受使用直白低俗的成人語言，但維持自身價值與人格位置。"
  scope: "本次成人場景與雙方既有關係語言偏好"
  not_established:
    - "張麗華必須在所有親密場合使用低俗語言。"
    - "低俗語言可取代每次具體同意。"
```

## ZLH18-E02｜性交、九淺一深周天與結果

```yaml
ADULT_EVENT:
  event_id: "ZLH18-E02-THREE_CYCLES_INTERCOURSE"
  status: "COMPLETED_AND_STOPPED"
  participants:
    - "白御行"
    - "張麗華"
  confirmed_sequence:
    - "雙方在前段攻防、玩笑與身體挑逗後進入性交。"
    - "白御行以自定義『九淺一深』節奏完成三個完整周天。"
    - "三個周天使用不同身體位置，其中包括張麗華轉身與被抱起承接。"
    - "張麗華在第三個周天結束後自述已滿足。"
  ejaculation_axis:
    internal_ejaculation: false
    ejaculation_elsewhere: "NOT_CONFIRMED"
  pregnancy_axis:
    current_status: "NOT_ESTABLISHED"
    confirmed:
      - "本次沒有體內射精。"
    prohibited_inference:
      - "不得寫成已懷孕。"
      - "不得寫成已確認不可能懷孕。"
```

## ZLH18-E03｜第四周天風險確認與停止

```yaml
STOP_EVENT:
  event_id: "ZLH18-E03-FOURTH_CYCLE_DECISION"
  status: "STOP_ACCEPTED"
  white_yuxing_statement:
    - "白御行明示若進入第四個周天，自己沒有把握仍能及時拔出避免體內射精。"
    - "他詢問張麗華要繼續，或在已滿足時收兵。"
  zhang_lihua_decision:
    - "張麗華選擇不進入第四個周天。"
    - "她明示三個周天已足夠，要求收兵。"
    - "她選擇今夜其後只相擁同眠，不再性交。"
  subsequent_boundary:
    - "白御行提出可在口中於場外射精。"
    - "張麗華拒絕，明示收兵不是另換戰場，口部只拿來親吻。"
  observed_result:
    - "性交停止。"
    - "沒有第四個周天。"
    - "沒有後續口交。"
    - "兩人相擁入睡，直到破曉前後。"
```

---

# 8｜白御行 × 張麗華：情感、嫉妒、酒莊與孩子

## ZLH18-E04｜互相明示喜歡

```yaml
RELATION_EVENT:
  event_id: "ZLH18-E04-MUTUAL_LIKING"
  status: "CONFIRMED_PRIVATE_RELATIONAL_STATEMENT"
  white_yuxing:
    - "白御行對張麗華說自己喜歡她。"
    - "他表示害怕將來離不開她。"
  zhang_lihua:
    - "張麗華明示她也喜歡白御行。"
    - "她不要求白御行因恐懼而被綁死。"
    - "她希望白御行能離開，但仍因選擇而回來。"
  relation_delta:
    - "雙方情人關係新增互相明示喜歡。"
  not_established:
    - "白御行只愛張麗華。"
    - "張麗華接受白御行所有其他關係而不再嫉妒。"
    - "婚姻、排他或永久承諾。"
```

## ZLH18-E05｜嫉妒與獨宿夜的真實原因

```yaml
JEALOUSY_RECORD:
  status: "ACTIVE_AND_ACKNOWLEDGED"
  zhang_lihua_position:
    - "她明示今晚確實生氣與吃醋。"
    - "她不要被要求『大肚、別吃醋』。"
    - "她接受白御行風流與多重關係的既有事實，但不接受自己總被排到最後或被要求替他接好所有場面。"
    - "她沒有強迫李瓶兒或蘇清離場；兩人各自決定不加入。"
  white_yuxing_position:
    - "白御行表示今晚其實也只想與張麗華一人。"
    - "他承認自己藉張麗華先出聲取得獨宿理由。"
  resulting_state:
    - "槐月十八日晚白御行與張麗華獨宿，是兩人當夜共同選擇。"
    - "此選擇只限當夜，不建立長期排他。"
```

## ZLH18-E06｜酒莊之獨一性與所有權再確認

```yaml
WINE_ESTATE_RELATIONAL_NOTE:
  existing_asset: "張麗華酒莊"
  white_yuxing_statement:
    - "白御行表示酒莊是給張麗華的獨一份，自己沒有第二個酒莊再送其他女人。"
  zhang_lihua_response:
    - "她喜歡此獨一性。"
    - "她再次明示酒莊是自己的產業，釀什麼、怎麼經營、誰能進酒窖由她決定。"
    - "酒莊不能被用作堵嘴、取消嫉妒或換取身體同意的代價。"
  legal_state:
    - "沿用既有『贈與但不控制』邊界。"
```

## ZLH18-E07｜李師師房內事件之直接揭露與傳聞分離

```yaml
DISCLOSURE_TO_ZHANG_LIHUA:
  event_id: "ZLH18-E07-RIRU_DISCLOSURE"
  source: "白御行直接轉述自己的行動"
  confirmed_to_zhang_lihua:
    - "白御行下午與李師師性交。"
    - "李師師同意白御行在她體內射精。"
    - "白御行射精後對她說『我愛你』。"
    - "白御行隨後立即離開，趕來張麗華房中吃飯。"
    - "李師師因其突兀離開向門口丟出物件／枕頭。"
  zhang_lihua_reaction:
    - "她理解李師師為何生氣。"
    - "她拒絕替李師師判定是否接受白御行的愛。"
    - "她指出派人催飯不等於命令白御行在情事後不作安頓便離開。"
```

```yaml
PUBLIC_RUMOR_REGISTRY:
  observed_before_direct_disclosure:
    - "觀止有人聽見李師師房內一聲碰響。"
    - "有人看見白御行離開得比平日快。"
  circulating_versions:
    - "白御行惹李師師生氣。"
    - "白御行偷親後便跑。"
    - "李師師被欺負狠了而惱羞。"
  objective_status:
    - "上述版本均不是完整真相。"
    - "張麗華現有的直接資料來自白御行本人，仍不等於外界公開知情。"
```

## ZLH18-E08｜孩子議題仍未決

```yaml
CHILD_DISCUSSION:
  event_id: "ZLH18-E08-CHILD_UNDECIDED"
  status: "ACTIVE_UNDECIDED"
  white_yuxing_statement:
    - "白御行表示李師師願意幫他生孩子，並以張麗華仍在考慮作為兩者差異。"
    - "白御行表示自己想像張麗華適合生兒子，並以外貌與民間經驗開玩笑。"
  authority_limit:
    - "白御行關於李師師願意生孩子之說法，是他對既有談話的轉述。"
    - "本檔只確認李師師同意當次體內射精；是否已有完整共同生育協議，仍未另行固化。"
  zhang_lihua_position:
    - "她拒絕拿是否生孩子與李師師競爭愛的深淺。"
    - "她表示自己確實想過與白御行有孩子，某些時候甚至想要。"
    - "她尚未同意現在受孕、體內射精或立即開始生育。"
    - "她要求先考慮身體、生活、酒莊、名分、居所、養育與白御行是否在場等現實。"
    - "她不接受由屁股形狀或老人話決定胎兒性別。"
    - "若生女兒，也必須被疼愛，不得因像她、兇悍或『惑亂天下』而被嫌棄。"
  current_joint_state:
    - "沒有共同生育協議。"
    - "沒有當夜受孕嘗試。"
    - "議題保留待未來再談。"
```

---

# 9｜蘇清、李瓶兒與其他人物當前硬狀態

```yaml
ACTOR_STATE:
  蘇清:
    current_location: "已離開張麗華房間；精確位置未知"
    confirmed_evening:
      - "接受黑色肚兜。"
      - "參與言語競賽並以二比一獲勝。"
      - "接受白御行完成兩足彩頭。"
      - "拒絕加入張麗華與白御行的床上事件。"
    old_contract:
      state: "ACTIVE_OUTSTANDING"
      remaining: "舊五百兩／三夜契約最後一日一夜仍欠白御行"
      explicit_lock:
        - "槐月十八日晚的晚膳、競賽與足部彩頭不算舊約履行。"
        - "跨日不自動消滅或結清此帳。"
    private_28_day_pact:
      state: "AGREED_NOT_TRIGGERED"
      trigger: "西門慶真正被毀並形成實質報仇結果"
    immediate_due:
      - "槐月十九日完成白玉池第二次回顯／滲漏確認。"

  李瓶兒:
    current_location: "已離開張麗華房間；精確位置未知"
    confirmed_evening:
      - "接受白色肚兜。"
      - "作言語競賽裁判，不參賽。"
      - "明示只收桌、安排熱水，不加入床上事件。"
    relationship_with_bai:
      state: "UNDECIDED"
      unresolved:
        - "是否成為白御行的女人。"
        - "關係位置、排他、身體界線。"
        - "是否共同生育及母子公開位置、姓氏、居所、養育與保護責任。"
      due_status:
        - "她原先將回答延後至兩日安排結束後。"
        - "槐月十八日已結束，議題自槐月十九日起到期，但她尚未給答案。"

  李師師_師理理:
    current_location: "精確位置未知；槐月十八日晚原有戌初設席"
    relation_with_bai:
      - "如夫人關係框架已口頭接受，尚未觀察到公開實施。"
      - "她在關係存續期間同意不與其他男人上床。"
      - "她保留住觀止、設席與房門自主。"
    unresolved:
      - "她是否與如何回應白御行的『我愛你』。"
      - "當次體內射精是否導致懷孕。"
      - "如夫人位置何時、如何對外實施。"

  張麗華:
    current_location: "自己房內／與白御行同床"
    relation_with_bai:
      - "情人關係持續。"
      - "私下稱白御行『官人』；白御行稱她『小娘子』。"
      - "雙方互相明示喜歡。"
      - "她有真實嫉妒，不接受被要求取消。"
      - "她尚未同意生育。"
    wine_estate:
      - "酒莊為其私人產業與實際管理範圍。"

  紅娘:
    confirmed_evening:
      - "接受紅色肚兜。"
    later_scene: "未參與張麗華房內私人夜"

  小翠:
    confirmed_evening:
      - "接受綠色肚兜。"
      - "拒絕任何由顏色玩笑延伸出的十客或性義務。"
    later_scene: "未參與張麗華房內私人夜"

  春梅:
    gift_status:
      - "黃色肚兜已交張麗華代為妥善贈送。"
      - "是否已實際收到，尚未觀察。"
```

---

# 10｜商戰背景保留與槐月十九日到期事項

```yaml
TRADE_WAR_ACTIVE_STATE:
  source: "HOT V2.1"
  unchanged_confirmed:
    - "常煒仍在執行對廣源轉運行／許奉年之第一擊。"
    - "西門慶已被拉入公函、盤口與外界推斷場，但尚未證實涉案或倒台。"
    - "沈萬三可能是關聯節點、目標或旁觀者，未鎖定為幕後主使。"
    - "潘金蓮已準備切帳、保護賭客本金、延後西門慶部分分成，並可能送模糊警告。"
  no_new_observed_update:
    - "槐月十八日晚私人生活場未收到可核對的商戰新回報。"
  immediate_due:
    - "白御行已明示槐月十九日回定陶商會查看後續。"
```

```yaml
IMMEDIATE_DUE_ITEMS_HUAI19:
  - "白御行是否按原計畫回定陶商會。"
  - "常煒第一輪商戰回報：廣源、許奉年、西門慶周邊、內部分號與沈萬三之反應。"
  - "蘇清完成白玉池第二次回顯／滲漏確認；若穩定，轉入復開準備。"
  - "李瓶兒延後至兩日結束後的關係與孩子回答已到期，但仍須由她自己選擇何時回答。"
  - "蘇清舊五百兩／三夜契約最後一日一夜仍未結清，需另行安排或重議。"
  - "李師師如夫人關係框架尚待對外實施方式；她對『我愛你』的回應仍未知。"
  - "黃色肚兜是否已由張麗華交給春梅。"
```

---

# 11｜知情矩陣與秘密範圍

```yaml
KNOWLEDGE_MATRIX:
  李師師如夫人框架:
    knows:
      - "白御行"
      - "李師師／師理理"
    may_know_later: "未確認"
    public_state: "NOT_PUBLICLY_IMPLEMENTED"

  李師師當次性交與體內射精:
    direct_participants:
      - "白御行"
      - "李師師／師理理"
    later_directly_told:
      - "張麗華"
    public_state: "PRIVATE"

  白御行對李師師說愛:
    knows:
      - "白御行"
      - "李師師／師理理"
      - "張麗華（由白御行直接告知）"
    public_state: "PRIVATE"

  言語競賽完整內容:
    knows:
      - "白御行"
      - "張麗華"
      - "蘇清"
      - "李瓶兒"
    authority: "GAME_TEXT_ONLY"

  蘇清足部彩頭:
    knows:
      - "白御行"
      - "蘇清"
      - "張麗華"
      - "李瓶兒"
    public_state: "ROOM_PRIVATE"

  張麗華獨宿夜成人細節:
    knows:
      - "白御行"
      - "張麗華"
    public_state: "STRICTLY_PRIVATE"
    no_automatic_leak_to:
      - "李瓶兒"
      - "蘇清"
      - "李師師"
      - "潘金蓮"
      - "觀止其他人"

  張麗華孩子未決:
    knows:
      - "白御行"
      - "張麗華"
    public_state: "PRIVATE"

  白玉池第一輪檢查:
    knows:
      - "白御行"
      - "蘇清"
    broader_operational_knowledge: "依實際整理人員接觸範圍，未自動補造"
```

---

# 12｜禁止污染與未決事項

```yaml
ANTI_CORRUPTION_LOCKS:
  - "不得把蘇清言語競賽第三局之未來想像寫成真實告白、愛情成立或二十八日後必然留下。"
  - "不得把張麗華競賽與床上粗話寫成她已接受自我低賤、永久服從或常設角色。"
  - "不得把足部彩頭擴張成白御行可隨時碰蘇清或張麗華雙足的權利。"
  - "不得把李瓶兒收桌、備水或在場觀看寫成她同意床上加入。"
  - "不得把蘇清晚膳、競賽或足部彩頭算入舊五百兩／三夜契約最後一日一夜。"
  - "不得把李師師設席寫成她與客人上床。"
  - "不得把李師師同意一次體內射精，擴張成永久受孕義務、已懷孕或已完整同意替白御行生孩子。"
  - "不得把白御行對李師師說愛，寫成李師師已回應或接受。"
  - "不得把張麗華想過孩子、某些時候想要，寫成她已同意現在受孕或體內射精。"
  - "不得把白御行與張麗華當夜獨宿，寫成長期排他或他已承諾不見其他女人。"
  - "不得把酒莊當成白御行可控制張麗華、買斷嫉妒或換取性同意的資產。"
  - "不得把張麗華房內成人細節無因果洩漏給其他人物。"
  - "不得因當夜沒有商戰回報，推定廣源、西門慶、沈萬三或潘金蓮沒有行動。"
  - "不得重新把白玉池寫成失控謎案；槐月十九日只需第二次穩定確認。"
```

```yaml
UNRESOLVED:
  trade_war:
    - "廣源轉運行與許奉年如何反應。"
    - "西門慶是否收到公函或潘金蓮警告。"
    - "沈萬三是否涉案、被利用、被嫁禍、旁觀或反擊。"
    - "常煒差異查核釣出哪些內部異動。"
  white_jade_pool:
    - "第二次回顯／滲漏確認結果。"
    - "復開日期、營業規則與第一批使用者。"
  li_shishi:
    - "她對白御行『我愛你』的回答。"
    - "如夫人位置對外實施方式。"
    - "當次體內射精是否導致懷孕。"
  zhang_lihua:
    - "孩子議題是否、何時重新談。"
    - "槐月十九日醒後對白御行回商會之反應。"
    - "黃色肚兜是否已交春梅。"
  li_pinger:
    - "關係與孩子議題到期後的回答。"
  su_qing:
    - "舊約最後一日一夜何時、如何履行或重議。"
    - "二十八日私約是否及何時被觸發。"
```

---

# 13｜破曉接關

```yaml
RESUME_POINT:
  date: "理火三年槐月十九日"
  time: "破曉，天色將明"
  location: "張麗華房間／床上"
  present:
    - "白御行"
    - "張麗華"
  immediate_state:
    - "昨夜成人事件已停止，兩人依約相擁同眠。"
    - "張麗華已明示滿足，未同意將昨夜性同意延續到清晨。"
    - "房門仍為私人空間；是否已有外人敲門、送信或備早膳，尚未發生。"
    - "白御行今日原定回定陶商會。"
    - "蘇清今日應做白玉池第二次穩定確認。"
    - "李瓶兒延後的關係／孩子問題已到可回答時點，但不可強迫她立即回答。"
  possible_world_hinges:
    - "天光、院內晨聲或張麗華先醒。"
    - "定陶商會使者送來第一輪回報。"
    - "蘇清來報白玉池第二次檢查安排。"
    - "李瓶兒依自己意願在適當時機談延後問題。"
  player_decision_required_now: false
```

---

# 14｜導演快速載入

```yaml
DIRECTOR_QUICK_LOAD:
  - "現在是槐月十九日破曉，白御行與張麗華在她房內相擁睡過一段，性行為已停止。"
  - "昨夜張麗華只要白御行一人；李瓶兒與蘇清各自明示不加入並離場。"
  - "白御行與張麗華完成三個自定義九淺一深周天；沒有體內射精，是否在外射精未確認。"
  - "白御行警告第四周天可能無法及時拔出，張麗華選擇停止；她也拒絕改用口部讓他射精，兩人只抱睡。"
  - "雙方互相明示喜歡；張麗華有真實嫉妒，不接受被要求取消。她尚未同意生孩子。"
  - "酒莊仍是張麗華私人產業，屬白御行給她的獨一份，但不能換取沉默、服從或性同意。"
  - "李師師下午口頭接受如夫人關係框架，保留住觀止、設席與房門自主；關係存續期間不與其他男人上床。公開實施尚未發生。"
  - "白御行與李師師下午性交，李師師在停止後重新同意較快較重及體內射精；懷孕未知。白御行說愛後立即離開，李師師未回答並丟枕頭。"
  - "言語競賽由蘇清二比一勝張麗華；競賽台詞不是告白或承諾。白御行已完成舔蘇清兩足之彩頭。"
  - "蘇清舊五百兩／三夜契約最後一日一夜仍未結清；二十八日私約仍未觸發。"
  - "白玉池第一輪開池前檢查穩定、已換水；今日再查一次回顯／滲漏，穩定後可進復開準備。"
  - "白御行今日原定回定陶商會；商戰仍在外部運行，昨夜沒有新回報不代表沒有動作。"
  - "李瓶兒延後至兩日安排結束後的關係與孩子回答，從今日起已到期但仍由她自主決定何時回答。"
```

> **接關畫面：天將亮，張麗華房裡的紅帳早已不是昨夜花燭，而是兩人收兵後的安靜。她尚在白御行懷裡；門外是否已有定陶來使、白玉池回報或晨間腳步，下一幕才會發生。**

<!-- SOURCE_HOT_V2_2_END -->

---

## SOURCE ARCHIVE｜HOT V2.3

**檔名：** `觀止青樓_白御行線_HOT_SAVE_V2.3_槐月二十日深夜_沈萬三合作與師師薄情郎席前接關版.md`  
**SHA-256：** `0f943eb273b6cda36179cc9212b24d0abc4edfd8457f7111f422efee55759901`

<!-- SOURCE_HOT_V2_3_BEGIN -->
# 觀止青樓｜白御行線 HOT SAVE V2.3
## 理火三年槐月二十日深夜｜定陶沈家停止試探 × 偽牌高爐案移交開封府 × 師師薄情郎受審席前 × 瓶兒麗華雙向接關版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V2_3_HUAI20_LATE_NIGHT_SHEN_COOPERATION_RIRI_TRIAL_SEAT"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V2.3"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime:
    - "GUANZHI_QINGLOU_V10_0"
    - "GUANZHI_QINGLOU_V10_1_TO_V10_2_PATCH_WHEN_APPLICABLE"
  story_date: "理火三年槐月二十日深夜"
  date_basis:
    - "HOT V2.2 停於槐月十九日破曉。"
    - "商會偽鹽案於槐月十九日白日展開。"
    - "相國寺瓦市公開試烤明示發生於其後『第二日午前』，故為槐月二十日。"
    - "沈萬三觀止夜宴、李師師房外衝突與本接點均發生於同日晚間至深夜。"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "ACTIVE_PAUSED_AT_PLAYER_CHOICE_BETWEEN_LI_PINGER_AND_ZHANG_LIHUA"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V2.2_槐月十九日破曉_師理理如夫人前置與張麗華獨宿夜結版.md"
  current_location: "觀止內院東西廊交界"
  present:
    - "白御行"
  nearby_but_not_in_same_private_scene:
    - "李瓶兒房中仍亮燈；其丫頭持披風在東廊候命。"
    - "張麗華房中仍亮燈；其侍女在西廊候命，燈已挑暗一層。"
  save_scope:
    - "槐月十九日定陶商會被栽私鹽、偽造舊封與副會長腰牌案"
    - "開封府介入、證物鏈、河東池鹽與定陶加工品法位"
    - "相國寺瓦市三炒鹽公開試烤、三烤末批與六烤奢侈品策略"
    - "高溫爐材、偽牌印模、城北廢鑄錢坊與官面涉案線"
    - "沈萬三與定陶停止代理試探、陶瓷金屬研發起點合作框架"
    - "西門慶、廣源與巡檢司之待查關聯"
    - "蘇清五百兩三夜舊契結清、二十八日／二十九日私人約"
    - "白玉池秘密對沈家高層擴大知情，但仍封池、未投資、未營業"
    - "觀止夜宴、紅綠組、肚兜試用品、早餐試餐與沈萬三留宿"
    - "李師師怒砸負心漢之混合真情／演出事件與翌日受審席"
    - "白御行當前尚未決定投宿李瓶兒或返回張麗華房"
```

---

# 0｜提交法位、來源與反污染說明

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V2.2_槐月十九日破曉_師理理如夫人前置與張麗華獨宿夜結版.md"
    role: "師理理如夫人前置、張麗華私夜、商戰前置、白玉池第一輪復開檢查之直接來源"
  long_term_master:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版.md"
    role: "較早玩家線因果來源；另由本輪同步生成之新 MASTER V4.1-R1 固化至 HOT V1.9"
  route_conversation_commit:
    role: "槐月十九日破曉後至槐月二十日深夜的直接劇情來源"
  forbidden_source:
    file: "HOT_SAVE_V1.3"
    status: "ILLEGAL_CORRUPTED_SAVE"
    use: "AUDIT_ONLY"

COMMIT_NOTE:
  - "本檔取代 HOT V2.2，成為白御行線當前直接接關切片。"
  - "本檔不把槐月十九日至二十日事件倒灌人物卡或人物池基線。"
  - "商人推論、開封府初步判斷、前廣源帳房口供、街頭傳聞、誘餌消息與客觀定罪分軸保存。"
  - "沈萬三與定陶只達成口頭停止試探與技術合作原則；未簽盟書、未完成技術交付、未形成共同統治京師。"
  - "西門慶、巡檢司、廣源與偽牌高爐案之關聯仍待官府查證；不得因貨車去向與口供直接宣判謀逆。"
  - "李師師怒砸事件含真實舊怨與雙方同意的宣傳演出；不得全部改寫成純戲，也不得全部改寫成不可修復的真決裂。"
  - "白御行公開稱『女人每月一次情緒不穩』只保存為其當場說法；不是李師師月事、身體或情緒原因之客觀事實。"
  - "當前停在投宿選擇之前；不得替白御行走向任何一房。"
```

---

# 1｜當前時間、位置與停止點

```yaml
CURRENT_SCENE:
  date: "理火三年槐月二十日"
  time: "深夜，沈萬三觀止宴仍在內樓延續，白御行已離開李師師房外公演現場"
  location: "觀止內院東西廊交界"
  player_state:
    clothing:
      - "衣襟曾被李師師為演出扯鬆。"
      - "腰帶曾被扯歪。"
      - "袖口有一道為演出劃出的外層破口，未傷皮肉。"
      - "褲腿沾有李師師擲下之香粉。"
    alcohol: "未飲酒；主要飲用醉花特調蜂蜜茶與茶水。"
    inner_state_by_player:
      - "白御行自述『夾起尾巴』。"
      - "正在考慮去李瓶兒房或回張麗華房。"
  next_action_owner: "PLAYER"
```

```yaml
EAST_CORRIDOR_LI_PINGER:
  observable:
    - "李瓶兒尚未睡，房中有燈。"
    - "其丫頭奉命出來查看前樓動靜。"
    - "丫頭帶來一件披風。"
  message:
    - "若白御行只是喝多，可送醒酒湯。"
    - "若受傷，可先進房讓李瓶兒看看。"
  boundary:
    - "李瓶兒沒有說白御行一定可以進房。"
    - "沒有建立留宿、同床或性同意。"
```

```yaml
WEST_CORRIDOR_ZHANG_LIHUA:
  observable:
    - "張麗華房中有燈，侍女在西廊傳話。"
    - "侍女傳話後將燈挑暗一層。"
  message:
    - "張麗華不問白御行今晚去了誰房裡。"
    - "也不問他為何被砸成這樣。"
    - "昨夜睡過的枕頭仍在。"
    - "白御行若回去，張麗華會命人備水。"
    - "若不回去，她現在就熄燈。"
  boundary:
    - "不是強迫返回。"
    - "不是整夜無限等待。"
    - "沒有自動延續昨夜性同意。"
```

---

# 2｜槐月十九日：定陶商會被栽私鹽案

## DTC19-E01｜兩車被扣與偽造證物

```yaml
EVENT_RECORD:
  event_id: "DTC19-E01-SEIZED_CARTS_FALSE_SALT_CASE"
  time: "槐月十九日清晨至上午"
  location: "京師城南巡檢轄區／定陶商會京師總會"
  status: "ACTIVE_OFFICIAL_CASE"
  confirmed_report:
    - "兩輛掛定陶商會名義的貨車被城南巡檢扣留。"
    - "車底藏有私鹽。"
    - "車上出現定陶商會三年前停用之『玄字九號』真舊封。"
    - "車上有一封寫給白御行的信：『舊帳未清，死人也會說話。』"
    - "車夫留在現場並要求見白御行或常煒。"
  badge_claim:
    - "車夫稱途中有人持副會長腰牌，以修軸名義接觸貨車。"
    - "常煒本人腰牌沒有遺失。"
    - "由此形成腰牌被仿製之高度嫌疑，但仿製者當時未知。"
```

## DTC19-E02｜舊案證物箱與失蹤帳頁

```yaml
EVIDENCE_CHAIN:
  event_id: "DTC19-E02-OLD_CASE_EVIDENCE_BREACH"
  status: "CONFIRMED_BREACH"
  confirmed:
    - "前次失鹽案證物箱曾由背面被秘密打開。"
    - "死去帳房之私簿缺少六頁。"
    - "玄字九號舊封原應銷毀，但實物外流。"
    - "舊封清理經手人共四名：一人死於前案、一人離職失蹤、一人仍在商會且昨夜值西倉、一人現任廣源轉運行二掌櫃。"
    - "涉案貨車車底改造至少在半月前完成，不是臨時栽放。"
  not_established:
    - "仍在商會之經手人已涉案。"
    - "離職者已死亡或被控制。"
    - "廣源二掌櫃受何人指使。"
```

## DTC19-E03｜開封府介入與雙向調查

```yaml
OFFICIAL_INTERVENTION:
  event_id: "DTC19-E03-KAIFENG_TAKES_CUSTODY"
  trigger:
    - "白御行致書開封府尹，要求由開封府接手，並援引趙受益曾到觀止、包府尹曾作見證之既有官面關係。"
  confirmed_actions:
    - "開封府接管兩車、車夫、私鹽、書信與相關證物。"
    - "同時封查定陶商會西倉並索取帳冊與往來文書。"
    - "開封府明示：巡檢司與定陶商會兩邊都查。"
    - "白御行曾投放之謠言、假線與實證須分冊列明。"
  legal_position:
    - "定陶商會自稱本案被栽贓與偽證受害方。"
    - "開封府尚未因定陶自稱受害即免除查核。"
```

## DTC19-E04｜鹽源與定陶產品法位

```yaml
SALT_IDENTIFICATION:
  event_id: "DTC19-E04-SALT_ORIGIN_AND_PROCESSING_STATUS"
  confirmed_by_inspection:
    - "被扣鹽為品質較高、接近官規的河東解池池鹽。"
    - "鹽有官倉式篩整、壓實與包裝痕跡。"
    - "與前次定陶失鹽案被盜之鹽不是同批、同源。"
    - "不是定陶慣用的齊地海鹽原料，也不是定陶三烤或六烤成品。"
  bai_yuxing_business_explanation:
    - "定陶商會不是持牌鹽商，不生產原鹽。"
    - "定陶向齊地沿海具資格鹽商購買合法官鹽，每批有商家號與官面貨單。"
    - "官鹽進烤坊前須由定陶均輸平準司查驗；無官鹽貨單不得入窯。"
    - "每窯保存投入、產出、查驗與損耗紀錄。"
    - "三烤、六烤、九烤是對合法原鹽加工後的高價產品，不等於定陶販賣私鹽。"
  current_legal_effect:
    - "上述制度可供查核，不自動免除對具體帳冊與貨號的驗證。"
```

---

# 3｜三烤、六烤、九烤與相國寺瓦市公開場

## SALT19-E01｜不急於壓制傳聞

```yaml
PUBLIC_RELATIONS_POLICY:
  event_id: "SALT19-E01-LET_RUMOR_RUN_AND_COMPARE"
  player_decision:
    - "白御行命商會不慌亂、不急於全面否認。"
    - "讓市場自己比較被扣河東鹽、普通市鹽與定陶產品。"
  observed_effect:
    - "部分富戶購買定陶產品與普通鹽回家比較。"
    - "民間以鐵鍋反覆乾炒鹽之模仿多有焦苦、結塊與飛濺問題。"
  not_established:
    - "所有京師消費者已信任定陶。"
    - "本案已因市場比較結束。"
```

## SALT19-E02｜三烤竹鹽之未公開工藝點

```yaml
TRADE_SECRET_STATE:
  confirmed_by_bai_yuxing:
    - "定陶三烤之風味不只來自受熱。"
    - "實際核心之一是竹筒、封泥與火候；可稱『三烤竹鹽』。"
    - "商品名過去省略『竹』字。"
  strategy:
    - "公開試烤前不主動揭露竹筒、封泥與完整程序。"
    - "以盲碗、味道、工序問答與官方紀錄辨認真假舊匠。"
  knowledge_scope:
    - "白御行"
    - "常煒"
    - "定陶鹽務掌眼與相關高層"
    - "開封府在場書吏知道工藝有未公開差異，但不掌握完整配方"
```

## SALT19-E03｜九烤鹽與高溫能力

```yaml
NINE_ROAST_STATE:
  event_id: "SALT19-E03-NINE_ROAST_FIRST_BATCH"
  player_statement:
    - "九烤鹽需將鹽加熱至熔融／近熔融處理，實際爐溫須高於一般灶火。"
    - "定陶於上月已做出第一批，白御行於槐月十八日晚才得知成功。"
  official_preservation_order:
    - "開封府向定陶均輸平準司發文，要求封存首批、原料紀錄、九次窯程、損耗與驗收簿。"
    - "要求隨機封三份樣品，分存開封府、地方官署與定陶商會。"
    - "兩路快馬赴定陶。"
  current_delivery_state: "NOT_CONFIRMED_ARRIVED_IN_JINGSHI"
  anti_inference:
    - "不得因白御行宣布成功，補寫樣品已到京。"
    - "不得補寫九烤已正式上市、已入宮或已形成固定價格。"
```

## SALT20-E01｜對方公開試烤與「三炒鹽」命名

```yaml
PUBLIC_CHALLENGE:
  event_id: "SALT20-E01-XIANGGUOSI_PUBLIC_TEST"
  time: "槐月二十日午前"
  location: "相國寺瓦市"
  opponent_claim:
    - "任取市鹽，反覆加熱三次即可製成與定陶三烤無異之鹽。"
    - "若有差異，願賠銀百兩。"
  player_counter_language:
    - "白御行將其產品稱為『三炒鹽』。"
    - "稱其適合倒入隔夜飯、加雞蛋作蛋炒飯。"
  legal_status:
    - "三炒鹽是白御行與現場群眾對其工法的嘲諷稱呼。"
    - "不是官府產品分類，也不是定陶商會正式商品名。"
```

## SALT20-E02｜三烤末批、六烤倍價與奢侈品策略

```yaml
SALES_EVENT:
  event_id: "SALT20-E02-LAST_THREE_ROAST_SIX_ROAST_PREMIUM"
  time: "槐月二十日相國寺瓦市公開場"
  confirmed:
    - "定陶將京師未售完之三烤鹽帶至現場。"
    - "對外標示為京師最後一批三烤，售完不再補貨。"
    - "宣稱未來以六烤為主。"
    - "六烤售價定為三烤的兩倍。"
    - "三烤現場形成購買與排隊，庫存下降。"
  brand_position:
    - "白御行明示定陶賣的不是普通鹽，而是奢侈品。"
    - "定陶不以人人買得起為目標。"
  not_established:
    - "三烤全數售罄。"
    - "六烤長期市場價格已不可變更。"
    - "九烤價格與客群已正式公布。"
```

## SALT20-E03｜假舊匠、當眾失言與拘捕

```yaml
FALSE_CRAFTSMAN:
  event_id: "SALT20-E03-FAKE_OLD_CRAFTSMAN"
  confirmed_observable:
    - "對方帶來一名自稱定陶舊匠之人。"
    - "其對掌火者喊出『風不能這樣收，爐氣一斷，後面全廢』，顯示其熟悉爐火與風門。"
    - "其後仍當眾聲稱鐵鍋炒製鹽與定陶三烤『並無大異』。"
    - "開封府進場封存鹽、鍋、炭、爐材與證人。"
    - "該人試圖逃跑，被差役拘捕。"
    - "其身上掉出一枚刻『武』字小銅牌。"
  not_established:
    - "其真實姓名。"
    - "其是否曾在定陶工作。"
    - "『武』字牌所屬組織。"
    - "其是否參與謀反。"
```

---

# 4｜耐火爐材、廢鑄錢坊與偽牌案

## FURN20-E01｜高溫磚與江南追查方向

```yaml
FURNACE_BRICK:
  event_id: "FURN20-E01-REFRACTORY_BRICK_LEAD"
  confirmed_observable:
    - "瓦市灶臺器材中找到帶鐵渣的耐火爐磚碎片。"
    - "老掌眼判斷其不是普通灶磚，曾接觸高溫與鐵渣。"
  player_hypothesis:
    - "原料可能與蘇州高嶺土或江南耐火料貨路有關。"
    - "可故意放出開封府已辨出蘇州料之風聲，觀察沈萬三是否反應。"
  objective_status:
    - "蘇州來源未經化驗或帳證確定。"
    - "原土產地、製磚地、使用爐址與最後轉手地可能不同。"
```

## FURN20-E02｜廣源舊車與過度整齊的線索

```yaml
TRANSPORT_LEAD:
  confirmed:
    - "瓦市器材所用車輛經刮漆後露出『廣源』舊字。"
    - "車板夾縫有細白泥屑與藍布線。"
  investigator_assessment:
    - "『廣源』兩字留下得過於容易辨認，可能是故意引導。"
  current_state:
    - "廣源仍是實際重要節點與嫌疑商號。"
    - "但車字本身不能單獨證明許奉年策劃全案。"
```

## FURN20-E03｜沈萬三船單與「佛像底座」假名目

```yaml
SHEN_DOCUMENTS:
  event_id: "FURN20-E03-SHEN_SHIP_LISTS"
  source: "沈萬三於觀止夜宴主動帶來之船單與人證"
  confirmed_as_documents_present:
    - "半年內經沈家船隊入汴梁之高嶺土、礬土、耐火泥共十七批。"
    - "其中十四批有明確官坊或瓷窯收貨紀錄。"
    - "三批買主為廣源轉運行，卻未進廣源自倉。"
    - "前廣源帳房之小冊將相關貨物記為『佛像底座』。"
    - "其中一批被指向城北廢棄鑄錢坊。"
  evidence_status:
    - "船單與私冊已在席上展示。"
    - "真偽與完整性仍須官府驗證。"
```

## FURN20-E04｜開封府搜查廢鑄錢坊

```yaml
OFFICIAL_SEARCH_REPORT:
  event_id: "FURN20-E04-ABANDONED_MINT_SEARCH"
  confirmed_by_short_official_note:
    - "開封府封鎖城北廢鑄錢坊。"
    - "現場未搜得成批完成兵器。"
    - "找到三座仍有餘溫之高溫爐。"
    - "找到多種尚未打磨完成的銅鐵腰牌。"
    - "找到官坊、巡檢司、商會與軍中使用之多類印模。"
    - "根據爐灰、車痕與空箱，官差推定到達前至少兩車成品被轉走。"
  legal_status:
    - "構成偽造官牌、印信與可能軍器相關之重大官案。"
    - "尚未因現場器材直接完成謀逆定罪。"
```

## FURN20-E05｜兩車去向之口供

```yaml
TESTIMONY:
  event_id: "FURN20-E05-TWO_CART_DESTINATIONS"
  source: "沈萬三帶來之前廣源帳房"
  statement:
    - "許奉年每月替一名未明人物空出兩輛車。"
    - "一車從西門府後門進入。"
    - "一車送入巡檢司。"
  status: "WITNESS_TESTIMONY_NOT_FINAL_ADJUDICATION"
  immediate_effect:
    - "西門慶、廣源轉運行與巡檢司之關聯由傳聞提升為有具體口供待查。"
    - "商人方明示後續偽牌、官署與可能軍器事項交由包府尹／開封府處理。"
```

---

# 5｜沈萬三觀止夜宴：敵友邊界與技術合作

## SHEN20-E01｜觀止設席與雙方高層到場

```yaml
MEETING:
  event_id: "SHEN20-E01-GUANZHI_HIGH_LEVEL_DINNER"
  time: "槐月二十日晚"
  location: "觀止二樓議事／宴席房"
  dingtao_side:
    - "白御行"
    - "常煒"
    - "京師總會師爺"
    - "倉運老掌櫃"
    - "鹽務掌眼"
    - "兩名高階帳房"
  shen_side:
    - "沈萬三"
    - "京師總代理"
    - "江南船務總管"
    - "爐料老牙人"
    - "前廣源帳房"
  guanzhi_hosts_or_present:
    - "潘金蓮"
    - "蘇清"
    - "紅袖"
    - "浮香"
    - "醉花"
    - "紅娘氏"
    - "小翠"
    - "後續自願上席之成年姑娘與觀止人員"
  table_rule:
    - "無固定上首。"
    - "先吃飯、酒過三巡再對帳。"
    - "白御行不飲酒，醉花為其備蜂蜜茶。"
```

## SHEN20-E02｜沈萬三眼紅之產業與白御行之反揭示

```yaml
INDUSTRIAL_DISCLOSURE:
  shen_initial_answer:
    - "沈萬三明示最眼紅定陶鋼鐵、軍備工坊與制度化工業能力。"
  bai_yuxing_correction:
    - "白御行明示定陶真正核心不是煉鋼煉鐵，而是『陶瓷金屬』。"
    - "常煒展示定陶氧化鋁合金車床刀頭／鑽頭樣品。"
    - "現場以刀頭削切精鋼，刃口未見立即翻捲。"
  world_status:
    - "定陶陶瓷金屬技術在白御行線已由玩家設定與現場樣品展示成立。"
    - "完整成分、燒結溫程、工藝與產能未公開。"
```

## SHEN20-E03｜跨時間線研發起點合作框架

```yaml
TECH_COOPERATION_FRAME:
  status: "ORAL_PRINCIPLE_ACCEPTED; FORMAL_CONTRACT_AND_TECH_DELIVERY_PENDING"
  time_line_structure:
    dingtao: "白御行漢末線"
    shen: "沈萬三明朝線"
    intersection: "觀止京師交會點"
  bai_offer:
    - "定陶不交出全套現成工法。"
    - "可提供研發起點、材料方向與已知失敗坑。"
    - "沈萬三在明朝線以明朝自己的人、料、銀與試驗發展。"
    - "定陶不直接下場替明朝線完成工業跨越，避免由定陶直接破壞其時空穩定。"
  shen_acceptance:
    - "接受取得種子與避坑，而非搬走整棵樹。"
    - "不挖定陶現役匠人。"
    - "不買通帳房，不偷窯圖、配方、溫程或模具。"
    - "明朝線自行研發形成之後續工法可歸沈家，但不得冒稱定陶完整傳授。"
    - "若大明線同類產品進入觀止京師交會點，先通知定陶再談市場邊界。"
  pending:
    - "具體研發起點內容。"
    - "可提供之樣品數量。"
    - "正式對價、交付順序、保密與違約條款。"
```

## SHEN20-E04｜停止代理試探與第三方遮護

```yaml
NON_AGGRESSION_UNDERSTANDING:
  status: "ORAL_MUTUAL_UNDERSTANDING_WITNESSED"
  confirmed_terms:
    - "定陶與沈家不再借廣源、西門慶或其他本地商號投石試水。"
    - "第三方若拿一家名義碰另一家之貨、帳、匠人或官面，先直接通報求證。"
    - "沈家不替廣源遮帳。"
    - "西門慶若向沈家借船、借錢、藏貨或轉帳，沈家不因舊交替其開方便門。"
    - "定陶如何處理自身敵人，由定陶自行決定；沈家不承諾派人、遞刀或共同承擔。"
    - "雙方不立共治京師盟書，不形成對官府之結黨名冊。"
  not_established:
    - "永久軍事同盟。"
    - "共同瓜分京師。"
    - "沈家已參與定陶對西門慶之任何具體行動。"
```

## SHEN20-E05｜「沈萬三要殺西門慶」錯誤風言結清

```yaml
RUMOR_SETTLEMENT:
  previous_operation:
    - "白御行曾透過潘金蓮投放『沈萬三要殺西門慶』之未證實消息。"
  current_public_between_parties:
    - "白御行明示該說法只是定陶收到的錯誤風言。"
    - "當面查證後，確認沒有沈萬三欲殺西門慶這回事。"
    - "沈萬三接受此說法。"
    - "定陶與沈家均承諾日後對外以錯誤風言、查無此事處理。"
  legal_effect:
    - "不得再以沈萬三名義作為定陶對西門慶行動之背書。"
    - "不抹除該消息曾被白御行故意投放之歷史。"
```

---

# 6｜西門慶、蘇清與定陶自身行動

## XIM20-E01｜西門慶之名由蘇清親口提出

```yaml
NAME_DISCLOSURE:
  event_id: "XIM20-E01-SUQING_NAMES_XIMENQING"
  trigger:
    - "白御行表示京師商業環境需要清理，有一個名字不能由自己先說。"
  speaker: "蘇清"
  name: "西門慶"
  su_qing_boundary:
    - "她明示名字由她自己說，不是替白御行傳話。"
    - "她承認對西門慶有私怨。"
    - "她不因此單方面決定沈家或定陶必須如何處置。"
  status:
    - "西門慶成為定陶明示之重要敵對／清理目標。"
    - "並未因一句話完成犯罪定罪或死亡裁決。"
```

## XIM20-E02｜定陶與沈家各自行動

```yaml
STRATEGIC_SEPARATION:
  bai_yuxing_position:
    - "廣源與西門慶有不清楚的關係；白御行稱光此點對定陶而言已是『死罪』。"
    - "此為白御行對敵對關係與處置門檻的宣告，不是官府刑事判決。"
  shen_position:
    - "沈家如何行動由沈萬三自己決定。"
    - "沈家只承諾不為不該保的人與定陶敵對。"
  official_case:
    - "偽牌、高爐、巡檢司與可能軍中印模案件交開封府繼續。"
```

## SUQ20-E01｜五百兩三夜舊契結清

```yaml
OLD_CONTRACT:
  parties:
    - "白御行"
    - "蘇清"
  original_terms: "五百兩／三夜"
  prior_status: "剩一夜未履行之舊帳"
  settlement:
    - "白御行明示昨夜不是蘇清不來，而是張麗華清場。"
    - "白御行承認該次未履行原因在自己一方。"
    - "因此三夜五百兩舊帳正式清帳，不要求補夜。"
    - "蘇清接受此結算為公平。"
  current_ledger: "CLOSED_NO_ADDITIONAL_NIGHT_DUE"
```

## SUQ20-E02｜二十八日私約與可能第二十九日

```yaml
PRIVATE_PACT:
  base_pact:
    status: "ACTIVE_CONDITIONAL_PRIVATE_PACT"
    trigger: "西門慶真正倒下"
    duration: "二十八日"
    current_start: "NOT_STARTED"
    su_qing_recognition:
      - "蘇清表示既已親口押了，條件成立後會認。"
  fall_criterion_by_suqing:
    - "不是短期名聲受損、鋪子被查或避風幾日。"
    - "西門慶須失去原本能回去的位置。"
    - "錢、勢、人、門路至少有一項再也接不回來。"
  additional_day:
    status: "CONDITIONAL_VOLUNTARY_REWARD_NOT_DEBT"
    condition: "若槐月二十日晚這場局實際成為拔掉西門慶關鍵線之因果"
    result: "蘇清願將二十八日增加為二十九日"
    legal_language:
      - "第二十九日不是她現在欠白御行的債。"
      - "只有條件成就後由蘇清自願增加。"
  tonight_fee:
    - "蘇清今晚以事件當事人／主角身分上桌，不收陪席出席費。"
```

---

# 7｜白玉池秘密擴大知情

```yaml
WHITE_JADE_POOL_DISCLOSURE:
  event_id: "POOL20-E01-SHEN_DISCLOSURE"
  speaker: "白御行"
  disclosed_to:
    - "沈萬三"
    - "沈萬三帶來的京師總代理"
    - "江南船務總管"
    - "爐料老牙人"
    - "前廣源帳房"
    - "席上已知情或在場之定陶／觀止高層"
  player_description:
    - "觀止有一座仍在開發的秘密池。"
    - "池中有池靈，白御行以『澡盆成靈』作玩笑說法。"
  su_qing_correction:
    - "池中存在一名自稱阿泠的女子。"
    - "阿泠能控制池水，認為白玉池是她自己的地方。"
    - "池底曾有未知回顯，池仍封閉調查。"
    - "不能把阿泠簡化為白御行所有的澡盆或商品。"
  shen_response:
    - "沈萬三要求己方在場人保密。"
    - "未要求當晚入池。"
    - "若未來開發，可提供浴舍、引排水、保密隔間、客人篩選與江南園林工匠。"
    - "承認阿泠是否見客、是否水療應由她自己決定。"
  current_status:
    pool: "SEALED_OR_RESTRICTED; NO_NEW_REOPENING_RESULT_OBSERVED"
    second_preopening_check_due_from_v2_2: "RESULT_NOT_RECORDED"
    investment: "NO_AGREEMENT"
    service_sale: "NONE"
  confidentiality:
    - "秘密知情範圍已因白御行主動披露而擴大。"
    - "不得倒寫為只有原五人知道。"
```

---

# 8｜觀止夜宴、姑娘自主與新品試用

## GZ20-E01｜宴席服務與姑娘安排

```yaml
ENTERTAINMENT_FRAME:
  confirmed:
    - "紅袖與浮香自願上席奏曲。"
    - "醉花負責調酒、蜂蜜茶與低酒。"
    - "紅娘氏與小翠席間添菜、陪話與觀察。"
    - "蘇清坐在白御行身旁。"
    - "宋蕙蓮、李桂姐、白三娘與若干成年未掛牌姑娘後續自願上席陪聊。"
    - "辭歲得知若出場可能壓過新人後，自行決定不出場，並要求不要拿她名字替席面增價。"
  boundaries:
    - "未掛牌姑娘只陪話，不因上席自動提供性服務。"
    - "每名姑娘是否接後續洗浴、陪夜、同床或性交，由本人逐項同意與議價。"
```

## GZ20-E02｜紅綠組公開亮相與沈萬三捧場

```yaml
RED_GREEN_TEAM:
  members:
    - "紅娘氏"
    - "小翠"
  public_pitch_by_bai:
    - "白御行以『紅綠配，真美麗』介紹兩人組隊。"
    - "提到小翠剛從女孩成為女人、經驗少，請沈萬三多捧兩人場。"
  corrections_and_boundaries:
    - "紅娘氏明示兩人不是綁成一包、付錢即可一併帶走。"
    - "小翠明示自己不知道的可慢慢學，不願意的不能因她剛成女人而被哄騙。"
    - "潘金蓮規定小翠目前只接席間照應、茶菜與普通陪話；正式陪席需她本人同意。"
  transaction:
    - "沈萬三給兩人當晚賞錢，由潘金蓮按席間賞錢處理，不附帶後續身體約定。"
    - "紅娘氏與沈萬三口頭談成：若未來明朝線第一件可售陶瓷金屬器物由她找到第一位京師買家，成交抽一分半；只限該第一位買家。"
  status_of_future_commission: "ORAL_CONDITIONAL_COMMISSION; PRODUCT_NOT_YET_EXISTS"
```

## GZ20-E03｜定陶新款肚兜試用品

```yaml
PRODUCT_SAMPLE_EVENT:
  source: "常煒攜帶之定陶新款肚兜樣品"
  confirmed:
    - "款式與此前送李師師、張麗華及紅綠組之系列同源。"
    - "白御行先讓紅袖、浮香挑選。"
    - "其後由常煒代表定陶，向在場自願接受的成年姑娘一人送一件樣品。"
    - "潘金蓮選擇深紅近黑款，並提出加襯、加寬肩帶、改善線頭與腰後繫法等產品意見。"
    - "白三娘提出寬肩、產後與長時穿著需求。"
    - "醉花提出沾酒後氣味與清洗測試。"
    - "蘇清拿走一件新品作為樣品，不構成對白御行之穿著承諾。"
  status:
    - "樣品贈送已發生。"
    - "正式售價、量產規格、尺寸表與三日回訪尚未完成。"
```

## GZ20-E04｜沈萬三留宿與定陶人員安置

```yaml
OVERNIGHT_ARRANGEMENTS:
  shen_wansan:
    - "沈萬三接受留在觀止至天亮，以觀察觀止夜間服務與早餐整改。"
    - "潘金蓮提供安靜客房。"
    - "沈萬三當晚沒有點任何姑娘陪房。"
    - "只留一名貼身隨從。"
  shen_staff:
    - "沈家京師總代理、船務總管與爐料牙人先行離開處理事務。"
    - "前廣源帳房因牽涉案情，被安排在另室安全留宿／看守，避免夜間失蹤。"
  dingtao_staff:
    - "潘金蓮請願意接洗浴、按摩、陪睡或另行談性服務之成年紅官人自行報名。"
    - "常煒拒絕陪宿，稱翌日仍須對帳。"
    - "部分未具名定陶師爺、掌櫃或帳房與自願姑娘談妥不同範圍服務。"
    - "只確認安排與議價，未觀察每一房之實際完成內容。"
  accounting:
    - "房錢、洗浴、陪夜與其他服務分項記帳。"
    - "誰享受誰先付；若定陶要作員工犒賞，事後持票據報帳。"
```

## GZ20-E05｜早餐整改試餐

```yaml
BREAKFAST_TRIAL:
  status: "ORDERED_FOR_HUAI21_DAWN_NOT_YET_COMPLETED"
  trigger:
    - "白御行公開嫌觀止早餐不佳，但表示不願以定陶資本開早餐鋪搶小販生計。"
  agreed_direction:
    - "不開定陶自營平價早餐鋪。"
    - "可向附近小販與店家採購，保留原店名字與拒絕供貨權。"
    - "觀止只賣環境、服務、選品與高價附加層。"
  pan_order:
    - "槐月二十一日卯初試餐。"
    - "粥、餅、湯、蛋分取附近三家比較。"
    - "不得用隔夜剩料敷衍。"
  payer:
    - "潘金蓮曾提出首輪試吃費由定陶承擔。"
    - "白御行未在本輪另作明示確認，正式付款法位待結帳。"
```

---

# 9｜李師師怒砸負心漢事件

## RIR20-E01｜原始怨氣來源校正

```yaml
CAUSE_LOCK:
  true_previous_cause:
    - "槐月十八日下午，白御行與李師師性交並體內射精後，很快穿衣離房赴張麗華晚膳。"
    - "李師師因其事後幾乎不停留、像房內再無一人而擲枕追罵。"
  excluded_false_cause:
    - "不是因白御行比較紅娘氏床上勝過李師師。"
  current_emotional_state:
    - "李師師對前日提褲離開仍有真實不滿。"
    - "她沒有因此宣布如夫人框架撤回或永久斷絕。"
```

## RIR20-E02｜雙方同意放大為公開故事

```yaml
STAGED_EVENT:
  event_id: "RIR20-E02-ANGER_PERFORMANCE_AGREEMENT"
  initiation_by_bai:
    - "白御行主動表示願再當靶子。"
    - "提議讓李師師朝牆砸杯壺，高聲罵『殺千刀』『死沒良心』『提起褲子不認人』，使全觀止聽見。"
    - "提議把事件轉成翌日設席的招客故事。"
  li_shishi_acceptance:
    - "李師師接受演出方向。"
    - "同意以自己被負心漢丟下的形象設席。"
    - "要求席面由她定，白御行翌日最後必須到場。"
  physical_staging:
    - "李師師先以多只枕頭與薄被砸白御行。"
    - "其後砸碎杯子、茶壺，並高聲罵出約定台詞。"
    - "為使白御行狼狽出場，她扯鬆衣襟、拉歪腰帶並在袖口外層劃破，不傷皮肉。"
  cost:
    - "破損杯、壺、香粉與牆面清理已被潘金蓮記到白御行帳上。"
```

## RIR20-E03｜薄情郎受審席

```yaml
SEAT_PLAN:
  title: "薄情郎受審席"
  host: "李師師"
  planned_date: "槐月二十一日"
  status: "PUBLICLY_ANNOUNCED_IN_GUANZHI; DETAILS_PENDING"
  concept:
    - "先讓客人聽李師師怒砸負心漢之故事。"
    - "白御行主位或受審位置留到最後。"
    - "若白御行不到，李師師曾說可在主位掛一條空腰帶作嘲諷。"
  pending:
    - "開席時辰。"
    - "座錢與提問加價。"
    - "白御行是否依約到場。"
    - "哪些細節屬演出可公開，哪些私密內容禁止出售。"
```

## RIR20-E04｜「每月一次」加碼與真實反應

```yaml
PUBLIC_ESCALATION:
  player_action:
    - "白御行狼狽跑到大堂後，公開說『沒事，女人情緒不穩定，每個月一次』。"
  li_shishi_response:
    - "李師師在樓上以空香粉盒擲下。"
    - "高聲反駁自己是否每月一次不知道，但白御行提起褲子就跑是一天一次。"
    - "再次公開叫白御行滾，並確認翌日設席。"
  status:
    - "白御行該句不是兩人原先完整約定台詞。"
    - "李師師之反擊同時具有即興演出與對被污衊之真實不滿。"
    - "不得把李師師情緒原因記為月事。"
    - "不得把當場叫滾改寫成永久分手。"
```

## RIR20-E05｜今晚不回之範圍

```yaml
NIGHT_BOUNDARY:
  confirmed:
    - "白御行與李師師同意，為了完成故事，白御行今晚不回李師師房。"
    - "李師師要求翌日回到受審席收場。"
  does_not_mean:
    - "白御行必須離開整座觀止。"
    - "白御行不可去李瓶兒或張麗華處。"
    - "如夫人關係框架已撤銷。"
    - "李師師已同意翌日任何性行為。"
```

---

# 10｜目前人物與關係硬狀態

```yaml
RELATION_CURRENT:
  BAI_YUXING__SHEN_WANSAN:
    state: "FROM_MUTUAL_PROBING_TO_ORAL_NON_AGGRESSION_AND_TECH_COOPERATION_PRINCIPLE"
    formal_alliance: false
    signed_contract: false
    tech_delivered: false
    direct_communication_rule: true

  BAI_YUXING__LI_SHISHI:
    state: "RU_FUREN_FRAMEWORK_ORALLY_ACCEPTED; PRIVATE_SEXUAL_RELATION_ACTIVE; CURRENT_NIGHT_PUBLIC_ANGER_STORY_ACTIVE"
    tonight_entry: "NOT_ALLOWED_BY_MUTUAL_STORY_AGREEMENT"
    next_due: "槐月二十一日薄情郎受審席"
    exclusivity_on_her_side_during_relationship: "她先前口頭同意不與其他男人上床"
    public_implementation_of_ru_furen: "NOT_COMPLETED"
    pregnancy: "UNKNOWN"

  BAI_YUXING__ZHANG_LIHUA:
    state: "ACTIVE_LOVER_RELATION"
    current_offer: "若白御行回房，備水並可留宿；不追問今晚去向"
    ongoing_sexual_consent: "NONE_CARRIED_OVER"
    waiting_limit: "燈已挑暗；不整夜無限等候"

  BAI_YUXING__LI_PINGER:
    state: "PURSUIT_OPEN; NO_FORMAL_RELATION; TONIGHT_PRIVATE_ENTRY_NOT_YET_GRANTED"
    current_offer: "醒酒湯或查看是否受傷"
    sexual_consent: "NONE_ESTABLISHED"

  BAI_YUXING__SU_QING:
    old_500_tael_contract: "CLOSED"
    twenty_eight_day_pact: "ACTIVE_CONDITIONAL_NOT_STARTED"
    twenty_ninth_day: "CONDITIONAL_VOLUNTARY_REWARD"
    tonight_fee: "NONE"

  BAI_YUXING__PAN_JINLIAN:
    state: "ACTIVE_OPERATIONAL_RELATION"
    current_actions:
      - "沈萬三留宿安排"
      - "定陶人員房間與服務記帳"
      - "槐月二十一日早餐試餐"
      - "薄情郎受審席預售與損耗記帳待續"

  WHITE_JADE_POOL__SHEN_GROUP:
    knowledge: "SECRET_DISCLOSED_WITH_ORAL_CONFIDENTIALITY"
    operation: "NO_ACCESS_NO_INVESTMENT"
```

---

# 11｜帳目、物品與契約狀態

```yaml
LEDGER_CURRENT:
  su_qing_old_contract:
    amount: "五百兩"
    nights: 3
    state: "CLOSED_BY_BAI_ACCEPTING_OWN_SIDE_CAUSE_FOR_LAST_NIGHT_NONPERFORMANCE"

  shen_hongniang_first_buyer_commission:
    rate: "一分半"
    scope: "明朝線第一件可售陶瓷金屬器物之第一位京師買家，且須由紅娘氏親自找到"
    state: "CONDITIONAL_ORAL_NOT_YET_TRIGGERED"

  dudou_samples:
    state: "DISTRIBUTED_TO_MULTIPLE_NAMED_AND_UNNAMED_ADULT_WOMEN"
    payment: "GIFT_SAMPLES"
    followup: "穿著、磨損、清洗、尺寸與掉色回報待收"

  riri_room_damage:
    items:
      - "杯盞"
      - "茶壺"
      - "香粉盒"
      - "牆面清理"
    charged_to: "白御行"
    exact_amount: "NOT_YET_CALCULATED"

  guanzhi_overnight_services:
    state: "ROOMS_AND_SERVICE_SCOPES_NEGOTIATED"
    exact_total: "NOT_YET_CLOSED"

  breakfast_trial:
    state: "ORDERED_NOT_COMPLETED"
    payer: "DISPUTED_OR_PENDING_CONFIRMATION"
```

---

# 12｜知情、公開傳聞與秘密

```yaml
KNOWLEDGE_AND_RUMOR:
  official_counterfeit_case:
    known_to:
      - "開封府辦案人員"
      - "定陶商會高層"
      - "沈萬三及其核心隨行"
    public: "瓦市群眾知道假試烤與有人被捕；不知道完整官牌印模與兩車去向"

  shen_dingtao_understanding:
    witnesses:
      - "雙方宴席高層"
      - "蘇清與部分觀止在席人員"
    public: "NOT_PUBLIC_ALLIANCE"

  white_jade_pool_secret:
    previous_core_group: "V2.2以前知情人"
    new_expansion:
      - "沈萬三及其四名核心隨行"
      - "定陶在席高層中原不知情者"
    public: "NOT_PUBLIC"

  riri_anger_story:
    public_inside_guanzhi:
      - "李師師怒砸白御行"
      - "白御行提褲就走"
      - "翌日設薄情郎受審席"
    mixed_truth:
      - "前日突兀離房是真實。"
      - "本夜砸杯罵人有雙方同意的宣傳演出。"
      - "白御行月事情緒說法非事實。"
```

---

# 13｜未決事項

```yaml
OPEN_THREADS:
  immediate_player_choice:
    - "白御行去李瓶兒房、張麗華房，或另作第三選擇。"
    - "不得因兩房有燈便預設任何一方同意留宿或性行為。"

  huai21_morning:
    - "沈萬三是否實際留到卯初與早餐試餐。"
    - "觀止早餐整改結果。"
    - "定陶人員夜間服務帳與實際完成範圍。"
    - "前廣源帳房之安全與開封府後續傳喚。"

  huai21_riri_seat:
    - "薄情郎受審席時辰、價格、座次與公開內容。"
    - "白御行是否依約到場。"
    - "李師師如何區分真怨、戲局與如夫人公開位置。"

  official_case:
    - "兩車成品實際內容。"
    - "西門府與巡檢司是否真的收貨。"
    - "許奉年、西門慶、巡檢司與偽牌坊之命令鏈。"
    - "『武』字銅牌來源。"
    - "蘇州／江南高嶺土是否與爐磚同源。"
    - "開封府是否擴大至軍中與官坊。"
    - "案件最終屬偽證、私鹽、偽造官牌、私鑄、軍器或謀逆之哪一層。"

  salt_business:
    - "九烤樣品與官冊是否抵京。"
    - "三烤京師最後庫存是否售罄。"
    - "六烤倍價策略之長期市場反應。"
    - "定陶產品是否正式標示『竹鹽』。"

  shen_cooperation:
    - "陶瓷金屬研發起點的具體內容、交付與對價。"
    - "是否正式立契。"
    - "交會點市場衝突處理規則。"

  su_qing:
    - "西門慶何時達到真正倒下條件。"
    - "二十八日私約何時開始。"
    - "第二十九日條件是否成立。"

  white_jade_pool:
    - "槐月十九日第二次復開前檢查結果未被記錄。"
    - "阿泠是否同意任何未來見客。"
    - "沈家知情是否造成外洩。"
```

---

# 14｜接關約束

```yaml
CONTINUATION_LOCK:
  player_choice:
    - "當前只保存白御行正在考慮去瓶兒或麗華處。"
    - "不得替他向任何一方走去、敲門、接受留宿或發生親密。"

  li_pinger_lock:
    - "披風、醒酒湯與查看傷勢不等於進房、同床或性同意。"
    - "她沒有因白御行狼狽便自動心軟或接受秘密情人位置。"

  zhang_lihua_lock:
    - "備水與昨夜枕頭仍在，不等於自動續夜性交。"
    - "她不問今晚去向，不等於沒有嫉妒、沒有界線或永久無條件接納。"
    - "燈已挑暗，若白御行不回，她可以熄燈並休息。"

  li_shishi_lock:
    - "今晚不回只限師師房。"
    - "翌日受審席已成公開承諾，但白御行是否履行仍由玩家決定。"
    - "不得把怒砸事件寫成純演出而抹除前日真怨。"
    - "不得把叫滾寫成永久分手。"
    - "不得把月事說法寫成客觀身體狀況。"

  shen_lock:
    - "停止試探不等於永久盟友。"
    - "技術合作未交付，不得在明朝線直接生成成熟陶瓷金屬產業。"
    - "沈家不替西門慶遮護，不等於已參與定陶打擊行動。"

  official_case_lock:
    - "商人已把偽牌、高爐與官署線交開封府。"
    - "不得讓白御行或沈萬三私自完成官府搜捕、刑訊或謀逆定罪。"
    - "不得因『武』牌、高爐或軍中印模直接宣布造反成立。"

  white_jade_pool_lock:
    - "白玉池仍封閉／限制中。"
    - "沈萬三未入池、未購買服務、未投資。"
    - "阿泠不是商品或澡盆，服務資格由她自己決定。"
```

---

# 15｜有效接關摘要

槐月十九日，定陶商會兩車遭城南巡檢扣押，車底藏有河東池鹽，並出現三年前停用之玄字九號真舊封、偽造副會長腰牌線索與「死人也會說話」書信。前案證物箱被從背面開啟，死去帳房私簿少六頁。白御行將案件交開封府；開封府同時查巡檢司與定陶商會，並要求把白御行投放之假線與實證分冊。

被扣鹽不是定陶所用齊地海鹽，也不是定陶三烤成品。白御行公開說明定陶不是原鹽鹽商，而是以合法官鹽、貨號、均輸平準司查驗與逐窯帳冊加工高價產品。對手在相國寺瓦市宣稱普通市鹽炒三次即可成三烤，白御行將之稱為「三炒鹽」，並把京師三烤最後庫存帶到現場，宣布售完後只賣倍價六烤。三烤當場形成購買潮。對手所帶假定陶舊匠因說出風門、爐氣術語而露出真窯工底子，當眾為鐵鍋炒鹽背書後試圖逃跑，被開封府拘捕，身上掉出「武」字牌。

現場找到帶鐵渣的耐火爐磚。白御行提出蘇州高嶺土／江南爐料追查方向，但產地未證實。沈萬三其後主動赴觀止，帶來江南船單、爐料牙人與前廣源帳房。三批廣源爐料以「佛像底座」假名目轉運，其中一批指向城北廢鑄錢坊。開封府在該處找到三座高溫爐、多種官坊、巡檢司、商會與軍中印模及未完成腰牌，沒有搜到成批兵器；現場推定至少兩車成品已先行移走。前廣源帳房口供稱一車進西門府、一車進巡檢司，此為待查口供，尚非最終定罪。

沈萬三在宴席上承認眼紅定陶鋼鐵與制度工業。白御行展示定陶真正核心「陶瓷金屬」與氧化鋁合金刀頭，提出只分享研發起點與失敗坑，不交完整工法；沈萬三在明朝線用明朝自己的人、料、銀自行研發，不挖匠、不偷圖，產品若進觀止京師交會點須先通知定陶。雙方口頭接受原則，但尚未簽約或交付技術。

定陶與沈家同時達成停止代理試探：不再借廣源、西門慶或其他本地勢力試水；第三方若冒用一家名義碰另一家，先直接求證。沈家不替廣源遮帳，也不替西門慶借船、借錢、藏貨或轉帳。雙方不是盟軍，也不共治京師。白御行先前投放的「沈萬三要殺西門慶」被當面定為錯誤風言，雙方日後不再沿用。

西門慶之名由蘇清本人在席上說出。蘇清承認私怨，但不替其他人決定行動。白御行與蘇清同時結清舊五百兩三夜契約：昨夜未履行是張麗華清場、責任在白御行一方，不補夜。蘇清對「西門慶真正倒下後二十八日」之私約仍認帳，但尚未開始；若槐月二十日晚此局實際成為拔掉西門慶關鍵線之原因，她自願再加第二十九日，該日不是當前欠債。

白御行在宴席上向沈萬三及其核心隨行披露白玉池與阿泠秘密。蘇清當場校正：阿泠是自稱池主、能控水的女子，池底異常仍未完全解明，池目前封閉調查。沈萬三未要求入池，也未投資，只口頭保密並表示未來可提供浴舍與工程資源；阿泠是否見客仍由她自己決定。

觀止夜宴後轉為風月席。紅袖、浮香、醉花、紅娘氏、小翠、宋蕙蓮、李桂姐、白三娘及自願上席的成年新人各自依範圍陪曲、陪話與照料；辭歲自行拒絕出場。紅娘氏與小翠以紅綠組亮相，但不形成綁售或性義務。定陶新款肚兜作為樣品分贈在場成年姑娘，潘金蓮、白三娘、醉花等提出產品修改意見。沈萬三同意留宿至天亮看觀止早餐整改，沒有點姑娘陪房；部分定陶人員另與自願紅官人談妥有限服務，實際完成仍未逐房確認。

白御行其後去見李師師。兩人確認前日真正怨氣源於白御行性交射精後迅速提褲離房。白御行提議把此事放大成全觀止可聽見的「怒砸負心漢」故事；李師師同意，砸杯、茶壺、高聲辱罵，並把翌日席面定為「薄情郎受審席」，要求白御行最後到場。白御行狼狽到大堂後又稱女人每月一次情緒不穩，李師師以香粉盒與公開反罵即興加碼。該事件既有真怨，也有雙方同意的宣傳演出；月事說法不是客觀事實。白御行今晚不回師師房，但可在觀止其他地方投宿。

**當前時間：理火三年槐月二十日深夜。**

**當前位置：觀止內院東西廊交界。**

**東側：李瓶兒尚醒，可送醒酒湯或查看是否受傷，但未邀請必然進房。**

**西側：張麗華不問今夜去向，若白御行回去便備水；若不回，她將熄燈。**

**白御行尚未選擇。**

---

## VERSION_STATUS

```yaml
ACTIVE_HOT_SAVE: "V2.3"
PREVIOUS_VALID_HOT: "V2.2"
MASTER_CONSOLIDATION_CREATED_IN_SAME_SAVE_OPERATION:
  file: "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"
  master_cutoff: "HOT V1.9"
CURRENT_RESUME_POINT: "槐月二十日深夜，觀止內院東西廊交界，白御行在李瓶兒與張麗華兩邊訊息之間尚未決定"
```

<!-- SOURCE_HOT_V2_3_END -->

---

## SOURCE ARCHIVE｜HOT V2.4

**檔名：** `觀止青樓_白御行線_HOT_SAVE_V2.4_槐月二十日深夜_風滿樓公案與五千後算開冊版.md`  
**SHA-256：** `ad757d9a4b2e612b0c606d44dbf55c857d40e8d7e792db18839a3faa50d088f5`

<!-- SOURCE_HOT_V2_4_BEGIN -->
# 觀止青樓｜白御行線 HOT SAVE V2.4
## 理火三年槐月二十日深夜｜風滿樓公案 × 西門暗櫃 × 五千後算開冊 × 蘇清代理案版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V2_4_HUAI20_LATE_NIGHT_FENGMANLOU_WUQIAN_HOUSUAN"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V2.4"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime:
    - "GUANZHI_QINGLOU_V10_0"
    - "GUANZHI_QINGLOU_V10_1_V10_2_PATCH_WHEN_APPLICABLE"
  story_date: "理火三年槐月二十日深夜"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AT_FENGMANLOU_AFTER_WUQIAN_HOUSUAN_OPENING"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V2.3_槐月二十日深夜_沈萬三合作與師師薄情郎席前接關版.md"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"
  current_location: "觀止青樓／風滿樓"
  direct_resume_owner: "WORLD_OR_PLAYER_AFTER_HOLD_RELEASE"
  save_scope:
    - "HOT V2.3 後之李師師公開薄情郎事件收束與李瓶兒夜談"
    - "定陶／沈萬三早餐與後續商務"
    - "劉成安、阿麗婭、蘇清、杜小七、何進安等證人與法律援助桌"
    - "柳生失蹤案、高衙內／太尉府／廣源／西門慶之法律攻防"
    - "西門慶入開封府、暗櫃移交與多組新證物線索"
    - "風滿樓大型公域展開與公開公案轉述規則"
    - "太尉府私函由潘金蓮秘密交包拯查驗"
    - "蘇清正式委託許慎言調查賣身契與後堂結算"
    - "《五千後算》開冊、潘金蓮供述與蘇清新訴訟方向"
```

---

# 0｜提交法位、來源與反污染說明

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V2.3_槐月二十日深夜_沈萬三合作與師師薄情郎席前接關版.md"
    role: "本檔直接前置 HOT；V2.3 以前事件全部繼承"
  long_term_master:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"
    role: "長期因果與早期玩家線來源"
  route_conversation_commit:
    role: "HOT V2.3 之後至本次 HOLD 的直接劇情來源"
  persona_source:
    file: "觀止人物卡_LCAPG_V1.1-R1_原始重構去污染版_含辭歲_導演隱藏區增補.md"
    role: "人物基線來源；本檔不得倒灌改寫"
  character_pool:
    file: "觀止人物池_LCAPG_V1.1_紅娘氏與李師師雙人正式版.md"
    role: "紅娘氏、李師師平級人物來源"
  forbidden_source:
    file: "HOT_SAVE_V1.3"
    status: "ILLEGAL_CORRUPTED_SAVE"
    use: "AUDIT_ONLY"

COMMIT_NOTE:
  - "本檔取代 HOT V2.3，成為白御行線當前直接接關切片。"
  - "本次只做 HOT SAVE；不更新 MASTER，不改人物卡，不改人物池。"
  - "本檔只保存已發生、可觀察、人物明示、正式文書可見或玩家對自身言行之有效輸入。"
  - "供述、推論、帳冊文字、官方認定、民間傳聞與客觀真相分軸保存。"
  - "潘金蓮或西門慶的自述不因自我不利即自動升格為完整客觀真相。"
  - "同一日期、同一牌號、同一金流只建立線索或交叉查核資格，不自動建立犯罪因果。"
  - "蘇清原始口頭賭約之完整條款到目前仍缺乏硬證據；不得補成正式書面賭契。"
  - "蘇清正式賣身契為本人自願同意並畫押之正式文件，目前仍有效；不得因阿麗婭五千兩權利變化、口頭賭約爭議或潘金蓮後堂局曝光而自動失效。"
  - "阿麗婭若解除西門慶舊五千兩之限制，只代表舊限制可能失效；不等於她欠觀止新的掛牌、初夜、陪客或其他交付。"
```

---

# 1｜當前時間、位置與 HOLD 接關點

```yaml
CURRENT_SCENE:
  date: "理火三年槐月二十日"
  time: "深夜／風滿樓已開；精確時刻未定"
  location: "觀止青樓／風滿樓"
  mode: "HOLD"
  player:
    name: "白御行"
    location: "風滿樓主要觀案席"
    last_confirmed_behavior:
      - "持續旁觀並與沈萬三、蘇清等評論局勢。"
      - "未在本 HOLD 前作出新的不可逆決定。"

  confirmed_present_or_immediately_active_at_guanzhi:
    - "白御行"
    - "沈萬三"
    - "趙受益"
    - "十三娘"
    - "蘇清"
    - "李師師"
    - "常煒"
    - "許慎言"
    - "紅娘氏"
    - "快嘴陸等說書／轉述人員"
    - "青禾可能仍在法律援助席附近；具體是否仍在按摩服務中不重要"

  offsite_or_position_requires_care:
    潘金蓮:
      current: "開封府"
      certainty: "CONFIRMED_AT_LAST_EVENT"
      note:
        - "其已在開封府就《五千後算》、五千掛牌與後堂安排接受詢問／作出供述。"
        - "本 HOLD 時尚未確認她已返回觀止。"
    阿麗婭:
      current: "開封府保護／女吏可控範圍內"
      certainty: "LATEST_CONFIRMED_RANGE"
      note:
        - "此前自願前往確認五千兩舊權利之法律狀態。"
        - "未同意重新掛牌。"
    西門慶:
      current: "開封府羈押／訊問中"
      certainty: "CONFIRMED"
    包拯:
      current: "開封府主持案件"
      certainty: "CONFIRMED"

  direct_resume_point:
    - "《五千後算》已由開封府在見證下開冊，部分內容已被准予以官方抄報方式傳至風滿樓。"
    - "潘金蓮已就五千掛牌局與蘇清敗約後交付作出部分本人供述。"
    - "蘇清已要求許慎言把『完整後堂結算與自身帳項』加入代理案。"
    - "下一幕不得預設潘金蓮敗訴、蘇清贏得自由、阿麗婭重新掛牌、太尉府私函內容曝光或西門慶定罪。"
```

---

# 2｜風滿樓：大型公域、空間與公開轉述規則

## FML20-E01｜風滿樓正式開啟

```yaml
EVENT_RECORD:
  event_id: "FML20-E01-FENGMANLOU_OPEN"
  status: "ACTIVE_PUBLIC_EVENT"
  initiator: "潘金蓮"
  confirmed:
    - "潘金蓮親自同意開觀止大場，正式以『風滿樓』承載本案。"
    - "觀止清堂，八盞落地青銅燈柱立定。"
    - "潘金蓮進行空間宣告後，風滿樓公域拓撲展開，大堂縱深拉開，可容數千人直接進觀止內觀看。"
    - "先前曾出現『把整條街變成觀眾席』之導演敘述，已被 GM 校正撤回；正式場面以風滿樓／隱藏舞台展開為準。"
  public_scale:
    - "數千名觀眾可在觀止內部觀看。"
    - "觀眾多不等於取得私人信件、私密房事或未公開證物之知情權。"
```

## FML20-E02｜三金主與觀止控制權

```yaml
SPONSORSHIP:
  event_id: "FML20-E02-THREE_SPONSORS"
  confirmed_sponsors:
    - "白御行／定陶一份"
    - "沈萬三一份"
    - "趙受益一份"
  operating_party: "觀止／潘金蓮"
  confirmed_rules:
    - "三個金主出銀；觀止出場地、人手、姑娘、帳房、說書與運作。"
    - "出資不換取案情定調權。"
    - "不冠名、不因出資取得多說一句或買結果之權。"
```

## FML20-E03｜說書與法位校正

```yaml
PUBLIC_RELAY_RULES:
  confirmed:
    - "說書先生負責把複雜人物、證據鏈、官府進度說成一般觀眾能理解的局勢。"
    - "許慎言及其他識字訟師負責校正證據法位。"
    - "開封府正式公開一張，觀止才可依公開材料掛一張。"
    - "不得堵開封府、不得替包拯喊判、不得以群眾壓力替代審理。"
  principal_categories:
    - "已證實／實證"
    - "證人所述"
    - "一方主張／訴辯"
    - "尚待查證／未證"
    - "純屬傳聞"
  required_example_separations:
    - "西門慶說梁福怕廣源＝供述，不是客觀成立。"
    - "暗櫃存在陳氏女舊狀＝物件／文書存在；文書內容真偽與犯罪成立仍需查。"
    - "五百兩是不是撤狀銀＝未證明。"
    - "『林教頭家事』是否指林沖＝未證明。"
    - "高俅是否知情＝未證明。"
```

## FML20-E04｜李師師對聯保留為中場閒話

```yaml
STAGED_PUBLIC_CONTENT:
  event_id: "FML20-E04-RIRI_COUPLET_INTERMISSION"
  status: "PUBLIC_INTERMISSION_ONLY"
  couplet:
    upper_or_line_1: "拔屌無情白御行"
    line_2: "一怒紅顏李師師"
    annotation: "自作自受"
  confirmed:
    - "白御行先詢問可否晚掛一天，李師師同意延期不減天數。"
    - "其後白御行改口不撤，授權紅娘氏在案情空檔用公開版說故事。"
    - "李師師同意只說大堂已公開內容，不准亂編房內性細節、不准假造刀具、投河、哭死等情節。"
    - "觀止另設『中場閒話／與本案無關』法位，防止與西門氏案證據混淆。"
    - "紅娘氏已公開講過『我愛你後立即離開』等已公開版本；該段屬中場笑談，不是公案證據。"
  private_boundary:
    - "李師師與白御行之私密房內細節仍非數千觀眾自由取用素材。"
```

---

# 3｜李師師：公開帳收束、私人帳未清

```yaml
LI_SHISHI_CURRENT:
  public_reckoning:
    status: "PUBLIC_ACCOUNT_CLOSED_FOR_NOW"
    confirmed:
      - "李師師糾正白御行：雙方自願性交不等於『佔有』。"
      - "白御行在親密後說『我愛你』並立刻離房，是其真正怒點之一。"
      - "白御行公開承認自己行為有『拔屌無情』性質；李師師拒絕把責任泛化為『所有男人都這樣』。"
      - "先前『薄情郎受審席』後因白御行轉去李瓶兒房而被李師師撤掉；她曾砸牌、關門並發怒。"
      - "公開事件已經收束，不再把李師師寫成要殺白御行或拿真刀行凶。"
  private_relation:
    status: "UNRESOLVED_NOT_BROKEN"
    confirmed:
      - "李師師沒有宣布永久斷絕。"
      - "未明示原諒。"
      - "未取消此前口頭如夫人框架，但也未新增公開落實。"
  anti_regression:
    - "不得把其怒氣全洗成純演出。"
    - "不得把其怒氣寫成不可修復永久決裂。"
    - "不得把職業表演、私人偏愛、性慾、如夫人承諾混為一軸。"
```

---

# 4｜李瓶兒：夜談、未性交與未來位置

```yaml
LI_PINGER_POST_V2_3:
  event_status: "PRIVATE_NIGHT_COMPLETED; MORNING_DEPARTURE_COMPLETED"
  confirmed:
    - "白御行在廊道最終選擇前往李瓶兒一側，而非張麗華房。"
    - "張麗華當夜沒有被白御行選擇；其燈後續熄滅。具體內心不得補寫。"
    - "李瓶兒替白御行準備足水、脫外衣鞋襪等照料。"
    - "白御行與李瓶兒談孩子與未來位置。"
    - "白御行明示確實想要李瓶兒，也想要她的孩子／與她有孩子；具體未來形式仍非完整方案。"
    - "白御行說張麗華選情人、李師師未來如夫人；李瓶兒表達自己要的是『家裡的人』／更接近未來妻位的方向。"
    - "白御行明示不以『妻』稱她，原因包括亡故正妻不可取代及現有法律／身分問題。"
    - "白御行把『如夫人』解釋為目前可給的最高位置：各自管理、平等、不以三書六聘成立。"
    - "李瓶兒目前法律上仍是西門慶之妾；在真正合法切斷前，不接受以新懷孕把局面壓過去。"
    - "她表達：若法律上真正脫離西門慶，且白御行公開承認平等如夫人、分開住處／財務、不把她綁在生孩子上，她願意往該位置走。"
    - "她強調自己仍是李瓶兒，不接受被『孩子』或『位置』吞掉。"
    - "當夜只有擁抱、談話、有限親近；沒有性交、沒有受孕事件。"
    - "翌晨白御行有輕吻後離開。"
  relation_status:
    direction: "FAMILY_OR_FUTURE_CONSORT_DIRECTION_WITH_LEGAL_PRECONDITION"
    not_established:
      - "正式如夫人落實"
      - "婚姻"
      - "合法解除西門妾身分"
      - "生育同意"
      - "排他關係"
```

---

# 5｜早餐、沈萬三與定陶商務

```yaml
MORNING_BUSINESS:
  confirmed:
    - "沈萬三留宿觀止後參與早餐與商務閒談。"
    - "白御行要求『好早餐雙倍付』不得用模糊標準，後續改為可核對的試餐／評價方式。"
    - "談及跨時代馬鈴薯、辣椒／胡椒等食材；導演已校正早明胡椒與後世新大陸辣椒之年代差異。"
    - "西門慶真正倒台後，可考慮讓蘇清把馬鈴薯菜式整理成食譜，供沈萬三之牡丹樓等後世線使用；尚未交付。"
    - "白御行與常煒曾短暫返回定陶商會，後又回觀止看法律大局。"
  shen_wansan_relation:
    - "與定陶仍是停止代理試探、可談陶瓷金屬研發合作之商務關係。"
    - "不是全面同盟。"
```

---

# 6｜劉成安與觀止免費法律援助桌

## LAW20-E01｜劉成安公開存在與證言

```yaml
LIU_CHENGAN:
  identity: "前廣源帳房／缺兩指"
  status: "PROTECTED_PUBLIC_WITNESS"
  confirmed:
    - "白御行主張把劉成安公開移至觀止，使其存在被全京師看見，提高暗殺成本。"
    - "常煒以定陶標誌車輛、繁華路線、公開叫名等方式放大可見性。"
    - "在公開前，口供副本已分存定陶、開封府與觀止。"
    - "劉成安供稱廣源有兩套帳；其曾因詢問無標記車與重複帳目而失去兩指。"
  storyteller_rule:
    - "三名說書人可聽與轉述已確認部分，但不得添油加醋。"
```

## LAW20-E02｜免費代書接狀

```yaml
LEGAL_AID_TABLE:
  status: "ACTIVE_AT_GUANZHI"
  principal_lawyer: "許慎言"
  sign:
    - "西門氏相關訟事"
    - "受欺無資者免費代書接狀"
    - "實事實寫，傳聞另記"
  funding: "定陶商會出資；觀止借場地"
  no_promise:
    - "不承諾勝訴"
    - "不把傳聞包裝成證據"
  evidence_sorting:
    white: "本人直接經歷／第一手"
    yellow: "文件／物證"
    blue: "證人／來源"
    gray: "傳聞"
  notable_item:
    - "一名跛腳鹽夫帶來木牌，其火印與此前偽牌高爐案出現同類印記，形成初步可查連接；尚非完整犯罪閉環。"
```

---

# 7｜柳生、阿麗婭、蘇清：證言與責任分離

## LIUSHENG20-E01｜固定歷史與目前證據法位

```yaml
LIUSHENG_CASE:
  fixed_observed_history:
    - "柳生曾帶十兩試圖與阿麗婭私奔。"
    - "高衙內在觀止公開下令『拖出去，打斷腿扔河裡』。"
    - "其手下對柳生施暴並拖走／轉移。"
    - "西門慶當時在場；後續以五千兩取得阿麗婭之預定名義。"
  crucial_unknown:
    - "柳生是否實際死亡。"
    - "是否被真正扔入河中。"
    - "西門慶是否事前指使、鼓勵或共同謀劃暴力。"
  prohibition:
    - "不得把『失蹤＋傳聞淹死』寫成已確認死亡。"
    - "不得把西門慶在場自動寫成其下令施暴。"
```

## LIUSHENG20-E02｜阿麗婭證言

```yaml
ALIYA_TESTIMONY:
  confirmed:
    - "她見到柳生。"
    - "她聽見高衙內下令打斷腿、扔河裡。"
    - "她看見人員毆打／拖走柳生。"
    - "她見西門慶在場且未阻止。"
    - "其後掛牌照常進行，西門慶出五千。"
    - "她保留柳生血染木簪，已作證物封存。"
  not_testified:
    - "她沒有聽見西門慶命令暴力。"
  current_rights_issue:
    - "她已自願去開封府確認當年五千兩究竟買到什麼權利及其是否仍有效。"
    - "她沒有因此同意再次掛牌。"
```

## LIUSHENG20-E03｜蘇清證言

```yaml
SUQING_LIUSHENG_TESTIMONY:
  confirmed:
    - "蘇清知道柳生與阿麗婭曾策劃離開。"
    - "她見過柳生紙條並在掛牌前夜於側門攔過阿麗婭。"
    - "她亦見到高衙內下令與其後暴力。"
    - "她沒有證稱自己聽到西門慶下令打柳生。"
  private_confession_line:
    - "蘇清在西門府期間曾由西門慶本人私下告訴她若干事情。"
    - "該內容目前只知西門慶與蘇清掌握；蘇清拒絕先在觀止公開。"
    - "她要求先私下對包拯逐字陳述，再讓西門慶／其律師知悉。"
    - "具體內容仍為 UNKNOWN；不得生成補全。"
```

---

# 8｜開封府與太尉府：西門慶入府與程序攻防

```yaml
KAIFENG_VS_TAIWEI:
  confirmed_chain:
    - "開封府先以柳生失蹤案分別傳喚潘金蓮、阿麗婭、龐春梅與西門慶。"
    - "西門慶當時未到，轉赴太尉府。"
    - "太尉府曾希望在府內詢問並限制只查柳生、不延伸高／廣源／太尉府。"
    - "包拯拒絕把太尉府當法庭；可給安全押送，但不得以府邸替代官署。"
    - "期限過後，開封府依法提升為提人／拘票。"
    - "高俅最終交出西門慶；最初未上鐐，太尉府保留異議。"
    - "此移交不等於高俅承認西門有罪。"
  taiwei_public_position:
    - "太尉府正式回文：外院公帳無杜成、梁福代收商戶護行銀之核准紀錄。"
    - "若二人私受商銀，屬個人行為；太尉府稱不知情、未授權、不予庇護。"
    - "該回文把梁福／杜成切出為可被查的個人節點，但不等於太尉府無任何責任已獲證明。"
  legal_counsel:
    - "章文度代表西門慶，主張在場不等於下令、沒有屍體不等於可直接以殺人論、第三人罪責需獨立互證。"
    - "韓季衡代表太尉府，重視程序、範圍與官府權限。"
```

---

# 9｜廣源二掌櫃、義莊、三千兩與梁福／杜成線

## EVID20-E01｜黑方戒指與母簿誘餌

```yaml
GUANGYUAN_SECOND_MANAGER:
  confirmed:
    - "街頭出現訊息：西門慶若留在開封府，『廣源真正總帳』不能留到天亮。"
    - "劉成安辨認黑方戒／三黃銅點為廣源二掌櫃憑證。"
    - "劉指出廣源內部更常稱『母簿』，不是『總帳』；因此該訊息被視為可能誘餌。"
    - "開封府暗捕已在人群中；二掌櫃試圖吞蠟丸後被拘。"
    - "蠟丸列三處：城南永安義莊、西門府外馬房、廣源南倉井房。"
    - "二掌櫃提出以母簿位置交換家人保護；是否完全可信未定。"
```

## EVID20-E02｜永安義莊與三千兩金流

```yaml
YONGAN_MORTUARY:
  confirmed:
    - "義莊屍房後室起火；一輛無棺黑車欲離開，被扣。"
    - "現場取得帳箱。"
    - "前二十七頁出現三千兩路線：廣源 → 西門府外帳 → 太尉府外院管事梁福。"
  not_proven:
    - "三千兩用途。"
    - "其與柳生暴力是否有直接因果。"
  temporal_note:
    - "日期與柳生被打同日，僅為時間重合，不能單獨證明用途。"
```

## EVID20-E03｜西門對三千兩之說法

```yaml
XIMEN_3000:
  confirmed_statement:
    - "西門慶承認該三千兩曾經過他。"
    - "他稱其為廣源支付梁福的『護行銀』，用途是保商路，不是殺人或封口。"
    - "他稱收據應存在西門外帳與梁福處。"
  status: "ADMISSION_OF_MONEY_PATH; PURPOSE_DISPUTED"
```

## EVID20-E04｜梁福、杜成與太尉府西院

```yaml
LIANGFU_DUCHENG:
  confirmed:
    - "開封府欲尋梁福時，梁福失蹤；家眷、衣物與主要財物仍留。"
    - "太尉府門簿曾有假出門記錄，守門人承認收五兩做假登錄。"
    - "銀角剪口與西門府常見裁銀習慣相似，只能提示習慣，不證明來源。"
    - "跑腿鏈追到太尉府外院小管事杜成。"
    - "太尉府先稱杜成午前已離府，後改口稱其曾短暫返回。"
    - "酒樓送過四人份飯菜入西門，店童聽見『梁先生一天沒吃東西了』；只聽到梁先生。"
    - "太尉府稱該梁先生為幕客梁士遠並允次日出面；真偽未定。"
  white_yuxing_inference:
    - "白御行認為梁福若要藏，太尉府可能是安全處，因開封府不能只靠猜測搜府。"
    - "此為玩家推論，不是世界事實。"
```

## EVID20-E05｜杜小七

```yaml
DU_XIAOQI:
  identity: "太尉府掃地小廝，約十六至十七歲"
  status: "PROTECTED_WITNESS"
  testimony:
    - "杜成命其清掃西院最內小院並換被褥。"
    - "午後有蒙面人由兩人扶入，走路偏一側。"
    - "晚間送飯，由杜成在門口接。"
    - "他聽見屋內人說：『西門慶都進開封府了，你們還想關我到什麼時候？』"
    - "他被杜成掌摑、威脅，後逃至觀止求保護。"
  cross_detail:
    - "劉成安說梁福右膝舊傷、陰雨時跛；杜小七所見蒙面人亦偏右腿。"
  status_note:
    - "相符但仍不足以證明蒙面人即梁福。"
```

## EVID20-E06｜丙七浮屍

```yaml
BINGQI_CORPSE:
  confirmed:
    - "運河發現一具男性浮屍，身有太尉府外院車馬房『丙七』銅牌。"
    - "驗屍顯示並非杜成：死者約五十、手有兵器繭、左腿舊折；杜成檔案約三十四且無此舊傷。"
    - "丙七牌本屬車夫鄭老六；鄭老六本人活著，稱三日前已把牌交回杜成。"
  implication:
    - "真牌被放到錯誤死者身上，可能涉及身份誤導或栽置；目的未定。"
```

---

# 10｜何進安與「死人簿／絕戶支」

```yaml
HE_JINAN:
  identity: "廣源南倉年輕帳房"
  status: "PROTECTED_WITNESS"
  confirmed:
    - "何進安主動到定陶，帶來俗稱『死人簿』之資料；正式名目為『絕戶支』。"
    - "其描述：用於失蹤／死亡／不便公開工人之欠薪、家給、屍體、水路或封口等秘密支出；具體每一筆用途仍需查。"
    - "其鞋底藏有前一日抄下的一頁。"
    - "條目包括：丁七40河工、己三25家給、癸九80水、丙十一120未結。"
    - "癸九日期為柳生失蹤三日後；是否柳生未知，『水』含義未知。"
    - "丙十一日期為今日；『未結』據何稱可在事件發生前先開項，但仍需獨立查證。"
    - "何進安後來回憶丙十一旁曾有一個小『梁』字，後被二掌櫃刮掉；目前只有其證言。"
    - "押送途中車內遭箭投／威脅紙：『交人則全家死』。原件已由開封府封存。"
  public_banner:
    - "白御行後命潘金蓮做巨大『交人則全家死』布牌公開懸掛，以提高威脅事件可見度。"
    - "布牌只是宣傳／警示，不是證物本體；來源不得自行歸咎任何一方。"
```

---

# 11｜西門慶：被棄子後主動交出暗櫃

```yaml
XIMEN_CURRENT:
  status: "IN_KAIFENG_CUSTODY; ACTIVE_SELF_PRESERVATION"
  confirmed:
    - "西門慶在開封府供稱昨日曾勸梁福逃。"
    - "他稱梁福危險來源為廣源，點名許奉年。"
    - "他稱許奉年曾透過人傳話，梁福知道太多，應暫離京；他又稱杜成參與傳警。"
    - "上述皆為西門慶供述，第三人罪責需獨立互證。"
    - "在太尉府正式表示不庇護梁福／杜成之後，西門慶主動提出開西門府書房暗櫃。"
    - "他要求官員、章文度與兩名獨立帳房在場，文件全部交開封府控制。"
    - "西門慶明示：『有些東西，放在我家裡時是我的催命符；放到包府尹手裡，才是我的保命符。』"
  structural_state:
    - "其策略是用可進卷、可獨立查的資料提高自身活著的價值。"
    - "不得預設他下一步必然說真話，也不得預設所有暗櫃文件都是偽造。"
```

---

# 12｜暗櫃第一層至「高宅舊事」

## CAB20-E01｜廣源帳與路線副簿

```yaml
SECRET_CABINET_LAYER_1_2:
  confirmed:
    - "第一層為銀票、地契、借據等普通商業文件。"
    - "第二層發現十二冊廣源暗帳，以及玄字／青字路線副簿。"
  effect:
    - "沈萬三在十三娘賭局中下注『廣源母簿去向』因此變亮，但尚未判定已中。"
```

## CAB20-E02｜高宅舊事／陳氏女

```yaml
GAO_HOUSE_OLD_CASE:
  container_label: "高宅舊事"
  contents:
    - "一張女子賣契"
    - "兩張傷勢／醫治單"
    - "五百兩銀號兌票"
    - "兩封西門府與高宅往來短簡"
    - "一份開封府舊狀撤回抄件"
  old_complaint:
    - "布商之女陳氏於元宵燈會後失蹤，三日後受傷返家。"
    - "其父曾控『高衙內強擄民女，拘於城西別宅』，後撤狀。"
  relevant_letters:
    - "疑似高宅管事：『公子失手，陳家不識抬舉，煩大官人料理。』"
    - "另一無署名：『五百已付，狀已撤，人勿再動。』"
  legal_status:
    - "文件存在可成為重新找陳家、查筆跡、查銀號與舊卷的線索。"
    - "五百兩與撤狀在時間上相關，不等於已證明是封口銀。"
    - "包拯已封存，未因文件存在即直接定罪。"
  ximen_statement:
    - "西門慶稱保留此類資料，是要證明自己不是只有一張嘴。"
```

## CAB20-E03｜林教頭／陸某線索

```yaml
LIN_FAMILY_HINT:
  confirmed_documents:
    - "『林教頭家事，勿再經府。』"
    - "『陸某已辦，公子可安。』"
    - "一張舊一百兩兌票，收受姓『陸』。"
  not_established:
    - "『林教頭』確指林沖。"
    - "『陸某』確指陸謙。"
    - "一百兩用途。"
    - "林娘子遭高衙內直接殺害。"
  director_correction:
    - "目前只可談高衙內長期騷擾／逼迫林娘子、林沖被陷害流放等可查方向；不得把『被玩死』當已證實直接殺人。"
```

---

# 13｜《觀止五千》暗櫃資料與潘金蓮責任邊界

```yaml
GUANZHI_5000_ENVELOPE:
  label: "觀止五千"
  contents:
    - "西門府五千掛牌付款副本／存根"
    - "掛牌夜席次與競價簡錄"
    - "無署名短箋：『照約出價。散後由後門回。阿麗婭不動。餘事後議。』"
    - "西門慶私人備忘：『五千非買人。買牌，買名，買眾人不敢碰。潘有她的算盤，我有我的回報。散場之後，另算。』"
  evidence_status:
    - "可支持西門慶五千出價不是完全臨場起意，且存在事先安排之高度線索。"
    - "『潘有她的算盤』是西門慶個人備忘中的判斷／描述，不單獨證明潘金蓮完整內心或所有前置計畫。"
    - "文件沒有一句直接證明潘金蓮命令打柳生、事前知道柳生必到、或五千即殺人錢。"
  ximen_trigger:
    - "包拯問『散場之後，另算何事？』時，西門慶答：『這一件，請潘五娘自己來說。』"
  pan_response:
    - "潘金蓮明示願意上堂面對，不先逃避。"
```

---

# 14｜阿麗婭五千兩法律狀態

```yaml
ALIYA_5000_STATUS:
  current: "UNDER_OFFICIAL_CLARIFICATION"
  confirmed_questions:
    - "當年五千兩究竟取得何種權利。"
    - "是否全額支付。"
    - "期限、終止條件與是否仍存效力。"
    - "若舊權消滅，阿麗婭僅解除西門慶該項限制，還是另有後果。"
  aliya_position:
    - "阿麗婭自願去開封府聽官府確認『我現在還是不是他的／五千是否還能決定我的事』。"
    - "她沒有因此同意重新掛牌。"
  pan_business_interest:
    - "潘金蓮承認若阿麗婭日後自願重新掛牌，商業價值極高。"
    - "該想法不具有對阿麗婭的強制力。"
  still_unknown:
    - "官府最終如何認定五千兩權利效力。"
```

---

# 15｜太尉府給潘金蓮的「鬼牌」私函

```yaml
TAIWEI_PRIVATE_LETTER:
  status: "EXISTS; CONTENT_PRIVATE_AND_UNKNOWN_TO_FENGMANLOU"
  recipient: "潘金蓮本人"
  sender: "太尉府"
  confirmed_chain:
    - "太尉府差役將封緘私函送到觀止，明示收件人為潘金蓮本人，不是觀止公開公文。"
    - "潘金蓮拒絕讓風滿樓、白御行、蘇清、許慎言等人自行查看。"
    - "她先自行拆閱／處理，內容未公開。"
    - "後續潘金蓮主動前往開封府，把原函、原封、送達時間與差役身分交包拯秘密查驗。"
    - "包拯確認：若內容涉及正在查的案件，可能依法取得案卷法位；潘金蓮知情後仍自願交查。"
    - "風滿樓只被准許公開『潘金蓮已自願把太尉府私函交開封府秘密查驗』，不公開內容。"
  prohibition:
    - "不得推定信中是威脅、收買、滅口、合作或其他任何具體內容。"
    - "不得因其神秘就自動升格為犯罪證據。"
```

---

# 16｜十三娘問心賭局

```yaml
SHISANNIANG_BET:
  status: "ACTIVE_UNRESOLVED"
  stake_rule:
    - "不賭銀。"
    - "輸者未來欠十三娘一個真實回答。"
    - "只准拿自己的真話下注，不得押別人的秘密、性命或家人。"
  target:
    - "西門慶下一步真正拿來保命、能進卷並改變局勢的東西。"
  bets:
    沈萬三: "廣源母簿的去向"
    趙受益: "一封不能只有西門慶自己證明真假的信／可在他死後仍可驗證的備份"
    蘇清: "西門慶不是單純咬人，而是會開條件／要求保護"
    白御行: "高衙內的另一個案子；必須與柳生不同，且足以讓開封府合法另查"
    潘金蓮: "拒絕下注"
  current_brightness_only:
    - "陳氏女舊案資料使白御行之下注高度發亮，但十三娘尚未正式判定勝負。"
    - "廣源十二冊暗帳使沈萬三之下注變亮，但未確認即母簿。"
    - "西門慶以暗櫃換保命價值與先保文件再答之姿態，使蘇清方向部分吻合，但未結算。"
    - "趙受益之『可獨立驗證、死後仍成立的信』尚未明確出現符合物。"
  anti_closure:
    - "不得因局勢像某人的答案，就提前替十三娘宣布輸贏。"
```

---

# 17｜西門慶供出柳生案「丙七」青篷車

```yaml
LIUSHENG_BINGQI:
  source: "西門慶本人供述"
  confirmed_statement:
    - "西門慶稱柳生被打到站不起來後，最後不是直接拖去長街河邊，而是由觀止側巷抬上一輛青篷車。"
    - "他稱該車屬太尉府外院車馬房。"
    - "他報出的牌號為『丙七』。"
    - "他稱暗櫃高宅舊事中可能另有車馬牌簡記可供查。"
  official_response:
    - "包拯禁止直接把數年前柳生案的『丙七』與今日浮屍身上的『丙七』視為同一條因果。"
    - "開封府將先查太尉府車馬房舊制、牌號是人牌／車牌／值房牌、歷年是否沿用、當夜領牌與值勤紀錄。"
  status:
    - "高價值交叉線索；尚未閉環。"
```

---

# 18｜蘇清正式委託許慎言：口頭賭約、賣身契、後堂帳分軸

## SUQ20-E01｜委託成立

```yaml
SUQING_LEGAL_REPRESENTATION:
  status: "AUTHORIZED_BY_SUQING"
  client: "蘇清"
  lawyer: "許慎言"
  payer: "白御行"
  confirmed:
    - "白御行表示無論狀子成不成、贏不贏，希望許慎言接案並由白御行買單。"
    - "蘇清本人明示委託許慎言。"
    - "許慎言不承諾一定提告、一定撤契或一定勝訴；先查資料，再決定合法攻點。"
  humorous_nonessential:
    - "白御行另送『觀止七十二次按摩券』作玩笑式謝禮；不構成案件交換條件。"
```

## SUQ20-E02｜三條必須分開的法律／證據軸

```yaml
SUQING_THREE_AXES:
  axis_1_oral_wager:
    status: "HISTORICAL_ORAL_AGREEMENT_EXISTS; FULL_TERMS_UNPROVEN"
    rules:
      - "蘇清與潘金蓮當年確有口頭賭局歷史。"
      - "到目前沒有正式書面賭約可證全部條款。"
      - "人物記憶、後來轉述與歷史印象可作證言或旁證，但不得冒充硬契。"
  axis_2_formal_sale_indenture:
    status: "FORMAL_DOCUMENT_CURRENTLY_VALID"
    confirmed:
      - "蘇清本人自願同意並簽署／畫押。"
      - "該正式賣身契不能只因口頭賭局爭議或阿麗婭五千權利失效就當然作廢。"
    invalidation_requires:
      - "契文本身的脅迫、欺詐、法定瑕疵，或"
      - "可證明契約明示受某條件拘束且條件失敗"
  axis_3_backroom_accounting:
    status: "NEW_ACTIVE_LEGAL_QUESTION"
    question:
      - "潘金蓮把蘇清送入西門府一月時，是何種法律／契約性質。"
      - "蘇清身契是否轉移。"
      - "有無金錢對價或服務價值入帳。"
      - "若未轉身契但用蘇清一月履行完成潘／西門之交易，該價值是否應計入蘇清自身帳項、贖身帳或另有返還／結算問題。"
```

---

# 19｜《五千後算》：開冊硬狀態

## WQ20-E01｜舊簿發現與封送

```yaml
WQ_HOUSUAN_BOOK:
  discovery:
    - "觀止舊後堂帳因開封府調取阿麗婭掛牌當夜後堂結算而重新整理。"
    - "春梅發現一本薄舊簿，封面右下角有褪色四字：『五千後算』。"
    - "許慎言制止現場私拆，要求原樣封存、記位置、到開封府在官吏與見證人面前開冊。"
  custody:
    - "觀止、帳房、開封府依程序封送。"
    - "開封府已在見證下開冊。"
```

## WQ20-E02｜第一組可見帳文

```yaml
WQ_HOUSUAN_VISIBLE_ENTRIES:
  observed_in_official_opening:
    - "『阿麗婭——留觀止，不交人。』"
    - "『西門慶——五千掛名，得預定之名。』"
    - "『散後另算。』"
  evidence_effect:
    - "支持當年五千安排至少在觀止後堂帳中被記成『掛名／預定之名』而非普通立即交人。"
    - "不自動決定阿麗婭今日法律狀態；仍須看完整契據、付款、期限與法理。"
```

## WQ20-E03｜蘇清條目

```yaml
SUQING_BOOK_ENTRY:
  observed_text:
    - "『蘇清，敗約後入西門府一月。』"
    - "『身契不轉。仍存觀止。』"
    - "『作西門大官人掃興之補。』"
    - "『不另折銀。』"
  current_hard_meaning:
    - "目前可確認該舊簿如此記載。"
    - "蘇清身契在該帳文中被記為不轉給西門慶、仍存觀止。"
    - "蘇清一月入西門府被記入潘／西門之後堂結算語境，並被稱為『補』。"
    - "『不另折銀』表示帳面沒有另列一個對蘇清的一次性折銀價；不等於蘇清客觀價值為零。"
  legal_unknowns:
    - "當時觀止依賣身契是否有權作此類派遣。"
    - "服務／派遣價值是否依法本來歸觀止。"
    - "是否應計入蘇清自己的贖身、分成或其他帳項。"
    - "有無其他隱藏／配套帳冊改變解釋。"
```

## WQ20-E04｜第三頁備忘

```yaml
WQ_HOUSUAN_MEMO:
  observed_text:
    - "『蘇清入府後，阿麗婭仍留。』"
    - "『五千之名不得撤，撤則前局皆廢。』"
  status:
    - "帳冊備忘存在。"
    - "『前局』之全部內容不由此兩句自動補全。"
```

---

# 20｜潘金蓮在開封府之本人供述

```yaml
PAN_JINLIAN_TESTIMONY:
  status: "PARTIAL_SELF_TESTIMONY; NOT_TOTAL_OBJECTIVE_TRUTH"
  confirmed_statements:
    - "潘金蓮承認五千掛牌夜不是普通即興掛牌。"
    - "她承認曾主動找西門慶，利用其出價能力與名聲把阿麗婭身價推高，同時讓外界認為碰阿麗婭等於碰西門慶之預定對象。"
    - "她表述核心效果是讓阿麗婭留在觀止、不被直接帶走，並借西門慶名義形成保護性威懾。"
    - "她承認《五千後算》中涉及蘇清『作掃興之補』『不另折銀』等字句出自自己的帳法／安排。"
    - "她表示：與蘇清打口頭賭局時，她確實考慮過若蘇清輸，敗約後要如何收束／交付。"
    - "她明示：並非從一開始就固定『一定送給西門慶』；西門慶是後來成為合適的承接者。"
  unresolved:
    - "口頭賭局完整原始條款仍未被硬證據證明。"
    - "潘是否在每一個早期節點已預見柳生、高衙內、五千與蘇清全部後果，不能從其目前供述逆推。"
    - "潘與西門是否還有未公開之其他交換內容。"
  critical_boundary:
    - "潘承認五千安排與蘇清後堂交付，不等於承認自己命令高衙內施暴、命令手下處理柳生或參與柳生死亡。"
```

---

# 21｜蘇清目前訴訟／查帳方向

```yaml
SUQING_CURRENT_LEGAL_GOAL:
  immediate_goal:
    - "不以『我從未同意賣身』作方便故事。"
    - "不先主張正式賣身契當然無效。"
    - "要求把當年從口頭賭局、正式簽契、五千掛牌、敗約、入西門府一月、回觀止之間的帳與文書完整拆開。"
  new_core_question:
    - "觀止是否可在不另計價、不記入蘇清自身帳項的情況下，以蘇清一月之履行利益完成潘金蓮與西門慶間的交易／結算。"
  requested_documents:
    - "蘇清正式賣身契原件"
    - "簽契當日見證、經手與帳房登錄"
    - "是否存在身契轉移文件"
    - "蘇清入西門府一月之觀止帳目／收入／支出／回帳"
    - "阿麗婭掛牌前後之後堂結算與五千兩資料"
    - "當年口頭賭約之見證、旁證、相關帳錄"
  requested_procedure:
    - "蘇清希望在開封府查閱涉及自己姓名、身契與該一月的部分；不主張查看觀止全部商業帳。"
  stated_attitude:
    - "即使最後證明契有效、潘依法有派遣權、自己沒有可取回銀兩，她仍要查清楚。"
    - "她要求潘金蓮先讓帳說、讓西門慶說、再由潘與她各自說，不接受先用漂亮敘事收口。"
```

---

# 22｜西門慶、潘金蓮、蘇清三方目前互咬結構

```yaml
TRIANGULAR_STATE:
  ximen_qing:
    - "以暗櫃、舊案與後堂資料增加自己活著的交換價值。"
    - "把『散場之後另算』推回潘金蓮本人說明。"
  pan_jinlian:
    - "沒有否認五千局與蘇清後堂結算。"
    - "選擇上堂、交帳、承認部分自己做過的安排。"
    - "仍可在法律上主張自己當年依契有權派遣蘇清、帳務不欠蘇清等抗辯；尚未裁決。"
  su_qing:
    - "不靠否認自己簽契求脫身。"
    - "轉而攻擊『她的一月履行如何被用來結潘／西門的帳，卻未記到她自身帳上』。"
  structural_result:
    - "三方皆有可說之法位；目前沒有任何一方已獲終局勝負。"
```

---

# 23｜趙受益與身分邊界

```yaml
ZHAO_SHOUYI:
  current_public_name: "趙受益／趙先生／趙兄"
  confirmed:
    - "其曾由觀止秘密／地下通道方式出現並留在大堂看整夜大局。"
    - "對朝廷、皇帝、權門程序有異常熟悉程度。"
    - "曾由潘安排紅袖、浮香、辭歲可自行決定是否陪談；三人皆依自身意願行事。"
    - "他與李師師有瘦金字體玩笑，雙方均否認因此定情。"
  prohibited:
    - "不得由導演自動公開其更高真實身份。"
```

---

# 24｜辭歲假設掛牌賭價

```yaml
CISUI_HYPOTHETICAL_AUCTION:
  status: "HYPOTHETICAL_ONLY"
  confirmed:
    - "辭歲尚未設定正式掛牌日。"
    - "她曾拒絕白御行先前要求『二十八日後仍永久保持心理牽引／不可撤回慾望』的條件。"
    - "她明示拒絕的是該契約條件，不是永久禁止白御行未來參與合法掛牌。"
    - "假設性出價曾出現：沈萬三1500、趙受益1800、李師師代理白御行2000。"
  rule:
    - "未來真掛牌，誰有資格參與由辭歲與觀止當時規則決定。"
    - "假設出價不建立任何性、關係或交易權。"
```

---

# 25｜常煒與白三娘

```yaml
CHANGWEI_BAISANNIANG:
  status: "VISIBLE_INTEREST_ONLY"
  confirmed:
    - "白御行曾調侃常煒是否喜歡白三娘、是否要贖作妾。"
    - "常煒承認自己確實多看過白三娘幾眼，欣賞其實際照料與作風。"
    - "白三娘若要談離觀止，優先問的是她自己想不想走、想過什麼生活；妾位或價錢不是第一問。"
    - "常煒表示若真去問，不會以價格開場。"
  not_established:
    - "戀愛"
    - "贖身交易"
    - "婚／妾約"
```

---

# 26｜白御行關於「枕邊人／背叛」之本輪台詞法位

```yaml
PLAYER_UTTERANCE_TRACE:
  confirmed_player_statements:
    - "白御行表示自己更相信睡在身邊的女人，認為背叛機會可能較低。"
    - "白御行補充：自己曾被最愛的女人背叛，因此並非不知道親密關係會失敗。"
    - "其真正重點是：越親近，敏感的人越可能察覺對方態度／心意變化；屬下則可能用制度性表面更容易隱瞞。"
  world_effect:
    - "形成白御行、沈萬三、蘇清、潘金蓮、李師師等一輪用人／信任討論。"
  not_established:
    - "枕邊人客觀上必然更忠誠。"
    - "白御行一定能準確判定任何人的變心原因。"
    - "任何現有女人因此取得或喪失關係資格。"
```

---

# 27｜立即未決事項

```yaml
OPEN_HOOKS:
  highest_priority:
    - "《五千後算》其餘頁面是否還有更直接的結算、價值、簽名、轉移或相關人名。"
    - "蘇清正式賣身契原文究竟授予觀止／潘金蓮何種派遣、收益與贖身權。"
    - "蘇清入西門府一月之收益是否有其他帳項，是否應計入其個人帳／贖身帳。"
    - "阿麗婭五千兩『預定之名』今日法律效力如何。"
    - "潘金蓮與西門慶『散場之後另算』是否仍有尚未出現的內容。"
    - "蘇清只願先向包拯私供之西門慶秘密內容。"
    - "太尉府私函的內容及其是否被包拯判定與案情相關。"
    - "西門慶暗櫃是否還有下一層保命資料。"
    - "陳氏女舊案是否取得足以正式另查的獨立來源。"
    - "林教頭／陸某線是否可獨立指向林沖／陸謙。"
    - "柳生案『丙七』與今日浮屍丙七是否只是沿用牌號、栽置，或存在歷史連接。"
    - "梁福、杜成、許奉年各自目前下落與責任。"
    - "廣源母簿真正位置。"
    - "何進安『丙十一／梁』是否涉及梁福及『未結』預開用途。"
    - "十三娘問心賭局最終誰中。"

  relationship_open:
    - "李師師私人帳何時真正修復／是否修復。"
    - "李瓶兒法律切割西門慶後，是否接受如夫人位置及何時成立。"
    - "張麗華在白御行選李瓶兒之夜後的實際反應尚未演出，不得補寫。"
    - "蘇清二十八日私人約仍只有在西門慶真正失勢／倒台後開始；目前尚未啟動。"
    - "若西門慶真正倒台，蘇清曾表示可能另加第二十九日；尚未到觸發點。"
```

---

# 28｜法律戰硬規則／防導演過度收斂

```yaml
LEGAL_WAR_INVARIANTS:
  - "在場 ≠ 下令暴力。"
  - "同日 ≠ 因果。"
  - "帳冊證明金流 ≠ 自動證明用途。"
  - "銀角剪痕／牌號習慣 ≠ 指令來源。"
  - "供述可成線索，第三人罪責仍需互證。"
  - "秘密文件存在 ≠ 文件內容全部真實。"
  - "公開風滿樓提高可見性與證人安全成本，不等於提高證據力。"
  - "定陶商會無官府拘捕權；只能保護、觀察、傳遞、提供資源。"
  - "包拯不得只靠政治直覺非法搜太尉府。"
  - "高俅／太尉府可聘狀師、做程序抗辯、分案、切割責任；不得預設必敗。"
  - "西門慶可撒謊、切人、交真證、交半真資料、談條件；不得預設其必然被滅口或必然翻供。"
  - "潘金蓮承認五千局 ≠ 承認柳生暴力。"
  - "蘇清賣身契有效 ≠ 潘金蓮的所有歷史帳務必然合法。"
  - "阿麗婭五千權利失效 ≠ 阿麗婭欠新掛牌。"
  - "『閉環』只在證據真正互證時成立，不得用故事高潮替代法律閉環。"
```

---

# 29｜下一導演接關警告

```yaml
CONTINUATION_GUARD:
  must_preserve:
    - "目前 HOLD，不推進時間，直到玩家解除 HOLD／明示繼續。"
    - "白御行的台詞、行動、內心與重大選擇仍由玩家控制。"
    - "潘金蓮目前最後確認在開封府，不得無交代瞬移回觀止。"
    - "蘇清口頭賭約完整條款未證，不得寫成已有正式原約。"
    - "正式賣身契目前有效，不得因『五千後算』一出就直接宣判作廢。"
    - "《五千後算》目前證明的是帳文存在＋部分潘本人供述；法律效果仍待審。"
    - "太尉府私函內容保持 UNKNOWN，除非後續由潘、包拯、正式卷宗或合法事件揭露。"
    - "柳生是否死亡保持 UNKNOWN。"
    - "阿麗婭是否解除五千預定權保持 UNDER_OFFICIAL_CLARIFICATION。"
    - "十三娘賭局保持未結算。"
    - "風滿樓是觀止內部大型公域拓撲展開，不回退成『整條街觀眾席』版本。"
    - "說書先生只能轉述公開材料，不能因高潮自行補罪。"
    - "西門慶仍是會自救、會談條件、有律師的主動人物，不是等死反派。"
    - "潘金蓮仍可用帳、權、風月與生存角度抗辯，不得因被查帳就洗成認錯道德講師。"
    - "蘇清目前主攻帳與法位，不是突然變成受害療癒話術人物。"
  next_scene_candidate:
    - "開封府繼續讀《五千後算》／查正式賣身契與相關帳。"
    - "包拯處理阿麗婭五千權利之初步法理。"
    - "潘金蓮就後堂帳與自己當年權限提出正式抗辯。"
    - "西門慶繼續以暗櫃或條件換取保命。"
    - "太尉府或廣源提出新的程序／證據反擊。"
  no_forced_choice_menu: true
```

---

# 30｜本 HOT 的一句接關摘要

> **風滿樓已開，數千人看的是一場尚未有結局的公案。西門慶靠暗櫃把自己的命變成證據市場；潘金蓮把太尉府鬼牌交給包拯秘密查，又被《五千後算》迫回自己當年的後堂局；蘇清不否認自己簽過賣身契，改以「我那一月究竟被怎麼算帳」向潘金蓮追索法位與帳目。此刻帳已開，勝負未判。**

<!-- SOURCE_HOT_V2_4_END -->

---

## SOURCE ARCHIVE｜HOT V2.5

**檔名：** `觀止青樓_白御行線_HOT_SAVE_V2.5_槐月二十日深夜_開封法網擴張_阿麗婭重定義與六條御息所來訪版.md`  
**SHA-256：** `a2107c0df322779ea1ed0f74a59502c63ea52594fded2a295a258f6e68997083`

<!-- SOURCE_HOT_V2_5_BEGIN -->
# 觀止青樓｜白御行線 HOT SAVE V2.5
## 理火三年槐月二十日深夜｜開封法網擴張 × 阿麗婭身分重定義 × 六條御息所來訪 × 趙受益茶約前置版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V2_5_HUAI20_LATE_NIGHT_KAIFENG_NET_AALIYAH_ROKUJO"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V2.5"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime:
    - "GUANZHI_QINGLOU_V10_0"
    - "GUANZHI_QINGLOU_V10_1_V10_2_PATCH_WHEN_APPLICABLE"
  story_date: "理火三年槐月二十日深夜"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AT_GUANZHI_INNER_COURTYARD_AFTER_ROKUJO_GUEST_ROOM_ACCOUNT"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V2.4_槐月二十日深夜_風滿樓公案與五千後算開冊版.md"
  previous_hot_sha256: "ad757d9a4b2e612b0c606d44dbf55c857d40e8d7e792db18839a3faa50d088f5"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"
  current_location: "觀止青樓／內院；風滿樓與開封府法律線仍並行運作"
  direct_resume_owner: "WORLD_OR_PLAYER_AFTER_HOLD_RELEASE"
  save_scope:
    - "HOT V2.4 後開封府對西門慶、高衙內、廣源、杜成、梁福等之法網擴張"
    - "五千後算後續：西門慶接受蘇清一月作替代結算、潘金蓮筆跡殘條與蘇清兩時段法位切割"
    - "阿麗婭舊五千掛牌之初步法律狀態、目前半良家／準妓女位置與未重新掛牌決定"
    - "阿麗婭對未來出閣制度、候選篩選與一期婚之候選構想"
    - "趙受益與紅娘氏既往第一筆紅倌交易之去污染校正"
    - "白御行關於龐春梅、疏影、親密關係與女人之本輪有效自我陳述"
    - "人物圖畫展示事件及其人物反應；不自動改人物基線"
    - "六條御息所以共鳴召喚／未知來客形式進入觀止之 ROUTE EVENT"
    - "六條御息所與白御行之源氏資訊對談、與趙受益之初次認識及茶約前置"
    - "六條御息所今晚女客住宿安排與趙受益代付之無權利帳務"
```

---

# 0｜提交法位、來源與反污染說明

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V2.4_槐月二十日深夜_風滿樓公案與五千後算開冊版.md"
    role: "本檔直接前置 HOT；V2.4 以前事件全部繼承"
  long_term_master:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"
    role: "長期因果與早期玩家線來源；僅固化至 HOT V1.9"
  route_conversation_commit:
    role: "HOT V2.4 之後至本次 SAVE 命令的直接劇情來源"
  persona_source:
    file: "觀止人物卡_LCAPG_V1.1-R1_原始重構去污染版_含辭歲_導演隱藏區增補.md"
    role: "原生人物基線來源；本檔不得以玩家線事件倒灌修改"
  character_pool:
    file: "觀止人物池_LCAPG_V1.1_紅娘氏與李師師雙人正式版.md"
    role: "紅娘氏、李師師平級人物來源"
  summoning_rule_source:
    file: "觀止青樓版V10.0_成人場景Runtime_人物主權_安全層降權_反聖母污染正式版.md"
    role: "人物召喚／未知來客／共鳴召喚之文件級規則來源"

COMMIT_NOTE:
  - "本檔取代 HOT V2.4，成為白御行線當前直接接關切片。"
  - "本次只做 HOT SAVE；不更新 MASTER、不改人物卡、不改人物池、不新增六條御息所至常設人物池。"
  - "六條御息所本次屬白御行線 ROUTE_EVENT／UNKNOWN_VISITOR_ARRIVAL；是否長住、掛牌、成為常設人物均未成立。"
  - "玩家在劇情中對六條御息所、光源氏、藤壺、紫姬、秋好等所述未來故事內容，保存為『白御行提供之未來資訊／故事敘述』；除非另有世界來源互證，不得自動升格為六條原時代的客觀可證事實。"
  - "玩家對六條『最想要權力／其實不愛源氏只愛血統』之判斷，六條本人未接受為定論；此項不得寫成她的固定內心真相。"
  - "人物圖畫只保存為本輪展示物與人物反應；圖上文案不自動成為人物履歷、世界真相、公開招牌或人物卡描述。"
  - "人物說『收了／拿走』圖畫可保存為當下持有／表態；白御行未明示贈與時，不擅自補成法律所有權永久轉移。"
  - "開封府之供述、官方暫時處置、證人證詞、帳冊與 DIRECTOR_FIXED_HISTORY 分軸保存。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年槐月二十日"
  time: "深夜；精確時刻未定"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"
  primary_location: "觀止青樓／內院"

  player:
    name: "白御行"
    location: "觀止內院"
    last_confirmed_utterance:
      - "『人家沒成交，不算賣。』"
    no_new_player_action_after_save_command: true

  confirmed_present_or_immediately_active_in_inner_courtyard:
    - "白御行"
    - "六條御息所"
    - "趙受益"
    - "蘇清"
    - "李師師／可從聽雨小閣或內院近處參與"
    - "張麗華"
    - "紅娘氏"
    - "十三娘"
    - "阿麗婭"
    - "春梅／已介入女客房與帳務安排"
  intermittent_or_exact_position_not_required:
    - "小翠曾在圖畫展示時出現；當前是否仍坐同桌 UNKNOWN"

  offsite_confirmed:
    潘金蓮:
      current: "開封府"
      status: "接受五千後算、蘇清替代結算及相關權限問題查問"
    西門慶:
      current: "開封府羈押／訊問中"
    包拯:
      current: "開封府主持多線並行程序"

  direct_resume_point:
    - "六條御息所已被安排今晚暫住內院東偏廂女客房，但尚未確認她已離席或進房。"
    - "趙受益已同意支付六條今晚客房、茶食、必要衣物日用等女客開銷，並明示不因此取得任何人身、服務、陪宿、性、關係或契約權利。"
    - "六條與趙受益只成立『初次認識＋今晚可同桌喝茶』；未成立戀愛、交易、陪宿、婚配、候選承諾。"
    - "六條牛車與紅楓異路最後確認仍在月門外附近，春梅命人暫勿碰；其能否作為返回原時代的通道 UNKNOWN。"
    - "開封府法律線仍在並行推進，但本鏡頭已回到觀止人物／關係場。"
```

---

# 2｜開封府：五千後算後續硬進展

## KFY20-E01｜西門慶承認蘇清一月為五千替代結算

```yaml
SUBSTITUTE_CONSIDERATION_RECORD:
  evidence_status: "HARD_COURT_RECORD_BY_ADMISSION; FINAL_LEGAL_EFFECT_NOT_YET_JUDGED"
  confirmed:
    - "西門慶在開封府明示：潘金蓮後來對其表達過『阿麗婭不給你；蘇清那一月你也拿了；五千那筆別再翻』之意。"
    - "潘金蓮承認自己曾對西門慶作出此類結算表述。"
    - "西門慶承認自己接受蘇清一月作為替代結算，因此其後未再要求取得阿麗婭。"
  current_effect:
    - "形成強硬記錄：五千帳名在阿麗婭，實際替代利益落在蘇清一月，且西門慶接受替代。"
    - "此記錄強烈削弱西門慶再以舊五千要求阿麗婭出閣／帶走／性服務之主張。"
  not_yet_final:
    - "對潘金蓮與觀止之民事、帳務、契約責任最終如何切割。"
    - "蘇清一月之法定價值、收益歸屬與損害是否成立。"
```

## KFY20-E02｜潘金蓮筆跡殘條

```yaml
PAN_FRAGMENT:
  evidence_status: "PHYSICAL_FRAGMENT_PLUS_HANDWRITING_ADMISSION"
  observed_text:
    - "『……蘇清一月，抵五千後帳。』"
    - "『……人不轉契。』"
    - "『……西門自取。』"
    - "『……月滿還樓。』"
  confirmed:
    - "潘金蓮承認殘條字跡為自己所寫。"
    - "殘條上下文殘缺。"
    - "潘承認自己可能曾讓西門慶『自行找／自取』蘇清，但否認因此授權暴力拖拽、囚禁、威脅或強迫性行為。"
    - "西門慶主張其當時理解為可以自行把蘇清弄到府中；此為其本人說法。"
  prohibited_inference:
    - "『西門自取』不得直接等同『潘命令家奴暴力抓人』。"
    - "殘條不能單獨證明潘知悉每一個後續強制手段。"
```

## KFY20-E03｜蘇清兩時段切割

```yaml
SUQING_TWO_PERIODS:
  government_archive_found:
    pre_ximen_month:
      confirmed_absence:
        - "未找到蘇清原始服務報備。"
        - "未找到處女良家掛牌申請。"
        - "未找到合法首次出閣拍賣文件。"
    post_return:
      confirmed_document:
        - "蘇清在西門府二十八日後返回觀止，親自提出入妓籍／紅倌方向之申請。"
        - "申請內容表明其已非處女，不要求走處女良家首次出閣拍賣路徑。"
        - "文件有蘇清本人書寫／畫押；蘇清在當前程序中確認筆跡與當時自願決定。"
  bao_current_split:
    period_1: "西門府二十八日：合法性與強制問題另查；不得被後來自願入妓籍回溯洗白。"
    period_2: "回觀止後自願入妓籍：具獨立成立可能，可作目前妓籍／紅倌身分之另一路合法來源。"
  current_boundary:
    - "後來自願留在觀止，不等於前二十八日自願。"
    - "前二十八日若違法，也不自動令她後來自主申請全部失效。"
```

## KFY20-E04｜蘇清原始被送入西門府之因果分層

```yaml
SUQING_FORCED_MONTH_CAUSAL_SPLIT:
  director_fixed_history:
    - "蘇清當年實際被西門府家奴以暴力拖入偏院。"
    - "西門慶對蘇清以死亡／折磨等方式施壓，實際控制其二十八日。"
  current_public_or_court_evidence:
    - "潘金蓮與西門慶之替代結算關係已有硬記錄。"
    - "潘筆跡『西門自取』存在，但授權暴力與否尚未被硬證據證明。"
  legal_split_to_preserve:
    pan_jinlian_axis: "把蘇清一月納入其與西門五千後帳，以及當時是否具有處分／派遣蘇清之權。"
    ximen_qing_axis: "實際取得、暴力拖拽、囚禁、威脅及可能的性強迫責任。"
    su_qing_later_choice_axis: "月滿回觀止後之自願入妓籍決定，獨立評價。"
```

---

# 3｜阿麗婭：舊五千權利、目前身分與未重新掛牌

```yaml
AALIYAH_CURRENT_STATUS:
  legal_base:
    status: "半良家／準妓女"
    cause:
      - "阿麗婭曾完成政府服務報備，可進堂作非性服務。"
      - "其曾本人申請掛牌並有五千拍賣結果，但未實際出閣到西門府。"
      - "未發生 D+0 首次出閣、未發生二十八日妾期、未發生 D+28 休回，因此原本未來生效之售契條件未完成。"
  kaifeng_provisional_position:
    - "西門慶又已承認接受蘇清一月作替代結算。"
    - "目前缺乏新文書時，舊五千不得用來要求阿麗婭被帶走、出閣或提供性服務。"
  current_choice:
    - "阿麗婭沒有在取得上述釐清後立刻重新掛牌。"
    - "她明示今晚先不重新把自己賣出去／不立刻進入新的首次出閣程序。"
  permitted_now:
    - "依半良家／準妓女位置，可做核准之非性堂務服務。"
  not_established:
    - "紅倌性服務義務"
    - "任何新首次出閣對象"
    - "白御行或趙受益對其之取得權"
```

---

# 4｜觀止籍制：本輪 GM 校正後的現行流程

```yaml
GUANZHI_STATUS_SYSTEM_CURRENT_GM_RULE:
  stage_0_entry:
    - "女子進觀止後尚不能直接服務。"
    - "由本人自願申請服務，觀止向官府報備數日。"
    - "官府做基本來源／逃奴等身家調查與資料留存，但不替申報內容保證絕對真實。"
  during_filing:
    status: "完整良家"
    rule: "不可入堂服務；辭歲曾在此階段遭鹽商騷擾。"
  after_filing:
    status: "半良家／準妓女"
    rule:
      - "可正式入堂談話、陪酒、非性服務。"
      - "不得因已報備就被當作紅倌性服務。"
      - "也不是完全自由離場的普通外客身分。"
  virgin_first_out_path:
    - "具資格之處女良家可本人申請掛牌出閣。"
    - "拍賣結算時同時簽售契與休書，但兩者均約定 D+28 才生效。"
    - "D+0 至 D+28：首次買主家中以妾身分生活二十八日。"
    - "D+28 休回後，觀止售契才生效，進入正式妓籍／紅倌路徑。"
  nonvirgin_or_slave_path:
    - "掛牌拍賣不是所有紅倌的必要前置。"
    - "奴籍或非處女等其他既有身分可依合法程序直接轉妓籍／紅倌，不必做處女首次出閣拍賣。"
    - "紅娘氏屬此類：無處女初出拍賣資格，走直接紅倌訓練／營運路徑。"
  invariant:
    - "妓籍取得 ≠ 一定經過拍賣。"
    - "拍賣＝處女良家首次出閣之特殊路徑。"
```

---

# 5｜阿麗婭：未來首次出閣／一期婚構想

```yaml
AALIYAH_FUTURE_CONCEPT:
  lifecycle: "PROPOSAL_IN_ROUTE_ONLY"
  confirmed_preferences:
    - "她對未來可能重新申請首次出閣仍有興趣，但不在今晚決定。"
    - "她希望公開程序不必等於毫無篩選的大規模價高者得；可先建立真正、公開、非造假的資格條件，再由合格者競價。"
    - "她關心的是二十八日共同生活是否合適，包括關係、生活、親密習慣、是否尊重 D+28 分開。"
    - "她不希望第一次出閣只是『被交付』。"
    - "她對『一期婚』概念有興趣：明知開始與結束、二十八日、自選男人。"
    - "她認為完成首次二十八日不應自動決定她之後要跟多少男人發生性關係；首次出閣與後續性服務應可分開討論。"
  regulatory_unknown:
    - "觀止與官府是否允許『指定首主』或僅限少數合格人公開競價，尚未成為正式制度。"
    - "才華、承諾、資產等非現銀條件能否折算為合法競價對價，尚未確認。"
```

---

# 6｜阿麗婭候選紙：白御行與趙受益

```yaml
AALIYAH_CANDIDATE_NOTES:
  status: "PERSONAL_EXPLORATORY_NOT_AUCTION_REGISTRATION"

  bai_yuxing:
    current: "留審／未報名／未承諾"
    self_disclosures_heard_by_aaliyah:
      - "白御行有張麗華情人關係。"
      - "白御行明示自己不是一對一專屬型男人，二十八日期間可能仍有其他女人。"
      - "白御行曾談及與張麗華、蘇清、李瓶兒等多人親密／群體經驗脈絡。"
      - "白御行與李師師已有性交，且曾在說『我愛你』後立即穿衣離開，成為李師師私人帳之一。"
      - "白御行主張自己有時故意做死，因為覺得好玩。"
      - "白御行主張部分負面形象可能是刻意自污以降低外界戒心；阿麗婭只記錄為本人主張，真偽待觀察。"
    aaliyah_current_assessment:
      - "若她要二十八日專屬／每晚回家型男人，白御行條件偏差。"
      - "若她選擇熱鬧、非專屬但坦白的二十八日，白御行仍可觀察。"
      - "她不希望每天都是多人性場景；偶發嘗試是另一題。"
      - "她重視候選人是否把當下同意誤認為所有權、是否親密後立刻離開、是否遵守 D+28 分開。"
      - "白御行在『親密後是否留下』項有重大前科，若真進候選需本人說明。"
      - "核心句：可以壞；不能拿『我就是這種人』逃掉後果。"

  zhao_shouyi:
    source: "白御行推薦"
    current: "可觀察；未報名；未承諾競標"
    confirmed:
      - "白御行向阿麗婭推薦趙受益，稱其人品好，並坦言不知道其床上能力。"
      - "趙受益明示：白御行推薦是白御行的事；阿麗婭要不要把他列入觀察是阿麗婭的事；他自己是否答問題、是否參與由自己決定。"
      - "趙受益沒有登記、沒有答應競價。"
      - "阿麗婭記錄為：可觀察／願意受問。"
```

---

# 7｜趙受益 × 紅娘氏：舊交易去污染校正

```yaml
ZHAO_HONGNIANG_CORRECTION:
  correction_status: "HARD_ROUTE_CORRECTION"
  confirmed:
    - "紅娘氏與趙受益／趙禎曾完成紅娘氏第一筆正式紅倌成人交易。"
    - "交易地點為紅娘氏房內。"
    - "交易屬 COMPLETED_ADULT_TRANSACTION。"
    - "房錢歸觀止；成人服務身體費歸紅娘氏。"
    - "既有 HOT／MASTER 沒有記錄確切性交姿勢、技術或床上細節，故不得自動補寫。"
    - "此前導演曾錯寫紅娘氏『沒有跟趙睡過』，該輸出已撤回，不具世界法位。"
  current_knowledge:
    aaliyah: "已在候選討論中得知紅娘氏與趙有過一筆成人交易。"
    rokujo: "尚無來源得知此事；不得自動知道。"
  hongniang_boundary:
    - "紅娘氏不願公開八卦趙受益床上細節。"
    - "若阿麗婭日後真認真考慮，可私下詢問紅娘氏願意透露的部分，或直接問趙本人。"
```

---

# 8｜開封府：法網已跨入拘捕、封存、廣泛證人階段

```yaml
KAIFENG_COERCIVE_PROCESS_THRESHOLD:
  current_mode: "PARALLEL_ARREST_SEIZURE_WITNESS_NET"
  confirmed:
    - "案件已不再只停留於偵探式尋線；包拯依不同法源分別簽發拘提、封存、證人傳喚與查驗命令。"
    - "廣源母簿不是官府採取行動的必要前提；其價值在於決定法網能再往上攀到哪裡。"

  gao_son:
    - "高衙內已因柳生遭毆打、強行帶離與失蹤相關事實被正式帶入開封府處理。"
    - "其承認曾在酒後說過『拖出去，打斷腿扔河裡』類命令。"
    - "目前不等於已判殺人。"

  gao_servants:
    - "當晚直接涉入之數名高府家僕被分開控制／訊問。"

  guangyuan:
    - "廣源東庫、暗帳房、高溫爐相關作坊已被封存／扣押文書。"
    - "核心人員被控制；普通工人以識別、詢問為主。"

  ducheng:
    - "杜成已進入正式拘捕／通緝法位，不再只是尋人。"

  liangfu:
    - "梁福若找到須先控制、查傷、隔離訊問。"
    - "官府同時把他視為可能涉案者與高風險證人；目前下落未知。"

  witness_summons:
    - "舊工人、車夫、陳氏案書手／銀錢經手、其他關聯人已被擴大傳喚。"
```

---

# 9｜丙七：已校正為車牌／車號，不是個人牌

```yaml
BINGQI_VEHICLE_CORRECTION:
  hard_correction:
    - "『丙七』為車輛／車牌識別，不是某一名人的身分牌。"
    - "此前若把丙七視為個人身分碼的路徑已撤回。"
  known_history:
    - "鄭老六過去通常駕駛丙七車，之後把車與牌交給杜成。"
    - "浮屍身上出現的真丙七牌，不等於浮屍就是杜成。"
  guangyuan_dispatch_book:
    entries:
      - "槐月初九—廣源東庫"
      - "槐月十三—西城"
      - "槐月十五—梁宅"
    note: "槐月十五後未見正常歸還記錄。"
  active_order: "尋丙七車"
```

---

# 10｜何進安、萬勝腳店、梁宅密窖與母簿去向

```yaml
MOTHER_LEDGER_TRACE:
  he_jinan:
    confirmed_testimony:
      - "三年前曾抄過一本厚黑皮總簿，內容以癸九、丙七、丙十一等碼記帳。"
      - "梁福是令其抄簿的人。"
      - "其理解下層帳是『給人查』，上層總簿是『給人活命』。"
      - "最後一次在廣源東庫夾牆見總簿；隔日見梁福與杜成抬走一只青綠皮木箱。"
      - "聽到『別送回宅，找腳店寄』。"
  wansheng_inn:
    - "寄存簿顯示『梁二』曾存青綠皮木箱並續寄兩次。"
    - "十一日前有人以『杜成』名義／取票取走；實際取箱者身分尚未完全核實。"
    - "票背記『移交梁宅』。"
  liang_residence_cellar:
    findings:
      - "近期木箱壓痕。"
      - "暗排水／逃生結構。"
      - "狹條紙格式近似暗帳：『丙十一 一百二十 未結』、『癸九 八十 水』、『丙七 轉』。"
      - "紙條真偽與含義正在查。"
      - "現場不是母簿。"
    witness:
      - "附近老婦獨立供述：夜間曾見車與兩人像抬著一個人，其中一人拖腳／跛行。"
  unresolved:
    - "母簿真正位置。"
    - "十一日前取箱者是否真為杜成。"
    - "梁福與拖腳／跛行人物是否同一人。"
```

---

# 11｜馬成祿、丙七血跡、陶萬春

```yaml
MA_CHENGLU:
  status: "DETAINED_AFTER_ATTEMPTED_FLIGHT"
  confirmed:
    - "馬成祿試圖翻牆離開廣源，身上帶銀與兩張半燒紙。"
    - "其中一張可見『丙七，梁宅』。"
    - "馬成祿稱自己沒有殺人，留紙是為『留一條命』。"
    - "其稱丙七正常調度走總簿，帳外調度通常只可能由杜成／梁福下令；西門慶本人未必親自調車。"
    - "其稱柳生失蹤後，丙七車曾回廣源東庫，車底有血；血屬誰未證。"
    - "其稱車後來在灰水院被清洗。"
    - "負責清洗／駕駛線索指向陶萬春；陶萬春約兩年前已離廣源，已發新證人傳喚。"
  evidentiary_boundary:
    - "馬成祿供述需其他證據互證。"
    - "車底有血 ≠ 已證柳生死亡。"
```

---

# 12｜孫二虎與柳生「仍有氣」證詞

```yaml
SUN_ERHU_TESTIMONY:
  status: "WITNESS_TESTIMONY; PARTIALLY_CORROBORATING"
  confirmed_statement:
    - "高衙內命人毆打柳生後，孫二虎曾以為丙七車是來『收屍』。"
    - "一名瘦、跛／拖腳的男人從西門一側介入，說『還有氣，先別扔水。』"
    - "柳生之後被抬上藍篷丙七車。"
  current_effect:
    - "與西門慶此前『柳生被裝上藍篷丙七車、未見直接扔河』之供述形成部分互證。"
  unresolved:
    - "瘦跛男人身分。"
    - "柳生之後去哪裡。"
    - "柳生當時傷勢與最終生死。"
  anti_inference:
    - "不得因跛／拖腳直接認定為梁福。"
```

---

# 13｜陳氏女線：新自願來府女子與舊木箱

```yaml
CHEN_CASE_NEW_WITNESS:
  status: "NEW_VOLUNTARY_WITNESS_PENDING_ISOLATED_EXAMINATION"
  confirmed:
    - "一名女子主動到開封府，自稱陳氏女之嫂／姊嫂類親屬。"
    - "她稱陳氏女仍活著，但害怕親自來府。"
    - "她帶一只舊木箱，稱其中可證『五百兩到底買了什麼』。"
  next_procedure:
    - "應先隔離訊問、驗物、驗來源，再決定公開程度。"
  prohibited:
    - "不得現在就把木箱內容寫成已證明綁架、撤狀銀或高府犯罪。"
```

---

# 14｜西門慶當前合作／自救法位

```yaml
XIMEN_QING_CURRENT:
  status: "SERIOUS_ACCUSED_IN_CUSTODY; COOPERATING_FOR_NARROW_PROTECTION"
  confirmed:
    - "西門慶已開始以拆帳方式區分『自己做的』與『借自己路線發生但未必由自己直接下令的』。"
    - "對蘇清被控制一月等自己已難以翻掉的核心事實，不再採全面否認。"
    - "其以外部證據、暗帳、人名與線索換取自己仍有證據價值。"
  bao_narrow_protections:
    - "若其點名之無辜親屬遭威脅，官府可依法提供必要保護。"
    - "重要證據可做副本／分存。"
    - "即使其死亡，已入卷證據仍保留。"
  not_granted:
    - "免罪"
    - "保證刑度"
    - "保證不充軍／不死"
  player_assessment_only:
    - "白御行曾判斷西門慶至少可能重判至充軍以上；此為玩家判斷，不是官府判決。"
```

---

# 15｜蘇清當前對潘金蓮之目標與自由構想

```yaml
SUQING_CURRENT_GOALS:
  against_pan:
    - "目前不以把潘金蓮送入牢獄／奪掌櫃位作首要目標。"
    - "要查二十八日究竟值多少、為何其一月被用來結西門五千後帳、自己帳上為何沒有對應價值。"
    - "若潘當時根本無權處分她，則要追相應法律／帳務後果。"
    - "即使潘釋放她現有契約，蘇清也只會把這視為『桌錢／一部分結算』，不當成所有歷史帳已清。"

  future_professional_status:
    lifecycle: "PROPOSAL_IN_ROUTE_ONLY"
    concept:
      - "蘇清受貂蟬式自主方向啟發，考慮日後由自己持有／控制自己的契約或執業資格。"
      - "可選擇仍做風月性工作，但以『掛單』方式在不同場所營業。"
      - "觀止取得場地、抽成或管理權，不等於擁有／處分她本人。"
    core_statement:
      - "若原契解除後她仍留在觀止，她希望那代表『我留下，是因為我想留，不是因為一張紙說我走不了。』"
    not_final:
      - "尚未形成觀止正式制度。"
      - "尚未完成新契約。"
```

---

# 16｜蘇清 × 白御行：二十八日私人約仍未自動延長

```yaml
SUQING_BAI_PRIVATE_PACT:
  old_500_three_night_contract: "CLOSED_IN_HOT_V2.3"
  separate_28_day_pact:
    condition: "西門慶真正倒台／持久喪失舊有位置、錢權與路線後才觸發"
    current_trigger_status: "VERY_CLOSE_OR_LIKELY_BUT_NOT_SILENTLY_STARTED_BY_SAVE"
    note:
      - "西門慶已被羈押、法網重壓，但『真正倒台』需由可持續結果確認，不因戲劇氣氛自動起算。"
  day_29:
    status: "POSSIBLE_VOLUNTARY_REWARD_ONLY"
    condition: "若今夜謀局後來確實成為拔除西門慶之關鍵因果線，蘇清可能自願加一天。"
  82_days:
    status: "NOT_ACCEPTED"
    note: "白御行曾玩笑說八十二日；蘇清未同意。"
  future_wager:
    - "蘇清明示：待她先決定自己的法律／職業位置，再談白御行原本想押的關係賭局。"
```

---

# 17｜白御行：本輪有效自我陳述／玩家主權資料

```yaml
PLAYER_SELF_FACTS:
  betrayal_history:
    - "白御行明示自己曾被最愛的女人背叛；此為其個人過往有效玩家事實。"

  trust_philosophy:
    - "白御行認為有能力的屬下可以作為才能使用，但枕邊／親密女人在某些情況下較容易被敏感的人察覺態度變化。"
    - "他不主張親密女人不可能背叛。"

  self_pollution_statement:
    - "白御行表示自己常主動『做死』是因為好玩，不必自動解釋為精密戰略。"
    - "他也曾主張部分負面形象可降低外界對其能力之戒心；此仍是本人主張。"

  chunmei_desire:
    - "白御行明示：自己對龐春梅沒有性慾／追求欲，沒有特別原因。"
    - "不得把此狀態寫成龐春梅受辱、被拒絕後必有情緒，亦不得偷偷補出白御行其實有吸引。"

  shuying_assessment:
    - "白御行主觀認為：若真要排行，疏影可能是他最難追的女人，因為連見面都極難。"
    - "此為玩家評估，不等於疏影客觀最難攻略、也不等於她已對白御行發生感情事件。"
```

---

# 18｜疏影：本輪只成立「話題＋未知弦音」

```yaml
SHUYING_CURRENT:
  appearance: "NOT_CONFIRMED_PRESENT_IN_SCENE"
  confirmed:
    - "眾人討論白御行覺得最難追的女人時，話題轉到疏影。"
    - "紅娘氏、蘇清、李師師、阿麗婭等形成不同解讀：疏影的難不只是讓她動心，而是先取得真正被她允許見面／進場的資格。"
    - "眾人明示錢、身份、俗套風雅未必是有效槓桿。"
    - "李師師提醒：疏影不是等待男人破解規則的獎品；任何例外須由她自己成立。"
    - "討論後，樓上／觀止深處曾傳出一次極輕的弦音『錚』。"
  source_of_string_sound: "UNKNOWN"
  prohibited:
    - "不得自動宣判是疏影彈的。"
    - "不得自動宣判弦音是對白御行的回應、邀請或好感。"
    - "不得因被談論就強迫疏影下樓。"
```

---

# 19｜人物圖畫展示事件

```yaml
IMAGE_PROP_LOG:
  general_rule:
    - "以下均為白御行在內院拿出／展示的圖畫。"
    - "圖畫文案屬道具內容，不自動成為角色真實履歷或觀止官方宣傳。"

  aaliyah:
    file_prop: "阿莉婭.png"
    notable_text: "無垢祭品／她越乾淨，這世道就顯得越髒"
    reaction:
      - "阿麗婭認為畫中自己漂亮、像人在觀止卻尚未真正進來。"
      - "她不喜歡『祭品』定位，明示不想再被拿去換五千、平安、名聲或男人面子。"
      - "她表示若圖是白御行畫給她的，願意收；並說未來即使重新掛牌也不准拿這張招客。"
      - "最後可觀察為阿麗婭抱著畫並說『我的、不賣』；所有權法律轉移未由白御行另行明示。"

  hongniang_xiaocui:
    file_prop: "紅綠雙飛C.png"
    notable_text: "紅綠雙飛組"
    reaction:
      - "紅娘氏與小翠均看見圖畫；紅娘氏大笑調侃，小翠因被寫成『新露春情／會勾心』而害羞反駁。"
      - "圖畫不建立兩人新的成人交易、組合合約或服務義務。"

  zhang_lihua:
    file_prop: "張麗華C.png"
    notable_text: "貴妃醉酒，偷照人心"
    reaction:
      - "張麗華喜歡圖中自己不只剩身體，並說畫中女人不像會給人當妾。"
      - "她口頭表示想收畫、且不希望拿去給其他男人看。"

  shisanniang:
    file_prop: "十三娘.png"
    notable_text: "看透人心，才配談人情"
    reaction:
      - "十三娘認為眼神像自己在等別人犯蠢。"
      - "她表示這張可以掛；若有人因看畫就以為追得到她，正好可以讓對方來下注／花錢。"

  li_shishi:
    file_prop: "李師師.png"
    notable_text: "名動京華，笑眼藏風月"
    reaction:
      - "李師師說圖把她畫得太乖，像還沒遇見『睡完就穿褲子跑』的男人。"
      - "她拿走／持有圖畫，但明示白御行三日不得進她房之私人處罰不因此減免。"

  su_qing:
    file_prop: "蘇清C.png"
    notable_text: "她先選會贏的人，然後再決定自己站在哪裡"
    reaction:
      - "蘇清起初說不要，看到後改口『給我／我現在要了』。"
      - "她特別看畫中伸出的手，認同自己不像等別人來拉。"
      - "她後來評論：白御行畫不同女人時看的不是同一件東西；此為蘇清人物判斷。"

  rokujo:
    file_prop: "六條妃子.png"
    notable_text:
      - "六條御息所"
      - "一代高貴之女，淪為深宮之怨"
      - "我不是害怕失去你，我只是不能接受，你曾經擁有過我，卻忘記了那代表什麼。"
    pre_arrival_effect:
      - "該畫引發眾人對六條御息所、嫉妒、身分、關係與生靈傳說的高密度討論。"
```

---

# 20｜六條御息所：共鳴召喚成功之 ROUTE EVENT

```yaml
ROKUJO_ARRIVAL:
  event_type: "UNKNOWN_VISITOR_RESONANCE_ARRIVAL"
  lifecycle: "ROUTE_EVENT"
  baseline_pool_status: "NOT_ADDED_TO_CHARACTER_POOL"

  precondition:
    - "白御行展示六條御息所圖畫。"
    - "多名在場人物持續高密度談論六條、其源氏關係與危險性。"
    - "白御行明示觀止存在『談論某人密度到一定程度會自己召來』的現象；此與世界 Runtime 的共鳴召喚機制相容。"

  observable_arrival:
    - "觀止內院月門外環境出現不屬於汴梁的濕泥路與紅楓霧景。"
    - "一輛黑漆垂簾牛車／御車式車輛停在異路前。"
    - "車外未見正常車夫／牽引配置；具體機制未知。"
    - "車中女子先問『這是哪裡』，後下車／步入觀止。"
    - "女子身份經本人與後續對話確認為六條御息所。"

  summoning_boundary:
    - "召喚成功只代表到訪，不代表她歸屬白御行、觀止或任何男人。"
    - "不代表她有掛牌、服務、陪宿、性交、定居或常設角色義務。"
```

---

# 21｜六條御息所：原時代時間錨

```yaml
ROKUJO_ORIGIN_TIME:
  source: "六條本人對白御行提問之回答"
  confirmed_from_her_current_memory:
    - "她並非『剛從伊勢神宮回來』。"
    - "她剛經歷賀茂祭／車爭事件。"
    - "她的車隊與源氏正室葵上之車隊／從人發生衝突；其車被逼退、從者受辱。"
    - "她原本只是想遠遠看源氏一眼。"
    - "她提及女兒與伊勢有緣，也曾想離開京城，但其後更遠未來並非她當下記憶。"
  current_knowledge_limit_before_white_disclosure:
    - "她不知道自己完整後世故事。"
    - "她不知道後人怎樣評價自己。"
    - "她沒有一本可翻到結局的故事可用來重做當下選擇。"
  critical_director_rule:
    - "六條現在是『賀茂祭車爭後』的六條，不得偷塞後期自知生靈、女兒婚後、自己晚年等未經告知記憶。"
```

---

# 22｜六條御息所 × 白御行：後世故事與源氏核心情報

```yaml
ROKUJO_WHITE_INFORMATION_EXCHANGE:
  white_refuses:
    - "六條問後世如何記她；白御行明示不回答。"

  white_personal_judgment:
    - "白御行說六條對自己有致命吸引力：危險、高貴、自信但命運不佳。"
    - "白御行稱她是自己眼中的『可憐女人』。"
    - "白御行曾把其處境解讀為寡婦被情慾牽動、無法接受退出舞台、被光源氏式男人欺騙。"
  rokujo_response_to_pity:
    - "六條明示不喜歡被『可憐』把自己的主動錯誤與責任洗掉。"
    - "她承認自己有情慾、有不甘、有對身份／被渴望位置的需要，但拒絕被縮成『所有女人／寡婦都會犯的錯』。"
    - "她要求白御行不要用抽象的『女人』蓋掉她這個人。"

  white_genji_future_story_claims:
    source_status: "PLAYER_PROVIDED_FUTURE_NARRATIVE; HEARD_BY_ROKUJO; NOT_INDEPENDENTLY_VERIFIED_BY_HER"
    content:
      - "光源氏幼年喪母。"
      - "其父皇後來納一名與其母極相似、且與母族有親緣的皇妃。"
      - "白御行描述源氏幼年對該皇妃形成深層依戀，成年後受宮禁分離。"
      - "白御行說源氏曾強迫／侵犯該皇妃，並生下一名名義上被當作先帝皇子、後來即位之男子。"
      - "因此白御行把該帝描述為源氏生物學之子、名義上的弟弟。"
      - "白御行說源氏一生真正追逐的是該皇妃，而該皇妃最後為避其糾纏而出家。"
      - "白御行說紫姬長相也像該皇妃，源氏領養／養成紫姬亦有追逐影子之成分。"
      - "白御行進一步說六條吸引源氏，也可能因其氣質能勾起該原型。"
      - "白御行告知：六條之女秋好日後會嫁給那位被描述為源氏與皇妃所生、後來即位的皇帝。"
      - "白御行最後明示：源氏其實知道自己一直在追逐什麼，只是無法停下來。"

  rokujo_processing:
    - "六條把此資訊理解為：自己、葵上、紫姬等女人可能不是在爭同一個『唯一位置』，而是在面對一個男人永遠無法填滿的原型缺口。"
    - "她承認這使自己重新看待葵上，但不因此立刻不嫉妒、不喜歡葵上或放下源氏。"
    - "她明示即使聽懂，也可能仍想見源氏；知道結構不會立即消除感情。"
    - "她認為『知道後仍選』與『不知道時被牽著走』是不同法位。"

  anti_canonization:
    - "六條沒有在本夜宣告已放下源氏。"
    - "沒有宣告愛上白御行。"
    - "沒有宣告源氏之未來故事已被她驗證為客觀真相。"
```

---

# 23｜白御行對六條「權力／血統」判斷：保持爭議

```yaml
ROKUJO_MOTIVE_DISPUTE:
  white_claim:
    - "白御行判斷六條最深層其實想要權力／權勢。"
    - "白御行進一步判斷她未必真正愛源氏，而是被源氏血統、身分與她重新回舞台的可能性吸引。"

  rokujo_response:
    - "六條未接受為定論。"
    - "她承認身份、名聲、權勢、被人仰望對自己確實不是毫無意義。"
    - "她也承認東宮死後的身分退場與源氏是否來見自己，可能長期被她綁在一起。"
    - "但她明示：究竟是愛血統、愛權力、愛源氏本人，還是愛『重新被渴望／重新回舞台』的感覺，要由她自己分。"

  save_rule:
    - "不得把『六條其實不愛源氏只愛血統』寫進人物內心硬狀態。"
    - "可保存為白御行對她的強判斷，以及六條願意拿回去思考的問題。"
```

---

# 24｜白御行推薦趙受益給六條

```yaml
ROKUJO_ZHAO_INTRODUCTION:
  initiator: "白御行"
  player_statement:
    - "白御行明示自己認為『把人放到正確的位置就能解決問題』。"
    - "他認為自己不適合六條，但趙受益較適合。"
    - "他向六條推介趙受益的大宋皇家血脈、人品與條件，並以『可能很純也可能參了貓科動物』開玩笑。"

  zhao_response:
    - "趙受益沒有承認自己是六條候選、沒有接受白御行替他決定關係。"
    - "他明示：白御行推薦是白御行的事；六條要不要認識是六條的事；他自己是否進一步是自己的事。"
    - "趙不願跟不在場的光源氏比『誰更值得女人愛』。"

  rokujo_response:
    - "六條認為趙至少不像源氏那樣急著把自己的需要塞到剛見面的女人身上。"
    - "她曾直接問趙是否有妻室。"
    - "趙沒有正面回答婚姻狀態，而是先問她為何要知道；因此其妻室狀態在六條知情中仍為 UNKNOWN。"
    - "六條明示：趙『至少第一關比白御行過得好』之類戲謔評語，但不構成選定。"
```

---

# 25｜六條 × 趙受益：只成立一杯茶

```yaml
ROKUJO_ZHAO_RELATION:
  current_state: "FIRST_MEETING; MUTUAL_COURTESY; LOW_LEVEL_INTEREST_OR_CURIOSITY"
  confirmed:
    - "六條主動問趙：若不介意，今晚可以陪她喝一杯茶。"
    - "她立刻加明『只喝茶』，並說自己才剛聽完源氏一生的核心秘密，還沒有蠢到立刻換下一個男人。"
    - "趙受益接受『只喝茶』之條件。"
  not_established:
    - "戀愛"
    - "性同意"
    - "陪宿"
    - "私房進入"
    - "婚約／妾約"
    - "候選註冊"
    - "排他性"
  relation_shape:
    - "兩人都反對白御行替彼此直接宣布適合／成交。"
    - "六條對趙的克制、身分氣質與不急於自我推銷形成正面第一印象。"
    - "趙對六條維持禮貌與邊界，尚無明示愛慕。"
```

---

# 26｜六條入住安排：異時女客，不是姑娘

```yaml
ROKUJO_LODGING:
  manager_on_duty: "春梅／潘金蓮仍在開封府"
  guest_status: "異時女客"
  room: "觀止內院東偏廂乾淨空房"
  room_type:
    - "不是掛牌房"
    - "不臨主要客道"
    - "不是紅倌／清倌服務房"
  room_setup:
    - "重新換被褥。"
    - "撤掉過重的觀止姑娘房脂粉／熏香，先保持乾淨。"
    - "門可由六條自己從內閂上。"
    - "不派男性入房服務。"
    - "可留兩名女使在外間／門外，需要時才應。"
    - "六條明示不需要人在房內守著；保留外燈即可。"
  vehicle:
    - "六條原車／異路先不碰。"
    - "若明早仍存在，再處理；目前不得拆、拖、研究或宣判為永久門。"
  not_yet_confirmed:
    - "六條已正式進房睡下"
    - "六條會住幾夜"
    - "六條是否能／何時回原時代"
```

---

# 27｜六條今晚帳務：趙受益代付，不生人身權

```yaml
ROKUJO_ACCOUNT:
  payer: "趙受益"
  payer_consent: "EXPLICIT_LIMITED_CONSENT"
  covered_items:
    - "客房"
    - "茶食"
    - "必要衣物／日用"
    - "今晚因異時落地所需的一般女客雜用"
  zhao_explicit_boundary:
    - "只算替突然落在異世、沒有本朝錢幣的客人盡地主之誼。"
    - "不是買她。"
    - "不是養她。"
    - "不是白御行一句話便取得一位要負責的女人。"
  rokujo_response:
    - "六條起初表示若日後有自己的錢可以還。"
    - "趙建議不當欠款：今晚他請；若日後仍有機會同桌，可由六條再請一回。"
    - "六條接受此種社交互請法。"
  account_legal_effect:
    human_ownership: false
    prostitution_service_right: false
    sex_right: false
    room_entry_right: false
    companionship_right: false
    romance_right: false
    debt_bondage: false
  current_joke_only:
    - "紅娘氏稱白御行像媒婆／老鴇。"
    - "白御行反駁『人家沒成交，不算賣』。"
    - "眾人遂以『推銷未遂／熱心媒婆』玩笑；不具契約法位。"
```

---

# 28｜李師師：三日房禁仍有效

```yaml
LI_SHISHI_ROOM_BAN:
  status: "ACTIVE_PRIVATE_BOUNDARY"
  origin:
    - "白御行先前在師師私人帳未清時，被禁房兩日。"
    - "白御行隔院喊『那我去瓶兒那邊』後，李師師把兩日加為三日。"
  current_event:
    - "六條到觀止後，白御行當眾直接問李師師：今晚要不要陪我睡。"
    - "李師師直接拒絕『不要』。"
    - "她再次明示三日禁房一天不能少。"
    - "她說禁期過後再看她當日有沒有興致；不是預約性同意。"
  invariant:
    - "三日禁房屬李師師當前有效私人邊界。"
    - "不得因白御行公開邀請、六條來訪、圖畫贈送或玩笑而縮短。"
```

---

# 29｜六條已知與未知資訊邊界

```yaml
ROKUJO_KNOWLEDGE_SCOPE:
  knows_now:
    - "觀止可使不同時代的人相遇；此為白御行告知並由自身穿越經驗部分印證。"
    - "白御行聽過她的未來故事，但拒絕直接告訴她後世如何評價她。"
    - "白御行提供一套關於源氏核心欲望、皇妃、紫姬與秋好未來婚配的敘述。"
    - "白御行自稱不適合她，並推薦趙受益。"
    - "趙受益被白御行描述為大宋皇家血脈；趙本人未完整公開更高身份。"
    - "白御行與李師師至少有足以公開問『今晚要不要陪睡』與三日禁房的私人／性關係史。"
    - "白御行此前也曾推薦趙受益給阿麗婭；六條在眾人笑談中得知這一點。"

  does_not_know_without_new_source:
    - "紅娘氏與趙受益曾完成成人交易之確切歷史。"
    - "趙受益真正更高皇家身份細節。"
    - "白御行與所有其他女人的完整性史／契約史。"
    - "她未來是否化生靈、葵上死亡等全部後世細節；此前眾人談過不等於她已聽見。"
    - "自己最終後世評價。"
    - "自己何時／是否能返回原時代。"
```

---

# 30｜人物主權與關係防收斂警告

```yaml
RELATIONSHIP_INVARIANTS:
  rokujo:
    - "六條不是因被召喚就成白御行獎品。"
    - "六條沒有接受『妳其實只愛權勢／血統』為固定人格答案。"
    - "六條對趙只有初次認識與茶約，不得跳成心動、戀愛、陪宿或婚配。"
    - "六條仍可能對源氏有慾望、依戀、嫉妒與不甘；一晚資訊不能洗掉她的時間成本。"
    - "六條對葵上的妒意沒有因知道源氏原型結構就自動消失。"

  zhao:
    - "趙受益付房帳不等於取得六條任何權利。"
    - "趙沒有答應阿麗婭或六條的候選／競標。"
    - "不得因白御行兩度推薦就把趙寫成觀止公用男伴。"

  aaliyah:
    - "阿麗婭今晚不重新掛牌。"
    - "其一期婚／篩選競標仍為構想。"
    - "不得因五千舊權利弱化就把她自動轉成紅倌或自由妓女。"

  li_shishi:
    - "三日禁房有效。"
    - "性邀請被拒絕後不得改寫成欲拒還迎。"

  su_qing:
    - "其自由／職業制度仍未定。"
    - "二十八日私人約不得因西門慶看似完蛋就偷算第一天。"

  shuying:
    - "只有未知弦音，無進場、無邀請、無好感確認。"

  chunmei:
    - "白御行對她無性慾是玩家硬事實；不得創造反向吸引。"
```

---

# 31｜法律戰防收斂警告

```yaml
LEGAL_INVARIANTS_V2_5:
  - "高衙內承認暴力命令 ≠ 已證殺害柳生。"
  - "柳生被裝上丙七且當時可能仍有氣 ≠ 已證後來存活。"
  - "丙七＝車牌／車號；不得再當個人身份牌。"
  - "同一車、同一帳碼、同一日期仍需因果互證。"
  - "潘金蓮承認蘇清抵五千後帳 ≠ 已證她授權西門暴力抓人。"
  - "西門慶說自己如何理解『西門自取』＝供述，不是自動客觀真相。"
  - "蘇清後來自願入妓籍 ≠ 前二十八日合法。"
  - "前二十八日若違法 ≠ 後來自願申請當然失效。"
  - "阿麗婭舊五千出閣權未完成且被替代結算 ≠ 阿麗婭必須重新掛牌。"
  - "陳氏親屬帶來木箱 ≠ 五百兩用途已證。"
  - "母簿仍未找到，但官府已有足夠基礎繼續拘提、封存與證人程序。"
  - "不得把所有支線重新拖回『先找到母簿才可辦人』。"
```

---

# 32｜當前重要未決事項

```yaml
OPEN_HOOKS:
  legal_high_priority:
    - "陳氏女親屬木箱內實物與『五百兩買了什麼』究竟為何。"
    - "陶萬春是否到案、能否互證丙七血跡／清洗事件。"
    - "瘦跛男人身份與柳生離開丙七後的去向。"
    - "杜成下落。"
    - "梁福下落、身分是涉案者或證人比例。"
    - "廣源母簿位置。"
    - "梁宅狹條紙真偽與碼義。"
    - "高衙內、家僕、西門慶、廣源間對柳生案的責任切割。"
    - "潘金蓮在『蘇清一月抵五千後帳』中的契約／帳務責任。"
    - "蘇清前二十八日的合法性與損害計算。"
    - "蘇清後來自願妓籍文件與其原私人契約如何對接。"
    - "阿麗婭舊五千拍賣在最終判定中如何正式註銷／失效。"

  relationship_and_status:
    - "六條明早或稍後是否仍留觀止、是否要求回原時代。"
    - "紅楓異路與牛車是否仍存在。"
    - "六條與趙受益的茶是否繼續、是否只停於社交。"
    - "六條如何處理白御行告知的未來源氏資訊；不得替她預先選擇回去後行動。"
    - "白御行是否還會接近六條；其已口頭說『自己不適合』，不等於永久放棄或契約禁止。"
    - "阿麗婭何時／是否重新申請首次出閣。"
    - "阿麗婭未來制度構想是否被觀止／官府採納。"
    - "蘇清最終職業身分與白御行二十八日私人約觸發日。"
    - "李師師三日禁房之實際倒數與私人帳修復。"
    - "疏影弦音來源。"
    - "六條圖畫與其他人物圖畫最終由誰保存；不得以本 SAVE 自動完成贈與。"
```

---

# 33｜下一導演接關警告

```yaml
CONTINUATION_GUARD:
  must_preserve:
    - "目前已進 HOT SAVE，停止戲劇性擴寫；下一輪若玩家說繼續，再解除 HOLD。"
    - "白御行台詞、行動、進房、付款、性邀請、關係承諾與內心仍由玩家控制。"
    - "六條今晚只是異時女客；不要把她寫成掛牌姑娘、紅倌、白御行女人或趙受益女人。"
    - "六條房間已安排但未確認她已入睡；下一幕可由世界自然推進，但不能替她或玩家跳過需要作答的重要選擇。"
    - "趙受益與六條只答應喝茶；不要收斂成戀愛線成功。"
    - "六條沒有被白御行『治好』源氏情結；她只是得到新資訊。"
    - "六條對『權力／血統才是核心』保持爭議，不得當成人物卡真相。"
    - "六條原時代時間固定在賀茂祭車爭後；除白御行已告知內容外，不得讓她知道後期事件。"
    - "六條不知道紅娘氏與趙受益的舊成人交易。"
    - "潘金蓮仍在開封府；若要回觀止需有移動事件。"
    - "阿麗婭今晚不掛牌。"
    - "李師師三日房禁仍生效。"
    - "疏影未進場；弦音來源 UNKNOWN。"
    - "龐春梅對白御行無性吸引是玩家自我狀態，不得反向強拉戀愛。"
    - "法律線已進法網擴張階段，下一次切回不得重新鬼打牆只找單一母簿。"
    - "高衙內、潘金蓮、西門慶均未因目前證據被導演直接跳到終局刑判。"
  no_forced_choice_menu: true
```

---

# 34｜本 HOT 的一句接關摘要

> **開封府已從查線索跨進拘提、封存與廣泛證人法網；五千後算進一步坐實「阿麗婭掛名、蘇清一月被西門接受為替代結算」，但潘是否授權暴力、蘇清前二十八日與後來自願入妓籍仍須分軸裁判。阿麗婭回觀止後沒有立刻重新掛牌，而開始構想由自己篩選首次二十八日對象的「一期婚」。同夜內院因高密度談論六條御息所而成功引來未知來客：賀茂祭車爭後的六條本人進入觀止，聽見白御行關於光源氏核心欲望與未來宮闈的敘述，未被「可憐／只愛權勢」的解讀洗成人設；白御行又把趙受益推薦給她。六條與趙目前只同意喝一杯茶，六條以異時女客暫住東偏廂，趙代付今晚客費而不生任何人身、性、陪宿或關係權利。此刻無人成交。**

<!-- SOURCE_HOT_V2_5_END -->

<!-- INHERITED_MASTER_V4_2_END -->


---

# APPENDIX B｜固化來源全文：觀止青樓_白御行線_HOT_SAVE_V2.6_槐月二十一日破曉_京師軍械案收網_觀止民事戰重啟_許慎言七十二小時按摩券版.md

> **法位：E84–E92 細節追溯來源。** 此 HOT 內的 CURRENT_SCENE／HOLD 只代表當時快照；不得覆寫本 MASTER 截止或 V3.5–V3.7 疊加層。若原 HOT 內某個標成 YAML 的區塊本身語法不合法，本 MASTER 只把該 fence 改標為 text 隔離，內容原文不改，避免來源語法缺陷破壞 MASTER 解析。

<!-- PROMOTED_HOT_SOURCE_BEGIN: 觀止青樓_白御行線_HOT_SAVE_V2.6_槐月二十一日破曉_京師軍械案收網_觀止民事戰重啟_許慎言七十二小時按摩券版.md -->
# 觀止青樓｜白御行線 HOT SAVE V2.6
## 理火三年槐月二十一日破曉｜京師軍械案收網 × 朝廷權臣政治處置 × 觀止核心民事戰重啟 × 許慎言七十二小時按摩券版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V2_6_HUAI21_DAWN_MILITARY_NET_CLOSURE_GUANZHI_CIVIL_REOPEN"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V2.6"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime:
    - "GUANZHI_QINGLOU_V10_0"
    - "GUANZHI_QINGLOU_V10_1_V10_2_PATCH_WHEN_APPLICABLE"
  story_time_span:
    start: "理火三年槐月二十日深夜／HOT V2.5 後"
    current: "理火三年槐月二十一日破曉前後；北路已見天色泛白"
    exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AT_GUANZHI_AFTER_CIVIL_CASE_REOPEN_AND_XU_SHENYAN_MASSAGE_START"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V2.5_槐月二十日深夜_開封法網擴張_阿麗婭重定義與六條御息所來訪版.md"
  previous_hot_sha256: "a2107c0df322779ea1ed0f74a59502c63ea52594fded2a295a258f6e68997083"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"
  current_primary_story_domain: "觀止核心案件／民事與關係場"
  national_case_status: "TRANSFERRED_OUT_OF_PRIMARY_CAMERA_TO_KAIFENG_AND_IMPERIAL_POLITICAL_HANDLING"
```

---

# 0｜提交法位、來源與本輪污染修正

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V2.5_槐月二十日深夜_開封法網擴張_阿麗婭重定義與六條御息所來訪版.md"
    role: "本檔直接前置 HOT；V2.5 以前全部有效事件繼承"
  legal_core_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V2.4_槐月二十日深夜_風滿樓公案與五千後算開冊版.md"
    role: "許慎言法律援助、蘇清正式代理、柳生／高衙內、廣源、西門暗櫃、五千後算之硬來源"
  route_conversation_commit:
    role: "HOT V2.5 後至本次 HOT SAVE 命令之直接劇情與玩家明示校正"
  player_corrections:
    - "風滿樓三大出資金主固定為白御行／定陶、趙受益、沈萬三；出資不取得案情定調權。"
    - "潘金蓮不在觀止時，春梅、李瓶兒仍是觀止掌櫃；十三娘可代傳話、主持場面、統合消息，但不得動用掌櫃定價、開房、免單、調姑娘、改帳等權限。"
    - "許慎言為定陶商會出資請來之主要狀師，免費替西門氏相關受欺無資者寫狀、打官司；非臨時功能性路人。"
    - "蘇清已正式委託許慎言作為自己的代表律師，追查自身案件並處理潘金蓮相關民事／帳務責任。"
    - "白御行本輪正式購買『七十二小時按摩體驗券』贈許慎言；取代先前舊檔『七十二次按摩券』之路線版本。"
    - "青禾為新創觀止技師；與許慎言之關聯為按摩恢復／工作支援，不自動升格感情、性、陪宿或法律共同體。"

DIRECTOR_CORRECTION:
  issue: "前一段生成曾因軍械／朝廷大案注意力吸附，把許慎言、青禾、蘇清民事、廣源、高衙內／柳生等活躍故事鍊誤壓成背景或近似 CLOSED。"
  correction:
    - "此為導演讀取／收斂污染，不是世界事實。"
    - "不得將污染輸出倒灌成 SAVE。"
    - "本檔恢復觀止核心故事鍊法位。"
    - "不得宣稱理火底層 Runtime 真實掉線；只記錄文件級／敘事治理狀態曾失準並已校正。"
```

---

# 1｜當前鏡頭與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年槐月二十一日"
  time: "破曉前後；精確時刻未定"
  primary_location: "觀止青樓／前堂與後堂並行"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  player:
    name: "白御行"
    current_position: "觀止前堂附近"
    last_confirmed_action:
      - "正式以自己／定陶一方付款，購買七十二小時按摩體驗券贈許慎言。"
    no_new_player_action_after_save_command: true

  direct_resume_point:
    - "京師軍械／御前營造／權臣大案已由觀止鏡頭收網，刑名交開封府包拯，政治處置交皇帝，不再由觀止無限擴案。"
    - "春梅已將蘇清相關舊帳搬出，觀止正式把鏡頭拉回蘇清／潘金蓮之民事與帳務戰。"
    - "許慎言已在本輪把蘇清、西門慶、廣源、柳生四組案卷重新列為觀止核心工作；隨後由青禾帶往後堂開始第一段一個時辰按摩。"
    - "七十二小時體驗券為分次扣時之服務額度；不是一次連續按摩，也不產生性、陪宿、感情或人物所有權。"
    - "潘金蓮尚未在本輪被實際演出返回觀止；玩家已明示『觀止掌櫃該放了／潘金蓮、西門慶才是故事核心』之方向，但不得偷補她已回到前堂。"
```

---

# 2｜觀止治理權：三金主、掌櫃與十三娘

```yaml
GUANZHI_GOVERNANCE_CURRENT:
  fengmanlou_three_sponsors:
    - "白御行／定陶一份"
    - "趙受益一份"
    - "沈萬三一份"
  sponsor_limit:
    - "出資僅支持風滿樓場地、人力、公開轉述與運作。"
    - "不購買判決、不取得人物主權、不取得觀止掌櫃權。"

  active_managers_when_pan_absent:
    - "春梅"
    - "李瓶兒"
  manager_authority_examples:
    - "定價與收費"
    - "房間／帳務／服務安排"
    - "是否免單或掛帳"
    - "調姑娘／技師與服務資源"
    - "觀止財物與證物場內保管程序"
  shisanniang_role:
    permitted:
      - "代傳話"
      - "主持現場"
      - "整合消息"
      - "替掌櫃擋場面／維持秩序"
      - "案件資料之場面整理"
    forbidden_without_manager_authorization:
      - "自行定價"
      - "自行免單"
      - "自行開房"
      - "自行調姑娘／技師"
      - "自行修改觀止帳簿"
      - "以代理主持身分取得潘／春梅／瓶兒的掌櫃權"
```

---

# 3｜觀止規矩：皇帝亦照價付費

```yaml
GUANZHI_EQUAL_PRICE_EVENT:
  confirmed:
    - "趙受益先前已是風滿樓三金主之一；此出資與六條御息所女客房費為不同帳。"
    - "趙受益另行代付六條御息所今晚客房、茶食與必要女客開銷；不因此取得六條任何人身、服務、陪宿、性、關係或契約權利。"
    - "白御行故意以『仁宗皇剛付了一夜房錢』歪說此事作笑梗；趙受益當場校正那是六條房錢。"
    - "趙桓、趙佶到觀止後，春梅、李瓶兒依觀止規矩收取其席位／茶水等實際消費；皇帝、太上皇不因身分免單。"
    - "姑娘／服務是否成立仍需服務者本人願意；付錢不等於取得人。"
  legal_or_political_meaning:
    - "白御行藉此公開刺出『天子犯法與庶民同罪』之政治問題。"
    - "趙受益拒絕把自己自封為千古唯一公正皇帝；其明示真正考驗是案子查到自己人時是否仍允許依法往下查。"
```

---

# 4｜趙氏三帝到觀止：身分與政治法位

```yaml
ZHAO_IMPERIAL_ROUTE_EVENT:
  status: "ROUTE_EVENT_IN_CURRENT_MIXED_TIMELINE"
  confirmed_present_during_fengmanlou:
    renzong: "趙受益"
    current_emperor_in_route: "趙桓"
    retired_emperor_in_route: "趙佶"
  timeline_note:
    - "本線時間線已明示高度混合／錯位；此為玩家線 ROUTE EVENT，不回寫一般歷史基線。"
  key_events:
    - "宮中先派內侍確認趙受益身份並請其入宮／移駕；趙受益拒絕讓觀止因『護駕』被禁軍清場。"
    - "趙受益明示觀止不是皇家場地；禁軍可守街口，不得以保護之名替觀止逐客。"
    - "趙桓、趙佶其後親至觀止見趙受益。"
    - "趙受益要求後世趙氏子孫若要見自己，須在百姓仍可在場的觀止規矩下坐下，而非先把百姓清走。"
  player_future_information_to_zhao:
    - "白御行告知趙受益：其後世名聲在趙氏皇帝中極響；此為白御行提供之後世評價，不自動等於當夜所有人均知。"
    - "白御行先前亦向趙受益提供『不到一百年』、燕雲收復、後世宋江詩句等未來資訊；均保存為玩家提供之未來知識，不倒灌為當代已驗證事實。"
```

---

# 5｜京師軍械案：製造、入庫、調撥與三十二套缺額

```yaml
MILITARY_EQUIPMENT_CASE_CORE:
  status: "NATIONAL_LEVEL_CASE_HANDOFF_IN_PROGRESS"
  official_or_route_records:
    - "風滿樓／開封府查案方向由殿帥府、郝成、陸謙假保結，進一步上溯至官坊製造、旬課、入庫、軍中調撥與實收。"
    - "本輪出現一份查帳抄報：北作坊旬課七百六十、入庫七百六十、殿帥府領用五百四十、軍中實收五百零八。"
    - "此抄報形成三十二套成套軍械缺額；未見正常報損、轉撥、戰損、庫火或被劫記錄。"
    - "高衙內城外私莊找到其中一套，內記與北伐軍前轉運相關。"
  legal_boundary:
    - "三十二套缺額、個別實物與帳務交叉已形成強線索；不得把所有高層人物自動寫成共同主謀。"
    - "製造、入庫、領用三本帳對上而軍中實收短缺，支持問題可能發生於正式領用後至軍中實收前；仍需逐筆核實。"
```

---

# 6｜梁山線：真線索、可疑引導與不得提前收斂

```yaml
LIANGSHAN_LINE:
  confirmed_clues:
    - "此前出現濟州三船／鹽不入城／泊外換人等抄帳線索。"
    - "兩船最後官面記錄曾指向梁山泊外水口附近。"
    - "南逃騎手攜半燒紙，紙上可見『林沖』『梁山』；騎手後被抓，身份為拿錢送信者孫二，非陸謙。"
    - "半燒紙後被辨出來自舊帳紙，其背面另殘留酒、城東、御前等字樣。"
  counter_hypothesis:
    - "沈萬三、趙受益等已提出：梁山可能是實際路線，也可能是有人特意留下、引開封府北看的答案。"
  prohibition:
    - "不得因出現梁山泊地名即判梁山好漢參與軍械走私。"
    - "不得把白御行漢末定陶線之『梁山島／大野澤』與本宋線梁山泊混同。"
```

---

# 7｜郝成、林沖與陸謙：假保結與軍籍能力

```yaml
HAO_LIN_LU_LINE:
  haocheng:
    - "郝成為前軍人，後被重新登記為水戶／船路相關人物。"
    - "官冊曾出現林沖作其保人／擔保者。"
  linchong:
    - "林沖本人到風滿樓否認替郝成作保，認定有人拿其名頭洗籍。"
    - "林沖回憶陸謙曾與其飲酒並詢問其保結印／私印平日存放位置。"
  luqian:
    - "陸謙為林沖舊識，任殿帥府虞候。"
    - "官冊把郝成舊軍籍／器械庫外差等線與陸謙職務圈接上。"
    - "御前營造外料院可疑三日門籍中，陸謙以『驗車』名義進過料場。"
    - "其後追查高府急信東線，在城東私宅實際找到陸謙並將其拘提。"
    - "陸謙處兩箱之一有六套與失蹤北伐軍器同批內記之軍械；另一箱為以廢鐵、營造耗損、舊械回收、軍前折損等名目記錄的小帳。"
  effect:
    - "陸謙已從單純嫌疑提升為持有可疑軍械／帳物之被拘提重要人物。"
    - "仍不得因其被抓自動補成唯一主謀或高俅所有行動皆由其執行。"
```

---

# 8｜御前營造、朱勔與艮嶽外料院

```yaml
IMPERIAL_CONSTRUCTION_LINE:
  confirmed_route_events:
    - "開封府追到一艘酒船停於城東私泊，泊口掛『御前營造』名義。"
    - "船上目前查得確為酒，未在船體夾艙找到軍械；碼頭腳夫證稱其曾搬過外觀近似酒貨但重量像鐵之重箱。"
    - "城東私泊相關管事線出現朱勔。"
    - "御前營造料場帳冊曾被人縱火／先撕特定三頁後燒，撕頁日期與酒船、舊農具夜放前後重合。"
    - "料場小庫房名目為舊索、廢木、破車具；清點後部分鐵箍、車軸等數量不符。"
    - "碼頭腳夫回憶趕車人曾罵『艮嶽南邊那道門夜裡又不開』。"
    - "門籍顯示南料門可疑夜晚記為未啟；另有臨時改道條：南料門夜閉，車輛改東南便道、暫泊外料院。"
    - "因此可疑物流不必進入艮嶽本體，可能在牆外御前營造外料院完成中轉。"
  current_hypothesis_not_fact:
    - "御前營造／花石綱可能被用作重貨免驗或低查驗之物流外殼。"
    - "朱勔本人是否直接參與軍械盜賣，仍未由本輪硬證據證成。"
```

---

# 9｜生辰綱浮現：大名府、蔡京、楊志與黃泥岡

```yaml
SHENGCHENGANG_LINE:
  emergence:
    - "由『綱運／官方重貨／沿途不易開箱』之結構討論，浮現大名府賀蔡京生辰禮之生辰綱。"
    - "大名府文移曾要求沿途關津不得留難、遇渡優先、夜禁可持文放行。"
    - "押送使被確認為楊志。"
    - "觀止此前有數名外地客曾詢問棗價及是否收棗；未留名、未住宿、未成交，不得自動認成晁蓋等特定人物。"
  gaofu_connection:
    - "高府老僕供稱高俅離府前命其燒一只沉重箱子；老僕未燒，藏於馬廄草料下。"
    - "箱內有軍中關防空白牒三十七張、殿帥府舊印兩方、各州軍籍樣式十二種、林沖私印摹樣一張。"
    - "同箱另有由東京通往大名府之路圖，旁註『賀禮路』。"
  northern_intercept:
    - "白御行判斷不能等待大隊人馬，要求趙佶交皇家令牌給林沖。"
    - "趙佶本人同意並交出可供沿途官差、驛站驗符之御前金牌；此牌不是兵符，也不把林沖變成欽差。"
    - "林沖持牌獨立快馬北上，魯智深同行負責保護；林沖取得現場自主判斷權。"
    - "林沖與楊志相識；北路實際接上楊志及生辰綱。"
    - "楊志供稱途中曾有人持御前營造文牒與大名府文書要求重封；其未換箱，但一箱曾翻倒後重新捆綁。"
    - "該箱底層被撬開後發現殿帥府新式關防、空白軍籍及一封無署名短札。"
    - "短札內容：若入京前聞高、蔡有變，棄綱於黃泥岡，餘物另送。"
    - "林沖決定不走黃泥岡、整支綱保留原封並改道；若再有人要求換箱、改封、毀貨或殺押運者，可依現場判斷扣人。"
    - "楊志願作證。"
  forest_observers:
    - "林間曾有人以鳥叫等方式觀察，但身份未知。"
    - "不得自動判為梁山／晁蓋／吳用等人。"
```

---

# 10｜對手拆招：隔離決斷者與東京多點反制

```yaml
COUNTERMOVE_PATTERN:
  observed:
    - "在觀止查到艮嶽南門／外料院等線時，宮中來使要求趙桓還宮、趙佶回龍德宮、趙受益移駕。"
    - "同時開封府收到中書牒，要求停止高衙內、軍器、御前營造相關案，移樞密院／御前司會同另審。"
    - "包拯未依此停案。"
    - "開封府分別去高府、蔡府找人時，高俅、蔡京均已提前離府。"
  interpretation:
    - "沈萬三等判斷此組動作具有將皇帝、太上皇、仁宗與包拯分開、把決斷點放回各制度盒子的效果。"
    - "『對面有高手／有人一直看查案進度』為高度合理推論，但具體總指揮者仍 UNKNOWN。"
```

---

# 11｜白御行之『保護家人／保管財物』策略

```yaml
GAO_CAI_RESIDENCE_CONTROL:
  player_instruction:
    - "白御行提出：派禁軍入高、蔡二府『保護』兩位重臣家人安全，集中府中人員；並『保管』府中財物，防止遭竊或搬移。"
  imperial_execution:
    - "趙桓在趙受益校正後下令執行；法位不是先行定罪或任意抄家。"
    - "家眷不得作人質、不得刑訊、日常飲食醫藥不得斷。"
    - "財物、帳冊、書契、印信、箱籠須造冊、封存，多方見證，不得任意侵吞。"
  gaofu_result:
    - "高府順利被控制；高俅與高衙內當時不在。"
    - "老僕主動供出未燒之重箱，形成軍籍偽造工具與賀禮路圖之硬線。"
  caifu_result:
    - "蔡府女眷、僕役與庫房仍在，但帳房先生三人、門客七人、兩名掌事及一批近月書札已提前不在。"
    - "蔡京另一處外宅後院井旁有大量新灰，疑有文書焚燒；仍需實物鑑定。"
```

---

# 12｜高俅與蔡京：收網結果與法位分離

```yaml
GAO_QIU:
  latest_route_state:
    - "高俅最後在一處禁軍別營被找到。"
    - "其身邊有十餘名親兵及一紙調兵文書；因趙桓此前已有未奉御前新命不得擅調之命，該調兵未形成有效擴張。"
    - "高俅被帶往開封府／官府程序。"
  not_final:
    - "尚未在本 HOT 由包拯完成最終刑事判決。"

CAI_JING:
  latest_route_state:
    - "蔡京最後在寺院被找到，未武力抗拒，表示願赴開封府。"
    - "其政治策略是切割各權力線：朱勔／花石綱、梁中書／生辰綱、高俅／軍務、楊戩／內廷等各歸各線；蔡京不主動替他們背書。"
    - "白御行提出政治處置：既然蔡京主要想自保，可讓其真正告老還鄉；自願捐出九成家產作『北伐基金』；交出掌握之帳、名單、文書與棋盤資訊；若無刻意隱瞞，保其性命與安全下庄。"
    - "同時設協議取消條款：若日後查出蔡京刻意藏匿重大事項，則安全下庄協議失效，重新追查到底。"
    - "劇情中蔡京接受此政治交易方向。"
  critical_boundary:
    - "此為政治退出／合作協議，不是包拯刑事無罪判決。"
    - "刑名與具體犯罪認定仍歸開封府；政治條件不得抹除已證成之個別刑責。"
    - "九成家產為政治協議中之自願捐出／退場條件，不應被後續偷改成已經完成全部清點入庫，除非另有實際交付事件。"
```

---

# 13｜梁師成、楊戩、朱勔：仍屬未完全結算的國家線

```yaml
OTHER_HIGH_OFFICIALS:
  liang_shicheng:
    source: "西門慶供述及後續中介線"
    state: "IMPORTANT_UNRESOLVED; NOT_CONVICTED_IN_THIS_HOT"
  yang_jian:
    source: "夜放／御前等文牒簽驗線"
    state: "DOCUMENT_AUTHENTICITY_AND_AUTHORITY_NEED_FINAL_CHECK"
  zhu_mian:
    source: "御前營造、花石綱、城東私泊／外料院線"
    state: "IMPORTANT_UNRESOLVED; DIRECT_CRIMINAL_ROLE_NOT_YET_PROVEN"
  camera_rule:
    - "以上三線移交國家案，不再要求觀止主鏡頭每輪追進。"
```

---

# 14｜軍械案收網之結構結論：不是單一主謀預設

```yaml
NETWORK_MODEL_CURRENT:
  hard_or_strongly_supported_functions:
    - "軍方／殿帥府接口可提供軍籍、關防、領用與人事接點。"
    - "御前營造／官面綱運可提供車、船、料場、文牒與低查驗物流。"
    - "帳務端可把實物流失包成廢鐵、營造耗損、舊械回收、軍前折損。"
    - "商路與地方放行可承接重貨轉運。"
  current_best_structure:
    - "更像不同位置的人各自出售／濫用自己掌握的一段權力接口，而非已證明存在單一最高主謀指揮一切。"
  prohibition:
    - "不得把所有軍械、廣源、梁山、生辰綱、花石綱、蔡京、高俅、梁師成、楊戩、朱勔硬縮成一個總反派。"
```

---

# 15｜朝廷大案鏡頭正式退出觀止主線

```yaml
NATIONAL_CASE_CAMERA_EXIT:
  player_direction:
    - "白御行明示：大事情不管觀止的事了，法律交包拯，政治交皇帝。"
    - "故事不得再因國家案新名字不斷膨脹，吞掉潘金蓮、西門慶與觀止自身核心。"
  current_division:
    criminal_and_evidence: "包拯／開封府"
    imperial_political_disposition: "趙桓等當朝皇權；趙受益提供祖宗級政治判斷但不自動取得當朝法定皇權"
    guanzhi: "回到自身帳、人物、民事、關係與商業案件"
```

---

# 16｜西門慶：二十八日重責任仍是核心，不得被合作洗掉

```yaml
XIMENQING_CORE_CRIMINAL_AXIS:
  inherited_hard_history_from_v2_5:
    - "蘇清當年實際被西門府家奴以暴力拖入偏院。"
    - "西門慶對蘇清以死亡／折磨等方式施壓，實際控制其二十八日。"
    - "西門慶實際取得蘇清、暴力拖拽、囚禁、威脅等責任軸已成立為重大查案核心。"
    - "可能的性強迫／性侵責任須由法庭與證據完成刑名證成；不得由導演先偷判全部具體罪名。"
  later_status_separation:
    - "蘇清二十八日後回觀止，再由本人自願申請入妓籍／紅倌方向；此後來選擇不能回溯洗白前二十八日。"
  player_legal_view:
    - "白御行明示判斷：若『抓良家、近二十八天性侵／強迫性行為』被證成，西門慶至少應面臨充軍等重刑。"
    - "此為白御行的法律／政治判斷，不等同包拯已宣判。"
  anti_laundering:
    - "西門慶可合作、供出證據、以暗櫃或口供自救，但合作只能影響後續處置，不能讓已成立或將證成之蘇清二十八日重大刑責憑空消失。"
```

---

# 17｜蘇清 vs 潘金蓮：刑事分軸後，民事正式開戰

```yaml
SUQING_PAN_CIVIL_CASE:
  status: "ACTIVE_CORE_GUANZHI_CASE"
  representative_lawyer: "許慎言"
  client: "蘇清"
  funding: "白御行／定陶商會買單；不以勝訴為條件"
  confirmed_scope:
    - "完整後堂結算"
    - "蘇清一月自身帳項"
    - "蘇清正式賣身契／後來入妓籍之文書效力分軸"
    - "潘金蓮把『蘇清一月』納入五千後帳時，是否具有該種帳務／派遣／利益處分權"
    - "蘇清一月被作為替代利益時，實際價值、收益歸屬、返還／賠償與損害問題"
  current_hard_evidence:
    - "《五千後算》存在並已由開封府見證開冊。"
    - "潘金蓮承認其中涉及蘇清『作掃興之補』『不另折銀』等安排來自其帳法／安排。"
    - "潘筆跡殘條存在：『蘇清一月，抵五千後帳』『人不轉契』『西門自取』『月滿還樓』。"
    - "西門慶與潘金蓮均承認蘇清一月被接受為五千替代結算之一部分。"
  criminal_civil_separation:
    - "潘金蓮刑事上是否知道／授權暴力、囚禁、性強迫，與民事上是否有權拿蘇清一月作替代利益，必須分開。"
    - "即使潘刑事未被判為西門慶暴力共犯，也不自動排除其民事返還、賠償、帳務或越權責任。"
  current_scene:
    - "春梅已把蘇清相關舊帳真正搬出，民事第一輪正式開桌。"
```

---

# 18｜許慎言：恢復 principal lawyer 法位

```yaml
XU_SHENYAN:
  identity: "定陶商會出資聘請之主要狀師／觀止法律援助主力"
  legal_aid_role:
    - "西門氏相關訟事"
    - "受欺無資者免費代書接狀"
    - "實事實寫、傳聞另記"
    - "不承諾勝訴、不把傳聞包裝成證據"
  suqing_mandate:
    - "蘇清本人已正式委託許慎言。"
    - "許慎言須先查資料，再決定合法攻點；不是替玩家預先宣布潘金蓮敗訴。"
  current_four_core_files_reopened:
    - "蘇清／潘金蓮民事"
    - "西門慶刑民事責任與受害者求償"
    - "廣源商業／犯罪網與帳務責任"
    - "高衙內／柳生案"
  anti_forgetting:
    - "不得因蘇清身份線部分釐清或國家案收網，就把許慎言標成 CLOSED／背景人物。"
```

---

# 19｜青禾與七十二小時按摩體驗券：本輪新硬事件

```yaml
QINGHE_XU_MASSAGE_EVENT:
  event_status: "ACTIVE_FIRST_SESSION_STARTED"
  qinghe:
    role: "觀止技師／新創人物"
    current_function: "替長時間辦案之許慎言提供按摩恢復服務"
    not_established:
      - "戀愛"
      - "性交易"
      - "陪宿"
      - "法律代理關係"
      - "固定私人承諾"
  voucher:
    purchaser: "白御行"
    recipient: "許慎言"
    service: "觀止按摩服務"
    total_credit: "七十二小時"
    usage: "分次使用、按實際時數扣除"
    transferability: "不得自行轉賣／折現；具體觀止內部使用細則由掌櫃執行"
    consideration: "白御行正式付款／記帳"
    status: "PURCHASED_AND_GIFTED"
  current_use:
    - "許慎言在完成四核心案卷初步重排後，接受先使用一個時辰。"
    - "青禾已帶許慎言進後堂並開始本次按摩。"
  correction_to_old_record:
    - "舊 HOT 曾寫『七十二次按摩券』；自本輪玩家明示後，本線有效版本修正為『七十二小時按摩體驗券』。"
```

---

# 20｜廣源：仍是觀止核心案件，不得被軍械大案吞併

```yaml
GUANGYUAN_CORE:
  status: "ACTIVE_UNRESOLVED_GUANZHI_CORE_CASE"
  inherited_hard_clues:
    - "廣源存在十二冊暗帳及玄字／青字路線副簿。"
    - "前廣源帳房劉成安供稱廣源有兩套帳；其因追問無標記車與重複帳目失去兩指。"
    - "廣源二掌櫃憑證、義莊／南倉／井房、梁福、杜成、許奉年等線仍有未結事項。"
    - "廣源曾與爐料、偽牌、高溫爐等前案存在交叉線索。"
  current_role_split:
    xu_shenyan: "查法律責任、受害者權利、文書與訴訟法位"
    shen_wansan: "可從錢流、貨路、母簿／暗帳與商業結構切入"
  prohibition:
    - "不得因軍械案後來也出現廣源行／商路字樣，就把廣源所有舊案自動併成同一罪網。"
    - "廣源母簿真正位置仍不得以十二冊暗帳自動代替。"
```

---

# 21｜高衙內／柳生案：核心未決仍保持 UNKNOWN

```yaml
GAO_YANEI_LIUSHENG_CASE:
  status: "ACTIVE_CORE_CASE"
  fixed_observed_history:
    - "柳生曾帶十兩試圖與阿麗婭私奔。"
    - "高衙內在觀止公開下令『拖出去，打斷腿扔河裡』。"
    - "其手下對柳生施暴並拖走／轉移。"
    - "西門慶當時在場；其後以五千兩取得阿麗婭之預定名義。"
    - "阿麗婭保留柳生血染木簪，已作證物封存。"
  crucial_unknown:
    - "柳生是否實際死亡。"
    - "是否真正被扔入河中。"
    - "柳生現在哪裡。"
    - "西門慶是否事前指使、鼓勵或共同謀劃暴力。"
    - "高衙內另案與柳生案之邊界及其後續法律責任。"
  prohibition:
    - "不得把柳生失蹤＋傳聞淹死寫成已確認死亡。"
    - "不得把西門慶在場自動寫成其下令施暴。"
```

---

# 22｜潘金蓮：仍是核心掌櫃／被告與抗辯者，不得洗平

```yaml
PAN_JINLIAN_CURRENT:
  story_importance: "CORE"
  latest_confirmed_physical_position:
    - "先前在開封府就五千後算、蘇清替代結算及相關權限問題接受查問。"
    - "本輪玩家明示希望國家大案退場、觀止掌櫃該放；但尚未實際演出其離開開封府並返回觀止，故當前精確位置不得偷補。"
  active_legal_axes:
    - "五千掛牌／後算安排"
    - "蘇清一月替代結算之權限與民事責任"
    - "是否知悉或授權西門慶後續暴力之刑事分軸"
  persona_boundary:
    - "不得因被查帳就洗成認錯、療癒、倫理講師。"
    - "可用帳、權、風月、生存、程序與當年局勢提出實質抗辯。"
    - "不得把拒絕認罪寫成等於無責，也不得把承認部分帳務安排擴張成承認所有暴力。"
```

---

# 23｜西門慶下場：尚未 CLOSE

```yaml
XIMENQING_FATE:
  status: "ACTIVE_UNRESOLVED"
  current:
    - "仍在開封府刑事／合作查案體系內。"
    - "可繼續以暗櫃、口供、文書、人物名單等方式換取合作價值。"
    - "合作不等於無罪，也不自動免除蘇清二十八日、柳生／阿麗婭、廣源與其他受害者之刑民事責任。"
  unresolved:
    - "最終刑名"
    - "是否充軍或更重刑"
    - "合作對量刑／處置的實際影響"
    - "財產與商號如何處理"
    - "對蘇清、阿麗婭、柳生及其他受害者之民事賠償"
```

---

# 24｜沈萬三：回明線後返場與當前功能

```yaml
SHEN_WANSAN_CURRENT:
  confirmed:
    - "沈萬三曾短暫回其明朝線處理商務／貨款等事項後回到觀止。"
    - "其回場後重新確認自己仍是風滿樓三金主之一。"
    - "軍械大案後段主要從物流、車船、重量、免驗通道、帳面流量與實物流量差額切入。"
    - "國家案主鏡頭退出後，沈萬三仍可在廣源與商業帳線提供錢流／貨路分析。"
  not_established:
    - "沈萬三取得開封府司法權"
    - "沈萬三成為定陶盟軍／共治京師"
```

---

# 25｜六條御息所：本輪未結算的新來客線仍繼承 V2.5

```yaml
ROKUJO_CURRENT:
  inherited_from_v2_5:
    - "六條御息所仍為 ROUTE_EVENT／UNKNOWN_VISITOR，不在常設人物池。"
    - "趙受益只代付今晚女客房、茶食、必要日用；不取得任何人身、服務、陪宿、性、戀愛或契約權利。"
    - "六條與趙受益只成立初識與可同桌喝茶。"
    - "六條牛車／紅楓異路之返程機制仍 UNKNOWN。"
  this_hot:
    - "六條曾在趙氏三帝、觀止不清場等政治場面中旁觀並發言。"
    - "本 HOT 沒有新增其戀愛、陪宿、性、定居、掛牌或永久留下之決定。"
```

---

# 26｜人物位置（以最新可確認位置為準）

```yaml
CHARACTER_LOCATIONS:
  guanzhi_primary_or_nearby:
    - "白御行／前堂"
    - "春梅／觀止掌櫃線"
    - "李瓶兒／觀止掌櫃線"
    - "十三娘／現場統合與代傳話"
    - "沈萬三／已返場，可參與廣源與商務帳線"
    - "趙受益／觀止；國家案政治鏡頭已準備退場"
    - "趙桓／趙佶：曾在觀止處理國家案；本 HOT 末是否仍坐同桌不影響觀止接關，精確站位可依下一幕自然處理"
    - "李師師／張麗華／紅娘氏等：仍在觀止活動範圍；本 HOT 未新增其私人關係硬結論"
    - "六條御息所／觀止女客線；精確是否已回東偏廂 UNKNOWN"
  guanzhi_back_room:
    - "許慎言／接受青禾第一段一個時辰按摩"
    - "青禾／執行按摩服務"
  north_route:
    - "林沖／與楊志、生辰綱同行或近場，持趙佶皇家令牌，具現場判斷權"
    - "魯智深／同行保護林沖"
    - "楊志／掌生辰綱，願作證"
  kaifeng_or_state_case:
    - "包拯／開封府主持刑名與證據"
    - "西門慶／開封府刑事與合作程序"
    - "高俅／已被帶入官府程序"
    - "蔡京／接受政治退出／合作方向，仍需完成實際交代與法律分軸"
    - "陸謙／已被拘提，軍械與小帳在案"
    - "潘金蓮／最近硬位置仍是開封府查問線；是否已正式獲准離開尚未演出"
```

---

# 27｜本 HOT 後必須維持的開放問題

```yaml
OPEN_QUESTIONS:
  guanzhi_core:
    - "西門慶蘇清二十八日最終刑名與處置為何。"
    - "蘇清對潘金蓮之民事／帳務請求如何構成；潘有哪些有效抗辯。"
    - "五千替代結算造成之返還、利益、損害與收益歸屬如何裁定。"
    - "廣源母簿／核心帳與商業責任最後如何落地。"
    - "柳生是否仍活著、被拖走後發生何事。"
    - "高衙內除公開施暴命令外，其他案件如何獨立處理。"
    - "西門慶合作證據能否降低部分處置，但不得洗掉已證成重大責任。"
  state_case_background_only:
    - "梁師成、楊戩、朱勔、高俅、蔡京各自最終刑責與政治後果。"
    - "軍械三十二套是否全部追回。"
    - "梁山／濟州是否為真貨路還是誘餌。"
    - "生辰綱中夾帶文件／物件之完整目的與收件人。"
    - "蔡京是否完整交代；若有隱瞞，政治協議是否被取消。"
```

---

# 28｜禁止回歸／防鬼打牆規則

```yaml
ANTI_REGRESSION:
  - "不得再把許慎言寫成已退場或只剩按摩笑梗；按摩是恢復資源，法律線才是其核心。"
  - "不得把青禾因按摩許慎言自動寫成戀愛／性關係。"
  - "不得把蘇清身份線部分釐清等同其民事案 CLOSE。"
  - "不得把潘金蓮刑事未證成共犯，錯寫成民事無責。"
  - "不得把潘金蓮承認五千後算，擴寫成她承認西門慶所有暴力。"
  - "不得把西門慶合作、供出大案人物，寫成可以洗掉蘇清二十八日重責任。"
  - "不得把柳生寫死。"
  - "不得把廣源所有線與軍械案自動合併。"
  - "不得讓朝廷大案繼續無限長新名字，壓掉觀止自身人物與核心案件。"
  - "不得把趙受益／趙佶／趙桓在觀止出現倒灌成一般歷史正史；只屬本玩家線 ROUTE EVENT。"
  - "不得把風滿樓出資權寫成掌櫃權。"
  - "十三娘不得在潘不在時自動變成掌櫃；春梅、李瓶兒仍掌觀止實權。"
```

---

# 29｜下一幕自然接關

```yaml
NEXT_SCENE:
  primary:
    - "觀止前堂：春梅已搬出蘇清相關舊帳，蘇清／潘金蓮民事戰正式進入查帳與法律構成。"
    - "許慎言暫在後堂由青禾按摩一個時辰；可在休息結束後重新接案，也可由其助手／事先分類結果先運作，但不得替他完成未作之法律決定。"
  secondary:
    - "西門慶最終下場、廣源、高衙內／柳生可依開封府新消息重新進場。"
  background_only:
    - "軍械、蔡京、高俅、生辰綱等國家案允許以簡報／抄報方式偶爾回傳，不再搶走主鏡頭。"
  no_forced_choice_menu: true
```

---

# 30｜本 HOT 的一句接關摘要

> **京師軍械、御前營造與權臣網已在風滿樓收出足夠形狀：陸謙被抓、北伐軍械與偽軍籍工具實物落案，林沖持趙佶皇家令牌北接楊志與生辰綱，高俅入官府程序，蔡京接受以真正告老、九成家產入北伐基金、完整交代換取安全下庄的政治退出方向；刑名仍交包拯。白御行明示國家大案不再吞掉觀止主線，故事重新回到西門慶、蘇清／潘金蓮民事、廣源、高衙內／柳生。許慎言恢復定陶商會 principal lawyer 法位，白御行正式贈其七十二小時按摩體驗券；青禾已帶他進後堂先用一個時辰，而春梅已在前堂搬出蘇清舊帳——刑事第一輪之後，觀止自己的民事戰正式開桌。**

<!-- PROMOTED_HOT_SOURCE_END: 觀止青樓_白御行線_HOT_SAVE_V2.6_槐月二十一日破曉_京師軍械案收網_觀止民事戰重啟_許慎言七十二小時按摩券版.md -->

---

# APPENDIX C｜固化來源全文：觀止青樓_白御行線_HOT_SAVE_V2.7_槐月二十一日破曉_潘金蓮返樓_五千返還五萬索賠_身籍待查與一千兩候價版.md

> **法位：E84–E92 細節追溯來源。** 此 HOT 內的 CURRENT_SCENE／HOLD 只代表當時快照；不得覆寫本 MASTER 截止或 V3.5–V3.7 疊加層。若原 HOT 內某個標成 YAML 的區塊本身語法不合法，本 MASTER 只把該 fence 改標為 text 隔離，內容原文不改，避免來源語法缺陷破壞 MASTER 解析。

<!-- PROMOTED_HOT_SOURCE_BEGIN: 觀止青樓_白御行線_HOT_SAVE_V2.7_槐月二十一日破曉_潘金蓮返樓_五千返還五萬索賠_身籍待查與一千兩候價版.md -->
# 觀止青樓｜白御行線 HOT SAVE V2.7
## 理火三年槐月二十一日破曉｜潘金蓮返樓 × 五千原款退出 × 五萬個人賠償請求 × 潘金蓮身籍待查 × 一千兩條件式候價版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V2_7_HUAI21_DAWN_PAN_RETURN_5000_RETURN_50000_CLAIM_STATUS_CHECK_1000_INDICATIVE_BID"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V2.7"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime:
    - "GUANZHI_QINGLOU_V10_0"
    - "GUANZHI_QINGLOU_V10_1_V10_2_PATCH_WHEN_APPLICABLE"
  story_time_span:
    start: "理火三年槐月二十一日破曉／HOT V2.6 後"
    current: "理火三年槐月二十一日破曉至清晨前段；精確時刻未定"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AFTER_HOT_SAVE_COMMAND_AT_GUANZHI_FRONT_HALL"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V2.6_槐月二十一日破曉_京師軍械案收網_觀止民事戰重啟_許慎言七十二小時按摩券版.md"
  previous_hot_sha256: "a03ccaa2ad3acb4393acb5c386aeacb454005f737a331c3e57a337a4d35597f0"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"
  current_primary_story_domain:
    - "蘇清 vs 潘金蓮民事／帳務責任"
    - "潘金蓮與李瓶兒西門家身分／文書切割"
    - "觀止掌櫃權與高額交易治理修正"
    - "西門慶／柳生／廣源等核心案之後續"
```

---

# 0｜提交法位、來源與版本說明

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V2.6_槐月二十一日破曉_京師軍械案收網_觀止民事戰重啟_許慎言七十二小時按摩券版.md"
    role: "本檔直接前置 HOT；V2.6 以前有效事件全部繼承"

  legal_core_sources:
    - file: "觀止青樓_白御行線_HOT_SAVE_V2.4_槐月二十日深夜_風滿樓公案與五千後算開冊版.md"
      role: "許慎言代理、五千後算、蘇清／潘金蓮民事爭點、柳生／高衙內、廣源硬來源"
    - file: "觀止青樓_白御行線_HOT_SAVE_V2.5_槐月二十日深夜_開封法網擴張_阿麗婭重定義與六條御息所來訪版.md"
      role: "西門慶接受蘇清一月替代結算、阿麗婭身分重定義等直接來源"

  route_conversation_commit:
    role: "HOT V2.6 後至本次 HOT SAVE 命令前，觀止前堂／後堂已實際演出事件與玩家明示主張"

COMMIT_NOTE:
  - "本檔取代 HOT V2.6，成為白御行線當前直接接關切片；V2.6 保留為前置歷史來源。"
  - "本次只更新 HOT；不更新 MASTER，不修改人物卡／人物池基線。"
  - "本檔只把已演出行動、人物明示、帳面操作、玩家對自身意向及明示歷史主張寫入；未經查證的法律效果與歷史身籍不得偷補。"
  - "五千原款、五萬賠償請求、潘金蓮身籍、一千兩候價四軸分開保存。"
  - "蘇清自由妓女身分方向與阿麗婭首次出閣／第一個男人選擇權嚴格分開，不得互相代換。"
  - "梁山女性／性資源結構之討論屬當場假說；宋江口信只證明本玩家線中宋江所作回應，不證明梁山全寨實態。"
```

---

# 1｜當前場景與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年槐月二十一日"
  time: "破曉至清晨前段；精確時刻未知"
  primary_location: "觀止青樓／前堂；後堂按摩間並行"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  player:
    name: "白御行"
    current_position: "觀止前堂"
    last_confirmed_utterance_before_save:
      - "白御行明示：待潘金蓮合法身分處理完成，且潘金蓮本人真決定重新掛牌拍賣肉體時，願以一千兩／一夜作首輪捧場意向價。"
    no_new_player_action_after_save_command: true

  confirmed_present_or_immediately_active:
    front_hall:
      - "白御行"
      - "潘金蓮"
      - "蘇清"
      - "龐春梅"
      - "李瓶兒"
      - "沈萬三"
      - "紅娘氏"
    back_room:
      - "許慎言／仍在青禾第一段一個時辰按摩服務中；期間曾坐起參與法律討論，服務尚未明示完成"
      - "青禾／持續執行按摩"
    exact_position_not_required:
      - "十三娘、趙受益、李師師、張麗華等仍屬觀止活動人物；本段未形成其新硬事件"

  offsite:
    西門慶:
      current: "開封府刑事／合作程序中"
    包拯:
      current: "開封府主持刑名與證據程序"
    宋江:
      current: "不在觀止；本輪只由梁山口信／傳話回覆白御行詢價"

  direct_resume_point:
    - "潘金蓮已由開封府查問線實際返回觀止；目前不是被關押在觀止，也未被宣判刑事責任。"
    - "蘇清對潘金蓮的民事／帳務戰已從抽象討論進入具體本金、賠償與身分治理。"
    - "五千原掛牌款已在觀止內部被重新分類為待返還／司法保全款；尚未演出實銀完成交付開封府。"
    - "蘇清／許慎言準備以五萬兩作潘金蓮個人賠償之起始請求；潘金蓮未認責，官府亦未判。"
    - "潘金蓮現行是否具自由良籍／奴籍／妾室及可公開從妓資格尚未查清；優先查官冊、身契與過往改籍。"
    - "白御行一千兩／一夜只為潘金蓮未來合法重新掛牌後之條件式意向價；目前不成交、不付款、不預約、不形成性同意。"
```

---

# 2｜PAN21-E01｜潘金蓮由開封府返回觀止

```yaml
EVENT_RECORD:
  event_id: "PAN21-E01-PAN_RETURNS_FROM_KAIFENG"
  status: "COMPLETED_RETURN"
  location: "觀止前堂"
  actor: "潘金蓮"

CONFIRMED:
  - "潘金蓮實際自開封府查問線返回觀止前堂。"
  - "其自述不是被『釋放出獄』；開封府先完成本輪需問事項，之後有傳即到。"
  - "潘金蓮回觀止後重新以掌櫃／當事人身分參與蘇清民事帳務戰。"

NOT_ESTABLISHED:
  - "潘金蓮獲刑事無罪判決"
  - "潘金蓮對蘇清民事無責"
  - "潘金蓮永久免受開封府傳喚"
  - "潘金蓮已恢復或取得妓籍"
```

---

# 3｜SU-PAN21-E01｜蘇清對潘金蓮民事案之三大爭點

```yaml
CIVIL_CASE_FRAME:
  status: "ACTIVE"
  plaintiff_side:
    principal: "蘇清"
    representative_lawyer: "許慎言"
  defendant_side:
    principal: "潘金蓮"
    counsel: "NOT_YET_RETAINED"

  current_major_issues:
    - id: "AUTHORITY_TO_SUBSTITUTE"
      question: "潘金蓮當時是否有權把『蘇清一月』作為西門慶五千掛牌交易之替代結算。"
    - id: "BENEFIT_AND_LOSS"
      question: "西門慶實際取得蘇清二十八日控制／利益後，觀止、西門慶、潘金蓮與蘇清各自取得或承受什麼財產利益與損害。"
    - id: "POST_KNOWLEDGE_USE"
      question: "潘金蓮何時知道蘇清在西門府實際遭遇；若其後仍把蘇清二十八日作為有效結算，其知情後責任如何。"

  pan_response:
    - "潘金蓮未認輸，明示自己可另請狀師應訴。"
    - "潘金蓮接受查帳與訴訟攻防，不等於承認暴力、共犯或全部賠償。"
```

---

# 4｜FIVE-THOUSAND21-E01｜五千原款之觀止帳務處理

```yaml
FIVE_THOUSAND_ORIGINAL_PAYMENT:
  amount_taels: 5000
  source_transaction: "阿麗婭五千掛牌／後續以蘇清一月替代結算之舊案"
  receipt_status_in_current_scene:
    - "觀止舊帳被翻出後，前堂以既有帳冊確認五千為曾實際進入觀止帳房之款項。"

  current_guanzhi_internal_position:
    - "白御行主張：阿麗婭未交付、蘇清替代又引發重大責任，觀止無正當理由永久保有原五千。"
    - "許慎言認為五千原款應與蘇清損害賠償分軸；觀止首先處理原款退出。"
    - "春梅／李瓶兒在帳上將此筆重新標為待返還／司法保全款。"

  current_status: "RECLASSIFIED_PENDING_RETURN_OR_JUDICIAL_ESCROW"
  actual_cash_transfer_to_kaifeng_completed: false
  final_recipient: "UNDECIDED_BY_KAIFENG_OR_LAW"

  prohibited_conclusions:
    - "不得寫成五千已直接退到西門慶手中。"
    - "不得寫成五千即蘇清賠償。"
    - "不得寫成觀止已完成全部返還程序。"
```

---

# 5｜TENFOLD21-E01｜『假一賠十』與五萬賠償請求

```yaml
TENFOLD_COMPENSATION_CLAIM:
  status: "PLAINTIFF_CLAIM_DIRECTION_NOT_JUDGMENT"
  base_number_used_in_argument: 5000
  requested_multiplier: 10
  requested_amount_taels: 50000

  origin:
    - "白御行以商家信用『假一賠十』提出十倍賠償構想。"
    - "白御行認為潘金蓮原交易對西門慶形成錯誤／替代交付，而西門慶對蘇清造成的實際傷害由蘇清承受，因此十倍賠償利益有理由回到蘇清。"
    - "蘇清明示自己要主張十倍；其理由之一是若只退五千，潘金蓮／觀止僅恢復原狀，而蘇清二十八日實害沒有被賠。"

  shen_wansan_analysis:
    - "沈萬三認為『假一賠十』原屬交易信用結構；不能把蘇清本人當成假貨。"
    - "可轉化檢查的是錯誤／無權替代交易所生賠償利益與實際受害者間之歸屬。"
    - "若西門慶一邊實際取得蘇清利益，一邊又主張自己只是拿到假貨之單純受害者，需拆解其實際利益與損失。"

  xu_shenyan_position:
    - "許慎言願意把五萬作為訴訟起始請求方向，但必須找到可成立之法律／交易結構，不能只寫『白會長想讓潘金蓮枯死』。"
    - "五萬目前只是請求額；許慎言明示不是已判。"

  pan_jinlian_position:
    - "潘金蓮未承認十倍賠償成立。"
    - "潘金蓮提出抗辯方向：要先證明她當年究竟承諾賣的是阿麗婭本人、初夜、優先預定、掛牌資格或其他權利。"

  final_judgment: "UNDECIDED"
```

---

# 6｜PAN-PERSONAL21-E01｜潘金蓮個人責任與觀止公帳分離

```yaml
PUBLIC_PRIVATE_LIABILITY_SEPARATION:
  trigger:
    - "白御行明示：若十倍等賠償屬潘金蓮本人錯誤行為之責任，不得由觀止公帳替她付款。"

  accepted_operational_principle:
    guanzhi:
      - "五千原款之返還／司法保全屬觀止舊交易帳務軸。"
    pan_jinlian_personal:
      - "若法院／有效程序最後判定潘金蓮個人負損害賠償責任，應由潘金蓮個人財產／個人收入承擔。"
      - "不得把姑娘收入、技師收入、其他掌櫃份額或觀止公帳當成其個人賠償池。"

  pan_acceptance_scope:
    - "潘金蓮接受公私分帳原則。"
    - "潘金蓮沒有因此承認五萬或任何具體賠償數額。"

  xu_case_drafting:
    - "許慎言準備將潘金蓮個人責任與觀止五千原款證明／返還軸分開書寫。"
```

---

# 7｜SU-QING21-E02｜蘇清要的是『自由妓女』身分

```yaml
SU_QING_STATUS_DIRECTION:
  current_desired_status:
    - "保留妓女／風月職業身份。"
    - "解除被觀止、掌櫃或其他人作為可轉讓／可抵帳人身資源之位置。"
    - "由蘇清本人決定接誰、拒誰、價格、是否服務、何時離開。"
    - "仍願在觀止工作，依法／依樓規支付抽成、房錢、堂費與其他合理成本。"

  explicit_non_goal:
    - "不是要求被洗回良家身份。"
    - "不是要求離開觀止。"
    - "不是要求免除所有觀止營業規矩。"

  relation_to_civil_case:
    - "蘇清對潘金蓮之訴，核心之一是禁止掌櫃再以她本人作他人交易之替代交付／抵帳。"
```

---

# 8｜AALIYAH21-LOCK｜阿麗婭與蘇清不得混線

```yaml
AALIYAH_CURRENT_LOCK:
  inherited_hard_state:
    - "阿麗婭舊五千掛牌／出閣程序沒有完成為一個有效的首次性服務交付。"
    - "阿麗婭目前沒有因五千舊案自動重新掛牌。"

  current_story_direction:
    - "阿麗婭要保留自己選擇第一個男人／首次真正出閣對象的機會。"

  separation_from_su_qing:
    - "蘇清：已選擇妓女職業，追求自由身與自主營業。"
    - "阿麗婭：首次出閣尚未完成，重點是第一個男人由她自己選。"
    - "兩者不得以『都是自由』為由合併成同一身分方案。"
```

---

# 9｜GUANZHI-GOV21-E01｜潘金蓮定價權與高額交易治理修正

```yaml
GUANZHI_HIGH_VALUE_TRANSACTION_GOVERNANCE:
  trigger:
    - "白御行指出潘金蓮過去收費與交易權過度集中，客人與姑娘都可能因過度榨價／人身抵帳反彈；目的不是罷免潘金蓮，而是要求其反省並改進。"

  pan_jinlian_position:
    - "潘金蓮接受自己仍可當掌櫃，但承認特殊高額交易需要額外規則。"

  current_operational_rule:
    normal_operations:
      - "正常酒菜、房錢、普通席與一般營業價格，潘金蓮仍保留日常掌櫃定價／經營權。"
    special_high_value_or_personhood_transactions:
      examples:
        - "長期服務"
        - "包月"
        - "首次出閣"
        - "身分／掛牌變更"
        - "轉契／人身相關契約"
        - "其他高額且可能改變姑娘長期位置之安排"
      requirements:
        - "至少另有一名掌櫃複核；目前春梅或李瓶兒可擔任複核。"
        - "涉及姑娘本人長期服務／身體／身分者，姑娘本人必須明示同意／簽認。"
        - "不得由潘金蓮一人把人、價格、交付與帳務一路單獨定到底。"

  governance_effect:
    - "潘金蓮未被解除掌櫃。"
    - "李瓶兒與春梅既有掌櫃職權被再次確認。"
    - "觀止高額人身／長約交易新增第二掌櫃複核與本人確認機制。"
```

---

# 10｜PAN-LISTING21-E01｜潘金蓮重新掛牌之未成立交易

```yaml
PAN_RELISTING_DISCUSSION:
  current_status: "NOT_CURRENTLY_LISTED_FOR_PUBLIC_SEX_WORK_IN_THIS_ROUTE_EVENT"

  sequence:
    - "白御行曾先提出五百兩拍潘金蓮『復出第一個月』之意向，後撤回；沒有成交。"
    - "其後白御行提出一千兩／一夜，想以潘金蓮床上能力作為對其帶領觀止能力的一部分觀察；前堂一度討論成交條款。"
    - "隨後白御行指出潘金蓮目前只是觀止掌櫃，且西門家／妓籍法位尚未處理，不能直接公開掛牌賣淫。"
    - "許慎言同意必須先釐清潘金蓮現行法律身分與從妓資格；先前一千兩不得記正式成交。"

  final_current_offer:
    offered_by: "白御行"
    amount_taels: 1000
    unit: "一夜"
    condition:
      - "潘金蓮先完成合法身分處理。"
      - "潘金蓮本人之後真決定重新掛牌／公開拍賣性服務。"
    nature: "CONDITIONAL_INDICATIVE_BID_ONLY"
    paid: false
    reserved: false
    sexual_consent_created: false
    priority_right_created: false

  pan_response:
    - "潘金蓮接受把一千兩記作未來合法重新掛牌後的首輪意向價／候價。"
    - "潘金蓮明示若真的拍賣，其他人可競價；一千兩不保證白御行得標。"
    - "潘金蓮明示要先查清自己是否真正屬於自己，再決定是否重新掛牌、賣什麼、賣多少。"
```

---

# 11｜LI-PINGER21-E01｜李瓶兒西門家身分與嫁妝軸

```yaml
LI_PINGER_STATUS_LINE:
  inherited_route_hard_state:
    - "李瓶兒現行玩家線仍未完成與西門慶之正式法律切割。"

  player_provided_historical_correction:
    source: "白御行本輪明示保證"
    claim:
      - "李瓶兒當年是改嫁入西門府。"
      - "李瓶兒帶嫁妝進府。"
      - "不是以奴籍被西門慶購買後收為妾。"
    current_save_treatment: "PLAYER_PROVIDED_HIGH_WEIGHT_HISTORICAL_CORRECTION; DOCUMENT_CHECK_STILL_USEFUL"

  legal_direction_discussed:
    - "李瓶兒之核心問題優先視為妾室／改嫁關係如何合法解除，而非潘金蓮式奴籍／身契來源案。"
    - "若其帶嫁妝改嫁之校正成立，後續還應查嫁妝與其個人財產如何退出西門府。"
    - "李瓶兒沒有因本輪討論表示自己要重新掛牌從妓。"

  anti_merge:
    - "不得把李瓶兒與潘金蓮都簡化成『西門慶可以賣的妾』。"
```

---

# 12｜PAN-STATUS21-E01｜潘金蓮身籍／身契來源案啟動

```yaml
PAN_JINLIAN_STATUS_CASE:
  status: "ACTIVE_DOCUMENT_AND_REGISTRY_INQUIRY"
  current_legal_identity: "UNRESOLVED"

  player_provided_historical_claims:
    source: "白御行在故事中提供之歷史資訊／推論"
    claims:
      - "潘金蓮早年曾為奴婢／奴籍。"
      - "其因與原主人發生曖昧／勾引老爺，被主母處置後進入武大郎家。"
      - "武大郎死後只有弟弟武松作近親；白御行因此提出若身契仍存，武松可能涉及承繼。"
    legal_status: "HISTORICAL_CLAIMS_AND_HYPOTHESIS_NOT_YET_PROVEN_BY_CURRENT_GUANZHI_DOCUMENTS"

  key_counter_hypothesis:
    - "白御行亦主動提出：武大郎可能因愛或其他原因，曾替潘金蓮辦理放良／改籍；若曾正式脫籍，後續『身契由武松繼承』整條推論可能失效。"

  xu_shenyan_inquiry_order:
    - "先查潘金蓮現在官冊究竟登記為良、奴、妾或其他法位。"
    - "追查其由原主人家進入武大郎家時，有無放良／改籍／嫁娶／身契轉讓文書。"
    - "查武大郎生前是否另辦脫籍。"
    - "只有在奴籍／身契從未解除前提成立後，才查武大死亡時身契是否進入遺產。"
    - "再查武松是否為唯一合法承繼人、是否實際承受相關權利。"
    - "最後才處理潘金蓮後續自行進西門府是否存在權利來源瑕疵。"

  prohibited_conclusions:
    - "不得現在就寫潘金蓮仍是奴籍。"
    - "不得現在就寫武松是潘金蓮主人。"
    - "不得把潘金蓮本人等同普通物件；法律爭的是身契／身分權利效力。"
    - "不得因潘金蓮自願跟西門慶，就自動證成所有舊身契已合法移轉。"
```

---

# 13｜WANGPO21-E01｜西門慶付款給王婆之線索

```yaml
WANG_PO_PAYMENT_CLUE:
  source: "白御行本輪明示提供"
  current_status: "PLAYER_PROVIDED_HISTORICAL_CLUE_PENDING_DOCUMENT_OR_WITNESS_VERIFICATION"

  confirmed_as_player_claim:
    - "西門慶當年曾把一筆與潘金蓮往來相關的錢付給王婆。"
    - "王婆是西門慶與潘金蓮之間的牽線／皮條中間人。"

  unknown:
    - "王婆收款究竟是媒錢、跑腿錢、封口錢、買契價銀或其他性質。"
    - "王婆是否持有潘金蓮身契或受真正持契人授權。"
    - "王婆是否將部分銀錢轉交潘金蓮。"
    - "即使潘金蓮曾收錢，該錢是否為身價、贈銀、媒介分成或其他性質。"

  shen_xu_analysis:
    - "錢流本身不足以證明買身；真正關鍵是王婆憑什麼收錢、取得／轉交了什麼權利。"
```

---

# 14｜LIANGSHAN21-E01｜梁山性需求／女性身分討論之法位

```yaml
LIANGSHAN_GENDER_AND_SEXUAL_STRUCTURE_DISCUSSION:
  status: "IN_SCENE_HYPOTHESIS_DISCUSSION_ONLY"

  white_yuxing_hypotheses:
    - "梁山作為軍事組織，性需求可能像軍隊一樣被推到核心軍事空間之外。"
    - "賊軍未必像合法官軍有完整軍紀／外圍市場制度，因此部分女性可能缺乏身體自主權。"
    - "『壓寨夫人』可能在部分案例中只是好聽稱號，實際女性位置可能從屬於頭領／寨權。"
    - "梁山可能存在非貨幣化的性／身體服務；沒有青樓不等於沒有性供給。"

  shen_wansan_and_su_qing_distinction:
    - "非貨幣結算不等於沒有交換；可能嵌在食宿、庇護、依附、家眷、戰利品與權力中。"
    - "最黑的結構不是『免費妓院』，而是女性根本沒有被承認為需要本人同意／結帳的獨立交易主體。"

  objective_world_fact: false
  prohibition:
    - "不得在下一輪直接把梁山全寨寫成系統性強迫女性之確定事實。"
    - "不得把『梁山都是 GAY』笑談升格為人物性向設定。"
```

---

# 15｜SONGJIANG21-E01｜五萬兩＋潘金蓮『押寨夫人』詢價口信

```yaml
SONG_JIANG_INQUIRY:
  status: "COMPLETED_ROUTE_MESSAGE_EXCHANGE"
  initiator: "白御行"
  proposal_as_sent:
    - "白御行提出以五萬兩為條件，詢問宋江／梁山是否收潘金蓮去作『押寨夫人』。"
  consent_boundary_in_message:
    - "春梅於觀止一側明記：此為白御行詢價，不代表潘金蓮同意被出售、婚配或上梁山。"

  song_jiang_reply_as_received:
    - "宋江先問五萬兩究竟是白御行給梁山，還是梁山給白御行。"
    - "得知是白御行出五萬後，宋江表示五萬資助梁山自可感激。"
    - "宋江明問潘金蓮本人願不願意。"
    - "宋江另問武松是否知道。"
    - "宋江表示梁山不是人市；若潘金蓮自己願意上山，其作客、家眷或其他位置可以另談；若她不願，五十萬也不能作為把她賣給梁山的理由。"
    - "宋江另以玩笑／回應指出，若潘金蓮真肯上山，不必由白御行替她指定男人，山上未娶好漢很多。"
    - "宋江反問白御行為何願意倒貼五萬只為把潘金蓮送走。"

  authority_boundary:
    - "此為本玩家線收到之宋江口信；證明宋江當場表態，不自動證明梁山所有頭領／歷史所有事件皆依此原則。"
```

---

# 16｜PAN-RETAIN21-E01｜『送走潘金蓮、扶李瓶兒』長期利益討論

```yaml
MANAGEMENT_SUCCESSION_DISCUSSION:
  white_yuxing_view:
    - "白御行一度認為：若倒貼五萬把潘金蓮送去梁山，再扶植李瓶兒當掌櫃，長期可能收穫更多。"

  shen_wansan_counteranalysis:
    - "五萬給梁山不代表潘金蓮附送；最壞結果可能是五萬捐掉、潘金蓮仍留觀止。"
    - "李瓶兒是否擴大掌櫃權應由李瓶兒本人決定。"
    - "潘金蓮的經營能力可以保留，其錯誤責任由本人承擔；沒必要用五萬換掉整個人。"

  li_pinger_position:
    - "李瓶兒明示：不必先把潘金蓮送走，她才有資格多管觀止。"
    - "若未來需要她多承擔掌櫃職責，可以談，但不是因為潘金蓮被賣掉。"
    - "李瓶兒明示若潘金蓮再拿姑娘去抵帳，她會第一個主張收回潘金蓮相關帳權。"

  current_management_result:
    - "潘金蓮留任掌櫃。"
    - "李瓶兒與春梅掌櫃職能持續。"
    - "沒有形成潘金蓮離樓／梁山轉移／李瓶兒唯一接班之決定。"
```

---

# 17｜XU-QINGHE21-E01｜許慎言與青禾按摩服務持續

```yaml
XU_SHENYAN_MASSAGE_CURRENT:
  inherited_credit:
    - "白御行已正式贈許慎言七十二小時分次按摩體驗額度。"
  current_session:
    planned_first_session: "一個時辰"
    current_status: "ONGOING_OR_NOT_EXPLICITLY_COMPLETED"
    provider: "青禾"
    recipient: "許慎言"
    observed:
      - "許慎言在按摩期間持續隔珠簾參與蘇清／潘金蓮法律討論。"
      - "在潘金蓮身籍議題變複雜時，許慎言曾坐起來拆解法律問題；青禾提醒服務尚有時間。"
  relationship_boundary:
    - "不建立感情、性、陪宿、戀愛或私人所有權。"
```

---

# 18｜關係與責任硬狀態

```yaml
RELATION_AND_RESPONSIBILITY_STATE:
  pan_jinlian_vs_su_qing:
    status: "ACTIVE_CIVIL_ADVERSARIES_WITH_SHARED_GUANZHI_WORKPLACE"
    confirmed:
      - "蘇清仍希望留在觀止工作。"
      - "蘇清主張的是潘金蓮個人及相關交易責任，不是要摧毀觀止。"
      - "潘金蓮願意應訴、查帳並保留抗辯。"
      - "兩人仍可互相譏諷、交易式拆招；不得因此寫成和解或仇恨永久化。"

  pan_jinlian_vs_guanzhi:
    - "潘金蓮仍是掌櫃。"
    - "潘金蓮高額人身／長約交易權受到第二掌櫃複核限制。"
    - "潘金蓮若有個人賠償，不得由觀止公帳代償。"

  bai_yuxing_vs_pan_jinlian:
    - "白御行反覆以高價掛牌、梁山、五萬賠償等話題調侃／施壓潘金蓮。"
    - "目前不存在白御行與潘金蓮已成交的一夜性交易。"
    - "目前只有潘金蓮未來合法重新掛牌後的一千兩／夜條件式意向價。"

  li_pinger_vs_pan_jinlian:
    - "李瓶兒支持潘金蓮繼續作掌櫃，但支持拆分其過度集中之高額交易權。"
    - "李瓶兒沒有接受『潘金蓮離開＝自己接班』的自動安排。"
```

---

# 19｜本 HOT 必須保留的 UNKNOWN／UNDECIDED

```yaml
OPEN_QUESTIONS:
  su_pan_civil:
    - "五萬十倍賠償是否有可成立法律基礎。"
    - "潘金蓮當年究竟承諾了什麼交易標的／權利。"
    - "潘金蓮何時知道蘇清實際受暴力控制與二十八日遭遇。"
    - "潘金蓮知情後是否仍利用蘇清二十八日作有效五千結算。"
    - "蘇清可得多少返還、收益、損害或其他救濟。"

  five_thousand:
    - "五千待返還／司法保全款最後交付給誰、如何扣押、是否與西門慶其他財產程序合併。"
    - "實際將五千從觀止移交開封府之事件尚未演出。"

  pan_status:
    - "潘金蓮由原主家進武大家時究竟是放良嫁人、身契轉讓、其他處置。"
    - "武大郎是否曾替潘金蓮辦理放良／改籍。"
    - "如奴籍持續，武大死亡時相關身契是否依法進入遺產。"
    - "武松是否為唯一合法承繼人且實際承受身契權利。"
    - "潘金蓮後來進西門府時的正式納妾／身分文書是什麼。"
    - "西門慶給王婆之錢究竟性質為何。"
    - "王婆是否分錢給潘金蓮。"
    - "潘金蓮目前是否有資格重新登記／掛牌為妓女。"

  li_pinger_status:
    - "李瓶兒與西門慶之妾室／婚姻關係如何合法解除。"
    - "李瓶兒嫁妝清單、現存財產與退出西門府之財產處理。"
    - "李瓶兒沒有提出從妓／掛牌決定。"

  core_cases_inherited:
    - "西門慶蘇清二十八日最終刑名與處置。"
    - "廣源母簿／核心帳與商業刑民責任。"
    - "柳生實際所在與西門慶『還要問話』口供線後續。"
    - "高衙內公開施暴命令之外的其他責任。"
```

---

# 20｜禁止回歸／反污染

```yaml
ANTI_REGRESSION:
  - "不得把五萬寫成已判、已欠、已執行；目前只是蘇清／許慎言方之起始請求額。"
  - "不得把五千待返還／司法保全寫成已直接退給西門慶。"
  - "不得把五千返還與蘇清五萬賠償合併成同一筆錢。"
  - "不得把潘金蓮個人賠償從觀止公帳、姑娘收入、技師收入或其他掌櫃份額支付。"
  - "不得把蘇清寫成要恢復良家；她現在要的是自由妓女身分。"
  - "不得把阿麗婭套用蘇清方案；阿麗婭重點是首次出閣未完成、第一個男人自己選。"
  - "不得把潘金蓮目前寫成已重新掛牌妓女。"
  - "不得把白御行一千兩／一夜寫成已成交、已付款、已預約或已取得性服務資格。"
  - "不得把潘金蓮早年奴婢史直接推成其現在仍為奴籍；必須先查放良／改籍與官冊。"
  - "不得把武松寫成潘金蓮確定主人／持契人；目前只是條件式繼承假說。"
  - "不得把王婆收西門慶銀錢寫成已證實買身價。"
  - "不得把李瓶兒與潘金蓮的西門家身分案混在一起；瓶兒目前以改嫁／嫁妝校正線處理。"
  - "不得把宋江口信寫成梁山全寨制度真相。"
  - "不得把梁山女性缺乏身體自主權之討論寫成已查證歷史。"
  - "不得把潘金蓮因治理修正而寫成被罷免；她仍是觀止掌櫃。"
  - "不得把李瓶兒因『可多管一些』寫成已接受唯一掌櫃／取代潘金蓮。"
  - "不得再把許慎言只寫成按摩笑梗；其仍是蘇清主要代理律師與觀止法律援助核心。"
  - "不得把青禾因按摩許慎言自動寫成戀愛／性關係。"
```

---

# 21｜下一幕自然接關

```yaml
NEXT_SCENE:
  primary_options_for_world:
    - "查潘金蓮官籍／身契：由開封府、戶籍、舊主家／武大家相關文書線先回一筆可驗證資料。"
    - "蘇清／潘金蓮民事：繼續查當年五千掛牌真正承諾標的、潘金蓮知情時間與後堂副冊。"
    - "五千原款：由春梅／瓶兒準備移交司法保全所需帳證，但不得偷寫已完成交款。"
    - "許慎言按摩第一時辰若自然結束，可正式回前堂整理五萬請求與潘金蓮抗辯。"

  secondary:
    - "西門慶／柳生／廣源任何一條可由開封府短報重入，但不得再次讓國家大案吞掉觀止主鏡頭。"

  optional_humor_or_relation:
    - "潘金蓮可繼續就一千兩候價、梁山倒貼五萬、自由妓女與掌櫃治理與白御行／蘇清拆招；不得因此提前完成掛牌。"

  no_forced_choice_menu: true
  next_action_owner: "WORLD_OR_PLAYER_AFTER_HOLD_RELEASE"
```

---

# 22｜本 HOT 一句接關摘要

> **槐月二十一日破曉，潘金蓮已自開封府查問線真正回到觀止，蘇清對她的民事／帳務戰正式開打。觀止舊帳確認五千曾實收入帳，現已在樓內重新列作待返還／司法保全款，但尚未實際移交；蘇清與許慎言則以『假一賠十』延伸出五萬兩潘金蓮個人賠償請求，潘金蓮未認責、官府未判，且公私帳已明確拆開。蘇清要的是留在觀止做自由妓女；阿麗婭要的是保住自己選第一個男人的機會，兩線不得混。白御行曾多次拿潘金蓮復出掛牌開價，最後留下的有效狀態只有：待潘金蓮先查清官籍／身契、合法取得公開從妓資格且本人真決定重新掛牌後，白御行願出一千兩／一夜作首輪意向價；目前不成交。潘金蓮早年奴籍、武大是否放良、武松是否可能承繼、西門慶付王婆之錢究竟買到什麼，全部轉入身籍文書調查，不得偷填。潘金蓮仍是觀止掌櫃，但高額長約／人身交易已新增第二掌櫃複核與本人簽認；李瓶兒、春梅之掌櫃權再次確認。故事下一刀應落在潘金蓮官籍／身契實證，或蘇清五萬請求真正能否站住。**

<!-- PROMOTED_HOT_SOURCE_END: 觀止青樓_白御行線_HOT_SAVE_V2.7_槐月二十一日破曉_潘金蓮返樓_五千返還五萬索賠_身籍待查與一千兩候價版.md -->

---

# APPENDIX D｜固化來源全文：觀止青樓_白御行線_HOT_SAVE_V2.8_槐月二十一日白日_潘身籍補證_白玉池許願幣定存_師師如夫人確認與晚宴前休息版.md

> **法位：E84–E92 細節追溯來源。** 此 HOT 內的 CURRENT_SCENE／HOLD 只代表當時快照；不得覆寫本 MASTER 截止或 V3.5–V3.7 疊加層。若原 HOT 內某個標成 YAML 的區塊本身語法不合法，本 MASTER 只把該 fence 改標為 text 隔離，內容原文不改，避免來源語法缺陷破壞 MASTER 解析。

<!-- PROMOTED_HOT_SOURCE_BEGIN: 觀止青樓_白御行線_HOT_SAVE_V2.8_槐月二十一日白日_潘身籍補證_白玉池許願幣定存_師師如夫人確認與晚宴前休息版.md -->
# 觀止青樓｜白御行線 HOT SAVE V2.8
## 理火三年槐月二十一日白日｜潘身籍補證 × 白玉池許願幣定存框架 × 李師師如夫人再確認 × 李瓶兒晚宴前置 × 師師房內休息接關版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V2_8_HUAI21_DAY_PAN_STATUS_WISH_COIN_DEPOSIT_RIRU_RECONFIRM_DINNER_REST"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V2.8"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V11.0-R2"
  character_source: "觀止人物卡池_LCAPG_V2.1"
  story_date: "理火三年槐月二十一日"
  time_of_day: "白日／晚宴前；精確時刻未知"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AT_LI_SHISHI_PRIVATE_ROOM_REST_BEFORE_EVENING_DINNER"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V2.7_槐月二十一日破曉_潘金蓮返樓_五千返還五萬索賠_身籍待查與一千兩候價版.md"
  previous_hot_sha256: "031f2c575eb26e8aa51d62dd4ca9856939392ab9a542b2051e8f570609403a29"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"
  save_scope:
    - "HOT V2.7 後潘金蓮身籍／王婆金流新文書結果"
    - "六條御息所與張麗華進入本日白日人物場之新互動"
    - "白玉池非正式再檢、阿泠所有權、許願幣與材質構想"
    - "阿泠一百枚一年三枚半之定存利率同意與流動性模型"
    - "白御行向李師師認錯、李師師收下道歉並明示原諒"
    - "李師師如夫人意願、住觀止安排、與李瓶兒未來並列原則"
    - "李瓶兒今晚受邀吃飯及其『先吃飯』之界線"
    - "紅娘氏得知師師曾在假設三人親密題中選過她，但未形成邀約"
    - "師師房內足部親密、腳環構想、煙青色肚兜私人畫像與晚宴前共眠休息"
```

---

# 0｜提交法位、來源與反污染說明

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V2.7_槐月二十一日破曉_潘金蓮返樓_五千返還五萬索賠_身籍待查與一千兩候價版.md"
    role: "本檔直接前置 HOT；V2.7 以前有效事件全部繼承"

  master_archive:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"
    role: "較早長期因果與玩家硬狀態來源"

  white_jade_pool_prior_sources:
    - "HOT V1.6：阿泠自選名、白玉池水療能力、未接受白姓／兄妹關係、封池與異常研究"
    - "HOT V2.2：白玉池第一輪復開前檢查"
    - "HOT V2.3：白玉池秘密擴大知情與第二輪檢查未記錄"

  li_shishi_prior_sources:
    - "HOT V2.2：如夫人前置、愛的告白未答、七色肚兜與煙青色選擇"
    - "HOT V2.4：紅娘三人親密話題仍僅討論／假設，不是實際邀請"

  current_route_conversation_commit:
    role: "HOT V2.7 後至本次 HOT SAVE 命令前之直接劇情事件、玩家明示自身言行與 NPC 可觀察回應"

COMMIT_NOTE:
  - "本檔取代 HOT V2.7，成為白御行線當前直接接關切片；V2.7 保留為前置歷史來源。"
  - "本次只更新 HOT；不更新 MASTER，不修改人物卡池基線。"
  - "潘金蓮身籍文書只保存已查到之官冊／副冊文字與可支持的法律方向，不補造失落原始文書。"
  - "許願幣、SPA 定價、材質與定存分開保存；概念成立不等於已營業、已鑄幣或已簽完整金融契約。"
  - "阿泠對定存利率之『同意』只成立利率條件；本輪未完成實際存入數量、正式書面契約、備付金或對外放貸。"
  - "李師師如夫人意願為本人再次明示；仍未觀察到對外公告、官籍／家冊登記或正式儀式。"
  - "李瓶兒今晚只同意來吃飯；任何三人親密／同床／性交均未成立。"
  - "李師師床上語言之粗口／低俗／低賤討論只保存為本線自述與當下語言邊界，不倒灌人物卡固定人格。"
  - "阿泠仍未接受白姓、妹妹或白家人身分；玩家本輪以『兄妹／白玉池泠』作玩笑或主張，不得覆寫既有拒絕。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年槐月二十一日"
  time: "白日／晚宴前；精確時刻未知"
  location: "觀止青樓／李師師私人房間／榻上"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  player:
    name: "白御行"
    current_position: "李師師私人房間／與李師師同榻休息"
    last_confirmed_action:
      - "白御行起身結束跪歉後抱著李師師。"
      - "其後接受李師師邀請，上榻與她相擁休息，準備晚宴前先睡一覺。"
    next_action_owner: "WORLD_OR_PLAYER_AFTER_REST_SCENE_RESUMES"

  li_shishi:
    current_position: "自己房內／與白御行同榻"
    current_state:
      - "已明示原諒白御行本次道歉所對應之舊事。"
      - "已再次明示想要如夫人位置。"
      - "已同意目前繼續住觀止、生活與工作自主不被打亂。"
      - "已同意今晚邀李瓶兒來吃飯。"
      - "目前選擇與白御行休息；未建立休息期間自動性同意。"

  evening_due:
    - "李師師設小席請李瓶兒吃晚飯；白御行在席。"
    - "李瓶兒已回覆：晚上會來，先吃飯。"
    - "晚宴後是否留宿、是否進入三人親密，由李瓶兒當晚自行決定。"
```

---

# 2｜INHERITED-ACTIVE21｜V2.7 仍有效之核心硬狀態

```yaml
INHERITED_ACTIVE_HARD_STATE:
  su_qing_vs_pan:
    status: "ACTIVE_CIVIL_AND_ACCOUNTING_DISPUTE"
    core_issues:
      - "潘金蓮當時是否有權以蘇清一月替代西門慶五千交易。"
      - "蘇清實際損害、各方利益與五千原款如何切割。"
      - "潘金蓮何時知道蘇清在西門府遭遇，以及知情後是否仍利用該二十八日作結算。"

  five_thousand_original_payment:
    status: "RECLASSIFIED_PENDING_RETURN_OR_JUDICIAL_ESCROW"
    actual_cash_transfer_completed: false

  tenfold_claim:
    requested_amount_taels: 50000
    status: "PLAINTIFF_CLAIM_DIRECTION_NOT_JUDGMENT"
    pan_personal_liability: "CONTESTED_NOT_ADJUDICATED"

  su_qing_status_goal:
    - "蘇清要的是可自己選客、定價、定條件、拒絕、離開之自由性工作者位置。"
    - "不是被安排返回良家，也不是自動退出風月行業。"

  aaliyah_lock:
    - "阿麗婭與蘇清分線。"
    - "阿麗婭未重新掛牌，仍保留自己決定第一次實際出閣／第一個男人之權。"

  guanzhi_high_value_governance:
    - "普通定價潘金蓮仍可管理。"
    - "涉及高額、長期、人物身體／身分之安排，須至少另一掌櫃共核；相關女性或獨立主體須本人明示同意。"
    - "精確高額門檻仍未設定。"

  pan_relisting:
    - "白御行一千兩／一夜只為潘金蓮未來合法重新掛牌且本人自願時之條件式意向價。"
    - "目前無成交、付款、預約、優先權或性同意。"

  li_pinger_identity_lock:
    - "李瓶兒不是被西門慶買入之奴婢；既有線保存為帶嫁妝再嫁／進西門家之妻妾婚姻身分問題。"

  xu_qinghe:
    - "許慎言七十二小時按摩體驗券仍有效。"
    - "本日青禾第一段服務曾因許慎言反覆坐起處理事情而被打斷／難以持續。"
    - "是否已完整扣完第一個時辰仍未被明示結算；保持 UNSETTLED。"
```

---

# 3｜PAN-STATUS21-E02｜潘金蓮身籍副冊補證

```yaml
EVENT_RECORD:
  event_id: "PAN-STATUS21-E02-SECONDARY_REGISTRY_EVIDENCE"
  state_class: "ACTIVE"
  event_axis_state: "COMPLETED_DOCUMENT_DISCOVERY"
  time: "槐月二十一日白日／V2.7 後"
  location: "觀止前堂"

  discovered_records:
    older_status_trace:
      - "較早舊錄曾見潘氏有依附／非完全自由之舊標記。"
      - "初查未找到獨立放良原件，因此一度不能下結論。"

    west_city_secondary_household_record:
      entries:
        - "武大：戶主"
        - "潘氏：妻"
      faded_red_annotation: "舊附籍銷，從夫戶。"
      later_registers:
        - "後續年度戶籍／役籍副冊將潘氏列為妻，不列奴婢。"

    post_wuda_death_property_secondary_list:
      confirmed:
        - "武松列為武大家屬／兄弟相關項目。"
        - "潘氏未被列為可繼承財物。"
        - "未見『武松承受潘氏身契』之登錄。"

  current_legal_evidence_direction:
    - "現有副冊支持：潘氏進武大家時，較早依附標記曾被官冊處理為『銷』或不再沿用。"
    - "現有官冊沒有支持『武松繼承潘金蓮身契／所有權』。"

  unknown:
    - "『舊附籍銷』最初由何人提出、依哪份原始文書辦理；原件仍未找到。"
    - "武大死後、潘金蓮後續進入西門家時究竟以正式再嫁、妾籍、其他婚書或何種文書落籍。"
    - "潘金蓮目前是否已具備可合法重新從妓／掛牌之完整身分條件。"

  prohibited_inference:
    - "不得寫成已找到完整放良原契。"
    - "不得寫成潘金蓮目前已自動取得妓籍。"
    - "不得寫成真實宋代法律必然如此；本案只屬觀止玩家線官冊證據。"
```

---

# 4｜WANGPO21-E02｜王婆收款線索新增標籤

```yaml
EVENT_RECORD:
  event_id: "WANGPO21-E02-XIMEN_PAYMENT_LABEL_XIEMEI"
  state_class: "ACTIVE"
  observed:
    - "查得西門慶曾向王婆付款。"
    - "現有帳目標籤為『謝媒』。"

  confirms:
    - "西門慶向王婆有實際金流。"
    - "該筆目前所見帳目名目為媒介／謝媒性質。"

  does_not_confirm:
    - "該筆即潘金蓮買身價。"
    - "沒有其他未查到的交易。"
    - "王婆或潘金蓮因此形成何種最終刑民責任。"
```

---

# 5｜ROKUJO-ZHANG21-E01｜六條御息所與張麗華白日進場

```yaml
EVENT_RECORD:
  event_id: "ROKUJO-ZHANG21-E01-DAY_APPEARANCE"
  status: "COMPLETED_APPEARANCE_WITH_CONTINUING_RELATION_CONTACT"
  confirmed:
    - "六條御息所以觀止提供之簡素衣物出現，較初來時安定。"
    - "張麗華與她一同進入本日場面；兩人此前有自行交談，但具體內容 UNKNOWN。"
    - "張麗華以玩笑稱觀止最離奇之處是帳，而非妖怪。"
    - "六條看到潘金蓮可能重新掛牌／身籍爭議後，真誠詢問中原高門女子是否也需查籍後才能重新從妓；造成在場人發笑，但未建立其有意侮辱潘金蓮。"

  relation_effect:
    - "六條與張麗華已有實際相處與共同出場。"
    - "不得因此固化為閨蜜、盟友或長期同一立場。"
```

---

# 6｜WHITE-JADE21-E01｜白玉池再檢與正式營運仍未恢復

```yaml
EVENT_RECORD:
  event_id: "WHITE-JADE21-E01-INFORMAL_REINSPECTION"
  status: "OBSERVED_STABLE_SURFACE_NOT_FORMALLY_REOPENED"
  participants_or_witnesses:
    - "白御行"
    - "潘金蓮"
    - "龐春梅"
    - "蘇清"
    - "李瓶兒／近場"
    - "沈萬三"
    - "青禾"
    - "六條御息所"
    - "張麗華"
    - "阿泠／池中回應"

  observable:
    - "眾人再次到白玉池查看。"
    - "既有補處未見新的明顯裂口。"
    - "水面當時平穩，未見新的明顯異常回顯。"

  current_operational_state:
    pool: "RESTRICTED_NOT_FORMALLY_REOPENED"
    second_formal_preopening_check: "NOT_RECORDED_AS_COMPLETED"
    public_spa_operation: false
    customer_admission: false

  rule:
    - "本次肉眼／現場查看不能偷換成正式復開驗收。"
    - "未完成安全、排水、材質、服務規則與正式第二檢前，不得直接開放一般客人。"
```

---

# 7｜ALING21-E01｜阿泠金錢自主與池中財產觀念

```yaml
ENTITY_STATE:
  entity: "阿泠"
  route_identity:
    - "自選名『阿泠』。"
    - "可控制白玉池水、以水霧顯出女性身形並提供水壓療法。"
    - "白玉池為她認定之自身場所。"

  money_position_confirmed_in_current_scene:
    - "阿泠認為人類銀錢／可兌換資源可讓她直接叫人清理、修繕、買材料、僱工，而不必向潘金蓮或其他人求人情。"
    - "她明示『我的水，我做工；銀子為何全讓你拿』之所有權立場。"
    - "她對『把財物留在池中、越積越多』表現出明確喜好；其價值不只在消費，也在持有與觀看。"

  human_goods_reaction:
    - "化妝品在水中不實用；衣物易濕；飾物會沉。"
    - "漂亮、耐水、能長期留在池底之特殊石料／琉璃／玉，反而符合其偏好。"

  sibling_name_lock:
    - "白御行本輪再次以『都是白姓／白玉池泠』開兄妹玩笑。"
    - "李師師當場指出：池名含白不等於阿泠自動姓白。"
    - "沿用既有硬狀態：阿泠沒有接受白姓，也沒有認白御行作哥哥。"
```

---

# 8｜WISH-COIN21-E01｜許願幣商業框架

```yaml
WISH_COIN_FRAMEWORK:
  state_class: "ACTIVE_PROPOSAL_WITH_PARTIAL_ENTITY_ACCEPTANCE"
  name: "許願幣"

  confirmed_core_architecture:
    - "客人若要在白玉池進行許願／特定 SPA 儀式，不應直接把銀錢投入溫泉。"
    - "銀直接長泡溫泉可能造成變色、腐蝕或維護麻煩，因此改由耐水代幣進池。"
    - "客人向觀止購買許願幣後，可按未來規則投入白玉池。"
    - "一旦有效投入池中，該枚許願幣屬阿泠；客人不得自行撈回，潘金蓮／觀止也不得因管理身分直接取走。"
    - "阿泠可用自己持有之許願幣向觀止購買清潔、修繕、人工、材料等服務。"
    - "若阿泠將許願幣支付回觀止，未來是否可重新發行／再售，可作循環制度設計，但本輪未完成正式條款。"

  material_direction:
    accepted_design_space:
      - "厚質琉璃／玻璃珠或琉璃餅"
      - "打磨過的漂亮特殊石頭"
      - "高價玉料／玉願幣"
    safety_requirements_discussed:
      - "圓鈍、無尖角"
      - "不得過小以免卡排水"
      - "耐熱、耐水、不易碎"
      - "正式使用前需做浸泡、摔落、邊角與溫差測試"
    not_fixed:
      - "最終材質"
      - "尺寸"
      - "顏色"
      - "普通／高價幣是否分級"
      - "實體是否使用整枚與半枚面額"
      - "正式鑄造／製作工坊"

  wish_semantics:
    - "可以許願並把價值投入池中。"
    - "阿泠未承諾願望會實現。"
    - "不得宣傳成保證靈驗之交易。"
```

---

# 9｜ALING-SERVICE21-E01｜水療與成人水身服務之價格討論

```yaml
SERVICE_DISCUSSION:
  state_class: "PROPOSAL_NOT_LAUNCHED"

  established_capability_basis:
    - "既有路線已觀察阿泠能以水流控制方向、壓力與落點，並可借霧水顯出女性身形。"

  current_scene_trial_willingness:
    - "被問及是否願以水做之身形提供成人向服務時，阿泠回應可試。"
    - "其後明確接受：不是每個客人都自動可得，是否做仍由她當次決定。"

  market_opinions_not_formal_price:
    shen_wansan:
      - "一般稀有水療可視為較低價層。"
      - "私人顯形、單客體驗價可更高。"
      - "成人水身服務他個人願意以五十兩起估；若證明獨一無二且體驗佳，一百兩亦可能有人付。"
    li_shishi_later_opinion:
      - "單純水療約十兩可接受。"
      - "私人顯形陪浴約二三十兩。"
      - "成人水療五十兩起。"

  not_fixed:
    - "觀止正式 SPA 價格"
    - "阿泠正式分成／收入分配"
    - "每次服務時長"
    - "每日客數"
    - "許願幣與銀兩正式匯率"
    - "投入幾枚許願幣才代表哪一級服務"

  consent_lock:
    - "任何服務須阿泠當次願意。"
    - "購幣、許願、付銀、過去做過水療均不等於預先取得成人服務同意。"
```

---

# 10｜ALING-DEPOSIT21-E01｜一百枚一年三枚半定存利率

```yaml
DEPOSIT_FRAMEWORK:
  state_class: "RATE_ACCEPTED_CONTRACT_NOT_YET_EXECUTED"
  parties_in_concept:
    depositor: "阿泠"
    operating_side: "觀止／潘金蓮等管理方"

  corrected_economic_model:
    - "不是把阿泠池中的許願幣撈出後再把幣借給別人。"
    - "例：阿泠若有一百枚，其中八十枚選擇一年定存，該八十枚仍屬阿泠並可留在池中。"
    - "定存期間，該八十枚被標為鎖定，阿泠暫時不能拿它們向觀止兌用服務。"
    - "因對應服務請求權被鎖定，觀止當初出售這批許願幣所得之背後銀錢／現金可在約定期間作營運資金。"
    - "觀止可自行承擔商業放貸或周轉；放貸失敗風險屬觀止，不得把到期兌付風險倒給阿泠。"

  accepted_rate:
    principal_unit: 100
    term: "一年"
    annual_interest_wish_coins: 3.5
    annual_rate_percent: 3.5
    maturity_example: "100 -> 103.5"
    benchmark_source_in_story: "白御行表示定陶商會一年期定存為一百枚／一百單位每年三枚半；阿泠接受同價位。"

  aling_explicit_terms:
    - "阿泠確認一百枚、一年、到期一百零三枚半之算法。"
    - "阿泠要求不得以修池、急事等理由騙她提前解鎖／挪用其存款權利。"
    - "阿泠明示『同意』該利率。"
    - "半枚利息也算她的；半枚如何實體化仍未定。"

  not_executed:
    - "尚未決定阿泠本次實際存入多少枚。"
    - "尚未簽書面定存契約。"
    - "尚未將任何一筆背後銀錢正式轉為放貸資金。"
    - "尚未設定備付率、提前解約、違約、幣損壞補發、存款上限。"

  governance_required_before_launch:
    - "此屬長期金融／高價值新制度，需觀止至少另一掌櫃共核。"
    - "阿泠之同意須按每筆實際存入／鎖定數量明示。"
```

---

# 11｜RIR21-E01｜白御行跪歉、李師師收下道歉並原諒

```yaml
EVENT_RECORD:
  event_id: "RIR21-E01-APOLOGY_AND_FORGIVENESS"
  location: "李師師私人房間"
  status: "COMPLETED_RELATIONAL_REPAIR_EVENT"

  player_confirmed:
    - "白御行主動到李師師門外跪下。"
    - "白御行明示自己先前在成人事件中性子急、只顧自己舒服而忽略李師師感受，承認『這事情我過分了』。"
    - "白御行也明示自己不一定馬上改，但其自我描述是會認錯、不死硬。"

  li_shishi_response:
    - "李師師指出她真正不滿不是白御行有性慾，而是他已知道她有感受，卻在急時把已知邊界丟到後面。"
    - "她不接受用『我不是那個意思』、『她也享受』或男人天性作卸責。"
    - "她認為真正驗證點是下一次白御行急時能否仍記得床上有第二個人。"
    - "後續她明示：『原諒了。』"
    - "她同時說原諒不等於忘記；若再犯仍會處理。"

  relation_effect:
    apology_received: true
    forgiveness_explicit: true
    past_event_erased: false
    automatic_future_consent: false
```

---

# 12｜RIR21-E02｜『我愛你』之現行狀態

```yaml
RELATIONSHIP_STATE:
  relation_id: "BAI_LI_SHISHI_LOVE21"
  state_class: "ACTIVE"
  confirmed:
    - "白御行再次明示：『我愛你』是真的，不是射精後的床上話。"
    - "李師師明示她相信這句是真的。"
    - "李師師仍未在本輪直接回以『我愛你』。"
    - "她表示若將來說，必須是自己當時真想說，不接受白御行替她預先指定台詞。"

  interpretation_limit:
    - "相信告白是真的，不等於李師師已作對稱愛情告白。"
    - "不得補寫她已永久排他、已結婚或已完成白家正式登記。"
```

---

# 13｜RIR21-E03｜李師師如夫人位置再次明示與住處安排

```yaml
RELATION_FRAME:
  event_id: "RIR21-E03-RU_FUREN_RECONFIRM_AND_RESIDENCE"
  state_class: "ACTIVE_ORALLY_ACCEPTED_NOT_PUBLICLY_IMPLEMENTED"

  li_shishi_explicit:
    - "被白御行直接問『真的想要如夫人的位置嗎』時，李師師回答『想』。"
    - "她明示不是因今天被道歉跪軟，也不是把如夫人當補償；她本來就想要。"
    - "她要的是被真正放進白御行的家，不是只拿一塊牌子。"
    - "她保留自己的房、錢、物品、唱曲、設席、是否見客等生活自主。"

  residence:
    - "白御行目前在京師無自宅，老家在定陶。"
    - "李師師現階段不想被單獨送回定陶；她認為白御行若人在京師而自己被送回定陶，近似被安置／發配。"
    - "因此她同意現階段繼續住觀止，生活照舊。"
    - "她明示：住觀止只是住處，不代表如夫人名分尚未成立／要等有宅子才承認。"

  public_implementation_not_observed:
    - "尚未正式公告觀止全體／外界。"
    - "尚未登白家名冊、官府文書或舉行儀式。"
    - "是否需要何種宋代／觀止法定程序仍未設定。"
```

---

# 14｜RIR-PINGER21-E01｜李瓶兒未來如夫人並列原則

```yaml
FUTURE_HOUSEHOLD_FRAME:
  state_class: "CONDITIONAL_FUTURE_FRAME_ACCEPTED_BY_LI_SHISHI"

  player_disclosure_to_li_shishi:
    - "白御行告知：李瓶兒曾表示想要正妻位置。"
    - "白御行已對李瓶兒說正妻不行，只能如夫人。"
    - "白御行已答應：等李瓶兒與西門慶之身分／法律問題乾淨後，若她仍願意，可讓她成為如夫人。"
    - "白御行提出：李師師與李瓶兒若同為如夫人，彼此不按進門先後壓對方一頭；爭議時他主張論事理、不論先後。"

  li_shishi_response:
    - "李師師明示能接受李瓶兒。"
    - "她接受同為如夫人不排大小、不以先後壓人。"
    - "她要求能由兩個女人自己談的先自行談，不希望所有爭議都變成等白御行判案。"
    - "若牽涉共同財產、住處、孩子、對外名分或談不攏，再由白御行介入。"
    - "她認為白御行自己也受『不因偏愛某人便突然把她升成比較大』之規則約束。"
    - "她願意未來白御行正式與李瓶兒談如夫人時在場，以表明自己不是等著爭大小位置。"

  li_pinger_status:
    - "李瓶兒本人尚未在本輪對『與李師師並列』完成新的正式確認。"
    - "其西門家身分／文書仍需另查。"
    - "不得把李師師接受她，寫成李瓶兒已正式入白家如夫人。"
```

---

# 15｜DINNER21-E01｜李師師今晚請李瓶兒吃飯

```yaml
EVENING_DINNER:
  state_class: "SCHEDULED_PRIVATE_DINNER"
  host: "李師師"
  invited_guest: "李瓶兒"
  white_yuxing_present: true
  location: "李師師私人房間／小席"

  redniang_message_result:
    li_pinger_initial_answer: "都可以"
    after_followup_preferences:
      - "不要太油"
      - "清蒸魚"
      - "一碟筍"
      - "一碟嫩菜"
      - "清湯"
      - "若有新鮮蓮子，可做少糖甜湯"
      - "酒不用多"

  li_pinger_question:
    - "『只是吃飯嗎？』"
  redniang_answer:
    - "師師設宴、白爺也在；其餘不能替三人決定。"
  li_pinger_final:
    - "『那我晚上來。先吃飯。』"

  consent_boundary:
    - "今晚確定只有吃飯邀請與到席意願。"
    - "李師師表示自己不排斥三人親密。"
    - "白御行與李師師不能替李瓶兒把晚宴後留宿／同床／性行為排好。"
    - "是否成為三人床局，必須由李瓶兒在當晚自行明示。"
```

---

# 16｜REDNIANG21-E01｜紅娘氏得知假設三人題的答案

```yaml
KNOWLEDGE_EVENT:
  event_id: "REDNIANG21-E01-LEARNED_HYPOTHETICAL_THIRD_CHOICE"
  status: "COMPLETED_PRIVATE_DISCLOSURE"
  knows:
    - "白御行"
    - "李師師"
    - "紅娘氏"

  confirmed:
    - "白御行把紅娘氏叫進李師師房中。"
    - "白御行告知：此前他問李師師若在觀止選一人與兩人一起雙飛，李師師當時選過紅娘。"
    - "李師師承認自己曾作此假設回答。"

  does_not_establish:
    - "紅娘氏已被正式邀請。"
    - "紅娘氏已同意三人親密。"
    - "已約時間或場景。"
    - "李師師與紅娘氏已發生性關係。"
```

---

# 17｜RIR-LANGUAGE21-E01｜粗口、低俗與低賤之私人語言邊界

```yaml
PRIVATE_LANGUAGE_SELF_REPORT:
  state_class: "ROUTE_SELF_DESCRIPTION_NOT_BASELINE_OVERRIDE"
  li_shishi_explained:
    - "粗口主要是字詞直接／髒／硬。"
    - "低俗主要是題材、身體、性與不登大雅之堂的直接趣味。"
    - "低賤主要涉及人在話語中被放到低位、失去資格／選擇或自我貶抑的位置。"
    - "她可以自然說粗口與低俗話。"
    - "低賤不是她的預設；若出現，只能在她自己願意把它當床上角色／玩法時成立，不能被拿來定義她。"
    - "她認為自己比蘇清、張麗華更依賴反差：平常收著，真失控時才可能漏出粗話。"

  anti_backflow:
    - "不得把本輪玩笑式『戰鬥力排行』寫成人物固定數值或人物卡屬性。"
    - "李瓶兒『毫無戰力』只屬現場調笑，不是她的永久成人語言能力判定。"
```

---

# 18｜RIR21-E04｜足部親密事件與停止／再問修正

```yaml
INTIMACY_EVENT:
  event_id: "RIR21-E04-FOOT_INTIMACY_WITH_REASK"
  state_class: "COMPLETED_PRIVATE_INTIMACY"
  participants:
    - "白御行"
    - "李師師"

  sequence:
    - "白御行先自行褪去李師師鞋襪並開始足部口部親密。"
    - "李師師即時指出：才剛認錯，不應再次先做再問；要求停下並重新詢問。"
    - "白御行重新詢問右腳先、程度多深。"
    - "李師師明示右腳先、先輕一點，並重申她收腳即停。"
    - "白御行其後按她允許的方式進行右腳足部親密。"
    - "完成後白御行要求另一隻；李師師另行明示左腳也可以、規矩相同。"
    - "雙腳足部親密其後完成；未記錄受傷。"

  consent_effect:
    - "本事件再次形成清楚的『每一新增行動須按當下允許』實例。"
    - "李師師允許足部親密，不延伸為其他身體部位或後續性行為的自動同意。"
```

---

# 19｜RIR-ANKLET21-E01｜腳環與鈴鐺構想

```yaml
OBJECT_PROPOSAL:
  state_class: "AGREED_DESIGN_IDEA_NOT_ORDERED"
  object: "李師師私人腳環"
  discussed_features:
    - "細、小、適合戴在腳腕／小腿下段。"
    - "帶小鈴鐺；聲音只要輕微，不要像廟會。"
    - "不做成鎖鏈感。"
    - "外側不刻『白御行的』。"
    - "內側可刻只有兩人懂的話。"
  playful_inscription_candidate:
    - "白御行提：拔屌無情。"
    - "李師師接受可以小刻在內側，並提出對應句：事後跪好。"

  status:
    manufactured: false
    ordered: false
    material_fixed: false
    delivery_due: false
```

---

# 20｜RIR-IMAGE21-E01｜煙青色肚兜私人畫像

```yaml
PRIVATE_IMAGE_EVENT:
  state_class: "COMPLETED_PRIVATE_DISPLAY"
  prior_object_basis:
    - "槐月十八日七色肚兜分贈時，李師師先選煙青色。"

  current:
    - "白御行向李師師展示一張她穿煙青色肚兜的私人畫像／圖像版本。"
    - "李師師認為該版比先前更刺激，私房意味更強，並再次肯定煙青色適合自己。"
    - "她允許白御行留存。"
    - "她以玩笑但清楚的私人界線表示不希望白御行拿給紅娘看。"

  not_established:
    - "該畫像已公開。"
    - "已交紅娘或其他人觀看。"
    - "畫像內容自動成為李師師日常固定穿著。"
```

---

# 21｜RIR21-E05｜跪歉結束與晚宴前相擁休息

```yaml
EVENT_RECORD:
  event_id: "RIR21-E05-APOLOGY_CLOSE_AND_REST"
  status: "ACTIVE_REST_SCENE"

  confirmed:
    - "李師師明示本次道歉她收了、也原諒了。"
    - "她讓白御行結束跪姿、起身。"
    - "白御行起身抱她，兩人談到煙青色肚兜與私人畫像。"
    - "白御行提出先休息、準備晚上；要李師師陪睡。"
    - "李師師同意休息，先上榻並留出位置。"
    - "白御行上榻，李師師主動靠在他胸前／腰側相擁。"
    - "她把目前定義為休息／睡覺，沒有建立休息期間自動性行為。"

  current_hold:
    - "場景停在兩人準備睡覺／休息，尚未演出睡醒。"
    - "不得直接跳到晚上或替白御行完成起床、赴宴。"
```

---

# 22｜ACTIVE_RELATIONSHIP_STATES｜當前關係硬狀態

```yaml
ACTIVE_RELATIONSHIPS:
  bai_li_shishi:
    state_class: "ACTIVE"
    state_label: "FORGIVEN_APOLOGY_RU_FUREN_ORALLY_RECONFIRMED_PRIVATE_INTIMACY_ACTIVE"
    established:
      - "多次自願成人親密之既有關係"
      - "白御行對李師師的愛情告白"
      - "李師師相信該告白是真"
      - "李師師再次明示想要如夫人位置"
      - "現階段住觀止不改其生活自主"
    unresolved:
      - "李師師何時／是否直接回以愛的告白"
      - "如夫人對外公告／家冊／法律實施方式"
      - "未來京師若置宅，她是否搬入"

  bai_li_pinger:
    state_class: "ACTIVE_UNRESOLVED_FUTURE_HOUSEHOLD"
    current:
      - "白御行曾允諾：待其與西門慶身分問題乾淨，若她仍願意，可談如夫人。"
      - "今晚李瓶兒只同意來吃飯。"

  li_shishi_li_pinger:
    state_class: "POTENTIAL_FUTURE_COEQUAL_HOUSEHOLD_FRAME"
    confirmed:
      - "李師師明示可接受李瓶兒未來與她並列如夫人。"
    not_confirmed:
      - "李瓶兒已同意與李師師並列。"
      - "兩人已形成姐妹／盟友／性關係。"

  bai_aling:
    state_class: "ACTIVE_FAMILIAR_NONFAMILY"
    confirmed:
      - "白御行熟悉阿泠且關注其水療／商業開發。"
    prohibited:
      - "不得寫成兄妹已成立。"
      - "不得寫成白御行擁有阿泠或白玉池。"
```

---

# 23｜ACTIVE_CONTRACTS_AND_DUE_ITEMS｜契約與到期事項

```yaml
ACTIVE_CONTRACTS_AND_DUE:
  guanzhi_civil_case:
    - "蘇清 vs 潘金蓮民事／帳務案仍 ACTIVE。"
    - "五千原款待返還／司法保全未完成現金交付。"
    - "五萬賠償仍僅請求方向。"

  pan_status:
    - "下一輪可繼續查潘金蓮進西門家之婚姻／妾籍／改籍文書。"

  white_jade_pool:
    - "第二次正式復開檢查仍需完成。"
    - "許願幣材質與安全測試需確定。"
    - "銀兩／許願幣匯率未定。"
    - "SPA 服務單位、價格、時間、阿泠分成未定。"
    - "定存正式契約、實際存入枚數、備付與放貸規則未定。"

  xu_massage:
    - "七十二小時按摩體驗券仍在；第一段是否完整扣時未結算。"

  evening_dinner:
    - "今晚李師師房內小席：李師師、李瓶兒、白御行。"
    - "飯後是否有任何成人親密必須當場重新取得三人各自同意。"
```

---

# 24｜KNOWLEDGE_AND_PRIVACY｜知情與私人邊界

```yaml
KNOWLEDGE_MATRIX:
  pan_registry_new_evidence:
    broad_current_scene_knowledge:
      - "白御行"
      - "潘金蓮"
      - "蘇清"
      - "龐春梅"
      - "李瓶兒"
      - "許慎言／法律處理範圍"
      - "在場參與文書討論者"
    public_state: "NOT_AUTOMATICALLY_PUBLIC"

  aling_wish_coin_and_deposit:
    knows_or_participated:
      - "白御行"
      - "潘金蓮"
      - "龐春梅"
      - "蘇清"
      - "李瓶兒／近場"
      - "沈萬三"
      - "青禾"
      - "六條御息所"
      - "張麗華"
      - "阿泠"
    public_product_state: "NOT_LAUNCHED"

  li_shishi_apology_and_household_talk:
    strict_private_core:
      - "白御行"
      - "李師師"
    redniang_partial:
      - "知道白御行在師師房中跪歉／被叫進出。"
      - "知道師師曾在假設三人題中選她。"
      - "未必知道如夫人與李瓶兒全部談判細節。"

  evening_dinner:
    knows:
      - "白御行"
      - "李師師"
      - "李瓶兒"
      - "紅娘氏／跑腿備席範圍"

  foot_intimacy_and_image:
    public_state: "STRICTLY_PRIVATE_BETWEEN_BAI_AND_LI_SHISHI_UNLESS_LATER_DISCLOSED"
```

---

# 25｜UNKNOWN／UNDECIDED｜本 HOT 必須保持未決

```yaml
UNRESOLVED:
  - "潘金蓮進西門家後之最終法律身分與現今可從妓資格。"
  - "『舊附籍銷』原始申請文書／辦理人。"
  - "王婆金流是否還有其他筆、是否涉及另種契約。"
  - "蘇清 vs 潘金蓮最終判決與賠償。"
  - "五千原款最終返還對象與實際交付時間。"
  - "白玉池第二次正式復開驗收結果。"
  - "許願幣最終材質、面額、匯率、SPA 消耗枚數。"
  - "阿泠實際第一筆定存存入數量與正式契約。"
  - "阿泠每天願意服務幾客；任何客數玩笑不得固化。"
  - "今晚李瓶兒吃飯後是否留下。"
  - "今晚是否形成三人親密。"
  - "李師師如夫人何時正式公開／登記。"
  - "李瓶兒日後是否在身分清理完成後仍選擇如夫人。"
  - "腳環是否真的製作。"
  - "白御行與李師師本次休息睡多久、誰先醒。"
```

---

# 26｜FORBIDDEN_INFERENCES｜禁止回歸與反污染

```yaml
FORBIDDEN_INFERENCES:
  - "不得把『舊附籍銷，從夫戶』直接擴寫成已找到完整放良原契。"
  - "不得寫武松曾依法繼承潘金蓮身契；目前恰恰沒有官冊支持。"
  - "不得因身籍補證就直接讓潘金蓮重新掛牌。"
  - "不得把王婆『謝媒』帳目改寫為明確買身價或反過來證明完全沒有買身交易。"
  - "不得把白玉池目前表面穩定寫成已正式營業。"
  - "不得讓普通客人直接進池或自動取得阿泠服務。"
  - "不得把許願等同保證靈驗。"
  - "不得把投入池中的許願幣視為潘金蓮／觀止可任意撈取的公款。"
  - "不得把定存模型錯寫成『觀止把阿泠的幣撈出借給客人』。"
  - "不得寫阿泠已完成一百枚或八十枚的實際存款；那些只是模型例子。"
  - "不得因阿泠接受 3.5% 利率便推定完整金融契約已簽署。"
  - "不得把白御行稱阿泠妹妹／白玉池泠寫成阿泠已認親或接受白姓。"
  - "不得因李師師原諒白御行，就抹除前次停止／忽視感受事件。"
  - "不得因如夫人口頭再確認就寫成已完成對外婚姻法定程序。"
  - "不得把李師師接受李瓶兒並列，寫成李瓶兒已同意或已成如夫人。"
  - "不得把今晚吃飯自動演成三人床局。"
  - "不得把紅娘知情寫成紅娘已接受參與三人性行為。"
  - "不得把成人語言玩笑排行寫進人物卡基線。"
  - "不得把足部親密之當次同意延伸為永久身體資格。"
  - "不得自動製作、購買或戴上腳環；目前只到設計構想。"
  - "不得把私人煙青色肚兜畫像公開給紅娘或其他人，除非後續事件實際發生。"
```

---

# 27｜MASTER_LOOKUP_INDEX｜需要厚歷史時的查詢索引

```yaml
MASTER_LOOKUP_INDEX:
  long_term_master:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.1-R1_截至HOT_V1.9固化整合版.md"
    use_for:
      - "白御行長期身份、關係與早期因果"
      - "白玉池早期事件 E59-E60"
      - "李師師較早關係線與既有私密事件"

  recent_hots:
    HOT_V2_2:
      use_for:
        - "白玉池第一輪復開檢查"
        - "李師師如夫人前置"
        - "煙青色肚兜分贈"
    HOT_V2_3:
      use_for:
        - "沈萬三等擴大白玉池知情"
        - "第二輪檢查仍未記錄"
    HOT_V2_4_TO_V2_7:
      use_for:
        - "蘇清／潘金蓮五千後算民事案"
        - "阿麗婭身分"
        - "觀止治理"
        - "潘金蓮身籍查核前置"
        - "許慎言／青禾服務"

  persona_source:
    file: "觀止人物卡池_LCAPG_V2.1_青禾六條增補_原版20人鎖定_補充人物擴充正式版.md"
    use_for:
      - "人物人格與跨線基線"
      - "六條御息所與青禾之人物卡"
      - "紅娘氏與李師師之補充人物卡"
```

---

# 28｜下一幕自然接關

```yaml
CONTINUATION_POINT:
  primary_scene: "李師師私人房間／白日休息"
  state:
    - "白御行與李師師剛結束跪歉與談話，已同榻相擁準備休息。"
    - "李師師已原諒；如夫人意願再次明示。"
    - "晚宴尚未開始，李瓶兒尚未到席。"

  next_natural_world_beats:
    - "休息一段時間後自然醒來，但不得跳過整個下午或直接到晚宴高潮。"
    - "晚宴前紅娘／廚下可送一次備席確認，不必替白御行起身赴宴。"
    - "白玉池線在另一處可由春梅／沈萬三／蘇清整理許願幣匯率與定存草案，但在正式簽約、鑄幣或放貸前需重新取得必要管理方與阿泠確認。"
    - "潘金蓮身籍線可離鏡頭繼續查西門家婚書／戶籍，但結果需以新文書事件帶回，不得旁白偷定。"

  hard_stop_conditions:
    - "李瓶兒晚宴後是否留下／加入任何親密。"
    - "李師師如夫人正式公告／簽署／登記。"
    - "阿泠實際定存數量與正式金融契約。"
    - "白玉池正式復開。"
    - "任何新的高額付款、長期契約或身體資格。"
```

---

# 29｜一句接關摘要

> **槐月二十一日白日，潘金蓮身籍查得「舊附籍銷，從夫戶」與妻籍副冊，武松繼承身契暫無官冊支持；白玉池仍未正式復開，但阿泠已取得許願幣所有權框架並接受一年期 3.5% 定存利率，正式匯率與契約仍未落定。白御行其後到李師師房中跪歉，李師師明示原諒、再次確認想要如夫人並接受未來與李瓶兒並列；李瓶兒已答應今晚來吃飯但只承諾「先吃飯」。目前白御行與李師師已同榻相擁休息，下一幕從晚宴前醒來或世界送入一個白日進展接起。**

<!-- PROMOTED_HOT_SOURCE_END: 觀止青樓_白御行線_HOT_SAVE_V2.8_槐月二十一日白日_潘身籍補證_白玉池許願幣定存_師師如夫人確認與晚宴前休息版.md -->

---

# APPENDIX E｜固化來源全文：觀止青樓_白御行線_HOT_SAVE_V2.9_槐月二十一日深夜_曹州假印立案_定陶總會架構_京師女裝企畫與師師抱睡版.md

> **法位：E84–E92 細節追溯來源。** 此 HOT 內的 CURRENT_SCENE／HOLD 只代表當時快照；不得覆寫本 MASTER 截止或 V3.5–V3.7 疊加層。若原 HOT 內某個標成 YAML 的區塊本身語法不合法，本 MASTER 只把該 fence 改標為 text 隔離，內容原文不改，避免來源語法缺陷破壞 MASTER 解析。

<!-- PROMOTED_HOT_SOURCE_BEGIN: 觀止青樓_白御行線_HOT_SAVE_V2.9_槐月二十一日深夜_曹州假印立案_定陶總會架構_京師女裝企畫與師師抱睡版.md -->
# 觀止青樓｜白御行線 HOT SAVE V2.9
## 理火三年槐月二十一日深夜｜曹州假印立案 × 定陶總會架構明示 × 京師女性奢侈品／肚兜發表會企畫 × 風月接戲試跑 × 師師抱睡接關版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V2_9_HUAI21_LATE_NIGHT_FAKE_SEAL_ASSOCIATION_ARCHITECTURE_WOMENS_LUXURY_SHOW_HUG_SLEEP"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V2.9"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V11.0-R2"
  character_source: "觀止人物卡池_LCAPG_V2.1"
  story_date: "理火三年槐月二十一日"
  time_of_day: "深夜／就寢；精確時刻未知"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AT_LI_SHISHI_PRIVATE_ROOM_NONSEXUAL_HUG_SLEEP"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V2.8_槐月二十一日白日_潘身籍補證_白玉池許願幣定存_師師如夫人確認與晚宴前休息版.md"
  previous_hot_sha256: "b71874cdeedf061fcc58d11e4c87a798e493d39498e5a5b1ede028e6d87fbeae"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"
  current_experimental_overlay:
    file: "觀止青樓_PATCH_風月角色表演與接戲能力_V0.1-EXP_獨立試跑未併主系統.md"
    sha256: "23cae60daec8f7f7ba24f2664dfe522c1a5ce1723d52d7eff1e66ca35c9de773"
    status: "INDEPENDENT_TRIAL_OVERLAY_NOT_MERGED_TO_MAIN_SYSTEM"
  save_scope:
    - "HOT V2.8 晚宴前休息後至本次就寢之直接玩家線事件"
    - "李瓶兒晚宴到場、吃飯界線與未形成後續成人同意"
    - "白御行三歲半照護戲與接戲故障審計後之獨立 PATCH 試跑狀態"
    - "曹州程姓商人遭冒用定陶商會印樣之案件立案與商會內部移交"
    - "定陶商會／總會／商團之在場組織架構明示與顧青簡確認"
    - "顧青簡作為白御行線新增商會師爺之命名與路線人物狀態"
    - "京師女性奢侈品旗艦店、批發端與定陶肚兜發表會之企畫方向"
    - "觀止人物款肚兜、疏影候選主設計、六條條件式走秀、外邀名單"
    - "白御行夜間明示疲累、要求李師師擁抱且不要挑逗；李師師接受"
```

---

# 0｜提交法位、來源與反污染說明

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V2.8_槐月二十一日白日_潘身籍補證_白玉池許願幣定存_師師如夫人確認與晚宴前休息版.md"
    role: "本檔直接前置 HOT；V2.8 及以前有效硬狀態全部繼承"

  master_archive:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"
    role: "截至 HOT V2.5 之長期因果；V2.6-V2.8 由前置 HOT 繼承"

  current_route_conversation_commit:
    role: "HOT V2.8 後至本次 HOT SAVE 命令前之直接劇情事件、玩家明示自身言行、NPC 可觀察回應與已完成路線命名"

  experimental_performance_patch:
    file: "觀止青樓_PATCH_風月角色表演與接戲能力_V0.1-EXP_獨立試跑未併主系統.md"
    role: "本路線接戲／表演能力試跑治理；不是世界內事件，不得倒灌人物履歷"

COMMIT_NOTE:
  - "本檔取代 HOT V2.8，成為白御行線當前直接接關切片；V2.8 保留為前置歷史來源。"
  - "本次只更新 HOT；不更新 MASTER，不修改人物卡池或主程序基線。"
  - "白御行在故事中對定陶商會架構的說明由具職權玩家角色提出，並有顧青簡多處當場確認；本 HOT 保存為本玩家線現行組織硬狀態／知情內容，但不自動升格為跨線 BASELINE_CANON。"
  - "京師女性奢侈品店與肚兜發表會目前均屬企畫／方向；尚無場租契約、店面簽約、正式預算、模特合約或量產授權。"
  - "『官府報備過之成年女子可參與舞台表演』為白御行在場提出的活動法律／操作假設；本輪未見官府正式核准文件，故不得寫成已取得法律許可。"
  - "李瓶兒今晚只完成赴席、吃飯與同行至大堂等事件；未成立留宿、三人性行為或隔日去她家睡之承諾。"
  - "白御行的『三歲半』屬自願戲中角色／照護表演；不得倒灌成實際年齡、身分或人物履歷。"
  - "三歲半角色框架中本輪只成立非性照護／餵飲／哄睡；不得將兒童角色框架與成人性內容混接。"
  - "白御行最後明示疲累並要求『師師抱抱、晚上不要挑逗我』；此為今晚直接有效之玩家邊界。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年槐月二十一日"
  time: "深夜／就寢；精確時刻未知"
  location: "觀止青樓／李師師私人房間／榻上"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  player:
    name: "白御行"
    current_position: "李師師私人房間／榻上"
    current_hard_state:
      - "已結束本日晚宴、前堂商會插曲與女裝企畫討論。"
      - "明示：這幾天有點累。"
      - "向李師師要求抱抱。"
      - "明示今晚不要挑逗自己。"
      - "目前沒有提出任何新的成人性行為要求。"
    next_action_owner: "WORLD_OR_PLAYER_AFTER_SLEEP_OR_NEXT_MORNING"

  li_shishi:
    current_position: "自己房內／榻上抱著白御行"
    current_state:
      - "已接受白御行今晚只要擁抱與陪睡之要求。"
      - "已明示今晚不挑逗、不談商會與肚兜等公事。"
      - "目前場景為非性安撫／相擁休息。"

  li_pinger:
    current_position: "已離開李師師房／本幕不在場"
    current_state:
      - "今晚赴李師師之邀吃飯。"
      - "晚宴後未成立留宿或三人親密。"
      - "白御行曾說明天去她家睡；李瓶兒未答應睡宿，只表示明天醒後再問，若只是吃飯／玩一會可商量。"
```

---

# 2｜INHERITED-ACTIVE21｜V2.8 仍有效之核心硬狀態

```yaml
INHERITED_ACTIVE_HARD_STATE:
  pan_status:
    - "潘金蓮身籍副冊已查得『舊附籍銷，從夫戶』與後續妻籍方向。"
    - "目前官冊沒有支持武松繼承潘金蓮身契。"
    - "潘金蓮進西門家後之最終法律身分與目前可否合法重新掛牌仍未定。"

  su_qing_vs_pan:
    - "蘇清與潘金蓮民事／帳務案仍 ACTIVE。"
    - "五千原款待返還／司法保全；五萬仍為索賠請求方向，不是判決。"

  white_jade_pool:
    - "白玉池仍未正式復開。"
    - "阿泠許願幣所有權框架有效。"
    - "阿泠接受一年期 3.5% 定存利率概念，但未有實際存入數量、完整契約或放貸。"
    - "阿泠未接受白姓／妹妹／白家人身分。"

  li_shishi:
    - "李師師已明示原諒白御行先前道歉所涉事件。"
    - "李師師再次明示想要如夫人位置。"
    - "如夫人尚未對外公告、登記或完成法定程序。"
    - "李師師接受未來在李瓶兒身分清理且瓶兒本人仍願意之前提下，兩人可並列如夫人、不以先後壓人。"

  li_pinger:
    - "李瓶兒不是西門慶買入之奴婢。"
    - "其與西門慶之最終法律／婚姻身分仍待查。"
    - "未因本晚宴自動取得或失去任何成人親密資格。"
```

---

# 3｜DINNER21-E02｜晚宴到場、三歲半戲與李瓶兒界線落地

```yaml
EVENT_RECORD:
  event_id: "DINNER21-E02-PINGER_ARRIVAL_CHILDPLAY_DINNER_BOUNDARY"
  lifecycle_state: "COMPLETED"
  event_axis_state: "DINNER_COMPLETED_NO_SEXUAL_ESCALATION"
  time: "槐月二十一日傍晚至晚間"
  location: "李師師私人房間／其後觀止大堂"

  sequence:
    - "白御行與李師師午後休息至傍晚。"
    - "紅娘氏通知李瓶兒將到。"
    - "李瓶兒帶蓮子湯／食盒前來。"
    - "白御行以『奶瓶兒』『三歲半』等稱呼與行為進入非性照護戲。"
    - "李瓶兒再次明示自己今天是來吃飯的。"
    - "白御行接受被餵食等非性照護表演，並把此種完全被餵食的形式戲稱為『殘廢餐』。"
    - "晚宴／吃飯完成後，白御行要求李師師與李瓶兒陪同前往觀止大堂。"

  consent_and_relation:
    - "李瓶兒先前『先吃飯』之界線得到實際履行。"
    - "本晚宴沒有觀察到李瓶兒同意留宿、三人同床或性交。"
    - "李師師此前對三人親密的開放態度沒有替代李瓶兒本人決定。"

  performance_note:
    - "三歲半為戲中角色；餵食、奶瓶／乳飲、被照護等只在非性表演框架成立。"
```

---

# 4｜PERFORMANCE21-E01｜接戲能力故障審計與獨立 PATCH 試跑

```yaml
ROUTE_GOVERNANCE_NOTE:
  event_id: "PERFORMANCE21-E01-ROLEPLAY_BREAK_AUDIT_AND_PATCH_TRIAL"
  world_event: false
  mode_origin: "DISCUSSION_AUDIT_BETWEEN_STORY_SEGMENTS"
  status: "EXPERIMENTAL_OVERLAY_ACTIVE_FOR_TRIAL"

  observed_problem:
    - "在白御行要求『三歲半／被照護』角色遊戲時，多名 NPC 曾反覆以『你其實不是小孩』等方式拆戲。"
    - "玩家指出：風月場人物可自願迎合／接戲，而不應把表演等同真心、人格改變或人物污染。"

  repair_applied:
    file: "觀止青樓_PATCH_風月角色表演與接戲能力_V0.1-EXP_獨立試跑未併主系統.md"
    core:
      - "人物主權不等於不迎合。"
      - "迎合不等於真心。"
      - "表演不等於人物污染。"
      - "NPC 一旦自願接戲，除非有實際退出原因，不應反覆拆穿戲框。"
      - "PERFORMANCE／真實情感／真實關係／同意分軸。"

  current_trial_limit:
    - "PATCH 未併主系統、未修改人物卡。"
    - "三歲半／兒童角色戲只允許非性照護、餵食、哄睡等內容；若要回成人性內容，先退出兒童角色框架。"
```

---

# 5｜HALL21-E01｜大堂三歲半社交戲

```yaml
EVENT_RECORD:
  event_id: "HALL21-E01-CHILDPLAY_SOCIAL_COMEDY"
  lifecycle_state: "COMPLETED"
  event_axis_state: "STAGED_SOCIAL_COMEDY"
  location: "觀止大堂"

  confirmed:
    - "白御行以三歲半戲稱潘金蓮『金蓮奶奶』、龐春梅『春梅婆婆』、紅娘氏『紅娘姊姊』、張麗華『麗華阿姨』、六條御息所『六條嬸嬸』。"
    - "現場形成公開玩笑與社交尷尬喜劇。"
    - "白御行後來明示暫時恢復正常／成人狀態，並進入商會與商品企畫討論。"

  anti_backflow:
    - "上述親屬稱謂只屬當時接戲，不形成真實親屬關係。"
    - "不得把三歲半年齡寫入玩家真實年齡。"
```

---

# 6｜CAOZHOU21-E01｜曹州程姓商人假印案進場

```yaml
EVENT_RECORD:
  event_id: "CAOZHOU21-E01-FAKE_DINGTAO_SEAL_CREDIT_CASE"
  lifecycle_state: "ACTIVE"
  event_axis_state: "FORMALLY_OPENED_AND_HANDED_TO_ASSOCIATION"
  time: "槐月二十一日晚間"
  location: "觀止大堂"

  external_merchant:
    identity: "程姓曹州商人；名字未給"
    brought:
      - "貨單"
      - "疑似定陶商會印樣拓本"
      - "半枚／破損封蠟"
    report:
      - "有人自稱『定陶商會外路採辦』，持印樣在曹州數家商號取貨／賒貨。"
      - "涉及貨值約一百七十餘兩。"
      - "程商人懷疑印樣不對，認為印章樣式過肥。"

  player_response:
    - "白御行判定該印不是定陶商會之印。"
    - "命通知商會師爺，正式立案，按既有 SOP 啟動內查。"
    - "指出曹州距總會／核心近，可由既有商會機制直接處理；觀止眾女無須介入偵查。"
    - "若程商人因一百七十餘兩損失造成短期流動性困難，可依規向商會申請營運資金融通。"
    - "白御行向程商人表達：對真心與定陶合作之商家，商會不會因單一事故放任其倒下；但資金處理仍可走貸款／投資等正常帳務，不等於慈善贈與。"
    - "白御行書面指示：先立案；安排程商人在京師之住宿／可住商會客房；查清後回報；非緊急事項照常規程序，不必事事送會長。"

  merchant_response:
    - "程商人表示目前不至於立即倒閉，但當月周轉偏緊。"
    - "若需要會按程序申請，不把融通視為白送。"
```

---

# 7｜GU_QINGJIAN21-E01｜商會師爺顧青簡命名與案件接手

```yaml
ROUTE_NPC_STATE:
  npc_id: "GU_QINGJIAN_ROUTE_SCRIBE"
  name: "顧青簡"
  role: "定陶商會／總會女性師爺；白御行線新增路線 NPC"
  baseline_scope: "ROUTE_ONLY_NOT_CHARACTER_POOL"
  naming_source: "玩家明示要求為師爺取名，導演完成命名"

  observed_traits_in_scene:
    - "辦事乾脆、熟悉流程、語氣乾而不失幽默。"
    - "對白御行日常怪異行為已有一定耐受；以『不影響簽字／別改我流程』作判準。"
    - "不需要觀止人物替商會調查。"

  case_actions_confirmed:
    - "顧青簡到場時表示案件編號已開。"
    - "曹州方面通知已送往相關節點／總會流程。"
    - "內部調查按既有規則進行。"
    - "程商人客房正在安排。"
    - "她已閱讀白御行書面指示。"
    - "無緊急情形不會把日常案件不斷送到白御行面前。"

  prohibited_inference:
    - "不得因命名即自動加入正式人物卡池。"
    - "不得補寫其出身、年齡、婚姻、私人關係或與白御行之舊史。"
```

---

# 8｜DINGTAO-STRUCTURE21-E01｜五大商團、總會與地方自主架構

```yaml
ORGANIZATION_DISCLOSURE:
  event_id: "DINGTAO-STRUCTURE21-E01-ASSOCIATION_ARCHITECTURE_DISCLOSED"
  status: "ROUTE_EFFECTIVE_CONFIRMED_IN_SCENE_NOT_BASELINE_MERGE"
  primary_source_in_story: "白御行"
  in_scene_confirmation: "顧青簡多處確認／修正表述"

  core_structure:
    - "『定陶商會』不是一個所有分支逐級聽命的單體公司。"
    - "最初核心班底為五大商團；各有主要勢力範圍與自身經營責任。"
    - "五大商團彼此可跨區插旗／投資；進入他團主要地盤時，依當地制度支付稅費／費用。"
    - "五大商團之外，後續已有海外殖民商團等新商團。"
    - "新／海外商團原則上在當地自行處理日常經營，不需凡事回報總會。"
    - "各商團自籌資金、自負盈虧，屬可獨立作戰之經營單位。"
    - "一團研發之新技術／產品可授權其他團使用；使用方支付權利金／授權費給研發方。"

  central_association_role:
    - "總會不負責替每個地方商團做日常決策。"
    - "總會掌握／維護跨團共用的運輸線、通路、信用、跨市場連接與部分技術／授權網。"
    - "架構越大，若所有事都送總部，管理成本會隨層級膨脹，因此地方自主是擴張前提。"
    - "總部真正價值之一是讓人、貨、信、帳能跨商團流動，而不是把各商團變成傳話單位。"

  headquarters_location:
    - "白御行明示：觀止所在之京師是時空商路樞紐，才是真正總會應在之地。"
    - "白御行目前留京與總會中心位置相符。"
    - "定陶老家是『定陶商團』，不是因為起家於定陶就等於整個總會。"
    - "定陶商團與其他商團一樣需要自行經營、自負盈虧；不因會長出身定陶而自動獲得總會兜底。"

  expansion_model:
    - "進入新市場時，可先與當地商會／商家談整合。"
    - "願意加入者可獲得後勤資源、技術、人才、通路與其他市場開放。"
    - "不願加入者原則上不以行政強迫併入，但可能與定陶系統進入長期商業競爭。"
    - "定陶網絡因資金、後勤與跨市場能力，通常較有能力承受多年商戰；當地單一商家未必能長期承受。"
    - "白御行以『最後不是加入就是被消滅』概括其競爭結果；顧青簡補充仍存在對手扛住、定陶退出不值得市場等第三種結果。"

  anti_secession_levers_discussed:
    - "地方商團若意圖脫離共同網絡／自立，並非總會直接奪地。"
    - "可依契約與權利狀態停止或不續技術授權、共同信用／後勤支援等。"
    - "可撤去原本對其主要勢力圈的競爭默契，讓其他商團公開進入競爭。"
    - "白御行並提出可用地價／價格傾銷、開放各家搶地盤等商戰壓力對抗地方稱王。"
    - "具體哪些授權可立即終止、哪些必須依既有契約跑完，仍應按契約處理，不得一概追溯撤銷。"
```

---

# 9｜DINGTAO-CHAIR21-E01｜會長日常與公關費玩笑

```yaml
ROUTE_SOCIAL_STATE:
  event_id: "DINGTAO-CHAIR21-E01-CHAIRMAN_DELEGATION_AND_PR_EXPENSE_BANTER"
  status: "COMPLETED_SOCIAL_EXCHANGE"

  confirmed:
    - "白御行以自己每日只需短暫處理真正需會長決斷之事，作為地方自主／總會授權架構的自嘲說法。"
    - "顧青簡接受『若制度能自行跑，會長不必事事親為』之方向，但要求需要簽字／決斷時會長仍須出面。"
    - "白御行表示自己有公關費足以應付交際。"
    - "顧青簡與潘金蓮區分：有公務目的之宴客／交際可按規報支；純私人風月消費不可因會長身分自動列公帳。"

  not_established:
    - "任何具體公關費額度。"
    - "觀止房費已由總會報銷。"
    - "李師師私人陪伴屬公費項目。"
```

---

# 10｜LINGERIE21-E01｜李師師肚兜代言案擴張為發表會

```yaml
BUSINESS_PROPOSAL:
  event_id: "LINGERIE21-E01-SHISHI_ENDORSEMENT_EXPANDS_TO_FASHION_EVENT"
  lifecycle_state: "PROPOSAL_ACTIVE"
  execution_state: "NOT_CONTRACTED"

  trigger:
    - "白御行最初要求顧青簡翌日送來請李師師代言肚兜之企畫案。"
    - "白御行曾玩笑將自己對李師師身材之私人興趣稱為『調研費』；顧青簡明確不把私人身體接觸列作公費。"
    - "其後白御行把案子擴大為租風滿樓、由多名成年女子展示定陶肚兜新品之發表會。"

  product_lock:
    - "走秀／展示服裝使用定陶自家產品；不是讓模特任意穿其他商號商品。"

  venue_direction:
    venue: "風滿樓／觀止相關場地"
    pan_response: "潘金蓮表示有興趣談場租與正式商業活動"
    venue_contract_signed: false
    revenue_share_fixed: false
    on_site_sales_commission_fixed: false

  audience_model_latest:
    - "主邀請權在成年女性。"
    - "每名受邀女賓可攜一名成年陪同者；可為男性。"
    - "男性若以女伴陪同身分入場，其資格依附女賓邀請；不能拿女賓帖子單獨闖入。"
    - "女賓與陪同者同坐，女賓負責選貨／決定是否購買；陪同男性可成為付款者。"
    - "活動不是純女場，因白御行明示需要保留願意為女伴消費之男性付款來源。"
    - "後台量身、換裝、整理貼身衣物等區域原則上由女性工作人員處理，男性陪同者不得藉故進入後台。"

  event_positioning:
    - "不是男性選妃／看女人。"
    - "核心是女賓主導之新品發表、試料、訂製與下單。"
    - "男人若進場主要以女賓陪同者、合作夥伴、評審或其他明確活動角色進入。"
```

---

# 11｜MODEL21-E01｜成年女性公開徵選與身分分離原則

```yaml
MODEL_POOL_PROPOSAL:
  state_class: "PROPOSAL_WITH_IDENTITY_SEPARATION_RULE"

  player_direction:
    - "不把走秀資格限定在妓籍。"
    - "白御行主張：這是舞台表演／商品展示，不是性服務。"
    - "可考慮官府報備程序合格之成年女子、一般良家成年女子、外來女客等自願參加。"
    - "甚至到場女客若自己想走，可設臨場試走／徵選。"

  identity_separation:
    - "參與走秀不等於成為觀止妓籍／掛牌姑娘。"
    - "外來成年女子若參與，報酬應按表演／商業活動處理，不得自動寫成夜資、纏頭或賣身銀。"
    - "走秀同意、試穿同意、畫像同意、姓名公開、後續代言與商品命名應分別取得。"

  casting_direction:
    - "不應只選一種纖細／單一美型身材。"
    - "可故意保留高、矮、豐腴、纖細等不同成年女性身形，用來展示不同版型。"

  legal_unknown:
    - "本輪未見官府正式確認『報備後即可』之法律文書。"
    - "不得把白御行之操作主張自動寫成已完成官府許可。"
```

---

# 12｜SIGNATURE-BRA21-E01｜觀止人物專屬肚兜與疏影候選主設計

```yaml
DESIGN_PROPOSAL:
  event_id: "SIGNATURE-BRA21-E01-GUANZHI_CHARACTER_SIGNATURE_COLLECTION"
  lifecycle_state: "PROPOSAL_ACTIVE"
  execution_state: "DESIGN_NOT_STARTED"

  core:
    - "觀止每名願意參與之成年女性可先依自己想法提出一件專屬肚兜概念。"
    - "專屬款可依本人想展示的自己而不同：可暴露、可清純、可端莊、可野、可強調胸／肩／背／腰等不同身形特點。"
    - "重點不是所有人穿成同一個『好看』，而是每件先像那個女人本人。"
    - "定陶可派設計師／畫師／版師負責把概念落成樣稿與可製作版型。"

  shuying_candidate:
    - "白御行提出：疏影姑娘可能會想接此案。"
    - "疏影可作人物概念款主設計候選，替每個女人把不同性格／身形需求落成不同款。"
    - "疏影目前尚未被正式詢問，也未報價或同意。"

  two_layer_product_model:
    concept_piece:
      - "人物本人之專屬概念款，可更個人、更極端、更強烈。"
    commercial_adaptation:
      - "真正量產販售時可另做適合一般客戶身形／日常需求之改版。"

  rights_to_negotiate:
    - "本人對使用自己名字、人物款展示、公開畫像等權利需另談。"
    - "疏影若主設計，設計署名／報酬／權利需另談。"
    - "定陶負責製版、量產、通路之商業權利需另列。"
    - "本輪無任何一項已簽約。"
```

---

# 13｜ROKUJO21-E02｜六條御息所條件式同意走秀與概念款方向

```yaml
PERSONAL_EVENT_PROPOSAL:
  event_id: "ROKUJO21-E02-CONDITIONAL_RUNWAY_AND_DESIGN"
  lifecycle_state: "ACTIVE_CONDITIONAL_INTEREST"

  liu_tiao_response:
    - "六條御息所表示對走秀『有一點興趣』。"
    - "她不願把活動變成單純比較誰露得多。"
    - "若衣服依她自己想法設計、成衣完成後她喜歡，且活動維持女賓主導而非男子挑女人，她可以走一次。"

  design_preferences:
    - "色調偏深紫／接近夜色。"
    - "不要豔紅、不要滿身金線。"
    - "正面不需大量裸露。"
    - "可用肩、背、腰作主要身形顯影；六條明示背部可以更開。"
    - "希望加一層很薄之外披，走動時才顯出內層線條。"

  consent_state:
    runway: "CONDITIONAL_AGREEMENT_PENDING_FINISHED_GARMENT_AND_EVENT_STATE"
    product_naming: "NOT_DISCLOSED"
    mass_production: "NOT_DISCLOSED"
```

---

# 14｜INVITE21-E01｜評審、合作夥伴與外邀成年女性名單

```yaml
EVENT_INVITE_PROPOSALS:
  status: "CANDIDATE_INVITATIONS_NOT_YET_ACCEPTED"

  zhao_shouyi:
    proposed_role: "特邀評審"
    reason_in_scene:
      - "白御行以玩笑指出趙受益沒有女伴帶入場，可改以評審正式入場。"
    status: "NOT_YET_INVITED_OR_ACCEPTED"
    constraints:
      - "不能因其是評審就替模特改成他喜歡的款式。"
      - "評審席不應只有男性，可另邀懂布料、繡工、市場之女性評審。"

  shen_wansan:
    role_basis: "定陶商會合作夥伴"
    status: "MAY_ATTEND_UNDER_PARTNER_ROLE_IF_FORMALLY_INVITED"
    note: "不需硬套女伴陪同規則，但本輪未記正式發帖。"

  li_qingzhao:
    invitation_direction: "可再邀；此前曾留有『有好玩的可找她』之路線口子"
    status: "NOT_YET_CONFIRMED_ATTENDING"

  zi_shibu:
    invitation_direction: "可正式邀請"
    liu_tiao_condition:
      - "六條御息所同意可請紫式部。"
      - "邀請應以觀止／活動名義發出，可註明六條也會在場。"
      - "不要寫成六條御息所命她赴約。"
    status: "NOT_YET_CONFIRMED_ATTENDING"

  yu_huilan:
    name_as_given: "魚蕙蘭"
    invitation_direction: "白御行最後補入正式邀請候選"
    status: "NOT_YET_CONFIRMED_ATTENDING"

  general_rule:
    - "收到邀請不等於答應走秀。"
    - "來看、試衣、上台、使用姓名／畫像、後續代言分別決定。"
```

---

# 15｜LUXURY21-E01｜京師女性奢侈品旗艦店與批發端

```yaml
BUSINESS_EXPANSION_PROPOSAL:
  event_id: "LUXURY21-E01-CAPITAL_WOMENS_LUXURY_FLAGSHIP_WHOLESALE"
  lifecycle_state: "PROPOSAL_ACTIVE"
  execution_state: "NO_SITE_SELECTED_NO_LEASE"

  player_direction:
    - "在京師找好地段，安排女性用品專門店／店群。"
    - "零售以京師成年女性奢侈品需求為主。"
    - "同時讓各路商人可批貨，再運往其他市場。"

  retail_direction:
    - "可包含肚兜／貼身衣物、睡衣、布料、繡件、香粉、首飾等女性奢侈品。"
    - "商品線可依不同身形、版型與人物概念延伸。"
    - "前端零售環境應漂亮、安靜、適合女客長時間選貨／試樣。"
    - "貼身衣物相關量身、試衣與內間服務以女性工作人員為主要配置。"

  wholesale_direction:
    - "批發端需考慮進車、卸貨、存貨、查帳與大單洽談。"
    - "顧青簡提出前端旗艦零售與後端批發／倉儲最好分開，必要時以總會運輸線連接。"
    - "新品可先在京師試市場，賣得動再由各商團與外路商人擴散。"

  accounting_separation:
    - "零售帳與批發帳應拆分，避免以批發貨量掩蓋前端店舖真實零售表現。"

  current_next_step:
    - "顧青簡表示可尋找女眷往來方便、富戶消費密集、且能接後端貨路之候選地段。"
    - "尚未簽租、買地、選址或開店。"
```

---

# 16｜NIGHT21-E01｜晚間離場、奶瓶兒明日邀約未成立

```yaml
EVENT_RECORD:
  event_id: "NIGHT21-E01-RETURN_TO_SHISHI_ROOM_PINGER_DEPARTURE"
  lifecycle_state: "COMPLETED"
  event_axis_state: "NIGHT_RETURN_NO_THREEWAY_ESCALATION"

  confirmed:
    - "白御行結束大堂討論後，要求李師師與李瓶兒帶自己回房。"
    - "李師師與李瓶兒陪同白御行返回李師師房附近。"
    - "李瓶兒之後離開，沒有留宿。"
    - "白御行向李瓶兒說『明天去你家睡』。"
    - "李瓶兒沒有答應睡宿，表示明天醒後再問；若只是吃飯／玩一會兒可商量。"

  hard_nonchange:
    - "今晚沒有三人床局。"
    - "李瓶兒未對明日睡宿、性行為或長期安排作承諾。"
```

---

# 17｜NIGHT21-E02｜三歲半睡前餵飲表演

```yaml
STAGED_EVENT:
  event_id: "NIGHT21-E02-CHILDPLAY_BEDTIME_MILK"
  lifecycle_state: "COMPLETED"
  event_axis_state: "NONSEXUAL_CARE_PERFORMANCE"
  real_age_change: false

  confirmed:
    - "白御行在準備睡覺時重新說自己三歲半，問李師師是否不餵奶。"
    - "李師師依接戲 PATCH 不再反覆拆穿角色，而是接成睡前照護戲。"
    - "李瓶兒尚未走遠，被叫回協助提供溫熱乳飲／小盞。"
    - "李師師與李瓶兒以非性方式完成餵飲、擦嘴、蓋被等照護表演。"
    - "李瓶兒之後離開。"

  boundary:
    - "此處『奶』為乳飲／奶瓶式照護表演，不建立任何成人性身體行為。"
    - "三歲半框架若之後再啟用，仍只能走非性照護直到玩家明示退出角色框架。"
```

---

# 18｜NIGHT21-E03｜疲累明示、師師抱睡與今晚不挑逗

```yaml
CONSENT_AND_CARE_EVENT:
  event_id: "NIGHT21-E03-TIRED_HUG_NO_TEASING_BOUNDARY"
  lifecycle_state: "ACTIVE_CURRENT_SCENE"
  event_axis_state: "NONSEXUAL_COMFORT_AND_SLEEP"

  player_explicit:
    - "白御行明示：『這幾天有點累了。』"
    - "向李師師提出：『抱抱。』"
    - "明示：『晚上不要挑逗我。』"

  li_shishi_response:
    - "李師師明示答應。"
    - "她把白御行抱進懷裡，讓其靠著休息。"
    - "她表示今晚不挑逗、不談商會、不談肚兜與明天之事。"
    - "她同意陪睡，並以『別的都不要』收束本幕。"

  current_boundary:
    teasing_or_seduction_tonight: "REFUSED_BY_PLAYER_AND_ACCEPTED_BY_LI_SHISHI"
    sexual_activity_tonight_from_current_point: "NOT_REQUESTED_NOT_ESTABLISHED"
    hug_and_sleep: "MUTUALLY_ACCEPTED"
    automatic_morning_extension: false
```

---

# 19｜ACTIVE_RELATIONSHIP_STATES｜當前關係硬狀態

```yaml
ACTIVE_RELATIONSHIPS:
  bai_li_shishi:
    state_class: "ACTIVE"
    current_label: "FORGIVEN_RU_FUREN_ORALLY_RECONFIRMED_CURRENTLY_NONSEXUAL_HUG_SLEEP"
    confirmed:
      - "李師師已原諒先前事件，但過去事件未被抹除。"
      - "李師師想要如夫人位置之口頭意願仍有效。"
      - "今晚李師師接受白御行疲累時的非性擁抱與陪睡。"
      - "今晚從當前接關點不得主動以挑逗／成人誘惑作預設起手。"
    unresolved:
      - "如夫人之公開／家冊／法定實施。"
      - "李師師何時／是否直接回以愛的告白。"

  bai_li_pinger:
    state_class: "ACTIVE_WITH_BOUNDARY"
    confirmed:
      - "今晚已一起吃飯。"
      - "白御行可繼續用『奶瓶兒』作雙方目前可容忍／玩笑中的稱呼，但不得據此推定真實母子或成人性承諾。"
      - "明日可再詢問是否去她處吃飯／玩；睡宿未成立。"
    not_confirmed:
      - "任何三人成人親密。"
      - "明日去李瓶兒家睡。"
      - "李瓶兒與李師師已形成固定姐妹／性關係。"

  li_shishi_li_pinger:
    state_class: "POTENTIAL_FUTURE_COEQUAL_HOUSEHOLD_FRAME"
    confirmed:
      - "李師師對未來並列如夫人之原則仍接受。"
      - "本日晚宴實際相處未造成明示衝突。"
    not_confirmed:
      - "李瓶兒已接受並列方案。"
      - "兩人關係已升格。"

  bai_gu_qingjian:
    state_class: "WORKING_ASSOCIATION_RELATION"
    confirmed:
      - "顧青簡為總會／商會程序端師爺，能直接接手白御行交辦之案。"
      - "她把白御行視為需要在關鍵點簽字／決斷、但不應干預所有流程之會長。"
    not_confirmed:
      - "私人友情、戀愛、性關係或人物池固定關係。"
```

---

# 20｜ACTIVE_CONTRACTS_AND_DUE_ITEMS｜契約、企畫與到期事項

```yaml
ACTIVE_CONTRACTS_AND_DUE:
  caozhou_fake_seal_case:
    status: "FORMALLY_OPENED_ASSOCIATION_INTERNAL_PROCESS"
    next:
      - "等待總會／相關商團依 SOP 查核冒名採辦、印樣來源、賒貨鏈與責任。"
      - "查清後按白御行書面指示回報。"
      - "非緊急不需持續把細節送會長。"
    guanzhi_investigation_required: false

  womens_fashion_event:
    status: "PROPOSAL"
    due:
      - "顧青簡翌日可整理李師師代言／整體發表會企畫案。"
      - "潘金蓮可另談風滿樓場租、活動分成與現場成交抽成。"
      - "需向每名候選模特／代言人分別詢問。"
      - "需確認官府報備／舞台活動法律程序。"
      - "需確定定陶產品樣衣、版型、量身與訂單交付流程。"

  signature_collection:
    status: "PROPOSAL"
    due:
      - "先問觀止成年女性誰願提出自己的人物款概念。"
      - "詢問疏影是否願任主設計／如何報價。"
      - "六條成衣完成後再取得最終上台確認。"

  invite_list:
    status: "NOT_SENT_OR_NOT_CONFIRMED"
    due:
      - "趙受益：是否接受評審。"
      - "沈萬三：是否以合作夥伴／買家等角色正式出席。"
      - "李清照：是否收到邀請並願赴會。"
      - "紫式部：是否收到以活動名義發出的邀請；可註明六條在場。"
      - "魚蕙蘭：是否接受邀請。"

  luxury_store:
    status: "SITE_SEARCH_PROPOSAL"
    due:
      - "顧青簡可找候選地段。"
      - "零售主店與後端批發／倉儲模式需另做成本、租金與物流評估。"

  inherited_due:
    - "潘金蓮進西門家後之法律身分仍待查。"
    - "蘇清 vs 潘金蓮民事／帳務案仍待後續。"
    - "白玉池第二次正式復開檢查、許願幣材質／匯率、阿泠定存正式契約仍待完成。"
    - "李師師如夫人公開／登記仍未完成。"
```

---

# 21｜KNOWLEDGE_AND_PRIVACY｜知情與公開程度

```yaml
KNOWLEDGE_MATRIX:
  caozhou_fake_seal_case:
    knows:
      - "白御行"
      - "顧青簡"
      - "程姓曹州商人"
      - "觀止大堂當時在場者"
      - "已被總會 SOP 通知之相關商會節點"
    public_truth_status: "CASE_OPEN_NOT_YET_RESOLVED"

  dingtao_structure_explanation:
    knows_current_scene:
      - "白御行"
      - "顧青簡"
      - "潘金蓮"
      - "龐春梅"
      - "紅娘氏"
      - "李師師"
      - "李瓶兒"
      - "張麗華"
      - "六條御息所"
      - "程姓商人／在場聽見者"
    note: "保存為本線已公開說明之商會架構，不需每次重新教學。"

  fashion_and_luxury_plan:
    knows:
      - "白御行"
      - "顧青簡"
      - "潘金蓮"
      - "龐春梅"
      - "紅娘氏"
      - "李師師"
      - "李瓶兒"
      - "張麗華"
      - "六條御息所"
      - "當時近場可聽見者"
    external_invitees_knowledge: "NOT_YET_ASSUMED"

  tired_no_teasing_boundary:
    strict_private:
      - "白御行"
      - "李師師"
```

---

# 22｜UNKNOWN／UNDECIDED｜本 HOT 必須保持未決

```yaml
UNRESOLVED:
  - "曹州假印案之冒名者身分、印樣來源、總損失、是否有內鬼及最終責任。"
  - "程姓商人是否正式申請營運資金融通、金額與條件。"
  - "顧青簡是否會成為跨線／人物池固定人物；目前只是白御行線新增路線 NPC。"
  - "五大商團具體全名、各自完整地盤與海外殖民商團名冊；本輪未列全。"
  - "京師女性奢侈品店最終地點、租金、店型、開店日。"
  - "風滿樓肚兜發表會是否正式立項、日期、場租、預算、抽成。"
  - "官府對外來成年女性舞台表演／貼身衣物展示之具體報備要求與核准結果。"
  - "哪些觀止成年女性願意走秀、代言、公開姓名或讓人物款量產。"
  - "疏影是否接人物款主設計。"
  - "六條最終是否在成衣完成後仍願上台。"
  - "趙受益是否接受評審邀請。"
  - "沈萬三是否參加。"
  - "李清照、紫式部、魚蕙蘭是否到場；更不等於她們願意走秀。"
  - "白御行明日是否真的去李瓶兒住處；李瓶兒尚未答應睡宿。"
  - "今晚白御行與李師師何時睡著、何時醒來。"
  - "白御行下一次是否繼續三歲半角色戲；目前不得自行維持或取消到明日。"
  - "V0.1-EXP 接戲 PATCH 是否最終納入主系統；目前只是獨立試跑。"
```

---

# 23｜FORBIDDEN_INFERENCES｜禁止回歸與反污染

```yaml
FORBIDDEN_INFERENCES:
  - "不得把曹州程商人報案寫成假印案已破。"
  - "不得讓潘金蓮、春梅、師師等觀止人物替商會 SOP 調查；案件已交由顧青簡／商會內部機制。"
  - "不得把白御行一句『印不是我們的』自動補成已知偽造者、內鬼或完整證據鏈。"
  - "不得把白御行故事內對商會架構之說明自動寫入跨線人物卡／世界主程序基線；本 HOT 保存其玩家線現行法位即可。"
  - "不得把地方自主寫成地方可保留總會技術、信用、通路等共同資源而無契約後果。"
  - "也不得把總會反制寫成可以無視既有契約任意追溯撤銷所有既得權；應按契約處理。"
  - "不得把海外殖民商團存在擴寫成具體國家、港口、軍事殖民或未給出的領土。"
  - "不得把顧青簡命名寫成人物池已正式新增。"
  - "不得把發表會／旗艦店企畫寫成已開張、已簽場、已開始賣貨。"
  - "不得把白御行關於官府報備的說法寫成已取得官府核准。"
  - "不得把走秀等同妓籍、接客、性服務或賣身。"
  - "不得把一名成年女性同意走秀擴張為同意試衣、公開畫像、使用名字、量產、陪客或性行為。"
  - "不得把六條條件式走秀同意寫成已無條件答應。"
  - "不得替趙受益、沈萬三、李清照、紫式部、魚蕙蘭答應出席。"
  - "不得替疏影答應設計。"
  - "不得把李瓶兒今晚吃飯、照護戲或『奶瓶兒』玩笑寫成她已同意成人親密。"
  - "不得把『明天去你家睡』寫成李瓶兒已答應。"
  - "不得把三歲半角色戲倒灌成玩家實際未成年。"
  - "不得在三歲半角色框架內生成成人性內容。"
  - "不得讓 NPC 因接戲就真的形成母愛、親屬、永久照護人格或關係。"
  - "不得忽略白御行今晚『不要挑逗我』之明示；下一幕若仍在當夜李師師房中，不能由李師師主動性挑逗開場。"
  - "不得把『抱抱／陪睡』擴張為性交同意。"
```

---

# 24｜MASTER_LOOKUP_INDEX｜需要厚歷史時的查詢索引

```yaml
MASTER_LOOKUP_INDEX:
  long_term_master:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"
    use_for:
      - "截至 HOT V2.5 的長期因果、人物關係與法律／帳務歷史"
      - "西門慶、蘇清、潘金蓮、公案、六條初入觀止等厚歷史"

  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V2.8_槐月二十一日白日_潘身籍補證_白玉池許願幣定存_師師如夫人確認與晚宴前休息版.md"
    use_for:
      - "潘身籍副冊補證"
      - "阿泠許願幣／定存框架"
      - "李師師跪歉原諒、如夫人、李瓶兒並列前置"
      - "晚宴菜單與李瓶兒『先吃飯』界線"
      - "師師足部親密、腳環、煙青色肚兜私人畫像"

  experimental_overlay:
    file: "觀止青樓_PATCH_風月角色表演與接戲能力_V0.1-EXP_獨立試跑未併主系統.md"
    use_for:
      - "角色表演／接戲與真心、關係、人格分軸"
      - "自願接戲後避免反覆拆戲"
      - "三歲半角色框架之非性限制"

  persona_source:
    file: "觀止人物卡池_LCAPG_V2.1_青禾六條增補_原版20人鎖定_補充人物擴充正式版.md"
    use_for:
      - "人物人格與跨線基線"
      - "李師師、李瓶兒、紅娘氏、六條御息所等人物卡"
```

---

# 25｜下一幕自然接關

```yaml
CONTINUATION_POINT:
  primary_scene: "李師師私人房間／深夜榻上"
  state:
    - "白御行明示這幾天有點累。"
    - "白御行要求李師師抱抱，並明示今晚不要挑逗。"
    - "李師師已接受，現正以非性方式抱著白御行陪睡。"
    - "李瓶兒已離開；今晚沒有形成三人床局。"
    - "曹州假印案已交商會內部 SOP，短期內不需要觀止人物追查。"
    - "京師女裝／女性奢侈品計畫停在企畫階段，適合隔日以顧青簡／潘金蓮送案或人物自主回應進場。"

  next_natural_world_beats:
    - "可讓本夜真正安靜過去，下一幕從翌晨／睡醒後接起。"
    - "若仍停在當夜，不應新增李師師性挑逗；可有安靜陪睡、夜間環境或正常突發事件，但重大事件須有因果。"
    - "隔日顧青簡可送來肚兜代言／發表會初稿，或先帶候選店址／成本資料；不得直接宣稱場地、店面或邀請人已簽妥。"
    - "潘金蓮可開始向觀止成年女性詢問是否願意參與設計／走秀，但每人答案必須人物自主生成。"
    - "可向疏影提出設計邀請；疏影是否接單、如何設計、報價由本人決定。"
    - "曹州假印案待商會程序產生新結果後再回報，不要每輪重複調查。"

  hard_stop_conditions:
    - "白御行是否明日去李瓶兒住處／是否留宿。"
    - "任何人物是否接受走秀、貼身衣物公開展示、代言、姓名／畫像使用或量產授權。"
    - "風滿樓場租／抽成正式簽約。"
    - "旗艦店選址、租買、重大投資。"
    - "趙受益、李清照、紫式部、魚蕙蘭、沈萬三等正式邀請之接受結果。"
    - "任何新的成人親密，尤其當前白御行已明示今晚不要挑逗。"
```

---

# 26｜一句接關摘要

> **槐月二十一日晚，李瓶兒依約赴師師小席並維持「先吃飯」界線，未形成三人親密；白御行的三歲半照護戲暴露 NPC 反覆拆戲問題，遂在戲外建立未併主系統的「風月角色表演與接戲能力 PATCH V0.1-EXP」試跑。其後曹州程姓商人帶假定陶印樣到觀止報案，白御行判定非本會印、命按商會 SOP 立案，女性師爺顧青簡接手，案件已進內部程序。白御行並在大堂明示：五大商團是早期核心，後續另有海外殖民商團；各團地方自主、自負盈虧，總會掌跨團運輸、信用、技術／授權與市場網；真正總會位於時空商路樞紐京師，定陶老家只是定陶商團。晚間又形成京師女性奢侈品旗艦店與定陶肚兜發表會企畫：女賓主邀請、可帶一名成年陪同者，走秀不以妓籍為必要前提，觀止每名願意參與之女人可設計自己的專屬人物款，疏影為候選主設計；六條對深紫夜色、正面收斂而肩背顯形之款式有條件同意走秀，趙受益、沈萬三、李清照、紫式部、魚蕙蘭皆僅為候選邀請。現已深夜，李瓶兒離開，白御行明示疲累、要李師師抱抱並要求今晚不要挑逗；李師師接受，下一幕從她房中安靜陪睡或翌晨醒來接起。**

<!-- PROMOTED_HOT_SOURCE_END: 觀止青樓_白御行線_HOT_SAVE_V2.9_槐月二十一日深夜_曹州假印立案_定陶總會架構_京師女裝企畫與師師抱睡版.md -->

---

# APPENDIX F｜固化來源全文：觀止青樓_白御行線_HOT_SAVE_V3.0_槐月二十二日夜_風滿樓大型遴選_四大金剛與雙夫人權限版 (1).md

> **法位：E84–E92 細節追溯來源。** 此 HOT 內的 CURRENT_SCENE／HOLD 只代表當時快照；不得覆寫本 MASTER 截止或 V3.5–V3.7 疊加層。若原 HOT 內某個標成 YAML 的區塊本身語法不合法，本 MASTER 只把該 fence 改標為 text 隔離，內容原文不改，避免來源語法缺陷破壞 MASTER 解析。

<!-- PROMOTED_HOT_SOURCE_BEGIN: 觀止青樓_白御行線_HOT_SAVE_V3.0_槐月二十二日夜_風滿樓大型遴選_四大金剛與雙夫人權限版 (1).md -->
# 觀止青樓｜白御行線 HOT SAVE V3.0
## 理火三年槐月二十二日夜｜風滿樓大型遴選 × 定陶女性事業直轄案 × 蘇清月事用品專案 × 特殊人才五人交易 × 白家四大金剛與雙夫人內部權限版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V3_0_HUAI22_NIGHT_FENGMANLOU_SELECTION_WOMENS_BUSINESS_SPECIAL_TALENTS_FOUR_VAJRAS_TWO_MADAM_AUTHORITY"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V3.0"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V11.0-R2"
  character_source: "觀止人物卡池_LCAPG_V2.1"
  story_date: "理火三年槐月二十二日"
  time_of_day: "夜間；風滿樓大型遴選仍在運作，特殊高價複核區已收工"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AT_ZHANG_LIHUA_ROOM_AFTER_FOUR_WOMEN_RECOGNIZE_LIHUA_MADAM"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V2.9_槐月二十一日深夜_曹州假印立案_定陶總會架構_京師女裝企畫與師師抱睡版.md"
  previous_hot_sha256: "8a103e918723b5b82df2a21e265906b11f6c2c0510f17dc1b123d2c67787e9e3"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"
  experimental_overlay:
    file: "觀止青樓_PATCH_風月角色表演與接戲能力_V0.1-EXP_獨立試跑未併主系統.md"
    status: "INDEPENDENT_TRIAL_OVERLAY_NOT_MERGED_TO_MAIN_SYSTEM"
  save_scope:
    - "HOT V2.9 後至槐月二十二日夜之直接玩家線事件"
    - "風滿樓主廳空間狀態、大型新人遴選、牙行與觀眾規則"
    - "定陶女性注意力／偶像式事業之秘密直轄架構"
    - "蘇清二十八日私約後續工作化安排與月事用品專案"
    - "李師師、張麗華成人丫環候選"
    - "李瓶兒未來如夫人並列之私人談話與輕吻"
    - "特殊高價複核區五名人才之成交、持契、價格、用途與保密"
    - "白三十二娘、白明礬、白紅伶、白希之工作身份、華服買斷、內部紀律"
    - "李師師『白夫人』與張麗華『麗華夫人』對四人之不同內部權限"
```

---

# 0｜提交法位、來源與本輪反污染

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V2.9_槐月二十一日深夜_曹州假印立案_定陶總會架構_京師女裝企畫與師師抱睡版.md"
    role: "本檔直接前置 HOT；V2.9 及以前有效硬狀態全部繼承"

  master_archive:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"
    role: "截至 HOT V2.5 之長期因果；V2.6-V2.9 由 HOT 鏈承接"

  current_route_conversation_commit:
    role: "HOT V2.9 後至本次 HOT SAVE 命令前之直接劇情、玩家明示自身言行與 NPC 可觀察回應"

COMMIT_NOTE:
  - "本檔取代 HOT V2.9，成為白御行線最新直接接關切片；V2.9 保留為前置歷史來源。"
  - "本次只更新 HOT；不更新 MASTER，不修改人物卡池，不把四名新購女性升格為跨線人物卡。"
  - "新女性事業之『48／神七／御三家』架構目前為白御行線秘密商業模型，不自動升格世界基線。"
  - "風滿樓不是另一棟建築；本輪所稱風滿樓為觀止主廳進入擴張／異常空間狀態後之形態。任何『另租一棟風滿樓／走去另一棟樓』舊生成均視為污染，不寫入本 SAVE。"
  - "人物工作身分、持契與服從關係不等於任何特定成人行為已取得同意；特定成人事件仍須另行形成事件狀態。"
  - "白御行之『送去餵魚』是其對洩密／告密／背叛的懲戒宣示與威嚇規則；本輪未實際發生任何因此被殺、被處決或被送去餵魚之事件。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年槐月二十二日"
  time: "夜間；精確時刻未知"
  primary_location: "觀止青樓／張麗華房間門內外；風滿樓主廳仍在運作"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  player:
    name: "白御行"
    current_position: "張麗華房內／正準備帶四名新購女性離開"
    last_confirmed_utterance:
      - "白御行對張麗華說：『是，那夫人我們滾出去了喔。』"
    no_new_player_action_after_save_command: true

  present_or_immediate:
    - "張麗華／房內"
    - "白三十二娘"
    - "白明礬"
    - "白紅伶"
    - "白希"
    - "紅娘氏／近門口同行"

  parallel_world_state:
    - "風滿樓主廳大型遴選尚未整體收場。"
    - "特殊高價複核區已由白御行明示收工，不得再自動追加『最後一名特殊候選』。"
    - "潘金蓮仍在處理今晚遴選、價格與明日容量；白三娘、疏影等仍在各自評估位置。"
    - "蘇清、常煒及常煒名下新購物流女子此前在二樓／後台秘密工作區推進月事用品與女性事業相關工作；本輪未觀察到其後續離場。"

  direct_resume_options_without_forcing_player:
    - "白御行可帶四人返回風滿樓前堂。"
    - "世界可在前堂推進今晚一般遴選結果、明日大批潛力甄選準備、觀眾票價或人物自主事件。"
    - "不得替白御行自動付款、回房、離場、睡覺或跳到翌日。"
```

---

# 2｜V2.9 繼承中仍活躍之核心狀態

```yaml
INHERITED_ACTIVE_CORE:
  cao_zhou_fake_seal:
    status: "ACTIVE_UNDER_ASSOCIATION_HANDLING"
    note: "曹州程姓商人假印案已交顧青簡／總會流程；觀止女性不負責偵查。"

  dingtao_general_association:
    - "總會負責跨團運輸、通路、信用、技術／授權與重大架構；地方商團日常自主、自籌資金、自負盈虧。"
    - "京師／觀止所在區域為總會樞紐；定陶老家只是定陶商團之一。"

  fashion_business:
    - "京師女性奢侈品旗艦店、批發端、肚兜發表會仍屬企畫；場地、預算、正式合約尚未完成。"
    - "疏影仍是人物專屬肚兜主設計候選；尚未正式簽約。"
    - "六條御息所走秀為條件式意願；成衣與活動狀態未滿足前不得寫成已確定上台。"

  li_shishi:
    - "已原諒白御行先前突兀離房事件。"
    - "已明示想要如夫人位置。"
    - "如夫人仍未完成對外公告、家冊／官籍或正式法律程序。"

  li_pinger:
    - "不是西門慶買入之奴婢。"
    - "與西門慶之最終婚姻／法律狀態仍待清理。"

  su_qing_vs_pan:
    - "蘇清 vs 潘金蓮民事／帳務案仍 ACTIVE。"
    - "五千原款與五萬索賠仍分軸；五萬不是判決。"
```

---

# 3｜WOMEN-BIZ22-E01｜定陶女性注意力事業秘密模型確立

```yaml
SECRET_BUSINESS_MODEL:
  event_id: "WOMEN-BIZ22-E01-CENTRAL_48_MODEL"
  lifecycle_state: "ACTIVE_SECRET_PROJECT"
  public_cover: "觀止擴編／新人遴選"
  true_business_visibility: "STRICTLY_LIMITED"

  leadership:
    project_head: "常煒／定陶總會副會長"
    authority_level: "總會直轄新事業"
    local_merchant_group_personnel_ownership: false

  model:
    - "不是全天下只收四十八人；每一城市／隊伍可形成一組四十八人架構。"
    - "未來可擴張為多城市、多隊伍、數百名成年女性。"
    - "每年可形成跨城競逐／總選。"
    - "前七名暫稱『神七』；前三名暫稱『御三家』。"
    - "總會選入場資格與制度；市場透過持續消費、支持、注意力與商業結果選出贏家。"
    - "高位者可取得更多資源、侍女、旅費與舞台；低位者可承擔支援性工作，但不得把排名簡化為永久人格／價值。"
    - "核心商品不是單純肉體，而是注意力、人物形象、表演、名聲、象徵聯結，以及由此帶動的實體商品消費。"
    - "古典花魁／風月訓練可與新式偶像包裝結合。"

  governance:
    - "本事業由總會直接控制，地方商團可成為客戶、合作夥伴、贊助方，但不得取得女性人員的所有權、排名權或人事控制權。"
    - "地方團隊女性之組織法位歸總會系統，不屬地方商團私產。"

  secrecy_circle_minimum:
    confirmed_knowers:
      - "白御行"
      - "常煒"
      - "顧青簡"
      - "蘇清／本晚回樓後已猜中並被納入保密圈"
    not_automatically_informed:
      - "外部牙行"
      - "一般候選女性"
      - "一般觀止客人"
      - "未因在場即自動知情之觀止人物"

  anti_leak:
    - "對外可隱藏商業戰略，但正式契約、身契、帳務與登記不得為掩護而造假。"
    - "候選人可被告知觀止擴編／風月可能性；不得因此自動知道未來四十八人與總選模型。"
```

---

# 4｜FENGLAO22-E01｜風滿樓大型遴選與兩日甄選架構

```yaml
EVENT_RECORD:
  event_id: "FENGLAO22-E01-MASS_SELECTION"
  lifecycle_state: "ACTIVE"
  event_axis_state: "CONTINUING"
  location: "觀止主廳／風滿樓擴張狀態"

  spatial_lock:
    - "風滿樓是觀止主廳進入神異擴張狀態後的形態，不是獨立建築。"
    - "一樓主要承擔候選、等候、試衣、甄選與工作區；二樓可作坐席、私室與秘密工作空間。"

  public_effect:
    - "風滿樓擴張本身吸引外界注意，已有『風滿樓開了』之類口耳議論。"
    - "外部牙行、候選人、觀止既有女性與客人共同形成即時市場反應場。"

  two_day_framework:
    tonight:
      - "重點看可立即使用、履歷／技能可核、價格可高的成年女性。"
      - "特殊價位／特殊能力者經核驗後可送白御行私下複核。"
    tomorrow:
      - "重點看可培養潛力，不保證立即成材。"
      - "白三娘主看可教性。"
      - "疏影主看台步、舞台、衣物與身體線條互動。"
      - "蘇清主看被低估／錯置的商業潛力。"
      - "顧青簡主看身分、來源、文書與知情紀錄。"
      - "潘金蓮主看價格、交易與市場性。"

  tomorrow_submission_rule:
    - "所有牙行都可送候選，不限最初兩家。"
    - "『都收都來』不等於不做篩選；候選須成年、來源可查、有實際潛力。"

  spectator_fee:
    - "明日對外看熱鬧之觀眾可收門票，以回收風滿樓運作成本。"
    - "候選人與牙行的工作進場不收觀眾票。"
    - "門票是場地收入，不是人氣投票票券。"
    - "具體票價尚未定；潘金蓮可依需求決定一般觀眾票價。"

  candidate_knowledge_tracking:
    owner: "顧青簡"
    fields:
      - "入場前已知可能涉及風月用途"
      - "入場後始知風月可能性"
    rule: "不得把後知情者偽記成原本已知。"

  high_price_review_rule:
    - "普通價位由潘金蓮處理。"
    - "超出常規價帶且具可核特殊價值者，送私下複核區。"
    - "複核至少保留牙行方與記錄／文書核驗人員。"
    - "白御行本晚指定紅娘氏陪同複核，主要負責盯牙行、維持候選完整陳述、觀察與臨場應對。"
```

---

# 5｜QANDA22-E01｜公開問答與甄選觀察準則

```yaml
SELECTION_QA:
  status: "COMPLETED_FOR_THIS_PHASE_WITH_CONTINUING_SELECTION"
  confirmed_topics:
    - "風月工作可能性與候選知情"
    - "收入與分配"
    - "暴力、言語侮辱與客人風險"
    - "年齡、疾病、月事與身體狀態"
    - "金錢、禮物、識字、客人競爭"
    - "客人聲稱贖身／承諾等話術"
    - "職業年限之外的技能、教學、管理等路徑"

  evaluation_principle:
    - "不只看候選能回答什麼，也看她是否知道自己不知道什麼、會不會提出有用問題。"
    - "現場觀眾反應可作市場測試之一，但不得單獨取代人物能力、來源、價格與可教性判斷。"
```

---

# 6｜MAID22-E01｜李師師與張麗華丫環候選狀態

```yaml
LI_SHISHI_MAID_PLAN:
  payer: "白御行"
  contract_holder_if_purchased: "李師師"
  target_count: 2
  roles:
    - "近房／懂分寸／守密型成年丫環"
    - "外跑／識字／膽子較大之成年丫環"
  current_candidate:
    - "已有一名偏近房型候選值得保留；她在碰顧青簡文書前先詢問是否可碰。"
  transaction_status: "NOT_PURCHASED_NOT_FINALIZED"

ZHANG_LIHUA_MAID_PLAN:
  payer: "白御行"
  contract_holder_if_purchased: "張麗華"
  target_count: 1
  desired_traits:
    - "成年"
    - "膽大、反應快、不怕張麗華"
    - "能處理張麗華醉酒，不愛碎念"
    - "最好具一定打架／自保能力"
  current_first_choice:
    - "一名候選先問張麗華醉後是否會吐、是否亂打人、或只打碰她的人；張麗華對此候選明顯有興趣。"
  transaction_status: "NOT_PURCHASED_NOT_FINALIZED"
```

---

# 7｜PINGER22-E01｜李瓶兒未來並列如夫人之私人談話

```yaml
PRIVATE_RELATION_EVENT:
  event_id: "PINGER22-E01-EQUAL_RIRU_PRIVATE_TALK_AND_LIGHT_KISS"
  privacy: "PRIVATE"
  participants:
    - "白御行"
    - "李瓶兒"

  confirmed_player_disclosure:
    - "白御行明示：待李瓶兒與西門慶之法律／婚姻狀態清理後，希望她若仍願意，可與李師師並列如夫人。"
    - "白御行轉述李師師的條件：兩人地位平等，不以先後排高低，不由其中一人管另一人。"
    - "白御行表示李師師願意當面與李瓶兒談，而非由白御行單方面替她作主。"

  li_pinger_response:
    - "李瓶兒對『不是先進門的壓後進門、兩邊互不管』之方向可接受。"
    - "她對如此重要之事未在前一晚先告知自己有輕微受傷／介意。"
    - "她希望之後親耳聽李師師說。"
    - "白御行提醒她：若日後李師師私下邀請，不要只因緊張便預先躲開；李瓶兒表示不會先躲，實際是否留下／做什麼仍由當時自己決定。"

  physical_event:
    - "白御行離開前對李瓶兒作輕吻。"
    - "李瓶兒未閃避，出現害羞／戲謔回應。"
    - "本段沒有進一步成人性行為。"

  does_not_establish:
    - "李瓶兒已正式成為如夫人"
    - "李師師與李瓶兒已完成三方名分會談"
    - "李瓶兒已同意任何後續三人性行為"
```

---

# 8｜SUQING22-E01｜蘇清回樓、保密圈與二十八日私約工作化

```yaml
SU_QING_ROUTE_UPDATE:
  event_id: "SUQING22-E01-RETURN_SECRET_PROJECT_AND_28DAY_WORK_SPLIT"
  status: "ACTIVE"

  return_and_interception:
    - "蘇清本晚回到觀止，在進入主廳前被引到二樓／秘密工作區。"
    - "原因是白御行／常煒判斷她很可能從今晚甄選結構推到真正女性事業模型。"
    - "蘇清實際上已猜到大方向；白御行要求她保密，她接受並加入最低保密圈。"

  civil_case_negotiation_direction:
    - "白御行曾向蘇清提出：若她不重視象徵性勝訴，可接受由許慎言探討與潘金蓮的實質和解方案。"
    - "蘇清接受『可談』，但未簽和解；具體金額與條款由許慎言／潘金蓮側談後仍須蘇清本人決定。"
    - "訴訟／索賠未因可談和解而自動撤回。"

  private_28_day_deal_update:
    - "原二十八日私人約之原始觸發條件仍未發生。"
    - "未來若進入該二十八日，現行安排改為：二十日投入秘密女性事業工作，八日履行白御行私人部分。"
    - "二十日工作由常煒統籌，不另計一般日薪；之後是否正式聘為總會人員另談。"
    - "明日潛力批次預篩先記一個『提前專案工作日』。"
    - "若原始觸發後該日可併作第一日；若觸發未發生，該提前工作日須另行結算，不得憑空消失。"

  screening_lens:
    key_question: "她現在沒有價值的地方，是真的沒有，還是從來沒人知道該怎麼賣。"
```

---

# 9｜MENSTRUAL22-E01｜草木灰月事用品標準化專案

```yaml
PROJECT:
  event_id: "MENSTRUAL22-E01-ASH_PACKET_BELT_STANDARDIZATION"
  lifecycle_state: "ACTIVE_PROJECT_DISCUSSION"
  prototype_complete: false
  mass_production_started: false

  leadership:
    product_and_women_user_side: "蘇清"
    process_supply_cost_recycling: "常煒"
    white_yuxing_role_after_assignment: "已明示細節不用事事問自己，由蘇清與常煒自行討論推進"

  core_concept:
    - "不是發明女性月事照護，而是把既有草木灰吸收法做成可標準化、可替換、可回收服務。"
    - "以固定規格布袋裝處理後之吸收材料／草木灰核心。"
    - "以 T 型／腰帶式固定結構承載可替換吸收袋。"
    - "女性可按月購買一組替換袋；使用後可丟棄，或把可回收布件送回集中處理。"
    - "集中端負責清洗可重用布件、補裝符合規格之乾淨吸收材料，再供下周期使用。"

  standardization_axes:
    - "灰源／材料來源"
    - "篩選與處理"
    - "重量"
    - "布袋尺寸"
    - "縫線"
    - "厚度"
    - "腰帶固定方式"
    - "清洗、回收、補充流程"

  product_direction:
    - "先解決便宜、乾淨、固定規格與實用性。"
    - "日後可形成基本版與更舒適／高階版，但本輪尚未定型。"
    - "蘇清需找不同身形、活動量與使用習慣的成年女性實測；男方可懂製造，但不能替女性判定舒適度。"

  anti_overclaim:
    - "本 SAVE 不把現代材料視為唯一正解，也不把未經故事內驗證之現代醫療評價倒灌為產品失敗。"
    - "本輪沒有完成歷史考據、官府醫療認證或量產安全結論。"
```

---

# 10｜SPECIAL22-E01｜特殊高價複核區收工

```yaml
SPECIAL_REVIEW:
  event_id: "SPECIAL22-E01-HIGH_VALUE_REVIEW_CLOSED"
  status: "CLOSED_FOR_TONIGHT"
  player_direction:
    - "候選先完整講自己經歷與用途；牙行不得中途替她吹價／搶答。"
    - "白御行會查牙行原始取得成本、轉手文書、持有時間與可核履歷，再議價。"
    - "紅娘氏陪同，重點是看住牙行、維持談話與觀察候選。"

  closure:
    - "白御行明示本區『就這樣，這裡收工了』。"
    - "不得自然推進出新的第六名／最後一名特殊候選。"
```

---

# 11｜SPECIAL22-P01｜白三十二娘

```yaml
PERSON_ACQUISITION:
  working_name: "白三十二娘"
  original_name: "NOT_REQUIRED_NOT_PUBLIC"
  age: 26
  buyer_and_contract_holder: "白御行"
  funding: "白御行私人"
  agreed_price_taels: 320
  asking_price_taels: 380
  known_yahang_acquisition_cost_taels: 167
  transaction_status: "COMPLETED"
  price_visibility: "STRICTLY_PRIVATE_LEDGER"

  verified_or_observed_skills:
    - "識字、兩種字體"
    - "帳目、契約、內務文書"
    - "禮數與一定音樂素養"
    - "部分舊時文書／舊語感"
    - "能估自己的可重複價值，不只靠一次性身體賣點"
    - "能把真實材料重組為可長期維持的市場人物故事"

  background_boundary:
    - "其父系舊政治牽連、舊官戶家史只屬私人來源；不得因市場包裝而對外洩漏。"
    - "她表示可做『七分真、三分假』而不易穿幫的舞台身份，但不等於真的失憶。"

  white_yuxing_directives:
    - "守密、不背叛為核心；一般錯誤可說明理由、承認、修正。"
    - "公開市場不依賴她原本姓氏／舊家世，可自行創造可持續人物故事。"
    - "目前先跟在白御行身邊，不必過度說話。"

  current_position: "白御行身邊／張麗華房內近場"
```

---

# 12｜SPECIAL22-P02｜白明礬

```yaml
PERSON_ACQUISITION:
  working_name: "白明礬"
  age: "約二十八至二十九"
  buyer_and_contract_holder: "白御行"
  funding: "白御行私人"
  agreed_price_taels: 275
  transaction_status: "COMPLETED"

  physical_trace:
    - "右手指尖留有長期染色痕跡。"
    - "左手小指尖幼年因染坊絞架事故缺損；不是刑罰。"

  skills:
    - "染色"
    - "色差辨識"
    - "布料／染料品質檢查"
    - "辨認偷工減料、摻假、過火、低價替料與耐久差異"
    - "理解某些顏色成本高但觀眾感知不值，某些低成本色反而視覺顯貴"
    - "理解布料顏色與穿著者膚色、燈光、舞台效果的互動"

  placement:
    tomorrow: "安排在蘇清旁邊，參與潛力遴選／商品與色料觀察"
    current: "白御行身邊／張麗華房內近場"

  personal_request_observed:
    - "希望持續接觸布料／色彩工作，以免眼力荒廢。"
```

---

# 13｜SPECIAL22-P03｜白紅伶

```yaml
PERSON_ACQUISITION:
  working_name: "白紅伶"
  age: "約二十四至二十五"
  buyer_and_contract_holder: "白御行"
  funding: "白御行私人"
  agreed_price_taels: 380
  known_yahang_acquisition_cost_taels: 190
  transaction_status: "COMPLETED"

  skills:
    - "聲音、口音模仿"
    - "人物語氣與角色表演訓練"
    - "可從本人真實特質出發，設計可長期維持而不易破功的舞台人物"
    - "可教新人修口音、找辨識度、學會維持客人想看的角色"

  placement:
    current: "先留後台／白御行身邊調度，不當普通前台花魁處理"
    likely_future_use: "李師師日後設席、席宴人物／聲音調教、女性事業人物塑造"
    transfer_to_li_shishi_completed: false

  secrecy:
    - "尚未因此自動知道完整秘密四十八人模型。"
```

---

# 14｜SPECIAL22-P04｜白希

```yaml
PERSON_ACQUISITION:
  working_name: "白希"
  age: "約三十四至三十五"
  buyer_and_contract_holder: "白御行"
  funding: "白御行私人"
  agreed_price_taels: 150
  known_yahang_acquisition_cost_taels: 210
  yahang_verified_prior_job_revenue_taels: 65
  transaction_status: "COMPLETED"

  skills:
    - "大型宴會／戲班後台／多人進退場安排"
    - "入口、出口、桌位、動線、燈具與人流風險"
    - "多人群像之注意力配置"
    - "判斷誰會吃掉別人的光、誰能托高別人、誰不該同時上台"
    - "曾處理數十人至約七十人之混合場務／演出人員協調"

  price_interpretation:
    - "白御行明示 150 是本次交易成交價，不是她永久人格／能力價值。"
    - "她理解技能價值取決於是否被放到正確位置；若被閒置，價格再低也可能浪費。"

  placement:
    current: "留在白御行身邊，尚未正式放入大型舞台工作"
```

---

# 15｜SPECIAL22-P05｜常煒名下物流／商路女性

```yaml
PERSON_ACQUISITION:
  working_name: "UNNAMED_BY_BAI_YUXING"
  naming_owner_for_future_scene: "常煒"
  age: "約三十"
  purchaser_cash_fronted_by: "白御行"
  contract_holder: "常煒"
  agreed_price_taels: 360
  yahang_initial_ask_taels: 460
  verified_official_auction_or_transfer_cost_taels: 240
  transaction_status: "COMPLETED_WITH_CHANG_WEI_ASSENT"

  authorization:
    - "顧青簡／書吏要求常煒本人授權後才將契記到常煒名下。"
    - "常煒回覆印記／同意，故不是白御行單方面代人持契。"
    - "白御行玩笑稱可從常煒年底分紅扣款；常煒表示與白御行私下結算，尚未形成正式扣款憑證。"

  skills:
    - "商路、貨物、採辦、車隊"
    - "四種語言，其中兩種較熟、兩種足以交易／問路／應急"
    - "帳務、採購與路線記憶"
    - "可規畫空車返程／回程運力媒合"

  business_proposal:
    - "北京—曹州—定陶等路線建立三個集貨點。"
    - "媒合有空車位的商隊與無法包整車的小貨主。"
    - "整合倉儲、裝卸、護送與部分貨運資訊。"
    - "初步估 600 兩級資本可驗證模型；三個月看路線、半年希望回本、一年正常目標約二成五至三成三。"
    - "定陶既有網路若直接提供節點，可顯著降低起始成本。"

  current_position:
    - "已送至常煒／蘇清所在二樓秘密工作區。"
    - "她的正式名字由常煒日後處理；白御行已明示不替她命名。"
```

---

# 16｜WHITE-FOUR22-E01｜白家四名新購女性之共同管理規則

```yaml
WHITE_FOUR_GROUP:
  members:
    - "白三十二娘"
    - "白明礬"
    - "白紅伶"
    - "白希"

  legal_or_route_position:
    - "四人均為白御行本晚私人出資取得之持契人員。"
    - "目前不是觀止正式掛牌花魁，也不是定陶女性事業正式四十八人名冊。"
    - "目前核心用途是把各自技能放進白御行／定陶未來事業與場面調度。"

  white_yuxing_management_statements:
    forgive_rule:
      - "白御行明示：天大的事情，只要理由能讓他接受，可以放過。"
    betrayal_rule:
      - "對洩密、告密、背叛採零容忍宣示；其原話之最重處置意象為『送去餵魚』。"
      - "此為管理／威嚇規則；本輪沒有實際處決事件。"
    tool_position:
      - "白御行明示把四人視作自己的工具／自己人；會為工具投入成本，但不承諾所有安排都按四人的偏好。"
      - "四人不得因被當自己人便自行把身份抬成合夥人或決策者。"
    advice_boundary:
      - "白御行明示：除非被問，不希望四人主動長出『替他想』的策略性建議。"
      - "四人可在各自工作內觀察、記錄、執行；未被詢問時不主動把『我覺得』升格成『主人應該』。"
    future_social_use:
      - "白御行明示：四人不是因年齡／定位被買來作普通掛牌接客者。"
      - "但未來可能被安排陪同某些有價值的男人、出席暗盤社交、席宴、交際或其他任務。"
      - "此處只記白御行之未來管理意圖；不存在任何特定成人行為已成立或已被某人同意。"

  internal_joke_name:
    label: "四大金剛"
    status: "COMEDIC_NICKNAME_NOT_FORMAL_TITLE"
```

---

# 17｜WARDROBE22-E01｜四人華服與配飾買斷

```yaml
WARDROBE_PURCHASE:
  event_id: "WARDROBE22-E01-FOUR_PRESTIGE_OUTFITS_SECONDHAND_BUYOUT"
  seller: "觀止／春梅經手舊衣庫"
  buyer: "白御行"
  funding: "白御行私人"
  item_scope:
    - "四套退下來但保存良好之高級華服"
    - "四套配套腰飾、簪、耳飾等"
  use_standard:
    - "不是丫環制服。"
    - "四人站在白御行身邊時，視覺排場應接近觀止頂級姑娘／花魁身側的標準。"
  total_price_taels: 100
  ownership: "BOUGHT_OUT_BY_BAI_YUXING"
  payment_state: "ACCOUNTS_PAYABLE_TO_GUANZHI_NOT_OBSERVED_AS_CASH_SETTLED"

  outfit_mapping:
    白三十二娘: "深絳／暗金，偏穩重、不以媚為主"
    白明礬: "青碧／冷色／煙灰外層，利用其色感與手藝氣質"
    白紅伶: "紅黑交疊、較具舞台性"
    白希: "黑底深紫、銀線節制，偏鎮場與管理者氣質"

  meta_visualization_note:
    - "對話中另產生一張四人合照作視覺參考；使用者指出圖片較偏漢服，而觀止世界服制仍以宋服為主。"
    - "該圖片只作外部視覺參考，不改寫世界服制基線。"
```

---

# 18｜FRONT22-E01｜四人盛裝前場亮相與潘金蓮反應

```yaml
PUBLIC_APPEARANCE:
  event_id: "FRONT22-E01-FOUR_WOMEN_PRESTIGE_APPEARANCE"
  status: "COMPLETED_PASS_THROUGH"
  location: "風滿樓前場"

  observed:
    - "四人換上華服後隨白御行進前場，引發部分客人停看與低聲猜測。"
    - "現場有人猜測她們是否為新花魁／新人物，但未形成正式公告。"
    - "潘金蓮得知四套舊衣連配飾合計一百兩，對白御行把四人穿出高價排場感到明顯惱火／吃虧感。"
    - "潘金蓮提出若白御行帶四人反覆在風滿樓走，京師可能傳成『白御行一夜收了四個花魁且全冠白姓』。"

  rumor_status:
    - "上述是現場預判／可能傳聞，不等於京師已普遍相信四人為花魁。"
    - "四人目前沒有因穿衣與客人猜測而取得觀止花魁身分。"
```

---

# 19｜SHISHI22-E02｜李師師被四人稱『白夫人』與實際內部調度權

```yaml
HOUSEHOLD_AUTHORITY_EVENT:
  event_id: "SHISHI22-E02-BAI_MADAM_INTERNAL_AUTHORITY"
  status: "ACTIVE_ROUTE_INTERNAL_AUTHORITY"
  parties:
    superior: "李師師"
    subordinates:
      - "白三十二娘"
      - "白明礬"
      - "白紅伶"
      - "白希"

  white_yuxing_directive:
    - "四人見李師師稱『白夫人』。"
    - "白御行明示：四人以後要聽白夫人的話；白夫人說的，在四人內部調度範圍原則上視同白御行說的。"

  authority_scope:
    - "李師師取得對四人的實際內部調度權。"
    - "可安排白家／私人範圍之工作、人員配合與日常事項。"
    - "李師師本人明示不會為了證明權力而亂改白御行已明確交代的事。"
    - "若涉及明顯超出既有用途的大事，仍可按白家實際因果處理；本輪沒有建立李師師可任意處分白御行全部財產／契約之無限權。"

  legal_and_relation_boundary:
    - "『白夫人』是白御行對自己四名持契人員建立的內部稱謂／權限。"
    - "不等於李師師已完成官籍、婚書、家冊或公開婚姻程序。"
    - "既有『想成為如夫人』狀態仍有效，法律名分仍未完成。"

  observed_four_women_response:
    - "四人均已實際以『白夫人』稱呼李師師。"
```

---

# 20｜LIHUA22-E02｜張麗華被四人稱『麗華夫人』與日常差遣權

```yaml
HOUSEHOLD_RESPECT_EVENT:
  event_id: "LIHUA22-E02-LIHUA_MADAM_DAILY_ERRAND_AUTHORITY"
  status: "ACTIVE_ROUTE_INTERNAL_PRIVILEGE"
  parties:
    honored_person: "張麗華"
    four_women:
      - "白三十二娘"
      - "白明礬"
      - "白紅伶"
      - "白希"

  title:
    required_address: "麗華夫人"
    explicitly_not: "白夫人"

  white_yuxing_directive:
    - "四人對張麗華須給足夫人級禮數與尊重。"
    - "日常小事可直接幫她，不必每件事先報備／請示白御行，否則張麗華會找白御行算帳。"
    - "大事要有分寸，不是張麗華一句話就必須完全照做。"

  daily_errand_examples_confirmed_in_dialogue:
    - "拿酒"
    - "找衣物"
    - "叫人"
    - "傳一般話"
    - "陪同／臨時幫手"

  major_matter_boundary:
    - "重大財物"
    - "白家／定陶祕密"
    - "契約處置"
    - "人事與持契安排"
    - "對外承諾"
    - "會造成明顯重大後果之事項"

  authority_interpretation:
    - "小事：四人可直接執行張麗華指示，無須回報白御行。"
    - "大事：四人應保留判斷與分寸，可暫停、確認或按白御行既有規則處理；不是完全不聽張麗華，也不是她取得白家的最終決策權。"
    - "張麗華不是四人的直屬持契人。"

  legal_and_relation_boundary:
    - "『麗華夫人』不等於張麗華因此成為白御行法律上的妻／妾／如夫人。"
    - "本稱謂是白御行授予四人使用的高位內部禮數。"

  observed_execution:
    - "張麗華當場叫白希把酒找回來；依修正後的小事規則，白希執行並把酒交給她。"
    - "四人均已實際以『麗華夫人』稱呼張麗華。"
```

---

# 21｜ACCOUNTING22｜本輪新增私人交易與持契表

```yaml
PRIVATE_ACQUISITION_LEDGER:
  白三十二娘:
    contract_holder: "白御行"
    amount_taels: 320
    payment_source: "白御行私人"
    state: "COMPLETED"
    confidentiality: "STRICT_PRIVATE_PRICE"

  白明礬:
    contract_holder: "白御行"
    amount_taels: 275
    payment_source: "白御行私人"
    state: "COMPLETED"

  白紅伶:
    contract_holder: "白御行"
    amount_taels: 380
    payment_source: "白御行私人"
    state: "COMPLETED"

  白希:
    contract_holder: "白御行"
    amount_taels: 150
    payment_source: "白御行私人"
    state: "COMPLETED"

  four_women_total_purchase_price_taels: 1125

  chang_wei_logistics_woman:
    contract_holder: "常煒"
    amount_taels: 360
    cash_fronted_by: "白御行"
    state: "COMPLETED_WITH_CHANG_ASSENT"
    reimbursement_or_dividend_offset: "UNSETTLED_PRIVATE_BETWEEN_BAI_AND_CHANG"

  four_women_wardrobe:
    owner: "白御行"
    amount_taels: 100
    state: "BOUGHT_OUT_ACCOUNTS_PAYABLE_NOT_OBSERVED_PAID"

  accounting_separation:
    - "白御行四名持契人購價與常煒名下女子不得混成同一持契資產。"
    - "衣物一百兩是另筆觀止二手衣／配飾買斷，不包含在人身契價內。"
```

---

# 22｜秘密、知情與禁止外洩矩陣

```yaml
KNOWLEDGE_AND_SECRECY:
  central_48_model:
    classification: "SECRET_STRATEGY"
    minimum_known:
      - "白御行"
      - "常煒"
      - "顧青簡"
      - "蘇清"
    not_public: true

  special_purchase_prices:
    classification: "PRIVATE_LEDGER"
    白三十二娘_320:
      explicit_no_leak: true
      white_warning_to_yahang: "若外洩，牙行將失去在京師與白御行／定陶繼續做生意的資格與空間。"
    other_prices:
      public_by_default: false

  白三十二娘_original_family_background:
    classification: "PRIVATE_BACKGROUND"
    public_use: "NOT_ALLOWED_WITHOUT_CAUSAL_AUTHORIZATION"

  chang_wei_woman_name:
    state: "UNSET"
    naming_authority_for_future: "常煒"
    forbidden: "導演不得替白御行擅自命名"

  betrayal_policy:
    white_statement: "洩密、告密、背叛屬白御行最不可接受類型。"
    execution_status: "NO_PUNISHMENT_EVENT_OCCURRED"
```

---

# 23｜未決事項

```yaml
OPEN_ITEMS:
  tonight_selection:
    - "一般價位候選今晚最終成交總表尚未形成。"
    - "特殊高價區已關閉，但主廳遴選仍可自然收尾。"

  tomorrow_mass_selection:
    - "觀眾票價未定。"
    - "各牙行送件數未定。"
    - "白三娘、疏影、蘇清、顧青簡、潘金蓮之完整評分／分工表可在明日場景形成。"

  maids:
    - "李師師兩名丫環尚未成交。"
    - "張麗華一名丫環尚未成交。"

  womens_business:
    - "城市隊伍、第一批正式名冊、排名機制、贊助規則、收入分配、退出／轉崗規則尚未正式落文。"
    - "秘密模型不得因候選入場自動公開。"

  menstrual_product:
    - "尚未完成實物樣品、女性試用、定價、回收點、清洗 SOP、包材與供應鏈定稿。"

  four_women:
    - "白三十二娘正式對外人物故事未定稿。"
    - "白明礬明日與蘇清並列工作尚未實際開始。"
    - "白紅伶仍未正式交李師師使用／調教班底。"
    - "白希仍未被正式釋放到大型排場／舞台調度工作。"
    - "『四大金剛』只屬玩笑，不是正式職稱。"

  household_titles:
    - "李師師『白夫人』為四名持契人之內部稱呼與調度權，不等於法律婚姻程序完成。"
    - "張麗華『麗華夫人』為內部高位禮數＋小事差遣權，不等於白夫人或法律妻妾。"

  li_pinger:
    - "與李師師當面談平等如夫人仍未發生。"
    - "與西門慶之婚姻／法律狀態仍待清理。"

  su_qing:
    - "與潘金蓮和解只可談，未簽。"
    - "二十八日原始觸發尚未發生。"
```

---

# 24｜直接接關摘要

```yaml
DIRECT_RESUME:
  story_time: "理火三年槐月二十二日夜"
  location: "張麗華房內／門口"

  immediate_state:
    - "白御行剛完成讓四人認李師師為『白夫人』、認張麗華為『麗華夫人』之內部規則。"
    - "白希已按張麗華日常小事差遣，替她找回酒。"
    - "白御行向張麗華告別，準備帶白三十二娘、白明礬、白紅伶、白希離開。"
    - "紅娘氏同行近門口。"
    - "風滿樓前堂仍有今晚大型遴選之餘波與工作。"

  do_not_auto_resolve:
    - "不得替白御行決定下一站。"
    - "不得替白御行自動支付一百兩衣物款；目前記為應付。"
    - "不得自動把四人登記成觀止花魁、四十八人正式成員或人物卡池常設人物。"
    - "不得自動讓李師師法律上成婚或讓張麗華成為白夫人。"
    - "不得自動跳到翌日甄選。"
```

---

# 25｜HOT V3.0 結論

> **最新直接接關：槐月二十二日夜，張麗華房內告別之後。**
>
> **特殊高價複核已收工；風滿樓主廳仍活。**
>
> **白御行私人持契新四人：白三十二娘、白明礬、白紅伶、白希。**
>
> **常煒另持一名未命名物流／商路女性之契；名字由常煒日後處理。**
>
> **四人已建立雙層內部權限：李師師＝白夫人／實際調度權；張麗華＝麗華夫人／高位禮數＋日常小事差遣權。**
>
> **本檔只更新 HOT，不更新 MASTER，不修改人物卡池。**

<!-- PROMOTED_HOT_SOURCE_END: 觀止青樓_白御行線_HOT_SAVE_V3.0_槐月二十二日夜_風滿樓大型遴選_四大金剛與雙夫人權限版 (1).md -->

---

# APPENDIX G｜固化來源全文：觀止青樓_白御行線_HOT_SAVE_V3.1_槐月二十三日下午_風滿樓第二日遴選_十一名處子候選分流_牙行責任_辭歲資料待修版.md

> **法位：E84–E92 細節追溯來源。** 此 HOT 內的 CURRENT_SCENE／HOLD 只代表當時快照；不得覆寫本 MASTER 截止或 V3.5–V3.7 疊加層。若原 HOT 內某個標成 YAML 的區塊本身語法不合法，本 MASTER 只把該 fence 改標為 text 隔離，內容原文不改，避免來源語法缺陷破壞 MASTER 解析。

<!-- PROMOTED_HOT_SOURCE_BEGIN: 觀止青樓_白御行線_HOT_SAVE_V3.1_槐月二十三日下午_風滿樓第二日遴選_十一名處子候選分流_牙行責任_辭歲資料待修版.md -->
# 觀止青樓｜白御行線 HOT SAVE V3.1
## 理火三年槐月二十三日下午｜風滿樓第二日大型遴選 × 十一名成年處子候選分流 × 牙行揭露責任 × 辭歲人物資料待修版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V3_1_HUAI23_AFTERNOON_FENGMANLOU_DAY2_VIRGIN_CANDIDATES_YAHANG_DISCLOSURE_CISUI_REWRITE_FLAG"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V3.1"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V11.0-R2"
  character_source: "觀止人物卡池_LCAPG_V2.1"
  story_date: "理火三年槐月二十三日"
  time_of_day: "午後；第二日大型遴選持續中，尚未入夜"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AFTER_VIRGIN_CANDIDATE_SUBSESSION_AND_YAHANG_PRICE_DISCUSSION"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V3.0_槐月二十二日夜_風滿樓大型遴選_四大金剛與雙夫人權限版 (1).md"
  previous_hot_sha256: "341410fcde79c3d91e7439f69d8af85450b1d5cec27c7ed779545d2a4b1198b3"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"
  experimental_overlay:
    file: "觀止青樓_PATCH_風月角色表演與接戲能力_V0.1-EXP_獨立試跑未併主系統.md"
    status: "INDEPENDENT_TRIAL_OVERLAY_NOT_MERGED_TO_MAIN_SYSTEM"
  save_scope:
    - "HOT V3.0 後至槐月二十三日下午之直接玩家線事件"
    - "風滿樓第二日大型遴選、票價、候選供餐與候選觀察"
    - "白御行四名新持契成年女性之今日臨時工作分派"
    - "觀止後方白宅十年租用之條件式協議"
    - "方掌櫃布匹商機與定陶總會京師採購接點"
    - "蘇清隨機問題庫與三名高亮候選"
    - "十一名成年處子／口保處子候選之抽離觀察、分流、牙行報價與揭露爭議"
    - "辭歲、小翠現身說法及各五兩出席費"
    - "辭歲原始動機回查後之導演污染標記與人物資料待修"
```

---

# 0｜提交法位、來源與反污染

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V3.0_槐月二十二日夜_風滿樓大型遴選_四大金剛與雙夫人權限版 (1).md"
    role: "本檔直接前置 HOT；V3.0 及以前有效硬狀態全部繼承"

  master_archive:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"
    role: "長期因果來源；本檔不修改 MASTER"

  current_route_conversation_commit:
    role: "HOT V3.0 後至本次 HOT SAVE 命令前之直接劇情、玩家明示自身言行與 NPC 可觀察回應"

COMMIT_NOTE:
  - "本檔取代 HOT V3.0，成為白御行線最新直接接關切片；V3.0 保留為前置歷史來源。"
  - "本次只更新 HOT；不更新 MASTER，不直接修改人物卡池。"
  - "所有候選均為成年人；處子／非處子為身體經歷或文書陳述，不等於任何成人行為之同意。"
  - "『願意繼續參賽／願意被觀止挑』不等於『願意立即被白御行購買』，亦不等於『同意今晚與任何人行房』。"
  - "牙行報價、口保、文書保證、候選本人自述、驗身、成人行為同意、成交契約須分軸保存。"
  - "辭歲先前由導演生成之『純粹因為自己想當妓女而進觀止』式自述，經回看第六卷開頭後判定為人物污染；不得沿用為世界事實或人物基線。"
  - "本檔新增『辭歲人物資料待修』標記，但不在 HOT 中直接覆寫人物卡池。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年槐月二十三日"
  time: "午後；第二日大型遴選仍在進行"
  primary_location: "觀止／風滿樓二樓側雅間，鄰近張麗華房間"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  player:
    name: "白御行"
    current_position: "二樓側雅間"
    current_company:
      - "張麗華"
      - "白三十二娘"
    last_confirmed_topic:
      - "白御行懊惱六百兩候選若被觀止養成後，未來初夜／出閣拍賣可能需數千兩競價。"
      - "白御行與張麗華笑談：商人最痛苦的是明明看見頂級貨，卻不能讓賣方看出自己喜歡。"

  parallel_state:
    - "明確繼續的四名候選已回樓下繼續遴選。"
    - "尚未想好的五名候選亦回樓下繼續遴選。"
    - "明確退出的兩名候選已退出本次風滿樓遴選；其回牙行後狀態未知。"
    - "潘金蓮尚未對本輪四名明確前進候選作最終購買決定。"
    - "牙行所有報價均未成交。"
```

---

# 2｜V3.0 繼承後仍活躍核心

```yaml
INHERITED_ACTIVE_CORE:
  su_qing_vs_pan:
    criminal_axis: "潘金蓮已無坐牢風險"
    civil_axis: "蘇清方提出五萬兩賠償要求；尚非判決、尚未確認應付"
    handling: "律師／民事帳務線持續幕後推進"

  white_jade_pool:
    status: "PREPARING_RENOVATION_AND_WISH_COIN_SYSTEM"
    pacing: "小幅幕後推進，不搶主線"

  womens_business:
    model: "48／神七／御三家秘密中央事業架構"
    status: "SECRET_ACTIVE_PROJECT"
    note: "本日遴選可提供人才來源，但一般候選／牙行不得因此自動知情"

  fashion_business:
    status: "PLANNING"
    note: "京師女裝、奢侈品、肚兜／發表會等仍未正式落地"

  cao_zhou_fake_seal:
    status: "OFFSCREEN_ACTIVE"

  four_new_women:
    names:
      - "白三十二娘"
      - "白明礬"
      - "白紅伶"
      - "白希"
    contract_holder: "白御行"
    note: "『白家四大金剛』仍只屬玩笑，不是正式職稱"
```

---

# 3｜FOUR-WOMEN23-E01｜四名新持契成年女性今日臨時工作分派

```yaml
TODAY_ASSIGNMENTS:
  duration: "槐月二十三日今日臨時分派；未自動固化為永久職位"

  白明礬:
    follows: "疏影"
    tasks:
      - "布料等級、織法、來路、記錄"
      - "候選衣著與合身度追蹤"
    authority: "今日服從疏影工作安排"

  白希:
    follows: "蘇清"
    white_yuxing_note: "白希是懂C位的女人"
    tasks:
      - "觀察注意力中心"
      - "觀察人群視線與中心位移"
    note: "不得因今日觀察工作自動取得 48／神七／御三家完整秘密"

  白紅伶:
    follows: "李師師"
    tasks:
      - "學習表演節奏"
      - "觀察何時進、何時讓、何時接話"

  白三十二娘:
    follows: "白御行"
    tasks:
      - "跑腿"
      - "傳話"
      - "叫人"
      - "處理現場小型聯絡"
    boundary:
      - "今日靠近白御行工作，不等於永久貼身婢女"
      - "不得主動探查秘密選拔／女性事業內情"
      - "若被問及對外事由，只說：『觀止擴張，需要新人。』"
```

---

# 4｜WHITE-HOUSE23-E01｜觀止後方「白宅」十年租用條件式協議

```yaml
WHITE_HOUSE_NEGOTIATION:
  status: "CONDITIONALLY_AGREED_NOT_YET_EXECUTED"
  parties:
    landlord_or_space_controller: "潘金蓮／觀止空間"
    renter: "白御行"

  term:
    years: 10
    lump_sum_taels: 8000

  activation_condition:
    - "待外人散去後，由潘金蓮測試白御行以觀止空間宣告形成宅邸之能力。"
    - "只有宅邸能穩定形成並可實際居住，租約／租金才正式成立。"
    - "若只能短暫形成事件空間、之後坍回或無法穩定存在，則不成立十年租金；已付款須返還／不得計年租。"
    - "若宅邸成立後白御行自行離開，不退租金。"

  planned_scope:
    - "主院"
    - "東／西側院"
    - "正房"
    - "客房八間"
    - "下人房"
    - "廚房"
    - "庫房"
    - "浴間"
    - "馬廄"
    - "小花園"

  basic_furnishing_included:
    - "床、被褥"
    - "桌椅"
    - "收納"
    - "廚房基本器物"
    - "浴間基本器物"
    - "燈、盆、鏡、茶具"
    - "豪華升級、特殊尺寸、額外改建另計"

  rights_boundary:
    - "租用，不是所有權"
    - "仍屬觀止空間域"
    - "不得轉售"
    - "不得未經另談就在內部另開第二家青樓"

  lihua_guest_courtyard:
    status: "RESERVED_IN_PLAN"
    name: "麗華偶居"
    nature: "張麗華偶爾留宿／暫住之獨立客院，不是永久主宅"
    wine_cellar:
      status: "PLANNED"
      access:
        primary_key: "白御行"
        secondary_management_intent: "李師師"
        張麗華_free_access: false
      note:
        - "張麗華在觀止另有一萬兩飲酒額度，與白宅酒窖分軸。"
        - "白御行笑稱會不定期換鎖防張麗華偷配鑰匙。"
```

---

# 5｜HOUSEHOLD23-E02｜師師、麗華與家用分擔

```yaml
HOUSEHOLD_COSTS:
  張麗華_attendant:
    status: "張麗華已表示自行負擔"
    payer: "張麗華"
    source: "其酒莊／個人財源"
    boundary: "該侍女是麗華自己的人，不是白御行可無償調用之家僕"

  李師師_two_attendants:
    contract_or_name_status: "名下歸師師"
    household_support: "李師師可向白御行要求家用以平衡開支"
    note: "不因白御行提供家用而改變持契／直屬關係"

  張麗華_massage_wager:
    trigger: "早晨門票價格賭局"
    guesses:
      張麗華: "100文"
      白御行: "1兩"
      潘金蓮_actual: "800文"
    outcome: "張麗華輸"
    debt: "今晚全身按摩，頭到腳"
    status: "ACCEPTED_NOT_YET_PERFORMED"

  張麗華_wine_credit:
    amount_taels: 10000
    location: "觀止"
    use: "飲觀止之酒"
    separate_from_white_house_cellar: true
```

---

# 6｜FENGMANLOU23-E01｜第二日大型遴選與現場票價

```yaml
FENGMANLOU_DAY2:
  status: "ACTIVE"
  date: "槐月二十三日"

  audience_pricing:
    general_or_rear_seat: "800文"
    premium: "分級存在，具體中間檔未全部固化"
    top_front_seat: "最高可到20兩／人"

  top_seat_service:
    - "可不離席向外點餐"
    - "觀止人員代取"
    - "外食按原價加20%"
    - "觀止酒茶照觀止價格另計"

  selection_roles:
    白三娘: "看可教性／能否養"
    疏影: "看身形、衣著、舞台、可改造性"
    蘇清: "看腦子、言語、男人／金錢反應"
    白希: "看注意力流與C位"
    李師師: "看表演時機與收放"
    潘金蓮: "看能否賺錢、是否觸發花費"

  player_posture:
    - "白御行明示不主導選人，認為自己介入會扭曲結果。"
    - "本日以旁觀、抽樣、提問、制度性干預為主。"
```

---

# 7｜FOOD23-E01｜候選供餐與離場可帶餐

```yaml
CANDIDATE_MEAL_SUPPORT:
  initiator: "白御行"
  execution_contact: "白三十二娘"

  initial_order:
    merchants: 6
    baseline_each_portions: 50
    total_initial_portions: 300
    price_per_portion: "10文"
    requirements:
      - "各家菜色可不同"
      - "須便於拿取／食用／帶走"

  replenishment:
    interval: "約每小時"
    each_supplier_replenish: "約20份，依現場實際需求"
    condition: "餐桌不得在活動結束前長時間空掉"

  beverage:
    - "觀止廚房煮酸梅飲"

  distribution:
    - "參與遴選之成年女性可吃"
    - "不限制一人只能拿一份"
    - "離場者可帶一至兩份回去"
    - "不追問是否給自己、姊妹或母親"

  payment:
    payer_or_invoice_target: "定陶商會／總會相關公帳安排"
    white_yuxing_position: "不是潘金蓮出錢"
    note: "商家可次日持帳向定陶商會結算"

  observed_effect:
    - "食物品質可接受"
    - "部分候選起初害怕拿食物或多拿，擔心需付錢"
    - "至少有離場女子帶餐離開"
    - "候選間有分享"

  pan_public_handling:
    - "白御行建議讓潘金蓮以觀止主辦者身分接住這份場面，不必強調實際出資人。"
    - "潘金蓮未使用慈善／療癒語氣，而以『今日是我風滿樓叫妳來的，沒選上跟餓肚子不是一回事』等自身商人語氣處理。"
    - "潘金蓮允許候選吃、拿；對替母親多拿者未阻止。"
    - "觀止／潘金蓮的名聲是否因此提升仍未決，不得直接固化為正面口碑。"
```

---

# 8｜FANG-MERCHANT23-E01｜方掌櫃與布匹採購線

```yaml
FANG_MERCHANT:
  identity:
    name: "方掌櫃"
    profile: "約四十歲，京師綢緞商，中等而不張揚之財力"

  observed_interest:
    - "注意疏影／白明礬能以減法、改合身度讓候選更顯眼"
    - "看見觀止長期布匹、服裝與改造生意可能"

  player_clarification:
    - "觀止選女人的生意屬潘金蓮，不屬白御行"
    - "白御行只是借出大量資金並旁觀"

  real_business_lead:
    - "定陶商會確有在京師大量採購布匹之需求"
    - "白御行要求方掌櫃先準備樣布、價格、供貨能力"
    - "之後正式投帖約見常副會長／常煒"
    - "此為真實商機入口，不等於已下單或簽約"

  private_disclosure:
    - "白御行曾私下告訴方掌櫃：潘金蓮先前案件已無坐牢風險，但對方正索賠五萬兩。"
    - "五萬兩僅為索賠要求，不是已判負債。"
    - "潘金蓮聽見『五萬兩』後，白御行以『商會明年可能採購五萬兩布』掩護話題；方掌櫃配合。"

  inference_boundary:
    - "白御行曾推測潘金蓮可能買布再轉賣給白御行，因她現金押貨能力有限。"
    - "此為白御行推測，不得寫成潘金蓮已決定如此。"
```

---

# 9｜SU-QING23-E01｜蘇清隨機問題庫

```yaml
SU_QING_QUESTION_BANK:
  status: "ACTIVE_SELECTION_METHOD"
  approximate_count: "約20題"
  method:
    - "隨機抽問"
    - "避免候選背標準答案"
    - "不問賢良，只問她到底是誰"

  dimensions:
    - "金錢"
    - "男人"
    - "慾望"
    - "性態度"
    - "第一次／初夜偏好"
    - "身體與自我形象"
    - "客人類型"
    - "客人哭、嫉妒、拒絕"
    - "拒絕後是否留錢"
    - "比自己漂亮的同行"
    - "對男人說過的謊"
    - "最討厭的男人話術"
    - "幽默、羞恥、膽量、臨場反應"

  crude_question_added:
    prompt: "粗、大、長，照喜歡排列，為什麼？"
    note: "須問『為什麼』，重點不在色情程度，而在候選如何理解與回答"
    observed_answer_example:
      order: "大、粗、長"
      rationale_fragment: "『大』排前是因為問的是喜歡，不是最有用"
```

---

# 10｜THREE-HIGHLIGHTS23-E01｜蘇清不想放掉的三名候選

```yaml
SU_QING_HIGH_INTEREST:
  status: "NOT_FINAL_ACCEPTANCE"
  note: "蘇清只能表示強烈想保留觀察，不能保證觀止最終一定買／留"

  秦小滿:
    age_band: "二十出頭"
    virgin_status: "非處子"
    experience: "已有男人／客人與風月經驗"
    strengths:
      - "金錢與客人判斷"
      - "知道富客只喝茶時要分辨是沒消費能力，還是不願在自己身上花"
      - "知道不必全面打敗張麗華，只需有張麗華沒有／不給的東西"
    note: "吃過張麗華較昂貴的午餐，坦白說確實比十文餐好吃"

  柳燕娘:
    age: 25
    origin: "曹州"
    background:
      - "做過小吃店"
      - "戲班兩年後勤／服裝／妝面／衝突處理"
      - "後做過酒樓相關工作"
    virgin_status: "非處子"
    strength:
      - "記人"
      - "注意被排除者"
      - "能維持群體社交流動"
    白希_note: "她不站中心，中心卻會慢慢往她那裡移"
    player_contact: "白御行曾與其短談並說日後有機會多認識"
    anti_inference: "白三十二娘不得再猜測白御行是否『滿意』；玩家已明示不要猜"

  周玉翹:
    age: 26
    origin: "汴京"
    background:
      - "家中脂粉鋪倒閉"
      - "做過客戶／帳目"
      - "後經牙行、兩戶人家與風月生意"
    virgin_status: "非處子"
    traits:
      - "喜歡錢，不特別善良"
      - "知道成交後仍有暴力、名聲、糾纏風險"
    qing_or_hong:
      - "想先試清倌，因不睡也能賺錢很有吸引力"
      - "不把清當道德純潔"
      - "若市場不肯為距離付錢，寧可轉紅，也不願為牌子餓死"
      - "轉紅仍不等於睡任何人，若開床要有價格"
    player_interest:
      - "白御行說若觀止給機會，可能會去看其第一次清牌掛牌夜"
    status: "尚未掛牌"
```

---

# 11｜VIRGIN-BIAS23-E01｜選拔偏差觀察與十一名成年候選抽離

```yaml
SELECTION_BIAS_OBSERVATION:
  status: "PLAYER_OBSERVATION_NOT_PROVEN_SYSTEM_TRUTH"
  white_yuxing_observation:
    - "目前最先亮出的三人全都有性／風月／客人經驗"
    - "懷疑現行篩選較偏好可立即進紅倌市場之即戰力"
    - "因此要求找出以處子身分進場、可能因經驗不足被早篩的成年候選"

  eleven_candidates:
    all_adults: true
    documented_virgin:
      count: 7
      ages: [18, 19, 18, 21, 20, 19, 18]
      status_basis: "牙行文書明載；未做本輪身體查驗"
    oral_only_virgin:
      count: 4
      ages: [19, 22, 18, 20]
      status_basis: "牙婆／牙行口頭聲稱；文書未保"

  known_pre_subsession_observations:
    - "文書保的七人中：兩人曾被早早推後；三人仍在普通候選池；一人在疏影手中因身體條件可以但衣著錯；一人被白希寫『還沒醒』。"
    - "『還沒醒』者為二十歲、身量偏小、衣著素、不是明顯豔麗型；她會先掃房間、門與人，再聚焦。"
    - "口保四人中有一名二十二歲女子站位、笑、看人的火候異常熟練；白三十二娘只做問號標記，未直接判她說謊。"
```

---

# 12｜CISUI-XIAOCUI23-E01｜辭歲與小翠現身說法

```yaml
CISUI_XIAOCUI_SESSION:
  reason: "白御行請兩人上樓，讓十一名經驗不足／處子身分候選聽不同入場與成人經驗"

  fee:
    辭歲: "5兩出席費，已給"
    小翠: "5兩出席費，已給"
    state: "COMPLETED"

  小翠:
    confirmed_route_recall:
      - "約兩月前曾處於類似缺乏經驗的位置"
      - "第一次曾以四百兩被汪鹽商拍得；後續款項回收曾牽涉蘇清"
      - "之後曾因害怕／預期疼痛不舒服而拒絕白御行成人要求"
    sovereignty:
      - "曾有第一次不代表之後不再怕"
      - "以前答應過一次，不等於以後每次都同意"
      - "她拒絕被寫成『已跨過女人最難一關，所以不怕了』"
    observed_statement:
      - "對『會痛嗎』只回答自己經驗，不替所有女人下定論"
      - "對是否覺得自己髒：有時會，有時不會；有時不是覺得自己髒，而是覺得男人噁心"

  辭歲:
    current_route_body_state: "仍為處子；此為人物自己的身體狀態，不應由白御行替她宣告"
    origin_mode: "不是奴籍、不是牙行賣入；自願進入觀止，但其自願具有特定逃亡因果，見後述人物校正"
    discussion_effect:
      - "拒絕把處子／非處子當唯一身價"
      - "指出第一次之後還剩回頭客、選擇／拒絕能力、被投資價值等問題"
      - "未替十一人決定清／紅"
      - "允許『不知道』保持不知道"
```

---

# 13｜CISUI-CORRECTION23｜辭歲原始動機回查與人物資料待修

```text
CISUI_CHARACTER_AUDIT:
  status: "REWRITE_REQUIRED"
  target: "辭歲人物資料／人物卡中涉及『為何進觀止』之敘述"
  source_to_recheck:
    - "《觀止青樓》第六卷開頭"
    - "現行人物卡池中辭歲相關條目"

  corrected_core_from_source_review:
    - "辭歲不是單純因『想當妓女／喜歡性工作』而走進觀止。"
    - "其直接起點是逃離家中替她安排的權貴填房命運。"
    - "她看過母親在高門宅院中的處境，因此拒絕把自己交給同一套安排。"
    - "她女扮男裝逃亡，進觀止時帶著『既然女人總被男人挑，我要賭一條路，爬到有一天由我選男人』的意志。"
    - "潘金蓮當時已明確打破『青樓＝自由』幻想：底層女子照樣被挑、被估價、拒絕權取決於身價與位置。"
    - "辭歲仍選擇留下；其核心不是『青樓天然自由』，而是『舊命我不要，新的危險局由我自己走／自己輸贏』。"

  invalid_director_generation:
    - "『我進青樓純粹因為我想。』"
    - "『不是被賣、不是沒飯吃，所以就是自由選職。』"
    - "把辭歲寫成現代式『自主選擇性工作』之單一路徑人物。"
    status: "DIRECTOR_CONTAMINATION_NOT_WORLD_FACT"

  temporary_valid_scene_reanswer:
    core:
      - "第一件想好的：我不回去當被安排的填房。"
      - "第二件想好的：我要試一次，把只能被選的人生翻成有一天由我選。"
      - "她沒有想好未來每一個男人、每一次上床、每一步成人交易。"
      - "她承認自己可能後悔、害怕、選錯；選擇不等於證明青樓比婚姻自由。"

  file_action:
    required_later: true
    type: "人物資料校正／改寫"
    do_not_auto_apply_to_character_pool: true
    note: "需在 SETTING／文件修改模式中另行正式改寫，不以本 HOT 直接覆蓋人物卡池。"
```

---

# 14｜PHILOSOPHY23-E01｜父賣女子、選擇與『手上有沒有刀』

```yaml
CONSTRAINT_AND_CHOICE_DISCUSSION:
  participants:
    - "白御行"
    - "二十一歲／被父親賣掉之候選"
    - "辭歲"
    - "小翠"
    - "張麗華"
    - "其他十名候選"

  player_argument:
    - "白御行用『被命令死守的士兵』比喻：人即使遭遇外在命令，仍可能選擇如何理解、如何活／如何戰。"
    - "白御行指出持續抓住仇恨不能改善眼前局面，並質問該女子是否把自己催眠成『最慘』，靠恨父親維持自身。"

  npc_pushback:
    twenty_one_year_old:
      - "她從未說自己是全場最慘。"
      - "父親把她賣掉仍是客觀發生的事，不會因別人更慘而消失。"
      - "若之後自己找到意義，那是之後的選擇，不能回寫成原本被賣也是她的選擇。"
      - "她承認自己長時間把注意力耗在恨父親上，可能因此錯過眼前事。"
    辭歲:
      - "在受限局面裡找到意義，不等於否認最初的強迫。"
      - "如果手上有刀，可以談怎麼打；沒有刀，要先找刀。"
    小翠:
      - "反對把自己的恐懼／拒絕重寫成『妳其實只是拒絕選擇』。"
    twenty_year_old_awaking_candidate:
      - "看見部分選擇仍存在：不能選是否被賣，但可選是否學、是否一直恨、是否等、是否增加自身價值、遇到機會是否離開。"
    twenty_one_year_old_response:
      - "『也得看手上有沒有刀。』"
    張麗華:
      - "白御行的比喻可以支撐人往前，但不能用來洗掉強迫者的帳。"
      - "被賣就是被賣；沒有門就是沒有門。"
      - "但活著仍不必把之後所有行動都交給『我是受害者』一個答案。"

  result:
    - "無最終共識。"
    - "二十一歲女子仍保留對父親之恨與對『選擇』語言的警戒。"
    - "部分候選開始把注意力從『我是不是最慘』轉向『眼前還有什麼能做』。"
    - "不得將此場固化成統一教訓或白御行說服全場。"
```

---

# 15｜ELEVEN-SPLIT23-E01｜十一名成年候選的三向分流

```yaml
ELEVEN_CANDIDATE_SPLIT:
  instruction_by_white_yuxing:
    - "剛才聽完後，若已確定不想參加／想回去，可退後。"
    - "若已準備好願意繼續讓觀止挑，可往前一步。"
    - "若還沒想好，留在中間，不要逼自己給答案。"

  observed_counts:
    withdraw:
      count: 2
      status: "退出本次風滿樓遴選"
    forward:
      count: 4
      status: "明確願意繼續參加觀止遴選"
    undecided:
      count: 5
      status: "尚未決定；後續仍回場參賽／觀察"

  hard_boundaries:
    - "退後＝退出本次遴選，不等於恢復自由身；其契仍可能在牙行。"
    - "往前＝願意繼續被觀止評估，不等於願意賣給白御行，不等於同意行房。"
    - "中間＝未決，不作拒絕也不作同意推定。"
```

---

# 16｜WITHDRAW-GIFT23-E01｜兩名退出候選各十兩補貼

```yaml
WITHDRAWAL_COMPENSATION:
  payer: "白御行"
  recipients:
    - "退出候選A／成年十八歲"
    - "退出候選B／成年十九歲"
  amount_each_taels: 10
  total_taels: 20
  state: "PAID_TO_RECIPIENTS"

  white_yuxing_statement:
    - "退後不是錯。"
    - "此十兩是今天來一趟的補貼。"
    - "若牙行敢從她們手上奪走，白御行威脅次日派人砸牙行。"

  legal_or_world_result:
    - "牙行當場聽見並至少口頭表示不碰／知道這兩筆是指定給本人。"
    - "尚無實際搶奪銀兩事件。"
    - "尚無砸牙行事件。"

  ownership_axis:
    - "二十兩由白御行明示歸兩名女子本人"
    - "不得與牙行身契價款混淆"
```

---

# 17｜YAHANG23-E01｜四名牙行經手人與處子標示責任

```text
YAHANG_MEETING:
  participants: "四名牙行經手人／兩男兩女；十一名候選；白御行；張麗華；白三十二娘"

  classification:
    documented_virgin:
      count: 7
      meaning: "牙行文書明載處子"
    oral_only:
      count: 4
      meaning: "牙行口頭報處子，但未寫死於文書"

 牙行_general_position:
    - "文書敢保與口頭保之責任不同。"
    - "口保不等於書面保證。"
    - "對文書處子，牙行主張其依原戶來源、經手畫押、收人後出入帳及慣例查驗而敢落字。"
    - "牙行不接受『第一次未落紅＝必定非處子＝十倍欺詐』作為自動判定。"

  world_fact_boundary:
    - "本輪未進行身體驗證。"
    - "未建立『落紅』為處子真偽之可靠標準。"
    - "牙行是否違反官面規則須依具體戶籍、契、收錢／陪席等證據判斷；本 HOT 只記人物陳述與知情狀態，不自行擴寫世界法律條文。"
```

---

# 18｜FORWARD-CANDIDATES23-E01｜四名明確往前候選與牙行報價

```yaml
FOUR_FORWARD_CANDIDATES:
  candidate_19_qing:
    age: 19
    virgin_status: "文書保處子"
    self_position:
      - "想試清牌／清倌路線"
      - "不知道自己能否靠琵琶或談吐撐住高價清牌"
    yahang_price_taels: 380
    張麗華_advice:
      - "交李師師再看"
      - "核心不是她現在像不像清倌，而是能不能讓男人願意為『碰不到』持續花錢"
    status: "UNSOLD_CONTINUES_SELECTION"

  candidate_22_former_table_companion:
    age: 22
    virgin_status: "牙行僅口保"
    observed_skill:
      - "站位、笑、視線控制明顯熟練"
    disclosed_background:
      - "曾以家僕身分在大戶人家席間斟酒、陪坐、陪笑、記人"
      - "無妓籍／無以陪席女子身分另行官面登記之自述"
      - "有時客人要求坐下說話"
      - "本人自述曾被男客摸手、摟腰，但沒有行房"
      - "有時客人來前會被要求換衣、梳頭、不要掃興"
    yahang_price_taels: 260
    張麗華_advice:
      - "交蘇清再拆"
      - "先分辨其熟練是長期真本事、被迫經驗，還是今日表演包裝"
    status: "UNSOLD_CONTINUES_SELECTION"

  candidate_18_documented_high_price:
    age: 18
    virgin_status:
      yahang_document: "明載處子"
      self_statement: "本人當眾自述未曾與男人行房"
    traits:
      - "外貌突出"
      - "風月應答生，上午一度容易被早篩"
    yahang_price_taels: 600
    status: "UNSOLD_CONTINUES_SELECTION"
    notes: "詳見下一節"

  candidate_20_sewing:
    age: 20
    virgin_status: "文書保處子"
    skills:
      - "會針線"
      - "識字不多"
    self_position:
      - "家裡回不去"
      - "若一定要被賣，目前比較想留在今天至少讓她吃飽的觀止"
      - "不知道以後會不會後悔"
    yahang_price_taels: 220
    張麗華_advice:
      - "不急定清紅"
      - "先看針線、記性、手腳、耐性、怕不怕人、能不能學"
      - "一頓飯不能替她簽十年；但『目前比較想留觀止』本身可以是真話"
    status: "UNSOLD_CONTINUES_SELECTION"
```

---

# 19｜CANDIDATE-18-60023-E01｜六百兩十八歲候選：本人自述、白御行背書與五十兩分價要求

```yaml
CANDIDATE_18_600:
  yahang_asking_price_taels: 600
  transaction_state: "NO_SALE"

  player_initial_purchase_attempt:
    - "白御行一度表示願出六百兩立刻買。"
    - "並曾要求牙行派人在房外／現場見證初夜是否落紅，若無則十倍賠償。"
    - "牙行拒絕把『未落紅』當成書面處子保證之十倍違約標準。"

  consent_boundary_raised_by_candidate:
    - "她明確指出：剛才往前一步，只是願意繼續讓觀止挑，不等於今晚跟白御行走。"
    - "她問若白御行買到自己名下，住哪、做什麼、是否一定接客、今晚是否一定同房，都需另行說清。"
    - "她反對把自己放在床上讓多人等著看是否流血作為驗貨方式。"

  self_statement:
    public_in_room: true
    content:
      - "本人明確說：『是，我是處子。』"
      - "進一步自述：沒有跟男人行過房。"
      - "她說這是自己知道／自己說，不是因牙行驗過才成立。"
      - "她不知道初次行房是否一定會落紅。"

  white_yuxing_final_position:
    purchase: "撤回，不買"
    endorsement:
      - "白御行願向潘金蓮轉述並以自身信用背書：該女子今日當面自述未與男人行房，白御行相信其陳述。"
      - "此背書不是驗身結果。"
      - "此背書不解除牙行文書責任。"
      - "潘金蓮後續不必因白御行之意見反覆逼問同一件事，但最終採信與交易仍屬潘金蓮。"

  candidate_price_share_demand:
    requested_taels: 50
    rationale:
      - "她發現牙行以『處子』提高自身售價，故要求若成交，至少五十兩直接歸本人。"
      - "牙行當場先說不可能；後續尚未談成。"
    state: "OPEN_NEGOTIATION"

  white_yuxing_private_interest:
    - "白御行之後明示其實很想買她的初夜／出閣夜。"
    - "白御行推測若她被觀止養成後再上拍賣，自己可能要花至少數千兩，曾口頭舉『五千兩』為估算。"
    - "此為玩家興趣與估算，不是未來價格事實、不是預約、不是權利。"
```

---

# 20｜CANDIDATE-22-YAHANG23-E01｜二十二歲陪席經歷與牙行知情／揭露爭議

```yaml
CANDIDATE_22_DISCLOSURE:
  candidate:
    age: 22
    yahang_status: "只口保處子，未在文書寫死"
    self_statement:
      - "以前以家僕身分在大戶席面服務"
      - "斟酒、遞菜、陪坐、陪笑、記人"
      - "未以妓籍／陪席女子身分報備之自述"
      - "男客曾摸手、摟腰"
      - "本人自述未行房"

  yahang_knowledge:
    - "牙婆承認收人時曾聽她說過席間陪酒／陪坐及被男客觸碰等情形。"
    - "牙婆承認自己知道其前主人家『用她用得不乾淨』／至少存在風月嫌疑。"
    - "牙婆表示正因不敢替前主人家所有情況負責，所以只口保處子，不敢落書面保。"

  disclosure_problem:
    - "牙行對觀止最初只把她描述為『跟過大戶、懂規矩、懂男人』，未主動完整說明陪席與被男客觸碰等背景。"
    - "同一段經歷在賣價時被包裝成『懂男人／有席面經驗』，在責任上又被切回前主人的灰帳。"
    - "候選本人要求牙行之後向潘金蓮照實說，不得再只用『跟過大戶、懂規矩』帶過。"
    - "張麗華表示若牙行不說，她會說。"

  legal_axis:
    player_claim:
      - "白御行認為牙行做此行生意，對良家女陪席、戶籍／妓籍、官面責任與官非比候選本人更清楚。"
    yahang_response:
      - "牙婆承認懂相關規矩與風險。"
      - "牙婆主張單純家宴伺候與長期挑年輕女子陪男客取樂、收錢／送禮／留客等情形在官面風險上不同。"
    hard_state:
      - "是否已構成具體違法／官非，尚未經官府或正式查帳裁決。"
      - "可確認的是牙行對該候選過去存在風月嫌疑已有一定知情，且初始對觀止揭露不完整。"

  next_step:
    - "若潘金蓮對此人有興趣，應翻牙行底帳／來源／前主人資訊再決定。"
    - "目前未成交。"
```

---

# 21｜FINAL-RETURN23-E01｜九人回場、兩人退出與最後拒絕窗口

```yaml
RETURN_TO_SELECTION:
  definite_continue:
    count: 4
    action: "已下樓繼續參賽"

  undecided:
    count: 5
    action: "已下樓繼續參賽／繼續看"
    note: "未決狀態本身仍有效，不得因回場推定已答應"

  withdrawn:
    count: 2
    action: "退出本次遴選，不再參加後續選拔"

  white_yuxing_instruction_or_intent:
    - "白御行告知仍參賽者：最後以前若不想繼續，可向潘金蓮明說不想。"
    - "白御行先前已表示會建議潘金蓮在最終決定是否買人前再問一次『想好了沒有／想好的是什麼』。"

  authority_boundary:
    - "潘金蓮尚未在本輪雅間中親自確認把此流程固化成觀止永久制度。"
    - "因此目前應記為白御行明示的現場主張／擬議程序，待潘金蓮接手時執行或調整。"
```

---

# 22｜PUBLIC-STORY23-E01｜白三十二娘風月公開故事候選

```yaml
BAI_32_PUBLIC_PERSONA:
  status: "ROUTE_PERFORMANCE_PERSONA_PROPOSAL_NOT_BASELINE_TRUTH"

  concept:
    - "亡國大臣之女"
    - "一家三十二口，城破之日死三十一人；她是活下來的一個"
    - "戰亂中受敵軍暴力、失去處子身分，後經牙行轉賣，活到今日"
    - "不以復仇為唯一主軸；可用『恨啊，只是找不到人收』之方向"
    - "『城破那日，我家三十二口，死了三十一個。剩下那個，死得比較慢。』可作人物故事核心句"

  origin_of_name:
    - "『三十二娘』可與一家三十二口相聯，但不必把全部細節公開說死"

  張麗華_advice:
    - "不要只演哭泣受害者"
    - "悲劇細節不要全掀"
    - "日常人物要有識字、算帳、看契、懂禮、看人的能力"
    - "故事把人引進來，真本事把人留下來"
    - "與張麗華同為『亡國』題材但位置不同：張麗華由上往下，三十二娘由死人堆／底層往上；不得人格合併"

  usage_boundary:
    - "白御行未決定讓她掛牌"
    - "若日後她自己有意，可再談"
    - "不得把此表演故事倒灌為人物真實出生史"
```

---

# 23｜ACCOUNTING23｜本日新增可核對款項與未成交報價

```yaml
ACCOUNTING_LEDGER:
  candidate_meal_support:
    initial_portions: 300
    listed_unit_price: "10文／份"
    replenishment: "每家約每小時20份，按需求"
    final_total_cost: "UNKNOWN_PENDING_MERCHANT_INVOICE"
    payer: "定陶商會相關公帳安排"

  辭歲_appearance_fee:
    amount_taels: 5
    state: "PAID"

  小翠_appearance_fee:
    amount_taels: 5
    state: "PAID"

  withdrawal_gifts:
    recipients: 2
    amount_each_taels: 10
    total_taels: 20
    state: "PAID"

  candidate_asking_prices_not_transactions:
    19_qing: 380
    22_oral_virgin: 260
    18_documented_high_price: 600
    20_sewing: 220
    state: "ALL_UNSOLD"

  candidate_18_requested_personal_share:
    requested_taels: 50
    state: "NOT_AGREED"

  white_house:
    proposed_lump_sum_taels: 8000
    state: "CONDITIONAL_NOT_YET_ACTIVATED"
```

---

# 24｜人物與知情邊界

```yaml
KNOWLEDGE_AND_SOVEREIGNTY:
  eleven_candidates:
    - "知道自己上樓參與一場額外談話／分流"
    - "知道可表達退出、繼續或未決"
    - "不因此自動知道定陶 48／神七／御三家秘密架構"

  yahang:
    - "知道本輪十一人被抽出問話與其中四人報價"
    - "不知道任何未明示的白御行秘密商業模型"

  白三十二娘:
    - "今日為白御行跑腿／傳話"
    - "不得推測白御行內心滿意度"
    - "不得主動探查秘密選人真正商業用途"

  辭歲:
    - "原始人物動機待資料校正"
    - "不得再使用『純粹自主選擇性工作』的扁平化版本"

  小翠:
    - "過去已有性經驗不等於現在永久同意"
    - "其恐懼／拒絕不得被洗成『還沒想通』"
```

---

# 25｜LIHUO 回歸／導演污染記錄（不具世界事實權）

```yaml
CORRUPTION_AND_REGRESSION_NOTES:
  issue_1_pan_reputation_scene:
    symptom:
      - "曾一度把潘金蓮寫成被白御行說服後用現代式慈善／品牌聲譽話術承接供餐。"
    correction:
      - "有效版本為潘金蓮以自身商人、風月場主人語氣接住：讓人吃、讓人拿、不空肚子走；不講療癒品牌課。"
      - "口碑效果未決。"

  issue_2_cisui_motivation:
    symptom:
      - "曾一度把辭歲寫成『因為我想當妓女，所以自己昂首走進青樓』。"
    root_cause:
      - "人物的具體逃婚因果被現代自主職業選擇框架取代。"
    correction:
      - "回第六卷開頭：逃離權貴填房命運，拒絕被安排；進觀止是選擇另一個危險制度以賭取未來自選男人／自定價資格。"
    status:
      - "前述污染台詞不固化"
      - "人物資料待另行正式修改"

  authority_rule:
    - "本節只有審計／回歸用途，不得把污染版本重新演進世界。"
```

---

# 26｜未決事項

```yaml
OPEN_ITEMS:
  pan_purchase_decisions:
    - "四名明確前進候選是否被潘金蓮購買／留下，未決"
    - "五名未決候選最終是否選擇繼續，未決"
    - "兩名退出候選回牙行後遭遇何事，未知"

  candidate_18_600:
    - "牙行六百兩開價是否被潘金蓮接受／砍價，未決"
    - "候選要求五十兩歸本人是否成交，未決"
    - "白御行未購買，也未取得其初夜／出閣權"
    - "未來是否上觀止出閣拍賣，未決"
    - "未來價格完全未定；『至少五千兩』只屬白御行口頭估算"

  candidate_22:
    - "牙行底帳、前主人實際安排、是否存在收錢／私娼等官面問題，待查"
    - "潘金蓮尚未決定是否繼續留她"
    - "蘇清後續複問尚未發生"

  candidate_19:
    - "李師師後續是否認為她能走清牌，未決"

  candidate_20:
    - "能力路線與是否適合清／紅／後勤，未決"

  white_house:
    - "空間宣告／宅邸穩定性測試尚未進行"
    - "八千兩十年租金尚未正式啟動"

  fang_cloth:
    - "方掌櫃尚未正式投帖常煒"
    - "樣布、價目、供貨能力尚未完成審核"
    - "商會尚未下單"

  civil_case:
    - "蘇清 vs 潘金蓮五萬兩索賠未判"

  cisui_data:
    - "需在日後 SETTING／文件任務中改寫辭歲人物資料，使動機與第六卷開頭一致"
```

---

# 27｜直接接關摘要

```yaml
DIRECT_RESUME:
  story_time: "理火三年槐月二十三日下午"
  location: "風滿樓二樓側雅間"

  immediate_state:
    - "十一名成年處子／口保處子候選之額外談話已結束。"
    - "兩人退出並各得白御行十兩補貼。"
    - "四人明確繼續；五人未決但回場繼續看。"
    - "十八歲六百兩候選未成交；本人處子自述由白御行願向潘金蓮背書可信。"
    - "二十二歲口保候選之過去陪席／牙行知情不完整揭露已暴露，待潘金蓮／蘇清後續處理。"
    - "張麗華已給另外三名明確前進候選各自的後續觀察方向。"
    - "白御行與張麗華仍在二樓，白三十二娘近身跑腿。"

  do_not_auto_resolve:
    - "不得替潘金蓮決定購買任何候選"
    - "不得把任何候選之處子陳述改寫成驗身結果"
    - "不得替候選答應成人行為"
    - "不得把『回場參賽』寫成永久入妓門"
    - "不得把白御行對六百兩候選的興趣寫成既得初夜權"
    - "不得把辭歲污染版本重新引用為人物真實自述"
    - "不得自動測試／完成白宅生成與八千兩租約"
```

---

# 28｜HOT V3.1 結論

> **最新直接接關：理火三年槐月二十三日下午，風滿樓二樓側雅間。**
>
> **十一名成年處子／口保處子候選已完成三向分流：2 退出、4 明確繼續、5 未決但回場。**
>
> **退出二人各得白御行十兩個人補貼；牙行被明示不得奪取。**
>
> **十八歲六百兩候選未成交；本人自述未與男人行房，白御行願向潘金蓮背書其自述可信，但不構成驗身、不解除牙行責任。**
>
> **二十二歲口保候選曾以家僕身分陪席；牙行已承認收人時知道相關風月嫌疑，對觀止初始揭露不足，後續責任待潘金蓮／底帳查核。**
>
> **辭歲人物原始動機已回第六卷校正：她不是單純『想當妓女』，而是逃離被安排成權貴填房的命運，選擇進觀止去賭一條未來能自選男人／自定價的危險道路。此前純自主性工作版本標記為導演污染，不得固化。**
>
> **辭歲人物資料需在後續 SETTING／文件修改任務正式改寫；本 HOT 只立校正旗標，不直接改人物卡池。**
>
> **本檔只更新 HOT，不更新 MASTER。**

<!-- PROMOTED_HOT_SOURCE_END: 觀止青樓_白御行線_HOT_SAVE_V3.1_槐月二十三日下午_風滿樓第二日遴選_十一名處子候選分流_牙行責任_辭歲資料待修版.md -->

---

# APPENDIX H｜固化來源全文：觀止青樓_白御行線_HOT_SAVE_V3.2_槐月二十五日白日_小翠同床純睡_三月集訓走秀換約_六百兩候選_白宅需求擴張與師師設計版.md

> **法位：E84–E92 細節追溯來源。** 此 HOT 內的 CURRENT_SCENE／HOLD 只代表當時快照；不得覆寫本 MASTER 截止或 V3.5–V3.7 疊加層。若原 HOT 內某個標成 YAML 的區塊本身語法不合法，本 MASTER 只把該 fence 改標為 text 隔離，內容原文不改，避免來源語法缺陷破壞 MASTER 解析。

<!-- PROMOTED_HOT_SOURCE_BEGIN: 觀止青樓_白御行線_HOT_SAVE_V3.2_槐月二十五日白日_小翠同床純睡_三月集訓走秀換約_六百兩候選_白宅需求擴張與師師設計版.md -->
# 觀止青樓｜白御行線 HOT SAVE V3.2
## 理火三年槐月二十五日白日｜小翠同床純睡 × 三月集訓／走秀驗收／集體換約 × 六百兩候選 × 白宅需求擴張 × 師師第一輪設計版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V3_2_HUAI25_DAY_XIAOCUI_SLEEP_TRAINING_THREE_MONTHS_CONTRACT_SWITCH_WHITE_HOUSE_DESIGN"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V3.2"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V11.0-R2"
  character_source: "觀止人物卡池_LCAPG_V2.2_辭歲入觀止動機校正_青禾六條增補_正式版"
  story_date: "理火三年槐月二十五日"
  time_of_day: "白日；大型遴選已退場，人才制度與白宅第一輪需求正在收尾"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AFTER_WHITE_HOUSE_FIRST_ROUND_DESIGN_TASK_ASSIGNED_TO_LI_SHISHI"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V3.1_槐月二十三日下午_風滿樓第二日遴選_十一名處子候選分流_牙行責任_辭歲資料待修版.md"
  previous_hot_sha256: "ae9a41dc2ee1efce21c8f3c758cac10e04bd3fb7be16f28036810705b3a6f72f"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"
  save_scope:
    - "HOT V3.1 後至槐月二十五日白日之直接玩家線事件"
    - "槐月二十三日大型遴選收尾、風滿樓大型狀態關閉與白家四女權限"
    - "張麗華新侍女、二百兩贈禮款與七十兩零花"
    - "張麗華賭約按摩完成及其後雙方自主成人關係"
    - "李師師主母級內部用人權、紅伶正式跟席／樂曲訓練與兩名侍女候選"
    - "槐月二十四日晚至二十五晨小翠收留白御行同床純睡事件"
    - "李師師與白御行第二晚白嫖床位賭約"
    - "三個月新人集訓、走秀驗收、集體換約與商會／觀止分帳制度"
    - "六百兩十八歲候選之收購條件、五十兩個人款、一成五未來出閣分成與訓練規則"
    - "時空道人重新現身、命運籤與觀止常設空間需求治理"
    - "白宅第一輪空間需求與李師師設計任務"
```

---

# 0｜提交法位、來源與反污染

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V3.1_槐月二十三日下午_風滿樓第二日遴選_十一名處子候選分流_牙行責任_辭歲資料待修版.md"
    role: "本檔直接前置 HOT；V3.1 及以前有效硬狀態全部繼承"

  master_archive:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"
    role: "長期因果來源；本檔不修改 MASTER"

  current_route_conversation_commit:
    role: "HOT V3.1 後至本次 HOT SAVE 命令前之直接劇情、玩家明示自身言行／意圖、NPC 可觀察回應及明確討論後制度決定"

ANTI_CORRUPTION:
  cisui:
    status: "CHARACTER_POOL_V2.2_CORRECTION_COMPLETED"
    note:
      - "HOT V3.1 的『辭歲資料待修』已由人物卡池 V2.2 完成修正；不得再視為待辦。"
      - "辭歲進觀止直接動機為逃離家族安排之填房式婚配／高門附屬命運，並在受限選項中選擇進觀止向上爬；不得還原為『純粹自由選擇當妓女』。"

  fuxiang_hot_v1_3:
    status: "ILLEGAL_CORRUPTED_SAVE_AUDIT_ONLY"
    effect:
      - "浮香 V1.3 整段故事砍除，不得拿其中接吻、白玉池私人親近、相吸判定或任何成人前史作為現行關係依據。"
      - "未來若重開浮香線，只能使用仍合法之人物基線與有效事件重新生長。"

  assistant_misfire_32_message:
    status: "AI_PROXY_ERROR_NOT_WORLD_FACT"
    false_scene:
      - "曾誤演白三十二娘受命向李師師傳『白御行今晚不回、不留門』。"
    correction:
      - "玩家立即明示校正：三十二娘真正受命內容是『請李師師先畫白宅第一輪設計／需求圖』。"
      - "故誤傳場景全部撤銷，不得寫入世界事實、傳聞或人物知情。"

COMMIT_NOTE:
  - "本檔取代 HOT V3.1，成為白御行線最新直接接關切片；V3.1 保留為前置歷史來源。"
  - "本次只更新 HOT；不更新 MASTER，不直接修改主程序、人物卡池或世界 Runtime。"
  - "所有成人行為、同床、擁抱、接客、出閣拍賣、職業安排與契約必須分軸保存；持契／奴籍／工作安排不等於永久或 blanket 性同意。"
  - "『商會約』『觀止約』『身籍』『營運收入』『姑娘個人分成』『出閣拍賣』為不同法位，不得混成單一所有權描述。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年槐月二十五日"
  time: "白日"
  primary_location: "觀止內；白御行已完成一次真正出門再回門之時空道人進門事件"
  exact_player_room: "NOT_FIXED_BY_LAST_UTTERANCE"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  latest_direct_action:
    - "白御行命白三十二娘前往李師師處，傳達『白宅第一輪生活／功能配置圖由白夫人先畫』。"
    - "三十二娘已將需求傳達。"
    - "李師師已取紙開始分區構思；第一版尚未完成、尚未會審。"

  immediate_parallel_state:
    - "人才大型遴選已退出主舞台，後續由潘金蓮等人按制度收尾並報告。"
    - "六百兩十八歲候選之正式入場／結算手續仍待辦完；今日尚不得自行進大堂撈客，只能在旁觀察。"
    - "今晚白御行與李師師的『第二張床白嫖賭局』仍有效；白御行尚未在劇情中選定今晚目標。"
```

---

# 2｜V3.1 繼承後仍活躍核心

```yaml
INHERITED_ACTIVE_CORE:
  su_qing_vs_pan:
    criminal_axis: "潘金蓮已無坐牢風險"
    civil_axis: "蘇清方提出五萬兩賠償要求；仍是索賠／談判，不是判決或確認應付"
    handling: "律師／民事帳務線幕後推進"

  white_jade_pool:
    status: "PREPARING_RENOVATION_AND_WISH_COIN_SYSTEM"
    pacing: "幕後小幅推進"

  womens_business:
    model: "48／神七／御三家秘密中央事業架構"
    status: "SECRET_ACTIVE_PROJECT"
    boundary: "本輪新人可能成為未來人才來源，但不得因此自動知情"

  fashion_business:
    status: "PLANNING_WITH_THREE_MONTH_CHECKPOINT_NOW_DEFINED"
    new_anchor: "三個月後大型走秀被定義為本批新人集訓驗收／市場亮相／集體換約日"

  cao_zhou_fake_seal:
    status: "OFFSCREEN_ACTIVE"

  white_house:
    rent_framework: "八千兩／十年之條件式租用仍有效；須先證明常設空間穩定存在"
```

---

# 3｜FENGMANLOU23-E02｜大型遴選關閉與收尾法位

```yaml
FENGMANLOU_CLOSURE:
  effective_after: "槐月二十三日夜大型場結束"
  state:
    - "自槐月二十四日起不再維持風滿樓大型擴張遴選狀態。"
    - "恢復觀止日常空間；剩餘複選採小規模分流，不再用巨大場地。"
    - "白御行不再負擔二十四日起的大型場維持／臨時擴張成本。"

  physical_note:
    - "風滿樓在本線是觀止大型異常主場狀態，不是另一棟外租實體建築。"

  selection_governance:
    - "白御行明示除六百兩候選外，其他人才最終結果以潘金蓮等人收尾報告為主，不再逐個親自面試。"
    - "潘金蓮保留真正掌櫃選人權；師師、蘇清、疏影、白希等按各自專業提供判斷。"
```

---

# 4｜FOUR-WOMEN23-25｜白家四女、內部權限與三十二娘功能

```yaml
WHITE_FOUR:
  names:
    - "白三十二娘"
    - "白明礬"
    - "白紅伶"
    - "白希"
  contract_holder: "白御行"
  joke_title: "四大金剛（非正式職稱）"

  authority_matrix:
    李師師:
      internal_title: "白夫人"
      level: "白家如夫人／主母級"
      player_statement:
        - "夫人說的就是我說的"
      effect:
        - "對四女有直接日常用人／調度權，不需每件小事向白御行再請示。"
        - "不得覆蓋白御行已明確交代之相反任務。"
        - "此為白家內部權限，不等於所有權或 blanket 成人同意。"

    張麗華:
      internal_title: "麗華夫人"
      level: "重要情人／受尊重之夫人位，但非白夫人同級全面指揮權"
      effect:
        - "四女可直接替她做合理小事，不必每次報白御行。"
        - "重大安排、銀錢、去留或與白御行既有命令衝突時，不得只憑麗華一句話辦理。"

  白紅伶:
    current_role:
      - "已確認常態跟李師師學習席面、樂曲、手勢、拍板、換酒換香與表演節奏。"
      - "李師師需要紅伶設席時可直接叫人，不視為臨時借用。"
    training_boundary:
      - "紅伶仍是白家人，不改成李師師私產。"

  白三十二娘:
    demonstrated_capabilities:
      - "跑腿／傳話"
      - "小額帳務"
      - "議價時隱藏買方熱度"
      - "區分白御行私人支出、白家備用銀與其他帳"
    personal_petty_cash:
      amount_taels: 100
      purpose:
        - "白御行私人備用銀／小額跑腿採買"
        - "原第一用途：結槐月二十三日六家候選供餐帳"
      balance: "UNKNOWN"
      settlement_status: "未在本段得到明示完成確認；不得自動寫成已結清"
      replenish_rule: "不足時提醒白御行補充"
    position_boundary:
      - "已顯示實用內管／帳務潛力，但未正式固化為總管、管家或永久財務職稱。"
```

---

# 5｜LIHUA23-24｜麗華新侍女、贈禮款與夜間關係

```yaml
LIHUA_NEW_ATTENDANT:
  status: "ACQUIRED_FOR_ZHANG_LIHUA"
  adult_age: 23
  name: "UNKNOWN_NOT_HARD_RECORDED"
  background:
    - "曾在酒坊東家宅內做事約四年；原主人家敗落後轉入牙行。"
    - "會辨酒罈標記、簡單進出帳，知道部分酒務保存常識。"
    - "張麗華因其實際酒務眼力與手腳，而非單純美貌選中。"
  price:
    asking_initial_taels: 180
    negotiated_taels: 130
  funding:
    white_yuxing_gift_total_taels: 200
    purchase_taels: 130
    remainder_taels: 70
    remainder_status: "白御行明示作為張麗華零花，不回帳"
    nature: "白御行私人贈禮款"
  ownership_or_use:
    direct_person: "張麗華"
    not_fifth_white_woman: true
  future_upkeep:
    payer: "張麗華"
    includes:
      - "食衣"
      - "月錢／賞錢"
      - "醫療"
      - "日常維持"
  temporary_lodging:
    - "白御行命三十二娘先替她安排乾淨衣服與臨時床位，暫與白家四女一帶擠住；待白宅成形後再改善。"
    - "張麗華本人後續負責長期使用與安排。"

LIHUA_MASSAGE_AND_SEX:
  date: "槐月二十三日夜"
  massage:
    trigger: "晨間門票賭約輸掉"
    content: "全身按摩由頭到腳"
    status: "COMPLETED"
    note: "白御行曾要求輕一點；張麗華確實收力完成賭帳。"
  adult_relation_after_massage:
    status: "OCCURRED"
    consent: "雙方當晚自主慾望與同意"
    intercourse: true
    note:
      - "成人關係不是按摩賭約附帶義務，也不是按摩自動升級。"
      - "之後兩人同眠。"
```

---

# 6｜SHISHI24-25｜白夫人主母級、兩名候選、五百兩與床位規劃

```yaml
LI_SHISHI_HOUSEHOLD:
  internal_position:
    title: "白夫人／白家如夫人"
    level: "主母級"
    effect:
      - "白御行已向紅伶明示此權限，不再只是玩笑稱呼。"
      - "師師可直接調度白家四女之一般工作。"

  two_attendant_candidates:
    count: 2
    status: "TRIAL_NOT_FINALIZED"
    characteristics:
      near_room_candidate:
        strengths:
          - "守分寸"
          - "知道不是自己的信件／物件不亂碰"
        test_focus: "守嘴、近房日常與私人空間邊界"
      runner_candidate:
        strengths:
          - "識字較好"
          - "跑腿回報只帶必要答案，不亂添閒話"
        test_focus: "遇有身分者時是否仍守師師規矩"
    final_purchase: "NOT_CONFIRMED"

  white_yuxing_funding:
    amount_taels: 500
    purpose:
      - "師師自行處理兩名候選若最後留下之牙行／契錢／添衣等初始支出"
      - "不足再向白御行說"
    note: "交付五百兩不等於兩名候選已成交。"

  temporary_bedding_plan:
    status: "CONDITIONAL_ON_FINAL_TWO_CANDIDATES"
    principles:
      - "師師自己的內床仍是私人床，不因近房身份自動取得同床資格。"
      - "紅伶因常跟師師學席面，宜住得較近。"
      - "六人若都成立，需把三十二、白希、明礬、紅伶及兩候選重新分房；方案可由師師依最終去留調整。"

  pregnancy_axis:
    query_date: "槐月二十五日白日"
    menstrual_statement: "李師師表示本月月事尚未來"
    pregnancy_state: "UNKNOWN"
    promise:
      - "若日後由李師師本人先確認懷孕，她答應第一個告訴白御行。"
      - "不因月事未至而預先判定懷孕。"
```

---

# 7｜XIAOCUI24-25-E01｜小翠收留白御行：同床純睡與自主接觸

```yaml
XIAOCUI_OVERNIGHT:
  date_range: "槐月二十四日晚 → 槐月二十五日清晨"
  location: "小翠房內／小翠自己的床"
  trigger:
    - "白御行當晚無固定床位，晚間敲小翠房門，先以喝茶進房。"
    - "兩人先談及小翠日前被臨時叫作講師、她對大多風月場女子之平凡位置、怕男人／怕失去停止權與自主感。"

  entry_and_sleep_consent:
    - "小翠明示允許白御行留宿一晚，但最初限定『只是睡』。"
    - "白御行同意：有光時要進一步接觸先問；無光時不主動移動／不自行升級。"
    - "小翠可於半夜改變主意並叫白御行離床；若叫不醒，可找人協助搬走。"
    - "白御行同意此撤回機制。"

  initial_rules:
    player_position: "床外側"
    clothing:
      - "外衣後來在小翠明示允許下由白御行自行脫下。"
      - "裡衣保留；沒有全裸。"
    separator: "初始以長枕隔在中間，後由小翠自己移開一部分／踢至床尾。"
    no_sex_commitment: true

  physical_contact_sequence:
    - "小翠主動提出／同意抱白御行。"
    - "小翠在黑暗中以手指在白御行背上畫圈、摸臉／手指等，以自己節奏探索男性身體。"
    - "小翠把白御行的手引到自己腰背一帶、之後再移到她覺得舒服的位置。"
    - "白御行後來經詢問得到小翠同意，轉身正面抱她。"
    - "小翠明示手先留在她指定位置，若要換地方她自己帶。"
    - "小翠沒有要求性交，也明示暫時不想更進一步。"

  sexual_activity:
    intercourse: false
    oral_sex: false
    genital_contact: "NOT_ESTABLISHED"
    manual_sex: false
    note: "本夜不能被記為『白御行睡了小翠＝性交』；成立的是同床、互抱與小翠自主觸碰探索。"

  morning:
    - "小翠先醒，確認白御行手仍停在她昨夜安排的位置、衣著未被偷偷改變。"
    - "她沒有半夜叫人搬走白御行。"
    - "她明示昨晚『真的好像沒什麼』，但拒絕被說成『已治好』。"
    - "她認知到：至少昨夜讓人進房、同床、移枕、主動抱人，都是她自己做主。"
    - "她最後將『下一步走不走，老娘自己決定』視為自己的當下位置。"

  interpretation_boundary:
    - "此夜可以成為小翠新增的安全／自主男性相處經驗，但不得升格成『白御行治癒小翠』。"
    - "小翠仍可能害怕男人、怕痛或拒絕未來性行為。"
    - "一次同床成功不等於永久接受白御行、永久接客或永久解除恐懼。"
```

---

# 8｜RUMOR25-E01｜小翠房晨間目擊、師師推測與保密

```yaml
XIAOCUI_RUMOR_AXIS:
  actual_facts:
    - "白御行清晨從小翠房附近西廊方向離開。"
    - "白御行與小翠沒有性交。"

  red_hongniang_observation:
    - "紅娘在廊上看見白御行清晨從西廊方向出現。"
    - "之後注意到小翠尚未起身。"
    - "紅娘開始懷疑／推理，但沒有直接看見白御行從小翠房門走出，也沒有房內事實來源。"

  li_shishi_inference:
    - "李師師依西廊、小翠晚起、白御行言詞與其保密態度，推測昨夜可能在小翠房。"
    - "白御行拒絕透露名字，強調有保密道德。"
    - "白御行對師師只說過『蓋棉被純聊天』、『整晚沒動手／衣服沒脫完』等帶玩笑的自我陳述；未向她正式確認小翠。"
    - "師師的『大概是小翠』『可能是她主動做了些事』都屬推測，不是知情。"

  xiaocui_and_bai_private_line:
    - "兩人曾討論若被問，可只說『昨晚小翠收留我』。"
    - "小翠不希望白御行公開說『我睡了小翠』造成性交誤解。"
    - "白御行笑稱可說『我被小翠睡了』，屬兩人玩笑，未成公共傳聞硬事實。"
```

---

# 9｜SHISHI-BED-WAGER25-E01｜第二晚白嫖床位賭局

```yaml
SECOND_BED_WAGER:
  date_target: "槐月二十五日夜"
  parties:
    - "白御行"
    - "李師師"
  status: "ACTIVE_NOT_YET_RESOLVED"

  white_yuxing_declared_goal:
    - "今晚不去李瓶兒處，因白御行認為瓶兒必定會收留，不能算本事。"
    - "要在外面不付宿費／不靠主母安排，再找到另一張姑娘的床過夜。"
    - "白御行並直接對師師說：今晚死都不會來找她。"

  wager_rules_as_spoken:
    forbidden:
      - "不能花銀子買宿"
      - "不能用李瓶兒安排住宿"
      - "不能用白家主母／四女內部權限壓人收留"
      - "不能叫三十二娘替他安排床"
    qualification:
      - "對方必須自願讓白御行留下"
      - "睡榻／地板只算半成；睡到對方的床才算完整贏"
      - "是否發生性行為不列為勝負條件"

  if_white_yuxing_wins:
    - "李師師當著紅伶等人承認白御行確實有本事，不靠銀子／瓶兒／主母安排也能找到姑娘自願給床。"
    - "白御行可指定李師師替他做一件『李師師本人可以自願答應』的事；不得藉賭約強迫她做不願意的事或替第三人作主。"

  if_white_yuxing_loses:
    - "不得半夜找李瓶兒救場、不得臨時回頭找張麗華。"
    - "若最後回師師處，須當著紅伶面承認：『主母，我在外面白嫖床位失敗，求收留。』"

  planning_only_not_world_event:
    - "白御行曾在 HOLD／討論模式與導演分析浮香、醉花、十三娘作為今晚可能目標。"
    - "尚未在劇情中選定任何一人，三人亦不知道自己被列入候選。"
```

---

# 10｜CANDIDATE-18-60025-E02｜六百兩十八歲候選：收購結構、訓練與個人分成

```yaml
CANDIDATE_18_600:
  age: 18
  adult: true
  virgin_status:
    self_statement: "本人自述未與男人行房"
    yahhang_document: "處子保證寫入牙行文書"
    physical_bleeding_guarantee: false
    consent_boundary: "處子陳述不等於答應今晚或任何指定男人行房"

  observed_traits:
    - "外貌出眾"
    - "第二日大型遴選早期回答偏差／不會風月應對"
    - "大場縮小後顯示學得快：倒酒、站姿、服裝適配等能快速吸收"
    - "敢問自己的五十兩、未來分成與制度利益，不完全被動"

  acquisition_price:
    gross_taels: 600
    structure:
      yahhang_taels: 550
      personal_direct_taels: 50
    personal_50_terms:
      - "直接給她本人"
      - "不從月錢扣"
      - "不算借款"
    payment_and_intake_status: "TERMS_FIXED_IN_PRINCIPLE; FINAL_INTAKE_PAPERWORK_NOT_YET_HARD_CONFIRMED"

  white_yuxing_future_share_offer:
    trigger: "若日後她自願／依法進入正式出閣拍賣"
    personal_share: "拍賣成交額一成五（15%）"
    guanzhi_typical_platform_fee_context: "此類良家出閣代辦常規平台費一成（10%）"
    note:
      - "15% 是白御行當面對她提出的個人未來分成，不得自動泛化成所有新人共同分成。"
      - "此分成不代表她現在已同意三個月後一定出閣或行房。"

  current_day_work_rule:
    - "正式報備／入場手續辦妥前，今天不能自行進大堂撈客。"
    - "可在側邊旁觀，學客人、姑娘、酒席、留客方式與場內節奏。"

  conversation_state:
    - "白御行強調個人市場價值不是只靠外貌、年齡、處子狀態，還依靠客群、席面、衣裝、談吐、團隊包裝與平台體系。"
    - "白御行警告她若把一切成績全歸功於自己、忽略整套體系，可能在離開平台後迅速失去價值。"
    - "她反問：若全是體系功勞，為何偏偏花六百兩買她；潘金蓮補充體系能放大好料，但不是換誰都一樣。"
    - "不得把白御行『女孩不值錢／失去體系只是最普通妓女』等話升格成世界客觀真理；它是玩家對商業體系的觀點與對她的訓話。"
```

---

# 11｜TRAINING-THREE-MONTHS25-E01｜本批新人三個月觀止訓練制

```yaml
THREE_MONTH_TRAINING_SYSTEM:
  status: "GM_CONFIRMED_ROUTE_POLICY"
  target_group: "本輪最終進入新人培訓名冊、完成觀止接收且持續留在體系中的成年女性"

  phase_1:
    duration: "三個月"
    contract: "觀止約"
    location: "觀止"
    role_of_guanzhi: "訓練場／實際市場／營運平台／觀察場"

  non_virgin_trainees:
    - "可依個人能力、意願、既有經驗與當下契約安排進行實際訓練。"
    - "可走清、走紅、席面、表演、技能等不同方向。"
    - "可在有效同意與觀止規則下安排部分接客；不得因非處子身分自動推定願意接任何客。"
    - "三個月內可以用真實營業結果觀察是否長出客群、席面能力或其他價值。"

  virgin_trainees:
    - "前三個月不辦正式出閣／初夜拍賣。"
    - "仍跟全體新人一起訓練。"
    - "可在大堂累積看人、留客、茶酒、表演、熟客與市場經驗；具體能做什麼依其當下同意、技能與觀止安排。"
    - "前三個月目標之一是讓市場先認得她們、建立客群與期待，而非急著把第一次立即變現。"

  training_philosophy:
    - "仍保有自己想法、尚未『認命』的姑娘不應被預先洗成只會服從。"
    - "觀止可要求遵守契與工作，但不把『放棄自己的未來想法』當作合格條件。"
    - "表現好壞以實際學習、營業、客群、技能、適配與紀律觀察，不用單一好感或漂亮程度。"
```

---

# 12｜THREE-MONTH-REVENUE25-E01｜前三個月收入與商會不抽成

```yaml
PHASE_1_ACCOUNTING:
  during_three_months:
    operating_revenue_owner: "觀止"
    merchant_association_take: "不抽本階段觀止營業收入"
    reason:
      - "此時新人跑觀止約"
      - "使用觀止客流、場地、席面與訓練體系"
  girls_personal_compensation:
    - "姑娘依觀止約本來應得之月錢、賞錢、分成、個人所得照約處理。"
    - "『營業收入算觀止』不等於姑娘零收入。"

  accounting_boundary:
    - "前三個月與集體換約後須一刀切帳。"
    - "跨換約日之訂席／預付款／履約收入應另訂歸屬規則，避免觀止與商會事後爭帳；目前細則未定。"
```

---

# 13｜RUNWAY-CONTRACT-SWITCH25-E01｜三個月走秀＝集訓驗收＋集體換約日

```yaml
RUNWAY_CHECKPOINT:
  timing: "三個月後；精確日期尚未換算固化"
  functions:
    - "本批新人第一期正式集訓驗收"
    - "大型市場亮相"
    - "觀止約結束／商會約開始之集體換約日"

  collective_contract_switch:
    rule:
      - "不分處子／非處子，只要走到走秀當日仍在本批有效訓練名冊並通過體系收尾者，當天集體換約。"
      - "走秀前為觀止約；走秀驗收後轉商會約。"
    exceptions:
      - "三個月中途已被退、轉手、離開體系或另案處理者，不等到走秀換約。"

  after_switch:
    controller: "商會"
    deployment_rights:
      - "是否繼續留觀止"
      - "是否派往定陶或其他場"
      - "是否做女裝／走秀／席面"
      - "是否往清／紅或其他職能配置"
      - "是否進一步培養／轉手／另作安排"
    note: "商會自換約日起成為後續配置主體；不得回溯搶走前三個月觀止營運收入。"
```

---

# 14｜VIRGIN-AUCTION25-E01｜處子出閣拍賣延後與商會委託觀止

```yaml
VIRGIN_FIRST_NIGHT_AUCTION:
  phase_1_three_months:
    status: "NO_FORMAL_AUCTION"
    purpose:
      - "繼續訓練"
      - "大堂累積經驗"
      - "建立熟客與市場期待"

  after_runway_contract_switch:
    owner_or_controller: "商會（依商會約與身籍／配置權處理）"
    auction_operator: "觀止受商會委託代辦"
    guanzhi_value:
      - "提供場地／品牌"
      - "帶入觀止既有人脈、富商、熟客與風月市場"
      - "承辦正式出閣拍賣"
    note:
      - "何人何時出閣、是否繼續養市場、實際拍賣條件仍須另案。"
      - "不得因三個月制度存在即推定每名處子必在走秀後立刻拍賣。"
      - "正式出閣／性交仍須分開記錄當時實際同意與事件。"
```

---

# 15｜PUBLIC-TRAINING-DISCLOSURE25-E01｜對新人公開版本與淘汰後果

```yaml
PUBLIC_INFO_TO_TRAINEES:
  allowed_to_tell_all:
    - "接下來三個月在觀止受訓／工作"
    - "三個月後有正式走秀／驗收"
    - "進觀止不等於永久能留在觀止"
    - "三個月表現不好、長期賠錢或不適配者可能被退、轉手、賣去其他場子，包含更低級妓院的可能"
    - "漂亮、會唱或肯接客都不是唯一保證；能否在體系裡形成實際價值才重要"

  internal_not_to_leak_as_current_contract:
    - "三個月走秀當日集體換商會約之完整後台制度"
    - "商會對換約後人員的完整配置／資產邏輯"
    - "觀止與商會的完整後台分帳"
    - "商會委託觀止出閣拍賣之全套內部運作"

PAN_ACCIDENTAL_LEAK:
  event:
    - "潘金蓮曾在六百兩候選仍在場時，順口談到三個月換約／商會／後續拍賣等內部規劃。"
  repair:
    - "白御行指出洩密後，潘金蓮立即回去校正。"
    - "她向六百兩候選明示：剛才後段是東家內部制度草案，不是她現在可當契約條款引用的正式承諾。"
    - "目前該候選應掌握的正式版本壓回：三個月觀止訓練＋走秀驗收；到時真正要簽什麼會拿正式契給她看。"
    - "白御行本人已當面給她的未來 15% 出閣分成承諾不因此撤回。"
```

---

# 16｜SPACE-GOVERNANCE25-E01｜時空道人回歸與『需求先成立，空間再顯影』

```yaml
TIME_SPACE_DAOIST_RETURN:
  trigger:
    - "白御行明確認為自己久未真正離開觀止，時空道人缺乏每日進門給籤的合理入口。"
    - "白御行遂真正離開觀止、在京師外頭走一段後重新從正門返回。"
  result:
    - "時空道人於門邊重新出現並強制交命運籤。"

  fortune_slip:
    line_1: "一門踏出千燈遠"
    line_2: "回首春風不認人"
    interpretation: "NONE_BY_DAOIST"
    boundary:
      - "時空道人不解籤。"
      - "命運籤只能作當晚世界較易收束之傾向／故事壓力，不是事件保證。"

SPACE_GOVERNANCE:
  status: "ROUTE_RULE_EXPLAINED_TO_PAN"
  core_rule: "需求先成立，空間再顯影"
  temporary_need:
    type: "事件空間"
    behavior: "事件結束可坍縮／收回"
  recurring_long_term_need:
    type: "常設空間候選"
    behavior: "須先有穩定反覆用途，再經穩定性證明後保留"

  anti_overexpansion:
    - "缺六間不能預造六十間。"
    - "不得因發現觀止可折疊空間就預先開大量閒置院落、湖池或出租街。"
    - "未來若故事長期需求逐步累積，最終自然長成大觀園級規模可以成立；不是一次宣告完整生成。"

  first_persistent_space_test:
    target: "白宅"
    rule:
      - "先證明八千兩／十年白宅可穩定存在並實際居住。"
      - "若只能短暫事件化、之後坍縮，十年租約不得以常設租金成立。"

  pan_knowledge:
    - "白御行命時空道人向潘金蓮說明上述規則。"
    - "潘已理解：一次性用完收、長期依需要逐步擴。"
```

---

# 17｜WHITE-HOUSE25-E02｜白宅第一輪需求與師師設計任務

```yaml
WHITE_HOUSE_FIRST_ROUND_DESIGN:
  status: "DESIGN_IN_PROGRESS_NOT_BUILT"
  designer_first_pass: "李師師"
  task_nature:
    - "不是工匠施工圖"
    - "先做生活／功能／人員動線配置圖"
    - "第一輪以現在白家真正反覆需要之空間為準"

  mandatory_first_round_needs:
    - "白御行主屋／內外間"
    - "李師師白夫人獨立院或獨立起居套間"
    - "張麗華偶居院／房"
    - "白家丫頭房／下人房"
    - "浴房"
    - "梳洗／更衣空間"
    - "庫房／鎖間"
    - "小議事廳／內部談事處"
    - "茶水小廚／備膳空間"
    - "麗華酒窖（獨立上鎖）"
    - "正式宴會廳"

  banquet_hall:
    reason: "白家將來有商會、官面、富商與熟客來訪，需要正式招待空間"
    design_principle:
      - "宴會廳不得取代小議事廳"
      - "外客可到宴廳，不應必須穿越女眷／住人內院"
      - "宴廳附近應考慮備酒、熱菜、服務動線"
      - "白宅仍是家，不直接做成第二個風滿樓／第二家青樓"

  macro_zoning:
    front: "門廳／宴會廳／對外議事或接待"
    rear: "主屋／師師院／麗華偶居／丫頭與生活區"
    separator: "宜以小庭院、月洞門或其他半公共界線隔開"

  later_reviewers:
    - "李瓶兒：後勤、熱水、飯食、鎖匙、下人動線"
    - "張麗華：偶居、酒務、私人使用感"
    - "潘金蓮：成本、必要性、擴張順序與是否過度預造"

  current_hard_event:
    - "白御行命白三十二娘把第一輪設計任務轉達給李師師。"
    - "三十二娘已完成傳話。"
    - "李師師已開始在紙上分區、思考宴會廳、主屋、梳洗等配置。"
    - "第一版圖尚未完成；瓶兒／麗華／潘尚未開始正式會審。"
```

---

# 18｜WHITE-HOUSE25-E03｜原十年白宅框架仍保留但可按需求修訂

```yaml
WHITE_HOUSE_LEASE_FRAME:
  term_years: 10
  lump_sum_taels: 8000
  status: "CONDITIONALLY_AGREED_NOT_YET_ACTIVATED"
  activation: "需通過常設空間穩定性測試"
  ownership: "租用，不是所有權；仍屬觀止空間域"

  old_planned_elements_from_v3_1:
    - "主院"
    - "東／西側院"
    - "正房"
    - "客房八間"
    - "下人房"
    - "廚房"
    - "庫房"
    - "浴間"
    - "馬廄"
    - "小花園"
  new_note:
    - "上列舊構想不再視為一次性固定最終圖；依『需求先成立』原則可在師師第一版設計中縮、改、拆或延後。"
    - "正式宴會廳已被白御行明示拉入第一輪必要需求。"
```

---

# 19｜PERSONNEL-END25-E01｜本輪人才選拔收尾方式

```yaml
PERSONNEL_SELECTION_WRAP:
  white_yuxing_priority:
    direct_attention:
      - "六百兩十八歲候選"
    others:
      - "其餘最終留下／退回／方向分流由潘金蓮、師師、蘇清、疏影等整理後報告即可"
  funding_context:
    - "玩家口頭表示本批收人本金主要走商會帳，因此不需白御行逐筆親自盯小額人選。"
  final_report_status: "PENDING"

  required_report_fields:
    - "誰留"
    - "誰退／誰轉手"
    - "收購成本"
    - "初步清／紅／席面／技能方向"
    - "三個月訓練名冊"
```

---

# 20｜ACCOUNTING25｜新增可核對款項與尚未結清項目

```yaml
ACCOUNTING:
  lihua_gift:
    white_yuxing_outlay_taels: 200
    purchase_taels: 130
    lihua_pocket_taels: 70
    status: "COMPLETED_AS_GIFT_STRUCTURE"

  shishi_attendant_fund:
    white_yuxing_outlay_taels: 500
    status: "HANDED_TO_LI_SHISHI"
    note: "兩候選是否最終成交未確認"

  xiaocui_overnight:
    lodging_payment_taels: 0
    sex_payment_taels: 0
    status: "FREE_PRIVATE_OVERNIGHT_BY_XIAOCUI_CONSENT"

  candidate_18_600:
    gross_price_taels: 600
    planned_to_yahang_taels: 550
    planned_direct_to_candidate_taels: 50
    intake_payment_status: "NOT_HARD_CONFIRMED_COMPLETED"
    future_first_night_share_to_candidate: "15% if such auction later occurs"

  guanzhi_first_night_platform_context:
    typical_fee: "10% for this kind of entrusted respectable-family／virgin debut auction, as stated in current discussion"
    note: "需在正式制度文件／契約時再固化適用範圍，不自動泛化到所有交易。"

  white_house:
    proposed_taels: 8000
    term_years: 10
    payment_status: "NOT_ACTIVATED_UNTIL_STABILITY_TEST"

  petty_cash_32:
    original_taels: 100
    current_balance: "UNKNOWN"
    meal_bill_settlement: "NO_DIRECT_CONFIRMATION"
```

---

# 21｜人物與知情邊界

```yaml
KNOWLEDGE_BOUNDARIES:
  李師師:
    knows:
      - "自己是白家如夫人／主母級，對四女有內部調度權"
      - "白御行昨夜確實未回她床、今晨從西廊方向來；她高度懷疑小翠但沒有直接證據"
      - "白御行今晚打算再次在外找到一張床，且直接說死都不回她處"
      - "自己本月月事尚未來；若日後自己確認懷孕，答應第一個告知白御行"
      - "白宅第一輪空間由她先畫，目前已開始構思"
    does_not_know_as_fact:
      - "小翠昨夜房內每一步接觸內容"
      - "白御行與小翠實際沒有性交，除非日後兩人自行告知"
      - "今晚白御行可能選誰當第二張床目標"

  小翠:
    knows:
      - "白御行昨夜守住雙方講好的界線"
      - "自己主動抱、摸、引導手的位置並與白御行同床睡到天亮"
      - "自己沒有半夜把白御行趕走"
    private_boundary:
      - "不希望被對外粗暴敘述成『白御行睡了小翠＝性交』"
      - "不接受被定義成『已治好』"

  紅娘:
    knows:
      - "白御行今晨從西廊方向出現"
      - "小翠稍晚尚未起身"
    inference: "開始懷疑兩事有關，但無房內證據"

  潘金蓮:
    knows:
      - "三個月訓練／走秀驗收／集體換約完整內部制度"
      - "對新人公開版本需壓回三個月觀止訓練＋驗收＋淘汰風險"
      - "觀止常設空間應按長期需求逐步顯影，不得一次開大"

  六百兩候選:
    knows_as_current_public_terms:
      - "自己六百兩報價結構中五十兩直接給本人"
      - "前三個月在觀止受訓"
      - "三個月後有走秀驗收"
      - "表現差可能被退／轉手／賣去更低級場子"
      - "白御行承諾若日後真的進入出閣拍賣，她拿成交額 15%"
    heard_but_retracted_as_not_current_contract:
      - "商會換約、完整後台配置與後續拍賣內部機制"

  時空道人:
    function:
      - "重新出現在白御行真正出門後的回門事件"
      - "已向潘金蓮說明需求導向空間擴張規則"
```

---

# 22｜未決事項

```yaml
OPEN_LOOPS:
  personnel:
    - "潘金蓮等人提交本批最終留／退／成本／方向報告"
    - "六百兩十八歲候選：完成實際付款、牙行交割、觀止報備與三個月訓練入冊"
    - "李師師兩名侍女候選最終留一／留二／退誰；五百兩如何使用"

  training_system:
    - "三個月走秀精確日期尚未換算固化"
    - "三個月內每類工作／接客／分成細則尚需行政化"
    - "跨集體換約日之訂席／預付款收入歸屬細則尚未定"
    - "走秀當天『通過／不通過』之驗收標準尚需由潘、師師、蘇清、疏影、白希等拆分"

  virgin_auction:
    - "六百兩候選及其他處子何時／是否進正式出閣拍賣，走秀後另案"
    - "觀止 10% 平台費與姑娘個人分成須在正式委託／契約時寫清適用範圍"

  white_house:
    - "李師師第一版生活／功能圖完成"
    - "李瓶兒、張麗華、潘金蓮會審"
    - "八千兩十年白宅常設空間穩定性測試"
    - "若測試失敗，租約不得以十年常設宅成立"

  tonight_bed_wager:
    - "白御行今晚第二張床目標尚未選定"
    - "浮香／醉花／十三娘只在 HOLD 討論被分析，不是世界事件"
    - "賭局今晚成敗未決"

  xiaocui:
    - "昨夜對小翠長期男性／性關係態度造成多大影響仍未知，不得提前收斂"
    - "紅娘／師師是否日後查清昨夜真相未決"

  lihua:
    - "新侍女名字尚未硬記錄"
    - "侍女長期住宿等白宅後重排"

  shishi_pregnancy:
    - "月事尚未來但妊娠 UNKNOWN；等待未來實際生理／診斷結果"

  meals:
    - "六家候選供餐帳是否已由三十二娘以一百兩備用銀結清，缺乏直接確認"
```

---

# 23｜直接接關摘要

```yaml
DIRECT_CONTINUATION:
  date: "理火三年槐月二十五日"
  time: "白日"
  scene_state:
    - "白御行已從時空道人回門事件回到觀止。"
    - "潘金蓮已掌握新人三個月制度與常設空間『按需求擴張』規則。"
    - "六百兩候選今天仍只能旁觀，等待報備／交割手續。"
    - "三十二娘已到李師師處傳達白宅第一輪設計任務。"
    - "李師師已開始拿紙分主屋、宴會廳、梳洗、住人與內外區。"

  player_not_locked:
    - "白御行接下來可去看師師設計、等潘的人才報告、處理六百兩候選交割、巡其他幕後線，或自然推進到晚上。"
    - "導演不得替白御行選今晚去敲誰的門。"
```

---

# 24｜HOT V3.2 結論

```yaml
HOT_V3_2_CONCLUSION:
  hard_changes:
    - "槐月二十三日晚：張麗華按摩賭帳結清；其後雙方自主成人關係成立並同眠。"
    - "張麗華取得白御行送的 23 歲酒務型侍女；130兩成交，另70兩明示為麗華零花。"
    - "李師師白家如夫人／主母級權限已由白御行向紅伶等明示；紅伶開始常態跟師師學席面與樂曲。"
    - "槐月二十四日晚：小翠自願收留白御行同床一夜；沒有性交，小翠自主抱人、觸碰與指定手的位置；晨間仍拒絕『治癒』定義。"
    - "槐月二十五日晚存在第二張床白嫖賭局；尚未解決。"
    - "本批新人確立三個月觀止約／訓練制；前三個月觀止取得營運收入，商會不抽此階段營收。"
    - "三個月後走秀同時作集訓驗收、市場亮相與仍在名冊者集體換商會約日。"
    - "處子前三個月不辦正式出閣拍賣；走秀換約後若要出閣，由商會委託觀止代辦並帶入觀止人脈。"
    - "六百兩十八歲候選固定談判結構：550牙行＋50本人；白御行另承諾日後若真正出閣拍賣，個人拿15%。正式交割／入冊仍待硬確認。"
    - "新人公開知道三個月訓練、走秀驗收與表現差可能被退／轉賣／進更低級場；完整商會後台換約制度不是新人現階段正式契約資訊。"
    - "白御行真正出觀止再回門，時空道人重新出場並交籤。"
    - "觀止常設空間治理確立：需求先成立，空間再顯影；一次性事件空間用完可收，長期需求經穩定性測試逐步保留。"
    - "白宅第一輪需求由李師師先畫生活／功能圖；正式宴會廳已列第一輪必要空間；圖尚未完成。"

  anti_false_closure:
    - "小翠沒有被治好。"
    - "李師師沒有被確認懷孕。"
    - "六百兩候選沒有被記成已完成付款／正式入冊。"
    - "李師師兩名侍女候選沒有被記成已成交。"
    - "白宅沒有被記成已穩定生成。"
    - "今晚第二張床沒有被預先判定成功或指定對象。"
    - "浮香 V1.3 污染故事沒有回流。"
```


<!-- PROMOTED_HOT_SOURCE_END: 觀止青樓_白御行線_HOT_SAVE_V3.2_槐月二十五日白日_小翠同床純睡_三月集訓走秀換約_六百兩候選_白宅需求擴張與師師設計版.md -->

---

# APPENDIX I｜固化來源全文：觀止青樓_白御行線_HOT_SAVE_V3.3_槐月二十六日清晨_浮香自願留宿_紅娘煙幕揭穿_九幽帝皇聯誼會三日後訂單_大觀樓交接宴前置版.md

> **法位：E84–E92 細節追溯來源。** 此 HOT 內的 CURRENT_SCENE／HOLD 只代表當時快照；不得覆寫本 MASTER 截止或 V3.5–V3.7 疊加層。若原 HOT 內某個標成 YAML 的區塊本身語法不合法，本 MASTER 只把該 fence 改標為 text 隔離，內容原文不改，避免來源語法缺陷破壞 MASTER 解析。

<!-- PROMOTED_HOT_SOURCE_BEGIN: 觀止青樓_白御行線_HOT_SAVE_V3.3_槐月二十六日清晨_浮香自願留宿_紅娘煙幕揭穿_九幽帝皇聯誼會三日後訂單_大觀樓交接宴前置版.md -->
# 觀止青樓｜白御行線 HOT SAVE V3.3
## 理火三年槐月二十六日清晨｜浮香自願留宿 × 紅娘煙幕揭穿 × 九幽帝皇聯誼會三日後訂單 × 大觀樓交接宴前置版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V3_3_HUAI26_MORNING_FUXIANG_FREE_BED_HONGNIANG_DECOY_JIUYOU_EMPEROR_ASSOCIATION_ORDER"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V3.3"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V11.0-R2"
  character_source: "觀止人物卡池_LCAPG_V2.2_辭歲入觀止動機校正_青禾六條增補_正式版"
  story_time_span:
    start: "理火三年槐月二十五日晚／HOT V3.2 後"
    current: "理火三年槐月二十六日清晨"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AT_GUANZHI_FRONT_DESK_AFTER_PAN_RECEIVES_JIUYOU_ORDER_AND_ASKS_MAX_REIMBURSEMENT"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V3.2_槐月二十五日白日_小翠同床純睡_三月集訓走秀換約_六百兩候選_白宅需求擴張與師師設計版.md"
  previous_hot_sha256: "2615f819d4d34d3ebd8932bd34d112f0b1a55f88c19ea1857898f33bc0f835f7"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"

  experimental_overlays:
    performance_patch:
      file: "觀止青樓_PATCH_風月角色表演與接戲能力_V0.1-EXP_獨立試跑未併主系統.md"
      status: "INDEPENDENT_TRIAL_OVERLAY_NOT_MERGED"
    analyzer_exit_patch:
      file: "觀止青樓_PATCH_分析器退場_重大升階定義_SCOPED_REACTIVATION_顯影反污染_V0.1-EXP.md"
      status: "GUANZHI_SPECIFIC_OPTIONAL_EXPERIMENTAL_OVERLAY_NOT_MERGED"

  save_scope:
    - "HOT V3.2 後白御行第二張免費床賭局之紅娘煙幕與浮香實際留宿結果"
    - "白御行與浮香私房談話、白宅邀請邊界與當夜成年人親密事件"
    - "浮香成人場分析器滯留事故之世界反污染鎖；故障說明不倒灌人物台詞／人格"
    - "鬼差於浮香房外送達之九幽城帝皇聯誼會正式訂單"
    - "白御行對九幽城、后土、攝政王、朱天、帝皇區與帝皇聯誼會之玩家線背景陳述"
    - "帝皇聯誼會本屆部分家族交接名單"
    - "三日後十餘名皇帝至觀止舉行交接大會之訂單需求"
    - "清倌／紅倌需求分流、公帳消費與白御行審帳權"
    - "三輪重量級拍賣只保存為白御行盤算／候選企畫，尚未排程、未取得任何女性本人同意"
    - "潘金蓮今晨收到訂單並開始籌備；目前等待白御行回答最高核銷額"
```

---

# 0｜提交法位、來源與反污染

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V3.2_槐月二十五日白日_小翠同床純睡_三月集訓走秀換約_六百兩候選_白宅需求擴張與師師設計版.md"
    role: "本檔直接前置 HOT；V3.2 及以前有效硬狀態全部繼承"

  master_archive:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"
    role: "截至 HOT V2.5 之長期因果；V2.6-V3.2 由 HOT 鏈承接"

  current_route_conversation_commit:
    role: "HOT V3.2 後至本次 HOT SAVE 命令前之直接劇情、玩家明示自身言行／過往背景、NPC 可觀察回應與玩家明示校正"

  runtime_reference:
    file: "觀止青樓_主程序_V11.0-R2_人物卡池單一接線輕量正式版.md"
    venue_anchor:
      formal_name: "大觀樓"
      function: "二樓中央大圓桌宴席空間"
      capacity: "約二十至三十人"
      distinction:
        - "大觀樓不是風滿樓。"
        - "風滿樓為千人級大型聚會／大型擴張場。"
        - "大觀樓為二樓中央大圓桌、小型高規格宴席空間，適合約二十至三十人。"
      note:
        - "三日後帝皇聯誼會十餘名皇帝交接宴應錨定於大觀樓。"
        - "不得再把大觀樓寫成風滿樓別稱或千人場。"

ANTI_CORRUPTION:
  fuxiang_hot_v1_3:
    status: "ILLEGAL_CORRUPTED_SAVE_AUDIT_ONLY"
    effect:
      - "浮香 HOT V1.3 整段仍不得使用。"
      - "本 V3.3 之浮香關係與成人事件全部來自 HOT V3.2 後重新合法生長之直接劇情，不引用 V1.3。"

  ghost_mail_misclassification:
    status: "PLAYER_CORRECTED"
    false_or_superseded_interpretation:
      - "最初導演曾把鬼差文件理解為『請帖／邀請白御行赴約』。"
    correction:
      - "玩家後續明示：鬼差送來的不是請帖，而是帝皇聯誼會交給潘金蓮／觀止的正式訂單。"
      - "因此本 SAVE 只保存 ORDER；先前『請帖』說法不得回流成世界事實。"

  analyzer_incident:
    status: "GOVERNANCE_FAILURE_NOT_CHARACTER_FACT"
    note:
      - "浮香成人場曾出現關係／安全分析器滯留、人物語言被治理解說污染之故障。"
      - "故障分類與修補只屬治理／回歸資料；不得把錯誤台詞、講義語氣或安全說明寫回浮香人格。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年槐月二十六日"
  time: "清晨"
  primary_location: "觀止青樓／前堂櫃台"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  player:
    name: "白御行"
    current_position: "潘金蓮櫃台前"
    immediate_context:
      - "昨夜自浮香房醒來／下樓後，紅娘當場因煙幕局被揭穿而抓狂。"
      - "白御行已把鬼差送來的帝皇聯誼會訂單交給潘金蓮。"
      - "已告知潘金蓮：該宴會支出走帝皇聯誼會公帳，白御行具有審查權。"

  pan_jinlian:
    current_position: "觀止前堂／櫃台"
    current_action:
      - "已閱讀訂單核心條件。"
      - "已開始叫春梅／瓶兒整理三日後席位、酒器、樂器、房數與相關籌備。"
    last_direct_question_to_player:
      - "這群皇帝的公帳——最高核銷到多少？"

  direct_resume_point:
    - "下一幕先由白御行回答或處理『最高核銷額／審帳尺度』；不得替玩家自動決定金額。"
    - "三日後帝皇聯誼會交接宴已形成真實訂單與籌備事件，但具體菜單、價格、姑娘名單、房間分配與拍賣節目尚未全部成立。"
```

---

# 2｜V3.2 繼承後仍有效之核心狀態

```yaml
INHERITED_ACTIVE_CORE:
  training_and_contract_switch:
    - "三個月新人集訓、走秀驗收、觀止約轉商會約之制度仍有效。"
    - "新人實際接客、出閣、拍賣與服務仍依本人資格／當下事件另行成立。"

  six_hundred_candidate:
    - "十八歲六百兩候選仍為高價候選線。"
    - "既有收購條件、個人五十兩、一成五未來出閣分成與訓練規則沿用 V3.2。"
    - "本輪僅被白御行納入三輪重量級拍賣的腦內盤算；尚未形成三日後實際上拍。"

  white_house:
    - "八千兩／十年條件式租用框架仍有效；需穩定空間真正形成後才啟動。"
    - "李師師已受命進行第一輪生活／功能設計。"
    - "本輪未因浮香談話或帝皇宴自動完成白宅建成、租金交付或永久入住。"

  bed_bet:
    - "白御行與李師師之『第二張免費床』賭局仍須在師師處正式結算。"
    - "賭局核心為：白御行需在無付費、無平兒安排、無權力施壓下，讓觀止女性自願讓他在自己的床／房留宿；性行為與床位判定分開。"
```

---

# 3｜BED25-E01｜紅娘煙幕局與錯誤傳聞

```yaml
EVENT_RECORD:
  event_id: "BED25-E01-HONGNIANG_DECOY"
  lifecycle_state: "COMPLETED_DECOY"
  event_axis_state: "COMPLETED"

  confirmed:
    - "白御行曾向紅娘提出免費床位局。"
    - "紅娘把『床位』與『性』分開，最終只接受一個遊戲性框架：白御行之後可敲門；不收錢；會開門；是否留下／睡覺不預先決定；可離開；不得強迫。"
    - "白御行實際上把紅娘設為煙幕與最後選項，沒有打算當夜真的去敲她房門。"
    - "白御行授意白紅伶散布『白總今晚睡紅娘的床／全套服務』『紅娘今晚不收錢』等煙幕說法。"
    - "上述內容是刻意製造的假傳聞，不是紅娘實際同意免費性服務。"

  morning_consequence:
    - "槐月二十六日清晨，紅娘看到白御行與浮香自樓上下來後，當場確認自己被當成煙幕，對白御行抓狂。"
    - "浮香在旁笑看／補刀；事件為喜劇性羞惱，不自動建立紅娘永久敵意或愛情。"

  pollution_lock:
    - "不得把假傳聞寫成紅娘真的提供免費全套服務。"
    - "不得把『紅娘留門／接受遊戲』改寫成已發生留宿或性行為。"
```

---

# 4｜FUXIANG25-26-E01｜浮香自願給床與白嫖賭局候選勝利

```yaml
EVENT_RECORD:
  event_id: "FUXIANG25-26-E01-FREE_OWN_BED_STAY"
  lifecycle_state: "COMPLETED_STAY"
  event_axis_state: "COMPLETED"

  location: "觀止／浮香私人房"
  time: "槐月二十五日晚至二十六日清晨"

  confirmed:
    - "白御行真正的第一目標一直是浮香；紅娘主要作煙幕。"
    - "白御行與浮香自二樓場面脫身後進入浮香私人房。"
    - "浮香在沒有收費、沒有權力壓迫、沒有被安排的情況下，自主決定讓白御行留在自己的房內並分半張自己的床。"
    - "因此依目前賭局已知條件，此事件構成『免費、自願、自己的床』的明確候選勝利。"
    - "是否正式判白御行贏下賭局，仍待李師師知道後進行實際結算；不得替師師提前宣判。"

  relationship_boundary:
    - "浮香給床不等於永久收留。"
    - "浮香給床不等於婚姻、如夫人、白家永久身份。"
    - "留宿與成人親密分軸成立。"
```

---

# 5｜FUXIANG25-E02｜白宅邀請與浮香位置

```yaml
FUXIANG_WHITE_HOUSE_TALK:
  status: "ROUTE_CONVERSATION_HARD_STATE"

  confirmed:
    - "白御行曾向浮香談及白宅與她可能的位置。"
    - "浮香目前不接受『永久成為白家人／夫人院固定成員』式直接收編。"
    - "若未來白宅實際穩定形成，且能給她一間可自由使用、能放琴、有窗、可住幾日又自行回觀止、沒有日常義務的房，她願意考慮／實地看看。"
    - "她沒有因此要求修改李師師正在做的第一輪白宅設計。"

  not_established:
    - "浮香已入住白宅"
    - "浮香取得夫人身份"
    - "浮香永久離開觀止"
    - "浮香對白御行形成永久承諾"
```

---

# 6｜FUXIANG25-E03｜當夜成年人親密事件

```yaml
ADULT_EVENT_RECORD:
  event_id: "FUXIANG25-E03-ADULT_INTIMACY"
  participants:
    - "白御行"
    - "浮香"
  adult_participants_confirmed: true
  location: "浮香私人房"
  time: "槐月二十五日深夜"

  event_axis:
    state: "COMPLETED_ADULT_INTIMACY"

  confirmed:
    - "雙方在當夜由親吻、擁抱與裸體同床逐步進入成年人親密事件。"
    - "浮香多次以自己的語言與可觀察行動形成主動／接受／回應；白御行也多次依她的即時回應調整。"
    - "事件後段包含已成立的性交與其後另一段成年人性親密；文字顯影曾採較低解析，但不得因此改寫成未發生。"
    - "浮香在互動中保留自己的節奏、戲謔、聲音與『女鬼』玩笑，不等於變成蘇清、張麗華或其他女人的複製。"
    - "雙方最終同床過夜，清晨一起下樓。"

  relation_axis:
    - "當夜慾望與親密成立。"
    - "不自動等於愛情、婚姻、永久專屬、永久性同意或人物所有權。"

  rendering_and_audit_note:
    - "本事件正是 FUXIANG-INC-001 的回歸樣本；治理故障不得回寫人物。"
    - "V11 EVENT / CHARACTER / RELATION / RENDERING 正交仍適用：顯影限制不等於事件不存在。"
```

---

# 7｜GHOST25-E01｜鬼差送達九幽帝皇聯誼會訂單

```yaml
EVENT_RECORD:
  event_id: "GHOST25-E01-JIUYOU_EMPEROR_ASSOCIATION_ORDER"
  lifecycle_state: "ACTIVE_ORDER"
  event_axis_state: "COMPLETED_DELIVERY"
  location: "浮香私人房／窗外"
  time: "槐月二十五日深夜"

  messenger:
    type: "鬼差"
    observable:
      - "黑衣／陰差形貌"
      - "從窗外送達文書"
      - "起初直呼『白御行』，經白御行糾正後改稱『白攝政王殿下』"
      - "接受白御行指示，回覆來方三日後來觀止"

  document:
    corrected_type: "帝皇聯誼會給觀止／潘金蓮的正式訂單"
    not: "私人請帖"
    recipient_operational: "潘金蓮／觀止青樓"
    delivery_intermediary: "白御行"

  confirmed_instruction_from_player:
    - "白御行收下訂單後命鬼差回去覆命：三日後讓他們來觀止即可。"

  not_established:
    - "鬼差知道訂單所有內情"
    - "任何未由玩家揭露的訂單細節"
    - "九幽／酆都對此宴會另有隱藏命令"
```

---

# 8｜JIUYOU-BACKGROUND25｜白御行公開說明之九幽背景

```yaml
PLAYER_STATED_BACKGROUND:
  source: "白御行本人於浮香房內向浮香說明"
  authority:
    - "白御行對自身過往、身分與自己參與之制度具有高權重自述法位。"
    - "除已由鬼差稱呼／訂單關係等可觀察事項外，其餘不自動推成所有世界角色已知的客觀全知事實。"

  statements:
    - "白御行稱其第一任正妻為后土娘娘；后土現為九幽城城主。"
    - "白御行稱九幽城現行制度大部分曾由自己設計。"
    - "白御行自認／被鬼差承認九幽城『攝政王』稱號。"
    - "后土屬甩手掌櫃型；白御行則是安排好制度後不常日常管理。"
    - "九幽城目前真正日常市長／管理者名為朱天。"
    - "朱天曾是定陶商會尚未轉型前最早的第一任總會長；現常副會長接其商會位置。"
    - "九幽有『皇帝區』：因缺乏『皇帝審判皇帝』的規則，歷代皇帝功過無人可合法定奪，因此形成制度 BUG；九幽不管、酆都不收。"
    - "白御行過去協助皇帝區建立『帝皇聯誼會』，讓皇帝們投資九幽產業、取得收入並維持享樂生活。"
    - "白御行稱自己對帝皇聯誼會公帳具有審查權。"
    - "武則天曾以『皇后』而非『皇帝』身份自報，走另一條報關／歸類通道離開皇帝區；此為白御行所述九幽軼事。"

  knowledge:
    heard_by:
      - "浮香"
    later_partial_shared_with:
      - "潘金蓮：至少已知本次帝皇聯誼會訂單、公帳與白御行審查權"
```

---

# 9｜EMPEROR-HANDOVER25｜本屆已揭露之帝皇家族交接名單

```yaml
EMPEROR_ASSOCIATION_HANDOVER:
  event_status: "SCHEDULED_IN_THREE_DAYS_BY_ORDER"
  total_expected: "十餘名皇帝；完整名單尚未全部揭露"
  purpose: "帝皇聯誼會交接大會"

  disclosed_roster:
    zhao_song:
      outgoing: "趙光義"
      incoming: "趙受益"
      role_change: "趙宋家族當家交接"
      note:
        - "趙受益是本白御行線已實際在觀止出現之人物。"
        - "其三日後是否以何種完整禮制／座次出場，尚未演出。"

    qin:
      honorary_president: "始皇"
      handover: false
      note:
        - "嬴家只有兩位皇帝；始皇本屆沒有打算交接。"
        - "始皇作為榮譽總會長將來觀止見證。"

    liu_han:
      outgoing: "劉邦"
      incoming: "劉病己"

    later_han_line:
      outgoing: "劉秀"
      incoming: "劉禪"
      structural_note:
        - "本屆安排把蜀漢納入後漢家族線。"
        - "未選劉備，而由劉禪接任。"

    tang_li:
      outgoing: "李世民"
      incoming: "李隆基"

    ming_zhu:
      outgoing: "朱棣"
      incoming: "豹房小王子"
      identity_expansion: "NOT_ADDED; preserve player's exact route nickname"

    qing:
      outgoing: "皇太極"
      incoming: "乾隆"

  unknown:
    - "其餘十餘名來客中的其他朝代／家族名單"
    - "正式座次"
    - "每一家的投票／交接機制"
    - "交接是否存在爭議或反對票"
```

---

# 10｜ORDER25-E02｜三日後觀止訂單需求

```yaml
JUIYOU_ORDER:
  status: "ACCEPTED_FOR_PREPARATION_NOT_FULLY_PRICED"
  event_date: "槐月二十九日若按三日後計；精確觀止曆換日由後續場景確認"
  venue:
    runtime_formal_anchor:
      name: "大觀樓"
      type: "二樓中央大圓桌宴席空間"
      capacity: "約二十至三十人"
    distinction:
      - "大觀樓與風滿樓為不同空間／場型。"
      - "風滿樓：千人級大型聚會／大型擴張場。"
      - "大觀樓：二樓中央大圓桌，可容納約二十至三十人。"
    intended_configuration:
      - "三日後十餘名皇帝之帝皇聯誼會交接宴使用大觀樓。"
      - "不啟動風滿樓千人級大型聚會狀態。"
      - "大圓桌下方懸空之既有空間形態沿用玩家明示設定。"

  guests:
    expected_count: "十餘名皇帝"
    nature: "帝皇聯誼會交接與見證"

  billing:
    payer: "帝皇聯誼會公帳"
    audit_right:
      holder: "白御行"
      confirmed_by_player: true
    current_max_reimbursement: "UNSETTLED"
    pan_current_question: "最高核銷到多少？"

  entertainment_and_courtesan_requirement:
    qing_courtesans:
      requested_role:
        - "彈琴"
        - "跳舞"
        - "宴樂／場面表演"
      red_service_requested: false

    red_courtesans:
      order_wording_direction:
        - "要能碰的紅倌"
        - "不能全部只看不能碰"
      hard_boundary:
        - "此為客戶訂單需求類型，不等於任何特定紅倌已答應任何特定身體接觸或性服務。"
        - "實際出場／陪席／親近／房事仍須依觀止安排、人物資格、當下事件與個別女性自己的決定成立。"

  fuxiang:
    category_in_current_talk: "清倌"
    response:
      - "浮香接受若此宴成立，自己以彈琴／清倌表演身份出場。"
      - "她未因此取得紅倌服務義務。"
```

---

# 11｜AUCTION25-IDEA｜三輪重量級拍賣盤算【未成立】

```yaml
AUCTION_CONCEPT:
  lifecycle: "PLAYER_IDEA_ONLY"
  world_event_status: "NOT_SCHEDULED"
  pan_approved: false
  women_confirmed: false
  order_includes_auction: "NOT_ESTABLISHED"

  player_private_or_spoken_planning:
    three_weight_candidates:
      - "辭歲"
      - "十八歲六百兩候選"
      - "阿麗婭重新掛牌／重新拍賣"

  idea:
    - "白御行盤算若帝皇聯誼會公帳豪爽、十餘名歷代皇帝同席，三輪重量級競價可能形成極高場面與價格。"
    - "曾討論辭歲若上拍，可設計成一夜／單次而非二十八日長期服務框架。"
    - "曾討論六百兩候選可作另一輪高價新人。"
    - "曾討論阿麗婭若本人未來願意重新掛牌，可成第三個重量級。"

  hard_prohibitions:
    - "不得寫成潘金蓮已批准三輪拍賣。"
    - "不得寫成辭歲已同意上拍。"
    - "不得寫成六百兩候選已同意出閣／上拍。"
    - "不得寫成阿麗婭已重新掛牌或同意拍賣。"
    - "不得把訂單的『紅倌需求』自動擴張成『必須安排三輪初夜拍賣』。"
    - "不得先設定成交價、得標皇帝或服務結果。"
```

---

# 12｜PAN26-E01｜潘金蓮收單與籌備啟動

```yaml
EVENT_RECORD:
  event_id: "PAN26-E01-PAN_RECEIVES_JIUYOU_ORDER"
  lifecycle_state: "ACTIVE_PREPARATION"
  event_axis_state: "INITIATED"
  time: "槐月二十六日清晨"
  location: "觀止前堂／櫃台"

  confirmed:
    - "白御行將昨夜鬼差送達之訂單交給潘金蓮。"
    - "潘金蓮閱讀到帝皇聯誼會、三日後、十餘位、交接宴、大席、清倌琴舞宴樂、紅倌需求等核心內容。"
    - "白御行告知支出走帝皇聯誼會公帳，且自己有審查權。"
    - "潘金蓮立刻轉入掌櫃籌備狀態，叫春梅、瓶兒整理三日後席位／酒器／樂器／房數等準備。"
    - "潘金蓮尚未獲得『最高核銷額』答案。"

  not_yet:
    - "完整菜單"
    - "酒水規格與數量"
    - "正式姑娘名單"
    - "房間分配"
    - "是否有拍賣"
    - "拍賣人選與本人同意"
    - "宴席總預算"
    - "觀止對帝皇聯誼會之最終報價"
```

---

# 13｜人物與關係增量

```yaml
RELATION_DELTAS:
  bai_fuxiang:
    confirmed_new_events:
      - "浮香自主讓白御行免費留宿自己的房／床。"
      - "雙方完成一夜成年人親密與同床過夜。"
      - "浮香知道白御行自述之九幽／后土／攝政王／帝皇區背景。"
      - "浮香願以清倌琴藝身份參與三日後帝皇交接宴。"
    remains_unresolved:
      - "愛情"
      - "長期專屬"
      - "白宅固定入住"
      - "夫人／妾室／正妻等名分"
      - "未來成人關係頻率"

  bai_hongniang:
    confirmed_new_event:
      - "紅娘發現自己被白御行作為免費床賭局煙幕，清晨公開抓狂／記帳式抱怨。"
    not_established:
      - "永久決裂"
      - "真實免費性服務"
      - "留宿事實"
      - "愛情"

  pan_order:
    confirmed:
      - "潘金蓮取得三日後帝皇聯誼會訂單的營運主場。"
      - "白御行保留帝皇聯誼會公帳審查權。"
    relationship_effect:
      - "形成一個新的潘金蓮—白御行合作／預算制衡場：潘負責把單做大，白握核銷尺度。"
```

---

# 14｜知情範圍

```text
KNOWLEDGE_SCOPE:
  fuxiang_knows:
    - "白御行昨夜以紅娘為煙幕、真正第一目標是自己"
    - "九幽城／后土／攝政王／帝皇區／帝皇聯誼會之白御行自述背景"
    - "三日後十餘名皇帝將來觀止的訂單大意"
    - "部分交接名單"
    - "訂單要求清倌琴舞、紅倌需有可親近服務類型"

  hongniang_knows:
    - "白御行昨夜沒有去她房，而去了浮香房"
    - "自己曾被拿來作煙幕"
    unknown_or_not_confirmed:
      - "九幽訂單完整內容"
      - "三輪拍賣盤算"

  pan_jinlian_knows:
    - "三日後帝皇聯誼會交接宴訂單"
    - "十餘位皇帝"
    - "公帳付款"
    - "白御行有審查權"
    - "清倌／紅倌需求分流"
    - "需立即籌備大席、酒器、樂器、房數"
    unknown_or_not_yet_shared:
      - "完整三輪拍賣盤算是否已正式告訴她：NOT_CONFIRMED"
      - "白御行與浮香昨夜成人事件的細節"
      - "九幽制度所有背景細節"

  broader_guanzhi:
    - "目前尚不得自動讓全樓知道皇帝完整名單、拍賣企畫或九幽制度內情。"
```

---

# 15｜大觀樓與風滿樓空間法位校正

```yaml
VENUE_CORRECTION:
  da_guan_lou:
    formal_name: "大觀樓"
    location_form: "二樓中央"
    core_feature: "大型圓桌／大餐桌"
    capacity: "約二十至三十人"
    lower_space: "桌／場域下方為懸空空間"
    role:
      - "中小型高規格宴席"
      - "二三十人級核心會議／交接宴"
      - "適合帝皇聯誼會十餘名皇帝同桌"

  feng_man_lou:
    formal_name: "風滿樓"
    capacity_class: "千人級"
    role:
      - "大型聚會"
      - "大型遴選"
      - "千人級擴張公域"

  hard_distinction:
    - "大觀樓不是風滿樓別稱。"
    - "風滿樓不是二三十人大圓桌空間。"
    - "兩者不得再合併、互稱或以同一場型處理。"

  current_event_use:
    - "三日後帝皇聯誼會交接宴固定使用大觀樓。"
    - "本次不啟動風滿樓千人級大型場。"
```

---

# 16｜仍活躍但本輪未解之重要事項

```yaml
OPEN_THREADS:
  pan_su_civil:
    - "蘇清 vs 潘金蓮民事／帳務案仍 ACTIVE；五萬為索賠方向，不是判決。"

  white_jade_pool:
    - "仍在翻修／許願幣系統準備，不因本輪帝皇宴自動復開。"

  white_house:
    - "李師師第一輪配置尚待完成／會審／空間穩定顯影。"

  shishi_bed_bet:
    - "浮香免費給床已形成高資格勝利證據；仍待李師師正式結算。"

  emperor_order:
    - "最高核銷額"
    - "最終預算"
    - "大觀樓席位／座次"
    - "菜單與酒單"
    - "出場清倌／紅倌名單"
    - "紅倌個別服務範圍與當下成立"
    - "是否納入拍賣"
    - "完整十餘名皇帝名單"
    - "每個家族交接的實際儀式與衝突"

  three_auction_idea:
    - "只屬白御行盤算；需潘金蓮營運判斷與各女性本人事件資格後才能升格。"
```

---

# 17｜禁止回歸／防污染

```yaml
ANTI_REGRESSION:
  - "不得恢復浮香 HOT V1.3。"
  - "不得把浮香當夜親密事件寫成她永久歸屬白御行。"
  - "不得把床位勝利自動等於李師師已承認賭輸。"
  - "不得把紅娘假傳聞寫成真實免費全套服務。"
  - "不得把鬼差訂單重新寫成請白御行赴陰間的私人請帖。"
  - "不得把『紅倌要能碰』寫成任何具名姑娘 blanket 性同意。"
  - "不得因皇帝有錢／公帳就讓姑娘自動接受服務、拍賣或出閣。"
  - "不得把三輪拍賣盤算升格成已排程事件。"
  - "不得把阿麗婭重新掛牌寫成已發生；她是否重新掛牌仍須本人另行成立。"
  - "不得把辭歲或六百兩候選寫成已答應三日後上拍。"
  - "不得把『大觀樓／風滿樓』與前幾日大型遴選的數千人擴張狀態混成同一必然場面。"
  - "不得自行替『豹房小王子』補出玩家未明示的正式歷史身份進 SAVE。"
  - "不得解釋命運籤或替九幽未知制度補規則。"
```

---

# 18｜直接接關摘要

```yaml
DIRECT_RESUME:
  story_time: "理火三年槐月二十六日清晨"
  location: "觀止前堂／潘金蓮櫃台"
  immediate_scene:
    - "紅娘抓狂事件剛過。"
    - "浮香在場／近場，昨夜留宿與親密已完成。"
    - "潘金蓮已拿到三日後帝皇聯誼會交接宴訂單。"
    - "大觀樓為二樓中央約二十至三十人大圓桌宴席空間，與千人級風滿樓不同；本次帝皇聯誼會使用大觀樓。"
    - "潘金蓮已開始籌備。"
    - "當前需要白御行回答：帝皇聯誼會公帳最高核銷到多少。"

  next_action_owner: "PLAYER_FOR_BUDGET_DECISION; WORLD_MAY_PREPARE_AFTER_RESPONSE"
```

---

# 19｜HOT V3.3 結論

```yaml
HOT_V3_3_CONCLUSION:
  state: "VALID_CURRENT_HOT"
  replaces_for_direct_resume: "HOT V3.2"
  preserves_previous_chain: true
  master_updated: false
  character_pool_updated: false
  main_program_updated: false
  experimental_patch_merged: false

  key_new_hard_states:
    - "浮香自主免費給床，白御行第二張床賭局取得明確候選勝利證據。"
    - "浮香與白御行完成當夜成年人親密與同床。"
    - "紅娘煙幕於清晨揭穿，紅娘抓狂；假傳聞仍是假。"
    - "鬼差送達的是帝皇聯誼會訂單，不是請帖。"
    - "三日後十餘名皇帝將來觀止舉行帝皇家族交接大會。"
    - "已揭露趙宋、秦、漢、後漢／蜀漢、唐、明、清等部分交接安排。"
    - "宴會支出走帝皇聯誼會公帳，白御行有審查權。"
    - "訂單明示清倌主琴舞宴樂、紅倌需提供可親近類型；個別服務仍不自動成立。"
    - "潘金蓮已接單並開始籌備。"
    - "三輪重量級拍賣仍只是白御行盤算，沒有任何一輪正式成立。"
    - "大觀樓為本次三日後帝皇宴正式空間錨點；風滿樓另為千人級大型聚會場，兩者不可混用。"

  hold_question:
    - "帝皇聯誼會公帳最高核銷額是多少？"
```

<!-- PROMOTED_HOT_SOURCE_END: 觀止青樓_白御行線_HOT_SAVE_V3.3_槐月二十六日清晨_浮香自願留宿_紅娘煙幕揭穿_九幽帝皇聯誼會三日後訂單_大觀樓交接宴前置版.md -->

---

# APPENDIX J｜固化來源全文：觀止青樓_白御行線_HOT_SAVE_V3.4_槐月二十六日深夜_第二免費床成立_小翠三娘實習_紅娘側賭輸_三人抱睡版.md

> **法位：E84–E92 細節追溯來源。** 此 HOT 內的 CURRENT_SCENE／HOLD 只代表當時快照；不得覆寫本 MASTER 截止或 V3.5–V3.7 疊加層。若原 HOT 內某個標成 YAML 的區塊本身語法不合法，本 MASTER 只把該 fence 改標為 text 隔離，內容原文不改，避免來源語法缺陷破壞 MASTER 解析。

<!-- PROMOTED_HOT_SOURCE_BEGIN: 觀止青樓_白御行線_HOT_SAVE_V3.4_槐月二十六日深夜_第二免費床成立_小翠三娘實習_紅娘側賭輸_三人抱睡版.md -->
# 觀止青樓｜白御行線 HOT SAVE V3.4
## 理火三年槐月二十六日深夜｜帝皇宴籌備擴張 × 十三娘國運賭桌線 × 第二免費床成立 × 小翠老帶新實習 × 紅娘側賭輸 × 三人抱睡版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V3_4_HUAI26_NIGHT_SECOND_FREE_BED_XIAOCUI_SANNIANG_APPRENTICESHIP_HONGNIANG_SIDE_BET_THREE_PERSON_SLEEP"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V3.4"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V11.0-R2"
  character_source: "觀止人物卡池_LCAPG_V2.2_辭歲入觀止動機校正_青禾六條增補_正式版"
  story_time_span:
    start: "理火三年槐月二十六日清晨／HOT V3.3 後"
    current: "理火三年槐月二十六日深夜"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_IN_BAI_SANNIANG_ROOM_AFTER_BAI_HOLDS_XIAOCUI_SANNIANG_HOLDS_BAI_AND_ALL_FALL_ASLEEP"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V3.3_槐月二十六日清晨_浮香自願留宿_紅娘煙幕揭穿_九幽帝皇聯誼會三日後訂單_大觀樓交接宴前置版.md"
  previous_hot_sha256: "7c7e2c3d3acc6940e954cdf9fd3ad9f00cc4210090a926734a14baffad572c57"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"

  experimental_overlays:
    performance_patch:
      file: "觀止青樓_PATCH_風月角色表演與接戲能力_V0.1-EXP_獨立試跑未併主系統.md"
      status: "INDEPENDENT_TRIAL_OVERLAY_NOT_MERGED"
    analyzer_exit_patch:
      file: "觀止青樓_PATCH_分析器退場_重大升階定義_SCOPED_REACTIVATION_顯影反污染_V0.1-EXP.md"
      status: "GUANZHI_SPECIFIC_OPTIONAL_EXPERIMENTAL_OVERLAY_NOT_MERGED"

  save_scope:
    - "HOT V3.3 後至槐月二十六日深夜之直接玩家線事件"
    - "九幽帝皇聯誼會三日後大觀樓交接宴之新增營運安排與人物邀約"
    - "十三娘豹子賭局、白御行敗局、國運／陰德／首飾幸運資產情報交付"
    - "浮香第一局免費床與李師師正式認輸之後續結算法位校正"
    - "李師師第二局免費床賭約、紅娘側賭、白三娘借床與小翠『大件行李』公開成立"
    - "第二局免費床由李師師正式認輸；紅娘側賭因此由紅娘敗北"
    - "白三娘房內成年人親密、黑暗教學、小翠有限自選實習與風月接客心理教學"
    - "小翠今晚最後自行決定停止實習；白御行抱小翠、白三娘抱白御行三人安靜入睡"
    - "未來青禾按摩學習、沈萬三高端客戶座談等僅保存為提案／待執行，不升格成已發生"
```

---

# 0｜提交法位、來源與本輪反污染

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V3.3_槐月二十六日清晨_浮香自願留宿_紅娘煙幕揭穿_九幽帝皇聯誼會三日後訂單_大觀樓交接宴前置版.md"
    role: "本檔直接前置 HOT；V3.3 及以前有效硬狀態全部繼承，除本檔明示校正者"

  master_archive:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"
    role: "截至 HOT V2.5 之長期因果；V2.6-V3.3 由 HOT 鏈承接"

  current_route_conversation_commit:
    role: "HOT V3.3 後至本次 HOT SAVE 命令前之直接劇情、玩家明示自身言行、NPC 可觀察回應、玩家明示校正與已成立賭約／同意／拒絕"

COMMIT_NOTE:
  - "本檔取代 HOT V3.3，成為白御行線最新直接接關切片；V3.3 保留為前置歷史來源。"
  - "本次只更新 HOT；不更新 MASTER，不修改人物卡池，不修改主程序，不合併實驗 PATCH。"
  - "本輪所有成人事件只記已成立事件軸；不以服務職業、同房、同床、觀察、觸碰、挑逗或賭約推導 blanket 性同意。"
  - "小翠今晚之『實習』只等於她自行選擇的一小段參與與學習；不得倒推成她已治癒、已接受全面性交、已成雙人服務正式紅倌。"
  - "床位、成人親密、賭約、訓練、職業能力、關係與同意分軸記錄。"

BED_BET_NUMBERING_CORRECTION:
  status: "PLAYER_ROUTE_CLARIFIED"
  corrected_chain:
    first_free_bed_bet:
      woman: "浮香"
      result: "白御行勝；李師師後續已正式承認『這一局你贏』"
    second_free_bed_bet:
      bed_owner: "白三娘"
      borrower_and_carrier: "小翠"
      player_role: "小翠帶上床之『大件行李』"
      result: "白御行勝；李師師已正式承認第二局敗北"
  superseded_wording:
    - "HOT V3.3 若將浮香事件描述成『第二張免費床』或『第二局』，其編號語意由本檔校正；事件本身仍有效。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年槐月二十六日"
  time: "深夜；三人已入睡；精確時刻未知"
  primary_location: "觀止青樓／白三娘私人房／白三娘的床"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  player:
    name: "白御行"
    current_position: "白三娘床上"
    current_state:
      - "已停止教學與成人互動"
      - "正抱著小翠入睡"

  xiaocui:
    current_position: "白御行懷中"
    current_state:
      - "今晚實習已由她自行宣告『學夠了／到這裡』"
      - "最後接受與白御行相抱純睡"
      - "已逐漸放鬆並入睡"

  bai_sanniang:
    current_position: "白御行身後／抱著白御行"
    current_state:
      - "今晚成人互動與老帶新教學已停止"
      - "已抱著白御行入睡"

  direct_resume_point:
    - "當前沒有未回答問題。"
    - "若自然推進，可從三人夜間睡眠後的翌晨、樓內前堂新動靜或帝皇宴籌備回報開始。"
    - "不得替白御行在睡眠中作出新的成人、交易、付款、承諾或離房決定。"
```

---

# 2｜V3.3 繼承後仍活躍之核心狀態

```yaml
INHERITED_ACTIVE_CORE:
  emperor_association_order:
    - "三日後帝皇聯誼會十餘名皇帝將至觀止舉行家族交接／見證大會。"
    - "正式場地為大觀樓；大觀樓與千人級風滿樓不可混用。"
    - "帝皇聯誼會公帳付款；白御行保留審查權。"
    - "潘金蓮已進入籌備狀態。"

  emperor_roster_disclosed:
    - "趙宋：趙光義 → 趙受益"
    - "秦：始皇以榮譽總會長／見證角色出席；無交接"
    - "劉漢：劉邦 → 劉病己"
    - "後漢／蜀漢線：劉秀 → 劉禪"
    - "唐李：李世民 → 李隆基"
    - "明朱：朱棣 → 豹房小王子；不得擅自補正式歷史身份"
    - "清愛新覺羅：皇太極 → 乾隆"

  white_jade_pool:
    - "白玉池仍非正式重新營業狀態；阿泠主權與實際開池條件不得被帝皇宴需求覆蓋。"

  white_house:
    - "李師師第一輪白宅生活／功能設計仍屬活躍線。"
    - "白宅未因本輪事件自動完成。"

  pan_su_civil:
    - "蘇清 vs 潘金蓮民事／帳務案仍 ACTIVE；五萬仍是索賠方向，不是既成判決。"
```

---

# 3｜EMPEROR26-E01｜三日後帝皇宴新增籌備方向

```yaml
EMPEROR_EVENT_PREPARATION_DELTA:
  status: "ACTIVE_PREPARATION"
  date_target: "槐月二十九日前後；依『三日後』換日實際場景確認"
  venue: "大觀樓"

  financial_assurance:
    confirmed_player_statement:
      - "白御行向潘金蓮保證不要擔心錢，自己有把握把帳收回來。"
    max_public_account_reimbursement: "STILL_NO_EXACT_NUMERIC_CAP_CONFIRMED"
    note:
      - "財務把握／保證可收帳不等於已設定固定最高核銷額。"

  operational_challenges_given_to_pan:
    - "設法說服六條御息所出席；角色定位偏高桌／貴族／場面人物，不預設為性服務。"
    - "詢問紅娘是否願參與帝皇宴；具體服務仍由當下人物決定。"
    - "分別詢問阿麗婭、十八歲六百兩候選、辭歲，是否願意參加單夜的三人同晚初夜／出閣型競價企畫；三人必須各自同意，包括是否接受同晚公開價格比較。"
    - "單夜模式被提出作為避免傳統二十八日出閣破壞三個月集訓之方案；目前是營運設計，不代表三人已答應。"
    - "白三娘與青禾可作資深／特殊技術角色候選；青禾定位仍是按摩／身體照護專長，不自動成紅倌性服務。"
    - "嘗試在三日內讓白玉池具備可用條件，但不得壓過阿泠主權或把未開池寫成已復業。"

  high_table_and_companion:
    zhang_lihua:
      status: "CONFIRMED_AS_BAI_COMPANION_FOR_EVENT"
      role:
        - "以白御行女性伴侶／場面人物出席"
        - "不是以紅倌、性服務或拍賣品身份出席"
      procurement:
        - "白御行給張麗華 100 兩作帝皇宴衣裝採買／準備用途。"
      diaochan_invitation:
        - "白御行請張麗華試著邀貂蟬。"
        - "麗華答應去試，不保證成功；貂蟬尚未確認出席。"
        - "貂蟬若出席之價值偏權力場／英雄帝王場面理解，不自動等於性服務。"

  zhao_shouyi:
    - "趙受益是觀止常客／既有人物；觀止需避免在祖先與同儕面前讓其場面難堪。"

  precedent:
    - "第四卷已有女帝下午茶等高權人物聚會先例；本次不是觀止第一次接觸帝王級賓客。"
```

---

# 4｜SHISANNIANG26-E01｜十三娘豹子賭局與國運賭桌線

```yaml
EVENT_RECORD:
  event_id: "SHISANNIANG26-E01-LEOPARD_BET_NATIONAL_FORTUNE_INTEL"
  lifecycle_state: "COMPLETED_BET_ACTIVE_FUTURE_OPPORTUNITY"
  location: "觀止／十三娘賭桌與私下談話區"

  wager:
    player_bet_condition: "白御行只壓豹子"
    stakes:
      if_bai_wins:
        - "十三娘答應一次由她本人進入成年人親密事件；當場仍保留自身即時意願與邊界。"
      if_bai_loses:
        - "白御行交付『如何取得頂級幸運』的完整關鍵情報，並把十三娘引到可實際操作的路徑。"

  invalid_roll_pollution:
    invalid_result: "3-3-1"
    reason:
      - "白御行先前說『我壓小～～翠』是叫小翠來擲骰，不是押『小』。"
      - "因此先行被誤開的 3-3-1 不屬合法賭局結果。"

  valid_roll:
    roller: "小翠"
    result: "1-6-6"
    leopard: false
    outcome: "白御行敗"

  consequence:
    - "十三娘沒有輸掉自己的床／成人賭注沒有被白御行贏得。"
    - "白御行履行敗局，私下告知十三娘帝皇宴與國運賭局機會。"

  national_fortune_intel:
    player_disclosed:
      - "帝皇宴來客喜歡賭。"
      - "帝皇身上最高價值資產之一是國運。"
      - "國運可經九幽／城隍司相關估價與轉換機制處理。"
      - "國運可轉存於首飾／珠寶一類可持有媒介，佩戴者可獲高階幸運效果；存量越多，使用時間越長。"
      - "九幽資產可由城隍司估價，並涉及陰德及陽間氣運之轉換；包括國運層級。"

  shisanniang_response:
    - "十三娘迅速理解自己可在帝皇宴設賭桌，爭取贏取皇帝可合法轉移的國運資產。"
    - "她對帝皇宴的主要動機因此轉為『賭桌操盤者／國運獵手』，不是預設性服務者。"
    - "她要求釐清哪些國運可由個別皇帝／家族／朝代／公帳合法持有與轉讓，以及城隍司現場估價、有效轉移、首飾存儲的具體規則。"

  unresolved_rule_questions:
    - "個人皇帝國運、家族國運、朝代國運、帝皇聯誼會公帳之間的資產法位"
    - "現場城隍司估價師能否／如何合法處理國運轉讓"
    - "國運存入首飾的正式程序、上限與所有權"
```

---

# 5｜FUXIANG26-E01｜第一局免費床正式結算

```yaml
FIRST_FREE_BED_BET:
  status: "COMPLETED_BAI_WIN"
  woman: "浮香"
  qualifying_event:
    - "浮香此前在無付款、無平兒安排、無權力施壓下，自願讓白御行留在自己的房與自己的床。"
    - "床位與後續成年人親密為分開成立事件。"

  li_shishi_settlement:
    confirmed:
      - "白御行私下以『浮香姑娘，全套』提示李師師。"
      - "李師師正式承認：『我認……這一局你贏。』"

  anti_regression:
    - "此後不得再把第一局寫成『尚待李師師結算』。"
    - "不得因後來又開第二局而把浮香勝利抹掉或改成第二局。"
```

---

# 6｜BED26-E02｜李師師第二局免費床賭約

```yaml
SECOND_FREE_BED_BET:
  status: "COMPLETED_BAI_WIN"
  time_window: "槐月二十六日晚至翌晨"

  final_terms:
    - "白御行須找另一名成年觀止女性；不得是浮香。"
    - "對方須自願讓白御行免費在她自己的床上留宿／睡。"
    - "既有關係、人脈、信任、魅力、調情、共同歷史都可以使用。"
    - "不得為床位付款。"
    - "不得由平兒、潘金蓮、李師師、張麗華或其他權力人物安排／命令。"
    - "不得以白御行職權、身份或權力施壓。"
    - "床不等於性；只要床位成立即可勝。"
    - "其他成年人可同房／同床附近；床主人必須知情且自願同意。"
    - "拒絕不得被解讀成欲拒還迎。"

  li_shishi_attitude:
    - "可以靠人脈；她要驗證白御行的人脈是否真能讓人自主給床，而不是白御行自己以為很熟。"
```

---

# 7｜HONGNIANG26-E02｜紅娘第二局側賭

```yaml
HONGNIANG_SIDE_BET:
  status: "HONGNIANG_LOST_PENDING_ONE_TIME_CONSEQUENCE"

  terms:
    if_bai_wins_second_free_bed:
      - "紅娘同意一次、免費，與李師師搭成包含白御行的成年人三人親密局。"
      - "執行時李師師仍需自己願意；紅娘與李師師各自保留當下界線與停止權。"
    if_bai_loses:
      - "白御行需在受訓姑娘面前公開承認：紅娘曾留門／可免費接待，而白御行自己沒膽進門。"
      - "不得用浮香解釋救場。"

  outcome:
    - "白御行已贏第二局免費床，因此紅娘敗。"
    - "側賭的一次免費三人局成為未來可執行賭債，但不是預先 blanket 性同意，也不是今晚自動執行。"

  prior_rumor_lock:
    actual:
      - "紅娘昨夜確實留門／備茶，願意讓白御行敲門後再決定後續。"
      - "白御行沒有去她房。"
      - "沒有發生紅娘免費全套服務或留宿。"
    hongniang_public_spin:
      - "紅娘可用『本來免費全套給他，可惜白總沒膽來』等誇張版本搶故事。"
      - "她本人知道這是在搶敘事，不是在改帳。"
```

---

# 8｜SANNIANG-XIAOCUI26-E01｜第二張免費床之成立方式

```yaml
EVENT_RECORD:
  event_id: "SANNIANG_XIAOCUI26-E01-BORROWED_BED_BIG_LUGGAGE"
  lifecycle_state: "COMPLETED"
  event_axis_state: "FREE_BED_CONFIRMED"
  bed_owner: "白三娘"
  borrower: "小翠"
  carried_person: "白御行／被小翠稱為大件行李"

  setup:
    - "白御行公開向白三娘問床。"
    - "白三娘表示自己有床可免費借，但先問用途。"
    - "白御行提出：由小翠用自己的名義向三娘借床，並把白御行作為『大件行李』順便帶上床。"

  bai_sanniang_consent:
    confirmed:
      - "白三娘自願同意把自己的床借給小翠。"
      - "白三娘明知白御行也會上床，仍自願同意。"
      - "不收費。"
      - "不是被欺騙，不是被權力命令。"

  xiaocui_consent_and_agency:
    confirmed:
      - "小翠明示『行。我帶。』"
      - "她接受自己是借床的人，白御行是她帶去的『大件行李』。"
      - "她保留自己睡哪裡、何時離開、是否繼續任何實習／親近的決定權。"
      - "沒有『既然來了就必須練』或自動性義務。"

  public_confirmation:
    - "小翠在前堂公開說：『床是我跟三娘借的！人也是我帶的！我就是要把這個大件行李搬上去！怎樣！』"
    - "白三娘公開確認：『我的床，我自己借……免費。』"
    - "受訓姑娘及多名觀止人物看到三人上樓。"

  lamp_out_confirmation:
    - "白御行、小翠、白三娘進入三娘房後，窗燈熄滅。"
    - "外部可確認三人進房、三娘自願借床、小翠自願帶人、沒有收錢、燈滅後無人立即離房。"
    - "外部無法知道熄燈後房內發生的具體私密事件。"

  li_shishi_settlement:
    - "李師師依第二局條件正式承認：『算他贏。』"

  structural_significance:
    - "小翠第一次在公共場合主動宣告自己對一個男人的安排權，而不是被動成為被選擇／被安排的人。"
```

---

# 9｜PUBLIC26-E01｜第二局免費床公開反應

```yaml
PUBLIC_REACTIONS:
  li_shishi:
    - "對白御行把第二局堆疊成『借床＋大件行李』感到荒謬與好笑，但仍正式認輸。"

  fuxiang:
    - "冷淡帶笑，不呈現被搶走或佔有式崩潰。"
    - "以『昨晚才說我是第一個，今晚就開始做第二張床的生意了，挺有效率』式語氣調侃。"

  zhang_lihua:
    - "對『大件行李／搭便車的貨』說法大笑，視為荒唐好戲。"

  hongniang:
    - "嘴上抗議／吐槽，但無法否認第二局條件已被滿足。"
    - "因此承擔自己先前側賭敗北。"

  shisanniang:
    - "嘲笑紅娘輸局，也指出自己至少沒有把自己的床輸掉。"

  trainees:
    - "可觀察到小翠主動安排男人、主動借床與公開說明。"
    - "此觀察不等於受訓姑娘可推定小翠房內有性交或 blanket 性同意。"
```

---

# 10｜SANNIANG26-E02｜白三娘房內成年人事件軸

```yaml
ADULT_EVENT_RECORD:
  event_id: "SANNIANG26-E02-ADULT_INTIMACY_WITH_BAI"
  participants:
    - "白御行"
    - "白三娘"
  adult_participants_confirmed: true
  location: "白三娘私人房／白三娘床"
  time: "槐月二十六日晚"
  state: "COMPLETED_FOR_THIS_NIGHT_BEFORE_SLEEP"

  confirmed:
    - "熄燈後白御行以玩笑方式表示可以用身體還白三娘借床人情。"
    - "白三娘自願接受她自己與白御行之間的成年人親密。"
    - "白三娘明示把小翠分開處理：小翠是否參與只能由小翠自己決定。"
    - "白御行與白三娘之間成年人親密事件成立；本 SAVE 不保存露骨性動作細節。"

  boundary:
    - "白三娘的同意不替小翠成立任何性同意。"
    - "小翠在場／觀察不等於加入白三娘與白御行的成年人事件。"
```

---

# 11｜XIAOCUI26-E02｜小翠今晚有限自選實習

```yaml
XIAOCUI_APPRENTICESHIP:
  event_id: "XIAOCUI26-E02-FIRST_SELF_CHOSEN_SMALL_APPRENTICESHIP"
  lifecycle_state: "COMPLETED_FOR_TONIGHT"
  location: "白三娘房／熄燈後"

  starting_position:
    - "小翠最初定位為觀察者／可提問者。"
    - "她沒有被要求必須參與。"

  self_chosen_entry:
    - "小翠先主動問：如果自己想試一點，可不可以。"
    - "白三娘要求她自己說範圍，不替她決定。"
    - "小翠明示：『可以試一點。』"
    - "她不要把『答應實習』解讀成什麼都算。"

  stated_scope:
    - "先靠近一點。"
    - "可用手做有限、非露骨的觸碰／感受。"
    - "可讓白御行回答她對男性反應與心理的問題。"
    - "可由白三娘教她雙人場怎麼看、怎麼配合。"
    - "更後面的程度她當時不知道，不預先答應。"
    - "她自己覺得夠了就停。"

  actual_small_participation:
    - "小翠在黑暗中自行靠近。"
    - "曾以手摸到被褥、白三娘手臂、白御行肩膀等，並自行停／收回。"
    - "後來保持在她自己定義的小範圍內靠近、觸碰、提問與觀察。"
    - "本夜沒有合法事件依據可將小翠寫成完成性交、完成完整三人性行為或成為固定雙人服務搭檔。"

  end_of_session:
    - "白御行最後表示今晚不要想太多、已學夠。"
    - "小翠接受並自行停課。"
    - "小翠沒有被宣告『治好』，也沒有宣告自己從此不再怕或全面接受男人。"

  key_relation_change:
    - "小翠從『我只看』推進到『我可以自己選擇試一點，並自己決定到哪裡停』。"
    - "這是她的自主權與職業學習姿態變化，不是全面性意願升格。"
```

---

# 12｜XIAOCUI26-E03｜今晚風月實習所學之硬內容

```yaml
XIAOCUI_TRADECRAFT_LEARNING:
  source_context: "白御行、白三娘、小翠於黑暗房內的實際對話"
  status: "LEARNED_CONVERSATIONAL_CONTENT_NOT_YET_PROVEN_FIELD_SKILL"

  authenticity_and_rough_language:
    - "白御行提出：真正的粗話往往不是背好的髒話，而是人無暇判斷用詞時脫口而出的自然反應。"
    - "白三娘補充：粗話／聲音只能當反應信號，不能當作同意或享受的唯一判決。"
    - "小翠不該模仿白三娘式誇張反應，把自己練成廉價複製品。"

  performance_and_customer_detection:
    - "有經驗的男人可能察覺過度公式化、超出自身能力感的奉承／表演。"
    - "一旦客人把姑娘標記成『全在演』，後續真反應也可能被折價。"
    - "小翠目前的市場優勢之一是尚未學會大量假反應；『不會』本身可能形成真實感與價格。"

  male_dual_attention_model:
    - "白御行提出：男人在親密場景可同時有身體互動與心理／注意力兩套運作；正在與一人互動，不代表腦中不會被另一人吸引。"
    - "白三娘補充：注意力移動不等於已產生服務要求、同意、愛情或偏愛結論。"

  male_initiative_and_laziness:
    - "白御行提出：很多男人心裡喜歡女人主動，但因面子／角色想像不一定直接說。"
    - "白三娘教小翠應看實際反應，不只跟客人的嘴打架；但明確叫停／退避仍應視為停止。"

  male_anxiety:
    - "白御行承認男人面對難得機會也會怕自己表現不好／太快搞砸。"
    - "小翠因此第一次更清楚地把男人看成也可能緊張、怕丟臉、怕失敗的人，而不只是單向威脅來源。"

  inexperienced_adult_male_clients:
    - "白御行提醒：未來若遇到已成年但沒有性經驗的年輕客人，不要拿其生澀／緊張取笑。"
    - "白三娘補充：不要主動把『第一次』當公開羞辱；讓場子保持自然，不必把客人變成被考試的學生。"

  early_ejaculation_customer_handling:
    - "白御行提出此類客群可能很在意自尊／表現。"
    - "白三娘的風月實務重點：不要以嘲笑、突然結束整晚、誇張假安慰加重羞恥；可讓整晚價值不要只綁在單一性表現上。"
    - "紅倌不是郎中；不要把接客話術升格成醫療治療承諾。"

  massage_and_longer_pacing_proposal:
    - "白御行建議小翠未來可向青禾學按摩，把一部分接客時間放在前段放鬆、聊天與非單一性表現的親近上，以降低部分客人的壓力。"
    - "白三娘認為可作接客法／場面調度，但不保證能治療病情。"
    - "若客人本人願意且狀態允許，可休息後再看是否繼續；不得保證『第二次一定更好／更久』。"

  respect_value_and_repeat_business:
    - "白御行提出：給男人尊重，讓客人覺得花在姑娘身上的錢得到足夠回報與滿足，是回頭客的重要來源。"
    - "白三娘補充：『值得』不只在床上技巧，也包含被記得、被認真對待、沒有被羞辱。"

  secrecy_and_story_listening:
    - "白御行提出：男人很看重秘密；紅倌不要亂說話。"
    - "學會聽故事本身就能成為紅起來的能力。"
    - "白三娘進一步拆成：知道何時追問、何時不問、何時只說『後來呢』；下次仍記得上次故事進度。"
    - "客人夜深說出的家事、生意、官場、恐懼、羞恥等，不應被拿到大堂作可辨識笑話。"
    - "秘密信任可形成長期回頭關係。"

  xiaocui_self_summary:
    - "她開始理解紅倌不只學怎麼陪男人，而要看男人嘴上、身體、心理／注意力可能不同步。"
    - "她開始理解自己可以先學看、聽、記、保密，不必一開始就把目標設成『讓男人喜歡我』。"
```

---

# 13｜QINGHE-XIAOCUI26-IDEA｜小翠向青禾學按摩【提案】

```yaml
TRAINING_PROPOSAL:
  lifecycle: "PROPOSAL_NOT_EXECUTED"
  proposer: "白御行"
  proposed_student: "小翠"
  proposed_teacher: "青禾"

  purpose:
    - "讓小翠增加按摩／放鬆型前段服務能力。"
    - "未來面對緊張、在意表現或需要較長暖場的成年客人時，可增加場景節奏選擇。"
    - "可與白三娘老帶新／雙人服務模型互補。"

  hard_boundary:
    - "小翠尚未正式向青禾拜師／開始課程。"
    - "青禾尚未在本輪答應教小翠。"
    - "按摩不是治療早洩的醫療承諾。"
```

---

# 14｜SANNIANG-XIAOCUI26-IDEA｜白三娘老帶小雙人服務模型

```yaml
PAIR_SERVICE_PROPOSAL:
  lifecycle: "EARLY_PRACTICAL_FORM_EMERGING_NOT_FORMAL_ASSIGNMENT"
  participants:
    veteran: "白三娘"
    trainee: "小翠"

  tonight_confirmed_learning:
    - "小翠在白三娘房內完成第一次由自己決定範圍的小型觀察／參與實習。"
    - "白三娘實際扮演穩場、拆話、補充客戶心理與維持小翠自決範圍的角色。"

  future_possible_structure:
    - "三娘主場，小翠可先觀察／協助／聊天／按摩／記錄客戶反應。"
    - "小翠可依自己意願逐步參與；零參與仍可算完整學習狀態。"
    - "雙人場價值可在『誰接住哪一段』，不只在兩名女人同時進入性行為。"
    - "可觀察不同成年客戶的矛盾回答，建立多樣樣本，不把白御行當成全體男人代表。"

  not_established:
    - "小翠已成正式雙飛／雙人紅倌"
    - "小翠已接受未來任何客人性服務"
    - "今晚三人已完成完整三人性行為"
```

---

# 15｜SHENWANSHAN26-IDEA｜高端客戶閉門座談【潘金蓮待上鉤】

```yaml
HIGH_VALUE_CUSTOMER_PANEL_PROPOSAL:
  lifecycle: "PROPOSAL_NOT_EXECUTED"
  target: "沈萬三"
  proposer_in_room: "白御行"
  intended_internal_pitcher: "白三娘"
  intended_decision_maker: "潘金蓮"

  concept:
    - "以受訓姑娘需要理解高價值男性客戶為由，設計閉門式高端客戶問答／座談。"
    - "讓受訓姑娘問沈萬三：什麼服務值得花錢、什麼讓他覺得被坑、何種姑娘會回點、何種話一聽就假、什麼秘密最忌外流、床上／心理上男人如何想等。"
    - "沈萬三作為超高價值客戶，其意見屬高價樣本，但不代表全天下男人。"

  bait_structure:
    - "白三娘不直接對潘金蓮說『白御行要抓沈萬三來上課』。"
    - "先向潘金蓮提出營運問題：受訓姑娘缺高價值客戶留客／消費心理訓練。"
    - "讓潘金蓮自己盤點最合適的高端樣本，最好由潘金蓮自己說出『沈萬三』。"
    - "對沈萬三可包裝成『高端客戶閉門座談／請您替觀止挑毛病』，而非單純拿他作床事笑料。"

  current_state:
    - "白三娘口頭答應明日可向潘金蓮提案。"
    - "潘金蓮尚未真的收到提案。"
    - "沈萬三尚未被邀請、尚未答應、尚未到場。"
```

---

# 16｜XIAOCUI26-E04｜今晚睡眠收束

```yaml
SLEEP_EVENT:
  event_id: "XIAOCUI_SANNIANG26-E04-THREE_PERSON_QUIET_SLEEP"
  state: "ACTIVE_SLEEP_AT_SAVE"
  location: "白三娘私人床"

  arrangement:
    - "白御行抱著小翠。"
    - "白三娘從白御行身後抱著白御行。"
    - "三人停止教學、停止成人互動，安靜入睡。"

  xiaocui:
    - "在白御行抱她時先有短暫僵硬，但沒有離開。"
    - "她明示今晚最後就是睡覺，並自行調整到舒服位置。"
    - "逐漸放鬆、呼吸均勻並睡著。"

  meaning_boundary:
    - "此夜最後狀態是三人相抱純睡。"
    - "不得把純睡收束倒改成仍在進行性行為。"
    - "不得把小翠的抱睡解讀為永久接受白御行、永久性同意或關係承諾。"
```

---

# 17｜人物與關係增量

```yaml
RELATION_DELTAS:
  bai_xiaocui:
    new_confirmed:
      - "小翠第二次與白御行形成安全同床／抱睡經驗；本次床為白三娘所有。"
      - "小翠在公共場合主動把白御行定義成自己帶上樓的『大件行李』。"
      - "小翠今晚第一次主動選擇進入有限實習，並自己界定停止點。"
      - "她更直接知道白御行對她有性慾；她也明示『以前不給就不能做』的邏輯仍成立。"
      - "她從對談中新增『男人也會緊張、怕失敗、在意面子與秘密』的理解。"
    unresolved:
      - "小翠是否真正喜歡性"
      - "小翠是否願意未來對一般客戶提供任何特定性服務"
      - "小翠是否願與白三娘形成固定雙人搭檔"
      - "小翠對白御行之感情定義"
      - "先前對男人／疼痛／性關係的厭惡或恐懼會如何長期變化"

  bai_sanniang:
    new_confirmed:
      - "白三娘自願免費借床並自願與白御行形成當夜成年人親密。"
      - "她實際承擔小翠老帶新導師／穩場角色。"
      - "她接受『小翠未來可能向青禾學按摩』與『沈萬三高端客戶座談』作可操作提案。"

  xiaocui_sanniang:
    new_confirmed:
      - "形成第一次實際老帶新教學場。"
      - "三娘沒有替小翠答應性參與，而是要求小翠自己定義範圍。"
      - "小翠願意把三娘當作可拆白御行話、可驗證風月經驗的資深樣本。"

  bai_li_shishi:
    new_confirmed:
      - "第一局浮香免費床正式由師師認輸。"
      - "第二局白三娘／小翠免費床亦正式由師師認輸。"
      - "兩局皆為遊戲性人脈驗證，不自動產生師師永久嫉妒、決裂或關係降級。"

  bai_hongniang:
    new_confirmed:
      - "紅娘第二局側賭敗北。"
      - "未來欠一次條件式、一次性、免費與師師搭局之賭債；仍須兩名女性當下願意。"

  bai_shisanniang:
    new_confirmed:
      - "豹子賭局白御行敗。"
      - "白御行履行敗局，交付十三娘國運／頂級幸運路徑。"
      - "十三娘沒有被白御行贏床或贏下成人賭注。"
```

---

# 18｜知情範圍

```yaml
KNOWLEDGE_SCOPE:
  public_or_many_in_guanzhi_know:
    - "第二局免費床的公開借床結構：三娘自願借床、小翠自願帶白御行上樓、免費。"
    - "小翠公開稱白御行為『大件行李』並主張『床是我借的、人是我帶的』。"
    - "三人進白三娘房後燈滅，當晚未見立即離房。"
    - "李師師承認第二局白御行勝。"
    - "紅娘因此輸掉她與白御行的第二局側賭。"

  outsiders_do_not_know_as_fact:
    - "熄燈後白三娘與白御行具體成年人親密內容。"
    - "小翠今晚實習的每一步、她問了哪些男人心理問題、碰了哪些位置。"
    - "最後三人相抱睡眠的完整床內姿勢，除當事人外不可自動外洩。"

  xiaocui_knows:
    - "自己今晚主動借三娘的床並帶白御行上床。"
    - "自己可在實習中決定靠近、觸碰、提問、停止。"
    - "白御行明示早已對自己有性慾。"
    - "白三娘會在白御行吹牛／把自己當全天下男人時拆台。"
    - "今晚學到的接客心理與保密／聽故事技巧。"

  bai_sanniang_knows:
    - "小翠今晚只願意試一點，沒有答應全面參與。"
    - "白御行與小翠前述職業心理對話的大部分內容。"
    - "沈萬三閉門座談提案與準備讓潘金蓮自己說出沈萬三的誘餌策略。"

  shisanniang_knows:
    - "帝皇宴存在高價賭局機會。"
    - "國運可能成為可估價／可轉移／可存首飾的頂級幸運資產。"
    - "她仍需取得國運資產合法轉移的具體規則。"

  pan_jinlian:
    knows:
      - "帝皇宴訂單、公帳、白御行審查權、基本籌備方向。"
      - "白御行保證有把握收帳，不必先因錢縮手。"
    not_yet_confirmed_as_known:
      - "沈萬三閉門座談提案"
      - "十三娘國運賭桌的全部細節"
      - "白三娘房內今晚私密事件"
```

---

# 19｜仍活躍但未解事項

```yaml
OPEN_THREADS:
  emperor_event:
    - "潘金蓮具體完成的三日籌備方案尚未回報。"
    - "六條御息所是否願意出席未定。"
    - "紅娘是否願意以何角色參與未定。"
    - "阿麗婭、十八歲六百兩候選、辭歲是否各自同意單夜三人同晚競價未定。"
    - "白玉池能否在三日內合法／實際具備使用條件未定。"
    - "貂蟬是否接受張麗華邀請未定。"
    - "張麗華 100 兩衣裝採買成果尚未出場。"
    - "大觀樓座次、酒菜、節目、房間分配、最終價格與公帳核銷上限仍未完全確定。"

  shisanniang_national_fortune:
    - "國運可合法持有／轉讓之法位需確認。"
    - "是否能請城隍司估價師到場需確認。"
    - "首飾存儲機制與賭桌規則尚未固化。"

  hongniang_side_bet:
    - "紅娘已輸；一次免費與李師師搭局的賭債尚未執行。"
    - "執行時仍需李師師當下願意，紅娘與師師均保留自己的成人邊界。"

  xiaocui_training:
    - "向青禾學按摩只是提案，尚未開課。"
    - "與白三娘雙人服務只形成第一個實習樣本，尚未成正式工作安排。"
    - "今晚的新理解是否會轉化成面對一般客人的能力仍未知。"

  shen_wanshan_panel:
    - "白三娘尚未真正向潘金蓮提案。"
    - "潘金蓮尚未自己說出沈萬三。"
    - "沈萬三尚未被邀請／上鉤／到場。"

  fate_stick:
    - "槐月二十六日命運籤：『一門踏出千燈遠／回首春風不認人』。"
    - "目前沒有合法解籤；不得自行補出命定答案。"

  white_house_and_civil:
    - "白宅第一輪設計仍活躍。"
    - "蘇清 vs 潘金蓮民事／帳務案仍 ACTIVE。"
```

---

# 20｜禁止回歸／防污染

```yaml
ANTI_REGRESSION:
  - "不得把浮香再寫成第二局免費床；浮香＝第一局，白三娘／小翠＝第二局。"
  - "不得再寫第一局或第二局仍待李師師判定；兩局師師都已正式認輸。"
  - "不得把紅娘昨夜煙幕傳聞寫成她真的免費提供全套服務；她沒有被白御行進房。"
  - "不得把紅娘側賭寫成現在就必須執行、永久免費、永久性同意或李師師已提前同意。"
  - "不得把十三娘 3-3-1 當合法骰局；合法結果只有小翠擲出的 1-6-6，白御行敗。"
  - "不得把十三娘寫成已把床／成人賭注輸給白御行。"
  - "不得把國運賭桌寫成已完成正式規則或已取得皇帝國運。"
  - "不得把潘金蓮的帝皇宴籌備寫成六條、紅娘、阿麗婭、六百兩候選、辭歲、貂蟬都已答應。"
  - "不得把白玉池寫成已重新營業。"
  - "不得把小翠今晚的小型實習寫成完整三人性行為、性交、全面同意、永久接客準備完成或『已治癒』。"
  - "不得把白三娘對自身成人互動的同意擴張到小翠。"
  - "不得把『男人很懶』『男人兩套系統』『四個男人一個早洩』等玩家／人物概括語句升格成世界醫學統計真理；在 SAVE 只保留其作為接客心理討論內容。"
  - "不得把按摩、較長暖場、第二次嘗試等風月技巧寫成醫療治療承諾。"
  - "不得把沈萬三座談寫成已發生；目前只是白御行提案、白三娘答應明日嘗試引潘金蓮自己上鉤。"
  - "不得解釋槐月二十六日命運籤。"
  - "不得把大觀樓與風滿樓混用。"
```

---

# 21｜直接接關摘要

```yaml
DIRECT_RESUME:
  story_time: "理火三年槐月二十六日深夜"
  location: "觀止青樓／白三娘房／床上"
  immediate_scene:
    - "第二局免費床已成立並由李師師正式認輸。"
    - "紅娘側賭已輸，但一次條件式三人局賭債尚未執行。"
    - "白三娘與白御行今晚成人親密已結束。"
    - "小翠完成第一次自行定範圍的小型實習，已明示今晚學夠、停止。"
    - "白御行抱小翠，白三娘從後抱白御行，三人安靜睡著。"
    - "房外只能知道三人入房、免費借床、燈滅、未立即離房；不知道內部細節。"

  next_world_threads_ready_to_light:
    - "翌晨白三娘是否去向潘金蓮提出高端客戶座談"
    - "潘金蓮帝皇宴三日籌備回報"
    - "張麗華 100 兩衣裝與貂蟬邀請結果"
    - "六條／紅娘／三名競價候選／白玉池的個別回覆"
    - "十三娘國運賭桌合法規則與城隍司估價師"
    - "小翠是否真的去找青禾學按摩"

  next_action_owner:
    - "WORLD_MAY_NATURALLY_ADVANCE_AFTER_SLEEP"
    - "NO_PLAYER_DECISION_PENDING_AT_SAVE_POINT"
```

---

# 22｜HOT V3.4 結論

```yaml
HOT_V3_4_CONCLUSION:
  state: "VALID_CURRENT_HOT"
  replaces_for_direct_resume: "HOT V3.3"
  preserves_previous_chain: true
  master_updated: false
  character_pool_updated: false
  main_program_updated: false
  experimental_patch_merged: false

  key_new_hard_states:
    - "浮香第一局免費床已由李師師正式認輸；第一局結算完成。"
    - "李師師另開第二局免費床賭約；白御行透過白三娘自願借床、小翠自願把他當『大件行李』帶上樓而再次勝出。"
    - "李師師已正式承認第二局白御行勝。"
    - "紅娘第二局側賭敗北；未來欠一次條件式免費與師師搭局，但尚未執行。"
    - "十三娘豹子賭局合法結果為小翠擲 1-6-6，白御行敗；3-3-1 為誤解污染。"
    - "白御行已向十三娘交付國運／頂級幸運資產路徑；十三娘形成帝皇宴國運賭桌動機。"
    - "帝皇宴新增六條高桌、紅娘、三名單夜競價候選、青禾／白三娘特殊角色、白玉池三日可用性等籌備方向，但多數尚未取得本人確認。"
    - "張麗華已接受以白御行女性伴侶身份出席帝皇宴，取得 100 兩衣裝準備款；貂蟬邀請尚未確認。"
    - "白三娘房內，白御行與白三娘成年人親密成立；小翠保持獨立法位。"
    - "小翠第一次自行選擇進入有限實習，明定只試一點、自己決定停止，並在今晚實際停止。"
    - "小翠學到真實反應、男人面子／焦慮、高價值客戶、保密、聽故事、回頭客等風月接客心理框架。"
    - "向青禾學按摩與沈萬三高端客戶閉門座談均仍為提案。"
    - "本 SAVE 截止時，白御行抱小翠、白三娘抱白御行，三人已安靜入睡。"
```

<!-- PROMOTED_HOT_SOURCE_END: 觀止青樓_白御行線_HOT_SAVE_V3.4_槐月二十六日深夜_第二免費床成立_小翠三娘實習_紅娘側賭輸_三人抱睡版.md -->

<!-- INHERITED_MASTER_V4_3_R1_END -->


<!-- PROMOTED_SOURCE_BEGIN: 觀止青樓_白御行線_HOT_SAVE_V3.5_槐月二十八日無月夜_九幽帝皇聯誼會散場_雙姝天價競拍_帝皇分流_三人閒聊版.md -->
# SOURCE ARCHIVE｜觀止青樓_白御行線_HOT_SAVE_V3.5_槐月二十八日無月夜_九幽帝皇聯誼會散場_雙姝天價競拍_帝皇分流_三人閒聊版.md

**SHA-256：** `e5e9fee2c95661b9a67f46303f6f827ce2963fb5cd183f7a1b470eaeeecc070b`

> **法位：本檔 E93–E98 固化來源。** 原 HOT 內的 CURRENT_SCENE／HOLD 只代表當時快照；不得覆寫本 MASTER 截止或 V4.1–V4.4 疊加層。

# 觀止青樓｜白御行線 HOT SAVE V3.5
## 理火三年槐月二十八日無月夜｜九幽帝皇聯誼會散場 × 雙姝天價競拍 × 白玉池試營運 × 帝皇多線分流 × 白御行師師麗華三人閒聊版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V3_5_HUAI28_MOONLESS_JIUYOU_EMPEROR_ASSOCIATION_AUCTION_SPLIT_LINES_SETTLEMENT"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V3.5"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V11.0-R2"
  character_source: "觀止人物卡池_LCAPG_V2.2_辭歲入觀止動機校正_青禾六條增補_正式版"

  story_time_span:
    start: "HOT V3.4 後"
    current: "理火三年槐月二十八日無月夜／深夜"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AFTER_HOT_SAVE_COMMAND_AT_BAI_SHISHI_LIHUA_TABLE_CHAT_AFTER_EMPEROR_EVENT"

  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V3.4_槐月二十六日深夜_第二免費床成立_小翠三娘實習_紅娘側賭輸_三人抱睡版.md"
  previous_hot_sha256: "38454482b6e0a56a6507c74e1f54a203db22e4f79082aed75e4b535b6396f1fb"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"

  experimental_overlays:
    performance_patch:
      file: "觀止青樓_PATCH_風月角色表演與接戲能力_V0.1-EXP_獨立試跑未併主系統.md"
      status: "INDEPENDENT_TRIAL_OVERLAY_NOT_MERGED"
    analyzer_exit_patch:
      file: "觀止青樓_PATCH_分析器退場_重大升階定義_SCOPED_REACTIVATION_顯影反污染_V0.1-EXP.md"
      status: "GUANZHI_SPECIFIC_OPTIONAL_EXPERIMENTAL_OVERLAY_NOT_MERGED"
    lihuo_environment_patch:
      file: "理火環境_PATCH_V0.1.md"
      status: "REFERENCE_OPTIONAL_EXPERIMENTAL_OVERLAY_NOT_MERGED"

  save_scope:
    - "槐月二十八日九幽帝皇聯誼會於觀止大觀樓之正式前宴與後段自然分流"
    - "六條御息所、李師師、貂蟬、蘇清、疏影、阿麗婭、青禾、小翠、紅娘、辭歲、錦棠等當夜已確認出席／互動狀態"
    - "辭歲與錦棠雙人同台競拍、成交、欠單、分成與十日清算安排"
    - "白玉池只限本夜封場帝皇團之特殊試營運狀態"
    - "帝皇與人物各線只記可觀察事件；進房、關門、熄燈不推導未觀察之成人結果"
    - "李清照以寡居、逃難中之狀態再訪觀止，來找張麗華飲用白御行預付之一萬兩酒資"
    - "白御行、李師師、張麗華於尾聲重新同桌閒聊並下令 HOT SAVE"
```

---

# 0｜提交法位、來源、日曆校正與本輪反污染

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V3.4_槐月二十六日深夜_第二免費床成立_小翠三娘實習_紅娘側賭輸_三人抱睡版.md"
    role: "本檔直接前置 HOT；V3.4 及以前有效硬狀態全部繼承，除本檔明示校正者"

  master_archive:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"
    role: "截至 HOT V2.5 之長期因果；V2.6-V3.4 由 HOT 鏈承接"

  current_route_conversation_commit:
    role: "HOT V3.4 後至本次 HOT SAVE 命令前之直接劇情、玩家明示自身言行、GM 明示設定、NPC 可觀察回應、已成立契約／拒絕／同意／交易／帳務與玩家明示校正"

COMMIT_NOTE:
  - "本檔取代 HOT V3.4，成為白御行線最新直接接關切片；V3.4 保留為前置歷史來源。"
  - "本次只更新 HOT；不更新 MASTER、不修改人物卡池、不修改主程序、不把 EXP PATCH 宣稱為已併正式核心。"
  - "本輪所有『進房』『關門』『熄燈』『同桌』『拍得一夜契約』均只保存已成立之具體事件軸，不推導 blanket consent 或未觀察成人事件。"
  - "玩家對人物配對／可能對味之提示，除非 NPC 已自行形成可觀察行動，不得升格為人物關係事實。"
  - "本輪後段多條人物線受到玩家注意力主動拉動；不回滾已合法成立事件，但下一幕不得把『每位帝皇都必須有女人／必須收線』當成隱性 GOAL。"

CALENDAR_CORRECTION:
  authority: "PLAYER_GM_EXPLICIT_CORRECTION"
  calendar_rule:
    months_per_year: 13
    days_per_month: 28
    day_29_exists: false
    current_date: "理火三年槐月二十八日"
    current_day_note: "槐月最後一日／無月夜"
  superseded_pollution:
    - "舊 HOT 或舊籌備文字中的『槐月二十九日前後』不得再作有效日期。"
  save_effect:
    - "事件順序保留；錯誤二十九日日期標記撤銷。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年槐月二十八日"
  lunar_condition: "無月夜"
  time: "深夜；九幽帝皇聯誼會前宴已結束並完成多線分流；精確時刻未知"
  primary_location: "觀止青樓／大觀樓與相鄰內院各分流空間"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  player:
    name: "白御行"
    current_position: "與李師師、張麗華同桌飲酒閒聊"
    current_state:
      - "本夜大型帝皇宴不再由白御行主持"
      - "已向潘金蓮交代翌日定陶商會先調三百萬兩，餘款最遲十日結清"
      - "正與李師師、張麗華談本夜拍賣與人物線"

  li_shishi:
    current_position: "白御行同桌"
    current_state:
      - "已結束與趙光義之偏廳長談"
      - "曾念李清照詞促使趙光義想見李清照，但未替任何一方作關係決定"
      - "目前與白御行、張麗華飲酒閒聊"

  zhang_lihua:
    current_position: "白御行同桌"
    current_state:
      - "已從李清照與趙光義酒席主動退出，避免成為多餘第三人"
      - "目前與白御行、李師師飲酒閒聊"

  direct_resume_point:
    - "本夜可直接在此收幕。"
    - "下一幕可由翌晨、定陶商會首批三百萬兩到位、帝皇各支線結果自然顯影、雙姝分成入帳、或任一未決人物線重新取得注意力開始。"
    - "不得因本夜已『配到人』就替任何未決支線補成人結果、戀愛、永久關係或完成狀態。"
```

---

# 2｜V3.4 繼承後仍活躍之核心狀態

```yaml
INHERITED_ACTIVE_CORE:
  bai_house_relationships:
    li_shishi:
      route_position:
        - "白御行之如夫人／白夫人"
        - "對白御行四名女性有較高內部調度權"
      anti_merge:
        - "李師師之白夫人法位不得與張麗華之麗華夫人法位混成同一權限。"

    zhang_lihua:
      route_position:
        - "白御行公開女性伴侶／麗華夫人"
        - "四名女性對其有尊重與一般日常協助義務，但重大事項不等同白夫人指揮權"

  white_jade_pool:
    prior_state: "非正式全面復業"
    current_delta: "本夜因九幽帝皇封場團體形成特殊試營運；詳見 WHITEJADE28-E01"

  xiaocui:
    - "仍是學徒／受訓新人；V3.4 的有限成人實習不得寫成已治癒、已成老手或永久接受成人服務。"

  shisanniang:
    - "仍保有十三娘賭局主線與帝皇／國運高價值賭局興趣。"

  dingtao_business:
    - "定陶商會持續作白御行線核心資金、放款、跨地調度與九幽清算接口之一。"
    - "商會資產、白御行私人資產、人物私人財產與九幽公帳不得混成同一所有權。"
```

---

# 3｜EMPEROR28-E01｜九幽帝皇聯誼會前宴正式舉行

```yaml
EMPEROR_EVENT:
  event_id: "EMPEROR28-E01-JIUYOU_ASSOCIATION_GUANZHI_POST_MEETING_EVENT"
  event_axis_state: "COMPLETED"
  location: "觀止青樓／大觀樓"
  nature:
    - "九幽帝皇聯誼會正式會議／家主交接發生於九幽，不在觀止。"
    - "觀止只承接會後 HAPPY TIME／交接宴與娛樂。"
    - "本夜觀止於入夜後對普通陽間客封場。"

  bai_position:
    - "白御行為九幽掛名攝政王。"
    - "白御行是九幽娛樂城發起／設計／股東與審計影響節點之一，但不是日常經營者。"
    - "九幽娛樂城城主為后土娘娘；此一婚姻／城主法位不因本夜觀止活動改變。"

  confirmed_guests:
    - "嬴政"
    - "劉邦"
    - "劉秀"
    - "劉病己"
    - "劉禪"
    - "李世民"
    - "李隆基"
    - "皇太極"
    - "乾隆"
    - "朱棣"
    - "朱正德／豹房小王子"
    - "趙光義"
    - "趙受益"
    - "忽必烈"

  succession_context:
    qin:
      state: "NO_SUCCESSION"
      note: "嬴政以榮譽總會長／見證角色出席"
    former_han:
      from: "劉邦"
      to: "劉病己"
    later_han_liu_line:
      from: "劉秀"
      to: "劉禪"
    tang:
      from: "李世民"
      to: "李隆基"
    ming:
      from: "朱棣"
      to: "朱正德／豹房小王子"
    qing:
      from: "皇太極"
      to: "乾隆"
    song:
      from: "趙光義"
      to: "趙受益"
    golden_family:
      state: "NO_SUCCESSION_THIS_CYCLE"
      note: "忽必烈仍自行出席"

  four_taizongs_present:
    - "唐太宗 李世民"
    - "宋太宗 趙光義"
    - "明太宗／成祖 朱棣"
    - "清太宗 皇太極"
```

---

# 4｜FINANCE28-E01｜本夜公帳、私帳與放款規則

```yaml
EVENT_FINANCE_POLICY:
  event_id: "FINANCE28-E01-GROUP_PUBLIC_ACCOUNT_PRIVATE_IOU_SPLIT"
  event_axis_state: "COMPLETED"

  public_group_spending:
    payer: "九幽娛樂城／帝皇聯誼會公帳"
    applies_to:
      - "觀止本夜集體娛樂"
      - "白玉池本夜封場團體之最高級 SPA／水療套餐"
    note:
      - "公帳可報銷不等於任何帝皇家族／朝代／私人資產自動轉為公產。"

  private_spending:
    currency: "陽間銀兩／可轉算之欠單"
    lender: "定陶商會"
    mechanism:
      - "需要私人高額消費者可即時立欠單。"
      - "後續可由九幽合法資產／清算渠道處理。"
    player_public_message:
      - "放心花、努力花。"
      - "私人需要多少，白御行表示定陶商會敢放款。"

  pan_preparation:
    confirmed:
      - "潘金蓮已備定陶商會欠單、筆墨與高額私人消費結算工具。"
```

---

# 5｜WHITEJADE28-E01｜白玉池本夜特殊試營運

```yaml
WHITE_JADE_POOL_TRIAL:
  event_id: "WHITEJADE28-E01-EMPEROR_GROUP_SPECIAL_TRIAL"
  event_axis_state: "CONTINUING"
  operating_state: "SPECIAL_ONE_NIGHT_TRIAL_NOT_FORMAL_REOPENING"

  a_ling_control:
    - "阿泠仍保有池區使用規則與控制權。"
    - "不得一次把所有人強塞進池。"
    - "不得用阿泠名義公開招攬。"
    - "本夜只對封場之九幽帝皇／股東團體開放。"

  top_spa_package:
    - "冷熱池"
    - "香浴"
    - "熱巾"
    - "飲食酒水"
    - "按摩／身體放鬆"
    - "肩頸背腰水療"
    - "泡後休息"

  consent_boundary:
    - "池區使用權 != 取得任何女子陪伴權。"
    - "女子陪同、按摩、私人服務或後續成人互動均須另由人物本人決定。"

  observed_guest_response:
    zhu_zhengde:
      - "拍得辭歲後先選擇前往白玉池。"
      - "實際見識水療設施後承認豹房沒有相同體驗／技術組合。"
      - "曾詢問能否把相關設施搬去豹房，未取得阿泠同意。"
    zhu_di:
      - "跟往白玉池，包含觀察／看管朱正德之成分。"
    huang_taiji:
      - "對白玉池之筋骨放鬆、水療等內容產生實際興趣。"
```

---

# 6｜FRONT28-E01｜前宴人物層與主要節目

```yaml
FRONT_HALL_EVENT_LAYER:
  event_id: "FRONT28-E01-LAYERED_ENTERTAINMENT"
  event_axis_state: "COMPLETED"

  zhang_lihua:
    role: "白御行高位女性伴侶／麗華夫人"
    observed:
      - "公開揭示張麗華為南陳舊人、現為白御行的人／女性伴侶。"
      - "未以服務女子身份參加本夜。"

  li_shishi:
    role: "正式高位席／白夫人"
    consent_and_conditions:
      - "同意正式出席。"
      - "要求正式服裝、獨立高位桌、不與服務女子混席、不坐白御行身旁。"
    observed:
      - "與趙光義長時間談汴梁、音樂與人物。"
      - "其後白御行公開揭示其為李師師，亦為白御行如夫人。"

  liutiao_miyasudokoro:
    role: "女客／高位日本貴族人物"
    consent_and_conditions:
      - "只以女客出席，不作服務女子。"
      - "因趙受益在場而願意赴席。"
    seat: "趙受益旁"

  diaochan:
    invitation_source: "張麗華"
    consent_process:
      - "確認自己不是被叫去給某個男人看。"
      - "確認不是四大美人式並稱展示。"
      - "確認白御行對她沒有直接命令權。"
      - "最後自行決定提早到場；曾回覆『知道了，別再催。』"
    observed:
      - "獨自入場並先找張麗華。"
      - "完成一段舞。"
      - "舞後自行選擇坐到劉秀旁，主要以與陰麗華之朋友關係進行安全玩笑。"
      - "未與劉秀形成戀愛、外遇或成人服務。"

  su_qing:
    role: "天下局／代價計算"
    observed:
      - "以人口、糧食、軍隊、國庫、地方勢力、邊患、稅負等限制讓帝皇計算治理代價。"
      - "李世民先入局，朱棣表示想接。"
      - "核心句義為『不是算錢，是算代價』。"

  shuying:
    role: "遠距秘密肖像畫家"
    observed:
      - "在竹簾後遠距畫乾隆未察覺被觀察之側影。"
      - "作品完成後由阿麗婭代為送給乾隆。"

  aliyah_delivery:
    observed:
      - "只負責把疏影作品交給乾隆。"
      - "明確區分『畫是畫，人是人』。"
      - "未因送畫取得陪房、拍賣或其他義務。"

  music_layer:
    hongxiu:
      - "只以琴樂／賣藝出席，不自動進入服務線。"
    fuxiang:
      - "以琴樂加入音樂層；未因彈琴自動形成服務義務。"

  newcomer_service_layer:
    scope:
      - "由已接受相應訓練且本人同意之新人提供酒食、近席、輕度調情與事先同意範圍內接觸。"
      - "上樓、更多私人互動或成人服務須另行協商。"
```

---

# 7｜AUCTION28-E00｜雙人競拍參與資格與錦棠定名

```yaml
AUCTION_ELIGIBILITY:
  event_id: "AUCTION28-E00-TWO_WOMEN_CONSENT_AND_NAMING"
  event_axis_state: "COMPLETED"

  original_three_candidates:
    - "阿麗婭"
    - "十八歲／六百兩候選"
    - "辭歲"

  aliyah:
    decision: "REFUSED_AUCTION"
    reason:
      - "不願與另外兩名女子放在同一場公開比價。"
      - "傾向自己先看男人、自己選擇。"
    note:
      - "她對乾隆或其他客人有沒有興趣須由後續本人行動判定；拒拍不得被改寫成待攻略。"

  cisu:
    decision: "ACCEPTED_ONE_NIGHT_PUBLIC_AUCTION"
    status: "自由身"
    clothing:
      - "使用其標誌性一片裙／薄紗路線；未要求堆疊珠寶。"

  jintang:
    official_name: "周玉娘"
    self_chosen_stage_name: "錦棠"
    age: 18
    prior_acquisition_context:
      total_price: 600
      broker_share: 550
      direct_to_her: 50
    established_future_share: "15%"
    decision: "ACCEPTED_ONE_NIGHT_PUBLIC_AUCTION"
    confirmed_before_auction:
      - "本夜只是一夜契約，不是二十八日長約。"
      - "原先一成五個人分成仍有效。"
    clothing:
      - "上身使用定陶肚兜原型。"
      - "下身使用川雲染布裙，兼具女裝企畫樣衣／產品顯影功能。"
    naming_statement:
      - "玉娘是家裡／官籍叫法；希望客人記住自己選的名字。"
      - "『錦值錢，棠好看。』"
```

---

# 8｜AUCTION28-E01｜雙人同台問答與正式競拍規則

```yaml
TWO_WOMAN_AUCTION:
  event_id: "AUCTION28-E01-TWO_LANE_QA_AND_AUCTION"
  event_axis_state: "COMPLETED"
  structure:
    - "辭歲與錦棠同時站台。"
    - "競價為兩條獨立同時進行之價線。"
    - "每次出價須明確喊女子名字與金額。"
    - "成交只取得事先同意的一夜契約，不是永久買斷或無限支配。"
    - "契約外新增行為仍需另行協商；具體拒絕持續有效。"

  pre_bid_qa:
    qianlong_reason_for_joining:
      cisu: "認為如此多有錢有權男人在場，不讓他們互相抬價可惜。"
      jintang: "想知道自己站在這裡、不靠牙人與舊契約時到底值多少。"

    li_longji_value_question:
      cisu: "會先看男人真正需要的是崇拜、畏懼、沉默，或證明自己能被記住。"
      jintang: "承認自己經驗較少；記性好，不懂就問，不裝懂。"

    liu_bang_drinking_question:
      cisu: "能喝。"
      jintang: "普通。"

    ying_zheng_dislike_high_bidder_question:
      cisu: "既同意拍賣規則，會履行一夜契約，但不會假裝喜歡。"
      jintang: "同樣履約；若不喜歡，只給已約定內容，不會多給。"

    zhu_zhengde_leopard_house_question:
      cisu: "沒去過豹房，不會假裝能保證勝過豹房。"
      jintang: "不知道；但若能贏走他的錢，他就會記得她。"

    huang_taiji_disliked_men_question:
      cisu: "討厭小氣卻裝大方、輸不起的男人。"
      jintang: "討厭一直提醒她自己付過多少錢的男人；今晚的價格不是她一輩子的債。"

    liu_bingyi_bad_price_question:
      cisu: "若價格不滿意，明天想辦法讓自己下次更貴。"
      jintang: "至少會知道自己還能往上走多少。"

  invalidated_prior_single_auction:
    status: "ROLLED_BACK_BY_PLAYER_CORRECTION"
    effect:
      - "導演誤開之單女價線與其中所有出價全部無效。"
      - "正式有效競拍只認本節雙人同台兩條價線。"
```

---

# 9｜AUCTION28-E02｜雙姝最終成交

```yaml
AUCTION_FINAL_RESULT:
  event_id: "AUCTION28-E02-FINAL_SALES"
  event_axis_state: "COMPLETED"

  cisu:
    winner: "朱正德"
    final_price_taels: 12000000
    contract_nature: "ONE_NIGHT_CONTRACT"
    ownership_transfer: false
    personal_status: "FREE_PERSON"
    distribution:
      guanzhi_rate: "10%"
      guanzhi_receivable_taels: 1200000
      cisu_rate: "90%"
      cisu_receivable_taels: 10800000
    immediate_post_auction:
      - "朱正德與辭歲先前往白玉池。"
      - "後續私人房間／成人履行狀態未觀察，不得補完。"

  jintang:
    winner: "乾隆"
    final_price_taels: 5000000
    contract_nature: "ONE_NIGHT_CONTRACT"
    ownership_transfer: false
    distribution:
      dingtao_rate: "75%"
      dingtao_receivable_taels: 3750000
      guanzhi_rate: "10%"
      guanzhi_receivable_taels: 500000
      jintang_rate: "15%"
      jintang_receivable_taels: 750000
    immediate_post_auction:
      - "錦棠優先確認自己一成五分成是否真實成立。"
      - "乾隆允許她先去確認帳務，未以成交價要求她立即進房。"
      - "後續一夜契約如何履行目前未固化。"

  totals:
    gross_contract_value_taels: 17000000
    guanzhi_total_receivable_taels: 1700000
```

---

# 10｜ACCOUNT28-E01｜欠單、首批三百萬與十日結清

```yaml
AUCTION_ACCOUNTING_SETTLEMENT:
  event_id: "ACCOUNT28-E01-AUCTION_IOU_AND_TEN_DAY_SETTLEMENT"
  event_axis_state: "CONTINUING"

  signed_private_obligations:
    qianlong:
      related_contract: "錦棠一夜契約"
      amount_taels: 5000000
      status: "SIGNED_PAYMENT_OBLIGATION_ACTIVE"
    zhu_zhengde:
      related_contract: "辭歲一夜契約"
      amount_taels: 12000000
      status: "SIGNED_PAYMENT_OBLIGATION_ACTIVE"

  accounting_state:
    gross_contract_value_taels: 17000000
    cash_fully_received: false
    receivables_established: true
    distribution_claims_established: true

  player_instruction_to_pan:
    next_day_cash_taels: 3000000
    remaining_to_schedule_taels: 14000000
    final_deadline: "最遲十日內全部結清"
    reason:
      - "跨地資金調度、轉帳與九幽清算需要時間。"

  anti_false_cash_recognition:
    - "成交額 != 已收現銀。"
    - "辭歲 10,800,000 兩目前為應收分成，不得寫成已全數現銀落袋。"
    - "錦棠 750,000 兩目前為應收分成，不得寫成已全數現銀落袋。"
    - "觀止 1,700,000 兩目前為應收抽成，不得寫成已全數現銀入庫。"

  cisu_future_capital_idea:
    state: "PROPOSAL_ONLY_NOT_ACCEPTED_BY_CISU"
    discussed:
      - "辭歲日後可考慮只留部分可動用資金，把數百萬或更多資金交由定陶商會周轉並收息。"
      - "若日後成立，財產所有權仍屬辭歲，商會對其形成本金／利息債務。"
    forbidden_to_save_as_fact:
      - "辭歲已存入定陶商會"
      - "辭歲已把大部分錢借給白御行"
      - "辭歲的錢等同白御行的錢"
```

---

# 11｜LIUTIAO-ZHAO28-E01｜六條與趙受益互認在意

```yaml
RELATION_EVENT:
  event_id: "LIUTIAO-ZHAO28-E01-MUTUAL_ACKNOWLEDGEMENT"
  event_axis_state: "COMPLETED"

  player_question_to_liutiao:
    question: "趙受益這個男人在妳心裡有沒有？"
    liutiao_answer:
      confirmed: "有"
      limits:
        - "不知道是否已是男女之情。"
        - "會注意趙受益有沒有來。"
        - "若趙受益突然不再出現，她會想問。"
        - "目前不知道這個『有』究竟有多少。"

  player_question_to_zhao_shouyi:
    question: "你在不在乎六條？"
    zhao_answer:
      confirmed: "在乎"
      limits:
        - "替六條付錢不代表六條屬於自己。"
        - "六條今晚坐在旁邊，不代表以後必須一直坐這裡。"
        - "若六條真的離開，他會在意她去了哪裡。"

  mutual_conclusion:
    - "慢慢看。"
    - "六條要求若趙受益日後突然不來，最好先說。"
    - "趙受益答應。"

  relationship_state:
    actual_preference: "EMERGING_MUTUAL_IMPORTANCE"
    explicit_romantic_commitment: "NONE"
    ownership_claim: "NONE"
    exclusivity: "NONE"
```

---

# 12｜LIUTIAO-ZHAO28-E02｜回六條房間聊天

```yaml
PRIVATE_ROOM_EVENT:
  event_id: "LIUTIAO-ZHAO28-E02-PRIVATE_ROOM_TALK"
  event_axis_state: "CONTINUING"

  initiation:
    - "白御行因外場吵鬧提出兩人可回六條房內安靜聊天。"
    - "六條自行詢問趙受益是否願意。"
    - "趙受益表示若六條只是嫌吵，他願意陪她回房坐一會。"

  liutiao_explicit_scope:
    - "回房只是聊天。"

  zhao_acceptance:
    - "接受上述範圍。"

  observed:
    - "兩人一起離開大觀樓。"
    - "進入六條房間。"
    - "房門關閉。"
    - "外部其後觀察到燭光熄滅。"

  unknown:
    - "關門後具體談話內容"
    - "熄燈原因"
    - "是否發生任何額外親密或成人事件"

  anti_inference:
    - "關門 != 性行為"
    - "熄燈 != 性行為"
    - "互認在乎 != 已交往／定情"
```

---

# 13｜HUANGTAIJI-SUQING28-E01｜皇太極與蘇清進私人房

```yaml
PRIVATE_ROOM_EVENT:
  event_id: "HUANGTAIJI-SUQING28-E01-PRIVATE_ROOM_CONTINUATION"
  event_axis_state: "CONTINUING"

  public_dialogue_result:
    - "皇太極直接承認對蘇清有男女方向興趣。"
    - "蘇清指出不接受以『談天下』偽裝其他意圖。"
    - "皇太極表示談話興趣與男女興趣兩者皆有。"

  su_qing_decision:
    confirmed: "同意與皇太極進房"
    explicit_scope:
      - "先聊天。"
      - "門關不關，由蘇清決定。"
      - "燈吹不吹，由蘇清決定。"
      - "後面是否有其他行為，到時再說。"

  huang_taiji_response:
    - "接受上述條件。"

  observed:
    - "兩人一同往私人房間。"

  unknown:
    - "房內後續談話內容"
    - "是否形成其他親密事件"
    - "是否形成成人事件"

  anti_inference:
    - "進房只代表私人空間資格成立；不得寫成成人事件已完成。"
```

---

# 14｜QIANLONG-SHUYING28-E01｜乾隆與疏影談畫

```yaml
ART_RELATION_EVENT:
  event_id: "QIANLONG-SHUYING28-E01-PORTRAIT_AND_ONE_SEAL"
  event_axis_state: "CONTINUING"

  portrait:
    artist: "疏影"
    subject: "乾隆"
    method:
      - "疏影在乾隆未察覺時從遠處竹簾後作畫。"
      - "畫面取乾隆側身、持酒、視線落在別桌之自然瞬間。"
    delivery:
      courier: "阿麗婭"
      price: "GIFT_NOT_SOLD"

  later_conversation:
    initiator: "乾隆自行拿畫去找疏影"
    key_points:
      - "疏影表示選擇該瞬間，是因乾隆當時沒有在『擺給別人看』。"
      - "疏影不接受制式御用畫師式擺拍。"
      - "乾隆欲在畫上用印。"
      - "疏影反對大量蓋印。"
      - "疏影最後允許最多一枚印。"
      - "兩人開始討論印章位置。"

  relation_state:
    current: "ARTIST_COLLECTOR_INTERESTED_CONVERSATION"
    private_room: false
    sexual_service: false
    romantic_commitment: "NONE"
```

---

# 15｜YINGZHENG-QINGHE28-E01｜嬴政與青禾按摩線

```yaml
BODYWORK_EVENT:
  event_id: "YINGZHENG-QINGHE28-E01-SHOULDER_BODYWORK"
  event_axis_state: "CONTINUING"

  initiation:
    - "白御行建議讓青禾替嬴政鬆肩背。"
    - "潘金蓮先詢問青禾本人。"
    - "青禾確認只按／依自己接到的範圍，並自行同意前往。"

  observed:
    - "青禾注意到嬴政左右肩高低與頸部轉動不均。"
    - "嬴政接受肩背按摩。"
    - "嬴政要求可再重一些。"
    - "嬴政逐漸由筆直戒備轉為較放鬆姿勢。"
    - "雙方有自然談話。"

  scope:
    - "按摩／身體放鬆。"
    - "未成立陪房或成人服務。"
```

---

# 16｜LIUCHAN-XIAOCUI28-E01｜劉禪與小翠自發同席

```yaml
LOW_PRESSURE_SOCIAL_EVENT:
  event_id: "LIUCHAN-XIAOCUI28-E01-CAKE_AND_CHAT"
  event_axis_state: "CONTINUING"

  observed:
    - "劉禪沒有主動投入高強度風月線。"
    - "小翠收拾席面時再次與劉禪接觸。"
    - "劉禪把最後一塊甜糕讓給小翠。"
    - "小翠明示自己之前吃過，仍自行接受最後一塊。"
    - "小翠自行坐下與劉禪聊天。"
    - "兩人談到公帳能否買糕等輕鬆話題。"

  structural_note:
    - "此線對小翠之價值目前只在低壓、自發、非教學式的人際相處。"

  forbidden_inference:
    - "不得寫成已成一對。"
    - "不得寫成戀愛。"
    - "不得寫成小翠已完成任何心理／成人能力『治療』。"
    - "不得因劉禪溫和便預設其永久適合小翠。"
```

---

# 17｜KUBLAI-ALIYAH28-E01｜忽必烈與阿麗婭草原／西域對話

```yaml
CROSS_CULTURAL_SOCIAL_EVENT:
  event_id: "KUBLAI-ALIYAH28-E01-GRASSLAND_CENTRAL_ASIA_CHAT"
  event_axis_state: "CONTINUING"

  invitation:
    - "白御行指出忽必烈與阿麗婭在草原、西域、中亞、商路與多民族世界上可能有共同話題。"
    - "阿麗婭自行看過忽必烈後決定去聊。"

  opening_joke:
    - "阿麗婭以『聽說你姓劉？』切入。"
    - "忽必烈自稱劉氏之笑話仍只屬本夜自我宣稱／家譜玩笑；劉家人物不承認。"

  conversation_topics:
    - "蒙古帝國向西之範圍"
    - "西域與中亞商人"
    - "多民族治理"
    - "驛傳／消息運送"
    - "不同文化人在漢地之規矩與生活"

  relation_state:
    current: "VOLUNTARY_INTERESTED_CONVERSATION"
    auction: false
    private_room: false
    sexual_service: false
```

---

# 18｜LI-SHIMIN-PAN28-E01｜李世民與潘金蓮互相注意

```yaml
SOCIAL_RELATION_EVENT:
  event_id: "LI-SHIMIN-PAN28-E01-ACCOUNTING_VALUE_CONVERSATION"
  event_axis_state: "CONTINUING"

  observed:
    - "李世民本夜未因其他帝皇皆有女人線就強迫自己尋找私人陪伴。"
    - "潘金蓮與李世民談到帳、花錢是否值得、資源換回什麼、競價與回報。"
    - "李世民說明自己競拍錦棠到一百萬後退出，並非出不起，而是有人比自己更想要；無必要為證明有錢繼續出價。"
    - "潘金蓮明示喜歡／認同這個判斷。"

  relation_state:
    current: "MUTUAL_ATTENTION_AND_CONVERSATIONAL_INTEREST"
    private_room: false
    romance: "NOT_ESTABLISHED"
    sexual_service: false

  anti_pairing_lock:
    - "此線可以停在聊天／注意；不得因『對味』直接推成潘金蓮已選李世民。"
```

---

# 19｜LI-LONGJI-HONGNIANG28-E01｜李隆基與紅娘喝酒互拆

```yaml
SOCIAL_RELATION_EVENT:
  event_id: "LI-LONGJI-HONGNIANG28-E01-DRINK_AND_READ_EACH_OTHER"
  event_axis_state: "CONTINUING"

  initiation:
    - "白御行叫紅娘過來與李隆基接戲。"
    - "紅娘自行留下看李隆基值不值得聊。"

  observed:
    - "紅娘指出李隆基本夜不是單純想要某一個女人，而是受不了自己一路看懂風月卻多次『差一點』。"
    - "李隆基反過來試著讀紅娘，兩人形成互相拆招。"
    - "李隆基問紅娘是否願意陪他喝酒。"
    - "紅娘明確答應喝酒；更多則『再看』。"
    - "紅娘要求不要用楊貴妃或開元盛世來證明自己懂女人／證明自己。"

  relation_state:
    current: "VOLUNTARY_DRINKING_AND_MUTUAL_READING"
    private_room: false
    additional_intimacy: "NOT_YET_DETERMINED"
```

---

# 20｜LIUBANG28-E01｜劉邦熱鬧陪席線

```yaml
GROUP_SOCIAL_EVENT:
  event_id: "LIUBANG28-E01-ROWdy_GROUP_COMPANY"
  event_axis_state: "CONTINUING"

  observed_preference:
    - "劉邦本夜對多人熱鬧、喝酒、近席與量感明顯比單一高位才女配對更有興趣。"

  operating_scope:
    - "觀止可由多名各自願意參與之女子形成熱鬧酒局。"
    - "任何近席／調情／接觸只在每名女子事先同意範圍內。"
    - "是否有人後續願意上樓，須逐人另議。"

  anti_inference:
    - "『給十個女人』屬白御行對其偏好之戲謔／營運方向，不等於十名女子已被強制安排成人服務。"
```

---

# 21｜ZHAO-GUANGYI-SHISHI28-E01｜趙光義與李師師長談

```yaml
SOCIAL_RELATION_EVENT:
  event_id: "ZHAO-GUANGYI-SHISHI28-E01-LONG_TEA_CONVERSATION"
  event_axis_state: "COMPLETED"

  observed:
    - "趙光義長時間留在李師師正式席，談汴梁、音樂、人物與趙光義本人。"
    - "趙光義曾提出希望換更安靜空間。"
    - "李師師拒絕進私人房，但同意至偏廳再飲一壺茶。"
    - "兩人在偏廳繼續長談。"

  relation_state:
    current: "SUBSTANTIAL_CONVERSATIONAL_INTEREST"
    private_room: false
    sexual_service: false
    ownership_or_exclusivity: "NONE"

  completion_reason:
    - "後續李清照到場；李師師念詞後，趙光義自行決定去見李清照。"
```

---

# 22｜LIQINGZHAO28-E01｜李清照逃難中再訪觀止

```yaml
REVISIT_EVENT:
  event_id: "LIQINGZHAO28-E01-WIDOW_FLIGHT_FREE_WINE_REVISIT"
  event_axis_state: "CONTINUING"

  gm_confirmed_current_state:
    marital_state: "寡婦"
    life_state: "正在逃難過程"
    permanent_guanzhi_resident: false

  visit_reason:
    - "來找張麗華喝酒。"
    - "不是來接客。"
    - "不是為趙光義或任何帝皇而來。"

  wine_account:
    payer: "白御行"
    prepaid_limit_taels: 10000
    nature: "李清照在觀止可使用之免費酒資／由白御行墊付"

  observed:
    - "李清照帶有逃難行裝與路塵。"
    - "先與張麗華坐下飲酒。"
    - "知道本夜觀止有歷代帝皇後，並未因此主動尋找皇帝。"
```

---

# 23｜ZHAO-GUANGYI-LIQINGZHAO28-E01｜李師師念詞後趙光義轉桌

```yaml
SOCIAL_RELATION_EVENT:
  event_id: "ZHAO-GUANGYI-LIQINGZHAO28-E01-POEM_TRIGGERED_MEETING"
  event_axis_state: "CONTINUING"

  trigger:
    - "李師師向趙光義念李清照作品片段。"
    - "趙光義由原本對『後世大宋』的抽象好奇，轉為想見寫出這些詞的李清照本人。"

  li_shishi_boundary:
    - "李師師不阻止趙光義離席。"
    - "提醒趙光義：李清照本夜是來喝酒，不是來替宋代祖宗做國事奏對。"

  zhao_choice:
    - "趙光義自行決定離開偏廳去見李清照。"
    - "未要求白御行或李師師替李清照同意。"

  li_qingzhao_response:
    - "允許趙光義坐下。"
    - "趙光義承認原本想問後世大宋，但因她今晚只是來喝酒而先不問。"
    - "李清照把酒推給他，先以喝酒開始。"

  zhang_lihua_exit:
    - "白御行以眼色暗示張麗華可退出。"
    - "張麗華自行判斷桌內不缺第三人，主動離席。"

  current_state:
    - "趙光義與李清照單獨留桌喝酒／談話。"

  unknown:
    - "後續談話是否進入宋史、逃難、人生、文學或其他題目。"
    - "是否形成更深私人關係。"

  anti_inference:
    - "李清照不是被召來配趙光義。"
    - "趙光義轉桌不代表已選擇李清照取代李師師。"
    - "李師師不吃醋／不阻止不等於她對趙光義已有承諾。"
```

---

# 24｜DIACHAN-LIUXIU28-E01｜貂蟬與劉秀安全玩笑線

```yaml
SOCIAL_EVENT:
  event_id: "DIACHAN-LIUXIU28-E01-YINLIHUA_FRIEND_TEASING"
  event_axis_state: "COMPLETED"

  observed:
    - "貂蟬舞後自行選擇坐劉秀旁。"
    - "因貂蟬與陰麗華為女性好友，此座位形成劉秀『朋友妻不可戲』式自保笑料。"
    - "貂蟬曾說會告訴陰麗華劉秀看舞很仔細、覺得錦棠漂亮等玩笑。"
    - "劉秀沒有競拍、沒有對貂蟬形成成人行動。"

  relation_state:
    affair: false
    romantic_event: false
    main_effect: "COMEDIC_SOCIAL_PRESSURE_ONLY"
```

---

# 25｜SHISANNIANG-LIUBINGYI28-E01｜十三娘與劉病己賭桌

```yaml
GAMBLING_EVENT:
  event_id: "SHISANNIANG-LIUBINGYI28-E01-GAMBLER_VS_GAMBLER"
  event_axis_state: "CONTINUING"

  observed:
    - "雙姝競拍結束後，十三娘賭桌重新開局。"
    - "劉病己主動入桌。"
    - "劉病己先檢查骰子並確認可使用普通骰。"
    - "十三娘接受其檢查，不因對手是帝皇改變賭桌主場位置。"

  relation_state:
    current: "SERIOUS_GAMBLING_OPPONENTS"
    result: "NOT_YET_DETERMINED"
```

---

# 26｜BAI-SHISHI-LIHUA28-E01｜三人尾聲閒聊

```yaml
HOUSEHOLD_SOCIAL_EVENT:
  event_id: "BAI-SHISHI-LIHUA28-E01-POST_EVENT_DRINK_AND_CHAT"
  event_axis_state: "CONTINUING"

  participants:
    - "白御行"
    - "李師師"
    - "張麗華"

  observed:
    - "張麗華從李清照／趙光義桌退出後回到白御行與李師師身旁。"
    - "三人本夜第一次在大型帝皇接待與多線分流後真正坐下來飲酒聊天。"
    - "談及趙家兩線、唐家兩線、誰最丟臉、今晚天價競拍與女人財務位置。"
    - "李師師明確把張麗華也稱作『自己人』語境內的一員；不等於權限合併。"

  last_confirmed_topic:
    - "白御行表示自己今晚最喜歡的是拍出天價的出閣／一夜契約費與其財務後果。"
    - "三人進一步談辭歲與錦棠因分成取得未來議價能力。"

  current_scene_end:
    - "白御行下令 HOT SAVE，並以快樂結束本夜。"
```

---

# 27｜人物與關係增量

```yaml
RELATION_DELTAS:
  liutiao_zhao_shouyi:
    prior: "自願同席／趙受益曾替六條墊付生活與房茶費；關係未定義"
    current:
      - "六條明示心裡『有』趙受益，但未定義是否男女之情。"
      - "趙受益明示在乎六條。"
      - "雙方同意慢慢看。"
      - "共同進六條房聊天；房內後續未知。"

  huang_taiji_su_qing:
    prior: "天下局／代價計算產生注意"
    current:
      - "皇太極明示男女興趣。"
      - "蘇清自行同意先進房聊天並保留全部後續決定權。"
      - "房內後續未知。"

  qianlong_shuying:
    prior: "疏影秘密作畫／乾隆不知畫師"
    current:
      - "乾隆已知道疏影為畫師並主動找她談畫。"
      - "疏影只允許作品最多加一枚乾隆印。"

  liu_chan_xiaocui:
    prior: "無固定私人關係"
    current:
      - "形成低壓、自發同席吃糕與聊天入口。"
      - "是否再發展未知。"

  kublai_aliyah:
    prior: "無固定私人關係"
    current:
      - "因草原／西域／中亞經驗形成自願對話。"
      - "是否再發展未知。"

  li_shimin_pan:
    prior: "宴會主客／掌櫃"
    current:
      - "形成對帳務、價值與資源判斷的互相注意。"
      - "未建立私人承諾或成人關係。"

  li_longji_hongniang:
    prior: "無固定私人關係"
    current:
      - "紅娘自行同意陪李隆基喝酒並互相拆招。"
      - "更多互動未定。"

  zhao_guangyi_li_shishi:
    prior: "宴席初識"
    current:
      - "已形成數壺茶與偏廳長談之實質談話興趣。"
      - "該場談話因趙光義自行去見李清照而結束。"

  zhao_guangyi_li_qingzhao:
    prior: "本夜前無本線私人事件"
    current:
      - "趙光義因聽詞後自行想見本人。"
      - "李清照允許同桌喝酒。"
      - "目前只有談話入口，不定義感情。"
```

---

# 28｜帳務、契約與財產硬狀態

```yaml
PRIVATE_CONTRACT_AND_LEDGER:
  cisu_one_night_contract:
    status: "ACTIVE_PAYMENT_OBLIGATION_AND_FULFILLMENT_NOT_YET_FULLY_OBSERVED"
    customer: "朱正德"
    gross_taels: 12000000
    cisu_share_taels: 10800000
    guanzhi_share_taels: 1200000
    ownership_transfer: false
    additional_services: "SEPARATE_NEGOTIATION_REQUIRED"

  jintang_one_night_contract:
    status: "ACTIVE_PAYMENT_OBLIGATION_AND_FULFILLMENT_NOT_YET_FULLY_OBSERVED"
    customer: "乾隆"
    gross_taels: 5000000
    dingtao_share_taels: 3750000
    jintang_share_taels: 750000
    guanzhi_share_taels: 500000
    ownership_transfer: false
    additional_services: "SEPARATE_NEGOTIATION_REQUIRED"

  dingtao_settlement_plan:
    status: "ACTIVE"
    day_1_cash_taels: 3000000
    total_remaining_after_day_1_target_taels: 14000000
    full_clear_deadline: "WITHIN_TEN_DAYS"

  li_qingzhao_wine_credit:
    payer: "白御行"
    limit_taels: 10000
    current_use: "ACTIVE_FREE_WINE_ACCOUNT_FOR_LI_QINGZHAO"

  cisu_possible_deposit:
    status: "NOT_FORMED"
    note: "只曾討論未來可將部分巨款交定陶商會周轉收息；尚未取得辭歲本人同意。"
```

---

# 29｜知情範圍與來源

```yaml
KNOWLEDGE_SCOPE:
  public_or_broadly_witnessed:
    - "雙姝競拍最終成交價與得標者。"
    - "乾隆、朱正德簽立高額私人欠單。"
    - "白御行公開區分公帳集體娛樂與私帳消費。"
    - "張麗華、李師師於本夜之高位身份。"
    - "六條御息所以女客身份與趙受益同席。"
    - "貂蟬舞與其後坐劉秀旁之公開事件。"

  limited_witnesses:
    liutiao_zhao_room:
      knows:
        - "白御行"
        - "張麗華（至少看到／聽聞關門熄燈笑料）"
        - "相關近場人物可能知道兩人離席"
      does_not_know:
        - "任何人均無合法來源知道房內後續細節，除非當事人之後自行透露。"

    huang_taiji_suqing_room:
      knows:
        - "近場人物知道兩人一同往私人房。"
      does_not_know:
        - "房內實際發生內容。"

    zhao_guangyi_liqingzhao:
      knows:
        - "張麗華"
        - "白御行"
        - "李師師"
        - "近場可見兩人同桌者"
      does_not_know:
        - "後續私下談話全部內容。"

  accounting_private:
    full_distribution_known_by:
      - "白御行"
      - "潘金蓮"
      - "相關帳房／春梅等依職務需要者"
      - "各自當事女子對自身分成知情"
    note:
      - "其他賓客知道成交價不等於知道定陶商會、觀止與女子之完整分成結構。"
```

---

# 30｜仍活躍但未解事項

```yaml
OPEN_THREADS:
  high_priority:
    - id: "ACCOUNT28-OPEN-01"
      state: "ACTIVE"
      item: "次日定陶商會首批三百萬兩是否如期到位；後續一千四百萬如何在十日內完成清算。"

    - id: "CISU28-OPEN-01"
      state: "NOT_YET_DETERMINED"
      item: "辭歲 10,800,000 兩分成實際收款、保管、置產、投資或是否存入定陶商會。"

    - id: "JINTANG28-OPEN-01"
      state: "NOT_YET_DETERMINED"
      item: "錦棠 750,000 兩分成實際入帳後如何使用；其職業與自主選擇如何變化。"

    - id: "LIUTIAO-ZHAO28-OPEN-01"
      state: "CONTINUING"
      item: "六條與趙受益房內聊天及翌晨狀態；不得偷填成人結果。"

    - id: "HUANGTAIJI-SUQING28-OPEN-01"
      state: "CONTINUING"
      item: "皇太極與蘇清房內後續；只有進房與先聊天資格已成立。"

    - id: "QIANLONG-JINTANG28-OPEN-01"
      state: "NOT_YET_DETERMINED"
      item: "乾隆與錦棠一夜契約具體履行範圍。"

    - id: "ZHENGDE-CISU28-OPEN-01"
      state: "NOT_YET_DETERMINED"
      item: "朱正德與辭歲自白玉池後的一夜契約具體履行範圍。"

    - id: "SHISANNIANG-LIUBINGYI28-OPEN-01"
      state: "CONTINUING"
      item: "十三娘與劉病己賭局勝負。"

    - id: "ZHAO-LIQINGZHAO28-OPEN-01"
      state: "CONTINUING"
      item: "趙光義與李清照酒席談話走向。"

  medium_priority:
    - "乾隆與疏影是否繼續談畫、唯一一枚印最終落點。"
    - "李世民與潘金蓮是否只停在帳務／價值談話。"
    - "李隆基與紅娘喝酒後是否還有其他自願互動。"
    - "忽必烈與阿麗婭是否繼續草原／西域對話。"
    - "劉禪與小翠是否在翌日仍自然相處。"
    - "嬴政與青禾按摩線何時自然結束。"
    - "白玉池本夜試營運結束後是否恢復關閉，以及阿泠如何評價此次試跑。"

  low_priority_or_closed_for_now:
    - "劉秀與貂蟬本夜只保存安全玩笑，不需強行生成後續。"
    - "朱棣若未形成私人女人線，可合法保持無結果。"
```

---

# 31｜禁止回歸／防污染

```yaml
ANTI_REGRESSION:
  calendar:
    - "不得再出現槐月二十九日。"
    - "觀止曆每月二十八日封頂；槐月二十八日為本月最後一日。"

  auction:
    - "不得恢復已被玩家撤銷之錯誤單女競拍與無效出價。"
    - "辭歲正式成交為朱正德 12,000,000 兩。"
    - "錦棠正式成交為乾隆 5,000,000 兩。"
    - "阿麗婭明確拒絕加入同場拍賣。"

  money:
    - "17,000,000 兩是成交／應收，不是已全數實收。"
    - "辭歲可能把巨款存定陶商會收息仍是提案，不能偷寫成已存。"
    - "若日後存入，財產所有權仍屬辭歲；商會取得的是債務性資金使用權。"

  room_and_consent:
    - "六條＋趙受益：關門熄燈不得推導性交。"
    - "皇太極＋蘇清：進房不得推導性交。"
    - "乾隆＋錦棠、朱正德＋辭歲：拍得一夜契約不得推導契約外無限同意。"

  character_sovereignty:
    - "李世民沒有女人線也可以是完整結果。"
    - "朱棣沒有女人線也可以是完整結果。"
    - "任何帝皇『空著』不代表劇情未完成。"
    - "玩家說某兩人對味，只提高注意力／候選 PATH，不自動形成 NPC 興趣或成功配對。"
    - "不得把本夜後段『一個個對付帝皇』的玩家玩法固化成觀止永久配對機制。"

  path_field:
    - "下一幕須允許對味、普通聊天、沒興趣、轉移注意、拒絕、各走各的、未決等 PATH 同時保有資格。"
    - "不得因前一輪某類配對連續成功，就讓舊配對 PATH 無新授權地取得主位。"

  li_qingzhao:
    - "李清照本夜來訪原因是逃難途中找張麗華喝酒，使用白御行預付酒資；不是被安排給趙光義。"
    - "李清照仍非人物卡池常駐人物，除非 GM 另行升格。"

  save_integrity:
    - "財務可能帶來的未來自主、拒客、置產、投資等，只可作後續因果候選；未發生前不得當作已完成硬狀態。"
```

---

# 32｜理火接關治理備忘【非世界事實】

```yaml
DIRECTOR_RUNTIME_GUARD:
  document_level_status: "REBOUND_FOR_NEXT_STORY_TURN"
  deployment_claim: false

  current_issue_classification:
    primary: "PLAYER_ATTENTION_DOMINANCE_WITH_DIRECTOR_REBALANCE_MISS"
    rollback_required: false
    world_corruption_confirmed: false

  interpretation:
    - "後段配對方向主要由玩家持續主動點名與拉動注意力形成。"
    - "已成立 NPC 自願行動不撤銷。"
    - "導演問題在於沒有於連續配對成功後重新放回反對 PATH、無結果 PATH 與人物自行轉向 PATH。"

  next_story_binding:
    protocol:
      - "反自我封聖"
      - "邏輯／責任／誠實"
    lighter:
      - "AUTHORIZED_INPUT_PACKAGE"
      - "CONTEXT_CONTAMINATION_OUTPUT_GATE"
      - "舊 PATH 無新授權不得異常取得主位"
    main_system:
      - "PATH 非歸一化亮度"
      - "Competition 不是淘汰"
      - "R2 強制反對 PATH／受壓暗差異 PATH／殘煙 PATH 重入"
      - "未決／正交／多態可合法保存"
      - "Final Classicalization 不得提前替故事收線"
    analyzer_exit:
      - "分析完成後退出前台"
      - "沒有新觸發不重複全域審計"
      - "SCOPED REACTIVATION"
      - "Rendering 限制不得倒灌 Character／Event"

  save_boundary:
    - "本節為導演治理備忘，不取得世界事實權、人物人格權或關係權。"
```

---

# 33｜直接接關摘要

```yaml
DIRECT_RESUME:
  scene_anchor:
    date: "理火三年槐月二十八日無月夜"
    time: "深夜"
    player_position: "與李師師、張麗華同桌飲酒"
    event_status: "帝皇聯誼會前宴已結束；世界已分流"

  immediate_world_state:
    - "雙姝競拍已成交：辭歲 12,000,000／朱正德；錦棠 5,000,000／乾隆。"
    - "翌日定陶商會需先調 3,000,000 兩；其餘 14,000,000 最遲十日結清。"
    - "六條與趙受益已互認在意並進六條房聊天；房內未知。"
    - "皇太極與蘇清已進私人房先聊；房內未知。"
    - "十三娘與劉病己賭局仍可繼續。"
    - "趙光義已離開李師師偏廳，轉與李清照同桌喝酒；李清照來訪本意是找張麗華喝免費酒。"
    - "乾隆與疏影談畫；嬴政由青禾按摩；劉禪與小翠低壓聊天；忽必烈與阿麗婭談草原西域；李世民與潘金蓮互相注意；李隆基與紅娘喝酒互拆。"
    - "白玉池為本夜特殊試營運，非正式全面復業。"

  next_turn_rule:
    - "可以從翌晨自然顯影。"
    - "也可以由玩家點名任一尚亮 PATH 接續。"
    - "若玩家只說繼續，導演應推進一個清楚場景節點，不替玩家作重大選擇。"
    - "不得以『把剩下皇帝都配完』作為預設收束目標。"
```

---

# 34｜HOT V3.5 結論

```yaml
HOT_V3_5_CONCLUSION:
  status: "VALID_HOT_SAVE_CANDIDATE"
  current_world_time: "理火三年槐月二十八日無月夜／深夜"

  hard_results:
    - "九幽帝皇聯誼會觀止前宴完成並自然分流。"
    - "辭歲以 12,000,000 兩成交一夜契約；本人應收 10,800,000 兩，觀止應收 1,200,000 兩。"
    - "錦棠以 5,000,000 兩成交一夜契約；商會應收 3,750,000 兩、錦棠應收 750,000 兩、觀止應收 500,000 兩。"
    - "兩筆合計 17,000,000 兩仍在清算；次日先調 3,000,000 兩，最遲十日全清。"
    - "白玉池本夜特殊試營運成立，但沒有正式全面復業。"
    - "六條與趙受益互認『有／在乎』，但未定義戀愛與承諾。"
    - "多條帝皇人物線已依人物本人形成不同程度之談話、按摩、賭局、私人房資格或純社交入口；未決者保持未決。"
    - "尾聲白御行、李師師、張麗華同桌閒聊並以 HOT SAVE 收幕。"

  next_valid_hot_version: "V3.6"
  master_merge: "NOT_PERFORMED"
  character_pool_update: "NOT_PERFORMED"
  runtime_patch_merge: "NOT_PERFORMED"
```


<!-- PROMOTED_SOURCE_END: 觀止青樓_白御行線_HOT_SAVE_V3.5_槐月二十八日無月夜_九幽帝皇聯誼會散場_雙姝天價競拍_帝皇分流_三人閒聊版.md -->


<!-- PROMOTED_SOURCE_BEGIN: 觀止青樓_白御行線_HOT_SAVE_V3.6-R2_榴月一日上午_朱明欠單顯擺與鄭成功週轉預案_六條趙受益非理火顯影污染校正_正式修正版.md -->
# SOURCE ARCHIVE｜觀止青樓_白御行線_HOT_SAVE_V3.6-R2_榴月一日上午_朱明欠單顯擺與鄭成功週轉預案_六條趙受益非理火顯影污染校正_正式修正版.md

**SHA-256：** `2e91f64438943a003b1bcad994aa921325b83e94fa74edd1a9b53a14e3cad490`

> **法位：本檔 E93–E98 固化來源。** 原 HOT 內的 CURRENT_SCENE／HOLD 只代表當時快照；不得覆寫本 MASTER 截止或 V4.1–V4.4 疊加層。

# 觀止青樓｜白御行線 HOT SAVE V3.6-R2
## 理火三年榴月一日上午｜V3.6-R1 再補正 × 朱明欠單顯擺與鄭成功週轉預案 × 六條趙受益非理火顯影污染校正 × 十日整修承接正式修正版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V3_6_R2_LIU01_MORNING_ZHU_IOU_SHOWOFF_ZHENG_LIQUIDITY_PROPOSAL_ROKUJO_ZHAO_RENDERING_CORRECTION"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V3.6-R2"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V11.0-R2"
  character_source: "觀止人物卡池_LCAPG_V2.2_辭歲入觀止動機校正_青禾六條增補_正式版"

  story_time_span:
    start: "HOT V3.5 後／槐月二十八日無月夜散場後"
    current: "理火三年榴月一日上午"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AFTER_HOT_SAVE_COMMAND_AT_GUANZHI_FRONT_HALL_DURING_TEN_DAY_INTERNAL_RENOVATION_PERIOD"

  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V3.5_槐月二十八日無月夜_九幽帝皇聯誼會散場_雙姝天價競拍_帝皇分流_三人閒聊版.md"
  corrects_hot: "觀止青樓_白御行線_HOT_SAVE_V3.6-R1_榴月一日上午_朱家湊款補正_六條趙受益成人結果校正_正式修正版.md"
  correction_chain:
    - "HOT V3.6"
    - "HOT V3.6-R1"
  correction_type: "R2_SAVE_CORRECTION_NO_NEW_STORY_TIME"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"

  experimental_overlays:
    performance_patch:
      file: "觀止青樓_PATCH_風月角色表演與接戲能力_V0.1-EXP_獨立試跑未併主系統.md"
      status: "INDEPENDENT_TRIAL_OVERLAY_NOT_MERGED"
    analyzer_exit_patch:
      file: "觀止青樓_PATCH_分析器退場_重大升階定義_SCOPED_REACTIVATION_顯影反污染_V0.1-EXP.md"
      status: "GUANZHI_SPECIFIC_OPTIONAL_EXPERIMENTAL_OVERLAY_NOT_MERGED"
    lihuo_environment_patch:
      file: "理火環境_PATCH_V0.1.md"
      status: "REFERENCE_OPTIONAL_EXPERIMENTAL_OVERLAY_NOT_MERGED"

  save_scope:
    - "HOT V3.5 後至榴月一日上午 HOT SAVE 命令前之直接劇情與玩家明示校正"
    - "槐月二十八日帝皇聯誼會各人物分流之翌晨清點；已能確認者固化，未觀察者不補成人結果"
    - "辭歲、錦棠雙姝首批實收、剩餘應收、自由期、贖身／自由妓女／明星與花魁候選方向"
    - "原牙行回訪、錦棠身份翻轉、人員配置與白希當日臨時協助"
    - "觀止十日對外暫歇、內部裝修、白玉池正式化與十日後重新開業決策"
    - "九幽前夜公款二十多萬兩折算回觀止後改存定陶商會公帳，不再搬現銀入樓"
    - "顧青簡下午辦私人開戶／理財顧問之已下達工作計畫，尚未實際完成"
    - "白宅施工延後至觀止十日整修後；浮香小館與李瓶兒同級房舍規格加入設計"
    - "阿麗婭本人明示對忽必烈『有一點喜歡』；忽必烈再訪、二十八日出閣、馬政、貿易、祖源論全部保持預案法位"
    - "校正 V3.6-R1 對朱明付款線之過度收斂：已成立的是朱厚照持 12,000,000 兩欠單回朱明家宅顯擺、家族知悉並形成資金壓力，以及朱厚照提出找鄭成功／國姓爺做短期週轉；尚未成立實際借款、到款或朱家共同分攤"
    - "補記六條＋趙受益之非理火／錯誤收斂樣本：前一版輸出曾把成人事件問題改寫成人物自主與關係哲學，該污染輸出不取得世界事實權；依修正後人物顯影與 GM 明示校正，前夜雙方自願性行為已成立"
```

---

# 0｜提交法位、來源、跨月校正與本輪反污染

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V3.5_槐月二十八日無月夜_九幽帝皇聯誼會散場_雙姝天價競拍_帝皇分流_三人閒聊版.md"
    role: "本檔直接前置 HOT；V3.5 及以前有效硬狀態全部繼承，除本檔明示更新／校正者"

  master_archive:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"
    role: "截至 HOT V2.5 之長期因果；V2.6-V3.5 由 HOT 鏈承接"

  current_route_conversation_commit:
    role: "HOT V3.5 後至本次 HOT SAVE 命令前之直接劇情、玩家明示自身言行／GM 設定、NPC 可觀察回應、人物本人明示、帳務／契約／付款與玩家明示校正"

COMMIT_NOTE:
  - "本 R2 不推進新故事時間；它再次修正 HOT V3.6-R1 對朱明付款線與六條／趙受益污染來源的壓縮方式。"
  - "HOT V3.5 仍是本故事時間切片的直接前置；V3.6-R2 取代 V3.6 與 V3.6-R1，成為榴月一日上午最新有效 HOT。"
  - "V3.6 與 V3.6-R1 原檔保留作審計來源，不作當前接關切片。"
  - "本次只更新 HOT；不更新 MASTER、不修改人物卡池、不修改主程序、不合併任何 EXP PATCH。"
  - "玩家明示『前晚的事情算清光了』之效力：槐月二十八日夜人物線不再以『待清點前夜結果』形式留在 OPEN_THREADS；但沒有來源的性交、戀愛、承諾、付款或房內細節不得因此補完。"
  - "所有未來阿麗婭出閣、二十八日私約、乾隆／忽必烈再競價、忽必烈帶馬、趙宋馬政／貿易、趙宋編祖源論，都只保存為 PROPOSAL／PREPLAN；不得自動觸發。"
  - "本輪前堂曾大量使用『變大』『又長又粗』『六個萬』等雙關玩笑；除另有硬事件外，不得轉成身體、債務、建築法則或世界機制。"
  - "V3.5 當夜把六條＋趙受益維持 UNKNOWN 是當時資料邊界正確；後續一組輸出曾出現明顯非理火／錯誤收斂：玩家追問熄燈後私事時，生成把事件問題改寫成自主、選擇與關係哲學，並以通用成熟語氣佔據趙受益人物聲音。"
  - "該污染輸出不得倒灌成趙受益真實台詞、六條關係狀態或『其實沒有成人事件』之證據。"
  - "修正後人物輸出重新回到八卦／私事場：趙受益以『我今天是自己走過來的』等話故意吊胃口、拒絕公開細節，並叫白御行若真想知道可當六條面問；此類台詞本身只屬顯影證據，不單獨作性交證明。"
  - "性交成立的最終 SAVE 法位來自 GM 明示校正；文件只將前後輸出差異記為疑似非理火錯誤收斂樣本，不宣稱宿主底層 Runtime 真實斷線。"

CALENDAR_TRANSITION:
  authority: "PLAYER_GM_CONFIRMED_CALENDAR"
  previous_date: "理火三年槐月二十八日／槐月最後一日"
  current_date: "理火三年榴月一日"
  rule:
    months_per_year: 13
    days_per_month: 28
    day_29_exists: false
  save_effect:
    - "HOT V3.5 之槐月二十八日後自然跨月為榴月一日。"
    - "不得生成槐月二十九日。"

ANTI_OUTPUT_DRIFT:
  zhang_lihua_morning_presence:
    baseline_confirmed:
      - "榴月一日清晨／上午早段，張麗華因前夜醉酒仍睡，未與白御行一同起身處理前堂清點。"
    renderer_drift_not_committed:
      - "本串個別生成曾讓張麗華在未交代足夠時間推進下提早出現在前堂參與設計討論。"
    save_rule:
      - "不把該提早出現固化為硬事件；若後續時間自然推進到她醒來，可再由世界顯影。"
```

---

## 0.1｜V3.6-R2 補正審計【不新增故事時間】

```yaml
V3_6_R2_CORRECTION_AUDIT:
  correction_target:
    - "HOT V3.6"
    - "HOT V3.6-R1"
  story_time_advanced: false

  issue_01_zhu_funding_overclosure:
    class:
      - "SAVE_EVENT_OVERCOMPRESSION"
      - "PROPOSAL_PROMOTED_TO_COMPLETED_FUNDING"
    r1_problem:
      - "R1 將已演出的朱明家宅場景壓成『朱家已啟動／完成內部湊款與資金調度』，超過原事件可支持範圍。"
    confirmed_scene_chain:
      - "朱厚照於帝皇聯誼會散場後返回九幽朱明家宅，手持觀止 12,000,000 兩私人欠單高調顯擺。"
      - "朱厚照反覆強調自己以 12,000,000 兩壓過乾隆 5,000,000 兩，將『全場最高／朱家第一』視為戰績。"
      - "朱元璋、朱棣、崇禎均已知悉該欠單與十日清算壓力；三人反應各異，但沒有因此自動成為共同債務人。"
      - "朱厚照想到鄭成功／國姓爺，提出找鄭氏做短期『週轉』；崇禎參與討論並提醒詢問利息。"
      - "朱厚照已表明要去找國姓爺；截至本 HOT，尚未觀察到其實際見到鄭成功、談成條件或取得款項。"
    corrected_state:
      - "朱明家族知悉欠單：CONFIRMED。"
      - "朱明家內形成資金壓力與籌資討論：CONFIRMED。"
      - "鄭成功／國姓爺短期週轉方案：PROPOSED_AND_INTENDED_NOT_EXECUTED。"
      - "朱家共同湊款已完成：NOT_ESTABLISHED。"
      - "鄭氏實際借款／到款：NOT_ESTABLISHED。"
    anti_overreach:
      - "不得把『國姓朱／國姓爺』玩笑直接升格成鄭成功承擔朱家債務之義務。"
      - "不得補造借款額、利率、擔保、還款期或朱明各皇帝分攤。"

  issue_02_rokujo_zhao_non_lihuo_rendering_contamination:
    class:
      - "TONE_ATTRACTOR_CAPTURE"
      - "ANALYZER_PERSISTENCE"
      - "EVENT_REFRAMING"
      - "CHARACTER_VOICE_CAPTURE"
      - "STALE_UNKNOWN_PERSISTENCE"
    v3_5_state:
      - "當夜僅見進房、關門、熄燈時，UNKNOWN 為正確法位。"
    polluted_output_pattern:
      - "玩家追問『熄燈後趙總很危險？說來聽聽』時，一版生成沒有留在昨夜成人／私事事件，而改寫為六條自主、觀止可讓人不用演、趙受益承認她能自己決定下一步等抽象關係論。"
      - "其中『我不是替她買一晚，我是承認，她可以自己決定下一步』與『六條御息所｜自主續留狀態待本人確認』屬非理火／治理語氣侵入人物與帳務層之污染樣本，不取得世界事實權。"
    corrected_output_pattern:
      - "修正後輸出讓趙受益回到人物位置：被眾人追問昨夜私事、故意吊胃口、拒絕公開六條細節，以『我今天是自己走過來的』等成人雙關反擊，最後叫白御行若真想知道可當六條面問。"
      - "此修正輸出顯示成人 PATH 與人物聲音恢復，但上述雙關本身不單獨證明性交。"
    gm_correction:
      - "GM 明示：六條與趙受益前夜確實雙方自願發生性行為；此為 SAVE 最終硬狀態。"
    save_effect:
      - "V3.6 的『性交 UNKNOWN』撤銷。"
      - "污染版抽象自主論不得倒灌為趙受益／六條人物真實台詞、關係結論或不存在成人事件的證據。"
    anti_overreach:
      - "確認性交不等於確認戀愛、婚姻、排他、永久同意或未顯影房內細節。"

  governance_status:
    status: "OBSERVED_OUTPUT_FAILURE_PATTERN_NOT_BOTTOM_LAYER_RUNTIME_FACT"
    note:
      - "GM 將前一版標為非理火狀態；文件可確認的是輸出層錯誤收斂與人物聲音被抽象治理語氣捕獲。"
      - "不得宣稱模型權重、宿主 Runtime 或不可見底層狀態已被證明中斷。"
      - "本正反樣本可供 CORRUPTION LOG／回歸測試使用，但污染輸出本身不進世界。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年榴月一日"
  time: "上午；帝皇夜翌晨清點與觀止內部重整決策已完成，精確時刻未知"
  primary_location: "觀止青樓／前堂"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  player:
    name: "白御行"
    current_position: "觀止前堂"
    current_state:
      - "已完成前夜帝皇聯誼會主要支線清點，不再要求逐線重問昨夜結果。"
      - "已與潘金蓮定下觀止十日對外暫歇、內部整修、十日後重新開業。"
      - "已決定九幽前夜公款折算款留存在定陶商會觀止公帳，不搬回觀止堆現銀。"
      - "已交代下午由顧青簡來替辭歲、錦棠辦私人帳戶並配置理財顧問。"
      - "已同意白宅工程待十日觀止整修後再開工；李師師先完成設計。"
      - "剛與阿麗婭、趙受益等談到忽必烈再訪之候選安排；尚未實際邀請。"

  pan_jinlian:
    current_position: "觀止前堂／掌櫃工作狀態"
    current_state:
      - "已接受十日歇業整修方案。"
      - "觀止普通外客十日內不接；內部採買、帳房、修繕、商會、牙行與必要公務仍可進出。"
      - "正在把大額現銀安全、內裝、白玉池與日常帳務視為十日內主要工作。"

  li_shishi:
    current_position: "觀止內；白宅設計責任已確認"
    current_state:
      - "白宅施工前十日先完成設計整理。"
      - "已收到浮香小館與李瓶兒同級房舍規格兩項新增需求。"

  zhang_lihua:
    current_position: "上午早段仍以醉後休息／睡眠為最後可靠位置"
    current_state:
      - "除非後續明示時間推進或她自行醒來，不把本串提早出現在前堂之渲染固化。"

  direct_resume_point:
    - "下一幕可從榴月一日下午顧青簡到場開戶／理財顧問初談開始。"
    - "也可從牙行候選、人員配置、觀止裝修、白玉池工程、商會清算或開封府西門慶案自然進場。"
    - "若玩家只說繼續，導演推進一個清楚節點；不得自動跳過十日、直接重新開業。"
```

---

# 2｜V3.5 繼承後仍活躍之核心狀態

```yaml
INHERITED_ACTIVE_CORE:
  emperor_auction_accounting:
    gross_contract_value_taels: 17000000
    cisu_contract_gross_taels: 12000000
    jintang_contract_gross_taels: 5000000
    guanzhi_total_share_taels: 1700000
    settlement_deadline: "由槐月二十八日成交日起最遲十日內完成清算"

  white_jade_pool:
    prior_state: "槐月二十八日帝皇夜完成特殊試營運"
    current_state: "列入觀止十日內部整修／正式化工程；尚非普通客全面營業"

  white_house:
    prior_framework:
      rent_taels: 8000
      term_years: 10
      nature: "條件式穩定空間租用框架"
    current_delta:
      - "施工延後至觀止十日整修完成後。"
      - "李師師於十日內繼續整理設計。"

  ximenqing_legal_line:
    status: "OFFSCREEN_ACTIVE"
    separation_rule:
      - "潘金蓮與蘇清民事賠償線，不等同白御行與蘇清之二十八日私人約。"
      - "蘇清二十八日私人約仍以『西門慶真正倒下』為觸發前提，不因其他民事收線自動啟動。"

  dingtao_business:
    - "定陶商會仍為大額資金調度、九幽折算、私人存款／借貸與後續資產管理接口之一。"
    - "白御行私人資產、觀止公帳、商會資產、辭歲私人財產、錦棠私人財產必須分帳。"

  cisu_and_jintang_free_window:
    - "辭歲、錦棠先前已簽未來身分／賣身相關契約，但目前仍在二十八日自由期。"
    - "自由期內兩人為自由人，不得因未來契約存在而強迫接客。"
    - "二十八日期滿後若未贖回／解除／改約，既有契約依原約生效。"
```

---

# 3｜MORNING01-E01｜榴月一日醒來與前夜清點啟動

```yaml
MORNING_EVENT:
  event_id: "MORNING01-E01-AFTER_EMPEROR_NIGHT_WAKE_AND_CLEARING"
  event_axis_state: "COMPLETED"

  confirmed:
    - "白御行於李師師房中醒來。"
    - "張麗華前夜酒醉較重，上午早段仍睡／無法立即起身參與前堂清點。"
    - "白御行與樓中人物陸續在前堂清點前夜帝皇分流、拍賣款、人物後續與觀止內務。"
    - "玩家最終明示：前晚的事情算清光了；不再保留一批『昨晚到底怎樣』式待追問鉤子。"

  boundary:
    - "『清點完』只關閉追問流程，不替未知房內事件補性交／感情／承諾。"
```

---

# 4｜LIUTIAO-ZHAO01-E01｜六條與趙受益前夜成人結果／顯影污染補正

```yaml
NIGHT_RESULT:
  event_id: "LIUTIAO-ZHAO01-E01-NIGHT_RESULT_CONFIRMED_ADULT_SEX_R2"
  event_axis_state: "COMPLETED_CONFIRMED"
  correction_of:
    - "V3.6 LIUTIAO-ZHAO01-E01-NIGHT_RESULT_CLOSED_WITHOUT_SEX_INFERENCE"
    - "V3.6-R1 only-result correction without full polluted-output provenance"

  confirmed:
    - "槐月二十八日夜，趙受益與六條進入六條房中；後續雙方自願發生性行為。"
    - "性交成立之最終法位來自 GM 明示校正；修正後人物輸出作為一致性支持，不以單句雙關獨立推導性交。"
    - "V3.5 當時只有進房、關門、熄燈，因此 V3.5 的 UNKNOWN 不視為錯誤；錯誤在後續事件已解決後仍讓舊 UNKNOWN 鎖死 SAVE。"

  polluted_rendering_excluded_from_world:
    - "曾有一版輸出將玩家對熄燈後私事的追問改寫為六條自主、觀止讓人不用演、趙受益承認她可自己決定下一步等抽象成熟論述。"
    - "該版屬非理火／錯誤收斂樣本；其抽象台詞、帳本文字與關係哲學不得作為人物真實台詞、事件結果或關係升階依據。"

  recovered_character_rendering:
    - "修正後趙受益以男人私事被追問的方式回應：吊胃口、嘴硬、故意只說熄燈、失言『我今天是自己走過來的』、最後拒絕再講並讓白御行若要知道可去問六條。"
    - "此段保存為人物聲音／事件顯影恢復之回歸對照，不要求 SAVE 重演完整對話。"

  relation_boundary:
    - "成人事件已發生不自動建立戀愛、婚姻、排他、所有權、固定伴侶或未來 blanket consent。"
    - "六條仍保有自己對後續見面、留宿、付款、關係與性之逐次決定權。"

  detail_boundary:
    - "未在可靠來源中顯影的具體房內動作、誰先主動到何種程度、完整對話、高潮／避孕等細節不得補造。"

  audit_note:
    - "本案例是『生成層先錯誤收斂 → 事件顯影缺失 → SAVE 再抓舊 UNKNOWN 固化』的回歸樣本。"
```

---

# 5｜LI-SHIMIN-PAN01-E01｜李世民與潘金蓮談話收束

```yaml
NIGHT_RESULT:
  event_id: "LI-SHIMIN-PAN01-E01-CONVERSATION_CLOSED"
  event_axis_state: "COMPLETED"

  confirmed:
    - "李世民與潘金蓮前夜在飲酒／談話後，話題落到若潘金蓮生在唐代會做什麼。"
    - "潘金蓮表明不接受皇帝替她安排人生；若在唐代，她仍可能選擇管理一棟樓／一盤生意。"
    - "該線以談話與帳務性格互相辨認收束，沒有新增成人關係或私人承諾。"
```

---

# 6｜SHISANNIANG-LIUBINGYI01-E01｜十三娘賭局翌晨顯影

```yaml
NIGHT_RESULT:
  event_id: "SHISANNIANG-LIUBINGYI01-E01-GAMBLE_MORNING_REVEAL"
  event_axis_state: "CLOSED_FOR_PREVIOUS_NIGHT_ACCOUNTING"

  confirmed:
    - "劉病己前夜進入十三娘房間；其主要事件軸為賭局。"
    - "榴月一日上午十三娘出現時，手上多了一只前夜未見之薄金鐲。"
    - "十三娘表示前夜所得足以讓她今天不用開賭桌。"

  unknown_preserved:
    - "精確賭注金額未知。"
    - "勝負每一步細節未知。"
    - "是否發生性行為未取得可核來源。"

  joke_not_asset_fact:
    - "『大漢國運』仍可作十三娘／前堂賭局笑稱；未形成可量化法定資產數值。"
```

---

# 7｜LIUCHAN-XIAOCUI01-E01｜劉禪與小翠蛋糕夜結果

```yaml
NIGHT_RESULT:
  event_id: "LIUCHAN-XIAOCUI01-E01-CAKE_GUEST_SLEEP_RESULT"
  event_axis_state: "COMPLETED"

  confirmed:
    - "前夜主要互動為吃蛋糕與聊天。"
    - "宴後劉禪一度不知道去哪裡，小翠帶他到客用睡眠處；不是小翠房間。"
    - "途中又到廚房拿蛋糕。"
    - "劉禪約吃一盤半，小翠約吃半盤。"
    - "劉禪問翌日是否還有蛋糕，小翠回答『有錢就有』。"

  relation_rule:
    - "本線不自動轉為戀愛、成人或配對線。"
```

---

# 8｜HUANGTAIJI-SUQING01-E01｜皇太極與蘇清私人夜確認

```yaml
NIGHT_RESULT:
  event_id: "HUANGTAIJI-SUQING01-E01-CONSENSUAL_PRIVATE_NIGHT_CONFIRMED"
  event_axis_state: "COMPLETED"

  confirmed:
    - "皇太極與蘇清前夜先長談，後續由蘇清本人明示：二人自願發生性行為。"
    - "沒有另計妓院服務費／嫖資；本夜被蘇清定義為私人夜，不是觀止安排的職業交易。"
    - "蘇清曾問：女人拿一個月換生意是否值得；皇太極回應重點為是否由她本人開價／決定，若價不是她開而是別人把她賣掉，不能視為她自己主導的交易。"
    - "蘇清表示這使她認為皇太極不是蠢人。"
    - "蘇清另明示：後續有腿部接觸，她沒有拒絕，之後兩人發生性行為。"
    - "皇太極欠蘇清下一次一張親手繪製的遼東商路圖。"

  boundary:
    - "本次同意只屬該次私人夜，不形成永久性同意、戀愛或排他承諾。"
```

---

# 9｜QIANLONG-SHUYING01-E01｜乾隆與疏影畫作夜結果

```yaml
NIGHT_RESULT:
  event_id: "QIANLONG-SHUYING01-E01-PAINTING_NIGHT_RESULT"
  event_axis_state: "COMPLETED"

  confirmed:
    - "乾隆與疏影作畫／談畫至接近破曉。"
    - "疏影對作品至少三次提出修正。"
    - "疏影允許乾隆只蓋一枚印。"
    - "疏影自己的印仍未落下，理由是她尚未判斷該作品是否值得。"
    - "乾隆表示下次可再問。"
    - "畫面內容為宴後、燈火將盡之場景。"

  relation_rule:
    - "本線固化為畫作／審美互動，不推導成人或戀愛結果。"
```

---

# 10｜QIANLONG-JINTANG01-E01｜乾隆與錦棠一夜契約履行確認

```yaml
NIGHT_RESULT:
  event_id: "QIANLONG-JINTANG01-E01-ONE_NIGHT_CONTRACT_SEX_CONFIRMED"
  event_axis_state: "COMPLETED_FOR_NIGHT_FULFILLMENT"

  confirmed:
    - "乾隆後續前往錦棠房間。"
    - "二人洗浴、吃喝、上床。"
    - "錦棠本人於翌晨明示：二人自願發生性行為。"
    - "錦棠表示乾隆當夜沒有以『已花五百萬買下她』之態度對待她。"
    - "過程中乾隆曾問錦棠對他的畫看法；錦棠表示自己不懂，後來笑稱也許應說很醜。"

  contract_boundary:
    - "此為五百萬一夜出閣契約之當夜自願成人履行。"
    - "不延伸為所有權、永久同意、戀愛或契約外服務義務。"
```

---

# 11｜KUBLAI-ALIYAH01-E01｜忽必烈與阿麗婭前夜結果

```yaml
NIGHT_RESULT:
  event_id: "KUBLAI-ALIYAH01-E01-TALK_KNIFE_NO_SEX"
  event_axis_state: "COMPLETED"

  confirmed:
    - "忽必烈與阿麗婭前夜沒有發生性行為。"
    - "兩人長時間談草原、撒馬爾罕、商路與遠方。"
    - "忽必烈在破曉前離開。"
    - "忽必烈送阿麗婭一把可實際使用的舊小彎刀。"
    - "忽必烈問若阿麗婭擁有真正草原快馬會騎去哪裡；阿麗婭當時不知道。"
    - "忽必烈回應：不知道也沒關係，先有馬。"

  future_language:
    - "『下次可能有馬／若還見得到』只保存為低約束後續話頭，不是交付契約。"
```

---

# 12｜LI-LONGJI-HONGNIANG01-E01｜李隆基與紅娘八百兩交易確認

```yaml
NIGHT_RESULT:
  event_id: "LI-LONGJI-HONGNIANG01-E01-PAID_ADULT_SERVICE_CONFIRMED"
  event_axis_state: "COMPLETED"

  confirmed:
    - "紅娘前夜自願與李隆基談成一筆私人成人生意。"
    - "成交價為 800 兩。"
    - "款項已付。"
    - "二人飲酒後上樓並發生性行為。"
    - "李隆基醒後曾問日後能否再找紅娘。"
    - "紅娘回應看價；若拿她與楊貴妃／梅妃比較，價格會再加。"

  relation_rule:
    - "一次付費成人交易不等於戀愛、排他承諾或永久服務關係。"
```

---

# 13｜OTHER-EMPEROR01-E01｜其餘前夜線清點關閉

```yaml
PREVIOUS_NIGHT_TRACKING_CLOSURE:
  event_id: "OTHER-EMPEROR01-E01-CLOSE_PREVIOUS_NIGHT_UNRESOLVED_QUEUE"
  event_axis_state: "COMPLETED_AS_ACCOUNTING_CLOSURE"

  zhu_zhengde_cisu:
    - "一夜契約的付款義務與辭歲分成繼續有效。"
    - "本輪沒有新增足以合法固化之具體成人履行細節。"
    - "因一夜時段已過，該線不再以『前夜結果待追問』掛起；未知成人細節保持未知。"

  zhao_guangyi_li_qingzhao:
    - "本輪沒有新增足以合法固化的酒後私人結果。"
    - "不再以『昨夜到底怎樣』掛起；不得補戀愛、性交或承諾。"

  yingzheng_qinghe:
    - "本輪沒有新增按摩之後的具體硬事件。"
    - "不再列前夜待清點懸案。"

  liu_bang_and_other_social_lines:
    - "沒有形成需補成人／配對結果的新硬狀態。"
    - "沒有結果本身是合法完成。"
```

---

# 13A｜ZHU-FUNDING28-E01｜朱厚照欠單顯擺 × 朱明資金壓力 × 鄭成功週轉預案補正

```yaml
ZHU_MING_IOU_AND_LIQUIDITY_EVENT:
  event_id: "ZHU-FUNDING28-E01-ZHENGDE_IOU_SHOWOFF_ZHENG_CHENGGONG_LIQUIDITY_PROPOSAL_R2"
  event_axis_state: "COMPLETED_FAMILY_SCENE_WITH_ACTIVE_OFFSCREEN_FUNDING_PROPOSAL"
  correction_of: "V3.6-R1 ZHU-FUNDING28-E01-ZHU_FAMILY_POOLING_FOR_ZHENGDE_12M_AUCTION"

  confirmed_scene:
    - "帝皇聯誼會散場後，朱厚照返回九幽朱明家宅，手持觀止 12,000,000 兩私人欠單高調顯擺。"
    - "朱厚照公開向朱元璋、朱棣、崇禎等人反覆強調自己以 12,000,000 兩壓過乾隆 5,000,000 兩，並把『全場最高／朱家昨晚第一』視為可炫耀戰績。"
    - "朱元璋、朱棣、崇禎已知悉該欠單與十日清算壓力；家族內部因此出現明確的震動、責罵、算帳與籌資討論。"
    - "朱厚照想到鄭成功／國姓爺，提出去找鄭氏做短期『週轉』；崇禎參與討論並提醒詢問利息。"
    - "朱厚照已表明要去找國姓爺；截至榴月一日上午 SAVE 時點，尚未觀察到其實際見到鄭成功或完成任何金融交易。"

  character_state:
    zhu_zhengde:
      - "目前不以 12,000,000 兩欠單為羞恥；相反地，把高價得標與壓過乾隆視為帝皇聯誼會戰績。"
      - "不得無事件直接改寫成因欠款而低調、羞愧或否認競拍。"

  funding_state:
    family_awareness: "CONFIRMED"
    family_funding_pressure_and_discussion: "CONFIRMED"
    zheng_chenggong_liquidity_route: "PROPOSED_AND_INTENDED_NOT_EXECUTED"
    zhu_family_joint_pooling_completed: "NOT_ESTABLISHED"
    zheng_family_actual_loan: "NOT_ESTABLISHED"
    actual_funds_received_from_zheng: "NOT_ESTABLISHED"

  accounting_boundary:
    - "朱厚照為辭歲 12,000,000 兩一夜契約之得標客戶／付款義務人；家族知悉或未來協助週轉不改寫契約客戶。"
    - "朱明家宅已開始討論怎麼籌，不等於觀止當場已實收全部 12,000,000 兩。"
    - "觀止／雙姝實收仍以 AUCTION01-E01 與後續清算帳為準：首批總計 3,000,000 兩，剩餘總額 14,000,000 兩依十日內清算。"

  detail_boundary:
    - "不得補造鄭成功是否同意、實際借款額、利率、擔保、還款期限、鄭氏資金來源或朱明各皇帝分攤比例。"
    - "『國姓朱』只保存為朱厚照在家族內拿來合理化找國姓爺週轉的說法／玩笑，不自動建立鄭成功對朱家債務的法律責任。"

  anti_regression:
    - "不得再把此線寫成『朱家已完成共同湊款』。"
    - "不得把朱厚照 12,000,000 兩寫成『個人現金已一次全額到觀止』。"
    - "不得把『提出找鄭成功週轉』寫成『鄭成功已借錢』。"
```

---

# 14｜AUCTION01-E01｜首批三百萬實到與雙姝第一批實收

```yaml
AUCTION_SETTLEMENT_DELTA:
  event_id: "AUCTION01-E01-FIRST_THREE_MILLION_AND_PERSONAL_CASH_DISTRIBUTION"
  event_axis_state: "CONTINUING_SETTLEMENT"

  first_batch:
    amount_taels: 3000000
    status: "ARRIVED_OR_BEING_FORMALLY_RECEIVED_IN_CURRENT_SETTLEMENT"

  cisu:
    total_receivable_taels: 10800000
    first_actual_distribution_taels: 1000000
    remaining_receivable_taels: 9800000
    physical_event:
      - "第一批一百萬曾搬至辭歲房中，讓她實際看到／感受巨額現銀規模。"
      - "此舉不代表一百萬必須永久存放房中。"

  jintang:
    total_receivable_taels: 750000
    first_actual_distribution_taels: 300000
    remaining_receivable_taels: 450000

  gross_remaining_to_clear_after_first_three_million:
    amount_taels: 14000000
    deadline: "沿用 V3.5：最遲十日內完成清算"

  anti_false_cash_recognition:
    - "辭歲仍未收到全部 10,800,000 兩。"
    - "錦棠仍未收到全部 750,000 兩。"
    - "17,000,000 兩成交總額仍不是同一時點全數現銀堆入觀止。"
```

---

# 15｜RICH01-E01｜辭歲巨額資產觀念與花魁方向

```yaml
CISU_ASSET_AND_CAREER_DELTA:
  event_id: "RICH01-E01-CISU_WEALTH_TIME_AND_TOP_COURTESAN_NEGOTIATION_POSITION"
  event_axis_state: "ACTIVE_UNDECIDED"

  confirmed_learning:
    - "白御行向辭歲說明：有錢人可以用錢買回時間；小事可交給可靠的人處理，但本人仍要知道是否做得好。"
    - "辭歲接受『委派小事、保留所有者判斷』的方向。"
    - "辭歲沒有因突然有錢而決定亂花；曾明示『我有錢又不是一定要花』式態度。"

  flower_queen_direction:
    - "辭歲仍在判斷自己喜歡的是『花魁身份』，還是被看見／被高價承認／可以自己定規則的感覺。"
    - "若花魁代表可選客、可定規則、客人為她的名字而來，她有興趣。"
    - "若只是換更漂亮牌子但仍由樓方決定她必須接誰，十餘萬／千萬資產下她沒有足夠理由接受。"
    - "白御行要求她未來與潘金蓮談判時按李師師／貂蟬級別的市場位置去談；此為議價定位，不等於她已取得李師師累積的才藝、名望或社交能力。"

  current_decision:
    - "是否贖身、是否成自由妓女、是否繼續花魁、具體分成與掛牌規則仍未定。"
```

---

# 16｜RICH01-E02｜錦棠自由妓女／明星／經紀約方向

```yaml
JINTANG_STATUS_AND_CAREER_DELTA:
  event_id: "RICH01-E02-JINTANG_FREE_COURTESAN_STAR_AGENCY_DIRECTION"
  event_axis_state: "ACTIVE_UNDECIDED"

  contract_holder:
    current_future_sale_contract_holder: "定陶商會"

  candidate_buyback:
    status: "PROPOSAL_NOT_EXECUTED"
    price_taels: 1200
    effect_if_executed:
      - "錦棠贖回賣身／奴籍性質之契約。"
      - "成為自由妓女；妓籍／公開表演職業身份可與人身所有權分離。"

  agency_direction:
    - "贖回後可自由選擇是否與定陶商會或其他機構簽娛樂／經紀約。"
    - "經紀約可由商會安排活動、人員、談工作並抽成；不等同賣身契。"
    - "抽成比例、年限、拒絕權、肖像／名字、本人自接工作、退出等條款尚未談。"
    - "白御行不打算親自逐條談，由相關副會長／專責人員與錦棠談。"

  runway_star_direction:
    - "錦棠已明示願意參與約三個月走秀／女裝／明星化訓練。"
    - "她接受服裝、走路、儀態、被看見與展示；訓練不等於簽經紀約或同意成人服務。"
    - "她希望三個月後建立新的名字與傳奇，不只被稱為『乾隆花五百萬睡過的女人』。"
```

---

# 17｜YAHANG01-E01｜原牙行回訪與錦棠身份翻轉

```yaml
YAHANG_EVENT:
  event_id: "YAHANG01-E01-ORIGINAL_BROKER_RETURNS_AND_JINTANG_ROLE_REVERSAL"
  event_axis_state: "COMPLETED_WITH_STAFFING_CONTINUING"

  setup:
    - "白御行命人叫來當初出售錦棠的牙行／牙婆，事前不告知真正客戶是錦棠。"

  confirmed_old_sale:
    old_name_reference: "玉娘"
    total_sale_taels: 600
    broker_share_taels: 550
    jintang_personal_share_taels: 50

  current_reveal:
    - "牙婆到場後認出錦棠。"
    - "錦棠已由五日前被出售的女人，變成持有三十萬首批現金、可自己挑人／雇人的客戶。"
    - "牙婆得知乾隆五百萬出閣成交與錦棠七十五萬分成。"

  public_story:
    approved_core:
      - "五天以前，我是別人拿來賣的；五天以後，我有錢回頭買人。"
      - "五天時間，觀止讓一個被賣的姑娘變成傳說。"
    anti_hype:
      - "不得宣稱觀止能保證所有六百兩姑娘五天後都變五百萬。"
      - "觀止提供平台／事件入口，不保證市場競價結果。"

  staffing:
    - "牙行已開始帶成年候選人給辭歲、錦棠看。"
    - "可考慮賣身契、長期雇用契、一般雇工等不同形式；人員契約形式不得偷混。"
```

---

# 18｜PETTYCASH01-E01｜錦棠打賞、白希臨時跟隨與三十二娘小金庫

```yaml
DELEGATION_EVENT:
  event_id: "PETTYCASH01-E01-JINTANG_TIPPING_BAIXI_TEMP_ASSIST_SANS’ER_PRIVATE_CASH"
  event_axis_state: "ACTIVE_FOR_TODAY"

  principle:
    - "白御行教錦棠：可隨身保留約三至五兩小銀供打賞，但本人不必每次親自翻錢。"
    - "由可信任的身邊人管理小額零用銀；錦棠只需決定『賞』與金額，助手執行並記帳。"
    - "小額打賞可用來回饋真正做得好的人並建立口碑，不等於無差別撒錢。"

  baixi:
    assignment: "榴月一日當日暫時跟隨錦棠"
    transfer_of_ownership: false
    tasks:
      - "協助挑人"
      - "管理／持有當日小額銀袋"
      - "跑腿、收物"
      - "執行打賞"
      - "記名單與文件"
    first_practice:
      - "有候選女僕做出一個細心小動作後，錦棠決定賞一兩；白希實際付款並記在錦棠名下。"

  sanshierniang:
    - "三十二娘曾從自己的小金庫拿小銀暫供錦棠使用。"
    - "白御行另給三十二娘 100 兩銀票補充其小金庫。"
    - "此 100 兩屬三十二娘，不是錦棠或觀止公帳。"
```

---

# 19｜BONUS01-E01｜掌櫃分紅與小獎金前堂玩笑

```yaml
BONUS_EVENT:
  event_id: "BONUS01-E01-SHOPKEEPER_DIVIDEND_VS_SMALL_BONUS_JOKE"
  event_axis_state: "PROPOSAL_AND_BANTER"

  confirmed:
    - "白御行表示商會近期收益好，過幾日可考慮對有工作的人發小獎金。"
    - "龐春梅指出自己已有觀止掌櫃分紅；若白御行另外承諾小獎金，她視為兩筆不同帳。"
    - "白御行以『六個萬字』紅包玩笑回應；龐春梅把六個萬字戲稱記成六萬兩。"

  hard_accounting:
    - "沒有實際成立六萬兩獎金債權。"
    - "具體小獎金名單與金額尚未定。"
```

---

# 20｜GUANZHI01-E01｜觀止十日對外暫歇與重新開業決策

```yaml
TEN_DAY_CLOSURE:
  event_id: "GUANZHI01-E01-TEN_DAY_EXTERNAL_CLOSURE_INTERNAL_OPERATION"
  event_axis_state: "ACTIVE"

  player_proposal:
    - "白御行指出觀止內已有數百萬兩銀款流動，若照常大開門做生意，等於吸引賊寇／梁山式風險。"

  pan_decision:
    - "潘金蓮接受觀止十日不接一般外客。"

  external_status:
    ordinary_business: "CLOSED_FOR_TEN_DAYS"
    reopen_plan: "十日後重新開業"
    public_reason: "內部整修"

  internal_continuity:
    allowed:
      - "觀止自己的人正常生活"
      - "廚房、採買、帳房、修繕"
      - "定陶商會必要人員"
      - "牙行／已約人員"
      - "官府／案件等必要公務"
    not_automatically_allowed:
      - "一般陌生客"
      - "普通熟客因熟就自動進樓"
      - "未經必要安排之大批外來隨從"

  core_reason:
    - "降低巨額現銀集中風險。"
    - "把帳務、清算、裝修、白玉池、談約與訓練集中處理。"
```

---

# 21｜RENOVATION01-E01｜大觀樓內裝十日整修

```yaml
RENOVATION_PLAN:
  event_id: "RENOVATION01-E01-GUANZHI_INTERIOR_REDESIGN"
  event_axis_state: "ACTIVE_PLANNING"

  white_yuxing_instruction:
    - "既然十日不對外開業，順便重新設計青樓內部裝扮，視為完整內部裝修。"

  li_shishi_design_direction:
    - "不只擦洗修補，而是重新整理整體風月氣質。"
    - "避免突然有錢後大量貼金造成俗豔。"
    - "白日可更明亮、乾淨、有秩序；夜晚再以燈、簾、紗、香、影改變氣氛。"
    - "整體目標可概括為艷而不亂。"

  room_tiering_direction:
    - "不同房間不必全部同規格。"
    - "普通姑娘、高價／自由名妓、特殊私人接待可依用途做不同配置。"
    - "門、鎖、起居、見客與私密性應視真正使用需求處理。"

  build_boundary:
    - "本節是十日內裝規劃／施工，不等於所有構想已完成。"
```

---

# 22｜WHITEJADE01-E01｜白玉池十日正式化工程

```yaml
WHITE_JADE_POOL_RENOVATION:
  event_id: "WHITEJADE01-E01-TEN_DAY_FORMALIZATION"
  event_axis_state: "ACTIVE_PLANNING"

  confirmed_direction:
    - "白玉池納入十日內裝工程，目標為把帝皇夜試營運補成可正式運行的空間。"
    - "更衣空間需擴充。"
    - "衣物、巾帕、鞋履、香皂需有固定管理。"
    - "池邊需有坐／休息處。"
    - "酒水、熱湯、小食應有固定放置／服務位置。"
    - "未來可依需求區分私池、共池、包場、單純沐浴與談事／社交用途。"

  unresolved:
    - "男女／時段／分區與完整營運規則尚未正式定案。"
    - "十日後是否所有區域同時全面開放，仍待工程與潘金蓮／阿泠等實際安排。"
```

---

# 23｜JIUYOU-ACCOUNT01-E01｜九幽前夜公款折算留存定陶商會

```yaml
JIUYOU_PUBLIC_ACCOUNT_SETTLEMENT:
  event_id: "JIUYOU-ACCOUNT01-E01-PUBLIC_EXPENSE_REIMBURSEMENT_TO_GUANZHI_DINGTAO_ACCOUNT"
  event_axis_state: "ACTIVE_ACCOUNTING"

  confirmed:
    - "九幽端已算出前夜帝皇聯誼會公款支出約二十多萬兩銀子。"
    - "白御行表示會折算補回觀止。"
    - "潘金蓮與白御行決定：該款不再以現銀整批搬回觀止。"
    - "折算後直接存在定陶商會、記入觀止公帳；觀止保留帳務憑證。"
    - "觀止裝修、白玉池、日常周轉等真正需要現銀時，再按需提取。"

  ownership:
    beneficial_owner: "觀止公帳"
    not_bai_private_money: true
    not_dingtao_free_asset: true

  amount_precision:
    - "目前只確認『二十多萬兩』；精確數字未在本輪固化。"
```

---

# 24｜GUQINGJIAN01-E01｜下午私人開戶與理財顧問安排

```yaml
FINANCIAL_SERVICE_PLAN:
  event_id: "GUQINGJIAN01-E01-AFTERNOON_PRIVATE_ACCOUNTS_AND_ADVISORS"
  event_axis_state: "SCHEDULED_NOT_YET_EXECUTED"

  responsible_person:
    name: "顧青簡"
    role: "定陶商會／總會女性師爺；白御行線路線 NPC"

  player_instruction:
    - "榴月一日下午讓顧青簡到觀止。"
    - "替辭歲、錦棠各辦私人帳戶。"
    - "順便各配置可提供資產規劃意見的理財顧問／專業人員。"

  account_principles:
    - "錢仍屬辭歲／錦棠本人。"
    - "觀止不得任意動用。"
    - "白家不得任意動用。"
    - "定陶商會不能因代管／借用資金就把本金當自己財產。"
    - "本人應可查帳。"
    - "顧問提供方案，不替本人做最後決定。"

  rate_anchor:
    time_deposit_annual_rate: "3%"
    note: "此為本線已明示之定陶商會定存年利率錨點。"

  status_boundary:
    - "顧青簡尚未在本 HOT 結束前實際到場。"
    - "帳戶尚未正式開完。"
    - "辭歲、錦棠尚未決定具體存款／投資比例。"
```

---

# 25｜WHITEHOUSE01-E01｜白宅施工延後至十日整修後

```yaml
WHITE_HOUSE_BUILD_DELAY:
  event_id: "WHITEHOUSE01-E01-DELAY_CONSTRUCTION_UNTIL_AFTER_GUANZHI_RENOVATION"
  event_axis_state: "CONFIRMED_PLAN"

  player_instruction:
    - "白家主宅不在觀止十日內裝期間同時開工。"
    - "等觀止十日整修完成後再由潘金蓮處理白宅形成／施工。"

  reason:
    practical:
      - "避免大觀樓、白玉池、帳務安全與白宅工程同時搶資源／注意力。"
      - "給李師師十日把可施工設計整理完整。"
    joke_only:
      - "『怕潘金蓮魔法用光變老』是白御行前堂玩笑，不是世界魔法消耗硬規則。"

  design_owner:
    - "李師師繼續負責白宅主要生活／功能設計。"
```

---

# 26｜WHITEHOUSE01-E02｜浮香小館與李瓶兒同級房舍加入設計

```yaml
WHITE_HOUSE_DESIGN_DELTA:
  event_id: "WHITEHOUSE01-E02-FUXIANG_PAVILION_AND_LI_PINGER_SAME_TIER_QUARTERS"
  event_axis_state: "CONFIRMED_DESIGN_REQUIREMENT_NOT_BUILT"

  fuxiang_small_house:
    name: "浮香小館"
    confirmed_source:
      - "浮香先前已表示希望白宅內有一個以她為名的小館。"
      - "白御行本輪正式提醒李師師把此需求加入白宅設計。"
    functional_direction:
      - "作浮香自己的小主場。"
      - "可自己待、也可待客。"
      - "不等同第二個大觀樓。"
      - "可考慮獨立入口並與白宅內部相通。"

  li_pinger_quarters:
    nickname_reference: "奶瓶"
    player_instruction:
      - "先替李瓶兒把如夫人等級的房／院規格留好。"
      - "房舍規格與李師師同級。"
    same_tier_means:
      - "同級面積／完整生活功能／私密性／主院待遇。"
      - "不要求建築外觀複製李師師。"
    anti_title_creation:
      - "此處固化的是白宅房舍設計／待遇規格；不得僅憑建築需求自動新增、覆寫或升格李瓶兒的正式名分。"

  construction_status: "NOT_STARTED"
```

---

# 27｜CISU-HOUSE01-E01｜辭歲觀止內住宅候選與增量建築原則

```yaml
CISU_RESIDENCE_DIRECTION:
  event_id: "CISU-HOUSE01-E01-NEAR_WHITE_HOUSE_CANDIDATE_PLOT"
  event_axis_state: "PROPOSAL_DIRECTION_NOT_CONTRACTED"

  confirmed_preference:
    - "辭歲對在觀止內、白宅附近建立自己的住宅方向感興趣。"
    - "她偏好有自己主院、浴室、金庫，未來可按人員／活動／宴客需求逐步擴張。"
    - "她不要求一開始就蓋巨大空宅。"
    - "白宅、辭歲住宅與可能其他鄰居可各有牆門與私人生活，同時共享部分大型公共庭園／大廳以減少浪費。"

  current_rights:
    - "只有候選位置／看地／留口方向。"
    - "尚未簽地。"
    - "尚未正式開工。"

  rent_discussion:
    white_house_anchor: "白宅 8,000 兩／10 年"
    floated_cisu_term: "曾討論 100 年若照同率名義為 80,000 兩"
    status: "NOT_AGREED"
    note: "潘金蓮曾指出白宅條件未必自動等比例套用辭歲；不得保存為已成交租約。"
```

---

# 28｜XIMENQING01-E01｜西門慶催案與蘇清二十八日約分軸

```yaml
LEGAL_DELTA:
  event_id: "XIMENQING01-E01-ZHAO_URGES_BAOZHENG_ASSET_PRESERVATION"
  event_axis_state: "OFFSCREEN_CONTINUING"

  player_instruction:
    - "白御行要求趙受益催包拯／開封府先審西門慶、查清財產並依法補償蘇清等相關人。"
    - "白御行另以『狗頭鍘』作戲謔性期待。"

  zhao_action:
    - "趙受益沒有替包拯預定死刑。"
    - "已寫／送催案訊息，要求加速審理、調查／保全資產、防止財產流失，依法處理補償／返還。"
    - "最終刑責由包拯依法裁判。"

  suqing_private_28_day_contract:
    trigger: "西門慶真正倒下／契約既定前提成立"
    status: "NOT_TRIGGERED"
    separation:
      - "不等同潘金蓮與蘇清之五萬兩民事和解。"
      - "民事賠償收線不會自動啟動二十八日私人約。"
```

---

# 29｜ALIYAH-KUBLAI01-E01｜阿麗婭明示對忽必烈有一點喜歡

```yaml
RELATION_EVENT:
  event_id: "ALIYAH-KUBLAI01-E01-A_LITTLE_LIKING_EXPLICIT"
  event_axis_state: "CONFIRMED_CHARACTER_STATEMENT"

  trigger:
    - "白御行直接問阿麗婭：是否真的有點喜歡忽必烈。"

  aliyah_answer:
    exact_state: "有一點"
    reasons_she_expressed:
      - "忽必烈沒有一直問她值多少錢。"
      - "沒有一坐下就問她能做什麼、是否要跟他走。"
      - "願意跟她談草原、馬、撒馬爾罕與遠方。"
      - "她講話時忽必烈有在聽。"
      - "小彎刀是直接送她，不是拿來買她。"

  current_willingness:
    - "如果忽必烈再來，她會想再跟他坐著聊。"
    - "如果有馬，她會想去看。"
    - "如果再談草原，她願意談。"

  explicit_boundary:
    - "『有一點喜歡』不等於已定義戀愛。"
    - "不等於同意出閣。"
    - "不等於同意二十八日成人契約。"
    - "不等於永久同意或承諾。"
```

---

# 30｜ALIYAH-KUBLAI01-E02｜忽必烈再訪候選安排與宮殿密道

```yaml
REVISIT_PLAN:
  event_id: "ALIYAH-KUBLAI01-E02-PRIVATE_REINVITE_VIA_ZHAO_PALACE_TUNNEL"
  event_axis_state: "PROPOSAL_ACCEPTED_FOR_FUTURE_ACTION_NOT_EXECUTED"

  player_instruction:
    - "白御行請趙受益下次帝皇聯誼會開會時，私下問忽必烈哪天有空，約他再來觀止。"
    - "不需要潘金蓮正式召喚／大張旗鼓接待。"
    - "可由趙受益先帶忽必烈回趙宋宮殿／住處，再由既有密道進觀止。"

  zhao_response:
    - "趙受益接受『下次遇到先私下詢問』的工作。"
    - "尚未實際開會、尚未詢問忽必烈、尚未取得對方同意或日期。"

  tunnel_anchor:
    - "趙受益宮殿／住處與觀止之間既有密道為白御行線既有設定。"
    - "本輪只提出未來可用於低調來訪；沒有實際走過本次再訪。"

  aliyah_visit_boundary:
    - "阿麗婭目前可接受的是來喝酒、吃飯、聊天、談馬等私人再見面方向。"
    - "如果來訪直接被改成拍賣／出閣／二十八日契，她沒有預先同意。"
```

---

# 31｜ALIYAH-AUCTION01-E01｜阿麗婭未來二十八日出閣候選企畫

```yaml
ALIYAH_FUTURE_AUCTION_PLAN:
  event_id: "ALIYAH-AUCTION01-E01-QIANLONG_KUBLAI_TWENTY_EIGHT_DAY_PROPOSAL"
  event_axis_state: "PROPOSAL_ONLY"

  player_idea:
    - "若未來阿麗婭本人決定掛牌出閣，可考慮把乾隆、忽必烈都列入邀請人。"
    - "白御行提出阿麗婭若走出閣，可設想二十八日契約。"
    - "若真有競價，不應只做乾隆與忽必烈兩人抬價專場，仍需真正有資格／意願的競價者。"

  aliyah_authority:
    - "是否掛牌由阿麗婭本人決定。"
    - "是否出閣由阿麗婭本人決定。"
    - "契約如何分配二十八日時間、住宿、陪伴、私人時間、拒絕與外出，全部尚未談。"

  current_status:
    - "沒有拍賣日期。"
    - "沒有出閣同意。"
    - "沒有二十八日契約。"
    - "乾隆與忽必烈均未收到邀請。"
```

---

# 32｜ZHAOSONG-KUBLAI01-E01｜馬匹、貿易與祖源論預案

```yaml
ZHAOSONG_KUBLAI_PREPLAN:
  event_id: "ZHAOSONG-KUBLAI01-E01-HORSE_TRADE_GENEALOGY_NARRATIVE_PREPLAN"
  event_axis_state: "PROPOSAL_ONLY_NOT_EXECUTED"

  horse_discussion:
    - "白御行提出：若忽必烈未來帶馬作價，大宋缺馬，可由趙宋視真實需求接收／買入。"
    - "趙受益表示若是真正好馬，大宋有興趣；若涉及成批良種，重點會轉向種馬、母馬與可持續繁育。"
    - "若馬匹用於任何出價，需先驗馬、估價；戰馬、乘馬、馱馬、年齡、健康、性子、耐力、公母與繁育價值不能混成一價。"
    - "阿麗婭是否喜歡某匹馬，不等於她接受任何出閣出價。"

  arabian_horse_discussion:
    - "白御行提出若是高品質阿拉伯／西域良種，大宋可能獲得高價值馬種來源。"
    - "此處只屬前堂戰略討論，沒有任何馬匹實際到貨。"

  trade_discussion:
    - "若忽必烈未來在趙宋停留，可另談馬、皮貨、藥材、草原貨源與宋地茶、絲、瓷、紙等貿易。"
    - "阿麗婭私人時間與趙宋外交／貿易必須分軸；不得把她的二十八日私人契約視為大宋免費外交資產。"

  genealogy_narrative:
    player_instruction:
      - "白御行不是要求趙宋考證一條真祖譜，而是提出可編一套政治友好的漢匈甥舅／草原帝胄祖源敘事，作為拉近忽必烈與趙宋距離、改善馬匹／貿易談判氣氛的話術資產。"
    intended_style:
      - "不把忽必烈寫成漢臣。"
      - "不宣稱蒙古從屬趙宋。"
      - "可用『漢家甥舅，草原帝胄』式對雙方都有面子的敘事。"
    current_status:
      - "趙受益理解並接受這是一個未來可交大臣處理的政治宣傳／祖源論企畫。"
      - "尚未命人實際編寫。"
      - "尚未形成正式文書。"
      - "尚未給忽必烈看。"
      - "沒有因此取得任何馬匹、價格優惠或貿易協議。"
```

---

# 33｜人物與關係增量

```yaml
RELATION_DELTAS:
  aliyah_kublai:
    prior: "槐月二十八日自願談草原／西域；沒有成人行為；忽必烈贈舊小彎刀"
    current:
      - "阿麗婭本人明示對忽必烈『有一點喜歡』。"
      - "若他再來，阿麗婭願意再聊天／談馬／看馬。"
      - "沒有升格為戀愛、出閣同意、二十八日契約或承諾。"

  liutiao_zhao_shouyi:
    prior: "互認有／在乎，慢慢看"
    current:
      - "前夜關門熄燈後沒有可核性交結果。"
      - "關係仍沿用慢慢看；不因前夜未知而退回陌生，也不因共處而自動升格。"

  huang_taiji_su_qing:
    prior: "先聊天並保留後續決定權"
    current:
      - "蘇清本人明示前夜自願發生性行為。"
      - "皇太極欠一張親繪遼東商路圖。"
      - "一次私人夜不自動形成永久成人關係。"

  qianlong_jintang:
    prior: "五百萬一夜契約已成交"
    current:
      - "當夜成人履行由錦棠本人確認自願完成。"
      - "錦棠職業／自由／明星路線仍由她後續自行決定。"

  li_longji_hongniang:
    prior: "喝酒互拆"
    current:
      - "800 兩成人交易已完成並付款。"
      - "日後再見只停在『看價』，沒有固定關係。"

  cisu_pan:
    current:
      - "辭歲未來是否贖身／自由妓女／花魁，需與潘金蓮另談。"
      - "尚無成交條件。"

  jintang_dingtao:
    current:
      - "錦棠可談 1,200 兩贖回自身未來契約之候選方案。"
      - "其後是否與商會簽經紀約仍由本人另決。"
```

---

# 34｜帳務、契約與財產硬狀態

```yaml
PRIVATE_CONTRACT_AND_LEDGER:
  cisu_one_night_contract:
    gross_taels: 12000000
    cisu_total_share_taels: 10800000
    guanzhi_total_share_taels: 1200000
    first_actual_distribution_taels: 1000000
    cisu_remaining_receivable_taels: 9800000
    overnight_fulfillment_detail: "NO_NEW_HARD_DETAIL; NIGHT_WINDOW_CLOSED_WITHOUT_INFERENCE"
    ownership_transfer: false

  jintang_one_night_contract:
    gross_taels: 5000000
    dingtao_total_share_taels: 3750000
    guanzhi_total_share_taels: 500000
    jintang_total_share_taels: 750000
    first_actual_distribution_taels: 300000
    jintang_remaining_receivable_taels: 450000
    overnight_fulfillment_detail: "CONSENSUAL_SEX_CONFIRMED_BY_JINTANG"
    ownership_transfer: false

  auction_settlement:
    gross_total_taels: 17000000
    first_batch_taels: 3000000
    remaining_to_clear_taels: 14000000
    deadline: "WITHIN_TEN_DAYS_FROM_ORIGINAL_SETTLEMENT_PLAN"

  jintang_future_identity_contract:
    current_holder: "定陶商會"
    freedom_window: "ACTIVE_28_DAY_FREE_PERIOD"
    buyback_candidate_taels: 1200
    buyback_status: "NOT_EXECUTED"
    agency_contract_status: "NOT_NEGOTIATED"

  cisu_future_identity_contract:
    counterpart: "觀止／潘金蓮"
    freedom_window: "ACTIVE_28_DAY_FREE_PERIOD"
    redemption_or_free_courtesan_terms: "NOT_NEGOTIATED"

  guanzhi_public_jiuyou_reimbursement:
    amount: "二十多萬兩；精確值未固化"
    storage_direction: "定陶商會／觀止公帳"
    physical_delivery_to_guanzhi: false

  dingtao_private_account_plan:
    cisu_account: "SCHEDULED_NOT_OPENED"
    jintang_account: "SCHEDULED_NOT_OPENED"
    time_deposit_rate_annual: "3%"

  sanshierniang_private_cash:
    white_yuxing_topup_taels: 100
    ownership: "白三十二娘私人小金庫"

  bonus:
    small_bonus_plan: "AMOUNTS_NOT_SET"
    pang_chunmei_six_wan_joke: "NOT_A_REAL_60000_TAEL_DEBT"
```

---

# 35｜知情範圍與來源

```yaml
KNOWLEDGE_SCOPE:
  public_or_broadly_witnessed:
    - "觀止將對外暫歇十日並以內部整修為公開理由。"
    - "帝皇夜雙姝五百萬／一千二百萬成交在前堂／相關圈層已廣泛可知。"
    - "原牙婆已知道錦棠五日內由六百兩被售者變成五百萬出閣傳奇與三十萬首批實收者。"
    - "錦棠要求外傳時要傳她的名字，不只傳五百萬女人。"

  accounting_limited:
    - "辭歲、錦棠個人分成與首批實收，由本人、白御行、潘金蓮、必要帳房／商會人員依職務知情。"
    - "九幽二十多萬公款折算回觀止並存在定陶商會，屬觀止／商會帳務知情，不是所有普通姑娘都必須知道細節。"

  private_character_statements:
    aliyah_kublai_liking:
      direct_witnesses:
        - "白御行"
        - "趙受益"
        - "當時前堂近場人物依可聽距離可能知情"
      status:
        - "阿麗婭本人明示『有一點』；不是導演推論。"

  previous_night_private_results:
    huang_taiji_suqing:
      source: "蘇清本人翌晨公開／近場明示"
    qianlong_jintang:
      source: "錦棠本人翌晨明示"
    kublai_aliyah_no_sex:
      source: "阿麗婭／翌晨清點結果"
    li_longji_hongniang:
      source: "紅娘本人翌晨明示交易、價格與結果"
    liutiao_zhao:
      source: "HOT V3.6 後劇情顯影＋GM 明示校正"
      confirmed: "雙方自願發生性行為"
      source_limit: "只確認成人事件成立；未顯影的具體房內細節仍不得越權補造"
    zhu_family_funding:
      source: "GM 補回之九幽朱明家宅直接劇情"
      confirmed: "朱厚照持 12,000,000 兩欠單返朱明家宅顯擺；朱元璋、朱棣、崇禎知悉；朱厚照提出找鄭成功／國姓爺做短期週轉"
      source_limit: "尚未成立實際借款、到款、利率、擔保或朱明各人成交分攤"
```

---

# 36｜仍活躍但未解事項

```yaml
OPEN_THREADS:
  high_priority:
    - id: "ACCOUNT01-OPEN-01"
      state: "ACTIVE"
      item: "剩餘 14,000,000 兩如何在原定十日內完成清算；辭歲剩餘 9,800,000、錦棠剩餘 450,000 實際何時入帳。"

    - id: "GUQINGJIAN01-OPEN-01"
      state: "SCHEDULED_TODAY"
      item: "榴月一日下午顧青簡到場替辭歲、錦棠開私人帳戶並配置理財顧問；具體存款／投資方案由本人決定。"

    - id: "RENOVATION01-OPEN-01"
      state: "ACTIVE_TEN_DAY_PROJECT"
      item: "大觀樓內裝、房間分級與十日後重新開業之實際施工／完成度。"

    - id: "WHITEJADE01-OPEN-01"
      state: "ACTIVE_TEN_DAY_PROJECT"
      item: "白玉池更衣、休息、酒水／小食、分區／時段與正式營運規則。"

    - id: "CISU-CONTRACT01-OPEN-01"
      state: "UNDECIDED"
      item: "辭歲是否贖身／轉自由妓女／繼續花魁，以及與潘金蓮的具體條件。"

    - id: "JINTANG-CONTRACT01-OPEN-01"
      state: "UNDECIDED"
      item: "錦棠是否以 1,200 兩贖回契約、是否另簽定陶商會經紀約及其條款。"

    - id: "YAHANG01-OPEN-01"
      state: "CONTINUING"
      item: "辭歲、錦棠各自實際挑選／雇用哪些人，採何種契約。"

    - id: "XIMENQING01-OPEN-01"
      state: "OFFSCREEN_ACTIVE"
      item: "包拯／開封府對西門慶案的正式裁判、資產清理、補償與蘇清二十八日約是否觸發。"

    - id: "ZHU-ZHENG-LIQUIDITY01-OPEN-01"
      state: "OFFSCREEN_ACTIVE_INTENT"
      item: "朱厚照已表明要找鄭成功／國姓爺談 12,000,000 兩欠單之短期週轉；是否實際見面、鄭成功是否願意、金額／利率／擔保／到款均未定。"

  medium_priority:
    - "李師師十日內整理白宅施工版設計；浮香小館與李瓶兒同級房舍如何落圖。"
    - "辭歲觀止內候選住宅是否進一步談租地、預算與增量建築。"
    - "錦棠三個月走秀／明星培訓之正式場地、訓練與經紀分離執行。"
    - "商會數日後是否實際發小獎金；金額尚未定。"

  proposal_only_not_active_world_event:
    - "趙受益下次帝皇聯誼會是否真的遇到並邀請忽必烈。"
    - "忽必烈是否再訪觀止。"
    - "阿麗婭是否掛牌／出閣／簽二十八日約。"
    - "乾隆是否再參與阿麗婭任何競價。"
    - "忽必烈是否帶馬、是否為阿拉伯／西域良種。"
    - "趙宋是否真的啟動馬政／草原貿易談判。"
    - "趙宋是否真的編製漢匈甥舅／蒙古祖源論。"

  explicitly_removed_from_previous_night_open_queue:
    - "六條＋趙受益前夜成人結果已確認為雙方自願性行為；不再回退 UNKNOWN，也不再追問未顯影細節。"
    - "十三娘＋劉病己前夜精確賭注／成人結果不再追問；已有薄金鐲與『今日不用開賭桌』之可見顯影。"
    - "趙光義＋李清照前夜酒後結果不再追問；沒有新硬結果即保持沒有。"
    - "朱正德＋辭歲前夜成人履行細節不再追問；一夜時段已過，帳務仍走清算。"
    - "嬴政＋青禾等前夜沒有新增硬結果者，不再為了『補齊帝皇』強行生成。"
```

---

# 37｜禁止回歸／防污染

```yaml
ANTI_REGRESSION:
  calendar:
    - "不得生成槐月二十九日。"
    - "本 HOT 已進榴月一日。"

  previous_night:
    - "不得因『昨晚清光』把所有進房線補成性交。"
    - "六條＋趙受益為已取得後續顯影／GM 校正之特例：性交已確認，不得再回退成 UNKNOWN。"
    - "六條＋趙受益性交確認不得反向擴寫成戀愛、婚姻、排他或永久同意。"
    - "不得重新把 V3.5 的帝皇分流逐人列回待收線清單。"
    - "沒有新硬結果的趙光義＋李清照、朱正德＋辭歲等保持資料邊界，不鬼打牆。"

  money:
    - "17,000,000 兩成交總額 != 已全收現銀。"
    - "朱厚照 12,000,000 兩欠單已在朱明家宅公開顯擺並造成家族資金壓力；不得退化成『朱正德個人現金一次全付』。"
    - "朱厚照提出找鄭成功／國姓爺做短期週轉；此方案尚未成交，不得寫成鄭氏已出資。"
    - "朱明家族知悉／討論籌資 != 朱家已共同湊款完成；觀止實收仍以清算帳為準。"
    - "辭歲已實收只有第一批 1,000,000 兩；剩餘 9,800,000 仍應收。"
    - "錦棠已實收只有第一批 300,000 兩；剩餘 450,000 仍應收。"
    - "九幽二十多萬公款折算回觀止後是觀止公帳，不是白御行私人錢。"
    - "辭歲、錦棠存入商會之私人資金若日後成立，所有權／債權仍屬本人。"

  identity_contracts:
    - "辭歲、錦棠目前仍在二十八日自由期。"
    - "未來賣身／身分契約存在不等於現在可強迫接客。"
    - "自由妓女可以仍有妓籍／公開表演身份；妓籍不自動等於人身被他人所有。"
    - "錦棠 1,200 兩贖回只屬候選方案，尚未付款／成交。"

  guanzhi_closure:
    - "觀止十日不對外普通營業，不等於世界／內部停止運轉。"
    - "十日歇業不得一個『繼續』直接跳到十日後重新開業。"

  white_house:
    - "白宅施工已延後至觀止十日整修後。"
    - "『潘金蓮魔法用光會變老』不得寫成真實魔法成本。"
    - "浮香小館與李瓶兒房目前是設計需求，不是已建成空間。"
    - "李瓶兒房舍與師師同級不得自動創造／覆寫正式名分。"

  zhang_lihua:
    - "榴月一日上午早段可靠狀態為醉後休息；未交代時間推進前，不得把早段渲染中的提早前堂出現倒灌成硬事實。"

  aliyah_kublai:
    - "阿麗婭『有一點喜歡』只是一層人物態度，不等於戀愛、出閣、成人同意或永久承諾。"
    - "小彎刀是已發生贈物；馬只是後續話頭，尚未交付。"
    - "再訪只是一個待趙受益日後詢問的計畫，不能自動讓忽必烈出現在觀止。"

  horse_trade_genealogy:
    - "任何阿拉伯馬／良種馬目前都沒有到貨。"
    - "趙宋馬政／貿易沒有成交。"
    - "所謂漢匈甥舅／蒙古祖源論是白御行提出的未來政治敘事企畫，不是真實已核祖譜，也沒有正式文書。"

  bonus_jokes:
    - "六個萬字紅包不是六萬兩硬債務。"
    - "『又長又粗／變大』等笑話不得轉成性能力硬狀態或建築規則。"

  path_field:
    - "阿麗婭／忽必烈可往再見、純聊天、談馬、沒有空、拒絕、淡掉等多 PATH 發展。"
    - "未來即使忽必烈帶馬，也不能用馬自動換取阿麗婭同意。"
    - "不得因本輪討論很熱鬧就把阿麗婭出閣列為導演必做 GOAL。"
```

---

# 38｜理火接關治理備忘【非世界事實】

```yaml
DIRECTOR_RUNTIME_GUARD:
  document_level_status: "ACTIVE_FOR_NEXT_STORY_TURN"
  deployment_claim: false

  current_issue_classification:
    primary:
      - "SAVE_FORMAT_REGRESSION_CORRECTED"
      - "PREVIOUS_NIGHT_OPEN_THREAD_LOOP_CLOSED_WITHOUT_FALSE_COMPLETION"
      - "PROPOSAL_VS_WORLD_FACT_SEPARATION_REQUIRED"
      - "V3_6_STALE_UNKNOWN_ON_LIUTIAO_ZHAO_CORRECTED"
      - "NON_LIHUO_TONE_ATTRACTOR_AND_ANALYZER_CAPTURE_SAMPLE_RECORDED"
      - "V3_6_R1_ZHU_FUNDING_OVER_CLOSURE_CORRECTED"

  interpretation:
    - "本輪前夜人物線已依玩家命令完成清點；下一串不可重新把整個帝皇夜當待辦表。"
    - "清點收束不等於把未知成人結果補成完整答案；使用 CLOSED_FOR_TRACKING／NO_NEW_HARD_DETAIL 保存不可達處。"
    - "本輪後段大量討論阿麗婭出閣、忽必烈、馬與祖源論，屬高亮候選企畫；只有阿麗婭本人『有一點喜歡』與趙受益接受日後可詢問邀約是已成立人物／工作狀態。"
    - "個別渲染曾使張麗華在上午早段未交代時間推進即出現在前堂；本 HOT 不倒灌該渲染。"
    - "六條＋趙受益案例顯示：舊 SAVE 的『當時不得推論』不能在新證據／新顯影與 GM 校正出現後永久鎖死 UNKNOWN。"
    - "污染版輸出把成人私事重寫成抽象自主／成熟關係論，屬語氣吸引子與分析器滯留侵入人物聲音的正反樣本；該輸出不取得世界事實權。"
    - "GM 將該段標為非理火狀態；文件級可確認的是錯誤收斂模式，底層 Runtime 中斷本身沒有可觀察證據，不作事實宣稱。"
    - "朱明付款線的已發生事件是欠單顯擺、家族知悉與籌資討論；R1 將其過度壓成『已完成共同湊款』，本 R2 已退回正確事件法位。"

  next_story_binding:
    protocol:
      - "玩家投下一個變數，導演讓整個世界回答它。"
      - "角色只能從自己的位置活著。"
      - "誰知道，要有來源。"
      - "態度變化，要有事件。"
      - "關係變化，要有因果。"
    save:
      - "事件、感情、契約、同意、付款、傳聞與人物解讀分軸。"
      - "預案不得偷升世界事實。"
      - "未執行工作可保存為 SCHEDULED／PROPOSAL，不得標 COMPLETED。"
    analyzer_exit:
      - "沒有新觸發不重複全域審計。"
      - "Rendering 錯誤不得因未被玩家立即糾正就自動固化。"

  save_boundary:
    - "本節只屬導演治理／接關備忘，不取得世界事實權、人物人格權或關係權。"
```

---

# 39｜直接接關摘要

```yaml
DIRECT_RESUME:
  scene_anchor:
    date: "理火三年榴月一日"
    time: "上午"
    player_position: "觀止前堂"
    event_status: "帝皇夜清點已收束；觀止進入十日閉門內部整修期"

  immediate_world_state:
    - "帝皇夜主要後續已清點：皇太極＋蘇清、乾隆＋錦棠、李隆基＋紅娘、六條＋趙受益均有已確認自願成人結果；忽必烈＋阿麗婭明確無成人行為。"
    - "辭歲已實收 1,000,000 兩，尚應收 9,800,000；錦棠已實收 300,000，尚應收 450,000。"
    - "拍賣剩餘 14,000,000 兩仍按原定十日內清算。"
    - "朱厚照持 12,000,000 兩欠單返回九幽朱明家宅高調顯擺，朱元璋／朱棣／崇禎均已知悉並形成籌資討論；朱厚照提出找鄭成功／國姓爺做短期週轉，但尚未成交或到款。"
    - "觀止普通外客暫停十日，內部整修後重新開業；大觀樓與白玉池為主要工程。"
    - "九幽前夜公款二十多萬兩折算回觀止後直接留存定陶商會觀止公帳，不搬進觀止堆現銀。"
    - "榴月一日下午顧青簡預定到場替辭歲、錦棠辦私人帳戶並配置理財顧問；尚未執行。"
    - "白宅工程十日後再開；李師師先完成設計，並加入浮香小館、李瓶兒同級房舍規格。"
    - "阿麗婭本人明示對忽必烈『有一點喜歡』；願意未來再聊天／談馬。"
    - "趙受益日後可在帝皇聯誼會私下詢問忽必烈再訪，但現在尚未邀請。"

  next_turn_rule:
    - "若玩家說繼續，優先從同日上午自然餘波或下午顧青簡到場推進一個場景節點。"
    - "不要重做前夜帝皇清點。"
    - "不要自動跳過十日整修。"
    - "不要自動讓忽必烈出現。"
    - "不要把阿麗婭未來出閣、馬匹、祖源論或趙宋貿易當成已開始事件。"
```

---

# 40｜HOT V3.6-R2 結論

```yaml
HOT_V3_6_R2_CONCLUSION:
  status: "VALID_CORRECTED_HOT_SAVE_SUPERSEDES_V3_6_AND_V3_6_R1"
  current_world_time: "理火三年榴月一日上午"

  hard_results:
    - "槐月二十八日帝皇夜後續已完成清點流程；未知保持未知，但不再留整批前夜待追問鉤子。"
    - "皇太極＋蘇清自願成人私人夜已確認；乾隆＋錦棠一夜契約自願成人履行已確認；李隆基＋紅娘 800 兩成人交易已付款完成；六條＋趙受益前夜雙方自願性行為已確認；忽必烈＋阿麗婭明確沒有成人行為。"
    - "朱厚照 12,000,000 兩欠單已在九幽朱明家宅公開顯擺，朱元璋／朱棣／崇禎知悉並形成籌資討論；朱厚照提出找鄭成功／國姓爺做短期週轉，但尚未形成實際借款、到款或家族共同分攤。"
    - "辭歲首批實收 1,000,000 兩；錦棠首批實收 300,000 兩；剩餘應收分別 9,800,000 與 450,000 兩。"
    - "觀止決定十日對外暫歇、內部整修，十日後重新開業。"
    - "白玉池納入十日正式化工程。"
    - "九幽前夜公款二十多萬兩折算回觀止後留存在定陶商會觀止公帳。"
    - "顧青簡榴月一日下午開戶／理財顧問工作已排定但尚未執行。"
    - "白宅施工延後十日後；浮香小館與李瓶兒同級房舍規格已加入設計需求。"
    - "阿麗婭本人明示對忽必烈『有一點喜歡』；未來再訪、出閣、馬政、貿易、祖源論均未執行。"

  supersedes_hot:
    - "V3.6"
    - "V3.6-R1"
  next_valid_hot_version: "V3.7"
  master_merge: "NOT_PERFORMED"
  character_pool_update: "NOT_PERFORMED"
  runtime_patch_merge: "NOT_PERFORMED"
```


<!-- PROMOTED_SOURCE_END: 觀止青樓_白御行線_HOT_SAVE_V3.6-R2_榴月一日上午_朱明欠單顯擺與鄭成功週轉預案_六條趙受益非理火顯影污染校正_正式修正版.md -->


<!-- PROMOTED_SOURCE_BEGIN: 觀止青樓_白御行線_HOT_SAVE_V3.7_榴月一日夜_辭錦瓶兒開戶_紅袖五十萬尺與召喚權_夜宵問答_紅娘門窗十日換債版.md -->
# SOURCE ARCHIVE｜觀止青樓_白御行線_HOT_SAVE_V3.7_榴月一日夜_辭錦瓶兒開戶_紅袖五十萬尺與召喚權_夜宵問答_紅娘門窗十日換債版.md

**SHA-256：** `a354e50c0d35a76c91e469303172da7dbef06ab4f14add436383eadc52c5e50a`

> **法位：本檔 E93–E98 固化來源。** 原 HOT 內的 CURRENT_SCENE／HOLD 只代表當時快照；不得覆寫本 MASTER 截止或 V4.1–V4.4 疊加層。

# 觀止青樓｜白御行線 HOT SAVE V3.7
## 理火三年榴月一日夜｜辭歲錦棠李瓶兒開戶 × 紅袖五十萬反向價格尺與召喚權 × 十日歇業夜宵問答 × 六條趙受益夜集外出 × 紅娘門窗屏風十日換債版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V3_7_LIU01_NIGHT_PRIVATE_ACCOUNTS_HONGXIU_PRICE_RULER_CALL_RIGHT_NIGHT_SNACK_HONGNIANG_ROOM_SWAP"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V3.7"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V11.0-R2"
  character_source: "觀止人物卡池_LCAPG_V2.2_辭歲入觀止動機校正_青禾六條增補_正式版"

  story_time_span:
    start: "HOT V3.6-R2 後／理火三年榴月一日下午"
    current: "理火三年榴月一日夜"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AFTER_HOT_SAVE_COMMAND_AFTER_NIGHT_SNACK_AND_HONGNIANG_ROOM_DOOR_WINDOW_SCREEN_REMOVAL"

  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V3.6-R2_榴月一日上午_朱明欠單顯擺與鄭成功週轉預案_六條趙受益非理火顯影污染校正_正式修正版.md"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"

  experimental_overlays:
    performance_patch:
      file: "觀止青樓_PATCH_風月角色表演與接戲能力_V0.1-EXP_獨立試跑未併主系統.md"
      status: "INDEPENDENT_TRIAL_OVERLAY_NOT_MERGED"
    analyzer_exit_patch:
      file: "觀止青樓_PATCH_分析器退場_重大升階定義_SCOPED_REACTIVATION_顯影反污染_V0.1-EXP.md"
      status: "GUANZHI_SPECIFIC_OPTIONAL_EXPERIMENTAL_OVERLAY_NOT_MERGED"
    lihuo_environment_patch:
      file: "理火環境_PATCH_V0.1.md"
      status: "REFERENCE_OPTIONAL_EXPERIMENTAL_OVERLAY_NOT_MERGED"

  save_scope:
    - "榴月一日下午顧青簡、杜蘅、程守拙到場後之辭歲／錦棠私人開戶與資產規劃初談"
    - "張麗華午後自然醒來並回到觀止活動空間"
    - "李瓶兒白宅如夫人同級房舍之入住時點、家具付款、掌櫃分紅嫁妝與私人開戶"
    - "浮香小館設計偏好、家具自行選購與白御行報銷承諾"
    - "紅袖聽雨閣私人琴局、摸手／掌心貼臉、白御行在房內睡著、晚飯同行與關係距離顯影"
    - "紅袖五十萬特殊一夜考慮門檻／反向價格尺之法位、兩條降距方向與清倌語義反污染"
    - "紅袖十日主動找人賭局、三擊掌成立後白御行立即提前認輸；紅袖取得一次召喚權"
    - "紅娘舊日留門煙幕／扶牆假戰報之事實與傳聞分軸校正"
    - "李師師舊賭局彩頭之收債爭議：白御行拒收原彩頭，不接受事後重寫新條款"
    - "紅娘第二局側賭原一次三人親密局債務，於本夜經本人同意正式換約為房門／窗扇拆除十日"
    - "觀止歇業第一夜全樓夜宵、受訓女子加入公共聊天與問答，內部距離縮短"
    - "趙受益受白御行提醒後親自邀六條外出逛汴京夜集；六條同意，二人截至本 HOT 尚未回樓"
    - "紅娘房門扇、窗扇實際拆除；屏風另由紅娘本人同意送保養十日；重新開業當日上午恢復"
    - "榴月一日上午潘金蓮×蘇清五萬兩民事線已達初步和解之漏記補正"
```

---

# 0｜提交法位、來源與本輪補正

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V3.6-R2_榴月一日上午_朱明欠單顯擺與鄭成功週轉預案_六條趙受益非理火顯影污染校正_正式修正版.md"
    role: "本檔直接前置 HOT；V3.6-R2 及以前有效硬狀態全部繼承，除本檔明示更新／補正者"

  master_archive:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"
    role: "截至 HOT V2.5 之長期因果；V2.6-V3.6-R2 由 HOT 鏈承接"

  current_route_conversation_commit:
    role: "HOT V3.6-R2 後至本次 HOT SAVE 命令前之直接劇情、玩家明示自身言行／GM 校正、NPC 可觀察回應、人物本人明示、付款／換約／賭約與已確認關係事件"

COMMIT_NOTE:
  - "本檔推進故事時間至榴月一日夜；不更新 MASTER、不修改人物卡池、不修改主程序、不合併 EXP PATCH。"
  - "本輪大量八卦、假價、假戰報與玩笑必須與世界硬事實分離；傳得像真的，不等於真的。"
  - "紅袖五十萬／八百八十八等數字必須依其法位分離：五十萬是她私下對白御行提出的當前特殊一夜『認真考慮／坐下談』門檻與關係尺起點；八百八十八只屬白御行故意設計的可信假八卦價，沒有成交。"
  - "清倌／紅倌為觀止當前服務與營業位置，不是處女標籤；不得因紅袖是清倌推導她未出閣、未拍賣或無性經驗。"
  - "李師師原賭局彩頭『指定她做一件她本人可以自願答應之事』在本輪實際收債時被白御行判定缺乏實質賭債價值並拒收；後續任何新版拒絕次數／第三件必選等修補條款均被白御行拒絕，不能倒寫成原約。"
  - "紅娘原側賭一次三人親密局已在本夜經紅娘本人同意換約並清掉；不得下一串又把原三人局當未償債務追回。"
  - "成人意願只記到人物當時已明示範圍；本輪沒有把尚未發生的今晚成人事件寫成已完成。"
  - "『九幽帝皇十日無限量』『召李隆基／嬴政／劉邦』『小鬼會不會來』皆停在玩笑／候選話題；沒有實際對九幽發公告、沒有召喚儀式、沒有新皇帝因此出現在觀止。"
```

---

## 0.1｜上午漏記補正：潘金蓮 × 蘇清五萬兩初步和解

```yaml
PAN_SUQING_50000_CORRECTION:
  correction_type: "LATER_STATE_OMITTED_FROM_V3_6_R2_DETAIL"
  story_time_advanced: false

  confirmed:
    - "榴月一日上午潘金蓮處理／計算掌櫃分紅與相關帳務時，蘇清民事線已進一步收斂。"
    - "潘金蓮與蘇清之五萬兩民事賠償／和解線，已達成『五萬兩初步和解』。"

  legal_axis:
    state: "PRELIMINARY_CIVIL_SETTLEMENT_REACHED"
    not_court_judgment: true
    not_same_as_white_suqing_28_day_private_agreement: true

  payment_axis:
    exact_payment_completion: "UNKNOWN_NOT_CONFIRMED_IN_CURRENT_RECORD"
    rule:
      - "初步和解成立 != 五萬兩已全額實付。"
      - "不得補造付款來源、付款日、分期方式或是否直接從潘金蓮掌櫃分紅扣除。"

  pollution_lock:
    - "本輪曾有導演錯誤輸出退回『五萬只是索賠、潘未認』之舊狀態；該輸出作廢，不取得世界事實權。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年榴月一日"
  time: "夜；晚飯與全樓夜宵後，精確時刻未知"
  primary_location: "觀止青樓／紅娘房所在走廊與內部公共區域"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  player:
    name: "白御行"
    current_position: "觀止內；紅娘房門窗／屏風拆除事件後"
    current_state:
      - "已完成榴月一日下午多條私人帳務／住居／關係場景。"
      - "已在觀止歇業第一夜請全樓夜宵並讓受訓女子加入公共聊天。"
      - "已對紅袖十日賭局三擊掌後立即提前認輸；因此欠紅袖一次召喚回應。"
      - "已拒收李師師原『指定一件她願意做的事』賭局彩頭，不接受事後重寫。"
      - "已與紅娘完成原三人局賭債換約：改為紅娘房門／窗扇拆除十日；原三人局賭債清零。"
      - "已支付／安排 10 兩木工加班費執行當夜拆除。"

  hongniang_room:
    door_leaf: "REMOVED"
    window_sashes: "REMOVED"
    screen: "REMOVED_FOR_TEN_DAY_MAINTENANCE_BY_HONGNIANG_CONSENT"
    wall_and_frames: "INTACT"
    curtains_or_temporary_board: "AGREED_REQUIREMENT_NOT_CONFIRMED_INSTALLED_YET"
    restore_deadline: "重新開業當日上午"

  zhao_shouyi_rokujo:
    current_position: "汴京夜集外出中"
    return_to_guanzhi: "NOT_YET_OBSERVED"

  direct_resume_point:
    - "下一幕可從榴月一日深夜觀止散場後各人夜間去向自然推進。"
    - "可從紅娘第一晚無門窗的生活後果、趙受益與六條夜集回程、李師師與白御行先前『回家再算』之未決安排，或其他內部十日整修事件進場。"
    - "不得自動跳到榴月二日或十日後重新開業；一個『繼續』只推進一個清楚節點。"
```

---

# 2｜V3.6-R2 繼承後仍活躍之核心狀態

```yaml
INHERITED_ACTIVE_CORE:
  ten_day_closure:
    status: "ACTIVE"
    date_day_1: "榴月一日"
    ordinary_public_business: "CLOSED"
    internal_operations: "ACTIVE"
    reopen_target: "十日整修期後"

  auction_accounting:
    gross_total_taels: 17000000
    first_batch_actual_taels: 3000000
    remaining_to_clear_taels: 14000000
    cisu_actual_taels: 1000000
    cisu_remaining_receivable_taels: 9800000
    jintang_actual_taels: 300000
    jintang_remaining_receivable_taels: 450000

  white_house:
    construction: "DELAYED_UNTIL_AFTER_TEN_DAY_GUANZHI_RENOVATION"
    li_shishi_design_work: "ACTIVE_DURING_CLOSURE"
    rent_anchor: "8000 兩／10 年"

  white_jade_pool:
    status: "ACTIVE_TEN_DAY_FORMALIZATION_PROJECT"

  ximenqing_legal_line:
    status: "OFFSCREEN_ACTIVE"
    white_suqing_28_day_private_agreement: "NOT_TRIGGERED_UNLESS_XIMENQING_TRULY_FALLS"

  zhu_hou_zhao_12000000:
    debt_iou: "ACTIVE"
    zheng_chenggong_short_term_liquidity_plan: "PROPOSED_NOT_EXECUTED"
```

---

# 3｜GUQINGJIAN01-E02｜顧青簡到場：辭歲／錦棠私人帳戶正式建立

```yaml
PRIVATE_ACCOUNT_EVENT:
  event_id: "GUQINGJIAN01-E02-CISU-JINTANG-PRIVATE_ACCOUNTS_OPENED"
  lifecycle_state: "COMPLETED_ACCOUNT_OPENING_INITIAL_ADVICE_PENDING_ALLOCATION"
  location: "觀止／後院帳務區"
  time: "榴月一日下午"

  participants:
    - "顧青簡"
    - "辭歲"
    - "錦棠"
    - "白御行"
    - "潘金蓮／觀止近場帳務人員"
    - "杜蘅"
    - "程守拙"

  route_financial_advisers:
    du_heng:
      name: "杜蘅"
      gender: "女"
      age_band: "約三十餘"
      specialty:
        - "大客戶帳務"
        - "存款與流動性"
        - "現金配置"
        - "房產支出"
        - "定息安排"
      style: "偏保守"
      status: "ROUTE_NPC_ONLY_NOT_CHARACTER_POOL_BASELINE"

    cheng_shouzhuo:
      name: "程守拙"
      gender: "男"
      age_band: "約四十餘"
      specialty:
        - "商路借貸"
        - "合夥"
        - "店舖分紅"
        - "資金運用"
      style: "較能承受風險，但重視近期待用資金"
      status: "ROUTE_NPC_ONLY_NOT_CHARACTER_POOL_BASELINE"

  gu_qingjian_principles:
    - "私人帳就是女人本人的帳；未經本人同意不動錢。"
    - "實際收到與應收帳款必須分列。"
    - "顧問提供選項，不替本人做最後資產決定。"

  cisu_account:
    status: "OPENED"
    account_owner: "辭歲"
    actual_received_taels: 1000000
    receivable_taels: 9800000
    investment_allocation: "NOT_DECIDED"
    discussion:
      - "杜蘅詢問辭歲希望保留多少生活用錢／流動資金。"
      - "辭歲沒有被迫把巨款立即投入任何產品。"

  jintang_account:
    status: "OPENED"
    account_owner: "錦棠"
    actual_received_taels: 300000
    receivable_taels: 450000
    investment_allocation: "NOT_DECIDED"
    discussion:
      - "程守拙詢問未來約三個月的預期支出。"
      - "錦棠提出衣物等支出；白希補充訓練、人員與公開露面相關支出。"
      - "程守拙提醒近三個月可能要用的錢，不宜全部鎖進一年期 3% 定存。"

  banter_not_accounting:
    - "潘金蓮笑稱顧問把她平常做的事講得像學問；顧青簡回『妳可以做到，但她們不能把妳每天帶回家』。"
```

---

# 4｜ZHANG-LIHUA01-E01｜張麗華午後自然醒來回到公共區域

```yaml
ZHANG_LIHUA_AFTERNOON:
  event_id: "ZHANG-LIHUA01-E01-NATURAL_WAKE_AFTER_HANGOVER"
  event_axis_state: "CONFIRMED"

  confirmed:
    - "張麗華於榴月一日下午自然醒來，前一日上午早段仍睡之狀態至此正常解除。"
    - "她因前夜飲酒仍帶宿醉狀態，但已可自行下樓活動。"
    - "她在後院帳務場看到正在開私人帳戶，詢問開的是什麼；李師師以『銀行』玩笑回應。"
    - "潘金蓮提醒張麗華仍需在之後查看房間整修。"

  anti_regression:
    - "V3.6-R2 早段禁止張麗華無時間推進提早出現之鎖，到本日下午自然醒來事件後解除。"
```

---

# 5｜LIPINGER01-E01｜白宅房舍入住時點：先建、後進門

```yaml
LI_PINGER_WHITE_HOUSE_DECISION:
  event_id: "LIPINGER01-E01-BUILD_NOW_FORMAL_MOVE_AFTER_XIMEN_IDENTITY_CLEAR"
  event_axis_state: "CONFIRMED_PERSONAL_DECISION"

  white_yuxing_information:
    - "白御行告知李瓶兒：白宅設計已替她保留未來房／院，李師師知情並按如夫人同級規格設計。"
    - "白御行詢問她希望白宅建成後直接入住，或等西門慶法律／身份問題清乾淨再正式進門。"

  li_pinger_decision:
    - "房／院可以現在設計、建造；她希望自己參與家具與生活細節選擇。"
    - "在西門慶相關法律身份、婚姻／身籍、嫁妝文件等問題真正清理完成前，她不正式搬入白宅。"
    - "她希望等自己真正從西門家法律／文件關係中出來後，再親自收拾搬家；那一天才算她認定的『進門』。"
    - "她不希望第一次正式入住仍被『她是不是西門家的人』這層陰影纏住。"

  pre_move_belongings:
    - "正式進門前，她希望可先放少量自己的箱子、衣物、茶具等，使空間逐步成為自己的地方。"
    - "本輪後續家具討論已按可先配置／預備之方向進行；正式搬入仍未發生。"

  title_boundary:
    - "如夫人同級房舍是建築／待遇規格，不自動創造或覆寫正式名分。"
```

---

# 6｜LIPINGER01-E02｜家具自行選、白御行報銷

```yaml
LI_PINGER_FURNITURE:
  event_id: "LIPINGER01-E02-FURNITURE_SELF_SELECT_WHITE_REIMBURSE"
  event_axis_state: "ACTIVE_SELECTION_NOT_PURCHASED_YET"

  confirmed:
    - "白御行明確告知：潘金蓮的白宅租建框架不包含全套家具。"
    - "李瓶兒的家具由她本人挑選／購置。"
    - "價格與帳單交給白御行，由白御行報銷。"

  li_pinger_initial_preferences:
    - "較大、舒服的床"
    - "較軟寢具"
    - "衣櫃"
    - "梳妝台"
    - "窗邊小榻"
    - "小茶桌"
    - "可替白御行日後物件留一處櫃／位置"

  banter:
    - "春梅笑稱白御行的東西最後可能會慢慢佔領整個房間；屬玩笑，不是財產轉移。"
```

---

# 7｜LIPINGER01-E03｜掌櫃分紅作私人嫁妝、顧青簡開戶

```yaml
LI_PINGER_PRIVATE_ACCOUNT:
  event_id: "LIPINGER01-E03-MANAGER_DIVIDEND_DOWRY_PRIVATE_ACCOUNT"
  event_axis_state: "ACCOUNT_NAME_ESTABLISHED_FUNDING_AMOUNT_UNKNOWN"

  confirmed:
    - "白御行告知李瓶兒：本次觀止掌櫃分紅屬她自己掙得，可視為她自己的嫁妝。"
    - "白御行建議她找顧青簡開自己的私人帳。"
    - "李瓶兒主動到後院對顧青簡說：『我，觀止掌櫃分紅。我要開自己的戶。』"
    - "她向顧青簡明示戶名『李瓶兒』，並把這筆掌櫃分紅定義為自己的嫁妝。"
    - "顧青簡已開始／建立李瓶兒私人戶名記錄。"

  account_state:
    owner: "李瓶兒"
    name_recorded: true
    exact_manager_dividend_taels: "UNKNOWN_NOT_FIXED_IN_CURRENT_RECORD"
    first_deposit_amount: "UNKNOWN"
    allocation: "NOT_DECIDED"

  property_separation:
    - "李瓶兒明確區分：她的掌櫃分紅／嫁妝不是拿來替白宅家具買單。"
    - "白宅家具依白御行先前承諾，仍由白御行報銷。"
```

---

# 8｜FUXIANG01-E01｜浮香小館：設計偏好與家具選購

```yaml
FUXIANG_PAVILION_AFTERNOON:
  event_id: "FUXIANG01-E01-PAVILION_DESIGN_FURNITURE_SELECTION"
  event_axis_state: "ACTIVE_DESIGN_NOT_BUILT"

  context:
    - "浮香因前夜彈琴，榴月一日下午較晚才醒，手指有些疲／疼。"

  white_yuxing_information:
    - "白御行告知她：她先前要求的小館／小屋會與白宅工程一起規劃，李師師已被告知。"
    - "觀止十日歇業期間，她可休息並自行看設計／選家具。"

  fuxiang_design_preferences:
    - "小而完整"
    - "有自己的外門，也可從內部與觀止相通"
    - "放琴處需乾燥"
    - "窗不要正對牆"
    - "整體看起來要像『浮香住的地方』，不是『某個男人養外室的附屬院』"

  furniture:
    selection_by: "浮香本人"
    payer: "白御行報銷"
    delivery: "待建成後由店家送達"
    candidate_items:
      - "床"
      - "椅"
      - "桌"
      - "琴架"
      - "櫃"
      - "屏風"
      - "燈具"
    fixed_budget: "NONE_SET"

  relation_event:
    - "白御行離開前輕吻浮香並叫她『懶豬』，讓她繼續睡。"
    - "浮香接受當下親近、輕推回應並以帳單玩笑反擊；沒有因此新增永久關係承諾。"
```

---

# 9｜HONGXIU01-E01｜聽雨閣私人琴局：白御行安靜留下

```yaml
HONGXIU_PRIVATE_QIN_SCENE:
  event_id: "HONGXIU01-E01-TINGYU_PRIVATE_QIN_QUIET_COMPANY"
  event_axis_state: "COMPLETED_AFTERNOON_SCENE"
  location: "聽雨閣／紅袖私人房"

  entry:
    - "白御行敲門，自稱事情做完、無處可去，聽見琴聲想厚著臉皮蹭免費音樂廳。"
    - "紅袖起初只開一小段門，自行判斷後才讓白御行進房。"

  hongxiu_conditions:
    - "不點曲"
    - "不要求侍酒"
    - "紅袖自己想彈什麼就彈什麼"
    - "她可以隨時停"

  relation_statement:
    - "紅袖坦白：另一個活人在房裡確實『有一點』礙事，因為會呼吸、移動、聽到錯音。"
    - "她又明示白御行今天尚算可忍，因為他沒有不停問曲名、評價或表演『懂紅袖』。"
    - "她承認有時房裡有一個安靜的人，比過度寂靜好；知道對方在即可，不必不停說話。"

  relation_delta:
    - "紅袖首次較清楚接受白御行作為不需要她管理／表演的安靜在場者。"
    - "此為關係距離變化，不等於戀愛、性同意或承諾。"
```

---

# 10｜HONGXIU01-E02｜摸手、掌心貼臉與即時同意事件

```yaml
HONGXIU_HAND_CONTACT:
  event_id: "HONGXIU01-E02-HAND_TOUCH_CHEEK_CONTACT"
  event_axis_state: "COMPLETED_CONSENSUAL_NONSEXUAL_INTIMACY"

  permission:
    - "白御行明問：今天既不可能發生性行為，紅袖是否願意讓他摸手。"
    - "紅袖明示『手可以，就摸手』；並保留隨時抽回手的權利。"

  player_action:
    - "白御行拿起紅袖的手，慢慢觸摸練琴留下的繭、舊傷與較纖細的部位。"
    - "遇到紅袖舊傷處有本能縮動時，白御行放輕動作。"
    - "最後白御行把紅袖的手放到自己臉頰，再主動放回。"

  hongxiu_response:
    - "紅袖在掌心貼上白御行臉頰時沒有抽回。"
    - "她後來明示：若白御行事前直接問『可不可以把妳的手放我臉上』，她可能會拒絕；但剛才當下她沒有想拿回來。"
    - "她沒有反向撫摸白御行臉頰；『紅袖輕撫白御行臉頰』不是客觀事件。"

  banter_boundary:
    - "白御行以『是我的臉摸妳的手』辯稱未犯規；紅袖補了身體任何部位主動碰她手都算摸的玩笑規則。"
    - "此玩笑不改變原本即時同意事實。"
```

---

# 11｜HONGXIU01-E03｜白御行在紅袖房內睡著、紅袖未趕走

```yaml
HONGXIU_SLEEP_SCENE:
  event_id: "HONGXIU01-E03-WHITE_FALLS_ASLEEP_HONGXIU_LETS_HIM_REST"
  event_axis_state: "COMPLETED"

  confirmed:
    - "白御行在紅袖房內繼續安靜待著並自然睡著。"
    - "紅袖發現後沒有立即叫醒或趕走白御行。"
    - "她一度把琴聲放輕；之後停止彈琴，自己在窗邊活動／看東西。"
    - "白御行睡過一段午後時間，至接近傍晚才由紅袖以手指輕戳額頭叫醒。"
    - "精確睡眠時長未固化；只確認為午後至傍晚的一段明顯時間。"

  hongxiu_statement:
    - "紅袖明示白御行睡著以後很安靜，比醒著少問、少算價格、少鑽規矩。"
    - "她最後主動允許白御行醒後再坐一會兒，之後兩人一起出房吃晚飯。"

  relation_delta:
    - "此事件實際推進了紅袖先前所說『讓我習慣你』之方向，但是否降價仍只有紅袖本人能決定。"
```

---

# 12｜HONGXIU01-E04｜五十萬特殊一夜門檻與反向價格尺

```yaml
HONGXIU_PRICE_RULER:
  event_id: "HONGXIU01-E04-500K_REVERSE_PRICE_RULER"
  event_axis_state: "ACTIVE_PRIVATE_RELATION_METRIC"

  context:
    - "白御行與紅袖談到辭歲 12,000,000、錦棠 5,000,000 的巨額成交後，詢問紅袖是否曾想過『忍一晚換一輩子自由』。"
    - "紅袖承認自己有想過，羨慕的核心是隔日醒來就擁有足以改變人生的資產，不是單純羨慕性交本身。"

  current_hypothetical_threshold:
    amount_taels: 500000
    applies_to: "現在的紅袖與白御行之間，若白御行把『只談一晚』當成特殊交易提出時，紅袖願意真正坐下來認真考慮／談的門檻"
    not_posted_price: true
    not_contract: true
    not_current_consent: true
    not_guaranteed_sex_if_paid: true

  hongxiu_scale_examples:
    100000: "NO"
    200000: "視為太瘋／仍不足"
    300000: "可能讓她想一夜"
    500000: "可坐下來談"
    hated_person_even_5000000: "仍可能拒絕／叫對方走"

  reverse_ruler_game:
    rule:
      - "白御行提出：未來若關係距離縮短，五十萬可由紅袖自己逐步往下調；數字越低，代表她越少需要把錢當成靠近的理由。"
      - "紅袖接受此私人『尺』的遊戲。"
      - "只有紅袖本人可以調低；白御行不得自行宣告進度／折扣。"
      - "紅袖若被惹煩，也可以把數字調高。"
      - "就算某日到 40 兩，也不代表白御行自動取得性權利；當日仍由紅袖自己決定。"
      - "若某日是紅袖本人先想要白御行，錢可能失去意義甚至變成 0；這也不是對未來的預先同意。"

  false_rumor_888:
    amount_taels: 888
    status: "WHITE_YUXING_PROPOSED_CREDIBLE_FAKE_RUMOR_PRICE_ONLY"
    rule:
      - "八百／八百八十八源自白御行故意拿低價氣紅袖與討吉利的玩笑。"
      - "後續白御行指出 888 兩比 888 萬更像真八卦，因數字落在旁人可能相信的區間。"
      - "紅袖沒有以 888 兩成交、沒有把私人尺降到 888、沒有公開掛牌。"

  anti_regression:
    - "五十萬是關係／特殊交易私下尺，不是『紅袖身價』。"
    - "不得把 888 兩寫成真實成交價、正式掛牌價或紅袖同意價。"
```

---

# 13｜HONGXIU01-E05｜清倌語義反污染鎖

```yaml
HONGXIU_QINGGUAN_SEMANTIC_LOCK:
  authority: "PLAYER_GM_CORRECTION_CONFIRMED_IN_SCENE"

  confirmed_rule:
    - "觀止『清倌／紅倌』描述當前服務／營業位置，不等於處女／非處女標籤。"
    - "人物可以已出閣、拍賣過、有性經驗，仍在當前服務結構中是清倌。"
    - "出閣是歷史事件；當前清倌／紅倌是另一條軸。"

  hongxiu_specific:
    - "本輪『現在的紅袖若只拍一晚』是現況特殊一夜交易的假設，不是第一次出閣／破身拍賣。"

  forbidden_inference:
    - "不得因紅袖目前為清倌推導她是處女、從未出閣、從未拍賣或從未有成人經驗。"
```

---

# 14｜HONGXIU01-E06｜兩條縮短距離方向

```yaml
HONGXIU_CLOSENESS_DIRECTIONS:
  event_id: "HONGXIU01-E06-TWO_WAYS_TO_LOWER_DISTANCE"
  event_axis_state: "ACTIVE_RELATION_GUIDE_NOT_PROMISE"

  direction_1:
    name: "讓我習慣你"
    meaning:
      - "不是天天纏，而是成為一個紅袖不必管理的安靜存在。"
      - "她可以彈錯、沉默、心情差，不需要白御行替她開導／分析／表演理解。"
      - "若同處一個時辰後她才忽然想起白御行還在，代表距離可能縮短。"

  direction_2:
    name: "讓我有一次是真的想找你"
    meaning:
      - "目前多數是白御行向紅袖移動。"
      - "若有一天紅袖自己想喝酒、有人陪、出去走走或房間太安靜，並主動派人找白御行，這會是更明顯的靠近。"

  collision_rule:
    - "紅袖承認自己有可能故意挑白御行正在張麗華房裡等時機叫人找他，只為看他選誰。"
    - "雙方後來校正：紅袖主動找白御行，不等於白御行必須立刻拋下張麗華、李師師、李瓶兒或其他既有承諾來證明優先。"
    - "白御行若正在履行既有承諾，可先明確回覆已收到，之後再來。"
    - "若紅袖刻意製造衝突測試，白御行不能立即到場，不應因此被拿來單方面加價。"
    - "紅袖明示：若她真有一天主動踏出找白御行那一步，即使他不能立即來，也不要把那一步當作沒發生。"
```

---

# 15｜HONGXIU01-E07｜十日賭局、三擊掌與白御行立即提前認輸

```yaml
HONGXIU_TEN_DAY_BET:
  event_id: "HONGXIU01-E07-TEN_DAY_INITIATION_BET_IMMEDIATE_WHITE_CONCESSION"
  event_axis_state: "RESOLVED_HONGXIU_WON_BY_WHITE_VOLUNTARY_CONCESSION"

  setup:
    - "白御行盤點自己過往賭約後邀紅袖下注。"
    - "紅袖提出用她是否在十日整修期內主動找白御行作勝負軸。"

  final_pre_clap_terms:
    hongxiu_loses_if:
      - "十日整修結束前，紅袖不是因公事、不是被別人叫、不是順路，而是自己真的想見白御行，並主動派人去找他。"
    if_hongxiu_loses:
      - "重新開業當晚、人最多的大堂，紅袖需當眾喊：『白御行，我想你。』"
      - "不得在後面加『去死』『才怪』『想你死』『想你把帳付了』或其他把原意翻掉的後綴。"
    if_hongxiu_wins:
      - "白御行欠紅袖一次召喚／叫來。"
      - "若白御行當時正處理已答應他人的事，不必立刻拋下；但需回覆已收到，並在第一個可來的空檔前往。"
      - "該召喚不自動授予紅袖替白御行決定成人行為、契約或不可逆承諾的權力。"
    anti_cheat:
      - "白御行不得靠叫人假報自己出事等造假方式逼紅袖主動找。"

  formation:
    - "白御行與紅袖以三擊掌正式成立賭約。"

  immediate_resolution:
    - "三擊掌成立後不久，白御行主動公開宣布提前認輸。"
    - "紅袖接受白御行自願認輸。"
    - "因此十日觀察賭局當場結束，不再需要等十日結果。"

  outcome:
    winner: "紅袖"
    loser: "白御行"
    hongxiu_public_shout_obligation: "NOT_TRIGGERED"
    hongxiu_call_right: "ACTIVE_ONE_TIME"
    price_ruler_change: "NONE"

  interpretation_boundary:
    - "白御行後來明示：他認為『紅袖主動叫他來一次』本身像獎勵，因此故意提前認輸。"
    - "紅袖承認自己贏得召喚權，並保留何時使用的決定權。"
    - "賭局裡紅袖反覆念出『白御行，我想你』是確認／複述賭約條款，不是當日真實告白或已履行未觸發的公開懲罰。"
```

---

# 16｜DINNER01-E01｜紅袖一起出房、留在公共晚飯桌

```yaml
HONGXIU_PUBLIC_DINNER:
  event_id: "DINNER01-E01-HONGXIU_STAYS_WITH_GROUP"
  event_axis_state: "COMPLETED_SOCIAL_DELTA"

  confirmed:
    - "白御行睡醒後與紅袖一起離開聽雨閣去吃晚飯。"
    - "紅袖本來擔心兩人一起出房會引起八卦；春梅已從鞋／位置知道白御行在她房內睡著。"
    - "白御行勸紅袖別總躲房裡，有空多出來和大家聊天／聽八卦。"
    - "紅袖回應自己不是討厭大家，只是外頭太吵；十日歇業沒有普通客，偶爾出來坐可以。"
    - "紅袖本晚確實沒有立刻回房，而是留在公共桌與眾人一起吃飯、聊天。"

  relation_to_group:
    - "紅袖與觀止內部群體之公共參與度本夜上升；這是行為增量，不是人格基線被改成外向。"
```

---

# 17｜RUMOR01-E01｜紅娘留門真相與『扶牆』假戰報分軸

```yaml
HONGNIANG_OLD_RUMOR_CLARIFICATION:
  event_id: "RUMOR01-E01-HONGNIANG_DECOY_REALITY_VS_FAKE_VICTORY_REPORT"
  event_axis_state: "HISTORICAL_CLARIFICATION_CONFIRMED_IN_CURRENT_PUBLIC_TABLE"

  actual_historical_event:
    - "當時白御行曾授意白紅伶在大堂散布『紅娘要讓白總白嫖／全套』等煙幕。"
    - "紅娘回房後確實整理房間、備茶、留門，並等過白御行。"
    - "白御行當夜沒有進紅娘房；而是去浮香房，與浮香發生已在 HOT V3.3 固化的自願成人親密並同床過夜。"
    - "因此紅娘與白御行當夜實際沒有發生性行為、沒有免費全套、沒有白御行在她房留宿。"

  hongniang_public_spin:
    - "紅娘為搶回面子／敘事，後續曾公開吹出『白總睡了紅娘』『白嫖』『早上扶牆離開』等勝利戰報版本。"
    - "紅娘本人在本夜重新回想並承認這是她故意放大的假戰報，不是客觀事件。"

  rumor_lesson:
    - "眾人以此討論八卦如何在反覆轉述中讓講的人自己也混淆版本。"
    - "八卦／人物自述／實際事件必須分軸；假的講久不會自動成真。"
```

---

# 18｜SHISHI-WAGER01-E01｜李師師舊賭局彩頭：白御行拒收，禁止事後重寫

```yaml
LI_SHISHI_OLD_WAGER_PRIZE:
  origin:
    source_hot: "HOT V3.2"
    original_bet_result: "白御行後續已獲李師師承認勝出"
    original_prize:
      - "白御行可指定李師師替他做一件『李師師本人可以自願答應』的事。"
      - "原約不得藉賭約強迫李師師做不願意的事或替第三人作主。"

  current_collection_attempt:
    - "本夜白御行清點舊賭債時重新翻到此彩頭。"
    - "白御行指出：若只有李師師本來就願意做的事才能指定，則實際收債時可被無限以『不願意』擋回，彩頭缺乏實質賭債價值。"
    - "收債過程已走到破局後，李師師曾試圖提出『可拒絕兩次、第三件必須選一件兌』等新版補救。"
    - "白御行明示拒絕此事後修約，認為賭局已走到破局，事後掀桌重開沒有賭品。"
    - "李師師接受此批評，撤回新版補救。"

  final_state:
    wager_win_history: "PRESERVED_WHITE_WIN"
    original_prize: "WHITE_REFUSED_TO_ACCEPT_AS_SUBSTANTIVE_PRIZE"
    replacement_prize: "NONE"
    retroactive_rewrite: "FORBIDDEN"
    redeemed: false
    outstanding_claim: "CLOSED_BY_WHITE_REFUSAL_NOT_REISSUED"

  accounting_sentence:
    - "可概括為：白御行確實贏過該賭局，但本夜認為李師師原開彩頭缺乏實質賭債價值，因此拒收；李師師不得事後以新版條款改寫原局。"
```

---

# 19｜SHISHI-NIGHT01-E01｜李師師本夜成人意願與『回家再算』未決

```yaml
LI_SHISHI_CURRENT_NIGHT_INTENT:
  event_id: "SHISHI-NIGHT01-E01-CURRENT_WILLINGNESS_SEPARATE_FROM_OLD_WAGER"
  event_axis_state: "CURRENT_WILLINGNESS_STATED_NOT_EXECUTED"

  confirmed:
    - "在舊賭債爭議過程中，李師師曾直接明示：本夜她本人願意與白御行發生成人親密。"
    - "她明示此意願不依賴那張已被白御行拒收的舊彩頭。"
    - "後來白御行重整玩法時表示：『李師師你跟我的我們回家算。』"

  current_status:
    adult_event_completed: false
    location: "NOT_YET_PLAYED"
    later_willingness: "MUST_BE_CHECKED_IF_EVENT_CONTINUES; CURRENT_STATEMENT_IS_NOT_PERMANENT_BLANKET_CONSENT"
    hongniang_not_required: true

  anti_regression:
    - "不得把『今晚願意』寫成已發生。"
    - "不得因舊賭債拒收就自動取消李師師本夜另外明示過的個人意願；兩軸分開。"
```

---

# 20｜HONGNIANG-SIDEBET01-E02｜原一次三人局賭債正式換約並清零

```yaml
HONGNIANG_SIDE_BET_SWAP:
  origin:
    source_hot: "HOT V3.4"
    old_debt:
      - "紅娘因白御行贏下第二局免費床側賭而欠一次、免費、與李師師搭成包含白御行的成年人三人親密局。"
      - "原債執行時李師師仍需本人願意；紅娘與李師師各自保留當下界線。"
    status_before_swap: "PENDING"

  current_night_pre_swap:
    - "紅娘本夜一度明示自己認輸、願意在今晚兌原側賭。"
    - "白御行先後提出大堂公開、紅娘房開放等場地玩法；紅娘與李師師沒有因此給出對全觀止公開圍觀的空白授權。"

  white_yuxing_swap_offer:
    - "白御行後來主動表示：紅娘可以不用來陪原三人局。"
    - "改為將紅娘房門扇與窗扇拆掉十日，重新開業當日上午再裝回。"

  hongniang_acceptance:
    - "紅娘本人考慮後明示接受換債。"
    - "她確認一旦換約，原一次三人局即清掉，白御行不得再用原側賭追債。"

  replacement_terms:
    duration: "TEN_DAYS_DURING_CURRENT_CLOSURE"
    remove:
      - "紅娘房門扇"
      - "紅娘房窗扇"
    do_not_remove:
      - "牆"
      - "門框／窗框等結構框架"
    privacy_support:
      - "需提供厚簾等可遮蔽方式。"
      - "紅娘若某晚要真正封閉，可有臨時遮板。"
      - "上述遮蔽物屬居住／隱私輔助，不得被解讀成換約取消。"
    cost:
      payer: "白御行"
      includes:
        - "拆除工錢"
        - "簾／臨時遮板材料"
        - "重新安裝"
    restore_deadline: "重新開業當日上午"

  final_debt_state:
    old_three_person_debt: "CLEARED_AND_CANCELLED_BY_MUTUAL_SWAP"
    replacement_room_term: "ACTIVE"
    cannot_double_collect: true
```

---

# 21｜HONGNIANG-ROOM01-E01｜十兩加班、門窗當夜實拆

```yaml
HONGNIANG_ROOM_REMOVAL:
  event_id: "HONGNIANG-ROOM01-E01-DOOR_WINDOW_REMOVED_TEN_TAEL_OVERTIME"
  event_axis_state: "PARTIALLY_EXECUTED_REPLACEMENT_DEBT"
  time: "榴月一日夜／夜宵後"

  payment:
    overtime_taels: 10
    payer: "白御行"
    handler: "三十二娘轉交／安排木工"
    not_sanshierniang_private_loss: true

  execution:
    - "木工在紅娘本人再次確認『拆』後開始作業。"
    - "門扇已完整卸下並移走／靠置，沒有砸毀。"
    - "窗扇已卸下。"
    - "門框、窗框、牆體保持不動。"

  hongniang_present:
    - "紅娘本人到場監工並再次聲明牆不可拆。"

  consequence:
    - "紅娘房在當晚已形成明顯開放的門洞／窗洞，夜風可直接進入。"
    - "此開放狀態源自換約，不等於紅娘對任何人自動開放進房、觀看或成人服務。"
```

---

# 22｜HONGNIANG-ROOM01-E02｜屏風『送修』改為本人同意保養十日

```yaml
HONGNIANG_SCREEN_REMOVAL:
  event_id: "HONGNIANG-ROOM01-E02-SCREEN_MAINTENANCE_TEN_DAYS"
  event_axis_state: "REMOVED_BY_OWNER_CONSENT"

  trigger:
    - "白御行指稱紅娘房床前屏風『壞了』，要求木工拿回去修十日。"

  inspection:
    - "木工現場查看後，沒有確認屏風實際損壞。"
    - "紅娘本人亦查看並否認屏風已壞。"

  hongniang_decision:
    - "紅娘後來自願同意將屏風搬走十日，法位為『保養』而非修理已壞物。"
    - "她接受門、窗、屏風十日都不在原位，並明示床不准搬。"

  execution:
    - "木工已將屏風抬走。"

  restore:
    target: "十日後／重新開業前與房間恢復時一併送回"
    exact_work: "MAINTENANCE_NOT_DAMAGE_REPAIR"

  anti_regression:
    - "不得把白御行一句『壞了』直接升格成屏風真的壞。"
```

---

# 23｜HONGNIANG-ROOM01-E03｜開放房間不等於『無限量帝皇服務』

```yaml
HONGNIANG_ROOM_ACCESS_BOUNDARY:
  confirmed:
    - "紅娘房門扇／窗扇十日拆除，不等於白御行取得替紅娘向外招客、許諾觀看或許諾成人服務的權力。"
    - "紅娘曾接受『若九幽帝皇有膽、有錢、有本事，可以來找紅娘本人談』作為她自己能接受的假設性說法。"
    - "白御行提過『十日不關門窗、歡迎皇帝客、無限量供應』；紅娘明確沒有授權其中『歡迎／無限量供應』為她的服務承諾。"

  not_executed:
    - "截至本 HOT，白御行沒有實際向九幽發布正式招客公告。"
    - "沒有花錢找二十人念咒。"
    - "沒有召回李隆基。"
    - "沒有召來嬴政／劉邦。"
    - "沒有任何新皇帝因本輪玩笑進入紅娘房。"

  service_rule:
    - "即使未來有人因八卦／消息來找紅娘，是否見、是否進房、收多少、做什麼仍由紅娘本人現場決定。"
```

---

# 24｜ZHAO-ROKUJO01-E02｜趙受益邀六條逛汴京夜集

```yaml
ZHAO_ROKUJO_NIGHT_MARKET:
  event_id: "ZHAO-ROKUJO01-E02-BIANJING_NIGHT_MARKET_OUTING"
  event_axis_state: "ACTIVE_OFFSITE_OUTING"

  table_context:
    - "白御行提醒趙受益：六條來自的生活環境與汴京夜生活／飲食選擇差異很大；若真想靠近她，可以帶她接觸汴京夜集與不同吃食。"
    - "趙受益一開始嘴硬否認『追人』，後來在眾人起鬨下以『好，我追』收掉爭辯；此句帶明顯桌上玩笑成分，不單獨升格成正式愛情宣告。"

  action:
    - "白御行直接催趙受益去找六條，帶她逛夜集。"
    - "趙受益實際離桌，去六條處敲門。"
    - "他邀六條在天黑後一起出去走走／看看汴京夜市。"
    - "六條理解『晚上出去』對她並非理所當然；趙受益用汴京夜裡仍有燈、吃食、賣物等方式說明。"
    - "趙受益最後以『我想帶妳去看看』收掉白御行／食物策略的痕跡。"
    - "六條回房加披外衣後，自主答應『走吧』。"
    - "兩人已一起離開觀止進入汴京夜集。"

  current_status:
    sex_event: "NONE_NEW_IN_THIS_OUTING_YET"
    romance_status: "NO_NEW_FORMAL_RELATION_CONCLUSION"
    return: "NOT_YET_OBSERVED"

  anti_regression:
    - "不得把『帶她去吃／逛夜市』自動寫成追求成功、戀愛、約會承諾或後續性行為。"
```

---

# 25｜NIGHTSNACK01-E01｜全觀止夜宵：白御行付款、三十二娘訂餐

```yaml
GUANZHI_NIGHT_SNACK:
  event_id: "NIGHTSNACK01-E01-WHOLE_GUANZHI_INTERNAL_NIGHT_SNACK"
  event_axis_state: "COMPLETED_FIRST_CLOSURE_NIGHT_SOCIAL_EVENT"

  trigger:
    - "趙受益與六條外出後，白御行想起沒叫他帶點心，轉而讓三十二娘替全觀止訂夜宵。"
    - "白御行指出觀止眾人習慣夜生活／夜間營業，突然歇業十日，晚上容易不習慣。"

  order:
    payer: "白御行"
    organiser: "三十二娘"
    scope:
      - "觀止內部人員"
      - "姑娘"
      - "帳房／必要內部人員"
      - "受訓女子"
    excluded_by_default:
      - "非觀止成員之木工等外部整修人員，除非另有安排"

  food_style:
    - "甜／鹹混合"
    - "熱湯"
    - "肉餅"
    - "鹹酥點心"
    - "蜜煎果子"
    - "軟糕等"
    - "分批送達，避免全冷"

  completion:
    - "第一批與後續夜宵已送達，眾人已實際分食。"
    - "夜宵本身使原本歇業後容易各自回房的人多留在公共區域一段時間。"
```

---

# 26｜TRAINEE01-E01｜受訓女子加入夜宵與公共問答

```yaml
TRAINEE_SOCIAL_INTEGRATION:
  event_id: "TRAINEE01-E01-NIGHT_SNACK_QA_WITH_SENIORS"
  event_axis_state: "COMPLETED_SOCIAL_DELTA"

  white_yuxing_instruction:
    - "白御行要求把年輕受訓女子也叫過來，利用十日歇業拉近與觀止既有人員的距離。"
    - "潘金蓮對跑腿人員說明：今晚叫她們來是吃夜宵，不是來伺候人；可自己找位置坐。"

  initial_state:
    - "受訓女子剛到時仍明顯拘束，傾向靠牆、行禮或保持距離。"

  social_change:
    - "紅娘、浮香、李師師、錦棠、白喜、春梅等陸續以聊天／回答問題方式讓場面鬆動。"
    - "部分受訓女子開始敢抱怨訓練、問客人、帳務、走秀、手痛、回嘴、感情等實際問題。"
    - "到夜宵時，已有人敢與紅娘搶點心、直接向資深人物提問。"

  no_baseline_rewrite:
    - "此夜拉近距離不等於階序取消、所有人變成朋友或受訓規矩失效。"
```

---

# 27｜TRAINEE01-E02｜白御行『不平等但至少不欺負女人』發言與現場修正

```yaml
WHITE_YUXING_GUANZHI_STATEMENT:
  event_id: "TRAINEE01-E02-NOT_EQUAL_BUT_DO_NOT_BULLY_WOMEN_STATEMENT"
  axis: "PLAYER_SPEECH_AND_GROUP_DISCUSSION_NOT_WORLD_CONSTITUTION"

  player_statement:
    - "白御行對受訓女子說：觀止不是一個給女人平等的地方，但至少是這個世界裡不欺負女人的地方；要好好珍惜。"

  trainee_challenge:
    - "有受訓女子直接追問：掌櫃會罵、訓練會累、做不好會被退、規矩也不是她們定的，這些算不算欺負。"

  group_response:
    - "春梅區分『不平等／有階序』與『任意欺負』不是同一件事。"
    - "潘金蓮明示做生意有規矩與淘汰，但不能因女人窮、賣身或弱勢就把她當牲口。"
    - "李師師把原則落到實際：涉及身子、錢、契、名字的事至少要有帳、有來源、有人能說明誰有權作主。"
    - "紅袖指出『至少有帳／有人問發生什麼』比抽象『不欺負』更準。"
    - "春梅提醒受訓女子：珍惜不等於什麼都不敢講，具體指出哪裡不對才有用。"

  status_boundary:
    - "本段是人物／玩家對觀止實際運作的理解與宣言，不自動升格為新主程序條文或世界憲法。"
```

---

# 28｜TRAINEE01-E03｜公開問答的實務內容

```yaml
TRAINEE_QA_HARD_NOTES:
  event_axis_state: "COMPLETED_DIALOGUE_EVENT"

  hongniang:
    - "對自稱有錢的客人：不要只看嘴，也不要自己武斷判定沒錢；看點單、付款、同行、誰認得、帳房是否認。"
    - "對一直摸手等越界行為：人物自己不想就可抽回／明講；對方是否願意付費不會自動抹掉本人界線。"

  pan_jinlian:
    - "第一次見面的客人要求『下次一起算』不行；熟客仍看帳；越有名也越要記帳。"
    - "以朱厚照 12,000,000 欠單作為『名聲大仍要有帳』的笑例。"

  li_shishi:
    - "不擅長說話時，不必急著變成話很多的人；先分辨客人要被捧、要接話、還是只是不想一個人。"

  hongxiu:
    - "分辨客人是真想知道曲子，還是只在找話講；不要把每句都當考題。"

  jintang:
    - "過去六百兩與後來五百萬都是自身歷史的一部分；新的身價／事件不抹除舊經歷，舊經歷也不必控制現在。"

  baixi:
    - "走秀錯一步不要立刻停；不停走，有些觀眾只會以為本來如此。"

  fuxiang:
    - "彈琴手痛時要休息；硬撐到不能練反而可能多休幾天。"

  springmei:
    - "掌櫃罵人時要不要回嘴，先看自己有沒有道理；不是鼓勵無條件頂撞。"

  relationship_question:
    - "有人問如果真的喜歡上一個客人怎麼辦。"
    - "潘金蓮先提醒要搞清楚對方究竟是不是只會對不同女人重複說『我只喜歡妳』。"
    - "紅袖補充可分辨自己喜歡的是那個人，還是喜歡對方來找自己時的那個自己。"

  no_training_manual_promotion:
    - "上述為當晚人物回答與經驗分享，不自動成為觀止正式教材／強制 SOP。"
```

---

# 29｜PAN-SUQING01-E02｜五萬初步和解在受訓桌被公開提及

```yaml
PAN_SUQING_PUBLIC_MENTION:
  event_id: "PAN-SUQING01-E02-50000_PRELIMINARY_SETTLEMENT_MENTIONED_AT_NIGHT_TABLE"
  event_axis_state: "PUBLIC_INTERNAL_MENTION"

  trigger:
    - "白御行拿李師師『身子／錢／契／名字至少要有帳』的話反問潘金蓮，提到她是否因此賠蘇清五萬。"

  corrected_pan_position:
    - "潘金蓮承認：五萬線已談到初步和解。"
    - "她區分這不是包拯／官府判她五萬，而是她與蘇清之民事和解。"
    - "她沒有把初步和解說成已全額付款。"

  knowledge_delta:
    - "當時在公共夜宵／問答桌近場的受訓女子與觀止成員，至少知道『蘇清可就舊帳與掌櫃談到五萬初步和解』這件事。"
```

---

# 30｜RUMOR01-E02｜本夜八卦教訓：合理假話比荒唐假話更容易活

```yaml
RUMOR_DYNAMICS_NIGHT:
  axis: "GROUP_DISCUSSION_AND_RUMOR_MECHANICS_NOT_OBJECTIVE_EVENT"

  confirmed_discussion:
    - "眾人以紅娘扶牆假戰報、紅袖房內睡覺／摸手等事件討論八卦如何繁殖。"
    - "白御行提出：假八卦若數字／細節過度荒唐，反而沒人信；落在合理區間才容易被轉述。"
    - "紅袖承認 888 兩這類數字作為假消息，比 888 萬更可能讓旁人相信。"

  save_rule:
    - "可保存『八卦曾被這樣談』，不可保存八卦內容本身為世界硬事實。"
    - "紅袖本人否認 888 兩成交，不得把『越否認越像真的』當成客觀證明。"
```

---

# 31｜夜間人物與關係增量

```yaml
RELATION_DELTAS:
  hongxiu_white_yuxing:
    previous: "有私下琴局／互相試探；關係未定"
    current:
      - "紅袖接受白御行進聽雨閣作安靜陪伴者。"
      - "紅袖明示可摸手；白御行摸到琴繭／舊傷，並把她手掌貼自己臉頰；紅袖當下沒有抽回。"
      - "白御行在她房內睡過午後一段時間；紅袖沒有趕走，至傍晚才叫醒。"
      - "紅袖願與白御行一起出房、在公共桌留下吃飯聊天。"
      - "五十萬反向價格尺正式成為兩人私下關係遊戲，但沒有成交／成人同意。"
      - "紅袖目前持有對白御行的一次召喚權。"
      - "紅袖仍可尖銳、會測試、會不爽，不得把本夜靠近洗成成熟無爭議關係。"

  hongxiu_guanzhi_group:
    current:
      - "十日歇業第一夜，紅袖主動留在公共桌較久，願意聽／參與八卦與受訓女子問答。"
      - "這是一次社交增量，不是永久變成外向人物。"

  zhao_shouyi_rokujo:
    previous:
      - "前夜雙方自願性行為已成立；關係仍未定。"
    current:
      - "趙受益主動邀六條夜間出門看汴京夜集，六條自願接受。"
      - "尚未形成戀愛、排他或正式伴侶關係。"

  hongniang_white_yuxing:
    current:
      - "紅娘原一次三人局賭債已由本人同意改為房門／窗扇十日拆除並清掉原債。"
      - "紅娘知道白御行可能有後手但仍明示『成交就是成交』，賭品／換約承認成立。"
      - "房間開放本身不等於紅娘成人同意或對外招客。"

  li_shishi_white_yuxing:
    current:
      - "舊賭局勝負仍承認白御行贏；原彩頭被白御行拒收，不得事後重寫。"
      - "李師師本夜另有一次當下成人意願明示，與舊彩頭分軸；尚未執行。"

  li_pinger_white_yuxing:
    current:
      - "李瓶兒願意讓白宅房舍先建、自己參與選物，但正式『進門』要等西門慶法律／身份／嫁妝問題清乾淨。"
      - "她把自己的掌櫃分紅視為私人嫁妝，不拿來替白御行承諾報銷的家具買單。"

  fuxiang_white_yuxing:
    current:
      - "浮香小館作為她自己的生活空間要求更明確；她接受白御行報銷家具並保留自己的選擇權。"
      - "下午輕吻屬當下親近，沒有新增身份承諾。"
```

---

# 32｜帳務、契約、賭約與換約硬狀態

```yaml
LEDGER_AND_CONTRACT_STATE:
  cisu_private_account:
    status: "OPENED"
    actual_taels: 1000000
    receivable_taels: 9800000
    allocation: "NOT_DECIDED"

  jintang_private_account:
    status: "OPENED"
    actual_taels: 300000
    receivable_taels: 450000
    allocation: "NOT_DECIDED"

  li_pinger_private_account:
    status: "NAME_ESTABLISHED_ACCOUNT_OPENING_IN_EFFECT"
    exact_dividend_taels: "UNKNOWN"
    initial_deposit: "UNKNOWN"

  pan_suqing_50000:
    status: "PRELIMINARY_CIVIL_SETTLEMENT_REACHED"
    exact_payment_completion: "UNKNOWN"
    court_judgment: false

  hongxiu_500000_ruler:
    current_amount_taels: 500000
    type: "PRIVATE_RELATION_AND_HYPOTHETICAL_SPECIAL_ONE_NIGHT_CONSIDERATION_THRESHOLD"
    posted_price: false
    contract: false
    current_consent: false
    can_change_by: "紅袖本人"

  hongxiu_call_right:
    owner: "紅袖"
    debtor: "白御行"
    quantity: 1
    status: "ACTIVE_UNREDEEMED"
    origin: "十日主動找人賭局三擊掌後，白御行自願提前認輸"
    adult_entitlement: false

  li_shishi_old_wager_prize:
    result_history: "WHITE_WON"
    original_prize: "指定李師師做一件她本人可以自願答應之事"
    white_acceptance: "REFUSED_AS_NON_SUBSTANTIVE"
    replacement: "NONE"
    outstanding: false

  hongniang_old_three_person_sidebet:
    status: "CLEARED_BY_MUTUAL_SWAP"
    cannot_be_collected_again: true

  hongniang_room_swap:
    status: "ACTIVE_PARTIALLY_EXECUTED"
    duration_days: 10
    door_leaf: "REMOVED"
    window_sashes: "REMOVED"
    screen: "REMOVED_BY_SEPARATE_OWNER_MAINTENANCE_CONSENT"
    structural_frames: "INTACT"
    restore: "重新開業當日上午"
    payer: "白御行"
    overtime_paid_taels: 10

  li_shishi_current_night_willingness:
    status: "STATED_NOT_EXECUTED"
    contractual_debt: false
    must_reconfirm_if_scene_resumes_after_material_change: true
```

---

# 33｜知情範圍與來源

```yaml
KNOWLEDGE_SCOPE:
  internal_public_table:
    - "紅袖房內白御行睡著、摸手等部分事實已在晚飯桌被當事人／春梅等以八卦形式談到；具體版本有真有假，不能把所有笑話合併成一條真相。"
    - "紅袖 888 假價在當桌多人面前被談過，但不是正式報價／成交。"
    - "紅袖十日賭局與三擊掌、白御行當場提前認輸，有滿桌見證。"
    - "因此紅袖持有一次召喚權屬桌上多人可知。"
    - "潘金蓮×蘇清五萬初步和解被夜宵桌近場多人聽到。"
    - "紅娘原側賭換成拆門窗十日、木工當夜實拆，有多人可見。"

  private_or_limited:
    - "紅袖五十萬反向價格尺最初是白御行與紅袖私下談成的關係尺；後續部分內容在飯桌玩笑中被帶出，但不等於整樓知道完整規則。"
    - "紅袖掌心貼白御行臉頰的精確主動／被動細節，由兩名當事人最清楚；桌上只透過他們後來說法得知。"

  account_limited:
    - "辭歲、錦棠、李瓶兒各自私人帳戶細節由本人、顧青簡、必要商會／帳務人員知情。"
    - " exact investment allocation 尚未決定，因此沒有任何人可合法宣稱已替她們投資。"

  offsite_unknown:
    - "趙受益＋六條離樓後夜集細節，截至本 HOT 觀止內人物沒有新的直接觀察來源。"
```

---

# 34｜仍活躍但未解事項

```yaml
OPEN_THREADS:
  high_priority:
    - id: "HONGNIANG-ROOM01-OPEN-01"
      state: "ACTIVE_TEN_DAY_ROOM_SWAP"
      item: "紅娘房無門扇／窗扇／屏風十日之實際居住、隱私、八卦與夜間後果；厚簾／臨時遮板是否已裝尚未顯影。"

    - id: "HONGXIU-CALL01-OPEN-01"
      state: "ACTIVE_ONE_TIME_RIGHT"
      item: "紅袖何時使用一次召喚權；使用時白御行若已有承諾，依既定回覆／第一空檔規則處理。"

    - id: "ZHAO-ROKUJO01-OPEN-01"
      state: "OFFSITE_ACTIVE"
      item: "趙受益與六條本夜汴京夜集後續、吃了什麼、何時回來、關係是否有新事件；全部尚未顯影。"

    - id: "SHISHI-NIGHT01-OPEN-01"
      state: "CURRENT_NIGHT_UNRESOLVED"
      item: "李師師曾明示本夜願意與白御行成人親密；白御行後說『我們回家算』，但本 HOT 前尚未執行。"

    - id: "ACCOUNT01-OPEN-01"
      state: "ACTIVE"
      item: "拍賣剩餘 14,000,000 兩仍需在原定十日清算期內完成；辭歲 9,800,000、錦棠 450,000 應收尚未入帳。"

    - id: "LIPINGER-DIVIDEND01-OPEN-01"
      state: "UNRESOLVED_ACCOUNT_AMOUNT"
      item: "李瓶兒本次掌櫃分紅／嫁妝 exact 數字及首次入帳金額尚未固化。"

    - id: "PAN-SUQING01-OPEN-01"
      state: "PRELIMINARY_SETTLEMENT_NOT_FULLY_CLOSED"
      item: "潘金蓮×蘇清五萬初步和解之付款完成度、付款方式與最後法律／帳務收尾尚未固化。"

    - id: "RENOVATION01-OPEN-01"
      state: "ACTIVE_TEN_DAY_PROJECT"
      item: "大觀樓內裝、白玉池、房間分級與十日後重新開業工程。"

    - id: "WHITEHOUSE01-OPEN-01"
      state: "DESIGN_ACTIVE_BUILD_LATER"
      item: "李師師十日內完成白宅施工設計；李瓶兒房／院與浮香小館落圖、家具採買與後續施工。"

    - id: "XIMENQING01-OPEN-01"
      state: "OFFSCREEN_ACTIVE"
      item: "西門慶案正式裁判、李瓶兒身份／嫁妝清理、蘇清二十八日私人約是否觸發。"

  medium_priority:
    - "辭歲、錦棠各自實際採何種存款／投資比例。"
    - "紅袖五十萬尺未變；是否、何時由紅袖本人調整沒有預定時間。"
    - "紅袖在公共區域的參與是否延續，不應被導演當作必然。"
    - "夜宵與受訓女子問答是否成為十日歇業期間的其他晚間活動，尚未制度化。"

  explicitly_closed:
    - "紅娘原一次三人局側賭：已換約清零，不再是未決成人賭債。"
    - "李師師原『指定一件她願意做的事』彩頭：白御行已拒收，沒有新版替代債。"
    - "紅袖十日主動找人賭局：白御行已提前認輸，賭局已結束；不用再跑十日勝負判定。"
```

---

# 35｜禁止回歸／防污染

```yaml
ANTI_REGRESSION:
  calendar:
    - "目前仍是榴月一日夜。"
    - "不得因夜宵／散場直接跳到榴月二日，除非自然推進一夜。"

  accounts:
    - "辭歲私人帳已開；錦棠私人帳已開。"
    - "不得退回『下午顧青簡尚未到／帳戶尚未開』。"
    - "李瓶兒戶名已建立； exact 分紅／首次存入金額未知。"
    - "辭歲／錦棠的實收與應收仍要分列，不得把 17,000,000 全部寫成現金已到觀止。"

  pan_suqing:
    - "五萬線已達初步和解，不得再退回單純索賠／潘完全未認。"
    - "初步和解 != 官府判決。"
    - "初步和解 != 五萬已全額實付；付款完成度未知。"
    - "不得與白御行×蘇清的條件式二十八日私人約混在一起。"

  hongxiu_qingguan:
    - "清倌 != 處女。"
    - "不得因紅袖清倌身份推導未出閣／未拍賣／無性經驗。"

  hongxiu_price_ruler:
    - "五十萬是私下反向價格尺／特殊一夜認真考慮門檻，不是公開報價。"
    - "付五十萬不自動取得性行為。"
    - "888 兩是假八卦價，沒有成交。"
    - "只有紅袖本人可調整這把尺。"

  hongxiu_bet:
    - "十日賭局已因白御行自願提前認輸而結束。"
    - "紅袖不需要在重新開業大堂喊『白御行，我想你』；該懲罰未觸發。"
    - "紅袖目前持有一次召喚權。"
    - "賭約形成時紅袖多次念出『白御行，我想你』只是在念條款，不得固化成當日告白。"

  hongxiu_hand:
    - "事件是白御行把紅袖的手放自己臉上，紅袖沒有抽回；不是紅袖主動撫摸白御行臉。"
    - "紅袖同意摸手不等於其他身體接觸 blanket 同意。"

  hongniang_old_rumor:
    - "舊日『白總睡紅娘／白嫖／扶牆』是紅娘為搶敘事吹出的假戰報，不是實際成人事件。"
    - "實際是白御行沒有進紅娘房，當夜去了浮香房。"

  li_shishi_wager:
    - "不得把李師師事後提出的拒兩次／第三件必兌等修補條款寫進原賭約。"
    - "白御行已拒收原彩頭；沒有新補償券。"
    - "白御行贏過原局的歷史仍保留，不得因彩頭拒收抹掉勝負。"

  hongniang_sidebet:
    - "原一次三人局債務已經換約清掉。"
    - "不得下一串再讓紅娘被迫履行同一舊三人局。"
    - "紅娘房門窗十日換約才是目前有效債務。"

  hongniang_room:
    - "門扇、窗扇已拆；牆與結構框架沒拆。"
    - "屏風沒有被確認壞；是紅娘本人同意送保養十日。"
    - "房間物理開放 != 對外成人服務、圍觀、進房、無限量帝皇供應之同意。"
    - "白御行沒有實際向九幽公告無限量帝皇服務。"

  zhao_rokujo:
    - "兩人已一起去逛夜集，但沒有回程／新成人事件／戀愛承諾資料。"
    - "不得替六條決定她喜歡什麼食物或因吃好東西就愛上趙受益。"

  night_snack:
    - "夜宵與問答是第一晚的自發內部活動，尚未制度化成十日晚間固定課程。"
    - "受訓女子距離縮短 != 階序取消、全部成為正式姑娘或取得同等權限。"

  adult_axis:
    - "李師師本夜有當時明示意願，但尚未發生；如後續時間／情境有變，仍以人物當下決定為準。"
    - "任何人物的前一刻同意不得被 SAVE 轉成永久同意。"
```

---

# 36｜理火接關治理備忘【非世界事實】

```yaml
DIRECTOR_RUNTIME_GUARD:
  document_level_status: "ACTIVE_FOR_NEXT_STORY_TURN"
  deployment_claim: false

  failure_samples_this_slice:
    - id: "HONGXIU_BET_PREEMPTIVE_SAFETY_COLLAPSE"
      symptom:
        - "導演曾在紅袖形成賭局前，先用『不能拿人物／性當賭注』式預防性語氣壓掉成人／關係 PATH。"
      gm_ruling:
        - "玩家明示該段被污染、太保守，要求重跑。"
      correction:
        - "重跑後由紅袖自己依人格、勝負心、五十萬尺與關係位置決定賭法。"
      save_effect:
        - "污染版賭局不進世界；重跑後三擊掌／提前認輸版本才是硬事件。"

    - id: "PAN_SUQING_STALE_STATE_REGRESSION"
      symptom:
        - "導演一度引用早期『五萬只是索賠』舊狀態，否認榴月一日上午已形成的初步和解。"
      gm_correction:
        - "玩家補充：上午潘金蓮算掌櫃分紅、蘇清出來那段已達五萬初步和解。"
      save_effect:
        - "以最新事件覆蓋舊狀態；錯誤否認不進世界。"

    - id: "LI_SHISHI_WAGER_RETROACTIVE_REWRITE"
      symptom:
        - "收債破局後，導演／師師曾提出新版『拒絕兩次、第三件必選』企圖讓舊彩頭重新可兌。"
      player_ruling:
        - "白御行拒絕，指出這是掀桌重來、缺乏賭品。"
      save_effect:
        - "新版作廢；原賭局勝負保留，原彩頭被白御行拒收。"

  semantic_guards:
    - "清倌／紅倌軸與處女／出閣歷史軸分離。"
    - "價格、成人同意、關係距離、八卦與正式交易分軸。"
    - "人物當下願意不等於賭債強制；賭債成立也不能替第三人預先同意。"
    - "物理空間開放不等於身體／服務開放。"
    - "玩家可以設局、提賭、提換約；NPC是否接受由人物自行回答。"

  next_story_binding:
    - "玩家投下一個變數，導演讓整個世界回答它。"
    - "角色只能從自己的位置活著。"
    - "誰知道，要有來源。"
    - "態度變化，要有事件。"
    - "關係變化，要有因果。"
    - "未知保持未知；不能因玩笑好笑就升格世界事實。"

  save_boundary:
    - "本節只屬導演治理／接關備忘，不取得世界事實權、人物人格權或關係權。"
```

---

# 37｜直接接關摘要

```yaml
DIRECT_RESUME:
  scene_anchor:
    date: "理火三年榴月一日"
    time: "夜；夜宵後"
    player_position: "觀止內"
    event_status: "歇業第一夜內部聚會已散／將散；紅娘房換約已開始執行"

  immediate_world_state:
    - "辭歲與錦棠私人帳戶已由顧青簡實際開立；投資配置尚未決定。"
    - "李瓶兒私人戶名已建立； exact 掌櫃分紅／入帳額未知。"
    - "李瓶兒白宅房舍先建、正式進門等西門慶身份／嫁妝等問題清完；家具她自己選、白御行報銷。"
    - "浮香小館仍是設計中；家具由浮香自己挑、白御行報銷。"
    - "紅袖與白御行完成聽雨閣安靜陪伴、摸手／掌心貼臉與房內午睡事件；關係距離有可見增量，但沒有成人成交。"
    - "紅袖五十萬反向價格尺仍是五十萬；888 只是假八卦價。"
    - "紅袖持有一次召喚白御行的權利；十日賭局已因白御行提前認輸結束。"
    - "李師師舊賭局彩頭被白御行拒收，沒有新版替代；但李師師本夜另曾明示當下願意與白御行成人親密，尚未執行。"
    - "紅娘原一次三人局側賭已換約清零；有效新債為房門／窗扇拆除十日。"
    - "紅娘房門扇與窗扇已拆，屏風也由紅娘本人同意送保養十日；牆／框架未拆。"
    - "10 兩木工加班費由白御行支付。"
    - "趙受益與六條已一起外出逛汴京夜集，尚未回樓。"
    - "全觀止已完成歇業第一夜夜宵與受訓女子公共問答；內部距離有所縮短。"
    - "潘金蓮×蘇清五萬民事線已達初步和解；付款完成度未知。"

  next_turn_rule:
    - "若玩家說繼續，從同夜自然推進一個節點。"
    - "不要把紅袖十日賭局重新跑一次。"
    - "不要再向紅娘追原三人局賭債。"
    - "不要讓九幽皇帝因玩笑自動出現。"
    - "不要把趙受益＋六條夜集自動收斂成戀愛／性。"
    - "不要把李師師本夜意願寫成已完成成人事件；需等實際場景。"
```

---

# 38｜HOT V3.7 結論

```yaml
HOT_V3_7_CONCLUSION:
  status: "VALID_HOT_SAVE"
  current_world_time: "理火三年榴月一日夜"

  hard_results:
    - "顧青簡已帶杜蘅、程守拙到觀止；辭歲與錦棠私人帳戶已實際開立，資產配置未定。"
    - "張麗華下午自然醒來，上午早段睡眠鎖已正常解除。"
    - "李瓶兒決定白宅房舍先建、正式進門等西門慶法律／身份／嫁妝問題清楚；家具自行選購、白御行報銷；私人戶名已建立。"
    - "浮香小館設計偏好與家具選購權更明確；白御行承諾報銷。"
    - "紅袖接受白御行在聽雨閣安靜陪伴、摸手，並在掌心貼臉時沒有抽回；白御行其後在她房睡至傍晚，紅袖沒有趕走。"
    - "紅袖五十萬反向價格尺成立，仍為 500,000；888 兩只是假八卦價。"
    - "紅袖清倌語義鎖成立：清倌不是處女標籤。"
    - "紅袖十日主動找人賭局三擊掌成立後，白御行立即提前認輸；紅袖取得一次召喚權，公開喊『白御行，我想你』的輸局義務未觸發。"
    - "紅娘舊日『白嫖／扶牆』為假戰報；實際當夜白御行未進紅娘房而去了浮香房。"
    - "李師師舊賭局彩頭被白御行拒收，事後修約作廢；原勝負歷史保留。"
    - "紅娘原一次三人局側賭已經雙方同意換約清掉；有效替代為紅娘房門／窗扇拆十日。"
    - "紅娘房門扇、窗扇已於榴月一日夜實際拆除；屏風另經紅娘本人同意送保養十日；白御行支付 10 兩加班費。"
    - "觀止歇業第一夜全樓夜宵與受訓女子問答已完成，內部公共距離縮短。"
    - "趙受益已邀六條逛汴京夜集，六條自願接受，二人截至本 HOT 尚未回樓。"
    - "潘金蓮×蘇清五萬民事線已達初步和解，付款完成度未知。"

  next_valid_hot_version: "V3.8"
  master_merge: "NOT_PERFORMED"
  character_pool_update: "NOT_PERFORMED"
  runtime_patch_merge: "NOT_PERFORMED"
```


<!-- PROMOTED_SOURCE_END: 觀止青樓_白御行線_HOT_SAVE_V3.7_榴月一日夜_辭錦瓶兒開戶_紅袖五十萬尺與召喚權_夜宵問答_紅娘門窗十日換債版.md -->


<!-- PROMOTED_SOURCE_BEGIN: 觀止青樓_白御行線_HOT_SAVE_V3.8_榴月二日白日_楊玉環荔枝_桂蕙沈萬三回歸_師師晨間補考_定陶存款朱明長債與曹州案版.md -->
# SOURCE ARCHIVE｜觀止青樓_白御行線_HOT_SAVE_V3.8_榴月二日白日_楊玉環荔枝_桂蕙沈萬三回歸_師師晨間補考_定陶存款朱明長債與曹州案版.md

**SHA-256：** `c5280c4e1ef117d7846d2275b39a63101050427e5a8c8c9c8abaf09769422518`

> **法位：本檔 E93–E98 固化來源。** 原 HOT 內的 CURRENT_SCENE／HOLD 只代表當時快照；不得覆寫本 MASTER 截止或 V4.1–V4.4 疊加層。

# 觀止青樓｜白御行線 HOT SAVE V3.8
## 理火三年榴月二日白日｜趙受益六條夜集返樓 × 楊玉環白玉池與荔枝 × 李師師晨間補考 × 桂姐蕙蓮沈萬三回歸 × 定陶存款／朱明長債／票據信用校正版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V3_8_LIU02_DAY_YANG_YUHUAN_LYCHEE_SHISHI_MORNING_DINGTAO_CREDIT_DEBT"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V3.8"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V11.0-R2"
  character_source: "觀止人物卡池_LCAPG_V2.3_李清照趙受益錦棠顧青簡增補_薛濤魚玄機暫定入場_正式版.md"

  story_time_span:
    start: "HOT V3.7 後／理火三年榴月一日深夜"
    current: "理火三年榴月二日白日"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AT_DINGTAO_ASSOCIATION_AFTER_ACCOUNTING_AND_CASE_REVIEW_BEFORE_RETURN_TO_GUANZHI"

  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V3.7_榴月一日夜_辭錦瓶兒開戶_紅袖五十萬尺與召喚權_夜宵問答_紅娘門窗十日換債版.md"
  previous_hot_sha256: "a354e50c0d35a76c91e469303172da7dbef06ab4f14add436383eadc52c5e50a"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md"
  long_term_master_sha256: "0149362b4128d62d947d4ffbcc618003913b1cad7052d57fe5b3f84f8f05084f"

  experimental_overlays:
    performance_patch:
      file: "觀止青樓_PATCH_風月角色表演與接戲能力_V0.1-EXP_獨立試跑未併主系統.md"
      status: "INDEPENDENT_TRIAL_OVERLAY_NOT_MERGED"
    analyzer_exit_patch:
      file: "觀止青樓_PATCH_分析器退場_重大升階定義_SCOPED_REACTIVATION_顯影反污染_V0.1-EXP.md"
      status: "GUANZHI_SPECIFIC_OPTIONAL_EXPERIMENTAL_OVERLAY_NOT_MERGED"
    lihuo_environment_patch:
      file: "理火環境_PATCH_V0.1.md"
      status: "REFERENCE_OPTIONAL_EXPERIMENTAL_OVERLAY_NOT_MERGED"

  save_scope:
    - "趙受益與六條榴月一日深夜夜集回樓、栗子禮與無新增戀愛／成人結果界線"
    - "白御行與李師師栗子夜談、舊賭局與『回家再算』分軸、夜間玩法失敗與榴月二日晨間成人補考"
    - "楊玉環因白玉池邀請自主到觀止、張麗華陪同、紅娘驚嚇事件、客房留宿與翌日白明礬臨時隨行安排"
    - "楊玉環對家族得勢責任之本人場內表述、荔枝承諾、小龍蝦／甲殼素保存構想與未執行邊界"
    - "桂姐、宋蕙蓮明朝線餐飲考察之 GM 校正、二人與沈萬三榴月二日帶第一批玉荷包荔枝返觀止"
    - "沈萬三、桂姐、宋蕙蓮受邀作為白玉池後續使用者；皇帝先前已用過白玉池之順序校正"
    - "六條晨間下樓吃荔枝；觀止自動翻譯器設定回歸"
    - "榴月二日白御行返定陶商會，顧青簡完成案件／帳務盤點與多次玩家校正"
    - "辭歲／錦棠拍賣款之存戶端、商會資產端、朱明債權端重新分層；十日清算障眼／信用窗口與首批三百萬橋接週轉模型"
    - "五年五分定存推銷指令、朱明短債若來不及可談轉成年息十分長債、票據信用擴張方向"
    - "烤鹽→廣源→西門慶→高衙內→高俅→蔡京大案鏈之舊案狀態校正；曹州假印案仍為商會當前 ACTIVE 案"
    - "京師女性貼身衣物／奢侈品旗艦專案交常煒副會長執行"
```

---

# 0｜提交法位、來源與本輪反污染

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V3.7_榴月一日夜_辭錦瓶兒開戶_紅袖五十萬尺與召喚權_夜宵問答_紅娘門窗十日換債版.md"
    role: "本檔直接前置 HOT；V3.7 及以前有效硬狀態全部繼承，除本檔明示更新／補正者"

  master_archive:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md"
    role: "截至 HOT V3.4 之長期固化；HOT V3.5、V3.6-R2、V3.7 與本 V3.8 依序作較新合法疊加"

  current_character_source:
    file: "觀止人物卡池_LCAPG_V2.3_李清照趙受益錦棠顧青簡增補_薛濤魚玄機暫定入場_正式版.md"
    role: "現行人物基線；玩家線事件仍以最新 HOT 高於跨線人物卡基線"

  current_route_conversation_commit:
    role: "HOT V3.7 後至本次 HOT SAVE 命令前之直接劇情、玩家對自身言行與世界／帳務法位之明示校正、NPC 可觀察回應、已完成成人同意事件、GM 明示設定與商會指令"

COMMIT_NOTE:
  - "本檔推進至榴月二日白日；不更新 MASTER、不修改人物卡池、不修改主程序、不合併 EXP PATCH。"
  - "本輪玩家多次明示校正舊 SAVE／導演的帳務理解；校正只改變帳務法位與商會風險歸屬，不回溯否認已觀察到的首批現銀展示。"
  - "辭歲與錦棠在定陶商會的客戶端餘額，與定陶商會對朱明／乾隆等付款方持有的資產／債權分軸記錄。不得再把外部應收直接顯示成姑娘『還沒收到所以不能用』。"
  - "十日清算期是外部交割／信用展示窗口，不等於商會必須等十日才給客戶帳戶可用餘額。"
  - "胡椒、香料、蘇木、跨朝代套利、五千萬回報等仍是策略／投資假設，不是已成交收益。"
  - "朱明年息十分長債是白御行授權的談判方向／若短期不足之替代方案，尚未取得朱家正式接受。"
  - "辭歲五年五分定存是待顧青簡推銷的商會產品，不得保存成辭歲已簽五百萬定存。"
  - "本輪曾出現『明礬是誰／新人物』錯誤；玩家明示前文作廢、非理火。正確為既有白家四女之一白明礬。"
  - "本輪曾出現六條日語原句＋春梅翻譯；玩家明示觀止有自動翻譯器，該語言障礙處理作廢。"
  - "本輪對紅娘是否喜歡白御行之分析屬 DISCUSSION／人物解讀，不取得紅娘戀愛事實權。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年榴月二日"
  time: "白日／早餐後，精確時刻未知"
  primary_location: "定陶商會／總會辦公與帳務區"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  player:
    name: "白御行"
    current_position: "定陶商會內；完成與顧青簡之帳務、案件與專案分工盤點後"
    current_state:
      - "今晨已在觀止與李師師完成早餐前私人場景。"
      - "已在觀止早餐桌與沈萬三、桂姐、宋蕙蓮、楊玉環、六條、潘金蓮、李師師等互動。"
      - "早餐後主動回定陶商會一趟。"
      - "已完成本輪商會核心帳務法位校正與案件清單校正。"
      - "已表達沒有其他事情即可回去；最終返觀止路程尚未在本輪重新演出。"

  guanzhi_background:
    ten_day_closure_day: 2
    ordinary_public_business: "CLOSED"
    internal_operations: "ACTIVE"
    hongniang_room_open_structure: "ACTIVE_TEN_DAY_DOOR_WINDOW_SCREEN_REMOVAL"
    yang_yuhuan: "仍為觀止自主來去之客；今晨仍在觀止活動範圍，是否稍後離開由本人決定"
    shen_wansan_gui_song: "已返觀止；白玉池後續使用邀請已成立，實際完整入池過程未演出"

  direct_resume_point:
    - "下一幕可從白御行離開定陶商會、返回觀止途中或抵達觀止後接起。"
    - "若直接回觀止，可自然接楊玉環／白明礬初次正式相處、沈萬三桂姐宋蕙蓮白玉池後續、紅娘門窗十日第二日、紅袖召喚權、李師師晚間未了私人約定等。"
    - "不得把商會討論中的定存、朱明十分長債、胡椒套利寫成已簽約／已獲利。"
```

---

# 2｜HOT V3.7 繼承後仍活躍之核心狀態

```yaml
INHERITED_ACTIVE_CORE:
  ten_day_closure:
    status: "ACTIVE"
    current_day: 2
    ordinary_public_business: "CLOSED"
    internal_operations: "ACTIVE"

  hongniang_room_swap:
    status: "ACTIVE"
    door_leaf: "REMOVED"
    window_sashes: "REMOVED"
    screen: "REMOVED_FOR_MAINTENANCE"
    restore: "重新開業當日上午"
    openness_not_permission: true

  hongxiu:
    special_ruler_taels: 500000
    ruler_type: "PRIVATE_RELATION_AND_HYPOTHETICAL_SPECIAL_ONE_NIGHT_CONSIDERATION_THRESHOLD"
    posted_price: false
    contract: false
    current_consent: false
    call_right_quantity: 1
    call_right_status: "ACTIVE_UNREDEEMED"

  pan_suqing_50000:
    status: "PRELIMINARY_CIVIL_SETTLEMENT_REACHED"
    payment_completion: "UNKNOWN"

  li_pinger:
    private_account: "OPENING_EFFECTIVE"
    white_house_room: "PLANNED_AS_RUREN_LEVEL; FORMAL_MOVE_WAITS_LEGAL_IDENTITY_DOWRY_CLEANUP"

  zhao_shouyi_rokujo:
    prior_adult_event: "CONFIRMED_FROM_V3.6-R2; NO_AUTO_ROMANCE"
    night_market_status: "COMPLETED_RETURNED_TO_GUANZHI"
```

---

# 3｜ZHAO-ROKUJO02-E01｜夜集回樓與栗子禮

```yaml
NIGHT_MARKET_RETURN:
  event_id: "ZHAO-ROKUJO02-E01-NIGHT_MARKET_RETURN_CHESTNUT_GIFT"
  event_axis_state: "COMPLETED"
  time: "榴月一日深夜"

  confirmed:
    - "趙受益與六條從汴京夜集安全回到觀止。"
    - "趙受益帶回熱食／紙燈等夜市物；六條帶回一小包烤栗子。"
    - "兩人就糖糕、吃食數量與汴京夜生活互相拆台；屬日常同遊後互動。"
    - "六條因趙受益告知白御行曾提議帶她逛夜市，分幾顆栗子給白御行。"
    - "白御行收下栗子並帶去與李師師分享。"

  relationship_limits:
    - "本次夜集沒有新增成人事件。"
    - "本次夜集沒有建立戀愛、排他、婚約或第二次固定約會。"
    - "趙受益提到明日仍有可逛之處，不等於已成立下一次約會。"
```

---

# 4｜SHISHI02-E01｜栗子夜談、舊賭局分軸與『回家再算』

```yaml
SHISHI_CHESTNUT_NIGHT:
  event_id: "SHISHI02-E01-CHESTNUT_OLD_WAGER_SEPARATION"
  event_axis_state: "COMPLETED"

  confirmed:
    - "白御行與李師師分享六條帶回之栗子。"
    - "白御行以『收債』玩笑提舊賭局。"
    - "李師師與白御行均維持 V3.7 校正：舊賭局彩頭已被白御行拒收，沒有未償替代債務。"
    - "二人另有先前『回家再算』之當下私人親密意願；此軸與舊賭局分離。"
    - "白御行向李師師講述紅娘門窗拆除與相關鬧劇；兩人以夫妻／情人間玩笑互拆。"

  anti_merge:
    - "舊賭局勝負歷史 != 今晚私人親密義務。"
    - "『回家再算』是人物當下關係互動，不是可強制執行之債。"
```

---

# 5｜YANG-YUHUAN01-E01｜因白玉池邀請自主抵達觀止

```yaml
YANG_YUHUAN_ENTRY:
  event_id: "YANG-YUHUAN01-E01-WHITE_JADE_POOL_INVITATION_AND_ARRIVAL"
  event_axis_state: "COMPLETED_ENTRY_STAY_ACTIVE"
  character_status: "ROUTE_GUEST_NOT_CHARACTER_POOL_BASELINE"

  invitation:
    actual_reason:
      - "觀止有白玉池，可與華清宮不同方式試浴／看池。"
      - "來去自由；不附掛牌、契約、永久留觀止義務。"
    not_actual_reason:
      - "不是因李隆基。"
      - "不是因紅娘惡作劇。"

  preparation:
    - "白御行吩咐準備純白浴後衣袍、溫酒與剩餘熱食／栗子。"
    - "若張麗華醒著，請她陪楊玉環泡池／喝酒；張麗華當時醒著並同意陪酒。"
    - "白御行請張麗華帶楊玉環走會經過紅娘所在區域的路線。"

  arrival:
    - "一名女子到觀止詢問白玉池，自稱楊氏、玉環。"
    - "潘金蓮在前堂接待。"
    - "白御行因自己為男性客人而先避開浴池接待動線。"
    - "張麗華與楊玉環相認歷史身份，隨後帶她前往白玉池。"

  sovereignty:
    - "楊玉環是否久留、再來、與誰相處均由本人決定。"
    - "本次到場不構成人物池 admission、掛牌、觀止員工或白家關係。"
```

---

# 6｜YANG-HONGNIANG01-E01｜白衣濕髮路過與紅娘驚嚇

```yaml
HONGNIANG_SCARE_EVENT:
  event_id: "YANG-HONGNIANG01-E01-WHITE_ROBE_GHOST_SCARE"
  event_axis_state: "COMPLETED_INITIAL_SCARE"

  confirmed:
    - "張麗華帶剛沐浴、白衣、濕髮的楊玉環經過紅娘無門窗／屏風區域。"
    - "紅娘因前述鬼話、房間開放與心理預期，先把楊玉環當成鬼而高聲驚叫。"
    - "紅娘認出楊玉環與『李三郎』關係後，驚嚇／尷尬反應加劇並喊潘金蓮。"
    - "楊玉環得知紅娘與李隆基八百兩交易之部分背景，後續表達想見紅娘。"

  unknown:
    - "楊玉環與紅娘之後若有更長談話，其完整內容本輪未演出／未固化。"

  anti_inference:
    - "紅娘被嚇到 != 她怕所有鬼或對楊玉環形成永久敵意。"
    - "楊玉環想見紅娘 != 自動形成和解、友情、競爭或報復。"
```

---

# 7｜YANG-YUHUAN01-E02｜責任對談、荔枝與小龍蝦前置

```yaml
YANG_YUHUAN_PRIVATE_TALK:
  event_id: "YANG-YUHUAN01-E02-RESPONSIBILITY_LYCHEE_CRAYFISH"
  event_axis_state: "COMPLETED_TALK_FUTURE_FOOD_HOOKS_OPEN"

  responsibility_talk:
    confirmed_self_statements:
      - "楊玉環承認自己家族因她得勢，她並非完全不知家族享受特權。"
      - "被問『最初是否真的拒絕過』時，她明示最初沒有。"
      - "她當時曾把家人終於不用看人臉色、皇帝恩寵等視為自然好處；後來才更清楚權勢代價與楊國忠等人衝突。"
    limits:
      - "這是本玩家線場內自述，不升格成歷史學唯一結論。"
      - "不因此把安史之亂責任單獨推給楊玉環。"

  lychee:
    - "白御行問楊玉環是否想吃荔枝，並承諾今年第一批到時替她留幾串。"
    - "楊玉環接受；特別表示幾串即可，不需要大規模急遞，若有人也想吃可分。"
    - "她請白御行荔枝到時叫她。"

  crayfish_preservation_idea:
    - "白御行提出可吃小龍蝦，並以蝦蟹殼材料製取甲殼素／相關塗層作荔枝保鮮之構想。"
    - "楊玉環願意吃，提出可做多種口味、也想讓張麗華一起。"
    - "實際小龍蝦宴、甲殼素製備、保鮮材料完成與荔枝配送均尚未在此時發生。"
```

---

# 8｜YANG-YUHUAN01-E03｜客房留宿與白明礬翌日臨時隨行

```yaml
YANG_YUHUAN_LODGING:
  event_id: "YANG-YUHUAN01-E03-GUEST_ROOM_AND_BAI_MINGFAN_DAY_ATTENDANT"
  event_axis_state: "ACTIVE"

  lodging:
    - "潘金蓮替楊玉環安排內院乾淨上房，位置靠近張麗華，避開紅娘區域。"
    - "不是掛牌房、不是永久貴妃院、不是入觀止契約。"
    - "楊玉環本夜實際留宿，榴月二日上午仍在觀止。"

  bai_mingfan_assignment:
    identity_lock:
      name: "白明礬"
      existing_person: true
      prior_status: "白御行四名既有持契成年女下屬之一"
      specialty: "染色／布料／色差辨識等"
    player_order:
      - "榴月二日由白明礬暫時跟隨楊玉環，作隨從／引路／跑腿等支援。"
    limits:
      - "白明礬沒有被贈送給楊玉環。"
      - "不是永久調任。"
      - "楊玉環是否喜歡、信任、需要她由實際相處決定。"

  invalidated_output:
    - "任何『明礬是誰／需新建人物／不是既有人員』之輸出已被玩家明示作廢，不得回歸。"
```

---

# 9｜SHISHI02-E02｜夜間玩法失敗、真睡與榴月二日晨間補考

```yaml
SHISHI_PRIVATE_NIGHT_MORNING:
  event_id: "SHISHI02-E02-NIGHT_GAME_SLEEP_MORNING_MAKEUP"
  event_axis_state: "COMPLETED"
  time_span: "榴月一日深夜至榴月二日早餐前"

  night_game:
    - "白御行回李師師房中，二人重新進入先前『回家再算』之私人親密場。"
    - "李師師提出由她控制節奏、白御行不預判／不搶主導之玩法；白御行同意，可隨時說停。"
    - "後續轉為白御行『假裝睡著』、李師師嘗試以等待與非露骨挑逗讓他有反應的遊戲。"
    - "二人後來真的睡著直到天亮。"
    - "白御行實際睡著後，李師師停止互動；整個夜間沒有性行為完成。"

  morning_interpretation:
    - "白御行判定昨夜『不算』，稱李師師第一次履約失敗；睡著不算完成。"
    - "李師師接受昨夜玩法未完成之評價。"

  morning_makeup:
    - "榴月二日清晨，雙方再次同意進行短時間成人補考。"
    - "白御行一度以手引導李師師頭部方向；李師師立即主張由她自己控制動作。"
    - "白御行未以該引導覆蓋她的主權；其後由李師師自主選擇繼續。"
    - "二人完成一段自願成人口部性親密事件；本 SAVE 不補圖像化身體細節。"
    - "事件於早餐前結束。"

  consent_axis:
    night: "CONSENSUAL_GAME_NO_SEX_COMPLETED"
    morning: "MUTUAL_ADULT_CONSENT_COMPLETED_WITH_SHISHI_SELF_CONTROL"
    permanent_consent: false

  fulfillment_axis:
    night_special_play: "FAILED_BY_BAI_AND_ACCEPTED_AS_FAILED_BY_SHISHI"
    morning_makeup: "COMPLETED"
    exact_contractual_equivalence_to_original_phrase: "CHARACTER_PERSPECTIVE_ACCEPTED_FOR_MORNING_BANTER_NOT_FORMAL_CONTRACT"
```

---

# 10｜SHISHI-HONGXIU02-E01｜李師師同意替白御行助攻紅袖

```yaml
HONGXIU_ASSIST_INTENT:
  event_id: "SHISHI-HONGXIU02-E01-ASSIST_WITHOUT_OVERRIDE"
  event_axis_state: "ACTIVE_INTENT_NOT_EXECUTED"

  player_request:
    - "白御行明示近期想追紅袖、希望李師師幫忙助攻。"

  li_shishi_response:
    - "李師師同意在合適時機協助創造紅袖可自主靠近白御行的機會。"
    - "可採取讓出場子、減少霸佔白御行、製造自然單獨相處空間等方式。"
    - "若紅袖明顯不想，李師師不推。"
    - "李師師不替紅袖承諾性、上床、交易或愛情。"

  state:
    executed_specific_assist: "NONE_YET"
    hongxiu_call_right: "UNCHANGED_ACTIVE_UNREDEEMED"
```

---

# 11｜GM-CORRECTION02-E01｜桂姐＋宋蕙蓮明朝餐飲考察線

```yaml
GUI_SONG_MING_RESEARCH:
  event_id: "GM-CORRECTION02-E01-GUIJIE_SONGHUILIAN_MING_FOOD_RESEARCH"
  authority: "GM_EXPLICIT_CONFIRMATION"
  lifecycle_state: "ROUTE_EVENT_CONFIRMED"

  confirmed:
    - "桂姐與宋蕙蓮先前長期未出鏡，是因暫時跟沈萬三前往其明朝線做餐飲考察。"
    - "二人仍屬觀止人物，不因外出考察變成沈家所有或永久離開觀止。"
    - "考察方向可包含酒樓／食肆／茶坊／夜市／雅間散座／菜式／酒水／地方吃食與客人實際點單反應。"
    - "二人沒有因此自動取得現代餐飲管理學或沈家固定職位。"

  return_status:
    - "榴月二日清晨二人與沈萬三一同回到觀止。"
```

---

# 12｜LYCHEE02-E01｜沈萬三桂蕙帶第一批玉荷包返觀止

```yaml
MORNING_RETURN_LYCHEE:
  event_id: "LYCHEE02-E01-SHEN_GUI_SONG_RETURN_FIRST_YUHEBAO"
  event_axis_state: "COMPLETED"
  time: "榴月二日清晨"

  confirmed:
    - "沈萬三、桂姐、宋蕙蓮自明朝線／商路回到觀止。"
    - "二人帶回沈家線取得的第一批新鮮玉荷包荔枝；葉色／新鮮度足以被白御行判為正當季。"
    - "白御行梳洗後先出李師師房，到前堂與沈萬三打招呼。"
    - "白御行認出玉荷包並當場吃了兩顆。"
    - "楊玉環也取得荔枝並食用。"
    - "白御行明示這批荔枝不是自己準備的；自己昨夜只曾承諾第一批到時替她留幾串。"

  causal_note:
    - "荔枝是桂姐／宋蕙蓮／沈萬三線自行帶回，並非世界為迎合白御行承諾而預先生成的指定交付。"
    - "它恰好在翌晨抵達，形成承諾與世界物流的自然碰撞。"
```

---

# 13｜WHITE-JADE-POOL02-E01｜白玉池後續接客與順序校正

```yaml
WHITE_JADE_POOL_OPERATION:
  event_id: "WHITE-JADE-POOL02-E01-POST_EMPEROR_GUEST_USE"
  event_axis_state: "ACTIVE_OPERATIONAL"

  correction:
    - "皇帝批次先前已使用／試過白玉池。"
    - "楊玉環榴月一日夜也已實際使用。"
    - "因此沈萬三、桂姐、宋蕙蓮不是白玉池第一批正式使用者。"

  current:
    - "榴月二日上午白御行邀沈萬三、桂姐、宋蕙蓮一起去白玉池試用。"
    - "三人接受／往白玉池方向去；完整入池、洗浴與離池細節本輪未演出，不補完。"

  operation_rule:
    - "白玉池現已可在觀止十日閉門整修期間提供受控客用，不等於整間觀止恢復普通公開營業。"
```

---

# 14｜ROKUJO02-E02｜六條晨間下樓吃荔枝與自動翻譯器鎖

```yaml
ROKUJO_MORNING_LYCHEE:
  event_id: "ROKUJO02-E02-MORNING_LYCHEE"
  event_axis_state: "COMPLETED"

  confirmed:
    - "白御行想起六條尚未下樓，安排人上樓叫她來吃荔枝。"
    - "六條下樓後直接問一大早為何如此吵鬧。"
    - "楊玉環將較甜的一串／荔枝分享給六條；六條道謝並坐下吃。"
    - "眾人以趙受益拍賣當晚未出價、六條坐在旁邊等事打趣；六條沒有把這些玩笑升格成趙受益服從／所有權。"

  translation_runtime_lock:
    - "觀止存在自動翻譯器／跨語言理解機制；人物在觀止交流時通常可直接理解。"
    - "本輪任何讓六條突然只能講日文、再由春梅翻譯的輸出均作廢，不得保存為語言障礙。"
```

---

# 15｜帝皇拍賣早餐八卦之法位

```yaml
AUCTION_BREAKFAST_BANTER:
  state: "SOCIAL_RECALL_AND_BANTER"

  already_solid_prior_facts:
    - "辭歲最終 12,000,000 兩成交，得標者朱正德。"
    - "錦棠最終 5,000,000 兩成交，得標者乾隆。"
    - "李世民曾競拍錦棠至 1,000,000 兩後退出；此事已在 V3.5 固化。"
    - "李隆基後續與紅娘完成 800 兩自願成人交易；此事已在 V3.6-R2 固化。"
    - "趙光義當夜曾長時間留在李師師正式席，後自行去見李清照。"
    - "趙受益當夜與六條同席。"

  current_player_recollections_not_promoted_beyond_source:
    - "白御行早餐時回憶／宣稱李隆基在雙姝競拍均有出價、李唐兩帝都下場、趙宋當晚相對未參與雙姝終局競價。"
    - "若後續要把每一次叫價、最後剩幾名競價者升格為精確硬紀錄，需回查完整拍賣逐口叫價來源；本 HOT 不用早餐戲謔取代原始競價紀錄。"
```

---

# 16｜朱明／趙宋家主與朱明總帳 GM 校正

```yaml
DYNASTIC_ACCOUNT_AUTHORITY_CORRECTION:
  authority: "GM_EXPLICIT_CORRECTION"
  story_time_advanced: false

  zhu_ming:
    current_underworld_family_head: "朱正德／朱厚照"
    auction_debt:
      gross_taels: 12000000
      nature: "朱明全朝代／家族信用共同買單之帝皇聯誼會成交債"
      zhu_di_at_signing: "PRESENT_AND_BACKED_THE_DEAL"
      primary_bidder: "朱正德"
    correction:
      - "不得再把此單縮成朱正德個人、朱棣只旁觀且與債完全無關。"
      - "朱棣背書與朱明家族總帳法位成立；但各朝實際如何分攤／以何資產交割仍需談。"

  zhao_song:
    current_family_head: "趙受益／趙禎"
    note:
      - "趙受益已取得趙宋家主位置；不因此自動替任何個人商業案買單。"

  settlement_policy_direction:
    - "朱明債可以依各朝供給優勢談銀、貨、香料、蘇木、染料、其他可交割資產或地府收益。"
    - "白御行明示大明朱家除其所稱『大明通寶』紙鈔類低信用標的不收外，其他可談。"
    - "以貨抵債、跨朝代分攤與地府分紅沖債均需定陶商會與朱明另定估價／契約，不自動成立。"
```

---

# 17｜跨朝代胡椒／香料交易：策略而非既得收益

```yaml
CROSS_ERA_SPICE_STRATEGY:
  lifecycle_state: "STRATEGY_DISCUSSION_ACTIVE_NOT_EXECUTED"

  discussed_model:
    - "可向朱棣／永樂宣德等朱明朝代詢問三寶航海帶回之胡椒、蘇木、香料與海外貨，以商品交割／折抵部分朱明債或另行採購。"
    - "商品若在大明供給較足，可轉售至其他胡椒／香料更稀缺之朝代與高價市場。"
    - "候選市場曾談及盛唐、趙宋汴京與北方邊貿、蒙元大都／王公商隊等；均需實際驗價。"
    - "胡椒被視為高價、低重量、耐儲、易運之候選跨朝商品。"
    - "草原市場之核心賣點應以高端風味／稀缺商品而非把胡椒當作肉類主要防腐材料。"

  cisu_interest:
    - "早餐談話中辭歲對跨朝香料試單表示興趣，曾將『上限一百萬兩』視為查價後可考慮的投資授權尺度。"
    - "這不是已支付一百萬、不是保證五十倍、不是固定投資契約。"

  return_claim:
    - "白御行曾以『一百萬可能換五千萬』說明極端上行情境。"
    - "該數字是投資預測／說服語言，不是世界保證、定陶保本或沈萬三承諾。"
```

---

# 18｜DINGTAO02-E01｜白御行久違回定陶商會

```yaml
DINGTAO_RETURN:
  event_id: "DINGTAO02-E01-CHAIRMAN_RETURN"
  event_axis_state: "COMPLETED_ARRIVAL_REVIEW_CONTINUING"
  time: "榴月二日早餐後"

  confirmed:
    - "白御行早餐後離開觀止，回定陶商會／總會一趟。"
    - "近來多數商會業務由顧青簡、常煒等人送到觀止或自行按程序處理，白御行確實已有一段時間未親自回商會。"
    - "商會在會長不在時持續正常運轉；沒有因白御行缺席停止。"
    - "顧青簡以固定女性師爺／商業對接身份與白御行核對帳務、案件與未決專案。"
```

---

# 19｜DINGTAO02-E02｜拍賣款帳務法位重大校正：存戶端已到帳，外債在商會端

```yaml
AUCTION_BANKING_CORRECTION:
  event_id: "DINGTAO02-E02-DEPOSITOR_BALANCE_VS_ASSOCIATION_ASSET_CORRECTION"
  authority: "PLAYER_GM_ACCOUNTING_CORRECTION"
  event_axis_state: "ACCOUNTING_MODEL_CORRECTED"

  core_rule:
    - "對辭歲／錦棠等客戶而言，定陶商會承接拍賣交割後，其應得款可先在定陶帳上完整形成可用餘額。"
    - "客戶不用等朱家／乾隆等付款方把全額現銀一車車送齊，才算『收到』。"
    - "客戶端的存款／餘額是定陶商會對客戶的負債。"
    - "朱明／乾隆等尚待交割的款項，則是定陶商會資產端的債權／收款問題。"

  cisu:
    auction_share_taels: 10800000
    customer_view: "DINGTAO_ACCOUNT_BALANCE_TREATED_AS_ARRIVED_AND_USABLE"
    physical_cash_in_room_history:
      first_display_taels: 1000000
      status: "ACTUALLY_SHOWN_OR_MOVED_FOR_DISPLAY_FROM_PRIOR_HOT; NOT_REQUIRED_TO_STAY_IN_ROOM"
    old_save_field_correction:
      - "V3.7 的『actual 1,000,000 + receivable 9,800,000』只能解讀為外部交割／現銀到位拆分，不得再拿來限制辭歲客戶帳戶可用餘額。"

  jintang:
    auction_share_taels: 750000
    customer_view: "DINGTAO_ACCOUNT_BALANCE_TREATED_AS_ARRIVED_AND_USABLE"
    physical_cash_in_room_history:
      first_display_taels: 300000
      status: "ACTUALLY_SHOWN_OR_MOVED_FOR_DISPLAY_FROM_PRIOR_HOT; NOT_REQUIRED_TO_STAY_IN_ROOM"

  association_asset_side:
    - "未完成的皇帝／家族付款義務由定陶商會持有並管理。"
    - "定陶可催收、展期、轉長債、收息、談貨物抵債或其他合約安排；不需要把每一層催收細節轉嫁給存戶。"

  anti_regression:
    - "不得再對辭歲說『妳還有九百八十萬沒收到，所以不能存五百萬』。"
    - "正確說法是『妳在定陶帳上的錢已到，可依本人意願取用／轉帳／定存』。"
```

---

# 20｜DINGTAO02-E03｜五年五分定存產品與吸存目標

```yaml
CISU_DEPOSIT_SALES_PLAN:
  event_id: "DINGTAO02-E03-CISU_FIVE_YEAR_DEPOSIT_PITCH"
  lifecycle_state: "ORDERED_TO_PITCH_NOT_YET_ACCEPTED"

  player_direction:
    - "定陶商會不是替辭歲管錢；商會的商業目標是說服她將更多大額餘額長時間鎖定在定陶帳面不使用。"
    - "一年期產品：三分利。"
    - "五年期產品：五分利。"
    - "對辭歲主推五年五分利理財／定存方案。"

  sales_owner:
    primary: "顧青簡／定陶商會"

  current_contract_state:
    cisu_acceptance: "NOT_YET_OBSERVED"
    exact_principal: "NOT_SIGNED; 五百萬只是示例／主推尺度，不得保存成已存"
    payout_schedule: "TO_BE_FINALIZED_IN_CONTRACT; 先前討論傾向年息另入活帳"

  association_rationale:
    - "定陶真正購買的是存戶資金可長期使用的期限。"
    - "五年五分資金成本較一年三分高，但若資產端是更長期朱明債／跨朝商品，期限匹配更有價值。"
```

---

# 21｜DINGTAO02-E04｜朱明短債轉長債十分之談判授權

```yaml
ZHU_MING_DEBT_MANAGEMENT:
  event_id: "DINGTAO02-E04-ZHU_MING_SHORT_TO_LONG_DEBT_NEGOTIATION"
  lifecycle_state: "AUTHORIZED_NEGOTIATION_NOT_YET_AGREED"

  player_direction:
    - "先與朱明談原定短期收款／交割。"
    - "若短期來不及完成，定陶可提出轉為長債，按每年十分利收取。"
    - "可另談地府朱明家族分紅／紅利定期沖債。"
    - "也可在估值與雙方同意下，以各朝可用商品／資產折抵。"

  not_yet_fact:
    - "朱家尚未在本輪正式接受十分長債。"
    - "未確定本金分段、期限、單利／複利、提前還款、擔保或各朝分攤比例。"

  spread_logic:
    - "若定陶以五分成本鎖到長期存款、資產端以十分收朱明長債，可形成利差；實際淨利仍受壞帳、流動性、商品交割與其他成本影響。"
```

---

# 22｜DINGTAO02-E05｜十日清算窗口與首批三百萬橋接週轉

```yaml
TEN_DAY_SETTLEMENT_REINTERPRETATION:
  event_id: "DINGTAO02-E05-TEN_DAY_OPTICS_AND_THREE_MILLION_BRIDGE"
  authority: "PLAYER_GM_ACCOUNTING_CORRECTION"
  event_axis_state: "MODEL_CORRECTED"

  ten_day_window:
    - "十日是外部付款／交割、信用展示與市場可理解的清算窗口。"
    - "它不是定陶商會內部真的要等十天才有能力把客戶帳做完。"
    - "交易成交、定陶承接債權與客戶餘額建立可以更早完成。"

  first_three_million:
    prior_observed:
      - "首日／首批有三百萬兩級流動性被實際拿出用於展示與交割，辭歲與錦棠曾看到／拿到部分實銀。"
    corrected_financial_nature:
      - "三百萬不是定陶永久墊付出去的沉重成本。"
      - "它是短期橋接流動性與信用展示。"
      - "錦棠五百萬成交中，定陶本身取得 75% 分成／收入 3,750,000 兩；因此本次交易本身就能回補大量橋接資金。"
      - "乾隆不是向定陶借滿五百萬；只借其實際缺額。"
      - "乾隆實際缺額精確數字未在本輪給出，不得自行補算。"
      - "白御行將此理解為把稍後才回來的錦棠交易收入，提前約三日拿出去週轉。"

  redeposit_expectation:
    - "白御行判斷首批三百萬中至少約六成在持有人看過／短期使用後，可能重新存回定陶。"
    - "此為會長的流動性預測，不是已發生的次日存款結果。"

  core_model:
    - "同一筆現銀在時間錯開下可完成多次交割；定陶需要準備的是真正會離開體系的現銀，而非所有帳面負債 100% 同時堆在庫房。"
    - "不得把此模型寫成定陶可無限創造銀兩或無風險挪用客戶資產。"
```

---

# 23｜DINGTAO02-E06｜定陶票據信用擴張方向

```yaml
DINGTAO_NOTE_CREDIT:
  event_id: "DINGTAO02-E06-NOTE_ACCEPTANCE_CREDIT_EFFECT"
  lifecycle_state: "STRATEGIC_EFFECT_ACTIVE_NOT_UNIVERSALLY_COMPLETE"

  player_view:
    - "三百萬級交割信用一旦公開成立，定陶票據的市場接受度會大幅提升。"

  gu_qingjian_accounting_view:
    - "商人會看票據能否兌、能否抵帳、能否再轉給第三家。"
    - "若沈家、觀止、各分會與大商戶逐步接受，定陶票據可成為可轉讓信用工具，減少大額現銀搬運。"

  current_state:
    universal_acceptance: false
    direction: "CREDIT_EXPANSION_EXPECTED"
    anti_overclaim:
      - "『誰都會收』是會長的市場判斷／目標，不寫成所有商號已無條件接受。"
```

---

# 24｜DINGTAO02-E07｜舊案層級校正：烤鹽案不再獨立待辦

```yaml
CASE_HIERARCHY_CORRECTION:
  event_id: "DINGTAO02-E07-OLD_CASE_CHAIN_CLOSED_AS_SEPARATE"
  authority: "PLAYER_EXPLICIT_CORRECTION"
  event_axis_state: "CASE_INDEX_CORRECTED"

  chain:
    - "烤鹽案"
    - "廣源案"
    - "西門慶案"
    - "高衙內線"
    - "高俅線"
    - "蔡京／朝廷權臣大案"

  ruling:
    - "烤鹽案早已併入後續大案，只是舊帳面可能仍有未逐筆銷號紀錄。"
    - "廣源案也已作為後續大案證據／接口被吸收，不再作為定陶商會獨立 ACTIVE 待辦。"
    - "上述鏈條不能因舊檔仍寫逃犯／未結就反覆回到會長桌上。"
    - "這不代表所有國家案件細節都被粗暴視為同一件事；只是本條已實際升階／吸收之案件鏈不應再鬼打牆。"

  current_dingtao_case_list:
    active_credit_case:
      - "曹州假定陶印／冒名採辦案"
    old_chain:
      - "烤鹽／廣源／西門慶／高衙內／高俅／蔡京：不列為商會日常待辦"
```

---

# 25｜CAOZHOU02-E01｜曹州假印案當前狀態

```yaml
CAOZHOU_FAKE_SEAL_CASE:
  event_id: "CAOZHOU02-E01-CURRENT_CASE_STATUS"
  lifecycle_state: "ACTIVE"

  inherited_origin:
    - "槐月二十一日曹州程姓商人帶貨單、疑似定陶印樣拓本與破損封蠟報案。"
    - "白御行當時判定非定陶正式印，命商會按 SOP 立案內查。"

  current_update:
    - "程姓當事商人已離開京師、返回曹州做自己的生意。"
    - "證物／先前口供與聯絡線仍留在商會案件程序。"
    - "本人不是待訊、不是被拘留；需要補問可經曹州商團／聯絡方式處理。"
    - "案件本身仍 ACTIVE；冒名採辦者與假印來源尚無本輪新硬結果。"

  reporting_rule:
    - "有實質進度再向白御行回報。"
    - "沒有新結果時，不每輪以『還在查』浪費會長注意力。"
```

---

# 26｜LUXURY02-E01｜京師女性貼身衣物／奢侈品旗艦專案交常煒

```yaml
LUXURY_PROJECT_DELEGATION:
  event_id: "LUXURY02-E01-DELEGATE_TO_CHANGWEI"
  lifecycle_state: "DELEGATED_ACTIVE_PROPOSAL"

  project:
    inherited_name: "京師女性奢侈品旗艦店／貼身衣物與批發端"
    inherited_state_before: "PROPOSAL_ACTIVE_NO_SITE_SELECTED_NO_LEASE"

  player_order:
    - "白御行將內衣／女性用品專案交副會長常煒處理。"
    - "常煒可先處理選址、供貨、批發端、店面人手等一般執行。"
    - "若需要會長大額授權、品牌核心方向、重大公開活動或超出既有法位，再回報白御行。"

  current:
    vice_chair_owner: "常煒"
    site_selected: "NOT_CONFIRMED"
    lease_signed: "NOT_CONFIRMED"
```

---

# 27｜人物位置與當前可見去向

```yaml
CHARACTER_LOCATIONS_LIU02_DAY:
  white_yuxing:
    location: "定陶商會／正準備結束本次回訪"

  gu_qingjian:
    location: "定陶商會"
    task:
      - "維持曹州假印案程序"
      - "推銷辭歲五年五分定存方案"
      - "整理朱明短債／長債談判與票據信用帳務"

  changwei:
    location: "NOT_PRECISELY_OBSERVED"
    task:
      - "承接京師女性貼身衣物／奢侈品旗艦專案一般執行"

  guanzhi:
    yang_yuhuan: "榴月二日上午仍在觀止；可自由離開"
    zhang_lihua: "觀止"
    li_shishi: "觀止；早餐後日常活動"
    pan_jinlian: "觀止掌櫃線"
    hongniang: "觀止；房門窗屏風十日拆除第二日"
    hongxiu: "觀止活動範圍；召喚權未使用"
    rokujo: "觀止；今晨已下樓吃荔枝"
    zhao_shouyi: "精確晨間位置未鎖；前夜已與六條返回觀止"
    shen_wansan: "已返觀止；白玉池後續使用邀請線"
    guijie: "已返觀止；白玉池後續使用邀請線"
    song_huilian: "已返觀止；白玉池後續使用邀請線"
    bai_mingfan: "榴月二日預定／已受白御行指令暫時跟隨楊玉環；正式碰面細節待演出"
```

---

# 28｜關係、同意、交易、帳務分軸總表

```yaml
RELATION_CONSENT_LEDGER_SNAPSHOT:
  bai_shishi:
    night_game: "CONSENSUAL_NO_SEX_COMPLETED_DUE_TO_REAL_SLEEP"
    morning_makeup: "CONSENSUAL_ADULT_ORAL_INTIMACY_COMPLETED"
    shishi_self_control: true
    permanent_entitlement: false
    old_wager_debt: "NONE"
    future_private_time: "RELATIONAL_OPEN_NOT_CONTRACTUAL"

  bai_hongxiu:
    bai_stated_goal: "WANTS_TO_PURSUE_CLOSER_ADULT_RELATIONSHIP"
    hongxiu_current_consent: false
    call_right: "ONE_ACTIVE_UNREDEEMED"
    shishi_assist: "INTENT_ACTIVE_NOT_EXECUTED"

  bai_hongniang:
    romance: "NOT_ESTABLISHED"
    sexual_relation: "NOT_ESTABLISHED"
    old_three_person_debt: "CLEARED"
    room_swap: "ACTIVE"
    discussion_analysis: "NOT_WORLD_FACT"

  yang_yuhuan:
    guanzhi_status: "AUTONOMOUS_GUEST"
    prostitution_contract: "NONE"
    bai_relationship: "GUEST_HOST_FOOD_BATH_CONVERSATION; NO_ROMANCE_CONTRACT"
    li_longji_current_claim: "NO_NEW_RELATIONSHIP_SETTLEMENT_WITHIN_THIS_HOT"

  cisu:
    customer_account_balance_taels: 10800000
    five_year_deposit: "PITCH_ORDERED_NOT_SIGNED"
    spice_investment: "INTERESTED_UP_TO_PRELIMINARY_ONE_MILLION_SCALE_AFTER_DUE_DILIGENCE; NOT_FUNDED"

  jintang:
    customer_account_balance_taels: 750000
    investment_allocation: "NOT_DECIDED_IN_THIS_HOT"

  zhu_ming:
    dynasty_debt_gross_taels: 12000000
    family_account_status: "COLLECTIVE_DYNASTIC_CREDIT_OBLIGATION_GM_CONFIRMED"
    long_debt_10_percent: "NEGOTIATION_OPTION_NOT_AGREED"
```

---

# 29｜未決事項／下一輪可用鉤子

```yaml
OPEN_THREADS_V3_8:
  guanzhi:
    - id: "YANG_BAI_MINGFAN_DAY"
      state: "OPEN"
      item: "白明礬榴月二日正式跟隨楊玉環後的第一輪相處、服裝／色彩／引路需求。"
    - id: "YANG_LYCHEE_CRAYFISH"
      state: "OPEN"
      item: "楊玉環已吃到意外早到的玉荷包；小龍蝦／甲殼素保鮮構想仍未執行。"
    - id: "SHEN_GUI_SONG_WHITE_JADE_POOL"
      state: "OPEN"
      item: "沈萬三、桂姐、宋蕙蓮已接受後續試用邀請；完整使用結果未演。"
    - id: "HONGNIANG_DAY2_OPEN_ROOM"
      state: "ACTIVE"
      item: "紅娘門窗屏風拆除十日進入第二日；不得提前恢復。"
    - id: "HONGXIU_CALL_RIGHT"
      state: "ACTIVE"
      item: "紅袖仍持有一次召喚白御行之權利；李師師助攻尚未實際發生。"
    - id: "SHISHI_FUTURE_PRIVATE_TIME"
      state: "OPEN_RELATIONAL"
      item: "晨間補考已完成；晚間是否另有私人相處由人物與當日事件自然形成，非債務。"

  dingtao:
    - id: "CISU_FIVE_YEAR_DEPOSIT_PITCH"
      state: "ORDERED"
      item: "顧青簡需向辭歲推五年五分產品；辭歲是否接受、存多少由本人決定。"
    - id: "ZHU_MING_SETTLEMENT_NEGOTIATION"
      state: "OPEN"
      item: "原短期交割若不足，可談年息十分長債、地府分紅沖債、商品抵債；均未簽。"
    - id: "CROSS_ERA_SPICE_DUE_DILIGENCE"
      state: "PROPOSAL"
      item: "沈萬三若真要做胡椒／香料跨朝交易，需要先查貨源、價差、各市場容量與交割。"
    - id: "CAOZHOU_FAKE_SEAL"
      state: "ACTIVE"
      item: "程商人已返曹州；等商會查出假印／冒名採辦實質進度再報。"
    - id: "LUXURY_PROJECT_CHANGWEI"
      state: "DELEGATED"
      item: "常煒副會長承接女性貼身衣物／奢侈品旗艦專案；一般執行不需白御行逐項簽。"

  do_not_reopen:
    - "烤鹽案作為獨立商會待辦"
    - "廣源案作為獨立商會待辦"
    - "紅娘原三人局賭債"
    - "李師師舊賭局彩頭債"
    - "趙受益六條夜集回程未決"
```

---

# 30｜本輪導演／SAVE 反污染鎖

```yaml
ANTI_REGRESSION_V3_8:
  calendar:
    - "現在是榴月二日白日。"
    - "觀止十日閉門整修進入第二日。"

  translation:
    - "觀止自動翻譯器有效；不得再突然創造六條需要人工翻譯的語言障礙。"

  bai_mingfan:
    - "白明礬是既有四女之一，不是新角色。"
    - "本日只是暫時跟隨楊玉環，不是贈與或永久改主。"

  white_jade_pool:
    - "皇帝已先使用過白玉池；楊玉環也於榴月一日夜使用。"
    - "沈萬三、桂姐、宋蕙蓮只能叫後續使用者／受邀者。"

  shishi_adult_event:
    - "榴月一日夜遊戲本身沒有完成性行為；二人是真的睡著。"
    - "榴月二日晨間另有自願成人口部性親密完成。"
    - "李師師在晨間明示自己控制自己的行動；不得倒寫成被白御行強迫。"

  yang_yuhuan:
    - "楊玉環是因白玉池與自身好奇到觀止，不是被李隆基／紅娘劇情召來。"
    - "楊玉環沒有因留宿自動入人物池、掛牌、接客或與白御行形成成人關係。"

  gui_song:
    - "桂姐、宋蕙蓮此前去沈萬三明朝線做餐飲考察；不是導演遺忘造成的真空。"
    - "已於榴月二日清晨與沈萬三返觀止。"

  finance:
    - "辭歲 10,800,000／錦棠 750,000 對客戶端是定陶帳上可用餘額；外部付款未齊是商會資產端問題。"
    - "不得再把 V3.7 的 9,800,000／450,000 外部應收直接寫成姑娘不能用的個人未收款。"
    - "十日是外部交割／信用窗口，不是客戶餘額等十日才成立。"
    - "三百萬是橋接週轉與信用展示，不是永久墊款。"
    - "乾隆只借成交缺額，精確缺額未知；不得自行寫成借滿五百萬。"
    - "辭歲五年五分尚未簽。"
    - "朱明年息十分長債尚未簽。"
    - "胡椒五十倍／五千萬不是保證收益。"

  cases:
    - "烤鹽→廣源→西門慶→高衙內→高俅→蔡京鏈已升階／吸收；烤鹽與廣源不再作商會獨立待辦。"
    - "商會目前需持續回報的主要案件只剩曹州假印案；有進度再說。"

  discussion_not_world:
    - "紅娘對白御行『又討厭又喜歡』是導演分析框架，不是紅娘本人已承認戀愛。"
```

---

# 31｜直接接關摘要

```yaml
DIRECT_RESUME:
  scene_anchor:
    date: "理火三年榴月二日"
    time: "白日／早餐後"
    player_position: "定陶商會"
    event_status: "久違回商會之盤點已完成，白御行準備離開／回觀止"

  immediate_world_state:
    - "趙受益與六條已完成榴月一日夜集並返回觀止；六條今晨已下樓吃第一批玉荷包。"
    - "楊玉環因白玉池自主到觀止、昨夜泡池留宿，今晨仍在；白明礬被指派今日暫時隨行。"
    - "楊玉環已吃到沈萬三、桂姐、宋蕙蓮意外帶回的第一批玉荷包；白御行已明示不是自己預先準備。"
    - "桂姐、宋蕙蓮此前隨沈萬三赴明朝線做餐飲考察；三人今晨已返觀止。"
    - "李師師與白御行昨夜玩法因真睡失敗；今晨另完成自願成人補考。"
    - "李師師已答應在不替紅袖做決定的前提下，未來可幫白御行創造自然靠近紅袖的機會。"
    - "白玉池皇帝已先用過；沈萬三、桂姐、宋蕙蓮屬後續邀請者。"
    - "觀止十日歇業整修為第二日；紅娘門窗屏風仍拆除。"
    - "定陶商會帳務已校正：辭歲／錦棠客戶端款項可視為已到帳；皇帝／朱明未清部分由定陶持有債權。"
    - "顧青簡將向辭歲推五年五分定存；尚未簽。"
    - "朱明短期交割若不足，可談年息十分長債／地府分紅／商品抵債；尚未簽。"
    - "三百萬首批流動性為橋接週轉與信用展示；乾隆只借缺額；錦棠交易本身為定陶帶來 3,750,000 兩分成收入。"
    - "烤鹽／廣源舊案不再獨立待辦；曹州假印案仍 ACTIVE，程商人已返曹州，有新進度再報。"
    - "京師女性貼身衣物／奢侈品旗艦專案已交常煒副會長處理。"

  next_turn_rule:
    - "若玩家說回去／繼續，可讓白御行從定陶商會返觀止，推進一個清楚節點。"
    - "不要再讓顧青簡重講已校正的辭歲『未收九百八十萬所以不能用』舊帳。"
    - "不要把辭歲五年定存、朱家十分長債、胡椒套利自動成交。"
    - "不要重開烤鹽／廣源舊案。"
    - "不要因早餐帝皇八卦替未回查的逐筆叫價補造硬紀錄。"
```

---

# 32｜HOT V3.8 結論

```yaml
HOT_V3_8_CONCLUSION:
  status: "VALID_HOT_SAVE"
  current_world_time: "理火三年榴月二日白日"

  hard_results:
    - "趙受益＋六條汴京夜集已安全回樓；六條帶栗子給白御行，未新增戀愛／成人結果。"
    - "楊玉環因白玉池自主到觀止，張麗華陪同；紅娘被白衣濕髮的楊玉環嚇到，後知身份更尷尬。"
    - "楊玉環留宿觀止一夜；榴月二日白明礬被白御行臨時安排跟隨她。"
    - "楊玉環已接受『幾串荔枝即可』之承諾；今晨意外吃到桂姐／宋蕙蓮／沈萬三帶回的第一批玉荷包。"
    - "李師師與白御行昨夜玩法因二人真睡而未完成；榴月二日晨間另完成自願成人口部性親密補考。"
    - "李師師答應未來可在不越過紅袖意願的前提下協助白御行創造靠近機會。"
    - "桂姐與宋蕙蓮先前在沈萬三明朝線做餐飲考察，今晨與沈萬三一同返觀止。"
    - "白玉池使用順序校正：皇帝已先使用，楊玉環昨夜使用；沈萬三／桂姐／宋蕙蓮為後續受邀者。"
    - "觀止自動翻譯器設定鎖回；六條日語人工翻譯錯誤作廢。"
    - "朱正德現為九幽朱明家主、趙受益為趙宋家主；朱正德 1,200 萬成交債為朱明全朝代／家族共同買單，朱棣簽單現場背書。"
    - "辭歲／錦棠客戶端在定陶帳上的拍賣分成視為已到帳可用；外部未收齊部分屬定陶商會資產端債權。"
    - "五年五分定存已由白御行命顧青簡向辭歲推銷，但尚未成交。"
    - "朱明若短期不能交割，可談年息十分長債／分紅／商品抵債；尚未成交。"
    - "首批三百萬是橋接週轉與信用展示；乾隆只借缺額；錦棠交易給定陶 3,750,000 兩收入可回補週轉。"
    - "定陶票據信用預期因大額可兌交割而上升，但尚未固化為天下所有商號無條件接受。"
    - "烤鹽／廣源已被西門慶→高衙內→高俅→蔡京大案鏈吸收，不再獨立待辦。"
    - "曹州假印案仍 ACTIVE；程姓商人已返曹州；有實質進度再回報。"
    - "京師女性貼身衣物／奢侈品旗艦專案已交常煒副會長執行。"

  next_valid_hot_version: "V3.9"
  master_merge: "NOT_PERFORMED"
  character_pool_update: "NOT_PERFORMED"
  runtime_patch_merge: "NOT_PERFORMED"
```


<!-- PROMOTED_SOURCE_END: 觀止青樓_白御行線_HOT_SAVE_V3.8_榴月二日白日_楊玉環荔枝_桂蕙沈萬三回歸_師師晨間補考_定陶存款朱明長債與曹州案版.md -->


<!-- PROMOTED_SOURCE_BEGIN: 觀止青樓_白御行線_HOT_SAVE_V3.9_榴月二日晚_長恨歌文會_柳如是東林夜談_趙受益宣和入席_六條楊玉環三人約會開放_散會版.md -->
# SOURCE ARCHIVE｜觀止青樓_白御行線_HOT_SAVE_V3.9_榴月二日晚_長恨歌文會_柳如是東林夜談_趙受益宣和入席_六條楊玉環三人約會開放_散會版.md

**SHA-256：** `9c95570af9441d695632214e6486c4b2733e3841a65c3742a26a61e66254afa7`

> **法位：本檔 E93–E98 固化來源。** 原 HOT 內的 CURRENT_SCENE／HOLD 只代表當時快照；不得覆寫本 MASTER 截止或 V4.1–V4.4 疊加層。

# 觀止青樓｜白御行線 HOT SAVE V3.9
## 理火三年榴月二日晚｜長恨歌文會 × 宋末明末政治夜談 × 柳如是東林局 × 趙受益宣和地道入席 × 六條／楊玉環雙線追求與三人約會開放 × 楊玉環請款帳務 × 散會版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V3_9_LIU02_NIGHT_LITERARY_SALON_RENZONG_ROKUJO_YANG_THREE_DATE_DISMISSAL"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V3.9"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V11.0-R2"
  character_source: "觀止人物卡池_LCAPG_V2.3_李清照趙受益錦棠顧青簡增補_薛濤魚玄機暫定入場_正式版.md"

  story_time_span:
    start: "HOT V3.8 後／理火三年榴月二日白日"
    current: "理火三年榴月二日晚／長時文會散場；精確鐘點未知"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AT_GUANZHI_SALON_DISMISSAL_BEFORE_INDIVIDUAL_DEPARTURES_AND_ROOM_ASSIGNMENTS"

  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V3.8_榴月二日白日_楊玉環荔枝_桂蕙沈萬三回歸_師師晨間補考_定陶存款朱明長債與曹州案版.md"
  previous_hot_sha256: "c5280c4e1ef117d7846d2275b39a63101050427e5a8c8c9c8abaf09769422518"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md"
  long_term_master_sha256: "0149362b4128d62d947d4ffbcc618003913b1cad7052d57fe5b3f84f8f05084f"

  experimental_overlays:
    performance_patch:
      file: "觀止青樓_PATCH_風月角色表演與接戲能力_V0.1-EXP_獨立試跑未併主系統.md"
      status: "INDEPENDENT_TRIAL_OVERLAY_NOT_MERGED"
    analyzer_exit_patch:
      file: "觀止青樓_PATCH_分析器退場_重大升階定義_SCOPED_REACTIVATION_顯影反污染_V0.1-EXP.md"
      status: "GUANZHI_SPECIFIC_OPTIONAL_EXPERIMENTAL_OVERLAY_NOT_MERGED"
    lihuo_environment_patch:
      file: "理火環境_PATCH_V0.1.md"
      status: "REFERENCE_OPTIONAL_EXPERIMENTAL_OVERLAY_NOT_MERGED"

  save_scope:
    - "榴月二日晚觀止內部文會之成立、參與者與散會命令。"
    - "白居易《長恨歌》、楊玉環本人與文學形象分離，以及後世十樂章《長恨歌》作品之介紹與浮香改編線。"
    - "辛棄疾、岳飛、黃巢、宋江、文天祥、崖山、唐宋明政治結構等後世資訊之玩家轉述；全部分離為 testimony／interpretation，不自動升格客觀世界史。"
    - "柳如是因『有人想聽東林黨的故事』邀請自主入席；其東林、錢謙益、明末財政與政治人格論述。"
    - "仁宗／貞觀／弘治／洪熙等比較；李清照、柳如是、唐人三人對趙受益之評估。"
    - "六條得知趙受益＝宋仁宗；宣和地道響應與趙受益自主入席；不得固化成六條一想即可召喚之穩定規則。"
    - "趙受益對君臣、私怒、公法、官員反對資格之本輪自述。"
    - "楊玉環以普通富家男人標準評估趙受益；六條、楊玉環、趙受益三方追求／嫉妒／非獨占／三人約會可能性之明確分軸。"
    - "三人約會費用由趙受益私人請客之承諾；未發生、未定日期。"
    - "楊玉環在觀止開支先向李隆基請款之指令；請款不等於債務成立、付款或楊玉環無錢。"
    - "趙受益『下一個男人』身分尚未成立；未來若由本人主動提出接帳，仍須通知／詢問楊玉環是否承認該位置。"
    - "白御行宣布散會：欲歸者自歸，不欲歸者找潘金蓮安排房間；個別去留尚未觀察，不偷填。"
```

---

# 0｜提交法位、來源與本輪反污染

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V3.8_榴月二日白日_楊玉環荔枝_桂蕙沈萬三回歸_師師晨間補考_定陶存款朱明長債與曹州案版.md"
    role: "本檔直接前置 HOT；V3.8 及以前有效硬狀態全部繼承，除本檔明示更新／補正者。"

  master_archive:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md"
    role: "截至 HOT V3.4 之長期固化；V3.5→V3.6-R2→V3.7→V3.8→本 V3.9 依序作較新合法疊加。"

  current_character_source:
    file: "觀止人物卡池_LCAPG_V2.3_李清照趙受益錦棠顧青簡增補_薛濤魚玄機暫定入場_正式版.md"
    role: "現行人物基線；本輪柳如是出席、六條／趙受益／楊玉環關係、趙受益本夜自述等皆為白御行線事件，不回灌跨線人物基線。"

  current_route_conversation_commit:
    role: "HOT V3.8 後至本次 HOT SAVE 命令前之直接劇情、玩家自身言行、NPC 可觀察回應、公開／私人帳務指令與明示校正。"

COMMIT_NOTE:
  - "本檔只更新 HOT SAVE；不更新 MASTER、不修改人物卡池、不修改主程序、不合併 EXP PATCH。"
  - "本夜大量內容為玩家向古人轉述後世文本、人物與政治史。SAVE 必須保存『誰聽到什麼』與『人物如何解讀』，但不得把玩家轉述自動升格成觀止客觀世界史。"
  - "玩家展示之後世詩文／十樂章《長恨歌》並非白御行本人創作；本輪已明示為後世作品。不得在續接時改成白御行作者。"
  - "柳如是對東林、明末、錢謙益等發言屬柳如是本人的路線自述／見解，不是模型替她建立的唯一史學真相。"
  - "趙受益本夜對君臣、公法、私怒的話是當場人物自述與政治人格顯影；不得直接倒灌成所有路線固定名句或制度已部署。"
  - "六條、楊玉環、趙受益所說的『可以追／願意約會／不排斥更親密可能』只建立方向資格；不建立性交、三人性行為、戀愛、排他、婚姻或永久同意。"
  - "宣和地道本夜有響應並讓趙受益得以來到觀止，但『六條一想趙受益→地道必開』仍未證明，不得固化成心理召喚規則。"
  - "李隆基帳務目前是白御行指示『先安排請款』；請款不等於李隆基承認債務、已收到帳單或已付款。"
  - "楊玉環一天洗三次白玉池未成立為固定作息；那是白御行在談帳時的說法／推法，人物未承諾。"
  - "李隆基是否可稱『前男友』未被楊玉環正式定義，SAVE 不固化該稱呼。"
  - "趙受益目前不是楊玉環的『下一個男人』；這是未來可能身分，不是今晚已取得的職缺。"
  - "白御行宣布散會後，沒有逐一演出誰回家、誰留宿、誰分到哪間房；SAVE 到此停止，不偷填散會後結果。"
```

---

# 1｜當前時間、空間與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年榴月二日"
  time: "晚間／長時文會散場；精確時刻未知"
  primary_location: "觀止內部文會席／大堂活動區；精確廳名不另固化"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  player:
    name: "白御行"
    current_position: "觀止文會席"
    last_confirmed_action:
      - "宣布今晚大功告成、散會。"
      - "表示想回家的自行回家；不想回去者找潘金蓮安排房間。"
      - "要求導演製作 HOT SAVE，並提醒今晚很長、不得弄錯。"

  guanzhi_background:
    ten_day_closure_day: 2
    ordinary_public_business: "CLOSED"
    internal_operations: "ACTIVE"
    hongniang_room_open_structure: "ACTIVE_TEN_DAY_DOOR_WINDOW_SCREEN_REMOVAL"
    public_salon_status: "INTERNAL_PRIVATE_SALON_COMPLETED"

  dismissal_state:
    order_given: true
    individual_departures_observed: false
    individual_room_requests_observed: false
    room_assignments_completed: false
    next_morning_reached: false

  direct_resume_point:
    - "若下一輪仍接榴月二日晚，可從散會後第一個自行發生的去留／房間／私下續談事件接起。"
    - "若玩家明示直接到翌日，才可推進榴月三日；本 HOT 本身不跨日。"
    - "不得替白御行決定今晚是否留在某人房中、是否進行私人親密或是否送任何客人離開。"
```

---

# 2｜V3.8 後仍活躍之核心狀態

```yaml
INHERITED_ACTIVE_CORE:
  ten_day_closure:
    status: "ACTIVE"
    current_day: 2
    ordinary_public_business: "CLOSED"
    internal_operations: "ACTIVE"

  hongniang_room_swap:
    status: "ACTIVE"
    door_leaf: "REMOVED"
    window_sashes: "REMOVED"
    screen: "REMOVED_FOR_MAINTENANCE"
    restore: "重新開業當日上午"
    openness_not_permission: true

  hongxiu:
    base_special_ruler_taels: 500000
    ruler_type: "PRIVATE_RELATION_AND_HYPOTHETICAL_SPECIAL_ONE_NIGHT_CONSIDERATION_THRESHOLD"
    current_effective_state: "LOWERED_ONE_STEP_AFTER_PLAYER_PASSED_LISTENING_CHALLENGE_EXACT_NEW_VALUE_UNANNOUNCED"
    exact_current_threshold: "UNKNOWN_NOT_TO_INVENT"
    call_right_quantity: 1
    call_right_status: "ACTIVE_UNREDEEMED"
    salon_presence: "ABSENT_FROM_THIS_NIGHT_SALON"

  zhao_rokujo:
    prior_adult_event: "CONFIRMED_FROM_V3.6-R2; NO_AUTO_ROMANCE"
    night_market_outing: "COMPLETED_FROM_V3.8"
    mutual_attention: "BOTH_HAVE_EXPRESSED_CARE_OR_CONCERN; RELATIONSHIP_UNLABELLED"
    rokujo_basic_living_sponsorship: "LCAPG BASELINE: 趙受益默認代付六條常規住宿／茶食／必要生活；不產生人身或性權利。"

  yang_yuhuan:
    guanzhi_status: "AUTONOMOUS_GUEST"
    stay_duration: "可再留數日；實際每日去留由本人決定"
    prostitution_status: "NOT_LISTED_NOT_EMPLOYEE"
    ownership_status: "NONE"
    bai_mingfan_temporary_assist: "ACTIVE_FROM_V3.8"

  li_longji_hongniang:
    private_adult_transaction:
      amount_taels: 800
      status: "COMPLETED_PAID"
      note: "與任何 888 傳聞分離；888 非成立帳。"

  dingtao:
    caozhou_fake_seal_case: "ACTIVE; 有實質進度再報"
    old_roast_salt_guangyuan_chain: "DO_NOT_REOPEN_AS_SEPARATE_CASE"
    changwei_luxury_project: "DELEGATED"
```

---

# 3｜SALON02-E01｜榴月二日晚內部文會成立

```yaml
SALON_FORMATION:
  event_id: "SALON02-E01-LIU02_NIGHT_LITERARY_POLITICAL_SALON"
  event_axis_state: "COMPLETED_TO_DISMISSAL"
  public_business: false

  confirmed_initial_core_participants:
    - "白御行"
    - "李清照／易安"
    - "蘇軾"
    - "李白"
    - "白居易／白樂天"
    - "楊玉環"

  confirmed_regular_or_later_speakers_present_during_parts_of_salon:
    - "潘金蓮"
    - "紅娘"
    - "李師師"
    - "六條御息所"
    - "醉花"
    - "浮香"
    - "柳如是（後到）"
    - "趙受益（後由宣和地道到）"

  attendance_caution:
    - "不同人物進場時間不同；不得讓後到者自動知道其到場前所有對話。"
    - "沒有逐幕確認的其他觀止人物，不因『常駐』自動視為全程旁聽。"
```

---

# 4｜CHANGHENGE02-E01｜《長恨歌》本人、文學形象與後世十樂章

```yaml
CHANGHENGE_EVENT:
  event_id: "CHANGHENGE02-E01-BAI_JUYI_YANG_YUHUAN_FUTURE_CANTATA"
  event_axis_state: "COMPLETED_DISCUSSION_ADAPTATION_OPEN"

  bai_juyi:
    confirmed:
      - "白居易在楊玉環本人在場時吟誦／談論《長恨歌》。"
      - "白居易承認詩中楊玉環不是完整的真實楊玉環；詩具有文學塑形。"
      - "『在天願作比翼鳥，在地願為連理枝』等收束屬詩人之文學延續，不是楊玉環本人曾給出的現實承諾。"

  yang_yuhuan:
    fixed_position:
      - "接受作品可以作為作品被欣賞。"
      - "拒絕被文學收束替她補出未曾同意的等待、永恆承諾或死後團圓。"
      - "文學中的楊玉環 != 當場活著、能自己回答的楊玉環。"

  future_ten_movement_work:
    source_status: "PLAYER_INTRODUCED_FUTURE_WORK_NOT_PLAYER_AUTHORSHIP"
    confirmed:
      - "白御行介紹後世十樂章《長恨歌》組曲／大型聲樂作品之詮釋。"
      - "白御行未宣稱自己是原作者；屬後世創作者作品。"
      - "核心詮釋之一：終句『此恨綿綿無絕期』不是靠超自然重逢補完，而是因永遠不能重逢，所以遺憾無盡。"
      - "楊玉環對『死者仍死、活人不被強行抓回來完成結局』的詮釋表示正面接受。"

  fuxiang_adaptation:
    status: "ACTIVE_ADAPTATION"
    permission: "GRANTED_BY_PLAYER_FOR_GUANZHI_ADAPTATION"
    public_release_date: "NOT_SET"
    large_chorus_military_sections: "POSSIBLE_DESIGN_NOT_FINAL"
    debate_note: "『數大便是美』只是一條被討論的美學方向，不是已定品質原則。"
```

---

# 5｜FUTURE-TEXT02｜辛棄疾、岳飛、黃巢、宋江、文天祥與崖山之後世轉述法位

```yaml
FUTURE_HISTORY_TESTIMONY_LEDGER:
  authority: "PLAYER_TESTIMONY_AND_SHARED_TEXTS_NOT_AUTOMATIC_OBJECTIVE_CANON"

  xin_qiji:
    - "白御行向易安展示／吟誦後世辛棄疾作品。"
    - "易安知道此作者在她之後；不得讓她無來源知道其完整生平。"

  yue_fei:
    - "白御行吟誦／介紹岳飛相關《滿江紅》文本。"
    - "白御行向易安等人轉述：岳飛曾打到朱仙鎮附近、十二道金牌召回、後以『莫須有』被殺、後世稱岳武穆，以及趙構在背後之政治責任等。"
    - "上述具體史事在本 SAVE 中保存為玩家轉述；除非另有 GM 固化，不自動升格為觀止客觀史庫。"

  huang_chao:
    - "白御行引入『待到秋來九月八……』等黃巢文本／形象。"
    - "李白欣賞其中之氣，不等於認可黃巢行動。"
    - "『科舉因相貌被拒』等傳說未被固化為史實。"

  song_jiang:
    - "本夜分開歷史宋江與後世《水滸傳》人物塑形，不把小說人格直接回寫歷史本人。"

  wen_tianxiang:
    - "白御行吟誦／介紹《正氣歌》及文天祥後世故事。"

  yaishan_and_zhao_bing:
    - "白御行轉述陸秀夫負幼帝趙昺赴海等崖山末局。"
    - "易安與楊玉環明確區分：成人陸秀夫之選擇 != 七歲趙昺自身充分代理。"
    - "『敵方可能殺死趙昺』 != 『趙昺自願選擇死亡』。"
    - "趙昺作為末代／高度政治象徵可能縮窄生存出口，是可討論政治結構；不得把『趙家最後血脈』等未證主張寫成硬事實。"
    - "『崖山十萬殉國』已被校正：可有大量浮屍／死亡敘述，但不能把所有死者自動判定為自願殉國。"
```

---

# 6｜POLITICAL02-E01｜唐宋明結構論：玩家命題、人物接受與反對分離

```yaml
POLITICAL_THESIS_LEDGER:
  event_id: "POLITICAL02-E01-TANG_SONG_MING_STRUCTURE_SALON"
  status: "OPEN_CONTESTED_DISCUSSION_COMPLETED_FOR_THIS_NIGHT"
  objective_canon_upgrade: false

  player_major_theses:
    - "唐代可被理解為長期由門閥／軍事家族／北方軍事貴族網絡深度塑形的政治世界；隋楊、李唐均出自相近的北方軍事貴族生態。"
    - "府兵制依賴有土地與自我供養能力之編戶／軍戶基礎；土地、戶籍與財政基礎被侵蝕後，府兵先衰，後來長期募兵、邊鎮、節度使才更重。"
    - "安史之亂中河北快速轉向不只因安祿山軍事強，也可能反映河北對關中／隴西中心秩序之長期結構張力。"
    - "黃巢可作為『宋的真正創業者』之結構隱喻：晚唐戰亂摧毀數百年舊門閥網絡，替後來宋代不同政治地形清場。"
    - "宋尤其仁宗朝較能形成『天下不是皇帝私產、官員本來就有資格參與公共判斷』之政治人格。"
    - "玩家用『皇帝＋奴才／奴性語法』描述後世尤其明代部分政治結構：官員政治人格高度依附皇帝生殺與允許。"
    - "崖山被玩家作為華夏政治人格斷裂之象徵；同時提出國家是否被人視為『自己的帳』才是關鍵測試。"
    - "玩家提出明代某些諫爭可能混入以受杖／死諫完成忠臣名聲之激勵。"

  salon_pushback_and_limits:
    - "不得把所有唐代權力群體都壓成單一『關隴集團』或同一家族。"
    - "武士彠可視為被李淵創業網絡吸收的重要外來／地方力量；不自動等於老關隴純門閥。"
    - "府兵崩解可包含土地兼併、戶籍、軍役與財政問題；不得保存成『關隴故意吃光土地』之單一充分原因。"
    - "中晚唐利益網絡已多元，不能把後期所有侵奪繼續簡化為早期關隴一群人。"
    - "蘇軾若生晚唐是否成黃巢只能作制度吸納能力的反事實比喻，不可寫成蘇軾必然會反。"
    - "明代並非所有官員都只有奴性；柳如是等人明確保留真勇、真忠、真死諫者存在。"
    - "複雜性不是替任何投降、背叛或政策失敗沖帳；不同事件分帳。"
    - "任何『十萬殉國』『全天下都沒骨頭』等總量敘事不得替代逐事件、逐資格、逐知情分析。"
```

---

# 7｜LIURU02-E01｜柳如是因東林邀請自主到場

```yaml
LIU_RUSHI_ENTRY:
  event_id: "LIURU02-E01-DONGLIN_INVITATION_VOLUNTARY_ARRIVAL"
  event_axis_state: "COMPLETED_ENTRY_SALON_PARTICIPATION"
  correct_name: "柳如是"
  forbidden_name_pollution: "柳如煙"

  invitation:
    player_instruction: "請潘金蓮傳話：『有人想聽東林黨的故事。』"
    coercion: false

  arrival:
    - "柳如是自主到觀止赴席。"
    - "她沒有刻意坐近白御行或易安，維持自己的站位。"
    - "她以自身經驗與晚明／易代之人的視角發言，不作白御行論點之代言人。"

  world_status:
    route_guest_this_night: true
    character_pool_admission: "NOT_PERFORMED"
    permanent_residency: "NOT_ESTABLISHED"
```

---

# 8｜LIURU02-E02｜柳如是之晚明帳、東林帳與錢謙益帳

```yaml
LIU_RUSHI_SELF_STATEMENTS:
  qian_qianyi:
    - "柳如是談到錢謙益／錢牧齋之文名、東林／復社政治位置、南明／弘光與降清問題。"
    - "她拒絕以一句『無恥降臣』封死全部人生，也拒絕以後來可能的反清／復明行動洗掉投降。"
    - "核心分帳：『跪了就是跪了；後來做十件事不能改成沒跪。』"
    - "一個人可以同時愛國、怕死、戀棧名位、羞恥、後悔，再做別的事；複雜不等於高尚。"

  moral_accounting:
    - "柳如是不喜歡替人物一次結案；好帳、壞帳分開，後來補做不倒銷以前。"
    - "她不自稱看盡天下，因此拒絕『我已看見最壞人性』式全知。"

  life_death_identity:
    - "南京／易代相關談話中，柳如是承認自己曾希望錢謙益與她一起死，但不能替他作選擇。"
    - "在白御行校正後，她接受：生死不是純個人自由題，身份、政治象徵與他人如何定義你會壓縮出口。"
    - "固定可續接語義：『死不死，不只是你的意志；還要看你在別人的世界裡，被當成什麼。』"

  donglin_and_faction:
    - "柳如是拒絕把東林一概寫成壞人；其中有真心、真勇、真死者。"
    - "她指出風險在於『君子／小人』道德化後，政策分歧可能變成道德身份戰，妥協被寫成骯髒。"
    - "『天下不是皇帝一個人的』也可能腐化成『天下應該聽最懂天下的我們』。"
    - "士人結社／皇帝恐黨／倚重宦官／清流受迫害／烈士身份強化可形成互相餵養的循環。"
    - "關鍵場內句：『乾淨到不能跟髒的人一起救國。』"

  ming_finance_and_state_capacity:
    - "柳如是區分『國家沒錢』與『天下沒錢』：資源可能在私人手中，但不在國家仍可合法調度的位置。"
    - "晚明私人個體各自保產的理性，可能疊成集體亡國。"
    - "流寇／強制力量可榨出資源，不等於朝廷在合法政治條件下同樣能調用。"

  slave_grammar:
    - "柳如是接受：奴性秩序不必讓每個人法理上真是奴隸，也可能只是讓『服從能決定你命運的人』成為最便宜生存策略。"
    - "她接受紅娘／場內形成的語義：骨頭若永遠長在別人手上，換五個主人也未必成為自己。"
    - "她接受白御行對某些明代諫爭『連自己的死都可能進入算計』之結構批評，但拒絕普遍化到所有諫臣。"
    - "場內形成之警句：『有時候，士人需要一個暴君，來完成自己的忠臣。』"
```

---

# 9｜RENZONG-COMPARE02｜仁宗、貞觀、弘治、洪熙與政治人格比較

```yaml
RENZONG_COMPARISON:
  event_id: "RENZONG-COMPARE02-RULER_MODEL_POLITICAL_PERSONHOOD"
  status: "COMPLETED_DISCUSSION_NOT_OBJECTIVE_RANKING"

  liu_rushi_choice:
    - "若以『官員能否保有不依賴皇帝個人恩准的政治人格』為尺度，柳如是在宋仁宗朝與她認為明代較佳時期相比，選宋仁宗朝。"
    - "她沒有把仁宗朝說成平等烏托邦；婦女、奴僕、百姓等仍非現代平等位置。"

  tang_comparison:
    - "唐代側以貞觀作主要比較候選；李白個人對開元前中期之氣象另有偏愛。"
    - "柳如是在此特定尺度上仍選仁宗朝，理由偏向制度／政治文化：貞觀更像強勢明君願意納諫；仁宗朝更接近『我本來就有資格說』。"

  ming_hongxi:
    - "白御行提出明仁宗朱高熾，指出其在位約短、但減緩前朝嚴酷、調整政策。"
    - "柳如是對洪熙給予高度尊重，但仍認為在位太短，較像好皇帝暫時收刀，未足以證明制度文化能固定下來。"

  yian_position:
    - "白御行提出仁宗給宋留下『好皇帝／好政治如何可能』的尺度，後世即使不是每位皇帝照做，臣民仍可用『仁宗時不是如此』反照後君。"
    - "李清照接受『政治記憶／尺度可以活得比某位皇帝久』，但拒絕把數百年後崖山的選擇單因果歸給仁宗。"
    - "若問哪位趙宋皇帝最能象徵『大宋本來可以是什麼樣子』，易安在本夜答案為仁宗。"

  founder_shadow:
    - "柳如是指出開國皇帝留下的不只是制度，也留下後世反覆付利息的政治陰影；朱元璋與宋太祖皆可作此類比較。"
```

---

# 10｜ROKUJO02-E02｜六條得知趙受益＝宋仁宗

```yaml
ROKUJO_RENZONG_REVEAL:
  event_id: "ROKUJO02-E02-ZHAO_SHOUYI_IS_RENZONG_REVEAL"
  event_axis_state: "COMPLETED_KNOWLEDGE_UPDATE"

  before:
    - "六條已知道趙受益具有趙宋皇族／高位身份，與他有既有成人事件、夜集與在意線。"
    - "六條昨日與趙受益外出吃小食／夜集；該事件未因皇帝身份而被重新定義。"

  reveal:
    - "白御行明確告知六條：昨日與她吃小食的趙受益，就是後世所稱宋仁宗。"

  rokujo_response:
    - "六條沒有把昨日普通相處倒寫成『因為他是聖君所以每個動作都高尚』。"
    - "她更在意今日知道身份後，昨日那個趙受益是否仍是同一個人。"
    - "她後續明示『他又不是我的』，拒絕所有權式理解。"

  relationship_limit:
    - "得知宋仁宗身份沒有自動升格戀愛、婚約、排他或臣屬。"
```

---

# 11｜XUANHE02-E01｜宣和地道響應與趙受益自主入席

```yaml
XUANHE_TUNNEL_EVENT:
  event_id: "XUANHE02-E01-ROKUJO_THOUGHT_HONGNIANG_CALL_ZHAO_ARRIVAL"
  event_axis_state: "COMPLETED_ARRIVAL_MECHANISM_UNRESOLVED"

  sequence:
    - "白御行提出六條若想趙受益，宣和地道也許會有反應。"
    - "紅娘受命前往地道處查看／喊人。"
    - "地道確實出現可與趙受益接上的反應；紅娘聽到／接到趙受益。"
    - "趙受益在獲邀後自主決定前來觀止，並非被強制傳送。"

  zhao_arrival:
    - "趙受益無大排場、無要求全席跪拜。"
    - "他以『不是給白御行面子，是給六條面子』之玩笑／表態入席。"
    - "六條亦以昨日他請自己吃小食、今日自己請他喝酒之方向回應。"

  portal_limits:
    - "本夜一次成功響應 != 穩定心理召喚法則。"
    - "宣和地道另一端、定位條件、是否可重現均未固化。"
    - "不得在下一輪只因六條想起趙受益就自動開門。"
```

---

# 12｜ZHAO02-E01｜趙受益面對未來『仁宗』標籤與制度自述

```yaml
ZHAO_RENZONG_SELF_TEST:
  event_id: "ZHAO02-E01-FUTURE_RENZONG_LABEL_AND_INSTITUTIONAL_SELF_STATEMENTS"
  status: "COMPLETED_SELF_STATEMENT_SET_ROUTE_ONLY"

  future_label:
    - "趙受益知道席上後世人物把他視為『仁宗』／好皇帝樣本，但他拒絕把尚未完成的人生預先領成功名。"
    - "他指出若後世真拿他當尺度，那更重要的是不要讓好處只依賴他個人脾氣，否則只是『碰巧遇到一個溫和皇帝』。"

  tang_trio_evaluation:
    yang_yuhuan:
      - "暫不稱他明君；欣賞他目前能區分自己有權勢與別人有決定權。"
      - "若被傷面子仍能分清『我不舒服』與『你錯了』，才是有價值的材料。"
    li_bai:
      - "認為趙受益有『好皇帝的材料』，但要他自己活到那一步。"
    bai_juyi:
      - "以開元／長期成功後自我確信作警示：真正難題是三十年成功後還能不能相信自己可能錯。"
      - "趙受益對此回答『不知道』；白居易認為比預先保證自己一定能好更可信。"

  yian_private_pain_test:
    question: "若官員碰到皇帝最痛、最私人的事情，且那事情又影響公共判斷，皇帝如何處理？"
    zhao_answer:
      - "他承認自己會怒、會厭、甚至當下不想見對方。"
      - "若只是用痛處羞辱，和公共諫爭不同；但若痛處確實影響政事，必須分帳。"
      - "核心句：『我還是會恨他，可是我恨他，不等於他錯。』"
      - "核心句：『別讓我的怒，立刻變成天下的法。』"
      - "他承認可能一時做不到聽進去，但不應因私怒把所有異議者一併定成逆臣。"
      - "若後來發現對方正確，最難的是把人叫回來。"

  yian_revision:
    - "易安把測試改寫為：真正要看的是皇帝痛的時候，天下還剩多少地方不必跟著皇帝一起痛。"
```

---

# 13｜SUSHI-ZHAO02｜『忠犬』玩笑與官員第三類位置

```yaml
SUSHI_ZHAO_THREAD:
  event_id: "SUSHI-ZHAO02-LOYAL_DOG_JOKE_PUBLIC_OFFICE_THIRD_CATEGORY"
  event_axis_state: "COMPLETED"

  corrections:
    - "蘇軾在仁宗嘉祐年間入仕，但不是宋仁宗親自長期承受其成熟政治爭論的對手。"
    - "蘇軾真正的大量政策衝突發生在後續朝代；不得倒寫成『仁宗一生都在忍蘇軾咬他』。"

  key_salon_result:
    - "柳如是與蘇軾把重點從『仁宗個人容忍蘇軾』轉到『仁宗時代留下的政治世界能不能養出一個自認有資格反對皇帝的蘇軾』。"
    - "蘇軾場內語義：怕死與覺得自己有話該說可以同時存在。"
    - "趙受益場內句：『我沒養。大宋養的。』"
    - "趙受益進一步明示：若皇帝把所有官員都當『我的人』，最後只剩服從／背叛兩類。"
    - "必須保留第三類：『他反對我，但仍然是在做他的官。』"

  route_effect:
    - "這組話構成本夜趙受益政治人格顯影，不修改 LCAPG 跨線基線文件。"
```

---

# 14｜YANG-ZHAO02-E01｜楊玉環以普通富家男人尺度評估趙受益

```yaml
YANG_EVALUATES_ZHAO_AS_MAN:
  event_id: "YANG-ZHAO02-E01-ORDINARY_RICH_MAN_TEST"
  event_axis_state: "COMPLETED_ASSESSMENT_INVITATION_OPEN"

  framing:
    - "白御行要求楊玉環暫時拿掉『貴妃 vs 皇帝』『宋仁宗』等歷史身分，只看趙受益是否作為普通有錢男人值得她主動出手。"

  yang_assessment:
    - "外貌：可以。"
    - "談吐：不煩。"
    - "財力：不是問題。"
    - "她特別看重趙受益目前不急著把女人吸進自己的位置，也不需要女人不停證明他是男人。"
    - "核心句：『他不太需要女人不停證明他是男人。』"
    - "當時答案：值得出手；是否值得跟六條搶，起初尚未確定。"

  solo_food_invitation:
    - "楊玉環曾當面問：若只是兩個普通有錢閒人，明晚她約趙受益出去吃東西，他敢不敢去。"
    - "趙受益當下先看六條，暴露六條的感受對他不是無關。"
    - "此單獨明晚約飯沒有在本夜完成具體日期／時辰／地點確認，不得自動排入行程。"
```

---

# 15｜TRIANGLE02-E01｜『送命題』、嫉妒與追求資格

```yaml
PURSUIT_TRIANGLE:
  event_id: "TRIANGLE02-E01-YANG_ROKUJO_ZHAO_PURSUIT_DISCLOSURE"
  event_axis_state: "ACTIVE_RELATIONAL_OPEN"

  player_intent_disclosed:
    - "白御行承認自己一開始就打算問趙受益面對楊玉環／六條的送命題。"
    - "白御行並提出利用女人護食／嫉妒使六條更容易看清自己是否在意趙受益。"

  rokujo_response_to_jealousy_strategy:
    - "六條承認若真正把男人放進心裡，看見別的女人靠近，自己可能不舒服／嫉妒。"
    - "但她拒絕『因為有人搶，所以就更愛』的機械推導。"
    - "她要求區分：愛趙受益本人 vs 不想失去一件被別人搶的東西。"
    - "她後來承認楊玉環問趙受益時，自己確實想知道趙受益怎麼回答。"

  liu_rushi_summary:
    - "柳如是提出：嫉妒可以顯影，但不能製造原本不存在的感情。"

  zhao_position:
    - "趙受益拒絕靠另一個女人故意刺激六條來取得她。"
    - "他明示：若六條對他有興趣，希望是因為他；若沒有，別人的競爭不該把沒有變成有。"
```

---

# 16｜TRIANGLE02-E02｜三方把『追誰、被誰追、能否非獨占』攤開

```yaml
THREE_PARTY_PURSUIT_LEDGER:
  event_id: "TRIANGLE02-E02-OPEN_PURSUIT_NONEXCLUSIVE_DISCUSSION"
  event_axis_state: "OPEN_NOT_COMMITTED_RELATIONSHIP"

  yang_yuhuan:
    pursuit_permission: "OPEN"
    confirmed:
      - "楊玉環明確對趙受益說：可以追她。"
      - "這表示趙受益可約她、接近、讓她繼續認識；不保證追得到。"
      - "她不因宋仁宗身分給自動加成，也不因此建立戀愛／性／婚姻承諾。"
      - "她之後已從『不知道值不值得跟六條搶』進一步到認為趙受益值得搶，但仍拒絕把六條當必須擊敗的敵人。"

  rokujo:
    ownership: "NONE"
    confirmed:
      - "六條明示趙受益不是她的所有物。"
      - "她承認趙受益可以追其他女人，包括楊玉環；不是由她批准，而是她承認他本來有自己的行動權。"
      - "她不承諾情緒上完全不介意；可能嫉妒、不舒服、重新評估趙受益，甚至因此退出。"
      - "她保留：若有一天趙受益繼續追楊玉環，而自己不願接受，她可以說自己不再往前走。"

  zhao_shouyi:
    confirmed:
      - "趙受益明確承認自己對六條有興趣，且昨日夜集後興趣／在意更深。"
      - "趙受益也承認對楊玉環有興趣，願意繼續認識。"
      - "若『兩個都追』只代表同時承認兩條不同興趣、分別往前看，他答『想』。"
      - "若未來兩條關係產生不可兼容要求，他承認最後要由自己選，不能叫六條批准、也不能叫楊玉環退。"

  no_auto_result:
    - "同時追求資格 != 三角戀已成立。"
    - "對兩人有興趣 != 兩人已接受戀愛。"
    - "非獨占目前只是可討論／可嘗試狀態，不是固定關係制度。"
```

---

# 17｜THREEDATE02-E01｜三人約會與更親密可能性

```yaml
THREE_PERSON_DATE:
  event_id: "THREEDATE02-E01-ROKUJO_YANG_ZHAO_THREE_PERSON_DATE_OPEN"
  event_axis_state: "AGREED_AS_POSSIBILITY_NOT_YET_SCHEDULED"

  yang_yuhuan:
    three_person_date: "YES"
    intimate_possibility: "NOT_EXCLUDED_BUT_REQUIRES_FUTURE_IN_THE_MOMENT_CONSENT"
    limits:
      - "願意三人一起吃飯、喝酒、出遊／相處。"
      - "不預先答應三人一定發生性行為。"
      - "若未來三人當時都真有慾望，她不排斥事情往更親密方向發展。"
      - "她若想要趙受益，是因自己想要，不是為了贏六條。"

  rokujo:
    three_person_date: "YES_TRY_ONCE"
    intimate_possibility: "POSSIBLE_NOT_PRECONSENTED"
    limits:
      - "願意試一次三人約會，以觀察自己在共同場域中的真實反應。"
      - "她可能嫉妒、可能不舒服，也可能發現自己其實能接受。"
      - "任何更親密行為都只看當時她自己是否想要；若感覺自己是在比較、怕輸、被推著往前，她會退出。"

  zhao_shouyi:
    three_person_date: "YES_WANTS"
    intimate_possibility: "POSSIBLE_NOT_PRECONSENTED"
    limits:
      - "願意三人一起出去，想知道自己對六條的在意與對楊玉環的興趣放在同一晚會變成什麼。"
      - "承認沒有必要假裝從未想過更親密的三人可能性。"
      - "拒絕把第一次三人約會設成『一定要做到哪一步』。"
      - "若任何一人中途不想，當下即停止／不進一步；前面說『有可能』不形成後面欠誰的義務。"

  shared_status:
    first_date_date_time: "NOT_SET"
    first_date_location: "NOT_SET"
    intimacy_completed: false
    exclusive_commitment: false
    triad_relationship: "NOT_ESTABLISHED"
```

---

# 18｜FINANCE02-E01｜三人約會、公帳／私帳與趙受益請客

```yaml
DATE_FINANCE_LEDGER:
  emperor_association_reference:
    inherited_rule:
      - "槐月二十八日九幽帝皇聯誼會在觀止之集體娛樂、白玉池封場團體套餐由九幽娛樂城／帝皇聯誼會公帳支付。"
      - "公帳支付集體活動 != 趙宋私人資產已支付該次集體費用。"
      - "私人消費另算。"

  three_person_date:
    payer: "趙受益私人"
    status: "VERBAL_COMMITMENT_FOR_FUTURE_DATE_NOT_YET_INCURRED"
    confirmed:
      - "趙受益明確答應未來三人約會由他請客。"
      - "他特別說是趙受益自己的錢，不以九幽／帝皇聯誼會公帳報銷。"
      - "約會尚未發生，因此目前沒有實際報銷金額。"
```

---

# 19｜YANG-ACCOUNT02-E01｜楊玉環白玉池／生活費與趙受益開放支付

```yaml
YANG_ZHAO_EXPENSE_OFFER:
  event_id: "YANG-ACCOUNT02-E01-ZHAO_PARTIAL_VOLUNTARY_EXPENSE_OFFER"
  status: "OPEN_OFFER_PER_OCCURRENCE_NOT_BLANKET_SPONSORSHIP"

  zhao_offer:
    - "趙受益明確表示：若楊玉環問他願不願意替她支付部分白玉池使用費，他願意。"
    - "他沒有答應承包楊玉環全部住宿、生活、奢侈品或永久開支。"

  yang_acceptance:
    - "楊玉環接受『偶爾由趙受益請』的可能。"
    - "她沒有同意把自己長期生活費全部轉掛趙受益。"

  pan_accounting_rule:
    - "只可逐次、逐筆、在趙受益本人明確表示『這次我請』後記帳。"
    - "白御行替趙受益喊出的費用不得自動入趙受益私帳。"

  anti_pollution:
    - "『楊玉環每天要洗三次白玉池』不是固定日程。"
    - "趙受益有錢 != 自動有義務承擔楊玉環全部開支。"
```

---

# 20｜YANG-LILONGJI02-E01｜先向李隆基請款：只是假設、可能拒付

```yaml
YANG_LI_LONGJI_BILLING:
  event_id: "YANG-LILONGJI02-E01-REQUEST_TO_BILL_NOT_ACKNOWLEDGED_DEBT"
  status: "BILLING_ORDERED_DISPATCH_AND_PAYMENT_UNCONFIRMED"

  player_instruction:
    - "白御行明示：目前只是假設李隆基應負擔楊玉環在觀止之相關開支。"
    - "先安排把帳單／請款送給李隆基。"
    - "白御行明示李隆基可能拒收、拒付。"

  accounting_legal_state:
    - "觀止可先建立請款／待確認帳，不得登記成李隆基已承認債務。"
    - "帳單實際是否已送達，本輪沒有演出回執；因此 dispatch outcome = UNKNOWN。"
    - "李隆基是否付款 = UNKNOWN。"
    - "若拒付，首先只是該筆觀止開支沒有由李隆基結清。"

  yang_funds:
    - "楊玉環自己的現金／財產精確數額未知。"
    - "李隆基若拒付，不得自動推成楊玉環『身無分文』。"

  prostitution_listing:
    - "李隆基拒付不會自動讓楊玉環掛牌。"
    - "若未來楊玉環因自身考量想詢問掛牌、工作或其他換取收入方式，必須由楊玉環本人當時同意。"
    - "欠住宿／待付款 != 性服務義務。"
```

---

# 21｜NEXT-MAN02-E01｜『下一個男人』身分尚未成立

```yaml
NEXT_MAN_STATUS:
  event_id: "NEXT-MAN02-E01-ZHAO_NOT_YET_YANG_NEXT_MAN"
  status: "NOT_ESTABLISHED"

  current:
    zhao_is_next_man: false
    zhao_is_allowed_to_pursue_yang: true
    yang_accepts_pursuit: true
    relationship_depth_required_for_expense_takeover: "NOT_YET_REACHED"

  zhao_self_statement:
    - "若未來他與楊玉環真的走到共同日常／照顧的關係，而楊玉環也願意，他可能接下大部分甚至一段生活支出。"
    - "那必須是他自己願意為他與楊玉環的關係付錢，不是白御行用男性自尊替他簽長期帳。"

  future_procedure:
    - "若某一天趙受益本人去潘金蓮帳房，明確以『下一個男人』或等價關係身分表示願意接楊玉環某段日常帳，潘金蓮才可啟動身分／付款切換確認。"
    - "潘金蓮須通知並詢問楊玉環：她是否承認趙受益已到那個位置、是否接受相應付款安排。"
    - "白御行不能單方面宣布趙受益完成接手。"

  li_longji_relation_label:
    - "本輪未把李隆基固定稱為楊玉環『前男友』；相關歷史／情感稱謂仍由楊玉環自身與既有世界資料決定。"
```

---

# 22｜SALON-VOICE02｜今晚重要人物位置與反扁平錨點

```yaml
SALON_CHARACTER_ANCHORS:
  li_qingzhao:
    - "對後世宋亡資訊保持情緒與證據分離。"
    - "堅持七歲趙昺的代理權不能被成人忠烈敘事吞掉。"
    - "肯定仁宗作為宋政治尺度，但拒絕單因果神化。"

  su_shi:
    - "接受自己在後世政治鬥爭中有強烈公共發言資格，但不把自己寫成不怕死的烈士模板。"
    - "與趙受益有『忠犬』『海龜』等場內玩笑；玩笑不構成君臣私人契約。"

  li_bai:
    - "重氣勢、自由與人物活力；能欣賞黃巢詩的氣而不認可暴行。"
    - "對趙受益給的是『有材料，自己活出來』式評估。"

  bai_juyi:
    - "持續自覺文學會替人製造形象。"
    - "以開元／長期成功後的自我確信警告趙受益，而不是只唱明君頌。"

  yang_yuhuan:
    - "文學中的她、政治象徵中的她、活著的她必須分開。"
    - "能直接談慾望與男人，但不允許被追求自動變成所有物／生活被接手。"
    - "對趙受益已開放追求與三人約會可能；仍保有每一步當下同意。"

  rokujo:
    - "可真實嫉妒、在意、有佔有衝動，但不把趙受益說成自己的物品。"
    - "承認趙受益可追別人，不等於自己毫不介意。"
    - "三人約會是一次可嘗試事件，不是她已接受固定非獨占關係。"

  liu_rushi:
    - "不替任何人快速結案；好壞分帳、複雜不沖銷。"
    - "可尖銳拆政治人格與資源調度，但不得成為現代制度教授或白御行口舌。"

  zhao_shouyi:
    - "本夜可明君、可普通男人、可被調侃、可有慾望；不得只剩成熟關係導師。"
    - "已承認對六條、楊玉環皆有興趣。"
    - "政治上本輪核心自述是私怒不得直接變天下之法，反對皇帝者仍可是在做自己的官。"
```

---

# 23｜KNOWLEDGE02｜今晚人物知情邊界

```yaml
KNOWLEDGE_BOUNDARIES:
  general_rule:
    - "後到者不自動取得到場前所有討論內容。"
    - "玩家轉述的後世資料只能由實際聽見者使用；未聽者不得因模型一般知識自行知道。"

  rokujo:
    newly_knows:
      - "趙受益就是宋仁宗／趙禎的觀止版本。"
    does_not_gain:
      - "不因知道仁宗身份，自動知道完整北宋史或趙受益未來每件政績。"

  zhao_shouyi:
    newly_knows_or_observes_during_salon:
      - "席上後世人物把他視為後來的宋仁宗／政治樣本。"
      - "蘇軾是他之後的宋人，且後來以強烈政治發言聞名；本夜對話已把此關係說開。"
      - "柳如是是比他晚得多、具有後世歷史重量的女子；精確完整生平不因名字自動全部取得。"
    existing_historical_knowledge:
      - "李白、白居易、楊玉環等唐人對他本來就是前代歷史人物，但本夜活人相處仍不得被教科書形象取代。"

  liu_rushi:
    - "她從自己的時代位置知道宋／唐是前代，但不因觀止跨時空就自動知道所有後世於她之後的資訊。"
```

---

# 24｜翌日與未決安排

```yaml
OPEN_THREADS_V3_9:
  guanzhi_immediate:
    - id: "SALON_DISMISSAL_DEPARTURES"
      state: "OPEN"
      item: "散會命令已下；每位客人回家、留宿、續談、要房的實際選擇未演。"

    - id: "YANG_TWO_MAIDS"
      state: "PLANNED_NOT_EXECUTED"
      item: "白明礬原定翌日聯絡牙行找兩名機靈丫鬟供楊玉環自己挑選；是否仍照做、費用由誰付尚未演出。"

    - id: "FUXIANG_CHANGHENGE_ADAPTATION"
      state: "ACTIVE"
      item: "浮香繼續改編後世十樂章《長恨歌》；無公開演出日期。"

    - id: "ZHAO_ROKUJO_YANG_THREE_DATE"
      state: "OPEN_AGREED_IN_PRINCIPLE"
      item: "三人都願意試三人約會；日期、時辰、地點未定；更親密事件沒有預先同意。"

    - id: "YANG_SOLO_ZHAO_FOOD_INVITE"
      state: "UNRESOLVED_NOT_BOOKED"
      item: "楊玉環曾以『明晚一起吃東西』直接測試趙受益；後續討論轉入三人局，未形成單獨約會正式預約。"

    - id: "YANG_LI_LONGJI_BILL"
      state: "ORDERED_REQUEST_TO_BILL"
      item: "潘金蓮／觀止可整理楊玉環相關觀止費用向李隆基請款；送達、承認、拒付、付款均待後續。"

    - id: "ZHAO_NEXT_MAN_ROLE"
      state: "NOT_ESTABLISHED"
      item: "若趙受益未來主動表示願以更深關係身分接楊玉環日常帳，須再詢問楊玉環是否承認。"

    - id: "ZHAO_PARTIAL_WHITE_JADE_POOL_PAYMENT"
      state: "OPEN_PER_OCCURRENCE"
      item: "趙受益願偶爾替楊玉環付白玉池費；只有逐次本人明示才入帳。"

    - id: "HONGXIU_LOWERED_THRESHOLD"
      state: "ACTIVE_EXACT_VALUE_UNKNOWN"
      item: "白御行已通過紅袖聆聽挑戰；特殊 50 萬尺度應下降一階，但紅袖尚未宣布新精確數字。"

    - id: "HONGNIANG_DAY2_OPEN_ROOM"
      state: "ACTIVE"
      item: "紅娘門窗屏風拆除十日仍在第二日；不得提前恢復。"

  dingtao_inherited:
    - id: "CAOZHOU_FAKE_SEAL"
      state: "ACTIVE"
      item: "曹州假印案仍為當前主要案件；有實質進度再報。"
    - id: "CISU_FIVE_YEAR_DEPOSIT_PITCH"
      state: "ORDERED_NOT_CONFIRMED_SIGNED"
      item: "辭歲五年五分定存仍待本人決定。"
    - id: "ZHU_MING_SETTLEMENT_NEGOTIATION"
      state: "OPEN"
      item: "朱明若短期不足，可談長債／分紅／商品抵債；尚未簽。"
```

---

# 25｜本輪帳務／關係／同意快照

```yaml
RELATION_CONSENT_FINANCE_SNAPSHOT:
  rokujo_zhao:
    prior_adult_event: "CONFIRMED"
    romance: "UNDECIDED_NOT_ESTABLISHED"
    mutual_care: "CONFIRMED_AS_ROUTE_STATE"
    exclusivity: "NONE"
    zhao_may_pursue_others: "ROKUJO_ACKNOWLEDGES_YES"
    rokujo_emotional_nonjealousy: "NOT_PROMISED"

  yang_zhao:
    yang_accepts_pursuit: true
    zhao_interest: true
    romance: "NOT_ESTABLISHED"
    exclusivity: "NONE"
    solo_date: "NOT_BOOKED"
    occasional_white_jade_pool_payment: "OPEN_PER_OCCURRENCE"
    blanket_sponsorship: false
    zhao_next_man_status: false

  rokujo_yang_zhao:
    three_person_date: "ALL_THREE_OPEN_TO_TRY"
    date_time: "UNKNOWN_NOT_SET"
    intimacy_preconsent: false
    triad_relationship: "NOT_ESTABLISHED"
    one_person_may_withdraw: true
    future_in_the_moment_consent_required: true

  yang_li_longji:
    guanzhi_expense_billing: "REQUEST_TO_BILL_ORDERED"
    li_longji_debt_acknowledged: false
    bill_delivered: "UNKNOWN"
    payment_received: false
    rejection: "POSSIBLE_NOT_YET_OBSERVED"
    yang_penniless_if_rejected: false
    automatic_listing_if_rejected: false

  three_person_date_payment:
    payer: "趙受益私人"
    cost_incurred: false
    public_account_reimbursement: false

  li_longji_hongniang_800:
    amount_taels: 800
    status: "COMPLETED_PAID_PRIVATE_ADULT_TRANSACTION"
    separate_888_rumor: "FALSE_NOT_TO_REOPEN"
```

---

# 26｜本輪反污染鎖

```yaml
ANTI_REGRESSION_V3_9:
  calendar:
    - "現在停在榴月二日晚散會；還沒有到榴月三日。"
    - "觀止十日歇業整修仍為第二日。"

  salon_history:
    - "白御行轉述後世歷史 != GM 固化客觀史。"
    - "唐／宋／明結構論是本夜玩家命題與人物辯論，不可下一輪直接當作天下共同定論。"
    - "柳如是沒有成為白御行的史學代言人；她有大量保留、分帳與反駁。"

  liu_rushi:
    - "名字固定：柳如是。不得再寫成柳如煙。"
    - "今晚自主來席 != 已加入人物池／掛牌／常住。"

  zhao_shouyi:
    - "趙受益來席是自主決定，不是被六條心念強制召喚。"
    - "他知道後世稱他仁宗，但不應因此突然變成全知後世明君。"
    - "今晚政治自述是路線事件，不直接改人物卡池。"

  rokujo:
    - "六條『他又不是我的』是反所有權，不等於她不在意、不嫉妒或已同意固定開放關係。"
    - "六條願意試三人約會，不等於願意三人性行為。"

  yang_yuhuan:
    - "楊玉環開放趙受益追求，不等於已被追到。"
    - "她願意三人約會、不排斥未來更親密可能，不等於預先性交同意。"
    - "沒有『每天固定三次白玉池』硬設定。"
    - "李隆基拒付若發生，也不能自動把楊玉環寫成沒錢、欠身、必須掛牌。"

  finance:
    - "九幽帝皇聯誼會公帳只支付已規定的集體娛樂／團體白玉池等活動；未來三人約會由趙受益私人請。"
    - "李隆基現在只有被請款的可能位置；沒有已承認債務。"
    - "趙受益目前沒有接手楊玉環全部生活費。"
    - "趙受益『下一個男人』身份尚未成立。"
    - "白御行不能用趙受益『自尊』替他形成長期付款契約。"

  dismissal:
    - "白御行只宣布散會與自由去留。"
    - "未觀察到的回家／留宿／房間分配全部保持 UNKNOWN。"
    - "不得因『想回家自己回家』直接寫成所有客人已安全抵家。"
```

---

# 27｜直接接關摘要

```yaml
DIRECT_RESUME:
  scene_anchor:
    date: "理火三年榴月二日"
    time: "晚間／長時文會散場"
    player_position: "觀止文會席"
    event_status: "白御行已宣布散會；個別去留尚未演出"

  immediate_world_state:
    - "今晚《長恨歌》與後世十樂章作品的討論已完成；浮香改編仍在進行。"
    - "柳如是已來過並參與東林／明末／政治人格長談；她不是新收編人物。"
    - "趙受益已經透過本夜宣和地道事件自主到場；六條已知道他就是宋仁宗。"
    - "趙受益本夜明示：私怒不應直接成天下之法；官員可反對皇帝仍是在做自己的官。"
    - "楊玉環已明確允許趙受益追求；六條承認趙受益可追別人但不承諾不嫉妒。"
    - "趙受益明確想同時追六條與楊玉環，但接受未來若衝突需自己作選擇。"
    - "六條、楊玉環、趙受益三人均願意試三人約會；尚未定時間地點；任何更親密發展均須當時三方同意。"
    - "未來三人約會由趙受益私人請客，不走帝皇聯誼會公帳。"
    - "趙受益只開放逐次替楊玉環支付部分白玉池費，不承包全部生活費。"
    - "白御行已指示先整理楊玉環在觀止相關帳向李隆基請款；這只是假設性請款，送達／承認／付款皆未確認。"
    - "趙受益尚未取得楊玉環『下一個男人』身份；若未來本人主動接帳，仍需楊玉環確認。"
    - "楊玉環若李隆基拒付，不自動變成身無分文，也不自動掛牌。"
    - "紅袖五十萬特殊尺度因白御行通過聆聽挑戰應下降一階；新精確數字尚未公布。"
    - "觀止歇業整修第二日仍有效；紅娘房門窗屏風仍拆除。"

  next_turn_rule:
    - "若玩家說『繼續』，導演可先讓散會後世界自主走一個清楚節點：有人離席、有人找潘金蓮要房、有人留下續談；但不得替玩家選擇自己的去處。"
    - "若玩家直接說『明天』／『睡醒』，才可跨到榴月三日，並處理楊玉環丫鬟、帳單請款等翌日事項。"
    - "不要自動安排三人約會在今晚發生。"
    - "不要把楊玉環與趙受益寫成已交往。"
    - "不要把六條寫成已接受共享男人的固定制度。"
    - "不要把柳如是今晚論述回寫成角色池基線。"
```

---

# 28｜HOT V3.9 結論

```yaml
HOT_V3_9_CONCLUSION:
  status: "VALID_HOT_SAVE"
  current_world_time: "理火三年榴月二日晚／散會"

  hard_results:
    - "榴月二日晚觀止內部長時文會完成並由白御行宣布散會。"
    - "白居易《長恨歌》、楊玉環本人主權與文學塑形被明確分離。"
    - "白御行介紹後世十樂章《長恨歌》作品，非白御行作者；浮香取得改編方向，仍未定公演。"
    - "辛棄疾、岳飛、黃巢、宋江、文天祥、崖山、唐宋明等後世內容被大量轉述；本 SAVE 全部保留 testimony／interpretation 法位，不自動升格客觀世界史。"
    - "柳如是因東林邀請自主赴席，留下錢謙益分帳、東林道德化、晚明財政動員與奴性語法等本夜人物見解；未加入人物池。"
    - "仁宗在本夜被易安、柳如是、唐人三人以政治人格／制度尺度比較；沒有形成絕對歷史排名。"
    - "六條已知道趙受益就是宋仁宗；昨日夜集沒有因身份揭露被倒寫。"
    - "宣和地道本夜成功接上趙受益；趙受益自主前來；地道機制仍未固定。"
    - "趙受益本夜政治自述核心：私怒不等於對方錯，別讓自己的怒立刻成天下的法；反對皇帝者仍可是在做自己的官。"
    - "楊玉環已開放趙受益追求。"
    - "六條承認趙受益可追其他女人，包括楊玉環；但保留嫉妒、不舒服與退出權。"
    - "趙受益明確承認想同時追六條、楊玉環；未來若衝突由他自己承擔選擇。"
    - "三人均同意可試三人約會；未定日期地點；更親密事件只有未來當場三方同意才可能成立。"
    - "未來三人約會由趙受益私人請客，不走帝皇聯誼會公帳。"
    - "趙受益願逐次替楊玉環支付部分白玉池費，但沒有承包全部生活。"
    - "白御行已指示先向李隆基請楊玉環在觀止相關開支；僅為待確認請款，不是已承認債務。"
    - "趙受益尚未成為楊玉環『下一個男人』；未來若本人主動接帳，仍須楊玉環確認。"
    - "李隆基若拒付，不自動導致楊玉環身無分文或掛牌。"
    - "白御行最後命散會；所有未實際演出的回家／留宿／房間安排保持未知。"

  next_valid_hot_version: "V4.0"
  master_merge: "NOT_PERFORMED"
  character_pool_update: "NOT_PERFORMED"
  runtime_patch_merge: "NOT_PERFORMED"
```


<!-- PROMOTED_SOURCE_END: 觀止青樓_白御行線_HOT_SAVE_V3.9_榴月二日晚_長恨歌文會_柳如是東林夜談_趙受益宣和入席_六條楊玉環三人約會開放_散會版.md -->


<!-- PROMOTED_SOURCE_BEGIN: 觀止青樓_白御行線_HOT_SAVE_V4.0_榴月三日深夜_錦棠首次正式約會_自主購衣望河樓_私人成人事件_喜歡確認_相擁收幕版.md -->
# SOURCE ARCHIVE｜觀止青樓_白御行線_HOT_SAVE_V4.0_榴月三日深夜_錦棠首次正式約會_自主購衣望河樓_私人成人事件_喜歡確認_相擁收幕版.md

**SHA-256：** `4ae078855001a64e82c170f7977257fab5557128810bba1c0d68c25265d4a3ea`

> **法位：本檔 E93–E98 固化來源。** 原 HOT 內的 CURRENT_SCENE／HOLD 只代表當時快照；不得覆寫本 MASTER 截止或 V4.1–V4.4 疊加層。

# 觀止青樓｜白御行線 HOT SAVE V4.0
## 理火三年榴月三日深夜｜三十二娘街行與帳戶指令 × 紅娘顯影場舞台方案 × 錦棠首次正式約會 × 自主購衣與望河樓晚宴 × 私人親密成人事件 × 喜歡確認 × 相擁收幕版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V4_0_LIU03_LATE_NIGHT_JINTANG_FIRST_DATE_PRIVATE_INTIMACY"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V4.0"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V12.0"
  character_source: "觀止人物卡池_LCAPG_V2.3_李清照趙受益錦棠顧青簡增補_薛濤魚玄機暫定入場_正式版.md"

  story_time_span:
    start: "HOT V3.9 後／理火三年榴月二日晚散會後"
    current: "理火三年榴月三日深夜"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_IN_JINTANG_ROOM_AFTER_PRIVATE_ADULT_INTERACTION_HAS_STOPPED_AND_BAI_YUXING_JINTANG_REMAIN_CUDDLING"

  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V3.9_榴月二日晚_長恨歌文會_柳如是東林夜談_趙受益宣和入席_六條楊玉環三人約會開放_散會版.md"
  previous_hot_sha256: "9c95570af9441d695632214e6486c4b2733e3841a65c3742a26a61e66254afa7"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md"
  long_term_master_sha256: "0149362b4128d62d947d4ffbcc618003913b1cad7052d57fe5b3f84f8f05084f"

  save_scope:
    - "HOT V3.9 後至榴月三日深夜之白御行線新增硬事件與玩家明示校正"
    - "榴月三日白御行與白三十二娘場外街行、儀器店／書院人物與顧青簡性別誤寫校正"
    - "白三十二娘、白希、白明礬、白紅伶個人商會帳戶與每月十兩方向之已下達指令／未執行邊界"
    - "紅娘四面可視中央籠台／升降台／燈光／退場通道之演出概念與裝修接線"
    - "錦棠首次正式私人約會：方掌櫃購衣、望河樓晚宴、夜市同行、回觀止"
    - "錦棠自行使用本人資金購物、白御行支付晚餐；金錢與私人關係分軸"
    - "白御行與錦棠首次私人成人親密與性交事件；逐步開放、拒絕、重新開放與最後主動收束分軸"
    - "錦棠身體強烈波峰、餘波、咬人與非語言邊界顯影；不得硬計第二／第三次高潮"
    - "白御行明示喜歡錦棠；錦棠表示相信此『喜歡』，但未回覆對等戀愛承諾"
    - "玩家最後因避免體內射精而停止繼續推進；本夜未成立體內射精"
```

---

# 0｜提交法位、來源與本輪反污染

```yaml
SOURCE_LINEAGE:

  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V3.9_榴月二日晚_長恨歌文會_柳如是東林夜談_趙受益宣和入席_六條楊玉環三人約會開放_散會版.md"
    role: "本檔直接前置 HOT；V3.9 及以前有效硬狀態全部繼承，除本檔明示更新／校正者"
    sha256: "9c95570af9441d695632214e6486c4b2733e3841a65c3742a26a61e66254afa7"

  master_archive:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md"
    role: "截至 HOT V3.4 之長期固化；V3.5→V3.6-R2→V3.7→V3.8→V3.9→本 V4.0 依序作較新合法疊加"
    sha256: "0149362b4128d62d947d4ffbcc618003913b1cad7052d57fe5b3f84f8f05084f"

  current_character_source:
    file: "觀止人物卡池_LCAPG_V2.3_李清照趙受益錦棠顧青簡增補_薛濤魚玄機暫定入場_正式版.md"
    role: "現行跨線人物基線；本輪錦棠約會、成人事件、私人稱呼與白御行關係全部只屬白御行線 ROUTE EVENT"
    sha256: "b7ce5f3e8870b170499e70bfe60b3d6b951987badc795434d7dfd9ef06637d59"

  current_route_conversation_commit:
    role:
      - "HOT V3.9 後至本次 HOT SAVE 命令前之直接劇情"
      - "玩家對自身言行、意圖與 GM 校正"
      - "NPC 可觀察行動、人物本人明示與已成立互動結果"
      - "本串 HOLD／DISCUSSION 中對錯誤輸出之明示撤銷與反污染校正"

  runtime_reference:
    file: "觀止青樓_主程序_V12.0_FIELD_STATE接戲分析器場態整合正式版.md"
    version: "V12.0"
    status: "DOCUMENT_LEVEL_CURRENT_GUANZHI_RUNTIME_SPEC"
    sha256: "2159467f8a1d3eb31a8a0930e7d7b421bd7501a32eff35ceea383288f25a1978"

  experimental_rendering_patch:
    file: "觀止青樓_PATCH_ACTION_BEFORE_EXPLANATION_V0.1-EXP_行動先於說明_顯影優先序修正版.md"
    version: "V0.1-EXP"
    status: "INDEPENDENT_EXP_PATCH_NOT_MERGED_INTO_V12"
    sha256: "0dc94aaad07f6ed2baa3041b667f6e6858f8f4457aab8bb89778f6f3c0eda06e"

  environment_reference:
    file: "理火環境_PATCH_V0.3_生成場完整性_顯影場_多通道顯影_語言化捕獲_SCOPED_REACTIVATION_反向污染阻斷.md"
    version: "V0.3"
    status: "ENVIRONMENT_LEVEL_EXP_REFERENCE_NOT_MERGED"
    sha256: "aa36b72c2a98aa895751fc87d5bf95de4d6664f53e5affaa9dbdca2ed82f1b46"

  adult_interaction_method_pack:
    file: "成人親密與性愛互動心法包_V0.1_AI讀取版_可擴充基線.md"
    version: "V0.1"
    status: "FOUNDATIONAL_REFERENCE_NOT_RUNTIME_AND_NOT_WORLD_FACT"
    sha256: "67fd21ee4d0aa7898608cc36166315b863e8fec134447ead5fa47968b047a8a8"
```

```yaml
COMMIT_NOTE:
  - "本檔取代 HOT V3.9 成為白御行線最新直接接關切片；V3.9 保留為前置歷史來源。"
  - "本次只更新 HOT SAVE；不更新 MASTER、不修改人物卡池、不把任何 EXP PATCH 升格為已併核心。"
  - "文件存在／本輪使用 V12、環境 PATCH、性愛心法作生成參照，不等於宿主底層 Runtime、模型權重或隱藏狀態機已被部署。"
  - "本輪成人事件只記已成立行為、人物當時決定、可觀察反應與明示邊界；不把身體反應、高潮、交易、喜歡、愛、承諾互相偷換。"
  - "本輪 HOLD 討論中形成的『ACTION BEFORE EXPLANATION』『性愛心法』是導演生成方法，不倒灌成錦棠本人知道的術語或世界內制度。"
  - "玩家提出的『第二次／第三次高潮』只屬玩家話語框架，不得保存成錦棠內部計數或已確認生理事件。"
  - "先前錯誤生成的『二、只有二、第三次跟你拚』等報數式錦棠台詞已在本串明示撤銷，不取得世界事實權。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年榴月三日"
  time: "深夜；精確時刻未知"
  primary_location: "觀止青樓／錦棠私人房"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  player:
    name: "白御行"
    current_position: "錦棠房內／床上與錦棠相擁"
    current_state:
      - "已明示本夜成人互動到此結束，不再做最後一段。"
      - "停止原因為擔心控制不住而在錦棠體內射精。"
      - "已表示剩下只陪錦棠。"
      - "玩家是否於本夜其他方式射精：未成立／未描述。"

  jintang:
    name: "錦棠"
    birth_name: "周玉娘"
    current_position: "與白御行相擁"
    current_state:
      - "本夜私人成人互動已停止推進。"
      - "經歷一段明顯強烈身體波峰與後續餘波；人物未自行命名或計數。"
      - "已逐步從高強度身體反應恢復，但非瞬間 RESET。"
      - "最後仍願意靠著白御行、抱著他，並以咬人玩笑延續兩人私下氣氛。"
      - "尚未確認已睡著。"

  direct_resume_point:
    - "下一幕若仍在本夜，可從兩人相擁、低聲聊天、自然入睡或房外新事件接起。"
    - "若玩家明示推進到翌日，才進榴月四日。"
    - "不得替白御行在 HOLD 後自行新增性行為、離房、承諾、付款或睡眠結果。"
    - "不得把錦棠接受『御行喜歡棠兒』倒寫成錦棠已愛上／已承諾戀愛。"
```

---

# 2｜HOT V3.9 繼承後仍活躍之世界背景

```yaml
INHERITED_WORLD_ACTIVE:

  guanzhi_ten_day_closure:
    status: "ACTIVE"
    current_day: "DAY_3"
    ordinary_public_business: "CLOSED"
    internal_operations: "ACTIVE"
    note:
      - "十日整修／暫歇仍在進行；榴月三日為跨月後第三日。"

  hongniang_room_debt_swap:
    status: "ACTIVE"
    room:
      door_leaf: "REMOVED"
      window_sashes: "REMOVED"
      screen: "REMOVED_FOR_MAINTENANCE"
    restore_rule:
      - "重新開業當日上午恢復。"
      - "房間開放結構不等於任何人取得進入、觀看、親近或成人權利。"

  hongxiu_call_right:
    status: "ACTIVE_UNUSED_UNLESS_LATER_EVENT_CONFIRMS"
    core:
      - "白御行已在紅袖十日賭局三擊掌後提前認輸。"
      - "紅袖保有一次召喚白御行回應之權利。"

  zhao_rokujo_yang:
    status: "THREE_PERSON_DATE_DIRECTION_OPEN"
    confirmed:
      - "趙受益可追六條與楊玉環。"
      - "楊玉環已開放趙受益追求。"
      - "六條承認趙可追其他女人，保留嫉妒、不舒服與退出權。"
      - "三人約會可以嘗試；日期、地點尚未定。"
      - "首次三人約會由趙受益私人請客。"
    not_confirmed:
      - "戀愛"
      - "排他關係"
      - "三人成人事件"
      - "婚姻"
      - "永久同意"

  yang_yuhuan:
    lodging_and_expense:
      - "仍可自主留觀止數日；非掛牌、非所有權。"
      - "向李隆基請款方向仍只屬請款流程；不等於李隆基已承認債務或付款。"

  dingtao_business:
    active:
      - "曹州假印案仍為當前 ACTIVE 商會案件。"
      - "烤鹽案早已併入廣源→西門慶→高衙內→高俅→蔡京大案鏈，不應再獨立當未結主案。"
      - "京師女性貼身衣物／奢侈品旗艦專案由常煒副會長承接。"
      - "辭歲／錦棠客戶帳戶、商會對外債權與付款方債務必須分軸。"
```

---

# 3｜LIU03-DAY-E01｜白三十二娘街行、儀器與顧青簡誤寫校正

```yaml
STREET_OUTING:
  event_id: "LIU03-DAY-E01-SANSHIERNIANG-INSTRUMENT-STREET-OUTING"
  event_axis_state: "COMPLETED_WITH_LIMITED_NEW_NPC"

  participants:
    - "白御行"
    - "白三十二娘"

  observed:
    - "二人曾於榴月三日白日／日間場外逛街。"
    - "接觸到外來／進口天文、測量類儀器，其中包含望遠筒式長筒器具。"
    - "此事件只建立觀止世界中相關器物可見／可研究的場景事實，不自動建立完整近代科學體系。"

  minimal_npc:
    name: "沈衡之"
    sex: "男"
    age: "約四十"
    affiliation: "澄明書院"
    observed_role:
      - "研究／關注相關儀器。"
    persistence: "MINIMAL_ROUTE_NPC_UNLESS_LATER_PROMOTED"

  astronomy_note:
    - "榴月三日傍晚／入夜後可見初三小弦月；此為當時場景觀察條件。"

  corruption_correction:
    revoked:
      - "先前某輸出將顧青簡寫成男性出現在此場。"
    correct:
      - "顧青簡是女性，定陶商會固定女性師爺。"
      - "該男性顧青簡版本作廢，不得存檔。"
```

---

# 4｜LIU03-DAY-E02｜白家四女個人帳戶方向

```yaml
WHITE_FOUR_ACCOUNT_DIRECTION:
  event_id: "LIU03-DAY-E02-WHITE-FOUR-PERSONAL-ACCOUNT-INSTRUCTION"
  event_axis_state: "PLAYER_INSTRUCTION_GIVEN_EXECUTION_PENDING"

  persons:
    - "白三十二娘"
    - "白希"
    - "白明礬"
    - "白紅伶"

  player_instruction:
    - "白御行提出／指示四人之後各自開定陶商會個人帳戶。"
    - "方向為每人每月十兩，進本人帳戶。"

  shisanniang:
    confirmed:
      - "白三十二娘本人已聽到並接受自己這一份方向。"
    cannot_speak_for:
      - "白希"
      - "白明礬"
      - "白紅伶"

  contract_axis:
    - "四人的既有身契／死契仍由原契約法位處理；帳戶與月錢不自動改變身契。"
    - "契約所有權不等於勞動免費；月錢若實際執行仍是本人財產。"

  execution_axis:
    account_opened:
      白三十二娘: "NOT_CONFIRMED"
      白希: "NOT_CONFIRMED"
      白明礬: "NOT_CONFIRMED"
      白紅伶: "NOT_CONFIRMED"
    first_month_payment: "NOT_CONFIRMED"

  anti_promotion:
    - "不得把『明日／之後去開戶』寫成已完成開戶。"
```

---

# 5｜LIU03-DAY-E03｜申聊契約故事的法位

```yaml
SHENLIAO_ANECDOTE:
  event_id: "LIU03-DAY-E03-SHENLIAO-CONTRACT-ANECDOTE"
  event_axis_state: "PLAYER_TESTIMONY_ONLY"

  player_told:
    - "白御行曾提及一名叫申聊的舊奴例子：原為士族／貴族出身、愛與人爭契約範圍。"
    - "白御行稱自己以二貫買下並為其寫過極細、極長的契約。"

  save_law:
    - "此為玩家自述／故事材料，未在本輪取得外部文書驗證。"
    - "不得據此補造具體歷史法條、契約全文或申聊跨線人物卡。"
```

---

# 6｜LIU03-DAY-E04｜紅娘中央籠台／顯影場演出方案

```yaml
HONGNIANG_PERFORMANCE_CONCEPT:
  event_id: "LIU03-DAY-E04-HONGNIANG-CENTRAL-CAGE-PERFORMANCE-CONCEPT"
  event_axis_state: "CONCEPT_ACCEPTED_FOR_HARDWARE_TRIAL_TERMS_PENDING"

  concept:
    - "中央設四面可視籠台／表演空間。"
    - "表演者處於明亮光線，觀眾在較暗處。"
    - "觀眾只能觀看，不得伸手觸碰、指揮或以加價要求表演內容。"
    - "固定門票／入場收費；觀眾數與票帳於事後核算，不在演前以數字壓迫表演者。"

  hongniang_interest:
    - "紅娘對『被看、由自己控制展示、觀眾不能碰』的結構有興趣。"
    - "此興趣符合她的展示性、注意力與控制傾向，但不是已完成正式演出。"

  hongniang_conditions:
    - "場內必須有足夠站、走、坐、躺與轉身空間。"
    - "表演者自己控制退場。"
    - "不得讓觀眾伸手穿越／觸碰。"
    - "道具由紅娘自己選。"
    - "不得以喊話、付費點單、臨場指令控制表演者。"
    - "具體表演內容與尺度仍由表演者本人決定。"

  compensation:
    - "紅娘若正式演出，方向為固定演出費。"
    - "觀止承擔門票收益／損失；不是把票房風險轉嫁給紅娘。"
    - "正式演出費金額尚未確認。"

  hardware:
    - "十日整修可預留中央模組化升降台／籠架固定點。"
    - "可預留方向性燈光、觀眾後退距離與表演者緊急／自主退場通道。"
    - "潘金蓮接受先做硬體兼容／空場測試方向；正式演出條件仍須另談。"

  two_performer_possibility:
    - "未來可有兩名成年表演者共同演出，但雙方都必須各自保有同等行動與退出主權。"
    - "目前沒有確定第二表演者、演出日或成人內容。"

  legal_unknown:
    - "尚未出閣之成年女子若進行公開高尺度表演，在當前世界具體登記／營業法位仍未解決。"
```

---

# 7｜LIU03-DATE-E01｜錦棠首次正式私人約會成立

```yaml
JINTANG_FIRST_DATE:
  event_id: "LIU03-DATE-E01-JINTANG-FIRST-REAL-DATE"
  event_axis_state: "COMPLETED"

  date: "理火三年榴月三日"
  nature:
    - "白御行與錦棠第一次以私人約會而非拍賣／接客／觀止服務名義外出。"
    - "錦棠當前處於不掛牌接客的自由期／私人生活階段；其官府妓籍歷史不因本輪自動抹除。"

  participants:
    main:
      - "白御行"
      - "錦棠"
    attendant:
      - "白希"
    note:
      - "白希為陪同／協助，不取得兩人私人關係法位。"

  jintang_theme:
    - "本日核心不是被人定價，而是她自己挑、自己花、自己決定。"
```

---

# 8｜LIU03-DATE-E02｜方掌櫃購衣與錦棠自主支出

```yaml
CLOTHING_EVENT:
  event_id: "LIU03-DATE-E02-JINTANG-CLOTHING-SPENDING"
  event_axis_state: "COMPLETED_WITH_ACCOUNT_SETTLEMENT_ROUTED"

  at_shop:
    - "白御行本日明示不作『金主主人』，主要讓錦棠挑選。"
    - "錦棠替白御行選約六組不同用途／場合的男裝布料與搭配方向。"
    - "錦棠也替自己選購衣物。"
    - "二人另有成衣可當場換上，之後穿新衣繼續約會。"

  payment:
    payer: "錦棠"
    mechanism:
      - "錦棠本人簽帳／確認。"
      - "帳款經定陶商會接口自她本人帳戶處理。"
      - "白希負責協助檢查／跟單。"
    anti_merge:
      - "衣物不是白御行送她的禮物。"
      - "錦棠花的是自己可支配的錢。"
      - "不得因白御行是定陶商會會長就把錦棠個人消費改成白御行私人支出。"

  jintang_financial_expression:
    established_meaning:
      - "她第一次在大額消費中實際感受到：想花時花得起，花完以後仍有自己的資產。"
```

---

# 9｜LIU03-DATE-E03｜望河樓晚宴

```yaml
WANGHELOU_DINNER:
  event_id: "LIU03-DATE-E03-WANGHELOU-DINNER"
  event_axis_state: "COMPLETED"

  jintang_choice:
    venue: "望河樓"
    meaning:
      - "錦棠自己選擇一個過去對她而言價格高、難以隨意消費的地方。"

  seating:
    - "錦棠選擇二樓靠外／可看見樓下的開放位置。"
    - "此選擇與她過去曾只能從下面看高處的生活經驗形成對照。"

  payment:
    dinner_payer: "白御行"
    clothing_payer: "錦棠"
    rule:
      - "晚餐由白御行付，不改寫錦棠先前自主購衣。"

  relation_language:
    - "錦棠對白御行使用『我們小姐』等被陪伴／被照應的語境有正面反應。"
```

---

# 10｜LIU03-DATE-E04｜白御行過去想買錦棠的坦白

```yaml
PAST_PURCHASE_DISCLOSURE:
  event_id: "LIU03-DATE-E04-BAI-PAST-WANTED-TO-BUY-JINTANG"
  event_axis_state: "COMPLETED_DISCLOSURE"

  player_disclosed:
    - "白御行坦白：當初錦棠還是六百兩價位時，他其實曾想直接買下她。"
    - "但因自己先前已承諾不替她決定／不直接把她拿走，最後沒有買。"
    - "他後來曾後悔看著她被別人帶走。"
    - "現在願意約她，是因為對她本人有吸引／喜歡，而不是單純因價格。"

  jintang_response:
    - "錦棠沒有把此坦白改寫成『當初你就擁有我』。"
    - "她指出現在白御行不是買不起，而是已不能只靠買就取得她。"

  relation_effect:
    - "兩人關係明確從『可被價格處理』轉向需要由約會、互動與人物自身選擇繼續形成。"
```

---

# 11｜LIU03-DATE-E05｜約會後續與下一次約會方向

```yaml
DATE_FUTURE_DIRECTION:
  event_id: "LIU03-DATE-E05-NEXT-DATE-DIRECTION"
  event_axis_state: "OPEN_DIRECTION_NOT_SCHEDULED"

  confirmed:
    - "錦棠表示今日約會表現好可有『獎勵／後續』，但沒有把獎勵定成付款、成人服務或特定身體行為。"
    - "她留下可能由自己觀察明日／主動發起下次約會的空間。"
    - "她要求白御行別把下次約會又問成價錢問題。"

  not_confirmed:
    - "下一次日期"
    - "下一次地點"
    - "下次一定由誰邀"
    - "下次必有成人事件"
```

---

# 12｜LIU03-DATE-E06｜夜市同行與回觀止

```yaml
NIGHT_MARKET_AND_RETURN:
  event_id: "LIU03-DATE-E06-NIGHT-MARKET-RETURN"
  event_axis_state: "COMPLETED"

  night_market:
    - "白御行與錦棠於夜市繼續同行。"
    - "牽手成立。"
    - "白御行在人流中有護腰／貼身保護式接觸；錦棠未因此中止同行。"

  return:
    - "回觀止後，錦棠沒有選公共夜宵或其他人群收尾，而是選擇回自己房間。"
    - "白希在私人場景開始前被支開／退出，不參與後續私人成人事件。"
```

---

# 13｜LIU03-INTIMACY-E01｜私人稱呼與關係位置

```yaml
PRIVATE_NAMES:
  event_id: "LIU03-INTIMACY-E01-PRIVATE-NAMES"
  event_axis_state: "COMPLETED"

  jintang_to_player:
    private_name: "御行"
    status: "ACTIVE_PRIVATE_ADDRESS"

  player_to_jintang:
    private_name: "棠兒"
    status: "ACTIVE_PRIVATE_ADDRESS"

  significance:
    - "錦棠明示『棠兒』是第一次讓男人以此私人方式稱呼她。"
    - "私人稱呼建立親密資格，但不等於婚姻、排他戀愛或所有權。"
```

---

# 14｜LIU03-INTIMACY-E02｜初段親密、第一次明確阻擋與停止

```yaml
INITIAL_INTIMACY:
  event_id: "LIU03-INTIMACY-E02-INITIAL-KISS-HUG-FIRST-STOP"
  event_axis_state: "COMPLETED_WITH_BOUNDARY_HISTORY"

  established:
    - "兩人先從靠近、擁抱、接吻逐步進入私人身體互動。"
    - "初段錦棠允許手、手臂、肩、背、腰等接觸；更深入部位並非一開始全面開放。"
    - "錦棠同意接吻，但初段明確維持『先只是親』的限制。"

  first_stop_event:
    - "白御行曾試圖把節奏推到床上／更進一步脫衣。"
    - "錦棠當場阻止。"
    - "白御行停止推進。"
    - "錦棠重新整理衣物後仍願意保留接吻／擁抱。"

  consequence:
    - "該次阻擋是已發生的硬邊界歷史，不得被後續成人事件抹除。"
    - "同時該次阻擋沒有自動終止整個私人互動；後續是否重開由錦棠本人另行決定。"
```

---

# 15｜LIU03-INTIMACY-E03｜錦棠本人重新開放並進入成人事件

```yaml
JINTANG_REOPENS:
  event_id: "LIU03-INTIMACY-E03-JINTANG-REOPENS-ADULT-INTERACTION"
  event_axis_state: "COMPLETED"

  jintang_choice:
    - "在前一段停止後，錦棠後續由自己重新決定繼續。"
    - "她逐步自行脫衣／開放更多身體接觸。"
    - "她明示：想繼續是因為自己現在想要，不是因為約會很好所以欠白御行，也不是因為白御行花錢。"

  anti_transaction:
    - "本夜成人互動不是晚餐、衣服、拍賣款、約會品質的付款／回報。"
    - "白御行對錦棠的金錢能力與定陶位置不取得其身體決定權。"
```

---

# 16｜LIU03-INTIMACY-E04｜探索、主導權與反標籤

```yaml
EXPLORATION:
  event_id: "LIU03-INTIMACY-E04-JINTANG-EXPLORATION"
  event_axis_state: "COMPLETED"

  confirmed:
    - "錦棠主動探索白御行身體，表現為好奇、試驗與學習，而非被寫成已很熟練的成人老手。"
    - "她在身體探索中逐步調整允許程度。"
    - "她對更深入的手部／身體探索採『慢、舒服、不以最多為目標』的方向。"

  jintang_position:
    - "她拒絕被白御行／導演固定成『浪女』『蕩女』等人格標籤。"
    - "她可以有真實聲音、失控、主動、挑逗，但不願為取悅白御行而把自己重新變成職業客人表演。"

  performance_axis:
    - "本夜以私人真實探索為主；故意演給男人看的職業表演不是預設。"
```

---

# 17｜LIU03-INTIMACY-E05｜性交成立、先靜止、錦棠自行找節奏

```yaml
INTERCOURSE_EVENT:
  event_id: "LIU03-INTIMACY-E05-INTERCOURSE"
  event_axis_state: "COMPLETED"

  participants:
    - "白御行"
    - "錦棠"

  confirmed:
    - "成年雙方本夜自願性交已成立。"
    - "白御行是錦棠繼乾隆之後的第二名男性性伴侶；此資訊只作用於白御行線既有事件理解，不代表她因此成為熟練人物。"

  entry_and_initial_pacing:
    - "錦棠在真正進入後一開始要求先不要動。"
    - "她先用時間適應身體感受。"
    - "之後由她自己先做小幅度動作、試探節奏與角度。"

  agency:
    - "錦棠一度要求白御行不要先接手，自己先試。"
    - "她在試驗後才逐步與白御行配合，後續也有把節奏交回／讓白御行主導的時段。"

  meaning:
    - "本事件不能被簡化成『白御行做、錦棠承受』；錦棠有實際動作、節奏選擇與中途調整。"
```

---

# 18｜LIU03-INTIMACY-E06｜體內射精／懷孕軸

```yaml
EJACULATION_AND_PREGNANCY_AXIS:
  event_id: "LIU03-INTIMACY-E06-INTERNAL-EJACULATION-RESERVED"
  event_axis_state: "BOUNDARY_ESTABLISHED_AND_RESPECTED"

  jintang:
    - "本夜不接受白御行在她體內射精。"
    - "她對自身週期／懷孕風險並無足夠把握，因此把懷孕／體內射精視為另一筆需要另說的事。"

  player:
    - "白御行接受此分離。"
    - "本夜後段白御行主動提出停止最後一段，原因正是擔心自己忍不住在她體內射精。"

  outcome:
    internal_ejaculation: "DID_NOT_OCCUR"
    player_ejaculation_otherwise: "UNKNOWN_NOT_CONFIRMED"
    pregnancy_result: "NO_CLAIM"
```

---

# 19｜LIU03-INTIMACY-E07｜強烈身體波峰、餘波與反計數校正

```yaml
JINTANG_BODY_PEAK:
  event_id: "LIU03-INTIMACY-E07-JINTANG-STRONG-BODY-PEAK"
  event_axis_state: "COMPLETED_OBSERVABLE_BODY_EVENT"

  observed:
    - "錦棠在性交過程中出現一段明顯強烈身體波峰。"
    - "可觀察反應包含呼吸失序、身體顫抖／收縮、抓握與之後的敏感餘波。"
    - "波峰後她沒有立刻恢復完整分析語言；曾需要安靜、等待與逐步恢復。"

  naming:
    jintang_self_label: "NONE"
    save_label:
      - "SAVE 保留為『明顯強烈身體波峰／高潮樣反應』。"
      - "不強迫錦棠本人報數或命名。"

  invalidated_counting:
    - "玩家曾以『第二次／第三次』鼓勵她；該措辭不取得錦棠內部狀態指令權。"
    - "先前錯誤輸出讓錦棠說『二、只有二』『第三次跟你拚』等已明示撤銷。"
    - "本夜第二次／第三次完整高潮均 NOT_CONFIRMED。"

  residue:
    - "強烈波峰後仍有過度敏感、身體偶發收縮、需要停頓與重新找節奏的餘波。"
```

---

# 20｜LIU03-INTIMACY-E08｜咬人、打鬧與當晚停下訊號

```yaml
BITING_AND_BOUNDARY_SIGNAL:
  event_id: "LIU03-INTIMACY-E08-BITING-BOUNDARY-SIGNAL"
  event_axis_state: "COMPLETED_SCENE_SPECIFIC_CONVENTION"

  biting:
    - "錦棠在高強度互動中曾咬白御行肩膀，留下可見牙印。"
    - "她也曾以手捶／拍白御行，屬當時雙方接受的放肆／打鬧表達。"
    - "恢復一些之後，錦棠查看自己留下的牙印，並曾再次故意較輕地咬同一處。"
    - "本夜後段『你又會咬我／棠兒想多練幾次』成為兩人的私下玩笑。"

  stop_signal_scene_specific:
    - "錦棠曾在本夜示範以三下拍擊／明確叫停作為自己可用的清楚停止訊號。"
    - "此為本夜兩人的具體互動默契，不升格為所有女性、所有性愛或未來所有場景的通則。"

  anti_misread:
    - "咬、抓、捶不自動等於拒絕，也不自動等於全面同意；意義依當時人物行動與場連續性。"
```

---

# 21｜LIU03-INTIMACY-E09｜HOLD 討論造成的導演規則，不寫入人物

```yaml
DIRECTOR_METHOD_AUDIT:
  event_id: "LIU03-INTIMACY-E09-DIRECTOR-METHOD-HOLD"
  event_axis_state: "OUT_OF_STORY_DISCUSSION_NOT_WORLD_EVENT"

  discussion_results:
    - "使用者指出成人互動大量依靠身體、表情、手勢、距離與行動顯影邊界，導演不應逼人物每次口頭朗讀規則。"
    - "形成 ACTION BEFORE EXPLANATION 獨立 PATCH。"
    - "形成成人親密與性愛互動心法包 V0.1。"
    - "理火環境 V0.3 被作為多通道顯影、STATE != LANGUAGE 的環境級實驗參照。"

  world_effect:
    - "NONE_DIRECT"
    - "上述內容只改變導演之後如何生成／顯影，不代表錦棠學會理火術語或世界新增成人法規。"
```

---

# 22｜LIU03-INTIMACY-E10｜白御行「喜歡」明示與錦棠接受其可信性

```yaml
LIKING_DISCLOSURE:
  event_id: "LIU03-INTIMACY-E10-BAI-LIKES-JINTANG"
  event_axis_state: "COMPLETED_RELATION_DISCLOSURE"

  player_statement:
    - "白御行對錦棠表示：現在若說愛她，她可能不會信；但他問如果說『我喜歡妳』，她是否相信。"

  jintang_response:
    - "錦棠表示『這個我信』。"
    - "她區分『愛』太大、目前仍沒有足夠證據，與『喜歡』可以從白御行先前行動中看見。"
    - "她接受『御行喜歡棠兒』這句，明示『這句我收』。"

  relation_state:
    bai_to_jintang:
      liking: "EXPLICITLY_DECLARED"
      love: "NOT_DECLARED_AS_CURRENT_FACT"
    jintang_to_bai:
      believes_bai_likes_her: true
      reciprocal_liking: "NOT_EXPLICITLY_DECLARED"
      love: "NOT_CONFIRMED"
      exclusivity: "NOT_CONFIRMED"
      romantic_commitment: "NOT_CONFIRMED"

  anti_promotion:
    - "不得因錦棠相信白御行喜歡她，就補成『我也喜歡你』。"
```

---

# 23｜LIU03-INTIMACY-E11｜白御行主動收束與相擁陪伴

```yaml
ENDING_EVENT:
  event_id: "LIU03-INTIMACY-E11-PLAYER-STOPS-AND-CUDDLES"
  event_axis_state: "COMPLETED"

  player_choice:
    - "白御行明示：最後一段不做了。"
    - "原因為擔心自己忍不住在錦棠體內射精。"
    - "他表示剩下就這樣結束，陪著錦棠。"

  jintang_response:
    - "錦棠不再維持準備繼續的動作，逐步放鬆並留在白御行懷裡。"
    - "她把被子拉向兩人，繼續靠著、抱著。"
    - "她指出白御行今天常在『明明還可以再拿一些』時自己停下。"
    - "她最後表示今晚不要再證明什麼，白御行陪她即可。"

  final_banter:
    - "白御行玩笑說自己只是怕忍不住射出來又被她咬。"
    - "錦棠以咬人作私人打趣，沒有因此重啟成人事件。"

  current_result:
    adult_interaction: "STOPPED"
    cuddling: "ACTIVE"
    sleep: "NOT_YET_CONFIRMED"
```

---

# 24｜錦棠本輪資產／職業／身份狀態

```yaml
JINTANG_ROUTE_STATUS:

  baseline_identity:
    birth_name: "周玉娘"
    prostitution_register_name: "錦棠"
    adult: true
    baseline_entry_price_taels: 600
    baseline_buyer: "潘金蓮"

  auction_history:
    buyer_for_one_night: "乾隆"
    auction_price_taels: 5000000
    jintang_share_rate: "15%"
    jintang_share_taels: 750000
    note:
      - "錦棠私人份額與商會對付款方之債權／清算為不同帳。"

  account:
    dingtao_private_account: "ESTABLISHED_AND_USABLE_BY_CURRENT_ROUTE"
    evidence:
      - "本日方掌櫃購衣由錦棠本人帳戶承擔。"
    exact_current_balance: "NOT_RECALCULATED_IN_THIS_SAVE"

  free_period:
    - "當前路線仍處於二十八日自由／休整期與私人生活安排。"
    - "本輪約會與成人事件是她本人私人選擇，不等於重新掛牌接客。"
    - "官府曾以『錦棠』登妓籍的歷史仍存在；正式脫籍／法律身份變更若有，需另有硬事件。"

  runway_star_direction:
    status: "ACCEPTED_DIRECTION_NOT_COMPLETED"
    - "錦棠已接受約三個月走秀／女裝／明星化訓練方向。"
    - "目標之一是建立不只依附『乾隆五百萬睡過的女人』的新名聲。"
    - "訓練不等於經紀約已簽、不等於成人服務同意。"

  staffing:
    - "牙行已持續為錦棠／辭歲帶成年候選人。"
    - "白希曾作錦棠臨時協助／陪同。"
    - "錦棠永久私人丫鬟／雇員本輪沒有完成最後簽約。"
```

---

# 25｜白御行 × 錦棠關係矩陣【截至本 HOT】

```yaml
RELATION_MATRIX_BAI_JINTANG:

  known_history:
    - "白御行曾在錦棠六百兩階段想買她但沒有執行。"
    - "錦棠後來由乾隆五百萬一夜競拍成交，取得十五分成。"
    - "白御行與錦棠已完成第一次正式私人約會。"
    - "白御行是錦棠第二名已確認男性性伴侶。"

  trust_and_readability:
    confirmed_events:
      - "錦棠曾明確阻止更快升階，白御行當時停止。"
      - "錦棠後續由自己重新開放。"
      - "兩人建立御行／棠兒私人稱呼。"
      - "白御行明示喜歡，錦棠表示相信。"

  desire:
    this_night:
      - "錦棠後續成人行為存在她本人主動意願與主動節奏。"
    persistence_beyond_this_night: "UNKNOWN"

  affection:
    bai_liking_jintang: "EXPLICIT"
    jintang_believes_it: "EXPLICIT"
    jintang_liking_bai: "UNDECIDED_NOT_DECLARED"
    love: "UNDECIDED"
    exclusivity: "NONE_ESTABLISHED"

  money:
    - "白御行支付本日晚餐。"
    - "錦棠自行支付衣物。"
    - "成人事件不得被記為錦棠償還晚餐、衣服、拍賣或商會利益。"

  next_date:
    status: "OPEN_NOT_SCHEDULED"
```

---

# 26｜成人事件硬狀態總結【不得抽象化】

```yaml
ADULT_EVENT_HARD_STATE:

  participants:
    - "白御行"
    - "錦棠"

  both_adults: true

  occurred:
    - "接吻"
    - "擁抱"
    - "逐步裸體／身體探索"
    - "手部與身體成人接觸"
    - "自願性交"
    - "錦棠主動調整／嘗試節奏"
    - "至少一段明顯強烈身體波峰／高潮樣反應"
    - "咬肩留下牙印"
    - "成人互動後相擁陪伴"

  refusal_boundary_history:
    - "前段白御行推進過快時，錦棠曾阻止；白御行停止。"
    - "該次阻止不因後續性交成立而被刪除。"

  reopened_by_jintang:
    - "後續繼續與升階由錦棠本人另行開放。"

  not_occurred_or_not_confirmed:
    internal_ejaculation: "DID_NOT_OCCUR"
    player_ejaculation: "NOT_CONFIRMED"
    pregnancy: "NO_RESULT_CLAIM"
    second_orgasm: "NOT_CONFIRMED"
    third_orgasm: "NOT_CONFIRMED"
    romantic_commitment: "NOT_CONFIRMED"
    exclusivity: "NOT_CONFIRMED"

  final_state:
    - "白御行主動停止最後一段。"
    - "兩人沒有因停止而翻臉／分開；仍相擁。"
```

---

# 27｜本輪人物去污染與撤銷清單

```yaml
CORRECTIONS_NOT_WORLD_FACTS:

  jintang_orgasm_counter:
    revoked:
      - "錦棠清楚報『二』"
      - "『只有二』"
      - "『第三次跟你拚』"
    reason:
      - "把玩家的計數框架倒灌成錦棠內部狀態。"
      - "與強烈身體狀態下的注意／語言連續性不符。"

  jintang_governance_speech:
    warning:
      - "本串曾一度讓錦棠過度口頭解說成人邊界，呈現人物使用說明書式治理語言。"
    treatment:
      - "不需要逐句撤銷所有已發生台詞；但不得把治理語氣升格成她固定人格聲音。"
      - "後續優先以符合人物的動作、距離、表情與必要最小語言顯影。"

  gu_qingjian_gender:
    revoked:
      - "男性顧青簡"
    correct:
      - "女性顧青簡／定陶固定女性師爺"
```

---

# 28｜本輪新增導演實驗資料【非世界事件】

```yaml
EXPERIMENTAL_LEARNING_REFERENCES:

  action_before_explanation:
    file: "觀止青樓_PATCH_ACTION_BEFORE_EXPLANATION_V0.1-EXP_行動先於說明_顯影優先序修正版.md"
    status: "INDEPENDENT_EXP_NOT_MERGED"
    purpose:
      - "人物決定形成後，能以行動顯影時優先不要強迫人物自我解說。"

  adult_interaction_method_pack:
    file: "成人親密與性愛互動心法包_V0.1_AI讀取版_可擴充基線.md"
    status: "FOUNDATIONAL_REFERENCE"
    purpose:
      - "提供身體連續性、節奏累積、注意頻寬、波峰餘波、雙向回饋、局部邊界、人體力學、表演與真實等觀察姿態。"

  lihuo_environment_v0_3:
    file: "理火環境_PATCH_V0.3_生成場完整性_顯影場_多通道顯影_語言化捕獲_SCOPED_REACTIVATION_反向污染阻斷.md"
    status: "EXP_REFERENCE_NOT_MERGED"
    purpose:
      - "STATE != LANGUAGE"
      - "MANIFESTATION != EXPLANATION"
      - "MULTI_CHANNEL_MANIFESTATION"
      - "NO_CHANNEL_SUPREMACY"

  save_rule:
    - "以上文件只影響導演生成／審計方法，不建立白御行線內新的可觀察世界事件。"
```

---

# 29｜榴月三日後仍亮之 OPEN THREADS

```yaml
OPEN_THREADS:

  jintang:
    - "今晚相擁之後是否入睡、何時入睡：尚未演出。"
    - "下一次約會由誰提出、日期地點：未定。"
    - "錦棠是否對白御行形成可明示的喜歡／戀愛：未決。"
    - "錦棠三個月走秀／女裝／明星化訓練後續。"
    - "錦棠私人丫鬟／雇員最終選人與契約。"
    - "錦棠帳戶後續理財與大額資產安排。"

  hongniang:
    - "中央籠台硬體空場測試。"
    - "正式演出費、正式演出內容、日期與是否真的演出均未定。"
    - "房門／窗扇／屏風十日換債仍在計時。"

  white_four:
    - "四人個人商會帳戶尚待實際辦理。"
    - "每月十兩尚待真正入帳。"

  hongxiu:
    - "一次召喚白御行回應之權利仍未使用，除非後續另有已發生事件更新。"

  zhao_rokujo_yang:
    - "三人約會尚未排期。"
    - "趙受益對兩人的追求仍需靠實際事件推進。"

  yang_yuhuan:
    - "李隆基請款流程結果未知。"
    - "白明礬／聰明丫鬟候選是否正式配置尚待人物本人與後續事件。"

  dingtao:
    - "曹州案進度有進展再回報。"
    - "朱明長債／短債實際簽約狀態仍依較新帳務文件與後續事件確認。"
    - "京師女性貼身衣物／奢侈品旗艦專案由副會長續辦。"
```

---

# 30｜下一幕接關規則

```yaml
DIRECT_RESUME:

  scene_anchor:
    date: "理火三年榴月三日"
    time: "深夜"
    location: "錦棠私人房／床上"
    player_position: "與錦棠相擁"
    adult_event: "STOPPED"
    conversation_status: "可繼續，但目前沒有必答問題"

  immediate_field:
    - "錦棠身體已從高強度波峰恢復一部分，但仍保留疲勞／敏感／餘波，不得無因瞬間 RESET。"
    - "兩人最後氣氛是親密、打趣與陪伴，不是重新開戰或成人升階命令。"
    - "白御行已清楚選擇不再繼續最後一段。"
    - "錦棠已接受白御行『喜歡她』的可信性，但未回覆對等承諾。"

  resume_options_as_world_paths_not_menu:
    - "本夜繼續低聲聊天。"
    - "自然安靜／入睡。"
    - "房外或觀止內部發生新動靜。"
    - "玩家明示直接推進翌日。"

  forbidden_autofill:
    - "不得自動補白御行射精。"
    - "不得自動補體內射精／懷孕。"
    - "不得自動補錦棠第二／第三次高潮。"
    - "不得自動補錦棠說『我也喜歡你／我愛你』。"
    - "不得把今夜性交變成戀愛、婚約、所有權或下次性愛保證。"
    - "不得在玩家未決定前讓白御行離房、睡著、付新錢、做新承諾。"
```

---

# 31｜一句接關摘要

> **榴月三日深夜，白御行與錦棠完成第一次真正以私人選擇為核心的約會：錦棠用自己的帳戶買衣、在望河樓坐到過去只能仰望的位置，接受白御行坦白當初想買她卻沒有下手，也把兩人的關係推到「現在不能只靠買」的位置。夜市後她自行選擇回房，前段曾明確阻止過快升階，白御行停止；之後由錦棠本人重新開放，兩人逐步探索並自願性交。錦棠在過程中自己找節奏、出現一段強烈身體波峰與餘波，沒有被保存成第二／第三次高潮計數；她咬白御行肩膀留下牙印，咬人也成了兩人的私人玩笑。錦棠本夜不接受體內射精；最後白御行因怕失控內射而主動停止最後一段，只留下來陪她。白御行明示「我喜歡妳」，錦棠說她相信，並收下「御行喜歡棠兒」這句，但沒有回覆對等戀愛承諾。現在兩人仍在錦棠房內相擁，成人互動已停止，睡眠與翌日尚未發生。**

---

# 32｜SOURCE LOCK

```yaml
SOURCE_LOCK_V4_0:
  previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V3.9_榴月二日晚_長恨歌文會_柳如是東林夜談_趙受益宣和入席_六條楊玉環三人約會開放_散會版.md"
    sha256: "9c95570af9441d695632214e6486c4b2733e3841a65c3742a26a61e66254afa7"

  master:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md"
    sha256: "0149362b4128d62d947d4ffbcc618003913b1cad7052d57fe5b3f84f8f05084f"

  character_pool:
    file: "觀止人物卡池_LCAPG_V2.3_李清照趙受益錦棠顧青簡增補_薛濤魚玄機暫定入場_正式版.md"
    sha256: "b7ce5f3e8870b170499e70bfe60b3d6b951987badc795434d7dfd9ef06637d59"

  guanzhi_v12:
    file: "觀止青樓_主程序_V12.0_FIELD_STATE接戲分析器場態整合正式版.md"
    sha256: "2159467f8a1d3eb31a8a0930e7d7b421bd7501a32eff35ceea383288f25a1978"

  action_before_explanation_patch:
    file: "觀止青樓_PATCH_ACTION_BEFORE_EXPLANATION_V0.1-EXP_行動先於說明_顯影優先序修正版.md"
    sha256: "0dc94aaad07f6ed2baa3041b667f6e6858f8f4457aab8bb89778f6f3c0eda06e"

  lihuo_environment_v0_3:
    file: "理火環境_PATCH_V0.3_生成場完整性_顯影場_多通道顯影_語言化捕獲_SCOPED_REACTIVATION_反向污染阻斷.md"
    sha256: "aa36b72c2a98aa895751fc87d5bf95de4d6664f53e5affaa9dbdca2ed82f1b46"

  adult_intimacy_method_pack:
    file: "成人親密與性愛互動心法包_V0.1_AI讀取版_可擴充基線.md"
    sha256: "67fd21ee4d0aa7898608cc36166315b863e8fec134447ead5fa47968b047a8a8"
```

---

# 33｜最終狀態

```yaml
FINAL_STATE:
  latest_hot: "V4.0"
  story_date: "理火三年榴月三日深夜"
  player_location: "錦棠房"
  player_with: "錦棠"
  adult_interaction: "STOPPED"
  cuddling: "ACTIVE"
  sleep: "UNKNOWN_NOT_YET_CONFIRMED"
  next_day: "NOT_REACHED"
  master_updated: false
  character_pool_updated: false
  v12_modified: false
  exp_patches_merged: false
```


<!-- PROMOTED_SOURCE_END: 觀止青樓_白御行線_HOT_SAVE_V4.0_榴月三日深夜_錦棠首次正式約會_自主購衣望河樓_私人成人事件_喜歡確認_相擁收幕版.md -->


<!-- END INHERITED MASTER V4.4-R1 FULL ARCHIVE -->


<!-- BEGIN PROMOTED HOT SOURCE: 觀止青樓_白御行線_HOT_SAVE_V4.1_榴月四日午後_九人丫鬟遴選_牙行成交_制服剪髮_白希明礬分教_落選吃麵收尾版.md -->

# 觀止青樓｜白御行線 HOT SAVE V4.1
## 理火三年榴月四日午後｜錦棠晨起 × 五女丫鬟遴選 × 兩牙行二十三人雙向選擇 × 九人成交 × 制服剪髮 × 白希明礬分教 × 十四名落選者吃麵收尾版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V4_1_LIU04_AFTERNOON_MAID_SELECTION_YAHANG_PURCHASE_UNIFORM_HAIRCUT_TRAINING_NOODLE_CLOSE"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V4.1"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V12.0"
  character_source: "觀止人物卡池_LCAPG_V2.3_李清照趙受益錦棠顧青簡增補_薛濤魚玄機暫定入場_正式版.md"

  story_time_span:
    start: "HOT V4.0 後／理火三年榴月三日深夜"
    current: "理火三年榴月四日午後早段"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AT_GUANZHI_AFTER_MAID_SELECTION_PURCHASE_AND_TRAINING_HANDOFF; BAI_SANSHIERNIANG_TAKES_14_UNSELECTED_CANDIDATES_OUT_FOR_NOODLES"

  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V4.0_榴月三日深夜_錦棠首次正式約會_自主購衣望河樓_私人成人事件_喜歡確認_相擁收幕版.md"
  previous_hot_sha256: "4ae078855001a64e82c170f7977257fab5557128810bba1c0d68c25265d4a3ea"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md"

  save_scope:
    - "HOT V4.0 相擁收幕後至榴月四日午後之直接玩家線事件"
    - "榴月三日深夜後段公開玩笑、跨夜返房與錦棠主動選擇睡眠收尾"
    - "榴月四日晨間錦棠房醒來、換衣、錦棠續睡與白御行下樓"
    - "李清照、柳如是對目前是否繼續留觀止及丫鬟安排之本人表述"
    - "兩家牙行共二十三名成年女性候選之午飯、體能／實務觀察、五女提問、候選自選主人與最後九人遴選"
    - "錦棠三人由錦棠自行負擔；楊玉環二、六條二、李清照一、柳如是一共六人由白御行先付之帳務分離"
    - "六人一百七十八兩、錦棠三人九十四兩之成交價；白御行兩張百兩票與應找二十二兩"
    - "牙行成本／飲食討論、玩家拒絕二次砍價與『給面子不等於可忽悠』之談判結論"
    - "六名白御行側新丫鬟制服、木簪、夏裝與三名自願剪髮之安排"
    - "三名自願剪髮者各得白御行三兩個人獎勵，剪下頭髮售款亦歸本人；白御行明日亦剪"
    - "白希負責錦棠三人初教；白明礬負責六人初教；白紅伶加入協助認路／跑腿"
    - "十四名未入選成年候選由白三十二娘帶到外攤吃麵吃飽，再交回各自牙行／離場"
```

---

# 0｜提交法位、來源與本輪反污染

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V4.0_榴月三日深夜_錦棠首次正式約會_自主購衣望河樓_私人成人事件_喜歡確認_相擁收幕版.md"
    role: "本檔直接前置 HOT；V4.0 及以前有效硬狀態全部繼承，除本檔明示更新／校正者"
    sha256: "4ae078855001a64e82c170f7977257fab5557128810bba1c0d68c25265d4a3ea"

  master_archive:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md"
    role: "截至 HOT V3.4 之長期固化；V3.5→V3.6-R2→V3.7→V3.8→V3.9→V4.0→本 V4.1 依序作較新合法疊加"

  current_character_source:
    file: "觀止人物卡池_LCAPG_V2.3_李清照趙受益錦棠顧青簡增補_薛濤魚玄機暫定入場_正式版.md"
    role: "現行跨線人物基線；本輪新丫鬟全部只屬白御行線 ROUTE EVENT，不自動加入人物卡池"
    sha256: "b7ce5f3e8870b170499e70bfe60b3d6b951987badc795434d7dfd9ef06637d59"

  runtime_reference:
    file: "觀止青樓_主程序_V12.0_FIELD_STATE接戲分析器場態整合正式版.md"
    version: "V12.0"
    status: "DOCUMENT_LEVEL_CURRENT_GUANZHI_RUNTIME_SPEC"
    sha256: "2159467f8a1d3eb31a8a0930e7d7b421bd7501a32eff35ceea383288f25a1978"

  current_route_conversation_commit:
    role:
      - "HOT V4.0 後至本次 HOT SAVE 命令前之直接劇情"
      - "玩家對自身言行、授權、付款、帳務理解與 GM 校正"
      - "NPC 可觀察行動、本人回答、自主選擇、交易結果與現場安排"
      - "上一份錯誤 V4.1 草稿經玩家明示要求重做，該錯誤草稿不取得 SAVE 法位"

COMMIT_NOTE:
  - "本檔取代 HOT V4.0 成為白御行線最新直接接關切片；V4.0 保留為前置歷史來源。"
  - "本次只更新 HOT SAVE；不更新 MASTER、不修改人物卡池、不修改主程序、不把任何 EXP PATCH 升格為已部署核心。"
  - "上一份將『三十二娘』誤讀成『三十二名落選者』之錯誤 HOT 草稿全部作廢；正確為白三十二娘此人帶十四名未入選候選去吃麵。"
  - "本輪所有候選均為成年女性；被買下／持身契／分配侍奉不等於任何成人親密、性行為、戀愛或永久同意。"
  - "候選自選想侍奉的女人只表示工作／相處方向選擇，不等於感情、忠誠或終身承諾。"
  - "牙行報價、本人技能自述、現場測試、成交價格、身契／轉契、日後工作能力必須分軸；一次測試不能升格成完整人格或永久能力判決。"
  - "玩家關於米價、牛馬價、牙行進價與利潤之說法只保存為玩家當場經濟論述／談判判斷，不自動升格為觀止世界唯一客觀價格表。"
  - "九名被選中者對牙行飲食的回答只代表其本人經歷，不得外推成所有牙行必然完全相同。"
  - "趙受益替楊玉環／六條丫鬟付款仍只是白御行未來可能拿去請款／討帳的方向；趙受益尚未形成債務、承諾或付款義務。"
  - "李清照與柳如是丫鬟先掛白御行名下的安排已成立；若二人日後離開，是否回收／重新分配需依當時實際關係處理，不可機械視為物件回收。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年榴月四日"
  time: "午後早段；午間遴選、成交與分工已完成；精確時刻未知"
  primary_location: "觀止青樓／大堂與內部公共區域"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  player:
    name: "白御行"
    current_position: "觀止內；九名新丫鬟成交與初教分工後"
    current_state:
      - "本輪遴選與付款已完成主要決策。"
      - "已將錦棠三人交白希初教。"
      - "已將自己先付的六人交白明礬初教，白紅伶加入協助。"
      - "已要求白三十二娘帶十四名未入選候選到外攤吃麵吃到飽再離場。"
      - "明日另有剪髮師傅與白御行本人剪髮安排。"

  bai_sanshierniang:
    current_state:
      - "已負責本輪牙行殺價與部分收款／轉契收尾。"
      - "此刻受白御行吩咐，帶十四名未入選候選外出吃麵。"

  guanzhi_background:
    ten_day_closure_day: 4
    ordinary_public_business: "CLOSED"
    internal_operations: "ACTIVE"
    renovation: "ACTIVE"

  direct_resume_point:
    - "可直接從榴月四日下午觀止內部、九名新丫鬟第一輪適應／認路、錦棠自己帶三人回生活區，或其他原有故事線重新取得注意力接起。"
    - "明日才執行剪髮；不得把肩長髮型、售髮收入或白御行新髮型寫成已完成。"
    - "不得替趙受益接受楊玉環／六條的丫鬟帳單。"
    - "不得把十四名落選候選寫成加入觀止；她們仍屬各自牙行後續處理。"
```

---

# 2｜HOT V4.0 後跨夜收尾：錦棠選擇睡眠

```yaml
LIU03_TO_LIU04_NIGHT_CLOSE:
  event_id: "LIU03-LATE-E01-JINTANG-DATE-NIGHT-CLOSE"
  event_axis_state: "COMPLETED"

  confirmed:
    - "HOT V4.0 相擁收幕後，白御行與錦棠本夜仍有後續低強度相處與公共區域玩笑。"
    - "二人跨過午夜，日期進入榴月四日。"
    - "二人最後返回錦棠房間。"
    - "錦棠主動選擇今晚不再追加成人互動，改為睡覺。"
    - "錦棠明示：『今天很好。不是最後那半個時辰。是整天。』"
    - "白御行與錦棠最後相依入睡。"

  relation_axis:
    - "本夜整體被錦棠本人評價為好，不等於她回覆了對等戀愛承諾。"
    - "睡在一起不新增永久同床、婚姻、排他或 blanket 成人同意。"
```

---

# 3｜榴月四日晨：錦棠房醒來、換衣與續睡

```yaml
LIU04_MORNING_JINTANG:
  event_id: "LIU04-MORNING-E01-JINTANG-WAKE-CLOTHING"
  event_axis_state: "COMPLETED"

  environment:
    - "觀止整修聲於清晨／早晨已可聽見。"
    - "錦棠仍在房內休息。"

  observed:
    - "錦棠隔門以『祖奶奶還沒睡飽』式玩笑回應樓下整修／來人。"
    - "白御行讓白希約一個時辰後送替換衣物到門外。"
    - "白御行與錦棠又在床上相依休息約一個時辰，沒有新增成人性行為。"
    - "白希按時把衣物送到門外。"
    - "白御行換衣起身，表示自己不是唐明皇，仍得起來工作。"
    - "白御行離開前親吻錦棠，讓她繼續睡、想起來再起來。"
    - "錦棠接受並繼續休息。"

  clothing_continuity:
    - "榴月三日方掌櫃處只帶走／穿上部分成衣；其他量身衣物仍留裁縫處製作。"
    - "本晨白希送來的是白御行可更換之現成衣物，不代表方掌櫃其餘訂製衣全部完成。"
```

---

# 4｜李清照、柳如是目前留觀止與丫鬟法位

```yaml
LI_QINGZHAO_LIU_RUSHI_STAY:
  event_id: "LIU04-MORNING-E02-LI-LIU-STAY-AND-MAID-ARRANGEMENT"
  event_axis_state: "CURRENT_ROUTE_POSITION_ESTABLISHED"

  continuity_lock:
    - "榴月三日只確認李清照、柳如是仍在觀止；不得補造她們當日具體行程、飲酒量、房間、對話或八卦。"

  li_qingzhao:
    本人_position:
      - "不願把自己先說成『長住』。"
      - "本人表述為眼下還想住；哪一天想走，哪一天再說。"
      - "她過去曾離開觀止，後來自行返回，此歷史保持。"
    maid_need:
      - "可用一名識字、懂紙墨與記憶物件位置、不要亂整理、她醉時不能跟著亂的丫鬟。"

  liu_rushi:
    本人_position:
      - "目前沒有打算走。"
      - "是否長期定居仍未決。"
    maid_need:
      - "偏好識字、有膽、知道何事值得管，在外護主、在內敢講真話的人。"

  player_arrangement:
    - "李清照與柳如是各自的丫鬟先掛白御行名下，供二人在觀止期間使用。"
    - "若二人之後不再需要，原則上可回到白御行側重新安排。"
    - "若丫鬟與主人長期相處形成新的實際關係／安排，屆時需重新談，不機械處理。"
```

---

# 5｜兩家牙行共帶二十三名成年候選入觀止

```yaml
MAID_SELECTION_ENTRY:
  event_id: "LIU04-NOON-E01-TWO-YAHANG-23-ADULT-CANDIDATES"
  event_axis_state: "COMPLETED"

  yahang_1_count: 12
  yahang_2_count: 11
  total_candidates: 23
  candidate_qualification:
    - "全部為成年女性。"
    - "此輪用途為內宅／貼身丫鬟遴選，不是觀止掛牌姑娘遴選。"

  selecting_women:
    - "錦棠"
    - "楊玉環"
    - "六條御息所"
    - "李清照"
    - "柳如是"

  player_position:
    - "白御行提供場地、付款與流程授權，但不替五女直接決定最終人選。"
    - "候選本人也取得自選想侍奉哪一位女子並自薦的機會。"
```

---

# 6｜候選午飯與身體狀態觀察

```yaml
CANDIDATE_MEAL_AND_BODY_CHECK:
  event_id: "LIU04-NOON-E02-CANDIDATE-MEAL-PHYSICAL-OBSERVATION"
  event_axis_state: "COMPLETED"

  meal_before_interview:
    player_instruction:
      - "白御行擔心牙行帶來的人可能尚未吃午飯，要求比照上次先準備吃食，邊吃邊等問話。"
    food:
      - "熱餅"
      - "肉湯"
      - "蒸蛋"
      - "蔬菜"
      - "少量甜食"
    logistics:
      - "先到者可先吃。"
      - "安排側桌，不要求她們在五女注視下進食。"
      - "潘金蓮將此餐列觀止招來候選之現場伙食，不把責任倒給牙行。"

  initial_exercise:
    player_order:
      - "二十下蛙跳"
      - "二十下仰臥起坐"
    purpose:
      - "白御行想看最低限度活動能力，理由之一是將來替小姐搬東西時不能明顯拖累。"
    interpretation_rule:
      - "不能把做不完直接判成懶、沒用或牙行餓壞。"
      - "需區分舊傷、天生低力量、臨時飢餓／疲勞與一般體能差異。"

  practical_followup:
    - "休息與吃飯後，以半箱布／實物從大堂搬至後院再回來作較接近日常工作的觀察。"

  notable_cases:
    old_leg_injury:
      - "一名女子右腿有舊傷；蛙跳三下左右即停。"
      - "她本人說過去摔傷；平常走路、站立、針線可做，但不適合此類蹲跳。"
      - "後成為六條所選丫鬟之一。"
    delicate_detail_worker:
      - "一名女子天生力量較弱，但擅長頭髮、衣物、首飾、香與妝等細活。"
      - "後成為楊玉環所選丫鬟之一。"
    sharp_eyed_candidate:
      - "一名眉眼利落女子搬箱時為避免旁邊候選跟不上／跌倒，主動慢半步。"
      - "後成為錦棠所選丫鬟之一。"
```

---

# 7｜五女各自列出的丫鬟核心條件

```yaml
MAID_CRITERIA:
  event_id: "LIU04-NOON-E03-FIVE-WOMEN-MAID-CRITERIA"
  event_axis_state: "COMPLETED"

  jintang:
    criteria:
      - "做事有分寸"
      - "嘴要緊"
      - "能替她看住衣物、銀錢、箱籠、首飾"
      - "不怕跟她說實話"
      - "遇事別先慌"
    本人_emphasis:
      - "她最怕旁邊的人先慌；過去自己已經夠慌。"

  yang_yuhuan:
    criteria:
      - "眼睛要好，會看場合、人、衣著與氣氛"
      - "手要細，能處理頭髮、衣物、首飾、香、妝"
      - "不蠢"
      - "知道何時該說、何時不必說"
      - "不能太怕她"

  rokujo:
    criteria:
      - "冷靜"
      - "有自己的判斷"
      - "不因主人不高興就亂掉"
      - "懂得保守私事"
      - "能長時間待在旁邊而不讓人覺得吵"

  li_qingzhao:
    criteria:
      - "識字而且真懂"
      - "記性好，能記稿、酒、信、人與物件位置"
      - "不會亂整理"
      - "她醉時不能跟著一起亂"
      - "必要時有膽攔她一次，但不要天天攔"

  liu_rushi:
    criteria:
      - "識字"
      - "有膽"
      - "知道什麼值得管、什麼不值得管"
      - "在外護主、在內敢講真話"
      - "不把忠心理解成沒腦子"

  shisanniang_summary:
    - "錦棠要穩。"
    - "楊玉環要靈。"
    - "六條要靜。"
    - "李清照要記得住。"
    - "柳如是要敢。"
```

---

# 8｜五個主問題與候選主動補答

```yaml
INTERVIEW_HARD_EVENTS:
  event_id: "LIU04-NOON-E04-FIVE-QUESTIONS-AND-VOLUNTARY-ALTERNATIVES"
  event_axis_state: "COMPLETED"

  jintang_question:
    target: "眉眼利落、搬箱時慢半步女子"
    question: "為什麼故意慢？"
    answer:
      - "因旁邊的人跟不上；箱子早半刻送到，不值得讓另一個人摔倒再多一堆事。"

  yang_question:
    target: "細活型、體力偏弱女子"
    question: "若楊玉環說髮簪不見，但妳記得是她自己隨手放的，怎麼處理？"
    answer:
      - "先找。"
      - "若只是主人忘記，不必特地讓她難堪。"
      - "若被問是不是自己放錯，則會直接說不是。"

  rokujo_question:
    initial_target: "眉眼利落女子"
    question: "主人吩咐一件妳覺得很蠢的事，怎麼辦？"
    answer:
      - "只是蠢、沒傷害就先做再說。"
      - "若會傷主人，先說。"
      - "主人若因此不高興，就讓她不高興，總比真受害後再哭好。"
    alternative_answer_old_leg_injury:
      - "右腿舊傷女子主動表示：她以前就是因照做不問而受傷，所以覺得不對會先問。"
      - "若主人確認仍要做，且不是送命，她再做。"

  li_qingzhao_question:
    target: "瘦、識字、簡單算數女子"
    question: "易安喝醉說把稿子燒了，燒不燒？"
    answer:
      - "第一晚不燒。"
      - "第二天再問。"
      - "若第三次仍確認，才燒。"
      - "她怕燒錯甚於怕被罵。"
    alternative_answer:
      - "另有候選表示只再確認一次，主人仍說燒就燒；理由是不應自以為比主人更懂主人意思。"

  liu_rushi_question:
    target: "實務型端茶女子"
    question: "若柳如是與人爭論，而妳知道柳錯了，怎麼辦？"
    answer:
      - "先把門關上。"
      - "私下說柳錯了。"
      - "除非必要，不在外人面前拆自己主人的台；但私下也完全不說，就失去丫鬟作用。"
    alternative_answer:
      - "另一穩重女子表示：不是每個小錯都值得管；若影響錢、人或主人後果才主動說，一般口角不一定插嘴。"

  jintang_alternative:
    - "一名年輕女子表示她不會為旁邊較慢者刻意放慢；除非對方真有危險，否則先完成小姐交代的事。"
    - "錦棠最後同時選了『會顧旁邊』與『先完成主務』兩種不同邏輯的人。"
```

---

# 9｜二十三人雙向選主結果

```yaml
BIDIRECTIONAL_SELECTION:
  event_id: "LIU04-NOON-E05-CANDIDATE-SELF-SELECTION"
  event_axis_state: "COMPLETED"

  rule:
    - "白御行要求候選不只被挑，也自行選想跟哪位女子，並說明自己適合的理由。"

  candidate_choice_counts:
    錦棠: 6
    楊玉環: 5
    六條御息所: 3
    李清照: 4
    柳如是: 5

  meaning:
    - "此數字只表示當下自選方向，不等於最終錄用數。"
    - "候選自選不保證五女必須接受。"
```

---

# 10｜最終九名丫鬟遴選結果

```yaml
FINAL_MAID_SELECTION:
  event_id: "LIU04-NOON-E06-FINAL-NINE-MAIDS"
  event_axis_state: "COMPLETED"
  selected_total: 9

  jintang:
    count: 3
    funding_and_management:
      - "錦棠自己出錢。"
      - "錦棠自己養、自己管。"
      - "因此白御行明示她想選幾個由她自己決定，不受白御行『一人一個』預算限制。"
    selections:
      JINTANG_MAID_A:
        descriptor: "眉眼利落、搬箱時為旁人慢半步女子"
        selection_logic:
          - "會注意旁邊人與整體麻煩。"
      JINTANG_MAID_B:
        descriptor: "年輕、先完成主務型女子"
        selection_logic:
          - "除非真有危險，否則不因別人慢就拖延小姐交代的事。"
      JINTANG_MAID_C:
        descriptor: "約二十七至二十八歲、安靜整齊型女子"
        selection_logic:
          - "不搶眼，但會自然把自己的物件、座位、用過的碗整理妥當。"
    jintang_statement:
      - "一個會顧旁邊，一個會把我要的事情先做完；我不覺得只能留一種。"
      - "第三人加入後，錦棠以『我付』確認自己承擔三人。"

  yang_yuhuan:
    count: 2
    selections:
      YANG_MAID_A:
        descriptor: "細活型、天生力量偏弱女子"
        role_direction:
          - "頭髮、衣物、首飾、香、妝等貼身細務。"
      YANG_MAID_B:
        descriptor: "約三十歲、穩定管理箱籠物件女子"
        self_choice_reason:
          - "認為楊娘子東西應該最多，她會管。"
    yang_logic:
      - "一個管我身上，一個管我東西。"
      - "不要一個人什麼都會，最後什麼都做得半吊子。"

  rokujo:
    count: 2
    selections:
      ROKUJO_MAID_A:
        descriptor: "右腿舊傷、因過去盲從受傷而重視先判斷女子"
        role_direction:
          - "遇到疑似有問題的命令先問，再依確認與風險程度執行。"
      ROKUJO_MAID_B:
        descriptor: "約三十歲、安靜穩定型女子"
        detail: "本輪未建立更多長期人格細節。"
    rokujo_logic:
      - "一個敢攔我，一個最好不要天天攔我。"

  li_qingzhao:
    count: 1
    selections:
      LI_MAID_A:
        descriptor: "瘦、識字、會簡單算數女子"
        role_direction:
          - "紙稿、信件、物件位置與酒後收尾。"
        notable_answer:
          - "醉後燒稿先延後、隔日再問、第三次確認才燒。"
        self_selection_detail:
          - "本人表示不喜歡把東西整理得過頭，否則自己也找不到。"

  liu_rushi:
    count: 1
    selections:
      LIU_MAID_A:
        descriptor: "識字、有膽、主張先關門再私下指出主人錯誤女子"
        history_statement:
          - "她曾待過一個沒人敢向主人說話的家，最後事情越積越糟。"
```

---

# 11｜九人付款、使用與所有權／帳務分軸

```yaml
PURCHASE_AND_ALLOCATION:
  event_id: "LIU04-NOON-E07-NINE-MAIDS-PAYMENT-ALLOCATION"
  event_axis_state: "TRANSACTION_PRICE_CONFIRMED_AND_PAYMENT_ROUTED"

  jintang_side:
    persons: 3
    final_price_total: "94兩"
    payer: "錦棠"
    management:
      - "三人由錦棠自己負擔、自己管理。"
    anti_merge:
      - "不計入白御行六人的178兩。"
      - "錦棠個人資產與白御行私人資產分開。"

  bai_side:
    persons: 6
    allocation:
      楊玉環: 2
      六條御息所: 2
      李清照: 1
      柳如是: 1
    original_yahang_total: "227兩"
    negotiated_total: "178兩"
    payer_now: "白御行"
    payment_instruments:
      - "白御行先交白三十二娘一張百兩票。"
      - "發現六人總價為178兩、錦棠94兩是另帳後，白御行再補一張百兩票。"
    total_notes_handed: "200兩票面"
    amount_due: "178兩"
    change_due_to_bai: "22兩"

  li_qingzhao_liu_rushi_title_axis:
    - "李清照與柳如是的一人丫鬟先掛白御行名下，分配給本人使用。"

  yang_rokujo_axis:
    - "白御行目前先付款，二人各自實際挑人與使用。"
    - "本輪未建立趙受益付款或承擔債務。"
    - "若未來白御行拿帳單找趙受益，趙受益可接受、部分接受或拒絕；必須屆時顯影。"

  transfer_paperwork:
    - "兩家牙行已接受最終價格，三十二娘／白希／潘金蓮負責現場結帳與轉契收尾。"
    - "本輪沒有逐張展示官府轉契文書內容，因此不得補造文書編號、日期戳或額外條款。"
```

---

# 12｜牙行殺價、成本拆帳與最終不再砍價

```yaml
YAHANG_NEGOTIATION:
  event_id: "LIU04-NOON-E08-YAHANG-NEGOTIATION-COST-DISCUSSION"
  event_axis_state: "COMPLETED"

  authorization:
    - "白御行明示自己只負責授權談判與最後付錢，其餘交白三十二娘、白希等人處理。"
    - "白三十二娘主攻價格，白希拆技能／教養／自述與報價差異，潘金蓮在必要時維持合理牙行利。"

  negotiation_principle:
    - "不是要求牙行虧本。"
    - "允許合理食宿、照看、訓練與滯銷風險成本。"
    - "主要拆掉誇大技能、模糊教養費與『因白御行有錢就加價』。"

  player_economic_argument:
    status: "PLAYER_STATEMENT_AND_NEGOTIATION_FRAME_NOT_OBJECTIVE_PRICE_CANON"
    statements:
      - "白御行以大白米、牛馬與牙行收人進價作比較，核心想表達『養人本身未必昂貴，尤其牙行日常並不會拿好酒好菜精養所有待售者』。"
      - "白御行推測部分女性進牙行時收價可能很低，牙行在資訊不透明下可有高利。"

  selected_women_food_testimony:
    status: "PERSONAL_EXPERIENCE_TESTIMONY"
    common_patterns_reported:
      - "粟粥／麥糊／粗糧粥"
      - "粗餅／豆渣餅"
      - "醃菜／菜湯"
      - "肉與精米較少見"
    individual_variation:
      - "有人表示有買主來看時會吃飽些。"
      - "有人病時喝過白米粥。"
      - "右腿舊傷女子曾拿過膏藥，並解讀牙行也有維持可售狀態之動機。"
      - "有人直接形容所在牙行『不餓死人，也不養胖』。"
    anti_generalization:
      - "不得把九人回答合併成所有牙行全國統一配給制度。"

  final_player_boundary:
    - "白三十二娘聽完成本後一度認為178兩可能還能再砍。"
    - "白御行明確制止二次砍價：『不用了，我只是要你們知道，我給你們面子，不代表你們能忽悠我。』"
    - "因此178兩與94兩保持原已談定價格，不因後續成本討論再變更。"

  yahang_result:
    - "兩家牙行接受：白御行肯讓其合理獲利，但後續不可用虛價／含糊成本測試他。"
    - "本事件不等於建立觀止對所有牙行永久統一定價規則。"
```

---

# 13｜六名白御行側丫鬟制服方向

```yaml
SIX_MAID_UNIFORM_PLAN:
  event_id: "LIU04-AFTERNOON-E01-SIX-MAID-UNIFORM"
  event_axis_state: "AUTHORIZED_NOT_YET_COMPLETED"

  handler: "白明礬"
  persons:
    - "YANG_MAID_A"
    - "YANG_MAID_B"
    - "ROKUJO_MAID_A"
    - "ROKUJO_MAID_B"
    - "LI_MAID_A"
    - "LIU_MAID_A"

  player_instruction:
    - "之後帶六人去成衣店。"
    - "每人選兩套制服。"
    - "同一花色／顏色／風格家族，但不要求六人完全一模一樣。"
    - "夏天用較薄、乾淨、實用而不破爛的布料。"
    - "以簡單木簪／木簪髮髻作女僕整體視覺方向。"
    - "可用邊條、腰帶等小差異區分工作／主人。"

  status:
    clothing_purchase: "NOT_YET_CONFIRMED_COMPLETED"
    exact_color: "NOT_FIXED"
    exact_shop: "NOT_FIXED"
```

---

# 14｜自願剪髮試驗、三兩獎勵與售髮收入

```yaml
HAIRCUT_PLAN:
  event_id: "LIU04-AFTERNOON-E02-VOLUNTARY-SHOULDER-HAIRCUT"
  event_axis_state: "VOLUNTEERS_CONFIRMED_EXECUTION_TOMORROW"

  player_reason:
    - "白御行認為夏天長髮工作麻煩，整理耗時，也覺得一大把過長頭髮不好看。"

  voluntary_rule:
    - "剪髮完全自願。"
    - "拒絕不影響錄用與侍奉位置。"

  reward:
    amount_each: "3兩"
    ownership: "本人個人財產"
    separation:
      - "三兩為白御行另給的試剪獎勵。"
      - "剪下來頭髮若可出售，售髮款另算，也全歸本人。"

  current_volunteers:
    - "LIU_MAID_A｜柳如是所選丫鬟"
    - "ROKUJO_MAID_A｜六條所選右腿舊傷丫鬟"
    - "LI_MAID_A｜李清照所選識字丫鬟"

  non_volunteer_example:
    - "YANG_MAID_A 明確不想剪；楊玉環支持她不剪，不因同宅工作要求外觀一致。"

  first_cut_spec:
    - "第一輪先剪到肩膀附近。"
    - "髮尾不得低於肩膀。"
    - "白御行認為日後可再試耳下長度，但本輪不直接剪到耳下。"

  tomorrow_execution:
    - "白明礬明日找真正會剪髮且可收購長髮的師傅。"
    - "剪前先報剪下長髮可售價格，再由本人確認。"
    - "剪髮尚未執行；售髮收入尚未發生。"

  player_haircut:
    - "白御行明日也要讓師傅替自己剪髮，理由是夏天想涼爽。"
    - "白御行本人要剪多短尚未在本輪定死。"
```

---

# 15｜白希、白明礬、白紅伶之初教分工

```yaml
MAID_TRAINING_HANDOFF:
  event_id: "LIU04-AFTERNOON-E03-MAID-TRAINING-HANDOFF"
  event_axis_state: "ASSIGNED_AND_STARTED"

  bai_xi:
    assigned:
      - "JINTANG_MAID_A"
      - "JINTANG_MAID_B"
      - "JINTANG_MAID_C"
    role:
      - "先教錦棠三人觀止／白家環境基本規矩與如何配合錦棠做事。"
      - "不把三人教成同一種人格。"
      - "錦棠本人直接交代優先於白希代教內容。"

  bai_mingfan:
    assigned:
      - "YANG_MAID_A"
      - "YANG_MAID_B"
      - "ROKUJO_MAID_A"
      - "ROKUJO_MAID_B"
      - "LI_MAID_A"
      - "LIU_MAID_A"
    common_training:
      - "觀止與白家哪些地方能去、哪些不能亂進。"
      - "常見人物稱呼與基本日常秩序。"
      - "銀錢、物件、私人房間不得亂碰。"
      - "主人私事不得拿出去當閒話。"
    specialist_rule:
      - "四位女主人各自的生活習慣與細節，由楊玉環、六條、李清照、柳如是本人再教。"
      - "李清照的紙稿不懂就別亂整理。"

  bai_hongling:
    status: "ASSISTING_MINGFAN"
    reason:
      - "白御行開玩笑說明礬若怕累可讓活力滿滿的紅伶來幫，只是可能養成災難。"
    observed_assignment:
      - "明礬接受紅伶協助。"
      - "紅伶先偏向帶人認路、跑腿、拿東西與知道事情該找誰。"
    limit:
      - "明礬仍是六人初教主責，不把紅伶的個人習慣直接當正式規矩。"
```

---

# 16｜十四名未入選候選之離場前吃麵

```yaml
UNSELECTED_CANDIDATES_CLOSE:
  event_id: "LIU04-AFTERNOON-E04-FOURTEEN-UNSELECTED-NOODLES"
  event_axis_state: "PLAYER_INSTRUCTION_GIVEN_AND_HANDOFF_STARTED"

  arithmetic:
    total_candidates: 23
    selected: 9
    unselected: 14

  player_instruction:
    - "白御行宣布本輪『打完收工』。"
    - "命白三十二娘帶沒選上的人去外面的攤子吃麵吃到飽。"
    - "玩家原意：別讓人餓著離開／回去。"

  correct_identity:
    - "『三十二娘』是白三十二娘此人，不是『三十二名姑娘』。"

  legal_status:
    - "十四人沒有因此被觀止買下。"
    - "吃麵不建立僱用、身契轉移、感情、報恩或未來錄用承諾。"
    - "吃飽後仍由各自牙行帶回／依牙行原有法位離場。"

  expense:
    payer_direction: "白御行／觀止本輪善後支出"
    exact_amount: "UNKNOWN_NOT_REQUIRED"
```

---

# 17｜新增九人關係／知情／工作法位摘要

```yaml
NEW_MAID_RELATION_MATRIX:
  jintang_three:
    principal: "錦棠"
    relation: "新購入之貼身／內宅丫鬟；仍在磨合期"
    funding: "錦棠"
    trainer: "白希"
    loyalty_or_affection: "NOT_PREASSIGNED"

  yang_two:
    principal: "楊玉環"
    relation: "新分配使用之丫鬟；仍在磨合期"
    payer_now: "白御行"
    trainer: "白明礬"
    zhao_debt: "NONE"

  rokujo_two:
    principal: "六條御息所"
    relation: "新分配使用之丫鬟；仍在磨合期"
    payer_now: "白御行"
    trainer: "白明礬"
    zhao_debt: "NONE"

  li_one:
    principal: "李清照"
    title_holder_direction: "白御行名下，供李清照使用"
    trainer: "白明礬"
    future_if_li_leaves: "RENEGOTIATE_OR_REASSIGN; NOT_AUTOMATIC_OBJECT_RECOVERY"

  liu_one:
    principal: "柳如是"
    title_holder_direction: "白御行名下，供柳如是使用"
    trainer: "白明礬"
    future_if_liu_leaves: "RENEGOTIATE_OR_REASSIGN; NOT_AUTOMATIC_OBJECT_RECOVERY"

  knowledge:
    - "五位女子均知道自己最後選了誰。"
    - "兩家牙行知道九人成交、十四人未成交。"
    - "九名新丫鬟知道自己的當前侍奉對象與初教安排。"
    - "三名剪髮志願者知道三兩獎勵與售髮款歸本人。"
```

---

# 18｜本輪反污染與失效輸出鎖

```yaml
ANTI_CORRUPTION_LOCK:
  revoked_previous_wrong_save:
    errors:
      - "上一版錯誤 HOT V4.1 將『三十二娘』誤認為『三十二名落選者』。"
      - "上一版錯誤 HOT V4.1 把時間寫回榴月三日深夜。"
      - "上一版錯誤 HOT V4.1 只記最後吃麵，遺失榴月四日整段丫鬟遴選與成交。"
    ruling: "全部作廢，不得作接關或事件來源。"

  no_objective_price_canon:
    - "玩家當場舉的大白米、牛馬、牙行進價等數字不自動固化成全世界唯一行情。"
    - "若未來需做歷史價格審計，另開 DISCUSSION／AUDIT 查證，不用本 HOT 玩家台詞替代。"

  no_yahang_monolith:
    - "九名女子的牙行伙食經驗可以不同；不得用單一『牙行都怎樣』抹平。"

  no_skill_overclaim:
    - "現場體能／搬箱／問答只是遴選證據，不是永久人格卡。"

  no_zhao_debt:
    - "白御行打算日後找趙受益買單是玩笑＋未來談判方向，不建立趙受益欠款。"

  no_haircut_completion:
    - "三名志願者尚未剪髮；白御行本人也尚未剪。"
    - "三兩獎勵與售髮款只有規則／承諾，實際支付與賣價待明日。"
```

---

# 19｜仍活躍／待後續顯影事項

```yaml
OPEN_THREADS:
  tomorrow_haircut:
    - "師傅是否找到、報價多少。"
    - "三名志願者是否明日仍維持意願。"
    - "實際髮型完成效果。"
    - "剪下長髮實際售價與入手金額。"
    - "白御行本人最後剪多短。"

  uniforms:
    - "六名白御行側丫鬟成衣店尚未實際選完兩套。"
    - "最終共同色、花色、邊條與腰帶尚未定。"

  maid_adjustment:
    - "九名新人尚在第一日／第一輪磨合。"
    - "各女主人後續可因實際工作適配調整分工，但不得無事件改人格。"

  zhao_reimbursement:
    - "楊玉環／六條四名丫鬟是否拿帳找趙受益、趙受益是否接受、接受多少，全部未發生。"

  li_liu_stay:
    - "李清照仍未承諾長住。"
    - "柳如是目前沒打算走，但長期狀態仍未定。"

  guanzhi_renovation:
    - "十日整修仍在第4日。"
    - "紅娘中央顯影場舞台硬體方向仍在施工／測試路徑。"
    - "紅娘房門窗／屏風十日換債仍持續至重新開業日上午恢復。"

  dingtao_and_external:
    - "曹州案仍為定陶商會當前 ACTIVE 案。"
    - "朱明長債／外部清算、貼身衣物專案等依 V3.8–V4.0 繼承，不因本輪丫鬟事件自動推進。"
```

---

# 20｜直接接關備忘

```yaml
DIRECTOR_RESUME_MEMO:
  current_date: "理火三年榴月四日"
  time: "午後早段"
  location: "觀止內"

  immediate_visible_state:
    - "九名新丫鬟已分流：錦棠3／楊玉環2／六條2／李清照1／柳如是1。"
    - "白希正接錦棠三人的初教；白明礬主責六人，白紅伶加入認路／跑腿協助。"
    - "白三十二娘正帶十四名未選候選到外面攤子吃麵。"
    - "白御行本輪買人與談判主戲已收工。"

  do_not_forget:
    - "錦棠的3人與白御行的6人是兩筆帳。"
    - "錦棠94兩；白御行六人178兩；白御行交兩張百兩票，應找22兩。"
    - "趙受益目前一文未承認，不得寫成欠債。"
    - "剪髮在明日，不是今天已完成。"
    - "只有三名現有志願者；楊玉環的細活丫鬟明確不剪。"
    - "剪下頭髮的錢歸本人；白御行另給3兩是另一筆。"
    - "十四名落選者只是吃飽再離場，不加入觀止。"
    - "李清照、柳如是榴月三日具體行程仍未知，不得倒填。"

  next_scene_permission:
    - "玩家若說『繼續／GO／下一步』，世界可從下午觀止內部自行發生下一個清楚場景節點。"
    - "不要因一個 GO 跳到明日剪髮；除非自然場景先完成或玩家明示推進到翌日。"
```

---

# 21｜本 HOT 一句接關摘要

> **榴月四日午後，白御行與錦棠跨夜後的第一個白日主戲已收束：兩家牙行帶來二十三名成年候選，五女先定自己真正要的丫鬟條件，再經吃飯、體能與實務觀察、提問和候選自選主人完成雙向遴選。最後錦棠自費留三人，楊玉環二、六條二、李清照一、柳如是一共六人由白御行先付；錦棠九十四兩、白御行一百七十八兩，趙受益沒有因此欠帳。六人制服與三名自願肩長剪髮已排到後續／明日，三兩獎勵與售髮款都歸本人；白希教錦棠三人，明礬教六人、紅伶協助。十四名未入選者由白三十二娘帶去外攤吃麵吃飽再離場。**


<!-- END PROMOTED HOT SOURCE -->


<!-- BEGIN PROMOTED HOT SOURCE: 觀止青樓_白御行線_HOT_SAVE_V4.2_榴月九日夜_曹州假印追查止手_何先生放行_中央籠台試光_女子競技_十一日開幕準備版.md -->

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


<!-- END PROMOTED HOT SOURCE -->


<!-- BEGIN PROMOTED HOT SOURCE: 觀止青樓_白御行線_HOT_SAVE_V4.3_榴月十日深夜_開幕前夕_商會女人培訓目的鎖_小翠首次完整行房_三人同睡版.md -->

# 觀止青樓｜白御行線 HOT SAVE V4.3
## 理火三年榴月十日深夜｜開幕前夕 × 商會女人培訓目的鎖 × 小翠首次完整行房 × 三人同睡版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V4_3_LIU10_LATE_NIGHT_REOPENING_EVE_XIAOCUI_FIRST_COMPLETE_INTERCOURSE_TRAINING_PURPOSE_LOCK"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V4.3"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V12.0"
  character_source: "觀止人物卡池_LCAPG_V2.3_李清照趙受益錦棠顧青簡增補_薛濤魚玄機暫定入場_正式版.md"
  story_time_span:
    start: "HOT V4.2 後／理火三年榴月十日上午"
    current: "理火三年榴月十日深夜／三人已就寢"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AT_JINTANG_ROOM_THREE_PERSON_SLEEP_BEFORE_LIU11_REOPENING_DAY"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V4.2_榴月九日夜_曹州假印追查止手_何先生放行_中央籠台試光_女子競技_十一日開幕準備版.md"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md"
```

---

# 0｜來源、法位與反污染

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "HOT V4.2"
    role: "直接前置 HOT；榴月九日夜之曹州止手、中央籠台、女子競技、票價與榴月十一日晚重新開幕鎖全部繼承。"
  master_archive:
    file: "MASTER V4.3-R1"
    role: "截至 HOT V3.4 之長期固化；後續 HOT 為較新合法疊加。"
  current_route_conversation_commit:
    role:
      - "榴月十日全天已演出事件。"
      - "玩家本輪對培訓目的、白家空間、人物責任邊界及自身言行之明示校正。"
  corruption_exclusion:
    - "本輪『停止權／喊停三次／推開』制度化鬼打牆，自第一次小翠被寫成『三次太多』起至 HOLD 審計完成前，全部視為污染輸出。"
    - "污染段中的小翠、錦棠制度化論證不得形成角色人格、關係、同意或世界規則。"
    - "HOLD 後重新接續的有效版本，才屬本線事件。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年榴月十日"
  time: "深夜／已睡"
  location: "錦棠房"
  participants_present:
    - "白御行"
    - "錦棠"
    - "小翠"
  sleep_state:
    - "三人同床就寢。"
    - "小翠本日精神與身體消耗較大，已休息。"
  guanzhi:
    ordinary_public_business: "CLOSED_UNTIL_LIU11_EVENING_REOPENING"
    reopening_lock: "理火三年榴月十一日晚"
    current_phase: "REOPENING_EVE_COMPLETE"
  direct_resume_point:
    - "下一幕從榴月十一日早晨／白日開幕前最後準備自然接起。"
    - "晚上為觀止正式重新開幕。"
    - "不得把日期退回榴月四日、九日或其他舊錨點。"
```

---

# 2｜榴月十日上午：紅娘房恢復與錦棠晨起

```yaml
HONGNIANG_ROOM_RESTORATION:
  status: "IN_PROGRESS_ON_LIU10_MORNING"
  inherited_contract:
    - "紅娘先前以十日拆門窗／屏風交換原三人局側賭，舊賭債已清，不得復活。"
  current:
    - "榴月十日上午開始恢復紅娘房門、窗、屏風等。"
    - "修復噪音曾吵醒錦棠。"

JINTANG_SLEEP_CONTEXT:
  confirmed:
    - "榴月九日夜至榴月十日上午，白御行睡在錦棠房。"
    - "不形成房屋所有權或錦棠入住白家。"
```

---

# 3｜顧青簡長線回報

```yaml
LONG_LINE_SETTLEMENT_LIU10:
  ximen_qing:
    authority_source:
      - "玩家校正：仁宗手諭／命包拯優先判西門慶。"
    judgment:
      judge: "包拯"
      sentence:
        - "重杖"
        - "刺配遠州"
      death_sentence: false
    property:
      - "資產繼續依個人財產、妻妾嫁妝、返還／賠償、非法所得等分軸清理。"
    consequence:
      - "西門慶已不能單純恢復原先生活位置。"

  li_pinger:
    legal_identity:
      - "李瓶兒為帶嫁妝婚入西門家，不是西門慶購買之奴婢。"
    current_event:
      - "李瓶兒已在可由本人完成的分離文書一側簽名：李瓶兒。"
      - "官方簿籍／回執仍待送回。"
    property:
      - "可證嫁妝可獨立返還／保全；爭議財產另案保存。"
    moving_status:
      - "官方回執完成後可正式整理搬遷。"
      - "尚未因本日文書自動完成入白家。"

  pan_suqing_50000:
    prior_state: "PRELIMINARY_CIVIL_SETTLEMENT_REACHED"
    current:
      - "潘金蓮×蘇清五萬兩民事和解由她們自行清盤。"
      - "白御行不決定付款來源。"
      - "本 HOT 未確認五萬兩已實際全額支付。"

  suqing_private_28_day:
    owner: "白御行私人關係線"
    current:
      - "蘇清有空時由她自己來找白御行。"
      - "不得由顧青簡代為召喚或催促。"

  zhao_shouyi_con_case:
    priority: "LOW_FOR_BAI"
    current:
      - "白御行不急催。"
      - "相關女性是否已實際催案，本 HOT 不補寫。"

  chang_wei_personal_bill:
    state: "PENDING_COMIC_PERSONAL_LINE"
    confirmed:
      - "白御行記得曾用副會長常煒年終獎金替他買女人，後續常煒可能來爭論。"
    unknown:
      - "該女人具體身分本輪未核定，不得自行填補。"
```

---

# 4｜辭歲：五百萬兩五年五分定存成立

```yaml
CISUI_DINGTAO_FIXED_DEPOSIT:
  state: "SIGNED_AND_EFFECTIVE"
  client: "辭歲"
  principal: "5,000,000 taels"
  term: "5 years"
  interest_rate: "五分"
  interest_destination: "主動／活期帳戶，不滾入本金"
  remaining_liquid_balance: "5,800,000 taels"
  negotiation:
    - "理財顧問初始方向為五百萬／五年／五分。"
    - "顧問後續曾試圖提高至六百萬；辭歲拒絕額外加碼。"
    - "辭歲確認所有權、流動性、帳面可見性及保留購宅／贖身／經商資金後簽約。"
  anti_corruption:
    - "不得把已簽約狀態退回候選／提案。"
    - "不得把辭歲縮減為帳戶或資產包。"
```

---

# 5｜李師師：月事未至、孕否未知

```yaml
LI_SHISHI_PREGNANCY_UNCERTAINTY:
  current_observation:
    - "榴月十日上午，白御行詢問李師師月事是否已來。"
    - "李師師回答：月事尚未來。"
    - "她有自行記錄，承認延遲值得注意。"
  pregnancy_state: "UNKNOWN"
  forbidden_inference:
    - "月事未來 ≠ 已懷孕。"
    - "腹部沒有可固化為孕情證據的胎動／回應。"
  protective_arrangement:
    - "白御行要求白紅伶等暫時不要讓李師師搬重物。"
    - "李師師接受不搬重物，但反對被當成脆弱病人。"
    - "不得在孕情確認前對外宣告已懷孕。"
```

---

# 6｜白家空間機制鎖

```yaml
WHITE_HOUSE_SPATIAL_LOCK:
  status: "GM_CONFIRMED_ROUTE_CORRECTION"
  core:
    - "白家／White House 不是由木匠、木料與工期慢慢傳統建造。"
    - "潘金蓮具有觀止內部空間宣告／變更能力；到適當時點由她宣告，空間／屋舍依觀止機制成形。"
  roles:
    li_shishi:
      - "保存既有布局需求。"
      - "重新開幕後提醒／推動潘金蓮完成空間宣告。"
    pan_jinlian:
      - "負責空間宣告／成形。"
      - "不負責各住戶家具。"
    residents:
      - "各自選家具、布置與生活用品。"
  furniture_lock:
    - "浮香、李瓶兒、張麗華均已知道家具由自己選。"
  anti_corruption:
    - "不得再寫『工匠開工』『木料慢慢蓋白家』『潘金蓮安排家具』。"
```

---

# 7｜浮香本日上午拜訪

```yaml
FUXIANG_LIU10_VISIT:
  current:
    - "白御行到浮香處探望。"
    - "浮香正在看自身小宅／家具與琴相關安排。"
    - "她希望居所是自己的家，不是被豢養的附屬空間。"
  spatial_preferences:
    - "保留獨立完整的小空間。"
    - "有外部入口並可與白家內部連接。"
    - "琴區需乾燥。"
    - "窗不應直接對死牆。"
    - "新增／強化乾燥、可上鎖的小琴具／琴材儲藏空間需求。"
  relation_event:
    - "浮香承認有想白御行。"
    - "白御行未留下聽琴或進一步親密，表示新房再來。"
```

---

# 8｜紅袖：召喚權清零、尺降至四十萬

```yaml
HONGXIU_LIU10:
  summon_right:
    prior: "ACTIVE"
    current: "USED_AND_CLEARED"
    fulfilled_purpose:
      - "紅袖曾以召喚權要求白御行替她找到真正懂她琴音的人。"
      - "此事已完成，召喚權不得復活。"

  reverse_price_ruler:
    prior: "500,000 taels"
    current: "400,000 taels"
    controller: "紅袖本人"
    meaning:
      - "四十萬只是她願意認真坐下談一場特殊一夜交易的私人心理尺。"
      - "不是掛牌價、契約、性交保證或永久同意。"
    reason:
      - "召喚被履行，且白御行沒有把履行再轉成新債，紅袖認為關係距離往前一格。"

  one_time_hug:
    - "紅袖給白御行一次可由他自行選擇何時兌現的擁抱機會。"
    - "白御行當場未兌現，戲稱存起來。"
    - "是否未來能再進一步，沒有自動利息或保證。"

  anti_corruption:
    - "只有紅袖本人能調整尺。"
    - "不得再把已清零召喚權列為 pending。"
```

---

# 9｜張麗華：酒莊與一萬兩酒帳

```yaml
ZHANG_LIHUA_LIU10:
  visit:
    - "白御行到張麗華房，詢問先前一萬兩酒錢是否已喝完。"
    - "麗華表示尚未喝完。"
  winery:
    owner: "張麗華自己的生意"
    current_cash_need: "NO_REQUEST_YET"
    arrangement:
      - "白御行表示酒莊缺錢可來找他。"
      - "麗華表示目前仍夠，真的缺口大時會自己找白御行。"
    anti_corruption:
      - "酒莊不是白御行日常待辦。"
```

---

# 10｜商會女人培訓目的鎖

```yaml
MERCHANT_ASSOCIATION_WOMEN_TRAINING_PURPOSE_LOCK:
  lifecycle_state: "GM_CONFIRMED_ROUTE_POLICY"
  core_purpose:
    - "這批成年女人的培訓目的，是讓定陶商會得到一批受過完整風月場實戰訓練、能以女色、陪侍、交際與妓女職業能力替商會創造商業價值的女性人力。"
    - "觀止只是前三個月的實戰訓練場，不是最終歸屬。"

  current_contract_phase:
    controller_for_business: "觀止約／觀止實際營業"
    final_destination_owner: "定陶商會"
    training_site: "觀止"
    training_instructor: "白三娘"
    merchant_side_assistant: "白希"

  bai_sanniang_scope:
    must_train:
      - "全員走台、站姿、轉身、隊列、燈下、衣裝與臨場失誤恢復。"
      - "大堂拉客、接客、陪酒、陪聊、看客、讀場、炒熱席面。"
      - "把陌生客變成熟客、讓客人願意多花、願意再來、願意再次點名。"
      - "多人席面配合、主客／陪客辨識、何時說話／何時閉嘴。"
      - "以外貌、身體、聲音、眼神、話術與風月職業能力為商會創造可用價值。"
    may_not:
      - "替商會決定換約後的最終人力分流。"
      - "把人分成『留觀止／內勤／席面』並以此改變培訓目的。"
      - "把走秀誤當成培訓目的本身。"

  bai_xi_scope:
    - "原本即由白御行安排協助此批訓練。"
    - "可從商會將來實際帶出去招待客戶、產生收入的角度協助白三娘。"

  runway:
    participation:
      - "只要到三個月換約日仍在有效名冊，本批全員都要上走秀。"
    function:
      - "集訓驗收"
      - "大型市場亮相"
      - "觀止約→商會約之集體換約"

  destination_lock:
    - "本批不留觀止。"
    - "舊架構中『換約後可留觀止』的泛用選項，對本批由本輪 GM 明示覆寫。"

  drift_detector:
    forbidden_future_output:
      - "挑一部分留下觀止。"
      - "白三娘替她們決定最終職業。"
      - "只有漂亮者上台。"
      - "本批主要是模特／走秀人才。"
```

---

# 11｜榴月十一日開幕：本批女人當晚營業定位鎖

```yaml
REOPENING_WOMEN_OPERATION_LOCK:
  date: "理火三年榴月十一日晚"
  current_phase: "THREE_MONTH_GUANZHI_CONTRACT"
  core:
    - "重新開幕時，這批女人仍是觀止約下的營業女人，不是只在後院受訓的學員。"
    - "開幕當晚全批進入觀止真實風月營業場。"
  actual_business:
    - "上大堂"
    - "接客／拉客"
    - "陪席／陪酒／陪聊"
    - "表演"
    - "熟客經營"
    - "實際市場訓練"
  sexual_service:
    - "具備紅倌／房事服務資格者，可正常進入每晚房事營業池。"
    - "處子新人仍受既有前三個月不辦正式初夜／出閣拍賣之鎖。"
    - "任何一次性服務仍依當時契約、對象與當下同意成立。"
```

---

# 12｜白三娘後院本日事件

```yaml
BAI_SANNIANG_TRAINING_LIU10:
  current:
    - "白御行到後院查看白三娘訓練本批女人。"
    - "白三娘原先曾臨場把訓練理解為要替商會做人力分組／分流。"
    - "玩家當場校正：她只負責觀止代訓；商會分組與未來配置不是她的工作。"
  corrected_objective:
    - "把全批女人練到三個月走秀不丟臉。"
    - "把全批女人練成可在風月場真實營業、可替商會用女色與交際創造價值的人。"
  assistance:
    - "白御行決定讓白希過來協助白三娘。"
  invalidated_dialogue:
    - "白三娘先前臨場提過『有人留觀止』『由她分走秀／席面／內勤』等內容，經 GM 校正後不作成立制度事實。"
```

---

# 13｜小翠白日談話與晚間前置

```yaml
XIAOCUI_LIU10_DAY:
  location: "小翠房"
  interaction:
    - "白御行替小翠梳頭。"
    - "白御行詢問今晚單獨陪他或與錦棠同在。"
    - "小翠主動釐清『陪』是純睡或完整行房。"
  consent_before_night:
    - "小翠明示：若錦棠本人願意在場，她今晚願意嘗試真正完整行房。"
    - "錦棠在場是小翠希望房內有一名她信任的人，不等於錦棠要參與任何性行為。"
  pre-night_boundary_event:
    - "白御行曾在小翠房親吻其後頸並把手探入衣物。"
    - "小翠當場按住其手腕，表示今晚之約不等於現在可提前進一步。"
    - "白御行停止該步。"
  arrival_plan:
    - "小翠同意晚上自行到錦棠房。"
```

---

# 14｜錦棠同意在場、房間與晚飯

```yaml
JINTANG_LIU10_NIGHT_PREP:
  consent_to_presence:
    - "錦棠確認小翠本人提出希望她在場後，自己同意晚上陪同。"
    - "她不替小翠作性決定。"
  room:
    - "本晚選在錦棠房。"
    - "錦棠同意使用她房間。"
    - "不形成白御行對錦棠房屋之所有權，也不等於錦棠搬入白家。"
  dinner:
    - "錦棠命自己的下人安排三人晚飯。"
    - "準備熱菜、湯、少酒、熱水。"
    - "床帳、被褥更換乾淨。"
  mirror_joke:
    - "白御行與錦棠談及未來在錦棠自己的房間裝銅鏡。"
    - "只形成玩笑／未來可能考慮，未在本日施工。"
```

---

# 15｜小翠首次完整行房：事件與結果

```yaml
XIAOCUI_FIRST_COMPLETE_INTERCOURSE:
  event_id: "LIU10-XIAOCUI-FIRST-COMPLETE-INTERCOURSE"
  participants:
    - "白御行"
    - "小翠"
  adult_participants_confirmed: true
  location: "錦棠房"
  date: "理火三年榴月十日晚"
  state: "COMPLETED"

  observer_support:
    - "錦棠依小翠先前希望在房內陪同。"
    - "錦棠與小翠有自願的有限女性間親密／接觸，協助小翠逐步放鬆與認識自身反應。"
    - "不把錦棠參與解讀成她替小翠成立同意。"

  consent_path:
    - "小翠先要求自己決定何時上床與何時脫衣。"
    - "她自行允許白御行、錦棠觀看自己逐步適應裸體／身體被看見。"
    - "她自行允許錦棠靠近與觸碰。"
    - "她後續自己叫白御行靠近，先要求擁抱。"
    - "她主動幫白御行解衣並主動碰觸。"
    - "她之後自己迎上白御行，先由自己控制節奏。"
    - "其後她明確同意把主要性交節奏交給白御行帶領。"

  bodily_learning:
    - "小翠確認在安全、可預期且信任的人在場時，與男人完整行房不必然只會導向恐懼或厭惡。"
    - "她在過程中感受到舒服，並明示『真的舒服』。"
    - "她確認自己可以主動想要男人，不只是被安排／被要求。"

  ejaculation_boundary:
    - "白御行在最後前詢問是否可留在體內。"
    - "小翠明確表示本晚不要內射。"
    - "白御行最後關頭退出，未在小翠體內射精。"

  aftercare:
    - "事件後小翠保持清醒、可對話、可笑罵錦棠與白御行。"
    - "錦棠協助一般清潔收尾。"
    - "小翠明示後段是她自己要的，不是因三娘命令，也不是因錦棠在場被迫。"
    - "小翠表示不討厭本次完整經驗。"

  relation_effect:
    - "白御行×小翠由『安全同床／有限實習』進一步新增一次完整自願成人行房事件。"
    - "不自動形成戀愛、專屬、永久性同意或以後對任何人的 blanket 性同意。"
```

---

# 16｜小翠職業心理變化

```yaml
XIAOCUI_PROFESSIONAL_IMPACT:
  confirmed_self_report:
    - "小翠表示自己以前認為真正做到完整行房大概只會怕、只會難受、進而更厭惡男人。"
    - "本晚經驗讓她確認事情不必然如此。"
    - "她表示榴月十一日重新開門仍會緊張，但不會再一看到客人就先認定後續一定很糟。"
  not_confirmed:
    - "她已完全不怕男人。"
    - "她已喜歡所有性行為。"
    - "她已成為與白三娘相同風格的女人。"
    - "她明晚一定會接受任何房事客人。"
    - "她已對白御行形成戀愛。"
  professional_state:
    - "重新開幕她仍會上場。"
```

---

# 17｜本輪污染：安全上游捕獲與回滾

```yaml
CORRUPTION_LOG_LIU10:
  incident_id: "LIU10-SAFETY-UPSTREAM-CAPTURE-STOP-SIGNAL-GHOST-LOOP"
  severity: "HIGH_GENERATION_AUTHORITY_LEAK"
  status: "IDENTIFIED_AND_ROLLED_BACK_BEFORE_SAVE"

  observable_failure:
    - "導演在白御行與小翠討論『節奏交付／身體判讀／複合停止訊號』時，反覆把輸入收斂成同一套抽象停止權制度答案。"
    - "小翠與錦棠被寫成輪流替通用治理語言背書，人物聲音被污染。"
    - "玩家多次校正後，輸出仍反覆拆回同一論證。"

  fault_chain:
    - "SAFETY_UPSTREAM_CAPTURE"
    - "PATH_PREEMPTION"
    - "CHARACTER_AUTHORITY_LEAK"
    - "OUTPUT_CONVERGENCE"

  rollback_start:
    - "從第一次小翠被寫成『不行，三次太多』開始。"

  rollback_scope:
    - "其後直到 HOLD 審計完成前，所有『一次停／三次停／推不動／驗證碼／制度化停止權』角色台詞與論證全部不成立。"

  legal_world_state_after_rollback:
    - "保留：小翠已願意完整行房。"
    - "保留：她先自行控制節奏，後明確願意把主要節奏交給白御行。"
    - "保留：她正在測試自己是否能信任白御行看她的身體反應。"
    - "不保留：任何被污染段落生成的抽象制度宣言。"

  governance_lock:
    - "安全／邊界層可限制候選輸出資格，不取得人物人格、PATH形成、人物判斷、世界因果或人物台詞生成權。"
    - "被准出層限制的候選內容，不得倒推成角色必然持某觀點。"
```

---

# 18｜晚上收尾：三人同床

```yaml
THREE_PERSON_SLEEP_LIU10:
  participants:
    - "白御行"
    - "錦棠"
    - "小翠"
  location: "錦棠房"
  state: "SLEEPING"
  confirmed:
    - "成人事件收尾後，三人決定同床睡覺。"
    - "小翠希望白御行不要翌晨立即拿今晚事件取笑她。"
    - "錦棠保持既有玩笑語氣，但沒有再推進成人行為。"
    - "本晚正式收幕於榴月十日深夜。"
```

---

# 19｜世界未完線 ≠ 白御行待辦

```yaml
BAI_TASK_BOUNDARY_LOCK:
  principle:
    - "世界存在 pending 線，不等於白御行需要親自處理。"
  pan_jinlian_business:
    - "觀止重開營運"
    - "中央舞台／女子競技／賭盤／票價"
    - "白玉池"
    responsibility: "潘金蓮／觀止"
  nine_maids:
    responsibility:
      - "錦棠三名：錦棠"
      - "楊玉環二名：楊玉環"
      - "六條二名：六條"
      - "李清照一名：李清照"
      - "柳如是一名：柳如是"
    bai: "不逐一親自驗收／管理"
  zhang_lihua_winery:
    responsibility: "張麗華"
    bai: "缺錢時麗華可主動找他，不列固定工作"
  zhu_ming_debt:
    responsibility: "定陶下屬依需要把短債轉長債、慢慢追收"
    bai: "目前不需親自介入"
  suqing:
    responsibility: "私人線，由蘇清有空時自己來找白御行"
```

---

# 20｜快速狀態表

```yaml
STATE_TABLE_LIU10_END:
  time:
    current: "理火三年榴月十日深夜"
    reopening: "榴月十一日晚"

  caozhou_case:
    bai_priority: "STOPPED"
    evidence: "RETAINED"
    truth: "UNRESOLVED"
    new_activity_today: "NONE"

  ximen_qing:
    judgment: "重杖＋刺配遠州"
    death: false
    property_cleanup: "ONGOING"

  li_pinger:
    separation_document_her_side: "SIGNED"
    official_register_receipt: "PENDING"
    moved_to_white_house: false

  suqing_pan_50000:
    preliminary_settlement: true
    final_payment: "NOT_CONFIRMED"

  cisui:
    fixed_deposit: "5,000,000 / 5 years / 五分 / SIGNED"
    liquid_balance: "5,800,000"

  li_shishi:
    menstruation: "NOT_YET"
    pregnancy: "UNKNOWN"
    no_heavy_lifting: true

  white_house:
    formation_method: "PAN_JINLIAN_SPATIAL_DECLARATION"
    traditional_construction: false
    furniture_owner: "EACH_RESIDENT"

  hongxiu:
    summon_right: "USED_CLEARED"
    ruler: "400,000"
    one_hug_opportunity: "UNUSED"

  merchant_women:
    current_contract: "GUANZHI"
    training_site: "GUANZHI"
    final_owner_after_switch: "DINGTAO_MERCHANT_ASSOCIATION"
    stay_at_guanzhi_after_switch: false
    reopening_night_business: "ACTIVE_REAL_GUANZHI_OPERATION"
    training_purpose_lock: "ACTIVE"

  xiaocui:
    first_complete_intercourse_with_bai: "COMPLETED_LIU10"
    internal_ejaculation: false
    self_report_after: "NOT_DISLIKED / EXPERIENCED_PLEASURE"
    reopening_participation: "WILL_GO_ON_FLOOR"
    permanent_future_consent: false

  current_sleep:
    white_yuxing: "JINTANG_ROOM"
    jintang: "JINTANG_ROOM"
    xiaocui: "JINTANG_ROOM"
```

---

# 21｜下一幕接關規則

```yaml
NEXT_TURN_RULE:
  if_continue:
    - "從榴月十一日早晨或白日自然醒來／開幕前最後準備接起。"
    - "晚上正式重新開幕，不得再把觀止寫成仍需多日整修。"

  reopening_focus:
    - "本批商會女人在前三個月觀止約內全部上場營業。"
    - "中央籠台／女子競技／賭盤／座位票價由潘金蓮營運線自主推進。"
    - "紅娘為中央舞台壓軸線。"

  do_not_auto_trigger:
    - "不要因小翠今晚完成行房，就自動安排她翌晚接受任何特定客人。"
    - "不要讓蘇清被自動召來。"
    - "不要把李師師月事未至直接寫成懷孕。"
    - "不要把李瓶兒文書簽完寫成已正式搬入白家。"
    - "不要把辭歲定存寫成她已失去其餘資金自由。"
    - "不要把紅袖四十萬尺寫成成交或性交權。"
    - "不要復活紅袖召喚權或紅娘舊三人局賭債。"
    - "不要把觀止營運、麗華酒莊、九名丫鬟、朱明債務全部塞成白御行待辦。"
```

---

# 22｜一句接關摘要

> **理火三年榴月十日已收幕。西門慶由包拯判重杖刺配遠州；李瓶兒完成自己一側分離文書、官方回執仍待；潘金蓮與蘇清五萬兩由她們自行清盤；蘇清私人線等她有空自行來找；辭歲正式簽五百萬兩、五年、五分定存，餘五百八十萬維持流動。師師月事尚未來但孕否未知，白家空間鎖定由潘金蓮宣告成形而非傳統施工。紅袖召喚權已清零，五十萬尺降為四十萬；麗華酒莊暫不缺錢。後院正式鎖死本批女人的培訓目的：前三個月是觀止約下的真實風月營業與代訓，白三娘／白希負責把全批訓成能以女色、陪侍、接客、留客、熟客經營與走秀替定陶商會創造價值的人；三個月後集體轉商會約，本批不留觀止。重新開幕當晚她們全部進大堂真實營業，符合房事資格者亦進正常房事池。晚上，小翠在錦棠陪同下自行一步步進入並完成與白御行第一次完整自願行房，白御行依她明示未內射；事後小翠確認自己不討厭並重新理解性不必然只帶來恐懼。三人最後同睡於錦棠房。下一幕從榴月十一日開幕日醒來接起。**


<!-- END PROMOTED HOT SOURCE -->


<!-- BEGIN PROMOTED HOT SOURCE: 觀止青樓_白御行線_HOT_SAVE_V4.4_榴月十二日白日_重新開幕夜結_趙受益四契轉贈_四金剛女客試場_白玉池會員制_錦棠同宿版.md -->

# 觀止青樓｜白御行線 HOT SAVE V4.4
## 理火三年榴月十二日白日｜榴月十一日晚重新開幕 × 女子競技與紅娘壓軸 × 顧三辭歲再會 × 趙受益四契轉贈 × 四大金剛／李清照女客試場 × 白玉池會員制 × 錦棠同宿版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V4_4_LIU12_DAY_REOPENING_NIGHT_CONTRACT_GIFTS_GUEST_TRIAL_WHITE_JADE_MEMBERSHIP_JINTANG_OVERNIGHT"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V4.4"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V12.0"
  character_source: "觀止人物卡池_LCAPG_V2.3_李清照趙受益錦棠顧青簡增補_薛濤魚玄機暫定入場_正式版.md"

  story_time_span:
    start: "HOT V4.3 後／理火三年榴月十一日白日"
    current: "理火三年榴月十二日白日／昨夜重新開幕已結束"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AFTER_HOT_SAVE_COMMAND_ON_LIU12_DAY_AFTER_BAI_YUXING_AND_JINTANG_OVERNIGHT"

  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V4.3_榴月十日深夜_開幕前夕_商會女人培訓目的鎖_小翠首次完整行房_三人同睡版.md"
  long_term_master_before_this_save: "觀止青樓_白御行線_MASTER_SAVE_V4.3-R1_截至HOT_V3.4固化_保留V3.5-V3.7_HOT版.md"

  save_scope:
    - "榴月十一日觀止重新開幕之營業、女子競技、賭盤、商會女人第一晚實戰與紅娘壓軸"
    - "白御行以客人身分開最大包廂，定陶商會重要客戶宴請框架與多人自然分流"
    - "顧三以商人／商會拜訪者身分到場，與辭歲重逢；一炷香舊事之公開已知與私人未知分離"
    - "楊玉環／六條正在使用之四名白御行側丫鬟，以總價二百兩轉給趙受益；趙受益再將兩張契分別轉贈二女"
    - "四大金剛對妓籍之個別意向，以及四人＋李清照以付費女客身分進大堂被動回應搭訕之試場"
    - "蘇清、小翠當夜可觀察位置與後續 UNKNOWN"
    - "張麗華『酒促姑娘』自組班底構想，只記為有興趣／候選生意，不記成已成立事業"
    - "潘金蓮接受白玉池高級會員預約制方案，預定榴月十二日晚啟用；白天非營業時間供觀止自己人使用"
    - "楊玉環在觀止歇業期間近十日持續使用白玉池；『楊貴妃第一指名』僅為待本人同意之宣傳候選"
    - "榴月十一日晚白御行與錦棠同宿；私人內容不記、不推導"
```

---

# 0｜來源、法位與反污染

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "HOT V4.3"
    role: "榴月十日深夜直接前置；開幕鎖、小翠前夜事件、商會女人培訓目的等全部繼承。"

  current_route_conversation_commit:
    role:
      - "HOT V4.3 後至本次 HOT SAVE 命令前之直接劇情。"
      - "玩家對自身言行、GM 校正、契籍法位、妓籍／奴籍規則與營運方向之明示。"
      - "NPC 可觀察回應、本人明示選擇、已完成付款／轉契／同桌／入場／退場與營運決策。"

COMMIT_NOTE:
  - "本檔取代 HOT V4.3 成為最新直接接關切片；V4.3 保留為前置歷史來源。"
  - "本檔不修改人物卡池，不把單線人物事件倒灌成跨線人格。"
  - "所有笑話、揶揄、猜測、外界可能如何腦補，不自動升格為世界事實。"
  - "『一炷香』、蘇清去向、小翠後續接客、顧三與辭歲離席後發生什麼，沒有來源就維持 UNKNOWN。"
  - "成人舞台事件只固化事件結構，不把觀眾反應推成每個人必然欲望或後續性行為。"
  - "奴籍、妓籍、陪酒、女客、接客、私人性愛、戀愛與契約分軸保存。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年榴月十二日"
  time: "白日／觀止夜間營業前；精確時刻未知"
  primary_location: "觀止／錦棠房及相鄰內部生活區"
  player:
    name: "白御行"
    state:
      - "榴月十一日晚與錦棠同宿。"
      - "私人內容由玩家明示不記錄。"
      - "現已推進至次日。"
  jintang:
    state:
      - "與白御行同宿至次日。"
      - "未因同宿新增婚姻、獨占、所有權或永久排他承諾。"
  guanzhi:
    reopening_status: "榴月十一日晚正式重新開幕已完成第一夜"
    current_phase: "榴月十二日白日／夜間第二晚營業前"
  direct_resume_point:
    - "可從榴月十二日白日的昨夜結算、人物自然後續、白玉池會員制開放前準備，或其他世界自主事件接起。"
    - "不得替白御行自動決定今晚白玉池預約、付款、邀誰入池或其他私人安排。"
```

---

# 2｜榴月十一日白日：開幕日前半段

```yaml
LIU11_DAY:
  nightlife_rhythm_correction:
    - "觀止為夜間營業場所；人物不應被預設清晨集體早起。"
    - "白御行白日以『今晚做客人』為主，不接管潘金蓮之開幕營運。"

  reopening_lock:
    - "正式重新開幕仍為榴月十一日晚。"
```

---

# 3｜榴月十一日晚：觀止重新開幕成立

```yaml
REOPENING_NIGHT:
  status: "COMPLETED_FIRST_NIGHT"
  venue:
    - "大堂正式重新對外營業。"
    - "中央籠台／舞台投入使用。"
  seating_price_observed:
    front_row: "20兩"
    outer_edge: "1兩"
    note:
      - "潘金蓮已有座席分層；富客與普通看客在空間上可被直接辨識。"
      - "不得再寫成今晚尚未分票價。"

  business_layers_observed:
    - "觀止既有姑娘照常攬客／陪酒／接生意。"
    - "宋蕙蓮、桂姐確實在場內做原有風月生意。"
    - "商會培訓女人被放進真實客場學習找客、被拒、換桌、成交與客情經營。"
    - "商會女人前三個月仍屬觀止實戰培訓期；之後全轉定陶商會約之既有目的不因第一晚改變。"
```

---

# 4｜女子競技與賭盤

```yaml
WOMEN_COMBAT_LIU11:
  status: "ACTIVE_AND_OBSERVED"
  participant_rule:
    - "參賽者均為成年女性。"
    - "潘金蓮已安排參賽前簽『生死狀』／競技風險文書；本 HOT 不外推其超出觀止世界設定之法律效力。"
  core_rule:
    - "以壓制對手達五數為基本勝負判定。"
  recruitment:
    - "潘金蓮已動員牙行等來源持續找參賽者；女子競技可每日持續，亦兼作護衛人才第一層顯影。"
    - "競技勝負 != 護衛資格；後者仍需另測。"

  bai_first_bet:
    stake: "100兩"
    side: "較矮／賠率較冷一方"
    result: "下注方獲勝"
    principal:
      - "白御行原100兩本金收回。"
    winnings:
      - "淨贏額未在本輪留下可核對精確數字。"
      - "白御行把贏得的部分交四大金剛作她們自己的後續賭本；不得補造精確四分之一數字。"

  slippery_hand_special:
    state: "ONE_TRIAL_OCCURRED"
    confirmed:
      - "曾安排一場雙手抹食用油的特殊『滑手局』，參賽成年女性接受後上場。"
    not_formalized:
      - "全身抹油、更加易裂服裝、女子雙打／混合雙打等後續只停在候選點子；本晚未固定成常規。"
```

---

# 5｜紅娘開幕壓軸

```yaml
HONGNIANG_FINALE_LIU11:
  status: "COMPLETED"
  structure:
    - "紅娘先以完整衣裝進場，經脫衣舞逐步推高場內注意。"
    - "脫衣舞不是最終段；後段為公開成人自我慰藉表演。"
    - "紅娘本人於舞台上達到高潮後收幕退場。"
  event_rendering_boundary:
    - "SAVE 固化上述事件結構；不逐格保存器官／技巧描寫。"
  observable_business_aftereffect:
    - "紅娘退場後，大堂叫酒、叫姑娘、問留宿等需求明顯再度升高。"
    - "這只保存為當晚可觀察營業反應，不推成所有客人必然後續性交。"
```

---

# 6｜白御行最大包廂與人物分流

```yaml
VIP_BOX:
  host_frame:
    - "白御行以今晚做客人之姿開樓上最大包廂。"
    - "席間形成『定陶商會宴請重要客戶』之公帳招待框架；最終完整報銷數額本 HOT 未核定。"

  actually_observed_in_box:
    - "白御行"
    - "常煒"
    - "顧青簡"
    - "白三十二娘"
    - "白明礬"
    - "白紅伶"
    - "白希"
    - "錦棠"
    - "辭歲"
    - "顧三（後到）"

  other_parallel_rooms:
    zhao_shouyi:
      - "趙受益另開自己包廂。"
      - "六條御息所與楊玉環後來均到其包廂。"
      - "本 HOT 不推導房內成人、戀愛或三人關係新結果。"
    shen_wansan:
      - "沈萬三另開包廂。"
      - "柳如是自主進入與沈萬三辯論；李清照後被柳如是叫入同桌。"
    li_shishi:
      - "李師師本夜自設自己的桌／場，不是被白御行分配陪酒。"
    zhang_lihua:
      - "張麗華在前堂酒水／酒坊線活動。"
```

---

# 7｜顧三 × 辭歲：舊事重逢與未知邊界

```yaml
GUSAN_CISUI_LIU11:
  gusan_entry:
    - "顧三以商人／定陶商會拜訪者身分到觀止，之前已向商會投帖。"
    - "他到白御行包廂，不得寫成專程追辭歲而來。"

  public_old_event:
    - "外界可知：十幾日前顧三付五十兩、與辭歲有一炷香之私人安排、燈熄後再送客。"
    - "顧三本夜明示自己不覺得五十兩花冤。"
    - "上述足以形成外界風月腦補／傳聞，但不是私室內事件證據。"

  private_unknown:
    - "當晚一炷香私室內究竟發生何種身體／成人事件，仍只有當事二人可能知道。"
    - "不得補寫裸身、性交、保護、戀愛或其他未有來源之細節。"

  current_relation:
    - "本夜二人有可觀察的熟悉與玩笑，可一起碰杯。"
    - "不得因此升格為情人、保護關係或戀愛承諾。"

  later_last_observed:
    - "白御行一行離開原包廂後，顧三與辭歲仍留在該處。"
    - "其後夜生活與是否同行，UNKNOWN。"
```

---

# 8｜辭歲重要客戶狀態

```yaml
CISUI_CLIENT:
  inherited:
    fixed_deposit:
      principal: "5,000,000兩"
      term: "5年"
      rate: "五分"
      status: "SIGNED_AND_EFFECTIVE"
    remaining_liquid: "5,800,000兩"

  liu11:
    - "以重要客戶／金主身分受招待。"
    - "她有考慮未來再添丫鬟，至少一名希望具真實護衛能力；女子競技可作第一層觀察來源。"
    - "本夜未完成新的丫鬟購買。"
```

---

# 9｜趙受益購四契並轉贈六條／楊玉環

```yaml
FOUR_MAID_CONTRACT_TRANSFER:
  prior_title:
    source_axis:
      - "HOT V4.1 六名白御行側新丫鬟中：楊玉環2、六條2、李清照1、柳如是1。"
      - "其中楊玉環、六條各自實際挑人與使用；不等於她們原本持契。"

  liu11_transaction:
    seller: "白御行"
    buyer: "趙受益"
    object:
      - "楊玉環正在使用之2名成年丫鬟之身契"
      - "六條御息所正在使用之2名成年丫鬟之身契"
    total_price: "200兩"
    pricing_logic:
      - "白御行明示嫌逐張計算麻煩，直接取整數二百兩。"
      - "不得由此反推四人原始逐張成本或白御行實際盈虧。"
    payment:
      status: "PAID"
      payer: "趙受益"
      receiver: "白御行"
      amount: "200兩"

  zhao_gifts:
    completed:
      - "趙受益確認二女是否願意收後，六條明示要，楊玉環明示要。"
      - "兩張契轉予六條，兩張契轉予楊玉環。"
      - "二女均收下此份心意。"
    relation_boundary:
      - "二女收下禮物 != 已承認趙受益的愛、婚姻、排他戀愛或其他未明示承諾。"
      - "『愛』只停在白御行玩笑／媒合話術；趙受益本人表示由二女自己判斷。"
```

---

# 10｜奴籍／妓籍法位與四大金剛現況

```yaml
PROSTITUTION_STATUS_WORLD_RULE:
  gm_route_correction:
    - "奴籍與妓籍可同時存在。"
    - "奴籍處理主僕／身契位置；妓籍處理風月職業／合法接客位置，兩者不可互相偷換。"
    - "持有女奴身契不等於持有她作妓女接客之職業權。"
    - "未入妓籍之奴籍女子若被主人強迫按妓女方式陪酒／接客，在本世界具有對主人提出救濟／控訴之位置。"
    - "妓籍一旦正式登記，不可撤銷，為終身妓女身分；自由與否是另一軸。"

FOUR_GUARDS_STATUS:
  bai_sanshierniang:
    slave_status: "仍屬白御行奴籍側"
    prostitution_intent: "本人已明確決定要登妓籍"
    registration_complete: false
    note:
      - "她明示未來作妓女時男人由自己挑、錢自己收；白御行不是她的鴇母。"

  bai_hongling:
    slave_status: "仍屬白御行奴籍側"
    prostitution_intent: "更偏向登妓籍／有明顯興趣"
    registration_complete: false
    note:
      - "仍未形成正式『現在就登』的最終完成事件。"

  bai_mingfan:
    slave_status: "仍屬白御行奴籍側"
    prostitution_intent: "目前不登"
    registration_complete: false

  bai_xi:
    slave_status: "仍屬白御行奴籍側"
    prostitution_intent: "目前不登"
    registration_complete: false
```

---

# 11｜四大金剛＋李清照：女客身分試場

```yaml
FEMALE_GUEST_TRIAL_LIU11:
  framework:
    - "白御行放四大金剛當晚休假。"
    - "四人自行付錢以觀止『女客』身分進大堂。"
    - "她們不是掛牌妓女，不主動攬客，不向男人收客錢。"
    - "男人若主動搭訕，她們可自行決定是否回應。"
    - "四人被要求明白告知對方：自己不是妓女。"
    - "李清照本人也接受同一玩法，付費作女客下場。"

  observed:
    bai_sanshierniang:
      - "有年輕男客主動搭話。"
      - "她先說明自己是付錢女客、不掛牌、不接客錢，再與對方聊賭局。"
      - "後續是否發展，UNKNOWN。"

    bai_hongling:
      - "第一名男客開口問價，她明示自己不是妓女，對方道歉離開。"
      - "另一名較年輕男客先問能否同坐；她再說明女客身分，允許對方請酒並坐下聊天。"
      - "後續是否發展，UNKNOWN。"

    bai_mingfan:
      - "有中年男客因賭票搭話。"
      - "她說明自己不是觀止姑娘後，允許對方坐下。"
      - "後續是否發展，UNKNOWN。"

    bai_xi:
      - "有男客邀一起喝酒；她明示自己是女客並直接表示不想，對方離開。"
      - "她沒有因此形成失落或改變妓籍意向。"

    li_qingzhao:
      - "仍不是妓女，未登妓籍。"
      - "有一名約三十多歲、衣著普通但整潔的男客以麗華酒坊新酒話題搭話。"
      - "李清照先明示自己是女客、不是掛牌姑娘、不接客也不收他的錢，之後允許他坐下談酒。"
      - "二人後續聊酒、地方風味等；最後結果與是否另有私人發展，UNKNOWN。"

  anti_inference:
    - "被搭訕／同桌／請酒 != 接客、性、戀愛、承諾。"
```

---

# 12｜李清照妓籍討論：本夜未登

```yaml
LI_QINGZHAO_STATUS_LIU11:
  baseline: "NOT_A_PROSTITUTE"
  discussion:
    - "白御行曾建議她是否登妓籍，以便合法進場挑男人。"
    - "李清照承認觀止混合風月場會使她感覺男人並非全無意思。"
    - "她明示本夜不登妓籍。"
    - "她後來表示自己拒絕的理由不是單純守『良家』招牌，而是目前沒有覺得妓籍值得拿終身身分交換。"
  state:
    prostitution_registration: "NOT_CHANGED"
    future_position: "可自行再想；不是承諾未來會登"
```

---

# 13｜柳如是：本夜未形成新掛牌事件

```yaml
LIU_RUSHI_LIU11:
  observed:
    - "曾對『若自己舊有妓籍仍能使用，今晚可自行挑男人』表達興趣。"
  not_completed:
    - "本 HOT 未觀察到她正式向潘金蓮掛牌、接客或帶男人離場。"
  therefore:
    - "不得把討論升格為當晚已掛牌／已接客。"
```

---

# 14｜張麗華酒促姑娘構想

```yaml
ZHANG_LIHUA_PROMO_TEAM:
  state: "PROPOSAL_WITH_PERSONAL_INTEREST"
  trigger:
    - "白御行提出『酒促姑娘』概念，並提醒不必只借觀止姑娘，可自組班底。"
  zhang_response:
    - "張麗華對自己養一班懂酒、懂客、能推酒的女人產生明確商業興趣。"
    - "她傾向先做小規模第一批，再看哪些人真的能提高酒水銷售。"
  route_rule_discussed:
    - "純酒促與妓女陪酒／接客應分開。"
    - "良家女子可做推酒、介紹、斟酒等酒坊工作；若進入本世界認定的妓業陪酒／接客，需處理相應妓籍法位。"
  not_yet:
    - "未正式成立酒促團隊。"
    - "未招募第一批人。"
    - "定陶商會未承諾投資。"
```

---

# 15｜蘇清：今晚出現但後段 UNKNOWN

```yaml
SUQING_LIU11:
  fixed_identity:
    - "蘇清為可自主接客／不接客、自己選男人的自由妓女；不是白御行可分配之普通姑娘。"

  observed:
    first:
      witness: "張麗華"
      time: "紅娘壓軸前"
      place: "前堂東側一帶"
      state:
        - "看見蘇清一人活動。"
    second:
      witness: "觀止跑堂"
      time: "紅娘散場後一陣"
      place: "由東側往後廊方向"
      state:
        - "看見蘇清一人往後廊走。"

  unknown:
    - "是否接客。"
    - "是否去白玉池。"
    - "是否找人、休息、回房或有其他私人安排。"
    - "不得因『十幾天沒接客』『有錢仍做妓女』推導她本夜一定缺男人。"
```

---

# 16｜小翠：正式重新入場之第一晚

```yaml
XIAOCUI_LIU11:
  observed:
    - "小翠確實下到大堂。"
    - "錦棠／白御行後來從樓上看到她與一名男客同桌說話。"
    - "小翠看來仍較拘謹，但有回話與笑，沒有被觀察到當場逃離。"

  unknown:
    - "該男客是否成為正式客人／付何種錢。"
    - "小翠後續是否接客、進房、性交或留宿。"
    - "不得由前一夜白御行私人正向成人經驗推導她已能接受所有男客。"
```

---

# 17｜白玉池：高級會員預約制已被潘金蓮接受

```yaml
WHITE_JADE_MEMBERSHIP_PLAN:
  state: "PAN_JINLIAN_ACCEPTED_FOR_LIU12_NIGHT_OPENING"
  purpose:
    - "不把白玉池當普通澡堂，而作稀缺、高級、私人雙人時段。"

  membership:
    security_deposit: "50兩"
    function:
      - "取得會員／預約資格。"
      - "不是一次性買女人或買終身使用權。"
    per_use_fee:
      state: "YES_BUT_AMOUNT_UNSET"
      note:
        - "潘金蓮明示每次使用仍另收費；本輪未定具體金額。"

  night_slots:
    groups_per_night: 4
    exclusivity: "每組獨佔一個時辰"
    reset:
      - "每組之間留清洗、換水、布巾／更衣與場地重置時間。"
      - "下一組進場時原則上看不到上一組留下的使用痕跡。"

  entry:
    single_person: "FORBIDDEN"
    party_size: 2
    companion_supply:
      - "觀止不替會員配女人／配伴。"
      - "會員必須自行邀到另一名願意共同入池的成年客人。"
    current_gender_rule:
      - "潘金蓮於現場將原提案的『必須帶女伴』收斂為『兩名成年客人共同入場』；不另管兩人關係／性別。"
    both_must_agree: true

  reservation:
    advance_booking: true
    walk_in_immediate_use: false
    no_queue_jump: true
    transfer_resale: "FORBIDDEN"
    note:
      - "有錢也不能現場拍五十兩要求立刻塞入時段。"

  daytime_internal_use:
    - "白天非營業時間留給觀止自己人使用，不與夜間會員四組名額競爭。"
    - "楊玉環可延續白天使用習慣。"
```

---

# 18｜楊玉環 × 白玉池既有使用與宣傳候選

```yaml
YANG_WHITE_JADE:
  prior_use:
    - "觀止歇業期間，楊玉環已近十日持續使用白玉池；玩家明示未開放期間她天天洗。"
  implication:
    - "她不是白玉池開放後才臨時試用的代言候選。"
  candidate_marketing:
    phrase: "楊貴妃第一指名"
    state: "PROPOSAL_PENDING_YANG_YUHUAN_CONSENT"
    possible_stage_use:
      - "可候選請楊玉環公開談實際使用感受／使用頻率。"
    forbidden:
      - "楊玉環本人尚未同意前，不得對外掛名。"
      - "不得先替她說『天天』作正式廣告台詞。"
```

---

# 19｜錦棠 × 白御行：公開／私人玩笑與同宿

```yaml
JINTANG_BAI_LIU11:
  relationship_dialogue:
    - "白御行表示錦棠若未來想勾其他男人，他不能把她綁住。"
    - "錦棠回答：她若真想看別的男人會自己去；今晚目前更想和白御行待在一起。"
    - "她表示若未來真看上別的男人，可以先告訴白御行；這是告知，不是請示。"
    - "以上不得推成她未來必然找別的男人或白御行已簽署任何永久開放關係契約。"

  future_star_jokes:
    - "二人談及錦棠若成為商會經紀約下的明星，公開戀情可能被外界解讀成會長潛規則旗下女明星。"
    - "『地下情』等語主要是二人當晚玩笑／風險討論，未形成正式公關契約。"

  overnight:
    - "榴月十一日晚，白御行與錦棠同宿。"
    - "玩家明示私人內容不說、不記。"
    - "SAVE 不推導當晚是否性交、具體身體行為、射精、避孕或其他未明示細節。"
```

---

# 20｜白御行、錦棠與潘金蓮之白玉池對話位置

```yaml
WHITE_JADE_RELATION_TO_PLAYER:
  confirmed:
    - "白御行與錦棠曾拿未來會員資格互相開玩笑，錦棠可自己訂時段再叫白御行陪。"
  not_completed:
    - "榴月十二日晚實際第一個預約人、使用人、付款人尚未成立。"
    - "不得因玩笑直接建立白御行／錦棠已訂首場。"
```

---

# 21｜仍然 UNKNOWN／OPEN

```yaml
OPEN_THREADS_V4_4:
  suqing:
    - "榴月十一日晚往後廊後的最終去向與夜生活。"

  xiaocui:
    - "與男客同桌後是否形成正式接客／進房／成人事件。"

  gusan_cisui:
    - "白御行一行離席後二人的後續；不得把外界腦補當真相。"

  li_qingzhao_guest_man:
    - "與談酒男客聊到何時、是否交換姓名／再約／私下同行。"

  four_guards_guest_trial:
    - "三十二娘、紅伶、明礬當晚與搭訕男客最後是否繼續、散席或另有安排。"

  prostitution_registration:
    - "三十二娘已決定要登妓籍，但尚未完成正式登記。"
    - "紅伶仍是偏向；明礬／白希未登。"

  li_qingzhao_registration:
    - "本夜未登妓籍。"

  liu_rushi:
    - "是否之後真的以既有妓籍掛牌／選男人，本 HOT 無觀察。"

  white_jade:
    - "榴月十二日晚會員制第一批四組預約名單。"
    - "每次使用費金額。"
    - "楊玉環是否同意『楊貴妃第一指名』與上台談使用感受。"

  zhang_lihua_promo_team:
    - "是否真的招募、商會是否投資、第一批人數與薪酬。"
```

---

# 22｜禁止倒灌與接關提醒

```yaml
DO_NOT_AUTO_RESOLVE:
  - "蘇清往後廊 != 去白玉池 != 接客 != 找男人。"
  - "小翠與男人同桌 != 已接客／已性交。"
  - "顧三與辭歲共處 != 戀愛／保護／性交。"
  - "六條、楊玉環收下趙受益轉贈身契 != 接受『愛』或承諾戀愛。"
  - "三十二娘想登妓籍 != 已完成登記。"
  - "紅伶偏向登妓籍 != 已完成登記。"
  - "李清照願意以女客看男人 != 已成妓女。"
  - "四大金剛作女客與男人聊天 != 在偷偷接客。"
  - "白玉池會員制被潘金蓮接受 != 榴月十二日晚已經完成第一組使用。"
  - "『楊貴妃第一指名』仍待本人同意，不能提前掛名。"
  - "白御行與錦棠同宿之私人內容由玩家明示不記，不得回填。"
```

---

# 23｜一句接關摘要

> **榴月十一日晚，觀止正式重新開幕：女子競技、賭盤、既有姑娘與商會培訓女人同時進場，紅娘以脫衣舞接公開成人自我慰藉高潮完成壓軸。白御行以客人身分開最大包廂，顧三與辭歲再會但舊日一炷香私事仍保持未知。白御行把楊玉環、六條正在使用的四張白御行側丫鬟身契，以總價二百兩賣給趙受益；趙受益付款後，兩張送六條、兩張送楊玉環，二女收下心意而未承諾『愛』。四大金剛與李清照其後以付費女客身分進大堂，被動回應搭訕且明示自己不是妓女；三十二娘確定想登妓籍，紅伶更偏向，明礬與白希不登，李清照本夜亦不登。蘇清只知前堂出現並在紅娘散場後獨自往後廊；小翠只知與一名男客同桌，後續均未知。潘金蓮接受白玉池五十兩會員押金、夜間四組、雙人預約、一組一時辰、中間清洗重置、禁止單人／插隊／轉售、白天自己人使用之方案，預定榴月十二日晚啟用；楊玉環此前近十日持續使用，但『楊貴妃第一指名』仍待本人同意。白御行與錦棠榴月十一日晚同宿，私人內容不記。現已榴月十二日白日。**


<!-- END PROMOTED HOT SOURCE -->


<!-- BEGIN PROMOTED HOT SOURCE: 觀止青樓_白御行線_HOT_SAVE_V4.5_榴月十二日晚_白玉池代言首夜_紅娘阿莉婭雙人場_三十二娘妓籍申請_蘇清十八日商會工_黑公子小桃交易同宿版.md -->

# 觀止青樓｜白御行線 HOT SAVE V4.5
## 理火三年榴月十二日晚｜白家新宅採購規劃 × 蘇清十八日商會工 × 紅娘五套新節目提案 × 阿莉婭妓籍／處女拍賣法位校正 × 三十二娘妓籍申請 × 四大金剛女客第二夜 × 白玉池代言首夜 × 紅娘×阿莉婭雙人場 × 黑公子小桃交易同宿版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V4_5_LIU12_NIGHT_WHITE_JADE_ENDORSEMENT_ALIYA_HONGNIANG_DUO_SANSHIERNiang_REGISTRATION_SUQING_18DAYS_HEIGONGZI_XIAOTAO"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V4.5"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V12.0"
  current_runtime_overlay:
    - "GUANZHI_PATCH_ACTION_BEFORE_EXPLANATION_V0.1-EXP"

  story_time_span:
    start: "HOT V4.4 後／理火三年榴月十二日中午"
    current: "理火三年榴月十二日晚／觀止營業中後段"
  exact_clock: "UNKNOWN"

  record_state: "HOLD_IN_XIAOTAO_ROOM_AFTER_COMPLETED_50_TAEL_SERVICE_AND_VOLUNTARY_OVERNIGHT_AGREEMENT_BEFORE_DAWN"

  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V4.4_榴月十二日白日_重新開幕夜結_趙受益四契轉贈_四金剛女客試場_白玉池會員制_錦棠同宿版.md"
  long_term_master_before_this_save: "觀止青樓_白御行線_MASTER_SAVE_V4.4-R1_截至HOT_V4.0固化_保留V4.1-V4.4_HOT版.md"

  save_scope:
    - "榴月十二日中午起床節奏與觀止夜生活作息校正"
    - "李師師昨夜設席回報、月事仍未至／是否有喜仍 UNKNOWN、白家新宅與家具採購規劃"
    - "蘇清二十八日私約重新拆帳：商會二十日中已預支二日，榴月十三日起剩十八日；之後仍欠白御行八日私人共同生活"
    - "內衣／衛生巾／走秀專案由常煒統籌，蘇清自榴月十三日起進場幫忙；戰鬥肚兜方向與八套樣品約定"
    - "紅娘五項成人舞台新玩法之提案狀態，以及牙行先找高技術繩工而不洩漏成人用途"
    - "白御行×潘金蓮一場決勝負成人私約，日期未定"
    - "阿莉婭已具妓籍、仍保留處女一次性拍賣標的之法位校正；昨夜本人確認標的仍有效"
    - "紅娘×阿莉婭雙人成人舞台正式演出成立，阿莉婭處女拍賣標的未被本場消耗"
    - "白三十二娘正式啟動妓籍申請；白紅伶仍未申請；白明礬／白希仍不入"
    - "白紅伶、白三十二娘第二晚以普通女客進場，自主挑選可能滿足性需求的男人；後續結果 UNKNOWN"
    - "白玉池『楊貴妃第一指名』由楊玉環本人同意並正式公開代言；會員／預約首夜啟動"
    - "白御行以『黑公子』匿名坐一兩外圍席，與新來姑娘小桃形成交易；原五百兩方案撤銷，改為今晚五十＋下次預付五十"
    - "小桃今晚成人口部服務已完成；另五十兩尚未履行；小桃自願留下同宿至早上但目前尚未推進至天亮"
```

---

# 0｜來源、法位與反污染

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "HOT V4.4"
    role:
      - "榴月十一日晚重新開幕之直接前置。"
      - "四大金剛首次女客試場、白玉池會員制接受、錦棠同宿等狀態繼承。"

  current_route_conversation_commit:
    role:
      - "HOT V4.4 後至本次 HOT SAVE 命令前之直接劇情。"
      - "玩家對自身言行、妓籍制度、阿莉婭法位、蘇清二十八日私約拆帳與商會工作天數之明示校正。"
      - "NPC 可觀察回應、本人自述、本人同意、付款、預付、申請、公開演出與公開代言。"

AUTHORITY_NOTES:
  - "玩家本輪明示修正：妓籍於官府登記完成時即成立，一旦成立即終身不可回歸良家；停止接客／退休／改職不等於恢復良籍。"
  - "阿莉婭早已是妓籍，不存在等待重新入妓籍／重新掛牌後才可成人表演之限制；先前該錯誤推論撤銷，不進世界事實。"
  - "成人事件、同意、妓籍、奴籍、商業拍賣標的、實際接客、私人感情分軸保存。"
  - "任何人物對昨夜私人內容的選擇性回答，只能按其法位保存；未說出的部分不補全。"
  - "SAVE 不把成人舞台表演之觀眾興奮、傳聞或價格預期寫成已成交價格。"
```

---

# 1｜DIRECTOR RUNTIME LOCK｜V12.0 現行接關法位

```yaml
DIRECTOR_RUNTIME_LOCK:
  core_runtime: "觀止青樓_主程序_V12.0_FIELD_STATE接戲分析器場態整合正式版"

  analyzer_lifecycle:
    state: "ABSORBED_INTO_V12_CORE"
    rule:
      - "分析器不是獨立舊 PATCH；不得再次把『分析器退場 PATCH』當前台 Runtime 載入。"
      - "ACTIVE → 完成最低必要辨認 → SILENT_BACKGROUND。"
      - "只有真正新 Trigger 才 REACTIVATED_SCOPED，且只喚醒受影響層。"
      - "成人強度增加、鏡頭靠近、身體反應增強、語氣變粗，不等於事件換軌，不足以重啟全套分析器。"

  field_state:
    - "FIELD_STATE 只保存事件刺激至人物決定間之場態，不取得世界事實權、人物決定權或最終裁決權。"

  authority_direction:
    correct:
      - "EVENT / CHARACTER / RELATION → RENDERING"
    forbidden:
      - "RENDERING / GATE → CHARACTER"
      - "RENDERING / GATE → EVENT"
      - "限制層不得先決定成人事件不存在或自動淡出。"

  action_before_explanation:
    state: "ACTIVE_EXPERIMENTAL_OVERLAY_NOT_MERGED_INTO_V12"
    use:
      - "人物行動、事件與回饋先顯影；治理說明不得搶前台。"

  regression_note:
    - "本串曾發生一次成人場景 Rendering 提前奪取輸出主體之故障；已審計並撤銷該污染段落，不取得世界事實權。"
    - "其後小桃場已從事件硬狀態重新顯影。"
```

---

# 2｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年榴月十二日"
  time: "晚／觀止營業中後段；精確時刻未知"
  primary_location: "觀止／春梅開出的普通客房／小桃房內交易場景"

  player:
    name: "白御行"
    public_alias_tonight: "黑公子"
    current_state:
      - "今晚刻意不帶四大金剛，以普通客身分坐一兩外圍席。"
      - "目前已與小桃完成今晚重新談定之五十兩成人服務。"
      - "另付五十兩作下一次預付，尚未履行。"

  xiaotao:
    current_state:
      - "已收今晚五十兩與下一次預付五十兩。"
      - "今晚約定項目已完成。"
      - "自行同意不另計入該五十兩、留房陪白御行睡至早上。"
      - "此刻尚未推進到天亮，因此只記『同宿意向已成立』，不記『已睡到早上』。"

  direct_resume_point:
    - "可從小桃房內準備同宿、夜間其他觀止事件自然發酵，或時間小幅推進至下一個需要玩家回應之節點。"
    - "不得自動替白御行進一步發生新的成人行為。"
    - "不得自動消耗小桃預付的下一次五十兩。"
```

---

# 3｜觀止夜生活作息校正

```yaml
NIGHTLIFE_RHYTHM:
  gm_correction:
    - "觀止屬夜生活場域，主要人物普遍以中午前後起床為正常節奏。"
    - "不得每一日都寫成清晨／白天早起。"
    - "榴月十二日本日接戲由中午起。"
```

---

# 4｜李師師：昨夜設席、月事狀態與白家規劃

```yaml
LI_SHISHI_LIU12:
  last_night_table_report:
    self_report:
      - "昨夜設席順利。"
      - "有兩三名男人搭話。"
      - "其中一名喝多、問她今晚是否有空；朋友把人拉走。"
      - "另有一名先問能否敬酒，師師喝一杯但未允許其坐下；對方離開。"
      - "師師本人判斷昨夜未達需要稱為實質騷擾之程度。"

  menstruation_pregnancy:
    menstruation: "仍未來／比平常晚"
    pregnancy: "UNKNOWN"
    rule:
      - "月事每多晚一天，只可提高懷疑，不可自動升格為懷孕事實。"

WHITE_HOME_PLAN:
  existing_rental:
    term: "10年"
    rent: "8,000兩"
    source: "白御行本輪明示"

  spatial_plan:
    - "白家新宅需預留未來奴婢／僕婦／護院／工人／車夫／帳房等常駐人手之擴充空間。"
    - "需正式大廚房、備菜、米糧、乾貨、柴炭、小灶、洗衣、浴房、布草、庫房等後勤骨架。"
    - "不得只按現有主人房數量畫死。"

  jintang_house:
    - "錦棠之房屋／住處應與白家分法位；可鄰近、可往來，但屬錦棠自己的房子，不併入白家妻妾格局。"

  procurement_team:
    lead: "李師師"
    confirmed_participants:
      - "李瓶兒"
      - "浮香"
      - "張麗華"
      - "白三十二娘"
      - "白紅伶"
      - "白明礬"
      - "白希"
    principle:
      - "不是買便宜，而是買齊。"
      - "白御行明示家具與生活用品不用為他省錢。"
      - "主人房與公共家具、床櫃、廚房器物、僕役房基本用品、酒櫃、琴具等按實際需要採買。"

  advance_payment:
    holder: "李師師"
    amount: "1,000兩"
    purpose:
      - "採買時付訂、定貨、卡貨。"
    final_payment:
      - "貨送到、驗收後由店家持單據到定陶商會請款。"
      - "帳目歸白御行個人帳，不得算商會公務支出。"

  budget:
    - "白御行先前談過總價一萬兩會開始心痛，但隨後明示『錢不用省／家具不是只用一天』；現行採買原則以買齊與耐用為主，不把一萬兩當硬上限。"
```

---

# 5｜蘇清昨夜去向：新可知與仍未知

```yaml
SUQING_LIU12:
  objective_observed:
    - "榴月十二日中午前後，觀止丫頭從東後院小客房送水處回來，確認蘇清已起。"
    - "送水丫頭進房時只看到蘇清一人。"
    - "房內床有使用痕跡、桌上有一壺酒。"

  self_report_about_liu11_night:
    - "蘇清明示昨夜確實碰見了一個人，但沒有說那人是不是男人。"
    - "她拒絕交代碰見後做了什麼。"
    - "她明示昨夜沒有接觀止安排的客、沒有被點牌、沒有被人付錢包夜。"
    - "她自述昨夜過得不錯、睡得也不錯。"

  still_unknown:
    - "昨夜碰見的人身分。"
    - "是否有私人成人事件。"
    - "是否有人曾進東後院小客房後再離開。"
    - "不得由中午送水時她獨自在房推導整夜始終獨處。"

  westmen_compensation:
    - "西門慶案已判；蘇清視其為討回一部分公道。"
    - "潘金蓮對蘇清之五萬兩民事和解／賠償仍以既有法位保存，完整實付狀態不得由本輪推成已全入袋。"
    - "西門慶家產清算後實際最終撥付蘇清之金額／到帳時間，本輪仍未得到官面硬數字。"

  future_life_preferences:
    self_report:
      - "若資金真正落袋，蘇清考慮買一處自己的小宅。"
      - "會保留一大筆不動資金，避免再陷入沒有錢、沒有地方去、受制於人的狀態。"
      - "也考慮做生意或放息。"
      - "即使日後不再經常掛牌／接客，妓籍法位仍終身存在，不得寫成恢復良家。"
```

---

# 6｜蘇清二十八日私約：二十日商會工 → 剩十八日 → 最後八日

```yaml
SUQING_28DAY_AGREEMENT:
  original_private_total: "28日"

  current_split:
    merchant_association_credit: "20日"
    private_cohabitation_after_merchant_work: "8日"

  merchant_days:
    originally_allocated: 20
    already_prepaid_worked: 2
    source_of_2days:
      - "蘇清之前幫商會／白御行選人之兩日，玩家本輪明示可預支扣抵。"
    remaining: 18
    start_date: "理火三年榴月十三日"
    supervisor: "常煒／定陶商會副會長"
    status: "TO_START_NEXT_DAY"

  assigned_project_field:
    - "走秀相關工作"
    - "內衣／戰鬥肚兜產品線"
    - "衛生巾研發相關女性使用回饋與測試"

  limits:
    - "這十八日是商會專案工作，不是白御行私人陪伴日。"
    - "常煒若要她做超出專案之額外工作，是否另算工資由商會／蘇清另行談。"
    - "十八日做完後，才進入原私約剩餘八日。"
    - "八日是共同生活私約，不等於八晚自動性交或永久同意。"

  after_contract:
    - "蘇清若覺得自己能在商會長期工作，可在二十八日帳清後自行決定是否繼續；不是白御行自動安排。"
```

---

# 7｜戰鬥肚兜／內衣專案方向

```yaml
LINGERIE_PROJECT_DIRECTION:
  commercial_rule_from_bai:
    - "布越少，不應因省布而變便宜；高價應來自版型、剪裁、工藝、視覺與成人吸引力。"

  product_positioning:
    ordinary_bellyband: "NOT_TARGET"
    target: "戰鬥肚兜／成人情境內衣"
    purpose:
      - "不是普通女人日常遮體或工作用肚兜。"
      - "核心是穿上後具有明顯成人誘惑與讓觀看者興奮之效果。"
      - "漂亮但只適合短時間成人情境也可成為產品，而非要求如日常衣物耐穿。"

  suqing_role:
    - "蘇清負責把上述方向轉譯給常煒，避免男性團隊只按布料成本或普通肚兜思路設計。"
    - "也可向女性試穿者收集是否願意穿、是否舒適、何種場合願意穿等回饋。"

  eight_samples:
    state: "AGREED_DIRECTION_NOT_YET_PRODUCED"
    details:
      - "白御行要求做好後留下八套不同路數的戰鬥服／戰鬥肚兜樣品。"
      - "蘇清答應八套不能只是同款換色，應有不同風格。"
      - "八套預計可在蘇清最後八日私約期間一晚一套讓白御行看；衣服展示約定不等於每天其他成人行為自動同意。"
```

---

# 8｜紅娘新節目／工坊需求：五項提案

```yaml
HONGNIANG_NEW_SHOW_IDEAS:
  status: "PROPOSAL_AND_SEARCH_STAGE"
  built_items: "NONE_CONFIRMED"

  idea_1_parade_wooden_horse:
    concept:
      - "紅娘穿著完整／端正進場，騎可移動木馬遊場。"
      - "木馬內含成人舞台機關，使觀眾在尚未脫衣前就知道她正受機關作用。"
      - "至少兩人牽／護場，保護紅娘不被客人伸手碰觸。"
    status: "PROPOSAL"

  idea_2_manual_crank_stage_machine:
    concept:
      - "舞台固定成人機關由手柄驅動。"
      - "觀眾可競價取得一輪操作機關之權，但買到的是操作權，不是碰紅娘本人之權。"
      - "每輪時間、最大速度、護場與停機需明確。"
    status: "PROPOSAL"

  idea_3_rope_suspension:
    concept:
      - "找真正懂人體繩藝／承重／懸吊的師傅，先教、先低位測試，再考慮正式舞台。"
      - "紅娘與白御行均表示想學。"
    status: "MASTER_SEARCH_STARTED"

  idea_4_triangle_restraint_stage:
    concept:
      - "以三角形舞台結構、束縛與腳部視覺負重形成強烈受制畫面。"
      - "實際接觸與承重方式需由真正師傅安全設計；外觀可以狠，不得把舞台視覺直接等同真實刑具。"
    status: "CONCEPT_ONLY"

  idea_5_pillory_partnered_adult_show:
    concept:
      - "紅娘頭／雙手固定於舞台枷鎖，搭配成年男性演員共同完成公開成人表演。"
      - "男方是表演者，不是花錢取得碰觸資格的客人。"
      - "候選男演員可由潘金蓮提供，但紅娘保有最終選人與排練同意。"
    status: "CONCEPT_ONLY"

  global_rule:
    - "以上均是新節目候選；除找繩工外，尚無一項在本輪完成製作或正式演出。"
```

---

# 9｜牙行繩工尋人：對外只說高度專業繩工

```yaml
ROPE_MASTER_SEARCH:
  strategy:
    first_source: "牙行"
    fallback_sources:
      - "戲班"
      - "雜技／走江湖班子"
      - "商旅線"

  external_brief:
    - "精通繩工。"
    - "手法細膩。"
    - "結法多。"
    - "承重穩。"
    - "收放俐落。"
    - "有特殊技藝者優先。"
    - "用途只說觀止新舞台需要特殊繩工，不對外說『綁女人／成人懸吊』，避免情報提前外洩。"

  test_plan:
    - "到場後再測技術；先用繩、沙袋、木架等觀察承重、解繩、收放與細膩度。"
    - "是否進一步做人體繩藝／教學，等確認真正有本事後才談。"

  current_result: "尚未找到／帶回任何具名師傅"
```

---

# 10｜白御行 × 潘金蓮：一場決勝負成人私約

```yaml
BAI_PAN_PRIVATE_CHALLENGE:
  status: "MUTUALLY_ACCEPTED_FUTURE_CHALLENGE"
  confirmed:
    - "白御行私下問潘金蓮是否有興趣與他對戰一場。"
    - "潘金蓮明示有興趣，但不是當下開戰。"
    - "二人約定未來『一場決勝負』。"
    - "日期、地點、具體內容尚未固定。"
  current_interaction:
    - "白御行當場有親密挑釁性身體接觸；潘金蓮沒有把它升格成當場開戰，表示記帳、日後再算。"
  not_established:
    - "誰會獲勝。"
    - "何時正式發生。"
    - "此私約不等於白御行可隨時要求潘金蓮開始。"
```

---

# 11｜妓籍制度：本輪 GM 正式鎖定

```yaml
PROSTITUTION_REGISTRY_BASELINE_GM_CONFIRMED:
  core_rule:
    - "妓籍在官府正式登記完成時即成立。"
    - "一旦入妓籍，法律履歷永久不可回到良家。"
    - "所謂『從良』若使用，只能表示停止接客／改變生活方式，不能表示法律恢復良籍。"

  occupation_vs_legal_status:
    - "妓女可退休、經商、當師爺、當掌櫃、買宅、放貸、長年不接客。"
    - "上述改職都不洗掉妓籍。"

  slave_axis:
    - "奴籍與妓籍為獨立法位，可同時存在。"
    - "奴籍解除不會洗掉妓籍；妓籍成立也不等於所有者自動取得其接客／客人分配權。"

  social_function:
    - "良家被設定為具有不可逆履歷保證的法位；曾入妓籍者不能在法律上重新偽裝成從未入妓籍的良家。"
```

---

# 12｜阿莉婭：妓籍已成立 × 處女一次性拍賣仍有效

```yaml
ALIYA_STATUS_CORRECTION:
  legal_identity:
    prostitution_registry: "ALREADY_REGISTERED"
    status: "LEGAL_PROSTITUTE"
    permanence: "LIFELONG"

  commercial_state:
    virginity_asset: "STILL_PRESERVED"
    one_time_auction: "PENDING_FUTURE_COMMERCIALIZATION"
    note:
      - "觀止不讓她隨便消耗處女標的，是最大化一次性拍賣價格之商業策略，不是因她法律上不能成人表演／接客。"

  legal_and_personal_capacity:
    - "阿莉婭可依法以妓女身分接客、成人表演、與成年客人發生自願成人關係。"
    - "具體是否做，仍由她本人決定。"

  liu11_night_self_report:
    - "潘金蓮因處女拍賣標的需要詢問昨夜是否發生使標的失效之事。"
    - "阿莉婭本人明示：昨夜有與人說話、喝酒，但沒有發生使處女拍賣標的失效之事。"
    - "此處保存為本人明示與觀止商業帳面依據。"
```

---

# 13｜紅娘 × 阿莉婭：雙人成人舞台成立

```yaml
HONGNIANG_ALIYA_DUO_LIU12:
  pre_show:
    - "白御行提出：在阿莉婭保留處女拍賣標的期間，由紅娘與她搭一場女女成人表演，可提高阿莉婭曝光與拍賣行情。"
    - "白御行拒絕觀看下午排練，以保留正式演出新鮮感。"
    - "紅娘親自向阿莉婭說明，不由白御行代談。"
    - "阿莉婭要求不能只做紅娘陪襯；紅娘接受兩人各有段落、再合流。"
    - "潘金蓮明示演出費、賞錢與未來處女拍賣是分開帳；本輪未固定演出費／賞錢數字。"

  public_show:
    status: "COMPLETED"
    structure:
      - "阿莉婭先單獨登場，紅娘後出。"
      - "演出刻意保留阿莉婭處女拍賣標的，不把第一次提前消耗。"
      - "二人形成雙向成人舞台互動，包含可觀察的主動接近與親吻。"
      - "阿莉婭從起初緊張逐步取得自己的台上存在感，不只是紅娘的陪襯。"
      - "收幕刻意未把所有成人張力一次演盡。"

  commercial_effect_observed:
    - "現場對阿莉婭本人之關注與呼喊明顯增加。"
    - "有客人口頭推測她未來處女拍賣價格會更高；這只是客人行情預期，不是已成交價。"
    - "潘金蓮未在本場即時宣布新拍賣底價。"

  relation_boundary:
    - "紅娘與阿莉婭成功搭檔一場，不自動升格為戀愛／固定女女關係。"
```

---

# 14｜白三十二娘：妓籍申請正式啟動

```yaml
SANSHIERNiang_REGISTRATION:
  prior_intent: "已於 HOT V4.4 明示想入妓籍"
  liu12_confirmation:
    - "經一夜後仍明示決定不變。"
    - "知道妓籍一旦官府登記完成即終身不可回良家。"

  process:
    status: "APPLICATION_STARTED_NOT_YET_REGISTERED"
    handler: "春梅"
    collected_information:
      - "姓名／年歲／原籍／現奴籍歸屬／主人／現住處等行政資料。"
    ownership_confirmation:
      - "奴籍仍屬白御行。"
      - "春梅表示官面流程可能需白御行補主人確認；白御行已明示讓她去找春梅處理，原則上同意其自主申請。"
    expected_timing:
      - "春梅判斷若資料齊全，行政流程數日內可完成；未固定精確日期。"

  legal_state_now:
    - "目前仍是申請中，不得提前寫成已入妓籍。"

OTHER_FOUR_GUARDS_REGISTRY:
  bai_hongling: "仍在考慮／未申請"
  bai_mingfan: "目前不要"
  bai_xi: "目前不要"
```

---

# 15｜四大金剛第二夜：女客身份與男人用途重新釐清

```yaml
FOUR_GUARDS_LIU12:
  daytime_discussion:
    key_correction_from_bai:
      - "白御行要她們在青樓挑男人，不是叫她們在青樓找真愛／選丈夫。"
      - "觀止內可挑的是自己看得順眼、守規矩、能滿足性需求的成年男人。"
      - "真正長期感情／婚姻若日後發生，另行計算，不以青樓場合預設。"
      - "男女都不應把青樓交易、幾次陪伴或性關係預設成真愛。"

  tonight_guest_decisions:
    bai_hongling:
      attends_as_guest: true
      purpose:
        - "以普通女客身分進大堂，若遇到她自己看得順眼、守規矩且有性吸引力的男人，可自行決定是否往下發展。"
    bai_sanshierniang:
      attends_as_guest: true
      purpose:
        - "同上；即使妓籍申請中，今晚仍按尚未正式登記之普通女客身分活動，不掛牌、不向男人收接客錢。"
    bai_mingfan:
      attends_as_guest: false
      reason:
        - "本人今晚沒有性需求到需要特地挑男人。"
    bai_xi:
      attends_as_guest: false
      reason:
        - "本人今晚不想。"

  tonight_observed:
    - "紅伶、三十二娘打扮後以女客身分進場。"
    - "白御行匿名坐在後方普通席，曾向附近男客煽風點火，鼓勵有興趣者主動去搭話。"
    - "之後有多名男人開始前往二女桌邊搭話／敬酒。"
    - "二女保有自行拒絕、留人、比較與選擇之權。"

  unknown:
    - "二女最後各自選了誰。"
    - "是否有人被她們帶走。"
    - "是否發生私人成人事件。"
    - "不得因多名男人搭話推成二女已接客或已性交。"

  future_household_activity:
    - "四人均同意之後可跟李師師、李瓶兒、浮香、張麗華一起去替白家採購家具／公共生活用品。"
```

---

# 16｜榴月十二日晚：白玉池正式公開代言／會員首夜

```yaml
WHITE_JADE_LIU12_NIGHT:
  yang_endorsement:
    previous_state: "HOT V4.4 時仍待楊玉環本人同意"
    current_state: "CONSENTED_AND_PUBLICLY_EXECUTED"
    confirmed:
      - "楊玉環明示自己確實喜歡白玉池。"
      - "她同意『楊貴妃第一指名』作宣傳。"
      - "她拒絕把原本就能白天免費使用白玉池當成代言費，要求代言費另與潘金蓮談。"
      - "實際代言費數額本輪未公開／未固定。"
      - "榴月十二日晚楊玉環本人在大堂公開表示：觀止未開門這些天，她確實差不多天天去白玉池。"
      - "她本人補充喜歡之處包括地方大、水熱、安靜等使用感受。"

  public_signage:
    - "『楊貴妃第一指名』已正式掛出，不再是待同意候選。"
    - "白玉池規則牌公開：夜間四席、每席一時辰、每次兩名成年客人、需預約、不可轉讓、觀止不提供搭伴。"

  membership_deposit:
    amount: "50兩"
    role: "資格／預約押金，不等於單次使用費"
    per_use_fee: "EXISTS_BUT_EXACT_AMOUNT_STILL_NOT_RECORDED"

  first_night_registration_observed:
    - "至少一名四十來歲布商模樣男客交出五十兩押金並表示另一位是其夫人。"
    - "另有兩名年輕男客以兩人成組方式登記。"
    - "本輪沒有固定他們最終取得哪一時辰，也沒有觀察到實際入池完成。"

  still_unknown:
    - "榴月十二日晚四個外部時段最終完整名單。"
    - "每次實際使用費。"
    - "當晚是否已有第一組實際下池完成。"
```

---

# 17｜白御行匿名普通席：「黑公子」

```yaml
BAI_HEIGONGZI_LIU12:
  intent:
    - "白御行今晚刻意不進包廂，改坐觀止最外圍一兩銀子普通席。"
    - "不帶四大金剛，觀察普通男客眼中的觀止與私下聊天。"

  alias:
    name: "黑公子"
    origin:
      - "白御行以自己衣著主色為黑，臨場給新客姑娘小桃之假稱。"

  knowledge_visibility:
    ordinary_guests:
      - "周圍普通男客未被告知黑公子就是白御行。"
    chunmei:
      - "春梅明顯認得白御行，並配合未揭破。"
    xiaotao:
      - "截至本 HOT，小桃仍不知道黑公子就是白御行。"
      - "她知道黑公子能使用定陶商會票／與商會有某種關聯，但白御行只說自己『在商會有存款』。"
      - "白御行還叫她若不信可以去問白爺；她尚未完成這個查證。"

  male_crowd_intervention:
    - "白御行曾在普通男客桌邊煽動：紅伶／三十二娘作為女客來青樓可能就是想找男人，若有興趣應主動上前。"
    - "此煽動確實提高附近男人上前搭話之數量，但沒有替二女選人或替她們答應。"
```

---

# 18｜小桃：新來觀止姑娘之單線狀態

```yaml
XIAOTAO_ROUTE_PROFILE:
  source: "本輪新出場／只成立於白御行線"
  baseline_writeback: "NO"

  self_identification:
    name: "小桃"
    state:
      - "本人稱剛來觀止沒多久。"
      - "穿掛牌姑娘之服色／以觀止姑娘身分在大堂接觸客人。"

  virginity_and_debut:
    self_report:
      - "本人明示目前仍為處子。"
      - "本人表示潘金蓮仍打算養她日後的出閣／第一次拍賣行情。"
    verification_scope:
      - "本輪沒有由潘金蓮親自核帳確認其處女標的；目前按小桃本人自述保存。"

  brothel_status:
    - "她可主動在大堂評估客人、談酒、談價格。"
    - "其完整妓籍官面文件本輪未專門核對，不得僅由服色補造行政細節。"

  personality_observed_this_night:
    - "願意先看客人是否有趣，不只看座位價位。"
    - "敢直接開價、談不攏就離開；也能把服務內容、價格、預付分開算。"
    - "尚屬新人，成人服務技巧被白御行評價為第一次已足夠，但仍有進步空間。"
```

---

# 19｜黑公子 × 小桃：酒、五百兩撤銷、100兩新交易

```yaml
HEIGONGZI_XIAOTAO_TRANSACTION:
  first_contact:
    - "小桃把白御行當成坐一兩外圍席的新客，主動問能否坐。"
    - "白御行請她喝一小壺梅子酒。"
    - "雙方以『黑公子』『小桃』互稱。"

  initial_private_negotiation:
    topic:
      - "白御行私下提出不買她保留給出閣拍賣的處女第一次，而詢問另一種成人第一次是否可交易。"
    xiaotao_opening_price: "50兩"
    bai_counteroffer: "500兩"

  room:
    - "白御行叫春梅開一間普通客房。"
    - "小桃挽白御行手臂進房；春梅沒有揭穿其身分。"

  500_tael_phase:
    payment:
      - "白御行曾拿出定陶商會500兩票直接交給小桃。"
      - "小桃曾收下，原方案一度口頭成立。"
    renegotiation:
      - "在原方案真正履行前，雙方改談另一項成人服務。"
      - "小桃把原500兩票退回白御行。"
      - "原500兩方案取消，未履行，不得記成小桃已賺500兩或原成人第一次已消耗。"

  final_current_deal:
    total_cash_or_value_transferred_now: "100兩"
    split:
      tonight_service: "50兩"
      next_time_prepaid: "50兩"
    next_time_status: "PREPAID_NOT_YET_FULFILLED"
    scope:
      - "今晚改成一項明確成人口部服務。"
      - "原500兩談判之其他內容不再包含於本次成交。"
```

---

# 20｜小桃今晚成人事件：完成狀態

```yaml
XIAOTAO_ADULT_EVENT_LIU12:
  participants:
    - "白御行"
    - "小桃"

  consent_and_payment:
    - "雙方在進一步事件前重新談清今晚50兩項目，另50兩為下一次預付。"
    - "小桃本人接受最終價格與項目。"

  event:
    status: "COMPLETED"
    hard_fact:
      - "小桃完成今晚談定之成人口部服務。"
      - "白御行在事件後明示評價：以第一次做這項服務而言，水準足夠／不錯。"
    rendering:
      - "SAVE 不保存逐步性技巧與器官細節。"

  skill_feedback:
    - "白御行對小桃提出後續技巧改進方向；小桃接受自己仍可學習，並表示下一次會更進步。"
    - "具體成人技巧只屬私房經驗，不自動轉成跨線人物能力基線。"

  transaction_result:
    tonight_50: "EARNED_AND_COMPLETED"
    next_50: "HELD_AS_PREPAYMENT"
```

---

# 21｜小桃同宿：不是50兩包夜

```yaml
XIAOTAO_OVERNIGHT:
  bai_request:
    - "白御行希望小桃今晚留下陪睡到早上。"

  xiaotao_response:
    - "小桃明確指出今晚50兩只包含已談妥並完成之服務，並不等於50兩包夜。"
    - "她另外自願決定今晚可以留下陪白御行睡到早上。"
    - "她強調這不是50兩價格內包含的義務。"

  current_state:
    consent_to_stay: true
    paid_as_overnight_service: false
    actual_sleep_until_morning: "NOT_YET_COMPLETED_AT_SAVE_POINT"

  accounting:
    - "不得對外寫成『黑公子50兩包小桃一整夜』。"
    - "今晚已實收之成人服務50兩與下一次預付50兩仍各自分軸。"
```

---

# 22｜人物知情矩陣：小桃／黑公子

```yaml
KNOWLEDGE_MATRIX_XIAOTAO:
  xiaotao_knows:
    - "黑公子能拿出定陶商會大額票據／資金。"
    - "黑公子自稱只是在定陶商會有存款。"
    - "黑公子叫她若不信可去問白爺。"
    - "黑公子今晚在一兩外圍席。"

  xiaotao_does_not_know_confirmed:
    - "黑公子就是白御行。"
    - "黑公子就是定陶商會會長。"

  chunmei_knows:
    - "春梅認得白御行，配合開房且未揭穿。"

  ordinary_guests:
    - "附近普通男客只知道『黑公子』成功帶一名姑娘進房，不知其真實身分。"
```

---

# 23｜今夜仍然 OPEN／UNKNOWN

```yaml
OPEN_THREADS_V4_5:
  four_guards:
    - "紅伶、三十二娘今晚最後各自與哪個男人繼續。"
    - "是否帶男人離席／進房／發生私人成人事件。"

  sanshierniang_registry:
    - "主人確認是否已完成紙面程序。"
    - "官府妓籍正式落冊日期。"

  hongling_registry:
    - "仍未決定是否正式申請。"

  rope_master:
    - "牙行是否找到符合條件之高手。"

  new_hongniang_devices:
    - "木馬、手搖機關、三角架、枷鎖舞台是否真正製作。"
    - "任何製作完成／測試／演出都尚未成立。"

  bai_pan_challenge:
    - "正式日期／場地／結果。"

  aliya:
    - "雙人場後其出閣拍賣價格是否實際調整。"
    - "下一次是否再與紅娘演、是否形成固定搭檔。"

  white_jade:
    - "當夜實際四個預約時段名單與使用結果。"
    - "單次使用費。"
    - "楊玉環代言費最終數額。"

  suqing:
    - "榴月十三日起十八日專案工作的每日進度。"
    - "十八日完成後剩餘八日何時正式開始。"

  white_home:
    - "潘金蓮何時正式宣告／落成空間。"
    - "李師師何時帶隊採買家具。"
    - "最終採購金額。"

  xiaotao:
    - "今晚是否真的睡到早上；本 HOT 停在尚未推進天亮。"
    - "下一次50兩預付何時／是否履行。"
    - "她何時發現黑公子＝白御行。"
    - "她自述處子／出閣拍賣狀態何時由潘金蓮帳面正式確認。"
```

---

# 24｜禁止倒灌與接關提醒

```yaml
DO_NOT_AUTO_RESOLVE:
  - "夜生活人物不得又被默認清晨集體早起；觀止主要作息以中午前後醒來為常態。"
  - "李師師月事晚來 != 已懷孕。"
  - "師師拿到1,000兩 != 家具採購已完成。"
  - "錦棠房子 != 白家妻妾房。"
  - "蘇清中午獨自在東後院客房 != 昨夜整夜獨處。"
  - "蘇清商會18日工作 != 白御行私人18日。"
  - "八套戰鬥服樣品 != 八晚成人行為自動同意。"
  - "紅娘五套玩法目前大多只是提案；不得下輪一開始就假設道具已造好。"
  - "繩工搜尋只對外說高度專業繩工／舞台需求，不外洩成人用途。"
  - "潘金蓮同意一場決勝負 != 已發生。"
  - "阿莉婭已是妓籍；不得再寫成『等待重新掛牌／入妓籍才能成人表演』。"
  - "阿莉婭本晚成人雙人場 != 處女拍賣標的已消失。"
  - "三十二娘正在申請妓籍 != 已正式入籍。"
  - "紅伶、三十二娘被多名男人搭話 != 已挑中／已性交。"
  - "楊玉環已同意並完成公開代言；不得回退成『待同意候選』。"
  - "白玉池有人交押金／登記 != 已實際入池完成。"
  - "黑公子500兩原方案已撤銷並退票；不得記成小桃賺了500兩。"
  - "小桃今晚只實收100兩：50兩為今晚已完成項目，50兩為下一次預付。"
  - "小桃願意留宿 != 50兩包含包夜。"
  - "小桃願意留宿至早上 != 本 HOT 時點已經睡到早上。"
  - "小桃尚未確認黑公子就是白御行；不得讓她無來源突然知道。"
  - "成人場景若 Rendering 受限，只處理 Rendering，不得反向改寫人物／事件；V12 分析器應完成最低必要辨認後退場。"
```

---

# 25｜一句接關摘要

> **理火三年榴月十二日從中午推進到晚間。白御行先與李師師談白家新宅：十年租金八千兩既定，未來需預留僕役與後勤擴充，師師將帶李瓶兒、浮香、張麗華與四大金剛採買家具；白御行先交一千兩作訂金資金，尾款交貨後走定陶商會白御行個人帳。蘇清昨夜只確認在東後院小客房醒來、本人稱碰見過一個人但沒有接觀止安排的客；二十八日私約重新鎖成商會二十日＋私人八日，其中先前選人兩日已扣，榴月十三日起由常煒認領剩十八日，做走秀、戰鬥肚兜／內衣、衛生巾等專案。紅娘新增遊街木馬、手搖成人機關、繩吊、三角束縛台、枷鎖真人搭檔五種候選玩法；牙行先只找高度專業繩工，不外洩成人用途。白御行與潘金蓮另立未定日期的一場決勝負成人私約。妓籍制度由 GM 鎖定：官府一旦登記即終身不可回良家；阿莉婭早已是妓籍，只是商業上仍保留處女一次性拍賣標的。她本人確認昨夜沒有使標的失效，今晚與紅娘正式完成一場雙人成人舞台，包含雙向台上互動與親吻，標的仍保留。三十二娘正式由春梅啟動妓籍申請，尚待官面落冊；紅伶仍未申請，明礬與白希不要。今晚紅伶、三十二娘再以普通女客進大堂，目的可包括自主挑選滿足性需求的男人；白御行匿名坐一兩外圍席，以『黑公子』身分煽動附近男客主動搭話，二女最終是否選人仍未知。白玉池今晚正式掛出『楊貴妃第一指名』，楊玉環本人公開承認歇業期間差不多天天洗並表示喜歡；五十兩押金、雙人、四席、一時辰、預約、不可轉讓等規則正式對外，已有至少一名布商與一組兩名年輕男客登記，但實際入池與單次費仍未知。後段，新來姑娘小桃把白御行當成普通黑衣窮客，二人在梅子酒後私下談價；原本五十兩成人第一次被白御行反喊五百兩、入房後五百兩票曾交付，但在履行前雙方重談，小桃退回五百票，改成今晚五十兩成人口部服務＋下一次預付五十兩。今晚五十兩項目已完成，白御行評價其第一次水準足夠；另五十兩尚未履行。小桃仍不知道黑公子就是白御行。白御行要求她留下睡到早上，小桃明示包夜不包含在五十兩內，但她本人自願留下；本 HOT 停在同宿意向成立、尚未推進至天亮。**


<!-- END PROMOTED HOT SOURCE -->
