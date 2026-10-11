import pytest
from agent import ContainerCheckAgent, audit

def codes(report): return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"name":"api","run_as_root":False,"privileged":False,"read_only_root":True,"cpu_limit":True,"memory_limit":True}]).healthy

def test_risky_input_is_detected():
    assert {"runs_as_root","privileged","writable_root","missing_cpu_limit","missing_memory_limit"} <= codes(audit([{"name":"legacy","run_as_root":True,"privileged":True,"read_only_root":False,"cpu_limit":False,"memory_limit":False}]))

def test_agent_delegates():
    assert ContainerCheckAgent().inspect([{"name":"api","run_as_root":False,"privileged":False,"read_only_root":True,"cpu_limit":True,"memory_limit":True}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError,match="non-empty"): audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError,match="object"): audit(["bad"])
