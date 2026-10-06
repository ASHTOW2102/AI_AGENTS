import pytest
from agent import LogSentryAgent, audit

def codes(report):
    return {item.code for item in report.findings}

def test_healthy_input_passes():
    assert audit([{"level": "info", "request_id": "r1", "duration_ms": 20, "message": "ok"}]).healthy

def test_risky_input_is_detected():
    assert {"error_event", "missing_request_id", "slow_event", "secret_field"} <= codes(audit([{"level": "error", "request_id": "", "duration_ms": 1500, "token": "hidden"}]))

def test_agent_delegates_to_audit():
    assert LogSentryAgent().inspect([{"level": "info", "request_id": "r1", "duration_ms": 20, "message": "ok"}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError, match="object"):
        audit(["bad"])
