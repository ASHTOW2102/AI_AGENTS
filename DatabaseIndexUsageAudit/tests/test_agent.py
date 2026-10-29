import unittest
from agent import audit


class DatabaseIndexUsageAuditTests(unittest.TestCase):
    def test_duplicate_index(self):
        self.assertIn("duplicates", audit({"indexes": [{"name": "idx_b", "duplicate_of": "idx_a"}]})[0]["issue"])

    def test_active_indexes(self):
        report = {"indexes": [{"name": "idx_main", "unused_days": 1}], "critical_queries_without_index": 0}
        self.assertEqual([], audit(report))


if __name__ == "__main__":
    unittest.main()
