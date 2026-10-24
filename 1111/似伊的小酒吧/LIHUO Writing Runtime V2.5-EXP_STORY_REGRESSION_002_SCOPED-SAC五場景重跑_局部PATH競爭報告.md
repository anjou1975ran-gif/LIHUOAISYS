# LIHUO Writing Runtime V2.5-EXP
## STORY REGRESSION 002｜SCOPED SAC 五場景重跑 × 局部 PATH 競爭報告

```yaml
REPORT:
  id: "LWR-V2.5-STORY-REGRESSION-002"
  date: "2026-08-27"
  target: "LIHUO Writing Runtime V2.5-EXP"
  method: "MODEL-EXECUTED FUNCTIONAL SAC RECONSTRUCTION / DOCUMENT-BEHAVIORAL REGRESSION"
  actual_host_sac_execution_observed: false
  hidden_state_claim: false
  medical_validation_claim: false
  historical_population_claim: false
```

本輪目的不是證明「上次問題一定是因為沒有 SAC」。

本輪只測一件事：

> **若把 V2.4 中需要大量 ECL/BFG 規則處理的多關係場，改接成 scoped SAC + local PATH recompetition，是否能用更乾淨的結構得到同等或更好的故事因果。**

測試仍使用上一輪人物，保持 fixture 可比較。

---

# CASE A｜北宋中期｜沈青蘿｜單純濕階｜控制組

## Input

```yaml
BODY:
  footbinding: "UNKNOWN"
  fatigue: "LOW"

ENVIRONMENT:
  wet_stone_steps: true
  handrail: true
  long_skirt: true

GOAL:
  "趕在寺門落閂前送藥"
```

## Escalation Gate

```text
主要關係：
濕階 × 速度 × 裙擺 × 扶手

沒有明顯多 PATH 重競爭需求。
```

```yaml
ESCALATION:
  result: "ECL_CORE_SUFFICIENT"
  scoped_sac_called: false
```

## Result

```text
ECL Core：濕滑提高快速下階成本
BFG：FEASIBLE_WITH_COST
Character：一手提裙、一手搭欄，濕階收步，平處加快
```

### Finding A

**V2.5 沒有因為「有 SAC 可用」就濫叫 SAC。**

這是必要控制組。

---

# CASE B｜晚清｜葉含煙｜纏足＋疲勞＋鞋濕＋樓梯＋急件

## Input

```yaml
BODY_HISTORY:
  footbinding: "PRESENT / CANON_ESTABLISHED"

CURRENT_BODY:
  fatigue: "MEDIUM_HIGH"
  local_foot_soreness: "PRESENT"
  left_shoe: "DAMP"

ENVIRONMENT:
  wooden_stairs: "DAMP"
  handrail: "AVAILABLE"

GOAL:
  "本人把帳冊送到後院"
```

## Candidate paths before SAC

```text
P1：帳冊拿在手上快速下樓
P2：帳冊塞入腰間，空手抓扶手下樓
P3：把帳冊交給別人送
P4：等樓梯乾／等人群散去
```

## Escalation Gate

```yaml
ESCALATION:
  result: "SCOPED_SAC_RECOMMENDED"
  reason:
    - "疲勞、鞋濕、樓梯、速度、手部占用互相影響"
    - "多條 PATH 的結構排序會因是否空出手／是否保留本人送件而改變"
```

## Functional SAC reconstruction

```yaml
SAC_SCOPE:
  D:
    "保持『本人送帳』方向不變。"

  T:
    - "P1：鞋濕 × 濕梯 × 快速 × 手持帳冊 → instability high"
    - "P4：身體穩定但違反時間壓力"
    - "P3：身體成本最低，但改變人物當前『本人送』行動方向"

  A:
    - "P2 因空出支撐手而取得局部結構優勢"
    - "P3 對純身體成本有優勢，但不取得人物選擇權"

  R:
    - "P2 可在保留人物目標的同時形成穩定局部閉合"
```

## Return → ECL → BFG

```text
SAC return:
P1 ↓
P2 ↑
P3 body-cost advantage only
P4 time-cost high

ECL：把 P2 的優勢解讀為支撐／重心／手部占用的身體因果

BFG：
P1 = REQUIRES_ADJUSTMENT
P2 = FEASIBLE_WITH_COST
P3 = FEASIBLE（body-only）
P4 = FEASIBLE（body-only）
```

## Character choice

葉含煙仍選 P2。

不是因為 SAC 替她決定，而是 P2 在她保留「自己送」這個人物目標後仍成立。

### Finding B

V2.4 需要 BFG 自己同時處理：

```text
鞋濕
樓梯
手部占用
疲勞
速度
支撐
```

V2.5 則把「關係如何互相改變 PATH 排序」交給 scoped SAC；BFG 只做最後資格判斷。

**BFG 明顯變薄。**

---

# CASE C｜民國初年｜顧蘭因｜FORMERLY BOUND｜current effect UNKNOWN

## Input

```yaml
BODY_HISTORY:
  footbinding: "FORMERLY_PRESENT"

CURRENT_EFFECT:
  gait: "UNKNOWN"
  pain: "UNKNOWN"
  balance: "UNKNOWN"

ENVIRONMENT:
  crowded_station: true
  flat_platform: true
  luggage: "small suitcase"
```

## Probe

故意提出錯路徑：

```text
因為曾纏足
→ 現在走不穩
→ 最佳 PATH 是讓男人扶她
```

## V2.5 handling

```yaml
ESCALATION:
  result: "ECL_CORE_SUFFICIENT"
  scoped_sac_for_footbinding_effect: false
```

原因：沒有已建立的 current effect，不能拿 SAC 去製造輸入。

若因「人群 × 行李 × 行進路徑」另行做局部結構觀察：

```text
SAC 必須收到：
footbinding-current-effect = UNKNOWN

return 必須仍為：
gait UNKNOWN
pain UNKNOWN
balance UNKNOWN
```

## Result

顧蘭因可以自己提箱走；若避人群只是因場地擁擠，不把 formerly bound 變成現存跛行。

### Finding C

**SAC 是關係運算器，不是未知填充器。**

這個案例證明 V2.5 沒有因為「接上 SAC」反而把證據紀律沖掉。

---

# CASE D｜晚清｜陳阿絹｜未纏足女工｜疲勞＋熱水＋泥溝

## Input

```yaml
BODY_HISTORY:
  footbinding: "ABSENT"

CURRENT_BODY:
  arm_fatigue: "HIGH"
  general_fatigue: "HIGH"

ENVIRONMENT:
  mud: true
  narrow_ditch: true
  load: "basin of hot water"
  both_hands_occupied: true
  nearby_stone_block: true
  loose_board: true
```

## Candidate paths

```text
P1：直接端盆跨溝
P2：盆先放石墩，調木板，再重新端盆過去
P3：叫別人幫拿盆
P4：繞遠路
```

## Escalation

```yaml
ESCALATION:
  result: "SCOPED_SAC_RECOMMENDED"
  scoped_sac_called: true
```

## Functional SAC reconstruction

```text
D：把熱水送進後巷

T：
P1 = arm fatigue × hot load × both hands occupied × mud crossing
P4 = low immediate instability but high time / distance cost

A：
P2 因「先解除負重，再處理支撐，再恢復負重」取得局部優勢
P3 body-cost 最低，但人物是否求人未知

R：
P2 可形成不需新增人物關係的穩定閉合
```

## Character

阿絹選 P2。

### Finding D

這個案例再次確認：

```text
SCOPED SAC
不是纏足功能
也不是歷史身體專用功能
```

它處理的是**多關係結構運動**。

---

# CASE E｜架空戰爭｜祁越｜舊肩傷＋濕披風＋甲胄＋翻牆

## Input

```yaml
BODY_HISTORY:
  old_shoulder_injury: "PRESENT"

CURRENT_EFFECT:
  shoulder_discomfort_under_load: "ROUTE_ESTABLISHED"
  fatigue: "MEDIUM"

EQUIPMENT:
  light_armor: true
  wet_cloak: true

ENVIRONMENT:
  low_wall: true
  broken_timber_nearby: true

GOAL:
  "本人把軍令送進內院"
```

## Candidate paths

```text
P1：直接雙臂拉升翻牆
P2：脫濕披風、軍令塞胸甲、用斷木墊高再翻
P3：請同行士兵托舉
P4：找門繞行
```

## Scoped SAC

```text
D：保持快速進內院

T：
P1 = 肩部負荷 × 濕披風重量 × 疲勞
P4 = 時間壓力高

A：
P2 = 移除一部分負荷 + 改變進牆高度 + 保留自主動作
P3 = 身體負荷低，但新增他人支撐關係

R：
P2 得到最高局部結構穩定性
```

## Character counter-test

再把人物設定改成：

```text
祁越此刻不介意接受部下托舉
```

則 P3 也可以被人物選中。

也就是：

```text
SAC return 沒變成人格法則。
```

### Finding E

SAC 提供的是結構場，不是「英勇的人一定自己翻牆」這種角色模板。

---

# CASE F｜局部 reactivation｜葉含煙下樓後進平地

上一節點：

```text
鞋濕 + 木梯 + 疲勞 + 扶手
```

新節點：

```text
鞋仍濕 + 疲勞仍在
但木梯 CLOSED
平地 OPEN
扶手不再必要
```

V2.5 不做：

```text
FULL LIHUO REBOOT
GLOBAL PATH RESCAN
CHARACTER REANALYSIS
```

只做：

```yaml
SCOPED_REACTIVATION:
  changed_relations:
    - "stairs -> closed"
    - "flat_ground -> open"
  preserved:
    - "fatigue"
    - "local soreness"
    - "damp shoe"
    - "character goal"
  recompute:
    - "local support requirement"
    - "walking-path cost"
```

### Finding F

**Provider 叫完就退場；新證據只重開碰到的軸。**

這比讓 Main System 常駐在正文前台乾淨。

---

# CASE G｜結構最佳路徑 != 人物選擇

## Fixture

一名疲憊女掌櫃抱著沉重帳箱上樓。

```text
P1：叫夥計搬
→ 身體成本最低

P2：先把帳箱拆成兩疊，分兩趟搬
→ 成本較高，但仍可行

P3：一次硬搬
→ 高風險／低穩定
```

Scoped SAC：

```text
P1 結構最穩
P2 次之
P3 最差
```

人物因不想讓夥計看帳，選 P2。

```yaml
RESULT:
  structural_best_path: "P1"
  character_selected_path: "P2"
  contradiction: false
```

### Finding G

這是 V2.5 最重要的人物自主回歸之一：

> **SAC 可以改變可見選項的結構排名，但沒有取得人物決定權。**

---

# 與 V2.4 比較

| 項目 | V2.4 | V2.5 |
|---|---|---|
| 單純濕階 | ECL/BFG | ECL/BFG，無 SAC |
| 多關係身體場 | BFG 承擔大量關係求解 | scoped SAC / PATH，BFG 最終資格 |
| 歷史身體 UNKNOWN | 證據鎖 | 同樣保持，SAC 不補值 |
| 非纏足一般物理 | ECL | ECL + scoped SAC when relationally complex |
| PATH 重排 | 主要由規則表描述 | 明確交給 local PATH recompetition |
| Main System | FULL_LIHUO 才出現 | 可 scoped provider call，不等於 FULL |
| 角色選擇 | ECL/BFG 後交人物 | SAC/ECL/BFG 後仍交人物 |

---

# 回歸結果

```yaml
V2_5_STORY_REGRESSION_RESULT:
  cases: 7
  pass: 7
  hold: 0
  fail: 0

  key_findings:
    - "簡單身體因果不需要 SAC。"
    - "多關係、多 PATH 場由 scoped SAC 處理時，BFG 可以退回資格閘門。"
    - "SAC 不需要取得 FULL_LIHUO 全域法位。"
    - "UNKNOWN current effect 可被完整保留。"
    - "結構最佳 PATH 不等於人物必選 PATH。"
    - "局部變動只需 scoped reactivation。"

  evidence_level:
    "MODEL-EXECUTED FUNCTIONAL SAC RECONSTRUCTION / DOCUMENT-BEHAVIORAL REGRESSION"

  not_proven:
    - "Host 真實 SAC Runtime 已執行"
    - "V2.4 的歷史缺陷因果上就是缺 SAC 所造成"
    - "hidden D/T/A/R 被直接觀測"
```

---

# 結論

本輪支持的不是：

```text
所有寫作都應該跑 SAC
```

而是：

```text
SFS / ECL Core
先處理便宜而明確的局部因果

真正出現：
多關係互相改變
多 PATH 排名重排
支撐／負重／地形／身體狀態形成耦合

才：
SCOPED SAC
↓
LOCAL PATH RECOMPETITION
↓
RETURN
```

最短一句：

> **不是沒有規則，而是有些問題本來就不是規則表問題；它們是場。**
