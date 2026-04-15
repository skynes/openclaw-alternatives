# OpenClaw Alternatives: From Giants to Micro-Agents

*Last updated: April 2026*

**Translations:** [English](README.md) · [中文](README.zh-CN.md) · [Español](README.es.md) · [日本語](README.ja.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

![Cover](cover.png)

---

In this overview we explore the current projects: from the flagship OpenClaw to extremely lightweight solutions like NullClaw that start faster than you can blink.

## 🧭 What to Choose? Quick Navigator

If you need to get up and running quickly, here's what we're here for:


| Goal                  | Recommended Project                                       | Why?                                                                                                       |
| --------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Universal choice**  | **[Nanobot](https://github.com/HKUDS/nanobot)**           | Golden mean: Python, active community, multi-instance support, not very demanding on hardware (RAM 300MB+) |
| **Maximum power**     | **[OpenClaw](https://github.com/openclaw/openclaw)**      | The standard, and that says it all. 15+ communication channels, voice, Canvas support, RAM 2GB+            |
| **Self-improving / research** | **[Hermes Agent](https://github.com/NousResearch/hermes-agent)** | Nous Research: learning loop, skills & memory, MCP, multi-platform gateway; `hermes claw migrate` from OpenClaw |
| **For weak machines** | **[ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw)** | Rust engine, consumes only ~5MB RAM                                                                        |
| **IoT and Edge**      | **[PicoClaw](https://github.com/sipeed/picoclaw)**        | Runs on hardware for $10 (ESP32 and similar)                                                               |
| **Security**          | **[IronClaw](https://github.com/nearai/ironclaw)**        | WebAssembly sandbox and paranoid approach to privacy                                                       |
| **Go / scale**        | **[GoClaw](https://github.com/nextlevelbuilder/goclaw)** | OpenClaw rebuilt in Go: multi-tenant isolation, 5-layer security, native concurrency                        |
| **Minimalism**        | **[TinyClaw](https://github.com/jlia0/tinyclaw)**         | Just 400 lines of code. Perfect for learning                                                               |


## 📊 Comparison Table

Sorting by popularity and project activity on GitHub (data as of April 2026).


| Project                                                   | ⭐ Stars | Language   | Type     | Features                                       |
| --------------------------------------------------------- | ------- | ---------- | -------- | ---------------------------------------------- |
| **[OpenClaw](https://github.com/openclaw/openclaw)**      | 357k    | TypeScript | AI-agent | Base project, MCP and AWS EC2 support          |
| **[Hermes Agent](https://github.com/NousResearch/hermes-agent)** | 86k | Python     | AI-agent | Learning loop, skills, gateway, OpenClaw migration |
| **[Nanobot](https://github.com/HKUDS/nanobot)**           | 39k     | Python     | AI-agent | Multi-instance, ultra-lightweight              |
| **[ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw)** | 30k     | Rust       | AI-agent | Memory usage ~5MB, fast startup                |
| **[AstrBot](https://github.com/AstrBotDevs/AstrBot)**     | 29k     | Python     | Chatbot  | Focus on IM platforms (TG, WhatsApp)           |
| **[PicoClaw](https://github.com/sipeed/picoclaw)**        | 28k     | Go         | Edge/IoT | Works as a node in gateway, cheap hardware     |
| **[NanoClaw](https://github.com/qwibitai/nanoclaw)**      | 27k     | TypeScript | AI-agent | Containerization, focus on business messengers |
| **[IronClaw](https://github.com/nearai/ironclaw)**        | 11.8k   | Rust       | AI-agent | WASM sandbox, maximum isolation                |
| **[GoClaw](https://github.com/nextlevelbuilder/goclaw)**  | 2.7k    | Go         | AI-agent | Multi-tenant, 5-layer security, MCP, Postgres  |

*Rounded star counts; exact figures: [scripts/data/github_stats.json](scripts/data/github_stats.json). Live star badges: [shields.io](https://shields.io/badges/git-hub-repo-stars) (`https://img.shields.io/github/stars/<owner>/<repo>`).*

## 🛠 Niche Alternatives and «Micro-Lobsters»

For those looking for specific solutions — from bare-metal to Erlang systems.

### Performance and Edge

- **[NullClaw](https://github.com/nullclaw/nullclaw)** (Zig): Fantastic performance. 678KB binary, startup <2ms. Suitable for Arduino and RPi.
- **[MimiClaw](https://github.com/memovai/mimiclaw)** (C): Runs on ESP32-S3 bare-metal. Solution cost ~$5.
- **[SubZeroClaw](https://github.com/jmlago/subzeroclaw)** (C): Only 54KB.

### Security and Fault Tolerance

- **[ZeptoClaw](https://github.com/qhkm/zeptoclaw)**: 7-layer security system on Rust.
- **[BeamClaw](https://github.com/peterdmv/beamclaw)**: Written in Erlang/OTP for distributed systems.
- **[Safeclaw](https://github.com/princezuda/safeclaw)**: Works without LLM (intent recognition), guaranteeing 100% predictability.

## 🚀 Quick Start

For those who've been wanting to try for a while — we've collected commands to launch the most popular branches. Setup time: up to 3 minutes.

### 1. Nanobot (Fastest entry)

```bash
git clone https://github.com/HKUDS/nanobot.git && cd nanobot
docker compose run --rm nanobot-cli onboard
# Add your API key to ~/.nanobot/config.json
docker compose up -d nanobot-gateway
```

### 2. ZeroClaw (minimal configuration)

```bash
git clone https://github.com/zeroclaw-labs/zeroclaw.git && cd zeroclaw
cp .env.example .env   # set API_KEY
docker compose up -d
```

### 3. PicoClaw

```bash
git clone https://github.com/sipeed/picoclaw.git && cd picoclaw
docker compose -f docker/docker-compose.yml --profile gateway up   # first run
vim docker/data/config.json   # API keys, bot tokens
docker compose -f docker/docker-compose.yml --profile gateway up -d
```

### 4. OpenClaw

```bash
git clone https://github.com/openclaw/openclaw.git && cd openclaw
./docker-setup.sh   # wizard, image build, first run
```

## Useful Resources

- **Skills / Resources:** [clawhub](https://github.com/clawhub) / [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)
- **Discover more repos:** GitHub topic [`openclaw-alternative`](https://github.com/topics/openclaw-alternative)

---

## Updating Data {#updating-data}

**GitHub (stars, forks):**

```powershell
python scripts/fetch_github_stats.py
```

Results → `scripts/data/github_stats.json`

To record **before → after** stars/forks, copy the current file to `scripts/data/github_stats_before_refresh.json`, then run the script again; a diff is written to `scripts/data/STATS_REFRESH_LOG.txt` when that snapshot exists.

**Monthly star history (comparison by month):**

- Data: [scripts/data/stars_monthly_history.json](scripts/data/stars_monthly_history.json)
- Human-readable table: [STARS_BY_MONTH.md](STARS_BY_MONTH.md)
- After each monthly fetch: `python scripts/append_stars_monthly.py` then `python scripts/render_stars_by_month_md.py`

**Tavily (project descriptions):**

```powershell
$env:TAVILY_API_KEY="your-api-key"
python scripts/compare_projects.py
```

Results → `scripts/data/tavily_results.json`

For full repository links, extended tables, and category summary, see [REFERENCE.md](REFERENCE.md).

**Technical stack & integration comparison** (MCP, skills, APIs, persistence, deployment): [comparison.md](comparison.md).

---

## 💡 Suggest Other Projects

**If we missed a project, please suggest it!** Open an [Issue](https://github.com/skynes/openclaw-alternatives/issues) or submit a Pull Request — we'll compare and add it to the overview.