import unittest
from agent import audit


class HSTSHeaderAuditTests(unittest.TestCase):
    def test_missing_hsts(self):
        self.assertIn("does not send", audit({"production": True})[0]["issue"])

    def test_long_lived_policy(self):
        site = {"production": True, "hsts_enabled": True, "max_age_seconds": 31536000,
                "minimum_max_age_seconds": 15552000, "include_subdomains_required": False}
        self.assertEqual([], audit(site))


if __name__ == "__main__":
    unittest.main()
