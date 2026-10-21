import unittest
from agent import audit


class CostAnomalyEvidenceAuditTests(unittest.TestCase):
    def test_unalerted_variance(self):
        self.assertTrue(any("without an alert" in f["issue"] for f in audit({"variance_percent": 80, "alert_threshold_percent": 20})))

    def test_documented_anomaly(self):
        item = {"variance_percent": 10, "alert_threshold_percent": 20, "monthly_estimate": 40,
                "materiality_amount": 100, "owner": "team", "service": "api"}
        self.assertEqual([], audit(item))


if __name__ == "__main__":
    unittest.main()
