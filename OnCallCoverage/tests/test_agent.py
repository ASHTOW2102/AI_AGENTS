import pytest
from agent import OnCallCoverageAgent,audit
def codes(r):return {x.code for x in r.findings}
def test_healthy():assert audit([{"team":"platform","uncovered_hours":0,"shifts_per_person":4,"backup":True,"escalation":True}]).healthy
def test_risky():assert set(['coverage_gap','responder_overload','missing_backup','missing_escalation'])<=codes(audit([{"team":"payments","uncovered_hours":12,"shifts_per_person":15,"backup":False,"escalation":False}]))
def test_agent():assert OnCallCoverageAgent().inspect([{"team":"platform","uncovered_hours":0,"shifts_per_person":4,"backup":True,"escalation":True}]).items_checked==1
def test_empty():
    with pytest.raises(ValueError,match="non-empty"):audit([])
