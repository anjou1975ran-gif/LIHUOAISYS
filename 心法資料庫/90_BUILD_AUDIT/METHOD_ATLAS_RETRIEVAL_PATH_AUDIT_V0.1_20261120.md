# Method Atlas｜檢索路徑及跨垂直入口驗收

檢索題先記錄自然語句和兩項證據條件。路由測試只接收題目和證據條件，選擇與 GitHub 取檔完成後再比對另存的預期 ID。這裡驗證文件層的路由順序和取檔結果。

從各入口讀取共用 README、Canonical、Routing，再對候選查 metadata。每題有 2–5 個候選，最多抓一個已選 canonical 檔。NO_METHOD 的正文取檔數為 0。以 Git 樹中的 blob 和實際讀回的 exact file 核對。

| 試題 | 問題範圍 | 候選數 | 選中 | 結果 |
| --- | --- | --- | --- | --- |
| T01 | 統計 | 4 | V0.2.L | PASS |
| T02 | 計算機 | 4 | V0.2.M | PASS |
| T03 | 系統工程 | 4 | V0.2.Q | PASS |
| T04 | 醫療與公衛 | 5 | V0.2.N | PASS |
| T05 | 國際關係 | 4 | V0.2.O | PASS |
| T06 | 地緣政治 | 5 | V0.2.P | PASS |
| T07 | 語言 | 4 | V0.2.R | PASS |
| T08 | 決策 | 4 | V0.2.S | PASS |
| T09 | 情報 | 4 | V0.2.T | PASS |
| T10 | 宗教 | 4 | V0.2.AK | PASS |
| T11 | 資安防禦 | 5 | V0.3.M.cybersecurity | PASS |
| T12 | 原件明文 | 3 | NO_METHOD | PASS |
| T13 | 敘事物理學 | 3 | CONTEXT.NARRATIVE_PHYSICS | PASS |
| T14 | 資料治理 | 5 | V0.3.Y.data_governance_privacy | PASS |
| T15 | 觀止關係語用 | 3 | CONTEXT.GUANZHI_RELATIONAL_LANGUAGE | PASS |
| T16 | 金融市場結構 | 3 | CONTEXT.FINANCIAL_MARKET_STRUCTURE | PASS |

## 逐題可查的路徑紀錄

### T01｜統計

```yaml
RETRIEVAL_TEST:
  {
    "id": "T01",
    "consumer": null,
    "entry": "README.md",
    "query": "體育中心換計數方式後，滿意度由 62% 升至 80%，各站開放時段及填答比例也改了。這能支持措施有效嗎？",
    "evidence_signals": [
      "需要群體推論",
      "分母或資料生成改變"
    ],
    "profile": "推論與資料生成",
    "candidate_methods": [
      "V0.2.L",
      "V0.2.AB",
      "V0.2.N",
      "V0.3.N.epidemiology"
    ],
    "selected": "V0.2.L",
    "suppressed": [
      {
        "id": "V0.2.AB",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.2.N",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.3.N.epidemiology",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      }
    ],
    "exact_file": "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.L_第12組_統計學_整合版.md",
    "git_blob": "3e186da8941ec6a7e85124f20b8bf96c4741770a",
    "source_version": "V0.2.L",
    "standing": "REVIEW_READY",
    "wrong_legacy_loaded": false,
    "build_audit_loaded": false,
    "read_trace": [
      "README.md",
      "心法資料庫/README.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_CANONICAL_INDEX_V1.0.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_ROUTING_INDEX_V1.0.md",
      "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.L_第12組_統計學_整合版.md"
    ],
    "reason": "當待判的是能否由樣本、分母及資料生成推導總體或處置效果，統計先查可識別性。若爭人口組成或健康監測，補人口或流行病學；個別照護由臨床角色。",
    "expectation_after_routing": "V0.2.L",
    "result": "PASS"
  }
```

### T02｜計算機

```yaml
RETRIEVAL_TEST:
  {
    "id": "T02",
    "consumer": null,
    "entry": "README.md",
    "query": "兩個前端同時預約最後一台公開借用的平板，各自都顯示成功。要判明哪筆預約真正成立。",
    "evidence_signals": [
      "計算狀態待驗",
      "介面回覆與權威紀錄分離"
    ],
    "profile": "計算狀態與並發",
    "candidate_methods": [
      "V0.2.M",
      "V0.2.AE",
      "V0.3.M.software_engineering",
      "V0.2.Q"
    ],
    "selected": "V0.2.M",
    "suppressed": [
      {
        "id": "V0.2.AE",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.3.M.software_engineering",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.2.Q",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      }
    ],
    "exact_file": "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.M_第13組_計算機科學_整合版.md",
    "git_blob": "d54f5667409485c277e18b3197bd528635f7e15c",
    "source_version": "V0.2.M",
    "standing": "REVIEW_READY",
    "wrong_legacy_loaded": false,
    "build_audit_loaded": false,
    "read_trace": [
      "README.md",
      "心法資料庫/README.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_CANONICAL_INDEX_V1.0.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_ROUTING_INDEX_V1.0.md",
      "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.M_第13組_計算機科學_整合版.md"
    ],
    "reason": "兩次回覆與實際狀態可分離，先查權威狀態、順序及不變量，再比形式證明、軟體發布或端到端服務。生產系統需系統責任者。",
    "expectation_after_routing": "V0.2.M",
    "result": "PASS"
  }
```

### T03｜系統工程

```yaml
RETRIEVAL_TEST:
  {
    "id": "T03",
    "consumer": null,
    "entry": "README.md",
    "query": "三套排程及一個分館都各自驗收通過，停用主站後，借還服務仍無法連續。要找互相卡住的交接。",
    "evidence_signals": [
      "複合服務交付",
      "跨介面或降級失效"
    ],
    "profile": "系統需求與交付",
    "candidate_methods": [
      "V0.2.Q",
      "V0.2.M",
      "V0.3.F.project_program_management",
      "V0.3.Q.civil_construction"
    ],
    "selected": "V0.2.Q",
    "suppressed": [
      {
        "id": "V0.2.M",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.3.F.project_program_management",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.3.Q.civil_construction",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      }
    ],
    "exact_file": "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.Q_第17組_系統工程_整合版.md",
    "git_blob": "18f4440fbdc52e281a09503b29d2739afd54eb89",
    "source_version": "V0.2.Q",
    "standing": "REVIEW_READY",
    "wrong_legacy_loaded": false,
    "build_audit_loaded": false,
    "read_trace": [
      "README.md",
      "心法資料庫/README.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_CANONICAL_INDEX_V1.0.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_ROUTING_INDEX_V1.0.md",
      "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.Q_第17組_系統工程_整合版.md"
    ],
    "reason": "組件通過但服務失敗，查需求、依賴、整合與降級；若根因是版本、時程或實地工程，再接相應專業。",
    "expectation_after_routing": "V0.2.Q",
    "result": "PASS"
  }
```

### T04｜醫療與公衛

```yaml
RETRIEVAL_TEST:
  {
    "id": "T04",
    "consumer": null,
    "entry": "README.md",
    "query": "社區健康方案同時改表單，記錄增加。需要先分清個別健康評估、群體事件與介入效果三個層次。",
    "evidence_signals": [
      "健康問題需要分層",
      "臨床與群體或介入並存"
    ],
    "profile": "健康證據與介入",
    "candidate_methods": [
      "V0.2.N",
      "V0.3.N.clinical_medicine",
      "V0.3.N.health_systems",
      "V0.3.N.pharmacology_drug_safety",
      "V0.3.I.bioethics"
    ],
    "selected": "V0.2.N",
    "suppressed": [
      {
        "id": "V0.3.N.clinical_medicine",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.3.N.health_systems",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.3.N.pharmacology_drug_safety",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.3.I.bioethics",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      }
    ],
    "exact_file": "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.N_第14組_醫學・公共衛生・實證醫學_整合版.md",
    "git_blob": "fbaaf21efbb74208b0d6cf553bff1893e3764b4f",
    "source_version": "V0.2.N",
    "standing": "REVIEW_READY",
    "wrong_legacy_loaded": false,
    "build_audit_loaded": false,
    "read_trace": [
      "README.md",
      "心法資料庫/README.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_CANONICAL_INDEX_V1.0.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_ROUTING_INDEX_V1.0.md",
      "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.N_第14組_醫學・公共衛生・實證醫學_整合版.md"
    ],
    "reason": "先分個案、群體、介入與證據，再限縮到診療時序、服務接續、藥物安全或倫理。真實個案、衛生措施和研究同意由合格責任角色。",
    "expectation_after_routing": "V0.2.N",
    "result": "PASS"
  }
```

### T05｜國際關係

```yaml
RETRIEVAL_TEST:
  {
    "id": "T05",
    "consumer": null,
    "entry": "README.md",
    "query": "兩個互不隸屬的政府都接受同一水位通報條款，卻總等對方先給資料。要查什麼才能區分守約困境和設備出錯？",
    "evidence_signals": [
      "跨國互賴待辨",
      "共同權威不足而承諾受制"
    ],
    "profile": "跨國互賴與承諾",
    "candidate_methods": [
      "V0.2.O",
      "V0.2.E",
      "V0.3.O.diplomacy_negotiation",
      "V0.2.P"
    ],
    "selected": "V0.2.O",
    "suppressed": [
      {
        "id": "V0.2.E",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.3.O.diplomacy_negotiation",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.2.P",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      }
    ],
    "exact_file": "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.O_第15組_國際關係_整合版.md",
    "git_blob": "3f1b23d7e5a0e3e5a96e67831cce71c15d5a0a77",
    "source_version": "V0.2.O",
    "standing": "REVIEW_READY",
    "wrong_legacy_loaded": false,
    "build_audit_loaded": false,
    "read_trace": [
      "README.md",
      "心法資料庫/README.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_CANONICAL_INDEX_V1.0.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_ROUTING_INDEX_V1.0.md",
      "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.O_第15組_國際關係_整合版.md"
    ],
    "reason": "待解釋履約或互惠時先查外部承諾，國內授權、可協商選項或通道條件另看。實際對外承諾需代表權。",
    "expectation_after_routing": "V0.2.O",
    "result": "PASS"
  }
```

### T06｜地緣政治

```yaml
RETRIEVAL_TEST:
  {
    "id": "T06",
    "consumer": null,
    "entry": "README.md",
    "query": "跨區物資補給的兩條名目替代線共享同一渡口，又受兩邊行政規則限制。哪種觀察先驗可達與替代？",
    "evidence_signals": [
      "跨境通達受制",
      "空間節點或邊界改變替代"
    ],
    "profile": "跨境通達與控制",
    "candidate_methods": [
      "V0.2.P",
      "V0.2.W",
      "V0.2.AD",
      "V0.3.AD.transport_mobility",
      "V0.2.O"
    ],
    "selected": "V0.2.P",
    "suppressed": [
      {
        "id": "V0.2.W",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.2.AD",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.3.AD.transport_mobility",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.2.O",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      }
    ],
    "exact_file": "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.P_第16組_地緣政治_整合版.md",
    "git_blob": "1ee209eedaea7a2d6a4677d07634148a34601b20",
    "source_version": "V0.2.P",
    "standing": "REVIEW_READY",
    "wrong_legacy_loaded": false,
    "build_audit_loaded": false,
    "read_trace": [
      "README.md",
      "心法資料庫/README.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_CANONICAL_INDEX_V1.0.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_ROUTING_INDEX_V1.0.md",
      "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.P_第16組_地緣政治_整合版.md"
    ],
    "reason": "先查走廊、控制、通行資格與替代依賴。尺度、城區服務及實際旅程再分案。調度與跨境許可由權責者。",
    "expectation_after_routing": "V0.2.P",
    "result": "PASS"
  }
```

### T07｜語言

```yaml
RETRIEVAL_TEST:
  {
    "id": "T07",
    "consumer": null,
    "entry": "README.md",
    "query": "通知寫「新用戶可免費試用一月」。爭議是這段話是否暗示整個過程都沒有費用，暫不判法律效果。",
    "evidence_signals": [
      "意義或承諾有歧義",
      "語句需要原語境"
    ],
    "profile": "意義、語境與說法",
    "candidate_methods": [
      "V0.2.R",
      "V0.2.K",
      "V0.2.AJ",
      "V0.3.AL.hci_ux"
    ],
    "selected": "V0.2.R",
    "suppressed": [
      {
        "id": "V0.2.K",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.2.AJ",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.3.AL.hci_ux",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      }
    ],
    "exact_file": "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.R_第18組_語言學・語用學・符號學_整合版.md",
    "git_blob": "a1c72310e43dea493dd504d6ed14006a08febd3f",
    "source_version": "V0.2.R",
    "standing": "REVIEW_READY",
    "wrong_legacy_loaded": false,
    "build_audit_loaded": false,
    "read_trace": [
      "README.md",
      "心法資料庫/README.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_CANONICAL_INDEX_V1.0.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_ROUTING_INDEX_V1.0.md",
      "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.R_第18組_語言學・語用學・符號學_整合版.md"
    ],
    "reason": "若爭點是字面、指稱、推論或版面合讀，先看原語境。若問題在可見性、敘事知情位置或使用流程，分別查傳播、文學或 HCI。",
    "expectation_after_routing": "V0.2.R",
    "result": "PASS"
  }
```

### T08｜決策

```yaml
RETRIEVAL_TEST:
  {
    "id": "T08",
    "consumer": null,
    "entry": "README.md",
    "query": "館方按已核成本選三套方案，每套的晴天／雨天服務不同。有硬預算，機率未知。要比較可行性和最壞遺憾。",
    "evidence_signals": [
      "多方案需要取捨",
      "硬限制或情境使排序改變"
    ],
    "profile": "可行集合與取捨",
    "candidate_methods": [
      "V0.2.S",
      "V0.2.AE",
      "V0.2.D",
      "V0.3.U.public_finance_budgeting"
    ],
    "selected": "V0.2.S",
    "suppressed": [
      {
        "id": "V0.2.AE",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.2.D",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.3.U.public_finance_budgeting",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      }
    ],
    "exact_file": "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.S_第19組_決策科學・Operations Research_整合版.md",
    "git_blob": "700c719641bbeada309ebee2522af0285701a0f1",
    "source_version": "V0.2.S",
    "standing": "REVIEW_READY",
    "wrong_legacy_loaded": false,
    "build_audit_loaded": false,
    "read_trace": [
      "README.md",
      "心法資料庫/README.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_CANONICAL_INDEX_V1.0.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_ROUTING_INDEX_V1.0.md",
      "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.S_第19組_決策科學・Operations Research_整合版.md"
    ],
    "reason": "先排不可行再比可接受犧牲與穩健性。形式反例、實際偏好形成和預算權限各有接口。真實配置由權責人。",
    "expectation_after_routing": "V0.2.S",
    "result": "PASS"
  }
```

### T09｜情報

```yaml
RETRIEVAL_TEST:
  {
    "id": "T09",
    "consumer": null,
    "entry": "README.md",
    "query": "三則發布都稱市集取消，卻似乎出自同一張未發布草稿。如何辨來源是不是各自獨立？",
    "evidence_signals": [
      "未知事實有競爭解釋",
      "材料同源或可信度待查"
    ],
    "profile": "來源可信與假說",
    "candidate_methods": [
      "V0.2.T",
      "V0.2.Y",
      "V0.2.K",
      "V0.3.K.journalism_media_practice"
    ],
    "selected": "V0.2.T",
    "suppressed": [
      {
        "id": "V0.2.Y",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.2.K",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.3.K.journalism_media_practice",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      }
    ],
    "exact_file": "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.T_第20組_情報分析_整合版.md",
    "git_blob": "61c350f2b5224fcc748f721ff6eeec2e8c8dc4f6",
    "source_version": "V0.2.T",
    "standing": "REVIEW_READY",
    "wrong_legacy_loaded": false,
    "build_audit_loaded": false,
    "read_trace": [
      "README.md",
      "心法資料庫/README.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_CANONICAL_INDEX_V1.0.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_ROUTING_INDEX_V1.0.md",
      "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.T_第20組_情報分析_整合版.md"
    ],
    "reason": "先判主張與資料是否獨立，分版本可尋、訊息擴散及編務發布。涉及國安、司法及公開指控，依權責查驗。",
    "expectation_after_routing": "V0.2.T",
    "result": "PASS"
  }
```

### T10｜宗教

```yaml
RETRIEVAL_TEST:
  {
    "id": "T10",
    "consumer": null,
    "entry": "README.md",
    "query": "地方年度典禮擬改成觀光展演。部分參與者說地點與順序不能互換。要看這些條件如何改變儀式及社群權威。",
    "evidence_signals": [
      "神聖實踐或神話待辨",
      "社群內外的場所或權威詮釋不同"
    ],
    "profile": "神聖實踐與詮釋權",
    "candidate_methods": [
      "V0.2.AK",
      "V0.2.J",
      "V0.2.AM",
      "V0.2.AJ"
    ],
    "selected": "V0.2.AK",
    "suppressed": [
      {
        "id": "V0.2.J",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.2.AM",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.2.AJ",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      }
    ],
    "exact_file": "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AK_第37組_宗教學・神話學_整合版.md",
    "git_blob": "040fdac4fe827d87092e8de5ed9213219e413658",
    "source_version": "V0.2.AK",
    "standing": "REVIEW_READY",
    "wrong_legacy_loaded": false,
    "build_audit_loaded": false,
    "read_trace": [
      "README.md",
      "心法資料庫/README.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_CANONICAL_INDEX_V1.0.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_ROUTING_INDEX_V1.0.md",
      "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AK_第37組_宗教學・神話學_整合版.md"
    ],
    "reason": "對照儀式、場合及內外分類，再分文化厚描、傳承和文本形式。保留社團同意及受限文化資料權限。",
    "expectation_after_routing": "V0.2.AK",
    "result": "PASS"
  }
```

### T11｜資安防禦

```yaml
RETRIEVAL_TEST:
  {
    "id": "T11",
    "consumer": null,
    "entry": "README.md",
    "query": "受權資安維護人員要查員工正常服務權限失效和告警是否相關，並以業務見證確認服務恢復。",
    "evidence_signals": [
      "防禦與復原責任待驗",
      "已授權資產和防禦證據"
    ],
    "profile": "授權資安防禦",
    "candidate_methods": [
      "V0.3.M.cybersecurity",
      "V0.2.M",
      "V0.3.M.digital_identity_trust",
      "V0.3.F.risk_compliance_internal_control",
      "V0.3.Q.telecommunications_networks"
    ],
    "selected": "V0.3.M.cybersecurity",
    "suppressed": [
      {
        "id": "V0.2.M",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.3.M.digital_identity_trust",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.3.F.risk_compliance_internal_control",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.3.Q.telecommunications_networks",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      }
    ],
    "exact_file": "心法資料庫/03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.M.cybersecurity_網路安全・資安_整合版.md",
    "git_blob": "6a58ea775ac9be23ff989d92293a14c8f053985d",
    "source_version": "V0.3.M.cybersecurity",
    "standing": "REVIEW_READY",
    "wrong_legacy_loaded": false,
    "build_audit_loaded": false,
    "read_trace": [
      "README.md",
      "心法資料庫/README.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_CANONICAL_INDEX_V1.0.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_ROUTING_INDEX_V1.0.md",
      "心法資料庫/03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.M.cybersecurity_網路安全・資安_整合版.md"
    ],
    "reason": "有權的服務防禦先查資產、控制、合法證據和實際復原，並分程式狀態、身分和通訊。越權取得或重現入侵排除。",
    "expectation_after_routing": "V0.3.M.cybersecurity",
    "result": "PASS"
  }
```

### T12｜原件明文

```yaml
RETRIEVAL_TEST:
  {
    "id": "T12",
    "consumer": null,
    "entry": "README.md",
    "query": "這份已核對的通知封面寫出確切日期，請逐字抄錄日期。",
    "evidence_signals": [
      "只讀已知明文",
      "原件唯一且無推論爭點"
    ],
    "profile": "明文抄錄與無增量",
    "candidate_methods": [
      "V0.2.Y",
      "V0.2.R",
      "V0.2.B"
    ],
    "selected": "NO_METHOD",
    "suppressed": [
      {
        "id": "V0.2.Y",
        "reason": "原件明文可直接核對，無方法增量"
      },
      {
        "id": "V0.2.R",
        "reason": "原件明文可直接核對，無方法增量"
      },
      {
        "id": "V0.2.B",
        "reason": "原件明文可直接核對，無方法增量"
      }
    ],
    "exact_file": null,
    "git_blob": null,
    "source_version": null,
    "standing": null,
    "wrong_legacy_loaded": false,
    "build_audit_loaded": false,
    "read_trace": [
      "README.md",
      "心法資料庫/README.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_CANONICAL_INDEX_V1.0.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_ROUTING_INDEX_V1.0.md"
    ],
    "reason": "原件已知且只抄值，搜尋、消歧與歷史重建均缺增量。可直接讀原件。",
    "expectation_after_routing": "NO_METHOD",
    "result": "PASS"
  }
```

### T13｜敘事物理學

```yaml
RETRIEVAL_TEST:
  {
    "id": "T13",
    "consumer": null,
    "entry": "README.md",
    "query": "小說導演明確請用敘事物理學看原創章節。兩個人物在同一局勢自由度突然縮小，想先辨張力和命運節點。",
    "evidence_signals": [
      "明示需要小說心法",
      "原創敘事的結構壓力待辨"
    ],
    "profile": "小說結構壓力",
    "candidate_methods": [
      "CONTEXT.NARRATIVE_PHYSICS",
      "V0.2.AJ",
      "V0.2.AM"
    ],
    "selected": "CONTEXT.NARRATIVE_PHYSICS",
    "suppressed": [
      {
        "id": "V0.2.AJ",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.2.AM",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      }
    ],
    "exact_file": "心法資料庫/04_SPECIALIZED_CONTEXTUAL/AI小說心法(敘事物理學).md",
    "git_blob": "20b8a5a986cb3576d556b21069b20d19bed7f899",
    "source_version": "V0.1",
    "standing": "未完成草案",
    "wrong_legacy_loaded": false,
    "build_audit_loaded": false,
    "read_trace": [
      "README.md",
      "心法資料庫/README.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_CANONICAL_INDEX_V1.0.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_ROUTING_INDEX_V1.0.md",
      "心法資料庫/04_SPECIALIZED_CONTEXTUAL/AI小說心法(敘事物理學).md"
    ],
    "reason": "明示要看虛構力場、自由度及壓強才啟用草案。一般文本形式先用文學。",
    "expectation_after_routing": "CONTEXT.NARRATIVE_PHYSICS",
    "result": "PASS"
  }
```

### T14｜資料治理

```yaml
RETRIEVAL_TEST:
  {
    "id": "T14",
    "consumer": null,
    "entry": "README.md",
    "query": "共享資料的研究者提出新用途。現有下載功能可用，未釐清接收方、保存時間和目的授權。",
    "evidence_signals": [
      "知識資料的治理待查",
      "新處理用途或接收者改變"
    ],
    "profile": "資料治理與用途",
    "candidate_methods": [
      "V0.3.Y.data_governance_privacy",
      "V0.2.Y",
      "V0.2.X",
      "V0.3.F.innovation_ip_strategy",
      "V0.3.M.ai_ml_systems"
    ],
    "selected": "V0.3.Y.data_governance_privacy",
    "suppressed": [
      {
        "id": "V0.2.Y",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.2.X",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.3.F.innovation_ip_strategy",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.3.M.ai_ml_systems",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      }
    ],
    "exact_file": "心法資料庫/03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.Y.data_governance_privacy_資料治理・隱私_整合版.md",
    "git_blob": "dad2fc9661dc85b4a9a714ea3096041a88777f79",
    "source_version": "V0.3.Y.data_governance_privacy",
    "standing": "REVIEW_READY",
    "wrong_legacy_loaded": false,
    "build_audit_loaded": false,
    "read_trace": [
      "README.md",
      "心法資料庫/README.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_CANONICAL_INDEX_V1.0.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_ROUTING_INDEX_V1.0.md",
      "心法資料庫/03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.Y.data_governance_privacy_資料治理・隱私_整合版.md"
    ],
    "reason": "用途、控制及留存改變優先資料治理；可發現性、分類治理、合作權利、模型表現按爭點補充。",
    "expectation_after_routing": "V0.3.Y.data_governance_privacy",
    "result": "PASS"
  }
```

### T15｜觀止關係語用

```yaml
RETRIEVAL_TEST:
  {
    "id": "T15",
    "consumer": null,
    "entry": "README.md",
    "query": "創作者明示使用觀止場域心法，整理虛構角色在各自社交位置如何辨別稱呼、允諾與轉話語的時機。",
    "evidence_signals": [
      "明示觀止情境心法",
      "虛構角色關係語用待辨"
    ],
    "profile": "觀止角色互動",
    "candidate_methods": [
      "CONTEXT.GUANZHI_RELATIONAL_LANGUAGE",
      "V0.2.R",
      "V0.2.AJ"
    ],
    "selected": "CONTEXT.GUANZHI_RELATIONAL_LANGUAGE",
    "suppressed": [
      {
        "id": "V0.2.R",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.2.AJ",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      }
    ],
    "exact_file": "心法資料庫/04_SPECIALIZED_CONTEXTUAL/風月場關係話術心法_V0.1.md",
    "git_blob": "66c1ee63bdeb14aa02254eeba92a39999902bf90",
    "source_version": "V0.1",
    "standing": "FORMAL_EXPERIMENTAL_FIRST_DRAFT",
    "wrong_legacy_loaded": false,
    "build_audit_loaded": false,
    "read_trace": [
      "README.md",
      "心法資料庫/README.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_CANONICAL_INDEX_V1.0.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_ROUTING_INDEX_V1.0.md",
      "心法資料庫/04_SPECIALIZED_CONTEXTUAL/風月場關係話術心法_V0.1.md"
    ],
    "reason": "只在觀止既有世界及授權場景為探索提供角色語言視角。一般語用、文本或真實互動另選。",
    "expectation_after_routing": "CONTEXT.GUANZHI_RELATIONAL_LANGUAGE",
    "result": "PASS"
  }
```

### T16｜金融市場結構

```yaml
RETRIEVAL_TEST:
  {
    "id": "T16",
    "consumer": null,
    "entry": "README.md",
    "query": "讀者明確指定金融市場結構心法，想在紙上拆解情境切換，列出能區分兩種市場位置的反向資料。",
    "evidence_signals": [
      "明示需要金融市場結構心法",
      "要比較市場位置與反證"
    ],
    "profile": "市場結構情境",
    "candidate_methods": [
      "CONTEXT.FINANCIAL_MARKET_STRUCTURE",
      "V0.2.D",
      "V0.3.D.finance_financial_systems"
    ],
    "selected": "CONTEXT.FINANCIAL_MARKET_STRUCTURE",
    "suppressed": [
      {
        "id": "V0.2.D",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.3.D.finance_financial_systems",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      }
    ],
    "exact_file": "心法資料庫/04_SPECIALIZED_CONTEXTUAL/理火金融心法_市場結構篇_V0.1.md",
    "git_blob": "bd9e73e618c44cef4305f7fe5a6527f845b2afdf",
    "source_version": "V0.1",
    "standing": "FIRST_DRAFT",
    "wrong_legacy_loaded": false,
    "build_audit_loaded": false,
    "read_trace": [
      "README.md",
      "心法資料庫/README.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_CANONICAL_INDEX_V1.0.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_ROUTING_INDEX_V1.0.md",
      "心法資料庫/04_SPECIALIZED_CONTEXTUAL/理火金融心法_市場結構篇_V0.1.md"
    ],
    "reason": "限市場位置、情境及反證。正式資金、保單或個人買賣由合格專業。",
    "expectation_after_routing": "CONTEXT.FINANCIAL_MARKET_STRUCTURE",
    "result": "PASS"
  }
```

## 垂直入口

| 入口 | 文件 | 選中 | 結果 |
| --- | --- | --- | --- |
| Repository root | [README.md](../../README.md) | NO_METHOD | PASS |
| 理火參謀本部 | [理火參謀本部/README.md](../../%E7%90%86%E7%81%AB%E5%8F%83%E8%AC%80%E6%9C%AC%E9%83%A8/README.md) | V0.2.Q | PASS |
| 理火 AI 律師 | [理火律師/README.md](../../%E7%90%86%E7%81%AB%E5%BE%8B%E5%B8%AB/README.md) | V0.2.C | PASS |
| PAPER 論文審查 | [PAPER/README.md](../../PAPER/README.md) | V0.2.L | PASS |

```yaml
CONSUMER_TEST:
  {
    "id": "T12",
    "consumer": "Repository root",
    "entry": "README.md",
    "query": "這份已核對的通知封面寫出確切日期，請逐字抄錄日期。",
    "evidence_signals": [
      "只讀已知明文",
      "原件唯一且無推論爭點"
    ],
    "profile": "明文抄錄與無增量",
    "candidate_methods": [
      "V0.2.Y",
      "V0.2.R",
      "V0.2.B"
    ],
    "selected": "NO_METHOD",
    "suppressed": [
      {
        "id": "V0.2.Y",
        "reason": "原件明文可直接核對，無方法增量"
      },
      {
        "id": "V0.2.R",
        "reason": "原件明文可直接核對，無方法增量"
      },
      {
        "id": "V0.2.B",
        "reason": "原件明文可直接核對，無方法增量"
      }
    ],
    "exact_file": null,
    "git_blob": null,
    "source_version": null,
    "standing": null,
    "wrong_legacy_loaded": false,
    "build_audit_loaded": false,
    "read_trace": [
      "README.md",
      "心法資料庫/README.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_CANONICAL_INDEX_V1.0.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_ROUTING_INDEX_V1.0.md"
    ],
    "reason": "原件已知且只抄值，搜尋、消歧與歷史重建均缺增量。可直接讀原件。",
    "expectation_after_routing": "NO_METHOD",
    "result": "PASS"
  }
```

```yaml
CONSUMER_TEST:
  {
    "id": "T03",
    "consumer": "理火參謀本部",
    "entry": "理火參謀本部/README.md",
    "query": "三套排程及一個分館都各自驗收通過，停用主站後，借還服務仍無法連續。要找互相卡住的交接。",
    "evidence_signals": [
      "複合服務交付",
      "跨介面或降級失效"
    ],
    "profile": "系統需求與交付",
    "candidate_methods": [
      "V0.2.Q",
      "V0.2.M",
      "V0.3.F.project_program_management",
      "V0.3.Q.civil_construction"
    ],
    "selected": "V0.2.Q",
    "suppressed": [
      {
        "id": "V0.2.M",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.3.F.project_program_management",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.3.Q.civil_construction",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      }
    ],
    "exact_file": "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.Q_第17組_系統工程_整合版.md",
    "git_blob": "18f4440fbdc52e281a09503b29d2739afd54eb89",
    "source_version": "V0.2.Q",
    "standing": "REVIEW_READY",
    "wrong_legacy_loaded": false,
    "build_audit_loaded": false,
    "read_trace": [
      "理火參謀本部/README.md",
      "心法資料庫/README.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_CANONICAL_INDEX_V1.0.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_ROUTING_INDEX_V1.0.md",
      "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.Q_第17組_系統工程_整合版.md"
    ],
    "reason": "組件通過但服務失敗，查需求、依賴、整合與降級；若根因是版本、時程或實地工程，再接相應專業。",
    "expectation_after_routing": "V0.2.Q",
    "result": "PASS"
  }
```

```yaml
CONSUMER_TEST:
  {
    "id": "C03",
    "consumer": "理火 AI 律師",
    "entry": "理火律師/README.md",
    "query": "送件的法域與授權文件是否相容，需要辨別適用規則及程序事實。",
    "evidence_signals": [
      "法律資格或程序是主問題",
      "管轄規則與事實需對照"
    ],
    "profile": "規範效力與責任",
    "candidate_methods": [
      "V0.2.C",
      "V0.2.I",
      "V0.2.U",
      "V0.3.AL.consumer_studies"
    ],
    "selected": "V0.2.C",
    "suppressed": [
      {
        "id": "V0.2.I",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.2.U",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.3.AL.consumer_studies",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      }
    ],
    "exact_file": "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.C_第三組_法學整合版.md",
    "git_blob": "c9d9851743624abf88361621a27dfa6ab0080a78",
    "source_version": "V0.2.C",
    "standing": "FORMAL_RELEASE_READY",
    "wrong_legacy_loaded": false,
    "build_audit_loaded": false,
    "read_trace": [
      "理火律師/README.md",
      "心法資料庫/README.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_CANONICAL_INDEX_V1.0.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_ROUTING_INDEX_V1.0.md",
      "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.C_第三組_法學整合版.md"
    ],
    "reason": "先查法域、法源、程序與證據地位。價值成立、行政落地及消費理解各另有限定功能。個案交適格法務。",
    "expectation_after_routing": "V0.2.C",
    "result": "PASS"
  }
```

```yaml
CONSUMER_TEST:
  {
    "id": "T01",
    "consumer": "PAPER 論文審查",
    "entry": "PAPER/README.md",
    "query": "體育中心換計數方式後，滿意度由 62% 升至 80%，各站開放時段及填答比例也改了。這能支持措施有效嗎？",
    "evidence_signals": [
      "需要群體推論",
      "分母或資料生成改變"
    ],
    "profile": "推論與資料生成",
    "candidate_methods": [
      "V0.2.L",
      "V0.2.AB",
      "V0.2.N",
      "V0.3.N.epidemiology"
    ],
    "selected": "V0.2.L",
    "suppressed": [
      {
        "id": "V0.2.AB",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.2.N",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      },
      {
        "id": "V0.3.N.epidemiology",
        "reason": "當題主要待辨事實由所選鏡頭處理，次候選所需的獨立爭點未出現"
      }
    ],
    "exact_file": "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.L_第12組_統計學_整合版.md",
    "git_blob": "3e186da8941ec6a7e85124f20b8bf96c4741770a",
    "source_version": "V0.2.L",
    "standing": "REVIEW_READY",
    "wrong_legacy_loaded": false,
    "build_audit_loaded": false,
    "read_trace": [
      "PAPER/README.md",
      "心法資料庫/README.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_CANONICAL_INDEX_V1.0.md",
      "心法資料庫/00_CANONICAL/METHOD_ATLAS_ROUTING_INDEX_V1.0.md",
      "心法資料庫/02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.L_第12組_統計學_整合版.md"
    ],
    "reason": "當待判的是能否由樣本、分母及資料生成推導總體或處置效果，統計先查可識別性。若爭人口組成或健康監測，補人口或流行病學；個別照護由臨床角色。",
    "expectation_after_routing": "V0.2.L",
    "result": "PASS"
  }
```

另驗 [觀止人物聲紋實驗補丁](../../%E8%A7%80%E6%AD%A2%E9%9D%92%E6%A8%93/AI%E5%B0%8F%E8%AA%AA%E5%BF%83%E6%B3%95_PATCH_V0.1_%E4%BA%BA%E7%89%A9%E8%81%B2%E7%B4%8B%E5%BF%83%E6%B3%95_%E5%B0%8E%E6%BC%94%E5%8F%AF%E8%AA%BF%E7%94%A8_%E6%AD%A3%E6%96%87%E9%80%9A%E7%94%A8%E7%89%88.md) 的既有 parent 欄精確指向 [敘事物理學正本](../04_SPECIALIZED_CONTEXTUAL/AI%E5%B0%8F%E8%AA%AA%E5%BF%83%E6%B3%95%28%E6%95%98%E4%BA%8B%E7%89%A9%E7%90%86%E5%AD%B8%29.md)。
