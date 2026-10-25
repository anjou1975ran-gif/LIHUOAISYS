# LIHUOOS V1｜L0 — INDEX / SOURCE / VERSION / ROUTING

**版本：** V1.0-L0.1  
**日期：** 2026-10-25  
**狀態：** FORMAL V1 INDEX / SOURCE ROUTING / VERSION CONTROL  
**層級：** LIHUOOS / L0  
**法位鎖：** NON_THEORY / NON_RUNTIME / NON_NORMATIVE / NON_QUALIFICATION_AUTHORITY / NON_EXECUTION_AUTHORITY  
**Formal V1 Root：** LIHUOOS_V1.0_FORMAL_SYSTEM_BASELINE_20261025.md

---

# L0.0｜L0 是什麼

L0 只回答：

> **現在這套 LIHUOOS V1 由哪些文件構成、哪一份是 current source、問題應該往哪裡找、文件彼此是什麼關係。**

```text
L0
=
INDEX
+
SOURCE
+
VERSION
+
DOCUMENT RELATION
+
ROUTING
```

L0 不回答理論、資格、執行或顯影本身。

```text
INDEX
!=
OWNER
```

---

# L0.1｜LIHUOOS V1 正式總架構

```text
L0｜INDEX / SOURCE / VERSION / ROUTING
哪份文件、哪個版本、哪個問題往哪裡找

L1｜STRUCTURAL PHILOSOPHY
什麼結構有資格成立

L2｜SAC
結構如何變得可觀察、可描述、可形式化

L3｜LIHUO THEORY FAMILY
問題如何分化成不同理論

L4｜GENERATIVE DYNAMICS
生成如何動

L5｜OBSERVATION & AUDIT
我們憑什麼說看見／知道

L6｜INTERVENTION
誰能在何時對何物做有限改變

L7｜MANIFESTATION
什麼內容能以什麼方式進入 recipient 世界

L8｜LIHUO OPERATING CYCLE
把一次理火完整跑完，並在最後對帳

L9｜DAIL CALLABLE CAPABILITY REPOSITORY
需要能力時，提供可尋址、可替換、可調用的工具與模組
```

最短讀法：

```text
L0–L7
=
UNDERSTANDING / THEORY /
QUALIFICATION / GOVERNANCE BASIS

L8
=
OPERATE ONE LIHUO CYCLE
+
ACCOUNT FOR WHAT HAPPENED

L9
=
PROVIDE CALLABLE CAPABILITIES
```

注意：

```text
LAYER ORDER
!=
FIXED RUNTIME PIPELINE
```

---

# L0.2｜Main 的位置

Main 不新增為另一層。

```text
MAIN
=
COMPUTE ENGINE
USED BY L8 OPERATING CYCLE
```

所以：

```text
L8
=
OPERATING CYCLE

MAIN
=
COMPUTE

L9
=
CAPABILITY REPOSITORY
```

不得混型。

---

# L0.3｜Formal V1 Current Source Snapshot

```yaml
LIHUOOS_V1_FORMAL_SOURCE_SNAPSHOT:

  L0:
    file: "L0_INDEX_SOURCE_VERSION.md"
    standing: "FORMAL_INDEX"

  L1:
    file: "L1 第五版本.md"
    blob_sha: "79778cbfc770cf97923802aafc0367fa86d603c4"
    standing: "STRUCTURALLY_PASS"

  L2:
    file: "L2 第五版本.md"
    blob_sha: "4081cd55aa12de6391ca20fe8f00c8c9fca0e00f"
    standing: "STRUCTURALLY_PASS"

  L3:
    file: "L3 第二版本.md"
    blob_sha: "fac489076cb6b37776ffdcb6de11f36b1644d142"
    standing: "STRUCTURALLY_PASS"

  L4:
    file: "L4 第二版本.md"
    blob_sha: "5d7ad061cda5ac549adf611ab1cb2b8003bbe936"
    standing: "PASS"

  L5:
    file: "L5 第二版本.md"
    blob_sha: "84c3cb9f978932d99a1c9e9dbae7c9ee9fcd1274"
    standing: "PASS"

  L6:
    file: "L6 第二版本.md"
    blob_sha: "f028e4c35a047e8fe6851c616ba3251a8a740418"
    standing: "PASS"

  L7:
    file: "L7 第二版本.md"
    blob_sha: "a25fc8da5efcb267d6f0aec4e626748cf097e1d8"
    standing: "PASS"

  L8:
    file: "L8_LIHUO_OPERATING_CYCLE_V0.3_WORKING_20261025.md"
    blob_sha: "ebddf0c4ee0fdbfa358786070b5d61e396a58640"
    internal_version: "V0.3.1-WORKING"
    standing: "FORMAL_V1_OPERATIVE_BASELINE"

  L9:
    file: "L9_DAIL_CALLABLE_CAPABILITY_REPOSITORY_V0.1_WORKING_20261025.md"
    blob_sha: "4e5336b0e499e11de1a71e1e07e6c33440f5b024"
    internal_version: "V0.1.1-WORKING"
    standing: "FORMAL_V1_CAPABILITY_BASELINE"
```

L8 / L9 原始檔名保留歷史版本名稱；Formal V1 以 exact blob 固定其 operative source。

---

# L0.4｜Formal V1 Integration Rule

```text
LAYER BASELINE FILE
=
AUTHORITATIVE SOURCE FOR THAT LAYER

FORMAL SYSTEM BASELINE
=
CURRENT SYSTEM MAP

FORMAL FULL BODY
=
SOURCE-PRESERVING PACKAGE

INTEGRATION MANIFEST
=
EXACT SNAPSHOT RECORD
```

以及：

```text
INTEGRATION
=
PACKAGING
+
NAVIGATION
+
BASELINE PROJECTION

NOT
NEW THEORY OWNER
```

---

# L0.5｜L8 的正式定位

L8 只有一個核心工作：

> **完整跑一趟理火；需要回報時完整回報；最後列出該收到但沒收到的 receipt / return。**

```text
L8
DOES NOT INVENT LIHUO

L8
RUNS LIHUO
```

它不建立新 evidence system、新 event ontology、新 cross-layer court。

---

# L0.6｜L9 的正式定位

L9 只做：

```text
REGISTER
DISCOVER
BIND
CALL
```

它把可獨立叫用的功能能力從舊式 monolithic control plane 拆出來，以 DAIL 定義並綁到 implementation。

```text
L9
CAN PROVIDE HANDS

L9
CANNOT BECOME
THE BRAIN OR THE JUDGE
```

---

# L0.7｜Routing

```text
STRUCTURE / ELIGIBILITY
→ L1

STRUCTURAL OBSERVATION / SAC
→ L2

THEORY DIFFERENTIATION
→ L3

GENERATIVE DYNAMICS
→ L4

EVIDENCE / OBSERVATION / AUDIT
→ L5

ACTION / AUTHORIZATION / INTERVENTION
→ L6

MANIFESTATION / RELEASE SEMANTICS
→ L7

RUN ONE COMPLETE LIHUO CYCLE /
REENTRY / FINAL ACCOUNTING
→ L8

TOOLS / MODULES / PROVIDERS /
RETRIEVAL / EXECUTION CAPABILITIES
→ L9
```

---

# L0.8｜Owner Separation

```text
STRUCTURE
!=
OBSERVATION
!=
THEORY
!=
DYNAMICS
!=
EPISTEMIC STANDING
!=
ACTION STANDING
!=
MANIFESTATION STANDING
!=
OPERATING CYCLE
!=
CAPABILITY REPOSITORY
```

以及：

```text
MAIN
=
COMPUTE

OWNER
=
OWNS ITS DECISION

TOOL
=
DOES ITS JOB

L8
=
RUNS AND ACCOUNTS FOR THE CYCLE
```

---

# L0.9｜Audit / Engineering References

下列文件保留其研究價值，但不屬每次 L8 cycle 必跑程序：

```text
CROSS_LAYER_EVENT_CONTRACT_REVIEW_V0.1.1_WORKING_20261025.md

EVIDENCE_INSTRUMENTATION_BOUNDARY_REVIEW_V0.1.1_WORKING_20261025.md

OWNER_RETURN_EVIDENTIARY_CONSTITUTIVE_BOUNDARY_REVIEW_V0.1_WORKING_20261025.md
```

法位：

```text
OPTIONAL AUDIT NOTE
/
FAILURE-MODE LIBRARY
/
ENGINEERING TEST MATERIAL
```

可在：

```text
dispute
external execution
high-responsibility claim
provider receipt ambiguity
host evidence ambiguity
real runtime failure
```

時調用。

但：

```text
NOT
MANDATORY COURT
FOR EVERY LIHUO CYCLE
```

---

# L0.10｜Source Priority

V1 理論與 genealogy 來源仍遵守：

```text
1. 理火體系 / 分科原典庫
2. 理火總體系早期大型整合
3. LIHUO-AI-SYS V2.3 理論接線與 SAC 中心架構
4. V3.x / 後續成熟工程版
5. 理火 2.0 / 3.0 / 4.0 後代理論回照
```

原則：

> **回原典找第一次真正看見的問題；後代理論回照，但不倒灌。**

---

# L0.11｜Version / Document Semantics

```text
VERSION LABEL
!=
RUNTIME AUTHORITY

DOCUMENT PASS
!=
HOST ENFORCEMENT

SCHEMA
!=
EXECUTION

FORMAL V1
!=
WHOLE-SYSTEM EMPIRICAL VALIDATION
```

Formal V1 表示：

> **當前 LIHUOOS 的 document-level system baseline 已整合完成。**

不表示 host 已經照文件運行。

---

# L0.12｜正式版後的修版門檻

V1 不再因：

```text
"I CAN IMAGINE AN EDGE CASE"
```

而自動修版。

合理重開入口以真實使用為優先：

```text
ACTUAL CYCLE GETS STUCK

ROLE CANNOT FIND THE NEXT OWNER

REQUIRED STEP IS LOST

REAL TYPE COLLISION OCCURS

TOOL CANNOT BE WIRED

RECEIPT CANNOT BE ACCOUNTED FOR

A LAWFUL RESULT CANNOT PROGRESS
```

另保留：

```text
empirical contradiction
owner contradiction
cross-layer circularity
new irreducible problem domain
source genealogy correction
material historical evidence
```

核心：

```text
RUNTIME FIRST

ENGINEERING FRICTION
ALONE
!=
THEORY FALSIFICATION
```

---

# L0.13｜Overengineering Lock

```text
A CORRECT DISTINCTION
DOES NOT AUTOMATICALLY REQUIRE
A NEW RUNTIME OBJECT
```

以及：

```text
ENGINEERING GUARDRAILS
SHOULD APPEAR
WHERE THE SYSTEM ACTUALLY HITS A WALL

NOT
TURN THE ENTIRE ROAD
INTO GUARDRAILS
```

---

# L0.14｜Formal V1 最短定義

> **L0–L7 給理火意義與邊界；L8 把理火跑完並對帳；L9 在需要手的時候提供可調用能力。**

```text
L0–L7
UNDERSTAND / QUALIFY / GOVERN

L8
OPERATE

L9
PROVIDE CAPABILITY
```

L0 只負責指出這些東西在哪裡。

