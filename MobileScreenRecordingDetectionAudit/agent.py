"""Checks that mobile apps detect and respond to active screen recording during sensitive-data display."""
from typing import Any


def audit(app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if app.get("displays_sensitive_data") and not app.get("screen_recording_detection_enabled"):
        findings.append({"severity": "high", "issue": "Sensitive data screens have no screen-recording detection."})
    if app.get("screen_recording_detection_enabled") and not app.get("blur_on_detection"):
        findings.append({"severity": "medium", "issue": "Recording is detected but content is not blurred in response."})
    return findings
