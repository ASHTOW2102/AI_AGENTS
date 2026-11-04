import unittest
from agent import audit


class ServerlessConcurrencyLimitAuditTests(unittest.TestCase):

    def test_no_limit(self):
        self.assertTrue(audit({"concurrency_limit_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"concurrency_limit_configured": True, "max_concurrency": 10, "downstream_safe_capacity": 50, "shares_account_concurrency_pool": False}))
