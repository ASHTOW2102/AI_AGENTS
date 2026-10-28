import unittest
from agent import audit


class DataLineageCompletenessAuditTests(unittest.TestCase):
    def test_missing_consumer(self):
        self.assertIn("warehouse", audit({"required_downstream_consumers": ["warehouse"],
                                           "documented_downstream_consumers": []})[0]["issue"])

    def test_complete_lineage(self):
        dataset = {"upstream_sources": ["events"], "critical": True, "owner": "data-platform",
                   "required_downstream_consumers": ["warehouse"],
                   "documented_downstream_consumers": ["warehouse"], "lineage_last_verified": "2026-10-01"}
        self.assertEqual([], audit(dataset))


if __name__ == "__main__":
    unittest.main()
