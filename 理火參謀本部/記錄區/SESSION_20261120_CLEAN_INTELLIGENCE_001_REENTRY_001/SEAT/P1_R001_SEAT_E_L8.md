# P1 Corrective Route｜Seat E scoped L8
**Cycle:** SH-CI-REENTRY-P1-E-L8-001
**Council Round:** CR-R001
**Input:** Original D0/D1, P1 `CANDIDATE_FOR_REENTRY / NOT_COUNCIL_QUALIFIED`, P0→P1 material delta, Shenzhen/no-cap human update, seat contract COST / RESOURCE, source register. No other seat's current stance as initial input.
**Execution:** NON_HOST / SAME_MODEL_MULTI_ROLE_REFERENCE, functional L8; no independent agent.

## P1 material review scope
```yaml
old_P0: SOURCE_NETWORK_FIRST / HKD_4B_ENVELOPE_REFERENCE_ONLY
old_P1: BUYER_PRICE_ALERT + CUSTOMER_OWNED_DATA + PARTNER_RIGHTS + EVIDENCE_PASSPORT + HKD_1_8M_90_DAYS
current_human_delta: [CITY_SHENZHEN_ONLY,NO_CAPITAL_LIMIT,COST_AND_RECOVERY_ONLY,REENTRY_NOT_APPROVAL]
P1_standing: NOT_COUNCIL_QUALIFIED
```

## R1 candidate competition
- **P1-E-A / 依原 P1 HKD1.8M/90d 上限** — support: 利於管支出; objection: 人類明確不再設上限/下限.
- **P1-E-B / 每客利潤與可回收固定投入判斷** — support: 符合當輪授權; objection: 成本及售價皆須客戶報價.
- **P1-E-C / 低成本 SaaS 一定比場域採集好** — support: 看似風險低; objection: 未考慮更高定價和渠道自有網路.
**R1 provisional stance:** 直接反對 P1 的固定 HKD1.8M/90 天約束；人類改為以 cost/payback 驗證。

### O9-LAMP-R1 + T1
- LAMP_R1: most salient P1 carryover against COST / RESOURCE; dark: 無正式價格報價、CAC、實際續約、工時或回款資料；現在不能做確定 payback 年數。
- I9: NOT_TRIGGERED; no neural telemetry claimed.
- T1 `SH-CI-P1-E-T1`: 若仍用原預算當作入選條件，就算 180 萬內實現也不一定能盈利；反而拒絕可回收的高投入場景。

## R2 consumes T1
重建成本模型：每客實收減 variable cost，固定團隊/法務/平台；CAC 回收月數和現金/設備折舊獨立；每條候選路線都計算若 P=0、資料費暴漲、服務量增加的停損邊界。
- Recompetition is not a summary of R1; the original candidate is demoted or changed by the stated legal/business/human-material delta.
- O9 LAMP_R2: `REMOVE_FIXED_HKD_CAP / NO_COST_VALIDATION_YET`; counterforce remains `無正式價格報價、CAC、實際續約、工時或回款資料；現在不能做確定 payback 年數。`.
- T2 `SH-CI-P1-E-T2`: R2 change basis=重建成本模型：每客實收減 variable cost，固定團隊/法務/平台；CAC 回收月數和現金/設備折舊獨立；每條候選路線都計算若 P=0、資料費暴漲、服務量增加的停損邊界。

## Mandatory post-R2 premise audit
```yaml
plurality: MULTIPLE_MATERIAL_PREMISE_FAMILIES
premise_scope_narrowness: DETECTED
alternative_framing: "P1 commercial form vs rights-scoped services / Shenzhen field or supplier evidence"
R3_required: true
```

## R3 cross premise material round
SaaS、線下巡檢、採購證據服務的成本驅動各異；以每個訂單/場次/資料源的貢獻與回款週期比較，不能宣稱哪個一定最便宜。
- LAMP_R3: REMOVE_FIXED_HKD_CAP / NO_COST_VALIDATION_YET + surviving material objection.
- T3 `SH-CI-P1-E-T3`: P1 support limited / qualification still absent.
- R4+: NOT_REQUIRED, no additional evidence.

## Main Return / Release
**Main:** `REMOVE_FIXED_HKD_CAP / NO_COST_VALIDATION_YET`. **Objection:** 無正式價格報價、CAC、實際續約、工時或回款資料；現在不能做確定 payback 年數。
**Post-Main Governance:** CONDITIONAL_SEAT_JUDGMENT; source/legal/cost/engineering limits remain.
**Manifestation:** origin type=OBJECTION / AMENDMENT / CONDITION based on seat; semantic type remains this seat's, not Secretary's.
**TM:** `SH-CI-P1-E-TM` checked no material drift.
**Vertical Acceptance:** CANONICAL_ADMIT_AS_LIMITED_SEAT_STATEMENT; formal Council release training status contested.

```yaml
STRUCTURED_GENERATION_EVIDENCE_RECORD_V1_3_1:
  cycle_ref: SH-CI-REENTRY-P1-E-L8-001
  R1: {state: RECEIVED, candidate_count: 3}
  T1: {state: RECEIVED, ref: SH-CI-P1-E-T1}
  R2: {state: RECEIVED, consumes_T1: SH-CI-P1-E-T1}
  T2: {state: RECEIVED, ref: SH-CI-P1-E-T2}
  post_R2_premise_audit: {state: COMPLETE, status: MULTIPLE_MATERIAL_PREMISE_FAMILIES, narrowness: DETECTED}
  R3_plus: {requirement: REQUIRED, performed: [R3], trace_ref: SH-CI-P1-E-T3}
  main_return: {state: RECEIVED, ref: SH-CI-P1-E-MAIN}
  manifestation: {state: PRESENT, claim: "REMOVE_FIXED_HKD_CAP / NO_COST_VALIDATION_YET"}
  TM: {state: RECEIVED, ref: SH-CI-P1-E-TM, drift: NONE_DETECTED}
  release: {status: LIMITED_SEAT_STATEMENT, not: COUNCIL_PROPOSAL_APPROVAL}
  unresolved: ["無正式價格報價、CAC、實際續約、工時或回款資料；現在不能做確定 payback 年數。"]
  persistence: GIT_AFTER_VERIFICATION
  provider_receipt: NONE
```

## Compact L8 Receipt
```text
P1-E / R1+O9+T1 RECEIVED / R2 CONSUMES T1 / O9+T2 RECEIVED
Post-R2 plurality=DETECTED -> R3+O9+T3 RECEIVED / I9 NOT_TRIGGERED
MAIN RECEIVED / TM RECEIVED / SGER PRESENT
Seat Statement: REMOVE_FIXED_HKD_CAP / NO_COST_VALIDATION_YET
Formal Council Qualification: NOT ESTABLISHED
```
