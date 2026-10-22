"""Check mobile backup exclusions for sensitive application data."""
from typing import Any


def audit(app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    included = set(app.get("backup_included_paths", []))
    sensitive = set(app.get("sensitive_paths", []))
    exposed = sorted(included & sensitive)
    if exposed:
        findings.append({"severity": "high", "issue": "Sensitive paths are included in device backups: " + ", ".join(exposed)})
    if app.get("backup_enabled") and not app.get("backup_encryption_confirmed"):
        findings.append({"severity": "medium", "issue": "Backup encryption is not confirmed for application data."})
    if app.get("auth_tokens_backup_enabled"):
        findings.append({"severity": "critical", "issue": "Authentication tokens are included in device backups."})
    return findings
