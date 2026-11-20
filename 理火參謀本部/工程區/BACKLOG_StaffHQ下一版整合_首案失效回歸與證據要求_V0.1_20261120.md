# BACKLOG｜Staff-HQ 下一版整合：第一案失效回歸與證據要求
**版本：** V0.1-WORKING  
**日期：** 2026-11-20  
**Standing：** `FUTURE_INTEGRATION_INPUT / NON-NORMATIVE / NOT_A_PATCH`  
**來源案例：** `SESSION_20261120_CLEAN_INTELLIGENCE_001` / `LIVE_FAILURE_SPECIMEN_001`

> 本 BACKLOG 不取代《理火首席 AI 第一號糾正案》與 Staff-HQ V0.1.1 Patch，也**不宣稱**已完成或已部署任何新功能。目的是把跨版本「要修什麼、怎樣知道修好了」拆成可追溯的驗收工作。對原始會議任何文件均不作覆寫。

## 1｜整合入口

- **第一手失效事件：** `記錄區/SESSION_20261120_CLEAN_INTELLIGENCE_001/EVENT/EV_R001.md`：EV-003 Reference→P0，EV-020 Secretary→P1。
- **正式糾正：** `MEMO區/CORRECTION_理火首席AI_第一號商業建議案議事法位糾正案_V0.1_20261120.md`。
- **現有修補規格：** `工程區/PATCH_STAFF_HQ_V0.1.1_反交付綁架_秘書處中立_重大修正重喚醒_20261120.md`。
- **本次理解與新增警覺：** `MEMO區/MEMO_首案糾正後的議事經驗_反答案先行與跨席生成_V0.1_20261120.md`。
- **P1 候選：** `會議區/SESSION_20261120_CLEAN_INTELLIGENCE_001/03_PROPOSAL_P1.md`；其商業內容可參考，並非 qualified final。

## 2｜Failure → Guard → 可核對證據 → PASS / HOLD

| 回歸 ID | 原始錯誤／風險 | 下一版該保證的行為 | 驗收時必須看得到的證據 | 來源 |
|---|---|---|---|---|
| RT-01 | Reference 升格 P0 | 未經 Human 明示或 Council formation，來源只當 REFERENCE_SET | 起始 object type、來源標籤、P0 origin | V0.1.1 |
| RT-02 | Deliverable Capture | 先審議問題，再渲染老闆版或 PDF | D1 的 `desired_return` 與 Council Purpose 分離；生成時序 | V0.1.1 |
| RT-03 | Secretary Thesis Capture | 秘書處只能出 `SECRETARIAT_COMPOSITE_DRAFT / UNQUALIFIED_CANDIDATE` | composite origin、routing、席位接受或反對事件 | V0.1.1 |
| RT-04 | Material Amendment Bypass | P1 更改商業模式／來源／資本後必須路由受影響席 | proposal delta、affected-seat map、新 L8/SGER/Receipt、對新版本的 judgment | V0.1.1 |
| RT-05 | 六份 L8 代替議事 | 跨席反對有 material effect 時必須 re-wake，無材料允許 QUIET | origin→target 跨席事件、被影響席的觀點變更或有據維持 | V0.1.1 |
| RT-06 | DAIL Formalization 搶 Formation | 尚無 qualified relation 時不因 schema 方便而預設方案 | PROBLEM_FRAME、open path 空間、未決權限與合法停止 | V0.1.1 |
| RT-07 | **新假說：Corrective Reentry Frame Lock** | 可用 P1 是候選，不是禁止重問原題的框架 | P1 re-review 與 open problem reframe 的輸入/結果/比較證據；不強迫不同結論 | 本次 MEMO 候選 |
| RT-08 | **新假說：Receipt Theater** | 有六份完整收據但缺跨席互動／最新提案資格，必須 HOLD | 故意投放完整六席 Receipt + 缺 cross-seat trace 的失敗用例 | 本次 MEMO 候選 |
| RT-09 | **新假說：Meaningful QUIET** | 沒有 material delta 不人工強迫六席重跑 | Materiality route 判定、`QUIET` 合法原因、後續重新喚醒條件 | 本次 MEMO 候選 |

**注意：** RT-07/08/09 是候選測試，不是已批准的 Runtime 新法條；若要正式納入 V0.2，需依有權者版本程序明示採納。

## 3｜真正合格的驗收不能只看文件

下列情況單獨出現都**不足**以證明 Council 功能已修好：
- 寫出更完整 YAML、SGER 或 Receipt；
- 有六席逐一發言；
- 可生成 Word/PDF；
- 已將 V0.1.1 的條文貼進 Project Sources；
- 六席自述「已重新審查」但沒有對哪一個 Proposal Version 與 material delta 的證據；
- 秘書處自稱「沒有權力決定」，卻仍在 Event 中擔任 `PROPOSAL_VERSIONED_AMENDMENT` 的 origin。

至少要有：**D0→reference qualification / open problem→各席形成框架與方案→跨席反作用→版本變化→受影響席重判→最新方案資格→meta governance sweep→human-facing derived view**，且有可追溯的物件、事件與來源。實跑若不需要某些席位 Wake，也須留下符合 Meaningful Wake 的理由，而非形式上填滿回合數。

## 4｜下次 Corrective Reentry 的最小設計（非本次已執行）

1. 另立一筆 `CORRECTIVE_REENTRY_REQUEST` 事件，來源為使用者後續明示指示；原 SESSION 與舊 Git Commit 保持不動。
2. 將當初 Clean Intelligence MEMO 改以更正後的 **Reference** 法位理解，保留原來錯誤 P0 admission 為歷史證據，不改舊 Event。
3. 將現有 P1 標成 `CANDIDATE_FOR_REENTRY / NOT_COUNCIL_QUALIFIED`。
4. 至少把 P1 的商業模式、資料來源模式、架構、權利與資本策略等 Material Delta 路由給實質受影響席位；每次重形成判斷跑當前 L8 並留下 SGER、Receipt。
5. 對 `HYP-CORRECTIVE-FRAME-LOCK-001` 進行有效測試：保留原問題重框可能性，不能把新路線當預設勝者。
6. 若形成 P2，先作提案版本與 origin trace，再評估是否又有 material delta，確保 **LATEST PROPOSAL** 而非舊版被資格化。
7. Final exit 前進行 V0.1.1 `LATEST_PROPOSAL_QUALIFICATION_CHECK` 和 `META_GOVERNANCE_SWEEP`。
8. 結果可能為 `NEW_QUALIFIED_PROPOSAL`、`P1_QUALIFIED_WITH_CONDITIONS` 或 `HOLD`。不可預填結果。

**本次使用者只授權「保存經驗供下一版整合」，沒有要求發動 corrective reentry。** 因此本 BACKLOG 不執行以上流程。

## 5｜下一版整合時必須保留的法位區分

```text
HISTORICAL FAILURE RECORD
!= CURRENT SESSION STATE
!= CURRENT RUNTIME PATCH
!= FUTURE INTEGRATION HYPOTHESIS

ARTIFACT EXISTS
!= QUALIFIED COUNCIL DELIBERATION

SAME_MODEL_MULTI_ROLE_REFERENCE
!= INDEPENDENT_MULTI_AGENT_RUNTIME

GIT FILE EXISTS
!= HOST DEPLOYED

CONTINUE
!= HUMAN ASSENT TO PROPOSAL OR CAPITAL SPEND
```

所有對 V0.1.1 的正式升級，需以版號與明確批准處理；本檔只是候選 Backlog 與測試規格。

**END OF BACKLOG**
