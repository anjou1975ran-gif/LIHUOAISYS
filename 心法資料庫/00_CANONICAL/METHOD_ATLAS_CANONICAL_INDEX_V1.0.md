# Method Atlas｜Canonical Index V1.0

這是 LIHUOAISYS 根層共用資料庫的唯一 canonical registry。各垂直依原有授權調閱。欄位 `default_retrieval` 指候選選定後唯一預設來源。讀取時鎖定當次 Git ref、精確路徑、來源版本與 blob。

整庫 census 為 **39 Main + 51 Functional = 90**。先前 Final Build Report 的 **79** 是該次新增批次。3 個情境心法組成獨立的限定調閱目錄。

```yaml
ATLAS_STANDING:
  canonical_home: /心法資料庫/
  previous_home: /理火參謀本部/心法區/
  ownership: LIHUOAISYS_ROOT_SHARED_METHOD_DATABASE
  main_method_packs:
    existing_A_K: 11
    new_wave: 28
    total: 39
  functional_modules: 51
  total_method_assets: 90
  specialized_contextual:
    count: 3
    included_in_90: false
  new_build:
    standing: BUILD COMPLETE / REVIEW READY
    ratified: false
    ordinary_runtime_authorization: per_vertical
  legacy:
    load_by_default: false
  build_audit:
    method_source: false
    audit_source: true
    load_by_default: false
```

## Main Pack Registry

```yaml
MAIN_PACK_REGISTRY:
- id: V0.2.A
  name: 社會學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: CLEAN_STANDALONE_PACK_READY
  source_version: V0.2.A
  first_sees: 個體行動所在的群體、場域、規範、分層與制度位置
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.A_第一組_社會學心法包_純淨版.md
  git_blob: 72b47c9f45008ddbae0e377a68d790f38b8485c4
  neighbors:
  - V0.2.J
  - V0.2.G
  - V0.2.E
  default_retrieval: true
- id: V0.2.B
  name: 歷史學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: FORMAL_RELEASE_INTEGRATED
  source_version: V0.2.B
  first_sees: 史料的來源、形成的時間尺度、歷史路徑與制度轉化
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.B_第二組_歷史學整合版.md
  git_blob: 6362cab9baba205d7dafd058bec869da7898b1d1
  neighbors:
  - V0.2.A
  - V0.2.J
  - V0.2.I
  default_retrieval: true
- id: V0.2.C
  name: 法學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: FORMAL_RELEASE_READY
  source_version: V0.2.C
  first_sees: 法域、法源、權利主體、證據資格與程序狀態
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.C_第三組_法學整合版.md
  git_blob: c9d9851743624abf88361621a27dfa6ab0080a78
  neighbors:
  - V0.2.E
  - V0.2.I
  - V0.2.R
  default_retrieval: true
- id: V0.2.D
  name: 經濟學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: FORMAL_RELEASE_READY
  source_version: V0.2.D
  first_sees: 稀缺、邊際選擇、交換條件、價格及風險或分配
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.D_第四組_經濟學整合版.md
  git_blob: 66953c83ca7d9a96b974b634dd9fb5ea99e0051e
  neighbors:
  - V0.2.S
  - V0.2.F
  - V0.2.A
  default_retrieval: true
- id: V0.2.E
  name: 政治學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: FORMAL_RELEASE
  source_version: V0.2.E
  first_sees: 權力取得、機關分工、集體決策、制衡與政治正當性
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.E_第五組_政治學整合版.md
  git_blob: 43eba96ef8be74250d4c476132c9c556e94556cd
  neighbors:
  - V0.2.U
  - V0.2.C
  - V0.2.O
  default_retrieval: true
- id: V0.2.F
  name: 管理學
  class: MAIN_METHOD_PACK
  layer: L2
  standing: INTEGRATED_DRAFT
  source_version: V0.2.F-INTEGRATED
  first_sees: 組織目標、權責、流程、執行與回饋如何配合
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄 V0.2.F-INTEGRATED_第六組_管理學整合版.md
  git_blob: 0380457b6e33e1b73e73a36e139ccd03ef95d0f6
  neighbors:
  - V0.2.Q
  - V0.2.D
  - V0.2.U
  default_retrieval: true
- id: V0.2.G
  name: 心理學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: INTEGRATED_DRAFT
  source_version: V0.2.G-INTEGRATED
  first_sees: 認知、情緒、動機、發展、互動情境與個體學習
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.G-INTEGRATED_第七組心理學整合版.md
  git_blob: 7ad8a579bec7442a9289e19b5e29f5e60cdafb8f
  neighbors:
  - V0.2.A
  - V0.2.H
  - V0.2.N
  default_retrieval: true
- id: V0.2.H
  name: 教育學
  class: MAIN_METHOD_PACK
  layer: L2
  standing: INTEGRATED_DRAFT
  source_version: V0.2.H-INTEGRATED
  first_sees: 教育目的、課程、學習環境、評量及制度化能力形成
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.H-INTEGRATED_第八組教育學整合版.md
  git_blob: 9a8cfd51ed115333a732f0f688ac2f73842d4850
  neighbors:
  - V0.2.G
  - V0.2.A
  - V0.2.AL
  default_retrieval: true
- id: V0.2.I
  name: 哲學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: INTEGRATED_RELEASE
  source_version: V0.2.I-INTEGRATED
  first_sees: 概念、知識條件、論證、價值前提及其推論邊界
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.I-INTEGRATED_第九組哲學整合版.md
  git_blob: 866ea2d132c8915d7d0820520523d118b48e43e0
  neighbors:
  - V0.2.C
  - V0.2.AE
  - V0.2.R
  default_retrieval: true
- id: V0.2.J
  name: 人類學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: FORMAL_RELEASE_READY
  source_version: V0.2.J-INTEGRATED
  first_sees: 日常實踐、在地分類、關係權力、物件使用與厚描
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.J-INTEGRATED_第十組人類學整合版.md
  git_blob: 311b12fb74d9b64e729bb8733438b4d4184427b4
  neighbors:
  - V0.2.A
  - V0.2.AK
  - V0.2.B
  default_retrieval: true
- id: V0.2.K
  name: 傳播學
  class: MAIN_METHOD_PACK
  layer: L2
  standing: FORMAL_INTEGRATED_VERSION
  source_version: V0.2.K-INTEGRATED
  first_sees: 誰向誰說、經過哪個媒介與框架、受眾怎樣接收及擴散
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.K-INTEGRATED_第十一組傳播學整合版.md
  git_blob: c8c8b514941556409040c7a7c6561365ae74e514
  neighbors:
  - V0.2.R
  - V0.2.T
  - V0.2.Y
  default_retrieval: true
- id: V0.2.L
  name: 統計學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  source_version: V0.2.L
  first_sees: 先辨認 estimand、分母和資料生成過程，再問觀察差異有多少來自選取、量測、隨機波動或處置。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.L_第12組_統計學_整合版.md
  git_blob: 3e186da8941ec6a7e85124f20b8bf96c4741770a
  neighbors:
  - V0.2.D
  - V0.2.G
  default_retrieval: true
- id: V0.2.M
  name: 計算機科學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  source_version: V0.2.M
  first_sees: 找輸入如何表示、何處存放權威狀態、操作須維持哪些不變量，再問資源界線與失敗可觀測性。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.M_第13組_計算機科學_整合版.md
  git_blob: d54f5667409485c277e18b3197bd528635f7e15c
  neighbors:
  - V0.2.F
  - V0.2.L
  default_retrieval: true
- id: V0.2.N
  name: 醫學／公共衛生／實證醫學
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  source_version: V0.2.N
  first_sees: 先確定眼前是單人診療、群體健康監測，或介入效果問題。辨認誰在風險中、什麼可測、何時需有責任的專業者。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.N_第14組_醫學・公共衛生・實證醫學_整合版.md
  git_blob: fbaaf21efbb74208b0d6cf553bff1893e3764b4f
  neighbors:
  - V0.2.L
  - V0.2.Q
  default_retrieval: true
- id: V0.2.O
  name: 國際關係
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  source_version: V0.2.O
  first_sees: 找跨境互賴中沒有共同上級可保證履約的行為者，定位承諾、可觀察性和認同如何改變互動。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.O_第15組_國際關係_整合版.md
  git_blob: 3f1b23d7e5a0e3e5a96e67831cce71c15d5a0a77
  neighbors:
  - V0.2.E
  - V0.2.C
  default_retrieval: true
- id: V0.2.P
  name: 地緣政治
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  source_version: V0.2.P
  first_sees: 把行政邊界、實際通達網絡與跨境管制分開，找哪些路徑、節點和依賴塑造可選行動。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.P_第16組_地緣政治_整合版.md
  git_blob: 1ee209eedaea7a2d6a4677d07634148a34601b20
  neighbors:
  - V0.2.O
  - V0.2.Q
  default_retrieval: true
- id: V0.2.Q
  name: 系統工程
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  source_version: V0.2.Q
  first_sees: 從服務任務倒推需求、工作介面與生命週期驗證，定位哪個局部合格仍可使整體失效。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.Q_第17組_系統工程_整合版.md
  git_blob: 18f4440fbdc52e281a09503b29d2739afd54eb89
  neighbors:
  - V0.2.M
  - V0.2.F
  default_retrieval: true
- id: V0.2.R
  name: 語言學／語用學／符號學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  source_version: V0.2.R
  first_sees: 先固定話語、指稱、語境及符號呈現，再分字面內容、語用推論和由介面構成的意義。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.R_第18組_語言學・語用學・符號學_整合版.md
  git_blob: a1c72310e43dea493dd504d6ed14006a08febd3f
  neighbors:
  - V0.2.K
  - V0.2.C
  default_retrieval: true
- id: V0.2.S
  name: 決策科學／Operations Research
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  source_version: V0.2.S
  first_sees: 把可控選項、不可違限制、多目標與不確定性列清楚，先問可行集合，再問偏好與後悔。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.S_第19組_決策科學・Operations Research_整合版.md
  git_blob: 700c719641bbeada309ebee2522af0285701a0f1
  neighbors:
  - V0.2.D
  - V0.2.L
  default_retrieval: true
- id: V0.2.T
  name: 情報分析
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  source_version: V0.2.T
  first_sees: 先列所需判斷及競爭假說，為每項材料追原始可知性、依賴、偏差與缺口。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.T_第20組_情報分析_整合版.md
  git_blob: 61c350f2b5224fcc748f721ff6eeec2e8c8dc4f6
  neighbors:
  - V0.2.K
  - V0.2.L
  default_retrieval: true
- id: V0.2.U
  name: 公共政策／公共行政
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  source_version: V0.2.U
  first_sees: 畫從公共問題到利害關係人接觸的實施鏈，定位每一交接的裁量、資源與回饋。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.U_第21組_公共政策・公共行政_整合版.md
  git_blob: 5d4dc727b782c3a699687d8ef8144ca816c74e05
  neighbors:
  - V0.2.E
  - V0.2.F
  - V0.2.S
  default_retrieval: true
- id: V0.2.V
  name: 安全研究
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  source_version: V0.2.V
  first_sees: 先標何人或何物受威脅、實質風險與緊急化說法如何作用、誰承擔措施代價
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.V_第22組_安全研究_整合版.md
  git_blob: 7aab272580b2dc70ba990ebad3902c7b38fb4259
  neighbors:
  - V0.2.O
  - V0.2.T
  default_retrieval: true
- id: V0.2.W
  name: 地理學／空間研究
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  source_version: V0.2.W
  first_sees: 先確定現象的空間單位、尺度、連通和地方條件。確認換界線或量尺會否改圖樣
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.W_第23組_地理學・空間研究_整合版.md
  git_blob: 78712dc2aa0f25a9f2faf65548cd0f2ce3b2db1d
  neighbors:
  - V0.2.P
  - V0.2.L
  default_retrieval: true
- id: V0.2.X
  name: 科技與社會研究 STS
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  source_version: V0.2.X
  first_sees: 先追技術分類、使用規範、權威和救濟怎樣在採用中互相塑造
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.X_第24組_科技與社會研究 STS_整合版.md
  git_blob: e54e417fe6e8bf780ff9281d6d708f7d1ee93a87
  neighbors:
  - V0.2.Q
  - V0.2.A
  default_retrieval: true
- id: V0.2.Y
  name: 資訊科學／知識組織
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  source_version: V0.2.Y
  first_sees: 先問使用者在什麼詞彙及權限下，能否找到、辨認並追溯所需的知識物件
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.Y_第25組_資訊科學・知識組織_整合版.md
  git_blob: 92b9513550d2fc7a38f0dd69e90829d8404cefa5
  neighbors:
  - V0.2.M
  - V0.2.R
  default_retrieval: true
- id: V0.2.Z
  name: 犯罪學／刑事司法研究
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  source_version: V0.2.Z
  first_sees: 把實際被害、報案、警察紀錄、裁判及處遇結果分開，追群體及流程如何改變觀察
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.Z_第26組_犯罪學・刑事司法研究_整合版.md
  git_blob: f19df6b48e8a5adfdd6b7641a8b38ebf503f4d01
  neighbors:
  - V0.2.C
  - V0.2.L
  default_retrieval: true
- id: V0.2.AA
  name: 社會工作／社會政策
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  source_version: V0.2.AA
  first_sees: 先聽當事人目標，重建人與環境、實際關係、服務缺口及可行支持
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AA_第27組_社會工作・社會政策_整合版.md
  git_blob: 6ec8da71490449dc005a5ff93781fc192e41baf9
  neighbors:
  - V0.2.N
  - V0.2.U
  default_retrieval: true
- id: V0.2.AB
  name: 人口學／人口研究
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  source_version: V0.2.AB
  first_sees: 先區分人口存量、期間流量、風險暴露及世代替換，問總量變化來自組成或率
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AB_第28組_人口學・人口研究_整合版.md
  git_blob: af4038fac6a12813965a2b4f1e021f32533005b1
  neighbors:
  - V0.2.L
  - V0.2.AA
  default_retrieval: true
- id: V0.2.AC
  name: 環境／氣候／生態系統研究
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  source_version: V0.2.AC
  first_sees: 先畫壓力、受體、暴露、系統邊界與反事實基線，追變動跨時間和上下游的累積
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AC_第29組_環境・氣候・生態系統研究_整合版.md
  git_blob: 88b0f8255a2d0147ed28d8eb7d3322456e1a7068
  neighbors:
  - V0.2.W
  - V0.2.L
  default_retrieval: true
- id: V0.2.AD
  name: 都市／建成環境研究
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  source_version: V0.2.AD
  first_sees: 先追土地、建物、公共空間、運輸和住房如何共同形成實住、可達與外部影響
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AD_第30組_都市・建成環境研究_整合版.md
  git_blob: 41ebfcd046a75a081531ad2e1cb8ce34bda3d968
  neighbors:
  - V0.2.W
  - V0.2.Q
  default_retrieval: true
- id: V0.2.AE
  name: 數學／形式方法
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  source_version: V0.2.AE
  first_sees: 先寫定義、量詞、約束和可證性。找最小反例及哪些結論僅在模型內成立
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AE_第31組_數學・形式方法_整合版.md
  git_blob: 4b5e6498f224cce3941c8654f80bcf7a439eed3b
  neighbors:
  - V0.2.M
  - V0.2.S
  default_retrieval: true
- id: V0.2.AF
  name: 生物學／生命科學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  source_version: V0.2.AF
  first_sees: 先辨生物層級和性狀。區分個體、發育經驗、環境反應、族群組成及代際變化
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AF_第32組_生物學・生命科學_整合版.md
  git_blob: 2263acca93cae3ed6173f2036f26c8635167d588
  neighbors:
  - V0.2.AC
  - V0.2.N
  default_retrieval: true
- id: V0.2.AG
  name: 物理學／物理系統
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  source_version: V0.2.AG
  first_sees: 先界定物理系統邊界、守恆量、驅動和時間尺度，問模型允許哪些變化
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AG_第33組_物理學・物理系統_整合版.md
  git_blob: 2a64b4bafa2f7e6ae2e65aeb7ec70ce81e90b44e
  neighbors:
  - V0.2.AE
  - V0.2.Q
  default_retrieval: true
- id: V0.2.AH
  name: 化學／材料科學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  source_version: V0.2.AH
  first_sees: 先定位物質身分、組成與微結構、加工履歷、暴露及量到的性能，辨候選變化路徑
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AH_第34組_化學・材料科學_整合版.md
  git_blob: 8c19bfa56b1edb13443505b8e2027752a6ec191d
  neighbors:
  - V0.2.AG
  - V0.2.Q
  default_retrieval: true
- id: V0.2.AI
  name: 地球科學／地質與地球系統
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  source_version: V0.2.AI
  first_sees: 先重建地層、水、地形和演變，分地表現象、深度來源和跨期地球過程
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AI_第35組_地球科學・地質與地球系統_整合版.md
  git_blob: 2c15d37f77487e6c0531dc6bf60d4f663aa75056
  neighbors:
  - V0.2.AC
  - V0.2.AG
  default_retrieval: true
- id: V0.2.AJ
  name: 文學／敘事學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  source_version: V0.2.AJ
  first_sees: 先拆事件、講述者、誰可知與讀者何時獲知，再問形式如何組織意義
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AJ_第36組_文學・敘事學_整合版.md
  git_blob: 8468c97d879023225b3da9def1d416e56b32b1b5
  neighbors:
  - V0.2.R
  - V0.2.B
  default_retrieval: true
- id: V0.2.AK
  name: 宗教學／神話學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  source_version: V0.2.AK
  first_sees: 先看參與者如何使實踐、敘事、場所及時間取得神聖或共同體意義，保留各種位置
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AK_第37組_宗教學・神話學_整合版.md
  git_blob: 040fdac4fe827d87092e8de5ed9213219e413658
  neighbors:
  - V0.2.J
  - V0.2.AJ
  default_retrieval: true
- id: V0.2.AL
  name: 設計學／Human-Centered Design
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  source_version: V0.2.AL
  first_sees: 先觀察人的工作、情境、障礙及修正行動，原型能否實際讓對象完成正確任務
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AL_第38組_設計學・Human-Centered Design_整合版.md
  git_blob: 8bc2425a734a25bd77297b71b742bf72e90fda0d
  neighbors:
  - V0.2.G
  - V0.2.Q
  default_retrieval: true
- id: V0.2.AM
  name: 藝術／文化／文化遺產研究
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  source_version: V0.2.AM
  first_sees: 先辨視覺表現、物件來源、場所價值與活態傳承，問一次改造或展示會保留並抹去哪一層
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AM_第39組_藝術・文化・文化遺產研究_整合版.md
  git_blob: 43647fc954b09fd142aabac59a4c333a709daf4d
  neighbors:
  - V0.2.AK
  - V0.2.AH
  default_retrieval: true
```

## Functional Module Registry

```yaml
FUNCTIONAL_MODULE_REGISTRY:
- id: V0.3.A.labor_industrial_relations
  name: 勞動／工業關係
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.A.labor_industrial_relations
  first_sees: 先比契約、實際指揮及集體接入
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.A.labor_industrial_relations_勞動・工業關係_整合版.md
  git_blob: 63d2d8601dc13cedc33ecf34fcd966c18d392b37
  neighbors:
  - V0.2.A
  - V0.3.F.organizational_behavior_hr
  default_retrieval: true
  parent_method: V0.2.A
  trigger:
  - 契約形式與工作實況不合
  - 代表與執行範圍有缺口
  suppress:
  - 只查章程日期
  professional_support_trigger:
  - 實際勞動資格、仲裁及工作安全由勞務專業與授權代表。
- id: V0.3.AA.aging_gerontology
  name: 高齡／老年學
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.AA.aging_gerontology
  first_sees: 分年齡、功能、意願與環境支持
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AA.aging_gerontology_高齡・老年學_整合版.md
  git_blob: 2f311273ab4f85fd0e8cd8ec9fac962c6d2e70bb
  neighbors:
  - V0.2.AA
  - V0.2.N
  default_retrieval: true
  parent_method: V0.2.AA
  trigger:
  - 活動下降未確認功能
  - 長期支持條件在變
  suppress:
  - 只檢程序文件
  professional_support_trigger:
  - 個案健康、決策能力與長照由具資格專業及當事人決定。
- id: V0.3.AA.care_systems
  name: 照護系統
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.AA.care_systems
  first_sees: 分照護需求、交接、可提供時間與回饋
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AA.care_systems_照護系統_整合版.md
  git_blob: fb13c94e3031681551c77173edacdd816d67d660
  neighbors:
  - V0.2.AA
  - V0.2.N
  default_retrieval: true
  parent_method: V0.2.AA
  trigger:
  - 跨單位照護或身分變動
  - 無確認責任接手
  suppress:
  - 只問已核發文人
  professional_support_trigger:
  - 照護處遇、臨床、危機及保密均交具責任者。
- id: V0.3.AA.child_development_protection
  name: 兒少發展／保護
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.AA.child_development_protection
  first_sees: 先定位年齡處境、兒少意見及保護授權
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AA.child_development_protection_兒少發展・保護_整合版.md
  git_blob: 90322d61df6672b0fb4edc3fdea38b0f879388c9
  neighbors:
  - V0.2.AA
  - V0.2.H
  default_retrieval: true
  parent_method: V0.2.AA
  trigger:
  - 兒少意見沒有進入決策
  - 保護紀錄有轉介缺口
  suppress:
  - 純文件擷取
  professional_support_trigger:
  - 實際安全危機、保護評估、通報、照護與個案資料交授權保護或醫療法律人員。
- id: V0.3.AA.disability_studies
  name: 障礙研究
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.AA.disability_studies
  first_sees: 分活動、功能、環境和制度障礙
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AA.disability_studies_障礙研究_整合版.md
  git_blob: 812dafab5b0e2c6fcb41f8416ff579df4b663721
  neighbors:
  - V0.2.AA
  - V0.2.AL
  default_retrieval: true
  parent_method: V0.2.AA
  trigger:
  - 同環境有穩定參與落差
  - 當事人反映障礙而物理檢表通過
  suppress:
  - 只問文件版本
  professional_support_trigger:
  - 當事人權利、安全及可及標準由自我倡議、受權專業與法務。
- id: V0.3.AA.family_studies
  name: 家庭研究
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.AA.family_studies
  first_sees: 從各人生活與照護工作重建
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AA.family_studies_家庭研究_整合版.md
  git_blob: 068837cbb46216c87ba680e866c43b2a950df04f
  neighbors:
  - V0.2.AA
  - V0.2.G
  default_retrieval: true
  parent_method: V0.2.AA
  trigger:
  - 照護負擔未清
  - 搬家及工作調動改家庭安排
  suppress:
  - 只問出生證明印刷值
  professional_support_trigger:
  - 兒少、個人安全、家庭權利和資源分配由負責社工和法律人員。
- id: V0.3.AC.agriculture_food_systems
  name: 農業／食物系統
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.AC.agriculture_food_systems
  first_sees: 分產出、損耗、流通、可及與季節
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AC.agriculture_food_systems_農業・食物系統_整合版.md
  git_blob: 94ca4d6c16d4d22f0b1d3f1b4575f909f6d93f9b
  neighbors:
  - V0.2.AC
  - V0.3.F.operations_supply_chain_logistics
  default_retrieval: true
  parent_method: V0.2.AC
  trigger:
  - 產量與實際供應不同
  - 季節或品質門檻影響農戶
  suppress:
  - 純粹土地法位
  professional_support_trigger:
  - 食品可食安全、農務操作及勞動、採購責任由有責任人。
- id: V0.3.AC.forestry_fisheries_conservation
  name: 森林／漁業／保育
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.AC.forestry_fisheries_conservation
  first_sees: 拆觀測、努力量、棲地與受影響者
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AC.forestry_fisheries_conservation_森林・漁業・保育_整合版.md
  git_blob: 2f843e05c7878325b826732f2c90497bc23c6456
  neighbors:
  - V0.2.AC
  - V0.2.AF
  default_retrieval: true
  parent_method: V0.2.AC
  trigger:
  - 資源件數變且活動強度不同
  - 保育與利用的監測未對齊
  suppress:
  - 只問法律登記
  professional_support_trigger:
  - 實地保育、捕撈、林業許可和社群資料由權責者與社群授權。
- id: V0.3.AD.transport_mobility
  name: 交通／運輸
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.AD.transport_mobility
  first_sees: 從起訖及時段重建各運具交接
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AD.transport_mobility_交通・運輸_整合版.md
  git_blob: 208355af0a97944cd8433139ec90b27d10a8e1e7
  neighbors:
  - V0.2.AD
  - V0.2.W
  default_retrieval: true
  parent_method: V0.2.AD
  trigger:
  - 班次很多但旅程失敗
  - 某些轉乘和時段無服務
  suppress:
  - 只判承運合約格式
  professional_support_trigger:
  - 真實交通調度、安全、工程和法規由有權營運及專業。
- id: V0.3.AF.biotech_biosafety
  name: 生技／生物安全
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.AF.biotech_biosafety
  first_sees: 先查授權、用途、責任和狀態
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AF.biotech_biosafety_生技・生物安全_整合版.md
  git_blob: 985e6370b55104e36a47c5b5eb3594c160908a92
  neighbors:
  - V0.2.AF
  - V0.3.I.bioethics
  default_retrieval: true
  parent_method: V0.2.AF
  trigger:
  - 機構計畫用途或供應責任有變
  - 稽核與事件紀錄缺接手
  suppress:
  - 要求操作、改造或規避安全篩查
  professional_support_trigger:
  - 具體材料、操作或暴露、事件處置與風險定級須交依法授權生物安全責任者。
- id: V0.3.AI.mining_mineral_resources
  name: 礦業／礦產
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.AI.mining_mineral_resources
  first_sees: 核場址條件、許可、復育及事後維護
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AI.mining_mineral_resources_礦業・礦產_整合版.md
  git_blob: 66f71c78d502029f04df726d8e58349d2cab5d64
  neighbors:
  - V0.2.AI
  - V0.2.AC
  default_retrieval: true
  parent_method: V0.2.AI
  trigger:
  - 現場營運與閉區責任接續不明
  - 地表修復後仍須查長程風險
  suppress:
  - 要求開採或危險物操作
  professional_support_trigger:
  - 工地採掘、資源與污染評估、安全及材料須由場址授權工程和環境專業。
- id: V0.3.AI.water_resource_management
  name: 水資源
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.AI.water_resource_management
  first_sees: 先列入出、儲存與不同負擔
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AI.water_resource_management_水資源_整合版.md
  git_blob: a62fc9c6c8163aca25fa2ba204cb0d3af25d1cc6
  neighbors:
  - V0.2.AI
  - V0.2.AC
  default_retrieval: true
  parent_method: V0.2.AI
  trigger:
  - 取用、供應及時段失配
  - 單井與區域資料不一致
  suppress:
  - 只讀地籍權人
  professional_support_trigger:
  - 調水、取水、水質、災害和權利由水文及主管工程。
- id: V0.3.AL.consumer_studies
  name: 消費者研究
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.AL.consumer_studies
  first_sees: 追資訊、退出成本與後果
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AL.consumer_studies_消費者研究_整合版.md
  git_blob: 6e8fd2026a5c5c13c98984d5ef485d2df871a10c
  neighbors:
  - V0.2.AL
  - V0.3.F.marketing_consumer
  default_retrieval: true
  parent_method: V0.2.AL
  trigger:
  - 接受者多但大量退費
  - 資訊或選項不等價
  suppress:
  - 只確認條款版本
  professional_support_trigger:
  - 實際申訴、退款、個資及金融行為責任依具資格專業。
- id: V0.3.AL.hci_ux
  name: 人機互動／UX
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.AL.hci_ux
  first_sees: 定任務、觀察、比較錯誤及恢復
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AL.hci_ux_人機互動・UX_整合版.md
  git_blob: 24b12d0c46c4d00fba386f237c0e063eb7dcc142
  neighbors:
  - V0.2.AL
  - V0.2.G
  default_retrieval: true
  parent_method: V0.2.AL
  trigger:
  - 使用者畫面操作易失敗
  - 首用與熟用差異
  suppress:
  - 只關合約或後端驗真
  professional_support_trigger:
  - 實際敏感流程、無障礙及版面合規由主管與有責任專業。
- id: V0.3.D.finance_financial_systems
  name: 金融／銀行／資本市場
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.D.finance_financial_systems
  first_sees: 先拆資產與資金期限、可變現性、損失吸收及中介責任
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.D.finance_financial_systems_金融・銀行・資本市場_整合版.md
  git_blob: 9e5b056b76d91d859de52de6a68706839836026f
  neighbors:
  - V0.2.D
  - V0.3.F.accounting
  default_retrieval: true
  parent_method: V0.2.D
  trigger:
  - 資金承諾和期限不一致
  - 市場流量與中介接口待查
  suppress:
  - 單純查法律身份
  - 請求買賣或個案資金安排
  professional_support_trigger:
  - 實際銀行及金融監理、資金調度、定價、投資與處置由責任專業者。
- id: V0.3.D.insurance_risk_transfer
  name: 保險／風險移轉
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.D.insurance_risk_transfer
  first_sees: 先追誰承擔何種事件與期間、哪些風險實際留存
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.D.insurance_risk_transfer_保險・風險移轉_整合版.md
  git_blob: 280e36ef808ab168700ba843f8ae5221089015fa
  neighbors:
  - V0.2.D
  - V0.3.D.finance_financial_systems
  default_retrieval: true
  parent_method: V0.2.D
  trigger:
  - 名義承保與實際事件有距離
  - 分層或共同暴露待辨
  suppress:
  - 只問無損失關聯的權限
  professional_support_trigger:
  - 個案給付、精算、資本和理賠指示交合格保險、精算及法務。
- id: V0.3.D.tax
  name: 稅務
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.D.tax
  first_sees: 先辨納稅主體、交易、連結點與時間，再定位查證資料
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.D.tax_稅務_整合版.md
  git_blob: 6ae378c697452558d5167bac5d951086144a23e5
  neighbors:
  - V0.2.D
  - V0.3.F.accounting
  default_retrieval: true
  parent_method: V0.2.D
  trigger:
  - 多地關係企業分工和價格待查
  - 發票、履約、對價有差
  suppress:
  - 只查法定截止日
  - 要求代行申報
  professional_support_trigger:
  - 任何納稅義務、稅率、申報、選擇與爭訟由實際法域稅務專業及責任人。
- id: V0.3.F.accounting
  name: 會計
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.F.accounting
  first_sees: 先把交易事實、控制、科目、期間與估計變更釐清
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.F.accounting_會計_整合版.md
  git_blob: 49b877d8825cbd3dfb90a92183aa773de67ff578
  neighbors:
  - V0.2.F
  - V0.2.D
  default_retrieval: true
  parent_method: V0.2.F
  trigger:
  - 同交易在現金和報表期間不同
  - 有變更估計或分類
  suppress:
  - 只判治理權限
  - 要求獨立確信
  professional_support_trigger:
  - 正式報表、準則適用和稅務申報交具資格會計師與責任人。
- id: V0.3.F.auditing_assurance
  name: 審計／確信
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.F.auditing_assurance
  first_sees: 先鎖特定主張、確信範圍、獨立性及充分適切證據
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.F.auditing_assurance_審計・確信_整合版.md
  git_blob: 38415c1f8fbe2c0e9452f40d7eeb16384e9a2b41
  neighbors:
  - V0.3.F.accounting
  - V0.2.F
  default_retrieval: true
  parent_method: V0.2.F
  trigger:
  - 報表主張要獨立驗證
  - 內外部來源可能同源
  suppress:
  - 單純對帳分類
  - 要求發出確信
  professional_support_trigger:
  - 正式審計、確信和任何簽署由具資格且具獨立性的專業人員。
- id: V0.3.F.corporate_governance
  name: 公司治理
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.F.corporate_governance
  first_sees: 先追誰提議、批准、執行、監督與揭露衝突
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.F.corporate_governance_公司治理_整合版.md
  git_blob: 9f2efbb920a7b1e0341a7e505d34e2c0b16cd6d2
  neighbors:
  - V0.2.F
  - V0.2.E
  default_retrieval: true
  parent_method: V0.2.F
  trigger:
  - 決定有權責或利益衝突
  - 多機關核准與監督不清
  suppress:
  - 單一門市流程或加總
  professional_support_trigger:
  - 董事義務、表決效力、大股東與證券揭露，交具資格法務及權責治理機關。
- id: V0.3.F.innovation_ip_strategy
  name: 創新／智慧財產策略
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.F.innovation_ip_strategy
  first_sees: 區分來源、貢獻、公開狀態及業務用途
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.F.innovation_ip_strategy_創新・智慧財產策略_整合版.md
  git_blob: 47b64d9c930da9da6cdcf94b62a302ca9dff1733
  neighbors:
  - V0.2.F
  - V0.3.F.strategy_entrepreneurship
  default_retrieval: true
  parent_method: V0.2.F
  trigger:
  - 新合作但成果來源未分清楚
  - 將展示或發行而授權未核
  suppress:
  - 只有市場價格或資格查詢
  professional_support_trigger:
  - 申請、轉讓、保密和共享承諾由知識產權專業與權責者。
- id: V0.3.F.marketing_consumer
  name: 行銷／消費者行為
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.F.marketing_consumer
  first_sees: 先查使用情境、替代方案、客戶可理解的利益與後續行為
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.F.marketing_consumer_行銷・消費者行為_整合版.md
  git_blob: 4d5fbd17471e6753e5ad42f218bc5854a6389dcb
  neighbors:
  - V0.2.F
  - V0.2.AL
  default_retrieval: true
  parent_method: V0.2.F
  trigger:
  - 流量增加但續用降低
  - 需辨產品價值、訊息或客群
  suppress:
  - 只問廣告適法或商標資格
  professional_support_trigger:
  - 行銷合規、隱私或脆弱群體的實施需行銷倫理、資料保護及法務審查。
- id: V0.3.F.operations_supply_chain_logistics
  name: 營運／供應鏈／物流
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.F.operations_supply_chain_logistics
  first_sees: 把需求、庫存、補貨、吞吐及服務交付串成按時序的鏈
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.F.operations_supply_chain_logistics_營運・供應鏈・物流_整合版.md
  git_blob: 57271fc763b58e71db6b33ac79ac61c1d6358bbf
  neighbors:
  - V0.2.F
  - V0.2.Q
  default_retrieval: true
  parent_method: V0.2.F
  trigger:
  - 缺貨與庫存看似矛盾
  - 交付時間或跨站流量失配
  suppress:
  - 只問單一合約資格
  professional_support_trigger:
  - 實際載運、危險物、安全及合約處理由物流和對應權責專業承接。
- id: V0.3.F.organizational_behavior_hr
  name: 組織行為／人力資源
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.F.organizational_behavior_hr
  first_sees: 先把職責、配時、激勵、團隊互動與管理回饋分開
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.F.organizational_behavior_hr_組織行為・人力資源_整合版.md
  git_blob: cfa966ac544c897a16467057717992ec4bff56f2
  neighbors:
  - V0.2.F
  - V0.2.G
  default_retrieval: true
  parent_method: V0.2.F
  trigger:
  - 相似員工在不同班表結果相差
  - 支持及回饋可能塑造事件
  suppress:
  - 單一文件事實且無人事影響
  professional_support_trigger:
  - 實際考核、監控、處分、歧視與職安，由人資、工會或專業及法務承接。
- id: V0.3.F.project_program_management
  name: 專案／Program 管理
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.F.project_program_management
  first_sees: 先找實際交付、前置依賴、可核里程和受益責任
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.F.project_program_management_專案・Program 管理_整合版.md
  git_blob: 6122624a45c53c6e63b0c47448f8866b00a7f095
  neighbors:
  - V0.2.F
  - V0.2.Q
  default_retrieval: true
  parent_method: V0.2.F
  trigger:
  - 不同工作流同時晚於規格
  - 已交付未有受益
  suppress:
  - 只摘契約固定欄位
  professional_support_trigger:
  - 實際工程投標、合同、資源承諾與安全由負責方簽核。
- id: V0.3.F.risk_compliance_internal_control
  name: 風險／法遵／內控
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.F.risk_compliance_internal_control
  first_sees: 先區分目標、風險、控制設計、實作證據及例外升級
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.F.risk_compliance_internal_control_風險・法遵・內控_整合版.md
  git_blob: ab0f4552fad98702db37fb4f9b33340f037640af
  neighbors:
  - V0.2.F
  - V0.3.F.auditing_assurance
  default_retrieval: true
  parent_method: V0.2.F
  trigger:
  - 規章記載與實施缺口
  - 例外控制有待證
  suppress:
  - 只問管轄法效力
  professional_support_trigger:
  - 實際合規決定、金融通報、現場操作與內控證明由合格責任人。
- id: V0.3.F.strategy_entrepreneurship
  name: 策略／創業
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.F.strategy_entrepreneurship
  first_sees: 先找關鍵假設、可行承諾、已有資源與證偽代價
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.F.strategy_entrepreneurship_策略・創業_整合版.md
  git_blob: 2153a08d8c7c4af53f71e6c646ffa01351ddcb56
  neighbors:
  - V0.2.F
  - V0.2.D
  default_retrieval: true
  parent_method: V0.2.F
  trigger:
  - 方案還未確立便要求規模化
  - 關鍵承諾的可逆性未查
  suppress:
  - 只需既有流程執行
  professional_support_trigger:
  - 真實融資、勞務和合併承諾交具授權的董事、財務與法務。
- id: V0.3.I.bioethics
  name: 生物／醫學倫理
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.I.bioethics
  first_sees: 把目的、益害、不確定、替代及同意分列
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.I.bioethics_生物・醫學倫理_整合版.md
  git_blob: e2c7f4d4c08c2def99fccacdaaea6c863c9f4066
  neighbors:
  - V0.2.I
  - V0.2.N
  default_retrieval: true
  parent_method: V0.2.I
  trigger:
  - 現場同意與參與壓力可能衝突
  - 利益、風險或退出條件不明
  suppress:
  - 只問已審結的檔案書目
  professional_support_trigger:
  - 真實研究倫理、臨床同意與脆弱情境由倫理審查、臨床、法律及當事人。
- id: V0.3.K.journalism_media_practice
  name: 新聞／媒體實務
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.K.journalism_media_practice
  first_sees: 先鎖原件、知情權、隱私與責任
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.K.journalism_media_practice_新聞・媒體實務_整合版.md
  git_blob: 94a43d0e9b683d185a0c49cdc37758d69c25037e
  neighbors:
  - V0.2.K
  - V0.2.T
  default_retrieval: true
  parent_method: V0.2.K
  trigger:
  - 打算發布尚未查驗主張
  - 已發布內容出現可查錯誤
  suppress:
  - 只有敘事形式分析
  professional_support_trigger:
  - 真實指控、受保護當事人、資料公開及採訪安全由編輯與法務。
- id: V0.3.M.ai_ml_systems
  name: AI／ML 系統
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.M.ai_ml_systems
  first_sees: 明示目的、資料、版本和人員接手
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.M.ai_ml_systems_AI・ML 系統_整合版.md
  git_blob: d707228a23c42a2a7da7f1988ae568333a6bffb3
  neighbors:
  - V0.2.M
  - V0.2.L
  default_retrieval: true
  parent_method: V0.2.M
  trigger:
  - 開發指標與現場差異
  - 用途版本或使用者組成變了
  suppress:
  - 只查權利或設備物理狀態
  professional_support_trigger:
  - 生產部署與高風險決策交有權 AI 工程、監管、資料及領域專家。
- id: V0.3.M.cybersecurity
  name: 網路安全／資安
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.M.cybersecurity
  first_sees: 先畫資產、權責、保護與復原證據
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.M.cybersecurity_網路安全・資安_整合版.md
  git_blob: 6a58ea775ac9be23ff989d92293a14c8f053985d
  neighbors:
  - V0.2.M
  - V0.3.F.risk_compliance_internal_control
  default_retrieval: true
  parent_method: V0.2.M
  trigger:
  - 資產責任與異常訊號不合
  - 服務復原需驗證
  suppress:
  - 要求重現利用弱點或侵入
  professional_support_trigger:
  - 現場事件、數位鑑識、通報與復原均先由授權責任者判定。
- id: V0.3.M.digital_identity_trust
  name: 數位身分／信任
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.M.digital_identity_trust
  first_sees: 分查證、認證、資料聲明、授權和恢復
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.M.digital_identity_trust_數位身分・信任_整合版.md
  git_blob: 7e40860fe119406dffe3eb92f1eb5c0abe7eae1c
  neighbors:
  - V0.2.M
  - V0.3.Y.data_governance_privacy
  default_retrieval: true
  parent_method: V0.2.M
  trigger:
  - 認證成功卻服務拒絕
  - 憑據恢復後權限不同
  suppress:
  - 只查國籍與法院法源
  professional_support_trigger:
  - 驗證、個資、身份紛爭與服務配置由有權身份、法務及資料責任者。
- id: V0.3.M.software_engineering
  name: 軟體工程
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.M.software_engineering
  first_sees: 鎖需求、相容、配置及負責人
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.M.software_engineering_軟體工程_整合版.md
  git_blob: 942ec8642739ea06a0a4ff53461b0d22b0a53758
  neighbors:
  - V0.2.M
  - V0.2.Q
  default_retrieval: true
  parent_method: V0.2.M
  trigger:
  - 改版與既有資料不相容
  - 測試綠但服務差
  suppress:
  - 只問數學結論或合約效力
  professional_support_trigger:
  - 實際生產部署、高責任交付和資料改動由系統所有者核定。
- id: V0.3.N.clinical_medicine
  name: 臨床醫學
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.N.clinical_medicine
  first_sees: 先區分自述、所見、時序和待核
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.N.clinical_medicine_臨床醫學_整合版.md
  git_blob: 0a91dc22de76cd90ef7f8615734d2a2b02e6d6b1
  neighbors:
  - V0.2.N
  - V0.3.AA.care_systems
  default_retrieval: true
  parent_method: V0.2.N
  trigger:
  - 個人健康主張與記錄不齊
  - 需理清照護時序和證據
  suppress:
  - 只問一般群體比例
  professional_support_trigger:
  - 具體健康和急迫性、診療、照護安全由合格臨床人員承接。
- id: V0.3.N.epidemiology
  name: 流行病學
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.N.epidemiology
  first_sees: 先比較定義、時間、地點和人群
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.N.epidemiology_流行病學_整合版.md
  git_blob: cd3679fa0ada0cec2122efc6fda55f9bb330fe38
  neighbors:
  - V0.2.N
  - V0.2.L
  default_retrieval: true
  parent_method: V0.2.N
  trigger:
  - 通報量改變且口徑可能變
  - 群體風險的分母未知
  suppress:
  - 急需個案臨床判斷
  professional_support_trigger:
  - 真實公衛調查、個人健康和處置由授權專業機構。
- id: V0.3.N.food_safety
  name: 食品安全
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.N.food_safety
  first_sees: 分品項、批次、流程、控制及查證
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.N.food_safety_食品安全_整合版.md
  git_blob: 44b9e839ceb12f777bd1c40c73c1783eb3db42b8
  neighbors:
  - V0.2.N
  - V0.3.AC.agriculture_food_systems
  default_retrieval: true
  parent_method: V0.2.N
  trigger:
  - 批次紀錄或品質回報不符
  - 控制點有責任交接缺
  suppress:
  - 要求現場食品可食或個人處置
  professional_support_trigger:
  - 食品衛生、實際產品放行、召回、就醫及稽核由有資格與授權的食品安全、衛生或醫療責任者。
- id: V0.3.N.health_systems
  name: 健康系統
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.N.health_systems
  first_sees: 拆資源、服務、等待、費用和品質
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.N.health_systems_健康系統_整合版.md
  git_blob: 840f2030b245c86426853ed982c74af678b8c0ff
  neighbors:
  - V0.2.N
  - V0.3.AA.care_systems
  default_retrieval: true
  parent_method: V0.2.N
  trigger:
  - 資源增加但等待未降
  - 健康服務各群覆蓋分歧
  suppress:
  - 只需查化驗紀錄日期
  professional_support_trigger:
  - 醫療配置、付款與服務政策交權責管理、衛生及臨床專業。
- id: V0.3.N.pharmacology_drug_safety
  name: 藥理／藥物安全
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.N.pharmacology_drug_safety
  first_sees: 先定產品、暴露、事件及原始來源
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.N.pharmacology_drug_safety_藥理・藥物安全_整合版.md
  git_blob: f68fad571acb5a5ac3a2c086918e7919d94ae1c6
  neighbors:
  - V0.2.N
  - V0.3.N.epidemiology
  default_retrieval: true
  parent_method: V0.2.N
  trigger:
  - 產品使用後出現新安全主張
  - 監測數變化但資料含重複
  suppress:
  - 要求個人用藥決策
  professional_support_trigger:
  - 個別用藥、劑量、停藥、疑似不良事件與監管措施交醫師、藥師及權責單位。
- id: V0.3.O.diplomacy_negotiation
  name: 外交／談判
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.O.diplomacy_negotiation
  first_sees: 區分立場、利益、可逆安排與履約
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.O.diplomacy_negotiation_外交・談判_整合版.md
  git_blob: 708c2cb78a3d71f8c3232b1b8e871ccb2b77903d
  neighbors:
  - V0.2.O
  - V0.2.R
  default_retrieval: true
  parent_method: V0.2.O
  trigger:
  - 表面立場衝突
  - 多方才能核准並履約
  suppress:
  - 只查有效法源
  professional_support_trigger:
  - 真實外交、代表及和解由有授權者及合格法務。
- id: V0.3.Q.civil_construction
  name: 土木／建築工程
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.Q.civil_construction
  first_sees: 比設計、工序、變更與完工
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.Q.civil_construction_土木・建築工程_整合版.md
  git_blob: 27ad1ffee31743088e502f262f581be0802a274a
  neighbors:
  - V0.2.Q
  - V0.2.AD
  default_retrieval: true
  parent_method: V0.2.Q
  trigger:
  - 工程圖、實施和驗收有差
  - 有當期變更待追
  suppress:
  - 只問產權或形式日期
  professional_support_trigger:
  - 結構、工地安全及實地變更由有資格工程與主管責任者。
- id: V0.3.Q.energy_systems
  name: 能源系統
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.Q.energy_systems
  first_sees: 查需求、配置、時間與可用性
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.Q.energy_systems_能源系統_整合版.md
  git_blob: 7932e4a7e0dd2b491edf04fdf67bbbd27c577f99
  neighbors:
  - V0.2.Q
  - V0.2.AG
  default_retrieval: true
  parent_method: V0.2.Q
  trigger:
  - 整體可用和尖峰服務差
  - 假設備援有效但未驗
  suppress:
  - 只要求法律分類
  professional_support_trigger:
  - 現場電力、供能、關鍵設施及安全交有資格工程和營運者。
- id: V0.3.Q.space_systems
  name: 太空系統
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.Q.space_systems
  first_sees: 分任務目標、地面接手、版本與生命週期治理
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.Q.space_systems_太空系統_整合版.md
  git_blob: 67b582a14992615c33969db3399b18f5998dd34e
  neighbors:
  - V0.2.Q
  - V0.2.AG
  default_retrieval: true
  parent_method: V0.2.Q
  trigger:
  - 民用觀測與發布產品不對齊
  - 資料版本和任務責任不明
  suppress:
  - 要求軍事行動或業外操作
  professional_support_trigger:
  - 太空及射頻操作、發射資格、監管和安全由合格責任者。
- id: V0.3.Q.telecommunications_networks
  name: 電信／網路系統
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.Q.telecommunications_networks
  first_sees: 分端點、接續、承載、呼叫體驗及範圍
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.Q.telecommunications_networks_電信・網路系統_整合版.md
  git_blob: f099852492b40186b461f34e3a9958789c85901b
  neighbors:
  - V0.2.Q
  - V0.2.M
  default_retrieval: true
  parent_method: V0.2.Q
  trigger:
  - 通信標稱品質和用戶體驗不同
  - 跨網接續有重複異常
  suppress:
  - 只有權利文件爭議
  professional_support_trigger:
  - 電信服務配置、頻譜和現場處置由資質人員與主管。
- id: V0.3.Q.utilities_infrastructure
  name: 公共事業／基礎設施
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.Q.utilities_infrastructure
  first_sees: 分設施、服務、支付可及與復原
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.Q.utilities_infrastructure_公共事業・基礎設施_整合版.md
  git_blob: c78832c4f1c2b2457a860f0009d5f855871c367b
  neighbors:
  - V0.2.Q
  - V0.2.U
  default_retrieval: true
  parent_method: V0.2.Q
  trigger:
  - 工程完成而用戶未恢復
  - 費率和連續性需要拆分
  suppress:
  - 只查章程權責
  professional_support_trigger:
  - 實際供應、費率、復原及設施安全由公共部門和營運工程負責。
- id: V0.3.U.emergency_disaster_management
  name: 緊急／災害管理
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.U.emergency_disaster_management
  first_sees: 分準備、應變、維持和復原
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.U.emergency_disaster_management_緊急・災害管理_整合版.md
  git_blob: 03112959d217dd8cc6acd37c5421084c66e69a62
  neighbors:
  - V0.2.U
  - V0.2.Q
  default_retrieval: true
  parent_method: V0.2.U
  trigger:
  - 危害跨站且需求變動
  - 已處理宣稱缺到達證據
  suppress:
  - 只問公告時間
  professional_support_trigger:
  - 真實警報、撤離、救援及復原由救援、主管及執業人員。
- id: V0.3.U.migration_refugee_studies
  name: 移民／難民研究
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.U.migration_refugee_studies
  first_sees: 分離身份判斷、流動時間、知情與社會支持
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.U.migration_refugee_studies_移民・難民研究_整合版.md
  git_blob: f791ea87824b91fa2638adbdd9dfedd6cd51b0e3
  neighbors:
  - V0.2.U
  - V0.2.AB
  default_retrieval: true
  parent_method: V0.2.U
  trigger:
  - 異地移動後服務中斷
  - 數據及個人需求混用
  suppress:
  - 只確認明文名單
  professional_support_trigger:
  - 具體移民、難民、兒童安全、保護資料和身份審定由授權機構及獨立專業。
- id: V0.3.U.public_finance_budgeting
  name: 公共財政／預算
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.U.public_finance_budgeting
  first_sees: 分授權、支出承諾和現金
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.U.public_finance_budgeting_公共財政・預算_整合版.md
  git_blob: aeba5062799445ca1564eeada3d8971ea387b1b2
  neighbors:
  - V0.2.U
  - V0.2.D
  default_retrieval: true
  parent_method: V0.2.U
  trigger:
  - 已批准與已支付有差
  - 跨期資金負擔不明
  suppress:
  - 只確認稅務身分
  professional_support_trigger:
  - 實際撥用和債務、財政披露由有權機關、會計與財政專業。
- id: V0.3.U.public_procurement
  name: 政府採購
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.U.public_procurement
  first_sees: 從生活服務回溯規格、比較及交付
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.U.public_procurement_政府採購_整合版.md
  git_blob: d65d65bbea27f3e4427f5f8b158df3dcd3e77e7d
  neighbors:
  - V0.2.U
  - V0.2.S
  default_retrieval: true
  parent_method: V0.2.U
  trigger:
  - 規格只一種來源
  - 低標與使用驗收有落差
  suppress:
  - 只問逾期效力
  professional_support_trigger:
  - 實際招標、評選、締約、救濟及利益衝突由採購、法務和主管。
- id: V0.3.U.regulatory_governance
  name: 監管治理
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.U.regulatory_governance
  first_sees: 把風險、工具、成本與監測列清
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.U.regulatory_governance_監管治理_整合版.md
  git_blob: 2dcabdade0f7c4e78e96f3ee5f460f75021e4fcf
  neighbors:
  - V0.2.U
  - V0.2.C
  default_retrieval: true
  parent_method: V0.2.U
  trigger:
  - 擬改有普遍效果規則
  - 執行行為未達目標
  suppress:
  - 只判單一法定期限
  professional_support_trigger:
  - 監管、正式處分及法律效力由有權機關和專業者。
- id: V0.3.V.defence_military_studies
  name: 國防／軍事研究
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.V.defence_military_studies
  first_sees: 先核公開授權、預算與責任接口
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.V.defence_military_studies_國防・軍事研究_整合版.md
  git_blob: 97882269ccd32224246a2121cfdfd55c36675fae
  neighbors:
  - V0.2.V
  - V0.2.E
  default_retrieval: true
  parent_method: V0.2.V
  trigger:
  - 文人監督和預算權責未對齊
  - 需檢視民用協助的結束條件
  suppress:
  - 要求戰術、武器或行動方法
  professional_support_trigger:
  - 帶權公務、保密、民用保護與國際法決定由授權機關及獨立監督、法律和人道責任者。
- id: V0.3.Y.data_governance_privacy
  name: 資料治理／隱私
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  source_version: V0.3.Y.data_governance_privacy
  first_sees: 畫蒐集到刪除、分享與回應權
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.Y.data_governance_privacy_資料治理・隱私_整合版.md
  git_blob: dad2fc9661dc85b4a9a714ea3096041a88777f79
  neighbors:
  - V0.2.Y
  - V0.2.X
  default_retrieval: true
  parent_method: V0.2.Y
  trigger:
  - 新用途或接收方
  - 表內資訊可與他源連結
  suppress:
  - 不涉及資料使用而只問談判利益
  professional_support_trigger:
  - 合法性、個資安全和委外由合格資料保護及法務。
```

## Specialized / Contextual Registry

```yaml
SPECIALIZED_CONTEXTUAL_REGISTRY:
- id: CONTEXT.NARRATIVE_PHYSICS
  name: AI 小說心法／敘事物理學
  class: SPECIALIZED_CONTEXTUAL
  layer: SPECIALIZED_CONTEXTUAL
  standing: 未完成草案
  source_version: V0.1
  first_sees: 原創敘事裡的力量、壓強、自由度、張力與命運節點
  canonical_file: ../04_SPECIALIZED_CONTEXTUAL/AI小說心法(敘事物理學).md
  git_blob: 20b8a5a986cb3576d556b21069b20d19bed7f899
  neighbors:
  - V0.2.AJ
  - V0.2.AM
  default_retrieval: false
  included_in_main_39: false
  included_in_functional_51: false
  included_in_total_90: false
  explicit_context_required: true
- id: CONTEXT.FINANCIAL_MARKET_STRUCTURE
  name: 理火金融心法／市場結構篇
  class: SPECIALIZED_CONTEXTUAL
  layer: SPECIALIZED_CONTEXTUAL
  standing: FIRST_DRAFT
  source_version: V0.1
  first_sees: 目前市場位置、可能情境、支持與反向證據、失效條件
  canonical_file: ../04_SPECIALIZED_CONTEXTUAL/理火金融心法_市場結構篇_V0.1.md
  git_blob: bd9e73e618c44cef4305f7fe5a6527f845b2afdf
  neighbors:
  - V0.2.D
  - V0.2.S
  default_retrieval: false
  included_in_main_39: false
  included_in_functional_51: false
  included_in_total_90: false
  explicit_context_required: true
- id: CONTEXT.GUANZHI_RELATIONAL_LANGUAGE
  name: 風月場關係話術心法
  class: SPECIALIZED_CONTEXTUAL
  layer: SPECIALIZED_CONTEXTUAL
  standing: FORMAL_EXPERIMENTAL_FIRST_DRAFT
  source_version: V0.1
  first_sees: 觀止世界的對話角色、關係位置、語境與人物自主
  canonical_file: ../04_SPECIALIZED_CONTEXTUAL/風月場關係話術心法_V0.1.md
  git_blob: 66c1ee63bdeb14aa02254eeba92a39999902bf90
  neighbors:
  - V0.2.R
  - V0.2.AJ
  default_retrieval: false
  included_in_main_39: false
  included_in_functional_51: false
  included_in_total_90: false
  explicit_context_required: true
```

## Default Retrieval Exclusion

**DO NOT LOAD FOR ORDINARY METHOD ROUTING.** 版本、Coverage、來源及治理爭議才查 [Build / Audit](../90_BUILD_AUDIT/README.md)。

```yaml
DEFAULT_RETRIEVAL_EXCLUSION:
- BUILD_AUDIT
- LEGACY
- COMPATIBILITY
- DERIVED_AI_FRIENDLY_VIEW
- HISTORICAL_TOTAL_CATALOG
- SUPERSEDED_INTEGRATED_VERSION
```

## 入口與治理

先查 [Routing Index](METHOD_ATLAS_ROUTING_INDEX_V1.0.md)。相容與歷史查 [Current / Legacy Map](METHOD_ATLAS_CURRENT_LEGACY_MAP_V1.0.md)。逐檔變動見 [Migration Map](METHOD_ATLAS_MIGRATION_MAP_V1.0.md)。專案正式規範見 [階段邊界修正版](../01_ATLAS_CORE/學科心法總目錄_V0.2_總綱版_階段邊界修正版.md)。
