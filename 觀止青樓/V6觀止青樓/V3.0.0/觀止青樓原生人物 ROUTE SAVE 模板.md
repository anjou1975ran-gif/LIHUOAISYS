# 觀止青樓｜原生人物 ROUTE SAVE 模板 V0.1

**法位：** HUMAN_RATIFIED_DOCUMENT_2026_10_29 / APPROVED_ROUTE_LOCAL_FORMAT_TEMPLATE / NOT_ACTIVATED / NOT_RUNTIME_SAVE / NOT_SHARED_CHARACTER_POOL
**日期：** 2026-10-27
**命名禁則補修：** 2026-10-27／人類明示：十姓禁用＋同一個新創名字中高頻警戒字最多一個；保留既有角色姓名，不宣稱此警戒字庫是統計排名。
**目的：** 原生人物可以先只在某條故事線出現。SAVE 保存她已走過的事實，讓她逐步顯影，不必初登場就寫完姓名、八軸、性愛偏好、身世和未來命運。
**建議實際位置：** 複製至 觀止青樓/SAVE/<實際故事線>/原生人物_SAVE.md；一線一份人物表或每人一檔皆可。原有 HOT／MASTER／人物履歷 RCL 仍各司其職，不由本模板自動取代。
**理火接線法位：** 模板為已獲人類授權的 Route-local 格式，不自帶治理週期；需要完整理火工作時，依觀止 CORE／Director 接現行 **LIHUOOS V1.4（L8 V1.3／L9 V1.2.2／Main V5.1.1＋V5.1.2）**。此模板沒有啟動 Runtime，亦不替原生人物決定意志或幫任何 Route 寫 SAVE。
**保存限制：** 寫下這個模板不等於已有故事線 SAVE。只有具體事件與實際寫入經驗證，才能聲稱對應資料被持久化；不能假稱 Host 或 Runtime 已部署。

---

## 0｜原生創建的前置選角規則（2026-10-29 人類正式批准）

> **「導演因為劇情需要調用新人物，優先從人物池找適合的人物，若無，才進行原生。」**

1. 導演先檢索**觀止人物池 V3.0.0（73 人）**與當 Route 已有、仍適用的人物，檢查是否有符合情境的身份、地點、時間、關係、可達性、知情與人物意願者。
2. **存在合適人物：優先從既有人物選用。** 人物卡入池不是已到場證據；是否真正出場仍需其當次行動、世界條件及授權來源。
3. **不存在合適人物：才可原生建立。** 可以先以路人稱謂最低限度登場，必要時再固定本地 ID；不能為了避免查池或製造新奇，任意生成重複人物。
4. 原生角色的當線事實只寫入本 Route；人類另行批准前不得自動升格共用人物池。人物意志、世界因果、當線保存依各原有 Owner。

這條是**選角次序**，不是角色出場排程器，也不授權為劇情便利奪走池內人物的自由；人類明示指定新人物或既有特定人物時，以人類有效明示與世界條件處理。

---

## 1｜原生人物命名禁則

~~~yaml
ORIGINAL_CHARACTER_NAMING_RULE:
  forbidden_director_generated_surnames: ["沈", "顧", "柳", "蘇", "林", "江", "陸", "葉", "蕭", "白"]
  applies_to: "由導演替全新純原生人物自行創造的姓名"
  exceptions:
    - "人類明示指定姓名或同意例外（記錄來源）"
    - "已存在的人物池與既有故事線正式姓名"
    - "真實歷史、文學 donor 和有來源依據的人物原名"
  frequent_given_name_warning_chars: ["清", "晚", "若", "念", "知", "雪", "棠", "煙", "月", "汐", "瑤", "兮", "芷", "柔", "霜", "歌"]
  max_warning_chars_per_new_given_name: 1
  given_name_scope: "僅計名字（姓氏之後的名），適用導演自行新創人物；同一名字最多含一個警戒字"
  count_rule: "按字的出現次數計；同字出現兩次亦為2個，不能以不同字才算2個"
  examples:
    - {candidate: "汐月", warning_char_hits: ["汐", "月"], count: 2, result: "REJECT"}
    - {candidate: "汐婷", warning_char_hits: ["汐"], count: 1, result: "ALLOW"}
    - {candidate: "桂枝", warning_char_hits: [], count: 0, result: "ALLOW"}
  further_bans: "只能由人類後續明示擴充"
  name_rule_note: "十姓屬人類硬禁；十六個名字警戒字屬本專案的防同質化工作字庫，不冒充經實測的AI真實字頻排名"
  note: "避免AI高頻姓名模板；命名前檢查重名、時代、家庭、職業與階級"
~~~

**規則判讀：** 先檢查新創原生人物的姓氏是否落入十姓禁用表，再檢查**名字（不含姓）**中十六個警戒字的出現次數。零個或一個可以；兩個以上必須重取。比如「汐月」因為包含「汐＋月」而不通過，「汐婷」只命中「汐」所以通過。這是**逐一姓名**的檢查，不是禁止一條故事線出現兩個名字各含一個不同警戒字。

人類明示的原有人名、既有故事線、歷史文學原名不受本次禁則追溯；若人類明確指定例外，保留其指定並記錄來源，不自行改成合規新名。這些警戒字並非不能寫入人物的詩詞、對話或地名，限制僅作用於導演自行創作的人名。

不強制每個人姓氏漂亮、身份神祕、性格清冷、出身名門、一定有黑歷史或愛情線。可以先用「西街挑水婦人」「當鋪新夥計」等臨時稱呼。此規則**不回頭改名**：例如人物池既有顧青簡、沈玉晶、柳如是、蘇清、白玉潔等來源名字照舊保留。

## 2｜第一次出場：只要最少四項

~~~yaml
ORIGINAL_CHARACTER_MINIMUM:
  route_id: "REQUIRED"
  local_id: "NPC_LOCAL_001"
  seen_as: "UNKNOWN / 臨時稱謂"
  first_scene_anchor: "REQUIRED"
  first_observed_action_or_word: "REQUIRED"
  status: "ROUTE_ONLY / NOT_SHARED_POOL"
~~~

缺姓名、職業或身世不算失敗。新人物由當場行動取得最小存在資格；人物想說什麼與導演已知什麼並不相等。

## 3｜當線人物資料｜只填已知欄位

每新增一位原生人物，複製一段「NPC_LOCAL」；同一局部識別碼須在這條線穩定，不重用給另一人。

~~~yaml
ORIGINAL_CHARACTER_ROUTE_SAVE:
  route_id: "REQUIRED"
  local_id: "NPC_LOCAL_001"
  name:
    current: "UNKNOWN"
    aliases: []
    naming_source: "UNKNOWN"
    surname_rule_checked: false
    given_name_warning_char_rule_checked: false
  first_entry:
    scene: "UNKNOWN"
    time_precision: "UNKNOWN"
    location: "UNKNOWN"
    evidence: "UNKNOWN"
  person:
    confirmed_adult: "UNKNOWN"
    appearance_observed: []
    occupation_claimed: "UNKNOWN"
    occupation_verified: "UNKNOWN"
    legal_and_social_status: "UNKNOWN"
    abilities_demonstrated: []
    voice_or_gesture_observed: []
    habits_observed: []
    source_history_confirmed: []
    speculation_not_fact: []
    ambitions: []
    private_desires: "UNKNOWN"
    intimacy_tags:
      status: "NOT_NEEDED / UNKNOWN"
      tags: []
  relations:
    confirmed_links: []
    unverified_claims: []
  knowledge:
    this_character_knows: []
    player_knows: []
    others_know: []
    director_confirmed: []
  continuity:
    current_location: "UNKNOWN"
    last_observed_event: "UNKNOWN"
    property_or_money_confirmed: []
    unresolved_threads: []
    open_questions: []
  state:
    route_only: true
    shared_pool: "NOT_PROPOSED"
    save_write: "DRAFT"
~~~

此格式可以只有第一次登場時填的幾格，然後一場一場累積。性偏好是可選人物線索，不因妓籍、外觀、工作或曾有關係便推得；涉及成人親密的人物，需先確認其為成年人。

## 4｜事件後，只記新的 Delta

~~~yaml
CHARACTER_SAVE_DELTA:
  route_id: "REQUIRED"
  character_local_id: "NPC_LOCAL_001"
  scene_anchor: "REQUIRED"
  event_time_precision: "UNKNOWN / 午後等真實精度"
  kind: "NAME / STATUS / ACTION / RELATION / KNOWLEDGE / BODY / OTHER"
  observation: "這次實際發生／聽見什麼"
  evidence: "場景、文書、證詞或有效 SAVE"
  class: "ESTABLISHED_ACTION / SELF_REPORT / RUMOR / DIRECTOR_CANDIDATE"
  known_by: []
  still_unknown: []
  scope: "CURRENT_ROUTE_ONLY"
  actual_write: "PENDING / VERIFIED"
~~~

- 人物自述首先證明**她說過**，不保證說的都是真的；流言不可硬升為事實。
- 導演擬議、角色意願、別人猜測、物理能力、願望和實際完成事件要分開保存。
- 人物可能沒有姓名，可能沒秘密；不為了填滿資料捏造「從小就」或「早已」發生的事。
- 修訂已存事件須留足變更依據；不同路線的婚姻、財物、死亡、見面與秘密不能互相倒灌。

## 5｜從當線人物升格至共用人物池

~~~yaml
POOL_PROMOTION_CANDIDATE:
  original_route_id: "REQUIRED"
  original_local_id: "NPC_LOCAL_001"
  portable_shared_baseline: []
  route_specific_events_not_to_import: []
  name_and_identity_checked: false
  author_decision: "PENDING"
  actual_pool_write: "NOT_DONE"
~~~

原生人物在某線活得精彩，可以提名入共用池，但**不能自動升格**。共用池只提煉能跨線成立的人格、來源、能力和世界位置；該線 SAVE 仍保管專屬歷史，不因入池而消失。

**例子：** 羅見微目前仍是人類接受的原生人物設定提案；尚未有特定 Route 出場事件，不應捏造她的實際 SAVE。崔鶯鶯則屬《西廂記》來源人物，使用人物池候選而非當線純原生 SAVE 的初創流程。

---

**最小原則：** 第一次見面記她是誰（甚至不用有姓名）、做了什麼；第二次再記變化。不要一出場就替她完成一生。

END OF TEMPLATE
