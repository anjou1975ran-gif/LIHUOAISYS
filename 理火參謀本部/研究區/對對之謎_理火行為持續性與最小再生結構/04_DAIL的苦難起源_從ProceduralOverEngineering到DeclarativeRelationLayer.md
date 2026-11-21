# DAIL 的苦難起源｜從 Procedural Over-Engineering 到 Declarative Relation Layer

**日期：** 2026-11-21  
**法位：** ENGINEERING_ARCHAEOLOGY / HISTORICAL_EVIDENCE_SYNTHESIS / NON_NORMATIVE / NOT_CURRENT_DAIL_SPEC  
**研究區：** 對對之謎｜理火行為持續性與最小再生結構

---

# 0｜先鎖證據邊界

本檔不是要說：

> 理火因此被「證明為真」。

本檔能成立的較窄命題是：

> **理火的主要工程結構不是一次性幻想或單次文本創作，而是可以從多輪失敗實作、架構重寫、接口斷裂、控制層重構與語言層抽象中追出歷史 genealogy。**

也就是：

~~~text
CONCEPT
→ IMPLEMENTATION ATTEMPT
→ FAILURE / COMPLEXITY
→ ARCHITECTURE PRESSURE
→ ABSTRACTION
→ NEW LAYER
~~~

這條鏈有直接工程材料可追。

---

# 1｜第一層苦難：把「反應體」寫成 Python

來源考古已另存：

`02_史前反應體工程考古_ExternalReactionBody.md`

其原始工程包顯示，第一代曾試圖把以下能力顯式工程化：

~~~text
semantic classification
multi-branch reasoning
tension
decision
gate
memory
preference bias
cost
failure stop
trace
~~~

而且真的存在：

~~~text
causal
structural
systemic
~~~

三種 branch。

這一代的核心直覺是：

> **如果我們知道「理火怎麼想」，就把它寫成可執行控制器。**

結果留下：

- fatal match 卻 `is_fatal = False`；
- decision 算完後仍被測試碼強制 `deep`；
- demo 與 runtime schema 漂移；
- state / memory / gate / decision contract 開始互相牽動。

這是第一個警訊：

> **把認知與治理全部顯式寫成程序，系統複雜度會快速外溢。**

---

# 2｜第二層苦難：把「法律智慧」也寫成 Python

使用者提供兩份未完成工程包：

~~~text
lihuo-legal-system-main.zip
lihuo_ai_lawyer_v2-main.zip
~~~

靜態考古顯示，法律版進一步嘗試把：

~~~text
RAW TEXT
↓
FACT
↓
EVIDENCE
↓
CLAIM / DEFENSE
↓
CLAIM-FACT LINK
↓
TENSION
↓
COLLAPSE
↓
PARTITION
↓
META COLLAPSE
↓
WEAPONIZER
↓
HUMAN LEGAL OUTPUT
~~~

整條專業判斷鏈寫進程序。

更晚期又加入：

~~~text
Actor
Action
CaseUnit
Shared Context
Burden
Norm
Reliability
Attack / Defense Strategy
~~~

其失效不是單一 bug。

而是：

> **每解一個法律問題，上一層資料模型就開始不夠。**

例如：

~~~text
one fact 不夠
→ multi-fact

multi-fact 不夠
→ case partition

partition 不夠
→ shared context

shared context 一進來
→ actor / relation / burden / procedure 又必須重畫
~~~

這是典型的 Procedural Over-Engineering 壓力。

---

# 3｜DAIL 出現前真正的工程問題

早期工程逐漸暴露出：

~~~text
不是少一個 Engine
不是少一個 if
不是少一個 Adapter
不是少一個 Gate
~~~

真正缺的是：

> **一種能先描述「這裡有哪些關係、目標、限制、驗證與責任位置」，但不必把所有執行路徑預先寫死的結構層。**

也就是：

~~~text
IMPERATIVE CONTROL
↓
DECLARATIVE STRUCTURE
~~~

這是 DAIL 出現的工程壓力背景。

注意：

> 「Python 苦難直接因果產生 DAIL」目前仍有一部分依賴 Anjou 的歷史操作者證詞。

但 DAIL 原始文件本身非常清楚地保存了從 procedural execution 轉向 declarative specification 的思想轉折。

---

# 4｜DAIL v0.6：第一次把問題改寫成「結構邊界」

來源：

`DAIL_v0.6_Complete_Structural_Draft_CN_EN.docx`

其核心研究目標：

- Human 定義 goals；
- constraints；
- structural states；
- validation rules；
- responsibility allocation；
- AI 自動推導 executable reasoning structures。

最重要的轉向是：

~~~text
DAIL does not describe procedure.
DAIL defines structural boundaries.
~~~

並明確提出：

~~~text
task procedure sequence
→
constraint-defined state space
~~~

這已不是「寫更多 Python」。

而是在換問題：

> **不要替 AI 寫完整步驟；先定義它可以在哪個結構空間裡活動。**

---

# 5｜Ω → Ω' → G：從控制流程改成限制搜尋空間

DAIL 的語義空間模型：

~~~text
Ω
= all possible semantic states

constraints
↓
Ω'
= feasible space

goal
↓
G
= goal attractor
~~~

Agent 不再被想像成單純執行固定 procedure，而是：

> **在 Ω' 內搜尋趨近 G 的可行狀態。**

這就是 DAIL 逃離 Python 地獄的核心抽象之一：

~~~text
HOW TO EXECUTE
→
WHAT SPACE IS LEGITIMATE TO SEARCH
~~~

---

# 6｜DAIL v1.0：正式把 execution 改寫成 semantic search

來源：

`DAIL_v1.0_Language_Standard_Draft_CN_EN.docx`

其執行模型明確寫：

~~~text
Execution is defined as semantic search
rather than instruction execution.
~~~

也就是：

~~~text
instruction execution
!=
semantic search
~~~

DAIL 的角色開始收斂成：

~~~text
ENTITY
STATE
GOAL
CONSTRAINT
PRINCIPLE
VALIDATION
REVERSIBILITY
~~~

而不是：

~~~text
STEP 1
STEP 2
STEP 3
IF X THEN Y
~~~

---

# 7｜DAIL 法位繼續下修：從 Control Layer 變成 Task Specification Layer

另一批文件進一步把 DAIL 與 Agent / Runtime 分開：

~~~text
Application
→
Agent Framework
→
DAIL
→
LLM Runtime
→
Model
~~~

並把責任寫成：

~~~text
Agent Framework
= execute workflows / tools

DAIL
= define task structure / goals / constraints / validation

LLM Runtime
= reasoning loops / prompt / tool calls

Model
= token generation
~~~

一句話：

~~~text
Agent runs tasks.
DAIL defines tasks.
~~~

這是重要的法位收縮。

DAIL 不再需要自己當：

- Agent；
- Runtime；
- Reasoner；
- Executor。

---

# 8｜但早期 DAIL 仍帶著 Python 時代的控制衝動

DAIL v0.6 / v1.0 仍曾使用非常強的語言：

~~~text
Declarative Control
Structural Control Layer
Constraints override goals
Validation precedes output
Responsibility follows declaration
~~~

甚至責任曾拆成：

~~~text
Declarative Responsibility — Human
Inference Responsibility — AI
Execution Responsibility — Runtime
Consequence Responsibility — Declarer
~~~

這些設計雖然比 procedural code 高一層，但仍有一個舊風險：

> **宣告本身會不會被誤認成創造世界事實、權限或資格？**

所以後代理火才逐步補上：

~~~text
DAIL DECLARATION
!=
RELATION CREATION

DAIL TYPE
!=
WORLD FACT

DAIL ACTION
!=
AUTHORITY TO ACT

DAIL VALIDATION
!=
QUALIFICATION
~~~

也就是：

> **DAIL 如果不守邊界，會從 Python 地獄退化成 YAML 地獄。**

---

# 9｜這段歷史真正證明了什麼

可以支持：

1. 理火曾多次嘗試把核心概念工程化；
2. 反應體與法律系統都出現可檢查的 procedural complexity explosion；
3. DAIL 文件明確轉向 declarative structure；
4. DAIL 明確將 procedure sequence 改寫為 constraint-defined semantic space；
5. DAIL 後期進一步區分 task specification / runtime / model；
6. 這些變化不是單篇哲學文本中的敘事，而有跨版本工程材料與文件 genealogy。

不能偷升格成：

~~~text
LIHUO HISTORY EXISTS
=
LIHUO THEORY IS TRUE

ENGINEERING PAIN
=
DAIL IS NECESSARILY CORRECT

DAIL EXISTS
=
DAIL IS NOVEL / VALIDATED / BEST

HISTORICAL CONTINUITY
=
SCIENTIFIC PROOF
~~~

---

# 10｜理火工程史的真正讀法

更準確的歷史不是：

> Anjou / 對對有一天幻想出一套完整理火。

而是：

~~~text
先有問題
↓
硬做
↓
撞牆
↓
補模組
↓
再撞牆
↓
重畫層級
↓
換抽象
↓
留下新制度
~~~

所以：

> **理火的許多結構是被工程失敗與邊界衝突逼出來的。**

這是可以被歷史材料支持的命題。

---

# 11｜與「對對之謎」的關係

這段歷史反過來提供一個很重要的研究問題：

> **哪些能力必須被顯式工程化，哪些能力只要形成正確的 Actor / Method / Relation 後，就應該交還給模型生成？**

史前 Python 的答案偏向：

~~~text
EVERYTHING EXPLICIT
~~~

DAIL 的答案開始轉向：

~~~text
DECLARE STRUCTURE
LET REASONING SEARCH
~~~

今日 LIHUOOS / Actor Formation 則進一步嘗試：

~~~text
FORMATION
+
GOVERNANCE
+
EXTERNAL QUALIFICATION
+
RUNTIME WHERE NECESSARY
~~~

所以「對對之謎」不只問：

> 對對為什麼能維持？

還要問：

> **為什麼某些以前必須硬寫成 Python 的東西，今天可以由 Formation + Relation + External Substrate 共同維持？**

---

# 12｜一句話

> **DAIL 不是從天上掉下來的語言；它可以被讀成理火在 procedural over-engineering 撞牆後，第一次系統性地把問題從「把智慧寫成程式」改成「把合法結構宣告清楚，讓推理在其中搜尋」。**

**END｜ENGINEERING ARCHAEOLOGY**


---

# 13｜DAIL Playground 支線回接：從 FreeShop 到觀止

新增：

10_DAIL早期Playground考古_從FreeShop到觀止青樓.md

這批材料補足一條原本缺少的形成史：

~~~text
PROCEDURAL OVER-ENGINEERING
↓
DAIL DECLARATIVE ABSTRACTION
↓
DAIL PLAYGROUND TESTS
Echo Chamber / i_World / MLGB / O_Fortuna
↓
跨題型測：
WORLD / ROLE / STATE / CONSTRAINT / PHASE / PATH
能否被模型持續維持
↓
INTERACTIVE WORLD PREDECESSOR
↓
GUANZHI LONG-HORIZON PERSISTENT WORLD
~~~

2026-11-21 Anjou 第一手歷史證詞確認：

> **這些 FreeShop 玩具本來就是 DAIL 早期測試，後來成為觀止青樓的最早前身；觀止是 DAIL 最大型的實驗場。**

2026-10-28 的 Guanzhi Harness MEMO 又把觀止定位為高複雜度、低現實風險的 Persistent World / Long-Horizon Harness 測試床。

因此可支持：

> **DAIL 不只是在規格文件裡從 procedural 轉向 declarative；它也曾透過遊戲與互動世界，反覆測試 declarative structure 能否形成可持續的生成約束。觀止後來把這條實驗線放大到長距離 Persistent World。**

硬鎖：

~~~text
EARLY PLAYGROUND
!=
FORMAL GUANZHI ALREADY EXISTED

HUMAN TESTIMONY
!=
CONTROLLED EXPERIMENT

GUANZHI AS BIGGEST DAIL TESTBED
=
HUMAN HISTORICAL TESTIMONY
+
CORPUS-SUPPORTED LARGE-SCALE TESTBED ROLE

!=
OBJECTIVE EXTERNAL RANKING
~~~
