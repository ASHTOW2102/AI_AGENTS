import pytest
from agent import HealthProbeAgent, audit

def codes(report): return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"service":"api","interval_seconds":30,"timeout_seconds":3,"checks_dependencies":True,"check_type":"readiness"}]).healthy

def test_risky_input_is_detected():
    assert {"long_interval","slow_timeout","dependencies_ignored","shallow_check"} <= codes(audit([{"service":"legacy","interval_seconds":600,"timeout_seconds":120,"checks_dependencies":False,"check_type":"tcp"}]))

def test_agent_delegates():
    assert HealthProbeAgent().inspect([{"service":"api","interval_seconds":30,"timeout_seconds":3,"checks_dependencies":True,"check_type":"readiness"}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError,match="non-empty"): audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError,match="object"): audit(["bad"])
