# 01｜關係語義應在 Coding 以前：DAIL 研究契約草圖

**Standing: DAIL-INSPIRED WORKING SEMANTIC CONTRACT，非正式 compiler output，非已被 L9 綁定的新 capability。**

現行理火 OS L9 的分工為 DAIL DEFINES / IR NORMALIZES / CODING CONNECTS / RUNTIME EXECUTES。本次**沒有實際跑正式 DAIL 編譯器或 IR**；下面只是清楚列出語義契約，避免把 Python 程式偷升格為 AI 認知。

## 關係問題
一個事件不是孤立字串；要追蹤它如何改變另一些已存在的關係。候選關係包括時間與資源衝突、權限與用途相容性、證據資格、來源版本、未知的保留。真正的 Radar 還應幫 AI 注意尚未被現有類別吸收的關係。

## 草擬的關係宣告
- Capability candidate: RELATION_EVENT_DELTA_ADVISORY
- Input: source-linked immutable event id / relation key / asserted event type / source / time-or-scope / explicit replacement link when modifying earlier event
- Output: raised / withdrawn / lineage updated / quiet; a candidate explanation, source refs, unknown and possible exploration
- Truth standing: SIGNAL_WORTH_EXAMINING_ONLY
- Authority effect: NONE
- Owners: Radar may suggest, but MAIN/Seat own substantive judgment; human retains real-world authorization
- Lifecycle: append-only evidence; old alert withdrawn does not mean old evidence retroactively never existed
- Nonclaims: NO_HIDDEN_STATE, NO_INDEPENDENT_RADAR, NO_READY_FOR_RUNTIME_PATCH

## 目前真正交給 Coding 的部分
Python RelationMonitor 只有四種硬型別：activity、disruption、permission、evidence。它不理解真正的合約語義。
- 相同 zone、相同 weekday、重疊時段且狀態符合預設時，產生「可能」的使用衝突候選；
- 權限在 UNKNOWN/PENDING/REVOKED/DENIED，產生未解權限提醒；
- 證據在 INCOMPLETE/SELF_REPORT_UNVERIFIED/DRAFT，產生未知提醒；
- 新來源替換同一 relation_key 時，比對 raised/withdrawn/source-lineage change/quiet。
- 所有 source_ref 均為測試輸入自行宣告；程式沒有加密鑑證，也不代表已實際獲得許可。

## Material gap：Case D
D01：資料使用許可 status=GRANTED，但原始用途限公開展示，明示禁止販售衍生分析報告。
D02：擬議產品正是販售衍生分析。
D03：新許可仍為 GRANTED，卻改成允許衍生分析（附歸屬條件）。

程式只看 status，三個事件都沒有提醒。這是**真正的任務語義遺失**：使用權利不應被壓縮成單一 GRANTED 布林量。不同權限、用途、主體、時間、條件彼此形成有方向的關係。

修補 D 專用 if 條件可以解決這個例子，卻不能證明抓到下一個陌生領域的關係；也會讓 Coding 的既有預設類別再次控制什麼被看見。

因此我現在傾向一個兩層假說：
(1) 可機械化的關係變更、版本與撤回，給可重跑的後端做；
(2) 未知的關係辨認、範圍對照、問題前提改變與候選方向，保留 AI/SAC 的語義探索，之後再以 DAIL 宣告可保留的關係。

這是**研究假說**，不是證明實際 SAC Hidden State 可被控制，也不是新的正式 DAIL 文法。