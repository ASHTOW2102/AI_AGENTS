import pytest
from agent import EnvDoctorAgent,audit_env,parse_env

def test_parser_supports_comments_quotes_and_export():
 values=parse_env("# note\nexport HOST=localhost\nPORT='8000'\n")
 assert values=={"HOST":"localhost","PORT":"8000"}

def test_finds_missing_unexpected_and_placeholder():
 report=audit_env("HOST=\nTOKEN=\n","HOST=changeme\nEXTRA=yes\n")
 codes={item.code for item in report.findings}
 assert {"missing","unexpected","placeholder"}<=codes
 assert not report.valid

def test_never_places_secret_value_in_findings():
 secret="sk_live_ABCDEF1234567890xyz"
 report=audit_env("API_KEY=\n",f"API_KEY={secret}\n")
 assert any(item.code=="possible_secret" for item in report.findings)
 assert secret not in str(report.to_dict())

def test_duplicate_key_is_rejected():
 with pytest.raises(ValueError,match="duplicate"):
  parse_env("A=1\nA=2\n")

def test_agent_works_without_key(monkeypatch):
 monkeypatch.delenv("OPENAI_API_KEY",raising=False)
 assert EnvDoctorAgent().inspect("HOST=\n","HOST=localhost\n").mode=="local"
