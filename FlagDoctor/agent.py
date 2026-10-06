from __future__ import annotations
import json, os
from dataclasses import asdict, dataclass
from datetime import date
from typing import Any

FLAG_TYPES = {"release", "experiment", "ops", "permission"}

@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    flag: str
    message: str

@dataclass(frozen=True)
class FlagReport:
    valid: bool
    flags: int
    findings: list[Finding]
    cleanup_order: list[str]
    recommendations: list[str]
    explanation: str = ""
    mode: str = "local"
    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

def _date(value: Any, field: str) -> date:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be an ISO date")
    try:
        return date.fromisoformat(value.strip())
    except ValueError:
        raise ValueError(f"{field} must be an ISO date") from None

def audit_flags(payload: dict[str, Any], *, stale_days: int = 30) -> FlagReport:
    if not isinstance(payload, dict):
        raise ValueError("input must be a JSON object")
    evaluated = _date(payload.get("evaluated_at"), "evaluated_at")
    flags = payload.get("flags")
    if not isinstance(flags, list) or not flags:
        raise ValueError("flags must be a non-empty list")
    if stale_days < 1:
        raise ValueError("stale_days must be at least 1")

    findings: list[Finding] = []
    seen: set[str] = set()
    ages: dict[str, int] = {}
    for index, flag in enumerate(flags, 1):
        if not isinstance(flag, dict):
            raise ValueError(f"flag {index} must be an object")
        key = str(flag.get("key", "")).strip()
        owner = str(flag.get("owner", "")).strip()
        kind = str(flag.get("type", "")).lower().strip()
        state = str(flag.get("state", "")).lower().strip()
        if not key:
            raise ValueError(f"flag {index}.key is required")
        if key in seen:
            findings.append(Finding("duplicate_key", "critical", key, "Feature-flag key appears more than once."))
        seen.add(key)
        if kind not in FLAG_TYPES:
            raise ValueError(f"{key}.type must be release, experiment, ops, or permission")
        if state not in {"enabled", "disabled"}:
            raise ValueError(f"{key}.state must be enabled or disabled")
        created = _date(flag.get("created_at"), f"{key}.created_at")
        if created > evaluated:
            raise ValueError(f"{key}.created_at cannot be in the future")
        ages[key] = (evaluated - created).days
        if not owner:
            findings.append(Finding("missing_owner", "high", key, "Flag has no accountable owner."))

        rollout = flag.get("rollout_percentage")
        if isinstance(rollout, bool) or not isinstance(rollout, (int, float)) or not 0 <= rollout <= 100:
            raise ValueError(f"{key}.rollout_percentage must be between 0 and 100")
        if state == "disabled" and rollout != 0:
            findings.append(Finding("disabled_with_rollout", "high", key, "Disabled flag still has a non-zero rollout."))

        expires_raw = flag.get("expires_at")
        expires = _date(expires_raw, f"{key}.expires_at") if expires_raw else None
        if expires and expires < created:
            raise ValueError(f"{key}.expires_at cannot precede created_at")
        if state == "enabled" and expires and expires < evaluated:
            findings.append(Finding("expired_enabled_flag", "critical", key, f"Enabled flag expired on {expires.isoformat()}."))
        if kind in {"release", "experiment"} and not expires:
            findings.append(Finding("temporary_flag_without_expiry", "high", key, f"{kind.title()} flag has no expiry date."))
        if state == "disabled" and ages[key] >= stale_days:
            findings.append(Finding("stale_disabled_flag", "medium", key, f"Disabled flag is {ages[key]} days old."))

        environments = flag.get("environments", [])
        if not isinstance(environments, list) or not all(isinstance(item, str) and item.strip() for item in environments):
            raise ValueError(f"{key}.environments must be a list of names")
        if state == "enabled" and not environments:
            findings.append(Finding("enabled_without_environment", "medium", key, "Enabled flag has no target environment."))

    severity_rank = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    cleanup = []
    for item in sorted(findings, key=lambda x: (severity_rank[x.severity], -ages.get(x.flag, 0), x.flag)):
        if item.flag not in cleanup:
            cleanup.append(item.flag)

    codes = {item.code for item in findings}
    recommendations: list[str] = []
    if {"expired_enabled_flag", "disabled_with_rollout"} & codes:
        recommendations.append("Correct runtime state before removing flag code.")
    if {"stale_disabled_flag", "temporary_flag_without_expiry"} & codes:
        recommendations.append("Schedule flag removal and add expiry dates for temporary flags.")
    if "missing_owner" in codes:
        recommendations.append("Assign one accountable owner to every flag.")
    if "duplicate_key" in codes:
        recommendations.append("Resolve duplicate keys before deployment.")
    if not findings:
        recommendations.append("All flags meet the supplied lifecycle checks.")
    return FlagReport(not findings, len(flags), findings, cleanup, recommendations)

class FlagDoctorAgent:
    def __init__(self, use_model: bool = True) -> None:
        self.use_model = use_model
    def inspect(self, payload: dict[str, Any], *, stale_days: int = 30) -> FlagReport:
        report = audit_flags(payload, stale_days=stale_days)
        if not self.use_model or not os.getenv("OPENAI_API_KEY"):
            return report
        try:
            from openai import OpenAI
            safe = report.to_dict(); safe.pop("explanation", None)
            response = OpenAI().responses.create(model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"), input="Turn this sanitized feature-flag audit into a safe cleanup plan. Do not invent rollout behavior.\n" + json.dumps(safe))
            return FlagReport(report.valid, report.flags, report.findings, report.cleanup_order, report.recommendations, response.output_text.strip(), "openai")
        except Exception:
            return report
