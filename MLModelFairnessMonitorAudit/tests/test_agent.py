import unittest
from agent import audit


class MLModelFairnessMonitorAuditTests(unittest.TestCase):
    def test_missing_group_metrics(self):
        self.assertIn("No protected-group", audit({})[0]["issue"])

    def test_covered_metrics(self):
        report = {"protected_group_metrics": True, "max_group_gap": 0.02,
                  "approved_max_group_gap": 0.05, "days_since_last_review": 10,
                  "max_review_age_days": 90, "low_sample_groups": 0}
        self.assertEqual([], audit(report))


if __name__ == "__main__":
    unittest.main()
