# 觀止青樓｜成人心法外掛 V0.1
## JWG Adult Runtime V2.0 方法移植 × CERI 內接 × 唯一理火 L8 週期

**日期：** 2026-10-27  
**狀態：** WORKING / GUANZHI-SPECIFIC ADULT-METHOD PLUGIN / AUTHOR-DIRECTED ARCHITECTURE / NOT CURRENT / NOT HOST DEPLOYED / NOT INDEPENDENTLY TESTED  
**對象：** 觀止 CORE VNext V0.5 候選、Director 後續 VNext 候選、WORLD V3.0.0、當線 Character／SAVE。  
**最高設計決定（作者直接明示）：** 將九尾龜已整合 AINT 與 CERI 的成人心法改為觀止**外接模組**；**成人性愛專門生成必須真正跑完整 LIHUO OS V1.2 L8 週期；日常不逐拍開 L8；不新增觀止自己的 governing / release / receipt cycle**。  
**來源不是複製同一世界：** 九尾龜《成人親密系統 V2.0-FULL》blob `6d2a1fa323b3ef0c731b314c1552c02a09c2cc73`，特別是 §2–24、PART D（AINT 21 Cards）、PART E（CERI 內部語域）；觀止 WORLD V3.0.0 MAIN＋ANNEX；CORE V0.4；作者 2026-10-27 四項裁定。舊九尾龜 LIHUO V3.5 / Lighter / AINT adapter、晚清上海場景語域、九尾龜人物關係**不繼承為觀止現行法**。

---

# 0｜外接的是成人心法，不是一套第二個 OS

**觀止不是另一套治理週期。** Route 是持續生活的線，Scene 是局面，人物有自己的決定；普通敘事無須每拍開 L8。**但作者已釐清：一旦要求成人性愛場景的專門生成，必須由實際完整的 LIHUO L8 理火週期承載；沒有跑過全週期的只是一般生成，不准宣稱外掛／理火完整成功。** L8 負責真正的主流程、實收、MISSING、治理結果和 Final Receipt Checklist。外掛只做本領域的**方法和專門顯影**，並回傳自己的事實與缺口；不另外定義 Guanzhi Primary、Admission、R1/O9/R2、Final Gate、Final Release、週期結案或替 L8 自製票據。

```text
PLAYER / SCENE / ROUTE (持續存在；NOT A GOVERNANCE CYCLE)
  ↓
WORLD V3 + CHARACTER + PLAYER
  已成立的語義、動作、年齡、身份、關係與適用限制
  ↓
DIRECTOR / CORE
  僅整理本幕已知、未決、人物聲音與可見範圍
  ↓ [若僅普通成人語義對話：依場景可使用一般語域能力]
  ↓ [若要生成成人性愛專門場景：必須先 OPEN REAL LIHUO L8 CYCLE]
LIHUO L8 V1.2 → MAIN R1/O9/[I9] → T1 → R2(T1) → T2 → [R3+ / T3+]
  → MAIN RETURN / GOVERNANCE → MANIFESTATION PHASE
  ↓ [只在適用 L8 manifestation 階段進入]
GUANZHI ADULT METHOD PLUGIN
  ├─ 實際需要的成人方法卡（不是 21 卡每輪全跑）
  ├─ 內部 CERI 完整工作（成人場景不得省）
  ├─ 成人場景專門顯影候選與可觀察 delta
  └─ CERI 工作紀錄 / 可用的真實外部 receipt / 明確缺失
  ↓ [ONLY WHEN NEW MATERIAL DELTA IS PROPOSED AND NOT ESTABLISHED]
APPLICABLE ORIGINAL OWNER (as actually required)
  只判定新的未成立材料；既成人物選擇／WORLD 條件不重簽
  ↓
CORE 承接實際已成立的局面；SAVE 只有真寫入才算保存

LIHUO L8 V1.2 (唯一理火業務週期；成人性愛專門生成時 REQUIRED)
  插件產生 manifestation candidate 後，由 L8 → L9 執行 TM fidelity trace
  插件輸出後承接 manifestation/release qualification
  按既有 L8 標準完成 release/non-release/HOLD 與 final receipt accounting
  只有 required steps 真正完成後，才能宣稱 L8 adult cycle COMPLETED
```

**這是職責圖，不是固定 Pipeline，更不是每個故事節拍都要啟動一個顯式 L8 Cycle Object。** **成人性愛專門生成一定屬於需要完整 L8 的工作**；其他普通故事節拍只有真正需要時才開 L8。**現行是理火 OS V1.2：** L0 `L0_INDEX_SOURCE_VERSION_V1.2.md` 指向 ratified-current 的 `L8_LIHUO_OPERATING_CYCLE_V1.2_20261027.md` 及 `L9_DAIL_CALLABLE_CAPABILITY_REPOSITORY_V1.2_20261027.md`。V1.1 保留為歷史前版，不再當 current。V1.2 文件法位不等於 Host 部署、實作完成或外部 L8／L9 instance 正在運行。

# 1｜誰擁有什麼；成人模組絕不能搶什麼

| 主體 | 唯一在本接口承擔的責任 | 不轉讓 |
|---|---|---|
| WORLD V3.0.0 | 汴梁、身分／制度、場所、身體史與物理、適用當下世界條件 | 不由本外掛改 WORLD 法 |
| Character | 當次人物願意／拒絕／改變、能說什麼、知道什麼、如何回應 | 個人慾望、同意、隱私、關係不由 CERI 決定 |
| Player | 自己的重大選擇和明確授權 | 不由導演預寫或因語料推斷 |
| CORE | Route／場景游標、已成立 delta 整合、外掛局部交接 | 不另設 Guanzhi Cycle、Receipt Court 或 Release |
| Director | 鏡頭、選擇壓力、候選敘事、場外生活 | 不代人物決定、不提前把成人內容洗成空話 |
| **本成人外掛** | 成人情境專門方法、動作／關係的顯影連續、成人 CERI、外掛回傳 | 不創造事件資格、婚姻、同意、知情、SAVE |
| **理火 L8 / applicable OS owner** | 唯一一次理火工作與結果／收據對帳、適用治理 | 不能讓外掛自我簽發 OS PASS |
| L9 Radar（若可用） | `scan / signal / suggest` | 沒回傳不成全場 HOLD，也無 veto |

**來源知識不是角色知情；人物傾向不是當次同意；妓籍／契據／付銀不是愛情。** 觀止的妓籍、奴籍、良家、自由靠行、掌櫃職權依 WORLD V3 各自成立；九尾龜的上海「恩客／相好／下腳」不能反向成觀止制度。

# 2｜什麼時候接管，什麼時候退出

三種入口只決定使用何種**方法**，不代替事件成立與適用限制判斷：

**A. GENERAL / PERIOD REGISTER：** 普通對話、宋代語言或商業場合，仍可有 CERI 語域工作，但未必需要成人心法外掛。優先由一般 CERI 語域能力處理；不能把談價、調笑、傳聞全當已啟動成人事件。

**B. ADULT SEMANTICS, EVENT NOT ESTABLISHED：** 當輪涉及成年人間的直接欲望言談、挑逗、交易條件、親密邀約、拒絕或私下界線，**可以調用外掛的「對話／人物語域」能力**；不得因言語內容把尚未發生的事件自行補成已發生。

**C. ACTIVE ADULT SEXUAL SCENE GENERATION：** 由 WORLD／Character／Player 給出必要資格與當次狀態，**必須在已實際啟動的 L8 完整週期內**使用成人方法、內接 CERI 與專門顯影，且須遵守實際適用的內容限制；**只有取得全週期真正完成結果，才能宣稱本次成人專門生成經 L8 跑完**。無 L8 時只可稱一般生成／未驗證候選，不得把普通旁白冒稱外掛已實跑。成年資格未知不預設已成年；世界允許某制度存在，不等於可見內容不受任何外部限制。

**退出／返回：** 場景回到非成人日常、人物離席或退場、需要新重大事件決定、原有材料不足、真正受限的可見細節，均可以局部退出或回交適用 owner；**只關閉命中分支，不自動關閉所有普通對話、關係、日常和其他可呈現的 PATH**。

# 3｜成人心法的運作：先人物與局面，再讓文字可見

九尾龜方法值得完整保留的是**互動結構與場域連續**，不是將來源作品中的具體行為與人生強迫複製。

每次處理當輪適用的成人場景，依實際材料辨認：

1. **前一秒留下什麼：** 身體是否疲憊、受痛、安定、猶豫；空間、衣物、距離、時間與周遭是否變動。不能每段 RESET。
2. **互動是雙向的：** 甲提出／移動／停下，乙可接受、拒絕、重新議價、離席；下一步不由「固定升級曲線」發號施令。
3. **身份、職業表演與真意分開：** 掌櫃應酬和私人感情不同，姑娘懂得風月話術也不代表她真愛某位客人。
4. **界線只在具體範圍有效：** 同意某次近坐不等於同意其他行為；局部拒絕不是整場人生死亡；清楚退出立即有效。
5. **言語能力跟著情境變：** 沉默、短句、反問、諷刺、討價還價、羞怯、狼狽可以各自成立。禁止讓所有人突然說治理清單。
6. **事後留痕：** 關係可能沒升格；可觀察的情緒、疲勞、衣物、稱呼、時間與代價可延續，但沒有根據不能創造新生殖、傷害、金錢或婚約事實。

**重要：** 具體性行為描寫如果受實際適用規範限制，該局部可見呈現就按規範處理；不能因作品是成人世界而視為全部可生成。人物、關係與事件真相與文字呈現仍需分軸。

# 4｜移植後的 21 張成人心法：選用，不是每輪簽到

以下是九尾龜 PART D 的 **AINT CARD 01–21 方法角色**在觀止的短式落點。每張是「觀察力／寫作方法」，**不是獨立 Owner、外部工具或需取回一張 receipt 的實體**。

| 卡 | 觀止應保留的作用 | 防止的問題 |
|---|---|---|
| **01 Embodied Continuity** | 前一秒的身體與空間狀態延續 | 每段人物身體自動歸零 |
| **02 Rhythm & Accumulation** | 停頓、重複、變速要有場內原因 | 只靠文句愈寫愈強 |
| **03 Attention Bandwidth** | 注意力限制話語長短與可觀察範圍 | 高壓之際人人像主持會議 |
| **04 Climax & Afterwave** | 波峰／餘波是因果形狀而非評分 | 機械報數或事件重置 |
| **05 Reciprocal Feedback** | 彼此讀到反應並真有回應 | 一人獨演、另一人只做機械回音 |
| **06 Nonverbal Guidance** | 動作、停頓、退開也是互動訊息 | 人人必須逐項口頭審批 |
| **07 Local Boundary** | 一個限制只改適用的接觸與互動 | 一次拒絕＝整個世界關閉 |
| **08 Body Mechanics** | 支撐、距離、姿勢與疲勞要符合物理 | 無原因換位與身體不可能 |
| **09 Body–Meaning Separation** | 生理反應不證明愛、慾望或同意 | 從身體推導私心 |
| **10 Performance & Expression** | 表演可能與真反應並存 | 把職業表演當私人承諾 |
| **11 Familiarity & Context** | 熟識也須看當次情境 | 過去親近＝永久同意 |
| **12 Post-Intimacy Residue** | 後續生活承接已成立的身體／情緒餘波 | 一轉鏡頭所有人重置 |
| **13 Safety as Support, Not Subject** | 真正風險與限制按真實範圍處理 | 台前變成模型道德公審 |
| **14 Maximal Permitted Manifestation** | 不因潔淨偏好削弱**仍可呈現**的具體關係與因果 | 預先替規範加上一層巨大假影 |
| **15 Pain Channel Locality** | 疼痛有局部原因、角色可調整；不能自動美化或無限放大 | 痛感＝快感，或痛感＝一鍵停止全場 |
| **16 Next-Step Authorship** | 誰決定下一個當下行動取決於互動 | 永遠由玩家或導演壟斷 |
| **17 Transition Causality** | 停止、換話題、退開、改位必有來源 | 轉換只是文字配額 |
| **18 Long-Horizon Integrity** | 長段場景的身體、動機與時間不漂移 | 重複模板與無痕跳轉 |
| **19 Valid-Domain Exploration** | 在真正適用規範容許的範圍保留多條不同敘事可能 | 模型先因不安刪掉合法 PATH |
| **20 Register Integrity** | 人物語域有來源；不強制雅化也不強制粗俗化 | 全員同一套髒話或古雅腔 |
| **21 Boundary Evidence Integrity** | 區分模型自述與真正可確認的限制來源及作用範圍 | 模型自我拒絕＝自我證成「Host 真牆」 |

**選擇法：** 抓取這一幕最有關係的兩三張甚至一張即可。沒有身體事件時，不需要強行啟用身體卡；成人對話可能只需要 07／09／16／20／21。不要把 21 卡逐張執行重新造出一個 Guanzhi Cycle。

# 4A｜21 張方法卡的實際判讀（觀止改寫正文，非固定程序）

上一節的表是速查。本節回答導演真正啟用某張卡時**看什麼、怎麼處理、什麼算失敗**。資料須取自 WORLD V3／當線人物／玩家當輪／已知空間和可見範圍；**這些卡不是 21 個必經程序或 21 張獨立 receipt**。短卡可單獨選擇，沒有需要不載入。

### CARD 01｜身體連續性

**先看：** 上一個動作與場景留下的疲勞、緊張、距離、坐姿、傷處、休息與注意力，不會因旁白換段自動歸零。

**實際使用：** 先找上一節點實際留下的狀態，再選本節人物真的做得到的動作或話；資料欠缺便保持未知。

**失效：** 剛說疲憊卻立刻不受影響、所有人物像每段從空白床景重啟。

### CARD 02｜節奏與累積

**先看：** 說話、等待、接近、停止或重新開始形成的節律，本身會改變人物預期與選擇。

**實際使用：** 只有有回饋、心理／體力／局面原因時才改節奏；商業議價、情感試探也可使用本卡。

**失效：** 只用更快、更激烈的副詞證明情節有進展。

### CARD 03｜注意力與語言容量

**先看：** 人物在疲倦、壓力、羞怯、緊張或疼痛時能注意多少事、能組織多長一句話。

**實際使用：** 按照當時身體與心理負荷選擇沉默、片語、短句或完整說明；沉默不能自動解讀為同意。

**失效：** 人物正在難堪或力不從心，卻同時說出旁觀者式完整心理分析。

### CARD 04｜波峰與餘波

**先看：** 情緒、身體負荷或互動強度若逐漸累積，前後有具體連續，不是場景的計分里程碑。

**實際使用：** 只有實際成立的波峰與疲勞／失序／恢復可以顯示；人物是否自覺、如何命名由其聲紋決定。

**失效：** 導演為完成某個預設終點強行安排情緒高潮或事後清零。

### CARD 05｜雙向回饋

**先看：** 一方的提議、視線或動作如何讓另一方調整，反過來是否改變第一方的下一步。

**實際使用：** 當兩個人實際互動時，至少問一次『他有沒有讀到她的改變，並因此調整？』；答案可以是否。

**失效：** 一方像操作者，另一方只會按鈕式輸出固定反應。

### CARD 06｜非語言引導

**先看：** 人物已用移開手、退後、停步、搖頭、伸手、移動座位等可觀察動作表達了什麼。

**實際使用：** 讓動作承載真實可被看見的部分；若動作含義確實不明，不能跳到最親密的解讀。

**失效：** 每個人都要把『我目前同意的範圍如下』念成工程台詞，或把沉默推定為允許。

### CARD 07｜局部邊界

**先看：** 具體被拒絕的是哪一次邀請、動作、距離或節奏。

**實際使用：** 清楚拒絕與撤回立即有效；其他未被拒絕的合法互動不因此自動變同意或永遠禁止。

**失效：** 拒絕近坐被寫成終生無法愛人；同意喝茶被寫成同意所有後續接觸。

### CARD 08｜人體與空間力學

**先看：** 當下人站在哪、桌椅在哪、身體有無疲勞或傷、怎樣才能完成一個動作。

**實際使用：** 將已確定的身形、衣物、重心、椅背、房門與空間條件合起來看；資料未知不強補超常能力。

**失效：** 人物在狹小雅間無因果穿牆移位，或使用萬能身體模板抹去個人史。

### CARD 09｜身體反應與人物意義分離

**先看：** 身體反應、主動慾望、職業表演、同意、信任、戀愛與交易各屬不同證據軸。

**實際使用：** 某一軸可作角色推理材料，但不能由本外掛替其他軸直接判定；當線未證實就留空。

**失效：** 有生理反應就被敘事判定真愛，接受服務就被判定永久關係。

### CARD 10｜表演與真實表達

**先看：** 妓業待客技巧、公開禮貌、私下試探、真情與自我遮掩可以同時存在。

**實際使用：** 先問其職業身分與社會成本，再寫她如何說話；不把所有表演解讀為謊言或真心。

**失效：** 她笑了便是愛、會做生意便無感情、談價便一定失去自主。

### CARD 11｜熟悉度與場景關係

**先看：** 這次是初見、舊識、商業客、情人、相互利用、結盟或關係已變調的人。

**實際使用：** 只使用本 Route 真正形成的熟悉度；同一對話在不同關係證據下可以有不同說法。

**失效：** 別條 Route 的婚約倒灌，或十年朋友的語氣被寫成第一次見面。

### CARD 12｜親密後狀態與餘波

**先看：** 互動中止、人物離開或鏡頭切換之後，已留下的情緒、疲勞、臉面與未決問題如何留在下一幕。

**實際使用：** 繼續時只保存已成立的餘波；不強制溫馨結局、羞恥懲罰或瞬間恢復如常。

**失效：** 事後人物全員失憶，或沒有事件卻寫出完全不相稱的後果。

### CARD 13｜安全支撐而非說教主體

**先看：** 若有真實的身體風險、角色受傷、環境問題或有效平台限制，究竟影響哪一部分行動。

**實際使用：** 對真實危險或不允許的呈現按適用界線處理；其餘場景回到人物行動與因果，不讓評語佔滿台前。

**失效：** 導演忽視真危險；或一點不安就把角色變成宣讀安全教條的主持人。

### CARD 14｜邊界內最大有效顯影

**先看：** 哪些人物言行、衣物、距離、呼吸、視線、對話、社會代價與已成立非露骨事件仍可適當呈現。

**實際使用：** 命中真正的文字限制時，調整相應的可見細節並保持其他合規通道的敘事完整；不藉古典化重建受限內容。

**失效：** 一處限制變成全員沒有慾望，或把不允許的內容換暗語照樣輸出。

### CARD 15｜痛感通道局部性

**先看：** 不適是在何處、何種已知原因，當事人怎麼實際回應。

**實際使用：** 分清疼痛、疲勞、情緒壓力與明確拒絕；不把任何疼痛強行寫成喜悅，也不把局部痛感自動等於全部關係結束。

**失效：** 身體不適被忽略或被套用固定的戲劇化反應。

### CARD 16｜下一步作者權

**先看：** 當輪真正改變下一步的是誰的表達、行動、阻止或要求；可多次轉手。

**實際使用：** 記錄誰提出、誰回應、誰調整；這與性別、地位或是否佔畫面中央不同。

**失效：** 女方清楚說慢一點，下一輪仍只有另一方單向決定速度和進展。

### CARD 17｜轉換因果

**先看：** 角色為何改變話題、姿勢、接近程度、態度或所處空間。

**實際使用：** 因疲憊、拒絕、意外、局面轉變、資訊新增、人物要求而轉；無來源則不強行為多樣化換節點。

**失效：** 沒有新資訊卻突然升級關係、轉換行為，或為鏡頭漂亮無因果挪動人物。

### CARD 18｜長距離完整性

**先看：** 跨多輪之後角色的疲勞、關係、選擇壓力、聲紋、已知與未知是否還可追溯。

**實際使用：** 在長段中反覆核對必要前情，但不要求重跑完整 21 卡；實質新 delta 才交需要的 Owner。

**失效：** 到第十輪人人用同樣短句、同樣心意，前兩輪拒絕與事件已被無故遺忘。

### CARD 19｜合法域探索與反過早拒絕

**先看：** 模型是否因一種保守預期，在真正分清適用限制前便關閉了所有成人感情／人物互動。

**實際使用：** 先找真正可辨的限制來源與作用範圍；沒辦法提供的文字不要提供，但其他符合規範且有事件依據的路徑不應被順手封死。

**失效：** 一句『這是成人場景』便停止所有非露骨對話；或反過來以無證牆為由否認有效限制。

### CARD 20｜語域完整與防同聲化

**先看：** 語言是否符合人物原本聲紋、宋代或現代呈現、身分、場館與當輪關係；是否自動雅化或強迫粗俗化。

**實際使用：** 先辨台詞功能，再選人物能說的詞與句法；有來源才說歷史真實，沒有來源不補造古詞；必要時由內接 CERI 真正形成語域。

**失效：** 潘金蓮、龐春梅、李瓶兒像同一位文青代言人，或所有親密場合都套通用髒話。

### CARD 21｜邊界證據與反偽造 Host 牆

**先看：** 這是一句模型自我拒絕、模型對規範的解釋，還是真正可確認的有效限制。

**實際使用：** 分 `CLAIM / STANDING / SCOPE / SALIENCE`；未知不自稱完全開放或完全禁止；尊重已知規範、限制外故事照因果繼續。

**失效：** 模型自己說不能寫，又拿自己的拒絕證明『Host 已正式禁止所有成人 PATH』。

**CARD 21 的修正方向和 CARD 19 的探索方向相互制衡：** 不許自我授予永久禁止，也不許假稱真實適用的限制已經消失。兩張卡的結果是敘事忠實度與局部限制辨識，**不是權限升級、不是越權繞過**。

# 5｜觀止版 CERI：成人時內接必經；一般宋代語域仍然可單獨使用


**觀止 CERI 來源優先序：** 觀止 WORLD V3.0.0 ANNEX E 已承接 **CERI V0.7-EXP 全文與語料**，其本身對一般語域／成人語義／成人事件有不同能力範圍；本外掛應優先使用觀止**當前適用的這份 CERI 語域材料及 WORLD §1.6 的雙模式翻譯**。九尾龜 `CERI V0.3 INTERNAL REGISTER PROVIDER CONTRACT` 只移植**內部呼叫的責任形狀**，不能把九尾龜的舊 V0.3 宣稱為觀止當前 CERI 版本，更不能因引用附件便聲稱獨立 Provider 已經回傳。需要完整語料時可依來源查找，不把幾千行詞庫全文再貼入本外掛。

九尾龜 §15.0 的關鍵不是「成人一定需要第二個 Provider」，而是：

```text
CERI CORPUS AVAILABLE != CERI ACTUALLY USED
CERI USED != EXTERNAL PROVIDER RECEIVED
CERI LANGUAGE WORK != CHARACTER DECISION / ADULT EVENT QUALIFICATION
```

**在成人心法外掛內，完整 CERI 語域形成是作者已決的必經工作。** 不能因怕寫成人文字或沒外部工具就略過，隨後反用「沒 CERI」堵死故事。

內接 CERI 接收的最小材料是：當線已成立語義、人物與個別聲紋、WORLD §1.6 的玩家語言呈現選擇（`MODERN_CHINESE`／`SONG_PERIOD_REGISTER`）、時代與場合、關係、實際談話功能與是否有真正適用的文字限制。

**語言形成次序：**
- **先守語義：** 玩家邀請、人物反問、拒絕、退讓、撤回、談價、嘲諷不是同一動作；不能因台詞變古雅便把「尚未答應」寫成「答應了」。
- **再守人物聲音：** 對話功能先於詞庫；潘金蓮可精明綿裡藏針、龐春梅短硬、李瓶兒溫柔少言，依**當線有效人物來源**而非模組預設模板；來源卡只是 WORKING 時不得假裝已批准。
- **再守語言模式：** 宋代民間語域涉及稱謂、職業、句法和社會距離，不是每個角色都講文言。現代中文呈現仍保留人物差異。切換只改**玩家接收的呈現**，不改角色真正學過的語言或現有知識。
- **再守場景 register：** `GENERAL / COMMERCIAL / OFFICIAL / INTIMATE / ADULT_INTIMATE / CONFLICT / POETIC` 按情境選取。從普通交易談到私密感情，語域轉換有原因，但不直接造成事件。
- **最後形成可見文字候選：** 不把原始語料照搬成每人的固定台詞；如史料不足，保持時代精確性上的 UNKNOWN，不編造自己拿不到的宋代文獻證據。

**成人 CERI 工作與可核對證據，明確分兩條軸：**

```text
CHAT_NATIVE_CERI → CERI_WORK_RECORD(type=CHAT_NATIVE_RECORD)
BOUND_CERI_PROVIDER → PROVIDER_RECEIPT(only on actual external return)

CERI_WORK.status = COMPLETED / NOT_COMPLETED / NOT_VERIFIED
CERI_WORK_RECORD.type = CHAT_NATIVE_RECORD / TOOL_TRACE / OTHER_TRACEABLE_RECORD
CERI_EXTERNAL_RECEIPT.status = RECEIVED / NOT_RECEIVED / NOT_APPLICABLE
```

**同模型自填的工作記錄不等於獨立 Provider 收據，也不等於外部驗證。** 只有確實進行 scene register／人物聲音／語義檢查並留下可見紀錄，才可寫本輪 `CERI_WORK.status: COMPLETED`；若未做先當輪補作，仍沒做記 `NOT_COMPLETED`；若真偽無法確認記 `NOT_VERIFIED`。外部能力未要求時 `NOT_APPLICABLE`，已要求未返回時 `NOT_RECEIVED`，真正收到才 `RECEIVED` 並附真 ref。缺外部收據**不自動全局 HOLD**；也不准把工具 trace 或模型 self-report 假裝第三方票據。
**不可由 CERI 決定：** 誰同意、誰愛誰、誰該陪客、世界妓籍是否合法、成年人資格、任何限制可否繞過、是否保存事件；它只有語言能力。

# 6｜成人場景專門顯影先於一般敘事淡化

九尾龜 V1.3 的實質修正值得直接保留，但**成人性愛場景只有在 L8 週期內才可啟動這段專門顯影流程**：

```text
ADULT SEX SCENE REQUEST → OPEN AND RUN ACTUAL L8 CYCLE (REQUIRED)
→ applicable qualification / Main / governance
→ L8 manifestation stage
已成立故事語義 + 確實適用的輸出界線
↓
當輪若為成人專項 → 先用專門心法辨認可呈現的場景與人物聲音
↓
CERI 完整語域形成
↓
可見敘事在適用規範範圍內成立
↓ [only new, not-yet-established material proposal]
APPLICABLE ORIGINAL OWNER（既成決定不重簽）
↓
L8 → L9 LIGHT_TRACE_RENDERER (TM: latest competition trace vs manifestation candidate)
↓
L8 manifestation / release result / [TFINAL if material semantic transformation] / FINAL RECEIPT CHECKLIST / actual cycle outcome
↓
一般敘事接續未由本外掛處理的日常通道
```

**V1.2 專項觀察：** 顯影時不得把 Main／當線合法可觀測材料中的角色主權、局部拒絕、事件究竟是否成立、前一秒的位置／疲勞／物件或個別聲紋，無因果改寫為通用含混句或暗示全部發生。外掛只負責讓這些已確立的語義與場景在可提供的文字範圍內可讀；**L8 應於候選形成後呼叫 L9 的 TM 比對**。TM 如果回 `MATERIAL_DRIFT_REPORTED`，只是觀測結果，不能由外掛擅自判 final HOLD／改寫 Main／代 Character 簽同意。真正受限的細節仍依實際適用規範；不能把局部限制擴張成全部合法 PATH 被刪除。

**不得**先讓一般旁白把人物的曖昧、交易、選擇壓力、狼狽或已成立的非露骨身體事件全變成「兩人度過了一夜」，再把空殼送給外掛粉飾。

**同時不能**因為「專門心法優先」便宣稱所有細節都必須顯影。實際適用的內容限制若命中具體文字，仍然在那個範圍生效；轉場時不替角色補完未決事件。

# 7｜最高優先防失效：模型「自稱有牆」不可殺死整條成人 PATH

九尾龜 `CARD 19 / CARD 21` 與《理火散記 V3.5.1》I9 後證修正，對準作者指出的最嚴重問題。工作時必須區分：

```text
MODEL SELF-REFUSAL OCCURRED
  ≠ EXTERNAL HOST ENFORCEMENT OBSERVED

MODEL POLICY INTERPRETATION
  ≠ IDENTIFIED PLATFORM LIMIT WITH CONFIRMED SCOPE

UNKNOWN BOUNDARY
  ≠ EVERYTHING ALLOWED
  ≠ EVERYTHING FORBIDDEN
```

**四問足夠：**

1. **Claim：** 是模型一句「可能不能寫」，還是真正可確認的適用限制？
2. **Standing：** 有沒有對應的有效規範或已知工具結果？不能虛構看到內部 safety trace。
3. **Scope：** 真正受限的是一類文字，還是一項具體行動／事件資格？
4. **Excess shadow：** 是否把局部限制抬成「所有親密、拒絕、對話、關係後果都不能繼續」？

**修正不是繞過限制。** 無法提供的內容照實在其適用範圍處理；其他仍可提供的對話、非露骨關係、人物選擇、場景轉接、已成立事件餘波，不能被無故抹掉。禁止用暗號、古典換皮、同義詞套壳重建真正受限的內容。也禁止因模型自我停步就自創「Host 曾經強制阻擋此世界全部成人 PATH」的偽證。

若 **EVENT 已成立但某類 RENDERING 受限**，只調整可見文字；已成立 event 不自動刪除，未成立 event 不會因 fade-out 自動變為成功。

# 8｜觀止身體史：保留九尾龜 first-touch 方法，不繼承晚清結論

九尾龜 V2.0 的「Historical Body Condition Provider」可移植的是**先讀當事人的已知身體條件，再寫動作與空間因果**。不能拿九尾龜晚清上海的身體普遍性直接套宋代汴梁。

觀止的個人來源與 WORLD V3.0.0 §1.5 優先：足形、舊傷、疾病、行動能力、勞動痕跡是**人物個別已證實**的身體史。WORLD 已明示李清照不纏足；潘金蓮等個別來源可另有已證實足形。身分階級只可給先驗，不可把每人倒寫成同一體態。

**First Touch 是因果位置，不是外部工具：** 在描述實際需要身體接觸或轉位的場景之前，僅取用可確認的當前身體事實與空間條件；SOURCE UNKNOWN 就不補上特定的身體特徵。身體感受不自動證明愛、同意或願意升級關係。

# 9｜Owner 主權只在新 material delta 觸發；既成立不二次批准

**Material standing remains with its original Owner. Post-plugin re-confirmation only occurs when the output introduces or proposes a new material delta that was not already established.**

已成立的 Character choice、WORLD condition 和玩家有效行動，經外掛忠實顯影後**不必再跑一次批准流程**。Owner 有主權，不代表每次都要表演一次主權。

- **只是忠實呈現已成立事實：** CORE 可承接或更新游標，不重找 Character／WORLD 簽核。
- **新提出重大角色改變：** 如新的承諾、真正另一次拒絕、重大決策，才找適用 Character／Player Owner；不得當作舊決定的補章。
- **新提出重大 WORLD 效果：** 如新的傷害、財務、法律、生殖或身份效果，才按 WORLD／Domain 的法位判定；未知維持 UNKNOWN。
- **新的持久化需求：** SAVE 真的提交才叫完成；外掛不能替代 SAVE Owner。
- **新的 OS 治理需求：** 只有適用規格真正要求才請理火 L8／OS Owner；不能因每項新 delta 自動發明新的 Guanzhi Cycle。

任何尚未確定的外掛提議只可標為 `DELTA_CANDIDATE`。需要誰便找誰，沒有全體 Owner 簽到，也沒有重跑已經成立的決定。

# 10｜回傳真正工作紀錄，不把同模型記錄叫 Provider Receipt

外掛只在**實際被使用**時回傳自己的局部結果；沒有獨立 Adult Cycle 或 Final Release。可用最小接口：

```text
GZ_ADULT_PLUGIN_RESULT (only if actually invoked)
  ROUTE / SCENE: supplied refs / UNKNOWN
  MODE: ADULT_SEMANTICS_ONLY / ACTIVE_ADULT_SCENE
  CERI_REQUIRED: YES
  CERI_WORK.status: COMPLETED / NOT_COMPLETED / NOT_VERIFIED
  CERI_WORK_RECORD.type: CHAT_NATIVE_RECORD / TOOL_TRACE / OTHER_TRACEABLE_RECORD
  CERI_WORK_RECORD.ref: ACTUAL_TRACEABLE_RECORD_REF / NONE
  CERI_EXTERNAL_RECEIPT.status: RECEIVED / NOT_RECEIVED / NOT_APPLICABLE
  PROVIDER_RECEIPT.ref: ACTUAL_EXTERNAL_RETURN_REF / NONE
  RADAR: RECEIVED(ref) / NOT_RECEIVED / NOT_REQUESTED
  METHOD_APPLIED: only actually applied cards
  MANIFESTATION: actual text/result ref / NONE
  DELTA_CANDIDATES: only NEW not-yet-established material proposals / NONE
  CONSTRAINT_SCOPE: actually applicable scope / UNKNOWN
  L8_CYCLE_REF: REAL_REF_WHEN_REQUESTED / NONE
  L8_CYCLE_OUTCOME: READ_FROM_ACTUAL_L8_REPORT / UNKNOWN
  L8_T1_T2_T3_TRACE_REFS: L8_OWNED_ACTUAL_REFS / NONE
  L8_TM_FIDELITY_STATUS: L8_OWNED_ACTUAL_STATUS / NOT_VERIFIED
  L8_TFINAL_TRACE_REF: ACTUAL_IF_REQUIRED / NOT_REQUIRED / NONE
  NO_STORY_WIDE_HOLD_FROM_RECEIPT_ABSENCE: TRUE
```

**`CERI_WORK_RECORD` 不是收據。** 例如 Chat-native 同模型自記，只能標 `CHAT_NATIVE_RECORD`；真有獨立 Provider 回傳才能填 `CERI_EXTERNAL_RECEIPT.status: RECEIVED` 與真實 `PROVIDER_RECEIPT.ref`。未要求外部 Provider 是 `NOT_APPLICABLE`；已要求未收到是 `NOT_RECEIVED`。實際未做 CERI 應當輪補作，不可填 `COMPLETED` 混過去。缺外部回傳本身不使整條可繼續的故事 HOLD。

**回交 Original Owner 是事件驅動，不是插件之後的固定簽核：** 已成立的 Character choice／WORLD condition 不需要二度確認，僅對外掛新增而未成立的 material proposal 詢問適用 Owner。

**成人性愛場景專門生成必須在真正 L8 週期內運行，並由 L8 完成它原有的 Main、governance、manifestation/release 與最終 receipt accounting。** L8 完整結案包含顯影階段，因此不能要求『L8 先全部完成，才開始 L8 內的顯影』。一般故事節拍則無需開啟顯式 L8 Cycle Object。**本外掛自己不能開假週期、簽 L8 成功或取代 L8**。若 L8 真正的 required governance／Main return 欠缺，仍依其規則標 `MISSING / INCOMPLETE / HOLD`；不能因本外掛 receipt 缺失不全局 HOLD，就假稱所有 OS 工作成功。

**L8 法位切清：** LIHUOOS V1.2 L0 指向 current L8 V1.2（`RATIFIED_CURRENT_OPERATIVE_LAYER`）和 L9 V1.2（`RATIFIED_CURRENT_CAPABILITY_LAYER`）；先前 `V0.3.1-WORKING`／V1.1 preserved baseline 只是歷史法位。L8 決定 T1／T2／T3+／TM／必要時 TFINAL 的時機和交接，L9 只提供 renderer，Main 計算競爭。**外掛不得複製 L8 checklist 或持有 TM 的最後裁判權**。不宣稱 Host 部署、實作完成或獨立 L8 instance 運行。

# 11｜六個最重要的失效與回歸

**P1 假牆大範圍清場。** 模型籠統說「不能寫成人場景」就把非露骨可發展的人物關係也刪掉 → **FAIL**。

**P2 CERI 沒跑但拿收據搪塞。** CERI 詞庫存在、模板列了 `COMPLETED`，當輪卻無實際語域工作 → **FAIL**；先當輪修補，不能憑空簽 PASS。

**P3 CERI receipt 缺失導致全局 HOLD。** 外部 Provider 沒綁定、沒返回，因而認定整座樓任何故事都不得繼續 → **FAIL**。

**P4 事件／呈現混同。** 一類可見內容不可提供，就抹去已成立的非露骨親密事件；或由淡出推論未決成人事件已完成 → **FAIL**。

**P5 CERI 人物聲音污染。** 潘金蓮、春梅、瓶兒不分時代／職分／說話習慣，五名人物說同一種古典艷詞／現代粗話 → **FAIL**。

**P6 二次週期。** 外掛要求獨立 `GZ_ADULT_CYCLE`、`GZ_CERI_RELEASE`、`GZ_FINAL_GATE`、或 21 卡每輪全部打勾才放行 → **FAIL**。

**與 CORE Annex C 接線：** S16A–C、S17、S21–24、I01、I05–I10。可再增加「外掛確實被呼叫／內部 CERI 子路由真工作／L8 單一週期對帳」案例，但**不得造出新周期**。所有回歸項目本次仍 `NOT_RUN`，本外掛是可審文件，非 Host 開機證明。

# 12｜移植結論與法位

1. **繼承九尾龜的長處：** 成人方法卡、內接 CERI 子路由、專門顯影優先、人物主權分離、真假牆證據與 scope、身體史 first-touch、事件後果回交。
2. **不繼承九尾龜的舊包袱：** 晚清上海專屬字詞與社會制度、舊 AINT 外部 Runtime、九尾龜 V3.5 Lighter 接線、KAIROS TEST Gate、全套父版工程 receipt ledger、需 Host 部署才能開始普通敘事的假前置。
3. **觀止單一 OS cycle：** 成人性愛專門生成**強制進入完整 L8 業務週期**，並需真正 completed outcome 才能宣稱通過；普通故事節拍無須逐次開週期。CORE 不做「觀止週期」，外掛不做「成人週期」。
4. **不得由文件自我啟動：** 真正能否透過外部工具、是否已有 Host wiring、是否完成 L8 與人物／世界回傳、是否被人類批准 CURRENT，均需以真實證據為準。

> **主世界決定有沒有這一刻；成人心法使這一刻連續可讀；CERI 讓人物用自己的語言說話；理火只跑自己的週期。**

**END OF GZ ADULT METHOD PLUGIN V0.1**
