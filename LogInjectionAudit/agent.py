"""Flags logging configurations that write raw, unsanitized request bodies to logs, letting attacker-controlled input forge or inject fake log entries."""
from typing import Any


def audit(logging_config: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if logging_config.get("logs_raw_request_body") and not logging_config.get("sanitizes_user_input_before_logging"):
        findings.append({"severity": "medium", "issue": "Raw request bodies are logged without sanitization, enabling log injection/forgery."})
    return findings
