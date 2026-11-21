# 05｜再入金价翻桌实验审计：Git readback、Word QA、归因与法位
**Date**：2026-11-21；**Session**：SESSION_20261121_GOLD_FUTURES_FLIP_REENTRY_002；**cutoff**：2026-11-21 22:05 Asia/Taipei；**window**：11/21—11/30，10个自然日。
**Runtime**：Formal Staff-HQ Vertical V0.1 / LIHUOOS V1.4.2；Enhanced A–K CP3 human report是2026-11-21 WORKING候选样式；无Current Cutover。
**Execution identity**：CHAT_NATIVE / SAME_MODEL_MULTI_ROLE_REFERENCE / NON_HOST；翻桌Agent没有独立Provider或独立模型调用证据。本次翻桌为源绑定研究方法，不是CORE-7/L9/Production。
**Original session kept**：SESSION_20261121_GOLD_FUTURES_TENDAY_INSTITUTION_001 未覆盖，本轮新Session追加再入资料。

## Git 五份源档验证
- 00_REENTRY_MANDATE_AND_SOURCE_LOCK.md sha `b89ca60c9fc37e4b48802abd7d062cab4ff6f6d5`：D0、D1未确认、初始框架和时间。
- 01_PROFESSIONAL_SOURCE_PACKET_AND_EVIDENCE_GAPS.md sha `7a80e30150845628c2247b0bc99485dff403e74f`：领域来源与可验/未知的分层，尤其CFTC官方网页缓存版本异议。
- 02_FLIP_SIGNAL_FIVE_OWNER_L8_SGER_AND_OBJECTIONS.md sha `bbd8e328a245f14794cd907fcf82748e40563f5b`：翻桌信号＋5个受材料影响责任席的可见文本L8参考周期、SGER、Compact Receipt；N1 QUIET，没有假称六人轮番改判。
- 03_CANONICAL_REFERENCE_TYPED_EVENTS.jsonl sha `30147d4a25c4740f024940450ab46d32f09792ca`：16个顺序连续可解析的参考Typed Events，GFLIP-EV-000至015，**不是生产Host-admitted事件处理系统**。
- 04_HUMAN_READABLE_ENHANCED_AK_REPORT_DERIVED.md sha `f2da42276088882534f7be66f8e525fc7e0436a1`：CP3派生A–K，不作为第二份Canonical。
以上Git文档均在main创建后逐份readback成功。本文自身要在写入后再独立fetch，才可说它也已持久。

## Word 二进制交付
- Exact path `/mnt/data/2026年11月最后十天黄金期货_翻桌式因果重构与机构策略报告_20261121.docx`。
- SHA256 `ef3d0eb0f5d40d647c1f4188d3563e4b71cc9c2fdda140e81095fca671ff0aaf`。
- 13页A4，14张结构化表格，25项来源记录（包括原始Flip研究源），46处标题级段落。
- 用document技能 `render_docx.py` 渲染13张PNG并进行全页接触图和页面非空检查，未见裁切、空白页、缺字/表格断裂；`a11y_audit.py` high=0、medium=0、low=0。
- **DOCX_GIT_PERSISTENCE=NOT_ATTEMPTED**；Git保存文本研究与审计，不保存Word二进制。仅此对话sandbox可下载原Word。内部PDF和PNG只是QA，不作为对外交付。
- 报告语言为**简体中文**，原始英文文献标题/网址经链接方式保留，正文使用自然的人类专业职责任称。

## 反向因果与主要缺口的审计
- 传统利率解释可以成立，但不是唯一因果：长期实际利率、美元、资金清算、订单簿和持仓结构可共同影响价格。
- 原始翻桌Nov19 memo提出的上游美元升息问题得到正面竞争；**美元升息≠财政自动印钞≠黄金十天必涨**，制度机制需要独立证据。
- 11/17 CFTC持仓及11月初WGC ETF观察早于11/20快速跌势；TEMPORAL / SECONDARY SOURCE，不能反写为当天清算记录。
- CFTC官网网页web-open缓存Aug04、搜索快照Nov17有冲突；报告显式来源版本差异，未沉默强制解决。
- CME提供可查工具≠实际取得11/20盘口深度；因此买盘真空机制仍是HYPOTHESIS/HOLD。
- 一手GC 100oz，GCG27 11/20历史结算$3544.10，5%逆向跳空每手$17,720.50；单笔1千万美元NAV×0.10%=$10,000预算；止损60美元+缓冲10美元→每手计划$7,000，2手$14,000超出。只是数学演示，不能拿来开真实账户。
- 新报告以11/21—11/30为合法时窗，明确12/01 ISM在窗口外；11/25 PCE/GDP数据未公布；11/30旧月FND及券商更早截止需要实核。
- MARKET DIRECTION != EXECUTABLE TRADE != APPROVED AUTHORITY。三种存活路径：空仓、条件性空头、条件性流动性修复反弹。

## Current未修改与人类权限
Current Staff-HQ Vertical V0.1 blob `1c23fe0feea77f2e546a08254d6a0e8b6d022583`、Secretariat V0.1 blob `8838bd91a7c201a2f769da8994b44ad5af021872`、Meeting Record V0.1 blob `eb588d7c0fc5cc337088d9f4d749f4a46d0f18ba` readback unchanged。
- `RESEARCH_DOCUMENT_COMPLETE`、`INDEPENDENT_EXPERT_AGENT_NOT_RUN`、`TRADING_EDGE_NOT_BACKTESTED`、`NOT_ENGINEERING_VALIDATED`、`NOT_COST_VALIDATED`、`NOT_HOST_DEPLOYED`。
- D1仍`SECRETARY_INTERPRETATION_HUMAN_UNCONFIRMED`，没有交易权限，`CHECKPOINT_ENDING`但不是`SESSION_END`；人类继续或沉默不是批准。
- Human smallest next decision：是否批准使用真实市场深度、期货保证金与账户合规数据完成盘前验证；**不是**直接授权买卖。
