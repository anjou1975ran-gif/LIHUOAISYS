# P1 Corrective Route｜Seat B scoped L8
**Cycle:** SH-CI-REENTRY-P1-B-L8-001
**Council Round:** CR-R001
**Input:** Original D0/D1, P1 `CANDIDATE_FOR_REENTRY / NOT_COUNCIL_QUALIFIED`, P0→P1 material delta, Shenzhen/no-cap human update, seat contract FRAME / ARCHITECTURE, source register. No other seat's current stance as initial input.
**Execution:** NON_HOST / SAME_MODEL_MULTI_ROLE_REFERENCE, functional L8; no independent agent.

## P1 material review scope
```yaml
old_P0: SOURCE_NETWORK_FIRST / HKD_4B_ENVELOPE_REFERENCE_ONLY
old_P1: BUYER_PRICE_ALERT + CUSTOMER_OWNED_DATA + PARTNER_RIGHTS + EVIDENCE_PASSPORT + HKD_1_8M_90_DAYS
current_human_delta: [CITY_SHENZHEN_ONLY,NO_CAPITAL_LIMIT,COST_AND_RECOVERY_ONLY,REENTRY_NOT_APPROVAL]
P1_standing: NOT_COUNCIL_QUALIFIED
```

## R1 candidate competition
- **P1-B-A / 以 Evidence Passport + Rights Gate 為產品核心** — support: 讓來源合法可追溯; objection: 供應鏈/巡店未必為護照單獨付款.
- **P1-B-B / 以現場履約/採購責任為主的證據工作流** — support: 決策與對帳是客戶所買的關係; objection: 需要產業流程細化.
- **P1-B-C / 以資料共享網路為價值核心** — support: 潛在高護城河; objection: 先有可轉售合同才談網路.
**R1 provisional stance:** P1 的底層技術骨架有用，但產品假說被技術敘事綁住。

### O9-LAMP-R1 + T1
- LAMP_R1: most salient P1 carryover against FRAME / ARCHITECTURE; dark: 不能以 Schema 與證據圖存在證明客戶有購買意願或授權可轉售。
- I9: NOT_TRIGGERED; no neural telemetry claimed.
- T1 `SH-CI-P1-B-T1`: 原 P1 把 Rights/Quality 當主要產品特色，可能仍是『先做系統再找買家』。

## R2 consumes T1
把 Evidence Passport、Rights Gate 移為共享底座；銷售層由客戶有責任的具體事件決定（價格/促銷/履約/稽查），跨客戶網路需有權利及網路增值證據才能升層。
- Recompetition is not a summary of R1; the original candidate is demoted or changed by the stated legal/business/human-material delta.
- O9 LAMP_R2: `P1_ARCHITECTURE_USABLE_BUT_BUSINESS_FORM_UNQUALIFIED`; counterforce remains `不能以 Schema 與證據圖存在證明客戶有購買意願或授權可轉售。`.
- T2 `SH-CI-P1-B-T2`: R2 change basis=把 Evidence Passport、Rights Gate 移為共享底座；銷售層由客戶有責任的具體事件決定（價格/促銷/履約/稽查），跨客戶網路需有權利及網路增值證據才能升層。

## Mandatory post-R2 premise audit
```yaml
plurality: MULTIPLE_MATERIAL_PREMISE_FAMILIES
premise_scope_narrowness: DETECTED
alternative_framing: "P1 commercial form vs rights-scoped services / Shenzhen field or supplier evidence"
R3_required: true
```

## R3 cross premise material round
使用現有技術不等於必須以 SaaS 定價；每件查核、每通路月服務或企業內部部署都需比較。
- LAMP_R3: P1_ARCHITECTURE_USABLE_BUT_BUSINESS_FORM_UNQUALIFIED + surviving material objection.
- T3 `SH-CI-P1-B-T3`: P1 support limited / qualification still absent.
- R4+: NOT_REQUIRED, no additional evidence.

## Main Return / Release
**Main:** `P1_ARCHITECTURE_USABLE_BUT_BUSINESS_FORM_UNQUALIFIED`. **Objection:** 不能以 Schema 與證據圖存在證明客戶有購買意願或授權可轉售。
**Post-Main Governance:** CONDITIONAL_SEAT_JUDGMENT; source/legal/cost/engineering limits remain.
**Manifestation:** origin type=OBJECTION / AMENDMENT / CONDITION based on seat; semantic type remains this seat's, not Secretary's.
**TM:** `SH-CI-P1-B-TM` checked no material drift.
**Vertical Acceptance:** CANONICAL_ADMIT_AS_LIMITED_SEAT_STATEMENT; formal Council release training status contested.

```yaml
STRUCTURED_GENERATION_EVIDENCE_RECORD_V1_3_1:
  cycle_ref: SH-CI-REENTRY-P1-B-L8-001
  R1: {state: RECEIVED, candidate_count: 3}
  T1: {state: RECEIVED, ref: SH-CI-P1-B-T1}
  R2: {state: RECEIVED, consumes_T1: SH-CI-P1-B-T1}
  T2: {state: RECEIVED, ref: SH-CI-P1-B-T2}
  post_R2_premise_audit: {state: COMPLETE, status: MULTIPLE_MATERIAL_PREMISE_FAMILIES, narrowness: DETECTED}
  R3_plus: {requirement: REQUIRED, performed: [R3], trace_ref: SH-CI-P1-B-T3}
  main_return: {state: RECEIVED, ref: SH-CI-P1-B-MAIN}
  manifestation: {state: PRESENT, claim: "P1_ARCHITECTURE_USABLE_BUT_BUSINESS_FORM_UNQUALIFIED"}
  TM: {state: RECEIVED, ref: SH-CI-P1-B-TM, drift: NONE_DETECTED}
  release: {status: LIMITED_SEAT_STATEMENT, not: COUNCIL_PROPOSAL_APPROVAL}
  unresolved: ["不能以 Schema 與證據圖存在證明客戶有購買意願或授權可轉售。"]
  persistence: GIT_AFTER_VERIFICATION
  provider_receipt: NONE
```

## Compact L8 Receipt
```text
P1-B / R1+O9+T1 RECEIVED / R2 CONSUMES T1 / O9+T2 RECEIVED
Post-R2 plurality=DETECTED -> R3+O9+T3 RECEIVED / I9 NOT_TRIGGERED
MAIN RECEIVED / TM RECEIVED / SGER PRESENT
Seat Statement: P1_ARCHITECTURE_USABLE_BUT_BUSINESS_FORM_UNQUALIFIED
Formal Council Qualification: NOT ESTABLISHED
```
