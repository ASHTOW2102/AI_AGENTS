import unittest
from agent import audit


class WebhookPayloadSizeAuditTests(unittest.TestCase):

    def test_exceeds_receiver_limit(self):
        self.assertTrue(audit({"max_payload_bytes": 5_000_000, "known_receiver_limit_bytes": 1_000_000}))

    def test_ok(self):
        self.assertFalse(audit({"max_payload_bytes": 500_000, "known_receiver_limit_bytes": 1_000_000, "payload_grows_with_data_volume": False}))
