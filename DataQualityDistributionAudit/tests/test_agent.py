import unittest
from agent import audit


class DataQualityDistributionAuditTests(unittest.TestCase):
    def test_distribution_drift(self):
        self.assertIn("drift", audit({"distribution_distance": 0.5, "max_distribution_distance": 0.2})[0]["issue"])

    def test_clean_profile(self):
        profile = {"missing_rate_percent": 0, "max_missing_rate_percent": 1,
                   "distribution_distance": 0.01, "max_distribution_distance": 0.1,
                   "out_of_range_count": 0, "sample_size": 1000, "minimum_sample_size": 100}
        self.assertEqual([], audit(profile))


if __name__ == "__main__":
    unittest.main()
