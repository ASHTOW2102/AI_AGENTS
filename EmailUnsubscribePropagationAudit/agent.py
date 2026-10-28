"""Review unsubscribe propagation latency and sender-system coverage."""
from typing import Any


def audit(request: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    missing = sorted(set(request.get("sender_systems", [])) - set(request.get("systems_updated", [])))
    if missing:
        findings.append({"severity": "high", "issue": "Unsubscribe not propagated to: " + ", ".join(missing)})
    if request.get("propagation_minutes", 0) > request.get("max_propagation_minutes", 60):
        findings.append({"severity": "medium", "issue": "Unsubscribe propagation exceeds the target."})
    if not request.get("suppression_list_shared") and len(request.get("sender_systems", [])) > 1:
        findings.append({"severity": "medium", "issue": "Sender systems do not share a central suppression list."})
    if not request.get("confirmation_recorded"):
        findings.append({"severity": "low", "issue": "Unsubscribe completion has no confirmation record."})
    return findings
