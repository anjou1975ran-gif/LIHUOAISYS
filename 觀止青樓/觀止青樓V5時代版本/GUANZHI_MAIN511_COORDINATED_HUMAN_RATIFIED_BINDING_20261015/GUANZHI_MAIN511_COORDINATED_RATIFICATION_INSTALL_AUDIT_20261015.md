# GUANZHI × Main 5.1.1｜協調批准與安裝檢查

本報告記錄已製作的文件、SHA 檢查及尚未完成的外部步驟。

```json
{
  "ratification_event": "GUANZHI_MAIN511_HUMAN_COORDINATED_RATIFICATION_20261015",
  "human_ratification_record": {
    "filename": "GUANZHI_MAIN511_HUMAN_RATIFICATION_BINDING_20261015.md",
    "sha256": "4a2a5f927a1790cc1f05422e19c4390f9007952b67b227ff87f4c1c693716699"
  },
  "core": {
    "filename": "01_GUANZHI_RUNTIME_CORE_V4.1.2_MAIN511_REBIND_HUMAN_RATIFIED_FULL_20261015.md",
    "sha256": "b756fbb7308781ca6ec0ca2d982778f32d12aa87de04d4072741bc851f5782bf",
    "candidate_sha256": "a2b4863a210fbec2375f0f4a914f8a2d0e68273cb08f56ed2e1edba5a68e4de6"
  },
  "director": {
    "filename": "03_GUANZHI_DIRECTOR_V4.1.2_MAIN511_REBIND_HUMAN_RATIFIED_FULL_20261015.md",
    "sha256": "d21611e8256ba0b24f8b8f3b87f8d62ca424de1262da6c7c43f538fb454b0696",
    "candidate_sha256": "c1a29ba3b4283c96362728e4037f346ac31a47288f7351016de0eb7af132ed90"
  },
  "world": {
    "filename": "02_GUANZHI_WORLD_V2.3.2_MAIN511_POINTER_HUMAN_RATIFIED_FULL_20261015.md",
    "sha256": "16cd1ef80dc0db94a0bd53ea7aaf5ecd34444071461ace776f72657d637dffc9",
    "candidate_sha256": "932fec2533ffe42df036543e044ba77debbdd5ac0027a5cc07e551fe94c60ddb"
  },
  "local_binding_index": {
    "filename": "GUANZHI_STACK_COORDINATED_BINDING_INDEX_MAIN511_20261015.md",
    "sha256": "47b9e225b909142b1cba37a9bf7c8d6fbdc970a6b2e23bb7b9bf5093557aad9b"
  },
  "upstream_sha256": {
    "protocol": "b0cf16f39f8aa0d971068cdf09b06039e66640c2545a8f7810ee1d216597acee",
    "lighter": "1b64aeb40be2ae514e25ea15da653d8b41edd20472df57f9f2f49b320a1b7a10",
    "main": "63f89f211f5eca8f850438a3d75265e810c7e320ab62d3859b20886082234129"
  },
  "evidence": {
    "human_ratification": "VERIFIED_FROM_CURRENT_USER_MESSAGE",
    "local_sha_consistency": "PASS",
    "candidate_and_parents_embedded": "PASS",
    "central_index": "NOT_VERIFIED",
    "project_repository_swap": "NOT_PERFORMED",
    "host_runtime": "NOT_ESTABLISHED"
  }
}
```

## 待核驗之非文件步驟

1. 取得中央 LIHUO_STACK_CURRENT_INDEX 對 Main V5.1.1 的有效精確版本解析，或其適格外部 Ratification Binding；不能由觀止附屬索引取代。
2. 將三份協調批准版安裝／替換至有權的專案正式四主檔存放處，原 V4.1.1 留作歷史。人物池不修改。
3. 由真實的 Core/Reference Executor/Lighter/Main 及各 Owner 進行完整單週期整合驗證；未返回之前不得宣稱 Story Dispatch、Release 或 SAVE 成功。
