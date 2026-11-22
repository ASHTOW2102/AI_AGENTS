import unittest
from agent import audit


class WebhookSignatureVerificationAuditTests(unittest.TestCase):

    def test_no_verification(self):
        self.assertTrue(audit({"verifies_hmac_signature": False}))

    def test_ok(self):
        self.assertFalse(audit({"verifies_hmac_signature": True, "uses_constant_time_compare": True, "accepts_replay_without_timestamp_check": False}))
