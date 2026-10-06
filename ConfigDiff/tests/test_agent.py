import pytest
from agent import ConfigDiffAgent, audit

def codes(report):
    return {item.code for item in report.findings}

def test_matching_config_passes():
    assert audit({"baseline":{"debug":False},"current":{"debug":False}}).healthy

def test_risky_drift_detected():
    report=audit({"baseline":{"debug":False,"tls_required":True,"region":"uk"},"current":{"debug":True,"region":"eu","new_option":1}})
    assert {"debug_enabled","changed_security_control","changed_value","new_key","missing_key"} - codes(report) == {"missing_key"}

def test_missing_key_detected():
    assert "missing_key" in codes(audit({"baseline":{"region":"uk"},"current":{}}))

def test_agent_delegates():
    assert ConfigDiffAgent().inspect({"baseline":{},"current":{}}).healthy

def test_invalid_payload_rejected():
    with pytest.raises(ValueError, match="baseline"):
        audit({})
