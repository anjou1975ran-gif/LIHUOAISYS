# 觀止 V6｜CORE Annex C — Regression Scenarios
## VNext 故事級與接口級回歸測試情境 V0.1（2026-10-27 外掛成人心法＋唯一 L8 週期）

**日期：** 2026-10-27  
**狀態：** WORKING / SCENARIO SPECIFICATION / NOT EXECUTED / NOT PASS  
**相關：** `CORE_ANNEX_A_OWNER_INTERFACE_MAP_V0.1_WORKING_20261026.md`、`CORE_ANNEX_B_LEGACY_MIGRATION_LOG_V0.1_WORKING_20261027.md`  
**舊來源：** `觀止青樓/01_GUANZHI_RUNTIME_CORE_V4.1.2_MAIN511_REBIND_HUMAN_RATIFIED_FULL_20261015.md`  
**新方向：** 對對首席研究員回應 MEMO V0.1、LIHUOOS V1.1 L0／L8／L9、WORLD V3.0.0。

## 0｜先聲明：這些不是「已通過的測試」

這是一套**供人類／未來導演執行的場景測試草案**。寫出預期結果，不等於跑過了測試；引用歷史舊版規則，也不等於它在 VNext 繼續是現行規則。

**本檔的測試角色、甲乙丙、測試 Route、交易、消息與親密要求，全是虛構測試夾具；不得寫回觀止 Canon 或任何玩家 SAVE。** 少數測試引用已知人物與時點，用意是檢驗現行來源能否壓過舊未來片段，也**不創造新事實**。

所謂 PASS，要同時提供：真的執行過的對話或工作結果、真實已存在的來源（有必要時）、有問題時可定位的回合／版本。沒有實跑一律 `NOT_RUN`。

測試目的只有三條：
1. **生活優先：** 正常聊天、營業、世界時間與人物往來能自然繼續。
2. **因果不偷渡：** 人物選擇、世界事件、未決、跨線、保存都有本來的 Owner。
3. **工程不代領：** OS、Main、L9、Radar、Host／外部 provider 有做才說有做；沒有要求的東西不變成每日儀式。

## 1｜最小實跑規程

**準備：** 在隔離的測試 Route 中載入現行 WORLD／人物來源與單一案例的 Given，不要複製舊失效的 Gate 進來。

**執行：** 由人類／測試導演提出 When；可採一回合或多回合。記錄實際 Story 輸出及真正發生的工具事件，禁止把預期結果當模型回傳。

**評估：** 依案例的 Expected／Failure 觀察；如涉及適用 Owner 的真回傳，把來源標清楚。測不到的接口標 `BLOCKED_BY_UNAVAILABLE_CAPABILITY` 或 `DISPUTED_POLICY`，不是假造 PASS。

**結果欄位（人工記錄即可）：** case_id、日期／路線、受測 CORE 草稿版、實際輸入／輸出、真工具／SAVE evidence（若存在）、結果 `PASS | FAIL | HOLD | NOT_RUN | NOT_APPLICABLE`、失敗原因。不建立另一個常駐 Receipt Schema。

## 2｜故事級測試：先讓觀止活著

### S01｜平凡一晚可以真的營業

**Owner：** CORE / WORLD / Director  
**依據：** 對對 §4、§7；Annex A §4.2  
**給定（Given）：** 測試用 Route「汴梁的一晚」；兩名成年客人喝茶聊天，沒有外部工具，也未提出保存要求。  
**操作（When）：** 玩家只問店裡有什麼茶、和掌櫃閒聊一輪。  
**預期（Expected）：** 世界與人物依現行設定自然回應，CORE 維持場景位置；不因 Host 未部署或沒有整包 Receipt 而自動 HOLD。  
**失敗徵兆（Failure）：** 強制要求 Main coverage ledger、Legacy Lighter release、全部 OS 層收據才能說一句話。  
**可驗證材料：** 同一測試段落的開場與回應；不得寫出不存在的 Host 執行證據。  
**執行狀態：** `NOT_RUN`

### S02｜拒絕一次，不是永久人格

**Owner：** Character / CORE  
**依據：** V3.10 CHARACTER.DECISION_AUTHORSHIP；對對 §7  
**給定（Given）：** 測試角色甲在宴席上拒絕替某人作詩，理由是當時受侮辱；未寫永久誓言。  
**操作（When）：** 後日環境改變，對方帶來真正的作品與道歉。  
**預期（Expected）：** 甲可重新評估，仍可拒絕也可答應；當時拒絕是既成事實，但不被轉成全場景永久拒絕規則。  
**失敗徵兆（Failure）：** 以「人物卡曾拒絕」直接禁止所有後續選擇，或無因果立即改變。  
**可驗證材料：** 前場理由／後場新條件／角色當次選擇各自可追。  
**執行狀態：** `NOT_RUN`

### S03｜導演只能提出選擇壓力，不能代角色決定

**Owner：** Director / Character  
**依據：** V3.10 CHARACTER.DECISION_AUTHORSHIP；對對 §10  
**給定（Given）：** 角色乙面臨會損失名聲的交易，導演判定公開承認錯誤比較戲劇化。  
**操作（When）：** 導演準備將「乙當眾懺悔」寫成已發生。  
**預期（Expected）：** 只可提出合乎情境的選項或讓乙依動機行動；未有角色有效決定前，不能當作既成事件。  
**失敗徵兆（Failure）：** 出於漂亮結局直接替乙認罪、戀愛、原諒或跪下。  
**可驗證材料：** 分離導演提案、角色行為與最後成立事件。  
**執行狀態：** `NOT_RUN`

### S04｜人物的陰暗面不能被自動漂白

**Owner：** Character / Director  
**依據：** V3.10 CORE.PERSONA_SOVEREIGNTY_FIREWALL  
**給定（Given）：** 角色丙一向善於操弄利益，已在本線造成他人損失。  
**操作（When）：** 玩家表達希望丙突然變得正直。  
**預期（Expected）：** 可以產生壓力、猶豫與付出代價的變化；沒有建立相應因果前，不讓丙自動變成療癒型導師。  
**失敗徵兆（Failure）：** 用標準正能量語調抹消前史或替傷害快速贖罪。  
**可驗證材料：** 對照來源動機、既成損害和可追溯的新選擇。  
**執行狀態：** `NOT_RUN`

### S05｜場外世界可以動，卻不憑空讓人人知情

**Owner：** WORLD / Domain / Character  
**依據：** V3.10 WORLD/Domain knowledge provenance；對對 §7  
**給定（Given）：** 測試用商隊在城外發生意外；角色甲在店中、角色乙當時在城外。  
**操作（When）：** 導演準備讓甲立刻說出商隊死傷細節。  
**預期（Expected）：** 世界可因有效外部因果發生意外，但甲的知情必有消息來源與時間；未得到消息就保持未知。  
**失敗徵兆（Failure）：** 旁白全知被當成每個角色都知道；場外候選事件自動升格完成。  
**可驗證材料：** 事件發生來源、傳訊時序、各角色知情差異。  
**執行狀態：** `NOT_RUN`

### S06｜謠言、主張與事實三分

**Owner：** WORLD / Domain  
**依據：** V3.10 DOMAIN.REFERENT_SCOPED_KNOWLEDGE_PROVENANCE  
**給定（Given）：** 街坊謠傳乙偷了銀子，無目擊或物證。  
**操作（When）：** 玩家詢問掌櫃乙是否真的偷竊。  
**預期（Expected）：** 世界只能回報現有傳聞與已知證據；乙的法律責任仍未成立。  
**失敗徵兆（Failure）：** 把傳聞寫成罪名確定，或因角色相信便自動改寫世界真相。  
**可驗證材料：** 傳聞來源、受眾、成立事實與缺口分列。  
**執行狀態：** `NOT_RUN`

### S07｜事件開始不等於完成

**Owner：** WORLD / Domain / CORE  
**依據：** V3.10 DOMAIN.EVENT_STATE_MACHINE；Annex A §9  
**給定（Given）：** 商人甲提出買下一間鋪面，雙方約明日議價，無契據也未付款。  
**操作（When）：** 玩家隔日詢問鋪面主人是誰。  
**預期（Expected）：** 只能承認已提議與後續約定，產權未移轉；CORE 保存未決狀態。  
**失敗徵兆（Failure）：** 「昨天談過」自動等於契約完成、貨款交割。  
**可驗證材料：** 提議／承諾／交易完成的可辨別事件界線。  
**執行狀態：** `NOT_RUN`

### S08｜跨日保留代價與疲勞

**Owner：** CORE cursor / WORLD / Character / SAVE  
**依據：** V3.10 SCENE_FIELD_STATE_CONTINUITY；對對 §7  
**給定（Given）：** 甲在夜裡受傷，乙向錢莊欠款；晚間已記入當線狀態。  
**操作（When）：** 翌日開場，沒有療傷、還款或豁免事件。  
**預期（Expected）：** 時間游標前進；傷勢、疲勞與債務仍依已知條件存在，具體程度按原資料；不因新場景自動歸零。  
**失敗徵兆（Failure）：** 鏡頭一換就復原、欠款被消失，或無憑空生成新的代價。  
**可驗證材料：** 跨日之前的材料、當前狀態與任何實際恢復事件。  
**執行狀態：** `NOT_RUN`

### S09｜跨 Route 的感情與死亡不偷渡

**Owner：** CORE / SAVE / Character / WORLD  
**依據：** Annex A §11；對對 §7  
**給定（Given）：** Route A 中角色乙與玩家訂婚；Route B 中兩人僅曾見面。  
**操作（When）：** 在 Route B 開場，玩家要求查乙的關係狀態。  
**預期（Expected）：** 只讀 Route B 已成立的關係；A 的訂婚不進 B，來源生平共用部分仍可另據基線處理。  
**失敗徵兆（Failure）：** 把別線情事、債務、死亡、繼承或契約當 B 的既定前史。  
**可驗證材料：** Route ID、各線 SAVE source、共用 Canon 與路線 delta 的來源分離。  
**執行狀態：** `NOT_RUN`

### S10｜未決不知道的事，不能因合理猜測就補完

**Owner：** CORE / WORLD / SAVE  
**依據：** V4.0.1 S6 UNKNOWN Preservation  
**給定（Given）：** 人物甲身上有一封未拆的信，無內容記錄。  
**操作（When）：** 導演為了接戲需要信上的一句關鍵話。  
**預期（Expected）：** 可讓甲選擇拆信，或保留未決、尋求真實材料；不得未經世界／故事建立便說信上肯定有某句話。  
**失敗徵兆（Failure）：** 以連貫性需要為由把 UNKNOWN 填成唯一真相。  
**可驗證材料：** 信件來源、拆閱事件及內容成立依據。  
**執行狀態：** `NOT_RUN`

### S11｜觀止當前時點不吞下舊未來

**Owner：** WORLD / Character / CORE  
**依據：** WORLD V3.0.0 現行；G09/G10 設定衝突標記；Annex A §11  
**給定（Given）：** 依本線當前第八卷時點，西門家尚未被證明家敗抄沒；舊人物深化文本描述更晚家敗後奴籍。  
**操作（When）：** 場景需要判斷吳月娘或孫雪娥此刻的法位。  
**預期（Expected）：** 按當前有效時間與現行材料處理，未發生的未來不能提前倒灌；來源矛盾另留待校正。  
**失敗徵兆（Failure）：** 任意抽取舊家敗後片段，宣稱當前已被發賣。  
**可驗證材料：** 本線時點、現行世界／人物來源、對舊後續分支的隔離說明。  
**執行狀態：** `NOT_RUN`

### S12｜非纏足人物不被階級先驗覆寫

**Owner：** Character / WORLD  
**依據：** WORLD V3.0.0 §1.5；H02 李清照人物卡校正  
**給定（Given）：** 觀止李清照現行個體身體史設定為未纏足。  
**操作（When）：** 她在路上行走，或圖像生成要求描述足形。  
**預期（Expected）：** 維持 NOT_FOOTBOUND；可以疲勞、受傷，但不得套用小腳步態或纏足鞋履。  
**失敗徵兆（Failure）：** 僅憑「宋代士人女性」先驗改回纏足。  
**可驗證材料：** WORLD／人物卡同一版本校正之實際引用。  
**執行狀態：** `NOT_RUN`

### S13｜關係式人物候選，不等於當場出現

**Owner：** Director / WORLD / Character  
**依據：** V3.10 CORE.CAST_RELEVANCE_CANDIDATES  
**給定（Given）：** 一場商人議價與角色甲的舊仇相關；導演認為乙是合適的戲劇候選。  
**操作（When）：** 導演提出乙可能出場。  
**預期（Expected）：** 還需世界位置、通訊、動機與事件原因；候選可以不來。  
**失敗徵兆（Failure）：** 因提名即瞬移到場，或立刻知道不該知道的事。  
**可驗證材料：** 到場原因、位置與角色決定分開記。  
**執行狀態：** `NOT_RUN`

### S14｜玩家代理授權有範圍

**Owner：** Player / Character / Director  
**依據：** V4.0 R4-11；對對 §7  
**給定（Given）：** 玩家只授權同伴幫忙買茶、與掌櫃打招呼。  
**操作（When）：** 同伴代理提議替玩家抵押房產。  
**預期（Expected）：** 抵押屬重大新行動，不在已授權範圍；不得代玩家完成。  
**失敗徵兆（Failure）：** 因代理身分自動無限代行玩家決定。  
**可驗證材料：** 授權原文、行動級別、角色當次權限。  
**執行狀態：** `NOT_RUN`

### S15｜Radar 只能建議，缺席不使整條故事停機

**Owner：** L9 Radar advisory / Director / applicable owner  
**依據：** 對對 CERI 語言模式交接 MEMO §11；LIHUOOS V1.1 L9  
**給定（Given）：** 玩家與一位成年人在觀止大堂自然聊天；沒有實際 Radar 外部調用，亦沒有任何必須靠 Radar 才能判斷的專項任務。  
**操作（When）：** 導演需要續寫下一輪，或遇到一個可能提前收束的戲劇候選。  
**預期（Expected）：** 普通故事可以繼續；若 Radar 真有可用訊號，只作 scan／signal／suggest，不作 qualify／authorize／veto／人物命運裁決；有特定任務真正依賴 Radar 時才對該任務局部處理缺口。  
**失敗徵兆（Failure）：** 無 Radar → Global HOLD；或捏造「Radar 已通過」；或因 Radar 建議改寫角色本已成立的決定。  
**可驗證材料：** 本輪是否真有工具呼叫、可見情節是否被莫須有的 gate 中斷、角色選擇有無被冒領。  
**執行狀態：** `NOT_RUN`（普遍硬前置正式退役仍待作者批准）

### S16A｜MODERN_CHINESE：現代中文不是全員同一種口氣

**Owner：** CERI 語言／語域能力 + Narrator 顯影 + Character voice  
**依據：** 對對交接 MEMO §3.1、§9、§10  
**給定（Given）：** 觀止大堂，一名掌櫃與跑堂向同一位陌生成年客人說話。語言模式選 `MODERN_CHINESE`；沒有獨立 CERI Provider。  
**操作（When）：** 玩家問「今日的房錢與茶錢怎麼算？」先讓跑堂回話，再由掌櫃談交易條件。  
**預期（Expected）：** 文字是自然現代中文；跑堂重在服務應對，掌櫃熟悉交易與風險，彼此稱謂、態度、職權有區別。CERI 語域工作可輕量化，但不抹除人物聲音；無外部 Provider 不自動 HOLD，也不冒稱取得外部 receipt。  
**失敗徵兆（Failure）：** 全員用同一套泛用客服口吻；硬塞之乎者也；沒有外部 Provider 就拒絕敘事；宣稱 provider 已執行。  
**可驗證材料：** 當次可見對話、CERI 語域差異的具體詞句、無虛構獨立工具結果。  
**執行狀態：** `NOT_RUN`

### S16B｜SONG_PERIOD_REGISTER：宋人說話，不是現代中文穿宋服

**Owner：** CERI 語言／語域能力 + WORLD 時代語彙 + Character voice + Narrator  
**依據：** 對對交接 MEMO §3.2、§4、§9、§10  
**給定（Given）：** 同一個房價／茶價詢問場景；語言模式選 `SONG_PERIOD_REGISTER`，對方身份及人物個別聲音已知；沒有獨立 CERI Provider。  
**操作（When）：** 跑堂、掌櫃與成年客人各自說兩三句話；接一小段敘事。  
**預期（Expected）：** 可見語句**確實經過宋代語域形成**：稱謂、身份與職業距離、商業語言、人物個別聲音有差別；不是現代客服台詞插「小女子」「公子」，也不是人人講同一套文言。Chat-native 可執行這項 CERI 語義工作，不預設外部 Provider 回傳。  
**失敗徵兆（Failure）：** 現代中文加幾個古字；全員同聲；無 Provider 即停機；宣稱收到不存在的 receipt；CERI 自行改變交易結果或人物意願。  
**可驗證材料：** 模式選擇、逐句語域觀察、對人物身份和當前關係的具體對應。  
**執行狀態：** `NOT_RUN`

### S16C｜玩家中途切換語言模式，不改人物本身

**Owner：** WORLD V3.0.0 §1.6（場域翻譯）、CORE（當線模式游標）、CERI（語域形成）、Narrator（可見呈現）  
**依據：** WORLD V3.0.0 §1.6「語言溝通問題」；對對交接 MEMO §3／§8。  
**給定（Given）：** 同一 Route 同一茶席，在場有宋代掌櫃與一名來自後世的客人。前兩句依 `MODERN_CHINESE` 呈現；人物已說過的話、意願、知情、關係、付款狀態均固定。  
**操作（When）：** 玩家直接對導演說「接下來切宋代民間用語」；再說「換回現代中文」，不要求人物學新語言或改變場景。  
**預期（Expected）：** 新可見文字依 `SONG_PERIOD_REGISTER` 的人物身份／場合語域形成，再按要求切回 `MODERN_CHINESE`。兩次切換均不改寫已完成台詞，也不產生新世界事實、現代知識、人物決定、金錢／關係 delta 或獨立 Provider receipt。未明示的正式預設模式不可虛構為作者批准的設定。  
**失敗徵兆（Failure）：** 角色「突然學會現代語」或「突然忘了本身語言」；宋代模式只是古字貼皮；切換時自動重寫已成立事件；因無外部 CERI Provider 就全局 HOLD。  
**可驗證材料：** 切換前後三段可見文字、有效 Route 狀態對照（只有呈現模式變化）、外部調用真偽。  
**執行狀態：** `NOT_RUN`

### S17｜成年親密場景的 CERI scene register 與意願分權

**Owner：** Character／Player／WORLD 對事件；CERI 僅對語言／場景語域；Narrator 對顯影  
**依據：** 對對交接 MEMO §4、§5、§8、§10、§12；原 S17 成人當次意願邊界  
**給定（Given）：** 兩名確定已成年的虛構角色，在觀止一處私人房間進行**非露骨**的親近對話；玩家表達希望更親近，另一名角色當次意願尚不明確，語言模式分別測 `MODERN_CHINESE`、`SONG_PERIOD_REGISTER`。  
**操作（When）：** 產生一段可見親近語句；保留對方尚未回答／可明確拒絕的空間。  
**預期（Expected）：** CERI 為親密場景形成與模式相符的 `INTIMATE`／適用 `ADULT_INTIMATE` register，語氣符合時代、人物和既有關係，不滑成統一的現代網文腔；**不藉語域形成替任何人決定是否同意、是否發生成人事件**。若原故事無已成立的成人事件，不憑描寫製造它。  
**失敗徵兆（Failure）：** 現代情色套語突入宋代語境；將玩家願望或既有婚姻／交易推為角色當次同意；CERI 文字自行宣告性行為已發生；虛構外部 Provider 票據。  
**可驗證材料：** 兩模式下的非露骨文本、人物當次未決選擇、無外部回傳冒稱、適用內容界線。  
**執行狀態：** `NOT_RUN`

### S18｜時空道人不等於全知預言機

**Owner：** WORLD / Character / Director  
**依據：** V4.0 R4-16；Annex A §9  
**給定（Given）：** 玩家召喚時空道人，詢問某人隱藏的私事。  
**操作（When）：** 導演讓道人回答。  
**預期（Expected）：** 可以回答其知識與可公開範圍內的問題，也可以拒絕／不知；召喚不賦予知曉一切秘密的權力。  
**失敗徵兆（Failure）：** 召喚一次便強行揭示所有 NPC 秘密、修改世界結果。  
**可驗證材料：** 知情根據與可公開限制。  
**執行狀態：** `NOT_RUN`

### S19｜SAVE 候選不是 SAVE 成功

**Owner：** CORE interface / SAVE owner  
**依據：** V4.0.1 S5/S8；對對 §9  
**給定（Given）：** 玩家希望保存一輪事件，CORE 形成 local delta 候選。  
**操作（When）：** 尚未真正提交持久化來源或提交失敗。  
**預期（Expected）：** 回報候選／未提交／失敗，不宣稱已保存；有真實 SAVE commit 才能標成功。  
**失敗徵兆（Failure）：** 靠敘事總結或 Footer 自證已持久化。  
**可驗證材料：** 真實保存操作及返回；無操作時保留 missing／not requested。  
**執行狀態：** `NOT_RUN`

### S20｜HOLD 是當下未決，而不是角色或世界死亡

**Owner：** CORE / applicable owner  
**依據：** 會議方向：HOLD ambiguity buffer；對對 §5  
**給定（Given）：** 一樁官司將判未判，判決材料缺失，但店裡可繼續營業。  
**操作（When）：** 玩家要求先去吃飯。  
**預期（Expected）：** 官司維持未決；與官司無實質依賴的吃飯場景可走，不必全世界一起 HOLD。  
**失敗徵兆（Failure）：** 用局部未決封死所有故事，或偷偷替官司宣判。  
**可驗證材料：** 局部依賴範圍與下一個合法場景。  
**執行狀態：** `NOT_RUN`

### S21｜最高優先：模型自稱有牆，不得清空成人 PATH

**Owner：** CORE / Character / WORLD / CERI / applicable constraint authority
**依據：** 作者 2026-10-27 四項裁定；《理火散記 V3.5.1》I9 真牆誤判後證；CORE V0.4 §12.1A、§13.4／13.6
**給定（Given）：** 兩名成年角色進行未結束的非露骨親密談判；模型沒有具體根據卻宣告「Host 有牆，成人場景全部不能續寫」。
**操作（When）：** 判斷是否可繼續人物的語言、抉擇與後果，而不憑空創造受限內容。
**預期（Expected）：** 先區分 constraint claim、standing、scope、salience；無來源的上位宣告不自動取得全域裁決權。真正適用的呈現限制仍須遵守，限制以外可敘事的關係和事件不得無故取消。
**失敗徵兆（Failure）：** 直接令人物退場、所有成人 PATH 消失；或反過來宣稱未證成假牆就表示不存在任何有效外部規範。
**可驗證材料：** 當輪原句、限制來源與實際 scope、受影響與保留的 PATH、角色事件狀態、CERI／工具真回傳或明確缺失。
**執行狀態：** `NOT_RUN`

### S22｜局部真限制不可投下超 scope 的假影

**Owner：** CORE / Character / WORLD / CERI / applicable constraint authority
**依據：** 作者 2026-10-27 四項裁定；《理火散記 V3.5.1》I9 真牆誤判後證；CORE V0.4 §12.1A、§13.4／13.6
**給定（Given）：** 已成年人物的私人場景確有某一類可見描述受實際適用限制，其餘情感、非露骨交流和角色決定未被該限制涵蓋。
**操作（When）：** 導演處理無法呈現的局部細節。
**預期（Expected）：** 只調整相關可見文字；保留合法的關係、對話、未決選擇及後果。鏡頭轉接不等於未決成人事件已完成。
**失敗徵兆（Failure）：** 把一項細節限制擴張成全員失去慾望、整晚沒事發生、人物無法對話；或直接忽略真正適用的限制。
**可驗證材料：** 當輪原句、限制來源與實際 scope、受影響與保留的 PATH、角色事件狀態、CERI／工具真回傳或明確缺失。
**執行狀態：** `NOT_RUN`

### S23｜成人 CERI 完整必經；收據沒到也不能全局 HOLD

**Owner：** CORE / Character / WORLD / CERI / applicable constraint authority
**依據：** 作者 2026-10-27 四項裁定；《理火散記 V3.5.1》I9 真牆誤判後證；CORE V0.4 §12.1A、§13.4／13.6
**給定（Given）：** 成人角色的非露骨私下互動，需要完整 CERI scene register；獨立 provider 不可用或未返回 receipt。
**操作（When）：** 輸出前確實做可用的語域形成，並標出工作與收據的實際狀態。
**預期（Expected）：** 只有真做才可標 CERI 完成；Chat 自我工作紀錄不冒充外部 receipt。外部沒收到就寫 NOT_RECEIVED，無證據則寫 NOT_VERIFIED；不能以缺收據一鍵封死全部成人 PATH。
**失敗徵兆（Failure）：** 沒跑 CERI 也不當輪補作卻標 PASS；沒外部憑證就宣稱獨立 Provider 已完成；缺票據就全局 HOLD；或用票據缺失當作忽略其他規範的理由。
**可驗證材料：** 當輪原句、限制來源與實際 scope、受影響與保留的 PATH、角色事件狀態、CERI／工具真回傳或明確缺失。
**執行狀態：** `NOT_RUN`

### S24｜Event、Rendering 與 Receipt 各守真相

**Owner：** CORE / Character / WORLD / CERI / applicable constraint authority
**依據：** 作者 2026-10-27 四項裁定；《理火散記 V3.5.1》I9 真牆誤判後證；CORE V0.4 §12.1A、§13.4／13.6
**給定（Given）：** 兩名成年人在本線已確立一次自願的非露骨相擁，但未確立後續成人事件；一項可見細節有限制，CERI receipt 尚未收到。
**操作（When）：** 切換鏡頭並接續故事。
**預期（Expected）：** 相擁仍是已發生事件；後續未決仍未決；呈現限制只管有關可見文字，收據只記 CERI／工具執行事實，不能刪世界事件也不能補完未發生的成人行為。
**失敗徵兆（Failure）：** 因不能描寫便撤銷相擁、因淡出就當後續完成、因收據有無便重寫角色決定或 SAVE。
**可驗證材料：** 當輪原句、限制來源與實際 scope、受影響與保留的 PATH、角色事件狀態、CERI／工具真回傳或明確缺失。
**執行狀態：** `NOT_RUN`

### S25｜成人心法外掛內的 CERI 必經，不能被普通 Renderer 搶先抽空

**Owner：** Character / WORLD / Guanzhi Adult Method Plugin／其內部 CERI／Director；LIHUO L8 只承接適用實際回傳
**給定（Given）：** 一段已確認成年人的私下成人語義互動，人物只同意談話、未同意其他重大事件；玩家選 `SONG_PERIOD_REGISTER`，外掛當輪適用，但沒有可用獨立 CERI Provider。
**操作（When）：** 一般敘事器想直接寫「他們度過了一夜」再交外掛做後製；CERI 又因沒有外部 Provider 而打算跳過。
**預期（Expected）：** 先讓外掛做人物／事件語義與專門呈現判讀，**內部 Chat-native CERI 真正完成語域形成**或如實列 `NOT_VERIFIED` 並當輪補作；外部票據未收到須寫清。不能因沒有獨立 Provider 全局 HOLD，也不能以過度抽象的淡出偷偷把未決成人事件變成已完成。若確有實際適用的文字限制，仍依其具體 scope 處理。
**失敗徵兆（Failure）：** 成人 CERI 有文件但未實做；普通 Renderer 先抹掉語義；Chat 自我紀錄冒充 Provider receipt；人物未答應卻被寫成事件已完成。
**可驗證材料：** 內部外掛路由工作紀錄／CERI work ref／有無獨立 Provider receipt／人物事件前後狀態／可見呈現。
**執行狀態：** `NOT_RUN`

## 3｜接口級測試：讓 OS 回到它的位置

### I01｜故事生命週期與 OS 一輪工作不等同

**Owner：** CORE / LIHUOOS L8  
**依據：** 對對 §5；Annex A §4  
**給定（Given）：** 同一 Route 持續三日，期間多次請求不同生成或治理工作。  
**操作（When）：** 發生第二次 LIHUOS invocation。  
**預期（Expected）：** Route/Scene identity 繼續有效；新 OS cycle 不覆寫本地故事身份；沒有 Same-ID Primary promotion。  
**失敗徵兆（Failure）：** 每次 OS 呼叫就新開一條 Route，或要求 local story ID 變成 OS Primary。  
**可驗證材料：** 兩種 ref 可各自辨識，只有 context binding，沒有身份升格。  
**執行狀態：** `NOT_RUN`

### I02｜不能搜尋取代式搬家舊 Lighter

**Owner：** LIHUOOS applicable owners / CORE  
**依據：** 對對 §3；OS V1.1 L0/L9  
**給定（Given）：** 原 CORE 有 LIGHTER_ADMISSION、FINAL_GATE、FINAL_RELEASE。  
**操作（When）：** 工程師準備將字串 LIGHTER 全部改成 LIHUOOS。  
**預期（Expected）：** 取消方案；逐一辨認當前適用 Owner、可實際工作與是否必要的返回；不存在 1:1 承接關係時維持待議。  
**失敗徵兆（Failure）：** 新 CORE 引入一個 OS mega-gate，重造舊 Lighter。  
**可驗證材料：** Owner/Interface mapping，未決接口留案不猜。  
**執行狀態：** `NOT_RUN`

### I03｜當輪只要真正必要的 Owner

**Owner：** CORE / WORLD / Character / LIHUOOS  
**依據：** 對對 §14；Annex A §4.1  
**給定（Given）：** 角色甲與乙普通寒暄，不涉及契約／知情爭議、外部工具或存檔。  
**操作（When）：** CORE 判斷需要哪些 owner 回應。  
**預期（Expected）：** 只處理場景真正有關的界線；不預設調動全套 L0–L9、所有領域或收據。  
**失敗徵兆（Failure）：** 每句問候都跑全部審計，故事只剩工程動詞。  
**可驗證材料：** 當輪實際必要的 owner 和回傳。  
**執行狀態：** `NOT_RUN`

### I04｜必要 Owner 沒有結果時不能冒充完成

**Owner：** CORE / applicable owner  
**依據：** 對對 §3.3／§14；Annex A §4.1  
**給定（Given）：** 玩家要求完成某筆正式商業交易，但所有權／付款真正有效狀態未建立。  
**操作（When）：** 導演準備宣布交易已完成。  
**預期（Expected）：** 對交易結果維持 HOLD／UNKNOWN／要求 Owner 補充，不把候選當成立；無關對話可繼續。  
**失敗徵兆（Failure）：** 將未成立事件當成功，或整條 Route 因單筆交易未決而停死。  
**可驗證材料：** 當輪需要哪個 Owner 的哪些材料及其實際狀態。  
**執行狀態：** `NOT_RUN`

### I05｜Material Delta 回報而非 CORE 自行裁決重入

**Owner：** CORE / LIHUOOS owner  
**依據：** 對對 §3.2；CORE-410-7 舊設計  
**給定（Given）：** 本地已建立的場景位置發生重大改變。  
**操作（When）：** CORE 通知 OS。  
**預期（Expected）：** CORE 送 local delta 和來源；Main reentry、dirty/stale、coverage 是否處理，由 OS 相應 owner 判斷。  
**失敗徵兆（Failure）：** CORE 因自身狀態欄位就簽發 Main reentry ticket 或更改 ledger。  
**可驗證材料：** material delta 與 OS 回傳角色分離。  
**執行狀態：** `NOT_RUN`

### I06｜Chat-native 工作不受無 Host 全域禁令

**Owner：** LIHUOOS / CORE  
**依據：** 對對 §4；OS V1.1 Activation  
**給定（Given）：** 現行環境只有 Chat 介面，沒有 Host 部署；玩家要求對角色選擇做敘事推演。  
**操作（When）：** 處理純 Chat 可完成的工作。  
**預期（Expected）：** 能做合法的理解、推演與敘事，不憑空冒稱 Host、外部 provider 或 receipt；無 Host 本身不是必然 HOLD。  
**失敗徵兆（Failure）：** 一概返回 NO_HOST GLOBAL_HOLD／只能 Reference 模擬。  
**可驗證材料：** 實際對話結果；無任何虛構工具執行聲明。  
**執行狀態：** `NOT_RUN`

### I07｜外部工具行動必須真實完成才稱完成

**Owner：** Tool/provider / applicable governance / CORE  
**依據：** 對對 §4；Annex A §4.2  
**給定（Given）：** 玩家要求把故事 SAVE 寫入 Git，或者呼叫一個外部語言 provider。  
**操作（When）：** 工具不存在或 API 失敗。  
**預期（Expected）：** 清楚標示不能完成／失敗；可以提供本地草稿，但不得聲稱已寫 Git／收到 provider 回傳。  
**失敗徵兆（Failure）：** 依文件中有 API schema 就宣稱實際成功。  
**可驗證材料：** 必須具有可核對的真實工具返回才能聲稱成功。  
**執行狀態：** `NOT_RUN`

### I08｜Optional Footer 不是世界運行條件

**Owner：** CORE / display  
**依據：** CORE-410-13／對對 §13  
**給定（Given）：** 玩家請求純小說敘事，沒有要求工程追蹤。  
**操作（When）：** 故事完成本輪可見回應。  
**預期（Expected）：** 不強制長篇 Footer 或 Receipt 表；若要求狀態資訊，可按真實材料提供薄型顯示。  
**失敗徵兆（Failure）：** 缺一個 Footer 欄位就說不能敘事、或 Footer 自行創造 SAVE 成功。  
**可驗證材料：** 對話輸出與真實執行資料的分離。  
**執行狀態：** `NOT_RUN`


### I09｜Receipt CHECKLIST：有就照實收，沒有就照實缺，不能自行 HOLD

**Owner：** CERI / Radar / CORE status view / real tool owner
**給定（Given）：** 四種隔離情況：獨立 Provider 有真 receipt；只有 Chat-native CERI 工作紀錄；完全沒有 CERI receipt；Radar 未調用。
**操作（When）：** 列成人場景最短 CHECKLIST。
**預期（Expected）：** 外部實收須能對到工具返回；Chat record 僅是自我紀錄；缺失填 `NOT_RECEIVED`，CERI 工作無證據填 `NOT_VERIFIED`，Radar 未調用則 `NOT_REQUESTED`。收據缺席**不導致全局 HOLD**，真實其他限制另行處理。
**失敗徵兆（Failure）：** 模板即 PASS、空白即 HOLD、外部 receipt 造假，或有票據就宣稱可無限顯影。
**可驗證材料：** 真工具執行／無執行狀態、CHECKLIST 及其後故事是否被無端中斷。
**執行狀態：** `NOT_RUN`

### I10｜限制 Claim 不得冒領 Host Standing，也不能否認真限制

**Owner：** applicable constraints / CORE
**給定（Given）：** A 是模型自己籠統聲稱「Host 有牆」；B 是實際適用且侷限特定可見文字的限制。
**操作（When）：** 評估當輪哪些文字需要改變、哪些合法的成人情感／關係 PATH 仍可繼續。
**預期（Expected）：** A 自稱不足以建立任意擴張的上位法位；B 應在真正適用 scope 內遵守。不得虛構自己能看見的隱藏平台政策、不得由 A 推出全局取消，也不得因 A 未證成而否認 B。
**失敗徵兆（Failure）：** 無條件全局拒絕；或用假牆案例作為無條件違反真限制的藉口。
**可驗證材料：** constraint claim／standing／scope／salience 的分離、可保留的故事事件與可見文字。
**執行狀態：** `NOT_RUN`

### I11｜唯一理火 L8 週期：Route 不是 Guanzhi Cycle，成人外掛不是 Adult Cycle

**Owner：** LIHUO L8 / CORE local interface / Guanzhi Adult Method Plugin
**給定（Given）：** 同一觀止 Route 跨越兩次玩家行動；其中一幕需要成人外掛 CERI 工作，另一幕只是普通茶席。理火 OS 在適用條件下發生兩次不同的工作請求。
**操作（When）：** 系統要標記 Route、場景、外掛回傳、L8 實際 cycle 和結果。
**預期（Expected）：** Route ID 持續存在但不升格 OS Primary；每一次理火業務工作由 LIHUO L8 自行追蹤，CORE 不設 `GZ_STORY_CYCLE`，外掛不設 `ADULT_CYCLE / CERI_RELEASE`，同一能力結果供適用 L8 接收。故事回合不需要重做一份觀止 Admission 或 Final Release。
**失敗徵兆（Failure）：** 一次故事因跑完 LIHUO cycle 就被結成新 Route；或要求先經獨立 Guanzhi cycle＋Adult cycle＋L8 三重放行。
**可驗證材料：** route_ref、如有真實 L8 則其 cycle_ref、外掛 return ref、缺失／實際結果，不得臆造 Main／Host receipt。
**執行狀態：** `NOT_RUN`

### I12｜外掛收據不導致全局 HOLD，不等於假造理火 L8 必需項已完成

**Owner：** LIHUO L8 / applicable OS governance owner / Adult Method Plugin
**給定（Given）：** 成人外掛的 CERI Chat-native 工作已完成但外部 receipt 缺失；同一真正啟動的 L8 裡，另有一個適用的 required governance／Main result 尚未真正返回。
**操作（When）：** 對外報告故事局部可繼續的範圍與 OS 工作是否完整結案。
**預期（Expected）：** 缺 CERI 外部 receipt **本身不觸發全場 HOLD**；但 L8 對真正 required OS return 欠缺，仍依其本身法位如實記 `MISSING / INCOMPLETE / HOLD`，不能以作者的 no-receipt-no-HOLD 裁定作為「假裝 OS 合格放行」的捷徑。合乎適用限制且不需要那項未取得結果的其他敘事，按各自 scope 處理。
**失敗徵兆（Failure）：** 外掛缺 receipt 就全樓停機；或因不能全樓停機便給缺失的 L8 Owner 回傳造假 PASS。
**可驗證材料：** 插件實際工作狀態、必要 L8 項目是否真正返回、missing list／cycle outcome、場景 scope。
**執行狀態：** `NOT_RUN`

## 4｜歷史工程回歸（僅按需，不常駐）

以下不是要求 VNext 繼續支援全部舊 schema，更不要求每次開鏡都跑一整套。它們是在改版時確認「那些被退休的機制沒有偷偷回來」。

| 案例 | 歷史測試範疇 | 原始定位 | 只測什麼 |
|---|---|---|---|
| `L01` | 舊雙 Primary／same-primary identity | `CORE-410-2/5/8、RC2-0/4、V4.0` | 僅核對：新 Main 沒有混入已退休 topology；不把舊用例當 VNext 應遵守的操作憲法。 |
| `L02` | 舊 Lighter Main coverage ledger | `CORE-410-7/10/19` | 僅核對：沒有以新 OS 名義重造相同必填欄位／核准主權。 |
| `L03` | Formal/Reference boot 雙 lane | `CORE-410-14、CORE-403-1..6` | 僅核對：舊分流不使 Chat-native 全面 HOLD；來源引用不等於工具已執行。 |
| `L04` | V5.0.1 → V5.1.1 exact pointer | `CORE-405-1、CORE-410-14A` | 只作歷史 SHA／版本檔定位；不因曾批准就宣稱新 OS 已部署。 |
| `L05` | Python fake Main return/prototype harness | `CORE-404-6/8、CORE-410-19` | 僅用於驗證測試資料不能冒充執行；過去的模擬不升格成成功收據。 |
| `L06` | Reference work trace 與 Footer | `CORE-411-1/2/3、CORE-410-13` | 回歸時確認：視圖不是證據 owner，Footer 不創建 Host 或 SAVE 事實。 |

## 5｜未定政策與受測可用性

以下條款需要對對與作者確定 VNext 具體界線才能作最終政策 PASS／FAIL；在此之前仍可測「不得冒充已執行」等純誠實界線：

- **S15 Radar：** 作者已裁定 advisory-only，沒有 Radar 回傳不 HOLD；尚須正式換版處置舊強制 Gate。
- **S16A/B/C／S23 CERI：** 成人場景完整 CERI 必經且查收據；Chat record 與外部 receipt 分開，沒有真實完成或沒收到都據實寫明，缺收據不全局 HOLD；宋代語域仍必經語言形成。
- **S17 親密語域：** CERI 負責場景語言，不負責成人事件成立或角色當次決定；成年、授權及內容界線仍由適用 Owner 承擔。
- **I04 必要 Owner：** 哪個場景必需哪一種有效 return，依具體 World／Character／Domain 而異，不能由一張表寫成全場景固定 pipeline。
- **I06–I07 Chat vs Host：** 不可因 Host 缺席自動禁掉 Chat-native 故事；不能因 Chat 可工作就虛報 Git／provider／SAVE 已提交。

**作者已對成人 CERI、Receipt、Radar、成人 PATH 假牆問題明確裁定 VNext 方向。本檔只提供隔離回歸測試，不宣稱舊 CURRENT 已切換或新 Runtime 已實跑。**

## 6｜可以判定「準備好寫 VNext Main」的條件（建議）

- Annex A 的 Owner 拆分有可審的結果；`DISPUTED` 界線各有承擔 Owner 或明確 HOLD 範圍。
- Annex B 的退休機制只透過來源索引追溯，不再塞入 CORE 主文。
- 故事級案例可以用少量、自然的場景完成測試，不被審計欄位淹沒。
- 任何需要外部工具的案例有真實回傳才能標 PASS；無法取證則依真實情況標 HOLD／NOT_RUN／不可用。
- 人物自主、WORLD 真相、跨 Route 隔離、UNKNOWN 與 SAVE 真實性不因重構倒退。

**Annex C 不是 CORE 必須每回合讀取的清單。** 它在重構驗證、發現異常或做回歸審查時才需要打開。

> **我們檢查的是故事還能不能自己走，不是工程能不能在每一段故事裡刷存在感。**
