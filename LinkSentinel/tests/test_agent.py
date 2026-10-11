import pytest
from agent import LinkSentinelAgent,audit
def codes(r):return {x.code for x in r.findings}
def test_healthy():assert audit([{"url":"https://example.com","status":200,"redirects":0,"owner":"web"}]).healthy
def test_risky():assert set(['broken_link','insecure_link','redirect_chain','missing_owner']) <= codes(audit([{"url":"http://old.example","status":500,"redirects":6,"owner":""}]))
def test_agent():assert LinkSentinelAgent().inspect([{"url":"https://example.com","status":200,"redirects":0,"owner":"web"}]).items_checked==1
def test_empty():
    with pytest.raises(ValueError,match="non-empty"):audit([])
def test_bad_item():
    with pytest.raises(ValueError,match="object"):audit(["bad"])
