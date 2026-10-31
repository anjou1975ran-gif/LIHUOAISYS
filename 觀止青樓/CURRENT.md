# 觀止青樓｜CURRENT 正式入口

**啟用日期：** 2026-10-30；**最新相容性／依賴鎖更新：** 2026-10-31（Asia/Taipei）
**最新人類指令：** 「OK 動手改，順便注意 CORE 那邊跟導演那邊很多還沒指向新的 OS 1.4.1 版本。」
**狀態：** `HUMAN_AUTHORIZED / CURRENT_POINTER_ACTIVE / CHAT_NATIVE_OPERATION_ACTIVE / NON_HOST_MODE`
**未取得：** `HOST_DEPLOYED`、`INDEPENDENT_RUNTIME_PASS`、`PROVIDER_EXECUTION_RECEIPT`。不因正式指標切換就冒稱外部程序已部署或43項回歸已驗收。

## 現行 V3.0.0 組件

| 組件 | 唯一 CURRENT 正文（完整倉庫相對路徑） | 作用 |
|---|---|---|
| CORE | [觀止青樓CORE_V3.0.0.md](V6觀止青樓/V3.0.0/觀止青樓CORE_V3.0.0.md) | Route、Scene、Time、Delta、L8 入場、SGER 與專項 dependency 對接 |
| DIRECTOR | [觀止青樓導演新法V3.0.0.md](V6觀止青樓/V3.0.0/觀止青樓導演新法V3.0.0.md) | 人物池優先、場景與人物生成、顯影 |
| CERI | [觀止 CERI V1.0.1](V6觀止青樓/V3.0.0/觀止_CERI_全場景語言暨原生成人心法_V1.0.1_正式完整版_20261031.md) | A 全場景語言；B 原生 10A；C 21 卡；成人專項 mandatory dependency |
| WORLD MAIN | [觀止青樓主世界觀V3.0.0.md](V6觀止青樓/V3.0.0/觀止青樓主世界觀V3.0.0.md) | 世界、時間、制度與場域 |
| WORLD ANNEX | [觀止青樓世界觀附件V3.0.0.md](V6觀止青樓/V3.0.0/觀止青樓世界觀附件V3.0.0.md) | 世界附件 |
| CHARACTER POOL | [觀止人物池(73人)V3.0.0.md](V6觀止青樓/V3.0.0/觀止人物池(73人)V3.0.0.md) | 既有人物候選基線；選角優先 |
| 原生人物 | [觀止青樓原生人物 ROUTE SAVE 模板.md](V6觀止青樓/V3.0.0/觀止青樓原生人物%20ROUTE%20SAVE%20模板.md) | 人物池無合適人選時才原生 |

## 運作指向

- **唯一理火作業系統：** LIHUOOS V1.4.2；effective L8 V1.3.2、effective L9 V1.2.3、Main V5.1.1＋V5.1.2 正式補丁（不在觀止另建 OS）。
- **每個 Director 故事回合：** 先進同一 effective L8 V1.3.2；T1/T2/TM 由 effective L9 V1.2.3 的 Light Trace binding 供應，並形成 SGER，故事正文後顯示原生 Compact Visible Cycle Receipt，並另出 L9 Radar Report。不得跳過入場、只留狀態標籤或假造 Trace、Main Return、Provider receipt。低複雜節拍於週期內依法標 N/A，不整體 bypass。
- **語言／成人專項：** CERI A 全場景共用；Task Entry 一旦判定 `ACTIVE_ADULT_SCENE / ADULT_SPECIALTY_MANIFESTATION_REQUIRED`，CERI V1.0.1＋適用 B／C 方法即為 REQUIRED dependency。沒有 `CERI_WORK.status=COMPLETED` 與可回讀 `CERI_WORK_RECORD`，不得直接進成人專項 manifestation；外部 Provider 未要求時可為 `NOT_APPLICABLE`，不建立第二套 Adult Cycle。
- **人物：** 優先查本線已存在人物與 73 人池；無適合者才原生；角色到場、決策與關係變化各需來源。
- **失敗與歷史：** 已保存之安竹君線賀小滿事件保留，不回滾、不改名為紫蘭；導演須承認未先檢索人物池及未證明 L8 入場的失誤。日後以正確流程避免重犯，不倒改已成立事件。
- **模式：** 本次為 **Chat-native / Non-Host 使用啟動及 Git CURRENT 文件指標切換**；不是獨立 Host 部署，不宣布外部 Provider／所有測試 PASS。
- **SAVE：** 既有 HOT／MASTER 不因此次啟動而重寫，仍需具體授權與真實 Git 操作。

## 歷史保留

倉庫頂層 `01_GUANZHI_RUNTIME_CORE_V4.1.2...`、`03_GUANZHI_DIRECTOR_V4.1.2...` 等舊版文件作為歷史版本保留，不再充當本次 Chat-native 觀止的 CURRENT。VNext／V0.x 亦只作追溯來源。版本指向以本 CURRENT 為入口，應再依後續人類批准更新。

**本檔是 Git 倉庫公開可檢查的 CURRENT 文件指標；文件操作不能直接控制外部 Host Runtime。**
