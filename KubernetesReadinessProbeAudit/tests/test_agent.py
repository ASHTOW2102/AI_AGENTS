import unittest
from agent import audit


class KubernetesReadinessProbeAuditTests(unittest.TestCase):
    def test_missing_readiness_probe(self):
        self.assertIn("readiness probe", audit({})[0]["issue"])

    def test_probe_timing_is_safe(self):
        workload = {"readiness_probe": True, "liveness_probe": True,
                    "liveness_initial_delay_seconds": 30, "startup_duration_p99_seconds": 10,
                    "readiness_failure_threshold": 3, "min_readiness_failure_threshold": 1}
        self.assertEqual([], audit(workload))


if __name__ == "__main__":
    unittest.main()
