"""Review notification preference enforcement and consent records."""
from typing import Any


def audit(message: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if message.get("marketing") and not message.get("opt_in_recorded"):
        findings.append({"severity": "high", "issue": "Marketing message has no recorded opt-in."})
    if message.get("unsubscribe_requested") and message.get("sent_after_unsubscribe"):
        findings.append({"severity": "critical", "issue": "Message was sent after an unsubscribe request."})
    if message.get("transactional") and message.get("contains_marketing_content"):
        findings.append({"severity": "medium", "issue": "Transactional message also contains marketing content."})
    if message.get("preference_updated") and not message.get("propagation_completed"):
        findings.append({"severity": "medium", "issue": "Updated preferences have not propagated to senders."})
    return findings
