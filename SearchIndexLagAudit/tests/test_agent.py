import unittest
from agent import audit


class SearchIndexLagAuditTests(unittest.TestCase):
    def test_stale_index(self):
        self.assertIn("freshness", audit({"observed_lag_seconds": 20, "max_lag_seconds": 5})[0]["issue"])

    def test_fresh_index(self):
        index = {"observed_lag_seconds": 1, "max_lag_seconds": 5, "failed_documents": 0,
                 "oldest_queued_age_seconds": 1, "max_queued_age_seconds": 20, "lag_alert_configured": True}
        self.assertEqual([], audit(index))


if __name__ == "__main__":
    unittest.main()
