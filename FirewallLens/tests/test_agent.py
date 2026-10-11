import pytest
from agent import FirewallLensAgent, audit

def codes(report): return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"name":"web","source":"0.0.0.0/0","port":443,"protocol":"tcp","owner":"platform","temporary":False}]).healthy

def test_risky_input_is_detected():
    assert {"open_admin_port","missing_owner","temporary_no_expiry"} <= codes(audit([{"name":"ssh-temp","source":"0.0.0.0/0","port":22,"protocol":"tcp","owner":"","temporary":True,"expires_in_days":None}]))

def test_agent_delegates():
    assert FirewallLensAgent().inspect([{"name":"web","source":"0.0.0.0/0","port":443,"protocol":"tcp","owner":"platform","temporary":False}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError,match="non-empty"): audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError,match="object"): audit(["bad"])
