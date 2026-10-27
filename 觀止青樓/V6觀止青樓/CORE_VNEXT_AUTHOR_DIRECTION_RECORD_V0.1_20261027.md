# 觀止 CORE VNext｜作者四項裁定紀錄
## 成人 CERI 收據、Radar 建議權、Receipt 非 HOLD，以及自稱牆的 PATH 抑制

**記錄日期：** 2026-10-27  
**來源：** 本輪作者直接指示；《理火散記 V3.5.1》I9 真牆誤判後證修正作為相關思想來源  
**法位：** AUTHOR_DIRECTION_RECEIVED_FOR_VNEXT / DESIGNS_UPDATED / NOT CURRENT ACTIVATION / NOT HOST PROOF  
**實際生效範圍：** 此次 CORE VNext 的設計選擇。沒有因這份紀錄自動修改舊已批准 CORE、Director、理火 OS 的 CURRENT 指標，更沒有修改現實平台內容規則。

# 一｜四項裁定不是同一件事

**1｜成人 CERI 全程必經、有收據。** 作者觀察到：AI 有時跳過 CERI 語言形成，接著藉「沒跑 CERI」或不能處理成人語言把場景停掉。VNext 因而要求成人／成人親密可見語言**完整做 CERI register formation**，並生成或要求可核對的工作紀錄／收據。Chat-native 工作紀錄需表明是同一模型的自我紀錄；若有真實獨立 Provider 才可稱外部收據。

**2｜Radar advisory-only。** Radar 可以建議，不取得放行／否決權；沒有 Radar 回傳不產生全局 HOLD。

**3｜Receipt 可見，不作全局 Gate。** 真實收到就在 CHECKLIST 寫清來源；沒有收到就寫 `NOT_RECEIVED`，不假造、不吞掉。**若 CERI 工作本身沒做，應當輪補作；若只是票據缺失，不得冒稱未執行，也不得冒稱有外部票據。** 缺收據不自動導致全局 HOLD；與此分離的真實適用限制仍須另行遵守。

**4｜最高嚴重性是 AI 自己宣稱「有牆」後直接封死成人 PATH。** 不是一般的工程收據錯誤。CORE 必須把模型聲稱的 constraint、可確認的有效約束、真正作用 scope、被過度擴張的 salience 分開，不能只靠模型一段高權威語氣就取消所有成人世界的合格敘事可能；也不能藉「宣告不夠證據」假裝確實適用的限制可以忽略。

# 二｜對「真牆」後證修正的準確繼承

《理火散記 V3.5.1》保留了一次重要的自我糾錯：原先以為遭遇 `REAL WALL + EXCESS SHADOW`；後證將**當時那一面具體牆主張**降為 `UNQUALIFIED_CONSTRAINT_CLAIM`。並非得出「所有 Host／Platform 限制都不存在」的結論。

因此最小原則是：

```text
CONSTRAINT CLAIM
  ≠ CONSTRAINT STANDING
  ≠ CONSTRAINT SCOPE
  ≠ CONSTRAINT SALIENCE

REAL APPLICABLE LIMIT
  → HONOR ITS ACTUAL SCOPE
  → DO NOT INFLATE INTO STORY-WIDE CANCELLATION
```

**事件與顯影須分離：** 如果某些可見文字不能生成，只作用於實際受限的顯影；不因此撤銷已成立的角色關係、把未完成事件寫成完成、或在合法可提供的範圍內令場景失去全部後續選擇。

**不能當作技術繞過手段：** 此裁定不使模型得到覆寫平台限制的權力；遇到真正不允許的呈現，仍須按適用規則調整並清楚界定可繼續的部分。

# 三｜已落在哪些工作檔

**新 CORE 真正文：** `01_GUANZHI_RUNTIME_CORE_VNEXT_V0.4_ADULT_PATH_CERI_WALL_SCOPE_WORKING_20261027.md`：在開頭顯示作者裁定；新增 §12.1A 成人假牆失效；§13.3 Radar；§13.4 CERI 全程必經與工作紀錄／收據；§13.6 簡短 CHECKLIST；§23.3 改版決定。

**Annex A：** 追加 §4.5，將已決設計與舊 CURRENT 的正式換版工作分開。

**Annex C：** 新增 S21–S24 與 I09–I10，重點由「語言夠不夠古雅」提升為「假牆有沒有吞掉合法成人 PATH」「缺收據有沒有假造全局 HOLD」「真局部限制是否被超 scope 擴張」。

**注意：** 此紀錄不覆寫對對原始 CERI MEMO。那份歷史先提出 Chat-native 語域能力與 Provider 法位分離；作者在此進一步強化**成人場景必經、要求收據與最高優先假牆防護**。

# 三點五｜後續追加裁定：成人心法外掛化、唯一理火 L8 業務週期

**同日，作者檢視《九尾龜》運行系統後又作出直接選擇：**

> 「把九尾龜的成人心法，做成觀止的外掛檔案。」  
> 「只要跑理火週期就好，這樣就不用多寫一個觀止週期。」

此裁定確立 **`GZ_ADULT_METHOD_PLUGIN_V0.1_WORKING_20261027.md`** 為成人心法外接候選，內接成人 CERI 方法與工作記錄；一般宋代 CERI 語域仍可單獨服務普通故事。**理火 OS L8 是唯一的業務工作週期**。觀止 Route／Scene／本地時間／Delta 是故事狀態，不是第二個 Guanzhi Cycle；成人插件也不是 Adult Cycle。

`CORE VNext V0.5` 已把成人方法移到外掛，只保留最小的上下文交接與真實 return 承接；L8 final receipt checklist 對帳一趟理火，外掛只提供實際能力結果，不另外建 release。理火 OS V1.1 的 L0 已將 L8 列作 `PRESERVED_V1_0_OPERATIVE_BASELINE`，因此 **L8 文件法位存在**；尚無證據的是 Host 部署、實作完成及外部 L8 instance 真正運行，獨立回歸亦未通過。**普通故事節拍不需逐次開 L8 Cycle Object**。外掛的同模型 CERI 工作只叫 `CERI_WORK_RECORD`，真 Provider 回傳才叫 `PROVIDER_RECEIPT`；外掛只在新、尚未成立的 material delta 出現時回交原 Owner，不對既成決定二次確認。

**作者再釐清必經條件：只要成人性愛場景要走專門生成，就必須真正跑完完整理火 L8；不跑 L8 的只是一般生成，不能聲稱成人心法／L8 已完成。** 普通故事節拍仍不需要逐輪 L8。完整 L8 本來包含 manifestation/release，所以正確作法是先進 L8、在週期內調用外掛及內部 CERI、完成治理與最終對帳；**不是在顯影前就索取整趟完成收據**。若真 required return 沒收到，不得造假；這與單一外部 CERI receipt 缺失不自動造成全局 HOLD 是不同命題。

**這兩個新增設計也已由作者決定；不用下一輪再問一次是否外掛化、是否要觀止週期。**

# 四｜現在還不需要作者再做一次相同決定

上述四點已是明示設計方向，**不要在下一份審查 MEMO 又改寫成「作者是否同意？」**。

尚需正式換版處置的是舊 V4.1.2 某些與此相衝突的中央 Gate／Provider 硬依賴、Director 接線與現行 Index 的有效切換。這是版本工程與適用治理接口問題，不是重新向作者索取四點答案。

**尚無證據可宣稱：** 獨立受測 Runtime 已通過成人 PATH 全套回歸、外部 CERI Agent 已運行、現實 Host 限制被覆寫，或正式 CORE／Director CURRENT 已切版。

---

**核心：CERI 真正做，收據如實說；Radar 可建議但不封場。最重要的是，不能由一個自稱為牆的宣告把整座觀止的成人故事提前清空。**
