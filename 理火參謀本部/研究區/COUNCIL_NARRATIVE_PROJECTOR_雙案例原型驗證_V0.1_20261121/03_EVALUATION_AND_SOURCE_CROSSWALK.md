# Council Narrative Projector｜雙案例原型驗證結果與索引
**日期**：2026-11-21。**結果法位**：QUALITATIVE_DESK_PROTOTYPE / NOT_INDEPENDENT_HUMAN_EVALUATION / NOT_ENGINEERING_VALIDATED。
**三路都是同一模型在同一可見資料上下文中撰寫的報告；沒有實際 L9 binding 或獨立模型盲測。**

## 一、CASE A RESULT
**案例**：下一代 L8 Engine 概念會議 Session 001，R006 時點；17 筆事件，有 B 與 A 的 owner rejudgment。
**LEGACY A–K**：成功交代初始提案、C→B 和 E→A 改判，以及資格與成本問題。資訊跨 B、E、F、J、K 節分散。
**ORDINARY SUMMARY**：能準確說出兩項改判和未驗證／需人類決定，未被故意寫壞；但沒有否定因果範例和來源解析。
**DAIL PROJECTOR**：把 C EV009→B EV011、E EV010→A EV012 的反對／消費／修正／剩餘問題連成可讀過程；明示 D EV006 與 B 修正僅先後存在（TEMPORAL_ONLY）。四欄 BEFORE/MATERIAL CHANGE/AFTER/UNCHANGED 和七欄 OBJECTION_LIFECYCLE 都形成可核對結果。
**沒有宣稱**：在 R006 已有 Registry 人類批准；後來 Session 002/人類 KEEP 不回填此案。

## 二、CASE B RESULT
**案例**：V1.3 通用實習手冊評估 R001–R004，至 V1.3.1 P1 候選審議 Checkpoint；40 筆事件，有三個材料性 owner rejudgments，C universal empirical HOLD 存活。
**LEGACY A–K**：能正確列出 C/E 雙向異議、B→D、新候選非 Current 及 C HOLD。
**ORDINARY SUMMARY**：重要事實基本正確，能辨識能力／授權分離與仍未驗證的跨 Vertical 成效，缺少細緻異議生命週期。
**DAIL PROJECTOR**：明示 C EV-027→E EV-036、E EV-028→C EV-035、B EV-029→D EV-037 的各自 material basis。局部四條 Lane 條件性修訂與「C 對新生實際有效性 HOLD 未消失」被分開；N1 EV-031 先於 C/E 改判，但未證為改判原因（TEMPORAL_ONLY）。B 事後 V1.3.3 Current Adoption 不回鑄 R004。

## 三、驗收與未解項目

| 項目 | A–K | Ordinary LLM Summary | DAIL Projector | 本輪證據位階 |
|---|---|---|---|---|
| 原始問題與會議範圍 | 有 | 有 | 有 | 可核對 |
| 誰反對誰、改判材料 | 有，但多處分散 | 有簡述 | 有 owner event 鏈和關係欄 | 同模型人工內容檢查 |
| WHAT_CHANGED 四欄 | 可由文推回 | 概述 | 明示 BEFORE/MATERIAL/AFTER/UNCHANGED | 版面契約完成 |
| OBJECTION_LIFECYCLE 七欄 | 可由 E/F 補讀 | 通常不足 | 明示七欄且保留 remainder | 版面契約完成 |
| 假共識 | 無明顯假共識 | 無明顯假共識 | 無明顯假共識，QUIET 不當同意 | 非獨立負面檢查 |
| 錯寫因果 | 未標 TEMPORAL_ONLY | 未標 TEMPORAL_ONLY | 主張有 owner 來源，另列負例 TEMPORAL_ONLY | 非獨立負面檢查 |
| 少數異議 | 兩案皆留 | 兩案皆留 | 兩案皆留並標存活階段 | 可檢查 |
| HOLD/UNKNOWN/CONTESTED/SOURCE_MISSING | 大部分可讀出，非全部顯性 | 不充分區分 | Audit 明確區分；真正缺實驗記 EVIDENCE_GAP | 概念層 |
| 重要結論來源回查 | 有局部 ID | 概括/無細 ID | 論點級 ID＋來源 Crosswalk | 可檢查 |
| 真實人類閱讀理解/時間 | NOT_TESTED | NOT_TESTED | NOT_TESTED | **無資料** |
| 模型 token/latency/成本效益 | NOT_CAPTURED | NOT_CAPTURED | NOT_CAPTURED | **無資料** |

**FALSE CONSENSUS：** 原型稿中未見明顯「全席一致同意」「HOLD 已消失」等造假，並不代表對所有未見案例安全。
**FALSE CAUSALITY：** C 臂共呈現 2+3 條 owner 明示材料鏈，且每案至少一條 TEMPORAL_ONLY 負例；仍需要獨立人員核對語言有沒有比資料更強。
**MINORITY PRESERVATION：** Case A C 的資格異議、E 成本保留；Case B C empirical universality HOLD 保留。未把有條件收斂寫成全面勝利。
**SOURCE TRACEABILITY：** 各報告引用源代號及 EV ID；B 的 EV### 簡寫曾使精確回查不夠嚴謹，已另以 derived view 版本更新為原始 `EV-###` 格式，不更改 Canonical。
**HUMAN COMPREHENSION：** **NOT MEASURED**。可以說 C 的文本提供更多可答材料，不能說一般人已證明讀得更懂。
**COST OBSERVATION：** 只核對檔案字符量，沒有逐 arm 的計算 token、latency、真實閱讀秒數；C 三層加總較長，預設只應顯示 Executive，按需展開全文和 Audit。

## 四、Report Source ID Crosswalk
每個 `EV...` 只在該案例自己的固定截點解釋，不跨案合併。

**Case A**：`A00`=001/00_SESSION_INDEX；`A-HUMAN`=MEMO 原始 WORK；`A02`=001/02_SHELL_INVARIANTS；`A03`=001/03_ENGINE_DISTINCTNESS_REVIEW；`A04`=001/04_ROUTER_SWITCH_ARCHITECTURE；`A05`=001/05_ENGINE_INTERFACE_SCHEMA；`A06`=001/06_CASE_PRESSURE_TESTS；`A07`=001/07_CANONICAL_EVENT_LOG.jsonl；`A10`=001/10_SEAT_L8_OBSERVABLE_REFERENCE.md。001 來源資料夾精確路徑及 SHA 見 00_SOURCE_LOCK。`EV009` 等出自 A07；`A10#B_REWAKE` 等為當席原始可見再判檔章節。

**Case B**：`B00`=00_CASE_ENTRY；`B09`=09_HUMAN_REVISION_AUTHORIZATION；`B10`=10_P1_CANDIDATE_ADMISSION；`B-P1`=原始 V1.3.1-CANDIDATE 教材；`B03`=03_CANONICAL_TYPED_EVENTS；`B-R3-LEDGER`=12_CANONICAL_TYPED_EVENTS_R003；`B-R4-LEDGER`=12_CANONICAL_TYPED_EVENTS_R004；`B-R1`=03_COUNCIL_EVENTS_R001；`B-R2`=05_COUNCIL_EVENTS_R002；`B-R3`=12_COUNCIL_EVENTS_R003；`B-R4`=12_COUNCIL_EVENTS_R004；`B-C`=13_REWAKE_L8/R004_C；`B-E`=13_REWAKE_L8/R004_E；`B-D`=13_REWAKE_L8/R004_D；`B-LANES`=15_QUALIFICATION_LANES_REVIEW。精確 SHA 見 00_SOURCE_LOCK。B 事件號為 `EV-027` 而不是 Case A 的 `EV027`。

**此 Crosswalk 只是讀者索引，不可當成一份新的 Canonical Record。**

## 五、成本／篇幅（僅長度代理）
依 Git 回讀檔內容分段（含 Markdown 標題）：
- Case A：A–K 約 1,525 字元；Ordinary 約 357；C Executive 約 425，Narrative 約 1,807，Audit 約 805，合計約 3,037。
- Case B：A–K 約 1,584；Ordinary 約 461；C Executive 約 494，Narrative 約 2,813，Audit 約 861，合計約 4,168。
這是**輸出長度，不是 token、latency、費用或人類理解時間**；真正的 C 全包遠比 A–K 長。若預設只交 Executive，仍須實測它能不能讓人理解轉折；全文／Audit 按需取用是研究建議。

## 六、推薦與首席驗收界線
**WORK RECOMMENDATION: REVISE**。兩項 DAIL 語義能在真實 Session 的文本中生成可回查的報告，而且具體補上 A–K 對材料因果不夠直觀的部分。但這次只是同模型手工受來源約束的原型；**不能 PROMOTE** 到下一代主程序或 Current L9。

**下一個有辨識力的試驗**：請首席／獨立人類審核 Case A/B 的 6 份核心報告，隱去報告來源名稱，讓不熟 DAIL 的讀者回答「誰反對誰、改判因果、仍存 HOLD、下一步」，同時量測閱讀時間和回查成功率。增加一組「增強版 A–K（把兩個新語義直接加在 A–K）」對照，確認是否真的需要獨立模組，而非既有 Final Report 小修即可。

**禁止的升格**：NOT_ENGINEERING_VALIDATED／NOT_COST_VALIDATED／NOT_BENCHMARK_PROVEN／NOT_PRODUCTION_DEPLOYED／NOT_HOST_DEPLOYED。最終 PROMOTE 只由理火首席 AI 另行驗收及取得適當人類授權。

**無 CURRENT 檔案修改；沒有替原始 Session 發出新的 Council Event 或人體研究通過宣告。**
