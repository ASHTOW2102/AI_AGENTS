import unittest
from agent import audit


class MultiRegionReadinessAuditTests(unittest.TestCase):
    def test_missing_region(self):
        self.assertIn("fewer than two", audit({"multi_region_required": True, "regions": 1})[0]["issue"])

    def test_ready_service(self):
        service = {"multi_region_required": True, "regions": 2, "critical_dependencies": ["db"],
                   "failover_dependencies": ["db"], "failover_enabled": True,
                   "traffic_switch_tested": True, "measured_failover_minutes": 2,
                   "target_failover_minutes": 5}
        self.assertEqual([], audit(service))


if __name__ == "__main__":
    unittest.main()
