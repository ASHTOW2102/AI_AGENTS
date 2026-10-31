import unittest
from agent import audit


class DatabasePoolSaturationAuditTests(unittest.TestCase):
    def test_pool_over_budget(self):
        self.assertIn("exceeds", audit({"pool_max": 100, "database_connection_budget": 50})[0]["issue"])

    def test_healthy_pool(self):
        pool = {"utilization_percent": 30, "max_utilization_percent": 85,
                "waiting_requests": 0, "pool_max": 10, "database_connection_budget": 50,
                "connection_leak_detection": True}
        self.assertEqual([], audit(pool))


if __name__ == "__main__":
    unittest.main()
