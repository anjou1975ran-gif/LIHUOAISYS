# R001 INITIAL PASS｜B｜架構席｜改變座標與結構分層
**Session:** SESSION_20261120_CLEAN_INTELLIGENCE_IDEATION_002
**Cycle ID:** CI2-B-R001-L8-001 (CHAT_NATIVE REFERENCE)
**Initial qualified material:** Human D0/D1 + Shenzhen prior city scope + old P2/CASE-001 REFERENCE only + seat responsibility + publicly known PRC legal context. **No other current seat stance provided as an input.**
**Execution evidence:** Same-model scoped judgment; not independent blind model and no access to hidden neural state.

## R1｜本席獨立問題
『來源等級』是不是應該完全不同於『情報的銷售等級』？

- **B-F1｜把 APP 視為供稿端，而非情報交易本身**：分開源頭、核對、權利、包裝、收入
- **B-F2｜來源身分與來源歷史可評價，單則觀察仍需單獨核查**：高級來源也可能失誤或撒謊
- **B-F3｜同一份觀察對不同買方價值不同**：價值取決於行動時間、受益人、損失與排他權
- **B-F4｜讓『反證者』與『失效通報者』成為情報供應鏈一級角色**：資訊撤回與更正也可成產品
- **B-F5｜階級制度拆成『任務權限』與『商業定價』**：不以社會階層或拉人頭成為收入資格

### SAC / O9 / T1
- **O9 LAMP R1:** 亮處是可生成的新收入關係；暗區：評級標籤會被競爭者操縱，市場價值依客戶而變，不能拿這套座標裝作驗證完成
- `I9 = NOT_TRIGGERED`（只記可見推理產物，不假稱隱藏模型訊號）
- **T1 / CI2-B-T1:** 如果用一個金銀銅等級同時表示來源可靠、情報正確、合法可售與價格高低，將創造品質錯覺和權利錯配。

## R2｜消耗 T1 後的新判斷
提四個互不替代的座標：S＝SOURCE track record、E＝EVIDENCE quality、R＝RIGHTS scope、V＝BUYER-SPECIFIC VALUE；第五個 T＝TIME sensitivity。來源准入與任務權限依 S/E；真正對外交易須 R；商業價格基於 V/T 的買方可回收效用。框架是問題形成工具，不先寫成 DAIL 或硬-coded 收費引擎。

### SAC / O9 / T2
- **O9 LAMP R2:** 本席修正了「級別一個分數就夠」的前提；保留 評級標籤會被競爭者操縱，市場價值依客戶而變，不能拿這套座標裝作驗證完成。
- **T2 / CI2-B-T2:** 提四個互不替代的座標：S＝SOURCE track record、E＝EVIDENCE quality、R＝RIGHTS scope、V＝BUYER-SPECIFIC VALUE；第五個 T＝TIME sensitivity。來源准入與任務權限依 S/E；真正對外交易須 R；商業價格基於 V/T 的買方可回收效用。框架是問題形成工具，不先寫成 DAIL 或硬-coded 收費引擎。

## Post-R2 Premise Plurality Audit
- `MULTIPLE_MATERIAL_PREMISE_FAMILIES = TRUE`（來源生成、權利、品質、買方價值、收入都可獨立改變）
- `R3_REQUIRED = TRUE`（避免用單一 APP／高級來源定價前提封閉問題）

## R3｜跨前提競爭
一份低 E 的稀有『爆料』可能 V 很高，卻只能賣『待查線索的驗證任務』而不能賣成已知事實。多個低價 E 已合格的樣本，反而可能產生高 V 的可合法統計產品。
- **O9 LAMP R3:** 未知不補成真；反例仍在。
- **T3 / CI2-B-T3:** 以目前概念判斷為限。

## Main Return / Origin-declared Objects
**MAIN `CI2-B-MAIN`:** B-FRAME-SEVR-T｜來源履歷/單件證據/權利/買方價值/時效分離，讓低價批量與高價專用的商業關係合法共存
- `ORIGIN_TYPES = [PROBLEM_REFRAME, GRADE_RELATION, ARCHITECTURE_QUESTION]`
- **SURVIVING OBJECTION:** 評級標籤會被競爭者操縱，市場價值依客戶而變，不能拿這套座標裝作驗證完成
- **TM:** `CI2-B-TM`：確認本席表述與 Main 沒有摘要漂移；不使候選升格為已證實市場需求。
- **Vertical Acceptance:** `CONDITIONAL_SEAT_CONCEPT_MATERIAL`，供跨席路由，非 Proposal qualification。

```yaml
SGER:
  cycle_ref: CI2-B-R001-L8-001
  R1: OBSERVABLE_CANDIDATE_COMPETITION
  T1: CI2-B-T1
  R2: "CONSUMED T1"
  T2: CI2-B-T2
  POST_R2_PREMISE_AUDIT: MULTIPLE_FAMILIES
  R3_PLUS: [R3]
  T3: CI2-B-T3
  MAIN: CI2-B-MAIN
  O9: [R1, R2, R3]
  I9: NOT_TRIGGERED
  TM: CI2-B-TM
  release: CONDITIONALLY_ADMITTED_AS_SEAT_CONCEPT
  execution_identity: SAME_MODEL_MULTI_ROLE_REFERENCE
  actual_validation: NOT_PROVEN
```
**Compact L8 Receipt:** `R1/T1 → R2 consumes T1/T2 → Plurality Audit → R3/T3 → Main/TM/SGER`. Recorded text artifacts only; no independent model provider receipt.
