"""Review network ingress rules for source allowlisting and admin exposure."""
from typing import Any


def audit(ruleset: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if ruleset.get("world_open_rules", 0) > 0:
        findings.append({"severity": "high", "issue": "Ingress includes rules open to all source addresses."})
    if ruleset.get("admin_ports_publicly_reachable"):
        findings.append({"severity": "critical", "issue": "Administrative ports are publicly reachable."})
    if ruleset.get("temporary_rules", 0) > 0 and not ruleset.get("temporary_rule_expiry_enforced"):
        findings.append({"severity": "medium", "issue": "Temporary ingress rules have no enforced expiry."})
    if not ruleset.get("ingress_change_auditing"):
        findings.append({"severity": "low", "issue": "Ingress rule changes are not audited."})
    return findings
