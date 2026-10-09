import pytest
from agent import SessionSentryAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"application":"portal","idle_minutes":15,"absolute_minutes":480,"rotate_on_login":True,"secure_cookie":True,"max_sessions":3}]).healthy

def test_risky_input_is_detected():
    assert {"long_idle","long_absolute","no_rotation","insecure_cookie","unlimited_sessions"} <= codes(audit([{"application":"legacy","idle_minutes":1440,"absolute_minutes":10080,"rotate_on_login":False,"secure_cookie":False,"max_sessions":None}]))

def test_agent_delegates():
    assert SessionSentryAgent().inspect([{"application":"portal","idle_minutes":15,"absolute_minutes":480,"rotate_on_login":True,"secure_cookie":True,"max_sessions":3}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError, match="object"):
        audit(["bad"])
