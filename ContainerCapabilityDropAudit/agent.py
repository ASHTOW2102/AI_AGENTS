"""Checks containers drop unnecessary Linux capabilities instead of running with the full default set."""
from typing import Any


def audit(container: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not container.get("capabilities_dropped"):
        findings.append({"severity": "high", "issue": "Container does not drop any Linux capabilities."})
    if "NET_ADMIN" in container.get("retained_capabilities", []) and not container.get("net_admin_justified"):
        findings.append({"severity": "high", "issue": "NET_ADMIN capability is retained without justification."})
    return findings
