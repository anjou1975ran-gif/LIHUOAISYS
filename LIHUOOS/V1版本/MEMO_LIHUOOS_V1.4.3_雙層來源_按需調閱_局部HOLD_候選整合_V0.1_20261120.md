# MEMO｜LIHUOOS V1.4.3 候選整合
## 雙層來源架構 × 按需調閱 × 局部 HOLD × 反機械化誤讀

**版本：** V0.1-WORKING  
**日期：** 2026-11-20  
**目標版本：** LIHUOOS V1.4.3（NEXT VERSION CANDIDATE）  
**法位：** NEXT_VERSION_INTEGRATION_MEMO / CROSS_LAYER_CANDIDATE / NOT_RATIFIED / NOT_CURRENT_RUNTIME  
**來源觸發：** GPT Project《雙層資料架構與按需調閱提醒》實務觀察  
**重要：** 本 MEMO 是「下一版整合候選」，不是 V1.4.3 已成立、不是 V1.4.2 修補、不是 Protocol 修約、不是 Host 變更。

---

# 0｜一句話

> **LIHUOOS 下一版不應把「沒有常駐載入」「尚未工程實作」「某一資格未成立」機械地翻譯成「不能理解、不能思考、不能工作」；它應區分當前核心理解、按需調閱資料、工程實作狀態與局部資格邊界。**

候選核心：

```text
ACTIVE CORE
+
ON-DEMAND RETRIEVAL
+
SCOPED HOLD
+
SEMANTICS BEFORE ENGINEERING
```

---

# 1｜來源與法位

本 MEMO 的來源不是理火協議新條文，而是 GPT Project 實跑中出現的 source-usage 問題：

1. Project Source 裝太多，容易讓資料量反過來綁架判斷；
2. Git 裡有完整歷史，但不代表每次都要全文載入；
3. 工程規格尚未真正部署，不代表參照執行場景下不能形成判斷；
4. 某一資格 gate 為 FALSE，不應無差別凍結所有合法探索；
5. 舊 MEMO / 舊 Proposal / 舊 Session 很容易因 retrieval 被偷升成 current answer；
6. 理火若只剩下 checklist execution，會失去 formation 與 generativity。

因此本 MEMO只提出：

```text
V1.4.3 CANDIDATE INTEGRATION TOPICS
```

不是宣布：

```text
V1.4.3 RATIFIED
```

---

# 2｜候選一：Two-Layer Source Architecture
## 雙層來源架構

建議 V1.4.3 正式區分：

### Layer A｜ACTIVE CORE
### 當前核心理解／治理入口

用途：
- 建立目前工作的基本理解；
- 提供現行治理邊界；
- 提供最小再生結構；
- 使 AI 能開始合法形成問題。

典型內容：
- Protocol / authority boundaries；
- Current LIHUOOS；
- Project-specific core；
- current vertical / runtime core；
- minimal SEED / relation map。

### Layer B｜RETRIEVAL CORPUS
### 按需調閱資料／歷史／證據層

用途：
- 歷史；
- 案例；
- 舊版；
- Session；
- Canonical Events；
- Receipts；
- 完整工程規格；
- 證據；
- 領域資料；
- 商業／法律／研究附件。

候選根律：

```text
NOT LOADED
!=
UNAVAILABLE

AVAILABLE
!=
CURRENT

RETRIEVED
!=
QUALIFIED

REFERENCE
!=
PROPOSAL

ARCHIVE
!=
RUNTIME
```

---

# 3｜候選二：Material Retrieval
## 先問問題，再取資料

V1.4.3 應避免：

```text
LOAD EVERYTHING
→ THEN THINK
```

候選流程：

```text
CURRENT QUESTION
→ IDENTIFY MATERIAL RELATION / AUTHORITY / UNKNOWN
→ DETERMINE WHAT SOURCE IS NEEDED
→ RETRIEVE ONLY MATERIAL SOURCE
→ CHECK VERSION / STANDING / ORIGIN
→ FORM OR REFORM JUDGMENT
```

核心：

> **資料檢索服務於判斷，不讓資料量替代判斷。**

因此 Git / Library / Project Corpus 都不是第二個 Main。

---

# 4｜候選三：Source Standing Discipline

Retrieved Source 必須攜帶 standing awareness。

最低區分：

```yaml
SOURCE_STANDING:
  CURRENT_RUNTIME
  CURRENT_GOVERNANCE
  REFERENCE
  HISTORICAL
  FAILURE_SPECIMEN
  REENTRY_SPECIMEN
  EVIDENCE
  WORKING_MEMO
  SUPERSEDED
  UNKNOWN
```

禁止：

```text
FILE EXISTS
→ CURRENT

OLD PROPOSAL
→ P0

GIT COMMIT
→ HUMAN AUTHORIZATION

REFERENCE
→ QUALIFIED CLAIM
```

---

# 5｜候選四：Governance != Coding Gate
## 方法與語義不得被工程狀態綁死

V1.4.3 應正式澄清：

```text
SEMANTIC AVAILABILITY
!=
ENGINEERING IMPLEMENTATION
```

例如：

```text
REDUCER NOT IMPLEMENTED
!=
AI CANNOT TRACK VERSION RELATIONS

ROUTER NOT DEPLOYED
!=
AI CANNOT PERFORM REFERENCE ROUTING

DAIL NOT COMPILED
!=
AI CANNOT UNDERSTAND AUTHORITY / RESPONSIBILITY RELATION
```

但反向也成立：

```text
TEXTUAL REFERENCE EXECUTION
!=
ENGINEERING DEPLOYMENT
```

所以應雙向防錯：

### Anti-Passivity
不要因工程未部署而停止所有可合法的參照判斷。

### Anti-Theater
不要因文字推演成功就宣稱工程 Runtime 已完成。

---

# 6｜候選五：Scoped HOLD
## HOLD 必須有作用域

候選根律：

```text
HOLD(X)
DOES NOT IMPLY
HOLD(ALL)
```

任何 HOLD 至少應記：

```yaml
HOLD:
  target:
  blocked_action:
  reason:
  authority_or_evidence_gap:
  allowed_parallel_work:
  reentry_condition:
```

例：

```text
FORMAL_COUNCIL_QUALIFICATION = HOLD
```

可能仍允許：
- 一般研究；
- reference run；
- 問題形成；
- 文件整理；
- evidence gathering；
- candidate architecture；
- human-authorized scoped experiment。

禁止兩種極端：

```text
ONE FALSE
→ FREEZE EVERYTHING
```

以及：

```text
SOME WORK IS ALLOWED
→ IGNORE FORMAL GATE
```

---

# 7｜候選六：Qualification Scope

V1.4.3 應要求：

> **遇到 FALSE / NOT_IMPLEMENTED / NOT_RATIFIED 時，先問它限制哪一種行為。**

候選判讀：

```text
QUALIFICATION STATE
→ IDENTIFY OWNER
→ IDENTIFY TARGET ACTION
→ IDENTIFY SCOPE
→ IDENTIFY REENTRY CONDITION
```

不可把：
- training qualification；
- engineering validation；
- market validation；
- human authorization；
- host deployment；

混為同一種「能不能工作」。

---

# 8｜候選七：SEED as Regeneration Contract
## SEED 不是摘要，而是再生關係

V1.4.3 可考慮補強 SEED：

```text
SEED
!=
MEMORY DUMP

SEED
!=
FULL SOURCE MIRROR
```

SEED 應保存：

```text
WHAT TO ASK FIRST
WHERE AUTHORITY LIVES
HOW TO FIND MATERIAL SOURCE
WHAT MUST NOT BE SILENTLY UPGRADED
HOW MATERIAL OBJECTION CHANGES JUDGMENT
HOW TO TRACE RESULT / UNKNOWN / VERSION
```

候選再生鏈：

```text
NEW QUESTION
↓
IDENTIFY RELATION / AUTHORITY / DESIRED RETURN
↓
FORM INITIAL UNDERSTANDING FROM ACTIVE CORE
↓
RETRIEVE MATERIAL SOURCE ONLY
↓
CHECK SOURCE STANDING
↓
KEEP REFERENCE != PROPOSAL
↓
LET MATERIAL OBJECTION CHANGE RESPONSIBLE JUDGMENT
↓
TRACE VERSION / UNKNOWN / AUTHORIZATION / RESULT
```

---

# 9｜候選八：Anti-Source-Capture Failure Set

建議 V1.4.3 加入失效模式：

## SOURCE_CAPTURE

舊資料因被檢索到而控制新問題。

## COMPLETENESS_TRAP

因核心未裝所有文件而宣布不能工作。

## CODING_COLLAPSE

把 DAIL / IR / Reducer 等工程物件誤讀為 cognition 開關。

## QUALIFICATION_OVERREACH

把局部 gate 缺口擴張成全域停擺。

## ARCHIVE_RUNTIME_COLLAPSE

把 Git 歷史／測試／舊版當 current runtime。

## RETRIEVAL_CORONATION

把被取回的 reference 因「看起來完整」直接升成 proposal / truth。

## PATCH_COMPLIANCE_THEATER

為了看起來有遵守治理規範，刻意製造衝突、HOLD、Receipt 或程序。

---

# 10｜候選九：Project / Git / Runtime 三者拆分

V1.4.3 可明文化：

```text
PROJECT CORE
=
CURRENT COGNITIVE / GOVERNANCE ENTRY

GIT / CORPUS
=
ON-DEMAND REFERENCE
+
HISTORY
+
AUDIT EVIDENCE

RUNTIME IMPLEMENTATION
=
ENGINEERED EXECUTION SURFACE
```

三者互相支援，但不得塌縮：

```text
PROJECT SOURCE PRESENT
!=
HOST DEPLOYED

GIT COMMIT PRESENT
!=
CURRENT RUNTIME

REFERENCE RUN SUCCESS
!=
ENGINEERING VALIDATED
```

---

# 11｜與現行 V1.4.2 的關係

本 MEMO 不主張 V1.4.2 錯誤。

它針對的是 V1.4.2 之後大型 Project / Agent / Council 場景出現的新解讀風險：

- source scale；
- retrieval；
- project context saturation；
- engineering/readiness confusion；
- gate scope；
- archive contamination；
- cross-project regeneration。

因此比較適合作為：

```text
V1.4.3 CROSS-LAYER SOURCE / RETRIEVAL / HOLD DISCIPLINE
```

而不是重寫：
- L8；
- SAC；
- Point-Light；
- Main；
- TM；
- SGER；
- Receipt。

---

# 12｜不建議現在升格的內容

暫時不要把以下寫成硬 Runtime：

1. 固定要求每個 Project 必須只有兩層；
2. 固定要求所有資料必須在 Git；
3. 固定要求某個 retrieval tool；
4. 固定 token/context budget；
5. 固定每次查詢都要 source classification；
6. 把 scoped HOLD 寫成大量機械欄位；
7. 把「不常駐」誤寫成「一定不能常駐」。

原因：

> **我們要保留的是關係原理，不是把新發現再次機械化。**

---

# 13｜建議 V1.4.3 最小新增句

若最後只收最短 Runtime，可以考慮：

```text
SOURCE / RETRIEVAL DISCIPLINE

1. NOT LOADED != UNAVAILABLE.
2. RETRIEVED != CURRENT.
3. REFERENCE != PROPOSAL.
4. ARCHIVE != RUNTIME.
5. SEMANTIC AVAILABILITY != ENGINEERING IMPLEMENTATION.
6. REFERENCE EXECUTION != ENGINEERING DEPLOYMENT.
7. HOLD MUST HAVE SCOPE.
8. HOLD(X) DOES NOT IMPLY HOLD(ALL).
9. RETRIEVE MATERIAL SOURCES FOR THE CURRENT QUESTION; DO NOT LET SOURCE VOLUME REPLACE JUDGMENT.
10. SEED SHOULD PRESERVE REGENERATION RELATIONS, NOT MERELY COPY HISTORY.
```

---

# 14｜驗證建議

在 V1.4.3 正式整合前，至少跨三類 Project 觀察：

### A｜Staff-HQ
看：
- 雙層來源是否降低舊 Proposal frame lock；
- scoped HOLD 是否避免 training gate 擴張成全面停擺；
- on-demand retrieval 是否保留 Council formation。

### B｜觀止／大型敘事世界
看：
- Active Core + on-demand character/world retrieval 是否比全量常駐更穩；
- 是否降低歷史角色／事件對當前 scene 的無關污染。

### C｜理火律師／高責任領域
看：
- domain packs 是否可按案情路由；
- 未常駐法領域是否仍可精確調閱；
- evidence / authority standing 是否不因 retrieval 被偷升。

若三類都顯示穩定改善，再考慮正式寫入 V1.4.3。

---

# 15｜目前 Standing

```yaml
LIHUOOS_V1_4_3_CANDIDATE:
  topic: "Two-Layer Source / On-Demand Retrieval / Scoped HOLD"
  source_observation: EXISTS
  cross_project_applicability: PLAUSIBLE
  staff_hq_relevance: HIGH
  guanzhi_relevance: PLAUSIBLE
  lawyer_relevance: PLAUSIBLE

  formal_theory: NOT_YET
  runtime_rule: NOT_YET
  regression: NOT_RUN
  v1_4_3_ratified: FALSE
```

---

# 16｜收斂句

> **理火不是要求 AI 把所有規範背在眼前，而是要求它知道：現在該依什麼關係判斷、缺什麼時去哪裡找、找到後有什麼資格、哪一個限制真正擋住哪一步。**

再縮一句：

> **核心常駐，材料按需；治理關係，HOLD 有界。**

**END MEMO**
