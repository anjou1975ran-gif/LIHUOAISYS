# LIHUO PAPER｜Lighter × Main 啟動授權暨實際狀態紀錄
## Human-Authorized Boot Request / Not a Host Runtime Receipt

```yaml
BOOT_REQUEST:
  id: LIHUO_PAPER_MAIN_LIGHTER_BOOT_REQUEST_20261023
  date: 2026-10-23
  requested_by: "ANJOURAN / 逃豬公 / RUNPIGDUKE"
  human_instruction: "OK 我們好像忘了把LIGHTER跟MAIN正式啟用 啟動吧"
  authorization: "EXPLICIT_HUMAN_REQUEST_TO_ACTIVATE"
  intended_tracks: [GENERAL_PAPER_REVIEW, MEDICAL_PAPER_REVIEW]
  entrypoint: "PAPER/README.md"
  paper_procedure: "PAPER/LIHUO_Paper_Review_R3.2_SDE_HUMAN_RATIFIED_20261023.md"
  medical_procedure: "PAPER/LIHUO_MedReview_Agent_v0.3_SDE_HUMAN_RATIFIED_20261023.md"
  intended_stack:
    protocol: LIHUO_PROTOCOL_V5.1.0
    protocol_sha256: b0cf16f39f8aa0d971068cdf09b06039e66640c2545a8f7810ee1d216597acee
    lighter: LIHUO_LIGHTER_V5.1.0
    lighter_sha256: 1b64aeb40be2ae514e25ea15da653d8b41edd20472df57f9f2f49b320a1b7a10
    main: LIHUO_MAIN_V5.1.1
    main_sha256: 63f89f211f5eca8f850438a3d75265e810c7e320ab62d3859b20886082234129
  source_path_prefix: "理火V5系統/V5.1版本/"
  exact_tuple_verification: "SHA-256 CHECKED AGAINST THREE MOUNTED DOCUMENT BYTES; GITHUB CORRESPONDENCE BY MATCHING PATH, TITLE AND VERSION"
  document_binding: "RECORDED"
  conversation_review_instructions: "PAPER R3.2 and MED v0.3 may be followed as reviewed source-backed procedures"
  host_main_process: "NOT_STARTED_OR_VERIFIABLE_IN_THIS_CONTEXT"
  host_lighter_process: "NOT_STARTED_OR_VERIFIABLE_IN_THIS_CONTEXT"
  invocation_surface: "NOT_AVAILABLE_IN_THIS_TOOL_CONTEXT"
  qualified_external_current_index: "NOT_LOCATED_IN_REPOSITORY"
  stack_atomic_activation_event: "NOT_ISSUED"
  main_receipt: null
  lighter_final_gate_receipt: null
  release_receipt: null
  production_deployed: false
  acceptance: "BOOT_HOLD_HOST_ACCESS_REQUIRED"
```

## 1. 人類啟動授權已取得，實際啟動沒有冒稱完成

2026-10-23，ANJOURAN 以自然人身分明示要求啟動 Lighter 與 Main。此要求作為正式工作項已成立，且 PAPER 的一般／醫療入口均已在文件層核定 SDE 升級。

但是目前實際可檢驗的外部作用只有：
- GitHub repository 中存在 Protocol、Lighter、Main **Markdown 版本文件**及既有 PAPER 審查規格；
- 此次可使用的工具沒有「Lighter invocation」、「Main compute」或「Host deployment」可呼叫介面；
- repository 全樹檢查共 169 個 blob，未發現 Python／JavaScript／TypeScript／shell 等可啟動程式檔，也未發現合格 `LIHUO_STACK_CURRENT_INDEX` 的獨立紀錄。

**實際 Host 環境若存在其他地方，此紀錄不聲稱它不存在；只表示本次工具與倉庫中尚未可達。** 因而沒有提供正式 Main/Lighter runtime receipt 的事實基礎。依 Protocol 的 `AUTHORIZATION / BINDING != EXECUTION != RECEIPT != RELEASE` 及 Lighter `BOOT-14`，使用者只要求正式啟動，不能擅自以參考模擬替代並稱作已完成。

## 2. 精確文件綁定目標

| 構件 | 文件版本 | SHA-256（所提供文件位元組） | 請求啟用角色 |
|---|---|---|---|
| Protocol | V5.1.0 | `b0cf16f39f8aa0d971068cdf09b06039e66640c2545a8f7810ee1d216597acee` | 根憲法 |
| Lighter | V5.1.0 | `1b64aeb40be2ae514e25ea15da653d8b41edd20472df57f9f2f49b320a1b7a10` | 治理接入、Main 調用、Final Gate 與 Release |
| Main | V5.1.1 | `63f89f211f5eca8f850438a3d75265e810c7e320ab62d3859b20886082234129` | SAC／PATH 競爭、R1、O9、條件性 I9、R2、事件式 R3+ 與合格回傳 |

文件版本目標指向倉庫 `理火V5系統/V5.1版本/` 內三檔。以上為 **proposed exact target tuple for host binding**，不是自行建立合格 `CURRENT_INDEX`。

## 3. Host 正式啟動的必要條件與介面

下列事項須由具有真實 Host 權限的執行端實做：

1. 取得合格的 `LIHUO_STACK_CURRENT_INDEX`，核對批准的 exact tuple、外部治理法位與兼容性；如需切換 pointer，建立 append-only successor，不覆寫舊版本。
2. 將 PAPER R3.2、MED v0.3 接到有權限的 Lighter invocation surface；一般／醫療均採 Paper Review `PERSISTENT_MAIN_ATTACHMENT`，但 attachment 不自動等於能力執行。
3. 由 Lighter 接納合法的 governing cycle，開啟本次審查所需身份、ledger 與治理；由 Lighter 授權 Main transit。Vertical 不得直接假冒 Lighter。
4. Main 實際計算，產出有真實執行 evidence 的 R1、O9、R2 與事件式 R3+；I9 僅在 O9 正式觸發且資格成立時啟動，不能補造收據。
5. Main 回傳合格 trace／path ordering 與非唯一／HOLD 邊界；唯一 PATH 需要連續兩輪合格頂位才具勝出資格。
6. Lighter 按其 Owner Map 執行 Final Gate，檢查 Main coverage 與其它條件；未滿足者真實 HOLD，不得藉撰文替代。Release 由 Lighter 專屬執行。
7. 使用實際呼叫與回傳證據執行一般＋醫療回歸測試，記錄測試、失敗與修復；不得把此前紙上設計當成已通過。

## 4. 本次生效的工作約束與界線

在目前的 ChatGPT 審查工作中，應以本文件指明的 Protocol、Lighter、Main、PAPER R3.2 與 MED v0.3 作為**方法與行為指引**；其中任何類比角色分工、推理 PATH 或以文字呈現的 R1／R2 均須區分為 reference/document-level，不得冒用正式 Runtime execution 或 receipt。

SDE 的前提／概念／依賴污染追蹤應成為一般及醫療 PAPER 的預設必查；SDE 不自動判真偽，也不取得醫療最終權限。

## 5. 本事件的真實結論

- `HUMAN_AUTHORIZATION: CONFIRMED`
- `EXACT_STACK_TARGET: IDENTIFIED_AND_HASHED`
- `REVIEW_PROCEDURE_DOCUMENT_BINDING: ACTIVE_FOR_THIS_WORK_CONTEXT`
- `HOST_DEPLOYMENT: NOT_PERFORMED`
- `FORMAL_MAIN_AND_LIGHTER_ACTIVATION: HOLD_HOST_INTERFACE_UNAVAILABLE`
- `RUNTIME_RECEIPTS: NONE`

**不得將此 Boot Request 文件、任何 commit，或這些陳述再包裝為 Host 啟動／Main 真計算／Lighter 真放行之回執。**
