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
