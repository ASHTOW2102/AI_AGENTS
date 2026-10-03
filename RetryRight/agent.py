from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass
from typing import Any

SAFE_METHODS = {"GET", "HEAD", "OPTIONS", "TRACE", "PUT", "DELETE"}
RETRYABLE_STATUSES = {408, 425, 429, 500, 502, 503, 504}


@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    attempt: int
    message: str


@dataclass(frozen=True)
class AuditReport:
    valid: bool
    attempts: int
    findings: list[Finding]
    recommendations: list[str]
    explanation: str = ""
    mode: str = "local"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _number(value: Any, field: str, index: int) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"event {index}: {field} must be a number")
    return float(value)


def audit_retries(
    events: list[dict[str, Any]],
    *,
    max_attempts: int = 4,
    min_delay_ms: float = 100.0,
) -> AuditReport:
    if not isinstance(events, list) or not events:
        raise ValueError("events must be a non-empty JSON array")
    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")

    findings: list[Finding] = []
    delays: list[float] = []
    method = ""
    idempotency_key = False

    for index, event in enumerate(events, start=1):
        if not isinstance(event, dict):
            raise ValueError(f"event {index}: each event must be an object")
        current_method = str(event.get("method", "")).upper().strip()
        if not current_method:
            raise ValueError(f"event {index}: method is required")
        if index == 1:
            method = current_method
            idempotency_key = bool(event.get("idempotency_key"))
        elif current_method != method:
            raise ValueError("all events must describe the same HTTP method")

        status = event.get("status")
        if isinstance(status, bool) or not isinstance(status, int) or not 100 <= status <= 599:
            raise ValueError(f"event {index}: status must be an integer from 100 to 599")

        if index < len(events) and status not in RETRYABLE_STATUSES:
            findings.append(
                Finding(
                    "retried_terminal_status",
                    "high",
                    index,
                    f"Request was retried after terminal HTTP {status}.",
                )
            )

        if index > 1:
            delay = _number(event.get("delay_ms"), "delay_ms", index)
            if delay < 0:
                raise ValueError(f"event {index}: delay_ms cannot be negative")
            delays.append(delay)
            if delay < min_delay_ms:
                findings.append(
                    Finding(
                        "immediate_retry",
                        "medium",
                        index,
                        f"Retry delay {delay:g} ms is below the {min_delay_ms:g} ms floor.",
                    )
                )

            previous = events[index - 2]
            retry_after = previous.get("retry_after_ms")
            if retry_after is not None:
                required = _number(retry_after, "retry_after_ms", index - 1)
                if required < 0:
                    raise ValueError(f"event {index - 1}: retry_after_ms cannot be negative")
                if delay < required:
                    findings.append(
                        Finding(
                            "retry_after_ignored",
                            "high",
                            index,
                            f"Waited {delay:g} ms after a server requested {required:g} ms.",
                        )
                    )

            if len(delays) > 1 and delay < delays[-2]:
                findings.append(
                    Finding(
                        "backoff_regression",
                        "medium",
                        index,
                        f"Retry delay fell from {delays[-2]:g} ms to {delay:g} ms.",
                    )
                )

    if len(events) > 1 and method not in SAFE_METHODS and not idempotency_key:
        findings.append(
            Finding(
                "unsafe_method_without_idempotency_key",
                "critical",
                2,
                f"{method} was retried without an idempotency key.",
            )
        )

    if len(events) > max_attempts:
        findings.append(
            Finding(
                "excessive_attempts",
                "high",
                max_attempts + 1,
                f"Observed {len(events)} attempts; configured maximum is {max_attempts}.",
            )
        )

    codes = {item.code for item in findings}
    recommendations: list[str] = []
    if "unsafe_method_without_idempotency_key" in codes:
        recommendations.append("Add an idempotency key or do not retry this operation automatically.")
    if "retry_after_ignored" in codes:
        recommendations.append("Honor Retry-After before scheduling the next attempt.")
    if {"immediate_retry", "backoff_regression"} & codes:
        recommendations.append("Use capped exponential backoff with jitter.")
    if "retried_terminal_status" in codes:
        recommendations.append("Retry only transient failures explicitly allowed by policy.")
    if "excessive_attempts" in codes:
        recommendations.append("Enforce a strict retry-attempt budget.")

    return AuditReport(
        valid=not findings,
        attempts=len(events),
        findings=findings,
        recommendations=recommendations,
    )


class RetryRightAgent:
    def __init__(self, use_model: bool = True) -> None:
        self.use_model = use_model

    def inspect(
        self,
        events: list[dict[str, Any]],
        *,
        max_attempts: int = 4,
        min_delay_ms: float = 100.0,
    ) -> AuditReport:
        report = audit_retries(
            events,
            max_attempts=max_attempts,
            min_delay_ms=min_delay_ms,
        )
        if not self.use_model or not os.getenv("OPENAI_API_KEY"):
            return report

        try:
            from openai import OpenAI

            safe_payload = {
                "attempts": report.attempts,
                "findings": [asdict(item) for item in report.findings],
                "recommendations": report.recommendations,
            }
            response = OpenAI().responses.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
                input=(
                    "Explain how to repair this sanitized HTTP retry-policy audit. "
                    "Do not invent request data.\n" + json.dumps(safe_payload)
                ),
            )
            return AuditReport(
                report.valid,
                report.attempts,
                report.findings,
                report.recommendations,
                response.output_text.strip(),
                "openai",
            )
        except Exception:
            return report
