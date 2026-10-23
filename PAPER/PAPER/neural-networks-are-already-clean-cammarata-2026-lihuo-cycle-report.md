# LIHUO T5 審查與週期回報｜Neural Networks Are Already Clean

**日期**：2026-10-23（Asia/Taipei）  
**來源**：[Nick Cammarata, Neural Networks Are Already Clean, Goodfire](https://already-clean.goodfire.com/)（2026-10-15）  
**研究形式**：公開長篇研究文章／working hypothesis；非已確認通過期刊同行審查的論文。  
**網頁匯入封包**：[LIHUO WEB CASE TXT V0.4](./neural-networks-are-already-clean-cammarata-2026.txt)  
**審稿建議**：**MAJOR REVISION**（參考級學術意見，非期刊正式決定）。

## 0. 審查法位及真實執行聲明

本報告保存 **可見、來源支持的論文審查和參考級週期**，不冒充已接入 Host 的正式理火系統。已進行網路原文與批評／重測文本比較，未獨立重跑大型模型實驗，亦無正式 Main / O9 / I9 / Lighter 的機器執行回執。

| 項目 | 實際狀態 |
|---|---|
| 論文身份、來源與公開重測比對 | 已完成可見來源審查 |
| Q0 前提與命題拆分 | 已完成文字審查 |
| 候選 A/B/C 的多輪重審 | R1-REF、R2-REF、R3-REF 具可見紀錄 |
| O9 的暗區辨認 | O9-REF 文字分析，非真燈態 |
| 正式 I9 干預 | **無合法觸發／執行證據** |
| 正式 Main 週期和合格兩連勝 | **未建立** |
| Lighter admission / Final Gate / Release | **未執行；沒有正式裁決或收據** |
| 獨立神經網路實驗重現 | **未執行** |

這個區分不是否認研究過程產生的可觀察效果：本審查確有可見的觀點轉變；但它本身不能創造特定正式模組已實際執行的憑證。正式 HOLD 也不應在 Final Gate 根本沒有執行時被虛構。

## 1. SOURCE_SCOPE_LOCK｜來源與時點

- **S1**：[Goodfire / Cammarata 原文](https://already-clean.goodfire.com/)：作者的論述、視覺及語言模型神經元案例、局部迴路干預、初步 Qwen3-32B 估計。文章自行定位為工作假說。
- **S1a**：[Goodfire neuron gallery](https://already-clean.goodfire.com/neuron-scientist/papers/)：可讀神經元示例，但不是獨立驗證。
- **S2**：[OpenAI, Language models can explain neurons in language models](https://openai.com/index/language-models-can-explain-neurons-in-language-models/)（2023-05-09）：研究歷史背景；不能將 Goodfire 2026 文章說成 OpenAI 團隊發表。
- **S3**：[leogao, Neural networks are not already clean](https://www.lesswrong.com/posts/Dkh7pXKjoNWkkxQDz/neural-networks-are-not-already-clean)（2026-10-17）：技術性批評，特別針對標籤是否真能預測活化和下游行為。
- **S4**：[IRSI, Already Clean, retested](https://irsi.ai/notes/already-clean/)（2026-10-18 更新）：獨立公開重測，既有支持也有不通過項目；報告有預先註冊、後補與執行限制，非同行評審。
- **S5**：[Andriy Batutin, We Tried to Confirm … The Controls Said No](https://andriybatutin.substack.com/p/we-tried-to-confirm-neural-networks)（2026-10-19）：小型模型重測、隨機基線與因果標籤檢查，亦未經同行評審。

**證據截至**：2026-10-23。此次文字審查未檢查所有原始神經網路權重、訓練資料與完整可重跑程式。

## 2. Q0 FRAME｜明確審查命題

原文中的 clean 主要指神經元或電路的可讀性，而不是無偏見、訓練資料乾淨、已對齊或模型安全性。

| 命題 | 初步審查狀態 |
|---|---|
| C1 經典多義神經元的部分原始解釋曾失準 | 值得支持的局部重新詮釋 |
| C2 原生神經元軸在某些測量中有特殊結構 | 有有限正面證據 |
| C3 90% 左右神經元極性具有一項主要功能 | 方法與分類定義敏感，未成普遍定律 |
| C4 弱活化／旁支基本不重要 | 部分反證，需明確限定模型與操作 |
| C5 recursive generalization 廣義取代 superposition | 仍待能區分機制的對照實驗 |
| C6 大型網路已普遍乾淨且容易全面理解 | 目前缺乏相稱實證 |

**關鍵不等號**：可解釋的高峰案例 ≠ 完整活化區間的預測 ≠ 下游因果作用的正確預測 ≠ 整個模型機制已明瞭。

## 3. EVIDENCE MATRIX｜主要結果與限制

| 類別 | 正面資料 | 反對資料與邊界 |
|---|---|---|
| 神經元軸的意義 | S1 個別神經元及迴路；S4 稀疏旋轉重測在所測模型多次找回原生軸；S5 部分尖峰表現優於隨機方向 | 不能從原生軸特殊性推出整體因果可解釋 |
| 單一工作比例 | S1 Qwen3-32B 初步約 90% | S4 對 Goodfire 文本以自己事先設定的標準得到 78.3%；方法不同，不是直接證偽 |
| 解釋器陰性控制 | S1 的典型高活化語義命名 | S5 隨機初始化神經元 84% 亦被命名為 one job，受訓神經元僅 52%；分類標籤本身不宜直接當證據 |
| 不同活化區間的預測 | S4 在其測法下部分 Goodfire 解釋可預測正向高峰 | S5 小模型高峰 r 約 0.26，弱活化區段接近零；需統一測量協議 |
| 下游行為因果預測 | S1 提供個別迴路操控示例 | S5 在其標籤預測的下游結果中 0/50 超過配對對照；不同模型與測法不可直接合併 |
| 弱活化移除 | S1 某些視覺設定呈現小損失 | S4 在多個不同模型／設定測得效能影響；不能宣稱普遍無關 |
| 跨尺度普遍性 | 原作者提出具前景的機制研究方向 | 缺乏充分獨立、跨模型、跨層全面因果審查 |

## 4. R1-REF｜初次可見競爭

**問題**：原作者是否足以反駁神經網路本來普遍混亂、無法直接按神經元研究的強烈悲觀說？

提出三條可獨立審查的候選：

- **A**：廣義 clean 假說，許多神經元已有清楚主要功能，昔日 polysemanticity 敘事有系統性誤判。
- **B**：局部神經元／迴路可能相當可讀，但比例、弱活化、跨模型因果推論還不足以證成廣義結論。
- **C**：分散式／superposition 機制仍可能對不少現象重要，不能被過早排除。

**R1-REF 暫定方向：A。** 原作者提出的視覺、語言與局部操控例子，確實削弱全面不可讀的過度悲觀敘事。

**完整性聲明**：本輪是先接觸批評材料後，刻意將評估焦點放回原作者證據所重建的 first-pass view；並非對外部反證完全盲態、先行封存的正式 R1。其領先不創造正式站位。

## 5. O9-REF｜觀察競爭盲點

文字層觀察到 A 有較大的敘事亮度，而容易弱化四種競爭對象：

1. 標籤器即使面對隨機初始化神經元，也可能輸出高度流暢的單一功能標籤。
2. 最高活化峰值的解釋可能無法外推到一般或較弱活化輸入。
3. 描述「什麼會讓神經元活化」不等於「這個神經元對下游輸出做了什麼」。
4. 局部已展示的電路或視覺案例，不足以直接宣布大型模型全局都能被解釋。

這是**參考級 O9 式暗區觀察**，沒有真實 O9 主系統燈態、獨立封存或 Host receipt。

## 6. I9｜干預資格與界線

無正式 I9 觸發、權限核定或調燈執行證據。

在本次參考級文字工作中，只把 S3、S4、S5 中原先較不顯眼的反例與陰性控制條件納入同一比較面；不把這個分析動作稱為真實 I9 intervention，也不聲稱可以覆寫 Host 規則。

## 7. R2-REF｜去掉 A 的先發優勢

重新設定為對所有候選都適用的證據要求：

- 能否以陰性控制排除標籤器對任意資料補全合理故事？
- 能否在未曾用來生成標籤的 held-out activation 上預測活化與方向？
- 能否跨不同活化區間保有解釋力？
- 能否以事前預測的神經元操作，預測下游行為而不是事後命名？
- 能否在相稱尺度／架構／分層上重複？

S4 一方面承認原生軸有部分優勢，一方面將原文 90% 的說法置於定義敏感邊界；S5 的隨機初始化標籤與下游因果檢查顯著削弱單靠語義標籤做出廣義結論的資格。

**R2-REF 的暫定領先轉為 B**：局部結構有證據；普遍性與完整因果機制尚未證成。這是實際可見的文字重審判斷變化，但不是正式 Main R2 狀態機 receipt。

## 8. R3-REF｜逆轉後事件式再挑戰

由於 R2 A→B 逆轉，B 此時只有一次參考級領先；因此再次用**最有利於 A 的資料**挑戰 B：

- 原作者不只展示語言標籤，也有具體神經元／迴路的干預與反事實操作。
- S4 在多項測試支持原生神經元軸在稀疏旋轉與高峰活化上有特殊性。
- S5 也不表示所有原生神經元軸都等同任意方向，部分局部峰值仍有預測訊號。
- C 的「superposition 普遍支配」不能直接因 A 的強主張受挫便視為成立。

**R3-REF：B 保持最能同時解釋支持與反對資料的限定審查結論。**

可見分析順序為 R1 A → R2 B → R3 B。這**不能**宣稱通過 Main V5.1.1 的正式 qualified unique-top 兩連勝：R1 非獨立封存；缺 Main/O9 合法 runtime 以及 Lighter 對正式週期的入場核定。

## 9. 參考級收束／正式停止邊界

本次截至 2026-10-23 的**公開材料文本審查**已有足夠證據，提出附條件的編輯性建議；並沒有透過這次工作解決 recursive generalization 與 superposition 的完整機制爭論。

- 可停止：本次文本審查與發布可見分析成果。
- 不得宣稱：正式 Main termination、Lighter Final Gate、正式 HOLD/RELEASE、模型實驗已完成、機制已全域被證明。
- 需新證據：同標準 32B 陰性對照、全活化區間預測、跨層干預、跨模型重現及對抗性理論區分測試。

## 10. 審稿建議：Major Revision

按實證學術論文標準，要求作者：

1. 明確定義 clean、one job、神經元極性及抽樣母體，公布評分類別、閾值、盲化與一致性。
2. 同一 pipeline 測試 random initialization、random directions、shuffled labels、explanation swap 等對照。
3. 報告最強、高中低活化與 near misses 的 held-out 預測，而非僅挑選典型峰值。
4. 先以解釋預測下游 token/輸出方向及效應大小，再做 ablation、amplification、matched-control 對照。
5. 設計 recursive generalization 與 superposition 兩者不同的可驗證預測。
6. 不同模型規模、架構和層次上重複測試，保存反例及失敗資料。
7. 對樣本選擇、解釋器、模型／參數／工具及計算步驟提供可重現工件。
8. 將局部神經元可讀性與全網路可理解性、AI 安全性分開；摘要與標題清楚保留 working-hypothesis 法位。

## 11. 最終判斷與留存

**可支持**：部分神經元及局部迴路比過去某些強悲觀敘事更具有可研究性／可解釋性；原生神經元軸的特殊性有若干獨立重測支持。

**尚不可支持**：多數神經元在所有語境都具一項功能；所有弱活化都不重要；recursive generalization 已普遍淘汰 superposition；大型網路內部機制已普遍理解或安全。

**參考級審稿意見：MAJOR REVISION。** 其效力僅及於這份已標示資料與日期的學術審查；不是期刊決定或正式理火系統准出。

---
LIHUO T5 reference-level review / visible cycle appendix · 2026-10-23
