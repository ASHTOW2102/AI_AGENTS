import unittest
from agent import audit


class CloudCostAnomalyAuditTests(unittest.TestCase):

    def test_spike(self):
        self.assertTrue(audit({"baseline_daily_cost": 100, "current_daily_cost": 500, "anomaly_multiplier": 2}))

    def test_ok(self):
        self.assertFalse(audit({"baseline_daily_cost": 100, "current_daily_cost": 110, "anomaly_multiplier": 2, "budget_alert_configured": True}))
