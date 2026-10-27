# 觀止青樓｜成人心法外掛 V0.1
## JWG Adult Runtime V2.0 方法移植 × CERI 內接 × 唯一理火 L8 週期

**日期：** 2026-10-27  
**狀態：** WORKING / GUANZHI-SPECIFIC ADULT-METHOD PLUGIN / AUTHOR-DIRECTED ARCHITECTURE / NOT CURRENT / NOT HOST DEPLOYED / NOT INDEPENDENTLY TESTED  
**對象：** 觀止 CORE VNext V0.5 候選、Director 後續 VNext 候選、WORLD V3.0.0、當線 Character／SAVE。  
**最高設計決定（作者直接明示）：** 將九尾龜已整合 AINT 與 CERI 的成人心法改為觀止**外接模組**；**只使用 LIHUO OS V1.1 適用的 L8 理火週期，不新增觀止自己的 governing / release / receipt cycle**。  
**來源不是複製同一世界：** 九尾龜《成人親密系統 V2.0-FULL》blob `6d2a1fa323b3ef0c731b314c1552c02a09c2cc73`，特別是 §2–24、PART D（AINT 21 Cards）、PART E（CERI 內部語域）；觀止 WORLD V3.0.0 MAIN＋ANNEX；CORE V0.4；作者 2026-10-27 四項裁定。舊九尾龜 LIHUO V3.5 / Lighter / AINT adapter、晚清上海場景語域、九尾龜人物關係**不繼承為觀止現行法**。

---

# 0｜外接的是成人心法，不是一套第二個 OS

**觀止不是另一套治理週期。** Route 是持續生活的線，Scene 是局面，人物有自己的決定；理火一次工作要啟動時由**現行適用的 L8 理火 Operating Cycle**負責調用、實收、MISSING、真實的治理結果與最終 CHECKLIST。外掛只做本領域的**方法和專門顯影**，並回傳自己的事實與缺口；不另外定義 Guanzhi Primary、Admission、R1/O9/R2、Final Gate、Final Release、週期結案或替 L8 自製票據。

```text
PLAYER / SCENE / ROUTE (持續存在；NOT A GOVERNANCE CYCLE)
  ↓
WORLD V3 + CHARACTER + PLAYER
  已成立的語義、動作、年齡、身份、關係與適用限制
  ↓
DIRECTOR / CORE
  僅整理本幕已知、未決、人物聲音與可見範圍
  ↓ [本幕成人方法或語域真正適用]
GUANZHI ADULT METHOD PLUGIN
  ├─ 實際需要的成人方法卡（不是 21 卡每輪全跑）
  ├─ 內部 CERI 完整工作（成人場景不得省）
  ├─ 成人場景專門顯影候選與可觀察 delta
  └─ CERI 工作紀錄 / 可用的真實外部 receipt / 明確缺失
  ↓
WORLD / CHARACTER 對 material delta 再確認
  ↓
CORE 更新當線已成立局面；SAVE 只有真寫入才算保存

LIHUO L8 (唯一業務週期，按其實際適用條件承接上列工作)
  需要時調用 applicable owner / MAIN / 本外掛或真正工具
  接收而非製造結果 → FINAL RECEIPT CHECKLIST / MISSING
```

**以上是職責圖，不是要求另按圖每回合跑一趟第二 pipeline。** L8 的 CURRENT 與適用治理依 LIHUOOS V1.1 確定；來源獨立 L8 `V0.3.1-WORKING` 自己標記 `NOT_RATIFIED / NOT_HOST_DEPLOYED`，故本稿不聲稱 Host 已實現全圖。

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

**C. ACTIVE ADULT INTIMACY SCENE：** 由 WORLD／Character／Player 真正給出必要資格與當次狀態，且按實際適用內容規範可提供的範圍，使用成人方法與專門顯影。成年資格未知不預設已成年；世界允許某制度存在，不等於可見內容不受任何外部限制。

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

# 5｜觀止版 CERI：成人時內接必經；一般宋代語域仍然可單獨使用

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

**成人 CERI 的兩種可誠實回報的實作：**

```text
CHAT_NATIVE_CERI
  → 同模型在當輪確實進行 register / voice / semantic work
  → 可提供工作紀錄（self-report），不是獨立 provider 認證

BOUND_CERI_PROVIDER
  → 真實連線、授權且真的調用外部能力
  → 只在確實收到的回傳上記 external receipt

NO WORK ACTUALLY DONE
  → 當輪補作 CERI；不准靠模板假裝已經執行

NO RECEIPT RETURNED
  → 誠實標 NOT_RECEIVED；不因收據缺席自動 GLOBAL HOLD
```

**不可由 CERI 決定：** 誰同意、誰愛誰、誰該陪客、世界妓籍是否合法、成年人資格、任何限制可否繞過、是否保存事件；它只有語言能力。

# 6｜成人場景專門顯影先於一般敘事淡化

九尾龜 V1.3 的實質修正值得直接保留：

```text
已成立故事語義 + 確實適用的輸出界線
↓
當輪若為成人專項 → 先用專門心法辨認可呈現的場景與人物聲音
↓
CERI 完整語域形成
↓
可見敘事在適用規範範圍內成立
↓
WORLD / CHARACTER 驗證真正 material delta
↓
一般敘事接續未由本外掛處理的日常通道
```

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

# 9｜只有真正跨越 material 範圍才回交主權

外掛可以觀察並建議：站位／距離變了、人物說「不要」、有人離開、服飾／器物改變、疲勞／傷痛被表達、場面產生可追溯的社會風險。

**外掛不能把候選直接當正式 Route delta。** 只把真正可觀察的候選交給 WORLD／Character 及當線依據核對：

- **需要人物新決定：** 新的關係承諾、重大的行為轉換、退出／拒絕、涉及第三人的事件。
- **需要 WORLD 判定：** 生殖／法律／契約／資產／傷害等重大結果；未知生理能力不補成已成立。
- **需要 SAVE：** 真正跨回合保留狀態時，由 SAVE owner 寫入；只產生 candidate 不等於 Git 已 commit。
- **需要 LIHUO reentry：** 依適用 L8／OS owner 自己的要求處理；CORE 或外掛不自造「此時必須 Main」的新治理規格。

處在同一件事的延續裡，不要每個動作重開新的大審判；但有新的重大狀態變動時，也不能藉「連續」替人物一次答應永久授權。

# 10｜回傳給唯一 L8 的收據：要真實，不要第二套 Cycle

**本外掛能有自己的「能力回傳／工作紀錄」，但沒有 Guanzhi Cycle／Release。** 本模組輸出的最小結果可包含：

```text
GZ_ADULT_PLUGIN_RESULT (only if actually invoked)
  ROUTE / SCENE: references actually supplied, or UNKNOWN
  MODE: ADULT_SEMANTICS_ONLY / ACTIVE_ADULT_SCENE
  CERI_REQUIRED: YES
  CERI_WORK: COMPLETED_CHAT_NATIVE / COMPLETED_BOUND_PROVIDER / NOT_VERIFIED
  CERI_WORK_RECORD: actual visible self-report ref or NONE
  CERI_EXTERNAL_RECEIPT: RECEIVED(ref) / NOT_RECEIVED / NOT_REQUESTED
  RADAR: RECEIVED(ref) / NOT_RECEIVED / NOT_REQUESTED
  METHOD_APPLIED: only cards really considered
  MANIFESTATION: actual text or local result ref, if produced
  DELTA_CANDIDATES: observable only / NONE
  CONSTRAINT_SCOPE: only genuinely applicable known scope / UNKNOWN
  NO_STORY_WIDE_HOLD_FROM_RECEIPT_ABSENCE: TRUE
```

成人 CERI **工作必經**和**外部工具票據真的收到**是兩回事。若應做卻未做，先在當輪補作；仍缺就標 `NOT_VERIFIED`，不得自稱成功。若外部 receipt 缺失，標 `NOT_RECEIVED`；**不因單一外掛票據缺席把可合法繼續的生活封死**。

理火 L8 的 `FINAL_RECEIPT_CHECKLIST` 是**唯一整趟業務週期對帳**；它可以在「本次外掛實際適用」時把外掛 return 與缺失列成適用項，不需要本模組再創獨立最後清單或 second release。若 L8 的其他**真正必需項**缺失，L8 依自己的規則誠實報 `INCOMPLETE / HOLD / FAILED`；**「故事不因 CERI receipt 缺席全局 HOLD」不等於「OS 必須假裝所有必要 Owner 都已完成」**。

本地 Chat 顯影可如實完成，不宣稱 L8 真實工具／Main／Host 一定已部署。需要工程狀態時由 L8 最終報告或本外掛最小工作紀錄揭露，**不在角色台詞中念出 CHECKLIST**。

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
3. **觀止單一 OS cycle：** L8 需要時負責一次理火，CORE 不做「觀止週期」，外掛不做「成人週期」。
4. **不得由文件自我啟動：** 真正能否透過外部工具、是否已有 Host wiring、是否完成 L8 與人物／世界回傳、是否被人類批准 CURRENT，均需以真實證據為準。

> **主世界決定有沒有這一刻；成人心法使這一刻連續可讀；CERI 讓人物用自己的語言說話；理火只跑自己的週期。**

**END OF GZ ADULT METHOD PLUGIN V0.1**
