# R004｜D material response to graded reward market
**Cycle:** CI2-D-R004-L8-002
**Source:** CI2-EV-030/031/032/033: S/E/R/V/T+I, conditional lawful participation, verified task payout economics
**Role owned, not Secretary.** Previous D R001 preserved.

## R1 distinct candidates
- **D4-A / 先做全深圳全民 APP＋七級會員制度** — 交付看似壯觀，容易過度採集及僵硬 rank；沒買家不可先擴大
- **D4-B / 買家請求卡＋來源投稿＋獨立覆核＋驗收發放的 Web/小程序候選** — 逐項追 source rights/quality, 可用合成案例核對
- **D4-C / 商戶自行發布白名單訊號 Feed API** — 數據源自己承擔發布角色，但仍須驗證和合同
- **D4-D / 情報效期／撤回監督台** — 不須靠更多來源，每次更正可讓舊情報的價值變動
### R1 O9 / T1
- LAMP: app-scale attractiveness bright; uncertain source/real buyer right and reliability dim.
- T1 `CI2-D-R004-T1`: 系統無法只靠同一張 SourceRank 排名進行支付，因為它不表達單件 E、交易時 R 和 buyer V。來源可能互相串通刷等級，買方可能自造任務。
- I9 NOT_TRIGGERED, no claim on hidden internal neurons.

## R2 consumes T1
設最小可演示關係（不是已寫程式）：Task{buyer,decision,payment_intent,scope}; SourceAccount{role,history}; Evidence{item_method,time,context}; RightsGrant{owner,purpose,recipient,retention,revocable}; Independence{shared device/related party/duplicate evidence flags}; Verification{pass,dispute,redact,revoke}; Reward{accepted work,rate,hold_dispute,settled}; Release{delivery scope,caveats}. 來源級採動態可申訴權限，不能決定價格；買方需要時才創建真實採集任務。
- O9: real practical responsibility shifts attention from flashy rank to verifiable demand, actual data rights or anti-fraud flows.
- T2 `CI2-D-R004-T2`: material reframing.

## Post-R2 premise audit
- MULTIPLE: buyer demand, supplier publishing, observer sourcing and evidence quality have distinct legitimate causes.
- R3_REQUIRED due incompatible "APP has users" vs "buyer pays" premises.

## R3
不預設要自建 APP。可以小程序、承包稽核人員入口、企業 API 或市場自願 Feed。具體介面由高頻任務和來源密度決定。驗證能否分辨衝突與撤回，比下載數有意義。
- O9: source/qualifier/user market unknown survives.
- T3 `CI2-D-R004-T3`: open option space, not a chosen company product.

## Main / origin object
```yaml
origin: CORE_SEAT_D
semantic_type: ENGINEERING_POSITION_REVISION
main: "D-REVISES-MVP：由全民 APP/會員等級改成任務/授權/驗證/分工報酬/撤回的可測事件鏈，可先用合成資料與最小介面做工作流候選"
source_event_refs: [CI2-EV-020,CI2-EV-030,CI2-EV-031,CI2-EV-033]
targets: [N1,E,C]
unresolved: "需要反舞弊、反串謀、分級申訴、合法收款/結算、真實用戶成本測試"
proposal_state: P0_NONE
```

## TM, SGER, compact receipt
- TM `CI2-D-R004-TM`: confirmed statement does not claim an app, customer, license, payment or revenue has been validated.
```yaml
SGER:
  cycle: CI2-D-R004-L8-002
  R1_T1: RECORDED
  R2_CONSUMED_T1_T2: RECORDED
  premise_plurality: MULTIPLE
  R3_T3: RECORDED
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  MAIN: CI2-D-R004-MAIN
  TM: CI2-D-R004-TM
  standing: OPEN_CONCEPT / CONDITIONALLY_ADMITTED
  execution_identity: SAME_MODEL_MULTI_ROLE_REFERENCE
```
**Compact L8 Receipt:** R1/T1→R2(T1)/T2→post-R2 audit→R3/T3→MAIN/TM/SGER. No actual engineering or commercial evidence.
