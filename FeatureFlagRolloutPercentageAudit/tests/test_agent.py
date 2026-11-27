import unittest
from agent import audit


class FeatureFlagRolloutPercentageAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"rollout_percentage": 25, "has_kill_switch": False}))

    def test_ok(self):
        self.assertFalse(audit({"rollout_percentage": 25, "has_kill_switch": True}))
