"""Review webhook replay-window and event freshness protections."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not endpoint.get("timestamp_validated"):
        findings.append({"severity": "high", "issue": "Webhook timestamp is not validated."})
    if not endpoint.get("nonce_or_event_id_deduplicated"):
        findings.append({"severity": "high", "issue": "Webhook nonce or event ID is not deduplicated."})
    if endpoint.get("accepted_timestamp_skew_seconds", 0) > endpoint.get("max_timestamp_skew_seconds", 300):
        findings.append({"severity": "medium", "issue": "Accepted webhook timestamp window is too wide."})
    if endpoint.get("deduplication_ttl_seconds", 0) < endpoint.get("replay_window_seconds", 0):
        findings.append({"severity": "medium", "issue": "Deduplication entries expire before the replay window."})
    return findings
