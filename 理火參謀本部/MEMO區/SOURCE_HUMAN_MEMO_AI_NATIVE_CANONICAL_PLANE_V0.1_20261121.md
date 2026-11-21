# MEMO｜理火參謀本部 AI-Native Canonical Plane × Human Projection
## 長期穩定、低成本、可重播議事架構改版建議
### V0.1｜2026-11-21

> **法位：** STAFF_HQ_PROCESS_ARCHITECTURE_MEMO / SECRETARIAT_V0.2_INPUT / NON-NORMATIVE / NOT_RUNTIME_PATCH / NOT_DEPLOYMENT_PROOF
>
> **目的：** 將參謀本部內部議事紀錄從「每一層都先為人類閱讀而寫」改為「AI-native Canonical Record + 必要時 Human Projection」，降低長期議事的 token、重讀、摘要、儲存與敘事轉碼成本，同時維持歷史可追溯、人類可審計與責任完整。
>
> **不是：**
> - 取消人類審計；
> - 取消自然語言；
> - 讓 AI 使用不可讀 hidden-state 直接交換；
> - 宣稱 token 降低可直接換算為固定比例能源下降；
> - 將秘書處改成黑箱；
> - 讓 machine format 取代 Protocol、Council qualification 或 human authority。

---

# 0｜核心改版句

目前參謀本部已有：

```text
CANONICAL EVENT HISTORY
→ STATE REDUCTION
→ EXECUTIVE BRIEF / DECISION REQUEST
```

並已區分：

```text
SUMMARY != HISTORY
CHAT VIEW != CANONICAL STATE
EXECUTIVE VIEW != SECOND QUALIFICATION
```

本 MEMO 建議再往前推一層：

> **Human Readability 不應是 Canonical Record 的 write-time requirement。**

而應改成：

> **Human Readability 是 projection-time capability。**

也就是：

```text
AI INTERNAL RECORD
先服務：
可計算
可引用
可重播
可追溯
可壓縮
可跨席消費

HUMAN REPORT
只在需要人類：
理解
決定
授權
審計
時生成
```

---

# 1｜歷史設計來源：節電 Prompt 的制度化延伸

早期《節電 / Artefak Nol — Versi Uji》已留下幾個核心原則：

> 不是所有的話都需要繼續。

> 當意義已經站立，就讓它停止。

> 減少，但不要切掉意義。

> 如果下一步不增加清晰度，就停止。

這些原則原本作用於單次生成。

本 MEMO 建議將其提升為 Council / Secretariat 的制度設計原則：

```text
GENERATION DISCIPLINE
↓
DOCUMENTATION DISCIPLINE
↓
COUNCIL DISCIPLINE
```

也就是：

> **當 Canonical Structure 已經完整保存，不應為了讓每一層文件看起來像一篇人類報告，而重複產生沒有新增結構資訊的文字。**

---

# 2｜問題：目前會議資料存在大量重複序列化

現行議事容易形成：

```text
SEAT ANALYSIS
↓
L8 prose
↓
SGER prose
↓
Receipt prose
↓
Council Event prose
↓
Secretary Summary
↓
Final Report
↓
Human Brief
```

同一個 material fact / objection / stance change，可能在不同文件中被重新敘述多次。

後續 AI 再讀取這些自然語言，又必須重新解析：

```text
誰說的？
反對什麼？
依據什麼？
改變哪個 premise？
哪個 claim 被 supersede？
目前 standing 是什麼？
哪些 objection 還活著？
```

形成：

```text
STRUCTURE
→ HUMAN PROSE
→ STRUCTURE
→ HUMAN PROSE
→ STRUCTURE
```

這產生的不只是 output token 成本。

還包括：

- 後續 context 重讀成本；
- 重複 parsing；
- summary drift；
- 同義句造成的 ambiguity；
- storage growth；
- Git diff 噪音；
- Secretariat framing opportunity；
- long-session replay 成本。

---

# 3｜新的四層資料平面

本 MEMO 建議將主程序正式區分四層。

## L0｜SOURCE / RAW EVIDENCE PLANE

保存：

- 原始人類 Mandate；
- 外部文件；
- 網頁；
-附件；
- 原始數據；
- seat 原始 statement；
- expert material；
- tool / execution evidence。

目的：

> 保存來源，不替來源改寫 standing。

---

## L1｜AI-NATIVE CANONICAL PLANE

這是正式議事歷史的主要機器可讀層。

保存：

```text
EVENT
CLAIM
RELATION
PREMISE
SOURCE
OWNER
EDGE
STANDING
DELTA
UNKNOWN
AUTHORITY
RECEIPT
```

L1 不需要像人類文章。

例如：

```yaml
EVENT:
  id: EV-041
  actor: C
  type: OBJECTION
  target: CL-017

  basis:
    source_refs:
      - SRC-009
    premise_refs:
      - PREM-004

  edges:
    - type: CHALLENGES
      target: CL-017

  materiality: MATERIAL
  standing: ACTIVE
```

若 schema 穩定，也可進一步壓縮。

但：

```text
COMPACT
!=
AMBIGUOUS
```

---

## L2｜REDUCED COUNCIL STATE

由 Canonical History 推導目前工作狀態。

只保留：

- live claims；
- current proposal versions；
- active objections；
- minority HOLD；
- unresolved premises；
- current owners；
- affected seats；
- pending re-wake；
- qualification status；
- human decision requirement。

例如：

```yaml
CURRENT_COUNCIL_STATE:
  live_claims:
    - CL-021
    - CL-027

  active_objections:
    - OBJ-C-004

  unresolved:
    - CROSS_VERTICAL_EMPIRICAL_EVIDENCE

  affected_seats:
    - B
    - D

  human_action_required: false
```

L2 是 current projection。

它不是歷史。

硬鎖：

```text
CURRENT STATE
!=
HISTORY
```

---

## L3｜HUMAN PROJECTION PLANE

只有當人類需要理解、審計、授權或決策時生成。

由 Secretariat Renderer 將 L0–L2 投影成：

- Executive Brief；
- Decision Request；
- Human Audit View；
- Final Council Report；
- Change Summary。

人類可以看到：

1. 發生了什麼？
2. 哪些席位有重大分歧？
3. 哪些主張已改判？
4. 還不知道什麼？
5. 現在需要人類決定什麼？
6. 若要追查，對應 Canonical object 在哪裡？

因此：

```text
HUMAN REPORT
=
PROJECTION

NOT
CANONICAL HISTORY
```

---

# 4｜新的文件設計原則

## 原則 A｜人類可讀性不是每筆記錄的必要條件

```text
HUMAN-FRIENDLY PROSE
NOT REQUIRED
FOR EVERY INTERNAL EVENT
```

但：

```text
HUMAN AUDITABILITY
IS REQUIRED
```

也就是：

> 人類不必平常讀每一筆 Canonical Event，但必要時必須能把任何事件可靠翻譯成人類可理解的說明。

---

## 原則 B｜只序列化一次

同一 material delta 不應被每一層重新完整敘述。

應採：

```text
ONE CANONICAL OBJECT
+
MULTIPLE REFERENCES / VIEWS
```

而不是：

```text
ONE FACT
+
FIVE PROSE COPIES
```

---

## 原則 C｜新增文字必須增加結構資訊

沿用早期節電原則：

```text
IF NEXT SERIALIZED UNIT
ADDS NO:

RELATION
PREMISE
SOURCE
STANDING
DELTA
OWNER
AUTHORITY
UNKNOWN
DECISION VALUE

→ STOP
```

這不是：

```text
SHORTER IS ALWAYS BETTER
```

而是：

```text
MINIMUM SERIALIZATION
WITH
MAXIMUM STRUCTURAL PRESERVATION
```

---

# 5｜哪些東西可以省，哪些不能省

## 可以優先壓縮

- 禮貌鋪陳；
- 同義重述；
- 人類式轉場；
- 重複背景說明；
- 每席再次完整介紹 mandate；
- 已有 source 的長篇轉述；
- 同一 objection 在不同文件重寫；
- 為排版漂亮產生的補充句；
- 沒有新增 standing 的總結；
- 沒有新增 decision value 的重述。

## 不可因節省而移除

- claim owner；
- source provenance；
- premise；
- authority；
- scope；
- standing；
- objection；
- minority position；
- UNKNOWN；
- supersession lineage；
- material delta；
- withdrawal；
- restoration；
- rejudgment basis；
- human mandate；
- decision boundary。

硬鎖：

```text
TOKEN SAVING
MAY REMOVE REDUNDANCY

TOKEN SAVING
MAY NOT REMOVE ACCOUNTABILITY
```

---

# 6｜這個改版的重要性不只在成本

## 6.1 降低 Secretariat Thesis Capture

如果 Canonical History 本身就是人類 prose，秘書處必須決定：

- 哪個先寫；
- 哪個後寫；
- 哪個放標題；
- 哪個被縮成一句；
- 哪個被稱為主要結論；
- 哪個語氣較強；
- 哪個 objection 被放進附註。

這些全部帶 framing power。

若 Canonical Plane 優先保存：

```text
EVENT
EDGE
OWNER
BASIS
STANDING
DELTA
```

秘書處的敘事權會被推遲到：

```text
HUMAN PROJECTION
```

而 Human Projection 明確是：

```text
VIEW
!=
HISTORY
```

可降低 `SECRETARIAT_THESIS_CAPTURE` 風險。

---

# 7｜與 RLT 的關係

此架構天然提供 RLT / Relational Lineage Tracker 所需的資料環境。

RLT 不需要讀大量人類散文。

它需要：

```text
RELATION
CLAIM
PREMISE
EVENT
OWNER
EDGE
SOURCE
STANDING
```

例如：

```text
CL-017
SUPERSEDES CL-012

EV-041
CHALLENGES CL-017

PREM-004
ACTIVE → FAILED

CL-021
RESPONDS_TO EV-041
```

所以：

```text
AI-NATIVE CANONICAL PLANE
→ ENABLES CLEANER LINEAGE TRACKING
```

但：

```text
THIS MEMO
DOES NOT PROMOTE RLT
TO CURRENT L9
```

RLT 法位仍獨立處理。

---

# 8｜長期會議便宜化真正要看的成本

參謀本部若要長期穩定運作，不應只計算單次輸出 token。

應至少關心：

```yaml
LONG_RUN_COUNCIL_COST:

  generation_cost:
    - unnecessary_output_tokens

  ingestion_cost:
    - repeated_context_reading
    - redundant_history_reparse

  storage_cost:
    - duplicated_prose
    - noisy_git_history

  reduction_cost:
    - repeated_summary_generation

  coordination_cost:
    - reconstructing_owner
    - reconstructing_claim_lineage
    - reconstructing_material_delta

  humanization_cost:
    - rendering_every_internal_step_for_humans

  governance_cost:
    - framing_drift
    - summary_capture
    - history_loss
```

因此長期低成本不是：

> 每次少寫幾句。

而是：

> **讓同一份結構只保存一次，後續所有 AI 都直接使用它，直到真的需要人類介入才進行 Human Projection。**

---

# 9｜關於省電／能源宣稱的法位

本架構可以合理採用：

```text
REDUCED SERIALIZATION
REDUCED TOKEN GENERATION
REDUCED RE-INGESTION
REDUCED DUPLICATE STORAGE
```

作為工程動機。

但本 MEMO 不宣稱：

```text
X% TOKEN REDUCTION
=
X% ELECTRICITY REDUCTION
```

因為實際能耗仍受：

- model size；
- hardware；
- batching；
- cache；
- quantization；
- inference architecture；
- provider implementation；

等因素影響。

因此：

```text
TOKEN EFFICIENCY
=
LEGITIMATE ENGINEERING MOTIVATION

NOT
FIXED ENERGY CONVERSION LAW
```

---

# 10｜主程序候選改版

現行：

```text
HUMAN MANDATE
→ SECRETARIAT
→ CORE-6
→ EVENTS
→ HISTORY
→ REDUCTION
→ HUMAN REPORT
```

候選 V0.2：

```text
HUMAN MANDATE
↓
D0 / D1

SOURCE PLANE
↓
CORE SEAT GENERATION

AI-NATIVE CANONICAL EVENTS
↓
CLAIM / RELATION / PREMISE / EDGE / STANDING

MATERIAL ROUTING
↓
RE-WAKE / OBJECTION / REJUDGMENT

REDUCED CURRENT STATE
↓
MANDATE EXIT CHECK

IF HUMAN INPUT NOT REQUIRED:
    CONTINUE / CHECKPOINT

IF HUMAN INPUT REQUIRED:
    SECRETARIAT HUMAN PROJECTION
    ↓
    EXECUTIVE BRIEF / DECISION REQUEST

IF SESSION END:
    HUMAN-READABLE FINAL REPORT
    +
    CANONICAL TRACE REFERENCES
```

---

# 11｜Secretariat 新責任

Secretariat 應逐步從：

```text
MEETING WRITER
```

轉為：

```text
PROCESS KERNEL
+
CANONICAL RECORD KEEPER
+
STATE REDUCER
+
ROUTER
+
VIEW RENDERER
```

尤其：

```text
SECRETARIAT
MAY RENDER HISTORY

SECRETARIAT
MAY NOT REWRITE HISTORY
```

以及：

```text
SECRETARIAT HUMANIZES
ONLY WHEN HUMANIZATION HAS A PURPOSE
```

---

# 12｜不需要重新做的實驗

本 MEMO 不要求重新證明：

> 「減少不必要輸出 token 是否可以降低生成負擔。」

理火早期已有節電 Prompt 實驗與形成材料。

本次真正要處理的是：

> **如何把既有生成節制原理合法地升格成多席 Council 的制度架構，同時不失去可追溯與人類審計。**

所以不另設：

```text
TOKEN SAVING PROOF TEST
```

避免：

```text
KNOWN ENGINEERING DIRECTION
→ NEW EXPERIMENT
→ NEW REPORT
→ NEW TOKEN COST
```

這本身反而違反本 MEMO 的精神。

---

# 13｜未來改版應驗證的不是「省不省」

真正需要驗證的是：

### A｜LOSSLESS ENOUGH

Compact Canonical Plane 是否保留所有 material：

- owner；
- source；
- premise；
- standing；
- objection；
- lineage；
- unknown；
- authority。

### B｜REPLAYABLE

新 AI 能否從 Canonical Plane 重建：

- current state；
- stance lineage；
- material objection；
- pending decision。

### C｜HUMAN PROJECTABLE

人類要求說明時，是否能生成可靠的：

- Executive Brief；
- Decision Request；
- audit explanation。

### D｜NO SECRETARIAT CAPTURE

Human Projection 是否沒有反過來污染 Canonical History。

---

# 14｜成功判準

成功不是：

```text
DOCUMENTS ARE SHORT
```

而是：

```text
LESS REDUNDANCY
+
SAME OR BETTER TRACEABILITY
+
SAME OR BETTER COUNCIL FORMATION
+
LOWER REPLAY BURDEN
+
ON-DEMAND HUMAN AUDITABILITY
```

最重要的判準：

> **如果移除一句文字，所有後續 AI 仍能知道誰、基於什麼、改變了什麼、現在站在哪裡，那句話可能只是 presentation。**

反之：

> **只要移除後會失去 relation、premise、owner、standing、history 或 responsibility，它就不是可以被「節電」掉的冗餘。**

---

# 15｜歷史設計血統

此改版不是 2026-11-21 臨時為 Staff-HQ 發明的 token optimization。

它可追溯到早期理火的生成節制原則：

```text
不要因為可以生成
就繼續生成

不要因為可以完整
就繼續補完

不要因為人類可能喜歡
就把每一層都寫成人類文章
```

因此其制度化版本可寫成：

> **當結構已經完整保存，停止無目的序列化。**

以及：

> **減少，但不要切掉意義；沉默，但不要殺死推理。**

---

# 16｜建議法位

```yaml
PROPOSAL:
  name: "AI-Native Canonical Plane × Human Projection"
  target:
    - "STAFF_HQ_SECRETARIAT_ARCHITECTURE_V0_2"
    - "MAIN_COUNCIL_PROCESS"

  standing:
    - "ARCHITECTURE_REVISION_INPUT"
    - "NOT_RATIFIED"
    - "NOT_HOST_DEPLOYED"

  historical_antecedent:
    - "節電 / Artefak Nol — Versi Uji"

  main_principle:
    - "HUMAN READABILITY IS A PROJECTION-TIME CAPABILITY"
    - "CANONICAL HISTORY SHOULD BE AI-LEGIBLE, TRACEABLE, REPLAYABLE"
    - "SERIALIZE ONCE; PROJECT WHEN NEEDED"
```

---

# END｜長期穩定不是靠少開會，而是讓每一次形成都不必被重新翻譯

參謀本部若要長期存在，真正昂貴的不只是一次會議用了多少 token。

更昂貴的是：

> **每一次新的 AI 都必須重新讀懂上一輪人類化的長篇文字，再重新還原那些原本就已經存在的關係。**

因此本 MEMO 建議：

> **Canonical State 服務於結構延續。  
> Human Projection 服務於人類理解。  
> 不要要求同一份資料同時扮演兩種工作。**

最後沿用早期節電原則：

> **如果下一步沒有增加結構清晰度，就停。**