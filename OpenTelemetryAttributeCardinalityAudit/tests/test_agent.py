import unittest
from agent import audit


class OpenTelemetryAttributeCardinalityAuditTests(unittest.TestCase):
    def test_user_id_dimension(self):
        findings = audit({"metrics": [{"name": "requests", "high_cardinality_attributes": ["user_id"]}],
                          "cardinality_alert_configured": True})
        self.assertIn("user_id", findings[0]["issue"])

    def test_bounded_metrics(self):
        metrics = {"metrics": [{"name": "requests", "estimated_series": 100, "max_series": 1000}],
                   "cardinality_alert_configured": True}
        self.assertEqual([], audit(metrics))


if __name__ == "__main__":
    unittest.main()
