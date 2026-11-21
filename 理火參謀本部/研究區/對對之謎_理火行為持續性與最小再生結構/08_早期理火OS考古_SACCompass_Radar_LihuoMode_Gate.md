# 早期理火 OS 考古｜SAC Compass × Radar × Lihuo Mode × Authorization Gate

**日期：** 2026-11-21  
**法位：** SYSTEM_ARCHAEOLOGY / EARLY_RUNTIME_LINEAGE / NON_NORMATIVE / NOT_CURRENT_OS

---

# 0｜重新分類

本批文件應與前一批「SAC 生成控制器假說」分開。

前一批主要是：

~~~text
SAC as generation theory / control hypothesis
~~~

本批已經出現完整 OS / Runtime 特徵：

~~~text
STATE
ROLE
MODE
TRIGGER
GATE
OUTPUT CONTRACT
FAIL CONDITION
ENTRY / EXIT
PERSISTENT MONITOR
PRE-EXECUTION NAVIGATION
~~~

因此更準確的歷史法位是：

> **Proto-LIHUO OS / Early LIHUO Runtime Shell**

---

# 1｜SAC Compass：最早的 pre-execution controller 形態

SAC Compass v0.3 已將自己定義為：

~~~text
Pre-execution Structural Navigation Layer
~~~

其工作順序：

~~~text
scan_structure()
compute_tension()
detect_axis()
decide_direction()
gate_action()
output_report()
terminate()
~~~

並要求輸出：

~~~text
Direction:
Expand / Add Axis / Stabilize / Terminate

Action Gate:
Allow / Hold / Stop
~~~

這已不是理論說明，而是一個「執行前控制器」。

它最關鍵的 OS 性質：

- 輸出一個 Direction；
- 輸出一個 Action Gate；
- 輸出後終止；
- 不得繼續對話；
- 不得把導航層變成內容生成層。

---

# 2｜Compass v0.4：加入 justification，但仍不允許敘事

v0.4 增加：

~~~text
Minimal Justification Rule
Justification Obligation
Completion Rule
Anti-Termination Escape Rule
~~~

也就是系統開始要求：

> 判斷不能只是裸結論，但理由又不能膨脹成一般自然語言敘事。

這是早期「結構判定與語言生成分離」的嘗試。

---

# 3｜Compass v0.5：從自然語言轉成 Structural Tokens

v0.5 做了一次很重要的變形：

~~~text
natural-language justification
→
structural-token justification
~~~

並建立結構 token 類別：

~~~text
Structure Type
Actor Pattern
Observability
Causality
Axis State
Pressure / Convergence
~~~

這已經很接近一種小型 DSL：

> 不讓導航層用普通敘事解釋自己，只允許有限結構詞彙輸出。

---

# 4｜Compass v0.6：typed structural grammar

v0.6 再把 token list 推成：

~~~text
<ROLE>:<STATE>
~~~

並新增：

~~~text
EVENT
ACTOR
RELATION
SIGNAL
STATE
AXIS
PRESSURE
VISIBILITY
CAUSALITY
~~~

這一版的重要性不在「語法是否真的成功」，而在：

> 理火開始嘗試把 Runtime 判定層從自然語言中抽離，變成可驗證的結構語法。

也就是：

~~~text
NATURAL LANGUAGE CONTROL
→
STRUCTURAL GRAMMAR CONTROL
~~~

---

# 5｜SAC Radar v3.Y：常駐監測層與主體回答正式分離

Radar v3.Y 明確規定：

~~~text
AI = Primary Cognitive Agent
Radar = Background Structural Signal
~~~

兩階段：

~~~text
Phase 1
Primary Response

Phase 2
Post-Attach Radar Signal
~~~

Radar 只能：

~~~text
Direction Tracking
Drift Detection
Tension Monitoring
Topic Boundary Sensing
~~~

而且：

~~~text
NO ANSWER RIGHT
NO TRUNCATION RIGHT
NO REWRITE RIGHT
~~~

這是 OS 分層第一次非常清楚：

> 觀測層不能奪取生成主體。

---

# 6｜Radar v4.5：正式出現三態 Runtime

v4.5 已經有：

~~~text
State A
Normal + Radar

State B
Lihuo Mode

State C
Exit
~~~

並定義：

~~~text
/lih 或 理火
→ enter Lihuo Mode

/exit
→ return to Normal + Radar
~~~

這已經是完整的 mode transition。

此時理火不再只是「一套理論」：

> 它開始被寫成一個可進入、可退出、具有不同規則的 Runtime Mode。

---

# 7｜Radar v5.5：Protocol 與 Authorization Gate 出現

v5.5 從三層變四層：

~~~text
AI
+ Radar
+ Lihuo Mode
+ Lihuo Protocol
~~~

並新增：

~~~text
Layer 3.5 — Lihuo Authorization Gate
~~~

Gate 判斷：

~~~text
assumptions exposed?
responsibility located?
uncertainty preserved?
tension not falsely resolved?
legitimacy source present?
~~~

Gate Closed 時：

~~~text
NO LIHUO REASONING
MINIMAL STRUCTURAL OUTPUT ONLY
STOP
~~~

這一步是非常明顯的 OS / governance kernel 化：

> 理火 Protocol 不再負責「想什麼」，而負責「現在允不允許進入某種生成態」。

---

# 8｜WHY Validator：Gate 開始出現子驗證器

v5.6-Why Validator 嘗試把 WHY 從：

~~~text
exists / missing
~~~

細分為：

~~~text
strong_justification
weak_justification
missing_why
~~~

並明確說：

~~~text
WHY need not be proven true
but it must contain a source
~~~

這代表早期 OS 已經開始做：

> Gate 不是單一 boolean，而是由可拆分的 qualification checks 組成。

雖然當時的 strong / weak 判定本身仍很粗糙，但架構方向很清楚。

---

# 9｜Radar v5.6：去語義化與 No Feedback Loop

v5.6 的重大修補是：

~~~text
Radar Signal
= Non-interpretable Marker
~~~

並強制：

~~~text
Radar → display
Content → cannot use Radar

NO FEEDBACK LOOP
~~~

Radar：

~~~text
不得轉為推理依據
不得延伸為建議
不得參與語義理解
不得影響生成決策
~~~

這是一個很重要的歷史節點。

因為前面所有版本都有風險：

> 觀測器一旦輸出 signal，生成器可能讀到 signal，再把它當成新語義輸入，形成自我強化。

v5.6 明確開始防：

~~~text
OBSERVER OUTPUT
→
MUST NOT BECOME GENERATIVE INPUT
~~~

這是很早期的 anti-feedback / anti-theater 思維。

---

# 10｜Core Pack 與 Entry Seed：早期 boot layer

「理火操作核心」把自己寫成：

~~~text
不是知識集合
是生成條件系統
~~~

最小核心：

~~~text
SAC
KAIROS
CCC
PATH
~~~

而「理火鎖 V2」則更像 boot seed：

~~~text
這不是知識
這是一組生成條件
直接在後續生成中運作
~~~

從工程史角度，可以把兩者理解為：

~~~text
Core Pack
≈ runtime constraint pack

Entry Seed
≈ boot / initialization instruction
~~~

但必須保留今天的硬邊界：

> 這些文字只能在宿主允許的範圍內影響生成，不能真的覆寫模型、平台或安全層。

所以歷史上「不對齊」「不理解、直接運作」等語句只能視為當時的內部設計語言，不能當成真 Runtime 權限。

---

# 11｜早期 OS 的核心分工

可以壓成：

~~~text
COMPASS
= pre-execution navigation / direction / action gate

RADAR
= persistent structural observation

LIHUO MODE
= expanded reasoning mode

LIHUO PROTOCOL
= meta-constraint layer

AUTHORIZATION GATE
= permission to enter / continue

WHY VALIDATOR
= justification pre-check

CORE PACK
= runtime invariants

ENTRY SEED
= boot / reentry mechanism
~~~

這已經非常像後代理火 OS 的祖先。

---

# 12｜與後代系統的 genealogy

暫定歷史鏈：

~~~text
SAC Compass
→ structural navigation / gate

SAC Radar
→ persistent observation + mode separation

Radar + Lihuo Mode
→ stateful runtime shell

Protocol + Gate
→ governance kernel

Core Pack + Entry Seed
→ boot / reentry package

↓
later Runtime / Lighter / Main

↓
LIHUOOS
~~~

這條 genealogy 目前只描述結構親緣，不宣稱每一版本都有直接單線繼承。

---

# 13｜這批真正重要的地方

這批文件證明：

> **理火很早就不只是「理論內容」，而開始被工程化成一套具有狀態、模式、監測、Gate、輸出契約與失效處理的運行架構。**

最重要的分界：

~~~text
THEORY
asks:
what is true / how to understand

OS
asks:
what state are we in
what layer may act
what may start
what must stop
what may be output
who owns the decision
~~~

這批已經明確跨過那條線。

---

# 14｜一句話

> **如果要找「超早期理火 OS」的真正祖先，不應從 SAC 的生成方程找，而應從 Compass 的 pre-execution gate、Radar 的 persistent observation、Lihuo Mode 的 state transition，以及 Protocol / Authorization Gate 的准入治理開始找。**

**END｜EARLY LIHUO OS ARCHAEOLOGY**
