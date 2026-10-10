# 需要你本人登录的免费资料：操作清单

**编制日：** 2026-10-09（美东）。

**规则：**

- 登录、填写个人信息、接受条款，都由你本人完成。
- 密码、验证码、恢复码不要发给我，也不要写进聊天、脚本或项目文件。
- 遇到任何收费提示（订阅、按次或按页收费、购买、需绑定支付方式的试用）就停止这条路径，并告诉我卡在哪一步。我会把它记为缺口，继续做别的。

## 1. ERCOT Data Access Portal：2026 年节点价格月度归档（最有价值）

| 项目 | 内容 |
|---|---|
| 官方链接 | [NP6-905-CD 归档](https://data.ercot.com/data-product-archive/NP6-905-CD)；产品定义：[NP6-905-CD](https://www.ercot.com/mp/data-products/data-product-details?id=NP6-905-CD)；门户说明：[Data Access Portal](https://www.ercot.com/services/mdt/data-portal) |
| 登录目的 | 归档下载需要 ERCOT 的免费账户。公开列表只保留最近约 7 天的 15 分钟文件，拿不到整月数据 |
| 需要的文件 | NP6-905-CD 的 2026-01 至最新完整月份的月度归档 ZIP，文件名形如 `…SPPHLZNP6905_2026-MM.zip`，原样保存，不要解压后改动 |
| 需要的字段 | 文件里的全部列都保留。我会用本地脚本筛出 `TAYGETE2_ALL` 和 `HB_WEST`，所用列为 DeliveryDate、DeliveryHour、DeliveryInterval、SettlementPointName、SettlementPointType、SettlementPointPrice、DSTFlag |
| 用途 | FIN-08：RTC+B 上线（2025-12-05）后的正式价格，用于检验 VPPA 和商户尾段情景是否还适用。不做因果推断 |
| 保存位置 | `Data/raw/2026-10-10_Manual-Intake/ERCOT/`（如果实际在 10-10 完成，就用当天日期） |

**步骤：**

1. 打开归档链接，按页面提示用 ERCOT 账户登录。没有账户时，用免费注册入口；遇到要求付款就停止。
2. 在 NP6-905-CD 归档列表中按月份找 2026 年的月度文件，逐个下载。
3. 把文件放进上面的目录，然后告诉我。我会核对文件名、大小和 SHA-256，并在新的独立版本里提取价格。
4. 如果账户条款限制保存或再分发，请先只告诉我条款的大意。在你确认之前，我不会把文件放进 ZIP。

## 2. LevelTen PPA Price Index：免费摘要（如果有）

| 项目 | 内容 |
|---|---|
| 官方链接 | [LevelTen PPA Price Index](https://www.leveltenenergy.com/ppa)；[Q2 2026 公开说明页](https://www.leveltenenergy.com/post/levelten-north-american-ppa-price-index-q2-2026) |
| 登录目的 | 免费摘要通常要填一张联系表单（姓名、邮箱、公司），这属于个人信息，由你本人填写 |
| 需要的内容 | 2026 年 Q2（或最新季度）ERCOT 光伏 P25 报价（美元/MWh），以及报告对期限、结算点（枢纽或节点）、是否含 REC、负价条款的说明 |
| 用途 | FIN-03：替换我目前引用的二手转述（Q4 2025 ERCOT P25 49 美元/MWh），并确认报价期限，避免和 30 年保本价直接比较 |
| 停止条件 | 页面只提供订阅版（Report Center 需要付费账户），或者要求付款 |

**步骤：** 打开链接 → 找 “Download” 或 “Get the report” → 自行填写表单 → 把收到的 PDF 原样保存到 `Data/raw/2026-10-10_Manual-Intake/PPA/` → 告诉我。

## 3. 不建议使用：PACER

PACER 按页收费，每季度不超过 30 美元时免收，但计费机制本身属于按页收费，所以我没有把它列入。上诉状态我改用无需登录的 CourtListener RECAP 继续复核。

## 4. 无需登录、已自行获取的资料（2026-10-09 晚）

- ERCOT NP6-785-ER 2026 年 Hub/Load Zone 年度累计文件，已获取，仅含枢纽价格：data/HB_WEST-2026-JanSep-Post-RTCB-Context.csv。
- ERCOT 独立市场监测机构 2025 年市场状况报告及 2026 年 8 月 TAC 简报，已获取。
- 德州法规原文，已获取：PURA §35.004、Tax Code 第 313 章现行文本、Government Code §403.602(8)。JETI 明确排除非可调度发电。
- Business Wire 原文：用浏览器再试仍被拒绝访问，这条路径已停止。
- ATB 的 Tableau 组成表：尚未导出，不影响本轮结论。

详见 Followup-Evidence-No-Login.md。
