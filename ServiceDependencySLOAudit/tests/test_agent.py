import unittest
from agent import audit


class ServiceDependencySLOAuditTests(unittest.TestCase):
    def test_missing_critical_fallback(self):
        self.assertIn("no fallback", audit({"dependencies": [{"name": "db", "critical": True}]})[0]["issue"])

    def test_dependency_meets_contract(self):
        service = {"required_dependency_slo_percent": 99, "max_dependency_timeout_ms": 1000,
                   "dependencies": [{"name": "db", "availability_slo_percent": 99.9,
                                     "critical": True, "fallback_defined": True, "timeout_ms": 200}]}
        self.assertEqual([], audit(service))


if __name__ == "__main__":
    unittest.main()
