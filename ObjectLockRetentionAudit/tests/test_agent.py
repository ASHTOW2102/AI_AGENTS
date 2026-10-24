import unittest
from agent import audit


class ObjectLockRetentionAuditTests(unittest.TestCase):
    def test_missing_lock_mode(self):
        self.assertEqual("high", audit({})[0]["severity"])

    def test_compliant_retention(self):
        lock = {"retention_mode": "compliance", "retention_days": 365, "required_retention_days": 90,
                "legal_hold_required": False, "bypass_permission_count": 0}
        self.assertEqual([], audit(lock))


if __name__ == "__main__":
    unittest.main()
