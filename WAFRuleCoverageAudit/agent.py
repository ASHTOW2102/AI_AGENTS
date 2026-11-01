"""Checks web-application-firewall rule coverage, mode, and exception review freshness."""
from typing import Any


def audit(waf: dict[str, Any]):
    findings = []
    if waf.get("production") and waf.get("mode") != "block":
        findings.append({"severity": "high", "issue": "Production WAF is not in blocking mode."})
    missing = sorted(set(waf.get("required_rule_sets", [])) - set(waf.get("enabled_rule_sets", [])))
    if missing:
        findings.append({"severity": "high", "issue": "Required WAF rule sets are disabled: " + ", ".join(missing)})
    if waf.get("exception_count", 0) > 0 and waf.get("exception_review_age_days", 0) > waf.get("max_review_age_days", 90):
        findings.append({"severity": "medium", "issue": "WAF exceptions have not been reviewed recently."})
    return findings
