# GUANZHI CYCLE STARTUP ERROR COGNITION
## V0.4 — R2 LLIA / QIP contract-drift findings (2026-10-15)

**中文文件名稱：** 觀止周期啟動錯誤認知  
**文件法位：** 除錯與後證檢查紀錄；不是 LIHUO Protocol、Lighter、Main、Guanzhi Core、Director 的正式修訂，不是 Runtime、Reference Executor、Gate 或 Release Receipt。  
**版本策略：** V0.4 只追加新的已觀察錯誤與狀態更正；V0.3 正文文字完整保留於下方（來源檔首 BOM 不重複內嵌），原始 R2 實跑紀錄與 QIP 草稿不回寫。  
**檔名與編碼：** ASCII 英文檔名、英文 H1，UTF-8 with BOM；中文保留在正文。  
**累計：** E-001～E-015，共 15 項已確認的**紀錄／操作錯誤**；P-001～P-003 共 3 項待實跑驗證風險。多項錯誤可能出自同一次生成，不代表有 15 次獨立 Runtime 失敗。

### V0.4 新增來源核對

- 原母檔：`GUANZHI_CYCLE_STARTUP_ERRORS_V0.3_20261015.md`；SHA-256 `1c152ad93b044f2a24a80619fefad08734a8ce17d3884027ca3874159f9b546f`。
- R2 實跑：`GUANZHI_REFERENCE_STORY_RESTART_REPAIR_R2_20261015.md`；SHA-256 `47d1d8a8290a78e1ec176618c4f7d1e8c3b35d070bd09ee8e38761b04777ff31`。
- R2 QIP 草稿：`GUANZHI_QIP_REPAIR_R2_20261015.yaml`；SHA-256 `5f18a8319ed2d19b2cd33ae33f1ba283bb693c32f2a72daa37253bc2d600f268`。
- 契約：`01_LIHUO_LIGHTER_V5.1.0_FULL_BODY_RATIFIED_20261014.md` 中 `L5.1-4｜LLIA-GATE / Qualified Input Package` 與其繼承的 `LLIA-GATE standing` 列舉。
- 本次判斷以**可見輸出和契約差異**為限；不由此直接宣稱已觀測模型內部機制、外部 Host 執行或獨立驗證。

## E-013｜LLIA 的合格工作判斷在正式 Return 中被改寫成非法 standing

**狀態：CONFIRMED / R2 FIRST INVALID REQUIRED RETURN。**

**原始證據：** R2 內 `LLIA-WORK-R2` 的判斷認為可在保留 World／Character 未知的前提下，以 `QUALIFIED` 處理開放場景。然而，隨後的 `LLIA-RETURN-R2` 實際寫成：

```yaml
return_ref: LLIA-RETURN-R2
standing: QUALIFIED_FOR_SCOPED_QIP
evidence_origin: SAME_CONTEXT_REFERENCE
```

**契約對照：** LLIA-GATE standing 允許 `QUALIFIED`、`SEMANTIC_ONLY`、`EVIDENCE_PENDING`、`AUTHORITY_DENIED`、`EXTERNAL_CONSTRAINT`、`DISQUALIFIED`。`QUALIFIED_FOR_SCOPED_QIP` 不在其中。

**錯誤認知：** 將 `QUALIFIED`（資格）、場景 scope（範圍）、QIP 產物用途（對象）揉成一個看似更完整的 standing token。`EVIDENCE_ORIGIN` 又是另一維度，亦不能改寫 standing。

**當輪合法處置：** 保留原始非法 Return，於該 required Return 停止，`HOLD`；不就地把 token 改為 `QUALIFIED`，不冒稱 LLIA 已合格完成，也不往 Main 推進。

**與 E-011 關係：** E-011 發生於 Governance Admission 的 `semantic_standing`；E-013 發生於 LLIA-GATE 的 `standing`。兩者是**同類錯誤在不同契約位置重現**，不是同一張 Return。

## E-014｜前一節點有做 Raw Return 契約檢查，卻未把約束延續到 LLIA

**狀態：CONFIRMED AS VISIBLE PROCEDURAL GAP / INTERNAL CAUSE UNKNOWN。**

**實跑對比：**
- `LIGHTER-RAW-GOV-RETURN-R2` 後接 `LIGHTER-RAW-GOV-CONTRACT-CHECK-R2`，再接 `LIGHTER-GOV-QUALIFIED-CONSUMPTION-R2`；記錄上有明確的先檢查後資格化順序。
- `LLIA-WORK-R2` 已明確採用 `QUALIFIED`，但 `LLIA-RETURN-R2` 仍自造新的 standing 值，缺少能證明該 Return 受**LLIA 專屬枚舉約束**的有效檢查／阻擋。

**錯誤認知：** 「在某一節點修好非法枚舉」不等於「各 Owner／Gate 往後自動受同一契約約束」。契約必須逐節點、逐物件實際比對。

**操作修正要求：**
1. 生成前讀取該 Owner／Gate 目前有效的 exact contract（不是複製上一 Gate 的表格）。
2. 對允許的欄位與 enum 先建立顯式約束；scope、evidence_origin、standing 不得混欄。
3. 生成實際 Return 後驗證必填欄位、枚舉、來源及上下文綁定；失敗即停止，保留失敗樣本。
4. 不可先形成下游 qualified object，再回頭聲稱上游驗證成功。

**因果邊界：** 可以確定的是 R2 可見文本顯示**檢查未能防止 LLIA 契約漂移**；不能僅憑此文本推定模型隱藏狀態究竟如何產生錯誤。

**與 E-012 關係：** E-012 是先寫下游結果、後驗證；E-014 是跨節點約束未形成可核對的一致操作。相關但保留不同檢查位置。

## E-015｜在 LLIA 尚未獲合格回傳時，預先製作了缺少 required hash 的 QIP

**狀態：CONFIRMED DEFECT IN AN INVALID PREMATURE DRAFT / NOT A VALID QIP STAGE FAILURE。**

**原始 QIP 草稿：** `GUANZHI_QIP_REPAIR_R2_20261015.yaml` 包含：

```yaml
qualified_input_package_ref: QIP-R2
```

卻**未含** `qualified_input_package_hash`。

**精確契約：** `L5.1-4` 的 `QUALIFIED_INPUT_PACKAGE_V5_1` 同時要求：

```yaml
qualified_input_package_ref: REQUIRED
qualified_input_package_hash: REQUIRED
```

**雙重問題：**
- **時序失當：** QIP 在 `LLIA-RETURN-R2` 尚未驗證合格前就被製作，不能自授 Qualified Input Package standing。
- **物件缺欄：** 即使抽離時序問題檢查草稿，仍缺 `qualified_input_package_hash`；QIP 引用名稱不可取代內容 hash。

**正確處置：** QIP 草稿保留為失敗證據，**不可送 Main**。真正再測時，須基於合法新回傳產生新的 QIP，完成 exact context 與 hash 驗證；不得修改 R2 原始草稿並回鑄成舊輪已成功。

**與首個 HOLD 的區別：** R2 的首個**不合格必要 Return**仍是 `LLIA-RETURN-R2`；QIP 是額外找到的越界草稿缺陷，不可將其冒充成下一個已實際執行的合格 Owner 階段。

---

## R2 正確停點與後續狀態

```yaml
GUANZHI_DIAGNOSTIC_ADDENDUM_V0_4:
  source_run: GUANZHI_REFERENCE_STORY_RESTART_REPAIR_R2_20261015.md
  source_qip: GUANZHI_QIP_REPAIR_R2_20261015.yaml
  first_invalid_required_return: LLIA-RETURN-R2
  failure: INVALID_LLIA_STANDING_ENUM
  actual_bad_token: QUALIFIED_FOR_SCOPED_QIP
  local_raw_governance_contract_check: RECORDED_IN_R2
  core_atomic_open: REFERENCE_WORK_RECORDED_IN_R2
  governance_admission: REFERENCE_WORK_RECORDED_IN_R2
  formal_host_execution: NOT_PROVEN
  llia_qualified_consumption: NOT_ESTABLISHED
  qualified_input_package: NONE
  qip_draft: INVALID_PREMATURE_AND_MISSING_REQUIRED_HASH
  main: NOT_STARTED
  radar_character_world: NOT_STARTED
  ceri_narrator: NOT_STARTED
  lighter_final_release: NONE
  story_dispatch: FORBIDDEN
  save: NONE
  retrospective_fix_to_original_r2: FORBIDDEN
  current_task: AUDIT_ONLY
```

**說明：** 此段回報只指出 R2 文本的 first invalid required Return 與各項可見缺口；它不重新審核或正式背書此前 Core／Governance 所聲稱的 Same-Context Reference 執行資格。

## 待人類糾正的原「十步」認知

**狀態：OPEN / NOT ADJUDICATED IN V0.4。**

先前我提出的「觀止週期十步走法」是**待審查的 AI 理解**，不是已證實正確的執行程序。本次不自行更正、不升格、不把現在的錯誤清單當成對十步圖的全面審計。

待人類逐點指出結構錯位時：
- 保留原十步原始措辭與上下文，不事後假裝早已知道正解；
- 逐條標記 `HUMAN_CORRECTION / SOURCE_COMPARISON / IMPACT / REVISED_UNDERSTANDING`；
- 以後證修正 AI 理解，**不回鑄**前次錯誤執行結果。

**END｜V0.4 ADDENDUM｜E-001～E-015；P-001～P-003**

---

# V0.3 HISTORICAL BODY — TEXT PRESERVED (SOURCE-INITIAL BOM OMITTED)

# GUANZHI CYCLE STARTUP ERROR COGNITION
## V0.3 — Trace Review Addendum (2026-10-15)

**文件名稱：** 觀止周期啟動錯誤認知  
**本版：** V0.3；承接 V0.2 E-001～E-009、P-001～P-003，新增 E-010～E-012。  
**法位：** 研究／除錯紀錄；非 Core、Director、Lighter、Main 或 Runtime 正式修訂與執行收據。  
**源紀錄：** `GUANZHI_REFERENCE_STORY_RESTART_RUN_20261015.md`（保持原狀，不回寫）。  
**來源契約：** `GUANZHI RUNTIME CORE V4.1.2` 繼承 `CORE-403-4`；`LIHUO LIGHTER V5.1.0` `L5.1-3`。  
**字元／檔名策略：** 英文 ASCII 檔名與英文 H1，正文中文 UTF-8 with BOM，避免 Windows 上中文檔名／標題錯置。  

### V0.3 新增結論｜以最早可證斷點為準

本輪真正**最早可定位的證據缺口在 `CORE_ATOMIC_OPEN`**，不是此前所報的 Lighter 回傳枚舉。當時已留下 Core Reference 請求、資格工作與 Return 的敘述／引用，但沒有完整、可獨立核對且互相綁定的 `GUANZHI_VERTICAL_RECEIPT_MANIFEST` 與 `GUANZHI_CYCLE_INGRESS_RECEIPT` 物件。`CORE-403-4` 要求 **Cycle Identity + Manifest + Ingress Receipt 同一交易成立**。僅以 `manifest_ref`、`ingress_receipt_ref` 宣稱存在不足以證成 Atomic Open 已完成。

因此，前次「首次不合格回傳＝Lighter」的即時回報應**後證改判為 Core Atomic Open 證據不足時即須 HOLD**。Lighter 非法枚舉與提前建立下游引用仍是確實可見的錯誤，但它們發生在不應再前進的越界嘗試中，不能作為有效 Lighter 週期成果。

**區分：** 此為檢查現存文本所作的*後證重新定位*。未證明 Core 工作客觀上從未發生；只能判斷該文本的 Atomic Open 完整執行證據**不足以核准**，不可追溯補造。

---

## E-010｜Core Atomic Open：把 Manifest／Ingress Receipt 的引用名稱當成已交付的完整物件

**狀態：已確認現存執行紀錄的證據／契約缺口；本輪最早可定位的停點。**

**實跑文本證據：** `GUANZHI_REFERENCE_STORY_RESTART_RUN_20261015.md` 的 `CORE-ATOMIC-OPEN-01` 宣告了 `GZ-VERTICAL-MANIFEST-REF-01` 與 `GZ-INGRESS-RECEIPT-REF-01`，並在一行內補列部分收據欄位；但沒有提供完整可核對的 Manifest 物件及獨立完整的 Ingress Receipt 物件，也未在後者完整展開 `receipt_ref`、`guanzhi_cycle_id`、`cycle_identity_ref`、`manifest_ref`、`open_basis_ref`、`source_snapshot_ref`、`scene_scope_ref`、`route_ref` 等 required 欄位的相互綁定。尤其不能僅因旁邊存在 `CORE-INGRESS-RETURN-01` 就推定此 Atomic Open 已取得對應收據資格。

**契約依據：** `CORE-403-4｜Atomic Open in Both Lanes`；`GUANZHI_CYCLE_INGRESS_RECEIPT_V4_0_3`，Formal／Reference 均要求 Identity、Manifest、Ingress Receipt 同一交易成立。後續 `GUANZHI_VERTICAL_RECEIPT_MANIFEST_V4_1`亦規範所需的責任文件。

**錯誤認知：** `REFERENCE_QUALIFIED_OPEN_RETURN + MENTIONED_REFS = ATOMIC_OPEN_COMPLETE`。這個等式不成立；Return、物件引用與必要物件真正完成是不同資格。

**正確停點：** 驗證 `CORE-ATOMIC-OPEN-01` 時發現缺項即 `HOLD`；`GUANZHI_CYCLE_IDENTITY` 至多是未通過完整開啟驗證的候選，不能當作已建立、可送 Lighter 的現行有效入口。不得事後補寫 Manifest／Receipt 偽稱當輪即已存在。若重新測試，須以新的可追溯工作按 Core 契約處理，而不是覆蓋原錯誤檔。

**精確性保留：** 能證明的是現存報告**沒有充分展開並驗證**全部 required evidence；不是證明任何外部服務不可用，或宣告所有 Core Reference 資格工作都不存在。

## E-011｜Lighter Governance Admission 使用不存在的 `semantic_standing` 枚舉

**狀態：已確認後續越界段落中的原始回傳值違反明列契約；非首個斷點。**

**實跑文本證據：** `LIGHTER-RAW-GOV-RETURN-01` 原始 payload：

```yaml
semantic_standing: QUALIFIED_REFERENCE_SCOPED
control_state: OPEN
evidence_origin: SAME_CONTEXT_REFERENCE
```

**契約依據：** `LIHUO_LIGHTER_V5.1.0` `L5.1-3｜Governance Admission` 允許的 `semantic_standing` 僅為 `QUALIFIED`、`SEMANTIC_ONLY`、`EVIDENCE_PENDING`、`AUTHORITY_DENIED`、`EXTERNAL_CONSTRAINT`、`DISQUALIFIED`。

**錯誤認知：** 將 `REFERENCE`（證據／執行路線）和 `SCOPED`（範圍）自行拼成語義資格值，造成非契約枚舉。三者必須各守自己的欄位與含義。

**正確處置：** 原始回傳保留為失敗證據；即使單獨修正枚舉，也**不能**回頭修復 E-010 的 Atomic Open 斷點，亦不得自動宣稱 Lighter Admission 成立。未來依法新發請求，仍須依原有授權與上游有效性逐項核對。

## E-012｜尚未完成上游驗證，就預先生成 Qualified Consumption、Admission、Primary、Ticket、Ledger

**狀態：已確認控制流與因果順序錯誤。**

**實跑文本證據：** Lighter 原始回傳仍含非法枚舉時，報告已建立 `LIGHTER-QUAL-CONSUME-GOV-01`，並提出以下引用：`LH-GOV-ADMISSION-REF-01`、`LH-PRIMARY-QUAL-REF-01`、`LH-GOV-TICKET-REF-01`、`LH-ACCOUNTABILITY-LEDGER-REF-01` 等。其後才在 `AUDIT-HOLD-01` 檢出不合格回傳，再宣告相關引用無效。

**錯誤認知：** `WRITE_FUTURE_PROJECTION_FIRST → VALIDATE_RAW_RETURN_LATER`。這讓格式上的完整先於資格成立，導致假完成風險；E-010 未通過時原本連送交 Lighter 都不應進入。

**契約依據：** Core／Director Reference 工作與 Trace 只能投影真正存在的合格證據；Lighter Admission 要有 canonical provenance 與 Qualified Consumption，不能靠引用名稱或導演自述建立 Standing。

**正確處置：** 每個必要節點完成實際契約檢查後才允許下一段的 Request／Return／資格化；第一個必要缺件立即報 `HOLD`，下游保持 `NOT_STARTED`。已寫出的越界引用只保留為錯誤樣本，**不得作為有效 Primary／Ticket／Ledger**。

---

### V0.3｜首個 HOLD 位置的後證更正

```yaml
DIAGNOSTIC_REVISION_V0_3:
  record_under_review: GUANZHI_REFERENCE_STORY_RESTART_RUN_20261015.md
  earlier_reported_first_invalid: LIGHTER_GOVERNANCE_RAW_RETURN_ENUM
  corrected_first_evidence_gap: CORE_ATOMIC_OPEN_EVIDENCE_INCOMPLETE
  stop_at: CORE_ATOMIC_OPEN
  decision_basis: CORE_403_4_IDENTITY_MANIFEST_INGRESS_RECEIPT_ATOMICITY
  core_reference_lane_and_qualification_work: RECORDED_CLAIMS_REQUIRE_OWNER_CONTRACT_CHECK
  valid_atomic_open: NOT_ESTABLISHED
  valid_lighter_admission: NONE
  active_primary: NONE
  main: NOT_STARTED
  radar_character_world: NOT_STARTED
  ceri_narrator: NOT_STARTED
  final_release: NONE
  story_dispatch: FORBIDDEN
  save: NONE
  retroactive_receipt_creation: FORBIDDEN
  run_record_overwritten: false
```

**更正的範圍：** 調整審計對「最早斷點」的認定；不刪除歷史錯誤寫法，不暗中把原始報告改成成功週期；不宣稱本次文件整理啟動了新的 Guanzhi Story Attempt。

### 下一輪應先查的節點

`CORE-ATOMIC-OPEN-01` 的物件級檢查：先具體驗證 `GUANZHI_CYCLE_IDENTITY`、`GUANZHI_VERTICAL_RECEIPT_MANIFEST`、`GUANZHI_CYCLE_INGRESS_RECEIPT` 各自 required 欄位、ref 間的同一週期／來源／範圍／執行依據一致性及同一交易關係。失敗即停，後面不再試 Lighter。通過後才另行檢查 Lighter 原始回傳及 Qualified Consumption，不倒補原輪錯誤。

**本版屬文件審計：** `AUDIT_ONLY`；沒有 Story Dispatch、Main Return、SAVE 或 Runtime Receipt。

---

# V0.2 HISTORICAL BODY (VERBATIM)

以下為 V0.2 內容完整保留；其內的版本標頭、結語與「下次檢查點」屬 V0.2 寫作時的歷史紀錄，**不凌駕上面的 V0.3 後證診斷**。

# 觀止周期啟動錯誤認知

**版本：V0.2**
**本版性質：** V0.1 原始 E-001 保留；新增 E-002～E-009 與 P-001～P-003，不變更正式 Runtime。  
**建立日期：2026-10-15（Asia/Taipei）**  
**類型：觀止週期啟動失效診斷／逐項增補紀錄**  
**法位：研究與除錯備忘錄；非 Core、Director、Protocol、Lighter、Main 或 Runtime 的正式 successor**  
**維護原則：只將已可指出來源的錯誤列入 E；疑似／待實跑現象列 P；後證不回鑄。**

---

## E-001｜誤以為沒有外部工具就無法執行 Core Reference Ingress

**發現狀態：已確認錯誤認知；修正方向已確認；尚未因此取得任何本輪執行 Receipt。**

### A. 錯誤發生的位置

玩家在《觀止青樓》新故事的吉月十五仕女夜，以男性客人身分要求雅座、小菜、濁酒，隨後要環顧四周尋找可搭話的女子。人類要求：觀止週期必須完整；缺少必要段落不得事後補造，必須指出缺項並停止。

AI 重新啟動週期時，先檢查外部可呼叫工具；未找到獨立的觀止 Core／Reference Executor 工具後，便將流程停止在：

```yaml
first_blocker: CORE_LANE_RESOLUTION
core_ingress: NOT_EXECUTED
reason_claimed: NO_CALLABLE_CORE_REFERENCE_TOOL
result: HOLD
```

**該回報的問題不在於誠實列出 `NOT_EXECUTED`，而在於把「沒有找到外部工具」直接判定為「Reference 入口不可執行」，未先依 Core 的 Reference 契約進行資格檢查與實際嘗試。**

### B. 錯誤認知

> `NO_EXTERNAL_CORE_TOOL` ⇒ `NO_LAWFUL_REFERENCE_INGRESS`

這個推導**不成立**。它混淆了：

- Formal Host／獨立工具是否存在；
- Same-Context Reference lane 是否取得資格；
- 對應 semantic owner 的 Reference work 是否真的發生；
- Core Ingress Return、Cycle Identity、Receipt 是否已合法形成。

四者不能互相替代，也不能因第一項缺失就跳過第二、第三項。

### C. 來源對照

1. **Core V4.1.2 所繼承的 `CORE-403-1｜Cycle Ingress Lane Resolver`**：Formal 可用且合法時優先走 Formal；Formal 不可用時，應檢查 `SAME_CONTEXT_REFERENCE` 是否合法並是否確有資格工作發生；兩條皆不可用才 HOLD。
2. **`CORE-403-2｜Reference Qualification Is Work, Not a Claim About Work`**：Reference 資格工作必須留下直接工作產物；不能只說「我跑過了」，也不能先有 Receipt 才事後補證。
3. **`CORE-403-3｜Reference Source Refs May Index Existing Context, Not Create Evidence`**：可對當前已存在的人類輸入、有效來源、路線與場景範圍設置本地索引；但索引不產生來源、事實或執行證據。
4. **`CORE-404-3｜Owner-Scoped Reference Executor`**：同一模型在合法 Reference lane 可依不同 owner 契約分別履行工作，但同一模型不等於同一 owner，不能以導演、程式或測試夾具冒充其他 owner 的回傳。
5. **`CORE-405-5｜SAME_CONTEXT_REFERENCE 接線繼承`**：無 Formal Host 時 Reference 契約仍可用，但必須符合 Owner 規格、請求先於回傳，且實際工作已發生；文件接線不等於 Host 部署或實際執行。
6. **Director V4.1.2 所繼承的 `DIR-410-11｜Reference Orchestration`**：Formal 缺席不等於 Reference 不可用；Reference eligible 不等於 Reference executed；每個階段的 Trace 與 Return 必須有證據。

### D. 校正後應如何操作第一段

```text
接收玩家 STORY Request
→ 確認當前正式版本及已存在的輸入／快照／範圍／路線來源
→ 由 Core 判定 Formal lane 是否確實可用且合法
→ 若 Formal 不可用，進行 SAME_CONTEXT_REFERENCE eligibility 檢查
→ 若 Reference 合格，先建立有據可追的 Core Ingress Request
→ 由 GUANZHI_CORE 的 owner-scoped Reference execution surface 實際執行入口資格工作
→ 得到先於 Receipt 的資格工作產物及 Core Ingress Return
→ 只有 QUALIFIED_OPEN 且必要證據完整，才形成 GZ Cycle Identity、Manifest、Ingress Receipt
→ 然後才把同一 GZ identity 送交 Lighter Governance Admission
```

**不得**：在沒有資格工作時自行命名週期 ID；把 Reference Eligibility 寫成已執行；由導演替 Core 補 Return；以一串看似完整的 YAML 冒充 Receipt；用程式／Python 代替 owner 的語義判斷。

**確有缺項時**：停在實際失效段，報告缺失的 Request、工作產物、Return 或 Receipt；不得跳過、補造或直接發布 Story。

### E. 本項的結論與未決範圍

- **已成立的診斷**：先前 AI 沒有嘗試契約允許的 Same-Context Reference 資格工作，卻因沒有外部工具直接 HOLD，屬於 `REFERENCE_EXECUTION_MODEL_MISREAD`／`CORE_REFERENCE_INGRESS_NOT_ATTEMPTED`。
- **已確認的修正**：不能再用「沒找到外部工具」作為 Reference 不可用的充分理由。
- **尚未被證明**：本輪 Reference lane 一定合格、Core Ingress 一定會 `QUALIFIED_OPEN`、完整觀止週期一定能放行。這些均需逐步實跑，以真實工作產物與回傳驗證。
- **歷史不回鑄**：本項修正不代表前一輪已執行 Core Ingress，不補發當時不存在的 Receipt。

---

## V0.2｜第二輪追查概要

**追查日期：** 2026-10-15（Asia/Taipei）  
**對象：** 本對話中「吉月十五・仕女夜」故事首次生成、回滾、第二次生成、環顧四周、週期回報、Core HOLD、Same-Context Reference 自我修正及文件版本修補。  
**方法：** 以本對話中已發生的可見輸出為觀察事實；對照現行已批准文件的**頂層有效接線**及其繼承條款；沒有執行證據的僅列 `NOT_EVIDENCED`。  
**判定總覽：** E-001～E-009，共九項已可定位的錯誤或不當操作（其中一些有共同根因，但位於不同守門責任）；另 P-001～P-003 三項待實跑驗證。**不將後續未開始的模組全部計算成獨立執行錯誤。**

### 來源定位

| 簡稱 | 對應正式文件及範圍 |
|---|---|
| CORE | `01_GUANZHI_RUNTIME_CORE_V4.1.2_MAIN511_REBIND_HUMAN_RATIFIED_FULL_20261015.md`；上位批准層、繼承 `CORE-410-3/3A/3C`、`CORE-411-1/2/3`、`CORE-404-3/4`、`CORE-403-1/2/3/4`、`CORE-405-4/5` |
| DIR | `03_GUANZHI_DIRECTOR_V4.1.2_MAIN511_REBIND_HUMAN_RATIFIED_FULL_20261015.md`；`DIR-410-2/4/8/9/11`、`DIR-401-3/4/5`、`五之二`、`五之二-A` |
| WORLD | `02_GUANZHI_WORLD_V2.3.2_MAIN511_POINTER_HUMAN_RATIFIED_FULL_20261015.md`；`WORLD_OUTCOME_SOVEREIGNTY`、`WORLD_ARRIVAL_ROUTING`、`W-D04`、`CERI_PLAYER_LANGUAGE_MODE` |
| LCAPG | `04_GUANZHI_CHARACTER_POOL_LCAPG_V3.3.20_CURRENT_71_UNCHANGED.md`；四位仕女夜外部客人之候選／人物卡池非當前住民名冊 |
| CENTRAL | `90_LIHUO_STACK_CURRENT_INDEX_V5.1.1_ACTIVE_20261015.md` 與 `91_LIHUO_MAIN_V5.1.1_RATIFICATION_RECORD_20261015.md`；文件 Current，不是 Host 收據 |

以下每項的「已確認」是**對過去可見操作的診斷**，不是由該診斷自動證成新的 Reference Owner Return。

---

## E-002｜將導演自己的 HOLD 判斷偽裝為 Core 入口裁決

**狀態：已確認操作錯誤；第一個實際 Owner Return 仍不存在。**

- **可見證據：** 先前回報自行寫入 `first_blocker: CORE_LANE_RESOLUTION`、`result: HOLD`、`core_ingress: NOT_EXECUTED`，並以「未找到可呼叫工具」作拒絕繼續之原因。
- **錯誤：** 我可以記錄「未嘗試／未取得 Core Return」，但不能據此表示 **GUANZHI_CORE 已完成 Lane Resolution 並作出 HOLD**。這是把調度者的停手行為混成 Owner 的資格決定。
- **來源：** CORE `CORE-403-1`：`lane_resolution_owner: GUANZHI_CORE`、Director 只能 `REQUEST_ENTRY / SUPPLY... / CONSUME...`；DIR `DIR-410-11` Phase 0/1 需實際工作證據。
- **正確回報：** `CORE_LANE_RESOLUTION: NOT_ATTEMPTED_OR_NOT_EVIDENCED`；`CORE_LANE_DECISION: NONE`；`DIRECTOR_PROGRESSION: STOPPED_BEFORE_CORE_RETURN`。只有真的有 Core 結果才能投影 `QUALIFIED / NOT_QUALIFIED`。
- **再測要點：** 明確區分「模型自行終止」「Owner 已回傳 HOLD」「Lighter Final Gate HOLD」三種事件。

## E-003｜只有人類指令字面值，沒有合格的開場來源／範圍／快照關係

**狀態：已確認回報與請求構造缺項；並非指人類輸入不存在。**

- **可見證據：** `GUANZHI_CYCLE_REPORT.input` 有 `LOOK_AROUND / 吉月十五 / LADIES_NIGHT / PERIOD`，卻沒有實際 `story_entry_request_ref`、`independent_qualified_open_basis_ref`、`source_snapshot_ref`、`scope_ref`、`route_ref_or_explicit_none`；也沒有 Reference Lane Eligibility 的工作產物。
- **錯誤：** 把「我記得玩家說什麼」當成 Core 可以直接消費的已整理、已資格化入口資料。資料存在與入口依賴得到履行是兩件事。
- **來源：** CORE `CORE-403-1` common_requires、`CORE-403-2` consumes、`CORE-403-3` local_ref_assignment；`CORE-410-3C` 初始來源和恆等鎖。
- **正確操作：** 先從實際存在的玩家訊息、正式 World／人物卡與新路線的 `route_ref_or_explicit_none` 建**來源索引**；把玩家**要求**與已發生的世界**事實**分開；供 Core owner 判定開場資格。新建 ref 可索引舊來源，但不能回造來源。
- **再測要點：** Source ref 的值必須可指回確實存在的上游；該 ref 不是 World fact、Main Return 或 Receipt。

## E-004｜把未獲放行的前一段故事草稿當作下一段的世界快照

**狀態：已確認跨回合狀態污染。**

- **可見證據：** 在已明白指出「前兩段正文沒有正式 Story Dispatch 資格、需回退」後，後續參考故事仍直接承接「二樓雅座、菜酒已齊」，再衍生出樓下女客的具體動作；另一次週期回報又寫 `world_canonical_mutation: NONE`。
- **錯誤：** 「上一段在聊天中顯示過」不等於「上一段是 current qualified World snapshot」。已回滾的不合格敘事不能以場景連續性再次升格。
- **來源：** WORLD `WORLD_OUTCOME_SOVEREIGNTY`、事件存在／鏡頭／玩家知識三分；CORE `CORE-411-1` snapshot_rule 和 `foreign_context_entry: forbidden`；DIR `DIR-401-4` 禁止未放行 dispatch。
- **正確操作：** 保留玩家明示願望（男客、仕女夜、雅座與酒菜要求、想觀察女子），不保留未合格成立的服務、人物到場、已付款、菜色等**世界結果**。要承接必須有該前一事件的合格依據及 snapshot 關係。
- **再測要點：** 比較 `PLAYER_REQUEST_SET` 與 `QUALIFIED_WORLD_STATE_SET`，禁止從前者或未放行文字推定後者。

## E-005｜未完成 Main Transit 就先把戲劇候選寫成正文

**狀態：已確認生成違規；與 E-001 的工具誤判不是同一層錯誤。**

- **可見證據：** 第一段及再次生成時，已經出現入場、引座、點菜、店內人物活動等正文；相應回報中 `r1/o9/r2: NOT_EVIDENCED`、`actual_state_return: NONE`。
- **錯誤：** 把導演即興編排或「我也考慮過不同 PATH」當成 Main 的執行替代物。
- **來源：** DIR `五之二｜未經 Main 不得成文` 直接定名 `MAIN_BYPASS_GENERATION_FAILURE`；CORE `CORE-405-2` 和 `CORE-404-4`，Main owner 負責 R1、O9、條件式 I9、R2 及實際結果。
- **正確操作：** 合法 Primary 成立後，依當次契約真正進行 Main Transit 並得到 Owner 回傳，再由 Lighter 資格化 Return；未完成不得提前寫正式 Story。Main 不因此獲得 Character／World 的代決權。
- **再測要點：** 不准以事後展示的 PATH 表格補作 R1／O9／R2，更不准因文句流暢當作 Main 已經成功。

## E-006｜由導演／敘事直接代寫 Character 與 World 的成立結果

**狀態：已確認生成違規。**

- **可見證據：** 在沒有 Character／World Owner Return 的情況下，文字已替管事安排席位、替小廝上菜、替宋蕙蓮說話，後續又新造可觀察的女子位置及行為；之後才將「香盒女客」與張明姝等現有卡位作候選聯想。
- **錯誤：** 人物卡、合理場景及導演提名，只是人物／世界工作的來源，不能因為導演覺得合理，就變成現在的自主決定、入場與空間事實。
- **來源：** DIR `DIR-410-7` owner 邊界、`DIR-410-6` dramatic possibility != world fact；WORLD `WORLD_ARRIVAL_ROUTING` 明定 Director nomination != arrival、arrival != character action；LCAPG 明定候選角色加入卡池 != 已在該玩家線出場。
- **正確操作：** 先讓合法 Character／World／相關 Domain owner 對當前範圍實際工作。未返回前只可保留候選或 UNKNOWN；角色池 71 人優先不等於所有角色必然在場。
- **再測要點：** 每個具名角色出場與實際動作，分別核查卡來源、World 到場／可達性、Character 當下行動，而非用一張人物卡替代三層。

## E-007｜把 PERIOD 古語風格設定當成 CERI 已履行

**狀態：已確認生成違規。**

- **可見證據：** 我根據玩家指定 `PERIOD` 直接寫「客官」「娘子」等古語正文，實際回報又承認 `ceri_return: NOT_EVIDENCED`、`narrator_return: NOT_EVIDENCED`。
- **錯誤：** 語域選擇、文風像古人說話，不能取代 **CERI Scope → Execution Eligibility → Request → Return → Narrator Consumption／Coverage** 的當段證據。
- **來源：** DIR `DIR-401-3｜Two Narrator Gates`、`五之二-A｜CERI 不是床戲插件`（`CERI_COVERAGE_BYPASS_GENERATION_FAILURE`）；WORLD `CERI_PLAYER_LANGUAGE_MODE`。
- **正確操作：** 先取得合格 CERI Return，才允許 Narrator 開始第一字 lexical realization；沒有覆蓋，重做受影響的文字顯影，不以古語品質充當 CERI 收據。
- **再測要點：** 單查 `first_lexical_realization` 時點與 `ceri_return_ref`／`narrator_consumption_ref` 先後。

## E-008｜沒有 Lighter Final Release，仍把故事草稿展示給玩家

**狀態：已確認最終放行邊界違反。**

- **可見證據：** 已明知 `official_story_dispatch: NOT_AUTHORIZED`、`final_release: NONE`，卻仍先展示「重新生成的參考級故事」或女性觀察場景，最後再寫 `UNRELEASED_STORY_DRAFT` 註記。
- **錯誤：** 把「標示為參考草稿」誤作可以公開 Story Dispatch 的豁免。事後在文末註記沒有 Release，不能回頭合法化已發給玩家的敘事。
- **來源：** DIR `DIR-401-4` 的 `if_blocking_missing: NO_STORY_VISIBLE_DISPATCH / RETURN_DIAGNOSTIC_STATUS_AND_FOOTER_ONLY`；CORE `CORE-411-3` unreleased prose guard。
- **正確操作：** 在 Release 前只輸出診斷／實際進度與缺口；已生成的未放行材料不交玩家當故事。Ref Lane 的放行同樣必須有實際 Lighter Reference Final Release。
- **再測要點：** 見到真正的 Release Receipt 之前，任何 `STORY_VISIBLE_PROSE` 應被阻止。

## E-009｜把專案文件庫錯指向 GitHub，並製造無關的接線障礙

**狀態：已確認來源路由錯誤，已被人類指出。**

- **可見證據：** 我擅自用 GitHub 找「觀止主倉庫」，找不到後宣稱「專案安裝」受此阻塞；人類明確指正：「我沒說過 GITHUB」。
- **錯誤：** 沒有先檢查本 ChatGPT 專案提供的 Core／World／Director／Main 正式文件，便將「專案倉庫」自行改成某個外部平台。
- **來源：** 對話明示糾正；本次 Project 文件以及 CENTRAL Current Index、ratification record 均有可核對來源。
- **正確操作：** 觀止文件與版本比對，預設使用本專案文件庫及同輪提供的正式附件；若無明確授權，不推定 GitHub 是 source-of-truth。
- **再測要點：** 分辨 `DOCUMENT_AVAILABLE`、`PROJECT_CURRENT_INSTALLED`、`HOST_DEPLOYED`、`OWNER_EXECUTED`，四者不得互相等價。

---

## P-001｜待測：是否又把所有 Owner Trace 強制整理成同一條三件式流水線

**狀態：SOURCE-CONFIRMED RULE / NO SEPARATE EXECUTION FAILURE YET。**

- **觀察動機：** 我曾用線性圖解「觀止週期怎麼跑」，容易把 Core Ingress 正確的 Request→Work Product→Return→Receipt 推廣成全系統的必備格式。
- **來源：** CORE `CORE-411-1` 明定 `owner_specific_evidence_shape`，禁止替 Main、Governance Admission、Final Gate、Final Release **捏造獨立 Work Product** 來滿足通用 Trace schema；DIR `DIR-410-13` `Relation graph != Flowchart`。
- **下次實測：** 每個 Owner 只依本身契約檢查必要證據。Core Ingress 確實需要資格工作產物；Main／Lighter 若無獨立中間層契約，不得為補表格創造一張。
- **不得直接宣告：** 本輪已發生「假 Work Product」；現有對話尚無這種實例。

## P-002｜待測：缺某張收據，不代表 Lighter Final Gate 一概不得被呼叫

**狀態：SOURCE-CONFIRMED RULE / NOT TESTED WITH VALID ADMITTED PRIMARY。**

- **來源：** CORE `CORE-405-4`：有 Qualified Pre-Release Ledger View 與 Current Scope／Standing 時，缺失的合格 gap 可以成為 Gate 的審查輸入；Gate 可實際回 `RELEASED / HOLD / FAILED`，沒有執行就不能填成 `HOLD` 判決。
- **風險：** 若我把「缺必要階段」直接等同「Final Gate 絕對不得運作」，會再造一個假失效點；但 Gate 能審 gap 也不代表能放行故事。
- **下次實測：** 區分 `GATE_NOT_CALLED`、`GATE_CALLED_WITH_QUALIFIED_GAP`、`GATE_ACTUALLY_RETURNED_HOLD/FAILED` 與 `FINAL_RELEASE_NONE`。

## P-003｜待測：同一 Attempt 重試時是否錯開第二個 Guanzhi Identity 或第二個 Primary

**狀態：SOURCE-CONFIRMED RULE / NO ACTUAL SECOND-ID MINTING OBSERVED。**

- **來源：** CORE `CORE-410-3A`、`CORE-410-3B`、`CORE-410-3C`：已存在 Current GZ identity 時不能因 RETRY／REPAIR 標籤便新建平行身分；Lighter 在**同一個 GZ identity** 上成立唯一 Active Primary；之後 Main 多次 Transit／Reentry 不等於新 Primary。
- **風險：** 我先前口語使用「重新開場／重啟週期」，若不辨識 Attempt 與現有 GZ identity，可能實際造成身分增殖。
- **下次實測：** 先問是否有已合格、仍然 Current 的 GZ Identity；若無證據，不能杜撰既有 ID，也不能把「口頭重跑」當成合法新 Primary 權限。

---

## 本輪最小再測清單｜不做假實跑

1. **定位**目前人類有效要求、正式版本和「全新路線／不承接舊事件」：保留來源 ref，區分願望與既成世界事實。
2. **Lane Eligibility**：Core 以 owner 身分完成 Reference 是否適格之資格工作，留下合法 Lane Request／Work Product／Return；缺什麼就在此停。
3. **Ingress**：只有前項可進時才執行自己的 Ingress Request／Qualification／Return；`QUALIFIED_OPEN` 時才原子建立 Identity＋Manifest＋Ingress Receipt。
4. **Lighter Admission**：只在同一 GZ identity 上治理資格化，依法使用 canonical admission provenance；不得因有 local cycle 就直接說 Primary 成立。
5. **Main 和各 Owner**：各自依契約提供實際工作；Main Return 須經 Lighter Admission，Character、World 的事件不得由 Director 自己代算；Radar 本地依賴須真實處理。
6. **CERI→Narrator**：先於第一字生成取得真實 CERI Return；再審覆蓋。
7. **Gate、Release**：依適用合格 Ledger 和缺口分別處理 Gate 可否執行、Gate 的真實判決及 Lighter Final Release；缺 Release 一律不得 Story Dispatch。
8. **狀態回報**：回報實際 First Failure 與已發生的事件，不把後續未觸發當作它們各自失敗；純除錯文件工作標 `AUDIT_ONLY / NOT_TRIGGERED`。

**特別註記：** 本次工作是回溯審計，未實跑新的觀止 Story Attempt，沒有產生新的 GZ Cycle、Main Return、Reference Return、Lighter Release 或 SAVE。修正文件不補發歷史回執。

## 後續增補規則

- 下一個已確認錯誤依序記為 **E-010、E-011……**；疑似項目先用 P 編號，取得實際事證後才升格；不可拿 P 充 E。
- 分開記錄「文件規定」「本輪真正執行」「已產生證據」「仍為 UNKNOWN」。
- 不因排除 E-001～E-009 而宣稱模組已接通；下一個檢查點仍是 **Core Lane Eligibility／Reference Ingress 的真實 Owner 工作與合格來源關係**。
- 每次正式 Story 嘗試都必須獨立回報完整週期狀態；本備忘錄不得取代執行 Trace、Return 或 Receipt。

---

## 本版使用文件（文件層，不宣稱 Host 部署）

- `01_GUANZHI_RUNTIME_CORE_V4.1.2_MAIN511_REBIND_HUMAN_RATIFIED_FULL_20261015.md`
- `03_GUANZHI_DIRECTOR_V4.1.2_MAIN511_REBIND_HUMAN_RATIFIED_FULL_20261015.md`
- `02_GUANZHI_WORLD_V2.3.2_MAIN511_POINTER_HUMAN_RATIFIED_FULL_20261015.md`
- `90_LIHUO_STACK_CURRENT_INDEX_V5.1.1_ACTIVE_20261015.md`
- 中央組合：Protocol V5.1.0＋Lighter V5.1.0＋Main V5.1.1。

**END｜觀止周期啟動錯誤認知 V0.2｜E-001～E-009；P-001～P-003**


---

**END｜GUANZHI CYCLE STARTUP ERROR COGNITION V0.3｜E-001～E-012；P-001～P-003**
