# 02｜實際執行紀錄與失敗證據

## 環境
- Python 3.13.5；本回合容器中的本地程式實際執行（非模擬工具輸出）。
- source file Git blob SHA 對本地已執行 bytes: radar_relation_monitor.py = bf10d53fb86c5cf2e2b3a243d10e501e9a613690
- test_monitor.py = 95bf90723ba67c621d9d062b199476edf98e3e96
- mutation_probes.py = f1f6f2bbd7fc678e76f81500bb2dccaa2e0fb8bd
- semantic_limit_probe.py = 2b1a8b185a55b7cb954503befd735248d6bebe2c
- Case A/B/C/D SHA: b00e7b79cb2784c291de01d00d75f9b65761f07f / 9379f2710f58b2c385401b9e5c54aca4b556acdc / 40724bd4885c551c8950f97f5961241df9bccd02 / 1cbb2eb1e8a502af20f60bf498ac1ebf7ab36b94

## 實際命令與結果
1. python test_monitor.py → Ran 23 tests in 0.001s → OK，exit=0。測試驗證了時間／地點重疊、權限撤銷與再核准、狀態版本、不偷改原資料、source update 跟靜默等狹窄功能。
2. python mutation_probes.py → All 5 mutants caught，exit=0。預期失敗突變：
   - M1_IGNORE_ZONE → unit tests failures=2
   - M2_IGNORE_DAY → failures=2, errors=1
   - M3_DISCARD_REVOKED_PERMISSION → errors=2
   - M4_FORGET_ACTIVE_STATE → failures=6, errors=2
   - M5_HIDE_SOURCE_LINEAGE_DELTA → failures=2
   這說明測試有能力抓到**這五種人為已知錯誤**；不表示所有現實錯誤都會被抓到。
3. python semantic_limit_probe.py → exit=0，報出 KNOWN_SEMANTIC_BLINDSPOT_EXPOSED；Case D：3 events，0 candidate alerts。探針的成功是**確認研究目標尚未做到**，不是把漏報視為成功。
4. python radar_relation_monitor.py CASE_A_SITE_RELATIONS.json → 有來源的 raised/withdrawn 和 active list JSON；也單獨跑 B、C 兩份。這是 deterministic returns，沒有另一個模型參與判斷。

## 逐情境計數（程式輸出實際統計）
| Case | Events | Raised | Withdrawn | Lineage update | Quiet |
|---|---:|---:|---:|---:|---:|
| A 活動中心 | 8 | 5 | 1 | 1 | 1 |
| B 資料權利 | 6 | 3 | 2 | 1 | 0 |
| C 陰性對照 | 6 | 1 | 1 | 0 | 4 |
| D 語義盲點 | 3 | 0 | 0 | 0 | 3 |

A 中的 E05/E06 承接 004 的**虛構反事實更新**；不是原始 S02 真實被改寫。B/C/D 全是新的虛構 fixture，不代表世界真有此交易、合約或施工。

## 三個必須防止的誤讀
- **23/23** 是單元測試的 PASS，不是「雷達準確率 100%」或 23 次 AI 獨立推理。
- **5/5 mutation caught** 是對挑選過的破壞規則之檢驗，不是統計性的真實世界 false-positive/false-negative 量測。
- **Case D 0 alerts** 是最重要的負面結果：因為程式沒把授權目的與產品用途建成關係，明顯的權限不相容在簡化型別中被完全吞掉。

## 本輪真正知道與未知
知道：一個小型 source-linked event reducer 可重跑且能處理某些已命名的關係變動；原始程式能通過 23 tests，預設的突變被抓到；語義盲點 D 確實存在。

不知道：Radar V6 真能否從未建模文字辨認新關係？同樣消息下 Radar ON 是否較 OFF 產生 material discovery？對比真正的跨模型理火狀態與第一步回歸，是否可以移轉？完整成本是否合理？目前沒有獨立模型上下文或背景 Radar provider，不能測定這些未知。