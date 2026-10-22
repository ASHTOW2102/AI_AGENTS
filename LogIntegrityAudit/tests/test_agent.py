import unittest
from agent import audit


class LogIntegrityAuditTests(unittest.TestCase):
    def test_no_tamper_protection(self):
        self.assertEqual("high", audit({"tamper_protection": False})[0]["severity"])

    def test_hardened_logging(self):
        policy = {"tamper_protection": True, "access_audited": True, "retention_days": 400,
                  "minimum_retention_days": 365, "admin_write_access": True, "separate_admin_domain": True}
        self.assertEqual([], audit(policy))


if __name__ == "__main__":
    unittest.main()
