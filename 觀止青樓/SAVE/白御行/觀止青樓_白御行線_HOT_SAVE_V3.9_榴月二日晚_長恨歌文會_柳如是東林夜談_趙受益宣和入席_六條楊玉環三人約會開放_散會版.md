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
