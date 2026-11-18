import unittest
from agent import audit


class SearchTypoToleranceAbuseAuditTests(unittest.TestCase):

    def test_restricted_leak(self):
        self.assertTrue(audit({"fuzzy_matching_enabled": True, "indexes_restricted_terms": True, "fuzzy_matching_excludes_restricted_terms": False}))

    def test_ok(self):
        self.assertFalse(audit({"fuzzy_matching_enabled": True, "indexes_restricted_terms": True, "fuzzy_matching_excludes_restricted_terms": True, "query_rate_limited": True}))
