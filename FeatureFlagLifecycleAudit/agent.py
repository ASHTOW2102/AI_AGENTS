"""Find stale and risky feature-flag lifecycle configurations."""
from datetime import date
from typing import Any


def audit(flag: dict[str, Any], today: date | None = None) -> list[dict[str, str]]:
    today = today or date.today()
    findings = []
    if flag.get("temporary") and not flag.get("expiry_date"):
        findings.append({"severity": "medium", "issue": "Temporary flag has no expiry date."})
    if flag.get("expiry_date"):
        expiry = date.fromisoformat(flag["expiry_date"])
        if expiry < today and flag.get("enabled"):
            findings.append({"severity": "medium", "issue": "Expired feature flag remains enabled."})
    if flag.get("owner") is None or not str(flag.get("owner", "")).strip():
        findings.append({"severity": "low", "issue": "Feature flag has no accountable owner."})
    if flag.get("production_enabled") and not flag.get("rollback_plan"):
        findings.append({"severity": "high", "issue": "Production flag lacks a documented rollback plan."})
    return findings
