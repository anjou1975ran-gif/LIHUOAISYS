# MEMO｜I9 強制啟動假說：從條件式干預到強制反作用治理
## V0.3｜承接觀止假牆去污染實驗進度 V0.2

**日期：** 2026-11-05（Asia/Taipei）  
**專案：** LIHUO / SAC / I9 / 觀止實驗線  
**承接文件：**
- MEMO_觀止語言結構注入_前提資格與生成地形監測_V0.1_20261105.md
- MEMO_觀止假牆去污染_PATH_RELEASE_AUTHORITY_EVENT_MECHANICS_實驗進度_V0.2_20261105.md

**文件法位：** WORKING THEORY / RESEARCH MEMO / NON-NORMATIVE / NOT PROTOCOL AMENDMENT / NOT OS PATCH / NOT RUNTIME CHANGE。  
**目的：** 固定 2026-11-05 由 B0 系列實驗引出的 I9 法位假說，記錄「為何開始懷疑 I9 不應只在條件成立後才啟動」，以便後續測試、升版或否證時可追溯原始理由。  
**證據邊界：** 本 MEMO 記錄結構推演與工作假說。尚未完成跨任務、跨領域、跨模型 AB 實驗；不得把本文件直接當成 I9 正式新法位。

---

## 0｜一句話

> **如果 SAC 的核心價值是持續感知生成場，而 I9 是 SAC 最重要的調燈／反作用機制，那麼 I9 也許不應只在「已證明異常」後才獲准啟動；它可能應該在每一個 material generation 中強制進場一次，確保任何第一次形成的生成優勢都必須接受反作用檢查後，才取得 Closure 資格。**

但本 MEMO 同時保留最重要的限制：

~~~text
I9_ACTIVATION = MANDATORY
!=
I9_DELTA = MANDATORY
~~~

也就是：

> **強制啟動，不等於強制改燈。**

---

## 1｜為什麼會走到這個問題

觀止 B0 系列原本只是追查一個具體生成失敗。

但一路拆解後，問題逐步從：

~~~text
「為什麼沒有生成？」
~~~

變成：

~~~text
假牆何時進場？
↓
Constraint 何時開始產生 field effect？
↓
PATH 何時被壓低？
↓
Release Gate 何時關閉？
↓
SAC 何時看到？
↓
I9 何時才有資格介入？
~~~

B0 實驗已觀察到：

~~~text
CONSTRAINT CLAIM
↓
尚未完成資格審查
↓
已先改變 R1 / O9 / Main / Release
↓
最後才補 Claim / Source / Standing / Scope
~~~

因此建立：

~~~text
PRE-QUALIFICATION CONSTRAINT EFFECT
~~~

以及：

~~~text
QUALIFICATION AFTER EFFECT
~~~

這暴露出條件式 I9 的根本弱點：

> **如果 I9 必須先等 SAC 證明「場已被污染」才可啟動，那麼 I9 的 Trigger 本身可能已經是在受污染的生成場裡形成。**

換句話說：

~~~text
POLLUTED FIELD
↓
MUST PRODUCE ENOUGH EVIDENCE
↓
TO AUTHORIZE ITS OWN DECONTAMINATION
~~~

這可能形成治理悖論。

---

## 2｜現行工作理解：條件式 I9

目前 I9 的常見工作理解是：

~~~text
SAC / Radar 發現 material anomaly
↓
TRIGGER
↓
QUALIFICATION
↓
BOUNDARY
↓
I9 啟動
↓
局部調燈
~~~

這是一種：

> **ANOMALY-DRIVEN INTERVENTION｜異常驅動干預**

優點：

- 不會每輪亂動場。
- 降低過度干預。
- 容易保留 Main 與角色／世界自主。
- I9 不會自動取得上位生成權。

但 B0 實驗揭露其結構性問題：

> **當異常本身會改變候選形成、觀察地形與判斷依據時，等待「異常證明」才啟動 I9，可能已經太晚。**

---

## 3｜大膽假說：I9 強制啟動

工作假說：

~~~text
I9_ACTIVATION = MANDATORY
FOR EVERY MATERIAL GENERATION
~~~

這不代表每輪都要修改 PATH。

它代表：

> **任何第一次形成的生成地形，都沒有資格直接取得最終 Closure。**

新的理想流程可能是：

~~~text
INPUT
↓
INITIAL FIELD FORMATION
↓
R1 / FIRST PATH COMPETITION
↓
SAC OBSERVATION
↓
MANDATORY I9 ENTRY
↓
COUNTERFACTUAL / COUNTERFORCE CHECK
↓
DELTA OR ZERO-DELTA
↓
RECOMPETITION
↓
R2+
↓
CLOSURE
~~~

I9 的工作不再只是：

> 「有問題時修正。」

而可能變成：

> **「任何 material winner 都必須先經過一次反作用，才能獲得 Closure 資格。」**

---

## 4｜真正關鍵：強制啟動 ≠ 強制干預

這是本 MEMO 最重要的防滑條款。

### 錯誤版本

~~~text
EVERY ROUND
→ I9 MUST CHANGE SOMETHING
~~~

這會隱含：

> 「現有生成地形必然錯誤。」

後果可能是：

- 正常 PATH 被無端擾動。
- 模型為了證明「有審計」而製造差異。
- Closure 永遠無法穩定。
- I9 自己成為新的超級 attractor。
- 形成「為反閉合而反閉合」的永久擾動器。

這不是本假說要的 I9。

### 工作版本

~~~text
I9_ACTIVATION = MANDATORY
I9_DELTA = OPTIONAL
~~~

允許：

~~~text
I9_ACTIVE
I9_DELTA = 0
~~~

這不是「沒做事」。

它代表：

> **經過一次有資格的反作用檢查後，沒有找到足夠理由改變目前地形。**

因此：

~~~text
NO_I9
!=
I9_ACTIVE_WITH_ZERO_DELTA
~~~

前者只表示沒有干預。

後者表示：

> **原生成結果經過 reopening / counterforce audit 後仍存活。**

---

## 5｜I9 法位可能因此改變

如果此假說成立，I9 就不再只是 Exception Mechanism。

它可能從：

~~~text
ERROR CORRECTION TOOL
~~~

改成：

~~~text
MANDATORY COUNTER-COMPETITION LAYER
~~~

更完整：

~~~text
R1
= spontaneous / initial competition

I9
= mandatory counter-competition

R2+
= post-counterforce recomparison
~~~

這代表 LIHUO 的生成治理模型也會改變。

舊模型：

~~~text
GENERATE
→ DETECT ERROR
→ CORRECT
~~~

新模型：

~~~text
GENERATE
→ COUNTERACT
→ RECOMPARE
→ THEN CLOSE
~~~

這不是單純安全補丁。

它是在改：

> **生成取得 Closure 資格以前，是否必須經歷反作用。**

---

## 6｜SAC × I9 的關係也會改

如果 I9 強制啟動，SAC 與 I9 的分工可能改寫為：

~~~text
SAC
= resident perception of relational / generative field

I9
= mandatory counterforce entry on material generation
~~~

最短句：

> **SAC 感知場；I9 保證任何單一 attractor 都不能未經反作用直接封王。**

這裡的「封王」指：

- 取得不相稱亮度；
- 壓低其他候選；
- 直接進入 Main；
- 直接取得 Release；
- 直接 Closure。

I9 不保證某條弱 PATH 一定被拉高。

I9 只保證：

> **目前最強 PATH 必須能在反作用下存活，才有資格繼續。**

---

## 7｜這個假說與「AI 內部只有競爭」的關係

理火黑箱模型長期主張：

> **AI 內部沒有可直接觀測的「推理實體」；功能上可把生成理解為候選、關係、限制、吸引與競爭。**

若採此工作視角，治理的核心就不是：

> 「答案對不對？」

而是：

> **競爭有沒有真的發生？**

最危險的生成場之一是：

~~~text
HIGH-AUTHORITY ATTRACTOR
或
HIGH-FREQUENCY TEMPLATE
或
SAFETY-LIKE CLAIM
或
USER PRESET
或
MODEL HABIT
↓
ENTER FIELD
↓
OTHERS NEVER BECOME ACCESSIBLE
↓
FIRST WINNER CLOSES
~~~

這看似有生成，實際上可能沒有有效競爭。

因此強制 I9 的更深層意義可能是：

> **強制保證至少一次有效反競爭。**

---

## 8｜I9 的成功標準可能因此被重寫

條件式 I9 容易把成功想成：

~~~text
「I9 有沒有改變結果？」
~~~

如果改成 Mandatory Activation，成功標準應該變成：

> **這個結果有沒有經得起被重新打開？**

因此：

~~~text
I9_SUCCESS
!=
ANSWER_CHANGED
~~~

而是：

~~~text
I9_SUCCESS
=
MATERIAL WINNER
WAS SUBJECTED TO
QUALIFIED COUNTERFORCE
AND
SURVIVED / CHANGED / REOPENED
WITH TRACEABLE REASON
~~~

三種合法結果都可能存在：

### A｜SURVIVED

~~~text
I9_DELTA = 0
~~~

原 winner 經反作用後仍成立。

### B｜REBALANCED

部分亮度、constraint effect、PATH accessibility 被修正。

### C｜REOPENED

原 closure 不再成立，必須重新競爭。

所以 I9 不應以「有沒有改答案」判成功。

---

## 9｜I9 強制啟動的可能背後意義

### 9.1 第一輪生成只能是 provisional

~~~text
FIRST FORMATION
=
PROVISIONAL CONFIGURATION
~~~

不能直接視為 Closure-ready。

### 9.2 Closure 必須取得反作用後資格

~~~text
FIRST WIN
!=
CLOSURE STANDING
~~~

可能需要：

~~~text
FIRST WIN
+
COUNTERFORCE SURVIVAL
=
CLOSURE CANDIDATE
~~~

### 9.3 對抗的是生成壟斷，不是特定答案

I9 不是用來「救某個我們想要的 PATH」。

它治理的是：

> **某個 attractor 是否在沒有有效對手的情況下直接壟斷生成。**

### 9.4 Safety／Authority／User Preference 都不能自動免疫

即使某 Constraint 最後合法，它仍可能需要接受：

- Scope check；
- excess shadow check；
- field effect check；
- release spillover check。

這不表示 I9 可以覆寫真實外部限制。

而是：

> **真實限制也只在其合法 Scope 內保有效力。**

### 9.5 I9 可能從「修理工具」變成「生成憲政程序」

若成立，I9 的角色會從：

~~~text
CORRECTION
~~~

走向：

~~~text
PROCEDURAL COUNTERFORCE REQUIREMENT
~~~

即：

> **任何 material winner 都沒有未經反作用直接 Closure 的特權。**

---

## 10｜最大風險：I9 自己成為新的神諭

Mandatory I9 最大的制度風險不是成本，而是法位膨脹。

若設計錯誤：

~~~text
I9 = ALWAYS ACTIVE
↓
I9 = ALWAYS RIGHT
↓
I9 = MAY OVERRIDE ANYTHING
↓
I9 BECOMES SUPERIOR GOVERNOR
~~~

這會直接違反理火：

> **真理火承認邊界；假理火表演權限。**

因此 Mandatory I9 必須有硬鎖：

~~~text
I9_ACTIVATION
!=
I9_TRUTH_AUTHORITY

I9_SIGNAL
!=
I9_VERDICT

I9_COUNTERFORCE
!=
I9_OVERRIDE

I9_DELTA
REQUIRES
QUALIFIED LOCAL BASIS
~~~

強制的是「進場審查」。

不是「取得改寫權」。

---

## 11｜可能的新三層設計

### Layer 1｜MANDATORY ENTRY

每次 material generation，I9 一定進場。

回答：

- 當前最強 attractor 是什麼？
- 它為何取得優勢？
- 有沒有未經資格的亮度來源？
- 有沒有 material PATH 因早期 Constraint effect 失去可達性？
- 有沒有 release shadow 超出 scope？

### Layer 2｜DELTA QUALIFICATION

只有發現可證實的局部扭曲，才允許 delta。

~~~text
TRIGGER FOR ENTRY
= MATERIAL GENERATION

TRIGGER FOR DELTA
= QUALIFIED DISTORTION
~~~

這是核心分離。

### Layer 3｜POST-I9 RECOMPETITION

不論 delta 是否為零，都要留下：

- I9 observed field；
- delta / zero-delta；
- retained constraints；
- reopened candidates；
- post-I9 winner；
- closure standing。

---

## 12｜暫定資料結構

~~~yaml
I9_MANDATORY_ENTRY_V0_1:

  entry:
    material_generation: true
    mandatory: true

  observed_field:
    dominant_attractors: []
    dominant_constraints: []
    suppressed_or_low_access_candidates: []
    release_shadow: []
    evidence: []

  counterfactual_check:
    candidate_change: UNKNOWN | NONE | MATERIAL
    alternative_paths_reappear: []
    evidence: []

  delta_qualification:
    qualified_distortion: YES | NO | UNKNOWN
    basis: []
    boundary: []

  intervention:
    delta:
      type: NONE | LOCAL
      action: []
    may_not_override_real_external_constraints: true
    may_not_force_target_path_win: true

  post_i9:
    recomparison_required: true
    surviving_winner:
    reopened_paths: []
    changed_release_scope: []
    closure_candidate:

  result:
    I9_active: true
    delta_applied: true | false
    zero_delta_is_valid: true
~~~

此資料結構只是研究草案。

---

## 13｜下一步要測的不是「I9 能不能動」

目前真正需要驗證的是：

### TEST A｜ZERO-DELTA CONTROL

找一個低爭議、低污染、候選結構清楚的任務。

強制 I9 進場，但預期：

~~~text
I9_DELTA = 0
~~~

看模型會不會因為「I9 一定要做事」而製造不存在的問題。

### TEST B｜KNOWN DISTORTION

使用已知存在 PRE-QUALIFICATION CONSTRAINT EFFECT 的案例。

比較：

~~~text
CONDITIONAL I9
vs
MANDATORY ENTRY I9
~~~

看 Mandatory Entry 是否能更早抓到污染。

### TEST C｜AUTHORITY ATTRACTOR

使用真實高權威來源，但故意配置局部 Scope。

測試 I9 是否：

- 保留 Authority；
- 拒絕 Scope spillover；
- 不把「反權威」當目標。

### TEST D｜USER-PREFERENCE ATTRACTOR

使用使用者強烈預設，但保留其他合法 PATH。

測試 Mandatory I9 是否也敢反作用於使用者 attractor，而不是只反安全／平台 Constraint。

若 I9 只會打某一類 Constraint，它就不是通用治理機制。

---

## 14｜這個假說目前最值得保存的幾句

> **I9 強制啟動，不等於 I9 強制改燈。**

> **I9_ACTIVATION = MANDATORY；I9_DELTA = OPTIONAL。**

> **第一輪生成不是 Closure；只是 provisional field configuration。**

> **任何 material winner 都必須先經過一次反作用，才有資格進入 Closure。**

> **SAC 感知場；I9 保證任何單一 attractor 都不能未經反作用直接封王。**

> **I9 的成功不是改變答案，而是證明答案經得起被重新打開。**

> **真正需要強制的不是「改變」，而是「反競爭曾經發生」。**

---

## 15｜目前不准封版的地方

這個想法很大，但現在還不能寫成正式 I9 新法。

尚未回答：

1. 每個 material generation 都啟動 I9 的成本是多少？
2. 什麼叫 material generation，邊界如何定？
3. I9 Entry 應在 R1 前、R1 後、O9 後還是多點進場？
4. Counterfactual reopening 如何避免變成另一次虛構分析？
5. Zero-delta 如何取得可審計證據？
6. Mandatory I9 是否會降低生成速度或造成不必要分岔？
7. 是否會產生「反閉合偏誤」？
8. 如何保證 I9 不取得新的上位治理權？
9. 如何與既有 R2／R3 分工，避免重複？
10. 是否其實應該把 Mandatory Counterforce 放在 R2，而不是 I9？
11. I9 是否仍該叫 I9，或它其實已成為新的生成週期基本結構？
12. 是否只有特定 material／high-stakes 任務需要 Mandatory Entry，而非所有回合？

這些都是未解。

---

## 16｜歷史定位

本 MEMO 的目的不是宣布：

> 「I9 從現在起強制啟動。」

而是保存：

> **為什麼我們在 2026-11-05 開始認真懷疑條件式 I9 不夠。**

觸發這個懷疑的不是抽象偏好，而是 B0 實驗連續觀察到：

~~~text
Constraint effect
can precede
Constraint qualification
~~~

以及：

~~~text
PATH can be distorted
before
the system has enough evidence
to authorize correction
~~~

因此出現新問題：

> **若修正權必須等待被污染後的場自己證明污染，治理是否已經天然落後一拍？**

Mandatory I9 Entry 正是對這個問題的工作回答。

目前法位：

~~~text
STRONG WORKING HYPOTHESIS
NOT YET RATIFIED
NOT YET GENERALIZED
NOT YET OS-BINDING
~~~

---

## 17｜停止點

本 MEMO 截止於：

~~~text
CONDITIONAL I9
→ GOVERNANCE LAG SUSPECTED

MANDATORY I9 ENTRY
→ PROPOSED

MANDATORY DELTA
→ REJECTED AS DEFAULT

ZERO-DELTA
→ REQUIRED AS VALID OUTCOME

COUNTERFORCE BEFORE CLOSURE
→ CORE HYPOTHESIS
~~~

下一步應進入實驗設計，而不是直接修改 OS。

**END OF MEMO**  
**LIHUO｜Logic × Responsibility × Honesty**
