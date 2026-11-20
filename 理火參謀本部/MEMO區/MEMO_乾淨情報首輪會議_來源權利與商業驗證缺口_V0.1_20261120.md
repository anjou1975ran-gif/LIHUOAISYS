# MEMO｜首輪實跑發現的問題：乾淨情報來源系統 V0.1
**日期：** 2026-11-20  
**來源 Session：** SESSION_20261120_CLEAN_INTELLIGENCE_001  
**法位：** OPEN_ISSUES / WORKING_MEMO / NOT_APPROVED_PATCH / NOT_CLOSED

> 原 `理火商業化/` 的 Clean Intelligence MEMO 保留不改，本檔記載首次參謀本部議事後出現的新證據及問題。未經實測的建議不是既成事實。

## 問題台帳

| ID | 問題／反對 | 為何重大 | 現狀 | 建議下一次處理 |
|---|---|---|---|---|
| CI-01 | 已有 NIQ 等大規模市場數據公司 | 若直接以資料量競爭，沒有可證明競爭優勢 | OPEN / STRATEGIC | 找 3 個被現有方案忽略的付費窄痛點，列對照成本與品質 |
| CI-02 | 來源資料權利不等於轉售權 | 單靠企業交付資料無法合法形成跨客戶 Data Feed | OPEN / LEGAL | 取得實際合約，分別核對自用、加工、聚合、外售、模型訓練 |
| CI-03 | 法律管轄及修法施行日未確定 | 不同司法轄區與跨境資料會造成不同義務 | HOLD / LEGAL COUNSEL | 明確第一個法域、客戶與來源所在地，聘律師做資料權利矩陣 |
| CI-04 | 客戶付費證據為零 | 大量資料沒有 buyer willingness 不能形成生意 | OPEN / COMMERCIAL | 12–15 買家訪談，取得至少 2 份有效付費 Pilot PO |
| CI-05 | 「乾淨」不等於「正確／代表母體」 | Rewards、抽樣不足、資料過期會誘發錯決策 | OPEN / METHODOLOGY | 設抽查設計、樣本範圍、偏差報告與資料衝突保留 |
| CI-06 | 所有試點成本皆為假設 | HKD 1.8M 不是已報價成本，無法證明 ROI | OPEN / ECONOMICS | 招聘／外包／授權／雲商報價 + 實際客戶月費報價 |
| CI-07 | 撤銷同意如何影響下游資料／模型 | 單純標記來源失效不足以撤回衍生物 | OPEN / ENGINEERING | 設 rights-propagation 擴散測試，兼顧合法保存審計摘要 |
| CI-08 | 理火是否增加可衡量優勢 | 不能因套用 LIHUOOS 就宣布比普通 BI 更好 | OPEN / BENCHMARK | A/B 測試：普通 ETL+BI vs rights+evidence+LIHUO qualified report |
| CI-09 | 實體硬體何時才值得買 | 若 Partner API 已可覆蓋，設備成為額外負擔 | DORMANT / CAPEX | 待資料覆蓋缺口與單機成本/回收資料成立再重開 |
| CI-10 | Rights vs Quality 兩個 Gate 容易在執行時混用 | 合法≠真、可追溯≠可轉售 | OPEN / PRODUCT | 單元/整合測試含未授權、過期、衝突、資料更正 |
| CI-11 | 去槓桿或金融替代資料涉及敏感/內幕情報 | 法律與聲譽風險高於首輪價值 | EXCLUDED_IN_PILOT | 不納入第一個 Pilot，後續單獨法律與產品審查 |
| CI-12 | 跨地域銷售與地域偏差 | 同一份價格樣本不能自動推論整個市場 | OPEN / METHODOLOGY | 僅在已定義地區與樣本範圍內發布；另列覆蓋度 |
| CI-13 | 參謀本部本身尚無獨立 Multi-agent Runtime | 同一模型多席容易意見收斂 | OPEN / META_RUNTIME | 保留 seat 的 R1/T1 前置 Git commit，後續可用獨立模型/盲測比對 |
| CI-14 | 今次 D1 仍由秘書處解釋、未經人類確認 | RESULT RECOMMENDATION 不等於資本授權 | WAITING_HUMAN | 只要求一個最小決策，後續再核准各筆支出 |

## 此輪的具體新發現

- **重排順序：** 原案重點「來源網路先行」→ 本輪建議「先賣可追溯的特定決策產品 + 資料權利服務，然後建立有權重用的合作網路」。
- **不需重造底層：** 初版採 PostgreSQL、API、物件儲存、可追溯事件/版本與開源元資料標準；新技術研發限 Rights Propagation 及 Conflict-Aware Evidence Graph 候選。
- **費用為保守上限假說：** HKD 1.8M / 90d 只是風險規模參考；不得視為已報價或批准。
- **競品證據：** NIQ 2025 10-K 參照 https://www.sec.gov/Archives/edgar/data/2054696/000162828026012572/niq-20251231.htm
- **隱私風險：** 台灣個資法、歐盟 GDPR 與 FTC 地點數據執法；每項要依實際法域核對，而非以通用免責聲明替代律師審查。

## MEMO 版本治理
任何 CI-xx 的 CLOSED 必須由新的可查來源、實際測試或人類決定支持；不許把現在的 OPEN 改成歷史已解決。後續新失敗用新 Session / 新 Event / 新版本收容。
