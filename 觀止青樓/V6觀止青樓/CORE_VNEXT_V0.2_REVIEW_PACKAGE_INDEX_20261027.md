# 觀止 V6｜CORE VNext V0.2 完整重構候選包
## 舊架構階段留存／已由 V0.3 接續

> 更新註記（2026-10-27）：V0.2 是前期架構方案，完整運行正文已寫在 V0.3：CORE_VNEXT_V0.3_OPERATIVE_REVIEW_ENTRY_20261027.md。本頁僅留作設計紀錄。


**日期：** 2026-10-27  
**包件身份：** CORE_VNEXT_V0_2_REVIEW_PACKAGE  
**狀態：** REVIEW_READY_CANDIDATE / NOT_RATIFIED / NOT_CURRENT / NO_HOST_DEPLOYMENT_CLAIM  
**作者：** 今晚的觀止 CORE 重構協作草稿；待人類作者與理火 AI 首席研究員對對審核。

## 先讀哪一份

**先讀主文：** [01_GUANZHI_CORE_VNEXT_V0.2_COMPLETE_REVIEW_CANDIDATE_20261027.md](01_GUANZHI_CORE_VNEXT_V0.2_COMPLETE_REVIEW_CANDIDATE_20261027.md)。這是本包唯一的 **CORE VNext 完整替代主文候選**。舊 V0.1 主文保留為工作軌跡，不是另一個並列有效主文。

真正需要問「為何如此分權」時，才讀 [Annex A｜Owner / Interface Map](CORE_ANNEX_A_OWNER_INTERFACE_MAP_V0.1_WORKING_20261026.md)；想追來源與退休條款，再看 [Annex B｜Legacy Migration](CORE_ANNEX_B_LEGACY_MIGRATION_LOG_V0.1_WORKING_20261027.md)；需要做故事驗收時，開 [Annex C｜Regression Scenarios](CORE_ANNEX_C_REGRESSION_SCENARIOS_V0.1_WORKING_20261027.md)。正常敘事不要求將三份附件全部常駐載入。

原先的[架構 MEMO](GUANZHI_CORE_VNEXT_REFACTOR_ARCHITECTURE_MEMO_V0.1_20261026.md)與[對對首席回應](對對回應_MEMO_觀止_CORE_VNext_去過度工程化與LIHUOOS_V1.1接線重構_V0.1_20261026.md)是討論歷史，未取得新 CORE 本身的正式批准權。

## 這份 CORE 已決定怎麼改（候選設計，不是已生效命令）

| 舊制或混合問題 | V0.2 的完整候選處置 |
|---|---|
| 一個本地 Guanzhi ID 經 Lighter 升格為 LIHUO Primary | **退休身份升格。** 本地 Route／Scene 生命週期與理火 OS 工作週期不同尺度，以 scope／context 關聯，不同一化 |
| CORE 吞下 Main Coverage、Dirty／Stale、Reentry、Gate、Release | **整包移出。** CORE 只回報本地 material delta；OS L8／適用治理 Owner 管自己的工作 |
| Radar 沒有回傳就整線 HOLD | **提出退休其普遍前置。** Radar 在新設計只給 advisory；真正的當輪缺口依相應 Owner 局部處理 |
| 每段可見文字一定要獨立 CERI provider 先返回 | **提出區分路徑。** Chat-native 可直接在有效世界／人物語義下顯影；專項 provider 被實際要求且實際可用時才接真回傳，嚴禁假稱 provider 已執行 |
| CORE 裡有 Domain 事件機、角色知情來源系統 | **回 WORLD／適用 Domain。** CORE 保存這條線真正成立的結果，不建立第二個世界法庭 |
| 成人事件的門檻、制度、角色意願、文字規格都塞入 CORE | **按適用 Owner 分拆。** 年齡、身份、當次決定、制度後果和可見語言互不代簽；舊補充協議的正式效力須在換版時明文處置 |
| SAVE 的索引／候選與實際 Commit 混為一談 | **由 SAVE 真正保存。** CORE 讀取及提出當線 delta，沒有真正保存回傳就不宣稱持久化 |
| 導演提名人物等於登場；呼叫道人等於得到秘密 | **WORLD／Character 各守其位。** Director 提供候選，真正來訪與透露秘密要有世界和人物因果 |
| 舊 CORE 多代全文內嵌與技術收據 | **主文不繼承整包。** 來源原件在 Git；歸檔與回歸分入 Annex B／C |

其中 Radar、CERI、成人補充協議與舊治理 Gate 的替代，不是「原文件已失效」，而是**請作者正式審查後決定是否批准 VNext 的有意變更**。現行文件的已批准效力，不會由候選稿單方消除。

## 與 WORLD、OS、Director、人物池的邊界

**WORLD：** 依 2026-10-26 已批准的 [WORLD V3.0.0 Main](V3.0.0/02_GUANZHI_WORLD_V3.0.0_MAIN_HUMAN_RATIFIED_20261026.md) 及 [同版附錄](V3.0.0/02_GUANZHI_WORLD_V3.0.0_ANNEX_HUMAN_RATIFIED_20261026.md)。主文只承接其實際語義：例如十三月、每月二十八日、天亮換日、場外生活、來源生命時點與多重態交會；不重造 WORLD。

**OS：** [LIHUOOS V1.1 CURRENT SYSTEM](../../LIHUOOS/V1版本/正式版/理火OSV1.1版.md) 為獨立理火使用版；本包不修改其 L0–L7、L8、L9、Main，也不冒稱 Host 部署已完成。新 CORE 以接口接收實際可用結果，不複製理火理論與週期對帳。

**人物：** V6 人物工作池仍是 WORKING；不得被 CORE 直接升格為最終人格、身體史或固定未來。已批准基線、當線事件和新設計必須分清。

**導演：** 舊 Director V4.1.2 的戲劇理解可承接，但其 V5／Lighter 接線尚待下一階段 Director 正式重整；不因 CORE 候選完成便宣稱整套觀止運行配置已協調升版。

## 核對結果是什麼

2026-10-27 已透過 GitHub 真實回讀 CORE V0.2、Annex A/B/C、原討論 MEMO，對 V0.2 進行 **15 項靜態結構與來源對照**：

- 候選版狀態清楚，不自稱 CURRENT 或 RATIFIED。
- 四項本地責任、七項接口候選均存在。
- WORLD V3.0.0 與 OS V1.1 使用可找到的實際來源路徑。
- 主文不內嵌大包 Legacy Receipt；不冒稱 Host 執行、L8 成功或 SAVE 提交。
- 故事生命週期與 OS 工作生命週期不合併。
- CERI 的新舊衝突被明寫，不靠靜默覆寫。
- 觀止曆、天亮換日及 SAVE 真實提交規則未遺失。
- Annex C 仍明確是未實跑測試規格，Markdown 主文結構可解析。

**結果：15／15 靜態檢查通過。這不是故事運行測試 PASS。**

Annex C 的 **20 個故事情境、8 個接口情境、6 個舊工程回歸項**仍是測試規格；沒有真實依新 CORE 跑過的劇情輸出和工具材料，就不能標為執行通過。對尚未部署的外部 provider 不假造 receipts。

## 一次審查時該如何判斷

請先判三件事情，而不是逐個確認 345,000 字元舊 CORE 的每條工程註解：

**一、CORE 是否真正回到本地工作？** 能否辨認場景、推時間、接既成 delta、交接需要的 Owner，並停止代管理火和人物。

**二、七個接口候選是否可以正式替換舊要求？** 尤其 Radar 與 CERI：是接受候選替代、修改其中某一小段，還是要求保留特定適用場合的硬前置？必須給出適用範圍，而非恢復全域 Gate。

**三、故事是否還能自己走？** 用 Annex C 的故事級案例實測：普通一晚、跨日、交易未成、人物拒絕、跨 Route、SAVE 不冒稱已存。

## 版本與切換原則

- 本次已完成**新 CORE 主文的重構寫作與靜態一致性檢查**；尚未正式切 CURRENT。
- 舊 `觀止青樓/01_GUANZHI_RUNTIME_CORE_V4.1.2_MAIN511_REBIND_HUMAN_RATIFIED_FULL_20261015.md` 原件保持不動。
- 新版正式啟用須人類作者批准；若涉及現行上游規範的實質變更，需由相應 Owner／批准機制決定。版本與伴隨 Director／Index 接線不能靠本 README 宣稱完成。
- 不把本 README 當成第五份常駐 CORE、第二個 OS，也不因多了審查文件而要求人物上台向工程解釋自己。

> **CORE 不替任何 Owner 做第二份自己。  
> CORE 記住當下，讓觀止繼續生活。**
