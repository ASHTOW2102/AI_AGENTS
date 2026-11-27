import unittest
from agent import audit


class DatabaseForeignKeyCascadeAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"references_financial_data": True, "on_delete": "CASCADE"}))

    def test_ok(self):
        self.assertFalse(audit({"references_financial_data": True, "on_delete": "RESTRICT"}))
