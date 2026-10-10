# 客户 E 第二轮：以制造商/出口商客户身份质询专家意见

- **角色：** 客户 E，中国组件制造商/出口商的战略或商务负责人，首次阅读本报告。
- **阅读范围：** Expert-A、B、C、D 的首轮审查。Client-F 的审查只用于对照与 VPPA 摘要相关的条目。
- **规则：** 与首轮相同。不重跑模型，不联网，不新增数据。自己做的算术标为“审查者算术”。核对过的原件和数据文件逐项注明路径。
- **基本立场：** 我关心的是前 4 页能否让一位制造商高管读完后做出正确判断。凡是让执行摘要再多出一串限定和数字的修改，我都要求放到对应正文或表格里，摘要只留一句加指引。

---

## 一、对专家条目的立场

### 1. 对制造商读者真正重要的条目（支持）

| 条目 | 立场 | 理由 | 对修改的影响 |
|---|---|---|---|
| **D-01**（基准组件 $0.29/Wdc 已扣除 45X 补贴，未扣前约 $0.36/Wdc） | **支持**，附一个条件 | 我已复核 `data/supplement/A/A_pvscm_item_level_pv_only.csv`：组件各项 MMP 加总为 291.214，其中 Subsidy 一行为 −68.88，不计该行时为 360.094（审查者算术，与 D 一致）。`A_module_passthrough_parameters.csv` 也写明 "incl. 45X subsidy; not a Chinese-origin delivered module"。对出口商来说，这是全报告最可能导致定价误判的一处。现在的写法让人以为 MIP 比美国本土组件成本高约 30%。**条件：** 正文只补充“未扣补贴前约 $0.36/Wdc（2024 美元）”这一事实，**不要**写成“差距只有 $0.02/W”这样的结论。原因有三：两者年份不同（2024 美元对 2026 名义值）；单位基础不同（Wdc 对 W）；MIP 是对首次公平交易售价的下限，并另加 15% 从价税和 AD/CVD。写成“$0.02 差距”会让销售团队得出“按 MIP 进口和美国本土组件差不多”的反向误读 | 采用 D-01 对第 411 行、图 5-1 图注和第 1103 行的改法。我的 E-04 措辞据此调整（见第二部分） |
| **D-02**（表 4-2 把 A 股“分行业”毛利和隆基“分产品”毛利混在“Segment margin”下） | **支持**，倾向于方案 (a) 加附注数字 | 已核对原件：Trina_2025_AR.txt 第 2476 行“光伏行业 4.60”、第 2487 行“光伏产品 −1.42”；JASolar 第 914 行“光伏组件 −4.03%”；LONGi 第 965 行“光伏行业 0.81”。对中国厂商读者来说，表 4-2 首先是**同业对标**表。按现有标签，读者会认为天合（4.6%）最健康、隆基组件（0.19%）偏弱，但按组件产品口径排序正好相反。这是我首轮没有发现、但对我方最重要的口径问题 | 第一选择是方案 (a)：只改标签，在附注列出产品线数字，现有数字不变。若作者选方案 (b)，即把表中数字改为产品线口径，我也接受，但需在附注保留原数字和口径说明 |
| **D-05**（印尼/老挝的进口份额在 2026 年已大幅下降，印度未被提及） | **支持** | 对出口商来说，“采购来源已经从老挝、印度移走”比“印尼、老挝仍是主要来源”更接近事实，对东南亚产能布局判断也更有用。改写后的句子仍是描述性的，没有作因果判断 | 采用 D-05 替换句，只改 §5.7 正文，不进摘要 |
| **D-08**（终裁中包含“紧急情况”肯定性认定） | **支持** | 我方在途和在签合同最怕追溯征税。改法只有一句，而且是条件式表述 | 采用，放在 §5.7 |
| **D-10**（出口退税取消只引用了一个未取得的网页） | **支持**，并据此修改我自己的 E-01 | P08 页面未取得，而 Daqo 20-F 的描述与报告不同。在来源加强之前，不宜把“4 月 1 日取消出口退税”作为确定事实放进执行摘要 | E-01 的摘要新增句删去出口退税一项（见第二部分）；§4.4 按 D-10 补充引用 LONGi 年报和 Jinko 20-F |
| **D-03**（Daqo 定期存款没有计入现金栏） | **支持**，但对我方优先级较低 | 修改正确。对制造商而言，表 4-3 的意义在于“美国买方会这样筛查供应商”，口径缺口会让净现金最充裕的公司看起来偏弱。改法是加一条附注，不改数字 | 采用 D-03 的附注 |
| **D-04**（把可能含非债务项目的一行称为“borrowing obligations”） | 支持 | 措辞更准确，篇幅不增加 | 采用 |
| **D-06 / D-07 / D-09**（来源标签和日期精度） | 支持 | 不影响阅读主线，属于证据标签层面的完善 | 采用，均为 P2 |
| **A-02 / F-05**（“Realized sales price”和“earns”实际是模型毛能源价值） | **支持** | 与我首轮的 E-06 指向同一个标签，A-02 的改法更准确 | 我放弃 E-06 中 "Delivered-energy-weighted market price" 的建议，改用 A-02 的标签 "Modelled gross energy value per delivered MWh"。E-06 的另一半（第 32 行说明 $22.13 是停发前的价格、$26.4 是停发后）仍保留 |
| **A-05**（48% 捕获率在横截面中接近第 3 百分位） | 支持 | 只改表 13-1 的一个单元格，避免读者把它当成通用经验值 | 采用 |
| **F-09**（5.8 GW 包含在 238.6 GW 合计内） | **支持** | 我首轮在第一部分写过“避免按 238.6 GW 估算需求”，但没有注意到摘要第 6 条的 "against" 和表 13-1 的 "versus" 会让读者算出“41 倍”这样的伪转化率。设备商的需求判断正好会用到这个比率 | 摘要第 6 条和表 13-1 都改为 "of which" |
| **A-04**（Taygete II 止赎缺少时间背景） | 支持（中等信心） | 能减少“真实电站止赎说明行业亏损”的推论，这也是任务书 §4 禁止的推论。我无法独立核对 C06/C09 原件 | 采用，措辞按 A 的条件式写法 |
| **C-03**（“485 个节点”是结算点，彼此可能重复） | **有条件支持** | 内容正确。但“约 400 个不同的三年收入组合”这样的数字只能放在 §8.4，**不能进摘要**，否则摘要第 4 条会变成方法学说明 | 只改 §8.4 和第 883 行 |
| **EB-01 / EB-04 / EB-05 / EB-07 / EB-09 / EB-10，C-01 / C-02 / C-04 至 C-09** | 无立场（中性） | 这些都不在制造商的阅读路径上（第 10、11 章的图表与方法标签），我无法以客户身份判断其重要性。只要不进摘要，不影响我的阅读 | 不反对 |

### 2. 可能使摘要更难读、让限定淹没要点的条目（有条件支持或要求合并）

我数了一下：如果 A-01、A-03、A-08、EB-02、EB-03、F-01、F-02、F-10、D-11 和我自己的 E-01、E-02 全部按原文写进 §1.1 至 §1.3，执行摘要会新增约 8 到 10 个数字和 5 到 6 句限定，篇幅增加约一半。多数补充要么属于开发商视角，要么是第三处重复。制造商读者会更难在第 3 页找到“这份报告对我意味着什么”。所以我建议**合并处理**：

| 条目 | 立场 | 理由 | 对修改的影响 |
|---|---|---|---|
| **A-01 / F-01**（摘要补充 hub 对冲 VPPA 的 $60.6–$84.8/MWh） | **有条件支持** | 对买方确实重要，我也认同 $66 不是 VPPA 回本价。但 A-01 建议放进第 2 条，F-01 建议放进第 5 条，Table 1-1 还要加一行，同一个区间会出现三次 | **只放一处：**第 2 条（与 $66 并列，便于对照），外加 Table 1-1 新增一行。第 5 条只加 "(see item 2 and Section 10.3)"。这样第 5 条就不会再暗示这项计算没有做（F-01 指出的问题） |
| **A-08 / EB-02 / F-06**（"severe" 一词） | 支持删除 "severe"，**有条件**接受 EB-02 的补充数字 | 三人意见一致，删掉一个形容词有利无害。但 EB-02 要在摘要里再加 "$80.4/MWh if that share doubles"，会让第 2 条出现 5 个价格数字 | 第 2 条采用合并措辞（见下）。$80.4 留在 §10.3 和 §11.3 |
| **EB-03 / F-02**（$35.38m 抵免的税率、时点和“非税后”限定） | **支持** | 对制造商也重要：它直接对应我的 E-03，即不能把 $35.38m 当作“用我们的设备就能拿到的抵免”。EB-03 的措辞清楚 | 采用 EB-03 改写的句子，但 "$7.08m at the 6% base rate" 可以视篇幅保留或删去，我倾向保留，因为它最直接地说明结果对条件敏感 |
| **A-03**（2025 基准年约 93% 的区间在 RTC+B 上线之前） | **有条件支持** | 事实重要。但如果把 "$18.24 vs $21.36" 和 "23.6% vs 13.7%" 写进 §1.3，制造商读者很容易把它读成“2026 年市场在恶化”的预测。这正是 A 自己想避免的误读，也会反过来强化“美国光伏不划算”的印象（我的 E-02） | §1.3 只加一句不带数字的说明："Most 2025 intervals predate ERCOT's December 2025 real-time co-optimisation launch; a 2026 price diagnostic, not a forecast, is in Section 11.8." 数字放在 §10.3 和 §11.8 |
| **F-10 (b) / E-02**（阻断“光伏普遍不划算”的推论） | 合并 | 我和 F 独立地发现了同一个问题，F 定为 P2，我定为 P1。位置上我仍主张放在 §1.1 的加粗首段，而不是 §1.3 的 Limits 框：PDF 第 4–5 页的 Limits 框是灰底小字，首次阅读的高管不会看 | 一句话，放在第 26 行末，措辞见第二部分。F-10 (a) 改副标题属于可选项，我不反对 |
| **D-11 / E-01**（摘要中加入 2026 年贸易事实） | 合并，采用 D-11 的位置 | D-11 建议把一句话接在第 3 条之后，比我建议的新增第 7 条更省篇幅，而且直接放在讨论组件价格传导的位置，逻辑更连贯 | 改用 D-11 的位置。措辞去掉出口退税（据 D-10），加入 D-01 的口径提示（见第二部分） |

**合并后的执行摘要第 2 条（建议）：**
> 2. Payment terms matter. A 30-year, node-delivered flat nominal contract breaks even near $66/MWh when 15.24% of potential energy is assumed unpaid (a stress setting, not a contract term); paying for all potential generation lowers this to $55.9/MWh. A separately versioned 10–15-year West-hub-settled hedge with a node merchant tail breaks even at $60.6–$84.8/MWh, depending mainly on the unsourced tail (Section 10.3). None of these is an observed contract offer.

审查者自估：这样改动后，摘要总共新增约 110 到 130 个英文词，没有新增独立的条目编号。

### 3. 反对的条目

没有需要整体反对的条目。我反对的只是**放置位置**：A-03 的数字、C-03 的“约 400”、EB-02 的 $80.4 都不应进入摘要；A-01 与 F-01 的区间只能出现一次。专家的证据都成立，我的分歧只涉及版面和受众优先级，不涉及事实。

---

## 二、我首轮 E-01 至 E-04 的复核

| 条目 | 专家是否提供了已被覆盖、可降级的证据？ | 结论 | 措辞调整 |
|---|---|---|---|
| **E-01** 摘要缺少贸易事实 | D-11 独立提出了同一问题，定为 P2。D 在第 2 节确认 §5.7 正文完整准确，但没有任何人说摘要已经覆盖。**未被覆盖。** | 保留。严重性存在分歧：我定为 P1，D 定为 P2。我的理由是，导读表让制造商先读第 1 章，而 12 月 4 日距报告日期只有 8 周。**争议保留，交给协调者裁定。** 由于实施方式已与 D-11 合并，这一分歧不影响修改内容 | 改为接在第 3 条之后（D-11 的位置）："From 4 December 2026, covered imported cells and modules face section 232 minimum import prices ($0.22/W; $0.38/W), an additional 15% duty, and continuing antidumping and countervailing duties (Section 5.7). These are compliance thresholds and potential duties, not delivered prices or a tariff outcome for any supplier. [P01]" 删去首轮写入的出口退税（依据 D-10） |
| **E-02** 摘要可能被读成“普遍不划算、需求萎缩” | F-10 独立提出（P2），并指出 §10.5 第 770 行、§14.4 第 1194 行已有阻断句。但这两句都在报告后半部，摘要没有。**正文有覆盖，摘要没有。** | 保留 P1，与 F-10 合并 | 第 26 行末尾："These are conditional, pre-tax, pre-credit results for one hypothetical system; they do not show that solar projects in ERCOT are generally uneconomic and are not a forecast of U.S. module demand." |
| **E-03** 表 13-1 供应商资格一行与 10.8 的导读 | D 确认 40%/45% 门槛与法条一致；EB-08 指出情景文件中的资格表述比表 10-3 窄；EB-03 和 F-02 要求在摘要中补充 $35.38m 的条件。**没有人处理表 13-1 第 2 行，也没有人提出导读路径缺少 10.8。** | 保留 P1，不降级。EB-03 的摘要改写能减轻同一误读，但表 13-1 是销售团队最可能直接摘录的表 | 措辞不变（见首轮）。补充一点：若采纳 EB-03，表 13-1 该格可以引用相同的条件表述，保持一致 |
| **E-04** "U.S. module input" 首次出现时没有定义 | D-01 不但没有让它降级，反而**加强了**它：这个输入不仅是美国组装基准，而且已扣除建模的 45X 补贴。26.1% 的份额和 10% 敏感性都建立在扣除补贴后的口径上 | 保留 P1，措辞按 D-01 调整 | 第 30 行（以及第 371 行首次加粗处）的括号改为："(the DOE/NLR benchmark's U.S.-assembled module line, about $0.29/Wdc in 2024 dollars after a modeled section 45X subsidy of about $0.07/Wdc; not an imported-module price)"。审查者算术：68.88/1000 ≈ $0.069/Wdc。不在摘要里写“与 MIP 相差 $0.02”这类结论 |

E-05 至 E-08（P2）：D-01 和 D-02 没有改变它们的结论。E-06 按 A-02 调整，见上文。E-07（图 4-3 的 45X 图注）与 D-01 方向一致，保留。

---

## 三、专家没有指出、但我作为客户仍会误读的地方（3 条）

### R2-E-1 我会以为 MIP 不合规的最坏结果只是补缴差额；保留原件规定的“永久禁止进口”没有写进报告
- **严重性建议：** P1
- **PDF 页 / MD：** 第 21 页；§5.7 第 400–403 行；13.1 问题表第 1110 行
- **原句：** "With documentation but an entered value below the MIP, they bear a specific tariff equal to the shortfall."
- **问题：** 公告第 (3) 条规定，如果 CBP 认定进口商的文件存在重大不实或重大违反认证，"that importer and its affiliates shall permanently be prohibited from importing polysilicon and polysilicon derivatives into the United States"，此外还可处罚款。报告对执行机制的描述只到“补缴差额”为止。审查者用 grep 检索报告全文，没有找到 "permanent" 或 "prohibited from importing"。
- **证据：** `closure-evidence/sources/trade/FR-2026-16400_plain.txt` 第 (3) 条（约第 245–250 行）。
- **客户后果：** 我方可能把“首次公平交易售价 ≥ MIP”的认证当作一项可以事后补税的价格安排，低估进口商和关联方的合规风险。对需要设立美国进口实体的出口商，这是最关键的结构性风险。
- **最小改法：** 在 §5.7 第 403 行之后加一条：
  > CBP monitors the accuracy of these certifications; materially inaccurate documentation or material non-compliance can lead to a permanent import prohibition for the importer and its affiliates, as well as penalties. [P01, clause 3]

  并在 13.1 问题表 "Who is responsible for customs entry and duties?" 一行的证据栏加 "and MIP certification responsibility"。
- **是否改变现有数字：** N
- **信心：** High（逐字依据保留原件）
- **是否在范围内：** Y（证据已在包内，只是报告未使用）

### R2-E-2 我会把 $0.38/W 当作固定不变的门槛；公告授权商务部长可以调整 MIP
- **严重性建议：** P2
- **PDF 页 / MD：** 第 21 页；第 398、405、411 行；13.1 第 1103 行
- **原句：** "The headline $0.38/W is therefore a compliance threshold and potential duty for covered imports, not a delivered project price."
- **问题：** 公告第 1(b) 条："The Secretary is authorized to adjust these minimum import prices from time to time to reflect market conditions…"。报告多次把 $0.38/W 作为对照锚点（第 411、1103 行），但没有提到它可以调整。
- **证据：** `FR-2026-16400_plain.txt` 第 1(b) 条（约第 206–209 行）。
- **客户后果：** 定价团队可能把 $0.38/W 写进多年期供货合同的价格条款，或作为长期定价的下限。
- **最小改法：** 在第 405 行句末加：
  > The proclamation authorizes the Secretary of Commerce to adjust the MIPs from time to time, so the $0.38/W level is not a fixed long-term threshold.
- **是否改变现有数字：** N
- **信心：** High
- **是否在范围内：** Y

### R2-E-3 我会把表 1-1 中的“组件占 26.1%”读成“组件占客户项目总投资的 26%”
- **严重性建议：** P2
- **PDF 页 / MD：** 第 4 页；表 1-1 第 50 行（对照第 379 行）
- **原句：** "Module share of PV-only cost benchmark | 26.1% | National component model; 5.5"
- **问题：** 26.1% 的分母是不含并网费用、并已扣除 45X 补贴（D-01）的 PV-only 模型市场价。在本报告 $143.7m 的总投资中，组件对应约 $32.9m，约占 **22.9%**。审查者算术：126.04 × 0.26111 ≈ 32.91；32.91 / 143.67 ≈ 22.9%。两个份额都是基准值，不是项目实际份额。销售材料最常引用的恰恰是这类“组件占项目成本 X%”的数字。
- **证据：** 报告第 379 行（$126.04m PV 隔夜成本，$17.63m 并网费用）、第 43 行（$143.7m）；D-01 所引的 CSV。
- **客户后果：** 中等程度的误读。读者会高估组件在客户总投资中的权重，并与 D-01 揭示的扣除补贴后口径叠加。
- **最小改法：** 把表 1-1 该行的说明栏改为：
  > PV-only modeled cost excluding grid connection, U.S.-assembled module net of modeled 45X; about 23% of the $143.7m reference CAPEX; 5.5–5.6
- **是否改变现有数字：** N（新增的 23% 由现有数字推出，标注为审查者算术）
- **信心：** High
- **是否在范围内：** Y

---

## 四、第二轮结论

维持首轮结论 **②：完成所列最小编辑后可移交**。专家意见中没有出现阻碍制造商用途的 P0。

从制造商角度，建议移交前必须完成的修改（全部为措辞或标签修改，不改变现有数字）：

1. **E-04 与 D-01 合并：** 定义组件输入并标明 45X 口径。
2. **D-02：** 表 4-2 毛利口径改标签并加附注数字。
3. **E-03：** 表 13-1 第 2 行改写，并在导读路径中加入 10.8。
4. **E-02 与 F-10 合并：** 摘要加一句阻断推论。
5. **E-01 与 D-11 合并：** 第 3 条后加入贸易事实，不含出口退税。
6. **R2-E-1：** 写入 MIP 不实认证可导致永久禁止进口。
7. **F-09：** 摘要和表 13-1 改为 "of which"。

摘要篇幅控制原则：A-01 与 F-01 的区间只出现一次；A-03 和 C-03 的数字不进摘要。

**仍未解决的争议：**
- E-01 与 D-11 的严重性（P1 还是 P2）。
- E-02 与 F-10 的严重性（P1 还是 P2），以及该句放在 §1.1 首段还是 §1.3 的 Limits 框。
