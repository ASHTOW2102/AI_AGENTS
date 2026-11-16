import unittest
from agent import audit


class SearchQueryRateLimitAuditTests(unittest.TestCase):

    def test_no_limit(self):
        self.assertTrue(audit({"rate_limit_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"rate_limit_configured": True, "supports_expensive_queries": True, "query_cost_estimation_enabled": True}))
