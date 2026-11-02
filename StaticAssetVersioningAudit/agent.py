"""Checks static asset cache-busting and long-lived cache headers for safe versioning."""
from typing import Any


def audit(asset: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if asset.get("cache_max_age_seconds", 0) > 86400 and not asset.get("content_hash_in_filename"):
        findings.append({"severity": "medium", "issue": "Long-lived cache header is used without a content hash in the filename."})
    if asset.get("content_hash_in_filename") and asset.get("immutable_directive_present") is False:
        findings.append({"severity": "low", "issue": "Hashed asset does not set an immutable cache directive."})
    if asset.get("referenced_by_html") and not asset.get("html_cache_busted"):
        findings.append({"severity": "medium", "issue": "Referencing HTML is not cache-busted on deploy."})
    return findings
