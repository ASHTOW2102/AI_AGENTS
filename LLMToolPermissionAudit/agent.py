"""Review AI tool declarations for least-privilege scope and approval."""
from typing import Any


def audit(tool: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    extra = sorted(set(tool.get("granted_actions", [])) - set(tool.get("required_actions", [])))
    if extra:
        findings.append({"severity": "high", "issue": "Tool has unnecessary actions: " + ", ".join(extra)})
    if tool.get("side_effecting") and not tool.get("human_approval_required"):
        findings.append({"severity": "critical", "issue": "Side-effecting tool can run without human approval."})
    if tool.get("external_destination") and not tool.get("destination_allowlisted"):
        findings.append({"severity": "high", "issue": "Tool can send data to an unapproved destination."})
    if not tool.get("audit_log_enabled"):
        findings.append({"severity": "medium", "issue": "Tool invocations are not audited."})
    return findings
