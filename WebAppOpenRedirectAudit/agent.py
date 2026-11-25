"""Flags redirect endpoints that do not validate the target URL, enabling open-redirect abuse in phishing links."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not endpoint.get("validates_redirect_target"):
        findings.append({"severity": "high", "issue": "Redirect endpoint does not validate the target URL, enabling open-redirect abuse."})
    return findings
