import unittest
from agent import audit


class CacheStampedeProtectionAuditTests(unittest.TestCase):

    def test_high_concurrency_no_protection(self):
        self.assertTrue(audit({"expected_concurrent_requests": 200, "uses_recompute_lock": False, "uses_early_expiry_jitter": False}))

    def test_ok(self):
        self.assertFalse(audit({"expected_concurrent_requests": 200, "uses_recompute_lock": True, "ttl_seconds": 60}))
