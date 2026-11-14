import unittest
from agent import audit


class CloudSnapshotEncryptionAuditTests(unittest.TestCase):

    def test_unencrypted(self):
        self.assertTrue(audit({"encrypted": False}))

    def test_ok(self):
        self.assertFalse(audit({"encrypted": True, "key_age_days": 10, "max_acceptable_key_age_days": 365}))
