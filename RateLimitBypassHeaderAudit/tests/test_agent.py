import unittest
from agent import audit


class RateLimitBypassHeaderAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"trusts_client_supplied_rate_limit_headers": True}))

    def test_ok(self):
        self.assertFalse(audit({"trusts_client_supplied_rate_limit_headers": False}))
