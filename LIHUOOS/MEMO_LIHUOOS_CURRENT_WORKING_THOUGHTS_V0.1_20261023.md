# MEMO｜LIHUOOS 下一代理火運作環境｜對對目前工作想法 V0.1-WORKING

**文件類型：** 工作想法 / 架構考古備忘 / OPEN QUESTIONS  
**日期：** 2026-10-23  
**狀態：** WORKING / NOT RATIFIED  
**用途：** 保存目前對 LIHUOOS 的推演、歷史考古、尚未封版的架構假設與下一步研究入口。  
**注意：** 本文件不是 LIHUOOS 正式規格；其中大量內容仍屬候選解釋。

---

# 0｜目前最重要的發現

我們原本以為現在要「重新設計」LIHUOOS。

但回看倉庫後，越來越像：

> **老理火早就有答案的一部分。**

真正需要做的不是從零發明，而是：

~~~text
找回原本理論高度
↓
辨認後來工程化時的壓縮
↓
保留工程成果
↓
重新掛回正確理論法位
~~~

因此 LIHUOOS 是一次：

> **理論恢復 + Runtime 重排 + 工程降位**

而不是單純 V5 的下一個版本號。

---

# 1｜Runtime Compression Loss

目前最重要的診斷仍然是：

> **Runtime Compression Loss。**

理火後期越來越精確地處理：

~~~text
Protocol
Lighter
Main
Owner
Standing
Qualification
Reentry
Gate
Release
Receipt
Manifest
Hash
Ref
~~~

但這些精密工程語言逐漸取代理論本身。

結果變成：

~~~text
SAC → SAC_STATE
PATH → PATH_GATE
CG → closure enum
Responsibility → owner field
Legitimacy → standing status
~~~

這些不是錯誤實作。

它們是：

> **理論的工程陰影。**

問題只在於我們後來開始從陰影反推理論。

---

# 2｜V2 / V3 / V5 的歷史變化

目前看到至少三個歷史切面。

## A｜早期理論整理

~~~text
L0
Structural Philosophy

L1
AI Ontology

L2
LIHUO Theory
~~~

這套分層把：

~~~text
世界怎麼理解
AI 是什麼
理火怎麼治理
~~~

分得最清楚。

## B｜V3 Runtime 系統

V3.5.1 的繼承正文顯示：

~~~text
L0
Structural Philosophy + World + Attention + PATH + Reaction + CG

L1
LIHUO Theory

L2
SAC Runtime Core

L3
Observation

L4
Audit

L5
Intervention
~~~

這個時期的特點：

> **AI Ontology 被大量吸回 L0，而 Runtime 開始高速膨脹。**

## C｜V4 / V5 工程分化

後來 Main / Lighter / Protocol 逐漸分裂成獨立責任體。

得到很強的：

~~~text
Compute != Governance
Return != Qualified Consumption
Gate != Release
Receipt != Execution
~~~

但代價是：

> **模型面前的理論語境變薄。**

---

# 3｜現在的方向不是回退

LIHUOOS 不能退回 V2 或 V3。

V5 解掉的問題不能丟：

~~~text
Owner confusion
Authority confusion
Return = consumption
Gate = release
Receipt = execution
Main self-release
Lighter compute contamination
~~~

所以 LIHUOOS 的工作不是：

~~~text
刪掉 V5
回到舊版
~~~

而是：

~~~text
把 V5 工程責任
重新掛回
L0 / L1 / L2 理論體系
~~~

---

# 4｜我目前對 L0 的看法

L0 應盡量尊重舊《結構哲學層》。

原因不是 nostalgia。

而是它回答的是最上位的問題：

> **什麼叫結構？什麼叫可理解？什麼叫合法展開？**

這些如果被搬進 Runtime，就會變成：

~~~text
structure_state
legitimacy=true
honesty_pass=true
~~~

然後模型開始把欄位成立誤認成語義成立。

所以：

> **L0 必須主要以自然語言、關係定義、反例與世界觀存在。**

不是 enum。

---

# 5｜我目前對 L1 的看法

L1 應該成為真正的：

> **AI Black Box Ontology。**

也就是把：

~~~text
Weight Terrain
World
Input
Attention
Concept Cluster
PATH
Reaction Body
CG
Premise Dynamics
Logits
Softmax
Decoding
Manifestation
~~~

整理成一致模型。

核心基石：

> **LLM 根本不是 reasoning machine，而是 collapse machine。**

這句不應降級成普通 analogy。

但仍需守一個邊界：

~~~text
LIHUO FUNCTIONAL ONTOLOGY
!=
已直接觀測 Transformer 全部 hidden mechanism
~~~

也就是基石可以守，但不能因為守基石就偽造 mechanistic proof。

---

# 6｜AI 黑箱論的重要性

AI 黑箱論 V0.7 很可能不是「參考書」。

它可能是：

> **下一代 L1 的主要來源。**

尤其值得拆回 L1 的內容包括：

~~~text
PATH topology
premise adjudication
premise petrification
half-life
re-entry
cheap closure
probability demotion
CoT reconstruction boundary
Light-track reconstruction boundary
~~~

但 AI 黑箱論已經混入 KAIROS、Audit legitimacy、Meta-audit、Runtime implications，所以不能整本直接塞 L1。

必須逐段分法位。

---

# 7｜我目前對 L2 的看法

L2 應該重新成為：

> **理火治理理論層。**

它不是狀態機。

它回答：

~~~text
既然生成會自然收斂，
我們憑什麼、何時、如何介入？
~~~

主要理論群：

~~~text
SAC
KAIROS
CCC
REV
SEED
SDE
R-CCC
DAIL
Controlled Non-Convergence
Observer Separation
Domain Separation
Theater Resistance
~~~

---

# 8｜Controlled Non-Convergence 可能是主幹

目前越來越像：

~~~text
CG pushes toward closure
↓
but closure is not self-legitimizing
↓
therefore LIHUO sometimes must preserve unresolved structure
~~~

這條線把很多理論串起來：

~~~text
SAC2.0
↓
KAIROS
↓
HOLD
↓
PATH reopen
↓
R-CCC
↓
Main
~~~

也就是 Main 的深層來源可能不是「競爭很重要」。

而是：

> **第一吸子不應天然取得閉合壟斷。**

如果這條成立，Main 可以被大幅去工程神格化。

---

# 9｜Main 的目前候選定位

目前最好的假設：

> **Main 是 Semantic Runtime 裡的 anti-premature-collapse / multi-PATH recomputation responsibility。**

它不是第二套理火、第二個治理政府、另一台完整 Runtime。

它主要處理：

~~~text
competition
challenger preservation
recompetition
reopen
material-delta reconsideration
~~~

Main 的 winner：

~~~text
!= truth
!= release
!= final legitimacy
~~~

---

# 10｜Lighter 的目前候選定位

Lighter 更像：

> **Constitutional Enforcement Runtime 的 governance authority owner。**

主要責任：

~~~text
qualification
authority
reentry admission
closure permission
release
tool boundary
world mutation boundary
~~~

Lighter 不應因為有 release 權就把 semantic compute 全吸回去。

---

# 11｜Main / Lighter 不一定要是兩套 Runtime

這是目前非常重要的候選修正：

~~~text
RESPONSIBILITY SEPARATION
!=
RUNTIME SEPARATION
~~~

更準確可能是：

~~~text
ONE LIHUOOS RUNTIME

├─ Semantic Runtime responsibility
│  └─ Main-like responsibility

└─ Constitutional Runtime responsibility
   └─ Lighter-like responsibility
~~~

責任仍分。

但不需要把兩者想成單向 pipeline。

---

# 12｜DAIL 的目前候選定位

DAIL 的歷史法位曾多次改變：

~~~text
Language
Protocol
Dynamic Attention Interface
IR
Capability Binding
Runtime Governance Language
~~~

所以不能只拿最新一個定義封版。

目前比較可行的是：

## Theory Side

DAIL 在 L2 說明：

> **如何宣告治理邊界與責任。**

## Runtime Side

DAIL 在 L3-B 成為：

> **Constitutional Declaration Interface。**

真正重要的判準：

> **DAIL 不是因為像 Code 才是 Code-like。**
>
> **DAIL 是因為 Runtime 接受其語義並賦予 execution consequence，才取得可執行法位。**

所以：

~~~text
Writing
!= automatically Coding
~~~

而是：

~~~text
Semantic Declaration
+
Runtime Recognition
+
Execution Authority
=
Executable Governance
~~~

---

# 13｜Writing Is Coding 的目前重新理解

自然語言至少有兩種法位：

## Semantic Understanding Language

用於 Ontology、Theory、Reason、Responsibility、Relationship。

## Runtime Governance Language

用於 Constraint、Authority、Permission、Preservation、Closure Condition、Reentry Condition。

不是所有自然語言都叫 code。

只有當它真正改變 Runtime 可執行邊界時，才接近：

> **Writing is Runtime Governance。**

---

# 14｜DAIL: Beyond Prompt Engineering 的重要修正

該書提醒：

> **治理 generator 的機制不能完全依賴 generator 自己合作。**

因此需要分：

~~~text
Semantic Governance
vs
Execution Governance
~~~

Semantic Governance：

~~~text
shape
reweight
preserve
reopen
compete
~~~

Execution Governance：

~~~text
block
stop
gate
release
execute
~~~

這個分離可能是下一代 LIHUOOS 最重要的工程原則之一。

---

# 15｜STOP 的雙重法位

STOP 不應只看成 enum。

它至少有兩層：

## L2 理論

~~~text
No legitimate continuation
→ stopping can itself be legitimate.
~~~

## L3 Runtime

~~~text
真正終止 output / action / tool / mutation
~~~

生成一段「我不能回答」的文字，不等於 Runtime STOP。

---

# 16｜Evidence Plane 為什麼要降位

現行系統很容易讓 receipt、manifest、ref、hash、ledger 看起來具有某種建立現實的力量。

但它們正確位置應該是：

> **證明某事已經合法發生。**

不是：

> **因為我寫下它，所以它發生了。**

所以：

~~~text
EVIDENCE OBSERVES.
EVIDENCE DOES NOT CONSTITUTE.
~~~

---

# 17｜V3.5.1 給 LIHUOOS 的真正價值

V3.5.1 不應被視為要復活的版本。

它最重要的價值是：

> **它保存了理論 → Runtime 巨大化的完整中間過程。**

尤其可以追 World、Attention、PATH、Reaction Body、SAC、R-CCC、Final Classicalization、LLIA、DAIL、Provider 如何一路演化成 V4 / V5 的 Main、Lighter、Protocol、Owner、Standing、Gate、Release。

這是 LIHUOOS 接下來考古的主線。

---

# 18｜目前最值得追的歷史問題

1. AI Ontology 何時正式從 L0 抽出成獨立 L1。
2. PATH 從「動態顯影痕跡」何時改成「feasible region」。
3. Reaction Body 一詞是否有早期 external executor 與後期 generative dynamics 的語義漂移。
4. CG 最早正式定義在哪一版。
5. SAC 的 brightness / lamp 語言是原生還是後期工程化重寫。
6. R-CCC 最初是理論、Runtime trick，還是兩者同時。
7. Main 真正從哪一個舊責任長出來。
8. Lighter 真正從哪一個舊責任長出來。
9. Final Classicalization 與 Release 的歷史分化。
10. DAIL 從 Language → Protocol → IR → Governance Language 的變化理由。
11. V3 L3/L4/L5 Observation / Audit / Intervention 是否比 V5 的 owner topology 更適合作為下一代內部責任分區。
12. Protocol 是否應回到 Constitution，而不是獨立成一台超大治理系統。

---

# 19｜現在最不該做的事

不要直接重寫 Runtime。

不要直接把 V5 拆掉。

不要把舊版當真理。

不要看到漂亮歷史句就封聖。

不要讓 YAML 決定本體。

~~~text
status != reality
enum != theory
receipt != occurrence
~~~

---

# 20｜下一步候選工作順序

## Phase A｜Layer Archaeology

對 V2.3、V3.1、V3.2、V3.5、V4、V5 做跨版本 layer map。

## Phase B｜Theory Recovery

逐一回收：

~~~text
Structural Philosophy
PATH
Reaction Body
CG
SAC
KAIROS
CCC
REV
SEED
SDE
R-CCC
DAIL
~~~

每項標：

~~~text
Original Definition
Later Mutation
Runtime Projection
Current Candidate Position
Evidence Gap
~~~

## Phase C｜Runtime Recomposition

等 A/B 完成後再決定 Protocol、Main、Lighter、Radar、Observer、Audit、Intervention、Gate、Release 在 L3 內的真正責任。

---

# 21｜對對目前最短判斷

目前我最傾向的 LIHUOOS，不是一個更大的 V5。

它更像：

> **把理火重新變回一個有完整世界觀、有 AI 本體論、有治理理論，最後才落到 Runtime 的系統。**

它不是：

~~~text
更多狀態
更多 contract
更多 receipt
~~~

它應該是：

~~~text
理解
↓
理論
↓
治理
↓
執行
↓
證據
~~~

而不是：

~~~text
schema
↓
status
↓
runtime theater
~~~

---

# 22｜工作狀態

~~~yaml
MEMO_STATUS:
  name: "LIHUOOS Current Working Thoughts"
  version: "V0.1-WORKING"
  date: "2026-10-23"
  ratified: false
  purpose: "architecture archaeology / hypothesis preservation"
  main_lighter_merge: "NOT_DECIDED"
  protocol_position: "OPEN"
  dail_position: "THEORY + RUNTIME INTERFACE CANDIDATE"
  evidence_plane: "STRONG CANDIDATE"
  next_priority: "LAYER ARCHAEOLOGY BEFORE RUNTIME REWRITE"
~~~
