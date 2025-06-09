import json
import requests
from typing import List, Dict


def search_papers(query: str, rows: int = 5) -> List[Dict[str, str]]:
    """Search papers using the Crossref API as a proxy for IEEE and ACM results."""
    url = "https://api.crossref.org/works"
    params = {"query": query, "rows": rows}
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        resp = requests.get(url, params=params, headers=headers, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return [
            {
                "title": item.get("title", ["No title"])[0],
                "doi": item.get("DOI", ""),
                "abstract": item.get("abstract", ""),
                "keywords": ", ".join(item.get("subject", [])),
            }
            for item in data.get("message", {}).get("items", [])
        ]
    except Exception as e:
        return [{"error": str(e)}]

