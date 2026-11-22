import unittest
from agent import audit


class SearchIndexStalenessAuditTests(unittest.TestCase):

    def test_no_monitoring(self):
        self.assertTrue(audit({"monitors_index_staleness": False, "freshness_sla_seconds": None}))

    def test_ok(self):
        self.assertFalse(audit({"monitors_index_staleness": True, "freshness_sla_seconds": 300}))
