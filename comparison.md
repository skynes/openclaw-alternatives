# Technical stack comparison (OpenClaw & alternatives)

**Audience:** architects and engineers choosing a runtime for personal or team AI agents.  
**Language:** English.

This document compares **implementation stack**, **integration surfaces** (MCP, skills, APIs), **messaging**, **persistence**, and **operational profile**. **§11** is GitHub popularity; **§12** is **technological efficiency** (speed, lightness, functionality). Popularity (stars) is not the same as efficiency; see [README.md](README.md) and [REFERENCE.md](REFERENCE.md) for overview links.

**Disclaimer:** upstream projects change quickly. Treat cells as **orientation**, not a warranty. Confirm critical requirements in each project’s README, `docs/`, and issue tracker.

---

## Legend

| Symbol | Meaning |
|--------|---------|
| **Yes** | First-class, documented feature |
| **Partial** | Experimental, plugin, or limited |
| **—** | Not applicable or not a product goal |
| **N/A** | Not an end-user agent (e.g. library only) |

---

## 1. Core runtime & codebase

| Project | Primary language | Typical runtime | Rough footprint | Notes |
|---------|------------------|-----------------|-----------------|--------|
| [OpenClaw](https://github.com/openclaw/openclaw) | TypeScript | Node.js | **High** (full assistant + UI surfaces) | Reference ecosystem; broadest feature surface |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Python | CPython (e.g. 3.11+), `uv` workflows | **Medium–high** | TUI + gateway; optional heavy extras (see repo) |
| [Nanobot](https://github.com/HKUDS/nanobot) | Python | CPython | **Low–medium** | “Ultra-lightweight” agent; multi-instance |
| [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) | Rust | Native binary | **Very low** (~MB-scale resident RAM) | Migration story from OpenClaw configs |
| [AstrBot](https://github.com/AstrBotDevs/AstrBot) | Python | CPython | **Medium** | IM-first chatbot; not a 1:1 OpenClaw clone |
| [PicoClaw](https://github.com/sipeed/picoclaw) | Go | Native / containers | **Low–medium** | Edge / gateway node, cheap hardware |
| [NanoClaw (qwibitai)](https://github.com/qwibitai/nanoclaw) | TypeScript | Node.js + containers | **Medium** | Security via containerized deployment |
| [IronClaw](https://github.com/nearai/ironclaw) | Rust | Native + WASM sandbox | **Medium** | Isolation via WebAssembly |
| [GoClaw](https://github.com/nextlevelbuilder/goclaw) | Go | Native / services | **Medium–high** (multi-tenant services) | Go rewrite; PostgreSQL in stack |
| [MicroClaw](https://github.com/microclaw/microclaw) | Rust | Native | **Medium** | Agent framework; MCP-oriented |
| [BeamClaw](https://github.com/peterdmv/beamclaw) | Erlang | BEAM / OTP | **Medium** | Distributed gateway / MCP **host** patterns |
| [mcp-use](https://github.com/mcp-use/mcp-use) | TypeScript (+ Python lib) | Node / Python | **N/A** | **Framework** for MCP apps, not a user-facing agent |

---

## 2. MCP (Model Context Protocol)

| Project | MCP client (use tools) | MCP server (expose tools) | Notes |
|---------|------------------------|----------------------------|--------|
| OpenClaw | **Yes** | Ecosystem expectation | Large surface; check current issues for “external MCP server” scope |
| Hermes Agent | **Yes** | **Partial** (via integration docs) | First-class docs for MCP in user guide |
| Nanobot | **Yes** | **Partial** | Lightweight agent; verify version for your MCP needs |
| ZeroClaw | **Partial** | **Partial** | Ecosystem migration; MCP config topics in issues |
| AstrBot | **Partial** | **Partial** | IM/plugins model; not MCP-centric |
| PicoClaw | **Partial** | **Partial** | Edge/gateway focus |
| NanoClaw (qwibitai) | **Partial** | **Partial** | Business messengers + containers |
| IronClaw | **Partial** | **Partial** | Security-first; check compatibility |
| GoClaw | **Yes** | **Partial** | Go stack; enterprise-style integration |
| MicroClaw | **Yes** | Transport-focused | MCP + HTTP transport emphasis |
| BeamClaw | **Yes** (host role) | **Yes** | Gateway / MCP **host** positioning |
| mcp-use | **N/A** | **N/A** | **Library** to build MCP-aware apps |

---

## 3. Skills, plugins, and extension model

| Project | Skills / procedural memory | Plugin / extension style | Interop |
|---------|------------------------------|----------------------------|---------|
| OpenClaw | **Yes** (skills ecosystem, [clawhub](https://github.com/clawhub), curated lists) | Skills + config | Broad community |
| Hermes Agent | **Yes** (skills hub, learning loop, `agentskills.io`-compatible claims in upstream docs) | Python toolsets, optional skills | `hermes claw migrate` from OpenClaw |
| Nanobot | **Partial** | Python / config | OpenClaw-like patterns, smaller core |
| ZeroClaw | **Partial** | Config migration | Compatibility with OpenClaw workflows |
| AstrBot | **Yes** (plugin ecosystem) | Python plugins | IM adapters |
| PicoClaw | **Partial** | Go / config | Open-skills integration topics in ecosystem |
| NanoClaw (qwibitai) | **Partial** | TS / containers | Secure deployment story |
| IronClaw | **Partial** | Rust + sandbox | Tool execution under WASM |
| GoClaw | **Partial** | Go services | Multi-tenant operational model |
| MicroClaw | **Partial** | Rust framework | MCP tooling |
| BeamClaw | **Partial** | OTP / services | Gateway plugins |
| mcp-use | **—** | App framework | Build **custom** tool servers |

---

## 4. LLM providers & API surface

| Project | Provider model | Typical integration |
|---------|----------------|---------------------|
| OpenClaw | Multi-provider | API keys, managed connectors; check docs for latest list |
| Hermes Agent | Multi-provider | CLI `hermes model`; OpenRouter, OpenAI, Anthropic, portals, etc. (see upstream README) |
| Nanobot | Multi-model | Lightweight config; provider plugins |
| ZeroClaw | Config-driven | Migration from OpenClaw-style configs |
| AstrBot | Many LLM backends | GPT, Gemini, Llama, etc. |
| PicoClaw | Provider-dependent | Edge-oriented |
| NanoClaw (qwibitai) | API-based | Anthropic / cloud APIs (verify current README) |
| IronClaw | Provider with sandbox | Security boundary first |
| GoClaw | Service-oriented | API gateway patterns |
| MicroClaw | Framework-level | You wire models |
| BeamClaw | Gateway-level | MCP + messaging |

**Rule of thumb:** if you need **maximum provider flexibility out of the box**, compare **OpenClaw** vs **Hermes Agent** vs **AstrBot** (chatbot bias) vs **Nanobot** (minimal core).

---

## 5. Messaging & channels

| Project | CLI / local UI | Mobile / web | Chat platforms (examples) |
|---------|----------------|--------------|---------------------------|
| OpenClaw | **Yes** | **Partial** | Very wide channel list (15+), voice, Canvas |
| Hermes Agent | **Yes** (TUI) | **Partial** | Telegram, Discord, Slack, WhatsApp, Signal, Email, etc. |
| Nanobot | **Yes** | **Partial** | Multi-channel; slimmer than OpenClaw |
| ZeroClaw | **Partial** | **Partial** | Focus on lean runtime |
| AstrBot | **Partial** | Varies | **Strong**: TG, WhatsApp, many IM |
| PicoClaw | **Partial** | **Partial** | Gateway / Discord bot patterns |
| NanoClaw (qwibitai) | **Partial** | **Partial** | WhatsApp, Telegram, Slack, Discord, Gmail, … |
| IronClaw | **Partial** | **Partial** | Security-first |
| GoClaw | **Partial** | **Partial** | Enterprise messaging patterns |
| MicroClaw | **Partial** | **Partial** | MCP/HTTP less about consumer chat |
| BeamClaw | **—** | **—** | **Infrastructure**: fault-tolerant gateway |

Choose **AstrBot** or **Hermes** if **chat reach** is the main KPI; choose **OpenClaw** if you want **widest** surface including non-chat product features (e.g. Canvas) per upstream.

---

## 6. Persistence, memory, databases

| Project | Long-term memory | User/workspace model | Typical storage |
|---------|------------------|------------------------|-----------------|
| OpenClaw | **Yes** | Workspace, skills, memories | Local + cloud patterns; AWS references |
| Hermes Agent | **Yes** | Profiles, session search, migration from OpenClaw | SQLite / files + docs (Postgres where applicable in stack) |
| Nanobot | **Partial** | Lighter model | Local config/state |
| ZeroClaw | **Partial** | Migration-oriented | Minimal |
| AstrBot | **Yes** | Per-bot / per-platform | DB options in docs |
| PicoClaw | **Partial** | Edge | Resource-constrained |
| NanoClaw (qwibitai) | **Yes** | Container-isolated | Per deployment |
| IronClaw | **Partial** | Sandboxed execution | WASM boundary |
| GoClaw | **Yes** | Multi-tenant | **PostgreSQL** (explicit in ecosystem positioning) |
| MicroClaw | **Partial** | Framework | Your choice |
| BeamClaw | **Partial** | OTP state | Erlang patterns |

For **strong transactional backend** and **multi-tenant SaaS-style** design, **GoClaw** stands out on paper; for **rich personal agent memory + migration**, **Hermes** and **OpenClaw** are the usual shortlist.

---

## 7. Deployment & operations

| Project | Docker / compose | Bare metal / VPS | Serverless / remote env | Notes |
|---------|------------------|------------------|---------------------------|--------|
| OpenClaw | **Yes** | **Yes** | Cloud patterns | Mature setup scripts |
| Hermes Agent | **Yes** | **Yes** | Modal / Daytona / SSH backends (see docs) | Install script; not native Windows |
| Nanobot | **Yes** | **Yes** | **Partial** | Fast onboarding |
| ZeroClaw | **Yes** | **Yes** | **Partial** | Tiny binary story |
| AstrBot | **Yes** | **Yes** | **Partial** | Long-running bot |
| PicoClaw | **Yes** | **Yes** (edge) | **Partial** | Cheap devices |
| NanoClaw (qwibitai) | **Yes** | **Yes** | **Partial** | Apple Container angle (upstream) |
| IronClaw | **Yes** | **Yes** | **Partial** | Sandboxing ops |
| GoClaw | **Yes** | **Yes** | **Partial** | Service architecture |
| MicroClaw | **Yes** | **Yes** | **Partial** | HTTP service |
| BeamClaw | **Yes** | **Yes** | **Partial** | Cluster / HA mindset |

---

## 8. Licensing (check before production)

| Project | License (typical; verify file in repo) |
|---------|----------------------------------------|
| OpenClaw | See `LICENSE` in repo |
| Hermes Agent | MIT (per upstream README) |
| Nanobot | MIT (common; verify) |
| ZeroClaw | See repo |
| AstrBot | **AGPL-3.0** (copyleft; important for SaaS) |
| Others | Inspect each `LICENSE` |

If you cannot use **AGPL**, rule **AstrBot** in or out **before** deep integration.

---

## 9. Decision shortcuts

| If you need… | Shortlist |
|--------------|-----------|
| **Widest** product surface (channels, voice, ecosystem) | **OpenClaw** |
| **Python** + **skills** + **gateway** + **OpenClaw migration** | **Hermes Agent** |
| **Smallest** resource use, Rust | **ZeroClaw** / **IronClaw** (security) / **MicroClaw** (framework) |
| **Go** + **Postgres** + **multi-tenant** | **GoClaw** |
| **IM coverage** as primary (plugins, AGPL OK) | **AstrBot** |
| **Edge / MCU / binary size** | **PicoClaw**, **NullClaw**, **SubZeroClaw** (see [REFERENCE.md](REFERENCE.md)) |
| **Build MCP apps**, not pick an assistant | **mcp-use** |
| **Distributed gateway / MCP host** patterns | **BeamClaw** |

---

## 10. Related data in this repo

| Asset | Purpose |
|-------|---------|
| [scripts/data/github_stats.json](scripts/data/github_stats.json) | Fresh star/fork counts |
| [scripts/data/tavily_results.json](scripts/data/tavily_results.json) | Search-backed blurbs (regenerate via `compare_projects.py`) |
| [REFERENCE.md](REFERENCE.md) | Extended tables and categories |
| [STARS_BY_MONTH.md](STARS_BY_MONTH.md) | Stars over time (monthly); [stars_monthly_history.json](scripts/data/stars_monthly_history.json) |

---

## 11. Popularity ranking (GitHub)

**What this is:** a **community activity** snapshot, not a quality score. Useful to gauge momentum, fork interest, and discoverability.

**Formula** (same as `fetch_github_stats.py`): `popularity = 2 × stars + forks`.

**Source:** [scripts/data/github_stats.json](scripts/data/github_stats.json) — refresh with `python scripts/fetch_github_stats.py`.

| Rank | Project | ⭐ Stars | 🍴 Forks | Score |
|------|---------|--------:|---------:|------:|
| 1 | [OpenClaw](https://github.com/openclaw/openclaw) | 357 576 | 72 640 | 787 792 |
| 2 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 85 892 | 11 639 | 183 423 |
| 3 | [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | 46 054 | 4 490 | 96 598 |
| 4 | [Nanobot](https://github.com/HKUDS/nanobot) | 39 549 | 6 930 | 86 028 |
| 5 | [NanoClaw](https://github.com/qwibitai/nanoclaw) (qwibitai) | 27 292 | 11 972 | 66 556 |
| 6 | [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) | 30 153 | 4 351 | 64 657 |
| 7 | [AstrBot](https://github.com/AstrBotDevs/AstrBot) | 29 976 | 2 022 | 61 974 |
| 8 | [PicoClaw](https://github.com/sipeed/picoclaw) | 28 154 | 4 006 | 60 314 |
| 9 | [IronClaw](https://github.com/nearai/ironclaw) | 11 780 | 1 348 | 24 908 |
| 10 | [mcp-use](https://github.com/mcp-use/mcp-use) | 9 772 | 1 242 | 20 786 |
| 11 | [NullClaw](https://github.com/nullclaw/nullclaw) | 7 195 | 843 | 15 233 |
| 12 | [MimiClaw](https://github.com/memovai/mimiclaw) | 5 174 | 757 | 11 105 |
| 13 | [TinyClaw](https://github.com/jlia0/tinyclaw) (400-line) | 3 510 | 504 | 7 524 |
| 14 | [GoClaw](https://github.com/nextlevelbuilder/goclaw) | 2 706 | 683 | 6 095 |
| 15 | [zclaw](https://github.com/tnm/zclaw) | 2 074 | 177 | 4 325 |
| 16 | [ZeroClaw](https://github.com/openagen/zeroclaw) (openagen) | 1 808 | 267 | 3 883 |
| 17 | [MicroClaw](https://github.com/microclaw/microclaw) | 649 | 120 | 1 418 |
| 18 | [ZeptoClaw](https://github.com/qhkm/zeptoclaw) | 589 | 87 | 1 265 |
| 19 | [HermitClaw](https://github.com/brendanhogan/hermitclaw) | 319 | 54 | 692 |
| 20 | [TinyClaw](https://github.com/warengonzaga/tinyclaw) (warengonzaga) | 217 | 33 | 467 |
| 21 | [Safeclaw](https://github.com/princezuda/safeclaw) | 131 | 15 | 277 |
| 22 | [SubZeroClaw](https://github.com/jmlago/subzeroclaw) | 119 | 14 | 252 |
| 23 | [NanoClaw](https://github.com/ysz/nanoClaw) (ysz) | 61 | 18 | 140 |
| 24 | [SupaClaw](https://github.com/vincenzodomina/supaclaw) | 58 | 10 | 126 |
| 25 | [Carapace](https://github.com/puremachinery/carapace) | 43 | 6 | 92 |
| 26 | [RustClaw](https://github.com/shimaenaga1123/rustclaw) | 4 | 1 | 9 |
| 27 | [BeamClaw](https://github.com/peterdmv/beamclaw) | 0 | 2 | 2 |

*`awesome-openclaw-skills` is a curated list, not a runtime — kept here for completeness.*

---

## 12. Technological efficiency rating (speed · lightness · functionality)

**What this is:** a **qualitative** scorecard for **how fast / lean** a solution tends to be versus **how much it can do**. It is **not** measured in milliseconds or MB on a standard benchmark — upstream configs and hardware dominate real numbers.

**Scales (1 = low, 5 = high):**

| Axis | What we mean |
|------|----------------|
| **Speed** | Typical cold start and responsiveness of the **runtime** (native binary vs heavy Node/Python stacks; edge firmware vs full assistant). |
| **Lightness** | Resident **RAM**, binary size, and dependency surface (lighter = higher score). |
| **Functionality** | Breadth of **product features**: channels, MCP, skills, migration, enterprise options — not “code quality.” |

**Rule:** you cannot maximize all three at once. High **Functionality** usually lowers **Lightness** for comparable agent classes.

### 12.1 Main ecosystem agents (from §1)

| Project | Speed | Lightness | Functionality | Efficiency profile |
|---------|------:|----------:|--------------:|---------------------|
| [OpenClaw](https://github.com/openclaw/openclaw) | 2 | 1 | 5 | **Maximum features**; heaviest class — plan RAM and ops |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 3 | 2 | 5 | **Feature-rich Python**; better than OpenClaw on lean deploy options (SSH/Docker/serverless per docs), still not “tiny” |
| [Nanobot](https://github.com/HKUDS/nanobot) | 4 | 4 | 3 | **Strong balance**: relatively light, still a real agent |
| [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) | 5 | 5 | 3 | **Best lean full-path agent** in this table for many users (~MB RAM narrative) |
| [AstrBot](https://github.com/AstrBotDevs/AstrBot) | 3 | 3 | 4 | **IM-first**; efficiency depends on plugin load |
| [PicoClaw](https://github.com/sipeed/picoclaw) | 4 | 4 | 3 | **Edge / gateway**; Go binary, cheap hardware |
| [NanoClaw](https://github.com/qwibitai/nanoclaw) (qwibitai) | 3 | 3 | 3 | Containers add overhead; security trade-off |
| [IronClaw](https://github.com/nearai/ironclaw) | 3 | 3 | 3 | **Security** (WASM) over raw speed |
| [GoClaw](https://github.com/nextlevelbuilder/goclaw) | 3 | 2 | 4 | **Go + Postgres + multi-tenant** — server efficiency, not laptop-minimal |
| [MicroClaw](https://github.com/microclaw/microclaw) | 4 | 4 | 2 | **Framework** — you bring features |
| [BeamClaw](https://github.com/peterdmv/beamclaw) | 4 | 3 | 2 | **Infra gateway** — OTP HA, not a personal assistant |
| [mcp-use](https://github.com/mcp-use/mcp-use) | — | — | — | **Library**, not a deployable agent — skip this row for “assistant efficiency” |

### 12.2 Extreme lightweight & niche (from [REFERENCE.md](REFERENCE.md))

| Project | Speed | Lightness | Functionality | Efficiency profile |
|---------|------:|----------:|--------------:|---------------------|
| [NullClaw](https://github.com/nullclaw/nullclaw) | 5 | 5 | 2 | **Binary size / startup** — Zig; narrow vs full OpenClaw parity |
| [SubZeroClaw](https://github.com/jmlago/subzeroclaw) | 5 | 5 | 1 | **~54KB** class — skill-driven edge |
| [TinyClaw](https://github.com/jlia0/tinyclaw) (400 lines) | 4 | 5 | 1 | **Minimal codebase** — learning / experiments |
| [ZeptoClaw](https://github.com/qhkm/zeptoclaw) | 3 | 4 | 2 | Security layers add cost vs bare metal |
| [MimiClaw](https://github.com/memovai/mimiclaw) | 5 | 5 | 1 | **MCU / ESP32** — ultra-constrained |

### 12.3 Who wins “efficiency-first”?

| Your priority | Favour these |
|---------------|----------------|
| **Fast + light + still an “agent”** (not a toy) | **ZeroClaw**, then **Nanobot**, then **PicoClaw** (edge) |
| **Fast + light + extreme** (embedded / kB binary) | **NullClaw**, **SubZeroClaw**, **MimiClaw** |
| **Most capability per repo star** (accept weight) | **OpenClaw**, **Hermes Agent** |
| **Chat platforms only, moderate weight** | **AstrBot** |
| **Enterprise service efficiency (Go/DB)** | **GoClaw** |

---

## Contributing

If a row is outdated or wrong, open an issue or PR with a link to the **specific upstream doc or source file** that should replace it.
