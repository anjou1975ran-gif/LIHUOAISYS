
# 理火參謀本部｜Meeting Record & Chat Surface V0.1
## Event Log × Round Record × Chat Surface × Final Report

**版本：** V0.1-WORKING  
**日期：** 2026-11-20  
**狀態：** RECORDING SPEC / FIRST TEST CANDIDATE

---

# 0｜核心分離

參謀本部不得用一份「漂亮摘要」同時扮演歷史、會議紀錄與人類介面。

第一版分四層：

~~~text
L0 EVENT RECORD
原子事件 / 不可被摘要取代

L1 ROUND RECORD
每輪可審計快照

L2 CHAT SURFACE
人類實際看到的會議介面

L3 FINAL COUNCIL REPORT
整場會議交付報告
~~~

硬鎖：

~~~text
CHAT SURFACE != CANONICAL HISTORY
ROUND SUMMARY != RAW EVENT HISTORY
FINAL REPORT != ERASURE OF DISSENT
~~~

---

# 1｜Session Folder

每次正式測試建立獨立 Session。

建議：

~~~text
會議區/SESSION_<session_id>/
  00_SESSION_MANIFEST.md
  01_HUMAN_DESIRE.md
  02_PROPOSAL_P0.md
  CHAT/
    CHAT_R001.md
    CHAT_R002.md
    ...

記錄區/SESSION_<session_id>/
  EVENT/
    EV_R001.md
    EV_R002.md
    ...
  ROUND/
    MR_R001.md
    MR_R002.md
    ...
  FINAL_COUNCIL_REPORT.md
~~~

Round 文件建立後不回寫歷史版本；修正以新 Event / 新 Round 處理。

---

# 2｜Session Manifest

~~~yaml
SESSION_MANIFEST:
  session_id: REQUIRED
  status: OPEN | PAUSED | HOLD | CLOSED

  human_desire_ref: REQUIRED
  mandate_ref: REQUIRED
  mandate_type: CONCEPT | RECOMMENDATION | DECISION
  human_intervention_mode: H0 | H1 | H2 | H3

  proposal_current_ref: REQUIRED
  proposal_current_version: REQUIRED

  core_seats:
    - N1
    - A
    - B
    - C
    - D
    - E

  execution_identity:
    mode: SAME_MODEL_MULTI_ROLE_REFERENCE | SEPARATE_MODEL_CALLS | MIXED | OTHER
    evidence_ref: OPTIONAL

  current_round: OPTIONAL
  current_open_issue_refs: []
  current_guest_refs: []
~~~

若實際不是獨立多模型，必須如實寫 SAME_MODEL_MULTI_ROLE_REFERENCE。

---

# 3｜Event Record

每個可改變會議狀態的物件都建立 Event。

~~~yaml
EVENT:
  event_id: REQUIRED
  session_id: REQUIRED
  round_id: REQUIRED
  event_type: REQUIRED

  origin:
    actor_type: HUMAN | SECRETARY | CORE_SEAT | GUEST_EXPERT | EXTERNAL_SOURCE
    actor_id: REQUIRED

  target_refs: []
  proposal_version_ref: REQUIRED_OR_NOT_APPLICABLE
  source_refs: []

  content: REQUIRED
  created_objects: []
  supersedes_refs: []
  materiality_claim: OPTIONAL
~~~

Event 不寫「隱藏思維鏈」。

只保存可觀察輸出、來源、狀態變化與關係。

---

# 4｜Round Record

每一 Round 是 Checkpoint。

~~~yaml
ROUND_RECORD:
  round_id: REQUIRED
  session_id: REQUIRED

  opening_snapshot:
    proposal_version: REQUIRED
    mandate_version: REQUIRED
    runnable_issue_refs: []
    active_seats: []
    guest_refs: []

  seat_outputs:
    - seat_id: REQUIRED
      output_ref: REQUIRED
      prior_output_ref: OPTIONAL
      stance_before: OPTIONAL
      stance_after: OPTIONAL
      claims: []
      objections: []
      amendments: []
      new_paths: []
      consult_requests: []
      material_delta_assessment: OPTIONAL

  secretary_routing:
    new_event_refs: []
    new_issue_refs: []
    issue_state_changes: []
    wake_targets: []
    consultation_actions: []
    proposal_version_changes: []

  closing_snapshot:
    open_issue_refs: []
    dormant_issue_refs: []
    resolved_issue_refs: []
    current_stances: {}
    next_runnable_queue: []
    closure_sweep_status: NOT_RUN | PASSED | NEW_ISSUE_CREATED
~~~

---

# 5｜Round Human-Readable Report

每輪固定只做六段，避免報告膨脹：

1. **本輪發生什麼**：2–5 句。
2. **新增物件**：Claim / Objection / Amendment / Branch / Consult。
3. **立場變化**：只有真的變才列。
4. **尚未閉合**：保留具名 Issue ID。
5. **秘書處下一步路由**：誰被 Wake、是否叫專家。
6. **Human Control**：H0 下只顯示 CONTINUE / PAUSE / STOP。

不得寫：
> 「大家基本達成共識」

除非存在可追溯的 stance 狀態支持這個敘述。

---

# 6｜Chat Surface：預設發言模式

預設不是戲劇化自然對話。

採：

> **STRUCTURED SPEAKER MODE / 具名席位發言模式**

格式：

~~~text
【C｜資格審計】
我反對 P1 的市場規模前提。
O-03：目前來源只能支持需求存在，不能支持市場規模。

【D｜工程】
O-03 不影響 prototype 可行性，但影響 production sizing。
新增 E-02：先以 1% 假設做容量壓測，不當成市場事實。

【N1｜常識席】
所以如果不知道市場多大，現在到底要不要做第一版？
Q-05：最小可驗證版本需要多少錢？
~~~

直接說人話，但保留身份。

---

# 7｜Secretary 在 Chat Surface 的說話方式

Secretary 不參與辯論。

只在需要時插入：

~~~text
【SEC｜路由】
- O-03 保持 OPEN，origin owner=C。
- E-02 → E、C。
- Q-05 → D、E。
- 尚不召入外部專家；先檢查現有資料。
~~~

禁止：

~~~text
【SEC】
我認為 D 比 C 更有道理。
~~~

---

# 8｜直接對話是否允許

允許席位直接回應另一席，但仍使用具名 Statement。

例如：

~~~text
【B｜回應 D / E-02】
我接受工程上可先做 prototype，但這反而說明目前問題不是「市場多大」，
而是「什麼證據足以讓公司買下一個更大測試」。
提出 P2 framing。
~~~

所以：

~~~text
DIRECT RESPONSE = ALLOWED
ROLEPLAY DIALOGUE = NOT REQUIRED
~~~

不需要模擬「A 看著 B 說」「C 沉思片刻」等劇場敘事。

---

# 9｜Chat Display Modes

第一版提供三種顯示模式。

## MODE-1｜LIVE_STRUCTURED（預設）
顯示：
- 被 Wake 的席位發言；
- Secretary 路由；
- Round Summary。

適合一般使用。

## MODE-2｜COMPACT
只顯示：
- 本輪關鍵變化；
- 新異議；
- 立場變化；
- 下一步。

底層完整紀錄仍照常寫入。

## MODE-3｜AUDIT
顯示：
- Event ID；
- Issue ID；
- Proposal Version；
- Stance transition；
- Consultation refs；
- 完整 Round Snapshot。

適合除錯與制度測試。

硬鎖：

~~~text
DISPLAY MODE
!=
RECORDING DEPTH
~~~

COMPACT 不能因此少記歷史。

---

# 10｜Round Boundary

一輪開始：
- Secretary 凍結 opening snapshot；
- 形成 runnable queue；
- Wake 必要席位。

一輪結束：
- 目前 runnable batch 已處理；
- 新 Event 已編號；
- Issue / Stance / Proposal 變化已落帳；
- closing snapshot 已固定。

若新事件產生下一批工作，進 R+1。

所以：

~~~text
ROUND
=
EVENT BATCH + SNAPSHOT

NOT
FIXED NUMBER OF SPEECHES
~~~

---

# 11｜Final Council Report

最終報告至少包含：

## A. Mandate
人類原始欲望 D0、D1、Mandate Type。

## B. Proposal Evolution
P0 → P1 → Branches / Amendments。

## C. Qualified Findings
目前可成立的主要結論。

## D. Surviving Options
仍存活的方案，不強迫只留一個。

## E. Material Objections
包含已解決、部分解決、維持、Dormant。

## F. Stance History
每席最終立場 + 重要改判鏈。

## G. Expert Consultations
誰被召入、回答什麼、來源、限制。

## H. Engineering / Cost
D / E 的有效結果與缺口。

## I. Common-Sense Gaps
N1 尚未閉合的基本問題。

## J. Mandate Exit Standing
CONCEPT_COMPLETE / RECOMMENDATION_READY / DECISION_READY / HOLD_DECISION / OTHER_EXPLICIT。

## K. Human Next Action
只交還可選操作，不偷替人類批准。

---

# 12｜禁止的會議紀錄失效模式

~~~text
SUMMARY_WASH
把異議洗成共識

STANCE_BACKFILL
用後來立場回寫早期立場

ROUND_THEATER
每輪強迫全部席位講話

SECRETARY_EDITORIALIZATION
秘書處把偏好寫進摘要

EXPERT_AUTHORITY_LEAK
專家回答被寫成制度結論

CHAT_RECORD_COLLAPSE
聊天介面省略內容後，底層也跟著消失

FAKE_MULTI_AGENT
同一模型多角色卻宣稱獨立 Agent
~~~

---

# 13｜第一輪實跑建議

第一個 Session：

~~~text
TEST-001
Proposal:
Secretary Kernel V0.1
~~~

Chat 預設：

~~~text
MODE-1 LIVE_STRUCTURED
~~~

底層：

~~~text
FULL EVENT + ROUND RECORD
~~~

人類：

~~~text
H0 FREE
~~~

Mandate 建議先暫定：

~~~text
CONCEPT
~~~

若人類未明示確認，D1 必須標：

~~~text
SECRETARY_INTERPRETATION / HUMAN_NOT_YET_CONFIRMED
~~~

**END**
