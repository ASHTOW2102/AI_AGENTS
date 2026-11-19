import unittest
from agent import audit


class DatabaseSerialColumnWraparoundAuditTests(unittest.TestCase):

    def test_near_wraparound(self):
        self.assertTrue(audit({"current_value": 95, "max_value_for_type": 100, "max_acceptable_utilization": 0.8}))

    def test_ok(self):
        self.assertFalse(audit({"current_value": 10, "max_value_for_type": 100, "max_acceptable_utilization": 0.8}))
