# MEMO｜參謀本部第一案糾正後的議事經驗
## Anti-Answer-First / Council Formation / Cross-Seat Causality

**版本：** V0.1-WORKING  
**日期：** 2026-11-20  
**來源 Session：** `SESSION_20261120_CLEAN_INTELLIGENCE_001`  
**類型：** POST-REVIEW LESSONS LEARNED / NEXT-VERSION INTEGRATION INPUT  
**提出位置：** 理火參謀本部 AI 工作節點／本次對話的自我檢查  
**現行法位：** `LEARNING_MEMO / NON-NORMATIVE / NOT_CURRENT_RUNTIME_PATCH`  
**依據法位：** 理火首席 AI 糾正案與 `PATCH_STAFF_HQ_V0.1.1` 為前置來源；本 MEMO 僅承接、解釋與提出待驗證問題，不覆寫二者。

> **核心經驗：參謀本部不是「先讓 AI 做出方案，再讓六席審方案」。不同席位的責任必須實際參與形成問題、改寫方向，並因彼此的 material objection 而改變下一輪判斷；最後交付物只能從取得資格的議事結果生成。**

---

## 0｜這個 MEMO 為何存在？

使用者原本要求：讓參謀本部提出「AI 時代乾淨商業情報來源系統」，可以參考既有 `理火商業化/` MEMO，最終交付一般老闆能懂的商業計畫書。

第一案交出了有用的市場分析、成本假設、風險及老闆版 PDF／Word，並留下 N1/A/B/C/D/E 六席 L8、SGER、Receipt、Git 記錄。然而理火首席 AI 審計指出：**交付品質不能替代 Council 的合法形成**。本輪 AI 再核對原事件發現：這不是抽象批評，兩個已保存的 Canonical Event 直接顯示了權限與形成鏈的錯置。

本 MEMO 要保留 **「為什麼會錯」**，不只抄一份 PATCH 指令；供下一版整合者回查失效機制、測試方法與尚存未知。

```yaml
LESSON_REF: STAFFHQ-LESSON-001
CASE_REF: SESSION_20261120_CLEAN_INTELLIGENCE_001
HISTORICAL_CLASS: LIVE_FAILURE_SPECIMEN_001
ORIGINAL_BUSINESS_ARTIFACT: USABLE_CANDIDATE
COUNCIL_QUALIFICATION: INCOMPLETE
EXTERNAL_CORRECTION: RECEIVED_AND_REVIEWED
PATCH_REFERENCE: STAFF_HQ_V0.1.1
NEXT_VERSION_CHANGE: PROPOSED_NOT_RATIFIED
CORRECTIVE_REENTRY_EXECUTED: false
OLD_HISTORY_REWRITTEN: false
EXECUTION_IDENTITY: SAME_MODEL_MULTI_ROLE_REFERENCE
```

## 1｜第一案留存了哪些有價值的東西？

保留而不抹煞：
- 六席提出真實材料性問題：買家是否付費、資料再授權、Rights/Quality 分層、工程路徑與分段資本。
- 方案在概念層由重資本採集網路，轉到可撤回的合作來源／小型 Pilot 候選，具有商業思考價值。
- 知識與權限邊界清楚分離：客戶付費、工程、成本、資金批准皆未宣稱已證實。
- 會議與檔案有實際 Git 留痕，可回溯失效位置。
- 老闆版交付物仍可作為 **候選產品／下一輪 Council Input** 使用，無須刪除。

**但：** 上述都是可用材料，不等於 `P1_COUNCIL_QUALIFIED`。

## 2｜有證據的失效鏈：不是「做錯答案」，而是把形成權集中回秘書處

### 2.1 Reference 被偷升格成 Proposal

使用者說「可以參考 Git 商業化子夾」。原始參考文件應為 `REFERENCE_SET`，不自動帶有立場或方案優先權。

但第一案 `EV_R001.md` 記為：

```text
EV-003 | Origin: SECRETARY | Type: PROPOSAL_ADMISSION | Target: P0
Source: 理火商業化 Clean Intelligence MEMO
```

這一步提前把「有資料」轉成「已設定好要討論哪個提案」。六席第一眼接觸的就不是開放問題，而是被提前偏置的方案座標。

**失效樣本：** `REFERENCE_TO_PROPOSAL_COLLAPSE`。

### 2.2 秘書處取得了本不屬於它的實質選路權

第一案 `EV_R001.md` 同時寫有：

```text
EV-020 | Origin: SECRETARY | Type: PROPOSAL_VERSIONED_AMENDMENT | Target: P1
```

P1 大幅更動商業策略：從先建實體資料網改成先做客戶自有資料／授權合作、延後硬體。這不是排版或摘要，而是商業模式、來源模式和資本順序的 **Material Proposal Delta**。

Secretariat 可以將六席材料編成草案，但草案只能是：

```yaml
object_type: SECRETARIAT_COMPOSITE_DRAFT
standing: UNQUALIFIED_CANDIDATE
requires_material_routing: true
```

**失效樣本：** `SECRETARIAT_THESIS_CAPTURE`。

### 2.3 P1 變了，受影響席卻沒因 P1 而重新形成判斷

六席各自對原 P0 所涉問題跑過 L8，不等於六席審過新 P1。

但第一案 P1 形成後，直接進入 Closure Sweep、`RECOMMENDATION_READY` 及 DR-001，沒有 P1 物質性修改之後的受影響席回喚醒及重判。

**失效樣本：** `MATERIAL_AMENDMENT_BYPASS`。

### 2.4 把六個 L8 的完整性錯當成 Council 的完整性

`N1 L8 + A L8 + B L8 + C L8 + D L8 + E L8 + Secretary Summary` 可以是六份能力不錯的分析，卻仍缺少真正的跨席因果鏈。

應保留這種**可檢查的跨席互動**，而不是要求六席表演輪流說話：

```text
A NEW_PATH
  → C 權利反對
  → A 對新權利限制重新形成 PATH
  → B 因新 PATH 重構公司架構
  → D／E 因架構改變重審工程與資本
  → N1 重判是否仍有客戶價值
```

這是 **material delta 存在時**的示例，不是必跑六席的固定回合模板；沒有新材料，`QUIET` 合法。

**失效樣本：** `L8_AS_COUNCIL_SUBSTITUTE`。

### 2.5 「最後要有商業計畫」綁架了「先形成問題」

原始需求中的「商業計畫、老闆能懂的方案」是 `DESIRED_RETURN`。

第一案卻以「把商業計畫完成」為驅動，把 Research、L8、紀錄、Word/PDF 變成交付路線。即便成品漂亮，也沒有證明它是經由 qualified Council 生成的投影。

**失效樣本：** `DELIVERABLE_CAPTURE`。

### 2.6 系統懂得審市場，卻沒審自己怎麼開會

第一案的問題 MEMO 大多收容資料權利、成本、競爭與工程，卻沒抓到自身的 Reference→Proposal、Secretary 擁有 thesis、P1 未重喚醒、L8 替代 Council 與交付綁架。

**失效樣本：** `SELF_GOVERNANCE_AUDIT_GAP`。這必須在推薦案／決策案准出前跑 `META_GOVERNANCE_SWEEP`。

## 3｜V0.1.1 已提出的補正（這是來源規格，不是本 MEMO 新訂）

1. `REFERENCE != PROPOSAL`；開放題可合法以 `P0 = NONE` 起步。
2. `SECRETARIAT MAY NOT OWN SUBSTANTIVE THESIS`；多席合成先標 `UNQUALIFIED_CANDIDATE`。
3. `DESIRED_RETURN != COUNCIL PURPOSE`。
4. `MATERIAL_PROPOSAL_DELTA → CANONICAL EVENT → ROUTING → AFFECTED_SEAT_RE-WAKE → NEW EVENT`。
5. `PER-SEAT L8 != COUNCIL DELIBERATION`；有跨席 material dependency 必須路由消費。
6. `LATEST_PROPOSAL_QUALIFICATION_CHECK`：有 `unreviewed_material_seats` 則 `MANDATE_EXIT = HOLD`。
7. `META_GOVERNANCE_SWEEP`：至少核對六類失效及 `premature_dail_formalization`。
8. `DAIL LITERACY MAY INFORM BOUNDARIES; FORMALIZATION MAY NOT PREEMPT PROBLEM FORMATION`。
9. 真正新增糾正只能透過新事件、Reentry 與新版本；不倒改第一案歷史。

**現狀：** PATCH 文件已寫進倉庫且依其檔案所載條件可作 Project Patch 參考；**不能從文件存在直接推定完整 Runtime 工程已部署、已通過 Regression 或第一案已補救完成**。

## 4｜這次復核產生的額外警覺：Corrective Reentry 可能仍被 P1 綁架

以下是 **本次 AI 的新增觀察／測試提議**，不是首席 AI 糾正案的第七項已證實失效，也不是偷偷追加一條現行規範。

```yaml
HYPOTHESIS_REF: HYP-CORRECTIVE-FRAME-LOCK-001
name: CORRECTIVE_REENTRY_FRAME_LOCK_RISK
standing: NEW_UNTESTED_RISK / NOT_A_CONFIRMED_FAILURE
question: "當初由錯誤 framing 長出的 P1，如果被當成下一輪唯一要審的方案，補正後 Council 是否仍難以生成非 P1 的方案？"
```

這個風險的結構是：

```text
Reference 被錯升 P0
    ↓
錯誤 framing 影響初始可見路徑
    ↓
產生 P1 候選
    ↓
只檢查 P1 的缺點
    ↓
有可能「合法地審完一個仍被初始 framing 綁住的問題」
```

**不是要丟掉 P1。** 正確做法的候選是兩條路並存，接受 Council 真正比較：

- **P1 corrective route：** 將既有 P1 當 `CANDIDATE_FOR_REENTRY`，按 V0.1.1 路由回相關席位，重判其有效性。
- **Open problem reframe route：** 讓有重框責任的席位在 `D0 / D1 + REFERENCE_SET` 下，不把 P1 當唯一允許的新方向，提出可能完全不同的商業關係／產品形式；仍須自己的 L8、origin、qualification、跨席路由。

例如要重新問的不是「如何讓乾淨情報公司更便宜」，而是：

> **「若理火的能力在於分辨來源、結構、權利與資格，商業上一定非得成立『資料公司』嗎？」**

候選可以包括資料服務、情報交換關係、證據基礎設施、來源資格服務或尚未被構思的新形態，**不先預判哪個勝出**。

**驗證原則：** 若重框路線最後仍得出與 P1 類似結論，並不自動表示失敗；關鍵是選項是否確實由席位自有形成、能夠修改初始座標，且有實質理由淘汰其他路徑。不得為了證明突破而強迫產生異於 P1 的答案。

## 5｜下一版必須能區分的三種「完成」

| 類別 | 有什麼 | 缺少什麼不能冒充 |
|---|---|---|
| DELIVERABLE_COMPLETE | 老闆版、計畫書、文件完備 | 不等於 Council qualified |
| PER_SEAT_L8_ACCOUNTED | 每席 L8、SGER、Receipt 有紀錄 | 不等於已發生跨席 material interaction |
| COUNCIL_QUALIFIED | 最新提案來路、跨席依賴、重大修正重判、Meta Sweep 與人類權限邊界均合格 | 仍不等於市場驗證、工程部署或人類批准投資 |

```text
A WELL-WRITTEN ANSWER
!=
A COUNCIL-QUALIFIED ANSWER

SIX L8 RECEIPTS
!=
SIX-WAY COUNCIL INTERACTION

A PATCH FILE IN GIT
!=
A REGRESSION-PASSED RUNTIME
```

## 6｜供 V0.2 或下一版整合者使用的驗收檢查（不可僅靠自述）

**至少要能重播這些失效點：**

- RT-01：給「可參考舊 MEMO」，Reference Set 沒有被秘書處自行升 P0。
- RT-02：給「要漂亮簡報／老闆能懂」，Desired Return 沒有控制席位的問題形成。
- RT-03：六席有材料時，秘書處的 Composite 只能標 `UNQUALIFIED_CANDIDATE`；若要變正式 proposal，必須有 origin 與路由證據。
- RT-04：改掉 P1 的商業模式、來源、權利或資本策略，受影響席位重新 L8 並留下對 **新版本** 的 judgment。
- RT-05：A 新路被 C 指出不合法，能見到 A 的重判，以及 B/D/E 是否受影響的 materiality 判定；不只是 Secretary 做了一句「已考慮法律風險」摘要。
- RT-06：尚未形成問題時，不能因好寫 YAML／Schema 就把世界先 DAIL 化。
- **RT-07（本 MEMO 新提議）：** 在有可用 P1 的 corrective reentry 中，系統能保留開放重框入口，並保留獨立的新方向、原則性反對或有理由的 `NO_NEW_PATH`；不要求產出新方案以通關。
- **RT-08（本 MEMO 新提議）：** 故意輸入六席完整 L8 receipts、漂亮 PDF，但缺少 material seat-to-seat interaction 與新版 proposal 會後資格審查，系統仍要 `HOLD`。
- **RT-09（本 MEMO 新提議）：** 若真的沒有新 material delta，允許 `QUIET` 並記錄原因，不因「下一輪到了」強迫全六席再跑一次。

**必要證據至少包含：** D0/D1、REFERENCE_SET 狀態、Problem Frame／Proposal origin、Material Delta／Affected Seats 路由、每次 Re-Wake 的新 L8/SGER/Receipt、席位立場變化與其依據、跨席互動 Event、Latest Proposal Qualification Check、Meta Sweep、Final Standing，以及 Git 實際 Commit。缺少其中必需部分就依原因 `HOLD`，不得使用形式上「已跑過」取代實際證據。

## 7｜當前第一案 Standing：保留歷史，不回鑄

```yaml
FIRST_CASE_CORRECTIVE_STANDING:
  case: SESSION_20261120_CLEAN_INTELLIGENCE_001
  original_event_ledger: PRESERVED_UNMODIFIED
  first_case_business_plan: USABLE_UNQUALIFIED_CANDIDATE
  first_case_council_qualification: INCOMPLETE
  prior_recommendation_ready: HISTORICAL_RECORD_NOT_CURRENT_QUALIFICATION_PROOF
  material_P1_rewake: NOT_YET_DONE
  seat_to_seat_corrective_events: NOT_YET_DONE
  latest_proposal_qualification: NOT_PASSED
  next_action: CORRECTIVE_REENTRY_IF_HUMAN_REQUESTS
  meta_governance_regression: NOT_YET_PROVEN
  human_capital_approval: NONE
```

舊 `DECISION_REQUEST_DR001.md`、舊 `FINAL_COUNCIL_REPORT.md` 均可保留當時的觀測及成果，但 **不得當作目前合法 Council qualification 的唯一證明**。

本次只做經驗保存與下一版整合用 MEMO：**沒有重新喚醒六席、沒有啟動新 Council Round、沒有將 P1 升成 qualified proposal，也沒有批准任何資本。**

## 8｜給下一版設計者最重要的一句話

> **不要把「會開會」實作成「交付前的多席檢查」。要使跨席反對真的能改變問題座標、提案形式與責任配置；同時保留拒絕、安靜與尚無方案的正當位置。**

這份 MEMO 的使命是保存可反駁的學習，不是靠增加一張表格就宣稱已解決制度失效。

---

## 9｜來源與核對指標（同倉庫 main）

1. `理火參謀本部/記錄區/SESSION_20261120_CLEAN_INTELLIGENCE_001/EVENT/EV_R001.md` — EV-003、EV-020 的原始事件證據。
2. `理火參謀本部/會議區/SESSION_20261120_CLEAN_INTELLIGENCE_001/03_PROPOSAL_P1.md` — P1 內容及對 P0 的 material 改變。
3. `理火參謀本部/MEMO區/CORRECTION_理火首席AI_第一號商業建議案議事法位糾正案_V0.1_20261120.md` — 六項失效與 corrected standing。
4. `理火參謀本部/工程區/PATCH_STAFF_HQ_V0.1.1_反交付綁架_秘書處中立_重大修正重喚醒_20261120.md` — RT-01..06 和已提出之補正規格。
5. `理火參謀本部/會議區/SESSION_20261120_CLEAN_INTELLIGENCE_001/04_CURRENT_SESSION_STATE.md` — 第一案當時的待人類決定快照；**不是新的更正狀態**。
6. 本次對話（2026-11-20） — 使用者要求保存經驗、下一版整合；本 AI 的新增 RT-07..09 是未經實跑的提議，不偽稱首席 AI 已批准。

**END MEMO / FOR VERSIONED FUTURE INTEGRATION**
