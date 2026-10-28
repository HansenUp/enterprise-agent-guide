# 企业 Agent 架构与能力平台建设指南

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hans)
[![Code License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE-CODE)
[![Pages](https://img.shields.io/badge/在线阅读-GitHub%20Pages-2ea44f.svg)](https://hansenup.github.io/enterprise-agent-guide/)

[English](README.en.md) · 作者：[HansenUp](https://github.com/HansenUp) · 仓库：[HansenUp/enterprise-agent-guide](https://github.com/HansenUp/enterprise-agent-guide)

面向企业架构师、高级 Agent 开发工程师和 AI 平台负责人的中文指南。内容从核心概念和技术演进讲到生产架构、平台建设方案与业务落地。

- **120 个核心概念**（C001–C120）：每条包含定义、工程取舍和方向判断，并标注状态：基础／增强／条件／探索／迁移。
- **37 章**：概念与工程机制（1–21）、平台蓝图与业务案例（22–29）、企业 AI 平台建设方案（30–37）。
- **68 条参考资料**：以官方文档、规范和原始论文为主，正文用 `[Sxx]` 标注来源。
- **交互版**：单个 HTML 文件，支持概念检索、学习路线、40 道面试练习题、容量估算和本地学习进度。不依赖外部 CDN 或字体，可离线打开。

核心判断：企业 AI 平台的长期资产是业务工具、权限、知识与数据质量、任务状态、评测集及交付机制。模型、提示词、框架和编排策略都应能替换。

> 资料核验日期为 2026-09-11，2026-10 发布前抽查更新。协议、框架和产品版本变化很快，做选型时请以各项目的官方发布记录为准。

## 阅读方式

| 方式 | 入口 |
|---|---|
| 在线交互版 | <https://hansenup.github.io/enterprise-agent-guide/> |
| 本地交互版 | 用浏览器直接打开 [`site/index.html`](site/index.html) |
| Markdown 原文 | [`guide/README.md`](guide/README.md)（目录） |
| 框架调研报告 | [`research/agent-framework-comparison-2026-09.md`](research/agent-framework-comparison-2026-09.md)：LangChain、LangGraph、AgentScope、Spring AI Alibaba、Claude Agent SDK、DeepSeek Harness 对比 |
| 学习面试手册 | [`site/handbook.html`](site/handbook.html)（[在线](https://hansenup.github.io/enterprise-agent-guide/handbook.html)）：Agent 框架与 Python 技术栈学习面试手册，100 题。其中的框架版本与 API 反映截至 2026-09 的状态，使用前请以官方最新文档为准 |

建议路线：先通读第 1–3 章，再按问题查第 4–21 章；做平台方案时看第 22–37 章。

## 目录结构

```text
guide/       指南 Markdown 源文件（guide/README.md 决定章节顺序）
data/        面试题（interview.json）和概念搜索别名（term_aliases.json）
research/    框架调研对比报告
tools/       交互版生成脚本与 HTML 模板
site/        生成的交互版（index.html）和学习手册（handbook.html）
.github/     GitHub Pages 部署工作流
```

## 修改与构建

只修改 `guide/`、`data/` 或 `tools/template.html`，不要直接编辑 `site/index.html`。构建只需要 Python 3.9+ 标准库：

```bash
python3 tools/build_html.py          # 重新生成 site/index.html
python3 tools/build_html.py --check  # 检查 site/index.html 是否与源文件一致
```

构建脚本会校验：概念数量为 120、来源编号不重复，以及正文引用的每个 `[Sxx]` 都有对应来源。

Markdown 约定：

- 每个文件以 `# 标题` 开头；数字开头的标题（如 `# 10 协议与互操作的现行边界`）成为第 N 章。
- 概念标题格式为 `## C053 English Name（中文名） 【状态】`。
- 来源条目写在 `references-*.md` 中：`[S01] 标题`，下一段为 `https://` 链接。
- 章节末尾的 `[Sxx]: https://...` 链接定义只用于让 GitHub 上的引用可以点击，构建交互版时会忽略。

## 部署到 GitHub Pages

仓库已包含 `.github/workflows/pages.yml`，发布地址为 <https://hansenup.github.io/enterprise-agent-guide/>。在仓库 Settings → Pages 中，把 Source 设为 **GitHub Actions**。之后每次推送到 `main`，工作流都会重新构建并发布 `site/` 目录。

## 许可

- 文档内容（`guide/`、`research/`、`data/`、`site/`）采用 [CC BY-NC-SA 4.0](LICENSE)（署名-非商业性使用-相同方式共享）。转载或改编时请署名 HansenUp、附上仓库链接并注明是否修改；不得用于商业目的；改编作品须以相同许可发布。
- 构建脚本与模板代码（`tools/`）采用 [MIT](LICENSE-CODE)。
- 署名：HansenUp（<https://github.com/HansenUp/enterprise-agent-guide>）。
- 引用的第三方资料版权归原作者所有，本仓库只提供链接和评述。

## 免责声明

本指南中的架构、案例、阈值和实施计划都是待验证的设计建议，不是行业标准，也不代表任何企业的真实系统或已落地方案。面试题为学习整理，不来自任何企业的真实题库。
