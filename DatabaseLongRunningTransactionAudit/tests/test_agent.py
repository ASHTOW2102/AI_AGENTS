import unittest
from agent import audit


class DatabaseLongRunningTransactionAuditTests(unittest.TestCase):

    def test_long_running(self):
        self.assertTrue(audit({"duration_seconds": 300, "max_acceptable_duration_seconds": 60}))

    def test_ok(self):
        self.assertFalse(audit({"duration_seconds": 5, "max_acceptable_duration_seconds": 60, "holds_locks": False}))
