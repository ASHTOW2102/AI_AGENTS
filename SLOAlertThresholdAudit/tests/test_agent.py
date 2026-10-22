import unittest
from agent import audit


class SLOAlertThresholdAuditTests(unittest.TestCase):
    def test_threshold_beyond_objective(self):
        self.assertIn("SLO", audit({"alert_error_rate_percent": 2, "objective_error_rate_percent": 1})[0]["issue"])

    def test_bounded_alerts(self):
        slo = {"alert_error_rate_percent": 0.5, "objective_error_rate_percent": 1,
               "alert_latency_ms": 300, "objective_latency_ms": 500,
               "burn_rate_alert_configured": True, "alert_owner": "oncall"}
        self.assertEqual([], audit(slo))


if __name__ == "__main__":
    unittest.main()
