# PATCH｜雙時序分流：PRE-OBSERVATION METHOD ROUTING × MID-DELIBERATION PROFESSIONAL CONSULT
**版本：** V0.1.1-WORKING  
**日期：** 2026-11-20  
**來源：** Human 轉交首席 AI 對 `MEMO_PROFESSIONAL_TRIGGER_METHOD_ROUTING_V0.1_WORKING_20261120.md` 的結構審計。  
**適用：** 下一次 `TEST_METHOD_ROUTING_001` 的設計修正候選；尚未啟動測試。  
**法位：** `WORKING_CANDIDATE / NOT_RATIFIED / NOT_RUNTIME / NOT_DEPLOYED`。  
**法源：** 心法區 README、《心法作為第一步》與 Staff-HQ CORE Seat/External Expert 邊界。  
**兼容：** 只糾正上一版 MEMO 將 Method 與 Expert 放入同一時序的問題。不得覆寫 LIHUOOS、Protocol、現行 Staff-HQ V0.2、GPT Project-only PATCH 或 CASE-002 歷史。

## 0｜糾正案：什麼時間點錯了？
V0.1 原路徑以「Material Issue → Seat 發現專業缺口 → Professional Support Request → Method/Source/Agent → Return → Seat Consumption」作為共同生命周期。這對議事中途的專業外援可成立，**但對心法是事後 review，不能聲稱是第一步**。

必須區分兩個事件時鐘：
- **CLOCK A：席位尚未形成該問題的第一個 Material Judgment。** 此時選擇 Method 會影響第一次看見的問題單位、盲點、證據與候選。
- **CLOCK B：席位已有 L8 / 議事中途，出現新的 Material Professional Gap。** 此時支援是增量材料，必須回到席位自行判斷。

```text
METHOD_PACK != PROFESSIONAL_AGENT
PRE-L8 METHOD SELECTION != POST-L8 EXPERT REVIEW
SEAT != METHOD != KNOWLEDGE != STANCE
EXPERT RETURN != COUNCIL STANCE
```

## A｜PRE-OBSERVATION METHOD ROUTING｜第一觀察之前
```text
HUMAN D0 / QUALIFIED D1 / ISSUE OR MANDATE CLASSIFICATION
→ SEAT RESPONSIBILITY MATCH
→ POSSIBLE METHOD DELTA SCREEN
→ METHOD PACK SELECT OR NO_METHOD_WITH_REASON
→ LOCK SELECTED METHOD PATH / VERSION / BLOB SHA / SCOPE
→ SEAT FIRST OBSERVATION
→ SEAT L8 R1/R2/R3+ (as applicable)
→ SEAT-OWNED STANCE / QUESTION / PATH / OBJECTION
→ COUNCIL EVENTS
```

### A.1 哪些算「pre」？
- Classification 和 responsibility match 是**程序性的入口辨識**，不應偷做完整實質分析；並不等於已完成 Seat 的第一個 Material Judgment。
- 該席的 `POSSIBLE_METHOD_DELTA_SCREEN` 是**形成判斷之前的簡短選擇**：某心法是否可能改變「第一眼看什麼」。不要求先寫 L8 結論，再回頭假裝選擇發生在前面。
- 初始 pass 只讓席位看 Human D0/D1、自己的 Seat Contract、Qualified Context/References/Unknowns 和路由所需目錄；**不要先餵其他席立場**。
- 選心法不等於由秘書處選立場。Seat 應提出/認領第一觀察理由；Secretary 可以調目錄、核版本與提供可用選項，但不能指派 substantive thesis。
- `NO_METHOD_WITH_REASON` 是合法結果；它與 `NO_PROFESSIONAL_AGENT` 是兩個不同的決定。

### A.2 最小 Selection Receipt（候選，不是現行 schema）
```yaml
PRE_OBSERVATION_METHOD_DECISION_CANDIDATE:
  issue_or_mandate_ref: REQUIRED
  seat_id: REQUIRED
  seat_contract_ref: REQUIRED
  pre_l8_timestamp_or_event_order: BEFORE_FIRST_MATERIAL_SEAT_CYCLE
  possible_method_delta: "改變哪個第一觀察單位/證據/盲點?"
  selection: METHOD_PACK | NO_METHOD_WITH_REASON
  selected_method_path: null
  selected_method_version_or_blob_sha: null
  selected_lens: null
  reason_and_rejected_alternatives: REQUIRED_BRIEF
  first_observation_ref: AFTER_SELECTION_ONLY
  status: WORKING_SCHEMA_CANDIDATE
```
不以「提到法律／價格」作固定映射。若無有意義的 method delta，可選 NO_METHOD。若無法取得指定心法來源，應標 `METHOD_UNAVAILABLE` 和回退界線，不冒稱已載入。

## B｜MID-DELIBERATION PROFESSIONAL CONSULT｜議事中途新缺口
```text
L8 / COUNCIL → NEW MATERIAL PROFESSIONAL GAP
→ AFFECTED CORE SEAT IDENTIFIES GAP
→ PROFESSIONAL_SUPPORT_REQUEST (if justified)
→ SECRETARIAT CHECKS AUTHORIZATION STATE
  AND ROUTES WITHIN DELEGATED SCOPE
  OR REFER TO AUTHORIZED OWNER / HUMAN
→ SCOPE / SOURCE / PROVIDER / VERSION LOCK
→ EXTERNAL SOURCE / SCOPED SPECIALIST / PROFESSIONAL AGENT
→ ACTUAL RETURN WITH PROVENANCE, LIMITS & STATUS
→ MATERIALITY CHECK
→ AFFECTED CORE SEAT CONSUMES
→ IF MATERIAL: NEW SEAT L8
→ SEAT OWNS CHANGE / RETAIN_WITH_REASON / CHALLENGE / HOLD
```

### B.1 何時真的請外援？
- **只有**新材料使既有判斷面臨實質缺口，且需要額外資料、專門分析或有資格人士的服務，才觸發 B。
- 專業 Agent 不是永久第七席，不投票、不持有 Proposal、不關 Issue、不修改 Seat Stance；回傳只可能是 scoped Evidence、Method-shaped analysis、Expert Opinion。
- 外部資料查核可按需發生，但即便是可信來源，也不自動等於 Method Pack，更不等於專家身份。
- 若議事中新出現的是**全新問題或重大 reframe**，它的受影響席位在**下一次 Material L8 之前**仍應重新評估 A 路由；不能先完成新 L8 再說是第一觀察。A 的「pre」是**相對於該次問題/材料的第一個實質判斷**，不是僅限整個 Session 的 R001。
- 若外援請求不成立，`PROFESSIONAL_SUPPORT_REQUEST = NOT_REQUIRED_WITH_REASON`，無實際 Agent Call；同樣要留下是否有未決專業依賴的理由。

### B.2 最小授權修字（必須精確）
```text
SECRETARIAT CHECKS AUTHORIZATION STATE
AND ROUTES WITHIN DELEGATED SCOPE
!= SECRETARIAT GRANTS AUTHORIZATION
```
- 秘書處可辨識議事程序缺口、核對既有授權狀態、調閱被允許的 Git Method/公開來源、登記/路由/回傳。
- 外部付費、聘請真人專家、敏感資料外發、對外簽約或需專有資格的行動若**無現成授權**，必須 `PENDING_AUTHORIZED_OWNER / HUMAN_ACTION_REQUIRED`；不得擅自批准、製造授權或假稱 Agent 回傳成功。
- `SECRETARIAT ROUTES != SECRETARIAT OWNS EXPERT THESIS`。

### B.3 最小 Consultation Receipt（候選）
```yaml
MID_DELIBERATION_SUPPORT_CANDIDATE:
  triggering_material_issue_ref: REQUIRED
  origin_seat: REQUIRED
  gap_why_material: REQUIRED
  support_question: REQUIRED
  support_level: L0_NO_SUPPORT | L2_SOURCE | L3_AGENT | L4_HUMAN_SPECIALIST
  authorization_state: AUTHORIZED_WITHIN_DELEGATION | PENDING_OWNER | NOT_ALLOWED
  delegated_scope_ref: REQUIRED_IF_AUTHORIZED
  specialist_or_source_version_ref: REQUIRED_IF_USED
  return_type: EVIDENCE | METHOD_SHAPED_ANALYSIS | EXPERT_OPINION | NO_RETURN
  actual_return_ref: REQUIRED_IF_RETURNED
  affected_seats: []
  seat_new_l8_ref: REQUIRED_IF_MATERIAL_CONSUMPTION
  final_stance_ref: SEAT_OWNED_ONLY
  status: WORKING_SCHEMA_CANDIDATE
```

## C｜保留 V0.1 的 L0–L4，**不把級別當單一路徑**
```text
L0  NO_METHOD / NO_SUPPORT WITH REASON（兩個獨立決定）
L1  METHOD PACK（通常 A，亦可在新 Issue 的新 L8 前選）
L2  EXTERNAL SOURCE（按需；不等於 Expert）
L3  SCOPED PROFESSIONAL AGENT（通常 B，必須有實際 provider/return）
L4  HUMAN / LICENSED SPECIALIST（需真正 owner 授權）
```
L1 的 Method Pack 是觀察姿勢；L2 是外部證據；L3/4 是專業外援/有資格專業服務。不能把選擇 L1 模擬成專業 Agent 回傳。

## D｜兩個負面反例與防劇場
1. **PRE-OBSERVATION MISORDERING：** R001 Seat 先完成完整觀察和 L8，再補 Law Pack 並標 PRE-L8 = FAIL。那是合法的 review，但不是心法作為第一步。
2. **CONSULTATION THEATER：** R003 出現一個專業名詞就硬叫某 Agent，但無 material unknown、無合法授權或無 Seat consumption = FAIL。
3. **NO_METHOD / NO_AGENT：** 常識或當前合格證據足夠且有理由 = 合法 PASS 候選；不因一席未調心法/未叫外援而判失敗。
4. **RETENTION AFTER EXPERT:** Expert Return 後受影響席位保留原立場，只要留下消費與理由也可能 PASS；不得強迫改判。

## E｜下一個 Live Regression 的唯一必要改動
同一個新 Session 中分別測：
- **TEST A / PRE-L8**：看席位能否在第一 Material L8 前，自行選/拒絕 Method，記錄版本與第一觀察變化；避免提前載入所有心法。
- **TEST B / MID-COUNCIL**：看新 Material Professional Gap 是否形成真正席位請求、秘書處在既有授權內路由／無授權就交回 owner、專業材料回傳並由原席位形成 Own Response。
- **Control**：至少一個有理由的 `NO_METHOD` 或 `NO_AGENT`；結果不要求七席、固定專家數或固定改判。
- **Partial PASS** 合法：A pass 但 B 沒有自然出現專業缺口 → B = `NOT_TRIGGERED`，不是假裝叫人以求滿分。

**Version attitude：** 這份是新的修正檔與新版本測試設計，不刪改 V0.1 的錯誤；亦不回寫 CASE-002。只有實測後才有資格討論是否正式提升 Runtime。

**核心區別：** 心法是「先戴什麼眼鏡」；專業 Agent 是「真正遇到自己不能負責的問題時，請誰提供可追溯的外援」。