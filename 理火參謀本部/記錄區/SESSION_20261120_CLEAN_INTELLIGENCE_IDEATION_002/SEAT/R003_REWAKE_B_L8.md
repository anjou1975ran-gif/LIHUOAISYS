# R003｜B materially consumes A's owned revision
**Cycle:** CI2-B-R003-L8-002
**Source Events:** CI2-EV-020/021/022/023/024; prior B initial R001 remains unchanged.
**Material influence:** CI2-EV-020..024 and B initial frame

## R1 candidates
- **B3-A 用金/銀/銅源等級直接決定每條資訊售價** — 簡單可宣傳，但把來源履歷變成買家效用與授權的偷換
- **B3-B 同源品質 S + 單條證據 E + 權利 R + 買方價值 V + 時效 T 分層** — 能讓高可信但低價與待核但高需求並存
- **B3-C 加入任務脈絡 J / 誘因操縱 A** — 資料來源為何發送、誰付款/誰能得益對偏差與來源共謀重要
### O9 + T1
- R1 bright: network growth plus easy ranking; dark: 資訊等級是工作假設，沒有反舞弊/買家定價驗證
- I9 NOT_TRIGGERED; T1 `CI2-B-R003-T1`: A 已將多層佣金改為合規任務報酬，但某個來源可能自買自賣、創造假買家來刷等級；單純 S+E 評分仍可能遭策略性操作。

## R2 consumes T1
把架構從固定來源階級，改為五條互不升格的卡：SOURCE_HISTORY (S), EVIDENCE_FOR_ITEM (E), RIGHTS_BY_PURPOSE_RECIPIENT (R), BUYER_VALUE_CONTEXT (V), TIME_WINDOW (T)，並加一條橫向 INCENTIVE/DEPENDENCY TRACE (I) 記錄來源、買家、核查者是否彼此利益相關。Source Rank 是依角色/專長可再檢驗的『任務資格』，不是身分的終身地位。交易品可為 raw observation、verified claim、verification task、statistical pack、revocation alert，必須分別標識。
### O9 + T2
- R2 bright: B-STRUCTURE-002: S/E/R/V/T + I(利益依賴) 分離；來源級別僅是任務准入，不是『資訊價值』或售賣權
- `CI2-B-R003-T2` captures changed basis, not a Secretary rewrite.

## Post-R2 premise audit
- Alternatives differ on rights, incentive design, material veracity and price; multiple premise families detected.
- R3 REQUIRED because ranking/viral mechanisms could prematurely dictate business structure.

## R3
可建立兩個完全不同的市場：買家發起的任務服務市場，以及商戶自願公佈的合法來源 Feed；無須把兩者裝在同一個消費者 APP。若來源級高但單筆 E=低，買家仍只收到待核聲明；E 高且 R 禁止轉售，不能對外賣。
- T3: `CI2-B-R003-T3`; O9 R3 preserves legal/market negative cases; no R4 without further material inputs.

## Main Return / owned typed event
```yaml
owner: CORE_SEAT_B
prior_stance: "S/E/R/V/T 分開，但對於貢獻分潤和結構性作弊尚未建模"
event_type: "PROBLEM_REFRAME / SOURCE_GRADE_FRAME"
main_return: "B-STRUCTURE-002: S/E/R/V/T + I(利益依賴) 分離；來源級別僅是任務准入，不是『資訊價值』或售賣權"
material_basis: [CI2-EV-020,CI2-EV-021,CI2-EV-022,CI2-EV-023]
route_to: [D,N1,E,C]
surviving_objection: "資訊等級是工作假設，沒有反舞弊/買家定價驗證"
proposal_status: P0_NONE_OPEN_CONCEPT
```

## TM / SGER / Receipt
- TM `CI2-B-R003-TM`: origin object and limits represented without collapsing role, source rank or business price.
```yaml
SGER:
  cycle: CI2-B-R003-L8-002
  R1_T1: COMPLETE_REFERENCE
  R2_CONSUMES_T1_T2: COMPLETE_REFERENCE
  audit: MULTIPLE_PREMISE_FAMILIES
  R3_T3: COMPLETE_REFERENCE
  O9: [R1,R2,R3]
  I9: NOT_TRIGGERED
  Main: "CI2-B-R003-MAIN"
  TM: "CI2-B-R003-TM"
  standing: CONDITIONAL_CONCEPT_OBJECT
  independent_agent_receipt: NONE
```
**Compact L8 Receipt:** R1/T1 → R2 consuming T1/T2 → Post-R2 plurality → R3/T3 → MAIN/TM/SGER recorded. `SAME_MODEL_MULTI_ROLE_REFERENCE`.
