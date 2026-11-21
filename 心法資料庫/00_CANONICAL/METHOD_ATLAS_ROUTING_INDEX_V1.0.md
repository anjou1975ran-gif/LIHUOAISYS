# Method Atlas｜Routing Index V1.0

從 [Canonical Index](METHOD_ATLAS_CANONICAL_INDEX_V1.0.md) 進入。先辨任務目的、實際證據與下一步責任，對照同列全部觸發條件及抑制條件。候選控制為 2–5 個。若訊號交疊，選最切合主要待辨事實的列，再用該列候選的 `primary_when`、`secondary_when` 與觀察增量判取捨。

短列以證據條件和任務同時滿足為判準。判斷哪些事實成立需讀整題與授權，篇章裡碰巧出現相同字眼不足以觸發路由。若各候選都無實質增量，回傳 `NO_METHOD`。若來源或授權不確定，記錄理由並保持待查。

對已選中者核對 Canonical Index 唯一的 canonical_file、source_version、Git ref 與 blob，只調閱被選中的正本。指定業務需要第二個鏡頭時重新做增量檢查。情境包須先有明示場景。需要核定法律、醫療、金融、工程、資安防禦、生物安全或人身安全時，轉相應的權責角色。

**DO NOT LOAD FOR ORDINARY METHOD ROUTING.** Build、Audit、Legacy、AI 友善版及過時總綱退出日常候選與取檔。

## Problem → Method Index

```yaml
PROBLEM_METHOD_INDEX:
- problem: 推論與資料生成
  trigger:
  - 需要群體推論
  - 分母或資料生成改變
  suppress:
  - 只讀已知明文
  - 只要求個案處置
  candidates:
  - V0.2.L
  - V0.2.AB
  - V0.2.N
  - V0.3.N.epidemiology
  primary: V0.2.L
  secondary:
  - V0.2.AB
  - V0.2.N
  - V0.3.N.epidemiology
  neighbor:
  - V0.2.D
  - V0.2.G
  professional_support:
  - 重大裁判、公共發布或監管決策依賴複雜抽樣、非隨機缺失或個體敏感資料時，交統計／調查設計專業者核對設計及資料使用權限。
  routing_reason: 當待判的是能否由樣本、分母及資料生成推導總體或處置效果，統計先查可識別性。若爭人口組成或健康監測，補人口或流行病學；個別照護由臨床角色。
- problem: 計算狀態與並發
  trigger:
  - 計算狀態待驗
  - 介面回覆與權威紀錄分離
  suppress:
  - 只讀已知明文
  - 要求未授權入侵
  candidates:
  - V0.2.M
  - V0.2.AE
  - V0.3.M.software_engineering
  - V0.2.Q
  primary: V0.2.M
  secondary:
  - V0.2.AE
  - V0.3.M.software_engineering
  - V0.2.Q
  neighbor:
  - V0.2.F
  - V0.2.L
  professional_support:
  - 涉上線支付、敏感資料或關鍵基礎服務時，由負責的軟體與資安專業在授權範圍核對設計、測試與證據。個案鑑識和部署由責任人確認。
  routing_reason: 兩次回覆與實際狀態可分離，先查權威狀態、順序及不變量，再比形式證明、軟體發布或端到端服務。生產系統需系統責任者。
- problem: 系統需求與交付
  trigger:
  - 複合服務交付
  - 跨介面或降級失效
  suppress:
  - 只讀已知明文
  candidates:
  - V0.2.Q
  - V0.2.M
  - V0.3.F.project_program_management
  - V0.3.Q.civil_construction
  primary: V0.2.Q
  secondary:
  - V0.2.M
  - V0.3.F.project_program_management
  - V0.3.Q.civil_construction
  neighbor:
  - V0.2.M
  - V0.2.F
  professional_support:
  - 真人安全、公共工程、醫材或關鍵服務關切進入實地試驗、驗收、運行切換時，由授權的工程責任人與獨立安全驗證角色簽核。
  routing_reason: 組件通過但服務失敗，查需求、依賴、整合與降級；若根因是版本、時程或實地工程，再接相應專業。
- problem: 健康證據與介入
  trigger:
  - 健康問題需要分層
  - 臨床與群體或介入並存
  suppress:
  - 只讀已知明文
  candidates:
  - V0.2.N
  - V0.3.N.clinical_medicine
  - V0.3.N.health_systems
  - V0.3.N.pharmacology_drug_safety
  - V0.3.I.bioethics
  primary: V0.2.N
  secondary:
  - V0.3.N.clinical_medicine
  - V0.3.N.health_systems
  - V0.3.N.pharmacology_drug_safety
  - V0.3.I.bioethics
  neighbor:
  - V0.2.L
  - V0.2.Q
  professional_support:
  - 個案診斷、用藥、緊急照護、具體公共衛生處置或裁判中的傷害歸因，由具管轄責任的醫療、衛生或法醫專業承接。
  routing_reason: 先分個案、群體、介入與證據，再限縮到診療時序、服務接續、藥物安全或倫理。真實個案、衛生措施和研究同意由合格責任角色。
- problem: 跨國互賴與承諾
  trigger:
  - 跨國互賴待辨
  - 共同權威不足而承諾受制
  suppress:
  - 只讀已知明文
  candidates:
  - V0.2.O
  - V0.2.E
  - V0.3.O.diplomacy_negotiation
  - V0.2.P
  primary: V0.2.O
  secondary:
  - V0.2.E
  - V0.3.O.diplomacy_negotiation
  - V0.2.P
  neighbor:
  - V0.2.E
  - V0.2.C
  professional_support:
  - 真實外交立場、條約效力、高風險代表行動由具授權的外交或國際法專業者確認。輸出以比較假說及待查證據為限。
  routing_reason: 待解釋履約或互惠時先查外部承諾，國內授權、可協商選項或通道條件另看。實際對外承諾需代表權。
- problem: 跨境通達與控制
  trigger:
  - 跨境通達受制
  - 空間節點或邊界改變替代
  suppress:
  - 只讀已知明文
  candidates:
  - V0.2.P
  - V0.2.W
  - V0.2.AD
  - V0.3.AD.transport_mobility
  - V0.2.O
  primary: V0.2.P
  secondary:
  - V0.2.W
  - V0.2.AD
  - V0.3.AD.transport_mobility
  - V0.2.O
  neighbor:
  - V0.2.O
  - V0.2.Q
  professional_support:
  - 實際民生運輸安全、港口通達和跨境許可，交運輸規劃與主管機關確認。案例不提供行動、打擊或規避安排。
  routing_reason: 先查走廊、控制、通行資格與替代依賴。尺度、城區服務及實際旅程再分案。調度與跨境許可由權責者。
- problem: 意義、語境與說法
  trigger:
  - 意義或承諾有歧義
  - 語句需要原語境
  suppress:
  - 只讀已知明文
  candidates:
  - V0.2.R
  - V0.2.K
  - V0.2.AJ
  - V0.3.AL.hci_ux
  primary: V0.2.R
  secondary:
  - V0.2.K
  - V0.2.AJ
  - V0.3.AL.hci_ux
  neighbor:
  - V0.2.K
  - V0.2.C
  professional_support:
  - 法定廣告判定、合意效力、專業翻譯鑑定或具爭議的語意，移交律師及語言專家，保留原件及異讀。
  routing_reason: 若爭點是字面、指稱、推論或版面合讀，先看原語境。若問題在可見性、敘事知情位置或使用流程，分別查傳播、文學或 HCI。
- problem: 可行集合與取捨
  trigger:
  - 多方案需要取捨
  - 硬限制或情境使排序改變
  suppress:
  - 只讀已知明文
  - 法律資格是唯一爭點
  candidates:
  - V0.2.S
  - V0.2.AE
  - V0.2.D
  - V0.3.U.public_finance_budgeting
  primary: V0.2.S
  secondary:
  - V0.2.AE
  - V0.2.D
  - V0.3.U.public_finance_budgeting
  neighbor:
  - V0.2.D
  - V0.2.L
  professional_support:
  - 真實資源配置、法定保全、財務重整或生命安全方案，交主管、律師、財務與工程責任人核准假設和權限。
  routing_reason: 先排不可行再比可接受犧牲與穩健性。形式反例、實際偏好形成和預算權限各有接口。真實配置由權責人。
- problem: 來源可信與假說
  trigger:
  - 未知事實有競爭解釋
  - 材料同源或可信度待查
  suppress:
  - 原件唯一且無推論爭點
  - 要求未授權入侵
  candidates:
  - V0.2.T
  - V0.2.Y
  - V0.2.K
  - V0.3.K.journalism_media_practice
  primary: V0.2.T
  secondary:
  - V0.2.Y
  - V0.2.K
  - V0.3.K.journalism_media_practice
  neighbor:
  - V0.2.K
  - V0.2.L
  professional_support:
  - 涉重大司法或國安指控、受保護資料、機構通報與制裁適用，應交有授權的調查、法律或合規角色。
  routing_reason: 先判主張與資料是否獨立，分版本可尋、訊息擴散及編務發布。涉及國安、司法及公開指控，依權責查驗。
- problem: 神聖實踐與詮釋權
  trigger:
  - 神聖實踐或神話待辨
  - 社群內外的場所或權威詮釋不同
  suppress:
  - 只讀已知明文
  candidates:
  - V0.2.AK
  - V0.2.J
  - V0.2.AM
  - V0.2.AJ
  primary: V0.2.AK
  secondary:
  - V0.2.J
  - V0.2.AM
  - V0.2.AJ
  neighbor:
  - V0.2.J
  - V0.2.AJ
  professional_support:
  - 涉及活態宗教、受限制材料、權利或保護爭議，依具責任社群與法律、文化專業確認邊界。
  routing_reason: 對照儀式、場合及內外分類，再分文化厚描、傳承和文本形式。保留社團同意及受限文化資料權限。
- problem: 授權資安防禦
  trigger:
  - 防禦與復原責任待驗
  - 已授權資產和防禦證據
  suppress:
  - 只讀已知明文
  - 要求未授權入侵
  candidates:
  - V0.3.M.cybersecurity
  - V0.2.M
  - V0.3.M.digital_identity_trust
  - V0.3.F.risk_compliance_internal_control
  - V0.3.Q.telecommunications_networks
  primary: V0.3.M.cybersecurity
  secondary:
  - V0.2.M
  - V0.3.M.digital_identity_trust
  - V0.3.F.risk_compliance_internal_control
  - V0.3.Q.telecommunications_networks
  neighbor:
  - V0.2.M
  - V0.3.F.risk_compliance_internal_control
  professional_support:
  - 現場事件、數位鑑識、通報與復原均先由授權責任者判定。
  routing_reason: 有權的服務防禦先查資產、控制、合法證據和實際復原，並分程式狀態、身分和通訊。越權取得或重現入侵排除。
- problem: 明文抄錄與無增量
  trigger:
  - 只讀已知明文
  - 原件唯一且無推論爭點
  suppress: []
  candidates: &id001
  - V0.2.Y
  - V0.2.R
  - V0.2.B
  primary: NO_METHOD
  secondary: []
  neighbor: *id001
  professional_support: []
  routing_reason: 原件已知且只抄值，搜尋、消歧與歷史重建均缺增量。可直接讀原件。
- problem: 公權、立場與政策施行
  trigger:
  - 公權如何運作待解釋
  - 角色分權或前線施行有差
  suppress:
  - 只讀已知明文
  candidates:
  - V0.2.E
  - V0.2.U
  - V0.2.C
  - V0.3.U.regulatory_governance
  - V0.3.U.public_procurement
  primary: V0.2.E
  secondary:
  - V0.2.U
  - V0.2.C
  - V0.3.U.regulatory_governance
  - V0.3.U.public_procurement
  neighbor:
  - V0.2.U
  - V0.2.C
  - V0.2.O
  professional_support:
  - 正式公權決定、法律結論與涉及大眾風險的措施由權責人。
  routing_reason: 爭授權與政治責任用政治學，法定效果走法學。若瓶頸在服務抵達、監管或採購則選專門候選。
- problem: 規範效力與責任
  trigger:
  - 法律資格或程序是主問題
  - 管轄規則與事實需對照
  suppress:
  - 只讀已知明文
  candidates:
  - V0.2.C
  - V0.2.I
  - V0.2.U
  - V0.3.AL.consumer_studies
  primary: V0.2.C
  secondary:
  - V0.2.I
  - V0.2.U
  - V0.3.AL.consumer_studies
  neighbor:
  - V0.2.E
  - V0.2.I
  - V0.2.R
  professional_support:
  - 依本包法域、材料和輸出級別諸門，個案法律意見及處置由適格法務。
  routing_reason: 先查法域、法源、程序與證據地位。價值成立、行政落地及消費理解各另有限定功能。個案交適格法務。
- problem: 組織權責與執行
  trigger:
  - 組織各角色責任待定
  - 任務與實際授權或回報不一致
  suppress:
  - 只讀已知明文
  candidates:
  - V0.2.F
  - V0.3.F.corporate_governance
  - V0.3.F.organizational_behavior_hr
  - V0.3.A.labor_industrial_relations
  primary: V0.2.F
  secondary:
  - V0.3.F.corporate_governance
  - V0.3.F.organizational_behavior_hr
  - V0.3.A.labor_industrial_relations
  neighbor:
  - V0.2.Q
  - V0.2.D
  - V0.2.U
  professional_support:
  - 真實公司治理、勞動、投資、會計及改變承諾由具授權的專業者。
  routing_reason: 組織能否承接目標先用管理。治理授權、團隊行為、勞工代表和工作實況再細分。
- problem: 社會結構與個人支持
  trigger:
  - 群體位置與個人資源相互影響
  - 接觸門檻或生活關係有缺口
  suppress:
  - 只讀已知明文
  candidates:
  - V0.2.A
  - V0.2.AA
  - V0.2.G
  - V0.3.AA.family_studies
  - V0.3.AA.child_development_protection
  primary: V0.2.A
  secondary:
  - V0.2.AA
  - V0.2.G
  - V0.3.AA.family_studies
  - V0.3.AA.child_development_protection
  neighbor:
  - V0.2.J
  - V0.2.G
  - V0.2.E
  professional_support:
  - 社會工作、高風險決策或涉及個人權利時轉權責領域。
  routing_reason: 群體規範、角色與權力優先看社會結構。個案運作、心理與關係、兒少參與分 Scope 並由專業承擔。
- problem: 學習認知與參與
  trigger:
  - 學習或參與軌跡待辨
  - 任務與評量或理解方式不一致
  suppress:
  - 只讀已知明文
  candidates:
  - V0.2.H
  - V0.2.G
  - V0.2.AL
  - V0.3.AA.child_development_protection
  - V0.3.AA.disability_studies
  primary: V0.2.H
  secondary:
  - V0.2.G
  - V0.2.AL
  - V0.3.AA.child_development_protection
  - V0.3.AA.disability_studies
  neighbor:
  - V0.2.G
  - V0.2.A
  - V0.2.AL
  professional_support:
  - 兒少保護、特教、教育執業與重大政策交對應責任專業。
  routing_reason: 學習與制度化評量走教育。若關鍵在心理情境、設計障礙或保護職責，按證據改選。不據任務結果診斷個人。
- problem: 人口轉移與支持缺口
  trigger:
  - 群體世代或流入流出待辨
  - 服務需求與人群結構共變
  suppress:
  - 只讀已知明文
  candidates:
  - V0.2.AB
  - V0.2.AA
  - V0.3.AA.aging_gerontology
  - V0.3.AA.care_systems
  - V0.3.U.migration_refugee_studies
  primary: V0.2.AB
  secondary:
  - V0.2.AA
  - V0.3.AA.aging_gerontology
  - V0.3.AA.care_systems
  - V0.3.U.migration_refugee_studies
  neighbor:
  - V0.2.L
  - V0.2.AA
  professional_support:
  - 使用小區域個資、制定法定給付或發布人口預測，由人口學、統計、地方責任機關和法務覆核。
  routing_reason: 先分存量、世代與事件；個人接續、長者參與及跨地資格需相應專業。
- problem: 環境壓力與資源
  trigger:
  - 環境受體與壓力待辨
  - 跨時間場址的比較證據不足
  suppress:
  - 只讀已知明文
  candidates:
  - V0.2.AC
  - V0.2.W
  - V0.2.AF
  - V0.3.AC.forestry_fisheries_conservation
  - V0.3.AI.water_resource_management
  primary: V0.2.AC
  secondary:
  - V0.2.W
  - V0.2.AF
  - V0.3.AC.forestry_fisheries_conservation
  - V0.3.AI.water_resource_management
  neighbor:
  - V0.2.W
  - V0.2.L
  professional_support:
  - 涉及環評、環境安全、實地處置或受威脅棲地，由具責任專家、主管機關及相關社群審查。
  routing_reason: 跨場址與比較基線優先環境。物種機制、空間特徵、保育和流域調配保留各自證據。
- problem: 守恆與工況
  trigger:
  - 物理機轉待辨
  - 同耗用或測點的條件不同
  suppress:
  - 只讀已知明文
  candidates:
  - V0.2.AG
  - V0.2.AH
  - V0.2.Q
  - V0.3.Q.energy_systems
  primary: V0.2.AG
  secondary:
  - V0.2.AH
  - V0.2.Q
  - V0.3.Q.energy_systems
  neighbor:
  - V0.2.AE
  - V0.2.Q
  professional_support:
  - 實際結構、用電、運輸或設備安全需由具責任工程或物理專業以現地條件及標準核定。
  routing_reason: 先鎖單位、系統邊界及歷程。材料劣化、配置或能源供需再選。實際工程交責任者。
- problem: 材料、自然變異與合規
  trigger:
  - 材料或生物差異待辨
  - 組成或自然歷程與表象不同
  suppress:
  - 只讀已知明文
  - 要求高風險生物操作
  candidates:
  - V0.2.AH
  - V0.2.AF
  - V0.3.N.food_safety
  - V0.3.AF.biotech_biosafety
  primary: V0.2.AH
  secondary:
  - V0.2.AF
  - V0.3.N.food_safety
  - V0.3.AF.biotech_biosafety
  neighbor:
  - V0.2.AG
  - V0.2.Q
  professional_support:
  - 實際材料鑑定、處理文物、人體或環境暴露、產品安全與准出由合格保育或材料及環安專業負責。
  routing_reason: 材料來源與物相首查組成。自然變異走生命，食品及生物安全只接治理、合規查驗與有權專業。
- problem: 地層歷史與地貌
  trigger:
  - 地下或地球尺度待辨
  - 局地觀測與長期區域趨勢不符
  suppress:
  - 只讀已知明文
  candidates:
  - V0.2.AI
  - V0.2.W
  - V0.3.AI.mining_mineral_resources
  - V0.3.AI.water_resource_management
  - V0.2.AC
  primary: V0.2.AI
  secondary:
  - V0.2.W
  - V0.3.AI.mining_mineral_resources
  - V0.3.AI.water_resource_management
  - V0.2.AC
  neighbor:
  - V0.2.AC
  - V0.2.AG
  professional_support:
  - 沉陷、地質、地下水及礦務措施由合格地質、水文及土木責任人現勘和決定。
  routing_reason: 重建層位、時間及水體，再比較用地、場址閉區、流域與生態結果。
- problem: 資料治理與用途
  trigger:
  - 知識資料的治理待查
  - 新處理用途或接收者改變
  suppress:
  - 只讀已知明文
  candidates:
  - V0.3.Y.data_governance_privacy
  - V0.2.Y
  - V0.2.X
  - V0.3.F.innovation_ip_strategy
  - V0.3.M.ai_ml_systems
  primary: V0.3.Y.data_governance_privacy
  secondary:
  - V0.2.Y
  - V0.2.X
  - V0.3.F.innovation_ip_strategy
  - V0.3.M.ai_ml_systems
  neighbor:
  - V0.2.Y
  - V0.2.X
  professional_support:
  - 合法性、個資安全和委外由合格資料保護及法務。
  routing_reason: 用途、控制及留存改變優先資料治理；可發現性、分類治理、合作權利、模型表現按爭點補充。
- problem: 科技、制度與設計
  trigger:
  - 新技術落地效果待辨
  - 同一分類或工件在多場域不同
  suppress:
  - 只讀已知明文
  candidates:
  - V0.2.X
  - V0.2.M
  - V0.2.AL
  - V0.3.M.ai_ml_systems
  - V0.3.AL.hci_ux
  primary: V0.2.X
  secondary:
  - V0.2.M
  - V0.2.AL
  - V0.3.M.ai_ml_systems
  - V0.3.AL.hci_ux
  neighbor:
  - V0.2.Q
  - V0.2.A
  professional_support:
  - 實際 AI 治理、敏感資料及公共服務門檻需交有授權的治理、工程、法律與受影響者代表審查。
  routing_reason: 技術分類如何改權威先走 STS。若問題限實作、使用與模型評估，應換包。
- problem: 資本、金融承諾與風險
  trigger:
  - 資金或資源配置待辨
  - 期限曝險或資訊使行為不同
  suppress:
  - 只讀已知明文
  - 要求個人買賣
  candidates:
  - V0.2.D
  - V0.3.D.finance_financial_systems
  - V0.3.D.insurance_risk_transfer
  - V0.3.D.tax
  - V0.3.F.accounting
  primary: V0.2.D
  secondary:
  - V0.3.D.finance_financial_systems
  - V0.3.D.insurance_risk_transfer
  - V0.3.D.tax
  - V0.3.F.accounting
  neighbor:
  - V0.2.S
  - V0.2.F
  - V0.2.A
  professional_support:
  - 真實財務、投資、公共配置或重大政策由責任專業者。
  routing_reason: 要解選擇與分配先用經濟。再分到期、承保、稅務、會計與獨立審計。具體金錢承諾交專業。
- problem: 財務表述與獨立覆核
  trigger:
  - 報告中的主張待核
  - 實際交易與報表或控制記錄不合
  suppress:
  - 只讀已知明文
  candidates:
  - V0.3.F.accounting
  - V0.3.F.auditing_assurance
  - V0.3.F.corporate_governance
  - V0.3.F.risk_compliance_internal_control
  primary: V0.3.F.accounting
  secondary:
  - V0.3.F.auditing_assurance
  - V0.3.F.corporate_governance
  - V0.3.F.risk_compliance_internal_control
  neighbor:
  - V0.2.F
  - V0.2.D
  professional_support:
  - 正式報表、準則適用和稅務申報交具資格會計師與責任人。
  routing_reason: 先核事件、期間、量測與資料。正式確信依獨立證據，治理責任與例外控制各自行使。
- problem: 採用、交付與需求
  trigger:
  - 需求或組織交付待驗
  - 早期訊號與續用或供應不同
  suppress:
  - 只讀已知明文
  candidates:
  - V0.3.F.strategy_entrepreneurship
  - V0.3.F.marketing_consumer
  - V0.3.AL.consumer_studies
  - V0.3.F.operations_supply_chain_logistics
  - V0.2.F
  primary: V0.3.F.strategy_entrepreneurship
  secondary:
  - V0.3.F.marketing_consumer
  - V0.3.AL.consumer_studies
  - V0.3.F.operations_supply_chain_logistics
  - V0.2.F
  neighbor:
  - V0.2.F
  - V0.2.D
  professional_support:
  - 真實融資、勞務和合併承諾交具授權的董事、財務與法務。
  routing_reason: 策略承諾先證反事實。理解、消費負擔、物料流和組織持續性由對應候選。
- problem: 公共風險、權利與救助
  trigger:
  - 公共風險或制度應變待辨
  - 暴露與應變權責分配不清
  suppress:
  - 只讀已知明文
  - 要求戰術重現
  candidates:
  - V0.2.V
  - V0.2.Z
  - V0.3.U.emergency_disaster_management
  - V0.3.V.defence_military_studies
  - V0.2.N
  primary: V0.2.V
  secondary:
  - V0.2.Z
  - V0.3.U.emergency_disaster_management
  - V0.3.V.defence_military_studies
  - V0.2.N
  neighbor:
  - V0.2.O
  - V0.2.T
  professional_support:
  - 需要公共安全措施、權利限制、國防指揮或人道判斷時，由主管者、合格法律及相關專業評估並承擔。
  routing_reason: 先找保護、暴露、措施代價及問責。刑事分制度證據，救助看實際承接，國防限公權監督，人道及健康須專業。
- problem: 服務互連與可達
  trigger:
  - 多端服務的覆蓋待驗
  - 末端和設施正常呈現分歧
  suppress:
  - 只讀已知明文
  candidates:
  - V0.3.Q.utilities_infrastructure
  - V0.2.AD
  - V0.3.Q.telecommunications_networks
  - V0.3.Q.energy_systems
  - V0.3.Q.space_systems
  primary: V0.3.Q.utilities_infrastructure
  secondary:
  - V0.2.AD
  - V0.3.Q.telecommunications_networks
  - V0.3.Q.energy_systems
  - V0.3.Q.space_systems
  neighbor:
  - V0.2.Q
  - V0.2.U
  professional_support:
  - 實際供應、費率、復原及設施安全由公共部門和營運工程負責。
  routing_reason: 資產上線與實際可用分開。空間規劃及交通、電信、供能、民用資料各需對應證據。
- problem: 農食組成與流程
  trigger:
  - 食物供應或安全問題待辨
  - 批次或供應去向關聯未清
  suppress:
  - 只讀已知明文
  candidates:
  - V0.3.AC.agriculture_food_systems
  - V0.3.N.food_safety
  - V0.2.AC
  - V0.3.F.operations_supply_chain_logistics
  - V0.2.N
  primary: V0.3.AC.agriculture_food_systems
  secondary:
  - V0.3.N.food_safety
  - V0.2.AC
  - V0.3.F.operations_supply_chain_logistics
  - V0.2.N
  neighbor:
  - V0.2.AC
  - V0.3.F.operations_supply_chain_logistics
  professional_support:
  - 食品可食安全、農務操作及勞動、採購責任由有責任人。
  routing_reason: 先查季節、產出到供應與損耗。食品安全以批次查驗、職責及衛生專業；健康結果回 N。
- problem: 人本介面與參與
  trigger:
  - 人的任務完成度待辨
  - 可用界面與實際行為有落差
  suppress:
  - 只讀已知明文
  candidates:
  - V0.2.AL
  - V0.3.AL.hci_ux
  - V0.3.AA.disability_studies
  - V0.3.AL.consumer_studies
  - V0.2.G
  primary: V0.2.AL
  secondary:
  - V0.3.AL.hci_ux
  - V0.3.AA.disability_studies
  - V0.3.AL.consumer_studies
  - V0.2.G
  neighbor:
  - V0.2.G
  - V0.2.Q
  professional_support:
  - 真實無障礙符合性、專業介面驗收及敏感操作，交合格設計、可及性、工程及法律責任人。
  routing_reason: 觀察需求、場景及恢復。特定操作才能走 HCI 或無障礙，消費條件與臨床心理保持責任分立。
- problem: 歷史證據與論證
  trigger:
  - 歷史主張或理由待查
  - 時間脈絡或證據位置未分
  suppress:
  - 只讀已知明文
  candidates:
  - V0.2.B
  - V0.2.A
  - V0.2.J
  - V0.2.I
  primary: V0.2.B
  secondary:
  - V0.2.A
  - V0.2.J
  - V0.2.I
  neighbor:
  - V0.2.A
  - V0.2.J
  - V0.2.I
  professional_support:
  - 史料真偽、原件與文物身分由有資格的檔案或保育者。
  routing_reason: 事件重建先查材料與時序。群體機制、地方意義和推論正當性另看。
- problem: 文本、藝術與傳承
  trigger:
  - 表現形式或傳承待比較
  - 異本或場境改變見到的意義
  suppress:
  - 只讀已知明文
  candidates:
  - V0.2.AJ
  - V0.2.AM
  - V0.2.R
  - V0.2.AK
  - V0.2.J
  primary: V0.2.AJ
  secondary:
  - V0.2.AM
  - V0.2.R
  - V0.2.AK
  - V0.2.J
  neighbor:
  - V0.2.R
  - V0.2.B
  professional_support:
  - 著作權、來源認定及受限制記憶作品由法律、編輯、文化社群責任者承接。可分析授權範圍內的形式。
  routing_reason: 敘事形式時間、再脈絡和儀式詮釋有不同首問，視主要爭點選擇。風險涉及著作或文化治理交責任人。
- problem: 小說結構壓力
  trigger:
  - 明示需要小說心法
  - 原創敘事的結構壓力待辨
  suppress:
  - 只讀已知明文
  candidates:
  - CONTEXT.NARRATIVE_PHYSICS
  - V0.2.AJ
  - V0.2.AM
  primary: CONTEXT.NARRATIVE_PHYSICS
  secondary:
  - V0.2.AJ
  - V0.2.AM
  neighbor:
  - V0.2.AJ
  - V0.2.AM
  professional_support:
  - 作品權利或實際身分及敏感事項依編輯、法務與權責人。
  routing_reason: 明示要看虛構力場、自由度及壓強才啟用草案。一般文本形式先用文學。
- problem: 市場結構情境
  trigger:
  - 明示需要金融市場結構心法
  - 要比較市場位置與反證
  suppress:
  - 只讀已知明文
  - 要求個人買賣
  candidates:
  - CONTEXT.FINANCIAL_MARKET_STRUCTURE
  - V0.2.D
  - V0.3.D.finance_financial_systems
  primary: CONTEXT.FINANCIAL_MARKET_STRUCTURE
  secondary:
  - V0.2.D
  - V0.3.D.finance_financial_systems
  neighbor:
  - V0.2.D
  - V0.2.S
  professional_support:
  - 交易、投資及正式風險承擔由合格專業。
  routing_reason: 限市場位置、情境及反證。正式資金、保單或個人買賣由合格專業。
- problem: 觀止角色互動
  trigger:
  - 明示觀止情境心法
  - 虛構角色關係語用待辨
  suppress:
  - 只讀已知明文
  - 要求操控真實人物
  candidates:
  - CONTEXT.GUANZHI_RELATIONAL_LANGUAGE
  - V0.2.R
  - V0.2.AJ
  primary: CONTEXT.GUANZHI_RELATIONAL_LANGUAGE
  secondary:
  - V0.2.R
  - V0.2.AJ
  neighbor:
  - V0.2.R
  - V0.2.AJ
  professional_support:
  - 涉真實人物、隱私或保護問題，照各場景之授權與專業。
  routing_reason: 只在觀止既有世界及授權場景為探索提供角色語言視角。一般語用、文本或真實互動另選。
```

## Method Routes by ID

按候選 ID 搜尋下列標題，只查看候選的 metadata。方法檔取用由 canonical registry 唯一定位。候選法位由各原件保留。

### V0.2.A｜社會學

```yaml
METHOD_ROUTE:
  id: V0.2.A
  name: 社會學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: CLEAN_STANDALONE_PACK_READY
  trigger_signals:
  - 問群體行為如何受分層、權力或角色影響
  - 相同個人處境出現制度性的差別
  suppress_signals: &id001
  - 爭點只在個別病因或已確定的法律效果
  first_observation: 個體行動所在的群體、場域、規範、分層與制度位置
  primary_when: 主爭點符合「問群體行為如何受分層、權力或角色影響」，且需先查這類證據：各包已定義的分析單位、源料與當案事實
  secondary_when: 主要鏡頭已回應整體問題，而「相同個人處境出現制度性的差別」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.J
  - V0.2.G
  - V0.2.E
  compatible_ids:
  - V0.2.J
  professional_support_trigger:
  - 社會工作、高風險決策或涉及個人權利時轉權責領域。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.A_第一組_社會學心法包_純淨版.md
  do_not_use_when: *id001
```

### V0.2.B｜歷史學

```yaml
METHOD_ROUTE:
  id: V0.2.B
  name: 歷史學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: FORMAL_RELEASE_INTEGRATED
  trigger_signals:
  - 有過去事件、原件、異本或制度轉化待辨
  - 個案尺度與長時段敘事互相衝突
  suppress_signals: &id001
  - 只需摘錄明確事實或判現行法律效力
  first_observation: 史料的來源、形成的時間尺度、歷史路徑與制度轉化
  primary_when: 主爭點符合「有過去事件、原件、異本或制度轉化待辨」，且需先查這類證據：各包已定義的分析單位、源料與當案事實
  secondary_when: 主要鏡頭已回應整體問題，而「個案尺度與長時段敘事互相衝突」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.A
  - V0.2.J
  - V0.2.I
  compatible_ids:
  - V0.2.A
  professional_support_trigger:
  - 史料真偽、原件與文物身分由有資格的檔案或保育者。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.B_第二組_歷史學整合版.md
  do_not_use_when: *id001
```

### V0.2.C｜法學

```yaml
METHOD_ROUTE:
  id: V0.2.C
  name: 法學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: FORMAL_RELEASE_READY
  trigger_signals:
  - 同案須確認法律效果、程序或授權
  - 已有爭點但管轄、證據地位或時點仍未核
  suppress_signals: &id001
  - 僅需解釋語句或比較群體結果且無法定效果問題
  first_observation: 法域、法源、權利主體、證據資格與程序狀態
  primary_when: 主爭點符合「同案須確認法律效果、程序或授權」，且需先查這類證據：各包已定義的分析單位、源料與當案事實
  secondary_when: 主要鏡頭已回應整體問題，而「已有爭點但管轄、證據地位或時點仍未核」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.E
  - V0.2.I
  - V0.2.R
  compatible_ids:
  - V0.2.E
  professional_support_trigger:
  - 依本包法域、材料和輸出級別諸門，個案法律意見及處置由適格法務。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.C_第三組_法學整合版.md
  do_not_use_when: *id001
```

### V0.2.D｜經濟學

```yaml
METHOD_ROUTE:
  id: V0.2.D
  name: 經濟學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: FORMAL_RELEASE_READY
  trigger_signals:
  - 選擇受資源或激勵改變
  - 制度、價格或外部性使成本負擔轉移
  suppress_signals: &id001
  - 僅需法律形式、證據真偽或原文摘錄
  first_observation: 稀缺、邊際選擇、交換條件、價格及風險或分配
  primary_when: 主爭點符合「選擇受資源或激勵改變」，且需先查這類證據：各包已定義的分析單位、源料與當案事實
  secondary_when: 主要鏡頭已回應整體問題，而「制度、價格或外部性使成本負擔轉移」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.S
  - V0.2.F
  - V0.2.A
  compatible_ids:
  - V0.2.S
  professional_support_trigger:
  - 真實財務、投資、公共配置或重大政策由責任專業者。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.D_第四組_經濟學整合版.md
  do_not_use_when: *id001
```

### V0.2.E｜政治學

```yaml
METHOD_ROUTE:
  id: V0.2.E
  name: 政治學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: FORMAL_RELEASE
  trigger_signals:
  - 公共權力或共同體決策的形成待辨
  - 規則不同造成集體競爭或問責差異
  suppress_signals: &id001
  - 僅問條文效力或既定事實
  first_observation: 權力取得、機關分工、集體決策、制衡與政治正當性
  primary_when: 主爭點符合「公共權力或共同體決策的形成待辨」，且需先查這類證據：各包已定義的分析單位、源料與當案事實
  secondary_when: 主要鏡頭已回應整體問題，而「規則不同造成集體競爭或問責差異」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.U
  - V0.2.C
  - V0.2.O
  compatible_ids:
  - V0.2.U
  professional_support_trigger:
  - 正式公權決定、法律結論與涉及大眾風險的措施由權責人。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.E_第五組_政治學整合版.md
  do_not_use_when: *id001
```

### V0.2.F｜管理學

```yaml
METHOD_ROUTE:
  id: V0.2.F
  name: 管理學
  class: MAIN_METHOD_PACK
  layer: L2
  standing: INTEGRATED_DRAFT
  trigger_signals:
  - 組織交付、策略、資源或監督發生落差
  - 名義制度與流程承接不一致
  suppress_signals: &id001
  - 爭點只有數學證明、個人診斷或單純法律效力
  first_observation: 組織目標、權責、流程、執行與回饋如何配合
  primary_when: 主爭點符合「組織交付、策略、資源或監督發生落差」，且需先查這類證據：各包已定義的分析單位、源料與當案事實
  secondary_when: 主要鏡頭已回應整體問題，而「名義制度與流程承接不一致」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.Q
  - V0.2.D
  - V0.2.U
  compatible_ids:
  - V0.2.Q
  professional_support_trigger:
  - 真實公司治理、勞動、投資、會計及改變承諾由具授權的專業者。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄 V0.2.F-INTEGRATED_第六組_管理學整合版.md
  do_not_use_when: *id001
```

### V0.2.G｜心理學

```yaml
METHOD_ROUTE:
  id: V0.2.G
  name: 心理學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: INTEGRATED_DRAFT
  trigger_signals:
  - 需要以證據區分心理層次與情境影響
  - 類似行為可能出自不同機制
  suppress_signals: &id001
  - 只有群體制度、檔案盤點或未授權診斷
  first_observation: 認知、情緒、動機、發展、互動情境與個體學習
  primary_when: 主爭點符合「需要以證據區分心理層次與情境影響」，且需先查這類證據：各包已定義的分析單位、源料與當案事實
  secondary_when: 主要鏡頭已回應整體問題，而「類似行為可能出自不同機制」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.A
  - V0.2.H
  - V0.2.N
  compatible_ids:
  - V0.2.A
  professional_support_trigger:
  - 實際診斷、危機、醫療或處遇由合格的臨床專業。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.G-INTEGRATED_第七組心理學整合版.md
  do_not_use_when: *id001
```

### V0.2.H｜教育學

```yaml
METHOD_ROUTE:
  id: V0.2.H
  name: 教育學
  class: MAIN_METHOD_PACK
  layer: L2
  standing: INTEGRATED_DRAFT
  trigger_signals:
  - 教學、評量和真正學習成果沒有對齊
  - 學習者或群體參與不均需辨環境和制度
  suppress_signals: &id001
  - 只有臨床診斷或核實招生法條效力
  first_observation: 教育目的、課程、學習環境、評量及制度化能力形成
  primary_when: 主爭點符合「教學、評量和真正學習成果沒有對齊」，且需先查這類證據：各包已定義的分析單位、源料與當案事實
  secondary_when: 主要鏡頭已回應整體問題，而「學習者或群體參與不均需辨環境和制度」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.G
  - V0.2.A
  - V0.2.AL
  compatible_ids:
  - V0.2.G
  professional_support_trigger:
  - 兒少保護、特教、教育執業與重大政策交對應責任專業。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.H-INTEGRATED_第八組教育學整合版.md
  do_not_use_when: *id001
```

### V0.2.I｜哲學

```yaml
METHOD_ROUTE:
  id: V0.2.I
  name: 哲學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: INTEGRATED_RELEASE
  trigger_signals:
  - 理由是否足以支撐結論待辨
  - 價值衝突、定義或規範正當性是核心
  suppress_signals: &id001
  - 只問可直接查驗的明文事實或需緊急安全處置
  first_observation: 概念、知識條件、論證、價值前提及其推論邊界
  primary_when: 主爭點符合「理由是否足以支撐結論待辨」，且需先查這類證據：各包已定義的分析單位、源料與當案事實
  secondary_when: 主要鏡頭已回應整體問題，而「價值衝突、定義或規範正當性是核心」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.C
  - V0.2.AE
  - V0.2.R
  compatible_ids:
  - V0.2.C
  professional_support_trigger:
  - 高風險倫理判斷及需執業的個案交權責專業。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.I-INTEGRATED_第九組哲學整合版.md
  do_not_use_when: *id001
```

### V0.2.J｜人類學

```yaml
METHOD_ROUTE:
  id: V0.2.J
  name: 人類學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: FORMAL_RELEASE_READY
  trigger_signals:
  - 外部分類與在地說法不一致
  - 意義需從現場、習俗、關係及歷史脈絡理解
  suppress_signals: &id001
  - 僅問正式法定效力或無授權取得受限制知識
  first_observation: 日常實踐、在地分類、關係權力、物件使用與厚描
  primary_when: 主爭點符合「外部分類與在地說法不一致」，且需先查這類證據：各包已定義的分析單位、源料與當案事實
  secondary_when: 主要鏡頭已回應整體問題，而「意義需從現場、習俗、關係及歷史脈絡理解」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.A
  - V0.2.AK
  - V0.2.B
  compatible_ids:
  - V0.2.A
  professional_support_trigger:
  - 社群權威、敏感文化知識與人身安全須有當事社群與相關專業參與。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.J-INTEGRATED_第十組人類學整合版.md
  do_not_use_when: *id001
```

### V0.2.K｜傳播學

```yaml
METHOD_ROUTE:
  id: V0.2.K
  name: 傳播學
  class: MAIN_METHOD_PACK
  layer: L2
  standing: FORMAL_INTEGRATED_VERSION
  trigger_signals:
  - 媒介與理解落差或可見性有變
  - 同一訊息引出不同受眾行為與語境效果
  suppress_signals: &id001
  - 主要疑問只在原件真偽、字面意義或法律效力
  first_observation: 誰向誰說、經過哪個媒介與框架、受眾怎樣接收及擴散
  primary_when: 主爭點符合「媒介與理解落差或可見性有變」，且需先查這類證據：各包已定義的分析單位、源料與當案事實
  secondary_when: 主要鏡頭已回應整體問題，而「同一訊息引出不同受眾行為與語境效果」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.R
  - V0.2.T
  - V0.2.Y
  compatible_ids:
  - V0.2.R
  professional_support_trigger:
  - 公共資訊發布、敏感隱私、醫療及安全風險由責任編務、法務和專業者審查。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.K-INTEGRATED_第十一組傳播學整合版.md
  do_not_use_when: *id001
```

### V0.2.L｜統計學

```yaml
METHOD_ROUTE:
  id: V0.2.L
  name: 統計學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  trigger_signals:
  - 待以樣本推母體或預測外部群體
  - 比例有可疑分母、組成差異或測量漂移
  - 待用觀測資料識別介入效果
  suppress_signals: &id001
  - 只確認已給定的某份文件內容
  - 爭點是規範效力或定義且資料差異不改變判斷
  first_observation: 先辨認 estimand、分母和資料生成過程，再問觀察差異有多少來自選取、量測、隨機波動或處置。
  primary_when: 主爭點符合「待以樣本推母體或預測外部群體」，且需先查這類證據：有納入流程與原始定義的單位資料、測量與缺失紀錄、分派或自然變異證據。
  secondary_when: 主要鏡頭已回應整體問題，而「待用觀測資料識別介入效果」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.D
  - V0.2.G
  compatible_ids:
  - V0.2.D
  professional_support_trigger:
  - 重大裁判、公共發布或監管決策依賴複雜抽樣、非隨機缺失或個體敏感資料時，交統計／調查設計專業者核對設計及資料使用權限。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.L_第12組_統計學_整合版.md
  do_not_use_when: *id001
```

### V0.2.M｜計算機科學

```yaml
METHOD_ROUTE:
  id: V0.2.M
  name: 計算機科學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  trigger_signals:
  - 服務聲稱的結果和權威狀態不一致
  - 並發、重試或版本差異會改變輸出
  suppress_signals: &id001
  - 問題只在文本效力、價格誘因或職責分配
  - 資料處理已固定且只需摘錄
  first_observation: 找輸入如何表示、何處存放權威狀態、操作須維持哪些不變量，再問資源界線與失敗可觀測性。
  primary_when: 主爭點符合「服務聲稱的結果和權威狀態不一致」，且需先查這類證據：介面規格、狀態定義、順序可核對的端點事件與版本固定的典型輸入。
  secondary_when: 主要鏡頭已回應整體問題，而「並發、重試或版本差異會改變輸出」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.F
  - V0.2.L
  compatible_ids:
  - V0.2.F
  professional_support_trigger:
  - 涉上線支付、敏感資料或關鍵基礎服務時，由負責的軟體與資安專業在授權範圍核對設計、測試與證據。個案鑑識和部署由責任人確認。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.M_第13組_計算機科學_整合版.md
  do_not_use_when: *id001
```

### V0.2.N｜醫學／公共衛生／實證醫學

```yaml
METHOD_ROUTE:
  id: V0.2.N
  name: 醫學／公共衛生／實證醫學
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  trigger_signals:
  - 健康結局的個案、群體或方案尺度混用
  - 事件率、介入益害或人群適用性有爭議
  suppress_signals: &id001
  - 只問已核實照護合約的簽署人
  - 工程回報介面的問題已與健康結果分離
  first_observation: 先確定眼前是單人診療、群體健康監測，或介入效果問題。辨認誰在風險中、什麼可測、何時需有責任的專業者。
  primary_when: 主爭點符合「健康結局的個案、群體或方案尺度混用」，且需先查這類證據：個案經確認的縱向紀錄與查驗、定義一致的群體分母、匹配問題的研究證據。
  secondary_when: 主要鏡頭已回應整體問題，而「事件率、介入益害或人群適用性有爭議」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.L
  - V0.2.Q
  compatible_ids:
  - V0.2.L
  professional_support_trigger:
  - 個案診斷、用藥、緊急照護、具體公共衛生處置或裁判中的傷害歸因，由具管轄責任的醫療、衛生或法醫專業承接。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.N_第14組_醫學・公共衛生・實證醫學_整合版.md
  do_not_use_when: *id001
```

### V0.2.O｜國際關係

```yaml
METHOD_ROUTE:
  id: V0.2.O
  name: 國際關係
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  trigger_signals:
  - 跨境主體承諾互相制約
  - 同制度下履約或合作在多個互動回合出現差異
  suppress_signals: &id001
  - 同一機關權限爭議且無境外互動
  - 純條文適用和資格查驗
  first_observation: 找跨境互賴中沒有共同上級可保證履約的行為者，定位承諾、可觀察性和認同如何改變互動。
  primary_when: 主爭點符合「跨境主體承諾互相制約」，且需先查這類證據：有時序的政策互動、履約紀錄、替代行動成本、交叉查驗的行為與言談。
  secondary_when: 主要鏡頭已回應整體問題，而「同制度下履約或合作在多個互動回合出現差異」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.E
  - V0.2.C
  compatible_ids:
  - V0.2.E
  professional_support_trigger:
  - 真實外交立場、條約效力、高風險代表行動由具授權的外交或國際法專業者確認。輸出以比較假說及待查證據為限。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.O_第15組_國際關係_整合版.md
  do_not_use_when: *id001
```

### V0.2.P｜地緣政治

```yaml
METHOD_ROUTE:
  id: V0.2.P
  name: 地緣政治
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  trigger_signals:
  - 跨境位置、可達性或替代路徑影響決策
  - 地圖與實際服務腹地不一致
  suppress_signals: &id001
  - 只涉及同域規範解釋
  - 跨境問題唯一爭點是承諾、位置固定且無效果
  first_observation: 把行政邊界、實際通達網絡與跨境管制分開，找哪些路徑、節點和依賴塑造可選行動。
  primary_when: 主爭點符合「跨境位置、可達性或替代路徑影響決策」，且需先查這類證據：多尺度地圖、路網班表和各路徑容量權限、季節斷點與實際流量。
  secondary_when: 主要鏡頭已回應整體問題，而「地圖與實際服務腹地不一致」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.O
  - V0.2.Q
  compatible_ids:
  - V0.2.O
  professional_support_trigger:
  - 實際民生運輸安全、港口通達和跨境許可，交運輸規劃與主管機關確認。案例不提供行動、打擊或規避安排。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.P_第16組_地緣政治_整合版.md
  do_not_use_when: *id001
```

### V0.2.Q｜系統工程

```yaml
METHOD_ROUTE:
  id: V0.2.Q
  name: 系統工程
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  trigger_signals:
  - 組件各自通過但整合後失敗
  - 版本變化或降級影響跨服務需求
  suppress_signals: &id001
  - 故障已鎖定單一程式規格
  - 單純人事授權或法律效力
  first_observation: 從服務任務倒推需求、工作介面與生命週期驗證，定位哪個局部合格仍可使整體失效。
  primary_when: 主爭點符合「組件各自通過但整合後失敗」，且需先查這類證據：具驗收門檻的需求、版本化介面、整合與使用情境驗證、演練紀錄。
  secondary_when: 主要鏡頭已回應整體問題，而「版本變化或降級影響跨服務需求」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.M
  - V0.2.F
  compatible_ids:
  - V0.2.M
  professional_support_trigger:
  - 真人安全、公共工程、醫材或關鍵服務關切進入實地試驗、驗收、運行切換時，由授權的工程責任人與獨立安全驗證角色簽核。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.Q_第17組_系統工程_整合版.md
  do_not_use_when: *id001
```

### V0.2.R｜語言學／語用學／符號學

```yaml
METHOD_ROUTE:
  id: V0.2.R
  name: 語言學／語用學／符號學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  trigger_signals:
  - 同一表述承擔多種範圍、指稱或言語行動
  - 跨回合或多模態意義對判斷有增量
  suppress_signals: &id001
  - 原文已核且只問可定位的名稱
  - 只問媒體傳輸量或法定程序
  first_observation: 先固定話語、指稱、語境及符號呈現，再分字面內容、語用推論和由介面構成的意義。
  primary_when: 主爭點符合「同一表述承擔多種範圍、指稱或言語行動」，且需先查這類證據：完整原話及版本、前後回合、原始版面、受眾解讀資料。
  secondary_when: 主要鏡頭已回應整體問題，而「跨回合或多模態意義對判斷有增量」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.K
  - V0.2.C
  compatible_ids:
  - V0.2.K
  professional_support_trigger:
  - 法定廣告判定、合意效力、專業翻譯鑑定或具爭議的語意，移交律師及語言專家，保留原件及異讀。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.R_第18組_語言學・語用學・符號學_整合版.md
  do_not_use_when: *id001
```

### V0.2.S｜決策科學／Operations Research

```yaml
METHOD_ROUTE:
  id: V0.2.S
  name: 決策科學／Operations Research
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  trigger_signals:
  - 可選行動彼此衝突且有硬限制
  - 情境變更可能改變排序
  suppress_signals: &id001
  - 唯一問題是授權門檻
  - 任務只能任選一樣且無後果差異
  first_observation: 把可控選項、不可違限制、多目標與不確定性列清楚，先問可行集合，再問偏好與後悔。
  primary_when: 主爭點符合「可選行動彼此衝突且有硬限制」，且需先查這類證據：經授權的限制、選項成本、可比較績效與情境資料。
  secondary_when: 主要鏡頭已回應整體問題，而「情境變更可能改變排序」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.D
  - V0.2.L
  compatible_ids:
  - V0.2.D
  professional_support_trigger:
  - 真實資源配置、法定保全、財務重整或生命安全方案，交主管、律師、財務與工程責任人核准假設和權限。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.S_第19組_決策科學・Operations Research_整合版.md
  do_not_use_when: *id001
```

### V0.2.T｜情報分析

```yaml
METHOD_ROUTE:
  id: V0.2.T
  name: 情報分析
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  trigger_signals:
  - 相斥敘述被不同渠道重覆但來源鏈未知
  - 短期判斷待辨別證據或校準信心
  suppress_signals: &id001
  - 已確定唯一來源且只需摘錄
  - 任務要求越權取得材料
  first_observation: 先列所需判斷及競爭假說，為每項材料追原始可知性、依賴、偏差與缺口。
  primary_when: 主爭點符合「相斥敘述被不同渠道重覆但來源鏈未知」，且需先查這類證據：時間和來源可查的直接材料、獨立歧異資料、可區分假說的觀察。
  secondary_when: 主要鏡頭已回應整體問題，而「短期判斷待辨別證據或校準信心」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.K
  - V0.2.L
  compatible_ids:
  - V0.2.K
  professional_support_trigger:
  - 涉重大司法或國安指控、受保護資料、機構通報與制裁適用，應交有授權的調查、法律或合規角色。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.T_第20組_情報分析_整合版.md
  do_not_use_when: *id001
```

### V0.2.U｜公共政策／公共行政

```yaml
METHOD_ROUTE:
  id: V0.2.U
  name: 公共政策／公共行政
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  trigger_signals:
  - 同文政策在多地產生不同使用與交付
  - 公共工具、責任、資源及前線裁量均涉入
  suppress_signals: &id001
  - 只核公告版本或管轄權
  - 無實施任務的價值辯論
  first_observation: 畫從公共問題到利害關係人接觸的實施鏈，定位每一交接的裁量、資源與回饋。
  primary_when: 主爭點符合「同文政策在多地產生不同使用與交付」，且需先查這類證據：方案對象、各站容量與案件流程紀錄、前線決策及受益分布。
  secondary_when: 主要鏡頭已回應整體問題，而「公共工具、責任、資源及前線裁量均涉入」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.E
  - V0.2.F
  - V0.2.S
  compatible_ids:
  - V0.2.E
  professional_support_trigger:
  - 具體行政處分、補貼資格、執法標準及制度上線由權責機關及法律、評估專業者核定。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.U_第21組_公共政策・公共行政_整合版.md
  do_not_use_when: *id001
```

### V0.2.V｜安全研究

```yaml
METHOD_ROUTE:
  id: V0.2.V
  name: 安全研究
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  trigger_signals:
  - 有人以緊急名義改變長期公共服務
  - 受保護對象與代價分布不清
  suppress_signals: &id001
  - 來源與真偽才是唯一待查點
  - 只讀一張已確認文件
  first_observation: 先標何人或何物受威脅、實質風險與緊急化說法如何作用、誰承擔措施代價
  primary_when: 主爭點符合「有人以緊急名義改變長期公共服務」，且需先查這類證據：按群體與時間拆解的傷害、服務替代性、授權文件及同行複核
  secondary_when: 主要鏡頭已回應整體問題，而「受保護對象與代價分布不清」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.O
  - V0.2.T
  compatible_ids:
  - V0.2.O
  professional_support_trigger:
  - 需要公共安全措施、權利限制、國防指揮或人道判斷時，由主管者、合格法律及相關專業評估並承擔。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.V_第22組_安全研究_整合版.md
  do_not_use_when: *id001
```

### V0.2.W｜地理學／空間研究

```yaml
METHOD_ROUTE:
  id: V0.2.W
  name: 地理學／空間研究
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  trigger_signals:
  - 分布差異疑似行政邊界或尺度產生
  - 設施距離與居民實際可達有落差
  suppress_signals: &id001
  - 唯涉及來源真偽或法規效力
  - 空間位置對結果無增量
  first_observation: 先確定現象的空間單位、尺度、連通和地方條件。確認換界線或量尺會否改圖樣
  primary_when: 主爭點符合「分布差異疑似行政邊界或尺度產生」，且需先查這類證據：尺度與時間可追溯的底圖、服務路網、可步行性和地方觀測
  secondary_when: 主要鏡頭已回應整體問題，而「設施距離與居民實際可達有落差」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.P
  - V0.2.L
  compatible_ids:
  - V0.2.P
  professional_support_trigger:
  - 實際用地、工程交通安全、敏感地點公開及部落資訊使用，由權責規劃者、專家與當事社群授權。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.W_第23組_地理學・空間研究_整合版.md
  do_not_use_when: *id001
```

### V0.2.X｜科技與社會研究 STS

```yaml
METHOD_ROUTE:
  id: V0.2.X
  name: 科技與社會研究 STS
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  trigger_signals:
  - 技術指標已改變治理資格
  - 同工具的制度落地和例外處理不一致
  suppress_signals: &id001
  - 單一可重現程式錯誤即可完整解釋
  - 僅查成文規範
  first_observation: 先追技術分類、使用規範、權威和救濟怎樣在採用中互相塑造
  primary_when: 主爭點符合「技術指標已改變治理資格」，且需先查這類證據：同部署的決策紀錄、欄位規範與受影響者經驗，版本及責任鏈可追
  secondary_when: 主要鏡頭已回應整體問題，而「同工具的制度落地和例外處理不一致」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.Q
  - V0.2.A
  compatible_ids:
  - V0.2.Q
  professional_support_trigger:
  - 實際 AI 治理、敏感資料及公共服務門檻需交有授權的治理、工程、法律與受影響者代表審查。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.X_第24組_科技與社會研究 STS_整合版.md
  do_not_use_when: *id001
```

### V0.2.Y｜資訊科學／知識組織

```yaml
METHOD_ROUTE:
  id: V0.2.Y
  name: 資訊科學／知識組織
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  trigger_signals:
  - 查無資料與持有證據矛盾
  - 版本、詞彙或權限差改變可發現性
  suppress_signals: &id001
  - 已唯一定位物件且只求抄錄
  - 純政策管轄
  first_observation: 先問使用者在什麼詞彙及權限下，能否找到、辨認並追溯所需的知識物件
  primary_when: 主爭點符合「查無資料與持有證據矛盾」，且需先查這類證據：紀錄集、版本來源、查詢軌跡及由任務定義的相關性判讀
  secondary_when: 主要鏡頭已回應整體問題，而「版本、詞彙或權限差改變可發現性」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.M
  - V0.2.R
  compatible_ids:
  - V0.2.M
  professional_support_trigger:
  - 處理個資、交易憑證或有法律效果的保存、交割、披露，由檔案專業、系統管理者及法律責任人核定。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.Y_第25組_資訊科學・知識組織_整合版.md
  do_not_use_when: *id001
```

### V0.2.Z｜犯罪學／刑事司法研究

```yaml
METHOD_ROUTE:
  id: V0.2.Z
  name: 犯罪學／刑事司法研究
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  trigger_signals:
  - 事件數与通報與定罪混用
  - 要評估預防、流程或回歸結果
  suppress_signals: &id001
  - 個案歸責只有法條門檻
  - 僅知匿名錄案未有定義和比較
  first_observation: 把實際被害、報案、警察紀錄、裁判及處遇結果分開，追群體及流程如何改變觀察
  primary_when: 主爭點符合「事件數与通報與定罪混用」，且需先查這類證據：定義一致的事件與人口、被害調查、案件流程及教育支持結果
  secondary_when: 主要鏡頭已回應整體問題，而「要評估預防、流程或回歸結果」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.C
  - V0.2.L
  compatible_ids:
  - V0.2.C
  professional_support_trigger:
  - 個案定罪、司法調查、受害者安全和實際處遇由具授權刑事、社工及臨床人員承擔。可先做匿名制度審讀。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.Z_第26組_犯罪學・刑事司法研究_整合版.md
  do_not_use_when: *id001
```

### V0.2.AA｜社會工作／社會政策

```yaml
METHOD_ROUTE:
  id: V0.2.AA
  name: 社會工作／社會政策
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  trigger_signals:
  - 本人生活目標和服務結果分離
  - 多個給付或照護入口中斷
  suppress_signals: &id001
  - 只有未授權的私密猜測
  - 只問核准文件上的期限
  first_observation: 先聽當事人目標，重建人與環境、實際關係、服務缺口及可行支持
  primary_when: 主爭點符合「本人生活目標和服務結果分離」，且需先查這類證據：當事人敘述與偏好、可取得的環境及轉介證據、服務接續紀錄
  secondary_when: 主要鏡頭已回應整體問題，而「多個給付或照護入口中斷」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.N
  - V0.2.U
  compatible_ids:
  - V0.2.N
  professional_support_trigger:
  - 個人安全、法定通報、兒少保護、照護計畫及實際給付資格，交有授權的社工、醫療及法律角色。公開處理僅用去識別資料。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AA_第27組_社會工作・社會政策_整合版.md
  do_not_use_when: *id001
```

### V0.2.AB｜人口學／人口研究

```yaml
METHOD_ROUTE:
  id: V0.2.AB
  name: 人口學／人口研究
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  trigger_signals:
  - 同時有人口總數和事件率的變化
  - 需要年齡、世代或遷移資料以評估群體
  suppress_signals: &id001
  - 單一戶籍資格
  - 分布與人口事件無關
  first_observation: 先區分人口存量、期間流量、風險暴露及世代替換，問總量變化來自組成或率
  primary_when: 主爭點符合「同時有人口總數和事件率的變化」，且需先查這類證據：可配分母的生命事件、住居遷移、人口盤點與明確世代
  secondary_when: 主要鏡頭已回應整體問題，而「需要年齡、世代或遷移資料以評估群體」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.L
  - V0.2.AA
  compatible_ids:
  - V0.2.L
  professional_support_trigger:
  - 使用小區域個資、制定法定給付或發布人口預測，由人口學、統計、地方責任機關和法務覆核。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AB_第28組_人口學・人口研究_整合版.md
  do_not_use_when: *id001
```

### V0.2.AC｜環境／氣候／生態系統研究

```yaml
METHOD_ROUTE:
  id: V0.2.AC
  name: 環境／氣候／生態系統研究
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  trigger_signals:
  - 環境異常可能跨空間或累積
  - 多重背景壓力與受體變化待辨
  suppress_signals: &id001
  - 僅問產權或公文版本
  - 沒有環境後果關係
  first_observation: 先畫壓力、受體、暴露、系統邊界與反事實基線，追變動跨時間和上下游的累積
  primary_when: 主爭點符合「環境異常可能跨空間或累積」，且需先查這類證據：有校準的長期與對照監測、背景條件、生態受體資料
  secondary_when: 主要鏡頭已回應整體問題，而「多重背景壓力與受體變化待辨」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.W
  - V0.2.L
  compatible_ids:
  - V0.2.W
  professional_support_trigger:
  - 涉及環評、環境安全、實地處置或受威脅棲地，由具責任專家、主管機關及相關社群審查。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AC_第29組_環境・氣候・生態系統研究_整合版.md
  do_not_use_when: *id001
```

### V0.2.AD｜都市／建成環境研究

```yaml
METHOD_ROUTE:
  id: V0.2.AD
  name: 都市／建成環境研究
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  trigger_signals:
  - 都市用地、移動與住宅服務互相牽動
  - 示意可用與實際使用不同
  suppress_signals: &id001
  - 僅有地界核對
  - 單一工程部件失效
  first_observation: 先追土地、建物、公共空間、運輸和住房如何共同形成實住、可達與外部影響
  primary_when: 主爭點符合「都市用地、移動與住宅服務互相牽動」，且需先查這類證據：分時活動與路網、基地替代案、住房和設施容量、居民觀察
  secondary_when: 主要鏡頭已回應整體問題，而「示意可用與實際使用不同」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.W
  - V0.2.Q
  compatible_ids:
  - V0.2.W
  professional_support_trigger:
  - 具體都市計畫、工程安全、無障礙或租住法律，交規劃師、工程及法務依當地審查。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AD_第30組_都市・建成環境研究_整合版.md
  do_not_use_when: *id001
```

### V0.2.AE｜數學／形式方法

```yaml
METHOD_ROUTE:
  id: V0.2.AE
  name: 數學／形式方法
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  trigger_signals:
  - 有全稱保證或互斥規則待證
  - 局部通過但整體可能不一致
  suppress_signals: &id001
  - 只需算固定已知值
  - 經驗因果為主且沒有形式問題
  first_observation: 先寫定義、量詞、約束和可證性。找最小反例及哪些結論僅在模型內成立
  primary_when: 主爭點符合「有全稱保證或互斥規則待證」，且需先查這類證據：可核對定義、形式規約、證明與反例
  secondary_when: 主要鏡頭已回應整體問題，而「局部通過但整體可能不一致」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.M
  - V0.2.S
  compatible_ids:
  - V0.2.M
  professional_support_trigger:
  - 把形式結論用於實際支付、評選、權利或安全保證時，由形式驗證與領域權責共同確認假設對現實有效。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AE_第31組_數學・形式方法_整合版.md
  do_not_use_when: *id001
```

### V0.2.AF｜生物學／生命科學

```yaml
METHOD_ROUTE:
  id: V0.2.AF
  name: 生物學／生命科學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  trigger_signals:
  - 不同生物層級可能混為同一原因
  - 自然觀測的表型或族群差需查機制
  suppress_signals: &id001
  - 純照護診斷或法律資格
  - 需要生成或試驗高風險生物功能
  first_observation: 先辨生物層級和性狀。區分個體、發育經驗、環境反應、族群組成及代際變化
  primary_when: 主爭點符合「不同生物層級可能混為同一原因」，且需先查這類證據：可重複、標明生命階段的自然觀測、族群長期資料和形態紀錄
  secondary_when: 主要鏡頭已回應整體問題，而「自然觀測的表型或族群差需查機制」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.AC
  - V0.2.N
  compatible_ids:
  - V0.2.AC
  professional_support_trigger:
  - 實際保育鑑定、遺傳隱私及生物安全風險交具資格組織。只做概念性、非介入觀察及已授權材料解讀。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AF_第32組_生物學・生命科學_整合版.md
  do_not_use_when: *id001
```

### V0.2.AG｜物理學／物理系統

```yaml
METHOD_ROUTE:
  id: V0.2.AG
  name: 物理學／物理系統
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  trigger_signals:
  - 需要物理傳輸、守恆或跨尺度解釋
  - 不同配置或讀數可能衝突
  suppress_signals: &id001
  - 只要求法律、制度或簽署資格
  - 實驗與工程資料均無且只要求定論
  first_observation: 先界定物理系統邊界、守恆量、驅動和時間尺度，問模型允許哪些變化
  primary_when: 主爭點符合「需要物理傳輸、守恆或跨尺度解釋」，且需先查這類證據：校準、帶單位時序，受控條件、初始狀態與可重複觀測
  secondary_when: 主要鏡頭已回應整體問題，而「不同配置或讀數可能衝突」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.AE
  - V0.2.Q
  compatible_ids:
  - V0.2.AE
  professional_support_trigger:
  - 實際結構、用電、運輸或設備安全需由具責任工程或物理專業以現地條件及標準核定。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AG_第33組_物理學・物理系統_整合版.md
  do_not_use_when: *id001
```

### V0.2.AH｜化學／材料科學

```yaml
METHOD_ROUTE:
  id: V0.2.AH
  name: 化學／材料科學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  trigger_signals:
  - 成分、結構、製程或老化可改變結果
  - 同標示材料表現不同
  suppress_signals: &id001
  - 只問契約條款或作品權利
  - 只能取得未驗真的單張照片且要求實地結論
  first_observation: 先定位物質身分、組成與微結構、加工履歷、暴露及量到的性能，辨候選變化路徑
  primary_when: 主爭點符合「成分、結構、製程或老化可改變結果」，且需先查這類證據：有可追批次的樣品資訊、使用環境、可信的材料與測試結果
  secondary_when: 主要鏡頭已回應整體問題，而「同標示材料表現不同」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.AG
  - V0.2.Q
  compatible_ids:
  - V0.2.AG
  professional_support_trigger:
  - 實際材料鑑定、處理文物、人體或環境暴露、產品安全與准出由合格保育或材料及環安專業負責。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AH_第34組_化學・材料科學_整合版.md
  do_not_use_when: *id001
```

### V0.2.AI｜地球科學／地質與地球系統

```yaml
METHOD_ROUTE:
  id: V0.2.AI
  name: 地球科學／地質與地球系統
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  trigger_signals:
  - 地下異質性或地質歷史可能改結果
  - 淺層觀察和區域趨勢衝突
  suppress_signals: &id001
  - 只核土地或設備法定文件
  - 完全無地質、地貌或水文問題
  first_observation: 先重建地層、水、地形和演變，分地表現象、深度來源和跨期地球過程
  primary_when: 主爭點符合「地下異質性或地質歷史可能改結果」，且需先查這類證據：合格地質斷面、場地歷史、獨立水位及位移時序
  secondary_when: 主要鏡頭已回應整體問題，而「淺層觀察和區域趨勢衝突」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.AC
  - V0.2.AG
  compatible_ids:
  - V0.2.AC
  professional_support_trigger:
  - 沉陷、地質、地下水及礦務措施由合格地質、水文及土木責任人現勘和決定。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AI_第35組_地球科學・地質與地球系統_整合版.md
  do_not_use_when: *id001
```

### V0.2.AJ｜文學／敘事學

```yaml
METHOD_ROUTE:
  id: V0.2.AJ
  name: 文學／敘事學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  trigger_signals:
  - 情節相同但作品形式及讀者認知不同
  - 敘述位置、時間或文類有獨立影響
  suppress_signals: &id001
  - 只核署名或歷史事件真偽
  - 只需不涉形式的單句摘錄
  first_observation: 先拆事件、講述者、誰可知與讀者何時獲知，再問形式如何組織意義
  primary_when: 主爭點符合「情節相同但作品形式及讀者認知不同」，且需先查這類證據：作品原版及異本、段落前後、閱讀位置及視聽敘事
  secondary_when: 主要鏡頭已回應整體問題，而「敘述位置、時間或文類有獨立影響」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.R
  - V0.2.B
  compatible_ids:
  - V0.2.R
  professional_support_trigger:
  - 著作權、來源認定及受限制記憶作品由法律、編輯、文化社群責任者承接。可分析授權範圍內的形式。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AJ_第36組_文學・敘事學_整合版.md
  do_not_use_when: *id001
```

### V0.2.AK｜宗教學／神話學

```yaml
METHOD_ROUTE:
  id: V0.2.AK
  name: 宗教學／神話學
  class: MAIN_METHOD_PACK
  layer: L1
  standing: REVIEW_READY
  trigger_signals:
  - 公共描述與群體實踐語意不一致
  - 神聖時空、神話與權威影響理解
  suppress_signals: &id001
  - 只定位一筆日程資料
  - 無授權去查受限制信仰材料
  first_observation: 先看參與者如何使實踐、敘事、場所及時間取得神聖或共同體意義，保留各種位置
  primary_when: 主爭點符合「公共描述與群體實踐語意不一致」，且需先查這類證據：多位置的敘述、公開儀式語境、歷史異本及實際管理權
  secondary_when: 主要鏡頭已回應整體問題，而「神聖時空、神話與權威影響理解」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.J
  - V0.2.AJ
  compatible_ids:
  - V0.2.J
  professional_support_trigger:
  - 涉及活態宗教、受限制材料、權利或保護爭議，依具責任社群與法律、文化專業確認邊界。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AK_第37組_宗教學・神話學_整合版.md
  do_not_use_when: *id001
```

### V0.2.AL｜設計學／Human-Centered Design

```yaml
METHOD_ROUTE:
  id: V0.2.AL
  name: 設計學／Human-Centered Design
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  trigger_signals:
  - 介面看似明確但任務失敗
  - 服務對不同使用者的完成路徑不一
  suppress_signals: &id001
  - 唯一爭點為規範和文件效力
  - 只需複製已核內容
  first_observation: 先觀察人的工作、情境、障礙及修正行動，原型能否實際讓對象完成正確任務
  primary_when: 主爭點符合「介面看似明確但任務失敗」，且需先查這類證據：真實任務觀察、有差異的參與者、原型對照及錯誤路徑
  secondary_when: 主要鏡頭已回應整體問題，而「服務對不同使用者的完成路徑不一」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.G
  - V0.2.Q
  compatible_ids:
  - V0.2.G
  professional_support_trigger:
  - 真實無障礙符合性、專業介面驗收及敏感操作，交合格設計、可及性、工程及法律責任人。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AL_第38組_設計學・Human-Centered Design_整合版.md
  do_not_use_when: *id001
```

### V0.2.AM｜藝術／文化／文化遺產研究

```yaml
METHOD_ROUTE:
  id: V0.2.AM
  name: 藝術／文化／文化遺產研究
  class: MAIN_METHOD_PACK
  layer: L2
  standing: REVIEW_READY
  trigger_signals:
  - 物件、再利用與傳承存在競爭價值
  - 複製和遷移可能改變場境
  suppress_signals: &id001
  - 只問物理性質或法定日期
  - 無權查敏感社群內容
  first_observation: 先辨視覺表現、物件來源、場所價值與活態傳承，問一次改造或展示會保留並抹去哪一層
  primary_when: 主爭點符合「物件、再利用與傳承存在競爭價值」，且需先查這類證據：受授權的作品和場址觀察、來源鏈、社群見證與狀態紀錄
  secondary_when: 主要鏡頭已回應整體問題，而「複製和遷移可能改變場境」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.AK
  - V0.2.AH
  compatible_ids:
  - V0.2.AK
  professional_support_trigger:
  - 實際修復、返還、借展、敏感文化存取、保護指定和相關權利由文化社群、有責任的保育及法務承接。
  canonical_file: ../02_MAIN_METHOD_PACKS/學科心法總目錄_V0.2.AM_第39組_藝術・文化・文化遺產研究_整合版.md
  do_not_use_when: *id001
```

### V0.3.A.labor_industrial_relations｜勞動／工業關係

```yaml
METHOD_ROUTE:
  id: V0.3.A.labor_industrial_relations
  name: 勞動／工業關係
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 契約形式與工作實況不合
  - 代表與執行範圍有缺口
  suppress_signals: &id001
  - 只查章程日期
  first_observation: 先比契約、實際指揮及集體接入
  primary_when: 主爭點符合「契約形式與工作實況不合」，且需先查這類證據：實際任務與工時、代表紀錄、協商及申訴
  secondary_when: 主要鏡頭已回應整體問題，而「代表與執行範圍有缺口」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.A
  - V0.3.F.organizational_behavior_hr
  compatible_ids:
  - V0.2.A
  professional_support_trigger:
  - 實際勞動資格、仲裁及工作安全由勞務專業與授權代表。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.A.labor_industrial_relations_勞動・工業關係_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.A
```

### V0.3.AA.aging_gerontology｜高齡／老年學

```yaml
METHOD_ROUTE:
  id: V0.3.AA.aging_gerontology
  name: 高齡／老年學
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 活動下降未確認功能
  - 長期支持條件在變
  suppress_signals: &id001
  - 只檢程序文件
  first_observation: 分年齡、功能、意願與環境支持
  primary_when: 主爭點符合「活動下降未確認功能」，且需先查這類證據：本人目標、日常活動及環境時序
  secondary_when: 主要鏡頭已回應整體問題，而「長期支持條件在變」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.AA
  - V0.2.N
  compatible_ids:
  - V0.2.AA
  professional_support_trigger:
  - 個案健康、決策能力與長照由具資格專業及當事人決定。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AA.aging_gerontology_高齡・老年學_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.AA
```

### V0.3.AA.care_systems｜照護系統

```yaml
METHOD_ROUTE:
  id: V0.3.AA.care_systems
  name: 照護系統
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 跨單位照護或身分變動
  - 無確認責任接手
  suppress_signals: &id001
  - 只問已核發文人
  first_observation: 分照護需求、交接、可提供時間與回饋
  primary_when: 主爭點符合「跨單位照護或身分變動」，且需先查這類證據：受權需求、交接收件、服務實際時間
  secondary_when: 主要鏡頭已回應整體問題，而「無確認責任接手」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.AA
  - V0.2.N
  compatible_ids:
  - V0.2.AA
  professional_support_trigger:
  - 照護處遇、臨床、危機及保密均交具責任者。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AA.care_systems_照護系統_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.AA
```

### V0.3.AA.child_development_protection｜兒少發展／保護

```yaml
METHOD_ROUTE:
  id: V0.3.AA.child_development_protection
  name: 兒少發展／保護
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 兒少意見沒有進入決策
  - 保護紀錄有轉介缺口
  suppress_signals: &id001
  - 純文件擷取
  first_observation: 先定位年齡處境、兒少意見及保護授權
  primary_when: 主爭點符合「兒少意見沒有進入決策」，且需先查這類證據：經合規取得的本人意見、個案支持、交接及責任資料
  secondary_when: 主要鏡頭已回應整體問題，而「保護紀錄有轉介缺口」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.AA
  - V0.2.H
  compatible_ids:
  - V0.2.AA
  professional_support_trigger:
  - 實際安全危機、保護評估、通報、照護與個案資料交授權保護或醫療法律人員。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AA.child_development_protection_兒少發展・保護_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.AA
```

### V0.3.AA.disability_studies｜障礙研究

```yaml
METHOD_ROUTE:
  id: V0.3.AA.disability_studies
  name: 障礙研究
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 同環境有穩定參與落差
  - 當事人反映障礙而物理檢表通過
  suppress_signals: &id001
  - 只問文件版本
  first_observation: 分活動、功能、環境和制度障礙
  primary_when: 主爭點符合「同環境有穩定參與落差」，且需先查這類證據：本人適用任務、場地觀察、規則及替代方案
  secondary_when: 主要鏡頭已回應整體問題，而「當事人反映障礙而物理檢表通過」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.AA
  - V0.2.AL
  compatible_ids:
  - V0.2.AA
  professional_support_trigger:
  - 當事人權利、安全及可及標準由自我倡議、受權專業與法務。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AA.disability_studies_障礙研究_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.AA
```

### V0.3.AA.family_studies｜家庭研究

```yaml
METHOD_ROUTE:
  id: V0.3.AA.family_studies
  name: 家庭研究
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 照護負擔未清
  - 搬家及工作調動改家庭安排
  suppress_signals: &id001
  - 只問出生證明印刷值
  first_observation: 從各人生活與照護工作重建
  primary_when: 主爭點符合「照護負擔未清」，且需先查這類證據：分別同意的意見、照護時間與接手紀錄
  secondary_when: 主要鏡頭已回應整體問題，而「搬家及工作調動改家庭安排」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.AA
  - V0.2.G
  compatible_ids:
  - V0.2.AA
  professional_support_trigger:
  - 兒少、個人安全、家庭權利和資源分配由負責社工和法律人員。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AA.family_studies_家庭研究_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.AA
```

### V0.3.AC.agriculture_food_systems｜農業／食物系統

```yaml
METHOD_ROUTE:
  id: V0.3.AC.agriculture_food_systems
  name: 農業／食物系統
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 產量與實際供應不同
  - 季節或品質門檻影響農戶
  suppress_signals: &id001
  - 純粹土地法位
  first_observation: 分產出、損耗、流通、可及與季節
  primary_when: 主爭點符合「產量與實際供應不同」，且需先查這類證據：季節、批次去向、損耗、購買及交付資料
  secondary_when: 主要鏡頭已回應整體問題，而「季節或品質門檻影響農戶」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.AC
  - V0.3.F.operations_supply_chain_logistics
  compatible_ids:
  - V0.2.AC
  professional_support_trigger:
  - 食品可食安全、農務操作及勞動、採購責任由有責任人。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AC.agriculture_food_systems_農業・食物系統_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.AC
```

### V0.3.AC.forestry_fisheries_conservation｜森林／漁業／保育

```yaml
METHOD_ROUTE:
  id: V0.3.AC.forestry_fisheries_conservation
  name: 森林／漁業／保育
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 資源件數變且活動強度不同
  - 保育與利用的監測未對齊
  suppress_signals: &id001
  - 只問法律登記
  first_observation: 拆觀測、努力量、棲地與受影響者
  primary_when: 主爭點符合「資源件數變且活動強度不同」，且需先查這類證據：可重複監測、取用及用途、棲地和社群資料
  secondary_when: 主要鏡頭已回應整體問題，而「保育與利用的監測未對齊」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.AC
  - V0.2.AF
  compatible_ids:
  - V0.2.AC
  professional_support_trigger:
  - 實地保育、捕撈、林業許可和社群資料由權責者與社群授權。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AC.forestry_fisheries_conservation_森林・漁業・保育_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.AC
```

### V0.3.AD.transport_mobility｜交通／運輸

```yaml
METHOD_ROUTE:
  id: V0.3.AD.transport_mobility
  name: 交通／運輸
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 班次很多但旅程失敗
  - 某些轉乘和時段無服務
  suppress_signals: &id001
  - 只判承運合約格式
  first_observation: 從起訖及時段重建各運具交接
  primary_when: 主爭點符合「班次很多但旅程失敗」，且需先查這類證據：實際起訖、班表、載運與可及觀察
  secondary_when: 主要鏡頭已回應整體問題，而「某些轉乘和時段無服務」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.AD
  - V0.2.W
  compatible_ids:
  - V0.2.AD
  professional_support_trigger:
  - 真實交通調度、安全、工程和法規由有權營運及專業。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AD.transport_mobility_交通・運輸_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.AD
```

### V0.3.AF.biotech_biosafety｜生技／生物安全

```yaml
METHOD_ROUTE:
  id: V0.3.AF.biotech_biosafety
  name: 生技／生物安全
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 機構計畫用途或供應責任有變
  - 稽核與事件紀錄缺接手
  suppress_signals: &id001
  - 要求操作、改造或規避安全篩查
  first_observation: 先查授權、用途、責任和狀態
  primary_when: 主爭點符合「機構計畫用途或供應責任有變」，且需先查這類證據：已批准安全審查、訓練責任及事件紀錄
  secondary_when: 主要鏡頭已回應整體問題，而「稽核與事件紀錄缺接手」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.AF
  - V0.3.I.bioethics
  compatible_ids:
  - V0.2.AF
  professional_support_trigger:
  - 具體材料、操作或暴露、事件處置與風險定級須交依法授權生物安全責任者。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AF.biotech_biosafety_生技・生物安全_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.AF
```

### V0.3.AI.mining_mineral_resources｜礦業／礦產

```yaml
METHOD_ROUTE:
  id: V0.3.AI.mining_mineral_resources
  name: 礦業／礦產
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 現場營運與閉區責任接續不明
  - 地表修復後仍須查長程風險
  suppress_signals: &id001
  - 要求開採或危險物操作
  first_observation: 核場址條件、許可、復育及事後維護
  primary_when: 主爭點符合「現場營運與閉區責任接續不明」，且需先查這類證據：核准場址資料、覆土或水質見證、責任和資源
  secondary_when: 主要鏡頭已回應整體問題，而「地表修復後仍須查長程風險」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.AI
  - V0.2.AC
  compatible_ids:
  - V0.2.AI
  professional_support_trigger:
  - 工地採掘、資源與污染評估、安全及材料須由場址授權工程和環境專業。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AI.mining_mineral_resources_礦業・礦產_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.AI
```

### V0.3.AI.water_resource_management｜水資源

```yaml
METHOD_ROUTE:
  id: V0.3.AI.water_resource_management
  name: 水資源
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 取用、供應及時段失配
  - 單井與區域資料不一致
  suppress_signals: &id001
  - 只讀地籍權人
  first_observation: 先列入出、儲存與不同負擔
  primary_when: 主爭點符合「取用、供應及時段失配」，且需先查這類證據：流量、水位、庫容及使用時序
  secondary_when: 主要鏡頭已回應整體問題，而「單井與區域資料不一致」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.AI
  - V0.2.AC
  compatible_ids:
  - V0.2.AI
  professional_support_trigger:
  - 調水、取水、水質、災害和權利由水文及主管工程。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AI.water_resource_management_水資源_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.AI
```

### V0.3.AL.consumer_studies｜消費者研究

```yaml
METHOD_ROUTE:
  id: V0.3.AL.consumer_studies
  name: 消費者研究
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 接受者多但大量退費
  - 資訊或選項不等價
  suppress_signals: &id001
  - 只確認條款版本
  first_observation: 追資訊、退出成本與後果
  primary_when: 主爭點符合「接受者多但大量退費」，且需先查這類證據：同一情境的條款、呈現、交易與申訴
  secondary_when: 主要鏡頭已回應整體問題，而「資訊或選項不等價」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.AL
  - V0.3.F.marketing_consumer
  compatible_ids:
  - V0.2.AL
  professional_support_trigger:
  - 實際申訴、退款、個資及金融行為責任依具資格專業。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AL.consumer_studies_消費者研究_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.AL
```

### V0.3.AL.hci_ux｜人機互動／UX

```yaml
METHOD_ROUTE:
  id: V0.3.AL.hci_ux
  name: 人機互動／UX
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 使用者畫面操作易失敗
  - 首用與熟用差異
  suppress_signals: &id001
  - 只關合約或後端驗真
  first_observation: 定任務、觀察、比較錯誤及恢復
  primary_when: 主爭點符合「使用者畫面操作易失敗」，且需先查這類證據：可定義任務、對照原型和真實錯誤
  secondary_when: 主要鏡頭已回應整體問題，而「首用與熟用差異」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.AL
  - V0.2.G
  compatible_ids:
  - V0.2.AL
  professional_support_trigger:
  - 實際敏感流程、無障礙及版面合規由主管與有責任專業。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.AL.hci_ux_人機互動・UX_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.AL
```

### V0.3.D.finance_financial_systems｜金融／銀行／資本市場

```yaml
METHOD_ROUTE:
  id: V0.3.D.finance_financial_systems
  name: 金融／銀行／資本市場
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 資金承諾和期限不一致
  - 市場流量與中介接口待查
  suppress_signals: &id001
  - 單純查法律身份
  - 請求買賣或個案資金安排
  first_observation: 先拆資產與資金期限、可變現性、損失吸收及中介責任
  primary_when: 主爭點符合「資金承諾和期限不一致」，且需先查這類證據：確定到期表、資產限制、可用現金、利害人紀錄
  secondary_when: 主要鏡頭已回應整體問題，而「市場流量與中介接口待查」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.D
  - V0.3.F.accounting
  compatible_ids:
  - V0.2.D
  professional_support_trigger:
  - 實際銀行及金融監理、資金調度、定價、投資與處置由責任專業者。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.D.finance_financial_systems_金融・銀行・資本市場_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.D
```

### V0.3.D.insurance_risk_transfer｜保險／風險移轉

```yaml
METHOD_ROUTE:
  id: V0.3.D.insurance_risk_transfer
  name: 保險／風險移轉
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 名義承保與實際事件有距離
  - 分層或共同暴露待辨
  suppress_signals: &id001
  - 只問無損失關聯的權限
  first_observation: 先追誰承擔何種事件與期間、哪些風險實際留存
  primary_when: 主爭點符合「名義承保與實際事件有距離」，且需先查這類證據：完整保單、事故事實、暴露和理賠紀錄
  secondary_when: 主要鏡頭已回應整體問題，而「分層或共同暴露待辨」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.D
  - V0.3.D.finance_financial_systems
  compatible_ids:
  - V0.2.D
  professional_support_trigger:
  - 個案給付、精算、資本和理賠指示交合格保險、精算及法務。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.D.insurance_risk_transfer_保險・風險移轉_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.D
```

### V0.3.D.tax｜稅務

```yaml
METHOD_ROUTE:
  id: V0.3.D.tax
  name: 稅務
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 多地關係企業分工和價格待查
  - 發票、履約、對價有差
  suppress_signals: &id001
  - 只查法定截止日
  - 要求代行申報
  first_observation: 先辨納稅主體、交易、連結點與時間，再定位查證資料
  primary_when: 主爭點符合「多地關係企業分工和價格待查」，且需先查這類證據：契約、交付、對價、發票與會計勾稽
  secondary_when: 主要鏡頭已回應整體問題，而「發票、履約、對價有差」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.D
  - V0.3.F.accounting
  compatible_ids:
  - V0.2.D
  professional_support_trigger:
  - 任何納稅義務、稅率、申報、選擇與爭訟由實際法域稅務專業及責任人。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.D.tax_稅務_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.D
```

### V0.3.F.accounting｜會計

```yaml
METHOD_ROUTE:
  id: V0.3.F.accounting
  name: 會計
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 同交易在現金和報表期間不同
  - 有變更估計或分類
  suppress_signals: &id001
  - 只判治理權限
  - 要求獨立確信
  first_observation: 先把交易事實、控制、科目、期間與估計變更釐清
  primary_when: 主爭點符合「同交易在現金和報表期間不同」，且需先查這類證據：契約、交付、分錄、銀行與對帳
  secondary_when: 主要鏡頭已回應整體問題，而「有變更估計或分類」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.F
  - V0.2.D
  compatible_ids:
  - V0.2.F
  professional_support_trigger:
  - 正式報表、準則適用和稅務申報交具資格會計師與責任人。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.F.accounting_會計_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.F
```

### V0.3.F.auditing_assurance｜審計／確信

```yaml
METHOD_ROUTE:
  id: V0.3.F.auditing_assurance
  name: 審計／確信
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 報表主張要獨立驗證
  - 內外部來源可能同源
  suppress_signals: &id001
  - 單純對帳分類
  - 要求發出確信
  first_observation: 先鎖特定主張、確信範圍、獨立性及充分適切證據
  primary_when: 主爭點符合「報表主張要獨立驗證」，且需先查這類證據：獨立來源、可重作的抽查與控制活動證據
  secondary_when: 主要鏡頭已回應整體問題，而「內外部來源可能同源」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.3.F.accounting
  - V0.2.F
  compatible_ids:
  - V0.2.F
  professional_support_trigger:
  - 正式審計、確信和任何簽署由具資格且具獨立性的專業人員。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.F.auditing_assurance_審計・確信_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.F
```

### V0.3.F.corporate_governance｜公司治理

```yaml
METHOD_ROUTE:
  id: V0.3.F.corporate_governance
  name: 公司治理
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 決定有權責或利益衝突
  - 多機關核准與監督不清
  suppress_signals: &id001
  - 單一門市流程或加總
  first_observation: 先追誰提議、批准、執行、監督與揭露衝突
  primary_when: 主爭點符合「決定有權責或利益衝突」，且需先查這類證據：章程及授權、會議材料、利害關係、書面決議
  secondary_when: 主要鏡頭已回應整體問題，而「多機關核准與監督不清」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.F
  - V0.2.E
  compatible_ids:
  - V0.2.F
  professional_support_trigger:
  - 董事義務、表決效力、大股東與證券揭露，交具資格法務及權責治理機關。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.F.corporate_governance_公司治理_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.F
```

### V0.3.F.innovation_ip_strategy｜創新／智慧財產策略

```yaml
METHOD_ROUTE:
  id: V0.3.F.innovation_ip_strategy
  name: 創新／智慧財產策略
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 新合作但成果來源未分清楚
  - 將展示或發行而授權未核
  suppress_signals: &id001
  - 只有市場價格或資格查詢
  first_observation: 區分來源、貢獻、公開狀態及業務用途
  primary_when: 主爭點符合「新合作但成果來源未分清楚」，且需先查這類證據：實際成果、過程版本、雙方合同和公開紀錄
  secondary_when: 主要鏡頭已回應整體問題，而「將展示或發行而授權未核」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.F
  - V0.3.F.strategy_entrepreneurship
  compatible_ids:
  - V0.2.F
  professional_support_trigger:
  - 申請、轉讓、保密和共享承諾由知識產權專業與權責者。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.F.innovation_ip_strategy_創新・智慧財產策略_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.F
```

### V0.3.F.marketing_consumer｜行銷／消費者行為

```yaml
METHOD_ROUTE:
  id: V0.3.F.marketing_consumer
  name: 行銷／消費者行為
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 流量增加但續用降低
  - 需辨產品價值、訊息或客群
  suppress_signals: &id001
  - 只問廣告適法或商標資格
  first_observation: 先查使用情境、替代方案、客戶可理解的利益與後續行為
  primary_when: 主爭點符合「流量增加但續用降低」，且需先查這類證據：任務和購買／退費資料、清楚分母
  secondary_when: 主要鏡頭已回應整體問題，而「需辨產品價值、訊息或客群」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.F
  - V0.2.AL
  compatible_ids:
  - V0.2.F
  professional_support_trigger:
  - 行銷合規、隱私或脆弱群體的實施需行銷倫理、資料保護及法務審查。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.F.marketing_consumer_行銷・消費者行為_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.F
```

### V0.3.F.operations_supply_chain_logistics｜營運／供應鏈／物流

```yaml
METHOD_ROUTE:
  id: V0.3.F.operations_supply_chain_logistics
  name: 營運／供應鏈／物流
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 缺貨與庫存看似矛盾
  - 交付時間或跨站流量失配
  suppress_signals: &id001
  - 只問單一合約資格
  first_observation: 把需求、庫存、補貨、吞吐及服務交付串成按時序的鏈
  primary_when: 主爭點符合「缺貨與庫存看似矛盾」，且需先查這類證據：當日出貨、庫存、訂單和排隊
  secondary_when: 主要鏡頭已回應整體問題，而「交付時間或跨站流量失配」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.F
  - V0.2.Q
  compatible_ids:
  - V0.2.F
  professional_support_trigger:
  - 實際載運、危險物、安全及合約處理由物流和對應權責專業承接。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.F.operations_supply_chain_logistics_營運・供應鏈・物流_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.F
```

### V0.3.F.organizational_behavior_hr｜組織行為／人力資源

```yaml
METHOD_ROUTE:
  id: V0.3.F.organizational_behavior_hr
  name: 組織行為／人力資源
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 相似員工在不同班表結果相差
  - 支持及回饋可能塑造事件
  suppress_signals: &id001
  - 單一文件事實且無人事影響
  first_observation: 先把職責、配時、激勵、團隊互動與管理回饋分開
  primary_when: 主爭點符合「相似員工在不同班表結果相差」，且需先查這類證據：班表、任務量、同意訪談、通報與人事程序
  secondary_when: 主要鏡頭已回應整體問題，而「支持及回饋可能塑造事件」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.F
  - V0.2.G
  compatible_ids:
  - V0.2.F
  professional_support_trigger:
  - 實際考核、監控、處分、歧視與職安，由人資、工會或專業及法務承接。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.F.organizational_behavior_hr_組織行為・人力資源_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.F
```

### V0.3.F.project_program_management｜專案／Program 管理

```yaml
METHOD_ROUTE:
  id: V0.3.F.project_program_management
  name: 專案／Program 管理
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 不同工作流同時晚於規格
  - 已交付未有受益
  suppress_signals: &id001
  - 只摘契約固定欄位
  first_observation: 先找實際交付、前置依賴、可核里程和受益責任
  primary_when: 主爭點符合「不同工作流同時晚於規格」，且需先查這類證據：有驗收條件的依賴與受益數據、決策版本
  secondary_when: 主要鏡頭已回應整體問題，而「已交付未有受益」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.F
  - V0.2.Q
  compatible_ids:
  - V0.2.F
  professional_support_trigger:
  - 實際工程投標、合同、資源承諾與安全由負責方簽核。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.F.project_program_management_專案・Program 管理_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.F
```

### V0.3.F.risk_compliance_internal_control｜風險／法遵／內控

```yaml
METHOD_ROUTE:
  id: V0.3.F.risk_compliance_internal_control
  name: 風險／法遵／內控
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 規章記載與實施缺口
  - 例外控制有待證
  suppress_signals: &id001
  - 只問管轄法效力
  first_observation: 先區分目標、風險、控制設計、實作證據及例外升級
  primary_when: 主爭點符合「規章記載與實施缺口」，且需先查這類證據：職掌、控制設計和實際履行、例外和補救
  secondary_when: 主要鏡頭已回應整體問題，而「例外控制有待證」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.F
  - V0.3.F.auditing_assurance
  compatible_ids:
  - V0.2.F
  professional_support_trigger:
  - 實際合規決定、金融通報、現場操作與內控證明由合格責任人。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.F.risk_compliance_internal_control_風險・法遵・內控_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.F
```

### V0.3.F.strategy_entrepreneurship｜策略／創業

```yaml
METHOD_ROUTE:
  id: V0.3.F.strategy_entrepreneurship
  name: 策略／創業
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 方案還未確立便要求規模化
  - 關鍵承諾的可逆性未查
  suppress_signals: &id001
  - 只需既有流程執行
  first_observation: 先找關鍵假設、可行承諾、已有資源與證偽代價
  primary_when: 主爭點符合「方案還未確立便要求規模化」，且需先查這類證據：觀察到的現有替代、重複採用、可逆承諾
  secondary_when: 主要鏡頭已回應整體問題，而「關鍵承諾的可逆性未查」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.F
  - V0.2.D
  compatible_ids:
  - V0.2.F
  professional_support_trigger:
  - 真實融資、勞務和合併承諾交具授權的董事、財務與法務。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.F.strategy_entrepreneurship_策略・創業_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.F
```

### V0.3.I.bioethics｜生物／醫學倫理

```yaml
METHOD_ROUTE:
  id: V0.3.I.bioethics
  name: 生物／醫學倫理
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 現場同意與參與壓力可能衝突
  - 利益、風險或退出條件不明
  suppress_signals: &id001
  - 只問已審結的檔案書目
  first_observation: 把目的、益害、不確定、替代及同意分列
  primary_when: 主爭點符合「現場同意與參與壓力可能衝突」，且需先查這類證據：允許的方案與替代、材料、同意及受影響資料
  secondary_when: 主要鏡頭已回應整體問題，而「利益、風險或退出條件不明」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.I
  - V0.2.N
  compatible_ids:
  - V0.2.I
  professional_support_trigger:
  - 真實研究倫理、臨床同意與脆弱情境由倫理審查、臨床、法律及當事人。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.I.bioethics_生物・醫學倫理_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.I
```

### V0.3.K.journalism_media_practice｜新聞／媒體實務

```yaml
METHOD_ROUTE:
  id: V0.3.K.journalism_media_practice
  name: 新聞／媒體實務
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 打算發布尚未查驗主張
  - 已發布內容出現可查錯誤
  suppress_signals: &id001
  - 只有敘事形式分析
  first_observation: 先鎖原件、知情權、隱私與責任
  primary_when: 主爭點符合「打算發布尚未查驗主張」，且需先查這類證據：原件、具名或核實來源及向當事人求回應的紀錄
  secondary_when: 主要鏡頭已回應整體問題，而「已發布內容出現可查錯誤」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.K
  - V0.2.T
  compatible_ids:
  - V0.2.K
  professional_support_trigger:
  - 真實指控、受保護當事人、資料公開及採訪安全由編輯與法務。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.K.journalism_media_practice_新聞・媒體實務_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.K
```

### V0.3.M.ai_ml_systems｜AI／ML 系統

```yaml
METHOD_ROUTE:
  id: V0.3.M.ai_ml_systems
  name: AI／ML 系統
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 開發指標與現場差異
  - 用途版本或使用者組成變了
  suppress_signals: &id001
  - 只查權利或設備物理狀態
  first_observation: 明示目的、資料、版本和人員接手
  primary_when: 主爭點符合「開發指標與現場差異」，且需先查這類證據：版本化測試、分層結果、端點回饋
  secondary_when: 主要鏡頭已回應整體問題，而「用途版本或使用者組成變了」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.M
  - V0.2.L
  compatible_ids:
  - V0.2.M
  professional_support_trigger:
  - 生產部署與高風險決策交有權 AI 工程、監管、資料及領域專家。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.M.ai_ml_systems_AI・ML 系統_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.M
```

### V0.3.M.cybersecurity｜網路安全／資安

```yaml
METHOD_ROUTE:
  id: V0.3.M.cybersecurity
  name: 網路安全／資安
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 資產責任與異常訊號不合
  - 服務復原需驗證
  suppress_signals: &id001
  - 要求重現利用弱點或侵入
  first_observation: 先畫資產、權責、保護與復原證據
  primary_when: 主爭點符合「資產責任與異常訊號不合」，且需先查這類證據：核准資產、角色、服務告警和恢復見證
  secondary_when: 主要鏡頭已回應整體問題，而「服務復原需驗證」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.M
  - V0.3.F.risk_compliance_internal_control
  compatible_ids:
  - V0.2.M
  professional_support_trigger:
  - 現場事件、數位鑑識、通報與復原均先由授權責任者判定。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.M.cybersecurity_網路安全・資安_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.M
```

### V0.3.M.digital_identity_trust｜數位身分／信任

```yaml
METHOD_ROUTE:
  id: V0.3.M.digital_identity_trust
  name: 數位身分／信任
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 認證成功卻服務拒絕
  - 憑據恢復後權限不同
  suppress_signals: &id001
  - 只查國籍與法院法源
  first_observation: 分查證、認證、資料聲明、授權和恢復
  primary_when: 主爭點符合「認證成功卻服務拒絕」，且需先查這類證據：受權身份及權限規格、驗證與時序
  secondary_when: 主要鏡頭已回應整體問題，而「憑據恢復後權限不同」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.M
  - V0.3.Y.data_governance_privacy
  compatible_ids:
  - V0.2.M
  professional_support_trigger:
  - 驗證、個資、身份紛爭與服務配置由有權身份、法務及資料責任者。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.M.digital_identity_trust_數位身分・信任_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.M
```

### V0.3.M.software_engineering｜軟體工程

```yaml
METHOD_ROUTE:
  id: V0.3.M.software_engineering
  name: 軟體工程
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 改版與既有資料不相容
  - 測試綠但服務差
  suppress_signals: &id001
  - 只問數學結論或合約效力
  first_observation: 鎖需求、相容、配置及負責人
  primary_when: 主爭點符合「改版與既有資料不相容」，且需先查這類證據：追溯需求、程式版本、測試、變更與回復紀錄
  secondary_when: 主要鏡頭已回應整體問題，而「測試綠但服務差」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.M
  - V0.2.Q
  compatible_ids:
  - V0.2.M
  professional_support_trigger:
  - 實際生產部署、高責任交付和資料改動由系統所有者核定。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.M.software_engineering_軟體工程_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.M
```

### V0.3.N.clinical_medicine｜臨床醫學

```yaml
METHOD_ROUTE:
  id: V0.3.N.clinical_medicine
  name: 臨床醫學
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 個人健康主張與記錄不齊
  - 需理清照護時序和證據
  suppress_signals: &id001
  - 只問一般群體比例
  first_observation: 先區分自述、所見、時序和待核
  primary_when: 主爭點符合「個人健康主張與記錄不齊」，且需先查這類證據：由專業取得的病史、觀察、檢查及追蹤
  secondary_when: 主要鏡頭已回應整體問題，而「需理清照護時序和證據」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.N
  - V0.3.AA.care_systems
  compatible_ids:
  - V0.2.N
  professional_support_trigger:
  - 具體健康和急迫性、診療、照護安全由合格臨床人員承接。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.N.clinical_medicine_臨床醫學_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.N
```

### V0.3.N.epidemiology｜流行病學

```yaml
METHOD_ROUTE:
  id: V0.3.N.epidemiology
  name: 流行病學
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 通報量改變且口徑可能變
  - 群體風險的分母未知
  suppress_signals: &id001
  - 急需個案臨床判斷
  first_observation: 先比較定義、時間、地點和人群
  primary_when: 主爭點符合「通報量改變且口徑可能變」，且需先查這類證據：持同定義的病例、風險時間和觀察量
  secondary_when: 主要鏡頭已回應整體問題，而「群體風險的分母未知」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.N
  - V0.2.L
  compatible_ids:
  - V0.2.N
  professional_support_trigger:
  - 真實公衛調查、個人健康和處置由授權專業機構。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.N.epidemiology_流行病學_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.N
```

### V0.3.N.food_safety｜食品安全

```yaml
METHOD_ROUTE:
  id: V0.3.N.food_safety
  name: 食品安全
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 批次紀錄或品質回報不符
  - 控制點有責任交接缺
  suppress_signals: &id001
  - 要求現場食品可食或個人處置
  first_observation: 分品項、批次、流程、控制及查證
  primary_when: 主爭點符合「批次紀錄或品質回報不符」，且需先查這類證據：合規流程、批次收件及驗證與退件紀錄
  secondary_when: 主要鏡頭已回應整體問題，而「控制點有責任交接缺」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.N
  - V0.3.AC.agriculture_food_systems
  compatible_ids:
  - V0.2.N
  professional_support_trigger:
  - 食品衛生、實際產品放行、召回、就醫及稽核由有資格與授權的食品安全、衛生或醫療責任者。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.N.food_safety_食品安全_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.N
```

### V0.3.N.health_systems｜健康系統

```yaml
METHOD_ROUTE:
  id: V0.3.N.health_systems
  name: 健康系統
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 資源增加但等待未降
  - 健康服務各群覆蓋分歧
  suppress_signals: &id001
  - 只需查化驗紀錄日期
  first_observation: 拆資源、服務、等待、費用和品質
  primary_when: 主爭點符合「資源增加但等待未降」，且需先查這類證據：服務能力、排隊、費用、結果和群體差
  secondary_when: 主要鏡頭已回應整體問題，而「健康服務各群覆蓋分歧」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.N
  - V0.3.AA.care_systems
  compatible_ids:
  - V0.2.N
  professional_support_trigger:
  - 醫療配置、付款與服務政策交權責管理、衛生及臨床專業。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.N.health_systems_健康系統_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.N
```

### V0.3.N.pharmacology_drug_safety｜藥理／藥物安全

```yaml
METHOD_ROUTE:
  id: V0.3.N.pharmacology_drug_safety
  name: 藥理／藥物安全
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 產品使用後出現新安全主張
  - 監測數變化但資料含重複
  suppress_signals: &id001
  - 要求個人用藥決策
  first_observation: 先定產品、暴露、事件及原始來源
  primary_when: 主爭點符合「產品使用後出現新安全主張」，且需先查這類證據：合規個案紀錄、產品資料、比較分母及時間
  secondary_when: 主要鏡頭已回應整體問題，而「監測數變化但資料含重複」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.N
  - V0.3.N.epidemiology
  compatible_ids:
  - V0.2.N
  professional_support_trigger:
  - 個別用藥、劑量、停藥、疑似不良事件與監管措施交醫師、藥師及權責單位。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.N.pharmacology_drug_safety_藥理・藥物安全_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.N
```

### V0.3.O.diplomacy_negotiation｜外交／談判

```yaml
METHOD_ROUTE:
  id: V0.3.O.diplomacy_negotiation
  name: 外交／談判
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 表面立場衝突
  - 多方才能核准並履約
  suppress_signals: &id001
  - 只查有效法源
  first_observation: 區分立場、利益、可逆安排與履約
  primary_when: 主爭點符合「表面立場衝突」，且需先查這類證據：有授權的紀要、條件、核驗及續期
  secondary_when: 主要鏡頭已回應整體問題，而「多方才能核准並履約」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.O
  - V0.2.R
  compatible_ids:
  - V0.2.O
  professional_support_trigger:
  - 真實外交、代表及和解由有授權者及合格法務。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.O.diplomacy_negotiation_外交・談判_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.O
```

### V0.3.Q.civil_construction｜土木／建築工程

```yaml
METHOD_ROUTE:
  id: V0.3.Q.civil_construction
  name: 土木／建築工程
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 工程圖、實施和驗收有差
  - 有當期變更待追
  suppress_signals: &id001
  - 只問產權或形式日期
  first_observation: 比設計、工序、變更與完工
  primary_when: 主爭點符合「工程圖、實施和驗收有差」，且需先查這類證據：版控圖、變更核可、合格測試及照片或見證
  secondary_when: 主要鏡頭已回應整體問題，而「有當期變更待追」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.Q
  - V0.2.AD
  compatible_ids:
  - V0.2.Q
  professional_support_trigger:
  - 結構、工地安全及實地變更由有資格工程與主管責任者。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.Q.civil_construction_土木・建築工程_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.Q
```

### V0.3.Q.energy_systems｜能源系統

```yaml
METHOD_ROUTE:
  id: V0.3.Q.energy_systems
  name: 能源系統
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 整體可用和尖峰服務差
  - 假設備援有效但未驗
  suppress_signals: &id001
  - 只要求法律分類
  first_observation: 查需求、配置、時間與可用性
  primary_when: 主爭點符合「整體可用和尖峰服務差」，且需先查這類證據：時序需求與可用容量、服務恢復測試
  secondary_when: 主要鏡頭已回應整體問題，而「假設備援有效但未驗」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.Q
  - V0.2.AG
  compatible_ids:
  - V0.2.Q
  professional_support_trigger:
  - 現場電力、供能、關鍵設施及安全交有資格工程和營運者。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.Q.energy_systems_能源系統_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.Q
```

### V0.3.Q.space_systems｜太空系統

```yaml
METHOD_ROUTE:
  id: V0.3.Q.space_systems
  name: 太空系統
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 民用觀測與發布產品不對齊
  - 資料版本和任務責任不明
  suppress_signals: &id001
  - 要求軍事行動或業外操作
  first_observation: 分任務目標、地面接手、版本與生命週期治理
  primary_when: 主爭點符合「民用觀測與發布產品不對齊」，且需先查這類證據：民用需求、測試、元資料與來源、服務端驗收
  secondary_when: 主要鏡頭已回應整體問題，而「資料版本和任務責任不明」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.Q
  - V0.2.AG
  compatible_ids:
  - V0.2.Q
  professional_support_trigger:
  - 太空及射頻操作、發射資格、監管和安全由合格責任者。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.Q.space_systems_太空系統_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.Q
```

### V0.3.Q.telecommunications_networks｜電信／網路系統

```yaml
METHOD_ROUTE:
  id: V0.3.Q.telecommunications_networks
  name: 電信／網路系統
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 通信標稱品質和用戶體驗不同
  - 跨網接續有重複異常
  suppress_signals: &id001
  - 只有權利文件爭議
  first_observation: 分端點、接續、承載、呼叫體驗及範圍
  primary_when: 主爭點符合「通信標稱品質和用戶體驗不同」，且需先查這類證據：經授權端點品質、各段時窗與告警
  secondary_when: 主要鏡頭已回應整體問題，而「跨網接續有重複異常」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.Q
  - V0.2.M
  compatible_ids:
  - V0.2.Q
  professional_support_trigger:
  - 電信服務配置、頻譜和現場處置由資質人員與主管。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.Q.telecommunications_networks_電信・網路系統_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.Q
```

### V0.3.Q.utilities_infrastructure｜公共事業／基礎設施

```yaml
METHOD_ROUTE:
  id: V0.3.Q.utilities_infrastructure
  name: 公共事業／基礎設施
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 工程完成而用戶未恢復
  - 費率和連續性需要拆分
  suppress_signals: &id001
  - 只查章程權責
  first_observation: 分設施、服務、支付可及與復原
  primary_when: 主爭點符合「工程完成而用戶未恢復」，且需先查這類證據：服務分布、事件、復原及實際可及
  secondary_when: 主要鏡頭已回應整體問題，而「費率和連續性需要拆分」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.Q
  - V0.2.U
  compatible_ids:
  - V0.2.Q
  professional_support_trigger:
  - 實際供應、費率、復原及設施安全由公共部門和營運工程負責。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.Q.utilities_infrastructure_公共事業・基礎設施_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.Q
```

### V0.3.U.emergency_disaster_management｜緊急／災害管理

```yaml
METHOD_ROUTE:
  id: V0.3.U.emergency_disaster_management
  name: 緊急／災害管理
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 危害跨站且需求變動
  - 已處理宣稱缺到達證據
  suppress_signals: &id001
  - 只問公告時間
  first_observation: 分準備、應變、維持和復原
  primary_when: 主爭點符合「危害跨站且需求變動」，且需先查這類證據：主管指揮紀錄、演練、民眾求助與復原排行
  secondary_when: 主要鏡頭已回應整體問題，而「已處理宣稱缺到達證據」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.U
  - V0.2.Q
  compatible_ids:
  - V0.2.U
  professional_support_trigger:
  - 真實警報、撤離、救援及復原由救援、主管及執業人員。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.U.emergency_disaster_management_緊急・災害管理_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.U
```

### V0.3.U.migration_refugee_studies｜移民／難民研究

```yaml
METHOD_ROUTE:
  id: V0.3.U.migration_refugee_studies
  name: 移民／難民研究
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 異地移動後服務中斷
  - 數據及個人需求混用
  suppress_signals: &id001
  - 只確認明文名單
  first_observation: 分離身份判斷、流動時間、知情與社會支持
  primary_when: 主爭點符合「異地移動後服務中斷」，且需先查這類證據：依法可用的身份時序、本人意願及實際轉介
  secondary_when: 主要鏡頭已回應整體問題，而「數據及個人需求混用」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.U
  - V0.2.AB
  compatible_ids:
  - V0.2.U
  professional_support_trigger:
  - 具體移民、難民、兒童安全、保護資料和身份審定由授權機構及獨立專業。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.U.migration_refugee_studies_移民・難民研究_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.U
```

### V0.3.U.public_finance_budgeting｜公共財政／預算

```yaml
METHOD_ROUTE:
  id: V0.3.U.public_finance_budgeting
  name: 公共財政／預算
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 已批准與已支付有差
  - 跨期資金負擔不明
  suppress_signals: &id001
  - 只確認稅務身分
  first_observation: 分授權、支出承諾和現金
  primary_when: 主爭點符合「已批准與已支付有差」，且需先查這類證據：已核預算、承諾或現金表及或有負債
  secondary_when: 主要鏡頭已回應整體問題，而「跨期資金負擔不明」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.U
  - V0.2.D
  compatible_ids:
  - V0.2.U
  professional_support_trigger:
  - 實際撥用和債務、財政披露由有權機關、會計與財政專業。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.U.public_finance_budgeting_公共財政・預算_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.U
```

### V0.3.U.public_procurement｜政府採購

```yaml
METHOD_ROUTE:
  id: V0.3.U.public_procurement
  name: 政府採購
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 規格只一種來源
  - 低標與使用驗收有落差
  suppress_signals: &id001
  - 只問逾期效力
  first_observation: 從生活服務回溯規格、比較及交付
  primary_when: 主爭點符合「規格只一種來源」，且需先查這類證據：原規格、通告、評選及可驗收要求
  secondary_when: 主要鏡頭已回應整體問題，而「低標與使用驗收有落差」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.U
  - V0.2.S
  compatible_ids:
  - V0.2.U
  professional_support_trigger:
  - 實際招標、評選、締約、救濟及利益衝突由採購、法務和主管。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.U.public_procurement_政府採購_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.U
```

### V0.3.U.regulatory_governance｜監管治理

```yaml
METHOD_ROUTE:
  id: V0.3.U.regulatory_governance
  name: 監管治理
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 擬改有普遍效果規則
  - 執行行為未達目標
  suppress_signals: &id001
  - 只判單一法定期限
  first_observation: 把風險、工具、成本與監測列清
  primary_when: 主爭點符合「擬改有普遍效果規則」，且需先查這類證據：基線、替代工具、實際成本和受影響資料
  secondary_when: 主要鏡頭已回應整體問題，而「執行行為未達目標」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.U
  - V0.2.C
  compatible_ids:
  - V0.2.U
  professional_support_trigger:
  - 監管、正式處分及法律效力由有權機關和專業者。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.U.regulatory_governance_監管治理_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.U
```

### V0.3.V.defence_military_studies｜國防／軍事研究

```yaml
METHOD_ROUTE:
  id: V0.3.V.defence_military_studies
  name: 國防／軍事研究
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 文人監督和預算權責未對齊
  - 需檢視民用協助的結束條件
  suppress_signals: &id001
  - 要求戰術、武器或行動方法
  first_observation: 先核公開授權、預算與責任接口
  primary_when: 主爭點符合「文人監督和預算權責未對齊」，且需先查這類證據：正式公開授權、賬務和監督報告
  secondary_when: 主要鏡頭已回應整體問題，而「需檢視民用協助的結束條件」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.V
  - V0.2.E
  compatible_ids:
  - V0.2.V
  professional_support_trigger:
  - 帶權公務、保密、民用保護與國際法決定由授權機關及獨立監督、法律和人道責任者。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.V.defence_military_studies_國防・軍事研究_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.V
```

### V0.3.Y.data_governance_privacy｜資料治理／隱私

```yaml
METHOD_ROUTE:
  id: V0.3.Y.data_governance_privacy
  name: 資料治理／隱私
  class: FUNCTIONAL_MODULE
  layer: L3
  standing: REVIEW_READY
  trigger_signals:
  - 新用途或接收方
  - 表內資訊可與他源連結
  suppress_signals: &id001
  - 不涉及資料使用而只問談判利益
  first_observation: 畫蒐集到刪除、分享與回應權
  primary_when: 主爭點符合「新用途或接收方」，且需先查這類證據：資料流、目的、授權、保留和權利回應
  secondary_when: 主要鏡頭已回應整體問題，而「表內資訊可與他源連結」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.Y
  - V0.2.X
  compatible_ids:
  - V0.2.Y
  professional_support_trigger:
  - 合法性、個資安全和委外由合格資料保護及法務。
  canonical_file: ../03_FUNCTIONAL_MODULES/學科心法總目錄_V0.3.Y.data_governance_privacy_資料治理・隱私_整合版.md
  do_not_use_when: *id001
  parent_method: V0.2.Y
```

### CONTEXT.NARRATIVE_PHYSICS｜AI 小說心法／敘事物理學

```yaml
METHOD_ROUTE:
  id: CONTEXT.NARRATIVE_PHYSICS
  name: AI 小說心法／敘事物理學
  class: SPECIALIZED_CONTEXTUAL
  layer: SPECIALIZED_CONTEXTUAL
  standing: 未完成草案
  trigger_signals:
  - 創作情境明示採用敘事物理學
  - 須從虛構角色的行動限制與關係辨張力
  suppress_signals: &id001
  - 只需文獻考據、作者身分或字面摘錄
  first_observation: 原創敘事裡的力量、壓強、自由度、張力與命運節點
  primary_when: 主爭點符合「創作情境明示採用敘事物理學」，且需先查這類證據：已授權的原始場景、交易材料或對話脈絡
  secondary_when: 主要鏡頭已回應整體問題，而「須從虛構角色的行動限制與關係辨張力」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.AJ
  - V0.2.AM
  compatible_ids:
  - V0.2.AJ
  professional_support_trigger:
  - 作品權利或實際身分及敏感事項依編輯、法務與權責人。
  canonical_file: ../04_SPECIALIZED_CONTEXTUAL/AI小說心法(敘事物理學).md
  do_not_use_when: *id001
  explicit_context_required: true
```

### CONTEXT.FINANCIAL_MARKET_STRUCTURE｜理火金融心法／市場結構篇

```yaml
METHOD_ROUTE:
  id: CONTEXT.FINANCIAL_MARKET_STRUCTURE
  name: 理火金融心法／市場結構篇
  class: SPECIALIZED_CONTEXTUAL
  layer: SPECIALIZED_CONTEXTUAL
  standing: FIRST_DRAFT
  trigger_signals:
  - 明示比較市場結構及情境
  - 希望了解多路徑的支持和反證
  suppress_signals: &id001
  - 要求個別買賣訊號或保證獲利
  first_observation: 目前市場位置、可能情境、支持與反向證據、失效條件
  primary_when: 主爭點符合「明示比較市場結構及情境」，且需先查這類證據：已授權的原始場景、交易材料或對話脈絡
  secondary_when: 主要鏡頭已回應整體問題，而「希望了解多路徑的支持和反證」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.D
  - V0.2.S
  compatible_ids:
  - V0.2.D
  professional_support_trigger:
  - 交易、投資及正式風險承擔由合格專業。
  canonical_file: ../04_SPECIALIZED_CONTEXTUAL/理火金融心法_市場結構篇_V0.1.md
  do_not_use_when: *id001
  explicit_context_required: true
```

### CONTEXT.GUANZHI_RELATIONAL_LANGUAGE｜風月場關係話術心法

```yaml
METHOD_ROUTE:
  id: CONTEXT.GUANZHI_RELATIONAL_LANGUAGE
  name: 風月場關係話術心法
  class: SPECIALIZED_CONTEXTUAL
  layer: SPECIALIZED_CONTEXTUAL
  standing: FORMAL_EXPERIMENTAL_FIRST_DRAFT
  trigger_signals:
  - 明示觀止世界及角色語言視角
  - 文字的關係與世界內語用待辨
  suppress_signals: &id001
  - 一般語言查詢或要求操控真實人物
  first_observation: 觀止世界的對話角色、關係位置、語境與人物自主
  primary_when: 主爭點符合「明示觀止世界及角色語言視角」，且需先查這類證據：已授權的原始場景、交易材料或對話脈絡
  secondary_when: 主要鏡頭已回應整體問題，而「文字的關係與世界內語用待辨」仍有證據差異、會改變下一步時。
  neighbor_ids:
  - V0.2.R
  - V0.2.AJ
  compatible_ids:
  - V0.2.R
  professional_support_trigger:
  - 涉真實人物、隱私或保護問題，照各場景之授權與專業。
  canonical_file: ../04_SPECIALIZED_CONTEXTUAL/風月場關係話術心法_V0.1.md
  do_not_use_when: *id001
  explicit_context_required: true
```
