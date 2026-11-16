import unittest
from agent import audit


class BackupRecoveryTimeObjectiveAuditTests(unittest.TestCase):

    def test_slow_restore(self):
        self.assertTrue(audit({"measured_restore_time_minutes": 180, "rto_minutes": 60}))

    def test_ok(self):
        self.assertFalse(audit({"measured_restore_time_minutes": 20, "rto_minutes": 60, "restore_tested_within_last_quarter": True}))
