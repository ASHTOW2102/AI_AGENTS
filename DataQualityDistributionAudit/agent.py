"""Review dataset distribution statistics for drift and completeness."""
from typing import Any


def audit(profile: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if profile.get("missing_rate_percent", 0) > profile.get("max_missing_rate_percent", 0):
        findings.append({"severity": "high", "issue": "Missing-value rate exceeds the configured maximum."})
    if profile.get("distribution_distance", 0) > profile.get("max_distribution_distance", 0):
        findings.append({"severity": "medium", "issue": "Feature distribution drift exceeds the configured threshold."})
    if profile.get("out_of_range_count", 0) > 0:
        findings.append({"severity": "medium", "issue": "Values outside the expected range were observed."})
    if profile.get("sample_size", 0) < profile.get("minimum_sample_size", 0):
        findings.append({"severity": "low", "issue": "Profile sample is smaller than the minimum required size."})
    return findings
