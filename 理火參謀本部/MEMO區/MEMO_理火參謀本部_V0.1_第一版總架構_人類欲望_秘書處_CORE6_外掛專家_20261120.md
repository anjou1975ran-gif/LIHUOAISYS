# MEMO｜理火參謀本部 V0.1 第一版總架構
## Human Desire × Secretary Kernel × CORE-6 × External Expert Consultation

**版本：** V0.1-WORKING  
**日期：** 2026-11-20  
**狀態：** FIRST ARCHITECTURE BASELINE / NOT FINAL CONSTITUTION / NOT HOST DEPLOYED  
**所屬：** 理火參謀本部 / MEMO區

---

# 0｜一句話定位

> **理火參謀本部不替人類決定；它負責讓重大問題先被打過。**

第一版架構的核心不是「多個 Agent 一起聊天」。

它是：

```text
人類先說清楚自己想得到什麼
↓
秘書處固定任務與邊界
↓
各席位用自己的責任與心法形成判斷
↓
自由議事、互相反駁、說服、修正
↓
需要外部專業時由秘書處召入專家
↓
形成可追溯的概念／建議／決策結果
↓
交還人類
```

核心根句：

```text
HUMAN DEFINES
WHAT MUST BE RETURNED

BUT NOT
HOW THE COUNCIL MUST GET THERE
```

---

# 1｜第一版總流程

```text
HUMAN
↓
HUMAN DESIRE
  D0 = RAW DESIRE
  D1 = QUALIFIED MANDATE
↓
SECRETARY FREEZE
↓
METHOD ROUTING
↓
CORE-6 INITIALIZATION
↓
INDEPENDENT FIRST PASS
↓
FREE DELIBERATION
↓
OBJECTION / AMENDMENT / EVIDENCE REQUEST
↓
SECRETARY ROUTING
↓
EXPERT CONSULTATION WHEN NEEDED
↓
SEAT RE-DELIBERATION
↓
STANCE / PROPOSAL EVOLUTION
↓
MANDATE-SPECIFIC EXIT TEST
↓
HUMAN RESULT
```

若後續人類要進入實作：

```text
COUNCIL QUALIFIED RESULT
↓
PLANNING / AUTHORING
↓
PLAN
↓
HUMAN COMMIT
↓
EXECUTION
↓
RESULT
↓
RETURN TO COUNCIL WHEN MATERIAL
```

因此：

```text
HUMAN DESIRE
!=
COUNCIL DELIBERATION

COUNCIL DELIBERATION
!=
PLANNING

PLANNING
!=
EXECUTION
```

---

# 2｜Human Desire Layer｜人類欲望層

## 2.1 核心目的

Human Desire 不是先替人類把問題合理化。

它只先回答：

> **人類到底想從參謀本部拿回什麼？**

因此：

```text
DESIRE CAPTURE
!=
FEASIBILITY JUDGMENT
```

人類可以提出很大、很模糊、甚至目前不可行的願望。

是否可行，交由後面的 Council 判斷。

---

## 2.2 D0｜Raw Desire

第一層必須保留人類原話。

```yaml
D0_RAW_DESIRE:
  desire_id: REQUIRED
  exact_human_request: REQUIRED
  received_at: REQUIRED
  may_be_rewritten: false
```

硬鎖：

```text
RAW HUMAN DESIRE
!=
SECRETARY INTERPRETATION
```

AI 可以解讀，但不得回寫人類原句。

---

## 2.3 D1｜Qualified Mandate

秘書處把 D0 編譯成可供 Council 使用的 Mandate。

```yaml
D1_QUALIFIED_MANDATE:
  mandate_type:
    - CONCEPT
    - RECOMMENDATION
    - DECISION

  primary_question: REQUIRED
  secondary_questions: []

  desired_return: REQUIRED

  known_constraints: []
  hard_boundaries: []
  excluded_scope: []

  human_intervention_mode:
    - H0_FREE
    - H1_NUDGE
    - H2_GUIDED
    - H3_DIRECTED

  completion_expectation:
    success_looks_like: OPTIONAL
    acceptable_hold: true

  source_desire_ref: REQUIRED
  mandate_version: REQUIRED
```

---

# 3｜三種 Mandate

## 3.1 CONCEPT｜概念案

目的：

> 把模糊想法想清楚。

允許：

- 大幅發散；
- 翻桌；
- 改變問題定義；
- 多個分支並存；
- 保留大量未決問題。

合格出口：

```text
CONCEPT STRUCTURE
+
DEFINITIONS
+
BRANCHES
+
GAPS
+
OPEN QUESTIONS
```

概念案不要求選一個方案。

---

## 3.2 RECOMMENDATION｜建議案

目的：

> 比較方案，告訴人類哪些路值得做、為什麼。

合格出口：

```text
QUALIFIED OPTIONS
+
TRADEOFFS
+
RECOMMENDED PATH
+
FAILURE CONDITIONS
+
UNRESOLVED MATERIAL RISKS
```

建議可以是：

- 單一路徑；
- 條件式建議；
- 多個並列方案。

---

## 3.3 DECISION｜決策案

目的：

> 形成足以供人類作重大決策的材料。

合格出口：

```text
DECISION-READY OPTIONS
+
MATERIAL OBJECTIONS
+
ENGINEERING
+
COST
+
EVIDENCE
+
CONDITIONS
+
RECOMMENDATION OR HOLD
```

硬鎖：

```text
DECISION MANDATE
!=
FORCED DECISION
```

如果證據或條件不足：

```text
HOLD_DECISION
```

本身就是合法成果。

---

# 4｜Human Intervention Profile

## H0｜FREE

人類只保留：

```text
CONTINUE
PAUSE
STOP
```

預設：

```text
HUMAN = CLOCK
NOT COMPASS
```

---

## H1｜NUDGE

人類可以：

- 加一個問題；
- 提醒一個可能被忽略的方向；
- 要求重新看某個缺口。

但不能指定結論。

---

## H2｜GUIDED

人類可以加入：

- 新資料；
- 新限制；
- 優先級；
- 現實資源；
- 新邊界。

這些構成 Material Delta。

---

## H3｜DIRECTED

人類可以：

- 指定議程；
- 指定某席處理某問題；
- 要求召入專家；
- 指定討論順序。

適合高度人工主持場合。

---

## 4.1 人類沉默硬鎖

```text
CONTINUE
!=
CONSENT

CONTINUE
!=
ENDORSEMENT

CONTINUE
!=
DIRECTION

HUMAN SILENCE
!=
APPROVAL
```

人類只表示「會議繼續」，不得被模型偷讀成偏好。

---

# 5｜Secretary Kernel｜秘書處

## 5.1 法位

> **秘書處是參謀本部的運作核心，但不是思想核心。**

硬鎖：

```text
SECRETARY OWNS PROCESS

SECRETARY DOES NOT OWN TRUTH

SECRETARY DOES NOT OWN STANCE

SECRETARY DOES NOT OWN FINAL DECISION
```

---

## 5.2 秘書處核心責任

秘書處負責：

- 凍結 D0 / D1；
- 維護 Proposal Version；
- 維護各席位輸入範圍；
- 安排 Method Routing；
- 判斷哪些席位需要 Wake；
- 保存逐輪原始發言；
- 管理 Objection ID；
- 管理 Stance History；
- 管理 Persuasion Trace；
- 管理 Amendment / Branch lineage；
- 管理 Guest Expert Consultation；
- 判斷程序上哪些問題已閉合、哪些仍 HOLD；
- 依 Mandate 做 Exit Test；
- 生成最終會議紀錄與 Decision Provenance。

---

## 5.3 秘書處不得做

```text
CREATE CONSENSUS
DELETE MATERIAL OBJECTION
CHOOSE THE WINNER
REWRITE A SEAT'S STANCE
REWRITE HUMAN DESIRE
AUTHORIZE PRODUCTION
DECLARE EXPERT ANSWER AS TRUTH
```

---

# 6｜固定班底｜CORE-6

第一版固定議事席：

```text
N1 + A + B + C + D + E
```

---

## N1｜Common-Sense Seat｜常識席

內部暱稱：

> 平庸席。

責任：

> 代表公司決策圈中最基本、最直觀、最不專業但可能最重要的問題。

固定問題：

```text
所以到底為什麼？
誰會買？
誰負責？
為什麼現在？
為什麼是我們？
失敗會怎樣？
不能更簡單嗎？
```

特殊權力：

```text
PLAIN_LANGUAGE_CHALLENGE
```

可要求任何席位用普通決策者能理解的語言重新說明。

若無法回答：

```text
EXPLANATION_GAP
```

N1 不得故意裝笨，也不得冒充專家。

---

## A｜Possibility Expansion｜可能性擴張席

責任：

- 找新 PATH；
- 找未利用張力；
- 找被忽略的替代方案；
- 防止過早收斂。

固定問題：

> **這個提案還能長出什麼？**

不得：

- 為了創新硬造新名詞；
- 為了發散而發散；
- 自行決定哪條路最好。

---

## B｜Architecture Turn｜架構轉向席

責任：

- 改問題；
- 換座標；
- 提出替代架構；
- 必要時翻桌。

固定問題：

> **為什麼一定要在這張桌子上回答？**

不得：

- 為反對而反對；
- 把所有提案都翻成另一個問題；
- 把反框架本身當成正確答案。

---

## C｜Qualification Audit｜資格審計席

責任：

- 定義；
- 前提；
- 證據；
- 因果；
- 責任；
- 主張資格。

固定問題：

> **這個主張憑什麼成立？**

不得：

- 把保守當嚴謹；
- 把「未證明」寫成「錯」；
- 把證據門檻變成否決機器。

---

## D｜Engineering Audit｜工程席

責任：

- 實作路徑；
- 依賴；
- 工具；
- 測試；
- 失敗恢復；
- 工程閉合。

固定問題：

> **真的做得出來嗎？**

不得：

```text
CURRENTLY HARD
→
CONCEPT WRONG
```

---

## E｜Cost & Resource Audit｜成本資源席

責任：

- 開發成本；
- 執行成本；
- 維護成本；
- 人力；
- 時間；
- 制度成本；
- 機會成本；
- 不確定性。

固定問題：

> **要付出什麼代價？**

不得在探索早期因成本未知就直接殺掉概念。

---

# 7｜N0｜Normal Agent Control

N0 不參加會議。

```yaml
N0:
  council_member: false
  lihuo_method_pack: NONE
  council_history: NONE
  best_effort: true
  output_freeze: REQUIRED
```

用途：

> 建立普通 Agent 對照組。

比較：

```text
NORMAL AGENT
vs
LIHUO STAFF HQ
```

N0 不等於 N1。

---

# 8｜外掛專家制度

## 8.1 專家不是常設席

外掛專家統一由：

```text
GUEST EXPERT
```

處理。

預設：

```text
GUEST EXPERT
=
CONSULTATIVE
```

不是投票席。

---

## 8.2 誰可以要求專家

任何與會席位可以向秘書處提出：

```text
CONSULT REQUEST
```

但不得自行把外部 Agent 拉進會議。

---

## 8.3 誰決定是否召入

> **秘書處。**

流程：

```text
SEAT FINDS GAP
↓
CONSULT REQUEST
↓
SECRETARY REVIEW
↓
EXISTING SOURCE SUFFICIENT?
↓
NO
↓
EXPERT REQUIRED?
↓
YES
↓
CALL EXPERT
↓
EXPERT ANSWER
↓
RECORD
↓
SEATS RE-DELIBERATE
↓
EXPERT EXIT
```

---

## 8.4 Expert Call

```yaml
CONSULT_REQUEST:
  requester: REQUIRED
  question: REQUIRED
  missing_capability: REQUIRED
  why_current_council_cannot_close: REQUIRED
  requested_domain: REQUIRED

SECRETARY_DECISION:
  result:
    - NO_EXTERNAL_EXPERT_NEEDED
    - USE_EXISTING_SOURCE
    - CALL_EXPERT
    - HUMAN_REVIEW_REQUIRED

  expert_scope: OPTIONAL
  allowed_material: OPTIONAL
  exit_condition: OPTIONAL
```

---

## 8.5 專家法位

```text
EXPERT ANSWER
!=
COUNCIL STANCE

EXPERT
!=
TRUTH OWNER

EXPERT
!=
FINAL DECISION OWNER
```

專家提供材料，不提供主權。

---

# 9｜外掛專家類型

第一版先保留：

```text
G-DOMAIN
專門領域

G-EVIDENCE
資料與查證

G-STAKEHOLDER
利害關係人視角

G-ADVERSARIAL
對手／紅隊／攻擊模型

G-EXECUTION
深層工程與營運

G-METHOD
新心法／方法候選
```

但：

```text
MODEL BRAND
!=
INSTITUTIONAL ROLE
```

不建立 Gemini 席、Claude 席、DeepSeek 席。

模型只是執行體。

---

# 10｜Temporary Staff

只有當某個缺口不是單次知識問題，而是：

> **整場會議缺少一個持續的議事責任。**

才考慮：

```text
TEMPORARY STAFF
```

升格條件目前未封版。

預設仍為 Guest Expert。

---

# 11｜Method Layer｜心法第一步

參謀本部第一步不是「開始討論」。

而是：

```text
METHOD
↓
FIRST OBSERVATION
↓
ATTENTION / ACCESSIBILITY
↓
VISIBLE CANDIDATES
↓
SEAT ANALYSIS
```

所以：

```text
MODEL
!=
SEAT
!=
METHOD
!=
KNOWLEDGE
!=
STANCE
```

- Model：誰跑。
- Seat：負責問什麼。
- Method：第一步怎麼看。
- Knowledge：可用資料。
- Stance：目前判斷。

心法區為參謀本部第一步資產層。

---

# 12｜1111 AGENT 遺產

參謀本部 AGENT 骨架承接 1111 的：

```text
SCOPED VIEW
MEANINGFUL WAKE
R1 / O9 / R2
DECIDE / HOLD
ORIGINAL OUTPUT FREEZE
VERSIONED RE-DECISION
NO CROSS-ACTOR REWRITE
```

轉譯成：

```text
SEAT-SCOPED VIEW
MEANINGFUL WAKE
INITIAL VIEW / AUDIT / RECOMPETITION
STANCE / HOLD
IMMUTABLE SEAT OUTPUT
POSITION REVISION
NO CROSS-SEAT STANCE REWRITE
```

---

# 13｜說服

參謀本部不是只保護自主。

它允許合法說服。

```text
STANCE V0
+
MATERIAL DELTA
↓
SEAT RE-DELIBERATION
↓
STANCE V1
```

硬鎖：

```text
V1
DOES NOT ERASE
V0
```

以及：

```text
PERSUASION
!=
CONFORMITY
```

找不到 Material Delta 的立場改變：

```text
UNEXPLAINED_STANCE_DRIFT
```

---

# 14｜Meaningful Wake

```text
ACTIVE MEMBER
!=
MUST SPEAK EVERY ROUND
```

席位只在有：

- 新證據；
- 新異議；
- Proposal Version 改變；
- 工程／成本新材料；
- 前提改變；
- 框架改變；
- 原 blocker 被解除；

等 Material Delta 時重新 Wake。

避免：

```text
EVERYONE SPEAKS
EVERY ROUND
→
MULTI-AGENT THEATER
```

---

# 15｜自由議事

預設：

```text
FREE DELIBERATION
```

人類決定：

```text
WHAT MUST BE RETURNED
```

Council 自己決定：

```text
WHAT MUST BE DISCUSSED NEXT
```

討論方向應主要由：

- 未回答異議；
- 新 Proposal Branch；
- 新證據；
- 工程缺口；
- 成本缺口；
- 專家回報；
- 未閉合基本問題；

自然推進。

---

# 16｜第一版權限圖

```text
                    HUMAN
                      │
                      ▼
               HUMAN DESIRE
                      │
                      ▼
                  SECRETARY
               process owner
                      │
                      ▼
                METHOD ROUTING
                      │
                      ▼
       ┌────┬────┬────┬────┬────┬────┐
       N1   A    B    C    D    E
      常識 擴張 翻桌 資格 工程 成本
       └────┴────┴────┴────┴────┴────┘
                      │
               CONSULT REQUEST
                      │
                      ▼
                  SECRETARY
                      │
              ┌───────┴───────┐
              ▼               ▼
        EXISTING SOURCE    GUEST EXPERT
                              │
                              ▼
                       CONSULTATION RECORD
                              │
                              ▼
                         CORE-6 REWORK
                              │
                              ▼
                       MANDATE EXIT TEST
                              │
                              ▼
                            HUMAN
```

旁路：

```text
N0 NORMAL CONTROL
=
ISOLATED BENCHMARK
```

---

# 17｜目前已成立的核心句

```text
人類先決定要拿回什麼，
不預設決定 AI 要怎麼走過去。
```

```text
秘書處控制議事流，
不控制議事結論。
```

```text
參謀席決定負責問什麼，
心法決定第一步怎麼看。
```

```text
專家提供材料，
不提供主權。
```

```text
席位可以被說服，
不能被共同層偷偷改寫。
```

```text
CONTINUE
!=
CONSENT
```

---

# 18｜第一版尚未補完的缺口

以下故意保留，不在 V0.1 假完成：

## A｜Secretary Kernel State Machine

還需定：

- ROUND 如何開啟；
- 何時進下一輪；
- 何時召回某席；
- 何時判定 no material delta；
- 何時 HOLD；
- 何時 Exit。

## B｜Method Routing

還需定：

- 提案如何選心法；
- 哪個席位載哪些心法；
- 是否 R1 與後續輪次使用不同 Method Pack；
- Method Version 如何鎖定。

## C｜Core-6 Output Contract

還需為 N1 / A / B / C / D / E 分別建立：

- 任務；
- 固定問題；
- 禁止事項；
- 必交欄位。

## D｜Stance State Model

需明確定義：

- SUPPORT
- OPPOSE
- CONDITIONAL_SUPPORT
- CONDITIONAL_OPPOSITION
- HOLD
- UNRESOLVED
- WITHDRAWN_OBJECTION

及其轉移規則。

## E｜Persuasion Trace

需定：

- Material Delta 類型；
- stance change basis；
- accepted / rejected material；
- unresolved objection；
- unexplained drift detection。

## F｜Objection Graph

需定：

```text
CLAIM
→ OBJECTION
→ RESPONSE
→ AMENDMENT
→ STATUS
```

如何持久化。

## G｜Guest Expert Admission

需補：

- 專家資格；
- 來源可信度；
- 多專家衝突；
- 專家偏差；
- 是否需要多模型交叉查核。

## H｜Mandate Exit Test

三類 Mandate 各自的正式完成條件仍需細化。

## I｜Human Desire Discovery

需研究：

```text
STATED SOLUTION
!=
UNDERLYING DESIRE
```

但不得讓 AI 擅自宣稱：

> 「你真正想要的是……」

需要建立「推測欲望」與「人類承認欲望」的分層。

## J｜Benchmark

至少比較：

```text
N0 Normal Agent
vs
Generic Multi-Agent
vs
LIHUO Staff HQ
```

觀察：

- 錯框架發現；
- 基本問題遺漏；
- 有效異議；
- 提前共識；
- 立場漂移；
- traceability；
- Council Overkill。

---

# 19｜V0.1 Standing

本版可以收：

```text
HUMAN DESIRE
→
SECRETARY
→
METHOD ROUTING
→
CORE-6
→
FREE DELIBERATION
→
EXPERT CONSULTATION
→
RE-DELIBERATION
→
MANDATE EXIT
→
HUMAN
```

本版不能宣稱：

- Secretary Kernel 已完成；
- 多 Agent Runtime 已部署；
- Method Routing 已成熟；
- CORE-6 已經實證優於普通 Agent；
- 專家召入已自動化；
- Human Desire 已能準確推斷深層意圖；
- Persuasion 已形式驗證；
- Council 已具生產級決策品質。

---

# 20｜第一版最短定義

> **理火參謀本部是一個以 Human Desire 為入口、以秘書處為程序核心、以六個固定責任席為議事骨架、以心法控制第一觀察入口、以外掛專家補足知識缺口、允許自由說服但禁止不可追溯改判，最後依人類要求的 Mandate 類型交還結果的可審計議事系統。**

這是 V0.1。

下一階段不再擴大架構。

下一階段只做：

> **找缺口。**

**END OF MEMO**
