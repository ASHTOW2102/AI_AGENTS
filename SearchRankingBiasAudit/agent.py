"""Checks search ranking output for systematic bias toward a narrow set of sources or sellers."""
from typing import Any


def audit(ranking: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if ranking.get("top_result_single_source_share_percent", 0) > ranking.get("max_acceptable_source_share_percent", 50):
        findings.append({"severity": "medium", "issue": "A single source dominates top results beyond the acceptable share."})
    if ranking.get("sponsored_results_unlabeled", 0) > 0:
        findings.append({"severity": "high", "issue": "Sponsored results appear without a disclosure label."})
    if ranking.get("ranking_signal_audit_age_days", 0) > ranking.get("max_signal_audit_age_days", 180):
        findings.append({"severity": "low", "issue": "Ranking signals have not been reviewed for bias recently."})
    return findings
