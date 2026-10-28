import unittest
from agent import audit


class APIIdempotencyContractAuditTests(unittest.TestCase):
    def test_retryable_write_without_key(self):
        self.assertIn("idempotency-key", audit({"retryable_write": True})[0]["issue"])

    def test_valid_contract(self):
        item = {"retryable_write": True, "idempotency_key_supported": True,
                "key_retention_hours": 48, "max_retry_window_hours": 24, "payload_conflict_rejected": True}
        self.assertEqual([], audit(item))


if __name__ == "__main__":
    unittest.main()
