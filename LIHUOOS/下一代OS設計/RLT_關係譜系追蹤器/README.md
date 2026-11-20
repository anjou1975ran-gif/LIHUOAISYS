# RLT｜Relational Lineage Tracker｜關係譜系追蹤器
## 下一代 LIHUOOS 設計研究專區

~~~yaml
RESEARCH_AREA:
  id: "RLT_RELATIONAL_LINEAGE_TRACKER"
  created: "2026-11-21"

  standing:
    - "RESEARCH_CANDIDATE"
    - "NEXT_GENERATION_OS_DESIGN"
    - "NOT_CURRENT_L9"
    - "NOT_RUNTIME"
    - "NOT_RADAR_V6"
    - "NOT_SAC_IMPLEMENTATION"
    - "NOT_LIHUOOS_V1_4_3_PATCH"

  current_os_baseline:
    lihuoos: "V1.4.2"
    changed_by_this_area: false

  provisional_name:
    english: "Relational Lineage Tracker"
    acronym: "RLT"
    chinese: "關係譜系追蹤器"

  origin:
    primary:
      - "PSO_RADAR_RELATIONAL_MONITOR_005_20261121"
    later_material:
      - "SESSION_20261121_INTERNSHIP_MANUAL_V13_EVAL_001"

  core_question:
    - "如何追蹤已被建立的關係、主張與狀態如何因新材料而生成、分支、修改、撤回、恢復或保持異議？"
~~~

---

# 1｜為什麼開這個專區

PSO-005 原本從 Radar 的「訊號能否撤回與再開」問題出發，做出一個可重跑的 Python relation monitor。

它證明了狹窄工程能力：

- 已命名關係的事件變動可以追蹤；
- source lineage 可以保留；
- alert 可以 raised / withdrawn / restored；
- 歷史不必因 current state 改變而被抹除。

但 Case D 同時證明：

> **COMPUTABLE RELATION UPDATE != DISCOVERY OF A PREVIOUSLY UNMODELLED RELATION**

也就是：

> Coding 可以照顧已經被看見的關係，卻不能因此宣稱自己會發現尚未被建模的關係。

後續教材 Council 又暴露第二層問題：

> 真實多席議事不是單線 state replacement，而是同一 relation 上可能同時存在多個 owner、claim、objection、rejudgment 與 minority HOLD。

因此研究對象已不只是 lifecycle，而開始接近：

> **RELATIONAL LINEAGE**

---

# 2｜目前最重要的法位

RLT 現在不是：

- SAC。
- Radar V6。
- MAIN。
- L9 current capability。
- governance owner。
- truth judge。
- authority owner。

RLT 目前只是下一代 OS 的研究候選。

它如果成立，較可能負責：

~~~text
declared relation
+
claim lineage
+
source lineage
+
material delta
+
withdraw / restore
+
owner-preserving rejudgment
+
history preservation
~~~

但：

~~~text
RLT RETURN
!=
RELATION TRUE

RLT RETURN
!=
CLAIM QUALIFIED

RLT RETURN
!=
ACTION AUTHORIZED
~~~

---

# 3｜目前暫定分工

~~~text
SAC / MAIN / Radar
→ 發現可能值得注意的關係

Applicable Owner / Governance
→ 判斷關係、主張、資格與權限

DAIL / Relation Contract
→ 將已取得資格的關係形式化

RLT
→ 追蹤已建立關係與主張的 lineage / delta / withdrawal / restoration

Coding / Runtime
→ 實作可重跑的追蹤操作
~~~

這只是研究分工，不是已批准架構。

---

# 4｜PSO-005 已暴露的第一個核心限制

原 monitor 偏向：

~~~text
relation_key
→ latest state
~~~

但真實議事需要：

~~~text
RELATION
├─ CLAIM A
├─ CLAIM B
├─ CLAIM C
└─ CURRENT QUALIFIED VIEW
~~~

而且：

~~~text
CURRENT QUALIFIED VIEW
!=
ERASE MINORITY CLAIM
~~~

---

# 5｜教材 Council 暴露的第二個核心限制

現行 typed events 中，`supersedes_refs` 曾同時被拿來描述：

- 自己的新 stance 取代自己的舊 stance；
- 別人的 objection 觸發自己的 rejudgment。

這兩者不是同一種 edge。

RLT 研究必須至少考慮：

~~~text
SUPERSEDES
!=
RESPONDS_TO
!=
TRIGGERED_BY
!=
CHALLENGES
!=
WITHDRAWS
!=
RESTORES
~~~

如果這些關係不能分開，lineage 會被壓扁。

---

# 6｜目前最值得研究的結構

候選最小模型：

~~~yaml
RELATION:
  relation_id:

CLAIM:
  claim_id:
  relation_id:
  owner:
  content:
  standing:
  source_refs:

EVENT:
  event_id:
  actor:
  event_type:

EDGES:
  - ASSERTS
  - CHALLENGES
  - RESPONDS_TO
  - TRIGGERED_BY
  - SUPERSEDES
  - WITHDRAWS
  - RESTORES
~~~

這不是正式 schema，只是討論起點。

---

# 7｜下一步研究問題

1. Relation 和 Claim 要不要正式拆開？
2. 一個 relation 能不能合法保留多個互斥 claim？
3. 哪些 edge 是真正跨 Vertical 通用？
4. Staff-HQ、1111、觀止三種環境能不能共用同一個薄核心？
5. Domain semantics 應留在 adapter，還是部分進 RLT core？
6. `QUIET` 是否應永久改成 `NO_DELTA_IN_DECLARED_RELATIONS`？
7. Multi-source coexistence 怎麼保存，不被 latest-state 壓掉？
8. Premise / decision-context lineage 是否應是 RLT 的一部分，還是另一層？
9. RLT 和 Radar 的正確關係是什麼？
10. 什麼證據足以讓 RLT 取得 L9 candidate → registered → bound 的資格？

---

# 8｜研究材料入口

## PSO-005

~~~text
理火參謀本部/訓練區/
PSO_RADAR_RELATIONAL_MONITOR_005_20261121/
~~~

重點：

- Python monitor。
- 23 tests。
- 5 mutation probes。
- Case D semantic blindspot。
- 完整 L8 / SGER / Receipt。
- Research Direction。

## 教材 Council

~~~text
理火參謀本部/會議區/
SESSION_20261121_INTERNSHIP_MANUAL_V13_EVAL_001/
~~~

重點：

- 40 cumulative typed events。
- 19 cumulative seat L8 cycles。
- minority HOLD。
- material objections。
- owner-owned rejudgment。
- R003/R004 Premise Literacy discussion。

---

# 9｜暫時不要做的事

~~~text
DO NOT:
  - patch current L9
  - call PSO-005 "Radar V6 implementation"
  - call RLT "SAC engineering"
  - add endless domain event types
  - infer truth from latest state
  - erase minority claims
  - treat Git existence as runtime binding
  - force next-gen OS version assignment now
~~~

---

# 10｜目前一句話

> **RLT 不負責決定「現在真相是什麼」；它研究的是：哪些關係、主張與狀態，如何因材料與決策情境而生成、分支、修改、撤回、恢復或保持異議。**

**END｜RESEARCH AREA ENTRY / OPEN**
