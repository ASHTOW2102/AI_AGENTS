import pytest
from agent import PIIGuardAgent, redact_json, scan_text

def kinds(report):
    return {item.kind for item in report.findings}

def test_clean_text_passes():
    assert scan_text("Order completed successfully.").safe

def test_detects_email_and_masks_original():
    report = scan_text("Contact ash@example.com today.")
    assert "email" in kinds(report)
    assert "ash@example.com" not in report.redacted

def test_detects_valid_card_only():
    report = scan_text("Card 4111 1111 1111 1111; reference 4111 1111 1111 1112.")
    assert report.total_matches == 1
    assert "payment_card" in kinds(report)

def test_detects_uk_identifiers():
    report = scan_text("NI AB 12 34 56 C, phone 07700 900123, postcode SW1A 1AA")
    assert {"uk_nino", "uk_phone", "uk_postcode"} <= kinds(report)

def test_detects_valid_ipv4_only():
    report = scan_text("source=192.168.1.10 invalid=999.1.1.1")
    assert "ipv4" in kinds(report)
    assert report.findings[0].count >= 1

def test_json_redaction_preserves_structure():
    value = {"user": {"email": "person@example.org"}, "active": True}
    cleaned = redact_json(value)
    assert cleaned["active"] is True
    assert "person@example.org" not in cleaned["user"]["email"]

def test_empty_text_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        scan_text("")

def test_no_key_stays_local(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    assert PIIGuardAgent().inspect("hello").mode == "local"
