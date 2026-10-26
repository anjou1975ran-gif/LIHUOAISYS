# 觀止 V6｜CORE Annex B — Legacy Migration & Retirement Log
## CORE VNext 舊版工程歷史、接線退役與來源索引 V0.1

**日期：** 2026-10-27  
**狀態：** WORKING / MIGRATION RECORD / NOT RATIFIED / NOT A CORE SUCCESSOR  
**根源對照：** `CORE_ANNEX_A_OWNER_INTERFACE_MAP_V0.1_WORKING_20261026.md`  
**歷史母件：** `觀止青樓/01_GUANZHI_RUNTIME_CORE_V4.1.2_MAIN511_REBIND_HUMAN_RATIFIED_FULL_20261015.md`  
**母件 Git Blob SHA：** `b8ea8c87d7c0683e151e80c8476d780a4087e554`

## 0｜此 Annex 保存什麼、絕不做什麼

這是**歷史／退役說明索引**，不是完整舊 CORE 的第二份拷貝。舊版原檔由 Git 保留；追溯細節時再開原檔。CORE VNext 主文不再逐字承載全部父版，因為「歷史可考」不等於「每一輪故事都要把歷史吃進 Context」。

- **保存：** 舊接線曾經要解決什麼問題、何時被哪一個版本取代、真正該保留的故事保護、指向原章節的索引。
- **退出常駐：** 舊 Lighter governance、Same-ID Primary promotion、完整收據包、Reference/Formal 雙 Lane、防重入 ledger 的詳細 schema、逐層 byte-for-byte 母文。
- **不得宣告：** 舊保護已自然失效、新 OS 已真正 Host 部署、外部 provider 已實際執行、理火 OS V1.1 因本文取得新治理憲法。
- **保留討論權：** Annex A 標為 DISPUTED 的邊界，由作者與首席研究員確認；這裡不私自裁決。

## 1｜歷代結構的形成脈絡（按語義推移，不是新規則）

| 出現於 V4.1.2 內嵌母文的階段 | 當時試圖解決的事 | VNext 方向／目前身分 |
|---|---|---|
| V3.10 | `GENESIS_PATH_SOVEREIGNTY_CONSTITUTION`、薄型 Runtime、人物與 Domain 介面、垂直 DAIL 與 Wiring；含成人觸發補充文本 | **分流取其有效實質。** 人物意願歸 Character、事件真相歸 WORLD/Domain、語言顯影歸原適用 Owner、工程 wiring 作來源與回歸。不可因拆檔丟掉因果／身體／同意的保護。 |
| V3.11 | 觀止／理火雙週期、Vertical receipt manifest／packet、來源收據與證據一致性 | **舊設計退歷史。** 只有真實來源、事件、未決不能被偽造等邊界需要新的極薄表達。 |
| V4.0 | 以當時中央理火 V4.9 與本地故事週期做聯合拓撲修補；Radar、Agent、成人入口、CERI、SAVE 與時空道人等曾在 CORE 聚合 | **從混合主檔分拆 Owner。** 具象的角色／世界能力不因此被刪掉。 |
| V4.0.1 | SAVE 的位置、Relation-First 續讀、唯一真源、多索引視圖與 UNKNOWN 保存 | **歸 SAVE Owner／CORE thin interface。** SAVE 不是 CORE 的第五份主程序，更不是自動提交器。 |
| V4.0.2 | CORE-owned cycle ingress issuer、local eligibility 與 Final Lighter Release 區別 | 本地故事身份與最小續接保留；舊 Gate 與跨系統資格退役。 |
| V4.0.3 | Formal／Reference ingress 雙 Lane 與 evidence 不得自證 | 舊 Lane 退歷史；「有資料／有工具」不等於已執行應保持誠實。 |
| V4.0.4 | DAIL、IR、Provider、Reference executor、Smoke Test 技術層整理 | 技術細節交回 OS／L9 或純回歸，CORE 不常駐第二套 wiring engine。 |
| V4.0.5 | LIHUO V5.0.1 上游綁定、Radar v5、Final Gate、相同上下文來源引用 | 舊 Lighter 技術法位退至歷史；保留故事所需的 Owner 範圍。 |
| V4.1.0 | 從雙 Primary 調整為 `Guanzhi identity → Lighter admission → same identity becomes Primary`；Main coverage／reentry、ledger、final release | **整套跨系統 identity promotion 建議退休。** Route/Scene 的壽命與理火一次 cycle 不同尺度。 |
| V4.1.1 | Reference work trace、same-context evidence、canonical provenance、沒有真正 owner return 不得假稱執行 | 具體 trace objects／RC 測試移 Annex C；誠實表述仍有效。 |
| V4.1.2 | Main V5.1.1 exact binding、RC1 批准層、V4.1.1 父版全文承載 | 這是本次來源，**不是直接改名成 VNext 的母板**。批准歷史保留，當前新設計另審。 |
| WORLD V3.0.0／LIHUOOS V1.1（2026-10-26） | WORLD 主文／附件已分離；理火 OS L0–L7 意義／治理、L8 業務週期、L9 可調用能力、Main 計算；Legacy Lighter 退出現行 control plane | **新前提**。觀止 CORE 只能用最小接口消費新 OS；不能以「舊 Lighter 換字」假裝整合成功。 |

**史料性質：** 上表歸納舊檔各版自述與目前建議的 disposition。VNext 的任何未批准主張不因寫在「方向」欄而成為新現行規則。

## 2｜不應存活為新 CORE 操作機制的舊物

| 舊工程物 | 原定位（可回讀之來源） | VNext 不應複製的東西 | 值得繼承的最小責任 |
|---|---|---|---|
| Same Identity → Primary Promotion | `CORE-410-2/3/3C`、`R4-4` | Local Story ID 被提升為 LIHUO Primary；跨系統同一身份規則 | 使用 `GUANZHI_STORY_REF ↔ LIHUO_CYCLE_REF` 的上下文關聯，不取代 OS 的 cycle 身份 |
| Single Governing Cycle 對觀止的本地代理 | `CORE-410-3B/5/8/9` | CORE 維持 Primary ledger、successor primary state machine | 本地 Route 可延續多次不同 OS cycle |
| Lighter Admission／Final Gate／Final Release | `CORE-410-4/10`、`CORE-405-4` | 用 OS 作為「新 Lighter」強制每場蓋章 | 當輪真正必要 Owner 為阻斷性 HOLD／MISSING 時，不冒充完成結果 |
| Vertical Receipt Packet | `CORE-410-6`、`RC2-1..10` | 每場必生成全部 Manifest、Packet、receipt、Ledger | 實際存在且與當前材料相關的 owner return，可被本地引用 |
| Main Coverage／Reentry | `CORE-410-7..9` | CORE 自判 dirty/stale/coverage/reentry ticket | CORE 只報 material local delta，回交適用 OS owner |
| Reference／Formal 雙 Lane | `CORE-410-14`、`CORE-403-1..6` | 無 Host 便 Global HOLD 或無條件轉 Reference | Chat-native 可做的工作照做；真正外部動作需要真工具實證 |
| Lighter Radar 依賴 | `CORE-405-3`、`R4-12` | 將「有無 Radar 記錄」自動轉成每個場景的命運裁決 | Radar 為 advisory；舊較嚴依賴是否仍適用列 DISPUTED |
| Mandatory Footer | `CORE-410-13`、`CORE-405-6` | 每段故事都印一整行收據欄位 | 按需呈現實際狀態；顯示欄位不是產生執行證據 |
| 大量嵌入 DAIL／IR／Wiring | `V3.10 PART B/C`、`CORE-404-` | 在 CORE Main 重造 Character、Domain、CERI、Provider 的內部法規 | 只保留各 Owner 當輪適用的入口與輸出 |
| 逐字父版與批准史 | `APPENDIX A` 多層巢狀、V4.0 PART/版本註記 | 讓每一次閱讀 CORE 重新載入十多版工程史 | Git 原件可追溯、精簡索引可搜尋、真正有效的責任另見 Annex A |

## 3｜歷史分層讀取方法（避免舊語義倒灌）

```text
現行 CORE VNext（未形成，不得假定）
  ├─ 用適用的 WORLD / Character / Director / SAVE / LIHUOS 現行來源
  ├─ 遇具體舊爭議 → 到 Annex A 找 Owner / DISPUTED
  ├─ 遇「過去為何如此設計」→ 看本 Annex B 的來源條款
  └─ 需要精確條文／比較 → 開舊 V4.1.2 原件相應標題
```

**已取代內容不因出現在舊檔尾端或被逐字保留而恢復現行。** 比如舊 V3.11「Guanzhi Cycle != LIHUO Cycle」曾對當時雙週期有特定意義；不能因此直接推斷 VNext 要復活雙 Primary。現行要說的是兩個不同尺度的生命週期，各有 Owner，以 context binding 交換材料。

同樣，現行 OS V1.1 為文件級 CURRENT，**不是 Host 實體執行已成立**。兩句必須同時為真：Chat-native 不因無 Host 無端阻斷；外部執行不能被文字推演代領。

## 4｜Annex A 明列「歷史歸檔」的舊條款：定位索引

此表從 Annex A V0.1 的 108 項分類抽取，不把詳細 wording 重新寫成 CORE 硬規則。每項可回舊 CORE 以原標題搜尋。

| 舊 CORE 章節定位 | 保存位置／原則 |
|---|---|
| `CORE-410-0` | 歷版 highest-read／批准優先級收至歷史；新正文由現行 index 指路。 |
| `CORE-410-2` | Guanzhi identity → Lighter admission → same primary 的舊接線退休；不得以同 ID 改稱 V1.1。 |
| `CORE-410-5` | 舊雙週期 binding 及後續 same-primary 替代物一併作前代歷史。 |
| `CORE-410-14` | Formal/Reference 雙 lane boot 技術史退附錄；Chat 介面不得因沒有 Host 自動 HOLD。 |
| `CORE-410-14A` | 工程憲法 exact pointer 對照僅留歷史。 |
| `CORE-410-15` | DAIL/IR/Coding 三層分離屬理火／能力系統；舊實作敘述退出。 |
| `CORE-410-17` | 舊 WORLD V2.3.2／LCAPG V3.3.20 伴隨指針僅供版本沿革。 |
| `CORE-410-18` | 舊 supersession map 與 retired enum 僅供遷移核對。 |
| `CORE-410-20` | RC4.2 候選處置及批准史留 Annex B。 |
| `CORE-405-0` | V4.0.5 當時頂層優先規則，歷史化。 |
| `CORE-405-1` | V5.0.1 exact upstream binding 退版。 |
| `CORE-405-1A` | Reference DAIL 檔名勘誤屬歷史工程。 |
| `CORE-405-5` | Same-context reference adapter/trace 退遷移史。 |
| `CORE-404-1` | 舊 vertical DAIL inheritance 不複製。 |
| `CORE-404-3` | Reference executor 規格退休。 |
| `CORE-404-4` | Reference provider/consumer binding map 退休。 |
| `CORE-404-7` | Reference runtime execution law 屬舊接線階段。 |
| `CORE-403-1` | Formal/Reference lane resolver 不再作故事進入必要分流。 |
| `CORE-403-4` | Atomic open in both lanes 為舊雙 lane 技術措施。 |
| `CORE-403-5` | Implementation-absent 版本勘誤；不再推導無 Host 就全域 HOLD。 |
| `CORE-403-7` | 舊版 disposition 說明退歷史。 |
| `CORE-402-1` | 舊 upstream pointer read lock 退歷史。 |
| `R4-0` | V4.0 批准／父系紀錄作歷史索引。 |
| `R4-4` | 雙週期 Primary binding 退出現行。 |
| `R4-18` | 舊 World/Director pointer repair 作遷移歷史。 |
| `R4-20` | Joint package/Current status 過往沿革。 |
| `R4-23` | 舊版最短口訣僅存歷史，VNext 另寫。 |
| `RC2-0` | V3.11 雙 Primary root 憲法退休。 |
| `RC2-4` | LIHUO cycle binding receipt 老設計退休。 |
| `RC2-12` | Ticket/Execution/Receipt/Packet 全量型別系統退出。 |
| `RC2-13` | 跨週期 binding 舊 topology 退休。 |
| `RC2-15` | V3.10 compatibility bridge 與舊版本對照退休。 |
| `RC2-18` | 舊口訣／收束不作現行權威。 |

## 5｜Annex A 明列「僅保留回歸測試」的舊條款

具體案例如何測，另見 Annex C。過去的測試名稱與設計意圖可以保存，但不得用「以前有測試碼」暗示此刻已經實際執行。

| 舊 CORE 章節定位 | 保存位置／原則 |
|---|---|
| `CORE-411-1` | Reference Work Trace 的來源真偽核驗作測試，不寫進正常故事回合。 |
| `CORE-411-2` | Reference progress projection 作兼容驗證資料，非新本地 state machine。 |
| `CORE-411-3` | 證據不足不得冒充完成仍有效；具體 Reference guard 機制移出正文。 |
| `CORE-410-19` | RC4.2 SGC、receipt、ledger 逐項回歸清單入 Annex C；世界級保護另保留。 |
| `CORE-405-8` | V5.0.1 接線規範測試入 Annex C。 |
| `CORE-404-6` | Prototype harness 成果／局限入測試檔。 |
| `CORE-404-8` | 過往 smoke／reference 回歸附件化。 |
| `CORE-403-6` | 原有針對雙 lane 的測試入 Annex C。 |
| `CORE-402-4` | 舊回歸與 predecessor 記錄分入 B/C。 |
| `R4-19` | Static compatibility matrix 作工程測試。 |
| `RC2-16` | 舊反向稽核測試轉 Annex C。 |
| `RC2-17` | Legacy regression 轉 Annex C；挑出故事級保護重新測試。 |

## 6｜不因退工程而消失的故事保護

| 實質保護 | 界線與去處 |
|---|---|
| 人物自主／決定因果 | Character 主權；CORE 只承接真正成立的行動與已造成的關係後果 |
| 事件分段 | WORLD/Domain 判斷計畫、發生、完成、未完成；不因敘述飄過而自動成交 |
| 知情範圍 | 不因全知旁白就讓角色知道未被告知的秘密 |
| 世界代價／階級與權力 | 保留政治、制度、交易、暴力等已成立的世界結構；候選後果不等於實發 |
| 未決／UNKNOWN | SAVE／當線狀態應讓未決活下來，而不是自動塌縮成確定 |
| 玩家與角色代理 | 玩家授權只在該授權範圍；角色意願不能由導演猜測代簽 |
| 成人與身體歷史 | 年齡、身體史、當次同意、事件範圍不能混同；歸適用 Owner，具體接線待判 |
| 顯影忠實／語域 | 把能生成語句與合法／真實 provider return 分開；CERI/Narrator 問題待判 |
| 雷達建議 | 提醒可供採納或拒絕；不得憑 Radar 直接創造角色選擇或阻斷所有故事 |
| SAVE 真實提交 | 讀取、投影、保存有不同法位；沒成功 commit 不說已保存 |

## 7｜尚未取得遷移裁定的邊界

沿用 Annex A 第 10 節的 DISPUTED 清單：Radar 啟動義務、CERI/Narrator 的實際 Provider 責任、成人觸發與可見語言範圍、Domain 的最小存放位置、Story Dispatch 的必需 Owner、時空道人／Cast 能力、SAVE 提交界面、V3.10 人物關係語義接續。

**本 Annex 不裁定新接口**；也不假定外部能力存在。「內容保留」不等於「機制不變」，「機制退役」不等於「原本想守護的實質消失」。

## 8｜遷移完成判準（提議，非自動 PASS）

- 新 CORE Main 不再逐字內嵌舊版全文；可回溯至來源檔與章節。
- 新 CORE 四項本地責任清楚；不再維護第二套 Main、Lighter 或跨 Owner state machine。
- 新 OS 只在當輪適用且能真實獲得的範圍接入；不假稱 Host、provider、receipt 已執行。
- WORLD、Character、Director、SAVE、CERI 等保有本身主權；未決／跨 Route 不因減量而損壞。
- Annex C 故事級案例經真的場景演練與人工／適用工具評估，才可記 PASS；本 Annex 本身不提供通過證據。

**本檔結論：** 歷史要保留，但不再佔據新 CORE 的日常呼吸。

