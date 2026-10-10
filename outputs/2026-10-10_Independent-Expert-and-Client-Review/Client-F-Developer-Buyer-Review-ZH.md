# 客户 F 独立首轮审查：开发商 / 大型电力买方（ERCOT）视角

- 审查者角色：美国公用事业级开发商的投资负责人，或 ERCOT 大型电力买方（如数据中心运营商）的采购负责人；第一次阅读本报告。
- 审查对象：SOLAR-001 "Closure-integrated candidate edition"，9 October 2026，73 页 PDF（及对应 Markdown）。
- 审查依据：共同事实包；任务书 §4（适用边界）和 §6（严重性与结论标准）。
- 实际读取：PDF 文本（按物理页）、带行号的 Markdown；PDF 第 1–4、39–41、50–51 页的页面图像；PDF 书签结构；`scenario-versions/data/VPPA-Breakeven-Strikes.csv`、`VPPA-Route-Scenarios.csv`（前几行）、`HB_WEST-2026-JanSep-Post-RTCB-Context.csv`；`data/supplement/C/C_ercot_large_load_queue_status_by_year_2026-03.csv`。
- 未读取：其他审查者的输出。没有重跑模型，没有联网，也没有新增数据。下文的"审查者算术"只是简单核对。
- 引文保留英文原文。页码均为 PDF 物理页；行号对应 `REPORT_MD_WITH_LINE_NUMBERS.txt`。

---

## 一、总体印象（以首次阅读的买方或开发商身份）

1. **资本回收条件能否很快读懂：基本可以。** 第 3–4 页的 Key findings 和 Table 1-1 在两页内给出了几个关键数字：LCOE $48.9/MWh 对应已交付电量加权价 $26.4/MWh，NPV −$86.0m，固定价盈亏平衡约 $66/MWh，节点路线盈亏平衡 CAPEX $577/kWac，首年零 NPV 所需收入 $12.1m。第 50 页的 Table 11-1 和第 51 页的 Figure 11-2 用三种贴现率和二维网格把这些条件讲得比较透。我抽查了几项算术，结果一致（见第四部分）。按投资委员会的习惯，"要多少电价、多低的造价才能回本"这个问题在报告里能找到直接答案。
2. **价格和合同的区别：正文讲得很好，但摘要层面没有讲完整。** 第 10.3 节（第 39–40 页）区分了节点销售、简化固定价付费和以 hub 结算的金融对冲，并给出 G × node + H × (K − hub) 的结算恒等式。B.2 节的风险分配表（第 68 页）也很实用。问题在于：对买方最相关的 hub 结算 VPPA 盈亏平衡执行价（$60.6–$84.8/MWh）没有进入摘要和 Table 1-1，摘要第 5 条的措辞甚至让人以为这项计算还没做（见 F-01）。
3. **适用边界：大体守住了。** 报告反复写明假设电站不是 Taygete II，2023 年的正 NPV 依赖尖峰时段，NPV 是税前、无杠杆口径，节点占比不是盈利概率，而且没有给出"典型 IRR"。没有发现把条件情景说成投资建议或价格预测的核心表述。下面几处措辞或标签可能让首次阅读的买方高估确定性：摘要中的 −$50.59m（F-02）、"Realized sales price"（F-05），以及模拟出力高于运营同类电站这一点没有出现在摘要里（F-03）。
4. **对电力买方的导航与尽调问题：明显弱于对制造商的部分。** 制造商有 13.1 节的采购合同问题清单，电力买方的 13.4 节只有两段话，阅读导航表里也没有"买电或签对冲合同的一方"这一行（F-04）。报告其实已经有足够材料，可以拼出买方的尽调清单。
5. **图表与术语：总体清楚。** Figure 11-2 的零 NPV 斜线和 Table 11-1 一致。IRR 多根问题处理得规范。PDF 有完整的章节书签，弥补了目录只列到章级的不足。只发现若干 P2 级标签问题。

---

## 二、Findings

### F-01（P1）摘要和关键数字表遗漏了 hub 结算对冲（VPPA）的盈亏平衡结果，摘要第 5 条还暗示这项计算没有做

- **页码 / 行号**：PDF 第 3 页（摘要第 5 条）、第 4 页（Table 1-1）、第 40 页；MD §1.1 第 32 行、§1.2 第 39–52 行、§10.3 第 720–722 行。
- **短原句**："A hub contract therefore needs its own settlement calculation; switching benchmarks is not automatically an improvement."
- **问题**：报告在 §10.3 已经给出单独版本化的 HB_WEST 对冲计算："the break-even flat nominal strike ranges from **$60.6/MWh** to **$84.8/MWh** across the eight tenor, dispatch and negative-hub-clause combinations"；10 年期时，商业尾段约占收入现值的 43%。数据中心买方签的通常是 hub 结算的 VPPA，这是他们最想看到的数字。但摘要只说 hub 合同"需要自己的结算计算"，Table 1-1 只列了节点固定价的 $66/MWh。买方很可能把 $66 当作"VPPA 的回本价"。
- **证据**：MD 第 722 行；`scenario-versions/data/VPPA-Breakeven-Strikes.csv` 中 2025 路径、贴现率 0.0427 的八个组合为 60.57–84.77。审查者核对后与正文一致。
- **客户后果**：采购方会拿节点固定价的盈亏平衡价（$66，含 15.24% 不付费电量）去对照 hub VPPA 报价，两者机制不同，而且后者高度依赖未经来源支持的商业尾段价格。结果是低估开发商在 hub 结构下要求的执行价区间，也忽视了 basis 和负价条款的作用。
- **最小改法**：(a) 把摘要第 5 条最后一句改为："A hub-settled contract needs its own settlement calculation: in a separately versioned HB_WEST hedge setting (Section 10.3), break-even flat nominal strikes range from $60.6 to $84.8/MWh at 4.27% real, depending on tenor, dispatch and negative-price clauses, and depend heavily on the assumed merchant tail. Neither figure is an observed offer." (b) 在 Table 1-1 增加一行："Hub-hedge break-even strike (separate version) | $60.6–$84.8/MWh | 2025 path, 10–15-yr tenor + node merchant tail; 10.3"。
- **是否改变现有数字**：N（只是把已有数字搬进摘要）
- **信心**：High
- **是否在范围内**：Y

### F-02（P1）摘要中"含税收抵免"的 NPV −$50.59m 没有在同一句里说明它不是税后 NPV

- **页码 / 行号**：PDF 第 4 页；MD §1.1 第 35 行（另见 §10.8 第 822、840 行，§11.7 Table 11-3 第 982 行）。
- **短原句**："Its present value is **$35.38m**, leaving reference-node NPV at **−$50.59m**. Eligibility remains unproven"
- **问题**：−$50.59m 的算法是"税前、无杠杆 NPV + 一笔假设的 30% ITC 现值"。它没有计入所得税、折旧税盾，也没有计入 §50(c)(3) 规定的基数扣减。§10.8 第 840 行对此写得很清楚（"This edition does not claim the illustration is a complete after-tax NPV"），但摘要这一句只提示了"资格未证实"，没有提示口径混合。开发商的投资委员会习惯看税后数字，粗体的 −$50.59m 很容易被当作"税后项目 NPV"或"拿到 ITC 后的缺口"。
- **证据**：MD 第 690 行（税前范围）、第 840 行、第 842 行；Table 11-3 第 982 行已注明 "not complete after-tax DCF"。
- **客户后果**：读者可能误以为拿到 ITC 后还差约 $50m，于是把它当成融资或补贴谈判的目标缺口。实际的税后结果要看折旧、税负、转让折价和时点，方向和幅度都没有建模。
- **最小改法**：把该句改为："Its present value is $35.38m; adding it to the pre-tax reference NPV gives −$50.59m. This is a pre-tax NPV plus one illustrative credit, not an after-tax NPV: income tax, depreciation and the section 50(c) basis reduction are not modeled, and eligibility remains unproven."
- **是否改变现有数字**：N
- **信心**：High
- **是否在范围内**：Y

### F-03（P1）模拟出力高于所有筛选出的运营同类电站，这一点没有进入摘要或盈亏平衡说明，可能让买方低估所需电价

- **页码 / 行号**：PDF 第 37–38 页（§9.5）；第 4 页（§1.3 的 Limits 框，MD 第 66 行）；第 50 页（§11.3，MD 第 909–925 行）。MD §9.5 第 674、682 行。
- **短原句**："The simulated 2025 potential factor of 33.38% exceeds every observed plant in these screened cohorts."
- **问题**：§9.5 坦白说明了模拟的潜在容量因子是 33.38%，而 Pecos 筛选样本的中位数只有约 24.6–25.0%（交付口径 28.29% 落在三座较新电站的范围内），并说明"the simulated output is therefore not calibrated"。但摘要的 Limits 框只列了三条（单一价格参考、税前、历史年重复），没有提到出力未经校准且偏乐观。盈亏平衡价与付费电量大致成反比（报告自己的 paid-volume stress 就是 55.91 / (1 − u)），所以出力偏高会让 $66/MWh 偏低。
- **证据**：MD 第 674、682 行；第 712 行的付费电量缩放公式。
- **审查者算术（仅示意方向，不建议写入报告）**：如果付费电量比模型低 10%，固定价盈亏平衡价大约是 $66/0.9 ≈ $73/MWh。运营电站的净发电与模拟潜在出力边界不同，不能直接替换。
- **客户后果**：买方或开发商可能把 $66/MWh 当作"保守"的回本价。实际上，出力假设在同类样本里处于高位，NPV 为负的结论本身更稳健，但 $66 和 $577/kWac 这两个阈值在出力上并不保守。
- **最小改法**：在 §1.3 的 Limits 框加第 (4) 条："(4) Simulated output is uncalibrated: the 33.4% potential AC capacity factor exceeds every screened Pecos operating plant (medians about 25%), so break-even prices and costs are not conservative on volume (Section 9.5)." 并在 Table 11-1 的脚注加一句："Lower paid volume raises break-even prices approximately in inverse proportion (Section 10.3 paid-volume stress)."
- **是否改变现有数字**：N
- **信心**：Med。方向判断的信心高；能否直接比较受口径限制，报告已经披露。
- **是否在范围内**：Y

### F-04（P1）电力买方（如数据中心运营商）缺少导航入口和合同尽调问题清单

- **页码 / 行号**：PDF 第 3 页（阅读导航，MD 第 15–20 行）；第 61 页（§13.4，MD 第 1132–1136 行）；第 68 页（B.2 Contract risk allocation，MD 第 1323–1331 行）；第 70–72 页（Appendix C，MD 第 1365–1392 行）。
- **短原句**："Customer-specific procurement recommendations require evidence about the actual product and obligation, which has not yet been assembled."
- **问题**：Intended readership 明确包括 "electricity buyers"，但导航表只有 "Selling electricity to large loads"（卖方）这一行，没有买方入口。§13.4 只有两段原则性文字。制造商在 §13.1 有六问的采购合同问题表，开发商和买方没有类似的表。买方最有用的材料其实已经有了，只是分散在各处：§6.2 和 §6.6（产品定义、自供电容量构成）、§10.3（两条收入腿的恒等式、负价条款、VPPA 盈亏平衡）、B.2（三种结构的风险分配表）、Appendix C 的 FIN-03/FIN-11（合同字段、净收入项目）。首次阅读的买方很难自己把这些拼起来。
- **证据**：上述各处原文；缺口不需要新数据就能补上。
- **客户后果**：采购负责人会觉得报告"主要写给制造商"，错过最有价值的合同机制部分；或者只读第 1、6、8 章，就拿 $66/MWh 当谈判锚点。
- **最小改法**：(a) 导航表加一行："Buying electricity or hedges (e.g., data-center operator) | 1, 6.2, 6.6, 10.3, 11.3, 13.4, B.2 contract table, Appendix C"。(b) 在 §13.4 末尾加一张 "Questions for a PPA or hub-settled hedge" 表，只用已有字段：settlement point and hub（node-to-hub basis 由谁承担）；volume rule（as-generated、固定 shape 或 block）；negative-price clause（settle-through 还是 suspend，§10.3）；tenor 与之后的商业尾段（盈亏平衡对尾段很敏感）；REC 与能源是否分开签（Nestlé 案例说明 REC 期限不等于能源对冲期限）；QSE、偏差、uplift 费用由谁承担（Appendix C）；信用支持与抵押。(c) 把 B.2 风险分配表放到 §13.4 旁边，或在 §13.4 交叉引用它。
- **是否改变现有数字**：N
- **信心**：High
- **是否在范围内**：Y（只是重组和交叉引用已有材料，不是新的研究任务）

### F-05（P1）关键数字表把模型毛能源价值标成 "Realized sales price"，与报告自己的"毛值不是净收入"边界冲突

- **页码 / 行号**：PDF 第 4 页 Table 1-1；MD 第 45 行；另见第 3 页摘要第 1 条（MD 第 28 行 "earns $26.4/MWh"）。
- **短原句**："Realized sales price | $26.4/MWh | Reference node, stop exports below zero"
- **问题**：$26.4/MWh 是模拟出力乘以历史节点实时价格得到的交付电量加权毛能源价值。Appendix C 明确写着 "Modelled revenue is gross energy value"，Table C-1 FIN-11 的状态是 "Gross energy value only"。"Realized" 在采购和投资语境下通常指实际结算到手的价格。这是任务书 §4 点名必须分开的口径。
- **证据**：MD 第 1377、1385–1392 行；§8.2 第 561 行原本用的是 "delivered-energy-weighted price"。
- **客户后果**：买方或贷方可能以为这是某座电站实际结算的单价（甚至以为是 Taygete II 的实际数据），并把它当成扣除 QSE、偏差和损耗后的净价。
- **最小改法**：Table 1-1 改为 "Modeled gross delivered-energy-weighted price | $26.4/MWh | Reference-node prices × simulated output; before fees, imbalance and losses to settlement; 8.2"。摘要第 1 条的 "earns $26.4/MWh" 改为 "is modeled to receive a gross $26.4/MWh"。
- **是否改变现有数字**：N
- **信心**：High
- **是否在范围内**：Y

### F-06（P2）摘要把基准情景的 15.24% 不付费电量称作 "severe"，与第 10.3 节的标签不一致

- **页码 / 行号**：PDF 第 3 页；MD 第 29 行，对照第 706 行。
- **短原句**："breaks even near $66/MWh with the severe assumed 15.24% unpaid-energy deduction"
- **问题**：§10.3 和 Table 10-1 把 15.24% 定为 "Fixed base"，30.48% 才是 "downside … doubles the stress"。摘要把基准值称为 "severe"，读者会以为 $66 已经是压力上限。
- **客户后果**：买方会低估付费电量规则的下行空间（30.48% 时为 $80.43/MWh）。
- **最小改法**："…breaks even near $66/MWh with the assumed base 15.24% unpaid-energy stress ($80.4/MWh at 30.48%); paying for all potential generation lowers the threshold to $55.9/MWh."
- **是否改变现有数字**：N
- **信心**：High
- **是否在范围内**：Y

### F-07（P2）Table 10-2 的 "First-year delivered GWh" 在固定价路线下实际是付费电量

- **页码 / 行号**：PDF 第 41 页；MD 第 747–754 行。
- **短原句**："Fixed downside | 195.2 | 5.94 | … | 66.7"
- **问题**：固定价路线按潜在电量扣除不付费比例（§10.3："deducts 15.24% of potential energy from payment"）。审查者算术：292.4 GWh × (1 − 0.1524) ≈ 247.8 GWh，与 Fixed base 一栏吻合。所以固定价各行的 "delivered" 其实是付费电量，并不代表物理上少发了这么多。Fixed downside 的 LCOE $66.7 也是以付费电量作分母。Fixed downside 一行的潜在电量我没有单独核查（未能核查）。
- **客户后果**：买方可能误以为合同情景下电站会被物理弃电 30%，或把 66.7 和节点路线的 LCOE 直接比较。
- **最小改法**：列名改为 "First-year delivered (node) / paid (fixed) GWh"，或在表注加一句："For fixed routes, GWh is paid volume after the assumed unpaid share; LCOE uses the same denominator."
- **是否改变现有数字**：N
- **信心**：Med
- **是否在范围内**：Y

### F-08（P2）2026 年的负价占比没有写明价格位置，容易和参考节点 2025 年的 6.2% 混淆

- **页码 / 行号**：PDF 第 55 页；MD §11.8 第 1006 行（对照 §8.2 第 559 行）。
- **短原句**："Negative prices occur in 14.1% of 2026 intervals, against 7.7% in the 2025 months."
- **问题**：根据 `scenario-versions/data/HB_WEST-2026-JanSep-Post-RTCB-Context.csv`，这两个数字是 HB_WEST 在 1–9 月的数据（2026 年 Jan–Sep 行的 negative_interval_share 为 0.1412）。正文这一句没有写 "West hub"，也没有写 "January–September"。读者会拿它和 §8.2 中参考节点全年 6.2% 的数字比较。同一文件里 2026 年潜在出力落在负价时段的能量占比约 23.6%，对买方更有意义，但正文没有引用（是否补充由作者决定，不属于必改项）。
- **客户后果**：读者可能误读为"同一节点的负价频率翻倍"，或者看到 7.7% 与 6.2% 不一致而怀疑数据质量。
- **最小改法**："At the West hub, negative prices occur in 14.1% of January–September 2026 intervals, against 7.7% in the same months of 2025 (reference-node full-year 2025: 6.2%, Section 8.2)."
- **是否改变现有数字**：N
- **信心**：High（2026 年数值已核对；2025 年 7.7% 对应的行我没有逐行打开，未能核查）
- **是否在范围内**：Y

### F-09（P2）"238.6 GW requested versus 5.8 GW energized"：5.8 GW 其实包含在 238.6 GW 合计里

- **页码 / 行号**：PDF 第 4 页（摘要第 6 条，MD 第 33 行）；第 61 页（Table 13-1，MD 第 1150 行）；§6.5 第 458 行写法正确。
- **短原句**："238.6 GW requested versus about 5.8 GW observed energized; different measures"
- **问题**：`data/supplement/C/C_ercot_large_load_queue_status_by_year_2026-03.csv` 中 2030 列为：No Studies Submitted 130,303 MW；Under ERCOT Review 79,825 MW；Planning Studies Approved 19,482 MW；Approved to Energize 3,252 MW；Observed Energized 5,768 MW；TOTAL printed 238,630 MW。也就是说，5.8 GW 是 238.6 GW 合计的组成部分，不是另一个独立的量。§6.5 用 "total … in its 2030 large-load process table" 的写法是对的，摘要和 Table 13-1 中的 "requested versus" 让两者看起来像并列关系。
- **客户后果**：数据中心或开发商读者可能算出一个"申请量是通电量 41 倍"之类的比率，并把它当作转化率。
- **最小改法**：Table 13-1 改为 "238.6 GW total across all process statuses, of which about 5.8 GW is observed energized (noncoincident basis)"。摘要第 6 条同样改成 "of which"。
- **是否改变现有数字**：N
- **信心**：High
- **是否在范围内**：Y

### F-10（P2）副标题 "Market opportunities" 和摘要的 Limits 框没有挡住"光伏普遍不划算"这种误读

- **页码 / 行号**：PDF 第 1 页（封面副标题，MD 第 7 行）；第 4–5 页（§1.3 Limits 框，MD 第 66 行）。
- **短原句**："Market opportunities and commercial constraints in the context of data-center electricity demand"
- **问题**：报告没有量化任何市场机会，也没有建模数据中心买方的合同。这是正当的范围选择，但副标题会让数据中心买方期待买方侧经济性。另一方面，"not a market-wide finding about solar development"（§10.5 第 770 行）和 "do not prove that every solar project is uneconomic"（§14.4 第 1194 行）只出现在正文后部。摘要读者只看到"六个情景 NPV 全负"和"2024、2025 年只有 13 个和 2 个节点为正"，很容易得出"ERCOT 光伏不划算"的结论，而这正是任务书 §4 禁止支持的结论。
- **客户后果**：可能被内部转述为"顾问报告说 ERCOT 光伏投不了"。
- **最小改法**：(a) 副标题可改为 "Commercial conditions and constraints in the context of data-center electricity demand"，属于可选项。(b) 在 §1.3 的 Limits 框加一句："These are conditional results for one hypothetical system; they do not show that solar projects in ERCOT are generally uneconomic."
- **是否改变现有数字**：N
- **信心**：Med
- **是否在范围内**：Y

---

## 三、已披露边界（不升级，不需要修改）

| 项目 | 位置 | 判断 |
|---|---|---|
| 4.27% 实际贴现率偏低，不是市场 hurdle | §10.1 第 690–692 行；§10.9 第 870–872 行 | Disclosed limitation。报告给出了 6% 和 8% 的结果，并明确说明这不是 WACC。作为买方，我会自行看 8% 那一列。 |
| 没有真实合同条款、能源对冲价格和期限，也没有可比 IRR | Table C-1 FIN-01、FIN-03、FIN-10 | Disclosed limitation。Nestlé 的 15 年期限被正确标为 REC 期限而非能源对冲期限（第 726 行），处理得当。 |
| 净收入（QSE、偏差、REC）未建模 | Appendix C 第 1385–1392 行 | Disclosed limitation。只需按 F-05 修正摘要标签。 |
| 2026 年价格的最终性未逐行验证，也没有 2026 年回报 | §11.8 第 1000–1006 行 | Disclosed limitation。表述克制，正确。 |
| 没有 P50/P90，出力未经校准 | §9.5 第 682 行 | Disclosed limitation。正文已经说明，只需按 F-03 把它提到摘要。 |

## 四、抽查后认为无需修改的部分（审查者算术）

- 节点基准情景：15.47 × 6.55 − 187.3 ≈ −85.97，与 −$86.0m 一致。零 NPV 所需收入为 187.3 / 15.47 ≈ $12.1m；12.1 / 6.55 ≈ 1.85，与价格倍数 1.85 一致。2023 年中位数：15.47 × 18.56 − 187.3 ≈ +99.8，与 +$99.8m 一致。
- 盈亏平衡 CAPEX：(143.67 − 86.0) / 100 MW ≈ $577/kWac；6% 时 ≈ 484，8% 时 ≈ 404（表中为 403，属于四舍五入差异）；$40 固定价时 (143.67 − 73.7) ≈ 699。均一致。
- 2024 年 13 / 485 = 2.68%，2025 年 2 / 485 = 0.41%；尾部剔除后为负的 482 / 485 = 99.4%。均一致。
- ITC 示例：126.04 × 1.025 × 30% ÷ 1.025² ÷ 1.0427 ≈ 35.38；−86.0 + 35.38 ≈ −50.6。与正文一致（口径问题见 F-02）。
- 零价组件：10% 对应 3.76，按线性推到 100% 约为 37.6；−86.0 + 37.6 ≈ −48.4，与 "around −$48.3m" 一致。
- Figure 11-2（第 51 页）：在 1,437 那一行，$65 对应 −3、$70 对应 +11；在节点网格中，1.8× 对应 −5、2.0× 对应 +15。图表与 Table 11-1 一致，零 NPV 斜线位置合理。
- IRR 多根问题、2023 年尾部依赖、Taygete II 属性匹配和止赎事件的表述（§8.1）、hub 基准"不自动改善"的说法：均守住了边界，不需要修改。
- 导航：PDF 有到小节级的书签，可以弥补目录只列章级的不足。

## 五、给作者或我方团队的下一步尽调问题（报告已支持提出这些问题，不构成新研究任务）

1. 我们的实际结算点在哪里？到 HB_WEST 的 interval 级 basis 分布是什么样？报告提醒，年度加权 basis 小不代表 interval 级风险小。
2. 对方报价对应的是 as-generated、固定 shape 还是 block？负价时是 settle-through 还是 suspend？按 VPPA 情景说明，两者的差异约值 $12/MWh 的执行价，属于需要谈判的条款。
3. 合同期结束后的商业尾段由谁承担？用什么价格假设？10 年期时尾段约占收入现值的 43%。
4. 电站的 P50/P99 出力报告和第三方校准是什么情况？我们的盈亏平衡对出力高度敏感（F-03）。
5. REC 和能源是否分开签？期限分别多长？
6. ITC 的开工日期证据、material-assistance 比例、PWA 合规情况和转让价格如何？税后模型（含折旧和基数扣减）由谁出？
7. 并网设施的成本是否超过 16 TAC §25.195(f) 的限额？物业税实际负担是多少？FOM 中的置换准备金是否被重复计提？

---

## 六、总体结论

**② 完成所列最小编辑后可以移交。**

在任务书 §4 规定的用途内（初步商业筛选、比较合同机制、在明示假设下检验资本回收条件、提出尽调问题），这份报告对开发商和电力买方有实际价值，算术和图表经抽查一致，边界表述总体到位。我没有发现阻碍该用途的 P0。F-01 至 F-05 是摘要层面的标签、口径和导航问题，都可以用报告已有的数字和文字修正，不需要新数据，也不改变任何现有数字。修正后，首次阅读的买方能避免把节点固定价的盈亏平衡价当作 VPPA 回本价，避免把 −$50.59m 当作税后 NPV，也不会把 $26.4/MWh 当作实际结算价。F-06 至 F-10 是 P2 级措辞修订。

本结论不等于发布授权、销量保证或原 Version 1.0 验收。
