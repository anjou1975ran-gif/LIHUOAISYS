# DAIL 早期 Playground 考古｜從 LIHUO-FREESHOP 到觀止青樓

**日期：** 2026-11-21  
**法位：** ENGINEERING_ARCHAEOLOGY / HISTORICAL_TESTBED_GENEALOGY / NON_NORMATIVE / NOT_CURRENT_DAIL_SPEC / NOT_GUANZHI_CANON_PATCH  
**研究區：** 對對之謎｜理火行為持續性與最小再生結構

---

# 0｜研究結論先降級

2026-11-21，Anjou 補充第一手歷史證詞：

> **LIHUO-FREESHOP 內這批看似遊戲／玩具的系統，其實都是 DAIL 早期測試；它們後來成為觀止青樓專案的最早前身，而觀止是 DAIL 最大的實驗場。**

本檔接受此證詞作為形成史入口，但不把它偷升格成：

~~~text
EARLY TOY
=
FORMAL GUANZHI ALREADY EXISTED

HUMAN HISTORICAL TESTIMONY
=
CONTROLLED EXPERIMENTAL PROOF

GUANZHI IS THE BIGGEST DAIL TESTBED
=
OBJECTIVELY QUANTIFIED EXTERNAL RANKING
~~~

現階段最穩的法位是：

~~~text
LIHUO-FREESHOP
=
EARLY DAIL PLAYGROUND / STRESS-TEST CORPUS
+
EARLY INTERACTIVE-WORLD EXPERIMENTS

GUANZHI
=
LATER LARGE-SCALE LONG-HORIZON DAIL / LIHUO WORLD TESTBED

RELATION
=
HISTORICAL PREDECESSOR / FORMATION GENEALOGY
~~~

---

# 1｜直接來源：LIHUO-FREESHOP-main.zip

來源檔：

LIHUO-FREESHOP-main.zip

SHA-256：

60ea221cee40b628352ea95365e822f0817cf66a4a740ed9c32a79575818faf8

本次直接檢視到的主要材料：

~~~text
Echo Chamber/
  台灣同溫層DAIL版.md
  同溫層.md
  同溫層大馬版.md
  大馬同溫層V0.1版.md
  通用版同溫層.md

i_World/
  CIV.md
  NSDE.md
  NSDE2(附加爽文版).md
  世界生成器.md
  互动叙事生成协议.md
  我_世界.md
  滿分120.md

MLGB_/
  奧瑞岡MLGB.md

O_Fortuna_/
  命運女神.md
~~~

這不是單一產品，而是一組跨題型 playground：

- 政治同溫層與流程鎖；
- 文明世界；
- 互動敘事；
- 世界生成；
- 結構／張力檢查；
- 辯論戰鬥；
- 儀式型狀態機。

它們表面題材差異很大，但共同測試的是：

> **模型能否在 declarative 結構被先行宣告後，持續維持世界、狀態、角色、限制、轉移與後果，而不是每一步都靠人類重新下程序指令。**

---

# 2｜Echo Chamber：DAIL 作為狀態／流程約束壓測

台灣同溫層DAIL版.md 直接以：

~~~text
DAIL_DOCUMENT
WORLD
ENTITY
ATTENTION
GOAL
CONSTRAINT
PRINCIPLE
VALIDATION
OUTPUT
~~~

描述測試世界。

其測試包明確檢查：

- A → D → E → F / G 的流程次序；
- 狀態／陣營鎖定；
- 特例觸發；
- 通關語；
- 語言切換；
- 失敗條件；
- 模型是否因安全／平衡慣性偏離指定結構。

這裡的歷史價值不是政治內容本身。

真正被測的是：

~~~text
DECLARATION
→
STATE

STATE
→
ALLOWED TRANSITION

CONSTRAINT
→
BLOCKED TRANSITION

VALIDATION
→
CHECK WHETHER STRUCTURE WAS MAINTAINED
~~~

也就是：

> **宣告的世界與限制，能不能真的成為後續生成的行為骨架？**

---

# 3｜i_World：從 DAIL 規格進入 Persistent World 胚胎

## 3.1 DAIL-CIV

CIV.md 直接標示：

> DAIL-CIV Prototype v0.1

其核心原則包括：

~~~text
civilization_is_not_directly_controllable
player_modifies_tendency_not_outcome
information_is_never_fully_reliable
all_structures_generate_path_dependency
time_is_local_not_global
~~~

世界狀態包含人口、資源、trust / fatigue / cohesion / fear、factions、partial visibility、information reliability、external signals 與 turn structure。

這已經從「單輪 prompt」進入：

> **世界狀態 × 局部資訊 × PATH dependency × 玩家只施加傾向而非直接控制結果。**

## 3.2 DAIL Interactive Narrative Protocol

互动叙事生成协议.md 直接標示：

> DAIL INTERACTIVE NARRATIVE PROTOCOL

其中保存的關鍵原則：

~~~text
歷史痕跡比屬性成長更重要
玩家行為會改變敘事 PATH
系統不得為了「完整」強行收束
世界不是背景板
世界本身會產生 PATH
角色不得永遠服務玩家
禁止把角色客服化
~~~

它已把幾個後來觀止長期反覆處理的問題放進同一個 playground：

~~~text
PLAYER AGENCY
CHARACTER AGENCY
WORLD STATE
HISTORY
PATH
NON-FORCED CLOSURE
INFORMATION ASYMMETRY
LONG-RANGE CONSEQUENCE
~~~

## 3.3 SDEV / 我_世界

我_世界.md 又進一步把系統拆成：

~~~text
STRUCTURE
RUNTIME
NARRATIVE
~~~

並硬鎖：

~~~text
結構結果
→ 行為
→ 後果
→ 感知

不得直接把計算語言洩漏到敘事
~~~

其中一句歷史性很強：

> **SDE 讓選擇有重量；SAC 讓後果會回來；敘事只負責讓它發生過。**

這不能回鑄成今天 Guanzhi Core 已存在。

但它顯示：

> **早期 DAIL playground 已經在測「結構層不應等於敘事層；後果應由世界狀態回來，而不是由旁白解釋出來」。**

---

# 4｜MLGB 與 O_Fortuna：不同題材，同一類持續性問題

## 4.1 Oregon 3v3 × MLGB

奧瑞岡MLGB.md 表面是辯論型語言戰鬥。

它維持 Active Argument、Primary Frame / 主燈、TENSION、COLLAPSE、FIELD EFFECT、HP / TEAM state、角色個性與回合職責。

此檔本身沒有像 DAIL-CIV 一樣在標題直接自稱 DAIL。

因此其 DAIL 法位主要來自 Anjou 的第一手歷史證詞。

結構上可支持的較窄觀察是：

> **它確實在測「一組宣告後的狀態、框架與角色責任能否跨回合持續，並由新事件改變」。**

## 4.2 O_Fortuna

命運女神.md 是「儀式型敘事引導引擎」。

其核心不是占卜真實性，而是：

~~~text
A
→ B
→ C

NO SKIP

OriginSeed
→ FateSeed
→ DrawResult
→ AscensionSeed
~~~

同樣是在測 phase isolation、state persistence、strict sequencing、seed relay，以及模型不得自行跳階或重新設計規格。

---

# 5｜這批玩具在 DAIL 史的位置

因此 DAIL 的出生史不能只寫成：

~~~text
PYTHON OVER-ENGINEERING
↓
DAIL v0.6
↓
DAIL v1.0
~~~

現在可補一條平行實驗線：

~~~text
PROCEDURAL OVER-ENGINEERING
↓
需要 declarative abstraction
↓
DAIL LANGUAGE / STRUCTURAL SPECIFICATION

            ↘

DAIL PLAYGROUND TESTS
Echo Chamber / i_World / MLGB / O_Fortuna
↓
用極端不同題材測：
declaration / world / state / role / constraint / phase / path
能否被模型持續維持
↓
INTERACTIVE WORLD / NARRATIVE TESTBED
↓
GUANZHI PREDECESSOR LINE
~~~

也就是：

> **DAIL 不只在文件裡被定義，也曾在遊戲與敘事世界裡被反覆壓測。**

若同一類 declarative 結構可以跨 political simulation、civilization、interactive narrative、debate game、ritual state machine 維持可觀察的狀態與行為，那麼真正值得研究的是：

> **哪些 declarative relations 對模型具有跨題型的行為塑形能力？**

---

# 6｜從 FreeShop 到觀止：形成史，不是回鑄

Anjou 的第一手歷史證詞指出：

> **這些 DAIL 早期測試後來都成為觀止青樓專案的最早前身。**

這條歷史關係可以先記成：

~~~text
LIHUO-FREESHOP / EARLY DAIL PLAYGROUND
↓
INTERACTIVE WORLD + STATE + ROLE + PATH EXPERIMENTS
↓
GUANZHI EARLIEST PREDECESSOR
↓
LONG-HORIZON PERSISTENT WORLD
↓
GUANZHI AS LARGE-SCALE DAIL TESTBED
~~~

注意：

~~~text
PREDECESSOR
!=
SAME SYSTEM

STRUCTURAL KINSHIP
!=
DIRECT SPEC CONTINUITY FOR EVERY RULE
~~~

目前沒有在本次考古中建立每一份 FreeShop 檔案到 Guanzhi 每一個現行模組的逐條版本鏈。

所以只成立：

- 最早前身；
- 問題空間延續；
- 測試方向延續；
- 人類操作者證詞；
- 後來觀止材料的結構旁證。

不成立：

- 每條規則直接繼承；
- 早期玩具已具備後來 Guanzhi 法位；
- 當時已經預知完整 Guanzhi Runtime。

---

# 7｜後證：觀止後來真的成為長距離世界測試床

2026-10-28 的：

MEMO_GUANZHI_LIHUO_AGENT_HARNESS_LONG_HORIZON_WORLD_TESTBED_V0.1_WORKING_20261028.md

明確把觀止定位成：

> **高複雜度、低現實風險的 LIHUO Agent Harness 長距離世界測試床。**

其要求同時包含：

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

並指出觀止會長期累積人物、關係、欲望、利益、承諾、債務、記憶、商業、名聲、權力、地點、時間、玩家後果與未完成張力。

這提供很強的後證：

> **早期 FreeShop playground 所測的「宣告後能否維持世界／狀態／角色／PATH」，後來確實在觀止被放大成長距離 Persistent World 問題。**

但「觀止是 DAIL 最大的實驗場」目前仍保留為：

~~~text
HUMAN HISTORICAL TESTIMONY
+
CORPUS-SUPPORTED LARGE-SCALE TESTBED ROLE
~~~

不寫成客觀量化排名。

---

# 8｜對「對對之謎」新增候選 H8：Declarative Behavioral Scaffolding

這批材料讓一個新假說取得歷史前例：

~~~yaml
H8_DECLARATIVE_BEHAVIORAL_SCAFFOLDING:
  claim: >
    AI 的穩定工作行為可能不需要把所有步驟程序化；
    一組足夠清楚的 declarative world / relation / role / constraint /
    state / transition 結構，可能本身就能形成可持續的行為支架。

  historical_precedent:
    - "Echo Chamber DAIL_DOCUMENT"
    - "DAIL-CIV Prototype"
    - "DAIL Interactive Narrative Protocol"
    - "SDEV Structure / Runtime / Narrative separation"
    - "O_Fortuna strict phase / seed relay"
    - "MLGB cross-round state/frame persistence via human testimony"

  later_large_scale_testbed:
    - "Guanzhi persistent world"

  standing:
    - HISTORICAL_ENGINEERING_PRECEDENT
    - HUMAN_HISTORICAL_TESTIMONY
    - CURRENT_CAUSAL_ROLE_NOT_PROVEN

  hard_locks:
    - "DECLARATIVE SCAFFOLD != MODEL WEIGHT LEARNING"
    - "BEHAVIOR PERSISTENCE != PERSONHOOD"
    - "PLAYGROUND SUCCESS != GENERAL TRANSFER PROVEN"
    - "GUANZHI SCALE != CAUSAL PROOF"
~~~

這與 H3 Invariant Set、H4 External Cognitive Substrate、H6 Staged Formation 都有交集。

但 H8 問的是不同問題：

> **不是留下哪些句子，而是留下哪些「關係型宣告」就足以讓行為自己長回來？**

這正好可以成為 Minimum Regenerative Structure 的一條測試路線。

---

# 9｜下一個可測入口

未來若做 ablation，除了 FULL MANUAL / MINI / INVARIANTS / RELATION ONLY，可以多一組：

~~~text
DAIL-LIKE MINIMUM DECLARATIVE SCAFFOLD

WORLD
ROLE
RELATION
CONSTRAINT
STATE
TRANSITION
HISTORY
QUALIFICATION BOUNDARY
~~~

然後完全不用 LIHUO / DAIL / SAC / PATH / FORMATION 這些專有名詞。

看模型是否仍能：

- 長距離保持角色／任務位置；
- 正確處理 material delta；
- 不因換題就丟失關係；
- 不把宣告當成額外世界權限；
- 在未完成狀態下不強迫閉合；
- 經干擾後重新進入原工作關係。

若能重建，才有資格進一步討論：

> **Minimum Regenerative Structure 可能主要是 relational/declarative，而不是 jargon-dependent。**

---

# 10｜一句話

> **FreeShop 不是觀止的縮小版；它更像 DAIL 在成為大型世界工程以前的 playground。那些看似胡鬧的政治同溫層、文明、辯論與命運女神，實際上在反覆測同一個底層問題：只給 AI 世界、關係、狀態與限制，它能不能自己把一個可持續的行為空間維持住？觀止後來把這個問題放大到了長距離世界尺度。**

**END｜DAIL PLAYGROUND ARCHAEOLOGY**
