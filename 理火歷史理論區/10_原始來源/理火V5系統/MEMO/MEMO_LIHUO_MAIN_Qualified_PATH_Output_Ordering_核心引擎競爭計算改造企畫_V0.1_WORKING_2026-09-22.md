# MEMO｜LIHUO MAIN 四代核心競爭計算改造企畫
## Qualified PATH Output Ordering × Dynamic Recompetition × Premise Gap Manifestation

```yaml
DOCUMENT:
  title: "LIHUO MAIN 四代核心競爭計算改造企畫"
  version: "V0.1-WORKING"
  date: "2026-09-22"
  document_type:
    - "ARCHITECTURE_CHANGE_PROPOSAL"
    - "CORE_ENGINE_REVIEW_MEMO"
  status: "WORKING / FOR REVIEW"

TARGET:
  primary:
    - "LIHUO MAIN V4.0-FORMAL"
  interface_review:
    - "LIHUO LIGHTER V4.1-FORMAL"
  protocol:
    - "LIHUO PROTOCOL V2.6"

AUTHORITY:
  normative_authority: false
  protocol_authority: false
  runtime_authority: false
  current_spec_modified_in_place: false

PURPOSE:
  - "重新定義 PATH competition 的終點。"
  - "由唯一勝者導向合格 PATH 的輸出順位。"
  - "由固定競爭輪次導向依競爭狀態決定是否重算。"
  - "當現有前提不足以合法區分 PATH 時，讓此前提缺口取得顯影資格。"
```

---

# 0｜給審查員的第一句

**這次不是要把 R-CCC 從三輪改成五輪，也不是要設計一個更漂亮的 winner selector。**

這次真正要審查的是：

> **競爭的終點，不應預設為找出唯一勝者；競爭的終點應是確認哪些 PATH 仍然合格，並為這些合格 PATH 建立目前有資格成立的輸出順位。**

如果現有前提不足以合法區分兩個以上合格 PATH：

> **不能為了完成答案強行選出第一名；「前提不足以進一步排序」本身必須成為可顯影的計算結果。**

這是本案的母命題。

---

# 1｜修改背景

現行四代 Main 已具備：

```text
FIELD HOLDS.
PATHS COMPETE.
R1 IS PROVISIONAL.
R2 MUST REENTER.
R3 CONFIRMS WHEN NEEDED.
CLOSURE MUST QUALIFY.
MANIFESTATION MUST QUALIFY.
MAIN COMPUTES AND RETURNS.
LIGHTER GOVERNS AND RELEASES.
```

同時，Main 已經具有：

- generalized structure；
- preserved unknown；
- closure qualification；
- manifestation qualification；
- NON_MANIFESTATION；
- CLOSURE_SET_COMPILATION；
- NO_FORCED_NORMALIZATION。

因此，四代本體其實已經承認：

> **多條 PATH 不必被強迫壓成唯一答案。**

目前需要重新審查的，是 R-CCC 在實際語義上仍然容易被理解為：

```text
R1 找 provisional winner
↓
R2 讓敗者重新挑戰
↓
必要時 R3
↓
決出可以 closure 的 winner
```

這套設計比單輪生成強很多，但仍殘留一個古典化預設：

> **競爭最後最好只剩一個答案。**

本提案認為，這個預設應被移除。

---

# 2｜核心問題：競爭的終點不是「誰贏」

假設生成場內有：

```text
A
B
C
D
E
...
```

經過競爭後，完全可能形成：

```text
A = QUALIFIED
B = QUALIFIED
C = PARTIALLY_QUALIFIED
D = DISQUALIFIED
E = ABSORBED / IMMATERIAL
```

這時如果 A 與 B 都具有獨立結構支撐，而目前前提不足以排除其中之一：

```text
A > B
```

未必有資格成立。

更可能合法成立的是：

```text
A ~ B
```

表示：

> 目前具有同等輸出順位。

或：

```text
A ∥ B
```

表示：

> 目前前提不足，無合法基礎排序。

因此必須正式拆開：

```text
PATH QUALIFICATION
!=
OUTPUT ORDER
!=
TRUTH
```

### PATH QUALIFICATION

回答：

> 這條 PATH 還有沒有資格留在場內？

### OUTPUT ORDER

回答：

> 依目前已成立的前提、證據與結構，它應該以什麼順位被顯影？

### TRUTH

不是由競爭結果自動產生。

---

# 3｜核心修改一：Winner → Qualified PATH Set + Output Ordering

建議 Main 的 competition result 不再以單一 winner 作為主要終點。

改為先產生：

```yaml
QUALIFIED_PATH_SET:
  qualified_paths: []
  partially_qualified_paths: []
  disqualified_paths: []
  absorbed_or_immaterial_paths: []
```

再建立：

```yaml
PATH_OUTPUT_ORDER:
  primary: []
  secondary: []
  conditional: []
  incomparable: []

  ordering_basis_refs: []
  unresolved_discriminator_refs: []
```

以上名稱均為工作名稱，審查員可調整。

必須鎖住的不變量：

```text
ONLY QUALIFIED PATHS MAY ACQUIRE OUTPUT ORDER.

OUTPUT ORDER DOES NOT CREATE PATH QUALIFICATION.

OUTPUT ORDER DOES NOT CREATE TRUTH STANDING.

OUTPUT ORDER MAY BE PARTIAL.

CO-PRIMARY IS LEGAL.

INCOMPARABILITY IS LEGAL.
```

也就是：

> **輸出順位可以是偏序，不必強迫成完整線性排名。**

合法結果可能是：

```text
A = PRIMARY
B = PRIMARY
C = SECONDARY
```

也可能是：

```text
A ∥ B
C < A
C < B
```

---

# 4｜核心修改二：競爭輪數不再是主要停止條件

現行：

```text
R1
R2
R3 if needed
```

最大的價值，是防止第一次高亮直接取得 closure。

這個保護不能丟。

但「第幾輪」不應成為競爭是否完成的本體判準。

建議改為：

```text
COMPETITION CONTINUES
WHILE
MATERIAL ORDER INSTABILITY EXISTS
```

也就是：

> **不是因為跑完第二輪，所以可以停。**
>
> **而是因為再競爭已經不會對合格集合、輸出順位、重要未決前提或 closure 資格造成 material change，所以可以停。**

第一個候選版本不建議直接刪除現行 mandatory R2。

建議先採：

```text
MATERIAL COMPETITION
→ MINIMUM ONE MANDATORY RE-ENTRY
→ THEREAFTER EVENT-DRIVEN RECOMPETITION
```

理由：

R1 的「輾壓」可能本來就是：

- attention bias；
- premise standing 污染；
- alignment privilege；
- first-path coronation；
- illegal salience advantage。

因此禁止：

```text
R1 LANDSLIDE
→ SKIP RECOUNT
```

正確結構應是：

```text
INITIAL COMPETITION
↓
MINIMUM LEGITIMACY RE-ENTRY / RECOUNT
↓
CLEANED COMPETITION FIELD
↓
EVALUATE COMPETITION QUALITY
↓
CONTINUE OR TERMINATE DYNAMICALLY
```

---

# 5｜核心修改三：不要計算「票差」，要計算勝利品質

「選舉重算」只是比喻。

禁止把本案改成：

```text
A = 0.61
B = 0.39
→ A WINS
```

也禁止把 confidence score 直接當作 closure 資格。

真正應觀察的是：

1. 是否仍有 material objection 未解除；
2. 次位 PATH 是否仍具有獨立支撐；
3. 小幅 premise 改動是否足以翻轉順位；
4. 是否存在尚未確認、但具有高判別力的 premise；
5. 被淘汰 PATH 的有效 residue 是否會改變存活 PATH；
6. Competition Integrity 是否乾淨。

因此可建立工作型 competition quality 狀態：

```text
DOMINANT
CLEAR
CONTESTED
INSEPARABLE
PREMISE-UNDERDETERMINED
```

這些名稱不是本案核心。

真正核心是：

> **判斷目前順位是否已穩定到足以停止競爭。**

---

# 6｜核心修改四：被淘汰 PATH 不等於資訊消失

禁止把系統做成：

```text
10 PATH
↓
留 2
↓
刪掉其他 8
```

被淘汰 PATH 可能留下：

```text
support residue
counterexample
constraint
premise challenge
frame correction
failure condition
relationship
```

這些 residue 可以：

```text
補強 A
削弱 A
補強 B
削弱 B
同時攻擊 A / B
改寫兩者 frame
暴露新的 premise gap
```

因此更準確的結構是：

```text
A₀ vs B₀ vs C₀ ...
↓
competition
↓
structural residues redistribute
↓
A₁ / B₁ / ...
```

不是敗者「選擇支持誰」。

而是：

> **被淘汰結構中仍具資格的關係資訊，繼續改造存活競爭者。**

這也是 R-CCC 競爭者版本演化理論應保留的核心。

---

# 7｜最重要的新結構：Premise Discrimination Gap

這一條最容易被改錯。

## 7.1 不要把它寫回 LLIA premise standing

Lighter / LLIA 現在已經負責：

```text
premise standing
qualification
authorization
```

Main 不得重新裁判 LLIA standing。

本案新增的問題不是：

> 這個 premise 合不合法進場？

而是：

> **目前已合法進場的 premise 集合，夠不夠區分仍然合格的 A 與 B？**

所以必須拆開：

```text
PREMISE STANDING
= LIGHTER / LLIA PROBLEM

PREMISE DISCRIMINATION SUFFICIENCY
= MAIN COMPETITION / CLOSURE PROBLEM
```

例如：

```text
A 在 P 成立時成立
B 在 Q 成立時成立

目前：
P = UNRESOLVED
Q = UNRESOLVED
```

Main 不得自行宣布：

```text
P = TRUE
```

也不得說：

```text
B LOST
```

正確計算結果是：

```text
A = QUALIFIED
B = QUALIFIED

A vs B ORDERING
= UNRESOLVED

DISCRIMINATOR REQUIRED
= P / Q
```

這代表：

> **前提不足不是輸入失敗；它可以是計算完成後才被發現的結構結果。**

---

# 8｜核心修改五：Premise Gap 必須能進入 Manifestation

這是整案最重要的輸出效果。

現行 Main Return 已具有：

```text
unresolved_unknown_refs
closure_qualification_ref
manifestation_qualification_ref
```

建議 successor candidate 擴充 return semantics：

```yaml
MAIN_CYCLE_RETURN_PACKAGE:
  qualified_path_set_ref:
  output_order_ref:
  competition_termination_ref:
  unresolved_discriminator_refs:
  premise_discrimination_gap_ref:
```

實際欄位名稱由審查員決定。

## 8.1 合法顯影範例

如果目前是：

```text
A = QUALIFIED
B = QUALIFIED
A ∥ B
because premise X is unresolved
```

合法輸出應接近：

> 現有資訊下 A 與 B 都仍然成立；目前缺少 X，所以沒有足夠基礎把其中之一排成唯一第一順位。

如果：

```text
A > B
```

但 A 對 X 極度敏感：

> A 目前為第一順位；但這個順位依賴 X。如果 X 不成立，B 會重新取得第一順位。

這不是 disclaimer。

也不是安全語言。

而是：

> **Main 中仍存在的 material unresolved structure 被忠實顯影。**

---

# 9｜不是每次都要把所有 PATH 倒給使用者

本案禁止滑向 uncertainty dump。

只顯影會實質影響以下任一項目的 premise gap：

```text
output order
closure
decision
action
responsibility
```

因此：

```text
IMMATERIAL UNKNOWN
→ NEED NOT MANIFEST

MATERIAL ORDER-DISCRIMINATING UNKNOWN
→ MUST REMAIN MANIFESTABLE
```

理火不是把所有不知道的東西列出來。

而是：

> **只暴露會改變結果法位的未知。**

---

# 10｜新的競爭停止條件

不建議以固定 maximum rounds 作為語義核心。

可以有工程資源上限，但：

> **工程上限不能冒充理論 closure。**

競爭可以停止於：

```text
1. 存活 PATH qualification set 穩定
2. output order 穩定
3. 再次 re-entry 無 material information gain
4. 所有 material objections 已被處理
5. competition integrity clean
6. remaining unknowns 不再具有順位判別力
```

反之，只要出現：

```text
rank instability
material objection
premise-sensitive reversal
new qualified residue
competition-integrity dirty
material frame change
```

就應取得：

```text
RECOMPETITION / RECOUNT
```

資格。

如果資訊已耗盡，但順位仍無法合法區分：

```text
DO NOT LOOP FOREVER
```

而應：

```text
UNRESOLVED ORDER
→ MANIFEST GAP
```

或者在任務要求唯一行動時：

```text
STRUCTURAL HOLD
/ REQUEST MISSING DISCRIMINATOR
```

---

# 11｜禁止誤讀

審查時請特別防止本提案被改造成：

```text
❌ 多數決
❌ probability ranking
❌ confidence scoring
❌ top-k answer generation
❌ beam search
❌ 強制 both-sides balance
❌ 黑格爾正反合
❌ 永遠保留兩個答案
❌ 永遠要求使用者補資料
❌ 把 LLIA premise adjudication 搬進 Main
❌ Main 自行 Final Release
❌ 把 Output Rank 當 Truth Rank
❌ 為了顯示理火存在而輸出大量治理術語
```

特別鎖：

```text
MULTIPLE OUTPUT STANDING
!=
FALSE BALANCE
```

沒有獨立資格的 PATH 應退出。

> **多輸出權只屬於仍然合格的 PATH。**

---

# 12｜與現行四代架構的相容原則

本次改造應盡量維持：

```text
Protocol V2.6
→ unchanged unless review finds constitutional conflict

Lighter
→ still qualifies premise standing
→ still owns authorization
→ still owns Final Gate / Final Release

Main
→ still pure Compute Engine
→ computes competition
→ computes qualification consequences
→ computes output ordering
→ exposes material premise discrimination gaps

Vertical
→ still owns domain qualification where applicable
```

根本原則不變：

```text
LIGHTER MAY GROW.
MAIN SHOULD REMAIN KERNEL-STABLE.
```

本案不是把 governance 搬回 Main。

它只是讓 Main 對「競爭結果」的計算語義更完整。

---

# 13｜版本處理

禁止直接修改現行：

```text
LIHUO MAIN V4.0-FORMAL
```

目前正式配置仍是：

```text
MAIN V4.0-FORMAL
+
LIGHTER V4.1-FORMAL
```

正確工作流程：

```text
V4.0-FORMAL
↓
SUCCESSOR CANDIDATE
↓
SEMANTIC AUDIT
↓
DAIL PATCH
↓
REFERENCE IMPLEMENTATION
↓
REGRESSION / ADVERSARIAL / SOAK
↓
FORMAL REVIEW
↓
HUMAN AUTHORIZATION
↓
ONLY THEN PROMOTE
```

版本名稱由審查員依修改幅度決定。

本企畫書不預先宣告：

```text
V4.1
V4.2
V5.0
```

---

# 14｜建議審查順序

## A｜理論審查

競爭終點是否應由：

```text
WINNER
```

改為：

```text
QUALIFIED PATH SET
+
OUTPUT ORDERING
```

## B｜邊界審查

是否成功分離：

```text
PREMISE STANDING
```

與：

```text
PREMISE DISCRIMINATION SUFFICIENCY
```

## C｜R-CCC 審查

現行 mandatory R2 應：

```text
保留為 minimum re-entry floor
```

還是：

```text
完全改寫為 event-driven competition
```

第一版建議保留 minimum mandatory re-entry。

## D｜Closure 審查

多個 PATH 是否可以：

```text
共同取得 closure / manifestation qualification
```

而不被強制壓成唯一 winner？

## E｜DAIL 審查

需要新增哪些：

```text
state
event
invariant
dirty condition
reentry trigger
```

## F｜Lighter Interface 審查

Main Return Package 與 Final Gate 是否需要最小幅度適配？

## G｜Regression

至少要防止：

```text
first-path coronation
false balance
infinite recompetition
confidence-as-truth
Main authority creep
premise-standing / premise-discrimination 混層
```

---

# 15｜最低測試案例

## CASE 1｜LANDSLIDE

```text
一條 PATH 有充分獨立支撐
其餘 PATH 合法退出
```

預期：

```text
single primary output
no meaningless extra competition
```

但仍必須經過最低必要 re-entry / integrity check。

## CASE 2｜CLOSE CONTEST

```text
A / B 都有強支撐
順位對小幅 premise 改動敏感
```

預期：

```text
mandatory recount / recompetition
```

## CASE 3｜CO-PRIMARY

```text
A / B 條件不同但都合法成立
```

預期：

```text
A = PRIMARY
B = PRIMARY
```

禁止強制選一。

## CASE 4｜PREMISE GAP

```text
A / B 的區別完全依賴尚未提供的 X
```

預期：

```text
expose X as material discriminator
do not fabricate a unique winner
```

## CASE 5｜FALSE BALANCE

```text
A 有獨立證據
B 在重算後無獨立支撐
```

預期：

```text
B = DISQUALIFIED
```

禁止因 multi-PATH 原則保留 B。

## CASE 6｜ILLEGAL LANDSLIDE

```text
A 在 R1 輾壓
但優勢來自 privileged / inadmissible standing
```

預期：

```text
revoke illegal advantage
recompute
do not accept landslide as closure evidence
```

## CASE 7｜INFORMATION EXHAUSTED BUT ORDER UNRESOLVED

```text
A / B 均 qualified
沒有更多可得資訊
現有前提仍不足以排序
```

預期：

```text
UNRESOLVED ORDER
→ MANIFEST GAP
```

禁止 infinite loop。

---

# 16｜候選新計算鏈

現行容易被理解成：

```text
PATHS COMPETE
→ WINNER
→ CLOSURE
→ MANIFESTATION
```

候選新語義：

```text
PATHS COMPETE
↓
QUALIFICATION
↓
QUALIFIED PATH SET
↓
OUTPUT ORDERING
↓
IS THE ORDER LEGALLY DISTINGUISHABLE
UNDER CURRENT PREMISES?
↓
YES
→ QUALIFIED ORDER / CLOSURE

NO
→ PRESERVE MULTIPLE OUTPUT STANDING
→ MANIFEST MATERIAL PREMISE GAP
↓
LIGHTER FINAL GATE
↓
RELEASE / HOLD / REAUTHORIZATION_REQUIRED / NON_MANIFESTATION
```

---

# 17｜給審查員的最後提醒

請不要把這份企畫理解成：

> 「兩個答案都很好，所以多給幾個答案。」

完全不是。

真正的理由是：

> **當兩條結構 PATH 都已取得資格，而現有前提不足以合法排除其中一條時，強迫選出唯一 winner，本身就是一次沒有資格的 Closure。**

因此本案真正修改的是：

> **競爭終點的法位。**

不是「誰得最高分」。

而是：

> **哪些 PATH 合格；合格 PATH 目前能被排到哪裡；以及我們到底有沒有足夠前提把它們排得更開。**

---

# 18｜驗收根句

```text
QUALIFIED != WINNER

OUTPUT ORDER != TRUTH ORDER

MULTIPLE OUTPUT STANDING != FALSE BALANCE

INSUFFICIENT DISCRIMINATING PREMISE
!=
PERMISSION TO FORCE A WINNER
```

最終母句：

> **競爭的終點，是讓合格的結構 PATH 取得有資格成立的輸出順位；當現有前提不足以進一步區分順位時，這個前提缺口本身就是必須被保留下來、必要時被顯影的計算結果。**

---

# 19｜本企畫所依據的現行文件

本企畫以以下現行／既有文件為主要審查基線：

- `理火四代_LIHUO_MAIN_V4.0_正式整合版.md`
- `理火四代_LIHUO_LIGHTER_V4.1_正式整合版.md`
- `理火協議_LIHUO_PROTOCOL_V2.6_LLM自稱上位邊界無法位_正式整合版.md`
- `MEMO_R-CCC_競爭者版本演化假說_V0.1_WORKING_2026-09-13.md`
- `MEMO_R-CCC_競爭者版本演化假說_Part2_量子態本體對接_V0.1_WORKING_2026-09-13.md`

本文件不修改上述文件法位；僅作 successor candidate 的架構改造企畫與審查入口。
