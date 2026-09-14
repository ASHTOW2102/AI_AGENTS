import json
from typing import Any
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from agents import function_tool

GOVUK_SEARCH = "https://www.gov.uk/api/search.json"
TIMEOUT = 15

def _clean_text(text: str, limit: int = 12000) -> str:
    text = " ".join(text.split())
    return text[:limit]

@function_tool
def search_govuk(query: str, count: int = 5) -> str:
    """Search the official GOV.UK Search API for current UK government guidance.

    Use this for housing, renting, tenancy, deposits, eviction, repairs,
    homelessness, council housing and other government-process questions.
    Returns official GOV.UK result titles, descriptions and URLs.
    """
    count = max(1, min(int(count), 10))
    response = requests.get(
        GOVUK_SEARCH,
        params={
            "q": query,
            "count": count,
            "fields": ["title", "description", "link", "public_timestamp"],
        },
        headers={"User-Agent": "UK-Housing-Agent/1.0"},
        timeout=TIMEOUT,
    )
    response.raise_for_status()
    data: dict[str, Any] = response.json()

    results = []
    for item in data.get("results", []):
        link = item.get("link", "")
        if link.startswith("/"):
            link = urljoin("https://www.gov.uk", link)
        results.append(
            {
                "title": item.get("title", ""),
                "description": _clean_text(item.get("description", ""), 600),
                "url": link,
                "published_or_updated": item.get("public_timestamp", ""),
            }
        )

    return json.dumps(
        {"query": query, "results": results},
        ensure_ascii=False,
        indent=2,
    )

@function_tool
def fetch_govuk_page(url: str) -> str:
    """Fetch and extract readable text from a GOV.UK page.

    Only use this for URLs returned by search_govuk or clearly belonging to
    www.gov.uk. This helps verify details before answering.
    """
    if not url.startswith("https://www.gov.uk/"):
        return "ERROR: fetch_govuk_page only accepts https://www.gov.uk/ URLs."

    response = requests.get(
        url,
        headers={"User-Agent": "UK-Housing-Agent/1.0"},
        timeout=TIMEOUT,
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "noscript", "svg"]):
        tag.decompose()

    main = soup.find("main") or soup.body
    if not main:
        return "No readable page content found."

    title = soup.title.get_text(" ", strip=True) if soup.title else url
    text = _clean_text(main.get_text(" ", strip=True))

    return json.dumps(
        {
            "title": title,
            "url": url,
            "content": text,
        },
        ensure_ascii=False,
    )
