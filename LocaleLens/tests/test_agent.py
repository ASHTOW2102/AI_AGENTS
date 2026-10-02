from agent import LocaleLensAgent,audit_locale
BASE={"nav":{"home":"Home","hello":"Hello {name}"},"count":"%d items"}
def test_matching_catalog_passes():
 assert audit_locale(BASE,{"nav":{"home":"Accueil","hello":"Bonjour {name}"},"count":"%d articles"}).valid
def test_finds_missing_and_extra_keys():
 r=audit_locale(BASE,{"nav":{"home":"Accueil"},"extra":"x"});codes={x.code for x in r.findings}
 assert {"missing_key","extra_key"}<=codes and not r.valid
def test_detects_placeholder_drift():
 r=audit_locale(BASE,{"nav":{"home":"Accueil","hello":"Bonjour {user}"},"count":"articles"})
 assert sum(x.code=="placeholder_mismatch" for x in r.findings)==2
def test_detects_empty_and_type_mismatch():
 r=audit_locale(BASE,{"nav":{"home":"","hello":["Bonjour"]},"count":"%d articles"})
 assert {"empty_translation","type_mismatch"}<={x.code for x in r.findings}
def test_agent_works_without_key(monkeypatch):
 monkeypatch.delenv("OPENAI_API_KEY",raising=False)
 assert LocaleLensAgent().inspect(BASE,BASE).mode=="local"
