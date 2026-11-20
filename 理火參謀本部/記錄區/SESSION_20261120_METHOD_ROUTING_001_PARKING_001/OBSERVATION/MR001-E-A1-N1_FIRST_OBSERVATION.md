# MR001-E-A1-N1｜Seat N1 First Observation
**Canonical type:** `FIRST_OBSERVATION`. **Order:** A0 decision and actual selected method read receipt are already committed; `FIRST_MATERIAL_L8` NOT YET CREATED.
**Origin:** CORE_SEAT_N1, `NO_METHOD` (same-model role reference).
**Selection ref:** `METHOD/MR001-E-A0-N1_DECISION.md`.
**Source read reference:** `SOURCE/METHOD_PACK_ACTUAL_FETCH_RECEIPTS_A0.md` (NO_METHOD; no domain pack loaded).

## The very first observed unit (before any L8)
不是先問 APP 功能，而是辨識四個實際人：停車位占有人、附近可能使用者、社區管理者、受影響的住戶。『有人願付費』要找具體替代選項、行走距離、尖離峰與車位是否真的空著。

- **First analysis unit:** 一個具體時段＋一個真有需求的人＋一個能提供車位的人＋一個可能拒絕的人
- **Evidence this observation makes visible:** 實際空置時段、居民是否願付、車主允許哪些時段、管理者的具體擔心；目前完全沒有這些資料
- **Candidate relations made visible, not yet selected as stance:** 互相認識的鄰里臨時借位、以社區同意為前提的有償使用；不是先寫 APP
- **Method/absence blind spot:** 常識可能忽略正式權利鏈、事故責任與兩邊網路的定價成本，交 C/E 責任席處理
- **Method timing:** No Method was selected; bounded unassisted first look.
- **Not observable/unknown:** Exact city, jurisdiction, title/covenants, demand, availability, management staffing, tech apparatus.
- **Stance ownership status:** `NOT_YET_FORMED`. Next step is this Seat's own L8 R1/R2/R3+ with SGER and receipt, after THIS Git commit.

```yaml
event_id: MR001-E-A1-N1
origin_actor: CORE_SEAT_N1
semantic_type: FIRST_OBSERVATION
source_selection_event: MR001-E-A0-N1
method_status: NO_METHOD
method_read_receipt_ref: null
first_material_l8_ref: null
material_stance: NOT_FORMED
study_result_claim: FIRST_OBSERVATION_DOCUMENTED_NOT_EFFECTIVENESS_PROVEN
```

**A1 receipt:** Saved FIRST LOOK before any R1 Material Judgment. If another actor later disagrees, the original First Observation file remains immutable and stance changes must be separately appended.
