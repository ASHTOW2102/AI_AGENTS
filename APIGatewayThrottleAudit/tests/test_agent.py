import unittest
from agent import audit


class APIGatewayThrottleAuditTests(unittest.TestCase):

    def test_no_throttle(self):
        self.assertTrue(audit({"throttle_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"throttle_configured": True, "per_client_key": True, "burst_limit": 100, "steady_rate_limit": 50}))
