import unittest
from agent import audit


class CloudVPCPeeringTransitAuditTests(unittest.TestCase):

    def test_unreviewed_propagation(self):
        self.assertTrue(audit({"route_propagation_enabled": True, "transit_routes_reviewed": False}))

    def test_ok(self):
        self.assertFalse(audit({"route_propagation_enabled": True, "transit_routes_reviewed": True, "allows_transitive_peering": False}))
