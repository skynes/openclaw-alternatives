#!/usr/bin/env python3
"""
Re-fetch repositories that had rate limit errors.
Loads existing github_stats.json, fetches only failed entries, merges back.
"""
import json
import time
from pathlib import Path
import urllib.request

DATA_DIR = Path(__file__).parent / "data"

# Map of key -> (org/repo, key) for failed entries
REPOS = [
    ("jlia0/tinyclaw", "tinyclaw-400"),
    ("puremachinery/carapace", "carapace"),
    ("vincenzodomina/supaclaw", "supaclaw"),
    ("shimaenaga1123/rustclaw", "rustclaw"),
    ("openagen/zeroclaw", "zeroclaw-openagen"),
]

def main():
    with open(DATA_DIR / "github_stats.json", "r", encoding="utf-8") as f:
        results = json.load(f)

    for repo, key in REPOS:
        if key not in results or "error" not in results.get(key, {}):
            continue
        err = results[key].get("error", "")
        if "rate limit exceeded" not in err:
            continue

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

        time.sleep(1.5)  # Avoid rate limit

    with open(DATA_DIR / "github_stats.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("\nUpdated scripts/data/github_stats.json")

if __name__ == "__main__":
    main()
