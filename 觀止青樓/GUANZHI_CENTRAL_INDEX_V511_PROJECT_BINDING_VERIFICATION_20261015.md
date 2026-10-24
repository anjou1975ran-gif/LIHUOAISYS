# GUANZHI × LIHUO MAIN V5.1.1｜中央 Index 核驗補充紀錄

**日期：** 2026-10-15（Asia/Taipei）  
**性質：** 已批准的觀止接線包之後證補充；只更新中央 Index **可查核證據**，不改寫既有批准主檔，不製造 Runtime Receipt。  
**來源：** 目前《觀止青樓（新）》專案對話提供的文件，**不是 GitHub**。

## 本次取得之中央權威索引

```yaml
CENTRAL_INDEX_VERIFICATION:
  result: VERIFIED_FROM_USER_PROVIDED_DOCUMENTS
  current_index:
    file: 90_LIHUO_STACK_CURRENT_INDEX_V5.1.1_ACTIVE_20261015.md
    sha256: "98ffcfab9cc8729faff2966baab09b4f01a1712bc37791c8f26246102069949a"
    status: [ACTIVE, HUMAN_RATIFIED, DOCUMENT_LEVEL_CURRENT, NOT_HOST_DEPLOYMENT, NOT_RUNTIME_RECEIPT]
  ratification_record:
    file: 91_LIHUO_MAIN_V5.1.1_RATIFICATION_RECORD_20261015.md
    sha256: "460386631aabdb179d068a9f2393becf19dd89293db9120cdefc630b97a57fc1"
  main_patch_manifest:
    file: 90_LIHUO_STACK_V5.1.1_MAIN_PATCH_RATIFIED_MANIFEST_20261015.md
    sha256: "787bbe727e70caf04c9cfc898c1c572efbd83e6389476f2ed6a16835d22b4c37"
  resolved_tuple:
    protocol:
      exact: LIHUO_PROTOCOL_V5.1.0
      sha256: "b0cf16f39f8aa0d971068cdf09b06039e66640c2545a8f7810ee1d216597acee"
    lighter:
      exact: LIHUO_LIGHTER_V5.1.0
      sha256: "1b64aeb40be2ae514e25ea15da653d8b41edd20472df57f9f2f49b320a1b7a10"
    main:
      exact: LIHUO_MAIN_V5.1.1
      sha256: "63f89f211f5eca8f850438a3d75265e810c7e320ab62d3859b20886082234129"
```

## 觀止側批准接線核驗

```yaml
GUANZHI_COMPANION_BINDING:
  previous_binding_index:
    file: GUANZHI_STACK_COORDINATED_BINDING_INDEX_MAIN511_20261015.md
    sha256: "47b9e225b909142b1cba37a9bf7c8d6fbdc970a6b2e23bb7b9bf5093557aad9b"
    central_index_status_recorded_at_creation: UNVERIFIED
    superseding_evidence_for_that_field: CENTRAL_INDEX_VERIFICATION_ABOVE
  core:
    version: GUANZHI_RUNTIME_CORE_V4.1.2
    file: 01_GUANZHI_RUNTIME_CORE_V4.1.2_MAIN511_REBIND_HUMAN_RATIFIED_FULL_20261015.md
    sha256: "b756fbb7308781ca6ec0ca2d982778f32d12aa87de04d4072741bc851f5782bf"
  director:
    version: GUANZHI_DIRECTOR_V4.1.2
    file: 03_GUANZHI_DIRECTOR_V4.1.2_MAIN511_REBIND_HUMAN_RATIFIED_FULL_20261015.md
    sha256: "d21611e8256ba0b24f8b8f3b87f8d62ca424de1262da6c7c43f538fb454b0696"
  world:
    version: GUANZHI_WORLD_V2.3.2
    file: 02_GUANZHI_WORLD_V2.3.2_MAIN511_POINTER_HUMAN_RATIFIED_FULL_20261015.md
    sha256: "16cd1ef80dc0db94a0bd53ea7aaf5ecd34444071461ace776f72657d637dffc9"
  character_pool:
    version: LCAPG_V3.3.20
    sha256: "4bea6ad2383ef76e9d5cdae0389ddbe7962d92c39cf798acc270ba3a03c4df95"
  document_pointer_consistency: PASS
  central_main_tuple_consistency: PASS
```

## 分開記錄的資格與剩餘事項

- **已取得：** 使用者提供的中央 `ACTIVE` Current Index、Main 批准紀錄、Manifest；其內容的版本 tuple 與 SHA 符合現行觀止批准接線文件；本地實際檔案 hashes 核對一致。
- **未宣稱：** 已將三份更新後的觀止檔案覆寫成 Project 知識庫當前主檔、外部宿主安裝、Core Ingress、各 Owner Executor 執行、Main Receipt、Lighter Release、SAVE Commit。
- **項目來源澄清：** 所謂「專案倉庫」係此 ChatGPT 專案的文件來源，不應無使用者授權誤指 GitHub 倉庫；舊核驗紀錄中「缺乏 GitHub 觀止主倉庫」的阻塞判斷撤回。
- **歷史保全：** 先前批准文件內 `central_current_index_resolution: NOT_VERIFIED` 只表示當時未取得中央索引；不能直接改寫舊批准文件來假裝當時已有後證。本補充紀錄提供今日的新證據。

**結論：** 中央版本解析缺口已解除；目前可在文件層把 LIHUO Protocol V5.1.0、Lighter V5.1.0、Main V5.1.1 與觀止 Core/Director V4.1.2、World V2.3.2、LCAPG V3.3.20 對齊。但這並非 Runtime 執行放行。
