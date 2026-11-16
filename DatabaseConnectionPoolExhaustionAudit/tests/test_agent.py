import unittest
from agent import audit


class DatabaseConnectionPoolExhaustionAuditTests(unittest.TestCase):

    def test_near_exhaustion(self):
        self.assertTrue(audit({"active_connections": 95, "max_connections": 100, "max_acceptable_utilization": 0.85}))

    def test_ok(self):
        self.assertFalse(audit({"active_connections": 20, "max_connections": 100, "max_acceptable_utilization": 0.85, "queueing_enabled_on_exhaustion": True}))
