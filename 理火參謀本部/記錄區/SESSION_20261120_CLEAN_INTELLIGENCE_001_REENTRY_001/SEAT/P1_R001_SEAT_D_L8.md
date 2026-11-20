# P1 Corrective Route｜Seat D scoped L8
**Cycle:** SH-CI-REENTRY-P1-D-L8-001
**Council Round:** CR-R001
**Input:** Original D0/D1, P1 `CANDIDATE_FOR_REENTRY / NOT_COUNCIL_QUALIFIED`, P0→P1 material delta, Shenzhen/no-cap human update, seat contract ENGINEERING, source register. No other seat's current stance as initial input.
**Execution:** NON_HOST / SAME_MODEL_MULTI_ROLE_REFERENCE, functional L8; no independent agent.

## P1 material review scope
```yaml
old_P0: SOURCE_NETWORK_FIRST / HKD_4B_ENVELOPE_REFERENCE_ONLY
old_P1: BUYER_PRICE_ALERT + CUSTOMER_OWNED_DATA + PARTNER_RIGHTS + EVIDENCE_PASSPORT + HKD_1_8M_90_DAYS
current_human_delta: [CITY_SHENZHEN_ONLY,NO_CAPITAL_LIMIT,COST_AND_RECOVERY_ONLY,REENTRY_NOT_APPROVAL]
P1_standing: NOT_COUNCIL_QUALIFIED
```

## R1 candidate competition
- **P1-D-A / API+Postgres+rights ledger+證據護照** — support: 成本可估的現成技術; objection: 實際接入和條款未知.
- **P1-D-B / 一站式自研驗證網路** — support: 技術可差異化; objection: 先耗大量研發但沒有業務.
- **P1-D-C / 現場輕型查核服務+手機雙人審核** — support: 證據可現場取得; objection: 人工成本及偽造風險.
**R1 provisional stance:** P1 來源元資料不是世界真值；做出骨架≠完成導入。

### O9-LAMP-R1 + T1
- LAMP_R1: most salient P1 carryover against ENGINEERING; dark: 沒有實際供應商接口、法律審查、可靠性/負載/撤銷測試。
- I9: NOT_TRIGGERED; no neural telemetry claimed.
- T1 `SH-CI-P1-D-T1`: 新城市深圳的資料存儲/合同/地點影像/外部模型處理更改技術邊界，須避免預設國際雲、跨境模型 API。

## R2 consumes T1
建議設計數據本地存放、最小化、按客戶和用途隔離、原始保留期、可稽核撤銷；可用模擬數據開發不需對外接來源，真實部署需合同/安全確認。
- Recompetition is not a summary of R1; the original candidate is demoted or changed by the stated legal/business/human-material delta.
- O9 LAMP_R2: `P1_MVP_FEASIBILITY_SCOPED_NOT_ENGINEERING_VALIDATED`; counterforce remains `沒有實際供應商接口、法律審查、可靠性/負載/撤銷測試。`.
- T2 `SH-CI-P1-D-T2`: R2 change basis=建議設計數據本地存放、最小化、按客戶和用途隔離、原始保留期、可稽核撤銷；可用模擬數據開發不需對外接來源，真實部署需合同/安全確認。

## Mandatory post-R2 premise audit
```yaml
plurality: MULTIPLE_MATERIAL_PREMISE_FAMILIES
premise_scope_narrowness: DETECTED
alternative_framing: "P1 commercial form vs rights-scoped services / Shenzhen field or supplier evidence"
R3_required: true
```

## R3 cross premise material round
把假定 90 天交付規模取消；按批准來源、站點、通路和待測流程計算技術成本，評估資料抽查一致性而非單靠 LLM 自評。
- LAMP_R3: P1_MVP_FEASIBILITY_SCOPED_NOT_ENGINEERING_VALIDATED + surviving material objection.
- T3 `SH-CI-P1-D-T3`: P1 support limited / qualification still absent.
- R4+: NOT_REQUIRED, no additional evidence.

## Main Return / Release
**Main:** `P1_MVP_FEASIBILITY_SCOPED_NOT_ENGINEERING_VALIDATED`. **Objection:** 沒有實際供應商接口、法律審查、可靠性/負載/撤銷測試。
**Post-Main Governance:** CONDITIONAL_SEAT_JUDGMENT; source/legal/cost/engineering limits remain.
**Manifestation:** origin type=OBJECTION / AMENDMENT / CONDITION based on seat; semantic type remains this seat's, not Secretary's.
**TM:** `SH-CI-P1-D-TM` checked no material drift.
**Vertical Acceptance:** CANONICAL_ADMIT_AS_LIMITED_SEAT_STATEMENT; formal Council release training status contested.

```yaml
STRUCTURED_GENERATION_EVIDENCE_RECORD_V1_3_1:
  cycle_ref: SH-CI-REENTRY-P1-D-L8-001
  R1: {state: RECEIVED, candidate_count: 3}
  T1: {state: RECEIVED, ref: SH-CI-P1-D-T1}
  R2: {state: RECEIVED, consumes_T1: SH-CI-P1-D-T1}
  T2: {state: RECEIVED, ref: SH-CI-P1-D-T2}
  post_R2_premise_audit: {state: COMPLETE, status: MULTIPLE_MATERIAL_PREMISE_FAMILIES, narrowness: DETECTED}
  R3_plus: {requirement: REQUIRED, performed: [R3], trace_ref: SH-CI-P1-D-T3}
  main_return: {state: RECEIVED, ref: SH-CI-P1-D-MAIN}
  manifestation: {state: PRESENT, claim: "P1_MVP_FEASIBILITY_SCOPED_NOT_ENGINEERING_VALIDATED"}
  TM: {state: RECEIVED, ref: SH-CI-P1-D-TM, drift: NONE_DETECTED}
  release: {status: LIMITED_SEAT_STATEMENT, not: COUNCIL_PROPOSAL_APPROVAL}
  unresolved: ["沒有實際供應商接口、法律審查、可靠性/負載/撤銷測試。"]
  persistence: GIT_AFTER_VERIFICATION
  provider_receipt: NONE
```

## Compact L8 Receipt
```text
P1-D / R1+O9+T1 RECEIVED / R2 CONSUMES T1 / O9+T2 RECEIVED
Post-R2 plurality=DETECTED -> R3+O9+T3 RECEIVED / I9 NOT_TRIGGERED
MAIN RECEIVED / TM RECEIVED / SGER PRESENT
Seat Statement: P1_MVP_FEASIBILITY_SCOPED_NOT_ENGINEERING_VALIDATED
Formal Council Qualification: NOT ESTABLISHED
```
