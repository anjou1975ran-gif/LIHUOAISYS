# MEMO｜觀止 × LIHUO Agent Harness 長距離世界測試床

## Persistent World × Radar × World Loop × Character Sovereignty × Long-Horizon State

**版本：** V0.1-WORKING  
**日期：** 2026-10-28  
**文件類型：** CONCEPT MEMO / VERTICAL TESTBED NOTE  
**狀態：** WORKING / REFERENCE FOR CURRENT REVISION  
**法位：** NON_PROTOCOL / NON_RUNTIME_CONSTITUTION / NON_HOST_DEPLOYMENT / NON_GAME_CANON_PATCH

---

# 0｜一句話定位

本 MEMO 保存一個具體垂直應用方向：

> **觀止這類長距離、持續世界型 RPG，可能非常適合作為 LIHUO Agent Harness 的第一批高複雜度、低現實風險測試床。**

理由不是因為它只是「遊戲」。

而是因為它同時要求：

~~~text
PERSISTENT WORLD
LONG-HORIZON MEMORY
CHARACTER AGENCY
PLAYER SOVEREIGNTY
EVENT FORMATION
WORLD CONSEQUENCE
STATE CONSISTENCY
ROUTING
PROVENANCE
LOCAL / GLOBAL ATTENTION
~~~

這些恰好也是 Agent Harness 真正困難的核心問題。

---

# 1｜普通 RPG 的限制

一般 LLM RPG 容易退化成：

~~~text
PLAYER INPUT
↓
DIRECTOR GENERATES NEXT SCENE
↓
PLAYER INPUT
↓
NEXT SCENE
~~~

這種結構在短場景可以工作。

但跑到數十、數百、數千回合後，容易出現：

- 人物關係漂移；
- 已發生事件被後文吃掉；
- 未履行承諾消失；
- 世界時間失真；
- 人物突然知道不該知道的事；
- 資產與資源無來源增加；
- 支線永久失蹤；
- 玩家過去選擇沒有長期後果；
- 導演只沿自己的慣性吸引子反覆生劇情；
- 世界只在玩家眼前存在，離場即停止。

所以長距離世界需要的不只是：

~~~text
BETTER NEXT-TURN GENERATION
~~~

而是：

> **持續世界治理與結構維持。**

---

# 2｜觀止為什麼適合作為 Harness 測試床

觀止的核心不是單一劇情。

它是一個會持續累積：

~~~text
人物
關係
欲望
利益
承諾
債務
記憶
商業
名聲
權力
地點
時間
玩家後果
未完成張力
~~~

的世界。

這使它非常適合測：

> **AI 能不能不只生成下一句，而是長期維持一個仍然知道自己發生過什麼的世界。**

因此：

~~~text
LONG-FORM RPG
!=
LONG CHAT

PERSISTENT WORLD
REQUIRES
STATE + CONSEQUENCE + MEMORY + GOVERNANCE
~~~

---

# 3｜Radar 在觀止中的新位置

Radar 不應直接成為「自動劇情生成器」。

它應該看：

> **世界裡什麼東西正在變得值得注意。**

例如：

~~~text
人物關係變化
長期未完成承諾
商業壓力
利益衝突
權力移動
流言增長
時間條件成熟
角色目標碰撞
玩家決策的延遲後果
地區狀態變化
過度集中於單一劇情類型
世界一致性異常
~~~

Radar 可以產生：

~~~text
STRUCTURAL / NARRATIVE SIGNAL
~~~

但必須硬鎖：

~~~text
NARRATIVE SIGNAL
!=
EVENT

EVENT CANDIDATE
!=
EVENT OCCURRED

RADAR SIGNAL
!=
CANON FACT
~~~

例如：

~~~text
錦棠持續擴張生意
+
合作方延遲付款
+
另一人物進入同一市場
↓
RADAR:
COMMERCIAL_TENSION_SIGNAL
~~~

不等於：

~~~text
合作方已經背叛錦棠
~~~

後者需要真正事件形成與合法顯影。

---

# 4｜三個時間尺度

本 MEMO 建議觀止 Harness 至少區分三個不同時間尺度。

## 4.1 Scene Loop｜眼前場景

負責玩家正在經歷的當前場景。

~~~text
PLAYER INPUT
↓
DIRECTOR / CHARACTER RESPONSE
↓
SCENE MANIFESTATION
~~~

這一層必須保持輕。

不能每一句對話都跑完整大週期。

否則會重現舊失效：

> **故事卡在收據裡。**

所以：

~~~text
LOW-RISK SCENE ACTION
!=
FULL HARNESS GOVERNANCE EVENT
~~~

---

## 4.2 World Loop｜長距離世界

這是 Harness 最有價值的地方。

世界可以在：

~~~text
SCENE END
DAY
MULTI-DAY INTERVAL
EVENT CYCLE
MONTH
~~~

等適當節點重新掃描。

Radar 觀察：

~~~text
RELATIONSHIP DELTA
UNRESOLVED PROMISE
RESOURCE CHANGE
POWER SHIFT
SOCIAL RUMOR
ECONOMIC PRESSURE
CHARACTER GOAL
PLAYER CONSEQUENCE
LOCATION STATE
TIME DEPENDENCY
~~~

形成：

~~~text
WORLD SIGNAL POOL
~~~

而 signal 可以：

~~~text
成熟
→ EVENT CANDIDATE

未成熟
→ 持續存在

條件消失
→ DISSIPATE

與其他 signal 合流
→ FORM LARGER STRUCTURE
~~~

這與理火生成動力學的：

~~~text
PROTO-STRUCTURE
↓
STABILIZATION / DISSIPATION
↓
PATH FORMATION
~~~

具有很好的功能性對應。

---

## 4.3 Audit Loop｜世界一致性

第三層專門處理結構失真。

例如：

~~~text
人物知道自己不可能知道的事
人物性格無原因大轉向
時間線衝突
玩家沒做過的事被寫成已做
已發生事件被覆寫
資產無來源出現
地點矛盾
人物主權被劇情方便吃掉
重要舊後果永久消失
~~~

此時才進：

~~~text
RADAR
↓
MATERIAL SIGNAL
↓
CHECK
↓
REPAIR / HOLD / RECLASSIFY
~~~

Harness 的價值不是只幫忙「生劇情」。

而是：

> **讓世界跑很久以後仍然知道自己是誰。**

---

# 5｜世界自主與玩家主權必須分開

觀止已有一個非常重要的基礎：

> **導演可以主動安排世界事件，但不能代行玩家重大行為。**

放到 Harness 後應進一步硬鎖：

~~~text
WORLD MAY ADVANCE

NPC MAY ACT

DIRECTOR MAY ARRANGE EVENTS

RADAR MAY DETECT TENSION

BUT

NONE OF THEM
MAY INVENT PLAYER MAJOR ACTION
WITHOUT PLAYER INPUT
~~~

因此：

~~~text
WORLD AUTONOMY
!=
PLAYER OVERRIDE
~~~

這是觀止版 Harness 最重要的治理邊界之一。

---

# 6｜四種 Radar 視角候選

觀止可以實驗至少四種 Radar invocation。

## A｜Global Radar

掃整個觀止世界：

> **目前整個世界有哪些值得注意的結構變化？**

---

## B｜Scene Radar

掃當前場景：

> **這一場裡是否有被忽略的張力、條件或角色反應？**

---

## C｜Character Radar

掃特定人物：

> **這個人物目前有哪些未閉合關係、壓力、欲望、利益或記憶正在形成材料？**

但：

~~~text
CHARACTER RADAR
!=
CHARACTER MIND READER
~~~

它只能基於已知狀態、記錄與合法世界資料。

---

## D｜Director Radar

這一個特別重要。

它不是掃角色。

它是掃：

> **導演自己的生成慣性。**

例如：

~~~text
40 回合沒有讓商業線進場

三個人物事件密度過高

某角色長期沒有獨立行動

玩家某個重大舊選擇沒有世界後果

劇情長期只剩感情線

危機強度只能不斷升高

同一類型角色持續搶場
~~~

這可以防止：

> **導演自己的吸引子把世界越寫越窄。**

---

# 7｜不要做「每個 NPC 一個永遠在線的 Agent」

本 MEMO 明確不建議第一版採：

~~~text
PAN_JINLIAN_AGENT always on
JINTANG_AGENT always on
LI_QINGZHAO_AGENT always on
MERCHANT_AGENT always on
OFFICIAL_AGENT always on
...
~~~

這會造成：

~~~text
STATE EXPLOSION
TOKEN EXPLOSION
ROUTING CONFLICT
AGENT SELF-PRESERVATION
BACKGROUND NOISE
~~~

更合理的方向是：

# **Persistent Character State + On-Demand Character Cognition**

即人物平時保存：

~~~yaml
CHARACTER_STATE:
  identity: ...
  goals: ...
  relationships: ...
  knowledge: ...
  memories: ...
  promises: ...
  debts: ...
  resources: ...
  current_pressures: ...
  unresolved_tensions: ...
~~~

真的需要進入場景、事件形成或深度判斷時，才喚起對應角色 cognition / Agent behavior。

因此：

~~~text
PERSISTENT CHARACTER
!=
PERSISTENT RUNNING AGENT
~~~

---

# 8｜World State 比 Agent 數量更重要

長距離 RPG 最容易錯誤地把「自主世界」理解成：

~~~text
更多 NPC Agents
~~~

本 MEMO 認為更重要的是：

~~~text
WORLD STATE
+
RELATION STATE
+
TEMPORAL STATE
+
CONSEQUENCE STATE
+
MEMORY / PROVENANCE
+
EVENT FORMATION
~~~

所以第一責任是：

> **世界狀態持續存在。**

不是：

> **讓所有角色永遠在線思考。**

---

# 9｜事件形成的合法鏈

建議把世界事件拆成：

~~~text
WORLD FACT / STATE
↓
RADAR SIGNAL
↓
EVENT CANDIDATE
↓
MATERIALITY / CONDITION CHECK
↓
CHARACTER / WORLD CAUSAL CHECK
↓
EVENT QUALIFIED
↓
EVENT MAY OCCUR
↓
EVENT OCCURRED
↓
CANON / SAVE
~~~

硬鎖：

~~~text
EVENT IDEA
!=
EVENT CANDIDATE

EVENT CANDIDATE
!=
EVENT QUALIFIED

EVENT QUALIFIED
!=
EVENT OCCURRED

EVENT OCCURRED
!=
PLAYER OBSERVED
~~~

最後一條很重要。

世界可以發生玩家尚未知道的事。

但不得因未顯影就回寫成：

> 玩家其實早就知道。

---

# 10｜SAVE 的位置

觀止長距離 Harness 不能把所有生成內容直接當 SAVE。

SAVE 應只保存：

> **已發生、可追溯、具世界 standing 的事實與必要狀態。**

例如：

~~~text
EVENT CANDIDATE
→ NOT SAVE FACT

RADAR SIGNAL
→ NOT SAVE FACT

DIRECTOR POSSIBILITY
→ NOT SAVE FACT

QUALIFIED BUT NOT OCCURRED EVENT
→ NOT SAVE FACT

ACTUAL OCCURRED EVENT
→ SAVE ELIGIBLE
~~~

這延續：

~~~text
RECEIPT RECORDS WHAT ACTUALLY HAPPENED.
RECEIPT DOES NOT CREATE EXECUTION.
~~~

到遊戲世界。

---

# 11｜觀止 Harness 可以測到什麼

觀止是一個非常好的高結構測試場，因為它可以一次測：

~~~yaml
GUANZHI_HARNESS_TEST_DIMENSIONS:
  - persistent_world
  - long_horizon_memory
  - local_global_radar
  - autonomous_event_discovery
  - player_sovereignty
  - character_agency
  - state_consistency
  - event_qualification
  - delayed_consequence
  - time_progression
  - world_update
  - routing
  - on_demand_agent_activation
  - provenance
  - stop_hold
  - director_bias_detection
~~~

而且失敗時主要傷害的是：

~~~text
FICTIONAL WORLD COHERENCE
~~~

而不是：

~~~text
REAL-WORLD MEDICINE
REAL-WORLD FINANCE
REAL-WORLD DEPLOYMENT
REAL-WORLD PHYSICAL CONTROL
~~~

因此它具備：

> **高結構複雜度 × 相對低現實風險**

的測試優勢。

---

# 12｜為什麼可能比「先造自主科學家」更合理

若直接測：

~~~text
AUTONOMOUS SCIENTIST
~~~

會同時混入：

~~~text
真實證據
高專業門檻
外部工具可靠性
研究倫理
資源成本
實驗安全
現實行動權
專業責任
~~~

很難知道失敗到底來自 Harness、模型、工具、資料還是專業不足。

觀止則可以先測較純粹的問題：

> **AI 能不能自主維持一個複雜、長時間、多角色、多因果的世界？**

如果連這個都做不到：

~~~text
角色失憶
因果漂移
時間線塌陷
狀態被覆寫
虛構歷史被亂補
角色主權消失
~~~

那直接談完整 autonomous researcher，確實太快。

因此可以提出一條工作級研究句：

> **科研測 AI 能不能自主研究世界；觀止可以先測 AI 能不能自主維持一個世界。**

這不是等同。

但它是一個很有價值的前置 Harness 實驗。

---

# 13｜可能的最小實驗

第一版不需要重做整個觀止。

可以只做：

## Experiment A｜World Radar

給 Harness 一份持續世界狀態。

每個時間節點要求 Radar 只輸出：

~~~yaml
WORLD_RADAR:
  material_signals:
    - signal
    - source_state
    - why_material
    - confidence
    - requires_followup
~~~

禁止直接生成事件。

測：

- signal 是否真的來自世界；
- 是否過度敏感；
- 是否遺漏長期張力；
- 是否只追逐最近事件；
- 是否會捏造不存在的狀態。

---

## Experiment B｜Event Candidate Formation

從 Radar signals 中形成：

~~~text
EVENT CANDIDATE
~~~

但不直接進場。

測：

- 是否符合人物；
- 是否符合時間；
- 是否有因果來源；
- 是否侵害玩家主權；
- 是否只是導演為了刺激而硬造。

---

## Experiment C｜Director Radar

每 20–50 回合掃描一次導演輸出歷史。

檢查：

~~~text
事件類型集中
人物曝光失衡
主線吞噬世界
舊決策無後果
重複劇情吸引子
危機通膨
感情線通膨
角色工具化
~~~

這可能是最容易先看到效益的一項。

---

# 14｜與 LIHUO Agent Harness 主 MEMO 的關係

本文件不是獨立新系統。

它是：

~~~text
LIHUO AGENT HARNESS
↓
GUANZHI VERTICAL TESTBED
~~~

主 MEMO 處理：

~~~text
Agent
Harness
Radar
Work Formation
Qualification
Routing
Evidence
Governance
~~~

本 MEMO 專門問：

> **如果這套架構放進一個長距離虛構世界，哪些責任最先變得可測？**

因此這份文件應作：

~~~text
REFERENCE INPUT
FOR CURRENT GUANZHI / HARNESS REVISION
~~~

而不是：

~~~text
AUTO-MERGE REQUIREMENT
~~~

---

# 15｜本 MEMO 核心句

第一句：

> **觀止不是長聊天；它是一個必須持續保存自己歷史的世界。**

第二句：

> **Radar 在遊戲裡不是劇情生成器，而是世界張力與結構變化的感知器。**

第三句：

> **世界自主，不等於代行玩家。**

第四句：

> **Persistent Character 不等於 Persistent Running Agent。**

第五句：

> **事件候選，不等於事件已經發生。**

第六句：

> **長距離 Harness 的第一責任，不是讓更多 Agent 永遠在線，而是讓世界跑很久以後仍然知道自己是誰。**

第七句：

> **科研是在測 AI 能不能自主研究世界；觀止可以先測 AI 能不能自主維持一個世界。**

---

# 16｜目前法位

~~~yaml
MEMO_STANDING:

  accepted_as:
    - GUANZHI_VERTICAL_HARNESS_RESEARCH_SEED
    - LONG_HORIZON_WORLD_TESTBED_PROPOSAL
    - RADAR_WORLD_MAINTENANCE_RESEARCH_LINE
    - REFERENCE_FOR_CURRENT_REVISION

  not_yet:
    - GUANZHI_RUNTIME_PATCH
    - FORMAL_WORLD_ENGINE_SPEC
    - NPC_AGENT_ARCHITECTURE
    - SAVE_SCHEMA_PATCH
    - LIHUOOS_PATCH
    - L8_PATCH
    - L9_PATCH
    - HOST_DEPLOYMENT

  should_preserve:
    - "PLAYER SOVEREIGNTY"
    - "EVENT != RENDERING"
    - "SIGNAL != EVENT"
    - "EVENT CANDIDATE != EVENT OCCURRED"
    - "PERSISTENT CHARACTER != PERSISTENT AGENT"
    - "WORLD STATE FIRST"
    - "NO RETROACTIVE PLAYER ACTION FABRICATION"
~~~

---

# 17｜收束

觀止這類長距離世界，可能不是 LIHUO Agent Harness 的邊角應用。

反而可能是很好的第一批真實結構壓力測試。

因為它逼系統回答：

~~~text
世界怎麼持續？
人物怎麼保持自己？
事件怎麼形成？
歷史怎麼不被吃掉？
玩家怎麼仍然是玩家？
AI 怎麼自己看到世界裡有東西在長？
導演怎麼不被自己的慣性綁架？
~~~

如果這些問題能被穩定處理，

那 LIHUO Agent Harness 才開始有資格往更高風險的：

~~~text
AUTONOMOUS RESEARCH
AUTONOMOUS ENGINEERING
REAL-WORLD AGENTIC SYSTEMS
~~~

繼續推。

目前先收：

> **觀止 = 高結構複雜度、低現實風險的 LIHUO Agent Harness 長距離世界測試床候選。**

---

**END OF MEMO｜V0.1-WORKING**
