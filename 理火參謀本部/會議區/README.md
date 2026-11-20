
# 會議區

此區承載正式 Council / Staff Session 的**人類可讀會議面**。

現行第一版固定班底：

~~~text
N1｜Common-Sense / 常識席
A ｜Possibility Expansion / 可能性擴張
B ｜Architecture Turn / 架構轉向
C ｜Qualification Audit / 資格審計
D ｜Engineering Audit / 工程審計
E ｜Cost & Resource Audit / 成本資源
~~~

非議事角色：

~~~text
N0 = Normal Agent Control / 隔離對照
SEC = Secretary / 程序核心，不裁決
HUMAN = Human Desire + 最終授權來源
~~~

外掛：

~~~text
GUEST EXPERT = CONSULTATIVE BY DEFAULT
~~~

核心：

~~~text
ROLE != STANCE
ROUND != AGENDA
ACTIVE MEMBER != MUST SPEAK EVERY ROUND
PERSUASION != CONFORMITY
SUMMARY != HISTORY
~~~

會議預設採：
- Event-driven routing；
- Structured Speaker Mode；
- Round 作 checkpoint / snapshot；
- 只有被 Wake 的席位需要發言；
- 秘書處只做路由與狀態回報；
- 外掛專家由秘書處按 Consult Request 召入。

正式紀錄規格見：

~~~text
記錄區/MEETING_RECORD_AND_CHAT_SURFACE_V0.1_20261120.md
~~~

第一個實跑提案：

~~~text
提案區/P001_Secretary_Kernel_V0.1_第一個實跑提案_20261120.md
~~~

目前不宣稱已部署獨立多 Agent Runtime。若同一模型分角色執行，Session 必須標記：

~~~text
SAME_MODEL_MULTI_ROLE_REFERENCE
~~~
