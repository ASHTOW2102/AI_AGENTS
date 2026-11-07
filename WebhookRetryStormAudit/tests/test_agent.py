import unittest
from agent import audit


class WebhookRetryStormAuditTests(unittest.TestCase):

    def test_retry_storm(self):
        self.assertTrue(audit({"retry_backoff_strategy": "fixed", "max_retries": 10, "circuit_breaker_enabled": True}))

    def test_ok(self):
        self.assertFalse(audit({"retry_backoff_strategy": "exponential", "max_retries": 5, "circuit_breaker_enabled": True}))
