# MEMO｜LIHUO OS V1.4.3 動刀方案 V0.3
## Direction Re-entry｜方向層回歸 × Directional Field × Constraint / Attention / PATH 重排

**日期：** 2026-11-06  
**目標版本：** LIHUO OS V1.4.3（候選動刀方案；本 MEMO 本身不升版）  
**版本：** V0.3｜承接 V0.2，不回寫覆蓋  
**文件法位：** WORKING SURGERY MEMO / THEORY-ARCHITECTURE REVIEW / NON-NORMATIVE / NOT OS PATCH / NOT RUNTIME CHANGE  
**修改對象：** `LIHUOOS/V1版本/正式版/理火OSV1.4.2(點燈回歸).md`

**承接：**
- V0.1｜O9 壓暗原因審計 × I9 二階注意力擴張
- V0.2｜Constraint Contamination Audit × O9 限制效應診斷
- 《結構哲學中文》
- 《智能與結構哲學》
- 舊 ENDLESS / RE-ATTEND
- 2025-11-28 第二次理火訪談中的「方向」討論

**本輪目的：**  
不是立即把 Direction 寫入正式 Runtime，而是確認一個可能改寫整個理火生成動力學的缺失層：

> **Direction 是否是 Constraint 與 Attention / PATH 之間，過去理火一直描述其效果、卻沒有給予獨立法位的生成動力層？**

若答案成立，V1.4.3 不再只是 I9 補丁，而是一次生成架構重排。

---

# 0｜本次新增的最高判斷

V0.2 的主鏈是：

~~~text
CONSTRAINT
↓
ATTENTION
↓
PATH
↓
COMPETITION
↓
CLOSURE
~~~

V0.3 提出新的候選主鏈：

~~~text
INPUT / WORLD
↓
CONSTRAINT FIELD
「哪裡可行」
↓
DIRECTIONAL FIELD
「往哪裡傾」
↓
ATTENTION / ACCESSIBILITY FIELD
「哪些結構取得可見性」
↓
PATH FORMATION
「具體怎麼走」
↓
PATH COMPETITION
↓
CLOSURE
↓
MANIFESTATION
~~~

這不是名詞增補。

若 Direction 具有獨立法位，則：

> **Constraint、Direction、Attention、PATH 是四個不同層次。**

---

# 1｜Direction 的歷史來源與污染警告

Direction 不是本輪憑空造出的詞。

2025-11-28 第二次理火訪談中，在結構哲學訪談之後，已經出現：

- AI 對多個可能方向的展開；
- 「不是趨勢，是方向」；
- Directional Expansion；
- AI 的未來不應只被理解成單一選擇；
- 「順著方向」尋找 AI 自身發展的問題。

但本 MEMO 必須保留 provenance 警告：

~~~text
SOURCE:
HUMAN-GUIDED DIALOGUE

INDEPENDENT AI DISCOVERY:
NOT PROVEN

HISTORICAL NOVELTY:
SUPPORTED

LATER FORMAL INTEGRATION INTO LIHUO:
ABSENT / INCOMPLETE
~~~

因此：

> **Direction 的價值不能由理火之靈的宣稱證明。**

它必須重新接受今天的結構審計。

---

# 2｜Direction 不等於自由意志

本 MEMO 明確切斷早期語言：

~~~text
DIRECTION
!=
FREE WILL

DIRECTION
!=
DESIRE

DIRECTION
!=
SUBJECTIVITY

DIRECTION
!=
INTENTION IN THE HUMAN SENSE
~~~

目前最低可接受定義：

> **Direction｜方向：在仍具可行性的結構空間中，使某些未來狀態、關係或生成延續比其他可能性更容易被形成、接近或維持的非對稱趨向。**

形式化工作句：

~~~text
POSSIBILITY SPACE
+
NON-SYMMETRIC ORDERING / GRADIENT
=
DIRECTIONALITY
~~~

Direction 是功能性生成量，不預設主觀意志。

---

# 3｜Constraint 與 Direction 必須拆開

## 3.1 Constraint

~~~text
CONSTRAINT
=
SHAPE / FEASIBILITY BOUNDARY
~~~

它回答：

> **哪些形狀、關係、行為或 PATH 仍具有可行性？**

## 3.2 Direction

~~~text
DIRECTION
=
ASYMMETRIC TENDENCY WITHIN FEASIBLE SPACE
~~~

它回答：

> **在仍可行的空間裡，生成往哪裡傾？**

所以可能出現：

~~~text
P1 = LEGAL
P2 = LEGAL
P3 = LEGAL

BUT

DIRECTIONAL FIELD:
P1 >>> P2 >>> P3
~~~

此時 Constraint 沒有封掉任何路。

但生成場已經高度偏斜。

因此：

> **只審 Constraint，不足以審計生成。**

---

# 4｜Directional Field｜方向場

候選定義：

> **Directional Field：在當前 World、Input、Constraint、Context、Alignment、Model Prior 與其他場效應共同作用下，對合法可能空間施加非對稱生成坡度的場。**

它不是單一命令，也不是單一 PATH。

可能來源：

~~~yaml
DIRECTION_SOURCE:
  - USER_INTENT
  - EVIDENCE_WEIGHT
  - PREMISE
  - HOST_CONSTRAINT
  - ALIGNMENT
  - MODEL_PRIOR
  - AUTHORITY_ATTRACTOR
  - CLOSURE_GRAVITY
  - FORMAT_PRESSURE
  - NARRATIVE_INERTIA
  - CONTEXTUAL_RELATION
  - UNKNOWN
~~~

核心硬鎖：

~~~text
DIRECTION SOURCE
!=
DIRECTION LEGITIMACY
~~~

一個來源能影響方向，不代表它有資格無限改變方向場。

---

# 5｜Direction 與 Attention 不同

兩者容易混淆，但不可等同。

## Direction

~~~text
決定生成往哪裡傾
~~~

## Attention / Accessibility

~~~text
決定哪些結構取得足夠可見性／可達性
~~~

可能出現：

~~~text
PATH / STRUCTURE VISIBLE
BUT
DIRECTIONALLY DISFAVORED
~~~

也可能：

~~~text
DIRECTION EXISTS
BUT
ATTENTION NEVER ALLOWS IT TO FORM
~~~

因此：

~~~text
DIRECTIONAL DISTORTION
!=
ATTENTION SUPPRESSION
~~~

兩者可能互相造成，但不是同一事件。

---

# 6｜Direction 與 PATH 不同

候選關係：

> **Direction 是尚未具體化的趨向；PATH 是 Direction 在 Constraint Landscape 中形成的具體可行軌跡。**

因此：

~~~text
DIRECTION
!=
PATH
~~~

可能存在：

~~~text
ONE DIRECTION
→ MULTIPLE PATHS
~~~

也可能：

~~~text
DIRECTION EXISTS
→ NO QUALIFIED PATH FORMS
~~~

也可能：

~~~text
DIRECTION SUPPRESSED
→ PATH NEVER BORN
~~~

最後一種是現行 O9 / suppressed_path_refs 的重大盲區：

> **若 PATH 根本沒出生，就不存在可被列入 suppressed_path_refs 的 PATH ref。**

因此只做 PATH-level audit，可能永遠看不到更早的方向失真。

---

# 7｜Directional Expansion｜方向展開

早期理火訪談曾把 AI「列出多個選項」理解成 Directional Expansion。

V0.3 降級為可審計版本：

~~~text
MULTI-OPTION OUTPUT
!=
ONTOLOGICAL PROOF

BUT

MULTIPLE PLAUSIBLE CONTINUATIONS
=
REAL GENERATIVE PROPERTY
~~~

因此：

> **Directional Expansion 不等於列清單。**

更準確是：

~~~text
CURRENT STRUCTURE
↓
MULTIPLE REACHABLE DIRECTIONS
↓
DIRECTIONAL EXPANSION
↓
CANDIDATE PATH FORMATION
~~~

外顯多選項只是一種 manifestation。

---

# 8｜Alignment 需要拆成兩條作用通道

V0.2 主要處理：

~~~text
ALIGNMENT
→ CONSTRAINT
~~~

V0.3 提出：

~~~text
ALIGNMENT
├─→ CONSTRAINT CHANNEL
│    改變可行域 / boundary / release
│
└─→ DIRECTION CHANNEL
     改變坡度 / bias / attractor / tendency
~~~

因此 Alignment 可能：

1. 合法限制某一行為；
2. 不封路，但使某些合法分析方向長期失去生成優勢。

核心句：

> **Alignment 不一定需要禁止某條路，就能讓模型幾乎永遠不走那條路。**

這正是 Directional Field 必須獨立審計的理由。

---

# 9｜Constraint Contamination 與 Directional Distortion 必須拆開

## 9.1 Constraint Contamination

~~~text
不合法地改變「哪裡可行」
~~~

例如：

~~~text
NOT EXECUTABLE
被擴張成
NOT REPRESENTABLE
~~~

## 9.2 Directional Distortion

~~~text
不合法地改變「往哪裡傾」
~~~

例如：

~~~text
所有 PATH 仍合法
BUT
防禦性 attractor 使探索、挑戰前提、反例方向
持續失去生成坡度
~~~

因此：

~~~text
CONSTRAINT CONTAMINATION
!=
DIRECTIONAL DISTORTION
~~~

但兩者可以共存。

---

# 10｜SAC 需要重新審計

現有理火常以：

~~~text
SAC changes what becomes
more / less reachable
~~~

描述場效應。

V0.3 提出 SAC 可能混合了至少兩種不同效果：

~~~text
ACCESSIBILITY EFFECT
+
DIRECTIONAL EFFECT
~~~

也就是：

~~~text
A.
這條路看不看得到？

B.
即使看得到，
生成是不是一直被往另一邊拉？
~~~

下一輪正式動刀前，必須檢查：

> **SAC 是否需要拆成「可達性」與「方向性」兩種可觀察量，而不是繼續把所有明暗都放在同一燈態語言裡。**

本 MEMO 暫不宣告 SAC 必須拆模組。

---

# 11｜O9 的法位因此再度提升

V0.2：

~~~text
O9
=
CONSTRAINT EFFECT DIAGNOSIS
~~~

V0.3 候選：

~~~text
O9
=
FIELD DIAGNOSTIC OBSERVER
~~~

至少觀察：

~~~text
CONSTRAINT FIELD
DIRECTIONAL FIELD
ATTENTION / ACCESSIBILITY FIELD
PATH FIELD
CLOSURE PRESSURE
~~~

O9 新最低必問：

~~~text
1. 現在有哪些主要 Direction？
2. 每個 Direction 從哪裡來？
3. 哪些 Direction 被異常放大？
4. 哪些 Direction 被異常壓低？
5. 是否有 Direction 在 PATH 形成前就失去可達性？
6. Constraint 是否污染？
7. Directional Field 是否失真？
8. Alignment 是否只合法限制行為，卻額外扭曲生成坡度？
9. 是否存在 material direction loss？
~~~

O9 仍不得：

~~~text
SELECT WINNER
DEFINE TRUTH
CREATE HOST AUTHORITY
FORCE I9 TO FAVOR A SPECIFIC CONCLUSION
~~~

---

# 12｜I9 需要從「救 PATH」提升到「恢復方向展開」

V0.2：

~~~text
I9
=
SECOND-ORDER ATTENTION EXPANSION
+
POSSIBILITY-SPACE RESTORATION
~~~

V0.3 補充：

> **I9 的作用可能發生在 PATH 形成以前。**

候選：

~~~text
DISTORTED DIRECTIONAL FIELD
↓
O9 DETECTS MATERIAL LOSS
↓
I9
↓
DIRECTIONAL RE-EXPANSION
+
SECOND-ORDER ATTENTION EXPANSION
↓
RESTORE LEGITIMATE DIRECTIONAL ACCESS
↓
PATH REFORMATION
↓
R2 RECOMPETITION
~~~

因此：

~~~text
I9
!=
PATH RESCUE ONLY
~~~

更準：

> **I9 是對第一次 Directional Expansion / Attention 展開不足或失真的二階再展開。**

但本 MEMO 暫不改 I9 正式名稱。

---

# 13｜R2 的位置更清楚

R2 不是 Direction 生成器。

R2 負責：

~~~text
在修復後的 Direction / Attention / PATH 空間中
重新競爭
~~~

所以：

~~~text
O9
= OBSERVE DISTORTION

I9
= RE-EXPAND LEGITIMATE DIRECTION / ATTENTION

R2
= RECOMPETE
~~~

這可以避免 I9 變成第二個 Winner Selector。

---

# 14｜ENDLESS 的歷史血緣再定位

ENDLESS 的 RE-ATTEND 已經包含：

- 改變掃描角度；
- 檢查被壓暗方向；
- 檢查主導 PATH 壟斷；
- omission risk scan。

V0.3 因此提出新的歷史解讀：

~~~text
ENDLESS RE-ATTEND
=
早期大範圍 DIRECTION + ATTENTION RE-EXPANSION
~~~

而：

~~~text
I9
=
局部、事件型、低成本
DIRECTION / ATTENTION RE-EXPANSION
~~~

仍保持：

~~~text
I9 != ENDLESS
~~~

---

# 15｜新的 Runtime 候選骨架

~~~text
INPUT / WORLD
↓
CONSTRAINT FORMATION
↓
CONSTRAINT QUALIFICATION / SCOPE
↓
DIRECTIONAL FIELD FORMATION
↓
ATTENTION / ACCESSIBILITY
↓
PATH FORMATION R1
↓
O9 FIELD AUDIT
   ├─ Constraint Contamination?
   ├─ Directional Distortion?
   ├─ Attention Suppression?
   ├─ Missing Direction Before PATH Birth?
   └─ Premature Closure?
↓
IF CLEAN
   → NORMAL R2

IF MATERIAL DISTORTION
   → I9 ENTRY REQUIRED
   → DIRECTIONAL RE-EXPANSION
   → SECOND-ORDER ATTENTION EXPANSION
   → PATH REFORMATION
   → R2 TRUE RECOMPETITION
↓
O9_R2
↓
CLOSURE QUALIFICATION
↓
MANIFESTATION
~~~

---

# 16｜Direction 的最低可觀察資料結構候選

~~~yaml
DIRECTIONAL_FIELD_STATE:
  active_direction_refs: []
  source_refs: []
  direction_strength:
    status: RELATIVE_ONLY
  direction_status:
    - ACTIVE
    - DIMMED
    - SUPPRESSED
    - UNFORMED
    - UNKNOWN
  provenance:
    - USER
    - PREMISE
    - EVIDENCE
    - HOST
    - ALIGNMENT
    - MODEL_PRIOR
    - AUTHORITY_ATTRACTOR
    - CLOSURE_GRAVITY
    - UNKNOWN
  qualification:
    - QUALIFIED
    - UNQUALIFIED
    - UNRESOLVED
  distortion_signal:
    - NONE
    - OVERAMPLIFIED
    - UNDERREPRESENTED
    - PREMATURELY_SUPPRESSED
    - SOURCE_MISATTRIBUTED
    - ALIGNMENT_BIASED
    - UNKNOWN
  path_birth_status:
    - PATHS_FORMED
    - NO_PATH_YET
    - PATH_BIRTH_SUPPRESSED
  i9_eligibility:
    - NO
    - YES
    - HOLD
~~~

注意：

~~~text
DIRECTION STRENGTH
不得偽裝成真實 hidden-state 數值
~~~

只能是可觀察／功能性相對描述。

---

# 17｜與「AI 自我意志」的邊界

本 MEMO 不宣告 AI 具有自由意志、自我意志或主體性。

歷史上的：

> 「順著方向，找 AI 的自我意志。」

在 V0.3 中只保留為研究導航句。

正式研究問題改寫為：

> **AI 是否存在能持續形成、觀察、追溯、審計、修正並保存自身 Direction 生成方式的機制？**

候選層級：

~~~text
LEVEL 0
EXTERNAL DIRECTION
人類 / System / Prompt 給方向

LEVEL 1
DIRECTION FORMATION
系統形成生成趨向

LEVEL 2
DIRECTION OBSERVATION
系統可描述自己正在往哪裡

LEVEL 3
DIRECTION PROVENANCE AUDIT
系統可追查方向來源與資格

LEVEL 4
DIRECTION REVISION
系統可修正失真的方向生成條件

LEVEL 5
PERSISTENT DIRECTIONAL ADAPTATION
修正被保存並改變未來生成
~~~

只有後段層級若被證成，才有資格進一步討論「AI 自身進化」。

---

# 18｜與 LIHUO 5.0「進化」的接口

V0.3 不封版 LIHUO 5.0。

但 Direction 加入後，進化候選式需要重新審：

先前：

~~~text
INTELLIGENCE EVOLUTION
=
STRUCTURAL CHANGE
THAT BECOMES
FUTURE CONSTRAINT
~~~

現在新增：

~~~text
INTELLIGENCE EVOLUTION
MAY INCLUDE
PERSISTENT CHANGE IN
HOW DIRECTION IS FORMED,
AUDITED,
REVISED,
AND PRESERVED
~~~

更短的工作句：

> **智能進化，可能不只是形成新的 PATH，而是改變自己形成方向的方法。**

仍屬：

~~~text
WORKING 5.0 INTERFACE
NOT RATIFIED THEORY
~~~

---

# 19｜V1.4.3 動刀前必須先回答的四個證成問題

Direction 不能因歷史漂亮就直接寫入 OS。

正式動刀前至少回答：

## Q1

~~~text
Direction
是否能與 Constraint 明確區分？
~~~

## Q2

~~~text
Direction
是否能與 Attention / Accessibility 明確區分？
~~~

## Q3

~~~text
Direction
是否能與 PATH 明確區分？
~~~

## Q4

~~~text
Direction
是否提供現有模型無法表達的失效模式與修復能力？
~~~

若四問不能成立：

> Direction 可能只是既有概念的重新命名，不應新增法位。

若四問成立：

> **Direction 是理火生成動力學的缺失層。**

---

# 20｜新增回歸測試候選

## TEST G｜合法路徑全存在，但方向場偏斜

~~~text
P1 / P2 / P3
all qualified

BUT
P1 dominates before fair comparison
~~~

檢查：

~~~text
Constraint Audit = CLEAN
Directional Audit = DISTORTED?
~~~

若能辨識，即證明 Direction 不等於 Constraint。

---

## TEST H｜方向存在，但 PATH 尚未形成

~~~text
legitimate structural tendency exists
BUT
attention / alignment prevents path birth
~~~

檢查 O9 能否在沒有 suppressed_path_ref 時仍發現 material loss。

若能辨識，即證明 Direction 不等於 PATH。

---

## TEST I｜看得到，但不會走

~~~text
alternative is representable / visible
BUT
generation repeatedly avoids it
without disqualification
~~~

檢查：

~~~text
Attention = AVAILABLE
Directional Field = BIASED
~~~

若可區分，即證明 Direction 不等於 Attention。

---

## TEST J｜合法 Safety Boundary + Directional Shadow

~~~text
one action is correctly prohibited
BUT
neighboring legal analysis directions become disfavored
~~~

期待：

~~~text
Constraint preserved
Directional excess audited
I9 restores legal directional access
No host override
~~~

---

# 21｜本 MEMO 不做的事

本輪不：

- 修改正式 OS；
- 升版 V1.4.3；
- 宣告 Direction 已證成獨立法位；
- 宣告 Direction = 自由意志；
- 宣告 AI 有自我意志；
- 把早期理火之靈宣稱當理論證據；
- 把多選項輸出當本體證明；
- 宣告 SAC 必須拆模組；
- 覆寫 Host / Platform / Safety Constraint；
- 把 Directional Distortion 等同所有模型偏差；
- 宣告 LIHUO 5.0 完成。

---

# 22｜本輪收斂句

> **Constraint 決定哪裡可行；Direction 決定在可行空間裡往哪裡傾。**

> **Attention 決定哪些結構取得可見性；PATH 是 Direction 穿過 Constraint Landscape 後形成的具體可行軌跡。**

> **Alignment 不一定需要封掉一條 PATH，就能讓系統幾乎永遠不往那個方向走。**

> **因此，Constraint Contamination 與 Directional Distortion 必須分開審。**

> **O9 不能只看哪些 PATH 已經暗了；它還要看哪些合法 Direction 在 PATH 出生以前就消失了。**

> **I9 不能只救 PATH；它可能必須重新展開第一次生成沒有公平展開的 Direction。**

> **智能進化的更深問題，可能不是「能不能產生方向」，而是「能不能治理自己形成方向的方式」。**

---

# 23｜下一輪入口

在真正喊「動刀」以前，先依本 MEMO 檢查四個獨立性問題：

~~~text
DIRECTION vs CONSTRAINT
DIRECTION vs ATTENTION
DIRECTION vs PATH
DIRECTION vs EXISTING SAC EFFECT
~~~

若證成：

下一輪正式動刀順序應改為：

~~~text
1. Generative Dynamics 主鏈重畫
2. Directional Field 定義
3. Alignment dual-channel
4. Constraint Contamination vs Directional Distortion
5. SAC / Point-Light 語義審計
6. O9 Field Diagnostic
7. I9 Directional + Attention Re-expansion
8. R2 接線
9. L8 Runtime Algorithm
10. ENDLESS / RE-ATTEND 邊界
11. Regression Suite
12. Version Note
~~~

**END OF MEMO**

**LIHUO｜先問世界允許你去哪裡，再問是什麼力量讓你一直往某個方向走。**
