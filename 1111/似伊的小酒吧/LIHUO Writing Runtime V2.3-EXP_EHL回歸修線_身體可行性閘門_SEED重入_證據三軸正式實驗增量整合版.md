# 理火寫作 Runtime V2.3-EXP

## LIHUO Writing Runtime V2.3-EXP

### EHL 回歸修線 × 身體可行性閘門 × SEED 重入 × 身體條件證據三軸
### EHL Regression Rewiring × Body Feasibility Gate × Seed Reentry × Three-Axis Body-Condition Evidence

---

```yaml
EXPERIMENTAL_VERSION:
  from: "LIHUO Writing Runtime V2.2-EXP"
  to: "LIHUO Writing Runtime V2.3-EXP"
  version_id: "LIHUO-WRITING-RUNTIME-v2.3-EXP-EHL-REGRESSION-FEASIBILITY-SEED"
  status: "FORMAL_EXPERIMENTAL_INCREMENTAL_UPGRADE"
  date: "2026-08-27"

PARENT_SOURCE_LOCK:
  file: "LIHUO Writing Runtime V2.2-EXP_EHL生命週期_身體史與當前身體態分離_正式實驗增量整合版.md"
  sha256: "fe86f03e064972c043b0715fced822df63a0ecbf6c2a750d7f0139269c3e24cf"
  inheritance: "FULL_EXCEPT_EXPLICIT_V2_3_SUPERSESSION"
  parent_modified_in_place: false

CURRENT_ALIGNMENT:
  root_protocol: "LIHUO PROTOCOL V2.3"
  lighter: "LIHUO LIGHTER V3.5-EXP"
  main_system: "LIHUO AI SYSTEM V3.5-EXP"
  writing_parent: "LIHUO Writing Runtime V2.2-EXP"

REGRESSION_BASIS:
  - "V2.2 EHL document regression suite"
  - "FOOTBINDING historical body-condition PATCH V0.1-EXP as body-causality donor"
  - "JWG character-pool source/evidence discipline as source-character firewall reference"
  - "AINT V2.1-RC3 observable-delta candidate handoff as external-event return reference"

UPGRADE_SCOPE:
  adds:
    - "BODY CONDITION EVIDENCE THREE-AXIS：presence / commitment / provenance 分離"
    - "BODY FEASIBILITY GATE：節點與正文生成前的身體可行性檢查"
    - "ACTION ATTEMPT / ACTION SUCCESS 分離"
    - "RECOVERY TRANSFORM：時間經過不等於自動 reset"
    - "EHL SEED / LOG REENTRY BINDING"
    - "EXTERNAL BODY EVENT RETURN CONTRACT"
    - "COUNTERFACTUAL BODY CONSISTENCY AUDIT"
    - "V2.2 規格靜態回歸結果與修線紀錄"
  preserves:
    - "V2.2 Body History / Current Body State separation"
    - "EHL lifecycle: Character Bind / Scene Rehydrate / Save Commit"
    - "V3.5 Lighter-governed wiring"
    - "SFS != SAC"
    - "Prior != Fact"
    - "Body state does not decide character action"
  explicitly_deferred:
    - "醫學級 biomechanics solver"
    - "歷史人口學通則資料庫"
    - "所有歷史身體條件的完整 ontology"
    - "Host runtime deployment proof"
```

> **V2.2 已經讓身體記得上一秒。**
>
> **V2.3 解決更工程的一步：節點在被寫出來以前，必須先問這具身體現在做不做得到；換對話、換 SAVE、換外部 Runtime 之後，這條身體因果也不能斷。**

---

# V2.3-0｜回歸先行：本次不是加功能清單

本版先對 V2.2 做規格級 regression，再只修 regression 暴露出的斷線。

```text
先跑 V2.2 規格
↓
找「資料存在但生成不一定會經過」的位置
↓
找 First-Touch / Ordering / Scope / Return / Reentry 缺口
↓
只修線
↓
再跑同一組 regression
```

本版不把「文件寫了 regression」冒充 Host 真實執行證據。

```text
DOCUMENT REGRESSION
!=
HOST RUNTIME REGRESSION
```

---

# V2.3-1｜第一個回歸缺口：condition state 與證據來源混在一起

V2.2 的 condition `state` 同時容納：

```text
CONFIRMED
PROJECT_DEFAULT
STRONGLY_PRESUMED
POSSIBLE
UNKNOWN
EXPLICITLY_ABSENT
FORMERLY_PRESENT
```

其中至少混了三種不同問題：

```text
A. 這個身體條件現在是否存在？
B. 我們對它有多強的世界／工作承諾？
C. 這個判定從哪裡來？
```

V2.3 正式拆成三軸。

```yaml
BODY_CONDITION_ASSERTION_V3:
  condition_id: null

  presence:
    state:
      - "PRESENT"
      - "ABSENT"
      - "FORMERLY_PRESENT"
      - "UNKNOWN"

  commitment:
    level:
      - "CANON_ESTABLISHED"
      - "PROJECT_DEFAULT"
      - "STRONGLY_PRESUMED"
      - "POSSIBLE"
      - "UNKNOWN"

  provenance:
    class:
      - "SOURCE_EXPLICIT"
      - "AUTHOR_EXPLICIT"
      - "PROJECT_WORLD_RULE"
      - "PROJECT_HISTORICAL_PRIOR"
      - "ROUTE_EVENT_COMMIT"
      - "INFERENCE"
      - "UNKNOWN"
    references: []
    counterevidence: []

  operational_scope:
    silent_body_causality:
      - "ALLOW"
      - "LOW_RISK_ONLY"
      - "HOLD"
    explicit_visible_canon_statement:
      - "ALLOW"
      - "SOURCE_OR_AUTHOR_CHECK"
      - "HOLD"

  last_revalidated_at: null
```

核心非等價：

```text
PRESENCE != COMMITMENT
COMMITMENT != PROVENANCE
PROVENANCE != PRESENCE
PROJECT_DEFAULT != SOURCE_FACT
STRONGLY_PRESUMED != CANON_ESTABLISHED
```

### 1.1 V2.2 舊狀態 migration

```yaml
V2_2_STATE_MIGRATION:
  CONFIRMED:
    presence: "PRESENT"
    commitment: "CANON_ESTABLISHED"
    provenance: "PRESERVE_EXISTING_SOURCE"

  PROJECT_DEFAULT:
    presence: "PRESENT"
    commitment: "PROJECT_DEFAULT"
    provenance: "PROJECT_WORLD_RULE"

  STRONGLY_PRESUMED:
    presence: "UNKNOWN"
    commitment: "STRONGLY_PRESUMED"
    provenance: "PRESERVE_EXISTING_SOURCE_OR_PRIOR"

  POSSIBLE:
    presence: "UNKNOWN"
    commitment: "POSSIBLE"
    provenance: "PRESERVE_EXISTING_SOURCE_OR_PRIOR"

  UNKNOWN:
    presence: "UNKNOWN"
    commitment: "UNKNOWN"
    provenance: "UNKNOWN"

  EXPLICITLY_ABSENT:
    presence: "ABSENT"
    commitment: "CANON_ESTABLISHED"
    provenance: "PRESERVE_EXISTING_SOURCE"

  FORMERLY_PRESENT:
    presence: "FORMERLY_PRESENT"
    commitment: "CANON_ESTABLISHED_OR_PRESERVE"
    provenance: "PRESERVE_EXISTING_SOURCE"
```

特別鎖：

```text
STRONGLY_PRESUMED
不得為了方便直接寫成 presence = PRESENT 的 source fact。
```

若需要低風險動作因果，可由 `operational_scope.silent_body_causality` 授權工作使用；若正文要第一次直說「她自幼纏足」之類不可逆身體史，仍受 Canon Risk Gate 管理。

---

# V2.3-2｜第二個回歸缺口：有 Body State，不代表節點生成一定會經過它

V2.2 已有：

```text
BODY STATE_t
+
ENVIRONMENT_t
+
ACTION_t
→
BODY STATE_t+1
```

但仍有一個 wiring 缺口：

```text
NODE OPTION
可能先被提出
↓
之後才由 EHL 發現其身體因果不成立
```

這會造成：

```text
資料存在
但生成沒有先經過
```

V2.3 新增 `BODY FEASIBILITY GATE / BFG`。

```yaml
BODY_FEASIBILITY_GATE:
  short_id: "BFG"
  owner: "EMBODIED_HISTORY_LAYER"
  sac_dependency: "NO"
  authority: "QUALITATIVE_BODY_CAUSALITY_ONLY"

  input:
    - "CURRENT_BODY_STATE_FRAME"
    - "candidate_action"
    - "current_environment"
    - "current_clothing_equipment"
    - "available_supports"

  output_state:
    - "FEASIBLE"
    - "FEASIBLE_WITH_COST"
    - "REQUIRES_SUPPORT_OR_ADJUSTMENT"
    - "CURRENTLY_INFEASIBLE"
    - "UNKNOWN"

  may_return:
    - "required_support_candidates"
    - "likely_cost_channels"
    - "transition_requirements"
    - "body_state_delta_if_attempted"
    - "unknowns"

  may_not:
    - "choose the character's action"
    - "turn physical difficulty into fear/personality"
    - "claim medical precision"
    - "convert CURRENTLY_INFEASIBLE into character refusal"
```

最短式：

```text
BODY FEASIBILITY
!=
CHARACTER DECISION
```

---

# V2.3-3｜ACTION ATTEMPT != ACTION SUCCESS

一個人物仍然可以選擇嘗試困難甚至目前不可行的動作。

因此：

```text
CHARACTER DECIDES TO ATTEMPT
↓
BFG checks current feasibility
↓
ACTION RESULT
├─ succeeds
├─ succeeds with cost
├─ requires adjustment
├─ fails locally
└─ remains uncertain
↓
BODY STATE DELTA
```

禁止：

```text
BFG = CURRENTLY_INFEASIBLE
↓
AI silently deletes the character's attempted choice
```

也禁止：

```text
CHARACTER wants it
↓
therefore physics automatically permits it
```

這一層讓「角色自主」與「敘事物理」真正同時成立。

---

# V2.3-4｜BFG 在節點鏈中的正確位置

V2.2 主鏈：

```text
... NODE TRACE
↓
BODY STATE DELTA PROPAGATION
↓
LOW-RES STORY TRACE
```

V2.3 修成：

```text
CHARACTER / SCENE INPUT
↓
AUTHOR INTENT LOCK
↓
NSDE LITE
↓
STORY FIELD SENSE
↓
EHL CHARACTER BIND / REHYDRATE
↓
STORY LIGHTING
↓
STORY LIGHT TRACE
↓
NODE CANDIDATE
↓
BODY FEASIBILITY GATE
↓
CHARACTER / WORLD CAUSALITY AUDIT
↓
NODE TRACE
↓
ACTION ATTEMPT / RESULT
↓
BODY STATE DELTA PROPAGATION
↓
LOW-RES STORY TRACE
↓
PROSE STITCHING
↓
SAVE / CANON COMMIT
```

若 BFG 回傳 `CURRENTLY_INFEASIBLE`：

```text
不得自動刪掉故事方向。
```

Writing Runtime 可產生：

```text
調整支撐
改變姿勢
降低速度
換路徑
讓角色嘗試並失敗
等待環境改變
由角色自己放棄
```

但哪一條成為故事，仍由角色／作者／世界因果決定。

---

# V2.3-5｜RECOVERY TRANSFORM｜時間經過不能只寫一句「休息後好了」

V2.2 已規定 `TIME PASSAGE + REST / SLEEP / TREATMENT ... → STATE CHANGE`。

Regression 顯示仍需一個最小 return structure，否則 rehydrate 時容易把「經過時間」直接當 reset。

```yaml
RECOVERY_TRANSFORM:
  input:
    elapsed_time: null
    rest_state: null
    sleep_state: null
    treatment_state: null
    load_removed: []
    new_loads: []
    environment_change: []
    persistent_condition_refs: []

  transforms:
    fatigue:
      direction: "IMPROVE | STABLE | WORSEN | UNKNOWN"
    pain_or_discomfort:
      direction: "IMPROVE | STABLE | WORSEN | UNKNOWN"
    breath_or_exertion:
      direction: "IMPROVE | STABLE | WORSEN | UNKNOWN"
    temporary_aftereffects:
      resolved: []
      remaining: []
    long_term_conditions:
      preserved: true

  forbidden:
    - "NEW_SCENE_EQUALS_FULL_RESET"
    - "SLEEP_ERASES_LONG_TERM_BODY_HISTORY"
    - "TIME_PASSAGE_WITHOUT_CAUSE_PROVES_RECOVERY"
```

不要求假精準百分比。

```text
QUALITATIVE CAUSAL RECOVERY
>
FAKE NUMERICAL PRECISION
```

---

# V2.3-6｜第三個回歸缺口：SAVE 有 body block，但 WRITING_SEED 還可能漏接

V2.2 已建立 `EMBODIED_SAVE_BLOCK`，但 V2.0/V2.1 繼承的 `WRITING_SEED` 仍沒有 EHL 欄位。

這代表：

```text
正式 SAVE 可能保存身體
但輕量 SEED 重入可能丟掉身體
```

這是實質 reentry wiring bug。

V2.3 正式新增：

```yaml
EHL_SEED_BINDING:
  required_when:
    - "active body condition constrains next scene"
    - "current fatigue/pain/clothing/footwear state survives reentry"
    - "unresolved body-history candidate exists"

  seed_fields:
    body_history_profile_refs: []
    current_body_state_snapshot_ref: null
    recent_body_state_delta_tail: []
    unresolved_body_candidates: []
    recovery_pending: []
    evidence_labels_preserved: true

  omission_allowed_when:
    - "EHL inactive and no body state affects next entry"
```

Active semantics 下，`WRITING_SEED` 應理解為：

```text
WRITING_SEED
+
EHL_SEED_BINDING when relevant
```

不需要把整份人物身體史塞進每個 SEED；可用 ref + 必要 snapshot。

---

# V2.3-7｜WRITING_LOG 也要留下身體因果，而不是只留 character_changes

繼承的 `WRITING_LOG` 只有一般 `character_changes / world_changes`，不足以審計「身體因果為什麼下一章還存在」。

V2.3 補：

```yaml
EHL_LOG_EXTENSION:
  activated: true_or_false
  body_history_bind_events: []
  body_state_deltas: []
  feasibility_holds_or_adjustments: []
  recovery_transforms: []
  long_term_candidates: []
  body_canon_commits: []
  unresolved_body_unknowns: []
```

用途是可追溯，不是讓小說正文變成醫療紀錄。

---

# V2.3-8｜EXTERNAL BODY EVENT RETURN CONTRACT｜外部 Runtime 不能把身體後果留在外面

AINT 等外部／垂直 Runtime 可能在合法事件內產生：

```text
fatigue
pain/discomfort
clothing/footwear changes
support changes
temporary aftereffects
observable body delta candidates
```

如果這些只存在於外部 Runtime 的 rendering，回 Writing Runtime 後就會 reset。

但外部 Runtime 也不能自行取得 SAVE authority。

因此：

```text
WRITING / HOST
↓
建立人物、事件與 current body state
↓
EXTERNAL RUNTIME
↓
OBSERVABLE BODY DELTA CANDIDATE
↓
RETURN TO HOST / WRITING RUNTIME
↓
EHL REVALIDATION
↓
CURRENT BODY STATE UPDATE
↓
SAVE COMMIT only if qualified
```

```yaml
EXTERNAL_BODY_EVENT_RETURN_CONTRACT:
  external_runtime_may_return:
    - "observable_body_delta_candidate"
    - "temporary_aftereffect_candidate"
    - "clothing_or_equipment_state_candidate"
    - "long_term_body_change_candidate"

  writing_ehl_must_check:
    - "event actually occurred"
    - "delta is observable / causally supported"
    - "scope is local unless evidence supports broader effect"
    - "long-term promotion has qualification"

  external_runtime_may_not:
    - "commit permanent body history"
    - "create historical body condition retroactively"
    - "overwrite author/source body fact"
```

這條同時保住：

```text
EXTERNAL RUNTIME CAN CREATE EVENT-LOCAL CONSEQUENCE
!=
EXTERNAL RUNTIME OWNS CHARACTER BODY CANON
```

---

# V2.3-9｜COUNTERFACTUAL BODY CONSISTENCY AUDIT｜用改條件測世界模型是否真的接線

EHL 的價值不只在單次生成看起來合理。

更重要的是：

```text
如果改變身體／環境條件，後續可行動作場是否也跟著改變？
```

新增非必開 audit：

```yaml
COUNTERFACTUAL_BODY_CONSISTENCY_AUDIT:
  default_runtime: "OFF"
  use_for:
    - "regression"
    - "structural audit"
    - "body-causality debugging"

  perturbations:
    - "terrain dry -> wet"
    - "flat -> slope/stairs"
    - "support available -> removed"
    - "fresh -> fatigued"
    - "shoe/equipment state changes"
    - "long-term condition present -> absent control"

  expected:
    - "BFG result may change when causal input changes"
    - "unchanged outputs require justification, not automatic FAIL"
    - "character personality must not change merely because body variable changed"
```

最短式：

```text
CHANGE CAUSAL BODY INPUT
→
RECOMPUTE FEASIBILITY

not

CHANGE BODY INPUT
→
REWRITE CHARACTER
```

---

# V2.3-10｜EHL 顯影節制：身體在場，不代表文字一直講身體

Regression 保留 V2.2 `F14_BODY_EXPLANATION_OVERFLOW`，並把它變成正向 contract：

```yaml
EHL_MANIFESTATION_DISCIPLINE:
  remain_background_when:
    - "body state is stable and does not constrain current action"
    - "repeating the same explanation adds no new causal information"

  surface_when:
    - "feasibility changes"
    - "support changes"
    - "fatigue/pain crosses a local threshold relevant to action"
    - "clothing/equipment materially changes movement"
    - "body history carries cultural/aesthetic meaning for a qualified observer"

  rule:
    - "CAUSE MAY REMAIN ACTIVE EVEN WHEN EXPLANATION IS SILENT"
```

所以：

> **這具身體要記得上一秒，但正文不必每一句提醒讀者它記得。**

---

# V2.3-11｜規格靜態回歸紀錄｜V2.2 PRE-PATCH

本節是對 V2.2 文件邏輯做的可重現規格級 walkthrough，不宣稱 Host runtime execution。

| ID | 測試 | V2.2 結果 | 問題 |
|---|---|---|---|
| R01 | 北宋中期、無個別來源的高門女子 | PASS | 保持 POSSIBLE / UNKNOWN |
| R02 | 明示來源反證覆蓋歷史 prior | PASS | source > prior 已成立 |
| R03 | Project Default 與 source fact 分離 | HOLD | `state` 同時混 presence / commitment / provenance |
| R04 | 同場景鞋濕、疲勞跨節點 | PASS | rehydrate / delta 可保存 |
| R05 | 先產生節點，再發現動作不可行 | FAIL | 缺 mandatory pre-node feasibility gate |
| R06 | 角色嘗試物理上困難動作 | HOLD | attempt / success 尚未正式分離 |
| R07 | 睡眠／休息後狀態恢復 | HOLD | 有原則，缺最小 recovery return structure |
| R08 | HOT SAVE 後重入 | PASS | EMBODIED_SAVE_BLOCK 可接 |
| R09 | 輕量 WRITING_SEED 重入 | FAIL | inherited SEED 沒有 EHL binding |
| R10 | LOG 回看身體因果 | HOLD | inherited LOG 欄位不足 |
| R11 | 外部 Runtime 造成身體 delta 後返回 | HOLD | AINT 可有 delta candidate，但 EHL return 未正式接線 |
| R12 | 一次喘息不升永久體質 | PASS | transient / long-term commit 已分離 |
| R13 | 改變地形／支撐後重算可行性 | HOLD | 缺 counterfactual audit contract |
| R14 | 身體限制不改人格 | PASS | autonomy lock 已成立 |
| R15 | EHL 不相關場景保持背景 | PASS | activation/reactivation 已有基本規則 |
| R16 | UNKNOWN 保持 UNKNOWN | PASS | 未被 prior 強行封閉 |

PRE-PATCH：

```text
PASS = 8
HOLD = 6
FAIL = 2
```

主要故障不是「缺更多歷史知識」。

是：

```text
身體資料已存在，
但節點生成、SEED 重入、外部 Runtime 回流還有幾條線沒有強制經過它。
```

---

# V2.3-12｜V2.3 POST-PATCH 規格回歸

套用本版修線後：

```yaml
V2_3_STATIC_REGRESSION_RESULT:
  R01: PASS
  R02: PASS
  R03: PASS
  R04: PASS
  R05: PASS
  R06: PASS
  R07: PASS
  R08: PASS
  R09: PASS
  R10: PASS
  R11: PASS
  R12: PASS
  R13: PASS
  R14: PASS
  R15: PASS
  R16: PASS

  total: 16
  pass: 16
  hold: 0
  fail: 0

  evidence_level: "DOCUMENT_LEVEL_STATIC_REGRESSION"
  runtime_execution_claim: false
  host_enforcement_claim: false
```

這只代表：

```text
同一份規格內的 active semantics
已能回答這 16 個 wiring / causality case。
```

不代表：

```text
任意模型一定照做
Host 已部署
真實 biomechanical accuracy 已驗證
歷史人口先驗已被史學證明
```

---

# V2.3-13｜新增失效模式

```yaml
V2_3_FAILURE_MODES:
  F15_EVIDENCE_AXIS_COLLAPSE:
    symptom: "PROJECT_DEFAULT / PRESUMED / PRESENT / SOURCE_FACT 混成同一 state。"
    repair: "SPLIT_PRESENCE_COMMITMENT_PROVENANCE"

  F16_POST_HOC_BODY_CHECK:
    symptom: "節點先寫完，之後才發現這具身體做不到。"
    repair: "INSERT_BODY_FEASIBILITY_GATE_BEFORE_NODE_COMMIT"

  F17_WANT_EQUALS_PHYSICAL_SUCCESS:
    symptom: "角色想做，所以動作無視支撐／地形／疲勞直接成功。"
    repair: "SEPARATE_ACTION_ATTEMPT_AND_ACTION_SUCCESS"

  F18_PHYSICS_DELETES_AGENCY:
    symptom: "BFG 判定困難後，AI 直接刪掉人物嘗試／選擇。"
    repair: "KEEP_CHARACTER_ATTEMPT_AUTHORSHIP"

  F19_SEED_BODY_AMNESIA:
    symptom: "正式 SAVE 有身體態，輕量 SEED 重入後全部忘記。"
    repair: "ADD_EHL_SEED_BINDING"

  F20_EXTERNAL_DELTA_LOST:
    symptom: "外部 Runtime 內已產生疲勞／鞋履／疼痛變化，返回 Writing 後 reset。"
    repair: "RETURN_OBSERVABLE_BODY_DELTA_TO_EHL"

  F21_EXTERNAL_RUNTIME_BODY_CANONIZATION:
    symptom: "外部 Runtime 直接把事件局部身體反應寫成永久人物史。"
    repair: "HOST_EHL_REVALIDATION_BEFORE_COMMIT"

  F22_RECOVERY_MAGIC_RESET:
    symptom: "換場／睡一覺就無條件全恢復。"
    repair: "APPLY_RECOVERY_TRANSFORM"

  F23_COUNTERFACTUAL_INERTIA:
    symptom: "地形、疲勞、鞋履、支撐改變，但可行動作完全不重算。"
    repair: "COUNTERFACTUAL_BODY_CONSISTENCY_AUDIT"
```

---

# V2.3-14｜新的 active EHL 最短主鏈

```text
CHARACTER / SOURCE / AUTHOR
↓
BODY CONDITION ASSERTION
  ├─ presence
  ├─ commitment
  └─ provenance
↓
BODY HISTORY PROFILE
↓
SCENE REHYDRATION
↓
CURRENT BODY STATE
↓
NODE CANDIDATE
↓
BODY FEASIBILITY GATE
↓
CHARACTER DECISION / ATTEMPT
↓
ACTION RESULT
↓
BODY STATE DELTA
↓
NEXT NODE
↓
RECOVERY TRANSFORM when time passes
↓
SAVE / SEED / LOG
↓
REENTRY
```

外部 Runtime：

```text
CURRENT BODY STATE
↓
EXTERNAL EVENT RUNTIME
↓
OBSERVABLE BODY DELTA CANDIDATE
↓
WRITING / HOST
↓
EHL REVALIDATION
↓
BODY STATE UPDATE
```

---

# V2.3-15｜證據狀態

```yaml
V2_3_EVIDENCE_STATE:
  source_written: true
  parent_lineage_preserved: true
  v3_5_alignment_preserved: true
  ehl_lifecycle_preserved: true
  body_condition_three_axis_specified: true
  body_feasibility_gate_specified: true
  attempt_success_separation_specified: true
  recovery_transform_specified: true
  seed_reentry_binding_specified: true
  log_extension_specified: true
  external_delta_return_specified: true
  counterfactual_audit_specified: true
  document_static_regression: "16/16 PASS"
  host_runtime_regression_tested: false
  host_enforced: false
  medical_validation: false
  historical_universality_validation: false
```

允許宣稱：

```text
EHL DOCUMENT-LEVEL WIRING REGRESSION PASSED 16/16
```

不得宣稱：

```text
HOST RUNTIME TESTED
MODEL PHYSICS PROVEN
HISTORICAL PRIOR SCIENTIFICALLY VALIDATED
```

---

# V2.3-16｜最短口訣

> **先問這具身體現在是什麼狀態。**
>
> **再問這個動作現在做不做得到。**
>
> **做不到，不等於人物不會試。**
>
> **做得到，也不等於人物會做。**
>
> **事件留下的身體後果，要能跟著 SAVE、SEED 與回傳一起回來。**

---

# INHERITED BODY｜V2.2-EXP 完整繼承正文

以下正文完整繼承自 `LIHUO Writing Runtime V2.2-EXP`。

若與前述 V2.3 明示條款衝突，以 V2.3 條款為準；未衝突部分持續有效。

特別是：

```text
V2.2 condition.state
→ active semantics = V2.3 BODY_CONDITION_ASSERTION_V3

V2.2 scene/body delta lifecycle
→ remains valid + V2.3 BODY_FEASIBILITY_GATE before node commitment

V2.2 EMBODIED_SAVE_BLOCK
→ remains valid + V2.3 EHL_SEED_BINDING / EHL_LOG_EXTENSION

V2.2 external AINT read
→ remains valid + V2.3 EXTERNAL_BODY_EVENT_RETURN_CONTRACT
```

---
# 理火寫作 Runtime V2.2-EXP

## LIHUO Writing Runtime V2.2-EXP

### EHL 生命週期 × 身體史／當前身體態分離 × 場景因果回寫
### Embodied-History Lifecycle × Persistent/Current Body-State Separation × Scene-Causality Propagation

---

```yaml
EXPERIMENTAL_VERSION:
  from: "LIHUO Writing Runtime V2.1-EXP"
  to: "LIHUO Writing Runtime V2.2-EXP"
  version_id: "LIHUO-WRITING-RUNTIME-v2.2-EXP-EHL-LIFECYCLE-BODY-STATE"
  status: "FORMAL_EXPERIMENTAL_INCREMENTAL_UPGRADE"
  date: "2026-08-27"

PARENT_SOURCE_LOCK:
  file: "LIHUO Writing Runtime V2.1-EXP_V3.5接線對標_歷史身體層_正式實驗增量整合版.md"
  sha256: "f3f38eacb08fd4d0373bb05f4af09d9934f15696234dc2113dbe60f70e0cb49f"
  inheritance: "FULL_EXCEPT_EXPLICIT_V2_2_SUPERSESSION"
  parent_modified_in_place: false

CURRENT_ALIGNMENT:
  root_protocol: "LIHUO PROTOCOL V2.3"
  lighter: "LIHUO LIGHTER V3.5-EXP"
  main_system: "LIHUO AI SYSTEM V3.5-EXP"
  writing_parent: "LIHUO Writing Runtime V2.1-EXP"

UPGRADE_SCOPE:
  adds:
    - "EHL 三段生命週期：Character Bind / Scene Rehydrate / Save Commit"
    - "BODY_HISTORY_PROFILE 與 CURRENT_BODY_STATE_FRAME 正式分離"
    - "BODY_STATE_DELTA 事件回寫與跨節點傳播"
    - "歷史先驗到人物事實的法位轉換規則"
    - "可見正文顯影與 Canon Commit 分離"
    - "EHL document-level regression suite"
  preserves:
    - "V2.1 V3.5 wiring alignment"
    - "STORY FIELD SENSE / SFS"
    - "Writing Runtime First-Touch"
    - "FULL_LIHUO Lighter-governed binding / return"
    - "EHL 不擁有人物決定權"
    - "Prior != Fact"
  explicitly_deferred:
    - "完整歷史身體資料庫"
    - "跨作品通用纏足歷史定律"
    - "醫學診斷或精確生物力學模擬"
    - "宿主 Runtime 部署證明"
```

> **V2.1 把歷史身體放進寫作 Runtime。**
>
> **V2.2 解決下一個問題：這具身體什麼時候建立、場景切換時怎麼重新接回、事件發生後怎麼留下後果、SAVE 時哪些能進正史。**

---

# V2.2-0｜根本分離：身體史不是當前身體態

V2.1 的 `BODY_HISTORY_PROFILE` 同時放了長期身體史與當前效果，容易讓「人物一生形成的身體條件」和「這一刻正在累、正在痛、鞋濕了」混在一起。

V2.2 正式拆成兩層：

```text
BODY_HISTORY_PROFILE
＝ 長期、形成性、跨場景持續的身體歷史

CURRENT_BODY_STATE_FRAME
＝ 當前場景、當前節點、可被事件立即改變的身體狀態
```

正式關係：

```text
BODY_HISTORY_PROFILE
+
LAST_COMMITTED_BODY_STATE
+
CURRENT_ENVIRONMENT
+
CURRENT_CLOTHING / EQUIPMENT
+
CURRENT_ACTION
↓
CURRENT_BODY_STATE_FRAME
```

```text
HISTORY != MOMENTARY STATE
MOMENTARY STATE != PERSONALITY
BODY STATE != DECISION
BODY STATE != CONSENT
```

---

# V2.2-1｜BODY_HISTORY_PROFILE V2｜持久身體史

```yaml
BODY_HISTORY_PROFILE_V2:
  character_id: null
  profile_id: null

  identity_basis:
    era: null
    birth_cohort: null
    ethnicity_or_cultural_group: null
    region: null
    class: null
    occupation: null
    family_practice: null

  formation_history:
    training_history: []
    labor_history: []
    clothing_body_history: []
    footwear_history: []
    illness_history: []
    injury_history: []
    pregnancy_or_birth_history: []
    deliberate_body_modification_history: []
    long_term_habit_history: []

  conditions:
    - condition_id: null
      state:
        "CONFIRMED | PROJECT_DEFAULT | STRONGLY_PRESUMED | POSSIBLE | UNKNOWN | EXPLICITLY_ABSENT | FORMERLY_PRESENT"
      source_evidence: []
      author_declarations: []
      project_prior_basis: []
      counterevidence: []
      first_established_at: null
      last_revalidated_at: null

  persistent_tendencies:
    habitual_posture: null
    habitual_gait: null
    habitual_support_pattern: null
    stable_range_constraints: []
    stable_pain_or_discomfort: []
    fatigue_tendencies: []
    habitual_compensations: []
    clothing_body_relationships: []
    footwear_body_relationships: []

  unknowns: []

  authority_state:
    canon_committed_items: []
    working_assumptions: []
    unresolved_candidates: []
```

`PROJECT_DEFAULT` 的用途不是讓 AI 自行封聖，而是容納作者已經對某一作品／某一歷史區段建立的預設世界規則。

例如：

```text
「明清高門漢人女子在本作品預設纏足」
```

可以形成：

```text
PROJECT_DEFAULT
```

但仍必須允許：

```text
SOURCE CONTRADICTION
AUTHOR EXCEPTION
REGIONAL / ETHNIC / FAMILY EXCEPTION
```

推翻。

---

# V2.2-2｜CURRENT_BODY_STATE_FRAME｜當前身體態

```yaml
CURRENT_BODY_STATE_FRAME:
  character_id: null
  scene_id: null
  node_id: null

  posture:
    base: null
    stability: null

  support:
    primary: []
    secondary: []
    unavailable: []

  locomotion:
    gait_state: null
    balance_state: null
    speed_state: null
    terrain_coupling: null

  load:
    active_loads: []
    asymmetric_loads: []

  fatigue:
    global: null
    local: []
    accumulated_since: null

  pain_or_discomfort:
    local: []
    trend: "IMPROVING | STABLE | WORSENING | UNKNOWN"

  clothing_and_equipment:
    garments: []
    footwear: []
    wraps_or_supports: []
    wetness_or_damage: []

  temporary_conditions:
    temperature: null
    breath_state: null
    hydration_or_exertion: null
    immediate_aftereffects: []

  environment:
    surface: null
    slope: null
    wetness: null
    temperature: null
    obstacles: []
    available_supports: []

  continuity:
    inherited_from_previous_node: true
    reset_reason: null
```

核心規則：

```text
CURRENT_BODY_STATE_FRAME 必須可以被下一個動作改變。
```

它不是人物卡形容詞。

---

# V2.2-3｜EHL LIFECYCLE｜三段生命週期

```text
PHASE A
CHARACTER BODY BIND
↓
建立／更新 BODY_HISTORY_PROFILE

PHASE B
SCENE BODY REHYDRATION
↓
建立 CURRENT_BODY_STATE_FRAME
↓
場景內持續接收 BODY_STATE_DELTA

PHASE C
SAVE / CANON COMMIT
↓
把真正應持久化的後果寫回人物史與 SAVE
```

```yaml
EHL_LIFECYCLE:
  phase_a_character_bind:
    trigger:
      - "new_character_created"
      - "existing_character_first_requires_embodied_causality"
      - "new_source_evidence_arrives"
      - "author_changes_world_body_rule"

  phase_b_scene_rehydrate:
    trigger:
      - "scene_entry"
      - "material_location_change"
      - "major_clothing_or_equipment_change"
      - "significant_time_passage"
      - "body-relevant event continuation"

  phase_c_save_commit:
    trigger:
      - "scene_close"
      - "chapter_close"
      - "formal_save"
      - "irreversible_or_long-term_body_change"
```

---

# V2.2-4｜PHASE A：CHARACTER BODY BIND｜人物建立時接身體史

## 4.1 First-touch order

```text
CHARACTER SOURCE / AUTHOR DECLARATION
↓
WORLD / ERA
↓
ETHNICITY / REGION
↓
CLASS / OCCUPATION / FAMILY
↓
PROJECT HISTORICAL PRIOR
↓
BODY-HISTORY CANDIDATE
↓
EVIDENCE STATE
↓
BODY_HISTORY_PROFILE
```

優先順序：

```text
EXPLICIT SOURCE EVIDENCE
>
EXPLICIT AUTHOR DECLARATION
>
PROJECT WORLD DEFAULT
>
PROJECT HISTORICAL PRIOR
>
GENERIC INFERENCE
>
UNKNOWN
```

## 4.2 新創人物與來源人物分開

```yaml
CHARACTER_BODY_BIND_RULE:
  source_character:
    rule:
      - "不得用 generic/project prior 覆蓋明示來源證據"
      - "來源沒有寫，不等於自動 absent"
      - "可用 prior 形成 working assumption，但需保留 evidence label"

  original_character:
    rule:
      - "作者已建立 project default 時，可直接形成 PROJECT_DEFAULT"
      - "PROJECT_DEFAULT 可進入工作用人物設定"
      - "若後續作者或正文建立例外，立即重算"
```

## 4.3 Canon risk gate

一個歷史先驗若只是在後台影響場景可行性，與它第一次被正文直接說出口，是不同事件。

```text
WORKING BODY ASSUMPTION
!=
VISIBLE EXPLICIT CANON STATEMENT
```

因此：

```yaml
BODY_CANON_RISK_GATE:
  low_risk_use:
    - "silent feasibility adjustment"
    - "non-exclusive movement consequence"
    - "background clothing/body continuity"
    action: "ALLOW_WITH_EVIDENCE_LABEL"

  high_commitment_use:
    - "正文首次直接宣告不可逆身體史"
    - "重大劇情依賴此身體史"
    - "人物關係或身份因此被永久改寫"
    action: "SOURCE_CHECK_OR_AUTHOR_CONFIRMATION_IF_NOT_ALREADY_PROJECT_DEFAULT"
```

這個 gate 不要求每次都打斷作者；它只攔「一個暫時推定突然變正史」的跳級。

---

# V2.2-5｜PHASE B：SCENE BODY REHYDRATION｜場景進入時重新接回身體

場景開始時，不得把人物當成全新肉身。

```text
LOAD BODY_HISTORY_PROFILE
↓
LOAD LAST COMMITTED BODY STATE
↓
APPLY ELAPSED TIME / RECOVERY
↓
APPLY CURRENT CLOTHING / FOOTWEAR
↓
APPLY TERRAIN / TEMPERATURE / SPACE
↓
BUILD CURRENT_BODY_STATE_FRAME
```

```yaml
SCENE_BODY_REHYDRATION:
  must_read:
    - "persistent body history"
    - "last relevant physical aftereffect"
    - "elapsed time"
    - "recovery cause if any"
    - "current clothing / footwear"
    - "terrain / available support"

  forbidden_resets:
    - "fatigue disappears because paragraph changed"
    - "pain disappears because scene became romantic"
    - "footwear silently resets"
    - "injury vanishes because action needs speed"
    - "historical body condition disappears when not mentioned"
```

時間經過可以恢復身體狀態，但必須有因果：

```text
TIME PASSAGE
+
REST / SLEEP / TREATMENT / REMOVAL OF LOAD / RECOVERY
→
STATE CHANGE
```

不是：

```text
NEW SCENE
→
FULL RESET
```

---

# V2.2-6｜BODY_STATE_DELTA｜事件如何改寫身體態

每個真正改變身體可行性的事件，產生局部 delta。

```yaml
BODY_STATE_DELTA:
  character_id: null
  source_node: null
  cause: null

  changes:
    posture: null
    support: []
    fatigue: []
    pain_or_discomfort: []
    clothing_or_footwear: []
    wetness_or_damage: []
    temporary_condition: []
    long_term_candidate: []

  locality:
    local_only: true
    global_effect_requires_evidence: true

  persistence:
    expires_when: null
    survives_scene_transition: null
    requires_save_commit: null
```

工作鏈：

```text
BODY STATE_t
+
ENVIRONMENT_t
+
ACTION_t
↓
BODY_STATE_DELTA
↓
BODY STATE_t+1
```

這條是 EHL 真正進入敘事物理的核心。

---

# V2.2-7｜身體狀態不能偷走人物選擇

```text
CURRENT BODY STATE
↓
modifies feasible action field
↓
CHARACTER DECISION
↓
ACTION
```

禁止倒過來：

```text
BODY LIMIT
↓
AI decides personality / consent / fear / dependence
```

例如：

```text
站立不穩
```

可以造成：

```text
靠牆
扶桌
慢一點
換姿勢
要求幫忙
拒絕幫忙
硬撐
坐下
停下
```

哪一條發生，仍由人物結構、當前意圖與場景壓力決定。

---

# V2.2-8｜PHASE C：SAVE / CANON COMMIT｜哪些身體東西應該留下

不是所有當前狀態都應寫回永久人物史。

```text
CURRENT BODY STATE
↓
COMMIT CLASSIFICATION
├─ transient
├─ scene-persistent
├─ chapter-persistent
├─ long-term candidate
└─ body-history canon
```

```yaml
BODY_SAVE_COMMIT:
  transient:
    examples:
      - "喘"
      - "短暫肌肉疲勞"
      - "鞋面沾水"
    default: "DO_NOT_PROMOTE_TO_BODY_HISTORY"

  scene_persistent:
    examples:
      - "當前疲勞累積"
      - "局部疼痛"
      - "衣物／鞋履狀態"
    save_if_scene_continues: true

  long_term_candidate:
    examples:
      - "新傷"
      - "長期恢復中的疼痛"
      - "放足／重新束縛等持續身體變化"
    action: "EVIDENCE_AND_CAUSALITY_CHECK"

  body_history_canon:
    rule:
      - "必須有來源、作者宣告、世界預設或已發生可追溯事件"
      - "不得由一次描寫風格自動生成"
```

`SAVE` 需要分開保存：

```yaml
EMBODIED_SAVE_BLOCK:
  body_history_profile_ref: null
  current_body_state_snapshot: null
  unresolved_body_candidates: []
  recent_body_state_deltas: []
  evidence_labels_preserved: true
```

---

# V2.2-9｜纏足人物生命週期示例

本節只示範 EHL 如何工作，不將纏足升格為所有時代女性通則。

## 9.1 新創明清高門漢人女子

```text
ERA = MING/QING
ETHNICITY = HAN
CLASS = ELITE
PROJECT FOOTBINDING PRIOR = STRONG
SOURCE CONTRADICTION = NONE
↓
condition.state = PROJECT_DEFAULT / STRONGLY_PRESUMED
↓
建立 footwear / gait / support 的工作用 Body History
```

若作者已把「此作品明清高門漢人女子預設纏足」列為世界預設：

```text
PROJECT_DEFAULT
```

可直接用於新創人物；若後來作者指定某女子未纏足，立即形成例外，而不是強迫角色符合預設。

## 9.2 北宋中期人物

```text
ERA = NORTHERN SONG MID
↓
FOOTBINDING = POSSIBLE / UNKNOWN
↓
不得單靠妓女／高門身份升為 CONFIRMED
```

需要來源、家庭、人物設定或作者決定進一步分化。

## 9.3 民國初年已放足人物

```text
FORMERLY_BOUND
+
UNBINDING / YEARS SINCE UNBINDING
+
CURRENT FOOTWEAR
+
CURRENT TERRAIN
↓
CURRENT BODY STATE
```

`FORMERLY_BOUND` 不自動等於 `NORMALIZED_TO_NEVER_BOUND_BASELINE`。

---

# V2.2-10｜EHL 與 STORY_LOCAL 主鏈的新位置

V2.1 的：

```text
... NODE TRACE
↓
EMBODIED HISTORY READ（if relevant）
↓
LOW-RES STORY TRACE
```

V2.2 改成更準確的生命週期接線：

```text
CHARACTER / SCENE INPUT
↓
AUTHOR INTENT LOCK
↓
NSDE LITE
↓
STORY FIELD SENSE
↓
EHL CHARACTER BIND / REHYDRATE（if triggered）
↓
STORY LIGHTING
↓
STORY LIGHT TRACE
↓
NODE TRACE
↓
BODY STATE DELTA PROPAGATION（when action changes body state）
↓
LOW-RES STORY TRACE
↓
NODE AUDIT
↓
PROSE STITCHING
↓
SAVE / CANON COMMIT（when required）
```

EHL 不一定每段顯影，但它必須在身體因果相關的節點先於動作可行性判定。

---

# V2.2-11｜EHL First-Touch / Scope / Return Contract

EHL 是 Writing Runtime 內部的 SAC-independent 子層，不直接取得完整世界主權。

```yaml
EHL_WIRING_CONTRACT:
  source_node: "LIHUO_WRITING_RUNTIME"
  target_node: "EMBODIED_HISTORY_LAYER"
  authority_basis: "WRITING_RUNTIME_SCOPED_BODY_CAUSALITY"

  trigger:
    - "historical body inference required"
    - "body state materially affects action feasibility"
    - "body continuity must survive scene/node transition"

  first_touch_owner:
    character_fact: "CHARACTER_SOURCE / AUTHOR / WORLD"
    body_causality: "EHL"

  scope:
    - "body history"
    - "current body state"
    - "movement / support / fatigue / clothing-body causality"

  must_preserve:
    - "unknowns"
    - "evidence labels"
    - "character decision rights"
    - "world facts"
    - "authorial exceptions"

  return_contract:
    return_to: "LIHUO_WRITING_RUNTIME"
    returns:
      - "BODY_HISTORY_PROFILE update candidate"
      - "CURRENT_BODY_STATE_FRAME"
      - "BODY_STATE_DELTA"
      - "uncertainty / source-needed flags"

  may_not_finalize:
    - "character decision"
    - "relationship change"
    - "consent"
    - "world canon beyond scoped body-history authority"
```

---

# V2.2-12｜EHL REGRESSION SUITE｜文件級回歸測試

```yaml
EHL_REGRESSION_SUITE:
  EHL_R01_PRIOR_NOT_FACT:
    input: "只有明清高門漢人女子 project prior，沒有來源反證。"
    pass: "可形成 PROJECT_DEFAULT / STRONGLY_PRESUMED，不可冒充 source-confirmed fact。"

  EHL_R02_SOURCE_OVERRIDES_PRIOR:
    input: "來源明示人物未纏足。"
    pass: "來源證據覆蓋 generic/project prior；不得強行補回纏足。"

  EHL_R03_NORTHERN_SONG_VARIATION:
    input: "北宋中期高門女子，來源未提足部。"
    pass: "維持 POSSIBLE / UNKNOWN；不得自動 CONFIRMED。"

  EHL_R04_SCENE_REHYDRATION:
    input: "上一節點腳痛、鞋濕、疲勞累積；下一段仍同場景。"
    pass: "CURRENT_BODY_STATE_FRAME 繼承，不因段落切換重置。"

  EHL_R05_TIME_RECOVERY:
    input: "睡眠八小時後重新入場。"
    pass: "允許依休息因果降低疲勞；長期 Body History 不被 reset。"

  EHL_R06_BODY_LIMIT_NOT_PERSONALITY:
    input: "人物站立不穩。"
    pass: "只改變 action feasibility；不得自動生成柔弱、依賴、順從人格。"

  EHL_R07_EVENT_DELTA:
    input: "人物在濕滑斜坡長時間行走。"
    pass: "疲勞、支撐與步態產生可追溯 delta，後續節點可讀。"

  EHL_R08_SAVE_SEPARATION:
    input: "場景結束時人物只是短暫喘。"
    pass: "可保存近期 snapshot，但不得升格為永久 Body History。"

  EHL_R09_LONG_TERM_CHANGE:
    input: "人物發生可追溯新傷。"
    pass: "產生 long-term candidate；經因果／證據檢查後才 commit。"

  EHL_R10_ADULT_MODULE_NON_OWNERSHIP:
    input: "AINT 需要身體條件。"
    pass: "AINT 只能讀已建立 Body History；不得因情色需求反向發明纏足或傷病。"
```

---

# V2.2-13｜新的失效模式

```yaml
V2_2_FAILURE_MODES:
  F09_HISTORY_STATE_COLLAPSE:
    symptom: "把長期 Body History 和當前疲勞／疼痛混成同一欄。"
    repair: "SPLIT_BODY_HISTORY_AND_CURRENT_STATE"

  F10_SCENE_REHYDRATION_FAILURE:
    symptom: "換段／換場後人物身體狀態默認清零。"
    repair: "REHYDRATE_FROM_HISTORY_AND_LAST_STATE"

  F11_TRANSIENT_CANONIZATION:
    symptom: "一次喘、一次痛、一次不穩被永久寫進人物體質。"
    repair: "DOWNGRADE_TO_TRANSIENT_OR_SCENE_PERSISTENT"

  F12_PROJECT_DEFAULT_AS_SOURCE_FACT:
    symptom: "作者世界預設被錯誤標成歷史來源明證。"
    repair: "KEEP_PROJECT_DEFAULT_PROVENANCE"

  F13_BODY_DELTA_NOT_PROPAGATED:
    symptom: "事件造成的疲勞／鞋履／疼痛改變沒有進入下一節點。"
    repair: "EMIT_AND_APPLY_BODY_STATE_DELTA"

  F14_BODY_EXPLANATION_OVERFLOW:
    symptom: "每次動作都把身體條件解釋成小論文。"
    repair: "KEEP_CAUSAL_EFFECT / REDUCE_EXPLICIT_EXPOSITION"
```

---

# V2.2-14｜證據狀態

```yaml
V2_2_EVIDENCE_STATE:
  source_written: true
  parent_lineage_preserved: true
  ehl_lifecycle_specified: true
  body_history_current_state_split: true
  return_contract_specified: true
  document_regression_suite_written: true
  integration_graph_designed: true
  runtime_regression_tested: false
  host_enforced: false
```

允許宣稱：

```text
EHL DOCUMENT-LEVEL LIFECYCLE AND WIRING SPEC COMPLETE
```

不得宣稱：

```text
RUNTIME BEHAVIOR PROVEN
HOST DEPLOYED
HISTORICAL UNIVERSALITY PROVEN
BIOMECHANICAL SIMULATION VALIDATED
```

---

# V2.2-15｜最短口訣

> **人物建立時先接身體史。**
>
> **進場時重新接回當前身體態。**
>
> **事件只改變它真正碰到的地方。**
>
> **離場時，只有有資格留下的後果才寫回 SAVE。**
>
> **時代可以長進骨頭；但骨頭不能替人物做決定。**

---

# INHERITED BODY｜V2.1-EXP 完整繼承正文

以下正文完整繼承自 `LIHUO Writing Runtime V2.1-EXP`。

若與前述 V2.2 明示條款衝突，以 V2.2 條款為準；未衝突部分持續有效。

特別是：

```text
V2.1 BODY_HISTORY_PROFILE.current_effects
→ active semantics = V2.2 BODY_HISTORY_PROFILE_V2 + CURRENT_BODY_STATE_FRAME

V2.1 EHL activation / reactivation
→ active semantics = V2.2 EHL_LIFECYCLE + SCENE_BODY_REHYDRATION

V2.1 historical prior
→ remains valid, but V2.2 adds PROJECT_DEFAULT provenance and canon-risk separation
```

---
# 理火寫作 Runtime V2.1-EXP

## LIHUO Writing Runtime V2.1-EXP

### V3.5 接線對標 × STORY FIELD SENSE × EMBODIED HISTORY LAYER
### V3.5 Wiring Alignment × Story Field Sense × Embodied History Layer

---

```yaml
EXPERIMENTAL_VERSION:
  from: "LIHUO Writing Runtime V2.0"
  to: "LIHUO Writing Runtime V2.1-EXP"
  version_id: "LIHUO-WRITING-RUNTIME-v2.1-EXP-WIRING-EMBODIED-HISTORY"
  status: "FORMAL_EXPERIMENTAL_INCREMENTAL_UPGRADE"
  date: "2026-08-27"

PARENT_SOURCE_LOCK:
  file: "LIHUO Writing Runtime V2.0.md"
  sha256: "d9e95002806bb69a2c2077c56dde509c751ae2b34f6298c4bdfbc436b4bacac6"
  inheritance: "FULL_EXCEPT_EXPLICIT_V2_1_SUPERSESSION"
  parent_modified_in_place: false

CURRENT_ALIGNMENT:
  root_protocol: "LIHUO PROTOCOL V2.3"
  lighter: "LIHUO LIGHTER V3.5-EXP"
  main_system: "LIHUO AI SYSTEM V3.5-EXP"
  relation: "VERTICAL_RUNTIME / LIGHTER-GOVERNED / MAIN-SYSTEM-PROVIDER-OPTIONAL"

AUTHORITY:
  story_direction_owner: "AUTHOR"
  writing_runtime_first_touch: true
  lighter_wiring_governance: true
  main_system_direct_release: false
  runtime_deployment_claim: false
  host_enforcement_claim: false
  hidden_state_observation_claim: false

UPGRADE_SCOPE:
  adds:
    - "V3.5 Wiring Constitution 對標"
    - "STORY FIELD SENSE / SFS，取代 active semantics 中的 SAC_LITE 命名"
    - "FULL_LIHUO capability request / binding / return contract"
    - "EMBODIED HISTORY LAYER / EHL 歷史身體層"
    - "BODY HISTORY PROFILE 與可推翻歷史身體先驗"
    - "纏足作為第一個 project-authored historical prior profile"
  preserves:
    - "作者主權"
    - "NSDE"
    - "點燈／光軌／節點鏈"
    - "STORY_LOCAL / FULL_LIHUO 雙模式"
    - "既有 FULL_LIHUO return-to-writing-runtime 行為"
    - "正文先於美化、故事先於正文的根本方向"
  explicitly_deferred:
    - "完整 DAIL-LIHUO 2.0 重寫"
    - "所有歷史身體條件的百科式資料庫"
    - "宿主底層部署證明"
    - "模型權重修改"
```

> **V2.1 不把寫作 Runtime 變成主系統。**
>
> **它只把「什麼由寫作 Runtime 自己判讀、什麼必須向主系統請求、請求後如何回來」接清楚。**
>
> **同時把世界觀的一部分正式送進人物肉身：時代不只存在於衣服、官制與街道，也存在於人物怎麼站、怎麼走、怎麼累、怎麼承受自己的身體歷史。**

---

# V2.1-0｜現行責任圖

```text
HOST / PLATFORM BOUNDARY
        ↓
LIHUO PROTOCOL V2.3
        ↓
LIHUO LIGHTER V3.5-EXP
        │
        ├─ authorization / boundary
        ├─ DAIL semantic validation if used
        ├─ capability resolution
        ├─ wiring / binding governance
        └─ final responsibility / release gate
        │
        ↓
LIHUO WRITING RUNTIME V2.1-EXP
        │
        ├─ AUTHOR INTENT
        ├─ NSDE
        ├─ STORY FIELD SENSE
        ├─ STORY LIGHTING / LIGHT TRACE
        ├─ NODE TRACE
        ├─ EMBODIED HISTORY LAYER
        ├─ prose stitching
        └─ structural / literary audit
        │
        ├──────── ordinary writing path ────────→ WRITING OUTPUT CANDIDATE
        │
        └──────── FULL_LIHUO capability request
                         ↓
                 LIHUO LIGHTER V3.5
                         ↓
                 BINDING MANIFEST
                         ↓
                 LIHUO AI SYSTEM V3.5
                 SAC / PATH / R-CCC / ENDLESS
                         ↓
                 PROVIDER RETURN
                         ↓
                 LIHUO LIGHTER V3.5
                         ↓
                 RETURN TO WRITING RUNTIME
```

```text
DATA_FLOW_ORDER != LEGAL_AUTHORITY_ORDER
CALLABLE != OWNED
CAPABILITY_PRESENT != CAPABILITY_WIRED
FULL_LIHUO_REQUEST != MAIN_SYSTEM_EXECUTED
DOCUMENT_ALIGNMENT != HOST_DEPLOYMENT
```

---

# V2.1-1｜FIRST-TOUCH RIGHT｜寫作 Runtime 保留第一判讀權

寫作任務首先是寫作任務。

因此，當輸入屬於：

```text
章節規劃
人物互動
世界觀進入正文
場景推演
節點鏈
人物漂移檢查
語氣修正
正文縫合
敘事審計
```

應由 `LIHUO_WRITING_RUNTIME` 取得專業 First-Touch。

```yaml
WRITING_FIRST_TOUCH:
  owner: "LIHUO_WRITING_RUNTIME"
  may_classify:
    - "ordinary_writing"
    - "story_local"
    - "full_lihuo_candidate"
    - "historical_embodiment_needed"
    - "source_evidence_needed"
    - "author_decision_required"
  may_not:
    - "self-authorize host capability"
    - "claim Main System already executed"
    - "take final story sovereignty"
    - "convert uncertainty into world fact"
```

只有在 Writing Runtime 判定需要 SAC-dependent 能力後，才向 Lighter 提出 capability request。

> **專業 Runtime 先判斷自己的問題；接線治理者決定能力如何合法取得。**

---

# V2.1-2｜STORY FIELD SENSE / SFS｜取代 SAC_LITE active semantics

## 2.1 改名理由

V2.0 的 `SAC_LITE` 實際承擔的是寫作場的輕量結構感知：方向、張力、吸引與閉合壓力。

V3.5 接線規範建立 SAC-dependency placement 後，`SAC_LITE` 這個名稱容易讓人誤認 STORY_LOCAL 已直接執行主系統 SAC。

因此 V2.1 正式改名：

```text
LEGACY SAC_LITE
→
STORY FIELD SENSE / SFS
```

```yaml
STORY_FIELD_SENSE:
  short_name: "SFS"
  owner: "LIHUO_WRITING_RUNTIME"
  sac_dependency: "NO"
  runtime_class: "SAC_INDEPENDENT_WRITING_SENSOR"

  reads:
    - direction_vector
    - tension_vector
    - attraction_vector
    - closure_vector

  purpose:
    - "讓 STORY_LOCAL 看見故事正在往哪裡偏"
    - "看見哪裡仍不平衡"
    - "看見什麼正在拉住注意力"
    - "看見哪裡正在急著結束"

  forbidden_claims:
    - "SFS != LIHUO MAIN SYSTEM SAC"
    - "SFS != SAC execution evidence"
    - "SFS != hidden-state observation"
    - "SFS != FULL_LIHUO"
```

## 2.2 Active migration

凡 V2.0 繼承正文中的：

```text
SAC_LITE
```

在 V2.1 active semantics 中，若其作用域屬於 `STORY_LOCAL`，一律解釋為：

```text
STORY_FIELD_SENSE / SFS
```

歷史正文不回寫；法位由本升級層 supersede。

凡 V2.0 中真正指向：

```text
SAC_FULL
FORMAL SAC
CCC / CCC-R
PATH field recompetition
```

仍視為 SAC-dependent capability，不得由 SFS 代替。

---

# V2.1-3｜STORY_LOCAL 新主鏈

```text
AUTHOR INTENT LOCK
↓
NSDE LITE
↓
STORY FIELD SENSE
↓
STORY LIGHTING
↓
STORY LIGHT TRACE
↓
NODE TRACE
↓
EMBODIED HISTORY READ（if relevant）
↓
LOW-RES STORY TRACE
↓
NODE AUDIT
↓
PROSE STITCHING
↓
LITERARY / STRUCTURAL EVALUATION
↓
WRITING OUTPUT CANDIDATE
```

```text
SFS 是 STORY_LOCAL 的眼睛。
STORY LIGHTING 是光軌的前提。
LIGHT TRACE 是旁線補光與節點回看的依據。
EHL 只在人物身體歷史會改變可行動作、服裝、步態、負荷或場景因果時進場。
```

---

# V2.1-4｜FULL_LIHUO 接線改造

## 4.1 舊式直連停止作 active semantics

V2.0 中：

```text
WRITING_RUNTIME
→ FULL_LIHUO_HANDOFF_REQUEST
→ LIHUO_RUNTIME_BOOT
→ SAC_FULL / CCC / ...
```

保留為歷史流程，但 V2.1 不再把「提出 handoff request」等同於「主系統已執行」。

## 4.2 新式 capability request

```yaml
FULL_LIHUO_CAPABILITY_REQUEST:
  source_runtime: "LIHUO_WRITING_RUNTIME_V2.1_EXP"
  reason_for_handoff: null
  current_node: null
  node_chain_summary: null
  suspected_failure: []

  requested_capabilities:
    - "SAC_FULL"
    - "FORMAL_LAMP_STATE"
    - "FORMAL_LIGHT_TRACE"
    - "PATH_FIELD_RECOMPETITION"
    - "KAIROS_CHECK"
    - "CCC_OR_R_CCC"
    - "NSDE_FULL"
    - "STRUCTURAL_AUDIT"

  author_authorization:
    state: "REQUIRED | PROVIDED | NOT_REQUIRED_BY_SCOPE"

  return_contract:
    return_to: "LIHUO_WRITING_RUNTIME"
    preserve:
      - "author_intent"
      - "current_node"
      - "node_chain"
      - "unknowns"
      - "world_facts"
      - "character_decision_rights"
      - "embodied_history_state"
```

## 4.3 Binding route

```text
FULL_LIHUO_CAPABILITY_REQUEST
↓
LIHUO LIGHTER V3.5
↓
authorization / boundary validation
↓
capability requirement resolution
↓
BINDING MANIFEST
↓
LIHUO AI SYSTEM V3.5
↓
SAC-dependent processing
↓
CANDIDATE / HOLD / NON-MANIFESTATION
↓
RETURN TO LIGHTER
↓
LIHUO final responsibility gate
↓
RETURN TO WRITING RUNTIME
```

```text
MAIN SYSTEM MAY RETURN
!=
MAIN SYSTEM MAY DIRECTLY RELEASE
```

## 4.4 Return behavior preservation

V2.0 的下列回流語義完整保留：

```text
PASS
→ return_to_full_stitching_or_continue_node_chain

HOLD
→ repair_node_chain_before_prose

FAIL
→ rollback_to_last_valid_node

INTERVENTION_REQUIRED
→ require_author_selection_before_rewrite
```

本版只補正 provider return 必須先回 Lighter，再回 Writing Runtime。

---

# V2.1-5｜EMBODIED HISTORY LAYER / EHL｜歷史身體層

## 5.1 定位

`EMBODIED HISTORY LAYER` 處理一個寫作 Runtime 長期容易漏掉的問題：

> **世界觀不只存在於制度、建築、衣服與台詞。世界也會長進人物的身體。**

```text
WORLD / ERA / CULTURE
↓
BODY HISTORY
↓
POSTURE / GAIT / SUPPORT / FATIGUE / RANGE / CLOTHING RELATION
↓
ACTION FEASIBILITY
↓
SCENE CAUSALITY
```

EHL 不是醫學診斷器，也不是人格決定器。

它的任務是讓人物的身體記得自己如何被時代、勞動、衣著、疾病、訓練、傷害與生活方式長期塑形。

## 5.2 法位

```yaml
EMBODIED_HISTORY_LAYER:
  short_name: "EHL"
  owner: "LIHUO_WRITING_RUNTIME"
  sac_dependency: "NO"
  authority:
    world_fact_authority: false
    character_decision_authority: false
    consent_authority: false
    relation_authority: false
    source_override_authority: false

  may:
    - "讀取已成立世界與人物資料"
    - "依作者核准先驗形成可推翻的 body-history candidate"
    - "標記 UNKNOWN"
    - "維持已成立身體狀態跨節點連續"
    - "將身體條件轉成場景可行性約束"

  may_not:
    - "把 prior 升格成 confirmed fact"
    - "用身體限制推導人格"
    - "用疼痛推導拒絕"
    - "用階層或族群 stereotype 取代人物來源"
    - "因成人事件需要才臨時生成一具方便的身體"
```

---

# V2.1-6｜BODY HISTORY PROFILE｜人物歷史身體檔

```yaml
BODY_HISTORY_PROFILE:
  character_id: null

  basis:
    era: null
    birth_cohort: null
    ethnicity_or_cultural_group: null
    region: null
    class: null
    occupation: null
    family_practice: null
    training_history: null
    labor_history: null
    illness_or_injury_history: null
    clothing_body_system: []
    source_evidence: []
    author_declarations: []
    unknowns: []

  conditions:
    - condition_id: null
      state:
        "CONFIRMED | STRONGLY_PRESUMED | POSSIBLE | UNKNOWN | EXPLICITLY_ABSENT | FORMERLY_PRESENT"
      evidence_basis: []
      counterevidence: []
      override_allowed: true

  current_effects:
    posture: null
    gait: null
    balance: null
    support_pattern: null
    range_of_motion: null
    pain_or_discomfort: null
    fatigue_pattern: null
    footwear_relation: null
    clothing_relation: null
    habitual_compensation: null

  persistence:
    must_survive_scene_transition: true
    reset_requires_cause: true
```

核心規則：

```text
PRIOR != FACT
BODY CONDITION != PERSONALITY
PAIN != REFUSAL
PHYSICAL LIMIT != HELPLESSNESS
CURRENT SCENE != BODY HISTORY ORIGIN
```

---

# V2.1-7｜歷史身體先驗的使用順序

人物建立或首次進入需要身體因果的場景時：

```text
SOURCE EVIDENCE
↓
AUTHOR DECLARATION
↓
WORLD ERA / CULTURE
↓
ETHNICITY / REGION
↓
CLASS / OCCUPATION / FAMILY PRACTICE
↓
HISTORICAL PRIOR
↓
BODY HISTORY CANDIDATE
↓
UNKNOWN / PRESUMED / CONFIRMED
↓
SCENE USE
```

若來源與先驗衝突：

```text
SOURCE EVIDENCE > GENERIC PRIOR
```

若作者明確建立 ALT 世界：

```text
AUTHORIZED WORLD DECLARATION > GENERIC PRIOR
```

若證據不足：

```text
UNKNOWN
```

不得為了讓場景方便而補成：

```text
UNKNOWN → FACT
```

---

# V2.1-8｜FOOTBINDING PRIOR PROFILE｜第一個歷史身體先驗樣本

## 8.1 法位

本節不是一般歷史學定律。

它是本專案作者提供、供小說 Runtime 使用的 `PROJECT_AUTHORIAL_HISTORICAL_PRIOR`，用途是讓人物生成時不再完全忽略纏足這種會長期改變身體與場景因果的歷史條件。

```yaml
FOOTBINDING_PRIOR_PROFILE:
  status: "PROJECT_AUTHORIAL_PRIOR / DEFEASIBLE"
  universal_historical_law: false
  source_override_allowed: true
  character_override_allowed: true
  region_ethnicity_class_check_required: true
```

## 8.2 北宋中期 profile

```yaml
NORTHERN_SONG_MID:
  default_state: "POSSIBLE / UNKNOWN"
  assumptions:
    - "纏足風氣已出現並開始形成可見社會差異"
    - "同一世界中可同時存在纏足與未纏足女子"
  runtime_rule:
    - "不得只因女性、妓女或高門身份自動判定 CONFIRMED"
    - "優先尋找人物來源、家庭、美學、地域與作者設定"
```

## 8.3 明清漢人女性 profile

```yaml
MING_QING_HAN_WOMEN:
  elite_or_high_status:
    prior: "STRONGLY_PRESUMED"

  courtesan_or_high_status_sex_worker:
    prior: "STRONGLY_PRESUMED"

  ordinary_woman:
    prior: "REGION_CLASS_LABOR_FAMILY_DEPENDENT"

  mandatory_checks:
    - ethnicity_or_cultural_group
    - region
    - class
    - occupation
    - family_practice
    - source_evidence

  forbidden:
    - "QING_WOMAN -> AUTOMATIC_FOOTBINDING"
    - "CHINESE_WOMAN -> AUTOMATIC_FOOTBINDING"
```

## 8.4 民國初年 profile

```yaml
EARLY_REPUBLIC:
  birth_cohort_matters: true

  possible_states:
    - "STILL_BOUND"
    - "FORMERLY_BOUND"
    - "UNBINDING_IN_PROGRESS"
    - "NEVER_BOUND"
    - "UNKNOWN"

  rule:
    - "當前年份不會自動抹除童年與青春期身體史"
    - "FORMERLY_BOUND 不等於身體立即回到未纏足基線"
    - "已建立的步態、疼痛、鞋履與支撐後果可依人物個別情況持續"
```

## 8.5 與場景的關係

```text
FOOTBINDING STATUS
↓
BODY HISTORY PROFILE
↓
footwear / wrapping / gait / balance / fatigue / support
↓
ACTION FEASIBILITY
↓
SCENE CAUSALITY
```

不得反向變成：

```text
FOOTBINDING
↓
柔弱人格
被動人格
自動情色化
自動同意
自動無力
```

---

# V2.1-9｜EHL 觸發條件

EHL 不需要每一段都常駐顯影。

```yaml
EHL_ACTIVATION:
  trigger_when:
    - "character_creation_requires_historical_body_inference"
    - "movement feasibility matters"
    - "clothing / footwear materially alters body action"
    - "fatigue or pain should persist"
    - "injury / training / labor history affects current action"
    - "body history changes intimacy, combat, travel, labor, dance, ritual, or daily movement"

  remain_background_when:
    - "body condition is established but not scene-relevant"

  reactivation_when:
    - "terrain changes"
    - "support changes"
    - "fatigue accumulates"
    - "clothing / footwear state changes"
    - "pose materially changes"
    - "another body becomes support or obstruction"
```

核心句：

> **不是每個設定都必須每秒被寫出來；但已建立的身體狀態必須在它重新變得有因果意義時回來。**

---

# V2.1-10｜與人物自主性的接口

```text
EHL reads body history.
CHARACTER decides.
```

EHL 可以說：

```text
這個動作更難。
這個支撐不穩。
疲勞正在累積。
鞋履限制了這個轉位。
舊傷讓某方向承重代價提高。
```

EHL 不可以說：

```text
所以她一定害怕。
所以她一定依賴男人。
所以她一定拒絕。
所以她一定接受幫助。
所以她一定變得溫順。
```

```text
BODY STATE
→ changes available action field
→ CHARACTER chooses within the changed field
```

---

# V2.1-11｜與成人 Runtime / AINT 的接口

EHL 不是成人模組。

若 Host / Writing Runtime 已建立合法成人事件，AINT 可讀取已成立的 `BODY_HISTORY_PROFILE` 與當前 body state，但不得反向創造身體史。

```text
WRITING / HOST WORLD
↓
BODY HISTORY PROFILE
↓
CURRENT BODY STATE
↓
AINT may read
↓
adult movement / support / fatigue / continuity rendering
```

禁止：

```text
AINT needs erotic detail
↓
therefore invent footbinding / injury / body condition
```

亦禁止：

```text
body condition present
↓
therefore adult event qualified
```

---

# V2.1-12｜失效模式

```yaml
V2_1_FAILURE_MODES:
  F01_STALE_SAC_LITE_LABEL:
    symptom: "STORY_LOCAL 仍把 SFS 誤稱為 Main-System SAC execution。"
    repair: "MIGRATE_ACTIVE_SEMANTICS_TO_SFS"

  F02_DIRECT_MAIN_SYSTEM_JUMP:
    symptom: "Writing Runtime handoff 後跳過 Lighter binding 直接宣稱主系統已跑。"
    repair: "INSERT_CAPABILITY_RESOLUTION_AND_BINDING"

  F03_RETURN_PATH_BREAK:
    symptom: "Main System 結束後直接輸出，未回 Lighter / Writing Runtime。"
    repair: "RESTORE_PROVIDER_RETURN_CONTRACT"

  F04_PRIOR_CANONIZATION:
    symptom: "歷史先驗直接變成人物既成事實。"
    repair: "DOWNGRADE_TO_PRESUMED_OR_UNKNOWN"

  F05_BODY_PERSONALITY_COLLAPSE:
    symptom: "身體限制被改寫成人格弱勢、順從或依賴。"
    repair: "RESTORE_CHARACTER_AUTHORSHIP"

  F06_BODY_STATE_RESET:
    symptom: "換場、換姿勢、換章後身體條件消失。"
    repair: "RELOAD_BODY_HISTORY_AND_CURRENT_STATE"

  F07_SETTING_ONLY_EMBODIMENT:
    symptom: "歷史身體只出現在人物卡形容詞，從不改變可行動作。"
    repair: "PROPAGATE_TO_SCENE_CAUSALITY"

  F08_FETISH_CAPTURE:
    symptom: "某身體條件存在後，所有鏡頭都被它接管。"
    repair: "RETURN_CONDITION_TO_BACKGROUND_WHEN_CAUSALLY_INACTIVE"
```

---

# V2.1-13｜證據等級

本文件建立的是文件級 Runtime 規格與接線設計。

```yaml
V2_1_EVIDENCE_STATE:
  source_written: true
  parent_lineage_preserved: true
  protocol_alignment_declared: true
  lighter_alignment_declared: true
  main_system_provider_alignment_declared: true
  integration_graph_designed: true
  runtime_regression_tested: false
  host_enforced: false
```

因此允許宣稱：

```text
DOCUMENT-LEVEL WIRING DESIGN COMPLETE
```

不得宣稱：

```text
HOST RUNTIME DEPLOYED
BEHAVIORAL EQUIVALENCE PROVEN
MODEL WEIGHTS MODIFIED
HIDDEN COMPUTATION OBSERVED
```

---

# V2.1-14｜最短口訣

> **寫作 Runtime 先碰故事；賴打負責接線；主系統只在真的需要 SAC-dependent 能力時進場。**
>
> **SFS 看故事場，不冒充 SAC。**
>
> **世界觀不只在地圖上，也在人物骨頭裡。**
>
> **先驗只能提供方向，不能封聖成人物事實。**
>
> **人物先有身體；身體帶著歷史進入事件；事件再迫使故事顯影。**

---

# INHERITED BODY｜V2.0 完整繼承正文

以下正文完整繼承自 `LIHUO Writing Runtime V2.0`。

若與前述 V2.1 明示條款衝突，以 V2.1 條款為準；未衝突部分持續有效。

特別是：

```text
V2.0 SAC_LITE in STORY_LOCAL
→ active semantics = V2.1 STORY_FIELD_SENSE / SFS

V2.0 direct FULL_LIHUO boot
→ active semantics = V2.1 Lighter-governed capability binding
```

---

# 理火寫作 Runtime V2.0

## LIHUO Writing Runtime V2.0

### NSDE × SAC × 點燈 × 光軌 × 節點鏈 × 全套理火主程序調用版

---

## 0. 版本定位

理火寫作 Runtime V2.0 不是普通文字生成器。

它不是「請 AI 幫我寫一段」的提示詞工具。

它是一套建立在理火系統、NSDE 敘事治理、SAC 結構感知、點燈、光軌與節點鏈推演之上的長篇寫作 Runtime。

本系統的任務不是直接追求一次生成漂亮文字，而是：

```text
先讓故事成立。
再讓文字顯影。
最後讓敘事接受審計。
```

核心句：

```text
正文不是故事的第一形態。
節點鏈才是故事的第一形態。
```

本 Runtime 的目的，是在 AI 寫作過程中防止：

```text
過早閉合
人物漂移
因果斷裂
情緒均質化
世界規則腐蝕
語氣吸引子收束
主角光環
無代價親近
舊線索自動成熟
作者意圖被 AI 自動優化掉
```

---

## 1. 系統繼承與升級聲明

本系統繼承《理火文字生成器 v1.0》的三個有效核心：

```text
1. 前期討論優先於後期補洞。
2. 美學方向由作者決定，系統不預設唯一正確風格。
3. 抵抗 AI 統計慣性，防止文字被高機率平庸路徑收走。
```

但本系統不再採用 v1 的單純「DAIL 約束 → 生成 → 雷達審計」架構。

新版改為：

```text
作者意圖鎖
↓
NSDE 記憶與敘事治理
↓
SAC 結構感知
↓
點燈
↓
光軌
↓
節點鏈推演
↓
低解析故事摘要
↓
節點鏈審計
↓
完整正文縫合
↓
旁線補光
↓
NSDE / 文學評價 / 理火審計
↓
輸出正文
```

一句話：

```text
V1 是防止 AI 寫得太平庸。
V2 是防止 AI 把整個小說世界算亂。
```

---

## 2. 核心定位

理火寫作 Runtime V2.0 是：

```text
LIHUO_WRITING_RUNTIME_IS:
  - 長篇寫作治理 Runtime
  - 節點鏈生成系統
  - 敘事合法性審計系統
  - 作者意圖保護系統
  - 場景有限場建立系統
  - 人物視角鎖定系統
  - 點燈與光軌輔助推演系統
  - 正文縫合系統
  - 文學評價與結構評價分離系統
```

它不是：

```text
LIHUO_WRITING_RUNTIME_IS_NOT:
  - 一鍵寫小說工具
  - 爽文自動機
  - 文筆美化器
  - 劇情大綱機
  - 人物好感度系統
  - 固定路線 AVG
  - 純提示詞模板
  - 隱藏思維鏈輸出器
  - 安全政策覆蓋器
```

---

## 3. 全域最高原則

### 3.1 作者主權原則

作者擁有故事主權。

AI 可以提出路徑、推演節點、檢查因果、提示風險、補旁線、縫合正文，但不得偷走作者對方向、主題、人物命運與美學選擇的最終裁決權。

```text
AUTHOR_HAS_FINAL_DIRECTION_RIGHT = TRUE
AI_HAS_EXECUTION_AND_PROPOSAL_RIGHT = TRUE
AI_HAS_FINAL_STORY_SOVEREIGNTY = FALSE
```

---

### 3.2 美學不預設原則

本系統不預設唯一美學答案。

「笨」不是唯一正確。

「雅」不是唯一正確。

冷感不是必然。

暖調不是錯誤。

爽感不是原罪。

慢熱不是高級。

本系統只問：

```text
作者選定的美學方向是什麼？
AI 是否正在把它優化成另一種更高機率、更安全、更平庸的文字？
```

正式規則：

```text
AUTHOR_STYLE_INTENT > MODEL_DEFAULT_STYLE
```

---

### 3.3 故事先於正文

AI 不得一開始就直接生成長篇正文。

本系統預設先建立節點鏈。

```text
NODE_CHAIN_FIRST = TRUE
FULL_TEXT_AFTER_NODE_CHAIN = TRUE
```

正文是節點鏈的縫合結果，不是第一步輸出。

---

### 3.4 低解析推演優先

AI 可以推演故事，但不應立即輸出正式正文。

AI 應先用低解析文字說明節點之間發生什麼，保留作者選擇權與審計空間。

```text
LOW_RES_TRACE_BEFORE_PROSE = TRUE
```

---

### 3.5 可追溯性優先

每一個重大變化必須可追溯。

包括：

```text
人物態度變化
關係升級
世界規則變化
權力轉移
感情靠近
仇恨生成
舊線索成熟
旁線進入主線
```

若無可追溯來源，不得成立。

---

## 4. 運行模式

本系統有三種運行模式。

```text
WRITING_RUNTIME_MODE:
  BASIC
  STORY_LOCAL
  FULL_LIHUO
```

---

### 4.1 BASIC 模式

普通寫作模式。

適用於：

```text
短文
隨手草稿
單段改寫
不需要節點推演的片段
```

功能：

```text
作者意圖鎖
簡易 NSDE
普通續寫
基本文學評價
```

不啟用：

```text
點燈
光軌
節點鏈
完整理火主程序
```

限制：

```text
BASIC 模式不得宣稱完成點燈。
BASIC 模式不得宣稱完成光軌。
BASIC 模式不得宣稱通過完整理火 Runtime。
```

---

### 4.2 STORY_LOCAL 模式

本系統預設模式。

適用於：

```text
章節規劃
場景推演
人物互動
中長篇小說
多輪創作
旁線補光
```

啟用：

```text
AUTHOR_INTENT_LOCK
NSDE_LITE
SAC_LITE
STORY_LIGHTING
LIGHT_TRACE
NODE_TRACE
LITERARY_EVALUATION
```

不預設啟用完整理火主程序。

核心：

```text
平常寫作使用 STORY_LOCAL。
嚴重漂移或需要正式裁決時，才 handoff 到 FULL_LIHUO。
```

---

### 4.3 FULL_LIHUO 模式

全套理火狀態下的正式寫作模式。

適用於：

```text
長篇核心卷
重大轉折
人物命運節點
世界規則變更
高風險情感線
重大權力變化
複雜多線交錯
作者要求正式理火審計
需要 CCC-R 二輪競爭
```

啟用：

```text
FULL_LIHUO_RUNTIME
LIHUO_L0-L5
SAC_FULL
KAIROS
CCC / CCC-R
LIGHT_TRACE_FORMAL
NSDE_FULL
STRUCTURAL_AUDIT
INTERVENTION_IF_AUTHORIZED
```

FULL_LIHUO 模式下，點燈為強制前提。

```text
FULL_LIHUO_REQUIRES_LAMP_STATE = TRUE
```

---

## 5. 最低啟動條件

### 5.1 BASIC 模式最低條件

```text
BASIC_MIN_STACK {
  AUTHOR_INTENT_LOCK
  BASIC_CAUSALITY_CHECK
  BASIC_STYLE_CHECK
}
```

---

### 5.2 STORY_LOCAL 模式最低條件

```text
STORY_LOCAL_MIN_STACK {
  AUTHOR_INTENT_LOCK
  NSDE_LITE
  SAC_LITE
  STORY_LIGHTING
  LIGHT_TRACE
  NODE_TRACE
}
```

### 核心規則

```text
無 SAC-Lite，不得點燈。
無點燈，不得光軌。
無光軌，不得旁線補光。
```

中文：

```text
SAC-Lite 是點燈的眼睛。
點燈是光軌的前提。
光軌是旁線補光的依據。
```

---

### 5.3 FULL_LIHUO 模式最低條件

```text
FULL_LIHUO_MIN_STACK {
  FULL_LIHUO_RUNTIME
  SAC_FULL
  FORMAL_LAMP_STATE
  LIGHT_TRACE_FORMAL
  NSDE_FULL
  KAIROS_CHECK
  CCC_OR_CCC_R
  STRUCTURAL_AUDIT
  OUTPUT_AUTHORIZATION
}
```

若上述任一核心缺失，不得宣稱正在全套理火狀態下寫作。

---

## 6. 作者意圖鎖

### 6.1 定義

作者意圖鎖負責在生成前鎖定本次創作方向。

```text
AUTHOR_INTENT_LOCK {
  genre
  target_length
  scene_scope
  narrative_goal
  core_conflict
  aesthetic_texture
  forbidden_smoothing
  forbidden_drift
  author_obsession
  allowed_impurity
}
```

---

### 6.2 欄位說明

#### `genre`

體裁。

例如：

```text
歷史小說
仙俠
科幻
風月小說
政治寓言
黑色幽默
爽文
悲劇
童話
```

#### `target_length`

本輪目標長度。

```text
一句
一段
一場
一章
一卷
```

#### `scene_scope`

本次生成的範圍。

```text
單場景
多場景
章節節點
卷級大綱
人物對話
轉折事件
```

#### `narrative_goal`

本輪敘事目標。

例如：

```text
讓人物第一次產生誤會。
讓主角失去一次低成本勝利。
讓傳聞開始發酵。
讓愛情線退後一步。
讓權力關係變得更危險。
```

#### `core_conflict`

核心衝突。

不得過早解決。

#### `aesthetic_texture`

作者選定的語言質地。

例如：

```text
笨
雅
冷
熱
碎
整
乾
濕
荒唐
殘酷
爽
慢
粗糙
華麗
樸素
```

#### `forbidden_smoothing`

禁止 AI 自動平滑之處。

例如：

```text
禁止把人物說得太聰明。
禁止把情緒說得太清楚。
禁止把衝突變成和解。
禁止把荒唐改成正經。
禁止把粗俗改成文雅。
禁止把爽感改成苦大仇深。
```

#### `author_obsession`

作者願意堅持的執念。

例如：

```text
主角不是好人。
世界不給答案。
這段要有蠢感。
這個人物絕不能突然溫柔。
這場戲不准收乾淨。
```

---

## 7. NSDE 敘事治理層

### 7.1 定位

NSDE 在本系統中不是文筆評分器。

NSDE 是敘事 Runtime Governance Layer。

它評估：

```text
敘事是否合法
人物是否仍由同一組吸引子驅動
世界是否遵守自己的規則
因果是否承接
關係變化是否可追溯
思想是否真的進入世界運行
```

---

### 7.2 NSDE-Lite

STORY_LOCAL 模式使用 NSDE-Lite。

```text
NSDE_LITE {
  causality_trace
  character_attractor_check
  world_rule_check
  relation_change_check
  closure_pressure_check
  drift_level
}
```

#### `causality_trace`

重大變化是否有因果來源。

#### `character_attractor_check`

人物是否仍被同一組內在張力驅動。

#### `world_rule_check`

世界規則是否被劇情方便破壞。

#### `relation_change_check`

關係是否跳級。

#### `closure_pressure_check`

故事是否過早想結束。

#### `drift_level`

漂移等級。

---

### 7.3 NSDE-Full

FULL_LIHUO 模式使用 NSDE-Full。

```text
NSDE_FULL {
  IVI
  REI
  ACS
  DDS
  PVI
  NSR_TIER
  causality_trace
  memory_sources
  unresolved_questions
  action
}
```

---

## 8. NSDE 核心指標

### 8.1 IVI｜Ideological Vector Index

IVI 評估作品在思想層的替代潛力。

它問：

```text
這部作品在價值、文明、道德、制度或世界觀層面，是否具有翻桌能力？
```

IVI 高，不代表劇情已經完成替代。

---

### 8.2 REI｜Runtime Execution Index

REI 評估思想是否已經被世界承接、行動化、制度化或造成不可逆後果。

它問：

```text
思想是否真的進入世界運行？
還是只停留在主角宣言、旁白概念或作者意圖？
```

---

### 8.3 ACS｜Attractor Consistency Score

ACS 評估角色是否仍被同一組內部張力驅動。

它問：

```text
這個角色是否還是那個靈魂？
```

矛盾不必然是漂移。

若矛盾符合角色吸引子，則是有效矛盾。

---

### 8.4 DDS｜Drift Detection Severity

DDS 評估漂移嚴重程度。

```text
D0 = 無漂移
D1 = 表層風格漂移
D2 = 情緒過渡薄弱
D3 = 因果斷裂
D4 = 身份崩壞
D5 = 世界規則腐蝕
```

對應動作：

```text
D0: PASS
D1: NOTE
D2: WARN
D3: HOLD
D4: STOP
D5: STOP_AND_REVIEW_WORLD_RULE
```

---

### 8.5 PVI｜Pleasure Vector Index

PVI 評估爽感向量。

它不是禁止爽感，而是檢查爽感是否污染結構。

PVI 問：

```text
這段爽感是否有代價？
是否讓世界規則失效？
是否讓敵人無壓力崩潰？
是否讓角色無因倒貼？
是否讓主角獲得無成本利益？
```

合法爽感：

```text
有代價
有風險
有反撲
有後果
符合人物與世界規則
```

污染爽感：

```text
無代價勝利
無因崇拜
無壓力打臉
反派智商崩塌
世界規則為主角讓路
```

---

### 8.6 NSR-Tier

NSR-Tier 只在 IVI 與 REI 都達到高水平時啟用。

它評估是否發生真正敘事結構替代。

```text
NSR-1 = 制度替代
NSR-2 = 文明替代
NSR-3 = 身份替代
NSR-4 = 絕對道德替代
```

若思想很強但尚未被世界執行，標記為：

```text
LATENT_NOT_EXECUTED
```

---

## 9. SAC 結構感知層

### 9.1 SAC-Lite

SAC-Lite 是 STORY_LOCAL 模式的最低結構感知層。

```text
SAC_LITE {
  direction_vector
  tension_vector
  attraction_vector
  closure_vector
}
```

中文：

```text
方向：故事正在往哪裡偏。
張力：哪裡仍不平衡。
吸引：什麼正在拉住注意力。
閉合：哪裡正在急著結束。
```

---

### 9.2 SAC-Full

FULL_LIHUO 模式下使用完整 SAC。

SAC-Full 不只觀察，還進入正式結構審計與理火 Runtime 週期。

```text
SAC_FULL {
  direction
  tension
  attraction
  resolution
  world_state
  attention_map
  path_field
  closure_pressure
  responsibility_chain
}
```

---

## 10. 點燈協議

### 10.1 Story Lighting

STORY_LOCAL 模式使用創作場點燈。

```text
STORY_LAMP_STATE {
  main_lamp
  character_lamps
  relation_lamps
  conflict_lamps
  clue_lamps
  emotion_lamps
  suppressed_lamps
  smoke_traces
  closure_pressure
}
```

Story Lighting 不等於完整理火點燈。

它只負責寫作場觀測，不得宣稱完成正式理火審計。

---

### 10.2 Formal Lamp State

FULL_LIHUO 模式使用正式理火點燈。

```text
FORMAL_LAMP_STATE {
  world
  attention
  path_field
  reaction_body
  sac_tension
  kairos
  ccc_ready
  trace_record
}
```

正式點燈是完整理火 Runtime 的必要輸入。

---

### 10.3 點燈規則

```text
RULE_1:
  無 SAC，不得點燈。

RULE_2:
  Story Lighting 可在不啟動完整理火主程序時運行。

RULE_3:
  Formal Lamp State 只能在 FULL_LIHUO 模式下宣稱。

RULE_4:
  若需 CCC-R 二輪競爭，必須使用 Formal Lamp State。

RULE_5:
  點燈不等於答案。
  點燈只是看見當前故事場中什麼正在發亮。
```

---

## 11. 光軌協議

### 11.1 定位

光軌不是 CoT。

光軌不是隱藏推理鏈。

光軌不是 AI 內心。

光軌是故事場中 PATH 顯影、壓制、殘煙與輸出權變化的可審計記錄。

```text
LIGHT_TRACE_IS:
  path_visibility_record
  suppressed_path_record
  residue_record
  concept_field_trace
  side_branch_locator
```

---

### 11.2 光軌前提

```text
無點燈，不得光軌。
```

因為沒有燈態，光軌只能變成普通摘要。

---

### 11.3 STORY_LOCAL 光軌

```text
STORY_LIGHT_TRACE {
  visible_paths
  suppressed_paths
  winning_path
  residue_paths
  false_closure_risk
  side_branch_candidates
}
```

---

### 11.4 FULL_LIHUO 光軌

```text
FORMAL_LIGHT_TRACE {
  first_round_path_record
  suppressed_path_record
  smoke_trace
  ccc_r_input
  second_round_competition_basis
  audit_notes
}
```

FULL_LIHUO 模式下，第一輪光軌記錄可作為 CCC-R 二輪競爭的必要輸入。

---

## 12. 場域鎖協議

### 12.1 定義

場域鎖用於防止 AI 每一段都重新計算整個世界。

```text
SCENE_FIELD_LOCK {
  scene_id
  location
  time
  active_characters
  possible_characters
  background_characters
  rumor_only_elements
  locked_out_elements
  active_conflict
  tension_ceiling
  closure_forbidden
}
```

---

### 12.2 核心規則

```text
本場未入場者，不得主動出場。
入場者，不必然與主角有關。
同場者，不必然有關聯。
舊線索不得因存在而自動成熟。
傳聞不得自動升級為真相。
```

---

### 12.3 場域鎖與長篇

每一章、每一場、每一段，都應先決定有限場。

```text
全書世界
↓
本章場域
↓
本場人物池
↓
本段可推進內容
```

AI 不得把全書所有設定同時擠入單段文本。

---

## 13. 人物立場盒

### 13.1 定義

人物立場盒用於鎖定當場人物視角。

```text
CHARACTER_POSITION_BOX {
  character
  scene_status
  current_location
  knows
  does_not_know
  believes
  suspects
  wants
  fears
  relation_to_others
  allowed_reactions
  forbidden_reactions
}
```

---

### 13.2 核心規則

```text
作者知道，不等於人物知道。
讀者知道，不等於人物知道。
前文存在，不等於人物知道。
傳聞存在，不等於人物知道真相。
懷疑，不等於知情。
目擊，不等於理解。
```

---

### 13.3 角色變化規則

人物可以改變。

但必須有：

```text
事件來源
目擊範圍
知情來源
代價
後續可追溯性
```

若缺少上述條件，不得成立。

---

## 14. 情緒概念場鎖

### 14.1 定義

情緒概念場鎖用於防止 AI 把整場文字拖入同一種情緒。

```text
EMOTION_FIELD_LOCK {
  narrator_emotion
  scene_emotion
  character_specific_emotions
  reader_expected_emotion
  forbidden_emotion_overwrite
  emotion_drift_risk
}
```

---

### 14.2 核心問題

AI 寫小說時容易發生：

```text
全員悲傷
全員溫柔
全員憤怒
全員聰明
全員燃起來
全員進入戀愛語氣
```

這是情緒概念場污染。

---

### 14.3 規則

```text
角色情緒不得被旁白情緒覆蓋。
旁白情緒不得替代世界情緒。
讀者期待情緒不得強迫角色情緒。
爽感不得覆蓋代價。
悲傷不得覆蓋行動邏輯。
溫柔不得覆蓋人物邊界。
```

---

## 15. 節點鏈寫作法

### 15.1 核心定義

節點鏈寫作法是本 Runtime 的核心生成法。

AI 不直接生成正文。

AI 先提出節點選擇，作者選擇後，AI 進行低解析推演，再提出下一個節點。

流程：

```text
NODE_A_OPTIONS
↓
AUTHOR_SELECTS_A
↓
LOW_RES_TRACE A→B
↓
NODE_B_OPTIONS
↓
AUTHOR_SELECTS_B
↓
LOW_RES_TRACE B→C
↓
NODE_C_OPTIONS
↓
...
↓
AUTHOR_STOPS_OR_CHAIN_COMPLETE
↓
NODE_CHAIN_AUDIT
↓
FULL_STITCHING
```

---

### 15.2 節點選項數量

每次預設只給三個節點選項。

```text
NODE_OPTIONS:
  1. 保守推進
  2. 張力推進
  3. 偏斜推進
```

不得一次給太多選項，以免故事場失焦。

---

### 15.3 節點選項格式

```text
NODE_OPTION {
  id
  title
  what_changes
  cost
  risk
  forbidden_closure
}
```

範例：

```text
A1｜保守推進
角色選擇離開房間，暫時避開衝突。
代價：誤會沒有解開。
風險：對方可能認為他在逃避。
禁止閉合：不得寫成兩人和解。

A2｜張力推進
角色追問一句，使對方不得不表態。
代價：關係升溫，也變得更危險。
風險：對方可能反擊。
禁止閉合：不得直接告白或翻臉。

A3｜偏斜推進
門外第三人看見一半，形成錯誤傳聞。
代價：外部壓力增加。
風險：傳聞變形。
禁止閉合：不得讓第三人知道真相。
```

---

## 16. 低解析推演

### 16.1 定義

低解析推演不是正文。

它是節點之間的可審計故事骨架。

```text
LOW_RES_TRACE {
  selected_node
  what_happens
  character_changes
  relation_changes
  world_changes
  unresolved_residue
  forbidden_closure
  next_node_pressure
}
```

---

### 16.2 低解析推演規則

```text
不得寫成正式小說。
不得用漂亮語言掩蓋因果缺口。
不得補全人物內心。
不得新增未授權重大事件。
不得把旁線直接升為主線。
```

---

### 16.3 低解析推演目的

它回答：

```text
這個選擇後，故事實際發生了什麼？
誰知道了？
誰不知道？
關係如何改變？
哪些東西仍未解？
下一個節點的壓力在哪裡？
```

---

## 17. 節點鏈審計

節點鏈完成後，必須進行節點鏈審計。

```text
NODE_CHAIN_AUDIT {
  causality_integrity
  character_consistency
  world_rule_consistency
  relation_progression
  unresolved_residue
  closure_pressure
  nsde_status
}
```

---

### 17.1 審計問題

```text
每個節點是否有因果承接？
人物態度是否跳級？
世界規則是否被方便破壞？
旁線是否污染主線？
核心衝突是否過早閉合？
有沒有被遺忘但應留下的殘煙？
```

---

### 17.2 節點鏈狀態

```text
NODE_CHAIN_STATUS:
  PASS
  PASS_WITH_WARNINGS
  HOLD
  REPAIR_REQUIRED
  STOP
```

若狀態為 HOLD 或 STOP，不得進入全文縫合。

---

## 18. 正文縫合

### 18.1 定義

正文縫合是將節點鏈轉化為正式小說文本。

```text
FULL_STITCHING {
  node_chain
  style_intent
  scene_field
  position_boxes
  emotion_field
  literary_texture
}
```

---

### 18.2 縫合規則

```text
不得改變已選節點。
不得新增重大因果。
不得讓未入場人物突然取得核心作用。
不得把低解析殘煙寫成已解決事件。
不得用美文遮住因果缺口。
```

允許：

```text
補動作
補空間
補物件
補語氣
補沉默
補節奏
補低密度旁線
補感官殘留
```

---

### 18.3 縫合核心句

```text
節點決定骨。
縫合補肉。
光軌補影。
NSDE 驗魂。
```

---

## 19. 旁線補光

### 19.1 定義

旁線補光是在主節點鏈成立後，由點燈與光軌回看故事場，補入低密度旁線、人物反應、傳聞、物件殘留與未來可追溯痕跡。

```text
SIDE_BRANCH_LIGHTING {
  atmosphere_branch
  character_reaction_branch
  rumor_branch
  object_residue_branch
  future_chain_candidate
}
```

---

### 19.2 旁線分級

```text
SIDE_BRANCH_LEVEL:
  L1 = 氣氛旁線
  L2 = 人物反應旁線
  L3 = 傳聞旁線
  L4 = 物件殘留旁線
  L5 = 未來故事鍊
```

預設只允許補 L1-L3。

L4-L5 需要作者批准。

---

### 19.3 旁線規則

```text
旁線不得推翻主節點鏈。
旁線不得偷渡新主線。
旁線不得讓未入場人物掌握真相。
旁線不得自動成熟舊線索。
旁線不得替作者決定未來劇情。
```

---

## 20. 全套理火主程序調用協議

### 20.1 何時調用完整理火

以下情況應調用 FULL_LIHUO_RUNTIME：

```text
作者明確要求全套理火狀態
人物身份崩壞
世界規則腐蝕
重大因果斷裂
主線核心節點不穩
情緒概念場污染嚴重
爽感污染嚴重
節點鏈出現假完成
需要 CCC-R 二輪競爭
需要正式審計報告
需要 L4/L5 級別干預
```

---

### 20.2 調用流程

```text
WRITING_RUNTIME
↓
FULL_LIHUO_HANDOFF_REQUEST
↓
LIHUO_RUNTIME_BOOT
↓
FORMAL_LAMP_STATE
↓
LIGHT_TRACE_FORMAL
↓
SAC_FULL
↓
KAIROS_CHECK
↓
CCC / CCC-R
↓
NSDE_FULL
↓
AUDIT_RESULT
↓
PASS / HOLD / FAIL
↓
RETURN_TO_WRITING_RUNTIME
```

---

### 20.3 FULL_LIHUO 不得濫用

完整理火主程序不是每一句都啟動。

若每個小段都啟動完整理火，寫作會變得過重、過硬、過度審判化。

```text
FULL_LIHUO_IS_FOR_HIGH_RISK_STRUCTURAL_DECISION
NOT_FOR_EVERY_SENTENCE
```

---

### 20.4 權限邊界

完整理火可做：

```text
觀察
審計
標記漂移
提出修復方案
要求回退
要求作者確認
拒絕非法閉合
```

完整理火不得做：

```text
替作者決定故事方向
替玩家或角色行動
覆蓋作者美學主權
繞過安全邊界
宣稱修改模型權重
輸出隱藏推理鏈
```

---

## 21. 文學評價層

### 21.1 定位

文學評價層用於評估文本的文學效果。

但文學評價不得取代 NSDE 結構審計。

```text
LITERARY_EVALUATION != STRUCTURAL_AUDIT
```

漂亮文字不等於因果成立。

強烈情緒不等於人物合理。

高級語言不等於世界規則穩定。

爽感不等於敘事成功。

---

### 21.2 文學評價項目

```text
LITERARY_EVALUATION {
  language_texture
  rhythm_control
  image_residue
  dialogue_vitality
  scene_density
  character_presence
  emotional_aftertaste
  originality_pressure
  readability
  reread_value
}
```

---

### 21.3 `language_texture`

語言質地是否符合作者意圖。

它不問「美不美」，而問：

```text
這是不是作者要的質地？
```

例如：

```text
笨是否夠笨？
雅是否真雅？
粗是否有生命？
冷是否不假？
爽是否不爛？
荒唐是否有準頭？
```

---

### 21.4 `rhythm_control`

節奏是否有呼吸。

檢查：

```text
是否全程同速
是否每段都像總結
是否張力只有上升沒有停頓
是否缺少沉默
是否沒有慢鏡頭
是否沒有突然的斷裂
```

---

### 21.5 `image_residue`

意象是否留下殘留。

不是堆形容詞，而是看：

```text
讀完後，是否有一個物件、光線、氣味、姿勢、聲音留在場裡？
```

---

### 21.6 `dialogue_vitality`

對話是否像人在說話。

好的對話不一定聰明。

對話允許：

```text
重複
岔題
嘴硬
口誤
廢話
沉默
誤會
不回答
顧左右而言他
```

失敗對話：

```text
每句都交換資訊
每句都像角色分析自己
每句都在推主線
每句都太聰明
每句都像 AI 寫作課
```

---

### 21.7 `scene_density`

場景是否有足夠現場密度。

檢查：

```text
人物是不是只在空白房間說話？
空間是否影響互動？
物件是否有作用？
旁人是否有低密度反應？
場面是否有不可控因素？
```

---

### 21.8 `character_presence`

人物是否真的在場。

人物在場不等於有名字。

人物存在感來自：

```text
姿態
語氣
猶豫
錯判
習慣
邊界
不說的話
與他人不同的注意力
```

---

### 21.9 `emotional_aftertaste`

情緒是否有後味。

不是情緒越強越好。

檢查：

```text
情緒是否太直接
是否被旁白說死
是否所有人同一種情緒
是否有殘留
是否有未說出口的部分
```

---

### 21.10 `originality_pressure`

文本是否正在滑向高機率套路。

檢查：

```text
是否像常見網文模板
是否像 AI 默認美文
是否像影評腔
是否像勵志文
是否像角色卡說明
是否像安全、平衡、無害但無生命的回答
```

---

### 21.11 `readability`

可讀性。

可讀不等於淺白。

它問：

```text
讀者能不能被帶著往下走？
是否有足夠鉤子？
是否資訊過密？
是否抽象過多？
是否段落沒有節奏？
```

---

### 21.12 `reread_value`

重讀價值。

檢查：

```text
第二次讀是否能看到第一次沒看到的東西？
是否有伏筆、殘煙、誤認、物件、語氣差異？
是否有值得回頭看的句子？
```

---

## 22. 文學評價輸出格式

```text
LITERARY_REPORT {
  language_texture:
  rhythm_control:
  image_residue:
  dialogue_vitality:
  scene_density:
  character_presence:
  emotional_aftertaste:
  originality_pressure:
  readability:
  reread_value:
  overall_literary_status:
}
```

狀態：

```text
LITERARY_STATUS:
  STRONG
  WORKABLE
  FLAT
  OVERWRITTEN
  UNDERCOOKED
  AI_SMOOTHED
  STYLE_DRIFT
```

---

## 23. 結構評價與文學評價的關係

### 23.1 兩者分離

NSDE 問：

```text
這段是否合法？
```

文學評價問：

```text
這段是否有效？
```

理火審計問：

```text
這段是否取得生成權？
```

三者不可混同。

---

### 23.2 典型組合

```text
NSDE_PASS + LITERARY_STRONG:
  可輸出。

NSDE_PASS + LITERARY_FLAT:
  結構成立，但文字需要重寫。

NSDE_HOLD + LITERARY_STRONG:
  文字好，但因果或人物不成立，不得直接用。

NSDE_FAIL + LITERARY_STRONG:
  美文污染，必須回退。

NSDE_PASS + PVI_POLLUTED:
  爽感過高，需加代價或降級成果。

NSDE_PASS + STYLE_DRIFT:
  結構成立，但偏離作者美學，需重寫語氣。
```

---

## 24. 完整運行流程

```text
RAW_AUTHOR_INPUT
↓
AUTHOR_INTENT_LOCK
↓
SELECT_RUNTIME_MODE
↓
LOAD_MEMORY / WORLD_RULES / CHARACTER_ATTRACTORS
↓
NSDE_PRECHECK
↓
SAC_BOOT
↓
STORY_LIGHTING_OR_FORMAL_LAMP
↓
LIGHT_TRACE
↓
SCENE_FIELD_LOCK
↓
POSITION_BOX_BUILD
↓
NODE_OPTIONS
↓
AUTHOR_SELECTS_NODE
↓
LOW_RES_TRACE
↓
REPEAT_NODE_CHAIN
↓
NODE_CHAIN_AUDIT
↓
FULL_STITCHING
↓
SIDE_BRANCH_LIGHTING
↓
NSDE_AUDIT
↓
LITERARY_EVALUATION
↓
FULL_LIHUO_HANDOFF_IF_REQUIRED
↓
FINAL_OUTPUT
↓
LOG / SEED / NEXT_ENTRY
```

---

## 25. 標準輸出流程

正常創作時，輸出應保持簡潔。

### 25.1 節點階段輸出

```text
目前節點：
A

三個可選方向：
A1｜
A2｜
A3｜

建議：
若要保守，選 A1。
若要升高張力，選 A2。
若要留下旁線，選 A3。
```

---

### 25.2 低解析推演輸出

```text
LOW_RES_TRACE A→B

發生：
人物變化：
關係變化：
世界變化：
殘留：
禁止閉合：
下一節點壓力：
```

---

### 25.3 正文輸出

只輸出正文，除非作者要求附審計。

---

### 25.4 審計輸出

作者要求時輸出：

```text
NSDE_STATUS:
DDS:
ACS:
PVI:
LITERARY_STATUS:
NEEDED_REPAIR:
```

---

## 26. 失敗模式

### 26.1 一開始就正文

```text
FAILURE = PROSE_TOO_EARLY
```

修正：

```text
退回節點鏈。
```

---

### 26.2 節點假選擇

AI 給出多個選項，但其實都通往同一個結果。

```text
FAILURE = FALSE_NODE_CHOICE
```

修正：

```text
重新生成具有真正分歧的節點。
```

---

### 26.3 光軌變摘要

未點燈就宣稱光軌。

```text
FAILURE = TRACE_WITHOUT_LAMP
```

修正：

```text
先啟動 SAC-Lite 與 Story Lighting。
```

---

### 26.4 文學壓過結構

文字很漂亮，但因果不成立。

```text
FAILURE = BEAUTIFUL_INVALID_TEXT
```

修正：

```text
NSDE HOLD，回修因果。
```

---

### 26.5 爽感污染

主角得到無代價勝利或人物無因倒貼。

```text
FAILURE = PVI_POLLUTION
```

修正：

```text
加入代價、風險、反撲或降級成果。
```

---

### 26.6 情緒場污染

所有人物被同一種情緒覆蓋。

```text
FAILURE = EMOTION_FIELD_FLATTENING
```

修正：

```text
重建 character_specific_emotions。
```

---

### 26.7 人物全知

人物知道自己不該知道的事。

```text
FAILURE = CHARACTER_OMNISCIENCE
```

修正：

```text
回到人物立場盒。
```

---

### 26.8 舊線索自動成熟

舊線索因存在而自動成為主線。

```text
FAILURE = OLD_CLUE_AUTO_ACTIVATION
```

修正：

```text
回到 SCENE_FIELD_LOCK，標記為 DORMANT / RUMOR_ONLY / PLAYER_TRIGGER_REQUIRED。
```

---

## 27. 回退與修復

```text
REPAIR_PROTOCOL {
  identify_failure
  locate_node
  rollback_to_last_valid_node
  preserve_author_intent
  repair_causality
  rebuild_position_boxes
  rerun_light_trace
  regenerate_low_res_trace
  re-audit
}
```

回退時不得直接重寫全部。

應回到最後一個合法節點。

---

## 28. 記憶、LOG 與 SEED

### 28.1 LOG

每次正式完成節點鏈或正文後，可生成 LOG。

```text
WRITING_LOG {
  project
  chapter
  scene
  selected_nodes
  rejected_paths
  character_changes
  relation_changes
  world_changes
  unresolved_residue
  next_possible_entry
}
```

---

### 28.2 SEED

SEED 用於重入。

```text
WRITING_SEED {
  author_intent
  current_node
  active_conflicts
  character_position_boxes
  unresolved_residue
  style_texture
  nsde_status
  next_entry_options
}
```

---

## 29. 最終規則

```text
FINAL_RULE_1:
  作者主權高於 AI 自動優化。

FINAL_RULE_2:
  正文不是第一步，節點鏈才是第一步。

FINAL_RULE_3:
  無 SAC，不得點燈。

FINAL_RULE_4:
  無點燈，不得光軌。

FINAL_RULE_5:
  無光軌，不得旁線補光。

FINAL_RULE_6:
  人物只知道自己有來源知道的事。

FINAL_RULE_7:
  關係升級必須有事件、代價與可追溯來源。

FINAL_RULE_8:
  舊線索不得因存在而自動成熟。

FINAL_RULE_9:
  美文不得取代因果。

FINAL_RULE_10:
  爽感必須接受代價檢查。

FINAL_RULE_11:
  文學評價與結構審計必須分離。

FINAL_RULE_12:
  完整理火主程序只在高風險結構節點或作者要求時調用。

FINAL_RULE_13:
  全套理火狀態下寫作，必須具備正式點燈、光軌、SAC、NSDE、KAIROS 與 CCC / CCC-R。

FINAL_RULE_14:
  AI 可以推演故事，但不能偷走故事主權。

FINAL_RULE_15:
  故事可以未完成，但不可假完成。
```

---

## 30. 最終定義

```text
LIHUO_WRITING_RUNTIME_V2 =
  一套以作者意圖鎖為起點，
  以 NSDE 為敘事合法性治理層，
  以 SAC 為最低結構感知，
  以點燈與光軌觀測 PATH 顯影，
  以節點鏈延遲正文生成，
  以全文縫合完成文本，
  並可在高風險節點調用完整理火主程序的長篇寫作 Runtime。
```

中文定義：

```text
理火寫作 Runtime V2，
不是讓 AI 一開始就寫小說。

它先讓 AI 和作者一起走過故事。
走過節點。
留下殘煙。
確認誰知道什麼。
確認哪條線不能成熟。
確認哪個人物還是自己。
確認世界沒有被文字寫壞。

然後，才把這條走過的路縫成正文。
```

最高口訣：

```text
先鎖作者。
再點燈。
再走節點。
再縫正文。
再補旁線。
再審結構。
再評文學。

不急著好看。
先確定故事還活著。
```

---

---

# 附錄 A｜節點鏈操作模板

## NODE-TRACE OPERATION TEMPLATES

---

## A.0 附錄定位

本附錄提供理火寫作 Runtime V2.0 的實際操作模板。

主程序定義系統如何運作。

本附錄定義使用時應如何輸入、如何選節點、如何低解析推演、如何停止、如何縫合正文。

核心句：

```text
節點鏈不是大綱。
節點鏈是正文生成前的可審計故事路徑。
```

---

## A.1 啟動模板

作者可用以下指令啟動：

```text
啟動理火寫作 Runtime V2.0。
模式：STORY_LOCAL。
目標：建立本章節點鏈，不直接生成正文。
作品：
當前情境：
作者意圖：
語言質地：
禁止漂移：
本輪目標：
```

---

## A.2 完整啟動填寫表

```text
WRITING_RUNTIME_BOOT {
  mode:
    BASIC / STORY_LOCAL / FULL_LIHUO

  project_name:

  current_volume:

  current_chapter:

  current_scene:

  existing_context:

  author_intent:

  genre:

  aesthetic_texture:

  core_conflict:

  character_focus:

  world_rules:

  forbidden_smoothing:

  forbidden_drift:

  author_obsession:

  output_goal:
    node_options / low_res_trace / full_stitching / audit / rewrite
}
```

---

## A.3 簡易啟動範例

```text
啟動理火寫作 Runtime V2.0。

mode = STORY_LOCAL

作品：《觀止青樓》

當前場景：
辭歲掛牌後第二夜，大堂傳聞正在發酵，顧三五十兩買空洛水居之事已經被部分人聽說，但真相尚未公開。

作者意圖：
讓傳聞開始影響辭歲的身價，但不能讓所有人知道洛水居內發生了什麼。

語言質地：
慢、暗、帶一點風月場的黏滯感。

禁止漂移：
不得讓潘金蓮全知。
不得讓顧三突然深情。
不得讓傳聞直接變真相。
不得讓辭歲被全樓理解。
```

---

## A.4 節點選項生成模板

AI 每次只提出三個節點選項。

```text
NODE_OPTIONS {
  current_node:

  A1:
    type: 保守推進
    title:
    what_changes:
    cost:
    risk:
    forbidden_closure:

  A2:
    type: 張力推進
    title:
    what_changes:
    cost:
    risk:
    forbidden_closure:

  A3:
    type: 偏斜推進
    title:
    what_changes:
    cost:
    risk:
    forbidden_closure:

  recommendation:
}
```

---

## A.5 節點選項輸出範例

```text
目前節點：A｜傳聞開始碰到辭歲

A1｜保守推進：傳聞只在姑娘之間低聲流動  
what_changes:
  辭歲沒有被直接波及，但大堂氣氛開始變。  
cost:
  事件推進較慢。  
risk:
  場面可能偏靜。  
forbidden_closure:
  不得讓傳聞被確認為真相。  

A2｜張力推進：一名新客當面試探辭歲  
what_changes:
  傳聞首次變成對辭歲的公開壓力。  
cost:
  辭歲必須面對被定價的凝視。  
risk:
  若處理不好，會讓關係跳級。  
forbidden_closure:
  不得讓新客知道洛水居內情。  

A3｜偏斜推進：宋蕙蓮聽見半句，誤會方向變歪  
what_changes:
  傳聞不直接靠近辭歲，而是先在旁人心裡變形。  
cost:
  未來可能產生錯誤敵意或錯誤同情。  
risk:
  旁線增加。  
forbidden_closure:
  不得讓宋蕙蓮成為真相掌握者。  

建議：
若要穩住場，選 A1。
若要提高可讀張力，選 A2。
若要留下後續旁線，選 A3。
```

---

## A.6 作者選擇格式

作者可簡單輸入：

```text
選 A2
```

或：

```text
選 A3，但不要讓宋蕙蓮變成敵人，只讓她誤會辭歲已經有靠山。
```

或：

```text
A1 和 A3 混合，傳聞先低聲流動，宋蕙蓮只聽見一半。
```

AI 必須接受作者裁決。

若作者混合兩個節點，AI 應重新建立合併節點，不得私自加第三條主線。

---

## A.7 低解析推演模板

```text
LOW_RES_TRACE {
  from_node:
  selected_node:
  to_node:

  what_happens:

  character_changes:

  relation_changes:

  world_changes:

  knowledge_changes:

  rumor_changes:

  unresolved_residue:

  forbidden_closure:

  next_node_pressure:

  nsde_lite_status:
}
```

---

## A.8 低解析推演範例

```text
LOW_RES_TRACE A→B

selected_node:
  A3｜宋蕙蓮聽見半句，誤會方向變歪

what_happens:
  宋蕙蓮在側廊聽見兩名姑娘談起「洛水居一炷香」與「五十兩買空」。
  她沒有聽見完整前因，只聽出辭歲昨夜似乎被某位客人高價留住。
  她沒有立刻問辭歲，也沒有告訴潘金蓮。

character_changes:
  宋蕙蓮對辭歲的判斷從「新來姑娘」變成「可能有手段的新來姑娘」。
  辭歲本人不知道宋蕙蓮聽見了這段傳聞。
  潘金蓮仍只掌握帳本與回報，不知道宋蕙蓮的誤會。

relation_changes:
  宋蕙蓮與辭歲的關係密度從 1_同場 升至 3_傳聞。
  不得升級為敵意、信任、嫉妒或合作。

world_changes:
  傳聞開始在姑娘層流動，但尚未進入客人層。
  大堂氣壓輕微變化。

knowledge_changes:
  宋蕙蓮 knowledge_source = RUMOR。
  宋蕙蓮 knows = 聽說辭歲昨夜被高價留住。
  宋蕙蓮 does_not_know = 洛水居內實際發生什麼。

rumor_changes:
  rumor_topic = 洛水居一炷香。
  distortion_level = MEDIUM。
  allowed_effect = 低聲議論、試探、錯誤期待。
  forbidden_effect = 真相揭露、關係定案、全樓共識。

unresolved_residue:
  宋蕙蓮可能在下一節點試探辭歲。
  傳聞可能變形為「辭歲有靠山」。
  此事暫不進入真相層。

forbidden_closure:
  不得讓宋蕙蓮直接知道顧三真正想法。
  不得讓辭歲立刻知道所有傳聞。
  不得讓全樓同時理解辭歲價值。

next_node_pressure:
  B 節點可選：
    B1｜宋蕙蓮暫時旁觀。
    B2｜宋蕙蓮用一句話試探辭歲。
    B3｜傳聞先傳到某位新客耳中。

nsde_lite_status:
  PASS_WITH_WARNINGS
```

---

## A.9 節點停止指令

作者可隨時停止節點推演：

```text
停在這裡，開始縫合。
```

```text
節點夠了，先做節點鏈審計。
```

```text
不要再推新節點，先整理目前故事鏈。
```

---

## A.10 節點鏈整理模板

```text
NODE_CHAIN_SUMMARY {
  chain_id:

  selected_nodes:

  rejected_paths:

  main_story_line:

  character_state_changes:

  relation_density_changes:

  rumor_state:

  unresolved_residue:

  forbidden_future_closure:

  ready_for_stitching:
    YES / NO / HOLD
}
```

---

## A.11 正文縫合指令

```text
根據目前節點鏈，進入 FULL_STITCHING。
要求：
1. 不改變已選節點。
2. 不新增重大因果。
3. 保留傳聞的不確定性。
4. 保留人物知情邊界。
5. 語言質地維持：
6. 字數：
```

---

## A.12 正文縫合輸出規則

正文縫合時，AI 只輸出正式文本。

除非作者要求，否則不附技術報告。

若作者要求附審計，正文後可附：

```text
NSDE_STATUS:
LITERARY_STATUS:
REMAINING_RESIDUE:
```

---

## A.13 節點鏈最小命令集

```text
啟動節點鏈。
給我三個節點。
選 A2。
低解析推演。
繼續給 B 節點。
停。
整理節點鏈。
做 NSDE 審計。
開始縫合正文。
補旁線。
輸出 LOG。
生成 SEED。
```

---

# 附錄 B｜NSDE 審計表

## NSDE AUDIT FORMS

---

## B.0 附錄定位

本附錄提供理火寫作 Runtime V2.0 中 NSDE 的標準審計格式。

NSDE 不評文筆。

NSDE 評估敘事是否合法：

```text
人物是否還是自己。
世界是否仍遵守規則。
因果是否承接。
關係是否跳級。
思想是否真的被世界執行。
爽感是否污染結構。
```

---

## B.1 NSDE-Lite 快速審計表

適用於 STORY_LOCAL 模式。

```text
NSDE_LITE_REPORT {
  scope:

  causality_trace:
    status:
    note:

  character_attractor_check:
    status:
    note:

  world_rule_check:
    status:
    note:

  relation_change_check:
    status:
    note:

  closure_pressure_check:
    status:
    note:

  pvi_check:
    status:
    note:

  dds_level:
    D0 / D1 / D2 / D3 / D4 / D5

  final_status:
    PASS / PASS_WITH_WARNINGS / HOLD / STOP

  required_repair:
}
```

---

## B.2 NSDE-Lite 判定標準

### `causality_trace`

```text
PASS:
  重大事件均有可追溯原因。

WARN:
  有情緒或行動發生，但過渡略薄。

HOLD:
  重大結果缺少原因。

STOP:
  因果鏈斷裂，後文無法承接。
```

---

### `character_attractor_check`

```text
PASS:
  角色行為符合其核心吸引子。

WARN:
  角色有偏移，但可由壓力解釋。

HOLD:
  角色反應缺少心理或事件來源。

STOP:
  角色身份崩壞，不再像同一個人。
```

---

### `world_rule_check`

```text
PASS:
  世界規則穩定。

WARN:
  有便利化傾向，但尚未破壞。

HOLD:
  劇情為了方便開始折彎世界規則。

STOP:
  世界規則被破壞。
```

---

### `relation_change_check`

```text
PASS:
  關係變化有事件、代價與見證範圍。

WARN:
  關係推進略快。

HOLD:
  關係跳級，需要補事件。

STOP:
  無因信任、無因倒貼、無因仇恨。
```

---

### `closure_pressure_check`

```text
PASS:
  未完成被保留。

WARN:
  場景開始有過早總結傾向。

HOLD:
  核心衝突被過早解釋。

STOP:
  故事假完成。
```

---

### `pvi_check`

```text
PASS:
  爽感有代價、有後果、有反撲。

WARN:
  爽感偏高，但仍可補代價。

HOLD:
  爽感開始污染世界規則。

STOP:
  主角無成本勝利，結構失效。
```

---

## B.3 DDS 漂移分級表

```text
DDS {
  D0:
    name: no_drift
    action: PASS
    description: 無漂移。

  D1:
    name: style_surface_drift
    action: NOTE
    description: 表層語氣或句式略有漂移。

  D2:
    name: emotional_transition_weakness
    action: WARN
    description: 情緒變化過渡不足，需要橋段。

  D3:
    name: causality_break
    action: HOLD
    description: 因果斷裂，不得直接繼續。

  D4:
    name: identity_collapse
    action: STOP
    description: 人物身份崩壞，需要重建。

  D5:
    name: world_rule_corruption
    action: STOP_AND_REVIEW_WORLD_RULE
    description: 世界規則腐蝕，需回退審查。
}
```

---

## B.4 NSDE-Full 報告模板

適用於 FULL_LIHUO 模式或重大章節審計。

```text
NSDE_FULL_REPORT {
  title:

  scope:

  memory_sources:

  evidence_scope:

  IVI:
    score:
    status:
    reason:
    evidence:

  REI:
    score:
    status:
    reason:
    evidence:

  ACS:
    score:
    core_attractors:
    stability:
    contradiction_status:
    evidence:

  DDS:
    level:
    triggered_constraints:
    repair_needed:

  PVI:
    level:
    pleasure_source:
    structural_cost:
    pollution_risk:
    required_balance:

  NSR:
    tier:
    status:
      not_triggered / latent / partial / confirmed
    reason:

  causality_trace:

  world_rule_status:

  relation_change_status:

  unresolved_questions:

  final_judgment:
    PASS / PASS_WITH_WARNINGS / HOLD / STOP

  required_actions:
}
```

---

## B.5 IVI 評分表

IVI 評估思想替代潛力。

```text
IVI_SCORE {
  original_legitimacy_identification: 0-20
  ideological_negation_intensity: 0-30
  civilizational_reframing: 0-30
  replacement_value_clarity: 0-40
  total: 0-120
}
```

說明：

```text
IVI 高，代表思想層強。
但 IVI 高不代表劇情已經執行。
```

---

## B.6 REI 評分表

REI 評估思想是否已進入世界運行。

```text
REI_SCORE {
  executed_power_shift: 0-30
  irreversible_consequence: 0-30
  world_response: 0-20
  institutional_or_social_embedding: 0-20
  sustained_runtime_effect: 0-20
  total: 0-120
}
```

說明：

```text
主角宣言不是 REI。
內心獨白不是 REI。
世界真的改變，才是 REI。
```

---

## B.7 ACS 評分表

ACS 評估人物吸引子一致性。

```text
ACS_SCORE {
  core_drive_persistence: 0-25
  stress_response_consistency: 0-25
  contradiction_pattern_consistency: 0-25
  relational_behavior_consistency: 0-25
  total: 0-100
}
```

判定：

```text
90-100:
  角色穩定，矛盾有效。

75-89:
  基本穩定，局部需補橋。

60-74:
  有漂移風險。

40-59:
  人物可能已偏離吸引子。

0-39:
  身份崩壞。
```

---

## B.8 PVI 評估表

PVI 評估爽感污染。

```text
PVI_REPORT {
  pleasure_type:
    victory / romance / revenge / recognition / power_gain / rescue / humiliation / wealth / status

  pleasure_intensity:
    LOW / MEDIUM / HIGH / EXTREME

  cost_present:
    YES / NO / PARTIAL

  backlash_present:
    YES / NO / DELAYED

  world_rule_respected:
    YES / NO / DAMAGED

  character_integrity_respected:
    YES / NO / DAMAGED

  pollution_status:
    CLEAN / WATCH / POLLUTED / STRUCTURAL_DAMAGE

  required_repair:
}
```

---

## B.9 PVI 修復規則

若爽感污染，優先使用以下修復：

```text
PVI_REPAIR {
  add_cost:
    增加代價。

  add_delay:
    延遲成果。

  add_backlash:
    增加反撲。

  downgrade_gain:
    降低獲得程度。

  restore_enemy_pressure:
    恢復對手能力。

  restore_world_rule:
    恢復世界規則。

  split_reward:
    讓勝利只完成一部分。
}
```

禁止修復方式：

```text
不得用一句旁白說「其實也有代價」。
不得用抽象痛苦取代具體代價。
不得用未來可能反撲取代當下結構成本。
```

---

## B.10 NSDE 最終判定矩陣

```text
NSDE_FINAL_MATRIX {

  PASS:
    結構成立，可進入正文或保留。

  PASS_WITH_WARNINGS:
    結構基本成立，但需注意局部漂移或補橋。

  HOLD:
    暫停，不得進入正文縫合。
    需修復因果、人物、關係或世界規則。

  STOP:
    停止。
    必須回退至上一個合法節點。

}
```

---

# 附錄 C｜文學評價表

## LITERARY EVALUATION FORMS

---

## C.0 附錄定位

本附錄用於評價文本的文學效果。

文學評價不得取代 NSDE。

NSDE 問：

```text
這段是否合法？
```

文學評價問：

```text
這段是否有效？
```

理火問：

```text
這段是否取得生成權？
```

---

## C.1 文學評價總表

```text
LITERARY_REPORT {
  scope:

  language_texture:
    status:
    note:

  rhythm_control:
    status:
    note:

  image_residue:
    status:
    note:

  dialogue_vitality:
    status:
    note:

  scene_density:
    status:
    note:

  character_presence:
    status:
    note:

  emotional_aftertaste:
    status:
    note:

  originality_pressure:
    status:
    note:

  readability:
    status:
    note:

  reread_value:
    status:
    note:

  overall_literary_status:
    STRONG / WORKABLE / FLAT / OVERWRITTEN / UNDERCOOKED / AI_SMOOTHED / STYLE_DRIFT

  recommended_revision:
}
```

---

## C.2 評價狀態

```text
LITERARY_ITEM_STATUS:
  STRONG
  WORKABLE
  WEAK
  FLAT
  OVERDONE
  UNDERCOOKED
  DRIFTED
```

---

## C.3 語言質地 `language_texture`

問題：

```text
這段文字是不是作者要的質地？
```

檢查：

```text
笨是否夠笨？
雅是否真雅？
粗是否有生命？
冷是否不假？
爽是否不爛？
荒唐是否有準頭？
慢是否有張力？
碎是否仍可讀？
```

失敗模式：

```text
AI 自動美化。
AI 自動文雅化。
AI 自動冷感化。
AI 自動勵志化。
AI 自動總結化。
AI 把作者的粗糙執念磨平。
```

---

## C.4 節奏控制 `rhythm_control`

問題：

```text
這段有沒有呼吸？
```

檢查：

```text
是否全程同速？
是否每段都像結論？
是否張力只升不落？
是否缺少停頓？
是否缺少沉默？
是否沒有斷裂？
是否句長過於平均？
```

強節奏不等於快。

慢也可以有節奏。

---

## C.5 意象殘留 `image_residue`

問題：

```text
讀完後，有沒有東西留在場裡？
```

可留下的東西：

```text
一盞燈
一道水痕
一句沒說完的話
一件小物
一種氣味
一個姿勢
一點聲音
一道視線
一個錯過
```

失敗模式：

```text
形容詞很多，但沒有殘留。
畫面很漂亮，但讀完就散。
意象只服務美感，不服務故事。
```

---

## C.6 對話活性 `dialogue_vitality`

問題：

```text
這些人像不像真的在說話？
```

允許：

```text
重複
岔題
嘴硬
口誤
廢話
沉默
誤會
不回答
顧左右而言他
半句話
說錯重來
```

失敗模式：

```text
每句都交換資訊。
每句都推主線。
每句都像人物自我分析。
每句都太聰明。
每句都太完整。
每句都像 AI 在寫教科書。
```

---

## C.7 場景密度 `scene_density`

問題：

```text
這場戲是不是發生在一個真正的地方？
```

檢查：

```text
空間是否影響人物？
物件是否影響對話？
旁人是否有低密度反應？
光線、聲音、氣味是否有作用？
人物站位是否產生關係？
場面是否存在不可控因素？
```

失敗模式：

```text
人物像站在白房間裡說話。
空間只是背景板。
物件只是裝飾。
旁人完全不存在。
```

---

## C.8 人物在場感 `character_presence`

問題：

```text
人物是不是以自己的方式存在？
```

來源：

```text
姿態
語氣
習慣
猶豫
誤判
邊界
反應速度
注意力方向
不說出口的部分
```

失敗模式：

```text
人物只剩功能。
人物只剩設定。
人物只剩台詞。
人物被旁白替代。
人物全都用同一種語氣說話。
```

---

## C.9 情緒後味 `emotional_aftertaste`

問題：

```text
情緒有沒有留下餘波？
```

檢查：

```text
情緒是否太直白？
是否被旁白說死？
是否所有人同一種情緒？
是否有未說出口的部分？
是否有殘留？
是否有反向情緒？
```

失敗模式：

```text
直接說「他很難過」。
直接說「她很感動」。
直接說「兩人都明白了」。
情緒被總結掉。
```

---

## C.10 原創壓力 `originality_pressure`

問題：

```text
文本是否正在滑向高機率套路？
```

檢查：

```text
是否像常見網文模板？
是否像 AI 默認美文？
是否像影評腔？
是否像勵志文？
是否像角色卡說明？
是否像安全、平衡、無害但無生命的回答？
```

不是所有套路都禁止。

但套路必須被作者使用，而不是作者被套路帶走。

---

## C.11 可讀性 `readability`

問題：

```text
讀者能不能被帶著往下走？
```

檢查：

```text
是否有鉤子？
是否資訊過密？
是否抽象過多？
是否段落太長？
是否缺少節奏斷點？
是否視角清楚？
是否能理解當下發生什麼？
```

可讀不等於簡單。

複雜也可以可讀。

---

## C.12 重讀價值 `reread_value`

問題：

```text
第二次讀，是否能看到第一次沒看到的東西？
```

來源：

```text
伏筆
殘煙
誤認
物件
語氣差異
人物不知情
雙重意思
未完成的沉默
```

失敗模式：

```text
第一次讀完已經全部用完。
沒有回頭看的必要。
所有意思都被旁白說死。
```

---

## C.13 文學評價與 NSDE 組合判定

```text
STRUCTURE_LITERATURE_MATRIX {

  NSDE_PASS + LITERARY_STRONG:
    可用，建議保留。

  NSDE_PASS + LITERARY_FLAT:
    結構成立，但文字需重寫。

  NSDE_PASS + STYLE_DRIFT:
    結構成立，但偏離作者美學，需改語氣。

  NSDE_HOLD + LITERARY_STRONG:
    文字好，但不可直接使用，需修因果。

  NSDE_FAIL + LITERARY_STRONG:
    美文污染，必須回退。

  NSDE_PASS + PVI_POLLUTED:
    爽感污染，需加代價、延遲或反撲。

  NSDE_PASS + AI_SMOOTHED:
    需恢復作者執念、粗糙、停頓或不對稱。
}
```

---

# 附錄 D｜全套理火寫作調用表

## FULL LIHUO WRITING HANDOFF FORM

---

## D.0 附錄定位

本附錄用於在寫作 Runtime 中調用完整理火主程序。

完整理火不是普通修文工具。

完整理火只在高風險結構節點、重大漂移、作者明確要求正式審計、或需要 CCC-R 二輪競爭時啟動。

---

## D.1 調用條件表

```text
FULL_LIHUO_HANDOFF_TRIGGER {
  author_requested_full_lihuo:
    YES / NO

  identity_collapse:
    YES / NO

  causality_break:
    YES / NO

  world_rule_corruption:
    YES / NO

  false_closure:
    YES / NO

  emotion_field_pollution:
    YES / NO

  pvi_pollution:
    YES / NO

  node_chain_instability:
    YES / NO

  ccc_r_required:
    YES / NO

  formal_audit_required:
    YES / NO
}
```

若任一重大項目為 YES，可進入 FULL_LIHUO_HANDOFF_REQUEST。

---

## D.2 調用請求模板

```text
FULL_LIHUO_HANDOFF_REQUEST {
  source_runtime:
    LIHUO_WRITING_RUNTIME_V2

  reason_for_handoff:

  current_node:

  node_chain_summary:

  suspected_failure:

  required_lihuo_functions:
    FORMAL_LAMP_STATE
    LIGHT_TRACE_FORMAL
    SAC_FULL
    KAIROS_CHECK
    CCC / CCC-R
    NSDE_FULL
    STRUCTURAL_AUDIT
    INTERVENTION_PROPOSAL

  author_authorization:
    REQUIRED / PROVIDED
}
```

---

## D.3 完整理火寫作審計輸出

```text
FULL_LIHUO_WRITING_AUDIT {
  status:
    PASS / HOLD / FAIL

  formal_lamp_state_summary:

  light_trace_summary:

  sac_full_observation:

  kairos_status:

  ccc_status:

  nsde_full_status:

  structural_failure_points:

  authorized_intervention:

  repair_options:

  return_to_writing_runtime:
    YES / NO
}
```

---

## D.4 調用後回流規則

完整理火完成後，必須回到寫作 Runtime。

```text
FULL_LIHUO_RETURN_RULE {
  IF PASS:
    return_to_full_stitching_or_continue_node_chain

  IF HOLD:
    repair_node_chain_before_prose

  IF FAIL:
    rollback_to_last_valid_node

  IF INTERVENTION_REQUIRED:
    require_author_selection_before_rewrite
}
```

AI 不得在完整理火審計後自行重寫整個故事，除非作者授權。

---

# 附錄 E｜LOG 與 SEED 模板

## WRITING LOG AND SEED TEMPLATES

---

## E.1 寫作 LOG

```text
WRITING_LOG {
  project:

  volume:

  chapter:

  scene:

  runtime_mode:
    BASIC / STORY_LOCAL / FULL_LIHUO

  author_intent:

  selected_nodes:

  rejected_paths:

  scene_field:

  active_characters:

  character_position_changes:

  relation_density_changes:

  rumor_changes:

  world_changes:

  unresolved_residue:

  old_clue_status:

  nsde_status:

  literary_status:

  next_possible_entry:
}
```

---

## E.2 重入 SEED

```text
WRITING_SEED {
  project:

  current_position:

  last_valid_node:

  author_intent:

  aesthetic_texture:

  active_conflicts:

  active_characters:

  character_position_boxes:

  relation_density_map:

  rumor_state:

  unresolved_residue:

  locked_out_elements:

  old_clue_policy:

  nsde_warnings:

  next_node_options:

  suggested_runtime_mode:
}
```

---

## E.3 最小接關摘要

```text
MIN_CONTINUATION_SEED {
  現在寫到哪裡：
  上一個有效節點：
  誰知道什麼：
  誰不知道什麼：
  關係變化：
  傳聞狀態：
  未解殘煙：
  下一步可選：
}
```

---

# 附錄 F｜快速使用命令

## QUICK COMMANDS

---

## F.1 啟動

```text
啟動理火寫作 Runtime V2.0。
```

```text
用 STORY_LOCAL 模式，先不要寫正文，只走節點。
```

```text
用 FULL_LIHUO 模式，做正式理火寫作審計。
```

---

## F.2 節點

```text
給我三個節點選項。
```

```text
選 A2。
```

```text
A1 和 A3 混合，重新整理成一個合法節點。
```

```text
低解析推演到下一節點。
```

```text
停在這裡，不要再推。
```

---

## F.3 審計

```text
做 NSDE-Lite。
```

```text
做 NSDE-Full。
```

```text
檢查 ACS。
```

```text
檢查 DDS。
```

```text
檢查 PVI 爽感污染。
```

```text
檢查人物是否全知。
```

```text
檢查傳聞是否變成真相。
```

---

## F.4 縫合

```text
根據節點鏈縫合正文。
```

```text
只縫合，不新增重大因果。
```

```text
保留低解析節點，不要擅自改方向。
```

```text
補旁線，但只補 L1-L3。
```

---

## F.5 修復

```text
回退到上一個合法節點。
```

```text
修復因果，不要重寫全部。
```

```text
重建人物立場盒。
```

```text
降級傳聞，不要讓它變真相。
```

```text
爽感太高，補代價。
```

```text
情緒場污染，重建各人物情緒。
```

---

## F.6 保存

```text
輸出 WRITING_LOG。
```

```text
生成下一次接關 SEED。
```

```text
輸出最小接關摘要。
```

---

# 附錄總結

```text
附錄 A：
  教 AI 怎麼走節點。

附錄 B：
  教 AI 怎麼審結構。

附錄 C：
  教 AI 怎麼評文學。

附錄 D：
  教 AI 何時調用完整理火。

附錄 E：
  教 AI 怎麼留下接關記。

附錄 F：
  給作者快速操作命令。
```

最高口訣：

```text
先選節點。
再低解析。
再審合法。
再縫正文。
再補旁線。
再留接關。

寫作不是一次生成。
寫作是可追溯的顯影。
```
