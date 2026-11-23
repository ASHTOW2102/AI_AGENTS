import unittest
from agent import audit


class DatabaseCompositeIndexRedundancyAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"indexes": [["a"], ["a", "b"]]}))

    def test_ok(self):
        self.assertFalse(audit({"indexes": [["a"], ["b", "c"]]}))
