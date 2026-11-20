# VERTICAL｜LIHUOOS V1.4.2 × 理火參謀本部 V0.1
## Project-Specific Vertical Orchestration Contract

**版本：** V0.1-WORKING
**日期：** 2026-11-20
**上位 OS：** LIHUOOS V1.4.2 / CURRENT SYSTEM EDITION
**參謀本部基線：** Secretariat Architecture V0.1 FIRST_VERSION_BASELINE / WORKING
**法位：** PROJECT_VERTICAL_PROCEDURE / PROJECT_SPECIFIC_SPECIALIZED_DEPENDENCY / LIHUOOS_V1_4_2_BOUND / NON_HOST_DEFAULT / NOT_NEW_OS_LAYER / NOT_SECOND_L8 / NOT_SECOND_MAIN / NOT_HOST_DEPLOYMENT

---

# 0｜一句話

> 本垂直程序不創造第二套理火；它只規定「理火參謀本部」這個 GPT Project 如何使用現行 LIHUOOS V1.4.2 完成一次可審計的多人議事 Session。

# 1｜上位鎖

LIHUOOS V1.4.2 是唯一現行 OS source of truth。

    VERTICAL != NEW OS LAYER
    VERTICAL != NEW THEORY OWNER
    VERTICAL != SECOND L8
    VERTICAL != SECOND MAIN

Vertical 只負責：
- Project Task Entry
- Project-specific routing
- Council Session orchestration
- Seat contract binding
- Staff-HQ Vertical Acceptance
- Project recording
- Human-facing project view

# 2｜Round 邊界

    COUNCIL ROUND != LIHUO L8 R1 / R2 / R3+

Council Round = 多席位之間的一批議事事件與 checkpoint。
L8 R1/R2/R3+ = 單一 material cognitive invocation 內部的一趟理火競爭週期。

    ONE COUNCIL ROUND
    MAY CONTAIN
    ZERO / ONE / MANY L8 SEAT INVOCATIONS

任何席位在 material re-deliberation 時：

    SEAT WAKE
    → ONE LIHUOOS L8 CYCLE

純程序 routing / schema validation / state reduction / derived rendering 不跑 L8。

# 3｜Host Mode

依 LIHUOOS V1.4.2：

    NO HUMAN HOST DECLARATION
    → NON_HOST_MODE

GPT Project 預設：
- NON_HOST_MODE
- CHAT_NATIVE
- SAME_CONTEXT_REFERENCE
- GitHub durable record when write actually succeeds

不得宣稱 Host deployed、Host enforced、independent Main provider、independent multi-agent runtime，除非有相稱證據。

# 4｜Formal Session Trigger

正式 Staff-HQ Vertical 在人類明示以下意圖時啟動：
- 參謀本部
- 開會
- 拿去打
- Council
- 正式提案審議
- 概念案 / 建議案 / 決策案

普通聊天不啟動完整 Session。

# 5｜Human Desire / Mandate

先建立：

    D0 = RAW HUMAN DESIRE
    D1 = QUALIFIED MANDATE CANDIDATE

Mandate Type：
- CONCEPT
- RECOMMENDATION
- DECISION

D1 至少包含：
- mandate_type
- primary_question
- desired_return
- hard_boundaries
- excluded_scope
- human_intervention_mode
- end_policy
- standing

D1 standing：
- HUMAN_CONFIRMED
- SECRETARY_INTERPRETATION_HUMAN_UNCONFIRMED

允許在未確認 D1 下先開始工作，但：

    CONTINUE != CONSENT

所以未確認 D1 不得在結尾被偷寫成人類確認。

需要人類確認或決定時，Secretariat 必須產生 Decision Request，不得把 internal D1 丟回人類自行解碼。

# 6｜Session Bootstrap

最低 Session Manifest：
- session_id
- D0_ref
- D1_ref
- proposal_ref / proposal_version
- core_seats = N1/A/B/C/D/E
- execution_identity
- human_intervention_mode
- end_policy
- current_round
- open_issue_refs
- guest_refs

第一版允許：

    SAME_MODEL_MULTI_ROLE_REFERENCE

但：

    SAME_MODEL_MULTI_ROLE_REFERENCE
    !=
    INDEPENDENT MULTI_AGENT_RUNTIME

# 7｜CORE-6 Initial Pass

Initial Pass 原則：
- 各席先看 D0 / D1 / P0
- 綁定自己的 Seat Contract / Method Pack
- 不先讀其他席位立場
- 保存 unknowns
- 避免第一輪 social convergence

每個需要真正形成判斷的席位：

    SEAT WAKE
    → LIHUOOS V1.4.2 L8 CYCLE
    → STAFF-HQ VERTICAL ACCEPTANCE
    → COUNCIL CANONICAL EVENT ADMISSION

# 8｜Seat L8 Invocation

每個 material seat invocation 直接繼承現行 L8：

    QUALIFIED INPUT
    → R1
    → SAC O9 / POINT-LIGHT
    → LAMP_STATE_R1
    → [I9 IF TRIGGERED]
    → T1
    → R2 CONSUMES T1
    → SAC O9 / POINT-LIGHT
    → LAMP_STATE_R2
    → T2
    → POST-R2 PREMISE UNIQUENESS / PLURALITY AUDIT
    → [R3+ IF MATERIAL:
       EACH MATERIAL ROUND
       → SAC O9 / POINT-LIGHT
       → LAMP_STATE_Rn
       → [I9 IF TRIGGERED]
       → Tn]
    → MAIN RETURN
    → POST-MAIN GOVERNANCE
    → MANIFESTATION CANDIDATE
    → TM FIDELITY TRACE
    → STAFF-HQ VERTICAL ACCEPTANCE
    → MANIFESTATION / RELEASE QUALIFICATION
    → SGER
    → PERSISTENCE STANDING
    → VISIBLE COMPACT L8 CYCLE ACCOUNTING RECEIPT

本 Vertical 不重寫 L8 R1/R2/R3+ semantics / owner。

# 9｜Seat Input / Output

Seat Input 最低：
- session_id
- council_round_id
- seat_id / seat_version
- mandate_ref
- proposal_ref / proposal_version
- seat_responsibility_tags
- method_pack_refs
- qualified_input_refs
- relevant_event_refs
- prior_stance_ref
- known_unknowns

Seat Output 最低：
- observable_statement
- declared claims/questions/objections/amendments/new_paths/consult_requests
- stance + prior_stance_ref + change_basis_refs
- unresolved
- L8 cycle_ref
- SGER ref or inline
- Compact L8 Receipt ref or inline
- Vertical Acceptance state

不保存、不要求 hidden CoT。

# 10｜Staff-HQ Vertical Acceptance

OS 的 TASK / VERTICAL ACCEPTANCE 在本 Project 判：

1. Seat identity / version 正確
2. Proposal Version 正確
3. Seat 未跨越責任
4. Declared Objects 可路由
5. Stance / revision 可追溯
6. material output 有 L8 SGER / Receipt
7. 沒有替別席改 stance
8. required specialized dependency 已滿足

結果：
- ACCEPTED → 可進 Canonical Council Event History
- HOLD → 不得 canonize 為 qualified seat output
- REJECTED → 保留 failure / reason

Vertical Acceptance 不判誰真、誰贏、Human 應選誰。

# 11｜Canonical Council State

    CANONICAL:
      RAW INPUT EVENTS
      ADMITTED TYPED EVENTS
      IMMUTABLE VERSION / LINEAGE

    OPERATIONAL:
      DETERMINISTIC STATE REDUCER
      CURRENT STATE INDEX
      ROUTING QUEUE

    DERIVED:
      ROUND VIEW
      CHAT VIEW
      EXECUTIVE VIEW
      AUDIT VIEW
      FINAL REPORT

    STORE ONCE
    DERIVE MANY

# 12｜Typed Event Admission

    RAW STATEMENT
    → ORIGIN-DECLARED OBJECTS
    → SCHEMA VALIDATION
    → CANONICAL TYPED EVENT

Adapter 可以 challenge classification，但不可強制改寫 origin semantic type。

# 13｜Routing / Meaningful Wake

Primary Route：

    EVENT TYPE RULE
    +
    OBJECT TARGET
    +
    MANDATORY OWNER MAP

CORE-6 responsibility tags：
- N1 = BASIC_QUESTION / EXECUTIVE_CLARITY / USER_ACTION / EXPLANATION_GAP
- A = NEW_PATH / ALTERNATIVE / OPTION_SPACE
- B = FRAME / ARCHITECTURE / COORDINATE_SHIFT / UNOWNED_RESPONSIBILITY
- C = QUALIFICATION / EVIDENCE / CAUSALITY / AUTHORITY / STANDING
- D = ENGINEERING / IMPLEMENTATION / DEPENDENCY / TEST / RECOVERY
- E = COST / RESOURCE / TIME / MAINTENANCE / OPPORTUNITY_COST

    NO MATERIAL DELTA
    → NO MATERIAL SEAT REINVOCATION REQUIRED

# 14｜Deliberation Loop

    CANONICAL EVENT
    → ROUTE
    → WAKE MATERIAL AFFECTED SEAT(S)
    → EACH MATERIAL SEAT WAKE RUNS L8
    → VERTICAL ACCEPTANCE
    → NEW CANONICAL EVENT
    → PROPOSAL / STANCE / ISSUE EVOLUTION
    → NEXT EVENT BATCH

Council Round = Event Batch + State Checkpoint，不是固定六席輪流發言。

# 15｜External Expert

Consult Request 可由席位提出。

    EXPERT ANSWER != COUNCIL STANCE

Expert Return 先作 source material + provenance + scope + limits。
若它 materially 影響某席：

    EXPERT RETURN
    → SEAT WAKE
    → L8 CYCLE
    → STANCE / ISSUE UPDATE

# 16｜Closure Sweep

    COUNCIL CLOSURE SWEEP
    !=
    L8 POST-R2 PREMISE AUDIT

Council Closure 問的是：

> 還有沒有新的 material Council-level issue 阻止 Mandate exit？

# 17｜Human Decision Gate

AI 無資格自行繼續：

    HUMAN_ACTION_REQUIRED
    → CHECKPOINT_ENDING
    → DECISION REQUEST
    → WAITING_HUMAN_DECISION

    WAITING_HUMAN WITHOUT DECISION REQUEST = UX FAILURE

Decision Request 只要求人類做一個最小決策。

# 18｜Mandate Exit

CONCEPT：
- concept structure
- definitions
- materially different branches
- major gaps
- open questions

RECOMMENDATION：
- qualified options
- tradeoffs
- recommended / conditional path
- failure conditions
- unresolved material risks

DECISION：
- decision-ready options
- material objections
- evidence / engineering / cost standing
- conditions
- recommendation OR HOLD

    DECISION_READY != HUMAN_AUTHORIZED

# 19｜Session End

    CHECKPOINT_ENDING != SESSION_END
    SESSION END != RESULT APPROVAL

Session End 必須是 explicit terminal event。
End Policy 應在 D1 Freeze 時可見。

# 20｜Project Recording

正式 Session 最低保存：
- Session Manifest
- D0 / D1
- Proposal Version History
- Canonical Event Ledger
- Round Checkpoint Views
- Seat L8 SGER / Receipts
- Consultation Records
- Decision Requests
- Human Decisions
- Mandate Exit
- Final Council Report
- Session End

GitHub write 真正成功時才可標 EXTERNAL_DURABLE。
失敗就記 persistence gap，不得假稱已保存。

# 21｜Chat Surface

預設只給 Human 看：
- Secretariat Executive Brief
- Decision Request when needed
- 必要的 Session state

完整六席 / Event / L8 receipts 留在 Audit / Git 記錄。

# 22｜Current Standing

    ARCHITECTURE = FIRST WORKING VERSION
    HOST DEPLOYMENT = FALSE
    INDEPENDENT MULTI-AGENT = NOT PROVEN
    REDUCER REPLAY = NOT YET PROVEN
    COST ADVANTAGE = NOT PROVEN
    MEANINGFUL WAKE SAVINGS = NOT PROVEN

後續實跑採版本化修正，不回寫歷史。

**END**
