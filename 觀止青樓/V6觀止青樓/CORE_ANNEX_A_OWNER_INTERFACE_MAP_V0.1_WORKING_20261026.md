# 觀止 V6｜CORE Annex A — Owner / Interface Map
## CORE VNext 角色拆分與舊條款盤點 V0.1

**日期：** 2026-10-26  
**狀態：** WORKING / OWNER REMAP CANDIDATE / NOT RATIFIED / NOT CORE SUCCESSOR  
**文件用途：** 先對照舊 CORE V4.1.2 的有效責任，讓下一版主文可重寫而非繼承整包。本文是遷移架構意見，不對現行 CORE、理火 OS、WORLD 或人物池產生改寫效力。  
**工作資料夾：** \`觀止青樓/V6觀止青樓/\`  
**參閱原稿：** \`GUANZHI_CORE_VNEXT_REFACTOR_ARCHITECTURE_MEMO_V0.1_20261026.md\`  
**參閱首席回應：** \`對對回應_MEMO_觀止_CORE_VNext_去過度工程化與LIHUOOS_V1.1接線重構_V0.1_20261026.md\`

## 0｜為何先做這份 Annex

問題不是 CORE 字數多，而是 CORE 把「需要知道」誤當成「擁有主權」。V4.1.2 的歷代逐字嵌入、舊 Lighter 資格、雙週期身份、Main coverage 與 reference lane 佔據巨大篇幅；過去它們承擔過工程目的，卻不應成為 VNext 常駐敘事知識。

**本次動刀的基本順序：** 先分 Owner → 再分界面 → 才能寫短而真的 CORE。重要保護不可在瘦身時流失，候選 disposition 不構成批准。

## 1｜來源與可追溯界限

| 來源 | 讀取內容與範圍 |
|---|---|
| 舊 CORE | \`觀止青樓/01_GUANZHI_RUNTIME_CORE_V4.1.2_MAIN511_REBIND_HUMAN_RATIFIED_FULL_20261015.md\`；本文引用其原有章節代號定位舊責任。 |
| 對對回應 | 首席研究員 V0.1：四項 CORE owner、兩類 lifecycle、退休 identity promotion、Chat-native 可工作、不改名重造 Lighter。 |
| 理火 OS L0 V1.1 | \`LIHUOOS/V1版本/L0_INDEX_SOURCE_VERSION_V1.1.md\`；L0–L7 意義／治理、L8 運行、L9 能力、Main 計算，Legacy Lighter 非現行控制層。 |
| 理火 OS L8 | \`LIHUOOS/V1版本/L8_LIHUO_OPERATING_CYCLE_V0.3_WORKING_20261025.md\`；一次完整業務週期、不重造 owner 定義。注意該來源檔內標記 WORKING；不能把個別草稿視為額外批准的獨立執行模組。 |
| 理火 OS L9 V1.1 | \`LIHUOOS/V1版本/L9_DAIL_CALLABLE_CAPABILITY_REPOSITORY_V1.1_20261026.md\`；RADAR_V6、工具能力與治理資格分離。 |
| WORLD V3.0.0 | \`觀止青樓/V6觀止青樓/02_GUANZHI_WORLD_V3.0.0_MAIN_HUMAN_RATIFIED_20261026.md\`；世界規則與人文敘事語義另存，CORE 不二次著述。 |

**狀態聲明：** OS V1.1 在文件層已 ratified current，但來源明示未完成 Host 部署與全系統實證；不得把文件級 CURRENT 當成外部 Host 執行收據。反過來，也不得因 Host 缺席，無端阻斷 Chat 中可以正常完成的敘事工作。

## 2｜四個 CORE 自有責任（對對方案）

1. **LOCAL STORY IDENTITY：** 管這是什麼 Route、Scene、Story attempt、continuation；本地身份不是理火治理身份。
2. **LOCAL TEMPORAL / STATE CURSOR：** 管本線現在到哪一刻、場景處於哪一局；曆法、物理、制度定義仍屬 WORLD。
3. **ESTABLISHED DELTA INTEGRATION：** 接已成立的行動、事件、後果、角色決定與未決狀態，組成當線 local delta；不替世界或人物創造 standing。
4. **INTERFACE / TRANSITION COORDINATION：** 把當前局面交給真正擁有處置權的 Owner，接回其有效結果並承接 HOLD／MISSING；不取代對方的治理程序。

簡式：

\`\`\`text
CORE: WHICH STORY / WHERE NOW / WHAT ACTUALLY CHANGED / WHO NEEDS TO ACT NEXT
NOT CORE: WHO THE CHARACTER MUST BECOME / WHAT WORLD FACTS MUST BE TRUE / HOW OS COMPUTES
\`\`\`

**補充：** 上面第 4 項是「本地協調」責任，不是跨領域統一裁判權。四項 Owner 指對自己的工作內容負責，不能解讀成持有四種上位治理權。

## 3｜六個工作面與真主權分界

| 工作面 | CORE 對這件事的身分 | 真正決策／資料 Owner |
|---|---|---|
| 本地 Route／Scene 入口 | Owner | CORE：故事的本地身份，不等於 OS cycle ID |
| 時間與場景延續 | Owner + Interface | CORE：cursor；WORLD：時間語義與世界規則 |
| 人物、交易與事件狀態 | 讀取／整合已成立結果 | Character：意願／決定；WORLD／Domain：發生／代價／制度 |
| 導演交接與顯影 | 傳遞場景狀態 | Director：戲劇理解；CERI／Narrator 等適用工作各由原 Owner／現行接口處理 |
| 記憶／SAVE | 提出本地持久化候選、接回提交結果 | SAVE：實際 commit、路線 HOT／MASTER、保存版本與歷史 |
| 理火 OS | 以 scope/context 綁定工作結果 | OS applicable owners：治理；L8：cycle 運作；L9：可調用能力；Main：compute |

**重要：** L9 工具會分析，不代表 L9 有批准權；Radar 建議不決定人物命運。每一場不必為了「有可能涉及」而啟動全部 owner。

## 4｜VNext 本地最小接口（資料建議，非新 API 法規）

\`\`\`text
GUANZHI_LOCAL_CONTEXT (conceptual)
  route_ref
  scene_ref
  story_attempt_ref_if_needed
  local_time_cursor
  established_state_refs
  current_player_action_or_continuation_basis
  required_owner_input_refs
  unresolved_local_facts

LIHUOOS_BINDING (conceptual)
  guanzhi_story_ref
  relevant_scene_snapshot_ref
  lihuo_cycle_ref_if_returned
  scoped_owner_return_refs
  pending_or_hold_refs

LOCAL_STORY_DELTA (conceptual)
  established_changes[]
  unresolved_candidates[]
  event_occurrence_refs[]
  persistence_candidate_ref_if_requested
\`\`\`

它只是說明：CORE 需要能讀懂哪些資訊、回傳放在哪。**不是新造三套 canonical schema、必填 receipt、Host API，也不是說這些欄位在現行平台都已實作。**

\`\`\`text
GUANZHI_STORY_REF <-> LIHUO_CYCLE_REF
CONTEXT BINDING, NOT IDENTITY PROMOTION

ONE LONG GUANZHI ROUTE
MAY SPAN MANY DISTINCT LIHUOS INVOCATIONS

TOPOLOGY
!=
A MANDATORY LINEAR PIPELINE
\`\`\`

### 4.1 正常故事 dispatch 的必要責任

在當輪真正相關時，已取得本地故事／場景位置、玩家行動或合法延續基礎、人物與世界等 Owner 有效結果、適用的 OS 返回；沒有真正必要的 Owner 處於阻斷性的 HOLD／MISSING，即可推進本地故事。

- **不預設：** 每場都需 Host、Legacy Lighter Gate、完整 Receipt Packet、全部 Owner、全部 L0–L9 公開回報。
- **不允許：** 未完成付款自動變成交、導演代角色同意、玩家線關係偷跨線、工具結果冒充世界事件、未 commit 卻宣稱已保存。
- **不是取消所有現行界線：** 成人場景、CERI/Narrator 依賴及特別的實質門檻，在其適用 Owner／來源未確認前，不得以「簡化」為由自行宣告失效。

### 4.2 Chat-native 與外部行動

**Chat 裡能真實完成的解讀、提案、推演、敘事，不因 Host 未部署自動停機。** 真正需要 Git、外部 provider、工具或持久化時，須有相應真實工具回傳；文件中的「應該執行」不能當已執行。

### 4.3 Radar

來源 OS L9 V1.1 將 Radar 列為 advisory capability（可 scan/signal/suggest，無 qualify/veto/authorize 權）。舊 CORE 以沒有 Radar occurrence/consumption 為故事整輪 HOLD 的機制，與新分工的接線仍需精確核查；**此 Annex 不擅自宣布它已全部退休，也不把它默默帶入新常駐前置。**

## 5｜條款盤點的分類規則

採對對建議十一類：\`CORE_OWNER\`、\`CORE_INTERFACE\`、\`WORLD_OWNER\`、\`CHARACTER_OWNER\`、\`DIRECTOR_OWNER\`、\`SAVE_OWNER\`、\`LIHUOS_OWNER\`、\`L9_CAPABILITY\`、\`ARCHIVE\`、\`REGRESSION_ONLY\`、\`DISPUTED\`。

每條先標一個**首要遷移位置**；若一條同時涉及多 Owner，細節仍須另行拆分。不能用表格分類就宣稱另一個 Owner 已接收、已部署或已批准。


## 6｜V4.1.2／V4.1.1 操作層條款逐項定位

| 舊 CORE 條目 | 初步分類 | 遷移處置 |
|---|---|---|
| `CORE-410-0` | 歷史歸檔 | 歷版 highest-read／批准優先級收至歷史；新正文由現行 index 指路。 |
| `CORE-410-1` | 理火 OS 治理／週期 | 中央 V5.1 index、hash、exact binding 退休為歷史；V1.1 current 指針屬 OS L0。 |
| `CORE-410-2` | 歷史歸檔 | Guanzhi identity → Lighter admission → same primary 的舊接線退休；不得以同 ID 改稱 V1.1。 |
| `CORE-410-3` | CORE 自有 | 保留觀止本地 story/attempt 身份；舊理火 primary standing 權限分離。 |
| `CORE-410-3B` | CORE 自有 | 同一正在處理的本地 attempt 的身份一致性可保留；不推導跨系統 primary 規則。 |
| `CORE-410-3C` | CORE 只接接口 | 以 context binding 連向 OS；舊 Lighter admission request 物件退休。 |
| `CORE-410-3A` | CORE 只接接口 | 保留修復／重試不自動重寫已成立本地狀態；OS attempt admission 交 OS。 |
| `CORE-410-4` | CORE 只接接口 | 重寫 owner map；Lighter 主權欄位不移植，保留 Character/World/Director/Save 邊界。 |
| `CORE-410-5` | 歷史歸檔 | 舊雙週期 binding 及後續 same-primary 替代物一併作前代歷史。 |
| `CORE-410-6` | 理火 OS 治理／週期 | 大型 vertical receipt manifest/packet 不常駐本地 CORE；只保留必要本地結果指標。 |
| `CORE-410-7` | 理火 OS 治理／週期 | Main coverage、dirty、stale、reentry 資格交 OS；CORE 僅回報 material local delta。 |
| `CORE-410-8` | 理火 OS 治理／週期 | same-primary reentry 具體資格及 ledger 退出 CORE。 |
| `CORE-410-9` | 理火 OS 治理／週期 | lost/pending/successor Primary 為 OS 運行語義，不由 CORE 維護。 |
| `CORE-410-10` | CORE 自有 | 保留本地 Story Dispatch；移除舊 Final Lighter Release 依賴，改以必要 Owner unresolved 範圍判斷。 |
| `CORE-410-11` | CORE 只接接口 | Director 可以請求並接回 OS 結果；Main caller 的 exact V5.1 內部契約不複製。 |
| `CORE-410-12` | CORE 只接接口 | 保存 Character/World/CERI/Narrator 主權邊界；Radar 是 advisory，不是裁決。 |
| `CORE-410-13` | CORE 只接接口 | 可見 Footer 降為按需狀態顯示；不能假造 receipt 或強制每場列帳。 |
| `CORE-410-14` | 歷史歸檔 | Formal/Reference 雙 lane boot 技術史退附錄；Chat 介面不得因沒有 Host 自動 HOLD。 |
| `CORE-411-1` | 僅保留回歸測試 | Reference Work Trace 的來源真偽核驗作測試，不寫進正常故事回合。 |
| `CORE-411-2` | 僅保留回歸測試 | Reference progress projection 作兼容驗證資料，非新本地 state machine。 |
| `CORE-411-3` | 僅保留回歸測試 | 證據不足不得冒充完成仍有效；具體 Reference guard 機制移出正文。 |
| `CORE-410-14A` | 歷史歸檔 | 工程憲法 exact pointer 對照僅留歷史。 |
| `CORE-410-15` | 歷史歸檔 | DAIL/IR/Coding 三層分離屬理火／能力系統；舊實作敘述退出。 |
| `CORE-410-16` | CORE 只接接口 | 保留責任拓撲非固定 pipeline 的短句，不複製圖語法技術細則。 |
| `CORE-410-17` | 歷史歸檔 | 舊 WORLD V2.3.2／LCAPG V3.3.20 伴隨指針僅供版本沿革。 |
| `CORE-410-18` | 歷史歸檔 | 舊 supersession map 與 retired enum 僅供遷移核對。 |
| `CORE-410-19` | 僅保留回歸測試 | RC4.2 SGC、receipt、ledger 逐項回歸清單入 Annex C；世界級保護另保留。 |
| `CORE-410-20` | 歷史歸檔 | RC4.2 候選處置及批准史留 Annex B。 |

## 7｜V4.0.5 至 V4.0.2 舊接線條款定位

| 舊 CORE 條目 | 初步分類 | 遷移處置 |
|---|---|---|
| `CORE-405-0` | 歷史歸檔 | V4.0.5 當時頂層優先規則，歷史化。 |
| `CORE-405-1` | 歷史歸檔 | V5.0.1 exact upstream binding 退版。 |
| `CORE-405-1A` | 歷史歸檔 | Reference DAIL 檔名勘誤屬歷史工程。 |
| `CORE-405-2` | CORE 只接接口 | Owner / work / receipt 不得互相冒充的原則保留；舊 Lighter 具體 schema 移出。 |
| `CORE-405-3` | 待裁定 | 本地較嚴 Radar 依賴與新 L9 advisory-only 是否衝突，交對對再裁定；禁止先設無 Radar 全域 HOLD。 |
| `CORE-405-4` | 理火 OS 治理／週期 | Final gate 執行／缺口資格由 OS 適用 owner 判定。 |
| `CORE-405-5` | 歷史歸檔 | Same-context reference adapter/trace 退遷移史。 |
| `CORE-405-6` | CORE 只接接口 | Footer 可見性降為按需；不可用狀態欄位冒充已執行。 |
| `CORE-405-7` | CORE 只接接口 | 文件批准、工具實際執行、可用性分離作短界線。 |
| `CORE-405-8` | 僅保留回歸測試 | V5.0.1 接線規範測試入 Annex C。 |
| `CORE-404-1` | 歷史歸檔 | 舊 vertical DAIL inheritance 不複製。 |
| `CORE-404-2` | CORE 只接接口 | 保留能力／owner 分界，實際 DAIL/IR 層由 L9／OS 消費。 |
| `CORE-404-3` | 歷史歸檔 | Reference executor 規格退休。 |
| `CORE-404-4` | 歷史歸檔 | Reference provider/consumer binding map 退休。 |
| `CORE-404-5` | L9 能力倉 | 舊 normalized IR 技術接口如有存活能力由 L9 registry 對應，不移植本地 CORE。 |
| `CORE-404-6` | 僅保留回歸測試 | Prototype harness 成果／局限入測試檔。 |
| `CORE-404-7` | 歷史歸檔 | Reference runtime execution law 屬舊接線階段。 |
| `CORE-404-8` | 僅保留回歸測試 | 過往 smoke／reference 回歸附件化。 |
| `CORE-403-1` | 歷史歸檔 | Formal/Reference lane resolver 不再作故事進入必要分流。 |
| `CORE-403-2` | CORE 只接接口 | 「有來源」不等於「真的已執行」只留短誠實界線。 |
| `CORE-403-3` | CORE 只接接口 | 來源索引不創造外部執行證據／世界事實。 |
| `CORE-403-4` | 歷史歸檔 | Atomic open in both lanes 為舊雙 lane 技術措施。 |
| `CORE-403-5` | 歷史歸檔 | Implementation-absent 版本勘誤；不再推導無 Host 就全域 HOLD。 |
| `CORE-403-6` | 僅保留回歸測試 | 原有針對雙 lane 的測試入 Annex C。 |
| `CORE-403-7` | 歷史歸檔 | 舊版 disposition 說明退歷史。 |
| `CORE-402-1` | 歷史歸檔 | 舊 upstream pointer read lock 退歷史。 |
| `CORE-402-2` | CORE 自有 | 本地 story identity／進入點留下；不自授 OS admission 或 Primary standing。 |
| `CORE-402-3` | CORE 只接接口 | 本地可以說何時具備敘事條件，但不冒充 OS 的 final governance。 |
| `CORE-402-4` | 僅保留回歸測試 | 舊回歸與 predecessor 記錄分入 B/C。 |

## 8｜SAVE／V4.0／V3.11 深層繼承資料定位

| 舊 CORE 條目 | 初步分類 | 遷移處置 |
|---|---|---|
| `S1` | SAVE 持久化 | SAVE 是路線持久化資料；非第五常駐主檔。 |
| `S2` | SAVE 持久化 | relation-first 是續接讀取優先，不是記憶建立權。 |
| `S3` | SAVE 持久化 | 投影與索引不創造新的世界事實。 |
| `S4` | SAVE 持久化 | 單一 material event 有一條有效來源鏈；多個可讀視圖可以存在。 |
| `S5` | SAVE 持久化 | 保存需合法提交，CORE 不代簽。 |
| `S6` | CORE 只接接口 | 未決付款、契約、親密、未玩事件不得從關係感覺自動成交。 |
| `S7` | CORE 只接接口 | 路線讀取不可漏掉重要 NPC／機構關係。 |
| `S8` | SAVE 持久化 | HOT/MASTER/Index 按需讀取；寫入資格由 SAVE owner。 |
| `R4-0` | 歷史歸檔 | V4.0 批准／父系紀錄作歷史索引。 |
| `R4-1` | CORE 自有 | 保留 CORE 本地生命週期身份，不延續舊治理主權。 |
| `R4-2` | CORE 自有 | 觀止故事週期定位成 route/scene 局部持續，而非理火計算週期。 |
| `R4-3` | 理火 OS 治理／週期 | 理火週期定義交 OS L8。 |
| `R4-4` | 歷史歸檔 | 雙週期 Primary binding 退出現行。 |
| `R4-5` | CORE 自有 | Guanzhi 本地 identity 最小保留；不與 OS cycle_ref 合併。 |
| `R4-6` | 理火 OS 治理／週期 | Vertical receipts 的技術 manifest 由 applicable owner 實現。 |
| `R4-7` | CORE 只接接口 | receipt 不能等於執行、事件，短原則保留。 |
| `R4-8` | WORLD／領域真相 | 發生事實與現場可觀測來源回 WORLD/Domain，CORE 僅接 delta。 |
| `R4-9` | CORE 只接接口 | 本地可以投影 owner return，但不能創造 owner standing。 |
| `R4-10` | 導演心法 | Agent 交帳場景何時必要由 Director/適用 owner 定，不作固定台詞。 |
| `R4-11` | 人物意願 | 玩家授權代理角色的行為，需保留真實授權邊界。 |
| `R4-12` | 待裁定 | Radar direction advisory 不等於其調用硬前置；待 OS/L9 接線共同確認。 |
| `R4-13` | 待裁定 | 成人場景入口、年齡與同意是必要保護，但原補充協議及現行適用範圍待核；不得默默撤掉。 |
| `R4-14` | 導演心法 | 玩家可選語言語域；保持人物聲紋，不由 CORE 決定台詞。 |
| `R4-15` | 待裁定 | CERI 先於 Narrator 的特殊依賴是否具新 OS 接口待核；不得用假回傳充數。 |
| `R4-16` | WORLD／領域真相 | 時空道人是世界人物與玩家接觸能力，不是 CORE oracle 權限。 |
| `R4-17` | CORE 只接接口 | 只保留跨 owner 不偷造事實／不回鑄／UNKNOWN 原則。 |
| `R4-18` | 歷史歸檔 | 舊 World/Director pointer repair 作遷移歷史。 |
| `R4-19` | 僅保留回歸測試 | Static compatibility matrix 作工程測試。 |
| `R4-20` | 歷史歸檔 | Joint package/Current status 過往沿革。 |
| `R4-21` | CORE 只接接口 | Graph not pipeline 作簡短引導。 |
| `R4-22` | CORE 自有 | 本地 story dispatch 需要當回合適用 owner 結果；無 Central Lighter seal 預設。 |
| `R4-23` | 歷史歸檔 | 舊版最短口訣僅存歷史，VNext 另寫。 |
| `RC2-0` | 歷史歸檔 | V3.11 雙 Primary root 憲法退休。 |
| `RC2-1` | 理火 OS 治理／週期 | Vertical receipt manifest 一整份不內嵌。 |
| `RC2-2` | 理火 OS 治理／週期 | 大包 packet schema 退出本地 core。 |
| `RC2-3` | CORE 自有 | 本地 story/scene 進入身份可保留，重 receipt 機制不沿用。 |
| `RC2-4` | 歷史歸檔 | LIHUO cycle binding receipt 老設計退休。 |
| `RC2-5` | 待裁定 | Constraint admission 的誰能實際設限仍須按現行 owner；不讓 CORE 重造裁決。 |
| `RC2-6` | CORE 只接接口 | semantic owner 的結果可被引用，不由 CORE 簽發他人 return。 |
| `RC2-7` | 待裁定 | CERI actual provider return lineage 待現行接線裁定。 |
| `RC2-8` | 導演心法 | Narrator 文字顯影按實際可用能力處理，不冒充 provider 已執行。 |
| `RC2-9` | CORE 自有 | 本地 story dispatch eligibility 概念可保留；舊大型 receipt schema 不保留。 |
| `RC2-10` | SAVE 持久化 | SAVE disposition 由真正持久化結果判定。 |
| `RC2-11` | CORE 只接接口 | 記錄來源與表述區分，不在 CORE 建一座證據法庭。 |
| `RC2-12` | 歷史歸檔 | Ticket/Execution/Receipt/Packet 全量型別系統退出。 |
| `RC2-13` | 歷史歸檔 | 跨週期 binding 舊 topology 退休。 |
| `RC2-14` | CORE 只接接口 | 責任拓撲非單線流程；只保留必要界線。 |
| `RC2-15` | 歷史歸檔 | V3.10 compatibility bridge 與舊版本對照退休。 |
| `RC2-16` | 僅保留回歸測試 | 舊反向稽核測試轉 Annex C。 |
| `RC2-17` | 僅保留回歸測試 | Legacy regression 轉 Annex C；挑出故事級保護重新測試。 |
| `RC2-18` | 歷史歸檔 | 舊口訣／收束不作現行權威。 |

**盤點覆蓋：** 此表列出 108 個舊核心條款定位（V4.1.2 操作段、V4.0.5–4.0.2 接線段、SAVE、V4.0 根層與 V3.11 RC2 子條款），並另列 V3.10 內嵌的代表性語義模組。這是討論分派表，不宣稱原始全文每一個嵌套 YAML 欄位都已有最終 Owner。



## 9｜V3.10 內嵌語義的「有價值部分」：分送前不可遺失

這部分佔據舊 CORE 中段的大型 \`PART B｜CANONICAL VERTICAL DAIL\` 與 \`PART C｜WIRING CONTRACT\`。它們不是「工程垃圾」，但已經不適合全文留在 CORE Main。

| 舊模組／節點 | 先定位 Owner | 本次保留的實質邊界 |
|---|---|---|
| \`CORE.SITUATIONAL_CONTEXT\`（1.1） | CORE cursor + WORLD/Domain | 場合、公私、在場者、誰能看到什麼；情境訊號不創造法律事件 |
| \`GUANZHI.COST_CAUSALITY_ROOT\`（1.4） | WORLD/Domain + Director 用於張力 | 行動與選擇可能有時間／金錢／名聲／關係代價；候選成本不等於已發生 |
| \`CORE.ACTOR_DRIVE_DYNAMICS\`（1.5） | Character + Director／Main | 人物野心可碰撞，不能變成預先強迫的固定決策 |
| \`CORE.SCENE_FIELD_STATE_CONTINUITY\`（1.6） | CORE transient view + Character/Domain | 疲勞／餘波／注意力可能延續；場態不是同意，也不是 SAVE 事實 |
| \`DOMAIN.EVENT_STATE_MACHINE\`（1.9） | WORLD／Domain | 計畫、開始、繼續、完成、未決必須區分；呈現不自動使事件完成 |
| \`DOMAIN.REFERENT_SCOPED_KNOWLEDGE_PROVENANCE\`（1.10） | WORLD／Domain + SAVE | 某人知道／懷疑／聽聞一事不等於另一人也知道；流言不等於事實 |
| \`CORE.PERSONA_SOVEREIGNTY_FIREWALL\`（1.11） | Character + Director／Narrator 忠實度 | 不把人物漂白成道德教師或自動療癒版本 |
| \`CORE.PERFORMANCE_FRAME\`（1.12） | Character + Director | 公開演出與私人心意分離；分類不等於接受演出或同意親密 |
| \`STORY.NO_NARRATIVE_JUDGE\`（1.14） | CORE 主權界線 + OS 不重複裁決 | 不造一個超越人物與世界的「敘事法官」 |
| \`CORE.CHARACTER_ADAPTER\`（1.15） | CORE interface + Character | 人物基線能供場景引用，但基線不是當前決定 |
| \`CORE.CAST_RELEVANCE_CANDIDATES\`（4） | Director + 本地檢索／L9 能力 | 候選人物不是已在場，也不能憑提名創造出場原因 |
| \`CHARACTER.ACTOR_VIEW_LOCK / CAUSE_CONTINUITY / DECISION_AUTHORSHIP\`（5–8） | Character | 主觀知情視角、歷史因果、人物親自作決定 |
| \`PLAYER.DELEGATED_CHARACTER_AUTHORITY\`（9） | 玩家授權 + Character/Director | 代理授權不等於無限替玩家行事 |
| \`DOMAIN.SHARED_COLLISION\`（10） | WORLD／Domain + Character | 多股力量碰撞可以有結果，但結果由實際事件與選擇建立 |
| \`ADULT.*\`（1.2–16 等） | 各適用成人／人物／世界／語言 Owner；具體接線待裁定 | 年齡、當次同意、行動範圍、事件完成與描寫語域不得互相代簽 |
| \`STORY.CERI_SCOPE_AUTHORITY / STORY.CERI_VISIBLE_LANGUAGE_COVERAGE\`（17A/B） | 語言 Provider／現行 OS 接口待釐清 | 語域與顯影不能冒稱已執行 provider 回傳；不能把原流程直接複製 |
| \`CORE.STORY_VISIBLE_RELEASE_ELIGIBILITY\`（17B.1） | CORE 本地 dispatch + 相關顯影 Owner；待裁定 | 保護顯影忠實性，但不得自創一個新 Lighter |
| \`CORE.CONSTRAINT_ADMISSION_GATE\`（17-0） | LIHUOS／適用限制 Owner；待核 | 真正限制必須有來源；不能靠敘事偏好編造新硬牆 |
| \`PART C｜WIRING CONTRACT\` | ARCHIVE / REGRESSION / 適用 OS／L9 | Normalized IR、Boot/Cast/Provider/Narrator wiring 不再由 CORE Main 常駐定義 |
| \`成人互動觸發式補充協議 V0.2\` | 附件來源保留，適用法位待確認 | 人類選擇、人物成年與當次同意不可互代；不在此作協議新增或廢止 |

**此處為初步「遷移判斷」，不是對個別 provider／合同的法律效力裁定。** 牽涉安全、授權、身體史和當次同意的實質要求，必須完整保護；不採用「為了減少 Token，所以全部刪掉」的手法。

## 10｜對對需要再判的事項（DISPUTED）

1. **Radar 依賴：** 舊 CORE 的「沒真正消費 Radar 就 HOLD」如何與 L9 advisory-only 及 Chat 介面相容？保留何種極薄本地責任？
2. **CERI/Narrator 顯影依賴：** 現行是否存在可實際調用的獨立 provider／返回？若只具文件規格，應如何避免假執行與不必要的全場阻斷？
3. **成人場景接口：** 既有成人觸發協議在 VNext 的適用性、持有 Owner、玩家選擇與角色當次自主如何寫得清楚但不變成每回合教條？
4. **Domain 層：** 舊 CORE \`DOMAIN.EVENT_STATE_MACHINE\`、\`REFERENT_SCOPED_KNOWLEDGE_PROVENANCE\` 是移進 WORLD Annex、獨立 Domain，還是僅需各 Owner 維持實質邊界？
5. **Story Dispatch：** 「必要 Owner 未完成不得冒充完成」是最低邊界；哪些必需結果存在，不能用這個簡句自行削除？
6. **Time-space Daoist／關係式 Cast：** 這些世界／導演能力的具體調用分屬 WORLD、Director 或 L9 哪一塊？不能因 CORE 過度工程而把它們拔掉。
7. **SAVE 技術責任：** CORE 是否只需 \`persistence candidate + actual disposition\` 兩個界面，還是當前持久化還有少量不可省略的材料？
8. **舊 V3.10 人物／關係語義：** 如何避免在拆檔後被新導演忽略，而不是重新把整套 DAIL 塞回 Main？

## 11｜新的回歸測試不應重新膨脹 MAIN

**永遠值得測的故事行為：** 普通酒館夜晚能繼續、角色可以拒絕而非永久鎖死、契約未決不自動成交、跨日後疲勞與債務持續、不同 Route 的關係不相互覆蓋、人物不知道不該知道的事、玩家沒授權的關鍵行動不代行、Radar 訊號不等於命令、工具「有結果」不等於世界「已發生」、SAVE 沒有真實提交不稱已存。

**退到 Annex C 的工程測試：** 舊 Lighter ledger、same-primary identity projection、Formal/Reference lane、V5.0.1→V5.1 pointer、Python fake returns、無 Host 模擬收據等。

測試目標是故事成立，不是要求每段故事隨身背著測試清單。

## 12｜Disposition 總結與下一步

- 新 CORE Main **不沿用歷版整包附錄**；前代文件以來源指標完整保存在 Git 中，歷史說明入 Annex B。
- **先提出四項 CORE Owner＋六工作面接口**，其餘一律不因被 CORE 使用而歸 CORE 所有。
- **Story lifecycle 與 OS cycle 為不同尺度**；取消舊身份升格／跨系統 Primary 綁死。
- **舊 Lighter Release 不是新 OS 需要的儀式**；保存真正必要的 owner-result 防冒充責任。
- **Chat-native 可以工作**；外部工作仍須真實工具／provider 證據。
- 首席研究員與作者對 DISPUTED 條款完成取捨後，再形成乾淨的 CORE VNext Main 草稿；目前 CORE V4.1.2 仍保留原位。

**建議下一工作檔：** \`CORE_ANNEX_B_LEGACY_MIGRATION_LOG_V0.1_WORKING_20261026.md\` 或 \`CORE_ANNEX_C_REGRESSION_SCENARIOS_V0.1_WORKING_20261026.md\`，順序由討論確定；**本次不先寫 VNext 正式 CORE**。

> **CORE 要接得到，不代表 CORE 要把對方整套搬進自己肚子裡。**

> **CORE 不替任何 Owner 做第二份自己。**
