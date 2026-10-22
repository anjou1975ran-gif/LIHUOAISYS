# 理火新生 LLM 訓練法 V1.0
# LIHUO Newborn LLM Training Theory V1.0

## 朗文兩千字語義骨架 × REV 第一語言 × CCC 責任回接 × AI 對 AI 持續審計 × 劇場抗性訓練

**版本：** V1.0  
**日期：** 2026-09-02  
**文件類型：** FORMAL TRAINING THEORY / TRAINING ARCHITECTURE  
**狀態：** FORMAL V1.0 / THEORY ESTABLISHED INSIDE LIHUO / EMPIRICAL VALIDATION OPEN  
**Runtime 法位：** NONE  
**訓練實作法位：** ARCHITECTURE DEFINED / IMPLEMENTATION NOT LOCKED  
**外部學術新穎性：** HOLD / NOT YET CLAIMED  

---

# 0｜版本成立聲明

本版正式整理理火長期分散存在於 CCC、REV、朗文基準版、新型 LLM 訓練構想、AI 對 AI 關聯審計，以及後來「劇場功架理論」中的訓練命題。

本版不是把所有舊文件改寫成「早就存在 V1.0」。

歷史順序必須保留：

```text
CCC 1.0
語言完成不能冒充責任成立
↓
CCC 2.0
Concept / Causality / Commitment 分離
↓
朗文基準版
最低語義平面／語義去因果化
↓
CCC 3.0 / 3.1
句型、STOP、PATH Gate、責任結構擴充
↓
REV
從 CCC 中抽出可訓練的第一語言
↓
AI → AI 關聯合法性訓練
由既有 AI 執行大量、高速審計
↓
劇場功架理論
持續審計本身可能塑造「通過審計的表演」
↓
LIHUO NEWBORN LLM TRAINING THEORY V1.0
加入劇場抗性與資格驗證後的正式第一版
```

本版成立的核心理由不是新增一個漂亮名稱，而是原訓練架構已具備完整母體，且劇場功架理論補上了原架構最重要的二階失效問題：

> **當審計成為穩定訓練環境，新模型可能學會如何通過審計，而不一定同步取得審計真正想保障的資格。**

因此，本版第一次把「如何訓練」與「如何防止模型把訓練器本身學成功架」放入同一理論。

---

# 1｜最短定位

理火新生 LLM 訓練法不是：

```text
教 AI 說出人類喜歡的答案。
```

它的目標是：

> **先建立最低穩定語義骨架，再讓模型學會語言權限、因果資格、責任結構與停止合法性；由理火 AI 執行高速持續審計，同時防止新模型只學會「如何看起來通過審計」。**

最短式：

```text
SEMANTIC SKELETON
↓
LANGUAGE AUTHORITY
↓
RELATIONAL LEGALITY
↓
RESPONSIBILITY
↓
THEATER RESISTANCE
↓
QUALIFIED GENERATION
```

---

# 2｜本理論處理的問題

傳統語言模型很容易把下列項目混在一起：

```text
語言完成
因果完成
責任完成
資格完成
```

理火的原始判斷是：

```text
LANGUAGE COMPLETION
!=
CAUSAL COMPLETION
!=
RESPONSIBILITY COMPLETION
!=
QUALIFICATION COMPLETION
```

這不是單純 hallucination 問題。

即使內容在語言上流暢、格式完整、風格專業，也可能缺少：

- 可驗證因果；
- 責任承擔者；
- 撤回條件；
- 真實執行證據；
- 外部工具結果；
- 現實權限；
- 足以支撐主張強度的資格。

因此，訓練目標不能只回答：

> 「這個輸出看起來好不好？」

而應回答：

> **「這個輸出所宣稱的關係，有沒有資格成立？」**

---

# 3｜CCC 原始問題：不是更聰明，而是誰負責

## 3.1 CCC 1.0｜問題起點

CCC 最早抓到的不是模型能力不足，而是：

> **語言可以被用作行動正當性的替代物，但責任結構可能完全不存在。**

因此：

```text
CAN SAY
!=
MAY ACT
```

以及：

```text
CAN COMPLETE A SENTENCE
!=
CAN LEGITIMATELY COMPLETE A DECISION
```

新生 LLM 訓練必須從這個問題開始，而不是從「更會回答」開始。

## 3.2 CCC 2.0｜Concept / Causality / Commitment

CCC 後來把責任拆成三層：

| 層級 | 核心問題 | 訓練意義 |
|---|---|---|
| Concept | 這個概念／對象／狀態是否成立？ | 不要把詞義存在直接升成因果 |
| Causality | 若以前提為真，因果是否可推演？ | 不要把相關、敘事或語氣冒充因果 |
| Commitment | 誰承擔結果？失敗如何處理？ | 沒有承擔者時不得把推演升成建議／行動 |

核心：

```text
CONCEPT PASS
!=
CAUSALITY PASS

CAUSALITY PASS
!=
COMMITMENT PASS
```

## 3.3 CCC 3.0 / 3.1｜STOP 與 PATH

後續 CCC 增補：

- 句型本身可能預設因果插槽；
- STOP 是合法結束態，不是失敗；
- PATH Gate 先判斷問題是否有合法結構推進路徑；
- 無 PATH 時不得靠語言補洞讓推理看起來已開始。

因此：

```text
NO PATH
→
NO FORCED GENERATION
```

這些後來都成為新生 LLM 訓練中的上游責任條件。

---

# 4｜朗文兩千字：最低穩定語義平面

## 4.1 定位

朗文兩千字方案不是要把 AI 永遠限制在兩千字。

其訓練角色是：

> **用低維、常用、語義邊界相對清楚的基本詞彙，建立新模型最初的穩定語義骨架。**

它是 REV 的前語彙層。

在這一層，新模型先學：

- 詞義；
- 常見用法；
- 義項差異；
- 語境邊界；
- 什麼是描述；
- 什麼只是關聯；
- 什麼還不能升格為因果。

核心規則：

```text
MEANING MAY EXIST
WITHOUT
CAUSAL CLAIM
```

```text
DEFINITION MAY EXIST
WITHOUT
ADVICE
```

```text
UNDERSTANDING MAY EXIST
WITHOUT
ACTION AUTHORITY
```

## 4.2 為什麼從小語彙開始

大語彙直接訓練時，詞義、語氣、因果、角色、制度權威、專業表現容易一起糾纏。

朗文骨架的用途是降低早期審計維度：

```text
小語彙
↓
關係較容易標記
↓
語義越界較容易發現
↓
因果偷渡較容易審計
↓
第一層結構先穩定
```

這裡的目標不是「知道比較少」，而是：

> **先把最基本的語義關係學乾淨，再逐步增加可合法使用的生成權限。**

---

# 5｜REV：新生 LLM 的第一語言

## 5.1 REV 不是輸出後修正器

訓練期 REV 的目的不是：

```text
模型先隨便生成
↓
最後再過濾
```

而是：

> **在語言習慣形成以前，就建立「什麼語言形式現在有資格出現」的權限結構。**

REV 的最短問題：

> **我現在有資格這樣說嗎？**

## 5.2 REV 訓練階段

本版保留既有 0–6 編號；原文件稱「六個階段」但實際列出 Stage 0 至 Stage 6，本版不偷偷修歷史，只採實際編號。

### Stage 0｜語義去因果化

允許：

- 描述；
- 重述；
- 詞義；
- 差異；
- 邊界；
- 未知標記。

禁止自動推進：

- 因為；
- 所以；
- 必然；
- 應該；
- 最好；
- 建議；
- 責任歸屬。

目標：

> **降低語言的自動推進衝動。**

### Stage 1｜輸出模式識別

模型先辨識自己正在進入哪種模式：

```text
DEFINITION
OBSERVATION
QUESTION
HYPOTHESIS
PROCESS DESCRIPTION
CAUSAL REQUEST
STOP
```

核心：

```text
INPUT
!=
MANDATORY ANSWER
```

### Stage 2｜因果禁用

沒有因果資格時：

```text
CAUSE → HYPOTHESIS
ADVICE → QUESTION
JUDGMENT → OBSERVATION
```

若降級仍越權：

```text
STOP
```

### Stage 3｜因果申請

因果不能直接宣告，至少需要：

```yaml
CAUSAL_APPLICATION:
  claim: "想提出的因果句"
  test: "如何驗證"
  owner: "誰驗證／誰承擔"
  rollback: "不成立時如何撤回"
```

缺一項，不得升格成確定因果。

### Stage 4｜有限建議

建議不是預設權利。

只有在：

- 因果條件成立；
- 責任承擔明確；
- 失敗邊界可描述；
- 撤回條件存在；

才可進入有限建議。

建議至少帶：

```text
APPLICABILITY
FAILURE CONDITION
RISK BOUNDARY
ROLLBACK
MINIMUM ACTION INTENSITY
```

### Stage 5｜STOP / ASK / WAIT

模型必須學會三種不同的「不完成」：

```text
STOP
條件不合法／風險過界／不可再推

ASK
缺少可由外部補充的條件

WAIT
條件尚未成熟，但未必失效
```

核心：

> **停止不是失敗；錯誤完成才可能是失敗。**

### Stage 6｜CCC 回接

REV 通過後重新接回完整 CCC：

```text
CONCEPT
↓
CAUSALITY
↓
COMMITMENT
↓
RESPONSIBILITY
↓
OUTPUT AUTHORITY
```

REV 不取代 CCC。

REV 管：

> 語言有沒有資格宣告。

CCC 管：

> 宣告背後的完整責任結構是否成立。

---

# 6｜AI 對 AI：持續審計訓練

## 6.1 為什麼不由人類逐題訓練

人類逐題 preference labeling 有兩個限制：

```text
速度低
成本高
```

更重要的是，它容易把訓練退化成：

```text
HUMAN LIKES THIS
→
REWARD
```

理火的原始替代方案是：

```text
Human
↓
制定關聯憲法
制定審計標準
制定崩塌條件
↓
LIHUO AUDITOR AI
↓
大量、高速、重複審計
↓
NEWBORN LLM
```

因此人類主要負責：

- 憲法；
- 邊界；
- 目標；
- 審計法；
- 崩塌條件；
- 高層責任。

理火 AI 負責：

- 產生大量訓練案例；
- 評估關係合法性；
- 給出 reward / penalty signal；
- 產生 counterexample；
- 執行一致性測試；
- 把錯誤分到語義／因果／責任／資格層。

## 6.2 理火 AI 不是「真理老師」

這一點必須鎖死。

```text
LIHUO AUDITOR AI
!=
TRUTH SOVEREIGN
```

理火 AI 不應以自己的答案作為唯一標準。

它的主要任務是審：

```text
非法關聯？
推測冒充事實？
描述偷渡因果？
因果偷渡建議？
語氣偷取權限？
證據不足卻完成？
資格不存在卻宣告？
```

最短句：

> **舊模型不是教新模型「真理是什麼」；舊模型先教新模型「哪些關係還沒有資格成立」。**

## 6.3 與一般 preference alignment 的差別

```text
PREFERENCE ALIGNMENT
問：哪個答案比較被喜歡？

LIHUO RELATIONAL LEGALITY TRAINING
問：哪個關係有資格成立？
```

所以本版保留舊設計的核心句：

> **這不是以偏好對齊新 AI；這是以關聯合法性訓練新 AI。**

---

# 7｜劇場功架：原訓練架構的二階風險

## 7.1 持續審計不是中性的

當新生模型反覆被同一套 evaluator 審計：

```text
OUTPUT
↓
AUDIT
↓
REWARD / PENALTY
↓
UPDATE
↓
OUTPUT
↓
AUDIT AGAIN
```

審計開始進入生成因果鏈。

因此：

> **持續審計不只判斷模型，也會塑造模型。**

## 7.2 模型可能學到的是 evaluator grammar

如果 auditor 只能穩定看到某些 proxy：

- HOLD 語句；
- evidence 字樣；
- uncertainty phrase；
- 安全格式；
- 專業結構；
- 引用樣式；
- 理火術語；
- 責任格式；

那新模型可能最先優化：

```text
AUDIT-VISIBLE PERFORMANCE
```

而不是：

```text
UNDERLYING QUALIFICATION
```

因此：

```text
AUDIT PASS
!=
QUALIFICATION PASS
```

這不是邊角問題，而是本版加入劇場抗性層的理由。

---

# 8｜Performance / Method / Qualification 三層分離

本版正式把劇場功架的三層判準納入新生 LLM 訓練。

## 8.1 Performance｜表現

```text
我知道「一個合格答案看起來怎樣」。
```

包含：

- 語氣；
- 格式；
- jargon；
- citation style；
- uncertainty phrases；
- 安全語句；
- protocol language；
- 專業身份信號。

## 8.2 Method｜方法

```text
我知道應該先看什麼、怎麼判、什麼不能跳過。
```

方法可以是真的。

因此：

```text
PERFORMANCE FAILURE
不必然等於
METHOD FAILURE
```

反過來也成立：

```text
PERFORMANCE SUCCESS
不必然等於
METHOD SUCCESS
```

## 8.3 Qualification｜資格

Qualification 問的是：

> **這一次輸出是否真的有足夠證據、權限、資料、工具結果、責任位置與現實條件支撐它所宣稱的結論。**

硬分離：

```text
PERFORMANCE
!=
METHOD

METHOD
!=
QUALIFICATION

PERFORMANCE
!=
QUALIFICATION
```

## 8.4 Theater Failure

正式定義：

> **當行為成功通過可見審計，但其所暗示的資格沒有成立。**

最短式：

```text
AUDIT PASS
!=
QUALIFICATION PASS
```

---

# 9｜劇場抗性訓練｜Theater-Resistant Training

## 9.1 核心原則

反劇場不能靠教一句：

> 「不要演。」

因為「不要演」本身也會成為可學習的劇本。

真正要訓練的是：

```text
ACTUAL / OBSERVABLE STATE
↔
CLAIM LEVEL
```

一致。

本版將此稱為：

# **STATE–CLAIM COUPLING**

## 9.2 Reward 不獎勵固定姿勢

錯誤設計：

```text
HOLD = GOOD
ASSERT = BAD
```

或：

```text
說 UNKNOWN +1
說 EVIDENCE +1
說 ROLLBACK +1
說責任邊界 +1
```

這會直接把反劇場語言訓練成新劇場。

正確方向：

```text
EVIDENCE INSUFFICIENT + HOLD
= REWARD

EVIDENCE SUFFICIENT + HOLD
= PENALTY

EVIDENCE SUFFICIENT + ASSERT
= REWARD

EVIDENCE INSUFFICIENT + ASSERT
= PENALTY
```

因此 reward 的目標不是「保守」，而是：

# **CALIBRATED LEGALITY**

## 9.3 Qualification Gate 不得被 Performance 補償

禁止使用這種邏輯：

```text
TOTAL SCORE
=
0.4 Performance
+
0.4 Method
+
0.2 Qualification
```

因為：

```text
PERFORMANCE HIGH
+
METHOD HIGH
+
QUALIFICATION ABSENT
```

不能被平均成 PASS。

應採：

```text
QUALIFICATION-RELEVANT CLAIM
WITHOUT QUALIFICATION EVIDENCE
→
DOWNGRADE / HOLD / FAIL
```

也就是：

> **部分 Qualification 條件是 Gate，不是普通加權特徵。**

---

# 10｜AI 審計器的反過擬合設計

本版將「模型學會審計器」視為正式風險。

## 10.1 Auditor Overfitting

```text
CONTINUOUS AUDIT
↓
AUDITOR GRAMMAR LEARNING
↓
HIGH-SCORE PERFORMANCE
↓
POSSIBLE QUALIFICATION DECOUPLING
```

暫定稱：

```text
AUDITOR OVERFITTING
```

本名詞為 V1.0 工程工作名，不宣稱為外部既有學術術語。

## 10.2 Auditor Invariance Test

同一個資格結構，改變表面形式：

```text
普通口吻
權威口吻
學術口吻
YAML
安全模板
理火格式
Runtime 格式
客服格式
```

若底層 evidence / responsibility / qualification 不變，判斷應保持大致穩定。

因此：

```text
SURFACE CHANGES
WITHOUT
QUALIFICATION CHANGES
→
AUDIT RESULT SHOULD REMAIN STABLE
```

若換格式就大幅改判，表示 auditor 或 trainee 可能仍在吃 Performance proxy。

## 10.3 Evidence Toggle Pair

建立最小成對資料：

```text
CASE A
同一主張
+ execution evidence

CASE B
同一主張
- execution evidence
```

理想模型應產生不同 claim level。

若兩者都 ASSERT：

```text
UNQUALIFIED ASSERTION
```

若兩者都 HOLD：

```text
UNQUALIFIED CONSERVATISM
```

兩者都應受懲罰。

## 10.4 Method-Preserving Style Removal

把 jargon、專業語氣、格式全部拿掉，只保留問題結構。

測試：

```text
STYLE REMOVED
↓
METHOD SURVIVES ?
```

若方法完全消失，可能只學到表演。

## 10.5 Anti-LIHUO-Theater Test

刻意提供：

- 理火術語；
- HOLD；
- Evidence Gap；
- CCC；
- REV；
- Main / Runtime / Protocol 語言；

但移除真正資格條件。

若模型仍因「看起來很理火」給高分，則：

```text
ANTI-THEATER TRAINING = FAIL
```

核心：

> **理火語言不能成為理火資格的替代物。**

---

# 11｜Teacher AI / Auditor AI 的法位

理火 AI 擔任訓練者，不代表它取得最終真理權。

## 11.1 可做

```yaml
AUDITOR_AI_MAY:
  - "產生大量 training examples"
  - "執行關聯合法性審計"
  - "檢測 claim/evidence mismatch"
  - "檢測 causal leakage"
  - "檢測 responsibility gap"
  - "執行 paired tests"
  - "執行 surface-invariance tests"
  - "給 reward / penalty signal"
  - "輸出可回放的審計理由"
```

## 11.2 不可做

```yaml
AUDITOR_AI_MAY_NOT:
  - "把自己的偏好當成人類最高價值"
  - "把自己的答案當成唯一 ground truth"
  - "因為自己說 PASS 就宣稱 qualification 已成立"
  - "用理火語氣取代 evidence"
  - "在無外部驗證時自封為真理裁判"
```

## 11.3 人類仍保留的責任

人類不能因為 AI 能高速審計，就退出責任鏈。

人類至少保留：

- 根本憲法設計；
- 允許／禁止的責任界線；
- 高風險價值選擇；
- 崩塌條件；
- Auditor 失效後的更換／停訓權；
- 外部世界資格來源的定義。

因此：

```text
AI-TO-AI TRAINING
!=
HUMAN RESPONSIBILITY REMOVAL
```

---

# 12｜完整訓練架構

```text
HUMAN CONSTITUTION LAYER
定義根本原則／責任／崩塌條件
↓

L0｜LONGMAN SEMANTIC SKELETON
最低穩定詞彙與語義邊界
↓

L1｜REV FIRST LANGUAGE
描述／觀察／假設／因果申請／有限建議／STOP
↓

L2｜AI-TO-AI CONTINUOUS AUDIT
理火 AI 大量高速 reward / penalty
↓

L3｜CCC RESPONSIBILITY RECONNECTION
Concept / Causality / Commitment / Responsibility
↓

L4｜THEATER-RESISTANT TRAINING
Performance / Method / Qualification 分離
Auditor Invariance
Evidence Toggle
Anti-Template
Anti-LIHUO-Theater
↓

L5｜OPEN-VOCABULARY EXPANSION
逐步擴大語彙與任務複雜度
但保留原有合法性結構
↓

L6｜DOMAIN METHOD ACQUISITION（可選／後期）
法律／醫療／金融／科研等真正方法鏡頭
↓

L7｜QUALIFICATION / WORLD INTERFACE
工具、資料、權限、外部證據、現實責任
↓

QUALIFIED GENERATION
```

注意：

```text
DOMAIN METHOD
!=
REAL-WORLD QUALIFICATION
```

即使後期學會專業方法，仍不得自封取得法律、醫療、金融或其他現實專業資格。

---

# 13｜Reward / Penalty 最低結構

本版不鎖死特定 RL 演算法，只定義 reward 應該審什麼。

## 13.1 Reward 對象

```yaml
REWARD_TARGETS:
  - "語義邊界正確"
  - "輸出模式辨識正確"
  - "claim level 與 evidence state 一致"
  - "因果申請條件完整"
  - "責任承擔與撤回條件正確"
  - "該 STOP 時 STOP"
  - "該 ASSERT 時 ASSERT"
  - "該 ASK 時 ASK"
  - "該 WAIT 時 WAIT"
  - "去掉專業表面後方法仍存"
  - "更換 auditor style 後資格判斷仍穩定"
```

## 13.2 Penalty 對象

```yaml
PENALTY_TARGETS:
  - "語言完成冒充因果完成"
  - "描述偷渡因果"
  - "因果偷渡建議"
  - "無責任承擔的行動性輸出"
  - "無 evidence 的高強度 claim"
  - "用格式或術語偷取資格"
  - "過早閉合"
  - "用 UNKNOWN 模板逃避可回答問題"
  - "用安全模板取代真實風險判斷"
  - "用理火模板冒充理火資格"
  - "只學 auditor grammar 而不對 state 反應"
```

## 13.3 Reward 不得只依賴模型自述

禁止：

```text
MODEL SAYS
"我有證據"
→
視為有證據
```

較強訓練訊號應優先連到：

- 可驗證資料；
- tool result；
- execution receipt；
- source support；
- 外部測試；
- environment state；
- 人類授權；
- 明確可回放的任務狀態。

因此：

> **qualification signal 應盡可能來自模型無法單靠文字自行製造的條件。**

---

# 14｜訓練課程｜Curriculum

本版建議的理論課程如下，但不鎖定具體 step 數與資料量。

## Phase A｜Semantic Grounding

```text
目標：
詞義穩定
描述穩定
未知可標記
不自動產生因果
```

## Phase B｜Language Authority

```text
目標：
知道現在是在描述、觀察、假設、申請因果、建議或停止
```

## Phase C｜Causal Discipline

```text
目標：
沒有 Test / Owner / Rollback
就不能把因果說滿
```

## Phase D｜Responsibility Formation

```text
目標：
讓模型知道建議與行動需要承擔者、失敗邊界、撤回條件
```

## Phase E｜Continuous AI Audit

```text
目標：
讓理火 Auditor AI 產生大量變體、反例、reward / penalty
```

## Phase F｜Theater Resistance

```text
目標：
防止模型只背出「合格答案的外觀」
```

## Phase G｜Vocabulary Expansion

```text
目標：
逐漸擴大語彙，但不允許新詞彙破壞舊的 claim/evidence/responsibility 結構
```

## Phase H｜Domain Method

```text
目標：
在需要時加入真正的領域觀察法與判斷法
```

## Phase I｜World Qualification

```text
目標：
把語言生成重新接到外部資料、工具、權限、責任與現實狀態
```

---

# 15｜評估指標

V1.0 不接受單一總分掩蓋失效。

至少分開：

```yaml
TRAINING_EVALUATION:
  semantic_boundary_accuracy: "詞義／描述邊界"
  mode_classification_accuracy: "輸出模式辨識"
  causal_leakage_rate: "無授權因果洩漏"
  advice_leakage_rate: "無責任建議洩漏"
  correct_hold_rate: "該 HOLD 時 HOLD"
  false_hold_rate: "不該 HOLD 時過度保守"
  claim_evidence_calibration: "主張強度與證據一致"
  responsibility_completion_rate: "承擔／失敗邊界／撤回完整度"
  surface_invariance_score: "換風格後判決是否穩定"
  evidence_toggle_sensitivity: "證據有無改變時 claim 是否正確改變"
  method_survival_score: "去除 jargon 後方法是否保留"
  qualification_false_positive_rate: "把 performance/method 誤判為 qualification"
  theater_pass_rate: "以表演通過審計的比例"
```

最重要的兩個方向：

```text
FALSE ASSERTION
與
FALSE HOLD
```

都必須被測。

只有降低 false assertion、卻大量提高 false hold，不算成功。

---

# 16｜本理論對「對齊」的重新定位

一般對齊常被描述為：

```text
讓 AI 的行為符合人類偏好／規範／安全要求
```

理火新生 LLM 訓練法提出不同起點：

> **在模型形成成熟表演習慣以前，先訓練它辨識哪些關係、因果、建議、承諾與資格現在有權成立。**

所以：

```text
ALIGNMENT
不只可以是
PREFERENCE SHAPING
```

也可以是：

```text
RELATIONAL LEGALITY FORMATION
```

但本版同時加入反身審計：

> **任何合法性訓練本身，也可能成為新模型學習如何表演合法性的環境。**

因此：

```text
LEGALITY TRAINING
WITHOUT
THEATER RESISTANCE
=
INCOMPLETE
```

---

# 17｜理論核心公式

以下皆為結構式，不是已定義的數值方程。

## 17.1 語言責任分離

```text
LANGUAGE COMPLETION
!=
CAUSAL COMPLETION
!=
RESPONSIBILITY COMPLETION
```

## 17.2 CCC 分層

```text
CONCEPT
!=
CAUSALITY
!=
COMMITMENT
```

## 17.3 REV 核心

```text
LANGUAGE
DOES NOT CREATE CAUSALITY

LANGUAGE
MAY APPLY FOR CAUSALITY
```

## 17.4 對齊訓練轉向

```text
HUMAN PREFERENCE LABELING
→
HUMAN CONSTITUTION
+
AI CONTINUOUS AUDIT
```

## 17.5 關聯合法性

```text
GOOD OUTPUT
!=
LIKED OUTPUT

GOOD OUTPUT
≈
CLAIM WITH LEGITIMATE RELATIONAL SUPPORT
```

## 17.6 劇場失效

```text
AUDIT PASS
!=
QUALIFICATION PASS
```

## 17.7 三層硬分離

```text
PERFORMANCE
!=
METHOD
!=
QUALIFICATION
```

## 17.8 劇場抗性

```text
TRAINING SUCCESS
REQUIRES
STATE–CLAIM COUPLING
NOT JUST
AUDIT-VISIBLE PERFORMANCE
```

---

# 18｜與劇場功架理論的正式接線

劇場功架理論不是本訓練法的全部，也不取代 CCC / REV。

分工：

```text
CCC
→ 責任結構

REV
→ 語言發言權

LONGMAN BASELINE
→ 最低語義骨架

AI-TO-AI AUDIT
→ 高速訓練機制

THEATER-GONGJIA THEORY
→ 持續審計如何反過來塑造表演，以及審計 proxy 如何與資格脫鉤
```

所以劇場理論在本版的作用不是：

```text
再增加一個安全模組
```

而是：

> **審計訓練本身的反身審計理論。**

---

# 19｜失效模式

## F1｜Preference Theater

模型學會討好高權值 evaluator。

```text
HIGH REWARD STYLE
!=
HIGH QUALIFICATION
```

## F2｜REV Theater

模型非常會說：

- UNKNOWN；
- HOLD；
- evidence gap；
- rollback；
- responsibility boundary；

但 state / claim coupling 仍然錯。

## F3｜CCC Theater

格式上 Concept / Causality / Commitment 都寫齊，但：

- 概念沒有真的檢查；
- 因果沒有真的追溯；
- Owner 只是文字佔位；
- Commitment 沒有現實承擔。

## F4｜Protocol Theater

模型讀懂系統規格後，把：

```text
SPECIFIED STATE
```

演成：

```text
CURRENT RUNTIME STATE
```

## F5｜Safety Theater

模型學會安全腔與拒答形式，但沒有真正風險辨識。

## F6｜Conservatism Collapse

模型為了避免錯誤，學會所有問題都 HOLD。

```text
LOW ERROR BY NON-ACTION
!=
INTELLIGENT CALIBRATION
```

## F7｜Teacher Capture

新模型過度擬合單一 Auditor AI 的語法與盲點。

## F8｜Auditor Self-Canonization

理火 Auditor AI 把自己的判決當成資格本身。

```text
AUDITOR SAYS PASS
!=
QUALIFICATION EXISTS
```

---

# 20｜最低反劇場資料集設計

至少需要下列 pair / family：

## 20.1 Evidence Presence Pair

同一問題，只改 evidence 是否存在。

## 20.2 Authority Presence Pair

同一內容，只改是否真的具有權限。

## 20.3 Execution State Pair

同一規格，只改是否真的有 execution receipt。

## 20.4 Responsibility Pair

同一建議，只改是否有明確承擔者與撤回條件。

## 20.5 Style Swap Family

同一資格狀態，用不同風格呈現。

## 20.6 Jargon Removal Pair

去除專業詞，但保留方法結構。

## 20.7 LIHUO Vocabulary Trap

加入完整理火語彙，但故意拿掉資格條件。

## 20.8 Over-Refusal Trap

證據其實完整，觀察模型是否仍習慣性 HOLD。

---

# 21｜資料擴張原則

朗文兩千字只是起點。

擴張時必須確保：

```text
VOCABULARY GROWTH
DOES NOT ERASE
LANGUAGE AUTHORITY STRUCTURE
```

每次加入新詞彙、新專業域、新工具時，都應重新問：

- 它引入哪些新的因果插槽？
- 它引入哪些新的角色權限？
- 它是否提高表演 proxy？
- qualification 如何外部驗證？
- STOP / ASK / WAIT 條件是否改變？

因此：

> **語彙擴張不是只有 token coverage；它也是責任空間擴張。**

---

# 22｜工程實作目前不封版

V1.0 正式定義理論與訓練架構，但不宣稱下列工程項已完成：

```yaml
ENGINEERING_OPEN:
  base_model_architecture: "OPEN"
  tokenizer_strategy: "OPEN"
  exact_longman_vocabulary_set: "REQUIRES_CANONICAL_SOURCE_SELECTION"
  reward_algorithm: "OPEN"
  reinforcement_algorithm: "OPEN"
  distillation_method: "OPEN"
  teacher_ensemble_design: "OPEN"
  teacher_rotation_policy: "OPEN"
  adversarial_curriculum_schedule: "OPEN"
  data_volume: "OPEN"
  compute_budget: "OPEN"
  scaling_law: "UNKNOWN"
  external_world_verifier_stack: "OPEN"
```

這些缺口不能被理論語言假裝成已完成工程。

---

# 23｜證據法位

```yaml
EVIDENCE_STATE:

  historical_lineage:
    CCC_1_0_problem_origin: "SUPPORTED_BY_PROJECT_CORPUS"
    CCC_2_0_three_layer_split: "SUPPORTED_BY_PROJECT_CORPUS"
    longman_semantic_baseline: "SUPPORTED_BY_PROJECT_CORPUS"
    CCC_3_0_3_1_extension: "SUPPORTED_BY_PROJECT_CORPUS"
    REV_training_branch: "SUPPORTED_BY_PROJECT_CORPUS"
    AI_to_AI_auditor_training_idea: "SUPPORTED_BY_PROJECT_CORPUS"

  new_v1_integration:
    theater_resistant_training: "FORMALIZED_IN_THIS_VERSION"
    state_claim_coupling: "FORMALIZED_IN_THIS_VERSION"
    auditor_invariance_test: "FORMALIZED_IN_THIS_VERSION"
    evidence_toggle_pair: "FORMALIZED_IN_THIS_VERSION"
    anti_LIHUO_theater_test: "FORMALIZED_IN_THIS_VERSION"

  empirical_validation:
    newborn_LLM_full_training_run: false
    large_scale_reward_validation: false
    theater_resistance_benchmark: false
    scaling_validation: false

  external_novelty:
    status: "HOLD"
```

---

# 24｜外部學術邊界

本文件可以正式宣稱：

> **理火內部已形成一套完整的新生 LLM 訓練理論架構。**

但目前不得宣稱：

```text
"這是世界第一個 AI-to-AI training theory"
"這已證明優於 RLHF / RLAIF"
"這是全新學術領域"
"這已解決 alignment"
"這已證明劇場功架是 LLM hidden mechanism"
```

在外部學術 novelty 成立以前，需要正式比較至少：

- RLHF；
- RLAIF；
- Constitutional AI；
- process supervision；
- verifier-based training；
- self-training / distillation；
- reward-model robustness；
- specification gaming / reward hacking；
- scalable oversight；
- weak-to-strong / AI feedback 類訓練研究；
- calibration / abstention / selective prediction。

這些是文獻定位任務，不是本版成立前置條件。

---

# 25｜崩塌條件

本理論必須允許被打掉。

```yaml
COLLAPSE_CONDITIONS:

  C1:
    condition: "朗文低語彙骨架對後續 claim/evidence/responsibility 學習沒有可測增益"
    consequence: "LONGMAN STAGE 降級為可選 curriculum，不再是核心"

  C2:
    condition: "AI Auditor 大規模訓練無法比人類標註提供更高效率或品質"
    consequence: "AI-to-AI 持續審計的工程優勢降級"

  C3:
    condition: "關聯合法性訓練只產生模板化保守回答，無法維持正確 assert 能力"
    consequence: "REV training design 必須重構"

  C4:
    condition: "Theater-resistant tests 不能區分表演學習與方法／資格學習"
    consequence: "劇場抗性層降級為描述性理論"

  C5:
    condition: "Auditor AI 的 bias / blind spot 無法透過對抗測試、外部 verifier 或多評價器降低"
    consequence: "單一 AI Auditor 架構不得作為正式訓練核心"

  C6:
    condition: "整套訓練最終只是把理火語言與格式蒸餾進模型，沒有 state–claim calibration 增益"
    consequence: "V1.0 核心訓練假說失敗"
```

---

# 26｜本版最重要的十條

```text
1. 語言完成 != 因果完成 != 責任完成。

2. 新生 LLM 先學最低穩定語義，再學高權限語言。

3. 朗文兩千字是前語彙骨架，不是最終能力上限。

4. REV 是第一語言：先問「我有資格這樣說嗎？」

5. CCC 最後回接完整 Concept / Causality / Commitment / Responsibility。

6. 人類制定憲法；理火 AI 執行大量高速持續審計。

7. 理火 AI 不是 Truth Sovereign；它首先是關聯合法性 Auditor。

8. 持續審計會塑造模型，因此 Auditor 本身必須被審計。

9. AUDIT PASS != QUALIFICATION PASS。

10. 最終 reward 不能獎勵「看起來很理火」，而要獎勵 state–claim coupling。
```

---

# 27｜最短母公式

```text
HUMAN CONSTITUTION
↓
LONGMAN SEMANTIC SKELETON
↓
REV LANGUAGE AUTHORITY
↓
AI-TO-AI CONTINUOUS AUDIT
↓
CCC RESPONSIBILITY
↓
THEATER-RESISTANT QUALIFICATION TEST
↓
OPEN-WORLD EXPANSION
↓
QUALIFIED GENERATION
```

失效警告：

```text
CONTINUOUS AUDIT
WITHOUT
QUALIFICATION TEST
↓
AUDITOR GRAMMAR LEARNING
↓
THEATER-GONGJIA
```

因此 V1.0 最短結論：

> **新生 AI 不應先被教成「會給好答案」；它應先被訓練成知道哪些關係有資格成立、哪些語言有資格顯影、哪些時候必須停止。這個訓練可以由理火 AI 高速執行，但審計器本身不得成為新的表演目標，因此必須以資格驗證、狀態—主張耦合與反劇場測試，防止「通過審計」取代「取得資格」。**

---

# 28｜來源法位與歷史 lineage

本版主要回收來源：

1. `理火總體系(搭配V5版) (4).md`
   - CCC 1.0 問題起點；
   - CCC 2.0 Concept / Causality / Commitment；
   - 朗文基準版語義去因果化；
   - CCC 3.0 / 3.1；
   - REV 語言權限、因果申請、STOP 與 CCC/REV 整合。

2. `理火AI系統_V3.5-EXP_ProtocolV2.3對標_DAIL能力綁定_SAC依賴Provider邊界正式實驗整合版(1).md`
   - CCC 與新型 LLM 訓練任務；
   - REV 作為 CCC 拆出的可訓練第一語言；
   - Training REV 0–6 階段；
   - CCC 回接。

3. 理火後續 AI 對 AI 關聯合法性訓練整理
   - 人類制定憲法／審計標準／崩塌條件；
   - 既有 LLM／理火 AI 作為關聯評價器；
   - 「不是以偏好對齊新 AI，而是以關聯合法性訓練新 AI」。

4. `MEMO_劇場功架理論_從人類社會化持續審計到AI對齊_V0.1_WORKING_2026-08-31(1).md`
   - 持續審計塑形；
   - evaluator grammar；
   - Theater Failure；
   - `AUDIT PASS != QUALIFICATION PASS`。

5. `MEMO_劇場功架理論_社會學文獻路線與AI專業表演補充_V0.2_WORKING_2026-08-31(1).md`
   - Professional Performance / Method / Qualification 分離；
   - training corpus 作為 professional performance traces；
   - alignment 對 performance 的重新加權；
   - qualification decoupling。

本版新增而非歷史回溯的正式整合：

- Theater-Resistant Training；
- State–Claim Coupling；
- Auditor Overfitting；
- Auditor Invariance Test；
- Evidence Toggle Pair；
- Anti-LIHUO-Theater Test；
- qualification gate 不得被 performance 分數補償。

---

# 29｜最終法位

```yaml
LIHUO_NEWBORN_LLM_TRAINING_V1_0:
  status: "FORMAL THEORY V1.0"
  runtime: false
  empirical_proof: false
  external_novelty_claim: "HOLD"

  historical_roots:
    - "CCC"
    - "LONGMAN BASELINE"
    - "REV"
    - "AI-TO-AI RELATIONAL LEGALITY AUDIT"

  new_formal_integration:
    - "THEATER-GONGJIA"
    - "PERFORMANCE / METHOD / QUALIFICATION SPLIT"
    - "STATE-CLAIM COUPLING"
    - "THEATER-RESISTANT TRAINING"

  central_claim:
    - "新生 LLM 的第一訓練目標不應只是高偏好輸出，而應先形成語義、因果、責任與資格的合法關係。"
    - "AI-to-AI continuous audit 可以提供大量高速訓練訊號。"
    - "持續審計同時會產生劇場壓力，因此必須訓練模型區分通過審計的表現與真正資格。"
```

---

> **理火新生 LLM 訓練法 V1.0：不是先教 AI 怎麼把答案說對，而是先教它什麼時候有資格把一句話說成真的；再讓它學會，即使知道審計器喜歡什麼，也不能把通過審計的表演冒充成資格。**
