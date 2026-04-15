# OpenClaw Ecosystem — Extended Reference

*Full tables, repository links, category summary. For data update scripts, see [README.md#updating-data](README.md#updating-data). For **technical stack comparison** (MCP, skills, channels, persistence), see [comparison.md](comparison.md). For **GitHub stars by month**, see [STARS_BY_MONTH.md](STARS_BY_MONTH.md) and [scripts/data/stars_monthly_history.json](scripts/data/stars_monthly_history.json).*

---

## Repository Links

**Main:**
- https://github.com/sipeed/picoclaw
- https://github.com/HKUDS/nanobot
- https://github.com/nextlevelbuilder/goclaw
- https://github.com/NousResearch/hermes-agent
- https://github.com/openclaw/openclaw
- https://github.com/qwibitai/nanoclaw
- https://github.com/zeroclaw-labs/zeroclaw
- https://github.com/microclaw/microclaw
- https://github.com/ysz/nanoClaw
- https://github.com/peterdmv/beamclaw
- https://github.com/AstrBotDevs/AstrBot
- https://github.com/mcp-use/mcp-use
- https://github.com/nearai/ironclaw
- https://github.com/VoltAgent/awesome-openclaw-skills

**Additional alternatives** (from [awesome-openclaw-alternatives](https://github.com/T31K/awesome-openclaw-alternatives), [awesome-openclaw](https://github.com/vincentkoc/awesome-openclaw)):
- https://github.com/nullclaw/nullclaw — NullClaw (Zig, 678KB, <2ms startup)
- https://github.com/memovai/mimiclaw — MimiClaw (C, ESP32-S3 bare-metal)
- https://github.com/jlia0/tinyclaw — TinyClaw 400 (OpenClaw in 400 lines)
- https://github.com/tnm/zclaw — zclaw (C, ESP32)
- https://github.com/openagen/zeroclaw — ZeroClaw (Rust, openagen)
- https://github.com/qhkm/zeptoclaw — ZeptoClaw (Rust, 7-layer security)
- https://github.com/warengonzaga/tinyclaw — TinyClaw (Shell/TS, multi-agent)
- https://github.com/brendanhogan/hermitclaw — HermitClaw (Python, autonomous research)
- https://github.com/jmlago/subzeroclaw — SubZeroClaw (C, edge, ~54KB binary)
- https://github.com/princezuda/safeclaw — Safeclaw (Python, no LLM, intent recognition)
- https://github.com/puremachinery/carapace — Carapace (security, sandboxing)
- https://github.com/vincenzodomina/supaclaw — SupaClaw (Supabase-based)
- https://github.com/shimaenaga1123/rustclaw — RustClaw (Rust, Discord)

---

## Recommendation: What to Choose

| Goal | Project |
|------|--------|
| **Universal choice** | [**Nanobot**](https://github.com/HKUDS/nanobot) — balanced features, Python, active community |
| Maximum features | [**OpenClaw**](https://github.com/openclaw/openclaw) — reference implementation, 15+ channels, voice, Canvas |
| Self-improving / research | [**Hermes Agent**](https://github.com/NousResearch/hermes-agent) — Nous Research; learning loop, MCP, gateway; OpenClaw migration |
| Go at scale | [**GoClaw**](https://github.com/nextlevelbuilder/goclaw) — OpenClaw in Go, multi-tenant, 5-layer security, MCP |
| Minimum RAM | [**ZeroClaw**](https://github.com/zeroclaw-labs/zeroclaw) / [**NullClaw**](https://github.com/nullclaw/nullclaw) — ~5MB / 678KB |
| Edge / IoT | [**PicoClaw**](https://github.com/sipeed/picoclaw) / [**MimiClaw**](https://github.com/memovai/mimiclaw) — Go / C, ESP32 |
| Security | [**IronClaw**](https://github.com/nearai/ironclaw) / [**ZeptoClaw**](https://github.com/qhkm/zeptoclaw) — Rust, sandbox |
| IM Chatbot | [**AstrBot**](https://github.com/AstrBotDevs/AstrBot) — Python, many platforms |
| Minimalism | [**TinyClaw**](https://github.com/jlia0/tinyclaw) — OpenClaw in 400 lines |

---

## Comparison Table

*Sorted by popularity (⭐ stars, 🍴 forks)*

| Project | ⭐ | 🍴 | Language | Created | Organization | Type | Docker | Description | Features |
|---------|---:|---:|----------|---------|-------------|------|--------|-------------|----------|
| [**OpenClaw**](https://github.com/openclaw/openclaw) | 357 576 | 72 640 | TypeScript | 2025-11 | openclaw | AI agent | ✅ | Open personal AI agent. MCP, AWS EC2. | Core ecosystem project |
| [**Hermes Agent**](https://github.com/NousResearch/hermes-agent) | 85 892 | 11 639 | Python | 2025-07 | NousResearch | AI agent | ✅ | Self-improving agent; skills, memory, gateway. | OpenClaw migration, MCP |
| [**awesome-openclaw-skills**](https://github.com/VoltAgent/awesome-openclaw-skills) | 46 054 | 4 490 | — | 2026-01 | VoltAgent | Resource | — | Curated OpenClaw skills collection. | 5400+ skills |
| [**Nanobot**](https://github.com/HKUDS/nanobot) | 39 549 | 6 930 | Python | 2026-02 | HKUDS | AI agent | ✅ | Ultra-lightweight OpenClaw alternative. MCP. | Multi-instance, channels |
| [**ZeroClaw**](https://github.com/zeroclaw-labs/zeroclaw) | 30 153 | 4 351 | Rust | 2026-02 | zeroclaw-labs | AI agent | ✅ | Lightweight agent, ~5MB RAM. | OpenClaw migration |
| [**AstrBot**](https://github.com/AstrBotDevs/AstrBot) | 29 976 | 2 022 | Python | 2022-12 | AstrBotDevs | Chatbot | ✅ | IM platforms, LLM (GPT, Gemini, Llama). | AGPL-3.0 |
| [**PicoClaw**](https://github.com/sipeed/picoclaw) | 28 154 | 4 006 | Go | 2026-02 | sipeed | Migration / Edge | ✅ | Workspace migration, gateway node. | Edge, $10 hardware |
| [**NanoClaw** (qwibitai)](https://github.com/qwibitai/nanoclaw) | 27 292 | 11 972 | TypeScript | 2026-01 | qwibitai | AI agent | ✅ | Containers, WhatsApp, Telegram, Slack. | AI-native |
| [**IronClaw**](https://github.com/nearai/ironclaw) | 11 780 | 1 348 | Rust | 2026-02 | nearai | AI agent | ✅ | Rust, privacy, security. | WebAssembly sandbox |
| [**mcp-use**](https://github.com/mcp-use/mcp-use) | 9 772 | 1 242 | TypeScript | 2025-03 | mcp-use | MCP Framework | — | MCP Apps and MCP Servers. | Python/JS, LangChain |
| [**GoClaw**](https://github.com/nextlevelbuilder/goclaw) | 2 706 | 683 | Go | 2026-02 | nextlevelbuilder | AI agent | ✅ | OpenClaw rebuilt in Go. Multi-tenant, PostgreSQL. | 5-layer security, MCP |
| [**MicroClaw**](https://github.com/microclaw/microclaw) | 649 | 120 | Rust | 2026-02 | microclaw | AI agent | ✅ | Agentic framework. | MCP, HTTP transport |
| [**NanoClaw** (ysz)](https://github.com/ysz/nanoClaw) | 61 | 18 | Python | 2026-02 | ysz | AI agent | ✅ | Minimalism, isolated containers. | Agent Swarms |
| [**BeamClaw**](https://github.com/peterdmv/beamclaw) | 0 | 2 | Erlang | 2026-02 | peterdmv | Gateway / MCP | ✅ | Fault-tolerant gateway, MCP host. | Erlang/OTP |

### Additional Alternatives

| Project | ⭐ | 🍴 | Language | Created | Description |
|---------|---:|---:|----------|---------|-------------|
| [**NullClaw**](https://github.com/nullclaw/nullclaw) | 7 195 | 843 | Zig | 2026-02 | 678KB, <2ms startup, 22+ providers, Arduino/RPi |
| [**MimiClaw**](https://github.com/memovai/mimiclaw) | 5 174 | 757 | C | 2026-02 | ESP32-S3 bare-metal, ~$5, 0.5W |
| [**TinyClaw** (jlia0)](https://github.com/jlia0/tinyclaw) | 3 510 | 504 | TypeScript | 2026-02 | OpenClaw in 400 lines |
| [**zclaw**](https://github.com/tnm/zclaw) | 2 074 | 177 | C | 2026-02 | ESP32, Seeed XIAO, GPIO, Telegram |
| [**ZeroClaw** (openagen)](https://github.com/openagen/zeroclaw) | 1 808 | 267 | Rust | 2026-02 | 3.4MB, <10ms startup, trait-based |
| [**ZeptoClaw**](https://github.com/qhkm/zeptoclaw) | 589 | 87 | Rust | 2026-02 | 7-layer security, OpenClaw migration |
| [**HermitClaw**](https://github.com/brendanhogan/hermitclaw) | 319 | 54 | Python | 2026-02 | Autonomous research agent |
| [**TinyClaw** (warengonzaga)](https://github.com/warengonzaga/tinyclaw) | 218 | 33 | TypeScript | 2026-02 | Multi-agent, Claude Code + tmux |
| [**SubZeroClaw**](https://github.com/jmlago/subzeroclaw) | 119 | 14 | C | 2026-02 | Edge, ~54KB, skill-driven |
| [**Safeclaw**](https://github.com/princezuda/safeclaw) | 131 | 15 | Python | 2026-02 | No LLM, intent recognition, $0 API |
| [**SupaClaw**](https://github.com/vincenzodomina/supaclaw) | 58 | 10 | TypeScript | 2026-02 | OpenClaw on Supabase |
| [**Carapace**](https://github.com/puremachinery/carapace) | 43 | 6 | Rust | 2026-01 | Security, sandboxing |
| [**RustClaw**](https://github.com/shimaenaga1123/rustclaw) | 4 | 1 | Rust | 2026-02 | Discord AI assistant |

---

## Quick Start (Docker) — Setup Time

| Project | ~Time |
|---------|-------|
| [**OpenClaw**](https://github.com/openclaw/openclaw) | 180–300 sec |
| [**Hermes Agent**](https://github.com/NousResearch/hermes-agent) | 90–180 sec |
| [**Nanobot**](https://github.com/HKUDS/nanobot) | 90–150 sec |
| [**ZeroClaw**](https://github.com/zeroclaw-labs/zeroclaw) | 60–90 sec |
| [**PicoClaw**](https://github.com/sipeed/picoclaw) | 90–120 sec |
| [**AstrBot**](https://github.com/AstrBotDevs/AstrBot) | 90–120 sec |
| [**MicroClaw**](https://github.com/microclaw/microclaw) | 60–90 sec |
| [**IronClaw**](https://github.com/nearai/ironclaw) | 90–120 sec |
| [**NanoClaw** (qwibitai)](https://github.com/qwibitai/nanoclaw) | ~120 sec |
| [**NanoClaw** (ysz)](https://github.com/ysz/nanoClaw) | ~180 sec |

---

## Category Summary

| Category | Projects |
|----------|----------|
| **Full AI agents** | [OpenClaw](https://github.com/openclaw/openclaw), [Hermes Agent](https://github.com/NousResearch/hermes-agent), [Nanobot](https://github.com/HKUDS/nanobot), [GoClaw](https://github.com/nextlevelbuilder/goclaw), [NanoClaw](https://github.com/qwibitai/nanoclaw), [NanoClaw](https://github.com/ysz/nanoClaw), [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw), [MicroClaw](https://github.com/microclaw/microclaw), [IronClaw](https://github.com/nearai/ironclaw) |
| **Edge / IoT** | [PicoClaw](https://github.com/sipeed/picoclaw), [NullClaw](https://github.com/nullclaw/nullclaw), [zclaw](https://github.com/tnm/zclaw), [MimiClaw](https://github.com/memovai/mimiclaw), [SubZeroClaw](https://github.com/jmlago/subzeroclaw) |
| **Gateway / MCP Host** | [BeamClaw](https://github.com/peterdmv/beamclaw) |
| **MCP Framework** | [mcp-use](https://github.com/mcp-use/mcp-use) |
| **Chatbot / IM** | [AstrBot](https://github.com/AstrBotDevs/AstrBot) |
| **Security-focused** | [IronClaw](https://github.com/nearai/ironclaw), [ZeptoClaw](https://github.com/qhkm/zeptoclaw), [Safeclaw](https://github.com/princezuda/safeclaw), [Carapace](https://github.com/puremachinery/carapace) |
| **Minimalist** | [TinyClaw](https://github.com/jlia0/tinyclaw), [TinyClaw](https://github.com/warengonzaga/tinyclaw), [HermitClaw](https://github.com/brendanhogan/hermitclaw) |
| **Skills / Resources** | [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) |

---

*Stars, forks, language, creation date: GitHub API (April 2026). Discover more: [topic openclaw-alternative](https://github.com/topics/openclaw-alternative).*
