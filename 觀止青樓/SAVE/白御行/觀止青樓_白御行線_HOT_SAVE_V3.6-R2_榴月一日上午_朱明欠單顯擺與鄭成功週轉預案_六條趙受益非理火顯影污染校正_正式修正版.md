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
