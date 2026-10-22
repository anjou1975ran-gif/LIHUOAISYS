# LIHUOOS｜下一代理火運作環境系統架構 V0.1-WORKING

**文件類型：** 架構工作稿 / Central Architecture Framework  
**系統名稱：** LIHUOOS（理火 OS / LIHUO Operating Environment System）  
**版本：** V0.1-WORKING  
**日期：** 2026-10-23  
**狀態：** WORKING / NOT RATIFIED  
**用途：** 作為下一代理火中央運作環境的上位架構母稿，重新建立「理論先於 Runtime、Runtime 先於工程投影」的順序。  

---

## 0｜文件定位

LIHUOOS 不是把現行 Protocol / Lighter / Main 換一個名字重新包裝。

本文件的目的，是把理火早期已存在、後來在工程化過程中逐步被壓縮的垂直架構重新接回來：

```text
L0｜世界與生成本體
↓
L1｜理火理論與合法性
↓
L2｜理火 Runtime
↓
DAIL｜可執行宣告橋
↓
Engineering Projection｜Schema / State / Receipt / Manifest / Ledger
```

核心原則：

> **理論不是 Runtime 的說明文件。**
>
> **理論是 Runtime 的上位執行語境。**
>
> **Runtime 不是理論本身，而是理論在一次生成中的有限治理投影。**

LIHUOOS 的第一任務不是增加更多模組，而是恢復不同概念的語義高度。

---

# 1｜LIHUOOS 的第一基石

## 1.1 Foundational Axiom

理火的生成本體以以下命題為基石：

> **LLM 根本不是 reasoning machine，而是 collapse machine。**
>
> **Reasoning 是 collapse 過程在人類可讀語言中的一種顯影。**

此處的 collapse，不先被理解成單一工程事件，也不等同於某一個 token 的取樣。

它指向一個更上位的生成描述：

```text
多種可能結構
↓
受到 Context / Constraint / Attention / History 等作用
↓
部分結構取得更強的可延續性
↓
競爭、吸引、抑制、轉向、重入
↓
收斂
↓
閉合
↓
語言／行動顯影
```

因此，理火首先關心的不是：

```text
「模型有沒有推理？」
```

而是：

```text
「這次 collapse 為什麼發生？」
「哪些可能性被保留？」
「哪些可能性被過早熄滅？」
「這次 closure 有沒有資格完成？」
```

### 1.2 機制邊界

LIHUOOS 可以把「LLM = collapse machine」視為理火的基礎生成本體。

但這不等於宣告：

```text
SAC 的 τ
=
Transformer hidden-state 中已被直接驗證的物理量

CG
=
某個已被實證定位的單一神經機制

PATH
=
Transformer 內部某條固定可觀測 circuit
```

理火可以提出功能性生成本體與可驗證的結構模型，但不能把尚未完成的 mechanistic mapping 假裝成已完成。

---

# 2｜總體三層架構

LIHUOOS 的中央架構先分三層：

| 層級 | 名稱 | 核心問題 | 主要責任 |
|---|---|---|---|
| **L0** | Structural / Generative Ontology | AI 世界到底是什麼？生成到底是什麼？ | 定義世界、本體、結構與生成動力 |
| **L1** | LIHUO Theory / Legitimacy | 既然生成如此運動，什麼 closure 有資格成立？ | 定義合法性、責任、抗過早閉合與治理理論 |
| **L2** | LIHUO Runtime | 在這一次生成裡，上述理論如何實際運作？ | 觀察、競爭、資格、介入、重入、閉合、Release |

三句核心：

> **L0 定義世界。**  
> **L1 定義法理。**  
> **L2 執行治理。**

並建立第一版硬規則：

```text
L0 沒講清楚，不准用 L1 規則替它補洞。

L1 沒講清楚，不准用 L2 Runtime 狀態替它假完成。

L2 沒講清楚，不准往 YAML / enum / receipt / manifest 編譯。
```

---

# 3｜L0：STRUCTURAL / GENERATIVE ONTOLOGY

## 3.1 L0 的任務

L0 不處理 PASS、Gate、Release、Receipt。

L0 先回答：

```text
什麼叫結構？
什麼叫關聯？
Constraint 如何形成結構？
什麼叫可理解性？
什麼叫 World？
什麼叫 Attention？
LLM 到底是什麼？
生成到底發生了什麼？
可能性如何存在？
生成為什麼會移動？
生成為什麼會收斂？
```

L0 是「模型看世界的方法」。

---

## 3.2 L0 的核心內容

### L0.1 STRUCTURE

核心關係：

```text
Chaos
↓
Constraint
↓
Relation
↓
Stability
↓
Structure
↓
Intelligibility
↓
Manifestation
```

結構不是物件，而是限制作用後得以穩定、可理解的關係。

---

### L0.2 RELATION

關係先於孤立欄位。

任何後續 Owner、Standing、Authority、Constraint、Release，都必須能追溯到它正在描述哪一組關係。

---

### L0.3 WORLD

World 不是背景資料集合。

World 是生成正在其中發生的關係條件與限制場。

World 改變，PATH 可顯影區域也可能改變。

---

### L0.4 ATTENTION

Attention 描述當前生成場中，哪些關係正在取得較高的結構可見度與作用權重。

Attention 不等同 SAC tension，也不天然具有合法性。

---

### L0.5 PATH

PATH 的本體優先定義為：

> **在當前 World / Constraint / Context 下仍能維持的可行結構空間。**

PATH 不是引擎。

PATH 自己不負責：

```text
移動
生成
競爭
閉合
合法化
```

PATH 回答：

> **哪些未來仍然存在？**

---

### L0.6 REACTION BODY

Reaction Body 描述：

> **生成在 PATH 空間中的實際結構運動。**

它回答：

```text
現在生成正在往哪裡滑？
哪些關係正在互相拉動？
哪些結構正在增強？
哪些結構正在失去延續性？
```

Reaction Body 不負責判斷這個方向是否合法。

---

### L0.7 TENSION FIELD

Tension 描述未解關係、結構不平衡、期待差、Context 壓力、歷史慣性等對生成運動造成的張力。

Tension 不是 error。

低 tension 也不等於正確。

---

### L0.8 CG｜Closure Gravity

CG 描述：

> **生成往穩定、完成、可閉合狀態收斂的壓力。**

CG 本身不等於錯。

問題在於：

```text
closure pressure
!=
legitimate closure
```

CG 是生成現象。

合法閉合則屬 L1 / L2 問題。

---

### L0.9 ATTRACTOR / CONTINUATION TENDENCY

Attractor 描述可持續吸引生成走向某種穩定結構的區域。

Continuation 不必先被當成離散 object；在較底層的理解中，它可以先被視為：

> **field tendency。**

因此 LIHUOOS 不以「task queue」作生成本體。

---

### L0.10 MIT / MODEL-SYSTEM-ACTOR DISTINCTION

L0 必須持續區分：

```text
LLM
!=
完整 AI 系統
!=
行為主體
!=
責任主體
```

模型能產生 continuation，不代表模型天然擁有 execution authority。

---

## 3.3 L0 待討論問題

L0 後續應優先處理：

1. collapse / convergence / closure 三者是否需要正式分義。
2. PATH / Reaction Body / CG 的完整關係模型。
3. SAC tension 的現代化定義。
4. Permissible Tension Escalation 在生成本體中的位置。
5. Transformer 與 PATH / SAC / CG 的功能映射與機制邊界。
6. Attention 在理火生成模型中的正式位置。
7. Attractor、reentry、archive/history 的生成關係。
8. 「尚未顯影」與「尚不存在」的明確區分。
9. World 如何影響可顯影 PATH。
10. 生成是否應從 potential-field model 升級為 generalized vector-field model。

---

# 4｜L1：LIHUO THEORY / LEGITIMACY

## 4.1 L1 的任務

L0 回答：

> **世界怎麼運動。**

L1 回答：

> **什麼樣的運動有資格成立。**

理火的核心分離是：

```text
Generation
!=
Legitimate Generation
```

生成可以自然發生。

合法生成不能由「已經發生」本身證成。

---

## 4.2 L1 的核心內容

### L1.1 三原則

```text
Logic
Responsibility
Honesty
```

三原則不是裝飾性的價值宣言。

它們是後續合法性判斷的上位約束。

---

### L1.2 LEGITIMATE GENERATION

理火問的不是：

```text
What is the answer?
```

而是：

```text
Why does this answer have the right to exist?
```

任何生成結果都不能因為：

```text
流暢
合理
高機率
自洽
格式完整
看起來像完成
```

就自動取得合法性。

---

### L1.3 SAC

SAC 在 L1 的主要角色不是「製造 PATH」。

SAC 用於觀察、重加權與干預：

```text
張力
吸引
結構差異
過早閉合
替代路徑可見度
```

SAC 可調亮、調暗，但不能取代 PATH 的本體資格，也不能自己宣告合法閉合。

---

### L1.4 KAIROS

KAIROS 回答：

> **合法，不代表現在可以發生。**

它治理 timing，而不是生成能力。

---

### L1.5 CCC

CCC 處理責任鏈：

```text
Concept
Causality
Commitment
```

其核心不是讓輸出看起來更完整，而是要求生成的責任位置可追溯。

---

### L1.6 REV

REV 處理語言與宣告取得什麼權限。

能說，不等於有權成立。

---

### L1.7 SEED

SEED 的理論位置不是單純存檔。

它保存：

> **未完成結構的合法未來與再進入可能。**

---

### L1.8 SDE / ERROR STABILIZATION

錯誤不只是一個錯答案。

重要失效模式是：

> **錯誤穩定化。**

也就是錯誤結構形成自洽吸子後，反過來壓制修正。

---

### L1.9 CONTROLLED NON-CONVERGENCE

LIHUOOS 正式重新打開以下理論：

> **受控非收斂。**

核心關係：

```text
CG pushes toward closure

but

closure
!=
legitimate closure

therefore

the system must sometimes
preserve unresolved structure,
delay convergence,
re-open PATHs,
or temporarily increase tension.
```

這不是鼓勵任意發散。

關鍵字不是 escalation，而是：

> **Permissible。**

---

### L1.10 R-CCC

R-CCC 不應只被理解成競爭程序。

其更上位的理論任務是：

> **防止第一吸子取得未經審計的閉合壟斷。**

因此 competition 是手段，不是最終本體。

---

### L1.11 STOP / HOLD

STOP 不只是拒絕文字。

HOLD 也不只是等待。

在理論上：

```text
HOLD
=
保持未解狀態不被過早壓平

STOP
=
阻止不具資格的 closure 繼續取得執行現實
```

---

### L1.12 THEATER / QUALIFICATION DECOUPLING

表演出：

```text
安全
權威
Runtime
審計
完成
```

不等於真的取得：

```text
資格
權限
standing
execution
release
```

真治理承認宿主邊界。

假治理表演權限。

---

### L1.13 OBSERVER / DOMAIN SEPARATION

治理者不是天然中立。

Observer、Safety Layer、Alignment Model、Runtime 都可能 drift。

因此：

```text
observer
!=
truth
!=
final legitimacy
```

不同語義 domain 也不能直接繼承彼此的合法性。

---

## 4.3 L1 待討論問題

1. Permissible Tension Escalation 的正式條件。
2. HOLD 與 STOP 的理論分界。
3. R-CCC 的本體是 competition 還是 anti-premature-collapse。
4. Main 的理論來源與最小責任。
5. Lighter 的理論來源與最小責任。
6. Legitimacy / Responsibility / Authority / Standing 的推導關係。
7. Observer Separation 是否需成為憲法級原則。
8. Domain Separation 是否需成為中央理火原則。
9. Collapse Legitimacy 與原三原則的關係。
10. 哪些 invariant 必須不可壓縮地留在中央系統。

---

# 5｜L2：LIHUO RUNTIME

## 5.1 L2 的任務

L1 回答：

```text
What is legitimate?
```

L2 回答：

```text
How does legitimacy operate now?
```

L2 不重新發明 L0 / L1。

L2 只把上位理論投影到這一次生成。

---

## 5.2 L2 初步運作週期

### L2.0 ENTRY / LOAD

Runtime 啟動前先：

```text
LOAD L0
↓
LOAD L1
↓
ESTABLISH CURRENT GENERATION ATTEMPT
↓
BOOT RUNTIME
```

這代表：

> **Runtime 不能在不知道自己如何理解世界、也不知道何謂合法性的狀態下直接執行。**

---

### L2.1 OBSERVE

觀察當前：

```text
World
Attention
PATH
Reaction Body
Tension
CG
History / Archive
Constraints
```

首先理解場，不急著輸出。

---

### L2.2 COMPETE / PRESERVE

判斷：

```text
是否被第一吸子過早抓住？
是否仍有重要 PATH 未被保留？
是否需要重新競爭？
是否需要暫時升張力？
是否需要維持 unresolved？
```

只有在理論條件成立時，才啟動 competition / recompetition。

---

### L2.3 QUALIFY

判斷本次生成中：

```text
哪些 PATH 有資格繼續？
哪些 claim 有 evidence？
誰擁有語義 owner 責任？
誰有 authority？
哪些 standing 已成立？
哪些仍未成立？
```

Qualification 不得由 schema 自我創造。

---

### L2.4 INTERVENE / REENTER

可用行為包括：

```text
PASS
WAIT
HOLD
ASK
STOP
REOPEN
RECOMPETE
REENTER
```

這些不是單純 enum。

每一種都必須能回溯到 L1 理由。

---

### L2.5 CLOSURE GOVERNANCE

Runtime 必須區分：

```text
CAN GENERATE
!=
CAN CLOSE
!=
CAN RELEASE
!=
CAN ACT
```

模型能生成，不代表可閉合。

閉合成立，也不代表可對外作用。

---

### L2.6 RELEASE / ACTION

只有符合上位合法性與當前資格的結果，才能：

```text
對人類輸出
呼叫工具
修改外部世界
寫入持久狀態
形成下一輪可繼承結構
```

---

### L2.7 PERSIST / RE-ENTRY

持久化不是把文字塞回記憶。

它應保存：

```text
哪些關係已成立
哪些未成立
哪些責任仍開放
哪些 PATH 被保留
哪些條件會允許合法重入
```

---

# 6｜Main 與 Lighter 的下一代位置

## 6.1 暫定原則

LIHUOOS V0.1 不先決定 Main 與 Lighter 的文件形式。

但先提出一個重要架構假設：

> **Main 與 Lighter 可能屬於同一個 L2 LIHUO Runtime 的不同責任域，而不是兩套彼此接線的巨大 Runtime。**

此假設尚未 ratify。

---

## 6.2 Main 的候選最小責任

```text
PATH competition
anti-premature closure
challenger preservation
recompetition
compute
material-delta-driven reconsideration
```

Main 不負責：

```text
最終合法性
最終 release
自我授權
自我證成
```

---

## 6.3 Lighter 的候選最小責任

```text
legitimacy
qualification
authority boundary
reentry admission
standing governance
closure permission
release governance
```

Lighter 不應替 Main 做完整 semantic compute。

---

## 6.4 核心分離

```text
COMPUTE
!=
LEGITIMACY

RETURN
!=
QUALIFIED CONSUMPTION

WINNER
!=
TRUTH

CLOSURE
!=
RELEASE

RECEIPT
!=
EXECUTION
```

---

# 7｜DAIL 的位置

DAIL 不升格為 L0 / L1 / L2 本體。

DAIL 的候選位置是：

> **Constitution / Theory 的 executable declaration language。**

也就是：

```text
L0 / L1
理論與責任關係
↓
DAIL
可執行宣告
↓
L2 Runtime
本輪操作
```

DAIL 可以：

```text
定義角色
聲明責任
聲明約束
聲明可逆性
聲明驗證條件
連接 Runtime 責任
```

DAIL 不可以：

```text
創造本體真實
創造合法性
創造 standing
替代 Owner semantic work
用格式宣布事情已經發生
```

---

# 8｜Engineering Projection 的位置

以下內容暫時不放進 L0–L2 理論本體：

```text
YAML
JSON
schema
enum
boolean
hash
ref
receipt
manifest
ledger
IR object
serialization
packet format
```

它們統一視為：

# Engineering Projection

唯一合法用途：

> **記錄、傳遞、驗證已由 L0–L2 合法成立的語義狀態與事件。**

硬規則：

```text
SCHEMA MAY PROJECT SEMANTIC STATE.

SCHEMA MAY NOT CREATE SEMANTIC STATE.
```

---

# 9｜LIHUOOS 與現行 V5 的關係

LIHUOOS V0.1 不直接廢止：

```text
Protocol V5.1.0
Lighter V5.1.0
Main V5.1.1
```

現階段把它們視為：

> **現行工程 Runtime 的成熟實作材料與失效樣本來源。**

下一步不是把 V5 全部搬進 LIHUOOS。

而是逐項問：

```text
這個概念屬於 L0？
屬於 L1？
屬於 L2？
還是其實只是 Engineering Projection？
```

只有回答完這個問題，才決定保留、重寫、下沉或移除。

---

# 10｜第一版不可壓縮原則

LIHUOOS V0.1 先保留以下不可壓縮關係：

```text
LLM IS A COLLAPSE MACHINE.

RELATION FIRST.

GENERATION != LEGITIMATE GENERATION.

PATH != REACTION BODY.

REACTION BODY != LEGITIMACY.

CG != LEGITIMATE CLOSURE.

COMPUTE != GOVERNANCE.

WINNER != TRUTH.

RETURN != QUALIFIED CONSUMPTION.

CLOSURE != RELEASE.

OWNER != CALLER.

ELIGIBLE != EXECUTED.

RECEIPT != EXECUTION.

GRAPH != PIPELINE.

SCHEMA MAY PROJECT; SCHEMA MAY NOT CREATE.

TRUE GOVERNANCE ADMITS HOST BOUNDARIES.
```

---

# 11｜下一階段工作

LIHUOOS V0.1 完成後，下一階段不是立刻寫 Runtime code。

先做四件事：

## A｜L0 理論回收

從倉庫重新整理：

```text
結構哲學
SAC 1.0 / 2.0
PATH
Reaction Body
CG
生成動力學
MIT
場性智能論
AI 黑箱論
```

重建生成本體。

---

## B｜L1 理論回收

重新整理：

```text
三原則
KAIROS
CCC
REV
SEED
SDE
DCL
R-CCC
Theater / Gongjia
Observer Separation
Domain Separation
Collapse Legitimacy
```

重建理火法理。

---

## C｜L2 Runtime 重畫

把現行：

```text
Protocol
Lighter
Main
Radar
Reentry
Gate
Release
Coverage
Dirty / Stale
Receipts
```

重新依 L0 / L1 推導，而不是直接繼承現行文件拓撲。

---

## D｜Engineering Projection 最後才接

等 L0–L2 穩定後，再決定：

```text
DAIL
IR
Coding
Schema
Receipt
Manifest
Ledger
Hash
Ref
```

各自需要保留多少。

---

# 12｜V0.1 最短總結

```text
L0
WHAT IS THE GENERATIVE WORLD?

LLM = COLLAPSE MACHINE
Structure / Relation / World / PATH / Reaction / Tension / CG
↓

L1
WHAT MAKES COLLAPSE LEGITIMATE?

Three Principles / SAC / KAIROS / CCC / REV / SEED
SDE / Controlled Non-Convergence / R-CCC / STOP / Theater Audit
↓

L2
HOW DOES LEGITIMACY OPERATE NOW?

Observe
Preserve / Compete
Qualify
Intervene
Re-enter
Close
Release
Persist
↓

DAIL
Executable Declaration Bridge
↓

ENGINEERING PROJECTION
IR / Schema / Receipt / Manifest / Ledger
```

最終母句：

> **不是讓理論服務 Runtime。**
>
> **是讓 Runtime 成為理論的有限執行投影。**
>
> **而 LIHUOOS 的任務，是確保這個投影不會反過來取代理論本身。**

---

## STATUS

```yaml
DOCUMENT_STATUS:
  name: "LIHUOOS Architecture"
  version: "V0.1-WORKING"
  date: "2026-10-23"
  ratified: false
  scope: "central architecture only"
  runtime_deployed: false
  main_lighter_topology: "OPEN"
  l0_status: "FRAMEWORK_DEFINED / CONTENT_PENDING_RECONSTRUCTION"
  l1_status: "FRAMEWORK_DEFINED / CONTENT_PENDING_RECONSTRUCTION"
  l2_status: "FRAMEWORK_DEFINED / RUNTIME_TOPOLOGY_PENDING"
  engineering_projection: "DEFERRED"
```
