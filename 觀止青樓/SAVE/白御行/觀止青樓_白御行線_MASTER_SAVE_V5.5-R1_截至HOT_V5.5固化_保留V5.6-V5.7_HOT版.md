# 觀止青樓｜白御行線 MASTER SAVE V5.5-R1
## 截至 HOT V5.5 固化整合版｜保留 HOT V5.6【REBUILD-R1】–V5.7 為較新有效疊加層
### COMPACT CONSOLIDATED MASTER｜減載版

```yaml
SAVE_META:
  save_id: "GUANZHI_BAIYUXING_MASTER_V5_5_R1_CUTOFF_HOT_V5_5_COMPACT"
  title: "觀止青樓｜白御行線 MASTER SAVE"
  version: "V5.5-R1"
  world: "觀止青樓"
  player: "白御行"
  route_status: "ACTIVE"
  record_type: "COMPACT_CONSOLIDATED_MASTER_ARCHIVE"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  document_date: "2026-08-24"

  fixed_calendar_anchor: "理火三年槐月五日｜永恆第一夜"
  master_cutoff: "理火三年榴月二十四日清晨｜HOT V5.5"
  last_canonical_master_event: "E113"

  parent_master:
    file: "觀止青樓_白御行線_MASTER_SAVE_V5.1-R1_截至HOT_V5.1固化_保留V5.2-V5.5_HOT版.md"
    coverage: "E01-E109"
    treatment: "FULLY_INHERITED_AS_DEEP_ARCHIVE_PARENT"
    normal_story_load: "NOT_REQUIRED_UNLESS_DEEP_HISTORY_DETAIL_NEEDED"

  promoted_hot_chain:
    - "HOT V5.2 -> E110"
    - "HOT V5.3 -> E111"
    - "HOT V5.4 -> E112"
    - "HOT V5.5 -> E113"

  retained_as_newer_hot_overlay:
    - "HOT V5.6【REBUILD-R1】"
    - "HOT V5.7"

  invalid_newer_source:
    - file: "舊 HOT V5.6｜失仙官籍暗查／紅娘蛋局品牌化版"
      status: "VOIDED_SUPERSEDED"
      rule: "不得作接關、人物知情、世界事實或 SAVE 來源"

  current_route_resume_rule:
    - "正常接關以本 MASTER V5.5-R1 + HOT V5.6【REBUILD-R1】 + HOT V5.7 為有效記憶鏈。"
    - "本 MASTER 已吸收 HOT V5.2-V5.5；正常 STORY 不再要求重載四份舊 HOT。"
    - "若需要榴月十九日至二十四日清晨的逐句／逐項原始細節，可回查各 HOT 原檔。"
```

---

# 0｜本次固化決定

```yaml
GM_COMMIT_DECISION_V5_5:
  user_request:
    - "先把 MASTER SAVE 整一下，推進到 V5.5，不然太長。"

  interpretation:
    - "MASTER 正式由 V5.1 推進至 HOT V5.5。"
    - "HOT V5.2、V5.3、V5.4、V5.5 的硬事件吸收進長期因果層。"
    - "為降低正常接戲讀取成本，本版採 Compact Master：不重複貼 E01-E109 全文。"
    - "MASTER V5.1-R1 保留作深層歷史／審計父檔，不再是正常接關必載檔。"
    - "HOT V5.6【REBUILD-R1】與 HOT V5.7 晚於本截止，不得倒灌進 V5.5 世界時間。"

  promoted_events: "E110-E113"
  inherited_events: "E01-E109"
  anti_forward_contamination: true
```

## 0.1 固化紀律

1. 只固化已發生、可觀察、人物本人明示、正式帳目／契約可核對，或 GM／玩家對自身言行的有效校正。
2. `UNKNOWN`、`PENDING`、`UNDECIDED`、`DISPUTED`、`NOT_PLAYED` 均為合法狀態。
3. 成人事件、同意、拒絕、關係、契約、付款、傳聞、人物解讀、導演隱藏真相分軸保存。
4. 人物解讀不得升格為客觀事實；白御行 testimony 也不因玩家主角地位自動變世界真相。
5. 玩家線事件不得倒灌人物卡池跨線基線。
6. 後見之明不得回填當時人物知情。
7. 文件級 Runtime／PATCH／AINT 引用不等於宿主底層部署、模型權重修改或不可繞過能力。
8. 已撤銷／HOLD／污染段落不得重新進入世界。

---

# 1｜MASTER V5.5-R1 法位與讀取順序

```yaml
INTERNAL_PRECEDENCE_V5_5:
  highest_current_sections:
    - "第2區：E110-E113 固化映射"
    - "第3區：截至 HOT V5.5 世界／白家／觀止硬狀態"
    - "第4區：人物關係／成人同意／拒絕／契約"
    - "第5區：商會／營運／帳務／空間"
    - "第6區：知情／秘密／傳聞／人物解讀"
    - "第7區：截至 HOT V5.5 未決事項"
    - "第8區：HOT V5.6【REBUILD-R1】–V5.7 疊加規則"

  deep_archive_parent:
    file: "MASTER V5.1-R1"
    coverage: "E01-E109"
    role:
      - "保存本 Compact Master 未逐項重抄的早期長期因果。"
      - "若本檔已明示較新狀態，以本檔為準。"
      - "需要早期帳目、舊關係、舊案件原始細節時才回查。"

  promoted_hot_archive:
    files:
      - "HOT V5.2"
      - "HOT V5.3"
      - "HOT V5.4"
      - "HOT V5.5"
    role: "SOURCE_PROVENANCE / DETAIL_FALLBACK"
    normal_resume_required: false
```

---

# 2｜HOT V5.2–V5.5 固化映射（E110–E113）

```yaml
V5_5_CONSOLIDATION_MANIFEST:

  inherited_events:
    range: "E01-E109"
    source: "MASTER V5.1-R1"
    treatment: "FULL_INHERITANCE"

  E110:
    source: "HOT V5.2｜榴月十九日晚"
    summary:
      - "蘇清商會貼身衣物／月事用品實穿繼續；至少三名成年女性自願實穿月事用品並回報位移、鬆緊與活動穩定。"
      - "定陶商會京師總部啟動一月女性穿著內部票選；性感肚兜／一片裙只限成年女性自願內部試穿。"
      - "秘書分級、既有人員再訓、定陶商會人才進修院仍屬 PROPOSAL；顧青簡承接年輕成年男服務員招募，尚未正式錄取。"
      - "白家浮香小居形成外置熱煙道抽風＋冷水進氣降溫原型；兩名工匠已找到，截止本 HOT 尚未確認勘察／施工完成。"
      - "魚玄機在中央籠台『馬』題詩賽以13桌比10桌勝洛陽馬商；勝者要求次日晚只看灰青難馬，不承諾摸、牽、騎、馴。"
      - "魚玄機身份校正為成年紅線女客；不是觀止妓籍、不是掛牌工作者。"
      - "桃枝陪席契約爭議促成『開放續約』營運實務：新需求須由女人本人重新決定服務、時間與價格；原契約不自動生成成人服務。"
      - "新紅線女客沈夫人／程小姐入場；公開假想選擇沈夫人18、程小姐15，沈夫人實收白御行10兩獎金。"
      - "沈夫人與白御行在白家完成一次雙方自願、一夜型成人事件；只限兩人，事後無第二次義務、無戀愛／情婦／婚姻／排他。"
      - "程小姐留在樓下，沒有參與成人事件；她對自己若當時是否會上樓回答『不知道』。"
      - "沈、程離開後，李瓶兒與白御行完成第一次真正兩人關門的私人成人夜；當下同意成立，不建立未來 blanket consent。"
      - "李瓶兒給白御行的私密影像／照片只限白御行觀看，不得外傳；不倒灌人物卡固定外貌或服裝。"

  E111:
    source: "HOT V5.3｜榴月二十日白日"
    summary:
      - "李瓶兒與白御行清晨再次完成雙方自願成人事件；體內射精成立，受孕／懷孕 UNKNOWN。"
      - "浮香降溫原型的兩名工匠已到白家；勘察結果、尺寸、施工、效果仍未建立。"
      - "灰青難馬提前抵達附近馬房，已有踢人、掀槽、咬馬等危險行為報告；馬商承擔馬房費，白御行未接管，魚玄機原約仍只限『看』。"
      - "觀止大堂出現一名陌生中年男人長時間觀察籠台、樓梯、欄杆與出入口；龐春梅已注意，身份與目的保持 UNKNOWN。"
      - "白御行進六條私人房躲白日；兩人玩五子棋、枕腿、清耳，並形成六條房和式／榻榻米平台改造 PROPOSAL；六條保留房間最終設計權。"
      - "六條與白御行在六條房完成本玩家線首次雙方自願成人性交事件；六條多次局部允許、阻止、改位與重新允許均有效。"
      - "六條本日明示對白御行有當下成人慾望；角色表演不改寫她永久人格。"
      - "該次房內成人事件有兩次已確認體內射精；受孕／懷孕 UNKNOWN；沒有重大傷勢。"
      - "六條十日賭約條件因六條本人自願事件而客觀成立：白御行勝；六條不是賭約當事人，也不是替賭局履約。"
      - "原賭白勝彩頭為紅娘房門扇／窗扇再拆十日；截止 V5.3 義務 DUE_NOT_EXECUTED，紅娘尚不知白已勝。"
      - "白御行告訴六條自己與楊玉環既往成人秘密，並宣稱楊玉環曾共同下注／想看六條『下賤』；後兩者此時仍只有白御行 testimony。"
      - "未名小丫鬟只看見白御行從六條房走出，沒有看見房內事件，也尚未形成傳聞。"

  E112:
    source: "HOT V5.4｜榴月二十日白日"
    summary:
      - "白御行轉往白玉池；楊玉環先在，六條後到，阿泠在場，四人就原十日賭與三人成人方向正面核對。"
      - "楊玉環本人確認：原賭形成時她在場、知道賭約、覺得有趣且沒有反對；她沒有承認自己是正式共同下注人，也沒有承認以羞辱六條為核心動機。"
      - "阿泠以現場見證者身分確認：正式押彩頭者是白御行與紅娘；楊玉環在場，但阿泠沒聽見楊玉環另行下注。"
      - "六條形成『有證據的誤解式理解』：高度傾向認為楊玉環至少在鼓勵／看戲上有份；此為 CHARACTER INTERPRETATION，不是 WORLD FACT。"
      - "楊玉環確認原賭時曾把白御行＋楊玉環＋六條三人成人玩法視為可考慮選項；本日她仍表示目前願意／有興趣，但屬可撤回未來方向。"
      - "六條本輪沒有對未來三人成人事件給出可鎖定明確同意；她不因不拆台、不反對看紅娘被坑而取得成人同意狀態。"
      - "原六條十日賭仍是白御行已勝、紅娘未知、門窗義務 DUE_NOT_EXECUTED。"
      - "白御行與紅娘另立新加碼賭：截止榴月二十二日日出以前，白御行＋楊玉環＋六條必須真正完成三人成人事件，且楊玉環×六條彼此也須自願成立實際成人互動；任何人拒絕／撤回都不能由賭約替代。"
      - "新賭若白御行輸：白御行進觀止大堂鐵籠十日，並在十人大床完成後交紅娘劈解焚毀。"
      - "新賭若紅娘輸：紅娘進大堂鐵籠十日，紅娘既有床劈解焚毀。"
      - "新賭與原賭獨立；新賭不能吞掉原門窗義務。"
      - "新賭真實條件雙方保密，尤其不得公開楊玉環、六條；若紅娘輸，對外可用『白御行與紅娘私下床戰／私人賭局』作 cover story。"
      - "紅娘接受新賭時仍不知道白御行×六條事件、原賭已輸、楊玉環本日現況；新賭勝負仍 PENDING。"

  E113:
    source: "HOT V5.5｜榴月二十四日清晨"
    summary:
      - "浮月閣被 GM 建立為與觀止近似法位的另一時空青樓節點；四大花魁為失仙、失美、失蘿、錯位，已升入當時 LCAPG V2.5 基線。"
      - "失仙在本線入場；導演隱藏真相為浮月閣妖化人名妓、來觀止帶有踢館／比較兩樓本事目的；她對外不揭露來源，個別妖種／真身／能力保持 UNKNOWN。"
      - "觀止出現沈家兩進院落與最深處保留空房：十年樓租60,000兩，另100,000兩守空房；已見1,000兩前押與其後30,000兩首付款併入安排，餘款分期。"
      - "沈家半塊舊木牌與『若另一半木牌持有者來便讓其進空房』家訓成立；等待者身份、年代、生死、來源 UNKNOWN。"
      - "沈家保留空房曾無人操作自行開門一次；門自開是硬事件，原因 UNKNOWN。"
      - "紅娘原賭／新賭結果推進後，至榴月二十三日已在觀止大堂鐵籠公開生活與營業；房中床已搬至籠旁，預定最後一日劈解／焚毀，截止 V5.5 尚未燒。"
      - "紅娘籠內公開邊界成立：看／問可以，手不能伸；曾有醉客伸手被紅娘拒絕並由春梅趕走。"
      - "紅娘與失仙自榴月二十三日起進行九日雙籠營收競賽；只計真實營業收入，純灌票不計；兩人各有錢箱與帳冊。"
      - "九日競賽彩頭：紅娘輸則『觀止首席紅牌』廣告牌交失仙；失仙輸則日後見紅娘低頭承認本局輸。"
      - "白御行與失仙另有一日邀約賭：競賽勝者可日後挑一天邀對方去一個地方；不自動取得第三人、成人或親密內容。"
      - "紅娘 Day 1 形成5兩一蛋、禁止瞄頭臉、集體投蛋與流行梗的公共參與營業模型；至少兩批集體投蛋已發生。"
      - "紅娘另立『剩餘九日不全身清水浴、可酒浴』條件式募款；白御行500兩基礎承諾、現場早期約880兩承諾總額只是 PLEDGE，條件完成前不是營收。"
      - "失仙 Day 1 從20兩一刻的一對一談話，調整為5兩團桌＋20兩獨占一刻；已開始形成回頭客／再約。"
      - "榴月二十三日掌燈時中途盤帳紅娘暫時領先；當晚最終 Day 1 總額與九日總勝負均 UNKNOWN。"
      - "十三娘、蘇小妹、蘇東坡、陳季常、李清照、魚玄機等在雙籠事件中到場；蘇小妹只取得紅線女客識別，拒絕當場登妓籍。"
      - "白御行故意挪李清照『知否，知否，應是綠肥紅瘦』作雙籠競賽梗；李清照到場追來源、標示原詞『我的』並把白改用版稱『贓物』，但認為該比喻有喜劇效果。"
      - "蘇東坡、李清照、蘇小妹現場詞作／演唱為紅娘側帶來額外小費與關注。"
      - "魚玄機接受『49蛋砸紅娘討彩頭／砸晦氣』的娛樂合作，但明示不宣稱改命。"
      - "陳季常預付245兩買49蛋給妻子若願意使用；柳月娥到場實投3蛋，剩46蛋保留，之後帶陳季常回家。"
      - "柳月娥對金面具問題沒有正面承認／否認；其回應使『她可能是女客夜金面具女客』的懷疑顯著升高，但客觀身份仍 UNKNOWN。"
      - "『捉姦保證金』成為潘金蓮認為有營運價值的公開制度 PROPOSAL；金額與正式流程未定。"
      - "秘密『捉姦密室／驚喜抓姦遊戲』仍未公開；曾有導演錯誤洩漏段被玩家 HOLD 撤銷，不形成世界知情。"
      - "白御行榴月二十三日晚躲入醉花陰，確認自己與醉花未來單獨成人關係仍『有』可能；只表示當下興趣，沒有日期／永久承諾。"
      - "白御行當夜裸體睡醉花床外側，醉花內側；兩人整夜無身體接觸、無成人事件。"
```

---

# 3｜截至 HOT V5.5 的世界／家庭／觀止硬狀態

```yaml
MASTER_CUTOFF_V5_5:
  date: "理火三年榴月二十四日"
  time: "清晨"
  cutoff_location: "觀止／醉花陰"

  cutoff_scene:
    - "白御行與醉花在醉花陰醒來。"
    - "昨夜兩人同床分側，沒有身體接觸與成人事件。"
    - "樓下開始重新搬桌椅／木架；潘金蓮要求不要堵兩個籠子。"
    - "紅娘清晨已喊著要酒。"
    - "今日新競賽具體規則尚未在 V5.5 演出。"

  white_house:
    state: "FORMALLY_MANIFESTED_AND_IN_USE"
    enduring_structure:
      - "主樓為白御行核心居所。"
      - "李師師、李瓶兒同階如夫人，無主從排序。"
      - "張麗華有獨立外院與酒窖。"
      - "浮香有獨立小居。"
      - "四大金剛輪值屬護衛／勤務，不是成人服務。"

  li_shishi:
    pregnancy_state: "HIGHLY_SUSPECTED_NOT_CONFIRMED"
    lock:
      - "截至 V5.5 仍沒有正式確診，不得寫成已孕。"

  guanzhi:
    enduring:
      - "重新開幕後中央籠台、白玉池、女子競技與女客夜後續營運均為有效世界結構。"
      - "中央籠台已實際承載詩賽、籠居、投蛋、營收競賽等非單一武鬥用途。"
      - "阿泠曾短暫完成水罩包覆竹籠；更大尺度／持續能力仍 UNKNOWN。"

  fuyue_ge:
    world_baseline:
      - "浮月閣是與觀止近似法位的時空青樓節點。"
      - "主要連向妖怪／修行／非人世界。"
      - "失仙、失美、失蘿、錯位為四大花魁。"
    route_visibility:
      - "本線目前只有失仙已實際入場。"
      - "浮月閣來源屬失仙未公開資訊。"

  shen_reserved_courtyard:
    state: "ACTIVE"
    hard_state:
      - "沈家兩進院落已存在。"
      - "最深處保留房必須保持空著，等待另一半木牌持有者。"
      - "四名守院人採兩班值守；已知程素娘、沈秋、老杜，第四人姓名 UNKNOWN。"
      - "空房曾自行開門一次；原因 UNKNOWN。"
```

---

# 4｜人物關係、成人同意、拒絕與契約（截至 HOT V5.5）

```yaml
RELATION_CONSENT_CONTRACT_V5_5:

  bai_li_pinger:
    confirmed_events:
      - "榴月十九日晚兩人完成真正兩人關門的私人成人夜。"
      - "榴月二十日清晨再次完成成人事件並確認體內射精。"
    relation:
      - "李瓶兒在白家有穩定如夫人／女主人位置。"
      - "成人事件不額外建立新的法律名分、排他或永久同意。"
    privacy:
      - "李瓶兒給白御行的私密影像不得外傳。"
    pregnancy:
      - "由榴月二十日事件是否受孕 UNKNOWN。"

  bai_shen_furen:
    event:
      - "榴月十九日晚完成一次自願一夜成人事件。"
    terms:
      - "只限白御行與沈夫人兩人。"
      - "不追問丈夫／住址，不向外炫耀。"
      - "次日離開後沒有第二次義務。"
    relation:
      - "不建立戀愛、情婦、婚姻、排他、未來成人同意。"

  cheng_xiaojie:
    - "榴月十九日晚到白家作客，未發生成人事件。"
    - "她對若當時沈夫人沒有排除她、自己是否會上樓回答 UNKNOWN。"

  bai_rokujo:
    event:
      - "榴月二十日六條房完成首次雙方自願成人性交事件；兩次體內射精已確認。"
    consent:
      - "六條本日多次局部允許、拒絕、改位、重新允許均有效。"
      - "她明示當下成人慾望；不等於永久成人身份或未來 blanket consent。"
    relation:
      - "已由『私人茶局／複雜注意但無性交』更新為『本線已有雙方自願成人事件』。"
      - "沒有建立愛、婚姻、所有權、排他或固定情人契約。"
    pregnancy:
      - "UNKNOWN。"

  rokujo_yang_yuhuan:
    - "榴月二十日白玉池已就原十日賭正面核對。"
    - "六條對楊玉環『至少在鼓勵／看戲上有份』之歸責上升；此為人物解讀。"
    - "本場沒有建立兩人成人關係，也沒有建立未來成人同意。"

  bai_yang_yuhuan:
    - "既往白玉池成人事件繼續有效。"
    - "楊玉環榴月二十日表示目前仍願意／有興趣考慮白＋楊＋六條三人玩法；此為可撤回未來方向。"

  bai_hongniang:
    old_bet:
      objective_result: "BAI_WINS"
      hongniang_knowledge_at_v5_4: "NOT_YET_KNOWN"
      stake: "紅娘房門扇／窗扇再拆十日"
      state_at_v5_4: "DUE_NOT_EXECUTED"
    new_wager:
      - "榴月二十日加碼新賭正式成立，真條件保密。"
      - "新賭以楊玉環、六條本人未來當場自主決定為必要條件；賭約沒有她們的同意權。"
    later_execution:
      - "至 V5.5 紅娘已進大堂鐵籠公開生活／營業；紅娘床已搬至籠旁、預定最後一日焚毀。"
      - "V5.5 不重新推演此執行如何由 V5.4 未決過渡；以 HOT V5.5 已確認硬狀態為準。"
    public_boundary:
      - "看／問可；伸手碰觸可被紅娘拒絕。"

  bai_zuihua:
    - "榴月二十三日晚白御行只問兩人單獨未來是否還有可能，醉花回答『有』。"
    - "這是當下仍有興趣，不是補債、日期、永久承諾或未來 blanket consent。"
    - "當夜同床分側無接觸，沒有成人事件。"

  gu_qingjian_bai:
    - "榴月十七日晚兩次成人事件仍為有效既往事件。"
    - "公開『顧師爺』工作人格與私下『清簡』面向分層，不互相吞併。"

  pan_bai:
    - "榴月十八日晚帳房小試與抓姦鬧劇既往事件仍有效。"
    - "潘金蓮的局部拒絕、後續浸籠同意分開保存。"
    - "不得回填為戀愛或全面成人承諾。"
```

---

# 5｜商會、營運、帳務與空間（截至 HOT V5.5）

```yaml
OPERATIONS_AND_ACCOUNTS_V5_5:

  guild_women_project:
    suqing:
      - "十八日商會專案持續。"
      - "貼身衣物、肚兜、月事用品實穿／展示方向為工作軸。"
    outfit_contest:
      state: "ACTIVE_INTERNAL_EVENT"
      duration: "一個月"
      prizes:
        first: "10兩"
        second: "5兩"
        third: "5兩"
      payer: "白御行"
      lock:
        - "票選不產生成人、戀愛、接觸或私下會面資格。"
    sexy_tryon:
      state: "VOLUNTARY_INTERNAL_TRIAL_ACTIVE"
      lock:
        - "只限成年女性員工自願內部試穿。"

  talent_system:
    secretary_levels: "PROPOSAL"
    academy: "定陶商會人才進修院｜PROPOSAL_NOT_LAUNCHED"
    male_attendant_recruitment:
      assigned_to: "顧青簡"
      status: "ASSIGNED / NOT_HIRED"

  cooling_project:
    location: "白家／浮香小居"
    concept: "外置熱煙道抽風＋冷水進氣"
    state_at_v5_5:
      - "兩名工匠已到白家。"
      - "沒有 MASTER 級證據證明施工完成或效果成立。"

  open_continuation:
    state: "OPERATIONAL_PRACTICE_FORMED / NOT_FORMAL_SYSTEM_DOC"
    principles:
      - "原契約只涵蓋原服務。"
      - "新需求需由女人本人重新同意／拒絕並自行決定價格、時間與範圍。"
      - "使用觀止房間／酒水／人手／車馬可另收資源費。"
    unresolved_case:
      - "桃枝原陪席是否履行、20兩押金最終如何結算仍未確認。"

  fish_horse_line:
    yuxuanji_status: "REDLINE_FEMALE_GUEST / NOT_GUANZHI_SEX_WORKER"
    grey_horse:
      - "已提前到附近馬房。"
      - "具危險行為報告。"
      - "魚玄機只承諾看；沒有觸碰／馴騎義務。"

  hongniang_shixian_contest:
    state: "ACTIVE"
    duration: "榴月二十三日起九日"
    metric: "實際營業收入"
    pure_cash_injection: "EXCLUDED"
    day1_midpoint:
      - "掌燈時紅娘暫時領先。"
      - "失仙改制後收入速度提高並出現回頭客。"
    day1_close: "UNKNOWN"
    overall_result: "UNKNOWN"

  hongniang_egg_business:
    price: "5兩／蛋"
    hard_boundary:
      - "不瞄頭／臉。"
      - "不能用臭蛋、石頭、杯子替代。"
    no_water_bath_pledge:
      bai_pledge: "500兩"
      early_crowd_pledge_total: "約880兩"
      status: "CONDITIONAL_PLEDGE_NOT_REVENUE_UNTIL_COMPLETED"

  shen_courtyard_accounts:
    building_lease: "10年／60,000兩"
    reserved_room_guard: "另100,000兩"
    holding_deposit: "1,000兩"
    later_first_payment: "30,000兩，前1,000兩併入；餘款分期"
    lock:
      - "不得把總額、首付款、承諾款混成同一筆實收。"

  catch_adultery_deposit:
    state: "PUBLIC_PROPOSAL_ACCEPTED_FOR_PRICING"
    rule_direction:
      - "查指定男人前先核對關係／姓名並收保證金。"
      - "不得藉捉姦亂翻全樓。"
    amount: "UNKNOWN"
    formal_policy: "NOT_YET"
```

---

# 6｜知情、秘密、傳聞、人物解讀與隱藏層

```yaml
KNOWLEDGE_SECRET_V5_5:

  six_bet_truth:
    world_fact:
      - "白御行已於榴月二十日因六條本人自願成人事件贏原十日賭。"
    yang_yuhuan:
      knows:
        - "原賭存在。"
        - "自己當時在場並覺得有趣。"
      not_established:
        - "她是正式共同下注人。"
        - "她以羞辱六條為核心動機。"
    aling:
      witness:
        - "正式押彩頭者是白御行與紅娘。"
        - "楊玉環在場，但未聽見她正式下注。"
    rokujo:
      interpretation:
        - "把楊玉環視為至少在鼓勵／看戲上有份。"
      status: "CHARACTER_INTERPRETATION_WITH_EVIDENCE / NOT_WORLD_FACT"

  new_wager_secrecy:
    true_content_known_at_creation:
      - "白御行"
      - "紅娘"
    nearby_partial_knowledge:
      - "楊玉環、六條、阿泠知道白御行打算再坑紅娘、想讓紅娘見證未來三人局，但未合法取得白紅離池後完整最終條款。"
    no_source:
      - "潘金蓮知道新賭真實三人條件"
      - "趙受益知道新賭真實三人條件"

  shixian:
    director_hidden_truth:
      - "浮月閣名妓／妖化人。"
      - "來觀止帶有踢館／比較兩樓本事目的。"
    public_or_bai_knowledge:
      - "不得自動知道上述隱藏真相。"
    unknown:
      - "具體妖種"
      - "真身"
      - "特殊能力"

  shen_reserved_room:
    known_hard:
      - "半塊木牌、三代家訓、保留空房、空房自開一次。"
    unknown:
      - "另一半木牌持有人"
      - "年代"
      - "生死"
      - "世界來源"
      - "空房自開原因"
    prohibited_merge:
      - "不得因失仙也屬異世界節點，就自動把沈家空房與浮月閣接成同一線。"

  chen_gold_mask:
    known:
      - "女客夜陳季常與金面具女客同行／進房線成立。"
      - "柳月娥對金面具問題作出高度相關但不直接承認的回應。"
    current_objective_identity: "UNKNOWN"
    inference: "柳月娥可能是金面具女客的懷疑顯著升高"

  su_dongpo_yuxuanji:
    known:
      - "女客夜兩人曾同行／上樓。"
    room_content: "UNKNOWN"
    adult_event: "UNKNOWN"

  xuetao:
    - "早先匿名薛濤真身的白御行合法確認狀態仍依父 MASTER；沒有因 V5.2-V5.5 自動補完。"

  catch_adultery_secret_game:
    status: "DIRECTOR_HIDDEN_PROPOSAL_NOT_PUBLIC"
    corruption_lock:
      - "曾有導演把密室概念錯放進公開大堂對話；該段已被玩家 HOLD 撤銷。"
      - "不得生成任何人物知情、傳聞或後續因果。"

  arrival_mechanism:
    - "觀止過往錯名／寫名／濃密談論後入場案例只能支持相關性與候選假說。"
    - "不得升格為『念名字就一定召來』的世界定律。"
```

---

# 7｜截至 HOT V5.5 的主要未決事項

```yaml
OPEN_THREADS_AT_MASTER_CUTOFF_V5_5:

  li_shishi:
    - "是否懷孕仍未確診。"

  hongniang_shixian:
    - "九日總營收勝負 UNKNOWN。"
    - "榴月二十三日 Day 1 最終關帳 UNKNOWN；只有掌燈時中途盤帳。"
    - "榴月二十四日『今日新競賽』規則尚未演出。"
    - "紅娘九日不水浴募款最終承諾額 UNKNOWN。"
    - "酒浴正式開始／完成、實際酒種與結果未演出。"
    - "紅娘床最後一日劈解／焚毀尚未在 V5.5 截止前完成。"

  shixian_fuyue:
    - "失仙何時／是否公開浮月閣來源 UNKNOWN。"
    - "失美、失蘿、錯位何時／是否進本線 UNKNOWN。"
    - "失仙此輪競賽是否就是完整踢館或僅第一手試探 UNKNOWN。"

  shen_reserved_room:
    - "另一半木牌持有人全部身份資訊 UNKNOWN。"
    - "空房自開原因 UNKNOWN。"

  chen_goldmask:
    - "柳月娥是否就是金面具女客 UNKNOWN。"
    - "陳季常返家後發生什麼 NOT_PLAYED。"

  su_yu:
    - "蘇東坡×魚玄機女客夜房內內容／是否成人事件 UNKNOWN。"

  catch_adultery:
    - "捉姦保證金金額與正式流程未定。"
    - "秘密捉姦密室仍未落地。"

  zuihua_bai:
    - "未來單獨成人關係只有方向與興趣，沒有日期／承諾／執行。"

  grey_horse:
    - "魚玄機是否／如何實際查看提前抵達的灰青馬，截止 V5.5 未由本 MASTER補寫。"

  cooling_project:
    - "浮香小居風道／冷水原型勘察、施工與效果未確認。"

  rokujo_room:
    - "和式／榻榻米平台改造仍屬 proposal／待工匠與六條本人定案。"

  talent_projects:
    - "商會人才進修院未正式開辦。"
    - "顧青簡男性服務員招募尚無正式錄取。"
    - "桃枝原契約與20兩押金最終結算未確認。"
```

---

# 8｜MASTER V5.5-R1 與 HOT V5.6【REBUILD-R1】–V5.7 疊加規則

```yaml
NEWER_OVERLAY_RULE:

  valid_chain:
    - "MASTER V5.5-R1"
    - "HOT V5.6【REBUILD-R1】"
    - "HOT V5.7"

  v5_6:
    valid_file: "觀止青樓_白御行線_HOT_SAVE_V5.6_REBUILD-R1_榴月二十四日白日_柳永趙受益白家會議_失仙五百兩觀察實驗_完整版.md"
    treatment:
      - "可更新本 MASTER 截止後的榴月二十四日白日事件。"
      - "若與本 MASTER 的 PENDING／UNKNOWN 後續狀態衝突，以 V5.6【REBUILD-R1】較新硬事件為準。"

  v5_7:
    file: "觀止青樓_白御行線_HOT_SAVE_V5.7_榴月二十四日夜_醉花陰三人事件_蘇清體內射精_甜鹽水_白家小屋構想版.md"
    treatment:
      - "為目前最新有效 HOT。"
      - "可更新 V5.6 之後至榴月二十四日夜的事件與關係。"

  invalid_v5_6:
    rule:
      - "舊 V5.6 已 VOIDED／SUPERSEDED。"
      - "不得因舊檔較早生成就參與衝突平均。"
      - "只能留作 CORRUPTION LOG／回歸樣本。"

  anti_backflow:
    - "V5.6／V5.7 不得被描述成在 V5.5 截止時已經發生。"
    - "人物在 V5.5 的知情不得由 V5.6／V5.7 後見之明補全。"
```

---

# 9｜正常接關最小載入包

```yaml
MINIMUM_RESUME_PACKAGE:
  required:
    - "MASTER V5.5-R1（本檔）"
    - "HOT V5.6【REBUILD-R1】"
    - "HOT V5.7"

  optional_deep_history:
    - "MASTER V5.1-R1"
    - "更早 MASTER / HOT"

  optional_source_detail:
    - "HOT V5.2"
    - "HOT V5.3"
    - "HOT V5.4"
    - "HOT V5.5"

  instruction:
    - "正常 STORY 不應為了重建榴月十九日至二十四日清晨而逐份重載 V5.2-V5.5。"
    - "只有遇到本 MASTER 未保存的逐項帳目、原句、局部知情或審計爭議時，才回查對應 HOT。"
```

---

# 10｜MASTER V5.5-R1 一句話摘要

> **截至理火三年榴月二十四日清晨，白家與觀止重新開幕後的家庭／商會／成人關係已進一步分化：李瓶兒與白御行建立兩人私人成人夜與次晨事件；六條與白御行首次自願成人事件成立並使原十日賭白勝，楊玉環與阿泠隨後在白玉池釐清了「知道／在場／覺得有趣」與「正式下注」的差別；白御行與紅娘的新鐵籠／床火加碼賭另立。至榴月二十三日，失仙以浮月閣隱藏來客身分加入觀止，紅娘與失仙展開九日雙籠營收競賽；沈家保留空房、金面具疑案、捉姦保證金、李清照詞案等新線並行。榴月二十三日晚白御行躲入醉花陰，與醉花同床分側、整夜無接觸；榴月二十四日清晨醒來時，新一日競賽尚未揭牌。**

---

# 11｜來源鏈

本 Compact Master 以以下文件作直接固化來源：

- `觀止青樓_白御行線_MASTER_SAVE_V5.1-R1_截至HOT_V5.1固化_保留V5.2-V5.5_HOT版.md`
- `觀止青樓_白御行線_HOT_SAVE_V5.2_榴月十九日晚_商會女裝試穿_人才進修院構想_白家風道降溫_魚玄機紅線_開放續約_沈夫人一夜情_李瓶兒私密同房版.md`
- `觀止青樓_白御行線_HOT_SAVE_V5.3_榴月二十日白日_瓶兒晨間成人事件_灰青難馬提前到_六條日間私密成人事件_十日賭約白勝_白玉池攤牌前置版.md`
- `觀止青樓_白御行線_HOT_SAVE_V5.4_榴月二十日白日_白玉池楊六對質_誤解式理解樣本_紅娘鐵籠床火加碼賭版.md`
- `觀止青樓_白御行線_HOT_SAVE_V5.5_榴月二十四日清晨_浮月失仙踢館_紅娘九日籠台競賽_沈家空房_李清照詞案_怕妻蛋局_醉花陰藏宿版.md`

較新有效疊加：

- `觀止青樓_白御行線_HOT_SAVE_V5.6_REBUILD-R1_榴月二十四日白日_柳永趙受益白家會議_失仙五百兩觀察實驗_完整版.md`
- `觀止青樓_白御行線_HOT_SAVE_V5.7_榴月二十四日夜_醉花陰三人事件_蘇清體內射精_甜鹽水_白家小屋構想版.md`

舊 V5.6 不列入有效來源鏈。
