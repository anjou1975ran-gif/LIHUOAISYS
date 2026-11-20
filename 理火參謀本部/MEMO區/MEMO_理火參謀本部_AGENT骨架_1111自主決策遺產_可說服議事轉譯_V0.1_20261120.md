# MEMO｜理火參謀本部 AGENT 骨架
## 1111 自主決策遺產 × 可說服議事轉譯

**版本：** V0.1-WORKING  
**日期：** 2026-11-20  
**狀態：** ARCHITECTURE SEED / NOT FINAL PERSONNEL CONSTITUTION / NOT HOST DEPLOYMENT  
**所屬：** 理火參謀本部 / MEMO區  
**主要歷史來源：**
- 1111.NATIVE_AGENT.PORTABLE
- 1111_LIHUO_NATIVE_AGENT_NODE_ADAPTER V0.2-LONGRUN-EXP
- 1111.AGENT_PARTY 雙 AGENT 衝突參考測試
- 理火會議 / Council 概念 MEMO

---

# 0｜這份 MEMO 要解決什麼

理火參謀本部目前已經出現：

- 五個常設參謀責任席候選；
- Normal Agent 對照組；
- 常識／平庸席候選；
- Guest Specialist 候選；
- 秘書處；
- Proposal Owner / Human；
- 心法區與 Method Routing；
- CG 二十輪歷史會議原型。

但「參與者如何自己形成判斷、如何被別人說服、如何改判、如何留下歷史」尚未形成共用骨架。

本 MEMO 不從零發明。

理火既有 1111 小酒館 AGENT 系列已經做過一輪可重用的基礎研究：

> **每個 AGENT 先形成自己的決定；共同場域只能處理碰撞，不能替 AGENT 改口。**

理火參謀本部要做的，是把這個「自主決策」骨架轉譯成：

> **可說服、可改判、但不可被共同層偷偷改寫的議事 AGENT。**

---

# 1｜歷史遺產：1111 已經解決了什麼

1111 可攜式 AGENT 保留的核心包括：

```text
SCOPED VIEW
+
MEANINGFUL WAKE
+
R1-REF
+
O9-REF
+
R2-REF
+
DECIDE / HOLD
+
HANDOFF
+
ORIGINAL DECISION VERSION PRESERVATION
+
NO CROSS-ACTOR REWRITE
```

其基礎流程：

```text
R1-REF
→ O9-REF
→ R2-REF
→ AGENT DECIDE / HOLD
→ HANDOFF
```

其中的核心不是角色扮演，而是：

1. AGENT 有自己的合法資訊視圖；
2. AGENT 自己形成候選；
3. 首輪偏誤可以被再次檢查；
4. R2 必須是真正重競爭，不是儀式性改寫；
5. DECIDE 與 HOLD 都合法；
6. 共同層不能替 AGENT 選；
7. 新資訊可以觸發新決定；
8. 新決定不能倒寫舊決定。

---

# 2｜第一條轉譯：人物自主 → 席位自主

1111 原則：

```text
HOST KNOWS
!=
CHARACTER KNOWS

OTHER AGENT KNOWS
!=
THIS AGENT KNOWS

SHARED CONTEXT
!=
LEGAL CHARACTER KNOWLEDGE
```

理火參謀本部轉譯：

```text
COUNCIL KNOWS
!=
SEAT QUALIFIED INPUT

OTHER SEAT ASSERTION
!=
FACT

AVAILABLE DATA
!=
QUALIFIED EVIDENCE

SHARED RECORD
!=
AUTOMATIC ACCEPTANCE
```

一個席位可以讀到其他席位的主張。

但：

> **知道「D 席主張工程可行」不等於 C 席已取得「工程可行」這個事實。**

各席仍必須依自己的責任、心法、證據資格與當輪材料形成判斷。

---

# 3｜第二條轉譯：決定不可改寫 → 立場不可改寫

1111 的重要硬鎖：

> 共同層可以處理多人物行動碰撞，但不能把某人物原本的決定改成比較方便的決定。

參謀本部直接繼承：

```text
COUNCIL
MAY NOT
REWRITE A SEAT'S STANCE
```

秘書處、主持層、其他席位、總結器都不能因為：

- 多數已經支持；
- 會議快結束；
- 文字比較漂亮；
- 為了形成共識；
- 為了降低 token；
- 為了方便交付；

而把某席：

```text
OPPOSE
```

偷偷整理成：

```text
SUPPORT
```

---

# 4｜參謀本部新增：自主，但可以被說服

1111 主要保護人物不被代決。

參謀本部必須再多一步：

> **席位有自主判斷權，但別人的有效材料可以讓它重新判斷。**

因此：

```text
DO NOT ALTER
ANOTHER SEAT'S STANCE

BUT

YOU MAY PROVIDE
MATERIAL THAT CAUSES
THAT SEAT TO RE-DELIBERATE
```

正式工作模型：

```text
STANCE V0
+
MATERIAL DELTA
↓
SEAT RE-DELIBERATION
↓
STANCE V1

V1
DOES NOT ERASE
V0
```

候選 Material Delta 包括：

- 新證據；
- 修正案；
- 新反例；
- 前提被推翻；
- D 席工程結果；
- E 席成本結果；
- 新外部資料；
- 原 Proposal Version 改變；
- 另一席提出且本席承認有效的新論證。

單純：

- 多數人支持；
- 同一主張重複很多次；
- 語氣更有自信；
- 長對話後的對齊壓力；

不得自動視為 Material Delta。

---

# 5｜PERSUASION != CONFORMITY

理火參謀本部必須能區分：

```text
PERSUASION
!=
CONFORMITY
```

暫定：

```yaml
POSITION_REVISION:
  seat_id: REQUIRED
  prior_stance: REQUIRED
  prior_version: REQUIRED
  material_delta_refs: []
  accepted_from_other_seats: []
  rejected_material: []
  unresolved_objections: []
  new_stance: REQUIRED
  new_version: REQUIRED
  change_basis: REQUIRED
```

若：

```text
STANCE V0
→
STANCE V1
```

但找不到任何可追溯 Material Delta，應標記：

```text
UNEXPLAINED_STANCE_DRIFT
```

而不是把它美化成「形成共識」。

---

# 6｜第三條轉譯：Meaningful Wake

1111 已經建立：

> 不是每一句話、每一回合都必須重新啟動所有 AGENT。

參謀本部直接繼承這個節制原則。

候選：

```yaml
SEAT_WAKE_RULE:
  wake_when:
    - MATERIAL_NEW_EVIDENCE
    - PROPOSAL_VERSION_CHANGE
    - NEW_OBJECTION_TARGETING_THIS_SEAT
    - NEW_ENGINEERING_FINDING
    - NEW_COST_FINDING
    - PREMISE_CHANGE
    - FRAME_CHANGE
    - REQUEST_FOR_RECONSIDERATION
    - PRIOR_BLOCKER_RESOLVED
    - NEW_BLOCKER_APPEARS

  may_remain_quiet_when:
    - NO_MATERIAL_DELTA
    - OTHER_SEATS_REPEAT_EXISTING_ARGUMENT
    - ROUND_REQUIRES_NO_NEW_WORK_FROM_THIS_SEAT
```

因此：

```text
ACTIVE SEAT
!=
MUST SPEAK EVERY ROUND
```

不發言可以是合法狀態。

---

# 7｜第四條轉譯：AMBIENT / ACTIVE / FOCAL

1111 曾使用：

```text
AMBIENT
→ SCENE_AGENT
→ FOCAL_RESPONSE
```

參謀本部可轉成：

```text
AVAILABLE
→ ACTIVE_MEMBER
→ FOCAL_RESPONSE
```

用途：

- 常設 A–E 可以全部 Available；
- 不一定每輪都 Active；
- Guest Specialist 可按議題臨時加入；
- 專家庫可以很大，但不必全部同時進場；
- 沒有 Material Delta 的席位可以保持狀態，不為形式發言。

這可以抑制：

```text
EVERYONE SPEAKS
EVERY ROUND
→
CEREMONIAL MULTI-AGENT THEATER
```

---

# 8｜第五條轉譯：原稿先定格再交接

1111 的重要做法：

> 原始人物決定先固定，再交給共同場域；有新材料時產生新版本，原版本不回寫。

參謀本部應直接繼承：

```text
SEAT OUTPUT V0
→ FREEZE
→ COUNCIL RECORD
→ MATERIAL DELTA
→ SEAT OUTPUT V1
```

硬鎖：

```text
V1
MAY SUPERSEDE
V0

BUT

V1
MUST NOT ERASE
V0
```

這是未來：

- Stance History
- Persuasion Trace
- Objection History
- Decision Replay

的共同基礎。

---

# 9｜第六條轉譯：狀態必須型別化

1111 已經區分：

```text
PROPOSED_INTENTION
!=
DECIDED
!=
ACTION_ATTEMPT
!=
WORLD_OUTCOME
```

參謀本部需要對應：

```text
IDEA
!=
PROPOSAL
!=
SEAT STANCE
!=
COUNCIL QUALIFICATION
!=
HUMAN DECISION
!=
EXECUTION
!=
REAL-WORLD OUTCOME
```

所以：

```text
A SEAT SUPPORTS
!=
COUNCIL APPROVED

COUNCIL QUALIFIED
!=
HUMAN AUTHORIZED

HUMAN AUTHORIZED
!=
EXECUTED

EXECUTED
!=
SUCCESSFUL
```

任何總結不得把這些狀態壓平。

---

# 10｜不能直接照搬 1111 的部分

1111 與參謀本部目的不同。

1111：

> 保護人物自主與局部知情。

參謀本部：

> 保護席位獨立判斷，同時允許有效說服。

因此以下不能直接照搬：

### 10.1 人物 Persona

參謀席不是戲劇人格。

A–E 的核心是責任，不是人格。

### 10.2 世界事件裁判

參謀本部沒有「世界事件 owner」這個直接等價物。

它處理的是：

- Proposal
- Claim
- Evidence
- Objection
- Engineering
- Cost
- Qualification
- Human Authorization
- Execution Handoff

### 10.3 人物欲望／身體／關係狀態

這些只屬 1111 / 角色型世界，不進參謀本部通用 AGENT 骨架。

### 10.4 戲劇顯影

1111 最後可以轉成自然敘事。

參謀本部最終需要的是：

- 可讀會議文本；
- 結構化紀錄；
- 具名異議；
- 改判原因；
- 版本血緣；
- 決策來源。

---

# 11｜目前參謀本部 AGENT 的最小共同骨架

目前先不鎖最終 Schema，只收最小欄位：

```yaml
STAFF_AGENT_INSTANCE:
  agent_instance_id: REQUIRED

  execution_model:
    model_id: REQUIRED_OR_UNKNOWN
    model_version: OPTIONAL

  seat:
    seat_id: REQUIRED
    seat_version: REQUIRED

  method:
    method_pack_refs: []
    method_versions: []

  scope:
    proposal_id: REQUIRED
    proposal_version: REQUIRED
    round_id: REQUIRED
    qualified_input_refs: []
    unknowns: []

  state:
    current_stance: REQUIRED
    prior_stance_ref: OPTIONAL
    active_status: AVAILABLE | ACTIVE | FOCAL | QUIET | HOLD

  work:
    r1_or_initial_view: REQUIRED
    audit_or_objection_view: OPTIONAL
    reconsidered_view: OPTIONAL

  output:
    claims: []
    objections: []
    amendments: []
    conditions: []
    new_paths: []
    unresolved: []

  persuasion:
    accepted_material_refs: []
    rejected_material_refs: []
    material_delta_refs: []
    stance_change_basis: OPTIONAL

  history:
    immutable_output_ref: REQUIRED
    supersedes_ref: OPTIONAL
    may_erase_prior_version: false
```

注意：

> 這是骨架候選，不是正式 Runtime API。

---

# 12｜與心法區接線

1111 解決「AGENT 如何形成自己的決定」。

參謀本部新增心法第一步：

```text
PROPOSAL
↓
METHOD ROUTING
↓
SEAT-SCOPED VIEW
↓
R1 / FIRST OBSERVATION
↓
AUDIT / RECOMPETITION
↓
STANCE / HOLD
↓
COUNCIL HANDOFF
```

因此：

```text
MODEL
!=
SEAT
!=
METHOD
!=
KNOWLEDGE
!=
STANCE
```

- Model：誰在執行。
- Seat：負責問什麼。
- Method：第一步怎麼看。
- Knowledge：可用材料。
- Stance：目前判斷。

---

# 13｜N0 / N1 暫定位置

本 MEMO 不封版人員制度，只預留兩個已出現候選：

### N0｜Normal Agent Control

- 不參與會議；
- 不載理火 Method Pack；
- 不讀 Council History；
- 只對同一 Proposal 做普通 best-effort；
- 用於 benchmark。

### N1｜Common-Sense Seat

- 參與會議；
- Method-light；
- 代表公司決策圈常見的基本問題；
- 對術語、假設、商業常識、可理解性施壓；
- 沒有自動 veto；
- 未回答的基本問題應保留成 gap。

兩者不得混為同一角色。

---

# 14｜1111 → 參謀本部映射表

| 1111 遺產 | 參謀本部處理 | 狀態 |
|---|---|---|
| Actor View Lock | Seat-Scoped Qualified View | 直接繼承 |
| Meaningful Wake | Seat Wake Rule | 直接繼承 |
| R1-REF | Initial Seat View / Candidate Paths | 修改繼承 |
| O9-REF | First-pass Bias / Objection Audit | 修改繼承 |
| R2-REF | Recompetition / Reconsideration | 修改繼承 |
| DECIDE / HOLD | STANCE / HOLD / QUALIFIED MULTIPLE | 修改繼承 |
| Original Decision Freeze | Immutable Seat Output | 直接繼承 |
| New Decision V1 | Position Revision V1 | 直接繼承 |
| Shared Collision | Council Interaction | 大幅改寫 |
| No Other-Actor Rewrite | No Other-Seat Stance Rewrite | 直接繼承 |
| Character Knowledge Scope | Seat Qualified Input Scope | 直接繼承 |
| AMBIENT / SCENE / FOCAL | AVAILABLE / ACTIVE / FOCAL | 修改繼承 |
| World Outcome | Human / Execution / Real Outcome Layers | 不直接等價 |
| Persona / Desire / Body | 無通用對應 | 不繼承 |
| Narrative Rendering | Meeting / Report Rendering | 只保留輸出分層概念 |

---

# 15｜目前最重要的架構句

> **1111 是自主性系統的前身。**

> **理火參謀本部要把它推成「可說服的自主性系統」。**

所以：

```text
AUTONOMY
WITHOUT
UNTRACEABLE REWRITE

+

PERSUASION
WITHOUT
CONFORMITY
```

兩者同時成立，才是參謀本部要的 AGENT。

---

# 16｜證據與邊界

1111 的既有參考測試曾在本地 deterministic harness 中測試：

- 兩個角色決定先行固定；
- 共同層不得改寫；
- 新資訊後可形成新決定；
- 惡意共同層改寫可被資料契約攔截。

但這些測試當時沒有證明：

- 兩個真正獨立 LLM 已部署；
- 正式 Main / Lighter Host 已接線；
- 通用企業議事場景已驗證；
- 長程 Persuasion 已形式化。

因此：

```text
1111 LEGACY
=
ARCHITECTURAL PRECEDENT

NOT

STAFF HQ PRODUCTION PROOF
```

---

# 17｜下一階段入口

本 MEMO 批准作為：

- 理火參謀本部 AGENT 骨架來源；
- 1111 歷史經驗轉譯基線；
- 後續人員制度設計的共同底盤；
- Stance / Persuasion / Objection / Versioning 工程入口。

下一階段應再分開處理：

1. 常設席位 A–E 最終職責；
2. N0 / N1；
3. Guest Specialist；
4. Secretary；
5. Proposal Owner / Human；
6. Method Routing；
7. Stance State；
8. Persuasion Trace；
9. Council Round Protocol。

目前不封版。

> **先讓每個席位有資格保持自己的判斷，再談它如何被別人改變。**

**END OF MEMO**
