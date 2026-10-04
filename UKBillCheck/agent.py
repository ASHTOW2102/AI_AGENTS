from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass
from datetime import date
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Any

PENNY = Decimal("0.01")


@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    message: str


@dataclass(frozen=True)
class BillReport:
    valid: bool
    fuel: str
    billing_days: int
    usage_kwh: float
    usage_charge_pounds: float
    standing_charge_pounds: float
    expected_subtotal_pounds: float
    expected_total_pounds: float
    findings: list[Finding]
    recommendations: list[str]
    explanation: str = ""
    mode: str = "local"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _decimal(value: Any, field: str, *, minimum: Decimal | None = None) -> Decimal:
    if isinstance(value, bool):
        raise ValueError(f"{field} must be numeric")
    try:
        number = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise ValueError(f"{field} must be numeric") from None
    if not number.is_finite():
        raise ValueError(f"{field} must be finite")
    if minimum is not None and number < minimum:
        raise ValueError(f"{field} must be at least {minimum}")
    return number


def _money(value: Decimal) -> Decimal:
    return value.quantize(PENNY, rounding=ROUND_HALF_UP)


def check_bill(payload: dict[str, Any], *, tolerance_pounds: float = 0.05) -> BillReport:
    if not isinstance(payload, dict):
        raise ValueError("bill must be a JSON object")

    fuel = str(payload.get("fuel", "")).lower().strip()
    if fuel not in {"electricity", "gas"}:
        raise ValueError("fuel must be electricity or gas")

    try:
        start = date.fromisoformat(str(payload["period_start"]))
        end = date.fromisoformat(str(payload["period_end"]))
    except (KeyError, ValueError):
        raise ValueError("period_start and period_end must be ISO dates") from None
    billing_days = (end - start).days
    if billing_days < 1:
        raise ValueError("period_end must be after period_start")

    opening = _decimal(payload.get("opening_reading"), "opening_reading")
    closing = _decimal(payload.get("closing_reading"), "closing_reading")
    units = closing - opening
    if units < 0:
        raise ValueError("closing_reading cannot be below opening_reading")

    unit_rate = _decimal(payload.get("unit_rate_pence"), "unit_rate_pence", minimum=Decimal("0"))
    standing_rate = _decimal(
        payload.get("standing_charge_pence_per_day"),
        "standing_charge_pence_per_day",
        minimum=Decimal("0"),
    )
    vat_percent = _decimal(payload.get("vat_percent", 5), "vat_percent", minimum=Decimal("0"))
    tolerance = _decimal(tolerance_pounds, "tolerance_pounds", minimum=Decimal("0"))

    if fuel == "electricity":
        usage_kwh = units
    else:
        volume_unit = str(payload.get("volume_unit", "m3")).lower().strip()
        if volume_unit not in {"m3", "ft3"}:
            raise ValueError("volume_unit must be m3 or ft3")
        correction = _decimal(
            payload.get("correction_factor", "1.02264"),
            "correction_factor",
            minimum=Decimal("0"),
        )
        calorific = _decimal(
            payload.get("calorific_value", "39.2"),
            "calorific_value",
            minimum=Decimal("0"),
        )
        metric_volume = units if volume_unit == "m3" else units * Decimal("2.83")
        usage_kwh = metric_volume * correction * calorific / Decimal("3.6")

    usage_charge = _money(usage_kwh * unit_rate / Decimal("100"))
    standing_charge = _money(
        Decimal(billing_days) * standing_rate / Decimal("100")
    )
    subtotal = _money(usage_charge + standing_charge)
    total = _money(subtotal * (Decimal("1") + vat_percent / Decimal("100")))

    findings: list[Finding] = []
    reading_type = str(payload.get("reading_type", "")).lower().strip()
    if reading_type not in {"actual", "estimated", "mixed"}:
        raise ValueError("reading_type must be actual, estimated, or mixed")
    if reading_type != "actual":
        findings.append(
            Finding(
                "estimated_reading",
                "medium",
                "At least one meter reading is estimated rather than actual.",
            )
        )

    if "reported_subtotal_pounds" in payload:
        reported_subtotal = _money(
            _decimal(
                payload["reported_subtotal_pounds"],
                "reported_subtotal_pounds",
                minimum=Decimal("0"),
            )
        )
        difference = abs(reported_subtotal - subtotal)
        if difference > tolerance:
            findings.append(
                Finding(
                    "subtotal_mismatch",
                    "high",
                    f"Reported subtotal differs from the calculation by £{difference:.2f}.",
                )
            )

    if "reported_total_pounds" in payload:
        reported_total = _money(
            _decimal(
                payload["reported_total_pounds"],
                "reported_total_pounds",
                minimum=Decimal("0"),
            )
        )
        difference = abs(reported_total - total)
        if difference > tolerance:
            findings.append(
                Finding(
                    "total_mismatch",
                    "high",
                    f"Reported total differs from the VAT-inclusive calculation by £{difference:.2f}.",
                )
            )

    codes = {item.code for item in findings}
    recommendations: list[str] = []
    if "estimated_reading" in codes:
        recommendations.append("Submit an up-to-date meter reading and request a revised bill.")
    if {"subtotal_mismatch", "total_mismatch"} & codes:
        recommendations.append("Compare the tariff dates and line items, then ask the supplier to explain the difference.")
    if not findings:
        recommendations.append("The supplied readings, tariff, standing charge, and VAT reconcile within tolerance.")

    return BillReport(
        valid=not findings,
        fuel=fuel,
        billing_days=billing_days,
        usage_kwh=float(usage_kwh.quantize(Decimal("0.001"), rounding=ROUND_HALF_UP)),
        usage_charge_pounds=float(usage_charge),
        standing_charge_pounds=float(standing_charge),
        expected_subtotal_pounds=float(subtotal),
        expected_total_pounds=float(total),
        findings=findings,
        recommendations=recommendations,
    )


class UKBillCheckAgent:
    def __init__(self, use_model: bool = True) -> None:
        self.use_model = use_model

    def inspect(
        self,
        payload: dict[str, Any],
        *,
        tolerance_pounds: float = 0.05,
    ) -> BillReport:
        report = check_bill(payload, tolerance_pounds=tolerance_pounds)
        if not self.use_model or not os.getenv("OPENAI_API_KEY"):
            return report

        try:
            from openai import OpenAI

            safe_payload = report.to_dict()
            safe_payload.pop("explanation", None)
            response = OpenAI().responses.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
                input=(
                    "Explain this sanitized UK energy-bill calculation and practical "
                    "next steps. Do not provide legal advice or invent tariff data.\n"
                    + json.dumps(safe_payload)
                ),
            )
            return BillReport(
                report.valid,
                report.fuel,
                report.billing_days,
                report.usage_kwh,
                report.usage_charge_pounds,
                report.standing_charge_pounds,
                report.expected_subtotal_pounds,
                report.expected_total_pounds,
                report.findings,
                report.recommendations,
                response.output_text.strip(),
                "openai",
            )
        except Exception:
            return report
