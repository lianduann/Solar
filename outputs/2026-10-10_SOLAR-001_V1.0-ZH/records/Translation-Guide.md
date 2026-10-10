# SOLAR-001 V1.0 中文版 翻译规范（供分章翻译使用）

源文件：/home/claude/work/v10/2026-10-10_SOLAR-001_V1.0/source/SOLAR-001_V1.0_Report-EN.md
输出：每个分块写成一个独立的 Markdown 文件（路径由任务指定），内容为对应英文段落的简体中文译文，结构逐行对应。

## 绝对规则
1. **所有数字、单位、符号一个不改**：$26.4/MWh、247.8 GWh、−$86.0m、4.27%、1,436.7、2023–2025、§25.195(f)、P.L. 119-21 等原样保留，包括负号 "−"、千分位逗号、en dash "–"、"$m"/"$bn"。不要把 $m 改成"百万美元"，保留 "$86.0m" 这种写法，可在首次出现处不加解释（"关于本报告"的 Conventions 段会说明）。
2. **来源标识符原样保留**：[S08]、[F01–F05]、[CL-FIN-04]、[M01]、[P01; P08; Sections 4.4 and 5.7] 中的 Sections 改成中文（见第 4 条），其它原样。URL、反引号里的文件名、`figures/...png` 路径原样。
3. **Markdown 结构原样**：标题层级（#/##/###）、表格（竖线、对齐行 |---|---:|）、列表、`::: lead` / `::: kpis` / `::: uses` / `:::` 块、引用块 `>`、粗体 `**…**`、斜体 `*…*`。表格行数、列数不变。
4. **结构标签改用中文格式（构建脚本按此解析，必须严格一致）**：
   - 章标题：`# 1. 执行摘要：……`（数字和点保留）；附录：`# 附录 A. 来源书目`；前言：`# 关于本报告 {.front}`（保留 `{.front}`）。
   - 节标题：`## 1.1 标题`、`## A.1 标题`、`### 小标题`。
   - 表题行：`**表 1-1. 标题。**`（"表"+半角空格+编号+"."+空格+标题，末尾句号可省）。
   - 图：`![图 1-1. 标题](figures/xxx.png)`。
   - 交叉引用：`Section 10.3` → `第 10.3 节`；`Sections 10.3 and 10.8` → `第 10.3 节和第 10.8 节`；`Sections 11.6–11.9` → `第 11.6–11.9 节`；`Table 1-2` → `表 1-2`；`Tables 10-5 and 10-6` → `表 10-5 和表 10-6`；`Figure 8-4` → `图 8-4`；`Appendix C` → `附录 C`；`Appendix B.2` → `附录 B.2`；`Chapter 12` → `第 12 章`；`Chapters 4–5` → `第 4–5 章`；`Box 1` → `方框 1`。编号与英文完全相同。
   - 引用块固定开头：`> **本章限制。** (1) …… (2) …… (3) ……`（保留 (1)(2)(3) 编号）；`> **方框 1. 如何阅读本报告中的数字。** ……`；`> **示意：生产型税收抵免。** ……`。
   - KPI 块每行 `数值 | 标签 | 说明` 三段格式不变。
   - 表注/图注用斜体段落：`*来源：……*`。
   - 关键发现编号列表 `1. **粗体标题。** 正文` 格式不变。
5. **不增不减**：不加解释、不加免责、不删句子。英文一句对应中文一句或两句。
6. **术语**：英文缩写首次出现给中文并保留缩写，之后可只用缩写。固定译法：
   - ERCOT 德州电力可靠性委员会（ERCOT）；settlement point 结算点；resource node 资源节点；hub 枢纽（HB_WEST 西部枢纽、HB_BUSAVG 母线平均枢纽，代码保留）；load zone 负荷区；TAYGETE2_ALL 保留；
   - capture price 捕获价格；capture ratio 捕获比；generation-weighted / output-weighted price 发电量加权价格；time-weighted 时间加权；negative price 负电价；curtailment 限电；basis（node-to-hub）节点—枢纽价差（基差）；
   - PPA 购电协议；VPPA 虚拟购电协议；hub-settled 枢纽结算；strike price 执行价；merchant tail 市场化尾期；tenor 期限；paid volume 付费电量；unpaid energy 未付费电量；
   - LCOE 平准化度电成本；NPV 净现值；IRR 内部收益率；pre-tax, unlevered 税前、无杠杆；real / nominal 实际 / 名义；discount rate 折现率；break-even 盈亏平衡；capital recovery 资本回收；CAPEX 资本支出；OCC 隔夜资本成本；GCC 并网成本；FOM 固定运维成本；
   - ITC 投资型税收抵免；PTC 生产型税收抵免；PWA 现行工资与学徒要求；45Y / 48E / 45X 保留；transferability 可转让；
   - MIP 最低进口价格；AD/CVD 反倾销与反补贴税；USITC 美国国际贸易委员会；CBP 美国海关与边境保护局；FEOC/PFE 受禁外国实体；material assistance 实质协助；
   - data center 数据中心；large load 大负荷；Batch Zero 保留；WLPUN 保留；interconnection 并网；
   - module 组件；cell 电池片；wafer 硅片；polysilicon 多晶硅；utility-scale 大型地面（公用事业规模）；MWac/MWdc 保留；DC/AC ratio 容配比；tracker 跟踪支架；BOS 系统平衡部件；
   - weather year 气象年；price year 价格年；common calendar 共同日历；resampling 重抽样；mixture 混合情景；tail stress 尾部压力测试；Shapley / LMDI 保留；
   - hypothesis 假设；open question 待解问题；controlled conclusion 结论；practical implication 实务含义；"Limits of this chapter" 本章限制；
   - 公司：LONGi 隆基、JinkoSolar 晶科、Trina 天合、JA Solar 晶澳、Tongwei 通威、Daqo 大全、Canadian Solar 阿特斯、First Solar 保留；
   - 机构：MIIT 工信部；IRENA 国际可再生能源署；NLR/NREL 保留（美国国家实验室）；DOE 美国能源部；EIA 美国能源信息署；LBNL/Berkeley Lab 劳伦斯伯克利国家实验室；IMM 独立市场监测机构；Lazard、LevelTen、Potomac Economics 保留；Comptroller 德州审计长办公室；PUCT 德州公用事业委员会。
7. **文体**：专业研究报告的简体中文，用中文标点（，。；：（）），数字与英文之间加半角空格习惯按中文排版可不加。保持原文的谨慎语气，不夸张。句子可以拆短，但意思不变。
8. 不翻译：front matter 里的 `organization: Lucid Direction Insights LLC`、`project: SOLAR-001`；公司名 Lucid Direction Insights 保留。
