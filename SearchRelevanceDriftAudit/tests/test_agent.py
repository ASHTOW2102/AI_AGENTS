import unittest
from agent import audit


class SearchRelevanceDriftAuditTests(unittest.TestCase):
    def test_low_quality_score(self):
        self.assertIn("NDCG", audit({"ndcg_score": 0.4, "minimum_ndcg": 0.8})[0]["issue"])

    def test_healthy_evaluation(self):
        run = {"ndcg_score": 0.9, "minimum_ndcg": 0.8, "zero_result_rate_percent": 1,
               "max_zero_result_rate_percent": 5, "days_since_baseline": 20,
               "max_baseline_age_days": 90, "query_segments_evaluated": 5,
               "required_query_segments": 5}
        self.assertEqual([], audit(run))


if __name__ == "__main__":
    unittest.main()
