import unittest
from agent import audit


class ServerlessColdStartAuditTests(unittest.TestCase):
    def test_high_latency(self):
        self.assertIn("P95", audit({"p95_cold_start_ms": 2000, "max_p95_cold_start_ms": 1000})[0]["issue"])

    def test_healthy_function(self):
        function = {"p95_cold_start_ms": 200, "max_p95_cold_start_ms": 1000,
                    "initialization_error_rate_percent": 0, "max_initialization_error_rate_percent": 1,
                    "critical_path": False, "cold_start_dashboard": True}
        self.assertEqual([], audit(function))


if __name__ == "__main__":
    unittest.main()
