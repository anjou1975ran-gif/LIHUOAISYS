
# P001｜Secretary Kernel V0.1
## 理火參謀本部第一個實跑提案

**提案狀態：** READY_FOR_COUNCIL_TEST / NOT APPROVED  
**日期：** 2026-11-20

---

# D0｜Raw Human Desire

保留本輪人類指示：

> 「這套會是第一個被拿去打的提案，可以動手寫，然後我們用專案來跑看看。每輪會議要有會議紀錄格式，要規定怎樣紀錄、怎樣總結每次報告、怎樣寫入、怎樣在 CHAT 介面回報，是用對話模式還是怎樣的發言模式。」

---

# D1｜Secretary Interpretation

~~~yaml
D1_QUALIFIED_MANDATE:
  standing: SECRETARY_INTERPRETATION / HUMAN_NOT_YET_CONFIRMED
  mandate_type: CONCEPT

  primary_question: >-
    Secretary Kernel V0.1 及其 Meeting Record / Chat Surface 設計，
    是否足以作為理火參謀本部第一版議事運作骨架？

  desired_return:
    - 結構性缺口
    - 權力越界點
    - 可實作性問題
    - 成本與複雜度問題
    - 更好的替代設計
    - 第一版可保留部分
    - 尚不可封版部分

  human_intervention_mode: H0_FREE

  acceptable_hold: true
~~~

---

# Proposal Under Test

1. Secretary 是 process owner，不是 truth / stance / final decision owner。
2. Round 是 checkpoint，不是 agenda。
3. 會議採 event-driven routing。
4. CORE-6 不必每輪全部發言。
5. Issue 有 origin owner，但 owner 沒有 veto。
6. Expert Return 不自動關閉 Issue。
7. Proposal / Stance 都版本化。
8. Closure Sweep 由 CORE-6 最後掃描是否仍有 material issue。
9. Mandate Exit Test 依 CONCEPT / RECOMMENDATION / DECISION 不同。
10. Chat 採 Structured Speaker Mode，底層另存完整 Event / Round Record。

---

# Required Attack

CORE-6 必須至少檢查：

- N1：普通管理者實際使用會不會太複雜？
- A：是否還有更簡單或更強的議事形態？
- B：是否「Secretary Kernel」本身就是錯的框架？
- C：秘書處是否暗藏未授權的語義／裁決權？
- D：狀態、版本、queue、wake 是否可實作？
- E：token、latency、紀錄、專家召入、維護成本是否失控？

Secretary 必須允許：
- 反對本提案；
- 修改本提案；
- 分叉本提案；
- HOLD；
- 判定整套過度設計；
- 建議刪除自身權力。

**END**
