"""Flags API consumers still pinned to deprecated client library versions well past the recommended upgrade window."""
from typing import Any


def audit(consumer: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if consumer.get("client_version_deprecated") and consumer.get("days_since_deprecation", 0) > consumer.get("max_grace_period_days", 180):
        findings.append({"severity": "medium", "issue": "Consumer remains on a deprecated client version past the grace period."})
    if consumer.get("client_version_deprecated") and not consumer.get("upgrade_notified"):
        findings.append({"severity": "low", "issue": "Consumer has not been notified about the deprecated client version."})
    return findings
