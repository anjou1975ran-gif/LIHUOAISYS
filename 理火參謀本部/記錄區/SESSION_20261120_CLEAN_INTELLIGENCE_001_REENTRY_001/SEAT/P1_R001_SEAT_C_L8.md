# P1 Corrective Route｜Seat C scoped L8
**Cycle:** SH-CI-REENTRY-P1-C-L8-001
**Council Round:** CR-R001
**Input:** Original D0/D1, P1 `CANDIDATE_FOR_REENTRY / NOT_COUNCIL_QUALIFIED`, P0→P1 material delta, Shenzhen/no-cap human update, seat contract LEGAL / QUALIFICATION, source register. No other seat's current stance as initial input.
**Execution:** NON_HOST / SAME_MODEL_MULTI_ROLE_REFERENCE, functional L8; no independent agent.

## P1 material review scope
```yaml
old_P0: SOURCE_NETWORK_FIRST / HKD_4B_ENVELOPE_REFERENCE_ONLY
old_P1: BUYER_PRICE_ALERT + CUSTOMER_OWNED_DATA + PARTNER_RIGHTS + EVIDENCE_PASSPORT + HKD_1_8M_90_DAYS
current_human_delta: [CITY_SHENZHEN_ONLY,NO_CAPITAL_LIMIT,COST_AND_RECOVERY_ONLY,REENTRY_NOT_APPROVAL]
P1_standing: NOT_COUNCIL_QUALIFIED
```

## R1 candidate competition
- **P1-C-A / 已合作客戶 POS 資料做本客戶內部報告** — support: 較可約定處理目的; objection: 仍需合同和個資判斷.
- **P1-C-B / 商戶資料與競爭對手數據跨客戶轉售** — support: 可能有高價網路; objection: 目前沒有轉售授權及反不正當競爭評估.
- **P1-C-C / 有商戶明確許可的現場稽核** — support: 可收可查證的門店事件; objection: 現場拍攝/人員個資及授權範圍不明.
**R1 provisional stance:** P1 概念合法基礎是『可設計權利閘』，不是任何深圳商業資料已經合法取得。

### O9-LAMP-R1 + T1
- LAMP_R1: most salient P1 carryover against LEGAL / QUALIFICATION; dark: 無實際中國律師意見、來源授權/數據跨境評估；不准標 LEGAL_VALIDATED。
- I9: NOT_TRIGGERED; no neural telemetry claimed.
- T1 `SH-CI-P1-C-T1`: 新法域從原先未定城市變深圳，PRC 資料安全、個資、商業秘密和反不正當競爭須重新校正，不能引用台灣法作當地准出。

## R2 consumes T1
查 PRC PIPL、DSL、Network Data Regulation、2025 anti-unfair law 和 2026 trade secret rule；P1 的非個資與商業秘密是不同閘。平台店鋪看板報告的訪問權 ≠ 向第三方出售權。
- Recompetition is not a summary of R1; the original candidate is demoted or changed by the stated legal/business/human-material delta.
- O9 LAMP_R2: `P1_RIGHTS_RELEASE_HOLD_AND_SCOPE_TO_PR_CLAW`; counterforce remains `無實際中國律師意見、來源授權/數據跨境評估；不准標 LEGAL_VALIDATED。`.
- T2 `SH-CI-P1-C-T2`: R2 change basis=查 PRC PIPL、DSL、Network Data Regulation、2025 anti-unfair law 和 2026 trade secret rule；P1 的非個資與商業秘密是不同閘。平台店鋪看板報告的訪問權 ≠ 向第三方出售權。

## Mandatory post-R2 premise audit
```yaml
plurality: MULTIPLE_MATERIAL_PREMISE_FAMILIES
premise_scope_narrowness: DETECTED
alternative_framing: "P1 commercial form vs rights-scoped services / Shenzhen field or supplier evidence"
R3_required: true
```

## R3 cross premise material round
供應鏈價格/履約屬企業商業秘密高敏類；企業自有的來源不一定能授權給外部 LIHUO Core 作訓練。
- LAMP_R3: P1_RIGHTS_RELEASE_HOLD_AND_SCOPE_TO_PR_CLAW + surviving material objection.
- T3 `SH-CI-P1-C-T3`: P1 support limited / qualification still absent.
- R4+: NOT_REQUIRED, no additional evidence.

## Main Return / Release
**Main:** `P1_RIGHTS_RELEASE_HOLD_AND_SCOPE_TO_PR_CLAW`. **Objection:** 無實際中國律師意見、來源授權/數據跨境評估；不准標 LEGAL_VALIDATED。
**Post-Main Governance:** CONDITIONAL_SEAT_JUDGMENT; source/legal/cost/engineering limits remain.
**Manifestation:** origin type=OBJECTION / AMENDMENT / CONDITION based on seat; semantic type remains this seat's, not Secretary's.
**TM:** `SH-CI-P1-C-TM` checked no material drift.
**Vertical Acceptance:** CANONICAL_ADMIT_AS_LIMITED_SEAT_STATEMENT; formal Council release training status contested.

```yaml
STRUCTURED_GENERATION_EVIDENCE_RECORD_V1_3_1:
  cycle_ref: SH-CI-REENTRY-P1-C-L8-001
  R1: {state: RECEIVED, candidate_count: 3}
  T1: {state: RECEIVED, ref: SH-CI-P1-C-T1}
  R2: {state: RECEIVED, consumes_T1: SH-CI-P1-C-T1}
  T2: {state: RECEIVED, ref: SH-CI-P1-C-T2}
  post_R2_premise_audit: {state: COMPLETE, status: MULTIPLE_MATERIAL_PREMISE_FAMILIES, narrowness: DETECTED}
  R3_plus: {requirement: REQUIRED, performed: [R3], trace_ref: SH-CI-P1-C-T3}
  main_return: {state: RECEIVED, ref: SH-CI-P1-C-MAIN}
  manifestation: {state: PRESENT, claim: "P1_RIGHTS_RELEASE_HOLD_AND_SCOPE_TO_PR_CLAW"}
  TM: {state: RECEIVED, ref: SH-CI-P1-C-TM, drift: NONE_DETECTED}
  release: {status: LIMITED_SEAT_STATEMENT, not: COUNCIL_PROPOSAL_APPROVAL}
  unresolved: ["無實際中國律師意見、來源授權/數據跨境評估；不准標 LEGAL_VALIDATED。"]
  persistence: GIT_AFTER_VERIFICATION
  provider_receipt: NONE
```

## Compact L8 Receipt
```text
P1-C / R1+O9+T1 RECEIVED / R2 CONSUMES T1 / O9+T2 RECEIVED
Post-R2 plurality=DETECTED -> R3+O9+T3 RECEIVED / I9 NOT_TRIGGERED
MAIN RECEIVED / TM RECEIVED / SGER PRESENT
Seat Statement: P1_RIGHTS_RELEASE_HOLD_AND_SCOPE_TO_PR_CLAW
Formal Council Qualification: NOT ESTABLISHED
```
