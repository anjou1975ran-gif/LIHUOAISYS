
# HUMAN DECISION REQUEST SPEC V0.1
## Secretariat Human Decision Gate / 秘書處人類決策要求

**版本：** V0.1-WORKING  
**日期：** 2026-11-20  
**狀態：** FIRST UX / GOVERNANCE SPEC

---

# 0｜核心問題

治理正確但人類看不懂，等於產品失敗。

如果 Session 進入：

~~~text
WAITING_HUMAN
~~~

但只把 D1、Issue ID、Closure State、Mandate Standing 丟給人類自行理解，則：

~~~text
GOVERNANCE CORRECT
+
HUMAN UNUSABLE
=
SYSTEM FAILURE
~~~

因此新增：

> **DECISION REQUEST / 決策要求**

---

# 1｜定位

~~~text
EXECUTIVE BRIEF
=
告訴人類現在發生了什麼

DECISION REQUEST
=
告訴人類現在只需要決定什麼
~~~

當流程因人類輸入不可替代而停止時：

~~~text
HUMAN_ACTION_REQUIRED
→
DECISION_REQUEST_REQUIRED
~~~

硬鎖：

~~~text
WAITING_HUMAN
WITHOUT
DECISION_REQUEST
=
UX FAILURE
~~~

---

# 2｜中盤 Ending

新增：

~~~text
CHECKPOINT_ENDING
/
HUMAN_DECISION_GATE
~~~

它不是 Session End。

~~~text
CHECKPOINT_ENDING
!=
SESSION_END
~~~

意思是：

> 本階段 AI 議事已走到沒有合法資格自行往前的位置，必須交回人類一個最小決策。

---

# 3｜Decision Request 最小格式

~~~yaml
DECISION_REQUEST:
  request_id: REQUIRED
  session_id: REQUIRED
  reason_for_stop: REQUIRED

  plain_language_context:
    what_we_were_doing: REQUIRED
    what_happened: REQUIRED
    why_ai_cannot_continue_alone: REQUIRED

  decision_question: REQUIRED

  choices:
    - choice_id: REQUIRED
      plain_label: REQUIRED
      what_this_means: REQUIRED
      what_happens_next: REQUIRED
      what_this_does_not_mean: OPTIONAL

  no_response_behavior: REQUIRED
  provenance_refs: []
~~~

---

# 4｜白話要求

Decision Request 必須符合：

~~~text
ONE HUMAN DECISION
PER REQUEST
~~~

禁止：
- 要人類閱讀完整 D1 才能回答；
- 只給 internal enum；
- 只給 Issue ID；
- 用「是否確認上述 qualified mandate standing」當問題；
- 用專家術語代替決策本身。

應寫：

> 「我們這次是不是就是要測：這套秘書處架構能不能當第一版骨架？」

而不是：

> 「請確認 D1 Qualified Mandate Candidate。」

---

# 5｜Choice 設計

每個 Choice 至少要說明：

1. 你選這個代表什麼；
2. 系統下一步會做什麼；
3. 它不代表什麼。

候選：

~~~text
A｜對，就是這件事
→ 將現有 D1 升格為 Human-Confirmed Mandate
→ 進 Mandate Exit Test
!= 你已批准 P1R3 架構

B｜不對，我要改題目
→ 人類用一句話說真正要測什麼
→ 秘書處生成新 Mandate Version
!= 前六輪歷史作廢

C｜先不要收，繼續打
→ Session 回 OPEN
→ 明確要求再開議事
!= 目前架構已被否定
~~~

---

# 6｜不得偷的權

Decision Request Renderer 可以：
- 翻成普通語言；
- 把複雜狀態壓成單一決策；
- 描述每個選項後果。

不能：
- 偷加偏好；
- 把某 Choice 寫得故意可怕；
- 把 Council recommendation 冒充 Human obligation；
- 隱藏合法選項；
- 把「確認 Mandate」寫成「批准方案」。

硬鎖：

~~~text
CONFIRM MANDATE
!=
APPROVE RESULT

END SESSION
!=
ACCEPT RECOMMENDATION

CHOOSE NEXT PROCESS
!=
ENDORSE CURRENT STANCE
~~~

---

# 7｜來源與可追溯性

Decision Request 是 Derived Human View。

~~~text
CANONICAL STATE
+
HUMAN ACTION BLOCKER
↓
DECISION REQUEST
~~~

Decision Request 本身不創造 canonical decision。

Human response 才形成新的 Human Decision Event。

---

# 8｜與 Ending 的關係

~~~text
OPEN
↓
CONTENT CLOSURE / OTHER GATE
↓
HUMAN ACTION REQUIRED
↓
CHECKPOINT_ENDING
↓
DECISION REQUEST
↓
WAITING_HUMAN_DECISION
↓
HUMAN DECISION EVENT
↓
OPEN / EXIT_CANDIDATE / ENDED / OTHER LEGAL STATE
~~~

因此：

> **Ending 不一定是結束整場；也可以是 AI 把球合法交回人類的中盤終點。**

**END**
