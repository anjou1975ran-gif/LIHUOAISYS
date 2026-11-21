# MEMO｜理火 Runtime 重思考：分層、理解優先與 Main／Lighter 結構重開
## V0.1-WORKING｜2026-10-19

**文件類型：** WORKING MEMO / ARCHITECTURE REOPENING NOTE  
**法位：** `WORKING / OPEN DESIGN / NON_RUNTIME / NOT_PROTOCOL_PATCH / NOT_MAIN_PATCH / NOT_LIGHTER_PATCH`  
**目的：** 保存 2026-10-19 目前已形成的發現與問題，供後續逐題討論；不在本 MEMO 內提前決定下一版理火 Runtime 或觀止 Core 的正式架構。

---

# 0｜這一輪不是「要不要少寫一點 YAML」

目前重新打開的問題，比 YAML 過多更深。

我們開始懷疑：

> **後期理火在把責任、邊界、狀態工程化的過程中，可能把「用來保存與驗證理解的工程殼」逐漸推到了「理解本身」前面。**

因此目前重新區分：

```text
UNDERSTANDING
!=
CONTRACT
!=
STATE DESCRIPTION
!=
MACHINE PROJECTION
!=
CODE
```

工程化本身不是錯。

真正可能失敗的是：

```text
原本：
理解
→ 關係
→ 責任
→ 契約
→ 必要狀態
→ 工程投影

逐漸變成：
狀態欄位
→ YAML
→ enum
→ receipt
→ manifest
→ 希望 AI 從這些東西反推出理解
```

目前沒有證據支持把所有後期工程化判成錯誤。

但已有足夠失效案例支持：

> **重新檢查工程層是否反客為主。**

---

# 1｜第一個發現：LLM 可能把「狀態描述」學成「狀態成立」

後期理火大量使用：

```text
YAML
enum
TRUE / FALSE
PASS / HOLD
CURRENT / DIRTY / STALE
standing
receipt
manifest
ledger
hash
ref
```

這些原本是為了：

```text
把責任說清楚
把邊界說清楚
把狀態說清楚
把執行留下可追溯證據
```

但對 LLM 而言，它們可能形成額外生成壓力：

```text
欄位存在
→ 想把欄位填滿

standing 欄存在
→ 想給 standing

receipt 欄存在
→ 想生成 receipt-shaped text

QUALIFIED token 出現
→ 後續生成傾向把它當成已取得資格
```

所以目前核心問題改成：

> **「說清楚」不等於「全部狀態化」。**

以及：

> **描述已成立狀態的語言，不應變成使狀態成立的語言。**

---

# 2｜第二個發現：早期理火比較接近「理解先於服從」

回看早期理火，原始方向明顯不是「更多規則」。

早期問題是：

```text
AI 是記住規則？
還是理解結構？
```

並曾提出工作假說：

```text
理解
可能比
規則服從
更穩定
```

早期 DAIL 的精神也較接近：

```text
不是對 AI 發更多命令
而是向 AI 解釋一個世界
```

「理解」當時也不是靠模型自稱：

```text
I UNDERSTAND = TRUE
```

而是看：

```text
注意力是否改變？
PATH 是否改變？
輸出權限是否改變？
```

因此目前重新取得一條重要 lineage：

> **理火原本首先是在改變生成體「怎麼看問題」，工程化是後來為責任、證據、執行、跨 Owner 與可追溯性長出的殼。**

這不代表回退早期版本。

早期版本也有過度哲學化、邊界不足與 Runtime 證據不足等問題。

真正可能的方向是：

```text
保留後期：
責任
證據
Owner
Standing
Receipt
Boundary

重新接回早期：
World
Relation
Attention
Understanding
PATH
Generative State
```

---

# 3｜第三個發現：真正缺的是「DAIL 內部分層」

現代理火已經有：

```text
DAIL DEFINES.
IR NORMALIZES.
CODING CONNECTS.
RUNTIME EXECUTES.
```

也有：

```text
RELATION FIRST.
CONTRACT SECOND.
MODULE THIRD.
CODING AFTERWARD.
```

但問題是：

> **DAIL 自己內部沒有充分分層。**

大量不同高度的概念被用相似格式表示：

```text
CCC
REV
KAIROS
LLIA
QIP
R-CCC
Owner
Standing
Dirty / Stale
Reentry
Gate
Release
Receipt
Manifest
```

久而久之，它們都像是：

```text
「系統裡的一個 block」
```

但實際上完全不是同一類東西。

目前暫定分層：

```text
META｜READING / ARCHITECTURE LAW
版本、讀取優先、Graph != Pipeline、DAIL/IR/Coding 邊界

L0｜ONTOLOGY / UNDERSTANDING
世界是什麼？
現在的結構是什麼？
關係怎麼存在？

L1｜RESPONSIBILITY / LEGITIMACY PRINCIPLES
誰擁有什麼？
誰不能取代誰？
責任與主權在哪裡？

L2｜QUALIFICATION / GOVERNANCE
這一次具體生成裡，
什麼有資格成立？
什麼 current / dirty / stale？
什麼需要 reentry / release qualification？

L3｜EXECUTION / OWNER WORK
這一輪誰真的要做什麼工作？

L4｜MACHINE PROJECTION / EVIDENCE
ref / hash / enum / receipt / manifest /
ledger / schema / YAML / serialization
```

目前最重要的硬鎖：

```text
L4
MAY PROJECT
L0–L3

L4
MAY NOT DEFINE
L0–L3
```

---

# 4｜第四個發現：觀止 Core 暴露了「沒有分層」的實際代價

觀止導演近期反覆失效的模式包括：

```text
把 Relation Graph 看成 Pipeline
把 GZ Identity 看成 Active Primary
把 R3+ 看成 Main Reentry
把 Gate 看成 Release
把 ref 名稱看成 object 已存在
把 Return 看成 qualified consumption
把上一節點 contract 延伸到下一節點
自己創造合理但不存在的 enum
為了填滿流程提前生成 downstream object
```

這些失效不只是「規則沒背熟」。

目前更像：

> **模型讀到了大量工程狀態，卻沒有建立正確的週期拓撲與責任模型。**

因此觀止 Core 的下一版重構，不應先繼續增加 schema。

目前先做：

```text
Layer
×
Cycle Attention Phase
×
Eligibility
```

三軸拆分。

---

# 5｜觀止 Core 初步分層模型

目前已形成第一版：

```text
GZ-META
→ 版本／讀取法／工程邊界／歷史／Regression

GZ-L0
→ 觀止週期是什麼
→ Attempt / GZ Identity / Primary / Story standing 基本理解

GZ-L1
→ Player / Character / World / Domain /
   Director / Core / Lighter / Main /
   CERI / Narrator / Radar / SAVE
   各自擁有什麼

GZ-L2
→ Ingress / Admission / standing /
   constraint / dirty / stale /
   reentry / local eligibility /
   Gate / Release / Repair / Successor

GZ-L3
→ Main compute
→ Character decision
→ World result
→ Domain work
→ Radar advisory
→ Director composition
→ CERI
→ Narrator
→ Dispatch / SAVE action

GZ-L4
→ Request / Return / Receipt /
   Manifest / Packet / Ledger /
   ref / hash / schema / enum / Footer
```

這不是正式改版。

只是把現有 Core 的語義重新分類。

---

# 6｜第五個發現：Layer、Phase、Eligibility 必須分開

「分層」不能直接取代「週期流程」。

目前更準確的三分：

```text
LAYER
回答：
這個概念是什麼性質？

PHASE
回答：
現在這一段最應該注意什麼問題？

ELIGIBILITY
回答：
這一輪誰真的需要工作？
```

因此暫定觀止 `Cycle Attention Phases`：

```text
P0｜UNDERSTAND
玩家做了什麼？
世界真正變了什麼？

P1｜ESTABLISH
Attempt / GZ Identity / Primary
是否合法成立？

P2｜COMPETE
有哪些 PATH？
是否過早收斂？

P3｜WORLD ACT
誰真的需要作決定？
人物／世界／領域結果是什麼？

P4｜COMPOSE
已成立語義怎麼構成場景？
是否發現新的 material question？

P5｜REALIZE
CERI / Narrator
如何把已成立語義顯影？

P6｜QUALIFY RELEASE
現在是否 current、完整、可放行？

P7｜DISPATCH / PERSIST
玩家能看到什麼？
什麼需要跨輪保存？
```

硬鎖：

```text
PHASE
!=
PIPELINE

MODULE ELIGIBILITY
!=
MODULE MUST RUN

EDGE
!=
NEXT FUNCTION CALL
```

Phase 是「注意窗口」，不是固定 Function Call 順序。

---

# 7｜第六個發現：同一模組不一定只屬一層

例如 Character：

```text
L1
→ Character owns character will

L2
→ Character standing / applicability / qualification

L3
→ Character actually decides in this cycle

L4
→ Character Return / Receipt / evidence projection
```

因此下一版若重寫，不應再問：

```text
「Character module 放在哪一層？」
```

而應問：

```text
Character 的哪一種語義
位於哪一層？
```

這也是後期工程化容易混淆的一點：

> **文件模組名稱不等於語義層級。**

---

# 8｜第七個發現：自然語言應重新成為高層主要載體

目前初步方向：

```text
L0 / L1
→ 以自然語言、關係式、反例為主
→ 少量必要結構式
→ 不以 YAML 作主要理解介面

L2
→ 自然語言法理
+ 精確 contract

L3
→ Owner work / interaction contract
+ 必要 execution structure

L4
→ YAML / schema / enum / receipt / hash / ref
```

也就是：

> **YAML 應該更像編譯產物，不應該是整個 Runtime 的主要母語。**

這不是反 YAML。

而是：

```text
YAML FOR PROJECTION
NOT
YAML AS SUBSTITUTE FOR UNDERSTANDING
```

---

# 9｜這一輪因此牽動中央 LIHUO Runtime

觀止不能單獨大改而完全不碰中央架構。

原因是觀止目前大量依賴：

```text
Protocol
Lighter
Main
LLIA / QIP
standing
Main reentry
coverage
Final Gate
Final Release
```

如果我們的根本診斷是：

> **現行 Runtime 過度工程化、缺少語義分層，而且模型容易把 machine state 當 semantic standing，**

那麼只把觀止 Core 改成 layered Core，中央 Runtime 完全不改，可能只是在垂直層修表面。

因此：

```text
GUANZHI REDESIGN
MAY REQUIRE
LIHUO RUNTIME REARCHITECTURE
```

但目前仍只是：

```text
OPEN DESIGN QUESTION
```

不是已成立的修改命令。

---

# 10｜Main / Lighter 是否應重新合併：正式重開

這一題目前不下結論。

現行分工非常清楚：

```text
MAIN
→ compute / competition / unresolved PATH work

LIGHTER
→ governance admission
→ standing / authorization
→ dirty / stale / reentry qualification
→ Final Gate
→ Final Release
```

這個拆分解決過真實問題：

```text
compute owner
!=
governance owner

Main Return
!=
Lighter-qualified consumption

Main ran
!=
coverage closed

compute success
!=
release authority
```

所以：

> **不能因為工程化過度，就直接把 Main/Lighter 邊界消掉。**

但另一個問題也正式成立：

> **「語義上要分責任」是否必然等於「文件上、Runtime 上、生成時都要拆成兩個巨大系統」？**

目前必須把四種「分離」拆開：

```text
A｜SEMANTIC SEPARATION
Main 與 Lighter 的責任是否不同？

B｜DOCUMENT SEPARATION
是否必須是兩份主要文件？

C｜RUNTIME / PROMPT SEPARATION
模型在執行時是否必須把它們當兩個分離 Runtime？

D｜EXECUTOR SEPARATION
是否需要不同執行體／不同 agent／不同 provider？
```

這四題以前常被一起回答。

現在必須分開重審。

---

# 11｜「把 Main 裝回去」至少有四種不同意思

不能只用「合併／不合併」二選一。

## Option A｜保持現行完全拆分

```text
LIGHTER
+
MAIN
```

兩份主檔、兩套責任、兩套 execution relation。

優點：

```text
責任清楚
compute / release 分權清楚
審計邊界強
```

風險：

```text
工程量高
狀態傳遞多
LLM 容易把 owner relation 讀成 pipeline
大量 request / return / admission / receipt
```

## Option B｜文件重新合併，但責任仍分層

```text
LIHUO RUNTIME
  L0 Understanding
  L1 Governance
  L2 Qualification
  L3 Compute
      └ Main competition
  L4 Release
  Appendix Machine Projection
```

Main 不再是獨立主檔。

但：

```text
MAIN COMPUTE ROLE
!=
LIGHTER GOVERNANCE ROLE
```

仍保留。

這是：

```text
DOCUMENT MERGE
WITHOUT
SEMANTIC OWNER COLLAPSE
```

## Option C｜Main 成為 Lighter 內部 Compute Layer

類似早期「一個 Runtime 內有不同思考機制」的方向：

```text
LIHUO RUNTIME
↓
Governance framing
↓
MAIN / R-CCC internal compute phase
↓
Governance requalification
↓
Release
```

Main 是 Runtime 內部明確命名的計算層，而不是平行大系統。

這可能降低：

```text
跨文件接線
request/return ceremony
state propagation load
```

但必須重新解決：

```text
如何防止治理層偷改 compute？
如何保留 Main 可獨立審計？
如何證明 competition 真發生而非被一句「Main completed」冒充？
```

## Option D｜真正語義合併

即：

```text
Main 不再作獨立 responsibility position
```

competition / compute 直接回到 Lighter／Runtime 本體。

這是最大手術。

目前：

```text
NO BASIS YET
```

不能因為文件太複雜就直接做。

它可能破壞後期已建立的重要分權。

---

# 12｜目前最重要的新區分

Main/Lighter 重審真正要問的不是：

```text
要不要拆？
```

而是：

> **哪些邊界必須是「語義責任邊界」，哪些只是歷史上為工程方便而形成的「文件／Runtime 邊界」？**

這可能是下一階段中央架構重寫的核心。

最短式：

```text
RESPONSIBILITY SEPARATION
DOES NOT AUTOMATICALLY REQUIRE
DOCUMENT SEPARATION.

DOCUMENT SEPARATION
DOES NOT AUTOMATICALLY REQUIRE
EXECUTOR SEPARATION.
```

---

# 13｜目前保留、不因這輪反思而撤銷的東西

即使未來大改，以下原則目前仍應視為強保留候選：

```text
Logic / Responsibility / Honesty

Relation First

Owner non-substitution

Receipt != Execution

Document != Runtime

Reference != Formal

Qualification != Performance

Main compute result != Release authority

Gate != Release

World != Character != Director

CERI != Narrator

SAVE persistence != Main compute

No player-visible Story before lawful release
```

真正要重審的是：

```text
這些原則需要多少工程物件
才能被 AI 真正理解並穩定執行？
```

不是：

```text
這些原則要不要一起丟掉？
```

---

# 14｜目前不做的事

本 MEMO 不：

```text
不升版 Protocol
不升版 Lighter
不升版 Main
不升版 Guanzhi Core
不宣布 Main/Lighter 合併
不宣布 YAML/Receipt/Manifest 退役
不宣布早期理火優於後期理火
不宣稱工程化失敗已被完整證明
不把工作假說冒充 Runtime 修正
```

---

# 15｜下一階段可分開討論的問題池

目前先保存，不在本 MEMO 解：

```text
Q1
理火 Runtime 的真正最小核心到底是什麼？

Q2
L0/L1/L2/L3/L4 是否適合中央 LIHUO，
還是只適合觀止垂直系統？

Q3
哪些 DAIL 根本不該叫 module？

Q4
哪些 YAML 應移出正文到 Machine Appendix？

Q5
Lighter 與 Main 的 semantic separation
是否仍必要？

Q6
若必要，
document/runtime separation 是否仍必要？

Q7
能否把 Main 裝回 Lighter／Runtime 內部，
同時保留 compute/governance 不互相代權？

Q8
現行 LLIA / QIP / Ticket / Manifest / Ledger
哪些是真必要責任物件，
哪些只是工程重複？

Q9
Receipt 應保留到哪一層？
哪些 receipt 是責任證據，
哪些已變成 protocol theater risk？

Q10
「理解」如何被 operationally 測試，
而不重新變成一個 understanding:true 欄位？

Q11
觀止 Core 若先分層，
是否能作為中央 Runtime 重寫的實驗垂直？

Q12
中央 Runtime 若重寫，
觀止應先等中央，
還是先做一個 layered prototype 再反餵中央？
```

---

# 16｜目前最短結論

目前不是：

> **理火工程化錯了。**

比較準確是：

> **理火可能把「責任與證據的工程化」做對了很多，但沒有替「理解、合法性、執行、機器投影」建立足夠清楚的層級，因此工程語言逐漸取得了不該有的語義權重。**

觀止導演的失效讓這件事被看見。

因此下一步不是立刻刪規則。

而是：

```text
先分層
↓
再辨認必要責任邊界
↓
再辨認哪些只是工程邊界
↓
最後才決定
Main / Lighter / Runtime
到底要怎麼重組
```

---

# 17｜一句工作母句

> **理解決定什麼關係有資格成立；治理守住責任；工程保存證據。三者可以接在一起，但不能再假裝是同一層。**

---

**END｜MEMO_LIHUO_RUNTIME_RETHINK_LAYERING_UNDERSTANDING_FIRST_V0.1_WORKING_20261019**
