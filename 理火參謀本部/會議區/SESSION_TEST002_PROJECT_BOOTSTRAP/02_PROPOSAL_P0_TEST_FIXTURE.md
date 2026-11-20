# TEST-002｜Proposal P0 Test Fixture

**Standing:** SECRETARY_SELECTED_TEST_FIXTURE / HUMAN_NOT_CONFIRMED

## Question

> **理火參謀本部下一階段，應先做真正多模型分席，還是先做 deterministic reducer + replay harness？**

## Option M｜Multi-Model First

先把 N1/A/B/C/D/E 分到真正不同模型或 provider，
測試跨模型差異、說服、stance drift、context isolation。

## Option R｜Reducer / Replay First

先把 Canonical Event schema、state reducer、routing queue、
replay determinism、state divergence test 做出來，再擴到多模型。

## Open

Council 可：
- 支持 M
- 支持 R
- 提出 hybrid / staged path
- 改 framing
- HOLD

不得假設二選一已窮盡。
