import unittest
from agent import audit


class DNSFailoverHealthAuditTests(unittest.TestCase):
    def test_failover_without_health_check(self):
        self.assertIn("without a health check", audit({"failover_enabled": True})[0]["issue"])

    def test_ready_failover(self):
        zone = {"failover_enabled": True, "health_check_configured": True,
                "health_check_multi_region": True, "failback_tested": True,
                "health_check_interval_seconds": 10, "max_health_check_interval_seconds": 60}
        self.assertEqual([], audit(zone))


if __name__ == "__main__":
    unittest.main()
