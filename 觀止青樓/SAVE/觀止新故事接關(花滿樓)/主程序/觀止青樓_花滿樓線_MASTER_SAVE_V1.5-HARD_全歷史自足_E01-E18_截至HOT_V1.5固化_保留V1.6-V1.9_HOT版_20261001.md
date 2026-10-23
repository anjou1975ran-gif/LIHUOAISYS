# 觀止青樓｜花滿樓線 MASTER SAVE V1.5-HARD
## 第一次主存檔｜全歷史自足｜E01–E18｜截至 HOT V1.5 固化｜保留 HOT V1.6–V1.9 為 post-MASTER overlay
### SAVE MODE COMPILE｜2026-10-01｜STORY FROZEN AT V1.5 CUTOFF

```yaml
MASTER_SAVE_META:
  save_id: GUANZHI_HUAMANLOU_MASTER_V1_5_HARD_E01_E18
  route_id: GUANZHI_NEW_INDEPENDENT_PLAYER_ROUTE_HUAMANLOU
  player: 花滿樓
  version: V1.5-HARD
  memory_generation: V1.5
  record_type: MASTER_SAVE
  format_runtime: GUANZHI_SAVE_RUNTIME_V1_0_COMPATIBLE
  compile_date: 2026-10-01
  first_master_generation: true

  story_cutoff:
    date: 理火三年_菊月初三
    daypart: 巳正前後
    exact_clock: APPROXIMATE_ONLY
    scene: 薄櫻母親留下的香料鋪後堂_邵承祿對帳剛開場
    event_upper_bound: E18
    source_cutoff_hot: HOT_V1.5

  parent_master:
    file: NONE_FIRST_MASTER
    version: NONE
    treatment: FIRST_SELF_CONTAINED_COMPILE

  promoted_hot_chain:
    - HOT V1.0 -> E01-E03
    - HOT V1.1 -> E04-E07
    - HOT V1.2 -> E08-E10
    - HOT V1.3 -> E11-E13
    - HOT V1.4 -> E14-E15
    - HOT V1.5 -> E16-E18

  source_hot_files:
    V1.0:
      file: GUANZHI_花滿樓線_HOT_SAVE_V1.0_桂月十六亥正_20260927.md
      sha256: 5070b482eaae7b37d44e6de99f66e0073db5a31214208a9a56ba9300fced6f8d
    V1.1:
      file: GUANZHI_花滿樓線_HOT_SAVE_V1.1_桂月二十二亥末_20260927.md
      sha256: d6cb4a9a94577fffafb7914ae311a05af691bc2db45680a1c9c061713e03cafa
    V1.2:
      file: GUANZHI_花滿樓線_HOT_SAVE_V1.2_桂月二十五亥正_20260928.md
      sha256: b520eb62482cf6a7844777c6a12761867cf17bdad59ef724f9d74bf0c2c46b69
    V1.3:
      file: GUANZHI_花滿樓線_HOT_SAVE_V1.3_桂月二十五離樓_仕女夜巷_20260928.md
      sha256: 95a63c751f630bb4129d34df26cf25a7ed322f852ce11fae879e43b00aab2c23
    V1.4:
      file: GUANZHI_花滿樓線_HOT_SAVE_V1.4_沈如晦肛交場景結束_20260929.md
      sha256: 93549bbaf50cf23c292622dc546b3febff08b1751b5e465eea23586be7616b2d
    V1.5:
      file: GUANZHI_花滿樓線_HOT_SAVE_V1.5_薄櫻詞約_邵承祿對帳開場_20260929.md
      sha256: 12f7eaffc4122d0049a2eb89ba690291284f0638448faf1a5598982235b31d25

  historical_correction_sources:
    - source: HOT_V1.6
      use_only_for:
        - 將V1.4_V1.5相對時間校正為菊月初一至初三
        - 確認菊月初一一炷香相親會已實際辦過
      forbidden_backflow:
        - 不吸收V1.6在菊月初三巳正之後的新事件
    - source: CURRENT_HUMAN_CORRECTION_2026_10_01
      use_only_for:
        - 固化菊月初一相親後之菊月初八包廂前約
        - 覆蓋舊稿若寫成單純大堂等待的版本
      forbidden_backflow:
        - 不把青雀是否赴約寫成已發生

  paired_rcl:
    file: 觀止青樓_花滿樓線_人物履歷_RCL_V1.5_MASTER_E01-E18_SCHEMA_V1.1_67人對齊版_20261001.md
    memory_generation: V1.5
    schema: GUANZHI_RCL_SCHEMA_V1_1_COMPATIBLE
    status: REQUIRED_SAME_GENERATION_OUTPUT

  retained_as_newer_hot_overlay:
    - HOT V1.6
    - HOT V1.7
    - HOT V1.8
    - HOT V1.9

  retained_overlay_hashes:
    V1.6: a2a39f5837e2486d3c8ff8430661972eb55a4947e56ff35c997f7c4e2cc9476e
    V1.7: 49779d6cf01f9c24fd4b7b4611d8392eb0123b35d7222a1a34d6e289bc00ae5a
    V1.8: 2df9354f05872f59965652e205911e88eef64fade7cc801300781ecb1542c088
    V1.9: 6bf7d5e404d8a8947bdbc097945a41e3a0769e63e804f5beb3679090a9722b2a

  compile_runtime_baseline:
    core:
      version: V3.6-CURRENT
      file: 01_GUANZHI_RUNTIME_CORE_V3.6_CURRENT_RATIFIED_20261001.md
      sha256: 1a9f3491299bf3bffe3849d78c54e88e02be1121e47472aa6e61ab623aeacbc6
    world:
      version: V2.2.1-CURRENT
      runtime_pointer: V3.6-CURRENT
      file: 02_GUANZHI_WORLD_V2.2.1_CURRENT_V3.6_RUNTIME_POINTER_RATIFIED_20261001.md
      sha256: e42e58bb8631b3b53834f0fcc927453c98baa71cacbfb4e0cfae370d067dabce
    director_guidance:
      version: V3.2-CURRENT
      sha256: e4bab49d06d15bf3b3c199f32d12291357a478ac60c14e7a1f1b72bca50c2c1d
    first_glance:
      version: V0.5-CURRENT
      sha256: 5d69e7bf7e431c85d0e42ff46de07cdae99999755efa04d8bd080a469c60804a
    character_base:
      version: LCAPG_V3.3.18_67_PERSONS
      sha256: 598d544ce9fb1bcea73aa6f92d93c95434f9ab5d1a52b9662f7c8611461ee266

  historical_runtime_note:
    - 各HOT當時使用的Core／First-Glance版本按原檔保留
    - 本MASTER以2026-10-01現行V3.6環境編譯舊史_不宣稱V3.6曾在舊場景實際執行
    - DOCUMENT_COMPILE_NEQ_RETROACTIVE_RUNTIME_EXECUTION

  execution_evidence:
    host_execution: NOT_ESTABLISHED
    host_e6: NOT_ESTABLISHED
    host_e7: NOT_ESTABLISHED
    formal_ceri_provider_execution: NOT_ESTABLISHED
    independent_multi_model_agent_execution: NOT_ESTABLISHED
    formal_main_receipt: NONE_CLAIMED
    formal_lighter_receipt: NONE_CLAIMED
    external_project_save_commit: NONE_CLAIMED
    local_master_file_created: YES

SELF_CONTAINMENT:
  canonical_event_range: E01-E18
  old_hot_chain_required_for_normal_resume: false
  raw_hot_v1_0_to_v1_5_role: SOURCE_PROVENANCE_DETAIL_FALLBACK_AUDIT
  later_hot_v1_6_to_v1_9_role: POST_MASTER_OVERLAY

CURRENT_ROUTE_RESUME_RULE:
  normal_resume:
    1: 本_MASTER_V1.5-HARD
    2: paired_RCL_V1.5
    3: HOT_V1.6
    4: HOT_V1.7
    5: HOT_V1.8
    6: HOT_V1.9
  locks:
    - HOT_V1.0_TO_V1.5_ALREADY_ABSORBED_NOT_NORMAL_OVERLAY
    - HOT_V1.6_TO_V1.9_LATER_THAN_MASTER_CUTOFF_DO_NOT_BACKFLOW_EXCEPT_EXPLICIT_HISTORICAL_CORRECTIONS
    - TEST_DISCUSSION_AUDIT_RUNTIME_ENGINEERING_NEQ_WORLD_FACT
```

---

# 0｜第一次 MASTER V1.5 固化決定

```yaml
GM_COMMIT_DECISION_V1_5:
  explicit_request:
    - "HOT SAVE"
    - "同時第一次MASTER SAVE"
    - "根據標準格式來固化主存檔"
    - "推進到V1.5"

  legal_interpretation:
    - 本輪另產生最新HOT_V1.9_保存當前菊月初五午後狀態
    - 第一次MASTER依玩家明示只固化到HOT_V1.5截止
    - HOT_V1.0到V1.5編譯為E01到E18_形成全歷史自足主存檔
    - HOT_V1.6到V1.9保留為較新overlay_不得倒灌E18
    - HOT_V1.6可作一次明示歷史日期校正來源_僅修正已發生舊事的日期與一炷香首辦已發生事實
    - 本輪玩家對初八包廂前約的明示校正可修正E13舊事_不提前決定初八結果
    - 同代產生RCL_V1.5_作人物截至E18的位置帳

SAVE_DISCIPLINE_V1_5:
  - 只保存已發生事件_可觀察行動_人物本人明示_玩家明示_帳務契約物件_合法UNKNOWN_PENDING_DISPUTED
  - 後證可以校正舊事_不得回鑄當時人物未取得的知識
  - MONEY_NEQ_RELATION
  - PAYMENT_NEQ_ACCESS
  - RELATION_NEQ_CONSENT
  - ADULT_EVENT_NEQ_LOVE
  - INVITE_NEQ_ACCEPTANCE_NEQ_ARRIVAL
  - SOURCE_HISTORY_NEQ_ROUTE_FACT_WITHOUT_ENTRY
  - TEST_OR_VOID_ATTEMPT_NEQ_WORLD_FACT
```

---

# 1｜來源衝突與反污染登錄

```yaml
SOURCE_CONFLICT_REGISTRY:
  V1_5_ABSOLUTE_CALENDAR:
    old_state: NOT_REESTABLISHED
    later_correction: HOT_V1.6_EXPLICIT_CHRONOLOGY_CORRECTION
    current_master_resolution:
      - V1.4成人場定位於菊月初一夜
      - 翌晨為菊月初二
      - 薄櫻晚間會面在菊月初二
      - 邵承祿對帳開場在菊月初三巳正前後
    rule: 只修正日期_不吸收V1.6後續事件

  CHU_YUE_01_MATCHMAKING_ROUND_NUMBER:
    conflict: 舊對話對青雀是第一位或第二輪第八閣的序號描述不一致
    current_master_resolution: 不鎖精確輪次號_只鎖她是花滿樓該局最早形成明確後續約的女子之一

  QINGQUE_CHU_YUE_08_LOCATION:
    old_version: 大堂等待
    latest_human_correction: 花滿樓先開好觀止包廂等她
    current_master_resolution: 包廂版本優先
    lock: 青雀是否赴約仍PENDING

  TINGYUGE_TEMP_NAME:
    old_generated_label: 聽雨閣
    current_state: RETRACTED_NOT_CANONICAL
    retained_place: 南街一間安靜茶食館_後院雅間

  V1_4_DIRECTOR_PRECOMMIT_ATTEMPT:
    status: VOID
    effect: ENTIRE_ATTEMPT_EXCLUDED

  CERI_NARRATOR_RC5_REFERENCE_TESTS:
    status: TEST_ONLY_NONCANON
    effect: NOT_PROMOTED_TO_MASTER
```

---

# 2｜E01–E18 SELF-CONTAINED CAUSAL EVENT LEDGER

## E01｜桂月十六｜初到觀止與香料交貨糾紛

```yaml
EVENT_ID: E01
DATE: 理火三年桂月十六_申初
STATUS: CONFIRMED
SOURCE: HOT_V1.0
KEY_FACTS:
  - 花滿樓初到觀止時遇南市香藥行三匣香料交貨爭議
  - 原單據表面總價六十兩_定銀二十四兩_尾銀三十六兩
  - 外箱當眾開驗只見兩隻未開內匣_第三位置為乾草與兩塊布裹石頭
  - 換車_銅包角差異_疑似女人_換貨字條_觀止印章真偽_紅漆小匣均保持未定
  - 觀止拒收_暫停尾銀_定銀待追索_爭議物分別封存
  - 花滿樓提出先保全證據_按契約核責_必要時走官衙_但沒有替觀止提告
  - 香藥行東家承諾桂月十七辰時送出貨底簿_後續在本MASTER截止前仍未由可靠場景結案
LOCKS:
  - suspicion_ne_proof
  - later_evidence_may_rejudge_not_retroactively_create_knowledge
```

## E02｜桂月十六｜大堂生活、酒帳與新曲觀察

```yaml
EVENT_ID: E02
DATE: 理火三年桂月十六_申末至戌正
STATUS: CONFIRMED
SOURCE: HOT_V1.0
KEY_FACTS:
  - 花滿樓不選姑娘_坐大堂看世界_點一小壺溫酒與三樣小菜
  - 小桃送菜疏漏另賠蔥爆羊肉
  - 柳黃_青衣爭先與賞錢後合作_浮香臨場加琴但拒收當晚臨時合奏賞錢
  - 李桂姐與周官人酒帳責任_醉花賒酒與帳務問題成為樓內商業議題
  - 宋公子想見紫蘭但紫蘭早已退帖_不能用追加賞銀取得作陪
RESULT:
  - 觀止大堂被建立為會自行運作的營業場_不等玩家行動才生活
```

## E03｜桂月十六｜《鮮花滿月樓》與紫蘭一壺酒價交易

```yaml
EVENT_ID: E03
DATE: 理火三年桂月十六_亥初至亥正
STATUS: CONFIRMED
SOURCE: HOT_V1.0
KEY_FACTS:
  - 紫蘭_青衣_柳黃演新曲_浮香臨場加琴
  - 花滿樓評曲可詞不行_與紫蘭談詞意
  - 花滿樓當席寫成《鮮花滿月樓》_首次以花滿樓為筆名落款
  - 花滿樓說誰替他付當晚那一小壺酒錢便把詞送誰
  - 紫蘭搶先付款_取得詞稿
  - 青衣柳黃可另議譜曲與分潤_詞稿在紫蘭手中不等於可無償調度所有樂師
  - 潘金蓮另為答謝香料案方向請三樣小菜_花滿樓本夜帳結清離樓
RELATIONSHIP_IMPACT:
  - 紫蘭與花滿樓建立詞人_主唱的第一個實際作品交易
  - 不建立第二首作品優先權或私人戀愛
```

## E04｜桂月二十二仕女夜｜《鮮花滿月樓》首次公開試唱與小調方向

```yaml
EVENT_ID: E04
DATE: 理火三年桂月二十二_仕女夜
STATUS: CONFIRMED
SOURCE: HOT_V1.1
KEY_FACTS:
  - 潘金蓮自願替花滿樓付本夜男客入場銀二兩_另送桂花糕
  - 紫蘭主唱《鮮花滿月樓》_青衣柳黃琵琶合奏_有女客賞五兩_其他賞銀總額未定
  - 此為首次公開試唱_不是已唱紅或最終定譜
  - 花滿樓送短箋：改用小調唱法_紫蘭等開始試改_約明日再試
  - 浮香本夜休假_可給專業意見但未登台
```

## E05｜桂月二十二｜沈夫人二百兩送嫁詞約

```yaml
EVENT_ID: E05
DATE: 理火三年桂月二十二_仕女夜
STATUS: CONTRACT_ESTABLISHED_WORK_DELIVERED_PAYMENT_THEN_PENDING
SOURCE: HOT_V1.1
KEY_FACTS:
  - 沈夫人為下月出嫁妹妹求私人送嫁詞_不想要陳套喜辭
  - 花滿樓報價二百兩：二十兩潤筆_一百八十兩以花滿樓名義贈新娘
  - 沈夫人接受_要求180兩直接交妹妹本人_不混娘家或夫家帳
  - 花滿樓完成《滿庭芳·家後》_沈夫人收走原稿
  - 兩份憑記分列20兩潤筆與180兩賀禮
  - 截止V1.5原始檔時付款與賀禮送達仍未由當場證據完成
LOCKS:
  - 玩家說價值兩千兩只是藝術價值主張_不是成交價
  - 妹妹本人反應與婚後狀態未決
```

## E06｜桂月二十二｜阿蘅比詩、桂花釀與《鵲踏枝·曉別》

```yaml
EVENT_ID: E06
DATE: 理火三年桂月二十二_仕女夜
STATUS: CONFIRMED_PRIVATE_INTERACTION
SOURCE: HOT_V1.1
KEY_FACTS:
  - 年輕女客對外稱陸夫人_自稱小字阿蘅_全名與家門未知
  - 阿蘅請顧公子與花滿樓比七絕_題今宵偶遇_禁花月酒三字
  - 阿蘅按自己喜好判花滿樓《七絕·南風惜別》得選_履約請上等桂花釀一壺
  - 花滿樓後作《鵲踏枝·曉別》題贈阿蘅
  - 花滿樓提出若她願意可用一吻作象徵性代價_阿蘅自願短吻並收詞
  - 阿蘅回牌桌後離樓_沒有戀愛_再會日期_排他或未來身體權成立
```

## E07｜桂月二十二｜醉花西側半圓高台酒吧構想

```yaml
EVENT_ID: E07
DATE: 理火三年桂月二十二_仕女夜後段
STATUS: DESIGN_DIRECTION_ONLY
SOURCE: HOT_V1.1
KEY_FACTS:
  - 花滿樓提出大堂西側較暗處高台半圓吧檯_高腳椅_背牆酒架_兼顧看戲與隱蔽
  - 醉花對論杯賣酒_調配_招牌酒_陪聊另計等有興趣
  - 潘金蓮要求先請木作隔扇師傅量場畫圖_考慮立柱_視線_安全_出入口
  - 未開工_未撥款_未定醉花正式職位_無玩家分紅
```

## E08｜桂月二十五｜照夜／三聖母自主到觀止與三層身份

```yaml
EVENT_ID: E08
DATE: 理火三年桂月二十五_夜
STATUS: CONFIRMED_ROUTE_ENTRY
SOURCE: HOT_V1.2
KEY_FACTS:
  - 潘金蓮依花滿樓提議以掌櫃名義邀華山三聖母來觀止_聲明不強求
  - 三聖母自主到達_持寶蓮燈_由小桃帶入大堂
  - 她自述聽到邀請後走出華山拘禁範圍_機制與封印是否解除仍未知
  - 來源真身：華山三聖母_與劉彥昌_沉香故事相關
  - 人間行政草案：楊蓮娘_華陰成年女子_夫子離散_自願來汴梁憑才藝營生
  - 公開花名：照夜_由本人選定
  - 楊蓮娘文牒_妓籍_服務契約_掛牌_競拍均未完成
  - 照夜為自由身_不是觀止奴婢
```

## E09｜桂月二十五｜花滿樓 × 照夜「人間安身約」

```yaml
EVENT_ID: E09
DATE: 理火三年桂月二十五_夜
STATUS: CONTRACT_ESTABLISHED_FUTURE_PERFORMANCE_PENDING
SOURCE: HOT_V1.2
CORE_PROMISE:
  - 花滿樓承諾透過人間公堂與天庭法域爭議_取得天庭不能在人間合法依天條拘拿照夜的實際安身效果
  - 單有不能落實的紙判決不算履約
  - 天庭若不依法而動武是另一類風險_不把法理勝訴寫成物理無敵
CONDITIONAL_PRIVATE_RETURN:
  - 若花滿樓真正完成上述成果_照夜另擇一夜親邀共飲共寢_不收銀兩
  - 本線後續契約語境確認該原約包含成人性關係方向_但日期與原約外具體行為未預買
SECOND_SEPARATE_AGREEMENT:
  - 若照夜日後自主舉行首次正式一夜成人陪宿競拍
  - 扣除觀止事先約定分帳後_照夜本人實得款的三成一次性給花滿樓
  - 競拍尚未發生_分帳率未知_花滿樓未實收
PAN_BENEFIT:
  - 潘金蓮即刻答應花滿樓本人往後入場與普通茶水免費
  - 尋常酒菜免費仍附條件_須照夜人間身份與實際留居取得證據
```

## E10｜桂月二十五｜王昭君、《陽關三疊》與紫蘭藝術線

```yaml
EVENT_ID: E10
DATE: 理火三年桂月二十五_夜
STATUS: ACTIVE_ARTISTIC_THREAD
SOURCE: HOT_V1.2
KEY_FACTS:
  - 王昭君／王嬙自主入場_本人記憶與後世悲劇戲版本分層
  - 花滿樓提出新《陽關三疊》編排：極慢起_逐步加速_歌者追琴_峰頂雙琵琶驟停_紫蘭末兩句一口氣攀高延音
  - 青衣重整齊_柳黃愛提速_紫蘭對氣口體力有合理顧慮_尚未完成終極演出
  - 鈴娘受邀籌備《昭君出塞》第一幕_劇本_報酬_改編權尚未定
  - 醉花轉達浮香願修譜_紫蘭願談修譜費與署名_浮香尚未簽約或完成修譜
```

## E11｜桂月二十五｜仕女夜巷、夜市商業與疑似宮禁端

```yaml
EVENT_ID: E11
DATE: 理火三年桂月二十五_夜
STATUS: PARTIALLY_ESTABLISHED_SPACE_DESIGN
SOURCE: HOT_V1.3
KEY_FACTS:
  - 花滿樓選擇暫等天庭來告_本夜不主動擊鼓
  - 從外送笑談發展出觀止後院仕女夜市長街構想
  - 潘金蓮實際宣告延展後院_石板長街與兩側避雨騎樓初步成形
  - 最終名稱定為仕女夜巷_只在每月初一初八十五二十二四個仕女夜開市
  - 准入以女子與太監為主_普通男子不得入巷_皇帝為設計上的唯一男性例外但須另有真實宮禁授權
  - 男女相看與交際仍在主樓大堂_不把紅線入巷憑記當成戀愛或性同意
  - 長街尾端出現疑似宮牆／大內方向_潘與龐春梅先封控
  - 兩名禁軍來詢問疑似私修宮道_未形成定罪_開門許可或御前批准
```

## E12｜桂月二十五｜「一炷香鴛鴦會」制度與花滿樓首席報名

```yaml
EVENT_ID: E12
DATE: 理火三年桂月二十五_夜
STATUS: RULES_ESTABLISHED_FIRST_SESSION_THEN_FUTURE
SOURCE: HOT_V1.3
RULES:
  - 十男十女_十間屏風雅閣
  - 女子固定雅閣_男子按號換閣
  - 女方可自願戴面具_是否摘面具由本人決定
  - 一輪一炷香_危險或失禮可提前撤離
  - 雙方合意可提前雙雙離席_另約大堂飲宴私人約會或房間皆另議
  - 流水補位
  - 每人最多五輪_五輪未成即回大堂_不得同場重新排隊
  - 參加皆成年人且自願_交談不等於成人契約
PLAYER_ENTRY:
  - 花滿樓表示報名費若由潘出就參加
  - 潘金蓮接受替他承擔首場報名費_列為首批報名者
  - 當夜明示菊月初一仕女夜再來
```

## E13｜桂月二十五至菊月初一｜官家邀帖、劉娥密談與首屆輪轉相親實跑

```yaml
EVENT_ID: E13
DATE: 理火三年桂月二十五_夜_to_菊月初一_夜
STATUS: MIXED_CONFIRMED_WITH_HISTORICAL_CORRECTION
SOURCES:
  - HOT_V1.3
  - HOT_V1.6_CHRONOLOGY_CORRECTION
  - PRIOR_ROUTE_CONVERSATION
  - CURRENT_HUMAN_CORRECTION_2026_10_01

PRE_SESSION_FACTS:
  - 花滿樓親筆把官家邀帖改為「月上柳梢頭_人約黃昏後。老鴇潘金蓮率觀止姑娘們邀請官家蒞臨指導」
  - 潘金蓮蓋觀止印_交小桃預備次日循正常渠道呈送
  - 截止當晚無證據證明官家已讀_已批_已來或宮道獲准
  - 花滿樓在隔音私席提出劉娥倡婦／轉售等來源史疑雲_潘金蓮龐春梅蘇清照夜知情並同意封口
  - 來源史材料不等於當朝正式妓籍文書已取得

FIRST_SESSION_CORRECTION:
  - 菊月初一首屆一炷香鴛鴦會實際已辦過_不得再寫成未來首辦
  - 花滿樓實際參與輪轉
  - 舊紀錄對花滿樓精確排號與青雀輪次有不一致_本MASTER不硬鎖序號

QINGQUE:
  - 一名女子以青雀為花名／稱呼
  - 雙方在一炷香內以暫時情郎／女人的遊戲框架互動_互不強問真姓名家世
  - 她摘過面具_雙方有牽手與接吻的已演互動
  - 花滿樓送《蝶戀花·青雀離》_青雀收下
  - 她選擇不作當場正式配對退場
  - 後續約定校正為：菊月初八夜花滿樓先開好觀止包廂等她_她若仍想見可自行赴約_未承諾一定來_若來才再談要不要繼續

OTHER_ROUNDS:
  - 玄燕：談無聊_陪伴與花和尚／青樓不空不成佛等話題_曾摘面具_沒有正式配對或固定後約
  - 白鹿：有悖論／問答遊戲_摘面具_白棋物件相關舊記錄存在_但舊對話曾有結果作廢／不計的修正_本MASTER不把配對或勝負固定
  - 紅綃：花滿樓是她當夜最後一輪男人之一_她摘面具_收下花滿樓贈詞／話語後以「這第四世_我輸得心甘情願」收束_沒有正式配對_沒有下次約定_未建立接吻或成人事件

NEXT_ENTRY:
  - 其後另有以「故人」為花名／入口的成年女子_後來自報真名沈如晦
  - 該次相遇承接到E14私密場景

LOCKS:
  - MATCHMAKING_TALK_NE_RELATION
  - KISS_NE_FUTURE_ACCESS
  - MASK_REMOVAL_NE_PUBLIC_IDENTITY
  - CHU_YUE_08_INVITE_NE_ARRIVAL
```

## E14｜菊月初一夜｜「故人」沈如晦與私人成人場

```yaml
EVENT_ID: E14
DATE: 理火三年菊月初一_夜
STATUS: CONSENSUAL_ADULT_EVENT_COMPLETED
SOURCES:
  - HOT_V1.4
  - HOT_V1.6_CHRONOLOGY_CORRECTION
  - PRIOR_ROUTE_CONVERSATION
KEY_FACTS:
  - 以「故人」相遇的成年女子後自報真名沈如晦
  - 兩人談及婚約_夢中故人等私人內容_並轉入觀止私人房
  - 早段曾明確保留不進行陰道插入的界線_可抱可親近_任何時候可停
  - 後續雙方又形成新的當下成人意願_最終完成一次肛交
  - 本場沒有陰道插入
  - 最後停止肛交並退出後_花滿樓射精_以布帕承接
  - 沈如晦有疲勞與局部不適_沒有被硬寫成醫療診斷
  - 事件後雙方仍在同一房間_喝水_休息_整理衣物並可交談玩笑
  - 不建立戀愛_婚姻_排他_固定性伴侶_下一次成人同意或新金錢交易
ANTI_CORRUPTION:
  - 一次導演在生成前預決射精_鏡頭與收尾的attempt整次VOID_不進MASTER
  - CERI_Narrator_RC5等reference tests均不進故事史
```

## E15｜菊月初一夜至初二清晨｜同睡與沈如晦自行離房

```yaml
EVENT_ID: E15
DATE: 理火三年菊月初一_夜_to_初二_清晨
STATUS: CONFIRMED
SOURCE: HOT_V1.5_WITH_V1.6_DATE_CORRECTION
KEY_FACTS:
  - 花滿樓明示抱著沈如晦睡_並說天亮不用叫醒_她可自行離開
  - 兩人實際睡下
  - 菊月初二清晨沈如晦先醒_移開花滿樓手臂_整理衣著後自行離房
  - 沒有叫醒花滿樓
  - 未形成下次約會_戀愛_婚約_排他或成人承諾
```

## E16｜菊月初二午後｜小桃、陌生傳話女子與一炷香局外約見入口

```yaml
EVENT_ID: E16
DATE: 理火三年菊月初二_午後
STATUS: CONFIRMED
SOURCE: HOT_V1.5_WITH_V1.6_DATE_CORRECTION
KEY_FACTS:
  - 花滿樓午後醒來_沈如晦已離房
  - 小桃來敲門_送熱水_安排東邊清靜小包廂
  - 花滿樓與小桃有身形_胸衣_裁縫玩笑_並突然抱住小桃偷親一下
  - 小桃明顯驚訝生氣_以言語與踩鞋面反應
  - 只成立一次突來親吻_不建立戀愛或未來身體access
  - 一名未知成年女子作傳話者_詢問一炷香局是否可不抽籤直接指定花滿樓
  - 花滿樓表示真想見可直接另約時間請吃飯求詞_場外成年人的私人約定不由相親局替他們包辦
  - 傳話女子其後送帖子_約當晚南街一間未具名茶食館後院雅間
  - 舍方知作為LCAPG裁縫資源被提及_花滿樓截至E18尚未與她正式見面
```

## E17｜菊月初二晚｜薄櫻詞約、匿名測試與真正委託

```yaml
EVENT_ID: E17
DATE: 理火三年菊月初二_晚
STATUS: CONFIRMED_WITH_UNRESOLVED_IDENTITY
SOURCE: HOT_V1.5_WITH_V1.6_DATE_CORRECTION
NPC:
  route_name: 薄櫻
  true_name_at_cutoff: UNKNOWN
  adult: true
  later_true_name_not_backflowed_into_cutoff_knowledge: 龐宜娘_is_post_cutoff_reveal_in_V1.6
KEY_FACTS:
  - 會面在南街未具名茶食館後院雅間_聽雨閣臨時名已撤回
  - 薄櫻當晚不願透露真名_接受花滿樓稱她薄櫻
  - 她要一首外表體面_不直白哀怨_讓人看見自己有錢有閒且不好挑失態的詞
  - 花滿樓完成《青玉案·薄櫻》_薄櫻接受_偏私人／選擇性流通_不授權以花滿樓名義公開
  - 花滿樓另免費作《蝶戀花·薄櫻》_認為更適合風月場歌者公開唱
  - 當時設計為匿名送紫蘭試唱_若她真唱再揭作者_截止E18尚未確證送達或開唱
  - 薄櫻最初封套十兩_說五兩請吃飯聽她說話_另五兩詞定金
  - 接受第一首後又加一錠銀子_當時面額未固定_另放小金葉_明說不是詞錢
  - 後續帳務校正才確認10兩與50兩計入收入_金葉不折現_本MASTER保留該後證但不回鑄E17當時的即時精確核帳認知
TRUE_REQUEST:
  - 寫詞是真的_但也是接近與測試花滿樓的一部分
  - 她原想用一炷香局匿名測花滿樓是否追問身份_外傳女人私事_收錢後替客人做主人生
  - 真正主要委託是請花滿樓陪她見邵承祿_作獨立第三方／旁聽與談判支援
  - 花滿樓接受_理解為幫她拿回應由她自己決定的財產控制權
  - 薄櫻希望事情能成_但不是不惜代價
SECRET_SIGNAL:
  - 薄櫻若親手把茶壺嘴轉向花滿樓_表示她不再希望把事情往談成方向推
  - 暗號只傳達態度_不替花滿樓決定行動
```

## E18｜菊月初三巳正前後｜邵承祿六年帳契談判正式開場

```yaml
EVENT_ID: E18
DATE: 理火三年菊月初三_巳正前後
STATUS: CURRENT_MASTER_CUTOFF
SOURCE: HOT_V1.5_WITH_V1.6_DATE_CORRECTION
LOCATION:
  public_front: 薄櫻母親留下的香料鋪_前堂正常營業
  private_room: 後堂平常對帳的小房
PRESENT:
  - 花滿樓
  - 薄櫻
  - 邵承祿
  - 邵承祿帶來的捧帳冊小夥計
OBJECTS:
  - 薄櫻右手邊茶壺_壺嘴朝外_未觸發暗號
  - 薄櫻整理的數張紙
  - 邵承祿抱來的厚木匣_內容未開驗
  - 小夥計捧來的帳冊_未逐冊驗證
BAOYING_ACCOUNT_AS_TOLD:
  - 母親生前把一間香料鋪與兩處小田收益交邵承祿代管
  - 原說法為薄櫻成年能料理後交回帳與契據
  - 薄櫻已成年兩年
  - 她不是完全看不到帳或拿不到錢
  - 截止E18無證據證明邵承祿吞款
  - 她指稱邵多次以不懂生意_女子帶契不安全_等定親後交夫家等理由延後交契
REQUESTED:
  - 近六年完整帳冊
  - 香料鋪契據
  - 兩處田契
  - 歷年收支憑據
  - 邵承祿繼續代管的權限與理由
STOP_POINT:
  - 邵承祿先問陌生花滿樓身份
  - 薄櫻答：我請來旁聽的人
  - 邵承祿問：家裡的帳_讓外人聽？
  - 薄櫻沒有碰茶壺_最後說：邵叔。今天我們先把什麼叫「家裡的帳」說清楚。
UNRESOLVED:
  - 木匣內容
  - 帳冊真偽完整性
  - 邵承祿法律受託權
  - 是否侵占挪用或善意保管
  - 契據登記與交付結果
  - 薄櫻真名與家門
  - 談判結果
```

---

# 3｜玩家作品與文本硬存檔｜截至 E18

## 3.1 《鮮花滿月樓》

```text
春風到人間花開透
幽香四溢    百花滿月樓
秀麗百花    相伴絲絲柳
無窮春光實難求

春光過後會回頭
知心愛伴  世間最難求
你莫要等  花落心傷透
要趁春花開錦繡

莫要等  莫要等
莫要等  飄雪時候
並蒂花  知心友
心事你可知道否

枝枝愛情花已並頭
絲絲愛念寄花滿月樓
愛慕美景心事輕輕透
祈求知心   心相扣
```

- 作者／筆名：花滿樓。
- 紫蘭以初訪一小壺酒價取得詞稿；桂月二十二已有公開試唱。
- 小調唱法方向已提出；截至 E18 尚未固化唱紅結果。

## 3.2 《滿庭芳·家後》

```text
霜侵雙鬢，兒孫繞膝，閒庭同坐斜陽。
粗茶淡飯，冷暖兩尋常。
細數當年往事，君猶道、年少風光。
相看笑，衣衫何計，十指共天長。

思量。初嫁日，青絲未雪，拌嘴成雙。
看浮沉世事，誰似君強。
若到塵緣將盡日，寧先送、君過寒江。
還低語，容儂先去，怕見淚千行。
```

- 沈夫人已收原稿。
- 契約：總額 200 兩，其中 20 兩潤筆，180 兩以花滿樓名義給新娘。

## 3.3 《七絕·南風惜別》

```text
南風過檻帶茶香，
燭影低垂話更長。
曉色偷從簾縫入，
歸來夢裏掩晨光。
```

## 3.4 《鵲踏枝·曉別》

```text
今夜低聲君且住，
曉夢初分，莫覓離人處。
非是無情輕別去，
只恨浮生難久聚。

合眼猶聞君笑語，
相隔千山，此意仍如故。
莫把餘年交淚雨，
待到天涯重見汝。

花滿樓贈阿蘅
```

## 3.5 《蝶戀花·青雀離》

```text
閱盡天涯離別苦，不道歸來，零落花如許。
花底相看無一語，綠窗春與天俱莫。
待把相思燈下訴，一縷新歡，舊恨千千縷。
最是人間留不住，朱顏辭鏡花辭樹。
```

- 菊月初一一炷香相親時贈青雀；青雀收下。
- 此作存在與收受已保存；不因此建立正式配對或初八赴約必然性。

## 3.6 《青玉案·薄櫻》

```text
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
```

- 薄櫻接受；偏私人／選擇性流通。
- 截止 E18 不授權以花滿樓名義公開。

## 3.7 《蝶戀花·薄櫻》

```text
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
```

- 花滿樓明示免費第二版。
- 截止 E18 計畫匿名送紫蘭試唱，但送達／看過／答應唱／公開演出均未建立。

## 3.8 《陽關三疊》本線可核對片段

```text
悶坐雕鞍思憶漢皇
朝朝暮暮 暮暮朝朝
黯然神傷
前途茫茫 極目空翹望
見平沙雁 落聲斷衡陽
月昏黃返 照雁門關上
塞外風霜 悠悠馬蹄忙
整日思想 長夜思量
魂夢憶君王
```

結尾指定：

```text
天長地老長懷想
一曲琵琶恨正長
```

- 中段其餘逐字原文在現有 HOT 截止檔中不完整，本 MASTER 不補造。

---

# 4｜MASTER V1.5 CURRENT HARD STATE｜E18

```yaml
CURRENT_HARD_STATE_AT_E18:
  story_time: 理火三年菊月初三_巳正前後
  current_location: 薄櫻母親留下的香料鋪後堂對帳房
  present:
    - 花滿樓
    - 薄櫻
    - 邵承祿
    - 捧帳冊小夥計

  player_identity:
    public_name: 花滿樓
    true_name: UNKNOWN
    origin_family: UNKNOWN_AT_CUTOFF
    residence: UNKNOWN_AT_CUTOFF
    financial_profile: NOT_YET_CONSOLIDATED_AT_E18

  major_established:
    - 香料交貨案曾在桂月十六保全證據並拒收_後續六日結果截至本cutoff未可靠結案
    - 紫蘭持《鮮花滿月樓》並已完成桂月二十二首次公開試唱
    - 沈夫人200兩送嫁詞約與《滿庭芳·家後》交付成立
    - 阿蘅取得私人題贈與一次自願短吻_無後續關係承諾
    - 醉花高台半圓酒吧仍為設計／評估線
    - 照夜已進花滿樓線_人間安身約成立_官司未開_身分文牒妓籍未辦
    - 仕女夜巷空間與一炷香鴛鴦會制度已建立
    - 菊月初一首屆一炷香輪轉相親已實際舉行
    - 青雀與花滿樓留下初八條件式再見前約_到場未定
    - 沈如晦與花滿樓完成一次肛交成人事件_無陰道插入_無自動關係升級
    - 沈如晦翌晨自行離房_沒有下一次約定
    - 薄櫻已給兩首詞的委託／贈作線_並委託花滿樓陪見邵承祿
    - E18談判只剛開場_茶嘴暗號尚未觸發

  open_threads:
    - 香藥行貨底簿與賠償結果
    - 沈夫人20兩潤筆與180兩賀禮實際交付狀態_後續HOT另有校正
    - 醉花酒吧師傅量場與是否施工
    - 照夜人間身分_妓籍_服務契約_官訟_競拍_沉香消息
    - 官家請帖是否送達與宮禁端是否獲批
    - 劉娥來源秘聞的證據與保密
    - 紫蘭《陽關三疊》終極演出能否完成
    - 青雀菊月初八是否赴約
    - 玄燕白鹿紅綃是否未來再遇
    - 小桃一次突來親吻後的關係餘波
    - 薄櫻真名_邵承祿動機_木匣內容_帳冊真偽_契據交付與談判結果

  anti_backfill:
    - HOT_V1.6_TO_V1.9_NOT_PART_OF_E18_CURRENT_STATE
    - LATER_TRUE_NAME_GONG_YINIANG_NOT_KNOWN_AT_E18
    - LATER_GHOST_HOUSE_SERVANTS_FINANCE_NOT_BACKFLOWED
    - CURRENT_CORE_V3.6_COMPILE_DOES_NOT_MEAN_V3.6_EXECUTED_E01_E18
```

---

# 5｜知情與秘密硬邊界｜截至 E18

```yaml
KNOWLEDGE_BOUNDARIES:
  PLAYER_TRUE_IDENTITY:
    state: UNKNOWN_TO_ROUTE_CHARACTERS
    note: 花滿樓只是筆名

  LIU_E_SECRET_TALK:
    knowers:
      - 花滿樓
      - 潘金蓮
      - 龐春梅
      - 蘇清
      - 照夜
    outsiders_not_auto_informed:
      - 紫蘭
      - 醉花
      - 小桃
      - 普通客人
      - 禁軍
      - 汴梁市民

  SHEN_RUHUI_ADULT_EVENT:
    direct_knowers:
      - 花滿樓
      - 沈如晦
    others: NOT_AUTOMATICALLY_KNOWN

  QINGQUE_PRIVATE_IDENTITY:
    mask_removal_to_huamanlou: ESTABLISHED
    public_identity: NOT_ESTABLISHED
    later_meeting: PENDING

  BAOYING_TRUE_NAME:
    at_E18: UNKNOWN_TO_HUAMANLOU
    later_reveal: MUST_NOT_BACKFLOW_TO_E18_CHARACTER_KNOWLEDGE

  TEAPOT_SIGNAL:
    knowers:
      - 花滿樓
      - 薄櫻
    meaning: 薄櫻不想繼續往談成方向推
    status_at_cutoff: NOT_TRIGGERED
```

---

# 6｜帳務、契約、物件索引｜截至 E18

| 項目 | E18 截止狀態 |
|---|---|
| 香藥訂貨 | 24兩定銀待追索、36兩尾銀曾暫停支付；後續結果未在本 MASTER cutoff 結案 |
| 《鮮花滿月樓》 | 紫蘭以一壺酒價取得原詞；已首度公開試唱 |
| 沈夫人送嫁詞 | 200兩契約：20潤筆＋180花滿樓名義賀禮；詞稿已交 |
| 阿蘅桂花釀 | 阿蘅因比詩履約請一壺；非玩家欠帳 |
| 醉花高台酒吧 | 構想＋潘要求師傅評估；未施工 |
| 照夜人間安身約 | 已成立；履約成果未完成 |
| 照夜私人酬謝 | 條件式未來；未履行 |
| 照夜首次一夜競拍三成 | 獨立條件性協議；競拍未發生 |
| 花滿樓入場與普通茶水 | 潘已承諾即刻長期免費給花滿樓本人 |
| 仕女夜巷 | 空間初步呈現＋四夜限定運營方向；租戶與收入未完成 |
| 一炷香鴛鴦會 | 規則已定；菊月初一首屆後來確證已實際舉行 |
| 青雀初八前約 | 花滿樓將開包廂等待；青雀是否到場未定 |
| 《青玉案·薄櫻》 | 薄櫻已收；私人／選擇性流通 |
| 《蝶戀花·薄櫻》 | 免費第二版；匿名送紫蘭試唱計畫在 E18 尚未完成送達 |
| 薄櫻十兩＋銀錠＋金葉 | E17當下精確落袋／銀錠額未全固定；後續玩家校正10兩＋50兩計收入、金葉不折現，作歷史帳務校正保存 |
| 茶壺暗號 | 已約定；E18未觸發 |
| 邵承祿木匣與帳冊 | 到場但未驗；內容與真偽不得先決 |

---

# 7｜Normal Resume

> **正常接關：MASTER V1.5-HARD + paired RCL V1.5 → HOT V1.6 → HOT V1.7 → HOT V1.8 → HOT V1.9。**
>
> HOT V1.0–V1.5 已固化為 E01–E18；正常 STORY 不再逐份疊加。需要逐字作品、原始對話、帳證、私密知情或污染審計時，才回查原 HOT 作 provenance / detail fallback。

---

# 8｜編譯驗證

```yaml
COMPILE_STATS:
  memory_generation: V1.5
  master_event_range: E01-E18
  absorbed_hot_count: 6
  post_master_hot_overlays:
    - V1.6
    - V1.7
    - V1.8
    - V1.9
  first_master: true

VALIDATION:
  master_cutoff_matches_user_request: PASS_V1.5
  source_hot_hashes_present: true
  later_overlay_forward_contamination: false
  v1_6_date_correction_scoped_only: true
  current_human_chu8_correction_scoped_only: true
  v1_4_void_attempt_excluded: true
  tests_promoted_to_world_fact: false
  unresolved_states_preserved: true
  relation_auto_promoted_from_adult_event: false
  payment_auto_promoted_to_consent: false
  invite_auto_promoted_to_arrival: false
  player_true_identity_invented: false
  master_rcl_atomic_pair_required: true
```

---

# MASTER SAVE 責任聲明

本檔依玩家本輪明示授權建立，為《觀止青樓》花滿樓線**第一次 MASTER SAVE，版本 V1.5-HARD**。

它代表：

- HOT V1.0–V1.5 的有效故事史已編譯為 E01–E18；
- E18 截止點為菊月初三巳正前後、邵承祿對帳剛開場；
- HOT V1.6–V1.9 仍是較新的 post-MASTER overlay；
- 正常續玩不必再逐份重讀 V1.0–V1.5；
- 歷史校正與未決事項已分開；
- VOID／TEST／治理討論未升格為世界事實；
- 本 MASTER 與同代 RCL V1.5 構成正常重載配對。

它不代表：

- Host 已完成外部 SAVE commit；
- 外部專案倉庫已自動安裝此檔；
- Core V3.6 曾在 E01–E18 當時正式執行；
- 青雀初八赴約、邵承祿談判結果或任何 V1.6 以後事件已倒灌 E18。
