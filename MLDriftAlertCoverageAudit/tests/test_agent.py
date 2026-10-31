import unittest
from agent import audit


class MLDriftAlertCoverageAuditTests(unittest.TestCase):
    def test_measured_drift_without_alert(self):
        self.assertIn("no alert", audit({"drift_metric_enabled": True})[0]["issue"])

    def test_monitored_model(self):
        model = {"drift_metric_enabled": True, "drift_alert_configured": True,
                 "drift_threshold": 0.2, "production": True,
                 "feature_drift_monitored": True, "alert_owner": "ml-ops"}
        self.assertEqual([], audit(model))


if __name__ == "__main__":
    unittest.main()
