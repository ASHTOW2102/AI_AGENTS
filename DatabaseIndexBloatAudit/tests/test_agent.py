import unittest
from agent import audit


class DatabaseIndexBloatAuditTests(unittest.TestCase):

    def test_bloated(self):
        self.assertTrue(audit({"bloat_ratio": 0.6, "reindex_scheduled": False}))

    def test_ok(self):
        self.assertFalse(audit({"bloat_ratio": 0.1, "max_acceptable_bloat_ratio": 0.3, "reindex_scheduled": True, "unused_for_days": 2}))
