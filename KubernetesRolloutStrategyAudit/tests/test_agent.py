import unittest
from agent import audit


class KubernetesRolloutStrategyAuditTests(unittest.TestCase):
    def test_all_replicas_can_become_unavailable(self):
        self.assertIn("every replica", audit({"replicas": 3, "max_unavailable": 3})[0]["issue"])

    def test_available_rollout(self):
        deployment = {"replicas": 3, "max_unavailable": 1, "max_surge": 1,
                      "progress_deadline_seconds": 300, "automatic_rollback_expected": False}
        self.assertEqual([], audit(deployment))


if __name__ == "__main__":
    unittest.main()
