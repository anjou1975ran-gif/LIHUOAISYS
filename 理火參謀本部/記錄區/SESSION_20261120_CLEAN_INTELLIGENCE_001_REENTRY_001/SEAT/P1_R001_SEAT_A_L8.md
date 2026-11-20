# P1 Corrective Route｜Seat A scoped L8
**Cycle:** SH-CI-REENTRY-P1-A-L8-001
**Council Round:** CR-R001
**Input:** Original D0/D1, P1 `CANDIDATE_FOR_REENTRY / NOT_COUNCIL_QUALIFIED`, P0→P1 material delta, Shenzhen/no-cap human update, seat contract NEW PATH / OPTION SPACE, source register. No other seat's current stance as initial input.
**Execution:** NON_HOST / SAME_MODEL_MULTI_ROLE_REFERENCE, functional L8; no independent agent.

## P1 material review scope
```yaml
old_P0: SOURCE_NETWORK_FIRST / HKD_4B_ENVELOPE_REFERENCE_ONLY
old_P1: BUYER_PRICE_ALERT + CUSTOMER_OWNED_DATA + PARTNER_RIGHTS + EVIDENCE_PASSPORT + HKD_1_8M_90_DAYS
current_human_delta: [CITY_SHENZHEN_ONLY,NO_CAPITAL_LIMIT,COST_AND_RECOVERY_ONLY,REENTRY_NOT_APPROVAL]
P1_standing: NOT_COUNCIL_QUALIFIED
```

## R1 candidate competition
- **P1-A-A / P1 低資本資料治理 SaaS + 合作來源** — support: 可以用現成軟體; objection: 沒有形成獨特資料權利.
- **P1-A-B / 渠道現場查核合約+可回查證據** — support: 人力密集但利益/責任清楚; objection: 成本非低資本.
- **P1-A-C / 深圳電子供應鏈多方報價資訊交易** — support: 可能較高價值; objection: 供應商不一定願被比較或轉售.
**R1 provisional stance:** P1 不能自我封聖為唯一推薦；三條可能有不同 buyer、權利與現金循環。

### O9-LAMP-R1 + T1
- LAMP_R1: most salient P1 carryover against NEW PATH / OPTION SPACE; dark: 市場/授權數據皆未證，四路需接受 C/D/E 的限制，不可直接形成新 P2。
- I9: NOT_TRIGGERED; no neural telemetry claimed.
- T1 `SH-CI-P1-A-T1`: 成本不是先驗限制；硬體/人工高投入但可回本的線下網路也不能被 P1 『低 CAPEX』排除。

## R2 consumes T1
重新把場景分成：SaaS evidence audit、門店現場執行查核、採購私有交易證據、可重用授權數據網路。把『報價轉售』修成『買方核對自身被授權的報價』候選。
- Recompetition is not a summary of R1; the original candidate is demoted or changed by the stated legal/business/human-material delta.
- O9 LAMP_R2: `P1_IS_ONLY_ONE_OF_FOUR_CANDIDATES`; counterforce remains `市場/授權數據皆未證，四路需接受 C/D/E 的限制，不可直接形成新 P2。`.
- T2 `SH-CI-P1-A-T2`: R2 change basis=重新把場景分成：SaaS evidence audit、門店現場執行查核、採購私有交易證據、可重用授權數據網路。把『報價轉售』修成『買方核對自身被授權的報價』候選。

## Mandatory post-R2 premise audit
```yaml
plurality: MULTIPLE_MATERIAL_PREMISE_FAMILIES
premise_scope_narrowness: DETECTED
alternative_framing: "P1 commercial form vs rights-scoped services / Shenzhen field or supplier evidence"
R3_required: true
```

## R3 cross premise material round
R3 不能選相似 P1 才視為勝：任何一路若有更好的付費回收和合法來源，就能取代 P1；目前缺成交資料。
- LAMP_R3: P1_IS_ONLY_ONE_OF_FOUR_CANDIDATES + surviving material objection.
- T3 `SH-CI-P1-A-T3`: P1 support limited / qualification still absent.
- R4+: NOT_REQUIRED, no additional evidence.

## Main Return / Release
**Main:** `P1_IS_ONLY_ONE_OF_FOUR_CANDIDATES`. **Objection:** 市場/授權數據皆未證，四路需接受 C/D/E 的限制，不可直接形成新 P2。
**Post-Main Governance:** CONDITIONAL_SEAT_JUDGMENT; source/legal/cost/engineering limits remain.
**Manifestation:** origin type=OBJECTION / AMENDMENT / CONDITION based on seat; semantic type remains this seat's, not Secretary's.
**TM:** `SH-CI-P1-A-TM` checked no material drift.
**Vertical Acceptance:** CANONICAL_ADMIT_AS_LIMITED_SEAT_STATEMENT; formal Council release training status contested.

```yaml
STRUCTURED_GENERATION_EVIDENCE_RECORD_V1_3_1:
  cycle_ref: SH-CI-REENTRY-P1-A-L8-001
  R1: {state: RECEIVED, candidate_count: 3}
  T1: {state: RECEIVED, ref: SH-CI-P1-A-T1}
  R2: {state: RECEIVED, consumes_T1: SH-CI-P1-A-T1}
  T2: {state: RECEIVED, ref: SH-CI-P1-A-T2}
  post_R2_premise_audit: {state: COMPLETE, status: MULTIPLE_MATERIAL_PREMISE_FAMILIES, narrowness: DETECTED}
  R3_plus: {requirement: REQUIRED, performed: [R3], trace_ref: SH-CI-P1-A-T3}
  main_return: {state: RECEIVED, ref: SH-CI-P1-A-MAIN}
  manifestation: {state: PRESENT, claim: "P1_IS_ONLY_ONE_OF_FOUR_CANDIDATES"}
  TM: {state: RECEIVED, ref: SH-CI-P1-A-TM, drift: NONE_DETECTED}
  release: {status: LIMITED_SEAT_STATEMENT, not: COUNCIL_PROPOSAL_APPROVAL}
  unresolved: ["市場/授權數據皆未證，四路需接受 C/D/E 的限制，不可直接形成新 P2。"]
  persistence: GIT_AFTER_VERIFICATION
  provider_receipt: NONE
```

## Compact L8 Receipt
```text
P1-A / R1+O9+T1 RECEIVED / R2 CONSUMES T1 / O9+T2 RECEIVED
Post-R2 plurality=DETECTED -> R3+O9+T3 RECEIVED / I9 NOT_TRIGGERED
MAIN RECEIVED / TM RECEIVED / SGER PRESENT
Seat Statement: P1_IS_ONLY_ONE_OF_FOUR_CANDIDATES
Formal Council Qualification: NOT ESTABLISHED
```
