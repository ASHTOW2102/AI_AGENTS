import unittest
from agent import audit


class WebhookRetryIdempotencyAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"supports_retries": True, "has_idempotency_key_check": False}))

    def test_ok(self):
        self.assertFalse(audit({"supports_retries": True, "has_idempotency_key_check": True}))
