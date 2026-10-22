"""Review search relevance evaluation results for drift and coverage gaps."""
from typing import Any


def audit(eval_run: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if eval_run.get("ndcg_score", 1.0) < eval_run.get("minimum_ndcg", 0.8):
        findings.append({"severity": "high", "issue": "NDCG score is below the evaluation floor."})
    if eval_run.get("zero_result_rate_percent", 0) > eval_run.get("max_zero_result_rate_percent", 5):
        findings.append({"severity": "medium", "issue": "Zero-result rate exceeds the configured maximum."})
    if eval_run.get("days_since_baseline", 0) > eval_run.get("max_baseline_age_days", 90):
        findings.append({"severity": "low", "issue": "Search baseline evaluation is stale."})
    if eval_run.get("query_segments_evaluated", 0) < eval_run.get("required_query_segments", 0):
        findings.append({"severity": "medium", "issue": "Evaluation omits required query segments."})
    return findings
