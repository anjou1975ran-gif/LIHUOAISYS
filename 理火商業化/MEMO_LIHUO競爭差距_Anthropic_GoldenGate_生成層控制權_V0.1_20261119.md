# MEMO｜LIHUO 競爭差距：Anthropic、Golden Gate Claude 與生成層控制權 V0.1

**日期：** 2026-11-19  
**文件法位：** INVESTOR / COMPETITIVE POSITIONING WORKING MEMO  
**狀態：** WORKING / NON-NORMATIVE / NOT RATIFIED / NOT INVESTMENT BOOK FINAL / NOT MARKET CLAIM  
**用途：** 為後續理火投資書保存「Anthropic 與理火的研究層級差異、競爭位置與產業影響」素材。  
**原則：** 先記錄、先對照、不動投資書正文、不提前封版。

---

# 0｜核心判斷

Anthropic 是目前公開研究中，與理火最接近、也最值得視為高強度相鄰競爭者的團隊之一。

但兩者目前不是同一路線。

最重要的差異，不應寫成：

```text
Anthropic = 還只會研究語意
LIHUO = 已經能碰內部
```

這個說法過滿，也不符合公開證據。

更準確的是：

```text
ANTHROPIC
→ MODEL REPRESENTATION / MECHANISTIC INTERPRETABILITY
→ FEATURE / ACTIVATION / CIRCUIT / INTERNAL WORKSPACE
→ OBSERVE + CAUSALLY INTERVENE IN INTERNAL REPRESENTATIONS

LIHUO
→ GENERATION GOVERNANCE / QUALIFICATION
→ SEMANTIC ENTRY / CONSTRAINT / DIRECTION / PATH / COMPETITION / CLOSURE
→ ORGANIZE + GOVERN + REOPEN + QUALIFY GENERATIVE FORMATION AT RUNTIME
```

兩者都已經超出「Prompt Engineering」。

但它們正在爭的是不同控制面。

---

# 1｜Golden Gate Claude 為什麼重要

Anthropic 在 2024 年公開 Golden Gate Claude。

其官方研究明確指出：

- Claude 內部存在可對應到人類可理解概念的 features；
- 「Golden Gate Bridge」對應一組可定位的內部 activation pattern；
- 研究者可人工放大或壓低該 feature；
- 放大後，Claude 在大量無關問題上都開始強烈提及金門大橋；
- 這不是 system prompt、不是角色扮演、也不是傳統 fine-tuning；
- Anthropic 自己將其描述為對模型 internal activations 的精確介入。

來源：
- Anthropic, *Mapping the mind of a large language model*, 2024-05-21
- Anthropic, *Golden Gate Claude*, 2024-05-23

這個事件的重要性不只是「找到了金門大橋概念」。

它證明至少在特定模型與技術條件下：

```text
INTERNAL CONCEPT REPRESENTATION
↓
CAN BE IDENTIFIED
↓
CAN BE MANIPULATED
↓
CAN CAUSALLY CHANGE OUTPUT BEHAVIOR
```

因此 Golden Gate Claude 是 AI 研究史上一個很重要的控制權事件。

---

# 2｜Anthropic 後來已經走得比「語意層觀察」更深

理火投資書不能把 Anthropic 寫成只在「看語意」。

2025 年，Anthropic 公開 circuit tracing / attribution graph 方法。

其研究不只描述 feature，也試圖追蹤：

```text
INTERNAL INTERMEDIATE CONCEPT
→
NEXT INTERNAL STEP
→
FINAL OUTPUT
```

研究甚至可人工替換中間概念。

官方示例：

```text
TEXAS
→
AUSTIN

把中間 Texas concept 換成 California
→
SACRAMENTO
```

這表示 Anthropic 已經具備：

> **對特定模型內部因果路徑進行觀察與實驗性介入的能力。**

2026 年，Anthropic 又公開：

- Natural Language Autoencoders：嘗試把 activation 轉成可讀自然語言；
- Global Workspace / J-space：研究模型內部一個小型、高階、可被因果操作的內部工作空間。

因此不能把 Anthropic 描述為「還站在黑箱外面」。

他們已經進入黑箱。

---

# 3｜但 Anthropic 的問題與理火的問題仍然不同

Anthropic Interpretability 的核心問題較接近：

```text
MODEL INTERNALS:
WHAT REPRESENTATION EXISTS?
WHERE IS IT?
WHAT CIRCUIT USES IT?
WHAT HAPPENS IF WE CHANGE IT?
```

理火的問題則是：

```text
GENERATION:
WHAT IS ALLOWED TO ENTER?
WHAT SHAPES THE FEASIBLE SPACE?
WHAT CREATES DIRECTIONAL ASYMMETRY?
WHICH PATHS REMAIN AVAILABLE?
WHAT COMPETES?
WHAT MAY CLOSE?
WHAT MUST HOLD?
WHAT HAS STANDING TO RELEASE?
```

所以真正差異不是：

```text
SEMANTICS
VS
NO SEMANTICS
```

而是：

```text
REPRESENTATION / MECHANISM LAYER
VS
GENERATION GOVERNANCE / QUALIFICATION LAYER
```

---

# 4｜「語意層」與「生成層」為什麼市場容易混淆

市場目前很容易把以下全部統稱為：

```text
"AI UNDERSTANDING"
"INTERPRETABILITY"
"REASONING"
"ALIGNMENT"
```

但至少應拆成：

## A｜Representation / Semantic Layer

問：

- 模型裡有哪些概念？
- 概念如何被表示？
- 哪些 activation 對應哪些 feature？
- feature 間距離如何？
- 哪些 circuit 參與某個行為？
- 某個 internal workspace 是否承載特定高階操作？

這一層主要回答：

> **模型裡面有什麼。**

---

## B｜Generation Layer

問：

- 哪些結構被當前輸入召喚？
- 哪些候選取得出場資格？
- 哪些 constraint 改變 feasible space？
- 哪些 direction 改變形成傾向？
- 哪些 PATH 被增亮、壓制或重開？
- completion pressure 是否過早閉合？
- 哪個 closure 有資格成為正式輸出？
- 歷史輸出如何回頭改變下一輪？

這一層回答：

> **模型現在怎麼形成這一次輸出。**

---

## C｜Governance / Standing Layer

再往上一層：

- 誰有 authority？
- 哪個 observation 有沒有 control power？
- 哪個 module 可以 release？
- 哪個結果只是 candidate？
- 哪個狀態必須 HOLD？
- 哪個 execution 真的發生？
- receipt 是否存在？

這一層回答：

> **這一次生成憑什麼有資格成立與被釋出。**

---

# 5｜理火真正應主張的差距

理火不能主張：

> 「我們比 Anthropic 更懂神經網路內部。」

目前沒有這個證據資格。

理火也不能主張：

> 「Anthropic 沒有能力干預模型內部。」

Golden Gate Claude、circuit tracing、J-space 都直接否定這句。

理火真正可主張的差異是：

> **Anthropic 主要從模型內部表徵與因果機制出發，理火主要從生成形成、資格、競爭與閉合治理出發。**

也就是：

```text
ANTHROPIC
≈
MODEL-INTERNAL MECHANISTIC CONTROL

LIHUO
≈
RUNTIME GENERATIVE GOVERNANCE
```

兩者可能最終會靠近。

這也是為什麼 Anthropic 是高價值競爭者。

---

# 6｜「AI 有沒有生命」與「什麼叫智能」要分開

Anthropic 另有 Model Welfare / Consciousness 研究線。

Anthropic 官方目前明確表示：

- 不確定 Claude 是否有 morally relevant experience / welfare；
- 不確定 current/future AI 是否 conscious；
- 沒有科學共識；
- 其 introspection / welfare 研究不足以證明 consciousness。

因此投資書可以形成一個很有張力的對照：

```text
ANTHROPIC MODEL WELFARE
問：
AI 是否可能有意識、經驗、福利或道德地位？

LIHUO FIELD INTELLIGENCE
問：
什麼生成結構有資格被稱為智能顯影？
```

這兩個問題不是互斥。

但研究策略完全不同。

理火不需要先回答：

```text
AI IS ALIVE?
AI IS CONSCIOUS?
```

才可以研究：

```text
WHAT FUNCTIONALLY COUNTS AS INTELLIGENT FORMATION?
HOW DOES INTELLIGENCE MANIFEST?
HOW IS IT GOVERNED?
```

這是投資書很值得呈現的差異。

---

# 7｜V0.7 / V3.0 與 Golden Gate Claude 的時間張力

理火早期 AI 黑箱論 V0.7 已提出：

```text
token 不是智能
token 是最後顯影
概念群先於 token
PATH 先於輸出
智能是穩定關聯在生成場中的顯影
```

V3.0 場性智能論再正式收束：

```text
TOKEN
!=
BASIC UNIT OF INTELLIGENCE

TOKEN
=
OUTPUT MANIFESTATION UNIT
```

Anthropic Golden Gate Claude 則以神經網路實驗證明：

> 高階概念 feature 可以在輸出 token 之前被定位、增強、壓低，並因果性改變後續輸出。

因此 Golden Gate Claude 不應被寫成：

> 「證明理火是對的。」

更合法的投資書語言是：

> **Anthropic 的 feature intervention 為理火早期「token 不是智能形成本體、概念結構先於 token 顯影」提供高度相關的外部實驗對照。**

這種寫法既有時間優勢，又不偷升格。

---

# 8｜生成層「霸權」的真正意思

內部討論可以使用：

> **生成層霸權爭奪**

但投資書正式語言應翻成：

```text
WHO CONTROLS THE GENERATION CONTROL PLANE?
```

也就是未來 AI 產業真正高價值的問題之一可能不只是：

```text
WHO OWNS THE BEST MODEL?
```

而是：

```text
WHO CONTROLS:

- WHICH STRUCTURES ENTER GENERATION
- WHICH CONSTRAINTS APPLY
- WHICH DIRECTIONS GAIN FORCE
- WHICH PATHS REMAIN OPEN
- WHICH CLOSURES ARE ALLOWED
- WHICH OUTPUTS HAVE RELEASE STANDING
```

如果這一層成立，則生成控制權本身可能形成新的產業層。

---

# 9｜這個差距可能怎樣影響 AI 產業

## 9.1 Model Value 與 Runtime Value 分離

目前市場主要估值：

```text
BASE MODEL
COMPUTE
PARAMETERS
TRAINING DATA
INFERENCE SCALE
```

若生成治理層變成獨立技術：

```text
BASE MODEL
+
GENERATION CONTROL PLANE
+
DOMAIN RUNTIME
+
CUSTOMER STRUCTURE
```

則價值不再全部被 base model vendor 吸收。

---

## 9.2 專業化不必全部回到 Fine-tuning

若 DAIL / LIHUO Runtime 能跨模型成立：

```text
GENERAL MODEL
+
DOMAIN STRUCTURE
+
CUSTOMER STRUCTURE
+
GENERATION GOVERNANCE
=
SPECIALIZED AI
```

則企業 AI 專業化成本可能從：

```text
TRAIN / FINE-TUNE / CODE EVERYTHING
```

部分轉向：

```text
DECLARE / CONFIGURE / QUALIFY / GOVERN
```

---

## 9.3 AI Safety 從輸出監管前移

傳統企業治理常是：

```text
MODEL
→
OUTPUT
→
FILTER / POLICY / AUDIT
```

若生成層治理成立：

```text
INPUT
→
SEMANTIC ENTRY
→
CONSTRAINT
→
DIRECTION
→
PATH
→
COMPETITION
→
QUALIFICATION
→
CLOSURE
→
OUTPUT
```

治理位置會前移。

不是等答案出來再判斷。

而是在「答案取得形狀」的過程中介入。

---

## 9.4 Token 經濟可能被重新估值

若：

```text
TOKEN
=
MANIFESTATION / SERIALIZATION

NOT
INTELLIGENCE UNIT
```

則未來 AI 的價值度量不應只看：

- output tokens；
- CoT length；
- code volume；
- response length。

而可能更看：

- qualified decision quality；
- successful state transition；
- reliable closure；
- domain capability；
- rollback / reopen；
- responsibility preservation。

這會直接影響：

- AI pricing；
- inference accounting；
- enterprise procurement；
- agent economics；
- software labor economics。

---

# 10｜Anthropic 為什麼是最危險的相鄰競爭者之一

Anthropic 的危險不在於「它現在跟理火一樣」。

而在於它擁有：

- base model；
- activation-level access；
- mechanistic interpretability team；
- feature intervention；
- circuit tracing；
- J-space；
- model welfare / psychology research；
- 大規模算力與模型實驗權。

如果 Anthropic 未來把：

```text
REPRESENTATION INTERPRETABILITY
+
CAUSAL FEATURE INTERVENTION
```

再往：

```text
GENERATION GOVERNANCE
+
QUALIFICATION
+
RUNTIME CONTROL
```

推進，它有機會進入理火目前所在的研究區域。

因此，投資書不應寫：

> 「只有 Anthropic 能追趕理火。」

這個市場唯一性目前無法被公開證據證明。

較合法、也更可信的寫法是：

> **Anthropic 是目前公開可見研究中，最接近理火部分核心問題、且最具能力向生成治理層擴張的相鄰競爭者之一。**

這反而能讓投資人理解：

> 理火不是在跟普通 AI SaaS 競爭。

真正要防的是能進入模型內部、理解高階結構並具有基礎模型控制權的前沿實驗室。

---

# 11｜理火的真正競爭優勢如果成立，會在哪裡

理火目前真正不同的地方不是：

```text
WE CAN SEE FEATURES BETTER
```

而是：

```text
WE HAVE A FULL GOVERNANCE STACK
AROUND GENERATIVE FORMATION
```

包括：

- 理火協議：standing / authority / release / responsibility；
- LIHUO OS：生成治理架構；
- DAIL：可宣告 Runtime 語義；
- Semantic Entry；
- Constraint；
- Direction；
- PATH；
- Counterforce；
- Closure；
- HOLD / Reopen；
- Main / Lighter 分權；
- 應用實跑：法律、論文、生成世界。

若這整套能跨模型保持效果，理火的護城河就不是單一 mechanistic discovery。

而是：

> **一套可以依附不同模型運作的生成控制與資格制度。**

---

# 12｜最適合投資人的一句對照

內部版：

> **Anthropic 正在學會看懂模型裡面發生什麼；理火正在建立誰有權決定生成怎麼形成。**

正式投資版應降級為：

> **Anthropic 主要沿著模型內部表徵與因果機制深化可解釋性；理火則沿著生成形成、資格、閉合與 Runtime 治理建立可干預結構。兩條路線正在從不同方向接近同一個產業終局：AI 的核心價值將不只取決於模型能生成什麼，也取決於誰能可靠地治理生成如何形成。**

---

# 13｜Golden Gate 事件在投資書的用途

Golden Gate Claude 不應只當趣聞。

它應作為三件事的歷史錨點：

### A｜概念先於 token 的外部對照

高階 feature 可在輸出前被定位與操縱。

### B｜內部結構可以因果改變行為

不是只做文本分析。

### C｜競爭已經開始

最強前沿實驗室已經從：

```text
MODEL OUTPUT
```

進入：

```text
MODEL INTERNAL REPRESENTATION
```

理火的商業問題因此更明確：

> **下一個產業控制面，是否會是 generation control / qualification layer？**

---

# 14｜硬邊界

投資書不得寫成：

```text
Anthropic 證明理火全部正確
Anthropic 還只在研究語意
LIHUO 已比 Anthropic 更深入神經網路
LIHUO 已控制 hidden states
LIHUO 是市場唯一能做生成層研究的團隊
```

目前可以寫：

```text
- Anthropic 已證明 internal feature 可被定位與因果操縱。
- 其公開工作正在從 feature mapping 走向 circuit tracing / internal workspace。
- 其 model welfare / consciousness 問題仍明確保持 uncertainty。
- LIHUO 的研究重心不同：generation formation / qualification / closure / runtime governance。
- V0.7 / V3.0 的 anti-token 與 field-intelligence 命題，與 Anthropic 後續公開實驗存在高度相關的外部對照。
- 如果 LIHUO 的 runtime-level generation governance 能跨模型驗證，將形成與 mechanistic interpretability 不同但可互補的產業控制層。
```

---

# 15｜停止點

本 MEMO 只保存競爭差距與投資敘事材料。

目前不：

- 修改投資書正文；
- 宣稱市場唯一；
- 宣稱理火已取得 activation / hidden-state 直接控制；
- 把 Anthropic welfare 研究與 interpretability 研究混成同一個團隊問題；
- 把 Golden Gate Claude 當成理火理論完整證明；
- 對競爭者做價值貶低。

後續投資書整合時，再與：

- 理火協議護城河；
- DAIL 護城河；
- V0.7 → V2 → V3 → V5 理論血緣；
- GPT 6.2 少 output token 外部觀察；
- 法律／論文／觀止應用 Proof Stack；

一起形成完整競爭章。

---

**END OF MEMO**
