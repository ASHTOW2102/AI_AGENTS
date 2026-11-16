import unittest
from agent import audit


class DataRetentionPolicyEnforcementAuditTests(unittest.TestCase):

    def test_unenforced(self):
        self.assertTrue(audit({"retention_policy_days": 90, "automated_deletion_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"retention_policy_days": 90, "automated_deletion_enabled": True, "last_deletion_run_days_ago": 1, "expected_run_interval_days": 30}))
