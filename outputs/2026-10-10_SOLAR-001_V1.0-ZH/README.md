# SOLAR-001 1.0 版 中文版

**报告：**《从中国光伏供应链到美国电力市场：产业重构、ERCOT 价值捕获与大型地面光伏经济性》
**版本：** 1.0 版（中文版），2026 年 10 月 10 日
**PDF：** `SOLAR-001_V1.0_Integrated-Market-Research-Report-ZH.pdf`（92 页，US Letter）

本中文版译自英文 1.0 版（交付版标准，见 `records/V1.0-EN-inherited/V1.0-Acceptance-Record.md`）。内容、数字、来源与英文版一致，不另做新的计算或结论；如有歧义，以英文版为准。英文 1.0 版的验收边界同样适用：交付版标准 D1–D10 已满足，原十项 1.0 标准并未全部满足（第 6 项对假设项目无法关闭）。

## 与英文版的关系

| 项目 | 说明 |
|---|---|
| 正文 | 全文译为简体中文，与英文源文件逐行对齐（1,533 行，标题、表格行、列表、方框位置一一对应） |
| 数字 | 2,848 个数字逐行逐格与英文版比对，全部一致；3 处写法差异已逐条说明（见下） |
| 图表 | 35 张图与英文版完全相同（SVG 逐字节一致）；图题、图注为中文，**图内坐标轴和图例保留英文** |
| 来源 | 来源书目中的文献标题、数据集名、文件名、链接原样保留英文，描述性文字译为中文 |
| 术语 | 首次出现给出中文并保留缩写；附录 D 术语表"术语"列保留英文缩写 |

## 目录

| 路径 | 内容 |
|---|---|
| `SOLAR-001_V1.0_…-ZH.pdf` | 中文版 PDF：可点击目录、115 个书签、交叉引用与来源链接 |
| `source/SOLAR-001_V1.0_Report-ZH.md` | 中文 Markdown 源文件（由 `build/assemble_translation.py` 从分段译文生成） |
| `source/SOLAR-001_V1.0_Report-EN.md` | 英文 1.0 版源文件（未改动，作为数字核对基准） |
| `source/translation-parts/` | 13 段分段译文 |
| `assets/fonts/` | 嵌入字体：Noto Serif / Sans CJK SC 子集（思源宋体/黑体，SIL OFL 1.1），以及英文版的 Source Serif 4、Liberation Sans、DejaVu Sans Mono |
| `build/` | 构建与检查脚本（在英文版脚本基础上改为识别中文标签） |
| `records/` | 本版检查记录、翻译记录、逐页检查；`records/V1.0-EN-inherited/` 为英文 1.0 版的原始记录 |

## 重建

需要 Python 3.10+，以及 `weasyprint`（70.0）、`matplotlib`、`numpy`、`pandas`、`pymupdf`、`pillow`、`fonttools`。不需要联网、登录或付费服务。

```bash
python3 build/build_all.py                          # 原地重建
python3 build/verify_rebuild.py /tmp/zh-check       # 空目录重建并与交付 PDF 比对
sha256sum -c SHA256SUMS.txt
```

## 校验（`records/`）

| 文件 | 结果 |
|---|---|
| `Number-Preservation-Check-ZH.json` | PASS：中文与英文 1.0 版逐行、逐表格单元比对，2,848 个数字一致；3 处已说明的写法差异 |
| `Number-Preservation-Check-EN.json` | PASS：英文 1.0 版源文件相对 V0.999 的数字登记（与英文版相同） |
| `Figure-Data-Check.json` | 34 张上游图的绘图数据与快照一致 |
| `Report-Structure-Check.json` | PASS：表/图编号、全部交叉引用有目标、12 条必需限定语（中文措辞）在位、链接、目录页码 = 书签 |
| `Font-Check.json` | PASS：源文件 1,156 个不同字符全部有嵌入字体；PDF 只嵌入本包字体 |
| `Rebuild-Verification.json` | PASS：空目录重建 92 页，逐页文字、书签一致，35/35 张 SVG 一致 |
| `Translation-Record.md` | 翻译方法、数字核对、写法差异与编辑修正 |
| `Page-Inspection-Log.md` | 逐页检查记录；缩略图在 `page-inspection/sheets/` |

## 字体说明

思源字体原版（Noto CJK）每个文件 16–25 MB，本包只嵌入 GB 2312 全部汉字、标点和正文用到的字符，并转换为 TrueType 轮廓（WeasyPrint 70 无法绘制 CID 编码的 CFF 字形）。正文新增 GB 2312 以外的字时，`Font-Check` 会报出，用 `build/subset_cjk_fonts.py` 从官方原版字体重新生成子集即可。
