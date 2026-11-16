import unittest
from agent import audit


class APIGatewayAuthBypassAuditTests(unittest.TestCase):

    def test_bypassable(self):
        self.assertTrue(audit({"reachable_directly": True, "requires_auth_at_gateway": True, "requires_auth_at_service": False}))

    def test_ok(self):
        self.assertFalse(audit({"reachable_directly": False, "requires_auth_at_gateway": True, "requires_auth_at_service": True, "gateway_enforces_auth": True}))
