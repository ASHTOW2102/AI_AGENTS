"""Check machine-learning feature freshness against serving requirements."""
from typing import Any


def audit(feature: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if feature.get("observed_age_minutes", 0) > feature.get("max_age_minutes", 0):
        findings.append({"severity": "high", "issue": "Feature data is older than the serving freshness limit."})
    if feature.get("training_freshness_minutes", 0) > feature.get("serving_freshness_minutes", 0):
        findings.append({"severity": "medium", "issue": "Training and serving freshness expectations are misaligned."})
    if feature.get("null_rate_percent", 0) > feature.get("max_null_rate_percent", 0):
        findings.append({"severity": "high", "issue": "Feature null rate exceeds its quality threshold."})
    if not feature.get("owner"):
        findings.append({"severity": "low", "issue": "Feature has no accountable owner."})
    return findings
