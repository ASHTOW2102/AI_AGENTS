from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    delivery_id: str
    message: str


@dataclass(frozen=True)
class AuditReport:
    valid: bool
    deliveries: int
    findings: list[Finding]
    recommendations: list[str]
    explanation: str = ""
    mode: str = "local"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _timestamp(value: Any, field: str, delivery_id: str) -> datetime:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{delivery_id}: {field} must be an ISO-8601 timestamp")
    normalized = value.strip()
    if normalized.endswith("Z"):
        normalized = normalized[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as error:
        raise ValueError(
            f"{delivery_id}: {field} must be an ISO-8601 timestamp"
        ) from error
    if parsed.tzinfo is None:
        raise ValueError(f"{delivery_id}: {field} must include a timezone")
    return parsed.astimezone(timezone.utc)


def audit_deliveries(
    deliveries: list[dict[str, Any]],
    *,
    tolerance_seconds: float = 300.0,
) -> AuditReport:
    if not isinstance(deliveries, list) or not deliveries:
        raise ValueError("deliveries must be a non-empty JSON array")
    if tolerance_seconds < 0:
        raise ValueError("tolerance_seconds cannot be negative")

    findings: list[Finding] = []
    seen_delivery_ids: set[str] = set()
    processed_event_ids: set[str] = set()
    last_sequences: dict[str, int] = {}

    for index, delivery in enumerate(deliveries, start=1):
        if not isinstance(delivery, dict):
            raise ValueError(f"delivery {index}: each delivery must be an object")

        delivery_id = str(delivery.get("delivery_id", "")).strip()
        event_id = str(delivery.get("event_id", "")).strip()
        if not delivery_id:
            raise ValueError(f"delivery {index}: delivery_id is required")
        if not event_id:
            raise ValueError(f"{delivery_id}: event_id is required")

        if delivery_id in seen_delivery_ids:
            findings.append(
                Finding(
                    "duplicate_delivery_id",
                    "high",
                    delivery_id,
                    "The provider delivery identifier appears more than once.",
                )
            )
        seen_delivery_ids.add(delivery_id)

        signature_valid = delivery.get("signature_valid")
        if not isinstance(signature_valid, bool):
            raise ValueError(f"{delivery_id}: signature_valid must be a boolean")
        if not signature_valid:
            findings.append(
                Finding(
                    "invalid_signature",
                    "critical",
                    delivery_id,
                    "The delivery was accepted without a valid signature.",
                )
            )

        sent_at = _timestamp(delivery.get("sent_at"), "sent_at", delivery_id)
        received_at = _timestamp(
            delivery.get("received_at"), "received_at", delivery_id
        )
        skew = abs((received_at - sent_at).total_seconds())
        if skew > tolerance_seconds:
            findings.append(
                Finding(
                    "stale_delivery",
                    "high",
                    delivery_id,
                    f"Timestamp skew is {skew:g}s; limit is {tolerance_seconds:g}s.",
                )
            )

        processed = delivery.get("processed")
        if not isinstance(processed, bool):
            raise ValueError(f"{delivery_id}: processed must be a boolean")
        status = delivery.get("http_status")
        if isinstance(status, bool) or not isinstance(status, int) or not 100 <= status <= 599:
            raise ValueError(f"{delivery_id}: http_status must be an integer from 100 to 599")

        if processed and event_id in processed_event_ids:
            findings.append(
                Finding(
                    "event_processed_twice",
                    "critical",
                    delivery_id,
                    f"Event {event_id} was processed more than once.",
                )
            )
        if processed:
            processed_event_ids.add(event_id)

        if not processed and 200 <= status < 300:
            findings.append(
                Finding(
                    "failure_acknowledged",
                    "high",
                    delivery_id,
                    "Processing failed but the provider received a success response.",
                )
            )
        if processed and status >= 300:
            findings.append(
                Finding(
                    "success_rejected",
                    "medium",
                    delivery_id,
                    "Processing succeeded but the response can trigger another delivery.",
                )
            )

        aggregate = delivery.get("aggregate_key")
        sequence = delivery.get("sequence")
        if aggregate is not None or sequence is not None:
            if not isinstance(aggregate, str) or not aggregate.strip():
                raise ValueError(
                    f"{delivery_id}: aggregate_key is required when sequence is set"
                )
            if isinstance(sequence, bool) or not isinstance(sequence, int) or sequence < 0:
                raise ValueError(
                    f"{delivery_id}: sequence must be a non-negative integer"
                )
            key = aggregate.strip()
            if key in last_sequences and sequence <= last_sequences[key]:
                findings.append(
                    Finding(
                        "out_of_order_sequence",
                        "medium",
                        delivery_id,
                        f"Sequence {sequence} follows {last_sequences[key]} for {key}.",
                    )
                )
            last_sequences[key] = max(sequence, last_sequences.get(key, sequence))

    codes = {finding.code for finding in findings}
    recommendations: list[str] = []
    if "invalid_signature" in codes:
        recommendations.append("Verify signatures with the raw request body before processing.")
    if "stale_delivery" in codes:
        recommendations.append("Reject timestamps outside a short replay-tolerance window.")
    if {"duplicate_delivery_id", "event_processed_twice"} & codes:
        recommendations.append("Persist provider IDs and make event handling idempotent.")
    if "failure_acknowledged" in codes:
        recommendations.append("Return a retryable failure status when processing does not finish.")
    if "success_rejected" in codes:
        recommendations.append("Return success after durable processing to prevent needless redelivery.")
    if "out_of_order_sequence" in codes:
        recommendations.append("Buffer, reject, or reconcile events that violate aggregate ordering.")

    return AuditReport(
        valid=not findings,
        deliveries=len(deliveries),
        findings=findings,
        recommendations=recommendations,
    )


class HookSentryAgent:
    def __init__(self, use_model: bool = True) -> None:
        self.use_model = use_model

    def inspect(
        self,
        deliveries: list[dict[str, Any]],
        *,
        tolerance_seconds: float = 300.0,
    ) -> AuditReport:
        report = audit_deliveries(
            deliveries,
            tolerance_seconds=tolerance_seconds,
        )
        if not self.use_model or not os.getenv("OPENAI_API_KEY"):
            return report

        try:
            from openai import OpenAI

            safe_payload = {
                "deliveries": report.deliveries,
                "findings": [asdict(item) for item in report.findings],
                "recommendations": report.recommendations,
            }
            response = OpenAI().responses.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
                input=(
                    "Explain how to repair this sanitized webhook audit. "
                    "Do not invent payload or customer data.\n"
                    + json.dumps(safe_payload)
                ),
            )
            return AuditReport(
                report.valid,
                report.deliveries,
                report.findings,
                report.recommendations,
                response.output_text.strip(),
                "openai",
            )
        except Exception:
            return report
