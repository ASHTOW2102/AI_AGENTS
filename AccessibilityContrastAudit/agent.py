"""Check reported foreground/background color pairs against contrast targets."""
from typing import Any


def audit(report: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    for pair in report.get("color_pairs", []):
        ratio = pair.get("contrast_ratio", 0)
        target = pair.get("required_ratio", 4.5)
        if ratio < target:
            findings.append({"severity": "medium", "issue": f"{pair.get('element', 'Element')} contrast {ratio}:1 is below {target}:1."})
    if report.get("unlabeled_controls", 0) > 0:
        findings.append({"severity": "high", "issue": "Interactive controls are missing accessible labels."})
    return findings
