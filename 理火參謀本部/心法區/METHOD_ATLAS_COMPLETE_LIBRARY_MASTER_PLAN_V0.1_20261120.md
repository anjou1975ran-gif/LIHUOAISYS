# METHOD ATLAS COMPLETE LIBRARY MASTER PLAN V0.1
## 理火參謀本部｜完整心法庫施工總規格 × 法律四庫 204 域 Coverage Scanner

**版本：** V0.1-WORKING  
**日期：** 2026-11-20  
**法位：** MASTER_BUILD_PLAN / REGISTRY_CANDIDATE / NOT_METHOD_PACK / NOT_RUNTIME / NOT_RATIFIED  
**用途：** 先鎖定「完整心法庫要做到什麼、怎麼分層、怎麼施工、怎麼驗收、怎麼提交」，再交由 WORK 逐包製作與推送。  
**重要：** 本檔不新增任何學科核心心法，不替任何未完成學科宣稱成立。

---

# 0｜核心決議

> **完整心法庫不是大學系所清單，也不是把所有專業知識塞進 Project。**

完整心法庫的任務是：

```text
遇到一個問題
→ 知道哪些「眼睛」可能改變第一觀察
→ 知道哪些只是領域／功能方法
→ 知道何時需要專業 Agent / 外部證據
→ 能留下 Method Routing provenance
```

法律四庫 204 域作為 Coverage Scanner：

```text
204 LEGAL DLM
!=
204 METHOD PACKS
```

而是：

```text
204 REAL-WORLD LEGAL DOMAINS
→ SCAN REALITY COVERAGE
→ FIND MISSING METHOD LENSES
→ ROUTE TO DISCIPLINE / DOMAIN / MODULE / EXPERT
```

---

# 1｜上位不變量

沿用學科心法總綱：

```text
METHOD
=
HOW YOU FIRST SEE THE PROBLEM

KNOWLEDGE
=
WHAT INFORMATION YOU HAVE

SEAT
=
WHAT YOU ARE RESPONSIBLE TO ASK

STANCE
=
WHAT YOU CURRENTLY SUPPORT / OPPOSE / HOLD
```

硬鎖：

```text
MODEL != SEAT != METHOD != KNOWLEDGE != STANCE

METHOD PACK != KNOWLEDGE DATABASE
METHOD PACK != PROFESSIONAL AGENT
METHOD PACK != EXPERT AUTHORITY
METHOD ROUTED != METHOD EFFECTIVE
METHOD EFFECTIVE != EXPERT CAPABILITY
```

完整心法庫只治理 Method availability / selection / first observation，不創造外部專業資格。

---

# 2｜完整心法庫分層

## L0｜ATLAS CORE
控制：
- 註冊
- 版本
- 准入
- Method Shift Test
- Coverage
- Routing metadata
- 非回退規則

## L1｜FOUNDATIONAL OBSERVATION PACK
「控制眼睛」

資格：
- 能系統性改變第一觀察；
- 有獨立 evidence preference；
- 有獨立 causality model；
- 跨多場域有效；
- 能通過 Method Shift Test。

## L2｜DOMAIN / ACTION PACK
「控制大型場域」

資格：
- 在大型實踐場域中有穩定第一觀察；
- 不只是單一流程；
- 可能依賴一個或多個 L1 主包。

## L3｜FUNCTIONAL METHOD MODULE
「控制手」

用途：
- 組織職能
- 專業流程
- 責任接口
- 實務方法

## L4｜OPERATIONAL SKILL
「控制工具」

用途：
- 明確輸入／輸出
- 步驟
- 工具
- 格式化執行

## OUTSIDE ATLAS｜PROFESSIONAL SUPPORT
不是心法層。

```text
METHOD
→ FIRST OBSERVATION

PROFESSIONAL SUPPORT
→ SCOPED MATERIAL / EXPERT RETURN
```

兩者不可合併。

---

# 3｜目前已完成／已存在資產

## 3.1 現行主包

```yaml
CURRENT_PACKS:
  V0.2.A: 社會學
  V0.2.B: 歷史學
  V0.2.C: 法學
  V0.2.D: 經濟學
  V0.2.E: 政治學
  V0.2.F: 管理學
  V0.2.G: 心理學
  V0.2.H: 教育學
  V0.2.I: 哲學
  V0.2.J: 人類學
  V0.2.K: 傳播學
```

## 3.2 既有專門心法／模組

- 理火金融心法｜市場結構篇
- AI 小說心法｜敘事物理學
- 風月場關係話術心法
- AI 友善版學科包

以上不自動等於完整主包。

---

# 4｜V0.2 主序列擴充 Registry

以下先鎖「要做什麼」，不在本檔寫核心內容。

## WAVE 1｜原始 Phase 1 缺口 + Staff-HQ Runtime 高價值缺口

```yaml
WAVE_1:
  V0.2.L:
    discipline_id: statistics
    chinese_name: 統計學
    class: FOUNDATIONAL_OBSERVATION
    priority: P0
    first_look_target: "樣本、測量、不確定性、推論、基準率、偏差、相關與因果"
    legal_204_relevance: VERY_HIGH

  V0.2.M:
    discipline_id: computer_science
    chinese_name: 計算機科學
    class: FOUNDATIONAL_OBSERVATION
    priority: P0
    first_look_target: "表示、演算法、狀態、複雜度、介面、計算邊界、系統失效"
    legal_204_relevance: VERY_HIGH

  V0.2.N:
    discipline_id: medicine_public_health_evidence
    chinese_name: 醫學／公共衛生／實證醫學
    class: DOMAIN_ACTION
    priority: P0
    first_look_target: "個體與群體、診斷、因果、風險、效果、傷害、證據階層"
    legal_204_relevance: VERY_HIGH

  V0.2.O:
    discipline_id: international_relations
    chinese_name: 國際關係
    class: FOUNDATIONAL_OBSERVATION
    priority: P0
    first_look_target: "無最高權威、多行為體、安全困境、聯盟、威懾、制度合作"
    legal_204_relevance: VERY_HIGH

  V0.2.P:
    discipline_id: geopolitics
    chinese_name: 地緣政治
    class: DOMAIN_ACTION
    priority: P0
    first_look_target: "空間、交通線、資源、海陸、縱深、 chokepoint、可達性"
    legal_204_relevance: HIGH

  V0.2.Q:
    discipline_id: systems_engineering
    chinese_name: 系統工程
    class: DOMAIN_ACTION
    priority: P0
    first_look_target: "需求、介面、依賴、failure mode、驗證、恢復、生命週期、trade-off"
    legal_204_relevance: VERY_HIGH

  V0.2.R:
    discipline_id: linguistics_pragmatics_semiotics
    chinese_name: 語言學／語用學／符號學
    class: FOUNDATIONAL_OBSERVATION
    priority: P0
    first_look_target: "語義、語用、指稱、預設、含意、語境、符號與意義運作"
    legal_204_relevance: MEDIUM_HIGH

  V0.2.S:
    discipline_id: decision_science_operations_research
    chinese_name: 決策科學／Operations Research
    class: FOUNDATIONAL_OBSERVATION
    priority: P0
    first_look_target: "決策變數、限制、目標、trade-off、不確定性、scenario、robustness"
    legal_204_relevance: HIGH

  V0.2.T:
    discipline_id: intelligence_analysis
    chinese_name: 情報分析
    class: DOMAIN_ACTION
    priority: P0
    first_look_target: "來源可靠度、資訊可信度、collection gap、競爭假說、欺敵、交叉驗證、confidence"
    legal_204_relevance: HIGH
```

Wave 1 完成後，Staff-HQ 才算第一次具有：
證據／技術／健康／國際／空間／系統／語言／決策／情報九種目前明顯不足的專業眼睛。

---

# 5｜WAVE 2｜法律 204 域暴露出的主要場域缺口

```yaml
WAVE_2:
  V0.2.U:
    discipline_id: public_policy_public_administration
    chinese_name: 公共政策／公共行政
    class: DOMAIN_ACTION
    priority: P1

  V0.2.V:
    discipline_id: security_studies
    chinese_name: 安全研究
    class: DOMAIN_ACTION
    priority: P1

  V0.2.W:
    discipline_id: geography_spatial_studies
    chinese_name: 地理學／空間研究
    class: FOUNDATIONAL_OBSERVATION
    priority: P1

  V0.2.X:
    discipline_id: science_technology_studies
    chinese_name: 科技與社會研究 STS
    class: FOUNDATIONAL_OBSERVATION
    priority: P1

  V0.2.Y:
    discipline_id: information_science_knowledge_organization
    chinese_name: 資訊科學／知識組織
    class: FOUNDATIONAL_OBSERVATION
    priority: P1

  V0.2.Z:
    discipline_id: criminology_criminal_justice
    chinese_name: 犯罪學／刑事司法研究
    class: DOMAIN_ACTION
    priority: P1

  V0.2.AA:
    discipline_id: social_work_social_policy
    chinese_name: 社會工作／社會政策
    class: DOMAIN_ACTION
    priority: P1

  V0.2.AB:
    discipline_id: demography_population_studies
    chinese_name: 人口學／人口研究
    class: FOUNDATIONAL_OBSERVATION
    priority: P1

  V0.2.AC:
    discipline_id: environmental_climate_ecology
    chinese_name: 環境／氣候／生態系統研究
    class: DOMAIN_ACTION
    priority: P1

  V0.2.AD:
    discipline_id: urban_built_environment
    chinese_name: 都市／建成環境研究
    class: DOMAIN_ACTION
    priority: P1

  V0.2.AE:
    discipline_id: mathematics_formal_methods
    chinese_name: 數學／形式方法
    class: FOUNDATIONAL_OBSERVATION
    priority: P1

  V0.2.AF:
    discipline_id: biology_life_sciences
    chinese_name: 生物學／生命科學
    class: FOUNDATIONAL_OBSERVATION
    priority: P1

  V0.2.AG:
    discipline_id: physics_physical_systems
    chinese_name: 物理學／物理系統
    class: FOUNDATIONAL_OBSERVATION
    priority: P1

  V0.2.AH:
    discipline_id: chemistry_materials
    chinese_name: 化學／材料科學
    class: FOUNDATIONAL_OBSERVATION
    priority: P1

  V0.2.AI:
    discipline_id: earth_science_geoscience
    chinese_name: 地球科學／地質與地球系統
    class: FOUNDATIONAL_OBSERVATION
    priority: P1
```

---

# 6｜WAVE 3｜人文、制度與創意完備

```yaml
WAVE_3:
  V0.2.AJ:
    discipline_id: literature_narratology
    chinese_name: 文學／敘事學
    class: FOUNDATIONAL_OBSERVATION
    priority: P2
    note: "不得以 AI小說心法取代完整文學／敘事學。"

  V0.2.AK:
    discipline_id: religious_studies_mythology
    chinese_name: 宗教學／神話學
    class: FOUNDATIONAL_OBSERVATION
    priority: P2

  V0.2.AL:
    discipline_id: design_human_centered_design
    chinese_name: 設計學／Human-Centered Design
    class: DOMAIN_ACTION
    priority: P2

  V0.2.AM:
    discipline_id: art_culture_heritage_studies
    chinese_name: 藝術／文化／文化遺產研究
    class: DOMAIN_ACTION
    priority: P2
```

---

# 7｜V0.3 功能型 Method Module Registry

V0.3 才開始「補手腳」。

## 7.1 MONEY / ENTERPRISE

- accounting｜會計
- auditing_assurance｜審計／確信
- tax｜稅務
- finance_financial_systems｜金融／銀行／資本市場
- insurance_risk_transfer｜保險／風險移轉
- corporate_governance｜公司治理
- strategy_entrepreneurship｜策略／創業
- organizational_behavior_hr｜組織行為／人力資源
- marketing_consumer｜行銷／消費者行為
- operations_supply_chain_logistics｜營運／供應鏈／物流
- project_program_management｜專案／Program 管理
- risk_compliance_internal_control｜風險／法遵／內控

## 7.2 STATE / PUBLIC POWER

- public_finance_budgeting｜公共財政／預算
- regulatory_governance｜監管治理
- public_procurement｜政府採購
- diplomacy_negotiation｜外交／談判
- emergency_disaster_management｜緊急／災害管理
- defence_military_studies｜國防／軍事研究
- migration_refugee_studies｜移民／難民研究

## 7.3 PERSON / SOCIAL RELATIONS

- labor_industrial_relations｜勞動／工業關係
- family_studies｜家庭研究
- child_development_protection｜兒少發展／保護
- disability_studies｜障礙研究
- aging_gerontology｜高齡／老年學
- care_systems｜照護系統
- consumer_studies｜消費者研究

## 7.4 INFORMATION / DIGITAL

- cybersecurity｜網路安全／資安
- data_governance_privacy｜資料治理／隱私
- ai_ml_systems｜AI／ML 系統
- software_engineering｜軟體工程
- hci_ux｜人機互動／UX
- digital_identity_trust｜數位身分／信任
- telecommunications_networks｜電信／網路系統
- journalism_media_practice｜新聞／媒體實務
- innovation_ip_strategy｜創新／智慧財產策略

## 7.5 PHYSICAL / RESOURCE / INFRASTRUCTURE

- civil_construction｜土木／建築工程
- transport_mobility｜交通／運輸
- energy_systems｜能源系統
- utilities_infrastructure｜公共事業／基礎設施
- agriculture_food_systems｜農業／食物系統
- water_resource_management｜水資源
- forestry_fisheries_conservation｜森林／漁業／保育
- mining_mineral_resources｜礦業／礦產
- space_systems｜太空系統

## 7.6 HEALTH / LIFE

- clinical_medicine｜臨床醫學
- epidemiology｜流行病學
- health_systems｜健康系統
- bioethics｜生物／醫學倫理
- pharmacology_drug_safety｜藥理／藥物安全
- biotech_biosafety｜生技／生物安全
- food_safety｜食品安全

---

# 8｜法律四庫 204 域 Coverage Scanner

來源：
- DB1 STATE + JUSTICE：57
- DB2 MONEY + ENTERPRISE：64
- DB3 PERSON + PRIVATE RELATIONS：41
- DB4 INFORMATION + PHYSICAL SYSTEMS：42

總計：
```text
57 + 64 + 41 + 42 = 204 UNIQUE DLM
```

## 8.1 Coverage 原則

每個 DLM 最終必須有：

```yaml
DLM_METHOD_COVERAGE:
  dlm_id:
  dlm_name:
  legal_method_pack: V0.2.C
  nonlaw_method_candidates: []
  domain_module_candidates: []
  possible_professional_support: []
  routing_reason:
  standing: COVERED|LAW_ONLY_WITH_REASON|OPEN_GAP
```

硬鎖：

```text
DLM TITLE
!=
AUTOMATIC METHOD ROUTE

LEGAL DOMAIN
!=
NONLAW METHOD

204 COVERAGE
!=
204 PACKS
```

Atlas 完備前：

```text
204 / 204 DLM
MUST BE CLASSIFIED
```

但允許：

```text
LAW_ONLY_WITH_REASON
```

不得為了 100% 數字硬造 Method。

---

# 9｜204 域 × Method Family Macro Matrix

以下是施工 coverage seed，不是最終自動 Router。

## DB1｜STATE + JUSTICE

### FOUNDATION_AUTHORIZATION
Method candidates：
政治學、歷史學、公共政策／公共行政、國際關係、地緣政治。

### EXTERNAL_SOVEREIGNTY
Method candidates：
國際關係、地緣政治、安全研究、歷史學、地理／空間研究。

### ADMINISTRATIVE_GOVERNANCE
Method candidates：
公共政策／公共行政、政治學、管理學、經濟學、傳播學。

### SECURITY_COERCION_EXCEPTION
Method candidates：
安全研究、國際關係、地緣政治、犯罪學、公共衛生、災害管理。

### INTEGRITY_SANCTION_ACCOUNTABILITY
Method candidates：
公共行政、管理學、犯罪學、哲學／倫理、審計／內控模組。

### ACCESS_FORUM_JURISDICTION
Method candidates：
國際關係、決策科學、管理學；部分領域可 LAW_ONLY_WITH_REASON。

### WRONG_OFFENCE_QUALIFICATION
Method candidates：
犯罪學、心理學、社會學、公共衛生、計算機科學／資安。

### PROCEEDING_EVIDENCE
Method candidates：
統計學、心理學、資訊科學、犯罪學。

### INTERIM_PROTECTION
Method candidates：
決策科學／風險；可 LAW_ONLY_WITH_REASON。

### JUDGMENT_EFFECT_ENFORCEMENT
Method candidates：
管理／執行系統；多數核心可 LAW_ONLY_WITH_REASON。

### POST_JUDGMENT_PENAL_VICTIM
Method candidates：
犯罪學、社會工作、心理學、社會政策。

## DB2｜MONEY + ENTERPRISE

### FLOW_PUBLIC_MONEY
經濟學、公共政策／行政、金融、會計、公共財政。

### FLOW_CREDIT_SECURITY
金融、經濟學、風險管理、決策科學。

### FLOW_PAYMENT_SETTLEMENT
金融、計算機科學、系統工程、資安。

### FLOW_CAPITAL_ALLOCATION
金融、經濟學、統計學、決策科學。

### FLOW_RISK_TRANSFER
經濟學、統計學、金融／保險、風險管理。

### FLOW_DIGITAL_VALUE
金融、計算機科學、STS、資安。

### CONTROL_INTEGRITY_DISCLOSURE
會計、審計、管理學、統計學、內控。

### CONTROL_PRUDENTIAL_SYSTEMIC
金融、經濟學、統計學、系統工程、風險管理。

### FAILURE_RESOLUTION_PROTECTION
金融、經濟學、管理學、社會政策。

### ORGANIZATION_FORM_IDENTITY
管理學、社會學、政治學；宗教團體可加宗教學。

### INTERNAL_GOVERNANCE_DUTY
管理學、組織行為、會計／審計、哲學／倫理。

### CONTROL_RESTRUCTURING_CONTINUITY
管理學、金融、決策科學、策略。

### MARKET_STRUCTURE_COMPETITION
經濟學、統計學、管理學／策略。

### MARKET_INTERMEDIATION_COMMUNICATION
傳播學、經濟學、行銷、計算機科學／平台。

### SECTOR_ECOSYSTEM_OPERATION
管理學、經濟學、傳播學，再按體育／旅遊／餐旅等領域加 Domain Module。

### CROSS_BORDER_MARKET_EXCHANGE
經濟學、國際關係、地緣政治、供應鏈／物流。

## DB3｜PERSON + PRIVATE RELATIONS

### RIGHTS_STATUS_EQUALITY
社會學、人類學、政治學、哲學、心理學、社會工作。

### FAMILY_STATUS_DEPENDENCY
心理學、社會學、人類學、人口學、社會工作。

### INSTITUTIONAL_PARTICIPATION
教育學、管理學、社會學、經濟學、心理學、勞動／職安模組。

### SOCIAL_RISK_CARE
醫學／公衛、社會工作、人口學、經濟學、公共政策。

### PROPERTY_POSITION_USE_GOVERNANCE
地理／空間、都市研究、經濟學、管理學。

### AUTHORITY_FIDUCIARY_CONTROL
管理學、組織行為、哲學／倫理。

### VOLUNTARY_TRANSACTION_EXCHANGE
經濟學、管理學、傳播學、計算機科學（電子交易）。

### SUCCESSION_TRANSFER_AFTER_DEATH
人口學、家庭研究、社會工作、心理學。

### NONCONSENSUAL_OBLIGATION_ADJUSTMENT
風險、系統工程、產品安全、醫學／公衛、經濟學。

### REMEDY_QUANTIFICATION
經濟學、統計學、決策科學。

## DB4｜INFORMATION + PHYSICAL SYSTEMS

### COMMUNICATION_TRUST_IDENTITY_INFRASTRUCTURE
計算機科學、系統工程、資訊科學、資安。

### DATA_PROCESSING_GOVERNANCE_FLOW
資訊科學、計算機科學、STS、統計學、管理學、資料治理。

### MEDIA_EXPRESSION_PUBLIC_INFORMATION
傳播學、語言學／語用、公共政策、新聞實務。

### KNOWLEDGE_SIGNAL_EXCLUSIVITY
資訊科學、STS、傳播學、管理／創新、人類學。

### SYSTEM_ALGORITHMIC_SECURITY_GOVERNANCE
計算機科學、系統工程、STS、決策科學、資安。

### BUILT_ENVIRONMENT_LAND_DEVELOPMENT
地理／空間、都市研究、系統工程、土木／建築模組。

### ENVIRONMENT_CLIMATE_ASSESSMENT
環境／氣候、生態、公共政策、經濟學、統計學。

### NATURAL_RESOURCE_BIOSPHERE_USE
環境／生態、地理、生命科學、經濟學、公共政策。

### ENERGY_ESSENTIAL_NETWORK_SERVICE
系統工程、經濟學、公共政策、能源／基礎設施模組。

### PHYSICAL_MOBILITY_LOGISTICS_FRONTIER
系統工程、地理、營運／物流、工程、國際關係。

### BIOLOGICAL_PRODUCT_SAFETY_LIFECYCLE
醫學／公衛、生命科學、化學／材料、統計、系統工程。

### CULTURAL_PHYSICAL_HERITAGE
歷史學、人類學、宗教／文學、公共政策、文化遺產研究。

---

# 10｜WORK 單包施工契約

WORK 每次只做一個 Pack。

## 10.1 開工前必讀

1. 本 Master Plan。
2. 學科心法總綱最新版。
3. 該 Pack 的父層／鄰近 Pack。
4. 相關法律 204 DLM cluster。
5. 至少兩個容易混淆的鄰近 Method Pack。

## 10.2 不得直接開寫正文

先在同一檔案 header 建立：

```yaml
PACK_PROPOSAL:
  pack_id:
  discipline_id:
  chinese_name:
  class:
  problem_it_first_sees:
  unit_of_analysis:
  evidence_preference_candidate:
  causality_model_candidate:
  closest_neighbor_packs: []
  why_not_module:
  why_not_skill:
  legal_204_clusters: []
  expected_method_shift:
  known_boundary:
  status: PROPOSED
```

若無法回答 `why_not_module`，不得升主包。

---

# 11｜每個正式 Pack 最低正文規格

每包至少包含：

1. 學科／領域核心定義。
2. 第一觀察。
3. 分析單位。
4. evidence preference。
5. causality model。
6. actor model。
7. time / scale model。
8. 主要學派／方法取向。
9. 每個主要心法：
   - core question
   - first move
   - evidence preference
   - causality
   - blind spot
   - failure mode
   - use when
   - avoid when
10. 與鄰近 Pack 的區分。
11. 204 DLM crosswalk。
12. Professional Support Trigger。
13. Method Routing metadata。
14. Method Shift Test。
15. Canonical Demonstration Case。
16. Boundary / non-expert statement。

---

# 12｜驗收 Gate

## G0｜IDENTITY / ADMISSION

必須回答：

```text
它真的改變眼睛嗎？
還是只是知識？
還是只是職能？
還是只是 Skill？
```

FAIL：
- 大學有這個系所以及格；
- 名詞很多所以及格；
- 法律 204 有對應領域所以及格。

## G1｜OBSERVATION SHIFT

同題 baseline vs Method：

```text
第一眼是否真的不同？
```

## G2｜EVIDENCE SHIFT

啟用後優先證據是否改變。

## G3｜CAUSALITY SHIFT

啟用後因果模型是否改變。

## G4｜NEIGHBOR DIFFERENTIATION

至少與兩個鄰近 Pack 對打。

例如：

```text
IR != 政治學
地緣政治 != IR
統計 != 經濟
CS != 系統工程
醫學 != 公衛
傳播 != 語言學
情報分析 != 一般研究
```

## G5｜BLIND SPOT / BOUNDARY

必須有：
- blind spot
- failure mode
- misuse
- high-risk boundary
- when professional support is required

## G6｜LEGAL-204 COVERAGE

該 Pack 必須列：
- primary relevant DLMs
- secondary relevant DLMs
- false-friend DLMs（看似相關但不應自動路由）
- routing reason

## G7｜ROUTING METADATA

至少：

```yaml
METHOD_ROUTING:
  trigger_signals: []
  suppress_signals: []
  preferred_seats: []
  forbidden_fixed_mapping: true
  multi_method_compatibility: []
  professional_support_trigger: []
```

`preferred_seats` 只是候選，不得形成 Seat=Method 固定配對。

## G8｜CANONICAL DEMO CASE

至少：
- baseline
- 3 個不同心法／方法回答
- observation shift
- evidence shift
- causality shift
- blind spot
- boundary
- audit result

## G9｜NEGATIVE CONTROL

至少一題證明：

```text
NO_METHOD_WITH_REASON
```

可以比硬套本 Pack 更好。

## G10｜SOURCE / VERSION INTEGRITY

- exact filename
- version
- Git blob / commit
- source provenance
- 不倒改已接受 Pack
- 新版另立

---

# 13｜驗收結果詞彙

```text
PASS
PARTIAL
FAIL
HOLD
NOT_TESTED
```

禁止只有「完成」。

Pack 狀態：

```text
REGISTERED
→ ASSIGNED
→ DRAFTED
→ SELF_AUDITED
→ METHOD_SHIFT_TESTED
→ CROSSWALK_CHECKED
→ REVIEW_READY
→ ACCEPTED_FOR_ATLAS
→ ROUTABLE
```

WORK 最多可自行推到：

```text
REVIEW_READY
```

不得自行宣稱：

```text
ACCEPTED_FOR_ATLAS
ROUTABLE
```

除非另有 Human / Atlas Maintainer 授權。

---

# 14｜WORK Git 提交規則

每次一包。

檔名：

```text
學科心法總目錄_<VERSION>_<序號>_<名稱>_整合版.md
```

Commit 建議：

```text
method-atlas: add <discipline_id> V0.2 candidate pack
```

每次提交必須同時更新：
- Master Registry status
- 204 coverage status
- 本包 test result

不得：
- 順手改其他 Pack；
- 重寫歷史版本；
- 因某包完成就改 Atlas Core 規則；
- 自動產生大量子檔；
- 把研究筆記當 canonical Pack。

---

# 15｜提案／審查回報固定格式

WORK 完成後 Chat 只回：

```yaml
PACK_COMPLETION_REPORT:
  pack_id:
  file:
  commit:
  blob:
  status: REVIEW_READY

  gates:
    G0:
    G1:
    G2:
    G3:
    G4:
    G5:
    G6:
    G7:
    G8:
    G9:
    G10:

  legal_204:
    primary_count:
    secondary_count:
    open_gap_count:

  neighbor_tests: []

  method_effectiveness_claim:
    allowed: false

  expert_capability_claim:
    allowed: false

  open_questions: []
```

---

# 16｜204 Coverage 全庫完成判準

```yaml
LEGAL_204_COVERAGE_COMPLETION:
  total_dlm: 204
  classified: 204

  each_dlm_requires:
    - legal_method_ref
    - nonlaw_method_candidates_or_law_only_reason
    - domain_module_candidate_if_material
    - professional_support_trigger_if_material

  forbidden:
    - keyword_only_routing
    - one_to_one_dlm_equals_method_pack
    - legal_domain_title_as_method_proof
    - fake_100_percent_coverage

  open_gap_allowed_during_build: true
  open_gap_allowed_at_final: false
```

---

# 17｜Atlas 全庫完成判準

完整不是「每個候選都寫完」。

完整是：

```text
MAIN OBSERVATION COVERAGE
+
DOMAIN COVERAGE
+
204 DLM COVERAGE
+
METHOD SHIFT TESTS
+
NEGATIVE CONTROLS
+
ROUTING METADATA
+
PROFESSIONAL SUPPORT BOUNDARIES
```

Final Gate：

```yaml
ATLAS_COMPLETION:
  current_existing_packs_reviewed: REQUIRED
  wave_1_complete: REQUIRED
  wave_2_critical_gaps_closed: REQUIRED
  wave_3: MAY_HAVE_SCOPED_DEFERRALS

  legal_204_classified: 204/204
  unresolved_method_gap: 0
  unresolved_pack_overlap: 0

  all_routable_packs:
    method_shift_tested: true
    neighbor_differentiated: true
    boundary_present: true
    canonical_demo_present: true

  professional_agent_boundary: preserved
  no_pack_claims_expert_authority: true
```

---

# 18｜推薦施工順序

不要照字母做。

第一批：

```text
1 統計學
2 計算機科學
3 系統工程
4 醫學／公共衛生／實證醫學
5 國際關係
6 地緣政治
7 語言學／語用／符號學
8 決策科學／OR
9 情報分析
```

第二批：

```text
10 公共政策／公共行政
11 安全研究
12 地理／空間
13 STS
14 資訊科學
15 犯罪學／刑事司法
16 社會工作／社會政策
17 人口學
18 環境／氣候／生態
19 都市／建成環境
```

再依 204 coverage gap 決定自然科學與功能模組施工順序。

---

# 19｜核心防爆炸規則

```text
LEGAL DLM IS A COVERAGE SIGNAL.
NOT A PACK GENERATOR.
```

```text
UNIVERSITY DEPARTMENT EXISTS
!=
METHOD PACK REQUIRED
```

```text
PROFESSIONAL FUNCTION EXISTS
!=
FOUNDATIONAL OBSERVATION PACK REQUIRED
```

```text
MORE PACKS
!=
MORE COMPLETE
```

真正完整：

> **該看見的差異看得見；該分層的責任不混；該叫專家的時候知道自己還不是專家。**

---

# 20｜目前法位

```yaml
METHOD_ATLAS_MASTER_PLAN:
  current_main_packs: 11
  legal_dlm_scanner: 204
  legal_db_distribution:
    DB1: 57
    DB2: 64
    DB3: 41
    DB4: 42

  wave_1_registered: true
  wave_2_registered: true
  wave_3_registered: true
  functional_module_registry: true

  new_pack_core_written: false
  new_pack_accepted: false
  legal_204_full_crosswalk_completed: false
  runtime_router_updated: false
```

---

# 21｜收斂句

> **法律四庫告訴我們世界會出現哪些責任問題；心法庫要回答的不是每個問題的答案，而是遇到這些世界時，AI 應該先借哪一雙眼睛。**

以及：

> **先把書架、編號、准入、驗收和 coverage 鎖好；之後 WORK 只需要一本一本寫，不再重造圖書館。**

**END**
