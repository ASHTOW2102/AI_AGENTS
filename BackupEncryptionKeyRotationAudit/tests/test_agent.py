import unittest
from agent import audit


class BackupEncryptionKeyRotationAuditTests(unittest.TestCase):

    def test_stale_key(self):
        self.assertTrue(audit({"key_age_days": 400, "max_key_age_days": 365}))

    def test_ok(self):
        self.assertFalse(audit({"key_age_days": 30, "max_key_age_days": 365, "key_stored_alongside_backup": False}))
