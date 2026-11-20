# R003｜E materially consumes A's owned revision
**Cycle:** CI2-E-R003-L8-002
**Source Events:** CI2-EV-020/021/022/023/024; prior E initial R001 remains unchanged.
**Material influence:** CI2-EV-020..023 A 的收入分組與任務驗收報酬

## R1 candidates
- **E3-A 每上傳一筆就結算，不要求買家** — 成本隨假資料量增長，收入與驗證脫鉤
- **E3-B 買家付費訂閱限定合法的同類統計來源** — 合格且可授權多次重用可攤銷成本；但續權/稽核仍有成本
- **E3-C 買家預先定義任務，來源/複核者按被接受的工作領酬** — 需求較可見、可分工；要處理退件與複查
- **E3-D 高價獨家/先看時效** — 單筆價格可能較高，但法律、核查和銷售成本都可能更高
- **E3-E 免費社群裂變後收企業廣告費** — 可能造成流量假象、價值與合規問題；需證據
### O9 + T1
- R1 bright: network growth plus easy ranking; dark: 沒有實際 Shenzhen 價格、真實驗證率、報酬與買方回款；不排名實際 ROI
- I9 NOT_TRIGGERED; T1 `CI2-E-R003-T1`: A 已避開明顯的金字塔抽佣，但按被驗證情報分錢仍可能讓成本過高：同一訊號的來源數、查證者數、買家數和修正處理成本是獨立變數。

## R2 consumes T1
定義四種單位：q=合格交付的任務數、b=付費的企業數、k=合法可授權的資料包數、v=完成複核的數。Task CM=買家單任務實收−源報酬−核查報酬−錯誤/退款準備−支付/客服−獲客分攤；Feed CM=可重用訂閱收入−資料授權/續權−稽核/儲存−分發；稀有先看費另須扣除合法排他授權成本。來源層級越高不自動給更大佣金，應由合格任務複雜度與結果價值決定。
### O9 + T2
- R2 bright: E-ECON-002: 可獲利單位是合格任務／授權 Feed 的淨現金貢獻，不是成員數、原始投稿數或來源稱號
- `CI2-E-R003-T2` captures changed basis, not a Secretary rewrite.

## Post-R2 premise audit
- Alternatives differ on rights, incentive design, material veracity and price; multiple premise families detected.
- R3 REQUIRED because ranking/viral mechanisms could prematurely dictate business structure.

## R3
存在『垃圾訊號也會大量成長』的反誘因：若某任務的可回收總收益不足以支付採集與複核，平台應拒收或提高任務價，而非靠更高級會員補貼。低價可成包，但只有買家確定購買且再利用權允許才有規模經濟。
- T3: `CI2-E-R003-T3`; O9 R3 preserves legal/market negative cases; no R4 without further material inputs.

## Main Return / owned typed event
```yaml
owner: CORE_SEAT_E
prior_stance: "E 初始主張買家實收收入而非投稿量分紅，A 尚未重定提案"
event_type: "RESOURCE_MODEL + OBJECTION"
main_return: "E-ECON-002: 可獲利單位是合格任務／授權 Feed 的淨現金貢獻，不是成員數、原始投稿數或來源稱號"
material_basis: [CI2-EV-020,CI2-EV-021,CI2-EV-022,CI2-EV-023]
route_to: [A,B,D,N1]
surviving_objection: "沒有實際 Shenzhen 價格、真實驗證率、報酬與買方回款；不排名實際 ROI"
proposal_status: P0_NONE_OPEN_CONCEPT
```

## TM / SGER / Receipt
- TM `CI2-E-R003-TM`: origin object and limits represented without collapsing role, source rank or business price.
```yaml
SGER:
  cycle: CI2-E-R003-L8-002
  R1_T1: COMPLETE_REFERENCE
  R2_CONSUMES_T1_T2: COMPLETE_REFERENCE
  audit: MULTIPLE_PREMISE_FAMILIES
  R3_T3: COMPLETE_REFERENCE
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  Main: "CI2-E-R003-MAIN"
  TM: "CI2-E-R003-TM"
  standing: CONDITIONAL_CONCEPT_OBJECT
  independent_agent_receipt: NONE
```
**Compact L8 Receipt:** R1/T1 → R2 consuming T1/T2 → Post-R2 plurality → R3/T3 → MAIN/TM/SGER recorded. `SAME_MODEL_MULTI_ROLE_REFERENCE`.
