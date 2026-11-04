import unittest
from agent import audit


class DatabaseLongRunningQueryAuditTests(unittest.TestCase):

    def test_no_timeout(self):
        self.assertTrue(audit({"statement_timeout_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"statement_timeout_configured": True, "duration_seconds": 5, "max_acceptable_duration_seconds": 30, "holds_locks": False}))
