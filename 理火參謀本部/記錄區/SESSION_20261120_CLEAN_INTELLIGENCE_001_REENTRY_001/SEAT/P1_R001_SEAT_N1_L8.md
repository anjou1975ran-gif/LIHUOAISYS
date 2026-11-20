# P1 Corrective Route｜Seat N1 scoped L8
**Cycle:** SH-CI-REENTRY-P1-N1-L8-001
**Council Round:** CR-R001
**Input:** Original D0/D1, P1 `CANDIDATE_FOR_REENTRY / NOT_COUNCIL_QUALIFIED`, P0→P1 material delta, Shenzhen/no-cap human update, seat contract BUYER/EXECUTIVE, source register. No other seat's current stance as initial input.
**Execution:** NON_HOST / SAME_MODEL_MULTI_ROLE_REFERENCE, functional L8; no independent agent.

## P1 material review scope
```yaml
old_P0: SOURCE_NETWORK_FIRST / HKD_4B_ENVELOPE_REFERENCE_ONLY
old_P1: BUYER_PRICE_ALERT + CUSTOMER_OWNED_DATA + PARTNER_RIGHTS + EVIDENCE_PASSPORT + HKD_1_8M_90_DAYS
current_human_delta: [CITY_SHENZHEN_ONLY,NO_CAPITAL_LIMIT,COST_AND_RECOVERY_ONLY,REENTRY_NOT_APPROVAL]
P1_standing: NOT_COUNCIL_QUALIFIED
```

## R1 candidate competition
- **P1-N1-A / 賣價格異動報告給所有深圳中型品牌** — support: 產品淺顯易懂; objection: 可能已有 BI 或電商平台報表.
- **P1-N1-B / 只針對有核查責任的門店巡檢主管提供證據服務** — support: 清晰節省核查工時與爭議; objection: P1 未指定這類買家.
- **P1-N1-C / 先只賣證據護照無主題** — support: 概念通用; objection: 無明確採購預算權人.
**R1 provisional stance:** P1 可以當原型，但不是已找到的深圳買家；原先品牌/經銷商假說過寬。

### O9-LAMP-R1 + T1
- LAMP_R1: most salient P1 carryover against BUYER/EXECUTIVE; dark: 沒有深圳企業採購預算責任人/購買承諾證據，P1 不能固定產品類型。
- I9: NOT_TRIGGERED; no neural telemetry claimed.
- T1 `SH-CI-P1-N1-T1`: 若 buyer 只關心能否降低損失而不關心原始價格來源技術，P1 產品/客戶匹配需重新定義。

## R2 consumes T1
把 P1 的『200 SKU、價格警報』改視為獨立於付費痛點的工程示例。客戶問題應先由渠道主管的返工/扣款/巡店成本和採購主管的報價爭議費用等可量化問題形成。
- Recompetition is not a summary of R1; the original candidate is demoted or changed by the stated legal/business/human-material delta.
- O9 LAMP_R2: `P1_BUYER_UNQUALIFIED_UNTIL_NAMED_PROBLEM`; counterforce remains `沒有深圳企業採購預算責任人/購買承諾證據，P1 不能固定產品類型。`.
- T2 `SH-CI-P1-N1-T2`: R2 change basis=把 P1 的『200 SKU、價格警報』改視為獨立於付費痛點的工程示例。客戶問題應先由渠道主管的返工/扣款/巡店成本和採購主管的報價爭議費用等可量化問題形成。

## Mandatory post-R2 premise audit
```yaml
plurality: MULTIPLE_MATERIAL_PREMISE_FAMILIES
premise_scope_narrowness: DETECTED
alternative_framing: "P1 commercial form vs rights-scoped services / Shenzhen field or supplier evidence"
R3_required: true
```

## R3 cross premise material round
地理集中深圳有利於測量門店訪查及城市線下成本；單城限制不保證通路資料開放。
- LAMP_R3: P1_BUYER_UNQUALIFIED_UNTIL_NAMED_PROBLEM + surviving material objection.
- T3 `SH-CI-P1-N1-T3`: P1 support limited / qualification still absent.
- R4+: NOT_REQUIRED, no additional evidence.

## Main Return / Release
**Main:** `P1_BUYER_UNQUALIFIED_UNTIL_NAMED_PROBLEM`. **Objection:** 沒有深圳企業採購預算責任人/購買承諾證據，P1 不能固定產品類型。
**Post-Main Governance:** CONDITIONAL_SEAT_JUDGMENT; source/legal/cost/engineering limits remain.
**Manifestation:** origin type=OBJECTION / AMENDMENT / CONDITION based on seat; semantic type remains this seat's, not Secretary's.
**TM:** `SH-CI-P1-N1-TM` checked no material drift.
**Vertical Acceptance:** CANONICAL_ADMIT_AS_LIMITED_SEAT_STATEMENT; formal Council release training status contested.

```yaml
STRUCTURED_GENERATION_EVIDENCE_RECORD_V1_3_1:
  cycle_ref: SH-CI-REENTRY-P1-N1-L8-001
  R1: {state: RECEIVED, candidate_count: 3}
  T1: {state: RECEIVED, ref: SH-CI-P1-N1-T1}
  R2: {state: RECEIVED, consumes_T1: SH-CI-P1-N1-T1}
  T2: {state: RECEIVED, ref: SH-CI-P1-N1-T2}
  post_R2_premise_audit: {state: COMPLETE, status: MULTIPLE_MATERIAL_PREMISE_FAMILIES, narrowness: DETECTED}
  R3_plus: {requirement: REQUIRED, performed: [R3], trace_ref: SH-CI-P1-N1-T3}
  main_return: {state: RECEIVED, ref: SH-CI-P1-N1-MAIN}
  manifestation: {state: PRESENT, claim: "P1_BUYER_UNQUALIFIED_UNTIL_NAMED_PROBLEM"}
  TM: {state: RECEIVED, ref: SH-CI-P1-N1-TM, drift: NONE_DETECTED}
  release: {status: LIMITED_SEAT_STATEMENT, not: COUNCIL_PROPOSAL_APPROVAL}
  unresolved: ["沒有深圳企業採購預算責任人/購買承諾證據，P1 不能固定產品類型。"]
  persistence: GIT_AFTER_VERIFICATION
  provider_receipt: NONE
```

## Compact L8 Receipt
```text
P1-N1 / R1+O9+T1 RECEIVED / R2 CONSUMES T1 / O9+T2 RECEIVED
Post-R2 plurality=DETECTED -> R3+O9+T3 RECEIVED / I9 NOT_TRIGGERED
MAIN RECEIVED / TM RECEIVED / SGER PRESENT
Seat Statement: P1_BUYER_UNQUALIFIED_UNTIL_NAMED_PROBLEM
Formal Council Qualification: NOT ESTABLISHED
```
