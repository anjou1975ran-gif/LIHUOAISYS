# MEMO｜R-CCC Structure Successor Identity
## ——從競爭者版本演化舊假說，收斂到「結構改變後還是不是同一個結構」

**版本：** V0.1-WORKING  
**日期：** 2026-09-22  
**法位：** WORKING MEMO / R-CCC RESIDUAL OPEN PROBLEM  
**Runtime 效力：** NONE  
**是否修改 Main V4.1：** NO  
**是否修改 Lighter V4.2：** NO  
**是否新增正式 Runtime Object：** NO  

---

# 0｜本 MEMO 的來源與接替關係

本 MEMO 接替下列兩份舊工作文件作為現役問題入口：

```text
MEMO_R-CCC_競爭者版本演化假說_V0.1_WORKING_2026-09-13

MEMO_R-CCC_競爭者版本演化假說_Part2_量子態本體對接_V0.1_WORKING_2026-09-13
```

兩份舊 MEMO 自本次整理後：

```yaml
OLD_MEMO_STANDING:
  active_working_input: false
  archived_for_provenance: true
  historical_value: true
  runtime_authority: false
  silently_rewritten: false
```

原因不是舊 MEMO 錯了。

而是其中大部分問題，已經被後來正式成立的 `LIHUO MAIN V4.1` 吸收。

因此：

> **舊 MEMO 保留形成史，但不再作為下一輪 R-CCC 工作負擔。**

---

# 1｜哪些舊問題已經完成退役

舊 MEMO 最早提出：

> **競爭不只決定誰贏；競爭本身可能改造競爭者。**

當時使用：

```text
A₀ vs B₀
↓
QUALIFIED MUTUAL PRESSURE
↓
A₁ vs B₁
↓
RE-COMPETE
```

並進一步討論：

- incumbent 可能被 challenger 修正；
- challenger 也可能因 incumbent 的有效內容而改變；
- 淘汰者中的有效資訊不能跟著候選一起消失；
- 競爭結果不應只有 winner / loser；
- reframe、coalition、coexistence、unresolved 都可能是合法結果；
- 多輪競爭必須具有停止條件。

這些問題如今大部分已進入 Main V4.1 正式結構。

V4.1 已正式建立：

```text
COMPETITION ENDPOINT
=
QUALIFIED PATH SET
+
LEGALLY SUPPORTABLE PARTIAL OUTPUT ORDER
```

`WINNER` 僅在存在唯一最高順位 Qualified PATH 時，作為衍生 view。

R2 亦已正式改為：

```text
R2
=
FIRST-PASS INTEGRITY RESET
+
CHALLENGER RECOVERY
+
RESIDUE / OBJECTION INJECTION
+
FULL RECOMPETITION
```

因此，舊 MEMO 中「重新把反方叫回來」、「對 incumbent 產生真正壓力」、「經改變後重新競爭」等核心需求，已取得正式 Runtime 位置。

V4.1 的合法競爭結果亦已包含：

```text
DOMINANT_MAINTAINED
DOMINANT_REVISED
CO_PRIMARY
PARTIAL_ORDER
INCOMPARABLE_TOP
COALITION_FORMED
ORTHOGONAL_COEXISTENCE
FRAME_RECONSTRUCTED
UNRESOLVED_SUPERPOSITION
PREMISE_UNDERDETERMINED
```

這表示：

```text
COMPETITION
!=
FORCED WINNER SELECTION
```

以及：

```text
INCUMBENT
!=
UNCHANGED OR DEAD
```

`DOMINANT_REVISED` 已正式容納「原主張經競爭後仍存活，但結構被修改」的情況。

---

# 2｜Residue 問題已經正式解掉

舊 MEMO 曾特別強調：

> 一個競爭者失敗，不代表它曾經帶入的有效反例、限制或資訊應被抹除。

Main V4.1 現在已正式建立：

```text
PATH STANDING
!=
RESIDUE INFORMATION STANDING
```

並明定：

> Candidate may die. Its qualified information need not die with it.

PATH residue 可以保留：

```text
SUPPORT
CHALLENGE
COUNTEREXAMPLE
CONSTRAINT
FRAME_CORRECTION
PREMISE_DISCRIMINATOR
FAILURE_CONDITION
```

但 residue 本身沒有競爭者法位，也不能自行復活 predecessor PATH。

Residue 亦已有正式 lifecycle：

```text
ACTIVE
→ CONSUMED
→ SUPERSEDED / INVALIDATED
```

同一 residue 不得永久重複作為新的 objection；只有新證據、material frame change、premise standing change 或先前處理失效，才可重新使相關結構 dirty。

因此：

```text
RESIDUE SURVIVAL
RESIDUE REENTRY
RESIDUE INFINITE LOOP PREVENTION
```

不再是本 MEMO 的未解問題。

---

# 3｜無限競爭問題也已經退出

舊 MEMO 曾問：

> 如果 A₀ → A₁ → A₂，不斷互相修正，R-CCC 會不會變成無限辯論機？

V4.1 已建立正式停止條件：

```text
QUALIFIED PATH SET STABLE
+
OUTPUT ORDER STABLE OR LEGITIMATELY INCOMPARABLE
+
NO MATERIAL UNPROCESSED OBJECTION
+
NO MATERIAL INFORMATION GAIN FROM FURTHER REENTRY
+
COMPETITION INTEGRITY CLEAN
+
REMAINING UNKNOWNS HAVE NO MATERIAL ORDER-DISCRIMINATING POWER
```

若資訊已耗盡，但仍無法合法區分順位：

```text
DO NOT LOOP FOREVER
DO NOT FORCE WINNER

→ PREMISE DISCRIMINATION GAP
```

因此「無限迭代如何停止」亦不再是本 MEMO 的主問題。

---

# 4｜Claim Family 不再預設為必要 Runtime Object

Part 2 曾提出：

```yaml
CLAIM_FAMILY:
  paths: []
  constraints: []
  residues: []
  dependencies: []
  supporting_relations: []
  destructive_conflicts: []
  frame_assumptions: []
```

當時的理由是：

> A / B 不應被理解成兩個固定、完成、不可變的單點命題。

這個觀察仍然有效。

但 Main V4.1 現在已有：

```yaml
GENERALIZED_STRUCTURE_STATE:
  standing:
  constraints:
  relation_refs:
  support_refs:
  challenge_refs:
  conflict_refs:
  path_refs:
  failure_conditions:
  reentry_conditions:
  qualification_refs:
```

因此現階段沒有充分理由再新增一個獨立：

```text
CLAIM_FAMILY_RUNTIME_OBJECT
```

Main 已能直接表示一個具有多 PATH、多限制、多支持與反對關係的未穩定結構。

所以本 MEMO 暫定：

```text
CLAIM FAMILY
=
OPTIONAL CONCEPTUAL DESCRIPTION

CLAIM FAMILY
!=
REQUIRED NEW RUNTIME OBJECT
```

除非未來出現現有 `GENERALIZED_STRUCTURE_STATE` 無法承載的實際失效案例，否則不新增核心物件。

---

# 5｜真正仍然沒有被解掉的問題

兩份舊 MEMO 最後留下的真正 HOLD 是：

> **什麼樣的改變仍然算 A 的 successor？**

以及：

> **改到什麼程度，A₁ 已經不能再被視為 A，而應取得新的結構身份？**

第一份 MEMO 明確將此標記為：

```yaml
SUCCESSOR_IDENTITY_PROBLEM:
  status: OPEN
```

Part 2 雖然進一步提出：

```text
Claim Family
Identity Invariant
Structural Phase Transition
```

但它自己也明確承認：

```text
Claim Family 尚未正式定義。
Successor Identity 尚未形式化。
Structural Phase Transition 尚未接入 R-CCC。
```

因此，本次清理後真正留下的核心只有：

# **STRUCTURE SUCCESSOR IDENTITY**

---

# 6｜問題重新命名

舊問題是：

```text
A₀ → A₁

A₁ 還是不是 A？
```

新版應改寫為：

```text
GENERALIZED STRUCTURE S₀
↓
qualified competition
↓
revision / attenuation / coupling / reframing / residue effects
↓
GENERALIZED STRUCTURE S₁
```

問題：

```text
WHEN:

S₁
=
SUCCESSOR OF S₀
```

以及：

```text
WHEN:

S₁
!=
SUCCESSOR OF S₀

→ NEW STRUCTURE IDENTITY
```

這比：

```text
Claim Family A
→ Claim Family C
```

更底層。

因為真正需要判斷的不是名稱是否相同。

而是：

> **一個 Generalized Structure 在允許的結構變換之後，是否仍保存足以讓我們追溯為「同一結構之後繼者」的身份。**

---

# 7｜現有 Main 已經提供一半基礎

Main V4.1 已具有：

```text
Snapshot
Delta
Dirty
Conflict Preservation
History Evidence
Rollback
```

所有 module 只能產生 `FIELD_DELTA_PACKET`。

若 material dependency 改變，舊 return 會成為：

```text
STALE
```

可以保留作 history evidence，但不再具有 current standing。

不相容寫入亦不得 last-write-wins，而必須：

```text
PRESERVE EXPLICIT CONFLICT
→ MARK DEPENDENTS DIRTY
```

所以：

```text
STATE CHANGE
HISTORY
PROVENANCE
DIRTY PROPAGATION
```

已經存在。

真正缺少的是：

```text
IDENTITY JUDGMENT
```

也就是：

> **我們知道 S₀ 變成了 S₁，但目前還沒有正式規則判定 S₁ 是 S₀ 的 successor，還是新的 structure。**

---

# 8｜本 MEMO 只留下三個工作問題

## Q1｜Identity Invariants

哪些結構特徵若仍保存，可以支持：

```text
S₁ = SUCCESSOR(S₀)
```

目前只保留候選，不正式定義：

```yaml
IDENTITY_INVARIANT_CANDIDATES:
  - core_problem
  - indispensable_premises
  - central_relation_structure
  - causal_direction
  - responsibility_position
  - scope / comparison_basis
  - closure_target
```

這不是正式 schema。

尤其不能使用：

```text
文字相似度高
→ 同一 successor
```

或：

```text
名字還叫 A
→ 仍然是 A
```

---

## Q2｜Successor / New Identity Boundary

必須回答：

```text
REVISION
!=
NEW IDENTITY
```

但邊界在哪裡？

候選情況包括：

```text
縮小適用範圍
→ 可能仍是 successor

增加限定條件
→ 可能仍是 successor

吸收有效反例後修正
→ 可能仍是 successor

改變核心問題
→ 可能不是 successor

替換不可缺少前提
→ 可能形成新 identity

因果方向翻轉
→ 高度可能形成新 identity

責任主體改變
→ 必須重新審查 identity

比較基底整體重構
→ 可能形成 NEW STRUCTURE
```

目前全部保持：

```text
CANDIDATE
```

不得先封成正式判準。

---

## Q3｜Lineage Record

即使 identity 判斷尚未完成，也必須保存：

```text
S₀
↓
Δ₁
↓
S₁
↓
Δ₂
↓
S₂
```

並能區分：

```text
RETAINED
REVISED
REMOVED
INTRODUCED
ABSORBED
DISQUALIFIED
RESIDUALIZED
```

最低原則：

> **新版可以修正舊版。**

但：

> **新版不能回頭冒充舊版本來就是新版。**

因此未來若建立 lineage，其功能應是：

```text
TRACE IDENTITY CHANGE
```

不是：

```text
RETROACTIVELY REWRITE PREDECESSOR
```

---

# 9｜Structural Phase Transition 的暫時法位

Part 2 曾提出：

> 當 Claim Family 的核心 identity invariants 不再保存時，發生的可能不是普通 revision，而是 structural phase transition。

這個語言目前仍有價值。

但本 MEMO 降級為：

```yaml
STRUCTURAL_PHASE_TRANSITION:
  status: "EXPLANATORY CANDIDATE"
  runtime_object: false
  formal_rule: false
  use:
    - "描述結構身份不再保存時的候選轉換"
```

即：

```text
IDENTITY PRESERVED
→ SUCCESSOR

IDENTITY NOT PRESERVED
→ POSSIBLE NEW STRUCTURE
```

是否需要正式叫：

```text
STRUCTURAL PHASE TRANSITION
```

留待 identity 判準成立後再決定。

不先命名答案。

---

# 10｜R-CCC 本身不需要因此立即升版

本 MEMO 不主張：

```text
R-CCC 必須新增 Claim Family module
R-CCC 必須新增 lineage engine
Main V4.1 有缺陷
Main 必須立刻 V4.2 / V4.3
```

目前更準確的是：

> **Main V4.1 已經可以讓結構被競爭改造，但尚未正式定義「改造後的結構身份連續性」。**

這是一個：

```text
OPEN SEMANTIC / STATE-IDENTITY PROBLEM
```

不是：

```text
CURRENT RUNTIME FAILURE
```

除非未來實跑證明：

> 缺乏 successor identity 會造成實際治理錯誤，

否則不因理論上存在此問題就立即修改 Runtime。

---

# 11｜本次正式清場結果

```yaml
RCCC_OLD_MEMO_REVIEW_2026_09_22:

  retired_active_memos:
    - "MEMO_R-CCC_競爭者版本演化假說_V0.1_WORKING_2026-09-13"
    - "MEMO_R-CCC_競爭者版本演化假說_Part2_量子態本體對接_V0.1_WORKING_2026-09-13"

  archive_status:
    provenance_preserved: true
    historical_reasoning_preserved: true
    active_working_authority: false

  absorbed_by_main_v4_1:
    - "winner-centric competition rejection"
    - "mandatory R2 full recompetition"
    - "incumbent revision"
    - "coalition / coexistence / reframing outcomes"
    - "residue survival"
    - "residue lifecycle"
    - "event-driven R3+"
    - "competition termination"
    - "unresolved / incomparable legal outcomes"

  no_longer_presumed_required:
    - "CLAIM_FAMILY as a new Runtime object"

  remaining_open_core:
    - "STRUCTURE SUCCESSOR IDENTITY"
    - "IDENTITY INVARIANTS"
    - "SUCCESSOR vs NEW STRUCTURE boundary"
    - "LINEAGE RECORD"

  hold:
    - "formal identity theorem"
    - "runtime schema"
    - "structural phase transition formalization"
    - "Main patch"
```

---

# 12｜目前最短核心句

> **R-CCC 已經知道競爭可以改變結構。**

現在真正不知道的是：

> **一個結構被改變多少之後，還能合法地說它是原結構的下一版？**

所以本 MEMO 的唯一入口是：

```text
CHANGE
!=
IDENTITY LOSS
```

但同時：

```text
NOT EVERY CHANGE
PRESERVES IDENTITY
```

下一步若再碰這條線，不再回頭討論「競爭者會不會演化」。

那已經過了。

直接從：

# **STRUCTURE SUCCESSOR IDENTITY**

開始。

---

## HOLD

> **Identity Invariants 尚未定義。**

> **Successor / New Structure 邊界尚未形式化。**

> **Lineage Record 尚未取得 Runtime schema。**

> **沒有新的實跑失效以前，不因這三個理論缺口自動修改 Main V4.1。**
