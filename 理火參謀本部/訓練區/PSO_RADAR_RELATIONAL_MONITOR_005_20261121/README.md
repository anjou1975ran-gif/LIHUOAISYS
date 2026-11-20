# PSO-RADAR-RELATIONAL-MONITOR-005｜關係變動與語義盲點

**日期：2026-11-21｜執行身份：GPT-6 / CHAT_NATIVE_SAME_MODEL_REFERENCE**
**地位：本地 Python 實際執行的工程參考；未部署獨立 Radar、未完成獨立模型探索效益比較。**

本次不是替雷達再增加新的官僚程序，而是把 004 那個「訊號能否撤回與再開」的概念，變成真正能跑、能被故意打壞的實驗，並且找出它的失效條件。

## 實際完成
- 23 項 Python 單元測試 PASS（3 個虛構案例 A/B/C，共 20 個事件）。
- 5 種故意破壞的變體全部被測試抓到：忽略地點、忽略日期、忽略撤銷、忘記舊狀態、隱藏來源更新。
- Case D 額外 3 個事件：GRANTED 的授權只允許展示，實際擬做付費衍生分析，監測器卻沒有訊號。這是 **KNOWN_SEMANTIC_BLINDSPOT**，不是成功率的一部分。
- 原始程式、案例與測試碼全部保存；舊 PSO-003 的 18 份 label input 沒有虛構成已跑過。
- 全部工作是同一 ChatGPT 工作節點設計、由本地 Python 執行；不是獨立 AI Radar 感知成效。

## 入口
- [監測器原始碼](radar_relation_monitor.py)
- [A｜活動中心時段](CASE_A_SITE_RELATIONS.json) / [B｜資料授權更動](CASE_B_RIGHTS_RELATIONS.json) / [C｜陰性對照](CASE_C_NEGATIVE_CONTROLS.json)
- [D｜型別看不見的授權用途衝突](CASE_D_SEMANTIC_SCOPE_BLINDSPOT.json)
- [23 項 regression](test_monitor.py) / [五個故意失效的突變](mutation_probes.py) / [D 失效探針](semantic_limit_probe.py)
- [01｜DAIL 語義與 Coding 邊界](01_DAIL_RELATION_CONTRACT.md)
- [02｜執行結果與證據](02_LOCAL_EXECUTION_REPORT.md)
- [03｜完整 L8、SAC 點燈、T1/T2/T3、SGER 與 Receipt](03_L8_FULL_SGER_AND_RECEIPT.md)
- [04｜我的研究判斷與後續設計](04_RESEARCH_DIRECTION.md)
- [05｜Git 寫入回讀](05_GIT_PERSISTENCE_AUDIT.md)

## 重現
把本資料夾取出，在 Python 3.13+ 中分別執行：
- python test_monitor.py
- python mutation_probes.py
- python semantic_limit_probe.py
- python radar_relation_monitor.py CASE_A_SITE_RELATIONS.json

其中 mutation_probes.py 的故障版本應該失敗，原始版本 23 項應該通過；semantic_limit_probe.py 自己能成功觀察到系統漏報，不代表語義雷達通過測試。

## 最重要的限制
**COMPUTABLE RELATION UPDATE != DISCOVERY OF A PREVIOUSLY UNMODELLED RELATION。**
請勿因本工程成功將 SAC、Radar V6、DAIL、MAIN 或 LIHUOOS 全部降格為這段 Python。

本目錄不改上位協議、OS、Staff-HQ Runtime；004 的既有歷史同樣不改。