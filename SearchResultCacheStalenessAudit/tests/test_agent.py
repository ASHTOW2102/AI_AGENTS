import unittest
from agent import audit


class SearchResultCacheStalenessAuditTests(unittest.TestCase):

    def test_stale_ttl(self):
        self.assertTrue(audit({"ttl_seconds": 600, "index_update_interval_seconds": 60}))

    def test_ok(self):
        self.assertFalse(audit({"ttl_seconds": 30, "index_update_interval_seconds": 60, "cache_invalidated_on_index_update": True}))
