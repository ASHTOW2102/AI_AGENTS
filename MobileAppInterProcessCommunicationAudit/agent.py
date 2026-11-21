"""Flags mobile apps exposing exported components (activities, services, content providers) that accept input from other apps without permission checks."""
from typing import Any


def audit(app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    unprotected_exported = [c for c in app.get("exported_components", []) if c not in app.get("components_with_permission_checks", [])]
    if unprotected_exported:
        findings.append({"severity": "high", "issue": f"Exported components with no permission check: {unprotected_exported}"})
    if app.get("exported_components") and not app.get("ipc_input_validated"):
        findings.append({"severity": "medium", "issue": "Exported components do not validate input received via IPC."})
    return findings
