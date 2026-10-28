import unittest
from agent import audit


class WebhookReplayProtectionAuditTests(unittest.TestCase):
    def test_missing_deduplication(self):
        self.assertIn("not deduplicated", audit({"timestamp_validated": True})[0]["issue"])

    def test_bounded_replay_window(self):
        endpoint = {"timestamp_validated": True, "nonce_or_event_id_deduplicated": True,
                    "accepted_timestamp_skew_seconds": 60, "max_timestamp_skew_seconds": 300,
                    "deduplication_ttl_seconds": 900, "replay_window_seconds": 600}
        self.assertEqual([], audit(endpoint))


if __name__ == "__main__":
    unittest.main()
