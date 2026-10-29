"""Review personal-data flow inventories for destination and control coverage."""
from typing import Any


def audit(flow: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if flow.get("contains_personal_data") and not flow.get("purpose_documented"):
        findings.append({"severity": "high", "issue": "Personal-data flow has no documented purpose."})
    if flow.get("contains_personal_data") and not flow.get("destinations"):
        findings.append({"severity": "high", "issue": "Personal-data flow has no documented destinations."})
    missing = sorted(set(flow.get("required_controls", [])) - set(flow.get("implemented_controls", [])))
    if missing:
        findings.append({"severity": "medium", "issue": "Flow is missing controls: " + ", ".join(missing)})
    if not flow.get("last_review_date"):
        findings.append({"severity": "low", "issue": "Data-flow mapping has no review date."})
    return findings
