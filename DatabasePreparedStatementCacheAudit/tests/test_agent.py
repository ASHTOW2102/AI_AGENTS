import unittest
from agent import audit


class DatabasePreparedStatementCacheAuditTests(unittest.TestCase):

    def test_disabled(self):
        self.assertTrue(audit({"prepared_statement_cache_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"prepared_statement_cache_enabled": True, "cache_size": 100, "distinct_query_shapes": 20}))
