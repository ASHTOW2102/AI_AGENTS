import unittest
from agent import audit


class SecretExpiryCoverageAuditTests(unittest.TestCase):
    def test_no_expiry_or_rotation(self):
        self.assertIn("neither an expiry", audit({})[0]["issue"])

    def test_managed_secret(self):
        item = {"rotation_policy": "90d", "expiry_alert_configured": True,
                "owner_active": True, "days_until_expiry": 80, "warning_window_days": 30}
        self.assertEqual([], audit(item))


if __name__ == "__main__":
    unittest.main()
