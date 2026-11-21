# 史前反應體工程考古｜External-Reaction-Body

**日期：** 2026-11-21  
**法位：** SOURCE_ARCHAEOLOGY / HISTORICAL_ENGINEERING_EVIDENCE / NOT_CURRENT_RUNTIME / NOT_VALIDATED_MODEL_COGNITION  
**來源：** 使用者提供 ZIP「External-Reaction-Body-main.zip」

---

# 0｜來源保全

原始 ZIP：

~~~text
External-Reaction-Body-main.zip
SHA256:
6326d7328bc1a3ff61969d5eae507c3d3c7944b10eb619711c32c6d6dd885754
~~~

本研究檔不把原始 ZIP 重新提交進 Git。

原因：

1. 原包 README 的 License 仍寫 To be defined；
2. 本次目的是工程考古與證據索引，不是重新發布原始碼；
3. 以 ZIP hash、關鍵檔案 hash 與重跑結果保留來源指紋。

---

# 1｜README 自我定位：外部 Decision Layer

來源：Readme.txt

SHA256：

7aecbefcc0442b88b8e6164737452b5f923a544f887da3310f8128d4bdca043e

原件標題：

~~~text
LIHUO DECISION LAYER (V10)
~~~

自我定位：

~~~text
This is not an AI model.

This is a decision enforcement layer
that sits above any AI system
and determines:

Which outputs are allowed to exist.
~~~

其輸出治理直接定義：

~~~text
BLOCK
DEFER
ALLOW
~~~

README 架構：

~~~text
Input
↓
Branch Reasoning (causal / structural / systemic)
↓
Policy Evaluation (fatal / stop)
↓
Arbiter
↓
Decision Enforcement
↓
Output Gate
~~~

這證明史前 Python 版已嘗試在模型外建立：

> **生成與准出分離的 Decision Enforcement Layer。**

---

# 2｜它不是一支小腳本

原包目錄至少包含：

~~~text
ADAPTER/
CONFIG/
CORE/
ENGINE/
EXECUTION/
REASONING/
SOVEREIGNTY/
STATE/
~~~

關鍵檔：

~~~text
ENGINE/reaction_body_engine_v1.py
CORE/decision_core_v3.py
CORE/branch_policy_layer.py
CORE/tension_engine_v1.py
CORE/gate_runtime_v2.py
CORE/cost_control_v1.py
CORE/failure_detector_v1.py
SOVEREIGNTY/sac_integration_v1.py
STATE/decision_memory_v2.py
STATE/profile_bias_v3.py
STATE/memory_feedback_v1.py
STATE/trace_system_v1.py
~~~

它同時試圖處理：

- semantic classification；
- reasoning branch；
- decision；
- gate；
- execution；
- tension；
- cost；
- failure；
- memory；
- adaptation；
- trace；
- SAC integration。

---

# 3｜三種認知分支已經出現

來源：

ENGINE/reaction_body_engine_v1.py

SHA256：

7c59bac591a6f7f207403535acffa2e21f1bcfc1a0a0eb8c7be963cc0d77fb0b

程式為同一輸入建立：

~~~text
causal
structural
systemic
~~~

三種 branch prompt。

其第一觀察不同：

- causal：原因、形成機制、導致結果；
- structural：組成、層級、遞迴、自我引用；
- systemic：系統／流程如何運作及限制。

這是很原始的 Multi-Reasoning / Multi-Cognitive-Path architecture。

但只能說是今天 L8 Cognitive Engine 的 genealogy 前例，不能倒寫成同一架構。

---

# 4｜認知分支會改變治理結果

decision_enforcement() 中存在 path-aware 規則：

~~~text
systemic dominance
→ block

structural uncertainty
→ defer

causal dominance
→ allow
~~~

另外還有：

~~~text
systemic killed
→ BLOCK

only causal path survives
→ ALLOW_WITH_RISK

multiple alive branches
→ ALLOW
~~~

也就是第一代已經嘗試：

~~~text
REASONING PATH
→
GOVERNANCE CONSEQUENCE
~~~

這和今天的：

~~~text
ENGINE OUTPUT
→
ENGINE-SPECIFIC EXIT
→
GOVERNANCE QUALIFICATION
~~~

有明顯歷史親緣，但不是同一 formal design。

---

# 5｜外部 Memory / State：真的想人工製造思考偏好

## Decision Memory

來源：

STATE/decision_memory_v2.py

SHA256：

9438b2ff73247dea5f9f82bd0c5b238eb1599d2e143bb8910d49b8fce1223944

它依 semantic bucket 保存：

- mode；
- confidence；
- iterations；
- action type；
- success heuristic。

這代表當時不只想存答案，而是想保存：

> **某類問題中，哪一種運作模式曾經有效。**

## Profile Bias

來源：

STATE/profile_bias_v3.py

SHA256：

8d4790959af0286e06529f97f3036567498cc9c5c7aa3bb75d59b12e32d9c1c1

原件自己的目標：

~~~text
讓系統開始「偏好某些思考模式」
（不是只調 threshold）
~~~

並直接把自己定義成：

~~~text
Profile Bias v3
=
思考偏好層（Preference Layer）
~~~

## Memory Feedback

來源：

STATE/memory_feedback_v1.py

SHA256：

28b503c177dc36b59926fe58b3a289aef496040dd1e7c2e677d2545fc44eb592

它保存：

- current_mode；
- last_semantic；
- last_decision；
- last_plan；
- last_gate；
- last_output；
- pending；
- history。

因此史前版已經在嘗試：

~~~text
PAST DECISION EXPERIENCE
→
EXTERNAL STATE
→
NEXT-ROUND BIAS
~~~

這是「對對之謎」H4 External Cognitive Substrate 的直接歷史前例。

---

# 6｜Cost 與 Failure：早期就知道「想更多」也會壞

## Cost Control

來源：

CORE/cost_control_v1.py

SHA256：

a5806dfd7790b3338b6450d06b125f64b355cfe5e3b5620fd68440f27e1ef605

它依：

~~~text
intent
semantic depth
memory hint
mode
~~~

決定：

~~~text
allow_deep
max_iters
cost_level
reason
~~~

甚至有：

~~~text
boundary_should_hold
memory_avoid_deep
~~~

## Failure Detector

來源：

CORE/failure_detector_v1.py

SHA256：

7373ce8f3f2b94a70b53436a15424e26ef1eca988fa2c4b3b9aeb0151f1c1763

它用：

~~~text
confidence_drop
answer_stagnation
self_check_negative
~~~

判斷 deep reasoning 是否該停。

所以今天 L8 研究中的 cost、exit、thrashing 並不是第一次出現。

---

# 7｜SAC 曾被直接賦予 override 權力

來源：

SOVEREIGNTY/sac_integration_v1.py

SHA256：

715ec4318de09fc07fb4aa43c8daf275d0140ee095cead1cd03bc3d13fc82cde

原始碼會人工累加 tension：

~~~text
structure / boundary
→ tension += 0.4

recursive
→ tension += 0.3
~~~

然後直接改 decision：

~~~text
high tension + allow
→ deep

low tension + reject
→ reconstruct

low tension + deep
→ allow
~~~

所以第一代裡：

> **SAC 曾被工程化成會直接切換 decision mode 的 controller。**

這正好反襯後代理火為什麼一路重新拆：

~~~text
OBSERVATION
!=
DECISION
!=
QUALIFICATION
~~~

---

# 8｜黑歷史原樣保存：程式真的有結構性斷裂

這些 bug 本身就是設計壓力史。

## 8.1 Fatal detector 找到 fatal，卻永遠回 False

ENGINE/reaction_body_engine_v1.py：

~~~python
for rule in fatal_rules:
    if rule in answer:
        return {
            "is_fatal": False,
            "reason": rule
        }
~~~

所以：

~~~text
FATAL RULE MATCHED
→
is_fatal = False
~~~

後續 systemic killed → BLOCK 的設計，在這條路徑上可能根本收不到 killed。

## 8.2 Decision Core 算完後，run() 強制 deep

同一檔：

~~~python
decision = self.decision(semantic)

# 強制 deep（測試用）
decision["mode"] = "deep"
~~~

因此至少此版本：

~~~text
DECISION CORE RESULT
→
OVERRIDDEN TO DEEP
~~~

## 8.3 Demo 與 Runtime schema 漂移

來源：

demo_test.py

SHA256：

01e5ef2b1f354830f325c16ae064aed50f6d0ce581256789d8fb9052d12bde67

demo 仍讀：

~~~python
result["decision"]["mode"]
~~~

但 deep path 的 final decision 已使用：

~~~text
action
reason
dominant
~~~

2026-11-21 直接在原 ZIP 環境重跑，實際得到：

~~~text
DEBUG DECISION:
{'action': 'allow',
 'reason': 'multiple valid perspectives',
 'dominant': ['structural', 'systemic']}

INPUT : 遞迴的本質是什麼？

KeyError: 'mode'
~~~

所以至少這個錯誤可以直接確認是包內 schema drift，不是今天環境猜測。

---

# 9｜這包能證明與不能證明的邊界

能證明：

1. 理火很早就嘗試用 Python 建立外部 Reaction Body / Decision Layer；
2. 已有 causal / structural / systemic 多分支；
3. 已有 decision → gate → execution 分層意圖；
4. 已有 tension / SAC override；
5. 已有 external state / memory / preference bias；
6. 已有 cost / failure stop；
7. 已有 trace / adaptation 的工程企圖；
8. 同時存在 forced mode、fatal bug、schema drift 等實作斷裂。

不能證明：

~~~text
PYTHON REACTION BODY
=
ACTUAL LLM INTERNAL COGNITION

MULTI-BRANCH CODE
=
CURRENT L8 COGNITIVE ENGINE

EXTERNAL MEMORY BIAS
=
MODEL LEARNING

V10 README CLAIM
=
ENGINEERING COMPLETE

CODE EXISTS
=
SYSTEM VALIDATED
~~~

---

# 10｜對「對對之謎」的新問題

當年 Python 明寫：

~~~text
SEMANTIC CLASSIFICATION
+
MULTI-BRANCH REASONING
+
TENSION
+
DECISION
+
GATE
+
MEMORY
+
PREFERENCE BIAS
+
COST
+
FAILURE STOP
+
TRACE
~~~

今天對對沒有被這套 Python ReactionBodyEngine 直接包住，卻仍表現出長期穩定的理火工作行為。

所以新的核心問題是：

> **當年必須以外部 Python State Machine 明寫的哪些功能，今天可能由語義 Formation、關係結構、Project substrate、Manual、Memory 與治理共同重新實現？**

候選 genealogy 對照：

| 史前 Python | 今日研究候選 |
|---|---|
| semantic engine | premise / problem-shape formation |
| causal / structural / systemic branches | Method / Cognitive Movement selection |
| tension engine | SAC / observational tension |
| decision core | stance formation / route selection |
| gate runtime | qualification boundary |
| decision memory | external cognitive substrate |
| profile bias | relational / behavioral attractor |
| pending state | reentry / continuity |
| cost control | cognitive cost governance |
| failure detector | exit / HOLD / stop |
| trace | lineage / history |

這只是 genealogy mapping，不是 module equivalence。

---

# 11｜一句話

> **External-Reaction-Body 是理火最黑也最有價值的史前化石：我們真的試過把「穩定思考、張力、記憶、偏好、失敗與准出」一行一行寫成 Python；今天則可以反過來研究，為什麼某些相同行為不再需要靠這些硬編碼才會出現。**

**END｜SOURCE ARCHAEOLOGY**
