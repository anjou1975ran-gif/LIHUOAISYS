# 觀止青樓｜CORE VNext V0.3 實際運行正文
## 統一審查入口｜2026-10-27

**狀態：** OPERATIVE_DRAFT_COMPLETE / HUMAN_REVIEW_PENDING / NOT_RATIFIED / NOT_CURRENT
> **2026-10-27 CERI 定向補修紀錄：** 已依對對最新交接 MEMO 修改 CORE V0.3 的 §13.4／§14／§23.3、Annex A／C；第 0–12 章未重寫，仍未升 CURRENT。完整工作索引：  
> - [對對 CERI 語言模式交接 MEMO](MEMO_觀止_CORE_VNext_後續工作交接_CERI語言模式重定位_V0.1_20261027.md)（來源作者：對對）  
> - [Director VNext 遷移 MEMO](DIRECTOR_VNEXT_MIGRATION_MEMO_V0.1_WORKING_20261027.md)（只盤點、不改導演正文）  
> - [CERI Targeted Regression：靜態核對與 Chat-native 隔離試走](CORE_VNEXT_CERI_TARGETED_REGRESSION_DESK_TRIAL_V0.1_20261027.md)（非獨立 Runtime PASS）
> - [Targeted Story Walkthrough Round 2](CORE_VNEXT_TARGETED_STORY_WALKTHROUGH_ROUND2_V0.1_20261027.md)（18 個指定案例的隔離文字／來源走讀、模式中途切換與對抗式錯誤注入；非獨立 Runtime PASS）  
> - Annex C 的 S16 分為 S16A Modern／S16B Song，新增 S16C 翻譯模式中途切換；S17 補場景語域。正式 RC1 仍待審查。

  
**這次交付的對象：** 作者與理火 AI 首席研究員「對對」。本文件僅索引閱讀與驗證結果，不構成批准、安裝、部署或新的治理法位。

### 這次真正要審的是哪一份？

**[01_GUANZHI_RUNTIME_CORE_VNEXT_V0.3_OPERATIVE_BODY_WORKING_20261027.md](01_GUANZHI_RUNTIME_CORE_VNEXT_V0.3_OPERATIVE_BODY_WORKING_20261027.md)**

這份 V0.3 是**新 CORE 的實際故事運行正文**，不同於 V0.1／V0.2 的架構與接口方案。請直接檢查它能否讓導演接起一條 Route、逐回合走故事、處理真正有效的角色與事件結果、跨日、場外進度、實際 SAVE、錯誤與下一幕。

正文目前約 16,330 字元、495 行，內含 24 個編號章節（0–23）及六段有明確前提與當輪結果的情境試走。它是 Chat-native 文字運行核心，不是可以不靠任何模型或工具自行在背景啟動的軟體引擎。

### 實際正文涵蓋的工作

| 位置 | 真正解決什麼 |
|---|---|
| 第 1–2 章 | 新 Route／舊 HOT SAVE 入場、同線凍結點、玩家一句話怎麼轉成行動和下一幕 |
| 第 3–5 章 | 人物誰在場、各自知道什麼、願意如何選；事件從提出到完成；買賣、財物、身份與權利的因果 |
| 第 6–7 章 | 十三月曆、天亮換日、約期和場外事件的實際進度 |
| 第 8–10 章 | 關係和記憶、移動與場景空間、身體與物質代價 |
| 第 11–12 章 | HOT／MASTER／RCL 的接關與真實存檔；來源衝突、局部 HOLD 與錯誤修復 |
| 第 13–15 章 | 與理火 OS V1.1 合作但不自授治理；文字呈現、下一幕交接 |
| 第 16–21 章 | 六段逐步試走：茶席、交易、天亮、跨線 SAVE、流言、官府身份未決 |
| 第 22–23 章 | 最短接關口訣、來源、未批准事項與審查界線 |

### 跟先前工作檔的關係

- **V0.1、V0.2 主文：** 舊前置架構方案。V0.2 曾被誤稱為「CORE 完整重構」，實際只是責任和接口的設計框架；它不是這輪新的 CORE 本體。
- **[Annex A｜Owner Map](CORE_ANNEX_A_OWNER_INTERFACE_MAP_V0.1_WORKING_20261026.md)**：舊 CORE 逐條主權與接口定位。追爭議時才讀。
- **[Annex B｜Legacy Migration](CORE_ANNEX_B_LEGACY_MIGRATION_LOG_V0.1_WORKING_20261027.md)**：保留歷版接線與退役史。故事運行時不必常駐。
- **[Annex C｜Regression Scenarios](CORE_ANNEX_C_REGRESSION_SCENARIOS_V0.1_WORKING_20261027.md)**：22 個故事案例（含 S16A／B／C）、8 個接口案例與 6 組舊工程檢查，**尚未逐項執行**。
- 舊 `觀止青樓/01_GUANZHI_RUNTIME_CORE_V4.1.2_MAIN511_REBIND_HUMAN_RATIFIED_FULL_20261015.md` 保留原位；V0.3 候選不能使其自動退位。

### 來源核對

- 現行 [WORLD V3.0.0 主文](V3.0.0/02_GUANZHI_WORLD_V3.0.0_MAIN_HUMAN_RATIFIED_20261026.md)：十三個月、每月 28 日、**天亮換日**、場外生活與來源時點、李清照個體未纏足、成年性交易及出閣 18 歲門檻。
- 理火 [OS V1.1](../../LIHUOOS/V1版本/正式版/理火OSV1.1版.md)／L9：Radar 是建議工具，能力不等於治理法位；Main、L8、外部 provider 的真實工作不得由 CORE 冒充。
- 實際 SAVE 範例：白御行線 HOT V5.27、花滿樓線 HOT V1.16，其特定凍結點、排除範圍及跨線隔離已於正文示範；**本次沒有改寫任何 SAVE**。

### 我已做到哪種檢查

透過 GitHub 回讀主文及上述實際來源，完成 **28 個靜態／來源語義檢查**：章節存在、路線與時間處理、人物／交易／場外運作規則、六段試走、WORLD 的換日與成年及個別身體史、L9 Radar 定位、HOT SAVE 的有效斷點、OS／SAVE 不冒稱執行、歷版 CORE 原件未被改寫。

**靜態與來源核對不等於執行測試。** 六段「實際試走」是依情境做的人工 Chat-native 因果推演；它們展示操作步驟和應保留的狀態，不是獨立 Agent、Host、OS 全週期或 Annex C 逐項真實實跑的 PASS。

### 此次仍需人類核定才生效的差異

**Radar**：提議退出每回合固定強制回傳和全局 HOLD，保留 L9 advisory。  
**CERI／Narrator**：提議一般 Chat-native 可直接依有效語義顯影，獨立 provider 真有使用才認回傳；需明文處理與舊普遍硬前置的衝突。  
**舊 Lighter Final Release／Primary**：不以新 OS mega-gate 代替，故事 Route 身份不升格成 OS Primary；仍尊重實際啟動 OS 工作的適用 Owner 和 L8 義務。  
**成人補充合同與 Domain**：有效實質邊界不得因精簡而消失，具體責任與舊規範的正式退休／重綁須另審。  
**Director**：尚未正式重寫或連動批准，不能藉 CORE V0.3 宣稱整套觀止已完成 V6 調度。

### 作者與對對的審查焦點

審主文的第一件事不應是「少了幾萬 Token」，而是：

**讓新導演讀完這份 CORE，能不能不用偷偷補洞，就讓一晚青樓生活從第一句走到下一個清晨？**

如果可以，再逐項檢查接口替代是否真正合法、不會使人物或 WORLD 主權被 CORE 吞回。此處不預先給自己一個審查通過的結論。

---

**一句話：V0.2 是圖紙；V0.3 才是供審的 CORE 運行正文。**
