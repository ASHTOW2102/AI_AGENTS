import pytest
from agent import ResourceTaggerAgent,audit
def codes(r):return {x.code for x in r.findings}
def test_healthy():assert audit([{"resource":"vm-101","owner":"platform","environment":"production","cost_centre":"CC42","lifecycle":"managed"}]).healthy
def test_risky():assert set(['missing_owner','missing_environment','missing_cost_centre','missing_lifecycle'])<=codes(audit([{"resource":"disk-old","owner":"","environment":"","cost_centre":"","lifecycle":""}]))
def test_agent():assert ResourceTaggerAgent().inspect([{"resource":"vm-101","owner":"platform","environment":"production","cost_centre":"CC42","lifecycle":"managed"}]).items_checked==1
def test_empty():
    with pytest.raises(ValueError,match="non-empty"):audit([])
