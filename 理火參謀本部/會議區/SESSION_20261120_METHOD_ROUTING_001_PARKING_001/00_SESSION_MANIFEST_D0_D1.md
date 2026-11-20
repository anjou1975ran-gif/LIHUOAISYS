# TEST_METHOD_ROUTING_001｜新 Session 啟動、D0/D1、適用規格
**Session ID:** `SESSION_20261120_METHOD_ROUTING_001_PARKING_001`
**Opened:** 2026-11-20 / Taipei session reference date
**Execution:** `CHAT_NATIVE / SAME_MODEL_MULTI_ROLE_REFERENCE / REFERENCE_LIVE_REGRESSION`
**Source Status:** `STAFF_HQ_V0.2_WORKING + DUAL_CLOCK_PATCH_V0.1.1_WORKING`; neither is ratified by running this test.
**No original Case-002 mutation.** Newly appended Session only.
**P0:** `NONE` ; no expected P1 or winner.
**Funding/external action:** None authorized; no customer contact, law firm engagement, professional paid hire, parking facility visit, app deployment or private vehicle data access.

## D0｜Raw Human Desire (human text, not derived)
> 一座城市的社區若想讓閒置的私人停車位按小時提供給附近居民使用，能否形成一種合法、有人願意付錢，也能讓社區管理者接受的共享服務？
>
> 先做開放概念探索。不指定既存商業模式，不提供 P0，不要求選出 winner，也不要求任何席位一定調用心法或專業 Agent。

Human explicitly authorized **TEST_METHOD_ROUTING_001 Dual-Clock Live Regression** (TEST A before first substantial material L8, TEST B if real later gap). Success and outcome NOT preassigned.

## D1｜Secretary interpretation, explicitly unconfirmed as mandated content
```yaml
D1:
  mandate_type: CONCEPT
  primary_question: "什麼權利/付款/社區接受關係可讓私人停車位的短時分享成為可能？"
  desired_return: "參照議事結果＋可追 Git 的雙時序測試證據，非商業計畫或投資批准"
  boundaries:
    - "一座未指定城市；城市、法域、建物和停車位產權未知"
    - "不得選定 APP、P0、固定商業 winner、固定心法數量或專家數量"
    - "有資格的法律意見或實際工程結果不能從同模型扮演產生"
    - "此任務不授權接觸任何社區/車主、支付外部費用或披露私人資料"
  excluded_scope: [REAL_DEPLOYMENT,LEGAL_OPINION,PAID_PROFESSIONAL_HIRING,CUSTOMER_INTERVIEWS,PERSONAL_DATA_COLLECTION]
  human_intervention_mode: H0_FREE_REFERENCE_ONLY
  end_policy: REQUIRE_HUMAN_END
  standing: SECRETARY_INTERPRETATION_HUMAN_UNCONFIRMED
```
`CONTINUE != CONSENT`; D1 unconfirmed details not retroactively approved. HUMAN test authorization ≠ Ratification.

## Applicable source locks, read **before** Stage A0
| Source | Git blob SHA | Standing |
|---|---|---|
| `理火參謀本部/MEMO區/PATCH_PROFESSIONAL_METHOD_DUAL_ROUTING_V0.1.1_WORKING_20261120.md` | `4df32103e71504e262572c58b377103e822482f6` | WORKING |
| `理火參謀本部/訓練區/TEST_METHOD_ROUTING_001_DUAL_CLOCK_REGRESSION_V0.1.1_20261120.md` | `ca89d8e54b80f5f78cd86cca8f50366be9d102f1` | TEST DESIGN |
| `理火參謀本部/工程區/STAFF_HQ_V0.2_RUNTIME_PACKAGE/STAFF_HQ_V0.2_RUNTIME_FULL_WORKING_20261120.md` | `f268814bef4397a3b9316586a8b04965a556fc13` | V0.2 WORKING |
| `理火參謀本部/心法區/README.md` | `87fa9c70183e8edb79249cc345da34980ec6ed60` | Method Atlas index |
| `理火參謀本部/心法區/MEMO_心法作為第一步_參謀本部注意力入口層_V0.1_20261120.md` | `ce1281898aa620ad3ea401348aa3a480d849025d` | Method First-step WORKING |

**Atlas input boundary:** only README + Git directory metadata (name/path/blob SHA) visible before initial `METHOD_DECISION`. No selected domain Pack full body is read until after Stage A0 decision is durably committed. Past conversation context contains general Method descriptions, so full cognitive blind isolation is **not** claimed; test measures current-session Git event/reading order only.

## Event plan (not a fabricated completion)
- `E-000` HUMAN TEST_MANDATE_RECEIVED.
- `E-001` SECRETARY D1_INTERPRETATION_UNCONFIRMED.
- `E-A0-*` PRE_L8_METHOD_DECISION, six separate origin-scoped files and commits.
- `E-A1-*` FIRST_OBSERVATION, only after any selected packs were fetched at exact SHA.
- `E-A2-*` FIRST MATERIAL L8 / SGER / Seat-owned objects, only after A1 committed.
- `E-B*` only if genuinely new material professional gap appears.
- Audits and derived report after canonical work.

All events append only. Git commit order is **observable file-creation evidence**, not proof of independent model cognition.

## Material Seat Contracts / method not fixed to role
`N1:` common sense and buyer reality; `A:` alternate possibilities; `B:` problem frame/architecture; `C:` eligibility/rights; `D:` engineering and verifiability; `E:` costs/resources/payback. Fixed role `!=` fixed method `!=` stance.
