import unittest
from agent import audit


class DataCatalogCompletenessAuditTests(unittest.TestCase):

    def test_no_owner(self):
        self.assertTrue(audit({"description": "x", "owner": None, "classification": "internal"}))

    def test_ok(self):
        self.assertFalse(audit({"description": "x", "owner": "team", "classification": "internal"}))
