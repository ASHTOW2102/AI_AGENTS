import unittest
from agent import audit


class CloudNATGatewayAuditTests(unittest.TestCase):

    def test_allocation_errors(self):
        self.assertTrue(audit({"port_allocation_errors": 5}))

    def test_ok(self):
        self.assertFalse(audit({"port_allocation_errors": 0, "concurrent_connections": 100, "estimated_port_capacity": 1000}))
