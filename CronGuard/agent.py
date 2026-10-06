from __future__ import annotations
import json, os
from dataclasses import asdict, dataclass
from typing import Any
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    job: str
    message: str

@dataclass(frozen=True)
class ScheduleReport:
    valid: bool
    jobs: int
    enabled_jobs: int
    findings: list[Finding]
    recommendations: list[str]
    explanation: str = ""
    mode: str = "local"
    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

def _positive(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or value <= 0:
        raise ValueError(f"{field} must be a positive number")
    return float(value)

def audit_schedule(jobs: list[dict[str, Any]]) -> ScheduleReport:
    if not isinstance(jobs, list) or not jobs:
        raise ValueError("jobs must be a non-empty JSON array")
    findings: list[Finding] = []
    seen: set[str] = set()
    enabled_slots: dict[tuple[float, float, str], list[str]] = {}
    enabled_count = 0

    for index, job in enumerate(jobs, 1):
        if not isinstance(job, dict):
            raise ValueError(f"job {index} must be an object")
        name = str(job.get("name", "")).strip()
        if not name:
            raise ValueError(f"job {index}.name is required")
        if name in seen:
            findings.append(Finding("duplicate_name", "critical", name, "Scheduled job name appears more than once."))
        seen.add(name)
        enabled = job.get("enabled", True)
        singleton = job.get("singleton", False)
        if not isinstance(enabled, bool) or not isinstance(singleton, bool):
            raise ValueError(f"{name}.enabled and singleton must be booleans")
        interval = _positive(job.get("interval_minutes"), f"{name}.interval_minutes")
        duration = _positive(job.get("expected_duration_minutes"), f"{name}.expected_duration_minutes")
        timeout = _positive(job.get("timeout_minutes"), f"{name}.timeout_minutes")
        offset = job.get("offset_minutes", 0)
        retries = job.get("max_retries", 0)
        retry_delay = job.get("retry_delay_minutes", 1)
        if isinstance(offset, bool) or not isinstance(offset, (int, float)) or not 0 <= offset < interval:
            raise ValueError(f"{name}.offset_minutes must be within the interval")
        if isinstance(retries, bool) or not isinstance(retries, int) or retries < 0:
            raise ValueError(f"{name}.max_retries must be a non-negative integer")
        retry_delay = _positive(retry_delay, f"{name}.retry_delay_minutes")
        timezone_name = str(job.get("timezone", "")).strip()
        if not timezone_name:
            raise ValueError(f"{name}.timezone is required")
        try:
            ZoneInfo(timezone_name)
        except ZoneInfoNotFoundError:
            raise ValueError(f"{name}.timezone is not a valid IANA timezone") from None

        if not enabled:
            continue
        enabled_count += 1
        if duration >= interval and not singleton:
            findings.append(Finding("runtime_overlap", "high", name, f"Expected runtime {duration:g}m meets or exceeds the {interval:g}m interval without singleton protection."))
        if timeout >= interval and not singleton:
            findings.append(Finding("timeout_overlap", "medium", name, f"Timeout {timeout:g}m can extend into the next run."))
        retry_window = duration + retries * retry_delay
        if retries and retry_window >= interval:
            findings.append(Finding("retry_spillover", "high", name, f"Runtime plus retry delays can span {retry_window:g}m across a {interval:g}m interval."))
        slot = (interval, float(offset), timezone_name)
        enabled_slots.setdefault(slot, []).append(name)

    for (interval, offset, timezone_name), names in enabled_slots.items():
        if len(names) > 1:
            subject = ", ".join(sorted(names))
            findings.append(Finding("same_slot_collision", "medium", subject, f"Jobs share the same {interval:g}m interval and {offset:g}m offset in {timezone_name}."))

    codes = {item.code for item in findings}
    recommendations: list[str] = []
    if {"runtime_overlap", "timeout_overlap"} & codes:
        recommendations.append("Shorten runtime/timeout, widen the interval, or enforce singleton execution.")
    if "retry_spillover" in codes:
        recommendations.append("Cap retries within the schedule window or move retries to a queue.")
    if "same_slot_collision" in codes:
        recommendations.append("Stagger offsets to reduce shared-resource spikes.")
    if "duplicate_name" in codes:
        recommendations.append("Assign a unique stable name to every scheduled job.")
    if not findings:
        recommendations.append("The supplied interval schedules pass the configured collision checks.")
    return ScheduleReport(not findings, len(jobs), enabled_count, findings, recommendations)

class CronGuardAgent:
    def __init__(self, use_model: bool = True) -> None:
        self.use_model = use_model
    def inspect(self, jobs: list[dict[str, Any]]) -> ScheduleReport:
        report = audit_schedule(jobs)
        if not self.use_model or not os.getenv("OPENAI_API_KEY"):
            return report
        try:
            from openai import OpenAI
            safe = report.to_dict(); safe.pop("explanation", None)
            response = OpenAI().responses.create(model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"), input="Explain this sanitized schedule audit and propose a safer rollout. Do not invent infrastructure.\n" + json.dumps(safe))
            return ScheduleReport(report.valid, report.jobs, report.enabled_jobs, report.findings, report.recommendations, response.output_text.strip(), "openai")
        except Exception:
            return report
