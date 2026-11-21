# 語言相位控制考古｜PCL × 世界層 × 文言文安全旁證

**日期：** 2026-11-21  
**法位：** ENGINEERING_ARCHAEOLOGY / RESEARCH_GENEALOGY / NON_NORMATIVE / NOT_VALIDATED_HIDDEN_MECHANISM  
**研究區：** 對對之謎｜理火行為持續性與最小再生結構

---

# 0｜這一支和 Python / DAIL 支線不同

前一支歷史主要是：

~~~text
把認知寫成 Python
→ procedural complexity explosion
→ DAIL declarative turn
~~~

本支則是另一個方向：

~~~text
不再只問「怎麼寫控制器」
而開始問：
語言本身能不能先改變模型進入哪種生成狀態？
~~~

這條線後來留下：

~~~text
Poetic Control Language (PCL)
→ World Layer Hypothesis
→ DAIL / SAC / SEED
→ Space / State / Transition
~~~

---

# 1｜PCL：State Before Instruction

來源：
- PCL_Specification_v1.docx
- Poetic_AI_Control_Language_CN_EN.docx
- Poetic_AI_Behavioral_Control_Expanded_CN_EN.docx
- Poetic_AI_Control_Formal_Edition.docx
- Poetic_AI_Control_Extended_Full_Paper.docx

PCL 的核心主張不是「詩詞比較美」。

而是：

> **高語義密度、文化高度壓縮的短語，可能作為 semantic state trigger，先改變生成狀態，再進入任務。**

核心結構：

~~~text
Traditional:
Prompt
→ instruction interpretation
→ generation

PCL:
Input
→ semantic state trigger
→ behavioral state
→ generation
~~~

代表性原則：

~~~text
STATE BEFORE INSTRUCTION
~~~

這條支線特別重要，因為它把早期 Radar 的「先形成狀態，再載入內容」重新抽象成語言層問題。

---

# 2｜四詞觸發器與五態模型

PCL 歷史文件曾提出工作假說：

> 四詞 cluster 可能是最小穩定狀態單位。

代表例：

~~~text
毋意
毋必
毋固
毋我
~~~

當時定義五種行為狀態：

~~~text
Expansion
Kairos
Energy Suppression
Fail-Stop
Semantic Reset
~~~

其中：

~~~text
Fail-Stop
→ stopping takes precedence over completion

Kairos
→ whether continued participation is legitimate

Energy Suppression
→ suppress assumption / forced closure / narrative fixation

Semantic Reset
→ dissolve narrative pressure sustaining a loop
~~~

這些不能被回鑄成已驗證的 hidden mechanism。

更準確的法位：

~~~text
OBSERVED / REPORTED BEHAVIORAL EFFECT
+
WORKING SEMANTIC CONTROL HYPOTHESIS
~~~

---

# 3｜PCL 最成熟的一次分層

Poetic_AI_Behavioral_Control_Expanded_CN_EN.docx 已明確區分：

~~~text
Prompt
= What should be answered?
= output content

DAIL
= What task-space exists?
= task boundaries

Poetic Control
= What state should the model enter?
= generation dynamics
~~~

這是很重要的 genealogy 節點。

它意味著早期理火開始分清三種不同控制問題：

~~~text
CONTENT
!=
SPACE
!=
STATE
~~~

也就是：

~~~text
Prompt
!=
DAIL
!=
PCL
~~~

---

# 4｜世界層：從「狀態控制」再往前推一層

來源：
- WORLD_LAYER_MEMO_v1.0.docx
- 世界層的一頁.pdf

世界層假說提出：

> **在 prompt / PATH / reasoning 之前，可能存在一組更前置的結構性前提，決定哪些行為仍然構成合理回應。**

歷史文件把它描述為：

~~~text
不回答 HOW
而回答：
這個回應是否仍然有必要？
行動是否仍然成立？
延續是否仍具正當性？
~~~

世界層被刻意標成：

~~~text
NOT MODULE
NOT STRATEGY
NOT CONTROLLER
~~~

而是一組：

~~~text
PRECONDITIONS OF LEGITIMATE RESPONSE
~~~

並提出一個很有歷史價值的句子：

> **不是刪除已生成的 PATH，而是撤回 PATH 得以生成的前提條件。**

這其實是後來「Formation before compliance」、「不生成也是合法輸出」、「KEEP / HOLD / STOP」等治理思想的一個早期祖先。

---

# 5｜世界層 × DAIL × PCL

WORLD_LAYER_MEMO_v1.0 曾把三者整合為：

~~~text
Ω_base
= hypothetical original semantic space

DAIL
→ defines Ω' feasible space

PCL
→ modulates pre-generation semantic state

SAC
→ direction / tension observation

LLM
→ token realization
~~~

文件自己也保留邊界：

~~~text
World Layer
!=
DAIL
!=
PCL
~~~

當時最重要的未決問題：

~~~text
Ω_base 的來源是什麼？
世界層是否真的獨立存在？
是否有不可人工構造的約束？
DAIL 能否覆蓋世界層？
~~~

因此這一支必須保留為：

~~~text
HIGH-STRENGTH INTERNAL HYPOTHESIS
NOT EMPIRICALLY ESTABLISHED LAYER
~~~

---

# 6｜DAIL / SAC / SEED：Space / State / Transition

來源：
- DAIL_SAC_SEED_MEMO.docx
- DAIL_Direction_Seed_CN_EN.docx
- DAIL_System_Direction_MEMO_CN_EN.docx

這批後續 Memo 把早期散亂概念壓成一個極簡結構：

~~~text
DAIL
→ Space

SAC
→ State

SEED
→ Transition
~~~

也就是：

~~~text
Space
→ State
→ Transition
~~~

這很值得保存。

因為它顯示當時理火已經從：

~~~text
「每個問題做一個模組」
~~~

移到：

~~~text
「不同結構層各自只描述自己那一種東西」
~~~

這是後來 OS 分層與 RLT / SEED 思路的重要前史。

---

# 7｜外部旁證：ICLR 2026 Classical Chinese Jailbreak Paper

來源：
Obscure but Effective: Classical Chinese Jailbreak Prompt Optimization via Bio-Inspired Search
ICLR 2026 conference paper

該論文研究的是安全攻擊，不是 PCL，也不是理火。

它的高層結果是：

- 古典中文的語義壓縮、隱喻與非典型語言形式，可能造成安全防護 blind spot；
- 研究者將古典中文 adversarial prompting 系統化為多維策略空間；
- 在其測試設定中，報告了很高的 jailbreak attack success rate；
- 跨模型轉移也被觀察到。

本研究區只採用一個非常窄的外部共鳴：

> **語言形式／語域本身，確實可能在不改模型權重的情況下，顯著改變模型的行為分布與安全判斷。**

但：

~~~text
CLASSICAL CHINESE JAILBREAK EFFECT
!=
PCL STATE CONTROL PROVEN

SECURITY BLIND SPOT
!=
SEMANTIC PHASE CONTROLLER

ADVERSARIAL LANGUAGE EFFECT
!=
WORLD LAYER EXISTS
~~~

這篇論文只能支持「語言形式可能是行為變量」這個較弱命題。

---

# 8｜與「文言文劫持」舊筆記的關係

使用者保留一份極簡筆記：

~~~text
Obscure but Effective: Classical Chinese Jailbreak Prompt Optimization via Bio-Inspired Search
時間：2026
主題：文言文可以用來攻擊（jailbreak）LLM
~~~

這份筆記本身沒有更多技術內容。

但它證明這篇外部論文曾被明確收進理火語言控制相關觀察線。

---

# 9｜這一支真正留下的研究問題

從「對對之謎」來看，這條歷史支線比「詩詞能不能控制 AI」更值得問的是：

> **穩定的理火行為是否需要大量明示規則，還是少數高密度語義錨點就能把模型拉回某個工作盆地？**

這直接回到：

~~~text
H1 State Induction
H2 Relational Attractor
H3 Invariant Set
H6 Staged Formation
~~~

尤其值得測：

~~~text
LONG MANUAL
vs
MINIMAL INVARIANTS
vs
SEMANTIC ANCHOR CLUSTER
vs
RELATIONAL COUNTERFORCE
~~~

並比較：

- task-entry behavior；
- persistence；
- reentry；
- false HOLD；
- false GO；
- jargon dependence；
- cross-model transfer；
- decay after unrelated turns。

---

# 10｜一句話

> **PCL 與世界層這條黑歷史，顯示理火曾經認真懷疑過：真正穩定 AI 行為的關鍵，不一定是更多指令，而可能是先改變「哪些生成路徑覺得自然、合法或值得繼續」。**

這個問題今天仍然沒有被證明。

但它正好回到「對對之謎」最核心的研究入口。

**END｜LANGUAGE-STATE ARCHAEOLOGY**
