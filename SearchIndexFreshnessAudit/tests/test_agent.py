import unittest
from agent import audit


class SearchIndexFreshnessAuditTests(unittest.TestCase):

    def test_stale(self):
        self.assertTrue(audit({"reindex_lag_seconds": 600, "max_acceptable_lag_seconds": 300}))

    def test_ok(self):
        self.assertFalse(audit({"reindex_lag_seconds": 10, "max_acceptable_lag_seconds": 300, "failed_reindex_count": 0}))
