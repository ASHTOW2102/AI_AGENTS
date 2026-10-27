import unittest
from agent import audit


class QueueVisibilityTimeoutAuditTests(unittest.TestCase):
    def test_timeout_too_short(self):
        self.assertIn("P99", audit({"visibility_timeout_seconds": 5, "p99_processing_seconds": 10})[0]["issue"])

    def test_adequate_timeout(self):
        queue = {"visibility_timeout_seconds": 60, "p99_processing_seconds": 20,
                 "max_visibility_timeout_seconds": 120, "inflight_limit": 100,
                 "max_concurrent_handlers": 20, "long_processing": False}
        self.assertEqual([], audit(queue))


if __name__ == "__main__":
    unittest.main()
