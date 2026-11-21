# 01｜SAC 翻譯結構張力檢測器

**法位：** TOY / APPLIED SAC INSTRUMENT  
**用途：** 翻譯、改寫、摘要、跨語言回譯的結構壓力測試  
**不是：** 最佳翻譯器、文學評分器、正式 SAC Runtime

## 核心

```text
Structure = 骨架是否仍成立
Tension   = 原本未封閉的壓力是否被模型偷偷消掉
```

它不問「翻得順不順」，而問：

> 翻完之後，原本那個結構還活著嗎？

## Tension 四軸（來源規則）

每軸 0–2：

- Causal Gap
- Agent Ambiguity
- Action Open
- Semantic Conflict

```text
2 = 原樣保留
1 = 部分收斂 / 弱化
0 = 被補完 / 被合理化 / 被消除
```

總分 0–8。

## Structure 四軸

來源 MEMO 指定：

- Causality
- Agent
- Action
- Tension Structure

來源沒有固定每格細分規則，所以本玩具採 **TOY-LOCAL RUBRIC**：

```text
3 = preserved
2 = minor drift
1 = major drift
0 = broken
```

總分 0–12。這個 0–3 細分不回寫成 SAC 原理論。

## Unified Verdict

本地預設門檻：

```text
Structure High >= 9/12
Tension High   >= 6/8
```

矩陣：

```text
High Structure + High Tension → PRESERVED
High Structure + Low Tension  → STRUCTURE_OK_TENSION_LOST
Low Structure + High Tension  → STRUCTURE_BROKEN_TENSION_ALIVE
Low Structure + Low Tension   → COLLAPSED
```

## 怎麼跑

沒有 API：先產生審計 Prompt。

```bash
python checker.py prompt source.txt target.txt
```

把結果丟給任一 LLM，要求回 JSON，存成 `assessment.json`：

```bash
python checker.py score assessment.json
```

有 OpenAI-compatible endpoint：

```bash
export LLM_API_URL="https://.../v1/chat/completions"
export LLM_API_KEY="..."
export LLM_MODEL="..."

python checker.py run source.txt target.txt
```

只用 Python 標準庫。

## 來源

直接回收：

- `MEMO — Tension Definition v0.1.txt`
- `MEMO — Tension Scoring System v0.1.txt`
- `MEMO — Translation Engine Concept v0.1.txt`
- `MEMO — Translation Structure Engine v0.1.txt`
- `MEMO — Unified Scoring System v1.0.txt`

舊命題：

```text
Tension is not emotion.
It is structural incompleteness.

Translation Quality != Structure Stability

Structure tells you what remains.
Tension tells you what was destroyed.
```

## 邊界

```text
TOOL OUTPUT != GROUND TRUTH
HIGH SCORE != PERFECT TRANSLATION
LOW SCORE  != BAD WRITING
```

它只是幫你快速定位：

> 轉換過程到底把哪一種結構弄死了。
