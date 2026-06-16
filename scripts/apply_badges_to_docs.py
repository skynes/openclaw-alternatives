#!/usr/bin/env python3
"""
Inject live shields.io badges into markdown docs.
Run after fetch_github_stats.py when tables change.
"""
from __future__ import annotations

import re
from pathlib import Path

from badges import forks, stars

ROOT = Path(__file__).parent.parent

# repo slug -> display name variants in markdown links
RANKING = [
    ("openclaw/openclaw", "OpenClaw"),
    ("NousResearch/hermes-agent", "Hermes Agent"),
    ("pewdiepie-archdaemon/odysseus", "Odysseus"),
    ("VoltAgent/awesome-openclaw-skills", "awesome-openclaw-skills"),
    ("HKUDS/nanobot", "Nanobot"),
    ("AstrBotDevs/AstrBot", "AstrBot"),
    ("zeroclaw-labs/zeroclaw", "ZeroClaw"),
    ("qwibitai/nanoclaw", "NanoClaw"),
    ("sipeed/picoclaw", "PicoClaw"),
    ("nearai/ironclaw", "IronClaw"),
    ("mcp-use/mcp-use", "mcp-use"),
    ("nullclaw/nullclaw", "NullClaw"),
    ("memovai/mimiclaw", "MimiClaw"),
    ("jlia0/tinyclaw", "TinyClaw"),
    ("nextlevelbuilder/goclaw", "GoClaw"),
    ("tnm/zclaw", "zclaw"),
    ("openagen/zeroclaw", "ZeroClaw"),
    ("microclaw/microclaw", "MicroClaw"),
    ("qhkm/zeptoclaw", "ZeptoClaw"),
    ("brendanhogan/hermitclaw", "HermitClaw"),
    ("princezuda/safeclaw", "Safeclaw"),
    ("warengonzaga/tinyclaw", "TinyClaw"),
    ("jmlago/subzeroclaw", "SubZeroClaw"),
    ("RikyZ90/ShibaClaw", "ShibaClaw"),
    ("ysz/nanoClaw", "NanoClaw"),
    ("vincenzodomina/supaclaw", "SupaClaw"),
    ("puremachinery/carapace", "Carapace"),
    ("shimaenaga1123/rustclaw", "RustClaw"),
    ("peterdmv/beamclaw", "BeamClaw"),
]

MAIN_README_ROWS = [
    ("openclaw/openclaw", "379k", "TypeScript"),
    ("NousResearch/hermes-agent", "195k", "Python"),
    ("HKUDS/nanobot", "44k", "Python"),
    ("AstrBotDevs/AstrBot", "35k", "Python"),
    ("zeroclaw-labs/zeroclaw", "32k", "Rust"),
    ("qwibitai/nanoclaw", "30k", "TypeScript"),
    ("sipeed/picoclaw", "29k", "Go"),
    ("nearai/ironclaw", "12k", "Rust"),
    ("nextlevelbuilder/goclaw", "3.3k", "Go"),
]

README_LANG_TABLES: dict[str, dict] = {
    "README.de.md": {
        "header": "| Projekt | Live ⭐ | ⭐ Stars | Sprache | Typ | Merkmale |",
        "divider": "|---------|---------|---------|---------|-----|----------|",
        "rows": [
            ("openclaw/openclaw", "379k", "TypeScript", "KI-Agent", "Basisprojekt, MCP- und AWS-EC2-Support"),
            ("NousResearch/hermes-agent", "195k", "Python", "KI-Agent", "Lernschleife, Skills, Gateway, OpenClaw-Migration"),
            ("HKUDS/nanobot", "44k", "Python", "KI-Agent", "Multi-Instanz, ultra-leichtgewichtig"),
            ("AstrBotDevs/AstrBot", "35k", "Python", "Chatbot", "Fokus auf IM-Plattformen (TG, WhatsApp)"),
            ("zeroclaw-labs/zeroclaw", "32k", "Rust", "KI-Agent", "Speicherverbrauch ~5MB, schneller Start"),
            ("qwibitai/nanoclaw", "30k", "TypeScript", "KI-Agent", "Containerisierung, Fokus auf Business-Messenger"),
            ("sipeed/picoclaw", "29k", "Go", "Edge/IoT", "Läuft als Knoten im Gateway, günstige Hardware"),
            ("nearai/ironclaw", "12k", "Rust", "KI-Agent", "WASM-Sandbox, maximale Isolation"),
            ("nextlevelbuilder/goclaw", "3.3k", "Go", "KI-Agent", "Multi-Tenant, 5-Schicht-Sicherheit, MCP, Postgres"),
        ],
    },
    "README.es.md": {
        "header": "| Proyecto | Live ⭐ | ⭐ Stars | Lenguaje | Tipo | Características |",
        "divider": "|----------|---------|---------|----------|------|-----------------|",
        "rows": [
            ("openclaw/openclaw", "379k", "TypeScript", "Agente IA", "Proyecto base, soporte MCP y AWS EC2"),
            ("NousResearch/hermes-agent", "195k", "Python", "Agente IA", "Aprendizaje, skills, gateway, migración OpenClaw"),
            ("HKUDS/nanobot", "44k", "Python", "Agente IA", "Multi-instancia, ultra ligero"),
            ("AstrBotDevs/AstrBot", "35k", "Python", "Chatbot", "Enfocado en plataformas IM (TG, WhatsApp)"),
            ("zeroclaw-labs/zeroclaw", "32k", "Rust", "Agente IA", "Uso de memoria ~5MB, arranque rápido"),
            ("qwibitai/nanoclaw", "30k", "TypeScript", "Agente IA", "Containerización, enfoque en mensajería empresarial"),
            ("sipeed/picoclaw", "29k", "Go", "Edge/IoT", "Funciona como nodo en gateway, hardware barato"),
            ("nearai/ironclaw", "12k", "Rust", "Agente IA", "Sandbox WASM, máximo aislamiento"),
            ("nextlevelbuilder/goclaw", "3.3k", "Go", "Agente IA", "Multi-tenant, seguridad en 5 capas, MCP, Postgres"),
        ],
    },
    "README.ja.md": {
        "header": "| プロジェクト | Live ⭐ | ⭐ Stars | 言語 | タイプ | 特徴 |",
        "divider": "|-------------|---------|---------|------|--------|------|",
        "rows": [
            ("openclaw/openclaw", "379k", "TypeScript", "AIエージェント", "基盤プロジェクト、MCP・AWS EC2 対応"),
            ("NousResearch/hermes-agent", "195k", "Python", "AIエージェント", "学習ループ、スキル、ゲートウェイ、OpenClaw 移行"),
            ("HKUDS/nanobot", "44k", "Python", "AIエージェント", "マルチインスタンス、超軽量"),
            ("AstrBotDevs/AstrBot", "35k", "Python", "チャットボット", "IM プラットフォーム対応（TG、WhatsApp）"),
            ("zeroclaw-labs/zeroclaw", "32k", "Rust", "AIエージェント", "メモリ使用 ~5MB、高速起動"),
            ("qwibitai/nanoclaw", "30k", "TypeScript", "AIエージェント", "コンテナ化、ビジネスメッセンジャー向け"),
            ("sipeed/picoclaw", "29k", "Go", "Edge/IoT", "ゲートウェイノード、低コストハードウェア"),
            ("nearai/ironclaw", "12k", "Rust", "AIエージェント", "WASM サンドボックス、最大分離"),
            ("nextlevelbuilder/goclaw", "3.3k", "Go", "AIエージェント", "マルチテナント、5 層セキュリティ、MCP、Postgres"),
        ],
    },
    "README.zh-CN.md": {
        "header": "| 项目 | Live ⭐ | ⭐ Stars | 语言 | 类型 | 特点 |",
        "divider": "|------|---------|---------|------|------|------|",
        "rows": [
            ("openclaw/openclaw", "379k", "TypeScript", "AI 代理", "基础项目，支持 MCP 和 AWS EC2"),
            ("NousResearch/hermes-agent", "195k", "Python", "AI 代理", "学习循环、技能、网关、OpenClaw 迁移"),
            ("HKUDS/nanobot", "44k", "Python", "AI 代理", "多实例、超轻量"),
            ("AstrBotDevs/AstrBot", "35k", "Python", "聊天机器人", "专注 IM 平台（TG、WhatsApp）"),
            ("zeroclaw-labs/zeroclaw", "32k", "Rust", "AI 代理", "内存占用 ~5MB，快速启动"),
            ("qwibitai/nanoclaw", "30k", "TypeScript", "AI 代理", "容器化，专注商业通讯"),
            ("sipeed/picoclaw", "29k", "Go", "Edge/IoT", "作为网关节点，廉价硬件"),
            ("nearai/ironclaw", "12k", "Rust", "AI 代理", "WASM 沙箱，最大隔离"),
            ("nextlevelbuilder/goclaw", "3.3k", "Go", "AI 代理", "多租户、五层安全、MCP、Postgres"),
        ],
    },
}

NICHE_REPOS = [
    "nullclaw/nullclaw",
    "memovai/mimiclaw",
    "jmlago/subzeroclaw",
    "qhkm/zeptoclaw",
    "peterdmv/beamclaw",
    "princezuda/safeclaw",
    "RikyZ90/ShibaClaw",
]


def _link_name(repo: str) -> str:
    special = {
        "openclaw": "OpenClaw",
        "hermes-agent": "Hermes Agent",
        "nanobot": "Nanobot",
        "AstrBot": "AstrBot",
        "zeroclaw": "ZeroClaw",
        "nanoclaw": "NanoClaw",
        "picoclaw": "PicoClaw",
        "ironclaw": "IronClaw",
        "goclaw": "GoClaw",
        "nullclaw": "NullClaw",
        "mimiclaw": "MimiClaw",
        "subzeroclaw": "SubZeroClaw",
        "zeptoclaw": "ZeptoClaw",
        "beamclaw": "BeamClaw",
        "safeclaw": "Safeclaw",
        "ShibaClaw": "ShibaClaw",
        "mcp-use": "mcp-use",
        "awesome-openclaw-skills": "awesome-openclaw-skills",
        "odysseus": "Odysseus",
        "zclaw": "zclaw",
        "microclaw": "MicroClaw",
        "hermitclaw": "HermitClaw",
        "tinyclaw": "TinyClaw",
        "supaclaw": "SupaClaw",
        "carapace": "Carapace",
        "rustclaw": "RustClaw",
        "nanoClaw": "NanoClaw",
    }
    base = repo.split("/", 1)[1]
    return special.get(base, base)


def readme_table_row(repo: str, stars_txt: str, lang: str, typ: str, features: str) -> str:
    name = _link_name(repo)
    return (
        f"| [**{name}**](https://github.com/{repo}) "
        f"| {stars(repo)} "
        f"| {stars_txt} | {lang} | {typ} | {features} |"
    )


def build_readme_lang_table(cfg: dict) -> str:
    lines = [cfg["header"], cfg["divider"]]
    for row in cfg["rows"]:
        lines.append(readme_table_row(*row))
    return "\n".join(lines)


def inject_niche_badges(text: str) -> str:
    for repo in NICHE_REPOS:
        name = _link_name(repo)
        url = f"https://github.com/{repo}"
        badge = stars(repo)
        for pattern in (
            rf"(\*\*\[{re.escape(name)}\]\({re.escape(url)}\)\*\*)",
            rf"(\[\*\*{re.escape(name)}\*\*\]\({re.escape(url)}\))",
        ):
            text = re.sub(
                rf"{pattern}(?!\s+\[!\[stars\])",
                rf"\1 {badge}",
                text,
            )
    return text


def inject_link_list_badges(text: str) -> str:
    def repl(m: re.Match) -> str:
        url = m.group(1)
        suffix = m.group(2) or ""
        if "[![stars]" in m.group(0):
            return m.group(0)
        repo = url.replace("https://github.com/", "")
        return f"- {url} {stars(repo)} {forks(repo)}{suffix}"

    return re.sub(
        r"^- (https://github\.com/\S+)([^\n]*)$",
        repl,
        text,
        flags=re.MULTILINE,
    )


def render_comparison_ranking() -> str:
    import json

    stats = json.loads((ROOT / "scripts/data/github_stats.json").read_text(encoding="utf-8"))
    key_map = {
        "openclaw/openclaw": "openclaw",
        "NousResearch/hermes-agent": "hermes-agent",
        "pewdiepie-archdaemon/odysseus": "odysseus",
        "VoltAgent/awesome-openclaw-skills": "awesome-openclaw-skills",
        "HKUDS/nanobot": "nanobot",
        "AstrBotDevs/AstrBot": "AstrBot",
        "zeroclaw-labs/zeroclaw": "zeroclaw",
        "qwibitai/nanoclaw": "nanoclaw",
        "sipeed/picoclaw": "picoclaw",
        "nearai/ironclaw": "ironclaw",
        "mcp-use/mcp-use": "mcp-use",
        "nullclaw/nullclaw": "nullclaw",
        "memovai/mimiclaw": "mimiclaw",
        "jlia0/tinyclaw": "tinyclaw-400",
        "nextlevelbuilder/goclaw": "goclaw",
        "tnm/zclaw": "zclaw",
        "openagen/zeroclaw": "zeroclaw-openagen",
        "microclaw/microclaw": "microclaw",
        "qhkm/zeptoclaw": "zeptoclaw",
        "brendanhogan/hermitclaw": "hermitclaw",
        "princezuda/safeclaw": "safeclaw",
        "warengonzaga/tinyclaw": "tinyclaw",
        "jmlago/subzeroclaw": "subzeroclaw",
        "RikyZ90/ShibaClaw": "shibaclaw",
        "ysz/nanoClaw": "nanoClaw",
        "vincenzodomina/supaclaw": "supaclaw",
        "puremachinery/carapace": "carapace",
        "shimaenaga1123/rustclaw": "rustclaw",
        "peterdmv/beamclaw": "beamclaw",
    }
    labels = {
        "qwibitai/nanoclaw": "NanoClaw (qwibitai)",
        "jlia0/tinyclaw": "TinyClaw (400-line)",
        "openagen/zeroclaw": "ZeroClaw (openagen)",
        "warengonzaga/tinyclaw": "TinyClaw (warengonzaga)",
        "ysz/nanoClaw": "NanoClaw (ysz)",
    }
    rows = []
    ranked = []
    for repo, _ in RANKING:
        key = key_map[repo]
        s = stats.get(key, {})
        if not s.get("stars") and s.get("stars") != 0:
            continue
        ranked.append((s.get("popularity", 0), repo, key, s.get("popularity", 0)))
    ranked.sort(key=lambda x: -x[0])

    lines = [
        "| Rank | Project | Live ⭐ | Live 🍴 | Score |",
        "|------|---------|---------|---------|------:|",
    ]
    for i, (_, repo, key, score) in enumerate(ranked, 1):
        label = labels.get(repo, _link_name(repo))
        lines.append(
            f"| {i} | [{label}](https://github.com/{repo}) "
            f"| {stars(repo)} | {forks(repo)} | {score:,} |".replace(",", " ")
        )
    return "\n".join(lines)


def render_reference_main_table() -> str:
    rows = [
        ("openclaw/openclaw", "TypeScript", "2025-11", "openclaw", "AI agent", "✅", "Open personal AI agent. MCP, AWS EC2.", "Core ecosystem project"),
        ("NousResearch/hermes-agent", "Python", "2025-07", "NousResearch", "AI agent", "✅", "Self-improving agent; skills, memory, gateway.", "OpenClaw migration, MCP"),
        ("VoltAgent/awesome-openclaw-skills", "—", "2026-01", "VoltAgent", "Resource", "—", "Curated OpenClaw skills collection.", "5400+ skills"),
        ("HKUDS/nanobot", "Python", "2026-02", "HKUDS", "AI agent", "✅", "Ultra-lightweight OpenClaw alternative. MCP.", "Multi-instance, channels"),
        ("AstrBotDevs/AstrBot", "Python", "2022-12", "AstrBotDevs", "Chatbot", "✅", "IM platforms, LLM (GPT, Gemini, Llama).", "AGPL-3.0"),
        ("zeroclaw-labs/zeroclaw", "Rust", "2026-02", "zeroclaw-labs", "AI agent", "✅", "Lightweight agent, ~5MB RAM.", "OpenClaw migration"),
        ("qwibitai/nanoclaw", "TypeScript", "2026-01", "qwibitai", "AI agent", "✅", "Containers, WhatsApp, Telegram, Slack.", "AI-native", "NanoClaw (qwibitai)"),
        ("sipeed/picoclaw", "Go", "2026-02", "sipeed", "Migration / Edge", "✅", "Workspace migration, gateway node.", "Edge, $10 hardware"),
        ("nearai/ironclaw", "Rust", "2026-02", "nearai", "AI agent", "✅", "Rust, privacy, security.", "WebAssembly sandbox"),
        ("mcp-use/mcp-use", "TypeScript", "2025-03", "mcp-use", "MCP Framework", "—", "MCP Apps and MCP Servers.", "Python/JS, LangChain"),
        ("nextlevelbuilder/goclaw", "Go", "2026-02", "nextlevelbuilder", "AI agent", "✅", "OpenClaw rebuilt in Go. Multi-tenant, PostgreSQL.", "5-layer security, MCP"),
        ("microclaw/microclaw", "Rust", "2026-02", "microclaw", "AI agent", "✅", "Agentic framework.", "MCP, HTTP transport"),
        ("ysz/nanoClaw", "Python", "2026-02", "ysz", "AI agent", "✅", "Minimalism, isolated containers.", "Agent Swarms", "NanoClaw (ysz)"),
        ("peterdmv/beamclaw", "Erlang", "2026-02", "peterdmv", "Gateway / MCP", "✅", "Fault-tolerant gateway, MCP host.", "Erlang/OTP"),
    ]
    header = (
        "| Project | Live ⭐ | Live 🍴 | Language | Created | Organization | Type | Docker | Description | Features |\n"
        "|---------|---------|---------|----------|---------|-------------|------|--------|-------------|----------|"
    )
    lines = [header]
    for row in rows:
        if len(row) == 9:
            repo, lang, created, org, typ, docker, desc, feat, label = row
        else:
            repo, lang, created, org, typ, docker, desc, feat = row
            label = _link_name(repo)
        lines.append(
            f"| [**{label}**](https://github.com/{repo}) "
            f"| {stars(repo)} | {forks(repo)} "
            f"| {lang} | {created} | {org} | {typ} | {docker} | {desc} | {feat} |"
        )
    return "\n".join(lines)


def render_reference_additional_table() -> str:
    rows = [
        ("nullclaw/nullclaw", "Zig", "2026-02", "678KB, <2ms startup, 22+ providers, Arduino/RPi"),
        ("memovai/mimiclaw", "C", "2026-02", "ESP32-S3 bare-metal, ~$5, 0.5W"),
        ("jlia0/tinyclaw", "TypeScript", "2026-02", "OpenClaw in 400 lines", "TinyClaw (jlia0)"),
        ("tnm/zclaw", "C", "2026-02", "ESP32, Seeed XIAO, GPIO, Telegram"),
        ("openagen/zeroclaw", "Rust", "2026-02", "3.4MB, <10ms startup, trait-based", "ZeroClaw (openagen)"),
        ("qhkm/zeptoclaw", "Rust", "2026-02", "7-layer security, OpenClaw migration"),
        ("brendanhogan/hermitclaw", "Python", "2026-02", "Autonomous research agent"),
        ("princezuda/safeclaw", "Python", "2026-02", "No LLM, intent recognition, $0 API"),
        ("warengonzaga/tinyclaw", "TypeScript", "2026-02", "Multi-agent, Claude Code + tmux", "TinyClaw (warengonzaga)"),
        ("RikyZ90/ShibaClaw", "Python", "2026-03", "Security-first; 22 providers, 11 channels, WebUI, MCP"),
        ("jmlago/subzeroclaw", "C", "2026-02", "Edge, ~54KB, skill-driven"),
        ("vincenzodomina/supaclaw", "TypeScript", "2026-02", "OpenClaw on Supabase"),
        ("puremachinery/carapace", "Rust", "2026-01", "Security, sandboxing"),
        ("shimaenaga1123/rustclaw", "Rust", "2026-02", "Discord AI assistant"),
    ]
    header = (
        "| Project | Live ⭐ | Live 🍴 | Language | Created | Description |\n"
        "|---------|---------|---------|----------|---------|-------------|"
    )
    lines = [header]
    for row in rows:
        if len(row) == 5:
            repo, lang, created, desc, label = row
        else:
            repo, lang, created, desc = row
            label = _link_name(repo)
        lines.append(
            f"| [**{label}**](https://github.com/{repo}) "
            f"| {stars(repo)} | {forks(repo)} "
            f"| {lang} | {created} | {desc} |"
        )
    return "\n".join(lines)


def replace_between(text: str, start: str, end: str, body: str) -> str:
    i = text.index(start)
    j = text.index(end, i)
    return text[:i] + start + "\n" + body + "\n" + text[j:]


def patch_readme_lang(path: Path, cfg: dict) -> None:
    text = path.read_text(encoding="utf-8")
    table = build_readme_lang_table(cfg)
    text = re.sub(
        r"\| (?:Projekt|Proyecto|プロジェクト|项目) \| ⭐ Stars.*?\n(?:\|[^\n]+\n)+",
        table + "\n",
        text,
        count=1,
        flags=re.DOTALL,
    )
    text = inject_niche_badges(text)
    path.write_text(text, encoding="utf-8")
    print(f"Updated {path.name}")


def main() -> None:
    for fname, cfg in README_LANG_TABLES.items():
        patch_readme_lang(ROOT / fname, cfg)

    for fname in ("README.md", "README.ru.md"):
        path = ROOT / fname
        text = inject_niche_badges(path.read_text(encoding="utf-8"))
        path.write_text(text, encoding="utf-8")
        print(f"Updated niche badges in {path.name}")

    ref = ROOT / "REFERENCE.md"
    ref_text = ref.read_text(encoding="utf-8")
    ref_text = inject_link_list_badges(ref_text)
    ref_text = replace_between(
        ref_text,
        "## Comparison Table\n\n*Sorted by popularity (⭐ stars, 🍴 forks)*\n\n",
        "\n### Additional Alternatives",
        render_reference_main_table(),
    )
    ref_text = replace_between(
        ref_text,
        "### Additional Alternatives\n\n",
        "\n---\n\n## Quick Start",
        render_reference_additional_table(),
    )
    ref.write_text(ref_text, encoding="utf-8")
    print("Updated REFERENCE.md")

    cmp_path = ROOT / "comparison.md"
    cmp_text = cmp_path.read_text(encoding="utf-8")
    cmp_text = re.sub(
        r"\| Rank \| Project \| ⭐ Stars \| 🍴 Forks \| Score \|\n+",
        "",
        cmp_text,
    )
    start = "| Rank | Project | Live ⭐ | Live 🍴 | Score |\n"
    if start not in cmp_text:
        cmp_text = cmp_text.replace(
            "**Source:**",
            start + "\n**Source:**",
            1,
        )
    cmp_text = replace_between(
        cmp_text,
        "| Rank | Project | Live ⭐ | Live 🍴 | Score |\n",
        "\n*`awesome-openclaw-skills`",
        render_comparison_ranking() + "\n",
    )
    cmp_path.write_text(cmp_text, encoding="utf-8")
    print("Updated comparison.md")


if __name__ == "__main__":
    main()
