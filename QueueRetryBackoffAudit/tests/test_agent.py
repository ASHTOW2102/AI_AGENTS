import unittest
from agent import audit


class QueueRetryBackoffAuditTests(unittest.TestCase):
    def test_retry_forever(self):
        self.assertIn("indefinitely", audit({"retry_forever": True})[0]["issue"])

    def test_bounded_retries(self):
        queue = {"max_attempts": 3, "approved_max_attempts": 5, "backoff_seconds": 2,
                 "jitter_enabled": True, "retry_forever": False}
        self.assertEqual([], audit(queue))


if __name__ == "__main__":
    unittest.main()
