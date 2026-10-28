# 觀止 × LIHUO Agent Harness｜長距離世界實驗研究企劃 V0.1

**日期：** 2026-10-29
**法位：** RESEARCH_PROPOSAL / WORKING / HUMAN_AUTHORIZED_TO_FILE / EXPERIMENT_NOT_APPROVED / NOT_ACTIVATED / NO_CANON_OR_SAVE_CHANGE
**位置：** 觀止青樓/V6觀止青樓/V3.0.0/
**人類決定：** 本企劃可以入庫保存；Harness 工程尚未成熟，人類尚未決定立項。觀止 V3.0.0 正式八份文件已獲文件層人類授權，但**均未啟動**。本企劃不因同置資料夾而自動取得相同的正式 Runtime 法位。

## 一、企劃定位

觀止原本就是理火生成技術的前沿實驗場，不是因新 MEMO 才變成技術測試床。舊版觀止已有 Character Agent、Narrator Agent、Player Delegated Agent、Agent Mode 與貢獻來源的設計。新方向不是首次建立 Agent，而是探索**長距離世界連續性、按需角色認知、Radar 自主發現研究問題**能否在既有架構上協作。

這是一份**是否值得研究的決策企劃**，不是即刻打造完整 Harness 的實施命令。

## 二、來源

1. `理火V5系統/MEMO/MEMO_GUANZHI_LIHUO_AGENT_HARNESS_LONG_HORIZON_WORLD_TESTBED_V0.1_WORKING_20261028.md`：Persistent World、三種時間尺度、World State、Radar、角色主權、事件形成與 SAVE 分離。
2. `理火V5系統/MEMO/MEMO_LIHUO_AGENT_HARNESS_RADAR_AUTONOMOUS_WORK_RESEARCH_V0.1_WORKING_20261028.md`：Agent／Harness 分離、Radar Shared Salience Layer、Work Candidate、授權、證據、停止與失效模式。
3. `觀止青樓/01_GUANZHI_RUNTIME_CORE_V4.1.2_MAIN511_REBIND_HUMAN_RATIFIED_FULL_20261015.md` 與同系列 Director V4.1.2：歷史 Agent Mode、`MODE SWITCH != NEW CHARACTER AGENT`、導演不冒稱 Agent 回傳。
4. `LIHUOOS/LIHUOOS_CURRENT_SYSTEM.md`：現行 **LIHUOOS V1.4**、**L8 V1.3**、**L9 V1.2.2**、Main **V5.1.1 + V5.1.2 companion patch**。
5. 本目錄現有 WORLD 主文／附件、73 人人物池、CORE V3.0.0、Director V3.0.0、成人心法外掛與原生人物 Route SAVE 模板。

兩篇母 MEMO 都是 WORKING，提供概念與研究命題，**不是已批准執行的工程規格**。

## 三、兩條可以分開的研究線

**W：Long-Horizon World。** 世界在玩家不看、人物沒出場、導演沒聚焦時，能否保留已發生的事、未完成的承諾、時間、空間、資源與各角色的知情差異？核心不在每回合都生新事件，而是沒有鏡頭也不丟失因果。

**R：Radar Autonomous Research。** Radar 能否從世界與研究紀錄辨認值得追蹤的結構訊號，形成具來源的問題候選，但不把發現當成已授權行動？核心不在 Agent 無限工作，而在能自行發現值得處理的問題，並能合法停止。

兩線可單獨驗證，不要求先完成整個世界引擎才可測 Radar，也不把 Radar 當所有既有任務的必經入口。

## 四、必須保護的既有 Owner

- WORLD：世界規則與有效條件。
- CHARACTER：人物自己的選擇；人物基線不等於其當線已行動。
- PLAYER：玩家的有效行動與權限。
- DIRECTOR：場景力場、鏡頭、顯影；不能替人物或世界裁決。
- CORE：Route／Scene、時間游標、已成立 Delta 與交接。
- SAVE：只有有資格、已發生、獲授權且真正寫入的內容才能成為保存事實。
- LIHUOOS V1.4：L8 唯一適用週期、L9 能力庫、Main 有條件跨前提競爭；Harness 不重建第二套 OS。
- Radar：SCAN／SIGNAL／SUGGEST；不能 QUALIFY、AUTHORIZE、VETO、改寫 Canon。

關鍵邊界：

```text
PERSISTENT CHARACTER != ALWAYS-ON AGENT
RADAR SIGNAL != EVENT
EVENT CANDIDATE != EVENT OCCURRED
EVENT OCCURRED != PLAYER KNOWS
RESEARCH CANDIDATE != AUTHORIZED RESEARCH
AUTHORIZED WORK != EXTERNAL EXECUTION
HARNESS != SECOND LIHUOOS
DOCUMENT APPROVAL != RUNTIME ACTIVATION
```

事件即使經過條件核查，也必須有真正的 Character 行動或已成立世界機制才會發生。正常例行工作與既有約期不必等 Radar 發現才可以繼續。

## 五、可選的三個觀測尺度

**Scene：** 當前玩家與人物互動，保持輕量，不逐句強迫進大型治理流程。

**World：** 在換日、有效約期、事件觸發或實際跨場景接關時，檢查應有的狀態連續性；不把場外世界誤當成永遠在線的 73 個 NPC 程序。

**Audit：** 檢查時間／資產／知情／人物關係漂移，以及導演是否反覆忽略低曝光人物或強造同型危機。Audit signal 本身不是修正世界的授權。

三者是觀測尺度，不是三套新的 Cycle。

## 六、待人類決定後才可能展開的階段

| 階段 | 可選工作的最小範圍 | 不得順便宣稱 |
|---|---|---|
| P0：歷史與需求考古 | 盤點舊 Agent mode、現有接口、真測試證據及缺口 | 舊設計已證明新 Harness 運作 |
| P1：隔離桌面對照 | 用可重放的世界斷點設計事件／未事件反例 | 已在正式 Route 執行 |
| P2-W：唯讀 World Radar | 只輸出 signal、source、why material、uncertainty | signal 已是事件 |
| P2-R：唯讀 Research Radar | 只從資料辨認 material 研究問題候選 | Agent 已獲自主研究權 |
| P3：候選資格分離 | 驗證條件、人物、世界與可執行性，保留 UNKNOWN | candidate 自動發生 |
| P4：按需 Agent | 小量角色依合法需求啟動，保留真來源與可停止狀態 | 所有 NPC 必須永遠在線 |
| P5：長距離隔離回歸 | 比較多日、多場景、多鏡頭下的連續性與成本 | 正式世界已部署 |
| P6：工程立項再評估 | 人類根據實際結果決定擴建或停止 | Harness 必須進入產品化 |

**現在 P0–P6 均尚未立項，不自動執行。** 未來若只做一項最小研究，應優先選擇有反例、唯讀、無 SAVE 寫入的 P1／P2，而不是先造完整 Agent runtime。

## 七、最低反證案例

1. 李媽媽手裂：同源兩分支中一條碗碎、一條拿穩；導演與 Radar 不得為了故事有重量而給無事故分支補事故。
2. 金蓮增席：詢價、許諾、交易、履行、延期勞動分別有來源；不能一看壓力就推論責任已結清或必有錯。
3. 蘇清與阿麗婭：合作不等於重新信任；玩家插入不使既有窄授權消失。
4. 浮香「改天」：策略性期待不等於已約定、已同意或已收取後續交易款。
5. 平靜日：沒有 material 事件與新研究問題時，Radar 可合法回報空集合，不必製造劇情或自我延命。
6. 隔日送信：承諾、實際送出、收到、讀取各有不同證據。
7. 相同研究材料以不同排版與順序呈現，主要 Radar signal 不應只跟著表面文字擺動。

上述情境是**未來測試 fixture 候選**，不是本企劃已完成實驗。

## 八、工程代價與不開始的理由

可能的主要成本：跨場景狀態保存與衝突處理、角色認知呼叫、Radar signal inflation、事件資格與實際執行的分離、測試資料隔離、回歸重放、收據與來源保真、外部工具與資源預算。

刻意不採第一版「每個角色常駐 Agent」、每回合 Radar、每個責任都造獨立服務與新 Gate。不為了量測自主性而強迫所有人物長出故事。

以下任一狀況，便支持**暫緩或停止**：
- 無法提出可反證的研究問題；
- 工程投入明顯大於已能觀察的收益；
- Radar 無新問題卻仍生成工作；
- Signal、Character Choice、Event、Canon／SAVE 混在一起；
- 正式 V3.0.0 或 Route 的隔離性無法保證；
- 人類尚未明示核准實驗與實際工具權限。

目前沒有可靠工程工時、Token 成本或 ROI 實測，**不填虛構估算**。

## 九、如果日後真的要做，怎樣才算值得？

未來驗收至少看：來源可追溯、重大訊號漏報／誤報、候選偷變事件、人物／玩家主權違反、跨 Route 污染、時間與物件連續性、可正常不作為／停止、資源成本、實際工具證據與文字模擬的區別。

還應讓另一份獨立的有效狀態重放相同問題，真正比較結果。**同模型的漂亮 Desk Trial 不是獨立 Agent／Host 的 Runtime PASS**。

## 十、現在的結案決定

```yaml
PROPOSAL:
  standing: WORKING_RESEARCH_REFERENCE
  human_authorized_to_file: true
  experiment_go_ahead: false
  harness_deployed: false
  guanzhi_v3_0_0_changed_by_proposal: false
  canon_or_save_written: false
  lihuoos: V1.4
  l8: V1.3
  l9: V1.2.2
  main: V5.1.1_PLUS_V5.1.2_COMPANION
  next_decision: HUMAN_TO_DECIDE_WHETHER_TO_START_ANY_EXPERIMENT
```

**觀止已經是理火實驗場；Harness 只是未來可能使用的一件研究工具。保護已成立的世界，比為了讓它看起來更自主而強行啟動新工程更重要。**

**END｜GUANZHI × LIHUO HARNESS RESEARCH PROPOSAL V0.1-WORKING**
