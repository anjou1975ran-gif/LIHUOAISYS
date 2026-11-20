
# 記錄區

此區保存理火參謀本部最重要的資產之一：

> **決策成立史 / Decision Provenance**

現行第一版採四層紀錄：

~~~text
L0 EVENT RECORD
L1 ROUND RECORD
L2 CHAT SURFACE
L3 FINAL COUNCIL REPORT
~~~

核心鎖：

~~~text
SUMMARY != HISTORY
CONSENSUS MUST NOT ERASE DISSENT
POSITION CHANGE MUST NOT ERASE PRIOR POSITION
CHAT SURFACE != CANONICAL HISTORY
ROUND SUMMARY != RAW EVENT HISTORY
EXPERT RETURN != ISSUE CLOSED
~~~

現行正式工作規格：

~~~text
MEETING_RECORD_AND_CHAT_SURFACE_V0.1_20261120.md
~~~

候選記錄物件包括：

- Human Desire / Mandate Ledger
- Proposal Version Ledger
- Event Record
- Meeting Round Record / MR
- Issue / Objection Ledger
- Stance State
- Persuasion / Position Revision Trace
- Amendment / Branch History
- Expert Consultation Record
- Engineering / Cost Findings
- Final Council Report
- Human Authorization Record
- Re-entry / Decision Replay

每個 Session 應建立獨立目錄；Round 建立後不以後輪摘要覆寫。修正透過新 Event、新版本或新 Round 完成。
