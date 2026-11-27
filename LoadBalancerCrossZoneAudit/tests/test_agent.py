import unittest
from agent import audit


class LoadBalancerCrossZoneAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"targets_span_multiple_zones": True, "cross_zone_load_balancing_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"targets_span_multiple_zones": True, "cross_zone_load_balancing_enabled": True}))
