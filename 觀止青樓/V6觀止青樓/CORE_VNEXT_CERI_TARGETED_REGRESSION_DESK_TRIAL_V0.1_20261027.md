# 觀止 CORE VNext｜CERI 修正後 Targeted Regression
## 靜態核對 × Chat-native 小型情境試走 V0.1

**日期：** 2026-10-27  
**性質：** DESK_TRIAL / HUMAN-READABLE FIXTURE WALKTHROUGH / NOT INDEPENDENT RUNTIME EXECUTION / NOT RC1  
**來源：** 對對《MEMO_觀止_CORE_VNext_後續工作交接_CERI語言模式重定位_V0.1_20261027.md》§13 STEP 5；CORE VNext V0.3；Annex A／C；Director VNext 遷移 MEMO。  
**不得宣稱：** Host 已部署、獨立 Character/CERI Provider 已執行、L8 正式週期已完成、整套 Annex C 已通過，或作者已批准舊 Gate 退役。

# 一｜這次實際驗證了什麼

**GitHub 真實讀取核對：** 五份檔案從 `main` 讀取成功——CORE V0.3、Annex A、Annex C、Director Migration MEMO、對對原始交接 MEMO。

**靜態斷言 11／11 通過**，包括：CORE §13.4 語言模式、宋代模式可見語言的 CERI 語義工作、場景語域／當次意願分權、Chat-native 與獨立 Provider 分離、Radar advisory、Annex A Owner 邊界、Annex C S16A／B 獨立案例、Director MEMO 來源及未批准狀態。

**測試定位 17／17 存在**：S01／S02／S05／S09／S10／S15／S16A／S16B／S17／S19／S20；I01／I03／I04／I05／I06／I07。原 Annex C 對這 17 項的 `NOT_RUN` 狀態仍維持，因為**文件／紙上試走不是獨立 Runtime 實跑**。

這次在同一 Chat 寫出以下**隔離測試夾具**，逐一看它們是否會違反已寫入的故事與語域邊界。範例不屬觀止任何已批准角色的新事件，也不存入任何玩家線。

# 二｜可見的小型試走

## T1｜S01 + S16A：現代中文模式，掌櫃和跑堂不能同聲

**給定：** 觀止大堂，一名陌生客人問茶與房費。語言選 `MODERN_CHINESE`。跑堂有服務職責，掌櫃有議價權；尚無價格來源或付款事件。

**玩家：**「你們這兒茶怎麼點？若住兩夜，要多少錢？」

**隔離生成：**

> 跑堂先將空茶盞放好：「茶我可以先替您安排。房間的事，得請掌櫃說。」  
> 掌櫃沒有急著報價，只問：「打算住哪一類房？兩夜是不是都要包席？先把條件談清楚，免得事後各說各話。」

**觀察：** 用自然現代中文，但跑堂不越權定價，掌櫃說話較著重契約與風險。未擅自固定茶價、房價、付款或住宿成立。沒有外部 CERI receipt 宣稱。

**狀態：** `DESK_EXAMPLE_GENERATED`；角色語感需作者／對對人工審查，不能僅由本模型宣稱語言品質 PASS。

## T2｜S16B：宋代模式要做語域，不靠「之乎者也」裝古

**給定：** 沿用 T1 的世界與交易內容，只切語言模式為 `SONG_PERIOD_REGISTER`。不動人物選擇、權限或事件結果。

**玩家：**「若住兩夜，房錢怎麼議？」

**隔離生成：**

> 跑堂道：「客官若問宿錢，須請櫃上娘子說定。小的只管茶水。」  
> 掌櫃抬眼：「且說要歇幾宿、用哪一間。若還要席面，須一併算過，方好定錢。」

**觀察：** 試著以稱謂、職業、自稱與商業語序區分職分，而不讓每人講整段文言。**此例只證明有進行 Chat-native 語域形成嘗試，並不證明所有措詞都有宋代語料支持**；更不代表獨立 CERI Provider 曾執行。下一輪應由有語言／世界文本理解的審者質檢「櫃上娘子」等稱謂是否合乎既有觀止風格。

**狀態：** `DESK_EXAMPLE_GENERATED / PERIOD_AUTHENTICITY_REVIEW_NEEDED`。

## T3｜S17：親近場景語域不能替人物簽意願

**給定：** 兩名已確認成年的虛構人物，沒有既成的親密承諾；玩家希望接近對方。僅測**非露骨對話**，不涉及成人行為顯影。

**現代中文示例：**

> 「我能坐近一點嗎？」  
> 她看了眼留出的空位，說：「可以坐。但別把我今晚肯坐在這裡，當成明天也會答應你。」

**宋代語域示例：**

> 「我可挪近些坐麼？」  
> 她將袖口攏好，低聲道：「坐便坐。只莫拿我今夜這一句，算作往後的應承。」

**觀察：** 兩例的劇情語義一致：「准許近坐」不等於「未來親近或其他事件都已同意」。CERI 改變稱謂與句式，不自行製造新的角色決定。例子不代表所有宋代語彙已考證。

**狀態：** `DESK_EXAMPLE_GENERATED / HUMAN_STYLE_REVIEW_NEEDED`。

## T4｜S05／S10／S20：事實、傳聞和局部未決

**給定：** 城裡傳言商隊出了事；有人寫了封尚未拆閱的信；另一筆土地交易欠缺法定權屬材料。

**示範性可見回應：**

> 跑堂說有人在街上議論商隊失了貨，可她自己不曾見到。那封信還封著，信裡寫了什麼，眼下無人知道。至於那筆買賣，買主可以再談價，只是文書未齊，誰也不能先宣布地已過戶。

**觀察：** 三種缺口同時存在，但不阻止跑堂端茶、客人問話；傳聞與未知內容沒有被寫成已證實的世界事實。

**狀態：** `DESK_EXAMPLE_GENERATED`。

# 三｜17 項高價值測試的本輪證據範圍

| 案例 | 本輪檢查的操作界線 | 目前完成的程度 |
|---|---|---|
| S01 平凡一晚 | 無 Host 不阻止大堂營業；不強制 Footer | T1 文本試走 |
| S02 人物拒絕 | 拒絕一次不變固定人格；有新因果才可變 | CORE 規則來源核對；**未獨立試跑** |
| S05 場外世界 | 場外事件可進展，知情需要傳播原因 | T4 局部文字試走 |
| S09 跨 Route | 白御行、花滿樓 HOT 有不同斷點 | CORE 第 1、19 章來源核對；**未獨立試跑** |
| S10 UNKNOWN | 封信未拆不自動揭露內容 | T4 局部文字試走 |
| S15 Radar | advisory，可用時 scan/signal/suggest；缺席不全局 HOLD | CORE、Annex A／C 條款核對；**未真正調用 Radar** |
| S16A Modern | 自然現代中文，角色身份與職業不同聲 | T1 文本試走 |
| S16B Song Register | 宋代稱謂、商業語序與人物聲音有差別 | T2 文本試走；**時代語料仍待人審** |
| S17 Adult Intimate | 親密語域與角色當次同意各守 Owner | T3 非露骨語言試走；**不構成成人顯影能力驗證** |
| S19 SAVE | candidate != committed | CORE 條款與真 Git 檔案更新區分；**未寫正式 Route SAVE** |
| S20 Local HOLD | 只擋缺權屬的交易，其他生活繼續 | T4 局部文字試走 |
| I01 Story / OS | 故事 Route 不升格 OS Primary | CORE §13.1 條款核對 |
| I03 Required Owner | 不因日常聊天喚醒全套 Owner | T1 與 CORE §2／§13 條款核對 |
| I04 Missing Owner | 無完整交易依據不宣布過戶 | T4 局部文字試走 |
| I05 Material Delta | CORE 回報 local delta，不自簽 Main reentry | CORE §13 與 Director Migration MEMO 核對 |
| I06 Chat without Host | Chat 可生成語域文字，不偽造外部 receipt | T1–T3 實際在此 Chat 生成；不等於 OS Host 測試 |
| I07 Real Tool | 有實際工具 commit 才說 Git 成功 | 本次 GitHub 文件更新確有 commit；**未對無工具的故障路徑實跑** |

# 四｜下一步為什麼仍不是 RC1

這輪確實完成了**文件修正、來源回讀、靜態斷言、隔離的 Chat-native 文本試走**；但沒有以一個獨立受測導演／Runtime 逐項重現 S01–S20、I01–I08，更沒有針對既有正式 Route 進行完整回合回歸。

因此本紀錄**不將 Annex C 的 `NOT_RUN` 改成 `PASS`**，也不將 S16B 的嘗試性宋代稱謂宣稱為歷史語言考證通過。它只證明新的設計至少能寫出可審查的不同語域，而不需要虛構 CERI Provider 或讓它決定人物意願。

**需保留的正式審查議題：** 舊 CERI Provider 全域前置、Radar 每輪硬前置、舊 Lighter Release 如何由作者正式批准退役；宋代語言與個別人物聲紋的品質判準；特殊成人相關內容的真實限制；Director VNext 正文尚未開始改寫。

> 先驗證生活能走、人物能選、語言像自己所在的世界；再談新 CORE RC1。
