import unittest
from agent import audit


class BackupVerificationChecksumAuditTests(unittest.TestCase):

    def test_no_checksum(self):
        self.assertTrue(audit({"checksum_computed_at_write_time": False}))

    def test_ok(self):
        self.assertFalse(audit({"checksum_computed_at_write_time": True, "checksum_verified_on_restore_test": True, "checksum_mismatch_detected": False}))
