import pytest
from agent import OwnershipMapAgent,audit
def codes(r):return {x.code for x in r.findings}
def test_healthy():assert audit([{"asset":"payments-api","owner":"payments","backup_owner":"platform","escalation":True,"docs":True}]).healthy
def test_risky():assert set(['missing_owner','missing_backup','missing_escalation','missing_docs']) <= codes(audit([{"asset":"legacy-job","owner":"","backup_owner":"","escalation":False,"docs":False}]))
def test_agent():assert OwnershipMapAgent().inspect([{"asset":"payments-api","owner":"payments","backup_owner":"platform","escalation":True,"docs":True}]).items_checked==1
def test_empty():
    with pytest.raises(ValueError,match="non-empty"):audit([])
def test_bad_item():
    with pytest.raises(ValueError,match="object"):audit(["bad"])
