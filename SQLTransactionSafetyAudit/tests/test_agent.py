import unittest
from agent import audit


class SQLTransactionSafetyAuditTests(unittest.TestCase):
    def test_financial_dirty_read(self):
        self.assertIn("read-uncommitted", audit({"financial_data": True, "isolation_level": "read_uncommitted"})[0]["issue"])

    def test_safe_transaction(self):
        item = {"writes_data": True, "rollback_defined": True, "retryable": True, "idempotent": True,
                "isolation_level": "serializable", "expected_lock_seconds": 1, "max_lock_seconds": 5}
        self.assertEqual([], audit(item))


if __name__ == "__main__":
    unittest.main()
