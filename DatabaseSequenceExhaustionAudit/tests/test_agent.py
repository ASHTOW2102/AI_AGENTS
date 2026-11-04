import unittest
from agent import audit


class DatabaseSequenceExhaustionAuditTests(unittest.TestCase):

    def test_near_exhaustion(self):
        self.assertTrue(audit({"current_value": 95, "max_value": 100, "warning_fraction": 0.8}))

    def test_ok(self):
        self.assertFalse(audit({"current_value": 10, "max_value": 100, "warning_fraction": 0.8, "data_type": "int64", "growth_rate_per_day": 10}))
