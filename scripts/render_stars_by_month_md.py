#!/usr/bin/env python3
"""Regenerate STARS_BY_MONTH.md from scripts/data/stars_monthly_history.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = Path(__file__).parent / "data"


def fmt_num(n):
    if n is None:
        return "—"
    return f"{n:,}".replace(",", " ")


def main():
    hist_path = DATA / "stars_monthly_history.json"
    hist = json.loads(hist_path.read_text(encoding="utf-8"))
    months = sorted(hist["months"].keys())
    if len(months) < 2:
        raise SystemExit("Need at least two months in stars_monthly_history.json")

    # Compare last two months
    m_old, m_new = months[-2], months[-1]
    d_old = hist["months"][m_old]
    d_new = hist["months"][m_new]
    keys = sorted(d_new.keys(), key=lambda k: -d_new[k])

    lines = [
        "# GitHub stars by month",
        "",
        "Monthly **stargazers** comparison for tracked repositories. Fork counts are in "
        "[github_stats.json](scripts/data/github_stats.json).",
        "",
        "**Data files:** [stars_monthly_history.json](scripts/data/stars_monthly_history.json) (machine-readable) · source API: GitHub.",
        "",
        f"**Latest pair in this table:** `{m_old}` → `{m_new}`. Update history with "
        "`python scripts/append_stars_monthly.py` after `fetch_github_stats.py`, then re-run this script.",
        "",
        "*Рус.: сравнение звёзд GitHub по месяцам; исходные числа — в JSON.*",
        "",
        f"## {m_old} → {m_new}",
        "",
        "| Project | " + m_old + " ⭐ | " + m_new + " ⭐ | Δ stars |",
        "|---------|------------:|-----------:|--------:|",
    ]

    for k in keys:
        a, b = d_old.get(k), d_new.get(k)
        if a is None and b is not None:
            delta = "NEW"
        elif a is not None and b is not None:
            delta = b - a
            delta = f"+{delta:,}".replace(",", " ") if delta > 0 else str(delta)
        else:
            delta = "—"
        lines.append(
            f"| `{k}` | {fmt_num(a)} | {fmt_num(b)} | {delta} |"
        )
    lines.append("")

    out = ROOT / "STARS_BY_MONTH.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
