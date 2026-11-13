"""Flags search ranking systems that train directly on raw click data without correcting for position bias."""
from typing import Any


def audit(search: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if search.get("trains_on_click_data") and not search.get("position_bias_correction_applied"):
        findings.append({"severity": "medium", "issue": "Ranking model trains on click data without position bias correction."})
    if search.get("trains_on_click_data") and not search.get("feedback_loop_monitored"):
        findings.append({"severity": "medium", "issue": "No monitoring exists for runaway feedback loop effects on ranking."})
    return findings
