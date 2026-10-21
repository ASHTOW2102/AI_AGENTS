import unittest

from agent import audit


class BackupEncryptionAuditTests(unittest.TestCase):
    def test_flags_unencrypted_backup(self):
        self.assertEqual("critical", audit({"encrypted": False})[0]["severity"])

    def test_accepts_managed_rotated_backup(self):
        self.assertEqual([], audit({"encrypted": True, "key_type": "managed_kms", "key_rotation_days": 90,
                                    "restore_access_count": 2, "approved_restore_access_count": 2}))


if __name__ == "__main__":
    unittest.main()
