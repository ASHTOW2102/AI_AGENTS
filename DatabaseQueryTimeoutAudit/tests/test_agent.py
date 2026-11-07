import unittest
from agent import audit


class DatabaseQueryTimeoutAuditTests(unittest.TestCase):

    def test_no_timeout(self):
        self.assertTrue(audit({"statement_timeout_ms": None}))

    def test_ok(self):
        self.assertFalse(audit({"statement_timeout_ms": 5000, "max_acceptable_timeout_ms": 30000}))
