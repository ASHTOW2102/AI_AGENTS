"""Checks hypermedia API responses for valid, reachable action links matching current resource state."""
from typing import Any


def audit(resource: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    for link in resource.get("links", []):
        if link.get("rel") and not link.get("href"):
            findings.append({"severity": "medium", "issue": f"Link relation {link.get('rel')} has no href."})
    if resource.get("state") == "archived" and any(l.get("rel") == "delete" for l in resource.get("links", [])):
        findings.append({"severity": "medium", "issue": "Archived resource still exposes a delete action link."})
    if resource.get("links_signed_required") and not resource.get("links_signed"):
        findings.append({"severity": "high", "issue": "Action links are not signed though signing is required."})
    return findings
