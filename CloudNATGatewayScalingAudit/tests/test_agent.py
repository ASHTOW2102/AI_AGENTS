import unittest
from agent import audit


class CloudNATGatewayScalingAuditTests(unittest.TestCase):

    def test_near_exhaustion(self):
        self.assertTrue(audit({"allocated_ports": 90, "max_ports": 100, "max_acceptable_utilization": 0.8}))

    def test_ok(self):
        self.assertFalse(audit({"allocated_ports": 20, "max_ports": 100, "max_acceptable_utilization": 0.8, "port_exhaustion_alerting_enabled": True}))
