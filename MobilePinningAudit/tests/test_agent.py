import unittest

from agent import audit


class MobilePinningAuditTests(unittest.TestCase):
    def test_release_bypass_is_critical(self):
        findings = audit({"pinning_enabled": True, "backup_pins": ["pin"], "debug_bypass_in_release": True})
        self.assertEqual("critical", findings[0]["severity"])

    def test_missing_pinning_and_backup(self):
        self.assertEqual(1, len(audit({"pinning_enabled": False})))


if __name__ == "__main__":
    unittest.main()
