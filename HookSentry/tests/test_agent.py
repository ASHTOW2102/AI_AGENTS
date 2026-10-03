import pytest

from agent import HookSentryAgent, audit_deliveries


def delivery(**updates):
    item = {
        "delivery_id": "del-1",
        "event_id": "evt-1",
        "sent_at": "2026-10-03T09:00:00Z",
        "received_at": "2026-10-03T09:00:02Z",
        "signature_valid": True,
        "processed": True,
        "http_status": 204,
    }
    item.update(updates)
    return item


def test_healthy_delivery_passes():
    assert audit_deliveries([delivery()]).valid


def test_invalid_signature_and_stale_timestamp_are_reported():
    report = audit_deliveries(
        [
            delivery(
                signature_valid=False,
                received_at="2026-10-03T09:10:00Z",
            )
        ]
    )
    codes = {item.code for item in report.findings}
    assert {"invalid_signature", "stale_delivery"} <= codes


def test_replayed_event_is_detected_even_with_new_delivery_id():
    report = audit_deliveries(
        [
            delivery(),
            delivery(
                delivery_id="del-2",
                sent_at="2026-10-03T09:01:00Z",
                received_at="2026-10-03T09:01:01Z",
            ),
        ]
    )
    assert "event_processed_twice" in {item.code for item in report.findings}


def test_acknowledgement_mistakes_are_reported():
    report = audit_deliveries(
        [
            delivery(processed=False, http_status=204),
            delivery(
                delivery_id="del-2",
                event_id="evt-2",
                processed=True,
                http_status=500,
            ),
        ]
    )
    codes = {item.code for item in report.findings}
    assert {"failure_acknowledged", "success_rejected"} <= codes


def test_out_of_order_sequence_is_reported():
    report = audit_deliveries(
        [
            delivery(aggregate_key="order-7", sequence=3),
            delivery(
                delivery_id="del-2",
                event_id="evt-2",
                aggregate_key="order-7",
                sequence=2,
            ),
        ]
    )
    assert "out_of_order_sequence" in {
        item.code for item in report.findings
    }


def test_naive_timestamp_is_rejected():
    with pytest.raises(ValueError, match="timezone"):
        audit_deliveries(
            [delivery(sent_at="2026-10-03T09:00:00")]
        )


def test_no_key_uses_local_mode(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    assert HookSentryAgent().inspect([delivery()]).mode == "local"
