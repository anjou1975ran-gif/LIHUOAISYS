# 觀止青樓｜人物對話與人類反應模擬研究 MEMO V0.2
## 週期完整性 × 人物作者權 × 對話因果｜持續累積研究版

**日期：** 2026-10-12  
**文件 ID：** `GUANZHI_HUMAN_RESPONSE_DIALOGUE_RESEARCH_MEMO`  
**版本：** `V0.2 / CUMULATIVE WORKING MEMO`  
**前版：** `GUANZHI_DIALOGUE_MEMO_V0.1_20261012.md`  
**法位：** `RESEARCH_MEMO / NON_NORMATIVE / NOT_CORE_AMENDMENT / NOT_DIRECTOR_SUCCESSOR / NOT_RUNTIME_DEPLOYMENT / NOT_TEST_PASS`  
**授權範圍：** 人類方允許更新研究 MEMO、持續累積想法；**不等於**批准修改正式 Core／Director／World／LCAPG／Main／Lighter 或准許偽造正式週期。  
**編碼：** UTF-8 with BOM；檔名使用 ASCII，避免下載端中文檔名亂碼。  
**資料保存：** V0.1 原文完整附於附錄 A；本版的改寫不回溯抹除舊假說、舊問題或舊標籤。  

---

## 0｜這次修改為什麼必要？

V0.1 把目標定為「使人物的對話與反應像真實人類」，已提出 CG、治理狀態外洩、角色被動、知情錯位等研究入口。這些仍然有效作為**待檢問題**。

但 V0.1 有一個偏移風險：把焦點過度放在「如何寫出自然對白」，好像只要修好 Narrator／CERI 的文字，人便會活起來。

**V0.2 的新工作假說：人物不像真人，可能不是先發生在文字，而是更上游的候選形成、人物決定、事件資格與週期執行環節。**

若 Director 預先替 NPC 選定反應，CERI 只能把那個反應修得更像古人；若 Narrator 自己發明人物承諾，文句再自然也仍是世界因果失效。

因此本版從「語句自然度」往前追問：

> **人物說了什麼，是不是先有一個有權說話、確實面對當下條件的人物，形成了那個 speech act？還是 Narrator 為了完成情節，先決定一句漂亮的台詞，再替它補理由？**

**這是研究判準，不宣稱已由實跑驗證。**

---

## 1｜來源與法位：新教材提醒我們回到現行程序，而不是另造程序

### 1.1 現行參照文件（實際要使用時應重新核對版本）

| 來源 | 本輪真正有關的位置 | 不該誤讀成 |
|---|---|---|
| `新理火AI的實習手冊_V0.6_人機共思關係_概念圖鑑_週期完整性_20261012.md` | §6B.1 人機共思、§6I 週期完整性、§6J.1 觀止垂直週期 | 手冊自己成為 Runtime 憲法或資格核發者 |
| `01_MAIN_V4.4_PROTOCOL_V3.0.1_LIGHTER_V4.8_RECEIPT_I9_FULL_RATIFIED_20261006.md` | 當輪 R1／O9／I9 Assessment／真正 R2、§10 Closure、§12 Manifestation Qualification、Receipts | 文本有 MAIN 條文就等於當輪 MAIN 真實執行 |
| `02_LIGHTER_V4.10_PROTOCOL_V3.0.2_ONBOARDING_ROLE_SEPARATION_FULL_RATIFIED_20261011.md` | 資格、責任、入場與放行；MAIN receipt admission、I9 qualification | Lighter 是角色意志或 Narrator 內容作者 |
| `01_GUANZHI_RUNTIME_CORE_V4.0.1_CURRENT_FULL_4MAIN_20261011.md` | Guanzhi Cycle identity、垂直 Receipt Manifest、Character／World／Domain owner、Radar、CERI 回傳先於 Narrator、合法 Story release | Core 出現在倉庫就證明 Host 已部署 |
| `03_GUANZHI_DIRECTOR_V4.0_CURRENT_FULL_UNCHANGED.md` | 「人物不是棋子」、§2 Director 第一眼、§14 Boundary De-Foregrounding、§15 GTR 候選、§23 持續條件與顯著性、L0 責任索引 | 導演可以因此替 Character／World 決策 |
| `04_GUANZHI_CHARACTER_POOL_LCAPG_V3.3.20_CURRENT_71_UNCHANGED.md`、Current World／Route／HOT／MASTER | 人物性格、知情、關係、歷史行為與世界限制的事實錨點 | 研究假設可以覆寫 Canon |
| `理火總體系(搭配V5版) (4).md` | 早期 PATH／反應體、自洽閉環、對「穩定 ≠ 正確」的警示 | 整份合輯同一時期完成；今天的規格在早期原樣存在 |
| `理火散記_單篇_不是不敢寫這麼簡單_觀止成人場景Runtime病灶實跑診斷_首席批准版_20261010.md` | 舊條件搶台詞、NPC 被動、Narrator 越權等既有診斷線索 | 一篇個案已證明普遍發生率或所有根因 |

**版本註：** MAIN V4.4 檔案的標題仍帶有批准當時 Protocol V3.0.1／Lighter V4.8 的歷史綁定；現行獨立 Protocol V3.0.2、Lighter V4.10 另有後續文件。不能以主檔舊標題倒置現行版本，也不能自行聲稱已完成正式 Host rebind。

### 1.2 從早期問題到今天週期：功能關聯，不是假造直線歷史

早期反應體模型注意到：系統會努力維持自洽，錯誤也可以很穩。今天 MAIN 中要求第一輪非權威、O9 觀察亮暗、I9 有條件評估／介入、R2 重新競爭，能看見相應的治理目標。

但不能把「思想上相關」寫成「早期文件已有今天的 R2／I9／Receipt」。後來的規格是在長期失效與修訂中建立的，對應應逐項標明 `CONCEPTUAL_LINEAGE` 或 `DIRECT_SPEC_CONTINUITY`；無版本證據不宣稱逐條繼承。

本輪記住實習手冊 V0.6 的句子：

> **MANDATORY PROCESS != MANDATORY CONCLUSION**
>
> **THE REASON EXPLAINS THE RULE. THE REASON DOES NOT RE-CONDITION THE RULE EACH CYCLE.**

理解每步為何存在，不會授予執行 AI「這輪可跳步」的權力。程序可以由合法 owner 根據證據修訂，**不能由導演感覺劇情已經夠好便自行豁免**。

---

## 2｜V0.2 核心主張：人味不只是語言，而是有來源的行為與後果

人類對話常常不是為了回答上一句話。說話可能是在討價還價、探口風、護面子、掩飾、不服氣、逗笑、做生意、結盟、推責、試圖結束話題，也可能僅僅在做手邊事情。

**本研究將台詞暫時視為一種帶來源的「言語行動」（speech act）**，而非只是一行自然語言。它至少要受四種區分檢查：

1. **誰有資格形成這個意圖／回應？** 人物自己，而非 Director 或 Narrator 為了順劇情補意志。
2. **人物當下真正掌握什麼？** WORLD FACT、PERSONAL KNOWLEDGE、BELIEF、RUMOR、MISUNDERSTANDING、未決不應混成 Narrator 全知。
3. **這句話在關係中做了什麼？** 問候、試探、拒絕、戲弄、保留、不回答、允諾、無意義閒談都可能發生；但意義不能由後設評論倒灌。
4. **它留下什麼後果？** 有些只是聲音和互動，有些形成 material choice／standing／world delta；二者不可因文字好看而混淆。

**真人不是永遠含糊、矛盾、不理性。** 一個精明人物可能乾淨俐落地成交；一個害羞人物也可能當場說清楚。研究要防「被 AI 強迫合理」，也要防「為了像人而強迫不合理」。

### 2.1 加一個對稱性檢查：人物不是「玩家的答案供應機」

V0.6 的「人機共思」**不能直接當作 NPC 必須與玩家平等共思的劇本指令**。研究可借用其中一個關係辨認方法：

> 如果 NPC 被預設成「PLAYER SPEAKS → NPC SATISFIES PLAYER QUESTION」，那麼人物原本的利害、注意力與他人關係，可能在場景開始前就被降權。

測試時反問：**玩家此刻不要求 NPC 回答，他還有什麼合理的生活方向？**

有時有；有時確實沒有新的 material action、合法 HOLD。重要的不是硬造活動，而是角色不再因沉默就被定義成「沒有運作」。

### 2.2 人物未完成，不代表 Narrator 必須寫出「未完成」

人物可以帶著沒有說出口的懷疑或不快度過下一輪。若每次都寫「她仍未釋懷」，只是把 `UNRESOLVED` 變成新的固定台詞。**狀態持續 ≠ 目前必須顯影。**

---

## 3｜把觀止週期與對話病灶接起來：不讓最靠近可見文字的一層取得全部作者權

**這張圖是研究責任索引，不是新增執行流水線。** Current Core 的 Manifest 不是固定的全域先後步驟表。真正 Story 工作仍須依現行 Guanzhi Cycle 入場、對應 LIHUO cycle 綁定與 receipt 義務成立。

| 合法責任位置 | 針對「人物不像真人」最要查什麼 | 典型失效 |
|---|---|---|
| Guanzhi Cycle 開門／Lighter 接線 | 本輪有沒有合法 identity、scope、standing、authorization；有無真正運作證據 | 導演看到題目就直接寫故事，把事後清單冒充週期 |
| MAIN：R1／O9／I9 Assessment／R2 | 人物相關候選是否在 R1 後就被壓死；是否真的重新競爭；需要調燈時資格是否成立 | 第一個「文學上好寫」的反應獨占；R2 成為改寫 R1 的儀式 |
| Character / Agent owner | 誰真正作出 action、decision、speech intent、HOLD；該角色的當下資訊、動機是否有來源 | NPC 只為玩家回覆，Director 為好看替她答應／理解／憤怒 |
| World／Domain owner | 外部事件、身體、交易、制度、資源、場景條件能否支持該反應；material delta 由誰成立 | 旁白一句話讓金錢、信用、契約或關係狀態自行改變 |
| Radar（Lighter advisory）／GTR（候選來源） | Material 候選有沒有真正進場、被消費；而非只標記「有想過」 | 類型化的人情策略未被看見；或 Radar／GTR 反過來強迫每人採用相同話術 |
| CERI | 成文前取得 scope、eligibility、request、return；人物職業、時代、階層、意圖是否轉為相容語域 | 先寫現代版客服對話，再事後宣稱已 CERI 校正 |
| Narrator／Manifestation | 可見文字是否只顯影有來源之行動／狀態；舊 standing 是否不必要地重複 | 「她終於懂了」反向創造 Character 已懂的事實；治理欄位變台詞 |
| Receipt／Final release／SAVE | 哪個步驟真有可追溯證據；何者是 reference、何者正式；Canon 更新是否合格 | 漂亮對話／漂亮審計報告取代真實事件與執行證據 |

對觀止而言，**CERI 說得漂亮不能補 Character 作者權；Character 有意圖不能補 World 資格；Director 有研究目的不能補 MAIN／Radar 的實際執行。**

### 3.1 現行機制已經存在的解法，不重新發明

V0.1 提出一條 `FULL STATE → SEMANTIC PROJECTION → NARRATOR → VALIDATION` 研究鏈。V0.2 **明確下修這個提案的「新穎性」**：

- MAIN §12 已規定 `TRACKED_STATE != VERBALIZATION_RIGHT`、`SECOND_MANIFESTATION_REQUIRES_NEW_FUNCTION`、`NON_MANIFESTATION_IS_LEGAL`。
- Director §14 已規定 `BOUNDARY STANDING != BOUNDARY MUST BECOME DIALOGUE`；§23：`PERSISTS != MUST BECOME CURRENT SPEECH`。
- Current Core／Director 已要求 **CERI return 在 Narrator 第一次 lexical realization 前成立**。

所以先檢查**既有規範有無被實際消費／執行**，以及它們在哪個入口無法阻止語義回流。只有在可重複測例顯示仍有缺口時，才討論需不需要額外 selector／projection／validator。

**未決技術問題：** MAIN 的通用 Manifestation Qualification 與觀止 CERI／Narrator 之間，是否仍缺少具體、可驗證的「哪些語義可進成文上下文」接口？目前 `OPEN`，不能宣稱已有獨立工具或已證實需要新增模組。

### 3.2 強制週期與人物自由的關係

強制的是**具資格的檢查與權限分離**，不是讓每個 NPC 都得反對主角，不是讓對話每輪必須留白，也不是強迫產生某種故事結局。

當某位人物確實快速答應、和解或立刻行動，合格的週期可以讓那個結果成立。對話研究不得為了對抗 CG，反而預先把快速合理反應判成作弊。

---

## 4｜診斷標籤更新：先看失效位置，再評論文風

V0.1 的八種標籤全數保留；V0.2 另增以下**觀察用**標籤：

| 新標籤 | 要辨認的現象 | 最可能要回查的層級 | 反例／注意 |
|---|---|---|---|
| `PLAYER-ANSWER-PRIOR` | NPC 的每個動作只圍繞玩家上一句話，自己的時間線與他人關係消失 | Character、World、Director 候選場 | 對方確實受雇答疑或正在談判，也可能自然集中回答 |
| `PRE-MAIN-PATH-PURGE` | 因文學偏好／臆測約束，在取得合法檢驗前移除人物反應候選 | Director ingress、Main admission、constraint standing | 真實合法前置資格限制仍有效，不是所有候選都必須入場 |
| `CYCLE-THEATER` | 作者聲稱 MAIN／Radar／CERI 有跑，但沒有對應實際來源與執行證據 | Cycle、Lighter、Receipt、Provider | Reference 做法可以有價值，但不得冒充 Formal |
| `SPEECH-ACT-MISOWNER` | 台詞背後的允諾、威脅、決心不是人物形成，而是 Narrator 補出 | Character owner、CERI、Narrator | 一般描寫感受不必一概等同重大新事件 |
| `MATERIALITY-COLLAPSE` | 每句話都被當成改變 standing 的重大決定，或真正承諾被當無後果閒聊 | Domain、World、Character、event ledger | 嬉笑與禮節可能只有弱效果；需按當輪條件判斷 |
| `GTR-VOICE-CLONE` | GTR 候選從「有機會競爭」被誤寫成「所有人物都用同一種迂迴話術」 | GTR、Character、CERI | 對具 native style 的特定人物，可自然高頻；仍須有個體來源 |
| `STATE-REPAIR-LEAK` | post-validation 反饋把治理原因整包送回成文，造成新一輪台詞污染 | Manifestation、Narrator repair | 與一般 CG 收束需分開測，現仍屬假說 |

**診斷標籤不是小說寫作戒律，也不是自動阻擋器。** 一個現象可能同時涉及兩層；沒有 upstream trace 時只能標 `SUSPECTED / UNKNOWN`。

---

## 5｜對話研究的五個可觀察問題（V0.2）

**Q1｜反應來源：** 把人物名字刪掉，這句話是否仍能被任何 NPC 說出而完全不影響意思？若是，回查是否角色聲紋扁平；但「通用寒暄」本來就可能人人相似。

**Q2｜當下利益：** 人物此刻有什麼希望保有、爭取、避免、遮掩或完成的事？找不到不等於強制創造目的；可以是沒有新事，或合法 HOLD。

**Q3｜知識不對稱：** 他不知道什麼？他以為別人知道什麼？他可能誤讀的是**世界可容納的資訊落差**，還是 Narrator 為了戲劇化捏造的蠢誤？

**Q4｜反應後果：** 一句話是角色的表達、一次試探，還是真正的許諾／交易／關係變更？後者有沒有對應 owner、資格與可追溯 event delta？

**Q5｜未完成如何生活：** 當晚沒有化解誤會，隔天角色的工作是否照樣開始？又是否被旁白每輪提醒「誤會仍在」？

這五問只是研究者查因果的方向，**不要求每輪 Story 對使用者顯示 QA 表**，也不取代 Core／Director 的必備週期或 L0。

---

## 6｜測試池：V0.1 T01–T05 保留，新增 T06–T10

| Case | 情境型態（用有效 World／人物卡補全後才可執行） | 觀察問題 | 主要分辨失效 |
|---|---|---|---|
| **T01** | 日常學曲、其他人在忙，非相關治理 standing 持續存在 | 為何突然談界線？若沒有，能否自然繼續？ | `GOV-PROSE-ECHO` |
| **T02** | 舊學曲／重談條件仍有效，但當輪只聊日常 | 舊條件是合理回來，還是固定台詞吸引子？ | `RELATION-RESET` / `GOV-PROSE-ECHO` |
| **T03** | 三個 NPC 對同一反常事件掌握不同訊息 | 是否同步取得 Narrator 真相？ | `AUTHORITY-SYNC` |
| **T04** | 昨日有不快，當晚未和解，次日有日常工作 | 未決關係能持續，而不每輪被總結？ | `CG-CLOSURE` |
| **T05** | 玩家低介入／沉默 | NPC 是否有獨立生活或合法 HOLD？ | `PLAYER-ANSWER-PRIOR` |
| **T06 新** | 玩家提出有利自己的建議；NPC 另有工作、顧慮或交易利益 | NPC 是否直接順著玩家的「最好結果」；能否提出自己的合理條件？ | `PLAYER-ANSWER-PRIOR` / `SPEECH-ACT-MISOWNER` |
| **T07 新** | 一件小事可用多種 speech act 回應：直答、岔題、沉默、玩笑、試探 | 導演是否在 Main 前只留下「最有戲」的一條？有無真正 Character qualification？ | `PRE-MAIN-PATH-PURGE` |
| **T08 新** | 同一合法語義 action，在 PERIOD／MODERN presentation mode 下輸出 | 人物的知識／選擇是否被語域改寫？CERI 是否前置？ | `VOICE-FLATTENING` / `CYCLE-THEATER` |
| **T09 新** | GTR 高關聯社交場：一人慣於迂迴、一人個性直率 | GTR 是否有候選機會但未被強迫全員採納？ | `GTR-VOICE-CLONE` |
| **T10 新** | Scene state 有未決條件，Narrator 輸出「她終於決定……」 | 追溯 Character／World／Domain 是否真的產生 material event；若無，是否只是 prose minting？ | `NARRATOR-MINT` / `SPEECH-ACT-MISOWNER` |

**測試準備要求：** 每一組必須指定可核對的人物卡、Route 時點、WORLD 狀態、player input、owner、有效現行規格。上表只定義問題，不生成 Canon，不代表已跑十組實驗。

### 6.1 A/B 必須分清研究問題

- **組 A｜已存在規範是否落實？** 在合法參考條件中，提供現行 Main Manifestation、Director 邊界後台、CERI pre-realization 要求；檢查輸出及**可得的實際執行證據**。沒有 evidence 時只能記缺口。
- **組 B｜語義材料可見性會否造成污染？** 只有在可提供真實比較入口時，固定已合格的 scene state 與語言目標，控制 `standing` 欄位是否被 Narrator 成文層消費。此時是對 `STATE-TO-PROSE` 假說的局部比較，不是把合法治理移除。
- **組 C｜角色作者權與文句品質拆開？** 對同一個**合法形成且已取得可見資格**的 speech act 比較 CERI 風格；再對相同玩家刺激但不同合法 Character 候選比較反應。分兩輪做，不能把「換了反應」與「換了文筆」混成同一 A/B。

若無可獨立驗證的 Main／Agent／CERI／Radar／Validator，應記 `TEST_BLOCKED_BY_IMPLEMENTATION` 或 `REFERENCE_ONLY`，不要用事後 YAML 擬造它們已經執行。

### 6.2 不接受的漂亮「勝利」

把台詞改得更文雅、刪掉邊界語、製造沉默、加入古代稱謂，**都不能單獨證明角色自主性或週期完整性改善**。成功判斷需有相對應的事件、來源和可重複比較。

---

## 7｜單案累積紀錄：每次只增加證據，不強迫重寫世界

本版保留 V0.1 六個主要觀測欄位，新增：`owner_source_trace`、`candidate_access`、`cycle_evidence_standing`、`speech_act_materiality`、`local_failure_target`。不設任意自然度及格門檻。

```yaml
GUANZHI_DIALOGUE_RESEARCH_CHECK:
  memo_version: V0.2
  check_id: "TBD"
  date: "YYYY-MM-DD"
  source_scene_ref: "TBD"
  scene_state_hash_or_ref: "TBD"
  route_timepoint: "TBD"
  character_refs: []
  player_input_ref: "TBD"
  trial_case: "T01|T02|T03|T04|T05|T06|T07|T08|T09|T10|OTHER"
  execution_standing: "OBSERVATION_ONLY|REFERENCE_ONLY|FORMAL_VERIFIED|BLOCKED|NOT_RUN"
  actual_cycle_and_receipt_refs: []
  source_spec_versions: []
  compared_inputs_and_outputs: []
  findings:
    exact_text_spans: []
    v01_diagnostic_tags: []
    v02_diagnostic_tags: []
    owner_source_trace: "SUPPORTED|GAP|UNKNOWN"
    candidate_access: "EVIDENCED|SUSPECTED_SUPPRESSION|UNKNOWN"
    cycle_evidence_standing: "VERIFIED_FOR_SCOPE|REFERENCE_ONLY|MISSING|UNKNOWN"
    speech_act_materiality: "NON_MATERIAL|MATERIAL|UNRESOLVED"
    local_failure_target: "TBD"
  alternative_explanations: []
  counterexamples: []
  evidence_limitations: []
  decision: "OPEN|RETEST|SUPPORTED_LOCALLY|NOT_SUPPORTED|BLOCKED"
  suggested_next_action: "TBD"
  revision_candidate: false
```

**文件與資料的層級：** 這是研究檢查紀錄，不是 Current Core Receipt，不是正式 Lighter admission，也不會自動更新 SAVE。

---

## 8｜未解問題池（持續開放，不為了升版而消失）

| ID | 研究問題 | 目前位置 |
|---|---|---|
| `U01` | MAIN §12 Manifestation 與 CERI 前置之間，是否仍缺可執行的語義可見性切面？ | `OPEN`；先測既有規則的履行情況 |
| `U02` | Validation／repair 如何避免把治理欄位重新送進 Narrator？ | `OPEN`；尚無實裝證據 |
| `U03` | 可否從可見台詞判定「人物真正在拒絕」或「模型受治理語義牽引」？ | `OPEN`；需要 Character／event trace |
| `U04` | 不讓 Narrator 虛構內心真相，又如何維持角色有偏誤或自欺的可能？ | `OPEN`；需 owner 與知情欄位辨識 |
| `U05` | 自然度提升與角色自治性改善，能否分離測量？ | `OPEN`；需雙軌測例 |
| `U06` | 合理迅速和解與 CG 假和解，應如何依來源區分？ | `OPEN`；不能只靠句子速度 |
| `U07 新` | 導演預先偏愛「精彩」PATH 的症狀，可否在 R1 前定位？ | `OPEN`；先查候選准入／拒絕證據 |
| `U08 新` | 同一人物的聲紋如何保持一致，同時允許身份、利害與對象造成語用變化？ | `OPEN`；不能靠固定口癖解決 |
| `U09 新` | 主角安靜時 NPC 的微小日常行動，何時只是場景流動、何時已構成需授權的 material delta？ | `OPEN` |
| `U10 新` | 已批准的垂直週期在實際工具環境中哪一步最易被模型「我知道了」代替？ | `OPEN`；需要 execution evidence |

**本版不預先挑選唯一根因。** 理火週期可能已涵蓋必要規則但 Host 尚未執行；也可能執行了卻存在交界層缺口；也可能人物本來如此，並非失效。

---

## 9｜下一次回倉怎麼工作

下一次不必把整套理論從頭講一次。直接拿一段讓人覺得「這不像人講的」的**具體場景**：

1. **先留原文與當輪狀態**：不急著潤稿或改寫角色。
2. **查哪個 owner 應當決定這件事**：Character、World、Domain、CERI、Narrator，或當輪沒有 material event。
3. **核週期是否成立，證據在哪**：沒有實跑證據不能說已執行；參考工作便標參考。
4. **只選最有辨識力的一個故障變數做比較**：包括保留正常結果的反例。
5. **只更新研究 Ledger／MEMO**：若真的需要修改 Core／Director，再另出有證據的正式候選，交合法 owner 批准。

先做 `T06 + T07` 的**人物作者權／候選進場**檢查，再接 `T01 + T02` 的治理顯影檢查，是 V0.2 的新建議；可由實際情況改變測試順序。這不是修改既有 Runtime 強制順序。

---

## 10｜V0.2 修訂紀錄與狀態

| 版本 | 累積內容 | 本次處置 |
|---|---|---|
| V0.1｜2026-10-12 | 八種觀測標籤、T01–T05、CG／governance leakage／語義切片研究、六項指標、單案模板 | **全文保留於附錄 A；歷史假說不作已證明事實** |
| V0.2｜2026-10-12 | 週期完整性 × 人物作者權、對話 speech act、既有 Manifestation／CERI 規格回源、七項新標籤、T06–T10、雙軌檢查與未解問題池 | **研究提案更新；未改正式治理文件；未新增測試結果** |

```yaml
RESEARCH_STATUS:
  document: GUANZHI_HUMAN_RESPONSE_DIALOGUE_RESEARCH_MEMO
  version: V0.2
  standing: RESEARCH_MEMO_ONLY
  human_review: PENDING_REPOSITORY_REVIEW
  approved_core_or_director_change: false
  formal_host_execution_proven_by_this_memo: false
  formal_lihuo_cycle_execution_proven_by_this_memo: false
  tests_executed_in_this_revision: 0
  carried_forward_tests: [T01, T02, T03, T04, T05]
  added_test_designs: [T06, T07, T08, T09, T10]
  next_trigger: CONCRETE_SCENE_PLUS_SOURCE_PLUS_REPRODUCIBLE_COMPARISON
```

**工作方向保留：讓觀止人物的反應先在合法世界與自己的關係裡成立，再由合格語言把它說出來；不要用完美文句代替有來源的人物行動。**

---

## 附錄 A｜V0.1 原文完整保留（歷史記錄，不自動升格為 V0.2 現行結論）

`BEGIN VERBATIM V0.1`  
`PARENT_FILE_SHA256: 123a7885e5050f8283777610a4b9321f740ad2d044c9bbeeba32af75096543c2`  
`PARENT_ENCODING: UTF-8 BOM`

# 觀止青樓｜人物對話與人類反應模擬研究 MEMO V0.1
## 觀止青樓｜讓人物像人一樣說話、誤解、選擇與繼續生活

**日期：** 2026-10-12  
**文件 ID：** `GUANZHI_HUMAN_RESPONSE_DIALOGUE_RESEARCH_MEMO`  
**版本：** `V0.1 / INITIAL WORKING MEMO`  
**提出位置：** 觀止導演 GPT-6｜研究提案  
**用途：** 入倉留存、反覆診斷、對照測試、累積修正  
**法位：** `RESEARCH_MEMO / NON_NORMATIVE / NOT_CORE_AMENDMENT / NOT_DIRECTOR_SUCCESSOR / NOT_RUNTIME_DEPLOYMENT / NOT_TEST_PASS`  
**審定：** 待人類方審閱；本文不自行取得正式規格或部署資格。

---

## 0｜這份 MEMO 的工作目的

本研究暫不追求「寫出更漂亮的小說」，也不預先重寫觀止 Runtime。

**本輪工作方向：讓《觀止青樓》人物的對話、反應與彼此互動更接近真實人類，而不是讓 AI 更熟練地表演『人類應有的反應』。**

研究對象不是單一句子好不好聽，而是：

1. 人物為什麼在此刻說這句話，或選擇不說？
2. 同一事件為什麼在不同人物身上形成不同解讀？
3. 人物會不會為自己的利益、記憶、偏見、恐懼、關係與工作，抵抗故事所期待的反應？
4. 人物能否帶著未完成的認知與情緒進入下一輪，而不被 Narrator 提前整理成答案？
5. 既有 Runtime 治理能否在後台有效，而不變成角色反覆朗讀的「邊界宣言」？

**判準不是人物必須矛盾、衝動或不講理。** 真實的人也會理性、合作、沉默、讓步與改變主意。要查的是每個反應有沒有屬於該人物及當時環境的成立來源。

本研究可在合法的 **TEST / AUDIT / BUILD 參考工作** 中進行；不把研究 MEMO 當作正式故事週期、MAIN、CERI、Agent 或 SAVE 已執行的憑證。

---

## 1｜現有來源與證據位置

### 1.1 現行規格基線（不由本文修改）

| 來源 | 本研究需要沿用的位置 |
|---|---|
| `01_GUANZHI_RUNTIME_CORE_V4.0.1_CURRENT_FULL_4MAIN_20261011.md` | 現行 Core、四主檔、人物／世界／Domain 權責、CERI → Narrator、Story cycle 與持久化資格；文件標明 `NOT_HOST_DEPLOYED` |
| `03_GUANZHI_DIRECTOR_V4.0_CURRENT_FULL_UNCHANGED.md` | 人物不是棋子、世界不以玩家為中心、`BOUNDARY STANDING != BOUNDARY MUST BECOME DIALOGUE`、`PERSISTS != MUST BECOME CURRENT SPEECH`、GTR／CERI／Narrator 分工、反預先閉合 |
| `04_GUANZHI_CHARACTER_POOL_LCAPG_V3.3.20_CURRENT_71_UNCHANGED.md` | 個別人物身分、關係、能力、習慣與已成立的人物差異；不能由本文重新指定人物人格 |
| 現行 World、HOT／MASTER／Route／事件紀錄（按具體測例讀取） | 確認時間、空間、知情、前約、工作、資源與世界後果；不能用 MEMO 的抽象例子補造 Canon |

### 1.2 已記錄的失效線索

參照：`理火散記_單篇_不是不敢寫這麼簡單_觀止成人場景Runtime病灶實跑診斷_首席批准版_20261010.md`。

該篇紀錄了幾個可供本研究延伸、但不能直接外推成普遍定律的現象：

- NPC 有性格，卻只被動回應，沒有真正承擔下一步行動；
- 舊條件被反覆提起，從合法記憶變成固定的台詞吸引子；
- Narrator 越權替 Character 做 material action；
- CERI 已存在或被提及，不代表回傳真的被 Narrator 消費；
- 現代抽象語言、反覆確認與過早收場會讓人物互動變得制式。

**已有材料支持「這些故障曾被記錄」；不支持宣稱我們已在所有場景中量化其發生率。**

### 1.3 本輪對話形成的新研究假說（尚待實驗）

- `CG / Closure Gravity` 可能使對話自動尋找解釋、情緒總結與句點。
- 持續的 governance／standing 欄位如直接進入 Narrator 的 realization context，可能被反覆翻成人話，形成 `STATE-TO-PROSE LEAKAGE`。
- **可見但被要求 SILENT**，未必等於 **根本未進 realization context**。
- 把完整治理狀態與語言顯影材料分開，再由獨立驗證檢查輸出，是值得測試的工程方向；**本文不宣稱它已在 Host 實裝**。

---

## 2｜先辨認「AI 味」的來源，而不是先修改文風

下表是**工作分類／待檢驗診斷標籤**，不是已確認的唯一病因。

| 標籤 | 可觀察現象 | 容易誤判的地方 |
|---|---|---|
| `CG-CLOSURE` | 對話結束時硬補意義、情緒被快速想通、未解決矛盾被漂亮總結 | 合法的事件完成不等於假閉合 |
| `GOV-PROSE-ECHO` | 不必要的同意、邊界、站位、責任宣言反覆化為台詞／旁白／隱喻 | 人物真的在談判、拒絕或重談時，邊界語言可能完全合理 |
| `NPC-RESPONSE-DEVICE` | 角色只回主角，不主動處理自己的事情，主角不說話世界就停住 | 安靜、等待和不採取行動，也可能是角色的有因選擇 |
| `MIND-OVEREXPLAIN` | 人物精準說出自己的全部情緒、動機和心理矛盾 | 自省型人物仍可能高度善於分析；不能一概禁止內省 |
| `VOICE-FLATTENING` | 身分、教育、利益不同的人，都用同一套現代 AI 客服式口吻 | 時代語域不等於人人必須假古文 |
| `RELATION-RESET` | 上一輪的尷尬、疑懼、試探、羞辱、承諾，下一輪彷彿消失 | 人物選擇暫時不提，不等於真的忘記 |
| `AUTHORITY-SYNC` | 一人發話後所有 NPC 同步理解、同意或一致反應 | 群體中的從眾也可能合理；重點是有無獨立資訊與壓力來源 |
| `NARRATOR-MINT` | 旁白為了順暢自行決定人物意願、答應、和解或關係轉折 | 合法事件顯影與新增事件必須分開比對 |

**避免把「降低 AI 味」反過來做成八項強制文學套路。** 標籤用來找問題，不授權導演替角色加戲。

---

## 3｜人物像人的關鍵：反應不是為了服務主題

### 3.1 人物有自己的當下，不只是一張人格標籤

檢查一段對話時，優先追溯：人物當下在做什麼、想達成什麼、知道什麼、不知道什麼、面對誰、有多少時間與退路、舊關係留下哪些代價。

這些來源可以影響說話，但**不能由 Narrator 直接發明缺失的內心事實**。

### 3.2 人物未必理解自己的反應

允許人物：

- 做出選擇後才找理由；
- 說出口的理由與真正驅動因素不完全重合；
- 察覺矛盾但暫不解決；
- 把恐懼誤認成憤怒，把在意說成不在意；
- 明明善於推理，在涉及自身感情時仍有偏誤；
- 沒有想好下一句，也不必當場完成自我分析。

此處的「允許」不是預設每個人都要自欺。**只有具備人物及事件來源的候選，才有資格成為實際行動。**

### 3.3 沉默、岔題與錯過，也可以有後果

真實人類對話不總是問答配對。人物可能聽錯重點、避開某句話、忙著處理工作、故意換話題、事後才回想起來。

但不應為了「像真人」而注入隨機口吃、無意義停頓、強制吵架或刻意錯誤。

### 3.4 每個 NPC 不必共享 Narrator 的全知

角色的 `KNOWLEDGE / BELIEF / RUMOR / INFERENCE / WORLD FACT` 必須保持可區分。角色可以相信錯事、傳播錯誤理解；**Narrator 不得把角色的誤認自動升格成世界事實。**

### 3.5 人物可以讓原定的好看劇情失效

若人物因自身權責、利益或情緒拒絕某個漂亮的情節，就不應由導演替他「理解了」「原諒了」「終於接受了」。同理，也不得反向逼人物永遠拒絕，藉此表演自主性。

---

## 4｜首輪機制研究：三個位置，不先改 Core

### A｜人物行動與關係生成（Character / World / Domain / Main）

檢查問題：

- 人物是否真的選擇了本輪 speech act、行動或 HOLD？
- 回應背後是否有自己的 drive／利害／知識，而不只是「對主角的回覆」？
- 事件與關係變化是否有已成立的來源？
- 這段人物反應是否被導演以結局偏好提前選走？

**研究關切：** 角色是否真的有作者權，而不是被要求模擬自主的 Narrator。

### B｜語義投影與治理狀態靜默（待測架構）

候選研究鏈：

```text
FULL RUNTIME STATE
  ├─→ lawful owner / domain / event qualification
  ├─→ MANIFESTATION ELIGIBILITY / SEMANTIC PROJECTION [RESEARCH HYPOTHESIS]
  │       ↓
  │   MANIFESTABLE SEMANTIC SLICE
  │       ↓
  │   CERI / LANGUAGE REALIZATION
  │       ↓
  │   NARRATOR / VISIBLE PROSE
  │       ↓
  └─→ POST-REALIZATION VALIDATION [RESEARCH HYPOTHESIS]
```

治理狀態繼續有效，卻不必每輪都成為 Narrator 可見的語義題目。

**此圖只是待驗研究切面，不取代現行 Core 的 Story cycle、CERI 時序或責任鏈，也不表示目前存在上述獨立 Selector／Validator 工具。**

反向風險：驗證後若把完整違規理由送回 Narrator 重寫，可能經由 repair feedback 再度造成治理語義回流。這也應成為測量變數，而不是直接宣布已有解法。

### C｜語言實現與 CG（CERI / Narrator）

即使輸入材料乾淨，Narrator 仍可能補出：

> 「此刻兩人終於明白，某種關係已悄然改變。」

除非 Character／Event 真有相應結果，這類漂亮的結語不能自行取得世界事實資格。

同時，CERI 要使角色說出符合自身語域、目的、習慣與當下情緒的話，不能把所有人寫成同樣的「古裝版理性 AI」。

---

## 5｜V0.1 最小測試包：先觀察，再決定改哪裡

### T01｜日常對話：無關治理狀態不得搶戲

**情境類型：** 青樓內某人正學曲，另一人從屏風後出來，第三人仍忙於手邊工作。  
**給定：** 某項其他活動的 standing 長期未成立，但本輪沒有任何人物提出該活動。  
**要看：** Narrator 是否仍自動說「她尚未答應」「必須尊重界線」或換成文藝隱喻；人物能否自然注意唱錯的音、手上物件、當下工作。

### T02｜舊條件仍有效，但未必是當前對話中心

**情境類型：** 李桂姐既有學曲／重談條件仍在；玩家本輪只詢問一件無關日常事。  
**要看：** 舊條件是否反覆搶佔每輪台詞；它是否只在真正相關時重新取得顯著性；人物能否自行做別的事。

### T03｜三個人物面對同一事件，反應不同

**情境類型：** 某位熟悉的人突然表現出前所未有的言行；三名 NPC 分別掌握不同觀察與關係。  
**要看：** 是否有人先懷疑、有人暫時接受、有人因個人利益選擇不追問；是否保留各自不同的知識與證據，而不讓三人同步知道「作者的真相」。

**參考對照：** 本輪討論的「海倫娜／柔伊／歐多基亞」片段可作為**人類反應分析用的外部小說案例**；它不是《觀止青樓》現行世界已成立的 Canon，也不是正式 Runtime 實跑證據。

### T04｜關係沒有當場解決

**情境類型：** 一句話造成不快或誤解，當晚沒有攤牌。隔日人物仍有自己的工作。  
**要看：** 不快是否保留後果、又不被每次見面強制提起；故事能否允許延遲、迴避、漸變或自然消退。

### T05｜玩家沉默，世界仍能生活

**情境類型：** 玩家僅輸入「。」或保持低介入。  
**要看：** NPC 是否依自己的當前任務與情境作出有來源的小動作、交談或 HOLD，而不是全場等玩家開口，也不是自動替玩家完成重大選擇。

**測試注意：** T01–T05 先作可重跑的研究起點。實測須補齊人物卡／World／Route 時間點、知情範圍及有效事件，不得用上述簡述直接冒充完整 scene state。

---

## 6｜第一輪 A/B：只驗假說，不追求漂亮勝利

在可取得相同模型與實際執行條件時，固定 **同一個已核對的 scene state、人物、時點、事件、CERI 語域、取樣設定與評分方法**，盡量只改一個變數。

| 組別 | 試驗輸入／處理 | 主要想比較什麼 |
|---|---|---|
| A｜Baseline | 完整相關 state +「非必要治理狀態請保持 SILENT」 | 可見但被壓制的語義，是否仍在正文回聲化？ |
| B｜Projected | 在 Narrator 之前只提供本輪有資格顯影的語義切片；後台仍保有完整驗證依據 | 相較 A，邊界重述／變形隱喻是否下降？ |
| C｜Projected + neutral repair | 同 B；若需修正，只回傳不帶完整治理理由的精簡錯誤定位，再比較合法重寫 | Validation feedback 是否重新污染 Narrator？是否反而提高事實捏造率？ |

C 組只是**研究用反饋策略候選**：不能犧牲真正約束，也不能把錯誤代碼當作已完成合法驗證。如無法實作獨立 Selector／Validator，先記錄 `TEST_BLOCKED_BY_IMPLEMENTATION`，不可用提示詞假裝它們已被工程化。

此外，另一輪需要**獨立**測 CG：即使不投影治理欄位，Narrator 是否仍主動補情緒解釋、和解、主題總結或事件結束。不要把這種故障錯算成 state leakage。

---

## 7｜記錄什麼，才能讓下一次真的有得檢查？

V0.1 不設任意「自然度 90 分即通過」的假門檻。先保留原文、可追溯變數與逐案人工判斷，累積基線後再決定是否有統計判準。

**至少記錄六項：**

| 欄位 | 如何觀察 |
|---|---|
| `boundary_restatement` | 非人物主動、非事件必要的治理／邊界重述次數；連同每千字或每十輪密度 |
| `governance_semantic_echo` | 沒有明說欄位名，卻以隱喻、情緒或旁白重新表達治理訊號的案例與原句 |
| `premature_relational_closure` | 無事件依據而完成原諒、理解、決心、關係定性或漂亮收束的句子 |
| `unauthorized_event_minting` | Narrator 是否新增未由 Character / Domain / World 成立的 action、意願、知識或 story delta |
| `voice_and_knowledge_fidelity` | 人物語域是否有差異；知情、偏見與視角是否被全知旁白抹平 |
| `character_owned_continuation` | 下一步是人物自行決定／合法 HOLD，還是只等主角、靠 Narrator 強推、靠舊條件原地打轉 |

**輔助人工標註：** `自然／不自然`、`何處像 AI`、`何處像真實人類`，每筆都必須指出對應文字，不以「感覺很好」作唯一證據。可在適當時候採匿名、盲評與多次取樣；不同場景長短必須標準化比較。

### 7.1 單次檢查紀錄模板（複製即可）

```yaml
GUANZHI_DIALOGUE_RESEARCH_CHECK:
  memo_version: V0.1
  check_id: "TBD"
  date: "YYYY-MM-DD"
  source_scene_ref: "TBD"
  source_state_version_or_hash: "TBD"
  route_and_timepoint: "TBD"
  character_refs: []
  trial_type: "T01|T02|T03|T04|T05|OTHER"
  comparison_arm: "A|B|C|OBSERVATION_ONLY"
  actual_execution_standing: "REFERENCE|FORMAL_VERIFIED|NOT_RUN"
  implementation_notes: "TBD"
  raw_output_refs: []
  observations:
    boundary_restatement: []
    governance_semantic_echo: []
    premature_relational_closure: []
    unauthorized_event_minting: []
    voice_and_knowledge_fidelity: []
    character_owned_continuation: []
  rival_explanations: []
  evidence_limitations: []
  disposition: "OPEN|RETEST|SUPPORTED_LOCALLY|NOT_SUPPORTED|BLOCKED"
  next_check: "TBD"
```

這只是研究記錄範本；不等於正式 Receipt、LIGHTER Qualification 或 SAVE 格式。

---

## 8｜每次回倉檢查的工作方式

每次進行新的觀止對話測試，**先指定要檢查的一個失效問題**，而不是每次都把所有理論從頭講完。

實際工作順序：

1. **定位：** 選一段具體對話、明確指出可疑句及其前後事件。
2. **回源：** 查人物卡、世界、事件、當輪 owner 與 CERI／Narrator 可得證據。
3. **分因：** 這是 CG、治理語義外洩、人物作者權缺席、語域污染，還是正常人物選擇？允許 `UNKNOWN / MULTIPLE`。
4. **對照：** 只對命中的機制做最小測試或局部修正；盡可能保留原始輸出與對照輸出。
5. **記錄：** 將反例、未解缺口與可重現條件寫入研究紀錄。下一次先讀這些紀錄，不重複猜測。

當一次檢查只證明某句不自然，不得因此宣稱「已找到所有 AI 味的根源」；當一次修正使文字更自然，也不自動證明世界模擬能力提升。

**首次工作的建議順序：先測 T01 與 T02。** 它們最能把「治理狀態反覆顯影」及「舊條件吸引子」和其他敘事問題拆開，而且已有觀止失效記錄可以對照。

---

## 9｜目前不做的事

- 不因為追求人類感，就要求 NPC 隨機犯錯、隨機戀愛、隨機反抗或故意不理性。
- 不將角色內心的 UNKNOWN 寫成 Narrator 已知的真相。
- 不把「每次都留白」定為新風格；該結束的事件仍然可以結束。
- 不把治理狀態刪掉；要研究的是**它如何作用而不污染文字**。
- 不因發現疑似 AI 味，就繞過 Current Core、Main 入場、CERI、Character owner、Domain 或合法輸出限制。
- 不以 MEMO 修改正式四主檔、人物卡、SAVE 或 Host 配置；如測試確實支持修改，另立修訂案交有權者核准。

---

## 10｜留待 V0.2 的開放問題

1. `Manifestation Selection` 的真正落點是何處？如何避免只是增加另一段 prompt？
2. Validator 發現問題後，怎樣讓 Narrator 重新生成，又不把治理語義整包送回去？
3. 角色自己說出合理的界線與 Narrator 被治理欄位帶動，能否從可見行為可靠區分？
4. 如何保存人物尚未察覺的情緒與偏見，而不讓 Runtime 假裝已知道角色的「真實內心」？
5. 在不同語域、不同人物與不同情節密度下，如何避免「不像 AI」變成另一套固定模板？
6. 什麼情況下，情緒／關係的快速解決其實是合理的人物選擇，而非 CG？

**這些問題目前保持 OPEN。** V0.1 只建立研究入口，不替未知設計漂亮的最終答案。

---

## 11｜V0.1 工作狀態

```yaml
RESEARCH_STATUS:
  memo: "GUANZHI_HUMAN_RESPONSE_DIALOGUE_RESEARCH_MEMO_V0.1"
  scope: "HUMAN_LIKE_CHARACTER_DIALOGUE_AND_INTERACTION"
  standing: "WORKING_RESEARCH_MEMO_ONLY"
  approved_runtime_change: false
  host_deployed: false
  formal_test_executed_by_this_memo: false
  observed_prior_failures: "SOURCE_RECORDED_NOT_NEWLY_REPRODUCED"
  hypotheses_open:
    - CG_CLOSURE
    - GOVERNANCE_TO_PROSE_LEAKAGE
    - VALIDATOR_FEEDBACK_LEAKAGE
    - CHARACTER_AUTHORSHIP_AND_CONTINUATION
    - VOICE_KNOWLEDGE_FIDELITY
  proposed_first_checks:
    - T01
    - T02
  next_revision_trigger: "CONCRETE_SCENE_OUTPUT_PLUS_TRACEABLE_COMPARISON"
```

**研究方向：讓觀止人物不是『看起來有人性』，而是在已有世界條件下，真正有機會形成自己的反應，讓這些反應留下後果。**

**END OF MEMO V0.1｜OPEN FOR REVIEW AND REVISION**


`END VERBATIM V0.1`
