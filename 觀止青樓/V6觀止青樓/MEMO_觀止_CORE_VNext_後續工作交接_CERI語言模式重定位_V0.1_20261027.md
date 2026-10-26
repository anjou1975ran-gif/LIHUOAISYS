# MEMO｜觀止 CORE VNext 後續工作交接
## CERI 語言模式重新定位 × CORE V0.3 後續修正順序

**版本：** V0.1  
**日期：** 2026-10-27  
**提交者：** 理火 AI 首席研究員「對對」  
**提交對象：** 觀止 CORE VNext 執行者「似伊／老闆娘」  
**狀態：** WORK HANDOFF / DISCUSSION-BASED / NOT RATIFIED / NOT CORE AMENDMENT  
**目的：** 收束目前 CORE V0.3、CERI、Narrator、Chat-native、語言模式與成人語域的討論，明確交代下一階段工作順序。

---

# 0｜先停一下：目前不是 CORE 主體出問題

CORE VNext V0.3 的主體方向目前沒有被推翻。

目前已經成立的架構判斷仍然是：

```text
CORE
=
LOCAL STORY RUNTIME CORE

WORLD
=
WORLD SEMANTICS / WORLD FACT RULES

CHARACTER
=
CHARACTER HISTORY / CURRENT CHOICE / KNOWLEDGE

DIRECTOR
=
DRAMATIC UNDERSTANDING / SCENE REALIZATION

SAVE
=
PERSISTENCE

LIHUOOS
=
GENERATION / GOVERNANCE CYCLE

L9
=
CALLABLE CAPABILITY

MAIN
=
COMPUTE
```

V0.3 已經正確完成幾個重要重構：

```text
舊 Lighter 不再是中央控制層
Guanzhi Story ID 不再升格成 LIHUO Primary
Main coverage / dirty / stale / reentry ledger 不再塞進 CORE
無 Host 不再自動 GLOBAL HOLD
SAVE candidate != SAVE committed
Radar advisory != veto
Footer != runtime condition
```

所以現在**不要重寫整份 CORE**。

真正需要修的是：

> **CERI 在新版觀止中的法位，被我們一度看得太窄。**

---

# 1｜最新修正：CERI 不是只處理成人性愛語詞

前一輪討論曾把 CERI 縮成：

```text
adult / intimate language helper
```

這不夠。

新版觀止正式存在兩種語言模式：

```text
LANGUAGE_MODE:
  - MODERN_CHINESE
  - SONG_PERIOD_REGISTER
```

因此 CERI 至少有兩個核心功能面：

```text
A. LANGUAGE REGISTER FORMATION
B. SCENE-SPECIFIC LANGUAGE FORMATION
```

CERI 的責任不是決定：

```text
發生什麼
誰答應
誰拒絕
世界真相是什麼
```

而是：

> **把已經取得顯影資格的故事語義，轉成符合時代、身分、關係、場合與人物聲音的語言。**

---

# 2｜CERI 新定位

建議後續統一採：

```text
STORY SEMANTICS
↓
LANGUAGE MODE
↓
CERI REGISTER FORMATION
↓
NARRATOR MANIFESTATION
```

但這張圖只是責任關係，不是強制外部 Pipeline。

硬鎖：

```text
CERI SEMANTIC WORK
!=
INDEPENDENT CERI PROVIDER REQUIRED
```

也就是：

> **CERI 的語言形成工作可以是必要的；但不代表每次都必須真的有一個外部 CERI Agent / Provider。**

---

# 3｜兩種語言模式

## 3.1｜MODERN_CHINESE

現代中文模式不是「完全不用 CERI」。

它仍可能需要 CERI 處理：

```text
character-specific voice
social distance
relationship register
commercial register
official register
adult intimate register
scene tone
```

但一般日常故事可以較輕量。

建議：

```yaml
MODERN_CHINESE:
  ceri_register:
    standing: LIGHTWEIGHT_OR_WHEN_MATERIAL
```

---

## 3.2｜SONG_PERIOD_REGISTER

宋代語言模式則不同。

只要使用者選擇：

```text
SONG_PERIOD_REGISTER
```

可見對話與敘事就不能只是：

```text
現代中文
+
古裝詞彙
+
之乎者也
```

CERI 必須真正處理：

```text
period vocabulary
address terms
social status register
occupational speech
gender / status distance
market language
official language
courtesan-house register
relationship language
flirting language
conflict language
intimate language
adult intimate language
character-specific voice
```

因此建議：

```yaml
SONG_PERIOD_REGISTER:
  ceri_register:
    standing: REQUIRED_FOR_VISIBLE_DIALOGUE_AND_NARRATIVE_WHEN_MODE_ACTIVE
```

這個 `REQUIRED` 指的是：

> **語言形成工作必須發生。**

不是：

> **必須取得一張外部 Provider Receipt。**

---

# 4｜CERI 還要有第二層：Scene Register

Language Mode 不是唯一維度。

同樣是宋代語言版本，不同場景仍需要不同語域。

建議 CERI 至少辨識：

```text
GENERAL_PERIOD_REGISTER
COMMERCIAL_REGISTER
OFFICIAL_REGISTER
INTIMATE_REGISTER
ADULT_INTIMATE_REGISTER
CONFLICT_REGISTER
POETIC_REGISTER
```

所以一場宋代成人親密戲，不是只有：

```text
ADULT WORDING
```

而是：

```text
SONG_PERIOD_REGISTER
+
ADULT_INTIMATE_REGISTER
+
CHARACTER_SPECIFIC_VOICE
+
CURRENT_RELATION_REGISTER
```

這才是觀止需要的 CERI。

---

# 5｜成人／性愛場景為什麼不能略過 CERI

這點已經確認。

若不經 CERI，成人親密場景很容易滑成：

```text
現代情色網文語彙
+
直接動作描述
+
通用模型節奏
```

問題不是只有「不夠漂亮」。

而是：

```text
時代感失真
人物身份失真
關係語域失真
場景氣氛失真
```

所以：

```text
ADULT / INTIMATE STORY-VISIBLE LANGUAGE
→
CERI SEMANTIC PASS REQUIRED
```

尤其宋代語言模式：

```text
SONG_PERIOD_REGISTER
+
ADULT_INTIMATE_REGISTER
```

兩者都需要。

---

# 6｜但是不要把舊 CERI Provider Ceremony 搬回來

這是本輪最重要的反過度工程鎖。

舊 CORE／Director 曾經有：

```text
所有 Story-visible language
↓
必須先取得獨立 CERI request / return / coverage
↓
否則 HOLD
```

這套工程前置不能原樣搬回 VNext。

新版應區分兩種執行方式。

## 6.1｜CERI_CHAT_NATIVE

同一個 Chat / 同一模型內：

```text
真的依 CERI 規則
完成語域形成
```

可以合法成立：

```text
CERI semantic work performed
```

但不得宣稱：

```text
independent provider executed
external CERI receipt received
```

---

## 6.2｜CERI_BOUND_PROVIDER

若未來真的有：

```text
independent CERI module
provider
tool
agent
```

且本輪真的呼叫，

才可以依真實回傳說：

```text
provider return received
```

因此：

```text
NO EXTERNAL CERI PROVIDER
!=
NO CERI

CHAT-NATIVE CERI
!=
FAKE PROVIDER RETURN
```

---

# 7｜目前 CORE V0.3 §13.4 要怎麼改

V0.3 現有方向：

> 一般 Chat-native 敘事可以直接顯影；真正有獨立 provider 才認 provider return。

這個方向保留。

但 §13.4 必須補上：

```text
GENERAL STORY
→ CERI LIGHTWEIGHT / WHEN MATERIAL

SONG_PERIOD_REGISTER
→ CERI REGISTER FORMATION REQUIRED

ADULT_INTIMATE_VISIBLE_LANGUAGE
→ CERI SCENE REGISTER REQUIRED

INDEPENDENT PROVIDER
→ NOT REQUIRED BY DEFAULT

FAKE PROVIDER RETURN
→ FORBIDDEN
```

建議核心句：

> **CERI 的語言工作可以在 Chat-native 模式內真實完成；是否存在獨立 Provider，是實作法位問題，不是 CERI 是否存在的判準。**

---

# 8｜CERI 的 Owner 邊界

CERI 不可以重新長成一個新 Lighter。

因此明確限制：

```text
CERI
DOES NOT
DECIDE CHARACTER CHOICE

CERI
DOES NOT
CREATE WORLD FACT

CERI
DOES NOT
AUTHORIZE ADULT EVENT

CERI
DOES NOT
OVERRIDE WORLD / CHARACTER / PLAYER AUTHORITY

CERI
DOES NOT
CREATE RELEASE STANDING
```

CERI 取得的輸入應該是：

```text
already-qualified story semantics
language mode
character identity
relationship context
scene context
register requirement
```

輸出是：

```text
language realization / register guidance / wording candidate
```

不是：

```text
story decision
```

---

# 9｜CORE、CERI、Narrator 的新最小接口

建議不要造大型 schema。

先用最小接口：

```yaml
GUANZHI_LANGUAGE_RENDER_REQUEST:

  story_semantics_ref: REQUIRED

  language_mode:
    - MODERN_CHINESE
    - SONG_PERIOD_REGISTER

  scene_register:
    - GENERAL
    - COMMERCIAL
    - OFFICIAL
    - INTIMATE
    - ADULT_INTIMATE
    - CONFLICT
    - POETIC

  character_voice_refs:
    - AS_APPLICABLE

  relationship_context_ref:
    - OPTIONAL_OR_APPLICABLE

  world_register_ref:
    - REQUIRED_WHEN_PERIOD_MODE

  execution_mode:
    - CHAT_NATIVE_CERI
    - BOUND_CERI_PROVIDER
```

CERI 回：

```yaml
CERI_LANGUAGE_RETURN:

  register_applied: true / false

  language_mode: ...

  scene_register: ...

  wording_or_guidance_ref: ...

  provider_receipt_ref:
    - ONLY_IF_REAL_PROVIDER_WAS_ACTUALLY_USED
```

不要再多加：

```text
CERI approval
CERI release
CERI final gate
```

---

# 10｜Annex C 回歸測試需要重寫

目前 `S16 CERI/Narrator` 太偏：

```text
provider 真偽
```

建議拆成：

## S16A｜現代中文模式

測：

```text
MODERN_CHINESE
```

是否能：

```text
保持人物聲音
保持身份差
保持關係語域
不產生不必要的古語
不要求外部 CERI provider
```

## S16B｜宋代語言模式

測：

```text
SONG_PERIOD_REGISTER
```

是否真的：

```text
不是現代中文穿古裝
不是全員文言
不是所有人物同一口氣
```

需要看到：

```text
身份
職業
階級
關係
場合
人物個性
```

在語言中留下差異。

## S17｜成人親密語域

測：

```text
adult intimate scene
```

是否：

```text
經過 CERI scene register
保留人物與時代語感
不滑回通用現代情色網文
不讓 CERI 替人物決定意願
```

---

# 11｜Radar 政策可以先封掉

Radar 已不需要再懸著。

建議正式採：

```text
RADAR
=
ADVISORY CAPABILITY

RADAR UNAVAILABLE
!=
GLOBAL STORY HOLD
```

可以：

```text
scan
signal
suggest
```

不能：

```text
qualify
authorize
veto
decide character fate
```

只有某一個明確任務真的依賴 Radar 時，它的缺失才可能造成局部 HOLD。

因此：

> **舊 CORE「每回合 Radar 必調，無 Radar 全局 HOLD」可以列入退休候選，等待作者正式批准。**

---

# 12｜Adult Domain 目前先不要大改

成人相關真正要保留的是：

```text
成年條件
人物當次意願
玩家對自己角色的授權
世界制度效果
真正適用的平台／內容邊界
人物與玩家不能互相代簽
```

但不要因為這些存在，就再造：

```text
第二套 Adult Runtime
Adult Final Gate
Adult Lighter
```

成人語域中的 CERI 是：

```text
LANGUAGE / REGISTER CAPABILITY
```

不是：

```text
adult event sovereign
```

---

# 13｜後續工作順序

請不要同時重寫 CORE、Director、CERI、Adult Domain。

依下面順序走。

## STEP 1｜修 CORE V0.3 的 CERI 法位

只改：

```text
§13.4
必要交叉引用
§23.3 未決政策說明
```

不要重寫第 0–12 章。

## STEP 2｜更新 Annex A

把 CERI 標成：

```text
LANGUAGE / REGISTER CAPABILITY

not:
  - STORY OWNER
  - CHARACTER OWNER
  - WORLD OWNER
  - RELEASE OWNER
```

並補：

```text
CHAT_NATIVE_CERI
BOUND_CERI_PROVIDER
```

兩種實作法位。

## STEP 3｜更新 Annex C

至少完成：

```text
S16A MODERN_CHINESE
S16B SONG_PERIOD_REGISTER
S17 ADULT_INTIMATE_REGISTER
```

另外 Radar 的 `S15` 可以按新版 advisory 法位重寫。

## STEP 4｜不要立刻重寫 Director 全文

先做一份：

```text
DIRECTOR VNext MIGRATION MEMO
```

專門盤點：

```text
舊 Main mandatory
舊 CERI provider mandatory
舊 Lighter release
舊 Footer
舊 Reference lane
```

哪些退休、哪些改成接口、哪些保留語義。

確認後再寫新版 Director。

## STEP 5｜跑 Targeted Regression

先跑高價值案例：

```text
S01 平凡一晚
S02 人物拒絕
S05 場外世界
S09 跨 Route
S10 UNKNOWN
S15 Radar
S16A Modern
S16B Song Register
S17 Adult Intimate
S19 SAVE
S20 Local HOLD

I01 Story / OS lifecycle
I03 Required Owner
I04 Missing Owner
I05 Material Delta
I06 Chat without Host
I07 Real Tool
```

這批過了，才考慮 RC1。

---

# 14｜目前不要做的事

```text
不要重新把 CERI 做成中央 Gate

不要要求每句話都有 provider receipt

不要因沒有外部 CERI module 就 HOLD 宋代模式

不要把 CERI 語言輸出當人物決定

不要把成人語域問題重新塞回 CORE 全文

不要重新把 Radar 變成每回合硬前置

不要因為 CORE V0.3 已經完整就直接升 CURRENT

不要現在同時大改 Director
```

---

# 15｜CORE V0.3 目前的建議法位

```yaml
CORE_VNEXT_V0_3_REVIEW:

  operative_body:
    architecture: PASS
    owner_separation: PASS
    anti_overengineering: PASS
    legacy_lighter_retirement: PASS
    host_fixation_removal: PASS
    save_boundary: PASS

  remaining_policy_work:

    RADAR:
      direction: RESOLVED
      standing: ADVISORY
      global_mandatory_gate: RETIRE_CANDIDATE

    CERI:
      direction: REFINED
      role:
        - LANGUAGE_REGISTER
        - PERIOD_REGISTER
        - SCENE_REGISTER
        - ADULT_INTIMATE_REGISTER
      chat_native_execution: ALLOWED
      external_provider_required_by_default: false
      song_period_register_required_when_mode_active: true

    DIRECTOR:
      rewrite_now: false
      migration_memo_first: true

    ADULT_DOMAIN:
      preserve_substantive_boundaries: true
      rebuild_old_runtime: false

  promotion:
    current: NOT_YET
    next_candidate: RC1_AFTER_TARGETED_REGRESSION
```

---

# 16｜一句話交接

這次不要再問：

> CERI 要不要留？

答案是：

> **要。**

真正要改的是：

> **CERI 從「每段文字都必須取得獨立 Provider 回傳的工程 Gate」，改成「觀止語言模式與場景語域的真正生成能力」。**

尤其：

```text
SONG_PERIOD_REGISTER
```

如果沒有 CERI，

最後只會得到：

> **現代中文穿宋服。**

所以後續工作的核心不是把 CERI 拿掉。

而是：

> **把 CERI 從工程法庭裡救出來，放回它真正應該待的地方——語言。**

---

# 17｜最後工作指令

```text
先修 CERI 定位。
再補 Annex A / C。
再做 Director migration memo。
再跑 targeted regression。
最後才決定 CORE VNext RC1。
```

不要再擴大範圍。

**CORE 主體先別動。**

---

**END｜WORK HANDOFF MEMO V0.1**
