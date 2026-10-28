"""Check dataset lineage metadata for upstream and downstream completeness."""
from typing import Any


def audit(dataset: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not dataset.get("upstream_sources"):
        findings.append({"severity": "medium", "issue": "Dataset has no recorded upstream sources."})
    if dataset.get("critical") and not dataset.get("owner"):
        findings.append({"severity": "high", "issue": "Critical dataset has no accountable owner."})
    missing = sorted(set(dataset.get("required_downstream_consumers", [])) - set(dataset.get("documented_downstream_consumers", [])))
    if missing:
        findings.append({"severity": "medium", "issue": "Undocumented downstream consumers: " + ", ".join(missing)})
    if not dataset.get("lineage_last_verified"):
        findings.append({"severity": "low", "issue": "Lineage has no verification timestamp."})
    return findings
