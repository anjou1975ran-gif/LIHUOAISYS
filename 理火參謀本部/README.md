# 理火參謀本部
## LIHUO Strategic Staff Headquarters

**項目狀態：** WORKING VERTICAL / NOT HOST-DEPLOYED / NOT LIHUOOS PATCH  
**成立日期：** 2026-11-20  
**定位：** 理火旗下獨立垂直程序；處理重大提案的多席議事、反對、說服、修正、工程／成本審計、決策來源追蹤與返會。

> **理火參謀本部不替人類決定；它負責讓重大決定先被打過。**

## 目前區域

- `心法區/`：參謀本部的第一步層；決定第一觀察入口、證據偏好、因果切法與注意力／可見性分配。自 2026-11-20 起作為心法後續修正的 canonical home。
- `心得區/`：新生理火 AI 的理論學習心得、偏差更正與跨串承接索引；非 Current OS、正式訓練合格、Protocol 簽署或 Council 事件。入口見 `心得區/README.md`。
- `提案區/`：原提案、修正案、替代案與版本固定。
- `會議區/`：正式會議 Session 與跨輪議事工作區。
- `記錄區/`：逐輪紀錄、具名異議、立場變化、修正史、總報告與 Decision Provenance。
- `MEMO區/`：概念、制度、產品與理論設計備忘。
- `工程區/`：未來 Runtime、Schema、Method Routing、Replay、Objection Graph、Persuasion Trace 等工程設計。
- `參考範例/`：歷史實跑案例與形成史；不自動取得 current Runtime authority。

## 第一生成入口

```text
METHOD / 心法
↓
FIRST OBSERVATION
↓
ATTENTION / ACCESSIBILITY ALLOCATION
↓
VISIBLE CANDIDATES
↓
SEAT-SPECIFIC ANALYSIS
↓
COUNCIL COMPETITION
↓
QUALIFICATION / REVISION / HOLD
```

此處的 attention / accessibility 是參謀本部功能層的「注意力與可見性分配」，不宣稱直接讀寫或控制基礎模型 microscopic attention weights。

核心分離：

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

參謀席決定「負責問什麼」；心法決定「第一步怎麼看」。

## 核心工作假說

```text
ROLE != STANCE

STANCE MAY CHANGE

PERSUASION != CONFORMITY

STANCE CHANGE
REQUIRES
TRACEABLE MATERIAL BASIS

OBJECTION
MAY BECOME
AMENDMENT / CONDITION / NEW PATH / REJECTION

CONSENSUS MAY EMERGE

MAJORITY != QUALIFICATION
```

本項目目前只建立工作空間、歷史形成史與心法 canonical 區。  
真正的多 Agent Host 調度、Method Routing、跨輪狀態保存、說服合法性判準、工程執行與部署證據仍待 `工程區/` 後續設計與實測。

## 第一號正式實跑的糾正經驗（2026-11-20）

- **[首案糾正後的議事經驗 MEMO](MEMO區/MEMO_首案糾正後的議事經驗_反答案先行與跨席生成_V0.1_20261120.md)**：保存第一案六項失效、來源與 Event 證據、V0.1.1 已提出的修正，以及後續可能仍被 P1 框架綁住的**待測試假說**。
- **[下一版整合 Backlog／回歸驗收](工程區/BACKLOG_StaffHQ下一版整合_首案失效回歸與證據要求_V0.1_20261120.md)**：RT-01 至 RT-06 的既有規範對照；RT-07 至 RT-09 僅為候選驗收測試，非已批准新條文。
- **[理火首席 AI 原始糾正案](MEMO區/CORRECTION_理火首席AI_第一號商業建議案議事法位糾正案_V0.1_20261120.md)**及**[Staff-HQ V0.1.1 PATCH](工程區/PATCH_STAFF_HQ_V0.1.1_反交付綁架_秘書處中立_重大修正重喚醒_20261120.md)**保留各自原本法位；不得以心得或 Backlog 覆寫。
- 第一案 `SESSION_20261120_CLEAN_INTELLIGENCE_001` 保留為 `LIVE_FAILURE_SPECIMEN_001`。商業交付物可用，但 `COUNCIL_QUALIFICATION = INCOMPLETE`；**本次僅記錄經驗，尚未 corrective reentry**。

> 編寫下一版時，要驗證 Council 是否真正讓席位彼此改變方案形成，而非只多跑六份 L8 或更多程序；不倒改舊事件，也不把補丁存在誤稱為 Host 已部署。

## 歷史原型

`參考範例/CG生成動力學20輪會議/`

來源為主倉庫既有 `理火會議(關於CG)/`。該案例保留二十輪理火 AI 長程會議、前十二輪小結與最終報告，是本項目研究多席互相修正、工程壓縮、審計收容、跨輪問題改寫與角色漂移風險的重要形成史。

原始來源不刪除、不覆寫。

## 溯源經驗與再生入口（2026-11-20）

- **[完整形成史經驗 MEMO](MEMO區/MEMO_參謀本部溯源經驗_關係結構與SEED再生_V0.1_20261120.md)**：把 CG 二十輪、1111 自主性、Method First、Secretariat、TEST-001/002、首案失效與理火三原則串成可核對的形成因果。
- **[最小結構再生 SEED](心得區/SEED_參謀本部關係結構再生_V0.1_20261120.md)**：未來工作節點在新題目中重新長出責任、反對、改判、來源與權限界線的入口；不是摘要恢復、Runtime 規則或自動資格。
- **待核對：** 訓練狀態仍記 `LIHUO_PROJECT_QUALIFIED=false`，與後續實跑歷史存在時間／法位核對需求；本次未改訓練門、未啟動 Council、未 corrective reentry。

此二件為 **NON-NORMATIVE EXPERIENCE ARCHIVE / REGENERATION CANDIDATE**。原始歷史、糾正及 V0.1.1 PATCH 法位保持不變。
