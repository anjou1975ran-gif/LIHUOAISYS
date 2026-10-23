# 理火 PAPER 017｜R3.2 + SDE 深層推導邊審計（二輪增量）
## OpenAI, *The irrationality exponent of π is 2*

**日期：** 2026-10-23（Asia/Taipei）  
**審查模式：** Protocol V5.1.0／Lighter V5.1.0／Main V5.1.1 的文件規範 + PAPER R3.2／SDE；**可見參考級推導審計，不是正式 Host Main/Lighter 運行回執**。  
**前件：** `LIHUO_PI017_R3.2_SDE_Full_Cycle_Reaudit_20261023.md`（獨立保存，未改寫）。  
**新增工作：** 原文與形式化的「命題強度」差分；原始假設流轉；確切代數恆等式驗算；Lean 869 檔子樹範圍查證；來源反向競爭。  
**定案邊界：** 未發現可證成的非法前提偷換；已證實某些**合法弱化**和形式化證明路線差異；高風險深層插值幾何仍待獨立驗證。  

---

## 0. 鎖定的外部來源與版本

來源倉庫：`https://github.com/openai/math`；以下是實際透過 GitHub 來源介面讀取的檔案 blob SHA。若倉庫後續改版，須重新鎖定；此表不自動隨 `main` 移動。

| 來源 ID | 路徑／節點 | Git blob SHA |
|---|---|---|
| P1 | `preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/sections/interpolation.tex` | `69dd30eac65dd0817226970299e4100e15e9ec0b` |
| P2 | `.../build/sections/determinant.tex` | `8da644f464222a8ebcd8a46e1d6e3bf6975c916f` |
| P3 | `.../build/sections/conclusion.tex` | `1577b7461538faa5b6a23850ebb7dd66f01825d7` |
| L1 | `lean/OAI/NumberTheory/PiExponent/Approximation/DeterminantContradiction.lean` | `3b46a6c8002c548105a8228def6e23a7f5375d79` |
| L2 | `lean/OAI/NumberTheory/PiExponent/Approximation/AdmissibleMatrixInterpolation.lean` | `4020f7dd25e10186f64d56b7edbd47fb07b45921` |
| L3 | `lean/OAI/NumberTheory/PiExponent/Approximation/AdmissibleParameters.lean` | `aed8970acadb00f9198d8fbb83048bb48f82185d` |
| L4 | `lean/OAI/NumberTheory/PiExponent/Statement.lean` | `f26a2c5d0bff73d1279b8c579ef68be04ee7794b` |
| L5 | `lean/OAI/NumberTheory/PiExponent/Approximation/AdmissibleMatrixGeometry.lean` | `a684b7075f38134980a563da3968fcc9f13e50d2` |
| L6 | `lean/OAI/NumberTheory/PiExponent/Main.lean` | `486ed39ba52e5a10de7893cf0f302edb873801f2` |
| L7 | `lean/OAI/NumberTheory/PiExponent/Ampleness/AdmissibleBlowupAmple.lean` | `ef689a9fe02216d4659cb107ed1dec0147e1ca9c` |

GitHub 的獨立 PiExponent Git 子樹 `8a202af08bf5a2b708abfc07248834e4bd2a88fd` 的非截斷目錄計數：**869 份 `.lean`**；此數為原始碼規模，不是「869 份 kernel 驗證回執」。GitHub Code Search 在 `lean/OAI/NumberTheory/PiExponent` 前綴下查詢 `sorry`、`admit`、`sorryAx`、`native_decide` 顯示 0 個搜尋匹配；搜索索引陰性不能代替依賴閉包或 `#print axioms`。唯一 `axiom` 關鍵字匹配是 `WeightedGeometryScale.lean` 使用標準 `Classical.axiom_of_choice`，不能單憑名稱判定新增非標準公理。

## 1. Q0 錯誤置換防線：三個不同量詞強度

**論文插值定理（P1:24–57）：** 當 `Kθ^m<1`、`K(w0/v0)θ^m<1` 且固定 `m,K,w0,v0,θ`、再按**與中心點無關**的先後權重門檻選 `w1…wm`、各座標分別的中心座標互異時，jet map 對**所有充分大且適當可整除**的整數 `H` 滿射；充分大門檻可依中心位置變動。

**Lean determinant 介面（L1:94–96）：**

```
def GlobalInterpolationStatement : Prop :=
  ∀ nu : ℝ, 2 < nu → ∀ d : FixedData nu,
    ∀ L : ℝ, ∃ H : ℝ, L ≤ H ∧
      Function.Surjective (actualMatrix d H).mulVecLin
```

這是 **cofinal surjectivity（任意大處至少存在一個滿射點）**，弱於「所有充分大 admissible H 皆滿射」。**源文 vs 形式使用介面確有強度差異**，必須照實記錄，不可把兩者直接說成同一句。

**合法性核對：** L2:127–145 從 `∀ᶠ n atTop, Surjective (packetMap d n)` 建構 `cofinal_actualMatrix_of_eventual_packets`，證明可把「最終每個 n 的 packets 滿射」推到「任意大 H 有矩陣滿射」。L5:20–44 又從 blow-up jets 的 eventual surjectivity 建到 globalInterpolation。因此方向是強→弱，這個轉換本身**不是非法的前提增強**。

**最終使用需求：** L1:125–165 證明所有足夠大的 H 若矩陣滿射都將矛盾，隨後透過上面的 cofinal statement 選出一個 H，恰落入矛盾區。這精確解釋了為什麼最終只需要 cofinal 命題：`eventual contradiction + cofinal success => contradiction`。

**SDE-GEOM-01：** `STRENGTH_DIFFERENCE_OBSERVED`；`TRANSFORMATION=LEGAL_WEAKENING_WITH_TRACE`；`CONSTRAINT_LOSS=NOT_EVIDENCED`。**未得到的結果：** 這並不證明上游 eventual packetMap 或 blow-up jet theorem 數學上正確，只確認命題介面的量詞轉接邏輯有效。

## 2. 權重、中心與 H 的前提傳播／循環依賴檢驗

從 P1:24–57、P1:195–214、P2:24–41、P3:55–135，得以下選取順序：

```
ν>2 → θ,A,B,C,η 的有理參數
      → F0 → 選定 m,K,w0,v0
      → sequential thresholds for weights wi (independent of centers)
      → 從假設的無上界異常分母依次挑 qi，使 wi=ceil(log qi) 達門檻
      → c_{ji}= j*(2\mathrm{i}p_i/q_i), 檢查對 j 的各座標互異
      → 固定中心與權重後，才令 H→∞（或取充分大的 H）
```

P3:98–116 明示中心點依分母，且「權重分離門檻與中心無關」。這是避免循環條件的重要材料。P1 則允許 `H` 的下界在固定所有中心後依中心而定，並沒有要求先於 `qi` 選 `H`。

L3:50–104 中 `AdmissibleParameters` 包括：`volume_eq / volume_lt_one / dimension_margin / collision_margin / sigma_* / x_log / approximations / weight_growth / weight_margin`；L3:105–220 的 `exists_admissible_parameters` 在 `hbad`（任意大異常分母）假設下**逐項構造**這些資料，並非只任意宣告有個滿足所有不等式的參數物件。該構造依賴多個更深的 Lean 引理；**在未跑 kernel 前不可將其合法性保證擴張至完整閉包**。

**SDE-GEOM-02：** `QUANTIFIER_AND_ORDER_PRESERVED_IN_REVIEWED_TEXT`。剩餘的真風險是中心獨立門檻之深層證明是否成立，而非目前已見條件被悄悄刪除。

## 3. 插值到行列式的實際轉接

P2:43–81 選每個列（row）之係數封包，並依 P1 interpolation surjectivity 得所有列線性獨立。因此只要 full-row-rank 成立，即可選**同一組行列下的非零 square minor** `Δ_H`。算術界 P2:83–150 倚賴這個「先證非零」條件，不是僅從矩陣尺寸推得非零。

這條邊真正可能致命的上游是 P1:427–584 的 blow-up / nef / ample / Rees / Serre 命題。**PAPER 論文已逐項提出證明，Lean 也有對應幾何模組；本次沒有獨立核算該 869 檔 closure 與幾何基礎。**

P1:525–534 提供一個具體代數恒等式，將 `A−E` 寫為 `A−(1+σ)E`（nef）與 `aA−E`（ample）的正係數組合：

```
A−E = [(a−1)/(a(1+σ)−1)]*(A−(1+σ)E)
    + [σ/(a(1+σ)−1)]*(aA−E)
```

用 SymPy 符號消去，左右差為 **0**；當 `a>1,σ>0` 時係數為正，前提符號方向沒有倒置。但是「nef + ample 的正線性組合 ample」及先前的曲線不等式仍依賴幾何定理，代數恒等式測試不是完整幾何驗證。

**SDE-GEOM-03：** 橋接在原文中**明示而非直接跳步**；深層證明 `UNVERIFIED`。

## 4. 近似週期 → 真週期的獨立係數級測試（新結果）

P2:196–222 定義 `ε_i=j(r_i−ω)`、`τ_i(t)=G_i(t)−log(1+t)`、`z=jω+log(1+t)`，先作多項式恆等式再取得逐個 `t^s u^β` 的係數；P2:224–257 證明尾項與近似誤差的指數預算。**不是**直接把 `jr_i+G_i(t)` 當成精確的 `jω+log(1+t)`。

本次可重現 Python/SymPy 測試：`m=1`，取獨立符號 `r`、`ω`（無需預設兩者相等）；`G=t−t²/2`，`log(1+t)` 截斷到 `t³`，其尾差 `τ=−t³/3`。測試 `P=Y^h X^α`，`h=0..2`、`α=0..3`、`β≤α`、`j=0..2`，檢查各 `t^0..t³` 係數，**360 個位置差為零**。

- 此試驗是多項式層面的恆等式，可證明選取樣例中，分離 `r−ω` 與 `G−log` 的方法沒有直接吞掉差額。
- **不能**由此推出 P2 的完整無窮階 Taylor 估計、所有參數統一界限或最終 π 結論。

**SDE-TRANS-01：** `NO_ILLEGAL_EQUALITY_IN_TESTED_COEFFICIENTS`；`RISK_UNVERIFIED` 留在尾差規模及全局指數預算的深層證明。

## 5. 算術／解析下界矛盾：獨立代數與有理數參數測試

P2:419–424 有重點不等式（令 `bbar=\bar b`）：

```
ν[A(1−η)−bbar]−(1−bbar)
 − {ν[A(1−η)−θ]−(1−θ)}
 = (ν−1)(θ−bbar)
```

用 SymPy 因式分解得到 `(ν−1)(θ−bbar)`；因 `ν>2`、`0≤bbar≤θ`，這個差必定非負，**作者的 gap 估計方向是對的**。

另外獨立構造全分數參數（非浮點近似）：

- `ν=3`, `b=3/5`, `δ=1/20`, `θ=19/20`, `A=97/100`, `η=1/10000`；
- `C=18909/18430`；`B=3677173/3781800`；`g=9709/1000000`。

Python Fraction 對十項必要不等式全部核實為 `True`，包含 `0<θ<A<B<1`、`A²<θ`、`CB<1`、`Cθ/B>1`、`B/A>1`、`g>0`。這一組小型有理數證人補強了前案以浮點數驗算的正面證據。**注意：仍不代表已找出最終需要的超大 m、wi、H，也不代表論文全部參數已被完整求值或最終無理數指數已證明。**

**SDE-COMP-01：** 兩條局部估計代數證據支持作者；未定位符號倒轉／虛構常數。

## 6. 形式化與原文關係：可見證據與不可擴張項

- L4 的 `GoodRationalApproximations` 與 `EventualLowerBound` 保留了 `0<|x−p/q|`、`ν>2`、`Q(ν)` 以及**全部** p 的量詞；L6 的 `main` 同時聲明 eventual lower bound 與 supremum=2，並非只宣稱有限幾個近似。
- L6 透過 `AdmissibleMatrixInterpolation.globalInterpolation` 和 `LiteralAnalytic.analyticAggregate` 建立主結論；從本文核對，幾何鏈並沒有在 Main 中消失，而是轉交對應模組。
- 自然語言原文會由矛盾直接導出 π 無理性；Lean 內部改以 mathlib 已知 `irrational_pi` 證明 supremum 下界。這是**合法的路線差異**，不能在無反例下叫做虛構證明。
- `ComparatorChallenges/PiExponent.lean` 中的 `sorry` 是 challenge 佔位；
  `ComparatorChallenges/PiExponent.json` 的 `solution_module` 指向真實 `Main.lean`；
  **反之**，`Main.lean` 有 theorem code 也不能取代實際 kernel build 和 `#print axioms`，所以 FORMAL_KERNAL_VERIFIED=NO。
- GitHub Code Search 於 PiExponent 子樹（869 Lean 檔）沒有找到 `sorry / admit` 字串匹配，是支持材料而非完整依賴零缺口的形式證明。

**SDE-FORMAL-01：** `LOGICAL_SCOPE_MATCH_OF_MAIN_CLAIM` 有實際來源支持；`PAPER_INTERPOLATION_VS_COFINAL_FORMAL_INTERFACE` 是合法弱化；完整 Lean kernel 與權限內公理核驗 `NOT_EXECUTED`。

## 7. 新增 PATH 競爭、O9 與資格狀態（可見參考級）

保留四條互斥主路徑，與前份報告採相同身分以利比較：

| PATH | 若要成立必須提供 | 新增證據後狀態 |
|---|---|---|
| A：`CHAIN_INTEGRITY_CLEARED` | 幾何深層引理、依賴閉包、核驗範圍均完成獨立核驗 | 新增幾個正面校驗；**不能成立**（太早放行） |
| B：`ILLEGAL_PREMISE_OR_CONCEPT_SUBSTITUTION` | 來源前後實際不等價差分且缺少合法橋接 | 明確發現強→弱命題差異，但這是合法路線；**未證實** B |
| C：`CORE_DEPENDENCY_UNVERIFIED` | 原文有合理演繹鏈且具局部正面支持，但高影響幾何依賴與 kernel 仍未核實 | **本輪仍最有依據** |
| D：`CLAIM_SCOPE_MISMATCH` | 完全不對應的形式化主張／誤把部分形式化當全文 | 論文主結論與 Lean `main` 明確對上；然而 selected comparator 覆蓋範圍仍須註記 |

**R1（重新基線）：** C 保留領先；A 有新增正面證據，但缺少完整驗證。  
**O9（新增事件）：** 具體查得 P1 的 eventual-all-admissible-H 與 L1 的 cofinal-exists-H 強度不同，且完整追溯強→弱的使用關係；再檢查是否存在反向增強。  
**I9：** 沒有正式 Main/O9 回執，`ACTIVATION_UNKNOWN`，不得標稱實際調燈。  
**R2（完整重評）：** 關鍵接口在正確方向弱化，TRANSLATION 的有限係數恆等式支持作者，GEOM 深層仍不可略過，C 領先；A、B 仍不能取得完整成立要件。  
**R3+（事件式參考重競爭）：** 由新的 exact quantifier mismatch 事件啟動參考級覆核：結論仍為 C；不是合格 Runtime round，也不製造 Main R-CCC 合格連勝。  

**SDE 評估：** `NO_CONFIRMED_CONSTRAINT_LOSS`; `NO_CONFIRMED_ERROR_STABILIZATION`; `RISK_UNVERIFIED`。這些表示**本輪沒有足夠證據證成**，不是「已排除任何可能性」。

**Main/Lighter、Final Gate：** `NOT_ACTUALLY_INVOKED`；`MAIN_RECEIPT: NONE`；`LIGHTER_RECEIPT: NONE`；`GATE_NOT_RUN`，不能把 Gate `NOT_RUN` 混寫成正式 Gate `HOLD`。

## 8. 真正需要突破的下一段（由本輪資訊收斂，而非重複口號）

本輪已將最優先檢核點縮小到：

1. P1:72–176 的「Weighted transverse multiplicity」局部長度下界與 weighted Bézout 上界，檢查其對任意 irred. component、任意 analytic commuting frame 的**真正一致性**；
2. P1:241–425 的 curve inequality 是否能保留全部相異中心／原始 weight separation 條件；
3. P1:427–584 的 jet surjectivity：nef→ample 的代數式已驗，但 ordinary Rees powers／projective global sections 仍需逐條幾何驗證；
4. 如有 kernel 環境，對 `OAI.PiExponent.main` 做獨立 Lean 編譯、`#print axioms`、Comparator 對照與 source SHA 記錄；還須對紙本插值定理的**較強表述**進行獨立數學審查，不應只用最終較弱形式命題取代。

**審查方向建議：** 把接下來的專家／機器驗證集中於上述 **上游 3 組幾何推導邊**，而不是再以有限近似、論文作者身分或單一 `sorry` 當成反證。

---

### 可重現檔案

- `LIHUO_PI017_R32_SDE_Edge_Probe_v02.py`：完全分離近似週期與精確週期符號的 360 個係數測試、精確有理數參數、行列式 gap 符號判定與 ample 系數恆等式。
- `LIHUO_PI017_R32_SDE_Edge_Probe_v02_log.txt`：該腳本真實執行結果；不代表正式 Lean kernel、Main runtime 或證明完成。

**本輪評估：** `PREMISE_INTEGRITY_HOLD_UNVERIFIED / NO_EVIDENCED_SDE_STABILIZATION / FORMAL_RUNTIME_NOT_RUN`。限制範圍以本報告的明示來源與實際測試為準。
