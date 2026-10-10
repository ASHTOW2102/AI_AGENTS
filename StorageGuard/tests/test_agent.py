import pytest
from agent import StorageGuardAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"name":"backups","public":False,"encryption":True,"versioning":True,"retention_days":30}]).healthy

def test_risky_input_is_detected():
    assert {"public_bucket","missing_encryption","versioning_off","no_retention"} <= codes(audit([{"name":"uploads","public":True,"encryption":False,"versioning":False,"retention_days":None}]))

def test_agent_delegates():
    assert StorageGuardAgent().inspect([{"name":"backups","public":False,"encryption":True,"versioning":True,"retention_days":30}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError,match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError,match="object"):
        audit(["bad"])
