#!/usr/bin/env python3
"""
Append current github_stats.json star counts to stars_monthly_history.json for a given month.

Usage:
  python scripts/append_stars_monthly.py              # uses today's YYYY-MM
  python scripts/append_stars_monthly.py 2026-05        # explicit month

Run after: python scripts/fetch_github_stats.py
"""
import argparse
import json
from datetime import date
from pathlib import Path

DATA = Path(__file__).parent / "data"


def main():
    parser = argparse.ArgumentParser(description="Record monthly GitHub stars snapshot")
    parser.add_argument(
        "month",
        nargs="?",
        help="YYYY-MM (default: current month)",
    )
    args = parser.parse_args()
    if args.month:
        month = args.month
        if len(month) != 7 or month[4] != "-":
            raise SystemExit("Month must be YYYY-MM")
    else:
        month = date.today().strftime("%Y-%m")

    stats_path = DATA / "github_stats.json"
    hist_path = DATA / "stars_monthly_history.json"
    if not stats_path.exists():
        raise SystemExit(f"Missing {stats_path}")

    raw = json.loads(stats_path.read_text(encoding="utf-8"))
    stars_only = {k: raw[k]["stars"] for k in raw if "stars" in raw.get(k, {})}

    if hist_path.exists():
        hist = json.loads(hist_path.read_text(encoding="utf-8"))
    else:
        hist = {"meta": {}, "months": {}}

    hist.setdefault("meta", {})
    hist.setdefault("months", {})
    hist["months"][month] = stars_only
    hist["meta"]["last_month_added"] = month
    hist["meta"]["description"] = (
        "GitHub stargazers_count snapshots by calendar month (YYYY-MM)."
    )

    hist_path.write_text(json.dumps(hist, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Recorded {len(stars_only)} repos for {month} -> {hist_path}")


if __name__ == "__main__":
    main()
