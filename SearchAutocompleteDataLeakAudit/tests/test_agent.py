import unittest
from agent import audit


class SearchAutocompleteDataLeakAuditTests(unittest.TestCase):

    def test_cross_user_leak(self):
        self.assertTrue(audit({"suggestions_derived_from_all_users_history": True, "per_user_isolation": False}))

    def test_ok(self):
        self.assertFalse(audit({"suggestions_derived_from_all_users_history": True, "per_user_isolation": True, "suggestions_include_pii_patterns": False}))
