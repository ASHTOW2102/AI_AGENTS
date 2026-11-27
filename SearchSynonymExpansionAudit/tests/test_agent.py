import unittest
from agent import audit


class SearchSynonymExpansionAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"synonym_list_last_updated_days_ago": 400, "max_staleness_days": 180}))

    def test_ok(self):
        self.assertFalse(audit({"synonym_list_last_updated_days_ago": 30, "max_staleness_days": 180}))
