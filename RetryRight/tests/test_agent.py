import os

import pytest

from agent import RetryRightAgent, audit_retries


def test_healthy_exponential_backoff_passes():
    events = [
        {"method": "GET", "status": 503},
        {"method": "GET", "status": 429, "delay_ms": 200, "retry_after_ms": 700},
        {"method": "GET", "status": 200, "delay_ms": 800},
    ]
    assert audit_retries(events).valid


def test_post_retry_without_idempotency_key_is_critical():
    report = audit_retries(
        [
            {"method": "POST", "status": 503},
            {"method": "POST", "status": 200, "delay_ms": 200},
        ]
    )
    finding = next(
        item
        for item in report.findings
        if item.code == "unsafe_method_without_idempotency_key"
    )
    assert finding.severity == "critical"


def test_terminal_status_and_attempt_budget_are_reported():
    events = [
        {"method": "GET", "status": 400},
        {"method": "GET", "status": 503, "delay_ms": 200},
        {"method": "GET", "status": 503, "delay_ms": 400},
        {"method": "GET", "status": 503, "delay_ms": 800},
        {"method": "GET", "status": 200, "delay_ms": 1600},
    ]
    codes = {item.code for item in audit_retries(events).findings}
    assert {"retried_terminal_status", "excessive_attempts"} <= codes


def test_retry_after_immediate_retry_and_regression_are_reported():
    events = [
        {"method": "GET", "status": 429, "retry_after_ms": 1000},
        {"method": "GET", "status": 503, "delay_ms": 500},
        {"method": "GET", "status": 200, "delay_ms": 50},
    ]
    codes = {item.code for item in audit_retries(events).findings}
    assert {"retry_after_ignored", "immediate_retry", "backoff_regression"} <= codes


def test_invalid_event_is_rejected():
    with pytest.raises(ValueError, match="status"):
        audit_retries([{"method": "GET", "status": "503"}])


def test_no_key_uses_local_mode(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    report = RetryRightAgent().inspect([{"method": "GET", "status": 200}])
    assert report.mode == "local"
