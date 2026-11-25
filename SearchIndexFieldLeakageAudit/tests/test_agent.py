import unittest
from agent import audit


class SearchIndexFieldLeakageAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"indexed_fields": ["name", "ssn"], "pii_fields": ["ssn"]}))

    def test_ok(self):
        self.assertFalse(audit({"indexed_fields": ["name"], "pii_fields": ["ssn"]}))
