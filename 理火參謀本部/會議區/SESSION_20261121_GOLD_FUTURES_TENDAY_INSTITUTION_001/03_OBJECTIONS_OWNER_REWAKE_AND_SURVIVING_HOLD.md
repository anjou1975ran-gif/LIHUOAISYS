# 03｜Council Round 002：真实异议、一次 owner re-wake 与合法保持判断
**Execution:** SAME_MODEL_MULTI_ROLE_REFERENCE；没有第二轮强制六席轮发言；其余席按是否出现 Material Delta 决定醒不醒。`COUNCIL ROUND != L8 R1/R2/R3+`。

## O1｜资格审查专家对探索专家的反弹判断
- ORIGIN=C; TARGET_OWNER=A; TARGET_CLAIM=“价格已经跌得很多，是否构成做多证据？”
- SOURCE: S01（当周约-9.4%，宏观及流动性抛售），S06（历史价不是下周可执行价），S17（跨市场去杠杆）。
- DELIVERED：本轮挑战已在可见文本呈交。DELIVERED != CONSUMED。
- OWNED_RESPONSE：探索专家指出初轮R1已有“超跌立即抄底”候选竞争，但其**初轮R2**早已因相同来源否定无条件买入，最终立场为等待确认。因本轮没有新的足以改变立场的材料，`NO MATERIAL DELTA → NO MATERIAL REWAKE`。
- MATERIAL_EFFECT=NONE_NEW; PROPOSAL_EFFECT=KEEP_WITH_CLARIFICATION。
- CURRENT_STATE=SCOPED_RESPONSE, NOT_AGREEMENT; REMAINDER=市场真实底部证据缺口。
- **Anti-theater audit:** 不能写成“C本轮说服A改判”，那会将初轮原已完成的修正倒写成第二轮新因果。会议 Word 已按此修正。

## O2｜成本专家反对架构专家的追空风险
- ORIGIN=E; TARGET_OWNER=B; TARGET_CLAIM=宏观偏弱是否足以在暴跌低位立即追空？
- MATERIAL_BASIS：S01 近一成周跌幅、S06单日宽波幅；多空挤仓风险、美元保证金与短时价差是新而具体的执行风险约束。
- ADMITTED_MATERIAL_DELTA：B 初轮提出状态区分，但未明确设置至少2:1预期风险收益与回抽失败的条件。E要求补上盈亏结构及滑点约束。
- OWNER_RESPONSE：将“确认弱势”变成能审核的条件：有回抽失败或破低再确认；预计收益距离必须至少覆盖计划风险及交易成本的两倍；否则持仓权撤销。

## O3｜执行专家指出2026年12月黄金合约交割风险
- ORIGIN=D; TARGET_OWNER=B; TARGET_CLAIM=任何十日策略若忽略GCZ26 11月30日首个交割通知日会产生致命执行错误。
- MATERIAL_BASIS=S07、S03、S16，且GCZ26与GCG27合约历史结算不可混用，S01与S06。
- OWNER_RESPONSE：同一 B 席第二轮Material Wake把执行研究锚点转到GCG27，既有GCZ26持仓要求在经纪商较早截止前处理；除非经批准有实物交割权限，不等至11月30日。

## B｜一次 owner-specific L8 material re-invocation（同时消费 O2+O3）
- CYCLE: GOLD10-L8-B-R002, OWNER=B。
- **R1 competitor**：原“看空趋势即可择机卖空”；候选“合约正确、回抽失败或破低确认、并通过风险收益及滑点约束后才可卖空”。
- **O9（可见文本）**：预测方向容易抢先遮蔽合约操作与尾部损失，I9未触发；没有hidden state测量。
- **T1 source**：E提交近周下跌S01、单日波幅S06与预算风险；D提交S07/FND与S03假日、S16经纪商提前强平。
- **R2（owner消耗）**：明确修正为 GCG27 研究执行基准＋条件空头；执行时用实时价、成交、深度、动态保证金重核。
- **T2**：若市场数据转向且价格突破GCG27上一日高、美元回落，则可能出现快速反弹；不因偏弱趋势堵死多头研究槽。
- **POST-R2 PREMISE AUDIT**：宏观方向、技术走势、合约结算、交易成本、风险授权五类前提不能互推。
- **R3 cross-premise**：优先消除非交易观点错误（合约交割、权限、实时价），再用两倍预期风险收益与最大损失预算筛选方向交易；不能满足则无交易。
- **TM**：只保留“条件空头、条件多头、零仓位”三条互斥方案，基准GCG27；GCZ26交割风险独立治理。
- **SGER**：origin B；targets O2/E、O3/D；qualifying basis S01 S03 S06 S07 S16；R1竞争、T1来源、R2修订、T2反作用、R3跨前提均有可见文本；未承诺真实回测胜率。
- **COMPACT RECEIPT**：GOLD10-L8-B-R002；R1/O9/T1/R2/T2/postR2/R3/TM=VISIBLE_DOCUMENT_REFERENCE；SGER=THIS_FILE；independent_provider=NO；runtime_host_binding=NO；material_owner_change=YES。

## 其他责任席与重大保留
- A：KEEP_WITH_CLARIFICATION，初轮已拒绝超跌即买，**不假造第二次改判**。
- C：HOLD 对任何明确价格预测、未经实时验证的交易资格及后验统计胜率；并不阻止条件研究。无新增资格依据，QUIET 合法。
- D：合约通知日与券商时点风险均仍未关闭，要等待真实账户检查。QUIET 在本轮不等于认可实际交易。
- E：批准的风控预算未知，演示金额不是交易权限；维持立场不需强行重醒。
- N1：无信号时保持零仓位为有效的基准决定；QUIET != CONSENSUS。

## Current checkpoint
`RESEARCH_STRATEGY_PREPARED`；`NOT_ENGINEERING_BACKTESTED`；`NOT_TRADING_AUTHORIZED`；`STAGE_2B_NOT_RUN`；`CUTOFF_2026-11-21`。不写“利润证明”与未来数据。人类最小决定是是否另行批准十日监控与条件执行框架，而不是由报告自动下单。
