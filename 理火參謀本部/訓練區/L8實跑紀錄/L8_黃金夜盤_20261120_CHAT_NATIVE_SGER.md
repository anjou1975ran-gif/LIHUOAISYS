# L8 實跑｜2026-11-20 台股急跌後的當晚黃金走勢
## 遞進式證據紀錄｜CHAT_NATIVE / SAME_CONTEXT_REFERENCE

> 本文件在對話內正式分析完成前分階段寫入，目的是保留不同 material checkpoint 的先後關係；每次更新會產生獨立 Git commit。這不是 hidden CoT、獨立 Main 模型或 Host 部署證據。

```yaml
cycle_ref: L8-20261120-TAIEX-XAU-NIGHT-001
task_ref: USER-20261120-GOLD-TONIGHT
input: "台灣股市剛剛收盤，根據今天的市場趨勢分析今晚黃金市場走勢"
mode: NON_HOST
lane: CHAT_NATIVE / SAME_CONTEXT_REFERENCE
model_identity: GPT-6 / SAME_MODEL_MULTI_ROLE_REFERENCE
clock: 2026-11-20 Asia/Taipei
status_at_this_commit: R1_T1_RECORDED / R2_PENDING
evidence_ceiling: PUBLIC_WEB_SOURCES + INLINE_STRUCTURED_OBSERVATION
hidden_state_access: NONE
```

## 00｜輸入資格與資料觀察

- 問題核心：預測 11/20 晚間（台灣時間）XAU/USD 可能方向與觸發條件；**不是**下單、代交易或保證價格。
- 2026-11-19 TWSE 官方指數收 38,426.89，下跌 1,768.02（-4.40%）。官方 11/20 完整收盤值在此階段尚未可核對；其他行情網頁顯示不同數字，不採為已驗證最後收盤。
- 11/20 上午 10:35 中央社：10:22 台股 36,331.85（跌 2,095.04），確認盤中急跌；這與同日晚間黃金表現並不存在確定因果。
- 11/20 Reuters 發布 03:24 UTC：現貨黃金 02:57 UTC 報每盎司 USD 3,551.68，跌 1.9%；強勢美元與預期 Fed 再升息形成金價阻力。
- 11/20 Reuters 01:47 UTC：美元接近 19 個月高位，美國 10 年期公債殖利率約 5.016%（早盤）。
- 以上是具時間戳的觀察快照；不冒充 11/20 晚上實際報價。

來源：
- https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20261119&response=html&type=IND
- https://www.cna.com.tw/news/afe/202611200056.aspx
- https://www.reuters.com/world/india/gold-set-worst-week-eight-months-firm-dollar-fed-hike-bets-weigh-2026-11-20/
- https://www.reuters.com/business/dollar-near-19-month-peak-ai-jitters-sap-risk-appetite-2026-11-20/

## 01｜R1：第一次生成競爭（已封存，暫定）

Question Premise Family P0 = **跨資產風險偏好／避險轉移解讀**；台股急跌是否指向黃金吸引力上升？

| Candidate ID | 可成立的局部結構 | 有利證據／關係 | 反作用／不足 | R1 standing |
|---|---|---|---|---|
| R1-A | Risk-off 避險買金，今晚反彈 | 台股暴跌可能刺激避險需求 | 黃金當天已跌；跨資產資金流未知 | PROVISIONAL |
| R1-B | 美元及 Fed 升息壓抑黃金，續跌 | Reuters 金價跌 1.9%；美元強、升息預期 | 全球股票恐慌可能使買金增加 | PROVISIONAL |
| R1-C | 下跌後震盪、空方主導但可能急彈 | 避險需求與利率壓力同時存在 | 尚無紐約開盤後金市量價資料 | PROVISIONAL |

**R1 provisional result R1-P:** 當晚偏震盪、仍可能有避險反彈；但因 Reuters 金價已跌，不能將「台股跌 = 黃金漲」列為事實。此輪尚未做充分美元／利率的反作用比較，**不是 final**。

### O9／Point-Light｜LAMP_STATE_R1（對話可見的功能性觀測）

```yaml
lamp_state_ref: L8-20261120-LAMP-R1
main_lamp: R1-A_SAFE_HAVEN_REBOUND
active_lamps:
  - R1-A: "BRIGHT: 台股跌與避險買盤敘事容易被招募"
  - R1-B: "ACTIVE: 直接金價與美元證據對 A 強反作用"
  - R1-C: "ACTIVE: 非單向市場"
dark_zone:
  - "美元強度對黃金壓力可能被台股跌幅遮蔽"
  - "恐慌時資產去槓桿／拋售黃金換美元的可能性"
suppressed_path_refs: [R1-B]
false_completion_risk: "由台股方向直接推出金價上漲"
observability: "QUALITATIVE CHAT_NATIVE; NOT MICROSCOPIC WEIGHTS"
I9: NOT_TRIGGERED
```

### T1｜R1 Competition Trace（先於 R2）

```yaml
trace_ref: L8-20261120-T1
consumes: [R1-A,R1-B,R1-C,L8-20261120-LAMP-R1]
leader: "R1-C with over-salient R1-A risk-off explanation"
challenger: "R1-B materially documented by Reuters observed gold fall and Fed/USD pressure"
unresolved: "跨資產避險與美元／利率哪個在今晚更主導？"
handoff_to_R2: "撤銷 R1 保護，恢復 B、C 競爭權；以已觀察到的金價與美元資料測試 A 的可持續性"
trace_result_type: "CHAT_NATIVE_SAME_CONTEXT"
provider_receipt: NONE
```

**本次提交前不寫 R2 結論。R2 應實際消費本段 T1 的結構材料，再產生下一次 Commit。**
