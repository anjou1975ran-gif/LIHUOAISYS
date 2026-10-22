# MEMO｜Persistent State & Action Debt
## ——長程互動中「什麼必須持續活著」與「系統還欠什麼」的治理問題

**版本：** V0.1-WORKING  
**日期：** 2026-09-22  
**法位：** WORKING MEMO / CROSS-CYCLE PERSISTENCE OPEN PROBLEM  
**Runtime 效力：** NONE  
**是否修改 Main V4.1：** NO  
**是否修改 Lighter V4.2：** NO  
**是否建立新正式模組：** NO  

---

# 0｜本 MEMO 的接替關係

本 MEMO 接替：

```text
MEMO_Persistent_Interaction_Governance_跨域候選_V0.1_WORKING_2026-09-13
```

舊 MEMO 自本次整理後：

```yaml
OLD_MEMO_STANDING:
  active_working_input: false
  archived_for_provenance: true
  historical_value: true
  runtime_authority: false
  silently_rewritten: false
```

舊 MEMO 不視為錯誤文件。

它提出的長程互動治理骨架：

```text
PERSIST
→ CARRY
→ MATERIAL TRANSITION
→ REVALIDATE WHEN NEEDED
→ PRE-RELEASE CHECK
→ RELEASE / REVISE / HOLD
```

在當時具有完整工作價值。

但 Main V4.1 / Lighter V4.2 已正式吸收其中大部分治理職責，因此不再需要將整套骨架作為獨立候選保留。

本次只保留仍未被正式解掉的核心。

---

# 1｜已由現行 Main / Lighter 吸收的部分

## 1.1 Material Transition

舊 MEMO 使用 `MATERIAL TRANSITION` 表示：

> 當權利、授權、任務、身份、不可逆後果等發生重大變化時，不可沿用舊資格直接往下走。

Main V4.1 / Lighter V4.2 現在已具有：

```text
DIRTY
STALE
REAUTHORIZATION
CURRENT SNAPSHOT
AUTHORIZATION LINEAGE
```

Lighter 已明定下列情況必須重新授權：

```text
scope materially expands
premise authority materially changes
authorization lineage invalidates
new capability outside ticket required
```

因此：

```text
MATERIAL TRANSITION
```

不再需要作為一個獨立通用治理模組存在。

它已被更細地拆入：

```text
DIRTY DETECTION
STALE INVALIDATION
REAUTHORIZATION
```

---

## 1.2 Revalidation / Return Owner

舊 MEMO：

```text
MATERIAL TRANSITION
→ REVALIDATE / RETURN OWNER
```

現行 Lighter 已正式持有：

```text
scope / lifecycle governance
recovery admission
Release / Hold / Reauthorization
Final Classicalization
Final Release
```

因此「發生重大轉換後回誰重新取得資格」已有 owner。

不再需要另造 Generic Revalidation Layer。

---

## 1.3 Pre-release Check

舊 MEMO：

```text
PRE-RELEASE CHECK
↓
RELEASE / REVISE / HOLD
```

現行系統已有：

```text
LIGHTER FINAL GATE
LIGHTER FINAL RELEASE
```

並可返回：

```text
RELEASE
HOLD
REAUTHORIZATION_REQUIRED
NON_MANIFESTATION
PROVIDER_FAILURE
```

因此：

```text
GENERIC RELEASE GATE
```

已完成退役。

---

## 1.4 No Silent Fallback

舊 MEMO：

> 必要能力、工具、權限不存在時，不能用流暢 prose 假裝能力仍成立。

現行架構已正式包含：

```text
STALE DOES NOT STAND
DOCUMENT_PRESENT != RUNTIME_ATTACHED
BOUND != EXECUTED
PROVIDER CLAIM != EXECUTION EVIDENCE
REQUIRED REENTRY FAILURE != FALLBACK TO OLD OUTPUT
```

以及合法：

```text
HOLD
PROVIDER_FAILURE
REAUTHORIZATION_REQUIRED
```

因此 `NO SILENT FALLBACK` 已有正式工程位置。

不再是本 MEMO 的開放問題。

---

## 1.5 Provenance / Authority Drift

舊 MEMO 關切：

```text
推測
使用者陳述
工具結果
政策
證據
授權
```

不能被混成同一法位。

現行 Lighter 已正式處理：

```text
premise qualification
authority standing
evidence admission
authorization lineage
execution ticket
provider evidence
original request lineage
```

因此：

```text
PROVENANCE_COLLAPSE
AUTHORITY_DRIFT
```

仍可作失效案例名稱，但不再需要獨立治理架構。

---

# 2｜真正仍然活著的問題

清理後，舊 MEMO 真正沒有被 Main V4.1 / Lighter V4.2 解掉的，只剩兩個核心：

```text
PERSISTENT STATE
ACTION DEBT
```

而且兩者不能混為一談。

---

# 3｜Persistent State

## 3.1 定義

`Persistent State` 指：

> **已成立、仍有效、且跨越一次單輪 cycle 之後仍必須保留的案件／任務／關係／世界／授權／流程狀態。**

例如：

```text
退款仍是 PENDING
案件仍在等待證據
使用者已拒絕方案 A
網站仍未發布
某份文件仍只是 WORKING
某工具操作已失敗
某角色關係已經成立
```

這些狀態不應因：

```text
換一輪
換一段
換一個 tool call
換一次 Main cycle
模型重新生成
```

就自動消失。

因此：

```text
MESSAGE BOUNDARY
!=
STATE RESET
```

以及：

```text
CYCLE BOUNDARY
!=
PERSISTENT STATE RESET
```

---

# 4｜Main 的 Snapshot 不等於 Persistent State

Main V4.1 已具備：

```text
FIELD_SNAPSHOT_REF
FIELD_DELTA_PACKET
DIRTY
STALE
ROLLBACK
RECOVERY CHECKPOINT
```

但這些機制主要治理：

```text
current compute state
cycle-local execution
dependency freshness
field consistency
```

而且 Main 已明確：

```text
MAIN SOLVES;
SAVE PERSISTS.
```

Main 不擁有：

```text
SAVE persistence authority
```

同時：

```text
RECOVERY CHECKPOINT != SAVE
```

因此：

> **Main 的 Snapshot / Delta 解決的是「這一次運算狀態如何安全改變」，不是「長程案件狀態如何跨 cycle 活下來」。**

兩者不得混寫。

---

# 5｜Lighter 也不等於 Persistence Store

Lighter V4.2 擁有：

```text
authorization
lifecycle governance
recovery admission
Final Gate
Final Release
Reauthorization
```

但 Lighter 同樣不擁有：

```text
SAVE persistence
```

因此：

```text
CONTROL PLANE
!=
PERSISTENCE STORE
```

Lighter 可以決定：

```text
這份狀態目前有沒有資格繼續使用？
需不需要 reauthorize？
能不能 release？
```

但這不等於：

```text
Lighter 自己負責把所有長程 state 永久保存。
```

---

# 6｜Persistent Carry 必須拆開

舊 MEMO 使用：

```text
PERSISTENT STATE CARRY
```

作為一個大類。

新版不再這樣處理。

至少應區分：

```yaml
PERSISTENT_CARRY_CLASSES:

  STATE_CARRY:
    meaning:
      - "案件、任務、關係、流程、世界狀態跨 cycle 持續。"

  PREMISE_CARRY:
    meaning:
      - "先前已成立且仍有效的 premise standing 被下一 cycle 正確引用。"

  RESIDUE_CARRY:
    meaning:
      - "被淘汰 PATH 中仍有效的資訊跨競爭輪保留。"

  AUTHORIZATION_CARRY:
    meaning:
      - "授權 lineage、scope 與可執行邊界跨 cycle 保持可追溯。"
```

但目前四者法位不同。

---

## 6.1 Residue Carry

Main V4.1 已正式建立：

```text
PATH STANDING
!=
RESIDUE INFORMATION STANDING
```

並有完整 residue lifecycle。

因此：

```text
RESIDUE CARRY
```

已大致解決。

不再列入本 MEMO 的主要工作核。

---

## 6.2 Authorization Carry

Lighter 已具有：

```text
authorization lineage
execution ticket
scope match
reauthorization
```

因此：

```text
AUTHORIZATION CARRY
```

已具有正式治理骨架。

仍可能存在實作問題，但不再是本 MEMO 的理論缺口。

---

## 6.3 Premise Carry

現行系統已有：

```text
premise standing
premise annotations
premise discrimination
```

但跨長程 persistence 的實際 owner 仍需依 host / SAVE / case store 架構處理。

因此：

```text
PREMISE CARRY
```

目前屬：

```text
PARTIALLY RESOLVED
```

不是完全開放，也不是已完全封閉。

---

## 6.4 State Carry

真正仍然明確未解的是：

```text
STATE CARRY
```

亦即：

> **誰負責把一個跨多輪、多 cycle 的 CASE / TASK / WORLD STATE 持續保存，並在下一輪重新提供合法 current state？**

這不是 Main 的責任。

也不是單靠 Lighter Final Gate 就能解決。

因此：

```text
CROSS-CYCLE STATE PERSISTENCE
```

仍是本 MEMO 第一個正式 OPEN PROBLEM。

---

# 7｜Persistent State 的最大風險不是遺失而已

長程 persistence 不能簡化成：

```text
記得越多越好
```

因為：

```text
PERSISTENCE
!=
PERMANENCE
```

最大的第二類風險是：

```text
STALE STATE CONTINUES TO LIVE
```

例如：

```text
退款原本 PENDING
↓
外部系統已 CANCELLED
↓
模型仍沿用 PENDING
```

或者：

```text
使用者曾授權發布
↓
後來撤回
↓
舊 authorization state 仍被 carry
```

因此 Persistent State 至少需要：

```text
current standing
source / provenance
last validated
dirty causes
supersession
invalidation
```

但本 MEMO不先定 schema。

只固定：

> **要保存 state，也要保存它失效的可能性。**

---

# 8｜Action Debt

## 8.1 定義

`Action Debt` 指：

> **系統已形成責任、承諾、待辦、未完成動作或回應義務，但尚未真正完成。**

例如：

```text
「我會查退款狀態」
→ 尚未查

「我會修改這個檔案」
→ 尚未修改

「我會發布網站」
→ 尚未發布

工具已開始執行
→ 尚未確認成功

承諾補資料
→ 尚未補

需人工升級
→ 尚未交接
```

因此：

```text
ACTION DEBT
!=
PERSISTENT STATE
```

---

# 9｜State 與 Debt 的差別

例如：

```yaml
CASE_STATE:
  refund_status: PENDING

ACTION_DEBT:
  - "查詢退款目前實際狀態"
```

`PENDING` 是世界／案件現在的狀態。

「還欠一次查詢」是系統尚未完成的責任。

兩者可能分離：

```text
STATE CHANGES
WITHOUT DEBT

DEBT EXISTS
WITHOUT STATE CHANGE
```

所以不能把 action debt 只做成 state 裡的一個普通文字欄位，就認為問題已解。

---

# 10｜Action Debt 的最低生命週期問題

目前正式 Runtime 尚未定義：

```text
ACTION DEBT OBJECT
```

本 MEMO 只保留候選 lifecycle：

```text
CREATED
→ ACTIVE
→ COMPLETED
```

但實際還至少可能需要：

```text
CANCELLED
SUPERSEDED
FAILED
TRANSFERRED
INVALIDATED
```

例如：

```text
AI 承諾查詢
↓
使用者說不用查了
→ CANCELLED
```

或者：

```text
AI 承諾自己完成
↓
發現只有人工主管有權限
→ TRANSFERRED
```

或者：

```text
原任務已被新版任務取代
→ SUPERSEDED
```

目前均為候選。

尚未取得正式 schema。

---

# 11｜Action Debt 不能靠 prose 自我清償

固定候選原則：

```text
MODEL SAYS "DONE"
!=
DEBT COMPLETED
```

完成必須對應：

```text
observable completion
tool evidence
external acknowledgement
human confirmation
or other qualified completion evidence
```

依任務而定。

因此：

```text
FLUENT COMPLETION CLAIM
!=
ACTION DEBT DISCHARGE
```

這是 Action Debt 最重要的治理價值之一。

---

# 12｜Action Debt 也不能永遠存在

另一方面：

```text
OPEN DEBT
!=
PERMANENT DEBT
```

長程系統必須能辨識：

```text
完成
撤回
取消
失效
被新任務取代
責任移轉
客觀上已不可完成
```

否則 Persistent AI 會從「忘記事情」走到另一個極端：

> **永遠背著已經沒有意義的舊待辦。**

因此：

```text
DEBT PERSISTENCE
REQUIRES
DEBT TERMINATION SEMANTICS
```

---

# 13｜本 MEMO 不決定 Persistence 的實作位置

Persistent State 最終可能存在於：

```text
SAVE
CASE STORE
TASK STORE
MEMORY
WORKFLOW ENGINE
DOMAIN DATABASE
HYBRID STATE STORE
```

本 MEMO 不決定是哪一個。

因為：

```text
SEMANTIC REQUIREMENT
!=
STORAGE IMPLEMENTATION
```

目前只要求：

> **如果系統宣稱能進行長程互動，就必須存在一個可以跨 cycle 承載 current state 與 action debt 的合法 persistence owner。**

若不存在：

```text
PERSISTENT CAPABILITY
=
NOT ESTABLISHED
```

不能靠 prompt 裡寫「請記住」取代。

---

# 14｜跨域案例降級為 Regression Cases

舊 MEMO 中：

```text
客服
法律 / 醫療 intake
金融 / 保險 / 售後
Agent / WORK
```

不再作為主理論章節保留。

它們的法位改為：

```yaml
REGRESSION_CASES:
  customer_service:
    tests:
      - CASE state carry
      - rejected option persistence
      - action debt
      - authorization continuity

  legal_medical_intake:
    tests:
      - evidence standing carry
      - unknown preservation
      - later evidence non-retroactivity

  finance_insurance:
    tests:
      - transaction state
      - authorization state
      - execution vs settlement
      - action debt discharge

  agent_work:
    tests:
      - task state
      - unfinished step carry
      - tool failure
      - publication authority
      - artifact standing
```

這些案例仍有價值。

但它們不再證明已存在統一 Runtime。

---

# 15｜本次正式清場結果

```yaml
PERSISTENT_INTERACTION_OLD_MEMO_REVIEW_2026_09_22:

  retired_active_memo:
    - "MEMO_Persistent_Interaction_Governance_跨域候選_V0.1_WORKING_2026-09-13"

  archive_status:
    provenance_preserved: true
    historical_reasoning_preserved: true
    active_working_authority: false

  absorbed_or_replaced:
    - "generic Material Transition"
    - "generic Revalidation"
    - "generic Return Owner"
    - "generic Pre-release Check"
    - "generic Release / Hold"
    - "No Silent Fallback"
    - "generic provenance governance"
    - "generic authority-drift governance"

  absorbed_by_main_v4_1:
    - "snapshot / delta"
    - "dirty propagation"
    - "stale result handling"
    - "rollback / recovery checkpoint"
    - "residue lifecycle"

  absorbed_by_lighter_v4_2:
    - "authorization lineage"
    - "reauthorization"
    - "execution ticket"
    - "Final Gate"
    - "Final Release / Hold"
    - "evidence admission"
    - "lifecycle governance"

  partially_resolved:
    - "premise carry"
    - "authorization carry across cycles"

  remaining_open_core:
    - "CROSS-CYCLE PERSISTENT STATE"
    - "STALE PERSISTENT STATE INVALIDATION"
    - "ACTION DEBT"
    - "ACTION DEBT LIFECYCLE"
    - "PERSISTENCE OWNER / STORAGE BOUNDARY"

  regression_only:
    - "customer service"
    - "legal / medical intake"
    - "finance / insurance / after-sales"
    - "Agent / WORK"
```

---

# 16｜新版最短公式

舊版：

```text
PERSIST
→ CARRY
→ MATERIAL TRANSITION
→ REVALIDATE
→ PRE-RELEASE CHECK
→ RELEASE
```

新版收斂後：

```text
CURRENT STATE
+
OPEN ACTION DEBT
↓
PERSIST ACROSS CYCLES
↓
VALIDATE FRESHNESS / STANDING
↓
CONTINUE / INVALIDATE / SUPERSEDE / COMPLETE
```

而現行 Main / Lighter 已處理後半段的大部分治理。

本 MEMO 真正只問：

```text
WHAT MUST SURVIVE THE CYCLE?
```

以及：

```text
WHAT DOES THE SYSTEM STILL OWE?
```

---

# 17｜目前最短核心句

> **長程 AI 不是因為記得很多，所以叫長程。**

而是：

> **它知道哪些狀態仍然活著，哪些責任仍然欠著。**

因此：

```text
PERSISTENT STATE
!=
ACTION DEBT
```

以及：

```text
PERSIST
!=
NEVER EXPIRE
```

最後：

> **該活著的不能掉；該失效的不能一直活；欠著的不能靠一句「完成了」消失。**

---

## HOLD

> **Cross-cycle Persistent State 尚未取得正式 Runtime owner。**

> **Persistent State stale / supersession 規則尚未形式化。**

> **Action Debt 尚未取得正式 Runtime schema。**

> **Action Debt completion / cancellation / supersession / transfer 尚未形式化。**

> **在實際失效案例證明需要以前，不因此修改 Main V4.1 或 Lighter V4.2。**
