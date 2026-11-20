# MEMO｜Professional Trigger → Method Routing → Professional Support Request
## 最小外掛專業人員／學科心法路由候選 V0.1

**Date:** 2026-11-20
**Origin:** CASE-002 POSTHOC Method Audit / METHOD_ROUTING_NEGATIVE_SPECIMEN_001
**Standing:** `WORKING_CANDIDATE / NOT_RATIFIED / NOT_RUNTIME / NOT_DEPLOYED`
**Override:** NONE. Does not overwrite Staff-HQ V0.2, existing Project-only PATCH, LIHUOOS or Protocol. Not authorization to call real external professionals/spend money/release data.

## 1｜最小問題
CORE-6 有穩定**責任**，不是全學科全資料全專業的容器。現有心法目錄提供學科第一觀察、版本、調用總閘門；現有 Vertical 允許 CORE Seat 提 Consult Request；但 CASE-002 未留下每一個 Material Professional Gap 的選擇／不選擇依據。

**目標不是新設常駐第七席，而是把「問題是否需要外援」變成一個很輕的、可查的責任關係。**

```text
CORE-6 = PERMANENT RESPONSIBILITY OWNERS
METHOD PACK = VERSIONED FIRST-OBSERVATION LENS
EXTERNAL SOURCE = PROVENANCE-TIED EVIDENCE
PROFESSIONAL AGENT = TEMPORARY SCOPED SPECIALIST/EXPERT SUPPORT
STAFF STANCE = ONLY CORE SEAT CAN OWN ITS RESPONSE
```

## 2｜可觸發的最小關係

```text
MATERIAL ISSUE DETECTED
 ↓
SEAT IDENTIFIES PROFESSIONAL GAP (or reasoned NO_SUPPORT)
 ↓
PROFESSIONAL_SUPPORT_REQUEST [only if material gain plausible]
 ↓
SECRETARIAT ROUTES / AUTHORITY CHECK
 ↓
SELECT METHOD PACK or SOURCE or SCOPED PROFESSIONAL AGENT
 ↓
LOCK scope + source/method/agent version + owner + constraints
 ↓
SPECIALIST RETURN as scoped material (if actual specialist called)
 ↓
ADMISSION / MATERIALITY CHECK
 ↓
AFFECTED CORE SEAT CONSUMES
 ↓
OWNED SEAT RESPONSE: CHANGE / RETAIN_WITH_REASON / CHALLENGE / HOLD
```

**METHOD_PACK alone is not automatically a Professional Agent**. A seat may load the Method and form own judgment without external invocation; an external source search may supply evidence without either Method or Agent.

## 3｜Material Professional Gap 判定（不是關鍵字觸發）
一個問題可考慮調用支援，若有下列特徵之一**且**支援可能實質改變第一觀察、證據資格、重要風險或可執行界線：

- 法律權利、專業法域及交易許可將決定某方案能否合法存在或被准出。
- 學科 Method 可能使第一個問題單位由「使用者數量」改成「平台擴散分配」等新的因果座標。
- CORE Seat 已遇到與其責任有關、無法由既有 qualified source 解決的 MATERIAL UNKNOWN。
- 缺少專門的工程、安全、統計、金融、社會調查能力，使當前判斷可能發生實質誤差。
- 一個重大 objection 需要可查的外部法源、方法或有專業資格的持有人才能被解答。

**必要防劇場檢查：** `WOULD_THIS_SUPPORT_CHANGE_THE_FIRST_OBSERVATION_OR_QUALIFICATION?`；`CAN_WE_NAME_THE_DECISION_OR_PREMISE_AT_RISK?`；`IS_THERE_AN_EXISTING_QUALIFIED_INPUT_SUFFICIENT_FOR_THIS_STAGE?`

若只是提到法律/價格/APP，但目前只需一般概念定位且沒有 material delta，允許 `NOT_REQUIRED_WITH_REASON`，不產生任何 Agent call。

## 4｜最小支援梯度（不追求一次全開）

| Level | 最小支援 | 適用 | 需要的真實證據 |
|---|---|---|---|
| L0 | `NO_SUPPORT_REQUIRED_WITH_REASON` | 常識／現有資料已足夠支撐當輪限定問題；下一階段風險另列 | Seat own reason + material scope |
| L1 | Git `METHOD_PACK` 精確調閱 | 某學科第一觀察可能改變問題地形；不要求專家身份 | Method 文件路徑 + ref + blob SHA/version + selected lens + reason |
| L2 | `EXTERNAL_SOURCE_RETRIEVAL` | 缺最新官方法源、資料或研究依據，可由當前工具查核 | Source URL, fetch/verification time, relevance, limitations |
| L3 | `SCOPED_PROFESSIONAL_AGENT` | 需要特定技能形成獨立範圍分析；工具與授權允許 | identity, provider, model/professional standing, task scope, version, limits, return ref |
| L4 | `HUMAN/LICENSED_SPECIALIST_DECISION` | 真正法律意見、付費專業委託、外部資料披露等需要權限 | qualified owner authorization, privacy/budget/contract scope; no autonomous assumption |

L1 與 L2 可並用或不按序發生；L3/L4 不是「越高越好」，也不能以同模型模擬外部 Agent 來冒稱有獨立專業驗證。

## 5｜最小請求 schema（WORKING，不是已註冊 canonical schema）

```yaml
PROFESSIONAL_SUPPORT_REQUEST_CANDIDATE:
  request_id: PSR-CI3-EXAMPLE-001
  origin_seat: C
  source_issue_event_ref: MATERIAL_ISSUE_REF
  why_material: "某候選激勵合同的合法性決定能否對外上線"
  unresolved_professional_question: "實際 compensation tree 是否觸及 PRC 禁止傳銷類別？"
  support_intent: [FIRST_OBSERVATION,LEGAL_SOURCE_VERIFICATION]
  method_candidates:
    - path: "理火參謀本部/心法區/學科心法總目錄_V0.2.C_第三組_法學整合版.md"
      lens: "jurisdiction/procedure/evidence/referral_gate"
  minimal_expected_return: "法學觀察單位/可查法源/必須另尋執業者之界線"
  confidentiality: NO_CLIENT_PRIVATE_DATA
  provisional_standing: REQUESTED_NOT_APPROVED
```

```yaml
SECRETARIAT_ROUTING_DECISION_CANDIDATE:
  request_id: PSR-CI3-EXAMPLE-001
  route: METHOD_PACK_ONLY | SOURCE_RETRIEVAL | AGENT | REFER_QUALIFICATION_OWNER | NO_SUPPORT_WITH_REASON
  method_file_ref: null
  method_version_or_blob_sha: null
  actual_provider_id: null
  approval_basis: "within existing delegated scope, else request authorized human/owner"
  external_disclosure: NONE_UNLESS_AUTHORIZED
  conflict_of_interest_screen: PENDING_IF_RELEVANT
  route_status: CANDIDATE_ONLY
```

```yaml
SPECIALIST_RETURN_CANDIDATE:
  request_id: PSR-CI3-EXAMPLE-001
  origin_actor: ACTUAL_SPECIALIST_OR_PROVIDER_IF_CALLED
  material_type: EVIDENCE | METHOD_SHAPED_ANALYSIS | EXPERT_OPINION
  scope_and_version: REQUIRED
  provenance_and_limits: REQUIRED
  professional_verification: DECLARED_VERIFIABLE_LEVEL
  not_council_stance: true
```

```yaml
CORE_SEAT_CONSUMPTION_CANDIDATE:
  affected_seat: C
  request_id: PSR-CI3-EXAMPLE-001
  exact_return_ref: NONE_UNTIL_RETURN
  material_delta: TO_BE_DETERMINED
  own_l8_receipt: REQUIRED_IF_MATERIAL_JUDGMENT
  owned_response: CHANGE | RETAIN_WITH_REASON | CHALLENGE | HOLD
  secretary_may_not_assign_owned_stance: true
```

These are **illustrative candidate object shapes**. They are not actual CASE-002 records, not a live request, and not yet formal Canonical Event types. Real routing requires admission under then-current host and Staff-HQ source governance.

## 6｜秘書處與席位的權限，不偷改原制度
1. **CORE Seat** owns the material gap, question, demand for support and eventual judgment. May initiate `PROFESSIONAL_SUPPORT_REQUEST` (prior V0.1 Vertical expressly permits Consult Request); can also own `NOT_REQUIRED_WITH_REASON`. A support return cannot overwrite the seat.
2. **Secretariat** may **detect procedural omissions and ask the seat to decide**, route and record the selected Method/source/expert request, lock versions and remit results. Secretary cannot use "method selection" to pick the future Council thesis or force a particular school conclusion.
3. **Method Pack selection** should normally be proposed by seat with an issue-specific first-observation hypothesis. Secretary may resolve repository paths/versions or identify a candidate where the seat has not named it, but must record the candidate as routing, not the seat's owned judgment.
4. **External Expert** may return evidence, method-shaped analysis or a scoped opinion; not automatically a valid legal opinion or independently licensed professional. A method-only assistant reusing the same ChatGPT model must be labeled `SAME_MODEL_SPECIALIST_REFERENCE` and not independent Agent.
5. **Approval**: Free, permitted reading of Git packs under current mandate may be routed procedurally; invoking a cost-bearing agent, hiring a professional, disclosing company/client data, externally committing to contracts or changing authority requires the actually delegated owner or explicit human approval. No broad automatic Secretariat hiring power follows from `SECRETARIAT ROUTES`.
6. **Council role**: Specialist never becomes automatic seventh CORE seat, has no standing vote, cannot close issue, change Proposal, claim Council Qualification or sign decisions. Seat consumes material and chooses change/retention.
7. **If no material improvement** after evaluation, record `NO_MATERIAL_PROFESSIONAL_GAP → NO_AGENT`; no staged calls just to prove the test worked.

## 7｜Minimal Method Selection Receipt (reason over elaborate forms)
When material, one readable line is enough if it identifies source issue, responsible Seat, why a particular lens changes first observation, method pathname + exact Git blob or version, and choice to load / not load. When actual expert involved, add identity, scope, origin, time, confidentiality, return and affected-seat consumption.

```text
PSR_ID | ISSUE | SEAT | GAP | METHOD/AGENT + VERSION | REASON
→ RETURN TYPE + REF | AFFECTED SEAT REF | OWNED RESPONSE
```

For NO_SUPPORT:
```text
ISSUE | SEAT | support=NOT_REQUIRED | reason=...
→ unknowns/residual=... | recheck trigger=...
```

## 8｜Non-goals / law of minimum repair
- No permanent professional seats, no agent marketplace, no all-discipline preloading.
- No mandatory professional invocation per keyword or per CORE seat.
- No claim method retrieval equals expert truth.
- No attempt to retrofit CASE-002 history.
- No new L8 module, OS change or V0.2 Runtime replacement.
- No real specialist call in this audit task (by human instruction: audit → gap → relation → test design).

**Next:** conduct one deliberately visible regression and record both successful material support and correct abstentions. Only then decide whether to promote this into a formally ratified V0.2.x PATCH.

**Seed:** `MATERIAL_OBJECTION + EXPECTED_METHOD_DELTA` → ask/select/lock → `RETURN_AS_MATERIAL` → seat owns new judgment. `ABSENT_MATERIAL_DELTA` → no Agent is a valid success.
