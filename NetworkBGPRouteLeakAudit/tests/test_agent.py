import unittest
from agent import audit


class NetworkBGPRouteLeakAuditTests(unittest.TestCase):

    def test_leak(self):
        self.assertTrue(audit({"internal_prefix": True, "advertised_to_external_peer": True}))

    def test_ok(self):
        self.assertFalse(audit({"internal_prefix": True, "advertised_to_external_peer": False, "prefix_filter_configured": True, "max_prefix_limit_configured": True}))
