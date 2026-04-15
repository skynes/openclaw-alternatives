#!/usr/bin/env python3
"""Fetch GitHub stars and forks for projects"""
import json
from pathlib import Path
import urllib.request

DATA_DIR = Path(__file__).parent / "data"

REPOS = [
    ("sipeed/picoclaw", "picoclaw"),
    ("HKUDS/nanobot", "nanobot"),
    ("openclaw/openclaw", "openclaw"),
    ("NousResearch/hermes-agent", "hermes-agent"),
    ("qwibitai/nanoclaw", "nanoclaw"),
    ("zeroclaw-labs/zeroclaw", "zeroclaw"),
    ("microclaw/microclaw", "microclaw"),
    ("ysz/nanoClaw", "nanoClaw"),
    ("peterdmv/beamclaw", "beamclaw"),
    ("AstrBotDevs/AstrBot", "AstrBot"),
    ("mcp-use/mcp-use", "mcp-use"),
    ("nearai/ironclaw", "ironclaw"),
    ("VoltAgent/awesome-openclaw-skills", "awesome-openclaw-skills"),
    # Additional alternatives
    ("nullclaw/nullclaw", "nullclaw"),
    ("tnm/zclaw", "zclaw"),
    ("memovai/mimiclaw", "mimiclaw"),
    ("princezuda/safeclaw", "safeclaw"),
    ("qhkm/zeptoclaw", "zeptoclaw"),
    ("warengonzaga/tinyclaw", "tinyclaw"),
    ("brendanhogan/hermitclaw", "hermitclaw"),
    ("jmlago/subzeroclaw", "subzeroclaw"),
    ("jlia0/tinyclaw", "tinyclaw-400"),
    ("puremachinery/carapace", "carapace"),
    ("vincenzodomina/supaclaw", "supaclaw"),
    ("shimaenaga1123/rustclaw", "rustclaw"),
    ("openagen/zeroclaw", "zeroclaw-openagen"),
    ("nextlevelbuilder/goclaw", "goclaw"),
]

def main():
    results = {}
    for repo, key in REPOS:
        try:
            req = urllib.request.Request(
                f"https://api.github.com/repos/{repo}",
                headers={"Accept": "application/vnd.github.v3+json", "User-Agent": "NeroClaw"}
            )
            with urllib.request.urlopen(req, timeout=10) as r:
                d = json.loads(r.read().decode())
                stars = d["stargazers_count"]
                forks = d["forks_count"]
                lang = d.get("language") or "—"
                created = d.get("created_at", "")[:10] if d.get("created_at") else "—"
                results[key] = {
                    "stars": stars, "forks": forks, "popularity": stars * 2 + forks,
                    "language": lang, "created_at": created
                }
                print(f"{key}: {stars} stars, {forks} forks, {lang}, {created}")
        except Exception as e:
            results[key] = {"stars": 0, "forks": 0, "popularity": 0, "error": str(e)}
            print(f"{key}: ERROR - {e}")

    DATA_DIR.mkdir(exist_ok=True)
    with open(DATA_DIR / "github_stats.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    before_path = DATA_DIR / "github_stats_before_refresh.json"
    if before_path.exists():
        old = json.loads(before_path.read_text(encoding="utf-8"))
        lines = [
            "GitHub stats refresh (compare snapshot vs current run)",
            "Before: github_stats_before_refresh.json",
            "After:  github_stats.json",
            "",
            "Per repo (stars / forks):",
            "",
        ]
        for k in sorted(set(old) | set(results), key=str.lower):
            if k not in results:
                lines.append(f"- {k}: REMOVED")
                continue
            if k not in old:
                n = results[k]
                if "stars" not in n:
                    continue
                lines.append(f"- {k}: NEW -> {n['stars']} stars, {n['forks']} forks")
                continue
            o, n = old[k], results[k]
            if "stars" not in n:
                continue
            ds = n["stars"] - o["stars"]
            df = n["forks"] - o["forks"]
            lines.append(
                f"- {k}: {o['stars']}->{n['stars']} stars ({ds:+d}); "
                f"{o['forks']}->{n['forks']} forks ({df:+d})"
            )
        (DATA_DIR / "STATS_REFRESH_LOG.txt").write_text(
            "\n".join(lines) + "\n", encoding="utf-8"
        )
        print("Wrote scripts/data/STATS_REFRESH_LOG.txt (diff vs github_stats_before_refresh.json)")

    return results

if __name__ == "__main__":
    main()
