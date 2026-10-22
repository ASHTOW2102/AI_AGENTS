import unittest
from agent import audit


class DataArchiveRetrievalAuditTests(unittest.TestCase):
    def test_slow_retrieval(self):
        self.assertIn("exceeds", audit({"measured_retrieval_hours": 8, "target_retrieval_hours": 2})[0]["issue"])

    def test_ready_archive(self):
        archive = {"retrieval_procedure": "runbook", "measured_retrieval_hours": 1,
                   "target_retrieval_hours": 4, "restore_permission_tested": True, "owner": "data-team"}
        self.assertEqual([], audit(archive))


if __name__ == "__main__":
    unittest.main()
