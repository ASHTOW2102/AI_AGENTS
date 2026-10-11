import pytest
from agent import EmailTemplateAuditAgent,audit
def codes(r):return {x.code for x in r.findings}
def test_healthy():assert audit([{"template":"receipt","unsubscribe":True,"plaintext":True,"subject":"Your receipt","owner":"commerce"}]).healthy
def test_risky():assert set(['missing_unsubscribe','missing_plaintext','missing_subject','missing_owner']) <= codes(audit([{"template":"promo","unsubscribe":False,"plaintext":False,"subject":"","owner":""}]))
def test_agent():assert EmailTemplateAuditAgent().inspect([{"template":"receipt","unsubscribe":True,"plaintext":True,"subject":"Your receipt","owner":"commerce"}]).items_checked==1
def test_empty():
    with pytest.raises(ValueError,match="non-empty"):audit([])
def test_bad_item():
    with pytest.raises(ValueError,match="object"):audit(["bad"])
