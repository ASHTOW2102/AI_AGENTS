import unittest
from agent import audit


class QueueDeadLetterAuditTests(unittest.TestCase):
    def test_missing_controls(self):
        self.assertEqual(2, len(audit({"dead_letter_enabled": False, "max_delivery_attempts": 0})))

    def test_retention_must_cover_replay(self):
        self.assertIn("replay window", audit({"dead_letter_retention_days": 2, "replay_window_days": 7})[0]["issue"])


if __name__ == "__main__":
    unittest.main()
