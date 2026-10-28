# Enterprise Agent Architecture & AI Platform Guide (Chinese)

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Code License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE-CODE)
[![Pages](https://img.shields.io/badge/Read%20online-GitHub%20Pages-2ea44f.svg)](https://hansenup.github.io/enterprise-agent-guide/)

[中文](README.md) · Author: [HansenUp](https://github.com/HansenUp) · Repo: [HansenUp/enterprise-agent-guide](https://github.com/HansenUp/enterprise-agent-guide)

A Chinese-language guide for enterprise architects, senior agent developers and AI platform owners. It covers agent concepts and their evolution, production architecture, an enterprise AI platform blueprint and business case studies.

- **120 core concepts** (C001–C120), each with a definition, engineering trade-offs and a status label (foundational / enhancing / conditional / exploratory / migrating).
- **37 chapters** plus supplements, a glossary and **68 sources**, mostly official docs, specifications and papers.
- **Interactive single-file site** with concept search, learning paths, 40 interview practice questions, a capacity estimator and local progress tracking. It works offline and loads no external CDNs or fonts.

Sources were checked on 2026-09-11 and spot-checked again in October 2026. Protocol and framework versions change fast, so check the official release notes before you choose a stack.

## Read

- Interactive: open [`site/index.html`](site/index.html) in a browser, or visit <https://hansenup.github.io/enterprise-agent-guide/>.
- Markdown: start at [`guide/README.md`](guide/README.md).
- Interview handbook: [`site/handbook.html`](site/handbook.html) ([online](https://hansenup.github.io/enterprise-agent-guide/handbook.html)), 100 questions on agent frameworks and the Python stack. It reflects framework versions and APIs as of 2026-09; check the official docs before relying on it.
- Framework comparison (LangChain, LangGraph, AgentScope, Spring AI Alibaba, Claude Agent SDK, DeepSeek Harness): [`research/`](research/).

## Build

```bash
python3 tools/build_html.py          # regenerate site/index.html (stdlib only, Python 3.9+)
python3 tools/build_html.py --check  # verify site/index.html matches the sources
```

To publish, set **Settings → Pages → Source** to **GitHub Actions**. The included workflow then builds and deploys `site/` on every push to `main`.

## License

Content (`guide/`, `research/`, `data/`, `site/`) is licensed under [CC BY-NC-SA 4.0](LICENSE) (Attribution-NonCommercial-ShareAlike). Credit HansenUp with a link to <https://github.com/HansenUp/enterprise-agent-guide>, indicate changes, do not use it commercially, and share adaptations under the same license. The build script and template in `tools/` are licensed under [MIT](LICENSE-CODE). Third-party sources belong to their authors; this repo only links to and comments on them.
