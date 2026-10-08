import pytest
from agent import RetentionCheckAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"dataset":"orders","retention_days":365,"legal_basis":"contract","deletion_method":"hard-delete","owner":"ops"}]).healthy

def test_risky_input_is_detected():
    assert {"indefinite_retention","missing_legal_basis","missing_deletion_method","missing_owner"} <= codes(audit([{"dataset":"logs","retention_days":None,"legal_basis":"","deletion_method":"","owner":""}]))

def test_agent_delegates_to_audit():
    assert RetentionCheckAgent().inspect([{"dataset":"orders","retention_days":365,"legal_basis":"contract","deletion_method":"hard-delete","owner":"ops"}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError, match="object"):
        audit(["bad"])
