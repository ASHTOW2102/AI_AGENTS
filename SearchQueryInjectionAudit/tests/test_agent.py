import unittest
from agent import audit


class SearchQueryInjectionAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"builds_query_from_raw_string_concat": True}))

    def test_ok(self):
        self.assertFalse(audit({"builds_query_from_raw_string_concat": False}))
