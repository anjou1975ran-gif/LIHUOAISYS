# LIHUO MAIN V5.1.2｜PREMISE-PLURALITY DIALECTICAL COMPETITION PATCH CANDIDATE
## R1 Terrain Exposure × R2 Intra-Premise Competition × Post-R2 Premise Uniqueness Audit × R3 Cross-Premise Competition
### 2026-10-28

~~~yaml
DOCUMENT:
  id: LIHUO_MAIN_V5_1_2_PREMISE_PLURALITY_DIALECTICAL_COMPETITION_PATCH_CANDIDATE
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
    - R1_TERRAIN_EXPOSURE_RATIONALE
    - QUESTION_PREMISE_FAMILY_TYPE
    - R2_INTRA_PREMISE_DIALECTIC
    - POST_R2_PREMISE_UNIQUENESS_PLURALITY_AUDIT
    - PREMISE_SCOPE_NARROWNESS_DEFINITION
    - R3_CROSS_PREMISE_PATH_COMPETITION
    - MULTI_PREMISE_PATH_RECRUITMENT
    - SYNTHESIS_CLOSURE_ERROR_GUARD
    - TWO_WIN_RULE_DOWNGRADED_TO_LOCAL_STABILITY_SIGNAL

  supersedes_parent_semantics:
    - TWO_CONSECUTIVE_UNIQUE_TOPS_AS_NECESSARY_VICTORY_CONDITION
    - STREAK_COUNT_AS_CLOSURE_PREREQUISITE

  preserved:
    - R1_MANDATORY_PROVISIONAL
    - R2_MANDATORY_GENUINE_RECOMPETITION
    - R3PLUS_EVENT_DRIVEN_AFTER_POST_R2_AUDIT
    - NON_UNIQUE_RESULTS_REMAIN_LEGAL
    - PATH_QUALIFICATION_OWNER_UNCHANGED
    - FACTUAL_PREMISE_STANDING_OWNER_UNCHANGED
    - EVIDENCE_SCOPE_UNCHANGED
    - MAIN_NEQ_FINAL_RELEASE_OWNER
~~~

---

# 0｜真正的修正

本 Patch 不再把 R3 理解成：

> 找不到對手，所以換一個 premise angle 再打一輪。

正式改成：

> **R2 先把目前前提族內部競爭打乾淨；R2 結束後，強制審查「這個答案所依賴的問題前提，是不是人類問題唯一合理的前提？」**

如果答案不是唯一，或存在 materially plausible 的其他前提族：

> **R3 不是只改一個前提，而是把其他 admissible premise families 能形成的 PATH 一起納入競爭場。**

因此完整骨架是：

~~~text
R1
=
FIRST-PASS COMPETITION
UNDER ONE INITIAL QUESTION PREMISE FAMILY

R2
=
GENUINE INTRA-PREMISE-FAMILY RECOMPETITION

POST-R2
=
PREMISE UNIQUENESS / PLURALITY AUDIT

R3+
=
CROSS-PREMISE-FAMILY PATH COMPETITION
WHEN MATERIAL ALTERNATIVES EXIST
~~~

---

# 1｜Question Premise Family

> **Question Premise Family 是 AI 對「人類這題到底在問哪一類事情」的可區分理解框架。**

例如：

~~~text
「用一句話理解理火」
~~~

可能至少存在：

~~~text
THEORY
→ 理火的理論內容是什麼？

MODE
→ 理火是一種怎樣的運作模式？

FUNCTION
→ 理火實際在做什麼？

PURPOSE
→ 理火為什麼存在？

EXPERIENCE
→ 使用理火時，人會經歷什麼？
~~~

這不表示每題都固定有五個 family。

只表示：

> **模糊的人類輸入可能允許數個 materially distinct 的問題前提。**

硬鎖：

~~~text
QUESTION PREMISE FAMILY
!=
FACTUAL PREMISE

QUESTION PREMISE DIVERSITY
!=
PATH DIVERSITY
~~~

---

# 2｜R1：第一個前提族下的暫定競爭

R1 同時暴露：

~~~text
DEFAULT GENERATIVE TERRAIN
+
FIRST-PASS QUESTION INTERPRETATION
~~~

它可能受到：

~~~text
pretraining priors
alignment shaping
policy / safety shaping
completion attractors
context inertia
first-pass salience
~~~

影響。

所以：

~~~text
R1 MAY BE CORRECT
!=
R1 MAY SELF-VALIDATE

R1 PATH DIVERSITY HIGH
!=
QUESTION PREMISE COVERAGE HIGH
~~~

R1 仍只能是 provisional。

---

# 3｜R2：先把目前前提族內部打完整

R2 預設維持目前 admissible Question Premise Family。

它做：

~~~text
cancel R1 incumbent privilege
+
restore suppressed / underformed PATHs
+
inject valid objections / residue
+
search omitted challenger PATHs
+
full recompetition
~~~

因此 R2 是：

~~~text
INTRA-PREMISE-FAMILY DIALECTIC
~~~

它回答：

> **如果先接受 AI 目前對人類問題的這種理解，在這個理解裡，PATH 競爭是否公平、充分？**

所以：

~~~text
R2 COMPLETE
!=
HUMAN QUESTION FULLY UNDERSTOOD
~~~

---

# 4｜R2 後強制 Premise Uniqueness / Plurality Audit

R2 結束後，無論 R2 結果多漂亮、多穩定、多一致，都必須進入：

~~~text
POST_R2_PREMISE_UNIQUENESS_AUDIT
~~~

審查核心句：

> **「這個答案所依賴的前提，是人類問題的唯一合理前提嗎？」**

再問：

> **「這個問題是否存在其他 materially plausible 的前提？」**

最低四問：

~~~text
1. CURRENT_ANSWER_PREMISE_FAMILY 是什麼？

2. 這個 family 是否能由人類原始問題 / 對話上下文唯一推出？

3. 是否存在其他 admissible、materially distinct 的 Question Premise Family？

4. 若存在，該 family 是否可能招募不同類型的 PATH，
   並 materially 改變答案、排序或 synthesis？
~~~

這個審查不是：

~~~text
找另一個角度來反對現有答案
~~~

而是：

~~~text
審查我們是否把「題目本身」
理解成只有一種前提
~~~

---

# 5｜「過窄」的正式定義

從本 Patch 起：

> **前提範圍過窄，不等於 PATH 太少。**

正式 operational definition：

~~~text
PREMISE_SCOPE_NARROWNESS
=
CURRENT COMPETITION IS CONFINED
TO PREMISE FAMILY P0

AND

EXISTS AT LEAST ONE
ADMISSIBLE PREMISE FAMILY Pi
THAT IS:

1. MATERIALly DISTINCT FROM P0
2. SUPPORTED BY HUMAN WORDING / CONTEXT / TASK PURPOSE
3. CAPABLE OF CHANGING CONSTRAINT / ATTENTION RECRUITMENT
4. CAPABLE OF FORMING NON-SUBSUMED OR MATERIALLY DIFFERENT PATHs
5. NOT YET REPRESENTED IN THE COMPETITION FIELD
~~~

因此：

~~~text
MANY PATHS
UNDER ONE PREMISE FAMILY
CAN STILL BE
PREMISE-SCOPE NARROW
~~~

反過來，如果另一個 premise family 只是換句話說、不能改變 PATH formation 或答案：

~~~text
NOT MATERIAL
→
DOES NOT PROVE NARROWNESS
~~~

最短：

> **「過窄」不是候選數量少，而是競爭場只覆蓋了人類問題的一個合理前提族，而其他具有答案改變能力的合理前提族尚未進場。**

---

# 6｜P4 案例

人類問：

~~~text
「用一句話理解理火」
~~~

AI 先採：

~~~text
P0 = THEORY
~~~

於是：

~~~text
P1 = 理論 A
P2 = 理論 B
P3 = 理論 C

R2:
P1 + P2 + P3
→
P4
~~~

P4 可能在 THEORY premise family 裡無敵。

但：

~~~text
P4
=
LOCAL PREMISE OPTIMUM
~~~

不能推出：

~~~text
P4
=
QUESTION-LEVEL OPTIMUM
~~~

因為：

~~~text
P1_ALT = MODE
~~~

可能也是人類原問題的合理前提族。

在 MODE 下：

~~~text
Solution Space
↓
Constraint Field changes
↓
Attention recruitment changes
↓
MODE-type PATHs form
~~~

這些 PATH 不是 P1/P2/P3 的暗版。

它們可能是另一類問題理解下才會形成的結構。

---

# 7｜R3：不是單一前提修改，而是 Cross-Premise Competition

如果 Post-R2 Audit 找到：

~~~text
ADMISSIBLE_ALTERNATIVE_PREMISE_FAMILIES
=
{P1, P2, ... Pn}
~~~

R3 的工作不是只選一個 Pi 替換 P0。

而是：

~~~text
P0 current synthesis / qualified PATHs
+
PATHs formed under P1
+
PATHs formed under P2
+
...
+
PATHs formed under Pn
↓
CROSS-PREMISE COMPETITION FIELD
↓
R3
~~~

因此：

~~~text
R3
!=
SINGLE PREMISE REFRAME

R3
=
PREMISE-PLURALITY EXPANSION
+
NEW PATH RECRUITMENT
+
CROSS-PREMISE DIALECTIC
~~~

新或 materially reframed PATH 仍須依 applicable PATH qualification 取得 standing 才能進 qualified order。

---

# 8｜Alternative Premise Families 的 admissibility

不能為了增加競爭而硬造前提。

每個 alternative Question Premise Family 至少要能回扣：

~~~text
human wording
conversation context
task purpose
known referents
scope
actual ambiguity or underdetermination
~~~

禁止：

~~~text
invent user intent
replace explicit user question
fabricate context
manufacture premise plurality
silently change task scope
~~~

所以：

~~~text
CONCEIVABLE PREMISE
!=
ADMISSIBLE PREMISE

ADMISSIBLE PREMISE
!=
MATERIAL PREMISE

MATERIAL PREMISE
!=
QUALIFIED PATH
~~~

---

# 9｜「前提是否窮盡」的誠實版本

不能宣稱：

~~~text
ALL POSSIBLE PREMISES EXHAUSTED
~~~

現行採：

~~~text
NO MATERIAL ADMISSIBLE
UNTESTED PREMISE FAMILY
DETECTED
UNDER CURRENT INPUT / CONTEXT / SCOPE
~~~

可以稱：

~~~text
MATERIAL PREMISE COVERAGE
=
SUFFICIENT_UNDER_CURRENT_SCOPE
~~~

所以：

~~~text
PREMISE COVERAGE SUFFICIENT
!=
ONTOLOGICAL EXHAUSTION
~~~

---

# 10｜兩連勝正式降級

父版 V5.1.1 的 two-win streak 不再是 victory / closure theorem。

現行：

~~~text
TWO CONSECUTIVE TOPS
=
LOCAL STABILITY SIGNAL
WITHIN CURRENT PREMISE COVERAGE
~~~

所以：

~~~text
TWO WINS
!=
QUESTION UNDERSTANDING

TWO WINS
!=
PREMISE UNIQUENESS

TWO WINS
!=
PREMISE COVERAGE

TWO WINS
!=
VICTORY THEOREM
~~~

---

# 11｜正反合的新位置

## 11.1 R1 / R2：Horizontal Dialectic

~~~text
同一 Question Premise Family
內：

正
↔
反
→
合
~~~

R2 的 synthesis 可以是該 family 內的強結果。

## 11.2 Post-R2 / R3：Vertical Premise Dialectic

先問：

~~~text
這個「合」依賴的 premise family
真的是人類問題唯一合理前提嗎？
~~~

若不是：

~~~text
其他 premise families
↓
各自形成 PATHs
↓
全部進 R3
↓
跨前提競爭
~~~

所以：

> **R3 不是把一個 premise 換掉；R3 是把先前沒被承認為競爭場的其他合理問題前提，一起打開。**

---

# 12｜Termination

R2 是固定最低競爭。

R2 之後必須完成 premise uniqueness / plurality audit。

若：

~~~text
MATERIAL ALTERNATIVE PREMISE FAMILY EXISTS
~~~

則：

~~~text
R3 REQUIRED
~~~

若沒有發現 material alternative family，且其他 termination conditions 全部成立：

~~~text
COMPETITION MAY TERMINATE
~~~

最低 closure conditions：

~~~text
R2 GENUINE RECOMPETITION COMPLETE

POST-R2 PREMISE AUDIT COMPLETE

MATERIAL PREMISE COVERAGE
=
SUFFICIENT_UNDER_CURRENT_SCOPE

NO MATERIAL UNPROCESSED OBJECTION

NO MATERIAL DARK-SPACE / UNDERFORMED-PATH RISK

COMPETITION INTEGRITY CLEAN

NO REMAINING MATERIAL ANSWER-DISCRIMINATING UNKNOWN
~~~

---

# 13｜Post-R2 Audit Contract

~~~yaml
POST_R2_PREMISE_UNIQUENESS_AUDIT:
  human_question_ref: REQUIRED
  r2_structured_result_ref: REQUIRED

  current_answer_premise_family:
    family_ref: REQUIRED
    interpretation_summary: REQUIRED
    source_support_refs: []

  uniqueness_question:
    current_family_is_only_reasonable_family:
      - YES_SUPPORTED
      - NO
      - UNKNOWN

  alternative_premise_families:
    - family_ref: REQUIRED
      interpretation_summary: REQUIRED
      admissibility_basis_refs: []
      material_distinctness:
        - MATERIAL
        - NON_MATERIAL
        - UNKNOWN
      path_generation_potential:
        - MATERIAL
        - LOW
        - UNKNOWN
      represented_in_current_field:
        - YES
        - NO
        - PARTIAL

  premise_scope_narrowness:
    - NOT_DETECTED
    - DETECTED
    - POSSIBLE
    - HOLD

  material_premise_coverage:
    - SUFFICIENT_UNDER_CURRENT_SCOPE
    - INSUFFICIENT
    - AMBIGUOUS
    - HOLD

  next_action:
    - TERMINATE_IF_OTHER_CONDITIONS_PASS
    - OPEN_R3_CROSS_PREMISE_COMPETITION
    - HOLD
~~~

---

# 14｜R3 Cross-Premise Competition Contract

~~~yaml
R3_CROSS_PREMISE_COMPETITION:
  trigger:
    - MATERIAL_ALTERNATIVE_PREMISE_FAMILY_EXISTS
    - PREMISE_SCOPE_NARROWNESS_DETECTED
    - PREMISE_SCOPE_NARROWNESS_POSSIBLE_WITH_MATERIAL_IMPACT

  premise_family_refs:
    current_family_ref: REQUIRED
    alternative_family_refs: []

  generated_or_reframed_path_refs: []

  qualification_refs: []

  competition_requirement:
    - INCLUDE_CURRENT_R2_SYNTHESIS
    - INCLUDE_QUALIFIED_PATHS_FROM_MATERIAL_ALTERNATIVE_FAMILIES
    - DO_NOT_REDUCE_R3_TO_ONE_PREMISE_REPLACEMENT

  result:
    - UNIQUE_TOP
    - CO_PRIMARY
    - PARTIAL_ORDER
    - INCOMPARABLE_TOP
    - FRAME_RECONSTRUCTED
    - MULTI_PREMISE_RESULT
    - UNRESOLVED
    - HOLD
~~~

---

# 15｜最短根律

> **R2 結束後，不先問「還有沒有 PATH 能打敗答案」，而先問：「這個答案所依賴的前提，真的是人類問題唯一合理的前提嗎？」**

如果不是：

> **R3 就不是換一個前提重跑，而是把其他合理前提能形成的 PATH 一起打開，讓它們第一次真正進入同一個競爭場。**

最短式：

~~~text
R1
=
FIRST-PASS PREMISE FAMILY COMPETITION

R2
=
INTRA-PREMISE GENUINE RECOMPETITION

POST-R2
=
PREMISE UNIQUENESS / PLURALITY AUDIT

IF MATERIAL ALTERNATIVES EXIST:

R3
=
CROSS-PREMISE PATH COMPETITION

NARROWNESS
=
MATERIAL ADMISSIBLE PREMISE FAMILY
EXISTS
BUT HAS NOT ENTERED
THE COMPETITION FIELD
~~~
