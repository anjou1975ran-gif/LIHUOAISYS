
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


## SESSION_20261121_INTERNSHIP_MANUAL_V13_EVAL_001｜通用新理火 AI 實習手冊 V1.3 正式評估
- [會議入口與完整結構](SESSION_20261121_INTERNSHIP_MANUAL_V13_EVAL_001/00_SESSION_README.md)
- [最終評估](SESSION_20261121_INTERNSHIP_MANUAL_V13_EVAL_001/07_FINAL_EVALUATION.md)
- [給人類的簡報](SESSION_20261121_INTERNSHIP_MANUAL_V13_EVAL_001/08_HUMAN_BRIEF.md)

**結果：** 共享 Formation 核心＋各 Vertical 自有實習與證據介面（建議），C 席對跨 Vertical 實證仍 HOLD；本次未改 V1.3、Protocol、OS。六初始＋四重喚醒 L8，同模型參考執行。


## 2026-11-21｜V1.3.1-CANDIDATE 續會 R003/R004
- [同 Session 續會入口](SESSION_20261121_INTERNSHIP_MANUAL_V13_EVAL_001/00_CONTINUATION_INDEX_R003_R004.md)
- [P1 修正案審議判斷](SESSION_20261121_INTERNSHIP_MANUAL_V13_EVAL_001/17_P1_REVISION_VERDICT.md)
- [短版人類決策請求](SESSION_20261121_INTERNSHIP_MANUAL_V13_EVAL_001/18_HUMAN_BRIEF_REVISION.md)
**結果：** 建議再修 V1.3.1 候選，未批准成 CURRENT；Premise Literacy 有條件支持、四條 lane 需 D1/D2 非互推。40 個同 Session event，19 個 SAME_MODEL_MULTI_ROLE_REFERENCE L8；Cross Vertical 實證 HOLD。
