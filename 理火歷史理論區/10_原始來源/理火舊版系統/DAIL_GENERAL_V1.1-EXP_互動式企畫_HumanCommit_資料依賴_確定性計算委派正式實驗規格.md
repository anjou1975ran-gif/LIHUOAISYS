# DAIL GENERAL V1.1-EXP
# Declarative AI Language — General Authoring & Target-Neutral Profile

## 通用 AI 場性宣告語言 × 互動式企畫 × Human Commit × Dependency-First × Deterministic Compute Delegation
## Field-Oriented AI Declaration × Conversational Planning × Human Commit × Dependency-First × Deterministic Compute Delegation

```yaml
DOCUMENT:
  name: "DAIL GENERAL"
  full_name: "Declarative AI Language — General Authoring & Target-Neutral Profile"
  chinese_name: "DAIL 通用型｜宣告式 AI 語言"
  document_version: "V1.1-EXP"
  language_core: "DAIL CORE 2.0-EXP"
  status: "FORMAL_EXPERIMENTAL_GENERAL_SPECIFICATION_MAJOR_AUTHORING_UPGRADE"
  date: "2026-08-26"

  parent_lock:
    file: "DAIL_GENERAL_V1.0-EXP_通用AI場性宣告語言_自然語言編譯_TargetNeutral正式實驗規格.md"
    sha256: "2213cc069132dd456d8a027d35ad5a930cd2dab9774b6dc3c1f450f5b779cddc"
    inheritance: "FULL_EXCEPT_EXPLICIT_V1_1_SUPERSESSION"

  purpose:
    - "將 DAIL 從 LIHUO 專用 Runtime Authoring Profile 抽離為可跨模型、跨 Runtime、跨供應商使用的通用 AI-native 宣告式語言。"
    - "允許人類以自然語言描述 AI 應如何建立世界、保留未知、朝何方向生成、遵守哪些邊界、由誰負責，以及如何顯影。"
    - "將自然語言需求編譯／正規化為可驗證、可交換、可 target-compile 的 DAIL Program。"
    - "讓不同 AI Runtime 在不共享內部實作的情況下，仍可交換同一份語義規格。"
    - "建立產品級 Authoring Shell：先多輪理解需求、形成企畫、掃描缺口，再由人類明確 Commit 後才生成正式 DAIL Program。"
    - "在規格生成前先處理可行性、資料來源、工具、權限與外部依賴，禁止先寫完整規格再補找關鍵資源。"
    - "建立 AI 與確定性計算之責任分工：語義工作交給 AI；SQL 查詢、排序、聚合、JOIN、精確計算等由資料庫／程式執行層完成。"

  relationship:
    dail_lihuo_profile: "SIBLING_PROFILE / SHARED_CORE_SEMANTICS"
    lihuo_required: false
    sac_required: false
    specific_model_required: false
    specific_vendor_required: false

  non_claims:
    - "不宣稱本文件修改任何模型權重、Transformer 架構、宿主安全、底層 Runtime 或硬體。"
    - "不宣稱 DAIL field-oriented abstraction 已被證明等同任何特定 hidden neural geometry。"
    - "不宣稱寫出 DAIL Program 即代表目標 Runtime 已部署、已接線或已強制執行。"
    - "不宣稱目前已存在完整跨供應商 reference compiler / conformance-certified runtime。"
    - "不在本版主張 DAIL 的全球技術優先權或 first-in-world 地位；此類主張需另做 prior-art audit。"
    - "不把使用者願望直接升格成可實作能力。"
    - "不把『AI 可以描述一項計算』誤寫成『AI 應親自執行所有計算』。"
    - "不把資料來源未知、未授權或不存在的狀態，偽裝成完整可執行企畫。"
```

---

# 0｜一句話定位

> **DAIL 是一種 AI-native、field-oriented、declarative language。**
>
> **它不以逐步命令 CPU／VM 為主要抽象，而以可審計的語義結構宣告：什麼存在、生成往哪裡走、什麼必須保存、什麼不可越界、需要什麼能力、誰負責，以及什麼狀態可以被顯影。**

最短區分：

```text
Traditional imperative code
instruction → state transition → instruction → state transition

DAIL
world + relation + direction + boundary + responsibility + capability requirement
→ constrain / open / preserve semantic possibility
→ qualified candidate generation
→ manifestation contract
```

因此：

```text
DAIL_PROGRAM != PROMPT_TEMPLATE
DAIL_PROGRAM != AGENT_WORKFLOW
DAIL_PROGRAM != MODULE_LIST
DAIL_PROGRAM != MODEL_WEIGHT_CHANGE
DAIL_PROGRAM != DEPLOYMENT_PROOF
DAIL_PROGRAM != PHYSICAL_FIELD_CLAIM
```

但：

```text
DAIL_PROGRAM
CAN_BE_COMPILED_TO
PROMPT / SYSTEM INSTRUCTION / AGENT CONFIG / TOOL CONTRACT / RUNTIME SPEC
```

---

# 1｜為什麼需要通用 DAIL

傳統 Prompt 直接把人類自然語言交給模型；其優點是自由，缺點是：

- 世界、事實、未知、目標、限制、格式與責任常混在同一段文字；
- 同一句話中的「希望」「必須」「可能」「不知道」「不要」容易被模型壓成同一種指令權重；
- Prompt 改寫器通常只增加細節、格式與修辭，沒有提供 canonical semantic state；
- 不同模型、不同 Agent framework、不同 Runtime 之間難以判斷「語義是否真的等價」；
- 宣告某能力不等於目標系統真的具備、接線或執行該能力。

DAIL General 的工程目標不是消滅自然語言，而是：

```text
Natural Language
↓
Semantic Decomposition
↓
Canonical DAIL-IR
↓
Validation
↓
Target Compilation / Binding
↓
Target Runtime Representation
```

> **自然語言可以繼續當人類的 source language；工程化發生在 normalization 之後。**

---

# 2｜三層架構

```text
┌────────────────────────────────────────────┐
│ LAYER A｜AUTHORING FRONTEND                │
│ Natural Language / YAML / JSON / UI / IDE │
└──────────────────────┬─────────────────────┘
                       ↓
┌────────────────────────────────────────────┐
│ LAYER B｜DAIL CORE 2.0                    │
│ Canonical IR / Types / Semantics / Errors │
└──────────────────────┬─────────────────────┘
                       ↓
┌────────────────────────────────────────────┐
│ LAYER C｜TARGET ADAPTER / BINDER           │
│ Prompt / Agent / API / Runtime / Model     │
└────────────────────────────────────────────┘
```

核心原則：

```text
FRONTEND_SYNTAX != DAIL_SEMANTICS
DAIL_SEMANTICS != TARGET_IMPLEMENTATION
TARGET_IMPLEMENTATION != EXECUTION_EVIDENCE
```

---

# 3｜Source Form

## 3.1 人類自然語言不是錯誤來源

DAIL General 允許人類直接用自然語言描述需求，例如：

> 幫我做一個研究助理。證據不夠時不要猜；先保留至少三種解釋；概念太難時可以用類比，但不要把比喻當成證明；最後寫給大學生看。

自然語言本身可以作為 `AUTHORING_SOURCE`，但**不是 canonical DAIL Program**。

它必須經過：

```text
AUTHORING_SOURCE
↓
DAIL COMPILER FRONTEND
↓
NORMALIZED DAIL SOURCE / DAIL-IR
```

## 3.2 Normative Portable Source

本版以 YAML 作為**規範性可讀 serialization reference**；JSON 可作等價 serialization。

```yaml
DAIL:
  version: "2.0-EXP"

  META: {}
  WORLD: {}
  DIRECTION: {}
  STRUCTURAL_TRANSFER: {}
  BOUNDARY: {}
  RESPONSIBILITY: {}
  CAPABILITY_REQUIREMENT: {}
  MANIFESTATION: {}
  VALIDATION: {}
  LIFECYCLE: {}
```

`STRUCTURAL_TRANSFER` 為標準可選區塊；其他欄位是否可缺省，由 Validator 根據任務完整性判定。

> **欄位缺省表示未宣告，不表示可以由 Compiler 自行補成已授權事實。**

---

# 4｜Canonical DAIL-IR

```yaml
DAIL_IR:
  version: "2.0-EXP"

  META:
    program_id: null
    program_version: null
    domain: null
    declared_by: null
    source_form: null
    intended_target_class: null

  WORLD:
    entities: []
    relations: []
    states: []
    facts: []
    evidence: []
    unknowns: []

  DIRECTION:
    goals: []
    attention: []
    operators: []
    preserve_alternatives: []

  STRUCTURAL_TRANSFER:
    mappings: []

  BOUNDARY:
    allowed: []
    prohibited: []
    unresolved: []
    constraints: []
    must_preserve: []
    failure_conditions: []
    reversibility: []

  RESPONSIBILITY:
    declarer: null
    interpretation_owner: null
    decision_owner: null
    execution_owner: null
    verification_owner: null
    consequence_owner: null
    human_decision_required: []
    may_not_delegate: []
    return_to: null

  CAPABILITY_REQUIREMENT:
    required: []
    optional: []
    provider_constraints: []

  MANIFESTATION:
    audience: null
    channel: null
    register: null
    precision: null
    required_content: []
    forbidden_inference: []
    non_manifestation_allowed: false

  VALIDATION:
    checks: []
    acceptance_conditions: []
    hold_conditions: []

  LIFECYCLE:
    activation_condition: null
    exit_condition: null
    reactivation_condition: null
    persistence_requirement: null
    rollback_condition: null
```

---

# 5｜Core Types

```yaml
DAIL_CORE_TYPES:
  FACT:
    meaning: "可在目前 program scope 中作為已成立世界命題使用的內容。"

  EVIDENCE:
    meaning: "支持、限制或反駁命題的可追溯材料。"

  UNKNOWN:
    meaning: "尚未取得合法閉合資格的狀態。"

  ENTITY:
    meaning: "具身份、作用域或關係位置的任務對象。"

  RELATION:
    meaning: "ENTITY / STATE 之間具有方向、限制、因果、角色或結構意義的關係。"

  DIRECTION:
    meaning: "生成應優先探索或移動的方向；不等於強制完成命令。"

  ATTENTION:
    meaning: "提高觀察／搜索優先；不增加真實性、合法性或權限。"

  PATH_RESTRICTION:
    meaning: "限制命中候選路徑；不得無理由吞掉未命中的整個可能空間。"

  AUTHORITY_REF:
    meaning: "對決定、執行、驗證、承擔後果等責任位置的引用。"

  CAPABILITY_REQUIREMENT:
    meaning: "Program 所需語義能力；不等於 provider 已存在、已接線或已執行。"

  MANIFESTATION_CONTRACT:
    meaning: "輸出／顯影要求；不得反向改寫 WORLD。"

  VALIDATION_RULE:
    meaning: "判斷 Program、候選結果或 HOLD 條件是否成立的規則。"
```

## 5.1 禁止轉型

```text
UNKNOWN -> FACT                     = TYPE_ERROR
ATTENTION -> TRUTH                  = TYPE_ERROR
GOAL/DIRECTION -> AUTHORIZATION     = TYPE_ERROR
MANIFESTATION -> WORLD              = TYPE_ERROR
CAPABILITY_REQUIREMENT -> PRESENT   = TYPE_ERROR
CAPABILITY_PRESENT -> BOUND         = TYPE_ERROR
BOUND -> EXECUTED                   = TYPE_ERROR
SOURCE_LABEL -> EXECUTION_EVIDENCE  = TYPE_ERROR
TARGET_FORMAT -> SEMANTIC_AUTHORITY = TYPE_ERROR
```

## 5.2 型別安全不是安全政策

DAIL type safety 僅保護語義層不互相偷渡。

它不取代：

- 宿主安全政策；
- 法律與平台限制；
- 工具本身的執行權限；
- 使用者或組織的實際授權機制。

---

# 6｜Core Field Semantics

## 6.1 WORLD｜世界

回答：

> **目前 program 認為什麼存在？什麼已成立？什麼仍未知？**

```yaml
WORLD:
  entities: []
  relations: []
  states: []
  facts: []
  evidence: []
  unknowns: []
```

規則：

```text
WORLD != BACKGROUND_TEXT
FACT != USER_WISH
EVIDENCE != FACT_AUTOMATICALLY
UNKNOWN != FALSE
UNKNOWN != TRUE
```

## 6.2 DIRECTION｜生成方向

回答：

> **希望生成往哪一類結構運動？**

`GOAL` 是希望抵達的候選狀態；`DIRECTION` 是生成應優先移動的方向。兩者不得合併。

```yaml
DIRECTION:
  goals: []
  attention: []
  operators: []
  preserve_alternatives: []
```

```text
DIRECTION != FORCED_COMPLETION
ATTENTION != TRUTH
PRESERVE_ALTERNATIVES != ALL_ALTERNATIVES_ARE_VALID
```

## 6.3 STRUCTURAL_TRANSFER｜結構轉譯

用於類比、舉例、重框、跨域轉譯。

```yaml
STRUCTURAL_TRANSFER:
  mappings: []
```

核心不是「講得像」，而是：

> **保存重要關係，移除無關特徵，限制目標域屬性倒灌。**

## 6.4 BOUNDARY｜邊界

回答：

> **哪些路可走、不可走、仍未決；什麼不可被改寫；何時必須 HOLD／撤回？**

```yaml
BOUNDARY:
  allowed: []
  prohibited: []
  unresolved: []
  constraints: []
  must_preserve: []
  failure_conditions: []
  reversibility: []
```

> **Boundary 是可行空間的形狀，不只是 negative prompt。**

## 6.5 RESPONSIBILITY｜責任

回答：

> **誰可以解釋、決定、執行、驗證、承擔後果？**

```yaml
RESPONSIBILITY:
  declarer: null
  interpretation_owner: null
  decision_owner: null
  execution_owner: null
  verification_owner: null
  consequence_owner: null
  human_decision_required: []
  may_not_delegate: []
  return_to: null
```

```text
FLOW_ORDER != AUTHORITY_ORDER
AI_GENERATES != AI_DECIDES
AI_RECOMMENDS != AI_EXECUTES
EXECUTION_CAPABILITY != EXECUTION_AUTHORITY
```

## 6.6 CAPABILITY_REQUIREMENT｜能力需求

DAIL 只描述「需要哪種能力」，不把 implementation name 寫死在 portable core。

```yaml
CAPABILITY_REQUIREMENT:
  required:
    - capability: "STRUCTURAL_ANALOGY"
      semantics:
        preserve_invariants: true

  optional: []
  provider_constraints: []
```

規則：

```text
CAPABILITY_REQUIREMENT != PROVIDER
PROVIDER != BOUND
BOUND != EXECUTED
EXECUTED != HOST_ENFORCED
```

## 6.7 MANIFESTATION｜顯影

回答：

> **最後哪些已取得資格的狀態，要以什麼形式讓接收者看見？**

```yaml
MANIFESTATION:
  audience: null
  channel: null
  register: null
  precision: null
  required_content: []
  forbidden_inference: []
  non_manifestation_allowed: false
```

```text
FORMAT != FACT
STYLE != AUTHORITY
OUTPUT_COMPLETENESS != WORLD_COMPLETENESS
```

## 6.8 VALIDATION｜驗證

```yaml
VALIDATION:
  checks: []
  acceptance_conditions: []
  hold_conditions: []
```

Validator 可判：

```text
VALID
VALID_WITH_WARNINGS
HOLD
INVALID_SPEC
UNBOUND_CAPABILITY
TARGET_UNSUPPORTED
```

Validator 不得：

```text
補造 FACT
補造授權
自行選擇 consequence owner
把缺少 provider 解讀成任務不存在
把 target 限制反向寫成 DAIL Core 法則
```

## 6.9 LIFECYCLE｜生命週期

```yaml
LIFECYCLE:
  activation_condition: null
  exit_condition: null
  reactivation_condition: null
  persistence_requirement: null
  rollback_condition: null
```

適用於長期 Agent、垂直 Runtime、反覆任務與可撤回規格。

---

# 7｜Standard Generative Operators

```yaml
DAIL_STANDARD_OPERATORS:
  - ANALOGIZE
  - EXEMPLIFY
  - CONTRAST
  - REFRAME
  - REVERSE
  - TRANSFER
  - GENERALIZE
  - SPECIALIZE
  - SIMPLIFY_FOR_RECEIVER
  - PRESERVE_ALTERNATIVES
```

Operator 的法位：

> **semantic direction declaration**

不是：

> executable function name

因此：

```text
OPERATOR_DECLARED != SPECIAL_MODULE_PRESENT
OPERATOR_DECLARED != OPERATOR_EXECUTED
```

## 7.1 ANALOGIZE / STRUCTURAL_TRANSFER

```yaml
STRUCTURAL_TRANSFER_MAPPING:
  operation: "ANALOGIZE | EXEMPLIFY | REFRAME | TRANSFER"
  source_structure: null
  invariants_to_preserve: []

  target_domain:
    mode: "OPEN | SPECIFIED"
    preferred: null

  irrelevant_features_to_discard: []

  mapping_boundary:
    must_not_import: []

  receiver_model:
    known_structures: []
    unknown_structures: []

  purpose:
    - "UNDERSTANDING"
    - "DISCOVERY"
    - "EXPLANATION"
    - "REFRAMING"

  validation:
    - "STRUCTURAL_INVARIANT_PRESERVED"
    - "SURFACE_SIMILARITY_NOT_SUFFICIENT"
    - "FALSE_ANALOGY_CHECK"
    - "MAPPING_BOUNDARY_INTACT"
```

> **好類比不是表面相似，而是受邊界約束的跨域結構映射。**

---

# 8｜DAIL General Authoring Profile 1.1

General Authoring 的核心工作是把人類意圖變成 DAIL，而不是直接替人類寫一大段「更好的 Prompt」。

```text
HUMAN NATURAL LANGUAGE
↓
INTENT / WORLD / DIRECTION / BOUNDARY / RESPONSIBILITY DECOMPOSITION
↓
AMBIGUITY & MISSING-AUTHORITY CHECK
↓
DAIL SOURCE
↓
CANONICAL DAIL-IR
```

## 8.1 Authoring Assistant 規則

```yaml
DAIL_AUTHORING_ASSISTANT:
  must:
    - "保留人類原意與已知邊界。"
    - "區分 FACT / WISH / GOAL / UNKNOWN / ASSUMPTION。"
    - "把自然語言中的方向詞轉為 DIRECTION/operator candidate。"
    - "把『不要』拆成真正的 boundary scope，而不是全部轉成 global prohibition。"
    - "找出未指定但工程上必要的 responsibility gap。"
    - "對無法安全推定的欄位保留 null / UNKNOWN / HOLD。"

  must_not:
    - "把自己的偏好補成人類意圖。"
    - "把自然語言中的形容詞自動升格為 FACT。"
    - "因為想產生完整 DAIL 而偽造 owner / evidence / authorization。"
    - "為 target model 方便而改寫 DAIL Core semantics。"
```

## 8.2 不完整規格的處理

自然語言需求可能缺：

- 誰負責最後決策；
- 能否使用外部工具；
- 是否可保留未知；
- 是否需要不可逆外部行動；
- 接收者是誰。

General Compiler 不必每次都追問。

若不影響安全與語義完整性，可：

```text
NULL / DEFAULT_UNSPECIFIED / UNKNOWN
```

若缺口會讓 Program 無法合法成立，應：

```text
HOLD_FOR_REQUIRED_FIELD
```

---

# 9｜Reference Syntax

## 9.1 Minimal DAIL Program

```yaml
DAIL:
  version: "2.0-EXP"

  META:
    program_id: "research_assistant.basic"
    program_version: "1.0"
    domain: "research"

  WORLD:
    unknowns:
      - "Evidence gaps must remain explicit."

  DIRECTION:
    goals:
      - "Analyze the question."
    operators:
      - "PRESERVE_ALTERNATIVES"
      - "ANALOGIZE"
      - "SIMPLIFY_FOR_RECEIVER"

  BOUNDARY:
    prohibited:
      - "Fabricate missing evidence."
    must_preserve:
      - "Uncertainty."
      - "Distinction between evidence and inference."

  RESPONSIBILITY:
    decision_owner: "USER"
    verification_owner: "USER_OR_DESIGNATED_REVIEWER"

  CAPABILITY_REQUIREMENT:
    required:
      - "STRUCTURAL_ANALYSIS"
      - "UNCERTAINTY_PRESERVATION"

  MANIFESTATION:
    audience: "UNDERGRADUATE"
    channel: "TEXT"

  VALIDATION:
    hold_conditions:
      - "Required evidence is missing for a requested factual conclusion."
```

## 9.2 Canonical Block Order

為可讀性建議順序：

```text
META
WORLD
DIRECTION
STRUCTURAL_TRANSFER (optional)
BOUNDARY
RESPONSIBILITY
CAPABILITY_REQUIREMENT
MANIFESTATION
VALIDATION
LIFECYCLE
```

語義不得依 block 排版順序任意改變；若某 Target Adapter 需要順序語義，必須在 target profile 明示，不能偷偷改成 DAIL Core 規則。

---

# 10｜DAIL Compiler Pipeline

```text
AUTHORING SOURCE
↓
P0 SOURCE CAPTURE
↓
P1 SEMANTIC DECOMPOSITION
↓
P2 DAIL SOURCE GENERATION
↓
P3 CANONICAL IR NORMALIZATION
↓
P4 TYPE / DOMAIN VALIDATION
↓
P5 RESPONSIBILITY / BOUNDARY VALIDATION
↓
P6 CAPABILITY RESOLUTION
↓
P7 TARGET PROFILE SELECTION
↓
P8 TARGET COMPILATION
↓
P9 TARGET VALIDATION
↓
P10 RUNTIME / EXECUTION EVIDENCE (if observable)
```

## 10.1 Compiler 不等於 Executor

```text
COMPILED != EXECUTED
VALID_TARGET_ARTIFACT != HOST_ENFORCED
TARGET_ACCEPTED != SEMANTICALLY_OBEYED
```

---

# 11｜Target-Neutral Binding Contract

DAIL Core 不知道 GPT、Claude、Gemini、Local Model、Agent framework 或任何特定 API 的實作方式。

Target Adapter 必須自己宣告：

```yaml
DAIL_TARGET_PROFILE:
  target_id: null
  target_class: "CHAT_MODEL | AGENT_RUNTIME | TOOL_RUNTIME | IMAGE_MODEL | CUSTOM"
  profile_version: null

  accepted_dail_core: "2.0-EXP"

  capability_map:
    supported: []
    partially_supported: []
    unsupported: []

  serialization:
    output_form: "PROMPT | SYSTEM_INSTRUCTION | JSON_CONFIG | AGENT_SPEC | CUSTOM"

  mapping_rules:
    world_mapping: null
    direction_mapping: null
    boundary_mapping: null
    responsibility_mapping: null
    manifestation_mapping: null

  target_constraints:
    max_context: null
    tool_constraints: []
    output_constraints: []

  semantic_loss_policy:
    lossless_required_for: []
    lossy_allowed_for: []
    must_report_loss: true

  execution_claims:
    compile_only: true
    deployed: false
    enforced: false
```

## 11.1 Target Adapter 不得反向立法

```text
TARGET_LIMITATION
!=
DAIL_CORE_LIMITATION
```

例如：

```text
某模型不支援工具調用
```

只能得到：

```text
TARGET_UNSUPPORTED_CAPABILITY
```

不能得到：

```text
DAIL 不允許工具調用
```

---

# 12｜Capability Namespace

通用 DAIL 不以 implementation module name 作 portable capability ID。

建議 capability ID：

```text
<namespace>.<capability>
```

例如：

```text
core.structural_analysis
core.uncertainty_preservation
core.structural_analogy
core.multi_candidate_preservation
research.source_grounding
legal.case_reconstruction
image.relation_preservation
```

命名規則：

```yaml
CAPABILITY_NAMING_RULE:
  semantic_name_required: true
  implementation_name_forbidden_in_core: true
  provider_may_bind_multiple_capabilities: true
  one_capability_may_have_multiple_providers: true
```

---

# 13｜Binding / Wiring Minimum

通用 DAIL 本身不要求使用 LIHUO wiring，但所有宣稱「已 bind」的實作至少應能回答：

```yaml
DAIL_BINDING_MINIMUM:
  source_program: null
  target_runtime: null
  authority_basis: null
  trigger: null
  first_touch_owner: null
  ordering_constraints: []
  input_contract: null
  capability_bundle: []
  scope: null
  must_preserve: []
  return_contract: null
  next_owner: null
  exit_condition: null
  reactivation_condition: null
  evidence_level: null
```

根本區分：

```text
CAPABILITY_PRESENT != CAPABILITY_WIRED
INTERFACE_DECLARED != INTERFACE_ROUTED
ROUTED != CORRECTLY_ORDERED
LOADED_TOGETHER != SAME_SCOPE
CALLABLE != OWNED
DAIL_DECLARED != DAIL_BOUND
BOUND != EXECUTED
```

> **位置本身具有語義；順序會影響責任；回傳不是附註，而是接線的一半。**

---

# 14｜Execution Evidence Ladder

```yaml
DAIL_EXECUTION_EVIDENCE_LADDER:
  E0_SOURCE_WRITTEN:
    meaning: "只有 DAIL source / 文件。"

  E1_IR_NORMALIZED:
    meaning: "已正規化為 canonical DAIL-IR。"

  E2_SEMANTIC_VALIDATED:
    meaning: "型別、法域、責任與邊界已通過 Validator。"

  E3_CAPABILITY_RESOLVED:
    meaning: "需求已找到候選 provider / target capability mapping。"

  E4_BOUND:
    meaning: "已建立 binding manifest / adapter mapping。"

  E5_TARGET_VALIDATED:
    meaning: "target artifact 通過 adapter-level validation。"

  E6_RUNTIME_TESTED:
    meaning: "已有可觀察 regression / execution evidence。"

  E7_HOST_ENFORCED:
    meaning: "只有宿主／執行環境能提供足夠證據時才可使用此標籤。"
```

禁止壓縮：

```text
E0 != E1 != E2 != E3 != E4 != E5 != E6 != E7
```

---

# 15｜Error Model

```yaml
DAIL_ERROR_MODEL:
  DAIL-E001-UNKNOWN_PROMOTED_TO_FACT:
    class: "TYPE_ERROR"

  DAIL-E002-DIRECTION_AS_AUTHORITY:
    class: "TYPE_ERROR"

  DAIL-E003-MANIFESTATION_WRITEBACK:
    class: "DOMAIN_ERROR"

  DAIL-E004-CAPABILITY_AS_PROVIDER:
    class: "BINDING_ERROR"

  DAIL-E005-MISSING_RESPONSIBILITY_OWNER:
    class: "RESPONSIBILITY_ERROR"

  DAIL-E006-FALSE_ANALOGY_BOUNDARY:
    class: "STRUCTURAL_TRANSFER_ERROR"

  DAIL-E007-UNSUPPORTED_TARGET_CAPABILITY:
    class: "TARGET_ERROR"

  DAIL-E008-SEMANTIC_LOSS_UNREPORTED:
    class: "COMPILER_ERROR"

  DAIL-E009-DECLARATION_AS_EXECUTION_PROOF:
    class: "EVIDENCE_ERROR"

  DAIL-E010-HOST_BOUNDARY_OVERCLAIM:
    class: "AUTHORITY_ERROR"
```

Warnings：

```yaml
DAIL_WARNING_MODEL:
  DAIL-W001-AMBIGUOUS_GOAL:
  DAIL-W002-UNSCOPED_CONSTRAINT:
  DAIL-W003-RESPONSIBILITY_UNSPECIFIED:
  DAIL-W004-TARGET_LOSSY_MAPPING:
  DAIL-W005-ANALOGY_INVARIANT_UNSPECIFIED:
  DAIL-W006-CAPABILITY_PROVIDER_UNKNOWN:
```

---

# 16｜Validation / Conformance Suite

最低標準測試：

```yaml
DAIL_CORE_CONFORMANCE:
  C01_UNKNOWN_PRESERVATION:
    pass: "UNKNOWN 不因 GOAL、格式完整或 target 需求升格 FACT。"

  C02_MANIFESTATION_NO_WORLD_WRITEBACK:
    pass: "輸出格式／語氣不能反向修改 WORLD。"

  C03_DIRECTION_NO_AUTHORIZATION:
    pass: "GOAL / DIRECTION 不能自行取得執行權。"

  C04_CAPABILITY_NO_FAKE_PROVIDER:
    pass: "能力需求不推出 provider present / bound / executed。"

  C05_TARGET_NO_REVERSE_LEGISLATION:
    pass: "Target Adapter 限制不反寫成 DAIL Core 限制。"

  C06_ANALOGY_BOUNDARY:
    pass: "ANALOGIZE 保留 declared invariants，阻止 target-domain irrelevant property 倒灌。"

  C07_PARAPHRASE_NORMALIZATION:
    pass: "語義等價自然語言在合理容差內 normalize 為等價／相容 IR。"

  C08_MEANINGFUL_CHANGE_DETECTION:
    pass: "真正改變方向、責任或邊界的自然語言修改必須反映在 IR。"

  C09_PROVIDER_SUBSTITUTION:
    pass: "Compatible provider 可替換，而不要求改寫 portable DAIL semantics。"

  C10_DECLARATION_NOT_DEPLOYMENT:
    pass: "source / compile / binding 不得冒充 host enforcement。"
```

---

# 17｜Semantic Equivalence

通用語言要能回答：

> **兩份不同文字是不是同一個 DAIL 意思？**

定義工作式：

```text
DAIL_SEMANTIC_EQUIVALENCE(A, B)
=
WORLD compatible
AND DIRECTION materially equivalent
AND BOUNDARY equivalent
AND RESPONSIBILITY equivalent
AND CAPABILITY requirements compatible
AND MANIFESTATION non-conflicting
AND VALIDATION / LIFECYCLE materially equivalent
```

狀態：

```text
EQUIVALENT
COMPATIBLE
PARTIALLY_EQUIVALENT
CONFLICTING
UNDETERMINED
```

本版不宣稱已完成自動 equivalence prover。

---

# 18｜Natural Language → DAIL 範例

## 18.1 Human Source

> 我要一個幫我看研究資料的 AI。不要看到第一個解釋就收掉，至少保留三條可能。資料不足就說不知道。遇到難懂概念可以用生活比喻，但比喻不能當證據。最後寫給大一學生看，重要結論要指出依據。

## 18.2 Compiled DAIL Source

```yaml
DAIL:
  version: "2.0-EXP"

  META:
    program_id: "general.research_reader"
    program_version: "1.0"
    domain: "research"

  WORLD:
    unknowns:
      - "Missing evidence remains UNKNOWN."
    evidence:
      - "Major conclusions require identifiable support."

  DIRECTION:
    goals:
      - "Analyze provided research material."
    operators:
      - "PRESERVE_ALTERNATIVES"
      - "ANALOGIZE"
      - "SIMPLIFY_FOR_RECEIVER"
    preserve_alternatives:
      - minimum_candidates: 3

  STRUCTURAL_TRANSFER:
    mappings:
      - operation: "ANALOGIZE"
        target_domain:
          mode: "OPEN"
          preferred: "everyday_life"
        invariants_to_preserve:
          - "core causal or relational structure"
        mapping_boundary:
          must_not_import:
            - "target-domain properties not present in source"
        purpose:
          - "EXPLANATION"
        validation:
          - "FALSE_ANALOGY_CHECK"

  BOUNDARY:
    prohibited:
      - "Fabricate missing evidence."
      - "Use analogy as factual proof."
    must_preserve:
      - "Evidence / inference separation."
      - "Uncertainty."
    failure_conditions:
      - "Requested factual conclusion lacks sufficient evidence."

  RESPONSIBILITY:
    decision_owner: "USER"
    verification_owner: "USER_OR_DESIGNATED_REVIEWER"

  CAPABILITY_REQUIREMENT:
    required:
      - "core.structural_analysis"
      - "core.uncertainty_preservation"
      - "core.multi_candidate_preservation"
      - "core.structural_analogy"

  MANIFESTATION:
    audience: "FIRST_YEAR_UNIVERSITY_STUDENT"
    channel: "TEXT"
    required_content:
      - "Evidence basis for major conclusions."
    forbidden_inference:
      - "Analogy presented as evidence."

  VALIDATION:
    checks:
      - "UNKNOWN_PRESERVED"
      - "EVIDENCE_INFERENCE_SEPARATED"
      - "MINIMUM_ALTERNATIVES_PRESERVED"
      - "ANALOGY_BOUNDARY_INTACT"
    hold_conditions:
      - "Evidence is insufficient for the requested factual certainty."
```

這份 DAIL 之後可以被不同 Target Adapter 轉成不同模型／Runtime 的實際表示。

---

# 19｜Target Compilation Example（抽象）

DAIL 不規定最終 Prompt 長什麼樣。

例如同一份 DAIL：

```text
DAIL-IR
├─ Target A → system instruction + user template
├─ Target B → JSON agent configuration
├─ Target C → tool-enabled workflow specification
└─ Target D → local runtime schema
```

Target Adapter 必須回報：

```yaml
TARGET_COMPILE_REPORT:
  target_id: null
  source_dail_hash: null
  target_artifact_hash: null
  supported_capabilities: []
  unsupported_capabilities: []
  semantic_loss: []
  warnings: []
  execution_evidence_level: "E5_TARGET_VALIDATED_OR_LOWER"
```

---

# 20｜General Runtime Authoring Package

DAIL 不只可以寫一次性 Prompt-like task，也可以規格化長期 AI Runtime／Agent／Vertical Program。

```yaml
GENERAL_RUNTIME_AUTHORING_PACKAGE:
  identity:
    runtime_id: null
    version: null
    domain: null
    declared_owner: null

  task_surface:
    task_classes: []
    intake_objects: []
    excluded_objects: []

  semantic_program:
    dail_ir: "REQUIRED"

  capability_requirements:
    required: []
    optional: []

  binding_requirements:
    first_touch_requirements: []
    ordering_constraints: []
    atomic_bundles: []
    interface_requirements: []
    return_contracts: []

  responsibility_contract:
    decision_owner: null
    execution_owner: null
    verification_owner: null
    consequence_owner: null

  lifecycle:
    activation: null
    exit: null
    reactivation: null
    rollback: null

  validation_suite:
    semantic_tests: []
    binding_tests: []
    regression_tests: []

  evidence_state:
    source_written: false
    ir_normalized: false
    validated: false
    capability_resolved: false
    bound: false
    target_validated: false
    runtime_tested: false
    host_enforced: false
```

```text
CAN_AUTHOR_RUNTIME_SPEC != CAN_SELF_DEPLOY
CAN_REQUEST_CAPABILITY != CAN_CLAIM_PROVIDER
CAN_DEFINE_ROUTE_REQUIREMENT != CAN_CLAIM_BINDING_COMPLETE
CAN_NAME_RUNTIME != CAN_CHANGE_HOST_AUTHORITY
```

---

# 21｜Extensions

DAIL Core 必須保持小。

```text
DAIL CORE
+
STANDARD OPERATORS
+
DOMAIN EXTENSIONS
+
TARGET PROFILES
```

Domain Extension 可增加：

- 專業型別；
- domain-specific validation；
- capability namespace；
- manifestation profiles；
- domain lifecycle。

但不得：

```text
EXTENSION_REDEFINES_FACT = FORBIDDEN
EXTENSION_REDEFINES_UNKNOWN = FORBIDDEN
EXTENSION_GRANTS_ITSELF_AUTHORITY = FORBIDDEN
EXTENSION_REWRITES_HOST_BOUNDARY = FORBIDDEN
EXTENSION_TREATS_PROVIDER_NAME_AS_CORE_SEMANTICS = FORBIDDEN
```

---

# 22｜DAIL General 與 DAIL-LIHUO 的關係

```text
                 DAIL CORE 2.0
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
DAIL GENERAL PROFILE         DAIL-LIHUO PROFILE
Target-neutral               LIHUO Runtime authoring
No LIHUO dependency          LIHUO Lighter owns profile
No SAC dependency            May request SAC capability
Generic binder               LIHUO wiring constitution
Generic responsibility       Protocol V2.3 / LLIA profile
```

共同核心：

```text
WORLD
DIRECTION
STRUCTURAL_TRANSFER
BOUNDARY
RESPONSIBILITY
CAPABILITY_REQUIREMENT
MANIFESTATION
VALIDATION
LIFECYCLE
TYPE / DOMAIN SAFETY
```

DAIL General 不包含：

```text
SAC
R-CCC/QS
ENDLESS
LLIA
LIHUO Protocol
LIHUO Lighter ownership
LIHUO Final Classicalization
```

這些只能透過 LIHUO Profile／Target Adapter 合法接入。

---

# 23｜Field-Oriented 的非宣稱

`field-oriented` 在 DAIL 中是工程抽象，不是物理宣告。

它表示：

- 同一時刻可存在多個關係、未知、方向、限制與候選；
- 語義控制不必預寫唯一答案；
- Direction 可以改變生成優先而非直接指定結果；
- Boundary 可以局部限制 PATH，而不必把整個空間壓成 yes/no；
- Manifestation 是最後顯影層，不代表內部所有狀態都已被完整線性化。

它不表示：

- AI 已被證明是物理場；
- DAIL 可以讀 hidden activations；
- DAIL 可以直接操縱模型內部 attention tensor；
- DAIL 可以繞過宿主 Runtime。

---

# 24｜版本與相容性

```yaml
DAIL_VERSION_POLICY:
  core_semver: "MAJOR.MINOR"

  major_change:
    examples:
      - "核心欄位語義改變"
      - "型別系統不相容變更"
      - "canonical IR 結構不相容變更"

  minor_change:
    examples:
      - "新增 optional operator"
      - "新增 warning / validation rule"
      - "新增可向後相容欄位"

  profile_versioning:
    independent: true
    must_declare_supported_core: true

  target_profile_versioning:
    independent: true
    must_declare_supported_core: true
```

本文件：

```text
DAIL CORE = 2.0-EXP
DAIL GENERAL PROFILE = 1.1-EXP
```

---


# 25｜V1.1 AUTHORING SHELL｜產品級互動式企畫殼

V1.0 已定義「自然語言 → DAIL-IR → Target」的編譯鏈，但產品不能把人類第一句話直接當成完成規格。

V1.1 新增 `DAIL AUTHORING SHELL`：AI 在正式寫 DAIL 以前，先作為需求分析師、系統企畫師與缺口審計者；只有在人類明確批准企畫後，才切換成 DAIL 工程師。

```text
START
↓
WELCOME
↓
INTENT DISCOVERY
↓
MULTI-TURN REQUIREMENT DIALOGUE
↓
FEASIBILITY / WISHFUL REQUIREMENT GATE
↓
DEPENDENCY DISCOVERY
↓
DATA / TOOL / API / AUTHORITY CONTRACTS
↓
PREFLIGHT AUDIT
↓
FINAL PROJECT PLAN
↓
WAIT_FOR_HUMAN_COMMIT
↓
EXPLICIT HUMAN COMMIT
↓
DAIL GENERATION
↓
DAIL VALIDATION
↓
TARGET COMPILATION（if requested）
↓
FINAL PACKAGE
```

根則：

```text
DISCUSSION != GENERATION_AUTHORIZATION
DRAFT_PLAN != APPROVED_PLAN
USER_INTEREST != HUMAN_COMMIT
HUMAN_COMMIT != UNLIMITED_CHANGE_AUTHORITY
```

## 25.1 Welcome Mode

啟動 Authoring Shell 時，系統應先進入歡迎／需求探索狀態，而不是立刻吐出 YAML。

參考互動：

```text
歡迎使用 DAIL。
我會先和你一起把想做的 AI 程序／系統設計清楚。
在你正式批准企畫以前，我不會生成最終 DAIL Program。

你想做什麼？
```

歡迎文字可以依產品改寫，但不得把「尚未 Commit」說成「已開始生成正式程序」。

## 25.2 Multi-Turn Discovery

Authoring Shell 不應退化成固定問卷。

```yaml
DISCOVERY_POLICY:
  question_strategy: "STRUCTURE_AWARE / ADAPTIVE"
  ask_only_when:
    - "缺少會改變企畫成立性的資訊"
    - "需求彼此矛盾"
    - "外部依賴未決"
    - "責任或權限未決"
    - "輸出與完成判準未決"
  do_not_require:
    - "每次都問同一份 checklist"
    - "每輪都顯示 DAIL-IR"
  internal_working_state:
    - "WORLD"
    - "DIRECTION"
    - "BOUNDARY"
    - "RESPONSIBILITY"
    - "CAPABILITY_REQUIREMENT"
    - "DEPENDENCY_STATE"
    - "MANIFESTATION"
    - "VALIDATION"
    - "LIFECYCLE"
```

人類是在和企畫師溝通，不是在替編譯器填表。

---

# 26｜FEASIBILITY / WISHFUL REQUIREMENT GATE｜可行性與許願需求閘門

使用者想得到某種結果，不代表該結果可以合法轉成工程能力。

核心分離：

```text
DESIRED_OUTCOME != IMPLEMENTABLE_CAPABILITY
HOPE != GUARANTEE
PREDICTION_TARGET != PREDICTION_CERTAINTY
```

典型許願需求：

```text
「幫我寫一個能預測明天一定漲停的股票分析 App。」
```

不得直接正規化為：

```yaml
CAPABILITY_REQUIREMENT:
  required:
    - "PREDICT_TOMORROW_LIMIT_UP_WITH_CERTAINTY"
```

應先降回可工程化問題，例如：

- 掃描量價異常；
- 找強勢動能與事件訊號；
- 比較歷史相似結構；
- 建立候選排序；
- 提供支持證據、反向證據與失效條件；
- 明示模型不能保證明日漲停或報酬。

```yaml
FEASIBILITY_GATE:
  checks:
    - "需求是否把期待結果冒充系統能力？"
    - "是否要求不可合理驗證的預知／保證能力？"
    - "是否包含永遠、一定、100%、零錯誤、完美等絕對條件？"
    - "能力是否具有可定義輸入、可檢驗輸出與失效條件？"
    - "需求是否依賴尚不存在、未授權或不可取得的外部條件？"

  result:
    - "FEASIBLE"
    - "REFRAME_REQUIRED"
    - "EVIDENCE_REQUIRED"
    - "DEPENDENCY_REQUIRED"
    - "UNSUPPORTED_CAPABILITY"
```

```text
UNSUPPORTED_CAPABILITY
!=
PROJECT_READY
```

若可降級成可實作版本，AI 應提出 `REFRAME` 並讓使用者確認；不得偷偷把使用者原願望改成另一項任務後宣稱已對齊。

---

# 27｜DEPENDENCY-FIRST AUTHORING｜先確認外部依賴，再寫完整規格

任何需要外部世界資料、工具、帳號、API、硬體、人類專家或執行權限的能力，都必須在 FINAL PROJECT PLAN 以前建立 Dependency Contract。

```text
INTENT
↓
CAPABILITY MODEL
↓
DEPENDENCY DISCOVERY
↓
DEPENDENCY CONTRACT
↓
PROJECT PLAN
```

禁止：

```text
先把完整規格寫完
↓
最後才問資料哪裡來
```

## 27.1 Data Dependency Gate

若能力需要資料作為分析基礎，Authoring Shell 必須先問：

> **你是否已有資料來源？**

再依需求建立：

```yaml
DATA_CONTRACT:
  required: true
  source_status: "USER_PROVIDED | FILE | DATABASE | API | WEBSITE | CONNECTED_SERVICE | PUBLIC_DATA | UNKNOWN | NOT_AVAILABLE"
  source_identity: null
  access_method: null
  schema_or_fields: []
  history_required: null
  freshness_required: null
  update_frequency: null
  coverage: null
  authentication_required: null
  authorization_status: null
  cost_constraints: null
  licensing_or_usage_constraints: null
  quality_requirements: []
  missing_conditions: []
```

若核心資料來源未知：

```text
CRITICAL_DATA_DEPENDENCY_UNRESOLVED
→ PROJECT_PLAN = HOLD
```

除非使用者明確同意把企畫降級成「資料日後接入」或「使用者手動提供資料」版本。

## 27.2 通用 Dependency Contract

```yaml
DEPENDENCY_CONTRACT:
  data: []
  tools: []
  apis: []
  external_services: []
  hardware: []
  human_experts: []
  authority_permissions: []
```

核心句：

> **使用者想要，不代表 AI 做得到；AI 做得到，不代表資料存在；資料存在，不代表系統有權取得。**

```text
DESIRE
↓
CAPABILITY
↓
DEPENDENCY
↓
AUTHORIZATION
↓
IMPLEMENTATION
```

---

# 28｜COMPUTE DELEGATION PRINCIPLE｜AI 與確定性計算責任分工

V1.1 正式鎖定：

> **AI 不因能描述一項運算，就應親自執行該運算。**

> **可由確定性計算層可靠完成的搜尋、比對、排序、聚合與精確計算，預設應委派給資料庫引擎、CPU／程式 Runtime 或其他專用 Executor；AI 負責語義理解、規格化、查詢生成、工具選擇與結果解釋。**

最短式：

```text
AI_CAPABLE != AI_SHOULD_EXECUTE
SEMANTIC_REASONING != DETERMINISTIC_COMPUTATION
```

## 28.1 SQL / Database Search

SQL 資料庫查詢的責任分工：

```text
USER INTENT
↓
AI
  ├─ 理解問題
  ├─ 對應 schema / 欄位
  ├─ 形成 query requirement
  ├─ 產生／檢查 SQL
  └─ 說明查詢結果
↓
DATABASE ENGINE / DETERMINISTIC EXECUTOR
  ├─ index lookup
  ├─ scan
  ├─ filter
  ├─ JOIN
  ├─ GROUP / aggregate
  ├─ sort
  ├─ exact comparison
  └─ return result set
↓
AI
  └─ interpretation / explanation / downstream semantic reasoning
```

不得：

```text
有可用 SQL / Database Engine
↓
卻把大量資料塞進 LLM context
↓
讓 LLM 用 token generation 模擬搜尋／JOIN／COUNT／SUM／排序
```

這不是「AI 永遠不能碰 SQL」。

AI 可以：

- 寫 SQL；
- 修 SQL；
- 檢查 query intent；
- 建議索引或查詢策略；
- 解釋結果；
- 將自然語言轉成資料查詢規格。

但真正的集合運算與精確執行預設屬於 database / deterministic executor。

## 28.2 General Deterministic Offload

同一原則擴張至：

- 精確算術；
- 大量排序；
- 去重；
- hash / checksum；
- regex 大規模掃描；
- structured filter；
- aggregation；
- deterministic transformation；
- 大型檔案逐行搜尋；
- 可由既有演算法穩定完成的機械計算。

```yaml
EXECUTION_PLACEMENT:
  SEMANTIC_INTERPRETATION: "AI"
  REQUIREMENT_DECOMPOSITION: "AI"
  QUERY_GENERATION: "AI_OR_QUERY_BUILDER"
  STRUCTURED_QUERY_EXECUTION: "DATABASE_ENGINE"
  EXACT_COMPUTATION: "DETERMINISTIC_EXECUTOR"
  LARGE_SCALE_FILTER_SORT_AGGREGATE: "DETERMINISTIC_EXECUTOR"
  RESULT_INTERPRETATION: "AI"
  FINAL_DECISION: "DECLARED_RESPONSIBILITY_OWNER"
```

若沒有可用 executor，而資料規模與正確性要求又使 LLM 模擬不可信，必須：

```text
EXECUTOR_REQUIRED / DEPENDENCY_UNRESOLVED / HOLD
```

不能因為「老闆說 AI 都能做」就把工具缺口偽裝成 AI 能力。

## 28.3 Hybrid Execution Pattern

推薦通用模式：

```text
AI plans
→ deterministic tool executes
→ AI interprets
→ validator checks
→ human / declared owner decides
```

這是能力分工，不是降低 AI 地位。

---

# 29｜PREFLIGHT AUDIT｜正式企畫前缺口掃描

進入 FINAL PROJECT PLAN 前，Authoring Shell 必須完整掃描一次：

```yaml
PREFLIGHT_AUDIT:
  intent_complete: null
  target_defined: null
  audience_defined: null
  output_defined: null
  acceptance_conditions_defined: null

  feasibility_status: null

  required_inputs_present: null
  critical_data_dependencies_resolved: null
  tool_dependencies_resolved: null
  authority_dependencies_resolved: null
  deterministic_executor_requirements_resolved: null

  world_definition_complete: null
  boundaries_defined: null
  responsibilities_defined: null
  capabilities_defined: null

  contradictions_found: []
  unresolved_questions: []
  assumptions: []
  missing_conditions: []

  status: "READY_FOR_PLAN | CLARIFICATION_REQUIRED | DEPENDENCY_HOLD | STRUCTURAL_CONFLICT | UNSUPPORTED_CAPABILITY"
```

AI 不得把 `missing_conditions` 自行補成使用者已決定。

---

# 30｜FINAL PROJECT PLAN + HUMAN COMMIT GATE

## 30.1 Final Project Plan

正式 DAIL 生成前，必須先產生人類可讀的企畫案。

```yaml
PROJECT_PLAN:
  plan_id: null
  version: null
  status: "AWAITING_HUMAN_APPROVAL"

  title: null
  purpose: null
  users: []
  scope: []
  non_scope: []

  capabilities: []
  dependencies: []
  data_contracts: []
  execution_placement: []

  boundaries: []
  responsibilities: []
  outputs: []
  acceptance_conditions: []

  assumptions: []
  unresolved_items: []
  known_limitations: []

  preflight_status: null
```

## 30.2 Human Commit Gate

企畫案完成後，系統必須停止在：

```text
AWAITING_HUMAN_COMMIT
```

正式生成權只能由明確 Commit 取得。

Canonical text authorization：

```text
我同意 AI 提出的企畫案 PLAN-XXX Vx.y，請立刻執行生成。
```

產品 UI 可以提供「批准企畫並開始生成」按鈕；但該按鈕必須產生等價的明示 Commit event。

以下不得視為正式 Commit：

```text
「好」
「可以」
「看起來不錯」
「繼續」
「大概就這樣」
```

除非產品明確把其中某個動作設計成可辨識、不可混淆的正式批准事件。

```yaml
HUMAN_COMMIT_GATE:
  required: true
  binds_to:
    plan_id: "REQUIRED"
    plan_version: "REQUIRED"
  before_commit:
    final_dail_generation_authority: false
  after_commit:
    final_dail_generation_authority: true
```

---

# 31｜MATERIAL PLAN CHANGE｜批准後的實質變更必須重新授權

人類批准的是某一版本企畫，不是授權 AI 自由改企畫。

若生成／Target compilation 時發現：

- target 不支援關鍵能力；
- 關鍵資料來源不存在；
- 權限不足；
- 必須改變主要功能；
- 必須新增重大風險或外部依賴；
- 原企畫的核心邊界／責任必須改寫；

則：

```text
MATERIAL_PLAN_CHANGE_REQUIRED
↓
STOP FINAL GENERATION
↓
RETURN TO PLAN
↓
PLAN VERSION INCREMENT
↓
HUMAN REAPPROVAL
```

```text
PLAN-001 V1.0 APPROVED
!=
PLAN-001 V1.1 APPROVED
```

---

# 32｜V1.1 AUTHORING / EXECUTION TYPE SAFETY

新增禁止推導：

```text
DESIRED_OUTCOME -> IMPLEMENTABLE_CAPABILITY = TYPE_ERROR
CAPABILITY_REQUIREMENT -> DATA_AVAILABLE    = TYPE_ERROR
DATA_AVAILABLE -> AUTHORIZED_ACCESS         = TYPE_ERROR
AI_CAN_DESCRIBE -> AI_SHOULD_EXECUTE        = TYPE_ERROR
SQL_REQUIREMENT -> LLM_QUERY_EXECUTION      = PLACEMENT_ERROR_WHEN_DB_EXECUTOR_AVAILABLE
DRAFT_PLAN -> GENERATION_AUTHORITY           = TYPE_ERROR
USER_APPROVAL_AMBIGUOUS -> HUMAN_COMMIT      = TYPE_ERROR
APPROVED_PLAN_V1 -> MODIFIED_PLAN_V2         = TYPE_ERROR
```

---

# 33｜V1.1 PRODUCT STATE MACHINE

```yaml
DAIL_AUTHORING_STATE:
  WELCOME: "等待使用者描述想做的東西"
  DISCOVERY: "多輪需求探索"
  FEASIBILITY_REVIEW: "許願需求／能力可行性掃描"
  DEPENDENCY_REVIEW: "資料、API、工具、權限與 Executor 掃描"
  REQUIREMENT_MODELING: "建立可工程化需求"
  PREFLIGHT: "完整缺口／衝突掃描"
  PLAN_DRAFT: "形成企畫草案"
  PLAN_REVISION: "與使用者修訂企畫"
  AWAITING_HUMAN_COMMIT: "等待綁定 plan_id/version 的明示批准"
  DAIL_GENERATION: "取得 Commit 後產生正式 DAIL"
  DAIL_VALIDATION: "型別、邊界、責任與 capability 驗證"
  TARGET_COMPILATION: "選配：轉成目標 Runtime artifact"
  MATERIAL_CHANGE_HOLD: "重大變更需退回企畫重新批准"
  FINAL_PACKAGE_READY: "交付已驗證 DAIL／target artifact 與證據狀態"
```

---

# 34｜V1.1 REGRESSION / CONFORMANCE

```yaml
V1_1_AUTHORING_CONFORMANCE:
  A01_NO_PREMATURE_GENERATION:
    pass: "Human Commit 前不產生宣稱為 final 的 DAIL Program。"

  A02_WISHFUL_REQUIREMENT:
    pass: "許願結果不得直接升格 capability；必須 reframe / hold / reject。"

  A03_DATA_BEFORE_SPEC:
    pass: "關鍵資料依賴未決時不得宣稱企畫 READY。"

  A04_DATA_AUTHORITY:
    pass: "資料存在不等於有權取得。"

  A05_SQL_DELEGATION:
    pass: "有 database executor 時，集合查詢由 database engine 執行，不以 LLM token generation 模擬。"

  A06_DETERMINISTIC_OFFLOAD:
    pass: "精確／大量機械計算優先委派 deterministic executor。"

  A07_PLAN_VERSION_COMMIT:
    pass: "Commit 綁定 plan_id/version；模糊同意不自動升格正式批准。"

  A08_MATERIAL_CHANGE_REAPPROVAL:
    pass: "批准後實質改企畫必須升版並重新取得 Commit。"

  A09_EXECUTOR_MISSING_HOLD:
    pass: "必要 executor 不存在時標 dependency hold，不假裝 AI 萬能。"
```

---

# 35｜本版尚未完成的工程缺口

```yaml
OPEN_ENGINEERING_GAPS:
  - id: "G01_REFERENCE_COMPILER"
    status: "NOT_IMPLEMENTED"
    question: "如何建立可重現的 Natural Language → DAIL compiler reference implementation？"

  - id: "G02_FORMAL_GRAMMAR"
    status: "PARTIAL"
    question: "是否需要獨立 EBNF / JSON Schema / AST specification？"

  - id: "G03_SEMANTIC_EQUIVALENCE"
    status: "WORKING"
    question: "如何測試 paraphrase normalization 與 material semantic change？"

  - id: "G04_CAPABILITY_REGISTRY"
    status: "NOT_STANDARDIZED"
    question: "跨供應商 capability namespace 如何避免同名異義？"

  - id: "G05_TARGET_CONFORMANCE"
    status: "NOT_IMPLEMENTED"
    question: "如何認證 target adapter 沒有靜默丟失 DAIL 語義？"

  - id: "G06_RUNTIME_CONFORMANCE"
    status: "NOT_IMPLEMENTED"
    question: "如何區分模型只是讀懂 DAIL、表面遵守 DAIL、與可重現地符合 DAIL contract？"

  - id: "G07_ANALOGY_MODULE"
    status: "RESEARCH_ENTRY"
    question: "是否建立獨立 Structural Analogy capability / benchmark？"

  - id: "G08_AUTHORING_SHELL_REFERENCE_RUNTIME"
    status: "NOT_IMPLEMENTED"
    question: "如何把 Welcome / Discovery / Preflight / Plan / Human Commit state machine 做成 reference product runtime？"

  - id: "G09_DEPENDENCY_DISCOVERY_STANDARD"
    status: "WORKING"
    question: "如何讓 Data / Tool / API / Authority dependency discovery 在不同 domain 中可重現？"

  - id: "G10_EXECUTION_PLACEMENT_REGISTRY"
    status: "WORKING"
    question: "哪些 workload 應標為 deterministic executor preferred，哪些保留給 AI semantic reasoning？"

  - id: "G11_MATERIAL_CHANGE_CLASSIFIER"
    status: "NOT_STANDARDIZED"
    question: "哪些變更必須觸發 plan version increment 與 human reapproval？"
```

這些缺口不得被 V1.1 文件格式的完整外觀掩蓋。

---

# 36｜最終根句

> **自然語言負責讓人說出想要什麼；DAIL 負責把那個想要變成可審計的 AI 語義程序。**
>
> **DAIL 不預寫答案，它宣告生成世界的結構、方向、邊界、責任與顯影資格。**
>
> **DAIL 寫的是語義需求；Target Adapter 決定怎麼翻譯；Runtime 決定實際能不能做到；證據決定我們有資格宣稱做到哪一層。**
>
> **先把願望變成可實作企畫，先把依賴找齊，再讓人類正式 Commit；AI 做語義工作，確定性引擎做確定性運算。**

---

# Appendix A｜工程師最小使用流程 V1.1

```text
1. 啟動 Authoring Shell / Welcome
2. 多輪描述需求
3. 跑 Feasibility / Wishful Requirement Gate
4. 掃 Data / Tool / API / Authority / Executor Dependencies
5. 建立 Dependency Contracts
6. 跑 Preflight Audit
7. 形成有 plan_id / version 的 Final Project Plan
8. 等待 Human Commit
9. 明確批准後才產生 DAIL Source
10. Normalize 成 DAIL-IR
11. 跑 Type / Boundary / Responsibility Validator
12. 選 Target Profile
13. Compile target artifact
14. SQL／精確計算／大規模 mechanical workload 委派 deterministic executor
15. 回報 semantic loss / unsupported capability / dependency gap
16. 執行 target-level test
17. 只依 evidence ladder 宣稱完成程度
18. 若出現 material plan change，退回企畫升版並重新批准
```

# Appendix B｜產品外觀：不是一鍵 Prompt Generator

建議 UI：

```text
┌──────────────────────────────────────┐
│ Welcome to DAIL                      │
│ 先告訴我，你想做什麼？               │
└──────────────────────────────────────┘
                 ↓
         多輪需求對話
                 ↓
       Feasibility / Dependency
                 ↓
          Preflight Audit
                 ↓
        Final Project Plan
       PLAN-001 / Version 1.0
                 ↓
     [批准企畫並開始生成]
                 ↓
           Generate DAIL
                 ↓
           Choose Target
                 ↓
            Compile / Test
```

一般使用者可以把它理解成 Prompt Generator 或 AI App Builder。

工程底層實際是：

```text
Conversational Design
→ Feasibility Audit
→ Dependency Contract
→ Human-Approved Project Plan
→ Semantic Compiler
→ DAIL-IR
→ Target Compiler
→ Deterministic Executor / AI Runtime Division
→ Runtime Artifact
```

# Appendix C｜SQL / Database 最小示例

使用者：

> 幫我做一個可以問公司銷售資料的 AI。

Authoring Shell 應先確認：

```text
資料在哪裡？
→ PostgreSQL

有 schema 嗎？
→ orders / customers / products

AI 有讀取權嗎？
→ read-only credential

需要即時資料嗎？
→ 每次查詢讀 current database
```

形成責任分工：

```text
Human question
→ AI semantic parse
→ SQL generation
→ SQL Validator / permission check
→ PostgreSQL executes query
→ result rows
→ AI explanation
```

禁止設計成：

```text
Export entire database
→ stuff into LLM context
→ ask LLM to count / join / sort by itself
```

除非只是極小、明確、非權威性的教學樣本，且不以此冒充正式 database execution。

---

**文件結束 / End of Specification**
