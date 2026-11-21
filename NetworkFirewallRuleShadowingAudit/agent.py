"""Flags firewall rulesets where an earlier broad allow/deny rule shadows a later, more specific rule, making the specific rule dead code."""
from typing import Any


def audit(ruleset: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    shadowed = [r for r in ruleset.get("rules", []) if r.get("shadowed_by_earlier_rule")]
    if shadowed:
        findings.append({"severity": "medium", "issue": f"{len(shadowed)} rule(s) are shadowed by an earlier, broader rule and never take effect."})
    if not ruleset.get("rule_order_validated"):
        findings.append({"severity": "low", "issue": "Rule ordering has not been validated for shadowing."})
    return findings
