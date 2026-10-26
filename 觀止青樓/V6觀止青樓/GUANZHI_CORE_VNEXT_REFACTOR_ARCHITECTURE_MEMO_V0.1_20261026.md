# 觀止 CORE VNext｜去過度工程化與理火 OS V1.1 接線重構
## 架構討論 MEMO V0.1｜提交作者 × 理火AI首席研究員「對對」討論

**日期：** 2026-10-26  
**狀態：** `DISCUSSION_DRAFT / NOT_RATIFIED / NO_CORE_CHANGE / NO_DEPLOYMENT`  
**範圍：** 本次先談 CORE 的職責與結構，導演心法僅定交界；不在此稿重寫 CORE、Director、WORLD 或理火 OS。

## 一、問題定義

舊版 `GUANZHI RUNTIME CORE V4.1.2` 的 GitHub 主檔約 **34.5 萬字元、13,328 行**。從第一個「完整繼承父版」附錄起，後續約佔檔案篇幅 **79%**。這不等於其中 79% 全無效；它顯示了「歷史必須保存」被實作成「每次讀 CORE 都攜帶歷史全文」。

核心問題不只是太長，而是**角色錯位**：CORE 同時承擔觀止本地週期、舊理火 V5／Lighter 接線、Primary 身份、Main Reentry、收據與 Final Gate 條件、Ref/正式雙 Lane、測試和逐版批准史。大量篇幅用於證明前述元件各自有沒有資格，而非讓觀止正常運作。

- **實證 A：** `CORE-410-2` 仍以 `Guanzhi Identity → Lighter Admission → Same Identity Becomes Primary` 描述主拓撲。
- **實證 B：** `CORE-410-4` 的 Owner Map 仍把治理資格、Final Gate、Final Release 指向 `LIHUO_LIGHTER`。
- **實證 C：** `CORE-410-10` 的 Story Dispatch 以多組 Lighter/Main/ledger/receipt 條件串起來。
- **實證 D：** 多層 `APPENDIX A｜完整繼承` 保留 V4.0.5、V4.0.4、V4.0.3、V4.0.2、V4.0.1、V4.0、V3.11 等歷代母版，甚至包含現已退位的「雙週期」語義。

**新前提已不同：** `LIHUOOS V1.1` 的 L0 說明 L0–L7 提供意義／治理依據、L8 跑一次理火週期、L9 管可調用能力、Main 做 compute；Legacy Lighter 已退休為現行控制層，L9 只接能力、不接裁決權。L8 自己亦明白宣告「整合不等於重複所有元件契約」。

**因此：不能把 V4.1.2 的 Lighter 法位換個名字寫成 OS，就稱為接線完成。**

## 二、核心主張

> **CORE 只負責「觀止如何延續成為正在發生的世界」；理火 OS 負責生成與治理週期；WORLD 管世界成立的條件；人物自行決定；導演負責戲劇理解與顯影；SAVE 保存具資格的路線記憶。**

這是責任分離，不是把觀止縮成沒有自家運作能力的 OS 前端。CORE 仍須知道觀止此刻的時間、場域、事件狀態、誰在場、哪些選擇真的發生、還有哪些事未完成。但它**不自己裁判**理火的 execution、qualification 或 final release。

**關鍵工作句：**「CORE 不再替理火證明理火；CORE 專心讓觀止的生活繼續。」

## 三、提議的 CORE 主文：六項工作，不多發一份憲法

| 主文責任 | CORE 需要留下的最小內容 | 不應由 CORE 重複的內容 |
|---|---|---|
| 1. 本地故事入口與續接 | 當前 Story／Route／場景身份；本地 cycle／attempt 的參照和起停條件；必要的上下文來源 | 把本地 identity 自行宣告為 OS Primary，或複製 OS admission 憲法 |
| 2. 時間與世界進行 | 當前時點、日夜／跨日、場內外並行事件、已發生與尚未發生之差別 | 重寫 WORLD V3.0.0 的曆法、商業、物理、身分與社會全文 |
| 3. 人物與事件狀態 | 當事人位置、可見資訊、待決行動、事件造成的真實狀態變化；詢問對應 owner | 把人物傾向寫成固定反應、把傳聞與計畫升格已發生 |
| 4. 導演交接 | 把局勢、場景張力、參與者、未決問題與可用結果交給 Director；接收敘事提案 | 取代 Director 構思劇情，或由 Director 代 Character/WORLD 作主 |
| 5. 記憶與存檔 | 接收具來源的事件 delta；需要時讀取／請求 SAVE；保持未知、路線隔離與讀寫分工 | 在 CORE 內重建 HOT／MASTER／索引資料庫，或由摘要製造 canon |
| 6. 理火 OS 接口 | 發起符合當下 owner 的調用請求；接收 OS 已有的有效回傳、HOLD、缺口；據此處理可見輸出 | Lighter V5 的舊 gate、完整收據 schema、R1/O9/I9/R2/R3+ 詳規、L9 工具內部規格 |

**核心不應再收編：** Main 的計算動力學、L8 週期演算法、L9 Capability Registry、L0–L7 的理論與合法性裁定、工程回歸測試正文、來源批准長文。這些應由原 owner 保管或經索引調用。

## 四、文件分拆方案（提議，不是新增主控層）

| 文件 | 承載什麼 | 讀取策略 |
|---|---|---|
| `01_GUANZHI_CORE_VNEXT_MAIN_WORKING.md` | 六項本地責任、短接口、常見續接／暫停情境；**唯一新 CORE 主正文** | 故事執行時常駐或優先讀 |
| `CORE_ANNEX_A_OWNER_INTERFACE_MAP.md` | 舊 CORE 條款到 WORLD／Character／Director／SAVE／OS L8/L9 的責任對照；OS 版本與未決接線 | 需要接線／維護才讀 |
| `CORE_ANNEX_B_LEGACY_MIGRATION_LOG.md` | V3.11～V4.1.2 歷史變更、被取代的雙週期與舊 Lighter 條文、批准資料與 Git 精確來源 | 問題追溯才讀；**不整本逐字塞回新 CORE** |
| `CORE_ANNEX_C_REGRESSION_SCENARIOS.md` | 真實可檢查的事件測試：跨日、錯誤來源、拒絕、場外事件、錯誤 SAVE 等 | 回歸測試／審計才讀 |

附件是參考，不是新的第五主模組。也不應把附件全文再嵌進 MAIN；否則只是換資料夾的過度工程。

## 五、接入理火 OS V1.1 的最小契約

**建議只保留一組短交界：**

```text
觀止現行 Story 狀態／玩家行動
  → CORE 解析本地時點、場景、事件候選與相依的真實資料
  → WORLD／Character／Director 等各自形成其負責的判斷或提案
  → 涉及理火治理的生成／顯影由適用 OS owner / L8 處理
  → CORE 接收合格回傳、HOLD 或缺口，不能自己補造資格
  → 已實際發生的世界變化回到對應 owner／Route SAVE
```

這是**責任交接示意**，不是新強制線性 pipeline。探索性推演可以不形成世界事實；敘事成文、外部副作用、SAVE 寫入須依各自實際適用的法位處理。

**特別待決：** 舊 `NO_STORY_WITHOUT_LIGHTER_RELEASE` 的職責**不能直接刪除、也不能改標為 `OS_FINAL_RELEASE` 就算已實作**。必須由對對確認現行 OS 哪個 owner 持有對應資格、實際回傳是何物，以及在 host 尚未部署的文件環境如何誠實處置。現行 OS V1.1 是 **document-level current**，不等於 Host implementation 已完成。

**Radar：** 觀止可維持本地故事依賴，但接收 L9 Radar V6 的定位是 advisory；雷達結果不自動取得生成否決權、I9 授權或角色主權。

## 六、遷移方式：重建乾淨主文，不在舊卷宗上繼續打補丁

1. **盤點：** 將 V4.1.2 的每一個*仍具效力的實質義務*歸入 `CORE_LOCAL / WORLD / CHARACTER / DIRECTOR / SAVE / OS / ARCHIVE / DISPUTED`；保留一對一來源指標。
2. **提純：** 先以六項責任寫一份可以獨立讀懂的 CORE 主文；不抄接線長文、不重建理火憲法。
3. **處理衝突：** 舊 Lighter V5 介面、雙週期歷史、V2.3.2 WORLD 指標與新 OS／WORLD 的差異列入公開待決清單；不私自挑一條升格。
4. **測試：** 先用實際故事案例檢查*是否守住人物自主與世界因果*，再檢查接口；不得只用 schema/receipt PASS 代表故事成立。
5. **批准／切換：** 對對與人類確認 owner 分工及缺口後，再提出 CORE successor；原 V4.1.2 原檔保留作版本歷史，不冒稱新 CORE 已部署。
6. **導演後續：** 等 CORE 主權分工清楚，再為 Director 做同樣的去工程化；不能先讓 Director 吞下 CORE 刪掉的治理條款。

## 七、測試場景（討論時請對對挑戰）

- **普通的一晚：** 玩家沒要求存檔，也沒大型事件，是否仍能自然對話、營業、吃飯、睡覺，而不強制展開一整張收據表？
- **人物拒絕：** 角色說不時，誰保有決定權？CORE 能否正確保留未決與後果，不把拒絕寫成萬年固定人格？
- **跨日生活：** 玩家睡一晚，已具條件的場外事件會進行；未簽約的交易不能自動完成。
- **跨線誤植：** 別的 Route 已發生的關係、付款與死傷，不可直接進入本線。
- **錯誤來源：** 若人物卡與 WORLD V3.0.0 衝突（如李清照足史已校正案例），核心不在暗中自行裁定歷史真相，而是指向 owner 與明確校正。
- **治理缺口：** 若 OS 只有文件資格、沒有實際主機回傳，CORE 不能虛構 L8/L9/Final Release 已成功，更不能因為卡住就自行取消所有敘事責任。
- **雷達誤報：** Radar 只提出疑慮，不藉此關閉合理劇情，也不竊取角色選擇。

**衡量方式不是 Token KPI 或更高的 PASS 數量，而是：** 常規故事能不被工程解釋打斷、既成因果不丟失、未知可保存、角色仍能作真選擇、owner 清楚，且沒有偽造執行／收據／部署事實。

## 八、請「對對」首席回答的四個架構問題

1. **CORE 的最小不可再縮職責**究竟是哪幾項？上述六項是否混入 WORLD、SAVE 或 Director 的主權？
2. **OS V1.1 與舊 V5 Lighter 接縫：** 哪個實際 owner 接住 admission、reentry、release 的判定？若現階段只是文件規格，應如何在 CORE 明示待接線而不偽報已實跑？
3. **單一生成週期與本地故事生命週期**是否應區分身份？如何保持同一身份的有效性，又不在 CORE 復活「雙 Primary／雙收據憲法」？
4. **反過度工程的最小證據形式：** 哪些真正需要執行時檢查、哪些保留事件索引便夠、哪些歷史測試應永久退出常駐主文？

---

**本 MEMO 不請求直接批准新 CORE。** 它只提出一個可被反駁的責任配置，供人類與對對先討論，再決定是否施工。

**結語：** **讓 CORE 維持觀止的生命，不要再讓 CORE 自己扮演整套理火法庭。**

### 參閱來源

- `觀止青樓/01_GUANZHI_RUNTIME_CORE_V4.1.2_MAIN511_REBIND_HUMAN_RATIFIED_FULL_20261015.md`（特別是 `CORE-410-2/4/10/12/16` 與完整繼承父版附錄）
- `觀止青樓/V6觀止青樓/02_GUANZHI_WORLD_V3.0.0_MAIN_HUMAN_RATIFIED_20261026.md`、同版 `ANNEX`。
- `LIHUOOS/V1版本/L0_INDEX_SOURCE_VERSION_V1.1.md`、`L8_LIHUO_OPERATING_CYCLE_V0.3_WORKING_20261025.md`、`L9_DAIL_CALLABLE_CAPABILITY_REPOSITORY_V1.1_20261026.md`、`LIHUOOS_V1.1_ACTIVATION_RATIFICATION_20261026.md`。
- 人類提供：《基於DAIL作業系統的企劃書（理火會議紀錄）》——方向參考，非已實證 Runtime 技術規格。