import unittest
from agent import audit


class KubernetesNodeDrainReadinessAuditTests(unittest.TestCase):
    def test_critical_without_pdb(self):
        self.assertIn("disruption-budget", audit({"critical_workloads": 2})[0]["issue"])

    def test_drain_ready_node(self):
        node = {"critical_workloads": 2, "pod_disruption_budget_coverage": True,
                "daemonsets_unmanaged": False, "local_storage_workloads": 0,
                "max_unavailable_nodes": 1, "approved_max_unavailable_nodes": 1}
        self.assertEqual([], audit(node))


if __name__ == "__main__":
    unittest.main()
