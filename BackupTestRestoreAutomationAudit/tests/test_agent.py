import unittest
from agent import audit


class BackupTestRestoreAutomationAuditTests(unittest.TestCase):

    def test_manual_only(self):
        self.assertTrue(audit({"automated_restore_test_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"automated_restore_test_enabled": True, "days_since_last_successful_test": 5, "max_acceptable_test_interval_days": 30}))
