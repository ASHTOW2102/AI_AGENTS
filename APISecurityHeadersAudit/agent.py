"""Review HTTP security-header deployment and value coverage metadata."""
from typing import Any


def audit(site: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    for header in site.get("required_headers", []):
        if header not in site.get("present_headers", []):
            findings.append({"severity": "medium", "issue": f"Required security header {header} is missing."})
    if site.get("production") and site.get("server_version_disclosed"):
        findings.append({"severity": "low", "issue": "Production response exposes detailed server version."})
    if site.get("referrer_policy") in (None, "unsafe-url"):
        findings.append({"severity": "medium", "issue": "Referrer policy is missing or overly permissive."})
    return findings
