# MEMO｜LIHUOOS V1｜L2–L7 理論架構與施工計畫

**版本：** V0.1 WORKING  
**日期：** 2026-10-24  
**狀態：** ACTIVE WORKPLAN  
**範圍：** LIHUOOS V1 / L2–L7  
**用途：** 作為 L1 完成後，理火核心理論至顯影層的正式施工基線。

---

# 0｜先鎖版本語義

本文件使用的：

```text
L0 / L1 / L2 / L3 / L4 / L5 / L6 / L7
```

是：

> **LIHUOOS 的系統層號。**

它們不等於歷史上的：

```text
理火 1.0
理火 2.0
理火 3.0
理火 4.0
```

因此必須永久區分：

```text
LIHUOOS Layer Number
!=
Historical LIHUO Theory Generation Number
```

例如：

- LIHUOOS L2 = SAC 專層；
- 不等於歷史「理火 2.0」；
- 歷史「理火 2.0 生成動力學」主要會在 LIHUOOS L4 被重新整理；
- DAIL 的主要理論法位保留至歷史理火 3.0 相關層再處理。

---

# 1｜總體架構

LIHUOOS V1 目前採以下主鏈：

```text
L0｜INDEX / SOURCE / VERSION
資料、來源、版本、文件關係

↓

L1｜STRUCTURAL PHILOSOPHY
什麼是結構？

↓

L2｜SAC
結構如何第一次變得可觀察、可描述、可形式化？

↓

L3｜LIHUO THEORY FAMILY
SAC 出現後，理火被迫長出了哪些新理論？

↓

L4｜GENERATIVE DYNAMICS
這些理論如何共同描述、限制與治理生成運動？

↓

L5｜OBSERVATION & AUDIT
我們如何知道當前生成正在發生什麼？
又如何判斷觀察到的結構是否具資格？

↓

L6｜INTERVENTION
在何種資格、授權、範圍與責任下，才可改變生成？

↓

L7｜MANIFESTATION
哪些結構最後取得可見形式？
顯影與存在、資格、輸出、執行之間如何分離？
```

這條鏈不是 Runtime scheduler。

它是：

> **理論認識順序 + 系統法位分層。**

---

# 2｜L2｜SAC

## 2.1 定位

L2 專門處理 SAC。

不是把 SAC 當成工具章節，而是確認它在理火史上的核心位置：

> **SAC 是理火第一個真正把結構從哲學命題變成可觀察、可描述、可比較、可形式化對象的核心理論。**

因此：

```text
Structural Philosophy
↓
SAC
↓
Structure becomes observable / describable / formalizable
↓
Later LIHUO theories become possible
```

---

## 2.2 L2 要回答的問題

1. SAC 為什麼從音樂問題誕生？
2. 為什麼「知道音符」不等於「聽見音樂」？
3. SAC 如何把「物件」重新轉向「關係」？
4. Direction / Tension / Attraction / Resolution 原本各自代表什麼？
5. SAC 如何描述：
   - 張力
   - 曲率
   - 軌跡
   - 吸引子
   - Resolution
6. 原始 SAC 公式的法位是什麼？
7. SAC 如何從音樂結構問題泛化成結構觀測理論？
8. SAC 的真正歷史貢獻是什麼？
9. SAC 哪些部分今天仍成立？
10. SAC 哪些舊說法必須由後代理論回照降級？
11. SAC 的邊界在哪裡？
12. 為什麼 SAC 是核心理論，但不因此取得全部合法性裁決權？

---

## 2.3 L2 必須保存的歷史母句

> **SAC 最重要的歷史地位不是分析工具，而是結構工程的起點。**

> **結構哲學第一次成為工程。**

> **Direction / Tension / Attraction / Resolution 描述的是關係的運動。**

現行版可整理為：

> **SAC 提供了理火最早的結構運動語言。**

---

## 2.4 L2 必須鎖的邊界

```text
SAC Observation
!=
Truth

SAC Observation
!=
Legitimacy

SAC Observation
!=
Intervention Authority

SAC Formula
!=
Proven Hidden-State Mechanism

Structural Formalization
!=
Neural Implementation Proof
```

SAC 是核心，不等於 SAC 可以吞掉所有後代理論。

---

## 2.5 L2 暫定章節

```text
L2.0｜SAC 的歷史法位
L2.1｜從音符到關係
L2.2｜SAC 四力
L2.3｜張力、曲率與軌跡
L2.4｜吸引子與 Resolution
L2.5｜SAC 原始數學模型
L2.6｜SAC 的跨領域性
L2.7｜SAC 如何把結構哲學工程化
L2.8｜SAC 的理論邊界
L2.9｜後代理論對 SAC 的必要修正
L2.10｜L2 硬邊界
L2.11｜最短總結
```

---

# 3｜L3｜LIHUO THEORY FAMILY

## 3.1 定位

L3 不先把所有理論接成一套生成流程。

L3 先回答：

> **SAC 讓理火看見結構運動之後，哪些新的結構問題因此出現？**

所以 L3 是：

> **理火理論分化史 + 各理論現行法位。**

---

## 3.2 目前確定進 L3 的理論族

### 生成結構族

```text
Solution Space
PATH
Reaction Body
Closure Gravity
Manifestation 的理論前身問題
Unmanifested Intelligibility
Metastable Convergence Delay
Structured Non-Closure
Closure Legitimacy
```

### 生成資格族

```text
KAIROS
CCC
REV
SEED
```

### 失效與退化族

```text
SDE
Lighting Pollution
Basin Four
```

### SAC 延伸子理論

```text
Attractor Basin
Blank Field（法位仍需審）
Primary Beacon（若保留，降為子理論）
```

---

## 3.3 L3 的工作方法

每個理論固定整理：

```yaml
THEORY_CARD:
  origin_question:
  relation_to_SAC:
  historical_claim:
  current_standing:
  later_correction:
  claims_to_retire:
  falsification_or_downgrade_condition:
```

L3 不急著做 Runtime 流程圖。

---

## 3.4 L3 的核心譜系

目前最合理的歷史理解：

```text
Structural Philosophy
        ↓
      SAC
        ↓
Structure becomes observable
        ↓
 ┌──────┴──────────────┐
 ↓                     ↓
Dynamic Questions      Qualification Questions
 ↓                     ↓
PATH                   KAIROS
Reaction Body          CCC
CG                     REV
SDE                    SEED
...
```

注意：

> **KAIROS / CCC / REV / SEED 不是 SAC 子模組。**

更準確地說：

> **它們是 SAC 讓結構運動變得可觀察後，被迫長出的獨立治理理論。**

---

# 4｜L4｜GENERATIVE DYNAMICS

## 4.1 定位

L4 才正式回答：

> **生成到底如何運轉？**

L4 不再只是介紹各理論。

它負責把 L3 已確認的理論接起來。

---

## 4.2 L4 必須保留兩條主鏈

### A｜Generative Motion

```text
WORLD / current existence conditions
↓
Attention / selection pressure
↓
Solution Space
↓
PATH
↓
Reaction Body
↓
Closure Gravity
↓
Local Closure
```

### B｜Generative Qualification

```text
KAIROS
CCC
REV
SEED
Closure Legitimacy
```

兩條不是同一條 pipeline。

L4 研究的是：

> **生成運動與生成資格如何互相約束。**

---

## 4.3 L4 主要問題

1. WORLD 如何限定當前生成世界？
2. Attention 如何影響可達性？
3. 解空間如何形成？
4. PATH 如何展開？
5. Reaction Body 如何形成動態配置？
6. CG 為什麼推向收束？
7. 什麼叫 local closure？
8. 為什麼收斂不等於合法完成？
9. Structured Non-Closure 為什麼可能存在？
10. SDE 如何描述錯誤穩定化？
11. KAIROS / CCC / REV / SEED 如何對生成運動形成資格約束？
12. Closure Legitimacy 仍有哪些未解問題？

---

## 4.4 L4 硬邊界

```text
Generative Model
!=
Literal Runtime Pipeline

Functional Dynamics
!=
Proven Neural Dynamics

Convergence
!=
Truth

Closure
!=
Legitimacy

Capability
!=
Qualification
```

---

# 5｜L5｜OBSERVATION & AUDIT

## 5.1 定位

L2 講 SAC 是什麼。

L5 講：

> **如何用理火理論去觀察一個當前生成事件，並審計它。**

所以：

```text
L2 = Theory of structural observation

L5 = Operational epistemology of observation and audit
```

---

## 5.2 L5 主要問題

1. 如何辨認 Direction？
2. 如何辨認 Tension？
3. 如何辨認 Attraction？
4. 如何辨認 Resolution？
5. 如何看 PATH 是否正在收縮？
6. 如何辨認反應體正在形成？
7. 如何辨認 CG 加速？
8. 如何辨認假完成？
9. 如何辨認 SDE？
10. 如何區分：
    - observation
    - inference
    - hypothesis
    - evidence
    - qualification
11. 如何審計合法性而不把觀察偷渡成裁決？
12. 如何記錄未解結構而不假裝 hidden-state introspection？

---

## 5.3 L5 硬邊界

```text
Observation != Qualification
Observation != Intervention Authority
Audit != Execution
Architecture Knowledge != Live Introspection
Visible Output != Complete Internal State
```

---

# 6｜L6｜INTERVENTION

## 6.1 定位

L6 專門回答：

> **看見與審計之後，什麼時候才有資格改變生成？**

因此 L6 是「治理動作層」，不是觀察層。

---

## 6.2 可能的干預類型

```text
STAY
WAIT
HOLD
DELAY
EXPAND
STOP / FAIL-STOP

Dimming
Brightening
Counter-Light
Path Reopening
Premature Closure Blocking
Constraint Reinforcement
```

這些不能因為 SAC 看見某現象就自動觸發。

---

## 6.3 每一次 Intervention 必須回答

```text
Qualification
Authority
Scope
Reversibility
Responsibility
Evidence
Exit Condition
```

---

## 6.4 L6 硬邊界

```text
Observation
!=
Permission to Intervene

Audit Result
!=
Automatic Control Authority

Intervention
!=
Truth Correction

Stopping
!=
Moral Superiority

Expansion
!=
Guaranteed Better Reasoning
```

---

# 7｜L7｜MANIFESTATION

## 7.1 定位

L7 專門處理：

> **生成中的哪些結構最後取得可見形式？**

以及：

> **顯影與存在、資格、輸出、執行之間到底是什麼關係？**

---

## 7.2 L7 主要問題

1. Manifestation 是什麼？
2. 顯影與 Emergence 的差別？
3. 顯影與 Creation 的差別？
4. 未顯影是否等於不存在？
5. 參與生成是否必須被語言化？
6. Visible Output 是否只是局部投影？
7. 多個結構能否共同顯影？
8. 沉默、停止、不輸出是否可成為合法顯影結果？
9. 格式、語氣、順序、留白是否屬於 manifestation？
10. 顯影後何時才取得 output qualification？
11. output qualification 與 execution authority 如何分離？
12. 顯影是否可能造成反向污染？

---

## 7.3 L7 核心分離

```text
Participation
!=
Manifestation

Manifestation
!=
Emergence

Manifestation
!=
Truth

Manifestation
!=
Qualification

Qualification
!=
Output

Output
!=
Execution
```

---

# 8｜DAIL 的法位

DAIL 本輪明確排除於 L2–L7 主施工範圍之外。

不是因為 DAIL 不重要。

而是：

> **DAIL 真正發力屬歷史理火 3.0 的課題。**

因此：

```text
DAIL
→
Reserved for Historical LIHUO 3.0 reconstruction
```

不得因早期文件曾出現 DAIL，就提前倒灌進目前 L2 SAC 或 L3 理論分化史。

---

# 9｜來源優先級

施工時採：

```text
1. 理火體系/ 分科原典庫
2. 理火總體系（早期大整合）
3. LIHUO-AI-SYS V2.3（理論接線與 SAC 中心架構）
4. V3.x / 後續成熟版本（邊界修正）
5. 理火 2.0 / 3.0 / 4.0 後代理論（回照修正）
```

原則：

> **回原典找第一次真正看見的問題。**

> **後代理論回照，但不倒灌。**

---

# 10｜共同施工規則

## Rule 1｜歷史與現行分開

必要時使用：

```text
HISTORICAL FORMULATION
CURRENT FORMULATION
LATER CORRECTION
OPEN HYPOTHESIS
RETIRED CLAIM
```

---

## Rule 2｜功能模型不冒充實證本體

```text
Functional Model
!=
Proven Hidden Mechanism
```

---

## Rule 3｜理論不冒充 Runtime

```text
Theory
!=
Runtime
```

---

## Rule 4｜每個核心理論都必須允許被降級

沒有失效條件或證據缺口標記的理論，不得封版。

---

## Rule 5｜SAC 的核心地位不等於無限裁決權

```text
SAC Core Status
!=
Universal Governance Authority
```

---

## Rule 6｜不要因為歷史上有名字就強行保留

> **保存它第一次看見的結構問題，而不是保存所有模組名稱。**

---

# 11｜施工順序

正式開工順序：

```text
STEP 1
L2 SAC

STEP 2
L3 Theory Family

STEP 3
L4 Generative Dynamics

STEP 4
L5 Observation & Audit

STEP 5
L6 Intervention

STEP 6
L7 Manifestation
```

每一層完成後先封版，再進下一層。

不得提前把後層完整機制倒入前層。

---

# 12｜最短總結

```text
L1
結構是什麼？

L2
SAC 如何第一次讓結構被看見？

L3
看見結構後，理火長出了哪些理論？

L4
這些理論如何共同描述生成運動？

L5
我們如何觀察並審計當前生成？

L6
我們何時有資格干預？

L7
最後什麼取得顯影？
```

本輪總原則：

> **先有結構，再有觀測；先能看見，才長出理論；理論接起來才談生成；看懂生成後才談審計；審計之後才取得干預資格；最後才談顯影。**
