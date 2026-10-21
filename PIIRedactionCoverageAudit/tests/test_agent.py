import unittest
from agent import audit


class PIIRedactionCoverageAuditTests(unittest.TestCase):
    def test_uncovered_fields(self):
        self.assertIn("email", audit({"sensitive_fields": ["email", "phone"], "redacted_fields": ["phone"]})[0]["issue"])

    def test_complete_policy(self):
        self.assertEqual([], audit({"sensitive_fields": ["email"], "redacted_fields": ["email"],
                                    "redaction_tested": True, "raw_payload_retention_days": 3,
                                    "max_raw_payload_retention_days": 3}))


if __name__ == "__main__":
    unittest.main()
