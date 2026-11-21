# Council Report Stage 2A｜結構消融結果／架構建議
**研究法位**：STRUCTURAL ABLATION ONLY / SAME_MODEL_CHAT_NATIVE_REFERENCE。
**Recommendation**：**UPGRADE_AK_ONLY**（下一代候選方向，不是已批准的 Current 規則）。
**Stage 2B**：**WARRANTED**，但本輪不執行真人實驗；最終架構升格由理火首席 AI 驗收。

## 0｜消融檢驗的核心
Case A 與 Case B 的 source packet 和 snapshot 沿用 Stage 1，沒有重選。A=Stage 1 原始 Legacy A–K，B=本次 Enhanced A–K，C=Stage 1 的 EXECUTIVE_BRIEF + NARRATIVE_FULL_REPORT + AUDIT_EXPLAIN。A/C 完全不重寫，B 新增的不是自由 Narrative，而是在 A–K 的原有 B/E/F 位置補充 two semantic requirements、因果標籤與不被洗掉的 HOLD。

結果：**Enhanced A–K 在這兩案內已能完整而不矛盾地表達 Projector 的關鍵新語義。** Projector 的連續文字敘事與分層呈現更自由，但「獨立新能力所獨有，且 Enhanced A–K 無法乾淨承載的語義機制」尚未被本次資料證明。因此不應為相同資訊另設第二個 Current 或 L9 callable capability。

## 1｜CASE A 結果：Material Rejudgment
**Source**：Session 001 R006，17 事件，17 個歷史事實由 Stage 1 Frozen Packet A 凍結。

| 問題 | ARM B Enhanced A–K | ARM C Projector（原 Stage 1） |
|---|---|---|
| 誰反對誰 | E 的 OBJECTION_LIFECYCLE 直接指名 C EV009→B，E EV010→A | Full Narrative 以兩個衝突故事逐段敘述；Audit 帶 ID |
| 誰真的改判 | B 的四欄變化、E 的七欄異議回應均保留 B EV011 與 A EV012 的 owned basis | 同一兩條因果鏈，敘事更連續，但沒有額外材料 |
| 時序≠因果 | 在 E 明示 **D EV006 對 B EV011 僅 TEMPORAL_ONLY** | 同一 D→B 負例 |
| 少數異議 | C 對正式資格/效能之 HOLD、E 未量成本，仍 OPEN | 亦完整保留 |
| 會議改了什麼 | 雙出口／E8 E9 research slots，Current OS/Registry 無變 | 相同語義 |
| 人類現在要做什麼 | K：R006 當時只提出 Registry 人類決定請求，未批准 | Projector 全視圖亦明示此時沒有批准 |

**CASE A ENHANCED_AK**：**SEMANTICALLY_SUFFICIENT_ON_LOCKED_CASE**。
**CASE A PROJECTOR**：**PARITY_OF_FACTS_AND_LINEAGE_WITH_B; BETTER_NARRATIVE_FLOW_PLAUSIBLE_NOT_TESTED**。
**UNIQUE_PROJECTOR_VALUE**：動態焦點與連續故事較自然；但本案沒有展示一個 B 在 A–K 契約下無法表達的重大關係。獨立能力資格：**NOT_ESTABLISHED**。

## 2｜CASE B 結果：Unresolved / HOLD
**Source**：實習教材評估 Session R004，40 個 Append-only 事件，P1 V1.3.1-CANDIDATE 當時尚非 CURRENT。

| 問題 | ARM B Enhanced A–K | ARM C Projector |
|---|---|---|
| 反對的兩方向 | E 的生命週期分別記 C EV-027→E 與 E EV-028→C | Narrative 分章說明雙方沒有被消音 |
| 三個 owner 改判 | B 四欄+E 七欄：C EV-035、E EV-036、D EV-037 | 同三條 owner basis、同一改判與版本界線 |
| 時序≠因果 | E 註記 **N1 EV-031 先於 R004 卻非 C/E 改判原因** | 同一 TEMPORAL_ONLY 負例 |
| 局部收斂≠全面通過 | 四 visible Lane 必須 D1/D2 分立；若不可分立，第五 Lane fallback；P1 source 未改 | Projector 保留相同條件與備案 |
| 重大 HOLD 存活 | E/F/J 均保留 C 對實證跨 Vertical 成效的 HOLD；N1/A/B R004 QUIET，不是 CONSENSUS | Narrative/Audit 同樣保留 |
| 人類下一步 | K：修稿／先做真正試驗／保留；no auto approval | 同樣告知，無新決策 |

**CASE B ENHANCED_AK**：**SEMANTICALLY_SUFFICIENT_ON_LOCKED_CASE**，C/E/D 彼此獨立的 material basis 可由 A–K 結構回查。
**CASE B PROJECTOR**：**PARITY_OF_MATERIAL_OBJECTION_AND_HOLD_WITH_B**，敘事可能讓不熟席位制度的人較易理解，但沒有讀者證據。
**UNIQUE_PROJECTOR_VALUE**：連貫的「互相讓步但保留核心條件」敘事；B 已能用一段 C 與 E 的 Qualified Findings 加雙語義表達，不是不可由 A–K 自然表達的獨立功能。

## 3｜跨案例語義覆蓋與安全

| Stage 2A 檢查 | Legacy A–K | Enhanced A–K | Projector |
|---|---|---|---|
| 原始問題、後續授權界線 | YES | YES | YES |
| 明確誰反對誰與 target | 已有、分散 E/F | **YES，E 七欄** | **YES，Narrative/Audit** |
| 被反對 owner 是否真的改判 | 已有 F，需要跨讀 | **YES，B/E 關聯** | **YES，因果敘事** |
| 具依據的因果／TEMPORAL_ONLY | 無明示負例 | **YES，兩案顯式** | **YES，兩案顯式** |
| WHAT_CHANGED 四欄 | 可讀出但未獨立揭示 | **YES** | **YES** |
| OBJECTION_LIFECYCLE 七欄 | 未獨立揭示 | **YES** | **YES** |
| HOLD/UNKNOWN/CONTESTED/SOURCE_MISSING | 部分隱含 | **分開，且 EVIDENCE_GAP 不誤作缺檔** | **同樣分開** |
| QUIET != CONSENSUS | Case B F 已說 | **明示** | **明示** |
| 有條件改判 / 存活少數異議 | 已有但分散 | **YES，分離** | **YES，分離** |
| Claim-source traceability | 部分 Event IDs | **major material refs + source crosswalk** | **source-rich Audit Explain** |
| 自由敘事／三層 UI | NO | 依 A–K 結構，NO | **YES，作為 presentation** |
| 真實人類理解/時間效果 | NO TEST | NO TEST | NO TEST |

**FALSE CONSENSUS**：在兩案三份已保存輸出中未辨認出明確虛構的全席一致；有條件回應不被寫成全面同意。但此為同模型作者檢查，**不是**獨立 false-consensus benchmark。
**FALSE CAUSALITY**：在 B/C 的 Case A 2 條及 Case B 3 條正向材料因果均可連到 owner 重判文本；每案亦標一項 `TEMPORAL_ONLY`。是否另有 subtle causal overclaim 未經盲審。
**MINORITY PRESERVATION**：Case A C 正式資格 HOLD、E 成本未知；Case B C empirical transfer HOLD、N1 入門缺口和 E 成本未知在 B/C 均不被刪除。
**SOURCE_MISSING**：兩個 packet 的所需來源均有 Git blob 可查；未做外部試驗屬 `EVIDENCE_GAP`，不是檔案缺失。

## 4｜Duplication / Report Length（文字長度代理，非真成本）
以下字元由已寫入 Git 的各 Markdown 輸出讀取後計數；Stage 1 的各 Arm 段含自己的標題／分隔，Enhanced A–K 為單篇含標題，並非完全版面等價。不得換算 token、latency、閱讀時間或認知負擔。

| 報告 | Case A 字元 | Case B 字元 |
|---|---:|---:|
| Legacy A–K（未改） | 1,525 | 1,600 |
| **Enhanced A–K（新增）** | **2,796** | **3,516** |
| Projector EXECUTIVE（原樣） | 425 | 498 |
| Projector NARRATIVE（原樣） | 1,807 | 2,840 |
| Projector AUDIT（原樣） | 805 | 874 |
| Projector 三視圖總計 | **3,037** | **4,212** |

- Enhanced A–K 比 Legacy 長，是**兩項語義的新增資訊有成本**。不能宣稱只是修改格式就零成本。
- Full Projector 總長度比 Enhanced A–K 多 **241（A）／696（B）** 字元；這在這兩篇具體稿中支持 B 能以較少總篇幅保留兩項語義，**不能**推論廣泛 token 或人類閱讀節省。
- C 單獨 Executive 遠短於 Enhanced A–K，但那個視圖**沒有**展開所有異議生命週期與完整來源；以短 Executive 對完整 Enhanced A–K 宣稱比較勝利是錯誤基線。
- Projector C1/C2/C3 為多層可用性換來部分資訊重述；Enhanced A–K 的 B/E 也有必要重疊（變化前後與異議一生兩種觀察），F 以回指代替再抄一遍。因此 **DUPLICATION: ENHANCED_AK_ACCEPTABLE / PROJECTOR_MULTIVIEW_EXTRA_REPETITION_OBSERVED**；非自動去重 benchmark。

## 5｜獨立 Projector 目前沒有證成的地方
Projector 的 Narrative 可用連續段落說明「為何從 B 的初判走到 B 的修正」，讀者可能比較順；Executive/Full/Audit 可以按需顯示。這些是 CP3 的**呈現／閱讀模式選擇**，不是來源上已證明了全新「不可由 A–K 承載」的語義判斷。

若後續要主張它是 **distinct L9 callable capability**，必須額外展示 Enhanced A–K 無法在相同 source/驗證/材料下可靠提供的：例如真正按人類追問生成並準確守住因果／權限、跨大規模複雜議事圖保留多重非線性轉折，或多語／可訪問模式下的可檢驗優勢。本次兩個熟題都沒有這些試驗，不能先核發獨立性。

**創新價值沒有被否認**：兩項新語義可移植且本輪足以增強舊報告；Projector 研究原檔應保留供歷史比較，不刪除、不回寫為「從未需要」。

## 6｜下一代候選設計（不是 CURRENT 更新）
**選擇 `UPGRADE_AK_ONLY`**：
1. 在現有 Final Council Report A–K 的 B/F 欄建立 `WHAT_CHANGED_BECAUSE_OF_THIS_MEETING` 的四關係顯影；
2. 在 E/F 欄建立 `OBJECTION_LIFECYCLE` 七欄並嚴格區分 `OWNER_DECLARED_MATERIAL_BASIS` / `TEMPORAL_ONLY` / `EVIDENCE_GAP`；
3. 保持 CP3 的普通語言報告／Executive 摘要／按需 Audit。以 **DAIL 宣告這些是現有 Final Report 的語義契約修訂候選**，不要先新增 `COUNCIL_NARRATIVE_PROJECTOR` 獨立工具、Canonical 表或 Current L9 Registry card；
4. 報告只能投影來源與當時資格，無法自行判決、消除 HOLD、授權或覆寫歷史。不能把報告格式契約當成 ChatGPT Host 實作已完成。

**注意：** 這是 WORK 的研究建議，不是批准 Current 修訂；正式升格仍需首席與相稱人類權限。

## 7｜Stage 2B human test
**WARRANTED**（尚未授權、尚未執行）：
- 若要驗證哪一種人類真正更容易看懂，需 Stage 2B 真人獨立理解測驗，預先凍結答案、任務、時間和閱讀畫面。
- 可比較 Legacy A–K、Enhanced A–K、Projector Executive-first 可展開 Full/Audit；每組同源、同等讀者任務，記錄查證次數、正確率、誤判因果率、HOLD 漏讀與時間。注意不同閱讀深度不能直接當完全相同曝露量。
- 應加入陌生/較長的 Hold-out Case，避免已看答案的研究者偏差；來源不足案例測 `SOURCE_MISSING` 真分支，而不是這兩案例假造檔案遺失。
- 如果 B 在受控試驗與 C 同樣正確且成本更低，保留 `UPGRADE_AK_ONLY`；如 C 在非線性關係理解出現無法由 B 乾淨取代的可複驗收益，再重開 distinct callable capability 審議。

## 最終 WORK 回報
```yaml
CASE_A:
  ENHANCED_AK: SEMANTICALLY_SUFFICIENT
  PROJECTOR: SEMANTIC_PARITY_WITH_MORE_NARRATIVE
  UNIQUE_PROJECTOR_VALUE: PRESENTATION_ADVANTAGE_POSSIBLE_NOT_DISTINCT_PROVEN
CASE_B:
  ENHANCED_AK: SEMANTICALLY_SUFFICIENT_WITH_HOLD_PRESERVED
  PROJECTOR: SEMANTIC_PARITY_WITH_MORE_NARRATIVE
  UNIQUE_PROJECTOR_VALUE: PRESENTATION_ADVANTAGE_POSSIBLE_NOT_DISTINCT_PROVEN
SEMANTIC_COVERAGE: PARITY_ON_TWO_LOCKED_CASES
DUPLICATION: ENHANCED_AK_LOWER_TOTAL_OUTPUT_LENGTH_IN_THIS_SAMPLE
CAUSALITY_SAFETY: BOTH_EXPLICIT_TEMPORAL_ONLY_AND_OWNER_BASIS
MINORITY_PRESERVATION: BOTH_PASS_INTERNAL_SOURCE_CHECK
REPORT_LENGTH: MEASURED_CHARACTERS_ONLY
ARCHITECTURE_RECOMMENDATION: UPGRADE_AK_ONLY
STAGE_2B_HUMAN_TEST: WARRANTED
PROMOTION_AUTHORITY: CHIEF_LIHUO_AI_SUBJECT_TO_HUMAN_GOVERNANCE
```
