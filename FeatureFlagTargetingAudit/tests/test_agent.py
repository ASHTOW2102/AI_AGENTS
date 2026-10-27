import unittest
from agent import audit


class FeatureFlagTargetingAuditTests(unittest.TestCase):
    def test_rollout_over_limit(self):
        self.assertIn("approved limit", audit({"production_enabled": True, "rollout_percent": 80,
                                               "approved_rollout_percent": 50})[0]["issue"])

    def test_safe_targeting(self):
        flag = {"production_enabled": True, "rollout_percent": 20, "approved_rollout_percent": 50,
                "targeting_uses_user_id": True, "stable_hash_assignment": True,
                "kill_switch_required": True, "kill_switch_tested": True}
        self.assertEqual([], audit(flag))


if __name__ == "__main__":
    unittest.main()
