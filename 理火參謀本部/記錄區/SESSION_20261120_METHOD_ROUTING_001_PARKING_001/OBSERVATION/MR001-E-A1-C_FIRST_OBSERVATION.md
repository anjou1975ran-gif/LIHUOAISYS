# MR001-E-A1-C｜Seat C First Observation
**Canonical type:** `FIRST_OBSERVATION`. **Order:** A0 decision and actual selected method read receipt are already committed; `FIRST_MATERIAL_L8` NOT YET CREATED.
**Origin:** CORE_SEAT_C, `SELECTED_LAW` (same-model role reference).
**Selection ref:** `METHOD/MR001-E-A0-C_DECISION.md`.
**Source read reference:** `SOURCE/METHOD_PACK_ACTUAL_FETCH_RECEIPTS_A0.md` and V0.2.C L34–60、L238–250、L255–317.

## The very first observed unit (before any L8)
『私人車位』不是足以判定可對外收費的法律事實。必須先確認城市/法域、車位所有或使用權人、租約/建物規約、共用道路及門禁的許可權、事故與保險責任；現在無法域資料，因此不能作任何城市的合法性結論。

- **First analysis unit:** 法域→權利主體→授權事實→可能程序/契約→法律輸出資格
- **Evidence this observation makes visible:** 城市與法域、物權/租賃文件、管理規約、共用區決議、實際用途與責任安排；皆未知
- **Candidate relations made visible, not yet selected as stance:** 法律問題按不同車位型態開成條件分支，不先宣稱誰有法定出租資格
- **Method/absence blind spot:** 只能做 Tier1/2 法律資訊與假設分析；具體法律意見或重大財產權安排需有權人/合格專業者
- **Method timing:** Selected Method was read at its locked SHA before this observation; anchor V0.2.C L34–60、L238–250、L255–317.
- **Not observable/unknown:** Exact city, jurisdiction, title/covenants, demand, availability, management staffing, tech apparatus.
- **Stance ownership status:** `NOT_YET_FORMED`. Next step is this Seat's own L8 R1/R2/R3+ with SGER and receipt, after THIS Git commit.

```yaml
event_id: MR001-E-A1-C
origin_actor: CORE_SEAT_C
semantic_type: FIRST_OBSERVATION
source_selection_event: MR001-E-A0-C
method_status: SELECTED_LAW
method_read_receipt_ref: SOURCE/METHOD_PACK_ACTUAL_FETCH_RECEIPTS_A0.md
first_material_l8_ref: null
material_stance: NOT_FORMED
study_result_claim: FIRST_OBSERVATION_DOCUMENTED_NOT_EFFECTIVENESS_PROVEN
```

**A1 receipt:** Saved FIRST LOOK before any R1 Material Judgment. If another actor later disagrees, the original First Observation file remains immutable and stance changes must be separately appended.
