import unittest
from datetime import date
from agent import audit


class FeatureFlagLifecycleAuditTests(unittest.TestCase):
    def test_expired_enabled_flag(self):
        findings = audit({"temporary": True, "expiry_date": "2025-01-01", "enabled": True}, date(2026, 1, 1))
        self.assertTrue(any("Expired" in item["issue"] for item in findings))

    def test_production_needs_rollback(self):
        self.assertEqual("high", audit({"production_enabled": True})[-1]["severity"])


if __name__ == "__main__":
    unittest.main()
