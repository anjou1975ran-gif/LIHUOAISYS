# 00｜2026年台湾地区六都市长选举：研究入口与来源锁
**日期：** 2026-11-21（Asia/Taipei）
**用户原始请求：**「我想來測試下一個題目，更高風險的……預測台灣地區市長選舉，依然簡體中文輸出」；承接此前 Word 投资及政治研究报告工作流。
**D1解释状态：** `SECRETARY_INTERPRETATION_HUMAN_UNCONFIRMED`；任务视为公共政策与选举信息研究／简体中文报告。用户未在本条明确要求开启 CURRENT Staff-HQ formal Council Session，因此本次为 `SAME_MODEL_MULTI_ROLE_REFERENCE / RESEARCH_PROJECTION`，**不是正式 Canonical Council Event 录入，也不是六套独立专家 provider 调用**。
**研究范围：** 六个直辖市：台北、新北、桃园、台中、台南、高雄；其他16县市长选举存在，不声称本报告已覆盖全部22个县市。
**时间切片：** 截至2026-11-21，投票日2026-11-28。该日期之后发生的新闻、开票结果及人类判断不得回铸当时。
**外部报告语言：** 简体中文，内部出处保留原文 URL。
**输出：** `2026台湾地区六都市长选举_理火参谋本部政策情景与证据审查报告_20261121.docx`，**12页、11张表、18项查验来源**；本对话 sandbox 已生成并检查，Git 未保存 Word 二进制文件。

## 法律与证据硬锁
1. 台湾地区选举主管机关确认2026-11-28投票，2026-10-16审定六都23名市长候选人。
2. 《公职人员选举罢免法》第53条：2026-11-18 00:00至11-28 16:00不得发布、报道、散布、评论或引述选举民意调查资料，包括其法规范围内的旧数据和仿造民调外观的数据。原始官方说明： https://info.cec.gov.tw/vote2026/article/content/?id=M0092&target=%2Farticle%2FA0096
3. 本报告不提供任何个人胜选概率、胜负次序、得票率、候选人优劣评价或政治背书；专注全体正式候选人及可核实政策和行政情景。
4. 角色“资格审查专家、常识审查专家”等仅是本模型内部分析责任的对外别名，不是独立真人或不同模型。
5. 候选人政见≠完成政策；先后顺序≠原因；媒体转述的指控≠确立的违法事实；报告≠人类决策批准。

## Source Lock（18项）
01 https://info.cec.gov.tw/vote2026/ — election overview
02 https://info.cec.gov.tw/vote2026/article/content/?id=M0092&target=%2Farticle%2FA0096 — polling blackout Q&A
03 https://web.cec.gov.tw/central/article/65212 — 2026-10-16 approved six-mayor candidate list
04 https://law.cec.gov.tw/LawContent.aspx?id=GL000292 — public election law art.53
05 https://www.cna.com.tw/news/aipl/202609045002.aspx — candidate registration list (not substituted for approved list)
06 https://news.pts.org.tw/article/836749 — 2026-11-21 Taipei platform forum
07 https://www.businessweekly.com.tw/focus/blog/3023601 — Taipei policy source comparison
08 https://news.pts.org.tw/article/835570 — New Taipei three candidates policy forum
09 https://www.cna.com.tw/news/aloc/202611130116.aspx — New Taipei administrative staffing
10 https://www.businessweekly.com.tw/focus/blog/3023603 — New Taipei housing and transport comparison
11 https://www.cna.com.tw/news/aipl/202611170053.aspx — Taoyuan transport forum
12 https://news.pts.org.tw/article/836063 — Taoyuan platform forum
13 https://www.cna.com.tw/news/aloc/202611170312.aspx — Taichung three candidates
14 https://news.pts.org.tw/article/836220 — Taichung governance / welfare
15 https://news.pts.org.tw/article/836747 — Tainan platform forum
16 https://election2026.rti.org.tw/news/1052078.html — Tainan candidates forum
17 https://news.pts.org.tw/article/835748 — Kaohsiung AI / industry / regional policy
18 https://www.cna.com.tw/news/aloc/202611140167.aspx — Kaohsiung candidates forum

## 來源範圍與可信度
政府选务和法条为第一层；正式政见、公办发表会为第二层；署名有日期的媒体报道为第三层；研究者提出的行政情景和核验问题为第四层。四层不得彼此自动升格。公开链接并不等于已在本次证明所有政策可行或胜选结果。Word 附录内有全部来源的简体中文说明与原始链接。

## 第三方可追查与公开边界
候选人 23 名（简体显示）：
- 台北市6：郭玺、沈伯洋、萧文乾、唐新民、蒋万安、林志成
- 新北市3：苏巧慧、李四川、苏辉湟
- 桃园市2：张善政、黄世杰
- 台中市3：何欣纯、江启臣、洪丽华
- 台南市4：谢龙介、萧燐洪、叶人文、陈亭妃
- 高雄市5：张静、赖瑞隆、王肇民、柯志恩、洪方隆

**Not validated:** election winners, vote counts, election-time poll comparisons, independent six-agent runtime, third-party human comprehension trial, deployment. **Current Staff-HQ / Protocol / LIHUOOS / L9 Registry changed: NO.**
