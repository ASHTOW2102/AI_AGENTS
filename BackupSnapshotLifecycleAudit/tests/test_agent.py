import unittest
from agent import audit


class BackupSnapshotLifecycleAuditTests(unittest.TestCase):

    def test_no_lifecycle(self):
        self.assertTrue(audit({"lifecycle_policy_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"lifecycle_policy_configured": True, "age_days": 10, "retention_policy_days": 90}))
