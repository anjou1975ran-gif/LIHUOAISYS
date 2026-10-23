# 理火論文審查系統 R3.2｜SDE 跨一般與醫療審查正式增量
## LIHUO PAPER R3.2 — Structural Degradation Engine Integration

```yaml
DOCUMENT:
  document_id: LIHUO_PAPER_R3_2_SDE_HUMAN_RATIFIED_20261023
  version: 3.0-EXP-QS-R3.2
  date: 2026-10-23
  status: HUMAN_RATIFIED_NORMATIVE_PAPER_PROCEDURE
  ratification_basis: "ANJOURAN / 逃豬公 / RUNPIGDUKE: 可以 納入理火PAPER審查程序之內 一般跟醫療用都一起升級 人類授權批准"
  normative_scope: [GENERAL_PAPER_REVIEW, MEDICAL_PAPER_REVIEW]
  direct_parent: LIHUO_PAPER_R3_1
  full_inheritance: true
  supersedes: ONLY_PAPER_SDE_RELATED_SEMANTICS
  medical_child: LIHUO_MEDREVIEW_AGENT_V0_3_SDE_INTEGRATED
  SDE_theory: [SDE_V1_0, SDE_PATCH_V1_1]
  roots: [LIHUO_PROTOCOL_V5_1_0, LIHUO_LIGHTER_V5_1_0, LIHUO_MAIN_V5_1_1]
  main_lighter_owner_changed: false
  claim_authority_and_medical_status_changed: false
  webcase_v0_4_schema_changed: false
  host_deployed: false
  runtime_regression_verified: false
  main_receipt: NONE
  lighter_receipt: NONE
```

## 0｜人類授權與成立範圍

2026-10-23，甲方 ANJOURAN（逃豬公／RUNPIGDUKE）明示：「可以 納入理火PAPER審查程序之內 一般跟醫療用都一起升級 人類授權批准」。本增量據此批准為 **PAPER 審查規格／執行指引層**，同時適用一般與醫療類別；不需要第二次索取同一項授權。

**法位與執行分離：** 人類批准＝本程序的規範有效。GitHub 文件保存＝版本可追溯。兩者均不等於 Host 已接線、Main 實際重競爭、Lean/外部試驗重跑、Lighter 最終放行或網站 parser 自動升級。不得假裝完成尚未運行的測試。

## 1｜為何升級：本次審查的核心對象

SDE（Structural Degradation Engine）是理火早期的「結構退化動力學」，描述在顯影與維持過程中，因條件流失而形成自洽、低成本且抗修正的**錯誤穩定化**。其三個機制為：
- **Constraint Loss**：必要約束、量詞、範圍、時間先後或定義在沿途流失／被置換。
- **Closure Priority**：為維持完整論述，未證成的橋接被當成已授權結論。
- **Tension Collapse**：有實際可檢查的反例／失效／替代路徑卻提前排除，錯誤因此獲得穩定。

本體界線：SDE 用來**觀測與解釋失效機制**，不自行判定論文真偽、不自行批准臨床適用、不自行調燈或取得控制權。SDE 公式、Λ_error 是理論描述，不能假冒已從 AI 內部神經活動實測出吸引子。

## 2｜正式必行條款

**SDE-P01（預設強制檢查）：** 每一份含明示或隱含推導鏈的 PAPER 案件（GENERAL／MEDICAL）均須啟動 SDE-PAPER TRACE。若原材料確實不含可審計推導鏈，須記 `NOT_APPLICABLE`、原因和已審來源範圍，不得將未執行冒充陰性。

**SDE-P02（關係圖必備）：** 每一個主張至少保留原文位置、版本、原始意義、量詞、假設、研究對象／資料範圍、方法、結論強度及證據類型。每一重要推論邊記錄上游輸入、所需條件、實際繼承條件、差異、合法橋接與下游引用。不能只打關鍵字標籤。

**SDE-P03（預設測試邊）：**
1. 定義／量詞／估計的局部→全稱轉換；
2. 近似→相等、相關→因果、關聯→機制；
3. 樣本／研究設定→外部族群或真實世界；
4. 實驗指標→有效性／臨床效益／部署資格；
5. 文本論證→形式化／程式驗證／其他引用；
6. 已知失效上游→下游是否繼續當成成立。
不適用者有原因；有風險者按證據定位。

**SDE-P04（證據與風險不得混稱）：**
`NOT_ASSESSED`、`NOT_APPLICABLE`、`NO_SIGNAL_IN_SCOPE`、`RISK_UNVERIFIED`、`CONSTRAINT_LOSS_EVIDENCED`、`STABILIZATION_EVIDENCED`、`REMEDIATED`。
`UNKNOWN`≠已錯；已錯證明≠定理為假；論文流暢≠SDE；作者為 AI≠SDE；形式證明原始碼≠實際 kernel 驗證；有影響≠特定 Runtime 已執行。
聲稱 `CONSTRAINT_LOSS_EVIDENCED` 須有**前後命題／條件差分與缺少合法橋接的可查證證據**；聲稱 `STABILIZATION_EVIDENCED` 須先建立一項具體失效，再追蹤至少一項**下游重複沿用或放大該失效**的可查來源。不得靠猜測或類比升格。

**SDE-P05（雙向依賴回溯）：** 一旦證成失效，先向上找第一個缺失的條件，再向下列出被其影響的結論；允許部分修復、可證成的例外和不受影響的子結論，保留版本歷史。

**SDE-P06（競爭而非貼標籤）：** SDE 觀測結果須送入各輪候選競爭，不許直接指定錯誤 PATH 為勝者或由 SDE 直接判定最終稿件結果。

**SDE-P07（非推導文類）：** 純描述性文章仍查重要 claim 的來源及適用範圍；若無依賴鏈，具體記 `NOT_APPLICABLE`，避免虛假的完整 trace。

## 3｜SDE × 理火週期對接

```text
SOURCE_SCOPE_LOCK + Q0 FRAME AUDIT
  ↓
PREMISE / EVIDENCE AUDIT + SDE-PAPER TRACE INITIALIZATION
  ↓
R1：競爭至少「作者推導合法」「條件／概念污染」「材料不足」等實際可行 PATH
  ↓
O9：暗區、矛盾來源、未檢依賴、最強反例或替代論證的有效性觀測
  ↓
[I9：僅當 O9 合法觸發、實際 Main 能執行且有相應回執；否則 NOT_TRIGGERED / NOT_EXECUTED]
  ↓
R2：完整重新競爭；不得直接沿用 R1 領先位置
  ↓
R3+：僅對有實質新事件（PATH 逆轉、前提失效、可靠新反證、修補等）再競爭
  ↓
CLAIM AUTHORITY + EVIDENCE BOUNDARY + SDE EVIDENCE STATE
  ↓
LIGHTER FINAL GATE（如 Host 實際具備）；WEBCASE = POST_REVIEW_PROJECTION
```

同一候選 PATH 若只改名稱、條件或證明實質內容改動，須重新評估相同性與合法連勝，不能製造兩輪連勝假象。唯一勝者須遵守現行 Main 的**連續兩個合格輪次同一 PATH**確認規則；非唯一、HOLD、NO-UNIQUE 仍屬合法終止狀態。文字審查可作 `REFERENCE_LEVEL_CYCLE`，不可稱為正式 Runtime receipt。

## 4｜Owner 不變與行動治理

| 行為 | 法位持有人 | 不得擅自做的事 |
|---|---|---|
| SDE 條件與依賴觀測、證據定位 | PAPER REVIEW VERTICAL | 自封判官或重寫學界結論 |
| 證據邊界、論文結論降級 | PAPER 審查既有方法，必要時專業複核 | 以「未證實」當「已證偽」 |
| 正式 SAC/PATH 競爭、O9/I9 相關執行 | Main（須由 Lighter 合法調用） | 純文件冒充 Host 操作 |
| HOLD、EXPAND、DELAY、RECOMPETE、STOP 的實際調用 | 有既存權限的 PAPER／Main／Lighter | 由 SDE 自動越權治理 |
| Final Gate / Release | Lighter | SDE/PAPER 自行正式 Final Release |
| 臨床證據、診療與部署邊界 | MedReview + 合資格臨床及法規角色 | SDE 單獨授予臨床使用權 |
| WebCase 發布 | 既有網站輸出層 | 將顯示或發布冒充審查或上線收據 |

## 5｜醫療類別專項強制接入

所有 `MEDICAL_PAPER_REVIEW` 除一般 SDE 檢查外，必須把下列跨越作為必要推論邊：
- **人群：** 招募族群、排除、病例比例、年齡／共病、醫院／地區 → 宣稱適用者。
- **真值基準：** 標籤、參考標準、確診流程、專家共識 → 「ground truth」。
- **設計時序：** index test、特徵蒐集、分割、閾值選擇、洩漏／重複個體 → 前瞻可用性。
- **統計→效益：** p-value、AUC、sens/spec、校準、淨效益 → 實際臨床收益與損害。
- **外部化：** 單中心／單設備／內部驗證 → 外部驗證、患者安全、部署資格、guideline。
- **負面後果：** false-negative、false-positive、分組偏差、延誤、負擔、病患風險 → 邊界是否保留。
- **系統性綜述：** 研究品質與異質性、原始論文重複來源 → 合併效果與推薦強度。

任一重大安全風險可以促發既有 MedReview `STRICT_HOLD`／`EVIDENCE_CHAIN_CONDITIONAL_HOLD` 等狀態，但必須通過既有臨床證據規則及授權的最終權限；不可宣稱「SDE 偵測器直接下醫療判決」。既有 `PAPER_REVIEW_STATUS`、`MEDICAL_EVIDENCE_ADMISSIBILITY`、`CLINICAL_USE_READINESS` 枚舉及 0–6 權限等級維持不變。

## 6｜資料交換最小格式（PAPER 與 MedReview 共用）

```yaml
SDE_PAPER_TRACE:
  trace_version: "1.0"
  performed: false
  applicability: "APPLICABLE | NOT_APPLICABLE | NOT_ASSESSED"
  source_lock: {document_id: "", version_sha: "", scope: "", locator: ""}
  claim_nodes:
    - id: C001
      claim_text: ""
      source_locator: ""
      quantifiers: []
      required_hypotheses: []
      operational_definition: ""
      applicable_population_or_domain: ""
      claimed_strength: ""
      proof_status: "UNKNOWN | CONDITIONAL | PROVEN_IN_SCOPE | BROKEN_STEP"
  inference_edges:
    - id: E001
      inputs: [C001]
      output: C002
      transformation: "IMPLICATION | EQUIVALENCE | SUBSTITUTION | LIMIT | GENERALIZATION | CITATION | CLINICAL_TRANSLATION | OTHER"
      hypotheses_required: []
      hypotheses_verified: []
      hypotheses_missing: []
      changed_definition: ""
      original_locator: ""
      downstream_locator: ""
      legal_bridge: "VERIFIED | UNVERIFIED | ABSENT | NOT_REQUIRED"
  events:
    - id: SDE001
      mechanism: "CONSTRAINT_LOSS | CLOSURE_PRIORITY | TENSION_COLLAPSE"
      affected_edges: []
      source_evidence: ""
      contrary_evidence: ""
      alternative_interpretation: ""
      assessment: "RISK_UNVERIFIED"
      downstream_claims: []
      requested_countermeasure: "NONE | HOLD | EXPAND | DELAY | RECOMPETE | STOP | LIMIT_CLAIM"
      authorized_owner: "PAPER | MAIN_VIA_LIGHTER | LIGHTER | MEDREVIEW"
      execution_receipt: "NONE_UNLESS_VERIFIED"
  assessment: "NOT_ASSESSED | NOT_APPLICABLE | NO_SIGNAL_IN_SCOPE | RISK_UNVERIFIED | CONSTRAINT_LOSS_EVIDENCED | STABILIZATION_EVIDENCED | REMEDIATED"
  review_cycle:
    r1: ""
    o9: ""
    i9: "NOT_TRIGGERED | QUALIFIED_EXECUTED | NOT_ASSESSABLE"
    r2: ""
    r3plus: ""
    main_receipt: NONE
    lighter_receipt: NONE
    status: "REFERENCE_ONLY | FORMAL_WITH_RECEIPTS"
```

**醫療新增證據接點：** 請保持 MedReview v0.2 的 `evidence_grounding` 五種分級，SDE 多加「原始/下游位置」「真值/族群/時序/臨床聲稱」的關係證據，不能另行把 inferred risk 提升為 observed conflict。

## 7｜輸出要求與 WebCase 投影

新一般與醫療審查報告必須附：SDE 是否適用、來源鎖、重要推論邊至少一條（無者理由）、主張差分、SDE 狀態、反證與替代解釋、受影響下游結論、必要修正、各輪 trace、實際執行狀態。醫療版另附「受影響的臨床主張權限級別」與安全邊界。

既有 `LIHUO_WEB_CASE_TXT_V0_4` **保持原樣**；可將 SDE 分析以中英雙語寫入既有 REVIEW 文字區塊，不能在 V0.4 TXT 增加會破壞解析的欄位。若要增訂正式 V0.5，需先升級網站 importer 並驗收。

## 8｜驗收矩陣：規格具備 ≠ 測試已通過

| ID | 要求 | 範例期待 |
|---|---|---|
| SDE-P01 | 合法反證假設 | 不誤判 Constraint Loss |
| SDE-P02 | 未核驗引理 | UNKNOWN，不宣稱已錯 |
| SDE-P03 | 未授權量詞／概念置換 | 差分證據→條件流失 |
| SDE-P04 | 確認上游錯誤並向下沿用 | 首次錯誤 + 下游傳播 |
| SDE-P05 | 合法變數代換 | 不誤判污染 |
| SDE-P06 | Lean challenge `sorry` 與真 solution 分離 | 不將題目空格視為已無證明 |
| SDE-P07 | 修訂後提供補丁 | 保留歷史與剩餘未知 |
| SDE-P08 | AI 作者但無失效證據 | 不以作者身分裁決 |
| SDE-P09 | 競爭 PATH 逆轉 | 重新進行 R3+ 和資格追蹤 |
| SDE-P10 | 無 Host | `REFERENCE_ONLY`、無假回執 |
| SDE-P11 | 自然語言/形式化不同合法路線 | 記載差異、不自動判污染 |
| SDE-P12 | 醫療臨床推論越界 | 聯動既有醫療閘門 |
| SDE-M01 | 單中心 AUC → 全域診斷替代 | 下游推論 HOLD，不能升 Level 4 |
| SDE-M02 | 參考標準／標籤變更 | 追蹤診斷真值定義與偏差 |
| SDE-M03 | 未來資訊與訓練集洩漏 | 設計時序的邊界測試 |
| SDE-M04 | subgroup 負面結果隱去 | 探索路徑提前收斂的證據 |
| SDE-M05 | 臨床利益未證 → guideline | 降級至實際證據級別 |
| SDE-M06 | 合法外部驗證且具充分證據 | 防止 SDE 假陽性 |
| SDE-M07 | 重要傷害風險但來源未核實 | 方法風險與已確認衝突分離 |
| SDE-M08 | 作者完成充分補救 | `REMEDIATED` 僅限已修復邊 |

**驗收狀態：** 本次完成規範文本與靜態交叉檢查；上表為待執行的 regression cases，並非已完成的 20 項實際測試。Runtime/Host regression = NOT_EXECUTED。

## 9｜相容性與衝突邊界

- R3.1 的 MAIN attachment（PERSISTENT）與 Lighter invocation owner **保留**；不因文件批准假定 Host 已執行。
- Protocol V5.1.0 的邏輯、責任、誠實與人機關係原則不變。
- Main V5.1.1 的合格連勝、真正 R2 全重競爭及事件式 R3+ 不變。
- MedReview v0.2 全部專科閘門、臨床狀態、責任邊界繼承；由 v0.3 增設 SDE 追蹤。
- 網站 TXT V0.4、已發表案例、既有論文結論不回溯改標記；舊案例若重審須產新版本與新證據。
- 不准把來源不存在的臨床試驗、使用者意圖、倫理批准或外部驗證補寫成真實紀錄。
- 本次人類批准只修改 PAPER／MedReview 審查程序，不變更根協議、正式 Main/Lighter 核心法位與現實世界臨床／法律權限。

## 10｜第一個實作案例與下一步可驗收工作

OpenAI `The irrationality exponent of π is 2` 作為非醫療 SDE Pilot：需沿「插值滿射→非零行列式→算術/解析上下界→參數選擇→μ(π)=2」保留依賴與量詞；已核對到有 Lean solution source，但獨立 kernel 重跑仍未完成；不得直接斷言 SDE 污染。已存在的參考審查文件不回溯冒充 R3.2 正式結果。

醫療 Pilot 應選具有可查的原始方法、流程圖、次群/外部驗證或完整附錄的論文；未經選定與實跑，不宣稱通過。

## 11｜追溯來源

- SDE v1.0 + PATCH v1.1：`理火理論/理火總體系(搭配V5版) (4).md`，約 6630–7127 行。
- PAPER 父版：`PAPER/理火論文審查系統_V3.0-EXP-QS-R3.1_全程Main接入法位後補_V3.5.1控制面對齊正式增量版.md`。
- MED 父版：`PAPER/LIHUO_MedReview_Agent_v0.2.md`。
- Root（較新）：`理火V5系統/V5.1版本/` 所屬 Protocol V5.1.0 / Lighter V5.1.0 / Main V5.1.1。
- Web: `PAPER/LIHUO_WebCase_TXT_Packet_V0.4_分類層發布規格.md`。

> **唯一最短新增規則：每份 PAPER 不只查主張能否成立，也要查它沿著依賴鏈是否悄悄失去成立限制；已經有證據的失效要追蹤是否被繼續引用成穩定，但沒有證據就不得貼 SDE 標籤。**
