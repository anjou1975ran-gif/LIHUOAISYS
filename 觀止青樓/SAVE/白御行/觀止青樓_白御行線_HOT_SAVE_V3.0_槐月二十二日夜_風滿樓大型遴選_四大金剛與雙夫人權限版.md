# 觀止青樓｜白御行線 HOT SAVE V3.0
## 理火三年槐月二十二日夜｜風滿樓大型遴選 × 定陶女性事業直轄案 × 蘇清月事用品專案 × 特殊人才五人交易 × 白家四大金剛與雙夫人內部權限版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V3_0_HUAI22_NIGHT_FENGMANLOU_SELECTION_WOMENS_BUSINESS_SPECIAL_TALENTS_FOUR_VAJRAS_TWO_MADAM_AUTHORITY"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V3.0"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime_document_profile: "GUANZHI_QINGLOU_V11.0-R2"
  character_source: "觀止人物卡池_LCAPG_V2.1"
  story_date: "理火三年槐月二十二日"
  time_of_day: "夜間；風滿樓大型遴選仍在運作，特殊高價複核區已收工"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "HOLD_AT_ZHANG_LIHUA_ROOM_AFTER_FOUR_WOMEN_RECOGNIZE_LIHUA_MADAM"
  previous_valid_hot: "觀止青樓_白御行線_HOT_SAVE_V2.9_槐月二十一日深夜_曹州假印立案_定陶總會架構_京師女裝企畫與師師抱睡版.md"
  previous_hot_sha256: "8a103e918723b5b82df2a21e265906b11f6c2c0510f17dc1b123d2c67787e9e3"
  long_term_master: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"
  experimental_overlay:
    file: "觀止青樓_PATCH_風月角色表演與接戲能力_V0.1-EXP_獨立試跑未併主系統.md"
    status: "INDEPENDENT_TRIAL_OVERLAY_NOT_MERGED_TO_MAIN_SYSTEM"
  save_scope:
    - "HOT V2.9 後至槐月二十二日夜之直接玩家線事件"
    - "風滿樓主廳空間狀態、大型新人遴選、牙行與觀眾規則"
    - "定陶女性注意力／偶像式事業之秘密直轄架構"
    - "蘇清二十八日私約後續工作化安排與月事用品專案"
    - "李師師、張麗華成人丫環候選"
    - "李瓶兒未來如夫人並列之私人談話與輕吻"
    - "特殊高價複核區五名人才之成交、持契、價格、用途與保密"
    - "白三十二娘、白明礬、白紅伶、白希之工作身份、華服買斷、內部紀律"
    - "李師師『白夫人』與張麗華『麗華夫人』對四人之不同內部權限"
```

---

# 0｜提交法位、來源與本輪反污染

```yaml
SOURCE_LINEAGE:
  direct_previous_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V2.9_槐月二十一日深夜_曹州假印立案_定陶總會架構_京師女裝企畫與師師抱睡版.md"
    role: "本檔直接前置 HOT；V2.9 及以前有效硬狀態全部繼承"

  master_archive:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.2-R1_截至HOT_V2.5固化_保留V2.6-V2.8_HOT版.md"
    role: "截至 HOT V2.5 之長期因果；V2.6-V2.9 由 HOT 鏈承接"

  current_route_conversation_commit:
    role: "HOT V2.9 後至本次 HOT SAVE 命令前之直接劇情、玩家明示自身言行與 NPC 可觀察回應"

COMMIT_NOTE:
  - "本檔取代 HOT V2.9，成為白御行線最新直接接關切片；V2.9 保留為前置歷史來源。"
  - "本次只更新 HOT；不更新 MASTER，不修改人物卡池，不把四名新購女性升格為跨線人物卡。"
  - "新女性事業之『48／神七／御三家』架構目前為白御行線秘密商業模型，不自動升格世界基線。"
  - "風滿樓不是另一棟建築；本輪所稱風滿樓為觀止主廳進入擴張／異常空間狀態後之形態。任何『另租一棟風滿樓／走去另一棟樓』舊生成均視為污染，不寫入本 SAVE。"
  - "人物工作身分、持契與服從關係不等於任何特定成人行為已取得同意；特定成人事件仍須另行形成事件狀態。"
  - "白御行之『送去餵魚』是其對洩密／告密／背叛的懲戒宣示與威嚇規則；本輪未實際發生任何因此被殺、被處決或被送去餵魚之事件。"
```

---

# 1｜當前時間、位置與直接接關點

```yaml
CURRENT_SCENE:
  date: "理火三年槐月二十二日"
  time: "夜間；精確時刻未知"
  primary_location: "觀止青樓／張麗華房間門內外；風滿樓主廳仍在運作"
  mode: "HOLD_AFTER_HOT_SAVE_COMMAND"

  player:
    name: "白御行"
    current_position: "張麗華房內／正準備帶四名新購女性離開"
    last_confirmed_utterance:
      - "白御行對張麗華說：『是，那夫人我們滾出去了喔。』"
    no_new_player_action_after_save_command: true

  present_or_immediate:
    - "張麗華／房內"
    - "白三十二娘"
    - "白明礬"
    - "白紅伶"
    - "白希"
    - "紅娘氏／近門口同行"

  parallel_world_state:
    - "風滿樓主廳大型遴選尚未整體收場。"
    - "特殊高價複核區已由白御行明示收工，不得再自動追加『最後一名特殊候選』。"
    - "潘金蓮仍在處理今晚遴選、價格與明日容量；白三娘、疏影等仍在各自評估位置。"
    - "蘇清、常煒及常煒名下新購物流女子此前在二樓／後台秘密工作區推進月事用品與女性事業相關工作；本輪未觀察到其後續離場。"

  direct_resume_options_without_forcing_player:
    - "白御行可帶四人返回風滿樓前堂。"
    - "世界可在前堂推進今晚一般遴選結果、明日大批潛力甄選準備、觀眾票價或人物自主事件。"
    - "不得替白御行自動付款、回房、離場、睡覺或跳到翌日。"
```

---

# 2｜V2.9 繼承中仍活躍之核心狀態

```yaml
INHERITED_ACTIVE_CORE:
  cao_zhou_fake_seal:
    status: "ACTIVE_UNDER_ASSOCIATION_HANDLING"
    note: "曹州程姓商人假印案已交顧青簡／總會流程；觀止女性不負責偵查。"

  dingtao_general_association:
    - "總會負責跨團運輸、通路、信用、技術／授權與重大架構；地方商團日常自主、自籌資金、自負盈虧。"
    - "京師／觀止所在區域為總會樞紐；定陶老家只是定陶商團之一。"

  fashion_business:
    - "京師女性奢侈品旗艦店、批發端、肚兜發表會仍屬企畫；場地、預算、正式合約尚未完成。"
    - "疏影仍是人物專屬肚兜主設計候選；尚未正式簽約。"
    - "六條御息所走秀為條件式意願；成衣與活動狀態未滿足前不得寫成已確定上台。"

  li_shishi:
    - "已原諒白御行先前突兀離房事件。"
    - "已明示想要如夫人位置。"
    - "如夫人仍未完成對外公告、家冊／官籍或正式法律程序。"

  li_pinger:
    - "不是西門慶買入之奴婢。"
    - "與西門慶之最終婚姻／法律狀態仍待清理。"

  su_qing_vs_pan:
    - "蘇清 vs 潘金蓮民事／帳務案仍 ACTIVE。"
    - "五千原款與五萬索賠仍分軸；五萬不是判決。"
```

---

# 3｜WOMEN-BIZ22-E01｜定陶女性注意力事業秘密模型確立

```yaml
SECRET_BUSINESS_MODEL:
  event_id: "WOMEN-BIZ22-E01-CENTRAL_48_MODEL"
  lifecycle_state: "ACTIVE_SECRET_PROJECT"
  public_cover: "觀止擴編／新人遴選"
  true_business_visibility: "STRICTLY_LIMITED"

  leadership:
    project_head: "常煒／定陶總會副會長"
    authority_level: "總會直轄新事業"
    local_merchant_group_personnel_ownership: false

  model:
    - "不是全天下只收四十八人；每一城市／隊伍可形成一組四十八人架構。"
    - "未來可擴張為多城市、多隊伍、數百名成年女性。"
    - "每年可形成跨城競逐／總選。"
    - "前七名暫稱『神七』；前三名暫稱『御三家』。"
    - "總會選入場資格與制度；市場透過持續消費、支持、注意力與商業結果選出贏家。"
    - "高位者可取得更多資源、侍女、旅費與舞台；低位者可承擔支援性工作，但不得把排名簡化為永久人格／價值。"
    - "核心商品不是單純肉體，而是注意力、人物形象、表演、名聲、象徵聯結，以及由此帶動的實體商品消費。"
    - "古典花魁／風月訓練可與新式偶像包裝結合。"

  governance:
    - "本事業由總會直接控制，地方商團可成為客戶、合作夥伴、贊助方，但不得取得女性人員的所有權、排名權或人事控制權。"
    - "地方團隊女性之組織法位歸總會系統，不屬地方商團私產。"

  secrecy_circle_minimum:
    confirmed_knowers:
      - "白御行"
      - "常煒"
      - "顧青簡"
      - "蘇清／本晚回樓後已猜中並被納入保密圈"
    not_automatically_informed:
      - "外部牙行"
      - "一般候選女性"
      - "一般觀止客人"
      - "未因在場即自動知情之觀止人物"

  anti_leak:
    - "對外可隱藏商業戰略，但正式契約、身契、帳務與登記不得為掩護而造假。"
    - "候選人可被告知觀止擴編／風月可能性；不得因此自動知道未來四十八人與總選模型。"
```

---

# 4｜FENGLAO22-E01｜風滿樓大型遴選與兩日甄選架構

```yaml
EVENT_RECORD:
  event_id: "FENGLAO22-E01-MASS_SELECTION"
  lifecycle_state: "ACTIVE"
  event_axis_state: "CONTINUING"
  location: "觀止主廳／風滿樓擴張狀態"

  spatial_lock:
    - "風滿樓是觀止主廳進入神異擴張狀態後的形態，不是獨立建築。"
    - "一樓主要承擔候選、等候、試衣、甄選與工作區；二樓可作坐席、私室與秘密工作空間。"

  public_effect:
    - "風滿樓擴張本身吸引外界注意，已有『風滿樓開了』之類口耳議論。"
    - "外部牙行、候選人、觀止既有女性與客人共同形成即時市場反應場。"

  two_day_framework:
    tonight:
      - "重點看可立即使用、履歷／技能可核、價格可高的成年女性。"
      - "特殊價位／特殊能力者經核驗後可送白御行私下複核。"
    tomorrow:
      - "重點看可培養潛力，不保證立即成材。"
      - "白三娘主看可教性。"
      - "疏影主看台步、舞台、衣物與身體線條互動。"
      - "蘇清主看被低估／錯置的商業潛力。"
      - "顧青簡主看身分、來源、文書與知情紀錄。"
      - "潘金蓮主看價格、交易與市場性。"

  tomorrow_submission_rule:
    - "所有牙行都可送候選，不限最初兩家。"
    - "『都收都來』不等於不做篩選；候選須成年、來源可查、有實際潛力。"

  spectator_fee:
    - "明日對外看熱鬧之觀眾可收門票，以回收風滿樓運作成本。"
    - "候選人與牙行的工作進場不收觀眾票。"
    - "門票是場地收入，不是人氣投票票券。"
    - "具體票價尚未定；潘金蓮可依需求決定一般觀眾票價。"

  candidate_knowledge_tracking:
    owner: "顧青簡"
    fields:
      - "入場前已知可能涉及風月用途"
      - "入場後始知風月可能性"
    rule: "不得把後知情者偽記成原本已知。"

  high_price_review_rule:
    - "普通價位由潘金蓮處理。"
    - "超出常規價帶且具可核特殊價值者，送私下複核區。"
    - "複核至少保留牙行方與記錄／文書核驗人員。"
    - "白御行本晚指定紅娘氏陪同複核，主要負責盯牙行、維持候選完整陳述、觀察與臨場應對。"
```

---

# 5｜QANDA22-E01｜公開問答與甄選觀察準則

```yaml
SELECTION_QA:
  status: "COMPLETED_FOR_THIS_PHASE_WITH_CONTINUING_SELECTION"
  confirmed_topics:
    - "風月工作可能性與候選知情"
    - "收入與分配"
    - "暴力、言語侮辱與客人風險"
    - "年齡、疾病、月事與身體狀態"
    - "金錢、禮物、識字、客人競爭"
    - "客人聲稱贖身／承諾等話術"
    - "職業年限之外的技能、教學、管理等路徑"

  evaluation_principle:
    - "不只看候選能回答什麼，也看她是否知道自己不知道什麼、會不會提出有用問題。"
    - "現場觀眾反應可作市場測試之一，但不得單獨取代人物能力、來源、價格與可教性判斷。"
```

---

# 6｜MAID22-E01｜李師師與張麗華丫環候選狀態

```yaml
LI_SHISHI_MAID_PLAN:
  payer: "白御行"
  contract_holder_if_purchased: "李師師"
  target_count: 2
  roles:
    - "近房／懂分寸／守密型成年丫環"
    - "外跑／識字／膽子較大之成年丫環"
  current_candidate:
    - "已有一名偏近房型候選值得保留；她在碰顧青簡文書前先詢問是否可碰。"
  transaction_status: "NOT_PURCHASED_NOT_FINALIZED"

ZHANG_LIHUA_MAID_PLAN:
  payer: "白御行"
  contract_holder_if_purchased: "張麗華"
  target_count: 1
  desired_traits:
    - "成年"
    - "膽大、反應快、不怕張麗華"
    - "能處理張麗華醉酒，不愛碎念"
    - "最好具一定打架／自保能力"
  current_first_choice:
    - "一名候選先問張麗華醉後是否會吐、是否亂打人、或只打碰她的人；張麗華對此候選明顯有興趣。"
  transaction_status: "NOT_PURCHASED_NOT_FINALIZED"
```

---

# 7｜PINGER22-E01｜李瓶兒未來並列如夫人之私人談話

```yaml
PRIVATE_RELATION_EVENT:
  event_id: "PINGER22-E01-EQUAL_RIRU_PRIVATE_TALK_AND_LIGHT_KISS"
  privacy: "PRIVATE"
  participants:
    - "白御行"
    - "李瓶兒"

  confirmed_player_disclosure:
    - "白御行明示：待李瓶兒與西門慶之法律／婚姻狀態清理後，希望她若仍願意，可與李師師並列如夫人。"
    - "白御行轉述李師師的條件：兩人地位平等，不以先後排高低，不由其中一人管另一人。"
    - "白御行表示李師師願意當面與李瓶兒談，而非由白御行單方面替她作主。"

  li_pinger_response:
    - "李瓶兒對『不是先進門的壓後進門、兩邊互不管』之方向可接受。"
    - "她對如此重要之事未在前一晚先告知自己有輕微受傷／介意。"
    - "她希望之後親耳聽李師師說。"
    - "白御行提醒她：若日後李師師私下邀請，不要只因緊張便預先躲開；李瓶兒表示不會先躲，實際是否留下／做什麼仍由當時自己決定。"

  physical_event:
    - "白御行離開前對李瓶兒作輕吻。"
    - "李瓶兒未閃避，出現害羞／戲謔回應。"
    - "本段沒有進一步成人性行為。"

  does_not_establish:
    - "李瓶兒已正式成為如夫人"
    - "李師師與李瓶兒已完成三方名分會談"
    - "李瓶兒已同意任何後續三人性行為"
```

---

# 8｜SUQING22-E01｜蘇清回樓、保密圈與二十八日私約工作化

```yaml
SU_QING_ROUTE_UPDATE:
  event_id: "SUQING22-E01-RETURN_SECRET_PROJECT_AND_28DAY_WORK_SPLIT"
  status: "ACTIVE"

  return_and_interception:
    - "蘇清本晚回到觀止，在進入主廳前被引到二樓／秘密工作區。"
    - "原因是白御行／常煒判斷她很可能從今晚甄選結構推到真正女性事業模型。"
    - "蘇清實際上已猜到大方向；白御行要求她保密，她接受並加入最低保密圈。"

  civil_case_negotiation_direction:
    - "白御行曾向蘇清提出：若她不重視象徵性勝訴，可接受由許慎言探討與潘金蓮的實質和解方案。"
    - "蘇清接受『可談』，但未簽和解；具體金額與條款由許慎言／潘金蓮側談後仍須蘇清本人決定。"
    - "訴訟／索賠未因可談和解而自動撤回。"

  private_28_day_deal_update:
    - "原二十八日私人約之原始觸發條件仍未發生。"
    - "未來若進入該二十八日，現行安排改為：二十日投入秘密女性事業工作，八日履行白御行私人部分。"
    - "二十日工作由常煒統籌，不另計一般日薪；之後是否正式聘為總會人員另談。"
    - "明日潛力批次預篩先記一個『提前專案工作日』。"
    - "若原始觸發後該日可併作第一日；若觸發未發生，該提前工作日須另行結算，不得憑空消失。"

  screening_lens:
    key_question: "她現在沒有價值的地方，是真的沒有，還是從來沒人知道該怎麼賣。"
```

---

# 9｜MENSTRUAL22-E01｜草木灰月事用品標準化專案

```yaml
PROJECT:
  event_id: "MENSTRUAL22-E01-ASH_PACKET_BELT_STANDARDIZATION"
  lifecycle_state: "ACTIVE_PROJECT_DISCUSSION"
  prototype_complete: false
  mass_production_started: false

  leadership:
    product_and_women_user_side: "蘇清"
    process_supply_cost_recycling: "常煒"
    white_yuxing_role_after_assignment: "已明示細節不用事事問自己，由蘇清與常煒自行討論推進"

  core_concept:
    - "不是發明女性月事照護，而是把既有草木灰吸收法做成可標準化、可替換、可回收服務。"
    - "以固定規格布袋裝處理後之吸收材料／草木灰核心。"
    - "以 T 型／腰帶式固定結構承載可替換吸收袋。"
    - "女性可按月購買一組替換袋；使用後可丟棄，或把可回收布件送回集中處理。"
    - "集中端負責清洗可重用布件、補裝符合規格之乾淨吸收材料，再供下周期使用。"

  standardization_axes:
    - "灰源／材料來源"
    - "篩選與處理"
    - "重量"
    - "布袋尺寸"
    - "縫線"
    - "厚度"
    - "腰帶固定方式"
    - "清洗、回收、補充流程"

  product_direction:
    - "先解決便宜、乾淨、固定規格與實用性。"
    - "日後可形成基本版與更舒適／高階版，但本輪尚未定型。"
    - "蘇清需找不同身形、活動量與使用習慣的成年女性實測；男方可懂製造，但不能替女性判定舒適度。"

  anti_overclaim:
    - "本 SAVE 不把現代材料視為唯一正解，也不把未經故事內驗證之現代醫療評價倒灌為產品失敗。"
    - "本輪沒有完成歷史考據、官府醫療認證或量產安全結論。"
```

---

# 10｜SPECIAL22-E01｜特殊高價複核區收工

```yaml
SPECIAL_REVIEW:
  event_id: "SPECIAL22-E01-HIGH_VALUE_REVIEW_CLOSED"
  status: "CLOSED_FOR_TONIGHT"
  player_direction:
    - "候選先完整講自己經歷與用途；牙行不得中途替她吹價／搶答。"
    - "白御行會查牙行原始取得成本、轉手文書、持有時間與可核履歷，再議價。"
    - "紅娘氏陪同，重點是看住牙行、維持談話與觀察候選。"

  closure:
    - "白御行明示本區『就這樣，這裡收工了』。"
    - "不得自然推進出新的第六名／最後一名特殊候選。"
```

---

# 11｜SPECIAL22-P01｜白三十二娘

```yaml
PERSON_ACQUISITION:
  working_name: "白三十二娘"
  original_name: "NOT_REQUIRED_NOT_PUBLIC"
  age: 26
  buyer_and_contract_holder: "白御行"
  funding: "白御行私人"
  agreed_price_taels: 320
  asking_price_taels: 380
  known_yahang_acquisition_cost_taels: 167
  transaction_status: "COMPLETED"
  price_visibility: "STRICTLY_PRIVATE_LEDGER"

  verified_or_observed_skills:
    - "識字、兩種字體"
    - "帳目、契約、內務文書"
    - "禮數與一定音樂素養"
    - "部分舊時文書／舊語感"
    - "能估自己的可重複價值，不只靠一次性身體賣點"
    - "能把真實材料重組為可長期維持的市場人物故事"

  background_boundary:
    - "其父系舊政治牽連、舊官戶家史只屬私人來源；不得因市場包裝而對外洩漏。"
    - "她表示可做『七分真、三分假』而不易穿幫的舞台身份，但不等於真的失憶。"

  white_yuxing_directives:
    - "守密、不背叛為核心；一般錯誤可說明理由、承認、修正。"
    - "公開市場不依賴她原本姓氏／舊家世，可自行創造可持續人物故事。"
    - "目前先跟在白御行身邊，不必過度說話。"

  current_position: "白御行身邊／張麗華房內近場"
```

---

# 12｜SPECIAL22-P02｜白明礬

```yaml
PERSON_ACQUISITION:
  working_name: "白明礬"
  age: "約二十八至二十九"
  buyer_and_contract_holder: "白御行"
  funding: "白御行私人"
  agreed_price_taels: 275
  transaction_status: "COMPLETED"

  physical_trace:
    - "右手指尖留有長期染色痕跡。"
    - "左手小指尖幼年因染坊絞架事故缺損；不是刑罰。"

  skills:
    - "染色"
    - "色差辨識"
    - "布料／染料品質檢查"
    - "辨認偷工減料、摻假、過火、低價替料與耐久差異"
    - "理解某些顏色成本高但觀眾感知不值，某些低成本色反而視覺顯貴"
    - "理解布料顏色與穿著者膚色、燈光、舞台效果的互動"

  placement:
    tomorrow: "安排在蘇清旁邊，參與潛力遴選／商品與色料觀察"
    current: "白御行身邊／張麗華房內近場"

  personal_request_observed:
    - "希望持續接觸布料／色彩工作，以免眼力荒廢。"
```

---

# 13｜SPECIAL22-P03｜白紅伶

```yaml
PERSON_ACQUISITION:
  working_name: "白紅伶"
  age: "約二十四至二十五"
  buyer_and_contract_holder: "白御行"
  funding: "白御行私人"
  agreed_price_taels: 380
  known_yahang_acquisition_cost_taels: 190
  transaction_status: "COMPLETED"

  skills:
    - "聲音、口音模仿"
    - "人物語氣與角色表演訓練"
    - "可從本人真實特質出發，設計可長期維持而不易破功的舞台人物"
    - "可教新人修口音、找辨識度、學會維持客人想看的角色"

  placement:
    current: "先留後台／白御行身邊調度，不當普通前台花魁處理"
    likely_future_use: "李師師日後設席、席宴人物／聲音調教、女性事業人物塑造"
    transfer_to_li_shishi_completed: false

  secrecy:
    - "尚未因此自動知道完整秘密四十八人模型。"
```

---

# 14｜SPECIAL22-P04｜白希

```yaml
PERSON_ACQUISITION:
  working_name: "白希"
  age: "約三十四至三十五"
  buyer_and_contract_holder: "白御行"
  funding: "白御行私人"
  agreed_price_taels: 150
  known_yahang_acquisition_cost_taels: 210
  yahang_verified_prior_job_revenue_taels: 65
  transaction_status: "COMPLETED"

  skills:
    - "大型宴會／戲班後台／多人進退場安排"
    - "入口、出口、桌位、動線、燈具與人流風險"
    - "多人群像之注意力配置"
    - "判斷誰會吃掉別人的光、誰能托高別人、誰不該同時上台"
    - "曾處理數十人至約七十人之混合場務／演出人員協調"

  price_interpretation:
    - "白御行明示 150 是本次交易成交價，不是她永久人格／能力價值。"
    - "她理解技能價值取決於是否被放到正確位置；若被閒置，價格再低也可能浪費。"

  placement:
    current: "留在白御行身邊，尚未正式放入大型舞台工作"
```

---

# 15｜SPECIAL22-P05｜常煒名下物流／商路女性

```yaml
PERSON_ACQUISITION:
  working_name: "UNNAMED_BY_BAI_YUXING"
  naming_owner_for_future_scene: "常煒"
  age: "約三十"
  purchaser_cash_fronted_by: "白御行"
  contract_holder: "常煒"
  agreed_price_taels: 360
  yahang_initial_ask_taels: 460
  verified_official_auction_or_transfer_cost_taels: 240
  transaction_status: "COMPLETED_WITH_CHANG_WEI_ASSENT"

  authorization:
    - "顧青簡／書吏要求常煒本人授權後才將契記到常煒名下。"
    - "常煒回覆印記／同意，故不是白御行單方面代人持契。"
    - "白御行玩笑稱可從常煒年底分紅扣款；常煒表示與白御行私下結算，尚未形成正式扣款憑證。"

  skills:
    - "商路、貨物、採辦、車隊"
    - "四種語言，其中兩種較熟、兩種足以交易／問路／應急"
    - "帳務、採購與路線記憶"
    - "可規畫空車返程／回程運力媒合"

  business_proposal:
    - "北京—曹州—定陶等路線建立三個集貨點。"
    - "媒合有空車位的商隊與無法包整車的小貨主。"
    - "整合倉儲、裝卸、護送與部分貨運資訊。"
    - "初步估 600 兩級資本可驗證模型；三個月看路線、半年希望回本、一年正常目標約二成五至三成三。"
    - "定陶既有網路若直接提供節點，可顯著降低起始成本。"

  current_position:
    - "已送至常煒／蘇清所在二樓秘密工作區。"
    - "她的正式名字由常煒日後處理；白御行已明示不替她命名。"
```

---

# 16｜WHITE-FOUR22-E01｜白家四名新購女性之共同管理規則

```yaml
WHITE_FOUR_GROUP:
  members:
    - "白三十二娘"
    - "白明礬"
    - "白紅伶"
    - "白希"

  legal_or_route_position:
    - "四人均為白御行本晚私人出資取得之持契人員。"
    - "目前不是觀止正式掛牌花魁，也不是定陶女性事業正式四十八人名冊。"
    - "目前核心用途是把各自技能放進白御行／定陶未來事業與場面調度。"

  white_yuxing_management_statements:
    forgive_rule:
      - "白御行明示：天大的事情，只要理由能讓他接受，可以放過。"
    betrayal_rule:
      - "對洩密、告密、背叛採零容忍宣示；其原話之最重處置意象為『送去餵魚』。"
      - "此為管理／威嚇規則；本輪沒有實際處決事件。"
    tool_position:
      - "白御行明示把四人視作自己的工具／自己人；會為工具投入成本，但不承諾所有安排都按四人的偏好。"
      - "四人不得因被當自己人便自行把身份抬成合夥人或決策者。"
    advice_boundary:
      - "白御行明示：除非被問，不希望四人主動長出『替他想』的策略性建議。"
      - "四人可在各自工作內觀察、記錄、執行；未被詢問時不主動把『我覺得』升格成『主人應該』。"
    future_social_use:
      - "白御行明示：四人不是因年齡／定位被買來作普通掛牌接客者。"
      - "但未來可能被安排陪同某些有價值的男人、出席暗盤社交、席宴、交際或其他任務。"
      - "此處只記白御行之未來管理意圖；不存在任何特定成人行為已成立或已被某人同意。"

  internal_joke_name:
    label: "四大金剛"
    status: "COMEDIC_NICKNAME_NOT_FORMAL_TITLE"
```

---

# 17｜WARDROBE22-E01｜四人華服與配飾買斷

```yaml
WARDROBE_PURCHASE:
  event_id: "WARDROBE22-E01-FOUR_PRESTIGE_OUTFITS_SECONDHAND_BUYOUT"
  seller: "觀止／春梅經手舊衣庫"
  buyer: "白御行"
  funding: "白御行私人"
  item_scope:
    - "四套退下來但保存良好之高級華服"
    - "四套配套腰飾、簪、耳飾等"
  use_standard:
    - "不是丫環制服。"
    - "四人站在白御行身邊時，視覺排場應接近觀止頂級姑娘／花魁身側的標準。"
  total_price_taels: 100
  ownership: "BOUGHT_OUT_BY_BAI_YUXING"
  payment_state: "ACCOUNTS_PAYABLE_TO_GUANZHI_NOT_OBSERVED_AS_CASH_SETTLED"

  outfit_mapping:
    白三十二娘: "深絳／暗金，偏穩重、不以媚為主"
    白明礬: "青碧／冷色／煙灰外層，利用其色感與手藝氣質"
    白紅伶: "紅黑交疊、較具舞台性"
    白希: "黑底深紫、銀線節制，偏鎮場與管理者氣質"

  meta_visualization_note:
    - "對話中另產生一張四人合照作視覺參考；使用者指出圖片較偏漢服，而觀止世界服制仍以宋服為主。"
    - "該圖片只作外部視覺參考，不改寫世界服制基線。"
```

---

# 18｜FRONT22-E01｜四人盛裝前場亮相與潘金蓮反應

```yaml
PUBLIC_APPEARANCE:
  event_id: "FRONT22-E01-FOUR_WOMEN_PRESTIGE_APPEARANCE"
  status: "COMPLETED_PASS_THROUGH"
  location: "風滿樓前場"

  observed:
    - "四人換上華服後隨白御行進前場，引發部分客人停看與低聲猜測。"
    - "現場有人猜測她們是否為新花魁／新人物，但未形成正式公告。"
    - "潘金蓮得知四套舊衣連配飾合計一百兩，對白御行把四人穿出高價排場感到明顯惱火／吃虧感。"
    - "潘金蓮提出若白御行帶四人反覆在風滿樓走，京師可能傳成『白御行一夜收了四個花魁且全冠白姓』。"

  rumor_status:
    - "上述是現場預判／可能傳聞，不等於京師已普遍相信四人為花魁。"
    - "四人目前沒有因穿衣與客人猜測而取得觀止花魁身分。"
```

---

# 19｜SHISHI22-E02｜李師師被四人稱『白夫人』與實際內部調度權

```yaml
HOUSEHOLD_AUTHORITY_EVENT:
  event_id: "SHISHI22-E02-BAI_MADAM_INTERNAL_AUTHORITY"
  status: "ACTIVE_ROUTE_INTERNAL_AUTHORITY"
  parties:
    superior: "李師師"
    subordinates:
      - "白三十二娘"
      - "白明礬"
      - "白紅伶"
      - "白希"

  white_yuxing_directive:
    - "四人見李師師稱『白夫人』。"
    - "白御行明示：四人以後要聽白夫人的話；白夫人說的，在四人內部調度範圍原則上視同白御行說的。"

  authority_scope:
    - "李師師取得對四人的實際內部調度權。"
    - "可安排白家／私人範圍之工作、人員配合與日常事項。"
    - "李師師本人明示不會為了證明權力而亂改白御行已明確交代的事。"
    - "若涉及明顯超出既有用途的大事，仍可按白家實際因果處理；本輪沒有建立李師師可任意處分白御行全部財產／契約之無限權。"

  legal_and_relation_boundary:
    - "『白夫人』是白御行對自己四名持契人員建立的內部稱謂／權限。"
    - "不等於李師師已完成官籍、婚書、家冊或公開婚姻程序。"
    - "既有『想成為如夫人』狀態仍有效，法律名分仍未完成。"

  observed_four_women_response:
    - "四人均已實際以『白夫人』稱呼李師師。"
```

---

# 20｜LIHUA22-E02｜張麗華被四人稱『麗華夫人』與日常差遣權

```yaml
HOUSEHOLD_RESPECT_EVENT:
  event_id: "LIHUA22-E02-LIHUA_MADAM_DAILY_ERRAND_AUTHORITY"
  status: "ACTIVE_ROUTE_INTERNAL_PRIVILEGE"
  parties:
    honored_person: "張麗華"
    four_women:
      - "白三十二娘"
      - "白明礬"
      - "白紅伶"
      - "白希"

  title:
    required_address: "麗華夫人"
    explicitly_not: "白夫人"

  white_yuxing_directive:
    - "四人對張麗華須給足夫人級禮數與尊重。"
    - "日常小事可直接幫她，不必每件事先報備／請示白御行，否則張麗華會找白御行算帳。"
    - "大事要有分寸，不是張麗華一句話就必須完全照做。"

  daily_errand_examples_confirmed_in_dialogue:
    - "拿酒"
    - "找衣物"
    - "叫人"
    - "傳一般話"
    - "陪同／臨時幫手"

  major_matter_boundary:
    - "重大財物"
    - "白家／定陶祕密"
    - "契約處置"
    - "人事與持契安排"
    - "對外承諾"
    - "會造成明顯重大後果之事項"

  authority_interpretation:
    - "小事：四人可直接執行張麗華指示，無須回報白御行。"
    - "大事：四人應保留判斷與分寸，可暫停、確認或按白御行既有規則處理；不是完全不聽張麗華，也不是她取得白家的最終決策權。"
    - "張麗華不是四人的直屬持契人。"

  legal_and_relation_boundary:
    - "『麗華夫人』不等於張麗華因此成為白御行法律上的妻／妾／如夫人。"
    - "本稱謂是白御行授予四人使用的高位內部禮數。"

  observed_execution:
    - "張麗華當場叫白希把酒找回來；依修正後的小事規則，白希執行並把酒交給她。"
    - "四人均已實際以『麗華夫人』稱呼張麗華。"
```

---

# 21｜ACCOUNTING22｜本輪新增私人交易與持契表

```yaml
PRIVATE_ACQUISITION_LEDGER:
  白三十二娘:
    contract_holder: "白御行"
    amount_taels: 320
    payment_source: "白御行私人"
    state: "COMPLETED"
    confidentiality: "STRICT_PRIVATE_PRICE"

  白明礬:
    contract_holder: "白御行"
    amount_taels: 275
    payment_source: "白御行私人"
    state: "COMPLETED"

  白紅伶:
    contract_holder: "白御行"
    amount_taels: 380
    payment_source: "白御行私人"
    state: "COMPLETED"

  白希:
    contract_holder: "白御行"
    amount_taels: 150
    payment_source: "白御行私人"
    state: "COMPLETED"

  four_women_total_purchase_price_taels: 1125

  chang_wei_logistics_woman:
    contract_holder: "常煒"
    amount_taels: 360
    cash_fronted_by: "白御行"
    state: "COMPLETED_WITH_CHANG_ASSENT"
    reimbursement_or_dividend_offset: "UNSETTLED_PRIVATE_BETWEEN_BAI_AND_CHANG"

  four_women_wardrobe:
    owner: "白御行"
    amount_taels: 100
    state: "BOUGHT_OUT_ACCOUNTS_PAYABLE_NOT_OBSERVED_PAID"

  accounting_separation:
    - "白御行四名持契人購價與常煒名下女子不得混成同一持契資產。"
    - "衣物一百兩是另筆觀止二手衣／配飾買斷，不包含在人身契價內。"
```

---

# 22｜秘密、知情與禁止外洩矩陣

```yaml
KNOWLEDGE_AND_SECRECY:
  central_48_model:
    classification: "SECRET_STRATEGY"
    minimum_known:
      - "白御行"
      - "常煒"
      - "顧青簡"
      - "蘇清"
    not_public: true

  special_purchase_prices:
    classification: "PRIVATE_LEDGER"
    白三十二娘_320:
      explicit_no_leak: true
      white_warning_to_yahang: "若外洩，牙行將失去在京師與白御行／定陶繼續做生意的資格與空間。"
    other_prices:
      public_by_default: false

  白三十二娘_original_family_background:
    classification: "PRIVATE_BACKGROUND"
    public_use: "NOT_ALLOWED_WITHOUT_CAUSAL_AUTHORIZATION"

  chang_wei_woman_name:
    state: "UNSET"
    naming_authority_for_future: "常煒"
    forbidden: "導演不得替白御行擅自命名"

  betrayal_policy:
    white_statement: "洩密、告密、背叛屬白御行最不可接受類型。"
    execution_status: "NO_PUNISHMENT_EVENT_OCCURRED"
```

---

# 23｜未決事項

```yaml
OPEN_ITEMS:
  tonight_selection:
    - "一般價位候選今晚最終成交總表尚未形成。"
    - "特殊高價區已關閉，但主廳遴選仍可自然收尾。"

  tomorrow_mass_selection:
    - "觀眾票價未定。"
    - "各牙行送件數未定。"
    - "白三娘、疏影、蘇清、顧青簡、潘金蓮之完整評分／分工表可在明日場景形成。"

  maids:
    - "李師師兩名丫環尚未成交。"
    - "張麗華一名丫環尚未成交。"

  womens_business:
    - "城市隊伍、第一批正式名冊、排名機制、贊助規則、收入分配、退出／轉崗規則尚未正式落文。"
    - "秘密模型不得因候選入場自動公開。"

  menstrual_product:
    - "尚未完成實物樣品、女性試用、定價、回收點、清洗 SOP、包材與供應鏈定稿。"

  four_women:
    - "白三十二娘正式對外人物故事未定稿。"
    - "白明礬明日與蘇清並列工作尚未實際開始。"
    - "白紅伶仍未正式交李師師使用／調教班底。"
    - "白希仍未被正式釋放到大型排場／舞台調度工作。"
    - "『四大金剛』只屬玩笑，不是正式職稱。"

  household_titles:
    - "李師師『白夫人』為四名持契人之內部稱呼與調度權，不等於法律婚姻程序完成。"
    - "張麗華『麗華夫人』為內部高位禮數＋小事差遣權，不等於白夫人或法律妻妾。"

  li_pinger:
    - "與李師師當面談平等如夫人仍未發生。"
    - "與西門慶之婚姻／法律狀態仍待清理。"

  su_qing:
    - "與潘金蓮和解只可談，未簽。"
    - "二十八日原始觸發尚未發生。"
```

---

# 24｜直接接關摘要

```yaml
DIRECT_RESUME:
  story_time: "理火三年槐月二十二日夜"
  location: "張麗華房內／門口"

  immediate_state:
    - "白御行剛完成讓四人認李師師為『白夫人』、認張麗華為『麗華夫人』之內部規則。"
    - "白希已按張麗華日常小事差遣，替她找回酒。"
    - "白御行向張麗華告別，準備帶白三十二娘、白明礬、白紅伶、白希離開。"
    - "紅娘氏同行近門口。"
    - "風滿樓前堂仍有今晚大型遴選之餘波與工作。"

  do_not_auto_resolve:
    - "不得替白御行決定下一站。"
    - "不得替白御行自動支付一百兩衣物款；目前記為應付。"
    - "不得自動把四人登記成觀止花魁、四十八人正式成員或人物卡池常設人物。"
    - "不得自動讓李師師法律上成婚或讓張麗華成為白夫人。"
    - "不得自動跳到翌日甄選。"
```

---

# 25｜HOT V3.0 結論

> **最新直接接關：槐月二十二日夜，張麗華房內告別之後。**
>
> **特殊高價複核已收工；風滿樓主廳仍活。**
>
> **白御行私人持契新四人：白三十二娘、白明礬、白紅伶、白希。**
>
> **常煒另持一名未命名物流／商路女性之契；名字由常煒日後處理。**
>
> **四人已建立雙層內部權限：李師師＝白夫人／實際調度權；張麗華＝麗華夫人／高位禮數＋日常小事差遣權。**
>
> **本檔只更新 HOT，不更新 MASTER，不修改人物卡池。**
