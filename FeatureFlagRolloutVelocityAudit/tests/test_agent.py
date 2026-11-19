import unittest
from agent import audit


class FeatureFlagRolloutVelocityAuditTests(unittest.TestCase):

    def test_big_jump(self):
        self.assertTrue(audit({"new_rollout_percent": 100, "previous_rollout_percent": 10, "max_acceptable_jump_percent": 25}))

    def test_ok(self):
        self.assertFalse(audit({"new_rollout_percent": 50, "previous_rollout_percent": 25, "max_acceptable_jump_percent": 25}))
