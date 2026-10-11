import pytest
from agent import ScriptSentryAgent, audit

def codes(report): return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"src":"https://cdn.example.com/app.js","integrity":True,"owner":"web","pages":2,"approved":True}]).healthy

def test_risky_input_is_detected():
    assert {"insecure_origin","missing_integrity","missing_owner","unapproved_script","broad_coverage"} <= codes(audit([{"src":"http://unknown.example/tracker.js","integrity":False,"owner":"","pages":500,"approved":False}]))

def test_agent_delegates():
    assert ScriptSentryAgent().inspect([{"src":"https://cdn.example.com/app.js","integrity":True,"owner":"web","pages":2,"approved":True}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError,match="non-empty"): audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError,match="object"): audit(["bad"])
