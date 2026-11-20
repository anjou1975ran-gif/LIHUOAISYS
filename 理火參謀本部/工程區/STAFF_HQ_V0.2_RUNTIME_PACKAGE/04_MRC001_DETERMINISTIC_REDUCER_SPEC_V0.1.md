# MRC-001 DETERMINISTIC REDUCER SPEC V0.1
## Canonical Event → Council State｜重播規格

**版本：** V0.1-WORKING  
**日期：** 2026-11-20  
**法位：** REDUCER_SPEC / DETERMINISTIC_PROJECTION_ONLY / NOT_SEMANTIC_OWNER / NOT_IMPLEMENTED

---

# 0｜核心句

> **Reducer 的工作是重建已被 Canonical History 承認的狀態，不是替 Council 想答案。**

```text
SAME CANONICAL LOG
→
SAME REDUCED STATE
```

---

# 1｜Input

唯一 authoritative input：

```text
ORDERED CANONICAL EVENT LOG
+
STATIC QUALIFIED CONTRACTS
```

Static contracts：
- actor/authority bindings
- responsibility map
- valid lifecycle transitions
- qualified mandatory route rules
- project formal gates

Final Report、Round View、Chat View、Executive Brief 都不是 reducer source of truth。

---

# 2｜Replay Preconditions

Replay 前驗證：

1. event_id unique；
2. sequence_no monotonic；
3. every referenced object resolvable or explicitly EXTERNAL_PENDING；
4. origin actor/role binding exists；
5. proposal version lineage acyclic；
6. stance prior_ref acyclic；
7. material relation source event exists；
8. Human authorization refs must originate from Human-authorized source；
9. derived files not ingested as canonical events unless separately admitted。

Fail：

```text
REPLAY = HOLD_INVALID_CANONICAL_LOG
```

不得猜補。

---

# 3｜Reducer State Initialization

```yaml
INITIAL_STATE:
  session:
  mandate:
  problem_frame: NONE
  proposals: {}
  latest_proposal: NONE
  stances: {}
  issues: {}
  material_relations: {}
  routing_queue: []
  pending_wakes: []
  reviews: {}
  human_gate: NOT_REQUIRED
  qualification_blockers: []
  checkpoint: OPEN
  session_end: NONE
  persistence: UNKNOWN
```

---

# 4｜Event Application Order

每個 event 按 sequence_no：

```text
VALIDATE ORIGIN
→ APPLY OBJECT CREATION/UPDATE
→ APPLY VERSION LINEAGE
→ REGISTER MATERIALITY CLAIMS
→ REGISTER MATERIAL RELATIONS
→ PROJECT ROUTING REQUIREMENTS
→ APPLY SEAT CONSUMPTION/RESPONSE RECEIPTS
→ APPLY PROPOSAL REVIEW COVERAGE
→ APPLY ISSUE STANDING
→ APPLY HUMAN GATE
→ APPLY QUALIFICATION CHECK
→ APPLY CHECKPOINT / SESSION END
```

注意：

> ROUTING REQUIREMENT 可由已資格化規則投影；materiality 本身不可由 reducer 新創。

---

# 5｜Problem Frame Reduction

合法 transition：

```text
NONE
→ OPEN
→ CONTESTED
→ QUALIFIED_FOR_CURRENT_MANDATE
→ SUPERSEDED
```

Human-given 可：

```text
NONE → HUMAN_GIVEN
```

若 frame 被新 event supersede：
- 舊 frame 保留歷史；
- current_problem_frame_ref 指新 frame；
- 不刪前史。

---

# 6｜Proposal Reduction

建立 ProposalVersion 時：

- resolve origin event；
- set parent version；
- register material delta refs；
- determine affected-seat set only from qualified affected relations / mandatory map；
- if any affected seat pending review：

```text
standing = MATERIAL_REVIEW_PENDING
```

舊版：

```text
SUPERSEDED
```

但其 receipts / stances 不刪。

硬鎖：

```text
REVIEW OF P(n-1)
CANNOT
COUNT AS REVIEW OF P(n)
```

---

# 7｜Stance Reduction

每席 current stance：

```text
seat_current_stance[target]
=
LATEST VALID ORIGIN-OWNED STANCE EVENT
```

只有該 seat 或合法 Human override source 可建立該 seat substantive stance。

若 Secretary event 嘗試直接改別席 stance：

```text
VERTICAL_ACCEPTANCE = REJECTED
STATE NOT MUTATED
FAILURE EVENT MAY BE RECORDED
```

---

# 8｜MaterialRelation Reduction

Lifecycle：

```text
QUEUED
→ DELIVERED
→ CONSUMED
→ RESPONDED
→ CLOSED_FOR_VERSION
```

Reducer 只在看到對應 canonical receipt/event 時前進。

禁止：

```text
ROUTED
→ AUTO_CONSUMED

CONSUMED
→ AUTO_AGREED

RESPONDED
→ AUTO_CLOSED
```

CLOSED_FOR_VERSION 條件至少：
- target seat 已有 owned response；
- response explicitly references triggering relation/event；
- relation scope version 未被新的 material version supersede；
- no mandatory downstream relation remains unregistered。

---

# 9｜Routing Queue Projection

若已存在：

```text
MATERIAL_RELATION(state=QUEUED)
```

則：

```text
routing_queue += relation
pending_wakes += target_seat
```

若 relation 被 DELIVERED：
- routing_queue 移出；
- pending_wake 保留，直到 seat consumption / valid wake。

QUIET 合法條件：

```text
NO QUALIFIED PENDING MATERIAL RELATION
AND
NO MANDATORY VERSION REVIEW
```

---

# 10｜Exact-Version Review Coverage

對 latest proposal version：

```yaml
affected_seats:
reviewed_seats:
unreviewed_seats:
```

```text
unreviewed
=
affected - reviewed_exact_version
```

reviewed_exact_version 必須有：
- seat-origin response；
- proposal_version_ref exact match；
- Vertical Acceptance not rejected；
- required L8 receipt where material cognition required。

---

# 11｜Issue Reduction

Issue 不因 Final Report 未提而消失。

只有 canonical resolution event 可：

```text
OPEN → CONDITIONED
OPEN → HOLD
OPEN → RESOLVED_FOR_VERSION
OPEN → SUPERSEDED
```

若 Proposal Version supersedes issue context：
- issue 可 SUPERSEDED；
- 不可 silently delete。

---

# 12｜Qualification Projection

Qualification engine event 只可投影已存在 evidence。

Reducer 檢查：

```text
latest proposal exists?
all affected seats accounted?
any unconsumed material relation?
any unresolved mandatory issue?
meta-governance ref exists?
upper gate blockers?
human gate required?
```

合法結果：
- REVIEWED_CONDITIONALLY
- QUALIFIED
- HOLD

Reducer 不可自己決定 recommendation winner。

---

# 13｜Human Gate

```text
HUMAN_ACTION_REQUIRED
→ DECISION_REQUEST_REF REQUIRED
→ human_gate = WAITING
```

只有 explicit Human event 可：

```text
WAITING → SATISFIED
```

```text
CONTINUE
!=
AUTHORIZATION
```

---

# 14｜Checkpoint / Session End

```text
CHECKPOINT_ENDING
!=
SESSION_END
```

Session End 只接受 explicit terminal event。

若 HOLD：
- checkpoint 可 HOLD；
- session_end 預設 NONE，除非 End Policy + terminal event 合法成立。

---

# 15｜Replay Output

Replay 產生：
- CouncilState
- ReplayReceipt
- invariant violations
- unresolved refs
- divergence hash / state hash candidate

```yaml
ReplayReceipt:
  input_event_count:
  last_sequence_no:
  state_hash_candidate:
  invariant_violations: []
  unresolved_refs: []
  replay_standing: PASS|HOLD
```

State hash 只證明同一 normalized state representation；不證明語義真實。

---

# 16｜Determinism Property

同一：
- canonical event sequence
- static contracts
- reducer version

必須得到同一：
- proposal lineage
- stance refs
- relation states
- review coverage
- blockers
- checkpoint standing

若不同：

```text
MRC-001 FAIL
```

---

# 17｜Reference Specimen Replay Target

REFERENCE_SPECIMEN_001 最低應重建：

```text
P1 = CANDIDATE_FOR_REENTRY
OPEN ROUTE = P0_NONE
C/E → A material re-wake
A revision → C/B
C/A → B architecture revision
D/E/N1 → B
B → P2
P2 → ALL SIX EXACT-VERSION REVIEW
TRAINING GATE → HOLD
SESSION_END = NONE
```

不需要靠 V0.2 final report。

---

# 18｜Non-goals

Reducer 不：
- 呼叫模型形成新觀點；
- 推測 materiality；
- 修正法律問題；
- 自動生成 proposal；
- 自動投票；
- 自動 consensus；
- 自動 release。

**END**
