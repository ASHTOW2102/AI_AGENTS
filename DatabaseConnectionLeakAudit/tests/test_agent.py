import unittest
from agent import audit


class DatabaseConnectionLeakAuditTests(unittest.TestCase):

    def test_saturated(self):
        self.assertTrue(audit({"active_connections": 10, "pool_size": 10, "growth_trend": "increasing"}))

    def test_ok(self):
        self.assertFalse(audit({"active_connections": 2, "pool_size": 10, "longest_held_connection_minutes": 1}))
