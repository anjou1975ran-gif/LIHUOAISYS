# LIHUO Method Database

這是 LIHUOAISYS 的根層共用心法資料庫。參謀本部、AI 律師、論文審查及其他垂直依各自授權調閱。

## FIRST READ

1. [Canonical Index](00_CANONICAL/METHOD_ATLAS_CANONICAL_INDEX_V1.0.md)。確認 ID、版本、法位和唯一預設來源。
2. [Routing Index](00_CANONICAL/METHOD_ATLAS_ROUTING_INDEX_V1.0.md)。按問題和證據選 2–5 個候選，檢查有無實質觀察增量。
3. 只讀選中的 exact canonical file。若沒有實質增量，回傳 `NO_METHOD`。

**ROUTING BEFORE RETRIEVAL. EXACT PACK AFTER SELECTION.**

以索引指定路徑取檔。一般調閱排除整庫預載、檔名猜版本、舊版、AI 友善衍生版和施工稽核。

**DO NOT LOAD FOR ORDINARY METHOD ROUTING.** 版本、Coverage、來源或修改爭議才查 [90_BUILD_AUDIT](90_BUILD_AUDIT/README.md)。

歷史或相容需求才查 [99_LEGACY_COMPATIBILITY](99_LEGACY_COMPATIBILITY/README.md)。候選法位與執行授權以原正式文件為準。

## Separate Historical Archive

- [理火歷史理論區](../理火歷史理論區/README.md)

此區是歷史來源保存與譜系研究區，不屬於本資料庫的 Canonical Registry 或 Routing Index，也不參與一般方法路由。只有明確需要歷史理論追溯時才調閱。
