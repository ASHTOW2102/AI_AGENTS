import unittest
from agent import audit


class DataRetentionExceptionAuditTests(unittest.TestCase):
    def test_missing_expiry(self):
        self.assertIn("no expiry date", audit({})[2]["issue"])

    def test_approved_exception(self):
        exception = {"exception_reference": "EX-1", "owner": "privacy-team",
                     "expires_on": "2026-12-31", "data_classes": ["audit"], "scope_minimized": True}
        self.assertEqual([], audit(exception))


if __name__ == "__main__":
    unittest.main()
