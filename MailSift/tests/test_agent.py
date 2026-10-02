from agent import MailSiftAgent,local_triage,parse_eml,redact_sensitive

def test_parses_plain_email():
 raw=b"From: boss@example.com\nSubject: Weekly update\n\nPlease review the report."
 subject,sender,body=parse_eml(raw)
 assert subject=="Weekly update" and "boss@example.com" in sender and "Please review" in body

def test_redacts_sensitive_data():
 text,count=redact_sensitive("Email ada@example.com, phone +44 7700 900123, password=hunter2")
 assert count==3 and "ada@example.com" not in text and "7700" not in text and "hunter2" not in text

def test_flags_phishing_and_action():
 report=local_triage("Urgent: verify your account","Bank <alerts@example.com>","Action required immediately. Please confirm your password at http://10.0.0.1.")
 assert report.urgency in {"high","critical"}
 assert {"credential_request","suspicious_link"}<=set(report.phishing_flags)
 assert report.actions

def test_benign_is_low_risk():
 report=local_triage("Lunch notes","friend@example.com","It was good to catch up.")
 assert report.urgency=="low" and report.phishing_flags==[]

def test_agent_without_key(monkeypatch):
 monkeypatch.delenv("OPENAI_API_KEY",raising=False)
 assert MailSiftAgent().inspect(b"From: a@example.com\nSubject: Hello\n\nNormal.").mode=="local"
