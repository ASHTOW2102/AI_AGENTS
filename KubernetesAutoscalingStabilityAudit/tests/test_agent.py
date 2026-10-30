import unittest
from agent import audit


class KubernetesAutoscalingStabilityAuditTests(unittest.TestCase):
    def test_invalid_replica_range(self):
        self.assertIn("Minimum replicas", audit({"min_replicas": 5, "max_replicas": 2})[0]["issue"])

    def test_stable_scaler(self):
        scaler = {"min_replicas": 2, "max_replicas": 10, "scale_down_stabilization_seconds": 300,
                  "min_scale_down_stabilization_seconds": 60, "metrics_available": True,
                  "capacity_supported_replicas": 20}
        self.assertEqual([], audit(scaler))


if __name__ == "__main__":
    unittest.main()
