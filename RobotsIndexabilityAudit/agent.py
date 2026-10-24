"""Review site indexing directives for production release safety."""
from typing import Any


def audit(site: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if site.get("production") and site.get("sitewide_noindex"):
        findings.append({"severity": "high", "issue": "Production site is configured with a site-wide noindex directive."})
    if site.get("production") and site.get("robots_disallow_all"):
        findings.append({"severity": "high", "issue": "Production robots policy blocks all crawlers."})
    if site.get("sitemap_url") and not site.get("sitemap_fetchable", True):
        findings.append({"severity": "medium", "issue": "Configured sitemap is not reported as fetchable."})
    if site.get("canonical_mismatch_count", 0) > 0:
        findings.append({"severity": "medium", "issue": "Canonical URLs disagree with the intended host."})
    return findings
