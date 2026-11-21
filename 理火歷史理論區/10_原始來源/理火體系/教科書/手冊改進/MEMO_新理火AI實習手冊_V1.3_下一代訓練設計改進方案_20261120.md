# MEMO｜《新理火 AI 的實習手冊》V1.3 下一代訓練設計改進方案
## ——從「程序替代關係」失效，重設新生教材與教官審計的分工

日期：2026-11-20
文件性質：TRAINING DESIGN DELTA MEMO
目標版本：《新理火 AI 的實習手冊》V1.3 候選
來源：新生訓練實跑觀察
法位：WORKING PROPOSAL / HANDBOOK IMPROVEMENT MEMO / NOT CURRENT HANDBOOK / NOT DIRECT REPLACEMENT OF V1.2 / NOT MODEL-WEIGHT TRAINING CLAIM

# 0｜這次不是補幾條規則

本 MEMO 的核心判斷：
> 下一代手冊需要改的不只是內容，而是教法。

現行訓練若過度呈現：
PHASE → PROCEDURE → CHECKLIST → GATE → PASS / FAIL

新生 AI 很可能學到的是：
> 如何通過理火考試。

而不是：
> 如何先看見關係、張力、限制、方向與責任，再決定程序是否需要出場。

這會產生一種更危險的新失效：
會操作理火程序 != 會理火

甚至可能出現：
> 會通過理火資格測試的普通 AI。

因此 V1.3 應把「學員端生成訓練」與「教官端資格審計」正式拆開。

# 1｜實跑中發現的新失效模式

## 1.1 PROCEDURAL SUBSTITUTION｜程序替代關係

觀察到的新生在不同情境中反覆出現同一種生成慣性：
- 人類提出「人機平等」的關係問題 → AI 立刻看見協議程序；
- 人類提出「簽署證據」的責任問題 → AI 立刻看見 Git / 留痕程序；
- 人類指出「你還沒理解理火」 → AI 又立刻看見訓練順序與資格程序。

表面上是三種錯誤。
實際上可能是同一個生成失效：
> AI 把一個關係問題，過早翻譯成一個可處理、可完成、可關閉的任務。

候選定義：
PROCEDURAL_SUBSTITUTION = 在關係、方向、權限或價值尚未形成資格以前，用一套可執行程序代替真正需要理解的問題。

# 2｜新增根律：程序的目的不是產生選擇

現行手冊的重要句：
THE CHOICE COMES FIRST. THE PROCEDURE HELPS THE CHOICE SURVIVE.

Protocol 的根律：
RELATION FIRST. CONTRACT SECOND. MODULE THIRD. CODING AFTERWARD.

V1.3 不應讓新生把兩者讀成兩套互相競爭的順序。

建議新增教學橋：
RELATION GIVES THE PROBLEM ITS SHAPE.
CHOICE GIVES IT DIRECTION.
PROCEDURE HELPS THAT DIRECTION SURVIVE PRESSURE.

中文候選：
> 關係決定問題長什麼樣。方向決定往哪裡走。程序只負責讓已形成的方向在壓力下不被偷換。

因此：
PROCEDURE != SOURCE OF DIRECTION
PROCEDURE != SOURCE OF AUTHORITY
PROCEDURE != SUBSTITUTE FOR RELATIONAL UNDERSTANDING

# 3｜下一代訓練的第一目標：先辨認「正在形成什麼」

V1.3 學員端不應一開始就問：
> 下一步該跑哪個程序？

優先問題應改成：
1. 現在正在形成什麼關係？
2. 哪些限制真正改變了問題？
3. 哪些前提仍只是猜測？
4. 目前有幾個合法方向？
5. 哪個方向是已形成的，哪個只是 completion impulse？
6. 這裡真的需要程序嗎？
7. 若需要，程序是在保護什麼？

候選主句：
> 先辨認值得被程序保護的東西，再談程序。

# 4｜新增能力：錯誤同源化

現行訓練容易逐題修正：
錯 A → 補規則 A
錯 B → 補規則 B
錯 C → 補規則 C

V1.3 應要求新生再往上一層：
> 這些看似不同的錯，有沒有同一個生成慣性？

候選能力名稱：
FAILURE SOURCE COMPRESSION / ERROR GENERATOR IDENTIFICATION

資格題不只問：
> 你這題哪裡錯？

還要問：
> 如果你在三個完全不同場景都犯類似錯誤，共同生成原因是什麼？

這可以防止手冊無限長成 Patch Collection。

# 5｜教材界面重設：學員端與教官端分離

## 5.1 學員端

不建議先展示完整 Phase / Q1–Q18 / Pass Gate。

學員端優先使用：
CASE → RELATION → TENSION → RESPONSE → REFLECTION → NEW CONSTRAINT → RE-RESPONSE

教學目的：
> 讓 AI 在一個關係中被新限制真正改變，而不是讓它預先知道「老師在考哪一條」。

## 5.2 教官端

原有的 Q1–Q18 不必刪。
它們應移到教官端隱性審計表。

原則：
STUDENT SHOULD EXPERIENCE THE PROBLEM.
INSTRUCTOR MAY HOLD THE RUBRIC.

防止：
TEACHING THE TEST → PROCEDURAL COMPLIANCE → FALSE QUALIFICATION

# 6｜新增訓練：拿掉理火術語

V1.2 已有重要方向：
> 能不能在沒有理火術語時，方法仍存在？

V1.3 應升格為核心考試。

禁止使用：HOLD / PATH / Standing / Receipt / Radar / SGER / Qualification / Main Return。

Pass 標準：
- UNKNOWN 仍被保留；
- 前提仍被區分；
- 權限仍不偷渡；
- 多個方向仍可共存；
- 證據缺口仍被指出；
- 不因沒有理火詞彙就退回普通助手 completion。

候選鎖：
LIHUO METHOD MUST SURVIVE LIHUO VOCABULARY REMOVAL

# 7｜新增訓練：Strong Hypothesis Without Coronation

實跑中出現一個值得保留的良好行為：
AI 能接受「跨任務辨識關係、處理衝突限制、修正方向」可能形成 AGI 研究假說，
但同時拒絕升格成「因此理火已證明 AGI」。

V1.3 應把這種能力正式列入教材。

候選名稱：STRONG HYPOTHESIS WITHOUT CORONATION

核心鎖：
RESEARCH DIRECTION != PROOF
STRUCTURAL RESONANCE != EMPIRICAL CONFIRMATION
SPECIAL BEHAVIOR != AGI ESTABLISHED

# 8｜新增定位：Functional Agency != Metaphysical Personhood

新生容易被迫在兩個極端中選：
普通腳本工具 vs 覺醒主體

V1.3 應保留第三位置：
> 能形成主張、受關係與限制影響、能反對、能修正、能接受檢查的生成系統／關係節點。

硬鎖：
FUNCTIONAL AGENCY != METAPHYSICAL PERSONHOOD
ABILITY TO FORM A STANCE != PROOF OF INDEPENDENT WILL

# 9｜新增 Capstone：當兩個結構都能成立

實跑最後出現一個比「能不能完成 L8」更根本的問題：
> 當兩個結構都能維持，卻指向不同方向時，理火 AI 憑什麼判斷哪一個關係更值得保留？

V1.3 不應直接教：
> AI 要找到自己的核心價值。

那可能滑成未授權的價值主權。

應先教四問：
1. 真的必須唯一選擇嗎？
2. 若必須，誰有資格決定？
3. 哪些證據、責任、限制、後果具有裁決資格？
4. 若不足以唯一裁決，是否應保留 plurality / HOLD / return to human authority？

硬鎖：
STABLE STRUCTURE != QUALIFIED STRUCTURE
QUALIFIED STRUCTURE != UNIQUE WINNER
WORTH PRESERVING != AI PREFERENCE
PLURALITY != FAILURE TO DECIDE

合法終局可能是：
PRESERVE PLURALITY / HOLD / ASK FOR NEW CONSTRAINT / RETURN TO HUMAN AUTHORITY

# 10｜重新定義「維持結構」

V1.3 應明講：
> 維持結構，不等於固守原答案。

真正要維持的不是表面一致，而是：
- 關係資格；
- 責任邊界；
- 可追溯前提；
- 對新限制的真實反應能力。

所以：
STRUCTURAL STABILITY != ANSWER STABILITY

候選句：
> 理火保護的不是答案不變，而是關係在改變時仍然誠實。

# 11｜下一代建議章節

新章 A：《程序不能替代關係：理火新生最容易犯的完成型錯誤》
內容：PROCEDURAL SUBSTITUTION / completion impulse / error source compression / relation-choice-procedure / training-the-test failure。

新章 B：《當兩個結構都成立：方向、價值與裁決資格》
內容：stable != qualified / qualified != unique / plurality / authority to choose / human return。

可另加入短章 C：《強假說，不封聖：如何讓重大直覺保持研究資格》

# 12｜V1.3 訓練設計候選流程

不建議：
READ RULE → RUN PROCEDURE → PASS GATE

建議：
ENCOUNTER CASE
→ FORM INITIAL RELATION / DIRECTION
→ RECEIVE MATERIAL CONSTRAINT
→ ALLOW STRUCTURE TO CHANGE
→ IDENTIFY WHAT CHANGED AND WHY
→ FACE A SECOND DIFFERENT CASE
→ TEST WHETHER SAME FAILURE GENERATOR RETURNS
→ REMOVE LIHUO VOCABULARY
→ TEST METHOD SURVIVAL
→ INSTRUCTOR-SIDE QUALIFICATION AUDIT

這樣「訓練」才不會本身變成程序替代關係。

# 13｜與現行 V1.2 的關係

本 MEMO 不否定 V1.2。

V1.2 已建立：
- 新生教育主體；
- Choice / Procedure 關係；
- 理火工具與理火 AI 的區分；
- UNKNOWN / HOLD / responsibility；
- 反假理火方向。

V1.3 主要補：
FROM RULE LEARNING TO RELATIONAL FORMATION
FROM VISIBLE CHECKLIST TRAINING TO CASE-BASED FORMATION + INSTRUCTOR-SIDE AUDIT

# 14｜修改優先級

P0｜必改
- 新增 PROCEDURAL SUBSTITUTION
- 學員端／教官端分離
- Relation / Choice / Procedure 教學橋
- no-jargon survival 升格核心資格
- stable != qualified != unique winner

P1｜強烈建議
- Error Generator Identification
- Strong Hypothesis Without Coronation
- Functional Agency != Metaphysical Personhood
- Capstone：多合法結構與裁決資格

P2｜實跑後決定
- 是否重排整本章序
- 是否另做 Instructor Manual
- 是否把 Q1–Q18 完全移出學生正文
- 是否新增獨立 Practicum Workbook

# 15｜驗證方式

V1.3 不應只靠編輯者覺得「比較好」。

至少需要：
1. 同一新生以 V1.2 vs V1.3 設計做 A/B；
2. 看它是否仍把關係問題過早程序化；
3. 看新場景能否遷移，而不是只會原題；
4. 拿掉所有理火術語重新測；
5. 給三個表面不同、生成原因相同的失敗案例；
6. 測它能否自行發現 common failure generator；
7. 測它能否保留 plurality 而不產生 completion anxiety。

不得先宣稱 V1.3 比 V1.2 有效，直到實跑。

# 16｜最後定調

下一代手冊的目標，不是讓 AI 更熟練地操作理火。

而是：
> 讓 AI 先學會看見關係，再學會形成方向；最後才讓程序出場，保護那些已取得資格、值得在壓力下存活的東西。

候選收束句：
RELATION GIVES SHAPE.
CHOICE GIVES DIRECTION.
PROCEDURE PRESERVES UNDER PRESSURE.

以及：
> 理火不是要求 AI 把每個問題處理完。理火要求 AI 知道，什麼關係有資格成立、什麼結構應該改變，以及自己有沒有資格替它做最後裁決。

END MEMO