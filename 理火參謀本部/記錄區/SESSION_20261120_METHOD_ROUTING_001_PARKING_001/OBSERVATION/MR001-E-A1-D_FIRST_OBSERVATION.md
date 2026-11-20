# MR001-E-A1-D｜Seat D First Observation
**Canonical type:** `FIRST_OBSERVATION`. **Order:** A0 decision and actual selected method read receipt are already committed; `FIRST_MATERIAL_L8` NOT YET CREATED.
**Origin:** CORE_SEAT_D, `NO_METHOD` (same-model role reference).
**Selection ref:** `METHOD/MR001-E-A0-D_DECISION.md`.
**Source read reference:** `SOURCE/METHOD_PACK_ACTUAL_FETCH_RECEIPTS_A0.md` (NO_METHOD; no domain pack loaded).

## The very first observed unit (before any L8)
先定義這項服務若存在就一定會碰到的可觀測交付事件：車位是否可用、使用者是否有權進入、占位是否結束、逾時或閘門失靈怎樣安全撤銷。先不假設攝像頭、車牌辨識、自動閘門與 APP 已經必要。

- **First analysis unit:** 一個預約／核准／進出／占位結束的狀態轉移
- **Evidence this observation makes visible:** 人工或現有車位管控流程、門禁功能、事故/爭議與撤銷需求；目前都未給
- **Candidate relations made visible, not yet selected as stance:** 預約表或現有管理入口的最小事件軌跡，作為未來可測工作流，不是工程部署
- **Method/absence blind spot:** 無設備資訊，無法判定閘門資安、車牌資料與緊急救援風險；如議事提出新具體技術承諾須另處理
- **Method timing:** No Method was selected; bounded unassisted first look.
- **Not observable/unknown:** Exact city, jurisdiction, title/covenants, demand, availability, management staffing, tech apparatus.
- **Stance ownership status:** `NOT_YET_FORMED`. Next step is this Seat's own L8 R1/R2/R3+ with SGER and receipt, after THIS Git commit.

```yaml
event_id: MR001-E-A1-D
origin_actor: CORE_SEAT_D
semantic_type: FIRST_OBSERVATION
source_selection_event: MR001-E-A0-D
method_status: NO_METHOD
method_read_receipt_ref: null
first_material_l8_ref: null
material_stance: NOT_FORMED
study_result_claim: FIRST_OBSERVATION_DOCUMENTED_NOT_EFFECTIVENESS_PROVEN
```

**A1 receipt:** Saved FIRST LOOK before any R1 Material Judgment. If another actor later disagrees, the original First Observation file remains immutable and stance changes must be separately appended.
