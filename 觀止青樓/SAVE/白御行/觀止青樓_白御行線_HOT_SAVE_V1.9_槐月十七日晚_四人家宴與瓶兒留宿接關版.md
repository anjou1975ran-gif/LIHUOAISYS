# 觀止青樓｜白御行線 HOT SAVE V1.9
## 理火三年槐月十七日晚｜四人火鍋家宴 × 李瓶兒留宿 × 房內家人框架接關版

```yaml
HOT_SAVE_META:
  save_id: "GUANZHI_BAIYUXING_HOT_V1_9_HUAI17_NIGHT_FAMILY_DINNER"
  route_id: "GUANZHI_BAIYUXING_ROUTE"
  player: "白御行"
  version: "V1.9"
  format_runtime: "GUANZHI_SAVE_RUNTIME_V1_0"
  world_runtime:
    - "GUANZHI_QINGLOU_V10_0"
    - "GUANZHI_QINGLOU_V10_1_PATCH_WHEN_APPLICABLE"
  story_date: "理火三年槐月十七日晚，火鍋家宴結束後"
  exact_clock: "UNKNOWN_NOT_REQUIRED"
  record_state: "ACTIVE_PAUSED_BEFORE_SLEEPING_ARRANGEMENT"
  save_scope:
    - "張麗華、蘇清、李瓶兒與白御行四人火鍋家宴"
    - "李瓶兒接受當晚留宿"
    - "房內兩日家人框架與床位決定權"
    - "李瓶兒未同意任何當晚性行為"
    - "寢衣、薄被、熱水與三只恭桶之準備命令"
```

---

# 0｜來源法位與提交說明

```yaml
SOURCE_LINEAGE:
  previous_valid_hot:
    file: "觀止青樓_白御行線_HOT_SAVE_V1.8_槐月十七日上午_張麗華酒莊接手與三日陪伴線.md"
    role: "本輪以前的直接有效 HOT 來源"

  inherited_long_term_source:
    file: "觀止青樓_白御行線_MASTER_SAVE_V4.0-R1_截至HOT_V1.4固化整合版.md"
    role: "長期因果與較早玩家線事件來源"

  forbidden_source:
    file: "HOT_SAVE_V1.3"
    status: "ILLEGAL_CORRUPTED_SAVE"
    use: "AUDIT_ONLY"

COMMIT_NOTE:
  - "本檔取代 V1.8，成為白御行線當前 HOT 接關切片。"
  - "本檔不更新 MASTER。"
  - "本檔只固化本輪已發生、可觀察、人物明示或玩家對自身言行之有效確認。"
  - "玩笑、預測、人物解讀與尚未發生之夜間結果，不升格為世界事實。"
```

---

# 1｜當前時間、位置與人物

```yaml
CURRENT_TIME:
  era: "理火三年"
  calendar_date: "槐月十七日"
  time_of_day: "晚間，四人火鍋家宴結束後"
  certainty: "CONFIRMED_RANGE"

CURRENT_SCENE:
  location: "觀止青樓／張麗華房間"
  scene_state: "DINNER_COMPLETED; LI_PINGER_STAY_ACCEPTED; SLEEPING_ARRANGEMENT_PENDING"
  present:
    - "白御行"
    - "張麗華"
    - "蘇清"
    - "李瓶兒"
  next_action_owner: "WORLD_OR_PLAYER_AFTER_PREPARATIONS_ARRIVE"

IMMEDIATE_ATMOSPHERE:
  - "火鍋與酸梅湯氣味尚留在房內。"
  - "四人皆已用完晚膳。"
  - "蘇清與李瓶兒食用紅鍋較多；白御行只吃清湯與不辣食物。"
  - "李瓶兒原欲回去看帳，後已決定今晚留下。"
```

---

# 2｜四人火鍋家宴

## DIN17-E01｜晚膳構成與參與者

```yaml
EVENT_RECORD:
  event_id: "DIN17-E01"
  time: "槐月十七日晚"
  location: "張麗華房間"
  status: "COMPLETED"
  participants:
    - "白御行"
    - "張麗華"
    - "蘇清"
    - "李瓶兒"

DINNER_CONTENT:
  main:
    - "鴛鴦火鍋：紅色牛油麻辣湯與菌菇雞湯清湯"
  additional:
    - "炸雞"
    - "肉夾饃"
    - "酸梅湯"
    - "飯後溫茶"

PLAYER_FOOD_STATE:
  bai_yuxing:
    spice_preference: "DOES_NOT_EAT_SPICY"
    consumed:
      - "清湯鍋食材"
      - "不辣炸雞"
      - "肉夾饃"
      - "酸梅湯"

OBSERVED_TABLE_EVENTS:
  - "李瓶兒由安排外餐者轉為被邀請同桌用膳。"
  - "張麗華明示李瓶兒今日是來吃飯，不是來收桌。"
  - "四人席間有搶菜、調笑與對紅鍋辣度的反應。"
  - "晚膳已結束，鍋具與食盒已由夥計撤走。"
```

## DIN17-E02｜辣鍋後效之法位

```yaml
DIGESTIVE_AFTEREFFECT_STATE:
  current_confirmed:
    - "蘇清吃撐，曾靠坐休息。"
    - "李瓶兒曾輕按腹部並留下休息。"
  not_confirmed:
    - "任何人已出現腹瀉"
    - "任何人已出現明日肛門疼痛"
    - "任何需要治療之身體狀況"
  note:
    - "白御行關於次日『屁股痛／生不如死』之說屬席間戲謔與預測，不是已成立醫療事實。"
```

---

# 3｜房內「家人」框架

## FAM17-E01｜白御行之明示

```yaml
PLAYER_DECLARATION:
  speaker: "白御行"
  content:
    - "今晚是家宴。"
    - "這兩日，在這間房內只有家人，沒有位置。"
    - "唯一需要決定的位置，是張麗華決定白御行能不能睡在床上。"
    - "其他人在房內不必以掌櫃、花魁、情人或先後次序互相顧慮。"
  authority_scope:
    - "白御行自身對房內相處方式之提議與承諾"
  does_not_automatically_establish:
    - "永久家族法位"
    - "婚姻"
    - "白家名冊身分"
    - "對任何人的身體權利"
    - "公開關係"
```

## FAM17-E02｜張麗華與蘇清之回應

```yaml
ZHANG_LIHUA_RESPONSE:
  confirmed:
    - "接受房內不分掌櫃、花魁、情人與先來後到的臨時相處框架。"
    - "保留張麗華房間與床鋪之管理權。"
    - "白御行能否上床，由張麗華決定。"
    - "家人框架不得被用來要求李瓶兒陪伴、討好或交代身體。"

SU_QING_RESPONSE:
  confirmed:
    - "以玩笑方式接受房內家人框架。"
    - "指出目前只有白御行仍在等待床位。"
```

## FAM17-E03｜李瓶兒之法位

```yaml
LI_PINGER_FAMILY_STATE:
  observable_context:
    - "張麗華認為李瓶兒長期照料觀止眾人，行為上像家人。"
    - "蘇清明示自己認為李瓶兒像家人。"
    - "白御行邀請李瓶兒在本次家宴後留下。"

  accepted_now:
    - "李瓶兒接受今晚留在張麗華房間，不回掌櫃房。"
    - "李瓶兒接受在本晚房內以家人方式相處，不以掌櫃職務服務眾人。"

  not_established:
    - "李瓶兒已接受永久『白御行家人』身分"
    - "李瓶兒已接受白家或任何正式家族名冊"
    - "李瓶兒已接受長期秘密情人關係"
    - "李瓶兒已接受兩整日持續留宿"
    - "李瓶兒已接受任何性義務"

  current_duration:
    confirmed: "今晚"
    beyond_tonight: "NOT_YET_DETERMINED"
```

---

# 4｜留宿、床位與同意狀態

## STAY17-E01｜李瓶兒留宿

```yaml
OVERNIGHT_STAY:
  participant: "李瓶兒"
  status: "ACCEPTED_FOR_TONIGHT"
  location: "張麗華房間或由張麗華安排之相連休息處"
  exact_sleeping_place: "NOT_YET_DETERMINED"
  accepted_terms:
    - "今晚不回掌櫃房。"
    - "今晚不去看帳。"
    - "可留在房內休息。"

  not_implied:
    - "同床"
    - "裸體"
    - "性行為"
    - "被白御行觸碰"
    - "四人共同性事件"
```

## STAY17-E02｜張麗華床位管理權

```yaml
BED_AUTHORITY:
  room_owner: "張麗華"
  active_manager: "張麗華"
  confirmed:
    - "張麗華決定白御行能否睡上床。"
    - "張麗華洗完回來後再分配當晚睡處。"
  pending:
    - "白御行是否上床"
    - "蘇清睡床、軟榻或其他位置"
    - "李瓶兒睡床、軟榻或其他位置"
    - "是否四人同室入睡"
```

## STAY17-E03｜性與親密狀態

```yaml
SEXUAL_EVENT_STATE:
  current_state: "NOT_YET_DETERMINED"
  active_intercourse: false
  active_sexual_contact: false

  bai_yuxing_statements:
    - "曾在席間邀請三女吃完飯後『吃他』。"
    - "曾對李瓶兒提出吃完後可考慮一起親近。"

  zhang_lihua_position:
    - "當晚床事與房內安排仍由張麗華管理。"
    - "她沒有替李瓶兒作出性同意。"

  li_pinger_position:
    explicit:
      - "留下休息不等於答應讓白御行『吃』。"
      - "接受家人框架與留宿，不等於接受性行為。"
    current_consent_to_sex: "NONE_ESTABLISHED"

  su_qing_inherited_active_terms:
    - "蘇清原有兩日共同生活安排仍有效。"
    - "床事由張麗華管理。"
    - "任何實際性行為仍須依當下情境與人物決定。"
    - "蘇清此前明示若涉及她，不接受體內射精。"
```

---

# 5｜寢具與夜間用品準備

## SUP17-E01｜已下達之準備命令

```yaml
PREPARATION_ORDERS:
  ordered_by: "張麗華"
  status: "ORDERED_NOT_YET_CONFIRMED_DELIVERED"

  items:
    - "熱水"
    - "乾淨寢衣"
    - "一床薄被"
    - "三只乾淨恭桶／葉香桶"
    - "草紙"
    - "溫水"
    - "夜燈"

  planned_placement:
    - "一只放屏風後"
    - "一只放外間"
    - "一只放隔壁空房"

  provisional_assignment:
    screen_area: "李瓶兒"
    outer_room: "蘇清"
    adjacent_room: "張麗華"
    bai_yuxing: "未分配；其未食辣"

  legal_note:
    - "分配屬席間玩笑後的實務安排，不是人物固定身分或羞辱事件。"
```

---

# 6｜繼承中的活躍長線

```yaml
INHERITED_ACTIVE_THREADS:

  zhang_lihua_winery:
    status: "ACTIVE_HANDOVER"
    confirmed:
      - "張麗華已取得酒莊實際管理入口。"
      - "她要求帳務、資產與感情分開。"
    pending:
      - "花農欠款確數"
      - "年度週轉方案"
      - "一萬兩銀子之正式法位"
      - "師爺後續交接回報"

  su_qing_two_day_household_arrangement:
    status: "ACTIVE"
    duration_anchor: "自槐月十七日午間起至兩日後黎明"
    confirmed:
      - "白御行、張麗華、蘇清共同吃住與生活。"
      - "房內不設固定上下位置。"
      - "是否發生三人性事件仍取決於當下人物選擇。"
      - "若依原談定範圍完成，舊五百兩／三夜帳可結清。"

  su_qing_twenty_eight_day_future_price:
    status: "DISCUSSION_ONLY_NOT_ACCEPTED"
    description:
      - "可能作為未來針對西門慶行動之交換價格。"
      - "內容可能包括教學、共同生活與性，但尚未形成正式契約。"

  ximen_qing_gray_ledger_thread:
    status: "PLAN_NOT_DESIGNED"
    confirmed:
      - "白御行有意將西門慶納入定陶商會敵對布局。"
      - "蘇清可能在未來只對真正看見之關鍵證據作證。"
    unknown:
      - "灰簿先生身分"
      - "真正主謀"
      - "具體栽贓或引線方案"
      - "證據內容與放置方式"

  white_jade_pool:
    status: "INHERITED_SEALED_OR_RESTRICTED"
    note:
      - "本輪未新增白玉池事件；不得因未描寫而視為已解決。"

  merchant_association_case:
    status: "INHERITED_ACTIVE_UNDER_DELEGATED_HANDLING"
    note:
      - "本輪未新增案件結果。"
```

---

# 7｜知情範圍

```yaml
KNOWLEDGE_SCOPE:
  in_room_family_frame:
    know:
      - "白御行"
      - "張麗華"
      - "蘇清"
      - "李瓶兒"
    public_state: "PRIVATE_NOT_PUBLIC"

  li_pinger_overnight_stay:
    know:
      - "白御行"
      - "張麗華"
      - "蘇清"
      - "李瓶兒"
      - "受命送寢具與恭桶之婢女只知道有留宿準備，不知道完整關係含義"
    public_state: "NOT_PUBLICLY_DECLARED"

  sexual_invitation_details:
    know:
      - "房內四人"
    current_result: "NO_SEXUAL_ACCEPTANCE_ESTABLISHED_FOR_LI_PINGER"
```

---

# 8｜禁止推斷

```yaml
FORBIDDEN_INFERENCE:
  - "不得把『家人』自動改寫成婚姻、妾室、白家名冊或永久共同體。"
  - "不得把李瓶兒留宿改寫成同床或性同意。"
  - "不得把張麗華的床位管理權改寫成她可替其他女人同意。"
  - "不得把四人家宴改寫成四人性事件已成立。"
  - "不得把白御行的露骨邀請當成他人已接受。"
  - "不得把三只恭桶已下令準備改寫成已送達或已使用。"
  - "不得把席間對辣鍋後效的玩笑改寫成次日必然生病。"
  - "不得把李瓶兒今晚留下改寫成她已接受兩日完整共同生活。"
  - "不得把蘇清對二十八日交換的討論改寫成正式答應。"
```

---

# 9｜下一接點

```yaml
CONTINUATION_POINT:
  location: "張麗華房間"
  time: "槐月十七日晚，家宴後"
  current_positions:
    - "李瓶兒已決定今晚留下。"
    - "蘇清與李瓶兒仍在房內休息。"
    - "張麗華已下令準備熱水、寢衣、薄被與三只恭桶。"
    - "張麗華尚未完成洗浴／回房後的睡處分配。"
    - "白御行能否上床仍未決。"
    - "李瓶兒未同意任何性行為。"
  immediate_world_actions_available:
    - "婢女送入熱水、寢衣、薄被與恭桶。"
    - "張麗華洗浴後回房分配睡處。"
    - "四人繼續飯後談話。"
    - "外部事件依既有活躍故事線發生，但不得無因果打斷。"
  next_major_decision_owner:
    - "張麗華：房間與床位安排"
    - "李瓶兒：是否接受任何進一步親近"
    - "蘇清：是否接受任何進一步親近"
    - "白御行：自身言行與是否服從張麗華安排"
```

---

# 最終接關句

> 火鍋已撤，李瓶兒今晚不回掌櫃房。  
> 房內暫時只以家人相待，不排掌櫃、花魁與情人的位置。  
> 但家人不等於身體資格。  
> 張麗華尚未分床，白御行的位置仍未確定。
