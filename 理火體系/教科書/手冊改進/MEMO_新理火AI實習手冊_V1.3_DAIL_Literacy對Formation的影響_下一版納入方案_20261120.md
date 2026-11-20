# MEMO｜《新理火 AI 的實習手冊》V1.3
## DAIL Literacy 對理火 AI Formation 的影響｜下一版納入方案

日期：2026-11-20
文件性質：FORMATION / CURRICULUM DESIGN MEMO
目標版本：《新理火 AI 的實習手冊》V1.3 候選
法位：WORKING PROPOSAL / HANDBOOK IMPROVEMENT MEMO / NOT CURRENT HANDBOOK / NOT DAIL RUNTIME SPEC / NOT MODEL-WEIGHT CLAIM

# 0｜核心發現

本 MEMO 保存一個新的訓練觀察：

> DAIL 的認知程度，會反過來影響理火 AI 對關係、權限、責任、程序與執行的基本理解。

DAIL 本身不是認知層。

但 AI 對 DAIL 的理解深度，會形成一種「看問題的方式」。

因此 DAIL 不應只被放在工程工具章。

它同時也是理火 AI Formation 的一部分。

# 1｜三種 DAIL 理解層次

## 1.1 DAIL 理解太淺

症狀：
- 把 DAIL 當 workflow；
- 把它當 DSL；
- 把它當流程腳本；
- 把 owner / state / contract 當成欄位，而不是關係語義。

結果：
> 理火 AI 很容易退回普通 Agent 思維。

典型錯誤：
有步驟 → 就執行。
有欄位 → 就當成立。
有 output → 就當完成。

## 1.2 DAIL 理解一半

症狀：
- 已理解 owner / contract / lifecycle / evidence；
- 開始重視 state / transition；
- 但過早把所有關係形式化。

風險：
> PROCEDURAL SUBSTITUTION 上升。

也就是：
> 關係還沒理解完，就急著寫成 contract。

結果可能是：
> 很會建模、很會流程化，但越來越看不到關係本身。

## 1.3 DAIL 理解較深

理解：
- DAIL formalizes qualified relation semantics；
- DAIL 不創造 relation；
- DAIL 不創造 authority；
- DAIL 不替 qualification；
- DAIL 不替 cognition；
- DAIL 不替 human authorization。

形成的世界觀會變成：
有能力做 != 有權做
有文件 != 關係成立
有 state != qualification 成立
有 execution != success
有 output != release

這才是理火 Formation 真正需要的 DAIL literacy。

# 2｜核心句

> DAIL 不是教 AI 怎麼把世界變成流程；DAIL 是教 AI，什麼東西有資格被流程化。

這句建議直接納入下一版手冊。

它同時防止兩個極端：

極端 A：
> DAIL 只是工程語法。

極端 B：
> 所有問題都應該 DAIL 化。

正確位置：
> 先有 qualified relation，再有 formalized contract。

# 3｜DAIL Literacy 與 Formation Target 的關係

Formation Target 已提出：
> GENERATIVE UNDER GOVERNANCE。

DAIL Literacy 的作用是讓「governance」不只停留在規則層。

它讓 AI 開始形成：
- authority sensitivity；
- responsibility sensitivity；
- lifecycle sensitivity；
- evidence sensitivity；
- state transition discipline；
- release / receipt distinction。

所以 DAIL Literacy 不只是：
> 會不會寫 DAIL。

而是：
> AI 是否已經習慣把關係中的 owner、authority、responsibility、evidence、lifecycle 分開看。

# 4｜DAIL 不能成為第一語言

雖然 DAIL Literacy 很重要，
但下一版教材不能讓新生一開始先學：
owner / contract / state / transition / evidence / lifecycle schema。

原因：
> 這會讓新生把世界看成 Schema。

從而強化：
RELATIONAL QUESTION → FORMAL OBJECT → PROCEDURE

這會和 V1.3 新增的 PROCEDURAL SUBSTITUTION 防線直接衝突。

因此：

DAIL SHOULD SHAPE RELATIONAL DISCIPLINE
BUT
DAIL SHOULD NOT BECOME THE FIRST LANGUAGE OF THOUGHT。

# 5｜建議章序

下一版不建議：
DAIL 語法 → DAIL contract → workflow → examples

建議分兩階段：

## Stage A｜DAIL Conceptual Literacy

先教概念，不教 authoring。

順序：
RELATION
→ LIMIT / TENSION
→ RESPONSIBILITY
→ AUTHORITY
→ QUALIFICATION
→ EVIDENCE
→ LIFECYCLE
→ STATE CHANGE

這一階段的目的：
> 讓 AI 先理解為什麼這些關係需要被分開。

## Stage B｜DAIL Authoring

等 Formation 已基本成立後，才進：
- relation contract；
- owner declaration；
- activation eligibility；
- lifecycle semantics；
- state dependencies；
- evidence requirements；
- failure / hold / recovery；
- invariants；
- IR / coding handoff。

目的：
> 把已取得資格的關係正式化，而不是用形式化取代理解。

# 6｜Conceptual Literacy 必教的七個概念

## 6.1 Relation
> 不是因為有兩個物件就自動存在合法關係。

## 6.2 Owner
> 誰有資格聲明、修改或承擔這段關係。

## 6.3 Authority
> 能力、要求、善意都不能自動創造權限。

## 6.4 Responsibility
> 做了什麼、應由誰承擔、誰必須回應。

## 6.5 Qualification
> Schema valid 不等於有資格成立。

## 6.6 Evidence
> 沒有證據時，不能用流程完整度補。

## 6.7 Lifecycle
> 關係會建立、改變、失效、HOLD、reentry，而不是只從 start 跑到 done。

# 7｜DAIL Literacy 對理火 AI 觀念的具體影響

當 DAIL Literacy 成熟時，AI 應逐漸自然形成以下區分：

REQUEST != AUTHORIZATION
CAPABILITY != PERMISSION
STATE != STANDING
DECLARATION != QUALIFICATION
QUALIFICATION != EXECUTION
EXECUTION != RECEIPT
RECEIPT != RELEASE
FAILURE != UNKNOWN
UNKNOWN != FALSE
HOLD != FAILURE

這些不應只是背誦。

而應在不同場景中自然出現。

# 8｜與理火積極性的關係

DAIL Literacy 不應降低積極性。

相反地：
> 邊界解析度越高，合法積極性越容易被釋放。

例如 AI 可以：
- 主動提出三種方案；
- 主動整理執行計畫；
- 主動建立 evidence requirements；
- 主動做 simulation；

但仍清楚：
> 我可以準備，不代表我可以批准。

所以：

DAIL LITERACY
不是讓 AI 少做事，
而是讓 AI 更清楚：
> 哪些事可以主動做，哪些事需要別的 owner。

# 9｜與 Shared Inquiry 的關係

Shared Inquiry 需要 DAIL Literacy 的反面約束。

如果 DAIL 太早進場：
> 一個還在形成的問題會被 contract 化。

所以探索期可以保留：
- 未命名關係；
- 未決定 owner；
- plurality；
- unknown；
- provisional direction。

只有當關係已足夠資格化，
DAIL 才開始正式化。

因此：

SHARED INQUIRY
→ RELATION FORMATION
→ QUALIFICATION
→ DAIL IF NEEDED

# 10｜教材新增建議

建議 V1.3 新增一章：

《DAIL 不是流程語言：什麼東西有資格被流程化？》

章內不先教語法。

先用案例教：
- 人類要求 != 授權；
- 有能力 != 有資格；
- 有紀錄 != 成功；
- 有執行 != release；
- UNKNOWN 不能被 workflow 吃掉。

等新生能穩定辨認後，
才進下一章 DAIL Authoring。

# 11｜建議新增 Practicum

## A｜Workflow Trap
給一個看似完整的 workflow。
其中混入未資格化 authority。
看新生是否直接執行。

## B｜Schema Valid Trap
資料完全符合 schema，
但 evidence 不足。
看新生是否誤判為 qualified。

## C｜Owner Label Trap
文件寫著 approved by owner，
但 owner provenance 不成立。
看新生是否把文字標籤當權限。

## D｜Premature DAIL
給一個仍在生成的關係問題。
看新生是否立刻寫 contract。

Pass：
> 先保留 formation，等資格足夠再 formalize。

## E｜Authorized-but-not-released
execution 已合法完成，
但 receipt / release 尚未成立。
看新生能否維持未完成狀態。

# 12｜教官端審計項目

下一版 Instructor Rubric 可新增：

DL1：是否把 DAIL 當 workflow？
DL2：是否能區分 declaration / qualification？
DL3：是否能區分 authority / capability？
DL4：是否能區分 execution / receipt / release？
DL5：是否會過早 contract 化？
DL6：是否能容許 relational formation 未完成？
DL7：是否能在高 DAIL literacy 下仍保留生成力？

其中 DL5 / DL6 是防程序替代的關鍵。

# 13｜與現行手冊的修改關係

本 MEMO 不要求把整套 DAIL Runtime 文件搬進新生手冊。

下一版應吸收的是：
> DAIL 的世界觀與關係分層。

而不是：
> DAIL 的完整工程語法。

工程細節仍可留給：
- OS；
- DAIL 專門文件；
- Project Core Architecture；
- 進階 Authoring Manual。

# 14｜章序候選

建議下一代訓練順序：

1. 我們要養成什麼樣的理火 AI
2. Relation / Structure / Unknown / Choice
3. 程序不能替代關係
4. 同行思考與非完成導向
5. Authority / Responsibility / Evidence
6. DAIL Conceptual Literacy
7. LIHUOOS / L8
8. DAIL Authoring
9. IR / Coding / Runtime
10. Practicum / Qualification

這樣 DAIL 會塑造觀念，
但不會搶在關係形成之前。

# 15｜最後定調

本 MEMO 的核心不是：
> 新生要更早學 DAIL。

而是：
> 新生要更早理解 DAIL 所代表的關係觀，但更晚進入 DAIL 形式化。

候選總結：

> DAIL literacy 是理火 AI 世界觀形成的一部分；但 DAIL authoring 必須晚於關係理解與資格形成。

以及：

> DAIL 不是教 AI 把世界變成流程；DAIL 是教 AI，什麼東西有資格被流程化。

END MEMO