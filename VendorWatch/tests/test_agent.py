import pytest
from agent import VendorWatchAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"name":"PaymentsCo","owner":"finance","reviewed_days_ago":30,"data_agreement":True,"critical":False,"alternatives":2}]).healthy

def test_risky_input_is_detected():
    assert {"missing_owner","overdue_review","missing_agreement","concentration_risk"} <= codes(audit([{"name":"CoreCloud","owner":"","reviewed_days_ago":500,"data_agreement":False,"critical":True,"alternatives":0}]))

def test_agent_delegates():
    assert VendorWatchAgent().inspect([{"name":"PaymentsCo","owner":"finance","reviewed_days_ago":30,"data_agreement":True,"critical":False,"alternatives":2}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError, match="object"):
        audit(["bad"])
