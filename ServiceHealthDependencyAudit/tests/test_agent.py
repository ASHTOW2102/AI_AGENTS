import unittest
from agent import audit


class ServiceHealthDependencyAuditTests(unittest.TestCase):
    def test_liveness_coupled_to_dependency(self):
        self.assertIn("downstream failure", audit({"liveness_checks_downstream": True})[0]["issue"])

    def test_independent_health_checks(self):
        health = {"readiness_depends_on_optional_services": False, "liveness_checks_downstream": False,
                  "dependency_timeout_seconds": 2, "degraded_mode_supported": False}
        self.assertEqual([], audit(health))


if __name__ == "__main__":
    unittest.main()
