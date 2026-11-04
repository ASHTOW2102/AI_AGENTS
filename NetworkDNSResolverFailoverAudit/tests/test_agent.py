import unittest
from agent import audit


class NetworkDNSResolverFailoverAuditTests(unittest.TestCase):

    def test_single_resolver(self):
        self.assertTrue(audit({"resolver_count": 1}))

    def test_ok(self):
        self.assertFalse(audit({"resolver_count": 2, "failover_tested": True, "negative_cache_ttl_seconds": 60}))
