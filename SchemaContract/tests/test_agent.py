import pytest
from agent import SchemaContractAgent,audit
def codes(r):return {x.code for x in r.findings}
def test_healthy():assert audit([{"name":"order-event","version":"2.1","backward_compatible":True,"owner":"commerce","examples":True}]).healthy
def test_risky():assert set(['missing_version','breaking_change','missing_owner','missing_examples']) <= codes(audit([{"name":"legacy-event","version":"","backward_compatible":False,"owner":"","examples":False}]))
def test_agent():assert SchemaContractAgent().inspect([{"name":"order-event","version":"2.1","backward_compatible":True,"owner":"commerce","examples":True}]).items_checked==1
def test_empty():
    with pytest.raises(ValueError,match="non-empty"):audit([])
def test_bad_item():
    with pytest.raises(ValueError,match="object"):audit(["bad"])
