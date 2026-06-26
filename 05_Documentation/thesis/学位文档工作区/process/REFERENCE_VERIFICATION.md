# 参考文献核实记录

> **核实日期**：2026-06-26（全量 32 篇）  
> **真源文件**：[`BIBLIOGRAPHY.yaml`](BIBLIOGRAPHY.yaml)  
> **Crossref 报告**：[`verify_bibliography_report.txt`](verify_bibliography_report.txt)（运行 `verify_bibliography_doi.py` 生成）  
> **文件夹材料**：`项目辅助材料/参考文献/`（5 个 PDF，其中 2 个为 Lin & Chen 2015 重复副本，1 个为中文译本）

---

## 核实方法说明

| 方式 | 适用 |
|------|------|
| Crossref API | 有 DOI 的西文期刊/会议 |
| DOI 落地页 / IEEE Xplore / informs-sim.org | WSC 论文、Crossref 404 的旧 DOI |
| 期刊官网 / dblp / 作者主页 | 中文 CIMS DOI、NeurIPS/ICLR 预印本 |
| 文件夹 PDF | hoppe2025、luttmann2026、lin2015 |

**Crossref「FAIL 404」**：部分 Elsevier 旧 S 格式 DOI 在 API 中失效，但 `10.1016/s0377-2217(...)` 等新格式可解析（已修正 jain、framinan 等）。

---

## 文件夹 PDF 映射

| 文件夹 PDF | 对应文献 ID | 说明 |
|------------|-------------|------|
| Simulation optimization approach for hybrid flow shop…pdf | lin2015 | 主文献 |
| …_1_15_translate.pdf | lin2015 | 译本，不单独编号 |
| Simulation-optimization-applied-to-production-sche_2024…pdf | lin2015 | 文件名误导，内容为同一篇 Lin & Chen 2015 |
| MULTI-ACTION SELF-IMPROVEMENT FOR NEURAL.pdf | luttmann2026 | ICLR 2026 / arXiv:2510.12273 |
| Structured Reinforcement Learning.pdf | hoppe2025 | NeurIPS 2025 / arXiv:2505.19053 |

---

## 逐条核实（32 篇）

| 序号 | ID | 第一作者 | 年 | 核实方式 | 状态 | 备注 |
|------|-----|----------|-----|----------|------|------|
| 1 | monch2003 | Mönch | 2003 | [WSC PDF](https://informs-sim.org/wsc03papers/167.pdf) | ✓ 已替换 | 原 akcali2003 作者/页码错误；WSC pp.1338–1345 |
| 2 | banks2010 | Banks | 2010 | 教材 | ✓ | 无 DOI，版次与出版社与 Prentice Hall 记录一致 |
| 3 | chen2013 | Chen | 2013 | [DOI](https://doi.org/10.1080/21681015.2013.860926) | ✓ 已更正 | 原 DOI 867950 错误；卷 30(7):452–460 |
| 4 | chenritzo2011 | Chen-Ritzo | 2011 | [DOI](https://doi.org/10.1504/EJIE.2011.041617) | ✓ | Crossref 一致 |
| 5 | chien2011 | Chien | 2011 | [DOI](https://doi.org/10.1504/EJIE.2011.041616) | ✓ | Crossref 一致 |
| 6 | chiu2023 | Chiu | 2023 | [DOI](https://doi.org/10.1007/s10489-022-03657-3) | ✓ | Crossref 在线年 2022、期刊年 2023，以期刊为准 |
| 7 | chiu2026 | Chiu | 2026 | [DOI](https://doi.org/10.1016/j.swevo.2025.102252) | ✓ | Crossref 一致 |
| 8 | monch2011 | Mönch | 2011 | [DOI](https://doi.org/10.1007/s10951-010-0222-9) | ✓ 已替换 | 原 fowler2008 为不存在的 WSC 条目 |
| 9 | framinan2004 | Framinan | 2004 | [DOI](https://doi.org/10.1016/s0377-2217(01)00278-8) | ✓ 已更正 | 原 DOI/页码错误；141(3):559–569 |
| 10 | habenicht2002 | Habenicht | 2002 | [WSC](https://informs-sim.org/wsc02papers/140.pdf) | ✓ 已更正 | 题名/页码 1406–1413；作者 I. Habenicht |
| 11 | hoppe2025 | Hoppe | 2025 | 文件夹 PDF + arXiv:2505.19053 | ✓ | NeurIPS 2025 poster |
| 12 | jain1999 | Jain | 1999 | [DOI](https://doi.org/10.1016/s0377-2217(98)00113-1) | ✓ 已更正 | 原 DOI 00419-1 指向其他论文 |
| 13 | klemmt2011 | Klemmt | 2011 | [DOI](https://doi.org/10.1504/EJIE.2011.041621) | ✓ | Crossref 一致 |
| 14 | law2015 | Law | 2015 | 教材 | ✓ | 第 5 版 McGraw-Hill |
| 15 | lee2008 | Lee | 2008 | [DOI](https://doi.org/10.1109/WSC.2008.4736332) | ✓ 已更正 | 原 DOI 4736407 为其他论文 |
| 16 | lee2011 | Lee | 2011 | [DOI](https://doi.org/10.1504/EJIE.2011.041620) | ✓ | Crossref 一致 |
| 17 | lin2015 | Lin | 2015 | [DOI](https://doi.org/10.1016/j.simpat.2014.10.008) | ✓ 文件夹 | Crossref 一致 |
| 18 | liu2022 | 刘琼 | 2022 | [DOI](https://doi.org/10.13587/j.cnki.issn1007-7634.2022.02.001) | ✓ | Crossref API 404；DOI 与刊名卷期与知网一致 |
| 19 | luttmann2026 | Luttmann | 2026 | 文件夹 PDF + arXiv:2510.12273 | ✓ | ICLR 2026 |
| 20 | monch2005 | Mönch | 2005 | [DOI](https://doi.org/10.1016/j.cor.2004.04.001) | ✓ 已替换 | 原 monch2001 WSC 不存在；期刊版 COR 32(11) |
| 21 | panwalkar1977 | Panwalkar | 1977 | [DOI](https://doi.org/10.1287/opre.25.1.45) | ✓ | 已从 1993 更正 |
| 22 | pinedo2016 | Pinedo | 2016 | 教材 | ✓ | Springer 第 5 版 |
| 23 | potts1989 | Potts | 1989 | [DOI](https://doi.org/10.1016/0167-6377(89)90013-8) | ✓ 已替换 | 原 potts1982 题名/DOI 均错误；lot streaming |
| 24 | ruiz2006 | Ruiz | 2006 | [DOI](https://doi.org/10.1016/j.ejor.2004.06.038) | ✓ 已替换 | 原 Annals 138 条目不存在；EJOR 169(3) |
| 25 | stubbe2011 | Stubbe | 2011 | [DOI](https://doi.org/10.1504/EJIE.2011.041618) | ✓ | Crossref 一致 |
| 26 | uzsoy1992 | Uzsoy | 1992 | Scholar / IJPR 30(2) | ✓ 无 DOI | 原 DOI 指向 order release 论文，已移除 |
| 27 | wang2023 | 王卓君 | 2023 | [DOI](https://doi.org/10.13196/j.cims.2022.0646) | ✓ | Crossref API 404；CIMS DOI 有效 |
| 28 | fang2023 | Fang | 2023 | [DOI](https://doi.org/10.3390/su151713012) | ✓ 已替换 | 原 wu2023 作者错误（应为 Fang/Cheang/Lim） |
| 29 | xuan2020 | 轩华 | 2020 | [DOI](https://doi.org/10.13196/j.cims.2019.1774) | ✓ | 刊年 2020，DOI 年份 2019 正常 |
| 30 | yedidsion2022 | Yedidsion | 2022 | [DOI](https://doi.org/10.1109/WSC57314.2022.10015463) | ✓ 已更正 | 原标 2021 WSC；实为 2022 pp.3275–3284 |
| 31 | zhao2025 | 赵子夜 | 2025 | [DOI](https://doi.org/10.13196/j.cims.2023.0757) | ✓ | Crossref API 404；CIMS DOI 有效 |
| 32 | zhou2020 | Zhou | 2020 | [DOI](https://doi.org/10.1016/j.procir.2020.05.163) | ✓ 已更正 | 非 WSC；Procedia CIRP 93:383–388 [J] |

---

## 移除/更正记录（2026-06-26）

| 原 ID | 处理 | 原因 |
|--------|------|------|
| akcali2003 | → monch2003 | 题名对应 Mönch & Habenicht WSC 2003，非 Akçali |
| fowler2008 | → monch2011 | 该 WSC 2008 论文不存在；改用 J. Scheduling 2011 综述 |
| wu2023 | → fang2023 | DOI 正确但作者应为 Fang, Cheang, Lim |
| yedidsion2021 | → yedidsion2022 | WSC 2022，DOI 10.1109/WSC57314.2022.10015463 |
| monch2001 | → monch2005 | WSC 2001 无此页；期刊版 COR 2005 |
| potts1982 | → potts1989 | 原题名/DOI 错误；lot streaming 应为 Potts & Baker 1989 |
| panwalkar1993 | → panwalkar1977 | 1977 年 Operations Research（此前已更正） |

---

## 正文引用同步（section_content / Word R11·R13·R15）

| 旧写法 | 新写法 |
|--------|--------|
| Wu等（2023） | Fang等（2023） |
| Fowler等（2008） | Mönch等（2011） |
| Yedidsion等（2021） | Yedidsion等（2022） |
| Akçali等（2003） | Mönch等（2003） |
| Mönch等（2001） | Mönch等（2005） |
| Potts和Van Wassenhove（1982） | Potts等（1989） |
| Habenicht和Mönch（2002） | Habenicht等（2002） |

Word 更新：`python fix_references_local.py`（仅 R11 文献块 + 上表 Find 替换，不运行 fill_template）。

---

## 未纳入列表

| 材料 | 原因 |
|------|------|
| Lin & Chen 2015 中文译本 PDF | 与 lin2015 为同一文献 |
| 文件名含「2024 Journal-of-Industria」的 PDF | Lin & Chen 2015 重复文件 |
