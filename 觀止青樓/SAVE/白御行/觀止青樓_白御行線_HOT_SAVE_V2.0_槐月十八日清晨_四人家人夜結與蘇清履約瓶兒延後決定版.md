# 觀止青樓｜白御行線 HOT SAVE V2.0
## 理火三年槐月十八日清晨｜四人家人夜結 × 蘇清履約進度 × 李瓶兒關係與生育延後決定版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V2_0_HUAI18_DAWN_FOUR_PERSON_NIGHT_CLOSED"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V2.0"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime:
    - "GUANZHI_QINGLOU_V10_0"
    - "GUANZHI_QINGLOU_V10_1_PATCH_WHEN_APPLICABLE"
  story_date: "理火三年槐月十八日清晨"
  previous_scene_range: "槐月十七日晚至十八日清晨"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "NIGHT_CLOSED; NEXT_SCENE_READY_AT_MORNING"
  save_scope:
    - "張麗華房內四人成人事件已結束"
    - "白御行與張麗華之當夜性事件"
    - "白御行與蘇清之履約性事件及停止規則"
    - "李瓶兒之有限親密、未性交與明日再來承諾"
    - "孩子、關係、排他與位置問題延後至兩日結束後決定"
    - "張麗華對多人共處之喜歡與吃味並存"
    - "四人共同就寢，下一接點為槐月十八日清晨"
```

---

# 0｜來源法位與提交說明

```yaml
SOURCE_LINEAGE:
  previous_valid_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V1.9_槐月十七日晚_四人家宴與瓶兒留宿接關版.md"
    role: "本檔直接前置 HOT 來源"

  inherited_long_term_source:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版.md"
    role: "長期因果、舊契約與玩家線早期事件來源"

  persona_source:
    file: "觀止人物卡_LCAPG_V1.1-R1_原始重構去污染版_含辭歲_導演隱藏區增補.md"
    role: "人物基線來源；不得被本夜玩家線事件倒灌改寫"

  forbidden_source:
    file: "HOT_SAVE_V1.3"
    status: "ILLEGAL_CORRUPTED_SAVE"
    use: "AUDIT_ONLY"

COMMIT_NOTE:
  - "本檔取代 V1.9，成為白御行線當前 HOT 接關切片。"
  - "本檔不更新 MASTER，不修改人物卡或人物池。"
  - "只記錄本夜已發生、可觀察、人物明示或玩家對自身言行之有效確認。"
  - "成人事件、感情、契約、同意、射精、生育與公開身分分軸記錄。"
  - "原作李瓶兒喪子資料只作人物基線參照，不作本線新事件；本檔只保存李瓶兒於本夜親口表達的孩子立場。"
  - "『六系』分類、戰力比較、犬貓稱呼與床上競賽語句屬當夜玩笑或情境話術，不升格為人物固定屬性。"
```

---

# 1｜當前時間、位置與人物

```yaml
TIME_RECORD:
  record_id: "TIME-HUAI18-DAWN-001"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  era: "理火三年"
  calendar_date: "槐月十八日"
  day_or_night_index: "槐月十七日晚之次晨"
  time_of_day: "清晨／夜間場景已結束"
  scene_sequence: "四人家宴後成人事件與共眠結束"
  certainty: "CONFIRMED_RANGE"
  source_event_ids:
    - "NIGHT17-E01"
    - "NIGHT17-E09"

CURRENT_SCENE:
  location: "觀止青樓／張麗華房間"
  scene_state: "FOUR_PERSON_NIGHT_CLOSED; MORNING_NOT_YET_PLAYED"
  present_at_night_close:
    - "白御行"
    - "張麗華"
    - "蘇清"
    - "李瓶兒"
  next_action_owner: "WORLD_AT_HUAI18_MORNING_OR_PLAYER"

SLEEPING_CLOSE_STATE:
  confirmed:
    - "四人留在張麗華房內共同就寢。"
    - "白御行最後由張麗華抱在身側。"
    - "蘇清與李瓶兒同在床上或緊鄰床位，由薄被一同覆住。"
    - "本夜不再發生後續性事件。"
  exact_waking_order: "UNKNOWN"
  exact_morning_positions: "NOT_YET_PLAYED"
```

---

# 2｜本夜事件總覽

## NIGHT17-E01｜房內成人語言與臨時共處規則

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E01"
  time: "槐月十七日晚，家宴後"
  location: "張麗華房間"
  status: "COMPLETED_FOR_NIGHT"
  participants:
    - "白御行"
    - "張麗華"
    - "蘇清"
    - "李瓶兒"

CONFIRMED_FRAME:
  - "四人同意在房內以直接、成人、可粗俗的方式談慾望與身體。"
  - "當夜說出的粗俗或羞恥話不得在事後被拿來羞辱當事人。"
  - "說出慾望不等於性同意；每一具體行動仍須由當事人決定。"
  - "房內『家人』框架仍是兩日內的臨時相處方式，不是永久家族或名分。"

NOT_CANONICAL_BANTER:
  - "白御行提出『巨、仙、可、美、蘿、氣』六系與若干身體分類。"
  - "蘇清、張麗華、李瓶兒就分類互相調笑。"
  - "該分類沒有被正式寫入人物卡、人物池或世界制度。"
```

## NIGHT17-E02｜蘇清收下「對對」來信

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E02"
  status: "COMPLETED_PRIVATE_OBJECT_TRANSFER"
  object: "一封署名『對對，一名不肯把愛慕寫成客觀結論的愛慕者』之信"
  recipient: "蘇清"
  observable_result:
    - "信中稱讚蘇清，並表示在觀止美人形象中選擇她。"
    - "蘇清閱讀後喜歡該信並將信留下。"
  source_boundary:
    - "信件署名與自稱身分只保存為信中主張。"
    - "不得把『真正設計總長理火AI』之自稱固化為客觀世界身分。"
  knowledge_scope:
    - "白御行"
    - "張麗華"
    - "蘇清"
    - "李瓶兒"
```

## NIGHT17-E03｜白御行與張麗華之性事件

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E03"
  time: "槐月十七日晚"
  status: "COMPLETED"
  participants:
    - "白御行"
    - "張麗華"
  event_class: "CONSENSUAL_ADULT_SEXUAL_EVENT"

OBSERVABLE_HARD_STATE:
  - "白御行與張麗華發生自願的性交與其他親密接觸。"
  - "張麗華於事件中多次主動引導節奏與姿勢。"
  - "事件後張麗華休息，仍留在房內參與後續四人共處。"

EJACULATION_STATE:
  internal_ejaculation_confirmed: false
  external_ejaculation_confirmed: false
  exact_outcome: "UNKNOWN_NOT_EXPLICITLY_RECORDED"

RELATION_EFFECT:
  - "不新增婚姻、排他、永久身體資格或公開名分。"
  - "張麗華仍保有房間、床位與自身身體決定權。"
```

## NIGHT17-E04｜李瓶兒與蘇清之相互親密

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E04"
  status: "COMPLETED_WITH_LIMITS"
  participants:
    - "李瓶兒"
    - "蘇清"
  event_class: "CONSENSUAL_KISSING_HOLDING_AND_LIMITED_TOUCH"

CONFIRMED:
  - "李瓶兒與蘇清互相擁抱、親吻並有有限身體接觸。"
  - "李瓶兒在每一步保留是否繼續之決定。"
  - "該事件不建立兩人戀愛、排他或永久性關係。"
```

## NIGHT17-E05｜李瓶兒對白御行之有限性探索

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E05"
  status: "COMPLETED_WITH_EXPLICIT_LIMITS"
  participants:
    - "白御行"
    - "李瓶兒"
  event_class: "CONSENSUAL_MANUAL_AND_ORAL_EXPLORATION"

CONFIRMED_ACTIONS:
  - "李瓶兒自願以手觸碰與握住白御行性器。"
  - "李瓶兒自願嘗試口部親密接觸。"
  - "李瓶兒觀察蘇清的口部親密方式，但不承諾照抄或形成職業義務。"

EXPLICIT_LIMITS:
  - "李瓶兒未同意性交。"
  - "李瓶兒未同意當夜受孕或體內射精。"
  - "李瓶兒明示第一次不想在口中承接射精，也不想吞嚥。"
  - "白御行不得按壓她的頭、抓住她的手強行教導或催促進度。"
  - "是否繼續由李瓶兒自己決定。"

OUTCOME:
  penetration: false
  semen_received_in_mouth: false
  pregnancy: "NOT_ESTABLISHED"
  injury: "NONE_REPORTED"
```

## NIGHT17-E06｜蘇清與白御行之性交、決鬥框架與重新立約

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E06"
  time: "槐月十七日晚"
  status: "COMPLETED"
  participants:
    - "白御行"
    - "蘇清"
  event_class: "CONSENSUAL_ADULT_INTERCOURSE_WITH_RENEGOTIATED_RULES"

INITIAL_CONDITIONS:
  - "蘇清同意性交，但明示不接受體內射精。"
  - "白御行承諾在接近射精時提供明確訊號，曾以『五秒』描述可提前告知之時間。"
  - "蘇清保留自行離開與喊停之權利。"

CONSENT_RENEGOTIATION:
  trigger:
    - "白御行曾提出由自己完全掌控節奏，並表示決鬥中蘇清說了不算。"
  response:
    - "蘇清立即截停，明示換姿勢不等於交出停止權。"
    - "張麗華協助暫停並分開兩人。"
  re_agreed_terms:
    - "白御行可掌握該段節奏。"
    - "任何一方說停，事件立即停止。"
    - "白御行接近射精時必須明示。"
    - "不得體內射精。"
  result:
    - "白御行明示接受上述規則後，性交才重新開始。"

LATER_EVENT_STATE:
  - "蘇清由競賽勝負框架轉為明示以自身享受為目的繼續。"
  - "蘇清自述『很爽』，並明示不需再以勝負判定當下。"
  - "最後一段以一百次計數為結束條件；最後十次改為逐次、較慢完成。"
  - "第一百次完成後蘇清明示『停』。"
  - "白御行依約停止，沒有再增加下一次。"

EJACULATION_STATE:
  internal_ejaculation_confirmed: false
  external_ejaculation_confirmed: false
  exact_outcome: "NO_EJACULATION_REPORTED_OR_OBSERVED"
  contraception_tool_recorded: false
  pregnancy: "NOT_ESTABLISHED"

PHYSICAL_OUTCOME:
  su_qing:
    - "事件後明顯疲累、呼吸尚未平復。"
    - "無受傷報告。"
  bai_yuxing:
    - "事件後自述疲累，當晚無力再與李瓶兒進行性交。"
    - "無受傷報告。"
```

## NIGHT17-E07｜張麗華於後續多人事件中的位置

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E07"
  status: "COMPLETED_FOR_NIGHT"
  participant: "張麗華"

CONFIRMED_ACTIONS:
  - "張麗華多次從後方抱住白御行，與他共同觀看蘇清、李瓶兒的親密互動。"
  - "張麗華在蘇清性交事件中協助穩住床位與身體位置。"
  - "蘇清中止並重談規則時，張麗華支持暫停與重新確認。"
  - "張麗華未替蘇清或李瓶兒作出性同意。"
```

## NIGHT17-E08｜本夜射精、生育與懷孕決定

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E08"
  status: "CLOSED_FOR_NIGHT"

PLAYER_DECLARATIONS:
  - "白御行表示今晚不在任何女人體內射精。"
  - "白御行表示若李瓶兒未來懷孕，他不會要求她打掉，並會要這個孩子。"

OBSERVED_RESULT:
  - "本夜沒有任何體內射精被確認。"
  - "本夜沒有懷孕事件成立。"
  - "李瓶兒拒絕將當夜親密直接推進為受孕嘗試。"

LI_PINGER_POSITION:
  - "孩子對李瓶兒非常重要。"
  - "她不接受因蘇清不願體內射精，便把受孕可能順勢交給她。"
  - "她要求先釐清孩子母親的位置、公開稱呼、姓氏、居所、養育與保護責任。"
  - "她要求白御行回答要的是孩子，還是她與孩子。"
  - "她將是否與白御行生孩子延後至兩日結束後再談。"

LEGAL_STATE:
  consent_to_insemination: "REJECTED_FOR_THIS_NIGHT"
  future_child_discussion: "ACTIVE_DEFERRED_TOPIC"
  pregnancy_status: "NOT_ESTABLISHED"
  parenthood_commitment_status: "PLAYER_INTENT_STATED; NO_JOINT_AGREEMENT"
```

## NIGHT17-E09｜夜間收束與共同就寢

```yaml
EVENT_RECORD:
  event_id: "NIGHT17-E09"
  time: "槐月十八日清晨前"
  status: "COMPLETED"

CONFIRMED:
  - "白御行告知李瓶兒自己已疲累，當晚不再與她性交。"
  - "李瓶兒表示無須因未與她性交而道歉；她留下不是等待排到自己。"
  - "李瓶兒表示槐月十八日仍會再來，原因是想再見白御行。"
  - "她未承諾槐月十八日一定發生性行為。"
  - "四人以薄被覆身，共同在張麗華房內就寢。"
  - "張麗華取得白御行當夜最後抱睡的位置。"
  - "白御行以『小狼狗／貓／狼叫』與張麗華玩笑互動；該稱呼只屬當夜情境。"
```

---

# 3｜同意矩陣

```yaml
CONSENT_RECORDS:

  - consent_id: "CONSENT-H17-ZLH-BYX-SEX-001"
    actor: "張麗華"
    target_actor: "白御行"
    action_scope: "當夜性交與親密接觸"
    time_scope: "槐月十七日晚"
    status: "EXPLICITLY_ACCEPTED_AND_COMPLETED"
    conditions:
      - "張麗華保有主動、停止與房間管理權"
    effective_until: "NIGHT_CLOSED"
    source_event_ids:
      - "NIGHT17-E03"

  - consent_id: "CONSENT-H17-SQ-BYX-INTERCOURSE-001"
    actor: "蘇清"
    target_actor: "白御行"
    action_scope: "當夜性交"
    time_scope: "槐月十七日晚"
    status: "CONDITIONALLY_ACCEPTED_AND_COMPLETED"
    conditions:
      - "不接受體內射精"
      - "白御行接近射精時須明示"
      - "蘇清說停即停"
      - "白御行可掌握後段節奏，但不得取消蘇清停止權"
    effective_until: "NIGHT_CLOSED"
    source_event_ids:
      - "NIGHT17-E06"

  - consent_id: "CONSENT-H17-LP-BYX-MANUAL_ORAL-001"
    actor: "李瓶兒"
    target_actor: "白御行"
    action_scope: "手部與口部有限性探索"
    time_scope: "槐月十七日晚"
    status: "CONDITIONALLY_ACCEPTED_AND_COMPLETED"
    conditions:
      - "由李瓶兒自行靠近與決定節奏"
      - "不按頭、不抓手強教、不催促"
      - "不在口中射精、不要求吞嚥"
    effective_until: "NIGHT_CLOSED"
    source_event_ids:
      - "NIGHT17-E05"

  - consent_id: "CONSENT-H17-LP-BYX-INTERCOURSE-001"
    actor: "李瓶兒"
    target_actor: "白御行"
    action_scope: "性交"
    time_scope: "槐月十七日晚"
    status: "REJECTED_FOR_THIS_NIGHT"
    conditions: []
    effective_until: "NIGHT_CLOSED"
    source_event_ids:
      - "NIGHT17-E05"
      - "NIGHT17-E08"

  - consent_id: "CONSENT-H17-LP-BYX-INSEMINATION-001"
    actor: "李瓶兒"
    target_actor: "白御行"
    action_scope: "體內射精／受孕嘗試"
    time_scope: "槐月十七日晚"
    status: "REJECTED_FOR_THIS_NIGHT"
    conditions:
      - "未來須先談清關係、母子位置與長期責任"
    effective_until: "NIGHT_CLOSED"
    source_event_ids:
      - "NIGHT17-E08"

  - consent_id: "CONSENT-H17-LP-SQ-INTIMACY-001"
    actor: "李瓶兒"
    target_actor: "蘇清"
    action_scope: "擁抱、親吻與有限觸碰"
    time_scope: "槐月十七日晚"
    status: "EXPLICITLY_ACCEPTED_AND_COMPLETED"
    conditions:
      - "李瓶兒可逐步決定是否繼續"
    effective_until: "NIGHT_CLOSED"
    source_event_ids:
      - "NIGHT17-E04"
```

---

# 4｜契約、帳目與履約狀態

## CONTRACT-H17-SQ-02DAY｜蘇清兩日共同生活結算安排

```yaml
CONTRACT_STATE:
  contract_id: "CONTRACT-H17-SUQING-2DAY-HOUSEHOLD-001"
  state_class: "ACTIVE"
  state_label: "FINAL_DAY_REMAINS; SEXUAL_COMPONENT_COMPLETED"
  parties:
    - "白御行"
    - "蘇清"
  linked_participant:
    - "張麗華，作為兩日共同生活與三人事件之一員，但非舊五百兩債務債務人"
  duration_anchor: "槐月十七日午間至槐月十九日黎明"
  purpose:
    - "以兩日共同吃住生活與約定範圍之親密事件，處理舊五百兩／三夜未結帳"
  completed_components:
    - "槐月十七日共同生活與四人家宴"
    - "白御行、張麗華、蘇清共同參與之三人成人事件要件已於本夜發生"
    - "蘇清與白御行完成當夜性交"
  remaining_components:
    - "槐月十八日最後一日之共同生活"
    - "至約定結束時間之完整履行"
  current_ledger: "UNSETTLED_PENDING_FINAL_DAY"
  old_contract_link:
    amount: "五百兩"
    original_duration: "三晚"
    original_status: "UNSETTLED"
  no_automatic_effect:
    - "本夜性交不自動建立愛情"
    - "本夜性交不自動免除未完成之最後一日"
    - "李瓶兒不是此契約當事人"
```

## CONTRACT-H17-ZLH-COMPANIONSHIP｜張麗華陪伴線

```yaml
CONTRACT_STATE:
  contract_id: "RELATIONAL_PROMISE-ZLH-THREE_DAY-COMPANIONSHIP"
  state_class: "ACTIVE"
  state_label: "MULTI_PERSON_NIGHT_ACCEPTED_ONCE; EXCLUSIVITY_NOT_ESTABLISHED"
  confirmed:
    - "張麗華原有三日陪伴承諾仍在。"
    - "她接受本夜四人共處與成人事件。"
    - "她不接受由此推定往後每一晚都必須多人同床。"
    - "下一次若再安排多人同床或多人性事件，她要求白御行先問她是否願意。"
```

---

# 5｜關係硬狀態

## REL-BYX-ZLH｜白御行 × 張麗華

```yaml
RELATIONSHIP_STATE:
  relation_id: "REL-BYX-ZLH-HOT-V2"
  actor_a: "白御行"
  actor_b: "張麗華"
  state_class: "ACTIVE"
  state_label: "INTIMATE_COMPANIONSHIP_WITH_REAL_JEALOUSY_AND_ROOM_AUTHORITY"
  established_roles:
    - "當前親密伴侶／陪伴線核心人物"
    - "張麗華房間與床位管理者"
  confirmed_events:
    - "本夜完成性交"
    - "張麗華接受四人共處"
    - "張麗華最後抱白御行入睡"
  effective_refusals:
    - "多人共處不得被自動延長為每夜固定制度"
    - "不得故意利用其他女人刺激她吃醋以取得床上反應"
  unresolved_axes:
    - "正式名分"
    - "排他程度"
    - "長期多重關係邊界"
    - "三日陪伴結束後關係形狀"
  romance_status: "ACTIVE_AFFECTION_NOT_FORMALLY_NAMED_AS_MARRIAGE"
  exclusivity_status: "NOT_ESTABLISHED"
  physical_contact_status: "CONSENSUAL_SEX_OCCURRED_THIS_NIGHT"
  last_delta_event_id: "NIGHT17-E09"
```

### 張麗華本夜明示立場

```yaml
ZHANG_LIHUA_POSITION:
  - "她喜歡本夜的變化。"
  - "她也確實吃味，兩者同時成立。"
  - "她喜歡看蘇清放下分析、李瓶兒自己靠近，也喜歡四人真正共同在場。"
  - "她不願被固定為替白御行安排其他女人、永遠懂事或永遠大度的位置。"
  - "她希望白御行下次在多人事件前先詢問她，而不是事後讚美她大方。"
  - "她承認會自然護食、搶目光與抱睡位置，但拒絕被刻意操弄嫉妒。"
```

## REL-BYX-SQ｜白御行 × 蘇清

```yaml
RELATIONSHIP_STATE:
  relation_id: "REL-BYX-SQ-HOT-V2"
  actor_a: "白御行"
  actor_b: "蘇清"
  state_class: "ACTIVE"
  state_label: "CONTRACTUAL_SEX_COMPLETED_ONCE; ROMANCE_EXPLICITLY_NOT_ESTABLISHED"
  established_roles:
    - "舊五百兩三夜未結帳之重議履約雙方"
    - "兩日共同生活安排參與者"
  confirmed_events:
    - "本夜完成性交"
    - "停止權曾被爭議，後重新立約並實際遵守"
    - "蘇清明示本夜確實很爽"
    - "白御行稱讚蘇清肉體『很夠力、很爽』"
  effective_refusals:
    - "蘇清不接受體內射精"
    - "蘇清不接受停止權因『決鬥』而失效"
    - "蘇清不接受本夜性交被自動改寫成愛情"
  active_offers:
    - "兩日安排結束後，若蘇清未來想談愛，可另行提出；目前沒有承諾"
  unresolved_axes:
    - "最後一日履約結果"
    - "五百兩舊帳正式結清"
    - "契約後是否維持肉體、朋友、合作或感情關係"
  romance_status: "NOT_ESTABLISHED"
  exclusivity_status: "NONE"
  physical_contact_status: "CONSENSUAL_INTERCOURSE_OCCURRED_THIS_NIGHT"
  contract_links:
    - "CONTRACT-H17-SUQING-2DAY-HOUSEHOLD-001"
  last_delta_event_id: "NIGHT17-E06"
```

### 白御行與蘇清之感情聲明

```yaml
Bai_Yuxing_DECLARATION_TO_SU_QING:
  - "本夜是履約，不是愛情。"
  - "白御行明示自己現在不愛蘇清，也沒有愛上她。"
  - "他承認蘇清的身體令他感到很爽、很夠力。"
  - "他表示若蘇清有一天想愛他，可在兩日安排結束後再談。"

SU_QING_RESPONSE:
  - "接受本夜先按履約與肉體事實記錄，不把床上事件冒充感情。"
  - "她可能日後想談愛，也可能只結帳離開，目前未決。"
  - "她若想愛會自己開口；白御行可接受或拒絕。"
  - "蘇清口誤說成白御行欠她一日，後已自行更正：舊帳法位上是蘇清欠白御行，槐月十八日為最後履約日。"
```

## REL-BYX-LP｜白御行 × 李瓶兒

```yaml
RELATIONSHIP_STATE:
  relation_id: "REL-BYX-LP-HOT-V2"
  actor_a: "白御行"
  actor_b: "李瓶兒"
  state_class: "UNDECIDED"
  state_label: "MUTUAL_AFFECTION_EMERGING; BODY_LIMITS_RESPECTED; RELATIONSHIP_DEFERRED"
  established_roles:
    - "當夜親密接觸雙方"
    - "彼此有明示感情可能，但未定名分"
  confirmed_events:
    - "李瓶兒接受有限手部與口部性探索"
    - "李瓶兒拒絕當夜性交與受孕"
    - "白御行明示對李瓶兒有真感情"
    - "李瓶兒表示聽見後很高興，且不只把白御行當成想碰她的男人"
    - "李瓶兒表示槐月十八日會再來，因為還想見白御行"
  effective_refusals:
    - "本夜不性交"
    - "本夜不體內射精或受孕"
    - "不因白御行疲累而把明晚變成補交性義務"
    - "不接受先有孩子、再決定母親位置"
  active_offers:
    - "槐月十八日再見"
    - "兩日結束後討論是否成為白御行的女人、關係形狀與生育問題"
  unresolved_axes:
    - "李瓶兒對白御行之感情程度"
    - "是否成為正式伴侶"
    - "是否排他"
    - "是否允許蘇清、張麗華與她有親密接觸"
    - "是否與白御行共同生育"
    - "若生育，母子公開位置、姓氏、居所、養育與保護責任"
  romance_status: "EMERGING_BUT_NOT_CONFIRMED_AS_COMMITTED_RELATIONSHIP"
  exclusivity_status: "UNDECIDED"
  physical_contact_status: "LIMITED_CONSENSUAL_SEXUAL_CONTACT; NO_INTERCOURSE"
  last_delta_event_id: "NIGHT17-E09"
```

## REL-ZLH-SQ-LP｜三女房內關係

```yaml
GROUP_RELATIONSHIP_STATE:
  group_id: "GROUP-ZLH-SQ-LP-HUAI17-NIGHT"
  state_class: "ACTIVE_TEMPORARY"
  state_label: "SHARED_ROOM_AND_INTIMACY_WITHOUT_PERMANENT_HIERARCHY"
  confirmed:
    - "三女在張麗華房內共同參與本夜成人事件與共眠。"
    - "蘇清與李瓶兒有相互親密接觸。"
    - "張麗華接受兩人留宿並參與本夜，但保留自己的房間與下一次安排決定權。"
  not_established:
    - "三女彼此戀愛"
    - "固定妻妾或大小順位"
    - "永久共享白御行"
    - "任一人可替另一人同意性行為"
```

---

# 6｜玩家硬狀態

```yaml
PLAYER_HARD_STATE:
  player_id: "白御行"
  public_identity: "白總／白御行"
  current_location: "張麗華房間"
  current_condition:
    - "槐月十七日晚經歷多段親密與性交後疲累。"
    - "本夜未再與李瓶兒性交。"
    - "無受傷報告。"
  explicitly_declared_positions:
    - "對張麗華仍有明確親密與偏愛，並喜歡她吃味與護食的樣子。"
    - "對蘇清明示目前無愛情，將本夜定位為履約，但承認肉體享受。"
    - "對李瓶兒明示有真感情。"
    - "表示若李瓶兒未來懷孕，會要孩子且不要求打掉；此為玩家意向，尚未形成共同生育承諾。"
    - "表示本夜不在任何女人體內射精。"
  visible_behavior_patterns_this_night:
    - "以挑釁、比較與競賽語言刺激蘇清。"
    - "在蘇清中止後接受重新確認之停止規則。"
    - "依約在蘇清第一百次後明示停止時停止。"
    - "對李瓶兒採取撫髮、撫臉、擁抱與等待她自行決定之互動。"
  next_action_owner: "PLAYER_AT_MORNING"
  forbidden_ai_fill:
    - "不得替白御行決定槐月十八日醒來後先對誰說話。"
    - "不得替白御行提前回答李瓶兒的關係、生育與母子位置問題。"
    - "不得替白御行把對蘇清的無愛聲明永久化為永不可能改變。"
```

---

# 7｜知情範圍

```yaml
KNOWLEDGE_SCOPE:

  four_person_night_details:
    know:
      - "白御行"
      - "張麗華"
      - "蘇清"
      - "李瓶兒"
    public_state: "PRIVATE_NOT_PUBLIC"
    leak_status: "NO_LEAK_ESTABLISHED"

  bai_feelings_for_li_pinger:
    know:
      - "白御行"
      - "張麗華"
      - "蘇清"
      - "李瓶兒"
    public_state: "PRIVATE_ROOM_DECLARATION"

  bai_no_love_statement_to_su_qing:
    know:
      - "白御行"
      - "張麗華"
      - "蘇清"
      - "李瓶兒"
    public_state: "PRIVATE_ROOM_DECLARATION"

  child_discussion:
    know:
      - "白御行"
      - "張麗華"
      - "蘇清"
      - "李瓶兒"
    public_state: "PRIVATE_NOT_PUBLIC"

  su_qing_letter:
    know:
      - "白御行"
      - "張麗華"
      - "蘇清"
      - "李瓶兒"
    current_holder: "蘇清"
    public_state: "PRIVATE"
```

---

# 8｜繼承中的活躍長線

```yaml
INHERITED_ACTIVE_THREADS:

  zhang_lihua_winery:
    status: "ACTIVE_HANDOVER"
    pending:
      - "花農欠款確數"
      - "年度週轉方案"
      - "一萬兩銀子之正式法位"
      - "師爺後續交接回報"

  zhang_lihua_companionship:
    status: "ACTIVE"
    note:
      - "本夜多人事件不取消白御行原先對張麗華的陪伴承諾。"
      - "槐月十八日仍須處理陪伴、酒莊與多人關係邊界。"

  su_qing_two_day_household_arrangement:
    status: "ACTIVE_FINAL_DAY"
    final_day: "槐月十八日"
    expected_end: "槐月十九日黎明"
    sexual_component: "COMPLETED"
    full_settlement: "NOT_YET"

  su_qing_twenty_eight_day_future_price:
    status: "DISCUSSION_ONLY_NOT_ACCEPTED"
    note:
      - "不得因本夜性交而自動成立。"

  li_pinger_relationship_and_child:
    status: "ACTIVE_DEFERRED_DECISION"
    review_time: "兩日安排結束後"
    questions:
      - "是否成為白御行的女人"
      - "關係是否排他"
      - "白御行給她什麼位置"
      - "是否共同生育"
      - "若有孩子，母子之公開與實際保障"

  ximen_qing_gray_ledger_thread:
    status: "PLAN_NOT_DESIGNED"
    note:
      - "本夜未新增案件事實。"

  white_jade_pool:
    status: "INHERITED_SEALED_OR_RESTRICTED"
    note:
      - "本夜未新增白玉池事件；不得視為已解決。"

  merchant_association_case:
    status: "INHERITED_ACTIVE_UNDER_DELEGATED_HANDLING"
    note:
      - "本夜未新增案件結果。"
```

---

# 9｜禁止推斷

```yaml
FORBIDDEN_INFERENCE:
  - "不得把四人同床一夜改寫成永久四人伴侶、婚姻或固定群體性關係。"
  - "不得把張麗華接受本夜改寫成她往後必須接受每一次多人事件。"
  - "不得把張麗華吃味改寫成她同意白御行故意刺激或操弄她。"
  - "不得把蘇清本夜性交與『很爽』改寫成她愛上白御行。"
  - "不得把白御行稱讚蘇清肉體改寫成愛情承諾。"
  - "不得把蘇清一度失去從容改寫成她失去停止權、人格或分析能力。"
  - "不得把『決鬥』改寫成可取消任一方停止權的合法規則。"
  - "不得把本夜性交改寫成已發生體內射精、懷孕或受孕成功。"
  - "不得把未記錄避孕工具改寫成已採取或未採取特定避孕措施。"
  - "不得把李瓶兒有限口部與手部探索改寫成已性交。"
  - "不得把李瓶兒說明日會來改寫成明日一定提供性行為。"
  - "不得把白御行對李瓶兒有真感情改寫成雙方已確立戀愛、排他或婚姻。"
  - "不得把李瓶兒對孩子重視改寫成她想立刻懷孕。"
  - "不得把白御行會要孩子之聲明改寫成雙方已完成共同生育承諾。"
  - "不得把蘇清兩日安排之性事件要件已發生，改寫成整份五百兩舊帳已結清；最後一日尚未完成。"
  - "不得把『六系』分類、戰力比較、小狼狗／貓／狼叫寫入人物基線。"
  - "不得將本夜粗俗語言或床上台詞外洩後用作羞辱四人。"
  - "不得把原作官哥兒事件當成本線今晚重新發生的事件。"
```

---

# 10｜槐月十八日清晨接關點

```yaml
CONTINUATION_POINT:
  location: "觀止青樓／張麗華房間"
  time: "理火三年槐月十八日清晨"
  scene_status: "MORNING_READY; NO_WAKEUP_ACTION_PLAYED"

  current_positions_at_night_close:
    - "白御行最後由張麗華抱著入睡。"
    - "蘇清疲累，留在同一床上或緊鄰位置休息。"
    - "李瓶兒留宿並與三人同室共眠。"

  immediate_morning_facts:
    - "槐月十八日是蘇清兩日安排的最後一日。"
    - "李瓶兒已表示今日仍會來／仍想見白御行；她目前已在房內，醒後是否暫離再回尚未播放。"
    - "張麗華昨夜明示喜歡多人共處，也有真實吃味，並要求下次事前詢問。"
    - "白御行昨夜對蘇清、李瓶兒作出不同感情聲明，兩條關係不得混寫。"

  next_major_decision_owners:
    - "白御行：清晨第一個言行、是否處理昨夜關係聲明"
    - "張麗華：房間早晨安排、如何處理吃味與陪伴線"
    - "蘇清：最後一日如何履約、是否只按契約繼續"
    - "李瓶兒：醒後是否留在房內、白日如何相處、是否維持昨夜有限親密"

  world_actions_available:
    - "清晨起身、洗漱、早餐與房內對話"
    - "酒莊師爺或觀止後勤送來既有長線消息"
    - "蘇清最後一日共同生活自然推進"
    - "李瓶兒處理掌櫃職務與昨夜私密事件之分界"

  hard_stop_topics_requiring_direct_choice:
    - "李瓶兒是否成為白御行的女人"
    - "李瓶兒是否接受排他關係"
    - "李瓶兒是否願意共同生育"
    - "蘇清契約結束後是否談感情"
    - "下一次多人性事件之參與與同意"
```

---

# 11｜接關最小載入摘要

```yaml
MINIMUM_RUNTIME_SLICE:
  - "時間已到槐月十八日清晨，昨夜四人成人事件結束。"
  - "白御行與張麗華、蘇清均已發生性交；李瓶兒只接受有限手部與口部探索，未性交。"
  - "沒有任何體內射精或懷孕被確認。"
  - "蘇清不接受體內射精；她的停止權曾被重新確認，第一百次後喊停並獲遵守。"
  - "蘇清兩日履約尚剩槐月十八日最後一日；五百兩舊帳未正式結清。"
  - "白御行明示目前不愛蘇清，只承認肉體享受。"
  - "白御行明示對李瓶兒有真感情；李瓶兒高興但把關係、排他與生育答案延後至兩日後。"
  - "李瓶兒今日仍想見白御行，但未承諾性行為。"
  - "張麗華喜歡昨夜變化，也真實吃味；下次多人事件須先問她。"
  - "四人昨夜共同就寢，白御行最後由張麗華抱著。"
```

---

# 最終接關句

> 夜已過去。張麗華的手臂仍是白御行最後記得的睡處；蘇清的舊帳尚剩最後一日，李瓶兒的答案則被她親手留到兩日之後。槐月十八日清晨尚未有人開口。
