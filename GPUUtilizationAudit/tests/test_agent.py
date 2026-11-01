import unittest
from agent import audit


class GPUUtilizationAuditTests(unittest.TestCase):

    def test_low_utilization(self):
        self.assertTrue(audit({"avg_utilization_percent": 10, "min_expected_utilization_percent": 30}))

    def test_ok(self):
        self.assertFalse(audit({"avg_utilization_percent": 60, "idle_hours_per_day": 1, "memory_oom_events": 0}))
