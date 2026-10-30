import unittest
from agent import audit


class OAuthDeviceFlowAuditTests(unittest.TestCase):
    def test_unlimited_polling(self):
        self.assertIn("not rate limited", audit({"device_flow_enabled": True,
                                                 "polling_rate_limited": False})[0]["issue"])

    def test_restricted_device_flow(self):
        flow = {"device_flow_enabled": True, "user_code_entropy_adequate": True,
                "polling_rate_limited": True, "device_code_ttl_seconds": 600,
                "max_device_code_ttl_seconds": 1800, "user_consent_displayed": True}
        self.assertEqual([], audit(flow))


if __name__ == "__main__":
    unittest.main()
