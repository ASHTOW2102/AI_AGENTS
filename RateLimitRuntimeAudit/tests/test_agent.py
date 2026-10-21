import unittest

from agent import audit


class RateLimitRuntimeAuditTests(unittest.TestCase):
    def test_reports_unisolated_limits_and_missing_alert(self):
        findings = audit({"throttled_requests": 3, "per_tenant_limits": False})
        self.assertEqual(2, len(findings))

    def test_healthy_metrics(self):
        self.assertEqual([], audit({"throttled_requests": 0, "per_tenant_limits": True,
                                    "limit_saturation_percent": 40, "throttle_5xx_rate": 0,
                                    "max_throttle_5xx_rate": 0}))


if __name__ == "__main__":
    unittest.main()
