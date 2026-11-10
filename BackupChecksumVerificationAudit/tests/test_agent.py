import unittest
from agent import audit


class BackupChecksumVerificationAuditTests(unittest.TestCase):

    def test_unverified(self):
        self.assertTrue(audit({"checksum_verified_after_write": False}))

    def test_ok(self):
        self.assertFalse(audit({"checksum_verified_after_write": True, "checksum_mismatch_count": 0}))
