import unittest
from agent import audit


class NetworkVPNSplitTunnelAuditTests(unittest.TestCase):

    def test_excluded_traffic(self):
        self.assertTrue(audit({"split_tunnel_enabled": True, "corporate_traffic_excluded_from_tunnel": True}))

    def test_ok(self):
        self.assertFalse(audit({"split_tunnel_enabled": True, "corporate_traffic_excluded_from_tunnel": False, "dns_leak_protection_enabled": True}))
