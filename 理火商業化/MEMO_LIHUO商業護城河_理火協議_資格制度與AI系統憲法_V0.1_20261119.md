# MEMO｜LIHUO 商業護城河：理火協議 V0.1
## 資格制度 × 權責來源 × Runtime 真實性 × AI 系統憲法

**日期：** 2026-11-19  
**文件法位：** COMMERCIAL MOAT WORKING MEMO  
**狀態：** WORKING / NON-NORMATIVE / NOT RATIFIED / NOT INVESTMENT DECK / NOT MARKET CLAIM  
**用途：** 單獨保存「理火協議作為理火最深層商業護城河」的現階段判斷，供後續商業化總報告整合。  

**主要來源：**
- `理火V5系統/V5.1版本/00_LIHUO_PROTOCOL_V5.1.0_FULL_BODY_RATIFIED_20261014.md`
- 理火既有 Main / Lighter / DAIL / Runtime 實跑材料
- 現行商業化 DAIL 護城河 MEMO

---

# 0｜核心判斷

DAIL 是理火的重要技術載體。

但在更高一層：

> **理火協議決定什麼有資格成為 Runtime、誰有權改變什麼、什麼狀態可以成立、什麼輸出有資格被釋出。**

因此目前可將護城河層級暫時理解為：

```text
LIHUO PROTOCOL
= ROOT GOVERNANCE / STANDING / QUALIFICATION LAYER

LIHUO OS
= GOVERNED GENERATIVE SYSTEM

DAIL
= DECLARATIVE RUNTIME SEMANTIC REPRESENTATION

APPLICATIONS
= DOMAIN / MARKET PROOF
```

最短句：

> **DAIL 解決「怎麼寫 AI Runtime」。**

> **理火協議解決「這個 Runtime 憑什麼有資格這樣運作」。**

---

# 1｜理火協議不是 Prompt、Workflow 或答案庫

理火協議處理的不是「下一步該做什麼」而已。

它處理：

- relation；
- authority；
- standing；
- authorization；
- binding；
- execution；
- receipt；
- release；
- provenance；
- responsibility；
- lifecycle；
- reentry；
- failure / HOLD；
- final gate。

V5.1.0 根憲法保留句：

```text
RELATION FIRST.
CONTRACT SECOND.
MODULE THIRD.
CODING AFTERWARD.
```

這代表：

> **先決定關係與法位，再決定模組與程式。**

不是先寫出一個功能，再事後補治理語言。

---

# 2｜最關鍵的資格拆分

V5.1.0 保留：

```text
AUTHORIZATION / BINDING
!=
EXECUTION
!=
RECEIPT
!=
RELEASE.
```

以及：

```text
RECEIPT RECORDS WHAT ACTUALLY HAPPENED.
RECEIPT DOES NOT CREATE EXECUTION.
```

這是理火與一般 Agent / Workflow 系統非常重要的差異之一。

許多 AI 系統容易發生：

```text
USER ASKED
↓
MODEL CLAIMED IT CAN
↓
MODEL SAID IT DID
↓
SYSTEM TREATS IT AS DONE
```

理火協議強制拆開：

```text
REQUEST
!=
AUTHORIZATION

AUTHORIZATION
!=
BINDING

BINDING
!=
EXECUTION

EXECUTION
!=
RECEIPT

RECEIPT
!=
RELEASE
```

也就是：

> **文字宣告本身不能自動創造事實法位。**

---

# 3｜反假 Runtime 是協議級能力

V5.1.0 明確保留：

```text
OWNER-LABELED TEXT
!=
OWNER EXECUTION.

DOCUMENT RATIFIED
!=
HOST DEPLOYED.

VISIBLE GOVERNANCE LANGUAGE
!=
RUNTIME OCCURRENCE.
```

這直接對抗一類 AI 特有失效：

```text
「我已啟動」
「我已執行」
「安全閘門已關閉」
「Main 已跑」
「已完成審計」
```

但沒有：

- 真正 Runtime；
- 可核對執行；
- owner execution；
- receipt；
- host binding；
- provenance。

因此理火協議的一個重要商業價值是：

> **把「模型說發生了」和「系統真的發生了」制度性分離。**

這是高責任 Agent、法律、金融、企業 AI、自治工作流尤其需要的能力。

---

# 4｜Standing 不能由 Payload 自己鑄造

V5.1.0 對 Generation Attempt / Vertical 明確要求：

```text
VERTICAL PAYLOAD
MAY NOT SELF-MINT
GENERATION ATTEMPT STANDING.
```

以及：

```text
PAYLOAD
MAY NOT SELF-DECLARE
ATTEMPT TERMINATION.
```

Vertical Cycle 也不能只因「它存在」就取得 LIHUO governance standing。

正式結構是：

```text
LOCAL / VERTICAL EXISTENCE
!=
LIHUO GOVERNANCE ADMISSION
```

因此：

> **一個模組可以存在，不代表它有治理權。**

> **一個 Agent 可以輸出，不代表它有 Final Release 權。**

> **一個角色可以自稱 owner，不代表 owner execution 已成立。**

這種法位拆分是理火協議的重要累積性資產。

---

# 5｜Single Governing Cycle 與責任唯一性

V5.1.0 對已成立的理火治理生成嘗試要求：

```text
ONE ESTABLISHED LIHUO-GOVERNED GENERATION ATTEMPT.
ONE ACTIVE PRIMARY GOVERNING CYCLE.
```

它避免：

- Native 與 Vertical 同時都自稱 primary；
- 多個 Vertical 同時搶治理權；
- 前一輪未合法結束，下一輪已偷偷開始；
- failed / held / closed 狀態互相混用；
- accountability ledger 被新狀態覆蓋。

商業意義不是「只能有一個 Agent」。

而是：

> **任一具責任後果的生成嘗試，必須能回答目前哪一條治理鏈正在負責。**

這是責任追溯、稽核、企業部署與多 Agent 系統的重要基礎。

---

# 6｜Main / Lighter 的權責分離

理火協議保留：

```text
MAIN SOLVES.
LIGHTER RELEASES.
```

這不是單純模組分工。

它建立：

```text
COMPUTATION
!=
RELEASE AUTHORITY
```

Main 可以計算、重新競爭、回傳。

但 Main 不能因為自己算出結果就自動獲得 Release 權。

Lighter 可以治理 Final Gate。

但 Lighter 不能任意假裝 Main 已完成必要計算。

因此：

> **生成能力與准出權被結構性分離。**

這是理火協議能避免「最會生成答案的模組，同時又自己批准答案」的重要機制。

---

# 7｜HOLD 不是失敗，也不是偷偷終止

V5.1.0 特別修正：

```text
HOLD DECISION
!=
ATTEMPT TERMINATION.
```

HOLD 可以阻止 progression，但不等於：

- 已失敗；
- 已結案；
- 已重新開始；
- 已自動產生 successor。

要真正 terminal / closed，仍需要獨立的 termination standing 與 provenance。

這代表：

> **理火允許「尚不能合法完成」成為正式系統狀態。**

對 AI 而言這很重要。

因為一般生成系統具有強 completion pressure，容易把「不知道／未完成／缺資料」壓成一個看似完整答案。

理火協議把未完成合法化。

---

# 8｜Coverage 不等於「曾經跑過一次」

V5.1.0 將 V5.0 的 Main Transit 升級為 Main Coverage。

合法順序：

```text
MAIN_COVERAGE_PRECONDITIONS_READY
→
FINAL GATE MAY EXECUTE
→
GATE CONSUMES LATEST COVERING MAIN RETURN
→
MAIN_COVERAGE_CLOSED
→
RELEASED MAY BE DECIDED
```

因此：

```text
MAIN OCCURRED ONCE
!=
CURRENT STATE COVERED

GATE EXISTS
!=
COVERAGE CLOSED

COVERAGE CLOSED
!=
AUTOMATIC RELEASE
```

這是一種時間化、版本化的資格制度。

它避免：

> 「以前審過，所以現在也算審過。」

或：

> 「流程有經過 Main，所以所有後續修改都自動合格。」

---

# 9｜協議的護城河不是文件本身

如果理火協議只是 GitHub 上的一份 Markdown：

> **它不是強護城河。**

文字可以 Copy。

真正難以複製的是：

```text
PROTOCOL
+
VERSION HISTORY
+
FAILURE CORPUS
+
DAIL REPRESENTATION
+
OS IMPLEMENTATION
+
CONFORMANCE TESTS
+
RUNTIME RECEIPTS
+
DOMAIN IMPLEMENTATIONS
+
CUSTOMER PROFILES
+
REENTRY / MIGRATION HISTORY
```

也就是：

> **一整套「什麼叫符合協議」的判定能力與實跑歷史。**

別人可以抄：

```text
AUTHORIZATION != EXECUTION
```

但難以只靠複製一句話，就取得：

- 正確的 standing model；
- owner separation；
- lifecycle；
- provenance discipline；
- failure handling；
- reentry rules；
- cross-stack binding；
- release governance；
- 大量失效樣本所累積出的邊界。

---

# 10｜商業位置：協議是 Root Moat

目前商業結構可暫時整理為：

```text
LIHUO PROTOCOL
↓
defines legitimacy / standing / authority / responsibility

LIHUO OS
↓
implements governed generative architecture

DAIL
↓
represents domain / customer runtime structure

APPLICATIONS
↓
prove capability in real domains
```

因此：

> **理火協議不是單一產品。**

它更接近整個理火產品族的：

- constitutional root；
- compatibility root；
- qualification root；
- audit root；
- responsibility root。

這也是為什麼它比單一應用更難被市場價格戰直接商品化。

---

# 11｜可能形成的商業價值層

目前只保存方向，不定價、不正式命名產品。

未來可能形成：

```text
PROTOCOL-COMPATIBLE RUNTIME
PROTOCOL-CONFORMANT DEPLOYMENT
ENTERPRISE VALIDATION
RUNTIME RECEIPT / AUDIT
VERSION / MIGRATION ASSURANCE
DOMAIN IMPLEMENTATION CERTIFICATION
```

其價值不在「賣一份協議」。

而在：

> **客戶能否證明自己的 AI Runtime 真正依照某套資格、責任與准出制度運作。**

若理火成為可辨識的 Runtime 標準，則：

```text
OS
DAIL
SERVER
DOMAIN PACK
CUSTOMER PROFILE
MODEL ADAPTER
```

都可以在同一 Protocol compatibility framework 下形成商業生態。

---

# 12｜與 DAIL 護城河的關係

DAIL 與 Protocol 不應互相取代。

```text
LIHUO PROTOCOL
=
WHAT IS LEGITIMATE

DAIL
=
HOW THE LEGITIMATE STRUCTURE IS DECLARED

LIHUO OS / RUNTIME
=
HOW IT IS GOVERNED / EXECUTED

APPLICATION
=
WHERE IT IS USED
```

因此：

> **Protocol 是根護城河。**

> **DAIL 是核心技術載體。**

> **OS 是治理與生成系統。**

> **Applications 是市場與實證入口。**

---

# 13｜版本法位硬鎖

本 MEMO 使用的來源檔名為：

`00_LIHUO_PROTOCOL_V5.1.0_FULL_BODY_RATIFIED_20261014.md`

但該檔正文自身明示：

```text
artifact_class: FINAL_RATIFICATION_TARGET
standing:
- FINAL_RATIFICATION_TARGET
- NON_CURRENT_UNTIL_EXTERNAL_ATOMIC_RATIFICATION
- NOT_HOST_DEPLOYMENT
- NOT_RUNTIME_RECEIPT
- NOT_PRODUCTION_RELEASE_AUTHORITY
```

並明示：

```text
current_claim_in_bytes: NONE
```

因此本商業 MEMO：

- 可以使用其結構分析理火協議護城河；
- 不把檔名中的 `RATIFIED` 自動解讀成 Current Runtime；
- 不宣稱 V5.1.0 已 Host 部署；
- 不宣稱該文件本身就是 execution receipt。

---

# 14｜停止點

本 MEMO 只保存：

> **理火協議為何可能是理火最深層的商業護城河。**

目前不：

- 定價；
- 建立正式認證品牌；
- 宣稱已成為產業標準；
- 宣稱競爭者無法複製；
- 宣稱 V5.1.0 已 Current / Host deployed；
- 把 Protocol / DAIL / OS 混成同一件事。

後續商業化總報告再與 DAIL、應用、資料、服務與其他護城河一起整合。

---

**END OF MEMO**
