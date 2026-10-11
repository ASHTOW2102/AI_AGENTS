import pytest
from agent import StatusPageAuditAgent,audit
def codes(r):return {x.code for x in r.findings}
def test_healthy():assert audit([{"component":"API","public":True,"test_age_days":10,"subscriptions":True,"owner":"platform"}]).healthy
def test_risky():assert set(['hidden_component','stale_test','no_subscriptions','missing_owner']) <= codes(audit([{"component":"Database","public":False,"test_age_days":500,"subscriptions":False,"owner":""}]))
def test_agent():assert StatusPageAuditAgent().inspect([{"component":"API","public":True,"test_age_days":10,"subscriptions":True,"owner":"platform"}]).items_checked==1
def test_empty():
    with pytest.raises(ValueError,match="non-empty"):audit([])
def test_bad_item():
    with pytest.raises(ValueError,match="object"):audit(["bad"])
