import unittest
from agent import audit


class DatabaseDeadlockRetryAuditTests(unittest.TestCase):

    def test_unbounded_retry(self):
        self.assertTrue(audit({"deadlock_retry_enabled": True, "max_retry_count": None}))

    def test_ok(self):
        self.assertFalse(audit({"deadlock_retry_enabled": True, "max_retry_count": 3, "backoff_strategy": "exponential", "deadlock_rate_per_hour": 1}))
