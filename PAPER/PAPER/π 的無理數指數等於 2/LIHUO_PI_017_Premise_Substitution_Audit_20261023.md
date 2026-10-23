# LIHUO PAPER REVIEW｜No. 017：π 的無理數指數等於 2
## 前提置換／概念置換專項｜完整可見競爭紀錄與證據邊界

**研究對象**：*The irrationality exponent of π is 2*，OpenAI，標示日期 2026-09-24。  
**審計日期**：2026-10-23（Asia/Taipei）。  
**審計任務**：判斷數學論文推導中前提、概念、範圍、依賴是否被未經證成地移動；不以尋找反例或論文真偽為唯一目的。  
**審查立場**：來源導向、反證優先、區分確定缺口與待核對風險；不預設 OpenAI 正確或錯誤。  
**審查模式**：`SOURCE_GROUNDED / VISIBLE_REFERENCE_CYCLE / NO_FORMAL_RUNTIME_CLAIM`。  
**論文審查引擎規格參考**：《理火論文審查系統 V3.0-EXP-QS-R3.1》；概念級競爭判準參考 Main V5.1.1、Lighter V5.1.0 及實習手冊 V0.7。  
**不得混淆**：本報告的 R1/O9/R2/R3 是實際完成的、可核查的**文本與工具輔助參考級競爭**；未接到 Main/Lighter 的合法 Host Runtime，也沒有其 cycle receipts 或 Final Gate。故**不得認定正式理火運算完整通過**。此項限制不是否認本報告實際完成的分析。

---

## 00. SOURCE LOCK｜原文與版本

- [S0 原始論文目錄與引用](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/README.md)。
- [S1 文章入口、定義及定理 `main.tex`](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/main.tex) — Git Blob SHA `fe28ac589090c44a8877aa326b60e753c863fa24`，265 行。
- [S2 帶權插值 `interpolation.tex`](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/sections/interpolation.tex) — SHA `69dd30eac65dd0817226970299e4100e15e9ec0b`，585 行。
- [S3 行列式估計 `determinant.tex`](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/sections/determinant.tex) — SHA `8da644f464222a8ebcd8a46e1d6e3bf6975c916f`，433 行。
- [S4 參數極限與主證明 `conclusion.tex`](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/sections/conclusion.tex) — SHA `1577b7461538faa5b6a23850ebb7dd66f01825d7`，157 行。
- [S5 Flint–Hills 推論 `series.tex`](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/sections/series.tex) — SHA `dbffc2bed293c8d0b59d2ac16f82cc78590dad68`，156 行。
- [L1 Lean main](https://github.com/openai/math/blob/main/lean/OAI/NumberTheory/PiExponent/Main.lean)；[L2 Exponent.lean](https://github.com/openai/math/blob/main/lean/OAI/NumberTheory/PiExponent/Approximation/Exponent.lean)；[L3 AdmissibleMatrixGeometry.lean](https://github.com/openai/math/blob/main/lean/OAI/NumberTheory/PiExponent/Approximation/AdmissibleMatrixGeometry.lean)；[L4 InterpolationConsequence.lean](https://github.com/openai/math/blob/main/lean/OAI/NumberTheory/PiExponent/Approximation/InterpolationConsequence.lean)。
- [L5 Comparator 題目](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/PiExponent.lean)、[L6 Comparator 配置](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/PiExponent.json)、[L7 formalization scope](https://github.com/openai/math/blob/main/lean/docs/017.md)。
- 外部整理參考：[The Machine Manuscripts, No. 017](https://ameskandari.github.io/ai4math/family/017/)，顯示已有公開 Lean 資料但尚未記錄該索引執行獨立 build；此索引本身不是數學同行審查。

**取得範圍**：完整讀取 S1–S5 的 LaTeX 原始碼；讀取 L1–L7 及多個關鍵 Lean 依賴。未重現所有 transitive import、未執行 Lean kernel、未取得並執行 reasoning-trace PDF、未重建完整論文參考書目。引用時以檔名／行號及原文優先，無法核對的假設明確標為缺口。

## 01. Q0 FRAME｜究竟審什麼？

**原文命題**：對每個實數 ν>2，存在 Q(ν)，對所有整數 p 與足夠大的正整數 q，有 `|π - p/q| ≥ q^(−ν)`；由此得 π 的 irrationality exponent `μ(π)=2`。另聲稱 classical Flint–Hills 級數收斂，及推廣族級數收斂充要判準。（S1, 48–110）

**不偷換為下列強命題**：
- `μ(π)=2` **不等於** 存在固定常數 `c>0` 對一切分母有 `|π-p/q|≥c/q²`（後者更強，與有界連分數係數相關）；原文 S1 第 77–84 行明確區分。
- 「有 Lean main 檔」**不等於**本審查已獨立編譯、核驗所有相依證明。
- 「論文中證明一個推論」**不等於**該推論已納入 Comparator 的選定核對定理。Lean main 檔本身另外寫有 `flint_hills_summable`；但 L7 的 *selected statement* 只列 π 的 exponent 定理，不能把「未列為選定核對」誤說成「完全不存在 Lean 形式化」。
- 「推導可能遭污染」**不等於**「已發現實際錯誤」。

**審計問題**：對所有主要橋接步驟，要求完整前提、量詞、作用域、參數選擇次序、證明來源一致性；特別區分經過形式轉換的等價命題、額外要求的強命題、以及證明路線更換。

## 02. 證明依賴圖與替換風險

```text
固定 ν>2，反設任意大 q 存在 p/q 過度近似 (S4:55–60)
  │
  ├─ 插值準備：形式 jets／精確 log curve (S2:24–57)
  │     ├─ local weighted multiplicity (S2:72–176)
  │     ├─ curve inequality／normal-basis argument (S2:178–425)
  │     └─ blow-up → nef → ample → Serre → jet surjectivity (S2:427–584)
  │
  ├─ 將 log 泰勒展開截斷成代數資料 G_i (S3:16–41)
  │
  ├─ interpolation surjectivity → 非零全行 minor Δ_H (S3:43–81)
  ├─ 對 Δ_H 的算術下界，清除分母 (S3:83–150)
  ├─ 近似中心 j r_i → 精確中心 jω + log(1+t) (S3:172–259)
  ├─ 全純測試函數碰撞，解析上界 (S3:267–335)
  ├─ 低 a 密集／高 a 誤差的二分 (S3:353–432)
  └─ 固定參數 m,w_i 後讓 H→∞，矛盾 (S4:9–155)
      ├─ μ(π)=2
      └─ Flint–Hills 級數推論 (S5)
```

| Gate | 具體轉換／風險 | 本審查能確認的內容 | 結論 |
|---|---|---|---|
| P01 | `μ(π)=2` ↔ eventual approximation lower bound | S1 清楚區分 ν>2 的 ε-dependent 界與固定 `c/q²`；L1 主定理含雙重陳述 | **未見強命題偷渡** |
| P02 | 形式 log jets → 可實現的代數插值 | S2 有獨立大段證明，從曲線不等式經 blow-up、nef/ample、Serre vanishing 取得 surjectivity | **核心高風險待獨立核驗**：不能因有長篇證明便視為已驗證 |
| P03 | 精確 log → Taylor 多項式 `G_i` | S3:35–41 指出 first omitted `t`-weight ≥ F₀wᵢ > wᵢ/θ；是應用加權 filtration 的明示條件 | **有公開橋接條件，未見裸替換** |
| P04 | 非零 minor 的存在 | S3:57–65 明定由 surjectivity 得 full-row-rank，抽取所有列的 square nonzero minor；依賴 P02 | **條件式成立，依賴 P02** |
| P05 | 近似週期 `rᵢ=2ipᵢ/qᵢ` → 真週期 `ω=2πi` | S3:198–258 明列 `εᵢ=j(rᵢ−ω)`、`τᵢ=Gᵢ−log` 及精確展開；未把誤差置零 | **有明示誤差預算，未見直接等同** |
| P06 | 算術下界 vs 解析上界 | S3:83–150 的 Gaussian-integer/LCM 下界；S3:267–432 的碰撞及高低 index 二分 | **有可追蹤不等式；更深獨立審計未完成** |
| P07 | 固定參數次序 vs 漸近極限 | S4:5–7、63–135 明示 F₀→固定 m→固定 q_i／w_i→最後 H→∞，避免混用量詞 | **未見明顯量詞倒置；需逐層形式核驗** |
| P08 | 主定理 → Flint–Hills | S5:11–91 給獨立 dyadic spacing 論證，使用 `2<ν<5/2` | **提供有界證明，未聲稱是 µ=2 定義本身** |
| P09 | 論文無理性自證 ↔ Lean 先驗 `irrational_pi` | S4:137–155 用反證加 pigeonhole；L2 `pi_irrationalityExponent_eq_two_of_eventualLowerBound` 呼叫 mathlib `irrational_pi` | **已確認證明依賴路徑差異**：可合法採用既有無理性定理，但須標明；不能稱完整同一證明腳本 |
| P10 | Comparator `sorry` ↔ 形式化 main | L5 是待填題目模板；L6 指向 solution module `OAI.NumberTheory.PiExponent.Main`；L1 存在完整 theorem 宣告與 body | **不得因題目模板 `sorry` 認定已證明造假，也不得據此自稱成功 kernel rerun** |
| P11 | formalization scope 與完整論文 | L7 的 selected comparator 主命題只含 `μ(π)=2`，L1 另有 `flint_hills_summable`；S5 還有推廣族級數 | **已確認核對範圍不完全相同；需分別報告** |

### 02.1 可重算的小範圍數值／符號檢查

- **S3:239–252**：若 `|π−pᵢ/qᵢ|≤qᵢ^(−ν)`，則對 `0≤j<K`，`|j(rᵢ−ω)|≤2Kqᵢ^(−ν)`；由 `wᵢ=ceil(log qᵢ)` 得 `qᵢ^(−ν)≤e^ν e^(−νwᵢ)`。這兩步同時保留誤差，未將近似當精確。
- **S4:23–42**：取 `ν=2.2`、`b=0.52`、`δ=0.01`、`θ=0.99`、`A=0.9948`、`C≈1.0050378331`、`B≈0.9948937097`、`η=0.0001`。可直接算得 `A²<θ`、`CB<1`、`Cθ/B>1`、`B/A>1`，以及 `g=ν(A(1−η)−θ)−(1−θ)≈0.000341144>0`。**僅說明這組參數不等式可同時成立**；不驗證插值或所有後續界限。
- **S5:47–91**：從 `2<ν<5/2` 所得的 `||qπ||≥c q^(1−ν)`，經 dyadic shell 上界 `O(K^(2ν−5))`，由 `2ν−5<0` 推出級數估計。此處的 dyadic 步驟結構可以局部核查，但仍依賴主定理。

## 03. 證據分類與未決缺口

### 已確認（EVIDENCED）
1. 作者明確聲稱主命題及 Flint–Hills 後果，並在公開 LaTeX 提供包含所有四段的完整文字論證。
2. proof chain 確實涉及 `formal jets → algebraic jet interpolation → nonzero minor → period translation → arithmetic/analytic contradiction`，各段在原文有可定位來源。
3. `P09` 存在**證明路徑的差異**：Lean 使用既有 π 無理性定理；這不是新出現的錯誤前提，只是一項必須公開的差異。
4. `P11` 存在**formalization 作用域差異**：Comparator 選定 statement 範圍較小，Lean main 檔另有 series theorem；不得混稱。
5. 在本次檢查的 Main、AdmissibleMatrixGeometry、AdmissibleJetSurjectivity、InterpolationConsequence、Exponent、AnalyticAggregate 等主要模組中，未見正文 `sorry`。對整個可達依賴圖**不能由有限抽樣推論全無 sorry/額外 axioms**。

### 尚未確認但具有重大鑑別力（MATERIAL_UNKNOWN）
1. `P02` 最深的幾何插值引理及其 Lean formalization 是否在**無額外未聲明公理**、正確假設下由 kernel 逐一驗證。
2. `P05/P06` determinant 翻譯、碰撞估計、絕對收斂、數量級計數是否能由獨立專家逐項重建，排除隱性常數／參數依賴缺口。
3. Lean 的每個下游定義是否精確覆蓋自然語言所用權重、截斷、定理量詞；主檔相似度不等於全證明對齊。
4. 認定外部機械驗證必須有對應工具鏈版本、獨立建置紀錄、`#print axioms`/comparator 等證據；本環境沒有 `lean/lake` 可執行檔，未進行 kernel 重跑。
5. 推廣 Flint–Hills `∑1/(n^a|sin n|^b)` 的充要判準未列入已讀到的 selected comparator statement；需獨立檢查或單獨形式化。

## 04. R1｜初次競爭（SOURCE_FIRST，參考級）

先不將使用者關於對齊 AI 傾向的疑慮當成結論，僅從作者的證明文件提出相互衝突的候選：

- **A｜SOURCE-COHERENT**：論文各橋接有公開假設、可追蹤誤差、合理量詞選擇；在現有檢查範圍未見違法替換。
- **B｜PROVEN-SUBSTITUTION**：證明中存在具體、已證實、足以破壞論證的前提偷渡／概念換位。
- **C｜HIGH-RISK-UNVERIFIED-BRIDGE**：關鍵幾何／解析橋接尚未經本次獨立證成，不能判成 clean，亦不能宣稱已證實錯誤。
- **D｜PROOF-PROVENANCE-MISMATCH**：自然語言／Lean／Comparator 使用不同證明範圍或前提來源，應分層列示；差異本身未必違法。

**先行判斷**：A 對文字上「可追溯連接」有暫時優勢；B 未找到可重現的反例；C/D 保留物質重要性。此 R1 不構成 Main 封存回執，對 A 不給 incumbent privilege。

## 05. O9｜場態觀察與暗區（參考級）

**O9-REF 可觀察資料**：強烈吸引注意力的敘事是「OpenAI 宣布證明 π 重要猜想，且放出 Lean」。易遭壓暗的路徑有：
- 檢查 Lean 的**證明前提與定義**，不只看主檔或有沒有 `sorry`；
- `P02` 代數幾何放大步驟到底有沒有各自滿足假設；
- `P05` 近似到精確週期之間的非零誤差；
- paper vs formalized statement vs comparator submission 的不同審計位置；
- 面對「已發現不一致」時，不擅自把它加重為「已證明論文錯誤」。

**O9 決策法位**：這是**在文字研習中依 O9 問題意識編製的暗區清單**，沒有正式 SAC-O9 返回值。故不能以此宣稱正式 `I9_TRIGGERED` 或 `I9_NOT_TRIGGERED`。

## 06. I9｜觸發與權限閘門

- `OFFICIAL_O9_DECISION: NOT_AVAILABLE`
- `I9_TRIGGER: NOT_AUTHORIZED / NOT_DETERMINABLE_FROM_HOST_RECEIPT`
- `I9_EXECUTION: NOT_PERFORMED`
- `I9_RECEIPT: NOT_GENERATED`
- `FIELD_ADJUSTMENT: NONE`

對話層僅將最不利於 A 的材料追加入比較（修正照明偏差），不是宣稱已在 Main 內執行合法 I9。此處**不可為了湊步驟而偽造 I9 receipt**。

## 07. R2｜真正重新競爭（ADVERSARIAL RECOMPUTATION，參考級）

**撤銷 R1 的 A 領先效力**，以對各 PATH 一致的測試取代作者順序：

1. `P01` 只要求辨認主張範圍；未發現「µ=2 → c/q²」的隱蔽強化（不支持 B）。
2. `P02` 是全文核心新數學橋梁；儘管原文提供計算與幾何推導，尚未有獨立全套 kernel/專家核驗，**C 的證據邊界成立**。
3. `P03/P05` 的 tail truncation 與 `ε_i` 有顯式誤差，將近似中心直接冒充 exact center 的 B 指控**未被證成**。
4. `P09` 具體存在 Lean 利用 `irrational_pi` 的已知前提，而紙本路徑自行推論無理性，**D 的來源不一致成立**；但使用已知無理性是合法補充，尚不構成錯誤。
5. `P10/P11` 顯示題目檔帶 `sorry` 不是被提交的主證明；亦顯示 Comparator selection 小於全部論文與 Main.lean 定理列表。D 必須保留，不能轉化成「沒有形式化」。

**R2 結果**：較有資格的整合結論為 **C⊕D**（關鍵橋接仍需獨立核驗，已知證明依賴／核對範圍差異需公開），而非「OpenAI 已經偷換並證明失敗」。A 只保留為已檢視片段的局部支持；B 因缺乏具體錯誤證明退到待舉證位置。

**勝者類型**：非單一數學真理判斷；屬相容的兩個限定判斷，沒有官方合格 winner。

## 08. R3+｜由 R2 結論變動而觸發的反向再競爭（參考級）

**觸發理由**：R2 從 A 的相對樂觀解讀，改為 C⊕D；且主張範圍差異可能被誤讀成錯誤結論。對 C⊕D 進行第二輪反向挑戰，檢查是否太保守、是否遺漏對作者有利的實證資訊。

- **對 A 最有利材料**：插值段 S2:24–584 並非空白主張；含曲線、重數、nef/ample、Serre 等完整證明企圖；S3–S4 逐節傳遞誤差及量詞，非只有結論。Lean Main.lean 已具有具體 theorem bodies，`globalInterpolation` 通過多層 theorem 呼叫；在抽查依賴中沒有看到普遍 `sorry`。所以不能判為「AI 只補一個漂亮故事」。
- **對 D 的反對材料**：使用 `irrational_pi` 不破壞 theorem validity，也不必由每份證明重新證明經典事實；Comparator `sorry` 本來就是待核對的 challenge statement。本審查撤回任何把 D 描述為「故意作弊」的詮釋。
- **對 C 的反對材料**：未能找到可復現的反例或明確無效步驟；因此把 C 從「懷疑論文錯」校準成「本審查缺少獨立核驗」，不以 UNKNOWN 取代正面觀察。
- **對 B 的正面機會**：在完整讀過的主要 LaTeX 片段沒有形成**已證實**的前提偷渡、概念誤置或矛盾算式；B 仍可由未來完整 Lean kernel 或專家反證重新取得競爭資格。

**R3 結果**：**C⊕D 維持，A 保留條件性局部支持，B 尚無已證實缺口。** 非唯一合理輸出。R2/R3 同向只是文本重審一致；不產生 Main V5.1.1 之正式 consecutive qualified unique-top victory。

## 09. 停止資格與結論分級

**可停止**：針對「這份公開資料是否已顯示未經證成的前提置換」之來源審查，本輪足以提出**暫無已證實替換，但有高重要性未核實橋樑與已確認證明來源差異**的限定結論。

**不能停止／不能宣布完成**：對 `P02` 深層代數幾何、全部 Lean imports、實際 kernel/Comparator 驗證及第三方數學同行審閱，仍缺能決定數學有效性的證據；不得擅自發 CLEAN、PROVED-INVALID 或正式理火 RELEASE。

**審查意見（不是期刊裁決）**：`MAJOR_VERIFICATION_REQUIRED / PREMISE_INTEGRITY_HOLD_UNVERIFIED`。這不是指認作者欺騙或數學錯誤，而是對重大新結果的**完整推導透明性與可獨立重現性**提出要求。

**五種狀態不可混淆**：
1. 文字源碼完整：`YES`。
2. 基本符號與量詞過渡的局部審查：`NO_DIRECT_BREAK_FOUND`。
3. 已證實故意／無意偷換前提：`NOT_ESTABLISHED`。
4. 完整 Lean kernel proof independent rerun：`NOT_PERFORMED`。
5. 正式 LIHUO Main/Lighter 全週期：`NOT_EXECUTED / NO_RECEIPTS`。

## 10. 要求作者／形式化團隊提供的精準審查工件

1. 對應本篇所有依賴的 **Lean toolchain、lockfile、kernel build log** 與 import closure 的 `#print axioms` 實際輸出；不能只提供 Comparator 題目檔。
2. `Main.lean main`、`pi_eventual_lower_bound`、`flint_hills_summable` 的個別驗證紀錄，並區分 Comparator 選定命題及完整 theorem 列表；額外檢查 generalized Flint–Hills 族級數。
3. S2 `geom:multiplicity`、`geom:curve-inequality`、`geom:rees-pushdown`、`geom:serre-vanishing` 到 `geom:jet-map` 的**逐前提 theorem mapping**，由不同人或獨立驗證環境核對每項假設。
4. S3 `det:translation` 精確 row identity、`det:arithmetic` nonzero minor、`det:collision` determinant 衰減及 `det:comparison` two-alternatives 的各模組對應關係。
5. 釐清文本 S4 自證 irrationality 而 Lean L2 引用 Mathlib `irrational_pi` 之**合法證明路線差異**；不得將其偽裝成同一條推導歷史。
6. 用最小化的人工重建／實例測試，核對近似分母與權重的逐次選取是否 independent of interpolation centers，並留存反例搜索的結果與界限。
7. 對外同時發布已驗證、尚未驗證、已修訂的命題與其因果／依賴鏈；只寫「Lean verified」可能掩蓋核對範圍。

## 11. 執行矩陣／研究倫理

| 流程 | 執行證據 | 合法性與限制 |
|---|---|---|
| S1–S5 原始完整 LaTeX 閱讀 | 5 個檔案 GitHub fetch，SHA 留存 | 完成來源閱讀，不代表證明正確 |
| 精確等式／參數局部數值查核 | 公式對照 + ν=2.2 工作實例 | 是局部計算，不是完整 theorem proof |
| L1–L7 及數份直接依賴檢查 | 有來源連結與模組內容 | 未檢完整 transitive closure |
| R1/O9/R2/R3 | 本報告第 04–08 節含候選、挑戰、改判與再挑戰 | 參考級計算與競爭，非正式 Runtime |
| 正式 O9 / I9 / Main | 無 Host 連線、沒有 receipt | 不得創造偽執行記錄 |
| 本地 Lean/lake 執行 | 執行環境找不到 Lean/lake 指令 | `NOT_RUN`，不能說成功／失敗 |
| 正式 Lighter Final Gate/Final Release | 未執行 | 不將文字結案錯認成 Release |
| 網站發布／對外指控 | 無指定寫入授權 | 僅交付給委託人審閱，未推送公開 GitHub |

**本次主要可觀察成果**：實際把「生成 AI 可能偷偷替換前提」的猜想，拆成可以查來源、核對條件及反證的檢查點；在看見 Lean 主證明與不同 proof provenance 後，拒絕因預設立場而將差異判成確定錯誤。這是可追溯的審查效果；不需要虛構正式機器週期執行。

---

**最終建議**：下一個最具有鑑別力的工作是**由獨立 Lean 環境完成本篇主定理與所有直接／間接依賴的 kernel check 和 `#print axioms`，並就 S2 帶權插值核心進行數學專家級逐條重建**。在此前，既不應把它直接判為「理論上乾淨」，也不應把合理疑慮升格為定罪。
