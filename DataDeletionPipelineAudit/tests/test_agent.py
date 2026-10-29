import unittest
from agent import audit


class DataDeletionPipelineAuditTests(unittest.TestCase):
    def test_pending_requests_without_worker(self):
        self.assertIn("no active processing worker", audit({"deletion_requests_pending": 3})[0]["issue"])

    def test_operational_pipeline(self):
        pipeline = {"deletion_requests_pending": 0, "worker_enabled": True,
                    "retry_dead_letter_handling": True, "completion_requires_evidence": True,
                    "evidence_store_configured": True, "oldest_pending_age_hours": 1,
                    "max_pending_age_hours": 24}
        self.assertEqual([], audit(pipeline))


if __name__ == "__main__":
    unittest.main()
