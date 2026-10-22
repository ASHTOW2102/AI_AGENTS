import unittest
from agent import audit


class MobileBackupPrivacyAuditTests(unittest.TestCase):
    def test_sensitive_backup_path(self):
        self.assertTrue(any("database" in f["issue"] for f in audit({"backup_included_paths": ["database"],
                                                                      "sensitive_paths": ["database"]})))

    def test_excluded_sensitive_data(self):
        self.assertEqual([], audit({"backup_enabled": True, "backup_encryption_confirmed": True,
                                    "backup_included_paths": ["preferences"], "sensitive_paths": ["token"],
                                    "auth_tokens_backup_enabled": False}))


if __name__ == "__main__":
    unittest.main()
