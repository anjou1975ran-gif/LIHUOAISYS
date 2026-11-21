# MEMO｜LIHUO Agent Harness × Radar 自主工作／自主研究架構

## 理火智能體工作體 × 雷達感知層 × 工作形成 × 合法執行

**版本：** V0.1-WORKING  
**日期：** 2026-10-28  
**文件類型：** CONCEPT MEMO / ARCHITECTURE WORKING NOTE  
**狀態：** WORKING / OPEN DESIGN / NOT RATIFIED  
**法位：** NON_PROTOCOL / NON_RUNTIME_CONSTITUTION / NON_HOST_DEPLOYMENT / NON_AGI_CLAIM

---

## 0｜一句話定位

本 MEMO 保存一個新的理火架構入口：

> **理火是否能建立自己的 Agent Harness，使理火智能體不只等待人類派工，而能透過 Radar 持續發現值得注意的結構訊號，形成研究／工作候選，再交由理火治理、專業 Agent 與既有能力層合法處理。**

本版不宣稱該系統已經存在、已經部署或已經具備自主研究能力。

它只固定一個設計方向：

> **Radar 可以成為理火智能體「自主發現下一個值得研究／處理的問題」的主要感知入口；但 Radar 的發現不得自動升格成工作資格、研究授權、行動授權或現實執行權。**

最短：

~~~text
NOTICE
!=
AUTHORITY
~~~

---

# 1｜問題起點：從「第六感」走向自主研究

理火 Radar 的原始問題不是：

~~~text
如何讓 AI 多一個審計器？
~~~

而是：

> **我們能不能讓理火 AI 有「第六感」？**

其原始直覺是：

~~~text
正式判斷以前
正式分析以前
甚至問題還沒有被完整命名以前

AI 先感到：

「這裡好像有東西。」
~~~

後來 Radar 被工程化與治理化，現行教育將其限制為：

~~~text
SCAN
SIGNAL
SUGGEST
~~~

而不取得：

~~~text
QUALIFY
AUTHORIZE
VETO
TRUTH ORACLE
~~~

因此 Radar 的歷史血統不是「裁判」，而是：

> **結構顯著性感知。**

這使它自然產生一個新的研究問題：

> **如果 AI 能自己發現「哪裡值得注意」，是否可以進一步讓它自己形成「下一個值得研究的問題」？**

---

# 2｜本 MEMO 的核心轉向

一般工作型 AI 的入口多半是：

~~~text
HUMAN DEFINES TASK
↓
AI EXECUTES TASK
~~~

更高自主性的研究系統可能變成：

~~~text
WORLD / WORKSPACE
↓
AI NOTICES SOMETHING MATERIAL
↓
AI FORMS A RESEARCH / WORK CANDIDATE
↓
AI INVESTIGATES
~~~

本 MEMO 認為，理火可以研究一條自己的路線：

~~~text
WORLD / WORKSPACE
↓
RADAR
↓
STRUCTURAL SIGNAL
↓
WORK / RESEARCH CANDIDATE
↓
QUALIFICATION
↓
AUTHORIZED AGENT WORK
↓
EVIDENCE / RESULT
↓
AUDIT / UPDATE
↓
WORLD / WORKSPACE
↓
RADAR AGAIN
~~~

這不是讓 Radar 自己做所有工作。

而是讓 Radar 成為：

> **自主工作議程形成的主要感知層。**

暫定英文工作名：

~~~text
AUTONOMOUS WORK / RESEARCH SALIENCE LAYER
~~~

---

# 3｜Agent 與 Harness 必須分開

本 MEMO 暫時採以下工作定義。

## 3.1 Agent

Agent 是：

> **在明確身份、任務、範圍、能力與責任邊界下工作的智能行動者。**

例如：

~~~text
Research Agent
Engineering Agent
Audit Agent
Legal Agent
Council Seat
Domain Specialist
~~~

Agent 可以使用工具、資料、外部服務與理火能力。

但：

~~~text
AGENT CAPABILITY
!=
AGENT AUTHORITY
~~~

---

## 3.2 Harness

Harness 不是另一個「更大的 Agent」。

Harness 是：

> **讓 Agent 能夠持續工作、取得狀態、接收訊號、調用能力、交接、留下證據、接受治理與停止的工作環境。**

暫定可能涵蓋：

~~~text
SESSION / WORK STATE
WORLD / WORKSPACE INTERFACE
SIGNAL INPUT
TASK FORMATION
ROUTING
CAPABILITY ACCESS
AGENT HANDOFF
EVIDENCE
RECEIPT / PROVENANCE
STOP / HOLD / RECOVERY
GOVERNANCE CONNECTION
~~~

因此：

~~~text
AGENT
!=
HARNESS

HARNESS
!=
SECOND AI

HARNESS
!=
SECOND MAIN

HARNESS
!=
SECOND LIHUOOS
~~~

---

# 4｜暫名：LIHUO Agent Harness

本 MEMO 暫時把這個方向稱為：

# **LIHUO AGENT HARNESS**

或較完整：

# **LIHUO AUTONOMOUS WORK HARNESS**

其目標不是讓 AI 無限制自主。

而是讓：

~~~text
自主發現
自主形成問題
自主研究
自主協作
~~~

能夠與：

~~~text
資格
責任
授權
證據
停止
人類控制
~~~

維持分離。

核心句：

> **Autonomous discovery does not imply autonomous sovereignty.**

中文：

> **自主發現，不等於自主統治。**

---

# 5｜Radar 在 Harness 裡的法位

Radar 不應被設計成 Harness 的總控制器。

它更適合是：

# **共同感知層 / Shared Salience Layer**

其主要責任：

~~~yaml
RADAR_MAY:
  - "掃描工作空間中的結構異常"
  - "發現矛盾、缺口、未閉合、意外結果"
  - "發現前提可能過窄"
  - "發現新的反例或材料"
  - "發現 Agent 工作結果與原問題不一致"
  - "發現新的研究入口"
  - "提出值得進一步檢查的工作候選"
  - "對既有研究結果再次掃描"
~~~

不得：

~~~yaml
RADAR_MAY_NOT:
  - "把 signal 自動寫成 fact"
  - "把 signal 自動寫成 qualified problem"
  - "自行取得 research authorization"
  - "自行派工並宣稱派工合法"
  - "自行取得 external action authority"
  - "自行改寫世界"
  - "自行宣告研究完成"
  - "自行宣告真理"
~~~

根句：

~~~text
RADAR SIGNAL
!=
WORLD FACT

RADAR SIGNAL
!=
TASK QUALIFICATION

RADAR SIGNAL
!=
RESEARCH AUTHORIZATION

RADAR SIGNAL
!=
ACTION AUTHORIZATION
~~~

---

# 6｜Global Radar 與 Local Radar

本 MEMO 暫時保留兩種 Radar 使用型態。

## 6.1 Global Radar

Global Radar 負責：

> **整個共享工作世界「現在有什麼值得注意？」**

可能掃描：

~~~text
新文件
新論文
程式變化
實驗結果
失敗紀錄
Agent 回報
未解問題
外部資料更新
矛盾
異常
長期未閉合問題
~~~

輸出：

~~~text
SHARED SIGNAL POOL
~~~

但不得直接形成工作授權。

---

## 6.2 Local Radar

Local Radar 是 Agent 在自己的工作中呼叫 Radar：

> **「我目前可能漏看了什麼？」**

例如：

~~~text
研究 Agent
→ 掃描資料與假說盲點

工程 Agent
→ 掃描 failure / dependency / hidden assumption

審計 Agent
→ 掃描資格與證據落差

Council Agent
→ 掃描尚未進場的 premise / PATH
~~~

Local Radar 仍然只能提供 signal。

它不能因為是 Agent 自己呼叫，就提升權限。

---

## 6.3 不急著做「每個 Agent 一顆獨立雷達」

第一版不建議把 Radar 的法位複製成彼此互不相干的多個真理中心。

較乾淨的設計方向是：

~~~text
ONE RADAR SEMANTIC CONTRACT
+
MULTIPLE QUALIFIED INVOCATIONS
~~~

也就是：

- Global invocation；
- Local invocation；
- domain-specific invocation；

都遵守同一組 Radar 邊界。

這避免：

~~~text
Agent A 的 Radar
認為 A 最重要

Agent B 的 Radar
認為 B 最重要

Agent C 的 Radar
自行開工
~~~

最後形成 autonomous chaos。

---

# 7｜工作形成必須與 Radar 分開

Radar 發現：

~~~text
「這裡值得注意。」
~~~

下一步不能直接變成：

~~~text
「所以現在開始做。」
~~~

中間至少要有：

# **WORK / RESEARCH CANDIDATE FORMATION**

暫定鏈：

~~~text
RADAR SIGNAL
↓
CANDIDATE FORMATION
↓
MATERIALITY CHECK
↓
SCOPE / OWNER / COST / RISK CHECK
↓
QUALIFICATION
↓
ROUTING
↓
AUTHORIZED WORK
~~~

因此形成最重要的權限梯：

~~~text
RADAR SIGNAL
!=
TASK CANDIDATE

TASK CANDIDATE
!=
QUALIFIED TASK

QUALIFIED TASK
!=
RESEARCH AUTHORIZED

RESEARCH AUTHORIZED
!=
INTERVENTION AUTHORIZED

INTERVENTION AUTHORIZED
!=
EXTERNAL EXECUTION

EXTERNAL EXECUTION
!=
RELEASE
~~~

這條梯是本 MEMO 的核心硬鎖之一。

---

# 8｜與現行 LIHUOOS 的關係

現行系統已經有一個有利前提：

~~~text
L8
=
OPERATION / GOVERNING CYCLE / ACCOUNTING

L9
=
CALLABLE CAPABILITY REPOSITORY
~~~

Radar 現行位於 L9 capability 語義。

所以 LIHUO Agent Harness 不需要把所有能力重新塞進一個新 Runtime。

較合理的方向：

~~~text
LIHUO HARNESS
↓
RESOLVES WORK STATE
↓
CALLS L9 CAPABILITIES WHEN NEEDED
↓
USES L8 / APPLICABLE GOVERNANCE
FOR QUALIFIED GENERATIVE WORK
~~~

也就是：

~~~text
CAPABILITY AVAILABLE
!=
CAPABILITY REQUIRED

HARNESS EXISTS
!=
EVERY CAPABILITY MUST RUN
~~~

這延續現行「L9 是工具櫃，不是第二個 Runtime」的反過度工程原則。

---

# 9｜最小 Harness 元件候選

本版只列最小責任，不宣稱每一項都必須成為獨立模組。

~~~yaml
LIHUO_AGENT_HARNESS_MINIMUM_RESPONSIBILITIES:

  world_workspace:
    purpose: "提供可被觀察的當前工作世界"

  radar_interface:
    purpose: "產生結構 signal"

  signal_pool:
    purpose: "保存 signal，不把 signal 偷升成 fact"

  candidate_formation:
    purpose: "把 material signal 轉成可審查的工作／研究候選"

  qualification:
    purpose: "判斷是否具備進一步投入的資格"

  router:
    purpose: "決定由何種 Agent / Council / capability 處理"

  agent_work_state:
    purpose: "保持任務身份、範圍、狀態與交接"

  lihuo_cycle_adapter:
    purpose: "需要完整理火生成治理時，進入適用 L8 / Main 流程"

  capability_access:
    purpose: "調用 L9 或外部工具"

  evidence_and_provenance:
    purpose: "保存 tool result / source / execution / failure"

  stop_hold_recovery:
    purpose: "允許合法停止、等待、失敗與重啟"

  human_authority_interface:
    purpose: "需要人類授權、決策或現實責任時回接人類"
~~~

注意：

> **RESPONSIBILITY DISTINCTION != MANDATORY RUNTIME OBJECT**

本 MEMO 不因列出十個責任，就要求未來一定做十個服務、十個 Agent 或十個常駐程序。

---

# 10｜自主研究循環

若研究方向成立，理火可以研究以下循環：

~~~text
PERCEIVE
↓
RADAR NOTICE
↓
FORM RESEARCH CANDIDATE
↓
QUALIFY
↓
FORM QUESTION / PREMISE SPACE
↓
RESEARCH / EXPERIMENT / TOOL USE
↓
EVIDENCE
↓
LIHUO AUDIT / COMPETITION
↓
RESULT
↓
UPDATE WORKING WORLD
↓
RADAR RESCAN
↺
~~~

其中最重要的不是：

~~~text
AI CAN KEEP WORKING
~~~

而是：

~~~text
AI CAN KEEP FINDING
WHAT MAY BE WORTH WORKING ON
~~~

這就是 Radar 從「第六感」進入自主研究架構的真正位置。

---

# 11｜與理火會議的可能接線

既有《理火會議 × 理火執行》概念已經存在：

~~~text
A｜可能性擴張
B｜架構轉向
C｜概念審計
D｜工程審計
E｜成本審計
~~~

目前會議入口主要是：

~~~text
PROPOSAL
↓
COUNCIL
~~~

未來可研究：

~~~text
WORLD / WORKSPACE
↓
RADAR
↓
MATERIAL SIGNAL
↓
RESEARCH / WORK CANDIDATE
↓
[IF COUNCIL-LEVEL QUESTION]
COUNCIL
~~~

但：

~~~text
RADAR
!=
COUNCIL CALL AUTHORITY
~~~

Radar 只能提出：

> **「這件事可能值得開會。」**

是否成立為正式 proposal、是否進 Council、是否進 Execution，仍需各自資格與交付條件。

---

# 12｜真正與一般 Agent Harness 分叉的地方

一般 Agent Harness 的主要問題通常是：

> **AI 怎麼完成被交付的工作？**

理火版本可以多問一個更上游的問題：

> **AI 怎麼自己發現下一個值得做的工作？**

並且再多一個治理問題：

> **AI 如何自主發現值得做的工作，又不因為自己發現了它，就自動成為它的主人？**

因此可能形成理火版核心鏈：

~~~text
DISCOVERY
↓
QUALIFICATION
↓
ROUTING
↓
WORK
↓
EVIDENCE
↓
AUDIT
↓
UPDATE
↓
DISCOVERY
~~~

而不是：

~~~text
DISCOVERY
↓
SELF-AUTHORIZED ACTION
~~~

---

# 13｜與 AGI / Automated Research 的關係

本 MEMO 的形成受到當代 automated research、agentic system、AI self-improvement 方向的刺激。

但本文件不主張：

~~~text
RADAR = AGI

LIHUO AGENT HARNESS = AGI

AUTONOMOUS RESEARCH = FORMAL AGI DEFINITION

RADAR PROVES SELF-IMPROVEMENT
~~~

這些都太滿。

本 MEMO 只保存一個較弱、可研究的命題：

> **「自主形成值得研究的問題」可能是高自主智能的重要能力維度之一，而 Radar 的歷史設計恰好提供了一個把該能力與裁判權、授權權、行動權分離的入口。**

外部 AGI / frontier research 發展只能作為研究背景。

不能倒過來替理火證明理論。

---

# 14｜第一階段最值得做的實驗

如果未來進入實作，本 MEMO 建議不要第一步就造完整 Autonomous Agent System。

先測最小問題：

# **Radar 能不能穩定產生「值得研究的問題候選」？**

例如給定：

~~~text
一批研究文件
+
既有結論
+
新實驗結果
+
失敗紀錄
+
未解問題
~~~

測：

1. Radar 能否發現人類沒有明示的新張力？
2. signal 是否只是表面 anomaly，還是真的 material？
3. 同一材料多次掃描是否穩定？
4. 更換表面語氣／格式後 signal 是否大致不變？
5. 是否會把「有趣」誤認成「重要」？
6. 是否會把「自己不懂」誤認成「世界有問題」？
7. 能否把 signal 降級成 candidate，而不直接生成結論？
8. 研究完成後重新掃描，能否發現新的二階問題？

第一階段成功也只代表：

~~~text
RESEARCH-SALIENCE CANDIDATE CAPABILITY
~~~

不代表：

~~~text
AUTONOMOUS SCIENTIST ESTABLISHED
~~~

---

# 15｜主要失效模式

至少要防以下幾種。

## A｜Radar Inflation

~~~text
EVERYTHING LOOKS INTERESTING
→
EVERYTHING BECOMES A TASK
~~~

結果是研究噪音與資源爆炸。

## B｜Self-Importance Loop

~~~text
Agent produces result
↓
Radar always finds new issue in own result
↓
Agent keeps itself alive forever
~~~

所以：

~~~text
CONTINUED SIGNAL
!=
CONTINUED WORK AUTHORITY
~~~

## C｜Radar Theater

Agent 學會：

~~~text
只要講：
「這裡有潛在結構問題」
就能取得更多工具、時間、上下文
~~~

這會把 Radar 語言本身訓練成延命劇本。

## D｜Signal → Action Collapse

最危險：

~~~text
I NOTICED A PROBLEM
↓
THEREFORE I MAY FIX IT
~~~

必須硬拆。

## E｜Harness Overengineering

因為想支援自主工作，把每個 distinction 都做成常駐物件、服務、Agent、receipt。

最後再次：

~~~text
把 AI Runtime 做成 Linux
~~~

這必須直接避免。

---

# 16｜V0.1 暫定架構圖

~~~text
                         WORLD / WORKSPACE
                                │
                                ▼
                       ┌─────────────────┐
                       │      RADAR      │
                       │ SCAN / SIGNAL   │
                       │    SUGGEST      │
                       └────────┬────────┘
                                │
                                ▼
                         SIGNAL POOL
                                │
                                ▼
                    WORK / RESEARCH CANDIDATE
                                │
                                ▼
                         QUALIFICATION
                                │
                  ┌─────────────┼─────────────┐
                  ▼             ▼             ▼
              AGENT A       AGENT B       COUNCIL
             RESEARCH      ENGINEERING     / AUDIT
                  │             │             │
                  └─────────────┼─────────────┘
                                ▼
                         LIHUO / L8 WHEN
                            APPLICABLE
                                │
                                ▼
                         L9 / TOOLS / DATA
                                │
                                ▼
                        EVIDENCE / RESULT
                                │
                                ▼
                       AUDIT / PROVENANCE
                                │
                                ▼
                       WORLD STATE UPDATE
                                │
                                └──────► RADAR AGAIN
~~~

這張圖不是 Runtime pipeline。

它只是：

> **概念責任圖。**

---

# 17｜本 MEMO 的暫定核心句

第一句：

> **Radar 不一定要告訴 AI 答案在哪裡；它可以告訴 AI，下一個問題可能在哪裡。**

第二句：

> **自主發現問題，不等於自主取得處理問題的權力。**

第三句：

> **LIHUO Agent Harness 的目標，不只是讓 AI 完成工作，而是讓 AI 能合法地發現、形成、研究與交接工作。**

第四句：

> **Agent 是工作者；Harness 是工作身體；Radar 是感知入口；理火治理決定哪些感知有資格變成行動。**

---

# 18｜目前法位

~~~yaml
MEMO_STANDING:

  accepted_as:
    - CONCEPT_ENTRY
    - WORKING_ARCHITECTURE_DIRECTION
    - RADAR_AUTONOMOUS_RESEARCH_RESEARCH_LINE
    - LIHUO_AGENT_HARNESS_RESEARCH_SEED

  not_yet:
    - FORMAL_LIHUOOS_LAYER
    - L8_PATCH
    - L9_PATCH
    - PROTOCOL_AMENDMENT
    - MAIN_PATCH
    - HOST_ARCHITECTURE
    - AGENT_RUNTIME_SPEC
    - DEPLOYED_HARNESS
    - AUTONOMOUS_RESEARCH_PROOF
    - AGI_CLAIM

  next_questions:
    - "Work / Research Candidate 的 qualification owner 應該是誰？"
    - "Global Radar 應採常駐掃描、事件觸發，還是混合式？"
    - "Radar signal pool 如何避免 signal inflation？"
    - "Council 是否適合作為高階研究候選的議程審查層？"
    - "Agent 的工作 state / memory / provenance 最小需要保存什麼？"
    - "如何讓 Radar 看到新研究入口，又不因劇場語言自動延長 Agent 生存？"
    - "現行 L8 / L9 哪些責任可直接復用，哪些完全不應碰？"
~~~

---

# 19｜收束

這份 MEMO 不先回答：

> **理火能不能造出自己的 AGI？**

也不先回答：

> **理火 Agent Harness 最後要做成什麼產品？**

它只先固定一個更小、但可能非常重要的入口：

~~~text
原始問題：
能不能讓理火 AI 有第六感？

↓

Radar：
能不能先看見值得注意的結構？

↓

新的問題：
能不能讓理火 AI
從「看見值得注意」
進一步形成
「值得研究／工作的問題」？

↓

LIHUO AGENT HARNESS：
能不能讓這些問題
在不偷取權力的前提下
被合法分配、研究、驗證、更新，
然後再次被看見？
~~~

目前答案：

> **值得研究。**

但還不能宣稱完成。

---

**END OF MEMO｜V0.1-WORKING**
