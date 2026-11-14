import unittest
from agent import audit


class ServiceMeshZoneAffinityAuditTests(unittest.TestCase):

    def test_no_zone_routing(self):
        self.assertTrue(audit({"zone_aware_routing_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"zone_aware_routing_enabled": True, "cross_zone_traffic_percent": 5, "max_acceptable_cross_zone_percent": 30}))
