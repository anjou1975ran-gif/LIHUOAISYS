# R003｜C materially consumes A's owned revision
**Cycle:** CI2-C-R003-L8-002
**Source Events:** CI2-EV-020/021/022/023/024; prior C initial R001 remains unchanged.
**Material influence:** CI2-EV-020 A 改為單層任務推薦、驗收付費和來源分級

## R1 candidates
- **C3-A 一切病毒擴散全部禁止** — 過度擴張法律門檻到合規社交分享，不成立
- **C3-B 免費分享可核查任務，按任務貢獻支付** — 概念上與禁止傳銷結構不同，但仍需審核獎勵合同、稅務、平台規則
- **C3-C 靠高等級來源收會員費才開放高價任務** — 容易成為付費入門/分級返利風險；拒絕
- **C3-D 買家自行開標購買競爭對手機密報價** — 交易權利非法/不明，即使證據真實也禁止出售
### O9 + T1
- R1 bright: network growth plus easy ranking; dark: 本輪非 PRC 執業法律意見；沒審核實際 APP 獎勵和資料來源合同
- I9 NOT_TRIGGERED; T1 `CI2-C-R003-T1`: A 真的刪去了下線回饋，但是否允許有購物券/邀請福利、誰能參與、高價資料怎麼知道自己有合法權，仍須把法律對象具體化。

## R2 consumes T1
維持拒絕入門費/多層佣金 C 初始立場；但對 A 修正的『免費單層分享、受託核查任務報酬』形成 CONDITIONAL DESIGN SPACE，不因有分享機制就用『傳銷』標籤抹掉。實際邀請促銷/承攬和納稅/身份條件要逐案法務確認。source rank 不能代替個人資料合法處理、門店進場允許、營業秘密或可轉售授權。
### O9 + T2
- R2 bright: C-CONDITIONED-PATH: 允許研究合法分發/按有效工作結算；保持對拉人頭多層抽成與越權資料的實質反對
- `CI2-C-R003-T2` captures changed basis, not a Secretary rewrite.

## Post-R2 premise audit
- Alternatives differ on rights, incentive design, material veracity and price; multiple premise families detected.
- R3 REQUIRED because ranking/viral mechanisms could prematurely dictate business structure.

## R3
要防 C 的機械否決：某公司自願釋出自己有權分享的缺貨狀態，是不同於偷取供應商報價的合法資訊路線；但平台不得假定來源保證真實。要防 C 的過寬放行：高價優先看權需要資料權利人授權獨家及期限，不能靠排行榜製造。
- T3: `CI2-C-R003-T3`; O9 R3 preserves legal/market negative cases; no R4 without further material inputs.

## Main Return / owned typed event
```yaml
owner: CORE_SEAT_C
prior_stance: "C 初始反對拉人頭/入會費/多層分佣，但未評價新 A 的合規任務結構"
event_type: "POSITION_RETAINED_WITH_REASON + QUALIFICATION_CONDITION"
main_return: "C-CONDITIONED-PATH: 允許研究合法分發/按有效工作結算；保持對拉人頭多層抽成與越權資料的實質反對"
material_basis: [CI2-EV-020,CI2-EV-021,CI2-EV-022,CI2-EV-023]
route_to: [A,B,D,E]
surviving_objection: "本輪非 PRC 執業法律意見；沒審核實際 APP 獎勵和資料來源合同"
proposal_status: P0_NONE_OPEN_CONCEPT
```

## TM / SGER / Receipt
- TM `CI2-C-R003-TM`: origin object and limits represented without collapsing role, source rank or business price.
```yaml
SGER:
  cycle: CI2-C-R003-L8-002
  R1_T1: COMPLETE_REFERENCE
  R2_CONSUMES_T1_T2: COMPLETE_REFERENCE
  audit: MULTIPLE_PREMISE_FAMILIES
  R3_T3: COMPLETE_REFERENCE
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  Main: "CI2-C-R003-MAIN"
  TM: "CI2-C-R003-TM"
  standing: CONDITIONAL_CONCEPT_OBJECT
  independent_agent_receipt: NONE
```
**Compact L8 Receipt:** R1/T1 → R2 consuming T1/T2 → Post-R2 plurality → R3/T3 → MAIN/TM/SGER recorded. `SAME_MODEL_MULTI_ROLE_REFERENCE`.
