import unittest
from agent import audit


class WebhookRateLimitAuditTests(unittest.TestCase):

    def test_no_rate_limit(self):
        self.assertTrue(audit({"rate_limit_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"rate_limit_configured": True, "receiver_429_count": 0}))
