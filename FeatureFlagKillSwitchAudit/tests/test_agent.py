import unittest
from agent import audit


class FeatureFlagKillSwitchAuditTests(unittest.TestCase):

    def test_critical_no_kill_switch(self):
        self.assertTrue(audit({"is_critical_path": True, "has_remote_kill_switch": False}))

    def test_ok(self):
        self.assertFalse(audit({"is_critical_path": True, "has_remote_kill_switch": True, "kill_switch_requires_restart": False}))
