"""Review HTTP Strict Transport Security policy metadata."""
from typing import Any


def audit(site: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if site.get("production") and not site.get("hsts_enabled"):
        findings.append({"severity": "high", "issue": "Production site does not send an HSTS policy."})
    if site.get("hsts_enabled") and site.get("max_age_seconds", 0) < site.get("minimum_max_age_seconds", 15552000):
        findings.append({"severity": "medium", "issue": "HSTS max-age is shorter than the required minimum."})
    if site.get("include_subdomains_required") and not site.get("include_subdomains"):
        findings.append({"severity": "medium", "issue": "HSTS policy omits required subdomain coverage."})
    if site.get("preload_requested") and not site.get("preload_eligibility_confirmed"):
        findings.append({"severity": "low", "issue": "HSTS preload eligibility has not been confirmed."})
    return findings
