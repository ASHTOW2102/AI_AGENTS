from __future__ import annotations
import json, os
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any

@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    subject: str
    message: str

@dataclass(frozen=True)
class BackupReport:
    valid: bool
    successful_backups: int
    latest_success_age_hours: float | None
    latest_restore_age_days: float | None
    findings: list[Finding]
    recommendations: list[str]
    explanation: str = ""
    mode: str = "local"
    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

def _time(value: Any, field: str) -> datetime:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be an ISO-8601 timestamp")
    text = value.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        raise ValueError(f"{field} must be an ISO-8601 timestamp") from None
    if parsed.tzinfo is None:
        raise ValueError(f"{field} must include a timezone")
    return parsed.astimezone(timezone.utc)

def _positive(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or value <= 0:
        raise ValueError(f"{field} must be a positive number")
    return float(value)

def audit_backups(payload: dict[str, Any]) -> BackupReport:
    if not isinstance(payload, dict):
        raise ValueError("backup audit input must be a JSON object")
    now = _time(payload.get("evaluated_at"), "evaluated_at")
    policy, backups = payload.get("policy"), payload.get("backups")
    restores = payload.get("restore_tests", [])
    if not isinstance(policy, dict):
        raise ValueError("policy must be an object")
    if not isinstance(backups, list) or not backups:
        raise ValueError("backups must be a non-empty list")
    if not isinstance(restores, list):
        raise ValueError("restore_tests must be a list")
    rpo = _positive(policy.get("rpo_hours"), "policy.rpo_hours")
    restore_limit = _positive(policy.get("restore_test_max_age_days"), "policy.restore_test_max_age_days")
    requirements = {
        "encrypted": bool(policy.get("require_encryption", True)),
        "offsite": bool(policy.get("require_offsite", True)),
        "immutable": bool(policy.get("require_immutable", False)),
    }
    findings: list[Finding] = []
    parsed: list[tuple[datetime, dict[str, Any]]] = []
    for index, backup in enumerate(backups, 1):
        if not isinstance(backup, dict):
            raise ValueError(f"backup {index} must be an object")
        completed = _time(backup.get("completed_at"), f"backup {index}.completed_at")
        status = str(backup.get("status", "")).lower().strip()
        if status not in {"success", "failed"}:
            raise ValueError(f"backup {index}.status must be success or failed")
        if completed > now:
            raise ValueError(f"backup {index}.completed_at cannot be in the future")
        parsed.append((completed, backup))
        if status == "success":
            size = backup.get("bytes")
            if isinstance(size, bool) or not isinstance(size, int) or size < 0:
                raise ValueError(f"backup {index}.bytes must be a non-negative integer")
            if size == 0:
                findings.append(Finding("empty_success", "critical", f"backup {index}", "Successful backup contains zero bytes."))
            for flag, required in requirements.items():
                if required and backup.get(flag) is not True:
                    findings.append(Finding(f"missing_{flag}", "high", f"backup {index}", f"Successful backup lacks required {flag} protection."))
    parsed.sort(key=lambda item: item[0], reverse=True)
    successes = [(stamp, item) for stamp, item in parsed if str(item.get("status")).lower() == "success"]
    success_age = None
    if not successes:
        findings.append(Finding("no_successful_backup", "critical", "backup set", "No successful backup exists."))
    else:
        success_age = (now - successes[0][0]).total_seconds() / 3600
        if success_age > rpo:
            findings.append(Finding("rpo_breached", "critical", "latest success", f"Latest success is {success_age:.1f}h old; RPO is {rpo:g}h."))
    streak = 0
    for _, item in parsed:
        if str(item.get("status")).lower() != "failed":
            break
        streak += 1
    if streak >= 2:
        findings.append(Finding("repeated_failures", "high", "latest runs", f"The latest {streak} backup runs failed."))
    restore_successes: list[datetime] = []
    for index, restore in enumerate(restores, 1):
        if not isinstance(restore, dict):
            raise ValueError(f"restore test {index} must be an object")
        stamp = _time(restore.get("completed_at"), f"restore test {index}.completed_at")
        status = str(restore.get("status", "")).lower().strip()
        if stamp > now:
            raise ValueError(f"restore test {index}.completed_at cannot be in the future")
        if status not in {"success", "failed"}:
            raise ValueError(f"restore test {index}.status must be success or failed")
        if status == "success":
            restore_successes.append(stamp)
    restore_age = None
    if not restore_successes:
        findings.append(Finding("no_successful_restore_test", "critical", "restore tests", "No successful restore test is recorded."))
    else:
        restore_age = (now - max(restore_successes)).total_seconds() / 86400
        if restore_age > restore_limit:
            findings.append(Finding("stale_restore_test", "high", "restore tests", f"Latest successful restore test is {restore_age:.1f} days old."))
    codes = {item.code for item in findings}
    recommendations: list[str] = []
    if {"no_successful_backup", "rpo_breached", "repeated_failures"} & codes:
        recommendations.append("Restore healthy scheduled backups and verify the next completed artifact.")
    if {"missing_encrypted", "missing_offsite", "missing_immutable"} & codes:
        recommendations.append("Meet every configured storage-protection requirement.")
    if {"no_successful_restore_test", "stale_restore_test"} & codes:
        recommendations.append("Run and document a representative restore test.")
    if "empty_success" in codes:
        recommendations.append("Treat zero-byte successes as failures and inspect backup selection.")
    if not findings:
        recommendations.append("Freshness, protections, and restore evidence meet the supplied policy.")
    return BackupReport(not findings, len(successes), round(success_age, 2) if success_age is not None else None, round(restore_age, 2) if restore_age is not None else None, findings, recommendations)

class BackupBeaconAgent:
    def __init__(self, use_model: bool = True) -> None:
        self.use_model = use_model
    def inspect(self, payload: dict[str, Any]) -> BackupReport:
        report = audit_backups(payload)
        if not self.use_model or not os.getenv("OPENAI_API_KEY"):
            return report
        try:
            from openai import OpenAI
            safe = report.to_dict()
            safe.pop("explanation", None)
            response = OpenAI().responses.create(model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"), input="Explain this sanitized backup-policy audit and prioritize recovery steps. Do not claim that any backup is restorable.\n" + json.dumps(safe))
            return BackupReport(report.valid, report.successful_backups, report.latest_success_age_hours, report.latest_restore_age_days, report.findings, report.recommendations, response.output_text.strip(), "openai")
        except Exception:
            return report
