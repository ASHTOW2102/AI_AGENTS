import pytest

from agent import UKBillCheckAgent, check_bill


def electricity(**updates):
    bill = {
        "fuel": "electricity",
        "period_start": "2026-09-01",
        "period_end": "2026-10-01",
        "opening_reading": 1000,
        "closing_reading": 1100,
        "reading_type": "actual",
        "unit_rate_pence": 25,
        "standing_charge_pence_per_day": 50,
        "vat_percent": 5,
        "reported_subtotal_pounds": 40,
        "reported_total_pounds": 42,
    }
    bill.update(updates)
    return bill


def test_electricity_bill_reconciles():
    report = check_bill(electricity())
    assert report.valid
    assert report.billing_days == 30
    assert report.usage_kwh == 100
    assert report.expected_total_pounds == 42


def test_subtotal_and_total_mismatches_are_reported():
    report = check_bill(
        electricity(reported_subtotal_pounds=50, reported_total_pounds=55)
    )
    codes = {item.code for item in report.findings}
    assert {"subtotal_mismatch", "total_mismatch"} <= codes


def test_estimated_reading_is_flagged():
    assert "estimated_reading" in {
        item.code
        for item in check_bill(electricity(reading_type="estimated")).findings
    }


def test_metric_gas_conversion():
    report = check_bill(
        {
            "fuel": "gas",
            "period_start": "2026-09-01",
            "period_end": "2026-10-01",
            "opening_reading": 500,
            "closing_reading": 510,
            "reading_type": "actual",
            "volume_unit": "m3",
            "correction_factor": 1.02264,
            "calorific_value": 39.2,
            "unit_rate_pence": 6,
            "standing_charge_pence_per_day": 30,
        }
    )
    assert 111 < report.usage_kwh < 112


def test_imperial_gas_uses_volume_conversion():
    metric = check_bill(
        {
            **electricity(),
            "fuel": "gas",
            "opening_reading": 10,
            "closing_reading": 11,
            "volume_unit": "m3",
        }
    )
    imperial = check_bill(
        {
            **electricity(),
            "fuel": "gas",
            "opening_reading": 10,
            "closing_reading": 11,
            "volume_unit": "ft3",
        }
    )
    assert imperial.usage_kwh > metric.usage_kwh * 2.8


def test_reading_rollback_is_rejected():
    with pytest.raises(ValueError, match="closing_reading"):
        check_bill(electricity(closing_reading=900))


def test_no_key_uses_local_mode(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    assert UKBillCheckAgent().inspect(electricity()).mode == "local"
