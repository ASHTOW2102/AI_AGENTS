import unittest
from agent import audit


class FeatureFlagKillSwitchAuditTests(unittest.TestCase):

    def test_untested(self):
        self.assertTrue(audit({"risk_level": "high", "kill_switch_tested": False}))

    def test_ok(self):
        self.assertFalse(audit({"risk_level": "high", "kill_switch_tested": True, "rollback_time_seconds": 10, "max_acceptable_rollback_seconds": 60}))
