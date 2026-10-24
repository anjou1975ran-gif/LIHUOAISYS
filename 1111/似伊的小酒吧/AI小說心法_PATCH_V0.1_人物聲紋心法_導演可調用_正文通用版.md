# AI 小說心法 PATCH V0.1
# 人物聲紋心法｜Character Voiceprint Method Patch

## 導演可調用 × 人物池零侵入 × 正文寫作通用 × 反同聲化 × 關係變調 × 聲紋回聲測試

```yaml
PATCH:
  name: "人物聲紋心法"
  english_name: "Character Voiceprint Method"
  short_id: "CVMP"
  version: "V0.1"
  status: "EXPERIMENTAL_METHOD_PATCH"
  parent:
    file: "AI小說心法(敘事物理學).md"
    version: "V0.1"
  target:
    - "AI 小說導演"
    - "互動小說 Runtime"
    - "長篇小說生成"
    - "章節續寫"
    - "多角色對話"
    - "人物一致性審計"
  character_pool_schema_change_required: false
  standalone_character_database_required: false
  runtime_required: false
  decision_authority: false
  world_fact_authority: false
```

> **本 PATCH 不修改人物卡。**
>
> **本 PATCH 不替人物決定。**
>
> **它只處理一件事：當角色已經做出選擇，如何讓那個選擇穿過她自己的語言結構，成為只有她會這樣說的一句話。**

---

# 0｜來源法位

《AI 小說心法 V0.1》已建立三個前提：

```text
角色不是形容詞，而是穩定的決策系統。

高階角色必須具有：
穩定的行動邏輯
穩定的價值排序
穩定的壓力反應
穩定的語言方式
穩定的不可越界處
```

同時：

```text
對白不是聊天。
對白是角色在改變結構。
```

以及：

```text
不要先寫文本。
先看故事力場。
```

本 PATCH 不改寫這三條。

它只補上兩者之間原本缺少的顯影層：

```text
故事力場
↓
角色看見什麼
↓
角色承受什麼壓力
↓
角色如何判斷
↓
角色做出什麼選擇
↓
這句話要對場造成什麼作用
↓
【人物聲紋心法】
↓
台詞／沉默／打斷／轉移／稱呼／句法 顯影
```

---

# 1｜問題：角色不同，為什麼說話還是很像？

AI 可以讀懂：

```text
A 冷
B 狠
C 溫柔
D 世故
E 聰明
```

但進入長篇生成後，模型容易把它們壓成幾種共用語氣：

```text
冷角色
→ 短句

聰明角色
→ 反問

成熟角色
→ 少解釋

溫柔角色
→ 留台階

毒舌角色
→ 挖苦
```

結果是：

```text
CHARACTER_STRUCTURE_DISTINCT
but
LANGUAGE_SURFACE_CONVERGED
```

人物沒有真的變成同一個人。

可是她們經過同一個模型顯影後，長出了同一張嘴。

本 PATCH 將這個問題稱為：

```text
GENERIC_LLM_VOICE_CONVERGENCE
中文：通用模型聲線收斂／人物同聲化
```

---

# 2｜第一根法：聲紋不是口頭禪

人物聲紋不是：

```text
她常說「可不是嘛」
她總叫人「客官」
她喜歡冷笑
她每次生氣都說「有意思」
```

這些可以是人物語言的一部分。

但它們不是聲紋本體。

心法句：

> **聲紋不是角色常說什麼。**
>
> **聲紋是角色如何把自己的判斷變成語言。**

所以：

```text
CATCHPHRASE != VOICEPRINT
REGISTER != VOICEPRINT
DIALECT != VOICEPRINT
SHORT_SENTENCE != VOICEPRINT
```

真正的聲紋存在於：

```text
她先看見什麼
↓
她怎麼取得判斷
↓
她願意承認多少
↓
她想從對方身上拿到什麼
↓
她如何取得發言權
↓
她如何把話說完或故意不說完
```

---

# 3｜第二根法：人物先決定，聲紋後顯影

```text
VOICEPRINT
!=
CHARACTER_DECISION
```

人物聲紋不得取得：

- 人物選擇權；
- 關係成立權；
- 情緒成立權；
- 世界事實權；
- 劇情方向權。

錯誤：

```text
她設定毒舌
→ 所以她一定攻擊對方
```

錯誤：

```text
她設定冷淡
→ 所以她永遠短句
```

正確：

```text
她本輪選擇拒絕
+
她不願交出情緒解釋權
+
她要阻止對方取得追問資格
↓
再由她的聲紋決定如何拒絕
```

心法句：

> **人物先活，聲音後顯影。**

---

# 4｜第三根法：聲紋是「取得一句話的路徑」

同一句意思：

> 「我不同意。」

低階差異只是換字：

```text
A：不行。
B：恐怕不妥。
C：你想得美。
D：我看還是算了。
```

這不是穩定聲紋。

真正差異應該發生在「一句話如何被取得」。

例如：

```text
A
規矩
↓
判定違規
↓
拒絕

B
先辨認對方會失去什麼
↓
留台階
↓
拒絕

C
拆穿對方真正動機
↓
奪回發言權
↓
拒絕

D
估算代價
↓
把後果擺出來
↓
讓對方自己退
```

最後四個人甚至都可以說：

> 「不行。」

但讀者仍應感覺：

> 她們不是從同一個地方走到這句話。

心法句：

> **同一句意思，換一個人，就應該經過不同的路才能說出口。**

---

# 5｜聲紋六問

導演或小說生成 AI 在真正寫一句重要台詞前，不必建立大型表格。

只需要快速問六件事：

```yaml
VOICEPRINT_SIX_QUESTIONS:

  Q1_PERCEPTION:
    question: "她這一刻先看見的是什麼？"

  Q2_JUDGMENT:
    question: "她習慣用什麼東西判斷這件事？"

  Q3_DIALOGUE_GOAL:
    question: "她這句話想從場中取得什麼？"

  Q4_DISCLOSURE:
    question: "她願意讓對方知道多少？"

  Q5_LANGUAGE_PATH:
    question: "她會從什麼語言路徑走到這個意思？"

  Q6_EXIT:
    question: "她希望這句話說完後，對方還剩多少發言空間？"
```

這六問不一定顯式輸出。

它是生成前的心法。

---

# 6｜人物聲紋的七個可觀察面

本 PATCH 不要求人物卡新增欄位。

若來源人物資料足夠，導演可以從既有人物設定、原作、前文與場景中自行抽取以下七個面。

## 6.1 ENTRY｜如何取得發言權

人物開口前的習慣不同：

```text
直接回答
先反問
先糾正
先笑
先沉默
先接住對方
先否定前提
直接打斷
故意答非所問
```

這不是裝飾。

它表示人物如何理解：

> 誰有資格定義問題。

---

## 6.2 JUDGMENT LANGUAGE｜用什麼世界判斷

人物的生活經驗會形成不同的判斷材料。

例如：

```text
商人
→ 價、帳、風險、交換、虧欠

廚師
→ 火候、先後、熟生、配料、手上功夫

琴師
→ 音、弦、停頓、節拍、破音

軍人
→ 距離、陣形、位置、命令、退路

官員
→ 名分、程序、責任、上下

老鴇／生意人
→ 客、流水、回頭、生意、行情

醫者
→ 症狀、身體、反應、程度、時間
```

禁止機械化：

```text
琴師每句都說琴
商人每句都說錢
```

真正要求只是：

> **當人物需要理解陌生事物時，她最自然借用哪一套世界模型？**

---

## 6.3 SYNTAX｜句子怎麼走

聲紋可存在於：

```text
先結論後理由
先理由後結論
先問後答
不給主語
句子常中斷
大量並列
習慣反問
少用反問
長句堆條件
短句下判決
先重述對方再反駁
```

句法不是固定模板。

它應隨壓力改變。

但角色通常仍有慣性。

---

## 6.4 INFORMATION RELEASE｜資訊怎麼給

人物不是都用相同資訊密度。

有人：

```text
一次說完
```

有人：

```text
只說結論
```

有人：

```text
故意留半句
```

有人：

```text
讓對方自己追問
```

有人：

```text
只回答被問到的範圍
```

有人：

```text
表面回答 A
實際送出 B
```

資訊釋放方式是非常重要的聲紋。

---

## 6.5 TURN CONTROL｜如何控制對話

同一句話也可能透過不同輪次結構成立：

```text
搶話
等完
不接
轉題
追問
逼對方先回答
引用第三人
用動作結束
把問題退回去
```

人物聲紋不只存在於引號裡。

它也存在於：

> **她什麼時候開口，以及什麼時候拒絕開口。**

---

## 6.6 ADDRESS｜稱呼系統

稱呼不是單純古風裝飾。

人物對：

```text
陌生人
上位者
下位者
姐妹
家人
愛人
仇人
舊識
```

可能使用不同稱呼策略。

更重要的是：

> **人物在關係失穩時，稱呼是否改變。**

例如：

```text
名字
→ 姓氏

乳名
→ 正式名

姐姐
→ 掌櫃

你
→ 客官
```

稱呼變化可以直接表示關係溫度與權力距離改變。

---

## 6.7 EXIT｜怎麼結束一句話

人物常常不是靠「內容」收尾。

而是靠：

```text
下判決
留問題
轉身
繼續工作
不回答
換稱呼
笑
收回目光
一句禮貌話
一句威脅
一句玩笑
```

她如何收口，往往比她說了多少更能辨認她。

---

# 7｜聲紋不是固定聲線

人物不能像語音包。

同一角色在不同關係中，本來就應該變調。

本 PATCH 使用：

```text
MANIFESTED_VOICE
=
CHARACTER_BASE
× RELATION
× POWER_POSITION
× PUBLIC_PRIVATE_SCOPE
× EMOTIONAL_LOAD
× CURRENT_GOAL
× CURRENT_PRESSURE
```

所以：

```text
同一人物對陌生人
!=
對姐妹
!=
對掌櫃
!=
對愛人
!=
對仇人
```

但：

```text
RELATION_SHIFT
!=
IDENTITY_ERASURE
```

心法句：

> **聲紋要穩，聲線要活。**

---

# 8｜情緒不是換形容詞，要讓語言機制失衡

低階寫法：

```text
她冷冷地說。
她憤怒地說。
她顫聲說。
她悲傷地說。
```

人物聲紋心法要求：

> 情緒真正進入語言結構。

例如：

```text
平常長句
→ 生氣後變短

平常給理由
→ 生氣後只給判決

平常稱名字
→ 受傷後改用身份稱呼

平常不打斷
→ 焦躁後開始截斷

平常回答完整
→ 心虛時開始補太多

平常善於諷刺
→ 真正受傷時反而沒有諷刺

平常市井直白
→ 真正害怕時突然非常客氣
```

真正有價值的不是：

```text
ANGER = LOUDER
```

而是：

```text
EMOTION
→ LANGUAGE MECHANISM DEFORMATION
```

心法句：

> **情緒不是替台詞上色。**
>
> **情緒會改變人物原本說話的機械。**

---

# 9｜壓力越高，越不能把所有人寫成短句

AI 常見錯誤：

```text
高壓場景
→ 所有人短句
→ 所有人冷
→ 所有人不解釋
```

這會造成：

```text
PRESSURE
→ VOICE HOMOGENIZATION
```

但真實人物在高壓下可能完全相反：

```text
有人越危險越少話
有人越怕越囉嗦
有人開始重複
有人開始講規矩
有人開始說笑
有人突然變得正式
有人停止使用比喻
有人反而說得比平常更清楚
```

所以：

> **壓力必須放大人物差異，不是抹平人物差異。**

---

# 10｜對白功能先於聲紋

《AI 小說心法》已建立：

```text
對白可以：
暴露前提
改變權力
壓縮選擇
埋下命運節點
掀開結構矛盾
製造不可逆後果
```

本 PATCH 因此要求生成順序：

```text
CURRENT CHARACTER DECISION
↓
DIALOGUE STRUCTURAL FUNCTION
↓
VOICEPRINT RENDERING
↓
FINAL LINE
```

例如：

```yaml
DECISION:
  refuse_to_admit_jealousy: true

DIALOGUE_FUNCTION:
  - "讓對方知道她已看穿挑釁"
  - "不讓對方取得『她吃醋』的勝利"
  - "保留下一輪衝突"
```

這時才問：

> 這個人會如何說？

而不是看到人物卡的「毒舌」就直接生成毒舌句。

---

# 11｜沉默也是聲紋

有時最像角色的台詞：

> 根本不是台詞。

聲紋心法必須允許：

```text
SPEECH
SILENCE
ACTION
INTERRUPTION
NON_RESPONSE
REDIRECTION
```

都是合法顯影。

但沉默也不能偷懶。

要問：

```text
她是不想回答？
不能回答？
等對方先暴露？
正在壓住情緒？
覺得問題不值得回答？
用沉默懲罰對方？
```

心法句：

> **沉默不是沒有聲音。**
>
> **沉默是人物拒絕把哪一部分自己交出去。**

---

# 12｜禁止項：最常見的假聲紋

```yaml
VOICEPRINT_ANTI_PATTERNS:

  CATCHPHRASE_COSPLAY:
    meaning: "靠固定口頭禪辨認人物"

  ADJECTIVE_VOICE:
    meaning: "只寫冷、暖、毒、媚、穩等形容詞"

  UNIVERSAL_WIT:
    meaning: "所有聰明人物都會同一種漂亮反問"

  UNIVERSAL_COLDNESS:
    meaning: "所有強者都短句、不解釋、淡淡一笑"

  UNIVERSAL_MATURITY:
    meaning: "所有成熟人物都替別人總結人生"

  PERIOD_COSTUME:
    meaning: "用古風詞、方言或稱呼假裝完成角色差異"

  AUTHOR_VOICE_OVERWRITE:
    meaning: "所有人物最後都被生成 AI 自己的文學腔統一"

  EMOTION_AS_ADVERB:
    meaning: "情緒只靠『冷冷地／淡淡地／顫聲』"

  EXPOSITION_MOUTH:
    meaning: "所有人物都替作者解釋世界設定"

  TOO_CLEVER_TO_BE_HUMAN:
    meaning: "每個人物都能在當下說出完美精煉、可引用的名言"
```

---

# 13｜反作者聲音覆寫

長篇小說最危險的不是角色沒有設定。

而是作者型 LLM 的語言慣性太強。

它可能使所有人物都變成：

```text
同樣精準
同樣會反問
同樣克制
同樣會說漂亮的結構句
同樣知道自己在想什麼
```

因此導演／寫作 AI 在重要多角色場景應做：

```text
AUTHOR_VOICE_CHECK:

  ask:
    - "這句是否太像我平常會寫的句子，而不像人物會說的句子？"
    - "另一個角色是否也可以原封不動說這句？"
    - "這句是否把人物不知道的結構分析說出來了？"
    - "人物是否突然擁有作者級總結能力？"
```

若：

```text
LINE_TRANSFERABLE_TO_MULTIPLE_CHARACTERS = TRUE
```

則：

```text
VOICE_IDENTITY_WEAK
→ REWRITE
```

---

# 14｜導演調用流程

觀止、九尾龜或其他互動小說導演可以直接使用以下輕量流程，不需要修改人物池。

```yaml
BEFORE_DIALOGUE_RENDER:

  1_SCENE:
    - "確認當前場景力場與壓力線"

  2_CHARACTER:
    - "確認人物本輪知識"
    - "確認人物本輪關係"
    - "確認人物本輪選擇"

  3_DIALOGUE_FUNCTION:
    - "這句話要對場做什麼？"

  4_SOURCE_PRIOR:
    - "讀取可用人物設定／原作 expression prior／前文已成立語言習慣"

  5_VOICEPRINT:
    - "套用聲紋六問"
    - "選擇人物自己的語言路徑"
    - "依關係／權力／情緒變調"

  6_RENDER:
    - "生成台詞、沉默、打斷或動作"

  7_CHECK:
    - "檢查是否落入通用 LLM 聲線"
    - "檢查是否能被其他角色無痛替換"
```

最短 Runtime 句：

```text
先決定她要做什麼。
再決定這句話要改變什麼。
最後才決定她會怎麼說。
```

---

# 15｜正文寫作流程

本 PATCH 不只給導演 Runtime。

一般小說 AI 或作者在寫正文時也可以直接使用。

## 15.1 單人物場景

```text
人物當前壓力
↓
人物本輪選擇
↓
她不願說出的部分
↓
她對收話者的關係
↓
她的語言路徑
↓
台詞
```

## 15.2 多人物場景

先不要逐句寫。

先列：

```text
A 這輪想取得什麼
B 這輪想守住什麼
C 不能明說什麼
D 正在誤判什麼
```

再讓每個人使用不同語言路徑。

這樣對話才不是：

> 作者輪流借四張嘴說話。

而是：

> 四個結構在同一張桌上互相改變。

## 15.3 長篇續寫

長篇寫作中，聲紋不只來自人物卡。

也應讀取：

```text
早期章節已形成的說話習慣
近期關係變化
創傷／地位／職業變化
人物是否學會新的語言
某些稱呼是否已失效
某種幽默是否因事件而消失
```

所以：

```text
VOICE_CONTINUITY
!=
VOICE_IMMOBILITY
```

人物可以變。

但變化必須有事件來源。

---

# 16｜四個最小測試

## TEST 1｜Blind Voice Test

```text
生成多個角色的台詞
↓
刪除人物名字
↓
刪除動作身份提示
↓
只留下台詞
↓
能否辨認是誰？
```

判準：

```text
辨認只能靠「兇／柔／文雅」
→ WEAK

能指出其判斷路徑、資訊釋放與對話控制差異
→ STRONGER
```

心法句：

> **真正的聲紋，是拿掉名字之後，人物還留在句子裡。**

---

## TEST 2｜Same-Intent Contrast Test

給多個角色相同：

```text
WORLD FACT
CURRENT GOAL
DIALOGUE INTENT
```

看生成差異。

若只是：

```text
換詞
換口氣
換敬語
```

FAIL。

應出現：

```text
不同判斷入口
不同論證習慣
不同資訊釋放
不同收束方式
```

---

## TEST 3｜Relation Shift Test

同一角色分別對：

```text
陌生人
上位者
朋友
愛人
仇人
```

生成同一意圖的話。

要求：

```text
VOICE MODULATES
but
IDENTITY SURVIVES
```

若五組完全相同：

```text
VOICE_TOO_STATIC
```

若五組完全不像同一人：

```text
IDENTITY_LOST
```

---

## TEST 4｜Anti-Catchphrase Test

禁止使用角色：

- 招牌稱呼；
- 方言標記；
- 固定口頭禪；
- 招牌動作。

再生成。

如果人物立刻無法辨認：

```text
VOICEPRINT_NOT_ESTABLISHED
```

---

# 17｜第五個進階測試：Voice Echo Test

《AI 小說心法》已有「結構回聲測試」：

> 經翻譯、回譯或重述後，核心壓強、因果、角色功能與張力形狀是否仍保存。

人物聲紋可以建立對應測試：

```text
原台詞
↓
去修辭重述
↓
換語域重述
↓
再恢復人物台詞
↓
檢查人物的「語言取得路徑」是否仍在
```

例如原句中真正重要的若是：

```text
先算代價
→ 不直接拒絕
→ 讓對方自己退
```

那麼即使：

- 換成白話；
- 換成古典中文；
- 換成現代職場；
- 換成另一種方言；

只要這個路徑仍在，

人物聲紋仍有結構回聲。

本 PATCH 稱為：

```text
VOICE_ECHO
```

心法句：

> **能換詞而不換人的聲音，才是比較深的聲紋。**

---

# 18｜人物聲紋與對白裁決的分工

未來若《AI 小說心法》正式建立「對白裁決心法」，兩者應保持分工：

```text
對白裁決心法
→ 這句話對場做什麼？

人物聲紋心法
→ 這個人會怎麼做出這句話？
```

因此：

```text
DIALOGUE_FUNCTION
!=
VOICEPRINT
```

但：

```text
FINAL_DIALOGUE
=
DIALOGUE_FUNCTION
×
CHARACTER_DECISION
×
VOICEPRINT
×
CURRENT_RELATION
×
SCENE_PRESSURE
```

---

# 19｜人物聲紋與人物池的分工

人物池可以提供：

```text
人物歷史
價值排序
注意偏向
決策偏向
關係姿態
語氣 prior
迴避方式
失穩條件
原作語料
```

人物聲紋 PATCH 負責：

```text
把這些差異
↓
轉成當前場景中的語言差異
```

禁止：

```text
VOICE_PATCH_WRITES_NEW_CHARACTER_FACT = FALSE
VOICE_PATCH_CHANGES_RELATION = FALSE
VOICE_PATCH_DECIDES_DESIRE = FALSE
VOICE_PATCH_DECIDES_ACTION = FALSE
```

所以人物池不需要因本 PATCH 立即升版。

---

# 20｜沒有完整人物池也可以使用

本 PATCH 未來應可用在一般小說寫作。

即使角色沒有八軸卡，只要作者已經知道：

```text
她最在意什麼
她怎麼判斷
她怕失去什麼
她怎麼處理關係
她怎麼做決定
```

就可以從正文與人物設計中生成臨時聲紋。

最低輸入：

```yaml
MINIMUM_VOICEPRINT_INPUT:
  attention: "她先看什麼"
  judgment: "她怎麼判斷"
  relation: "她怎麼對待眼前這個人"
  decision: "她這輪選擇什麼"
  pressure: "她現在承受什麼"
```

不要求專用人物池。

因此：

```text
CVMP
!= GUANZHI_ONLY
CVMP
!= JIUWEIGUI_ONLY
CVMP
!= CHARACTER_CARD_REQUIRED
```

---

# 21｜快速版：一句台詞前的三秒檢查

如果不想跑完整流程，只問：

```text
1. 這個意思，為什麼是她得出來的？

2. 她為什麼會用這種方式把它交給眼前這個人？

3. 把名字拿掉，另一個角色能不能原封不動說這句？
```

如果第三題答案是：

> 可以。

重寫。

---

# 22｜PATCH Regression Checklist

```yaml
CVMP_V0_1_REGRESSION:

  C01_DECISION_PRECEDES_VOICE:
    pass: "聲紋不替角色做決定"

  C02_DIALOGUE_FUNCTION_PRECEDES_RENDER:
    pass: "先知道台詞對場的作用，再顯影語言"

  C03_NO_CHARACTER_POOL_MUTATION:
    pass: "不要求人物池 schema 升級"

  C04_NO_CATCHPHRASE_IDENTITY:
    pass: "人物差異不依賴口頭禪"

  C05_RELATION_MODULATION:
    pass: "人物對不同關係可變調"

  C06_IDENTITY_SURVIVES_MODULATION:
    pass: "變調後仍可辨認同一人物"

  C07_PRESSURE_DOES_NOT_HOMOGENIZE:
    pass: "高壓不自動把所有角色壓成短句冷語"

  C08_AUTHOR_VOICE_RESISTANCE:
    pass: "重要台詞不可無痛交換給其他人物"

  C09_SILENCE_IS_STRUCTURED:
    pass: "沉默有角色原因，不是生成偷懶"

  C10_GENERAL_NOVEL_PORTABILITY:
    pass: "無專用人物池時仍可使用"

  C11_BLIND_VOICE_TEST:
    status: "RECOMMENDED"

  C12_SAME_INTENT_CONTRAST:
    status: "RECOMMENDED"

  C13_RELATION_SHIFT_TEST:
    status: "RECOMMENDED"

  C14_ANTI_CATCHPHRASE_TEST:
    status: "RECOMMENDED"

  C15_VOICE_ECHO_TEST:
    status: "EXPERIMENTAL"
```

---

# 23｜本 PATCH 不處理什麼

```text
不建立人物人格。
不補人物未知歷史。
不替角色決定愛誰。
不替角色決定同意。
不替角色決定立場。
不修改世界事實。
不保證每一句台詞都必須可盲猜。
不要求人物永遠維持固定措辭。
不要求小說變成角色聲音展示會。
```

聲紋服務故事。

故事不是為聲紋服務。

---

# 24｜與《AI 小說心法》的總綱對齊

原心法：

> **不要先寫文本。先看故事力場。**

人物聲紋心法追加：

> **不要先寫台詞。先看這個人如何走到這句話。**

原心法：

> **角色不是「像一個人」。角色要「像一個系統」。**

人物聲紋心法追加：

> **角色的聲音，也不是語氣標籤。它是角色系統穿過語言後留下的痕跡。**

原心法：

> **對白不是角色在說話。對白是角色在改變結構。**

人物聲紋心法追加：

> **角色以自己的聲紋改變結構。否則只是作者借了另一張嘴。**

---

# FINAL｜人物聲紋心法三句

> **人物聲紋，不是她常說什麼。**
>
> **是她如何把自己的判斷變成語言。**

> **同一句意思，換一個人，就應該經過不同的路才能說出口。**

> **真正的聲紋，是拿掉名字之後，人物還留在句子裡。**

再加一條執行句：

> **先讓人物做出選擇。**
>
> **再讓選擇穿過她自己的聲音。**

---

# PATCH END

```yaml
PATCH_END:
  id: "CVMP-V0.1"
  parent: "AI 小說心法 V0.1"
  character_pool_change: false
  director_callable: true
  general_novel_writing_portable: true
  future_merge_candidate: true
  current_status: "EXPERIMENTAL METHOD PATCH / AWAITING STORY REGRESSION"
```
