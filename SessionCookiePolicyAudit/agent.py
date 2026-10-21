"""Check browser session-cookie security attributes and lifetime."""
from typing import Any


def audit(cookie: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not cookie.get("secure"):
        findings.append({"severity": "high", "issue": "Session cookie lacks the Secure attribute."})
    if not cookie.get("http_only"):
        findings.append({"severity": "high", "issue": "Session cookie lacks the HttpOnly attribute."})
    if cookie.get("same_site", "").lower() not in {"lax", "strict"}:
        findings.append({"severity": "medium", "issue": "SameSite policy is missing or permissive."})
    if cookie.get("max_age_seconds", 0) > cookie.get("max_allowed_age_seconds", 86400):
        findings.append({"severity": "medium", "issue": "Session cookie lifetime exceeds policy."})
    if cookie.get("domain_scope") == "parent_domain" and not cookie.get("shared_subdomain_session_approved"):
        findings.append({"severity": "medium", "issue": "Parent-domain cookie scope lacks explicit approval."})
    return findings
