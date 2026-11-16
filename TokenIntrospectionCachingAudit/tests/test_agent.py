import unittest
from agent import audit


class TokenIntrospectionCachingAuditTests(unittest.TestCase):

    def test_long_cache(self):
        self.assertTrue(audit({"introspection_cache_ttl_seconds": 600, "token_ttl_seconds": 300}))

    def test_ok(self):
        self.assertFalse(audit({"introspection_cache_ttl_seconds": 30, "token_ttl_seconds": 300, "cache_invalidated_on_revocation": True}))
