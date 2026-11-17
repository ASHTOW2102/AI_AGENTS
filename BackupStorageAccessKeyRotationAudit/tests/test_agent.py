import unittest
from agent import audit


class BackupStorageAccessKeyRotationAuditTests(unittest.TestCase):

    def test_stale_key(self):
        self.assertTrue(audit({"key_age_days": 200, "max_acceptable_age_days": 90}))

    def test_ok(self):
        self.assertFalse(audit({"key_age_days": 10, "max_acceptable_age_days": 90, "key_type": "static", "rotation_automated": True}))
