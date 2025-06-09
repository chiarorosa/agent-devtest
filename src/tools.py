from typing import Any, List, Dict
import requests
from crewai.tools import BaseTool


class CrossrefSearchTool(BaseTool):
    """Tool to search academic papers using the Crossref API."""

    name: str = "crossref_search"
    description: str = (
        "Busca artigos nas bases IEEE e ACM utilizando a API Crossref."
    )

    def _run(self, query: str, rows: int = 5) -> List[Dict[str, str]]:
        url = "https://api.crossref.org/works"
        params = {"query": query, "rows": rows}
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, params=params, headers=headers, timeout=10)
        resp.raise_for_status()
        data = resp.json().get("message", {}).get("items", [])
        return [
            {
                "title": item.get("title", ["No title"])[0],
                "doi": item.get("DOI", ""),
                "abstract": item.get("abstract", ""),
                "keywords": ", ".join(item.get("subject", [])),
            }
            for item in data
        ]
