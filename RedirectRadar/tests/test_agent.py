import pytest
from agent import RedirectRadarAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"name":"home","urls":["https://example.com","https://www.example.com"]}]).healthy

def test_risky_input_is_detected():
    assert {"redirect_loop","https_downgrade","too_many_hops"} <= codes(audit([{"name":"login","urls":["https://example.com/login","http://example.com/auth","https://example.com/login","https://example.com/final","https://example.com/end"]}]))

def test_agent_delegates_to_audit():
    assert RedirectRadarAgent().inspect([{"name":"home","urls":["https://example.com","https://www.example.com"]}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError, match="object"):
        audit(["bad"])
