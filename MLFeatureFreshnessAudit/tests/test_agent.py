import unittest
from agent import audit


class MLFeatureFreshnessAuditTests(unittest.TestCase):
    def test_stale_feature(self):
        self.assertTrue(any("older" in item["issue"] for item in audit({"observed_age_minutes": 20, "max_age_minutes": 5})))

    def test_fresh_feature(self):
        feature = {"observed_age_minutes": 1, "max_age_minutes": 5, "training_freshness_minutes": 2,
                   "serving_freshness_minutes": 5, "null_rate_percent": 0, "max_null_rate_percent": 1,
                   "owner": "ml-platform"}
        self.assertEqual([], audit(feature))


if __name__ == "__main__":
    unittest.main()
