"""Flags web apps storing authentication tokens in localStorage, where they're readable by any injected script, instead of an HttpOnly cookie."""
from typing import Any


def audit(app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if app.get("token_storage_location") == "localStorage":
        findings.append({"severity": "high", "issue": "Auth token is stored in localStorage, accessible to any script on the page via XSS."})
    if app.get("token_storage_location") == "cookie" and not app.get("cookie_httponly"):
        findings.append({"severity": "medium", "issue": "Token cookie is not marked HttpOnly."})
    return findings
