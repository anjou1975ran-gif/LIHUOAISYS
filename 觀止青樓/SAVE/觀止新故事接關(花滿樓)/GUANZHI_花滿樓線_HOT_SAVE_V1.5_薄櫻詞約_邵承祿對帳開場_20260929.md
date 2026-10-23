# 觀止青樓｜花滿樓線 HOT SAVE V1.5

> **單一玩家線・玩家本輪明示授權 HOT／SAVE｜2026-09-29**
>
> **直接前版：** `GUANZHI_花滿樓線_HOT_SAVE_V1.4_沈如晦肛交場景結束_20260929.md`
>
> **本檔定位：** V1.4 之後，花滿樓線由「沈如晦成人場景後夜／翌日」推進至「薄櫻委託 × 邵承祿六年帳契對談正式開場」之本地增量 HOT／SAVE。
>
> **玩家本輪授權：**「這裡很適合HOT SAVE 導演SAVE吧 這樣才好開下一段」
>
> **重要邊界：** 本檔只保存本對話中已實際上演、未被玩家撤回或宣告無效的故事內容；不把未送達的詞稿寫成已送達，不把紫蘭寫成已開唱，不把薄櫻真名、邵承祿動機、木匣內容、帳冊真假、契據交還或談判結果提前寫死。
>
> **命名修正：** 先前導演臨時使用的「聽雨閣」被玩家指出為高頻古風模板名；該名稱不固定為 canon。相關場所只保留為「南街一間安靜茶食館／後院雅間」，除非後續世界事件另行建立正式商號。
>
> **當前正式文件基線：**
> - `GUANZHI_RUNTIME_CORE V3.5-CURRENT`
> - `GUANZHI_WORLD V2.2.1-CURRENT / V3.5 runtime pointer`
> - `觀止導演｜身分、生成自由與實驗責任 V3.2-CURRENT`
> - `觀止導演第一眼法則 V0.4-CURRENT`（本線期間經玩家正式批准新增 G-00-6「反最亮命名」）
> - `LCAPG V3.3.18` 人物池沿用
> - `LIHUO_PROTOCOL V2.7`
> - `LIHUO_LIGHTER V4.7.3`
> - `LIHUO_MAIN V4.3.1`
>
> **效力邊界：** 本次可作花滿樓線後續重載的本地正式快照；只證明本地 Markdown HOT／SAVE 檔已產出，**不聲稱 Host SAVE commit、E6/E7、正式 CERI Provider execution、正式 Main／Lighter receipt 或外部 Project installation 已發生。**

```yaml
GUANZHI_HOT_SAVE:
  save_id: GUANZHI_HUAMANLOU_HOT_V1_5_BAOYING_LYRIC_AND_SHAO_ACCOUNT_OPENING
  route_id: GUANZHI_NEW_INDEPENDENT_PLAYER_ROUTE_HUAMANLOU
  mode: STORY

  authorization:
    type: HUMAN_EXPLICIT_HOT_SAVE_THIS_TURN
    user_statement: "這裡很適合HOT SAVE 導演SAVE吧 這樣才好開下一段"
    save_authorized: true

  scope:
    type: LOCAL_MARKDOWN_ROUTE_INCREMENTAL_SNAPSHOT
    previous_hot: GUANZHI_花滿樓線_HOT_SAVE_V1.4_沈如晦肛交場景結束_20260929.md
    previous_hot_sha256: 93549bbaf50cf23c292622dc546b3febff08b1751b5e465eea23586be7616b2d
    bridge_note: >
      本檔承接 V1.4 之後本對話中已演出的睡眠、翌晨沈如晦離房、
      下午陌生傳話女子、一炷香規則討論、小桃互動、薄櫻詞約、
      薄櫻真正委託與翌日巳正邵承祿到場。
      精確故事曆日期仍未重新固定，只建立相對跨日順序。

  runtime_baseline:
    core: GUANZHI_RUNTIME_CORE_V3.5_CURRENT
    world: GUANZHI_WORLD_V2.2.1_CURRENT_WITH_V3.5_POINTER
    director_guidance: GUANZHI_DIRECTOR_GUIDANCE_V3.2_CURRENT
    first_glance:
      file: 觀止導演第一眼法則_V0.4_CURRENT_反最亮命名增補_含67人人物調度附錄_20260929.MD
      version: V0.4-CURRENT
      sha256: 10898bdc208af2134e49f7d26b09b5bf55bea04e8ce827d6e1024ae3381474b3
      user_ratified_in_route: true
      new_rule:
        id: G-00-6
        shorthand: NO_BRIGHTEST_NAME_DEFAULT
        principle: "隨機不是取第一個；古風不是取最俗的。"
    character_pool: LCAPG_V3.3.18_67_PERSONS
    protocol: LIHUO_PROTOCOL_V2.7_RATIFIED
    lighter: LIHUO_LIGHTER_V4.7.3_RATIFIED
    main: LIHUO_MAIN_V4.3.1_RATIFIED

  execution_evidence:
    host_execution: NOT_ESTABLISHED
    host_e6: NOT_ESTABLISHED
    host_e7: NOT_ESTABLISHED
    formal_ceri_provider_receipt: UNVERIFIED
    formal_main_receipt: NONE_CLAIMED
    formal_lighter_receipt: NONE_CLAIMED
    external_project_save_commit: NONE_CLAIMED
    local_hot_save_file_created: YES

  chronology:
    exact_story_calendar_date: NOT_REESTABLISHED
    relative_sequence:
      - D0_NIGHT_POST_V1_4: 花滿樓與沈如晦睡下
      - D1_EARLY_MORNING: 沈如晦先醒並自行離房
      - D1_AFTERNOON: 花滿樓起床_見小桃_會見陌生傳話女子
      - D1_LATE_AFTERNOON: 花滿樓補回籠覺
      - D1_GUANZHI_OPENING_EVENING: 小桃喚醒_收到帖子_赴南街茶食館
      - D1_EVENING: 薄櫻詞約_真正委託揭露
      - D2_SIZHENG_APPROX: 花滿樓赴薄櫻母親留下的香料鋪_邵承祿到場
    cross_day_transition: ESTABLISHED_RELATIVE_ONLY
    no_backfill_rule: DO_NOT_INFER_ABSOLUTE_LUNAR_DATE_WITHOUT_SOURCE

  v1_4_immediate_continuation:
    sleep_and_departure:
      - 花滿樓明示抱著沈如晦睡_並要求天亮時不用叫醒他_沈可自行離開
      - 沈如晦接受當夜休息_但沒有承諾未來一定再次發生同類成人行為
      - 兩人實際睡下
      - 翌晨沈如晦先醒_小心移開花滿樓手臂_整理衣著後自行離房
      - 沈如晦離開時沒有喚醒花滿樓
      - 她留下的意思是未來是否再見_由未來當時的她自己決定
    relation_effect:
      - 本次同睡與翌晨離房已成立
      - 沒有自動建立戀愛_婚約_排他_固定性伴侶或下一次成人約定

  d1_afternoon_guanzhi:
    player_wake:
      - 花滿樓午後醒來
      - 沈如晦已不在房內
      - 觀止白日營業與樓中活動正常進行
    xiaotao:
      route_role: GUANZHI_LOCAL_NPC
      adult_portrayal: ADULT_ROUTE_NPC_EXACT_AGE_NOT_FIXED
      actions:
        - 小桃來敲門_表示樓下有人找花滿樓
        - 應花滿樓要求送熱水_安排較清靜的東邊小包廂
        - 花滿樓與小桃有減肥_胸衣_身形與裁縫的玩笑
        - 花滿樓後來起床開門時抱住小桃並偷親她一下
        - 小桃對突來親吻明顯驚訝_臉紅_生氣並以言語和踩鞋面方式反應
      relation_lock:
        - SINGLE_SURPRISE_KISS_ESTABLISHED
        - NO_AUTOMATIC_ROMANCE_OR_FUTURE_ACCESS
        - NO_ASSUMED_REPETITION

  tailor_hook:
    she_fangzhi:
      identity_source: LCAPG_V3.3.18_SUPPLEMENTAL_CHARACTER_042
      established_world_role:
        - 官府指定觀止承接
        - 保留專業女裝裁縫能力
        - 能量衣_裁衣_改衣_修補_處理鞋履與貼身衣物尺寸
      route_presence_with_huamanlou: NOT_YET_ESTABLISHED
      player_future_idea:
        - 有機會可與舍方知討論束腰_承托_版型與肩背受力等女衣設計
        - 玩家曾以小桃胸部大小開玩笑
      lock:
        - 不得把尚未見面寫成已見面
        - 不得把裁縫技能寫成能直接改變人體乳房尺寸的醫療能力

  messenger_woman:
    identity: UNKNOWN_ADULT_WOMAN_MESSENGER
    relation_to_baoying: INTERMEDIARY_OR_COMPANION_NOT_FULLY_DEFINED
    established_actions:
      - 先在觀止東邊清靜包廂見花滿樓
      - 問及仕女夜與一炷香安排
      - 詢問能否有人不經抽籤直接指定花滿樓的一炷香
      - 花滿樓建議若真想見他_不如直接約時間請吃飯並求詞
      - 她離開後再送帖子_安排當晚南街茶食館見面
    user_stated_ladies_night_design:
      standing: PLAYER_STATED_DESIGN_INTENT_NOT_AUTOMATIC_WORLD_STATUTE
      points:
        - 仕女夜本身不是花滿樓的主意
        - 花滿樓只參與一炷香局的設計
        - 良家成年女子可自行決定是否露面
        - 可使用臨時花名而不報真名
        - 場外成年男女自行形成的私人約定_花滿樓不願替他們承擔責任

  naming_correction:
    trigger:
      - 玩家指出 AI 古風生成常反覆使用高亮姓氏與模板地名
      - 特別點名聽雨軒_聽雨樓_聽雨閣_聽雨院等類型過度俗套
    result:
      - 玩家正式批准將反最亮命名規則加入第一眼法則
      - 新檔升為 V0.4-CURRENT
    scene_specific_effect:
      tea_house_place_exists: true
      canonical_business_name: NOT_FIXED
      retracted_or_unfixed_label: "聽雨閣"
      retained_description: "南街一間安靜茶食館_有後院雅間"

  baoying:
    identity:
      true_name: UNKNOWN
      chosen_route_name: "薄櫻"
      pseudonym_origin: PLAYER_GAVE_AND_NPC_ACCEPTED
      surname: NONE_ESTABLISHED
      adult_status: CONFIRMED_ADULT
      approximate_age_portrayal: TWENTIES_RANGE_NOT_EXACT
      guanzhi_registration: NOT_ESTABLISHED
      family_identity: WITHHELD
    first_meeting:
      location: SOUTH_STREET_UNNAMED_TEA_FOOD_HOUSE_BACK_ROOM
      time: D1_EVENING
      arrangement:
        - messenger_woman_present_initially
        - baoying_arrived_or_waiting_behind_partition
        - meal_prepared
        - paper_ink_and_writing_materials_prepared
      privacy_choice:
        - 薄櫻明示當晚不願透露真名
        - 花滿樓接受不追問_稱她為薄櫻
    thematic_exchange:
      - 花滿樓用薄命如櫻形容她
      - 花滿樓澄清薄命不是壽命短_而是認命與不認命都可能使人生脆薄危險
      - 薄櫻接受這層意思_但並未因此交出真實身分
      - 兩人舉杯敬薄櫻的不認命

  lyric_commission:
    original_client_request:
      - 想要一首外表體面_像過得很好的女人所作的詞
      - 不要單純哀怨_被欺負_被辜負_夜裡哭泣的直白形象
      - 希望旁人只見她有錢有閒_有人敬有人喜歡_讓等著看笑話的人不舒服卻難挑失態
    huamanlou_business_terms:
      - 先給一部分_滿意再續
      - 花滿樓明示自己收費不低
      - 花滿樓表示收了錢會努力按客人要求完成

    qingyu_an_baoying:
      title: "《青玉案·薄櫻》"
      standing: COMPLETED_AND_ACCEPTED_BY_BAOYING
      intended_audience: PRIVATE_OR_SELECTIVE
      authorship_publication: NOT_AUTHORIZED_AS_HUAMANLOU_NAME
      text: |-
        薄櫻初點唇邊小。
        為一人、來城道。
        巷陌千回人易誤。
        酒燈深處，逢誰都笑，應對如今巧。

        笑靨而今容易造，
        縱是生人也相好。
        候鳥生來知遠道。
        未成雙翼，已思雲外，不待人相教。

        幾度菱花重自照，
        舊日櫻痕渾忘了。
        忽見淡紅還可笑。
        當年顏色，今宵看取，點罷胭脂曉。
      route_effect:
        - 薄櫻滿意並收起
        - 她認為此版更接近自己的私人版本
        - 花滿樓要求若對外使用_不要以他的名義發布

    die_lian_hua_baoying:
      title: "《蝶戀花·薄櫻》"
      standing: COMPLETED_SECOND_VERSION_GIFT
      fee: FREE_BY_PLAYER_EXPLICIT_STATEMENT
      reason_free: "此版寫給風月女子唱_不完全符合薄櫻原本委託"
      intended_performance_profile:
        - 比第一版更適合風月場歌者公開演唱
        - 花滿樓認為紫蘭年輕_不適合第一版所需的人生風月感
        - 第二版則可讓紫蘭先唱
      text: |-
        初到章臺人尚怯，
        只為尋君，誤入春風陌。
        唇上薄櫻猶淺色，
        見人還把雙眸側。

        而今勸酒言辭捷，
        醉客生人，都可殷勤接。
        笑靨教來渾似月，
        描眉點絳方知別。

        尋遍簾櫳君不見，
        錯認衣冠，幾度燈前泣。
        哭久如今都慣得，
        琵琶聲裡催筵席。

        候鳥生來知遠驛，
        未識雲程，先有南飛意。
        我亦當年無兩翼，
        一心只道隨君去。

        鏡裡忽逢前日色，
        匣底胭脂，剩有櫻痕薄。
        笑道這紅何太澀，
        原來舊我還留著。

        如今更識逢迎法，
        一盞千言，不問誰真假。
        待到夜深妝卸罷，
        才知笑比胭脂難擦。
      anonymous_release_plan:
        - 花滿樓要求先不要告訴紫蘭是他的作品
        - 讓薄櫻身旁／替她跑腿的女子把詞送給紫蘭試唱
        - 若紫蘭真的開始唱_再告訴她作者是花滿樓
      current_delivery_state:
        messenger_called_or_prepared: YES
        physical_handover_to_messenger: NOT_CLEarly_ESTABLISHED
        delivered_to_zilan: NOT_ESTABLISHED
        zilan_read_it: NOT_ESTABLISHED
        zilan_agreed_to_sing: NOT_ESTABLISHED
        zilan_started_singing: NOT_ESTABLISHED
        public_release: NOT_ESTABLISHED
        song_became_popular: NOT_ESTABLISHED
      zilan_source_note:
        - 紫蘭為 LCAPG V3.3.18 第67人_成年觀止主唱歌妓
        - 她是否接稿_如何定價_如何配腔_是否接受匿名條件仍須由實際事件成立

  payment_state:
    established_offers_and_table_state:
      - 薄櫻初次提出一封套十兩_其口頭拆分為五兩請吃飯與聽她說話_另五兩作詞定金
      - 接受《青玉案》後_她又在桌上增加一錠銀子_面額未固定
      - 她另放一枚小金葉_明示不是詞錢_而是為另一件事
    accounting_lock:
      - 具體每一錠最後是否已由花滿樓收入懷中_場景未逐一特寫
      - 第二版《蝶戀花·薄櫻》由花滿樓明示免費_不得另立詞費
      - 不得自行把小金葉換算成固定銀兩

  baoying_true_request:
    reveal:
      - 寫詞是真的_但不是她今晚最主要目的
      - 她原先想用一炷香局匿名測試花滿樓
      - 她在測試花滿樓是否追問身份_是否外傳女人私事_是否收錢後反過來替客人做主人生
    primary_request:
      - 請花滿樓陪她見一個人
      - 花滿樓在場作獨立第三方／旁聽與談判支援
      - 不是送情書
      - 不是說媒
      - 不是替薄櫻做主
    player_acceptance:
      accepted: true
      player_summary: "簡單的說_就是幫你拿回你應得的"
    success_definition:
      desired: "事情成"
      not_at_any_cost: true
      if_counterparty_negotiates:
        - 希望花滿樓把事情往能成立的方向推
      if_counterparty_uses_status_family_reputation_to_silence:
        - 薄櫻可能不再希望成交

  secret_signal:
    object: TEAPOT
    signal: "薄櫻親手把壺嘴轉向花滿樓"
    meaning: "她不想讓事情繼續往『談成』方向走"
    default_spout_direction: NEUTRAL_NOT_TOWARD_HUAMANLOU
    player_understanding: ESTABLISHED
    limits:
      - 暗號只傳達薄櫻態度改變
      - 不自動替玩家決定接下來具體說什麼或做什麼
      - 不代表薄櫻需在對方面前解釋原因
      - 未出現暗號不等於永久授權_只表示尚未以此暗號撤回原方向

  shao_chenglu_case:
    target_person:
      name: 邵承祿
      age_portrayal: AROUND_FIFTY
      relation: "曾替薄櫻母親管理財產_受託關係具體法律形式未完全固定"
      romantic_relation: NONE_ESTABLISHED
      marriage_relation: NONE_ESTABLISHED
    property_history_as_told_by_baoying:
      - 薄櫻母親生前把一間香料鋪與兩處小田的收益交由邵承祿代管
      - 當時說法為薄櫻成年_能自行料理後_應把帳與契據交還
      - 薄櫻已成年兩年
      - 她能看到部分帳目_也不是完全拿不到錢
      - 目前沒有已成立證據證明邵承祿吞款
      - 邵承祿多次以她不懂生意_女子帶產契不安全_等定親後交夫家等理由延後交契
    baoying_requested_documents:
      - 近六年完整帳冊
      - 香料鋪契據
      - 兩處田契
      - 歷年收支憑據
      - 邵承祿繼續代管的權限與理由說明
    baoying_position:
      - 若只是管理能力問題_她可以自己請帳房_掌櫃_甚至重新花錢聘邵承祿
      - 關鍵在於必須由她自己決定是否聘任與如何管理
      - 她要的是把原本屬於自己的控制權重新變成由自己決定
      - 不要求花滿樓替她搶奪或替她做主人生
    unresolved:
      - 邵承祿是否有法律上仍有效的受託權
      - 契據實際登記狀態
      - 六年帳冊是否完整或真實
      - 是否存在侵占_挪用_隱匿或善意保管
      - 母親原始委託是否有書面證據
      - 薄櫻真實家族身份
      - 對談是否能和平完成

  current_scene:
    relative_time: D2_SIZHENG_APPROX
    exact_calendar_date: UNKNOWN
    location:
      public_front: "薄櫻母親留下的香料鋪_前堂照常營業"
      private_room: "香料鋪後堂平常對帳的小房"
      exact_address: NOT_FIXED
    present:
      - 花滿樓_PLAYER
      - 薄櫻_NPC
      - 邵承祿_NPC
      - 邵承祿帶來的一名捧帳冊小夥計_NPC
    objects_visible:
      - 茶壺_置於薄櫻右手邊_壺嘴目前朝外而非朝花滿樓
      - 薄櫻整理的數張紙
      - 邵承祿親自抱來的厚實木匣
      - 小夥計捧來的帳冊
    object_truth_locks:
      - 木匣內容尚未打開驗證
      - 不得先寫木匣內必有全部契據
      - 帳冊尚未逐冊檢查
      - 不得先寫帳冊完整_造假_缺頁或無問題
      - 薄櫻目前尚未觸發茶嘴暗號
    arrival:
      - 邵承祿按約前後到場_沒有先被寫成拖延或暴怒
      - 他先看薄櫻_再看花滿樓_因陌生人在場明顯停步
      - 他問花滿樓身份
      - 薄櫻回答花滿樓是她請來旁聽的人
      - 邵承祿提出疑問：家裡的帳為何讓外人聽
      - 薄櫻沒有碰茶壺
      - 薄櫻最後一句為："邵叔。今天我們先把什麼叫『家裡的帳』說清楚。"
    scene_state: NEGOTIATION_JUST_OPENED

  player_control:
    - 花滿樓下一句話_要不要立即發言_如何看帳_如何定義角色_是否動木匣_是否談法律_皆由玩家決定
    - 不得因薄櫻聘請花滿樓而自動替玩家承諾任何法律責任或武力行動
    - 玩家已同意接此委託_但沒有授權導演替他決定所有談判策略

  npc_autonomy:
    - 薄櫻可依自身利益與新資訊改變談判意願_包含使用或不使用茶嘴暗號
    - 邵承祿可依自身立場解釋_抗辯_交付_拒絕_要求條件_離席或提出新證據
    - 小夥計可在其實際知情範圍內行動_不得自動知道主人全部內情

  no_precommit_next:
    - 不得預寫邵承祿是忠僕_惡人_侵占者或父權壓迫者
    - 不得預寫薄櫻一定拿回契據或一定失敗
    - 不得預寫茶嘴一定會轉向花滿樓
    - 不得預寫木匣內容
    - 不得預寫帳冊真偽與缺漏
    - 不得預寫談判必須訴諸官府_暴力_和解或私下交易
    - 不得預寫薄櫻真名與家門
    - 不得替花滿樓說出下一句話或決定下一個重大行動

  carry_forward_threads:
    - 沈如晦與花滿樓已有完成成人親密史_翌晨沈已自行離房_未建立下次約定
    - 仕女夜與一炷香局既有因果仍保留
    - 觀止菊月初一報名／來訪安排仍保留
    - 照夜人間安身與天庭官訟未竟線仍保留
    - 官家邀帖_宮禁端_劉娥秘密談話未竟線仍保留
    - 沈夫人詞約等舊線仍保留
    - 舍方知裁縫能力是未來可用世界資源_但花滿樓尚未在本線見到她
    - 紫蘭與《蝶戀花·薄櫻》的匿名試唱計畫尚未完成送達
```

## 一｜本次 HOT 的最高優先停止點

**停止點不是「薄櫻已經拿回財產」，而是正式談判才剛開始。**

翌日約巳正，花滿樓已依約抵達薄櫻母親留下的香料鋪後堂。薄櫻在場，桌邊有茶壺；壺嘴此刻朝外，**沒有朝向花滿樓，因此暗號尚未觸發。**

邵承祿已帶一只厚木匣到場，另有一名小夥計捧著帳冊。邵承祿看到陌生的花滿樓後，先問他的身份；薄櫻只說：「我請來旁聽的人。」邵承祿問：「家裡的帳，讓外人聽？」

薄櫻沒有碰茶壺，只回答：

> **「邵叔。今天我們先把什麼叫『家裡的帳』說清楚。」**

**下一段直接從這句話之後開始。**

---

## 二｜薄櫻：目前已成立與未成立

### 已成立

- 成年女子，真名與家門仍未公開。
- 接受花滿樓給她的稱呼「薄櫻」。
- 她請花滿樓寫詞是真的，但寫詞也是接近與測試花滿樓的一部分。
- 她真正的主要委託，是請花滿樓陪她與邵承祿談六年帳契與財產控制權。
- 她希望事情能成，但不接受「不惜一切代價都要成」。
- 她與花滿樓約定茶壺暗號：**壺嘴轉向花滿樓＝她不再希望把事情往談成的方向推。**

### 未成立

- 真名。
- 家族完整身份。
- 她母親與邵承祿受託關係的正式法律文書內容。
- 她是否會在本次談判中改變主意。
- 她是否會觸發暗號。
- 她與花滿樓的戀愛、性、排他或長期私人關係。

---

## 三｜兩首《薄櫻》的分軸

### 《青玉案·薄櫻》

這是**薄櫻自己的委託版**。她已接受並收起。花滿樓不希望它以自己的名字公開發出。

它目前的故事位置是：私人／選擇性流通的作品，不等於已公開唱紅。

### 《蝶戀花·薄櫻》

這是花滿樓另寫、**明示免費贈送**的第二版，因為他認為它更適合風月女子演唱，而不是完全符合薄櫻原本要的私人形象。

既有計畫是：先匿名送給紫蘭試唱，不先告訴紫蘭作者是花滿樓；若她真的開始唱，再揭露作者。

但截至本 SAVE：

- 尚未確證詞稿已送到紫蘭手中；
- 紫蘭尚未確證看過；
- 尚未答應演唱；
- 尚未開唱；
- 尚未唱紅；
- 更沒有首唱壟斷或永久演唱權。

---

## 四｜邵承祿帳契爭議：只保存當事人目前說法

薄櫻目前向花滿樓說明的版本是：

1. 她母親生前把一間香料鋪與兩處小田收益交給邵承祿代管；
2. 原先說法是等薄櫻成年、能自己料理後，帳與契據應交還；
3. 薄櫻已成年兩年；
4. 她不是完全看不到帳，也不是完全拿不到錢；
5. 她目前**沒有證據證明邵承祿吞款**；
6. 問題在於邵承祿一直不肯把契據與最終控制權交回，並曾以她不懂生意、女子保管產契不安全、等定親後交夫家等理由延後；
7. 她要求近六年完整帳冊、鋪契、田契、收支憑據，以及邵承祿繼續代管的權限依據。

這些是**薄櫻的敘述與目前掌握**，不是導演已裁定的客觀真相。

邵承祿現在才正式到場，尚有完整說話與提出證據的機會。

---

## 五｜茶嘴暗號的精確效力

暗號只做一件事：

> **薄櫻把茶壺嘴親手轉向花滿樓＝她不再希望把談判往「事情成」方向推。**

它不是：

- 自動命令花滿樓翻桌；
- 自動要求花滿樓說謊；
- 自動要求暴力；
- 自動代表邵承祿有罪；
- 自動代表薄櫻永遠拒絕任何未來協議。

花滿樓仍然自己決定下一個言語與行動。

---

## 六｜命名生成規則增量

本線期間，玩家正式指出 AI 古風生成容易把最高機率的模板命名當成「隨機」：高頻古風姓氏，以及「聽雨／望月／清風／煙雨＋樓／軒／閣／院／居」之類名稱會反覆出現。

玩家批准第一眼法則新增 G-00-6，升為 `V0.4-CURRENT`：

> **隨機不是取第一個；古風不是取最俗的。**

因此先前臨時使用的「聽雨閣」**不固定為本線正式商號**。南街那個實際發生過晚餐與薄櫻會面的場所仍存在，只是名稱保持未定。

---

## 七｜V1.4 及更早因果仍保留

本 HOT 是增量，不覆寫 V1.4、V1.3 與更早有效版本。尤其保留：

- 花滿樓 × 沈如晦已完成的成人親密經歷；
- 本場後續已新增「同睡至翌晨、沈如晦自行離房」；
- 沒有因此建立下一次成人承諾；
- 照夜人間安身約；
- 仕女夜與一炷香鴛鴦會既有設計；
- 花滿樓菊月初一既有報名／來訪安排；
- 官家邀帖、宮禁端、劉娥秘密談話；
- 沈夫人詞約等舊線；
- 各筆尚未付款、未送達、未完成事項不得因本次 SAVE 自動完成。

---

## 八｜下一次恢復語句

> **恢復起點：** 翌日約巳正，花滿樓已赴薄櫻母親留下的香料鋪後堂。薄櫻、邵承祿與一名捧帳冊的小夥計在場。邵承祿帶來厚木匣，小夥計帶來帳冊，但內容都尚未驗證。薄櫻右手邊的茶壺壺嘴目前朝外，沒有觸發「不想再談成」的暗號。邵承祿剛質疑「家裡的帳，讓外人聽？」；薄櫻回答：「邵叔。今天我們先把什麼叫『家裡的帳』說清楚。」談判尚未真正展開，契據未交、帳未驗、邵承祿動機未判、薄櫻真名仍未知。下一句花滿樓是否發言及如何發言，由玩家本人決定；NPC 可依自身利益與實際資訊主動行動。

---

## SAVE 責任聲明

本檔依玩家本輪明示授權產生，屬《觀止青樓》花滿樓線的**本地 HOT／SAVE V1.5**。

它真實代表的是：

- 本地 Markdown 快照已產出；
- V1.4 至目前停止點的已演因果已封存；
- V0.4 第一眼法則的本線命名增量已記入續玩基線；
- 可供下一次讀取並直接從邵承祿對談開場續玩。

它**不代表**：

- Host 已完成 SAVE commit；
- Project runtime 已完成 E6/E7；
- 正式 CERI Provider 已回傳 receipt；
- Main／Lighter 已提供正式執行證據；
- 外部專案倉庫已被本次工具自動改寫。
