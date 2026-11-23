import unittest
from agent import audit


class ServerlessColdStartTimeoutAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"avg_cold_start_ms": 2800, "timeout_ms": 3000}))

    def test_ok(self):
        self.assertFalse(audit({"avg_cold_start_ms": 500, "timeout_ms": 3000}))
