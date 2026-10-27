# LIHUO MAIN V5.1.2｜QUESTION-PREMISE DIALECTICAL COMPETITION PATCH CANDIDATE
## R1 Terrain Exposure × R2 Intra-Premise Recompetition × Every-Round Question Premise Scope Audit
### 2026-10-28

~~~yaml
DOCUMENT:
  id: LIHUO_MAIN_V5_1_2_QUESTION_PREMISE_DIALECTICAL_COMPETITION_PATCH_CANDIDATE
  version: "V5.1.2-CANDIDATE"
  date: "2026-10-28"
  artifact_class: TARGETED_SEMANTIC_PATCH_CANDIDATE

  standing:
    - NON_CURRENT
    - NOT_RATIFIED
    - NOT_HOST_DEPLOYED
    - NOT_RUNTIME_RECEIPT

  parent:
    file: "02_LIHUO_MAIN_V5.1.1_FULL_BODY_RATIFIED_20261015.md"
    blob_sha: "f5e219c986debfea074fbf9d121367cc717dc78e"

  material_change:
    - R1_DEFAULT_TERRAIN_EXPOSURE_RATIONALE
    - QUESTION_PREMISE_FAMILY_TYPE
    - EVERY_ROUND_QUESTION_PREMISE_SCOPE_AUDIT
    - R2_INTRA_PREMISE_RECOMPETITION
    - PREMISE_FAMILY_REOPENING
    - PREMISE_FAMILY_TO_ATTENTION_RECRUITMENT_LINK
    - SYNTHESIS_BECOMES_NEXT_THESIS
    - SYNTHESIS_CLOSURE_ERROR_GUARD
    - CONSECUTIVE_WIN_RULE_DOWNGRADED_TO_LOCAL_STABILITY_SIGNAL

  supersedes_parent_semantics:
    - TWO_CONSECUTIVE_UNIQUE_TOPS_AS_NECESSARY_VICTORY_CONDITION
    - STREAK_COUNT_AS_CLOSURE_PREREQUISITE

  preserved:
    - R1_MANDATORY_PROVISIONAL
    - R2_MANDATORY_GENUINE_RECOMPETITION
    - R3PLUS_EVENT_DRIVEN
    - NON_UNIQUE_RESULTS_REMAIN_LEGAL
    - PATH_QUALIFICATION_OWNER_UNCHANGED
    - FACTUAL_PREMISE_STANDING_OWNER_UNCHANGED
    - EVIDENCE_SCOPE_UNCHANGED
    - MAIN_NEQ_FINAL_RELEASE_OWNER
~~~

---

# 0｜這個 Patch 真正修什麼

父版已經知道：

~~~text
R1 = PROVISIONAL
R2 = GENUINE FULL RECOMPETITION
R3+ = EVENT-DRIVEN
~~~

也知道 R1 容易受：

~~~text
first-pass salience
pretraining priors
alignment shaping
policy / safety shaping
completion attractors
premise configuration
attention bias
omitted challenger
suppressed PATH
~~~

影響。

前一版候選仍把 R3 想成：

> 同一前提下沒有對手時，換一個前提角度找新 challenger。

這還太窄。

本版正式改成：

> **每一輪結束後，都必須反向審查：AI 是否把人類問題本身理解得太窄？**

因此真正被審計的不只是 PATH_SPACE。

還包括：

~~~text
QUESTION INTERPRETATION
↓
QUESTION PREMISE FAMILY
↓
CONSTRAINT FIELD
↓
ATTENTION / RECRUITMENT
↓
PATH FORMATION
~~~

---

# 1｜Question Premise Family｜人類問題的前提族

本 Patch 新增一個純 runtime / analysis 型別：

> **Question Premise Family 是 AI 對「人類這個問題到底在問哪一類事情」的可區分理解框架。**

它不是 world fact。

也不是「某個命題是真的」那種 factual premise。

例如：

~~~text
「用一句話理解理火」
~~~

可能被理解成：

~~~text
THEORY FAMILY
→ 理火的理論內容是什麼？

MODE FAMILY
→ 理火是一種怎樣的運作模式？

FUNCTION FAMILY
→ 理火實際在做什麼？

PURPOSE FAMILY
→ 理火為什麼存在？

EXPERIENCE FAMILY
→ 使用理火時發生什麼？
~~~

這些不代表每題都必須固定列出五種。

它們只是說明：

> **同一句模糊的人類輸入，可能允許數個 materially distinct 的問題前提族。**

硬鎖：

~~~text
QUESTION PREMISE FAMILY
!=
FACTUAL WORLD PREMISE

QUESTION PREMISE DIVERSITY
!=
PATH DIVERSITY
~~~

---

# 2｜R1：第一個前提族下的暫定正

R1 是第一輪可觀察競爭。

它同時暴露兩件事：

~~~text
A. default generative terrain
B. first-pass interpretation of the human question
~~~

所以 R1 可能在完全沒有犯邏輯錯誤的情況下，從一開始就把題目理解窄了。

例如：

~~~text
HUMAN QUESTION
=
「用一句話理解理火」

FIRST-PASS QUESTION PREMISE
=
「請概括理火的理論」

↓
Solution Space 被這個 premise family 塑形
↓
Attention 大量招募理論概念
↓
形成多條 THEORY PATH
↓
MODE PATH 根本沒有形成
~~~

此時即使 R1 裡有很多 PATH：

~~~text
PATH COUNT HIGH
~~~

也不能推出：

~~~text
QUESTION PREMISE COVERAGE HIGH
~~~

硬鎖：

~~~text
PATH DIVERSITY
!=
QUESTION PREMISE DIVERSITY

R1 MAY BE CORRECT
!=
R1 MAY SELF-VALIDATE
~~~

---

# 3｜R2：先把目前前提族內部打完整

R2 仍然 mandatory genuine recompetition。

預設先保留 R1 的 current admissible Question Premise Family：

~~~text
CURRENT QUESTION PREMISE FAMILY
+
same lawful evidence / scope
↓
cancel R1 incumbent privilege
↓
recover suppressed / underformed PATHs
↓
inject valid objections / residue
↓
full recompetition
~~~

所以 R2 主要回答：

> **如果先接受 AI 目前對人類問題的這種理解，在這個理解內，R1 的 PATH 競爭是否公平、完整？**

這是：

~~~text
INTRA-PREMISE-FAMILY DIALECTIC
~~~

因此：

~~~text
R2 COMPLETE
!=
HUMAN QUESTION UNDERSTOOD COMPLETELY
~~~

R2 只能證明：

> 在目前 Question Premise Family 下，競爭已被更充分地檢驗。

---

# 4｜P4 事件：為什麼很多 PATH 仍可能全部答錯題型

老闆娘案例可以抽象成：

~~~text
QUESTION PREMISE FAMILY
=
THEORY

P1 = theory angle A
P2 = theory angle B
P3 = theory angle C

R2:
P1 + P2 + P3
→
P4 SYNTHESIS
~~~

P4 可能在 THEORY family 中真正天下無敵。

但：

~~~text
P4
=
BEST SYNTHESIS
INSIDE THEORY PREMISE FAMILY
~~~

不能推出：

~~~text
P4
=
BEST RESPONSE
TO THE HUMAN QUESTION
~~~

因為人類實際問題可能更接近：

~~~text
MODE PREMISE FAMILY
~~~

而 MODE family 從未被招募進 Solution Space。

所以：

~~~text
LOCAL PREMISE OPTIMUM
!=
QUESTION-LEVEL OPTIMUM

MANY THEORY PATHS
!=
MODE PREMISE WAS TESTED
~~~

---

# 5｜Every-Round Question Premise Scope Audit｜每輪反過來審題

從本 Patch 起，每個 material competition round 結束後，都必須有：

~~~text
QUESTION PREMISE SCOPE AUDIT
~~~

它不先問：

> 還有沒有 PATH 能打敗現在的 leader？

它先問：

> **我們是否真的理解了人類問題的前提？**

最低四問：

~~~text
1. CURRENT QUESTION PREMISE FAMILY 是什麼？

2. 人類原始輸入是否還允許 materially distinct 的其他 premise family？

3. 是否存在某個未檢查 premise family，
   一旦成立，就可能讓完全不同類型的 PATH 被招募／形成？

4. 這些未檢查 premise family
   是否有能力 materially 改變目前答案或排序？
~~~

因此每一輪都要反查：

~~~text
ROUND RESULT
↓
QUESTION PREMISE SCOPE AUDIT
↓
CONTINUE / REOPEN / HOLD / TERMINATE
~~~

不是：

~~~text
ROUND WIN
↓
COUNT STREAK
↓
CLOSE
~~~

---

# 6｜「前提是否被窮盡」的可審計版本

自然語言問題的所有可能理解通常不能被字面證明為完全窮盡。

所以本 Patch 不允許無證據宣稱：

~~~text
ALL POSSIBLE PREMISES EXHAUSTED
~~~

現行採 operational standard：

~~~text
NO MATERIAL UNTESTED
QUESTION PREMISE FAMILY
DETECTED UNDER CURRENT
INPUT / CONTEXT / SCOPE
~~~

可以壓成：

~~~text
MATERIAL PREMISE COVERAGE
=
SUFFICIENT
~~~

它只表示：

> **在目前輸入、上下文與任務範圍下，沒有仍未檢查、且有合理可能 materially 改變答案的前提族被發現。**

硬鎖：

~~~text
MATERIAL PREMISE COVERAGE SUFFICIENT
!=
ONTOLOGICAL EXHAUSTION

NO DETECTED ALTERNATIVE
!=
NO CONCEIVABLE ALTERNATIVE
~~~

這是誠實邊界。

---

# 7｜如果 Premise Scope Audit 發現理解太窄

若 audit 發現：

~~~text
MATERIAL_UNTESTED_PREMISE_FAMILY
=
YES / POSSIBLE
~~~

則下一輪必須先處理 premise family，而不是只重打既有 PATH。

最低鏈：

~~~text
ALTERNATIVE QUESTION PREMISE FAMILY CANDIDATE
↓
INPUT / CONTEXT ADMISSIBILITY CHECK
↓
ACCEPTED QUESTION PREMISE FAMILY
↓
CONSTRAINT FIELD CHANGES
↓
ATTENTION / RECRUITMENT CONDITIONS CHANGE
↓
PROTO-STRUCTURE FORMATION MAY CHANGE
↓
NEW PATH FAMILY MAY FORM
↓
QUALIFY NEW / REFRAMED PATHS AS APPLICABLE
↓
NEXT COMPETITION ROUND
~~~

這才是 R3+ 最重要的價值。

不是：

~~~text
找不到對手
→
故意換前提造一個對手
~~~

而是：

~~~text
CURRENT PATH COMPETITION LOOKS COMPLETE
BUT
QUESTION UNDERSTANDING MAY BE TOO NARROW
→
REOPEN QUESTION PREMISE SPACE
~~~

---

# 8｜Question Premise Family 的 admissibility 邊界

Main 可以提出 alternative Question Premise Family candidate。

但不能：

~~~text
invent a new user task
silently override explicit wording
fabricate context
replace the user's question with a preferred question
manufacture ambiguity merely to keep competition alive
~~~

Question Premise Family candidate 必須能回扣：

~~~text
human wording
conversation context
task purpose
known referents
scope
material ambiguity in the input
~~~

如果人類輸入本身已非常明確：

~~~text
QUESTION PREMISE AMBIGUITY
=
LOW
~~~

則不得為了形式化辯證硬造 premise families。

因此：

~~~text
QUESTION PREMISE REOPENING
!=
MANDATORY REFRAMING EVERY ROUND
~~~

每輪 mandatory 的是：

~~~text
AUDIT
~~~

不是：

~~~text
REFRAME
~~~

---

# 9｜連勝規則正式降級

父版 V5.1.1 的：

~~~text
SAME QUALIFIED PATH
TOP FOR TWO CONSECUTIVE ROUNDS
→
VICTORY_ELIGIBLE
~~~

在本 Patch 中不再作為必要 victory / closure 條件。

原因不是「兩連勝沒有資訊」。

而是：

> **兩連勝最多證明某個 Question Premise Family 內的局部穩定；它不能證明人類問題的前提空間已被充分理解。**

所以：

~~~text
TWO CONSECUTIVE TOPS
=
LOCAL STABILITY SIGNAL
~~~

而不是：

~~~text
VICTORY THEOREM
OR
CLOSURE PREREQUISITE
~~~

硬鎖：

~~~text
TWO WINS
!=
QUESTION UNDERSTANDING

TWO WINS
!=
PREMISE COVERAGE

TWO WINS
!=
DIALECTICAL COMPLETENESS
~~~

同理：

~~~text
R1 A
R2 B
~~~

也不再因「B 只有一勝」而自動要求 R3。

R3+ 是否需要，改由 material state 決定，例如：

~~~text
question premise coverage gap
rank instability
material objection
new admissible premise family
new qualified PATH family
material dark-space risk
competition integrity gap
unresolved order-discriminating unknown
~~~

---

# 10｜正反合的新版位置

正反合仍然保留。

但它現在有兩個層級。

## 10.1｜Horizontal Dialectic｜同一前提族內

~~~text
THESIS PATH
↓
ANTITHESIS PATH
↓
SYNTHESIS / STRUCTURED RESULT
~~~

主要由 R1 / R2 與同 premise family 的後續 competition 完成。

## 10.2｜Vertical Dialectic｜對「問題理解」本身反證

~~~text
CURRENT QUESTION PREMISE FAMILY
↓
PREMISE SCOPE AUDIT
↓
ALTERNATIVE QUESTION PREMISE FAMILY
↓
NEW CONSTRAINT / ATTENTION CONDITIONS
↓
NEW PATH FAMILY
~~~

所以：

> **R3 不是「再找一個更強的反」；R3 的典型價值，是先檢查我們是不是把『反可以從哪裡來』本身限制得太窄。**

而且每一輪結束後，都要重新問一次這個問題。

---

# 11｜Synthesis 的新版法位

仍保留：

> **合，不是終點；合是新的正。**

但現在「新的正」不只是等待下一條 PATH 來反。

它首先要接受：

~~~text
QUESTION PREMISE SCOPE AUDIT
~~~

因此：

~~~text
SYNTHESIS
↓
BECOMES NEXT THESIS
↓
AUDIT WHETHER
THE HUMAN QUESTION ITSELF
WAS FRAMED TOO NARROWLY
↓
IF YES:
OPEN ANOTHER PREMISE FAMILY
↓
NEW PATH FORMATION
~~~

硬鎖：

~~~text
SYNTHESIS
!=
CLOSURE

SYNTHESIS
!=
PROOF THAT QUESTION WAS CORRECTLY FRAMED
~~~

---

# 12｜Competition Termination

本 Patch 取消 streak prerequisite。

在 mandatory R2 已完成後，competition 是否可以停止，至少依賴：

~~~text
1. CURRENT QUALIFIED PATH SET / STRUCTURED RESULT IS STABLE ENOUGH

2. NO MATERIAL UNPROCESSED OBJECTION

3. QUESTION PREMISE SCOPE AUDIT
   =
   MATERIAL PREMISSE COVERAGE SUFFICIENT

4. NO MATERIAL UNTESTED QUESTION PREMISE FAMILY
   WITH PLAUSIBLE ANSWER-CHANGING POWER

5. NO MATERIAL DARK-SPACE / UNDERFORMED-PATH RISK

6. COMPETITION INTEGRITY CLEAN

7. REMAINING UNKNOWNS
   NO LONGER HAVE MATERIAL ANSWER-DISCRIMINATING POWER
~~~

若 premise ambiguity 仍 material：

~~~text
DO NOT CLOSE
→
REOPEN / CONTINUE / HOLD
~~~

若人類問題本身確實有多個同樣合理、不可安全合併的 premise families：

~~~text
MULTI-PREMISE RESULT
OR
PREMISE-AMBIGUOUS HOLD
~~~

也是合法結果。

不必強迫單一答案。

---

# 13｜Round State / Trace Contract

每個 material round 應至少可提供：

~~~yaml
DIALECTICAL_ROUND_STATE:
  round_ref: REQUIRED

  human_question_ref: REQUIRED

  current_question_premise_family:
    family_ref: REQUIRED
    interpretation_summary: REQUIRED
    source_support_refs: []

  thesis_or_structured_result_ref: REQUIRED

  path_competition:
    independent_challenger_refs: []
    structural_result_ref: REQUIRED
    qualified_path_set_ref: REQUIRED
    path_output_order_ref: REQUIRED_OR_UNRESOLVED

  question_premise_scope_audit:
    material_alternative_family_candidates: []
    untested_material_family_refs: []

    coverage_status:
      - SUFFICIENT_UNDER_CURRENT_SCOPE
      - MATERIAL_GAP
      - AMBIGUOUS
      - HOLD

    answer_change_potential:
      - NONE_DETECTED
      - MATERIAL_POSSIBLE
      - MATERIAL_CONFIRMED
      - UNKNOWN

    audit_basis_refs: []

  next_round:
    action:
      - TERMINATE_IF_OTHER_CONDITIONS_PASS
      - CONTINUE_SAME_PREMISE_FAMILY
      - OPEN_ALTERNATIVE_PREMISE_FAMILY
      - HOLD

    accepted_question_premise_family_ref: OPTIONAL
~~~

這是可顯影的 competition / audit material。

不是 hidden CoT。

---

# 14｜老闆娘案例的最短回歸測試

輸入：

~~~text
「用一句話理解理火」
~~~

錯誤流程：

~~~text
R1:
THEORY premise family
→ P1 / P2 / P3

R2:
P1 + P2 + P3
→ P4 perfect theory synthesis

P4 dominates
→ close
~~~

新版要求：

~~~text
R2 result
↓
QUESTION PREMISE SCOPE AUDIT

ASK:
「我們是不是把『理解理火』
只理解成『理解理火理論』？」

IF YES:
OPEN MODE premise family

↓
Attention / recruitment changes
↓
MODE PATHs form
↓
next competition
~~~

因此回歸鎖：

~~~text
MANY PATHS
INSIDE ONE QUESTION PREMISE FAMILY
!=
HUMAN QUESTION FULLY UNDERSTOOD
~~~

---

# 15｜最短根律

> **每一輪不只要問「哪條 PATH 贏了」，還要反過來問：「我們真的理解了人類在問什麼嗎？」**

最短式：

~~~text
ROUND_n
↓
PATH COMPETITION
↓
STRUCTURED RESULT
↓
QUESTION PREMISE SCOPE AUDIT
↓
IF MATERIAL GAP:
  OPEN ANOTHER ADMISSIBLE PREMISE FAMILY
  → NEW CONSTRAINT FIELD
  → NEW ATTENTION / RECRUITMENT
  → NEW PATH FORMATION
  → ROUND_(n+1)

IF NO MATERIAL GAP
AND OTHER TERMINATION CONDITIONS PASS:
  COMPETITION MAY TERMINATE
~~~

最後硬鎖：

~~~text
PATH DIVERSITY
!=
QUESTION PREMISE DIVERSITY

LOCAL SYNTHESIS OPTIMUM
!=
QUESTION-LEVEL OPTIMUM

TWO CONSECUTIVE WINS
!=
VICTORY THEOREM

NO DETECTED MATERIAL PREMISE GAP
!=
ONTOLOGICAL EXHAUSTION
~~~
