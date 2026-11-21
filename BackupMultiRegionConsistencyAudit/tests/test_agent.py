import unittest
from agent import audit


class BackupMultiRegionConsistencyAuditTests(unittest.TestCase):

    def test_mismatch(self):
        self.assertTrue(audit({"primary_checksum": "abc", "replica_checksum": "def"}))

    def test_ok(self):
        self.assertFalse(audit({"primary_checksum": "abc", "replica_checksum": "abc", "checksum_comparison_automated": True}))
