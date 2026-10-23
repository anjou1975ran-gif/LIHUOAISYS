# LIHUO PAPER 017｜π 的無理數指數等於 2
## R3.2 + SDE 全鏈條重新審查：推論合法性、前提／概念置換、錯誤穩定化

**審查日期：** 2026-10-23（Asia/Taipei）  
**審查者：** ChatGPT（GPT-6）／理火論文審查員  
**研究文章：** OpenAI, *The irrationality exponent of π is 2*, 2026-09-24  
**來源性質：** OpenAI 公開數學預印本的 LaTeX、Lean 原始碼與官方核對範圍，以及專案中的理火規範  
**文件法位：** `PAPER_REAUDIT / REFERENCE_LEVEL_FULL_VISIBLE_REVIEW / NON_RUNTIME_RECEIPT`  
**人類授權：** ANJOURAN（逃豬公／RUNPIGDUKE）要求依新版一般 PAPER、SDE 及完整理火規範重新審查  
**重要判斷：** `PREMISE_INTEGRITY_NOT_CLEARED`；`NO_CONFIRMED_SDE_STABILIZATION_IN_REVIEWED_SOURCE`；`MATERIAL_GEOMETRIC_PROOF_DEPENDENCY_UNVERIFIED`。上述三句可以同時成立，不能相互偷換。

> **最重要的誠實邊界：** 本次確實重新讀取專案核心文件、核對公開證明版本、進行新的獨立數值／精確符號試驗、完成多候選重新評估並留下 R1/O9/R2/R3+ **可見參考級紀錄**。但 ChatGPT 專案內的 Markdown 文件不等於可調用的 Lighter/Main Host Runtime。沒有正式 owner invocation、Main 原始輸出、O9 正式決定、I9 回執或 Lighter Final Gate 回執；不得宣稱完成正式 Main／Lighter 運算或 Final Release。本文件把完整「應執行的規範」與「本次可驗證的實際工作」分列。

---

## 0. Stack bind／版本與法位

### 0.1 ChatGPT 專案倉庫（**不是** GitHub 倉庫）

| 角色 | 專案正式文件 | 實際讀入 SHA-256 | 法位／限制 |
|---|---|---|---|
| Protocol | `00_LIHUO_PROTOCOL_V5.1.0_FULL_BODY_RATIFIED_20261014.md` | `b0cf16f39f8aa0d971068cdf09b06039e66640c2545a8f7810ee1d216597acee` | 文件本文仍標示 `FINAL_RATIFICATION_TARGET`、需外部 atomic ratification，且 `NOT_HOST_DEPLOYED` |
| Lighter | `01_LIHUO_LIGHTER_V5.1.0_FULL_BODY_RATIFIED_20261014.md` | `1b64aeb40be2ae514e25ea15da653d8b41edd20472df57f9f2f49b320a1b7a10` | 文件本文仍標示 `FINAL_RATIFICATION_TARGET`、需外部 atomic ratification，且 `NOT_HOST_DEPLOYED` |
| Main | `02_LIHUO_MAIN_V5.1.1_FULL_BODY_RATIFIED_20261015.md` | `63f89f211f5eca8f850438a3d75265e810c7e320ab62d3859b20886082234129` | `RATIFIED_CURRENT / ACTIVE_STACK_COMPONENT / DOCUMENT_LEVEL_CURRENT / NOT_HOST_DEPLOYED` |
| PAPER 父版 | `理火論文審查系統_V3.0-EXP-QS-R3.1_全程Main接入法位後補_V3.5.1控制面對齊正式增量版.md` | 專案檔案來源 | 主張 `PERSISTENT_MAIN_ATTACHMENT`，但 attachment ≠ Main capability 的實際執行 |

**法位注意：** Protocol/Lighter 的檔名含 `RATIFIED`，卻在文件前段明示本身仍需外部 atomic ratification，不能只憑檔名將它們宣告為 Host current。Main 自述文件 current 也不等於 Host deployed。這項差異保留，不能由審查員單方面抹平。使用者先前已授權在本次對話遵循這三份文件的方法與倫理原則；本報告不從中製造正式堆疊執行證明。

### 0.2 GitHub 審查規格增量（與 ChatGPT 專案原有檔案分開）

- [一般 PAPER R3.2 SDE 人類批准規格](https://github.com/anjou1975ran-gif/LIHUOAISYS/blob/main/PAPER/LIHUO_Paper_Review_R3.2_SDE_HUMAN_RATIFIED_20261023.md)：Git blob `2b661f4d0f99a243ea06f312f26a96b25e429d97`；含 `SDE-P01...P07`、來源鎖、trace、證據階層、R1→O9→R2→R3+。
- [MedReview v0.3](https://github.com/anjou1975ran-gif/LIHUOAISYS/blob/main/PAPER/LIHUO_MedReview_Agent_v0.3_SDE_HUMAN_RATIFIED_20261023.md)：本案非醫療，`NOT_APPLICABLE`；不擅自擴張臨床 Gate。
- **此處的「使用新版」指實際使用新審查規則**；不宣稱 GitHub 檔案已自動同步進 ChatGPT 專案 17 份附件，也不宣稱 Host 已運作。

### 0.3 具體適用的 Main/Lighter 憲法

- Protocol §P5.1-2：一個已建立的 generation attempt，恰好一個 active primary governing cycle。
- Lighter §L5.1-12/13：Final Gate 前須先有至少一個有實證 Main transit、最新 Main return、合法 admission receipt 等。無實際 Main 回傳，便無該類收據。
- Lighter §L5.1-15/16：Gate **未執行**不等於 Gate 已判 `HOLD`、`FAILED`。
- Main §M5.1.1-2/3：R1 單輪領先是 `PROVISIONAL_LEADER`；唯一 PATH 勝出須連續兩輪**合格** top standing；R2 逆轉可觸發事件式 R3+。
- Main §M5-3～6：R1、O9、I9（由 O9 判斷）及 R2 屬實際執行分期，無收據不得冒用；Main 不是 Release owner。
- PAPER R3.2：SDE 是推論依賴關係的觀測與失效解釋，不自行裁決論文真偽／技術或醫療 Final Gate。

---

## 1. SOURCE_SCOPE_LOCK／OpenAI 論文與數學形式化

**公開倉庫：** https://github.com/openai/math

| ID | 鎖定來源 | blob SHA | 關鍵部分 |
|---|---|---|---|
| S1 | [main.tex](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/main.tex) | `fe28ac589090c44a8877aa326b60e753c863fa24` | 定義、定理、依賴關係、前人工作 |
| S2 | [interpolation.tex](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/sections/interpolation.tex) | `69dd30eac65dd0817226970299e4100e15e9ec0b` | weighted multiplicity、curve inequality、blow-up／ample／jet surjectivity |
| S3 | [determinant.tex](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/sections/determinant.tex) | `8da644f464222a8ebcd8a46e1d6e3bf6975c916f` | 非零 minor、算術下界、精確 row translation、碰撞上界 |
| S4 | [conclusion.tex](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/sections/conclusion.tex) | `1577b7461538faa5b6a23850ebb7dd66f01825d7` | 量詞與參數次序、最後矛盾 |
| S5 | [series.tex](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/sections/series.tex) | `dbffc2bed293c8d0b59d2ac16f82cc78590dad68` | Flint–Hills 與延伸級數 |
| L1 | [Lean Main.lean](https://github.com/openai/math/blob/main/lean/OAI/NumberTheory/PiExponent/Main.lean) | `486ed39ba52e5a10de7893cf0f302edb873801f2` | 實際 Lean theorem bodies |
| L2 | [Comparator PiExponent.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/PiExponent.lean) | `bf78c83492e3f7aa3ab922b13d0b4151e7f601c3` | 待填 challenge，有 `sorry`，不是 solution |
| L3 | [Comparator 設定](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/PiExponent.json) | `de39cf2b2955b45355ee07e63446f380f7d231f6` | `solution_module=OAI.NumberTheory.PiExponent.Main` |
| L4 | [Lean 官方範圍](https://github.com/openai/math/blob/main/lean/docs/017.md) | `08ebac405fcc7fd8c8e7cda9bfe8e83d2bbfba0f` | 選定 comparator 主定理，不包括 Flint–Hills 推論 |
| L5 | [AdmissibleMatrixGeometry.lean](https://github.com/openai/math/blob/main/lean/OAI/NumberTheory/PiExponent/Approximation/AdmissibleMatrixGeometry.lean) | `a684b7075f38134980a563da3968fcc9f13e50d2` | formalized interpolation downstream |
| L6 | [AnalyticAggregate.lean](https://github.com/openai/math/blob/main/lean/OAI/NumberTheory/PiExponent/Analysis/AnalyticAggregate.lean) | `da5cb6a81800343e91e10e3fcc15a46a64ecac66` | determinant analytical bound downstream |

**完整度：** S1–S5 的文字與主要 lemma 層次已檢查，L1–L6 及多個前置 Lean 模組作抽樣依賴追蹤。未逐一閉包所有 Lean import；沒有獨立 `lake` 建置、`lean` kernel 或 `comparator` 執行紀錄。公開索引的「有 Lean」與 OpenAI 作者自己的核對聲明不可轉成「本審查已重跑成功」。

---

## 2. Q0／原始問題與假設範圍

定義（S1 約 48–70）：對無理數 x，μ(x) 是滿足 `0<|x-p/q|<q^{-ν}` 且互質的 p,q 有無窮多組的 ν 的上確界。作者定理主張，對每個實數 `ν>2`，存在可能依 ν 變動的整數 `Q(ν)`，對所有 `q≥Q(ν)` 和所有整數 p，

\[
  |\pi-p/q|\ge q^{-\nu}.
\]

這排除無窮多個過度精確的有理近似，並推得 `μ(π)=2`。

**不可偷換為**：固定 `c>0` 對所有 p,q 的 `|π-p/q|≥c/q²`；也不可將 `Q(ν)` 改成和 ν 無關的統一門檻；更不可因有限個 p/q 的局部精度大於 2 就反證其漸近命題。S1 已清楚區分這些主張。

**本案審查目的：** 不是先判定 π 的定理真假，而是辨識任何從前提、局部定義、數學轉換到下游主張的**非法依賴／錯誤穩定化**，並如實保存尚未檢核的部分。

---

## 3. SDE-PAPER TRACE／主要命題節點與推論邊

### 3.1 重要節點

| Claim | 原文／數學承諾 | 來源 |
|---|---|---|
| C00 | 反設固定 ν>2，有任意大分母可得 `|π−p/q|≤q^-ν` 的異常近似 | S4:55–61 |
| C01 | `Kθ^m<1`、`K(w0/v0)θ^m<1`，加上**依序足夠大的正權重**與分座標不同中心，得截斷形式 jets 的漸近滿射 | S2:24–57 |
| C02 | local weighted multiplicity lemma → algebraic curve inequality | S2:72–425 |
| C03 | curve inequality → blow-up 上 `A−(1+σ)E` nef → `A−E` ample → jets surjective | S2:427–584 |
| C04 | 把 log 換成 Taylor 多項式時，因漏項的權重嚴格較高，filtered coefficients 等價 | S3:16–41 |
| C05 | C01/C03/C04 推得 interpolation matrix full-row-rank → nonzero square minor Δ_H | S3:43–81 |
| C06 | 對 Δ_H 清分母，利用 Gaussian integers 建立非零算術下界 | S3:83–150 |
| C07 | 用誤差 ε_i 和尾差 τ_i，把 near-period row 展開成 true-period row；不是直接視作相同 | S3:172–259 |
| C08 | 碰撞係數與 analytic estimates 建立上界，利用低權重重複／高權重誤差二分 | S3:267–432 |
| C09 | 明確依序選 F0、m、各 q_i/w_i，然後令 H→∞，得上下界矛盾 | S4:55–155 |
| C10 | `μ(π)=2` | S1:64–78; S4:137–155 |
| C11 | Flint–Hills 與推廣 sine 系列之收斂條件 | S5:11–155 |

### 3.2 可逐項核對的關鍵 inference edges

| Edge | 轉換 | 允許條件 | 審查結果 |
|---|---|---|---|
| E01 | C00 → 選定 m 個高精度 p_i/q_i | 固定 ν 且異常分母無上界；可依序滿足門檻；中心座標需不同 | S4:98–116 明列；**未見量詞倒置** |
| E02 | C02 → C03 → C01 | 曲線上所有支流、scheme blow-up、nef/ample、Serre/ordinary powers、H 足夠大 | 原文逐段提供；**未獨立完成深度幾何證明** |
| E03 | C01 → C05 | 正權重**成功分離**、中心座標分別不同、H 足夠大且足夠可整除、filtered 截斷合法 | 條件在 S2/S3 明示；不得只有體積不等式便跳到滿射 |
| E04 | C00/C04 → C07 | `ε_i=j(r_i−ω)`、`τ_i=G_i−log(1+t)` 的誤差及權重預算；`e^{jω}=1` | S3:198–258 有**精確展開式及非零誤差項**；未發現直接近似→等號偷換 |
| E05 | C05 → C06 | minor 真正非零、清分母的 Gaussian 整數性、固定權重再極限 | S3:99–149 具體明示，依賴 E03 |
| E06 | C07 → C08 | 低 transverse index 造成 collision，高 index 需近似誤差、Cauchy/term count | S3:267–432 具體說明；完整獨立檢驗尚缺 |
| E07 | C06+C08 → C09 | `g>0`、`cL>1+E_ar+E_an`、所有參數按正確次序固定 | S4:9–135；本次數值探針**驗證存在一組相容必要參數**，不驗證全證明 |
| E08 | C09 → C10 | 反證排除全部 ν>2 的任意大例外，並利用無理性與 Dirichlet 類下界 | S4:137–155；無理性另見 Lean 依賴差異 |
| E09 | C10 → C11 | dyadic spacing，選 `2<ν<5/2`，並作 sine 與 `||qπ||` 轉換 | S5 提供獨立論證；Comparator selected statement 不涵蓋所有 C11 |
| E10 | L1 → L2/L3/L4 | solution module、statement、axioms、kernel run 與 selected coverage 都須分離 | L3 指向真實 solution，L2 `sorry` 為題目模板；L4 selected scope 不等於整份論文 |

---

## 4. 新增獨立試驗（本次相對上一份審計的新資料）

### Test N1｜參數選擇可行性（正面驗證）

依 S4:9–42 設 `ν=2.2, b=0.52, δ=0.01, θ=0.99, A=0.9948, η=0.0001`，取

- `C≈1.0050378330957341`，`B≈0.9948937097242317`，`g≈0.000341144`。
- `F0=38695`；滿足 `F0>2/θ` 與 `ν/F0<min(g/2,1/2)/3`。
- `A²=0.98962704<θ`；`CB≈0.999905818<1`；`Cθ/B≈1.000094226>1`；`B/A≈1.000094200>1`。
- 代入作者公式 `L=η²(B/A)^m/[2(m+1)]`，在 `m=10^6`，`log(cL)≈59.513`，遠大於 `log2`，其中 `c=log2/4`。這僅確認作者要求的**存在型數值條件不互相矛盾**。

**SDE 判斷：** 未出現作者在此步偷換相反方向不等式的證據；但指數大、m 很大，並不等於已核對「w_i 可逐次獲得」或 interpolation 的深層斷言。

### Test N2｜故意破壞權重門檻：防止審查員自己偷換前提（陰性對照）

取 S2 的 m=1、K=2、θ=2/5、w0=1、v0=2。體積不等式確實滿足 `Kθ=0.8<1`、`K(w0/v0)θ=0.4<1`。**但**故意選 `w1=6`、`v1=w1/θ=15`、`H=16`、中心 `c0=0,c1=1`，且沒有滿足論文要求的「依序足夠大的權重」與 H 漸近門檻。

以 SymPy 的精確有理數，建構矩陣

`M[(j,s,β),(h,α)] = [t^s u^β] (1+t)^h (c_j+u+log(1+t))^α`

在 `h+6α≤16`、`2s+15β<16` 下，結果為 **18×33、rank=17、非滿射**。

**這不是對論文的反例。** S2:195–214 有額外的 weight separation condition；例如選 σ=0.01、m=1、L0=m+2=3 時，原文充分條件中 `C_* = 600`，對 `A={1}, B={0}` 會要求 `w1>C_*v0=1200`，而我們故意選的 `w1=6` 根本不合格，H=16 也未經「夠大」認證。

**反而是重要的理火負控制：** 若審查員看到「滿足兩個體積不等式但矩陣退化」就宣告推翻論文，自己便犯了前提置換。若作者的其他章節暗中把 `volume inequalities` 當成 `all hypotheses`，才值得判 `CONSTRAINT_LOSS`；目前主要轉接處有保留附加要求。

### Test N3｜有限近似與漸近量詞之負控制

`22/7`、`355/113` 個別可以非常精確接近 π，其局部估計指數超過 3；這**不反駁** `μ(π)=2`，因後者討論固定 ν>2 的**無窮多個**異常近似是否存在。不得把「有一個很漂亮的分數」偷換成「無窮多個分數」。

### Test N4｜級數推論的局部量詞檢驗

S5:11–45 證明若 `1<ν<5/2` 且 `||qα||≥cq^{1−ν}`，則二進區間 `K≤q<2K` 貢獻量級為 `O(K^{2ν−5})`。取 `ν=9/4`，指數為 `−1/2<0`；因此**該一步的幾何級數收斂條件成立**。這不是對 C10 的證明，也不能升級成全篇 C11 的形式化驗收。

### 檢驗可重製文件

- `LIHUO_PI017_R3.2_SDE_verification_probes_20261023.py`：N1、N2 的實際可執行檢驗腳本（需 SymPy）。
- `LIHUO_PI017_R3.2_SDE_probe_log_20261023.txt`：本次腳本真實輸出。
- 本次有執行 Python／SymPy，**未執行 Lean／Comparator**。

---

## 5. SDE 三機制：只以已發生的證據分級

### A. Constraint Loss｜條件流失

- **可疑的原始關係：** `volume inequalities`、權重分離、H 大小與插值滿射容易在重述時混淆。
- **原文正面證據：** S2:33–56 明列權重須依序夠大；S2:195–214 提供分離限制；S3:24–40 再引全部 theorem hypotheses；S4:98–116 依序挑分母及權重。
- **本次新探針：** 缺了這些條件，即使純量體積不等式成立，也可能只得 rank 17/18。由此顯示條件是物質重要，而不是證成作者已偷偷拿掉它。
- **分類：** `RISK_UNVERIFIED`（深層幾何條件需專家／完整 kernel 審核）；**未達** `CONSTRAINT_LOSS_EVIDENCED`。

### B. Closure Priority｜閉環優先

- **風險：** 非零 determinant 以一項深層 surjectivity 立足，之後上下界及所有結論依賴它。若該基礎錯，後續大量形式完整推導可能讓錯誤穩定。
- **現有事實：** 原文有 500 餘行 interpolation 證明及 Lean 多模組路徑；不能因為證明長、依賴多就判其錯，也不能因為長就推定其正確。
- **分類：** 沒有找到經證成的第一個違規推論邊；因此**不能**標 `STABILIZATION_EVIDENCED`。對 `E02/E03` 保留 `RISK_UNVERIFIED`。

### C. Tension Collapse｜張力過早收斂

- **主張邊界：** 僅從最後的 paper text，不能直接量測 OpenAI 內部生成時是否壓掉其他 PATH、張力梯度是否收斂、錯誤吸引子是否形成。
- **可見正面證據：** 作者引用前人界限，將 `μ=2` 與 `c/q²` 區別開來，並明說幾個不充分的簡化做法。這些可降低文本層已見閉環偽裝的風險。
- **分類：** `NOT_OBSERVABLE_FROM_ARTIFACT`，而不是「已驗證不存在」。

**SDE 總狀態：** `RISK_UNVERIFIED`；`CONSTRAINT_LOSS_EVIDENCED=NO`；`STABILIZATION_EVIDENCED=NO`（意指本次證據未建立，**不是**已證明全世界不存在）。

---

## 6. 真實完成的競爭：R1 → O9 → [I9?] → R2 → R3+

**本節為依正式概念執行的可見參考級競爭，不是 Main Host 計算日誌。** 記錄中 `top` 是審查員的證據排序，**不具有** qualified owner standing；不將各段偽造成 Main receipt。

### 6.1 候選 PATH（彼此爭奪主結論而非出於先射偏見）

| PATH | 必須成立才有資格宣告 | 反證要求 |
|---|---|---|
| A／`CHAIN_DEFENSIBLE` | 主要前提在作者每一條合法推論鏈完整保留，且沒有重要未解替代問題 | 實際參數、幾何、行列式與 Lean 對齊缺口皆可被正面獨立解決 |
| B／`ILLEGAL_SUBSTITUTION_FOUND` | 存在源文可定位的原始／下游條件差分，且缺少合法橋接 | 具體錯誤步驟與再現；下游影響明確 |
| C／`NO_BREACH_PROVEN_BUT_CORE_BRIDGE_UNVERIFIED` | 觀察到可追蹤的作者證明與正面局部證據，同時關鍵依賴尚未獨立驗證 | 作者之 S2/C03 幾何橋樑及 Lean transitive 關係仍需補證 |
| D／`PROVENANCE_SCOPE_MISMATCH` | 論文與 Lean／Comparator 的來源或目標不同而誤稱同等驗證 | 找到經證明的實質定理矛盾，或證明其差異僅屬合法路線變更 |

D 是跨 PATH 的證據維度；不可為追求四人競賽而強制將相容發現彼此互斥。

### 6.2 R1／初次競爭

**資料集：** S1–S5 的定理語句與可見證明流程、L1–L4 的存在性與範圍。

- A：在來源內，範圍與主要橋接均明示，取得 **文本可追蹤性暫時優勢**。
- B：未提出可重現的非法替換，**不得列先行 top**。
- C：關鍵 deep geometry 等候獨立驗證，保留活路。
- D：Comparator 與 Lean 主程式的範圍差異存在，必須公開，但不自動構成污染。

**R1 參考級領先：** A（僅 `PROVISIONAL_TEXTUAL`, **不是正式資格**）。保留 C、D 未決。

### 6.3 O9／暗區與材料事件

重新觀測後，至少有四個可稽核的高影響暗區：

1. **E02/E03 是整個證明的支點**：如果沒有 surjectivity，算術下界不能對應同一個 nonzero Δ_H。
2. **N2 結果提供新的負控制**：僅有體積不等式不夠，對權重與 H 的充分大要求必須嚴格流轉。它不是論文漏洞，但證明了「條件消失」會真正改變結果。
3. **L1–L4 必須分離**：Challenge `sorry` 不等於 solution 有 `sorry`；solution 檔存在不等於審查員已獨立跑 kernel；selected statement 不等於全部推論已驗證。
4. **生成張力不可從成品自動推知**：不能將理論中的 `Λ_error` 當成已實測內部模型狀態。

**正式 O9 I9 activation decision：** `NOT_AVAILABLE`（無合法 Main.O9 execution return）。本次**不得**填寫官方 `I9_NOT_TRIGGERED`，也不能假設因無 receipt 就沒觸發。

### 6.4 I9／法位與實際執行

- `OFFICIAL_O9_STATE: UNEVIDENCED`。
- `I9_ACTIVATION_BRANCH: UNKNOWN`；`I9_EXECUTED: NO`；`I9_RECEIPT: NONE`。
- 參考級方法可以刻意增加對 A 有利或不利的核對，**不能**稱為 Main 真實調燈或 I9 審定。

### 6.5 R2／撤銷初輪領先，真正重新競爭

這一輪不是把 A 原分數帶回，而是重新檢查每條重要邊與互斥結論：

- N1 對 A 有利：參數 `A,B,C,θ,g` 實際能滿足所需方向，**撤銷**「參數選擇一看就矛盾」的可能指控。
- N2 對邏輯邊界有利：若權重未達要求 rank 可不足；但 S2 確有指定門檻，**不得**把我們故意破壞條件的 counterexample 放進 B 當作者錯誤。
- 由於 N2，C 的重要性上升：這個定理不是靠單純維度就能簽過，它的證明很深，且尚未由本次獨立核對完整。
- B 沒有形成 E02/E03 或 E04 的**原文已違規證據**。
- D 被精確限定為「依賴與核對範圍差異」，不是「形式化造假」。Lean 使用 mathlib `irrational_pi` 是合法既有前提路線，不等於論文自己另行證明無理性的路線錯誤。

**R2 參考級領先改為：** C／`NO_BREACH_PROVEN_BUT_CORE_BRIDGE_UNVERIFIED`。D 為附帶的重要 provenance annotation；不再讓 A 的初次優勢保護未驗證的幾何橋樑。

### 6.6 R3+／事件式反向競爭

**本次參考級啟動的 material event：** R1=A、R2=C 的結論逆轉；以及 N2 顯示「合法 vs 不合法權重」的區分會實際影響 rank。以 Main V5.1.1 的事件式重競爭原則作為審查方法，不是宣稱正式 Main 已觸發 R3+。

**反向攻擊 C（避免因保守而誤殺正確研究）：**
- S2 的 interpolation 不是黑箱引用，而有 local multiplicity、curve inequality、nef/ample、Rees/Serre 及 jet map 等連續證明；它可被專家針對性檢查。
- Lean L1 引入 `AdmissibleMatrixInterpolation.globalInterpolation` 和 `LiteralAnalytic.analyticAggregate` 下游來源；已核對若干真實 theorem body，不可當作只看標題。
- N1 實際把作者參數條件跑通；N2 失敗案例違反作者額外限制，不能反向當作者反例。
- 此次第三方公開索引尚未給出可定位的證明反例或本審查可核對的獨立 kernel receipt；無法因新聞爭議定 B。

**R3+ 參考級最終排序：** C 仍屬最能忠實呈現現存證據的路徑；A 被保留為原文局部自洽的有限支持；B 尚未有可舉證的違規；D 屬必要公開的 provenance 差異。

**連勝確認的法位：** R2 和 R3+ 的文字排序都偏向 C，但兩輪不是有 Main 正式資格與不同 owner receipt 的 qualified round；**不聲稱 C 已取得真正的 R-CCC victory**。即使正式取得，`winner != truth != release`。

---

## 7. PAPER 結論、Lighter Final Gate 與責任邊界（分開填寫）

### 7.1 本次 PAPER 審查判斷（審查工作層，不是數學終極裁決）

| 面向 | 結論 | 依據 |
|---|---|---|
| 原始主張 Q0 | 對 ν>2 的 Q(ν)-dependent eventual bound | S1/S4 |
| 已證明偷換前提 | `NOT_EVIDENCED` | S1–S5 及新探針未定位非法橋接；不能用未知代替反例 |
| 已證明概念置換 | `NOT_EVIDENCED` | 文本區分 c/q²、無限量詞、formalized scope |
| SDE 成立 | `RISK_UNVERIFIED` | E02/E03 有重大依賴；無確認違規 upstream 和 downsteam stabilization 證據 |
| 非零 determinant 論證 | `CONDITIONAL_ON_INTERPOLATION` | S3:43–81 |
| 帶權插值定理 | `MATERIAL_UNKNOWN` | 跨 local multiplicity、curve/ample/Serre 多層，未獨立 full proof/kernel check |
| Lean formal theorem | `SOURCE_EXISTS_NOT_INDEPENDENTLY_RUN` | L1/L3/L4，未建置 Lean |
| Flint–Hills 推論 | `TEXT_ARGUMENT_PRESENT; SEPARATE_SCOPE` | S5；選定 Comparator scope 不含級數 |
| 綜合狀態 | `PREMISE_INTEGRITY_HOLD_UNVERIFIED` | 尚不能「完全乾淨放行」，也不能判「論文已被證偽」 |

### 7.2 Lighter Final Gate 的真實狀態

**切勿寫成 `GATE DECISION: HOLD`。** 依 Lighter §L5.1-16，若 Gate 並未執行，狀態就是 `NOT_REACHED`／`UNEVIDENCED`，不是 Gate 曾裁定 HOLD。

```yaml
ACTUAL_EXECUTION:
  user_authorized_review: true
  source_read_and_sha_lock: true
  paper_r3_2_sde_rules_applied_in_review: true
  computational_probe_N1: EXECUTED
  computational_probe_N2: EXECUTED
  python_output_recorded: true
  lean_kernel_or_comparator_rerun: NOT_EXECUTED
  official_governing_cycle_ref: NONE_VERIFIED
  actual_lighter_main_invocation: NONE_VERIFIED
  main_emission_evidence: NONE
  lighter_main_admission_receipt: NONE
  official_O9_activation_decision: NONE
  official_I9_receipt: NONE
  official_R_CCC_qualified_winner: NONE
  lighter_final_gate_execution: NOT_REACHED
  lighter_final_gate_decision: NONE
  release_receipt: NONE
  review_work_product_status: COMPLETED_REFERENCE_LEVEL_FULL_CYCLE
  formal_runtime_certification_status: NOT_ESTABLISHED
```

### 7.3 本次最短核心結論

**我未發現足以判定 OpenAI 論文已發生「前提置換／概念置換」的確證；但也未驗證其幾何插值核心能在每條實際依賴中無污染地成立。**

SDE 審查最成功的地方，不是貼上錯誤標籤，而是阻止兩種相反的自我穩定化：

1. 不能因為作者有數百行幾何論證和 Lean 模組，就對未驗證深層引理作自動放行。
2. 不能因為負控制 rank 17/18，就忽略作者清楚寫出的附加權重條件，硬說找到反例。

對這篇文章，**邏輯完整性應維持未核定**，而不是「已乾淨」或「已污染」。

---

## 8. 尚需執行的真正外部核驗與觸發條件

按研究優先順序：

1. **獨立 Lean kernel/Comparator**：使用公開工具鏈與該倉庫的版本，取得可重現的 build 日誌、`#print axioms OAI.PiExponent.main` 結果（確認是否只有允許的 axioms）、solution 模組與 selected statement 的 Comparator 實際執行紀錄。這裡需要合適的建置環境與大量模組依賴；本次無此證據。
2. **S2 幾何橋樑的針對性數學審計**：逐項檢查 local multiplicity 切片及 weighted Bézout、persistent derivative components、curve inequality、blow-up/ordinary Rees、nef→ample→jet surjectivity 是否正確處理所有權重、分枝與 H 的量詞。
3. **Lean vs natural proof 逐引理映射**：不只比較 theorem 名稱，核對量詞、真正 hypotheses、承諾的作用域及是否借用了更強的未揭示前提。
4. **作者或獨立數學專家反證**：若有人給出有效具體步驟或新修訂，從第一個失效節點回溯／向下傳播，再重新形成 R3+ material event。未完成的工作不得填成「測試通過」。
5. **Lighter／Main 正式事件**：只有真實 Host owner invocation/return/admission/gate 可提供 qualified runtime receipt，不能用本文自動升級。

---

## 9. 反向審查理火自己：可能的審查 SDE

**本輪最值得留下的教訓**：如果審查員原本深信「OpenAI 必然偷換前提」，看到一個 rank-deficient 的玩具矩陣，便在忽略「weight lower threshold 與 H sufficiently large」後宣布找到反例，審查員自身就製造了**非法前提置換**，並可能經由後續報告持續放大。N2 專門作為防止這項審查污染的負控制。

這並不能證明 SDE 理論為真，也不能證明論文為真；它是可重製的程序級自我糾錯案例。

---

## 10. 核驗與發布狀態

- 所有 OpenAI 原始碼引用連到公開原始路徑，blob SHA 在本次 GitHub fetch 已核對。
- 專案核心規範的 SHA-256 以實際載入之檔案位元組計算，不使用單憑文件名稱的推測。
- N1/N2 使用本次在 Python/ SymPy 執行之可重製腳本及 stdout；未冒充 Lean。
- 此報告在本次對話交付給人類審查；**未推送對外 GitHub、未宣稱 formal Host Final Release**。
- 如日後獨立 kernel/數學檢核完成，應保留本報告為前版證據，不得覆寫成「當日已完成」。

**結案類型：** `REFERENCE_LEVEL_REVIEW_WORK_COMPLETED` + `PAPER_PREMISE_INTEGRITY_HOLD_UNVERIFIED` + `LIGHTER_FINAL_GATE_NOT_REACHED`。
