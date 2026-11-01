import unittest
from agent import audit


class SchemaDriftAuditTests(unittest.TestCase):

    def test_extra_column(self):
        self.assertTrue(audit({"live_columns": ["a", "b"], "declared_columns": ["a"]}))

    def test_ok(self):
        self.assertFalse(audit({"live_columns": ["a"], "declared_columns": ["a"]}))
