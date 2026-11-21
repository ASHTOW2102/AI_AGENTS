import unittest
from agent import audit


class ServerlessAPIGatewayThrottlingAuditTests(unittest.TestCase):

    def test_no_throttle(self):
        self.assertTrue(audit({"throttle_rate_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"throttle_rate_configured": True, "throttle_rate_limit": 50, "downstream_function_concurrency_limit": 100}))
