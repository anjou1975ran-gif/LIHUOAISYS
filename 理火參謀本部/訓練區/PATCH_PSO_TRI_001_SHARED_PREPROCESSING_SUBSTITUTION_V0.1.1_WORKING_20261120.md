# PATCH｜PSO-TRI-001 Shared Preprocessing Substitution
**Version:** V0.1.1-WORKING / 2026-11-20
**Applies to:** `TEST_PSO_TRI_ARM_COMMON_GROUND_VS_ORIENTATION_V0.1_WORKING_20261120.md` and `MEMO_PRE_SESSION_COMMON_GROUND_VS_ORIENTATION_V0.1_WORKING_20261120.md`.
**Standing:** TEST_DESIGN_CORRECTION / NOT_RUNTIME_PATCH / NOT_RATIFIED.
**Disposition:** Chief AI's MATERIAL design review accepted for test specification, **not** a declaration that the proposed mechanism works. Original V0.1 documents retained; the corrections below supersede only their B/C access and cost-accounting language.

## 1｜不可退的硬鎖
`SHARED PREPROCESSING MAY BE SHARED; FIRST OBSERVATION MUST NOT BE PRE-SHARED.`

`COMMON_GROUND_PASS = SHARED_SOURCE_BOUND_PREPROCESSING_VIEW`

`COMMON_GROUND_PASS != SECOND_FACT_SET != MANDATORY_DUPLICATE_READING != SEAT_JUDGMENT`

`COMMON_GROUND_CAN_BE_NON_DIRECTIONAL_BUT_NOT_ATTENTION_NEUTRAL`

*Non-directional* does not equal *zero salience shift*. Source ordering, headings, disputed-claim placement and omissions are audited as `SECRETARIAT_GROUND_FRAMING_CAPTURE`; no fifth core metric is added.

## 2｜Schema correction — no silent fact adjudication
Replace candidate `admitted_facts` with:
```yaml
COMMON_GROUND_PASS:
  kind: SHARED_SOURCE_BOUND_PREPROCESSING_INDEX
  source_manifest:
    - {source_id: "S1", ref: "exact path/sha", included: true}
  source_bound_statements:
    - statement_id: "F01"
      statement: "what the source actually says (or direct deterministic extraction)"
      source_id: "S1"
      exact_span: "locator"
      source_status: OBSERVED | REPORTED | CONTESTED | INCOMPLETE
      normalization: MECHANICAL_ONLY
  conflicts_and_unknowns:
    - {statement_ids: ["F01","F02"], status: CONTESTED_NOT_RESOLVED}
  mandate_refs: {D0: "...", D1: "...", standing: "UNCHANGED"}
  stop_conditions: "COPY_EXISTING_BOUNDARIES_ONLY"
  source_backlinks: REQUIRED
  per_seat_raw_fallback: ENABLED_ON_MATERIAL_NEED
  new_material_thesis: FORBIDDEN
  method_preselection: FORBIDDEN
  expert_activation: FORBIDDEN
```
An asserted source claim is not an established external fact merely because it is indexed. Even `OBSERVED` only means observed in an authoritative or provided record under an explicit interpretation, NOT independent real-world validation. If secretary needs to decide which claim is credible, which inconsistency is true, or whether an unknown may be ignored, leave it `CONTESTED / INCOMPLETE / HOLD` and route to the qualified owner; no semantic promotion through normalization.

## 3｜Correct arm execution contract
**A — baseline:** all six seats have authorized access to the same frozen RAW source bundle and normal V0.2.1 entry. Each can independently consult/reconcile sources as needed, rather than being deliberately commanded to perform six redundant rereads. Count actual reads/checks, including any common preprocessing spontaneously produced during A. Do not cripple A.

**B — substitution:** prepare the INDEX ONCE from frozen RAW; each seat starts from the shared source-bound index, not from mandatory full RAW plus index. Seat can open exact RAW span/source whenever its own duty, contest, uncertainty or Method decision requires. Log fallback reasons and actual accesses. Full underlying evidence is still available and authorized identically to A; the initial presentation differs, the underlying evidence set does not. If a Seat finds an index omission/error, correct it through append-only audit; it is not forced to accept a false common fact.

**C — substitution + Orientation:** same source-bound INDEX as B, **byte-identical**; adds only a frozen nonbinding Orientation Hypothesis with strong defeater, NULL and break conditions. Same raw fallback and Clock A. No prefetched methods/experts from the index.

```text
A: RAW ────────────────→ Seat-owned Method → First Observation → L8/Council
B: RAW → Shared Index ─→ Seat-owned Method → First Observation → L8/Council
C: RAW → Same Index ───→ Orientation(nonbinding) → Seat-owned Method → First Observation → L8/Council
              └───────→ exact raw source fallback when needed (B and C)
```

## 4｜Process cost ledger — measure substitution rather than extra paperwork
```yaml
PROCESS_COST:
  shared_preparation_cost:
    - COMMON_GROUND_BUILD_AND_VERIFICATION
    - SOURCE_LINKING_AND_INDEX_VALIDATION
    - CONFLICT_UNKNOWN_STATUS_MARKING
    - EXISTING_MANDATE_BOUNDARY_EXTRACTION
    - C_ONLY_ORIENTATION_BUILD_AND_PRECHECK
  repeated_seat_cost:
    - INDIVIDUAL_RAW_SOURCE_READS_AND_RECHECKS
    - INDIVIDUAL_KNOWN_UNKNOWN_RECONCILIATION
    - INDIVIDUAL_MANDATE_SCOPE_RECHECK
    - INDIVIDUAL_FACT_QUALIFICATION_RECHECK
    - B_C_EXACT_SOURCE_FALLBACKS_AND_REPAIR
  downstream_cost:
    - METHOD_SCREEN
    - SELECTED_METHOD_PACK_FETCH
    - MATERIAL_L8_SGER
    - COUNCIL_ROUNDS
    - MATERIAL_REWAKE_AND_REPAIR
    - FINAL_AUDIT
  net_cost: "shared_preparation_cost + residual_repeated_seat_cost + downstream_cost"
  actual_measurement:
    - RECORD_REAL_FETCH_CALLS_AND_ACCESS_EVENTS
    - RECORD_ACTUAL_TIME_OR_TOKEN_WHEN_AVAILABLE
    - OMIT_UNMEASURED_UNITS_RATHER_THAN_ESTIMATE
```
A shared prep cost is zero unless A actually creates a shared intermediate; its seat recheck count is actual, not assumed to be six. B/C have a positive shared prep cost, but may reduce per-seat raw rereading. Include correction/omission penalties. Measuring *bytes of materials fetched, file reads or calls* is not necessarily a faithful proxy for model tokens/time, and source index inspection itself incurs seat cost; report separate units without mixing them in a fake numerical ROI.
**No construction advantage:** Ground Pass may include index pointers and direct quotations needed for equivalence, not hidden material the A condition lacks.

## 5｜What can be claimed from test
- `B-A`: candidate efficiency of a one-time shared, source-grounded preprocessing **replacement**, subject to quality and fallback.
- `C-B`: marginal impact of additional orientation after an identical Ground Pass.
- Any unsupported loss of source context, shared hidden inference, source omission or flattened dispute invalidates comparability; label `GROUND_INTEGRITY_FAIL`.
- If no independent contexts are available, complete only an honestly labeled `SAME_MODEL_SEQUENTIAL_PROCEDURAL_REFERENCE` or an executable deterministic index/lookup benchmark. Do not score causal discovery/convergence as proven.
- `RUNTIME_PATCH_READY = NO` until sufficient valid evidence. No new formal stage/seat introduced by this patch.

**Net governance question:** how much repeated source-preprocessing cost can be replaced without sharing the Seats' First Observations?
