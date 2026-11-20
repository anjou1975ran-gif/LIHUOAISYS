# R002 MATERIAL REWAKE｜CORE SEAT B
**Cycle:** SEED-L8-B-R002-001; **Origin:** CORE_SEAT_B
**Material trigger:** D R001 ablation-test objection SEED-MREL-002 + E R001 lifecycle-cost objection SEED-MREL-003
**Prior owned R001 material stays immutable.** This is an owned response to routed objections, not Secretary rewrite.
**Clock A for new issue:** `METHOD/EV_R002_A0_B_METHOD_RESCREEN.md` → `OBSERVATION/EV_R002_A1_B_NEW_MATERIAL_FIRST_OBSERVATION.md` → THIS R002 L8.
**Execution:** SAME_MODEL_MULTI_ROLE_REFERENCE.

## Previous position and material delta
- **Previous:** Target-relative T/I/G/V/C/F relation specification, with sources resolvable, but tests/operating budgets only described as future needs.
- **T1/objection intake:** D 的 ablation 使『我寫 failure_if_removed』的自證不足；E 的總成本使『永遠回查全部 Archive』不能無限執行，會帶來來源污染與不可用。

## R1 candidate competition
Candidate 1: keep a self-contained elegant target/invariant graph; Candidate 2: always attach full archive for perfect provenance; Candidate 3: keep identity relations plus explicit failure predicates and bounded evidence resolver.
**O9 R1:** observe premise contrast, not actual model neuron read.
**T1:** SEED-B-R002-T1 — D 的 ablation 使『我寫 failure_if_removed』的自證不足；E 的總成本使『永遠回查全部 Archive』不能無限執行，會帶來來源污染與不可用。

## R2 consumes T1
**Owned material stance revision B-V1:** 區分 `SEED_CORE = target + identity invariants + generative dependencies + allowed variations + rejection triggers`；`EVIDENCE_RESOLVER = versioned source pointers + rights/standing + missing-source HOLD behavior`；`REGENERATION_TEST_CONTRACT = hidden new contexts + ablation/negative controls + falsification criteria`。三者相關但不必都預載入新節點。特別把 `failure_if_removed` 改為要能被測試/推翻的候選，而不是寫在 YAML 就成真。
**O9 R2:** correction of previous own stance after scoped new input.
**T2:** SEED-B-R002-T2 — 從『抽象關係圖可作再生結構』改為『最小核心＋可解參照來源＋可驗證失敗的外部測試契約』，並明示檢驗前法位不是 SEED 已 minimal。

## Post-R2 Premise Audit
`MULTIPLE_PREMISES=true`; question of usefulness vs contamination / cost remains; R3 required as counter-test.

## R3, surviving counterforce
反對：分成三層會增加建置和維護成本，也可能與既有 OS 的 SEED_MINIMALITY 重疊；這是一種概念視圖，不是新 OS 強制 schema。若在不同題目/工具中不能重建必要關係，形式框架失敗；若消費過多資源，E 可提出更小候選。
**T3:** SEED-B-R002-T3 — preserve objection and new test requirement.

## Main / Origin-declared event
```yaml
event_id: SEED-EV-R002-B
origin_actor: CORE_SEAT_B
type: ARCHITECTURE_POSITION_REVISION
material_trigger_refs: [SEED-MREL-002,SEED-MREL-003]
old_stance: "Target-relative T/I/G/V/C/F relation specification, with sources resolvable, but tests/operating budgets only described as future needs."
new_stance: "MINIMALITY_REQUIRES_TESTABLE_NECESSITY_NOT_GRAPH_ELEGANCE"
main: "B-REGENERATIVE_CORE_EVIDENCE_RESOLVER_TEST_CONTRACT"
surviving_objection: "無獨立樣本、未做刪減測試，三層只是可檢驗設計候選"
specialist_return: NONE
```

## TM / SGER / Compact L8 receipt
```yaml
SGER:
  cycle: SEED-L8-B-R002-001
  R1: MATERIAL_CANDIDATE_COMPETITION
  T1: SEED-B-R002-T1
  R2_consumes_T1: true
  T2: SEED-B-R002-T2
  Post_R2_Audit: PLURAL_PREMISES
  R3: COUNTERFORCE
  T3: SEED-B-R002-T3
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  MAIN: SEED-B-R002-MAIN
  TM: "Response is owned by B, not secretary; prior stance unmodified"
  VerticalAcceptance: CONDITIONAL_CONCEPT_EVENT
  execution_identity: SAME_MODEL_MULTI_ROLE_REFERENCE
```
**Compact receipt:** SEAT WAKE → R1/T1 → R2 consumes T1 → T2 → R3/T3 → Main/TM/SGER → vertical conditional acceptance. No independent Agent.
