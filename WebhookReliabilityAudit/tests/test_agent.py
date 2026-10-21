import unittest
from agent import audit


class WebhookReliabilityAuditTests(unittest.TestCase):
    def test_missing_signature_and_idempotency(self):
        findings = audit({"retry_max_attempts": 3, "retry_backoff_seconds": 1})
        self.assertEqual(2, len(findings))

    def test_complete_policy(self):
        self.assertEqual([], audit({"retry_max_attempts": 3, "retry_backoff_seconds": 2,
                                    "signature_verification": True, "idempotency_handling": True,
                                    "failure_alert_threshold": 5}))


if __name__ == "__main__":
    unittest.main()
