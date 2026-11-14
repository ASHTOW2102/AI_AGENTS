import unittest
from agent import audit


class BackupWriteOnceStorageAuditTests(unittest.TestCase):

    def test_mutable(self):
        self.assertTrue(audit({"worm_storage_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"worm_storage_enabled": True, "retention_lock_days": 60, "min_required_lock_days": 30}))
