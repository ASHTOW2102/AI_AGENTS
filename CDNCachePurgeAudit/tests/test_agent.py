import unittest
from agent import audit


class CDNCachePurgeAuditTests(unittest.TestCase):

    def test_missing_purge(self):
        self.assertTrue(audit({"cache_affecting_change": True, "purge_triggered": False}))

    def test_ok(self):
        self.assertFalse(audit({"cache_affecting_change": True, "purge_triggered": True, "purge_propagation_seconds": 10}))
