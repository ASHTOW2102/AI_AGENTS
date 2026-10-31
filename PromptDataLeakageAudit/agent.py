"""Review prompt construction metadata for sensitive-data exposure risks."""
from typing import Any


def audit(prompt_flow: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if prompt_flow.get("personal_data_in_prompt") and not prompt_flow.get("purpose_approved"):
        findings.append({"severity": "high", "issue": "Personal data is added to prompts without an approved purpose."})
    if prompt_flow.get("secrets_in_prompt"):
        findings.append({"severity": "critical", "issue": "Credential or secret material can enter the prompt."})
    if prompt_flow.get("external_model") and not prompt_flow.get("provider_retention_reviewed"):
        findings.append({"severity": "medium", "issue": "External model provider retention has not been reviewed."})
    if prompt_flow.get("prompt_logging_enabled") and not prompt_flow.get("sensitive_log_redaction"):
        findings.append({"severity": "high", "issue": "Prompt logs may retain sensitive content without redaction."})
    return findings
