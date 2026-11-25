import unittest
from agent import audit


class DatabaseDeadlockRetryStormAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"deadlock_retry_enabled": True, "retry_backoff_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"deadlock_retry_enabled": True, "retry_backoff_configured": True}))
