#!/usr/bin/env python3
"""
Compare projects from README via Tavily API.
"""
import json
import os
import time
from pathlib import Path
import urllib.request

DATA_DIR = Path(__file__).parent / "data"

TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY", "")
TAVILY_SEARCH_URL = "https://api.tavily.com/search"

PROJECTS = [
    {"name": "picoclaw", "org": "sipeed", "url": "https://github.com/sipeed/picoclaw"},
    {"name": "nanobot", "org": "HKUDS", "url": "https://github.com/HKUDS/nanobot"},
    {"name": "openclaw", "org": "openclaw", "url": "https://github.com/openclaw/openclaw"},
    {"name": "nanoclaw", "org": "qwibitai", "url": "https://github.com/qwibitai/nanoclaw"},
    {"name": "zeroclaw", "org": "zeroclaw-labs", "url": "https://github.com/zeroclaw-labs/zeroclaw"},
    {"name": "microclaw", "org": "microclaw", "url": "https://github.com/microclaw/microclaw"},
    {"name": "nanoClaw", "org": "ysz", "url": "https://github.com/ysz/nanoClaw"},
    {"name": "beamclaw", "org": "peterdmv", "url": "https://github.com/peterdmv/beamclaw"},
    {"name": "AstrBot", "org": "AstrBotDevs", "url": "https://github.com/AstrBotDevs/AstrBot"},
    {"name": "mcp-use", "org": "mcp-use", "url": "https://github.com/mcp-use/mcp-use"},
    {"name": "ironclaw", "org": "nearai", "url": "https://github.com/nearai/ironclaw"},
    {"name": "awesome-openclaw-skills", "org": "VoltAgent", "url": "https://github.com/VoltAgent/awesome-openclaw-skills"},
]


def search_tavily(query: str, max_results: int = 5) -> dict:
    """Search via Tavily API."""
    payload = {
        "query": query,
        "search_depth": "basic",
        "max_results": max_results,
        "include_answer": True,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        TAVILY_SEARCH_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {TAVILY_API_KEY}"
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        return {"error": str(e), "results": [], "answer": ""}


def main():
    if not TAVILY_API_KEY:
        print("Set TAVILY_API_KEY environment variable")
        return
    results = {}
    
    for project in PROJECTS:
        query = f"{project['name']} {project['org']} github MCP agent openclaw"
        print(f"Search: {project['name']}...")
        
        data = search_tavily(query)
        
        if "error" in data:
            results[project["name"]] = {"error": data["error"], "answer": "", "snippets": []}
        else:
            answer = data.get("answer", "")
            snippets = []
            for r in data.get("results", [])[:3]:
                snippets.append({
                    "title": r.get("title", ""),
                    "url": r.get("url", ""),
                    "content": (r.get("content", "") or "")[:300]
                })
            results[project["name"]] = {
                "answer": answer,
                "snippets": snippets,
                "url": project["url"]
            }
        
        time.sleep(1)  # Rate limiting
    
    # Save raw results
    DATA_DIR.mkdir(exist_ok=True)
    with open(DATA_DIR / "tavily_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print("\nResults saved to scripts/data/tavily_results.json")
    return results


if __name__ == "__main__":
    main()
