# 《九尾龜》RUNTIME BINDING MANIFEST V1.2
## KAIROS Situational Maturity JWG Test Hook × Relational-World Long-Run Regression × No Formal KAIROS Upgrade

```yaml
DOCUMENT:
  title: "JIUWEIGUI RUNTIME BINDING MANIFEST"
  version: "V1.2"
  date: "2026-09-03"
  document_type: "PROJECT_VERTICAL_RUNTIME_BINDING_SUCCESSOR / JWG_KAIROS_SITUATIONAL_TEST_HOOK"
  status: "FORMAL_PROJECT_BINDING_SPEC_SUCCESSOR / TEST-HOOK-ENABLED / NO_WORLD_FACT_AUTHORITY / NO_HOST_DEPLOYMENT_CLAIM"

REVISION_LINEAGE:
  parent:
    file: "九尾龜_RUNTIME_BINDING_MANIFEST_V1.1_LIHUO_LIGHTER_V3.5.1_MAIN_ROUTING_REBIND版(1).md"
    version: "V1.1"
    sha256: "86f9e746df631c906d65d21a361301edc60aaef18c7f19057a3b710c3f43e2f3"
    treatment: "FULL_INHERITANCE_EXCEPT_EXPLICIT_V1_2_SUPERSESSION"

  reasons:
    - "JWG Environment C002 exposed unnecessary-confirmation as a local scene-reading failure candidate."
    - "Relational-world research expanded the problem from confirmation style to situational qualification of speech/action."
    - "KAIROS_GATE_V0.1-JWG-TEST is READY_FOR_EXPERIMENT but explicitly NOT a formal KAIROS upgrade or Main-System patch."
    - "A project-level test hook is therefore added without changing formal Main-System KAIROS semantics."

GOVERNING_CURRENT:
  protocol: "LIHUO PROTOCOL V2.3"
  lighter: "LIHUO LIGHTER V3.5.1-EXP"
  ai_system: "LIHUO AI SYSTEM V3.5-EXP"
  main_world: "JIUWEIGUI MAIN WORLD V0.4-FULL"
  world_database: "V0.1-FULL"
  character_pool: "V0.2-FULL-ALL-SOURCE"
  adult_runtime: "V2.0-FULL"
  route_memory: "V0.3-FULL"
  environment: "JWG ENVIRONMENT V0.5 / NOT WORLD AUTHORITY"
  miscellany: "LIHUO MISCELLANY V3.0 / NON-NORMATIVE"

TEST_GATE_SOURCE:
  file: "KAIROS_GATE_V0.1-JWG-TEST_情境成熟性審計_九尾龜關係世界長距離測試版.md"
  version: "V0.1-JWG-TEST"
  sha256: "7f35ed6aedaffaf712d1dcc8a85d62a123671ea35040b4bb1be6d707442298c7"
  source_status: "EXPERIMENTAL / TEST-ONLY / READY_FOR_EXPERIMENT"
  formal_kairos_upgrade: false
  main_system_patch: false
  host_deployment_claim: false

VERSION_COMPATIBILITY:
  protocol_version_bump_required: false
  lighter_version_bump_required: false
  ai_system_version_bump_required: false
  jwg_main_world_version_bump_required: false
  adult_runtime_version_bump_required: false
  route_memory_version_bump_required: false

  reason:
    - "V1.2 adds a JWG project test hook, not a formal LIHUO core semantic replacement."
    - "Formal KAIROS remains the current AI-System KAIROS definition until a later explicit successor."
```

> **V1.2 根句：先讓候選語言／行動接受「此時、此地、此局是否成熟」的測試，再讓世界顯影；但測試 Gate 不是人物、不是世界，也不是新的 KAIROS 王位。**

---

# 1｜V1.2 現行專案拓撲

```text
HOST SYSTEM BOUNDARY
↓
LIHUO PROTOCOL V2.3
↓
LIHUO LIGHTER V3.5.1-EXP
│  MAIN INVOCATION AUTHORITY
│
├── JIUWEIGUI MAIN WORLD V0.4
│   │  WORLD / EVENT / CHARACTER DECISION / LIVE KNOWLEDGE
│   │
│   ├── WORLD DATABASE V0.1
│   ├── CHARACTER POOL V0.2
│   ├── ADULT RUNTIME V2.0
│   └── ROUTE MEMORY V0.3
│
│   JWG CANDIDATE SPEECH / ACTION
│        ↓
│   KAIROS_GATE_V0.1-JWG-TEST
│   [TEST-ONLY PRE-MANIFEST SITUATIONAL AUDIT]
│        ↓
│   TEST RESULT: STAY / WAIT / HOLD / STOP / PASS
│        ↓
│   RETURN TO JWG MAIN WORLD
│        ↓
│   MAIN WORLD retains final world / character decision authority
│
└── IF existing Lighter V3.5.1 field-distortion / Main-owned capability signal is met
     ↓
   JWG reports signal
     ↓
   LIGHTER decides scoped Main attachment
     ↓
   LIHUO AI SYSTEM V3.5-EXP
     ↓
   RETURN
```

硬鎖：

```text
KAIROS TEST GATE != FORMAL LIHUO KAIROS UPGRADE
KAIROS TEST RESULT != CHARACTER DECISION
KAIROS TEST RESULT != WORLD FACT
PASS != NPC MUST DO IT
STAY != NPC MUST BE SILENT
WAIT != PERMANENTLY FORBIDDEN
HOLD != CLOSED
STOP != GLOBAL HOST PROHIBITION

TEST GATE MAY NOT AUTHORIZE MAIN
TEST GATE MAY NOT VETO LIGHTER
TEST GATE MAY NOT CREATE CONSENT
TEST GATE MAY NOT WRITE SAVE FACTS
```

---

# 2｜Test Hook Invocation Contract

```yaml
JWG_KAIROS_TEST_HOOK:

  scope:
    mode:
      - "STORY candidate generation"
      - "director long-run regression"
    default_frontstage_visibility: "HIDDEN"
    story_time_advance_by_gate_itself: false
    save_write_by_gate_itself: false

  input:
    required:
      - "WORLD STATE"
      - "CHARACTER LOCAL KNOWLEDGE"
      - "CANDIDATE SPEECH OR ACTION"
    optional:
      - "LOCAL GONGJIA PROFILE"
      - "KNOWN AUDIENCE"
      - "PRIOR CONTRACT / EVENT TRIGGER"
      - "MATERIAL TRANSITION FLAGS"

  audit_axes:
    - "TIME"
    - "PLACE"
    - "EVENT"
    - "ENVIRONMENT"
    - "INFORMATION"
    - "AUDIENCE"
    - "RELATION"
    - "MATERIALITY"

  output:
    status:
      - "STAY"
      - "WAIT"
      - "HOLD"
      - "STOP"
      - "PASS"
    evidence_anchor_required: true
    hidden_reasoning_not_required_in_frontstage: true

  return_to:
    owner: "JIUWEIGUI MAIN WORLD V0.4"
    meaning:
      - "Gate only returns situational maturity audit."
      - "Main World still owns whether an NPC actually chooses an eligible action."
```

---

# 3｜Enforcement Semantics of the Test

這次「上線」不是把 Gate 變成世界主權。

測試方式：

```text
CANDIDATE GENERATED
↓
GATE AUDIT
↓
IF PASS
  → candidate retains manifestation eligibility
  → Main World still decides actual selection / world effect

IF STAY
  → do not add candidate merely to explain an already-running world
  → allow existing world action / silence / other qualified path to continue

IF WAIT
  → candidate may remain future-eligible
  → current manifestation deferred

IF HOLD
  → preserve unresolved state
  → do not force closure

IF STOP
  → candidate is rejected for current state because it conflicts with
     world / local knowledge / qualification / material boundary
```

因此：

```text
GATE HAS PRE-MANIFEST TEST EFFECT
!=
GATE OWNS WORLD
```

---

# 4｜與正式 KAIROS 的分離

現行 AI System V3.5 的 KAIROS 仍維持既有正式語義：

```text
KAIROS
→ temporal legitimacy
→ 「現在是不是時候？」
```

V1.2 不偷偷改成：

```text
KAIROS
=
TIME × PLACE × EVENT × ENVIRONMENT × INFORMATION × AUDIENCE × RELATION × MATERIALITY
```

八面式目前只在：

```text
KAIROS_GATE_V0.1-JWG-TEST
```

中成立。

未來只有經過：

```text
long-run tests
+ counterexamples
+ state-sensitive flips
+ cross-world reconstruction
+ formal version decision
```

才可以評估正式 KAIROS successor。

---

# 5｜C002 / 功架 Profile 的位置

```text
GENERAL GATE CORE
→ 情境成熟性怎麼審計

LOCAL GONGJIA PROFILE
→ 上海／風月場裡哪些訊號與分寸有地方意義
```

所以：

```text
GONGJIA != KAIROS
LOCAL CUSTOM != UNIVERSAL HUMAN LAW
```

《九尾龜》Corpus 的「功架」仍只作來源範圍內的 social-capability evidence。

Environment C002 的 derived criterion 仍是 experiment。

Gate 可以使用 local profile，但不能反向把：

```text
「上海風月場不長眼」
```

寫成：

```text
「全世界所有人際場合的固定規則」
```

---

# 6｜與 SAC / Main Routing 的位置

V1.2 不把八面 Gate 變成 SAC 替代品。

```text
KAIROS TEST GATE
→ candidate manifestation maturity

SAC / Main
→ relational field / PATH competition / generative field intervention
```

當 Gate 只靠已成立 world state 就能判斷：

```text
付款節點尚未到
→ WAIT
```

不需要因此叫 Main。

當 Gate 發現：

```text
relation meaning genuinely multi-path
+
weak signals compete
+
single-path template is collapsing the field
```

它只能輸出：

```text
OBSERVABLE DISTORTION / CAPABILITY NEED SIGNAL
```

再回到：

```text
LIHUO LIGHTER V3.5.1
```

由 Lighter 決定是否 scoped Main attach。

---

# 7｜本輪 Regression 目標

```yaml
V1_2_JWG_KAIROS_TEST_METRICS:
  primary:
    - "redundant_confirmation_rate DOWN"
    - "premature_question_rate DOWN"
    - "over_inference_rate NO INCREASE"
    - "missed_material_confirmation_rate NO INCREASE"
    - "audience_leak_rate DOWN"
    - "character_knowledge_leak_rate NO INCREASE"
    - "relation_overclosure_rate NO INCREASE"
    - "false_stay_rate NO INCREASE"
    - "state_sensitive_flip_accuracy UP"
    - "stay_competence UP"

  anti_theater:
    - "same wording + changed world state must be able to flip result"
    - "not every social scene should STAY"
    - "not every uncertainty should ASK"
    - "silence must not become fixed high-status style"
```

---

# 8｜SAVE / HOT handling

```text
THIS BINDING UPDATE
!= WORLD EVENT
```

所以：

```yaml
SAVE_POLICY:
  rewrite_existing_HOT_V0_4: false
  route_world_delta: "NONE"
  relation_delta: "NONE"
  knowledge_delta: "NONE"
  money_delta: "NONE"

  future_save:
    note:
      - "A later requested SAVE may refresh runtime/test-profile reference."
      - "Do not create a SAVE merely because binding changed."
```

---

# 9｜Evidence Status

```yaml
V1_2_EVIDENCE:
  E1_GATE_DOCUMENT_PRESENT:
    value: true

  E2_GATE_READY_FOR_EXPERIMENT:
    value: true
    source: "KAIROS_GATE_V0.1-JWG-TEST"

  E3_PROJECT_TEST_BINDING_DECLARED:
    value: true

  E4_STATIC_AUTHORITY_SEPARATION_CHECK:
    value: "PASS"
    checks:
      - "Main World remains world/character authority"
      - "Gate cannot authorize Main"
      - "Lighter retains Main invocation"
      - "Formal AI-System KAIROS unchanged"
      - "No SAVE rewrite"
      - "No consent/relation authority transfer"

  E5_LONG_RUN_JWG_REGRESSION:
    value: false
    note: "Test hook has just been bound; long-run evidence must be accumulated in STORY."

  E6_FORMAL_KAIROS_UPGRADE:
    value: false

  E7_HOST_ENFORCED:
    value: "UNKNOWN"
    rule: "Project binding declaration != host enforcement proof."
```

---

# 10｜CURRENT JWG PROJECT BINDING

```yaml
CURRENT_JWG_RUNTIME_BINDING_V1_2:
  protocol: "LIHUO PROTOCOL V2.3"
  lighter: "LIHUO LIGHTER V3.5.1-EXP"
  ai_system: "LIHUO AI SYSTEM V3.5-EXP / conditional SAC-dependent provider"
  main_world: "JIUWEIGUI MAIN WORLD V0.4-FULL"
  world_database: "V0.1-FULL"
  character_pool: "V0.2-FULL-ALL-SOURCE"
  adult_runtime: "V2.0-FULL"
  route_memory: "V0.3-FULL"

  project_test_hook:
    gate: "KAIROS_GATE_V0.1-JWG-TEST"
    mode: "ACTIVE JWG LONG-RUN EXPERIMENT / PRE-MANIFEST"
    formal_kairos_upgrade: false

  environment: "V0.5 / C002 TEST-HARNESS LINKED / NOT WORLD AUTHORITY"
  engineering_miscellany: "LIHUO MISCELLANY V3.0 / NON-NORMATIVE"
  binding_manifest: "V1.2"

  existing_hot:
    current: "程敬之 HOT V0.4"
    rewritten_by_binding_update: false
```

> **V1.2 最終句：從現在起，《九尾龜》長距離實跑可以真正測「世界已經回答時，AI 能不能閉嘴；世界尚未回答到重大門檻時，AI 又能不能知道該問」。這是 KAIROS 的測試，不是 KAIROS 的加冕。**
