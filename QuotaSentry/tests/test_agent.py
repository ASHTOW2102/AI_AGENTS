import pytest
from agent import QuotaSentryAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"endpoint":"/login","requests":10,"window_seconds":60,"burst":3,"per_client":True}]).healthy

def test_risky_input_is_detected():
    assert {"unlimited_requests","not_per_client","excessive_burst"} <= codes(audit([{"endpoint":"/search","requests":None,"window_seconds":60,"burst":500,"per_client":False}]))

def test_agent_delegates_to_audit():
    assert QuotaSentryAgent().inspect([{"endpoint":"/login","requests":10,"window_seconds":60,"burst":3,"per_client":True}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError, match="object"):
        audit(["bad"])
