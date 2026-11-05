import unittest
from agent import audit


class APIThrottleResponseHeaderAuditTests(unittest.TestCase):

    def test_no_retry_after(self):
        self.assertTrue(audit({"status": 429, "headers": {}}))

    def test_ok(self):
        self.assertFalse(audit({"status": 429, "headers": {"Retry-After": "5", "X-RateLimit-Remaining": "0"}, "rate_limited_endpoint": True, "body_cacheable": False}))
