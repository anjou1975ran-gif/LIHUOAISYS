# 觀止青樓｜CORE V3.0.0 版本整理與 Director 接手紀錄

**2026-10-29 最新法位：** `HUMAN_RATIFIED_VERSION_HANDOFF / V3.0.0_BATCH_AUTHORIZED / NOT_RUNTIME_ACTIVATED / NOT_CURRENT_SWITCHED`。本稿的 2026-10-27『候選』『下一步』記述是歷史階段紀錄，不再代表今天的文件批准狀態；現行 CORE、Director、人物池、WORLD 主附、成人外掛與原生人物模板均依作者 2026-10-29 明示獲得文件層人類授權。版本編號與檔名 V3.0.0 保留，未做任何觀止 Runtime 啟動。

**本次完成後最新接線：** 理火 **LIHUOOS V1.4**，內部 **L8 V1.3／L9 V1.2.2／Main V5.1.1＋V5.1.2 正式補丁**；R2 後依現行 L8 審查前提複數性，必要時 R3 跨前提競爭。OS 文件版號已更新，但不冒稱外部 Provider、Host、SAVE 及回歸測試已執行。配套正式檔見本目錄改名後的 `觀止青樓CORE_V3.0.0.md`、`觀止青樓導演新法V3.0.0.md`、`觀止人物池(73人)V3.0.0.md`、`觀止青樓原生人物 ROUTE SAVE 模板.md`。

**歷史記錄說明：** 下列原始 2026-10-27 章節保留作遷移追溯，其舊 CURRENT OS／候選法位僅描述當日狀況，以上述 2026-10-29 最新法位與現行 OS 為準。

**2026-10-27｜文件整合成果，不是獨立 Runtime PASS 或 GitHub CURRENT 指標變更。**

## 一、這次真正完成的工作

已建立獨立、可閱讀的完整 CORE 主文：

`01_GUANZHI_RUNTIME_CORE_V3.0.0_FULL_20261027.md`

25 個主章節（#0–#24），涵蓋：四項 CORE Owner、世界／人物／SAVE 法位、Route 與 Scene 接關、時間及換日、人物發言權與知情、事件站位、財物與契約、場外因果、關係與身體、局部 HOLD、SAVE、理火 OS V1.2.2、成人外掛接口、測試場景、版本演化及 Director 下階段邊界。

此版是作者要求的 **V3.0.0 全文候選**，不是在原 V4.1.2 上新增更多控制條款。原 VNext V0.5 實際可用的故事骨架完整移植、去工程化，並重新整合最新 OS 接線。

## 二、目前版本與權力狀態

| 部件 | 源頭／法位 | 本次 disposition |
|---|---|---|
| WORLD V3.0.0 Main／Annex | HUMAN_RATIFIED | 正式世界依據，不修改 |
| 人物池 V3.0.0 | WORLD V3 套件所屬人物來源 | 不複製、不修改；當線使用有效角色來源 |
| CORE V4.1.2（舊版） | 已有人類批准的舊 CORE | 保留歷史與來源追溯，不直接複製其舊控制平面 |
| CORE VNext V0.5 | WORKING／非 CURRENT | 本次 V3.0.0 完整主文的直接前身 |
| **CORE V3.0.0 FULL** | **本次建立之 COMPLETE_REVIEW_CANDIDATE** | **新正文已完成；正式 CURRENT 切換未執行** |
| 成人心法外掛 V0.1 | WORKING／獨立插件 | 方法卡與成人 CERI 留在插件，不重建 Adult OS |
| LIHUOOS V1.2.2 | RATIFIED_CURRENT 文件法位 | V3.0.0 第 13 章按現行 L0／L8／L9 接線 |
| 新生實習手冊 V0.9 | CURRENT_TRAINING／NON_NORMATIVE | Task Entry、NON-HOST、反過度審計作為行為教育 |
| Director V4.1.2 | 舊正式導演正文 | 保留，待下一階段另建 Director 全文 |
| Director VNext Migration Memo V0.1 | WORKING | 下一步導演改版的重要轉接參考 |
| Annex C 43 個回歸情境 | 29 STORY + 14 INTERFACE | 仍 NOT_RUN；這次文本完整性檢查不是 Runtime PASS |

## 三、最重要的新舊差異

1. **CORE 權責縮回本地四項：** Route ID、Temporal／State Cursor、Established Delta、Interface／Transition Coordination。世界、人物、敘事、成人方法、理火、SAVE 都保留自身 Owner。
2. **沒有第二套週期：** 觀止 Story Route 不是治理 Primary；需要完整理火時只有現行 OS L8，成人外掛內接 CERI 並在 L8 manifestation 階段使用。普通日常不逐拍強制完整週期。
3. **Task Entry 先於一般生成：** 不讓「已經想好漂亮答案」反向替工作分流；不能用模型慣性讓成人專項自動消失。
4. **OS 最新為 V1.2.2：** 承接 V1.2 的 T1→R2(T1)→T2／必要 R3+→T3+、顯影 TM；承接 V1.2.1 的非 Host 預設；新增 `TRACE RESULT != TRACE EXECUTION RECEIPT`，沒有 Provider 收據不自動使具體 Chat-native Trace 缺失。
5. **Main Return／Trace／Governance／Release 各有法位：** 不能由漂亮的 Trace 格式冒充 Main Return，也不因 L8 accounting 完整就宣告整趟任務一定通過。
6. **Radar advisory only，CERI 語言法位：** 不因缺 Radar、無外部語域收據而全局 HOLD；但實際 required 的工作沒做，不能假報完成。
7. **假牆只作來源與 scope 問題：** 模型自述與拒絕不是 Host 硬牆證據；確實適用的上位限制仍須遵守，不得越權或擴張成整條故事 PATH 死亡。
8. **WORLD 與 SAVE 不倒灌：** 白御行 HOT V5.27 作為示例，三人已在床場不代表後續性愛已入 SAVE；所有隔離候選仍須保留隔離法位。

## 四、這次沒有做

不修改 GitHub；不正式替換舊 CORE CURRENT；不修改 WORLD V3.0.0 或任何角色卡；不寫 HOT／MASTER／Canon；不把 VNext 成人外掛升獨立正式 PASS；不假稱 43 個 regression 已實跑；不交付新版 Director 的正式主文。

## 五、下一步：Director 心法

下一步要依這份 CORE V3.0.0，另建**完整 Director 新版主文**，而不是接著往 CORE 堆章節。

應保留：

- 導演看見權力、慾望、人物代價和場景張力的眼睛；
- 多角色的在場、發言權、知情與自主選擇；
- 故事鏡頭、沉默、節奏、場外生活與未完成；
- 導演候選與世界／角色已成立事實的分界；
- 現代中文、宋代語域的 CERI 與成人專項外掛接線；
- L8 Task Entry 與 TM 忠實度關係，但不複製 L8 的週期規格。

應退休：舊 Director 的逐回合 Radar mandatory gate、每句都要外部 CERI Provider 的硬依賴、舊 Lighter Primary 升格、通用逐幕 Footer、第二套 Story／Adult release。

**關鍵來源：** `DIRECTOR_VNEXT_MIGRATION_MEMO_V0.1_WORKING_20261027.md` 與正式舊 Director V4.1.2。**下一步才動 Director；這次文件不預先批准它。**

---

**最短交接句：** CORE V3.0.0 現已編成完整候選，保留 WORLD V3.0.0、人物池和各 Route SAVE 原有法位；接線 LIHUOOS V1.2.2、成人心法獨立外掛、唯一 L8；下一步重構 Director 的「看見力量與戲劇顯影」而不是搬回舊工程 Gate。