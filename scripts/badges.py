#!/usr/bin/env python3
"""shields.io badge helpers for GitHub stars/forks."""

def stars(repo: str, style: str = "social") -> str:
    return (
        f'[![stars](https://img.shields.io/github/stars/{repo}?style={style})]'
        f"(https://github.com/{repo})"
    )


def forks(repo: str, style: str = "social") -> str:
    return (
        f'[![forks](https://img.shields.io/github/forks/{repo}?style={style})]'
        f"(https://github.com/{repo})"
    )


def stars_forks(repo: str, style: str = "social") -> str:
    return f"{stars(repo, style)} {forks(repo, style)}"
