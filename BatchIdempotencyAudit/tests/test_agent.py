import unittest
from agent import audit


class BatchIdempotencyAuditTests(unittest.TestCase):
    def test_retry_without_key(self):
        self.assertTrue(any("idempotency key" in f["issue"] for f in audit({"retry_enabled": True})))

    def test_safe_job(self):
        job = {"retry_enabled": True, "idempotency_key": "job-id", "max_attempts": 3,
               "writes_external_state": True, "deduplication_store": True,
               "idempotency_ttl_hours": 48, "max_retry_window_hours": 24}
        self.assertEqual([], audit(job))


if __name__ == "__main__":
    unittest.main()
