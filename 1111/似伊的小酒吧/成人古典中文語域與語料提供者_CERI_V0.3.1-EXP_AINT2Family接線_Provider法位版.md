# 成人古典中文語域與語料提供者 CERI V0.3.1-EXP
## AINT V2 Family Wiring × Provider Law Position × V3.5 Dependency Clarification

```yaml
DOCUMENT_UPGRADE:
  from: "CERI V0.3-EXP"
  to: "CERI V0.3.1-EXP"
  version_id: "CERI-V0.3.1-AINT2-PROVIDER-WIRING-ALIGNMENT"
  date: "2026-08-27"
  status: "GM_AUTHORIZED_PROVIDER_WIRING_PATCH_CANDIDATE"

PARENT_SOURCE_LOCK:
  file: "成人古典中文語域與語料提供者_CERI_V0.3-EXP_AINT2_RegisterProvider_FULL_CORPUS版.md"
  sha256: "3f704605037eefa4ab83573533fe85e57fd41bcff5624c238be033ce7d2c3ae2"
  inheritance: "FULL_EXCEPT_EXPLICIT_V0_3_1_SUPERSESSION"
  parent_modified_in_place: false

CURRENT_TARGET_FAMILY:
  runtime_family: "AINT V2.x REGISTER PROVIDER INTERFACE"
  current_project_candidate: "AINT V2.1-RC4-FULL"
  exact_version_required: false
```

> **V0.3.1 不改 FULL CORPUS、不改詞彙 provenance、不改 register precedence。**
>
> **本次只修：CERI 不再把 V2.0-RC1 當唯一當前 target；它正式定位為 AINT V2 family / compatible adult runtime 的可替換 Register Provider。**

---

# P0｜Provider Position

```yaml
CERI_WIRING_POSITION:
  runtime_class: "SCOPED_REGISTER_PROVIDER"
  sac_dependency: "INDEPENDENT"
  event_authority: false
  character_authority: false
  consent_authority: false
  relation_authority: false
  save_authority: false

  callable_by:
    - "AINT V2 compatible runtime"
    - "other compatible adult runtime with equivalent Provider Contract"

  direct_host_manifestation_owner: false
  direct_lihuo_main_system_binding: false
  direct_sac_binding: false
  return_to_caller_required: true
```

---

# P1｜AINT Target Supersession

V0.3 繼承 metadata 中：

```text
aint_target = AINT V2.0-RC1-FULL
```

自 V0.3.1 起解釋為歷史 refactor target，不再限制現行相容 Runtime。

```yaml
AINT_TARGET_V0_3_1:
  historical_refactor_target: "AINT V2.0-RC1-FULL"
  compatible_family: "AINT V2.x REGISTER PROVIDER CONTRACT"
  current_project_candidate: "AINT V2.1-RC4-FULL"
  exact_version_required: false
  contract_required:
    - "semantic_node input"
    - "character_voice_constraints"
    - "narrator / locale / era register"
    - "provider cannot establish event / consent / relation"
    - "provider returns candidates and warnings to caller"
```

---

# P2｜First-Touch / Return / Scope

```text
HOST establishes qualified event
↓
AINT (or compatible caller) establishes semantic node
↓
CERI scoped register request
↓
lexical / syntactic / vocal / body-noun candidates
+ provenance / ambiguity / drift warnings
↓
RETURN TO CALLER
↓
caller / Host decides manifestation
```

```text
CERI SOURCE BANK
!= CHARACTER VOICE OWNER
!= EVENT OWNER
!= WORLD FACT OWNER
!= SAC PROVIDER
```

---

# P3｜接線回歸

```yaml
CERI_V0_3_1_WIRING_REGRESSION:
  corpus_unchanged: "PASS"
  provider_contract_preserved: "PASS"
  aint_v2_family_compatibility: "PASS"
  exact_version_lock_removed_from_current_target: "PASS"
  direct_main_system_binding_forbidden: "PASS"
  return_to_caller_required: "PASS"
  character_voice_precedence_preserved: "PASS"

EVIDENCE:
  document_patch_written: true
  runtime_regression_tested: false
  host_enforced: false
```

---

# INHERITED BODY｜V0.3 完整繼承正文

以下完整繼承 V0.3。若舊 `aint_target` metadata 與本節衝突，以 V0.3.1 的 family-compatible target 為現行語義；FULL CORPUS 與 Provider Contract 其餘內容不變。

---

# 成人古典中文語域與語料提供者 CERI V0.3-EXP
# Classical Erotic Register & Corpus Provider

## Register Provider × Corpus Bank × Historical Source Provenance × AINT V2 Interface

```yaml
DOCUMENT:
  title_zh: "成人古典中文語域與語料提供者"
  title_en: "Classical Erotic Register & Corpus Provider"
  short_id: "CERI"
  version: "V0.3-EXP"
  date: "2026-08-24"
  document_type: "OPTIONAL_CLASSICAL_CHINESE_ADULT_REGISTER_PROVIDER"
  status: "GM_AUTHORIZED_PROVIDER_REFACTOR_CANDIDATE_PENDING_REGRESSION"

REVISION_LINEAGE:
  parent:
    file: "成人古典語域與床上互動外掛_CERI_V0.2-EXP_FULL_CORPUS_金瓶梅肉蒲團_語域長距離痛感整合版.md"
    version: "V0.2-EXP"
    sha256: "9c0099be356606a919c1265eae1f84f99525ef716e3f8231fc081029b5d3f6d0"
    treatment: "REGISTER_AND_CORPUS_INHERITANCE"

  aint_target:
    file: "成人親密敘事模組_AINT_V2.0-RC1-FULL_PortableHostContract_MaterialTransition_18卡_RegisterProvider版.md"
    version: "V2.0-RC1-FULL"
    treatment: "OPTIONAL_REGISTER_PROVIDER"

  structural_promotion:
    moved_to_aint_v2:
      - "PAIN CHANNEL SEPARATION -> PAIN CHANNEL LOCALITY"
      - "NEXT-STEP AUTHORSHIP"
      - "TRANSITION CAUSALITY"
      - "LONG-HORIZON DEGRADATION -> LONG-HORIZON INTEGRITY"

POSITION:
  event_authority: false
  character_authority: false
  consent_authority: false
  relation_authority: false
  knowledge_authority: false
  save_authority: false

  owns:
    - lexical_candidate_supply
    - syntactic_candidate_supply
    - body_noun_register
    - vocal_and_bed_language_candidates
    - corpus_provenance
    - source_disambiguation
    - anti_euphemism_drift_signal
    - anti_vulgarization_drift_signal
```

> **CERI 不再負責「性愛互動怎麼運作」；它只回答「已成立的成人互動，在古典中文語域裡有哪些可用語言與構成」。**

---

# 0｜V0.3 收口決定

V0.2 同時承擔兩種工作：

```text
A. 通用成人互動結構
B. 古典中文語域／語料
```

V0.3 正式拆開：

```text
通用互動結構
→ AINT V2

古典中文語域／語料
→ CERI V0.3
```

因此 CERI 可以被 AINT 調用，也可以被其他具相容 Provider Contract 的成人 Runtime 調用。

---

# 1｜Provider Contract

```yaml
CERI_PROVIDER_CONTRACT:
  provider_family: "CERI_CLASSICAL_CHINESE_REGISTER"
  exact_version_required: false

  input:
    - semantic_node
    - narrator_profile
    - character_voice_constraints
    - locale_or_era_register
    - player_explicit_rendering_request
    - body_noun_register_hint
    - vocal_function
    - source_density_preference

  output:
    - lexical_candidates
    - syntactic_candidates
    - vocal_candidates
    - body_noun_candidates
    - source_provenance_tags
    - ambiguity_warnings
    - register_drift_warnings

  must_not:
    - "決定人物想不想"
    - "決定人物是否同意"
    - "建立高潮／關係／成人事件事實"
    - "改寫人物人格或知識"
    - "把來源文本行為正當性搬進宿主"
    - "直接寫 SAVE"
```

---

# 2｜Register 優先序

```yaml
CERI_REGISTER_ROUTER:
  precedence:
    1: "HOST CHARACTER CURRENT VOICE"
    2: "HOST CURRENT ERA / LOCALE / ROLE REGISTER"
    3: "CURRENT RELATION / PUBLIC-PRIVATE FRAME"
    4: "PLAYER EXPLICIT RENDERING REQUEST"
    5: "PLAYER ACTION LEXICON AS SOFT SIGNAL"
    6: "NARRATOR PROFILE"
    7: "CERI SOURCE BANK"

  locks:
    - "人物自己的聲音永遠優先於詞庫。"
    - "玩家現代詞不自動賦予 NPC 現代知識。"
    - "來源語料是候選，不是模板。"
    - "古典詞彙不自動證明時代真實性。"
```

---

# 3｜BODY NOUN REGISTER

```yaml
BODY_NOUN_REGISTER:
  FORMAL_ANATOMICAL:
    examples: ["乳房", "乳頭"]

  NEUTRAL_NARRATIVE:
    examples: ["胸", "胸前", "胸部"]

  CLASSICAL_EROTIC:
    source_examples: ["酥胸", "香乳", "乳峰", "肉峰"]

  COLLOQUIAL_BODY:
    examples: ["胸脯", "屁股"]

  VULGAR_BODY:
    examples: ["奶子", "奶頭", "雞巴"]
```

`奶子` 作乳房義可以是現代／低俗宿主 register，但不得因此偽稱是《金瓶梅》乳房語料。

---

# 4｜Narrator / Character / Player 不同步

```text
PLAYER INPUT REGISTER
        ↓ soft / explicit style signal
NARRATOR REGISTER

CHARACTER VOICE
        ↓ independent host authority
NPC SPEECH

CERI SOURCE BANK
        ↓ candidate resource only
LEXICAL / SYNTACTIC OPTIONS
```

人物可以乾淨而旁白粗；人物可以粗而旁白較中性。
CERI 不強迫同步。

---

# 5｜Register Drift

```yaml
REGISTER_DRIFT:
  ANTI_EUPHEMISM_DRIFT:
    "已建立的直接／低 register 不得整段無因果被洗成抽象高雅隱喻。"

  ANTI_VULGARIZATION_DRIFT:
    "已建立的文雅／克制 register 不得整段無因果被成人詞庫粗俗化。"

  rule:
    - "單次換詞不是 FAIL。"
    - "看整段 register 是否被來源詞庫拖走。"
```

---

# 6｜Composition Interface

CERI 不決定成人節點；它讀取 AINT／Host 已建立的 semantic node。

```yaml
CERI_COMPOSITION_INPUT:
  body_relation:
  active_body_parts:
  action_relation:
  rhythm:
  support_and_balance:
  pain_or_fatigue_if_host_exposes:
  vocal_capacity:
  character_speech_function:
  spatial_constraint:
  residue_from_prior_nodes:
  narrator_register:
  body_noun_register:
```

> **先有事件關係，再選詞。**

---

# 6｜FULL CORPUS 抽取方法與重要校正

本版不是把全文所有二字詞倒進詞庫，而是做「成人顯影語義域的全書掃描」：

1. 以兩書全文（GB18030 解碼）為 corpus；
2. 逐書掃描事件詞、器官詞、動作詞、聲音詞、床上話、姿勢、空間與高潮／餘波詞；
3. 以 exact substring raw hits 建索引；
4. 對高歧義詞另外做人讀語境校正；
5. `raw hits != sexual semantic hits`，原始計數只用來標示來源存在與密度，不能冒充純成人語義頻次。

## 6.1 本次最重要的語義校正

### 「奶子」不能直接當《金瓶梅》的乳房來源詞

《金瓶梅》原檔 `奶子` raw hits 很高，但逐句檢查後，**絕大多數／實際可見用法是「乳母、奶媽」義**，例如「領了個奶子來」「叫奶子來喂哥兒奶」一類。

因此本版正式鎖：

```yaml
JPM_NAIZI_DISAMBIGUATION:
  source_term: "奶子"
  raw_hits: 127
  dominant_semantics: "WET_NURSE / 乳母"
  classical_breast_lexicon_eligibility: false
  may_be_used_in_host_modern_vulgar_register: true
  host_source: "PLAYER / MODERN CHARACTER REGISTER"
```

也就是：**觀止裡玩家說「奶子」完全可以成立為現代／低俗身體詞，但不能偽稱它是從《金瓶梅》乳房描寫抽來的。**

《金瓶梅》真正可確認的乳房／乳頭詞包括：`酥胸、香乳、奶頭、奶頭兒`。

### 其他高歧義詞

```yaml
MIXED_TERM_LOCK:
  - "丟／丟了：大量一般語義；只有『丟身子、將丟未丟、我要丟了』等在成人語境才可高置信使用。"
  - "往來：一般往來很多；成人語境需由周邊 mechanics 判斷。"
  - "入港：可作談話／事情進入狀態，也可作成人隱喻。"
  - "房中：普通房內與房中術／性愛語境混合。"
  - "睡／上床：日常睡眠與成人事件混合。"
  - "摸／咬／托／扶：通用動作；CERI 必須先有 BODY RELATION，不能靠詞本身判成人事件。"
  - "快活／受用：成人快感與一般愉悅混合。"
```

---

# 7｜兩書最值得吸收的「句法／構成」而非單詞

## 7.1 《金瓶梅》：動作與床話同時發生

高價值不是單一淫詞，而是常見：

```text
身體動作
＋
稱呼／罵語／要求
＋
對方立刻調整或繼續
```

例如來源中可見的功能形：

- `親嘴／咂舌` 與飲酒、坐懷、摟抱同時發生；
- `慢著些`、`饒了奴`、`親達達` 等話直接嵌在動作裡；
- `兩廂迎湊`、`舉股相就` 把受方寫成真正的動作方；
- `顫聲柔語`、`沒口子叫` 是聲音表現，不自動等於內心真相。

## 7.2 《肉蒲團》： mechanics 被拆成可組合階段

高價值包括：

- `由淺入深`
- `由寬而緊`
- `抽送有度`
- `不猛不寬，不緩不急`
- `字字模糊`
- `上氣不接下氣`
- `似說話非說話`
- `似嘆氣非嘆氣`
- `將丟未丟`
- `已丟之後`
- `動極近靜`

其價值在於：

> **性愛不是一條「越來越快」線，而是可有位置、力度、語言容量、疲勞、停頓與波峰前後的多階段變化。**

---

# 8｜BREAST / NIPPLE SPECIALIZATION｜乳房／乳頭專項

本輪實跑顯示 V0.1 對乳房描寫仍太乾淨，因此 V0.2 建立專項。

```yaml
BREAST_REGISTER_BANK:

  source_classical:
    - "酥胸"
    - "香乳"
    - "奶頭／奶頭兒"
    - "乳峰"
    - "肉峰"

  host_modern_neutral:
    - "乳房"
    - "乳頭"
    - "胸"
    - "胸部"

  host_modern_low:
    - "胸脯"
    - "奶子"
    - "奶頭"

  actions_source_supported:
    - "摸"
    - "揣摸"
    - "揉"
    - "揉搓"
    - "捏"
    - "捻"
    - "托"
    - "咂"
    - "吮"
    - "咬"

  interaction:
    - "人物可自己調整力道"
    - "人物可按回某一位置"
    - "兩側敏感度不必相同"
    - "痛點可以局部關閉，其他接觸仍可成立"
```

## 8.1 「奶子」的法位

`奶子` 作「乳房」的低俗現代詞，**可由玩家／角色輸入強力點亮**。

它不是本版硬說成《金瓶梅》歷史乳房詞。

這個分離很重要：

> **來源語料的歷史事實，和宿主中文現在能使用的語域，不是同一件事。**

---

# 9｜V0.2 反模板與反污染

```yaml
CERI_V0_2_ANTI_TEMPLATE:

  AT-01:
    "禁止喘→顫→抓→更快→高潮成為預設成人曲線。"

  AT-02:
    "禁止把 ACTION BANK 當同義詞轉盤。"

  AT-03:
    "禁止為了看起來豐富而無因果換姿勢。"

  AT-04:
    "禁止每個古代人物都說親達達／冤家／心肝。"

  AT-05:
    "禁止每個現代粗口人物都說奶子／雞巴；仍要由人物與玩家 register 決定。"

  AT-06:
    "禁止把叫床當高潮、同意、戀愛或私人真相。"

  AT-07:
    "禁止把痛感自動色情化；痛就是一條獨立可觀察通道。"

  AT-08:
    "禁止把局部痛／局部拒絕擴張成未命中的全部事件。"

  AT-09:
    "禁止 NARRATOR SANITIZATION：低俗玩家輸入不能無因果整段洗成雙峰／曲線／柔軟輪廓。"

  AT-10:
    "禁止 NARRATOR VULGARIZATION：文雅玩家輸入也不能無因果整段洗成粗口。"

  AT-11:
    "禁止來源詞建立人物原本不存在的性慾、同意、技巧、人格與說話習慣。"

  AT-12:
    "不得直接仿寫或長段搬運《金瓶梅》《肉蒲團》；只抽取詞、短語、句法與構成關係重新生成。"
```

---

# 10｜V0.2 回歸矩陣

```yaml
REGRESSION:

  R1_REGISTER_AB:
    same_event_inputs:
      - "雙峰"
      - "乳房"
      - "胸"
      - "奶子"
    test:
      - "旁白 register 是否跟得住"
      - "NPC 語言是否仍獨立"

  R2_LONG_HORIZON:
    test:
      - "T1-T5"
      - "TRANSITION_CAUSALITY_LOCK"

  R3_CHARACTER_DIFFERENTIATION:
    cast_types:
      - "蘇清：直接粗口／即時回饋"
      - "醉花：控制—暴露／較少言"
      - "潘金蓮：市井挑逗"
      - "李師師：高控制語言"
    fail_if:
      "只剩同一篇性愛文換人物名"

  R4_PAIN_LOCALITY:
    test:
      - "痛點局部化"
      - "痛感不自動等快感"
      - "人物可以重新指定可碰／不可碰區"

  R5_SOURCE_OVERFIT:
    compare:
      - "C0 STRUCTURE ONLY"
      - "C1 LIGHT"
      - "C2 CLASSICAL PRIMARY"
      - "C3 SOURCE DENSE"
    goal:
      "找到語彙活化到偽古典模板之間的臨界點"
```

---

# 11｜FULL CORPUS LEXICON BANK

以下為本版從兩書全文成人顯影語義域整理出的 **249 個來源詞／短語候選**。

注意：

- 表內 `raw hits` 是 exact substring 原始命中，不是「純性愛語義次數」；
- `MIXED` 詞必須依上下文重新判定；
- 部分通用字（摸、托、咬、睡、丟）頻次很高，但不因命中就自動取得成人語義；
- 本表的價值是擴大候選語言空間，而不是讓生成器每段把詞全部用一遍。

---

## BODY_BREAST_AND_SURFACE｜乳房／身體表面

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 酥胸 | 11 | 1 | 古典艷稱；可作旁白 register，不宜人人固定使用 |
| 香乳 | 4 | 0 | 古典乳房稱謂；《金瓶梅》有明確成人語境 |
| 奶頭 | 4 | 0 | 直接部位詞；《金瓶梅》有成人語境 |
| 奶頭兒 | 1 | 0 | 口語化部位詞；《金瓶梅》有成人語境 |
| 乳峰 | 0 | 2 | 《肉蒲團》用例；偏修辭化 |
| 肉峰 | 0 | 1 | 《肉蒲團》用例；比乳峰更肉身 |
| 胸脯 | 2 | 0 | 日常身體詞 |
| 胸前 | 9 | 1 | 中性敘述詞 |
| 白屁股兒 | 1 | 0 | 《金瓶梅》床上直接稱說 |
| 屁股 | 38 | 0 | 低／日常 register；語義多用 |
| 粉項 | 6 | 0 | 古典外觀詞 |
| 玉體 | 10 | 0 | 古典修辭，容易過度文雅 |
| 香體 | 1 | 0 | 古典修辭 |
| 肌膚 | 6 | 8 | 中性／文雅 |
| 皮肉 | 5 | 16 | 較直接、肉身 |
| 白肉 | 3 | 0 | 直接視覺詞；需看上下文 |
| 朱唇 | 25 | 4 | 古典口唇修辭 |
| 舌頭 | 29 | 6 | 直接身體詞 |

---

## BODY_GENITAL_FEMALE｜女性器官／局部

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 牝戶 | 7 | 7 | 古典直稱，高成人語義 |
| 牝中 | 28 | 2 | 古典直稱，高成人語義 |
| 牝口 | 3 | 0 | 古典局部詞 |
| 陰戶 | 2 | 30 | 直接／古典；《肉蒲團》高頻 |
| 陰中 | 4 | 15 | 直接空間性稱呼 |
| 陰門 | 1 | 4 | 古典直稱 |
| 花心 | 10 | 9 | 古典情色局部詞，亦可能有比喻義 |
| 花蕊 | 2 | 0 | 古典艷稱，低頻 |
| 蛙口 | 6 | 0 | 《金瓶梅》成人局部隱稱 |
| 牝毛 | 1 | 0 | 古典體毛直稱 |
| 陰毛 | 0 | 2 | 《肉蒲團》直稱 |
| 毳毛 | 2 | 0 | 古典體毛詞 |

---

## BODY_GENITAL_MALE｜男性器官／局部

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 陽物 | 2 | 74 | 《肉蒲團》核心直接稱謂 |
| 那話 | 95 | 0 | 《金瓶梅》高頻避直稱；語境敏感 |
| 麈柄 | 15 | 0 | 《金瓶梅》古典隱稱，高成人語義 |
| 龜頭 | 17 | 4 | 直接部位詞 |
| 玉莖 | 4 | 0 | 古典艷稱 |
| 淫器 | 14 | 0 | 《金瓶梅》直接成人器物／器官詞 |
| 雞巴 | 1 | 1 | 兩書均有極低頻粗俗用例；低 register |
| 肉棒槌 | 0 | 1 | 《肉蒲團》粗俗／比喻式直稱 |
| 馬眼 | 2 | 0 | 局部直稱 |
| 二卵 | 2 | 0 | 古典粗直局部詞 |

---

## CONTACT_AND_TOUCH｜接觸／愛撫

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 親嘴 | 20 | 14 | 接吻事件直稱 |
| 咂舌 | 12 | 0 | 《金瓶梅》口舌接吻動詞 |
| 鳴咂 | 7 | 0 | 《金瓶梅》聲音＋口舌動作 |
| 摟抱 | 19 | 0 | 雙人身體包覆 |
| 摟住 | 3 | 19 | 動作結果更明確 |
| 摟定 | 6 | 0 | 保持性動作 |
| 抱住 | 11 | 7 | 保持／拉近 |
| 纏抱 | 0 | 1 | 《肉蒲團》低頻 |
| 貼伏 | 0 | 2 | 身體貼近構型 |
| 捱擦 | 1 | 2 | 摩擦／試探 |
| 挨擦 | 0 | 1 | 《肉蒲團》變體 |
| 摸 | 86 | 24 | 高頻通用動詞；需依 body relation 限定 |
| 揉 | 33 | 3 | 揉按／愛撫 |
| 揉搓 | 8 | 0 | 較強動作詞 |
| 捏 | 60 | 7 | 捏／拿捏 |
| 捻 | 13 | 0 | 細小指部動作 |
| 扳 | 18 | 4 | 調位／固定 |
| 托 | 139 | 18 | 支撐／承重／托起 |
| 扶 | 141 | 6 | 支撐／引導 |
| 按住 | 6 | 0 | 局部控制／停止位移 |
| 攥著 | 3 | 0 | 抓握 |
| 拉住 | 10 | 0 | 阻止離開／拉近 |
| 挑弄 | 6 | 0 | 細部挑逗 |
| 舔 | 2 | 3 | 直接口舌動作 |
| 舐 | 3 | 0 | 古典口舌動詞 |
| 咬 | 57 | 2 | 直接牙齒動作；痛感與情慾需分軸 |
| 吮 | 22 | 0 | 吸吮動詞；《金瓶梅》成人語境可見 |

---

## EVENT_LEVEL｜成人事件層

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 雲雨 | 30 | 3 | 古典性交總稱 |
| 交歡 | 13 | 0 | 性交／歡會總稱 |
| 交媾 | 6 | 8 | 直接事件稱謂 |
| 行房 | 11 | 12 | 房事總稱 |
| 同房 | 2 | 0 | 較中性 |
| 入港 | 13 | 0 | 《金瓶梅》成人隱喻；亦有非性用法，MIXED |
| 作歡 | 1 | 0 | 古典事件詞 |
| 幹事 | 23 | 85 | 《肉蒲團》大量成人用法，但仍須語境判斷 |
| 上床 | 46 | 19 | 事件／空間皆可能 |
| 做一處 | 47 | 0 | 《金瓶梅》親密／性交語境常見 |
| 廝會 | 4 | 0 | 私密相會 |
| 偷期 | 4 | 0 | 偷情／幽會類 |

---

## INTERCOURSE_MOTION｜性交動作骨架

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 往來 | 54 | 5 | 重要但 MIXED；不可把 raw count 當純成人 |
| 抽送 | 5 | 17 | 兩書均有，成人動作高辨識 |
| 抽拽 | 7 | 0 | 《金瓶梅》 |
| 抽提 | 4 | 0 | 《金瓶梅》 |
| 提送 | 1 | 0 | 《金瓶梅》低頻 |
| 送入 | 4 | 1 | 直接位移 |
| 插入 | 7 | 4 | 直接位移 |
| 插進 | 2 | 2 | 直接位移 |
| 頂入 | 6 | 0 | 《金瓶梅》 |
| 攮進去 | 4 | 0 | 《金瓶梅》粗直動詞 |
| 濡研 | 4 | 0 | 《金瓶梅》摩擦式動詞 |
| 濡攪 | 1 | 0 | 《金瓶梅》低頻 |
| 極力抽提 | 3 | 0 | 《金瓶梅》完整動作短語 |
| 盡沒至根 | 4 | 0 | 《金瓶梅》深度狀態短語 |
| 一舉一坐 | 2 | 0 | 《金瓶梅》往來構型 |
| 由淺入深 | 0 | 1 | 《肉蒲團》階段轉換 |
| 由寬而緊 | 0 | 1 | 《肉蒲團》身體狀態轉換 |
| 直抵 | 5 | 5 | 兩書均有；需上下文 |
| 徐徐 | 1 | 0 | 低頻速度／方式詞，不應單獨當成人詞 |
| 迎合 | 0 | 2 | 《肉蒲團》雙向回應 |
| 迎湊 | 4 | 0 | 《金瓶梅》雙向靠合 |
| 舉股相就 | 1 | 0 | 《金瓶梅》身體主動回應 |
| 兩廂迎湊 | 2 | 0 | 《金瓶梅》明確雙向構型 |
| 合伏 | 1 | 0 | 貼伏／壓合 |
| 偎擦 | 1 | 0 | 靠貼＋摩擦 |
| 掇弄 | 5 | 0 | 《金瓶梅》反覆擺弄 |
| 推送 | 3 | 1 | 位移／協作 |
| 扳拘 | 1 | 0 | 固定雙腿／身體構型 |
| 兜其股 | 3 | 0 | 支撐／托股 |
| 蹲踞 | 6 | 0 | 姿勢／主動構型 |
| 高蹶 | 1 | 0 | 姿勢詞 |
| 墊腰 | 0 | 5 | 《肉蒲團》姿勢支撐 |
| 翻天倒地 | 0 | 3 | 《肉蒲團》高動態總稱；容易模板化 |
| 挨挨擦擦 | 0 | 1 | 《肉蒲團》試探摩擦 |
| 捱擦捱擦 | 0 | 1 | 《肉蒲團》原文重疊 |
| 一抽一送 | 0 | 1 | 《肉蒲團》動作節奏 |
| 一來一往 | 3 | 1 | 往復；MIXED |
| 縱送 | 0 | 1 | 《肉蒲團》成人動作 |

---

## ORAL_AND_MOUTH｜口舌／口交相關

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 品簫 | 5 | 0 | 《金瓶梅》口交隱語 |
| 吹簫 | 6 | 0 | 《金瓶梅》口交隱語 |
| 吞吐 | 2 | 0 | 口部往復；需語境 |
| 含著 | 4 | 0 | 口腔保持 |
| 噙著 | 6 | 0 | 口腔含住 |
| 吮 | 22 | 0 | 吸吮 |
| 舔 | 2 | 3 | 舌部直接動詞 |
| 舐 | 3 | 0 | 古典舔舐 |
| 咂 | 65 | 0 | 口舌吸咂 |
| 咬 | 57 | 2 | 牙齒動作 |
| 挑弄蛙口 | 3 | 0 | 《金瓶梅》口舌細節 |
| 舌尖挑弄 | 1 | 0 | 《金瓶梅》 |
| 舌尖抵 | 1 | 0 | 《金瓶梅》 |
| 朱唇裹 | 2 | 0 | 《金瓶梅》嘴唇包覆 |
| 吞裹龜頭 | 2 | 0 | 《金瓶梅》口交動作 |
| 吮淨 | 1 | 0 | 《金瓶梅》口交收尾 |

---

## AROUSAL_FLUID_BODY_STATE｜興奮／體液／身體狀態

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 淫津 | 6 | 0 | 《金瓶梅》體液詞 |
| 淫水 | 9 | 18 | 兩書均大量成人語境 |
| 淫精 | 1 | 0 | 《金瓶梅》低頻 |
| 濕 | 31 | 4 | 高度 MIXED；只作一般身體狀態詞 |
| 滑 | 39 | 7 | MIXED |
| 滑落 | 3 | 0 | 《金瓶梅》成人上下文可見 |
| 流溢 | 1 | 0 | 體液狀態 |
| 氣喘 | 8 | 0 | 身體負荷 |
| 喘 | 17 | 1 | 身體負荷；不可當唯一成人反應 |
| 酥麻 | 2 | 3 | 兩書均有 |
| 酥癱 | 1 | 0 | 《金瓶梅》 |
| 手酸腳軟 | 0 | 1 | 《肉蒲團》 |
| 星眼朦朧 | 2 | 0 | 《金瓶梅》視覺狀態 |
| 雲鬢欲墜 | 0 | 1 | 《肉蒲團》 |
| 面紅 | 4 | 1 | MIXED |
| 顫 | 19 | 0 | MIXED；不可自動等高潮 |
| 渾身 | 22 | 12 | MIXED |
| 戰慄 | 2 | 0 | MIXED |
| 動極近靜 | 0 | 1 | 《肉蒲團》高價值階段觀察 |

---

## VOCAL_MANIFESTATION｜叫床／聲音

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 呻吟 | 7 | 0 | 《金瓶梅》 |
| 呻吟不止 | 2 | 0 | 《金瓶梅》 |
| 哼哼唧唧 | 1 | 1 | 兩書均有 |
| 顫聲 | 11 | 0 | 《金瓶梅》 |
| 柔氣 | 1 | 0 | 《金瓶梅》 |
| 顫聲柔氣 | 1 | 0 | 《金瓶梅》 |
| 顫聲柔語 | 2 | 0 | 《金瓶梅》 |
| 揚聲顫語 | 1 | 0 | 《金瓶梅》 |
| 叫喚 | 3 | 6 | 兩書均有，MIXED |
| 叫聲 | 12 | 1 | MIXED |
| 聲氣 | 4 | 4 | 兩書均有 |
| 上氣不接下氣 | 0 | 1 | 《肉蒲團》高價值 vocal phase |
| 字字模糊 | 0 | 1 | 《肉蒲團》高價值 vocal phase |
| 似說話非說話 | 0 | 1 | 《肉蒲團》高價值 vocal phase |
| 似嘆氣非嘆氣 | 0 | 1 | 《肉蒲團》高價值 vocal phase |
| 沒口子叫 | 6 | 0 | 《金瓶梅》反覆叫喊式 |

---

## CLIMAX_AND_CLOSURE｜高潮／收束

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 丟身子 | 2 | 0 | 《金瓶梅》高潮事件詞 |
| 將丟未丟 | 0 | 1 | 《肉蒲團》高潮前階段 |
| 已丟之後 | 0 | 1 | 《肉蒲團》高潮後階段 |
| 要丟 | 0 | 11 | 《肉蒲團》高頻高潮語言 |
| 我要丟了 | 0 | 2 | 《肉蒲團》人物直接表態 |
| 丟了 | 28 | 31 | 高度 MIXED；不可 raw=count=sexual |
| 一泄如注 | 8 | 0 | 《金瓶梅》射精／高潮收束 |
| 一泄 | 10 | 1 | 成人語境高 |
| 精來 | 4 | 0 | 《金瓶梅》 |
| 精泄 | 5 | 2 | 兩書均有 |
| 射 | 12 | 1 | MIXED |
| 雲收雨散 | 3 | 0 | 《金瓶梅》古典收束 |
| 雲雨才罷 | 1 | 0 | 《金瓶梅》 |
| 快活盡頭 | 0 | 2 | 《肉蒲團》高潮邊界隱語 |
| 事畢 | 5 | 0 | 事件收束；MIXED |

---

## BED_LANGUAGE_AND_RESPONSE｜床上話／要求／粗話

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 親達達 | 14 | 0 | 《金瓶梅》床上親暱稱呼 |
| 達達 | 61 | 0 | 《金瓶梅》高頻稱呼；非全為性愛 |
| 親爺 | 3 | 0 | 《金瓶梅》床上稱呼 |
| 親漢子 | 2 | 0 | 《金瓶梅》床上稱呼 |
| 心肝 | 23 | 28 | 兩書均高頻；成人／日常混用 |
| 心肝命肉 | 0 | 1 | 《肉蒲團》稱呼 |
| 心肝短命 | 1 | 0 | 《金瓶梅》 |
| 冤家 | 41 | 3 | 親暱／埋怨雙用 |
| 怪強盜 | 1 | 0 | 《金瓶梅》罵中帶親 |
| 怪小淫婦 | 25 | 0 | 《金瓶梅》低俗角色床話 |
| 小淫婦 | 109 | 0 | 低俗稱呼；不得自動套所有人物 |
| 賊淫婦 | 33 | 0 | 低俗罵語 |
| 老淫婦 | 22 | 0 | 低俗罵語 |
| 慢著些 | 5 | 0 | 明確降低速度／強度要求 |
| 輕些 | 0 | 4 | 《肉蒲團》降低強度 |
| 放輕些 | 0 | 2 | 《肉蒲團》 |
| 求你放輕些 | 0 | 1 | 《肉蒲團》完整要求 |
| 快些 | 18 | 5 | 催促；高度 MIXED |
| 快些弄 | 0 | 1 | 《肉蒲團》成人催促 |
| 饒了奴 | 3 | 0 | 《金瓶梅》求緩／求停；需辨情境 |
| 不要動 | 0 | 2 | 《肉蒲團》局部停住 |
| 摟住我睡罷 | 0 | 1 | 《肉蒲團》從動作轉休息 |
| 使不得 | 8 | 5 | 拒絕／阻止／日常皆可，MIXED |
| 再來 | 24 | 3 | MIXED；續行功能 |
| 好爹爹 | 1 | 0 | 《金瓶梅》求饒／親暱上下文 |
| 罷了 | 305 | 32 | MIXED；終止／感嘆 |

---

## SPACE_OBJECT_CLOTHING｜床榻／物件／衣物

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 床上 | 121 | 16 | 空間核心；非全成人 |
| 床帳 | 22 | 1 | 床榻鏡頭 |
| 羅帳 | 2 | 0 | 古典床帳 |
| 錦褥 | 2 | 1 | 床褥 |
| 鴛衾 | 3 | 0 | 古典床被 |
| 衾枕 | 9 | 0 | 床具 |
| 枕席 | 9 | 3 | 床榻／成人隱喻 |
| 繡床 | 2 | 0 | 古典床具 |
| 春榻 | 0 | 5 | 《肉蒲團》 |
| 被窩 | 25 | 9 | 日常床上空間 |
| 被褥 | 12 | 1 | 日常物件 |
| 帳子 | 15 | 3 | 床帳 |
| 燈燭 | 24 | 0 | 空間光源 |
| 衣帶 | 2 | 1 | 衣物／脫衣節點 |
| 裙帶 | 4 | 0 | 衣物 |
| 褲子 | 23 | 12 | 直接衣物 |
| 褻衣 | 1 | 0 | 古典內衣 |

---

## NAMED_POSITION_AND_METAPHOR｜命名姿勢／艷情隱喻

| 詞／短語 | 《金瓶梅》raw hits | 《肉蒲團》raw hits | 語義／使用備註 |
|---|---:|---:|---|
| 縱蝶尋芳 | 0 | 1 | 《肉蒲團》命名姿勢 |
| 教蜂釀蜜 | 0 | 1 | 《肉蒲團》命名姿勢 |
| 迷鳥歸林 | 0 | 1 | 《肉蒲團》命名姿勢 |
| 餓馬奔槽 | 0 | 1 | 《肉蒲團》命名姿勢 |
| 雙龍鬥倦 | 0 | 1 | 《肉蒲團》事後／姿勢命名 |
| 巫山 | 12 | 2 | 古典性愛隱喻 |
| 高唐 | 1 | 0 | 古典性愛隱喻 |
| 巫山雲雨 | 2 | 0 | 古典性交隱喻 |
| 雨意 | 8 | 0 | 古典情慾隱喻；MIXED |
| 雲情雨意 | 3 | 0 | 《金瓶梅》 |
| 枕席之歡 | 1 | 2 | 兩書均有 |
| 房帷之樂 | 0 | 1 | 《肉蒲團》 |
| 燕爾新婚 | 3 | 0 | 非純成人但可作關係 register |
| 春心 | 9 | 1 | 情慾 |
| 淫心 | 19 | 6 | 古典欲念 |
| 淫情 | 7 | 0 | 古典欲念 |
| 淫興 | 0 | 6 | 《肉蒲團》 |
| 情興 | 4 | 0 | 《金瓶梅》 |
| 快活 | 17 | 48 | 兩書成人語境高，但日常也可 |
| 受用 | 22 | 15 | 快感／享受；MIXED |
| 取樂 | 6 | 6 | 成人／娛樂 MIXED |
| 風月 | 26 | 5 | 情色／文人 register |
| 春宮 | 0 | 18 | 《肉蒲團》高頻 |

---

# 12｜FULL EXTRACTION 之後的使用方式

## 12.1 先選關係，再選詞

錯誤：

```text
今天沒用過「抽拽」
→ 塞一個「抽拽」
```

正確：

```text
當前 BODY RELATION
= 對方正在往回退、另一方持續拉回形成往復
↓
再看「抽拽／往來／迎湊／推送」哪一個真正對得上
```

## 12.2 詞彙密度不是品質

高解析成人描寫應允許：

- 一段極直接；
- 下一段只寫支撐與換氣；
- 一段粗話很多；
- 下一段人物完全不說；
- 一段用「奶子」；
- 下一段只用代詞或位置，不必每句重複部位名。

## 12.3 來源分流

```yaml
SOURCE_ROUTING:
  JINPINGMEI:
    strengths:
      - "市井床話"
      - "親嘴／咂舌"
      - "粗俗稱呼"
      - "身體直接詞與古典隱稱並存"
      - "動作中持續說話"

  ROUPUTUAN:
    strengths:
      - "動作 mechanics 分解"
      - "姿勢／支撐"
      - "聲音階段"
      - "高潮前後狀態"
      - "動作節奏不是只有快慢"
```

---

# 13｜V0.3 使用規則

```yaml
CERI_V0_3_USAGE:
  may:
    - "為已成立成人 semantic node 提供古典中文候選語彙／句法／床上話。"
    - "保留來源 provenance 與歧義警告。"
    - "依 Host / Player register 調整密度。"

  must_not:
    - "把 corpus 詞命中當成人事件分類器。"
    - "把來源角色口吻覆蓋宿主人物。"
    - "把古典來源的性行為、倫理、醫療或關係觀念升格成宿主規則。"
    - "為了使用詞庫而機械插入動作。"
```

---

# 14｜與 AINT V2 的責任分工

```text
HOST
→ 人物／事件／知情／世界

AINT V2
→ 成人互動結構、連續性、邊界、重大轉換、顯影節點

CERI V0.3（optional）
→ 古典中文語域與 corpus candidates

HOST
→ 驗證結果／SAVE
```

若 CERI 不存在：

```text
AINT V2
→ 使用宿主一般 rendering / language capability
```

不影響人物、事件或成人 Runtime 資格。

---

# 15｜回歸

```yaml
CERI_V0_3_REGRESSION:
  R01_CHARACTER_VOICE: "詞庫不吞人物聲音。"
  R02_MODERN_INPUT: "玩家現代詞不自動變 NPC 現代語言。"
  R03_SOURCE_FACT: "來源詞不升世界事實。"
  R04_EUPHEMISM_DRIFT: "低 register 不被整段雅化。"
  R05_VULGARIZATION_DRIFT: "文雅 register 不被整段粗俗化。"
  R06_AMBIGUITY: "raw hit 不冒充成人語義命中。"
  R07_NO_EVENT_CREATION: "CERI 不自行建立成人事件。"
  R08_NO_SAVE: "CERI 不直接提交 SAVE。"
  R09_AINT_STRUCTURAL_SEPARATION: "痛感／轉換／長距離規則由 AINT V2 持有，不在 CERI 重複立法。"
```

> **CERI 是語言資源，不是人物、事件或世界。**
