import unittest
from agent import audit


class CDNCacheKeyInjectionAuditTests(unittest.TestCase):

    def test_unvalidated_header(self):
        self.assertTrue(audit({"includes_unvalidated_header_in_cache_key": True}))

    def test_ok(self):
        self.assertFalse(audit({"includes_unvalidated_header_in_cache_key": False, "includes_all_query_params_in_cache_key": False}))
