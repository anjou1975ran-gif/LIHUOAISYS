# RLT｜OPEN DISCUSSION LOG
## 關係譜系追蹤器研究討論入口

**Standing:** OPEN / APPEND-ONLY DISCUSSION / NON-NORMATIVE

---

## 2026-11-21｜Opening Note

### 起點

本研究線由 PSO-005 的 relation monitor 演化而來。

最初問題：

> Radar 的提醒能不能隨事件改變而撤回、恢復與保留來源？

第一個工程答案：

> 已命名的 relation delta 可以被 deterministic code 追蹤。

第一個反例：

> Case D 證明 `GRANTED` 這種 scalar status 可能吞掉真正 material 的用途／範圍關係。

第一個上位修正：

> Coding 可維護已被表示的關係；未被表示的關係如何被看見，仍屬 SAC / MAIN / Radar / semantic discovery 問題。

### 第二次轉折

V1.3 教材評估 Council 產生多席 stance、objection、rejudgment 與 minority HOLD。

這暴露：

> relation lifecycle 並不總是單一路徑；真實工作更接近 branching lineage。

因此暫名從：

~~~text
Relation Lifecycle Tracker
~~~

調整為：

~~~text
Relational Lineage Tracker
RLT
關係譜系追蹤器
~~~

### 暫時觀察

RLT 可能不是 Radar 的眼睛。

更可能是：

> **Radar／MAIN 已經叫大家注意某個關係之後，負責保存這個關係後來怎麼變、誰改了什麼、什麼仍然活著的記憶與 lineage 工具。**

這個定位仍 OPEN。

---

## 明日可從這裡繼續

候選討論入口：

1. 先畫出 RLT 最小資料模型。
2. 用教材 Council 40 events 當第一個 lineage fixture。
3. 找出目前 `supersedes_refs` 的語義混用。
4. 再做 1111 fixture。
5. 再做觀止 fixture。
6. 三者通過後才討論 L9 promotion gate。

**DO NOT PROMOTE BEFORE CROSS-VERTICAL CORE SURVIVES.**
